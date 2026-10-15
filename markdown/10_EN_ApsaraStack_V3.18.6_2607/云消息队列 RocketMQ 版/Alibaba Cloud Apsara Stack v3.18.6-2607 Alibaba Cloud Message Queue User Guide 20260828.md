---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue User Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 379
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue User Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97%20RocketMQ%20%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Alibaba%20Cloud%20Message%20Queue%20User%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue User Guide 20260828

**1.?**

ApsaraMQ for RocketMQ is a distributed messaging middleware that is developed based on Apache RocketMQ. ApsaraMQ for RocketMQ features low latency, high concurrency, high availability, and high reliability. ApsaraMQ for RocketMQ provides a complete set of cloud messaging services based on the technologies that are used for building highly available and distributed clusters. The messaging services include message subscription and publishing, message tracing, scheduled and delayed messages, and resource statistics. ApsaraMQ for RocketMQ is used as a core service in an enterprise-grade Internet architecture. ApsaraMQ for RocketMQ provides asynchronous decoupling and peak-load shifting capabilities for distributed application systems. It also supports various features for Internet applications, including accumulation of large numbers of messages, high throughput, and reliable message consumption retries. ApsaraMQ for RocketMQ is one of the core cloud services that are used to support the Double 11 Shopping Festival. ApsaraMQ for RocketMQ supports connections over TCP and HTTP and supports multiple programming languages such as Java, C++, and .NET. This allows you to connect applications that are developed in different programming languages to ApsaraMQ for RocketMQ.

## Product updates

This topic describes the updates of ApsaraMQ for RocketMQ from V3.8.0 to V3.18.3 to help you get started with the latest version.

**Optimization of resource isolation by instance**

ApsaraMQ for RocketMQ provides instances for multi-tenancy isolation. Each user can purchase multiple instances and logically isolate them from each other. To ensure the compatibility with the existing resources of existing users, ApsaraMQ for RocketMQ provides the following types of instances and namespaces: Default instances, which are compatible with the existing resources of existing users This type of instance has no separate namespace. Resource names must be globally unique within and across all instances. By default, an instance without a namespace is automatically generated for the existing resources of each existing user. If no existing resources are available, you can create at most one instance without a namespace. You can configure an endpoint, which can be obtained from the **Instance details** page in the ApsaraMQ for RocketMQ console.

```
// Recommended configuration: properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxxx"); // Compatible configuration, which is not recommended. We recommend that you update this configuration to the recommended configuration. properties.put(PropertyKeyConst.ONSAddr, "xxxx");
```

New instances A new instance has a separate namespace. Resource names must be unique within an instance but can be the same across different instances. You can configure an endpoint, which can be obtained from the **Instance details** page in the ApsaraMQ for RocketMQ console.

```
// Recommended configuration: properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxx");
```

Your RocketMQ client must be updated to the following latest versions for different programming languages: Java: 1.8.7.1.Final C and C++: V2.0.0 .NET: 1.1.3

**Optimized procedure for applying for resources**

Previously, ApsaraMQ for RocketMQ resources consisted of topics, producer IDs, and consumer IDs. Each two types of the resources are in a many-to-many relationship, which was difficult to understand. Each time you created a topic, you must associate the topic with a producer ID and a consumer ID. This procedure was complex for medium- and large-sized enterprise customers. To optimize user experience and help new users get started, the procedure for applying for resources has been simplified. The procedure has been optimized in the following aspects: Topic management, which remains unchanged You need to apply for a topic. A topic is used to classify messages. It is the primary classifier. Manage groups You do not need to apply for a producer ID. Producer IDs and consumer IDs are integrated into group IDs. In the ApsaraMQ for RocketMQ console, the Producers module has been removed. The Producers and Consumers modules have been integrated into the Groups module. You do not need to associate a producer ID or consumer ID with a topic. Instead, you only need to apply for a group ID and associate it with a topic in the code. Compatibility: The list of producer IDs is no longer displayed. This does not affect the current services. The consumer IDs that start with CID- or CID_ and that you have applied for can still be used and can be specified in the **PropertyKeyConst.ConsumerId** or
**PropertyKeyConst.GROUP_ID** parameter of the code.
Sample code

**Note**

We recommend that you update your RocketMQ client to the following latest versions for different programming languages: Java: 1.8.7.1.Final C and C++: V2.0.0 .NET: 1.1.3 Existing producer IDs or consumer IDs can still be used and do not affect the current services. However, we recommend that you update your instance configurations to the recommended configurations. Recommended configurations: Integrate producer IDs and consumer IDs into group IDs.

```
// Configure the PropertyKeyConst.GROUP_ID parameter. The original PropertyKeyConst.ProducerId and PropertyKeyConst.ConsumerId parameters are deprecat ed. properties.put(PropertyKeyConst.GROUP_ID, "The original CID-XXX or GID-XXX");
```

Compatible configuration: Use a producer ID to identify a producer and a consumer ID to identify a consumer.

```
// When you create a producer, you must configure the PropertyKeyConst.ProducerId p arameter. properties.put(PropertyKeyConst.ProducerId, "The original PID-XXX or GID-XXX"); // When you create a consumer, you must configure the PropertyKeyConst.ConsumerId p arameter. properties.put(PropertyKeyConst.ConsumerId, "The original CID-XXX or GID-XXX");
```

## Quick start

### Overview

ApsaraMQ for RocketMQ provides TCP client SDKs and HTTP client SDKs for multiple programming languages. You can use the SDKs to send and subscribe to different types of messages. This topic describes how to use TCP client SDKs and HTTP client SDKs for multiple programming languages to send and subscribe to normal messages and the relevant usage notes.

**Background information**

If your application that is deployed on a server uses ApsaraMQ for RocketMQ, we recommend that you use an SDK to access ApsaraMQ for RocketMQ. This method is easy-to-use and provides high availability. This topic provides examples to show how to use the SDK for Java to connect to ApsaraMQ for RocketMQ and send and subscribe to messages over TCP or HTTP. ApsaraMQ for RocketMQ supports four types of messages. For more information, see Message types. In the following examples, normal messages are used. The topics that you create by using the procedure that is described in the following section cannot be used to send or subscribe to other types of messages. Each topic can be used to send and subscribe to messages only of a specific type.

**Process**

You can follow the process illustrated in the following figure based on the protocol that you select.
1. Create resources. You must create a ApsaraMQ for RocketMQ instance, a topic, and a
group, and obtain the endpoint information of the instance.
2. Use the corresponding SDK to send and subscribe to messages based on the protocol that
you select. Use the TCP client SDK for Java to send and subscribe to normal messages Use the HTTP client SDK for Java to send and subscribe to normal messages

**Usage notes**

ApsaraMQ for RocketMQ provides TCP and HTTP client SDKs for you to send and receive messages. You cannot specify the same group ID in the code of a TCP client SDK and the code of an HTTP client SDK at the same time. If you want to use a TCP client SDK to send and receive messages, you must create a group for the TCP protocol. You cannot specify a group that is created for the HTTP protocol in the code of the TCP client SDK. An ApsaraMQ for RocketMQ instance provides a TCP endpoint and an HTTP endpoint. An endpoint for a specific protocol must be used together with an SDK for the same protocol. For example, if you want to use a TCP client SDK to send and receive messages, you must obtain the TCP endpoint of your ApsaraMQ for RocketMQ instance. You cannot use the HTTP endpoint to connect to the instance.

**References**

For information about how to use TCP client SDKs and HTTP client SDKs for other programming languages to send and subscribe to messages, see the following topics:

**TCP**

C and C++: Send and subscribe to normal messages .NET: Send and subscribe to normal messages

**HTTP**

Go: Send and consume normal messages Python: Send and consume normal messages Node.js: Send and consume normal messages PHP: Send and consume normal messages C#: Send and consume normal messages C++: Send and consume normal messages

### Log on to the console

This topic describes how to log on to the ApsaraMQ for RocketMQ console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser.

**Procedure**

1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press
the Enter key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator.

**Note**

When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click **Login**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: It is the first time that you log on to the console after MFA is forcibly enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the account and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA authentication code and click **Authenticate**.

**Note**

For more information, see the **Bind a virtual MFA device to enable**
**MFA** topic in **Apsara Uni-manager Operations Console User Guide** .
5. In the top navigation bar, choose **Products > Middleware > ApsaraMQ for RocketMQ**.

### Create resources

Before you use a client SDK to send and receive messages, you must create the required resources and obtain the resource information in the ApsaraMQ for RocketMQ console. When you use the SDK, you must configure the resource parameters based on the resource information.

**Background information**

If a new application needs to access ApsaraMQ for RocketMQ, you must create the following ApsaraMQ for RocketMQ resources for the application:
**Instance**: An instance is a VM resource of ApsaraMQ for RocketMQ used to store
information about topics and group IDs.
**Topic**: topics. In ApsaraMQ for RocketMQ, a producer sends a message to a specific topic,
and a consumer subscribes to the topic to obtain and consume the message.
**Group ID**: A group ID is used to identify a group of producers or consumers.

**Important**

A TCP client cannot share a group with an HTTP client. You must create different groups for different protocols. For example, if you use a TCP client SDK to send and receive messages, you must use the group that is created only for TCP clients.
**Endpoint**: You can use an endpoint to connect producer or consumer clients to a specific
ApsaraMQ for RocketMQ instance.

**Important**

An ApsaraMQ for RocketMQ instance has a TCP endpoint and an HTTP endpoint. Each endpoint can be used only for clients over the same protocol. For example, if you use a TCP client SDK to send and receive messages, you must specify the TCP endpoint, instead of the HTTP endpoint, in the SDK code.
**AccessKey ID and AccessKey secret**: the user credentials that are used to verify the
identity of the user. For more information about how to obtain an AccessKey pair, see the
**Obtain an AccessKey pair** topic in ApsaraMQ for RocketMQ **Developer Guide**.

**Create an instance**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, click **Create an instance**.
4. On the **Create an MQ 4.0 instance** page, configure the parameters and click **Submit**.
The following table describes the parameters.

| Parameter |   | Description | Example |
|---|---|---|---|
| Region | Organization | The organization to which the instance belongs. | root test _ |
|   | Resource Set | The resource set to which the instance belongs. | DefaultResource |
|   | Region | The region in which you want to create the instance. | cn-qingdao- env66-d01 |
|   | Chip Architecture | The chip type of the instance that you want to create. By default, the type of the chip used by the instance is the same as that of the chip deployed in the ApsaraMQ for RocketMQ cluster. You cannot modify this parameter. Valid values: intel Kunpeng Hygon Phytium Yitian ShenWei | intel |
|   | Cluster | The cluster in which you want to create the instance. | cluster1 |
|   | Instance Name | The name of the instance. The name must be 3 to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores ( ). _ | test |
|   | Maximum Number of Topics | The maximum number of topics that can be created on the instance. If you no longer need a topic, delete the topic at the earliest opportunity. Value values: 10 to 5000. Default value: 50. | 50 |

| Basic Configuration |   |   |   |
|---|---|---|---|
|   | Message Sending TPS | The maximum transactions per second (TPS) for sending messages on the instance. If the throttling feature is enabled for the instance, the instance is throttled when the actual TPS for sending messages exceeds the specified threshold. By default, the throttling feature is disabled for an instance. For information about how to enable the feature, see the Instance throttling topic of ApsaraMQ for RocketMQ O&M Guide. Valid values: 500 to 30000. Default value: 500. | 500 |
|   | Message Subscription TPS | The maximum TPS for subscribing to messages in the instance. Valid values: 500 to 30000. Default value: 500. | 500 |
|   | Description | The description of the instance. The description must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), _ hyphens (-), and colons (:). It must start with a letter and cannot start with http:// or https://. | test |

5. **Optional.** If you configured a review workflow, you also need to perform the following
operations: i. In the **Process Information Supplement** dialog box, select a value for the **Execution**
**Method After Approval** parameter, specify a reason in the **Operation Reason** field,
and then click **Submit For Approval**. ii. In the **Operation Succeeded** message, click **Application Form Details** to go to the details page. iii. In the **Approval Progress of Application Form** section of the details page, click **View**
**All** to open the **Approval Progress of Application Form** panel and view the progress
of the review workflow. The review workflow is complete only after all steps are performed. On the **Instance List** page, you can view the instance that you created.

**Obtain an endpoint**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
3. On the **Instance details** page, click the **Network Management** tab. On this tab, view the
endpoint information of the instance.
**TCP client access point**: If you want to use a TCP client SDK to send and receive
messages, specify the TCP endpoint in the code.
**HTTP Endpoint**: If you want to use an HTTP client SDK to send and receive messages,
specify the HTTP endpoint in the code.

**Create a topic**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Topic Management** tab.
5. Click **Create a Topic**.
6. In the **Create a Topic** dialog box, configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| Topic | The name of the topic. The topic name can contain only letters, digits, hyphens (-), and underscores ( ). _ It must be 3 to 64 characters in length. The topic name must be different from existing topic names and group IDs. |
| Message Type | The message type. Important ApsaraMQ for RocketMQ supports the following types of messages: normal messages, ordered messages, scheduled messages, delayed messages, and transactional messages. When you create a topic, the message type that you select for the topic must be consistent with the type of messages that the topic sends and receives. Otherwise, messages may fail to be sent and received. |
| Description | The description of the topic. |

**Create a group**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Group Management** tab.
5. Select a protocol for the group that you want to create.
If you want to use TCP-based SDKs to send and receive messages, click the **TCP protocol** tab. If you want to use HTTP-based SDKs to send and receive messages, click the **HTTP**
**protocol** tab.
6. Click **Create Group ID**. In the **Create Group ID** dialog box, configure the parameters and
click **OK**.

| Parameter | Description |
|---|---|
| Group ID | The group ID. The group ID can contain only letters, digits, hyphens (-), and underscores ( ). _ It must be 4 to 64 characters in length. The group ID cannot be modified after it is created. The group ID must be different from existing topic names and group IDs. |
| Description | The description of the group. |

**Note**

A group ID can be used for producers to identify the same type of producer instance. In this case, the group ID is a producer group ID. A group ID can also be used for consumers to identify the same type of consumer instance. In this case, the group ID is a consumer group ID. TCP-based SDKs and HTTP-based SDKs cannot share the same group ID. Create separate group IDs for TCP-based SDKs and HTTP-based SDKs.

### Send messages

#### Use the TCP client SDK for Java to send

**and subscribe to normal messages**

After you create the required resources in the ApsaraMQ for RocketMQ console, you can use ApsaraMQ for RocketMQ TCP client SDKs to send and subscribe to normal messages.

**Prerequisites**

Required resources are created. For more information, see Create resources.

**Install ApsaraMQ for RocketMQ SDK for Java**

You can use one of the following methods to install ApsaraMQ for RocketMQ SDK for Java:

**Import Maven dependencies**

```xml
<dependency>
   <groupId>com.aliyun.openservices</groupId>
   <artifactId>ons-client</artifactId>
   <!-- Specify the version of ApsaraMQ for RocketMQ SDK for Java. -->
   <version>"XXX"</version>
</dependency>
```

**Download the JAR file that contains the dependencies**

For more information, see Overview.

**Use the TCP client SDK for Java to send normal messages**

The following sample code provides an example on how to use the TCP client SDK for Java to send normal messages. Before you run the code, we recommend that you specify the information about the required resources that are created in advance based on the comments included in the code.

```java
 import com.aliyun.openservices.ons.api.Message;
 import com.aliyun.openservices.ons.api.Producer;
 import com.aliyun.openservices.ons.api.SendResult;
 import com.aliyun.openservices.ons.api.ONSFactory;
 import com.aliyun.openservices.ons.api.PropertyKeyConst;
 import java.util.Properties;
 public class ProducerTest {
     public static void main(String[] args) {
         Properties properties = new Properties();
         // Specify the ID of the group that you created for TCP clients in the
ApsaraMQ for RocketMQ console.
         properties.put(PropertyKeyConst.GROUP_ID, "XXX");
         // Specify your AccessKey ID. The AccessKey ID is used for identity
authentication.
         properties.put(PropertyKeyConst.AccessKey,"XXX");
         // Specify your AccessKey secret. The AccessKey secret is used for identity au
thentication.
         properties.put(PropertyKeyConst.SecretKey, "XXX");
         // Specify the TCP endpoint of your instance. You can view the TCP endpoint on
the Network Management tab of the Instance details page in the ApsaraMQ for RocketMQ co nsole.
         properties.put(PropertyKeyConst.NAMESRV_ADDR,"XXX");
         Producer producer = ONSFactory.createProducer(properties);
         // Before you send a message, call the start() method only once to start the p
roducer.
         producer.start();
         // Cyclically send messages.
         while(true){
             Message msg = new Message(
                 // Specify the topic that you created in the ApsaraMQ for RocketMQ
console. The value is the name of the topic to which you want to send messages.
                 "TopicTestMQ",
                 // Message Tag,
                 // Specify a message tag, which is similar to a Gmail tag. It is used t
o sort messages and help the consumer filter messages on the ApsaraMQ for RocketMQ broker based on specified conditions.
                 "TagA",
                 // Message Body
```

```java
                 // Specify the message body in the binary format. ApsaraMQ for
RocketMQ does not process the message body.
                 // The producer and consumer must agree on the methods that are used
to serialize and deserialize message bodies.
                 "Hello MQ".getBytes());
             // Specify a message key. The message key is the business-specific
attribute of the message and must be globally unique. A unique key helps you query and resend a message in the console if the message fails to be received.
             // Note: A message can be sent and received even if you do not specify a m
essage key.
             msg.setKey("ORDERID_100");
             // Send the message. If no exception is thrown, the message is sent.
             // Print the message ID. The message ID can be used to query the sending
status of the message.
             SendResult sendResult = producer.send(msg);
             System.out.println("Send Message success. Message ID is: " +
sendResult.getMessageId());
         // Before you exit the application, shut down the producer.
         // Note: This operation is optional.
         producer.shutdown();
```

You can also send messages by performing the following operations in the ApsaraMQ for RocketMQ console: On the **Topic management** page, find the topic that you created, and click **Send message** in the **Operation** column.

**Use the TCP client SDK for Java to subscribe to normal**

**messages**

The following sample code provides an example on how to use the TCP client SDK for Java to subscribe to normal messages. Before you run the code, we recommend that you specify the information about the required resources that are created in advance based on the comments included in the code.

```java
import com.aliyun.openservices.ons.api.Action; import com.aliyun.openservices.ons.api.ConsumeContext; import com.aliyun.openservices.ons.api.Consumer; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.MessageListener; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import java.util.Properties; public class ConsumerTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
        // Specify the ID of the group that you created for TCP clients in the ApsaraMQ
for RocketMQ console.
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
        // Specify your AccessKey ID. The AccessKey ID is used for identity
authentication.
         properties.put(PropertyKeyConst.AccessKey,"XXX");
         // Specify your AccessKey secret. The AccessKey secret is used for identity au
thentication.
         properties.put(PropertyKeyConst.SecretKey, "XXX");
         // Specify the TCP endpoint of your instance. You can view the TCP endpoint on
the Network Management tab of the Instance details page in the ApsaraMQ for RocketMQ co nsole.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,"XXX");
        Consumer consumer = ONSFactory.createConsumer(properties);
        consumer.subscribe("TopicTestMQ", "*", new MessageListener() {
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
        });
        consumer.start();
        System.out.println("Consumer Started");
```

**Check whether message subscription is successful**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Group management** tab.
5. In the group list, find the group ID for the consumer of which you want to view the
subscription, and click **Subscription relationship** in the **Operation** column. If the value of the **Online or not** parameter is **Yes**, the consumer has been started and the subscription is successful. Otherwise, the subscription fails.

**What to do next**

Query messages Query a message trace

#### Use the HTTP client SDK for Java to

##### send and subscribe to normal messages

After you create the required resources in the ApsaraMQ for RocketMQ console, you can use ApsaraMQ for RocketMQ HTTP client SDK for Java to send and subscribe to normal messages.

**Before you begin**

Create resources

**Install ApsaraMQ for RocketMQ SDK for Java**

You can use one of the following methods to install ApsaraMQ for RocketMQ SDK for Java:

**Introduce a dependency by using Maven:**

```xml
<dependency>
    <groupId>com.aliyun.mq</groupId>
    <artifactId>mq-http-sdk</artifactId>
    <!-- Set the value to the version of ApsaraMQ for RocketMQ SDK for Java. -->
    <version>X.X.X</version>
    <classifier>jar-with-dependencies</classifier>
</dependency>
```

**Download a JAR file that contains a dependency**

For more information about the download link, see Overview.

**Use the HTTP client SDK for Java to send normal messages**

The following sample code provides an example on how to use the HTTP client SDK for Java to send normal messages. Before you run the code, we recommend that you specify the information about the required resources that are created in advance based on the comments included in the code.

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQProducer; import com.aliyun.mq.http.model.TopicMessage; import java.util.Date; public class Producer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
                // Specify the HTTP endpoint of your instance. To view the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console and go to the Network Management tab of the Instances page.
                "${HTTP_ENDPOINT}",
                // Specify the AccessKey ID for identity verification.
                "${ACCESS_KEY}",
                // Specify the AccessKey secret for identity verification.
                "${SECRET_KEY}"
```

`)` );

```
        // Specify the topic that you created in the ApsaraMQ for RocketMQ console. The
value is the name of the topic to which you want to send messages.
        final String topic = "${TOPIC}";
        // Specify the ID of the instance on which the topic is created.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the ApsaraMQ for R ocketMQ console.
        final String instanceId = "${INSTANCE_ID}";
        // Obtain the producer that sends messages to the topic.
        MQProducer producer;
        if (instanceId != null && instanceId != "") {
            producer = mqClient.getProducer(instanceId, topic);
        } else {
            producer = mqClient.getProducer(topic);
        try {
            // Cyclically send four messages.
            for (int i = 0; i < 4; i++) {
                TopicMessage pubMsg;        // Specify the normal message.
                pubMsg = new TopicMessage(
                // Specify the content of the message.
                "hello mq!".getBytes(),
                // Specify the message tag.
                "A"
```

);

```java
                // Specify the custom attributes of the message.
                pubMsg.getProperties().put("a", String.valueOf(i));
                // Specify the key of the message.
                pubMsg.setMessageKey("MessageKey");
            // Send the message in synchronous mode. If no exception is thrown, the
message is sent.
            TopicMessage pubResultMsg = producer.publishMessage(pubMsg);
            // Send the message in synchronous mode. If no exception is thrown, the
message is sent.
            System.out.println(new Date() + " Send mq message success. Topic is:" +
topic + ", msgId is: " + pubResultMsg.getMessageId()
                        + ", bodyMD5 is: " + pubResultMsg.getMessageBodyMD5());
        } catch (Throwable e) {
            // Specify the logic that you want to use to resend or persist the message
if the message fails to be sent and needs to be sent again.
            System.out.println(new Date() + " Send mq message failed. Topic is:" +
topic);
            e.printStackTrace();
        mqClient.close();
```

You can also send messages by performing the following operations in the ApsaraMQ for RocketMQ console: Log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Topics. On the **Topics** page, find the topic that you created, and click **Send**
**Message** in the **Actions** column.

**Use the HTTP client SDK for Java to subscribe to normal**

**messages**

The following sample code provides an example on how to use the HTTP client SDK for Java to subscribe to normal messages. Before you run the code, we recommend that you specify the information about the required resources that are created in advance based on the comments included in the code.

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQConsumer; import com.aliyun.mq.http.common.AckMessageException; import com.aliyun.mq.http.model.Message; import java.util.ArrayList; import java.util.List; public class Consumer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
                // Specify the HTTP endpoint of your instance. To view the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console and go to the Network Management tab of the Instances page.
                "${HTTP_ENDPOINT}",
                // Specify the AccessKey ID for identity verification.
                "${ACCESS_KEY}",
                // Specify the AccessKey secret for identity verification.
                "${SECRET_KEY}"
```

);

```
        // Specify the topic that you created in the ApsaraMQ for RocketMQ console. The
value is the name of the topic from which you want to consume messages.
        final String topic = "${TOPIC}";
        // Specify the ID of the group that you created for HTTP clients in the
ApsaraMQ for RocketMQ console.
        final String groupId = "${GROUP_ID}";
        // Specify the ID of the instance on which the topic is created.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        final String instanceId = "${INSTANCE_ID}";
        final MQConsumer consumer;
        if (instanceId != null && instanceId != "") {
            consumer = mqClient.getConsumer(instanceId, topic, groupId, null);
}else{
```

```
        } else {
            consumer = mqClient.getConsumer(topic, groupId);
        // Cyclically consume messages in the current thread. We recommend that you use
multiple threads to concurrently consume messages.
        do {
            List<Message> messages = null;
            try {
                // Consume messages in long polling mode.
                // In long polling mode, if no message in the topic is available for con
sumption, the request is suspended on the broker for a specified period of time. If a m essage becomes available for consumption within this period, the broker immediately sen ds a response to the consumer. In this example, the period is set to 3 seconds.
                messages = consumer.consumeMessage(
                        3,// Specify the maximum number of messages that can be consumed
at a time. In this example, the value is set to 3. The maximum value that you can speci fy is 16.
                        3// Specify the duration of a long polling cycle. Unit: seconds.
In this example, the value is set to 3. The maximum value that you can specify is 30.
```

);

```java
            } catch (Throwable e) {
                e.printStackTrace();
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e1) {
                    e1.printStackTrace();
            // No messages in the topic are available for consumption.
            if (messages == null || messages.isEmpty()) {
                System.out.println(Thread.currentThread().getName() + ": no new message,
continue!");
                continue;
            // Specify the message consumption logic.
            for (Message message : messages) {
                System.out.println("Receive message: " + message);
            // If the broker does not receive an acknowledgment (ACK) for a message
from the consumer before the delivery retry interval elapses, the broker sends the message for consumption again.
            // A unique timestamp is specified for the handle of a message each time th
e message is consumed.
```

`{`

```
                List<String> handles = new ArrayList<String>();
                for (Message message : messages) {
                    handles.add(message.getReceiptHandle());
                try {
                    consumer.ackMessage(handles);
```

```java
cosue.ac essage(ades);
                } catch (Throwable e) {
                    // If the handle of a message times out, the broker cannot receive a
n ACK for the message from the consumer.
                    if (e instanceof AckMessageException) {
                        AckMessageException errors = (AckMessageException) e;
                        System.out.println("Ack message fail, requestId is:" +
errors.getRequestId() + ", fail handles:");
                        if (errors.getErrorMessages() != null) {
                            for (String errorHandle :errors.getErrorMessages().keySet())
```

`{`

```java
                                System.out.println("Handle:" + errorHandle + ",
ErrorCode:" + errors.getErrorMessages().get(errorHandle).getErrorCode()
                                        + ", ErrorMsg:" +
errors.getErrorMessages().get(errorHandle).getErrorMessage());
                        continue;
                    e.printStackTrace();
        } while (true);
```

**Check whether message subscription is successful**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Group management** tab.
5. In the group list, find the group ID for the consumer of which you want to view the
subscription, and click **Subscription relationship** in the **Operation** column. If the value of the **Online or not** parameter is **Yes**, the consumer has been started and the subscription is successful. Otherwise, the subscription fails.

**What to do next**

Query messages Query a message trace

#### Check whether messages are sent

After you send a message, you can check the status of the message in the ApsaraMQ for RocketMQ console.

**Procedure**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Message query** tab.
5. On the **Message query** page, click the **Query By Message ID** tab.
6. In the search box, enter the **topic** name that corresponds to the message and the
**message ID** returned after the message is sent, and click **Query** to query the sending
status of the message.
**Storage time** indicates the time when the message is stored on the ApsaraMQ for
RocketMQ broker. If the message appears in the search results, the message has been sent to the ApsaraMQ for RocketMQ broker.

**Important**

This step demonstrates the situation where ApsaraMQ for RocketMQ is used for the first time and the consumer has never been started. Therefore, no consumption data is displayed in the message status information.

**What to do next**

You can start the consumer and subscribe to messages. For more information, see Subscribe to messages. For more information about message states, see Message query and Status in message traces.

### Subscribe to messages

After a message is sent, the consumer can subscribe to the message. You must use the SDK corresponding to the protocol and programming language to subscribe to the message. This topic describes how to use ApsaraMQ for RocketMQ TCP client SDK for Java to subscribe to messages.

**Procedure**

1. Run the following sample code to test the message subscription feature. Specify
parameters based on the descriptions before you run the code.

```java
import com.aliyun.openservices.ons.api.Action; import com.aliyun.openservices.ons.api.ConsumeContext; import com.aliyun.openservices.ons.api.Consumer; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.MessageListener; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import java.util.Properties; public class ConsumerTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
        // The ID of the consumer group that you created in the ApsaraMQ for RocketMQ
console.
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
        // The AccessKey ID used for identity authentication.
        properties.put(PropertyKeyConst.AccessKey, "XXX");
        // The AccessKey secret used for identity authentication.
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The TCP endpoint. To obtain the endpoint, log on to the ApsaraMQ for Rocke
tMQ console. In the left-side navigation pane, click Instances. On the Instance List page, click the ID of the instance that you want to manage to go to the instance deta ils page. On the Network Management tab, view the TCP endpoint in the TCP client acce ss point section.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,"XXX");
        Consumer consumer = ONSFactory.createConsumer(properties);
        consumer.subscribe("TopicTestMQ", "*", new MessageListener() {
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
        });
        consumer.start();
        System.out.println("Consumer Started");
```

After you run the code, you can check whether the consumer is started in the ApsaraMQ for RocketMQ console. This operation checks whether the message subscription is successful.
2. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
3. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
4. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
5. On the **Instance details** page, click the **Group management** tab.
6. In the group list, find the group ID for the consumer of which you want to view the
subscription, and click **Subscription relationship** in the **Operation** column. If the value of the **Online or not** parameter is **Yes**, the consumer has been started and the subscription is successful. Otherwise, the subscription fails.

## Message types

### Normal messages

This topic describes the definition of normal messages and provides the sample code for sending and subscribing to normal messages. In ApsaraMQ for RocketMQ, normal messages do not have special features. They are different from the following featured messages: scheduled messages, delayed messages, ordered messages, and transactional messages. For more information about these featured messages, see Scheduled messages and delayed messages, Ordered messages, and Transactional messages. The following sample code provide examples on how to use TCP client SDKs and HTTP client SDKs for different programming languages to send and subscribe to normal messages:

**Sample code for using TCP client SDKs**

For information about the sample code for using TCP client SDKs to send and subscribe to normal messages, see the following topics: The SDK for Java: Overview Send messages by using multiple threads Subscribe to messages The SDK for C and the SDK for C++: Send and subscribe to normal messages The SDK for .NET: Send and subscribe to normal messages

**Sample code for using HTTP client SDKs**

For information about the sample code for using HTTP client SDKs to send and subscribe to normal messages, see the following topics: The SDK for Java: Send and subscribe to normal messages The SDK for Go: Send and subscribe to normal messages The SDK for Python: Send and subscribe to normal messages The SDK for Node.js: Send and subscribe to normal messages The SDK for PHP: Send and subscribe to normal messages The SDK for C#: Send and subscribe to normal messages The SDK for C++: Send and subscribe to normal messages

### Scheduled messages and

**delayed messages**

This topic introduces the concepts related to scheduled messages and delayed messages and describes the scenarios, usage, and usage notes of these messages in ApsaraMQ for RocketMQ.

**Concepts**

Scheduled message: A scheduled message is not immediately sent to consumers after the ApsaraMQ for RocketMQ broker receives the message from the producer. The broker is configured to send the message to consumers at a specific point in time later than the current time. Delayed message: A delayed message is not immediately sent to consumers after the ApsaraMQ for RocketMQ broker receives the message. The broker is configured to send the message to consumers after a specific period of time elapses. Scheduled messages and delayed messages are slightly different in coding, but are consistent in the effect. Scheduled messages and delayed messages are not immediately sent to consumers after the ApsaraMQ for RocketMQ broker receives the messages. These messages are sent to consumers after being delayed for a specific period of time, which is specified in the attributes of the messages.

**Scenarios**

Scheduled messages and delayed messages can be used in the following scenarios: A time window between message production and message consumption is required. For example, when a transaction order is created on an e-commerce platform, a producer sends a delayed message to the ApsaraMQ for RocketMQ broker. A delay of 30 minutes is specified for the message to be sent to a consumer. The message is used to remind the consumer to check whether the order is paid. If the order is not paid, the related system closes the order. If the order is paid, the consumer ignores the message. Scheduled messages are sent to trigger scheduled tasks. For example, a notification message is sent to a user at a specified point in time.

**Usage**

Scheduled messages and delayed messages are slightly different in coding. To send a scheduled message, specify a point in time that is later than the point in time when the message is sent by a producer. The broker sends the message to consumers at the specified point in time. To send a delayed message, specify a period of time that starts from the point in time when the message is sent by a producer. The broker sends the message to consumers after the specified period of time elapses.

**Usage notes**

The **msg.setStartDeliverTime** parameter for a scheduled message or a delayed message must be set to a specific point in time after the current timestamp. Unit: milliseconds. If the scheduled time is earlier than the current time, the message is immediately sent to the consumer. The **msg.setStartDeliverTime** parameter for a scheduled message or a delayed message can be set to a specific point in time within 40 days after the scheduled message or the delayed message is generated. Unit: milliseconds. If the specified point in time is not within the 40 days, the message cannot be sent. The **StartDeliverTime** parameter specifies the time when the ApsaraMQ for RocketMQ broker starts to send the message to the consumer. If messages have been accumulated for the consumer, the scheduled message or the delayed message are queued after the accumulated messages, and are not sent to the consumer at the specified time. Due to the potential time difference between the producer and the broker, the actual delivery time may be different from the delivery time specified in the producer. Scheduled messages and delayed messages can be retained for at most three days on the ApsaraMQ for RocketMQ broker. For example, a message is scheduled to be consumed in 5 days. If the message is not consumed after 5 days, the message will be deleted on the eighth day.

**Sample code for using TCP client SDKs**

For information about the sample code for using TCP client SDKs to send and subscribe to scheduled messages or delayed messages, see the following topics: Java SDK Send and subscribe to scheduled messages Send and subscribe to delayed messages The SDK for C++: Send and subscribe to scheduled messages The SDK for .NET: Send and subscribe to scheduled messages

**Sample code for using HTTP client SDKs**

For information about the sample code for using HTTP client SDKs to send and subscribe to scheduled messages and delayed messages, see the following topics: The SDK for Java: Send and subscribe to scheduled messages and delayed messages The SDK for Go: Send and consume scheduled messages and delayed messages The SDK for Python: Send and consume scheduled messages and delayed messages The SDK for Node.js: Send and consume scheduled messages and delayed messages The SDK for PHP: Send and consume scheduled messages and delayed messages The SDK for C#: Send and consume scheduled messages and delayed messages The SDK for C++: Send and consume scheduled messages and delayed messages

### Transactional messages

This topic introduces the terms that are related to transactional messages in ApsaraMQ for RocketMQ. This topic also describes the scenarios, methods, and usage notes of using transactional messages.

**Terms**

Transactional message: ApsaraMQ for RocketMQ provides a distributed transaction processing feature that is similar to X/Open XA to ensure transaction consistency by using transactional messages. Half transactional message: A half transactional message is a message that cannot be sent to consumers by the ApsaraMQ for RocketMQ broker. If a ApsaraMQ for RocketMQ broker receives a message from a producer and does not receive the second acknowledgment (ACK) from the producer, the message is temporarily undeliverable. A message in this state is called a half transactional message. Message status check: In scenarios such as a transient connection occurs in the network or the producer application is restarted, the ApsaraMQ for RocketMQ broker does not receive the second ACK for a transactional message. When the ApsaraMQ for RocketMQ broker finds that a message remains as a half transactional message for an excessive long period of time, the broker sends a request to the producer to check whether the final status of the message is Commit or Rollback.

**Common scenarios**

ApsaraMQ for RocketMQ allows you to use transactional messages in the following scenarios: The distributed transaction processing feature provided by ApsaraMQ for RocketMQ can be used to ensure transaction consistency based on transactional messages. The distributed transaction processing feature is similar to X/Open XA. For example, an e-commerce platform provides a shopping cart system and a transaction system. When customers use the shopping cart to place orders, the customer entry point is the shopping cart system, and the entry point for order placement is the transaction system. Data in the two systems must be eventually consistent. In this case, transactional messages can be used. After an order is placed, the transaction system sends a transactional message about the order to ApsaraMQ for RocketMQ. The shopping cart system subscribes to the transactional message about the order from ApsaraMQ for RocketMQ, performs the required operations, and then updates data.

**How to use transactional messages**

Interaction process The following figure shows the process of using transactional messages in ApsaraMQ for RocketMQ. The procedure to send a transactional message includes the following steps:
1. A producer sends a message to the ApsaraMQ for RocketMQ broker.
2. The ApsaraMQ for RocketMQ broker persists the message and sends an ACK to the
producer. At this stage, the message is a half transactional message.
3. The producer executes a local transaction.
4. The producer sends an ACK to the ApsaraMQ for RocketMQ broker to submit the execution
result of the local transaction. In the execution result, the status of the transaction may be Commit or Rollback. If the status of the transaction is Commit, the broker marks the half transactional message as deliverable. Then, consumers can consume the message. If the status of the transaction is Rollback, the broker deletes the message. In this case, consumers cannot consume the message. The following list describes how to check the status of a transactional message: If the ApsaraMQ for RocketMQ broker does not receive an ACK from the producer because the network is disconnected or the message producer application is restarted, the ApsaraMQ for RocketMQ broker sends a request to query the status of the message after a specific period of time. After the producer receives the request, the producer checks the final status of the local transaction that corresponds to the message. The producer sends a new ACK to the ApsaraMQ for RocketMQ broker based on the final status of the local transaction. The broker processes the half transactional message based on the content of the ACK. For more information, see Step 4.

**Usage notes**

1. Producers of transactional messages cannot be in the same group to which producers of
messages of other types belong. ApsaraMQ for RocketMQ brokers perform status check operations for transactional messages based on the IDs of the groups to which the producers belong.
2. You must specify the implementation class of the **LocalTransactionChecker** method
when you call **ONSFactory.createTransactionProducer** to create a transactional message producer. This way, the broker can check the status of transactional messages after exceptions occur.
3. After the local transaction that corresponds to a transactional message is executed, the
**execute** method returns one of the following results:
**TransactionStatus.CommitTransaction**: The transaction is committed. The message
can be consumed by consumers.
**TransactionStatus.RollbackTransaction**: The transaction is rolled back. The message
is discarded and cannot be consumed.
**TransactionStatus.Unknow:** The transaction is in an unknown state. The ApsaraMQ for
RocketMQ broker is expected to send a request to the producer to check the status of the transaction again after a specific period of time.

**Sample code for using TCP SDKs**

For information about sample code, see the following references: SDK for Java: Send and receive transactional messages SDK for C and C++: Send and receive transactional messages SDK for .NET: Send and receive transactional messages

**Sample code for using HTTP-based SDKs**

For information about sample code, see the following references: SDK for Java: Send and consume transactional messages SDK for Go: Send and consume transactional messages SDK for Python: Send and consume transactional messages SDK for Node.js: Send and consume transactional messages SDK for PHP: Send and consume transactional messages SDK for C#: Send and consume transactional messages SDK for C++: Send and consume transactional messages

### Ordered messages

Ordered messages are consumed in the same order in which they are sent. The earliest message that is sent is consumed as the first message, and the message that is sent next is consumed later. In most cases, ordered messages are used in scenarios that require messages to be consumed in the order in which the messages are produced. For example, ordered messages are frequently used in the financial security and e-commerce industries. This topic describes the terms, scenarios, working mechanism, and usage notes of ordered messages in ApsaraMQ for RocketMQ.

**What is an ordered message?**

**Definition**

Ordered messages are a type of messages provided by ApsaraMQ for RocketMQ. Messages of this type are delivered and consumed in a strict first-in, first-out (FIFO) order in a topic. All messages in a specific topic of an ApsaraMQ for RocketMQ instance are partitioned based on a sharding key. The messages in each partition are published and consumed in a FIFO order. FIFO order applies only to messages in the same partition. No limits are imposed on the publishing and consumption of messages across partitions. Therefore, ordered messages in ApsaraMQ for RocketMQ are also known as partitionally ordered messages.

**Terms**

Sharding key: the key field used in ordered messages to identify partitions in a topic. This field is different from the key of a normal message. ApsaraMQ for RocketMQ routes messages that contain the same sharding key to a partition. The earliest published message in the partition is consumed as the first message. Partition: topic-level partitions. Each topic contains one or more partitions. Messages in a topic are distributed in partitions. Logical partitions in this topic are topic-level partitions. Physical partition: the physical unit used to store messages. Each physical partition is created on a specific node of a broker.

**Scenarios**

In most cases, ordered messages are used in scenarios that require messages to be consumed in the order in which the messages are produced. For example, ordered messages are frequently used in the financial security and e-commerce industries. Examples: If a verification code is required for user registration and the user ID is used as the sharding key, the messages that are sent by the same user are published and consumed in a FIFO order. In an e-commerce scenario, if the order ID is used as the sharding key, messages for the creation, payment, and refund of the same order are published and consumed in a FIFO order.

**Working mechanism**

To ensure that messages are sent and consumed in a FIFO order in ApsaraMQ for RocketMQ, you must pay attention to the following phases:

**Message sending**

In the preceding figure, messages for Orders A and B are produced in the following sequence: A1, B1, A2, A3, B2, and B3. The messages for the same order must be sent and consumed in the same sequence in which the messages are produced. For example, the messages for Order A are sent and consumed in the following sequence: A1, A2, and A3. Normal messages for Order A may be sent to different queues in polling mode. The original order of the normal messages cannot be retained in the queues. Ordered messages that use the same sharding key such as the same order ID are sequentially routed to the same partition in ApsaraMQ for RocketMQ. An ApsaraMQ for RocketMQ broker uses the time order in which messages are produced by the same producer to determine the message order. An ApsaraMQ for RocketMQ broker cannot determine the order of the messages that are sent in parallel by different producers or threads.

**Message storage**

In the preceding figure, each logical partition corresponds to a physical partition. When messages are sent to the logical partitions in order, the messages are stored in the corresponding physical partitions in the same order.

**Message consumption**

ApsaraMQ for RocketMQ delivers messages to a consumer in the order in which the messages are stored. Then, the consumers consume the messages from the earliest received message. When consumers consume messages, messages that contain the same sharding key are consumed by using a single thread. This helps ensure the consistency between the message consumption order and the message storage order, and the consistency between the message consumption order and the message publishing order.

**Message types**

| Message type | Performance | Reliable synchronous transmission | Reliable asynchronous transmission | One-way transmission |
|---|---|---|---|---|
| Unordered messages, including normal messages, transactional messages, scheduled messages, and delayed messages | High | Supported | Supported | Supported |
| Ordered messages | Moderate | Supported | Not supported | Not supported |

**Usage notes**

Each group corresponds to a topic type. A group cannot be used to send or receive both ordered messages and unordered messages. Ordered messages cannot be published in a broadcasting manner. Ordered messages cannot be sent in asynchronous mode. If ordered messages are sent in asynchronous mode, messages may be disordered.

**Sample code for using TCP client SDKs**

For information about sample code for using TCP client SDKs to send and receive ordered messages, see the following topics: SDK for Java: Send and receive ordered messages SDK for C/C++: Send and receive ordered messages SDK for .NET: Send and subscribe to ordered messages

**Sample code for using HTTP client SDKs**

For information about sample code for using HTTP client SDKs to send and receive ordered messages, see the following topics: SDK for Java: Send and consume ordered messages SDK for Go: Send and consume ordered messages SDK for Python: Send and consume ordered messages SDK for Node.js: Send and consume ordered messages SDK for PHP: Send and consume ordered messages SDK for C#: Send and consume ordered messages SDK for C++: Send and consume ordered messages

## Console guide

### Resource management

#### Overview

This topic describes how to manage resources in ApsaraMQ for RocketMQ. If a new application needs to access ApsaraMQ for RocketMQ, you must create the following ApsaraMQ for RocketMQ resources for the application: Instance: As a virtual machine (VM) resource of ApsaraMQ for RocketMQ, an instance stores information about topics and group IDs. Topic: In ApsaraMQ for RocketMQ, a producer sends a message to a specific topic, and a consumer subscribes to the topic to obtain and consume the message. Group ID: A group ID is used to identify a group of producers or consumers. You can add, delete, modify, and query the preceding resources in the ApsaraMQ for RocketMQ console or by calling API operations. You can also configure approval workflows for operations performed on the resources. This helps standardize the management process of the resources. When you use an SDK to send and receive messages, you must specify the information about the topic and group that you created in the ApsaraMQ for RocketMQ console. You must also enter the AccessKey ID and AccessKey secret that you created in the Apsara Uni-manager Management Console for identity authentication. If you have not obtained the AccessKey ID and AccessKey secret, you can obtain them in the Apsara Uni-manager Management Console. For more information, see Obtain the AccessKey ID and AccessKey secret.

#### Manage instances

In ApsaraMQ for RocketMQ, an instance is used to store information about topics and group IDs. This topic describes how to create, update, view, and delete instances in the ApsaraMQ for RocketMQ console.

**Create an instance**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, click **Create an instance**.
4. On the **Create an MQ 4.0 instance** page, configure the parameters and click **Submit**.
The following table describes the parameters.

| Parameter |   | Description | Example |
|---|---|---|---|
|   | Organization | The organization to which the instance belongs. | root test _ |

| baba Cloud Message | Queue User Guide·Console guid |   |   |
|---|---|---|---|
| Region |   |   |   |
|   | Resource Set | The resource set to which the instance belongs. | DefaultResource |
|   | Region | The region in which you want to create the instance. | cn-qingdao- env66-d01 |
|   | Chip Architecture | The chip type of the instance that you want to create. By default, the type of the chip used by the instance is the same as that of the chip deployed in the ApsaraMQ for RocketMQ cluster. You cannot modify this parameter. Valid values: intel Kunpeng Hygon Phytium Yitian ShenWei | intel |
|   | Cluster | The cluster in which you want to create the instance. | cluster1 |
|   | Instance Name | The name of the instance. The name must be 3 to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores ( ). _ | test |
|   | Maximum Number of Topics | The maximum number of topics that can be created on the instance. If you no longer need a topic, delete the topic at the earliest opportunity. Value values: 10 to 5000. Default value: 50. | 50 |

| Basic Configuration |   |   |   |
|---|---|---|---|
|   | Message Sending TPS | The maximum transactions per second (TPS) for sending messages on the instance. If the throttling feature is enabled for the instance, the instance is throttled when the actual TPS for sending messages exceeds the specified threshold. By default, the throttling feature is disabled for an instance. For information about how to enable the feature, see the Instance throttling topic of ApsaraMQ for RocketMQ O&M Guide. Valid values: 500 to 30000. Default value: 500. | 500 |
|   | Message Subscription TPS | The maximum TPS for subscribing to messages in the instance. Valid values: 500 to 30000. Default value: 500. | 500 |
|   | Description | The description of the instance. The description must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), _ hyphens (-), and colons (:). It must start with a letter and cannot start with http:// or https://. | test |

5. **Optional.** If you configured a review workflow, you also need to perform the following
operations: i. In the **Process Information Supplement** dialog box, select a value for the **Execution**
**Method After Approval** parameter, specify a reason in the **Operation Reason** field,
and then click **Submit For Approval**. ii. In the **Operation Succeeded** message, click **Application Form Details** to go to the details page. iii. In the **Approval Progress of Application Form** section of the details page, click **View**
**All** to open the **Approval Progress of Application Form** panel and view the progress
of the review workflow. The review workflow is complete only after all steps are performed. On the **Instance List** page, you can view the instance that you created.

**View instances**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. On the **Instance List** page, you can view the following instance information: **Instance**
**ID/name**, **Instance Type**, **Cluster ID**, **Department**, **Resource Set**, and **Status**. You can
also check whether the instance is a **disaster recovery cluster**.
3. Optional. On the **Instance List** page, you can select the **Automatic Identification**,
**Instance ID**, **Instance name**, or **Cluster ID** filter and enter a keyword in the search box
to search for instances.
4. Optional. On the **Instance List** page, you can click the
icon in the **Monitoring** column to view the instance monitoring information.

**View instance details**

On the **Instance List** page, find the instance that you want to manage and click the instance ID or click **Details** in the **Operation** column to go to the instance details page. Then, you can view information on the following tabs:
**Basic information**: This tab displays the ID of the instance, maximum number of topics
that can be created, name, maximum transactions sent per second (TPS) for sending messages, maximum TPS for message subscription, ID of the cluster to which the instance belongs, description, organization to which the instance belongs, organization ID, resource set to which the instance belongs, resource set ID, chip type, whether the instance has an independent namespace, and whether the instance is a disaster recovery instance.
**Network Management**: This tab displays the endpoint information of the instance. For
information about the scenarios in which the endpoint is used, see the Connect a client to an instance section of this topic.
**Topic Management**: This tab displays the basic information about all topics on the
instance, including the topic names, message types, permissions, descriptions, and operations that can be performed. For more information, see Manage topics.
**Group Management**: This tab displays the basic information about all groups on the
instance, including the group IDs, creation time, permissions, descriptions, and operations that can be performed. For more information, see Group management.
**Message Query**: You can query messages by message ID, message key, and topic. For
more information, see Message query.
**Message Trace**: You can query message traces. For more information, see Message
traces.
**Dead Letter Queue**: You can query, export, and resend dead-letter messages that are
sent to the dead-letter queue. For more information, see Manage dead-letter queues.
**Resource Report**: You can use resource reports to query message production and
consumption information. For more information, see Resource statistics.
**Monitoring**: You can view the monitoring information about ApsaraMQ for RocketMQ on
the instance, Group, Topic, and Topic&Group tabs. For more information, see View the monitoring information of an instance.
**Operation Log**: You can view the operation logs of the instance. For more information, see
View the operation logs of an instance.
**Data Integration**: You can configure relevant settings for data integration. For more
information, see Data integration. You can also click the icon to select another instance from the drop-down list.

**Modify the configurations of an instance**

You can upgrade or downgrade the configurations of an ApsaraMQ for RocketMQ instance.
1. On the **Instance List** page, find the instance that you want to manage and click **Modify** in
the **Operation** column.
2. On the **Modify Configurations** page, modify the parameters in the **Basic Settings**
section and click **Submit**. You can modify the following parameters: **Instance Name**, **Maximum Topics**, **Outbound**
**Message TPS**, **Inbound Message TPS**, and **Description**.
3. **Optional.** If you configured a review workflow, you also need to perform the following
operations: i. In the **Process Information Supplement** dialog box, select a value for the **Execution**
**Method After Approval** parameter, specify a reason in the **Operation Reason** field,
and then click **Submit For Approval**. ii. In the **Operation Succeeded** message, click **Application Form Details** to go to the details page. iii. In the **Approval Progress of Application Form** section of the details page, click **View**
**All** to open the **Approval Progress of Application Form** panel and view the progress
of the review workflow. The review workflow is complete only after all steps are performed.

**Delete an instance**

**Important**

Before you delete an ApsaraMQ for RocketMQ instance, make sure that the following requirements are met: All resources in the instance are deleted, including topics and groups. No ApsaraMQ for MQTT instance is bound to the instance.
1. On the **Instance List** page, find the instance that you want to delete and click **Delete** in
the **Operation** column.
2. In the message that appears, read the information and click **Release**.

**Connect a client to an instance**

When you use an ApsaraMQ for RocketMQ SDK to connect a client to an ApsaraMQ for RocketMQ instance, you must specify the instance information in the SDK code. The instance information includes the ID and endpoint of the instance. You can view the ID on the **Basic Information** tab of the **Instance details** page. You can obtain the endpoint in the **Network Management** tab of the **Instance details** page. The following sample code shows how to configure instance information:

```
// The instance ID. Replace <InstancedId> with the ID of the instance that you created in the ApsaraMQ for RocketMQ console. properties.put(PropertyKeyConst.INSTANCE_ID, "<InstancedId>"); // The instance endpoint. Replace <Endpoint> with the endpoint of the instance that you created in the ApsaraMQ for RocketMQ console. properties.put(PropertyKeyConst.NAMESRV_ADDR, "<Endpoint>");
```

**References**

For more information about how to call API operations to perform operations on instances, see ApsaraMQ for RocketMQ Developer Guide.

#### Manage topics

A topic is a primary category for messages in RocketMQ. RocketMQ uses a publish-subscribe model where a message producer publishes messages to a topic, and a message consumer subscribes to the topic to consume the messages. This topic describes how to create, view, update, and delete topics in the RocketMQ console.

**Prerequisites**

You have created a RocketMQ instance. For more information, see Create an instance.

**Create a topic**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Topic Management** tab.
5. Click **Create a Topic**.
6. In the **Create a Topic** dialog box, configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| Topic | The name of the topic. The topic name can contain only letters, digits, hyphens (-), and underscores ( ). _ It must be 3 to 64 characters in length. The topic name must be different from existing topic names and group IDs. |
| Message Type | The message type. Important ApsaraMQ for RocketMQ supports the following types of messages: normal messages, partitionally ordered messages, scheduled and delayed messages, and transactional messages. When you create a topic, the message type that you select for the topic must be consistent with the type of messages that the topic sends and receives. Otherwise, messages may fail to be sent and received. |
| Description | The description of the topic. |

**Update a topic description**

1. On the **Manage Topics** tab, find the topic that you want to update. In the **Description**
column, click the icon.
2. In the **Update Description** dialog box, enter a new description and click **OK**.

**View topic information**

On the **Instance Details** page, click the **Manage Topics** tab. You can view the basic information of all topics for the instance, such as the topic name, message type, permissions, description, last used time, and available operations.

**Delete a topic**

When you create an instance, you must specify the maximum number of topics for the instance. You cannot create more topics after this limit is reached. If you no longer need a topic, delete it to free up the quota.

**Important**

After a topic is deleted, its related producers and consumers immediately stop working. The topic metadata and message data are also deleted and cannot be recovered. Proceed with caution.
1. On the **Manage Topics** tab, find the topic that you want to delete. In the **Actions** column,
click **Delete**.
2. In the **Notice** dialog box, review the information and click **OK**.

**Import or export topics for a single instance**

**Import**

1. On the **Manage Topics** tab, click **Import**.
2. In the **Import Topics** window, click **Upload File**. After the file is uploaded, the platform
automatically detects the uploaded topics and removes duplicates.

**Note**

i. You can select and upload multiple topic files at a time. ii. Upload files in CSV format. You can use an exported topic file as a template.
3. Select the topics you want to upload and click **OK**.

**Export**

1. On the **Manage Topics** tab, select the topics you want to export and click the download
icon in the upper-right corner.

**Note**

If you do not select any topics and click the download icon, all topics are exported by default.
2. In the **Export** window, select an **Export Scope** and the **Columns to Export**.

| Parameter | Description |
|---|---|
| Export Scope | You can select All or Selected Data. |

| Columns to Export | Selected by default: topic, orderType, and remark. Optional: Type. |
|---|---|

3. Click **OK**.

**More information**

To perform these operations using an API, see the relevant topics in the **Developer Guide**
**for Message Queue for Apache RocketMQ**.

#### Group management

After you create an instance and a topic, you must create a Group ID. This ID serves as a client ID for your message producers and consumers. This topic describes how to create, view, and delete Group IDs in the ApsaraMQ for RocketMQ console.

**Prerequisites**

You have created a RocketMQ instance. For more information, see Create an instance.

**Background information**

A group is a set of producers or consumers that typically produce or consume the same category of messages and share the same publishing or subscription logic. To send and receive messages with ApsaraMQ for RocketMQ, you must create a Group ID to identify your producer or consumer instances. The relationship between Group IDs and topics is many-to-many (N:N). A consumer can subscribe to multiple topics, and multiple consumers can subscribe to a topic. Similarly, a producer can send messages to multiple topics, and multiple producers can send messages to a topic.

**Usage notes**

A Group ID cannot be used across different instances. For example, a Group ID created in instance A cannot be used in instance B. A Group ID cannot be used across different protocols. ApsaraMQ for RocketMQ supports SDKs that use the HTTP and TCP protocols to send and receive messages. If you select the TCP protocol when you create a Group ID, clients using this Group ID can only use a TCPbased SDK, not an HTTP-based SDK. For a consumer Group ID or an existing Consumer ID created by a sub-account, both the sub-account and its main account can use it. For a consumer Group ID or an existing Consumer ID created by a main account, subaccounts under this main account cannot use it. For information about the usage changes related to existing Producer IDs, Consumer IDs, and Group IDs, see Product updates.

**Create a group**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Group Management** tab.
5. Select a protocol for the group that you want to create.
If you want to use TCP-based SDKs to send and receive messages, click the **TCP protocol** tab. If you want to use HTTP-based SDKs to send and receive messages, click the **HTTP**
**protocol** tab.
6. Click **Create Group ID**. In the **Create Group ID** dialog box, configure the parameters and
click **OK**.

| Parameter | Description |
|---|---|
| Group ID | The group ID. The group ID can contain only letters, digits, hyphens (-), and underscores ( ). _ It must be 4 to 64 characters in length. The group ID cannot be modified after it is created. The group ID must be different from existing topic names and group IDs. |
| Maximum retries | The maximum number of retry attempts for normal messages. Valid values: 1 to 16. If you do not configure this parameter, the value of this parameter is 16 by default. Note If you set the maximum number of retry attempts on a client, the number on the client prevails. If you do not set the maximum number of retry attempts on a client, the value of this parameter prevails. |
| Description | The description of the group. |

**Note**

A group ID can be used for producers to identify the same type of producer instance. In this case, the group ID is a producer group ID. A group ID can also be used for consumers to identify the same type of consumer instance. In this case, the group ID is a consumer group ID. TCP-based SDKs and HTTP-based SDKs cannot share the same group ID. Create separate group IDs for TCP-based SDKs and HTTP-based SDKs.

**View Group ID information**

On the **Instance Details** page, click the **Group Management** tab to view basic information about all Group IDs in the instance. This information includes the creation time, permissions, description, last used time, and available actions, such as subscription relationships, consumer status, and sample code.

**Delete a Group ID**

**Important**

After you delete a Group ID, clients that use it will fail to authenticate on reconnection. Existing connections are not affected.
1. In the Group ID list, find the Group ID to delete. In the **Actions** column, click the
icon, and then select **Delete** from the drop-down list.
2. Review the details in the **Confirm Message** dialog box and click **OK**.

**Import and export groups for an instance**

**Import**

1. On the **Group Management** tab, click **Import**.
2. In the **Import Group** window, click **Upload File** and select a CSV file. You can use an
exported group file as a template.
3. Click **OK**.

**Export**

1. On the **Group Management** tab, click the download icon
in the upper-right corner.
2. In the **Export** window, select an **Export Scope** and the **Columns to Export**.
3. Click **OK**.

**More information**

To perform these operations by using an API, see the relevant topics in the ApsaraMQ for RocketMQ Developer Guide.

### Network management

#### View endpoint information

This topic describes how to view the endpoint information of an instance.

**Prerequisites**

You have created a RocketMQ instance. For more information, see Create an instance.

**Procedure**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Network Management** tab.
5. Then, you can view the **TCP client access point** and **HTTP client access point**.

**Important**

Sensitive information is included in the endpoint. Make sure that your network is protected.

#### Associate an ApsaraMQ for RocketMQ

**instance with a VPC**

ApsaraMQ for RocketMQ allows you to associate multiple virtual private clouds (VPCs) with an instance. ApsaraMQ for RocketMQ provides an endpoint for each Single Tunnel VPC. You can assign different endpoints of the same instance to different business services to enforce finegrained access control. This topic describes how to associate an instance with a VPC and disassociate an instance from a VPC in the ApsaraMQ for RocketMQ console.

**Background information**

By default, ApsaraMQ for RocketMQ provides an HTTP-based Any Tunnel endpoint and a TCPbased Any Tunnel endpoint for each instance. You can connect to the ApsaraMQ for RocketMQ instance by using an Any Tunnel endpoint over a VPC. You can associate multiple VPCs of the Single Tunnel type to provide multiple networks for an instance. After a Single Tunnel VPC is associated with an instance, the system automatically allocates an endpoint for the VPC. The endpoint can be used to connect to the ApsaraMQ for RocketMQ instance only over the VPC. You can associate multiple Single Tunnel VPCs with your ApsaraMQ for RocketMQ instance. This way, you can assign isolated networks to your business services to enforce fine-grained network access control.

**Prerequisites**

An ApsaraMQ for RocketMQ instance is created. For more information, see the Create an instance section of the Manage instances topic. A VPC is created. For more information, see the **Create a VPC** topic in the **VPC User Guide**. A vSwitch is created. For more information, see the **Create a vSwitch** topic in the **VPC User Guide**.

**Usage notes**

VPC connections are established based on Any Tunnel network connections. VPCs that are associated with an ApsaraMQ for RocketMQ instance do not affect the existing Any Tunnel networks of the instance. The Any Tunnel networks remain available after VPCs are associated with the instance. We recommend that you use the credential of the administrator of the ApsaraMQ for RocketMQ instance to associate with VPCs and manage VPCs that are associated with the instance. If you use the credentials of non-administrator users to associate with and manage VPCs for an ApsaraMQ for RocketMQ instance, your business services may fail to connect to the instance. Only TCP-based clients can use the endpoint for a VPC to connect to the instance. After a VPC is associated with an ApsaraMQ for RocketMQ instance, the system ensures only that ApsaraMQ for RocketMQ brokers can connect to the instance over the VPC. To connect your client to the ApsaraMQ for RocketMQ instance over the VPC, make sure that your client is connected to the VPC. In this example, the IPv4 CIDR block of a VPC is associated with an instance. For more information about how to associate the IPv6 CIDR block of a VPC, see Attach an IPv6 CIDR block to a VPC.

**Associate an ApsaraMQ for RocketMQ instance with a VPC**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Network Management** tab.
5. On the **Network Management** tab, click **Bind VPC**.
6. In the **Bind VPC** dialog box, configure the parameters and click **OK**.

**Note**

In this example, the IPv4 CIDR block of a VPC is associated with an instance. For more information about how to associate the IPv6 CIDR block of a VPC, see Attach an IPv6 CIDR block to a VPC. The following table describes the parameters.

| Parameter | Description |
|---|---|

| MQ cluster name | The name of the cluster to which the ApsaraMQ for RocketMQ instance belongs. The system automatically obtains the value of this parameter. You do not need to specify a value. |
|---|---|
| Instance | The ID of the ApsaraMQ for RocketMQ instance. The system automatically obtains the value of this parameter. You do not need to specify a value. |
| VPC ID | Select the VPC that you want to associate with the ApsaraMQ for RocketMQ instance from the drop-down list. |
| Switch | Select the vSwitch that you want to connect to the ApsaraMQ for RocketMQ instance from the drop-down list. |
| VPC NAME | Specify a name for the VPC that you want to associate with the ApsaraMQ for RocketMQ instance. We recommend that you specify a name that can help you identify the business service that connects to the instance over the VPC. |

7. After the VPC is associated with the ApsaraMQ for RocketMQ instance, you can view the
information about the VPC in the VPC list on the **Network Management** tab, including
**Zone**, **MQ cluster name**, **Endpoint** (the endpoint assigned to the VPC), **VPC name**, **VPC**
**ID**, and **VSwitch ID** (the vSwitch to which the ApsaraMQ for RocketMQ instance is
connected).
8. You can also click **VPC instance list** in the **Operation** column to view the ApsaraMQ for
RocketMQ instances associated with the VPC.

**Disassociate an ApsaraMQ for RocketMQ instance from a VPC**

**Important**

After a VPC is disassociated from an ApsaraMQ for RocketMQ instance, the endpoint of the VPC becomes invalid and cannot be used to access the instance. Proceed with caution. If a VPC is associated with multiple ApsaraMQ for RocketMQ instances in a cluster and you want to block requests that are sent over the VPC, you must disassociate the VPC from all ApsaraMQ for RocketMQ instances in the cluster.
1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Network Management** tab.
5. In the VPC list, find the VPC that you want to disassociate from the instance and click
**Unbind** in the **Operation** column.
6. In the **Unbind** message, confirm the VPC information and click **OK**.

#### Manage VPCs

This topic describes how to manage virtual private clouds (VPCs) that are associated with an ApsaraMQ for RocketMQ instance.

**Prerequisites**

An ApsaraMQ for RocketMQ instance is created. For more information, see the Create an instance section of the Manage instances topic. A VPC is associated with the ApsaraMQ for RocketMQ instance. You can choose **Network**
**Management > Bind VPC** to associate a VPC with the ApsaraMQ for RocketMQ instance.
For more information, see Associate an ApsaraMQ for RocketMQ instance with a VPC.

**Procedure**

If your ApsaraMQ for RocketMQ instance is already associated with a VPC, perform the following steps to view the VPC information and manage the VPC.
1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Network Management** tab.
5. On the **Network Management** tab, you can view the information of the associated VPC,
including **Zone**, **MQ cluster name**, **Endpoint**, **VPC name**, **VPC ID**, and **VSwitch ID**.
6. Optional. To disassociate the VPC from the ApsaraMQ for RocketMQ instance, click **Unbind**
in the **Operation** column of the VPC. In the **Unbind** message, confirm the information and click **OK**.
7. Optional. To view the ApsaraMQ for RocketMQ instances associated with the VPC, click **VPC**
**instance list** in the **Operation** column of the VPC. In the message that appears, you can
view **Instance**, **VPC name**, **VPC ID**, and **Switch**.

#### Attach an IPv6 CIDR block to a VPC

This topic describes how to attach an IPv6 CIDR block to a VPC.

**Procedure**

**Enable the IPv6 attachment switch**

To attach an IPv6 CIDR block to a VPC, you must first enable the IPv6 attachment switch.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top menu bar, choose **Platform O&M > UniConsole Management R&D**
**Platform**.
3. In the navigation pane on the left, click **Product List**.
4. On the **Product List** page, enter `rocketmq` in the search box and click **Search**.
5. In the **Operations** column for **rocketmq**, click **Switch List** to open the **rocketmq Switch**
**List** page.
6. On the **rocketmq Switch List** page, find the switch with the **Switch ID****useIpv6**. In the
**Operations** column, click **Modify Switch Status**.
7. In the **View Initial Status of Feature Switch** dialog box, turn on the **Current Value**
switch.

**Attach an IPv6 CIDR block to the VPC**

1. After you enable the **useIpv6** switch, log on to the RocketMQ console again. In the
navigation pane on the left, click **Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Network Management** tab.
5. Click the link in the prompt and follow the instructions to authorize resource access.
6. On the **Network Management** tab, click **Bind VPC**.
7. In the **Attach VPC** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|

| MQ Cluster Name | The name of the cluster to which the ApsaraMQ for RocketMQ instance belongs. The system automatically obtains the value of this parameter. You do not need to specify a value. |
|---|---|
| Instance | The ID of the ApsaraMQ for RocketMQ instance. The system automatically obtains the value of this parameter. You do not need to specify a value. |
| Network Type | Select ipv4 or ipv6. |
| VPC ID | Select the VPC that you want to associate with the ApsaraMQ for RocketMQ instance from the drop-down list. |
| vSwitch | Select the vSwitch that you want to connect to the ApsaraMQ for RocketMQ instance from the drop-down list. |
| VPC NAME | Specify a name for the VPC that you want to associate with the ApsaraMQ for RocketMQ instance. We recommend that you specify a name that can help you identify the business service that connects to the instance over the VPC. |

8. After the attachment is complete, you can find the attached VPC information on the
**Network Management** tab. The information includes **Zone**, **MQ Cluster Name**,
**Endpoint** (the instance endpoint assigned after the VPC is attached), **VPC Name**, **VPC ID**,
**Network Type** (**ipv4** or **ipv6**), and **VSwitch ID** (the vSwitch to which the VPC is attached).

### View consumer status

You can check the consumer status in the ApsaraMQ for RocketMQ console to troubleshoot issues that occur during message consumption. This feature allows you to view the information about a group or a consumer identified by the group ID. The information includes the connection status, subscription, number of transactions per second (TPS) for message consumption, number of accumulated messages, and thread stacks. This topic describes how to view such information.

**Background information**

The cause of an exception that occurs during message consumption is complicated. In most cases, the consumer status information in the console is insufficient to troubleshoot a problem. You must perform further troubleshooting by analyzing logs and business scenarios.

**Scenarios**

You can query the consumer status for troubleshooting in the following scenarios: Inconsistent subscriptions Problem: In the **Consumer status** panel, the value of the **Whether the subscription**
**relationship is consistent** parameter is **No**.
Solution: For more information about how to handle subscription inconsistency, see Inconsistent subscriptions. Message accumulation alert Problem: In the **Consumer status** panel, the value in the **Accumulation** column is large. Solution: For more information about how to handle message accumulation alerts, see Message accumulation.

**View the information about a group**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Group Management** tab.
5. Find the group that you want to manage and click **Consumer status** in the **Operation**
column. The following table describes the parameters in the **Consumer status** panel. Table 1. Parameter description

| Parameter | Description |
|---|---|
| Group ID | The group ID. |
| Consumption Pattern | The consumption pattern. |
| Whether the subscription relationship is consistent | Indicates whether the subscriptions of all consumer instances in the group are consistent. For more information about subscription consistency, see Subscription consistency. |
| Real-time consumption speed | The total TPS at which messages are received by the consumer instances in the group. Unit: messages/second. |
| Real-time message accumulation | The total number of messages that are not consumed by the consumer instances in the group. |
| Recent consumption time | The time when the consumer instances in the group last consumed a message. |
| Message latency | The difference between the production time of the earliest unconsumed message in the group and the current time. |

| Online or not | If one consumer instance in the group is online, the value of this parameter is Yes. In this case, you can view information about all online consumer instances in the Connection information section. If none of the consumer instances in the group ID is online, the value of this parameter is No, and no information is displayed in the Connection information section. |
|---|---|

You can also click **Refresh** in the upper-right corner of the panel to refresh the consumer status.

**View information about a single consumer instance in a group**

1. If a group is **online**, you can view information about each online consumer instance in the
group in the **Connection information** section of the **Consumer status** panel. The information includes the client ID, host or public IP address, current process ID, and number of accumulated messages.
2. If you want to view more information about a specific consumer instance, click **Detailed**
**information** in the **Operation** column. The information includes the number of consumer
threads, consumption start time, subscription, and message consumption statistics.
3. If you want to view the stack information about the current process for a specific consumer
instance, find the consumer instance and click **Stack information** in the **Operation** column.

### Reset consumer offsets

You can reset consumer offsets to skip the accumulated or undesired messages instead of consuming them. You can also consume messages that are sent after a point in time regardless of whether the messages sent before this point in time are consumed.

**Background information**

When you reset consumer offsets, take note of the following items: You cannot reset consumer offsets in broadcasting consumption mode. You cannot reset consumer offsets by message ID, message key, or tag.

**Procedure**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Group management** tab.
5. Find the group whose consumer offset you want to reset, click the
icon in the **Operation** column, and then choose **Reset consumption point**.
6. In the **Reset consumption point** dialog box, select the corresponding topic from the
**Topic** drop-down list, and configure the **Reset type** parameter based on your business
requirements. Valid values:
**Clear all stacked messages and start consumption from the latest point** : If you
select this option, consumers identified by the group ID skip all accumulated (unconsumed) messages within the topic and restart consumption from the latest offset. If the "reconsumeLater" error message is returned, the messages in the delivery retry process cannot be skipped.
**Reset consumption points by time**: If you select this option, a time picker appears.
Select a point in time. Only the messages that are sent after the selected point in time are consumed. The time period during which you can select a point in time ranges from the production time of the earliest message stored in the topic to the production time of the latest message stored in the topic. You can select a point in time only within the allowed time range.
7. Click **OK** to reset the consumer offset.

### Message query

#### Overview

If a message is not consumed as expected, you can query the message content to troubleshoot problems. ApsaraMQ for RocketMQ allows you to query messages by message ID, by message key, and by topic. Table 1. Comparison of query methods

| Method | Condition | Type | Description |
|---|---|---|---|
| By message ID | Topic+Messag e ID | Exact match | You can specify a topic and a message ID to obtain a message and its attributes. |
| By message key | Topic+Messag e Key | Fuzzy match | You can specify a topic and a message key to query the 64 messages that are most recently sent and contain the specified message key. We recommend that you specify a unique key for each message in producers whenever possible to ensure that the number of messages with the same key does not exceed 64. Otherwise, some messages cannot be queried. |
| By topic | Topic and time range | Range match | You can specify a topic and a time range to query all messages that meet the specified conditions. This type of query returns a large number of messages. It is difficult to find a specific message that you want to query. |

We recommend that you query messages by using the following process. Figure 1. Message query process

#### Query messages

This topic describes how to query messages in the ApsaraMQ for RocketMQ console by using three different methods.

**Procedure**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Message query** tab.
5. On the **Message query** tab, click a sub-tab, enter the required information, and then click
**Query**.

**Query by Message ID**

When you query messages by message ID, exact match is used. You can specify the topic and ID of a message to query the message. We recommend that you print the message ID to the log when a message is sent. This facilitates troubleshooting. In the following sample code, ApsaraMQ for RocketMQ SDK for Java is used to obtain a message ID:

```
SendResult sendResult = producer.send(msg); String msgId = sendResult.getMessageId();
```

To obtain the sample code for other programming languages, go to the **Group**
**management** tab, find the group, and then click **Sample code** in the Operation column.

**Query By Message key**

ApsaraMQ for RocketMQ creates an index for messages based on the message keys that you specify. When you enter a topic name and a message key to query messages, ApsaraMQ for RocketMQ returns the matched messages based on the index.

**Important**

If you query messages by message key, take note of the following items: The query condition is the specified message key. Only the latest 64 messages that contain the specified key are returned. Therefore, we recommend that you set the key for each message to a unique and business-specific value. The following sample code provides an example on how to specify a message key:

```
Message msg = new Message("Topic","*","Hello MQ".getBytes()); /**
* Specify a key that is used for message query for each message. The key is the pri
mary business attribute of a message. We recommend that you specify a globally uniq ue key for each message.
* If the message is not received as expected, you can query the message in the Apsa
raMQ for RocketMQ console by message key. A message can be sent and received even i f you do not specify a key for the message.
```

`*/`

```
msg.setKey("TestKey"+System.currentTimeMillis());
```

**Query by Topic**

If you cannot query messages by message ID or message key, query messages by topic. You can specify a topic and time range for message sending, retrieve messages in batches, and then find the data that you need.

**Important**

If you query messages by topic, take note of the following items: This query method allows you to obtain all messages that are sent in a topic during a specific time range. We recommend that you narrow down the time range to locate the message that you want to query in an efficient manner. If you query messages by topic, a large number of messages are returned on multiple pages.

#### Message query results

This topic describes the results of message queries. You can view the message query results on the **Message query** tab in the ApsaraMQ for RocketMQ console. The query result includes the **message ID**, **tag**, **key**, and **storage time**. In addition, you can download the message content, query message traces, and view message details in the
**Operation** column.

**Message details**

**Delivery status**

The **delivery status** is calculated by ApsaraMQ for RocketMQ based on the consumption progress of each group ID. For more information about the delivery status, see the Message delivery states table of this topic.

**Note**

The **delivery status** is calculated based on the consumption progress. To query the consumption details, view the **message trace**. The message trace displays the complete path of the message. For more information, see Query a message trace. Table 1. Message delivery states

| Delivery status | Possible cause |
|---|---|
| The message has been subscribed to and consumed at least once. | The group ID has consumed the message as expected. |
| The message has been subscribed to but is filtered out by the filter expression. Check the tag of the message. | The tag of the message does not comply with the subscription of the consumer and the message is filtered out. To query the subscription of the consumer, log on to the ApsaraMQ for RocketMQ console, go to the Group management tab, find the group ID of the consumer whose subscription you want to view, and then click Consumer status in the Operation column. |
| The message has been subscribed to but is not consumed. | A consumer identified by the group ID has subscribed to the message, but the message has not been consumed possibly because the consumption is slow or is blocked due to an exception. |
| The message has been subscribed to but the consumer that subscribes to the message and is identified by the group ID is not online. Use the message tracing feature to query the details about the message in an exact match. | A consumer identified by the group ID has subscribed to the message but the consumer is not online. Check the reason why the consumer is not online. |
| An unknown exception occurred. | An unknown exception occurred. Contact technical support for troubleshooting. |

**Verify message consumption**

In the **Message details** panel, you can check whether **message consumption** works as expected. ApsaraMQ for RocketMQ supports the consumption verification feature. You can push a specified message to a specified online consumer to check whether the consumer can consume the message based on the correct logic as expected.

**Important**

The consumption verification feature can be used only to verify whether consumers can consume messages based on the correct logic as expected. This feature does not affect the normal process of receiving messages. Therefore, information such as the consumption status of a message does not change after the consumption is verified.

### Message tracing

#### Overview

A message trace is the complete trace of a message that is sent from a producer to the ApsaraMQ for RocketMQ broker and then consumed by a consumer. The message trace includes the time, status, and other information of each node in the preceding process. The message trace provides robust data support for troubleshooting in production environments. This topic describes the scenarios, query procedure, and parameters of query results for message tracing.

**Message trace data**

In ApsaraMQ for RocketMQ, the complete trace of a message involves three roles: producer, broker, and consumer. Each role adds relevant information to the trace when the role processes the message. The information is aggregated to indicate the status of the message. The following figure shows the relevant data. Figure 1. Message trace data

**Scenarios**

You can use the message tracing feature to troubleshoot problems if a message is not sent or received as expected in your production environment. You can query the message trace by message ID, message key, or topic to check whether the message is sent and received as expected within the specified time range.

**Usage notes**

No extra fees are incurred when you use the message tracing feature. After a message is sent, you can query the trace of the message based on the ID or key of the message in the ApsaraMQ for RocketMQ console. You must take note of the following points. Table 1. Rules for querying message traces

| Message type | Query description |
|---|---|
| Normal messages | A sending trace is generated after the message is sent. If the message is not consumed, Not Consumed appears. After the message is consumed, the delivery and consumption information appears. |
| Ordered messages | A sending trace is generated after the message is sent. If the message is not consumed, Not Consumed appears. After the message is consumed, the delivery and consumption information appears. |
| Scheduled messages and delayed messages | If the current system time does not reach the specified message consumption time, the trace can be queried but the message cannot be queried. |

| Transactional messages | Before the transaction is committed, the trace can be queried but the message cannot be queried. |
|---|---|

**Examples**

If you find that a message is not received as expected based on the log information, perform the following steps to troubleshoot the problem by using the message trace:
1. Collect the information about the message that is suspected to be abnormal. The
information includes the message ID, message key, topic, and approximate sending time.
2. Log on to the ApsaraMQ for RocketMQ console, and create a query task to query the
message trace based on the available information.
3. Check the query results and analyze the cause.
If **Not Consumed** appears in the trace, go to the **Groups** page to View consumer status. Then, you can determine whether message accumulation is the reason why the message is not consumed. If the message is consumed, find the corresponding consumer and the time when the message is consumed in the consumption information. Then, log on to the consumer to view the relevant log.

#### Query a message trace

You are not charged when you use the message tracing feature of ApsaraMQ for RocketMQ. Before you use the message tracing feature, make sure that it is supported by the version of the SDK that you use. After you send and receive messages, you can query the messages in the ApsaraMQ for RocketMQ console.

**Prerequisites**

The message tracing feature is supported by the SDK version that you use. The following versions of SDKs support the message tracing feature:

**TCP**

SDK for Java: V1.2.7 and later SDK for C and C++: V1.1.2 and later For .NET: V1.1.2 and later

**HTTP**

Node.js: V1.0.2 and later SDKs for Java, Go, Python, C#, C++, and PHP: V1.0.1 and later

**Procedure**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Message trace** tab.
5. Click **Create a query task**.
6. In the **Create a query task** panel, configure query conditions based on your business
requirements. Then, click **OK**.

**Important**

Set the **time range** as accurately as possible to narrow down the query scope and speed up the query. You can use one of the following methods and configure the required parameters to query the trace of a message.

| Query method | Required parameter | Description |
|---|---|---|
| Query by Message ID | When you query a message trace by using this method, you must specify the unique ID of the message, the topic to which the message belongs, and the time range in which the message was sent. | We recommend that you use this method because this method is an exact match method and can query the trace of a message in an efficient manner. |
| Query By Message Key | When you query a message trace by using this method, you must specify the message key, the topic to which the message belongs, and the time range in which the message was sent. | This method is a fuzzy match method. Up to 1,000 traces can be returned for a query based on the specified message key. This method is ideal if you know the key of the message that you want to query but you do not know the ID of the message. |
| Query by Topic | You only need to enter the topic and time range in which the messages were sent. This method allows you to query multiple message traces. | This method uses a range query. It is ideal if you do not know the message ID or message key and the message volume is small. We recommend that you do not use this query method. In most cases, a large number of messages are produced in a topic within a specific time range. If you use this method, you can hardly identify a specific message among the queried messages. |

After you create a query task, you can view the information about the query task on the
**Message trace** tab. If the value in the **Task Status** column is **Querying**, the query is not
complete.
7. In the upper-right corner of the query task list, you can click the Refresh icon to refresh the
tab. After the value in the Task Status column changes to **Query completed**, you can view the information about the trace of the message. You can click **Details** in the **Operation** column to view the information about the trace of the message, including the attributes and consumption status of the message. If no message trace information is displayed, check whether the information that you specified when you created the query task is correct. If trace information is returned, you can view the brief information about the trace, such as the message ID, tag, message key, sending status, sending time, and consumption status.
8. Click **View Track** to view details of the message trace.
A message trace consists of three parts: Information about the message producer Information about the topic to which the message belongs Information about the message consumer If you perform a query based on a message key or a topic, multiple traces may be displayed. You can scroll the page to view and compare information about traces of different messages. For information about message traces, see States in message traces.

#### States in message traces

This topic describes the terms and status information displayed on the Message trace tab. Table 1. Terms

| Object | Field | Description |
|---|---|---|
| Producer | Sender | The IP address of the sender. |
|   | Sending time | The time when the message was sent from the producer. The time follows the ISO 8601 standard in the yyyy-MM- ddThh:mm:ssZ format. |
|   | Sending time | The period of time that the producer took to send a message by calling the Send method. Unit: milliseconds. |
|   | Status | The status of the message. |
|   | Topic | The topic name. |
|   | Key | The AccessKey ID of the Apsara Stack account. |

| Topic |   |   |
|---|---|---|
|   | Tag | The AccessKey ID is similar to a Gmail tag. It is used to sort messages and help the consumer filter messages on the ApsaraMQ for RocketMQ broker based on specified conditions. |
|   | Region | The region where the message is stored or the region where the consumer is located. |
| Consumers | First time | The consumption status. |
|   | IP | The IP address of the consumer. |
|   | Time consuming | The period of time that the consumer took to execute the consumeMessage method after the message is pushed to the consumer. |
|   | Delivery time | The time when the consumer executed the consumeMessage method to start consuming the message. The time follows the ISO 8601 standard in the yyyy- MM-ddThh:mm:ssZ format. |

Table 2. States in message traces

| Sent/Consumption Status | Field | Description |
|---|---|---|
| Sending status | Sent successfully | The message is sent and stored on the ApsaraMQ for RocketMQ broker. |
|   | Send failed | The message fails to be sent and is not stored on the ApsaraMQ for RocketMQ broker. In this case, the broker tries to redeliver the message. |
|   | Message Timing | The message is a scheduled or delayed message and it is not the time to deliver the message. |

|   | Transaction not committed | The message is a transactional message and has not been committed. |
|---|---|---|
|   | Transaction rollback | The message is a transactional message and has been rolled back. |
| Consumption status | All successful | The message has been consumed by all the consumers to which it is delivered. |
|   | Partial success | The message fails to be consumed in specific deliveries, or the message is consumed after it is redelivered. |
|   | All failed | The message still fails to be consumed after all delivery retries. |
|   | Not consumed yet | The message is not delivered to consumers. |
|   | Consumption result not returned | No results are returned for the message consumption method or the method is interrupted. Therefore, the consumption status is not returned to the ApsaraMQ for RocketMQ broker. |
|   | Consumption success | The message has been consumed. |
|   | Consumption failure | A failure result is returned for the message consumption method, or the method throws an exception. |

### Manage dead-letter queues

Dead-letter queues are used to process messages that cannot be consumed as expected. This topic describes how to query, export, and resend dead-letter messages in dead-letter queues. This helps you manage dead-letter messages based on your business requirements and prevent missing message processing.

**Background information**

When a message fails to be consumed for the first time, ApsaraMQ for RocketMQ automatically retries the consumption of the message. If the message still cannot be consumed after the maximum number of retries is reached, the message cannot be properly consumed. Instead of immediately discarding the message, ApsaraMQ for RocketMQ sends it to a particular queue of the corresponding consumer. In ApsaraMQ for RocketMQ, messages that cannot be consumed as expected are known as dead-letter messages. Queues that are used to store dead-letter messages are known as dead-letter queues.

**Dead-letter characteristics**

Dead-letter messages have the following features: Dead-letter messages can no longer be consumed as expected by consumers. Dead-letter messages have a validity period of seven days, which is the same as that of normal messages. After the validity period expires, dead-letter messages are automatically deleted. We recommend that you handle dead-letter messages within seven days after they are generated. Dead-letter queues have the following features: A dead-letter queue corresponds to a group ID instead of a consumer instance. If no dead-letter messages are generated in a consumer group, ApsaraMQ for RocketMQ does not create a dead-letter queue for the consumer group. A dead-letter queue contains all the dead-letter messages of the corresponding group ID regardless of the message topic. You can query, export, and resend dead-letter messages in the ApsaraMQ for RocketMQ console.

**Query dead-letter messages**

The following table describes the methods that you can use to query dead-letter messages in ApsaraMQ for RocketMQ.

| Query method | Query condition | Query type | Description |
|---|---|---|---|

| Query by Group ID | Group ID and time range | Range match | You can specify a group ID and a time range to query all messages that meet the specified conditions. This type of query returns a large number of messages. As a result, finding a specific message can be time- consuming. |
|---|---|---|---|
| Query by Message ID | Group ID+Message ID | Exact match | You can specify a group ID and a message ID to query a message by using exact match. |

**Query by group ID**

You can batch query all the dead-letter messages of a group ID within a time range by specifying the group ID and time range.

**Important**

The production time of a dead-letter message refers to the time when a message is sent to the dead-letter queue after the maximum number of redelivery retries for this message is reached.
1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Dead letter queue** tab.
5. Click the **Query by Group ID** tab.
6. Select the ID of the group whose dead-letter messages you want to view from the **GroupId**
drop-down list.
7. Select the start time and end time from the **Query time range** date and time picker.
8. Click **Query**. All dead-letter messages that meet the preceding conditions are displayed.
9. Find the dead-letter message that you want to view and click **View Details** in the
**Operation** column to view the details about the message. The details include the basic
attributes, **message body size**, and **delivery status**.

**Query by message ID**

If you query messages by message ID, exact match is used. You can search for a message by specifying its group ID and message ID.
1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Dead letter queue** tab.
5. Click the **Query by Message ID** tab.
6. Select the ID of the group whose dead-letter messages you want to view from the **GroupId**
drop-down list.
7. Specify the **ID of the message** that you want to query.
8. Click **Query**. All dead-letter messages that meet the preceding conditions are displayed.
9. Find the dead-letter message that you want to view and click **View Details** in the
**Operation** column to view the details about the message. The details include the basic
attributes, **message body size**, and **delivery status**.

**Export dead-letter messages**

If you cannot process dead-letter messages for the moment, you can export the messages in the ApsaraMQ for RocketMQ console to prevent them from being deleted after expiration. You can export a single dead-letter message or multiple dead-letter messages at a time in the ApsaraMQ for RocketMQ console. The exported file is in the CSV format. The following table describes the fields of an exported message.

| Field | Description |
|---|---|
| instanceId | The instance ID. |
| topic | The message topic. |
| msgId | The message ID. |
| bornHost | The URL of the producer that produced the message. |
| bornTimestamp | The time when the message was produced. |

| storeTimestamp | The time when the message turned into a dead- letter message. |
|---|---|
| reconsumeTimes | The number of consumption failures. |
| properties | The message attributes in the JSON format. |
| body | The Base64-encoded message body. |
| bodyCRC | The message body Cyclic Redundancy Check (CRC). |

Export a single dead-letter message In the ApsaraMQ for RocketMQ console, find the dead-letter message that you want to export and click **Export** in the **Operation** column to export the dead-letter message. Export multiple dead-letter messages at a time In the ApsaraMQ for RocketMQ console, search for the dead-letter messages that you want to export by group ID, select the dead-letter messages, and then click **Batch export** below the message list to export the dead-letter messages.

**Resend dead-letter messages**

If a message enters a dead-letter queue, the message cannot be consumed as expected for specific reasons. Therefore, you must process the message in a special way. After you troubleshoot the issues, you can resend the dead-letter messages for consumption in the ApsaraMQ for RocketMQ console.

**Important**

After a dead-letter message is resent to the consumer, the message will still be stored in the dead-letter queue for three days. The system automatically deletes the message after the three days. Resend a single dead-letter message In the ApsaraMQ for RocketMQ console, find the dead-letter message that you want to resend and click **Resend** in the **Operation** column to resend the dead-letter message. Resend multiple dead-letter messages at a time In the ApsaraMQ for RocketMQ console, search for the dead-letter messages that you want to resend by group ID, select the dead-letter messages, and then click **Batch resend** below the message list to resend the dead-letter messages.

### Resource statistics

#### Overview

This topic describes how to use the resource statistics feature to query the statistics of produced messages and consumed messages. The resource statistics feature provides the statistics of produced messages and consumed messages. This feature allows you to query the following data:

**Statistics of produced messages**

Queries by topic: You can query the total number of messages that are received by a topic or the average number of messages that are received by a topic per second in a specified period of time. Queries by instance: You can query the total number of messages that are received by the topics in a specified instance or the average number of messages that are received by the topics in a specified instance per second in a specified period of time.

**Statistics of consumed messages**

Queries by group ID: You can query the total number of messages that are sent from a topic to consumers identified by a group ID or the average number of messages that are sent from a topic to consumers identified by a group ID per second in a specified period of time. Queries by instance: You can query the total number of messages that are sent to all groups in a specified instance or the average number of messages that are sent to all groups in a specified instance per second in a specified period of time.

#### Query the statistics of produced

**messages**

This topic describes how to query the statistics of produced messages. You can query the total number of messages that are received by a topic or all topics across the brokers of a specified instance during a specified period of time. You can also query the average number of messages that are received by a topic or all topics across the brokers of a specified instance per second during a specified period of time.

**Procedure**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Resource Report** tab.
5. On the **Resource Report** tab, click the **Message production** tab.
6. From the **Resource type** drop-down list, select a resource type for which you want to
query the statistics of produced messages, configure the related parameters, and then click
**Query**.

| Parameter | Description |
|---|---|

| Resource type | The resource type. Valid values Instance and Topic. Instance: queries the total number of messages that are received by the topics of a specified instance or the average number of messages that are received by the topics of a specified instance per second during a specified period of time. Topic: queries the total number of messages that are received by a specified topic or the average number of messages that are received by a specified topic per second during a specified period of time. |
|---|---|
| Current instance | This parameter is displayed if you set Resource type to Instance. This parameter is automatically set to the name and ID of the current instance. |
| Topic | This parameter is displayed if you set Resource Type is set to Topic. Select a topic to query the statistics of the produced messages that are sent to a specified topic in the current instance. |
| Collection type | The collection type. Valid values: Total and TPS. Total: queries the total number of messages that are received by the topic in each collection cycle. TPS: queries the average number of messages that are received by the topic per second in each collection cycle. |
| Collection cycle | The collection interval. Valid values: 1 minute, 10 minutes, 30 minutes, and 1 hour. This parameter specifies the interval at which data is collected. A smaller value indicates a higher data collection frequency and more detailed data. |
| Time range | ApsaraMQ for RocketMQ allows you to query messages that are produced in the last three days. |

The query results are displayed in charts.

#### Query the statistics of consumed

**messages**

This topic describes how to query the statistics of consumed messages. You can query the total number of messages that are sent from a topic to consumers identified by a group ID during a specified period of time. You can also query the average number of messages that are sent from a topic to consumers identified by a group ID per second during a specified period of time.

**Procedure**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Resource Report** tab.
5. On the **Resource Report** tab, click the **Message Consumption** tab.
6. From the **Resource type** drop-down list, select a resource type for which you want to
query the statistics of consumed messages. Configure the related fields. Then, click **Query**.

| Parameter | Description |
|---|---|
| Resource type | The resource type. Valid values: Instance and GroupId. Instance: queries the total number of messages that are sent to all groups of the instance or the average number of messages that are sent to all groups of the instance per second during a specified period of time. GroupId: queries the total number of messages that are sent from a specified topic to a specified group or the average number of messages that are sent from a specified topic to a specified group per second during a specified period of time. |
| Current instance | This parameter is displayed only if Resource type is set to Instance. This parameter is automatically set to the name and ID of the current instance. |
| Group ID | If you set Resource type is set to GroupId, you must select the group ID for which you want to query data. |
| Collection type | Valid values: Total and TPS. Total: queries the total number of messages that are sent to consumers identified by the group ID in each collection cycle. TPS: queries the average number of messages that are sent to consumers identified by the group ID per second in each collection cycle. |
| Collection cycle | Valid values: 1 minute, 10 minutes, 30 minutes, and 1 hour. This parameter specifies the interval at which data is collected. A smaller value indicates a higher data collection frequency and more detailed data. |
| Time range | ApsaraMQ for RocketMQ allows you to query messages that are consumed in the last three days. |

Results are displayed in charts.

### View the monitoring

**information of an instance**

You can view monitoring charts in the CloudMonitor console to obtain the information about ApsaraMQ for RocketMQ instances. This topic describes how to view the monitoring information of an ApsaraMQ for RocketMQ instance in the ApsaraMQ for RocketMQ console and the CloudMonitor console.

**Background information**

CloudMonitor provides real-time monitoring, alerting, and notification services for resources to protect your services and business. For more information, see the **Overview** topic of the "Cloud Monitor Service" chapter in Apsara Uni-manager Management Console User Guide in Apsara Stack Documentation Center.

**Procedure**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Monitoring** tab.

**Note**

You can also click **More** to go to the CloudMonitor console and view the detailed monitoring information of the instance.

| Parameter | Description |
|---|---|
| Monitoring granularity | The granularity by which the instance is monitored. Valid values: instance, Group, Topic, and Topic&Group. |
| Monitoring period | The time range during which monitoring data is collected. Valid values: Hourly monitoring: Last Hour, Last 3 hours, Last 6 hours, and Last 12 hours. Daily monitoring: Last 1 day, Last 3 days, Last 7 days. Custom: allows you to specify the start time and end time to define a monitoring period based on your business requirements. |
| Monitoring metric | For more information about monitoring metrics, see the Metrics topic in the "Cloud service monitoring" topic of the "Cloud Monitor Service" chapter in Apsara Uni-manager Management Console User Guide in Apsara Stack Documentation Center. Note By default, the average values of each monitoring metric are displayed. You can also choose to display the maximum or minimum values of each monitoring metric based on your business requirements. |

### View the operation logs of an

**instance**

The operation log of an ApsaraMQ for RocketMQ instance records the time, location, and operator of each operation. These records are properly archived. If you encounter technical issues or faults when you manage or use ApsaraMQ for RocketMQ instances, operation logs can help you quickly find the causes of issues or faults to facilitate troubleshooting. In addition, operation logs can also be used to evaluate the impact scope of faults and determine the responsibility and other related issues.

**Note**

1. Operation logs are retained for seven days. To adjust the retention period, modify the
logging configurations as an administrator.
2. If you extend the retention period by modifying the logging configurations, the log data
before the new retention period is not backfilled.

**Procedure**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance Details** page, click the **Operation Log** tab.
5. View operation logs. By default, the system displays all operations performed on the
ApsaraMQ for RocketMQ instance and its related resources in the previous seven days. You can filter operation records by specifying filter conditions such as **Operator** and
**Operation Name**.

**Note**

You can also find an operation record and click **Operation Details** in the **Operation** column to view more detailed log information in the **Operation Details** panel.

### Account authorization

**management**

Message Queue for Apache RocketMQ allows you to use an Apsara Stack tenant account to grant permissions to publish and subscribe to a topic to another Apsara Stack tenant account or a Resource Access Management (RAM) user. An Apsara Stack tenant account is a level-1 department account. A RAM user is a personal account that is used to access the Apsara Stack resources.

**Grant permissions to another Apsara Stack tenant account**

You can use an Apsara Stack tenant account to grant permissions to another Apsara Stack tenant account. To grant permissions to publish and subscribe to a topic, perform the following steps:
1. Log on to the Message Queue for Apache RocketMQ console. In the left-side navigation
pane, click **Topics**.
2. On the **Topics** page, find the topic that you want to authorize another account to manage,
click in the **Actions** column, and then select **Authorize** from the drop-down list.
3. In the **Authorize** dialog box, set **Account Type** to **Apsara Stack Account**.
4. In the **Apsara Stack Account ID** field, enter the ID of the Apsara Stack tenant account to
which you want to grant permissions.
5. From the **Authorization Type** drop-down list, select the permissions that you want to
grant to the Apsara Stack tenant account. Then, click **OK**.

**Grant permissions to a RAM user**

You can use an Apsara Stack tenant account to grant permissions to a RAM user that belongs to the Apsara Stack tenant account. To grant permissions to publish and subscribe to a topic, perform the following steps:
1. Log on to the Message Queue for Apache RocketMQ console. In the left-side navigation
pane, click **Topics**.
2. On the **Topics** page, find the topic that you want to authorize a RAM user to manage, click
in the **Actions** column, and then select **Authorize** from the drop-down list.
3. In the **Authorize** dialog box, set **Account Type** to **RAM User**.
4. In the **RAM User Name** field, enter the name of the RAM user to which you want to grant
permissions.
5. From the **Authorization Type** drop-down list, select the permissions that you want to
grant to the RAM user. Then, click **OK**.

**Note**

The RAM user to which you want to grant permissions must be an account that is used to access the Apsara Stack resources and is owned by the department to which the Apsara Stack tenant account belongs.

**View authorization information**

You can view the authorization records and the details of each topic in the Message Queue for Apache RocketMQ console. To view authorization information, perform the following steps:
1. Log on to the Message Queue for Apache RocketMQ console. In the left-side navigation
pane, click **Topics**.
2. On the **Topics** page, find the topic that you want to view, click
in the **Actions** column, and then select **View Authorization** from the drop-down list to view the authorization records and information of the topic.

**Note**

You do not need to authorize your account to manage the topics that you create. After you log on to the Message Queue for Apache RocketMQ console by using an authorized account, you can view the topic that the account is authorized to manage. Then, you must create a group ID. You cannot use the group ID of the Apsara Stack tenant account that is used to grant permissions to your account. A topic that an account is authorized to manage belongs to the Apsara Stack tenant account that is used to grant permissions. Therefore, you cannot use the authorized account to delete the topic. If you grant permissions to a RAM user, you cannot use the authorized RAM user to create topics. If you grant permissions to another Apsara Stack tenant account, you can use the authorized Apsara Stack tenant account to create topics. However, the created topics are not associated to the Apsara Stack tenant account that is used to grant permissions.

### Data integration

#### Overview

ApsaraMQ for RocketMQ provides fully managed and O&M-free connectors for data synchronization between ApsaraMQ for RocketMQ and other Alibaba Cloud services. This topic describes the connector feature of ApsaraMQ for RocketMQ. This topic also describes the types, usage notes, and benefits of connectors.

**Description**

ApsaraMQ for RocketMQ connectors allow you to synchronize data between ApsaraMQ for RocketMQ and other Alibaba Cloud services. The following types of connectors are provided by ApsaraMQ for RocketMQ:

**Sink connectors**

In the following figure, ApsaraMQ for RocketMQ is the data source and other Alibaba Cloud services are the data destinations. Sink connectors can be used to export data from ApsaraMQ for RocketMQ to other Alibaba Cloud services.

**Source connectors**

In the following figure, other Alibaba Cloud services are data sources and ApsaraMQ for RocketMQ is the data destination. Source connectors can be used to import data from other Alibaba Cloud services to ApsaraMQ for RocketMQ.

**Connectors**

**Sink connectors**

| Connector | Description | References |
|---|---|---|
| MaxCompute sink connector | Export data from ApsaraMQ for RocketMQ to MaxCompute. | MaxCompute sink connectors |

**Source connectors**

ApsaraMQ for RocketMQ does not support data synchronization by using source connectors.

**Usage notes**

The running of a connector consumes system resources, such as CPU, memory, and I/O, and the resources of the data source and data destination. Make sure that resources are sufficient before you run a connector.

**Benefits**

**Zero impact on business**

When you use a connector to synchronize data between ApsaraMQ for RocketMQ and other heterogeneous data sources, you can use asynchronous messages as expected and the business is not affected.

**Ease of use**

ApsaraMQ for RocketMQ allows you to implement the connector feature in a visualized manner in the ApsaraMQ for RocketMQ console. You do not need to configure other complex services.

#### Configure a MaxCompute sink

### connector

You can use connectors to synchronize data between ApsaraMQ for RocketMQ and other Apsara Stack services. This topic describes how to create and deploy a MaxCompute sink connector to export data from a source topic in an ApsaraMQ for RocketMQ instance to a table in MaxCompute.

**Prerequisites**

A topic is created in the ApsaraMQ for RocketMQ console. For more information, see Create a topic. A table is created in MaxCompute. For more information, see the **Create a table** topic in
**MaxCompute User Guide**.
In this example, the following statement is executed to create a table named

```
 test_rocketmq .
```

**Important**

When you create a table, you can change the table name based on your business requirements. However, the format and fields of the table must be the same as those in the following sample code:

```
CREATE TABLE IF NOT EXISTS `test_rocketmq` (
  `topic` STRING,
  `msg_id` STRING,
  `value` STRING,
  `queue_id` BIGINT,
  `gmt_create` STRING,
  `offset` BIGINT,
  `tag` STRING
```

`)`

```
PARTITIONED BY (
  pt STRING
```

);

**Usage notes**

After a connector starts running, the connector consumes system resources, such as CPU and memory, and the resources of the data source and data destination. Make sure that resources are sufficient before you run a connector.

**Create a connector**

1. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
2. In the top navigation bar of the **Instance List** page, select an **organization** and a
**resource set**.
3. On the **Instance List** page, find the name of the instance that you want to manage and
click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
4. On the **Instance details** page, click the **Data integration** tab.
5. On this tab, click the **MaxCompute Sink Connector** card.
6. In the **Create a task** panel, perform the following steps:
i. In the **Basic configuration information** step, enter a **task name** and a **task**
**description**, and then click **Next Step**.
ii. In the **Configure a data source** step, configure the parameters and click **Next Step**. The following table describes the parameters.

| Parameter | Description | Example |
|---|---|---|
| Data source | The source service from which data is synchronized. This parameter is set to RocketMQ. | RocketMQ |
| Instance | The ID of the ApsaraMQ for RocketMQ instance to which the source topic belongs. The instance ID that you specified in Step 3 is automatically displayed. You do not need to configure this parameter. | MQ INST 1624605771445148 _ _ BfSh**** _ |
| Topic | The name of the ApsaraMQ for RocketMQ topic from which data is synchronized. | maxcompute sink input _ _ |
| Initial consumption location | The offset from which data is synchronized to MaxCompute. Valid values: Earliest site: Data is synchronized from the earliest offset in the topic when you run the connector. Closest site: Data is synchronized from the latest offset in the topic when you run the connector. | Earliest site |

| Filter rules | The rule that is used to filter messages. The connectors of ApsaraMQ for RocketMQ allow you to filter messages based on tags. If no filter rule is specified, all messages from the source topic are synchronized to the destination table. If a filter rule is specified, only data that meets the filter rule in the source topic is synchronized to the destination table. You can specify tags to filter messages based on tags. For example, if you want to synchronize messages whose tag is CartService to the destination table, enter CartService in this field. If you want to specify multiple tags, separate multiple values with double vertical bars (\|\|). Example: CartService\|\|Inventory\|\|Payment . For more information, see Message filtering. | Cart\|\|Inventory\|\|Payment |
|---|---|---|
| Number of tasks | The maximum number of connectors that can be created. Each connector contains an ApsaraMQ for RocketMQ consumer client. The consumption performance of a connector is less than or equal to 3,000 transactions per second (TPS). Valid values: 1 to 16. The value must be an integer. | 10 |

| Abnormal Data Topic | The topic that is used to store error data. The connector delivers messages that fail to be sent to the topic. The name of the topic that ApsaraMQ for RocketMQ creates for the connector is displayed. You do not need to configure this parameter. Format: connect-error-Connec tor name. Important Do not delete the error data topic that ApsaraMQ for RocketMQ creates for the connector. If you delete the connector, the error data topic is automatically deleted. | connect-error-mqsink |
|---|---|---|
| Connector Group ID | The group that is used to consume synchronized messages in the connector. The ID of the group that ApsaraMQ for RocketMQ creates for the connector is displayed. You do not need to configure this parameter. Format: connect- Connector n ame. Important Do not delete the group that ApsaraMQ for RocketMQ creates for the connector. If you delete the connector, the group is automatically deleted. | connect-mqsink |

iii. In the **Configure the target source** step, configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description | Example |
|---|---|---|
| Destination source | The destination service to which data is synchronized. This parameter is set to MaxCompute. | MaxCompute |

| MaxCompute table name | The name of the MaxCompute table to which the data is synchronized. | test rocketmq _ |
|---|---|---|
| Partition granularity | The frequency at which the source data is written to a new partition. Valid values: Minutes: writes data to a new partition every minute. Hours: writes data to a new partition every hour. Days: writes data to a new partition every day. | Minutes |
| Connection address | The endpoint of MaxCompute. ApsaraMQ for RocketMQ uses the specified MaxCompute endpoint to access MaxCompute. For more information about how to obtain the endpoint, see the Obtain an endpoint topic in MaxCompute Developer Guide. | http://service.xxxx.shuguang. com/api |
| Workspace | The name of the MaxCompute project to which the destination table belongs. | connector test _ |
| accessId | The AccessKey ID of the Apsara Stack tenant account to which the MaxCompute table belongs. For more information about how to obtain the AccessKey ID, see the Obtain an AccessKey pair topic in MaxCompute Developer Guide | j8geROUEAW1k**** |
| accessKey | The AccessKey secret of the Apsara Stack tenant account to which the MaxCompute table belongs. For more information about how to obtain the AccessKey secret, see the Obtain an AccessKey pair topic in MaxCompute Developer Guide. | AMx4ainrLWhT8jYUPHkdI4zY7 t**** |

| Number of retries | The maximum number of times that a message can be resent when timeouts or exceptions occur during message sending. Valid values: 1 2 3 Note If a message still fails to be sent after the maximum number of retries is reached, the message is delivered to the error data topic that ApsaraMQ for RocketMQ creates for the connector. For more information, see the Message retry topic in ApsaraMQ for RocketMQ User Guide | 1 |
|---|---|---|
| TargetParams. Timeout | The maximum amount of time to wait for a response during message sending. If a response is not returned for a message after the period of time specified by this parameter elapses, the message is redelivered. Valid values: 3000 to 30000. Unit: milliseconds. | 10 |

After you create a connector, you can see it in the connector list on the **Data Integration** page. The status of the connector is displayed as **Pending Deployment**.

**Deploy a connector**

You can use a connector to synchronize data only after you deploy the connector.
1. On the **Data integration** tab, find the connector task that you created and click **Deploy** in
the **Operation** column.
2. In the message that appears, click **OK** to deploy the connector.
If the connector task is in the **To be scheduled** or **Deploying** state after you perform the preceding operations, the system is scheduling backend resources to deploy the connector. In this case, you need to wait a moment. After the connector is deployed, the status of the connector changes to **Running**.

**View the details of a connector**

1. On the **Data integration** tab, find the connector task that you want to manage and click
**Details** in the **Operation** column.
2. On the task details page, click the **Overview** or **Configuration** tab.
The **Overview** tab displays the running status, running results, and statistical reports of the connector. The **Configuration** tab displays the basic information, data source information, and data destination information about the connector.

**Pause and resume a connector**

If you do not want to use a connector to synchronize data, you can pause the connector. After a connector is paused, data synchronization immediately stops. If you want to continue to use the connector, you can resume it.

**Important**

After the connector is resumed, the source data generated during the pause period is not synchronized to the data destination.
1. On the **Data integration** tab, find the connector task that you want to manage and click
**Pause** or **Recovery** in the **Operation** column.
2. In the message that appears, click **OK**.

**Delete a connector**

**Important**

After you delete a connector task, data synchronization between the specified source and destination immediately stops. Proceed with caution.
1. On the **Data integration** tab, find the connector task that you want to delete and click
**Delete** in the **Operation** column.
2. In the message that appears, click **OK**.

## Message routing

### Replicator

The replicator message routing feature provided by ApsaraMQ for RocketMQ allows you to synchronize messages between clusters. This topic describes how to create a replicator message routing task.

**Background information**

The replicator message routing feature of ApsaraMQ for RocketMQ is used to synchronize message data between clusters. You can configure routing rules to dynamically plan the synchronization path of messages. This way, the messages can be synchronized from the source node to the destination node based on filter conditions. This feature implements remote message synchronization across clusters within milliseconds and ensures data consistency and integrity across clusters. The following figure shows how replicator message routing works in ApsaraMQ for RocketMQ. In the figure, one-way synchronization is performed based on topics to synchronize messages from a specific source topic in the source instance to a specific destination topic in the destination instance. For more information, see Replicator message routing.

**Usage notes**

Only instances that have a namespace support the message routing feature. The message routing feature does not support chain routing. For example, you cannot create a task to route messages from Cluster A to Cluster B and then from Cluster B to Cluster C. You must create a task to route messages from Cluster A to Cluster C. The message type of the source topic must be the same as that of the destination topic. For example, if the message type of the source topic is normal message, the message type of the destination topic must also be normal message. A message routing task must be created in the production environment in which the destination cluster is deployed. If you want to route messages from Cluster A to Cluster B, you must create a message routing task in the cloud environment of Cluster B. When you create a message routing task, specify Cluster A as the source cluster and Cluster B as the destination cluster. Message routing consumes the CPU and memory resources of the source and destination clusters, and the storage resources of the destination cluster. You must evaluate the amount of resources that are required before you create a message routing task.

**Prerequisites**

An ApsaraMQ for RocketMQ instance is created. For more information, see Create an instance. A topic is created in the ApsaraMQ for RocketMQ instance. For more information, see Create a topic.

**Procedure**

To create a replicator message routing task, perform the following steps:

**Step 1: Create message synchronization clouds**

Before you create a message routing task, you must specify the information about the cloud on which your ApsaraMQ for RocketMQ cluster is deployed. The information includes the endpoint of the ApsaraMQ for RocketMQ instance and the AccessKey ID and AccessKey secret of the Apsara Stack tenant account to which the cloud belongs. ApsaraMQ for RocketMQ obtains the permissions to access ApsaraMQ for RocketMQ resources across clouds based on the cloud information that you specified.

**Step 2: Create a message routing task**

Specify the message source and the message destination, and configure relevant information. For example, specify filter conditions and set the start offset of message synchronization.

**Step 1: Create message synchronization clouds**

1. Log in to the ApsaraMQ for RocketMQ console.
2. In the left-side navigation pane, choose **Message Routing > Replicator**.
3. On the **replicator** page, click the **Cloud information** tab. On this tab, click **Create a**
**message synchronization cloud**.
4. In the **Create a message synchronization cloud** dialog box, configure the parameters
that are described in the following table and click **OK**.

**Note**

Creating a message route occupies the resources that are used to produce and consume messages in the message cluster. Carefully evaluate whether to perform the scale-out.

| Parameter | Description | Example |
|---|---|---|

| Cloud name | The name of the cloud from or to which you want to route messages. Note The combination of the cloud name and endpoint of the ApsaraMQ for RocketMQ instance uniquely identifies a message synchronization cloud. The combination must be unique. The cloud name can contain only letters, digits, hyphen (-), and underscores ( ). _ The cloud name must be 3 to 64 characters in length. | Center |
|---|---|---|
| AccessKey | The AccessKey ID of the account that is used to log in to the cloud. Make sure that the role of the account is the administrator of ApsaraMQ for RocketMQ or a user that is granted the permissions to write data to and read data from instances and topics. For more information about how to obtain the AccessKey ID, see Obtain an AccessKey pair in ApsaraMQ for RocketMQ Developer Guide. | j8geROUEAW1k**** |

| Region | The region in which the ApsaraMQ for RocketMQ cluster is deployed. The region is displayed in the top navigation bar of the ApsaraMQ for RocketMQ console. | cn-qingdao-****-d01 |
|---|---|---|
| Secret | The AccessKey secret of the account that is used to log in to the cloud. For more information about how to obtain the AccessKey secret, see Obtain an AccessKey pair in ApsaraMQ for RocketMQ Developer Guide. | AMx4ainrLWhT8jYUPHkdI4zY7t **** |
| MQ instance endpoint | The endpoint of ApsaraMQ for RocketMQ. For more information about how to obtain the endpoint of ApsaraMQ for RocketMQ, see the References section of this topic. | http://mq.server.****.com:808 0/rocketmq/nsaddr4client- internal |
| MQ API | The URL of the ApsaraMQ for RocketMQ console. The value of this parameter must be in the following format: http: {console.domain}/json . For more information about how to obtain the value of {console.domain}, see the References section of this topic. | http:mq.console.****.com/json |
| Note | The description of the cloud. You can specify a description that can help you identify the cloud. | Central node |

|   |   | http: |   |
|---|---|---|---|
|   | {console.domain}/json |   |   |

**Step 2: Create a message routing task**

1. Log in to the ApsaraMQ for RocketMQ console.
2. In the left-side navigation pane, choose **Message Routing > Replicator**.
3. On the **replicator** page, click the **Task** tab. On this tab, click **Create a task**.
4. In the **Create a task** dialog box, configure the parameters that are described in the
following table and click **OK**.

| Parameter | Description |
|---|---|
| Message Source | Message synchronization cloud: the name of the source cloud from which you want to route messages. Source region: the region in which the source ApsaraMQ for RocketMQ cluster is deployed. After you configure the Message synchronization cloud parameter, the system automatically displays the region in which the source cloud is deployed. You do not need to specify a value for this parameter. Source instance: the instance to which the source topic belongs. Source Topic: the name of the topic from which you want to route messages. |
| Message destination | Message synchronization cloud: the name of the destination cloud to which you want to route messages. Target region: the region in which the destination ApsaraMQ for RocketMQ cluster is deployed. After you configure the Message synchronization cloud parameter, the system automatically displays the region in which the destination cloud is deployed. You do not need to specify a value for this parameter. Target instance: the instance to which the destination topic belongs. Target Topic: the name of the topic to which you want to route messages. |
| Initial synchronization point | The consumer offset from which you want to route messages from the source topic to the destination topic. Default value: Maximum site. If this parameter is set to Maximum site, the message routing task routes messages to the destination topic starting from the most recent message in the source topic after the task is started. Important If this parameter is set to Maximum site, the messages that are sent to the source topic before the message routing task is started for the first time are not routed to the destination topic. |

| Filter rules | If no filter rules are specified, the message routing task routes all messages from the source topic to the destination topic. If filter rules are specified, the message routing task routes the messages that match the specified rules from the source topic to the destination topic. You can specify tags as filter rules. If the tag of the messages that you want to route to the destination topic is CartService, you can enter CartService in the Filter rules field. If you want to filter messages based on multiple tags, you can specify multiple tags and separate the tags with two vertical bars (\|\|). For example, you can enter CartService\|\|Inventory\|\|Payment . For more information, see Message filtering. |
|---|---|
| Description | The description of the message routing task, which helps you identify the task. |

**Modify cloud information**

1. On the **replicator** page, click the **Cloud information** tab.
2. On the Cloud information tab, find the cloud that you want to modify, move the pointer over
the value in the **Remarks** column, and then click the icon.
3. In the **Modify description** dialog box, modify the description and click **OK**.
4. In the message that appears, read the information and click **OK**.

**Delete a cloud**

1. On the **replicator** page, click the **Cloud information** tab.
2. On the Cloud Information tab, find the cloud that you want to delete and click **Delete** in the
**Operation** column.
3. In the message that appears, read the information and click **OK**.

**Start or stop a message routing task**

1. On the **replicator** page, click the **Task** tab.
2. On the Task tab, find the message routing task that you want to manage and click **Start** or
**Stop** in the **Operation** column to start or stop the task.

**Modify a message routing task**

**Important**

After you modify the **filter rules** of a task, you must stop the task and then restart the task to make the modification take effect.
1. On the **replicator** page, click the **Task** tab.
2. On the Task tab, find the message routing task that you want to modify and click **Modify** in
the **Operation** column.
3. In the **Edit task** dialog box, modify the configurations of the task and click **OK**.

**View the details of a message routing task**

1. On the **replicator** page, click the **Task** tab.
2. On the Task tab, find the message routing task that you want to view and click **Details** in
the **Operation** column. On the page that appears, view the details of the task. The following table describes the parameters that are included in the details of a message routing task.

|   | Parameter | Description |
|---|---|---|
| Task overview | Task Status | The status of the task. Valid values: Creating Created Running Paused |
|   | Message synchronization TPS | The average transactions per second (TPS) value that is collected at an interval of 1 minute. The TPS value indicates the number of messages that are routed from the source topic to the destination topic per second. |
|   | Message accumulation | The number of messages that are not routed to the destination topic. |
|   | Latest synchronization time | The point in time when the last message was routed. |
| Task details | Source Destination | The source and destination of the task. |
|   | Initial synchronization point | The offset to start data synchronization. |
|   | Filter rules | The filtering rules. |
| Message details | Message synchronization TPS | The average TPS value that is collected at an interval of 1 minute. The TPS value indicates the number of messages that are routed from the source topic to the destination topic per second. |

|   | Message latency | The time difference between the consumer offset of the most recent message that was routed and the consumer offset of the latest message. |
|---|---|---|
|   | Message accumulation | The number of messages that are not routed to the destination topic. |

**Delete a message routing task**

**Important**

After a message routing task is deleted, the task stops running.
1. On the **replicator** page, click the **Task** tab.
2. On the Task tab, find the message routing task that you want to delete and click **Delete** in
the **Operation** column.
3. In the message that appears, read the information and click **OK**.

**References**

**Obtain the endpoint of ApsaraMQ for RocketMQ and the URL of the ApsaraMQ for**

**RocketMQ console**

Before you create message synchronization clouds for message routing, you must perform the following steps to obtain the values of the **MQ instance endpoint** and **MQ API** parameters.
1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Apsara Infrastructure**
**Management** > **O&M Tools**.
3. In the left-side navigation pane, choose **O&M Tools** > **Service Registration Variable**
**Dashboard**.
4. On the **Service Registration Variable Dashboard** page, click **Advanced Filter**.
5. Enter `mq` in the **Service** field and click **Search**.
6. Obtain the value of the **MQ instance endpoint** parameter.
icon in the **Service Registration** column. i. Find the `mq-cai` service and click the ii. Click the text in the **Service Registration** column of the `mq-cai` service. In the
**Registration Variables** message, view the value of the **client.onsAddr** parameter. The
value of this parameter is used as the value of the **MQ instance endpoint** parameter.
7. Obtain the value of the **MQ API** parameter.
icon in the **Service Registration** i. Find the `mq-console` service and click the column. ii. Click the text in the **Service Registration** column of the `mq-console` service. In the
**Registration Variables** message, view the value of the **console.domain** parameter.
The value of the **MQ API** parameter is in the following format: http://{console.domain}/json.

### Connector

#### Elasticsearch

The Elasticsearch message routing feature provided by ApsaraMQ for RocketMQ can be used to route message data between Elasticsearch clusters. This topic describes how to create an Elasticsearch message routing task.

**Background information**

The Elasticsearch message routing feature provided by ApsaraMQ for RocketMQ is used to route message data between Elasticsearch clusters. You can route messages from the source Elasticsearch cluster to the specified ApsaraMQ for RocketMQ instance and then from the ApsaraMQ for RocketMQ instance to the destination Elasticsearch cluster. This ensures data consistency and integrity between Elasticsearch clusters.

**Prerequisites**

An ApsaraMQ for RocketMQ instance is created. For more information, see Create an instance. A topic is created in the ApsaraMQ for RocketMQ instance. For more information, see Create a topic. An Elasticsearch cluster is created. For more information, see **Create a cluster** in
**Elasticsearch User Guide**.

**Procedure**

To create an Elasticsearch message routing task, perform the following steps:

**Step 1: Create Elasticsearch cluster information**

Before you create a message routing task, you must specify the information about the Elasticsearch cluster. The information includes the region, username, password, and endpoint of the Elasticsearch cluster. ApsaraMQ for RocketMQ obtains the permissions to access Elasticsearch resources based on the Elasticsearch cluster information that you specified.

**Step 2: Create a message routing task**

Specify the message source and the message destination, and configure relevant information.

**Step 1: Create Elasticsearch cluster information**

1. Log in to the ApsaraMQ for RocketMQ console.
2. In the left-side navigation pane, choose **Message Routing > Connector**.
3. On the **ElasticSearch** tab, click the **Cloud Information** tab. Then, click **Create ES**
**instance information**.
4. In the **Create ES instance information** dialog box, configure the parameters that are
described in the following table and click **OK**.

| Parameter | Description |
|---|---|

| Cloud Information Name | The name of the cloud from or to which you want to route messages. You can customize the name. |
|---|---|
| Region | The region in which the Elasticsearch cluster resides. |
| Username | The username that is used to log in to the Elasticsearch cluster. |
| Password | The password that is used to log in to the Elasticsearch cluster. |
| ES Endpoint | The endpoint that is used to connect to the Elasticsearch cluster. The value is typically the private endpoint of the Elasticsearch cluster. |
| Note | The description of the cloud. You can specify a description that can help you identify the cloud. |

**Step 2: Create a message routing task**

1. Log in to the ApsaraMQ for RocketMQ console.
2. In the left-side navigation pane, choose **Message Routing > Connector**.
3. On the **ElasticSearch** tab, click the **Task** tab. Then, click **Create a task**.
4. In the **Create a task** dialog box, select a task type, configure the parameters, and then
click **OK**. i. **Source task**: Click the **Source** tab and configure the parameters that are described in the following table.

**Important**

Elasticsearch Source connectors support only full data synchronization and do not support real-time incremental data synchronization. After the task is executed, you must manually stop the Source task to prevent duplicate data synchronization upon restart (such as during a system upgrade).

| Parameter | Description |
|---|---|
| ES source | ES source: the cloud on which the source Elasticsearch cluster is deployed. Index: the index of the source Elasticsearch cluster. |
| MQ Objectives | Target instance: the ApsaraMQ for RocketMQ instance to which the destination topic belongs. Target Topic: the name of the topic to which you want to route messages. |
| Description | The description of the message routing task, which helps you identify the task. |

ii. **Sink task**: Click the **Sink** tab and configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| MQ Source | Source instance: the ApsaraMQ for RocketMQ instance to which the source topic belongs. Source Topic: the name of the topic from which you want to route messages. |
| ES target | ES target: the Elasticsearch cluster to which you want to route messages. Index: the index of the destination Elasticsearch cluster. |
| Description | The description of the message routing task, which helps you identify the task. |

**Delete a cloud**

1. On the **ElasticSearch** tab, click the **Cloud Information** tab.
2. On the Cloud Information tab, find the cloud that you want to delete and click **Delete** in the
**Operation** column.
3. In the message that appears, read the information and click **OK**.

**Start or stop a message routing task**

1. On the **ElasticSearch** tab, click the **Task** tab.
2. On the Task tab, find the message routing task that you want to manage and click **Start** or
**Stop** in the **Operation** column to start or stop the task.

**Delete a message routing task**

**Important**

After a message routing task is deleted, the task stops running.
1. On the **ElasticSearch** tab, click the **Task** tab.
2. On the Task tab, find the message routing task that you want to delete and click **Delete** in
the **Operation** column.
3. In the message that appears, read the information and click **OK**.

#### Redis

The Tair (Redis OSS-compatible) message routing feature provided by ApsaraMQ for RocketMQ can be used to route message data between Tair (Redis OSS-compatible) clusters. This topic describes how to create a Tair (Redis OSS-compatible) message routing task.

**Background information**

The Tair (Redis OSS-compatible) message routing feature provided by ApsaraMQ for RocketMQ is used to route messages from an ApsaraMQ for RocketMQ instance to the specified Tair (Redis OSS-compatible) instance.

**Prerequisites**

An ApsaraMQ for RocketMQ instance is created. For more information, see Create an instance. A topic is created in the ApsaraMQ for RocketMQ instance. For more information, see Create a topic. A Tair (Redis OSS-compatible) instance is created. For more information, see **Create an**
**instance** in **ApsaraDB for Redis User Guide**.

**Procedure**

To create a Tair (Redis OSS-compatible) message routing task, perform the following steps:

**Step 1: Create Tair (Redis OSS-compatible) connection information**

Before you create a message routing task, you must specify the information about the Tair (Redis OSS-compatible) instance. The information includes the endpoint, port number, password, and ID of the Tair (Redis OSS-compatible) instance. ApsaraMQ for RocketMQ obtains the permissions to access Tair (Redis OSS-compatible) resources based on the Tair (Redis OSS-compatible) instance information that you specified.

**Step 2: Create a message routing task**

Specify the message source and the message destination, and configure relevant information.

**Step 1: Create Tair (Redis OSS-compatible) connection**

**information**

1. Log in to the ApsaraMQ for RocketMQ console.
2. In the left-side navigation pane, choose **Message Routing > Connector**.
3. Click the **Redis** tab. On the **Cloud Information** tab, click **Create Redis Connection**.
4. In the **Create Redis Connection** dialog box, configure the parameters that are described
in the following table and click **OK**.

| Parameter | Description |
|---|---|
| Connection Name | The alias of the Tair (Redis OSS-compatible) connection. You can specify an alias that can help you identify the Tair (Redis OSS- compatible) connection. |
| Redis Address | The endpoint of the Tair (Redis OSS-compatible) server. |
| Redis Port | The number of the TCP port on which the Tair (Redis OSS-compatible) service listens. |
| Redis Password | The password used to connect to the Tair (Redis OSS-compatible) instance. |
| Redis Database | The number of the logical database to which you want to connect. Note By default, Tair (Redis OSS-compatible) supports 16 databases numbered from 0 to 15. |
| Note | The description of the cloud. You can specify a description that can help you identify the cloud. |

**Step 2: Create a message routing task**

1. Click the **Redis** tab. On the **Task** tab, click **Create Task**.
2. In the **Create Task** dialog box, configure the parameters that are described in the
following table and click **OK**.

| Parameter | Description |
|---|---|
| MQ Source | Source Instance: the ApsaraMQ for RocketMQ instance to which the source topic belongs. Source Topic: the name of the topic from which you want to route messages. |

| Redis Target | Redis Connection: the Tair (Redis OSS-compatible) connection to which messages are synchronized. Redis Command: specifies how messages are written to Tair (Redis OSS-compatible). Valid values: SET HSET: If you select HSET, you must also configure the Hash Field parameter. LPUSH RPUSH SADD ZADD Key Strategy: specifies how keys are generated to store data in Tair (Redis OSS-compatible). Valid values: RECORD TOPIC TOPIC PARTITION _ CUSTOM: If you select CUSTOM, you must also configure the Key Prefix parameter, which indicates the fixed prefix of the keys. Key TTL (seconds): the automatic expiration time for the generated Tair (Redis OSS-compatible) keys to prevent unlimited memory growth. Unit: seconds. |
|---|---|
| Description | The description of the message routing task, which helps you identify the task. |

**Delete a cloud**

1. On the **Redis** tab, click the **Cloud Information** tab.
2. In the cloud information list, find the cloud that you want to delete and click **Delete** in the
**Operation** column.
3. In the message that appears, read the information and click **OK**.

**Start or stop a message routing task**

1. On the **Redis** tab, click the **Task** tab.
2. On the Task tab, find the message routing task that you want to manage and click **Start** or
**Stop** in the **Operation** column to start or stop the task.

**Delete a message routing task**

**Important**

After a message routing task is deleted, the task stops running.
**Running** tasks cannot be deleted.
1. On the **Redis** tab, click the **Task** tab.
2. On the Task tab, find the message routing task that you want to delete and click **Delete** in
the **Operation**.
3. In the message that appears, read the information and click **OK**.

#### OSS

RocketMQ can sync messages to an Object Storage Service (OSS) bucket using the message routing feature. This topic describes how to configure a message routing task for OSS.

**Background information**

The message routing feature of RocketMQ syncs messages from a RocketMQ instance to an OSS bucket.

**Prerequisites**

You have created a RocketMQ instance. For more information, see Create an instance. You have created a topic. For more information, see Create a topic. You have created an OSS bucket. For more information, see **Object Storage Service**
**User Guide > Create a Bucket**.

**Procedure**

Follow these steps to configure an OSS message routing task:

**Step 1: Create OSS cloud information**

Before you create a routing task, you must provide information about the destination OSS bucket, such as its endpoint and name. RocketMQ uses this information to obtain the permissions required to access OSS resources.

**Step 2: Create a routing task**

Specify the message source, destination, and task description.

**Step 1: Create OSS cloud information**

1. Log on to the RocketMQ console.
2. In the navigation pane on the left, click **Message Routing > Connector**.
3. Click the **OSS** tab, click the **Cloud Information** subtab, and then click **Create OSS Cloud**
**Information**.
4. In the **Create OSS Cloud Information** dialog box, configure the following parameters and
click **OK**.

| Parameter | Description |
|---|---|
| Cloud Information Name | Enter a custom name for the cloud information. |
| OSS Endpoint | The regional endpoint of the OSS service. |
| OSS Bucket | The name of the bucket that you want to access. |

| AccessKey ID | Enter the AccessKey ID of an account that has permissions on the OSS instance. For information about how to obtain an AccessKey, see the Obtain an AccessKey topic in the RocketMQ Developer Guide. |
|---|---|
| AccessKey Secret | Enter the AccessKey secret of an account that has permissions on the OSS instance. For information about how to obtain an AccessKey, see the Obtain an AccessKey topic in the RocketMQ Developer Guide. |
| Remarks | Enter a description or remarks for the cloud information for identification and record- keeping. |

**Step 2: Create a routing task**

1. On the **OSS** tab, click the **Task** subtab, and then click **Create Task**.
2. In the **Create Task** dialog box, configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| MQ Source | Source Instance: Select the RocketMQ instance where the topic of the messages to be synced is located. Source Topic: Select the name of the topic to which the messages to be synced belong. |
| OSS Destination | OSS Cloud Information: Select the OSS cloud information that you created in the previous step. Object Key Prefix: Define the file path prefix for writing to OSS. This is used to organize the directory structure. Compression Type: Select the compression format for the output file. Valid values: No compression: The file is in a raw text format, such as .json or .txt . GZIP: Provides a high compression ratio. This format is suitable for log data. Minimum Records per File: The value must be greater than 0. When the number of accumulated messages reaches this value, a file is immediately written and rotated. Default value: 10000 . File Rotation Interval (ms): The value must be greater than 0. A new file is generated at the specified interval, even if the maximum number of records is not reached. Default value: 300000 (5 minutes). |

| Task Description | Enter a description or remarks for the sync task for identification and record-keeping. |
|---|---|

**Delete cloud information**

1. On the **OSS** tab, click the **Cloud Information** subtab.
2. In the cloud information list, find the cloud information that you want to delete and click
**Delete** in the **Actions** column.
3. In the dialog box, read the message and click **OK**.

**Start or stop a routing task**

1. On the **OSS** tab, click the **Task** subtab.
2. In the routing task list, find the task that you want to start or stop. In the **Actions** column,
click **Start** to start the task or click **Stop** to stop the task.

**Delete a routing task**

**Important**

Deleting a routing task stops it from running. You cannot delete a task that is in the **running** state.
1. On the **OSS** tab, click the **Task** subtab.
2. In the routing task list, find the task that you want to delete and click **Delete** in the
**Actions** column.
3. In the dialog box, read the message and click **OK**.

#### MySQL

Use the MySQL message routing feature in ApsaraMQ for RocketMQ to synchronize data between different MySQL instances. This topic explains how to configure a MySQL routing task.

**Background information**

The MySQL message routing feature of ApsaraMQ for RocketMQ synchronizes messages from an ApsaraMQ for RocketMQ instance to a target MySQL instance.

**Prerequisites**

You have created an ApsaraMQ for RocketMQ instance. For more information, see Create an instance. You have created a topic. For more information, see Create a topic. You have created a target MySQL instance.

**Procedure**

**Step 1: Create a MySQL connection**

Before creating a routing task, provide the connection information for your MySQL instance, including its address, username, and password. ApsaraMQ for RocketMQ uses this information to access your MySQL resources.

**Step 2: Create a routing task**

Specify the message source and destination, and configure other settings such as a description.

**Step 1: Create a MySQL connection**

1. Log on to the ApsaraMQ for RocketMQ console.
2. In the left-side navigation pane, click **Message Routing > Connector**.
3. Click the **MySQL** tab, click the **Cloud information** subtab, and then click **Create MySQL**
**connection**.
4. In the **Create MySQL connection** dialog box, configure the following parameters and click
**OK**.

| Parameter | Description |
|---|---|
| Connection name | Enter a name for the connection to help you identify and manage it. |
| MySQL address | The connection address for the MySQL instance. The format is host:port/database , for example, rm-xxx:3306/mydb . |
| Username | Enter the username for the MySQL instance. Note A Change Data Capture (CDC) source uses the MySQL binary log (binlog) for real-time synchronization. The database account requires the following permissions: SELECT : To read all data from the table during a snapshot. REPLICATION SLAVE : To connect to MySQL and read the binlog stream. REPLICATION CLIENT : To execute SHOW MASTER STATUS and get the binlog position. RELOAD : To apply a global read lock during a snapshot to ensure data consistency. |
| Password | Enter the password for the MySQL instance. |
| Remarks | Enter a description for the connection information for identification and management. |

|   | host:port/database |
|---|---|
| rm-xxx:3306/mydb |   |

**Step 2: Create a routing task**

1. On the **MySQL** tab, click the **Tasks** subtab, and then click **Create task**.
2. In the **Create Task** dialog box, configure the parameters, and then click **OK**.
i. **Source task:** Click the **Source (MySQL→MQ)** tab and configure the following parameters:

| Parameter | Description |
|---|---|
| MySQL source | MySQL connection: Select the MySQL connection for the data source. Tables to synchronize: Enter the tables to synchronize. The format is database.table . Use commas to separate multiple tables. |
| MQ target | MQ instance: Select the ApsaraMQ for RocketMQ instance where the target topic is located. Topic: Select the target topic. |
| Description | Enter a description for the task for identification and management. |
| Advanced settings | You can configure data transformations. For more information, see Advanced settings. |

ii. **Sink task:** Click the **Sink (MQ→MySQL)** tab and configure the following parameters:

| Parameter | Description |
|---|---|
| MQ source | MQ instance: Select the ApsaraMQ for RocketMQ instance where the source topic is located. Topic: Select the source topic. |

| MySQL target | MySQL connection: Select the connection information for the target MySQL instance. Write mode: Select the data writing strategy. Upsert: Updates the record if the primary key exists; otherwise, inserts a new record. Insert: Inserts new records only. Update: Updates existing records only. Primary key fields: Specify the primary key fields in the MySQL table. Use commas to separate multiple field names. Auto create table: Select whether to automatically create tables in the target MySQL instance if they do not exist. Auto-sync DDL: Specify whether to synchronize Data Definition Language (DDL) changes, such as table schema modifications, from the source. Sync DELETE: Specify whether to process delete operations. Yes: When a delete message is received, the corresponding delete operation is performed in the target MySQL instance. No: Ignores DELETE messages and only processes INSERT and UPDATE operations. Consumption starting point: Specify where the task starts consuming messages. You can select From earliest message or From latest message. |
|---|---|
| Description | Enter a description for the task for identification and management. |
| Advanced settings | You can configure data transformations. For more information, see Advanced settings. |

**Advanced settings**

ApsaraMQ for RocketMQ Connect provides five built-in single message transforms (SMTs) for MySQL. You can use SMTs to process messages in real time during data synchronization without modifying the upstream or downstream services:

| Transform | Function | Typical scenario |
|---|---|---|
| Field renaming (key)/Field renaming (value) | Renames one or more fields based on a regular expression. | Upstream and downstream column names differ, for example, from user id to _ uid . |

| Naming style conversion (value) | Converts field names between different naming styles, such as from snake case to camelCase. _ | Align the naming conventions of a Java service with those of a data warehouse. |
|---|---|---|
| Nullify field (value) | Sets the values of fields matching a regular expression to null. | Data masking, such as clearing phone numbers or ID numbers during synchronization. |
| Row filtering (value) | Discards messages if a field's value matches a regular expression. | Synchronize only specific business data, such as orders from a particular region. |

**Core benefits**:
**Zero-code integration**: All transforms are configured through the console, eliminating the
need to develop custom plug-ins.
**Flexible combination**: Multiple transforms can be chained together to meet complex
processing requirements.
**Enforce standards**: Implement data masking, naming conventions, and filtering rules
early in the synchronization pipeline to reduce downstream data governance costs. Click **Add Transform**, select a transform type, and then configure its parameters:

**Note**

You can add multiple data transforms. They are executed sequentially from top to bottom.
**Field renaming (key)**/**Field renaming (value)**

| Parameter | Description |
|---|---|
| Field name regex | Enter a regular expression to match the original field names you want to rename. |
| Replacement field name | Enter the new field name. If the Field name regex matches multiple fields, this new name is applied to all matched fields. |
| Regex flags | Set the matching mode for the regular expression. |

**Row filtering (value)**

| Parameter | Description |
|---|---|
| Value regex (discard message on match) | Enter a regular expression. If the value of a specified field matches the expression, the entire message is discarded. |

| Fields to check (comma- separated) | Specify one or more field names to which the Value regex (discard message on match) rule applies. |
|---|---|

**Naming style conversion (value)**

| Parameter | Description |
|---|---|
| Source naming style | Select the current naming style of the fields. LOWER UNDERSCORE _ LOWER CAMEL _ UPPER UNDERSCORE _ UPPER CAMEL _ LOWER HYPHEN _ |
| Target naming style | Select the target naming style to which you want to convert. LOWER UNDERSCORE _ LOWER CAMEL _ UPPER UNDERSCORE _ UPPER CAMEL _ LOWER HYPHEN _ |

**Nullify field (value)**

| Parameter | Description |
|---|---|
| Field name regex | Enter a regular expression to match the names (keys) of the fields whose values you want to set to null. |
| Placeholder parameter | This is a reserved parameter. You can leave it empty or keep the default value. |

**Delete a connection**

1. On the **MySQL** tab, click the **Cloud information** subtab.
2. In the list, find the connection that you want to delete and click **Delete** in the **Actions**
column.
3. Read the message in the dialog box carefully and click **OK**.

**Start or stop a routing task**

1. On the **MySQL** tab, click the **Tasks** subtab.
2. In the list of routing tasks, find the task you want to manage. To start the task, click **Start**
in the **Actions** column. To stop the task, click **Stop**.

**Delete a routing task**

**Important**

Deleting a routing task also stops the task. You cannot delete a task that is in the **Running** state.
1. On the **MySQL** tab, click the **Tasks** subtab.
2. In the list of routing tasks, find the task you want to delete and click **Delete** in the **Actions**
column.
3. Read the message in the dialog box carefully and then click **OK**.

## SDK user guide

### Overview

This topic lists the protocols supported by ApsaraMQ for RocketMQ and the related SDKs for multiple programming languages.

**SDKs for different protocols and programming languages**

The following table lists the protocols and SDKs for multiple programming languages that are supported by ApsaraMQ for RocketMQ.

| Protocol | Programming language | SDK download link | Sample code |
|---|---|---|---|
| TCP | Java | mq-tcp-java-sdk | mq-tcp-samples-java |
|   | C/C++ | mq-tcp-csharp-sdk | mq-tcp-samples- csharp |
|   | .NET | mq-tcp-.net-sdk | mq-tcp-samples-.net |
| HTTP | Java | mq-http-java-sdk | mq-http-samples-java |
|   | PHP | mq-http-php-sdk | mq-http-samples-php |
|   | Go | mq-http-go-sdk | mq-http-samples-go |
|   | Python | mq-http-python-sdk | mq-http-samples- python |
|   | Node.js | mq-http-nodejs-sdk | mq-http-samples- node.js |
|   | C# | mq-http-cpp-sdk | mq-http-samples-cpp |
|   | C++ | mq-http-csharp-sdk | mq-http-samples- csharp |

**Usage notes**

ApsaraMQ for RocketMQ provides TCP client SDKs and HTTP client SDKs for you to send and consume messages. You cannot specify the same group ID in the code of a TCP client SDK and the code of an HTTP client SDK at the same time. If you want to use a TCP client SDK to send and consume messages, you must create a group for the TCP protocol. You cannot specify a group that is created for the HTTP protocol in the code of the TCP client SDK. A ApsaraMQ for RocketMQ instance provides a TCP endpoint and an HTTP endpoint. An endpoint for a specific protocol must be used together with an SDK for the same protocol. For example, if you want to use a TCP client SDK to send and consume messages, you must obtain the TCP endpoint of your ApsaraMQ for RocketMQ instance. You cannot use the HTTP endpoint to connect to the instance.

### SDK user guide

#### Demo projects

##### Overview

This topic helps engineers who are new to ApsaraMQ for RocketMQ to build a ApsaraMQ for RocketMQ test project. The demo project is a Java project. It contains test code for normal messages, transactional messages, and scheduled messages. The demo project also contains Spring configurations.

##### Prepare the environment

This topic describes how to prepare an environment for a ApsaraMQ for RocketMQ demo project.

**Procedure**

Install an integrated development environment (IDE). You can use IntelliJ IDEA or Eclipse as the IDE. IntelliJ IDEA is used in this example. Download IntelliJ IDEA Ultimate Edition from IntelliJ IDEA. Then, follow the installation instructions to install IntelliJ IDEA Ultimate Edition. Download a demo project. Download a demo project from GitHub to your on-premises machine. Figure 1. Download a demo project After the downloaded package is decompressed, a folder named mq-demomaster appears on your on-premises machine.

##### Configure a demo project

This topic describes how to configure a demo project.

**Prerequisites**

You have prepared the environment for the demo project. You have installed the JDK on your on-premises machine. For more information, visit Java SE Downloads. We recommend that you use JDK 8.

**Procedure**

1. Import the demo project to IntelliJ IDEA.
i. On the IntelliJ IDEA page, click **Import Project** and select the mq-demo-master folder. Figure 1. Select the mq-demo-master folder ii. Select Import project from external model. Figure 2. Select Import project from external model iii. Click **Next** until the project is imported. The JAR dependency needs to be loaded to the demo project. Therefore, it takes two to three minutes to import the project.
2. Creates resources.
Create the required resources, such as topics and group IDs in the ApsaraMQ for RocketMQ console and obtain the AccessKey pair in the Apsara Uni-manager Management Console for identity authentication. i. For more information about how to create topics and group IDs, see Create resources. ii. Perform the following operations to obtain the AccessKey ID and AccessKey secret: In the Apsara Uni-manager Management Console, move your pointer over the profile picture and select **User Information**. On the page that appears, view the AccessKey ID and AccessKey secret in the **Apsara Stack AccessKey Pair** section.
3. Configure the demo.
Configure the MqConfig class and the common.xml file. i. The following sample code provides an example on how to configure the MqConfig class:

```
public static final String TOPIC = "The topic that you created in the ApsaraMQ for RocketMQ console." public static final String GROUP_ID = "The group ID that you created in the ApsaraM Q for RocketMQ console." public static final String ACCESS_KEY = "The AccessKey ID that you created in the A psara Uni-manager Management Console for identity authentication." public static final String SECRET_KEY = "The AccessKey secret that you created in t he Apsara Uni-manager Management Console for identity authentication." public static final String NAMESRV_ADDR = "The TCP endpoint of your ApsaraMQ for Ro cketMQ instance. You can obtain the endpoint in the ApsaraMQ for RocketMQ console."
```

**Note**

You must use the AccessKey ID and AccessKey secret of the account that you use to create the topic. ii. Configure the common.xml file.

```xml
 <props>
 <prop key="AccessKey">XXX</prop> <!-- Modify the values based on your resources --
```

`>`

```
 <prop key="SecretKey">XXX</prop>
 <prop key="GROUP_ID">XXX</prop>
 <prop key="Topic">XXX</prop>
 <prop key="NAMESRV_ADDR">XXX</prop>
</props>
```

##### Run the demo project

After you configure the demo project, you can start the corresponding classes to send and receive messages of different types.

**Call the main method to send and receive messages**

1. Run the SimpleMQProducer class to send a message.
2. Log on to the ApsaraMQ for RocketMQ console. On the Instances page, click the ID of the
instance that you want to manage. On the **Instance details** page, click the **Message**
**query** tab and then click the **Query by Topic** tab. On the Query by Topic tab, select a
topic name from the Topic drop-down list. Check whether the message is sent to the selected topic.
3. Run the SimpleMQConsumer class to receive the message. You can view logs to check
whether the message is received. The class needs to be initialized, which takes several seconds. Initialization seldom occurs in the production environment. On the Instance Details page, click the **Group management** tab. On the Group management tab, find the group ID that you want to manage and click **Consumer status** in the **Operation** column. In the **Consumer status** panel, the information shows that the started consumers are online and subscribed to the selected topic.

**Use Spring to send and receive messages**

1. Run the ProducerClient class to send a message.
2. Run the ConsumerClient class to receive the message.
On the Instance Details page, click the **Group management** tab. On the Group management tab, find the group ID that you want to manage and click **Consumer status** in the **Operation** column. In the **Consumer status** panel, the information shows that the started consumers are online and subscribed to the selected topic.

**Send transactional messages**

Run the SimpleTransactionProducer class to send a message.

**Note**

The LocalTransactionCheckerImpl class is used to check the status of local transactions. This class is used to check whether a local transaction is committed. For more information, see Send and subscribe to transactional messages.

**Send and receive ordered messages**

Run the SimpleOrderConsumer class to receive a message. Run the SimpleOrderProducer class to send a message.

**Note**

Ordered messages are sent and consumed in first-in-first-out (FIFO) order. For more information, see Send and receive ordered messages.

**Send scheduled or delayed messages**

Run the MQTimerProducer class to send a message. The message is delivered after a delay of 3 seconds.

**Note**

You can specify an exact delay, which can be up to 40 days. For more information, see Send and subscribe to scheduled messages.

#### Client parameters

This topic describes the parameters that are configured for ApsaraMQ for RocketMQ clients. Table 1. Client parameters

| Parameter | Client | Default value | Recommend ed value | Description | Client version |
|---|---|---|---|---|---|

| AccessKey | Producer or consumer | Configured by the user | Configured by the user | The AccessKey ID that is used to authenticate the user. | >=1.2.7.Final |
|---|---|---|---|---|---|
| SecretKey | Producer or consumer | Configured by the user | Configured by the user | The AccessKey secret that is used to authenticate the user. | >=1.2.7.Final |
| NAMESRV AD _ DR | Producer or consumer | Generated after deployment | Generated after deployment | The endpoint that is used to connect to ApsaraMQ for RocketMQ. | >=1.2.7.Final |
| MsgTraceSwit ch | Producer or consumer | true | true | Specifies whether to enable the message tracing feature of ApsaraMQ for RocketMQ. | >=1.7.0.Final |
| GROUP ID _ | Producer or consumer | Created in the console | Created in the console | The ID of the group to which the producer or consumer client belongs. Group IDs are compatible with producer IDs (PIDs) or consumer IDs (CIDs) in earlier versions. | >=1.7.8.Final |

| ProducerId | Producer | Created in the console | Created in the console | The ID of the group to which the producer client belongs. This parameter takes effect only on transactional messages. If a producer client fails, the ApsaraMQ for RocketMQ broker initiates requests to check the status of transactional messages on other producer clients in the same group. | >=1.2.7.Final |
|---|---|---|---|---|---|
| SendMsgTime outMillis | Producer | 5000 | Default | The timeout period for sending a message. If the ApsaraMQ for RocketMQ broker does not return an acknowledgm ent to the producer client within the specified period of time, the producer client determines that the message failed to send. | >=1.2.7.Final |
| ConsumerId | Consumer | Created in the console | Created in the console | The ID of the group to which the consumer client belongs. | >=1.2.7.Final |

| MessageMode l | Consumer | CLUSTERING | Default | The consumption mode. Valid values: CLUSTERING and BROADCASTI NG. CLUSTERING specifies that each subscribed message is received only by one consumer client. BROADCASTI NG specifies that each subscribed message is received by all consumer clients. | >=1.2.7.Final |
|---|---|---|---|---|---|
| ConsumeThre adNums | Consumer | Dynamically adjusted from 20 to 64 | Adjusted based on business requirements | The number of consumer threads. In most cases, this parameter is set to a larger value if a longer time is required to consume a single message. | >=1.2.7.Final |
| MaxReconsu meTimes | Consumer | 16 | Default | The maximum number of delivery retries that can be performed when a message fails to be consumed. | >=1.2.7.Final |

| ConsumeTim eout | Consumer | 15 | Default | The timeout period for consumption of each message. If the time to consume a message exceeds the specified timeout period, the message fails to be consumed and is redelivered after a retry interval. Configure an appropriate value for each type of application. Unit: minute. | >=1.2.7.Final |
|---|---|---|---|---|---|

| PostSubscripti onWhenPull | Consumer | false | Adjusted based on the consumption mode | Specifies whether to carry the latest subscription together with each request. If MessageMode l is set to BROADCASTI NG, this parameter must be set to true to prevent messages from failing to be received due to subscription inconsistency . If MessageMode l is set to CLUSTERING, this parameter must be set to false because subscription consistency is required for clustering consumption. | >=1.2.7.Final |
|---|---|---|---|---|---|

| ConsumeMes sageBatchMa xSize | Consumer | 1 | Adjusted based on business requirements | The maximum number of messages that can be consumed in each batch. The actual number of messages that are consumed in a batch can be smaller than the value of this parameter. The value must be an integer from 1 to 32. The default value is 1. | >=1.6.0.Final |
|---|---|---|---|---|---|
| MaxCachedM essageAmoun t | Consumer | 5000 | Adjusted based on the memory of consumer clients | The maximum number of messages that a consumer client can cache. A large value can cause an out of memory (OOM) issue on the client. The value must be an integer from 100 to 50000. The default value is 5000. | >=1.7.0.Final |

| MaxCachedM essageSizeIn MiB | Consumer | 512 | Adjusted based on the memory of consumer clients | The maximum size of messages that a consumer client can cache. A large value can cause an out of memory (OOM) issue on the client. The value ranges from 16 to 2048. The default value is 512. Unit: MB. | >=1.7.0.Final |
|---|---|---|---|---|---|

#### Client error codes

This topic describes error codes related to sending and subscribing to messages and their references.

**Error codes related to sending and subscribing to messages**

| HTTP status code | Status flag | Description | Cause and recommended solution | Broker version |
|---|---|---|---|---|
| 13 | MESSAGE ILLEGA _ L | This error is returned when the message verification fails. | Check whether the message body is empty. Check whether the length of the message property exceeds 32,767 bytes. Check whether the total size of the message exceeds 4 MB. | >=4.0.1 |

| 17 | TOPIC NOT EXIS _ _ T | This error is returned when the specified message topic does not exist. | 1. Create a topic in the ApsaraMQ for RocketMQ console. 2.Restart your application. For more information, see the "Nonexistent topic" section in the Nonexistent resources topic. | >=4.0.1 |
|---|---|---|---|---|
| 26 | SUBSCRIPTION G _ ROUP NOT EXIST _ _ | This error is returned if the specified group ID does not exist. | 1.Create a group ID in the ApsaraMQ for RocketMQ console. 2.Restart your application. For more information, see the "Nonexistent group ID" section in the Nonexistent resources topic. | >=4.0.1 |
| 24 | SUBSCRIPTION N _ OT EXIST _ | This error is returned when the subscription does not exist. | 1.Check whether the consumers identified by the group ID have been started. 2.Check whether subscription inconsistency occurs between consumers identified by the group ID. | >=4.0.1 |
| 23 | SUBSCRIPTION P _ ARSE FAILED _ | This error is returned when the system failed to parse the subscription expression. | Check the corresponding topic subscription expression and tag. | >=4.0.1 |

| 25 | SUBSCRIPTION N _ OT LATEST _ | This error is returned if subscription inconsistency occurs. | If this status continues for a moment, it is automatically restored. For more information, see Inconsistent subscriptions. | >=4.0.1 |
|---|---|---|---|---|
| 14 | SERVICE NOT AV _ _ AILABLE | This error is returned when messages cannot be sent. | The requested ApsaraMQ for RocketMQ broker is discontinued, the broker is abnormal and does not support write operations, or the broker is a standby broker. For more information, see the "The message failed to be sent." section in the Usage- related exceptions topic. | >=4.0.1 |
| 16 | NO PERMISSION _ (message sending) | This error is returned when the request is invalid. | The requested ApsaraMQ for RocketMQ broker disallows write operations. The topic on the requested ApsaraMQ for RocketMQ broker disallows write operations. The requested ApsaraMQ for RocketMQ broker disallows transactional messages. | >=4.0.1 |

| 16 | NO PERMISSION _ (message subscription) | This error is returned when the request is invalid. | The requested ApsaraMQ for RocketMQ broker disallows read operations. The current consumer group does not have the read permissions. The pulled topic disallows read operations. The current consumer group disallows message broadcasting. | >=4.0.1 |
|---|---|---|---|---|
| 1 | SYSTEM ERROR _ | This error is returned when a system exception occurs. | This is a temporary timeout that results from the restart of the ApsaraMQ for RocketMQ broker or heavy load on the broker. For more information, see the "The message failed to be sent." section in the Usage- related exceptions topic. | >=4.0.1 |
| 1 | SYSTEM ERROR _ (permission verification) | This error is returned when the permission verification fails. | Check whether the user is granted the permissions to publish messages to and subscribe messages from the topic. | >=4.0.1 |

| 2 | SYSTEM BUSY _ | This error is returned when the system is busy and the request is denied. | This is a temporary timeout that results from the restart of the ApsaraMQ for RocketMQ broker or heavy load on the broker. For more information, see the "The message failed to be sent." section in the Usage- related exceptions topic. | >=4.0.1 |
|---|---|---|---|---|

#### SDK for Java

##### Usage notes

ApsaraMQ for RocketMQ provides SDK for Java for you to send and subscribe to messages. This topic describes the parameters of Java methods and how to call these methods. Table 1. Common parameters

| Parameter | Description |
|---|---|
| NAMESRV ADDR _ | The TCP endpoint. You can obtain the endpoint on the Instance Details page in the ApsaraMQ for RocketMQ console. |
| AccessKey | The AccessKey ID that you created in the Apsara Uni-manager Management Console for identity authentication. |
| SecretKey | The AccessKey secret that you created in the Apsara Uni- manager Management Console for identity authentication. |
| OnsChannel | The source of the user. Default value: ALIYUN. |

Table 2. Parameters for sending messages

| Parameter | Description |
|---|---|

| SendMsgTimeoutMillis | The timeout period for sending messages. Unit: milliseconds. Default value: 3000. |
|---|---|
| CheckImmunityTimeInSeconds (for transactional messages) | The shortest time interval before the first back- check for the status of local transaction. Unit: seconds. |
| shardingKey (for ordered messages) | The partition key that is used to determine the partitions to which ordered messages are distributed. |

Figure 1. Methods and parameters for using SDK for Java to send messages Table 3. Parameters for subscribing to messages

| Parameter | Description |
|---|---|
| GROUP ID _ | The group ID that you created in the ApsaraMQ for RocketMQ console. |
| MessageModel | The mode in which a consumer instance consumes messages. Valid values: CLUSTERING and BROADCASTING. Default value: CLUSTERING. |
| ConsumeThreadNums | The number of consumer threads for a consumer instance. Default value: 64. |
| MaxReconsumeTimes | The maximum number of delivery retries for a message that fails to be consumed. Default value: 16. |

| ConsumeTimeout | The maximum timeout period for consuming a message. If a message fails to be consumed within this period, the consumption fails and the message can be redelivered. A proper value must be set for each type of business. Unit: minutes. Default value: 15. |
|---|---|
| suspendTimeMillis (for ordered messages) | The interval between delivery retries for an ordered message that fails to be consumed. |
| maxCachedMessageAmount | The maximum number of messages cached on the on- premises client. Default value: 1000. |
| maxCachedMessageSizeInMiB | The maximum size of messages cached on the on-premises client. Valid values: 16 MB to 2 GB. Default value: 512 MB. |

Figure 3. Methods and parameters for using SDK for Java to subscribe to messages

**Sample code for sending and subscribing to messages**

Send and subscribe to normal messages Send and receive ordered messages Send and subscribe to scheduled messages Send and subscribe to delayed messages Send and receive transactional messages

##### Prepare the environment

Before you run the Java code provided in this topic, prepare the environment based on the following instructions:

**Procedure**

1. Introduce the dependency by using one of the following methods:
Introduce the dependency by using Maven:

```xml
<dependency>
    <groupId>com.aliyun.openservices</groupId>
   <artifactId>ons-client</artifactId>
   <version>1.8.4.Final</version>
</dependency>
```

Download the JAR dependency.
2. Go to the console to create the topics and group IDs involved in the code.
You can customize message tags in your application. For more information about how to create a message tag, see Create resources.
3. For applications that use the TCP client SDK to access ApsaraMQ for RocketMQ, make sure
that the applications are deployed on Elastic Compute Service (ECS) instances in the same region.

##### Configure logging

Client logs record exceptions that occur when the ApsaraMQ for RocketMQ clients are running. Client logs help you locate and handle these exceptions in a quick manner. This topic describes how to print the logs of a ApsaraMQ for RocketMQ client and provides the default and custom configurations.

**Print client logs**

TCP client SDK for Java of ApsaraMQ for RocketMQ is programmed by using the Simple Logging Facade for Java (SLF4J). ApsaraMQ for RocketMQ **SDK for Java 1.7.8.Final or later** ApsaraMQ for RocketMQ SDK for Java 1.7.8.Final has a built-in framework for logging. You do not need to add a dependency on the corresponding logging framework for an application on the client before you print the logs of a ApsaraMQ for RocketMQ client. For information about the default logging configuration for a ApsaraMQ for RocketMQ client and how to modify this configuration, see Configure logging for a ApsaraMQ for RocketMQ client. ApsaraMQ for RocketMQ **SDK for Java versions earlier than 1.7.8.Final** ApsaraMQ for RocketMQ SDK for Java versions earlier than 1.7.8.Final support only Log4j and Logback. These versions do not support Log4j2. For these versions, you must add a dependency on the corresponding logging framework to the pom.xml file or the .lib file before you print the logs of a ApsaraMQ for RocketMQ client. The following sample code provides examples on how to add dependencies on Log4j and Logback:

**Method 1: Use Log4j as the logging framework**

```xml
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>jcl-over-slf4j</artifactId>
    <version>1.7.7</version>
</dependency> <dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-log4j12</artifactId>
    <version>1.7.7</version>
</dependency> <dependency>
    <groupId>log4j</groupId>
    <artifactId>log4j</artifactId>
    <version>1.2.17</version>
</dependency>
```

**Method 2: Use Logback as the logging framework**

```xml
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-core</artifactId>
    <version>1.1.2</version>
</dependency> <dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-classic</artifactId>
<version>1.1.2</version> </dependency>
```

**Note**

If an application uses both Log4j and Logback as logging frameworks, client logs cannot be properly printed due to logging conflicts. To properly print the logs of a ApsaraMQ for RocketMQ client, make sure that you add only one dependency on one logging framework for the application. We recommend that you run the **mvn clean**
**dependency:tree | grep log** command to check whether your application uses only
one of the logging frameworks.

**Configure logging for a ApsaraMQ for RocketMQ client**

You can customize the following settings for a ApsaraMQ for RocketMQ client: **the path for**
**storing log files** , **log level**, and **maximum number of historical log files retained** . To
facilitate log transmission and viewing, the **maximum size of a single log file** retains the default value of 64 MB. This value cannot be changed. The following table describes these parameters that you can configure.

| Parameter | Description |
|---|---|
| The path to store log files | Make sure that the application has the write permissions for this path. Otherwise, logs cannot be printed. |

| The maximum number of historical log files that are retained | You can set this parameter to a value between 1 and 100. If you enter a value that is not within this range or a value that is in an invalid format, the system retains 10 historical log files by default. |
|---|---|
| The log level | You can set this parameter to one of the following values: ERROR, WARN, INFO, and DEBUG. If this parameter is set to an invalid value, the system uses the default value INFO. |

**Default configuration**

After you start a ApsaraMQ for RocketMQ client, the client generates log files based on the following default configuration: The path to store log files: `/{user.home}/logs/ons.log` , where `{user.home}` is the root directory of the account that runs the current Java process. The maximum number of historical log files that are retained: 10 Log level: INFO The maximum size of a single log file: 64 MB

**Custom configuration**

**Note**

To customize the logging configuration of a ApsaraMQ for RocketMQ client, update the SDK for Java to V1.2.5 or later. To customize the logging configuration of a ApsaraMQ for RocketMQ client in the SDK for Java, configure the following system parameters: ons.client.logRoot: the path to store log files ons.client.logFileMaxIndex: the maximum number of historical log files that are retained ons.client.logLevel: the log level

**Examples**

Add the following system parameters to the startup script or integrated development environment (IDE) virtual machine (VM) options:

**Linux**

```
-Dons.client.logRoot=/home/admin/logs -Dons.client.logLevel=WARN - Dons.client.logFileMaxIndex=20
```

**Windows**

```
-Dons.client.logRoot=D:\logs -Dons.client.logLevel=WARN - Dons.client.logFileMaxIndex=20
```

/home/admin/ and D:\ are only examples. Replace them with your system directories.

##### Spring integration

###### Overview

This topic describes how to send and subscribe to messages by using ApsaraMQ for RocketMQ in the Spring framework. This topic includes three parts: the integration of a normal message producer and Spring, the integration of a transactional message producer and Spring, and the integration of a message consumer and Spring. The subscriptions of all consumer instances identified by the same group ID must be consistent. For more information, see Subscription consistency. The configuration parameters supported in the Spring framework are the same as those used in TCP client SDK for Java. For more information, see Usage notes.

###### Integrate a producer with Spring

This topic describes how to integrate a producer with Spring.

**Procedure**

1. Define information such as the producer bean in producer.xml.

```xml
<?xml version="1.0" encoding="UTF-8"?>
 <beans xmlns="http://www.springframework.org/schema/beans"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd">
     <bean id="producer" class="com.aliyun.openservices.ons.api.bean.ProducerBean" in
it-method="start" destroy-method="shutdown">
     <!-- The Spring framework supports all the configuration items that SDK for Java
supports. -->
         <property name="properties" > <! -- Configurations of the producer -->
             <props>
                 <prop key="AccessKey">XXX</prop>
                 <prop key="SecretKey">XXX</prop>
                 <!-- The ons-client version is 1.8.4.Final, which must be configured.
You can obtain the TCP endpoint on the Instance Details page in the ApsaraMQ for RocketMQ console.
                 <prop key="NAMESRV_ADDR">XXX</prop>
                 -->
             </props>
         </property>
     </bean>
 </beans>
```

2. Produce messages by using the producer that is integrated with Spring.

```java
 package demo;
 import com.aliyun.openservices.ons.api.Message;
 import com.aliyun.openservices.ons.api.Producer;
 import com.aliyun.openservices.ons.api.SendResult;
 import com.aliyun.openservices.ons.api.exception.ONSClientException;
 import org.springframework.context.ApplicationContext;
 import org.springframework.context.support.ClassPathXmlApplicationContext;
 public class ProduceWithSpring {
     public static void main(String[] args) {
         /**
          * The producer bean is configured in producer.xml. You can call the
ApplicationContext class to obtain the bean or inject the bean to other classes, such as a specific controller.
```

`*/`

```java
         ApplicationContext context = new
ClassPathXmlApplicationContext("producer.xml");
         Producer producer = (Producer) context.getBean("producer");
         // Cyclically send messages.
         for (int i = 0; i < 100; i++) {
             Message msg = new Message( //
                     // The topic of the message.
                     "TopicTestMQ",
                     // The message tag, which is similar to a Gmail tag. The message
tag is used to sort messages and helps the consumer filter messages on the ApsaraMQ f or RocketMQ broker based on specified conditions.
                     "TagA",
                     // The message body in the binary format. ApsaraMQ for RocketMQ d
oes not process the message body.
                     // The producer and consumer must agree on the serialization and
deserialization methods.
                     "Hello MQ".getBytes());
             // The key of the message. The key is the business-specific attribute of
the message and must be globally unique whenever possible.
             // A unique key helps you query and resend a message in the ApsaraMQ for
RocketMQ console if the message fails to be received.
             // Note: Messages can be sent and received even if you do not set this p
arameter.
             msg.setKey("ORDERID_100");
             // Send the message. If no error occurs, the message is sent.
             try {
                 SendResult sendResult = producer.send(msg);
                 assert sendResult != null;
                 System.out.println("send success: " + sendResult.getMessageId());
             }catch (ONSClientException e) {
                 System.out.println("failed to send the message");
```

###### Integrate a transactional message

**producer with Spring**

This topic describes how to integrate a producer that produces transactional messages with Spring.

**Background information**

For more information about transactional messages, see Send and receive transactional messages.

**Procedure**

1. Implement the LocalTransactionChecker class. A producer can have only one
LocalTransactionChecker class.

```java
package demo; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.transaction.LocalTransactionChecker; import com.aliyun.openservices.ons.api.transaction.TransactionStatus; public class DemoLocalTransactionChecker implements LocalTransactionChecker {
    public TransactionStatus check(Message msg) {
        System.out.println("Start to back-check the status of local transaction.");
        return TransactionStatus.CommitTransaction; // Returns different values for T
ransactionStatus based on the status check result of the local transaction.
```

2. Define information such as the producer bean in transactionProducer.xml.

```xml
 <?xml version="1.0" encoding="UTF-8"?>
 <beans xmlns="http://www.springframework.org/schema/beans"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd">
     <bean id="localTransactionChecker" class="demo.DemoLocalTransactionChecker"></be
an>
     <bean id="transactionProducer"
class="com.aliyun.openservices.ons.api.bean.TransactionProducerBean" init-method="sta rt" destroy-method="shutdown">
         <property name="properties" > <! -- Configurations of the transactional
message producer -->
             <props>
                 <prop key="AccessKey">AKDEMO</prop>
                 <prop key="SecretKey">SKDEMO</prop>
                 <prop key="GROUP_ID">GID_DEMO</prop>
                 <!-- The ons-client version is 1.8.4.Final, which must be configured.
You can obtain the TCP endpoint on the Instance Details page in the ApsaraMQ for RocketMQ console.
                 <prop key="NAMESRV_ADDR">XXX</prop>
                 -->
             </props>
         </property>
         <property name="localTransactionChecker" ref="localTransactionChecker">
</property>
     </bean>
 </beans>
```

3. Produce transactional messages by using the producer that is integrated with Spring.

```java
 package demo;
 import com.aliyun.openservices.ons.api.Message;
 import com.aliyun.openservices.ons.api.SendResult;
 import com.aliyun.openservices.ons.api.transaction.LocalTransactionExecuter;
 import com.aliyun.openservices.ons.api.transaction.TransactionProducer;
 import com.aliyun.openservices.ons.api.transaction.TransactionStatus;
 import org.springframework.context.ApplicationContext;
 import org.springframework.context.support.ClassPathXmlApplicationContext;
 public class ProduceTransMsgWithSpring {
     public static void main(String[] args) {
         /**
          * The bean of the transactional message producer is configured in
transactionProducer.xml. You can call the ApplicationContext class to obtain the bean or inject the bean to other classes, such as a specific controller.
          * Send transactional messages.
```

`*/`

```java
         ApplicationContext context = new
ClassPathXmlApplicationContext("transactionProducer.xml");
         TransactionProducer transactionProducer = (TransactionProducer)
context.getBean("transactionProducer");
         Message msg = new Message("XXX", "TagA", "Hello MQ
transaction===".getBytes());
         SendResult sendResult = transactionProducer.send(msg, new
LocalTransactionExecuter() {
             @Override
             public TransactionStatus execute(Message msg, Object arg) {
                 System.out.println("A local transaction is executed.");
                 return TransactionStatus.CommitTransaction; // Returns different valu
es for TransactionStatus based on the execution result of the local transaction.
         }, null);
```

###### Integrate a consumer with Spring

This topic describes how to integrate a consumer with Spring.

**Procedure**

1. Create a message listener. The following sample code provides an example:

```java
package demo; import com.aliyun.openservices.ons.api.Action; import com.aliyun.openservices.ons.api.ConsumeContext; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.MessageListener; public class DemoMessageListener implements MessageListener {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println("Receive: " + message.getMsgID());
        try {
            //do something..
            return Action.CommitMessage;
        }catch (Exception e) {
            // The message failed to be consumed.
            return Action.ReconsumeLater;
```

2. Define information such as the consumer bean in consumer.xml.

```xml
 <?xml version="1.0" encoding="UTF-8"?>
 <beans xmlns="http://www.springframework.org/schema/beans"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd">
     <bean id="msgListener" class="demo.DemoMessageListener"></bean> <!--
Configurations of the message listener-->
 <!-- When multiple consumers identified by the same group ID subscribe to the same t
opic, you can create multiple consumer beans. -->
     <bean id="consumer" class="com.aliyun.openservices.ons.api.bean.ConsumerBean" in
it-method="start" destroy-method="shutdown">
         <property name="properties" > <!-- Configurations of the consumer -->
             <props>
                 <prop key="GROUP_ID">GID_DEMO</prop> <!-- Replace the value with the
group ID that you created in the console. -->
                 <prop key="AccessKey">AKDEMO</prop>
                 <prop key="SecretKey">SKDEMO</prop>
                 <!-- The ons-client version is 1.8.4.Final, which must be configured.
```

```xml
You can obtain the TCP endpoint on the Instance Details page in the ApsaraMQ for RocketMQ console.
                 <prop key="NAMESRV_ADDR">XXX</prop>
                 -->
                 <!-- Set the number of consumer threads to 50.
                 <prop key="ConsumeThreadNums">50</prop>
                 -->
             </props>
         </property>
         <property name="subscriptionTable">
             <map>
                 <entry value-ref="msgListener">
                     <key>
                         <bean
class="com.aliyun.openservices.ons.api.bean.Subscription">
                             <property name="topic" value="TopicTestMQ"/>
                             <property name="expression" value="*"/><!--The expression
is the tag. You can set the value to a specific tag or *. For example, a specific tag can be taga||tagb||tagc. * indicates that all tags are subscribed to. Wildcards are not supported. -->
                         </bean>
                     </key>
                 </entry>
                 <!-- Add entry nodes to subscribe to more tags. -->
                 <entry value-ref="msgListener">
                     <key>
                         <bean
class="com.aliyun.openservices.ons.api.bean.Subscription">
                             <property name="topic" value="TopicTestMQ-Other"/> <!--Su
bscribe to another topic. -->
                             <property name="expression" value="taga||tagb"/> <!-- Sub
scribetomltipletags
```

`>`

```
scribe to multiple tags. -->
                         </bean>
                     </key>
                 </entry>
             </map>
         </property>
     </bean>
 </beans>
```

3. Run the consumer that is integrated with Spring.

```java
package demo; import org.springframework.context.ApplicationContext; import org.springframework.context.support.ClassPathXmlApplicationContext; public class ConsumeWithSpring {
    public static void main(String[] args) {
        /**
         * The consumer bean is configured in consumer.xml. You can call the
ApplicationContext class to obtain the bean or inject the bean to other classes, such as a specific controller.
```

`*/`

```java
        ApplicationContext context = new
ClassPathXmlApplicationContext("consumer.xml");
        System.out.println("Consumer Started");
```

##### Three modes for sending messages

###### Overview

In ApsaraMQ for RocketMQ, messages can be sent in reliable synchronous mode, reliable asynchronous mode, and one-way mode. This topic describes the principles, scenarios, and differences of these modes, and provides sample code for your reference.

**Note**

Ordered messages can be sent only in reliable synchronous mode.

###### Reliable synchronous transmission

This topic describes the principle and scenarios of the reliable synchronous transmission mode.

**How it works**

Synchronous transmission means that the message producer sends the next message only after it receives a response to the previous message from the broker. Figure 1. Synchronous transmission

**Scenarios**

This mode is applicable to various scenarios, such as important notification emails, short message service (SMS) notifications for registration results, and SMS marketing systems.

**Sample code**

```java
import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.Producer; import com.aliyun.openservices.ons.api.SendResult; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import java.util.Properties; public class ProducerTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
le for identity authentication.
        properties.put(PropertyKeyConst.AccessKey,"XXX");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The timeout interval for sending a message, in milliseconds.
        properties.setProperty(PropertyKeyConst.SendMsgTimeoutMillis, "3000");
        // The TCP endpoint. To obtain the endpoint, log on to the ApsaraMQ for RocketM
Q console. In the left-side navigation pane, click Instance Details. On the Instance De
```

```java
tails page, select your instance. On the Instance Information tab, view the endpoint in the Obtain Endpoint Information section.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        Producer producer = ONSFactory.createProducer(properties);
        // Before you use the producer to send a message, call the start() method once
to start the producer.
        producer.start();
        // Cyclically send messages.
        for (int i = 0; i < 10; i++){
            Message msg = new Message( //
                // The topic of the message.
                "TopicTestMQ",
                // The message tag, which is similar to a Gmail tag. The message tag is
used to sort messages and helps the consumer filter messages on the ApsaraMQ for RocketMQ broker based on specified conditions.
                "TagA",
                // The message body in the binary format. ApsaraMQ for RocketMQ does
not process the message body.
                // The producer and consumer must agree on the serialization and
deserialization methods.
                "Hello MQ".getBytes());
            // The key of the message. The key is the business-specific attribute of th
e message and must be globally unique whenever possible.
            // A unique key helps you query and resend a message in the ApsaraMQ for Ro
cketMQ console if the message fails to be received.
            // Note: Messages can be sent and received even if you do not specify the m
essage key.
            msg.setKey("ORDERID_" + i);
            try {
                SendResult sendResult = producer.send(msg);
                // Send the message in synchronous mode. If no error occurs, the message
is sent.
                if (sendResult != null) {
                    System.out.println(new Date() + " Send mq message success. Topic is:
" + msg.getTopic() + " msgId is: " + sendResult.getMessageId());
            catch (Exception e) {
                // Specify the logic to resend or persist the message if the message fai
ls to be sent.
                System.out.println(new Date() + " Send mq message failed. Topic is:" + m
sg.getTopic());
                e.printStackTrace();
        // Before you exit the application, shut down the producer object.
        // Note: You can choose not to shut down the producer object.
        producer.shutdown();
```

###### Reliable asynchronous transmission

This topic describes the principle and scenarios of the reliable asynchronous transmission mode.

**How it works**

In reliable asynchronous transmission mode, a producer sends the next message without waiting for a response to the previous message from the ApsaraMQ for RocketMQ broker. This mode uses the SendCallback method to fire a callback after a message is sent. An application sends the next message before it receives a response to the previous message from the ApsaraMQ for RocketMQ broker. After the SendCallback method is called, the application receives the response to the previous message from the ApsaraMQ for RocketMQ broker and processes the response. Figure 1. Asynchronous transmission

**Scenarios**

This mode is used for time-consuming processes in business scenarios that are sensitive to the response time. For example, after you upload a video, a callback is fired to enable transcoding. After the video is transcoded, a callback is fired to push transcoding results.

**Sample code**

```java
    import com.aliyun.openservices.ons.api.Message;
    import com.aliyun.openservices.ons.api.OnExceptionContext;
    import com.aliyun.openservices.ons.api.Producer;
    import com.aliyun.openservices.ons.api.SendCallback;
    import com.aliyun.openservices.ons.api.SendResult;
    import com.aliyun.openservices.ons.api.ONSFactory;
    import com.aliyun.openservices.ons.api.PropertyKeyConst;
    import java.util.Properties;
```

```
    public static void main(String[] args) {
        Properties properties = new Properties();
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
le for identity authentication.
        properties.put(PropertyKeyConst.AccessKey, "XXX");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The timeout interval for sending a message, in milliseconds.
        properties.setProperty(PropertyKeyConst.SendMsgTimeoutMillis, "3000");
        // The TCP endpoint. To obtain the endpoint, log on to the ApsaraMQ for RocketM
Q console. In the left-side navigation pane, click Instance Details. On the Instance De tails page, select your instance. On the Instance Information tab, view the endpoint in the Obtain Endpoint Information section.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        Producer producer = ONSFactory.createProducer(properties);
        // Before you use the producer to send a message, call the start() method once
to start the producer.
        producer.start();
        Message msg = new Message(
                // The topic of the message.
                "TopicTestMQ",
                // The message tag, which is similar to a Gmail tag. The message tag is
used to sort messages and helps the consumer filter messages on the ApsaraMQ for RocketMQ broker based on specified conditions.
                "TagA",
                // The message body in the binary format. ApsaraMQ for RocketMQ does
not process the message body. The producer and consumer must agree on the serialization and deserialization methods.
                "Hello MQ".getBytes());
        // The key of the message. The key is the business-specific attribute of the me
ssage and must be globally unique whenever possible. // A unique key helps you query a nd resend a message in the ApsaraMQ for RocketMQ console if the message fails to be rec eived.
        // Note: Messages can be sent and received even if you do not set this paramete
```

`r.`

```java
        msg.setKey("ORDERID_100");
        // Send the message in asynchronous mode. The result is returned to the
producer after the producer calls the callback function.
        producer.sendAsync(msg, new SendCallback() {
            @Override
            public void onSuccess(final SendResult sendResult) {
                // The message is sent to the consumer.
                System.out.println("send message success. topic=" +
sendResult.getTopic() + ", msgId=" + sendResult.getMessageId());
            @Override
            public void onException(OnExceptionContext context) {
                // Specify the logic to resend or persist the message if the message fai
ls to be sent.
                System.out.println("send message failed. topic=" + context.getTopic() +
", msgId=" + context.getMessageId());
```

`})`

```java
        });
        // The message ID can be obtained before the callback function returns the resu
lt.
        System.out.println("send message async. topic=" + msg.getTopic() + ", msgId=" +
msg.getMsgID());
        // Before you exit the application, shut down the producer object.  Note: You c
an choose not to shut down the producer object.
        producer.shutdown();
```

###### One-way transmission

This topic describes the principle and scenarios of the one-way transmission mode, and provides sample code.

**How it works**

In one-way transmission mode, a producer only sends messages and does not wait for a response from the ApsaraMQ for RocketMQ broker. In addition, no callback function is triggered. In this mode, a message can be sent within microseconds. Figure 1. One-way transmission

**Scenarios**

This mode is applicable to scenarios where message transmission takes a short time and has no demanding reliability requirements. For example, this mode can be used for log collection. The following table summarizes the features and major differences among the three modes.

| > Document Version: 202 | 60828 |   | 14 |
|---|---|---|---|

| Transmission mode | Transactions per second (TPS) | Response | Reliability |
|---|---|---|---|
| Synchronous transmission | High | Supported | No message loss |
| Asynchronous transmission | High | Supported | No message loss |
| One-way transmission | Highest | None | Possible message loss |

**Sample code**

```java
    import com.aliyun.openservices.ons.api.Message;
    import com.aliyun.openservices.ons.api.Producer;
    import com.aliyun.openservices.ons.api.ONSFactory;
    import com.aliyun.openservices.ons.api.PropertyKeyConst;
    import java.util.Properties;
    public static void main(String[] args) {
        Properties properties = new Properties();
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
le for identity authentication.
        properties.put(PropertyKeyConst.AccessKey, "XXX");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The timeout interval for sending a message, in milliseconds.
        properties.setProperty(PropertyKeyConst.SendMsgTimeoutMillis, "3000");
        // The TCP endpoint. To obtain the endpoint, log on to the ApsaraMQ for RocketM
Q console. In the left-side navigation pane, click Instance Details. On the Instance De tails page, select your instance. On the Instance Information tab, view the endpoint in the Obtain Endpoint Information section.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        Producer producer = ONSFactory.createProducer(properties);
        // Before you use the producer to send a message, call the start() method once
to start the producer.
        producer.start();
        // Cyclically send messages.
        for (int i = 0; i < 10; i++){
            Message msg = new Message(
                    // The topic of the message.
                    "TopicTestMQ",
                    // Message Tag,
                    // The message tag, which is similar to a Gmail tag. The message tag
is used to sort messages and helps the consumer filter messages on the ApsaraMQ for RocketMQ broker based on specified conditions.
                    "TagA",
                    // Message Body
                    // The message body in the binary format. ApsaraMQ for RocketMQ does
not process the message body. The producer and consumer must agree on the serialization
```

```
and deserialization methods.
                    "Hello MQ".getBytes());
            // The key of the message. The key is the business-specific attribute of th
e message and must be globally unique whenever possible.
            // A unique key helps you query and resend a message in the ApsaraMQ for Ro
cketMQ console if the message fails to be received.
            // Note: Messages can be sent and received even if you do not specify the m
essage key.
            msg.setKey("ORDERID_" + i);
            // In one-way transmission mode, the producer does not wait for the
response from the ApsaraMQ for RocketMQ broker. Therefore, data loss occurs if messages that fail to be delivered are not redelivered. If data loss is not acceptable, we recom mend that you use the reliable synchronous or asynchronous transmission mode.
            producer.sendOneway(msg);
        // Before you exit the application, shut down the producer object.
        // Note: You can choose not to shut down the producer object.
        producer.shutdown();
```

##### Send messages by using multiple threads

This topic describes how to send messages by using multiple threads and provides sample code. The consumer and producer objects of ApsaraMQ for RocketMQ are thread-secure and can be shared among threads. You can deploy multiple producer and consumer instances on one or more cloud servers. A producer or consumer instance can also run multiple threads to send or receive messages. This improves the transactions per second (TPS) for sending or receiving messages. Do not create a producer instance or consumer instance for every thread. The following sample code provides an example on how to share a producer among threads:

```java
import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.Producer; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.SendResult; import java.util.Properties; public class SharedProducer {
    public static void main(String[] args) {
        // Initialize the configuration of the producer instance.
        Properties properties = new Properties();
        // The group ID that you created in the ApsaraMQ for RocketMQ console.
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
le for identity authentication.
        properties.put(PropertyKeyConst.AccessKey,"XXX");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The timeout interval for sending a message, in milliseconds.
        properties.setProperty(PropertyKeyConst.SendMsgTimeoutMillis, "3000");
```

```
        // The TCP endpoint. To obtain the endpoint, log on to the ApsaraMQ for RocketM
Q console. In the left-side navigation pane, click Instance Details. On the Instance De tails page, select your instance. On the Instance Information tab, view the endpoint in the Obtain Endpoint Information section.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        final Producer producer = ONSFactory.createProducer(properties);
        // Before you use the producer to send a message, call the start() method once
to start the producer.
        producer.start();
        // The created producer and consumer objects are thread-secure and can be share
d among threads. Do not create a producer instance or consumer instance for every threa
```

`d.`

```java
        // Two threads share the producer object and concurrently send messages to Apsa
raMQ for RocketMQ.
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Message msg = new Message( //
                    // The topic of the message.
                    "TopicTestMQ",
                    // The message tag, which is similar to a Gmail tag. The message tag
is used to sort messages and helps the consumer filter messages on the ApsaraMQ for RocketMQ broker based on specified conditions.
                    "TagA",
                    // The message body in the binary format. ApsaraMQ for RocketMQ does
not process the message body.
                    // The producer and consumer must agree on the serialization and des
erialization methods.
                    "Hello MQ".getBytes());
                    SendResult sendResult = producer.send(msg);
                    // Send the message in synchronous mode. If no error occurs, the mes
sage is sent.
                    if (sendResult != null) {
                        System.out.println(new Date() + " Send mq message success. Topic
is:" + MqConfig.TOPIC + " msgId is: " + sendResult.getMessageId());
                } catch (Exception e) {
                    // Specify the logic to resend or persist the message if the message
fails to be sent.
                    System.out.println(new Date() + " Send mq message failed. Topic is:"
+ MqConfig.TOPIC);
                    e.printStackTrace();
        });
        thread.start();
        Thread anotherThread = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Message msg = new Message("TopicTestMQ", "TagA", "Hello MQ".getBytes
()); SendResltsendReslt prodcersend(msg)
```

```java
                    SendResult sendResult = producer.send(msg);
                    // Send the message in synchronous mode. If no error occurs, the mes
sage is sent.
                    if (sendResult != null) {
                        System.out.println(new Date() + " Send mq message success. Topic
is:" + MqConfig.TOPIC + " msgId is: " + sendResult.getMessageId());
                } catch (Exception e) {
                    // Specify the logic to resend or persist the message if the message
fails to be sent.
                    System.out.println(new Date() + " Send mq message failed. Topic is:"
+ MqConfig.TOPIC);
                    e.printStackTrace();
        });
        anotherThread.start();
        // If the producer instance is no longer used, shut it down to release
resources.
        // producer.shutdown();
```

##### Send and receive ordered messages

This topic describes how to use the SDK for Java to send and receive ordered messages. This topic also provides sample code. Ordered messages, also known as first-in, first-out (FIFO) messages, are a type of message provided by ApsaraMQ for RocketMQ. Ordered messages are published and consumed in a strict order. This topic provides sample code for using the TCP client SDK for Java to send and receive ordered messages. For more information, see Ordered messages. Use SDK for Java 1.2.7 or later to send and receive ordered messages.

**Sample code for sending ordered messages**

```java
package com.aliyun.openservices.ons.example.order; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.SendResult; import com.aliyun.openservices.ons.api.order.OrderProducer; import java.util.Properties; public class ProducerClient {
    public static void main(String[] args) {
        Properties properties = new Properties();
        // The ID of the consumer group that you created in the ApsaraMQ for RocketMQ c
onsole.
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
        // The AccessKey ID that you created in the Alibaba Cloud Management Console fo
r identity verification.
        properties.put(PropertyKeyConst.AccessKey, "XXX");
        // The AccessKey secret that you created in the Alibaba Cloud Management
Console for identity verification.
```

```
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The TCP endpoint of your instance. You can view the TCP endpoint on the Netw
ork Management tab of the Instances page in the ApsaraMQ for RocketMQ console.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        OrderProducer producer = ONSFactory.createOrderProducer(properties);
        // Before you send the message, call the start() method only once to start the
producer.
        producer.start();
        for (int i = 0; i < 10; i++) {
            String orderId = "biz_" + i % 10;
            Message msg = new Message(//
                    // The topic to which the message belongs.
                    "Order_global_topic",
                    // The message tag, which is similar to a Gmail tag. The message tag
is used to sort messages and helps the consumer filter messages on the ApsaraMQ for RocketMQ broker based on specific conditions.
                    "TagA",
                    // The message body in the binary format. ApsaraMQ for RocketMQ does
not process the message body. The producer and consumer must agree on the serialization and deserialization methods.
                    "send order global msg".getBytes()
```

);

```java
            // The message key. The key is the business-specific attribute of the
message and must be globally unique whenever possible.
            // A key can be used to query and resend a message in the ApsaraMQ for Rock
etMQ console if the message fails to be received.
            // Note: A message can be sent and received even if you do not specify the
message key.
            msg.setKey(orderId);
            // The key field that is used in ordered messages to identify different
partitions. The sharding key is different from the key of a normal message.
            String shardingKey = String.valueOf(orderId);
            try {
                SendResult sendResult = producer.send(msg, shardingKey);
                // Send the message. If no exception is thrown, the message is sent.
                if (sendResult != null) {
                    System.out.println(new Date() + " Send mq message success. Topic is:
" + msg.getTopic() + " msgId is: " + sendResult.getMessageId());
            catch (Exception e) {
                // The logic to resend or persist the message if the message fails to be
sent and needs to be resent.
                System.out.println(new Date() + " Send mq message failed. Topic is:" + m
sg.getTopic());
                e.printStackTrace();
        // Before you exit the application, shut down the producer object.
        // Note: This operation is optional.
        producer.shutdown();
```

**Sample code for receiving ordered messages**

```java
package com.aliyun.openservices.ons.example.order; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.order.ConsumeOrderContext; import com.aliyun.openservices.ons.api.order.MessageOrderListener; import com.aliyun.openservices.ons.api.order.OrderAction; import com.aliyun.openservices.ons.api.order.OrderConsumer; import java.util.Properties; public class ConsumerClient {
    public static void main(String[] args) {
        Properties properties = new Properties();
        // The ID of the consumer group that you created in the ApsaraMQ for RocketMQ c
onsole.
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
        // The AccessKey ID that you created in the Alibaba Cloud Management Console fo
r identity verification.
        properties.put(PropertyKeyConst.AccessKey, "XXX");
        // The AccessKey secret that you created in the Alibaba Cloud Management
Console for identity verification.
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The TCP endpoint of your instance. You can view the TCP endpoint on the Netw
ork Management tab of the Instances page in the ApsaraMQ for RocketMQ console.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
          // Set the delay time in milliseconds before the retry upon an ordered
message consumption failure. Value range: 10 to 1800.
        properties.put(PropertyKeyConst.SuspendTimeMillis, "100");
        // The maximum number of delivery retries when the message fails to be
consumed.
        properties.put(PropertyKeyConst.MaxReconsumeTimes, "20");
        // Before you send the message, call the start() method only once to start the
producer.
        OrderConsumer consumer = ONSFactory.createOrderedConsumer(properties);
        consumer.subscribe(
                // The topic to which the message belongs.
                "Jodie_Order_Topic",
                // Subscribe to messages with specific tags in the specified topic.
                // 1. An asterisk (*) specifies that the consumer subscribes to all
messages.
                // 2. TagA || TagB || TagC specifies that the consumer subscribes to mes
sages that contain Tag A, Tag B, or Tag C.
                "*",
                new MessageOrderListener() {
                    /**
                     * 1 If the message fails to be consumed or an exception occurs duri
ng message processing, OrderAction.Suspend is returned.
                     * 2. If the message is processed, OrderAction.Success is returned.
```

`*/`

```java
                    @Override
                    public OrderAction consume(Message message, ConsumeOrderContext cont
```

```java
ext) {
                        System.out.println(message);
                        return OrderAction.Success;
                });
        consumer.start();
```

##### Send and receive transactional messages

This topic describes the interaction process and the status check mechanism of transactional messages. This topic also shows you how to send and subscribe to transactional messages, and provides sample code.

**Interaction process**

The following figure shows the interaction process of transactional messages in ApsaraMQ for RocketMQ. Figure 1. Interaction process of transactional messages

**Send transactional messages**

Perform the following steps to send a transactional message:
1. Send a half message and execute a local transaction. Sample code:

```java
package com.alibaba.webx.TryHsf.app1; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.SendResult; import com.aliyun.openservices.ons.api.transaction.LocalTransactionExecuter; import com.aliyun.openservices.ons.api.transaction.TransactionProducer; import com.aliyun.openservices.ons.api.transaction.TransactionStatus; import java.util.Properties; import java.util.concurrent.TimeUnit; public class TransactionProducerClient {
 private final static Logger log = ClientLogger.getLog(); // Configure logging to fac
ilitate troubleshooting.
 public static void main(String[] args) throws InterruptedException {
     final BusinessService businessService = new BusinessService(); // Your on-premis
es business.
     Properties properties = new Properties();
     // The group ID that you created in the ApsaraMQ for RocketMQ console. Note: Tra
```

`g` `p` `y` `p`

```java
nsactional messages cannot share group IDs with other types of messages.
     properties.put(PropertyKeyConst.GROUP_ID, "XXX");
     // The AccessKey ID that you created in the Apsara Uni-manager Management Consol
e for identity authentication.
     properties.put(PropertyKeyConst.AccessKey, "XXX");
     // The AccessKey secret that you created in the Apsara Uni-manager Management Co
nsole for identity authentication.
     properties.put(PropertyKeyConst.SecretKey, "XXX");
     // The TCP endpoint. To obtain the endpoint, log on to the ApsaraMQ for RocketMQ
console. In the left-side navigation pane, click Instances. Click the instance that y ou want to manage to go to the Instance details page. On the Basic information tab, v iew the endpoint of the instance.
     properties.put(PropertyKeyConst.NAMESRV_ADDR,
       "XXX");
     TransactionProducer producer = ONSFactory.createTransactionProducer(properties,
             new LocalTransactionCheckerImpl());
     producer.start();
     Message msg = new Message("Topic", "TagA", "Hello MQ
transaction===".getBytes());
     try {
             SendResult sendResult = producer.send(msg, new
LocalTransactionExecuter() {
                 @Override
                 public TransactionStatus execute(Message msg, Object arg) {
                     // The ID of the message. Two messages may have the same message
body but cannot have the same ID. The current message ID cannot be queried in the con sole.
                     String msgId = msg.getMsgID();
                     // Calculate the message body by using CRC32 or other algorithms,
such as MD5.
                     long crc32Id = HashUtil.crc32Code(msg.getBody());
                     // The message ID and CRC32 ID are used to prevent duplicate mess
ages.
                     // You do not need to specify the message ID or CRC32 ID if your
business itself achieves idempotence. Otherwise, specify the message ID or CRC32 ID t o ensure idempotence.
                     // To prevent duplicate messages, calculate the message body by u
sing the CRC32 or MD5 algorithm.
                     Object businessServiceArgs = new Object();
                     TransactionStatus transactionStatus = TransactionStatus.Unknow;
                     try {
                         boolean isCommit =
                             businessService.execbusinessService(businessServiceArgs);
                         if (isCommit) {
                             // Commit the message if the local transaction succeeds.
                             transactionStatus = TransactionStatus.CommitTransaction;
                         } else {
                             // Roll back the message if the local transaction fails.
                             transactionStatus =
TransactionStatus.RollbackTransaction;
                     } catch (Exception e) {
                         log.error("Message Id:{}", msgId, e);
```

```java
                     System.out.println(msg.getMsgID());
                     log.warn("Message Id:{}transactionStatus:{}", msgId, transactionS
tatus.name());
                     return transactionStatus;
             }, null);
         catch (Exception e) {
             // Specify the logic to resend or persist the message if the message
fails to be sent.
             System.out.println(new Date() + " Send mq message failed. Topic is:" +
msg.getTopic());
             e.printStackTrace();
     // Use the demo example to prevent the process from exiting. This is not require
d in actual use.
     TimeUnit.MILLISECONDS.sleep(Integer.MAX_VALUE);
```

2. Commit the status of the transactional message.
After the local transaction is executed, the ApsaraMQ for RocketMQ broker must be notified of the transaction status of the current message, no matter whether the execution succeeds or fails. You can notify the ApsaraMQ for RocketMQ broker by using one of the following methods: Commit the status after the local transaction is executed. Wait until the ApsaraMQ for RocketMQ broker sends a request to check the transaction status of the message. A transaction can be in one of the following states:
**TransactionStatus.CommitTransaction**: The transaction is committed. The message
can be consumed by consumers.
**TransactionStatus.RollbackTransaction**: The transaction is rolled back. The message
is discarded and cannot be consumed.
**TransactionStatus.Unknow**: The status of the transaction is unknown. The ApsaraMQ
for RocketMQ broker is expected to send a request again to the producer to query the status of the local transaction that corresponds to the message.

```java
public class LocalTransactionCheckerImpl implements LocalTransactionChecker {
   private final static Logger log = ClientLogger.getLog();
   final  BusinessService businessService = new BusinessService();
   @Override
   public TransactionStatus check(Message msg) {
       // The ID of the message. Two messages may have the same message body but cann
ot have the same ID. The current message is a half message. Therefore, its message ID cannot be queried in the console.
       String msgId = msg.getMsgID();
       // Calculate the message body by using CRC32 or other algorithms, such as MD5.
       long crc32Id = HashUtil.crc32Code(msg.getBody());
       // The message ID and CRC32 ID are used to prevent duplicate messages.
       // You do not need to specify the message ID or CRC32 ID if your business itse
lf achieves idempotence. Otherwise, specify the message ID or CRC32 ID to ensure idem potence.
       // To prevent duplicate messages, calculate the message body by using the CRC3
2 or MD5 algorithm.
       // The parameter object of your business. Specify the object based on your bus
iness.
       Object businessServiceArgs = new Object();
       TransactionStatus transactionStatus = TransactionStatus.Unknow;
       try {
           boolean isCommit =
businessService.checkbusinessService(businessServiceArgs);
           if (isCommit) {
               // Commit the message if the local transaction succeeds.
               transactionStatus = TransactionStatus.CommitTransaction;
           } else {
               // Roll back the message if the local transaction fails.
               transactionStatus = TransactionStatus.RollbackTransaction;
       } catch (Exception e) {
           log.error("Message Id:{}", msgId, e);
       log.warn("Message Id:{}transactionStatus:{}", msgId,
transactionStatus.name());
       return transactionStatus;
```

**Utility class**

```java
import java.util.zip.CRC32; public class HashUtil {
    public static long crc32Code(byte[] bytes) {
        CRC32 crc32 = new CRC32();
        crc32.update(bytes);
        return crc32.getValue();
```

**Mechanism of transaction status check**

Why must the mechanism of transaction status check be implemented when transactional messages are sent? If the half message is sent in Step 1 but **TransactionStatus.Unknow** is returned for the local transaction, or no status is committed for the local transaction because the application exits, the status of the half message is unknown to the ApsaraMQ for RocketMQ broker. Therefore, the ApsaraMQ for RocketMQ broker periodically requests the producer to check and report the status of the half message. What does the business logic do when the check method is called back? The check method for transactional messages in ApsaraMQ for RocketMQ must contain the logic of transaction consistency check. After a transactional message is sent, ApsaraMQ for RocketMQ must call the **LocalTransactionChecker** operation to respond to the request of the ApsaraMQ for RocketMQ broker for the status of the local transaction. Therefore, the check method for transactional messages must contain the following check items: i. Check whether the status of the local transaction that corresponds to the half message is committed or rollback. ii. Commit the status of the local transaction that corresponds to the half message to the ApsaraMQ for RocketMQ broker.

**Subscribe to transactional messages**

The method for subscribing to transactional messages is the same as that for subscribing to normal messages. For more information, see Subscribe to messages.

##### Send and subscribe to delayed messages

This topic describes how to send and subscribe to delayed messages and provides sample code. Delayed messages are delivered to a consumer after a specified period of time from when they are sent to the ApsaraMQ for RocketMQ broker. For example, the specified period of time can be 3 seconds. Delayed messages are used in scenarios where a time window between message production and consumption is required or tasks need to be triggered after a delay. Delayed messages are used in a similar way to delay queues. For more information about the concepts and usage notes of delayed messages, see Scheduled messages and delayed messages.

**Send delayed messages**

The following sample code provides an example on how to send delayed messages:

```java
import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.Producer; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.SendResult; import java.util.Properties; public class ProducerDelayTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
le for identity authentication.
        properties.put(PropertyKeyConst.AccessKey, "XXX");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The TCP endpoint. To obtain the endpoint, log on to the ApsaraMQ for RocketM
```

`//` `e`

```
edpo
```

`t.`

```
oobta teedpo
```

`t,`

```
ogo tote psaaQ
```

`o`

```java
ocet Q console. In the left-side navigation pane, click Instance Details. On the Instance De tails page, select your instance. On the Instance Information tab, view the endpoint in the Obtain Endpoint Information section.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        Producer producer = ONSFactory.createProducer(properties);
        // Before you use the producer to send a message, call the start() method once
to start the producer.
        producer.start();
        Message msg = new Message( //
                // The topic that you created in the ApsaraMQ for RocketMQ console.
                "Topic",
                // The message tag, which is similar to a Gmail tag. The message tag is
used to sort messages and helps the consumer filter messages on the ApsaraMQ for RocketMQ broker based on specified conditions.
                "tag",
                // The message body in the binary format. ApsaraMQ for RocketMQ does
not process the message body. The producer and consumer must agree on the serialization and deserialization methods.
                "Hello MQ".getBytes());
        // The key of the message. The key is the business-specific attribute of the me
ssage and must be globally unique whenever possible.
        // A unique key helps you query and resend a message in the ApsaraMQ for Rocket
MQ console if the message fails to be received.
        // Note: Messages can be sent and received even if you do not specify the messa
ge key.
        msg.setKey("ORDERID_100");
        try {
            // The specified period of time, in milliseconds. After the specified
period of time elapses, the ApsaraMQ for RocketMQ broker delivers the message to the co nsumer. For example, you can set this parameter to 3 and the ApsaraMQ for RocketMQ broker delivers the message to the consumer after 3 seconds. The value must be later th an the current time.
            long delayTime = System.currentTimeMillis() + 3000;
            // The time when the ApsaraMQ for RocketMQ broker starts to deliver the mes
sage.
            msg.setStartDeliverTime(delayTime);
            SendResult sendResult = producer.send(msg);
            // Send the message in synchronous mode. If no error occurs, the message is
sent.
            if (sendResult != null) {
            System.out.println(new Date() + " Send mq message success. Topic is:" +
msg.getTopic() + " msgId is: " + sendResult.getMessageId());
            } catch (Exception e) {
            // Specify the logic to resend or persist the message if the message fails
to be sent.
            System.out.println(new Date() + " Send mq message failed. Topic is:" +
msg.getTopic());
            e.printStackTrace();
        // Before you exit the application, shut down the producer object.<br>
        // Note: You can choose not to shut down the producer object.
        producer.shutdown();
```

**Subscribe to delayed messages**

The method for subscribing to delayed messages is the same as that for subscribing to normal messages. For more information, see Subscribe to messages.

##### Send and subscribe to scheduled

**messages**

This topic describes the scenarios for sending and subscribing to scheduled messages and provides sample code. Scheduled messages are consumed after a specified timestamp. Such messages are used in scenarios where a time window between message production and consumption is required or tasks need to be triggered at a scheduled time. For more information about the concepts and usage notes of scheduled messages, see Scheduled messages and delayed messages.

**Send scheduled messages**

The following sample code provides an example on how to send scheduled messages:

```java
import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.Producer; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.SendResult; import java.text.ParseException; import java.text.SimpleDateFormat; import java.util.Properties; public class ProducerDelayTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
le for identity authentication.
        properties.put(PropertyKeyConst.AccessKey, "XXX");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The TCP endpoint. To obtain the endpoint, log on to the ApsaraMQ for RocketM
Q console. In the left-side navigation pane, click Instance Details. On the Instance De tails page, select your instance. On the Instance Information tab, view the endpoint in the Obtain Endpoint Information section.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        Producer producer = ONSFactory.createProducer(properties);
        // Before you use the producer to send a message, call the start() method once
to start the producer.
        producer.start();
        Message msg = new Message( //
                // The topic of the message.
                "Topic",
```

```java
                // The message tag, which is similar to a Gmail tag. The message tag is
used to sort messages and helps the consumer filter messages on the ApsaraMQ for RocketMQ broker based on specified conditions.
                "tag",
                // The message body in the binary format. ApsaraMQ for RocketMQ does
not process the message body. The producer and consumer must agree on the serialization and deserialization methods.
                "Hello MQ".getBytes());
        // The key of the message. The key is the business-specific attribute of the me
ssage and must be globally unique whenever possible.
        // A unique key helps you query and resend a message in the ApsaraMQ for Rocket
MQ console if the message fails to be received.
        // Note: Messages can be sent and received even if you do not specify the messa
ge key.
        msg.setKey("ORDERID_100");
        try {
            // The time when the ApsaraMQ for RocketMQ broker delivers the message to t
he consumer, in milliseconds. For example, you can set this parameter to 2016-03-07 16: 21:00 and the broker delivers the message at 16:21:00 on March 7, 2016. The value must be later than the current time. If the scheduled time is earlier than the current time, the message is immediately delivered to the consumer.
            long timeStamp = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").parse("2016-
03-07 16:21:00").getTime();
            msg.setStartDeliverTime(timeStamp);
            // Send the message. If no error occurs, the message is sent.
            SendResult sendResult = producer.send(msg);
            System.out.println("Message Id:" + sendResult.getMessageId());
        catch (Exception e) {
            // Specify the logic to resend or persist the message if the message fails
to be sent.
            System.out.println(new Date() + " Send mq message failed. Topic is:" +
msg.getTopic());
            e.printStackTrace();
        // Before you exit the application, shut down the producer object.
        // Note: You can choose not to shut down the producer object.
        producer.shutdown();
```

**Subscribe to scheduled messages**

The method for subscribing to scheduled messages is the same as that for subscribing to normal messages. For more information, see Subscribe to messages.

##### Subscribe to messages

This topic describes message subscription modes and provides sample code.

**Note**

The subscriptions of all consumer instances identified by the same group ID must be consistent. For more information, see Subscription consistency.

**Subscription modes**

ApsaraMQ for RocketMQ supports the following message subscription modes:
**Clustering subscription:** In this mode, all the consumer instances identified by the same
group ID evenly share messages. Assume that a topic contains nine messages and a group ID identifies three consumer instances. In clustering consumption mode, each instance consumes three messages.

```
 // Configure clustering subscription, which is the default mode.
 properties.put(PropertyKeyConst.MessageModel, PropertyValueConst.CLUSTERING);
```

**Broadcasting subscription:** In this mode, each consumer instance identified by a group
ID consumes each message once. Assume that a topic contains nine messages and a group ID identifies three consumer instances. In broadcasting consumption mode, each instance consumes nine messages.

```
 // Configure broadcasting subscription.
 properties.put(PropertyKeyConst.MessageModel, PropertyValueConst.BROADCASTING);
```

**Sample code**

```java
import com.aliyun.openservices.ons.api.Action; import com.aliyun.openservices.ons.api.ConsumeContext; import com.aliyun.openservices.ons.api.Consumer; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.MessageListener; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import java.util.Properties; public class ConsumerTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
        // The group ID that you created in the ApsaraMQ for RocketMQ console.
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
le for identity authentication.
        properties.put(PropertyKeyConst.AccessKey, "XXX");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The TCP endpoint. To obtain the endpoint, log on to the ApsaraMQ for RocketM
Q console. In the left-side navigation pane, click Instance Details. On the Instance De tails page, select your instance. On the Instance Information tab, view the endpoint in the Obtain Endpoint Information section.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
          // Clustering subscription, which is the default mode.
          // properties.put(PropertyKeyConst.MessageModel,
PropertyValueConst.CLUSTERING);
          // Broadcasting subscription.
          // properties.put(PropertyKeyConst.MessageModel,
PropertyValueConst.BROADCASTING);
        Consumer consumer = ONSFactory.createConsumer(properties);
        consumer.subscribe("TopicTestMQ", "TagA||TagB", new MessageListener() { //
Subscribe to multiple tags.
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
        });
        // Subscribe to another topic.
        consumer.subscribe("TopicTestMQ-Other", "*", new MessageListener() { //
Subscribe to all tags.
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
        });
        consumer.start();
        System.out.println("Consumer Started");
```

**Note**

In broadcasting consumption mode, you cannot query message accumulation information in the ApsaraMQ for RocketMQ console. You can create multiple group IDs to achieve the effect of broadcasting consumption. For more information, see Clustering consumption and broadcasting consumption.

#### SDK for C or C++

##### Prepare the SDK for C or C++ environment

###### Prepare the environment

Before you use the SDK for C or C++ to access ApsaraMQ for RocketMQ, make sure that the following preparations are made.

**Note**

Topics and groups involved in the code are created in the ApsaraMQ for RocketMQ console. You can specify custom message tags in your application. For information about how to create a message tag, see Create resources. Applications that use ApsaraMQ for RocketMQ are deployed on Elastic Compute Service (ECS) instances.

###### Download SDK for C++

This topic describes the preparations, instructions, and usage notes for using SDK for C++ to access ApsaraMQ for RocketMQ so that you can use SDK for C++ to send and subscribe to messages.

**Procedure**

1. Download SDK for C++ used in Linux.
2. Decompress the downloaded package.
After the package is decompressed, the following directory structure appears: demos/ Contains examples on how to send and consume normal messages and ordered messages and how to send messages in one-way transmission mode. This directory also contains the CMakeList.txt file that is used to compile and manage demos. include/ Contains header files that are required by your own programs. lib/ Contains dynamic libraries based on x86_64. The libraries include the libonsclient4cpp.so interface library and the librocketmq_client_core.so core library. changelog Contains bug fixes and new features in the new releases.

###### Use SDK for C++ in Linux

This topic describes how to use SDK for C++ in Linux. Starting June 28, 2019, the new SDK version provides only dynamic library solutions. The library file of ApsaraMQ for RocketMQ is stored in the lib/ directory. You must link librocketmq_client_core.so with libonsclient4cpp.so when you generate executable files. demos has introduced the features of C++ 11 and uses CMake for management. Therefore, you must install CMake 3.0 or later and g++ 4.8 or later in advance.

**Dynamic solution**

GCC 5.x or later has introduced Dual ABI. Therefore, you must add the **-**
**D_GLIBCXX_USE_CXX11_ABI=0** option when you compile the preceding links.
The following sample code provides an example on how to use demos:

```
cd aliyun-mq-linux-cpp-sdk // The path to which the downloaded SDK package is decompres sed. cd demos // Go to the demos directory and modify the demos file by entering information such as the topic and key that you created in the ApsaraMQ for RocketMQ console. cmake . // Check the dependencies and generate a compilation script. make // Compile the code. cd bin // Run the program in the directory where the generated executable files are loc ated.
```

##### Send and subscribe to normal messages

This topic provides the sample code for sending and subscribing to normal messages.

**Send normal messages**

The following sample code provides an example on how to send normal messages:

```
#include "ONSFactory.h"
#include "ONSClientException.h"
using namespace ons; int main()
```

`{`

```
    // Configure producer properties
    ONSFactoryProperty factoryInfo;
    factoryInfo.setFactoryProperty(ONSFactoryProperty::ProducerId, "<your-group-id>");
    factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR, "<your-tcp-endpoin
t>");
    factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics, "<your-topic>");
    factoryInfo.setFactoryProperty(ONSFactoryProperty::MsgContent, "<your-message-conte
nt>");
    // Load credentials from environment variables.
    // Make sure ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are se
```

`t.`

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")); factoryInfosetFactoryProperty(ONSFactoryProperty::SecretKey
```

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
    // Create and start the producer.
    // Call start() exactly once before sending any messages.
    Producer *pProducer = ONSFactory::getInstance()->createProducer(factoryInfo);
    pProducer->start();
    // Build the message
    Message msg(
            factoryInfo.getPublishTopics(),  // Topic (must be a normal-message topic)
            "TagA",                          // Tag -- consumers use tags to filter messa
ges
            factoryInfo.getMessageContent()  // Body -- cannot be empty
```

);

```
    // Set a message key for traceability.
    // Keys must be globally unique whenever possible (for example, an order ID).
    // Use the key to look up messages in the ApsaraMQ for RocketMQ console.
    msg.setKey("ORDERID_100");
    // Send the message. If no exception is thrown, the message is sent.
    try
```

`{`

```
        SendResultONS sendResult = pProducer->send(msg);
    catch(ONSClientException & e)
```

`{`

```
        // Handle the send failure (log, retry, alert, etc.)
    // Shut down the producer before your application exits to prevent issues such as m
emory leaks.
    pProducer->shutdown();
    return 0;
```

**Subscribe to normal messages**

For more information about how to subscribe to normal messages and about relevant sample code, see Subscribe to messages.

##### Send and receive ordered messages

This topic describes how to use the SDK for C or C++ to send and receive ordered messages. This topic also provides sample code.

**Send ordered messages**

The following sample code provides an example on how to send ordered messages by using the TCP client SDK for C or C++:

```
#include "ONSFactory.h"
#include "ONSClientException.h"
#include<iostream>
```

```
#include <iostream>
using namespace ons; int main()
```

`{`

```
    // The parameter that is required to create and use a producer.
    ONSFactoryProperty factoryInfo;
    factoryInfo.setFactoryProperty(ONSFactoryProperty::ProducerId, "XXX");// The ID of
the consumer group that you created in the ApsaraMQ for RocketMQ console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR, "XXX"); // The TCP
endpoint. You can obtain the endpoint in the TCP Endpoint section of the Instance Details page in the ApsaraMQ for RocketMQ console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics,"XXX" );// The top
ic that you created in the ApsaraMQ for RocketMQ console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::MsgContent, "XXX");// The messag
e content.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey, "XXX");// The AccessK
ey ID that you created in the Alibaba Cloud Management Console for identity authenticat ion.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey, "XXX" );// The Access
Key secret that you created in the Alibaba Cloud Management Console for identity authen tication.
    // Create a producer.
    OrderProducer *pProducer = ONSFactory::getInstance()-
>createOrderProducer(factoryInfo);
    //Before sending a message, call the start() method only once to start the producer
```

`.`

```
    pProducer->start();
    Message msg(
                //Message Topic
                factoryInfo.getPublishTopics(),
                // The message tag. A message tag is similar to a Gmail tag and is used
by consumers to filter messages in the ApsaraMQ for RocketMQ broker.
                "TagA",
                // The message body. A message body is data in the binary format. Apsara
MQ for RocketMQ does not process message bodies. The producer and the consumer must agree on the serialization and deserialization methods.
                factoryInfo.getMessageContent()
```

);

```
    // The message key. The key is the business-specific attribute of a message and mus
t be globally unique.
    // If you cannot receive a message as expected, you can use the key to query the me
ssage in the ApsaraMQ for RocketMQ console.
    // Note: A message can be sent and received even if you do not specify the message
key.
    msg.setKey("ORDERID_100");
    // The key field that is used to distinguish partitions for ordered messages.
    std::string shardingKey = "abc";
    // Messages that have the same sharding key are sent in order.
    try
```

`t``y` `{`

```
        // Send the message. If no exception is thrown, the message is sent.
        SendResultONS sendResult = pProducer->send(msg, shardingKey);
    std::cout << "send success" << std::endl;
    catch(ONSClientException & e)
```

`{`

```
        // Specify the logic to handle errors.
    // Before you exit the application, shut down the consumer. Otherwise, issues such
as memory leaks may occur.
    pProducer->shutdown();
    return 0;
```

**Receive ordered messages**

The following sample code provides an example on how to receive ordered messages by using the TCP client SDK for C or C++:

```
#include "ONSFactory.h"
using namespace std; using namespace ons; // Create the consumer instance. //After the push consumer pulls the message, the push consumer calls the consumeMessage function of the instance. class ONSCLIENT_API MyMsgListener : public MessageOrderListener
```

`{`

```
public:
    MyMsgListener()
```

`{`

```
    virtual ~MyMsgListener()
```

`{`

```
    virtual OrderAction consume(Message &message, ConsumeOrderContext &context)
```

`{`

```
        // Consume messages based on your business requirements.
        return Success; //CONSUME_SUCCESS;
```

};

```
int main(int argc, char* argv[])
```

`{`

```
    // The parameter that is required to create and use the consumer.
    ONSFactoryProperty factoryInfo;
    // The ID of the consumer group that you created in the ApsaraMQ for RocketMQ conso
le.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::ConsumerId, "XXX");
    // The topic that you created in the ApsaraMQ for RocketMQ console.
```

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics,"XXX" );
    // Make sure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA
_CLOUD_ACCESS_KEY_SECRET are configured.
    // The AccessKey ID that is used for authentication.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"));
  // The AccessKey secret that is used for authentication.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
    // The TCP endpoint. You can obtain the endpoint in the TCP Endpoint section of the
Instance Details page in the ApsaraMQ for RocketMQ console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR, "XXX");
    // Create the consumer.
    OrderConsumer* orderConsumer = ONSFactory::getInstance()-
>createOrderConsumer(factoryInfo);
    MyMsgListener  msglistener;
    // The message topic and tag to which the consumer subscribes.
    orderConsumer->subscribe(factoryInfo.getPublishTopics(), "*",&msglistener );
    // Register the instance to listen to messages. After the consumer pulls the messag
es, the consumer calls the consumeMessage function of the message listening class.
    //Start the consumer.
    orderConsumer->start();
    for(volatile int i = 0; i < 1000000000; ++i) {
        //wait
    // Destroy the consumer. Before you exit the application, destroy the consumer. Oth
erwise, issues such as memory leaks may occur.
    orderConsumer->shutdown();
   return 0;
```

##### Send and subscribe to scheduled

**messages**

This topic provides the sample code for sending and subscribing to scheduled messages. Scheduled messages are consumed by consumers after a specified period of time. Such messages are used in scenarios where a time window between message production and consumption is required or tasks need to be triggered at a scheduled time. Scheduled messages are used in a similar way to delay queues.

**Send scheduled messages**

The following sample code provides an example on how to send scheduled messages:

```
#include "ONSFactory.h"
```

```
#include "ONSClientException.h"
#include <windows.h>
using namespace ons; int main()
```

`{`

```
    // Create the producer and set the required properties.
    ONSFactoryProperty factoryInfo;
    // The ID of the consumer group that you created in the ApsaraMQ for RocketMQ conso
le.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::ProducerId, "XXX");
    // The TCP endpoint. Find this in the TCP Endpoint section of the Instance Details
page in the ApsaraMQ for RocketMQ console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR, "XXX");
    // The topic that you created in the ApsaraMQ for RocketMQ console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics,"XXX" );
    // The message content.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::MsgContent, "XXX");
    // Make sure the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and
ALIBABA_CLOUD_ACCESS_KEY_SECRET are set.
    // AccessKey ID for authentication.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"));
    // AccessKey secret for authentication.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
    // Create the producer.
    Producer *pProducer = ONSFactory::getInstance()->createProducer(factoryInfo);
    // Call start() once before sending messages.
    pProducer->start();
    Message msg(
            // Message topic.
            factoryInfo.getPublishTopics(),
            // Message tag, used by consumers to filter messages on the broker.
            "TagA",
            // Message body. Must not be empty. The producer and consumer must agree on
the serialization and deserialization methods.
            factoryInfo.getMessageContent()
```

);

```
    // The message key is a business-specific identifier. Keep it globally unique
    // so you can query the message by key in the ApsaraMQ for RocketMQ console.
    // Setting a key is optional.
    msg.setKey("ORDERID_100");
    // Set the delivery time as an absolute timestamp in milliseconds.
    // The broker delivers the message to consumers only after this time.
    // In this example, the message is delivered 3 seconds from now.
    long deliverTime = GetTickCount64() + 3000;
    msg.setStartDeliverTime(deliverTime);
```

```
    // Send the message. If no exception is thrown, the send succeeded.
    try
```

`{`

```
        SendResultONS sendResult = pProducer->send(msg);
    catch(ONSClientException & e)
```

`{`

```
        // Handle the exception.
    // Shut down the producer before exiting to avoid memory leaks.
    pProducer->shutdown();
    return 0;
```

**Subscribe to scheduled messages**

For more information about how to subscribe to scheduled messages and about relevant sample code, see Subscribe to messages.

##### Send and receive transactional messages

This topic describes the interaction process and the status check mechanism of transactional messages. This topic also shows you how to send and subscribe to transactional messages, and provides sample code.

**Interaction process**

The following figure shows the interaction process of transactional messages in ApsaraMQ for RocketMQ. Figure 1. Interaction process of transactional messages

**Send transactional messages**

Perform the following steps to send a transactional message:
1. Send a half message and execute a local transaction. Sample code:

```
#include "ONSFactory.h"
#include "ONSClientException.h"
using namespace ons;
    class MyLocalTransactionExecuter : LocalTransactionExecuter
```

`{`

```
        MyLocalTransactionExecuter()
```

`{`

```
        ~MyLocalTransactionExecuter()
```

`{`

```
        virtual TransactionStatus execute(Message &value)
```

`{`

```
                // The message ID. Two messages can have the same message body but no
t the same ID. You cannot query the ID of the current message in the ApsaraMQ for Roc ketMQ console. )
                string msgId = value.getMsgID();
                // Calculate the message body by using an algorithm such as CRC32 and
MD5.
                // The message ID and CRC32 ID are used to prevent duplicate messages.
                // You do not need to specify the message ID or CRC32 ID if your busin
ess is idempotent. Otherwise, specify the message ID or CRC32 ID to ensure idempotence.
                // To prevent duplicate messages, we recommend that you calculate the
message body by using the CRC32 or MD5 algorithm.
                TransactionStatus transactionStatus = Unknow;
                try {
                    boolean isCommit = The execution result of the local transaction;
                    if (isCommit) {
                        // Commit the message if the local transaction is executed.
                        transactionStatus = CommitTransaction;
                    } else {
                        // Roll back the message if the local transaction failed to be
executed.
                        transactionStatus = RollbackTransaction;
                } catch (...) {
                    //exception handle
                return transactionStatus;
    int main(int argc, char* argv[])
```

`{`

```
        // The parameters that are required to create the producer and send messages.
        ONSFactoryProperty factoryInfo;
        // The ID of the consumer group that you created in the ApsaraMQ for RocketMQ
console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty::ProducerId, "XXX");
        // The TCP endpoint. You can obtain the endpoint in the TCP Endpoint section
of the Instance Details page in the ApsaraMQ for RocketMQ console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR, "XXX");
        // The topic that you created in the ApsaraMQ for RocketMQ console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics,"XXX" );
//Th
```

`t` `t`

```
        // The message content.
        factoryInfo.setFactoryProperty(ONSFactoryProperty::MsgContent, "XXX");
        // Make sure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and A
LIBABA_CLOUD_ACCESS_KEY_SECRET are configured.
        // The AccessKey ID that is used for authentication.
        factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"));
      // The AccessKey secret that is used for authentication.
        factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
        // Create the producer. ApsaraMQ for RocketMQ does not release pChecker. You
must release pChecker by yourself.
        MyLocalTransactionChecker *pChecker = new MyLocalTransactionChecker();
        g_producer = ONSFactory::getInstance()-
>createTransactionProducer(factoryInfo,pChecker);
        // Before you send the message, call the start() method only once to start th
e producer.
        pProducer->start();
        Message msg(
            //Message Topic
            factoryInfo.getPublishTopics(),
            // The message tag. A message tag is similar to a Gmail tag and is used b
y consumers to sort and filter messages in the ApsaraMQ for RocketMQ broker.
            "TagA",
            // The message body. You cannot leave this parameter empty. ApsaraMQ for
RocketMQ does not process message bodies. The producer and consumer must agree on the methods that are used to serialize and deserialize message bodies.
            factoryInfo.getMessageContent()
```

);

```
        // The message key. The key is the business-specific attribute of a message a
nd must be globally unique whenever possible.
        // If you cannot receive a message as expected, you can use the key to query
the message in the ApsaraMQ for RocketMQ console.
        // Note: You can send and receive a message even if you do not specify the ke
```

`y.`

```
        msg.setKey("ORDERID_100");
        // Send the message. If no exception is thrown, the message is sent.
        try
```

`{`

```
            // ApsaraMQ for RocketMQ does not release pExecuter. You must release pEx
ecuter by yourself.
            MyLocalTransactionExecuter pExecuter = new MyLocalTransactionExecuter();
            SendResultONS sendResult = pProducer->send(msg,pExecuter);
        catch(ONSClientException & e)
```

`{`

```
            // Specify the logic to handle exceptions.
        // Before you exit the application, destroy the producer. Otherwise, issues s
uchasmemoryleaksoccur
```

```
uch as memory leaks occur.
        pProducer->shutdown();
        return 0;
```

2. Commit the status of the transactional message.
After the local transaction is executed, the ApsaraMQ for RocketMQ broker must be notified of the transaction status of the current message, no matter whether the execution succeeds or fails. You can notify the ApsaraMQ for RocketMQ broker by using one of the following methods: Commit the status after the local transaction is executed. Wait until the ApsaraMQ for RocketMQ broker sends a request to check the transaction status of the message. A transaction can be in one of the following states:
**TransactionStatus.CommitTransaction**: The transaction is committed. The consumer
can consume the message.
**TransactionStatus.RollbackTransaction**: The transaction is rolled back. The message is
discarded and cannot be consumed.
**TransactionStatus.Unknow**: The status of the transaction is unknown. The ApsaraMQ for
RocketMQ broker is expected to send a request again to the producer to query the status of the local transaction that corresponds to the message.

```
 class MyLocalTransactionChecker : LocalTransactionChecker
```

`{`

```
     MyLocalTransactionChecker()
```

`{`

```
     ~MyLocalTransactionChecker()
```

`{`

```
     virtual TransactionStatus check(Message &value)
```

`{`

```
         // The ID of the message. The current message ID cannot be queried in the cons
ole. Two messages may have the same message body but cannot have the same ID.
         string msgId = value.getMsgID();
         // Calculate the message body by using CRC32 or other algorithms, such as MD5.
         // The message ID and CRC32 ID are used to prevent duplicate messages.
         // You do not need to specify the message ID or CRC32 ID if your business
itself achieves idempotence. Otherwise, specify the message ID or CRC32 ID to ensure id empotence.
         // To prevent duplicate messages, calculate the message body by using the
CRC32 or MD5 algorithm.
         TransactionStatus transactionStatus = Unknow;
         try {
             boolean isCommit = The execution result of the local transaction;
             if (isCommit) {
                 // Commit the message if the local transaction succeeds.
                 transactionStatus = CommitTransaction;
             } else {
                 // Roll back the message if the local transaction fails.
                 transactionStatus = RollbackTransaction;
         } catch(...) {
             //exception error
         return transactionStatus;
```

**Mechanism of transaction status check**

Why must the mechanism of transaction status check be implemented when transactional messages are sent? If the half message is sent in Step 1 but **TransactionStatus.Unknow** is returned for the local transaction, or no status is committed for the local transaction because the application exits, the status of the half message is unknown to the ApsaraMQ for RocketMQ broker. Therefore, the ApsaraMQ for RocketMQ broker periodically requests the producer to check and report the status of the half message. What does the business logic do when the check method is called back? The check method for transactional messages in ApsaraMQ for RocketMQ must contain the logic of transaction consistency check. After a transactional message is sent, ApsaraMQ for RocketMQ must call the **LocalTransactionChecker** operation to respond to the request of the ApsaraMQ for RocketMQ broker for the status of the local transaction. Therefore, the check method for transactional messages must contain the following check items: i. Check whether the status of the local transaction that corresponds to the half message is committed or rollback. ii. Commit the status of the local transaction that corresponds to the half message to the ApsaraMQ for RocketMQ broker. How do different states of the local transaction affect the half message?
**TransactionStatus.CommitTransaction**: The transaction is committed. The message
can be consumed by consumers.
**TransactionStatus.RollbackTransaction**: The transaction is rolled back. The message
is discarded and cannot be consumed.
**TransactionStatus.Unknow**: The status of the transaction is unknown. The ApsaraMQ
for RocketMQ broker is expected to send a request again to the producer to query the status of the local transaction that corresponds to the message. For more information about the code, see the implementation of
**MyLocalTransactionChecker**.

**Subscribe to transactional messages**

For more information about how to subscribe to transactional messages and about relevant sample code, see Subscribe to messages.

##### Subscribe to messages

This topic describes how to subscribe to messages by using SDK for C or C++ provided by ApsaraMQ for RocketMQ.

**Note**

The subscriptions of all consumer instances identified by the same group ID must be consistent. For more information, see Subscription consistency.

**Subscription modes**

ApsaraMQ for RocketMQ supports the following message subscription modes:

**Clustering subscription:**

This mode is used to implement clustering consumption. In clustering consumption mode, all the consumer instances identified by the same group ID evenly share messages. Assume that a topic contains nine messages and a group ID identifies three consumer instances. In clustering consumption mode, each instance consumes three messages.

```
 // Configure clustering subscription, which is the default mode.
 factoryInfo.setFactoryProperty(ONSFactoryProperty:: MessageModel,
ONSFactoryProperty::CLUSTERING);
```

**Broadcasting subscription:**

This mode is used to implement broadcasting consumption. In broadcasting consumption mode, each consumer instance identified by a group ID consumes a message once. Assume that a topic contains nine messages and a group ID identifies three consumer instances. In broadcasting consumption mode, each instance consumes nine messages.

```
 // Configure broadcasting subscription.
 factoryInfo.setFactoryProperty(ONSFactoryProperty:: MessageModel,
ONSFactoryProperty::BROADCASTING);
```

**Sample code**

```
#include "ONSFactory.h"
#include <iostream>
#include <thread>
#include <mutex>
using namespace ons; // Mutex to synchronize access to shared resources across listener threads. std::mutex console_mtx; class ExampleMessageListener : public MessageListener { public:
    Action consume(Message& message, ConsumeContext& context) {
        // Return CommitMessage after successful processing.
        // Return ReconsumeLater if processing fails or you want to consume
        // the message again -- the broker redelivers the message after a
        // predefined interval.
        std::lock_guard<std::mutex> lk(console_mtx);
        std::cout << "Received a message. Topic: " << message.getTopic() << ", MsgId: "
        << message.getMsgID() << std::endl;
        return CommitMessage;
```

};

```
int main(int argc, char* argv[]) {
    std::cout << "=======Before consuming messages=======" << std::endl;
    ONSFactoryProperty factoryInfo;
    // Group ID created in the ApsaraMQ for RocketMQ console.
    // ApsaraMQ for RocketMQ instances use group IDs instead of producer IDs
    // and consumer IDs. This parameter maintains backward compatibility.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::ConsumerId, "GID_XXX");
    // Retrieve credentials from environment variables.
    // Make sure ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET
    // are set before running this program.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"));
    factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
    // Endpoint of the ApsaraMQ for RocketMQ instance.
    // Get this value from the ApsaraMQ for RocketMQ console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR,
"http://xxxxxxxxxxxxxxxx.aliyuncs.com:80");
    PushConsumer *consumer = ONSFactory::getInstance()-
>createPushConsumer(factoryInfo);
    // Subscribe to messages with a specific tag in topic-1.
    const char* topic_1 = "topic-1";
```

```
    const char* tag_1 = "tag-1";
    // Subscribe to all messages in topic-2 by using the wildcard tag "*".
    const char* topic_2 = "topic-2";
    const char* tag_2 = "*";
    // Register the listener and subscribe to both topics.
    ExampleMessageListener * message_listener = new ExampleMessageListener();
    consumer->subscribe(topic_1, tag_1, message_listener);
    consumer->subscribe(topic_2, tag_2, message_listener);
    // Start the consumer. Messages begin arriving after this call.
    consumer->start();
    // Keep the main thread alive. In production, replace this with
    // your application's main loop or signal handler.
    std::this_thread::sleep_for(std::chrono::milliseconds(60 * 1000));
    consumer->shutdown();
    delete message_listener;
    std::cout << "=======After consuming messages======" << std::endl;
    return 0;
```

#### SDK for .NET

##### 7.2.6.1. .Prepare the SDK for .NET environment

###### Overview

Before you use SDK for . NET to access ApsaraMQ for RocketMQ and send and subscribe to messages, make sure that the following prerequisites are met:

**Note**

You have created the topics and group IDs involved in the code in the ApsaraMQ for RocketMQ console. You can customize message tags in your application. For more information about how to create a message tag, see Create resources. Applications that use ApsaraMQ for RocketMQ are deployed on Elastic Compute Service (ECS) instances.

###### Download SDK for .NET

ApsaraMQ for RocketMQ SDK for .NET is a managed wrapper based on Apache RocketMQ Client CPP.ApsaraMQ for RocketMQ SDK for .NET is independent of Windows .NET public library.Multithreading and parallel processing in C++ are used to ensure the efficiency and stability of ApsaraMQ for RocketMQ SDK for .NET.

**Background information**

If Visual Studio is used to develop .NET applications and class libraries, the default target platform is Any CPU. This means that x86 or x64 is automatically selected based on the CPU type at runtime. This capability is provided because the assembly compiled by using .NET is based on the intermediate language (IL). At runtime, the just in-time compiler (JIT) in the common language runtime (CLR) of .NET converts the IL code into the x86 or x64 machine code. The DLL generated by the C or C++ compiler is the machine code. Therefore, a target platform is selected during compilation. The C or C++ project is compiled as an x64 64-bit DLL by configuring compilation options. Therefore, the 64-bit DLL in release mode compiled by using Visual Studio 2015 is provided. The 64-bit DLL in release mode is also available to other Visual Studio versions.

**Note**

C++ DLL files require the installation package of the Virtual C++ 2015 runtime environment. If the Visual Studio 2015 runtime environment is not installed, run the vc_redist.x64.exe program provided in the SDK.

**Procedure**

1. Download the SDK package.
We recommend that both new users and existing users that are not concerned with upgrade costs download the latest SDK. Download the latest version of SDK for .NET that are used in Windows
2. Decompress the downloaded package.
After the package is decompressed, the following directory structure appears: demo/ Contains examples on how to send normal messages, send messages in one-way mode, send ordered messages, consume normal messages, and consume ordered messages. lib/ Contains files related to the underlying C++ DLL and the installation package of the Virtual C++ 2015 runtime environment. If Visual Studio 2015 is not installed, copy and run the vc_redist.x64.exe program, as shown in the following information:

```
  64/
      NSClient4CPP.lib
      ONSClient4CPP.dll
      ONSClient4CPP.pdb
  vc_redist.x64.exe
```

interface/ Encapsulates P/Invoke code. The code must be included in the user project code. SDK_GUIDE.pdf Contains the documentation and frequently asked questions (FAQ) about how to prepare the SDK environment. changelog Contains bug fixes and new features in the new releases.

###### 7.2.6.1.3. .Configure SDK for .NET

This topic shows you how to use SDK for .NET in Windows.

**Procedure**

Use SDK for .NET in Visual Studio 2015NET SDK
1. Use Visual Studio 2015 to create your project.
Figure 1. .NET SDK-1
2. Right-click the project and choose **Add** > **Add Existing Item** to add all files in the
**interface** directory of the downloaded SDK package.
Figure 2. .NET SDK-2
3. Right-click the project and choose **Properties** > **Configuration Manager**. Set **Active**
**solution configuration** to **Release** and set **Active solution platform** to **x64**.
4. Write and compile the test program, save the DLL file of the SDK to the directory of the
executable file or to the system directory, and then run the program. Figure 3. .NET SDK-3

**Note**

The SDK provides a preconfigured demo project. You can directly open the project and compile it. When you run the project, copy the related DLL file to the directory of the executable file, as shown in the following figure. Figure 4. .NET SDK-4
**Configure ASP.NET in Visual Studio 2015 to use** ApsaraMQ for RocketMQ **SDK**
5. Create a **Web Forms** project for ASP.NET by using Visual Studio 2015.
Figure 5. .NET SDK-5
6. Right-click the project and choose **Properties** > **Configuration Manager**. Set **Active**
**solution configuration** to **Release** and set **Active solution platform** to **x64**.
Figure 6. .NET SDK-6
7. Right-click the project and choose **Add** > **Add Existing Item** to add all files in the
interface directory of the downloaded SDK package. For more information about how to configure a common .NET project, see Step 2.
8. Add the code for starting and stopping the SDK to the **Global.asax.cs** file.

**Note**

We recommend that you encapsulate the SDK code as a singleton class so that the code cannot be recycled by the garbage collector due to scope problems. The example directory of the SDK contains the Example.cs file for implementing a simple singleton class. To use Example.cs, you must include it in your own project.

```
using System; using System.Collections.Generic; using System.Linq; using System.Web; using System.Web.Optimization; using System.Web.Routing; using System.Web.Security; using System.Web.SessionState; using ons; // The namespace where the SDK is located. using test; // The namespace where the class with the roughly encapsulated SDK is located. See the Example.cs file in the example directory of the SDK. namespace WebApplication4
```

`{`

```java
    public class Global : HttpApplication
```

`{`

```
        void Application_Start(object sender, EventArgs e)
```

`{`

```
            // Code that runs on application startup
            RouteConfig.RegisterRoutes(RouteTable.Routes);
            BundleConfig.RegisterBundles(BundleTable.Bundles);
            try
```

`{`

```
                // The code for starting the SDK. The following code is the code
after the SDK is roughly encapsulated.
                OnscSharp.CreateProducer();
                OnscSharp.StartProducer();
            catch (Exception ex)
```

`{`

```java
                    // Specify the logic for handling errors.
        protected void Application_End(object sender, EventArgs e)
```

`{`

```
            try
```

`{`

```
               // The code for stopping the SDK.
              OnscSharp.ShutdownProducer();
            catch (Exception ex)
```

`{`

```
              // Specify the logic for handling errors.
```

9. Write and compile the test program.
0. Save the DLL file of the SDK to the directory of the executable file or to the system directory
and run the program. Figure 7. .NET SDK-7
1. Choose **Tools** > **Options** > **Projects and Solutions** > **Web Projects**. Then, select the
**Use the 64 bit version of IIS Express for websites and projects** check box.
Figure 8. .NET SDK-8 Figure 9. .NET SDK-9

##### Send and subscribe to normal messages

This topic provides the sample code for sending and subscribing to normal messages.

**Send normal messages**

The following sample code provides an example on how to send normal messages: Set related parameters based on the instructions.

```java
using System; using ons; public class ProducerExampleForEx
```

`{`

```
    public ProducerExampleForEx()
```

`{`

```
    static void Main(string[] args) {
        // Configure your account based on the resources that you created in the
console.
        ONSFactoryProperty factoryInfo = new ONSFactoryProperty();
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
le for identity authentication.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.AccessKey, "Your access
key");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.SecretKey, "Your access
secret");
        // The group ID that you created in the ApsaraMQ for RocketMQ console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.ProducerId, "GIDexample");
```

`y` `y` `p` `y` `y` `p` `y` `,` `_` `p`

```
        // The topic that you created in the ApsaraMQ for RocketMQ console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.PublishTopics,
"T_example_topic_name");
        // The TCP endpoint. To obtain the endpoint, log on to the ApsaraMQ for RocketM
Q console. In the left-side navigation pane, click Instance Details. On the Instance De tails page, select your instance. On the Instance Information tab, view the endpoint in the Obtain Endpoint Information section.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.NAMESRV_ADDR,
"NameSrv_Addr");
        // Specify the log path.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.LogPath, "C://log");
        // Create a producer instance.
        // Note: Producer instances are thread-secure and can be used to send messages
of different topics. Each of your threads
        // needs only one producer instance.
        Producer producer = ONSFactory.getInstance().createProducer(factoryInfo);
        // Start the producer instance.
        producer.start();
        // Create a message object.
        Message msg = new Message(factoryInfo.getPublishTopics(), "tagA", "Example mess
age body");
        msg.setKey(Guid.NewGuid().ToString());
        for (int i = 0; i < 32; i++) {
            try
```

`{`

```
                SendResultONS sendResult = producer.send(msg);
                Console.WriteLine("send success {0}", sendResult.getMessageId());
            catch (Exception ex)
```

`{`

```
                Console.WriteLine("send failure{0}", ex.ToString());
        // Shut down the producer instance when your thread is about to exit.
        producer.shutdown();
```

**Subscribe to normal messages**

For more information about how to subscribe to normal messages and about relevant sample code, see Subscribe to messages.

##### Send and subscribe to ordered messages

This topic describes how to send and subscribe to ordered messages and provides sample code.

**Send ordered messages**

The following sample code provides an example on how to send ordered messages:

```
using System; using ons; publicclassOrderProducerExampleForEx
```

```java
public class OrderProducerExampleForEx
```

`{`

```
    public OrderProducerExampleForEx()
```

`{`

```
    static void Main(string[] args) {
        // Configure your account based on the resources that you created in the Apsara
Uni-manager Management Console.
        ONSFactoryProperty factoryInfo = new ONSFactoryProperty();
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
le for identity authentication.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.AccessKey, "Your access
key");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.SecretKey, "Your access
secret");
        // The group ID that you created in the ApsaraMQ for RocketMQ console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.ProducerId, "GID_example");
        // The topic that you created in the ApsaraMQ for RocketMQ console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.PublishTopics,
"T_example_topic_name");
        // The TCP endpoint. To obtain the endpoint, log on to the ApsaraMQ for RocketM
Q console. In the left-side navigation pane, click Instance Details. On the Instance De tails page, select your instance. On the Instance Information tab, view the endpoint in the Obtain Endpoint Information section.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.NAMESRV_ADDR,
"NameSrv_Addr");
        // Specify the log path.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.LogPath, "C://log");
        // Create a producer instance.
        // Note: Producer instances are thread-safe and can be used to send messages of
different topics. Each thread
        // requires only one producer instance.
        OrderProducer producer =
ONSFactory.getInstance().createOrderProducer(factoryInfo);
        // Start the producer instance.
        producer.start();
        // Create a message.
        Message msg = new Message(factoryInfo.getPublishTopics(), "tagA", "Example mess
age body");
        string shardingKey = "App-Test";
        for (int i = 0; i < 32; i++) {
            try
```

`{`

```
                SendResultONS sendResult = producer.send(msg, shardingKey);
                Console.WriteLine("send success {0}", sendResult.getMessageId());
            catch (Exception ex)
```

`{`

```
                Console.WriteLine("send failure{0}", ex.ToString());
        // Disable the producer instance when your thread is about to exit.
        producer.shutdown();
```

**Subscribe to ordered messages**

The following sample code provides an example on how to subscribe to ordered messages:

```
using System; using System.Text; using System.Threading; using ons; namespace demo
```

`{`

```java
    public class MyMsgOrderListener : MessageOrderListener
```

`{`

```
        public MyMsgOrderListener()
```

`{`

```
        ~MyMsgOrderListener()
```

`{`

```
        public override ons.OrderAction consume(Message value, ConsumeOrderContext cont
ext)
```

`{`

```
            Byte[] text = Encoding.Default.GetBytes(value.getBody());
            Console.WriteLine(Encoding.UTF8.GetString(text));
            return ons.OrderAction.Success;
    class OrderConsumerExampleForEx
```

`{`

```
        static void Main(string[] args)
```

`{`

```
            // Configure your account based on the resources that you created in the
Apsara Uni-manager Management Console.
            ONSFactoryProperty factoryInfo = new ONSFactoryProperty();
            // The AccessKey ID that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
            factoryInfo.setFactoryProperty(ONSFactoryProperty.AccessKey, "Your access
key");
            // The AccessKey secret that you created in the Apsara Uni-manager
Management Console for identity authentication.
            factoryInfo.setFactoryProperty(ONSFactoryProperty.SecretKey, "Your access
secret");
            // The group ID that you created in the ApsaraMQ for RocketMQ console.
            factoryInfo.setFactoryProperty(ONSFactoryProperty.ConsumerId,
"GID_example");
            // The topic that you created in the ApsaraMQ for RocketMQ console.
            factoryInfo.setFactoryProperty(ONSFactoryProperty.PublishTopics,
"T_example_topic_name");
            // The TCP endpoint. To obtain the endpoint, log on to the ApsaraMQ for Roc
ketMQ console. In the left-side navigation pane, click Instance Details. On the Instanc e Details page, select your instance. On the Instance Information tab, view the endpoin t in the Obtain Endpoint Information section.
```

```
            factoryInfo.setFactoryProperty(ONSFactoryProperty.NAMESRV_ADDR,
"NameSrv_Addr");
            // Specify the log path.
            factoryInfo.setFactoryProperty(ONSFactoryProperty.LogPath, "C://log");
            // Create a consumer instance.
            OrderConsumer consumer =
ONSFactory.getInstance().createOrderConsumer(factoryInfo);
            // Subscribe to topics.
            consumer.subscribe(factoryInfo.getPublishTopics(), "*",new
MyMsgOrderListener());
            // Start the consumer instance.
            consumer.start();
            // Put the main thread to sleep for a period of time.
            Thread.Sleep(30000);
            // Disable the consumer instance when the instance is no longer used.
            consumer.shutdown();
```

##### Send and subscribe to scheduled

**messages**

Scheduled messages are consumed by consumers after a specified period of time. Such messages are used in scenarios where a time window between message production and consumption is required or tasks need to be triggered at a scheduled time. Scheduled messages are used in a similar way to delay queues.

**Send scheduled messages**

The following sample code provides an example on how to send scheduled messages:

```
using System; using System.Collections.Generic; using System.Linq; using System.Text; using System.Runtime.InteropServices; using ons; namespace ons
```

`{`

```
    class onscsharp
```

`{`

```
        static void Main(string[] args)
```

`{`

```
            // Set the parameters that are required to create a producer. These
parameters ensure that you can use the producer.
            ONSFactoryProperty factoryInfo = new ONSFactoryProperty();
            factoryInfo.setFactoryProperty(factoryInfo.ProducerId, "XXX ");// The group
ID that you created in the ApsaraMQ for RocketMQ console.
            factoryInfo.setFactoryProperty(factoryInfo.NAMESRV_ADDR, "XXX"); // The TCP
endpoint. To obtain the endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instance Details. On the Instance Details page, select yourinstance.OntheInstanceInformationtab,viewtheendpointintheObtainEndpoin
```

```
your instance. On the Instance Information tab, view the endpoint in the Obtain Endpoin t Information section.
            factoryInfo.setFactoryProperty(factoryInfo.PublishTopics, "XXX");// The
topic that you created in the ApsaraMQ for RocketMQ console.
            factoryInfo.setFactoryProperty(factoryInfo.MsgContent, "XXX");// The
message content.
            factoryInfo.setFactoryProperty(factoryInfo.AccessKey, "XXX");// The
AccessKey ID that you created in the Apsara Uni-manager Management Console for identity authentication.
            factoryInfo.setFactoryProperty(factoryInfo.SecretKey,"XXX");// The
AccessKey secret that you created in the Apsara Uni-manager Management Console for iden tity authentication.
            // Create a producer.
            ONSFactory onsfactory = new ONSFactory();
            Producer pProducer = onsfactory.getInstance().createProducer(factoryInfo);
            // Before you use the producer to send a message, call the start() method o
nce to start the producer.
            pProducer.start();
            Message msg = new Message(
                //Message Topic
                factoryInfo.getPublishTopics(),
                //Message Tag
                "TagA",
                //Message Body
                factoryInfo.getMessageContent()
```

);

```
            // The key of the message. The key is the business-specific attribute of th
e message and must be globally unique whenever possible.
            // A unique key helps you query and resend a message in the ApsaraMQ for Ro
cketMQ console if the message fails to be received.
            // Note: Messages can be sent and received even if you do not specify the m
essage key.
            msg.setKey("ORDERID_100");
            // The period of time after which the ApsaraMQ for RocketMQ broker delivers
the message to the consumer. Unit: milliseconds. The message can be consumed only after the specified period of time. In this example, the message can be consumed 3 seconds la ter.
            long deliverTime = Current system time (ms) + 3000;
            msg.setStartDeliverTime(deliverTime);
            // Send the message. If no error occurs, the message is sent.
            try
```

`{`

```
                SendResultONS sendResult = pProducer.send(msg);
            catch(ONSClientException e)
```

`{`

```
                // Specify the logic for handling failures.
            // Before you exit the application, shut down the producer object.
Otherwise, memory leaks may occur.
            pProducer.shutdown();
```

**Subscribe to scheduled messages**

For more information about how to subscribe to scheduled messages and about relevant sample code, see Subscribe to messages.

##### Send and receive transactional messages

This topic describes the interaction process and the status check mechanism of transactional messages. This topic also shows you how to send and subscribe to transactional messages, and provides sample code.

**Interaction process**

The following figure shows the interaction process of transactional messages in ApsaraMQ for RocketMQ. Figure 1. Interaction process of transactional messages

**Send transactional messages**

Perform the following steps to send a transactional message:
1. Send a half message and execute a local transaction. Sample code:

```
 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Runtime.InteropServices;
 using ons;
 namespace ons
```

`{`

```java
 public class MyLocalTransactionExecuter : LocalTransactionExecuter
```

`{`

```
     public MyLocalTransactionExecuter()
```

`{`

```
     ~MyLocalTransactionExecuter()
```

`{`

```
     public override TransactionStatus execute(Message value)
```

`{`

```
             Console.WriteLine("execute topic: {0}, tag:{1}, key:{2}, msgId:
{3},msgbody:{4}, userProperty:{5}",
             value.getTopic(), value.getTag(), value.getKey(), value.getMsgID(), value
.getBody(), value.getUserProperty("VincentNoUser")); //TheIDofthemessage Twomessagesmayhavethesamemessagebodybu
```

```
             // The ID of the message. Two messages may have the same message body bu
t cannot have the same ID. The current message ID cannot be queried in the console.
             string msgId = value.getMsgID();
             // Calculate the message body by using CRC32 or other algorithms, such as
MD5.
             // The message ID and CRC32 ID are used to prevent duplicate messages.
             // To prevent duplicate messages, calculate the message body by using
the CRC32 or MD5 algorithm.
             TransactionStatus transactionStatus = TransactionStatus.Unknow;
             try {
                 boolean isCommit = The execution result of the local transaction;
                 if (isCommit) {
                     // Commit the message if the local transaction succeeds.
                     transactionStatus = TransactionStatus.CommitTransaction;
                 } else {
                     // Roll back the message if the local transaction fails.
                     transactionStatus = TransactionStatus.RollbackTransaction;
             } catch (Exception e) {
                 //exception handle
             return transactionStatus;
 class onscsharp
```

`{`

```
     static void Main(string[] args)
```

`{`

```
         ONSFactoryProperty factoryInfo = new ONSFactoryProperty();
         factoryInfo.setFactoryProperty(factoryInfo.NAMESRV_ADDR, "XXX");// The TCP e
ndpoint. To obtain the endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instances. Click the instance that you want to manag e to go to the Instance details page. On the Basic information tab, view the endpoint of the instance.
         factoryInfo.setFactoryProperty(factoryInfo.ProducerId, "");// The group ID t
hat you created in the ApsaraMQ for RocketMQ console.
         factoryInfo.setFactoryProperty(factoryInfo.PublishTopics, "");// The topic t
hat you created in the ApsaraMQ for RocketMQ console.
         factoryInfo.setFactoryProperty(factoryInfo.MsgContent, "");//message body
         factoryInfo.setFactoryProperty(factoryInfo.AccessKey, "");// The AccessKey I
D that you created in the Apsara Uni-manager Management Console for identity authenti cation.
         factoryInfo.setFactoryProperty(factoryInfo.SecretKey, "");// The AccessKey s
ecret that you created in the Apsara Uni-manager Management Console for identity auth entication.
         //create transaction producer
         ONSFactory onsfactory = new ONSFactory();
         LocalTransactionChecker myChecker = new MyLocalTransactionChecker();
         TransactionProducer pProducer =
onsfactory.getInstance().createTransactionProducer(factoryInfo,ref myChecker);
         // Before you use the producer to send a message, call the start() method on
ce to start the producer. After the producer is started, messages can be concurrently sent in multiple threads.
         pProducer.start();
             Message msg = new Message(
```

`g` `g` `g``(`

```
             //Message Topic
             factoryInfo.getPublishTopics(),
             //Message Tag
             "TagA",
             //Message Body
             factoryInfo.getMessageContent()
```

);

```
         // Specify a key for the message. The key is the business-specific attribute
of the message and must be globally unique whenever possible.
         // A unique key helps you query and resend a message in the console if the m
essage fails to be received.
         // Note: A message can be sent and received even if you do not specify a mes
sage key.
         msg.setKey("ORDERID_100");
         // Send the message. If no error occurs, the message is sent.
         try
```

`{`

```
             LocalTransactionExecuter myExecuter = new MyLocalTransactionExecuter();
             SendResultONS sendResult = pProducer.send(msg, ref myExecuter);
         catch(ONSClientException e)
```

`{`

```
             Console.WriteLine("\nexception of sendmsg:{0}",e.what() );
         // Before you exit the application, shut down the producer object.
Otherwise, memory leaks may occur.
         // The producer cannot be started again after the producer object is shut do
wn.
         pProducer.shutdown();
```

2. Commit the status of the transactional message.
After the local transaction is executed, the ApsaraMQ for RocketMQ broker must be notified of the transaction status of the current message, no matter whether the execution succeeds or fails. You can notify the ApsaraMQ for RocketMQ broker by using one of the following methods: Commit the status after the local transaction is executed. Wait until the ApsaraMQ for RocketMQ broker sends a request to check the transaction status of the message. A transaction can be in one of the following states:
**TransactionStatus.CommitTransaction**: The transaction is committed. The message
can be consumed by consumers.
**TransactionStatus.RollbackTransaction**: The transaction is rolled back. The message
is discarded and cannot be consumed.
**TransactionStatus.Unknow**: The status of the transaction is unknown. The ApsaraMQ
for RocketMQ broker is expected to send a request again to the producer to query the status of the local transaction that corresponds to the message.

```java
    public class MyLocalTransactionChecker : LocalTransactionChecker
```

`{`

```
        public MyLocalTransactionChecker()
```

`{`

```
        ~MyLocalTransactionChecker()
```

`{`

```
        public override TransactionStatus check(Message value)
```

`{`

```
                Console.WriteLine("check topic: {0}, tag:{1}, key:{2}, msgId:
{3},msgbody:{4}, userProperty:{5}",
                value.getTopic(), value.getTag(), value.getKey(), value.getMsgID(), va
lue.getBody(), value.getUserProperty("VincentNoUser"));
                // The ID of the message. Two messages may have the same message body
but cannot have the same ID. The current message ID cannot be queried in the console.
                string msgId = value.getMsgID();
                // Calculate the message body by using CRC32 or other algorithms, such
as MD5.
                // The message ID and CRC32 ID are used to prevent duplicate messages.
                // You do not need to specify the message ID or CRC32 ID if your busin
ess itself achieves idempotence. Otherwise, specify the message ID or CRC32 ID to ens ure idempotence.
                // To prevent duplicate messages, calculate the message body by using
the CRC32 or MD5 algorithm.
                TransactionStatus transactionStatus = TransactionStatus.Unknow;
                try {
                    boolean isCommit = The execution result of the local transaction;
                    if (isCommit) {
                        // Commit the message if the local transaction succeeds.
                        transactionStatus = TransactionStatus.CommitTransaction;
                    } else {
                        // Roll back the message if the local transaction fails.
                        transactionStatus = TransactionStatus.RollbackTransaction;
                } catch (Exception e) {
                    //exception handle
                return transactionStatus;
```

**Mechanism of transaction status check**

Why must the mechanism of transaction status check be implemented when transactional messages are sent? If the half message is sent in Step 1 but **TransactionStatus.Unknow** is returned for the local transaction, or no status is committed for the local transaction because the application exits, the status of the half message is unknown to the ApsaraMQ for RocketMQ broker. Therefore, the ApsaraMQ for RocketMQ broker periodically requests the producer to check and report the status of the half message. What does the business logic do when the check method is called back? The check method for transactional messages in ApsaraMQ for RocketMQ must contain the logic of transaction consistency check. After a transactional message is sent, ApsaraMQ for RocketMQ must call the **LocalTransactionChecker** operation to respond to the request of the ApsaraMQ for RocketMQ broker for the status of the local transaction. Therefore, the check method for transactional messages must contain the following check items: i. Check whether the status of the local transaction that corresponds to the half message is committed or rollback. ii. Commit the status of the local transaction that corresponds to the half message to the ApsaraMQ for RocketMQ broker. How do different states of the local transaction affect the half message?
**TransactionStatus.CommitTransaction**: The transaction is committed. The message
can be consumed by consumers.
**TransactionStatus.RollbackTransaction**: The transaction is rolled back. The message
is discarded and cannot be consumed.
**TransactionStatus.Unknow**: The status of the transaction is unknown. The ApsaraMQ
for RocketMQ broker is expected to send a request again to the producer to query the status of the local transaction that corresponds to the message. For more information about the code, see the implementation of
**MyLocalTransactionChecker**.

**Subscribe to transactional messages**

For more information about how to subscribe to transactional messages and about relevant sample code, see Subscribe to messages.

##### Subscribe to messages

This topic describes how to use ApsaraMQ for RocketMQ SDK for .NET to subscribe to messages.

**Note**

The subscriptions of all consumer instances identified by the same group ID must be consistent. For more information, see Subscription consistency.

**Subscription modes**

ApsaraMQ for RocketMQ supports the following message subscription modes:
**Clustering subscription**: In this mode, all the consumer instances identified by the same
group ID evenly share messages. Assume that a topic contains nine messages and a group ID identifies three consumer instances. In clustering consumption mode, each instance consumes three messages.

```
 // Configure clustering subscription, which is the default mode.
 factoryInfo.setFactoryProperty(ONSFactoryProperty.MessageModel,
ONSFactoryProperty.CLUSTERING);
```

**Broadcasting subscription:** In this mode, each consumer instance identified by a group
ID consumes a message once. Assume that a topic contains nine messages and a group ID identifies three consumer instances. In broadcasting consumption mode, each instance consumes nine messages.

```
 // Configure broadcasting subscription.
 factoryInfo.setFactoryProperty(ONSFactoryProperty.MessageModel,
ONSFactoryProperty.BROADCASTING);
```

**Sample code**

```java
using System; using System.Threading; using System.Text; using ons; // The callback function to be executed when a message is pulled from the ApsaraMQ for RocketMQ broker. public class MyMsgListener : MessageListener
```

`{`

```
    public MyMsgListener()
```

`{`

```
    ~MyMsgListener()
```

`{`

```
    public override ons.Action consume(Message value, ConsumeContext context)
```

`{`

```java
        Byte[] text = Encoding.Default.GetBytes(value.getBody());
        Console.WriteLine(Encoding.UTF8.GetString(text));
        return ons.Action.CommitMessage;
public class ConsumerExampleForEx
```

`{`

```
    public ConsumerExampleForEx()
```

`{`

```
    static void Main(string[] args) {
        // Configure your account based on the resources that you created in the
console.
        ONSFactoryProperty factoryInfo = new ONSFactoryProperty();
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
le for identity authentication.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.AccessKey, "Your access
key");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.SecretKey, "Your access
secret");
        // The group ID that you created in the ApsaraMQ for RocketMQ console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.ConsumerId, "GID_example");
        // The topic that you created in the ApsaraMQ for RocketMQ console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.PublishTopics,
"T_example_topic_name");
        // The TCP endpoint. To obtain the endpoint, log on to the ApsaraMQ for RocketM
Q console. In the left-side navigation pane, click Instance Details. On the Instance De tails page, select your instance. On the Instance Information tab, view the endpoint in the Obtain Endpoint Information section.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.NAMESRVADDR,
```

```
actoy o.setactoy opety(OSactoy opety.
```

`S` `_` `,`

```
"NameSrv_Addr");
        // Specify the log path.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.LogPath, "C://log");
        // The clustering consumption mode.
        // factoryInfo.setFactoryProperty(ONSFactoryProperty:: MessageModel,
ONSFactoryProperty.CLUSTERING);
        // The broadcasting consumption mode.
        // factoryInfo.setFactoryProperty(ONSFactoryProperty:: MessageModel,
ONSFactoryProperty.BROADCASTING);
        // Create a consumer instance.
        PushConsumer consumer =
ONSFactory.getInstance().createPushConsumer(factoryInfo);
        // Subscribe to topics.
        consumer.subscribe(factoryInfo.getPublishTopics(), "*", new MyMsgListener());
        // Start the consumer instance.
        consumer.start();
        // This value is an example in the demo. In your production environment, you
must set a proper value to make sure that the process does not unexpectedly exit.
        Thread.Sleep(300000);
        // Shut down the consumer instance when the process is about to exit.
        consumer.shutdown();
```

### HTTP client SDK reference

#### Protocol description

##### Common parameters

This topic describes the common request parameters in an HTTP request header and the common response parameters in an HTTP response header for ApsaraMQ for RocketMQ.

**Common request header**

| Parameter | Required | Description |
|---|---|---|
| Authorization | Yes | The authorization string. Specify the value in the following format: MQ <AccessKey ID>: <Signature> . For more information, see Request signatures. |

|   |   |   | MQ |
|---|---|---|---|
|   |   | <AccessKey ID>: |   |
|   |   | <Signature> |   |

| Content-Length | Yes | The length of the HTTP request body. |
|---|---|---|
| Content-Type | Yes | The Multipurpose Internet Mail Extensions (MIME) type of the request body. Set the value to text/xml; charset=utf-8. This value sets the MIME type to XML and the character encoding method to UTF-8. |
| Date | Yes | The time when the request is constructed. The time must be in UTC. If the interval between the time when the request is constructed and the time when the request is received exceeds 15 minutes, the ApsaraMQ for RocketMQ broker determines that the request is invalid. |
| Host | Yes | The HTTP endpoint that you obtain on the Instances page of the console. |
| x-mq-version | Yes | The version of the ApsaraMQ for RocketMQ API. Set the value to 2015-06-06. |
| Content-MD5 | No | The MD5 hash value of the message body. For more information, see Content-MD5 Header Field. |

**Common response header**

| Parameter | Description |
|---|---|
| Content-Length | The length of the HTTP response body. |
| Connection | The status of the HTTP connection. |
| Date | The time when the response was returned. The time is displayed in UTC. |

| x-mq-request-id | The ID of the request. |
|---|---|
| x-mq-version | The version of the ApsaraMQ for RocketMQ API. The value is 2015-06-06. |

##### Request signatures

ApsaraMQ for RocketMQ verifies each HTTP request for access. Each HTTP request that is submitted to ApsaraMQ for RocketMQ contains an Authorization header that contains a signature. This topic describes how to generate a signature.

**Background information**

Apsara Stack issues an AccessKey pair that consists of an AccessKey ID and an AccessKey secret to each user. The user can apply for and manage AccessKey pairs in the Apsara Unimanager Management Console. The AccessKey ID is used to verify the identity of the user. The AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. The HTTP service provided by ApsaraMQ for RocketMQ uses an AccessKey pair to perform symmetric encryption to verify the identity of a request sender. If the calculated verification code is the same as that provided in the request, the HTTP service determines that the request is valid. Otherwise, the HTTP service rejects the request and returns HTTP 403. You must add the Authorization parameter to the header of each HTTP request to provide the signature of the request. This way, the HTTP service can determine the validity of the request.

**How to sign a request**

The Authorization parameter is specified in the following format:

```
 MQ <AccessKey ID>:<Signature>
```

The following code shows the parameters that are used to generate a signature:

```
Signature = base64(hmac-sha1(HTTP_METHOD + "\n"
                + "\n"+ CONTENT-TYPE + "\n"
                + DATE + "\n"
                + "x-mq-version:" + MQVersion + "\n"
                + CanonicalizedResource))
```

**HTTP_METHOD**: specifies an HTTP method in uppercase, such as PUT, GET, POST, or
DELETE.
**CONTENT-TYPE**: specifies the type of the request body. Set the value to text/xml;
charset=utf-8.
**DATE**: specifies the time when you want to perform the operation. This parameter cannot
be left empty and must be specified in UTC. For example, you can set this parameter to Thu, 07 Mar 2012 18:49:58 GMT.
**MQVersion**: specifies the version of the ApsaraMQ for RocketMQ API. The current version is
2015-06-06.
**CanonicalizedResource**: specifies the Uniform Resource Identifier (URI) of the resource
requested by the HTTP request. For example, set the URI of a consumption request to /topics/abc/messages?consumer=GID_abc.

**Note**

The string-to-sign must be in the UTF-8 format. The HMAC-SHA1 method defined in RFC 2104 is used to calculate the signature. In this method, the AccessKey secret is used as an encryption key.

##### Operation for sending messages

You can call this operation to send messages from a producer to an ApsaraMQ for RocketMQ broker.

**Request structure**

Request line

```
 POST /topics/TopicName/messages?ns=INSTANCE_ID HTTP/1.1
```

The following table describes the parameters in the request line.

| Parameter | Required | Description |
|---|---|---|
| TopicName | Yes | The name of the topic to which you want to send messages. |
| ns | No | The instance ID. This parameter is required for new instances that have namespaces. Check whether your instance has a namespace on the Instance Details page in the ApsaraMQ for RocketMQ console. Instances are classified into default instances and new instances based on whether they have namespaces. Default instance: A default instance does not have a namespace. The names of all resources in a default instance must be globally unique. New instance: A new instance has a namespace. The names of all resources in a new instance must be unique within the instance. For more information, see Optimization of resource isolation by instance. |

Request body (XML format) The following table describes the parameters in the request body.

| Parameter | Required | Description |
|---|---|---|
| MessageTag | No | The message tag. |
| MessageBody | Yes | The message body. |
| Properties | No | The message attributes. |

The following items describe key-value pairs in the serialized attributes of the message: The key-value pairs are displayed in the key1:value1|key2:value2|key3:value3 format. The following table describes the parameters that are used to specify the key-value pairs.

| Parameter | Type | Description |
|---|---|---|
| KEYS | String | The message key. |
| STARTDELIVERTIME __ | Long | The absolute scheduled time of a scheduled message. The value is a UNIX timestamp in milliseconds. |
| TransCheckT __ | Long | The relative time when you want to perform the first status check for a transactional message. Valid values: 10 to 300. Unit: seconds. |

**Response structure**

Response line

```
 HTTP/1.1 201
```

Response body The following table describes the parameters in the response body.

| Parameter | Type | Description |
|---|---|---|
| MessageId | String | The message ID. |
| MessageBodyMD5 | String | The MD5 hash value of the message body. |

**Examples**

Sample request

```xml
<?xml version="1.0" encoding="UTF-8"?> <Message xmlns="http://mq.aliyuncs.com/doc/v1/">
    <MessageBody>a</MessageBody>
<MessageTag>Tag</MessageTag> <Properties>KEYS:MessageKey|__STARTDELIVERTIME:1571388173000</Properties> </Message>
```

Sample response

```xml
<Message xmlns="http://mq.aliyuncs.com/doc/v1/"> <MessageId>1E057D566EAD42A579935B5CD874****</MessageId> <MessageBodyMD5>0CC175B9C0F1B6A831C399E26977****</MessageBodyMD5> </Message>
```

##### Operation for consuming messages

You can call this operation to consume messages from an ApsaraMQ for RocketMQ broker.

**Request structure**

Request line

```
 GET /topics/TopicName/messages?
ns=INSTANCE_ID&consumer=GID&tag=taga&numOfMessages=3&waitseconds=3 HTTP/1.1
```

**Important**

The total length of the request line cannot exceed 1,024 characters. The following table describes the parameters in the request line.

| Parameter | Required | Description |
|---|---|---|
| TopicName | Yes | The name of the topic from which you want to consume messages. |

| ns | No | The instance ID. This parameter is required for new instances that have namespaces. You can check whether your instance has a namespace on the Instances page in the ApsaraMQ for RocketMQ console. Instances are classified into default instances and new instances based on whether they have namespaces. Default instance: A default instance does not have a namespace. The names of all resources on a default instance must be globally unique. New instance: A new instance has a namespace. The names of all resources on a new instance must be unique within the instance. For more information, see Optimization of resource isolation by instance. |
|---|---|---|
| consumer | Yes | The ID of the consumer group. |
| tag | No | The message tag. If you do not specify a tag, all messages are pulled. If you want to specify multiple tags, separate them with double vertical bars (\|\|). Example: TagA\|\|TagB. |
| numOfMessages | Yes | The maximum number of messages that can be consumed at the same time. Valid values: 1 to 16. |
| waitseconds | No | The long polling period. If you do not configure this parameter, short polling is used. Valid values: 1 to 30. Unit: seconds. |

Request body (XML format) None.

**Response structure**

A message is available for consumption. Response line

```
 HTTP/1.1 200
```

Response body The following table describes the parameters in the response body.

| Parameter | Type | Description |
|---|---|---|
| MessageId | String | The message ID. |
| MessageBodyMD5 | String | The MD5 hash value of the message body. |
| MessageBody | String | The message body. |
| ReceiptHandle | String | The receipt handle that is used to acknowledge that the message is consumed. The receipt handle can be used only once and must be used before the period of time specified by the NextConsumeTime parameter elapses. The receipt handles that are obtained each time the same message is retried and consumed are different. |
| PublishTime | String | The timestamp that indicates the time when the message was sent. Unit: milliseconds. |
| FirstConsumeTime | String | The timestamp that indicates the time when the message was consumed for the first time. Unit: milliseconds. |

| NextConsumeTime | String | The timestamp that indicates the absolute time when the message was retried. Unit: milliseconds. Note If you connect to ApsaraMQ for RocketMQ over HTTP, a non-ordered message is retried every 5 minutes and an ordered message is retried every minute. Each message can be retried up to 288 times. |
|---|---|---|
| ConsumedTimes | String | The number of retries after the message failed to be consumed. |
| MessageTag | String | The message tag. |
| Properties | String | The message attributes. |

The following items describe key-value pairs in the serialized attributes of the message: The key-value pairs are displayed in the key1:value1|key2:value2|key3:value3 format. The following table describes the parameters in a key-value pair.

| Parameter | Type | Description |
|---|---|---|
| KEYS | String | The message key. |
| STARTDELIVERTIME __ | Long | The absolute scheduled time of the scheduled message. This value is a UNIX timestamp in milliseconds. |
| TransCheckT __ | Long | The relative time that indicates the time when the first status check for the transactional message is performed. Unit: seconds. Valid values: 10 to 300. |

No message is available for consumption. Response line

```
 HTTP/1.1 404
```

Response body The following table describes the parameters in the response body.

| Parameter | Type | Description |
|---|---|---|
| Code | String | The error code. MessageNotExist indicates that no message is available for consumption. If this error code is returned, the response is a normal response. |
| Message | String | The error message. |
| RequestId | String | The request ID. |
| HostId | String | The host that sent the request. |

**Sample responses**

A message is available for consumption.

```xml
<?xml version="1.0" ?> <Messages xmlns="http://mq.aliyuncs.com/doc/v1"> <Message>
  <MessageId>1E057D5E6EAD42A579937046FE17****</MessageId>
  <MessageBodyMD5>0CC175B9C0F1B6A831C399E26977****</MessageBodyMD5>
  <MessageBody>a</MessageBody>
  <ReceiptHandle>1E057D5E6EAD42A579937046FE17****-MTI5N****</ReceiptHandle>
  <PublishTime>1571742900759</PublishTime>
  <FirstConsumeTime>1571742902463</FirstConsumeTime>
  <NextConsumeTime>1571742922463</NextConsumeTime>
  <ConsumedTimes>1</ConsumedTimes>
  <MessageTag>Tag</MessageTag>
  <Properties>KEYS:MessageKey|__BORNHOST:30.5.**.**|</Properties>
</Message> <Message>
  <MessageId>1E057D5E6EAD42A579937046FE17****</MessageId>
  <MessageBodyMD5>0CC175B9C0F1B6A831C399E26977****</MessageBodyMD5>
  <MessageBody>a</MessageBody>
  <ReceiptHandle>1E057D5E6EAD42A579937046FE17****-MTI5N****</ReceiptHandle>
  <PublishTime>1571742900759</PublishTime>
  <FirstConsumeTime>1571742902463</FirstConsumeTime>
  <NextConsumeTime>1571742922463</NextConsumeTime>
  <ConsumedTimes>1</ConsumedTimes>
  <MessageTag>Tag</MessageTag>
  <Properties>KEYS:MessageKey|__BORNHOST:30.5.**.**|</Properties>
</Message> </Messages>
```

No message is available for consumption.

```xml
<?xml version="1.0" ?> <Error xmlns="http://mq.aliyuncs.com/doc/v1">
  <Code>MessageNotExist</Code>
  <Message>Message not exist.</Message>
  <RequestId>5DAEE3FF463541AD6E0322EB</RequestId>
  <HostId>http://123.mqrest.cn-hangzhou.aliyuncs.com</HostId>
</Error>
```

##### Operation for acknowledging messages

You can call this operation to acknowledge the consumption status of messages.

**Request structure**

Request line

```
 DELETE /topics/TopicName/messages?ns=INSTANCE_ID&consumer=GID HTTP/1.1
```

The following table describes the parameters in the request line.

| Parameter | Required | Description |
|---|---|---|

| TopicName | Yes | The name of the topic that contains the messages you want to acknowledge. |
|---|---|---|
| ns | No | The instance ID. This parameter is required for new instances that have namespaces. You can check whether your instance has a namespace on the Instances page in the ApsaraMQ for RocketMQ console. Instances are classified into default instances and new instances based on whether they have namespaces. Default instance: A default instance does not have a namespace. The names of all resources in a default instance must be globally unique. New instance: A new instance has a namespace. The names of all resources in a new instance must be unique within the instance. For more information, see Optimization of resource isolation by instance. |
| consumer | Yes | The ID of the consumer group. |

Request body (XML format) The following table describes the parameters in the request body.

| Parameter | Required | Description |
|---|---|---|

| ReceiptHandle | Yes | The receipt handle that is used to acknowledge that a message is consumed. You can call the operation for consuming messages to obtain the receipt handle. For more information, see Operation for consuming messages. The receipt handle can be used only once and must be used before the period of time specified by the NextConsumeTime parameter elapses. The receipt handles that are obtained each time the same message is retried are different. |
|---|---|---|

**Response structure**

Successful request Response line

```
 HTTP/1.1 204
```

Response body None. Failed request Response line

```
 HTTP/1.1 404
```

Response body For more information, see Examples.

**Examples**

Sample request

```xml
<?xml version="1.0" encoding="UTF-8"?> <ReceiptHandles xmlns="http://mq.aliyuncs.com/doc/v1/"> <ReceiptHandle>1E057D5E6EAD42A57993704EC383****-MTI5NT****</ReceiptHandle> <ReceiptHandle>1E057D5E6EAD42A57993704EC383****-MTI5NT****</ReceiptHandle> <ReceiptHandle>1E057D5E6EAD42A57993704EC383****-MTI5NT****</ReceiptHandle> </ReceiptHandles>
```

Sample response The request body does not contain a handle.

```xml
    <?xml version="1.0" ?>
    <Error xmlns="http://mq.aliyuncs.com/doc/v1">
<Code>MissingReceiptHandle</Code> <Message>ReceiptHandle is required.</Message> <RequestId>5DAEF2B9463541AD6E04490F</RequestId> <HostId>http://123.mqrest.cn-hangzhou.aliyuncs.com</HostId>
    </Error>
```

The handle of the request is invalid. The invalid handle is `adfadfadf` .

```xml
    <?xml version="1.0" ?>
    <Errors xmlns="http://mq.aliyuncs.com/doc/v1">
<Error>
        <ErrorCode>ReceiptHandleError</ErrorCode>
        <ErrorMessage>The receipt handle you provide is not valid.</ErrorMessage>
        <ReceiptHandle>adfadfadf</ReceiptHandle>
</Error>
    </Errors>
```

The handle of the request has expired. This indicates that the handle is not used before the period of time specified by the **NextConsumeTime** parameter elapses.

```xml
    <?xml version="1.0" ?>
    <Errors xmlns="http://mq.aliyuncs.com/doc/v1">
<Error>
        <ErrorCode>MessageNotExist</ErrorCode>
        <ErrorMessage>The receipt handle you provided has expired.</ErrorMessage>
        <ReceiptHandle>1E057D5E6EAD42A57993704EC383****-MTI5NT****</ReceiptHandle>
</Error>
    </Errors>
```

#### Java SDK

##### Prepare the environment

This topic describes how to prepare the environment before you use the HTTP client SDK for Java to send and consume messages.

**Environment requirements**

Java Development Kit (JDK) 1.6 or later is installed. For more information, see Java Downloads. Maven is installed. For more information, see Downloading Apache Maven 3.8.6.

**Install the SDK for Java**

Use Maven to import dependencies and add the following dependency to the pom.xml file:

```xml
<dependency>
    <groupId>com.aliyun.mq</groupId>
    <artifactId>mq-http-sdk</artifactId>
    <! -- Specify the version number of the SDK for Java. -->
    <version>X.X.X</version>
    <classifier>jar-with-dependencies</classifier>
</dependency>
```

**Note**

For more information about the versions of the SDK for Java, see Overview.

##### Send and consume normal messages

Normal messages are messages that have no special features in ApsaraMQ for RocketMQ. They are different from featured messages, such as scheduled messages, delayed messages, ordered messages, and transactional messages. This topic provides sample code to show how to use the HTTP client SDK for Java to send and consume normal messages.

**Prerequisites**

The following operations are performed: Install the SDK for Java. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send normal messages**

The following sample code provides an example on how to send normal messages:

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQProducer; import com.aliyun.mq.http.model.TopicMessage; import java.util.Date; public class Producer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
                // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
                "${HTTP_ENDPOINT}",
                // The AccessKey ID that is used for identity verification. You can
obtain the AccessKey ID in the Apsara Uni-manager Operations Console.
                "${ACCESS_KEY}",
                // The AccessKey secret that is used for identity verification. You can
obtain the AccessKey secret in the Apsara Uni-manager Operations Console. "${SECRETKEY}"
```

```
                "${SECRET_KEY}"
```

);

```
        // The topic to which you want to send messages. The topic is created in the Ap
saraMQ for RocketMQ console.
        // Each topic can be used to send and consume messages of a specific type. For
example, a topic that is used to send and consume normal messages cannot be used to sen d and consume messages of other types.
        final String topic = "${TOPIC}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        final String instanceId = "${INSTANCE_ID}";
        // Obtain the producer that sends messages to the topic.
        MQProducer producer;
        if (instanceId != null && instanceId != "") {
            producer = mqClient.getProducer(instanceId, topic);
        } else {
            producer = mqClient.getProducer(topic);
        }  try {
            // Cyclically send four messages.
            for (int i = 0; i < 4; i++) {
                TopicMessage pubMsg;        // The normal message.
                pubMsg = new TopicMessage(
                // The content of the message.
                "hello mq!".getBytes(),
                // The tag of the message.
                "A"
```

);

```java
                // The custom property of the message.
                pubMsg.getProperties().put("a", String.valueOf(i));
                // The key of the message.
                pubMsg.setMessageKey("MessageKey");
            // Send the message in synchronous mode. If no exception is thrown, the
message is sent.
            TopicMessage pubResultMsg = producer.publishMessage(pubMsg);
            // Send the message in synchronous mode. If no exception is thrown, the
message is sent.
            System.out.println(new Date() + " Send mq message success. Topic is:" +
topic + ", msgId is: " + pubResultMsg.getMessageId()
                        + ", bodyMD5 is: " + pubResultMsg.getMessageBodyMD5());
        } catch (Throwable e) {
            // Specify the logic that you want to use to resend or persist the message
if the message fails to be sent and needs to be sent again.
            System.out.println(new Date() + " Send mq message failed. Topic is:" +
topic);
            e.printStackTrace();
```

```
        mqClient.close();
```

**Consume normal messages**

The following sample code provides an example on how to consume normal messages:

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQConsumer; import com.aliyun.mq.http.common.AckMessageException; import com.aliyun.mq.http.model.Message; import java.util.ArrayList; import java.util.List; public class Consumer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
                // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
                "${HTTP_ENDPOINT}",
                // The AccessKey ID that is used for identity verification. You can
obtain the AccessKey ID in the Apsara Uni-manager Operations Console.
                "${ACCESS_KEY}",
                // The AccessKey secret that is used for identity verification. You can
obtain the AccessKey secret in the Apsara Uni-manager Operations Console.
                "${SECRET_KEY}"
```

);

```
        // The topic from which you want to consume messages. The topic is created in t
he ApsaraMQ for RocketMQ console.
        // Each topic can be used to send and consume messages of a specific type. For
example, a topic that is used to send and consume normal messages cannot be used to sen d and consume messages of other types.
        final String topic = "${TOPIC}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        final String groupId = "${GROUP_ID}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        final String instanceId = "${INSTANCE_ID}";
        final MQConsumer consumer;
        if (instanceId != null && instanceId != "") {
            consumer = mqClient.getConsumer(instanceId, topic, groupId, null);
```

```
cosue
```

`qC`

```
et.getCosue( staced,topc,goupd,
```

`u` );

```
        } else {
            consumer = mqClient.getConsumer(topic, groupId);
        // Cyclically consume messages in the current thread. We recommend that you use
multiple threads to concurrently consume messages.
        do {
            List<Message> messages = null;
            try {
                // Consume messages in long polling mode.
                // In long polling mode, if no message in the topic is available for con
sumption, the request is suspended on the broker for a specified period of time. If a m essage becomes available for consumption within this period, the broker immediately sen ds a response to the consumer. In this example, the period is set to 3 seconds.
                messages = consumer.consumeMessage(
                        3,// The maximum number of messages that can be consumed at a ti
me. In this example, the value is set to 3. The maximum value that you can specify is 1
```

6. `

```
                        3// The length of a long polling period. Unit: seconds. In this
example, the value is set to 3. The maximum value that you can specify is 30.
```

);

```java
            } catch (Throwable e) {
                e.printStackTrace();
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e1) {
                    e1.printStackTrace();
            // No messages in the topic are available for consumption.
            if (messages == null || messages.isEmpty()) {
                System.out.println(Thread.currentThread().getName() + ": no new message,
continue!");
                continue;
            // Specify the message consumption logic.
            for (Message message : messages) {
                System.out.println("Receive message: " + message);
            // If the broker does not receive an acknowledgment (ACK) for a message
from the consumer before the delivery retry interval elapses, the broker delivers the message for consumption again.
            // A unique timestamp is specified for the handle of a message each time th
e message is consumed.
```

`{`

```
                List<String> handles = new ArrayList<String>();
                for (Message message : messages) {
                    handles.add(message.getReceiptHandle());
                try {
```

```java
                    consumer.ackMessage(handles);
                } catch (Throwable e) {
                    // If the handle of a message times out, the broker cannot receive a
n ACK for the message from the consumer.
                    if (e instanceof AckMessageException) {
                        AckMessageException errors = (AckMessageException) e;
                        System.out.println("Ack message fail, requestId is:" +
errors.getRequestId() + ", fail handles:");
                        if (errors.getErrorMessages() != null) {
                            for (String errorHandle :errors.getErrorMessages().keySet())
```

`{`

```java
                                System.out.println("Handle:" + errorHandle + ",
ErrorCode:" + errors.getErrorMessages().get(errorHandle).getErrorCode()
                                        + ", ErrorMsg:" +
errors.getErrorMessages().get(errorHandle).getErrorMessage());
                        continue;
                    e.printStackTrace();
        } while (true);
```

##### Send and consume ordered messages

Ordered messages are a type of message that is published and consumed in a strict order. Ordered messages in ApsaraMQ for RocketMQ are also known as first-in-first-out (FIFO) messages. This topic provides sample code to show how to use the HTTP client SDK for Java to send and consume ordered messages.

**Background information**

Ordered messages are classified into the following types: Globally ordered message: All messages in a specified topic are published and consumed in first-in-first-out (FIFO) order. Partitionally ordered message: All messages in a specified topic are distributed to different partitions by using shard keys. The messages in each partition are published and consumed in FIFO order. A Sharding Key is a key field that is used for ordered messages to identify different partitions. The Sharding Key is different from the key of a normal message. For more information about the message routing feature, see Ordered messages.

**Prerequisites**

The following operations are performed: Install the SDK for Java. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send ordered messages**

The following sample code provides an example on how to send ordered messages:

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQProducer; import com.aliyun.mq.http.model.TopicMessage; import java.util.Date; public class OrderProducer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
                // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
                "${HTTP_ENDPOINT}",
                // The AccessKey ID that is used for identity verification. You can
obtain the AccessKey ID in the Apsara Uni-manager Operations Console.
                "${ACCESS_KEY}",
                // The AccessKey secret that is used for identity verification. You can
obtain the AccessKey secret in the Apsara Uni-manager Operations Console.
                "${SECRET_KEY}"
```

);

```
        // The topic to which you want to send messages. The topic is created in the Ap
saraMQ for RocketMQ console.
        // Each topic can be used to send and consume messages of a specific type. For
example, a topic that is used to send and consume normal messages cannot be used to sen d and consume messages of other types.
        final String topic = "${TOPIC}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        final String instanceId = "${INSTANCE_ID}";
        // Obtain the producer that sends messages to the topic.
        MQProducer producer;
        if (instanceId != null && instanceId != "") {
            producer = mqClient.getProducer(instanceId, topic);
        } else {
            producer = mqClient.getProducer(topic);
        try {
            // Cyclically send eight messages.
            for (int i = 0; i < 8; i++) {
                TopicMessage pubMsg = new TopicMessage(
                        // The content of the message.
```

`g`

```
                        "hello mq!".getBytes(),
                        // The tag of the message.
                        "A"
```

);

```java
                // The shard key that is used to distribute ordered messages to a specif
ic partition. Shard keys can be used to identify different partitions. A shard key is d ifferent from a message key.
                pubMsg.setShardingKey(String.valueOf(i % 2));
                pubMsg.getProperties().put("a", String.valueOf(i));
                // Send the message in synchronous mode. If no exception is thrown, the
message is sent.
                TopicMessage pubResultMsg = producer.publishMessage(pubMsg);
                // Send the message in synchronous mode. If no exception is thrown, the
message is sent.
                System.out.println(new Date() + " Send mq message success. Topic is:" +
topic + ", msgId is: " + pubResultMsg.getMessageId()
                        + ", bodyMD5 is: " + pubResultMsg.getMessageBodyMD5());
        } catch (Throwable e) {
            // Specify the logic that you want to use to resend or persist the message
if the message fails to be sent and needs to be sent again.
            System.out.println(new Date() + " Send mq message failed. Topic is:" +
topic);
            e.printStackTrace();
        mqClient.close();
```

**Consume ordered messages**

The following sample code provides an example on how to consume ordered messages:

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQConsumer; import com.aliyun.mq.http.common.AckMessageException; import com.aliyun.mq.http.model.Message; import java.util.ArrayList; import java.util.List; public class OrderConsumer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
                // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
                "${HTTP_ENDPOINT}",
                // The AccessKey ID that is used for identity verification. You can
```

```
obtain the AccessKey ID in the Apsara Uni-manager Operations Console.
                "${ACCESS_KEY}",
                // The AccessKey secret that is used for identity verification. You can
obtain the AccessKey secret in the Apsara Uni-manager Operations Console.
                "${SECRET_KEY}"
```

);

```
        // The topic from which you want to consume messages. The topic is created in t
he ApsaraMQ for RocketMQ console.
        // Each topic can be used to send and consume messages of a specific type. For
example, a topic that is used to send and consume normal messages cannot be used to sen d and consume messages of other types.
        final String topic = "${TOPIC}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        final String groupId = "${GROUP_ID}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        final String instanceId = "${INSTANCE_ID}";
        final MQConsumer consumer;
        if (instanceId != null && instanceId != "") {
            consumer = mqClient.getConsumer(instanceId, topic, groupId, null);
        } else {
            consumer = mqClient.getConsumer(topic, groupId);
        // Cyclically consume messages in the current thread. We recommend that you use
multiple threads to concurrently consume messages.
        do {
            List<Message> messages = null;
            try {
                // Consume messages in long polling mode. The consumer may pull
partitionally ordered messages from multiple partitions. The consumer consumes messages from the same partition in the order in which the messages are sent.
                // A consumer pulls partitionally ordered messages from a partition. If
the broker does not receive an acknowledgment (ACK) for a message after the message is consumed, the consumer consumes the message again.
                // The consumer can consume the next batch of messages from a partition
only after all messages that are pulled from the partition in the previous batch are ac knowledged to be consumed.
                // In long polling mode, if no message in the topic is available for con
sumption, the request is suspended on the broker for a specified period of time. If a m essage becomes available for consumption within this period, the broker immediately sen ds a response to the consumer. In this example, the period is set to 3 seconds.
                messages = consumer.consumeMessageOrderly(
                        3,  // The maximum number of messages that can be consumed at a
time. In this example, the value is set to 3. The maximum value that you can specify is 16.
                        3   // The length of a long polling period. Unit: seconds. In th
```

```
is example, the value is set to 3. The maximum value that you can specify is 30.
```

);

```java
            } catch (Throwable e) {
                e.printStackTrace();
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e1) {
                    e1.printStackTrace();
            // No messages in the topic are available for consumption.
            if (messages == null || messages.isEmpty()) {
                System.out.println(Thread.currentThread().getName() + ": no new message,
continue!");
                continue;
            // Specify the message consumption logic.
            System.out.println("Receive " + messages.size() + " messages:");
            for (Message message : messages) {
                System.out.println(message);
                System.out.println("ShardingKey: " + message.getShardingKey() + ", a:"
+ message.getProperties().get("a"));
            // If the broker does not receive an ACK for a message from the consumer be
fore the timeout period for a message retry elapses, the broker delivers the message fo r consumption again.
            // A unique timestamp is specified for the handle of a message each time th
e message is consumed.
```

`{`

```java
                List<String> handles = new ArrayList<String>();
                for (Message message : messages) {
                    handles.add(message.getReceiptHandle());
                try {
                    consumer.ackMessage(handles);
                } catch (Throwable e) {
                    // If the handle of a message times out, the broker cannot receive a
n ACK for the message from the consumer.
                    if (e instanceof AckMessageException) {
                        AckMessageException errors = (AckMessageException) e;
                        System.out.println("Ack message fail, requestId is:" +
errors.getRequestId() + ", fail handles:");
                        if (errors.getErrorMessages() != null) {
                            for (String errorHandle :errors.getErrorMessages().keySet())
```

`{`

```java
                                System.out.println("Handle:" + errorHandle + ",
ErrorCode:" + errors.getErrorMessages().get(errorHandle).getErrorCode()
                                        + ", ErrorMsg:" +
errors.getErrorMessages().get(errorHandle).getErrorMessage());
```

`ti`

```
                        continue;
                    e.printStackTrace();
        } while (true);
```

##### Send and consume scheduled messages

**and delayed messages**

This topic provides sample code to show how to use the HTTP client SDK for Java to send and consume scheduled messages and delayed messages.

**Background information**

Delayed message: The producer sends the message to the ApsaraMQ for RocketMQ server, but does not expect the message to be delivered immediately. Instead, the message is delivered to the consumer for consumption after a certain period of time. This message is a delayed message. Scheduled message: A producer sends a message to a ApsaraMQ for RocketMQ broker and expects the message to be delivered to a consumer at a specified point in time. This type of message is called a scheduled message. If an HTTP client SDK is used, the code configurations of scheduled messages are the same as the code configurations of delayed messages. Both types of messages are delivered to consumers after a specific period of time based on the attributes of the messages. For more information about the message routing feature, see Scheduled messages and delayed messages.

**Prerequisites**

The following operations are performed: Install the SDK for Java. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send scheduled messages or delayed messages**

The following sample code provides an example on how to send scheduled messages or delayed messages:

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQProducer; import com.aliyun.mq.http.model.TopicMessage; import java.util.Date; public class Producer { publicstaticvoidmain(String[]args){
```

```
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
                // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
                "${HTTP_ENDPOINT}",
                // The AccessKey ID that is used for identity verification. You can
obtain the AccessKey ID in the Apsara Uni-manager Operations Console.
                "${ACCESS_KEY}",
                // The AccessKey secret that is used for identity verification. You can
obtain the AccessKey secret in the Apsara Uni-manager Operations Console.
                "${SECRET_KEY}"
```

);

```
        // The topic to which you want to send messages. The topic is created in the Ap
saraMQ for RocketMQ console.
        // Each topic can be used to send and consume messages of a specific type. For
example, a topic that is used to send and consume normal messages cannot be used to sen d and consume messages of other types.
        final String topic = "${TOPIC}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        final String instanceId = "${INSTANCE_ID}";
        // Obtain the producer that sends messages to the topic.
        MQProducer producer;
        if (instanceId != null && instanceId != "") {
            producer = mqClient.getProducer(instanceId, topic);
        } else {
            producer = mqClient.getProducer(topic);
        try {
            // Cyclically send four messages.
            for (int i = 0; i < 4; i++) {
                TopicMessage pubMsg;
                pubMsg = new TopicMessage(
                // The content of the message.
                "hello mq!".getBytes(),
                // The tag of the message.
                "A"
```

);

```
                 // The custom property of the message.
                 pubMsg.getProperties().put("a", String.valueOf(i));
                 // The key of the message.
                 pubMsg.setMessageKey("MessageKey");
                 // The period of time after which the broker delivers the message. In
this example, when the broker receives a message, the broker waits for 10 seconds befor e it delivers the message to the consumer. Set this parameter to a timestamp in millise conds.
```

```java
                 // If the producer sends a scheduled message, set the parameter to the
time interval between the scheduled point in time and the current point in time.
                 pubMsg.setStartDeliverTime(System.currentTimeMillis() + 10 * 1000);
             // Send the message in synchronous mode. If no exception is thrown, the
message is sent.
             TopicMessage pubResultMsg = producer.publishMessage(pubMsg);
             // Send the message in synchronous mode. If no exception is thrown, the
message is sent.
             System.out.println(new Date() + " Send mq message success. Topic is:" +
topic + ", msgId is: " + pubResultMsg.getMessageId()
                        + ", bodyMD5 is: " + pubResultMsg.getMessageBodyMD5());
        } catch (Throwable e) {
            // Specify the logic that you want to use to resend or persist the message
if the message fails to be sent and needs to be sent again.
            System.out.println(new Date() + " Send mq message failed. Topic is:" +
topic);
            e.printStackTrace();
        mqClient.close();
```

**Consume scheduled messages or delayed messages**

The following sample code provides an example on how to consume scheduled messages or delayed messages:

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQConsumer; import com.aliyun.mq.http.common.AckMessageException; import com.aliyun.mq.http.model.Message; import java.util.ArrayList; import java.util.List; public class Consumer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
                // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
                "${HTTP_ENDPOINT}",
                // The AccessKey ID that is used for identity verification. You can
obtain the AccessKey ID in the Apsara Uni-manager Operations Console.
                "${ACCESS_KEY}",
                // The AccessKey secret that is used for identity verification. You can
```

```
obtain the AccessKey secret in the Apsara Uni-manager Operations Console.
                "${SECRET_KEY}"
```

);

```
        // The topic from which you want to consume messages. The topic is created in t
he ApsaraMQ for RocketMQ console.
        // Each topic can be used to send and consume messages of a specific type. For
example, a topic that is used to send and consume normal messages cannot be used to sen d and consume messages of other types.
        final String topic = "${TOPIC}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        final String groupId = "${GROUP_ID}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        final String instanceId = "${INSTANCE_ID}";
        final MQConsumer consumer;
        if (instanceId != null && instanceId != "") {
            consumer = mqClient.getConsumer(instanceId, topic, groupId, null);
        } else {
            consumer = mqClient.getConsumer(topic, groupId);
        // Cyclically consume messages in the current thread. We recommend that you use
multiple threads to concurrently consume messages.
        do {
            List<Message> messages = null;
            try {
                // Consume messages in long polling mode.
                // In long polling mode, if no message in the topic is available for con
sumption, the request is suspended on the broker for a specified period of time. If a m essage becomes available for consumption within this period, the broker immediately sen ds a response to the consumer. In this example, the period is set to 3 seconds.
                messages = consumer.consumeMessage(
                        3,// The maximum number of messages that can be consumed at a ti
me. In this example, the value is set to 3. The maximum value that you can specify is 1
```

6. `

```
                        3// The length of a long polling period. Unit: seconds. In this
example, the value is set to 3. The maximum value that you can specify is 30.
```

);

```
            } catch (Throwable e) {
                e.printStackTrace();
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e1) {
                    e1.printStackTrace();
            // No messages in the topic are available for consumption.
```

```java
            if (messages == null || messages.isEmpty()) {
                System.out.println(Thread.currentThread().getName() + ": no new message,
continue!");
                continue;
            // Specify the message consumption logic.
            for (Message message : messages) {
                System.out.println("Receive message: " + message);
            // If the broker does not receive an acknowledgment (ACK) for a message
from the consumer before the delivery retry interval elapses, the broker delivers the message for consumption again.
            // A unique timestamp is specified for the handle of a message each time th
e message is consumed.
```

`{`

```java
                List<String> handles = new ArrayList<String>();
                for (Message message : messages) {
                    handles.add(message.getReceiptHandle());
                try {
                    consumer.ackMessage(handles);
                } catch (Throwable e) {
                    // If the handle of a message times out, the broker cannot receive a
n ACK for the message from the consumer.
                    if (e instanceof AckMessageException) {
                        AckMessageException errors = (AckMessageException) e;
                        System.out.println("Ack message fail, requestId is:" +
errors.getRequestId() + ", fail handles:");
                        if (errors.getErrorMessages() != null) {
                            for (String errorHandle :errors.getErrorMessages().keySet())
```

`{`

```java
                                System.out.println("Handle:" + errorHandle + ",
ErrorCode:" + errors.getErrorMessages().get(errorHandle).getErrorCode()
                                        + ", ErrorMsg:" +
errors.getErrorMessages().get(errorHandle).getErrorMessage());
                        continue;
                    e.printStackTrace();
        } while (true);
```

##### Send and consume transactional messages

ApsaraMQ for RocketMQ provides a distributed transaction processing feature that is similar to X/Open XA. ApsaraMQ for RocketMQ uses transactional messages to ensure transactional consistency. This topic provides sample code to show how to use the HTTP client SDK for Java to send and consume transactional messages.

**Background information**

The following figure shows the interaction process of transactional messages. For more information about the message routing feature, see Transactional messages.

**Prerequisites**

The following operations are performed: Install the SDK for Java. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send transactional messages**

The following sample code provides an example on how to send transactional messages:

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQTransProducer; import com.aliyun.mq.http.common.AckMessageException; import com.aliyun.mq.http.model.Message; import com.aliyun.mq.http.model.TopicMessage; import java.util.List; public class TransProducer {
    static void processCommitRollError(Throwable e) {
        if (e instanceof AckMessageException) {
            AckMessageException errors = (AckMessageException) e;
            System.out.println("Commit/Roll transaction error, requestId is:" +
errors.getRequestId() + ", fail handles:");
            if (errors.getErrorMessages() != null) {
                for (String errorHandle :errors.getErrorMessages().keySet()) {
                    System.out.println("Handle:" + errorHandle + ", ErrorCode:" + errors
.getErrorMessages().get(errorHandle).getErrorCode()
```

```
                            + ", ErrorMsg:" +
errors.getErrorMessages().get(errorHandle).getErrorMessage());
    public static void main(String[] args) throws Throwable {
        MQClient mqClient = new MQClient(
                // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
                "${HTTP_ENDPOINT}",
                // The AccessKey ID that is used for identity verification. You can
obtain the AccessKey ID in the Apsara Uni-manager Operations Console.
                "${ACCESS_KEY}",
                // The AccessKey secret that is used for identity verification. You can
obtain the AccessKey secret in the Apsara Uni-manager Operations Console.
                "${SECRET_KEY}"
```

);

```
        // The topic to which you want to send messages. The topic is created in the Ap
saraMQ for RocketMQ console.
        // Each topic can be used to send and consume messages of a specific type. For
example, a topic that is used to send and consume normal messages cannot be used to sen d and consume messages of other types.
        final String topic = "${TOPIC}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        final String instanceId = "${INSTANCE_ID}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        final String groupId = "${GROUP_ID}";
        final MQTransProducer mqTransProducer = mqClient.getTransProducer(instanceId, t
opic, groupId);
        for (int i = 0; i < 4; i++) {
            TopicMessage topicMessage = new TopicMessage();
            topicMessage.setMessageBody("trans_msg");
            topicMessage.setMessageTag("a");
            topicMessage.setMessageKey(String.valueOf(System.currentTimeMillis()));
            // The time interval between the time when the transactional message is
sent and the start time of the first transaction status check. Unit: seconds. Valid val ues: 10 to 300.
            // If the message is not committed or rolled back after the first
transaction status check is performed, the broker initiates a request to check the stat us of the local transaction at an interval of 10 seconds within the next 24 hours.
            topicMessage.setTransCheckImmunityTime(10);
            topicMessage.getProperties().put("a", String.valueOf(i));
```

```java
            TopicMessage pubResultMsg = null;
            pubResultMsg = mqTransProducer.publishMessage(topicMessage);
            System.out.println("Send---->msgId is: " + pubResultMsg.getMessageId()
                    + ", bodyMD5 is: " + pubResultMsg.getMessageBodyMD5()
                    + ", Handle: " + pubResultMsg.getReceiptHandle()
```

);

```java
            if (pubResultMsg != null && pubResultMsg.getReceiptHandle() != null) {
                if (i == 0) {
                    // After the producer sends the transactional message, the broker ob
tains the handle of the half message that corresponds to the transactional message and commits or rolls back the transactional message based on the status of the handle.
                    try {
                        mqTransProducer.commit(pubResultMsg.getReceiptHandle());
                        System.out.println(String.format("MessageId:%s, commit", pubResu
ltMsg.getMessageId()));
                    } catch (Throwable e) {
                        // If the transactional message is not committed or rolled back
before the period of time specified by the TransCheckImmunityTime parameter for the han dle of the transactional message elapses, the commit or rollback operation fails.
                        if (e instanceof AckMessageException) {
                            processCommitRollError(e);
                            continue;
        // The client needs a thread or a process to process unacknowledged
transactional messages.
        // Start a thread to process unacknowledged transactional messages.
        Thread t = new Thread(new Runnable() {
            public void run() {
                int count = 0;
                while(true) {
                    try {
                        if (count == 3) {
                            break;
                        List<Message> messages = mqTransProducer.consumeHalfMessage(3, 3
```

);

```java
                        if (messages == null) {
                            System.out.println("No Half message!");
                            continue;
                        System.out.println(String.format("Half----
>MessageId:%s,Properties:%s,Body:%s,Latency:%d",
                                messages.get(0).getMessageId(),
                                messages.get(0).getProperties(),
                                messages.get(0).getMessageBodyString(),
                                System.currentTimeMillis() -
messages.get(0).getPublishTime())); for(Messagemessage:messages){
```

```java
                        for (Message message : messages) {
                            try {
                                if (Integer.valueOf(message.getProperties().get("a")) ==
1) {
                                    // Confirm to commit the transactional message.
                                    mqTransProducer.commit(message.getReceiptHandle());
                                    count++;
                                    System.out.println(String.format("MessageId:%s, commi
t", message.getMessageId()));
                                } else if
(Integer.valueOf(message.getProperties().get("a")) == 2
                                        && message.getConsumedTimes() > 1) {
                                    // Confirm to commit the transactional message.
                                    mqTransProducer.commit(message.getReceiptHandle());
                                    count++;
                                    System.out.println(String.format("MessageId:%s, commi
t", message.getMessageId()));
                                } else if
(Integer.valueOf(message.getProperties().get("a")) == 3) {
                                    // Confirm to roll back the transactional message.
                                    mqTransProducer.rollback(message.getReceiptHandle());
                                    count++;
                                    System.out.println(String.format("MessageId:%s, rollb
ack", message.getMessageId()));
                                } else {
                                    // Do not perform operations. Check the status next
time.
                                    System.out.println(String.format("MessageId:%s, unkno
wn", message.getMessageId()));
                            } catch (Throwable e) {
                                // If the transactional message is not committed or
rolled back before the timeout period specified by the TransCheckImmunityTime parameter for the handle of the transactional message elapses or before the timeout period specif ied for the handle of consumeHalfMessage elapses, the commit or rollback operation fail s. In this example, the timeout period for the handle of consumeHalfMessage is 10 secon ds.
                                processCommitRollError(e);
                    } catch (Throwable e) {
                        System.out.println(e.getMessage());
        });
        t.start();
        t.join();
        mqClient.close();
```

**Consume transactional messages**

The following sample code provides an example on how to consume transactional messages:

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQConsumer; import com.aliyun.mq.http.common.AckMessageException; import com.aliyun.mq.http.model.Message; import java.util.ArrayList; import java.util.List; public class Consumer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
                // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
                "${HTTP_ENDPOINT}",
                // The AccessKey ID that is used for identity verification. You can
obtain the AccessKey ID in the Apsara Uni-manager Operations Console.
                "${ACCESS_KEY}",
                // The AccessKey secret that is used for identity verification. You can
obtain the AccessKey secret in the Apsara Uni-manager Operations Console.
                "${SECRET_KEY}"
```

);

```
        // The topic from which you want to consume messages. The topic is created in t
he ApsaraMQ for RocketMQ console.
        // Each topic can be used to send and consume messages of a specific type. For
example, a topic that is used to send and consume normal messages cannot be used to sen d and consume messages of other types.
        final String topic = "${TOPIC}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        final String groupId = "${GROUP_ID}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        final String instanceId = "${INSTANCE_ID}";
        final MQConsumer consumer;
        if (instanceId != null && instanceId != "") {
            consumer = mqClient.getConsumer(instanceId, topic, groupId, null);
        } else {
            consumer = mqClient.getConsumer(topic, groupId);
        // Cyclically consume messages in the current thread. We recommend that you use
```

```
multiple threads to concurrently consume messages.
        do {
            List<Message> messages = null;
            try {
                // Consume messages in long polling mode.
                // In long polling mode, if no message in the topic is available for con
sumption, the request is suspended on the broker for a specified period of time. If a m essage becomes available for consumption within this period, the broker immediately sen ds a response to the consumer. In this example, the period is set to 3 seconds.
                messages = consumer.consumeMessage(
                        3,// The maximum number of messages that can be consumed at a ti
me. In this example, the value is set to 3. The maximum value that you can specify is 1
```

6. `

```
                        3// The length of a long polling period. Unit: seconds. In this
example, the value is set to 3. The maximum value that you can specify is 30.
```

);

```java
            } catch (Throwable e) {
                e.printStackTrace();
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e1) {
                    e1.printStackTrace();
            // No messages in the topic are available for consumption.
            if (messages == null || messages.isEmpty()) {
                System.out.println(Thread.currentThread().getName() + ": no new message,
continue!");
                continue;
            // Specify the message consumption logic.
            for (Message message : messages) {
                System.out.println("Receive message: " + message);
            // If the broker does not receive an acknowledgment (ACK) for a message
from the consumer before the delivery retry interval elapses, the broker delivers the message for consumption again.
            // A unique timestamp is specified for the handle of a message each time th
e message is consumed.
```

`{`

```
                List<String> handles = new ArrayList<String>();
                for (Message message : messages) {
                    handles.add(message.getReceiptHandle());
                try {
                    consumer.ackMessage(handles);
                } catch (Throwable e) {
                    // If the handle of a message times out, the broker cannot receive a
n ACK for the message from the consumer.
                    if (e instanceof AckMessageException) {
```

```java
                        AckMessageException errors = (AckMessageException) e;
                        System.out.println("Ack message fail, requestId is:" +
errors.getRequestId() + ", fail handles:");
                        if (errors.getErrorMessages() != null) {
                            for (String errorHandle :errors.getErrorMessages().keySet())
```

`{`

```java
                                System.out.println("Handle:" + errorHandle + ",
ErrorCode:" + errors.getErrorMessages().get(errorHandle).getErrorCode()
                                        + ", ErrorMsg:" +
errors.getErrorMessages().get(errorHandle).getErrorMessage());
                        continue;
                    e.printStackTrace();
        } while (true);
```

#### Go SDK

##### Prepare the environment

This topic describes how to prepare the environment before you use the HTTP client SDK for Go to send and consume messages.

**Environment requirements**

Go is installed. For more information, see Installing Go from source. After Go is installed, you can run the `go version` command to check the version of Go that you installed.

**Install the SDK for Go**

1. Run the following command to enable Go Modules: For more information about Go Modules,
see Go Modules Reference.

```
go env -w GO111MODULE=on
```

2. Run the following command to configure a Go Modules proxy:

```
go env -w GOPROXY=https://goproxy.cn,direct
```

3. Run the following command to initialize Go Modules and generate the go.mod file:

```
go mod init
```

4. Run the following command to install the SDK for Go:

```
go get github.com/aliyunmq/mq-http-go-sdk
```

##### Send and consume normal messages

Normal messages are messages that have no special features in ApsaraMQ for RocketMQ. They are different from featured messages, such as scheduled messages, delayed messages, ordered messages, and transactional messages. This topic provides sample code to show how to use the HTTP client SDK for Go to send and consume normal messages.

**Prerequisites**

The following operations are performed: Install the SDK for Go. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send normal messages**

The following sample code provides an example on how to send normal messages:

```java
package main import (
    "fmt"
    "time"
    "strconv"
    "github.com/aliyunmq/mq-http-go-sdk"
```

`)`

```
func main() {
    // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the console. In the left-side navigation pane, click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Man agement tab.
    endpoint := "${HTTP_ENDPOINT}"
    // The AccessKey ID that is used for identity verification. You can obtain the Acce
ssKey ID in the Apsara Uni-manager Operations Console.
    accessKey := "${ACCESS_KEY}"
    // The AccessKey secret that is used for identity verification. You can obtain the
AccessKey secret in the Apsara Uni-manager Operations Console.
    secretKey := "${SECRET_KEY}"
    // The topic to which you want to send messages. The topic is created in the Apsara
MQ for RocketMQ console.
    topic := "${TOPIC}"
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    instanceId := "${INSTANCE_ID}"
    client := mq_http_sdk.NewAliyunMQClient(endpoint, accessKey, secretKey, "")
```

```
    mqProducer := client.GetProducer(instanceId, topic)
    // Cyclically send four messages.
    for i := 0; i < 4; i++ {
        var msg mq_http_sdk.PublishMessageRequest
        msg = mq_http_sdk.PublishMessageRequest{
        MessageBody: "hello mq!",         // The content of the message.
        MessageTag:  "",                  // The tag of the message.
        Properties:  map[string]string{}, // The properties of the message.
        // The key of the message.
        msg.MessageKey = "MessageKey"
        // The custom property of the message.
        msg.Properties["a"] = strconv.Itoa(i)
        ret, err := mqProducer.PublishMessage(msg)
        if err != nil {
            fmt.Println(err)
            return
        } else {
            fmt.Printf("Publish ---->\n\tMessageId:%s, BodyMD5:%s, \n", ret.MessageId,
ret.MessageBodyMD5)
        time.Sleep(time.Duration(100) * time.Millisecond)
```

**Consume normal messages**

The following sample code provides an example on how to consume normal messages:

```java
package main import (
    "fmt"
    "github.com/gogap/errors"
    "strings"
    "time"
    "github.com/aliyunmq/mq-http-go-sdk"
```

`)`

```
func main() {
    // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
    endpoint := "${HTTP_ENDPOINT}"
    // The AccessKey ID that is used for identity verification. You can obtain the Acce
ssKey ID in the Apsara Uni-manager Operations Console.
    accessKey := "${ACCESS_KEY}"
    // The AccessKey secret that is used for identity verification. You can obtain the
AccessKey secret in the Apsara Uni-manager Operations Console.
```

```
    secretKey := "${SECRET_KEY}"
    // The topic from which you want to consume messages. The topic is created in the A
psaraMQ for RocketMQ console.
    // Each topic can be used to send and consume messages of a specific type. For exam
ple, a topic that is used to send and consume normal messages cannot be used to send an d consume messages of other types.
    topic := "${TOPIC}"
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    instanceId := "${INSTANCE_ID}"
    // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
    groupId := "${GROUP_ID}"
    client := mq_http_sdk.NewAliyunMQClient(endpoint, accessKey, secretKey, "")
    mqConsumer := client.GetConsumer(instanceId, topic, groupId, "")
    for {
        endChan := make(chan int)
        respChan := make(chan mq_http_sdk.ConsumeMessageResponse)
        errChan := make(chan error)
        go func() {
            select {
            case resp := <-respChan:
```

`{`

```json
                    // Specify the message consumption logic.
                    var handles []string
                    fmt.Printf("Consume %d messages---->\n", len(resp.Messages))
                    for _, v := range resp.Messages {
                        handles = append(handles, v.ReceiptHandle)
                        fmt.Printf("\tMessageID: %s, PublishTime: %d, MessageTag: %s\n"+
                            "\tConsumedTimes: %d, FirstConsumeTime: %d, NextConsumeTime:
%d\n"+
                            "\tBody: %s\n"+
                            "\tProps: %s\n",
                            v.MessageId, v.PublishTime, v.MessageTag, v.ConsumedTimes,
                            v.FirstConsumeTime, v.NextConsumeTime, v.MessageBody,
v.Properties)
                    // If the broker does not receive an acknowledgment (ACK) for a mess
age from the consumer before the period of time specified by the NextConsumeTime parame ter elapses, the broker delivers the message for consumption again.
                    // A unique timestamp is specified for the handle of a message each
time the message is consumed.
                    ackerr := mqConsumer.AckMessage(handles)
                    if ackerr != nil {
                        // If the handle of a message times out, the broker cannot recei
ve an ACK for the message from the consumer.
                        fmt.Println(ackerr)
                        if errAckItems, ok := ackerr.(errors.ErrCode).Context()
["Dtil"]([] htt dkE AkIt
```

`)` `k``{`

```json
["Detail"].([]mq_http_sdk.ErrAckItem); ok {
                           for _, errAckItem := range errAckItems {
                             fmt.Printf("\tErrorHandle:%s, ErrorCode:%s, ErrorMsg:%s\n",
                               errAckItem.ErrorHandle, errAckItem.ErrorCode,
errAckItem.ErrorMsg)
                        } else {
                           fmt.Println("ack err =", ackerr)
                        time.Sleep(time.Duration(3) * time.Second)
                    } else {
                        fmt.Printf("Ack ---->\n\t%s\n", handles)
                    endChan <- 1
            case err := <-errChan:
```

`{`

```
                    // No messages in the topic are available for consumption.
                    if strings.Contains(err.(errors.ErrCode).Error(), "MessageNotExist")
```

`{`

```
                        fmt.Println("\nNo new message, continue!")
                    } else {
                        fmt.Println(err)
                        time.Sleep(time.Duration(3) * time.Second)
                    endChan <- 1
            case <-time.After(35 * time.Second):
```

`{`

```
                    fmt.Println("Timeout of consumer message ??")
                    endChan <- 1
        }()
        // In long polling mode, the default network timeout period is 35 seconds.
        // In long polling mode, if no message in the topic is available for
consumption, the request is suspended on the broker for a specified period of time. If a message becomes available for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
        mqConsumer.ConsumeMessage(respChan, errChan,
            3, // The maximum number of messages that can be consumed at a time. In
this example, the value is set to 3. The maximum value that you can specify is 16.
            3, // The length of a long polling period. Unit: seconds. In this example,
the value is set to 3. The maximum value that you can specify is 30.
```

`)`

```
        <-endChan
```

##### Send and consume ordered messages

Ordered messages are a type of message that is published and consumed in a strict order. Ordered messages in ApsaraMQ for RocketMQ are also known as first-in-first-out (FIFO) messages. This topic provides sample code to show how to use the HTTP client SDK for Go to send and consume ordered messages.

**Background information**

Ordered messages are classified into the following types: Globally ordered message: All messages in a specified topic are published and consumed in first-in-first-out (FIFO) order. Partitionally ordered message: All messages in a specified topic are distributed to different partitions by using shard keys. The messages in each partition are published and consumed in FIFO order. A Sharding Key is a key field that is used for ordered messages to identify different partitions. The Sharding Key is different from the key of a normal message. For more information about the message routing feature, see Ordered messages.

**Prerequisites**

The following operations are performed: Install the SDK for Go. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send ordered messages**

The following sample code provides an example on how to send ordered messages:

```java
package main import (
    "fmt"
    "time"
    "strconv"
    "github.com/aliyunmq/mq-http-go-sdk"
```

`)`

```
func main() {
    // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
    endpoint := "${HTTP_ENDPOINT}"
    // The AccessKey ID that is used for identity verification. You can obtain the Acce
ssKey ID in the Apsara Uni-manager Operations Console.
    accessKey := "${ACCESS_KEY}"
    // The AccessKey secret that is used for identity verification. You can obtain the
AccessKey secret in the Apsara Uni-manager Operations Console.
    secretKey := "${SECRET_KEY}"
    // The topic to which you want to send messages. The topic is created in the Apsara
MQ for RocketMQ console.
    topic := "${TOPIC}"
```

`p` ${

```
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    instanceId := "${INSTANCE_ID}"
    client := mq_http_sdk.NewAliyunMQClient(endpoint, accessKey, secretKey, "")
    mqProducer := client.GetProducer(instanceId, topic)
    // Cyclically send eight messages.
    for i := 0; i < 8; i++ {
        msg := mq_http_sdk.PublishMessageRequest{
            MessageBody: "hello mq!",         // The content of the message.
            MessageTag:  "",                  // The tag of the message.
            Properties:  map[string]string{}, // The properties of the message.
        // The key of the message.
        msg.MessageKey = "MessageKey"
        // The custom property of the message.
        msg.Properties["a"] = strconv.Itoa(i)
        // The shard key that is used to distribute ordered messages to a specific part
ition. Shard keys can be used to identify different partitions. A shard key is differen t from a message key.
        msg.ShardingKey = strconv.Itoa(i % 2)
        ret, err := mqProducer.PublishMessage(msg)
        if err != nil {
            fmt.Println(err)
            return
        } else {
            fmt.Printf("Publish ---->\n\tMessageId:%s, BodyMD5:%s, \n", ret.MessageId,
ret.MessageBodyMD5)
        time.Sleep(time.Duration(100) * time.Millisecond)
```

**Consume ordered messages**

The following sample code provides an example on how to consume ordered messages:

```java
package main import (
    "fmt"
    "github.com/gogap/errors"
    "strings"
    "time"
    "github.com/aliyunmq/mq-http-go-sdk"
```

`)`

```
func main() {
```

```
    // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
    endpoint := "${HTTP_ENDPOINT}"
    // The AccessKey ID that is used for identity verification. You can obtain the Acce
ssKey ID in the Apsara Uni-manager Operations Console.
    accessKey := "${ACCESS_KEY}"
    // The AccessKey secret that is used for identity verification. You can obtain the
AccessKey secret in the Apsara Uni-manager Operations Console.
    secretKey := "${SECRET_KEY}"
    // The topic from which you want to consume messages. The topic is created in the A
psaraMQ for RocketMQ console.
    topic := "${TOPIC}"
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    instanceId := "${INSTANCE_ID}"
    // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
    groupId := "${GROUP_ID}"
    client := mq_http_sdk.NewAliyunMQClient(endpoint, accessKey, secretKey, "")
    mqConsumer := client.GetConsumer(instanceId, topic, groupId, "")
    for {
        endChan := make(chan int)
        respChan := make(chan mq_http_sdk.ConsumeMessageResponse)
        errChan := make(chan error)
        go func() {
            select {
            case resp := <-respChan:
```

`{`

```
                    // Specify the message consumption logic.
                    var handles []string
                    fmt.Printf("Consume %d messages---->\n", len(resp.Messages))
                    for _, v := range resp.Messages {
                        handles = append(handles, v.ReceiptHandle)
                        fmt.Printf("\tMessageID: %s, PublishTime: %d, MessageTag: %s\n"+
                            "\tConsumedTimes: %d, FirstConsumeTime: %d, NextConsumeTime:
%d\n"+
                            "\tBody: %s\n"+
                            "\tProps: %s\n"+
                            "\tShardingKey: %s\n",
                            v.MessageId, v.PublishTime, v.MessageTag, v.ConsumedTimes,
                            v.FirstConsumeTime, v.NextConsumeTime, v.MessageBody,
v.Properties, v.ShardingKey)
                    // If the broker does not receive an acknowledgment (ACK) for a mess
age from the consumer before the period of time specified by the NextConsumeTime parame ter elapses, the broker delivers the message for consumption again.
```

```json
                    // A unique timestamp is specified for the handle of a message each
time the message is consumed.
                    ackerr := mqConsumer.AckMessage(handles)
                    if ackerr != nil {
                        // If the handle of a message times out, the broker cannot recei
ve an ACK for the message from the consumer.
                        fmt.Println(ackerr)
                        if errAckItems, ok := ackerr.(errors.ErrCode).Context()
["Detail"].([]mq_http_sdk.ErrAckItem); ok {
                           for _, errAckItem := range errAckItems {
                              fmt.Printf("\tErrorHandle:%s, ErrorCode:%s,
ErrorMsg:%s\n",
                                 errAckItem.ErrorHandle, errAckItem.ErrorCode,
errAckItem.ErrorMsg)
                        } else {
                           fmt.Println("ack err =", ackerr)
                        time.Sleep(time.Duration(3) * time.Second)
                    } else {
                        fmt.Printf("Ack ---->\n\t%s\n", handles)
                    endChan <- 1
            case err := <-errChan:
```

`{`

```
                    // No messages in the topic are available for consumption.
                    if strings.Contains(err.(errors.ErrCode).Error(), "MessageNotExist")
```

`{`

```
                        fmt.Println("\nNo new message, continue!")
                    } else {
                        fmt.Println(err)
                        time.Sleep(time.Duration(3) * time.Second)
                    endChan <- 1
            case <-time.After(35 * time.Second):
```

`{`

```
                    fmt.Println("Timeout of consumer message ??")
                    endChan <- 1
        }()
                // The consumer may pull partitionally ordered messages from multiple
partitions. The consumer consumes the messages in each partition in the order in which the messages are sent.
                // A consumer pulls partitionally ordered messages from a partition. If
the broker does not receive an ACK for a message after the message is consumed, the con sumer consumes the message again.
                // The consumer can consume the next batch of messages from a partition
only after all messages that are pulled from the partition in the previous batch are ac knowledged to be consumed. //I
```

`l`

```
lli
```

`d` `th` `d``f` `lt` `t`

```
kti
```

`t`

```
idi
```

`d`

```
                // In long polling mode, the default network timeout period is 35 second
```

`s.`

```
                // In long polling mode, if no message in the topic is available for con
sumption, the request is suspended on the broker for a specified period of time. If a m essage becomes available for consumption within this period, the broker immediately sen ds a response to the consumer. In this example, the period is set to 3 seconds.
        mqConsumer.ConsumeMessageOrderly(respChan, errChan,
            3, // The maximum number of messages that can be consumed at a time. In
this example, the value is set to 3. The maximum value that you can specify is 16.
            3, // The length of a long polling period. Unit: seconds. In this example,
the value is set to 3. The maximum value that you can specify is 30.
```

`)`

```
        <-endChan
```

##### Send and consume scheduled messages

**and delayed messages**

This topic provides sample code to show how to use the HTTP client SDK for Go to send and consume scheduled messages and delayed messages.

**Background information**

Delayed message: The producer sends the message to the ApsaraMQ for RocketMQ server, but does not expect the message to be delivered immediately. Instead, the message is delivered to the consumer for consumption after a certain period of time. This message is a delayed message. Scheduled message: A producer sends a message to a ApsaraMQ for RocketMQ broker and expects the message to be delivered to a consumer at a specified point in time. This type of message is called a scheduled message. If an HTTP client SDK is used, the code configurations of scheduled messages are the same as the code configurations of delayed messages. Both types of messages are delivered to consumers after a specific period of time based on the attributes of the messages. For more information about the message routing feature, see Scheduled messages and delayed messages.

**Prerequisites**

The following operations are performed: Install the SDK for Go. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send scheduled messages or delayed messages**

The following sample code provides an example on how to send scheduled messages or delayed messages:

```java
package main
```

```java
import (
    "fmt"
    "time"
    "strconv"
    "github.com/aliyunmq/mq-http-go-sdk"
```

`)`

```
func main() {
    // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
    endpoint := "${HTTP_ENDPOINT}"
    // The AccessKey ID that is used for identity verification. You can obtain the Acce
ssKey ID in the Apsara Uni-manager Operations Console.
    accessKey := "${ACCESS_KEY}"
    // The AccessKey secret that is used for identity verification. You can obtain the
AccessKey secret in the Apsara Uni-manager Operations Console.
    secretKey := "${SECRET_KEY}"
    // The topic to which you want to send messages. The topic is created in the Apsara
MQ for RocketMQ console.
    topic := "${TOPIC}"
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    instanceId := "${INSTANCE_ID}"
    client := mq_http_sdk.NewAliyunMQClient(endpoint, accessKey, secretKey, "")
    mqProducer := client.GetProducer(instanceId, topic)
    // Cyclically send four messages.
    for i := 0; i < 4; i++ {
        var msg mq_http_sdk.PublishMessageRequest
            msg = mq_http_sdk.PublishMessageRequest{
            MessageBody: "hello mq!",         // The content of the message.
            MessageTag:  "",                  // The tag of the message.
            Properties:  map[string]string{}, // The properties of the message.
    // The key of the message.
            msg.MessageKey = "MessageKey"
            // The custom property of the message.
            msg.Properties["a"] = strconv.Itoa(i)
            // The period of time after which the broker delivers the message. In this
example, when the broker receives a message, the broker waits for 10 seconds before it delivers the message to the consumer. Set this parameter to a timestamp in milliseconds
```

`.`

```
            // If the producer sends a scheduled message, set the parameter to the time
interval between the scheduled point in time and the current point in time. msg.StartDeliverTime=time.Now().UTC().Unix()*1000+10*1000
```

```
sg.State
```

`e` `e` `t`

```
e.ow().UC().U
```

`()`

```
        ret, err := mqProducer.PublishMessage(msg)
        if err != nil {
            fmt.Println(err)
            return
        } else {
            fmt.Printf("Publish ---->\n\tMessageId:%s, BodyMD5:%s, \n", ret.MessageId,
ret.MessageBodyMD5)
        time.Sleep(time.Duration(100) * time.Millisecond)
```

**Consume scheduled messages or delayed messages**

The following sample code provides an example on how to consume scheduled messages or delayed messages:

```java
package main import (
    "fmt"
    "github.com/gogap/errors"
    "strings"
    "time"
    "github.com/aliyunmq/mq-http-go-sdk"
```

`)`

```
func main() {
    // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
    endpoint := "${HTTP_ENDPOINT}"
    // The AccessKey ID that is used for identity verification. You can obtain the Acce
ssKey ID in the Apsara Uni-manager Operations Console.
    accessKey := "${ACCESS_KEY}"
    // The AccessKey secret that is used for identity verification. You can obtain the
AccessKey secret in the Apsara Uni-manager Operations Console.
    secretKey := "${SECRET_KEY}"
    // The topic from which you want to consume messages. The topic is created in the A
psaraMQ for RocketMQ console.
    // Each topic can be used to send and consume messages of a specific type. For exam
ple, a topic that is used to send and consume normal messages cannot be used to send an d consume messages of other types.
    topic := "${TOPIC}"
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    instanceId := "${INSTANCE_ID}"
```

```
    // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
    groupId := "${GROUP_ID}"
    client := mq_http_sdk.NewAliyunMQClient(endpoint, accessKey, secretKey, "")
    mqConsumer := client.GetConsumer(instanceId, topic, groupId, "")
    for {
        endChan := make(chan int)
        respChan := make(chan mq_http_sdk.ConsumeMessageResponse)
        errChan := make(chan error)
        go func() {
            select {
            case resp := <-respChan:
```

`{`

```json
                    // Specify the message consumption logic.
                    var handles []string
                    fmt.Printf("Consume %d messages---->\n", len(resp.Messages))
                    for _, v := range resp.Messages {
                        handles = append(handles, v.ReceiptHandle)
                        fmt.Printf("\tMessageID: %s, PublishTime: %d, MessageTag: %s\n"+
                            "\tConsumedTimes: %d, FirstConsumeTime: %d, NextConsumeTime:
%d\n"+
                            "\tBody: %s\n"+
                            "\tProps: %s\n",
                            v.MessageId, v.PublishTime, v.MessageTag, v.ConsumedTimes,
                            v.FirstConsumeTime, v.NextConsumeTime, v.MessageBody,
v.Properties)
                    // If the broker does not receive an acknowledgment (ACK) for a mess
age from the consumer before the period of time specified by the NextConsumeTime parame ter elapses, the broker delivers the message for consumption again.
                    // A unique timestamp is specified for the handle of a message each
time the message is consumed.
                    ackerr := mqConsumer.AckMessage(handles)
                    if ackerr != nil {
                        // If the handle of a message times out, the broker cannot recei
ve an ACK for the message from the consumer.
                        fmt.Println(ackerr)
                        if errAckItems, ok := ackerr.(errors.ErrCode).Context()
["Detail"].([]mq_http_sdk.ErrAckItem); ok {
                           for _, errAckItem := range errAckItems {
                             fmt.Printf("\tErrorHandle:%s, ErrorCode:%s, ErrorMsg:%s\n",
                               errAckItem.ErrorHandle, errAckItem.ErrorCode,
errAckItem.ErrorMsg)
                        } else {
                           fmt.Println("ack err =", ackerr)
                        time.Sleep(time.Duration(3) * time.Second)
                    } else {
                        fmt.Printf("Ack ---->\n\t%s\n", handles)
```

```
                    endChan <- 1
            case err := <-errChan:
```

`{`

```
                    // No messages in the topic are available for consumption.
                    if strings.Contains(err.(errors.ErrCode).Error(), "MessageNotExist")
```

`{`

```
                        fmt.Println("\nNo new message, continue!")
                    } else {
                        fmt.Println(err)
                        time.Sleep(time.Duration(3) * time.Second)
                    endChan <- 1
            case <-time.After(35 * time.Second):
```

`{`

```
                    fmt.Println("Timeout of consumer message ??")
                    endChan <- 1
        }()
        // In long polling mode, the default network timeout period is 35 seconds.
        // In long polling mode, if no message in the topic is available for
consumption, the request is suspended on the broker for a specified period of time. If a message becomes available for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
        mqConsumer.ConsumeMessage(respChan, errChan,
            3, // The maximum number of messages that can be consumed at a time. In
this example, the value is set to 3. The maximum value that you can specify is 16.
            3, // The length of a long polling period. Unit: seconds. In this example,
the value is set to 3. The maximum value that you can specify is 30.
```

`)`

```
        <-endChan
```

##### Send and consume transactional messages

ApsaraMQ for RocketMQ provides a distributed transaction processing feature that is similar to X/Open XA. ApsaraMQ for RocketMQ uses transactional messages to ensure transactional consistency. This topic provides sample code to show how to use the HTTP client SDK for Go to send and consume transactional messages.

**Background information**

The following figure shows the interaction process of transactional messages. For more information about the message routing feature, see Transactional messages.

**Prerequisites**

The following operations are performed: Install the SDK for Go. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send transactional messages**

The following sample code provides an example on how to send transactional messages:

```java
package main import (
    "fmt"
    "github.com/gogap/errors"
    "strconv"
    "strings"
    "time"
    "github.com/aliyunmq/mq-http-go-sdk"
```

`)`

```
var loopCount = 0 func ProcessError(err error) {
    // If a transactional message is not committed or rolled back before the timeout pe
riod specified by the TransCheckImmunityTime parameter for the handle of the transactio nal message elapses or before the timeout period specified for the handle of consumeHal fMessage elapses, the commit or rollback operation fails. In this example, the timeout period for the handle of consumeHalfMessage is 10 seconds.
    if err == nil {
        return
    fmt.Println(err)
    for _, errAckItem := range err.(errors.ErrCode).Context()["Detail"].
([]mq_http_sdk.ErrAckItem) {
```

```
        fmt.Printf("\tErrorHandle:%s, ErrorCode:%s, ErrorMsg:%s\n",
            errAckItem.ErrorHandle, errAckItem.ErrorCode, errAckItem.ErrorMsg)
func ConsumeHalfMsg(mqTransProducer *mq_http_sdk.MQTransProducer) {
    for {
        if loopCount >= 10 {
            return
        loopCount++
        endChan := make(chan int)
        respChan := make(chan mq_http_sdk.ConsumeMessageResponse)
        errChan := make(chan error)
        go func() {
            select {
            case resp := <-respChan:
```

`{`

```
                    // Specify the business processing logic.
                    var handles []string
                    fmt.Printf("Consume %d messages---->\n", len(resp.Messages))
                    for _, v := range resp.Messages {
                        handles = append(handles, v.ReceiptHandle)
                        fmt.Printf("\tMessageID: %s, PublishTime: %d, MessageTag: %s\n"+
                            "\tConsumedTimes: %d, FirstConsumeTime: %d, NextConsumeTime:
%d\n\tBody: %s\n"+
                            "\tProperties:%s, Key:%s, Timer:%d, Trans:%d\n",
                            v.MessageId, v.PublishTime, v.MessageTag, v.ConsumedTimes,
                            v.FirstConsumeTime, v.NextConsumeTime, v.MessageBody,
                            v.Properties, v.MessageKey, v.StartDeliverTime,
v.TransCheckImmunityTime)
                        a, _ := strconv.Atoi(v.Properties["a"])
                        var comRollErr error
                        if a == 1 {
                            // Confirm to commit the transactional message.
                            comRollErr = (*mqTransProducer).Commit(v.ReceiptHandle)
                            fmt.Println("Commit---------->")
                        } else if a == 2 && v.ConsumedTimes > 1 {
                            // Confirm to commit the transactional message.
                            comRollErr = (*mqTransProducer).Commit(v.ReceiptHandle)
                            fmt.Println("Commit---------->")
                        } else if a == 3 {
                            // Confirm to roll back the transactional message.
                            comRollErr = (*mqTransProducer).Rollback(v.ReceiptHandle)
                            fmt.Println("Rollback---------->")
                        } else {
                            // Do not perform operations. Check the status next time.
                            fmt.Println("Unknown---------->")
                        ProcessError(comRollErr)
                    endChan <- 1
caseerr <errChan
```

```
            case err := <-errChan:
```

`{`

```
                    // No messages in the topic are available for consumption.
                    if strings.Contains(err.(errors.ErrCode).Error(), "MessageNotExist")
```

`{`

```
                        fmt.Println("\nNo new message, continue!")
                    } else {
                        fmt.Println(err)
                        time.Sleep(time.Duration(3) * time.Second)
                    endChan <- 1
            case <-time.After(35 * time.Second):
```

`{`

```
                    fmt.Println("Timeout of consumer message ??")
                    return
        }()
        // Check the status of half messages in long polling mode.
        // In long polling mode, if no message in the topic is available for
consumption, the request is suspended on the broker for a specified period of time. If a message becomes available for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
        (*mqTransProducer).ConsumeHalfMessage(respChan, errChan,
            3, // The maximum number of messages that can be consumed at a time. In
this example, the value is set to 3. The maximum value that you can specify is 16.
            3, // The length of a long polling period. Unit: seconds. In this example,
the value is set to 3. The maximum value that you can specify is 30.
```

`)`

```
        <-endChan
func main() {
    // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
    endpoint := "${HTTP_ENDPOINT}"
    // The AccessKey ID that is used for identity verification. You can obtain the Acce
ssKey ID in the Apsara Uni-manager Operations Console.
    accessKey := "${ACCESS_KEY}"
    // The AccessKey secret that is used for identity verification. You can obtain the
AccessKey secret in the Apsara Uni-manager Operations Console.
    secretKey := "${SECRET_KEY}"
    // The topic to which you want to send messages. The topic is created in the Apsara
MQ for RocketMQ console.
    // Each topic can be used to send and consume messages of a specific type. For exam
ple, a topic that is used to send and consume normal messages cannot be used to send an d consume messages of other types.
    topic := "${TOPIC}"
    // The ID of the instance to which the topic belongs. The instance is created in th
eApsaraMQforRocketMQconsole
```

```
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    instanceId := "${INSTANCE_ID}"
    // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
    groupId := "${GROUP_ID}"
    client := mq_http_sdk.NewAliyunMQClient(endpoint, accessKey, secretKey, "")
    mqTransProducer := client.GetTransProducer(instanceId, topic, groupId)
    // The client needs a thread or a process to process unacknowledged transactional m
essages.
    // Start a goroutine to process unacknowledged transactional messages.
    go ConsumeHalfMsg(&mqTransProducer)
    // Send four transactional messages. Commit one message after the message is sent.
Check the status of the half messages that correspond to the other three transactional messages after the three messages are sent.
    for i := 0; i < 4; i++ {
        msg := mq_http_sdk.PublishMessageRequest{
            MessageBody:"I am transaction msg!",
            Properties: map[string]string{"a":strconv.Itoa(i)},
        // The time interval between the time when the transactional message is sent an
d the start time of the first transaction status check. Unit: seconds. Valid values: 10 to 300.
        // If the message is not committed or rolled back after the first transaction s
tatus check is performed, the broker initiates a request to check the status of the loc al transaction at an interval of 10 seconds within the next 24 hours.
        msg.TransCheckImmunityTime = 10
        resp, pubErr := mqTransProducer.PublishMessage(msg)
        if pubErr != nil {
            fmt.Println(pubErr)
            return
        fmt.Printf("Publish ---->\n\tMessageId:%s, BodyMD5:%s, Handle:%s\n",
            resp.MessageId, resp.MessageBodyMD5, resp.ReceiptHandle)
        if i == 0 {
            // After the producer sends the transactional message, the broker obtains t
he handle of the half message that corresponds to the transactional message and commits or rolls back the transactional message based on the status of the handle.
            ackErr := mqTransProducer.Commit(resp.ReceiptHandle)
            fmt.Println("Commit---------->")
            ProcessError(ackErr)
    for ; loopCount < 10 ; {
        time.Sleep(time.Duration(1) * time.Second)
```

**Consume transactional messages**

The following sample code provides an example on how to consume transactional messages:

```java
package main import (
    "fmt"
    "github.com/gogap/errors"
    "strings"
    "time"
    "github.com/aliyunmq/mq-http-go-sdk"
```

`)`

```
func main() {
    // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
    endpoint := "${HTTP_ENDPOINT}"
    // The AccessKey ID that is used for identity verification. You can obtain the Acce
ssKey ID in the Apsara Uni-manager Operations Console.
    accessKey := "${ACCESS_KEY}"
    // The AccessKey secret that is used for identity verification. You can obtain the
AccessKey secret in the Apsara Uni-manager Operations Console.
    secretKey := "${SECRET_KEY}"
    // The topic from which you want to consume messages. The topic is created in the A
psaraMQ for RocketMQ console.
    // Each topic can be used to send and consume messages of a specific type. For exam
ple, a topic that is used to send and consume normal messages cannot be used to send an d consume messages of other types.
    topic := "${TOPIC}"
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    instanceId := "${INSTANCE_ID}"
    // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
    groupId := "${GROUP_ID}"
    client := mq_http_sdk.NewAliyunMQClient(endpoint, accessKey, secretKey, "")
    mqConsumer := client.GetConsumer(instanceId, topic, groupId, "")
    for {
        endChan := make(chan int)
        respChan := make(chan mq_http_sdk.ConsumeMessageResponse)
        errChan := make(chan error)
        go func() {
            select {
            case resp := <-respChan:
```

`{`

```
                    // Specify the message consumption logic.
```

`p` `y` `g` `p` `g`

```json
                    var handles []string
                    fmt.Printf("Consume %d messages---->\n", len(resp.Messages))
                    for _, v := range resp.Messages {
                        handles = append(handles, v.ReceiptHandle)
                        fmt.Printf("\tMessageID: %s, PublishTime: %d, MessageTag: %s\n"+
                            "\tConsumedTimes: %d, FirstConsumeTime: %d, NextConsumeTime:
%d\n"+
                            "\tBody: %s\n"+
                            "\tProps: %s\n",
                            v.MessageId, v.PublishTime, v.MessageTag, v.ConsumedTimes,
                            v.FirstConsumeTime, v.NextConsumeTime, v.MessageBody,
v.Properties)
                    // If the broker does not receive an acknowledgment (ACK) for a mess
age from the consumer before the period of time specified by the NextConsumeTime parame ter elapses, the broker delivers the message for consumption again.
                    // A unique timestamp is specified for the handle of a message each
time the message is consumed.
                    ackerr := mqConsumer.AckMessage(handles)
                    if ackerr != nil {
                        // If the handle of a message times out, the broker cannot recei
ve an ACK for the message from the consumer.
                        fmt.Println(ackerr)
                        if errAckItems, ok := ackerr.(errors.ErrCode).Context()
["Detail"].([]mq_http_sdk.ErrAckItem); ok {
                           for _, errAckItem := range errAckItems {
                             fmt.Printf("\tErrorHandle:%s, ErrorCode:%s, ErrorMsg:%s\n",
                               errAckItem.ErrorHandle, errAckItem.ErrorCode,
errAckItem.ErrorMsg)
                        } else {
                           fmt.Println("ack err =", ackerr)
                        time.Sleep(time.Duration(3) * time.Second)
                    } else {
                        fmt.Printf("Ack ---->\n\t%s\n", handles)
                    endChan <- 1
            case err := <-errChan:
```

`{`

```
                    // No messages in the topic are available for consumption.
                    if strings.Contains(err.(errors.ErrCode).Error(), "MessageNotExist")
```

`{`

```
                        fmt.Println("\nNo new message, continue!")
                    } else {
                        fmt.Println(err)
                        time.Sleep(time.Duration(3) * time.Second)
                    endChan <- 1
            case <-time.After(35 * time.Second):
```

`{`

```
                    fmt.Println("Timeout of consumer message ??")
                    endChan <- 1
        }()
        // In long polling mode, the default network timeout period is 35 seconds.
        // In long polling mode, if no message in the topic is available for
consumption, the request is suspended on the broker for a specified period of time. If a message becomes available for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
        mqConsumer.ConsumeMessage(respChan, errChan,
            3, // The maximum number of messages that can be consumed at a time. In
this example, the value is set to 3. The maximum value that you can specify is 16.
            3, // The length of a long polling period. Unit: seconds. In this example,
the value is set to 3. The maximum value that you can specify is 30.
```

`)`

```
        <-endChan
```

#### Python SDK

##### Prepare the environment

This topic describes how to prepare the environment before you use the HTTP client SDK for Python to send and consume messages.

**Environment requirements**

Install Python. For more information, visit the official website of Python. You must install an appropriate version of Python based on the following instructions: If the version of your SDK is V1.0.0, make sure that the version of Python you installed is 2.5 or is later than 2.5 but earlier than 3.0. If the version of your SDK is later than V1.0.0, make sure that the version of Python you installed is 2.5 or later. The pip tool is installed. For more information, see Install pip.

**Note**

The pip tool is provided in Python 3.4 or later by default. If the version of Python you installed is 3.4 or later, you do not need to install the pip tool. After Python is installed, you can run the `python -V` command to view the version of Python that you installed.

**Install the SDK for Python**

Run the following command to install the SDK for Python:

```
pip install mq_http_sdk
```

##### Send and consume normal messages

Normal messages are messages that have no special features in ApsaraMQ for RocketMQ. They are different from featured messages, such as scheduled messages, delayed messages, ordered messages, and transactional messages. This topic provides sample code to show how to use the HTTP client SDK for Python to send and consume normal messages.

**Prerequisites**

The following operations are performed: Install the SDK for Python. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send normal messages**

The following sample code provides an example on how to send normal messages:

```java
import sys from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_producer import * from mq_http_sdk.mq_client import * import time
# Initialize a producer client.
mq_client = MQClient(
    # The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
     "${HTTP_ENDPOINT}",
    # The AccessKey ID that is used for identity verification. You can obtain the Acces
sKey ID in the Apsara Uni-manager Operations Console.
     "${ACCESS_KEY}",
    # The AccessKey secret that is used for identity verification. You can obtain the A
ccessKey secret in the Apsara Uni-manager Operations Console.
    "${SECRET_KEY}"
```

`)`

```bash
# The topic to which you want to send messages. The topic is created in the ApsaraMQ fo
r RocketMQ console. topic_name = "${TOPIC}"
# The ID of the instance to which the topic belongs. The instance is created in the Aps
araMQ for RocketMQ console.
# If the instance has a namespace, specify the ID of the instance. If the instance does
not have a namespace, set the instance ID to null or an empty string. You can check whe ther your instance has a namespace on the Instances page in the RocketMQ console. instance_id = "${INSTANCE_ID}" producer = mq_client.get_producer(instance_id, topic_name)
# Cyclically send four messages.
```

```python
msg_count = 4 print("%sPublish Message To %s\nTopicName:%s\nMessageCount:%s\n" % (10 * "=", 10 * "=", topic_name, msg_count)) try:
    for i in range(msg_count):
            msg = TopicMessage(
                    # The content of the message.
                    "I am test message %s.hello" % i,
                    # The tag of the message.
                    "tag %s" % i
```

`)`

```python
            # The custom property of the message.
            msg.put_property("a", "i")
            # The key of the message.
            msg.set_message_key("MessageKey")
            re_msg = producer.publish_message(msg)
            print("Publish Message Succeed. MessageID:%s, BodyMD5:%s" %
(re_msg.message_id, re_msg.message_body_md5)) except MQExceptionBase as e:
    if e.type == "TopicNotExist":
         print("Topic not exist, please create it.")
         sys.exit(1)
    print("Publish Message Fail. Exception:%s" % e)
```

**Consume normal messages**

The following sample code provides an example on how to consume normal messages:

```bash
from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_consumer import * from mq_http_sdk.mq_client import *
# Initialize a consumer client.
mq_client = MQClient(
    # The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
    "${HTTP_ENDPOINT}",
    # The AccessKey ID that is used for identity verification. You can obtain the Acces
sKey ID in the Apsara Uni-manager Operations Console.
    "${ACCESS_KEY}",
    # The AccessKey secret that is used for identity verification. You can obtain the A
ccessKey secret in the Apsara Uni-manager Operations Console.
    "${SECRET_KEY}"
```

`)`

```bash
# The topic from which you want to consume messages. The topic is created in the Apsara
MQ for RocketMQ console. topic_name = "${TOPIC}"
# The ID of the group that you created in the ApsaraMQ for RocketMQ console.
group_id = "${GROUP_ID}"
# The ID of the instance to which the topic belongs. The instance is created in the Aps
```

```python
araMQ for RocketMQ console.
# If the instance has a namespace, specify the ID of the instance. If the instance does
not have a namespace, set the instance ID to null or an empty string. You can check whe ther your instance has a namespace on the Instances page in the RocketMQ console. instance_id = "${INSTANCE_ID}" consumer = mq_client.get_consumer(instance_id, topic_name, group_id)
# In long polling mode, if no message in the topic is available for consumption, the re
quest is suspended on the broker for a specified period of time. If a message becomes a vailable for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
# The length of a long polling period. Unit: seconds. In this example, the value is set
to 3. The maximum value that you can specify is 30. wait_seconds = 3
# The maximum number of messages that can be consumed at a time. In this example, the v
alue is set to 3. The maximum value that you can specify is 16. batch = 3 print(("%sConsume And Ak Message From Topic%s\nTopicName:%s\nMQConsumer:%s\nWaitSeconds:%s\n" \
        % (10 * "=", 10 * "=", topic_name, group_id, wait_seconds)))
while True:
    try:
        # Consume messages in long polling mode.
        recv_msgs = consumer.consume_message(batch, wait_seconds)
        for msg in recv_msgs:
            print(("Receive, MessageId: %s\nMessageBodyMD5: %s \
                              \nMessageTag: %s\nConsumedTimes: %s \
                              \nPublishTime: %s\nBody: %s \
                              \nNextConsumeTime: %s \
                              \nReceiptHandle: %s \
                              \nProperties: %s\n" % \
                  (msg.message_id, msg.message_body_md5,
                   msg.message_tag, msg.consumed_times,
                   msg.publish_time, msg.message_body,
                   msg.next_consume_time, msg.receipt_handle, msg.properties)))
            print(msg.get_property(""))
    except MQExceptionBase as e:
        # No messages in the topic are available for consumption.
        if e.type == "MessageNotExist":
            print(("No new message! RequestId: %s" % e.req_id))
            continue
        print(("Consume Message Fail! Exception:%s\n" % e))
        time.sleep(2)
        continue
    # If the broker does not receive an acknowledgment (ACK) for a message from the con
sumer before the period of time specified by the msg.next_consume_time parameter elapse s, the broker delivers the message for consumption again.
    # A unique timestamp is specified for the handle of a message each time the message
is consumed.
    try:
        receipt_handle_list = [msg.receipt_handle for msg in recv_msgs]
```

`k` `(`

```
ith
```

`dl`

```
lit)
```

```python
        consumer.ack_message(receipt_handle_list)
        print(("Ak %s Message Succeed.\n\n" % len(receipt_handle_list)))
    except MQExceptionBase as e:
        print(("\nAk Message Fail! Exception:%s" % e))
        # If the handle of a message times out, the broker cannot receive an ACK for th
e message from the consumer.
        if e.sub_errors:
            for sub_error in e.sub_errors:
                print(("\tErrorHandle:%s,ErrorCode:%s,ErrorMsg:%s" % \
                      (sub_error["ReceiptHandle"], sub_error["ErrorCode"],
sub_error["ErrorMessage"])))
```

##### Send and consume ordered messages

Ordered messages are a type of message that is published and consumed in a strict order. Ordered messages in ApsaraMQ for RocketMQ are also known as first-in-first-out (FIFO) messages. This topic provides sample code to show how to use the HTTP client SDK for Python to send and consume ordered messages.

**Background information**

Ordered messages are classified into the following types: Globally ordered message: All messages in a specified topic are published and consumed in first-in-first-out (FIFO) order. Partitionally ordered message: All messages in a specified topic are distributed to different partitions by using shard keys. The messages in each partition are published and consumed in FIFO order. A Sharding Key is a key field that is used for ordered messages to identify different partitions. The Sharding Key is different from the key of a normal message. For more information about the message routing feature, see Ordered messages.

**Prerequisites**

The following operations are performed: Install the SDK for Python. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send ordered messages**

The following sample code provides an example on how to send ordered messages:

```java
import sys from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_producer import * from mq_http_sdk.mq_client import *
# Initialize a producer client.
mq_client = MQClient(
    # The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces OntheInstancespage,selectthenameofyourinstance Then,viewtheHTTPendpo
```

```bash
ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
     "${HTTP_ENDPOINT}",
    # The AccessKey ID that is used for identity verification. You can obtain the Acces
sKey ID in the Apsara Uni-manager Operations Console.
     "${ACCESS_KEY}",
    # The AccessKey secret that is used for identity verification. You can obtain the A
ccessKey secret in the Apsara Uni-manager Operations Console.
    "${SECRET_KEY}"
```

`)`

```python
# The topic to which you want to send messages. The topic is created in the ApsaraMQ fo
r RocketMQ console. topic_name = "${TOPIC}"
# The ID of the instance to which the topic belongs. The instance is created in the Aps
araMQ for RocketMQ console.
# If the instance has a namespace, specify the ID of the instance. If the instance does
not have a namespace, set the instance ID to null or an empty string. You can check whe ther your instance has a namespace on the Instances page in the RocketMQ console. instance_id = "${INSTANCE_ID}" producer = mq_client.get_producer(instance_id, topic_name)
# Cyclically send eight messages.
msg_count = 8 print("%sPublish Message To %s\nTopicName:%s\nMessageCount:%s\n" % (10 * "=", 10 * "=", topic_name, msg_count)) try:
    for i in range(msg_count):
        msg = TopicMessage(
            # The content of the message.
            "I am test message %s.hello" % i,
            # The tag of the message.
            "tag %s" % i
```

`)`

```python
        # The custom property of the message.
        msg.put_property("a", str(i))
        # The shard key that is used to distribute ordered messages to a specific parti
tion. Shard keys can be used to identify different partitions. A shard key is different from a message key.
        msg.set_sharding_key(str(i % 3))
        re_msg = producer.publish_message(msg)
        print("Publish Message Succeed. MessageID:%s, BodyMD5:%s" % (re_msg.message_id,
re_msg.message_body_md5)) except MQExceptionBase as e:
    if e.type == "TopicNotExist":
        print("Topic not exist, please create it.")
        sys.exit(1)
    print("Publish Message Fail. Exception:%s" % e)
```

**Consume ordered messages**

The following sample code provides an example on how to consume ordered messages:

```bash
from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_consumer import * from mq_http_sdk.mq_client import *
# Initialize a consumer client.
mq_client = MQClient(
    # The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
     "${HTTP_ENDPOINT}",
    # The AccessKey ID that is used for identity verification. You can obtain the Acces
sKey ID in the Apsara Uni-manager Operations Console.
     "${ACCESS_KEY}",
    # The AccessKey secret that is used for identity verification. You can obtain the A
ccessKey secret in the Apsara Uni-manager Operations Console.
    "${SECRET_KEY}"
```

`)`

```python
# The topic from which you want to consume messages. The topic is created in the Apsara
MQ for RocketMQ console. topic_name = "${TOPIC}"
# The ID of the group that you created in the ApsaraMQ for RocketMQ console.
group_id = "${GROUP_ID}"
# The ID of the instance to which the topic belongs. The instance is created in the Aps
araMQ for RocketMQ console.
# If the instance has a namespace, specify the ID of the instance. If the instance does
not have a namespace, set the instance ID to null or an empty string. You can check whe ther your instance has a namespace on the Instances page in the RocketMQ console. instance_id = "${INSTANCE_ID}" consumer = mq_client.get_consumer(instance_id, topic_name, group_id)
# Consume messages in long polling mode. The consumer may pull partitionally ordered me
ssages from multiple partitions. The consumer consumes the messages in the same partiti on in the order in which the messages are sent.
# A consumer pulls partitionally ordered messages from a partition. If the broker does
not receive an acknowledgment (ACK) for a message after the message is consumed, the co nsumer consumes the message again.
# The consumer can consume the next batch of messages from a partition only after all t
he messages that are pulled from the partition in the previous batch are acknowledged t o be consumed.
# In long polling mode, if no message in the topic is available for consumption, the re
quest is suspended on the broker for a specified period of time. If a message becomes a vailable for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds. wait_seconds = 3
# The maximum number of messages that can be consumed at a time. In this example, the v
alue is set to 3. The maximum value that you can specify is 16. batch = 3 print(("%sConsume And Ak Message From Topic%s\nTopicName:%s\nMQConsumer:%s\nWaitSeconds:%s\n" \
        % (10 * "=", 10 * "=", topic_name, group_id, wait_seconds)))
while True:
    try:
        recv_msgs = consumer.consume_message_orderly(batch, wait_seconds)
```

```python
        print("=======>Receive %d messages:" % len(recv_msgs))
        for msg in recv_msgs:
            print("\tMessageId: %s, MessageBodyMD5: %s,NextConsumeTime:
%s,ConsumedTimes: %s,PublishTime: %s\n\tBody: %s \
                    \n\tReceiptHandle: %s \
                    \n\tProperties: %s,ShardingKey: %s\n" % \
                  (msg.message_id, msg.message_body_md5,
                   msg.next_consume_time, msg.consumed_times,
                   msg.publish_time, msg.message_body,
                   msg.receipt_handle, msg.properties, msg.get_sharding_key()))
    except MQExceptionBase as e:
        if e.type == "MessageNotExist":
            print(("No new message! RequestId: %s" % e.req_id))
            continue
        print(("Consume Message Fail! Exception:%s\n" % e))
        time.sleep(2)
        continue
    # If the broker does not receive an ACK for a message from the consumer before the
period of time specified by the msg.next_consume_time parameter elapses, the broker del ivers the message for consumption again.
    # A unique timestamp is specified for the handle of a message each time the message
is consumed.
    try:
        receipt_handle_list = [msg.receipt_handle for msg in recv_msgs]
        consumer.ack_message(receipt_handle_list)
        print(("========>Ak %s Message Succeed.\n\n" % len(receipt_handle_list)))
    except MQExceptionBase as e:
        print(("\nAk Message Fail! Exception:%s" % e))
        # If the handle of a message times out, the broker cannot receive an ACK for th
e message from the consumer.
        if e.sub_errors:
            for sub_error in e.sub_errors:
                print(("\tErrorHandle:%s,ErrorCode:%s,ErrorMsg:%s" % \
                      (sub_error["ReceiptHandle"], sub_error["ErrorCode"],
sub_error["ErrorMessage"])))
```

##### Send and consume scheduled messages

**and delayed messages**

This topic provides sample code to show how to use the HTTP client SDK for Python to send and consume scheduled messages and delayed messages.

**Background information**

Delayed message: The producer sends the message to the ApsaraMQ for RocketMQ server, but does not expect the message to be delivered immediately. Instead, the message is delivered to the consumer for consumption after a certain period of time. This message is a delayed message. Scheduled message: A producer sends a message to a ApsaraMQ for RocketMQ broker and expects the message to be delivered to a consumer at a specified point in time. This type of message is called a scheduled message. If an HTTP client SDK is used, the code configurations of scheduled messages are the same as the code configurations of delayed messages. Both types of messages are delivered to consumers after a specific period of time based on the attributes of the messages. For more information about the message routing feature, see Scheduled messages and delayed messages.

**Prerequisites**

The following operations are performed: Install the SDK for Python. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send scheduled messages or delayed messages**

The following sample code provides an example on how to send scheduled messages or delayed messages:

```java
import sys from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_producer import * from mq_http_sdk.mq_client import * import time
# Initialize a producer client.
mq_client = MQClient(
    # The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
     "${HTTP_ENDPOINT}",
    # The AccessKey ID that is used for identity verification. You can obtain the Acces
sKey ID in the Apsara Uni-manager Operations Console.
     "${ACCESS_KEY}",
    # The AccessKey secret that is used for identity verification. You can obtain the A
ccessKey secret in the Apsara Uni-manager Operations Console.
    "${SECRET_KEY}"
```

`)`

```bash
# The topic to which you want to send messages. The topic is created in the ApsaraMQ fo
r RocketMQ console. topic_name = "${TOPIC}"
# The ID of the instance to which the topic belongs. The instance is created in the Aps
araMQ for RocketMQ console.
# If the instance has a namespace, specify the ID of the instance. If the instance does
not have a namespace, set the instance ID to null or an empty string. You can check whe ther your instance has a namespace on the Instances page in the RocketMQ console. instance_id = "${INSTANCE_ID}"
```

`d` `li` `t` `t` `d` `(i` `t` `id` `t` `i` `)`

```python
producer = mq_client.get_producer(instance_id, topic_name)
# Cyclically send four messages.
msg_count = 4 print("%sPublish Message To %s\nTopicName:%s\nMessageCount:%s\n" % (10 * "=", 10 * "=", topic_name, msg_count)) try:
    for i in range(msg_count):
            msg = TopicMessage(
            # The content of the message.
            "I am test message %s.hello" % i,
            # The tag of the message.
            "tag1"
```

`)`

```python
            # The property of the message.
            msg.put_property("a", "i")
            # The key of the message.
            msg.set_message_key("MessageKey")
            # The period of time after which the broker delivers the message. In this e
xample, when the broker receives a message, the broker waits for 10 seconds before it d elivers the message to the consumer. Set this parameter to a timestamp in milliseconds.
            # If the producer sends a scheduled message, set the parameter to the time
interval between the scheduled point in time and the current point in time.
            msg.set_start_deliver_time(int(round(time.time() * 1000)) + 10 * 1000)
            re_msg = producer.publish_message(msg)
            print("Publish Timer Message Succeed. MessageID:%s, BodyMD5:%s" %
(re_msg.message_id, re_msg.message_body_md5)) except MQExceptionBase as e:
    if e.type == "TopicNotExist":
        print("Topic not exist, please create it.")
        sys.exit(1)
    print("Publish Message Fail. Exception:%s" % e)
```

**Consume scheduled messages or delayed messages**

The following sample code provides an example on how to consume scheduled messages or delayed messages:

```bash
from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_consumer import * from mq_http_sdk.mq_client import *
# Initialize a consumer client.
mq_client = MQClient(
    # The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
    "${HTTP_ENDPOINT}",
    # The AccessKey ID that is used for identity verification. You can obtain the Acces
sKey ID in the Apsara Uni-manager Operations Console. "${ACCESSKEY}",
```

```bash
    ${ACCESS_KEY},
    # The AccessKey secret that is used for identity verification. You can obtain the A
ccessKey secret in the Apsara Uni-manager Operations Console.
    "${SECRET_KEY}"
```

`)`

```python
# The topic from which you want to consume messages. The topic is created in the Apsara
MQ for RocketMQ console. topic_name = "${TOPIC}"
# The ID of the group that you created in the ApsaraMQ for RocketMQ console.
group_id = "${GROUP_ID}"
# The ID of the instance to which the topic belongs. The instance is created in the Aps
araMQ for RocketMQ console.
# If the instance has a namespace, specify the ID of the instance. If the instance does
not have a namespace, set the instance ID to null or an empty string. You can check whe ther your instance has a namespace on the Instances page in the RocketMQ console. instance_id = "${INSTANCE_ID}" consumer = mq_client.get_consumer(instance_id, topic_name, group_id)
# In long polling mode, if no message in the topic is available for consumption, the re
quest is suspended on the broker for a specified period of time. If a message becomes a vailable for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
# The length of a long polling period. Unit: seconds. In this example, the value is set
to 3. The maximum value that you can specify is 30. wait_seconds = 3
# The maximum number of messages that can be consumed at a time. In this example, the v
alue is set to 3. The maximum value that you can specify is 16. batch = 3 print(("%sConsume And Ak Message From Topic%s\nTopicName:%s\nMQConsumer:%s\nWaitSeconds:%s\n" \
        % (10 * "=", 10 * "=", topic_name, group_id, wait_seconds)))
while True:
    try:
        # Consume messages in long polling mode.
        recv_msgs = consumer.consume_message(batch, wait_seconds)
        for msg in recv_msgs:
            print(("Receive, MessageId: %s\nMessageBodyMD5: %s \
                              \nMessageTag: %s\nConsumedTimes: %s \
                              \nPublishTime: %s\nBody: %s \
                              \nNextConsumeTime: %s \
                              \nReceiptHandle: %s \
                              \nProperties: %s\n" % \
                  (msg.message_id, msg.message_body_md5,
                   msg.message_tag, msg.consumed_times,
                   msg.publish_time, msg.message_body,
                   msg.next_consume_time, msg.receipt_handle, msg.properties)))
            print(msg.get_property(""))
    except MQExceptionBase as e:
        # No messages in the topic are available for consumption.
        if e.type == "MessageNotExist":
            print(("No new message! RequestId: %s" % e.req_id))
            continue
        print(("Consume Message Fail! Exception:%s\n" % e))
```

`p` `g` `p`

```python
        time.sleep(2)
        continue
    # If the broker does not receive an acknowledgment (ACK) for a message from the con
sumer before the period of time specified by the msg.next_consume_time parameter elapse s, the broker delivers the message for consumption again.
    # A unique timestamp is specified for the handle of a message each time the message
is consumed.
    try:
        receipt_handle_list = [msg.receipt_handle for msg in recv_msgs]
        consumer.ack_message(receipt_handle_list)
        print(("Ak %s Message Succeed.\n\n" % len(receipt_handle_list)))
    except MQExceptionBase as e:
        print(("\nAk Message Fail! Exception:%s" % e))
        # If the handle of a message times out, the broker cannot receive an ACK for th
e message from the consumer.
        if e.sub_errors:
            for sub_error in e.sub_errors:
                print(("\tErrorHandle:%s,ErrorCode:%s,ErrorMsg:%s" % \
                      (sub_error["ReceiptHandle"], sub_error["ErrorCode"],
sub_error["ErrorMessage"])))
```

##### Send and consume transactional messages

ApsaraMQ for RocketMQ provides a distributed transaction processing feature that is similar to X/Open XA. ApsaraMQ for RocketMQ uses transactional messages to ensure transactional consistency. This topic provides sample code to show how to use the HTTP client SDK for Python to send and consume transactional messages.

**Background information**

The following figure shows the interaction process of transactional messages. For more information about the message routing feature, see Transactional messages.

**Prerequisites**

The following operations are performed: Install the SDK for Python. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send transactional messages**

The following sample code provides an example on how to send transactional messages:

```java
#!/usr/bin/env python
# coding=utf8
import sys from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_producer import * from mq_http_sdk.mq_client import * import time import threading
# Initialize a producer client.
mq_client = MQClient(
    # The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
     "${HTTP_ENDPOINT}",
    # The AccessKey ID that you created in the Resource Access Management (RAM) console
. The AccessKey ID is used for identity verification.
     "${ACCESS_KEY}",
    # The AccessKey secret that you created in the RAM console. The AccessKey secret is
used for identity verification.
    "${SECRET_KEY}"
```

`)`

```python
# The topic to which you want to send messages. The topic is created in the ApsaraMQ fo
r RocketMQ console. topic_name = "${TOPIC}"
# The ID of the group that you created in the ApsaraMQ for RocketMQ console.
group_id = "${GROUP_ID}"
# The ID of the instance to which the topic belongs. The instance is created in the Aps
araMQ for RocketMQ console.
# If the instance has a namespace, specify the ID of the instance. If the instance does
not have a namespace, set the instance ID to null or an empty string. You can check whe ther your instance has a namespace on the Instances page in the ApsaraMQ for RocketMQ console. instance_id = "${INSTANCE_ID}"
# Cyclically send four transactional messages.
msg_count = 4 print("%sPublish Transaction Message To %s\nTopicName:%s\nMessageCount:%s\n" \
      % (10 * "=", 10 * "=", topic_name, msg_count))
def process_trans_error(exp):
    print("\nCommit/Roll Transaction Message Fail! Exception:%s" % exp)
    # If a transactional message is not committed or rolled back before the timeout per
iod specified by the TransCheckImmunityTime parameter for the handle of the transaction almessageelapsesorbeforethetimeoutperiodspecifiedforthehandleofconsumeHalf
```

```python
al message elapses or before the timeout period specified for the handle of consumeHalf Message elapses, the commit or rollback operation fails. In this example, the timeout p eriod for the handle of consumeHalfMessage is 10 seconds.
    if exp.sub_errors:
        for sub_error in exp.sub_errors:
            print("\tErrorHandle:%s,ErrorCode:%s,ErrorMsg:%s" % \
                  (sub_error["ReceiptHandle"], sub_error["ErrorCode"],
sub_error["ErrorMessage"]))
# The client requires a thread or a process to process unacknowledged transactional mes
sages.
# Start a thread to process unacknowledged transactional messages.
class ConsumeHalfMessageThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.count = 0
        # Create another client.
        self.mq_client = MQClient(
                # The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the endpoint in the HTTP Endpoint section on the Network Management tab.
                "${HTTP_ENDPOINT}",
                # The AccessKey ID that is used for identity verification. You can
obtain the AccessKey ID in the Apsara Uni-manager Operations Console.
                "${ACCESS_KEY}",
                # The AccessKey secret that is used for identity verification. You can
obtain the AccessKey secret in the Apsara Uni-manager Operations Console.
                "${SECRET_KEY}"
```

`)`

```python
        self.trans_producer = self.mq_client.get_trans_producer(instance_id,
topic_name, group_id)
    def run(self):
        while 1:
            if self.count == 3:
                break;
            try:
                half_msgs = self.trans_producer.consume_half_message(1, 3)
                for half_msg in half_msgs:
                    print("Receive Half Message, MessageId: %s\nMessageBodyMD5: %s \
                                                  \nMessageTag: %s\nConsumedTimes: %s \
                                                  \nPublishTime: %s\nBody: %s \
                                                  \nNextConsumeTime: %s \
                                                  \nReceiptHandle: %s \
                                                  \nProperties: %s" % \
                          (half_msg.message_id, half_msg.message_body_md5,
                           half_msg.message_tag, half_msg.consumed_times,
                           half_msg.publish_time, half_msg.message_body,
                           half_msg.next_consume_time, half_msg.receipt_handle,
half_msg.properties))
                a = int(half_msg.get_property("a"))
try:
```

```python
                try:
                    if a == 1:
                        # Confirm to commit the transactional message.
                        self.trans_producer.commit(half_msg.receipt_handle)
                        self.count += 1
                        print("------>commit")
                    elif a == 2 and half_msg.consumed_times > 1:
                        # Confirm to commit the transactional message.
                        self.trans_producer.commit(half_msg.receipt_handle)
                        self.count += 1
                        print("------>commit")
                    elif a == 3:
                        # Confirm to roll back the transactional message.
                        self.trans_producer.rollback(half_msg.receipt_handle)
                        self.count += 1
                        print("------>rollback")
                    else:
                        # Do not perform operations. Check the status next time.
                        print("------>unknown")
                except MQExceptionBase as rec_commit_roll_e:
                    process_trans_error(rec_commit_roll_e)
            except MQExceptionBase as half_e:
                if half_e.type == "MessageNotExist":
                    print("No half message! RequestId: %s" % half_e.req_id)
                    continue
                print("Consume half message Fail! Exception:%s\n" % half_e)
                break
consume_half_thread = ConsumeHalfMessageThread() consume_half_thread.setDaemon(True) consume_half_thread.start() try:
    trans_producer = mq_client.get_trans_producer(instance_id, topic_name, group_id)
    for i in range(msg_count):
        msg = TopicMessage(
            # The content of the message.
            "I am test message %s." % i,
            # The tag of the message.
            "tagA"
```

`)`

```bash
        # The custom property of the message.
        msg.put_property("xy", i)
        # The key of the message.
        msg.set_message_key("MessageKey")
        # The time interval between the time when the transactional message is sent and
the start time of the first transaction status check. Unit: seconds. Valid values: 10 t o 300.
        # If the message is not committed or rolled back after the first transaction st
atus check is performed, the broker initiates a request to check the status of the loca l transaction at an interval of 10 seconds within the next 24 hours.
        msg.set_trans_check_immunity_time(10)
        remsg = transproducer.publishmessage(msg)
```

`_` `_` `_`

```python
        print("Publish Transaction Message Succeed. MessageID:%s, BodyMD5:%s,
Handle:%s" \
              % (re_msg.message_id, re_msg.message_body_md5, re_msg.receipt_handle))
        time.sleep(1)
        if i == 0:
            # After the producer sends the transactional message, the broker obtains th
e handle of the half message that corresponds to the transactional message and commits or rolls back the transactional message based on the status of the handle.
            try:
                trans_producer.commit(re_msg.receipt_handle)
            except MQExceptionBase as pub_commit_roll_e:
                process_trans_error(pub_commit_roll_e)
except MQExceptionBase as pub_e:
    if pub_e.type == "TopicNotExist":
        print("Topic not exist, please create it.")
        sys.exit(1)
    print("Publish Message Fail. Exception:%s" % pub_e)
while 1:
    if not consume_half_thread.is_alive():
        break
    time.sleep(1)
```

**Consume transactional messages**

The following sample code provides an example on how to consume transactional messages:

```bash
from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_consumer import * from mq_http_sdk.mq_client import *
# Initialize a consumer client.
mq_client = MQClient(
    # The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log
on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instan ces. On the Instances page, select the name of your instance. Then, view the HTTP endpo int on the Network Management tab.
    "${HTTP_ENDPOINT}",
    # The AccessKey ID that is used for identity verification. You can obtain the Acces
sKey ID in the Apsara Uni-manager Operations Console.
    "${ACCESS_KEY}",
    # The AccessKey secret that is used for identity verification. You can obtain the A
ccessKey secret in the Apsara Uni-manager Operations Console.
    "${SECRET_KEY}"
```

`)`

```bash
# The topic from which you want to consume messages. The topic is created in the Apsara
MQ for RocketMQ console. topic_name = "${TOPIC}"
# The ID of the group that you created in the ApsaraMQ for RocketMQ console.
group_id = "${GROUP_ID}"
# The ID of the instance to which the topic belongs. The instance is created in the Aps
araMQ for RocketMQ console.
# If the instance has a namespace, specify the ID of the instance. If the instance does
```

```python
not have a namespace, set the instance ID to null or an empty string. You can check whe ther your instance has a namespace on the Instances page in the RocketMQ console. instance_id = "${INSTANCE_ID}" consumer = mq_client.get_consumer(instance_id, topic_name, group_id)
# In long polling mode, if no message in the topic is available for consumption, the re
quest is suspended on the broker for a specified period of time. If a message becomes a vailable for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
# The length of a long polling period. Unit: seconds. In this example, the value is set
to 3. The maximum value that you can specify is 30. wait_seconds = 3
# The maximum number of messages that can be consumed at a time. In this example, the v
alue is set to 3. The maximum value that you can specify is 16. batch = 3 print(("%sConsume And Ak Message From Topic%s\nTopicName:%s\nMQConsumer:%s\nWaitSeconds:%s\n" \
        % (10 * "=", 10 * "=", topic_name, group_id, wait_seconds)))
while True:
    try:
        # Consume messages in long polling mode.
        recv_msgs = consumer.consume_message(batch, wait_seconds)
        for msg in recv_msgs:
            print(("Receive, MessageId: %s\nMessageBodyMD5: %s \
                              \nMessageTag: %s\nConsumedTimes: %s \
                              \nPublishTime: %s\nBody: %s \
                              \nNextConsumeTime: %s \
                              \nReceiptHandle: %s \
                              \nProperties: %s\n" % \
                  (msg.message_id, msg.message_body_md5,
                   msg.message_tag, msg.consumed_times,
                   msg.publish_time, msg.message_body,
                   msg.next_consume_time, msg.receipt_handle, msg.properties)))
            print(msg.get_property(""))
    except MQExceptionBase as e:
        # No messages in the topic are available for consumption.
        if e.type == "MessageNotExist":
            print(("No new message! RequestId: %s" % e.req_id))
            continue
        print(("Consume Message Fail! Exception:%s\n" % e))
        time.sleep(2)
        continue
    # If the broker does not receive an acknowledgment (ACK) for a message from the con
sumer before the period of time specified by the msg.next_consume_time parameter elapse s, the broker delivers the message for consumption again.
    # A unique timestamp is specified for the handle of a message each time the message
is consumed.
    try:
        receipt_handle_list = [msg.receipt_handle for msg in recv_msgs]
        consumer.ack_message(receipt_handle_list)
        print(("Ak %s Message Succeed.\n\n" % len(receipt_handle_list)))
```

```python
    except MQExceptionBase as e:
        print(("\nAk Message Fail! Exception:%s" % e))
        # If the handle of a message times out, the broker cannot receive an ACK for th
e message from the consumer.
        if e.sub_errors:
            for sub_error in e.sub_errors:
                print(("\tErrorHandle:%s,ErrorCode:%s,ErrorMsg:%s" % \
                      (sub_error["ReceiptHandle"], sub_error["ErrorCode"],
sub_error["ErrorMessage"])))
```

#### Node.js SDK

##### Prepare the environment

This topic describes how to prepare the environment before you use the HTTP client SDK for Node.js to send and consume messages.

**Environment requirements**

Node.js 7.6.0 or later is installed. For more information, see Install Node.js. After Node.js is installed, you can run the `node -V` command to view the version of Node.js that you installed.

**Install the SDK for Node.js**

Run the following command to install the SDK for Node.js:

```
npm i @aliyunmq/mq-http-sdk
```

##### Send and consume normal messages

Normal messages are messages that have no special features in ApsaraMQ for RocketMQ. They are different from featured messages, such as scheduled messages, delayed messages, ordered messages, and transactional messages. This topic provides sample code to show how to use the HTTP client SDK for Node.js to send and consume normal messages.

**Prerequisites**

The following operations are performed: SDK for Node.js is installed. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send normal messages**

The following sample code provides an example on how to send normal messages:

```
const {
  MQClient,
  MessageProperties
} = require('@aliyunmq/mq-http-sdk'); // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instances . On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab. const endpoint = "${HTTP_ENDPOINT}"; // The AccessKey ID that you created in the Resource Access Management (RAM) console fo r identity verification. The AccessKey ID is used for identity verification. const accessKeyId = "${ACCESS_KEY}"; // The AccessKey secret that you created in the RAM console for identity verification. The AccessKey secret is used for identity verification. const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret); // The topic to which you want to send messages. The topic is created in the ApsaraMQ f or RocketMQ console. const topic = "${TOPIC}"; // The ID of the instance to which the topic belongs. The instance is created in the Ap saraMQ for RocketMQ console. // If the instance has a namespace, specify the ID of the instance. If the instance doe s not have a namespace, set the instance ID to null or an empty string. You can check w hether your instance has a namespace on the Instances page in the RocketMQ console. const instanceId = "${INSTANCE_ID}"; const producer = client.getProducer(instanceId, topic); (async function(){
  try {
    // Cyclically send four messages.
    for(var i = 0; i < 4; i++) {
      let res;
      msgProps = new MessageProperties();
      // The custom property of the message.
      msgProps.putProperty("a", i);
      // The key of the message.
      msgProps.messageKey("MessageKey");
      res = await producer.publishMessage("hello mq.", "", msgProps);
      console.log("Publish message: MessageID:%s,BodyMD5:%s", res.body.MessageId, res.b
ody.MessageBodyMD5);
  } catch(e) {
    // Specify the logic that you want to use to resend or persist the message if the m
essage fails to be sent and needs to be sent again.
    console.log(e)
})();
```

**Consume normal messages**

The following sample code provides an example on how to consume normal messages:

```
const {
  MQClient
} = require('@aliyunmq/mq-http-sdk'); // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instances . On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab. const endpoint = "${HTTP_ENDPOINT}"; // The AccessKey ID that is used for identity verification. You can obtain the AccessKe y ID in the Apsara Uni-manager Operations Console. const accessKeyId = "${ACCESS_KEY}"; // The AccessKey secret that is used for identity verification. You can obtain the Acce ssKey secret in the Apsara Uni-manager Operations Console. const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret); // The topic from which you want to consume messages. The topic is created in the Apsar aMQ for RocketMQ console. const topic = "${TOPIC}"; // The ID of the group that you created in the ApsaraMQ for RocketMQ console. const groupId = "${GROUP_ID}"; // The ID of the instance to which the topic belongs. The instance is created in the Ap saraMQ for RocketMQ console. // If the instance has a namespace, specify the ID of the instance. If the instance doe s not have a namespace, set the instance ID to null or an empty string. You can check w hether your instance has a namespace on the Instances page in the RocketMQ console. const instanceId = "${INSTANCE_ID}"; const consumer = client.getConsumer(instanceId, topic, groupId); (async function(){
  // Cyclically consume messages.
  while(true) {
    try {
      // Consume messages in long polling mode.
      // In long polling mode, if no message in the topic is available for consumption,
the request is suspended on the broker for a specified period of time. If a message bec omes available for consumption within this period, the broker immediately sends a respo nse to the consumer. In this example, the period is set to 3 seconds.
      res = await consumer.consumeMessage(
          3, // The maximum number of messages that can be consumed at a time. In this
example, the value is set to 3. The maximum value that you can specify is 16.
          3 // The length of a long polling period. Unit: seconds. In this example, the
value is set to 3. The maximum value that you can specify is 30.
```

);

```
      if (res.code == 200) {
        // Specify the message consumption logic.
        console.log("Consume Messages, requestId:%s", res.requestId);
```

`g` `g` `,` `q` `,` `q`

```
        const handles = res.body.map((message) => {
console.log("\tMessageId:%s,Tag:%s,PublishTime:%d,NextConsumeTime:%d,FirstConsumeTime:%d, nsumedTimes:%d,Body:%s" +
            ",Props:%j,MessageKey:%s,Prop-A:%s",
              message.MessageId, message.MessageTag, message.PublishTime, message.NextCo
nsumeTime, message.FirstConsumeTime, message.ConsumedTimes, message.MessageBody,message.Properties,message.MessageKey,message.Properties.a);
          return message.ReceiptHandle;
        });
        // If the broker does not receive an acknowledgment (ACK) for a message from th
e consumer before the period of time specified by the message.NextConsumeTime parameter elapses, the broker delivers the message for consumption again.
        // A unique timestamp is specified for the handle of a message each time the me
ssage is consumed.
        res = await consumer.ackMessage(handles);
        if (res.code != 204) {
          // If the handle of a message times out, the broker cannot receive an ACK for
the message from the consumer.
          console.log("Ack Message Fail:");
          const failHandles = res.body.map((error)=>{
            console.log("\tErrorHandle:%s, Code:%s, Reason:%s\n", error.ReceiptHandle,
error.ErrorCode, error.ErrorMessage);
            return error.ReceiptHandle;
          });
          handles.forEach((handle)=>{
            if (failHandles.indexOf(handle) < 0) {
              console.log("\tSucHandle:%s\n", handle);
          });
        } else {
          // Obtain an ACK from the consumer.
          console.log("Ack Message suc, RequestId:%s\n\t", res.requestId,
handles.join(','));
    } catch(e) {
      if (e.Code.indexOf("MessageNotExist") > -1) {
        // If no message in the topic is available for consumption, the long polling mo
de continues to take effect.
        console.log("Consume Message: no new message, RequestId:%s, Code:%s",
e.RequestId, e.Code);
      } else {
        console.log(e);
})();
```

##### Send and consume ordered messages

Ordered messages are a type of message that is published and consumed in a strict order. Ordered messages in ApsaraMQ for RocketMQ are also known as first-in-first-out (FIFO) messages. This topic provides sample code to show how to use the HTTP client SDK for Node.js to send and consume ordered messages.

**Background information**

Ordered messages are classified into the following types: Globally ordered message: All messages in a specified topic are published and consumed in first-in-first-out (FIFO) order. Partitionally ordered message: All messages in a specified topic are distributed to different partitions by using shard keys. The messages in each partition are published and consumed in FIFO order. A Sharding Key is a key field that is used for ordered messages to identify different partitions. The Sharding Key is different from the key of a normal message. For more information about the message routing feature, see Ordered messages.

**Prerequisites**

The following operations are performed: SDK for Node.js is installed. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send ordered messages**

The following sample code provides an example on how to send ordered messages:

```
const {
  MQClient,
  MessageProperties
} = require('@aliyunmq/mq-http-sdk'); // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instances . On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab. const endpoint = "${HTTP_ENDPOINT}"; // The AccessKey ID that is used for identity verification. You can obtain the AccessKe y ID in the Apsara Uni-manager Operations Console. const accessKeyId = "${ACCESS_KEY}"; // The AccessKey secret that is used for identity verification. You can obtain the Acce ssKey secret in the Apsara Uni-manager Operations Console. const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret); // The topic to which you want to send messages. The topic is created in the ApsaraMQ f or RocketMQ console. const topic = "${TOPIC}"; // The ID of the instance to which the topic belongs. The instance is created in the Ap saraMQ for RocketMQ console. // If the instance has a namespace, specify the ID of the instance. If the instance doe s not have a namespace, set the instance ID to null or an empty string. You can check w hether your instance has a namespace on the Instances page in the RocketMQ console. const instanceId = "${INSTANCE_ID}"; const producer = client.getProducer(instanceId, topic); (async function(){
  try {
    // Cyclically send eight messages.
    for(var i = 0; i < 8; i++) {
      msgProps = new MessageProperties();
      // The custom property of the message.
      msgProps.putProperty("a", i);
      // The shard key that is used to distribute ordered messages to a specific partit
ion. Shard keys can be used to identify different partitions. A shard key is different from a message key.
      msgProps.shardingKey(i % 2);
      res = await producer.publishMessage("hello mq.", "", msgProps);
      console.log("Publish message: MessageID:%s,BodyMD5:%s", res.body.MessageId, res.b
ody.MessageBodyMD5);
  } catch(e) {
    // Specify the logic that you want to use to resend or persist the message if the m
essage fails to be sent and needs to be sent again.
    console.log(e)
})();
```

**Consume ordered messages**

The following sample code provides an example on how to consume ordered messages:

```
const {
  MQClient,
} = require('@aliyunmq/mq-http-sdk'); // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instances . On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab. const endpoint = "${HTTP_ENDPOINT}"; // The AccessKey ID that is used for identity verification. You can obtain the AccessKe y ID in the Apsara Uni-manager Operations Console. const accessKeyId = "${ACCESS_KEY}"; // The AccessKey secret that is used for identity verification. You can obtain the Acce ssKey secret in the Apsara Uni-manager Operations Console. const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret); // The topic from which you want to consume messages. The topic is created in the Apsar aMQ for RocketMQ console. const topic = "${TOPIC}"; // The ID of the group that you created in the ApsaraMQ for RocketMQ console. const groupId = "GID_http"; // The ID of the instance to which the topic belongs. The instance is created in the Ap saraMQ for RocketMQ console. // If the instance has a namespace, specify the ID of the instance. If the instance doe s not have a namespace, set the instance ID to null or an empty string. You can check w hether your instance has a namespace on the Instances page in the RocketMQ console. const instanceId = "${INSTANCE_ID}"; const consumer = client.getConsumer(instanceId, topic, groupId); (async function(){
  // Cyclically consume messages.
  while(true) {
    try {
      // Consume messages in long polling mode. The consumer may pull partitionally ord
ered messages from multiple partitions. The consumer consumes messages from the same partition in the order in which the messages are sent.
      // A consumer pulls partitionally ordered messages from a partition. If the broke
r does not receive an acknowledgment (ACK) for a message after the message is consumed, the consumer consumes the message again.
      // The consumer can consume the next batch of messages from a partition only afte
r all messages that are pulled from the partition in the previous batch are acknowledge d to be consumed.
      // In long polling mode, if no message in the topic is available for consumption,
the request is suspended on the broker for a specified period of time. If a message bec omes available for consumption within this period, the broker immediately sends a respo nse to the consumer. In this example, the period is set to 3 seconds.
      res = await consumer.consumeMessageOrderly(
          3, // The maximum number of messages that can be consumed at a time. In this
```

`,` `g`

```
example, the value is set to 3. The maximum value that you can specify is 16.
          3 // The length of a long polling period. Unit: seconds. In this example, the
value is set to 3. The maximum value that you can specify is 30.
```

);

```
      if (res.code == 200) {
        // Specify the message consumption logic.
        console.log("Consume Messages, requestId:%s", res.requestId);
        const handles = res.body.map((message) => {
console.log("\tMessageId:%s,Tag:%s,PublishTime:%d,NextConsumeTime:%d,FirstConsumeTime:%d, nsumedTimes:%d,Body:%s" +
            ",Props:%j,ShardingKey:%s,Prop-A:%s,Tag:%s",
              message.MessageId, message.MessageTag, message.PublishTime, message.NextCo
nsumeTime, message.FirstConsumeTime, message.ConsumedTimes, message.MessageBody,message.Properties,message.ShardingKey,message.Properties.a,message.M sageTag);
          return message.ReceiptHandle;
        });
        // If the broker does not receive an ACK for a message from the consumer before
the period of time specified by the message.NextConsumeTime parameter elapses, the brok er delivers the message for consumption again.
        // A unique timestamp is specified for the handle of a message each time the me
ssage is consumed.
        res = await consumer.ackMessage(handles);
        if (res.code != 204) {
          // If the handle of a message times out, the broker cannot receive an ACK for
the message from the consumer.
          console.log("Ack Message Fail:");
          const failHandles = res.body.map((error)=>{
            console.log("\tErrorHandle:%s, Code:%s, Reason:%s\n", error.ReceiptHandle,
error.ErrorCode, error.ErrorMessage);
            return error.ReceiptHandle;
          });
          handles.forEach((handle)=>{
            if (failHandles.indexOf(handle) < 0) {
              console.log("\tSucHandle:%s\n", handle);
          });
        } else {
          // Obtain an ACK from the consumer.
          console.log("Ack Message suc, RequestId:%s\n\t", res.requestId,
handles.join(','));
    } catch(e) {
      if (e.Code.indexOf("MessageNotExist") > -1) {
        // If no message in the topic is available for consumption, the long polling mo
de continues to take effect.
        console.log("Consume Message: no new message, RequestId:%s, Code:%s",
e.RequestId, e.Code);
      } else {
```

```
        console.log(e);
})();
```

##### Send and consume scheduled messages

**and delayed messages**

This topic provides sample code to show how to use the HTTP client SDK for Node.js to send and consume scheduled messages and delayed messages.

**Background information**

Delayed message: The producer sends the message to the ApsaraMQ for RocketMQ server, but does not expect the message to be delivered immediately. Instead, the message is delivered to the consumer for consumption after a certain period of time. This message is a delayed message. Scheduled message: A producer sends a message to a ApsaraMQ for RocketMQ broker and expects the message to be delivered to a consumer at a specified point in time. This type of message is called a scheduled message. If an HTTP client SDK is used, the code configurations of scheduled messages are the same as the code configurations of delayed messages. Both types of messages are delivered to consumers after a specific period of time based on the attributes of the messages. For more information about the message routing feature, see Scheduled messages and delayed messages.

**Prerequisites**

The following operations are performed: SDK for Node.js is installed. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send scheduled messages or delayed messages**

The following sample code provides an example on how to send scheduled messages or delayed messages:

```
const {
  MQClient,
  MessageProperties
} = require('@aliyunmq/mq-http-sdk'); // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instances . On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab. const endpoint = "${HTTP_ENDPOINT}"; // The AccessKey ID that is used for identity verification. You can obtain the AccessKe
```

```
y ID in the Apsara Uni-manager Operations Console. const accessKeyId = "${ACCESS_KEY}"; // The AccessKey secret that is used for identity verification. You can obtain the Acce ssKey secret in the Apsara Uni-manager Operations Console. const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret); // The topic to which you want to send messages. The topic is created in the ApsaraMQ f or RocketMQ console. const topic = "${TOPIC}"; // The ID of the instance to which the topic belongs. The instance is created in the Ap saraMQ for RocketMQ console. // If the instance has a namespace, specify the ID of the instance. If the instance doe s not have a namespace, set the instance ID to null or an empty string. You can check w hether your instance has a namespace on the Instances page in the RocketMQ console. const instanceId = "${INSTANCE_ID}"; const producer = client.getProducer(instanceId, topic); (async function(){
  try {
    // Cyclically send four messages.
    for(var i = 0; i < 4; i++) {
      let res;
      msgProps = new MessageProperties();
      // The custom property of the message.
      msgProps.putProperty("a", i);
      // The key of the message.
      msgProps.messageKey("MessageKey");
      // The period of time after which the broker delivers the message. In this exampl
e, when the broker receives a message, the broker waits for 10 seconds before it delive rs the message to the consumer. Set this parameter to a timestamp in milliseconds.
      // If the producer sends a scheduled message, set the parameter to the time inter
val between the scheduled point in time and the current point in time.
      msgProps.startDeliverTime(Date.now() + 10 * 1000);
      res = await producer.publishMessage("hello mq. timer msg!", "TagA", msgProps);
      console.log("Publish message: MessageID:%s,BodyMD5:%s", res.body.MessageId, res.b
ody.MessageBodyMD5);
  } catch(e) {
    // Specify the logic that you want to use to resend or persist the message if the m
essage fails to be sent and needs to be sent again.
    console.log(e)
})();
```

**Consume scheduled messages or delayed messages**

The following sample code provides an example on how to consume scheduled messages or delayed messages:

```
const { MQClient
```

```
  MQClient
} = require('@aliyunmq/mq-http-sdk'); // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instances . On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab. const endpoint = "${HTTP_ENDPOINT}"; // The AccessKey ID that is used for identity verification. You can obtain the AccessKe y ID in the Apsara Uni-manager Operations Console. const accessKeyId = "${ACCESS_KEY}"; // The AccessKey secret that is used for identity verification. You can obtain the Acce ssKey secret in the Apsara Uni-manager Operations Console. const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret); // The topic from which you want to consume messages. The topic is created in the Apsar aMQ for RocketMQ console. const topic = "${TOPIC}"; // The ID of the group that you created in the ApsaraMQ for RocketMQ console. const groupId = "${GROUP_ID}"; // The ID of the instance to which the topic belongs. The instance is created in the Ap saraMQ for RocketMQ console. // If the instance has a namespace, specify the ID of the instance. If the instance doe s not have a namespace, set the instance ID to null or an empty string. You can check w hether your instance has a namespace on the Instances page in the RocketMQ console. const instanceId = "${INSTANCE_ID}"; const consumer = client.getConsumer(instanceId, topic, groupId); (async function(){
  // Cyclically consume messages.
  while(true) {
    try {
      // Consume messages in long polling mode.
      // In long polling mode, if no message in the topic is available for consumption,
the request is suspended on the broker for a specified period of time. If a message bec omes available for consumption within this period, the broker immediately sends a respo nse to the consumer. In this example, the period is set to 3 seconds.
      res = await consumer.consumeMessage(
          3, // The maximum number of messages that can be consumed at a time. In this
example, the value is set to 3. The maximum value that you can specify is 16.
          3 // The length of a long polling period. Unit: seconds. In this example, the
value is set to 3. The maximum value that you can specify is 30.
```

);

```
      if (res.code == 200) {
        // Specify the message consumption logic.
        console.log("Consume Messages, requestId:%s", res.requestId);
        const handles = res.body.map((message) => {
console.log("\tMessageId:%s,Tag:%s,PublishTime:%d,NextConsumeTime:%d,FirstConsumeTime:%d, nsumedTimes:%d,Body:%s" + ",Props:%j,MessageKey:%s,Prop-A:%s",
```

```
            ,Props:%j,MessageKey:%s,PropA:%s,
              message.MessageId, message.MessageTag, message.PublishTime, message.NextCo
nsumeTime, message.FirstConsumeTime, message.ConsumedTimes, message.MessageBody,message.Properties,message.MessageKey,message.Properties.a);
          return message.ReceiptHandle;
        });
        // If the broker does not receive an acknowledgment (ACK) for a message from th
e consumer before the period of time specified by the message.NextConsumeTime parameter elapses, the broker delivers the message for consumption again.
        // A unique timestamp is specified for the handle of a message each time the me
ssage is consumed.
        res = await consumer.ackMessage(handles);
        if (res.code != 204) {
          // If the handle of a message times out, the broker cannot receive an ACK for
the message from the consumer.
          console.log("Ack Message Fail:");
          const failHandles = res.body.map((error)=>{
            console.log("\tErrorHandle:%s, Code:%s, Reason:%s\n", error.ReceiptHandle,
error.ErrorCode, error.ErrorMessage);
            return error.ReceiptHandle;
          });
          handles.forEach((handle)=>{
            if (failHandles.indexOf(handle) < 0) {
              console.log("\tSucHandle:%s\n", handle);
          });
        } else {
          // Obtain an ACK from the consumer.
          console.log("Ack Message suc, RequestId:%s\n\t", res.requestId,
handles.join(','));
    } catch(e) {
      if (e.Code.indexOf("MessageNotExist") > -1) {
        // If no message in the topic is available for consumption, the long polling mo
de continues to take effect.
        console.log("Consume Message: no new message, RequestId:%s, Code:%s",
e.RequestId, e.Code);
      } else {
        console.log(e);
})();
```

##### Send and consume transactional messages

ApsaraMQ for RocketMQ provides a distributed transaction processing feature that is similar to X/Open XA. ApsaraMQ for RocketMQ uses transactional messages to ensure transactional consistency. This topic provides sample code to show how to use the HTTP client SDK for Node.js to send and consume transactional messages.

**Background information**

The following figure shows the interaction process of transactional messages. For more information about the message routing feature, see Transactional messages.

**Prerequisites**

The following operations are performed: SDK for Node.js is installed. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send transactional messages**

The following sample code provides an example on how to send transactional messages:

```
const {
  MQClient,
  MessageProperties
} = require('@aliyunmq/mq-http-sdk'); // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instances . On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab. const endpoint = "${HTTP_ENDPOINT}"; // The AccessKey ID that is used for identity verification. You can obtain the AccessKe y ID in the Apsara Uni-manager Operations Console. const accessKeyId = "${ACCESS_KEY}"; // The AccessKey secret that is used for identity verification. You can obtain the Acce ssKey secret in the Apsara Uni-manager Operations Console. const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret); // The topic to which you want to send messages. The topic is created in the ApsaraMQ f or RocketMQ console. const topic = "${TOPIC}"; // The ID of the group that you created in the ApsaraMQ for RocketMQ console. const groupId = "${GROUP_ID}"; //Th
```

`ID`

```
fth
```

`i` `t` `t`

```
hihth
```

`t` `i` `b``l` `Th` `i` `t` `i`

```
tdi
```

`th` `A`

```
// The ID of the instance to which the topic belongs. The instance is created in the Ap saraMQ for RocketMQ console. // If the instance has a namespace, specify the ID of the instance. If the instance doe s not have a namespace, set the instance ID to null or an empty string. You can check w hether your instance has a namespace on the Instances page in the RocketMQ console. const instanceId = "${INSTANCE_ID}"; const mqTransProducer = client.getTransProducer(instanceId, topic, groupId); async function processTransResult(res, msgId) {
    if (!res) {
        return;
    if (res.code != 204) {
      // If a transactional message is not committed or rolled back before the timeout
period specified by the TransCheckImmunityTime parameter for the handle of the transact ional message elapses or before the timeout period specified for the handle of consumeH alfMessage elapses, the commit or rollback operation fails. In this example, the timeou t period for the handle of consumeHalfMessage is 10 seconds.
      console.log("Commit/Rollback Message Fail:");
      const failHandles = res.body.map((error) => {
        console.log("\tErrorHandle:%s, Code:%s, Reason:%s\n", error.ReceiptHandle,
error.ErrorCode, error.ErrorMessage);
        return error.ReceiptHandle;
      });
    } else {
      console.log("Commit/Rollback Message suc!!! %s", msgId);
var halfMessageCount = 0; var halfMessageConsumeCount = 0; (async function(){
  try {
    // Cyclically send four transactional messages.
    for(var i = 0; i < 4; i++) {
      let res;
      msgProps = new MessageProperties();
      // The custom property of the message.
      msgProps.putProperty("a", i);
      // The key of the message.
      msgProps.messageKey("MessageKey");
      // The time interval between the time when the transactional message is sent and
the start time of the first transaction status check. Unit: seconds. Valid values: 10 t o 300.
      // If the message is not committed or rolled back after the first transaction sta
tus check is performed, the broker initiates a request to check the status of the local transaction at an interval of 10 seconds within the next 24 hours.
      msgProps.transCheckImmunityTime(10);
      res = await mqTransProducer.publishMessage("hello mq.", "tagA", msgProps);
      console.log("Publish message: MessageID:%s,BodyMD5:%s,Handle:%s",
res.body.MessageId, res.body.MessageBodyMD5, res.body.ReceiptHandle);
      if (res && i == 0) {
//Aftertheproducersendsthetransactionalmessage thebrokerobtainsthe
```

```
         // After the producer sends the transactional message, the broker obtains the
handle of the half message that corresponds to the transactional message and commits or rolls back the transactional message based on the status of the handle.
          const msgId = res.body.MessageId;
          res = await mqTransProducer.commit(res.body.ReceiptHandle);
          console.log("Commit msg when publish, %s", msgId);
          // If the transactional message is not committed or rolled back before the ti
meout period specified by the TransCheckImmunityTime parameter elapses, the commit or r ollback operation fails.
        processTransResult(res, msgId);
  } catch(e) {
    // Specify the logic that you want to use to resend or persist the message if the m
essage fails to be sent and needs to be sent again.
    console.log(e)
})(); // The client needs a thread or a process to process unacknowledged transactional messa ges. // Process unacknowledged transactional messages. (async function() {
  // Cyclically check the status of half messages. This process is similar to consuming
normal messages.
  while(halfMessageCount < 3 && halfMessageConsumeCount < 15) {
    try {
        halfMessageConsumeCount++;
      res = await mqTransProducer.consumeHalfMessage(3, 3);
      if (res.code == 200) {
        // Specify the message consumption logic.
        console.log("Consume Messages, requestId:%s", res.requestId);
        res.body.forEach(async (message) => {
console.log("\tMessageId:%s,Tag:%s,PublishTime:%d,NextConsumeTime:%d,FirstConsumeTime:%d, nsumedTimes:%d,Body:%s" +
            ",Props:%j,MessageKey:%s,Prop-A:%s",
              message.MessageId, message.MessageTag, message.PublishTime, message.NextCo
nsumeTime, message.FirstConsumeTime, message.ConsumedTimes, message.MessageBody,message.Properties,message.MessageKey,message.Properties.a);
          var propA = message.Properties && message.Properties.a ?
parseInt(message.Properties.a) : 0;
                  var opResp;
                  if (propA == 1 || (propA == 2 && message.ConsumedTimes > 1)) {
                      opResp = await mqTransProducer.commit(message.ReceiptHandle);
                      console.log("Commit msg when check half, %s", message.MessageId);
                      halfMessageCount++;
                  } else if (propA == 3) {
                      opResp = await mqTransProducer.rollback(message.ReceiptHandle);
                      console.log("Rollback msg when check half, %s",
message.MessageId);
                      halfMessageCount++;
```

```
                  processTransResult(opResp, message.MessageId);
        });
    } catch(e) {
      if (e.Code && e.Code.indexOf("MessageNotExist") > -1) {
        // If no message in the topic is available for consumption, the long polling mo
de continues to take effect.
        console.log("Consume Transaction Half msg: no new message, RequestId:%s,
Code:%s", e.RequestId, e.Code);
      } else {
        console.log(e);
})();
```

**Consume transactional messages**

The following sample code provides an example on how to consume transactional messages:

```
const {
  MQClient
} = require('@aliyunmq/mq-http-sdk'); // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click Instances . On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab. const endpoint = "${HTTP_ENDPOINT}"; // The AccessKey ID that is used for identity verification. You can obtain the AccessKe y ID in the Apsara Uni-manager Operations Console. const accessKeyId = "${ACCESS_KEY}"; // The AccessKey secret that is used for identity verification. You can obtain the Acce ssKey secret in the Apsara Uni-manager Operations Console. const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret); // The topic from which you want to consume messages. The topic is created in the Apsar aMQ for RocketMQ console. const topic = "${TOPIC}"; // The ID of the group that you created in the ApsaraMQ for RocketMQ console. const groupId = "${GROUP_ID}"; // The ID of the instance to which the topic belongs. The instance is created in the Ap saraMQ for RocketMQ console. // If the instance has a namespace, specify the ID of the instance. If the instance doe s not have a namespace, set the instance ID to null or an empty string. You can check w hether your instance has a namespace on the Instances page in the RocketMQ console. const instanceId = "${INSTANCE_ID}"; const consumer = client.getConsumer(instanceId, topic, groupId); (async function(){
  // Cyclically consume messages.
```

```
  while(true) {
    try {
      // Consume messages in long polling mode.
      // In long polling mode, if no message in the topic is available for consumption,
the request is suspended on the broker for a specified period of time. If a message bec omes available for consumption within this period, the broker immediately sends a respo nse to the consumer. In this example, the period is set to 3 seconds.
      res = await consumer.consumeMessage(
          3, // The maximum number of messages that can be consumed at a time. In this
example, the value is set to 3. The maximum value that you can specify is 16.
          3 // The length of a long polling period. Unit: seconds. In this example, the
value is set to 3. The maximum value that you can specify is 30.
```

);

```
      if (res.code == 200) {
        // Specify the message consumption logic.
        console.log("Consume Messages, requestId:%s", res.requestId);
        const handles = res.body.map((message) => {
console.log("\tMessageId:%s,Tag:%s,PublishTime:%d,NextConsumeTime:%d,FirstConsumeTime:%d, nsumedTimes:%d,Body:%s" +
            ",Props:%j,MessageKey:%s,Prop-A:%s",
              message.MessageId, message.MessageTag, message.PublishTime, message.NextCo
nsumeTime, message.FirstConsumeTime, message.ConsumedTimes, message.MessageBody,message.Properties,message.MessageKey,message.Properties.a);
          return message.ReceiptHandle;
        });
        // If the broker does not receive an acknowledgment (ACK) for a message from th
e consumer before the period of time specified by the message.NextConsumeTime parameter elapses, the broker delivers the message for consumption again.
        // A unique timestamp is specified for the handle of a message each time the me
ssage is consumed.
        res = await consumer.ackMessage(handles);
        if (res.code != 204) {
          // If the handle of a message times out, the broker cannot receive an ACK for
the message from the consumer.
          console.log("Ack Message Fail:");
          const failHandles = res.body.map((error)=>{
            console.log("\tErrorHandle:%s, Code:%s, Reason:%s\n", error.ReceiptHandle,
error.ErrorCode, error.ErrorMessage);
            return error.ReceiptHandle;
          });
          handles.forEach((handle)=>{
            if (failHandles.indexOf(handle) < 0) {
              console.log("\tSucHandle:%s\n", handle);
          });
        } else {
          // Obtain an ACK from the consumer.
          console.log("Ack Message suc, RequestId:%s\n\t", res.requestId,
handles.join(','));
```

```
    } catch(e) {
      if (e.Code.indexOf("MessageNotExist") > -1) {
        // If no message in the topic is available for consumption, the long polling mo
de continues to take effect.
        console.log("Consume Message: no new message, RequestId:%s, Code:%s",
e.RequestId, e.Code);
      } else {
        console.log(e);
})();
```

#### PHP SDK

##### Prepare the environment

This topic describes how to prepare the environment before you use the HTTP client SDK for PHP to send and consume messages.

**Environment requirements**

PHP 5.5.0 or later is installed. For more information, see Install PHP. Composer is installed. For more information, see Install Composer. After PHP is installed, you can run the `php -v` command to view the version of PHP that you installed.

**Install the SDK for PHP**

To install the SDK for PHP, perform the following steps:
1. Add the following dependency to the composer.json file in your PHP installation directory:
`{`

```json
  "require": {
     "aliyunmq/mq-http-sdk": ">=1.0.3"
```

2. Run the following command to use Composer to install the SDK for PHP:

```
composer install
```

##### Send and consume normal messages

Normal messages are messages that have no special features in ApsaraMQ for RocketMQ. They are different from featured messages, such as scheduled messages, delayed messages, ordered messages, and transactional messages. This topic provides sample code to show how to use the HTTP client SDK for PHP to send and consume normal messages.

**Prerequisites**

The following operations are performed: Install the SDK for PHP. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send normal messages**

The following sample code provides an example on how to send normal messages:

```
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; use MQ\MQClient; class ProducerTest
```

`{`

```java
    private $client;
    private $producer;
    public function __construct()
```

`{`

```
        $this->client = new MQClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
        // The topic to which you want to send messages. The topic is created in the Ap
saraMQ for RocketMQ console.
        $topic = "${TOPIC}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        $instanceId = "${INSTANCE_ID}";
        $this->producer = $this->client->getProducer($instanceId, $topic);
    public function run()
```

`{`

```
        try
```

`{`

```
            for ($i=1; $i<=4; $i++)
```

`{`

```
                $publishMessage = new TopicMessage(
                // The content of the message.
                "hello mq!"
```

);

```
                // The custom property of the message.
                $publishMessage->putProperty("a", $i);
                // The key of the message.
                $publishMessage->setMessageKey("MessageKey");
                $result = $this->producer->publishMessage($publishMessage);
                print "Send mq message success. msgId is:" . $result->getMessageId() . "
, bodyMD5 is:" . $result->getMessageBodyMD5() . "\n";
        } catch (\Exception $e) {
            print_r($e->getMessage() . "\n");
$instance = new ProducerTest(); $instance->run();
```

?>

**Consume normal messages**

The following sample code provides an example on how to consume normal messages:

```
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; use MQ\MQClient; class ConsumerTest
```

`{`

```java
    private $client;
    private $producer;
    public function __construct()
```

`{`

```
        $this->client = new MQClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view
```

`th`

```
HTTP
```

`d` `i``t` `th` `N``t` `k``M`

```
ttb
```

```
the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
        // The topic from which you want to consume messages. The topic is created in t
he ApsaraMQ for RocketMQ console.
        $topic = "${TOPIC}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        $groupId = "${GROUP_ID}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        $instanceId = "${INSTANCE_ID}";
        $this->consumer = $this->client->getConsumer($instanceId, $topic, $groupId);
    public function run()
```

`{`

```
        // Cyclically consume messages in the current thread. We recommend that you use
multiple threads to concurrently consume messages.
        while (True) {
            try {
                // Consume messages in long polling mode.
                // In long polling mode, if no message in the topic is available for con
sumption, the request is suspended on the broker for a specified period of time. If a m essage becomes available for consumption within this period, the broker immediately sen ds a response to the consumer. In this example, the period is set to 3 seconds.
                $messages = $this->consumer->consumeMessage(
                    3, // The maximum number of messages that can be consumed at a time.
In this example, the value is set to 3. The maximum value that you can specify is 16.
                    3  // The length of a long polling period. Unit: seconds. In this ex
ample, the value is set to 3. The maximum value that you can specify is 30.
```

);

```
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\MessageNotExistException) {
                    // If no message in the topic is available for consumption, the long
polling mode continues to take effect.
                    printf("No message, contine long polling!RequestId:%s\n", $e->getReq
uestId());
                    continue;
                print_r($e->getMessage() . "\n");
sleep(3);
```

```
                sleep(3);
                continue;
            print "consume finish, messages:\n";
            // Specify the message consumption logic.
            $receiptHandles = array();
            foreach ($messages as $message) {
                $receiptHandles[] = $message->getReceiptHandle();
                printf("MessageID:%s TAG:%s BODY:%s \nPublishTime:%d,
FirstConsumeTime:%d, \nConsumedTimes:%d, NextConsumeTime:%d,MessageKey:%s\n",
                    $message->getMessageId(), $message->getMessageTag(), $message->getMe
ssageBody(),
                    $message->getPublishTime(), $message->getFirstConsumeTime(), $messag
e->getConsumedTimes(), $message->getNextConsumeTime(),
                    $message->getMessageKey());
                print_r($message->getProperties());
            // If the broker does not receive an acknowledgment (ACK) for a message
from the consumer before the period of time specified by $message->getNextConsumeTime() elapses, the broker delivers the message for consumption again.
            // A unique timestamp is specified for the handle of a message each time th
e message is consumed.
            print_r($receiptHandles);
            try {
                $this->consumer->ackMessage($receiptHandles);
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\AckMessageException) {
                    // If the handle of a message times out, the broker cannot receive a
n ACK for the message from the consumer.
                    printf("Ack Error, RequestId:%s\n", $e->getRequestId());
                    foreach ($e->getAckMessageErrorItems() as $errorItem) {
                        printf("\tReceiptHandle:%s, ErrorCode:%s, ErrorMsg:%s\n", $error
Item->getReceiptHandle(), $errorItem->getErrorCode(), $errorItem->getErrorCode());
            print "ack finish\n";
$instance = new ConsumerTest(); $instance->run();
```

?>

##### Send and consume ordered messages

Ordered messages are a type of message that is published and consumed in a strict order. Ordered messages in ApsaraMQ for RocketMQ are also known as first-in-first-out (FIFO) messages. This topic provides sample code to show how to use the HTTP client SDK for PHP to send and consume ordered messages.

**Background information**

Ordered messages are classified into the following types: Globally ordered message: All messages in a specified topic are published and consumed in first-in-first-out (FIFO) order. Partitionally ordered message: All messages in a specified topic are distributed to different partitions by using shard keys. The messages in each partition are published and consumed in FIFO order. A Sharding Key is a key field that is used for ordered messages to identify different partitions. The Sharding Key is different from the key of a normal message. For more information about the message routing feature, see Ordered messages.

**Prerequisites**

The following operations are performed: Install the SDK for PHP. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send ordered messages**

The following sample code provides an example on how to send ordered messages:

```
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; use MQ\MQClient; class ProducerTest
```

`{`

```java
    private $client;
    private $producer;
    public function __construct()
```

`{`

```
        $this->client = new MQClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
```

```
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
        // The topic to which you want to send messages. The topic is created in the Ap
saraMQ for RocketMQ console.
        $topic = "${TOPIC}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        $instanceId = "${INSTANCE_ID}";
        $this->producer = $this->client->getProducer($instanceId, $topic);
    public function run()
```

`{`

```
        try
```

`{`

```
            for ($i=1; $i<=4; $i++)
```

`{`

```
                $publishMessage = new TopicMessage(
                    "hello mq!"// The content of the message.
```

);

```
                // The custom property of the message.
                $publishMessage->putProperty("a", $i);
                // The shard key that is used to distribute ordered messages to a specif
ic partition. Shard keys can be used to identify different partitions. A shard key is d ifferent from a message key.
                $publishMessage->setShardingKey($i % 2);
                $result = $this->producer->publishMessage($publishMessage);
                print "Send mq message success. msgId is:" . $result->getMessageId() . "
, bodyMD5 is:" . $result->getMessageBodyMD5() . "\n";
        } catch (\Exception $e) {
            print_r($e->getMessage() . "\n");
$instance = new ProducerTest(); $instance->run();
```

?>

**Consume ordered messages**

The following sample code provides an example on how to consume ordered messages:

```
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; use MQ\MQClient; class ConsumerTest
```

`{`

```java
    private $client;
    private $producer;
    public function __construct()
```

`{`

```
        $this->client = new MQClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
        // The topic from which you want to consume messages. The topic is created in t
he ApsaraMQ for RocketMQ console.
        $topic = "${TOPIC}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        $groupId = "${GROUP_ID}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        $instanceId = "${INSTANCE_ID}";
        $this->consumer = $this->client->getConsumer($instanceId, $topic, $groupId);
    public function run()
```

`{`

```
        // Cyclically consume messages in the current thread. We recommend that you use
multiple threads to concurrently consume messages.
        while (True) {
            try {
                // Consume messages in long polling mode. The consumer may pull
```

`g` `g``p` `g` `y``p`

```
partitionally ordered messages from multiple partitions. The consumer consumes messages from the same partition in the order in which the messages are sent.
                // A consumer pulls partitionally ordered messages from a partition. If
the broker does not receive an acknowledgment (ACK) for a message after the message is consumed, the consumer consumes the message again.
                // The consumer can consume the next batch of messages from a partition
only after all messages that are pulled from the partition in the previous batch are ac knowledged to be consumed.
                // In long polling mode, if no message in the topic is available for con
sumption, the request is suspended on the broker for a specified period of time. If a m essage becomes available for consumption within this period, the broker immediately sen ds a response to the consumer. In this example, the period is set to 3 seconds.
                $messages = $this->consumer->consumeMessageOrderly(
                    3, // The maximum number of messages that can be consumed at a time.
In this example, the value is set to 3. The maximum value that you can specify is 16.
                    3  // The length of a long polling period. Unit: seconds. In this ex
ample, the value is set to 3. The maximum value that you can specify is 30.
```

);

```
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\MessageNotExistException) {
                    // If no message in the topic is available for consumption, the long
polling mode continues to take effect.
                    printf("No message, contine long polling!RequestId:%s\n", $e->getReq
uestId());
                    continue;
                print_r($e->getMessage() . "\n");
                sleep(3);
                continue;
            print "======>consume finish, messages:\n";
            // Specify the message consumption logic.
            $receiptHandles = array();
            foreach ($messages as $message) {
                $receiptHandles[] = $message->getReceiptHandle();
                printf("MessageID:%s TAG:%s BODY:%s \nPublishTime:%d,
FirstConsumeTime:%d, \nConsumedTimes:%d, NextConsumeTime:%d,ShardingKey:%s\n",
                    $message->getMessageId(), $message->getMessageTag(), $message->getMe
ssageBody(),
                    $message->getPublishTime(), $message->getFirstConsumeTime(), $messag
e->getConsumedTimes(), $message->getNextConsumeTime(),
                    $message->getShardingKey());
                print_r($message->getProperties());
            // If the broker does not receive an ACK for a message from the consumer be
fore the period of time specified by $message->getNextConsumeTime() elapses, the broker delivers the message for consumption again.
            // A unique timestamp is specified for the handle of a message each time th
e message is consumed.
```

```
            print_r($receiptHandles);
            try {
                $this->consumer->ackMessage($receiptHandles);
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\AckMessageException) {
                    // If the handle of a message times out, the broker cannot receive a
n ACK for the message from the consumer.
                    printf("Ack Error, RequestId:%s\n", $e->getRequestId());
                    foreach ($e->getAckMessageErrorItems() as $errorItem) {
                        printf("\tReceiptHandle:%s, ErrorCode:%s, ErrorMsg:%s\n", $error
Item->getReceiptHandle(), $errorItem->getErrorCode(), $errorItem->getErrorCode());
            print "=======>ack finish\n";
$instance = new ConsumerTest(); $instance->run();
```

?>

##### Send and consume scheduled messages

**and delayed messages**

This topic provides sample code to show how to use the HTTP client SDK for PHP to send and consume scheduled messages and delayed messages.

**Background information**

Delayed message: The producer sends the message to the ApsaraMQ for RocketMQ server, but does not expect the message to be delivered immediately. Instead, the message is delivered to the consumer for consumption after a certain period of time. This message is a delayed message. Scheduled message: A producer sends a message to a ApsaraMQ for RocketMQ broker and expects the message to be delivered to a consumer at a specified point in time. This type of message is called a scheduled message. If an HTTP client SDK is used, the code configurations of scheduled messages are the same as the code configurations of delayed messages. Both types of messages are delivered to consumers after a specific period of time based on the attributes of the messages. For more information about the message routing feature, see Scheduled messages and delayed messages.

**Prerequisites**

The following operations are performed: Install the SDK for PHP. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send scheduled messages or delayed messages**

The following sample code provides an example on how to send scheduled messages or delayed messages:

```
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; use MQ\MQClient; class ProducerTest
```

`{`

```java
    private $client;
    private $producer;
    public function __construct()
```

`{`

```
        $this->client = new MQClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
        // The topic to which you want to send messages. The topic is created in the Ap
saraMQ for RocketMQ console.
        $topic = "${TOPIC}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        $instanceId = "${INSTANCE_ID}";
        $this->producer = $this->client->getProducer($instanceId, $topic);
    public function run()
```

`{`

```
        try
```

`{`

```
            for ($i=1; $i<=4; $i++)
```

`{`

```
                $publishMessage = new TopicMessage(
                    "hello mq!"// The content of the message.
```

);

```
                // The custom property of the message.
                $publishMessage->putProperty("a", $i);
                // The key of the message.
                $publishMessage->setMessageKey("MessageKey");
                // The period of time after which the broker delivers the message. In
this example, when the broker receives a message, the broker waits for 10 seconds befor e it delivers the message to the consumer. Set this parameter to a timestamp in millise conds.
                // If the producer sends a scheduled message, set the parameter to the
time interval between the scheduled point in time and the current point in time.
                $publishMessage->setStartDeliverTime(time() * 1000 + 10 * 1000);
                $result = $this->producer->publishMessage($publishMessage);
                print "Send mq message success. msgId is:" . $result->getMessageId() . "
, bodyMD5 is:" . $result->getMessageBodyMD5() . "\n";
        } catch (\Exception $e) {
            print_r($e->getMessage() . "\n");
$instance = new ProducerTest(); $instance->run();
```

?>

**Consume scheduled messages or delayed messages**

The following sample code provides an example on how to consume scheduled messages or delayed messages:

```
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; use MQ\MQClient; class ConsumerTest
```

`{`

```
private$client;
```

```java
    private $client;
    private $producer;
    public function __construct()
```

`{`

```
        $this->client = new MQClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
        // The topic from which you want to consume messages. The topic is created in t
he ApsaraMQ for RocketMQ console.
        $topic = "${TOPIC}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        $groupId = "${GROUP_ID}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        $instanceId = "${INSTANCE_ID}";
        $this->consumer = $this->client->getConsumer($instanceId, $topic, $groupId);
    public function run()
```

`{`

```
        // Cyclically consume messages in the current thread. We recommend that you use
multiple threads to concurrently consume messages.
        while (True) {
            try {
                // Consume messages in long polling mode.
                // In long polling mode, if no message in the topic is available for con
sumption, the request is suspended on the broker for a specified period of time. If a m essage becomes available for consumption within this period, the broker immediately sen ds a response to the consumer. In this example, the period is set to 3 seconds.
                $messages = $this->consumer->consumeMessage(
                    3, // The maximum number of messages that can be consumed at a time.
In this example, the value is set to 3. The maximum value that you can specify is 16.
                    3  // The length of a long polling period. Unit: seconds. In this ex
ample, the value is set to 3. The maximum value that you can specify is 30.
```

);

```
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\MessageNotExistException) {
                    // If no message in the topic is available for consumption, the long
```

`//` `g` `p` `p` `,` `g`

```
polling mode continues to take effect.
                    printf("No message, contine long polling!RequestId:%s\n", $e->getReq
uestId());
                    continue;
                print_r($e->getMessage() . "\n");
                sleep(3);
                continue;
            print "consume finish, messages:\n";
            // Specify the message consumption logic.
            $receiptHandles = array();
            foreach ($messages as $message) {
                $receiptHandles[] = $message->getReceiptHandle();
                printf("MessageID:%s TAG:%s BODY:%s \nPublishTime:%d,
FirstConsumeTime:%d, \nConsumedTimes:%d, NextConsumeTime:%d,MessageKey:%s\n",
                    $message->getMessageId(), $message->getMessageTag(), $message->getMe
ssageBody(),
                    $message->getPublishTime(), $message->getFirstConsumeTime(), $messag
e->getConsumedTimes(), $message->getNextConsumeTime(),
                    $message->getMessageKey());
                print_r($message->getProperties());
            // If the broker does not receive an acknowledgment (ACK) for a message
from the consumer before the period of time specified by $message->getNextConsumeTime() elapses, the broker delivers the message for consumption again.
            // A unique timestamp is specified for the handle of a message each time th
e message is consumed.
            print_r($receiptHandles);
            try {
                $this->consumer->ackMessage($receiptHandles);
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\AckMessageException) {
                    // If the handle of a message times out, the broker cannot receive a
n ACK for the message from the consumer.
                    printf("Ack Error, RequestId:%s\n", $e->getRequestId());
                    foreach ($e->getAckMessageErrorItems() as $errorItem) {
                        printf("\tReceiptHandle:%s, ErrorCode:%s, ErrorMsg:%s\n", $error
Item->getReceiptHandle(), $errorItem->getErrorCode(), $errorItem->getErrorCode());
            print "ack finish\n";
```

```
$instance = new ConsumerTest(); $instance->run();
```

?>

##### Send and consume transactional messages

ApsaraMQ for RocketMQ provides a distributed transaction processing feature that is similar to X/Open XA. ApsaraMQ for RocketMQ uses transactional messages to ensure transactional consistency. This topic provides sample code to show how to use the HTTP client SDK for PHP to send and consume transactional messages.

**Background information**

The following figure shows the interaction process of transactional messages. For more information about the message routing feature, see Transactional messages.

**Prerequisites**

The following operations are performed: Install the SDK for PHP. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send transactional messages**

The following sample code provides an example on how to send transactional messages:

```
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; use MQ\MQClient; class ProducerTest
```

`{`

```java
    private $client;
```

`p`

```java
ate$c et;
    private $transProducer;
    private $count;
    private $popMsgCount;
    public function __construct()
```

`{`

```
        $this->client = new MQClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
        // The topic to which you want to send messages. The topic is created in the Ap
saraMQ for RocketMQ console.
        $topic = "${TOPIC}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        $groupId = "${GROUP_ID}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        $instanceId = "${INSTANCE_ID}";
        $this->transProducer = $this->client->getTransProducer($instanceId,$topic,
$groupId);
        $this->count = 0;
        $this->popMsgCount = 0;
    function processAckError($e) {
        if ($e instanceof MQ\Exception\AckMessageException) {
            // If a transactional message is not committed or rolled back within the
timeout period specified by the TransCheckImmunityTime parameter or the NextConsumeTime parameter, the commit or rollback operation fails. The TransCheckImmunityTime parameter specifies a timeout period for the handle of transactional messages. The NextConsumeTim e parameter specifies a timeout period for the handle of consumeHalfMessage.
            printf("Commit/Rollback Error, RequestId:%s\n", $e->getRequestId());
            foreach ($e->getAckMessageErrorItems() as $errorItem) {
                printf("\tReceiptHandle:%s, ErrorCode:%s, ErrorMsg:%s\n", $errorItem->ge
tReceiptHandle(), $errorItem->getErrorCode(), $errorItem->getErrorCode());
        } else {
            print_r($e);
```

```
    function consumeHalfMsg() {
        while($this->count < 3 && $this->popMsgCount < 15) {
            $this->popMsgCount++;
            try {
                $messages = $this->transProducer->consumeHalfMessage(4, 3);
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\MessageNotExistException) {
                    print "no half transaction message\n";
                    continue;
                print_r($e->getMessage() . "\n");
                sleep(3);
                continue;
            foreach ($messages as $message) {
                printf("ID:%s TAG:%s BODY:%s \nPublishTime:%d,
FirstConsumeTime:%d\nConsumedTimes:%d, NextConsumeTime:%d\nPropA:%s\n",
                    $message->getMessageId(), $message->getMessageTag(), $message->getMe
ssageBody(),
                    $message->getPublishTime(), $message->getFirstConsumeTime(), $messag
e->getConsumedTimes(), $message->getNextConsumeTime(),
                    $message->getProperty("a"));
                print_r($message->getProperties());
                $propA = $message->getProperty("a");
                $consumeTimes = $message->getConsumedTimes();
                try {
                    if ($propA == "1") {
                        print "\n commit transaction msg: " . $message->getMessageId() .
"\n";
                        $this->transProducer->commit($message->getReceiptHandle());
                        $this->count++;
                    } else if ($propA == "2" && $consumeTimes > 1) {
                        print "\n commit transaction msg: " . $message->getMessageId() .
"\n";
                        $this->transProducer->commit($message->getReceiptHandle());
                        $this->count++;
                    } else if ($propA == "3") {
                        print "\n rollback transaction msg: " . $message->getMessageId()
. "\n";
                        $this->transProducer->rollback($message->getReceiptHandle());
                        $this->count++;
                    } else {
                        print "\n unknown transaction msg: " . $message->getMessageId()
. "\n";
                } catch (\Exception $e) {
                    processAckError($e);
```

```
    public function run()
```

`{`

```
        // Cyclically send four transactional messages.
        for ($i = 0; $i < 4; $i++) {
            $pubMsg = new TopicMessage("hello,mq");
            // The custom property of the message.
            $pubMsg->putProperty("a", $i);
            // The key of the message.
            $pubMsg->setMessageKey("MessageKey");
            // The time interval between the time when the transactional message is
sent and the start time of the first transaction status check. Unit: seconds. Valid val ues: 10 to 300.
            // If the message is not committed or rolled back after the first
transaction status check is performed, the broker initiates a request to check the stat us of the local transaction at an interval of 10 seconds within the next 24 hours.
            $pubMsg->setTransCheckImmunityTime(10);
            $topicMessage = $this->transProducer->publishMessage($pubMsg);
            print "\npublish -> \n\t" . $topicMessage->getMessageId() . " " .
$topicMessage->getReceiptHandle() . "\n";
            if ($i == 0) {
                try {
                    // After the producer sends the transactional message, the broker ob
tains the handle of the half message that corresponds to the transactional message and commits or rolls back the transactional message based on the status of the handle.
                    $this->transProducer->commit($topicMessage->getReceiptHandle());
                    print "\n commit transaction msg when publish: " . $topicMessage->ge
tMessageId() . "\n";
                } catch (\Exception $e) {
                    // If the transactional message is not committed or rolled back befo
re the timeout period specified by the TransCheckImmunityTime parameter elapses, the co mmit or rollback operation fails.
                    processAckError($e);
        // The client needs a thread or a process to process unacknowledged
transactional messages.
        // Process unacknowledged transactional messages.
        $this->consumeHalfMsg();
$instance = new ProducerTest(); $instance->run();
```

?>

**Consume transactional messages**

The following sample code provides an example on how to consume transactional messages:

```
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; use MQ\MQClient; class ConsumerTest
```

`{`

```java
    private $client;
    private $producer;
    public function __construct()
```

`{`

```
        $this->client = new MQClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
        // The topic from which you want to consume messages. The topic is created in t
he ApsaraMQ for RocketMQ console.
        $topic = "${TOPIC}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        $groupId = "${GROUP_ID}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        $instanceId = "${INSTANCE_ID}";
        $this->consumer = $this->client->getConsumer($instanceId, $topic, $groupId);
    public function run()
```

`{`

```
        // Cyclically consume messages in the current thread. We recommend that you use
multiple threads to concurrently consume messages.
        while (True) {
            try {
                // Consume messages in long polling mode.
```

`g` `g``p` `g`

```
                // In long polling mode, if no message in the topic is available for con
sumption, the request is suspended on the broker for a specified period of time. If a m essage becomes available for consumption within this period, the broker immediately sen ds a response to the consumer. In this example, the period is set to 3 seconds.
                $messages = $this->consumer->consumeMessage(
                    3, // The maximum number of messages that can be consumed at a time.
In this example, the value is set to 3. The maximum value that you can specify is 16.
                    3  // The length of a long polling period. Unit: seconds. In this ex
ample, the value is set to 3. The maximum value that you can specify is 30.
```

);

```
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\MessageNotExistException) {
                    // If no message in the topic is available for consumption, the long
polling mode continues to take effect.
                    printf("No message, contine long polling!RequestId:%s\n", $e->getReq
uestId());
                    continue;
                print_r($e->getMessage() . "\n");
                sleep(3);
                continue;
            print "consume finish, messages:\n";
            // Specify the message consumption logic.
            $receiptHandles = array();
            foreach ($messages as $message) {
                $receiptHandles[] = $message->getReceiptHandle();
                printf("MessageID:%s TAG:%s BODY:%s \nPublishTime:%d,
FirstConsumeTime:%d, \nConsumedTimes:%d, NextConsumeTime:%d,MessageKey:%s\n",
                    $message->getMessageId(), $message->getMessageTag(), $message->getMe
ssageBody(),
                    $message->getPublishTime(), $message->getFirstConsumeTime(), $messag
e->getConsumedTimes(), $message->getNextConsumeTime(),
                    $message->getMessageKey());
                print_r($message->getProperties());
            // If the broker does not receive an acknowledgment (ACK) for a message
from the consumer before the period of time specified by $message->getNextConsumeTime() elapses, the broker delivers the message for consumption again.
            // A unique timestamp is specified for the handle of a message each time th
e message is consumed.
            print_r($receiptHandles);
            try {
                $this->consumer->ackMessage($receiptHandles);
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\AckMessageException) {
                    // If the handle of a message times out, the broker cannot receive a
n ACK for the message from the consumer.
                    printf("Ack Error, RequestId:%s\n", $e->getRequestId());
```

```
                    foreach ($e->getAckMessageErrorItems() as $errorItem) {
                        printf("\tReceiptHandle:%s, ErrorCode:%s, ErrorMsg:%s\n", $error
Item->getReceiptHandle(), $errorItem->getErrorCode(), $errorItem->getErrorCode());
            print "ack finish\n";
$instance = new ConsumerTest(); $instance->run();
```

?>

#### C# SDK

##### Prepare the environment

This topic describes how to prepare the environment before you use the HTTP client SDK for C# to send and consume messages.

**Environment requirements**

.NET is installed. For more information, see Install .NET. Visual Studio 2015 or later is installed. For more information, visit the official website of Visual Studio. After .NET is installed, you can run the `dotnet --version` command to check the version of .NET that you installed.

**Install the SDK for C#**

To install the SDK for C#, perform the following steps:
1. Download the SDK for C# and the project file to your on-premises machine and decompress
them. Aliyun_MQ_SDK is the directory where the SDK is located. Aliyun_MQ_SDK.sln is the project file.
2. Use Visual Studio to open the Aliyun_MQ_SDK.sln file and import the file to the
Aliyun_MQ_SDK project.
3. Run the Samples.cs file. In the Aliyun_MQ_SDK project, the Samples.cs file appears. This file
provides the sample code on how to send and consume messages by using the SDK for C#. Replace the values in the sample code with the actual values that are used in your application. Then, save and run the file.

##### Send and consume normal messages

Normal messages are messages that have no special features in ApsaraMQ for RocketMQ. They are different from featured messages, such as scheduled messages, delayed messages, ordered messages, and transactional messages. This topic provides sample code to show how to use the HTTP client SDK for C# to send and consume normal messages.

**Prerequisites**

The following operations are performed: Install the SDK for C#. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send normal messages**

The following sample code provides an example on how to send normal messages:

```
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ.Util; namespace Aliyun.MQ.Sample
```

`{`

```java
    public class ProducerSample
```

`{`

```java
        // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint,
log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click In stances. On the Instances page, select the name of your instance. Then, view the HTTP e ndpoint on the Network Management tab.
        private const string _endpoint = "${HTTP_ENDPOINT}";
        // The AccessKey ID that is used for identity verification. You can obtain the
AccessKey ID in the Apsara Uni-manager Operations Console.
        private const string _accessKeyId = "${ACCESS_KEY}";
        // The AccessKey secret that is used for identity verification. You can obtain
the AccessKey secret in the Apsara Uni-manager Operations Console.
        private const string _secretAccessKey = "${SECRET_KEY}";
        // The topic to which you want to send messages. The topic is created in the Ap
saraMQ for RocketMQ console.
        private const string _topicName = "${TOPIC}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        private const string _instanceId = "${INSTANCE_ID}";
        private static MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        static MQProducer producer = client.GetProducer(instanceId, topicName);
```

`p` `_` `_` `,``_` `p`

```
        static void Main(string[] args)
```

`{`

```
            try
```

`{`

```
                // Cyclically send four messages.
                for (int i = 0; i < 4; i++)
```

`{`

```
    TopicMessage sendMsg;
                // The content of the message.
                sendMsg = new TopicMessage("hello mq");
                // The custom property of the message.
                sendMsg.PutProperty("a", i.ToString());
                // The key of the message.
                sendMsg.MessageKey = "MessageKey";
                TopicMessage result = producer.PublishMessage(sendMsg);
                Console.WriteLine("publis message success:" + result);
            catch (Exception ex)
```

`{`

```
                Console.Write(ex);
```

**Consume normal messages**

The following sample code provides an example on how to consume normal messages:

```
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ; namespace Aliyun.MQ.Sample
```

`{`

```java
    public class ConsumerSample
```

`{`

```java
        // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint,
log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click In stances. On the Instances page, select the name of your instance. Then, view the HTTP e ndpoint on the Network Management tab.
        private const string _endpoint = "${HTTP_ENDPOINT}";
        // The AccessKey ID that is used for identity verification. You can obtain the
AccessKey ID in the Apsara Uni-manager Operations Console.
        private const string _accessKeyId = "${ACCESS_KEY}";
        // The AccessKey secret that is used for identity verification. You can obtain
the AccessKey secret in the Apsara Uni-manager Operations Console.
        private const string _secretAccessKey = "${SECRET_KEY}";
```

```java
        // The topic from which you want to consume messages. The topic is created in t
he ApsaraMQ for RocketMQ console.
        private const string _topicName = "${TOPIC}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        private const string _instanceId = "${INSTANCE_ID}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        private const string _groupId = "${GROUP_ID}";
        private static MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        static MQConsumer consumer = _client.GetConsumer(_instanceId, _topicName, _grou
pId, null);
        static void Main(string[] args)
```

`{`

```
            // Cyclically consume messages in the current thread. We recommend that you
use multiple threads to concurrently consume messages.
            while (true)
```

`{`

```
                try
```

`{`

```
                    // Consume messages in long polling mode.
                    // In long polling mode, if no message in the topic is available for
consumption, the request is suspended on the broker for a specified period of time. If a message becomes available for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
                    List<Message> messages = null;
                    try
```

`{`

```
                        messages = consumer.ConsumeMessage(
                            3, // The maximum number of messages that can be consumed at
a time. In this example, the value is set to 3. The maximum value that you can specify is 16.
                            3  // The length of a long polling period. Unit: seconds. In
this example, the value is set to 3. The maximum value that you can specify is 30.
```

);

```
                    catch (Exception exp1)
```

`{`

```
                        if (exp1 is MessageNotExistException)
```

`{`

```
                            Console.WriteLine(Thread.CurrentThread.Name + " No new messa
ge, " + ((MessageNotExistException)exp1).RequestId);
                            continue;
                        Console.WriteLine(exp1);
                        Thread.Sleep(2000);
```

```
                    if (messages == null)
```

`{`

```
                        continue;
                    List<string> handlers = new List<string>();
                    Console.WriteLine(Thread.CurrentThread.Name + " Receive Messages:");
                    // Specify the message consumption logic.
                    foreach (Message message in messages)
```

`{`

```
                        Console.WriteLine(message);
                        Console.WriteLine("Property a is:" + message.GetProperty("a"));
                        handlers.Add(message.ReceiptHandle);
                    // If the broker does not receive an acknowledgment (ACK) for a mess
age from the consumer before the period of time specified by Message.nextConsumeTime el apses, the broker delivers the message for consumption again.
                    // A unique timestamp is specified for the handle of a message each
time the message is consumed.
                    try
```

`{`

```
                        consumer.AckMessage(handlers);
                        Console.WriteLine("Ack message success:");
                        foreach (string handle in handlers)
```

`{`

```
                            Console.Write("\t" + handle);
                        Console.WriteLine();
                    catch (Exception exp2)
```

`{`

```
                        // If the handle of a message times out, the broker cannot recei
ve an ACK for the message from the consumer.
                        if (exp2 is AckMessageException)
```

`{`

```
                            AckMessageException ackExp = (AckMessageException)exp2;
                            Console.WriteLine("Ack message fail, RequestId:" +
ackExp.RequestId);
                            foreach (AckMessageErrorItem errorItem in ackExp.ErrorItems)
```

`{`

```
                                Console.WriteLine("\tErrorHandle:" +
errorItem.ReceiptHandle + ",ErrorCode:" + errorItem.ErrorCode + ",ErrorMsg:" + errorIte m.ErrorMessage);
                catch (Exception ex)
```

`{`

```
                    Console.WriteLine(ex);
                    Thread.Sleep(2000);
```

##### Send and consume ordered messages

Ordered messages are a type of message that is published and consumed in a strict order. Ordered messages in ApsaraMQ for RocketMQ are also known as first-in-first-out (FIFO) messages. This topic provides sample code to show how to use the HTTP client SDK for C# to send and consume ordered messages.

**Background information**

Ordered messages are classified into the following types: Globally ordered message: All messages in a specified topic are published and consumed in first-in-first-out (FIFO) order. Partitionally ordered message: All messages in a specified topic are distributed to different partitions by using shard keys. The messages in each partition are published and consumed in FIFO order. A Sharding Key is a key field that is used for ordered messages to identify different partitions. The Sharding Key is different from the key of a normal message. For more information about the message routing feature, see Ordered messages.

**Prerequisites**

The following operations are performed: Install the SDK for C#. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send ordered messages**

The following sample code provides an example on how to send ordered messages:

```
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ.Util; namespace Aliyun.MQ.Sample
```

`{`

```java
    public class OrderProducerSample
```

`{`

```java
        // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint,
log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click In stances. On the Instances page, select the name of your instance. Then, view the HTTP e ndpoint on the Network Management tab.
        private const string _endpoint = "${HTTP_ENDPOINT}";
        // The AccessKey ID that is used for identity verification. You can obtain the
AccessKey ID in the Apsara Uni-manager Operations Console. privateconststring accessKeyId="${ACCESSKEY}";
```

```java
        private const string _accessKeyId  ${ACCESS_KEY};
        // The AccessKey secret that is used for identity verification. You can obtain
the AccessKey secret in the Apsara Uni-manager Operations Console.
        private const string _secretAccessKey = "${SECRET_KEY}";
        // The topic to which you want to send messages. The topic is created in the Ap
saraMQ for RocketMQ console.
        private const string _topicName = "${TOPIC}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        private const string _instanceId = "${INSTANCE_ID}";
        private static MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        static MQProducer producer = _client.GetProducer(_instanceId, _topicName);
        static void Main(string[] args)
```

`{`

```
            try
```

`{`

```
                // Cyclically send eight messages.
                for (int i = 0; i < 8; i++)
```

`{`

```
                    // The content and tag of the message.
                    TopicMessage sendMsg = new TopicMessage("hello mq", "tag");
                    // The custom property of the message.
                    sendMsg.PutProperty("a", i.ToString());
                    // The shard key that is used to distribute ordered messages to a sp
ecific partition. Shard keys can be used to identify different partitions. A shard key is different from a message key.
                    sendMsg.ShardingKey = (i % 2).ToString();
                    TopicMessage result = producer.PublishMessage(sendMsg);
                    Console.WriteLine("publis message success:" + result);
            catch (Exception ex)
```

`{`

```
                Console.Write(ex);
```

**Consume ordered messages**

The following sample code provides an example on how to consume ordered messages:

```
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model;
```

```
using Aliyun.MQ.Model.Exp; using Aliyun.MQ; namespace Aliyun.MQ.Sample
```

`{`

```java
    public class OrderConsumerSample
```

`{`

```java
        // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint,
log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click In stances. On the Instances page, select the name of your instance. Then, view the HTTP e ndpoint on the Network Management tab.
        private const string _endpoint = "${HTTP_ENDPOINT}";
        // The AccessKey ID that is used for identity verification. You can obtain the
AccessKey ID in the Apsara Uni-manager Operations Console.
        private const string _accessKeyId = "${ACCESS_KEY}";
        // The AccessKey secret that is used for identity verification. You can obtain
the AccessKey secret in the Apsara Uni-manager Operations Console.
        private const string _secretAccessKey = "${SECRET_KEY}";
        // The topic from which you want to consume messages. The topic is created in t
he ApsaraMQ for RocketMQ console.
        private const string _topicName = "${TOPIC}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        private const string _groupId = "${GROUP_ID}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le. private const string _instanceId = "${INSTANCE_ID}";
        private static MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        static MQConsumer consumer = _client.GetConsumer(_instanceId, _topicName, _grou
pId, null);
        static void Main(string[] args)
```

`{`

```
            // Cyclically consume messages in the current thread. We recommend that you
use multiple threads to concurrently consume messages.
            while (true)
```

`{`

```
                try
```

`{`

```
                    // Consume messages in long polling mode. The consumer may pull part
itionally ordered messages from multiple partitions. The consumer consumes messages from the same partition in the order in which the messages are sent.
                    // A consumer pulls partitionally ordered messages from a partition.
If the broker does not receive an acknowledgment (ACK) for a message after the message is consumed, the consumer consumes the message again.
                    // The consumer can consume the next batch of messages from a partit
ion only after all messages that are pulled from the partition in the previous batch ar e acknowledged to be consumed.
                    // In long polling mode, if no message in the topic is available for
```

```
consumption, the request is suspended on the broker for a specified period of time. If a message becomes available for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
                    List<Message> messages = null;
                    try
```

`{`

```
                        messages = consumer.ConsumeMessageOrderly(
                            3, // The maximum number of messages that can be consumed at
a time. In this example, the value is set to 3. The maximum value that you can specify is 16.
                            3 // The length of a long polling period. Unit: seconds. In
this example, the value is set to 3. The maximum value that you can specify is 30.
```

);

```
                    catch (Exception exp1)
```

`{`

```
                        if (exp1 is MessageNotExistException)
```

`{`

```
                            Console.WriteLine(Thread.CurrentThread.Name + " No new messa
ge, " + ((MessageNotExistException)exp1).RequestId);
                            continue;
                        Console.WriteLine(exp1);
                        Thread.Sleep(2000);
                    if (messages == null)
```

`{`

```
                        continue;
                    List<string> handlers = new List<string>();
                    Console.WriteLine(Thread.CurrentThread.Name + " Receive Messages:");
                    // Specify the message consumption logic.
                    foreach (Message message in messages)
```

`{`

```
                        Console.WriteLine(message);
                        Console.WriteLine("Property a is:" + message.GetProperty("a"));
                        handlers.Add(message.ReceiptHandle);
                    // If the broker does not receive an ACK for a message from the cons
umer before the period of time specified by Message.nextConsumeTime elapses, the broker delivers the message for consumption again.
                    // A unique timestamp is specified for the handle of a message each
time the message is consumed.
                    try
```

`{`

```
                        consumer.AckMessage(handlers);
                        Console.WriteLine("Ack message success:");
                        foreach (string handle in handlers)
```

`{`

```
                            Console.Write("\t" + handle);
```

```
                        Console.WriteLine();
                    catch (Exception exp2)
```

`{`

```
                        // If the handle of a message times out, the broker cannot recei
ve an ACK for the message from the consumer.
                        if (exp2 is AckMessageException)
```

`{`

```
                            AckMessageException ackExp = (AckMessageException)exp2;
                            Console.WriteLine("Ack message fail, RequestId:" +
ackExp.RequestId);
                            foreach (AckMessageErrorItem errorItem in ackExp.ErrorItems)
```

`{`

```
                                Console.WriteLine("\tErrorHandle:" +
errorItem.ReceiptHandle + ",ErrorCode:" + errorItem.ErrorCode + ",ErrorMsg:" + errorIte m.ErrorMessage);
                catch (Exception ex)
```

`{`

```
                    Console.WriteLine(ex);
                    Thread.Sleep(2000);
```

##### Send and consume scheduled messages

**and delayed messages**

This topic provides sample code to show how to use the HTTP client SDK for C# to send and consume scheduled messages and delayed messages.

**Background information**

Delayed message: The producer sends the message to the ApsaraMQ for RocketMQ server, but does not expect the message to be delivered immediately. Instead, the message is delivered to the consumer for consumption after a certain period of time. This message is a delayed message. Scheduled message: A producer sends a message to a ApsaraMQ for RocketMQ broker and expects the message to be delivered to a consumer at a specified point in time. This type of message is called a scheduled message. If an HTTP client SDK is used, the code configurations of scheduled messages are the same as the code configurations of delayed messages. Both types of messages are delivered to consumers after a specific period of time based on the attributes of the messages. For more information about the message routing feature, see Scheduled messages and delayed messages.

**Prerequisites**

The following operations are performed: Install the SDK for C#. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send scheduled messages or delayed messages**

The following sample code provides an example on how to send scheduled messages or delayed messages:

```
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ.Util; namespace Aliyun.MQ.Sample
```

`{`

```java
    public class ProducerSample
```

`{`

```java
        // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint,
log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click In stances. On the Instances page, select the name of your instance. Then, view the HTTP e ndpoint on the Network Management tab.
        private const string _endpoint = "${HTTP_ENDPOINT}";
        // The AccessKey ID that is used for identity verification. You can obtain the
AccessKey ID in the Apsara Uni-manager Operations Console.
        private const string _accessKeyId = "${ACCESS_KEY}";
        // The AccessKey secret that is used for identity verification. You can obtain
the AccessKey secret in the Apsara Uni-manager Operations Console.
        private const string _secretAccessKey = "${SECRET_KEY}";
        // The topic to which you want to send messages. The topic is created in the Ap
saraMQ for RocketMQ console.
        private const string _topicName = "${TOPIC}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        private const string _instanceId = "${INSTANCE_ID}";
        private static MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        static MQProducer producer = _client.GetProducer(_instanceId, _topicName);
        static void Main(string[] args)
```

`{`

```
            try
```

`{`

```
                // Cyclically send four messages.
                for (int i = 0; i < 4; i++)
```

`{`

```
                    TopicMessage sendMsg;
                    // The content of the message.
                    sendMsg = new TopicMessage("hello mq");
                    // The custom property of the message.
                    sendMsg.PutProperty("a", i.ToString());
                    // The period of time after which the broker delivers the message. I
n this example, when the broker receives a message, the broker waits for 10 seconds bef ore it delivers the message to the consumer. Set this parameter to a timestamp in milli seconds.
                    // If the producer sends a scheduled message, set the parameter to t
he time interval between the scheduled point in time and the current point in time.
                    sendMsg.StartDeliverTime = AliyunSDKUtils.GetNowTimeStamp() + 10 * 1
000;
                    TopicMessage result = producer.PublishMessage(sendMsg);
                    Console.WriteLine("publis message success:" + result);
            catch (Exception ex)
```

`{`

```
                Console.Write(ex);
```

**Consume scheduled messages or delayed messages**

The following sample code provides an example on how to consume scheduled messages or delayed messages:

```
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ; namespace Aliyun.MQ.Sample
```

`{`

```java
    public class ConsumerSample
```

`{`

```java
        // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint,
log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click In stances. On the Instances page, select the name of your instance. Then, view the HTTP e ndpoint on the Network Management tab.
        private const string _endpoint = "${HTTP_ENDPOINT}";
        // The AccessKey ID that is used for identity verification. You can obtain the
AccessKey ID in the Apsara Uni-manager Operations Console. privateconststring accessKeyId="${ACCESSKEY}";
```

```java
        private const string _accessKeyId = ${ACCESS_KEY};
        // The AccessKey secret that is used for identity verification. You can obtain
the AccessKey secret in the Apsara Uni-manager Operations Console.
        private const string _secretAccessKey = "${SECRET_KEY}";
        // The topic from which you want to consume messages. The topic is created in t
he ApsaraMQ for RocketMQ console.
        private const string _topicName = "${TOPIC}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        private const string _instanceId = "${INSTANCE_ID}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        private const string _groupId = "${GROUP_ID}";
        private static MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        static MQConsumer consumer = _client.GetConsumer(_instanceId, _topicName, _grou
pId, null);
        static void Main(string[] args)
```

`{`

```
            // Cyclically consume messages in the current thread. We recommend that you
use multiple threads to concurrently consume messages.
            while (true)
```

`{`

```
                try
```

`{`

```
                    // Consume messages in long polling mode.
                    // In long polling mode, if no message in the topic is available for
consumption, the request is suspended on the broker for a specified period of time. If a message becomes available for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
                    List<Message> messages = null;
                    try
```

`{`

```
                        messages = consumer.ConsumeMessage(
                            3, // The maximum number of messages that can be consumed at
a time. In this example, the value is set to 3. The maximum value that you can specify is 16.
                            3  // The length of a long polling period. Unit: seconds. In
this example, the value is set to 3. The maximum value that you can specify is 30.
```

);

```
                    catch (Exception exp1)
```

`{`

```
                        if (exp1 is MessageNotExistException)
```

`{`

```
                            Console.WriteLine(Thread.CurrentThread.Name + " No new messa
ge, " + ((MessageNotExistException)exp1).RequestId);
                            continue;
```

```
                        Console.WriteLine(exp1);
                        Thread.Sleep(2000);
                    if (messages == null)
```

`{`

```
                        continue;
                    List<string> handlers = new List<string>();
                    Console.WriteLine(Thread.CurrentThread.Name + " Receive Messages:");
                    // Specify the message consumption logic.
                    foreach (Message message in messages)
```

`{`

```
                        Console.WriteLine(message);
                        Console.WriteLine("Property a is:" + message.GetProperty("a"));
                        handlers.Add(message.ReceiptHandle);
                    // If the broker does not receive an acknowledgment (ACK) for a mess
age from the consumer before the period of time specified by Message.nextConsumeTime el apses, the broker delivers the message for consumption again.
                    // A unique timestamp is specified for the handle of a message each
time the message is consumed.
                    try
```

`{`

```
                        consumer.AckMessage(handlers);
                        Console.WriteLine("Ack message success:");
                        foreach (string handle in handlers)
```

`{`

```
                            Console.Write("\t" + handle);
                        Console.WriteLine();
                    catch (Exception exp2)
```

`{`

```
                        // If the handle of a message times out, the broker cannot recei
ve an ACK for the message from the consumer.
                        if (exp2 is AckMessageException)
```

`{`

```
                            AckMessageException ackExp = (AckMessageException)exp2;
                            Console.WriteLine("Ack message fail, RequestId:" +
ackExp.RequestId);
                            foreach (AckMessageErrorItem errorItem in ackExp.ErrorItems)
```

`{`

```
                                Console.WriteLine("\tErrorHandle:" +
errorItem.ReceiptHandle + ",ErrorCode:" + errorItem.ErrorCode + ",ErrorMsg:" + errorIte m.ErrorMessage);
                catch (Exception ex)
```

`{`

```
                    Console.WriteLine(ex);
```

```
                    Thread.Sleep(2000);
```

##### Send and consume transactional messages

ApsaraMQ for RocketMQ provides a distributed transaction processing feature that is similar to X/Open XA. ApsaraMQ for RocketMQ uses transactional messages to ensure transactional consistency. This topic provides sample code to show how to use the HTTP client SDK for C# to send and consume transactional messages.

**Background information**

The following figure shows the interaction process of transactional messages. For more information about the message routing feature, see Transactional messages.

**Prerequisites**

The following operations are performed: Install the SDK for C#. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send transactional messages**

The following sample code provides an example on how to send transactional messages:

```
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ.Util; namespace Aliyun.MQ.Sample
```

`{`

```
publicclassTransProducerSample
```

```java
    public class TransProducerSample
```

`{`

```java
        // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint,
log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click In stances. On the Instances page, select the name of your instance. Then, view the HTTP e ndpoint on the Network Management tab.
        private const string _endpoint = "${HTTP_ENDPOINT}";
        // The AccessKey ID that is used for identity verification. You can obtain the
AccessKey ID in the Apsara Uni-manager Operations Console.
        private const string _accessKeyId = "${ACCESS_KEY}";
        // The AccessKey secret that is used for identity verification. You can obtain
the AccessKey secret in the Apsara Uni-manager Operations Console.
        private const string _secretAccessKey = "${SECRET_KEY}";
        // The topic to which you want to send messages. The topic is created in the Ap
saraMQ for RocketMQ console.
        private const string _topicName = "${TOPIC}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        private const string _instanceId = "${INSTANCE_ID}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        private const string _groupId = "${GROUP_ID}";
        private static readonly MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        private static readonly MQTransProducer transProducer =
_client.GetTransProdcuer(_instanceId, _topicName, _groupId);
        static void ProcessAckError(Exception exception)
```

`{`

```
            // If a transactional message is not committed or rolled back before the
timeout period specified by the TransCheckImmunityTime parameter for the handle of the transactional message elapses or before the timeout period specified for the handle of consumeHalfMessage elapses, the commit or rollback operation fails. In this example, th e timeout period for the handle of consumeHalfMessage is 10 seconds.
            if (exception is AckMessageException)
```

`{`

```
                AckMessageException ackExp = (AckMessageException)exception;
                Console.WriteLine("Ack message fail, RequestId:" + ackExp.RequestId);
                foreach (AckMessageErrorItem errorItem in ackExp.ErrorItems)
```

`{`

```
                    Console.WriteLine("\tErrorHandle:" + errorItem.ReceiptHandle + ",Err
orCode:" + errorItem.ErrorCode + ",ErrorMsg:" + errorItem.ErrorMessage);
        static void ConsumeHalfMessage()
```

`{`

```
            int count = 0;
            while (true)
```

`{`

```
                if (count == 3)
                    break;
                try
```

`{`

```
                    // Check the status of half messages. This process is similar to con
suming normal messages.
                    List<Message> messages = null;
                    try
```

`{`

```
                        messages = transProducer.ConsumeHalfMessage(3, 3);
                    } catch (Exception exp1) {
                        if (exp1 is MessageNotExistException)
```

`{`

```
                            Console.WriteLine(Thread.CurrentThread.Name + " No half mess
age, " + ((MessageNotExistException)exp1).RequestId);
                            continue;
                        Console.WriteLine(exp1);
                        Thread.Sleep(2000);
                    if (messages == null)
                        continue;
                    // Specify the business processing logic.
                    foreach (Message message in messages)
```

`{`

```
                        Console.WriteLine(message);
                        int a = int.Parse(message.GetProperty("a"));
                        uint consumeTimes = message.ConsumedTimes;
                        try {
                            if (a == 1) {
                                // Confirm to commit the transactional message.
                                transProducer.Commit(message.ReceiptHandle);
                                count++;
                                Console.WriteLine("Id:" + message.Id + ", commit");
                            } else if (a == 2 && consumeTimes > 1) {
                                // Confirm to commit the transactional message.
                                transProducer.Commit(message.ReceiptHandle);
                                count++;
                                Console.WriteLine("Id:" + message.Id + ", commit");
                            } else if (a == 3) {
                                // Confirm to roll back the transactional message.
                                transProducer.Rollback(message.ReceiptHandle);
                                count++;
                                Console.WriteLine("Id:" + message.Id + ", rollback");
                            } else {
                                // Do not perform operations. Check the status next
time.
                                Console.WriteLine("Id:" + message.Id + ", unkonwn");
                        } catch (Exception ackError) {
                            ProcessAckError(ackError);
```

```
                catch (Exception ex)
```

`{`

```
                    Console.WriteLine(ex);
                    Thread.Sleep(2000);
        static void Main(string[] args)
```

`{`

```
            // The client needs a thread or a process to process unacknowledged
transactional messages.
            // Start a thread to process unacknowledged transactional messages.
            Thread consumeHalfThread = new Thread(ConsumeHalfMessage);
            consumeHalfThread.Start();
            try
```

`{`

```
                // Cyclically send four transactional messages. Among the four messages,
commit the first message after the message is sent, and process the other three message s based on the specified conditions.
                for (int i = 0; i < 4; i++)
```

`{`

```
                    TopicMessage sendMsg = new TopicMessage("trans_msg");
                    sendMsg.MessageTag = "a";
                    sendMsg.MessageKey = "MessageKey";
                    sendMsg.PutProperty("a", i.ToString());
                    // The time interval between the time when the transactional message
is sent and the start time of the first transaction status check. Unit: seconds. Valid values: 10 to 300.
                    // If the message is not committed or rolled back after the first tr
ansaction status check is performed, the broker initiates a request to check the status of the local transaction at an interval of 10 seconds within the next 24 hours.
                    sendMsg.TransCheckImmunityTime = 10;
                    TopicMessage result = transProducer.PublishMessage(sendMsg);
                    Console.WriteLine("publis message success:" + result);
                    try {
                        if (!string.IsNullOrEmpty(result.ReceiptHandle) && i == 0)
```

`{`

```
                            // After the producer sends the transactional message, the b
roker obtains the handle of the half message that corresponds to the transactional mess age and commits or rolls back the transactional message based on the status of the hand le.
                            transProducer.Commit(result.ReceiptHandle);
                            Console.WriteLine("Id:" + result.Id + ", commit");
                    } catch (Exception ackError) {
                        ProcessAckError(ackError);
            } catch (Exception ex) {
```

```
                Console.Write(ex);
            consumeHalfThread.Join();
```

**Consume transactional messages**

The following sample code provides an example on how to consume transactional messages:

```
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ; namespace Aliyun.MQ.Sample
```

`{`

```java
    public class ConsumerSample
```

`{`

```java
        // The HTTP endpoint to which you want to connect. To obtain the HTTP endpoint,
log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click In stances. On the Instances page, select the name of your instance. Then, view the HTTP e ndpoint on the Network Management tab.
        private const string _endpoint = "${HTTP_ENDPOINT}";
        // The AccessKey ID that is used for identity verification. You can obtain the
AccessKey ID in the Apsara Uni-manager Operations Console.
        private const string _accessKeyId = "${ACCESS_KEY}";
        // The AccessKey secret that is used for identity verification. You can obtain
the AccessKey secret in the Apsara Uni-manager Operations Console.
        private const string _secretAccessKey = "${SECRET_KEY}";
        // The topic from which you want to consume messages. The topic is created in t
he ApsaraMQ for RocketMQ console.
        private const string _topicName = "${TOPIC}";
        // The ID of the instance to which the topic belongs. The instance is created i
n the ApsaraMQ for RocketMQ console.
        // If the instance has a namespace, specify the ID of the instance. If the inst
ance does not have a namespace, set the instance ID to null or an empty string. You can check whether your instance has a namespace on the Instances page in the RocketMQ conso le.
        private const string _instanceId = "${INSTANCE_ID}";
        // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
        private const string _groupId = "${GROUP_ID}";
        private static MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        static MQConsumer consumer = _client.GetConsumer(_instanceId, _topicName, _grou
pId, null);
        static void Main(string[] args)
```

`{`

```
//Cclicall consmemessagesinthecrrentthread Werecommendthat
```

`o`

```
            // Cyclically consume messages in the current thread. We recommend that you
use multiple threads to concurrently consume messages.
            while (true)
```

`{`

```
                try
```

`{`

```
                    // Consume messages in long polling mode.
                    // In long polling mode, if no message in the topic is available for
consumption, the request is suspended on the broker for a specified period of time. If a message becomes available for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
                    List<Message> messages = null;
                    try
```

`{`

```
                        messages = consumer.ConsumeMessage(
                            3, // The maximum number of messages that can be consumed at
a time. In this example, the value is set to 3. The maximum value that you can specify is 16.
                            3  // The length of a long polling period. Unit: seconds. In
this example, the value is set to 3. The maximum value that you can specify is 30.
```

);

```
                    catch (Exception exp1)
```

`{`

```
                        if (exp1 is MessageNotExistException)
```

`{`

```
                            Console.WriteLine(Thread.CurrentThread.Name + " No new messa
ge, " + ((MessageNotExistException)exp1).RequestId);
                            continue;
                        Console.WriteLine(exp1);
                        Thread.Sleep(2000);
                    if (messages == null)
```

`{`

```
                        continue;
                    List<string> handlers = new List<string>();
                    Console.WriteLine(Thread.CurrentThread.Name + " Receive Messages:");
                    // Specify the message consumption logic.
                    foreach (Message message in messages)
```

`{`

```
                        Console.WriteLine(message);
                        Console.WriteLine("Property a is:" + message.GetProperty("a"));
                        handlers.Add(message.ReceiptHandle);
                    // If the broker does not receive an acknowledgment (ACK) for a mess
age from the consumer before the period of time specified by Message.nextConsumeTime el apses, the broker delivers the message for consumption again.
                    // A unique timestamp is specified for the handle of a message each
time the message is consumed. try
```

```
                    try
```

`{`

```
                        consumer.AckMessage(handlers);
                        Console.WriteLine("Ack message success:");
                        foreach (string handle in handlers)
```

`{`

```
                            Console.Write("\t" + handle);
                        Console.WriteLine();
                    catch (Exception exp2)
```

`{`

```
                        // If the handle of a message times out, the broker cannot recei
ve an ACK for the message from the consumer.
                        if (exp2 is AckMessageException)
```

`{`

```
                            AckMessageException ackExp = (AckMessageException)exp2;
                            Console.WriteLine("Ack message fail, RequestId:" +
ackExp.RequestId);
                            foreach (AckMessageErrorItem errorItem in ackExp.ErrorItems)
```

`{`

```
                                Console.WriteLine("\tErrorHandle:" +
errorItem.ReceiptHandle + ",ErrorCode:" + errorItem.ErrorCode + ",ErrorMsg:" + errorIte m.ErrorMessage);
                catch (Exception ex)
```

`{`

```
                    Console.WriteLine(ex);
                    Thread.Sleep(2000);
```

#### C++ SDK

##### Prepare the environment

This topic describes how to prepare the environment before you use the HTTP client SDK for C++ to send and consume messages.

**Environment requirements**

SCons is installed. For more information, visit the official website of SCons. Before you can use SCons, make sure that Python 3.5 or later is installed. For more information, visit the official website of Python. Visual Studio 2015 or later is installed. For more information, visit the official website of Visual Studio.

**Note**

Visual Studio is required only in Windows environments. In this topic, Visual Studio 2019 is used in the example.

**Install the SDK for C++ in a Windows environment**

1. Download the SDK for C++ to your on-premises machine and decompress the package. For
more information about the download link to the SDK, see Overview.
2. In the SDK directory, run the following command to compile your C++ project:

```
scons
```

3. After the project is compiled, copy the include and lib folders in the SDK directory to the
C++ project directory that you created on your on-premises machine.
4. Configure project properties in Visual Studio. Right-click your project and select
**Properties**.

**Set the Additional Include Directories property**

In the Property Pages dialog box of your project, choose **Configuration Properties >**
**C/C++ > General** in the left-side navigation pane. On the right side, set **Additional**
**Include Directories** to the path of the include folder that you copied in Step 3.

**Set the Additional Library Directories property**

In the Property Pages dialog box of your project, choose **Configuration Properties >**
**Linker > General** in the left-side navigation pane. On the right side, set **Additional**
**Library Directories** to the path of the lib folder that you copied in Step 3 and the path of
the lib\windows\ {Platform directory} folder. Configure the {Platform directory} variable based on the OS that you use. If you use a 64-bit OS, set this variable to AMD64. If you use a 32-bit OS, set this variable to I386.

**Set the Additional Dependencies property**

In the Property Pages dialog box of your project, choose **Configuration Properties >**
**Linker > Input** in the left-side navigation pane. On the right side, add the following
content to the **Additional Dependencies** field:

```
mqcpp.lib libcurl.lib libcurl_debug.lib libeay32MT.lib libeay32MTd.lib ssleay32MT.lib ssleay32MTd.lib DbgHelp.lib User32.lib GDI32.lib Advapi32.lib
```

5. Copy the sample code to the project file, change the parameter values based on the
comments in the code, and then save the changes. For more information about the sample code, see Sample code.
6. Click the
icon to compile the project.

**Install the SDK for C++ in a Linux environment**

**Note**

The following procedure provides an example on how to install the SDK for C++ in CentOS.
1. Download the SDK for C++ to your on-premises machine and decompress the package. For
more information about the download link to the SDK, see Overview.
2. Run the following commands to install the `libcurl-devel` and `openssl-devel` libraries:

```bash
yum install libcurl-devel yum install openssl-devel
```

3. In the SDK directory, run the following command to compile your C++ project:

```
scons
```

4. After the project is compiled, copy the include and lib folders in the SDK directory to the
C++ project directory that you created on your on-premises machine.
5. Copy the sample code to the project file on your on-premises machine, change the
parameter values based on the comments in the code, and then save the changes. For more information about the sample code, see Sample code.
6. Run the following command to compile the project:

```bash
# Replace producer.cpp with the name of the project file that you created on your on-
premises machine. g++ producer.cpp -o producer lib/libmqcpp.a -I include/ -lcurl -lcrypto
```

##### Send and consume normal messages

Normal messages are messages that have no special features in ApsaraMQ for RocketMQ. They are different from featured messages, such as scheduled messages, delayed messages, ordered messages, and transactional messages. This topic provides sample code to show how to use the HTTP client SDK for C++ to send and consume normal messages.

**Prerequisites**

The following operations are performed: Install the SDK for C++. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send normal messages**

The following sample code provides an example on how to send normal messages:

```
#include <fstream>
#include <time.h>
#include "mq_http_sdk/mq_client.h"
using namespace std; using namespace mq::http::sdk; int main() {
    MQClient mqClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
    // The topic to which you want to send messages. The topic is created in the Apsara
MQ for RocketMQ console.
    string topic = "${TOPIC}";
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
```

`//` `t``e`

```
stace asa aespace,spec yte
```

`o` `t``e`

```
stace.
```

`t``e`

```
stace does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    string instanceId = "${INSTANCE_ID}";
    MQProducerPtr producer;
    if (instanceId == "") {
        producer = mqClient.getProducerRef(topic);
    } else {
        producer = mqClient.getProducerRef(instanceId, topic);
    try {
        // Cyclically send four messages.
        for (int i = 0; i < 4; i++)
```

`{`

```
            PublishMessageResponse pmResp;
            // The content of the message.
            TopicMessage pubMsg("Hello, mq!have key!");
            // The custom property of the message.
            pubMsg.putProperty("a",std::to_string(i));
            // The key of the message.
            pubMsg.setMessageKey("MessageKey" + std::to_string(i));
            producer->publishMessage(pubMsg, pmResp);
            cout << "Publish mq message success. Topic is: " << topic
                << ", msgId is:" << pmResp.getMessageId()
                << ", bodyMD5 is:" << pmResp.getMessageBodyMD5() << endl;
    } catch (MQServerException& me) {
        cout << "Request Failed: " + me.GetErrorCode() << ", requestId is:" <<
me.GetRequestId() << endl;
        return -1;
    } catch (MQExceptionBase& mb) {
        cout << "Request Failed: " + mb.ToString() << endl;
        return -2;
    return 0;
```

**Consume normal messages**

The following sample code provides an example on how to consume normal messages:

```
#include <vector>
#include <fstream>
#include "mq_http_sdk/mq_client.h"
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif
```

```
using namespace std; using namespace mq::http::sdk; int main() {
    MQClient mqClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
    // The topic from which you want to consume messages. The topic is created in the A
psaraMQ for RocketMQ console.
    string topic = "${TOPIC}";
    // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
    string groupId = "${GROUP_ID}";
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    string instanceId = "${INSTANCE_ID}";
    MQConsumerPtr consumer;
    if (instanceId == "") {
        consumer = mqClient.getConsumerRef(topic, groupId);
    } else {
        consumer = mqClient.getConsumerRef(instanceId, topic, groupId, "");
    do {
        try {
            std::vector<Message> messages;
            // Consume messages in long polling mode.
            // In long polling mode, if no message in the topic is available for consump
tion, the request is suspended on the broker for a specified period of time. If a messa ge becomes available for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
            consumer->consumeMessage(
                    3, // The maximum number of messages that can be consumed at a time.
In this example, the value is set to 3. The maximum value that you can specify is 16.
                    3, // The length of a long polling period. Unit: seconds. In this ex
ample, the value is set to 3. The maximum value that you can specify is 30.
                    messages
```

);

```
            cout << "Consume: " << messages.size() << " Messages!" << endl;
            // Specify the message consumption logic.
            std::vector<std::string> receiptHandles;
            for (std::vector<Message>::iterator iter = messages.begin();
                    iter != messages.end(); ++iter)
```

`{`

```
                cout << "MessageId: " << iter->getMessageId()
                    << " PublishTime: " << iter->getPublishTime()
                    << " Tag: " << iter->getMessageTag()
                    << " Body: " << iter->getMessageBody()
                    << " FirstConsumeTime: " << iter->getFirstConsumeTime()
                    << " NextConsumeTime: " << iter->getNextConsumeTime()
                    << " ConsumedTimes: " << iter->getConsumedTimes()
                    << " Properties: " << iter->getPropertiesAsString()
                    << " Key: " << iter->getMessageKey() << endl;
                receiptHandles.push_back(iter->getReceiptHandle());
            // Obtain an acknowledgment (ACK) from the consumer.
            // If the broker does not receive an ACK for a message from the consumer be
fore the period of time that is specified by the Message.NextConsumeTime parameter elap ses, the broker delivers the message for consumption again.
            // A unique timestamp is specified for the handle of a message each time th
e message is consumed.
            AckMessageResponse bdmResp;
            consumer->ackMessage(receiptHandles, bdmResp);
            if (!bdmResp.isSuccess()) {
                // If the handle of a message times out, the broker cannot receive an AC
K for the message from the consumer.
                const std::vector<AckMessageFailedItem>& failedItems =
                    bdmResp.getAckMessageFailedItem();
                for (std::vector<AckMessageFailedItem>::const_iterator iter = failedItem
s.begin();
                        iter != failedItems.end(); ++iter)
```

`{`

```
                    cout << "AckFailedItem: " << iter->errorCode
                        << "  " << iter->receiptHandle << endl;
            } else {
                cout << "Ack: " << messages.size() << " messages suc!" << endl;
        } catch (MQServerException& me) {
            if (me.GetErrorCode() == "MessageNotExist") {
                cout << "No message to consume! RequestId: " + me.GetRequestId() << endl
```

;

```
                continue;
            cout << "Request Failed: " + me.GetErrorCode() + ".RequestId: " +
me.GetRequestId() << endl;
#ifdef _WIN32
            Sleep(2000);
#else
```

```
            usleep(2000 * 1000);
#endif
        } catch (MQExceptionBase& mb) {
            cout << "Request Failed: " + mb.ToString() << endl;
#ifdef _WIN32
            Sleep(2000);
#else
            usleep(2000 * 1000);
#endif
    } while(true);
```

##### Send and consume ordered messages

Ordered messages are a type of message that is published and consumed in a strict order. Ordered messages in ApsaraMQ for RocketMQ are also known as first-in-first-out (FIFO) messages. This topic provides sample code to show how to use the HTTP client SDK for C++ to send and consume ordered messages.

**Background information**

Ordered messages are classified into the following types: Globally ordered message: All messages in a specified topic are published and consumed in first-in-first-out (FIFO) order. Partitionally ordered message: All messages in a specified topic are distributed to different partitions by using shard keys. The messages in each partition are published and consumed in FIFO order. A Sharding Key is a key field that is used for ordered messages to identify different partitions. The Sharding Key is different from the key of a normal message. For more information about the message routing feature, see Ordered messages.

**Prerequisites**

The following operations are performed: Install the SDK for C++. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send ordered messages**

The following sample code provides an example on how to send ordered messages:

```
//#include <iostream>
#include <fstream>
#include <time.h>
#include "mq_http_sdk/mq_client.h"
using namespace std; using namespace mq::http::sdk;
```

```
int main() {
    MQClient mqClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
    // The topic to which you want to send messages. The topic is created in the Apsara
MQ for RocketMQ console.
    string topic = "${TOPIC}";
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    string instanceId = "${INSTANCE_ID}";
    MQProducerPtr producer;
    if (instanceId == "") {
        producer = mqClient.getProducerRef(topic);
    } else {
        producer = mqClient.getProducerRef(instanceId, topic);
    try {
        // Cyclically send four messages.
        for (int i = 0; i < 8; i++)
```

`{`

```
            PublishMessageResponse pmResp;
            // The content of the message.
            TopicMessage pubMsg("Hello, mq!order msg!");
            // The shard key that is used to distribute ordered messages to a specific
partition. Shard keys can be used to identify different partitions. A shard key is diff erent from a message key.
            pubMsg.setShardingKey(std::to_string(i % 2));
            // The custom property of the message.
            pubMsg.putProperty("a",std::to_string(i));
            producer->publishMessage(pubMsg, pmResp);
            cout << "Publish mq message success. Topic is: " << topic
                << ", msgId is:" << pmResp.getMessageId()
                << ", bodyMD5 is:" << pmResp.getMessageBodyMD5() << endl;
    } catch (MQServerException& me) {
        cout << "Request Failed: " + me.GetErrorCode() << ", requestId is:" <<
me.GetRequestId() << endl;
```

`q` `()` ;

```
        return -1;
    } catch (MQExceptionBase& mb) {
        cout << "Request Failed: " + mb.ToString() << endl;
        return -2;
    return 0;
```

**Consume ordered messages**

The following sample code provides an example on how to consume ordered messages:

```
#include <vector>
#include <fstream>
#include "mq_http_sdk/mq_client.h"
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif
using namespace std; using namespace mq::http::sdk; int main() {
    MQClient mqClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
    // The topic from which you want to consume messages. The topic is created in the A
psaraMQ for RocketMQ console.
    string topic = "${TOPIC}";
    // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
    string groupId = "${GROUP_ID}";
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    string instanceId = "${INSTANCE_ID}";
```

```
    MQConsumerPtr consumer;
    if (instanceId == "") {
        consumer = mqClient.getConsumerRef(topic, groupId);
    } else {
        consumer = mqClient.getConsumerRef(instanceId, topic, groupId, "");
    do {
        try {
            std::vector<Message> messages;
            // Consume messages in long polling mode. The consumer may pull
partitionally ordered messages from multiple partitions. The consumer consumes messages from the same partition in the order in which the messages are sent.
            // A consumer pulls partitionally ordered messages from a partition. If the
broker does not receive an acknowledgment (ACK) for a message after the message is cons umed, the consumer consumes the message again.
            // The consumer can consume the next batch of messages from a partition onl
y after all messages that are pulled from the partition in the previous batch are ackno wledged to be consumed.
            // In long polling mode, if no message in the topic is available for consump
tion, the request is suspended on the broker for a specified period of time. If a messa ge becomes available for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
            consumer->consumeMessageOrderly(
                    3, // The maximum number of messages that can be consumed at a time.
In this example, the value is set to 3. The maximum value that you can specify is 16.
                    3, // The length of a long polling period. Unit: seconds. In this ex
ample, the value is set to 3. The maximum value that you can specify is 30.
                    messages
```

);

```
            cout << "Consume: " << messages.size() << " Messages!" << endl;
            // Specify the message consumption logic.
            std::vector<std::string> receiptHandles;
            for (std::vector<Message>::iterator iter = messages.begin();
                    iter != messages.end(); ++iter)
```

`{`

```
                cout << "MessageId: " << iter->getMessageId()
                    << " PublishTime: " << iter->getPublishTime()
                    << " Tag: " << iter->getMessageTag()
                    << " Body: " << iter->getMessageBody()
                    << " FirstConsumeTime: " << iter->getFirstConsumeTime()
                    << " NextConsumeTime: " << iter->getNextConsumeTime()
                    << " ConsumedTimes: " << iter->getConsumedTimes()
                    << " Properties: " << iter->getPropertiesAsString()
                    << " ShardingKey: " << iter->getShardingKey() << endl;
                receiptHandles.push_back(iter->getReceiptHandle());
            // Obtain an ACK from the consumer.
            // If the broker does not receive an ACK for a message from the consumer be
fore the period of time that is specified by the Message.NextConsumeTime parameter elap ses, the broker delivers the message for consumption again.
```

```
            // A unique timestamp is specified for the handle of a message each time th
e message is consumed.
            AckMessageResponse bdmResp;
            consumer->ackMessage(receiptHandles, bdmResp);
            if (!bdmResp.isSuccess()) {
                // If the handle of a message times out, the broker cannot receive an AC
K for the message from the consumer.
                const std::vector<AckMessageFailedItem>& failedItems =
                    bdmResp.getAckMessageFailedItem();
                for (std::vector<AckMessageFailedItem>::const_iterator iter = failedItem
s.begin();
                        iter != failedItems.end(); ++iter)
```

`{`

```
                    cout << "AckFailedItem: " << iter->errorCode
                        << "  " << iter->receiptHandle << endl;
            } else {
                cout << "Ack: " << messages.size() << " messages suc!" << endl;
        } catch (MQServerException& me) {
            if (me.GetErrorCode() == "MessageNotExist") {
                cout << "No message to consume! RequestId: " + me.GetRequestId() << endl
```

;

```
                continue;
            cout << "Request Failed: " + me.GetErrorCode() + ".RequestId: " +
me.GetRequestId() << endl;
#ifdef _WIN32
            Sleep(2000);
#else
            usleep(2000 * 1000);
#endif
        } catch (MQExceptionBase& mb) {
            cout << "Request Failed: " + mb.ToString() << endl;
#ifdef _WIN32
            Sleep(2000);
#else
            usleep(2000 * 1000);
#endif
    } while(true);
```

##### Send and consume scheduled messages

**and delayed messages**

This topic provides sample code to show how to use the HTTP client SDK for C++ to send and consume scheduled messages and delayed messages.

**Background information**

Delayed message: The producer sends the message to the ApsaraMQ for RocketMQ server, but does not expect the message to be delivered immediately. Instead, the message is delivered to the consumer for consumption after a certain period of time. This message is a delayed message. Scheduled message: A producer sends a message to a ApsaraMQ for RocketMQ broker and expects the message to be delivered to a consumer at a specified point in time. This type of message is called a scheduled message. If an HTTP client SDK is used, the code configurations of scheduled messages are the same as the code configurations of delayed messages. Both types of messages are delivered to consumers after a specific period of time based on the attributes of the messages. For more information about the message routing feature, see Scheduled messages and delayed messages.

**Prerequisites**

The following operations are performed: Install the SDK for C++. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send scheduled messages or delayed messages**

The following sample code provides an example on how to send scheduled messages or delayed messages:

```
#include <fstream>
#include <time.h>
#include "mq_http_sdk/mq_client.h"
using namespace std; using namespace mq::http::sdk; int main() {
    MQClient mqClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that you created in the Resource Access Management
(RAM) console. The AccessKey ID is used for identity verification.
            "${ACCESS_KEY}",
            // The AccessKey secret that you created in the RAM console. The AccessKey
secret is used for identity verification.
            "${SECRET_KEY}"
```

);

```
    // The topic to which you want to send messages. The topic is created in the Apsara
MQ for RocketMQ console.
    string topic = "${TOPIC}";
```

```
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    string instanceId = "${INSTANCE_ID}";
    MQProducerPtr producer;
    if (instanceId == "") {
        producer = mqClient.getProducerRef(topic);
    } else {
        producer = mqClient.getProducerRef(instanceId, topic);
    try {
        // Cyclically send four messages.
        for (int i = 0; i < 4; i++)
```

`{`

```
            PublishMessageResponse pmResp;
            // The content of the message.
            TopicMessage pubMsg("Hello, mq!have key!");
            // The custom property of the message.
            pubMsg.putProperty("a",std::to_string(i));
            // The key of the message.
            pubMsg.setMessageKey("MessageKey" + std::to_string(i));
            // The period of time after which the broker delivers the message. In this
example, when the broker receives a message, the broker waits for 10 seconds before it delivers the message to the consumer. Set this parameter to a timestamp in milliseconds
```

`.`

```
            // If the producer sends a scheduled message, set the parameter to the time
interval between the scheduled point in time and the current point in time.
            pubMsg.setStartDeliverTime(time(NULL) * 1000 + 10 * 1000);
            producer->publishMessage(pubMsg, pmResp);
            cout << "Publish mq message success. Topic is: " << topic
                << ", msgId is:" << pmResp.getMessageId()
                << ", bodyMD5 is:" << pmResp.getMessageBodyMD5() << endl;
    } catch (MQServerException& me) {
        cout << "Request Failed: " + me.GetErrorCode() << ", requestId is:" <<
me.GetRequestId() << endl;
        return -1;
    } catch (MQExceptionBase& mb) {
        cout << "Request Failed: " + mb.ToString() << endl;
        return -2;
    return 0;
```

**Consume scheduled messages or delayed messages**

The following sample code provides an example on how to consume scheduled messages or delayed messages:

```
#include <vector>
#include <fstream>
#include "mq_http_sdk/mq_client.h"
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif
using namespace std; using namespace mq::http::sdk; int main() {
    MQClient mqClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
    // The topic from which you want to consume messages. The topic is created in the A
psaraMQ for RocketMQ console.
    string topic = "${TOPIC}";
    // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
    string groupId = "${GROUP_ID}";
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    string instanceId = "${INSTANCE_ID}";
    MQConsumerPtr consumer;
    if (instanceId == "") {
        consumer = mqClient.getConsumerRef(topic, groupId);
    } else {
        consumer = mqClient.getConsumerRef(instanceId, topic, groupId, "");
    do {
        try {
            std::vector<Message> messages;
            // Consume messages in long polling mode.
            // In long polling mode, if no message in the topic is available for consump
```

```
tion, the request is suspended on the broker for a specified period of time. If a messa ge becomes available for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
            consumer->consumeMessage(
                    3, // The maximum number of messages that can be consumed at a time.
In this example, the value is set to 3. The maximum value that you can specify is 16.
                    3, // The length of a long polling period. Unit: seconds. In this ex
ample, the value is set to 3. The maximum value that you can specify is 30.
                    messages
```

);

```
            cout << "Consume: " << messages.size() << " Messages!" << endl;
            // Specify the message consumption logic.
            std::vector<std::string> receiptHandles;
            for (std::vector<Message>::iterator iter = messages.begin();
                    iter != messages.end(); ++iter)
```

`{`

```
                cout << "MessageId: " << iter->getMessageId()
                    << " PublishTime: " << iter->getPublishTime()
                    << " Tag: " << iter->getMessageTag()
                    << " Body: " << iter->getMessageBody()
                    << " FirstConsumeTime: " << iter->getFirstConsumeTime()
                    << " NextConsumeTime: " << iter->getNextConsumeTime()
                    << " ConsumedTimes: " << iter->getConsumedTimes()
                    << " Properties: " << iter->getPropertiesAsString()
                    << " Key: " << iter->getMessageKey() << endl;
                receiptHandles.push_back(iter->getReceiptHandle());
            // Obtain an acknowledgment (ACK) from the consumer.
            // If the broker does not receive an ACK for a message from the consumer be
fore the period of time that is specified by the Message.NextConsumeTime parameter elap ses, the broker delivers the message for consumption again.
            // A unique timestamp is specified for the handle of a message each time th
e message is consumed.
            AckMessageResponse bdmResp;
            consumer->ackMessage(receiptHandles, bdmResp);
            if (!bdmResp.isSuccess()) {
                // If the handle of a message times out, the broker cannot receive an AC
K for the message from the consumer.
                const std::vector<AckMessageFailedItem>& failedItems =
                    bdmResp.getAckMessageFailedItem();
                for (std::vector<AckMessageFailedItem>::const_iterator iter = failedItem
s.begin();
                        iter != failedItems.end(); ++iter)
```

`{`

```
                    cout << "AckFailedItem: " << iter->errorCode
                        << "  " << iter->receiptHandle << endl;
            } else {
                cout << "Ack: " << messages.size() << " messages suc!" << endl;
        } catch (MQServerException& me) {
            if (me.GetErrorCode() == "MessageNotExist") {
```

```
                cout << "No message to consume! RequestId: " + me.GetRequestId() << endl
```

;

```
                continue;
            cout << "Request Failed: " + me.GetErrorCode() + ".RequestId: " +
me.GetRequestId() << endl;
#ifdef _WIN32
            Sleep(2000);
#else
            usleep(2000 * 1000);
#endif
        } catch (MQExceptionBase& mb) {
            cout << "Request Failed: " + mb.ToString() << endl;
#ifdef _WIN32
            Sleep(2000);
#else
            usleep(2000 * 1000);
#endif
    } while(true);
```

##### Send and consume transactional messages

ApsaraMQ for RocketMQ provides a distributed transaction processing feature that is similar to X/Open XA. ApsaraMQ for RocketMQ uses transactional messages to ensure transactional consistency. This topic provides sample code to show how to use the HTTP client SDK for C++ to send and consume transactional messages.

**Background information**

The following figure shows the interaction process of transactional messages. For more information about the message routing feature, see Transactional messages.

**Prerequisites**

The following operations are performed: Install the SDK for C++. For more information about the message routing feature, see Prepare the environment. Create resources that you want to specify in the code. For example, you must create the instance, topic, and group that you want to specify in the code in the ApsaraMQ for RocketMQ console in advance. For more information about the message routing feature, see Create resources.

**Send transactional messages**

The following sample code provides an example on how to send transactional messages:

```
//#include <iostream>
#include <fstream>
#ifdef _WIN32
#include <windows.h>
#include <process.h>
#else
#include "pthread.h"
#endif
#include "mq_http_sdk/mq_client.h"
using namespace std; using namespace mq::http::sdk; const int32_t pubMsgCount = 4; const int32_t halfCheckCount = 3; void processCommitRollError(AckMessageResponse& bdmResp, const std::string& messageId)
```

`{`

```
    if (bdmResp.isSuccess()) {
        cout << "Commit/Roll Transaction Suc: " << messageId << endl;
        return;
    const std::vector<AckMessageFailedItem>& failedItems =
        bdmResp.getAckMessageFailedItem();
    for (std::vector<AckMessageFailedItem>::const_iterator iter = failedItems.begin();
            iter != failedItems.end(); ++iter)
```

`{`

```
        cout << "Commit/Roll Transaction ERROR: " << iter->errorCode
            << "  " << iter->receiptHandle << endl;
#ifdef WIN32
unsigned __stdcall consumeHalfMessageThread(void *arg)
#else
void* consumeHalfMessageThread(void *arg)
#endif
```

`{`

```
    MQTransProducerPtr transProducer = *(MQTransProducerPtr*)(arg);
    int count = 0;
    do {
        std::vector<Message> halfMsgs;
        try {
            // Consume messages in long polling mode.
            // In long polling mode, if no message in the topic is available for consump
tion therequestissuspendedonthebrokerforaspecifiedperiodoftime Ifamessa
```

```
tion, the request is suspended on the broker for a specified period of time. If a messa ge becomes available for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
            transProducer->consumeHalfMessage(
                    1, // The maximum number of messages that can be consumed at a time.
In this example, the value is set to 1. The maximum value that you can specify is 16.
                    3, // The length of a long polling period. Unit: seconds. In this ex
ample, the value is set to 3. The maximum value that you can specify is 30.
                    halfMsgs
```

);

```
        } catch (MQServerException& me) {
            if (me.GetErrorCode() == "MessageNotExist") {
                cout << "No half message to consume! RequestId: " + me.GetRequestId() <<
endl;
                continue;
            cout << "Request Failed: " + me.GetErrorCode() + ".RequestId: " +
me.GetRequestId() << endl;
        if (halfMsgs.size() == 0) {
            continue;
        cout << "Consume Half: " << halfMsgs.size() << " Messages!" << endl;
        // Process half messages.
        std::vector<std::string> receiptHandles;
        for (std::vector<Message>::iterator iter = halfMsgs.begin();
                iter != halfMsgs.end(); ++iter)
```

`{`

```
            cout << "MessageId: " << iter->getMessageId()
                << " PublishTime: " << iter->getPublishTime()
                << " Tag: " << iter->getMessageTag()
                << " Body: " << iter->getMessageBody()
                << " FirstConsumeTime: " << iter->getFirstConsumeTime()
                << " NextConsumeTime: " << iter->getNextConsumeTime()
                << " ConsumedTimes: " << iter->getConsumedTimes()
                << " Properties: " << iter->getPropertiesAsString()
                << " Key: " << iter->getMessageKey() << endl;
            int32_t consumedTimes = iter->getConsumedTimes();
            const std::string propA = iter->getProperty("a");
            const std::string handle = iter->getReceiptHandle();
            AckMessageResponse bdmResp;
            if (propA == "1") {
                cout << "Commit msg.." << endl;
                transProducer->commit(handle, bdmResp);
                count++;
            } else if(propA == "2") {
                if (consumedTimes > 1) {
                    cout << "Commit msg.." << endl;
                    transProducer->commit(handle, bdmResp);
                    count++;
                } else {
                    cout << "Commit Later!!!" << endl;
```

```
            } else if(propA == "3") {
                cout << "Rollback msg.." << endl;
                transProducer->rollback(handle, bdmResp);
                count++;
            } else {
                transProducer->commit(handle, bdmResp);
                cout << "Unkown msg.." << endl;
            // If the transactional message is not committed or rolled back before the
period of time specified by the NextConsumeTime parameter elapses, the commit or rollba ck operation fails.
            processCommitRollError(bdmResp, iter->getMessageId());
    } while(count < halfCheckCount);
#ifdef WIN32
    return 0;
#else
    return NULL;
#endif
int main() {
    MQClient mqClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
    // The topic to which you want to send messages. The topic is created in the Apsara
MQ for RocketMQ console.
    string topic = "${TOPIC}";
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    string instanceId = "${INSTANCE_ID}";
    // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
    string groupId = "${GROUP_ID}";
    MQTransProducerPtr transProducer;
    if (instanceId == "") {
        transProducer = mqClient.getTransProducerRef(topic, groupId);
```

```
    } else {
        transProducer = mqClient.getTransProducerRef(instanceId, topic, groupId);
    // The client needs a thread or a process to process unacknowledged transactional m
essages.
    // Start a thread to process unacknowledged transactional messages.
#ifdef WIN32
    HANDLE thread;
    unsigned int threadId;
    thread = (HANDLE)_beginthreadex(NULL, 0, consumeHalfMessageThread, &transProducer,
0, &threadId);
#else
    pthread_t thread;
    pthread_create(&thread, NULL, consumeHalfMessageThread, static_cast<void *>
(&transProducer));
#endif
    try {
        for (int i = 0; i < pubMsgCount; i++)
```

`{`

```
            PublishMessageResponse pmResp;
            TopicMessage pubMsg("Hello, mq, trans_msg!");
            pubMsg.putProperty("a",std::to_string(i));
            pubMsg.setMessageKey("ImKey");
            pubMsg.setTransCheckImmunityTime(10);
            transProducer->publishMessage(pubMsg, pmResp);
            cout << "Publish mq message success. Topic:" << topic
                << ", msgId:" << pmResp.getMessageId()
                << ", bodyMD5:" << pmResp.getMessageBodyMD5()
                << ", Handle:" << pmResp.getReceiptHandle() << endl;
            if (i == 0) {
                // After the producer sends the transactional message, the broker
obtains the handle of the half message that corresponds to the transactional message an d commits or rolls back the transactional message based on the status of the handle.
                // If a transactional message is not committed or rolled back after the
period of time specified by the TransCheckImmunityTime parameter elapses, the commit or rollback operation fails.
                AckMessageResponse bdmResp;
                transProducer->commit(pmResp.getReceiptHandle(), bdmResp);
                processCommitRollError(bdmResp, pmResp.getMessageId());
    } catch (MQServerException& me) {
        cout << "Request Failed: " + me.GetErrorCode() << ", requestId is:" <<
me.GetRequestId() << endl;
    } catch (MQExceptionBase& mb) {
        cout << "Request Failed: " + mb.ToString() << endl;
#ifdef WIN32
    WaitForSingleObject(thread, INFINITE);
    CloseHandle(thread);
```

```
#else
    pthread_join(thread, NULL);
#endif
    return 0;
```

**Consume transactional messages**

The following sample code provides an example on how to consume transactional messages:

```
#include <vector>
#include <fstream>
#include "mq_http_sdk/mq_client.h"
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif
using namespace std; using namespace mq::http::sdk; int main() {
    MQClient mqClient(
            // The HTTP endpoint to which you want to connect. To obtain the HTTP
endpoint, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane , click Instances. On the Instances page, select the name of your instance. Then, view the HTTP endpoint on the Network Management tab.
            "${HTTP_ENDPOINT}",
            // The AccessKey ID that is used for identity verification. You can obtain
the AccessKey ID in the Apsara Uni-manager Operations Console.
            "${ACCESS_KEY}",
            // The AccessKey secret that is used for identity verification. You can obt
ain the AccessKey secret in the Apsara Uni-manager Operations Console.
            "${SECRET_KEY}"
```

);

```
    // The topic from which you want to consume messages. The topic is created in the A
psaraMQ for RocketMQ console.
    string topic = "${TOPIC}";
    // The ID of the group that you created in the ApsaraMQ for RocketMQ console.
    string groupId = "${GROUP_ID}";
    // The ID of the instance to which the topic belongs. The instance is created in th
e ApsaraMQ for RocketMQ console.
    // If the instance has a namespace, specify the ID of the instance. If the instance
does not have a namespace, set the instance ID to null or an empty string. You can chec k whether your instance has a namespace on the Instances page in the RocketMQ console.
    string instanceId = "${INSTANCE_ID}";
    MQConsumerPtr consumer;
```

```
    if (instanceId == "") {
        consumer = mqClient.getConsumerRef(topic, groupId);
    } else {
        consumer = mqClient.getConsumerRef(instanceId, topic, groupId, "");
    do {
        try {
            std::vector<Message> messages;
            // Consume messages in long polling mode.
            // In long polling mode, if no message in the topic is available for consump
tion, the request is suspended on the broker for a specified period of time. If a messa ge becomes available for consumption within this period, the broker immediately sends a response to the consumer. In this example, the period is set to 3 seconds.
            consumer->consumeMessage(
                    3, // The maximum number of messages that can be consumed at a time.
In this example, the value is set to 3. The maximum value that you can specify is 16.
                    3, // The length of a long polling period. Unit: seconds. In this ex
ample, the value is set to 3. The maximum value that you can specify is 30.
                    messages
```

);

```
            cout << "Consume: " << messages.size() << " Messages!" << endl;
            // Specify the message consumption logic.
            std::vector<std::string> receiptHandles;
            for (std::vector<Message>::iterator iter = messages.begin();
                    iter != messages.end(); ++iter)
```

`{`

```
                cout << "MessageId: " << iter->getMessageId()
                    << " PublishTime: " << iter->getPublishTime()
                    << " Tag: " << iter->getMessageTag()
                    << " Body: " << iter->getMessageBody()
                    << " FirstConsumeTime: " << iter->getFirstConsumeTime()
                    << " NextConsumeTime: " << iter->getNextConsumeTime()
                    << " ConsumedTimes: " << iter->getConsumedTimes()
                    << " Properties: " << iter->getPropertiesAsString()
                    << " Key: " << iter->getMessageKey() << endl;
                receiptHandles.push_back(iter->getReceiptHandle());
            // Obtain an acknowledgment (ACK) from the consumer.
            // If the broker does not receive an ACK for a message from the consumer be
fore the period of time that is specified by the Message.NextConsumeTime parameter elap ses, the broker delivers the message for consumption again.
            // A unique timestamp is specified for the handle of a message each time th
e message is consumed.
            AckMessageResponse bdmResp;
            consumer->ackMessage(receiptHandles, bdmResp);
            if (!bdmResp.isSuccess()) {
                // If the handle of a message times out, the broker cannot receive an AC
K for the message from the consumer.
                const std::vector<AckMessageFailedItem>& failedItems =
                    bdmResp.getAckMessageFailedItem();
                for (std::vector<AckMessageFailedItem>::const_iterator iter = failedItem
sbegin()
```

```
s.begin();
                        iter != failedItems.end(); ++iter)
```

`{`

```
                    cout << "AckFailedItem: " << iter->errorCode
                        << "  " << iter->receiptHandle << endl;
            } else {
                cout << "Ack: " << messages.size() << " messages suc!" << endl;
        } catch (MQServerException& me) {
            if (me.GetErrorCode() == "MessageNotExist") {
                cout << "No message to consume! RequestId: " + me.GetRequestId() << endl
```

;

```
                continue;
            cout << "Request Failed: " + me.GetErrorCode() + ".RequestId: " +
me.GetRequestId() << endl;
#ifdef _WIN32
            Sleep(2000);
#else
            usleep(2000 * 1000);
#endif
        } catch (MQExceptionBase& mb) {
            cout << "Request Failed: " + mb.ToString() << endl;
#ifdef _WIN32
            Sleep(2000);
#else
            usleep(2000 * 1000);
#endif
    } while(true);
```

## Best practices

### Clustering consumption and

**broadcasting consumption**

This topic describes the terms, scenarios, and usage notes of clustering consumption and broadcasting consumption in ApsaraMQ for RocketMQ.

**Terms**

ApsaraMQ for RocketMQ is a messaging system that is based on the publish-subscribe model. In ApsaraMQ for RocketMQ, a consumer subscribes to a topic to obtain and consume messages. In most cases, consumer applications use distributed systems. Multiple machines are deployed in one cluster. Therefore, ApsaraMQ for RocketMQ defines the following terms:
**Cluster:** Consumers identified by the same group ID belong to the same cluster. These
consumers must have the same consumption logic that also involves tags. These consumers can be considered logically as one consumption node.
**Clustering consumption:** In this mode, a message needs to be processed only by a
consumer in the cluster.
**Broadcasting consumption:** In this mode, ApsaraMQ for RocketMQ broadcasts each
message to all consumers registered in the cluster to ensure that the message is consumed by each consumer at least once.

**Scenarios**

**Clustering consumption mode:**

Figure 1. Clustering consumption mode

**Scenarios and usage notes:**

Consumers are deployed in a cluster and each message needs to be processed only once. The consumption progress is recorded on the ApsaraMQ for RocketMQ broker. Therefore, the reliability is high. In clustering consumption mode, each message is delivered to only one consumer in the cluster for processing. If a message needs to be processed by each consumer in the cluster, use the broadcasting consumption mode. In clustering consumption mode, it is not guaranteed that a failed message can be routed to the same consumer each time the message is redelivered. Therefore, no definitive assumptions can be made during message processing.

**Broadcasting consumption mode:**

Figure 2. Broadcasting consumption mode Scenarios and usage notes: Ordered messages are not supported in broadcasting consumption mode. Consumer offsets cannot be reset in broadcasting consumption mode. Each message needs to be processed by multiple consumers that are subject to the same logic. The consumption progress is recorded on the consumer. Duplicate messages are more likely to occur in broadcasting consumption mode than in clustering consumption mode. In broadcasting consumption mode, ApsaraMQ for RocketMQ ensures that each message is consumed at least once by each consumer, but does not resend a message that fails to be consumed. Therefore, you need to pay attention to consumption failures. In broadcasting consumption mode, a consumer starts consumption from the latest message each time the consumer is restarted. The consumer automatically skips the messages that are sent to the ApsaraMQ for RocketMQ broker when the consumer is stopped. Therefore, use this mode with caution. In broadcasting consumption mode, each message is repeatedly processed by many consumers. Therefore, we recommend that you use the clustering consumption mode whenever possible. Only Java clients support the broadcasting consumption mode. In broadcasting consumption mode, the ApsaraMQ for RocketMQ broker does not record the consumption progress. In this mode, you cannot query accumulated messages, configure message accumulation alerts, or query subscriptions in the ApsaraMQ for RocketMQ console.

**Use the clustering consumption mode to simulate the broadcasting consumption**

**mode**

If the broadcasting consumption mode is required for your business, you can create multiple group IDs to subscribe to the same topic. Figure 3. Use the clustering consumption mode to simulate the broadcasting consumption mode Scenarios and usage notes: Each message needs to be processed by multiple consumers, and the logic of the consumers can be the same or different. The consumption progress is recorded on the ApsaraMQ for RocketMQ broker. Therefore, the reliability is higher than that in broadcasting consumption mode. For each group ID, one or more consumer instances can be deployed. When multiple consumer instances are deployed, these instances compose a cluster and work together to consume messages. Assume that three consumer instances C1, C2, and C3 are deployed for Group ID 1. These instances share the messages sent from the ApsaraMQ for RocketMQ broker to Group ID 1. In addition, these instances must subscribe to the same topics and same tags.

### Message filtering

This topic describes how ApsaraMQ for RocketMQ consumers filter messages on the ApsaraMQ for RocketMQ broker based on tags. A tag is used to classify messages in a topic into different types. ApsaraMQ for RocketMQ allows consumers to filter messages by using tags. This ensures that the consumers consume only messages that they are concerned with. The following figure shows an example in the e-commerce transaction scenario. In the process from placing an order to receiving the product by the customer, a series of messages including order messages, payment messages, and logistics messages are generated. These messages are sent to the Trade_Topic topic and subscribed to by different systems, such as the payment system, analysis system for transaction success rate, and real-time computing system. Among these systems, the logistics system receives only logistics messages and the real-time computing system receives all transaction-related messages, including the order messages, payment messages, and logistics messages. Figure 1. Filter messages

**Note**

To classify messages, you can create multiple topics, or create multiple tags in the same topic. In most cases, messages in one topic are irrelevant to those in another topic. Tags are used to distinguish between relevant messages in the same topic. For example, you can create different tags in the same topic to distinguish between a set and its subsets or distinguish between processes in sequence.

**Examples**

Send messages Specify a tag for each message before the message is sent.

```
Message msg = new Message("MQ_TOPIC","TagA","Hello MQ".getBytes());
```

Subscribe to messages Consumption method 1 If a consumer needs to subscribe to messages of all types in a topic, use an asterisk (*) to represent all tags.

```java
consumer.subscribe("MQ_TOPIC", "*", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
});
```

Consumption method 2 If a consumer needs to subscribe to messages of a specific type in a topic, specify the corresponding tag.

```java
consumer.subscribe("MQ_TOPIC", "TagA", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
});
```

Consumption method 3 If a consumer needs to subscribe to messages of multiple types in a topic, separate the corresponding tags with two vertical bars (||).

```java
consumer.subscribe("MQ_TOPIC", "TagA||TagB", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
});
```

Consumption method 4 (error example) If a consumer subscribes to messages with specific tags in a topic multiple times, the tags in the last subscription prevail:

```java
// In the following error code, the consumer can receive only messages with TagB in MQ_TOPIC and cannot receive messages with TagA. consumer.subscribe("MQ_TOPIC", "TagA", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
}); consumer.subscribe("MQ_TOPIC", "TagB", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
});
```

### Subscription consistency

In ApsaraMQ for RocketMQ, a group ID represents a consumer instance group. For most distributed applications, multiple consumer instances are attached to the same group ID. Subscription consistency means that the processing logic of all consumer instances identified by the same group ID must be identical. If the subscriptions of the consumer instances are inconsistent, errors occur in the message consumption logic and messages may be lost. Subscriptions in ApsaraMQ for RocketMQ involve topics and tags. Therefore, all consumer instances identified by the same group ID must be consistent in the following two aspects to ensure subscription consistency: The topics to which the consumer instances subscribe must be the same. The tags of the topics to which the consumer instances subscribe must be the same.

**Examples of subscriptions**

Consistent subscriptions Multiple group IDs subscribe to multiple topics, and the subscriptions of different consumer instances identified by the same group ID are consistent, as shown in the following figure. Figure 1. Consistent subscriptions Inconsistent subscriptions One group ID subscribes to multiple topics, but the subscriptions of different consumer instances identified by the group ID are inconsistent, as shown in the following figure. Figure 2. Inconsistent subscriptions

**Sample code of subscriptions**

Sample code of inconsistent subscriptions Example 1 In the following example, two consumer instances identified by the same group ID subscribe to different topics. Consumer instance 1-1:

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_1"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "*", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
});
```

Consumer instance 1-2:

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_1"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_B ", "*", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
});
```

Example 2 In the following example, two consumer instances identified by the same group ID subscribe to the same topic but subscribe to different numbers of tags of the topic. Consumer instance 2-1 has subscribed to Tag A, whereas consumer instance 2-2 has not specified a tag. Consumer instance 2-1:

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_2"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "TagA", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
});
```

Consumer instance 2-2:

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_2"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "*", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
});
```

Example 3 In this example, the subscriptions are inconsistent due to the following reasons: Two consumer instances identified by the same group ID subscribe to different numbers of topics. Both the consumer instances subscribe to one same topic but subscribe to different tags of the topic. Consumer instance 3-1:

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_3"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "TagA", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
}); consumer.subscribe("jodie_test_B", "TagB", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
});
```

Consumer instance 3-2:

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_3"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "TagB", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
});
```

### Consumption idempotence

After a ApsaraMQ for RocketMQ consumer receives messages, the consumer needs to perform idempotent processing on these messages based on the unique business-specific keys of the messages.

**Necessity for consumption idempotence**

In Internet applications, duplicate messages may occur in ApsaraMQ for RocketMQ especially if Internet connection is unstable. Duplicate messages may occur in the following two scenarios: A producer repeatedly sends a message to the ApsaraMQ for RocketMQ broker. If a network disconnection occurs or the producer breaks down after a message is sent to and persisted in the ApsaraMQ for RocketMQ broker, the broker fails to respond to the producer. If the producer realizes that the message failed to be sent and resends the message, the consumer subsequently receives two messages that have the same content and message ID. The ApsaraMQ for RocketMQ broker repeatedly delivers a message to a consumer. A message is delivered to a consumer and is processed by the consumer. However, a network disconnection occurs when the consumer sends a response to the ApsaraMQ for RocketMQ broker. To ensure that the message is consumed at least once, the ApsaraMQ for RocketMQ broker redelivers the previously processed message after the network connection recovers. The consumer subsequently receives two messages that have the same content and message ID. Duplicate messages are generated when rebalancing is triggered in scenarios such as network jitter, broker restart, and consumer application restart. Traffic is rebalanced if the ApsaraMQ for RocketMQ broker or consumer client is restarted or scaled. In this case, a consumer may receive duplicate messages.

**Solution**

Message IDs may be duplicate. Therefore, we recommend that you do not implement idempotent processing based on message IDs. The best practice is to use unique businessspecific keys for idempotent processing. The following sample code provides an example on how to specify a unique business-specific key for a message:

```
Message message = new Message(); message.setKey("ORDERID_100"); SendResult sendResult = producer.send(message);
```

The following sample code provides an example on how a consumer performs idempotent processing after it receives a message:

```
consumer.subscribe("ons_test", "*", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        String key = message.getKey()
        // Use the unique business-specific key for idempotent processing.
});
```

### Active geo-redundancy

ApsaraMQ for RocketMQ leverages Alibaba Cloud Express Connect and Multi-Site High Availability (MSHA) to support active geo-redundancy. MSHA allows you to implement twoway data synchronization and business traffic switchover across instances. This way, business recovery is decoupled from fault recovery. If a fault occurs, business continuity can be ensured. This topic introduces the concept of MSHA and describes the common scenarios in which MSHA is suitable. This topic also describes the benefits of MSHA.

**What is MSHA?**

MSHA is an active geo-redundancy solution that was developed in the e-commerce business environment of Alibaba Group. MSHA can help decouple business recovery from fault recovery. MSHA provides capabilities such as flexible scheduling based on traffic rules, crossregion and cross-cloud management, and data protection. If a fault occurs, fast failover and recovery operations can be performed. ApsaraMQ for RocketMQ leverages Alibaba Cloud Express Connect and MSHA to implement two-way synchronization of message data across instances in the same region or different regions. MSHA is different from a traditional disaster recovery solution. MSHA allows ApsaraMQ for RocketMQ clusters that are deployed in different units to provide services at the same time. This helps implement disaster recovery, improve business continuity, and achieve remote resource scaling. The following figure shows how to use MSHA to implement active geo-redundancy for ApsaraMQ for RocketMQ. A complete business system is deployed in the Hangzhou and Shanghai units. The MSHA access layer routes business data to the two units based on traffic rules. The application systems and ApsaraMQ for RocketMQ broker clusters in the Hangzhou and Shanghai units process business data in their local regions. The broker clusters in the two units are configured to support active geo-redundancy. Data is synchronized between Broker Cluster A and Broker Cluster B in a two-way manner. The data includes topics, groups, and consumer offsets. In normal cases, the business systems in the Hangzhou and Shanghai units process business data only in their local regions, and synchronize message data of the local unit to the cluster of the remote unit for disaster recovery and backup. Assume that a disaster occurs in the Hangzhou unit and the entire business system in the Hangzhou unit fails. In this case, MSHA switches the business data of the Hangzhou unit to the Shanghai unit. As a result, Broker Cluster B of the Shanghai unit stores the business data of the Hangzhou unit and can continue to process the unfinished message data. This allows you to troubleshoot and fix the fault without service downtime. This way, the business can be recovered before the fault is rectified. After the Hangzhou unit is recovered from the fault, MSHA switches the business data of the Hangzhou unit back to the business system in the Hangzhou unit. During the entire process, users are not aware of the fault, and the user experience is not affected.

**Common scenarios**

MSHA can be used in the following common business scenarios: Business scenarios in which workloads are divided into different units by region, such as logistics workloads. You can divide the logistics workloads based on the regions in which logistics orders are placed and send business data to production centers in different regions. This way, the data can be simultaneously processed. This helps improve resource utilization and business concurrency. Business scenarios that have strict requirements for the reliability of business data, such as financial and securities systems. If a system fault occurs, the transaction results are negatively affected. In this case, you can use MSHA to switch the workloads to the disaster recovery site. The disaster recovery site can continue to process unfinished message data based on the synchronized data.

**Benefits**

**High availability**

Compared with a traditional disaster recovery solution, MSHA implements two-way data synchronization across production centers. All production centers can provide services at the same time. This implements traffic balancing and improves resource utilization.

**Fast fault recovery**

MSHA effectively ensures business continuity. MSHA decouples business recovery from fault recovery. When one of the production centers fails, MSHA immediately switches the business to other healthy production centers to ensure business continuity. This is different from a traditional solution in which the fault must be identified and fixed before the business can be recovered.

**Remote resource scaling**

The limited resources in a single data center or region may not meet the requirements as the business rapidly develops. In addition, the business may face bottlenecks such as limited storage and computing performance. The horizontal scaling capability of ApsaraMQ for RocketMQ allows the business to be expanded in other data centers or regions to improve cost efficiency.

### Zone-disaster recovery

ApsaraMQ for RocketMQ supports the multi-chip cross-zone disaster recovery and asymmetric disaster recovery features in zone-disaster recovery scenarios. This topic describes the requirements, scenarios, and benefits of these two features.

**Background information**

In today's rapidly evolving digital business landscape, enterprises increasingly expect continuous operations and high service availability. To mitigate the threats posed by various unforeseen events such as natural disasters, hardware failures, and cyberattacks, large- and medium-sized enterprises have always considered building an information system with strong disaster tolerance capabilities as one of their fundamental requirements. However, ApsaraMQ for RocketMQ still faces the following challenges in implementing zone-disaster recovery in actual business scenarios:
**Asymmetric disaster recovery:** Most Apsara Stack zone-disaster recovery solutions
require symmetric deployments across primary and secondary zones. This requires that the number of servers deployed in both zones must be consistent. However, in actual business scenarios, customers often deploy a large number of ApsaraMQ for RocketMQ instances in the primary zone and require disaster recovery only for a small subset of these instances in a secondary zone. In this case, symmetric deployments lead to significant cost increases and resource waste.
**Multi-chip cross-zone disaster recovery:** Driven by hardware localization
requirements, an increasing number of customers require support for multi-cluster hybrid deployments in zone-disaster recovery scenarios to ensure supply chain security.

**Scenarios**

To resolve the preceding issues, Apsara Stack develops ApsaraMQ for RocketMQ that provides the cross-zone multi-cluster hybrid deployment and asymmetric disaster recovery features in the following scenarios:

**Scenario 1: Disaster recovery clusters and single-data center**

**clusters deployed in the primary zone**

**Scenario 2: Disaster recovery clusters and single-data center**

**clusters deployed in the secondary zone**

**Scenario 3: Disaster recovery clusters and single-data center**

**clusters deployed in the primary and secondary zones**

**Benefits**

**High resource utilization**

Traditional disaster recovery architectures often rely on a fixed resource allocation ratio between primary and secondary clusters, leading to significant resource underutilization in the secondary cluster during normal operation. In contrast, asymmetric cluster deployments offer greater flexibility in resource allocation, enabling more efficient resource utilization.

**Multi-chip hybrid deployments across clusters**

With the rise of multi-chip hybrid deployments, the multi-cluster architecture significantly improves system performance in heterogeneous computing scenarios by deeply integrating hardware features.

**High stability**

The multi-cluster architecture offers significant advantages in ensuring system stability by implementing a multi-level resource isolation mechanism. A failure in one cluster does not impact other clusters, effectively isolating fault domains.

### Message routing

ApsaraMQ for RocketMQ provides the message routing feature that can be used to synchronize message data across clusters. This ensures message consistency and integrity between clusters. This topic describes the concept, benefits, and configuration method of message routing. This topic also describes the scenarios to which the message routing feature is applicable.

**What is message routing?**

The message routing feature of ApsaraMQ for RocketMQ is used to synchronize messages across clusters. You can configure routing rules to dynamically plan the synchronization path of messages. This way, the messages can be synchronized from the source node to the destination node based on filter conditions. This feature implements remote message synchronization across clusters within milliseconds and ensures data consistency and integrity across clusters. The following figure shows how message routing works in ApsaraMQ for RocketMQ. In the figure, one-way synchronization is performed based on topics to synchronize messages from a specific source topic in the source instance to a specific destination topic in the destination instance.

**Scenarios**

The message routing feature can be used in the following common scenarios:

**Data synchronization**

Taobao and Tmall serve users all over the world. If sellers in a country or a region want to publish products, the products must be reviewed before they can be available for sale. However, the product review systems of Alibaba Cloud are central systems deployed only in the cities of China, such as Shanghai. In this scenario, messages from the regions outside China must be synchronized to the product review systems in China to achieve cross-region data synchronization.

**Data backup and disaster recovery**

For core trading systems, changes in the details and prices of various commodities need to be updated across all business systems in real time. Multi-region disaster recovery and backup solutions can be used to ensure high availability. This way, service continuity is ensured even if a region becomes unavailable due to issues such as the cut of optical fibers.

**Benefits**

**High performance**

The message routing feature provided by ApsaraMQ for RocketMQ enables real-time message synchronization within milliseconds and supports millions of transactions per second (TPS).

**Low cost**

You do not need to purchase additional leased lines, perform upgrades, or modify application code to use the message routing feature. The message routing process does not affect applications.

**Ease of use**

The message routing feature supports GUI-based configuration. You can create and manage routing tasks in the ApsaraMQ for RocketMQ console.

**Limits**

The message routing feature is applicable to instances that have a namespace. You can check whether an instance has a namespace on the **Instance Information** tab of the instance details page in the ApsaraMQ for RocketMQ console.

**Configure message routing**

This section describes the procedure to configure the message routing feature for an ApsaraMQ for RocketMQ instance. For more information, see Route messages from a cluster to another cluster.

**Step 1: Create message synchronization clouds**

Before you create a message routing task, you must specify the information about the cloud on which your ApsaraMQ for RocketMQ cluster is deployed. The information includes the endpoint of the ApsaraMQ for RocketMQ instance and the AccessKey ID and AccessKey secret of the Apsara Stack tenant account to which the cloud belongs. ApsaraMQ for RocketMQ obtains the permissions that are required to access ApsaraMQ for RocketMQ resources across clouds based on the cloud information that you specified.

**Step 2: Create a message routing task**

Specify the message source and message destination and configure relevant information. For example, specify filter conditions and set the start offset of message synchronization.

## Service usage FAQ

### FAQ

#### Quick start

This topic provides answers to questions frequently asked by new users when they use ApsaraMQ for RocketMQ.
1. Where do consumers identified by a new group ID start to consume?
If a consumer identified by the group ID is started for the first time, the consumer ignores the messages that are sent before the consumer is started. This means that the consumer ignores historical messages and starts to consume messages that are sent after the consumer is started. If the consumer is started for the second time, the consumer starts consumption from the previous consumer offset. If you want the consumer to start consumption from a specific offset, you can reset the previous consumer offset in the ApsaraMQ for RocketMQ console to specify a point in time from which the consumer starts to consume messages. Each reset affects only the specific topic under the specific group ID but does not affect other group IDs.
2. How does the ApsaraMQ for RocketMQ broker redeliver a message if the message fails to
be consumed?

**Clustering consumption**

In clustering consumption mode, if Action.ReconsumerLater or NULL is returned or an error occurs during consumption, the ApsaraMQ for RocketMQ broker attempts to redeliver the message for up to 16 times. If the message still fails to be consumed after the 16 delivery retries, the message is discarded. The following table describes the intervals between delivery retries.

| Nth delivery retry | Interval |
|---|---|
| 1 | 10 seconds |
| 2 | 30 seconds |
| 3 | 1 minute |
| 4 | 2 minutes |
| 5 | 3 minutes |
| 6 | 4 minutes |
| 7 | 5 minutes |

| 8 | 6 minutes |
|---|---|
| 9 | 7 minutes |
| 10 | 8 minutes |
| 11 | 9 minutes |
| 12 | 10 minutes |
| 13 | 20 minutes |
| 14 | 30 minutes |
| 15 | 1 hour |
| 16 | 2 hours |

The message.getReconsumeTimes() method can be called to query the serial number of a delivery retry.

**Broadcasting consumption**

In broadcasting consumption mode, ApsaraMQ for RocketMQ guarantees that a message can be consumed at least once. If the message fails to be consumed, the ApsaraMQ for RocketMQ broker does not redeliver the message.
3. What do I do if a sent message is not received?
ApsaraMQ for RocketMQ provides the following methods for Message query: Specify a topic and time range to query all messages received by this topic within the specified time range. Specify a topic and message ID to query messages by using exact match. Specify a topic and message key to query messages with the same message key. You can use the preceding methods to query the specific content and consumption information of messages. To track the time and location of each role from the producer to the consumer in the entire trace of a message, you can use the message tracing feature provided by ApsaraMQ for RocketMQ. For more information, see Query a message trace.
4. Can ApsaraMQ for RocketMQ ensure that no duplicate messages are delivered to
consumers? In most cases, ApsaraMQ for RocketMQ can ensure that no duplicate messages are delivered to consumers. As a distributed messaging middleware, ApsaraMQ for RocketMQ cannot ensure that no duplicate messages are delivered to consumers when exceptions such as network jitter and application processing timeout occur. However, ApsaraMQ for RocketMQ can ensure that no messages are lost.

#### Configurations

This topic provides answers to frequently asked questions about ApsaraMQ for RocketMQ configurations.
1. How long can messages be retained on the ApsaraMQ for RocketMQ broker?
Messages can be retained on the ApsaraMQ for RocketMQ broker for up to three days. The system automatically deletes the unconsumed after the three days.
2. What is the maximum message body size in ApsaraMQ for RocketMQ?
The maximum message body size in ApsaraMQ for RocketMQ varies with the message type. The following information shows the maximum message body size for different types of messages: A normal or ordered message: 4 MB A transactional, scheduled, or delayed message: 64 KB
3. How do I set the number of consumer threads on a ApsaraMQ for RocketMQ consumer?
To set the number of consumer threads on a ApsaraMQ for RocketMQ consumer, set the ConsumeThreadNums attribute when you start the consumer. The following sample code provides an example on how to set the number of consumer threads:

```
    public static void main(String[] args) {
        Properties properties = new Properties();
        properties.put(PropertyKeyConst.GROUP_ID, "GID_001");
        properties.put(PropertyKeyConst.AccessKey, "xxxxxxxxxxxx");
        properties.put(PropertyKeyConst.SecretKey, "xxxxxxxxxxxx");
        /**
         * Set the number of consumer threads to 20.
```

`*/`

```java
        properties.put(PropertyKeyConst.ConsumeThreadNums,20);
        Consumer consumer =ONSFactory.createConsumer(properties);
        consumer.subscribe("TestTopic", "*", new MessageListener() {
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
        });
        consumer.start();
        System.out.println("Consumer Started");
```

4. What do I do if an error in loading DLL or another running error occurs due to invalid .NET
client configuration? For more information, see SDK_GUIDE.pdf in the compressed package of SDK for .NET to verify that the project configuration is the same as that described in the document.

#### Message tracing

This topic provides answers to frequently asked questions about the message tracing feature of ApsaraMQ for RocketMQ.
1. Why is trace data not found?
If no trace data is found based on the specified query conditions, check whether the following requirements are met: i. Only Java clients of version 1.2.2 or later support the message tracing feature. ii. Check whether the query conditions are properly specified. This means that you need to check whether the topic name, message ID, and message key are properly entered. iii. Check whether the query time range is correct. To accelerate the query, you must specify the range of the message sending time. If you still cannot retrieve the data, expand the time range and try again. iv. If the preceding settings are correct but the trace data is still not found, contact the technical support and provide the related log file. The path to the log file is /home/{user}/logs/ons.log. v. If the preceding settings are correct but the trace data is still not found, submit a ticket to seek help from the technical support and provide the log file. The path to the log file is /home/{user}/logs/ons.log.
2. What do I do if the consumption information about a consumed message is not included in
the trace data and the client IP address and group ID in the trace data are wrong? This problem occurs because the client is not updated to the version that supports the message tracing feature. Therefore, the message tracing module of ApsaraMQ for RocketMQ can obtain only some trace data, and the displayed result is abnormal. We recommend that you upgrade your client as soon as possible. For more information about the message tracing feature, see Query a message trace.
3. Why is my group ID not shown in the list of consumers?
The possible cause is that a large number of downstream consumers have subscribed to messages, and the space in the tracing map is insufficient to display all the data. Move the pointer over the scroll bar and scroll down to see all the data.
4. Why are previous query tasks not displayed?
A large number of historical query tasks affect the display result. Therefore, ApsaraMQ for RocketMQ regularly cleans up historical query tasks and retains only query tasks created within the recent seven days. If you cannot find a historical task, query it again.

#### Alert handling

Alert handling is unavailable for ApsaraMQ for RocketMQ. Apsara Stack provides an isolated cloud-based environment and cannot be connected to the APIs of Internet services, such as the short message service (SMS) gateway. Therefore, the monitoring and alerting module in the console is unavailable.

#### Ordered messages

This topic provides answers to frequently asked questions about ordered messages in ApsaraMQ for RocketMQ.
1. Do ordered messages support clustering consumption and broadcasting consumption?
Ordered messages support clustering consumption but do not support broadcasting consumption.
2. Can a message be an ordered message, a scheduled message, and a transactional
message at the same time? No, a message cannot be an ordered message, a scheduled message, and a transactional message at the same time. Ordered messages, scheduled messages, and transactional messages are different and mutually exclusive message types.
3. What is the usage scope of ordered messages?
Ordered messages are messages that are guaranteed to be consumed in the order they are sent within the same topic. Ordered messages are classified into globally ordered messages and partially ordered messages.
4. Why is the performance of globally ordered messages mediocre?
Globally ordered messages are processed in first-in-first-out (FIFO) order. If the previous message is not consumed, the next message will be stored in a queue of the corresponding topic until the previous message is consumed. To improve the transactions per second (TPS) of globally ordered messages, upgrade the specifications of the host that runs the message client, and reduce as much as possible the time required by the message client application to process the local business logic.
5. What transmission modes do ordered messages support?
Ordered messages support only the reliable synchronous transmission mode.

### Exceptions

#### exceptions and solutions

This topic describes the exceptions that may occur when you use ApsaraMQ for RocketMQ, and the corresponding solutions.
1. The producer or consumer failed to be started, or duplicate group IDs exist.
Possible cause: You attempt to start multiple producer or consumer instances identified by the same group ID in one JVM process. This results in client startup failures. Solution: Perform the following steps: i. Make sure that only one producer or consumer instance with the same group ID is started in a JVM process. In other words, one producer instance and one consumer instance with the same group ID can be started simultaneously in a JVM process, but multiple producer or consumer instances cannot be started simultaneously. ii. Restart the application.
2. In broadcasting consumption mode, an error occurred when the JSON file is loaded for
consumer startup. Cause: The Fastjson version is outdated. In broadcasting consumption mode, the consumer failed to load the local offsets.json file and failed to be started. Solution: Update Fastjson to a version supported by ons-client and make sure that the offsets.json file can be normally loaded. By default, the offsets.json file is located in the /home/{user}/.rocketmq_offsets/ directory.
3. The queue list failed to be obtained when the consumer subscribes to messages.
Cause: You did not create this topic in the console. As a result, the consumer failed to obtain the queue information of the topic during startup. Solution: Perform the following steps: i. Log in to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Instance List**.
ii. On the **Instance List** page, find the name of the instance that you want to manage and click the instance ID or click **Details** in the **Operation** column to go to the **Instance**
**details** page.
iii. Click the **Topic management** tab and then click **Create a Topic** to create a topic as prompted. iv. Click **Group management** tab and then click **Create Group ID** to create a group ID as prompted. v. Restart the application.
4. Messages failed to be sent.
A message failed to be sent after multiple retries. Possible causes: i. The ApsaraMQ for RocketMQ broker returned an error code to the producer. For more information about the error code, see the nested exception that corresponds to this exception. ii. After the ApsaraMQ for RocketMQ broker fails and before the producer detects the latest broker list, this exception temporarily occurs. iii. The producer timed out when it attempted to send a message. This problem may be caused by heavy loads on the broker or unstable network connectivity. Solutions: Perform the following steps: i. Try again later. This exception is temporary. The temporary timeout might be caused by the restart of the ApsaraMQ for RocketMQ broker or heavy loads on the broker. ii. If the problem persists after several retries, contact technical support for troubleshooting.
5. No exception is recorded.
Problem: No exception is recorded. Solution: Contact technical support.
6. The status of the message is Consumed, but the consumer is not aware of this.
The status of the message is Consumed, but the consumer log shows that the message is not received. Possible causes: The business code defines that the message is not immediately printed after the message is received. If the business logic is directly executed after a message is received, the message information is not recorded in the log if the code misses a specific logic branch. This leads to the false symptom that the message is not received. We recommend that you immediately print the message information after you receive a message to keep the information such as messageId, timestamp, and reconsumeTime. Multiple consumer instances are deployed. A consumer is often restarted multiple times at the debugging stage. If the previous process does not exit before the next process starts, multiple consumption processes coexist. In this case, multiple consumer instances share the message information. This scenario is similar to clustering consumption. A message that fails to be received by one consumer is received by another consumer. Log on to the ApsaraMQ for RocketMQ console, click the ID of the instance that you want to manage, click the **Group management** tab, and then click **Consumer status** in the Operation column. In the Consumer status panel, view the information in the
**Connection Information** section. The deployment information of consumer instances is
displayed, including the number of consumer instances and the IP address of each instance. You can check for the problem based on the information. An exception that failed to be caught occurred during the consumption of a message. As a result, the message is redelivered.

```java
public class MessageListenerImpl implements MessageListener {
    @Override
    public Action consume(Message message, ConsumeContext context) {
        // If the consumption logic throws an exception, the message is retried.
        doConsumeMessage(message);
        // If an exception that is not caught occurs in the doConsumeMessage()
method, this line of log is not printed.
        log.info("Receive Message, messageId:", message.getMsgID());
        return Action.CommitMessage;
```

If the problem persists, contact technical support and provide the local SDK logs.

#### Nonexistent resources

This topic describes exceptions related to nonexistent resources and provides solutions.
1. Nonexistent group ID
Cause: The group ID is not created in the ApsaraMQ for RocketMQ console. As a result, when the group ID is used to connect to the ApsaraMQ for RocketMQ broker, verification fails on the broker. Solution: Perform the following steps: i. Log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Groups**.
If the group ID already exists, proceed to the next step. If the group ID does not exist, create the group ID. Then, perform the next step. ii. Restart your application.
2. Nonexistent hostname
Cause: A possible cause is that the correct hostname or host IP address cannot be retrieved. To verify this assumption, run the **hostname** command. If the correct hostname cannot be retrieved, this assumption is true. Otherwise, this problem may be due to another reason. In this case, contact technical support engineers. Solution: Perform the following steps: i. On the host for which the error is reported, run the following command to check the hostname:

```
[root@iZ231wxgt6mZ ~]# hostname iZ231wxgt6mZ
```

If an error is returned, check whether an alias is defined for the hostname. For example, an alias can be alias xxx='hostname' in .bash_profile or .bashrc. Another possible cause is that the command path does not point to $PATH. ii. Ping the host.

```
[root@iZ231wxgt6mZ ~]# ping iZ231wxgt6mZ
```

If the hostname cannot be pinged, add the local IP address to the /etc/hosts file. By default, each Elastic Compute Service (ECS) instance establishes a binding relationship between the local IP address and the hostname. Do not manually remove the relationship. iii. Check the system configurations. Check whether the hostname recorded in /etc/sysconfig/network is the same as that added to /etc/hosts. If the hostname is not the same as that added to /etc/hosts, modify the hostname. If you modify the content in /etc/sysconfig/network, you must restart the host after you modify the content. This way, the modification can take effect. Exercise caution when you modify configurations in a system file, because this operation may cause other exceptions. After the preceding three steps are performed, UnknownHostException will no longer be returned when your client starts.

#### Inconsistent status

This topic describes the exceptions related to inconsistent status and provides solutions.
1. Invalid messages

**Cause:**

The message attribute or content is invalid in the following scenarios: The message is empty. The message content is empty. The message content is 0 character in length. The length of the message content exceeds the limit.

**Solution:**

Check whether the preceding exceptions occur to the message and handle the exceptions as prompted.
2. Invalid parameters

**Cause:**

The following table lists the cases in which the parameters are invalid.

| Nested exception | Description |
|---|---|
| consumeThreadMin Out of range [1, 1000] | The specified number of consumer threads is inappropriate. |

| consumeThreadMax Out of range [1, 1000] | The specified number of consumer threads is inappropriate. |
|---|---|
| messageListener is null | messageListener is not configured. |
| consumerGroup is null | The group ID is not specified. |
| msg delay time more than 40 day | The delay for the delivery of a scheduled message cannot exceed 40 days. |

**Solution:**

Perform the following steps: i. Modify the parameter settings for the client as prompted and make sure that the new parameter values are within the valid ranges. ii. Restart your application.
3. Abnormal client status

**Cause:**

i. After the consumer or producer is created, the return code does not show that the start() method is called to start the consumer or producer. ii. After the consumer or producer is created, the consumer or producer fails to start due to an exception in the start() process. iii. After the consumer or producer is created and the start() method is called, the return code shows that the shutdown() method is called to shut down the consumer or producer.

**Solution:**

Perform the following steps: i. Make sure that the start() method is called after the group ID is created. Make sure that the producer or consumer is started. ii. Check ons.log for exceptions that occur during the startup of the producer or consumer.
4. Subscription inconsistency

**Problem description:**

Multiple consumer instances are started in different JVM processes. Consumer instances identified by the same group ID subscribe to different topics, or subscribe to the same topic but different tags. As a result, the subscriptions of the consumer instances are inconsistent, and messages cannot be received as expected.

**Sample code of inconsistent subscriptions:**

Example 1: The consumer instance on JVM 1 and the consumer instance on JVM 2 use the same group ID GID-MQ-FAQ. The two consumer instances subscribe to different topics. The consumer instance on JVM 1 subscribes to MQ-FAQ-TOPIC-1, whereas the consumer instance on JVM 2 subscribes to MQ-FAQ-TOPIC-2.

**Code on JVM-1:**

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
    });
    consumer.start();
```

**Code on JVM-2:**

```java
     Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-2", "NM-MQ-FAQ", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
    });
    consumer.start();
```

Example 2: The consumer instance on JVM 1 and the consumer instance on JVM 2 use the same group ID GID-MQ-FAQ and subscribe to the same topic. However, the two consumer instances subscribe to different tags. The consumer instance on JVM 1 subscribes to NM- MQ-FAQ-1, whereas the consumer instance on JVM 2 subscribes to NM-MQ-FAQ-2.

**Code on JVM-1:**

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ-1", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
    });
    consumer.start();
```

**Code on JVM-2:**

```java
     Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ-2", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
    });
    consumer.start();
```

**Solution:**

If you start multiple consumer instances identified by the same group ID in different JVM processes, make sure that the topics and tags to which the consumer instances subscribe are the same.

### Troubleshooting

#### Unexpected consumer connections

This topic describes the symptoms of an unexpected consumer connection, analyzes causes, provides a solution, and verifies the solution.

**Problem description**

[Symptom 1]: Some messages are sent but not received. After you query message traces in the ApsaraMQ for RocketMQ console, the returned information shows that some messages are sent to the ApsaraMQ for RocketMQ broker, but the broker does not deliver the messages to consumers. To query message traces, log on to ApsaraMQ for RocketMQ console. In the left-navigation pane, click **Message Tracing**. On the Message Tracing page, click **Create Query Task**. In the Create Query Task dialog box, click the **By Message ID** tab. [Symptom 2]: Some consumer IP addresses are not within the expected range and messages are accumulated on the consumers that correspond to these IP addresses. To query connection information about consumers, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click **Groups**. On the Groups page, find the group ID whose connection information you want to view and click **Consumer Status** in the Actions column. In the Consumer Status panel, view the connection information in the
**Connection Information** section.

**Problem analysis**

**Analysis**: Log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane,
click **Groups**. On the Groups page, find the group ID whose connection information you want to view and click **Consumer Status** in the Actions column. In the Consumer Status panel, view the connection information in the **Connection Information** section. The connection information about all consumers identified by the group ID are displayed. You can check the IP address and process ID of the unexpected consumer and check whether the configurations loaded by the process are valid. The configurations include the AccessKey ID, AccessKey secret, topic, and group ID. If the configurations are invalid, the consumer process occupies some queues but cannot properly consume messages.
**Cause**: In the same environment, if a consumer identified by the group ID and configured
with an invalid AccessKey ID, AccessKey secret, and topic is started, this consumer process may occupy some queues of the topic but cannot properly consume messages. As a result, messages are accumulated on the ApsaraMQ for RocketMQ broker and cannot be properly delivered to downstream consumers whose IP addresses are within the expected range.
**Confirmation**: Locate the faulty process based on the connection status and check the
AccessKey ID, AccessKey secret, and topic of the process based on the /{user.home}/logs/ons.log file or program code.
**Solution**: This is a quick solution. Shut down the faulty consumer process first. Then, the
accumulated messages will be immediately rebalanced and delivered to proper consumers. After the fault is rectified, restart the faulty process.

**Verification**

Log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click **Groups**. On the Groups page, find the group ID that you want to view and click **Consumer Status** in the Actions column. In the Consumer Status panel, view the connection information of consumers identified by the group ID in the **Connection Information** section. The displayed information shows that IP addresses of all consumers are within the expected range and the value of **Consistent Subscription** is **Yes**.

#### Inconsistent subscriptions

This topic describes the symptoms of inconsistent subscriptions, analyzes causes, provides a solution, and verifies the solution.

**Problem description**

Consumers identified by a group ID failed to receive some messages to which they want to subscribe. To query messages, log on to the ApsaraMQ for RocketMQ console. In the leftside navigation pane, click **Message Query**. On the Message Query page, click the **By**
**Message ID** tab. Specify the corresponding topic and message ID. The displayed
information shows that the message has been consumed at least once. However, the message is considered unconsumed based on the consumption logic. The subscriptions of consumers identified by the group ID are inconsistent. To check whether the subscriptions of consumers are consistent, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click **Groups**. On the Groups page, find the group ID and click **Consumer Status** in the Actions column. In the Consumer Status panel, the value of **Consistent Subscription** is **No**.

**Problem analysis**

In ApsaraMQ for RocketMQ, a group ID represents a consumer instance group. For most distributed applications, multiple consumer instances are attached to the same group ID. Subscription consistency means that the topics and tags of all consumer instances identified by the same group ID must be identical. If the consumer instances identified by the same group ID subscribe to different topics, or subscribe to the same topic but different tags, the subscriptions are inconsistent. If the subscriptions are inconsistent, errors occur in the message consumption logic and messages may be lost.
**[Cause 1]:** The topics subscribed to by consumers with the same group ID are different.
**Example 1:** Two consumers identified by the group ID GID-MQ-FAQ subscribe to different
topics: MQ-FAQ-TOPIC-1 and MQ-FAQ-TOPIC-2.

**Code on JVM-1:**

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
    });
    consumer.start();
```

**Code on JVM-2:**

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-2", "NM-MQ-FAQ", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
    });
    consumer.start();
```

**[Cause 2]:** Two consumers identified by the same group ID subscribe to the same topic
but different tags.
**Example:** Two consumers identified by the group ID GID-MQ-FAQ subscribe to the same
topic but different tags: NM-MQ-FAQ-1 and NM-MQ-FAQ-2.

**Code on JVM-1:**

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ-1", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
    });
    consumer.start();
```

**Code on JVM-2:**

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ-2", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
    });
    consumer.start();
```

**Solution**

Perform the following steps:
1. Check the subscription code of different consumers. Make sure that the subscriptions of all
consumers identified by the same group ID are consistent. This means that the topics and tags subscribed to by the consumers are all identical.
2. Restart all consumer applications.

**Verification**

Consumers can receive messages as expected. Log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Groups**. On the Groups page, find the group ID that you want to view and click **Consumer**
**Status** in the Actions column. In the Consumer Status panel, the value of **Consistent**
**Subscription** is **Yes**.

#### Message accumulation

This topic describes the symptoms of message accumulation, analyzes causes, provides a solution, and verifies the solution.

**Problem description**

The value of **Accumulated Messages** is higher than expected. To query the number of accumulated messages, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click **Groups**. On the Groups page, find the group ID that you want to view and click **Consumer Status** in the Actions column. In the Consumer Status panel, check the value of Accumulated Messages in the Connection Information section. Some messages have been sent to the ApsaraMQ for RocketMQ broker but are not delivered to consumers. To query message traces, log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click **Message Tracing**. On the Message Tracing page, click **Create Query Task**. In the Create Query Task dialog box, click the **By**
**Message ID** tab. Specify the corresponding topic and message ID to query the trace of a
message.

**Problem analysis**

In ApsaraMQ for RocketMQ, messages are first sent to the broker. Then, consumers identified by the group ID pull some messages from the broker to the on-premises machine for consumption based on the current consumer offset. In the consumption process, it may take a long time to consume a single message due to various reasons, such as access to locked shared resources, competition for I/O and network resources, and no timeout set for HTTP calls. As a result, messages start to accumulate on the broker. If messages are not accumulated, check whether the threshold value is excessively small and causes alerts on message accumulation.

**Solution**

**Perform the following operations for troubleshooting:**

Log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Resource Statistics**. On the Resource Statistics page, click the **Message Consumption**
tab. Enter the information to query historical consumption records. If message writing is faster than message consumption, modify the code or scale out the consumer. Print the Jstack information **jstack -l {PID} | grep ConsumeMessageThread** in the application. If messages are blocked, print the Jstack information for five consecutive times and identify the spot where the consumer thread is stuck. Then, rectify the fault and restart the application. Check whether messages can be consumed.

**Verification**

Print the Jstack information **jstack -l {PID} | grep ConsumeMessageThread** in the application. Verify that no consumer thread is blocked. Log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click
**Groups**. On the Groups page, find the group ID that you want to view and click **Consumer**
**Status** in the Actions column. In the Consumer Status panel, check whether the value of
**Real-time Consumption Speed** increases and the value of **Accumulated Messages**
decreases.

#### Message accumulation in Java

**processes**

**Symptoms**

In the **Consumer Status** panel of the ApsaraMQ for RocketMQ console, the number of realtime accumulated messages of the group ID is higher than expected, and the performance is much lower.

**Causes**

The number of real-time accumulated messages of the group ID is higher than expected due to an excessive number of messages accumulated in the Java process.

**Solutions**

1. Log on to the ApsaraMQ for RocketMQ console. Navigate to the Consumer Status panel,
obtain the host IP address of the consumer instance that has accumulated messages, and then log on to the host or container.
2. Run one of the following commands to view the PID of the Java process and record the PID:

```
ps -ef |grep java jps -lm
```

3. Run the following command to view the stack information:

```
jstack -l pid > /tmp/pid.jstack
```

4. Run the following command to view the information about `ConsumeMessageThread` and
focus on the thread status and stack:

```
cat /tmp/pid.jstack|grep ConsumeMessageThread -A 10 --color
```

The following figure shows an example of command output. For more information about the thread status, see official Java documentation.

**Note**

ApsaraMQ for RocketMQ can support 1 billion accumulated messages without compromising the performance. If the problem of compromised performance is not solved after you perform the preceding steps, contact O&M engineers and provide the following information: The heap.bin file. Run the jmap -dump:format=b,file=heap.bin [$PID] command to obtain this file. Then, run the `gzip heap.bin` command to generate a compressed package.[$PID] represents the PID of the Java process recorded in Step 2. The local ons.log file of the consumer client where messages are accumulated. The version of the consumer client.

#### Application OOM due to message

**caching on the client**

This topic describes the symptoms of application out of memory (OOM), analyzes causes, provides solutions, and verifies each solution.

**Problem description**

[Symptom 1]: The memory is exhausted on the machine where the application is deployed. [Symptom 2]: The keyword OutOfMemory can be found in `/{user.home}/logs/ons.log` . [Symptom 3]: In the ApsaraMQ for RocketMQ console, **Real-time Accumulated**
**Messages** in the **Consumer Status** panel of the **Groups** page shows that a large number
of messages are accumulated. The Connection Information section displays the number of accumulated messages for each connected consumer client. In addition, the result of check by running the jstack command indicates that `ConsumeMessageThread_` is not blocked.

**Analysis**

**Analysis**: A ApsaraMQ for RocketMQ consumer proactively pulls messages from the
ApsaraMQ for RocketMQ broker and caches them to the client. Then, the messages are consumed based on the consumption logic of the client. In versions earlier than 1.7.0.Final, the client caches up to 1,000 messages for each queue of each topic by default. Assume that each topic has 16 queues (two primary brokers and two secondary brokers, and eight queues on each broker). The average size of a message in this topic is 64 KB. The final message size cached for this topic on the client is calculated by using the following formula: 16 × 1000 × 64 KB = 1 GB. If you subscribe to eight topics at the same time and caches messages of all these topics in the client memory, the memory consumed will exceed the memory size specified in the JVM configuration. In this case, OOM occurs. [Cause 1]:An ons-client version earlier than 1.7.0.Final is depended on, and the average size of a message in each topic exceeds 4 KB. In addition, message consumption is slow. This is prone to message caching in the memory of the client.
**Confirmation**: Check whether the keyword OutOfMemory can be found in

| /{user.home}/logs/ons.log |   |
|---|---|
|   | command to detect th |

`/{user.home}/logs/ons.log` , or run the `jmap -dump:live,format=b,file=heap.bin` `<pid>` command to detect the objects that occupy a large amount of memory.
**Solution**: Update the ons-client version to 1.7.0.Final or later and set the

```
 com.aliyun.openservices.ons.api.PropertyKeyConst#MaxCachedMess ageSizeInMiB
```

parameter to an appropriate value for the corresponding ConsumerBean. Then, restart the application. [Cause 2]:ons-client-1.7.0.Final or later is depended on, and the default maximum memory consumed is 512 MB, which is the total cache capacity of all topics to which consumer instances identified by a group ID subscribe. If the application still suffers OOM, set the

```
 com.aliyun.openservices.ons.api.PropertyKeyConst#MaxCachedMessageSizeInMiB  parameter
```

to a value within the valid range from 16 MB to 2048 MB to customize the maximum memory that can be consumed during the startup of ConsumerBean.
**Confirmation**: Check the ons-client version used by the application and check the
memory size allocated to the process based on the JVM configuration.
**Solution**: Set the `com.aliyun.openservices.ons.api.PropertyKeyConst#MaxCachedMess`
`ageSizeInMiB` parameter for the corresponding ConsumerBean, based on the memory usage of the machine where the application runs. Then, restart the application.

**Verification**

[Verification 1]: The keyword OutOfMemory disappears from `/{user.home}/logs/ons.log` . [Verification 2]: Log on to the ApsaraMQ for RocketMQ console. In the left-side navigation pane, click **Groups**. On the Groups page, select your instance and click **Consumer Status** in the Actions column. In the Consumer Status panel, the value of **Real-time**
**Consumption Speed** increases, whereas the value of **Real-time Accumulated**
**Messages** decreases.
