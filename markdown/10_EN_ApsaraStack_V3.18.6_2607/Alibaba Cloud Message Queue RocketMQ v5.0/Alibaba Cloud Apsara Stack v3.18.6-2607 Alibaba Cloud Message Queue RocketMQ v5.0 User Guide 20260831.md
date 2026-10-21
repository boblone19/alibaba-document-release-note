---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue RocketMQ v5.0 User Guide 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 178
source_pdf: "55f38d68ac5e7d76_Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue RocketMQ v5.0 User Guide 2026083"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97%20RocketMQ%20%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Alibaba%20Cloud%20Message%20Queue%20RocketMQ%20v5.0%20User%20Guide%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue RocketMQ v5.0 User Guide 20260831

## Table of Contents

- 1 ApsaraMQ for RocketMQ v5.0
- 2 Getting started
  - 2.1 Log in to the ApsaraMQ for RocketMQ v5.0 console
  - 2.2 Overview
  - 2.3 Create resources
  - 2.4 Send messages
    - 2.4.1 Send messages in the console
    - 2.4.2 Use the TCP client SDK for Java to send and subscribe to normal messages
    - 2.4.3 Check whether messages are sent
  - 2.5 Subscribe to messages
  - 2.6 Use Apsara Copilot
- 3 Message types
  - 3.1 Normal messages
  - 3.2 Scheduled and delayed messages
  - 3.3 Transactional messages
  - 3.4 Ordered messages
- 4 Console guide
  - 4.1 Resource management
    - 4.1.1 Overview
    - 4.1.2 Manage instances
    - 4.1.3 Manage topics
    - 4.1.4 Manage groups
  - 4.2 Network management
  - 4.3 ACL account management
  - 4.4 ACL rule management
  - 4.5 Message query
    - 4.5.1 Overview
    - 4.5.2 Query messages
    - 4.5.3 Message query results
  - 4.6 Message traces
    - 4.6.1 Overview
    - 4.6.2 Query message traces
    - 4.6.3 States in message traces
  - 4.7 View consumer status
  - 4.8 Reset consumer offsets
  - 4.9 Manage dead-letter queues
  - 4.10 Message routing
    - 4.10.1 Replicator
    - 4.10.2 Connect instance
- 5 SDK user guide
  - 5.1 SDK overview
  - 5.2 TCP client SDK reference
    - 5.2.1 Demo projects
      - 5.2.1.1 Overview
      - 5.2.1.2 Prepare the environment
      - 5.2.1.3 Configure a demo project
      - 5.2.1.4 Run a demo project
    - 5.2.2 Client parameters
    - 5.2.3 Client error codes
    - 5.2.4 Java SDK
      - 5.2.4.1 Instructions for use
      - 5.2.4.2 Environment preparations
      - 5.2.4.3 Logging configurations
      - 5.2.4.4 Spring integration
        - 5.2.4.4.1 Overview
        - 5.2.4.4.2 Integrate a producer with Spring
        - 5.2.4.4.3 Integrate a transactional message producer with Spring
        - 5.2.4.4.4 Integrate a consumer with Spring
      - 5.2.4.5 Three modes for sending messages
        - 5.2.4.5.1 Overview
        - 5.2.4.5.2 Reliable synchronous transmission
        - 5.2.4.5.3 Reliable asynchronous transmission
        - 5.2.4.5.4 One-way transmission
      - 5.2.4.6 Send messages by using multiple threads
      - 5.2.4.7 Send and subscribe to ordered messages
      - 5.2.4.8 Send and subscribe to transactional messages
      - 5.2.4.9 Send and subscribe to delayed messages
      - 5.2.4.10 Send and subscribe to scheduled messages
      - 5.2.4.11 Subscribe to messages
    - 5.2.5 C/C++ SDK
      - 5.2.5.1 Prepare the SDK for C or C++ environment
        - 5.2.5.1.1 Overview
        - 5.2.5.1.2 Download SDK for C or C++
        - 5.2.5.1.3 Use SDK for C++ in Linux
      - 5.2.5.2 Send and subscribe to normal messages
      - 5.2.5.3 Send and subscribe to ordered messages
      - 5.2.5.4 Send and subscribe to scheduled messages
      - 5.2.5.5 Send and subscribe to transactional messages
      - 5.2.5.6 Subscribe to messages
    - 5.2.6. .NET SDK
      - 5.2.6.1 Prepare the .NET SDK environment
        - 5.2.6.1.1 Overview
        - 5.2.6.1.2 Download SDK for .NET
        - 5.2.6.1.3 Configure SDK for .NET
      - 5.2.6.2 Send and subscribe to normal messages
      - 5.2.6.3 Send and subscribe to ordered messages
      - 5.2.6.4 Send and subscribe to scheduled messages
      - 5.2.6.5 Send and subscribe to transactional messages
      - 5.2.6.6 Subscribe to messages
- 6 Best practices
  - 6.1 Clustering consumption and broadcasting consumption
  - 6.2 Message filtering
  - 6.3 Subscription consistency
  - 6.4 Consumption idempotence
  - 6.5 Message routing
- 7 Product usage issues
  - 7.1 FAQ
    - 7.1.1 Quick start
    - 7.1.2 Configuration
    - 7.1.3 Message trace
    - 7.1.4 Alarm handling
    - 7.1.5 Ordered messages
  - 7.2 Exception types
    - 7.2.1 Usage exceptions
    - 7.2.2 Resource not found
    - 7.2.3 Inconsistent state
  - 7.3 Troubleshooting
    - 7.3.1 Unexpected client connections
    - 7.3.2 Inconsistent subscriptions
    - 7.3.3 Message accumulation in a Java process
    - 7.3.4 OOM error from client-side message caching
    - 7.3.5 Message delivery fails with AuthenticationException

aMQ for RocketMQ v5.0

## 1 ApsaraMQ for RocketMQ v5.0

**v5.0**

ApsaraMQ for RocketMQ v5.0 is a distributed messaging middleware that is developed by Alibaba Cloud based on Apache RocketMQ v5.0. It features low latency, high concurrency, high availability, and high reliability. ApsaraMQ for RocketMQ v5.0 is a core service in the enterprise-level Internet architecture. Using the highly available distributed cluster technology, it offers a series of messaging services in the cloud, including message subscription and publishing, message trace query, scheduled and delayed messages, and resource statistics. ApsaraMQ for RocketMQ v5.0 provides asynchronous decoupling and peak-load shifting capabilities for distributed application systems. It also supports various features for Internet applications, including accumulation of large numbers of messages, high throughput, and reliable message consumption retries. ApsaraMQ for RocketMQ v5.0 is one of the core cloud services that are used to support Double 11. ApsaraMQ for RocketMQ v5.0 supports connections over TCP and supports multiple programming languages such as Java, C++, and .NET. This allows you to connect applications that are developed in different programming languages to ApsaraMQ for RocketMQ v5.0. ApsaraMQ for RocketMQ v5.0 uses a storage-compute decoupled architecture to support independent scaling of computing and storage resources. This enables a lighter-weight deployment mode and a more flexible and miniaturized cluster configuration, reducing resource overheads and O&M complexity. g started

## 2 Getting started

### 2.1 Log in to the ApsaraMQ for RocketMQ v5.0 console

**RocketMQ v5.0 console**

This topic describes how to log in to the ApsaraMQ for RocketMQ v5.0 console.

**Prerequisites**

You have obtained the service domain name for the Apsara Uni-manager Management Console from the deployment personnel. Use the Google Chrome browser.

**Procedure**

1. In the address bar of your browser, enter the service domain name for the Apsara Uni-
manager Management Console and press Enter. g started

> **Note:** You can click the current language in the upper-right corner to switch to another language.

2. Enter your username and password.

> **Note:** You can obtain the username and logon password from an operations administrator.
> If this is your first time logging on to the Apsara Uni-manager Management Console, you must change your password. For security, the password must be 10 to 32 characters long and contain uppercase letters, lowercase letters, digits, and special characters. The supported special characters are: !, @, #, $, and %.

3. Select **I Have Read And Agree To The Product Service Agreement, Privacy**
**Agreement, And User Agreement**.

**Note**

The link text on the logon page is the title of the agreement document. You can click the link to view the details of the agreement.

> The **Product Service Agreement**, **Privacy Agreement**, and **User** **Agreement** are displayed only if they have been published. If none of these agreements are published, you can skip this step.

4. Click **Account Logon** or **Authorized Logon**.

> **Note:** The Authorized Logon button is displayed only if the global IdP setting for third-party authentication is enabled. This display name can be customized. The default name is "Authorized Logon".

5. If multi-factor authentication (MFA) is enabled for your account, follow the steps for one of
the following scenarios:

> **Note:** When you log on from the Internet, multi-factor authentication (MFA) is mandatory by default.

**First logon after MFA is enabled**

a. After you log on with your username and password, the Bind Virtual MFA Device page appears. b. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind a virtual MFA device. c. You have logged in to the console.

**MFA is already enabled and a device is bound**

Enter the six-digit MFA code and click **Authenticate**. g started
6. In the top navigation bar, choose **Products > Middleware > ApsaraMQ > ApsaraMQ**
**for RocketMQ** to go to the ApsaraMQ for RocketMQ console.
7. In the left-side navigation pane, click **Switch** to the right of **v4.0**, and then click **OK** in the
message that appears to switch the environment to **v5.0**.

### 2.2 Overview

ApsaraMQ for RocketMQ v5.0 provides TCP client SDKs for multiple programming languages. You can use the SDKs to send and subscribe to different types of messages. This topic describes how to use TCP client SDKs for multiple programming languages to send and subscribe to normal messages and the relevant usage notes.

**Background information**

If your application that is deployed on a server uses ApsaraMQ for RocketMQ v5.0, we recommend that you use an SDK to access ApsaraMQ for RocketMQ v5.0. This method is easy to use and provides high availability. As a quick start guide, this topic demonstrates how to access ApsaraMQ for RocketMQ v5.0 to send and subscribe to messages. In the example, TCP client SDK for Java is used. ApsaraMQ for RocketMQ v5.0 supports four types of messages. For more information, see Message types. In the following example, normal messages are used. The topic that you create by performing the steps that are described in this section cannot be used to send or subscribe to messages of other types. Each topic can be used to send and subscribe to messages only of a specific type.

**Process**

You can follow the process illustrated in the following figure based on the protocol that you select. g started
1. Create an instance
(ApsaraMQ for RocketMQ v5.0 console)
2. Create a topic
(ApsaraMQ for RocketMQ v5.0 console) Create resources
3. Create a TCP Group ID
(ApsaraMQ for RocketMQ v5.0 console)
4. Obtain a TCP endpoint
(ApsaraMQ for RocketMQ v5.0 console)
5. Download and install a
TCP client SDK
6. Run TCP sample code
Use SDKs to send messages to send and
7. Run TCP sample code
subscribe to subscribe to messages to
1. Create resources: You must create an ApsaraMQ for RocketMQ v5.0 instance, a topic, and a
group, and obtain the endpoint of the instance.
2. Use the corresponding SDK to send and subscribe to messages based on the protocol that
you select. Use the TCP client SDK for Java to send and subscribe to normal messages

**References**

To send and subscribe to messages by using TCP client SDKs for other programming languages, see the following documentation:

**TCP**

SDK for C and C++: Send and subscribe to normal messages SDK for .NET: Send and subscribe to normal messages

### 2.3 Create resources

Before you use a client SDK to send and receive messages, you must create the required resources and obtain the resource information in the ApsaraMQ for RocketMQ v5.0 console. When you use the SDK, you must specify the resource parameters based on the resource information.

**Background information**

If a new application needs to access ApsaraMQ for RocketMQ v5.0, you must create the following ApsaraMQ for RocketMQ resources for the application: g started
**Instance**: An instance is a VM resource of ApsaraMQ for RocketMQ v5.0 that is used to
store information about topics and group IDs.
**Topic**: a topic. In ApsaraMQ for RocketMQ v5.0, a producer sends a message to a specific
topic, and a consumer subscribes to the topic to obtain and consume the message.
**Group ID**: A group ID is used to identify a group of producers or consumers.
**Endpoint**: You can use an endpoint to connect producer or consumer clients to a specific
ApsaraMQ for RocketMQ v5.0 instance.
*************************************: the user credentials that are used to verify the
identity of the user. For more information about how to obtain an AccessKey pair, see
**Obtain an AccessKey pair** in ApsaraMQ for RocketMQ v5.0 **Developer Guide**.

**Step 1: Create an instance**

For more information, see Create an instance.

**Step 2: Create a topic**

For more information, see Create a topic.

**Step 3: Create a group ID**

For more information, see Manage groups.

**Step 4: View the endpoints of the instance**

For more information, see View endpoints.

### 2.4 Send messages

#### 2.4.1 Send messages in the console

After you create a topic in the ApsaraMQ for RocketMQ v5.0 console, you can send messages in the console to verify the availability of the topic.

**Procedure**

1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
4. On the **Instance details** page, click the **Topic Management** tab.
5. On the **Topic Management** tab, find the topic that you created and click **Send message**
in the **Operation** column.
6. In the **Send message** dialog box, enter the message content in the **Message Body** field
and click **OK**. Table 1. Parameters for sending messages

| Parameter | Description |
|---|---|

g started

| Tag | A tag is a label that classifies messages into different types in a topic in ApsaraMQ for RocketMQ v5.0. ApsaraMQ for RocketMQ v5.0 allows consumers to filter messages by using tags. This ensures that the consumers consume only messages that they are concerned with. |
|---|---|
| Key | The key of the message. It is the key attribute of the message. Keep the key unique and business-distinctive whenever possible. ApsaraMQ for RocketMQ v5.0 creates an index for messages based on message keys that you specify. This way, when you query messages by message key, ApsaraMQ for RocketMQ v5.0 returns the messages that match the index. |
| Message Body | The body of the message. |

After the message is sent, a success prompt and the corresponding message ID are returned.

#### 2.4.2 Use the TCP client SDK for Java to send and subscribe to normal messages

**and subscribe to normal messages**

After you create the required resources in the ApsaraMQ for RocketMQ v5.0 console, you can use TCP client SDKs of ApsaraMQ for RocketMQ v5.0 to send and subscribe to normal messages.

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

The following sample code provides an example on how to use the TCP client SDK for Java to send normal messages. Before you run the code, we recommend that you specify the information about the required resources that are created in advance based on the comments included in the code. `i` `t` `li` `i` `i``M` g started

|   | import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.Producer; import com.aliyun.openservices.ons.api.SendResult; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import java.util.Properties; public class ProducerTest { public static void main(String[] args) { Properties properties = new Properties(); // Specify the ID of the group that you created for TCP clients in the ApsaraMQ for RocketMQ v5.0 console. properties.put(PropertyKeyConst.GROUP ID, "XXX"); _ // Specify your AccessKey ID. The AccessKey ID is used for identity authentication. properties.put(PropertyKeyConst.AccessKey,"XXX"); // Specify your AccessKey secret. The AccessKey secret is used for identity au thentication. properties.put(PropertyKeyConst.SecretKey, "XXX"); // Specify the TCP endpoint of your instance. You can view the TCP endpoint on the Network Management tab of the Instance details page in the ApsaraMQ for RocketMQ v5 .0 console. properties.put(PropertyKeyConst.NAMESRV ADDR,"XXX"); _ Producer producer = ONSFactory.createProducer(properties); // Before you send a message, call the start() method only once to start the p roducer. producer.start(); // Cyclically send messages. while(true){ Message msg = new Message( // Specify the topic that you created in the ApsaraMQ for RocketMQ v5.0 console. The value is the name of the topic to which you want to send messages. "TopicTestMQ", // Message Tag, // Specify a message tag, which is similar to a Gmail tag. It is used t o sort messages and help the consumer filter messages on the ApsaraMQ for RocketMQ v5.0 broker based on specified conditions. "TagA", // Message Body // Specify the message body in the binary format. ApsaraMQ for RocketMQ v5.0 does not process the message body. // The producer and consumer must agree on the methods that are used to serialize and deserialize message bodies. "Hello MQ".getBytes()); // Specify a message key. The message key is the business-specific attribute of the message and must be globally unique. A unique key helps you query and resend a message in the console if the message fails to be received. // Note: A message can be sent and received even if you do not specify a m essage key. msg.setKey("ORDERID 100"); _ // Send the message. If no exception is thrown, the message is sent. // Print the message ID. The message ID can be used to query the sending status of the message. SendResult sendResult = producer.send(msg); System.out.println("Send Message success. Message ID is: " + sendResult getMessageId()); |   |
|---|---|---|

g started

```
sendResult.getMessageId());
```

`}`

```
         // Before you exit the application, shut down the producer.
         // Note: This operation is optional.
         producer.shutdown();
```

`}` `}` You can also send messages by performing the following operations in the ApsaraMQ for RocketMQ v5.0 console: On the **Topic Management** tab, find the topic that you created, and click **Send message** in the **Operation** column.

**Use the TCP client SDK for Java to subscribe to normal**

**messages**

The following sample code provides an example on how to use the TCP client SDK for Java to subscribe to normal messages. Before you run the code, we recommend that you specify the information about the required resources that are created in advance based on the comments included in the code.

```java
import com.aliyun.openservices.ons.api.Action; import com.aliyun.openservices.ons.api.ConsumeContext; import com.aliyun.openservices.ons.api.Consumer; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.MessageListener; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import java.util.Properties; public class ConsumerTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
        // Specify the ID of the group that you created for TCP clients in the ApsaraMQ
for RocketMQ v5.0 console.
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
        // Specify your AccessKey ID. The AccessKey ID is used for identity
authentication.
         properties.put(PropertyKeyConst.AccessKey,"XXX");
         // Specify your AccessKey secret. The AccessKey secret is used for identity au
thentication.
         properties.put(PropertyKeyConst.SecretKey, "XXX");
         // Specify the TCP endpoint of your instance. You can view the TCP endpoint on
the Network Management tab of the Instance details page in the ApsaraMQ for RocketMQ v5 .0 console.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,"XXX");
        Consumer consumer = ONSFactory.createConsumer(properties);
        consumer.subscribe("TopicTestMQ", "*", new MessageListener() {
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
```

`}`

```java
        });
        consumer.start();
        System.out.println("Consumer Started");
```

`}` `}` g started

**Check whether message subscription is successful**

1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
4. On the **Instance details** page, click the **Group Management** tab.
5. In the group list, find the group ID for the consumer of which you want to view the
subscription, and click **Subscription relationship** in the **Operation** column. If the value of the **Online or not** parameter is **Yes**, the consumer has been started and the subscription is successful. Otherwise, the subscription fails.

**What to do next**

#### 2.4.3 Check whether messages are sent

After you send a message, you can check the status of the message in the ApsaraMQ for RocketMQ v5.0 console.

**Procedure**

1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
4. On the **Instance details** page, click the **Message Query** tab.
5. On the **Message Query** tab, click the **Query by Message ID** tab.
6. Enter the topic name in the **Topic** field and the message ID returned after the message is
sent in the **Message ID** field, and then click **Query** to query the sending status of the message.
**Storage time** indicates the time when the message is stored on the ApsaraMQ for
RocketMQ v5.0 broker. If the message appears in the search results, the message has been sent to the ApsaraMQ for RocketMQ v5.0 broker.

> **Important:** This step demonstrates the situation where ApsaraMQ for RocketMQ v5.0 is used for the first time, and the consumer has never been started. Therefore, no consumption data is displayed in the message status information.

**What to do next**

You can start the consumer and subscribe to messages. For more information, see Subscribe to messages. For more information about message states, see Message query and States in message traces.

### 2.5 Subscribe to messages

g started After a message is sent, the consumer can subscribe to the message. You must use the SDK corresponding to the protocol and programming language to subscribe to the message. This topic describes how to use ApsaraMQ for RocketMQ v5.0 TCP client SDK for Java to subscribe to messages.

**Procedure**

1. Run the following sample code to test the message subscription feature. Specify
parameters based on the descriptions before you run the code.

```java
import com.aliyun.openservices.ons.api.Action; import com.aliyun.openservices.ons.api.ConsumeContext; import com.aliyun.openservices.ons.api.Consumer; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.MessageListener; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import java.util.Properties; public class ConsumerTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
        // The ID of the consumer group that you created in the ApsaraMQ for RocketMQ
v5.0 console.
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
        // The AccessKey ID used for identity authentication.
        properties.put(PropertyKeyConst.AccessKey, "XXX");
        // The AccessKey secret used for identity authentication.
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The TCP endpoint. You can view the TCP endpoint on the Network Management
tab of the Instance details page in the ApsaraMQ for RocketMQ v5.0 console.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,"XXX");
        Consumer consumer = ONSFactory.createConsumer(properties);
        consumer.subscribe("TopicTestMQ", "*", new MessageListener() {
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
```

`}`

```java
        });
        consumer.start();
        System.out.println("Consumer Started");
```

`}` `}` After you run the code, you can check whether the consumer is started in the ApsaraMQ for RocketMQ v5.0 console. This operation checks whether the message subscription is successful.
2. Log in to the RocketMQ v5.0 console.
3. In the left-side navigation pane, click **instance list**.
4. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
5. On the **Instance Details** page, click the **Group Management** tab.
6. In the group list, find the group ID for the consumer of which you want to view the
subscription, and click **Subscription relationship** in the **Operation** column. g started If the value of the **Online or not** parameter is **Yes**, the consumer has been started and the subscription is successful. Otherwise, the subscription fails.

### 2.6 Use Apsara Copilot

Apsara Copilot is an intelligent tool provided by Alibaba Cloud to help you manage and maintain ApsaraMQ for RocketMQ v5.0 instances more efficiently. You can use Apsara Copilot to query resource information, trigger operations, diagnose instances, and request technical support. Apsara Copilot helps you improve the O&M efficiency and user experience. This topic describes how to use Apsara Copilot and provides some sample conversations. We recommend that you refer to the sample conversations based on your actual business scenario.

> **Important:** The results generated by Apsara Copilot cannot be used as the basis for final technical support conclusions or business decisions. Alibaba Cloud shall not be liable for any direct or indirect losses caused by taking actions based on the output of Apsara Copilot.
> The query results returned by Apsara Copilot are automatically generated by AI models. The results may not be completely accurate and are for reference only. We recommend that you verify the accuracy of the results based on the actual situation.

**Prerequisites**

The user, as an operations administrator, has enabled the display of the AI assistant in the Apsara Uni-manager Management Console under **Configurations** > **Apsara Copilot** >
**Custom Settings**.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. Click
in the top navigation bar or floating menu to enter Apsara Copilot. g started
3. In the **Apsara Copilot** input box, enter the questions that you want to ask and click the
icon.

| Scenario | Description |
|---|---|
| Knowledge Q&A | Provides accurate answers and guidance for usage-related questions regarding cloud service recommendations, feature operations, limitations, and best practices. |

g started

| Resource Search | Precisely locates target resources, provides detailed information, and enables viewing of associated resources. |
|---|---|
| Resource Operation | Supports operations such as creating, modifying, and deleting cloud resources to simplify your resource management process. |
| Bill Analysis | Analyzes your cloud resource usage costs, generates detailed expense reports, and provides optimization suggestions to reduce overall spending. |
| Resource Analysis | Tracks cloud resource usage, including utilization and performance metrics, to help you fully understand resource status and optimize resource allocation. |
| Code Generation | Automatically generates code samples in multiple programming languages for OpenAPI and Terraform based on your requirements, improving development efficiency and code quality. |

> **Note:** Apsara Copilot supports multiple models. You can switch between different models to ask questions. If the selected model supports deep thinking, you can enable or disable the deep thinking mode.
> You can click the
> icon in the input box to enable or disable Model Context
> Protocol (MCP) and internal network-based search.
> After you enable MCP and select cloud services (ApsaraMQ for RocketMQ v5.0) that you want to integrate, you can call the MCP services of the cloud services.
> The switch for internal network-based search is displayed in the Apsara Copilot pane only after Intranet Search is turned on by an operations administrator on the Custom Settings page of Apsara Copilot. You can enable the internal network-based search feature only after you turn on Intranet Search on the Custom Settings page of Apsara Copilot.
> For more information about how to use Apsara Copilot, see **Apsara Copilot** **User Guide**.

age types

## 3 Message types

### 3.1 Normal messages

This topic describes the definition of normal messages and provides the sample code for sending and subscribing to normal messages. Normal messages are featureless messages provided by ApsaraMQ for RocketMQ v5.0. Normal messages are different from featured messages, including Scheduled messages and delayed messages, Transactional messages, and Ordered messages. The following sample code shows how to send and subscribe to normal messages.

**Sample code for using TCP client SDKs**

For information about the sample code for using TCP client SDKs to send and subscribe to normal messages, see the following topics: SDK for Java: SDK for C or C++: Send and subscribe to normal messages SDK for .NET: Send and subscribe to normal messages

### 3.2 Scheduled and delayed messages

**messages**

This topic introduces the concepts related to scheduled messages and delayed messages and describes the scenarios, methods, and usage notes of using these messages in ApsaraMQ for RocketMQ v5.0.

**Terms**

Scheduled message: A scheduled message is not immediately sent to consumers after the ApsaraMQ for RocketMQ v5.0 broker receives the message from the producer. The broker is configured to send the message to consumers at a specific point in time later than the current time. Delayed message: A delayed message is not immediately sent to consumers after the ApsaraMQ for RocketMQ v5.0 broker receives the message. The broker is configured to send the message to consumers after a specific period of time elapses. Scheduled messages and delayed messages are slightly different in coding, but are consistent in the effect. Scheduled messages and delayed messages are not immediately sent to consumers after the ApsaraMQ for RocketMQ v5.0 broker receives the messages. These messages are sent to consumers after being delayed for a specific period of time, which is specified in the attributes of the messages.

**Applicable scenarios**

Scheduled messages and delayed messages can be used in the following scenarios: age types A time window between message production and message consumption is required. For example, when a transaction order is created on an e-commerce platform, a producer sends a delayed message to the ApsaraMQ for RocketMQ v5.0 broker. A delay of 30 minutes is specified for the message to be sent to a consumer. The message is used to remind the consumer to check whether the order is paid. If the order is not paid, the related system closes the order. If the order is paid, the consumer ignores the message. Scheduled messages are sent to trigger scheduled tasks. For example, a notification message is sent to a user at a specified point in time.

**How to use these messages**

Scheduled messages and delayed messages are slightly different in coding: If you want to send a scheduled message, specify a point in time that is later than the point in time when the message is sent by a producer. The broker sends the message to consumers at the specified point in time. If you want to send a delayed message, specify a period of time that starts from the point in time when the message is sent by a producer. The broker sends the message to consumers after the specified period of time elapses.

**Usage notes**

The **msg.setStartDeliverTime** parameter for a scheduled message or delayed message must be set to a specific point in time after the current timestamp. Unit: milliseconds. If the scheduled time is earlier than the current time, the message is immediately sent to the consumer. The **msg.setStartDeliverTime** parameter for a scheduled message or delayed message can be set to a specific point in time within three days after the scheduled message or the delayed message is generated. Unit: milliseconds. If the specified point in time is not within the three days, the message cannot be sent. The **StartDeliverTime** parameter specifies the time when the ApsaraMQ for RocketMQ v5.0 broker starts to send messages to the consumer. If accumulated messages exist, scheduled messages or delayed messages are queued after the accumulated messages and cannot be sent to the consumer at the specified time. Due to the potential time difference between the client and the broker, the actual delivery time may be different from the delivery time specified on the client. Scheduled messages and delayed messages can be retained for at most three days on the ApsaraMQ for RocketMQ v5.0 broker.

**Sample code for using TCP client SDKs**

For information about the sample code for using TCP client SDKs to send and subscribe to scheduled messages or delayed messages, see the following topics: SDK for Java: SDK for C++: Send and subscribe to scheduled messages SDK for .NET: Send and subscribe to scheduled messages

### 3.3 Transactional messages

This topic introduces the terms that are related to transactional messages in ApsaraMQ for RocketMQ v5.0. This topic also describes the scenarios, methods, and usage notes of using transactional messages. age types

**Terms**

Transactional message: ApsaraMQ for RocketMQ v5.0 provides a distributed transaction processing feature that is similar to X/Open XA to ensure transaction consistency by using transactional messages of ApsaraMQ for RocketMQ v5.0. Half transactional message: A half transactional message is a message that cannot be sent to consumers by the ApsaraMQ for RocketMQ v5.0 broker. If an ApsaraMQ for RocketMQ v5.0 broker receives a message from a producer and does not receive the second acknowledgment (ACK) from the producer, the message is temporarily undeliverable. A message in this state is called a half transactional message. Message status check: In scenarios such as a transient disconnection occurs in the network or the producer application is restarted, the ApsaraMQ for RocketMQ v5.0 broker does not receive the second ACK for a transactional message. When the ApsaraMQ for RocketMQ v5.0 broker finds that a message remains as a half transactional message for an excessively long period of time, the broker sends a request to the producer to check whether the final status of the message is Commit or Rollback.

**Applicable scenarios**

ApsaraMQ for RocketMQ v5.0 allows you to use transactional messages in the following scenarios: The distributed transaction processing feature provided by ApsaraMQ for RocketMQ v5.0 can be used to ensure transaction consistency based on transactional messages. The distributed transaction processing feature is similar to X/Open XA. For example, an e-commerce platform provides a shopping cart system and a transaction system. When customers use the shopping cart to place orders, the customer entry point is the shopping cart system, and the entry point for order placement is the transaction system. Data in the two systems must be eventually consistent. In this case, transactional messages can be used. After an order is placed, the transaction system sends a transactional message about the order to ApsaraMQ for RocketMQ v5.0. The shopping cart system subscribes to the transactional message about the order from ApsaraMQ for RocketMQ v5.0, performs the required operations, and then updates data.

**How to use transactional messages**

Interaction process The following figure shows the process of using transactional messages in ApsaraMQ for RocketMQ v5.0. The procedure for sending a transactional message includes the following steps:
1. A producer sends a message to the ApsaraMQ for RocketMQ v5.0 broker.
2. The ApsaraMQ for RocketMQ v5.0 broker persists the message and sends an ACK to the
producer. At this stage, the message is a half transactional message. age types
3. The producer executes a local transaction.
4. The producer sends an ACK to the ApsaraMQ for RocketMQ v5.0 broker to submit the
execution result of the local transaction. In the execution result, the status of the transaction may be Commit or Rollback. If the status of the transaction is Commit, the broker marks the half transactional message as deliverable. Then, consumers can consume the message. If the status of the transaction is Rollback, the broker deletes the message. In this case, consumers cannot consume the message. The following list describes how to check the status of a transactional message:
1. If the ApsaraMQ for RocketMQ v5.0 broker does not receive an ACK from the producer
because the network is disconnected or the message producer application is restarted, the ApsaraMQ for RocketMQ v5.0 broker sends a request to query the status of the message after a specific period of time.
2. After the producer receives the request, the producer checks the final status of the local
transaction that corresponds to the message.
3. The producer sends a new ACK to the ApsaraMQ for RocketMQ v5.0 broker based on the
final status of the local transaction. The broker processes the half transactional message based on the content of the ACK. For more information, see Step 4.

**Usage notes**

Producers of transactional messages cannot be in the same group to which producers of messages of other types belong. ApsaraMQ for RocketMQ v5.0 brokers perform status check operations for transactional messages based on the IDs of the groups to which the producers belong. You must specify the implementation class of the **LocalTransactionChecker** method when you call **ONSFactory.createTransactionProducer** to create a transactional message producer. This way, the broker can check the status of transactional messages after exceptions occur. After the local transaction that corresponds to a transactional message is executed, the
**execute** method returns one of the following results:
**TransactionStatus.CommitTransaction**: The transaction is committed. The message
can be consumed by consumers.
**TransactionStatus.RollbackTransaction**: The transaction is rolled back. The message
is discarded and cannot be consumed.
**TransactionStatus.Unknow**: The transaction is in an unknown state. The ApsaraMQ for
RocketMQ v5.0 broker is expected to send a request to the producer to check the status of the transaction again after a specific period of time.

**Sample code for using TCP client SDKs**

For information about sample code, see the following references: SDK for Java: Send and subscribe to transactional messages SDK for C and C++: Send and subscribe to transactional messages SDK for .NET: Send and subscribe to transactional messages

### 3.4 Ordered messages

age types Ordered messages are consumed in the same order in which they are sent. The earliest message that is sent is consumed as the first message, and the message that is sent next is consumed later. In most cases, ordered messages are used in scenarios that require messages to be consumed in the order in which they are produced. For example, ordered messages are frequently used in financial security and e-commerce industries. This topic describes the terms, scenarios, working mechanism, and usage notes of ordered messages in ApsaraMQ for RocketMQ v5.0.

**What is an ordered message?**

**Definition**

Ordered messages are a type of messages provided by ApsaraMQ for RocketMQ v5.0. Messages of this type are published and consumed in a strict first-in, first-out (FIFO) order in a topic. The earliest published message is consumed as the first message. All messages in a specific topic of an ApsaraMQ for RocketMQ v5.0 instance are partitioned based on a sharding key. The messages in each partition are published and consumed in a FIFO order. FIFO order applies only to messages in the same partition. Messages across partitions do not need to be consumed in FIFO order. Therefore, ordered messages in ApsaraMQ for RocketMQ v5.0 are also known as partitionally ordered messages.

**Terms**

Sharding key: the key field used in ordered messages to identify partitions in a topic. This field is different from the key of a normal message. ApsaraMQ for RocketMQ v5.0 routes messages that contain the same sharding key to a partition. The earliest published message in the partition is consumed first. Partition: topic-level partitions. Each topic contains one or more partitions. Messages in a topic are distributed in partitions. Logical partitions in this topic are topic-level partitions. Physical partition: the physical unit used to store messages. Each physical partition is created on a specific node of a broker.

**Applicable scenarios**

In most cases, ordered messages are used in scenarios that require messages to be consumed in the order in which the messages are produced. For example, ordered messages are frequently used in the financial security and e-commerce industries. Examples: If a verification code is required for user registration and the user ID is used as the sharding key, the messages that are sent by the same user are published and consumed in a FIFO order. In an e-commerce scenario, if the order ID is used as the sharding key, messages for the creation, payment, refund, and logistics of the same order are published and consumed in a FIFO order.

**Working mechanism**

age types To ensure that messages are sent and consumed in a FIFO order in ApsaraMQ for RocketMQ v5.0, you must pay attention to the following phases:

**Message publishing**

In the preceding figure, messages for Orders A and B are produced in the following sequence: A1, B1, A2, A3, B2, and B3. Messages for the same order must be sent and consumed in the same sequence in which they are produced. For example, messages for Order A are sent and consumed in the following sequence: A1, A2, and A3. Normal messages for Order A may be sent to different queues in polling mode. The original order of the normal messages cannot be retained in the queues. Ordered messages that use the same sharding key such as the same order ID are sequentially routed to the same partition in ApsaraMQ for RocketMQ v5.0. An ApsaraMQ for RocketMQ v5.0 broker uses the time order in which messages are produced by the same producer to determine the message order. An ApsaraMQ for RocketMQ v5.0 broker cannot determine the order of the messages that are sent in parallel by different producers or threads.

**Message storage**

In the preceding figure, each logical partition corresponds to a physical partition. When messages are sent to the logical partitions in order, the messages are stored in the corresponding physical partitions in the same order.

**Message consumption**

ApsaraMQ for RocketMQ v5.0 delivers messages to a consumer in the order in which the messages are stored. Then, the consumers consume the messages from the earliest received message. When consumers consume messages, messages that contain the same sharding key are consumed by using a single thread. This helps ensure the consistency between the message consumption order and the message storage order, and the consistency between the message consumption order and the message publishing order.

**Message types**

| Message type | Performance | Reliable synchronous transmission | Reliable asynchronous transmission | One-way transmission |
|---|---|---|---|---|

age types

| Unordered messages, including normal messages, transactional messages, scheduled messages, and delayed messages | High | Supported | Supported | Supported |
|---|---|---|---|---|
| Ordered messages | Moderate | Supported | Not supported | Not supported |

**Usage notes**

Each group corresponds to a topic type. A group cannot be used to send or receive both ordered messages and unordered messages. Ordered messages cannot be published in broadcasting mode. Ordered messages cannot be sent in asynchronous mode. If ordered messages are sent in asynchronous mode, messages may be disordered.

**Sample code for using TCP client SDKs**

For information about the sample code for using TCP client SDKs to send and subscribe to ordered messages, see the following topics: SDK for Java: Send and subscribe to ordered messages SDK for C and C++: Send and subscribe to ordered messages SDK for .NET: Send and subscribe to ordered messages le guide

## 4 Console guide

### 4.1 Resource management

#### 4.1.1 Overview

This topic describes how to manage resources in ApsaraMQ for RocketMQ v5.0. If a new application needs to access ApsaraMQ for RocketMQ v5.0, you must create the following ApsaraMQ for RocketMQ v5.0 resources for the application:
**Instance**: An instance is a VM resource of ApsaraMQ for RocketMQ v5.0 used to store
information about topics and group IDs.
**Topic**: In ApsaraMQ for RocketMQ v5.0, a producer sends messages to a specific topic, and
a consumer subscribes to the topic to obtain and consume the messages.
**Group ID**: A group ID is used to identify a group of producers or consumers.
You can add, delete, modify, and query the preceding resources in the ApsaraMQ for RocketMQ v5.0 console or by calling API operations. You can also configure approval workflows for operations performed on the resources. This helps standardize the management process of the resources. When you use an SDK to send and subscribe to messages, you must specify the information about the topic and group that you created in the ApsaraMQ for RocketMQ v5.0 console. You must also enter the AccessKey ID and AccessKey secret that you created in the Apsara Unimanager Management Console for identity authentication. If you have not obtained the AccessKey ID and AccessKey secret, you can obtain them in the Apsara Uni-manager Management Console. Perform the following operations to obtain the AccessKey ID and AccessKey secret: In the Apsara Uni-manager Management Console, move your pointer over the profile picture and select **User *************. On the page that appears, view the AccessKey ID and AccessKey secret in the ****************** section.

#### 4.1.2 Manage instances

In ApsaraMQ for RocketMQ v5.0, an instance is used to store information about topics and group IDs. This topic describes how to create, update, view, and delete instances in the ApsaraMQ for RocketMQ v5.0 console.

**Create an instance**

1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **Instance List** page, click **Create an instance**.
4. On the **Create MQ 5.0 Instance** page, configure the parameters and click **Submit**.
The following table describes the parameters.

| Parameter | Description | Example |
|---|---|---|

le guide

| Region | Organization/R esource Set | The organization and resource set in which you want to create the instance. | root test, _ DefaultResource |
|---|---|---|---|
|   | Region | The region in which you want to create the instance. | cn-qingdao- env66-d01 |
|   | Instance Type | Single Zone: All broker nodes are deployed in the same zone. This deployment mode offers low costs but lacks disaster recovery capabilities. Dual-Zone: Broker nodes are distributed in two different zones to achieve high availability across zones and tolerate single points of failure. | Single Zone |
|   | Primary Zone | The zone with scheduling priority, which handles the primary read and write traffic. | cn-qingdao- env66-d01-**** |
|   | Secondary Zone | Note This parameter is displayed only if you set the Instance Type parameter to Dual-Zone. A backup zone that automatically takes over services when the primary zone fails. | cn-qingdao- env66-d02-**** |
|   | Chip Architecture | The chip type of the instance that you want to create. By default, the type of the chip used by the instance is the same as that of the chip deployed in the ApsaraMQ for RocketMQ v5.0 cluster. You cannot modify this parameter. | Intel |
|   | Specification | The specification of the broker. Valid values: Broker4C32G Broker8C48G Broker16C96G Broker32C186G | Broker4C32G |

le guide

|   | Broker Count | The number of brokers. Default value: 4. Note The number of brokers must be an even number. | 4 |
|---|---|---|---|
| Basic Configuration | Instance Name | The name of the instance. The name must be 3 to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores ( ). _ | test |
|   | Authentication Type | ACL Authentication: Data plane authentication is independent of the authentication service provided by Apsara Stack. This improves the stability of ApsaraMQ for RocketMQ. RAM Authentication: integrates with the RAM system of Apsara Stack to support fine-grained role authorization and temporary credentials. | RAM Authentication |
|   | Maximum Number of Topics | The maximum number of topics that can be created in the instance. If you no longer need a topic, delete the topic at the earliest opportunity. Valid values: Broker4C32G: 10~500 Broker8C48G: 10 to 1000 Broker16C96G: 10 to 1500 Broker32C186G: 10~2000 Default value: 50. | 50 |
|   | Message Publishing TPS | Valid values: 500 to 30000. Default value: 500. | 500 |
|   | Message Subscription TPS | The maximum TPS for subscribing to messages in the instance. Valid values: 1500 to 30000. Default value: 1500. | 1500 |

le guide

|   | Description | The description of the instance. The description must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), _ hyphens (-), and colons (:). It must start with a letter and cannot start with http:// or https://. | test |
|---|---|---|---|

5. **Optional.** If you configured a review workflow, perform the following additional operations:
i. In the **Process Information Supplement** dialog box, select a value for the **Execution**
**Method After Approval** parameter and specify a reason in the **Operation Reason**
field, and then click **Submit For Approval**. ii. In the **Operation Succeeded** message, click **Application Form Details** to go to the application form details page. iii. In the **Approval Progress of Application Form** section of the application form details page, click **View All** to go to the **Approval Progress of Application Form** panel to view the approval progress. The approval is complete only if all approval steps are complete.
6. In the message that appears, click **OK**. On the **Instance List** page, you can view the
created instance.

**Modify the configurations of an instance**

You can upgrade or downgrade the configurations of an ApsaraMQ for RocketMQ instance.
1. On the **Instance List** page, find the instance that you want to modify and click **Edit** in the
**Operation** column.
2. On the **MQ 5.0 Update Configuration** page, modify the parameters in the **Basic**
**Configuration** section and click **Submit**.
You can modify the settings of the following parameters: **Instance Name**, **Maximum**
**Number of Topics**, **Message Publishing TPS**, **Message Subscription TPS**, and
**Description**.
3. **Optional.** If you configured a review workflow, perform the following additional operations:
i. In the **Process Information Supplement** dialog box, select a value for the **Execution**
**Method After Approval** parameter and specify a reason in the **Operation Reason**
field, and then click **Submit For Approval**. ii. In the **Operation Succeeded** message, click **Application Form Details** to go to the application form details page. iii. In the **Approval Progress of Application Form** section of the application form details page, click **View All** to go to the **Approval Progress of Application Form** panel to view the approval progress. The approval is complete only if all approval steps are complete.

**View instance details**

On the **Instance List** page, find the instance that you want to manage and click the instance ID or **Details** in the **Operation** column. On the **Instance details** page, view the details of the instance on the following tabs: le guide
**Basic information**: displays the instance ID, maximum number of topics that can be
created, instance name, maximum transactions sent per second (TPS) for message sending, maximum TPS for message subscription, ID of the cluster to which the instance belongs, description, department to which the instance belongs, department ID, resource set to which the instance belongs, resource set ID, chip type, whether the instance has an independent namespace, and whether the instance is a disaster recovery instance.
**Network Management**: displays the endpoint of the instance. For more information, see
Network management. For information about the scenarios in which the endpoint is used, see Connect a client to an instance of this topic.
**ACL Account**: allows you to manage the access credentials of the ApsaraMQ for RocketMQ
instance in a centralized manner. For more information, see ACL account management.
**ACL Rule**: allows you to view and manage the ACL rules of the ApsaraMQ for RocketMQ
instance. For more information, see ACL rule management.
**Topic Management**: displays the basic information about all topics on the instance,
including the topic names, message types, permissions, descriptions, and operations that can be performed. For more information, see Manage topics.
**Group Management**: displays the basic information about all groups in the instance,
including the group IDs, creation time, permissions, maximum numbers of retry attempts, descriptions, and operations that can be performed. For more information, see Manage groups.
**Message Query**: allows you to query messages by message ID, message key, or topic. For
more information, see Message query.
**Message Trace**: allows you to query message traces. For more information, see Message
tracing.
**Dead Letter Queue**: allows you to query, export, and resend dead-letter messages that
are sent to a dead-letter queue. For more information, see Manage dead-letter queues.

> **Note:** Optional. In the upper-right corner of the **Instance details** page, you can click **Refresh**, **Create Topic**, **Create a Group**, or **More** to perform the related operation.
> Optional. You can also click the
> icon next to the instance name to select another
> instance from the drop-down list.

**Scale out an instance**

1. On the **Instance List** page, find the instance that you want to scale out and click
**Expansion** in the **Operation** column.
2. In the **Expansion** dialog box, modify the value of the Number of brokers parameter and
click **OK**.

> **Note:** The number of brokers must be an even number.

**Delete an instance**

> **Important:** Before you delete an ApsaraMQ for RocketMQ v5.0 instance, make sure that the following

le guide

> requirements are met:
> All resources in the instance are deleted, including topics and groups.
> No ApsaraMQ for MQTT instance is bound to the instance.

1. On the **Instance List** page, find the instance that you want to delete and click **Release** in
the **Operation** column.
2. In the message that appears, read the notes and click **Confirm order**.

**Connect a client to an instance**

When you use an ApsaraMQ for RocketMQ v5.0 SDK to connect a client to an ApsaraMQ for RocketMQ instance, you must specify the instance information in the SDK code. The instance information includes the ID and endpoint of the instance. You can view the instance ID on the **Basic Information** tab of the **Instance details** page. You can obtain the instance endpoint on the **Network Management** tab of the **Instance**
**details** page.
The following sample code shows how to configure instance information:

```
// The instance ID. Replace <InstancedId> with the ID of the instance that you created in the ApsaraMQ for RocketMQ console. properties.put(PropertyKeyConst.INSTANCE_ID, "<InstancedId>"); // The instance endpoint. Replace <Endpoint> with the endpoint of the instance that you created in the ApsaraMQ for RocketMQ console. properties.put(PropertyKeyConst.NAMESRV_ADDR, "<Endpoint>");
```

#### 4.1.3 Manage topics

A topic is a first-level identifier that classifies messages in ApsaraMQ for RocketMQ v5.0. ApsaraMQ for RocketMQ v5.0 allows you to publish and subscribe to messages by using topics. Producers send messages to topics, and consumers subscribe to topics to consume messages. This topic describes how to create, view, update, and delete, import, and export topics in the ApsaraMQ for RocketMQ v5.0 console.

**Prerequisites**

An ApsaraMQ for RocketMQ v5.0 instance is created. For more information, see Create an instance of the Manage instances topic.

**Create a topic**

1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
4. On the **Instance details** page, click the **Topic Management** tab.
5. Click **Create a Topic**.
6. In the **Create a Topic** dialog box, configure the parameters and click **OK**.

| Parameter | Description |
|---|---|

le guide

| Topic | The name of the topic. The topic name can contain only letters, digits, hyphens (-), and underscores ( ). _ The topic name must be 3 to 64 characters in length. |
|---|---|
| Message Type | The message type. Important ApsaraMQ for RocketMQ v5.0 supports the following types of messages: normal messages, partitionally ordered messages, scheduled messages, delayed messages, and transactional messages. When you create a topic, the message type that you select for the topic must be consistent with the type of messages that the topic sends. Otherwise, messages may fail to be sent. |
| Description | The description of the topic. |

**Update the description of a topic**

1. On the **Topic Management** tab, find the topic whose description you want to modify,
move the pointer over the value in the **Description** column, and then click the icon.
2. In the **Modify description** dialog box, modify the description and click **OK**.

**View topic information**

On the **Instance details** page, click the **Topic Management** tab. On this tab, view the basic information about all topics on the instance, including the names, message types, permissions, descriptions, and supported operations of the topics.

**Delete a topic**

When you create an ApsaraMQ for RocketMQ v5.0 instance, you must specify the maximum number of topics that can be created on the instance. If the number of created topics on the instance exceeds the specified threshold, you cannot create topics on the instance. If you no longer need to use a topic, we recommend that you delete the topic at the earliest opportunity.

> **Important:** After you delete a topic, the producers stop sending messages to the topic, and the consumers stop consuming messages from the topic. In addition, the metadata and messages in the topic are deleted and cannot be restored. Proceed with caution.

1. On the **Topic Management** tab, find the topic that you want to delete and click **Delete** in
the **Operation** column.
2. In the **Reminder** message, read the information and click **OK**.

**Import topics to or export topics from a single instance**

**Import topics**

le guide
1. On the **Topic Management** tab, click **Import**.
2. In the **Import Topic** dialog box, click **Upload File**. Upload a CSV file. For more information
about file templates, see the exported topic files.
3. Click **OK**.

**Export topics**

1. On the **Topic Management** tab, select the topics that you want to export and click the
icon in the upper-right corner of the topic list.

> **Note:** If you do not select topics and click the Download icon, all topics are exported by default.

2. In the **Export** dialog box, configure the **Export Data by Scope** and **Columns to Export**
parameters.

| Parameter | Description |
|---|---|
| Export Data by Scope | The scope of the data that you want to export. Valid values: All and Selected Data. |
| Columns to Export | The data columns that you want to export. By default, topic, orderType, and remark are selected. Type is optional. |

3. Click **OK**.

**Send messages**

On the **Topic Management** tab, you can send messages. For more information, see Send messages in the console.

**Subscriptions**

On the **Topic Management** tab, you can view message subscriptions. For more information, see Subscribe to messages.

#### 4.1.4 Manage groups

After you create an instance and a topic, you need to create a group ID for message consumers or producers. This topic describes how to create, view, and delete group IDs in the ApsaraMQ for RocketMQ 5.0 console.

**Prerequisites**

An ApsaraMQ for RocketMQ v5.0 instance is created. For more information, see Create an instance of the Manage instances topic.

**Background information**

le guide Producers or consumers in a group produce or consume messages of the same type based on the same logic. To use ApsaraMQ for RocketMQ 5.0 to produce or consume messages, you must create group IDs to identify producer instances or consumer instances of the same type. One consumer can subscribe to multiple topics, and one topic can be subscribed to by multiple consumers in a group. One producer can send messages to multiple topics, and one topic can receive messages from multiple producers in a group.

**Usage notes**

A group cannot be used across instances. For example, a group that is created on Instance A cannot be used on Instance B. If a consumer group ID or an existing consumer ID that was created in an earlier version of ApsaraMQ for RocketMQ was created by using the credentials of a Resource Access Management (RAM) user, the RAM user and the Apsara Stack tenant account to which the RAM user belongs can use the consumer group ID or consumer ID. If a consumer group ID or an existing consumer ID that was created in an earlier version of ApsaraMQ for RocketMQ was created by using the credentials of an Apsara Stack tenant account, only the Apsara Stack tenant account can use the consumer group ID or consumer ID. RAM users of this Apsara Stack tenant account cannot use the consumer group ID or consumer ID.

**Create a group ID**

1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
4. On the **Instance details** page, click the **Group Management** tab.
5. On the **Group Management** tab, click the **TCP protocol** tab.

> **Note:** ApsaraMQ for RocketMQ 5.0 does not support using the HTTP client SDKs to send and subscribe to messages.

6. Click **Create Group ID**. In the **Create Group ID** dialog box, configure the parameters and
click **OK**.

| Parameter | Description |
|---|---|
| Group ID | Enter a group ID. The group ID can contain only letters, digits, hyphens (-), and underscores ( ). _ The group ID must be 7 to 64 characters in length. The group ID cannot be modified after it is created. |
| Description | Enter a topic description. |

le guide

> **Note:** A group ID can be used to identify producer instances of the same type. In this case, the group ID is a producer group ID. A group ID can also be used to identify consumer instances of the same type. In this case, the group ID is a consumer group ID.

**View group IDs**

On the **Instance details** page, click the **Group Management** tab. On this tab, view the basic information about all group IDs on the instance, including the creation time, permission, description, subscription relationship, consumer status, and sample code.

**Delete a group ID**

> **Important:** After you delete a group ID, producers or consumers in the group fail authentication when they attempt to connect to the ApsaraMQ for RocketMQ instance. Producers or consumers that are already connected to the ApsaraMQ for RocketMQ instance are not affected.

1. In the group ID list, find the group ID that you want to delete, click the
icon in the
**Operation** column, and then select **Delete**.
2. In the **Confirmation information** dialog box, check the information and click **OK**.

**Import groups to or export groups from a single instance**

**Import groups**

1. On the **Group Management** tab, click **Import**.
2. In the **Import Group** dialog box, click **Upload File**. Upload a CSV file. For more
information about the file template, see the exported group files.
3. Click **OK**.

**Export groups**

1. On the **Group Management** tab, select the group IDs that you want to export and click the
icon in the upper-right corner of the group ID list.

> **Note:** If you do not select group IDs and click the Download icon, all groups are exported by default.

2. In the **Export** dialog box, configure the **Export Data by Scope** and **Columns to Export**
parameters.

| Parameter | Description |
|---|---|
| Export Data by Scope | The scope of the data that you want to export. Valid values: All and Selected Data. |

le guide

| Columns to Export | The data columns that you want to export. By default, groupId, groupType, and remark are selected. |
|---|---|

3. Click **OK**.

### 4.2 Network management

This topic describes how to use the network management feature to view the endpoint of an instance.

**Prerequisites**

An ApsaraMQ for RocketMQ v5.0 instance is created. For more information, see Create an instance of the Manage instances topic.

**View the endpoint**

1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
4. On the **Instance details** page, click the **Network Management** tab.
5. On the Network Management tab, view the information in the **TCP client access point**
section.

> **Important:** Sensitive information is included in the endpoint. Make sure that your network is protected.

### 4.3 ACL account management

This topic describes how to create, view, modify, enable, disable, and delete an access control list (ACL) account.

**Feature overview**

The ACL account management module is used to centrally manage the access credentials (usernames/passwords) of ApsaraMQ for RocketMQ instances. By creating and managing ACL accounts, you can control the read and write permissions of client applications on topics and groups to ensure the security of the messaging service.

> **Important:** After you create an account, the account cannot access resources properly. You must use the ACL Rule module to configure specific authorization policies. For example, you can allow an account to publish or subscribe to specific topics.

**Prerequisites**

An ApsaraMQ for RocketMQ v5.0 instance is created. For more information, see Create an instance of the Manage instances topic. le guide

**Create an ACL account**

1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
4. On the **Instance details** page, click the **ACL Account** tab.
5. On the **ACL Account** tab, click **Create ACL Account**.
6. In the **Create ACL Account** dialog box, configure the following parameters and click
**Create**.

| Parameter | Description |
|---|---|
| Username | The account ID. Note The username must be 1 to 64 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). _ |
| Password | The password is automatically generated by the system. You can click Copy to obtain the password and click Regenerate to generate a new password. |
| Remark | Optional. Enter the usage description of the account. |

**View an ACL account**

After an ACL account is created, you can view the account information in the ACL account list, including **Username**, **Password**, **Status**, **Remark**, **Created At**, **Updated At**, and the operations that you can perform in the **Operation** column.

**Modify an ACL account**

1. In the ACL account list, find the ACL account that you want to modify and click **Edit** in the
**Operation** column.
2. In the **Edit ACL Account** dialog box, modify the **Password** and **Remark** parameters and
click **Save**.

**Enable and disable an ACL account**

> **Note:** **Disable**: temporarily blocks all access requests from the account, but retains the account data and associated rule configurations.
> **Enable**: restores normal access for the account.

le guide
1. In the ACL account list, find the ACL account that you want to manage and click **Disable** or
**Enable** in the **Operation** column.
2. In the message that appears, click **OK**.

**Delete an ACL account**

You can permanently remove an account and all its associated ACL rule configurations by deleting the ACL account.

> **Important:** The delete operation is irreversible. Active clients using this account will be disconnected immediately. Make sure no business relies on this account before deletion.

1. In the ACL account list, find the ACL account that you want to delete and click **Delete** in the
**Operation** column.
2. In the message that appears, click **OK**.

### 4.4 ACL rule management

This topic describes how to create, view, modify, and delete an access control list (ACL) rule.

**Feature overview**

ACL rule management is the core module for access control in ApsaraMQ for RocketMQ instances. It defines "who (accounts)" can perform "what operations (publish/subscribe)" on "which resources (topics/groups)".

**Prerequisites**

An ApsaraMQ for RocketMQ v5.0 instance is created. For more information, see Create an instance. An ACL account is created. For more information, see Create an ACL account. A topic or a group is created. For more information, see Create a topic or Create a group ID.

**Create an ACL rule**

1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
4. On the **Instance details** page, click the **ACL Rule** tab.
5. On the **ACL Rule** tab, click **Create ACL Rule**.
6. In the **Create ACL Rule** dialog box, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Username | Select the ACL account to be authorized. |

le guide

| Resource Type | Select the type of resource to which access control applies. TOPIC: message topics (for sending or subscribing to messages). GROUP: consumer groups (for consumers in a group to consume messages). |
|---|---|
| Resource Name | Select a topic or group ID. |
| Action | The operations that can be performed. PUB (Publish): allows publishing (sending messages) only. SUB (Subscribe): allows subscribing (receiving messages) only. PUB SUB (Publish + Subscribe): allows _ both publishing and subscribing (read and write permissions). |
| Decision | Allow: grants permissions. Deny: explicitly denies permissions (highest priority). |

**View an ACL rule**

After an ACL rule is created, you can view the rule information in the ACL rule list, including
**Rule ID**, **Username**, **Resource Type**, **Resource Name**, **Action**, **Decision**, **Created At**,
**Updated At**, and the operations that can be performed in the **Operation** column.

**Modify an ACL rule**

1. In the ACL rule list, find the ACL rule that you want to modify and click **Edit** in the
**Operation** column.
2. In the **Edit ACL Rule** dialog box, modify the **Username**, **Action**, and **Decision**
parameters, and then click **OK**.

**Delete an ACL rule**

> **Important:** After you delete an **Allow** rule, the account immediately loses access to the corresponding resources. After you delete a **Deny** rule, the account may regain access if no other Deny rules are in effect.

1. In the ACL rule list, find the ACL rule that you want to delete and click **Delete** in the
**Operation** column.
2. In the message that appears, click **OK**.

### 4.5 Message query

#### 4.5.1 Overview

le guide If you encounter a message consumption issue, you can query the content of a specific message for troubleshooting. ApsaraMQ for RocketMQ 5.0 allows you to query messages by message ID, by message key, and by topic. Table 1. Comparison of query methods

| Query method | Query condition | Query type | Description |
|---|---|---|---|
| By message ID | Topic+Messag e ID | Exact match | You can specify a topic and a message ID to find the exactly matched message and obtain the corresponding attributes. |
| By message key | Topic+Messag e Key | Fuzzy match | You can specify a topic and a message key to query the latest 64 messages that contain the specified message key. We recommend that you specify a unique key for each message in producers whenever possible to ensure that the number of messages with the same key does not exceed 64. Otherwise, some messages cannot be queried. |
| By topic | Topic + Time range | Range match | You can specify a topic and a time range to obtain all messages that meet the conditions. This type of query returns a large number of messages, which makes it difficult to locate the message that you want to query. |

We recommend that you choose a query method based on the following process. Figure 1. Message query process

#### 4.5.2 Query messages

This topic describes how to query messages in the ApsaraMQ for RocketMQ 5.0 console by using three different methods. le guide

**Procedure**

1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
4. On the **Instance details** page, click the **Message Query** tab.
5. On the **Message Query** tab, click a sub-tab, enter the required information, and then click
**Query**.

**Query by message ID**

When you query messages by message ID, an exact match is used. You can specify the topic and ID of a message to query the message. We recommend that you print the message ID to the log when a message is sent. This facilitates troubleshooting. In the following sample code, ApsaraMQ for RocketMQ 5.0 SDK for Java is used to obtain a message ID:

```
SendResult sendResult = producer.send(msg); String msgId = sendResult.getMessageId();
```

To obtain the sample code for other programming languages, go to the **Group**
**Management** tab, find the group ID, and then click **Sample code** in the Operation
column.

**Query by message key**

ApsaraMQ for RocketMQ 5.0 creates an index for messages based on the message keys that you specify. When you enter a topic name and a message key to query messages, ApsaraMQ for RocketMQ 5.0 returns the matched messages based on the index.

> **Important:** If you query messages by message key, take note of the following items:
> The query condition is the specified message key.
> Only the latest 64 messages that contain the specified key are returned. Therefore, we recommend that you set the key for each message to a unique and business-specific value.

The following sample code provides an example on how to specify a message key:

```
Message msg = new Message("Topic","*","Hello MQ".getBytes()); /**
* Specify a key that is used for message queries for each message. The key is the p
rimary business attribute of a message. We recommend that you specify a globally un ique key for each message.
* A unique key helps you query a message in the ApsaraMQ for RocketMQ 5.0 console i
f the message fails to be received. A message can be sent and received even if you do not specify the message key.
```

`*/`

```
msg.setKey("TestKey"+System.currentTimeMillis());
```

**Query by topic**

If you cannot query messages by message ID or message key, query messages by topic. You can specify a topic and time range for message sending, retrieve messages in batches, and then find the data that you need. le guide

> **Important:** If you query messages by topic, take note of the following items:
> This query method allows you to obtain all messages that are sent in a topic during a specific time range. We recommend that you narrow down the time range to locate the message that you want to query in an efficient manner.
> If you query messages by topic, a large number of messages are returned on multiple pages.

#### 4.5.3 Message query results

This topic describes the results of message queries. You can view the message query results on the **Message Query** tab in the ApsaraMQ for RocketMQ 5.0 console. The query result includes the **message ID**, **tag**, **key**, and **storage time**. In addition, you can download the message content, query message traces, and view message details by clicking buttons in the **Operation** column.

**Message details**

**Delivery status**

The **delivery status** in the **Message details** panel is calculated by ApsaraMQ for RocketMQ 5.0 based on the consumption progress of each group ID. For more information about the delivery status, see the Message delivery states table of this topic.

> **Note:** The **delivery status** is calculated based on the consumption progress. To query the consumption details, view the **message trace**. The message trace displays the complete path of the message. For more information, see Query message traces.

Table 1. Message delivery states

| Delivery status | Possible cause |
|---|---|
| The message has been subscribed to and consumed at least once. | A consumer identified by the group ID has consumed the message as expected. |

le guide

| The message has been subscribed to but is filtered out by the filter expression. Check the tag of the message. | The tag of the message does not comply with the subscription of the consumer, and the message is filtered out. To query the subscription of the consumer, log in to the ApsaraMQ for RocketMQ 5.0 console, go to the Group Management tab on the Instance details page, find the group ID of the consumer whose subscription you want to view, and then click Consumer status in the Operation column. |
|---|---|
| The message has been subscribed to but is not consumed. | A consumer identified by the group ID has subscribed to the message, but the message has not been consumed possibly because the consumption is slow or is blocked due to an exception. |
| The message has been subscribed to, but the consumer that subscribes to the message and is identified by the group ID is not online. Use the message trace feature to query the details about the message through an exact match. | A consumer identified by the group ID has subscribed to the message, but the consumer is not online. Check the reason why the consumer is not online. |
| An unknown exception occurred. | An unknown exception occurred. Contact technical support for troubleshooting. |

**Verify message consumption**

In the **Message details** panel, ApsaraMQ for RocketMQ 5.0 supports the **consumption**
**verification** feature. You can push a specified message to a specified online consumer to
check whether the consumer can consume the message based on the correct logic as expected.

> **Important:** The consumption verification feature can be used only to verify whether consumers can consume messages based on the correct logic as expected. This feature does not affect the normal process of receiving messages. Therefore, information such as the consumption status of a message does not change after the consumption is verified.

### 4.6 Message traces

#### 4.6.1 Overview

le guide A message trace is the complete trace of a message that is sent from a producer to the ApsaraMQ for RocketMQ 5.0 broker and then consumed by a consumer. The message trace includes the time, status, and other information on each node in the preceding process. The message trace can be used to help troubleshoot issues in production environments. This topic describes the scenarios in which the message trace feature can be used. This topic also describes how to query a message trace and the parameters that are returned in query results.

**Message trace data**

In ApsaraMQ for RocketMQ 5.0, the complete trace of a message involves three roles: producer, broker, and consumer. Each role adds relevant information to the trace when the role processes the message. The information is aggregated to indicate the status of the message. The following figure shows the relevant data. Figure 1. Message trace data

**Scenarios**

You can use the message trace feature to help troubleshoot issues if a message is not sent or received as expected in your production environment. You can query the message trace by message ID, message key, or topic to check whether the message is sent and received as expected within the specified time range.

**Usage notes**

le guide No extra fees are incurred when you use the message trace feature. After a message is sent, you can query the trace of the message based on the message ID, message key, or topic in the ApsaraMQ for RocketMQ 5.0 console. You must take note of the following points. Table 1. Rules for querying message traces

| Message type | Description |
|---|---|
| Normal message | A sending trace is generated after the message is sent. If the message is not consumed, Not Consumed is displayed. After the message is consumed, the sending information and consumption information are displayed. |
| Ordered message | A sending trace is generated after the message is sent. If the message is not consumed, Not Consumed is displayed. After the message is consumed, the sending information and consumption information are displayed. |
| Scheduled message and delayed message | If the current system time is earlier than the specified point in time for consumption, the trace of the message can be queried, but the message cannot be queried. |
| Transactional message | Before the local transaction for a message is committed, the trace of the message can be queried, but the message cannot be queried. |

**Usage example**

In this example, a message is not received as expected, and you identify the issue based on the business log. To use the message trace feature to troubleshoot this issue, perform the following steps:
1. Collect the information about the message, including the message ID, message key, topic,
and approximate sending time.
2. Log in to the ApsaraMQ for RocketMQ 5.0 console, and create a query task to query the
message trace based on the collected information.
3. Check the query results and analyze the cause.
If **Not Consumed** is displayed in the trace, you can go to the **Group Management** tab to view consumer status and determine whether the issue is caused by message accumulation. If the message is consumed, check the consumption information to find the corresponding consumer client and the time when the message was consumed. Then, log in to the consumer client to view the relevant logs.

#### 4.6.2 Query message traces

You are not charged when you use the message trace feature of ApsaraMQ for RocketMQ v5.0. Before you use the message trace feature, make sure that it is supported by the version of the SDK that you use. After you send and receive messages, you can query the messages in the ApsaraMQ for RocketMQ v5.0 console.

**Prerequisites**

le guide The message trace feature is supported by the SDK version that you use. The following versions of SDKs support the message trace feature:

**TCP**

SDK for Java: V1.2.7 and later SDK for C and C++: V1.1.2 and later SDK for .NET: V1.1.2 and later

**Procedure**

1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
4. On the **Instance details** page, click the **Message Trace** tab.
5. Click **Create a query task**.
6. In the **Create a query task** dialog box, configure query conditions based on your business
requirements. Then, click **OK**.

> **Important:** Set the **Time range** as accurately as possible to narrow down the query scope and speed up the query.

You can use one of the following methods and configure the required parameters to query the trace of a message.

| Query method | Required parameter | Description |
|---|---|---|
| Query by Message ID | When you query a message trace by using this method, you must specify the unique ID of the message, the topic to which the message belongs, and the time range in which the message was sent. | We recommend that you use this method because this method is an exact match method and can query the trace of a message in an efficient manner. |
| Query by Message Key | When you query a message trace by using this method, you must specify the message key, the topic to which the message belongs, and the time range in which the message was sent. | This method is a fuzzy match method. Up to 1,000 traces can be returned for a query based on the specified message key. This method is ideal if you know the key of the message that you want to query but you do not know the ID of the message. |

le guide

| Query by Topic | You need to only enter the topic and time range in which the messages were sent. This method allows you to query multiple message traces. | This method uses a range query. It is ideal if you do not know the message ID or message key and the message volume is small. We recommend that you do not use this query method. In most cases, a large number of messages are produced in a topic within a specific time range. If you use this method, you can hardly identify a specific message among the queried messages. |
|---|---|---|

After you create a query task, you can view the information about the query task on the
**Message Trace** tab. If the value in the **Task Status** column is **Querying**, the query is not
complete.
7. In the upper-right corner of the query task list, you can click the Refresh icon to refresh the
tab. After the value in the Task Status column changes to **Query completed**, you can view the information about the trace of the message. You can click **Details** in the **Operation** column to view the information about the trace of the message, including the attributes and consumption status of the message. If no message trace information is displayed, check whether the information that you specified when you created the query task is correct. If trace information is returned, you can view the brief information about the trace, such as the message ID, tag, message key, sending status, sending time, and consumption status.
8. Click **View Track** to view details of the message trace.
A message trace consists of three parts: Information about the message producer Information about the topic to which the message belongs Information about the message consumer If you perform a query based on a message key or a topic, multiple traces may be displayed. You can scroll the page to view and compare information about traces of different messages. For information about message traces, see States in message traces.

#### 4.6.3 States in message traces

This topic describes the terms and status information displayed on the Message Trace tab. Table 1. Terms

| Object | Field | Description |
|---|---|---|
|   | Sender | The IP address of the sender. |

| ocketMQ v5.0 User Guide·Conso e guide |   |   |
|---|---|---|
| Producer |   |   |
|   | Sending time | The time when the message was sent from the producer. The time follows the ISO 8601 standard in the yyyy-MM- ddThh:mm:ssZ format. |
|   | Sending time | The period of time that the producer took to send a message by calling the Send method. Unit: milliseconds. |
|   | Status | The status of the message. |
| Topic | Topic | The topic name. |
|   | Key | The AccessKey ID of the Apsara Stack account. |
|   | Tag | A message tag is similar to a Gmail tag. It is used to sort messages and help the consumer filter messages on the ApsaraMQ for RocketMQ v5.0 broker based on specified conditions. |
|   | Region | The region where the message is stored or the region where the consumer is located. |
| Consumer | First time | The consumption status. |
|   | IP | The IP address of the consumer. |
|   | Time consuming | The period of time that the consumer took to execute the consumeMessage method after the message is pushed to the consumer. |
|   | Delivery time | The time when the consumer executed the consumeMessage method to start consuming the message. The time follows the ISO 8601 standard in the yyyy- MM-ddThh:mm:ssZ format. |

Table 2. States in message traces le guide

| Sent/Consumption status | Field | Description |
|---|---|---|
| Sending status | Sent successfully | The message is sent and stored on the ApsaraMQ for RocketMQ v5.0 broker. |
|   | Send failed | The message fails to be sent and is not stored on the ApsaraMQ for RocketMQ v5.0 broker. In this case, the broker tries to redeliver the message. |
|   | Message Timing | The message is a scheduled or delayed message, and it is not the time to deliver the message. |
|   | Transaction not committed | The message is a transactional message and has not been committed. |
|   | Transaction rollback | The message is a transactional message and has been rolled back. |
| Consumption status | All successful | The message has been consumed by all the consumers to which it is delivered. |
|   | Partial success | The message fails to be consumed in specific deliveries, or the message is consumed after it is redelivered. |
|   | All failed | The message still fails to be consumed after all delivery retries. |
|   | Not consumed yet | The message is not delivered to consumers. |
|   | Consumption result not returned | No results are returned for the message consumption method, or the method is interrupted. Therefore, the consumption status is not returned to the ApsaraMQ for RocketMQ v5.0 broker. |

le guide

|   | Consumption success | The message has been consumed. |
|---|---|---|
|   | Consumption failure | A failure result is returned for the message consumption method, or the method throws an exception. |

### 4.7 View consumer status

You can check the consumer status in the ApsaraMQ for RocketMQ v5.0 console to troubleshoot issues that occur during message consumption. This feature allows you to view the information about a group or a consumer identified by the group ID. The information includes the connection status, subscription, number of transactions per second (TPS) for message consumption, number of accumulated messages, and thread stacks. This topic describes how to view such information.

**Background information**

The cause of an exception that occurs during message consumption is complicated. In most cases, the consumer status information in the console is insufficient to troubleshoot an issue. You must perform further troubleshooting by analyzing logs and business scenarios.

**Use scenarios**

You can query the consumer status for troubleshooting in the following scenarios: Symptom: In the **Consumer status** panel, the value of the **Whether the subscription**
**relationship is consistent** parameter is **No**.
Solution: For more information about how to handle subscription inconsistency, see Subscription inconsistency. Message accumulation alert Symptom: In the **Consumer status** panel, the value in the **Accumulation** column is large. Solution: For more information about how to handle message accumulation alerts, see

**View the information about a group**

1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
4. On the **Instance details** page, click the **Group Management** tab.
5. Find the group that you want to manage and click **Consumer status** in the **Operation**
column. The following table describes the parameters in the **Consumer status** panel. Table 1. Fields and descriptions le guide

| Field | Description |
|---|---|
| Group ID | The group ID. |
| Consumption Pattern | The consumption pattern. |
| Whether the subscription relationship is consistent | Indicates whether the subscriptions of all consumer instances in the group are consistent. For more information about subscription consistency, see Subscription consistency. |
| Real-time consumption speed | The total TPS at which messages are received by the consumer instances in the group. Unit: messages/second. |
| Real-time message accumulation | The total number of messages that are not consumed by the consumer instances in the group. |
| Recent consumption time | The time when the consumer instances in the group last consumed a message. |
| Message latency | The difference between the production time of the earliest unconsumed message in the group and the current time. |
| Online or not | If one consumer instance in the group is online, the value of this parameter is Yes. In this case, you can view information about all online consumer instances in the Connection information section. If none of the consumer instances in the group ID is online, the value of this parameter is No and no information is displayed in the Connection information section. |

**View information about a single consumer instance in a group**

1. If a group is **online**, you can view information about each online consumer instance in the
group in the **Connection information** section of the **Consumer status** panel. The information includes the client ID, host or public IP address, process ID, and number of accumulated messages.
2. If you want to view more information about a specific consumer instance, click **Detailed**
**information** in the **Operation** column. The information includes the number of consumer
threads, consumption start time, subscription, and message consumption statistics.
3. If you want to view the stack information about the current process for a specific consumer
instance, find the consumer instance and click **Stack information** in the **Operation** column. le guide

### 4.8 Reset consumer offsets

You can reset consumer offsets to skip the accumulated or undesired messages instead of consuming them. You can also consume messages that are sent after a point in time regardless of whether the messages sent after this point in time are consumed.

**Background information**

When you reset consumer offsets, take note of the following items: You cannot reset consumer offsets in broadcasting consumption mode. You cannot reset consumer offsets by message ID, message key, or tag.

**Procedure**

1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
4. On the **Instance details** page, click the **Group Management** tab.
5. Find the group whose consumer offset you want to reset, click the
icon in the **Operation** column, and then select **Reset consumption point**.
6. In the **Reset consumption point** dialog box, select the corresponding topic from the
**Topic** drop-down list, and configure the **Reset type** parameter based on your business
requirements. Valid values:
**Clear all stacked messages and start consumption from the latest point** : If you
select this option, consumers identified by the group ID skip all accumulated (unconsumed) messages within the topic and restart consumption from the latest offset. If the "reconsumeLater" error message is returned, the messages in the delivery retry process cannot be skipped.
**Reset consumption points by time**: If you select this option, a time picker appears.
Select a point in time. Only the messages that are sent after the selected point in time are consumed. The time period during which you can select a point in time ranges from the production time of the earliest message stored in the topic to the production time of the latest message stored in the topic. You can select a point in time only within the allowed time range.
7. Click **OK** to reset the consumer offset.

### 4.9 Manage dead-letter queues

Dead-letter queues are used to process messages that cannot be consumed as expected. This topic describes how to query, export, and resend dead-letter messages in dead-letter queues. This helps you manage dead-letter messages based on your business requirements and prevent missing message processing.

**Background information**

le guide When a message fails to be consumed for the first time, ApsaraMQ for RocketMQ v5.0 automatically retries the consumption of the message. If the message still cannot be consumed after the maximum number of retries is reached, the message cannot be properly consumed. In this case, instead of immediately discarding the message, ApsaraMQ for RocketMQ v5.0 sends it to a particular queue of the corresponding consumer. In ApsaraMQ for RocketMQ v5.0, messages that cannot be consumed as expected are known as dead-letter messages. Queues that are used to store dead-letter messages are known as dead-letter queues.

**Dead-letter characteristics**

Dead-letter messages have the following features: Dead-letter messages can no longer be consumed as expected by consumers. Dead-letter messages have a validity period of seven days, which is the same as that of normal messages. After the validity period expires, dead-letter messages are automatically deleted. We recommend that you handle dead-letter messages within seven days after they are generated. Dead-letter queues have the following features: A dead-letter queue corresponds to a group ID instead of a consumer instance. If no dead-letter messages are generated in a consumer group, ApsaraMQ for RocketMQ v5.0 does not create a dead-letter queue for the consumer group. A dead-letter queue contains all the dead-letter messages of the corresponding group ID regardless of the message topic. You can query, export, and resend dead-letter messages in the ApsaraMQ for RocketMQ v5.0 console.

**Query dead-letter messages**

The following table describes the methods that you can use to query dead-letter messages in ApsaraMQ for RocketMQ v5.0.

| Query method | Query condition | Query type | Description |
|---|---|---|---|
| Query by Group ID | Group ID and time range | Range match | You can specify a group ID and a time range to query all messages that meet the specified conditions. This type of query returns a large number of messages. As a result, finding a specific message can be time- consuming. |
| Query by Message ID | Group ID+Message ID | Exact match | You can specify a group ID and a message ID to query a message by using exact match. |

**Query by group ID**

le guide You can batch query all the dead-letter messages of a group ID within a time range by specifying the group ID and time range.

> **Important:** The production time of a dead-letter message refers to the time when a message is sent to the dead-letter queue after the maximum number of redelivery retries for this message is reached.

1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
4. On the **Instance details** page, click the **Dead Letter Queue** tab.
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
1. Log in to the RocketMQ v5.0 console.
2. In the left-side navigation pane, click **instance list**.
3. On the **instance list** page, find the target instance by name, and then click its instance ID
or **details** in the **actions** column to open the **instance details** page.
4. On the **Instance details** page, click the **Dead Letter Queue** tab.
5. Click the **Query by Message ID** tab.
6. Select the ID of the group whose dead-letter messages you want to view from the **GroupId**
drop-down list.
7. Specify the ID of the message that you want to query in the **Message ID** field.
8. Click **Query**. All dead-letter messages that meet the preceding conditions are displayed.
9. Find the dead-letter message that you want to view and click **View Details** in the
**Operation** column to view the details about the message. The details include the basic
attributes, **message body size**, and **delivery status**.

**Export dead-letter messages**

If you cannot process dead-letter messages for the moment, you can export the messages in the ApsaraMQ for RocketMQ v5.0 console to prevent them from being deleted after expiration. You can export a single dead-letter message or multiple dead-letter messages at a time in the ApsaraMQ for RocketMQ v5.0 console. The exported file is in the CSV format. The following table describes the fields of an exported message. le guide

| Field | Description |
|---|---|
| instanceId | The instance ID. |
| topic | The message topic. |
| msgId | The message ID. |
| bornHost | The URL of the producer that produced the message. |
| bornTimestamp | The time when the message was produced. |
| storeTimestamp | The time when the message turned into a dead- letter message. |
| reconsumeTimes | The number of consumption failures. |
| properties | The message attributes in the JSON format. |
| body | The Base64-encoded message body. |
| bodyCRC | The message body Cyclic Redundancy Check (CRC). |

Export a single dead-letter message In the ApsaraMQ for RocketMQ v5.0 console, find the dead-letter message that you want to export and click **Export** in the **Operation** column to export the dead-letter message. Export multiple dead-letter messages at a time In the ApsaraMQ for RocketMQ v5.0 console, search for the dead-letter messages that you want to export by group ID, select the dead-letter messages, and then click **Batch export** below the message list to export the dead-letter messages.

**Resend dead-letter messages**

If a message enters a dead-letter queue, the message cannot be consumed as expected for specific reasons. Therefore, you must process the message in a special way. After you troubleshoot the issues, you can resend the dead-letter messages for consumption in the ApsaraMQ for RocketMQ v5.0 console.

> **Important:** After a dead-letter message is resent to the consumer, the message will still be stored in the dead-letter queue for three days. The system automatically deletes the message after the three days.

le guide Resend a single dead-letter message In the ApsaraMQ for RocketMQ v5.0 console, find the dead-letter message that you want to resend and click **Resend** in the **Operation** column to resend the dead-letter message. Resend multiple dead-letter messages at a time In the ApsaraMQ for RocketMQ v5.0 console, search for the dead-letter messages that you want to resend by group ID, select the dead-letter messages, and then click **Batch resend** below the message list to resend the dead-letter messages.

### 4.10 Message routing

#### 4.10.1 Replicator

The replicator message routing feature provided by ApsaraMQ for RocketMQ 5.0 allows you to synchronize messages between clusters. This topic describes how to create a replicator message routing task.

**Background information**

The replicator message routing feature of ApsaraMQ for RocketMQ 5.0 is used to synchronize message data between clusters. You can configure routing rules to dynamically plan the synchronization path of messages. This way, the messages can be synchronized from the source node to the destination node based on filter conditions. This feature implements remote message synchronization across clusters within milliseconds and ensures data consistency and integrity across clusters. The following figure shows how replicator message routing works in ApsaraMQ for RocketMQ 5.0. In the figure, one-way synchronization is performed based on topics to synchronize messages from a specific source topic in the source instance to a specific destination topic in the destination instance. For more information, see Message routing.

**Usage notes**

Only instances that have a namespace support the message routing feature. The message routing feature does not support chain routing. For example, you cannot create a task to route messages from Cluster A to Cluster B and then from Cluster B to Cluster C. You must create a task to route messages from Cluster A to Cluster C. The message type of the source topic must be the same as that of the destination topic. For example, if the message type of the source topic is normal message, the message type of the destination topic must also be normal message. le guide A message routing task must be created in the production environment in which the destination cluster is deployed. If you want to route messages from Cluster A to Cluster B, you must create a message routing task in the cloud environment of Cluster B. When you create a message routing task, specify Cluster A as the source cluster and Cluster B as the destination cluster. Message routing consumes the CPU and memory resources of the source and destination clusters, and the storage resources of the destination cluster. You must evaluate the amount of resources that are required before you create a message routing task.

**Prerequisites**

An ApsaraMQ for RocketMQ 5.0 instance is created. For more information, see the Create an instance section in Manage instances. A topic is created in the ApsaraMQ for RocketMQ 5.0 instance. For more information, see the Create a topic section in Manage topics. A Connect instance is created. For more information, see the Create a Connect instance section in Connect instance.

**Procedure**

To create a replicator message routing task, perform the following steps:

**Step 1: Create a message synchronization cloud**

Before you create a message routing task, you must specify the information about the cloud on which your ApsaraMQ for RocketMQ 5.0 cluster is deployed. The information includes the endpoint of the ApsaraMQ for RocketMQ 5.0 instance, the domain name, and the AccessKey ID and AccessKey secret of the Apsara Stack tenant account to which the cloud belongs. ApsaraMQ for RocketMQ 5.0 obtains the permissions that are required to access ApsaraMQ for RocketMQ 5.0 resources across clouds based on the cloud information that you specified.

**Step 2: Create a message routing task**

Specify the message source and the message destination, and configure relevant information. For example, specify filter conditions and set the start offset of message synchronization.

**Step 1: Create a message synchronization cloud**

1. Log in to the ApsaraMQ for RocketMQ 5.0 console.
2. In the left-side navigation pane, choose **Message Routing > Replicator**.
3. On the **Replicator** page, click the **Cloud information** tab. On this tab, click **Create a**
**message synchronization cloud**.
4. In the **Create a message synchronization cloud** dialog box, configure the parameters
that are described in the following table and click **OK**.

> **Note:** Message routing task creation occupies the resources that are used to produce and consume messages in the message cluster. Carefully evaluate whether to perform the scale-out.

| Parameter | Description | Example value |
|---|---|---|

le guide

| Cloud name | The name of the cloud from or to which you want to route messages. Note The combination of the cloud name and endpoint of the ApsaraMQ for RocketMQ instance uniquely identifies a message synchronization cloud. The combination must be unique. The cloud name can contain only letters, digits, hyphen (-), and underscores ( ). _ The cloud name must be 3 to 64 characters in length. | Center |
|---|---|---|
| AccessKey | The AccessKey ID of the account that is used to log in to the cloud. Make sure that the role of the account is the administrator of ApsaraMQ for RocketMQ 5.0 or a user that is granted the permissions to write data to and read data from instances and topics. For more information about how to obtain the AccessKey ID, see Obtain an AccessKey pair in ApsaraMQ for RocketMQ Developer Guide. | j8geROUEAW1k**** |
| Region | The region in which the ApsaraMQ for RocketMQ cluster is deployed. The region is displayed in the top navigation bar of the ApsaraMQ for RocketMQ 5.0 console. | cn-qingdao-****-d01 |

le guide

| Secret | The AccessKey secret of the account that is used to log in to the cloud. For more information about how to obtain the AccessKey secret, see Obtain an AccessKey pair in ApsaraMQ for RocketMQ Developer Guide. | AMx4ainrLWhT8jYUPHkdI4zY7t **** |
|---|---|---|
| MQ instance endpoint | The endpoint of the ApsaraMQ for RocketMQ 5.0 instance. For more information about how to obtain the endpoint of an ApsaraMQ for RocketMQ 5.0 instance, see the References section of this topic. | http://mq.server.****.com:808 0/rocketmq/nsaddr4client- internal |
| MQ API | The URL of the ApsaraMQ for RocketMQ 5.0 console. The value of this parameter must be in the following format: http: {console.domain}/json . For more information about how to obtain the value of {console.domain}, see the References section of this topic. | http:mq.console.****.com/json |
| Remarks | The description of the cloud. You can specify a description that can help you identify the cloud. | Central node |

|   |   | http: |   |
|---|---|---|---|
|   | {console.domain}/json |   |   |

**Step 2: Create a message routing task**

1. On the **Replicator** page, click the **Task** tab. On this tab, click **Create a task**.
2. In the **Create a task** dialog box, configure the parameters that are described in the
following table and click **OK**.

| Parameter | Description |
|---|---|

le guide

| Message Source | Message synchronization cloud: the name of the source cloud from which you want to route messages. Source region: the region in which the source ApsaraMQ for RocketMQ 5.0 cluster is deployed. After you configure the Message synchronization cloud parameter, the system automatically displays the region in which the source cloud is deployed. You do not need to specify a value for this parameter. Source instance: the instance to which the source topic belongs. Source Topic: the name of the topic from which you want to route messages. |
|---|---|
| Message destination | Message synchronization cloud: the name of the destination cloud to which you want to route messages. Target region: the region in which the destination ApsaraMQ for RocketMQ 5.0 cluster is deployed. After you configure the Message synchronization cloud parameter, the system automatically displays the region in which the destination cloud is deployed. You do not need to specify a value for this parameter. Target instance: the instance to which the destination topic belongs. Target Topic: the name of the topic to which you want to route messages. Target Connect Instance: the Connect instance that is used to execute the synchronization task. |
| Initial synchronization point | The consumer offset from which you want to route messages from the source topic to the destination topic. Default value: Maximum site. If this parameter is set to Maximum site, the message routing task routes messages to the destination topic starting from the most recent message in the source topic after the task is started. Important If this parameter is set to Maximum site, the messages that are sent to the source topic before the message routing task is started for the first time are not routed to the destination topic. |

le guide

| Filter rules | If no filter rules are specified, the message routing task routes all messages from the source topic to the destination topic. If filter rules are specified, the message routing task routes the messages that match the specified rules from the source topic to the destination topic. You can specify tags as filter rules. For example, if you want to synchronize messages whose tag is CartService to the destination, enter CartService in this field. If you want to specify multiple tags, separate multiple values with double vertical bars (\|\|). Example: CartService\|\|Inventory\|\|Payment . For more information, see Message filtering. |
|---|---|
| Description | The description of the message routing task, which helps you identify the task. |

**Modify cloud information**

1. On the **Replicator** page, click the **Cloud information** tab.
2. On the Cloud information tab, find the cloud that you want to modify, move the pointer over
the value in the **Remarks** column, and then click the icon.
3. In the **Modify description** dialog box, modify the description and click **OK**.
4. In the dialog box that appears, check the information and click **OK**.

**Delete a cloud**

1. On the **Replicator** page, click the **Cloud information** tab.
2. On the Cloud Information tab, find the cloud that you want to delete and click **Delete** in the
**Operation** column.
3. In the dialog box that appears, check the information and click **OK**.

**Start or stop a message routing task**

1. On the **Replicator** page, click the **Task** tab.
2. On the Task tab, find the message routing task that you want to manage and click **Start** or
**Stop** in the **Operation** column to start or stop the task.

**Modify a message routing task**

> **Important:** After you modify the **filter rules** of a task, you must stop the task and then restart the task to make the modification take effect.

1. On the **Replicator** page, click the **Task** tab.
le guide
2. On the Task tab, find the message routing task that you want to modify and click **Modify** in
the **Operation** column.
3. In the **Edit task** dialog box, modify the configurations of the task and click **OK**.

**View the details of a message routing task**

1. On the **Replicator** page, click the **Task** tab.
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
|   | Filter rules | The filter rules. |
|   | Message synchronization TPS | The TPS value that is collected at an interval of 1 minute. The TPS value indicates the number of messages that are routed from the source topic to the destination topic per second. |

| baba Cloud Message Queue |   |   |
|---|---|---|
| Message details |   |   |
|   | Message latency | The time difference between the consumer offset of the most recent message that was routed and the consumer offset of the latest message. |
|   | Message accumulation | The number of messages that are not routed to the destination topic. |

**Delete a message routing task**

> **Important:** After a message routing task is deleted, the task stops running.

1. On the **Replicator** page, click the **Task** tab.
2. On the Task tab, find the message routing task that you want to delete and click **Delete** in
the **Operation** column.
3. In the dialog box that appears, check the information and click **OK**.

**References**

**Obtain the endpoint of an ApsaraMQ for RocketMQ instance and the URL of the**

**ApsaraMQ for RocketMQ console**

Before you create a message synchronization cloud for message routing, you must perform the following steps to obtain the values of the **MQ instance endpoint** and **MQ API** parameters.
1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Apsara Infrastructure**
**Management** > **O&M Tools**.
3. In the left-side navigation pane, choose **O&M Tools** > **Service Registration Variable**
**Dashboard**.
4. On the **Service Registration Variable Dashboard** page, click **Advanced Filter**.
5. Enter `mq` in the **Service** field and click **Search**.
6. Obtain the value of the **MQ instance endpoint** parameter.
icon in the **Service Registration** column. i. Find the `mq-cai` service and click the ii. Click the text in the **Service Registration** column of the `mq-cai` service. In the
**Registration Variables** dialog box, view the value of the **client.onsAddr** parameter.
The value of this parameter is used as the value of the **MQ instance endpoint** parameter.
7. Obtain the value of the **MQ API** parameter.
icon in the **Service Registration** i. Find the `mq-console` service and click the column. ii. Click the text in the **Service Registration** column of the `mq-console` service. In the
**Registration Variables** dialog box, view the value of the **console.domain** parameter.
The value of the **MQ API** parameter is in the following format: http://{console.domain}/json. le guide

#### 4.10.2 Connect instance

This topic describes how to manage Connect instances throughout the lifecycle in the ApsaraMQ for RocketMQ 5.0 console, with the focus on creating an instance and deleting an instance. The standardized operation processes ensure that data synchronization tasks can be executed stably and efficiently.

**Background information**

Concepts in the distributed messaging architecture:
**ApsaraMQ for RocketMQ instance**: Store and distribute messages.
**Connect instance**: Run specific data transmission logic (worker) and serve as the "bridge"
between the source and the destination.
**Dependency**: All data synchronization tasks must be bound to a running Connect instance
before execution.

**Prerequisites**

An ApsaraMQ for RocketMQ 5.0 instance is created. For more information, see the Create an instance section in Manage instances.

**Create a Connect instance**

1. Log in to the ApsaraMQ for RocketMQ 5.0 console.
2. In the left-side navigation pane, choose **Message Routing > Connect Instance**.
3. On the **Connect Instance** page, click **Create Connect**.
4. In the **Create Connect** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Connect Name | The name of the Connect instance. It must be 3 to 64 characters in length. |
| MQ Instance | Select the ApsaraMQ for RocketMQ 5.0 instance associated with the Connect instance. |
| Replicas | Set the number of Connect instance workers, which determines the concurrent processing and disaster recovery performance. The number of replicas ranges from 1 to 10. |

**Delete a Connect instance**

This operation is used to release instance resources that are no longer in use.

> **Important:** Data interruption: If you delete a Connect instance, all synchronization tasks bound to the instance stop immediately, and messages are accumulated or lost.

le guide

> Irreversibility: Once a Connect instance is deleted, its configurations and historical monitoring data cannot be restored.
> Pre-check: Do not directly delete the Connect instance that is supporting the core production business services.

1. On the **Connect Instance** page, find the instance that you want to delete and click **Delete**
in the **Operation** column.
2. In the dialog box that appears, click **OK**.

## 5 SDK user guide

### 5.1 SDK overview

This topic lists the protocols supported by ApsaraMQ for RocketMQ 5.0 and the related SDKs in multiple programming languages.

**Supported protocols and SDKs in multiple programming**

**languages**

The following table lists the protocols supported by ApsaraMQ for RocketMQ 5.0 and related SDKs in multiple programming languages.

| Protocol | Programming language | SDK download link | Sample code |
|---|---|---|---|
| TCP | Java | mq-tcp-java-sdk | mq-tcp-samples-java |
|   | C/C++ | mq-tcp-csharp-sdk | mq-tcp-samples- csharp |
|   | .NET | mq-tcp-.net-sdk | mq-tcp-samples-.net |

### 5.2 TCP client SDK reference

#### 5.2.1 Demo projects

##### 5.2.1.1 Overview

This topic helps engineers who are new to ApsaraMQ for RocketMQ 5.0 to build an ApsaraMQ for RocketMQ 5.0 test project. The demo project is a Java project. It contains test code for normal messages, transactional messages, and scheduled messages. The demo project also contains Spring configurations.

##### 5.2.1.2 Prepare the environment

This topic describes how to prepare an environment for an ApsaraMQ for RocketMQ 5.0 demo project.

**Procedure**

Install an integrated development environment (IDE). You can use IntelliJ IDEA or Eclipse as the IDE. In this topic, IntelliJ IDEA is used. Download IntelliJ IDEA Ultimate Edition from IntelliJ IDEA. Then, follow the installation instructions to install IntelliJ IDEA Ultimate Edition. Download a demo project. Download a demo project from GitHub to your on-premises machine. Figure 1. Download a demo project After the downloaded package is decompressed, a folder named mq-demomaster appears on your on-premises machine.

##### 5.2.1.3 Configure a demo project

This topic describes how to configure a demo project.

**Prerequisites**

The environment for the demo project is prepared. You have installed the Java Development Kit (JDK) on your on-premises machine. For more information, visit Java SE Downloads. We recommend that you use JDK 8.

**Procedure**

1. Import the demo project to IntelliJ IDEA.
i. On the IntelliJ IDEA page, click **Import Project** and then select the mq-demo-master folder. Figure 1. Select the mq-demo-master folder ii. Select an import type. Figure 2. Select an import type iii. Click **Next** until the project is imported. The project requires 2 to 3 minutes to be imported because the JAR dependency needs to be loaded to the demo project.
2. Create resources.
Create the required resources, such as topics and group IDs in the ApsaraMQ for RocketMQ 5.0 console and obtain the AccessKey pair in the Apsara Uni-manager Management Console for identity authentication. i. For more information about how to create topics and group IDs, see Create resources. ii. Perform the following operations to obtain the AccessKey ID and AccessKey secret: In the Apsara Uni-manager Management Console, move your pointer over the profile picture and select **User *************. On the page that appears, view the AccessKey ID and AccessKey secret in the ****************** section.
3. Configure the demo project.
Configure the MqConfig class and the common.xml file. i. Configure the MqConfig class by referring to the following sample code:

```
public static final String TOPIC = “The topic that you created in the ApsaraMQ for RocketMQ 5.0 console." public static final String GROUP_ID = “The group ID that you created in the ApsaraM Q for RocketMQ 5.0 console." public static final String ACCESS_KEY = “The AccessKey ID that you created in the A psara Uni-manager Management Console for identity authentication." public static final String SECRET_KEY = “The AccessKey secret that you created in t he Apsara Uni-manager Management Console for identity authentication." public static final String NAMESRV_ADDR = “The TCP endpoint of your ApsaraMQ for Ro cketMQ 5.0 instance. You can obtain the endpoint in the ApsaraMQ for RocketMQ 5.0 console."
```

> **Note:** You must use the AccessKey ID and AccessKey secret of the account that you use to create the topic.

ii. Configure the common.xml file.

```xml
 <props>
 <prop key="AccessKey">XXX</prop> <!-- Modify the values based on your resources. -
```

`->`

```
 <prop key="SecretKey">XXX</prop>
 <prop key="GROUP_ID">XXX</prop>
 <prop key="Topic">XXX</prop>
 <prop key="NAMESRV_ADDR">XXX</prop>
</props>
```

##### 5.2.1.4 Run a demo project

After you configure the demo project, you can start the corresponding classes to send and receive messages of different types.

**Call the main method to send and receive messages**

1. Run the SimpleMQProducer class to send a message.
2. Log in to the RocketMQ v5.0 console.
3. On the Instance List page, click the ID of the instance that you want to manage. On the
**Instance details** page, click the **Message Query** tab and then click the **Query by Topic**
tab. On the Query by Topic tab, select a topic name from the Topic drop-down list and perform a query. Check whether the message is sent to the selected topic.
4. Run the SimpleMQConsumer class to receive the message. You can view logs to check
whether the message is received. The class needs to be initialized, which takes several seconds. Initialization seldom occurs in the production environment. On the Instance details page, click the **Group Management** tab. On the Group Management tab, find the group ID that you want to manage and click **Consumer status** in the **Operation** column. In the **Consumer status** panel, check whether the started consumers are online and subscribed to the selected topic.

**Use Spring to send and receive messages**

1. Run the ProducerClient class to send a message.
2. Run the ConsumerClient class to receive the message.
On the Instance details page, click the **Group Management** tab. On the Group Management tab, find the group ID that you want to manage and click **Consumer status** in the **Operation** column. In the **Consumer status** panel, check whether the started consumers are online and subscribed to the selected topic.

**Send transactional messages**

Run the SimpleTransactionProducer class to send a message.

> **Note:** The LocalTransactionCheckerImpl class is used to check the status of local transactions. This class is used to check whether a local transaction is committed. For more information, see Send and subscribe to transactional messages.

**Send and receive ordered messages**

Run the SimpleOrderConsumer class to receive a message. Run the SimpleOrderProducer class to send a message.

**Note**

Ordered messages are sent and consumed in first-in-first-out (FIFO) order. For more information, see Send and subscribe to ordered messages.

**Send scheduled or delayed messages**

Run the MQTimerProducer class to send a message. The message is delivered after a delay of 3 seconds.

**Note**

You can specify an exact delay, which is up to 3 days. For more information, see Send and subscribe to scheduled messages.

#### 5.2.2 Client parameters

This topic describes the parameters that are configured for ApsaraMQ for RocketMQ 5.0 clients. Table 1. Client parameters

| Parameter | Client | Default value | Recommen ded value | Description | Client version |
|---|---|---|---|---|---|
| AccessKey | Producer or consumer | Configured by the user | Configured by the user | The AccessKey ID that is used to authenticate the user. | >=1.2.7.Fin al |
| SecretKey | Producer or consumer | Configured by the user | Configured by the user | The AccessKey secret that is used to authenticate the user. | >=1.2.7.Fin al |
| NAMESRV A _ DDR | Producer or consumer | Generated after deployment | Generated after deployment | The endpoint of ApsaraMQ for RocketMQ 5.0. | >=1.2.7.Fin al |
| MsgTraceS witch | Producer or consumer | true | true | Specifies whether to enable the message tracing feature of ApsaraMQ for RocketMQ 5.0. | >=1.7.0.Fin al |

| GROUP ID _ | Producer or consumer | Created in the console | Created in the console | The ID of the group to which the producer or consumer client belongs. Group IDs are compatible with producer IDs (PIDs) or consumer IDs (CIDs) in earlier versions. | >=1.7.8.Fin al |
|---|---|---|---|---|---|
| ProducerId | Producer | Created in the console | Created in the console | The ID of the group to which the producer client belongs. This parameter takes effect only on transactional messages. If a producer client fails, the ApsaraMQ for RocketMQ 5.0 broker initiates requests to check the status of transactional messages on other producer clients in the same group. | >=1.2.7.Fin al |
| SendMsgTi meoutMillis | Producer | 5000 | Default | The timeout for sending a message. If the ApsaraMQ for RocketMQ 5.0 broker does not return an acknowledgment to the producer client within the specified period of time, the producer client determines that the message failed to be sent. | >=1.2.7.Fin al |
| ConsumerId | Consumer | Created in the console | Created in the console | The ID of the group to which the consumer client belongs. | >=1.2.7.Fin al |

| MessageMo del | Consumer | CLUSTERIN G | Default | The consumption mode. Valid values: CLUSTERING and BROADCASTING. CLUSTERING specifies that each subscribed message is received by only one consumer client. BROADCASTING specifies that each subscribed message is received by all consumer clients. | >=1.2.7.Fin al |
|---|---|---|---|---|---|
| ConsumeTh readNums | Consumer | Dynamically adjusted from 20 to 64 | Adjusted based on business requirement s | The number of consumer threads. In most cases, this parameter is set to a larger value if a longer time is required to consume a single message. | >=1.2.7.Fin al |
| MaxRecons umeTimes | Consumer | 16 | Default | The maximum number of retries that can be performed when a message fails to be consumed. | >=1.2.7.Fin al |
| ConsumeTi meout | Consumer | 15 | Default | The timeout for consuming each message. If the time to consume a message exceeds the specified timeout, the message fails to be consumed and is resent for consumption after a retry interval. Configure an appropriate value for each business service. Unit: minute. | >=1.2.7.Fin al |

| PostSubscri ptionWhenP ull | Consumer | false | Adjusted based on the consumptio n mode | Specifies whether to carry the latest subscription together with each request. If MessageModel is set to BROADCASTING, this parameter must be set to true to prevent messages from failing to be received due to subscription inconsistency. If MessageModel is set to CLUSTERING, this parameter must be set to false because subscription consistency is required for clustering consumption. | >=1.2.7.Fin al |
|---|---|---|---|---|---|
| ConsumeMe ssageBatch MaxSize | Consumer | 1 | Adjusted based on business requirement s | The maximum number of messages that can be consumed in each batch. The actual number of messages that are consumed in a batch can be smaller than the value of this parameter. The value must be an integer in the range of 1 to 32. The default value is 1. | >=1.6.0.Fin al |

| MaxCached MessageAm ount | Consumer | 5000 | Adjusted based on the memory of consumer clients | The maximum number of messages that a consumer client can cache. A large value can cause an out-of- memory (OOM) issue on the client. The value must be an integer in the range of 100 to 50000. The default value is 5000. | >=1.7.0.Fin al |
|---|---|---|---|---|---|
| MaxCached MessageSiz eInMiB | Consumer | 512 | Adjusted based on the memory of consumer clients | The maximum size of messages that a consumer client can cache. A large value can cause an OOM issue on the client. The value ranges from 16 to 2048. The default value is 512. Unit: MB. | >=1.7.0.Fin al |

#### 5.2.3 Client error codes

This topic describes error codes related to sending and subscribing to messages and their references.

**Error codes related to sending and subscribing to messages**

| Status code | Status flag | Description | Cause and recommended solution | Broker version |
|---|---|---|---|---|
| 13 | MESSAGE ILLEGA _ L | The message verification failed. | 1. Check whether the message body is empty. 2. Check whether the length of the message property exceeds 32,767 bytes. 3. Check whether the total size of the message exceeds 4 MB. | >=4.0.1 |

| 26 | SUBSCRIPTION G _ ROUP NOT EXIST _ _ | The group ID does not exist. | 1. Create a group ID in the ApsaraMQ for RocketMQ 5.0 console. 2. Restart the application. For more information, see the Nonexistent group ID section in Nonexistent resources. | >=4.0.1 |
|---|---|---|---|---|
| 24 | SUBSCRIPTION N _ OT EXIST _ | The subscription does not exist. | 1. Check whether the consumers identified by the group ID have been started. 2. Check whether subscription inconsistency occurs. | >=4.0.1 |
| 23 | SUBSCRIPTION P _ ARSE FAILED _ | The subscription expression failed to be parsed. | Check the subscription expression and tag of the corresponding topic. | >=4.0.1 |
| 25 | SUBSCRIPTION N _ OT LATEST _ | Subscriptions are inconsistent. | If this status persists for a moment, it is automatically restored. For more information, see Inconsistent subscriptions. | >=4.0.1 |

| 14 | SERVICE NOT AV _ _ AILABLE | Messages cannot be sent. | The requested broker is discontinued, the broker is abnormal and does not support write operations, or the broker is a secondary broker. For more information, see the Messages failed to be sent section in ApsaraMQ for RocketMQ exceptions and solutions. | >=4.0.1 |
|---|---|---|---|---|
| 16 | NO PERMISSION _ (message sending) | The request is invalid. | The requested broker disallows write operations. The topic on the requested broker disallows write operations. The requested broker disallows transactional messages. | >=4.0.1 |
| 16 | NO PERMISSION _ (message subscription) | The request is invalid. | The requested broker disallows read operations. The current consumer group disallows read operations. The pulled topic disallows read operations. The current consumer group disallows message broadcasting. | >=4.0.1 |

| 1 | SYSTEM ERROR _ | A system exception occurred. | This is a temporary timeout that results from the restart of the ApsaraMQ for RocketMQ 5.0 broker or heavy load on the broker. For more information, see the Messages failed to be sent section in ApsaraMQ for RocketMQ exceptions and solutions. | >=4.0.1 |
|---|---|---|---|---|
| 1 | SYSTEM ERROR _ (permission verification) | The permission verification failed. | Check whether the user is granted the permissions to publish messages to and subscribe to messages from the topic. | >=4.0.1 |
| 2 | SYSTEM BUSY _ | The system is busy, and the request is rejected. | This is a temporary timeout that results from the restart of the ApsaraMQ for RocketMQ 5.0 broker or heavy load on the broker. For more information, see the Messages failed to be sent section in ApsaraMQ for RocketMQ exceptions and solutions. | >=4.0.1 |

#### 5.2.4 Java SDK

##### 5.2.4.1 Instructions for use

ApsaraMQ for RocketMQ 5.0 provides SDK for Java for you to send and subscribe to messages. This topic describes the parameters of methods in SDK for Java and how to call these methods. Table 1. Common parameters

| Parameter | Description |
|---|---|
| NAMESRV ADDR _ | The TCP endpoint. You can obtain the TCP endpoint from the Network Management tab on the Instance details page in the ApsaraMQ for RocketMQ 5.0 console. |
| AccessKey | The AccessKey ID that you created in the Apsara Uni-manager Management Console for identity authentication. |
| SecretKey | The AccessKey secret that you created in the Apsara Uni- manager Management Console for identity authentication. |
| OnsChannel | The user channel. Default value: ALIYUN. |

Table 2. Parameters for message sending

| Parameter | Description |
|---|---|
| SendMsgTimeoutMillis | The timeout period for sending messages. Unit: milliseconds. Default value: 3000. |
| CheckImmunityTimeInSeconds（事务消息） | 设置事务消息第一次回查的最快时间，单位（秒）。 |
| shardingKey（顺序消息） | 顺序消息中用来计算不同分区的值。 |

Figure 1. Methods and parameters for using SDK for Java to send messages Table 3. Parameters for message subscription

| Parameter | Description |
|---|---|
| GROUP ID _ | The group ID that you created in the ApsaraMQ for RocketMQ 5.0 console. |
| MessageModel | The mode in which a consumer instance consumes messages. Valid values: CLUSTERING and BROADCASTING. Default value: CLUSTERING. |
| ConsumeThreadNums | The number of consumer threads for a consumer instance. Default value: 64. |
| MaxReconsumeTimes | The maximum number of retries upon a consumption failure. Default value: 16. |
| ConsumeTimeout | The timeout period for consuming each message. If the time for consuming a message exceeds the specified timeout period, the message fails to be consumed and is redelivered after a retry interval. Configure an appropriate value for each business service. Unit: minute. Default value: 15. |
| suspendTimeMillis（顺序消息） | 只适用于顺序消息，设置消息消费失败的重试间隔时间。 |
| maxCachedMessageAmount | The maximum number of messages cached on the on- premises client. Default value: 1000. |
| maxCachedMessageSizeInMiB | The maximum size of messages cached on the on-premises client. Valid values: 16 MB to 2 GB. Default value: 512 MB. |

Figure 2. Methods and parameters for using SDK for Java to subscribe to messages

**Sample code for sending and subscribing to messages**

##### 5.2.4.2 Environment preparations

Before you run the Java code provided in this topic, perform the following steps to prepare the environment.

**Procedure**

1. Use either of the following methods to add the dependency:
Add the dependency by using Maven:

```xml
<dependency>
    <groupId>com.aliyun.openservices</groupId>
   <artifactId>ons-client</artifactId>
   <version>1.8.4.Final</version>
</dependency>
```

Download a JAR file that contains the dependency
2. Create the topics and group IDs that are referred to in the code of the TCP client SDK for
Java in the ApsaraMQ for RocketMQ 5.0 console. You can specify custom message tags in your application. For information about how to create a message tag, see Create resources.
3. For applications that use the TCP client SDK to access ApsaraMQ for RocketMQ 5.0, make
sure that the applications are deployed on Elastic Compute Service (ECS) instances in the same region.

##### 5.2.4.3 Logging configurations

Client logs record exceptions that occur when clients are running. These logs can help you quickly locate and handle exceptions. This topic describes how to print the logs of an ApsaraMQ for RocketMQ 5.0 client and provides the default and custom configurations.

**Print client logs**

The TCP client SDK for Java of ApsaraMQ for RocketMQ 5.0 is developed by using the SLF4J API.

**For SDK for Java 1.7.8.Final or later**

SDK for Java 1.7.8.Final provided by ApsaraMQ for RocketMQ 5.0 has a built-in framework for logging. You do not need to add a dependency on the corresponding logging framework for an application on the client before you print the logs of an ApsaraMQ for RocketMQ 5.0 client. For information about the default logging configuration for an ApsaraMQ for RocketMQ 5.0 client and how to modify such configuration, see the Custom configurations section in this topic.

**For versions earlier than SDK for Java 1.7.8.Final**

Versions earlier than SDK for Java 1.7.8.Final of ApsaraMQ for RocketMQ 5.0 support only Log4j and Logback but not Log4j2. You must add a dependency on the corresponding logging framework to the pom.xml file or the .lib file before you print the logs of an ApsaraMQ for RocketMQ 5.0 client. The following sample code provides examples on how to add dependencies on Log4j and Logback:

**Method 1: Use Log4j as the logging implementation dependency**

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

**Method 2: Use Logback as the logging implementation dependency**

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

> **Note:** If an application uses both Log4j and Logback as logging implementation dependencies, client logs cannot be properly printed due to logging conflicts. To properly print the logs of an ApsaraMQ for RocketMQ 5.0 client, make sure that you add only one dependency on one logging framework for the application. We recommend that you run the **mvn clean dependency:tree | grep log** command to check whether your application uses only one of the logging frameworks.

**Configure logging for an ApsaraMQ for RocketMQ 5.0 client**

You can customize the following settings for an ApsaraMQ for RocketMQ 5.0 client: **the path**
**for storing log files**, **log level**, and **maximum number of historical log files retained** .
To facilitate log transmission and viewing, the **maximum size of a single log file** retains the default value of 64 MB. This value cannot be changed. The following table describes these parameters.

| Parameter | Description |
|---|---|
| Path to store log files | Make sure that the application has the write permissions for this path. Otherwise, logs cannot be printed. |
| Maximum number of historical log files retained | You can set this parameter to a value between 1 and 100. If you enter a value that is not within this range or a value that is in an invalid format, the system retains 10 historical log files by default. |
| Log level | You can set this parameter to one of the following values: ERROR, WARN, INFO, and DEBUG. If this parameter is set to an invalid value, the system uses the default value INFO. |

**Default configurations**

After you start an ApsaraMQ for RocketMQ 5.0 client, the client generates log files based on the following default configurations: Path to store log files: `/{user.home}/logs/ons.log` , where `{user.home}` is the root directory of the account that runs the current Java process. Maximum number of historical log files retained: 10. Log level: INFO. Maximum size of a single log file: 64 MB.

**Custom configurations**

> **Note:** To customize the logging configuration of an ApsaraMQ for RocketMQ 5.0 client, update SDK for Java to V1.2.5 or later.

To customize the logging configuration of an ApsaraMQ for RocketMQ 5.0 client in SDK for Java, configure the following system parameters: ons.client.logRoot: the path to store log files. ons.client.logFileMaxIndex: the maximum number of historical log files retained. ons.client.logLevel: the log level.

**Examples**

Add the following system parameters to the startup script or VM options of the integrated development environment (IDE):

**Linux example**

```
-Dons.client.logRoot=/home/admin/logs -Dons.client.logLevel=WARN - Dons.client.logFileMaxIndex=20
```

**Windows example**

```
-Dons.client.logRoot=D:\logs -Dons.client.logLevel=WARN - Dons.client.logFileMaxIndex=20
```

/home/admin/ and D:\ are for reference only. Replace them as needed.

##### 5.2.4.4 Spring integration

###### 5.2.4.4.1 Overview

This topic describes how to send and receive messages by using ApsaraMQ for RocketMQ 5.0 in the Spring framework. This topic includes three parts: the integration of a normal message producer and Spring, the integration of a transactional message producer and Spring, and the integration of a message consumer and Spring. The subscriptions of all consumer instances identified by the same group ID must be consistent. For more information, see Subscription consistency. The configuration parameters supported in the Spring framework are the same as those used in TCP client SDK for Java. For more information, see Usage notes.

###### 5.2.4.4.2 Integrate a producer with Spring

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
         <property name="properties" > <!-- Configurations of the producer -->
             <props>
                 <prop key="AccessKey">XXX</prop>
                 <prop key="SecretKey">XXX</prop>
                 <!-- For ons-client in version 1.8.4.Final, configuration is required
. To do this, copy the TCP endpoint from the instance details page.
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
         // Cyclically send a message.
         for (int i = 0; i < 100; i++) {
             Message msg = new Message( //
                     // The topic to which the message belongs.
                     "TopicTestMQ",
                     // The message tag, which is similar to a Gmail tag. It is used t
o sort messages and help the consumer filter messages on the ApsaraMQ for RocketMQ 5.0 broker based on specified conditions.
                     "TagA",
                     // The message body in the binary format. ApsaraMQ for RocketMQ 5
.0 does not process the message body.
                     // The producer and consumer must agree on the serialization and
deserialization methods.
                     "Hello MQ".getBytes());
             // The key of messages. The key is the business-specific attribute of th
e message and must be globally unique whenever possible.
             // A unique key helps you query and resend a message in the console if t
he message fails to be received.
             // Note: A message can be sent and received even if you do not specify a
message key.
             msg.setKey("ORDERID_100");
             // Send the message. If no error occurs, the message is sent.
             try {
                 SendResult sendResult = producer.send(msg);
                 assert sendResult != null;
                 System.out.println("send success: " + sendResult.getMessageId());
             }catch (ONSClientException e) {
                 System.out.println("Failed to send the message.");
```

`}` `}` `}` `}`

###### 5.2.4.4.3 Integrate a transactional message producer with Spring

**producer with Spring**

This topic describes how to integrate a producer that produces transactional messages with Spring.

**Background information**

For more information about transactional messages, see Send and subscribe to transactional messages.

**Procedure**

1. Implement the LocalTransactionChecker class. A producer can have only one
LocalTransactionChecker class.

```java
package demo; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.transaction.LocalTransactionChecker; import com.aliyun.openservices.ons.api.transaction.TransactionStatus; public class DemoLocalTransactionChecker implements LocalTransactionChecker {
    public TransactionStatus check(Message msg) {
        System.out.println("Start to back-check the status of the local
transaction");
        return TransactionStatus.CommitTransaction; // Return different values for Tr
ansactionStatus based on the status check result of the local transaction.
```

`}` `}`
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
         <property name="properties" > <!--Configurations of the transactional
message producer-->
             <props>
                 <prop key="AccessKey">AKDEMO</prop>
                 <prop key="SecretKey">SKDEMO</prop>
                 <prop key="GROUP_ID">GID_DEMO</prop>
                 <!-- For ons-client in version 1.8.4.Final, configuration is required
. To do this, copy the TCP endpoint from the instance details page.
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
                 return TransactionStatus.CommitTransaction; // Return different value
s for TransactionStatus based on the execution result of the local transaction.
```

`}`

```
         }, null);
```

`}` `}`

###### 5.2.4.4.4 Integrate a consumer with Spring

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

`}` `}` `}`
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
                 <!-- For ons-client in version 1.8.4.Final, configuration is required
Todothis cop theTCPendpointfromtheinstancedetailspage
```

```xml
. To do this, copy the TCP endpoint from the instance details page.
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
is the tag. You can set the value to a specific tag or *. For example, a specific tag can be taga||tagb||tagc. "*" indicates that all tags are subscribed to. Wildcar ds are not supported.-->
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
scribe to multiple tags. -->
```

```
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

`}` `}`

##### 5.2.4.5 Three modes for sending messages

###### 5.2.4.5.1 Overview

In ApsaraMQ for RocketMQ 5.0, messages can be sent in reliable synchronous mode,reliable asynchronous mode, and one-way mode. This topic describes the principles, scenarios, and differences of these modes, and provides sample code for your reference.

> **Note:** Ordered messages can be sent only in reliable synchronous mode.

###### 5.2.4.5.2 Reliable synchronous transmission

This topic describes the principle and scenarios of the reliable synchronous transmission mode.

**Principle**

**p**

Synchronous transmission means that the message producer sends the next message only after it receives a response to the previous message from the ApsaraMQ for RocketMQ broker. Figure 1. Synchronous transmission

**Scenarios**

You can use the synchronous transmission mode in scenarios in which you want to send important notification emails, notification messages for registration, and promotional messages.

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
        // The timeout for sending a message, in milliseconds.
        properties.setProperty(PropertyKeyConst.SendMsgTimeoutMillis, "3000");
        // The TCP endpoint. You can view the TCP endpoint on the Network Management ta
b of the instance details page in the ApsaraMQ for RocketMQ console.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
```

```java
        Producer producer = ONSFactory.createProducer(properties);
        // Before you use the producer to send a message, call the start() method once
to start the producer.
        producer.start();
        // Cyclically send a message.
        for (int i = 0; i < 10; i++){
            Message msg = new Message( //
                // The topic to which the message belongs.
                "TopicTestMQ",
                // The message tag, which is similar to a Gmail tag. It is used to sort
messages and help the consumer filter messages on the ApsaraMQ for RocketMQ 5.0 broker based on specified conditions.
                "TagA",
                // The message body in the binary format. ApsaraMQ for RocketMQ 5.0
does not process the message body.
                // The producer and consumer must agree on the serialization and
deserialization methods.
                "Hello MQ".getBytes());
            // The key of the message. The key is the business-specific attribute of th
e message and must be globally unique whenever possible.
            // A unique key enables you to query a message and resend it in the Apsara
Uni-manager Management Console if you fail to receive the message.
            // Note: A message can be sent and received even if you do not specify a me
ssage key.
            msg.setKey("ORDERID_" + i);
            try {
                SendResult sendResult = producer.send(msg);
                // Send the message in synchronous mode. If no error occurs, the message
is sent.
                if (sendResult != null) {
                    System.out.println(new Date() + " Send mq message success. Topic is:
" + msg.getTopic() + " msgId is: " + sendResult.getMessageId());
```

`}` `}`

```java
            catch (Exception e) {
                // Specify the logic to resend or persist the message if the message fai
ls to be sent.
                System.out.println(new Date() + " Send mq message failed. Topic is:" + m
sg.getTopic());
                e.printStackTrace();
```

`}` `}`

```
        // Before you exit the application, shut down the producer.
        // Note: This step is optional.
        producer.shutdown();
```

`}` `}`

###### 5.2.4.5.3 Reliable asynchronous transmission

This topic describes the principle and scenarios of the reliable asynchronous transmission mode.

**Principle**

In reliable asynchronous transmission mode, a producer sends the next message without waiting for a response to the previous message from the ApsaraMQ for RocketMQ broker. Before you use the asynchronous transmission mode in ApsaraMQ for RocketMQ 5.0 to send messages, you must write the implementation logic of the SendCallback operation. An application sends the next message before it receives a response to the previous message from the ApsaraMQ for RocketMQ broker. After the SendCallback operation is called, the application receives the response to the previous message from the ApsaraMQ for RocketMQ broker and processes the response. Figure 1. Asynchronous transmission

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
    public static void main(String[] args) {
        Properties properties = new Properties();
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
le for identity authentication.
        properties.put(PropertyKeyConst.AccessKey, "XXX");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
```

```java
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The timeout for sending a message, in milliseconds.
        properties.setProperty(PropertyKeyConst.SendMsgTimeoutMillis, "3000");
        // The TCP endpoint. You can view the TCP endpoint on the Network Management ta
b of the instance details page in the ApsaraMQ for RocketMQ console.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        Producer producer = ONSFactory.createProducer(properties);
        // Before you use the producer to send a message, call the start() method once
to start the producer.
        producer.start();
        Message msg = new Message(
                // The topic to which the message belongs.
                "TopicTestMQ",
                // The message tag, which is similar to a Gmail tag. It is used to sort
messages and help the consumer filter messages on the ApsaraMQ for RocketMQ 5.0 broker based on specified conditions.
                "TagA",
                // The message body in the binary format. ApsaraMQ for RocketMQ 5.0
does not process the message body. The producer and consumer must agree on the serializ ation and deserialization methods.
                "Hello MQ".getBytes());
        // The key of the message. The key is the business-specific attribute of the me
ssage and must be globally unique whenever possible. A unique key helps you query and resend a message in the console if the message fails to be received.
        // Note: A message can be sent and received even if you do not specify a messag
e key.
        msg.setKey("ORDERID_100");
        // Send the message in asynchronous mode. The result is returned to the
producer after the producer calls the callback function.
        producer.sendAsync(msg, new SendCallback() {
            @Override
            public void onSuccess(final SendResult sendResult) {
                // The message is sent.
                System.out.println("send message success. topic=" +
sendResult.getTopic() + ", msgId=" + sendResult.getMessageId());
```

`}`

```java
            @Override
            public void onException(OnExceptionContext context) {
                // Specify the logic to resend or persist the message if the message fai
ls to be sent.
                System.out.println("send message failed. topic=" + context.getTopic() +
", msgId=" + context.getMessageId());
```

`}`

```java
        });
        // The message ID can be obtained before the callback function returns the resu
lt.
        System.out.println("send message async. topic=" + msg.getTopic() + ", msgId=" +
msg.getMsgID());
        // Before you exit the application, shut down the producer.   Note: This step i
s optional.
        producer.shutdown();
```

`}`

###### 5.2.4.5.4 One-way transmission

This topic describes the principle and scenarios of the one-way transmission mode, and provides sample code.

**Principle**

In one-way transmission mode, a producer only sends messages and does not wait for a response from the ApsaraMQ for RocketMQ broker. In addition, no callback function is triggered. In this mode, a message can be sent within microseconds. Figure 1. One-way transmission

**Scenarios**

This mode is applicable to scenarios where message transmission takes a short time and has low requirements for reliability. For example, this mode can be used for log collection. The following table summarizes the features of and major differences among the three modes.

| Transmission mode | Transactions per second (TPS) | Response | Reliability |
|---|---|---|---|
| Synchronous transmission | High | Yes | No message loss |
| Asynchronous transmission | High | Yes | No message loss |
| One-way transmission | Highest | No | Possible message loss |

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
        // The timeout for sending a message, in milliseconds.
        properties.setProperty(PropertyKeyConst.SendMsgTimeoutMillis, "3000");
        // The TCP endpoint. You can view the TCP endpoint on the Network Management ta
b of the instance details page in the ApsaraMQ for RocketMQ console.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        Producer producer = ONSFactory.createProducer(properties);
        // Before you use the producer to send a message, call the start() method once
to start the producer.
        producer.start();
        // Cyclically send a message.
        for (int i = 0; i < 10; i++){
            Message msg = new Message(
                    // The topic to which the message belongs.
                    "TopicTestMQ",
                    // Message Tag,
                    // It is similar to a Gmail tag. It is used to sort messages and hel
p the consumer filter messages on the ApsaraMQ for RocketMQ 5.0 broker based on specifi ed conditions.
                    "TagA",
                    // Message Body
                    // It is in the binary format. ApsaraMQ for RocketMQ 5.0 does not pr
ocess the message body. The producer and consumer must agree on the serialization and d eserialization methods.
                    "Hello MQ".getBytes());
            // The key of the message. The key is the business-specific attribute of th
e message and must be globally unique whenever possible.
            // A unique key enables you to query a message and resend it in the Apsara
Uni-manager Management Console if you fail to receive the message.
            // Note: A message can be sent and received even if you do not specify a me
ssage key.
            msg.setKey("ORDERID_" + i);
            // In one-way transmission mode, the producer does not wait for the
response from the ApsaraMQ for RocketMQ broker. Therefore, data loss occurs if messages that fail to be sent are not resent. If data loss is not acceptable, we recommend that you use the reliable synchronous or asynchronous transmission mode.
            producer.sendOneway(msg);
```

`}`

```
        // Before you exit the application, shut down the producer.
        // Note: This step is optional.
        producer.shutdown();
```

`}`

##### 5.2.4.6 Send messages by using multiple threads

This topic describes how to send messages by using multiple threads and provides sample code. The consumer and producer objects of ApsaraMQ for RocketMQ 5.0 are thread-secure and can be shared among threads. You can deploy multiple producer and consumer instances on one or more brokers. You can also run multiple threads to send or receive messages in a producer or consumer instance. This improves the transactions per second (TPS) for sending or receiving messages. Do not create a producer instance or consumer instance for each thread. The following sample code provides an example on how to share a producer among threads:

```java
import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.Producer; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.SendResult; import java.util.Properties; public class SharedProducer {
    public static void main(String[] args) {
        // Initialize the configuration of a producer instance.
        Properties properties = new Properties();
        // The group ID that you created in the console.
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
le for identity authentication.
        properties.put(PropertyKeyConst.AccessKey,"XXX");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The timeout for sending a message, in milliseconds.
        properties.setProperty(PropertyKeyConst.SendMsgTimeoutMillis, "3000");
        // The TCP endpoint. You can view the TCP endpoint on the Network Management ta
b of the instance details page in the ApsaraMQ for RocketMQ console.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        final Producer producer = ONSFactory.createProducer(properties);
        // Before you use the producer to send a message, call the start() method once
to start the producer.
        producer.start();
        // The created producer and consumer objects are thread-secure and can be share
d among threads. Do not create a producer instance or consumer instance for each thread
```

`.`

```java
        // Two threads share the producer object and concurrently send a message to Aps
araMQ for RocketMQ 5.0.
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Message msg = new Message( //
```

```java
                    // The topic to which the message belongs.
                    "TopicTestMQ",
                    // The message tag, which is similar to a Gmail tag. It is used to s
ort messages and help the consumer filter messages on the ApsaraMQ for RocketMQ 5.0 broker based on specified conditions.
                    "TagA",
                    // The message body in the binary format. ApsaraMQ for RocketMQ 5.0
does not process the message body.
                    // The producer and consumer must agree on the serialization and des
erialization methods.
                    "Hello MQ".getBytes());
                    SendResult sendResult = producer.send(msg);
                    // Send the message in synchronous mode. If no error occurs, the mes
sage is sent.
                    if (sendResult != null) {
                        System.out.println(new Date() + " Send mq message success. Topic
is:" + MqConfig.TOPIC + " msgId is: " + sendResult.getMessageId());
```

`}`

```java
                } catch (Exception e) {
                    // Specify the logic to resend or persist the message if the message
fails to be sent.
                    System.out.println(new Date() + " Send mq message failed. Topic is:"
+ MqConfig.TOPIC);
                    e.printStackTrace();
```

`}` `}`

```java
        });
        thread.start();
        Thread anotherThread = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Message msg = new Message("TopicTestMQ", "TagA", "Hello MQ".getBytes
());
                    SendResult sendResult = producer.send(msg);
                    // Send the message in synchronous mode. If no error occurs, the mes
sage is sent.
                    if (sendResult != null) {
                        System.out.println(new Date() + " Send mq message success. Topic
is:" + MqConfig.TOPIC + " msgId is: " + sendResult.getMessageId());
```

`}`

```java
                } catch (Exception e) {
                    // Specify the logic to resend or persist the message if the message
fails to be sent.
                    System.out.println(new Date() + " Send mq message failed. Topic is:"
+ MqConfig.TOPIC);
                    e.printStackTrace();
```

`}` `}`

```
        });
        anotherThread.start();
        // If the producer instance is no longer used, shut it down to release
resources.
        // producer.shutdown();
```

`}` `}`

##### 5.2.4.7 Send and subscribe to ordered messages

This topic describes how to send and subscribe to ordered messages and provides sample code. Ordered messages, also known as first-in, first-out (FIFO) messages, are a type of messages provided by ApsaraMQ for RocketMQ 5.0. Ordered messages are published and consumed in a strict order. This topic provides sample code for using the TCP client SDK for Java to send and subscribe to ordered messages. For more information, see Ordered messages. Use SDK for Java 1.2.7 or later to send and subscribe to ordered messages.

**Sample code for sending ordered messages**

```java
package com.aliyun.openservices.ons.example.order; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.SendResult; import com.aliyun.openservices.ons.api.order.OrderProducer; import java.util.Properties; public class ProducerClient {
    public static void main(String[] args) {
        Properties properties = new Properties();
        // The ID of the consumer group that you created in the ApsaraMQ for RocketMQ 5
.0 console.
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
le for identity authentication.
        properties.put(PropertyKeyConst.AccessKey, "XXX");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The TCP endpoint. You can view the TCP endpoint on the Network Management ta
b of the instance details page in the ApsaraMQ for RocketMQ 5.0 console.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        OrderProducer producer = ONSFactory.createOrderProducer(properties);
        // Before you send a message, call the start() method only once to start the pr
oducer.
        producer.start();
        for (int i = 0; i < 10; i++) {
            String orderId = "biz_" + i % 10;
            Message msg = new Message(//
                    // The topic of the message.
                    "Order_global_topic",
                    // The message tag, which is similar to a Gmail tag. It is used to s
ort messages and help the consumer filter messages on the ApsaraMQ for RocketMQ 5.0 broker based on specified conditions.
                    "TagA",
                    // The message body in the binary format. ApsaraMQ for RocketMQ 5.0
doesnotprocessthemessagebody Theproducerandconsumermustagreeontheserializ
```

```
does not process the message body. The producer and consumer must agree on the serializ ation and deserialization methods.
                    "send order global msg".getBytes()
```

);

```java
            // The key of the message. The key is the business-specific attribute of th
e message and must be globally unique whenever possible.
            // A unique key helps you query and resend a message in the console if the
message fails to be received.
            // Note: A message can be sent and received even if you do not specify a me
ssage key.
            msg.setKey(orderId);
            // The key field that is used in ordered messages to identify different
partitions. The sharding key is different from the key of a normal message.
            String shardingKey = String.valueOf(orderId);
            try {
                SendResult sendResult = producer.send(msg, shardingKey);
                // Send the message. If no exception occurs, the message is sent.
                if (sendResult != null) {
                    System.out.println(new Date() + " Send mq message success. Topic is:
" + msg.getTopic() + " msgId is: " + sendResult.getMessageId());
```

`}` `}`

```java
            catch (Exception e) {
                // Specify the logic to resend or persist the message if the message fai
ls to be sent.
                System.out.println(new Date() + " Send mq message failed. Topic is:" + m
sg.getTopic());
                e.printStackTrace();
```

`}` `}`

```
        // Before you exit the application, shut down the producer.
        // Note: This step is optional.
        producer.shutdown();
```

`}` `}`

**Sample code for subscribing to ordered messages**

```java
package com.aliyun.openservices.ons.example.order; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.order.ConsumeOrderContext; import com.aliyun.openservices.ons.api.order.MessageOrderListener; import com.aliyun.openservices.ons.api.order.OrderAction; import com.aliyun.openservices.ons.api.order.OrderConsumer; import java.util.Properties; public class ConsumerClient {
    public static void main(String[] args) {
        Properties properties = new Properties();
        // The ID of the consumer group that you created in the ApsaraMQ for RocketMQ 5
.0 console.
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
```

```
le for identity authentication.
        properties.put(PropertyKeyConst.AccessKey, "XXX");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The TCP endpoint. You can view the TCP endpoint on the Network Management ta
b of the instance details page in the ApsaraMQ for RocketMQ 5.0 console.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
          // The delay time in milliseconds before the retry upon a consumption failure
of an ordered message. Value range: 10 to 1800.
        properties.put(PropertyKeyConst.SuspendTimeMillis, "100");
        // The maximum number of retries upon a consumption failure.
        properties.put(PropertyKeyConst.MaxReconsumeTimes, "20");
        // Before you subscribe to a message, call the start() method once to start the
consumer.
        OrderConsumer consumer = ONSFactory.createOrderedConsumer(properties);
        consumer.subscribe(
                // The topic of the message.
                "Jodie_Order_Topic",
                // Subscribe to messages with specific tags in the specified topic.
                // 1. An asterisk (*) specifies that the consumer subscribes to all
messages.
                // 2. TagA||TagB||TagC specifies that the consumer subscribes to message
s attached with Tag A, Tag B, or Tag C.
                "*",
                new MessageOrderListener() {
                    /**
                     * 1. If the message fails to be consumed or an exception occurs dur
ing message processing, OrderAction.Suspend is returned.<br>
                     * 2. If the message is processed, OrderAction.Success is returned.
```

`*/`

```java
                    @Override
                    public OrderAction consume(Message message, ConsumeOrderContext cont
ext) {
                        System.out.println(message);
                        return OrderAction.Success;
```

`}`

```
                });
        consumer.start();
```

`}` `}`

##### 5.2.4.8 Send and subscribe to transactional messages

**messages**

This topic describes the interaction process and the status check mechanism of transactional messages. This topic also shows you how to send and subscribe to transactional messages, and provides sample code.

**Interaction process**

The following figure shows the interaction process of transactional messages in ApsaraMQ for RocketMQ 5.0. Figure 1. Interaction process of transactional messages

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
     // The group ID that you created in the ApsaraMQ for RocketMQ 5.0 console. Note:
Transactional messages cannot share group IDs with other types of messages.
     properties.put(PropertyKeyConst.GROUP_ID, "XXX");
     // The AccessKey ID that you created in the Apsara Uni-manager Management Consol
e for identity authentication.
     properties.put(PropertyKeyConst.AccessKey, "XXX");
     // The AccessKey secret that you created in the Apsara Uni-manager Management Co
nsole for identity authentication.
     properties.put(PropertyKeyConst.SecretKey, "XXX");
     // The TCP endpoint. You can view the TCP endpoint on the Network Management tab
of the instance details page in the ApsaraMQ for RocketMQ 5.0 console.
     properties.put(PropertyKeyConst.NAMESRV_ADDR,
       "XXX");
     TransactionProducer producer = ONSFactory.createTransactionProducer(properties,
             new LocalTransactionCheckerImpl());
     producer.start();
     Message msg = new Message("Topic", "TagA", "Hello MQ
transaction===".getBytes()); try{
```

```java
     try {
             SendResult sendResult = producer.send(msg, new
LocalTransactionExecuter() {
                 @Override
                 public TransactionStatus execute(Message msg, Object arg) {
                     // The message ID. Two messages can have the same message body bu
t not the same ID. You cannot query the ID of the current message in the ApsaraMQ for RocketMQ 5.0 console.
                     String msgId = msg.getMsgID();
                     // Calculate the message body by using CRC32 or other algorithms,
such as MD5.
                     long crc32Id = HashUtil.crc32Code(msg.getBody());
                     // The message ID and CRC32 ID are used to prevent duplicate mess
ages.
                     // You do not need to specify the message ID or CRC32 ID if your
business is idempotent. Otherwise, specify the message ID or CRC32 ID to ensure idemp otency.
                     // To prevent duplicate messages, we recommend that you calculate
the message body by using the CRC32 or MD5 algorithm.
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
```

`}`

```
                     } catch (Exception e) {
                         log.error("Message Id:{}", msgId, e);
```

`}`

```java
                     System.out.println(msg.getMsgID());
                     log.warn("Message Id:{}transactionStatus:{}", msgId, transactionS
tatus.name());
                     return transactionStatus;
```

`}`

```
             }, null);
```

`}`

```java
         catch (Exception e) {
             // Specify the logic to resend or persist the message if the message
fails to be sent.
             System.out.println(new Date() + " Send mq message failed. Topic is:" +
msg.getTopic());
             e.printStackTrace();
```

`}`

```
     // Use the demo example to prevent the process from exiting. This is not require
d in actual use.
     TimeUnit.MILLISECONDS.sleep(Integer.MAX_VALUE);
```

`}` `}`
2. Commit the transaction status of the message.
After the local transaction is executed, the ApsaraMQ for RocketMQ 5.0 broker must be notified of the transaction status of the current message, no matter whether the execution succeeds or fails. You can notify the ApsaraMQ for RocketMQ 5.0 broker by using one of the following methods: Commit the status after the local transaction is executed. Wait until the ApsaraMQ for RocketMQ 5.0 broker sends a request to check the transaction status of the message. A transaction can be in one of the following states:
**TransactionStatus.CommitTransaction**: The transaction is committed. The message
can be consumed by consumers.
**TransactionStatus.RollbackTransaction**: The transaction is rolled back. The message
is discarded and cannot be consumed.
**TransactionStatus.Unknow**: The transaction status is unknown. The ApsaraMQ for
RocketMQ 5.0 broker is expected to send a request again to the producer to query the status of the local transaction that corresponds to the message.

```java
public class LocalTransactionCheckerImpl implements LocalTransactionChecker {
   private final static Logger log = ClientLogger.getLog();
   final  BusinessService businessService = new BusinessService();
   @Override
   public TransactionStatus check(Message msg) {
       // The message ID. Two messages can have the same message body but not the sam
e ID. The current message is a half message. You cannot query its ID in the ApsaraMQ for RocketMQ 5.0 console.
       String msgId = msg.getMsgID();
       // Calculate the message body by using CRC32 or other algorithms, such as MD5.
       long crc32Id = HashUtil.crc32Code(msg.getBody());
       // The message ID and CRC32 ID are used to prevent duplicate messages.
       // You do not need to specify the message ID or CRC32 ID if your business is i
dempotent. Otherwise, specify the message ID or CRC32 ID to ensure idempotency.
       // To prevent duplicate messages, we recommend that you calculate the message
body by using the CRC32 or MD5 algorithm.
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
```

`}`

```
       } catch (Exception e) {
           log.error("Message Id:{}", msgId, e);
```

`}`

```
       log.warn("Message Id:{}transactionStatus:{}", msgId,
transactionStatus.name());
       return transactionStatus;
```

`}` `}`

**Utility class**

```java
import java.util.zip.CRC32; public class HashUtil {
    public static long crc32Code(byte[] bytes) {
        CRC32 crc32 = new CRC32();
        crc32.update(bytes);
        return crc32.getValue();
```

`}` `}`

**Mechanism of transaction status check**

Why must the mechanism of transaction status check be implemented when transactional messages are sent? If the half message is sent in Step 1 but **TransactionStatus.Unknow** is returned for the local transaction, or no status is committed for the local transaction because the application exits, the status of the half message is unknown to the ApsaraMQ for RocketMQ 5.0 broker. Therefore, the ApsaraMQ for RocketMQ 5.0 broker periodically requests the producer to check and report the status of the half message. What does the business logic do when the check method is called back? The check method for transactional messages in ApsaraMQ for RocketMQ 5.0 must contain the logic of transaction consistency check. After a transactional message is sent, ApsaraMQ for RocketMQ 5.0 must call the **LocalTransactionChecker** operation to respond to the request of the ApsaraMQ for RocketMQ 5.0 broker for the status of the local transaction. Therefore, the check method for transactional messages must contain the following logic: i. Check whether the local transaction that corresponds to the half message is committed or rolled back. ii. Commit the status of the local transaction that corresponds to the half message to the ApsaraMQ for RocketMQ 5.0 broker.

**Subscribe to transactional messages**

The method for subscribing to transactional messages is the same as that for subscribing to normal messages. For more information, see Subscribe to messages.

##### 5.2.4.9 Send and subscribe to delayed messages

This topic describes how to send and subscribe to delayed messages and provides sample code. Delayed messages are delivered to a client after a delay. For example, if the delay period is 3 seconds, messages are forwarded from the ApsaraMQ for RocketMQ 5.0 broker to the client for consumption after a 3-second delay. Delayed messages can be used when a time window is required between the production and consumption of the messages, or when tasks need to be triggered after a delay. Delayed messages are similar to delayed queues. For information about the terms and usage notes for using delayed messages, see Scheduled and delayed messages.

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
        // The TCP endpoint. You can view the TCP endpoint on the Network Management ta
b of the instance details page in the ApsaraMQ for RocketMQ 5.0 console.
        properties.put(PropertyKeyConst.NAMESRVADDR,
```

`p` `p` `p` `(` `p` `y` `y` `_` `,`

```java
          "XXX");
        Producer producer = ONSFactory.createProducer(properties);
        // Before you use the producer to send a message, call the start() method once
to start the producer.
        producer.start();
        Message msg = new Message( //
                // The topic that you created in the ApsaraMQ for RocketMQ 5.0 console.
                "Topic",
                // The message tag, which is similar to a Gmail tag. It is used to sort
messages and help the consumer filter messages on the ApsaraMQ for RocketMQ 5.0 broker based on specified conditions.
                "tag",
                // The message body in the binary format. ApsaraMQ for RocketMQ 5.0
does not process the message body. The producer and consumer must agree on the serializ ation and deserialization methods.
                "Hello MQ".getBytes());
        // The key of the message. The key is the business-specific attribute of the me
ssage and must be globally unique whenever possible.
        // A unique key helps you query and resend a message in the console if the mess
age fails to be received.
        // Note: A message can be sent and received even if you do not specify a messag
e key.
        msg.setKey("ORDERID_100");
        try {
            // The specified period of time, in milliseconds. After the specified
period of time elapses, the ApsaraMQ for RocketMQ 5.0 broker delivers the message to th e consumer. For example, you can set this parameter to 3, and the ApsaraMQ for RocketMQ 5.0 broker delivers the message to the consumer after 3 seconds. The value mus t be later than the current time.
            long delayTime = System.currentTimeMillis() + 3000;
            // The time when the ApsaraMQ for RocketMQ 5.0 broker starts to deliver the
message.
            msg.setStartDeliverTime(delayTime);
            SendResult sendResult = producer.send(msg);
            // Send the message in synchronous mode. If no exception occurs, the
message is sent.
            if (sendResult != null) {
            System.out.println(new Date() + " Send mq message success. Topic is:" +
msg.getTopic() + " msgId is: " + sendResult.getMessageId());
```

`}`

```java
            } catch (Exception e) {
            // Specify the logic to resend or persist the message if the message fails
to be sent.
            System.out.println(new Date() + " Send mq message failed. Topic is:" +
msg.getTopic());
            e.printStackTrace();
```

`}`

```
        // Before you exit the application, shut down the producer.<br>
        // Note: This step is optional.
        producer.shutdown();
```

`}` `}`

**Subscribe to delayed messages**

The method for subscribing to delayed messages is the same as that for subscribing to normal messages. For more information, see Subscribe to messages.

##### 5.2.4.10 Send and subscribe to scheduled messages

**messages**

This topic describes the scenarios of sending scheduled messages and provides sample code. Scheduled messages are consumed after a specified timestamp. Such messages are used in scenarios where a time window between message production and consumption is required or tasks need to be triggered at a scheduled time. For information about the terms and usage notes for using scheduled messages, see Scheduled and delayed messages.

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
        // The TCP endpoint. You can view the TCP endpoint on the Network Management ta
b of the instance details page in the ApsaraMQ for RocketMQ 5.0 console.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        Producer producer = ONSFactory.createProducer(properties);
        // Before you use the producer to send a message, call the start() method once
to start the producer.
        producer.start();
        Message msg = new Message( //
                // The topic of the message.
                "Topic",
                // The message tag, which is similar to a Gmail tag. It is used to sort
messages and help the consumer filter messages on the ApsaraMQ for RocketMQ 5.0 broker based on specified conditions.
                "tag",
                // The message body in the binary format. ApsaraMQ for RocketMQ 5.0
does not process the message body. The producer and consumer must agree on the serializ
```

```java
ation and deserialization methods.
                "Hello MQ".getBytes());
        // The key of the message. The key is the business-specific attribute of the me
ssage and must be globally unique whenever possible.
        // A unique key helps you query and resend a message in the console if the mess
age fails to be received.
        // Note: A message can be sent and received even if you do not specify a messag
e key.
        msg.setKey("ORDERID_100");
        try {
            // The time when the ApsaraMQ for RocketMQ 5.0 broker delivers the message
to the consumer, in milliseconds. For example, you can set this parameter to 2016-03-07 16:21:00, and the broker delivers the message at 16:21:00 on March 7, 2016. The value m ust be later than the current time. If the scheduled time is earlier than the current t ime, the message is immediately delivered to the consumer.
            long timeStamp = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").parse("2016-
03-07 16:21:00").getTime();
            msg.setStartDeliverTime(timeStamp);
            // Send the message. If no exception occurs, the message is sent.
            SendResult sendResult = producer.send(msg);
            System.out.println("Message Id:" + sendResult.getMessageId());
```

`}`

```java
        catch (Exception e) {
            // Specify the logic to resend or persist the message if the message fails
to be sent.
            System.out.println(new Date() + " Send mq message failed. Topic is:" +
msg.getTopic());
            e.printStackTrace();
```

`}`

```
        // Before you exit the application, shut down the producer.
        // Note: This step is optional.
        producer.shutdown();
```

`}` `}`

**Subscribe to scheduled messages**

The method for subscribing to scheduled messages is the same as that for subscribing to normal messages. For more information, see Subscribe to messages.

##### 5.2.4.11 Subscribe to messages

This topic describes how to subscribe to messages and provides sample code.

> **Note:** The subscriptions of all consumer instances identified by the same group ID must be consistent. For more information, see Subscription consistency.

**Subscription modes**

ApsaraMQ for RocketMQ 5.0 supports the following subscription modes:
**Clustering subscription**: All consumers identified by the same group ID consume an
equal number of messages. For example, a topic contains nine messages, and a consumer group contains three consumers. In clustering subscription mode, each consumer consumes three messages.

```
// Configure clustering subscription, which is the default mode.
 properties.put(PropertyKeyConst.MessageModel, PropertyValueConst.CLUSTERING);
```

**Broadcasting subscription**: Each of the consumers identified by the same group ID
consumes all messages once. For example, a topic contains nine messages, and a consumer group contains three consumers. In broadcasting subscription mode, each consumer consumes nine messages.

```
// Configure broadcasting subscription.
 properties.put(PropertyKeyConst.MessageModel, PropertyValueConst.BROADCASTING);
```

**Sample code**

```java
import com.aliyun.openservices.ons.api.Action; import com.aliyun.openservices.ons.api.ConsumeContext; import com.aliyun.openservices.ons.api.Consumer; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.MessageListener; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import java.util.Properties; public class ConsumerTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
        // The group ID that you created in the ApsaraMQ for RocketMQ 5.0 console.
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
        // The AccessKey ID that you created in the Apsara Uni-manager Management Conso
le for identity authentication.
        properties.put(PropertyKeyConst.AccessKey, "XXX");
        // The AccessKey secret that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
        properties.put(PropertyKeyConst.SecretKey, "XXX");
        // The TCP endpoint. You can view the TCP endpoint on the Network Management ta
b of the instance details page in the ApsaraMQ for RocketMQ 5.0 console.
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
          // Clustering subscription. This is the default mode.
          // properties.put(PropertyKeyConst.MessageModel,
PropertyValueConst.CLUSTERING);
          // Broadcasting subscription.
          // properties.put(PropertyKeyConst.MessageModel,
PropertyValueConst.BROADCASTING);
        Consumer consumer = ONSFactory.createConsumer(properties);
        consumer.subscribe("TopicTestMQ", "TagA||TagB", new MessageListener() { //
Subscribe to messages with multiple tags.
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
```

`}`

```java
        });
        // Subscribe to another topic.
        consumer.subscribe("TopicTestMQ-Other", "*", new MessageListener() {
//Subscribe to messages with all tags.
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
```

`}`

```java
        });
        consumer.start();
        System.out.println("Consumer Started");
```

`}` `}`

> **Note:** In broadcasting subscription mode, you cannot query message accumulation information in the ApsaraMQ for RocketMQ 5.0 console. You can create multiple group IDs to achieve the effect of broadcasting consumption. For more information, see Clustering consumption and broadcasting consumption.

#### 5.2.5 C/C++ SDK

##### 5.2.5.1 Prepare the SDK for C or C++ environment

###### 5.2.5.1.1 Overview

Before you use SDK for C or C++ to access ApsaraMQ for RocketMQ 5.0, make sure that the following preparations are made.

> **Note:** Create the topics and group IDs that are referred to in the code of the TCP client SDK for C or C++ in the ApsaraMQ for RocketMQ 5.0 console. You can specify custom message tags in your application. For information about how to create a message tag, see Create resources.
> Deploy applications that use ApsaraMQ for RocketMQ 5.0 on Elastic Compute Service (ECS) instances.

###### 5.2.5.1.2 Download SDK for C or C++

This topic describes the preparations, instructions, and usage notes for using SDK for C or C++ v2.0.0 to access ApsaraMQ for RocketMQ 5.0 so that you can use SDK for C or C++ to send and subscribe to messages.

**Procedure**

1. Download SDK for C or C++ used in Linux.
2. Decompress the downloaded package.
After the package is decompressed, the following directory structure appears: demos/ Contains examples on how to send normal messages, send messages in one-way mode, send ordered messages, consume normal messages, and consume ordered messages. This directory also contains the CMakeList.txt file that is used to compile and manage demos. include/ Contains header files that are required by your own programs. lib/ Contains dynamic libraries based on x86_64. The libraries include the interface library libonsclient4cpp.so and the kernel library librocketmq_client_core.so. changelog Contains bug fixes and new features in new releases.

###### 5.2.5.1.3 Use SDK for C++ in Linux

This topic describes how to use SDK for C++ in Linux. Starting from June 28, 2019, the SDK of the new version provides only dynamic library solutions. The library file of ApsaraMQ for RocketMQ 5.0 is stored in the lib/ directory. You must link librocketmq_client_core.so with libonsclient4cpp.so when you generate executable files. demos has introduced the features of C++ 11 and uses CMake for management. Therefore, you must install CMake 3.0 or later and g++ 4.8 or later in advance.

**Dynamic solution**

GCC 5.x or later has introduced Dual ABI. Therefore, you must add the **-**
**D_GLIBCXX_USE_CXX11_ABI=0** option when you compile the preceding links.
The following sample code provides an example on how to use demos:

```
cd aliyun-mq-linux-cpp-sdk // The path to which the downloaded SDK for C++ package is d ecompressed. cd demos // Go to the demos directory and modify the demos file by entering information such as the topic and key that you created in the ApsaraMQ for RocketMQ 5.0 console. cmake . // Detect dependencies and generate compilation scripts. make // Compile the code. cd bin // Run the program in the directory where the generated executable files are loc ated.
```

##### 5.2.5.2 Send and subscribe to normal messages

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
    // Create a producer and configure the parameters that are required to send message
```

`s.`

```
    ONSFactoryProperty factoryInfo;
    // The ID of the consumer group that you created in the ApsaraMQ for RocketMQ 5.0 c
onsole.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::ProducerId, "XXX");
    // The TCP endpoint. You can obtain the endpoint on the Network Management tab of t
he instance details page in the ApsaraMQ for RocketMQ 5.0 console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR, "XXX");
    // The topic that you created in the ApsaraMQ for RocketMQ 5.0 console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics,"XXX" );
    // The message content.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::MsgContent, "XXX");
//Mk thtth
```

`i` `t`

```
ibl ALIBABACLOUDACCESSKEYID dALIBABA
```

|   | // Make sure that the environment variables ALIBABA CLOUD ACCESS KEY ID and ALIBABA _ _ _ _ CLOUD ACCESS KEY SECRET are configured. _ _ _ _ // The AccessKey ID that is used for identity authentication. factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey, getenv("ALIBABA CLOUD ACCESS KEY ID")); _ _ _ _ // The AccessKey secret that is used for identity authentication. factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey, getenv("ALIBABA CLOUD ACCESS KEY SECRET")); _ _ _ _ //create producer; Producer *pProducer = ONSFactory::getInstance()->createProducer(factoryInfo); // Before you send a message, call the start() method only once to start the produc er. pProducer->start(); Message msg( // The topic to which the normal message belongs. A topic that is used to send and receive normal messages cannot be used to send or receive messages of other ty pes. factoryInfo.getPublishTopics(), // The message tag, which is similar to a Gmail tag. It is used to sort mess ages and help the consumer filter messages on the ApsaraMQ for RocketMQ 5.0 broker based on specified conditions. "TagA", // The message body. ApsaraMQ for RocketMQ 5.0 does not process the message body. The producer and consumer must agree on the serialization and deserialization met hods. You cannot leave this parameter empty. factoryInfo.getMessageContent() ); // The key of the message. The key is the business-specific attribute of the messag e and must be globally unique whenever possible. // A unique key helps you query and resend a message in the ApsaraMQ for RocketMQ 5 .0 console if the message fails to be received. // Note: A message can be sent and received even if you do not specify a message ke y. msg.setKey("ORDERID 100"); _ // Send the message. If no exception occurs, the message is sent. try { SendResultONS sendResult = pProducer->send(msg); } catch(ONSClientException & e) { // Specify the logic to handle exceptions. } // Before you exit the application, shut down the producer. Otherwise, issues such as memory leaks may occur. pProducer->shutdown(); return 0; } |   |
|---|---|---|

`}`

**Subscribe to normal messages**

For more information about how to subscribe to normal messages and about relevant sample code, see Subscribe to messages.

##### 5.2.5.3 Send and subscribe to ordered messages

This topic provides the sample code for sending and subscribing to ordered messages.

**Send ordered messages**

The following sample code provides an example on how to send ordered messages:

```
#include "ONSFactory.h"
#include "ONSClientException.h"
#include <iostream>
using namespace ons; int main()
```

`{`

```
    // The parameters that are required to create and use a producer.
    ONSFactoryProperty factoryInfo;
    factoryInfo.setFactoryProperty(ONSFactoryProperty::ProducerId, "XXX");// The ID of
the consumer group that you created in the ApsaraMQ for RocketMQ 5.0 console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR, "XXX"); // The TCP
endpoint. You can obtain the endpoint on the Network Management tab of the instance details page in the ApsaraMQ for RocketMQ 5.0 console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics,"XXX" );// The top
ic that you created in the ApsaraMQ for RocketMQ 5.0 console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::MsgContent, "XXX");// The messag
e content.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey, "XXX");// The AccessK
ey ID that you created in the Apsara Uni-manager Management Console for identity authen tication.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey, "XXX" );// The Access
Key secret that you created in the Apsara Uni-manager Management Console for identity a uthentication.
    // Create a producer.
    OrderProducer *pProducer = ONSFactory::getInstance()-
>createOrderProducer(factoryInfo);
    // Before you send a message, call the start() method only once to start the produc
er.
    pProducer->start();
    Message msg(
                //Message Topic
                factoryInfo.getPublishTopics(),
                // The message tag, which is similar to a Gmail tag. It is used to sort
messages and help the consumer filter messages on the ApsaraMQ for RocketMQ 5.0 broker based on specified conditions.
```

```
                "TagA",
                // The message body in the binary format. ApsaraMQ for RocketMQ 5.0
does not process the message body. The producer and consumer must agree on the serializ ation and deserialization methods.
                factoryInfo.getMessageContent()
```

);

```
    // The key of the message. The key is the business-specific attribute of the messag
e and must be globally unique whenever possible.
    // A unique key helps you query and resend a message in the ApsaraMQ for RocketMQ 5
.0 console if the message fails to be received.
    // Note: A message can be sent and received even if you do not specify a message ke
```

`y.`

```
    msg.setKey("ORDERID_100");
    // The key field that is used to distinguish partitions for ordered messages.
    std::string shardingKey = "abc";
    // Messages that have the same sharding key are sent in order.
    try
```

`{`

```
        // Send the message. If no exception occurs, the message is sent.
        SendResultONS sendResult = pProducer->send(msg, shardingKey);
    std::cout << "send success" << std::endl;
```

`}`

```
    catch(ONSClientException & e)
```

`{`

```
        // Specify the logic to handle exceptions.
```

`}`

```
    // Before you exit the application, shut down the producer. Otherwise, issues such
as memory leaks may occur.
    pProducer->shutdown();
    return 0;
```

`}`

**Subscribe to ordered messages**

The following sample code provides an example on how to subscribe to ordered messages:

```
#include "ONSFactory.h"
using namespace std; using namespace ons; // Create a consumer instance. // After the push consumer pulls the message, the push consumer calls the consumeMessag e function of the instance. class ONSCLIENT_API MyMsgListener : public MessageOrderListener
```

`{`

```
public:
    MyMsgListener()
```

`{` `}`

```
    virtual ~MyMsgListener()
```

`{` `}`

|   | virtual OrderAction consume(Message &message, ConsumeOrderContext &context) { // Consume messages based on your business requirements. return Success; //CONSUME SUCCESS; _ } }; int main(int argc, char* argv[]) { // The parameters that are required to create and use a consumer. ONSFactoryProperty factoryInfo; // The ID of the consumer group that you created in the ApsaraMQ for RocketMQ 5.0 c onsole. factoryInfo.setFactoryProperty(ONSFactoryProperty::ConsumerId, "XXX"); // The topic that you created in the ApsaraMQ for RocketMQ 5.0 console. factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics,"XXX" ); // Make sure that the environment variables ALIBABA CLOUD ACCESS KEY ID and ALIBABA _ _ _ _ CLOUD ACCESS KEY SECRET are configured. _ _ _ _ // The AccessKey ID that is used for identity authentication. factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey, getenv("ALIBABA CLOUD ACCESS KEY ID")); _ _ _ _ // The AccessKey secret that is used for identity authentication. factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey, getenv("ALIBABA CLOUD ACCESS KEY SECRET")); _ _ _ _ // The TCP endpoint. You can obtain the endpoint on the Network Management tab of t he instance details page in the ApsaraMQ for RocketMQ 5.0 console. factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV ADDR, "XXX"); _ // Create an order consumer. OrderConsumer* orderConsumer = ONSFactory::getInstance()- >createOrderConsumer(factoryInfo); MyMsgListener msglistener; // The message topic and tag to which the order consumer subscribes. orderConsumer->subscribe(factoryInfo.getPublishTopics(), "*",&msglistener ); // Register the instance to listen to messages. After the order consumer pulls the messages, the order consumer calls the consumeMessage function of the message listening class. // Start the order consumer. orderConsumer->start(); for(volatile int i = 0; i < 1000000000; ++i) { //wait } // Before you exit the application, shut down the order consumer. Otherwise, issues such as memory leaks may occur. orderConsumer->shutdown(); return 0; } |   |
|---|---|---|

`}`

##### 5.2.5.4 Send and subscribe to scheduled messages

**messages**

This topic provides the sample code for sending and subscribing to scheduled messages. Scheduled messages are consumed by consumers after a specified period of time. Such messages are used in scenarios where a time window between message production and consumption is required or tasks need to be triggered at a scheduled time. Scheduled messages are used in a similar way to delay queues.

**Send scheduled messages**

The following sample code provides an example on how to send scheduled messages:

```
#include "ONSFactory.h"
#include "ONSClientException.h"
#include <windows.h>
using namespace ons; int main()
```

`{`

```
    // Create a producer and configure the parameters that are required to send message
```

`s.`

```
    ONSFactoryProperty factoryInfo;
    // The ID of the consumer group that you created in the ApsaraMQ for RocketMQ 5.0 c
onsole.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::ProducerId, "XXX");
    // The TCP endpoint. You can obtain the endpoint on the Network Management tab of t
he instance details page in the ApsaraMQ for RocketMQ 5.0 console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR, "XXX");
    // The topic that you created in the ApsaraMQ for RocketMQ 5.0 console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics,"XXX" );
    // The message content.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::MsgContent, "XXX");
    // Make sure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA
_CLOUD_ACCESS_KEY_SECRET are configured.
    // The AccessKey ID that is used for identity authentication.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"));
  // The AccessKey secret that is used for identity authentication.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
    //create producer;
    Producer *pProducer = ONSFactory::getInstance()->createProducer(factoryInfo);
    // Before you send a message, call the start() method only once to start the produc
er.
    pProducer->start();
Messagemsg(
```

```
    Message msg(
            //Message Topic
            factoryInfo.getPublishTopics(),
            // The message tag, which is similar to a Gmail tag. It is used to sort mess
ages and help the consumer filter messages on the ApsaraMQ for RocketMQ 5.0 broker based on specified conditions.
            "TagA",
            // The message body. ApsaraMQ for RocketMQ 5.0 does not process the message
body. The producer and consumer must agree on the serialization and deserialization met hods. You cannot leave this parameter empty.
            factoryInfo.getMessageContent()
```

);

```
    // The key of the message. The key is the business-specific attribute of the messag
e and must be globally unique whenever possible.
    // A unique key helps you query and resend a message in the ApsaraMQ for RocketMQ 5
.0 console if the message fails to be received.
    // Note: A message can be sent and received even if you do not specify a message ke
```

`y.`

```
    msg.setKey("ORDERID_100");
    // The delay before the ApsaraMQ for RocketMQ 5.0 broker delivers messages to the c
onsumer. Unit: milliseconds. The message can be consumed only after the specified time. In this example, the message can be consumed 3 seconds later.
    long deliverTime = GetTickCount64() + 3000;
    msg.setStartDeliverTime(deliverTime);
    // Send the message. If no exception occurs, the message is sent.
    try
```

`{`

```
        SendResultONS sendResult = pProducer->send(msg);
```

`}`

```
    catch(ONSClientException & e)
```

`{`

```
        // Specify the logic to handle exceptions.
```

`}`

```
    // Before you exit the application, shut down the producer. Otherwise, issues such
as memory leaks may occur.
    pProducer->shutdown();
    return 0;
```

`}`

**Subscribe to scheduled messages**

For more information about how to subscribe to scheduled messages and about relevant sample code, see Subscribe to messages.

##### 5.2.5.5 Send and subscribe to transactional messages

**messages**

This topic describes the interaction process and the status check mechanism of transactional messages. This topic also shows you how to send and subscribe to transactional messages, and provides sample code.

**Interaction process**

The following figure shows the interaction process of transactional messages in ApsaraMQ for RocketMQ 5.0. Figure 1. Interaction process of transactional messages

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

`{` `}`

```
        ~MyLocalTransactionExecuter()
```

`{` `}`

```
        virtual TransactionStatus execute(Message &value)
```

`{`

```
                // The message ID. Two messages can have the same message body but no
t the same ID. You cannot query the ID of the current message in the ApsaraMQ for Roc ketMQ 5.0 console. )
                string msgId = value.getMsgID();
                // Calculate the message body by using an algorithm such as CRC32 and
MD5.
                // The message ID and CRC32 ID are used to prevent duplicate messages.
                // You do not need to specify the message ID or CRC32 ID if your busin
ess is idempotent. Otherwise, specify the message ID or CRC32 ID to ensure idempotency.
                // To prevent duplicate messages, we recommend that you calculate the
message body by using the CRC32 or MD5 algorithm.
                TransactionStatus transactionStatus = Unknow;
```

```
                try {
                    boolean isCommit = The execution result of the local transaction;
                    if (isCommit) {
                        // Commit the message if the local transaction is executed.
                        transactionStatus = CommitTransaction;
                    } else {
                        // Roll back the message if the local transaction fails to be
executed.
                        transactionStatus = RollbackTransaction;
```

`}`

```
                } catch (...) {
                    //exception handle
```

`}`

```
                return transactionStatus;
```

`}` `}`

```
    int main(int argc, char* argv[])
```

`{`

```
        // The parameters that are required to create a producer and send messages.
        ONSFactoryProperty factoryInfo;
        // The ID of the consumer group that you created in the ApsaraMQ for RocketMQ
5.0 console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty::ProducerId, "XXX");
        // The TCP endpoint. You can obtain the endpoint on the Network Management ta
b of the instance details page in the ApsaraMQ for RocketMQ 5.0 console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR, "XXX");
        // The topic that you created in the ApsaraMQ for RocketMQ 5.0 console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics,"XXX" );
        // The message content.
        factoryInfo.setFactoryProperty(ONSFactoryProperty::MsgContent, "XXX");
        // Make sure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and A
LIBABA_CLOUD_ACCESS_KEY_SECRET are configured.
        // The AccessKey ID that is used for identity authentication.
        factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"));
      // The AccessKey secret that is used for identity authentication.
        factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
        // Create a producer. ApsaraMQ for RocketMQ 5.0 does not release pChecker. Yo
u must release pChecker by yourself.
        MyLocalTransactionChecker *pChecker = new MyLocalTransactionChecker();
        g_producer = ONSFactory::getInstance()-
>createTransactionProducer(factoryInfo,pChecker);
        // Before you send a message, call the start() method only once to start the
producer.
        pProducer->start();
        Message msg(
            //Message Topic
            factoryInfo.getPublishTopics(),
            // The message tag, which is similar to a Gmail tag. It is used to sort me
dhl
```

`th`

```
filt
```

`th` `A`

```
MQf
```

`R`

```
ktMQ50b
```

`k`

```
ssages and help the consumer filter messages on the ApsaraMQ for RocketMQ 5.0 broker based on specified conditions.
            "TagA",
            // The message body. ApsaraMQ for RocketMQ 5.0 does not process the messa
ge body. The producer and consumer must agree on the serialization and deserializatio n methods. You cannot leave this parameter empty.
            factoryInfo.getMessageContent()
```

);

```
        // The key of the message. The key is the business-specific attribute of the
message and must be globally unique whenever possible.
        // A unique key helps you query and resend a message in the ApsaraMQ for Rock
etMQ 5.0 console if the message fails to be received.
        // Note: A message can be sent and received even if you do not specify a mess
age key.
        msg.setKey("ORDERID_100");
        // Send the message. If no exception occurs, the message is sent.
        try
```

`{`

```
            // ApsaraMQ for RocketMQ 5.0 does not release pExecuter. You must release
pExecuter by yourself.
            MyLocalTransactionExecuter pExecuter = new MyLocalTransactionExecuter();
            SendResultONS sendResult = pProducer->send(msg,pExecuter);
```

`}`

```
        catch(ONSClientException & e)
```

`{`

```
            // Specify the logic to handle exceptions.
```

`}`

```
        // Before you exit the application, shut down the producer. Otherwise, issues
such as memory leaks may occur.
        pProducer->shutdown();
        return 0;
```

`}`
2. Commit the transaction status of the message.
After the local transaction is executed, the ApsaraMQ for RocketMQ 5.0 broker must be notified of the transaction status of the current message, no matter whether the execution succeeds or fails. You can notify the ApsaraMQ for RocketMQ 5.0 broker by using one of the following methods: Commit the status after the local transaction is executed. Wait until the ApsaraMQ for RocketMQ 5.0 broker sends a request to check the transaction status of the message. A transaction can be in one of the following states:
**TransactionStatus.CommitTransaction**: The transaction is committed. The consumer
can consume the message.
**TransactionStatus.RollbackTransaction**: The transaction is rolled back. The message is
discarded and cannot be consumed.
**TransactionStatus.Unknow**: The transaction status is unknown. The ApsaraMQ for
RocketMQ 5.0 broker is expected to send a request again to the producer to query the status of the local transaction that corresponds to the message.

```
 class MyLocalTransactionChecker : LocalTransactionChecker
```

`{`

```
     MyLocalTransactionChecker()
```

`{` `}`

```
     ~MyLocalTransactionChecker()
```

`{` `}`

```
     virtual TransactionStatus check(Message &value)
```

`{`

```
         // The message ID. Two messages can have the same message body but not the sam
e ID. You cannot query the ID of the current message in the ApsaraMQ for RocketMQ 5.0 c onsole.
         string msgId = value.getMsgID();
         // Calculate the message body by using an algorithm such as CRC32 and MD5.
         // The message ID and CRC32 ID are used to prevent duplicate messages.
         // You do not need to specify the message ID or CRC32 ID if your business is i
dempotent. Otherwise, specify the message ID or CRC32 ID to ensure idempotency.
         // To prevent duplicate messages, we recommend that you calculate the message
body by using the CRC32 or MD5 algorithm.
         TransactionStatus transactionStatus = Unknow;
         try {
             boolean isCommit = The execution result of the local transaction;
             if (isCommit) {
                 // Commit the message if the local transaction succeeds.
                 transactionStatus = CommitTransaction;
             } else {
                 // Roll back the message if the local transaction fails.
                 transactionStatus = RollbackTransaction;
```

`}`

```
         } catch(...) {
             //exception error
```

`}`

```
         return transactionStatus;
```

`}` `}`

**Mechanism of transaction status check**

Why must the mechanism of transaction status check be implemented when transactional messages are sent? If the half message is sent in Step 1 but **TransactionStatus.Unknow** is returned for the local transaction, or no status is committed for the local transaction because the application exits, the status of the half message is unknown to the ApsaraMQ for RocketMQ 5.0 broker. Therefore, the ApsaraMQ for RocketMQ 5.0 broker periodically requests the producer to check and report the status of the half message. What does the business logic do when the check method is called back? The check method for transactional messages in ApsaraMQ for RocketMQ 5.0 must contain the logic of transaction consistency check. After a transactional message is sent, ApsaraMQ for RocketMQ 5.0 must call the **LocalTransactionChecker** operation to respond to the request of the ApsaraMQ for RocketMQ 5.0 broker for the status of the local transaction. Therefore, the check method for transactional messages must contain the following logic: i. Check whether the local transaction that corresponds to the half message is committed or rolled back. ii. Commit the status of the local transaction that corresponds to the half message to the ApsaraMQ for RocketMQ 5.0 broker. How do different states of the local transaction affect the half message?
**TransactionStatus.CommitTransaction**: The transaction is committed. The message
can be consumed by consumers.
**TransactionStatus.RollbackTransaction**: The transaction is rolled back. The message
is discarded and cannot be consumed.
**TransactionStatus.Unknow**: The transaction status is unknown. The ApsaraMQ for
RocketMQ 5.0 broker is expected to send a request again to the producer to query the status of the local transaction that corresponds to the message. For more information about the code, see the implementation of
**MyLocalTransactionChecker**.

**Subscribe to transactional messages**

For more information about how to subscribe to transactional messages and about relevant sample code, see Subscribe to messages.

##### 5.2.5.6 Subscribe to messages

This topic describes how to subscribe to messages by using the TCP client SDK for C or C++ provided by ApsaraMQ for RocketMQ 5.0.

> **Note:** The subscriptions of all consumer instances identified by the same group ID must be consistent. For more information, see Subscription consistency.

**Subscription modes**

ApsaraMQ for RocketMQ 5.0 supports the following subscription modes:
**Clustering subscription**:
This mode is used to implement clustering consumption. In this mode, all consumers identified by the same group ID consume an equal number of messages. For example, a topic contains nine messages, and a consumer group contains three consumers. In clustering subscription mode, each consumer consumes three messages.

```
// Configure clustering subscription, which is the default mode.
 factoryInfo.setFactoryProperty(ONSFactoryProperty:: MessageModel,
ONSFactoryProperty::CLUSTERING);
```

**Broadcasting subscription**:
This mode is used to implement broadcasting consumption. In this mode, each of the consumers identified by the same group ID consumes all messages once. For example, a topic contains nine messages, and a consumer group contains three consumers. In broadcasting subscription mode, each consumer consumes nine messages.

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
using namespace ons; std::mutex console_mtx; class ExampleMessageListener : public MessageListener { public:
    Action consume(Message& message, ConsumeContext& context) {
        // The consumer receives the message and attempts to consume it. After the mess
age is consumed, CommitMessage is returned.
        // If the consumer fails to consume the message or wants to consume the message
again, ReconsumeLater is returned. Then, the message is delivered to the consumer again after a predefined period of time.
        std::lock_guard<std::mutex> lk(console_mtx);
        std::cout << "Received a message. Topic: " << message.getTopic() << ", MsgId: "
        << message.getMsgID() << std::endl;
        return CommitMessage;
```

`}` };

```
int main(int argc, char* argv[]) {
    std::cout << "=======Before consuming messages=======" << std::endl;
    ONSFactoryProperty factoryInfo;
    // The ID of the consumer group that you created in the ApsaraMQ for RocketMQ 5.0 c
onsole. ApsaraMQ for RocketMQ 5.0 instances use group IDs instead of producer IDs and consumer IDs. This parameter is configured to ensure the compatibility with earlier ver sions.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::ConsumerId, "GID_XXX");
    // Make sure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA
_CLOUD_ACCESS_KEY_SECRET are configured.
    // The AccessKey ID that is used for identity authentication.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"));
  // The AccessKey secret that is used for identity authentication.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
    // The endpoint that is used to access the ApsaraMQ for RocketMQ 5.0 instance. You
can obtain the endpoint in the ApsaraMQ for RocketMQ 5.0 console.
    factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR,
"http://xxxxxxxxxxxxxxxx.aliyuncs.com:80");
    PushConsumer *consumer = ONSFactory::getInstance()-
>createPushConsumer(factoryInfo);
```

```
ceateusCosue(actoy o);
    // The topic that you created in the ApsaraMQ for RocketMQ 5.0 console.
    const char* topic_1 = "topic-1";
    // Subscribe to messages attached with tag-1 in topic-1.
    const char* tag_1 = "tag-1";
    const char* topic_2 = "topic-2";
    // Subscribe to all messages in topic-2.
    const char* tag_2 = "*";
    // Use a custom listener function to process the received messages and return the r
esults.
    ExampleMessageListener * message_listener = new ExampleMessageListener();
    consumer->subscribe(topic_1, tag_1, message_listener);
    consumer->subscribe(topic_2, tag_2, message_listener);
    // The preparation is complete. You must call the startup function to start the con
sumer.
    consumer->start();
    // Keep the thread running and do not shut down the consumer.
    std::this_thread::sleep_for(std::chrono::milliseconds(60 * 1000));
    consumer->shutdown();
    delete message_listener;
    std::cout << "=======After consuming messages======" << std::endl;
    return 0;
```

`}`

#### 5.2.6. .NET SDK

##### 5.2.6.1 Prepare the .NET SDK environment

###### 5.2.6.1.1 Overview

This topic describes how to prepare the environment for accessing ApsaraMQ for RocketMQ 5.0 by using SDK for .NET so that you can use SDK for .NET to send and subscribe to messages.

> **Note:** Create the topics and group IDs that are referred to in the code of SDK for .NET in the ApsaraMQ for RocketMQ 5.0 console. You can specify custom message tags in your application. For information about how to create a message tag, see Create resources.
> Deploy applications that use ApsaraMQ for RocketMQ 5.0 on Elastic Compute Service (ECS) instances.

###### 5.2.6.1.2 Download SDK for .NET

SDK for .NET provided by ApsaraMQ for RocketMQ 5.0 is a managed wrapper of SDK for C++ of ApsaraMQ for RocketMQ 5.0. This ensures that SDK for .NET is completely independent of the Windows .NET public library. C++ multithread concurrent processing is used internally to ensure the efficiency and stability of SDK for .NET.

**Background information**

When Visual Studio is used to develop .NET applications and class libraries, the default destination platform is AnyCPU. This means that the x86 or x64 platform can be automatically selected based on the CPU type. This capability is provided because the assembly compiled by using .NET is based on the intermediate language (IL). At runtime, the just in-time (JIT) compiler in the common language runtime (CLR) of .NET converts the IL code into the x86 or x64 machine code. The DLL generated by the C or C++ compiler is the machine code. Therefore, a destination platform is selected during compilation. The C or C++ project is compiled as an x64 64-bit DLL by configuring compilation options. Therefore, the 64-bit DLL in release mode compiled by using Visual Studio 2015 is provided. The 64-bit DLL in release mode is also available to other Visual Studio versions.

> **Note:** C++ DLL files require the installation package of the Virtual C++ 2015 runtime environment. If the Visual Studio 2015 runtime environment is not installed, run the vc_redist.x64.exe program provided in the SDK.

**Procedure**

1. Download the SDK package.
We recommend that both new users and existing users who are not concerned with upgrade costs download the latest SDK. Download link: Latest version of SDK for .NET used in Windows.
2. Decompress the downloaded package.
After the package is decompressed, the following directory structure appears: demo/ Contains examples on how to send normal messages, send messages in one-way mode, send ordered messages, consume normal messages, and consume ordered messages. lib/ Contains files related to the underlying C++ DLL and the installation package of the Virtual C++ 2015 runtime environment. If the Visual Studio 2015 runtime environment is not installed, copy and run the vc_redist.x64.exe file, as shown in the following information:

```
  64/
      NSClient4CPP.lib
      ONSClient4CPP.dll
      ONSClient4CPP.pdb
  vc_redist.x64.exe
```

interface/ Encapsulates P/Invoke code. The code must be included in the user project code. SDK_GUIDE.pdf Contains the documentation and frequently asked questions (FAQ) about how to prepare the SDK environment. changelog Contains bug fixes and new features in new releases.

###### 5.2.6.1.3 Configure SDK for .NET

This topic describes how to use SDK for .NET in Windows.

**Procedure**

Use SDK for .NET in the Visual Studio 2015 environment.
1. Use Visual Studio 2015 to create your project.
Figure 1. .NET SDK-1
2. Right-click the project and choose **Add** > **Add Existing Item** to add all files in the
**interface** directory of the downloaded SDK package.
Figure 2. .NET SDK-2
3. Right-click the project and choose **Properties** > **Configuration Manager**. Set **Active**
**solution configuration** to **Release** and set **Active solution platform** to **x64**.
4. Write and compile the test program, save the DLL file of the SDK to the directory of the
executable file or to the system directory, and then run the program. Figure 3. .NET SDK-3

> **Note:** The SDK provides a preconfigured demo project. You can open the project and compile it. When you run the project, copy the related DLL file to the directory of the executable file, as shown in the following figure.

Figure 4. .NET SDK-4

**Configure ASP.NET in Visual Studio 2015 to use ApsaraMQ for RocketMQ v5.0 SDK**

5. Create a **Web Forms** project for ASP.NET by using Visual Studio 2015.
Figure 5. .NET SDK-5
6. Right-click the project and choose **Properties** > **Configuration Manager**. Set **Active**
**solution configuration** to **Release** and set **Active solution platform** to **x64**.
Figure 6. .NET SDK-6
7. Right-click the project and choose **Add** > **Add Existing Item** to add all files in the
interface directory of the downloaded SDK package. For more information about how to configure a common .NET project, see Step 2.
8. Add the code for starting and stopping the SDK to the **Global.asax.cs** file.

> **Note:** We recommend that you encapsulate the SDK code as a singleton class so that the code cannot be recycled by the garbage collector due to scope problems. The example directory of the SDK contains the Example.cs file for implementing a simple singleton class. To use Example.cs, you must include it in your own project.

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
```

`}`

```
            catch (Exception ex)
```

`{`

```
                    // Specify the logic for handling exceptions.
```

`}` `}`

```java
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
```

`}`

```
            catch (Exception ex)
```

`{`

```
              // Specify the logic for handling exceptions.
```

`}` `}` `}` `}`
9. Write and compile the test program.
0. Save the DLL file of the SDK to the directory of the executable file or to the system directory
and run the program. Figure 7. .NET SDK-7
1. Choose **Tools** > **Options** > **Projects and Solutions** > **Web Projects**. Then, select the
**Use the 64 bit version of IIS Express for websites and projects** check box.
Figure 8. .NET SDK-8 Figure 9. .NET SDK-9

##### 5.2.6.2 Send and subscribe to normal messages

This topic provides the sample code for sending and subscribing to normal messages.

**Send normal messages**

The following sample code provides an example on how to send normal messages. You must follow the instructions to configure the parameters.

```java
using System; using ons; public class ProducerExampleForEx
```

`{`

```
    public ProducerExampleForEx()
```

`{` `}`

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
        // The group ID that you created in the ApsaraMQ for RocketMQ 5.0 console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.ProducerId, "GID_example");
```

```
        // The topic that you created in the ApsaraMQ for RocketMQ 5.0 console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.PublishTopics,
"T_example_topic_name");
        // The TCP endpoint. You can view the TCP endpoint on the Network Management ta
b of the instance details page in the ApsaraMQ for RocketMQ 5.0 console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.NAMESRV_ADDR,
"NameSrv_Addr");
        // Specify the log path.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.LogPath, "C://log");
        // Create a producer instance.
        // Note: Producer instances are thread-secure and can be used to send messages
of different topics.
        // Each thread requires only one producer instance.
        Producer producer = ONSFactory.getInstance().createProducer(factoryInfo);
        // Start the producer instance.
        producer.start();
        // Create a message.
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
```

`}`

```
            catch (Exception ex)
```

`{`

```
                Console.WriteLine("send failure{0}", ex.ToString());
```

`}` `}`

```
        // Before you exit your thread, shut down the producer instance.
        producer.shutdown();
```

`}` `}`

**Subscribe to messages**

For more information about how to subscribe to normal messages and about relevant sample code, see Subscribe to messages.

##### 5.2.6.3 Send and subscribe to ordered messages

This topic describes how to send and subscribe to ordered messages and provides sample code.

**Send ordered messages**

The following sample code provides an example on how to send ordered messages:

```java
using System; using ons; public class OrderProducerExampleForEx
```

`{`

```
    public OrderProducerExampleForEx()
```

`p` `p` `()` `{` `}`

```
    static void Main(string[] args) {
        // Configure your account. You can obtain the account information in the Apsara
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
        // The group ID that you created in the ApsaraMQ for RocketMQ v5.0 console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.ProducerId, "GID_example");
        // The topic that you created in the ApsaraMQ for RocketMQ v5.0 console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.PublishTopics,
"T_example_topic_name");
        // The TCP endpoint. You can view the TCP endpoint on the Network Management ta
b of the Instance details page in the ApsaraMQ for RocketMQ v5.0 console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.NAMESRV_ADDR,
"NameSrv_Addr");
        // Specify the log path.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.LogPath, "C://log");
        // Create a producer instance.
        // Note: Producer instances are thread-secure and can be used to send messages
of different topics. Each thread
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
```

`}`

```
            catch (Exception ex)
```

`{`

```
                Console.WriteLine("send failure{0}", ex.ToString());
```

`}` `}`

```
        // Before you exit your thread, shut down the producer instance.
        producer.shutdown();
```

`}` `}`

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

`{` `}`

```
        ~MyMsgOrderListener()
```

`{` `}`

```
        public override ons.OrderAction consume(Message value, ConsumeOrderContext cont
ext)
```

`{`

```
            Byte[] text = Encoding.Default.GetBytes(value.getBody());
            Console.WriteLine(Encoding.UTF8.GetString(text));
            return ons.OrderAction.Success;
```

`}` `}`

```
    class OrderConsumerExampleForEx
```

`{`

```
        static void Main(string[] args)
```

`{`

```
            // Configure your account. You can obtain the account information in the Ap
sara Uni-manager Management Console.
            ONSFactoryProperty factoryInfo = new ONSFactoryProperty();
            // The AccessKey ID that you created in the Apsara Uni-manager Management C
onsole for identity authentication.
            factoryInfo.setFactoryProperty(ONSFactoryProperty.AccessKey, "Your access
key");
            // The AccessKey secret that you created in the Apsara Uni-manager
Management Console for identity authentication.
            factoryInfo.setFactoryProperty(ONSFactoryProperty.SecretKey, "Your access
secret");
            // The group ID that you created in the ApsaraMQ for RocketMQ v5.0 console.
            factoryInfo.setFactoryProperty(ONSFactoryProperty.ConsumerId,
"GID_example");
            // The topic that you created in the ApsaraMQ for RocketMQ v5.0 console.
            factoryInfo.setFactoryProperty(ONSFactoryProperty.PublishTopics,
"T_example_topic_name");
            // The TCP endpoint. You can view the TCP endpoint on the Network
Management tab of the Instance details page in the ApsaraMQ for RocketMQ v5.0 console.
            factoryInfo.setFactoryProperty(ONSFactoryProperty.NAMESRV_ADDR,
"NameSrv_Addr");
            // Specify the log path.
            factoryInfo.setFactoryProperty(ONSFactoryProperty.LogPath, "C://log");
            // Create a consumer instance.
            OrderConsumer consumer =
```

```
ONSFactory.getInstance().createOrderConsumer(factoryInfo);
            // Subscribe to topics.
            consumer.subscribe(factoryInfo.getPublishTopics(), "*",new
MyMsgOrderListener());
            // Start the consumer instance.
            consumer.start();
            // Put the main thread to sleep for a period of time.
            Thread.Sleep(30000);
            // If the consumer instance is no longer used, shut down the consumer
instance.
            consumer.shutdown();
```

`}` `}` `}`

##### 5.2.6.4 Send and subscribe to scheduled messages

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
            // The parameters that are required to create and use a producer.
            ONSFactoryProperty factoryInfo = new ONSFactoryProperty();
            factoryInfo.setFactoryProperty(factoryInfo.ProducerId, "XXX ");// The ID of
the consumer group that you created in the ApsaraMQ for RocketMQ 5.0 console.
            factoryInfo.setFactoryProperty(factoryInfo.NAMESRV_ADDR, "XXX"); // The TCP
endpoint. You can view the TCP endpoint on the Network Management tab of the instance details page in the ApsaraMQ for RocketMQ 5.0 console.
            factoryInfo.setFactoryProperty(factoryInfo.PublishTopics, "XXX");// The
topic that you created in the ApsaraMQ for RocketMQ 5.0 console.
            factoryInfo.setFactoryProperty(factoryInfo.MsgContent, "XXX");// The
message content.
            factoryInfo.setFactoryProperty(factoryInfo.AccessKey, "XXX");// The
AccessKey ID that you created in the Apsara Uni-manager Management Console for identity athentication
```

```
authentication.
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
cketMQ 5.0 console if the message fails to be received.
            // Note: A message can be sent and received even if you do not specify a me
ssage key.
            msg.setKey("ORDERID_100");
            // The period of time after which the ApsaraMQ for RocketMQ 5.0 broker deli
vers the message to the consumer. Unit: milliseconds. The message can be consumed only after the specified period of time. In this example, the message can be consumed 3 seco nds later.
            long deliverTime = Current system time (ms) + 3000;
            msg.setStartDeliverTime(deliverTime);
            // Send the message. If no exception occurs, the message is sent.
            try
```

`{`

```
                SendResultONS sendResult = pProducer.send(msg);
```

`}`

```
            catch(ONSClientException e)
```

`{`

```
                // Specify the logic for handling failures.
```

`}`

```
            // Before you exit the application, shut down the producer. Otherwise,
issues such as memory leaks may occur.
            pProducer.shutdown();
```

`}` `}` `}`

**Subscribe to scheduled messages**

For more information about how to subscribe to scheduled messages and about relevant sample code, see Subscribe to messages.

##### 5.2.6.5 Send and subscribe to transactional messages

**messages**

This topic describes the interaction process and the status check mechanism of transactional messages. This topic also shows you how to send and subscribe to transactional messages, and provides sample code.

**Interaction process**

The following figure shows the interaction process of transactional messages in ApsaraMQ for RocketMQ 5.0. Figure 1. Interaction process of transactional messages

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

`{` `}`

```
     ~MyLocalTransactionExecuter()
```

`{` `}`

```
     public override TransactionStatus execute(Message value)
```

`{`

```
             Console.WriteLine("execute topic: {0}, tag:{1}, key:{2}, msgId:
{3},msgbody:{4}, userProperty:{5}",
             value.getTopic(), value.getTag(), value.getKey(), value.getMsgID(), value
.getBody(), value.getUserProperty("VincentNoUser"));
             // The ID of the message. Two messages may have the same message body bu
t cannot have the same ID. The current message ID cannot be queried in the console.
```

```
             string msgId = value.getMsgID();
             // Calculate the message body by using CRC32 or other algorithms, such as
MD5.
             // The message ID and CRC32 ID are used to prevent duplicate messages.
             // To prevent duplicate messages, we recommend that you calculate the
message body by using the CRC32 or MD5 algorithm.
             TransactionStatus transactionStatus = TransactionStatus.Unknow;
             try {
                 boolean isCommit = The execution result of the local transaction;
                 if (isCommit) {
                     // Commit the message if the local transaction succeeds.
                     transactionStatus = TransactionStatus.CommitTransaction;
                 } else {
                     // Roll back the message if the local transaction fails.
                     transactionStatus = TransactionStatus.RollbackTransaction;
```

`}`

```
             } catch (Exception e) {
                 //exception handle
```

`}`

```
             return transactionStatus;
```

`}` `}`

```
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
ndpoint. You can view the TCP endpoint on the Network Management tab of the instance details page in the ApsaraMQ for RocketMQ 5.0 console.
         factoryInfo.setFactoryProperty(factoryInfo.ProducerId, "");// The ID of the
consumer group that you created in the ApsaraMQ for RocketMQ 5.0 console.
         factoryInfo.setFactoryProperty(factoryInfo.PublishTopics, "");// The topic t
hat you created in the ApsaraMQ for RocketMQ 5.0 console.
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
         // Before you send a message, call the start() method only once to start the
producer. After the producer is started, messages can be concurrently sent in multipl e threads.
         pProducer.start();
             Message msg = new Message(
             //Message Topic
             factoryInfo.getPublishTopics(),
             //Message Tag
```

`"T` `A"`

```
             "TagA",
             //Message Body
             factoryInfo.getMessageContent()
```

);

```
         // The key of the message. The key is the business-specific attribute of the
message and must be globally unique whenever possible.
         // A unique key helps you query and resend a message in the console if the m
essage fails to be received.
         // Note: A message can be sent and received even if you do not specify a mes
sage key.
         msg.setKey("ORDERID_100");
         // Send the message. If no exception occurs, the message is sent.
         try
```

`{`

```
             LocalTransactionExecuter myExecuter = new MyLocalTransactionExecuter();
             SendResultONS sendResult = pProducer.send(msg, ref myExecuter);
```

`}`

```
         catch(ONSClientException e)
```

`{`

```
             Console.WriteLine("\nexception of sendmsg:{0}",e.what() );
```

`}`

```
         // Before you exit the application, shut down the producer. Otherwise, issue
s such as memory leaks may occur.
         // The producer cannot be started again after the producer is shut down.
         pProducer.shutdown();
```

`}` `}` `}`
2. Commit the transaction status of the message.
After the local transaction is executed, the ApsaraMQ for RocketMQ 5.0 broker must be notified of the transaction status of the current message, no matter whether the execution succeeds or fails. You can notify the ApsaraMQ for RocketMQ 5.0 broker by using one of the following methods: Commit the status after the local transaction is executed. Wait until the ApsaraMQ for RocketMQ 5.0 broker sends a request to check the transaction status of the message. A transaction can be in one of the following states:
**TransactionStatus.CommitTransaction**: The transaction is committed. The consumer
can consume the message.
**TransactionStatus.RollbackTransaction**: The transaction is rolled back. The message
is discarded and cannot be consumed.
**TransactionStatus.Unknow**: The transaction status is unknown. The ApsaraMQ for
RocketMQ 5.0 broker is expected to send a request again to the producer to query the status of the local transaction that corresponds to the message.

```java
    public class MyLocalTransactionChecker : LocalTransactionChecker
```

`{`

```
        public MyLocalTransactionChecker()
```

`{` `}`

```
        ~MyLocalTransactionChecker()
```

`{` `}`

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
ess is idempotent. Otherwise, specify the message ID or CRC32 ID to ensure idempotency.
                // To prevent duplicate messages, we recommend that you calculate the
message body by using the CRC32 or MD5 algorithm.
                TransactionStatus transactionStatus = TransactionStatus.Unknow;
                try {
                    boolean isCommit = The execution result of the local transaction;
                    if (isCommit) {
                        // Commit the message if the local transaction succeeds.
                        transactionStatus = TransactionStatus.CommitTransaction;
                    } else {
                        // Roll back the message if the local transaction fails.
                        transactionStatus = TransactionStatus.RollbackTransaction;
```

`}`

```
                } catch (Exception e) {
                    //exception handle
```

`}`

```
                return transactionStatus;
```

`}` `}`

**Mechanism of transaction status check**

Why must the mechanism of transaction status check be implemented when transactional messages are sent? If the half message is sent in Step 1 but **TransactionStatus.Unknow** is returned for the local transaction, or no status is committed for the local transaction because the application exits, the status of the half message is unknown to the ApsaraMQ for RocketMQ 5.0 broker. Therefore, the ApsaraMQ for RocketMQ 5.0 broker periodically requests the producer to check and report the status of the half message. What does the business logic do when the check method is called back? The check method for transactional messages in ApsaraMQ for RocketMQ 5.0 must contain the logic of transaction consistency check. After a transactional message is sent, ApsaraMQ for RocketMQ 5.0 must call the **LocalTransactionChecker** operation to respond to the request of the ApsaraMQ for RocketMQ 5.0 broker for the status of the local transaction. Therefore, the check method for transactional messages must contain the following logic: i. Check whether the local transaction that corresponds to the half message is committed or rolled back. ii. Commit the status of the local transaction that corresponds to the half message to the ApsaraMQ for RocketMQ 5.0 broker. How do different states of the local transaction affect the half message?
**TransactionStatus.CommitTransaction**: The transaction is committed. The consumer
can consume the message.
**TransactionStatus.RollbackTransaction**: The transaction is rolled back. The message
is discarded and cannot be consumed.
**TransactionStatus.Unknow**: The transaction status is unknown. The ApsaraMQ for
RocketMQ 5.0 broker is expected to send a request again to the producer to query the status of the local transaction that corresponds to the message. For more information about the code, see the implementation of
**MyLocalTransactionChecker**.

**Subscribe to transactional messages**

For more information about how to subscribe to transactional messages and about relevant sample code, see Subscribe to messages.

##### 5.2.6.6 Subscribe to messages

This topic describes how to subscribe to messages by using the TCP client SDK for .NET provided by ApsaraMQ for RocketMQ 5.0.

> **Note:** The subscriptions of all consumer instances identified by the same group ID must be consistent. For more information, see Subscription consistency.

**Subscription modes**

ApsaraMQ for RocketMQ 5.0 supports the following subscription modes:
**Clustering subscription**: All consumers identified by the same group ID consume an
equal number of messages. For example, a topic contains nine messages, and a consumer group contains three consumers. In clustering subscription mode, each consumer consumes three messages.

```
// Configure clustering subscription, which is the default mode.
 factoryInfo.setFactoryProperty(ONSFactoryProperty.MessageModel,
ONSFactoryProperty.CLUSTERING);
```

**Broadcasting subscription**: Each of the consumers identified by the same group ID
consumes all messages once. For example, a topic contains nine messages, and a consumer group contains three consumers. In broadcasting subscription mode, each consumer consumes nine messages.

```
// Configure broadcasting subscription.
 factoryInfo.setFactoryProperty(ONSFactoryProperty.MessageModel,
ONSFactoryProperty.BROADCASTING);
```

**Sample code**

```java
using System; using System.Threading; using System.Text; using ons; // The callback function to be executed when a message is pulled from the ApsaraMQ for RocketMQ 5.0 broker. public class MyMsgListener : MessageListener
```

`{`

```
    public MyMsgListener()
```

`{` `}`

```
    ~MyMsgListener()
```

`{` `}`

```
    public override ons.Action consume(Message value, ConsumeContext context)
```

`{`

```
        Byte[] text = Encoding.Default.GetBytes(value.getBody());
        Console.WriteLine(Encoding.UTF8.GetString(text));
        return ons.Action.CommitMessage;
```

`}` `}`

```java
public class ConsumerExampleForEx
```

`{`

```
    public ConsumerExampleForEx()
```

`{` `}`

```
    static void Main(string[] args) {
        // Configure your account. You can obtain the account information in the Apsara
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
        // The group ID that you created in the ApsaraMQ for RocketMQ 5.0 console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.ConsumerId, "GID_example");
        // The topic that you created in the ApsaraMQ for RocketMQ 5.0 console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.PublishTopics,
"T_example_topic_name");
        // The TCP endpoint. You can view the TCP endpoint on the Network Management ta
b of the instance details page in the ApsaraMQ for RocketMQ 5.0 console.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.NAMESRV_ADDR,
"NameSrv_Addr");
        // Specify the log path.
```

```
//Spec yte ogpat.
        factoryInfo.setFactoryProperty(ONSFactoryProperty.LogPath, "C://log");
        // The clustering subscription mode.
        // factoryInfo.setFactoryProperty(ONSFactoryProperty:: MessageModel,
ONSFactoryProperty.CLUSTERING);
        // The broadcasting subscription mode.
        // factoryInfo.setFactoryProperty(ONSFactoryProperty:: MessageModel,
ONSFactoryProperty.BROADCASTING);
        // Create a consumer instance.
        PushConsumer consumer =
ONSFactory.getInstance().createPushConsumer(factoryInfo);
        // Subscribe to topics.
        consumer.subscribe(factoryInfo.getPublishTopics(), "*", new MyMsgListener());
        // Start the producer instance.
        consumer.start();
        // This value is an example in the demo. In your production environment, you
must set a proper value to make sure that the process does not unexpectedly exit.
        Thread.Sleep(300000);
        // Shut down the consumer instance when the process is about to exit.
        consumer.shutdown();
```

`}` `}` practices

## 6 Best practices

### 6.1 Clustering consumption and broadcasting consumption

**broadcasting consumption**

This topic describes the terms, scenarios, and usage notes of clustering consumption and broadcasting consumption in ApsaraMQ for RocketMQ 5.0.

**Terms**

ApsaraMQ for RocketMQ 5.0 is a messaging system that is based on the publish-subscribe model. In ApsaraMQ for RocketMQ 5.0, a consumer subscribes to a topic to obtain and consume messages. In most cases, consumer applications use distributed systems and are deployed on multiple machines in a cluster. Therefore, ApsaraMQ for RocketMQ 5.0 defines the following terms:
**Cluster**: ApsaraMQ for RocketMQ 5.0 specifies that consumers identified by the same
group ID belong to the same cluster. These consumers must have the same consumption logic that also involves tags. These consumers can be considered logically as one consumption node.
**Clustering consumption**: In this mode, a message needs to be processed only by one
consumer in the cluster, as required by ApsaraMQ for RocketMQ 5.x.
**Broadcasting consumption**: In this mode, ApsaraMQ for RocketMQ 5.0 broadcasts each
message to all consumers registered in the cluster to ensure that the message is consumed by each consumer at least once.

**Scenarios**

**Clustering consumption mode:**

Figure 1. Clustering consumption mode

**Scenarios and usage notes:**

Consumers are deployed in a cluster, and each message needs to be processed only once. The consumption progress is recorded on the ApsaraMQ for RocketMQ 5.0 broker. Therefore, the reliability is high. In clustering consumption mode, each message is delivered to only one consumer in the cluster for processing. If a message needs to be processed by each consumer in the cluster, use the broadcasting consumption mode. In clustering consumption mode, it is not guaranteed that a failed message can be routed to the same consumer each time the message is redelivered. Therefore, no definitive assumptions can be made during message processing. practices

**Broadcasting consumption mode:**

Figure 2. Broadcasting consumption mode Scenarios and usage notes: Ordered messages are not supported in broadcasting consumption mode. Consumer offsets cannot be reset in broadcasting consumption mode. Each message needs to be processed by multiple consumers that are subject to the same logic. The consumption progress is recorded on the consumers. Duplicate messages are more likely to occur in broadcasting consumption mode than in clustering consumption mode. In broadcasting consumption mode, ApsaraMQ for RocketMQ 5.0 ensures that each message is consumed at least once by each consumer, but does not resend a message that fails to be consumed. Therefore, you need to pay attention to consumption failures. In broadcasting consumption mode, a consumer starts message consumption from the latest message each time the consumer is restarted. A consumer automatically skips the messages that are sent to the ApsaraMQ for RocketMQ 5.0 broker when the consumer is stopped. Proceed with caution when you use this mode. In broadcasting consumption mode, each message is repeatedly processed by a large number of consumers. We recommend that you use the clustering consumption mode whenever possible. Only Java clients support the broadcasting consumption mode. In broadcasting consumption mode, the ApsaraMQ for RocketMQ 5.0 broker does not record the consumption progress. In this mode, you cannot query accumulated messages, configure message accumulation alerts, or query subscriptions in the ApsaraMQ for RocketMQ 5.0 console.

**Use the clustering consumption mode to simulate the broadcasting consumption**

**mode**

If the broadcasting consumption mode is required for your business, you can create multiple group IDs to subscribe to the same topic. practices Figure 3. Use the clustering consumption mode to simulate the broadcasting consumption mode Scenarios and usage notes: Each message needs to be processed by multiple consumers, and the logic of the consumers can be the same or different. The consumption progress is recorded on the ApsaraMQ for RocketMQ 5.0 broker. Therefore, the reliability is higher than that in broadcasting consumption mode. For each group ID, one or more consumer instances can be deployed. When multiple consumer instances are deployed, these instances compose a cluster and work together to consume messages. Assume that three consumer instances C1, C2, and C3 are deployed for Group ID 1. These instances share the messages sent from the ApsaraMQ for RocketMQ 5.0 broker to Group ID 1. In addition, these instances must subscribe to the same topics and same tags.

### 6.2 Message filtering

This topic describes how ApsaraMQ for RocketMQ v5.0 consumers filter messages on the ApsaraMQ for RocketMQ v5.0 broker based on tags. A tag is used to classify messages in a topic in ApsaraMQ for RocketMQ v5.0 into different types. ApsaraMQ for RocketMQ v5.0 allows consumers to filter messages by using tags. This ensures that the consumers consume only messages that they are concerned with. The following figure shows an example in the e-commerce transaction scenario. In the process from placing an order to receiving the product by the customer, a series of messages, including order messages, payment messages, and logistics messages, are generated. These messages are sent to the Trade_Topic topic and subscribed to by different systems, such as the payment system, logistics system, analysis system for transaction success rate, and realtime computing system. Among these systems, the logistics system receives only logistics messages, and the real-time computing system receives all transaction-related messages, including the order messages, payment messages, and logistics messages. practices Figure 1. Message filtering

> **Note:** To classify messages, you can create multiple topics, or create multiple tags in the same topic. In most cases, messages in one topic are irrelevant to those in another topic. Tags are used to distinguish between relevant messages in the same topic. For example, you can create different tags in the same topic to distinguish between a set and its subsets or distinguish between processes in sequence.

**Examples**

Before you send messages, specify a tag for each message.

```
Message msg = new Message("MQ_TOPIC","TagA","Hello MQ".getBytes());
```

Consumption method 1 If a consumer needs to subscribe to messages of all types in a topic, use an asterisk (*) to represent all tags.

```java
consumer.subscribe("MQ_TOPIC", "*", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
```

`}`

```
});
```

practices Consumption method 2 If a consumer needs to subscribe to messages of a specific type in a topic, specify the corresponding tag.

```java
consumer.subscribe("MQ_TOPIC", "TagA", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
```

`}`

```
});
```

Consumption method 3 If a consumer needs to subscribe to messages of multiple types in a topic, separate the corresponding tags with two vertical bars (|).

```java
consumer.subscribe("MQ_TOPIC", "TagA||TagB", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
```

`}`

```
});
```

Consumption method 4 (error example) If a consumer subscribes to messages with specific tags in a topic multiple times, the tags in the last subscription prevail:

```java
// In the following error code, the consumer can receive only messages with TagB in MQ_TOPIC and cannot receive messages with TagA. consumer.subscribe("MQ_TOPIC", "TagA", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
```

`}`

```java
}); consumer.subscribe("MQ_TOPIC", "TagB", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
```

`}`

```
});
```

### 6.3 Subscription consistency

In ApsaraMQ for RocketMQ v5.0, a group ID represents a consumer instance group. For most distributed applications, multiple consumer instances are attached to the same group ID. Subscription consistency means that the processing logic of all consumer instances identified by the same group ID must be identical. If the subscriptions of the consumer instances are inconsistent, errors occur in the message consumption logic, and messages may be lost. Subscriptions in ApsaraMQ for RocketMQ v5.0 involve topics and tags. Therefore, all consumer instances identified by the same group ID must be consistent in the following two aspects to ensure subscription consistency: The topics to which the consumer instances subscribe must be the same. practices The tags of the topics to which the consumer instances subscribe must be the same.

**Examples of subscriptions**

Consistent subscriptions Multiple group IDs subscribe to multiple topics, and the subscriptions of different consumer instances identified by the same group ID are consistent, as shown in the following figure. Figure 1. Consistent subscriptions One group ID subscribes to multiple topics, but the subscriptions of different consumer instances identified by the group ID are inconsistent, as shown in the following figure. Figure 2. Inconsistent subscriptions

**Sample code of subscriptions**

Sample code of inconsistent subscriptions Example 1 In the following example, two consumer instances identified by the same group ID subscribe to different topics. Consumer instance 1-1: practices

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_1"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "*", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
```

`}`

```
});
```

Consumer instance 1-2:

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_1"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_B ", "*", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
```

`}`

```
});
```

Example 2 In the following example, two consumer instances identified by the same group ID subscribe to the same topic but subscribe to different numbers of tags of the topic. Consumer instance 2-1 has subscribed to TagA, whereas consumer instance 2-2 has not specified a tag. Consumer instance 2-1:

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_2"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "TagA", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
```

`}`

```
});
```

Consumer instance 2-2:

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_2"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "*", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
```

`}`

```
});
```

Example 3 In this example, the subscriptions are inconsistent due to the following reasons: practices Two consumer instances identified by the same group ID subscribe to different numbers of topics. Two consumer instances subscribe to the same topic but subscribe to different tags of the topic. Consumer instance 3-1:

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_3"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "TagA", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
```

`}`

```java
}); consumer.subscribe("jodie_test_B", "TagB", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
```

`}`

```
});
```

Consumer instance 3-2:

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_3"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "TagB", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
```

`}`

```
});
```

### 6.4 Consumption idempotence

After an ApsaraMQ for RocketMQ v5.0 consumer receives messages, the consumer needs to perform idempotent processing on these messages based on the unique business-specific keys of the messages.

**Necessity for consumption idempotence**

In Internet applications, duplicate messages may occur in ApsaraMQ for RocketMQ v5.0 especially if Internet connection is unstable. Duplicate messages may occur in the following two scenarios: A producer repeatedly sends a message to an ApsaraMQ for RocketMQ v5.0 broker. If a network disconnection occurs or the producer breaks down after a message is sent to and persisted in the ApsaraMQ for RocketMQ v5.0 broker, the broker fails to respond to the producer. If the producer realizes that the message failed to be sent and resends the message, the consumer subsequently receives two messages that have the same content and message ID. The ApsaraMQ for RocketMQ v5.0 broker repeatedly delivers a message to a consumer. practices A message is delivered to a consumer and is processed by the consumer. When the consumer sends a response to the ApsaraMQ for RocketMQ v5.0 broker, a transient network disconnection occurs. In this case, the ApsaraMQ for RocketMQ v5.0 broker does not know whether the message is consumed. To ensure that the message is consumed at least once, the broker delivers the message again after the network recovers. As a result, the consumer receives two messages that have the same content and the same message ID. Duplicate messages are generated when rebalancing is triggered in scenarios such as network jitter, broker restart, and consumer application restart. Traffic is rebalanced if the ApsaraMQ for RocketMQ v5.0 broker or consumer client is restarted or scaled. In this case, a consumer may receive duplicate messages.

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
```

`}`

```
});
```

### 6.5 Message routing

ApsaraMQ for RocketMQ v5.0 provides the message routing feature that can be used to synchronize message data across clusters. This ensures message consistency and integrity between clusters. This topic describes the concept, benefits, and configuration method of message routing. This topic also describes the scenarios to which the message routing feature is applicable.

**What is message routing?**

The message routing feature of ApsaraMQ for RocketMQ v5.0 is used to synchronize messages across clusters. You can configure routing rules to dynamically plan the synchronization path of messages. This way, the messages can be synchronized from the source node to the destination node based on filter conditions. This feature implements remote message synchronization across clusters within milliseconds and ensures data consistency and integrity across clusters. The following figure shows how message routing works in ApsaraMQ for RocketMQ v5.0. In the figure, one-way synchronization is performed based on topics to synchronize messages from a specific source topic in the source instance to a specific destination topic in the destination instance. practices

**Scenarios**

The message routing feature can be used in the following common scenarios:

**Data synchronization**

Taobao and Tmall serve users all over the world. If sellers in a country or region want to publish products, the products must be reviewed before they can be available for sale. However, the product review systems of Alibaba Cloud are central systems deployed only in the cities of China, such as Shanghai. In this scenario, messages from the regions outside China must be synchronized to the product review systems in China to achieve cross-region data synchronization.

**Data backup and disaster recovery**

practices For core trading systems, changes in the details and prices of various commodities need to be updated across all business systems in real time. Multi-region disaster recovery and backup solutions can be used to ensure high availability. This way, service continuity is ensured even if a region becomes unavailable due to issues such as the cut of optical fibers.

**Benefits**

**High performance**

The message routing feature provided by ApsaraMQ for RocketMQ v5.0 enables real-time message synchronization within milliseconds and supports millions of transactions per second (TPS).

**Low cost**

You do not need to purchase additional leased lines, perform upgrades, or modify application code to use the message routing feature. The message routing process does not affect applications.

**Ease of use**

The message routing feature supports GUI-based configurations. You can create and manage routing tasks in the ApsaraMQ for RocketMQ v5.0 console.

**Limits**

The message routing feature is applicable to instances that have a namespace. You can check whether an instance has a namespace on the **Basic Information** tab of the **Instance**
**details** page in the ApsaraMQ for RocketMQ v5.0 console.

**Configure message routing**

This section describes the procedure to configure the message routing feature for an ApsaraMQ for RocketMQ v5.0 instance. For more information, see Route messages from a cluster to another cluster.

**Step 1: Create message synchronization clouds**

Before you create a message routing task, you must specify the information about the cloud on which your ApsaraMQ for RocketMQ v5.0 cluster is deployed. The information includes the endpoint of the ApsaraMQ for RocketMQ v5.0 instance, the domain name, and the AccessKey ID and AccessKey secret of the Apsara Stack tenant account to which the cloud belongs. ApsaraMQ for RocketMQ v5.0 obtains the permissions that are required to access ApsaraMQ for RocketMQ v5.0 resources across clouds based on the cloud information that you specified. practices

**Step 2: Create a message routing task**

Specify the message source and the message destination, and configure relevant information. For example, specify filter conditions and set the start offset of message synchronization. ct usage issues

## 7 Product usage issues

### 7.1 FAQ

#### 7.1.1 Quick start

This topic answers common questions for new users of RocketMQ v5.0.

**Where does a new group ID start consuming messages?**

When a consumer group with a new group ID starts for the first time, it ignores all historical messages and begins consuming messages sent after startup. On subsequent startups, consumption resumes from the last saved consumer offset. If you need to start consumption from a specific point in time, you can reset the consumer offset. Use the RocketMQ v5.0 console to specify a start time for a specific topic and group ID. This reset does not affect any other group ID. RocketMQ v5.0**: How are messages retried after a consumption failure?**

**Cluster consumption mode**

If your consumer logic returns Action.ReconsumerLater, NULL, or throws an exception, the system automatically retries the message up to 16 times. If consumption still fails after 16 attempts, the message is discarded. The interval between each retry attempt increases over time, as shown below:

| Retry attempt | Retry interval |
|---|---|
| 1 | 10 seconds |
| 2 | 30 seconds |
| 3 | 1 minute |
| 4 | 2 minutes |
| 5 | 3 minutes |
| 6 | 4 minutes |
| 7 | 5 minutes |
| 8 | 6 minutes |
| 9 | 7 minutes |

ct usage issues

| 10 | 8 minutes |
|---|---|
| 11 | 9 minutes |
| 12 | 10 minutes |
| 13 | 20 minutes |
| 14 | 30 minutes |
| 15 | 1 hour |
| 16 | 2 hours |

You can call the message.getReconsumeTimes() method to get the number of retries for a message.

**Broadcast consumption mode**

The broadcast consumption mode guarantees at-least-once delivery. However, unlike the cluster consumption mode, it does not retry messages after a consumption failure.

**What happens if a sent message is not received?**

RocketMQ v5.0 provides several ways to perform a message query: Query all messages received by a specific topic within a specified time range. Query for a message by its topic and message ID. Query for a group of messages on a specific topic that share the same message key. These methods let you inspect message content and consumption status. To trace a message's entire journey from the producer to the consumer, including timestamps at each step, use the message trace feature in RocketMQ v5.0. For instructions, see Query a message trace. RocketMQ v5.0**: Are messages guaranteed not to be duplicated?** In most scenarios, messages are delivered without duplication. However, as a distributed messaging middleware, RocketMQ v5.0 cannot guarantee unique message delivery in exceptional circumstances such as network jitter or application timeouts. Although duplicate messages are possible, the system guarantees that no messages are lost.

#### 7.1.2 Configuration

This topic answers frequently asked questions about configuring RocketMQ v5.0.

**How long are messages stored on the server?**

The server stores messages for up to 3 days. After this period, it deletes any unconsumed messages.

**What is the maximum body size for a message?**

The maximum message size depends on the message type. The limits are as follows: ct usage issues Normal messages and ordered messages: 4 MB. Transactional messages and scheduled/delayed messages: 64 KB.

**How do I set the consumer thread count in the client?**

Set the ConsumeThreadNums property when you start the consumer. See the following example:

```
    public static void main(String[] args) {
        Properties properties = new Properties();
        properties.put(PropertyKeyConst.GROUP_ID, "GID_001");
        properties.put(PropertyKeyConst.AccessKey, "xxxxxxxxxxxx");
        properties.put(PropertyKeyConst.SecretKey, "xxxxxxxxxxxx");
        /**
         * Set the consumer thread count to 20.
```

`*/`

```java
        properties.put(PropertyKeyConst.ConsumeThreadNums,20);
        Consumer consumer =ONSFactory.createConsumer(properties);
        consumer.subscribe("TestTopic", "*", new MessageListener() {
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
```

`}`

```java
        });
        consumer.start();
        System.out.println("Consumer Started");
```

`}`

**How do I troubleshoot DLL load failures or other runtime errors caused by**

**configuration issues in the .NET client?**

For details, see the SDK_GUIDE.pdf file included with the .NET SDK. Ensure your project is configured as described in the guide.

#### 7.1.3 Message trace

This topic answers frequently asked questions about the RocketMQ v5.0 message trace feature.

**Why can't I find any message trace data?**

If your query returns no message trace data, check the following: Message trace is available only for Java clients, version 1.2.2 or later. Verify that your query conditions are correct. Ensure you have entered the correct Topic, Message ID, and Message Key. Verify that the time range is correct. To improve query speed, you must specify the time range in which the message was sent. If no results are returned, expand the time range and try again. If you still cannot find any results after you have verified the preceding information, contact technical support and attach the log file located at /home/{user}/logs/ons.log. If you have confirmed that the information above is correct but still cannot find any results, submit a ticket for technical support and attach the log file from /home/{user}/logs/ons.log.

**I am certain a message was consumed, but the trace shows no consumption, and**

**the client IP and Group ID are incorrect. Why?**

ct usage issues This issue occurs if your client version does not support the message trace feature. As a result, the RocketMQ v5.0 trace query backend can retrieve only incomplete data, which results in an incorrect display. Upgrade your client as soon as possible to resolve this issue. For more information, see Query the trace of a message.

**Why is my Group ID not in the consumer list?**

This can occur if the message has a large number of downstream subscribers, as the trace diagram has limited display space. To view the complete list, use the scroll bar.

**Why can I no longer see my previous query tasks?**

To prevent display clutter, RocketMQ v5.0 periodically clears your historical query tasks. By default, only query tasks from the last 7 days are retained. If you cannot find a historical task, run the query again.

#### 7.1.4 Alarm handling

Alarm handling for RocketMQ v5.0 is currently unavailable. Because Apsara Stack operates in an isolated environment and cannot connect to public network interfaces, such as an SMS gateway, the monitoring and alarms module is unavailable in the console.

#### 7.1.5 Ordered messages

This topic answers common questions about ordered messages in RocketMQ v5.0.

**Do ordered messages support cluster consumption and broadcast consumption?**

Ordered messages support cluster consumption but not broadcast consumption.

**Can a single message be an ordered message, a scheduled message, and a**

**transactional message at the same time?**

No. Ordered, scheduled, and transactional messages are mutually exclusive message types.

**What is the scope of ordering for ordered messages?**

Ordered messages maintain their sequence within a single topic.

**Which sending method do ordered messages support?**

Ordered messages support only reliable synchronous sending.

### 7.2 Exception types

#### 7.2.1 Usage exceptions

This article describes exceptions you might encounter when using RocketMQ v5.0.

**Failed to start a producer or consumer due to a duplicate group ID.**

Cause: This issue occurs if you configure multiple producer or consumer instances with the same group ID within a single JVM. This prevents the client from starting. Solution: Follow these steps: i. For each group ID, start no more than one producer and one consumer instance within a single JVM process. ct usage issues ii. Restart the application.

**A consumer fails to start and load a JSON file in broadcasting mode.**

Cause: An outdated Fastjson version causes the broadcast consumer to fail to load the local offsets.json file. As a result, the consumer fails to start. Solution: Upgrade Fastjson to the version required by the ons-client to ensure that the local offsets.json file can be loaded correctly. By default, the offsets.json file is located in the /home/{user}/.rocketmq_offsets/ directory.

**Failed to retrieve the queue list when subscribing to a topic.**

Cause: This issue occurs if the topic does not exist in the console. Consequently, the consumer cannot retrieve queue information for the topic at startup. Solution: Follow these steps: i. Log in to the RocketMQ v5.0 console. ii. In the left-side navigation pane, click **instance list**. iii. On the **instance list** page, find the target instance by name, and then click its instance ID or **details** in the **actions** column to open the **instance details** page. iv. Select the **Topic Management > Create Topic**. Follow the prompts to create a topic. v. Click the **Group Management** tab, and then click **Create Group ID**. Follow the prompts to create a group ID. vi. Restart the application.

**Failed to send a message.**

Attempts to send a message fail repeatedly. Causes: The RocketMQ v5.0 broker returns an error code to the producer. For details, check the corresponding nested exception. If a RocketMQ v5.0 broker crashes, the producer might not immediately discover the updated list of brokers, causing temporary send failures. The producer times out when sending a message. This is typically caused by high server load or an unstable network connection. Solution: Follow these steps: i. This error is often temporary. It can occur if a RocketMQ v5.0 broker is restarting for maintenance or during transient timeouts caused by high server load. Wait a few moments and try again. ii. If the issue persists, contact technical support.

**Troubleshooting unlisted exceptions.**

Problem description: The exception you encountered is not listed in this document. Solution: Contact technical support for assistance. ct usage issues

**A message is marked as consumed but is not processed by the consumer.**

The message is marked as consumed, but your application logs indicate that the message was not received. This issue is typically caused by one of the following three reasons: Your application code does not immediately log the message after receiving it. If the application proceeds directly to business logic after receiving a message, an error or unhandled condition could prevent the message details from being logged. This creates the false impression that the message was never received. We recommend that you log message details, such as the message ID, timestamp, and reconsume times, immediately upon receipt. Multiple consumer instances are deployed. This is common during debugging when a consumer application is restarted multiple times. If old processes are not terminated correctly, multiple consumer processes can run simultaneously, causing them to enter cluster consumption mode. In this mode, multiple instances share the load of consuming messages. The message you thought was missing was likely processed by another consumer instance. In the RocketMQ v5.0 console, navigate to **Group Management > Consumer Status >**
**Connection Information** to view the deployment details of your consumer instances,
such as the number of instances and their IP addresses. An uncaught exception occurs during message consumption, causing the message to be redelivered.

```java
public class MessageListenerImpl implements MessageListener {
    @Override
    public Action consume(Message message, ConsumeContext context) {
        // If the message processing logic throws an exception, the message will be
retried.
        doConsumeMessage(message);
        // If an uncaught exception occurs in the doConsumeMessage() method, this l
og entry will not be printed.
        log.info("Receive Message, messageId:", message.getMsgID());
        return Action.CommitMessage;
```

`}` `}` If the issue persists, contact technical support with your local SDK logs for assistance.

#### 7.2.2 Resource not found

This topic describes how to troubleshoot "resource not found" errors.

**The group ID does not exist**

Possible causes: The group ID was not created in the console. As a result, when you use this group ID to connect to a RocketMQ v5.0 broker, server-side validation fails. Recommended solution: Follow these steps: i. Log in to the RocketMQ v5.0 console. ii. In the left-side navigation pane, click **instance list**. ct usage issues iii. On the **instance list** page, find the target instance by name, and then click its instance ID or **details** in the **actions** column to open the **instance details** page. iv. On the **instance details** page, click **group management**. If the group ID already exists, proceed to the next step. If the group ID does not exist, create it. v. Restart the application.

**Hostname not found**

Possible causes: This error can occur if the system fails to retrieve the hostname or host IP address. To verify, run the **hostname** command. If the command does not return a valid output, this is the cause of the error. If the command runs successfully but the error persists, another cause exists; contact technical support. Recommended solution: Follow these steps: i. On the affected machine, run the command to check the hostname.

```
[root@iZ231wxgt6mZ ~]# hostname iZ231wxgt6mZ
```

If the command fails, check whether you have defined an alias for hostname in a file such as `.bash_profile` or `.bashrc` (for example, `alias xxx='hostname'` ). Also, ensure that the command's path is in the $PATH environment variable. ii. Ping the hostname.

```
[root@iZ231wxgt6mZ ~]# ping iZ231wxgt6mZ
```

If you cannot ping the hostname, you must bind the local host IP address to the hostname in the /etc/hosts file. By default, ECS machines have this binding. Do not manually remove it. iii. Verify the system configuration. Verify that the hostname in /etc/sysconfig/network matches the hostname bound in /etc/hosts. If they do not match, update the configuration. If you modify the /etc/sysconfig/network file, you must restart the machine for the changes to take effect. We recommend that you do not arbitrarily modify system files, as doing so can cause unexpected issues. After completing these steps, the client should no longer report an `UnknownHostException` error at startup.

#### 7.2.3 Inconsistent state

This topic describes exceptions related to an inconsistent state.

**Invalid message**

**Possible causes:**

This issue typically occurs when message properties or the message body are invalid. A message is considered invalid if: The message is null. The message body is null. ct usage issues The message body has a length of 0. The message body exceeds the size limit.

**Recommended solution:**

Ensure your message does not have any of the invalid properties listed above. Use the details in the exception message to resolve the issue.

**Invalid parameter**

**Possible causes:**

The following table describes common invalid parameter errors.

| Nested exception | Description |
|---|---|
| consumeThreadMin Out of range [1, 1000] | The number of consumer threads is outside the valid range. |
| consumeThreadMax Out of range [1, 1000] | The number of consumer threads is outside the valid range. |
| messageListener is null | The messageListener is not set. |
| consumerGroup is null | The group ID is not set. |

**Recommended solution:**

Follow these steps: i. Use the exception message to identify and correct the invalid parameter in your client configuration. ii. Restart the application.

**Abnormal client state**

**Possible causes:**

You did not call the start() method after creating the consumer or producer. The client failed to start because an exception occurred during the start() process. You called the shutdown() method after the client started.

**Recommended solution:**

Follow these steps: i. Ensure you call the start() method after creating the consumer or producer to keep the client running. ii. Check the ons.log file for any exceptions that occurred during client startup.

**Inconsistent subscription**

**Problem description:**

This issue occurs when consumers in the same group ID, running on different JVMs, subscribe to different topics or use different tags for the same topic. This configuration results in an inconsistent subscription and causes unexpected message delivery.

**Incorrect code examples:**

ct usage issues Example 1: Consumers in the same group ID (GID-MQ-FAQ) subscribe to different topics (MQ-FAQ-TOPIC-1 and MQ-FAQ-TOPIC-2).

**Code on JVM-1:**

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
```

`}`

```
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
```

`}`

```
    });
    consumer.start();
```

ct usage issues Example 2: Consumers in the same group ID (GID-MQ-FAQ) subscribe to the same topic but use different tags (NM-MQ-FAQ-1 and NM-MQ-FAQ-2).

**Code on JVM-1:**

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ-1", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
```

`}`

```
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
```

`}`

```
    });
    consumer.start();
```

**Recommended solution:**

When you launch multiple consumers with the same group ID in different JVMs, ensure that their topic and tag configurations are identical.

### 7.3 Troubleshooting

#### 7.3.1 Unexpected client connections

This topic describes the symptoms, analysis, recovery, and verification steps for unexpected client connection issues.

**Symptoms**

You observe that some messages are not received by consumers after being sent. When you check the message trace in the RocketMQ v5.0 console by navigating to **Message**
**Trace > Create Query Task > Query by Message ID**, you find that some messages
have been sent to the broker but not delivered to any downstream consumers. In the RocketMQ v5.0 console, you navigate to **Group Management > Consumer Status**
**> Connection Information**. You find unexpected client IP addresses and notice that a
message backlog is forming exclusively on these clients.

**Analysis**

ct usage issues
**Analysis method**: In the RocketMQ v5.0 console, select **Group Management > Consumer**
**Status > Connection Information**. The page displays the connection status of all clients
under the GID. You can use this information to locate the IP addresses and process IDs of unexpected clients. You must confirm that the configuration loaded by the corresponding process is correct, including the AK, SK, Topic, and GID. Otherwise, this can lead to an issue where the client process occupies some queues but cannot consume messages correctly.
**Cause**: This issue occurs when a client for the GID is started in the same environment with an
incorrect configuration, such as a wrong AK, SK, or Topic. This misconfigured client process occupies some of the Topic's queues but cannot consume messages correctly. As a result, a message backlog forms on the server, and messages cannot be delivered in real time to the correct downstream consumers.
**How to confirm**: First, use the connection status to locate the problematic process. Then,
check the client's application code and its log file at `/{user.home}/logs/ons.log` to verify the configured AK, SK, Topic, and other information.
**Recovery method**: (Quick recovery) You can first shut down the problematic client
process. The accumulated messages are then immediately rebalanced and delivered to healthy clients. After you locate and fix the issue, restart the problematic process.

**Verification**

In the RocketMQ v5.0 console, on the **Group Management > Consumer Status >**
**Connection Information** page, all connected clients are within the expected range and can
consume messages normally. The **Subscription Consistency** column also shows **Yes**.

#### 7.3.2 Inconsistent subscriptions

This topic describes the symptoms, analysis, solution, and verification of inconsistent subscriptions.

**Symptoms**

You notice that consumers for a specific `Group ID` fail to receive some messages. You log on to the RocketMQ v5.0 console and navigate to **Message Query > Query Messages by**
**Message ID**. The console shows that a message has been consumed at least once, but
your application never processed it. In the RocketMQ v5.0 console, you navigate to **Group Management > Consumer Status**. The **Consistent Subscriptions** column displays **No**.

**Analysis**

In RocketMQ v5.0, a `Group ID` identifies a group of consumer instances. In most distributed

| Group ID |   | . Co |
|---|---|---|
| me |   |   |

applications, multiple consumer instances run under the same `Group ID` . Consistent subscriptions require that all consumer instances within the same `Group ID` subscribe to the exact same topics and tags. If consumer instances within the same `Group ID` are configured with different topics, or with the same topic but different tags, their subscriptions become inconsistent. This inconsistency disrupts the message consumption logic and can lead to message loss.
**Cause 1:** Clients configured with the same `Group ID` subscribe to different topics.

| same | Group ID |   |
|---|---|---|
| MQ-FAQ-TOPIC-2 |   |   |
|   |   | ) |

**Incorrect example:** Consumer instances under the same `Group ID` ( `GID-MQ-FAQ` )
subscribe to different topics ( `MQ-FAQ-TOPIC-1` and `MQ-FAQ-TOPIC-2` ).

**Code on JVM-1:**

ct usage issues

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
```

`}`

```
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
```

`}`

```
    });
    consumer.start();
```

**Cause 2:** Different clients under the same `Group ID` subscribe to the same topic but use
different tags.

| Group ID ferent tags ( | ( GID-MQ-FAQ NM-MQ-FAQ-1 | GID-MQ-FAQ |
|---|---|---|

**Incorrect example:** Consumer instances under the same `Group ID` ( `GID-MQ-FAQ` )
subscribe to the same topic ( `MQ-FAQ-TOPIC-1` ) but use different tags ( `NM-MQ-FAQ-1` and `NM-MQ-FAQ-2` ).

**Code on JVM-1:**

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ-1", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
```

`}`

```
    });
    consumer.start();
```

**Code on JVM-2:**

ct usage issues

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ-2", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
```

`}`

```
    });
    consumer.start();
```

**Solution**

Follow these steps to resolve the issue:
1. Check the subscription code for all your clients. Ensure that all clients using the same
`Group ID` subscribe to the exact same topic and tag.
2. Restart all client applications.

**Verification**

Your consumers receive all expected messages. Log on to the RocketMQ v5.0 console and navigate to **Group Management > Consumer**
**Status**. The **Consistent Subscriptions** column now displays **Yes**.

#### 7.3.3 Message accumulation in a Java process

**process**

**Symptoms**

On the **Consumer Status** page of the RocketMQ v5.0 console, **real-time message**
**accumulation** for a Group ID is higher than expected, and performance is significantly
degraded.

**Cause**

Excessive message accumulation in the Java process causes this issue.

**Procedure**

1. Log in to the RocketMQ v5.0 console.
2. Retrieve the IP address of the host for the consumer instance with message accumulation
by checking the consumer status, and then log on to the host or container.
3. Run any of the following commands to view and record the PID of the Java process.

```
ps -ef |grep java jps -lm
```

4. Run the following command to view the stack trace.

```
jstack -l pid > /tmp/pid.jstack
```

ct usage issues
5. Run the following command to view the `ConsumeMessageThread` information, and focus on
the state and stack of the thread.

```
cat /tmp/pid.jstack|grep ConsumeMessageThread -A 10 --color
```

The output is similar to the following figure. See the official Java documentation for an explanation of thread states.

| Note RocketMQ v5.0 can handle billions of accumulated messages without significant performance degradation. If performance remains degraded after you follow the steps above, contact technical support and provide the following information: Generate the heap.bin file by running the jmap -dump:format=b,file=heap.bin [$PID] command. Then, create a compressed package by running the gzip heap.bin command. [$PID] is the PID of the Java process that you recorded in Step 2. The consumer client experiencing message accumulation: ons.log local logs. The version of the consumer client. |   |   |   |
|---|---|---|---|
|   | jmap -dump:format=b,file=heap.bin |   |   |
|   |   | gzip |   |

#### 7.3.4 OOM error from client-side message caching

**caching**

This topic describes how to troubleshoot an application Out of Memory (OOM) error, covering its symptoms, causes, resolution, and verification.

**Symptoms**

The machine hosting the application runs out of memory. Symptom 2: The `/{user.home}/logs/ons.log` file contains the keyword "OutOfMemory". Symptom 3: In the RocketMQ v5.0 console, after you navigate to **Group Management >**
**Consumer Status**, the **Real-time Message Backlog** column shows a large message
backlog, and the Connection Status column shows the message backlog for each connected client. However, a Jstack diagnosis of the `ConsumeMessageThread_` thread shows that consumption is not stuck.

**Analysis**

ct usage issues
**Analysis**: RocketMQ v5.0 consumers pull messages from a broker and cache them on the
client before delivering them to your business logic. In versions earlier than 1.7.0.Final, a client caches a maximum of 1,000 messages for each queue of a topic by default. For example, assume a topic has 16 queues (in a cluster of two master and two replica brokers, with 8 queues on each broker) and the average message size is 64 KB. In this scenario, the total size of cached messages for this topic on the client is: 16 × 1,000 × 64 KB = 1 GB. If you subscribe to eight such topics, the total memory consumption from cached messages can exceed your JVM configuration and cause an OutOfMemory (OOM) error.
**Cause 1:** Your application uses a version of `ons-client` earlier than 1.7.0.Final, the
average message size exceeds 4 KB, and message consumption is slow. This leads to messages accumulating in the client-side cache.
**How to confirm**: You can search for the "OutOfMemory" keyword in

```
 /{user.home}/logs/ons.log  , or use the  jmap -dump:live,format=b,file=heap.bin <pid>
```

command to determine which objects are consuming a large amount of memory.
**Resolution**: Upgrade the ons-client version to 1.7.0.Final or later and set the

```
 com.aliyun.openservices.ons.api.PropertyKeyConst#MaxCachedMess ageSizeInMiB
```

parameter on the corresponding ConsumerBean. Then, restart the application. Cause 2: For ons-client versions 1.7.0.Final and later, the default maximum memory consumption is 512 MB (the total cache size for all topics subscribed to by a GID). If your application still experiences an OutOfMemory (OOM) error, you can customize the maximum memory consumption by configuring the

```
 com.aliyun.openservices.ons.api.PropertyKeyConst#MaxCachedMessageSizeInMiB  parameter
```

when the ConsumerBean starts. The valid range for this parameter is 16 MB to 2048 MB.
**Verification method**: Verify the version of ons-client that the application depends on,
and use the JVM to verify the memory size allocated to the process.
**Recovery plan**: Set the

```
 com.aliyun.openservices.ons.api.PropertyKeyConst#MaxCachedMessageSizeInMiB
```

parameter for the corresponding ConsumerBean based on the memory usage of the application instance, and then restart the application.

**Verification**

Verification 1: In `/{user.home}/logs/ons.log` , the "OutOfMemory" keyword no longer appears. Verification 2: Go to **Group Management > Consumer Status** and verify that the value in the **Real-time Consumption Speed** column increases and the **Real-time Message**
**Backlog** decreases.

#### 7.3.5 Message delivery fails with AuthenticationException

**AuthenticationException**

**Symptoms**

Your application cannot send or receive messages, and an `AuthenticationException` appears in the {user.home}/logs/ons.log file.

**Possible causes**

This issue is caused by an authentication failure due to an incorrect AK/SK.

**Solution**

1. Check if you are using a primary account or a sub-account.
ct usage issues The account roles map as follows:

| Apsara Uni-manager | RocketMQ v5.0 |
|---|---|
| organization administrator | primary account |
| resource user | sub-account |

You can create custom roles in Apsara Uni-manager. To use a custom role as a resource user, its permissions must match the system's default permissions.
2. Verify the permissions of the account that created the resource.
A primary account can create topics and group IDs in the RocketMQ v5.0 console. These resources are created at the organization level. A sub-account can create group IDs but not topics, and its resources are scoped to the sub-account level. To use a sub-account to send and receive messages, first use a primary account to create a topic, such as Topic_bumen, in the RocketMQ v5.0 console. After you grant permissions for this topic to a sub-account, the sub-account can view Topic_bumen in the RocketMQ v5.0 console. The sub-account must then create its own group ID, such as GID_zizhanghao. Your application can then use the sub-account's AK/SK, Topic_bumen, and GID_zizhanghao to send and receive messages. To use a topic and a group ID created by a primary account, you must use the matching organization-level AK/SK, as these resources belong to the organization, not the individual account.
