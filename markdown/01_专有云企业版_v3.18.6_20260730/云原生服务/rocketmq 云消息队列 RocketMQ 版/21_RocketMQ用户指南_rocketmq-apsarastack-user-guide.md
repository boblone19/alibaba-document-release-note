---
title: "云消息队列 RocketMQ 版 RocketMQ用户指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 312
source_pdf: "21_RocketMQ用户指南_rocketmq-apsarastack-user-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/rocketmq/zh/rocketmq-apsarastack-user-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云消息队列 RocketMQ 版 RocketMQ用户指南

消息队列 tMQ版

## 消息队列RocketMQ版

消息队列RocketMQ版（简称RocketMQ）是阿里云基于开源Apache RocketMQ构建的低延迟、高并发、 高可用、高可靠的分布式消息中间件。 RocketMQ基于高可用分布式集群技术，提供消息订阅和发布、消息轨迹查询、定时（延时）消息、资源统计等一系列消息云服务，是企业级互联网架构的核心产品。RocketMQ为分布式应用系统提供异步解耦、削峰填谷的能力，同时具备海量消息堆积、高吞吐、可靠重试等互联网应用所需的特性，是支持阿里巴巴双11 的核心产品。 RocketMQ目前提供TCP协议和HTTP协议层面的接入方式，支持Java、C++、.NET等多种编程语言，方便不同编程语言开发的应用快速接入RocketMQ消息云服务。 消息队列

## 产品更新说明

本文介绍消息队列RocketMQ版（简称RocketMQ）从V3.8.0到V3.18.3的产品更新说明，帮助您更快地上手更新后的版本。

**资源隔离优化（实例化支持）**

RocketMQ开放实例化功能，解决多租之间的隔离问题，每个用户可以购买多个实例，每个实例之间逻辑隔离。 为兼容老用户的既有资源，RocketMQ实例的命名空间分为两种： 默认实例（兼容老用户的既有资源） 无独立命名空间，实例内或者跨实例之间，资源命名必须全局唯一。 对RocketMQ老用户来说，既有资源将自动生成一个默认的无独立命名空间实例；无既有资源，则可选择创建不带命名空间的实例，最多创建1个。 接入点配置（可在控制台**实例详情**页面中获取）。 `//` 推荐配置

```
properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxxx");
```

`//` 兼容配置（不推荐继续使用, 建议逐渐升级为推荐配置）

```
properties.put(PropertyKeyConst.ONSAddr, "xxxx");
```

新建实例有独立命名空间，资源命名确保实例内唯一，跨实例之间可重名。 接入点配置（可在控制台**实例详情**页面中获取）。 `//` 推荐配置

```
properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxx");
```

ons-client客户端必须升级到最新版本： JAVA：1.8.7.1.Final C/C++：v2.0.0 .NET：1.1.3

**资源申请流程优化**

原RocketMQ的资源包括3个部分：消息主题（Topic）、生产者（Producer ID）、消费者（Consumer ID），三者之间都是多对多的对应关系，三者之间的关系复杂而难以理解；对于中、大型企业客户来说，每创建一个Topic，都要关联或者更新Producer ID和Consumer ID，流程过于复杂。 因此，为进一步优化用户体验，降低新用户的接入门槛，对资源申请的接入流程进行简化。 资源申请方面，主要包括以下部分： Topic资源申请，一级消息类型，通过Topic对消息进行分类。 取消原Producer ID的申请，与原Consumer ID统一为Group ID，即对应控制台上，取消原生产者管取消原申请Producer ID或Consumer ID时需要指定Topic的关联约束，只需申请Group ID即可在代码中直接配置与Topic的关联使用。 消息队列兼容性相关问题原申请的Producer ID列表将不再显示，不影响当前业务的正常使用。 原申请的以“CID-”或者“CID_”打头的Consumer ID仍可以正常使用，代码中既可在**PropertyKeyConst.ConsumerId**中设置，亦可在**PropertyKeyConst.GROUP_ID**中设置。 示例代码

**说明**

建议您将ons-client客户端升级为最新版本： JAVA：1.8.7.1.Final C/C++：v2.0.0 .NET：1.1.3 原来已经在使用的Producer ID或者Consumer ID保持兼容，不影响当前在线业务的正常使用，但建议逐步替换为新的推荐配置方式。 推荐方式：将Producer ID、Consumer ID的概念融合成Group ID。

```
// 设置PropertyKeyConst.GROUP_ID，原PropertyKeyConst.ProducerId和 PropertyKeyConst.ConsumerId会被@Deprecated properties.put(PropertyKeyConst.GROUP_ID, "原CID-XXX或GID-XXX");
```

兼容方式：Producer ID用来标识生产者，Consumer ID用来标识消费者。 `//` 创建`Producer`时需要配置`PropertyKeyConst.ProducerId`。

```
properties.put(PropertyKeyConst.ProducerId, "原PID-XXX或GID-XXX");
```

`//` 创建`Consumer`时需要配置`PropertyKeyConst.ConsumerId`。

```
properties.put(PropertyKeyConst.ConsumerId, "原CID-XXX或GID-XXX");
```

消息队列

## 快速入门

### 快速入门概述

RocketMQ提供了TCP协议和HTTP协议的多语言客户端SDK以收发不同类型的消息。本文介绍使用两种协

**背景信息**

面向服务端场景的应用使用RocketMQ，推荐用SDK方式接入，操作简单且可用性高。 本文作为快速入门，分别以TCP协议和HTTP协议下调用Java SDK为例来演示如何快速接入RocketMQ收发消息。 RocketMQ提供了四种消息类型，更多信息，请参见消息类型。本文以收发普通消息为例进行说明，因此， 您按照本文提供的步骤创建的普通消息的Topic，不能用于收发其他类型的消息。换言之，不同消息类型的 Topic不能混用。

**使用流程**

根据您选择的协议，使用流程如下。 消息队列
1. 创建资源：包括创建RocketMQ实例、Topic、Group以及获取实例的接入点信息。
2. 根据您选择的协议调用对应的SDK收发消息。

**协议使用须知**

由于RocketMQ提供的TCP协议客户端SDK和HTTP协议客户端SDK不同，所创建的同一个Group ID不能混用于TCP协议和HTTP协议。若您使用TCP协议的SDK收发消息，则您需要创建TCP协议类型的Group ID，不能使用HTTP协议类型的Group ID。 同一个RocketMQ实例分别提供TCP协议接入点和HTTP协议接入点，不同协议的接入点不能混用。若您使用TCP协议的SDK收发消息，则您需要获取实例的TCP协议接入点，不能使用HTTP协议的接入点。

**更多信息**

若您需要使用TCP或HTTP协议下的其他语言收发消息，请参见以下文档： 消息队列

### 登录RocketMQ控制台

本文介绍登录RocketMQ的步骤。

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。
消息队列

**说明**

单击页面右上角的当前语言可以切换其它语言。 授权登录是第三方认证中配置了全局IdP设置才会显示，且“授权登录”名称用户可按需自定义。 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
2. 输入正确的用户名及密码。

**说明**

请向运营管理员获取登录控制台的用户名和密码。 首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为10~32位，且包含英文字母大小写、阿拉伯数字和特殊符号（感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等）。
3. 单击**账号登录**。
4. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：

**管理员强制开启MFA后的首次登录**

a. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定MFA设备。 b. 按照步骤2重新输入账号和密码，单击**账号登录**。 c. 输入6位MFA码后单击**认证**。

**您已开启并绑定MFA**

输入6位MFA码后单击**认证**。

**说明**

绑定并开启MFA的操作请参见《**Apsara Uni-manager****运营控制台用户指南》**中的章节**《管理**
**多因素认证》**。
5. 在顶部菜单栏选择**产品** > **中间件** > **云消息队列** > **消息队列** **RocketMQ** 版，进入消息队列
RocketMQ版控制台。

### 创建资源

在调用客户端SDK收发消息前，您需在RocketMQ控制台创建相关资源及获取相关信息。您在调用SDK时需填写这些资源信息。

**背景信息**

一个新的应用接入RocketMQ需要先创建相关的资源，包括：
**实例：**用于RocketMQ服务的虚拟机资源，会存储消息主题（Topic）和客户端ID（Group ID）信息。
**Topic**：消息主题。在RocketMQ的消息系统中，消息生产者将消息发送到某个指定的Topic，而消息消
费者则通过订阅该指定的Topic来获取和消费消息。
**Group ID**：用于标识一类消息消费者或生产者。
消息队列

**重要**

由于TCP协议和HTTP协议的客户端各不相同，您需为两种协议分别创建不同类型的Group ID。例如，如果您使用TCP协议的SDK收发消息，则必须使用创建的TCP协议的Group ID，不允许使用 HTTP协议的Group ID。
**接入点：**RocketMQ服务端的访问地址，用于消息生产者客户端或消费者客户端接入指定的RocketMQ实
例。

**重要**

RocketMQ提供TCP协议接入点和HTTP协议接入点，接入点不能跨协议使用。例如，您使用TCP协议的SDK收发消息，则必须在SDK中填写TCP协议的接入点，不允许使用HTTP协议的接入点。
**AK**和**SK**：阿里云的身份验证信息，即AccessKey ID和AccessKey Secret。获取方式，请参
见《RocketMQ**开发指南》**手册的**《获取****AccessKey**》章节。

**创建实例**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面单击**创建实例**。
4. 在**创建****MQ****实例**页面中设置相关参数，然后单击**提交**。
相关参数说明如下：

| 参数 |  | 说明 | 取值示例 |
|---|---|---|---|
| 区域 | 组织 | 待创建实例归属的组织。 | root test _ |
|  | 资源集 | 待创建实例归属的资源集。 | DefaultResource |
|  | 地域 | 待创建实例所属的地域。 | cn-qingdao- env66-d01 |
|  | 芯片架构 | 待创建实例所部署的芯片类型，默认和RocketMQ集群所部署的芯片架构一致， 不支持自定义修改。 参数取值如下： intel 鲲鹏海光飞腾倚天申威 | intel |
|  | 集群 | 待创建实例所属的集群。 | cluster1 |

消息队列

| 基本配置 | 实例名称 | 长度限制为 3 ~ 64 个字符，可以是中文、 英文、数字、短横线（-）以及下划线 （ ）。 _ | test |
|---|---|---|---|
|  | Topic 数上限 | 表示该实例下支持创建的Topic的最大数量，若您不再需要使用某个Topic，请及时删除。 取值范围：10~5000。 默认值：50。 | 50 |
|  | 消息发送 TPS | 表示该实例的消息发送TPS的上限值。若实例开启了限流功能，则消息发送TPS超过该上限值时，RocketMQ会对消息发送进行流控处理。 实例限流功能默认关闭，若您需要开启，请参见《RocketMQ运维指南》手册的《实例限流运维操作》章节。 取值范围：500~30000，单位：次/秒。 默认值：500。 | 500 |
|  | 消息订阅 TPS | 表示该实例的消息订阅TPS的上限值。 取值范围：500~30000，单位：次/秒。 默认值：500。 | 500 |
|  | 描述 | 2-128个字符，以字母或中文开头，支持数字和" "、"-"、":"特殊字符，不能以http:// _ 或https://开头。 | test |

5. **（可选）**如果您配置了审批流程，则需要额外进行如下操作：
i. 在**流程信息补充**对话框中，选择**审批后执行方式**并填写**操作理由，**然后单击**提交审批**。 ii. 在**操作成功**的对话框中，单击**申请单详情**，跳转到申请单详情页面。 iii. 在**申请单进度**区域中单击**查看全部**，进入到**申请单进度**面板，待所有环节全部完成，则完成审批流程。 在**实例列表**页面，即可查看到已创建的实例。

**获取实例接入点**

1. 在RocketMQ控制台的左侧导航栏，单击**实例列表**。
2. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
3. 在**实例详情**页面，单击**网络管理**页签，即可查看指定实例的接入点信息。
**TCP****协议客户端接入点**：若您使用TCP协议SDK收发消息，需要在代码中填写该接入点信息。
**HTTP****协议客户端接入点**：若您使用HTTP协议SDK收发消息，需要在代码中填写该接入点信息。

**创建Topic**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
消息队列
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**Topic****管理**页签。
5. 单击**创建****Topic**。
6. 在**创建****Topic**对话框设置相关参数，然后单击**确定**。

| 参数 | 说明 |
|---|---|
| Topic | 设置Topic名称。 Topic只能包含英文、数字、 短横线（-）和下划线（ ）。 _ 长度限制在3～64个字符之间。 新建Topic名称不能与已存在的Topic名称或Group ID完全一致。 |
| 消息类型 | 设置消息类型。 重要 RocketMQ支持普通消息、分区顺序消息、定时/延时消息和事务消息，您创建Topic时选择的消息类型必须和您后续发送消息的类型保持一致，否则可能会导致消息发送失败。 |
| 描述 | 设置Topic描述。 |

**创建Group ID**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**Group****管理**页签。
5. 选择Group ID的协议类型。
若您使用TCP协议的SDK收发消息，需要创建TCP协议类型的Group ID，请单击**TCP** **协议**页签。 若您使用HTTP协议的SDK收发消息，需要创建HTTP协议类型的Group ID，请单击**HTTP** **协议**页签。
6. 单击**创建** **Group ID**，在**创建** **Group ID**对话框设置相关参数，然后单击**确定**。

| 参数 | 说明 |
|---|---|
| Group ID | 设置Group ID。 Group ID只能包含英文、数字、 短横线（-）和下划线（ ）。 _ 长度限制在4～64个字符之间。 Group ID 一旦创建，则无法修改。 新建Group ID不能与已存在的Topic名称或Group ID完全一致。 |

消息队列

| 描述 | 设置Group描述。 |
|---|---|

**说明**

Group ID 既可用于生产者，标识同一类 Producer 实例（Producer ID），又可用于消费者， 标识同一类 Consumer 实例（Consumer ID）； 同一个 Group ID 不可以共用于 TCP 协议和 HTTP 协议，需要分别申请。

### 发送消息

#### 快速使用TCP协议的SDK收发普通消息

在控制台创建完所有资源之后，您可以调用RocketMQ的TCP协议的SDK收发普通消息。

**前提条件**

您已创建了相关资源，详细信息请参见创建资源。

**通过Maven方式引入依赖**

```xml
<dependency>
   <groupId>com.aliyun.openservices</groupId>
   <artifactId>ons-client</artifactId>
   <version>"XXX"</version>
</dependency>
```

**下载依赖JAR包**

**调用TCP协议的SDK发送普通消息**

运行以下示例代码发送普通消息。运行代码前请参考注释填写您提前创建好的资源信息。 消息队列

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
```

`//` 您在`RocketMQ`控制台创建的`TCP`协议类型的`Group ID`。

```
         properties.put(PropertyKeyConst.GROUP_ID, "XXX");
```

`// AccessKey ID`，阿里云身份验证。

```
         properties.put(PropertyKeyConst.AccessKey,"XXX");
```

`// AccessKey Secret`，阿里云身份验证。

```
         properties.put(PropertyKeyConst.SecretKey, "XXX");
```

`//` 设置为实例的`TCP`接入域名，进入`RocketMQ`控制台实例详情页面的网络管理页签中查看。

```
         properties.put(PropertyKeyConst.NAMESRV_ADDR,"XXX");
         Producer producer = ONSFactory.createProducer(properties);
```

`//` 在发送消息前，必须调用`start`方法来启动`Producer`，只需调用一次即可。

```
         producer.start();
```

`//`循环发送消息。

```
         while(true){
             Message msg = new Message(
```

`//` 您在`RocketMQ`控制台创建的`Topic`，即该消息所属的`Topic`名称。

```
                 "TopicTestMQ",
                 // Message Tag,
```

`//` 可理解为`Gmail`中的标签，对消息进行再归类，方便`Consumer`指定过滤条件在`RocketMQ`服务器过滤。

```
                 "TagA",
                 // Message Body
```

`//` 任何二进制形式的数据，`RocketMQ`不做任何干预。 `//` 需要`Producer`与`Consumer`协商好一致的序列化和反序列化方式。

```
                 "Hello MQ".getBytes());
```

`//` 设置代表消息的业务关键属性，请尽可能全局唯一，以方便您在无法正常收到消息情况下，可通过控制台查询消息并补发。 `//` 注意：不设置也不会影响消息正常收发。

```
             msg.setKey("ORDERID_100");
```

`//` 发送消息，只要不抛异常就是成功。 `//` 打印`Message ID`，以便用于消息发送状态查询。

```java
             SendResult sendResult = producer.send(msg);
             System.out.println("Send Message success. Message ID is: " +
sendResult.getMessageId());
         }
```

`//` 在应用退出前，可以销毁`Producer`对象。 `//` 注意：如果不销毁也没有问题。

```
         producer.shutdown();
     }
 }
```

同时，您也可以登录RocketMQ控制台，在**Topic****管理**页签找到您刚创建好的Topic，单击右侧**操作**列的发
**送消息**，通过控制台快速体验消息发送。

**调用TCP协议的SDK订阅普通消息**

消息队列运行以下示例代码订阅普通消息。运行代码前请参考注释填写您提前创建好的资源信息。

```java
import com.aliyun.openservices.ons.api.Action; import com.aliyun.openservices.ons.api.ConsumeContext; import com.aliyun.openservices.ons.api.Consumer; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.MessageListener; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import java.util.Properties; public class ConsumerTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
```

`//` 您在`RocketMQ`控制台创建的`TCP`协议类型的`Group ID`。

```
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
```

`// AccessKey ID`，阿里云身份验证。

```
         properties.put(PropertyKeyConst.AccessKey,"XXX");
```

`// AccessKey Secret`，阿里云身份验证。

```
         properties.put(PropertyKeyConst.SecretKey, "XXX");
```

`//` 设置为实例的`TCP`接入域名，进入`RocketMQ`控制台实例详情页面的网络管理页签中查看。

```java
        properties.put(PropertyKeyConst.NAMESRV_ADDR,"XXX");
        Consumer consumer = ONSFactory.createConsumer(properties);
        consumer.subscribe("TopicTestMQ", "*", new MessageListener() {
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
            }
        });
        consumer.start();
        System.out.println("Consumer Started");
    }
}
```

**查看消息订阅是否成功**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**Group****管理**页签。
5. 在Group列表中找到要查看消费者的Group ID，单击其右侧**操作**列的**订阅关系**。
如果**是否在线**显示为是，则说明消费端已成功启动且订阅成功。否则说明订阅失败。

**后续步骤**

#### 查询消息

#### 快速使用HTTP协议的SDK收发普通消息

在控制台创建完所有资源之后，您可以调用RocketMQ的HTTP协议的SDK收发普通消息。 消息队列

**前提条件**

您已创建了相关资源，详细信息请参见创建资源。

**通过Maven方式引入依赖**

```xml
<dependency>
    <groupId>com.aliyun.mq</groupId>
    <artifactId>mq-http-sdk</artifactId>
    <version>X.X.X</version>
    <classifier>jar-with-dependencies</classifier>
</dependency>
```

**下载依赖JAR包**

**调用HTTP协议的SDK发送普通消息**

运行以下示例代码发送普通消息。运行代码前请参考注释填写您提前创建好的资源信息。

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQProducer; import com.aliyun.mq.http.model.TopicMessage; import java.util.Date; public class Producer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
```

`//` 设置为实例的`HTTP`接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签中查看。

```
                "${HTTP_ENDPOINT}",
```

`// AccessKey ID`，阿里云身份验证。

```
                "${ACCESS_KEY}",
```

`// AccessKey Secret`，阿里云身份验证。

```
                "${SECRET_KEY}"
        );
```

`//` 您在控制台创建的`Topic`，即该消息所属的`Topic`名称。

```
        final String topic = "${TOPIC}";
```

`// Topic`所属的实例`ID`。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        final String instanceId = "${INSTANCE_ID}";
```

`//` 获取`Topic`的生产者。

```
        MQProducer producer;
        if (instanceId != null && instanceId != "") {
            producer = mqClient.getProducer(instanceId, topic);
        } else {
            producer = mqClient.getProducer(topic);
}
```

消息队列

```
        }
        try {
```

`//` 循环发送4条消息。

```
            for (int i = 0; i < 4; i++) {
                TopicMessage pubMsg;        // 普通消息。
                pubMsg = new TopicMessage(
```

`//` 消息内容。

```
                "hello mq!".getBytes(),
```

`//` 消息标签。

```
                "A"
                );
```

`//` 设置消息的自定义属性。

```
                pubMsg.getProperties().put("a", String.valueOf(i));
```

`//` 设置消息的`Key`。

```
                pubMsg.setMessageKey("MessageKey");
```

`//` 同步发送消息，只要不抛异常就是成功。

```
            TopicMessage pubResultMsg = producer.publishMessage(pubMsg);
```

`//` 同步发送消息，只要不抛异常就是成功。

```java
            System.out.println(new Date() + " Send mq message success. Topic is:" +
topic + ", msgId is: " + pubResultMsg.getMessageId()
                        + ", bodyMD5 is: " + pubResultMsg.getMessageBodyMD5());
            }
        } catch (Throwable e) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理。

```java
            System.out.println(new Date() + " Send mq message failed. Topic is:" +
topic);
            e.printStackTrace();
        }
        mqClient.close();
    }
}
```

同时，您也可以登录RocketMQ控制台，在**Topic****管理**页签找到您刚创建好的Topic，单击右侧**操作**列的发
**送消息**，通过控制台快速体验消息发送。

**调用HTTP协议的SDK订阅普通消息**

运行以下示例代码订阅普通消息。运行代码前请参考注释填写您提前创建好的资源信息。

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQConsumer; import com.aliyun.mq.http.common.AckMessageException; import com.aliyun.mq.http.model.Message; import java.util.ArrayList; import java.util.List; public class Consumer {
    public static void main(String[] args) {
```

消息队列

```
        MQClient mqClient = new MQClient(
```

`//` 设置为实例的`HTTP`接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签中查看。

```
                "${HTTP_ENDPOINT}",
```

`// AccessKey ID`，阿里云身份验证。

```
                "${ACCESS_KEY}",
```

`// AccessKey Secret`，阿里云身份验证。

```
                "${SECRET_KEY}"
        );
```

`//` 您在`RocketMQ`控制台创建的`Topic`，即该消息所属的`Topic`名称。

```
        final String topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`HTTP`协议类型的`Group ID`。

```
        final String groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        final String instanceId = "${INSTANCE_ID}";
        final MQConsumer consumer;
        if (instanceId != null && instanceId != "") {
            consumer = mqClient.getConsumer(instanceId, topic, groupId, null);
        } else {
            consumer = mqClient.getConsumer(topic, groupId);
        }
```

`//` 在当前线程循环消费消息，建议多开个几个线程并发消费消息。

```
        do {
            List<Message> messages = null;
            try {
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息,则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回客户端。

```
                messages = consumer.consumeMessage(
```

`3,//` 一次最多消费3条消息（最多可设置为`16`条）。 `3//` 长轮询时间3秒（最多可设置为`30`秒）。

```
                );
            } catch (Throwable e) {
                e.printStackTrace();
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e1) {
                    e1.printStackTrace();
                }
            }
```

`// Topic`中没有消息可消费。

```java
            if (messages == null || messages.isEmpty()) {
                System.out.println(Thread.currentThread().getName() + ": no new message,
continue!");
                continue;
            }
```

`//` 处理业务逻辑。

```
            for (Message message : messages) {
Systemoutprintln("Receivemessage:"+message);
```

消息队列

```java
                System.out.println("Receive message: " + message);
            }
```

`//` 消息重试时间到达前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费的时间戳都不一样。

```
            {
                List<String> handles = new ArrayList<String>();
                for (Message message : messages) {
                    handles.add(message.getReceiptHandle());
                }
                try {
                    consumer.ackMessage(handles);
                } catch (Throwable e) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```java
                    if (e instanceof AckMessageException) {
                        AckMessageException errors = (AckMessageException) e;
                        System.out.println("Ack message fail, requestId is:" +
errors.getRequestId() + ", fail handles:");
                        if (errors.getErrorMessages() != null) {
                            for (String errorHandle :errors.getErrorMessages().keySet())
{
                                System.out.println("Handle:" + errorHandle + ",
ErrorCode:" + errors.getErrorMessages().get(errorHandle).getErrorCode()
                                        + ", ErrorMsg:" +
errors.getErrorMessages().get(errorHandle).getErrorMessage());
                            }
                        }
                        continue;
                    }
                    e.printStackTrace();
                }
            }
        } while (true);
    }
}
```

**查看消息订阅是否成功**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**Group****管理**页签。
5. 在Group列表中找到要查看消费者的Group ID，单击其右侧**操作**列的**订阅关系**。
如果**是否在线**显示为是，则说明消费端已成功启动且订阅成功。否则说明订阅失败。

**后续步骤**

#### 查询消息

消息队列

#### 查看消息是否发送成功

消息发送后，您可以在控制台查看消息发送状态。

**操作步骤**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**消息查询**页签。
5. 在**消息查询**页面，单击按 **Message ID** **查询**页签。
6. 在搜索框中输入**Topic**以及发送消息后返回的**Message ID**，单击**查询**查看消息发送状态。
**存储时间**表示RocketMQ服务端存储这条消息的时间。如果查询到此消息，表示消息已经成功发送到服务
端。

**重要**

此步骤演示的是第一次使用RocketMQ的场景，此时消费者从未启动过，所以消息状态显示暂无消费数据。

**后续步骤**

要启动消费者并进行消息订阅请继续订阅消息。更多消息状态请参见消息查询和消息轨迹状态说明。

### 订阅消息

消息发送成功后，消费方就可以订阅消息。订阅消息需要通过调用相关协议及开发语言的SDK来完成。本文

**操作步骤**

1. 运行以下示例代码来测试订阅消息的功能。运行代码前请按照说明正确设置相关参数。
消息队列

```java
import com.aliyun.openservices.ons.api.Action; import com.aliyun.openservices.ons.api.ConsumeContext; import com.aliyun.openservices.ons.api.Consumer; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.MessageListener; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import java.util.Properties; public class ConsumerTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
```

`//` 您在控制台创建的`Group ID`

```
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
```

`//` 鉴权用`AccessKeyId`

```
        properties.put(PropertyKeyConst.AccessKey, "XXX");
        // 鉴权用AccessKeySecret
        properties.put(PropertyKeyConst.SecretKey, "XXX");
```

`//` 设置`TCP`接入域名，进入控制台的实例管理页面，在页面上方选择实例后，在实例信息中的“获取接入点信息”区域查看

```java
        properties.put(PropertyKeyConst.NAMESRV_ADDR,"XXX");
        Consumer consumer = ONSFactory.createConsumer(properties);
        consumer.subscribe("TopicTestMQ", "*", new MessageListener() {
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
            }
        });
        consumer.start();
        System.out.println("Consumer Started");
    }
}
```

完成后，可以在RocketMQ控制台查看消费端是否成功启动，即消息订阅是否完成。
2. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
3. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
4. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
5. 在**实例详情**页面，单击**Group****管理**页签。
6. 在Group列表中找到要查看消费者的Group ID，单击其右侧**操作**列的**订阅关系**。
如果**是否在线**显示为是，则说明消费端已成功启动且订阅成功。否则说明订阅失败。 消息队列

## 消息类型

### 普通消息

本文介绍普通消息的定义以及示例代码。 普通消息是指RocketMQ中无特性的消息，区别于有特性的定时和延时消息、顺序消息和事务消息。收发普通消息的示例代码如下所示。

**TCP SDK示例代码**

### 订阅消息

**HTTP SDK示例代码**

### 定时和延时消息

**概念介绍**

定时消息：生产者将消息发送到RocketMQ服务端，但并不期望这条消息立马投递，而是推迟到当前时间点之后的某一个时间投递到消费者进行消费，该消息即定时消息。 延时消息：生产者将消息发送到RocketMQ服务端，但并不期望这条消息立马投递，而是延迟一定时间后才投递到消费者进行消费，该消息即延时消息。 定时消息与延迟消息在代码配置上存在一些差异，但是最终达到的效果相同：消息在发送到RocketMQ服务端后并不会立马投递，而是根据消息中的属性延迟固定时间后才投递给消费者。

**适用场景**

定时消息和延时消息适用于以下一些场景： 消息生产和消费有时间窗口要求：例如在电商交易中超时未支付关闭订单的场景，在订单创建时会发送一条RocketMQ延时消息，这条消息将会在30分钟以后投递给消费者，消费者收到此消息后需要判断对应的订单是否已完成支付。如支付未完成，则关闭订单，如已完成支付则忽略。 通过消息触发一些定时任务，例如在某一固定时间点向用户发送提醒消息。 消息队列

**使用方式**

发送定时消息需要明确指定消息发送时间点之后的某一时间点作为消息投递的时间点。 发送延时消息时需要设定一个延时时间长度，消息将从当前发送时间点开始延迟固定时间之后才开始投递。

**注意事项**

定时和延时消息的**msg.setStartDeliverTime**参数需要设置成当前时间戳之后的某个时刻（单位毫秒）。如果被设置成当前时间戳之前的某个时刻，消息将立刻投递给消费者。 定时和延时消息的**msg.setStartDeliverTime**参数可设置40天内的任何时刻（单位毫秒），超过40 天消息发送将失败。
**StartDeliverTime**是服务端开始向消费端投递的时间。如果消费者当前有消息堆积，那么定时和延时
消息会排在堆积消息后面，将不能严格按照配置的时间进行投递。 由于客户端和服务端可能存在时间差，消息的实际投递时间与客户端设置的投递时间之间可能存在偏差。 设置定时、延时消息的投递时间后，依然受3天的消息保存时长限制。例如，设置定时消息5天后才能被消费，如果第5天后一直没被消费，那么这条消息将在第8天被删除。

**TCP SDK示例代码**

**HTTP SDK示例代码**

### 事务消息

本文介绍RocketMQ事务消息的概念、适用场景以及使用方式和注意事项。

**概念介绍**

事务消息：RocketMQ提供类似X/Open XA的分布事务功能，通过RocketMQ事务消息能达到分布式事务的最终一致。 半事务消息：暂不能投递的消息，发送方已经将消息成功发送到了RocketMQ服务端，但是服务端未收到生产者对该消息的二次确认，此时该消息被标记成“暂不能投递”状态，处于该种状态下的消息即半事务消息。 消息回查：由于网络闪断、生产者应用重启等原因，导致某条事务消息的二次确认丢失，RocketMQ服务端通过扫描发现某条消息长期处于“半消息”时，需要主动向消息生产者询问该消息的最终状态（Commit 或是Rollback），该过程即消息回查。 消息队列

**适用场景**

RocketMQ事务消息适用于以下场景： 帮助用户实现类似X/Open XA的分布事务功能，通过RocketMQ事务消息能达到分布式事务的最终一致。 例如，通过购物车进行下单的流程中，用户入口在购物车系统，交易下单入口在交易系统，两个系统之间的数据需要保持最终一致，这时可以通过事务消息进行处理。交易系统下单之后，发送一条交易下单的消息到RocketMQ，购物车系统订阅RocketMQ的交易下单消息，做相应的业务处理，更新购物车数据。

**使用方式**

交互流程 RocketMQ事务消息交互流程如下图所示。 事务消息发送步骤如下：
1. 发送方将半事务消息发送至RocketMQ服务端。
2. 服务端将消息持久化成功之后，向发送方返回ACK确认消息已经发送成功，此时消息为半事务消息。
3. 发送方开始执行本地事务逻辑。
4. 发送方根据本地事务执行结果向服务端提交二次确认（Commit或是Rollback），服务端收到Commit状
态则将半事务消息标记为可投递，订阅方最终将收到该消息；服务端收到Rollback状态则删除半事务消息，订阅方将不会接受该消息。 事务消息回查步骤如下： 在断网或者是应用重启的特殊情况下，上述步骤4提交的二次确认最终未到达服务端，经过固定时间后服务端将对该消息发起消息回查。 发送方收到消息回查后，需要检查对应消息的本地事务执行的最终结果。 发送方根据检查得到的本地事务的最终状态再次提交二次确认，服务端仍按照步骤4对半事务消息进行操作。

**注意事项**

1. 事务消息的Group ID不能与其他类型消息的Group ID共用。与其他类型的消息不同，事务消息有回查机
制，回查时RocketMQ服务端会根据Group ID去查询客户端。
2. 通过**ONSFactory.createTransactionProducer**创建事务消息的Producer时必须指
定**LocalTransactionChecker**的实现类，处理异常情况下事务消息的回查。
3. 事务消息发送完成本地事务后，可在**execute**方法中返回如下三种状态：
**TransactionStatus.CommitTransaction**提交事务，允许订阅方消费该消息。
**TransactionStatus.RollbackTransaction**回滚事务，消息将被丢弃不允许消费。
**TransactionStatus.Unknow**暂时无法判断状态，期待固定时间以后RocketMQ服务端向发送方
进行消息回查。

**TCP SDK示例代码**

消息队列

**HTTP SDK示例代码**

### 顺序消息

顺序消息可以保证消息的消费顺序和发送的顺序一致，即先发送的先消费，后发送的后消费，常用于金融证券、电商业务等对消息指令顺序有严格要求的场景。本文介绍RocketMQ顺序消息的概念、适用场景、实现原理以及使用过程中的注意事项。

**什么是顺序消息**

**定义**

顺序消息是RocketMQ提供的一种对消息发送和消费顺序有严格要求的消息。对于一个指定的Topic，消息严格按照先进先出（FIFO）的原则进行消息发布和消费，即先发布的消息先消费，后发布的消息后消费。 RocketMQ的顺序消息中，对于指定的一个Topic，所有消息根据Sharding Key进行区块分区，同一个分区内的消息按照严格的先进先出（FIFO）原则进行发布和消费。同一分区内的消息保证顺序，不同分区之间的消息顺序不做要求。因此RocketMQ的顺序消息也叫分区顺序消息。

**基本概念**

Sharding Key：顺序消息中用来区分Topic中不同分区的关键字段，和普通消息的Key是完全不同的概念。RocketMQ会将设置了相同Sharding Key的消息路由到同一个分区下，同一个分区内的消息将按照消息发布顺序进行消费。 分区：即Topic Partition，每个Topic包含一个或多个分区，Topic中的消息会分布在这些不同的分区中。本文中的逻辑分区指的就是Topic的分区。 物理分区：区别于逻辑分区，消息实际存储的单元，每个物理分区都会分配到某一台机器指定节点上。

**适用场景**

常用于金融证券、电商业务等对消息指令顺序有严格要求的场景。示例如下： 用户注册需要发送验证码，以用户ID作为Sharding Key，那么同一个用户发送的消息都会按照发布的先后顺序来消费。 电商的订单创建，以订单ID作为Sharding Key，那么同一个订单相关的创建订单消息、订单支付消息、 订单退款消息、订单物流消息都会按照发布的先后顺序来消费。

**如何实现顺序消息**

消息队列在RocketMQ中，消息的顺序需要由以下三个阶段保证：

**消息发送**

如上图所示，A1、B1、A2、A3、B2、B3是订单A和订单B的消息产生的顺序，业务上要求同一订单的消息保持顺序，例如订单A的消息发送和消费都按照A1、A2、A3的顺序。如果是普通消息，订单A的消息可能会被轮询发送到不同的队列中，不同队列的消息将无法保持顺序，而顺序消息发送时RocketMQ支持将Sharding Key相同（例如同一订单号）的消息序路由到一个分区中。 RocketMQ服务端判定消息产生的顺序性是参照同一生产者发送消息的时序。不同生产者、不同线程并发产生的消息，RocketMQ服务端无法判定消息的先后顺序。

**消息存储**

如上图所示，Topic中的每个分区（逻辑分区）对应一个物理分区，当消息按照顺序发送到Topic中的逻辑分区时，每个分区的消息将按照同样的顺序存储到对应的物理分区中。

**消息消费**

RocketMQ按照存储的顺序将消息投递给Consumer，Consumer收到消息后也不对消息顺序做任何处理，按照接收到的顺序进行消费。 Consumer消费消息时，同一Sharding Key的消息使用单线程消费，保证消息消费顺序和存储顺序一致，最终实现消费顺序和发布顺序的一致。

**消息类型对比**

| 消息类型 | 性能 | 支持可靠同步发送 | 支持可靠异步发送 | 支持Oneway发送 |
|---|---|---|---|---|
| 无序消息（普通、 事务、定时/延时消息） | 高 | 是 | 是 | 是 |
| 顺序消息 | 一般 | 是 | 否 | 否 |

**注意事项**

同一个Group ID只对应一种类型的Topic，即不同时用于顺序消息和无序消息的收发。 顺序消息暂不支持广播模式。 顺序消息不支持异步发送方式，否则将无法严格保证顺序。

**TCP SDK示例代码**

消息队列

**HTTP SDK示例代码**

消息队列

## 控制台使用指南

### 资源管理

#### 资源管理概述

本文介绍RocketMQ的资源管理。 一个新的应用接入RocketMQ需要先创建相关的RocketMQ资源，包括：
**实例：**用于RocketMQ服务的虚拟机资源，会存储消息主题（Topic）和客户端ID（Group ID）信息。
**消息主题（****Topic****）：**在RocketMQ的消息系统中，消息生产者将消息发送到某个指定的Topic，而消息
消费者则通过订阅该指定的Topic来获取和消费消息。
**Group ID**：用于标识消息消费者或生产者。
您可以在RocketMQ控制台或调用API对这些资源进行增删改查的操作，同时也可以对这些资源的增删改的操作配置审批流程，做到资源的流程化管理。 在调用SDK发送和订阅消息的时候，除了需要指定创建的Topic、Group ID以外，还需输入您在控制台创建的身份验证信息，即AccessKey ID和AccessKey Secret。 如果您还没获取访问密钥，可以在Apsara Uni-manager运营控制台获取。具体操作方式，请参见获取AK 和SK。

#### 实例管理

实例存储了消息主题（Topic）和客户端ID（Group ID）信息。本文介绍如何在RocketMQ控制台上创建、 更新、查看以及删除实例。

**创建实例**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面单击**创建实例**。
4. 在**创建****MQ****实例**页面中设置相关参数，然后单击**提交**。
相关参数说明如下：

| 参数 |  | 说明 | 取值示例 |
|---|---|---|---|
|  | 组织 | 待创建实例归属的组织。 | root test _ |
|  | 资源集 | 待创建实例归属的资源集。 | DefaultResource |
|  | 地域 | 待创建实例所属的地域。 | cn-qingdao- env66-d01 |

消息队列

| 区域 |  |  |  |
|---|---|---|---|
|  | 芯片架构 | 待创建实例所部署的芯片类型，默认和RocketMQ集群所部署的芯片架构一致， 不支持自定义修改。 参数取值如下： intel 鲲鹏海光飞腾倚天申威 | intel |
|  | 集群 | 待创建实例所属的集群。 | cluster1 |
| 基本配置 | 实例名称 | 长度限制为 3 ~ 64 个字符，可以是中文、 英文、数字、短横线（-）以及下划线 （ ）。 _ | test |
|  | Topic 数上限 | 表示该实例下支持创建的Topic的最大数量，若您不再需要使用某个Topic，请及时删除。 取值范围：10~5000。 默认值：50。 | 50 |
|  | 消息发送 TPS | 表示该实例的消息发送TPS的上限值。若实例开启了限流功能，则消息发送TPS超过该上限值时，RocketMQ会对消息发送进行流控处理。 实例限流功能默认关闭，若您需要开启，请参见《RocketMQ运维指南》手册的《实例限流运维操作》章节。 取值范围：500~30000，单位：次/秒。 默认值：500。 | 500 |
|  | 消息订阅 TPS | 表示该实例的消息订阅TPS的上限值。 取值范围：500~30000，单位：次/秒。 默认值：500。 | 500 |
|  | 描述 | 2-128个字符，以字母或中文开头，支持数字和" "、"-"、":"特殊字符，不能以http:// _ 或https://开头。 | test |

5. **（可选）**如果您配置了审批流程，则需要额外进行如下操作：
i. 在**流程信息补充**对话框中，选择**审批后执行方式**并填写**操作理由，**然后单击**提交审批**。 ii. 在**操作成功**的对话框中，单击**申请单详情**，跳转到申请单详情页面。 iii. 在**申请单进度**区域中单击**查看全部**，进入到**申请单进度**面板，待所有环节全部完成，则完成审批流程。 消息队列在**实例列表**页面，即可查看到已创建的实例。

**查看实例列表**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面，您可快速查看实例的**实例****ID/****名称**、**实例类型**、**集群****ID**、**部门**、**资源集**、**状态**信息，以
及其是否是**容灾集群**。
3. （可选）在**实例列表**页面，您可以通过选择**自动识别**、**实例****ID**、**实例名称**、**集群****ID**的方式，在搜索框内
快速搜索目标实例。
4. （可选）在**实例列表**页面，您可以单击目标实例**监控**列的
，快速查看实例的监控信息。

**查看实例详情**

在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，即可查看目标实例的详细信息： 基本信息：在**实例详情**页面的**基本信息**页签显示该实例的ID、Topic上限、名称、消息订阅TPS上限、消息发送TPS上限、集群ID、描述、部门及部门ID、资源集及资源集ID、芯片类型、是否拥有独立命名空间，以及是否是容灾集群。 网络管理：在**实例详情**页面的**网络管理**页签，可查看实例的接入点信息。接入点使用场景，请参见客户端接入说明。 Topic管理：在**实例详情**页面的**Topic****管理**页签，可查看到该实例下所有Topic的基本信息，包括Topic名称、Topic的消息类型、Topic的权限信息、描述和可执行操作。详细信息请参见Topic管理。 Group管理：在**实例详情**页面的**Group****管理**页签，可查看到该实例下的所有Group ID的基本信息，包括消息查询：在**实例详情**页面的**消息查询**页签，可按Message ID、Message Key以及Topic查询消息，详细信息请参见消息查询。 消息轨迹：在**实例详情**页面的**消息轨迹**页签，可进行消息轨迹查询，详细信息请参见消息轨迹。 死信队列：在**实例详情**页面的**死信队列**页签，可查询、导出和重新发送进入死信队列的死信消息，详细信息请参见死信队列。 资源报表：在**实例详情**页面的**资源报表**页签，可使用资源报表对消息生产和消费信息进行查询，详细信息请参见资源报表。 监控：在**实例详情**页面的**监控**页签，可查看实例、Group、Topic和Topic&Group的监控信息，详细信息操作日志：在**实例详情**页面的**操作日志**页签，可查看实例的操作日志，详细信息请参见查看实例操作日志。 数据集成：在**实例详情**页面的**数据集成**页签，可进行数据集成的相关配置，详细信息请参见数据集成。 您也可以点击实例名称右侧的下拉按钮切换实例。

**更新实例配置**

您可以升级或降级当前实例的配置。
1. 在**实例列表**页面选择目标实例，单击**操作**列的**变配**。
2. 在**更新配置**页面，修改实例的**基本配置**信息，然后单击**提交**。
可修改的基本配置信息包括**实例名称**、**Topic** **数上限**、**消息发送** **TPS**、**消息订阅** **TPS**和**描述**。
3. **（可选）**如果您配置了审批流程，则需要额外进行如下操作：
i. 在**流程信息补充**对话框中，选择**审批后执行方式**并填写**操作理由，**然后单击**提交审批**。 ii. 在**操作成功**的对话框中，单击**申请单详情**，跳转到申请单详情页面。 消息队列 iii. 在**申请单进度**区域中单击**查看全部**，进入到**申请单进度**面板，待所有环节全部完成，则完成审批流程。

**删除实例**

**重要**

删除RocketMQ实例前，请确保： 您已删除该实例下的所有资源，包括Topic和Group ID。 该实例无绑定的微消息队列MQTT版实例。
1. 在**实例列表**页面找到需要删除的目标实例，单击**操作**列的**删除**。
2. 在弹出的提示对话框中，仔细阅读提示信息，单击**释放**。

**客户端接入说明**

客户端使用消息队列RocketMQ版的SDK进行消息收发时，需要在代码中配置实例信息，包括实例ID和实例实例ID在**实例详情**页面的**基本信息**页签查看。 实例的接入点在**实例详情**页面的**网络管理**页签查看。 配置方式如下： `//` 配置实例`ID`，将`<InstancedId>`替换为您在控制台已创建好的实例的`ID`。

```
properties.put(PropertyKeyConst.INSTANCE_ID, "<InstancedId>");
```

`//` 配置实例接入点，将`<Endpoint>`替换为您在控制台已创建好的实例的接入点。

```
properties.put(PropertyKeyConst.NAMESRV_ADDR, "<Endpoint>");
```

**更多信息**

如需使用API完成相关操作，请参见《RocketMQ**开发指南》**的相关内容。

#### Topic管理

消息主题（Topic）是RocketMQ里对消息的一级归类。RocketMQ支持发布和订阅模型，通过Topic完成消息的发布和订阅。消息生产者将消息发送到Topic中，而消息消费者则通过订阅该Topic来消费消息。本文介绍如何在RocketMQ控制台上创建、查看、更新以及删除Topic。

**前提条件**

您已创建了RocketMQ实例，详细信息请参见创建实例。

**创建Topic**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**Topic****管理**页签。
5. 单击**创建****Topic**。
6. 在**创建****Topic**对话框设置相关参数，然后单击**确定**。

| 参数 | 说明 |
|---|---|

消息队列

| Topic | 设置Topic名称。 Topic只能包含英文、数字、 短横线（-）和下划线（ ）。 _ 长度限制在3～64个字符之间。 新建Topic名称不能与已存在的Topic名称或Group ID完全一致。 |
|---|---|
| 消息类型 | 设置消息类型。 重要 RocketMQ支持普通消息、分区顺序消息、定时/延时消息和事务消息，您创建Topic时选择的消息类型必须和您后续发送消息的类型保持一致，否则可能会导致消息发送失败。 |
| 描述 | 设置Topic描述。 |

**更新Topic描述**

1. 在**Topic****管理**页签，于Topic列表中找到需要修改描述的Topic，在其**描述**列，单击
图标。
2. 在弹出的**修改描述**对话框中，输入更新后的描述，单击**确定**。

**查看Topic信息**

在**实例详情**页面，单击**Topic****管理**页签。即可查看该实例下所有Topic的基本信息，包括Topic名称、Topic 的消息类型、Topic的权限信息、描述、最近使用时间和可执行操作。

**删除Topic**

在创建实例时，您需要指定实例的Topic数量上限值，超过该上限值则无法再继续创建Topic。当您不需要使用某个Topic时，请及时删除该Topic资源。

**重要**

删除Topic之后，相关的生产者、消费者将会立即停止服务，并且同时会删除Topic元数据和Topic的消息数据，且数据不可恢复，请谨慎操作。
1. 在**Topic****管理**页签，于Topic列表中找到您需删除的目标Topic，在其**操作**列单击**删除**。
2. 请仔细阅读弹出的**提醒**对话框中的内容，确认无误后，单击**确定**。

**单实例Topic导入/导出**

**导入**

1. 在**Topic****管理**页签，单击**导入**。
2. 在**导入****Topic**窗口，单击**上传文件**。文件上传完成后，平台将自动识别上传的topic并进行去重操作。

**说明**

i. 支持一次选择多个topic文件进行上传。 ii. 请上传csv格式文件，文件模板可参考导出的topic文件。
3. 选择需要上传的topic后，单击**确定**。
消息队列

**导出**

1. 在**Topic****管理**页签，勾选想要导出的Topic，单击右上方的下载图标
。

**说明**

不勾选任何Topic并点击下载图标时，将默认导出范围为全部Topic。
2. 在**导出**窗口，选择**导出范围**和**需要导出的数据列**。

| 参数 | 说明 |
|---|---|
| 导出范围 | 可选择全部，或选中数据。 |
| 需要导出的数据列 | 默认勾选：topic、orderType、remark。 可选：类型。 |

3. 单击**确定**。

**更多信息**

如需使用API完成相关操作，请参见**《消息队列****RocketMQ****版开发指南》**的相关内容。

#### Group管理

创建完实例和Topic后，您需要为消息的消费者（或生产者）创建客户端ID ，即Group ID。本文介绍如何在RocketMQ控制台上创建、查看以及删除Group ID。

**前提条件**

您已创建了RocketMQ实例，详细信息请参见创建实例。

**背景信息**

Group表示一类Producer或Consumer，这类Producer或Consumer通常生产或消费同一类消息，且消息发布或订阅的逻辑一致。使用RocketMQ进行消息收发，您需要创建Group ID用于标识同一类生产者实例或者同一类消费者实例。 Group ID和Topic的关系是N∶N，即一个消费者可以订阅多个Topic，同一个Topic也可以被多个消费者订阅；一个生产者可以向多个Topic发送消息，同一个Topic也可以接收来自多个生产者的消息。

##### 使用说明

Group ID不能跨实例使用，例如实例A中创建的Group ID不能在实例B中使用。 Group ID不能跨协议使用，RocketMQ支持使用HTTP协议和TCP协议的SDK收发消息。如果您创建 Group ID时选择的协议为TCP协议，则该Group ID标识的客户端只能用于TCP协议的SDK收发消息，不能用于HTTP协议的SDK收发消息。 对于子账号创建的消费者Group ID或存量CID，该子账号及其主账号有使用权限。 对于主账号创建的消费者Group ID或存量CID，该主账号下的子账号无使用权限。 存量Producer ID和Consumer ID与Group ID的使用变更，请参见产品更新说明。

**创建Group ID**

消息队列
1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**Group****管理**页签。
5. 选择Group ID的协议类型。
若您使用TCP协议的SDK收发消息，需要创建TCP协议类型的Group ID，请单击**TCP** **协议**页签。 若您使用HTTP协议的SDK收发消息，需要创建HTTP协议类型的Group ID，请单击**HTTP** **协议**页签。
6. 单击**创建** **Group ID**，在**创建** **Group ID**对话框设置相关参数，然后单击**确定**。

| 参数 | 说明 |
|---|---|
| Group ID | 设置Group ID。 Group ID只能包含英文、数字、 短横线（-）和下划线（ ）。 _ 长度限制在4～64个字符之间。 Group ID 一旦创建，则无法修改。 新建Group ID不能与已存在的Topic名称或Group ID完全一致。 |
| 最大重试次数 | 设置普通消息的最大重试次数，范围为1至16。若此项留空，默认值为 16。 说明若客户端也设置了最大重试次数，则以客户端设置的最大重试次数为准；如客户端未设置最大重试次数，则以此处设置的最大重试次数为准。 |
| 描述 | 设置Group描述。 |

**说明**

Group ID 既可用于生产者，标识同一类 Producer 实例（Producer ID），又可用于消费者， 标识同一类 Consumer 实例（Consumer ID）； 同一个 Group ID 不可以共用于 TCP 协议和 HTTP 协议，需要分别申请。

**查看Group ID信息**

在**实例详情**页面，单击**Group****管理**页签，即可查看该实例下所有Group ID的基本信息，包括创建时间、权限、描述、最近使用时间和可执行操作，如订阅关系、消费者状态和示例代码等。

**删除Group ID**

**重要**

删除Group ID后，由该Group ID标识的生产者和消费者客户端将在客户端发起重新连接时认证失败， 已连接生产者和消费者不受影响。 消息队列
1. 在Group ID列表，找到您需要删除的目标Group ID，在其**操作**列单击
图标，然后在下拉列表中单击删除。
2. 请仔细阅读弹出的**确认信息**对话框的内容，确认无误后，单击**确定**。

**单实例Group导入/导出**

**导入**

1. 在**Group****管理**页签，单击**导入**。
2. 在**导入****Group**窗口，单击**上传文件**。请上传csv格式文件，文件模板可参考导出的group文件。
3. 单击**确定**。

**导出**

1. 在**Group****管理**页签，单击右上方的下载图标
。
2. 在**导出**窗口，选择**导出范围**和**需要导出的数据列**。
3. 单击**确定**。

**更多信息**

如需使用API完成相关操作，请参见《RocketMQ开发指南》的相关内容。

### 网络管理

#### 查看接入点信息

**前提条件**

您已创建了RocketMQ实例，详细信息请参见创建实例。

**操作步骤**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**网络管理**页签。
5. 即可查看实例的**TCP** **协议客户端接入点**和**HTTP** **协议客户端接入点**信息。

**重要**

接入点信息包含敏感信息，请根据现场网络环境，注意网络安全防护。

#### 绑定VPC

RocketMQ支持为指定的实例绑定多个VPC并提供Single Tunnel VPC接入点。您可以为不同业务分配不同的VPC接入点，实现更细粒度的访问控制。本文介绍如何在RocketMQ控制台为指定实例绑定VPC以及解除绑定的VPC。 消息队列

**背景信息**

RocketMQ实例默认提供一个HTTP协议和一个TCP协议的Any Tunnel类型接入点，Any Tunnel的VPC环境都可以通过该接入点访问RocketMQ。您可以通过绑定Single Tunnel类型的VPC为实例划分更多的接入网络，绑定VPC后系统会自动分配一个Single Tunnel的VPC接入点，只有在指定VPC网络环境中才能通过该接入点访问RocketMQ实例。通过绑定Single Tunnel的VPC，可根据业务进行网络侧的隔离，获取更精确的网络访问控制。

**前提条件**

创建RocketMQ实例。具体操作，请参见创建实例。 创建专有网络。 具体操作，请参见**《专有网络****VPC****用户指南》**手册的**《创建专有网络》**章节。 创建交换机。 具体操作，请参考**《专有网络****VPC****用户指南》**手册的**《创建交换机》**章节。

**注意事项**

绑定VPC功能是在已存在Any Tunnel网络的基础上附加的网络操作，Any Tunnel网络仍然可用。 建议由拥有管理员身份的用户统一管理和操作VPC，普通用户请勿随意操作，否则可能会导致业务无法访问RocketMQ实例。 绑定的VPC分配的接入点仅支持TCP协议的客户端接入。 RocketMQ绑定VPC后，只保证RocketMQ服务端在指定VPC网络中的连通能力，若您使用绑定VPC的接入点访问RocketMQ，请自行保证您的客户端在该VPC网络中的连通能力。 本文默认绑定VPC的IPv4网段，如需绑定VPC的IPv6网段，请参考绑定VPC的IPv6网段。
1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**网络管理**页签。
5. 在**网络管理**页签单击**绑定****VPC**。
6. 在弹出的**绑定****VPC**对话框中设置相关参数，然后单击**确定**。

**说明**

本文默认绑定VPC的IPv4网段，如需绑定VPC的IPv6网段，请参考绑定VPC的IPv6网段。 消息队列您需要设置的参数及说明如下表所示。

| 参数 | 说明 |
|---|---|
| MQ集群名 | 当前RocketMQ实例所属的集群名称。该参数值由系统自动获取并填充，您无需输入。 |
| 实例 | 当前RocketMQ实例的ID。该参数值由系统自动获取并填充，您无需输入。 |
| VPC ID | 在下拉列表中选择您要给当前RocketMQ实例所绑定的VPC。 |
| 交换机 | 在下拉列表中选择待绑定的VPC所关联的交换机。 |
| VPC NAME | 输入您绑定的VPC名称，用于区分业务，建议按照业务语义进行设置。 |

7. 绑定完成后，您可以在**网络管理**页签的VPC列表中查看到已绑定的VPC信息，包括**可用区**、**MQ****集群**
名、**Endpoint**（绑定VPC后分配的实例接入点）、**VPC** **名称**、**VPC ID**、**VSwitch ID**（VPC所绑定的交换机）。
8. 您还可以单击指定VPC的**操作**列的**VPC** **实例列表**，查询该VPC被哪些RocketMQ实例所绑定。
消息队列

**解除绑定**

**重要**

解除绑定后，指定的VPC访问地址将失效，无法使用该VPC地址访问RocketMQ实例，请谨慎操作。 一个集群下多个实例绑定相同的VPC，若要彻底解除该VPC地址的访问，请将集群下所有已绑定该VPC的实例全部解除绑定。
1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**网络管理**页签。
5. 在VPC列表中，找到需要解绑的VPC，在其**操作**列单击**解除绑定**。
6. 在弹出的**解除绑定**对话框中仔细确认提示信息然后单击**确定**。

#### 管理VPC

本文介绍如何管理已绑定的VPC。

**前提条件**

您已为消息队列 RocketMQ版实例绑定了VPC。您可单击**网络管理** > **绑定****VPC**为消息队列 RocketMQ
1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**网络管理**页签。
5. 在**网络管理**页面，查看实例已绑定VPC的**可用区**、**MQ****集群名**、**Endpoint**、**VPC** **名称**、**VPC**
**ID**、**VSwitch ID**信息。
消息队列
6. （可选）如需解绑VPC，可单击目标VPC右侧**操作**列的**解除绑定**，仔细阅读**解除绑定**弹窗内的信息后，单
击**确定**。
7. （可选）如需查看VPC实例列表，可单击目标VPC右侧**操作**列的**VPC** **实例列表**以查看相关信息，包括实
例、**VPC****名称**、**VPC ID**、**交换机**。

#### 绑定VPC的IPv6网段

**操作步骤**

**开启 IPv6 绑定开关**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏，选择**平台运维** **> UniConsole****管控研发平台**。
3. 单击左侧菜单栏**产品列表**。
4. 在**产品列表**页面的搜索框内输入 `rocketmq` ，单击**搜索**。
5. 单击**rocketmq**右侧**操作**列的**开关列表**，进入**rocketmq** **开关列表**页面。
6. 在**rocketmq** **开关列表**页面，找到**开关****ID**为**useIpv6**的开关，单击右侧**操作**列**修改开关状态**。
7. 在**查看功能开关初始状态**窗口，开启**当前值**开关。
1. 开启**useIpv6**开关后，重新登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**网络管理**页签。
5. 单击界面的提示链接，并按照操作指引完成云资源访问授权。
6. 在**网络管理**页签单击**绑定****VPC**。
消息队列
7. 在弹出的**绑定****VPC**对话框中设置如下参数，然后单击**确定**。

| 参数 | 说明 |
|---|---|
| MQ集群名 | 当前RocketMQ实例所属的集群名称。该参数值由系统自动获取并填充，您无需输入。 |
| 实例 | 当前RocketMQ实例的ID。该参数值由系统自动获取并填充，您无需输入。 |
| 网络类型 | 可选ipv4或ipv6。 |
| VPC ID | 在下拉列表中选择您要给当前RocketMQ实例所绑定的VPC。 |
| 交换机 | 在下拉列表中选择待绑定的VPC所关联的交换机。 |
| VPC NAME | 输入您绑定的VPC名称，用于区分业务，建议按照业务语义进行设置。 |

8. 绑定完成后，您可以在**网络管理**页签的VPC列表中查看到已绑定的VPC信息，包括**可用区**、**MQ****集群**
名、**Endpoint**（绑定VPC后分配的实例接入点）、**VPC** **名称**、**VPC ID**、**网络类** 型（**ipv4**或**ipv6**）、**VSwitch ID**（VPC所绑定的交换机）。

### 查看消费者状态

RocketMQ控制台为您提供了查看消费者状态的功能，帮助您在消息消费出现异常时进行问题排查，初步诊断异常原因。通过该功能，您可以查看Group ID综合信息和Group ID下单个消费端信息，包括在线状态、 订阅关系、消费TPS 、消息堆积量和线程堆栈信息等，本节介绍具体查看步骤。

**背景信息**

通常发生消息消费异常的原因会比较复杂，单纯依靠在控制台查看消费者状态还不足以排查问题，这时就需要结合日志分析和业务场景分析等操作进行进一步排查。

**应用场景**

消费者状态查询经常被应用于以下两个故障排查场景。 现象：在**消费者状态**面板，看到Group ID的**订阅关系是否一致**一栏显示否。 堆积告警现象：在**消费者状态**面板，看到Group ID的**堆积量**一栏的值较大。 处理：消费堆积的告警处理方法，请参见消息堆积。

**查看Group ID综合信息**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
消息队列
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**Group****管理**页签。
5. 找到要查看的Group ID，单击其右侧**操作**列中的**消费者状态**。
打开的**消费者状态**页面的字段说明如下。 表 1. 字段说明

| 字段 | 说明 |
|---|---|
| Group ID | 显示该Group ID。 |
| 消费模式 | 显示消费模式。 |
| 订阅关系是否一致 | 显示是否该Group ID下多个消费者实例的订阅关系一致。订阅关系一致的概念请参见订阅关系一致 。 |
| 实时消费速度 | 该Group ID下消费者实例群组接收消息的总TPS，单位为“条/秒”。 |
| 实时消息堆积量 | 该Group ID下消费者实例群组的未消费消息的总量。 |
| 最近消费时间 | 该Group ID下消费者实例群组最近一次消费消息的时间。 |
| 消息延迟时间 | 该Group ID下消费者实例群组最早的一条未消费消息的生产时间与当前时间的差值。 |
| 是否在线 | 只要该Group ID下有一个消费者实例在线，就显示是， 此时您可以看到页面下方的连接信息区域显示了在线的消费者实例信息；若该Group ID下所有消费者实例都不在线，则显示否且连接信息区域无信息显示。 |

您也可以单击右上角**刷新**按钮，刷新消费者状态信息。

**查看Group ID下单个消费端信息**

1. 若此时该Group ID的在线状态为**在线**，则在**消费者状态**页面的**连接信息**区域您可以查看此时在线的每个
消费者实例的具体信息，包括客户端ID、宿主机IP/公网IP、当前进程ID和消息堆积量等。
2. 除了上述信息，若您还想查看关于某个消费者实例的更多详细信息，可以在其右侧**操作**列的**详细说明**，单
击**详细信息**查看更多详细信息，包括消费线程数、消费启动时间、订阅关系和消费统计数据等。
3. 如需查看某消费者实例当前进程的堆栈信息，找到需查看堆栈信息的消费者实例，单击其所在行右侧操
作列的**堆栈信息**。

### 重置消费位点

您可通过重置消费位点，按需清除堆积的或不想消费的消息后再开始消费，或直接跳转到某个时间点消费该时间点之后的消息（不论是否消费过该时间点之前的消息）。 消息队列

**背景信息**

目前不支持指定Message ID、Message Key和Tag来重置消息的消费位点。

**操作步骤**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**Group****管理**页签。
5. 找到需要重置消费位点的Group ID，在其所在行的**操作**列中单击
图标，然后在下拉列表中单击**重置消**
**费位点**。
6. 在**重置消费位点**对话框中，在**Topic**下拉框中选择相应的Topic，然后按需选择以下**重置类型**。
**清除所有堆积消息，从最新位点开始消费**：若选择此项，该Group ID在消费该Topic下的消息时会跳过
当前堆积（未被消费）的所有消息，从这之后发送的最新消息开始消费。 对于程序返回“reconsumeLater”，即走重试流程的这部分消息来说，清除无效。
**按时间点进行消费位点重置**：选择该选项后会出现时间点选择的控件。请选择一个时间点，在这个时间
点之后发送的消息才会被消费。 可选时间范围中的起始和终止时间分别是该 Topic 中储存的最早的和最晚的一条消息的生产时间。不能选择超过可选时间范围的时间点。
7. 单击**确定**以执行消费位点重置。

### 消息查询

#### 消息查询概述

当您遇到消息消费问题时，可通过查询具体发送的消息内容来进行排查。RocketMQ提供了三种消息查询方式，分别为按Message ID查询、按Message Key查询，以及按Topic查询。 表 1. 查询方式对比

| 查询方式 | 查询条件 | 查询类别 | 说明 |
|---|---|---|---|
| 按Message ID 查询 | Topic+Messag e ID | 精确查询 | 根据Topic和Message ID可以精确定位任意一条消息，获取消息的属性。 |
| 按Message Key查询 | Topic+Messag e Key | 模糊查询 | 根据Topic和Message Key可以匹配到包含指定Key的最近 64条消息，建议消息生产方为每条消息设置尽可能唯一的 Key，以确保相同的Key的消息不会超过64条，否则消息会漏查。 |
| 按Topic查询 | Topic+时间段 | 范围查询 | 根据Topic和时间范围，批量获取符合条件的所有消息，查询量大，不易匹配。 |

消息队列推荐您按照以下流程查询消息： 图 1. 消息查询流程

#### 查询消息

本文介绍通过控制台使用三种方法来查询消息的操作步骤。

**操作步骤**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**消息查询**页签。
5. 在**消息查询**页签，您可单击以下任一页签，然后按页面提示输入相应信息，再单击**查询**按钮来查询消息。

**按Message ID查询**

按Message ID查询消息属于精确查询，您输入Topic和Message ID即可精确查询到任意一条消息。因此，为了尽可能精确地查询，建议在发送消息成功后将Message ID信息打印到日志中，方便问题排查。

```
SendResult sendResult = producer.send(msg); String msgId = sendResult.getMessageId();
```

**按Message Key查询**

RocketMQ根据您设置的 Message Key建立消息的索引信息，当您输入Topic和Message Key进行查询时，RocketMQ根据该索引即可匹配相关的消息返回。 消息队列

**重要**

按Message Key查询消息，请注意以下几点： 按Message Key查询的条件是用户设置的Message Key属性。 按Message Key查询仅仅返回符合条件的最近64条消息，因此建议您尽可能保证设置的 Key是唯一的，并具有业务区分度。 设置Message Key的方法如下：

```
Message msg = new Message("Topic","*","Hello MQ".getBytes()); /**
```

* 对每条消息设置其检索的`Key`，该`Key`值代表消息的业务关键属性，请尽可能全局唯一。
* 以方便您在无法正常收到消息情况下，可通过`RocketMQ`控制台查询消息。不设置也不会影响消息正常收发。
`*/`

```
msg.setKey("TestKey"+System.currentTimeMillis());
```

**按Topic查询**

按Topic查询一般用在Message ID和Message Key都无法获得的情况下，根据Topic和消息的发送时间范围，批量获取该时间范围内的所有消息，然后再找到关心的数据。

**重要**

按Topic查询消息，请注意以下几点： 按Topic查询属于范围查询，获取Topic下符合时间条件的所有消息，消息量大，建议尽量缩短查询区间。 按Topic查询数据量大，采用分页展示。

#### 查询结果说明

本文对消息查询的结果进行说明。 您可以在控制台的**消息查询**页签查看查询到的消息。 直接显示的信息包含**Message ID**、**Tag**、**Key**和**存储时间**。此外，您还可以在每一行消息的**操作**列下载

**消息详情**

**投递状态**

其中，**消息详情**中的**投递状态**是RocketMQ根据各个Group ID的消费进度计算出的结果，投递状态的信息参见消息投递状态。

**说明**

**投递状态**仅仅是根据消费进度估算的结果，如果需要详细的消费信息，请使用**消息轨迹**工具查询。消息
表 1. 消息投递状态

| 投递状态 | 可能的原因 |
|---|---|

消息队列

| 已订阅，消息至少已被消费一次 | 该Group ID已经正常消费过这条消息。 |
|---|---|
| 已订阅，但消息被过滤表达式过滤，请查看Tag | 该消息的Tag不符合消费方的订阅关系，消息被过滤，可以在控制台进入Group管理，然后单击该Group ID的操作列的消费者状态查询订阅关系。 |
| 已订阅，但消息未被消费 | 该Group ID订阅了该消息，但还未消费，有可能是消费过慢，或者消费出现异常导致阻塞。 |
| 已订阅，但Consumer当前不在线，请通过消息轨迹功能进行精确查询 | 该Group ID订阅了该消息，但是不在线，请检查消费者端应用不在线的原因。 |
| 未知异常 | 出现未收录异常，请联系技术支持。 |

**消费验证**

在**消息详情**窗口内，RocketMQ还提供了**消费验证**功能。该功能可以将指定消息推送给指定的在线客户端， 以检测客户端消费该消息的逻辑和结果是否符合预期。

**重要**

消费验证功能仅仅适用于验证客户端的消费逻辑是否正常，并不会影响正常的接收消息流程，因此消息的消费状态等信息在单击消费验证后并不会改变。

### 消息轨迹

#### 消息轨迹概述

消息轨迹是指一条消息从生产者发送到RocketMQ服务端，再到消费者进行消费处理，整个过程中的各个相关节点的时间、状态等数据汇聚而成的完整链路信息。该轨迹可作为生产环境中排查问题时强有力的数据支持。本文介绍消息轨迹的使用场景、查询步骤以及查询结果的参数说明。

**消息轨迹数据**

RocketMQ系统中，一条消息的完整链路包含生产者、服务端、消费者三个角色，每个角色在处理消息的过程中都会在轨迹链路中增加相关的信息，将这些信息汇聚在一起即可获取任意消息当前的状态，涉及的数据如下图所示： 图 1. 消息轨迹数据消息队列

**使用场景**

在生产环境的消息收发不符合预期时，您可使用消息轨迹工具进行问题排查。通过消息的属性（Message ID、Message Key、Topic）搜索相关的消息轨迹，找到消息的实际收发状态，帮助诊断问题。

##### 使用说明

消息轨迹的使用不会增加额外的接入成本。所有类型的消息正常发送后，即可根据消息的属性在RocketMQ 控制台查询到消息的发送轨迹，但消费轨迹需要注意以下几点： 表 1. 消息轨迹查询规则

| 消息类型 | 查询说明 |
|---|---|
| 普通消息 | 消息发送之后有发送轨迹，未消费时显示尚未消费。消费后会展示投递和消费信息。 |
| 顺序消息 | 消息发送之后有发送轨迹，未消费时显示尚未消费。消费后会展示投递和消费信息。 |
| 定时和延时消息 | 如果当前系统时间没有到达指定消费的时间，您可查询到轨迹，但查询不到消息。 |
| 事务消息 | 事务未提交时，您可查询到轨迹，但查询不到消息。 |

**使用示例**

假设您根据业务日志里的信息判断一直没有收到某条消息，则可以参照以下步骤，利用消息轨迹来排查该问题。
1. 收集疑似有问题的消息信息，包括Message ID、Message Key、Topic以及大概的发送时间范围。
2. 进入RocketMQ控制台，根据已有的信息创建查询任务，查询相关消息的轨迹。
3. 查看结果，并分析、判断原因。
消息队列如果轨迹显示**尚未消费**，则可以去**Group** **管理**页签查看消费者状态，确认消息是否堆积而导致尚未消费。 如果发现已经消费，请根据消费端的信息，找到对应的客户端机器和时间，登录客户端机器查看相关日志。

#### 查询消息轨迹

使用消息轨迹不会对业务方增加额外的接入成本，仅需要确保客户端SDK版本支持该特性。正常收发消息后，便可以在RocketMQ控制台上进行查询。

**前提条件**

请确保您的SDK版本支持消息轨迹功能，具体说明如下： C/C++：v1.1.2及以上版本 .NET：v1.1.2及以上版本 Node.js：v1.0.2及以上版本 Java、Go、Python、C#、C++以及PHP：v1.0.1及以上版本

**操作步骤**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**消息轨迹**页签。
5. 单击**创建查询任务**。
6. 在弹出的**创建查询任务**对话框中，按需选择查询条件并按提示输入信息，单击**确定**完成创建。

**重要**

查询时，尽可能精确地设置**时间范围**，以便缩小查询范围，提高查询速度。 消息轨迹查询功能支持三种查询方式，请根据对应方式输入相应的查询条件，新建查询任务。

| 查询方式 | 输入参数 | 说明 |
|---|---|---|
| 按 Message ID 查询 | 需要输入消息唯一的Message ID、Topic以及消息的大致发送时间范围。 | 该方式属于精确查询，速度快，精确匹配，推荐使用。 |
| 按 Message Key 查询 | 需要输入消息的Message Key和Topic以及大致发送时间范围。 | 该方式属于模糊查询，最多查询 1000条轨迹。仅适用于您没有记录 Message ID但是设置了Message Key，同时Message Key具有区分度的情况。 |

消息队列

| 按 Topic 查询 | 仅需输入Topic和大致发送时间范围，进行批量查询。 | 该方式属于范围查询，适用于没有上述Message ID和Message Key，而且消息量比较小的场景。 因为时间范围内消息很多，且不具备区分度，所以不推荐使用。 |
|---|---|---|

创建查询任务后，即可在**消息轨迹**页签下查看刚创建的查询任务，且**任务状态**显示为**查询中**，说明暂不能查看消息轨迹。
7. 在消息轨迹的任务列表的右上角，单击刷新按钮，直到状态切换至**查询完成**。单击任务列表**操作**列的详
情可查看到轨迹的简要信息。 如果发现没有结果，请确认输入的查询信息是否正确。 如果查询到轨迹信息，可以查看轨迹的简要信息，如Message ID、Tag、Message Key、发送状态、 发送时间和消费状态。
8. 单击**查看轨迹**即可查看完整的链路图。
消息链路图包含3个部分： 生产者信息 Topic信息消费者信息对于Message Key和Topic查询方式，如果匹配到多条轨迹，可以进行上下翻页，查看比对轨迹数据。

#### 消息轨迹状态说明

本节介绍消息轨迹查询页面中涉及到的名词概念和状态信息。 表 1. 消息轨迹名词解释

| 链路部分 | 字段 | 说明 |
|---|---|---|
| 生产者 | 发送端 | 发送端IP地址。 |
|  | 发送时间 | 消息从发送端发送时的客户端时间戳。 |
|  | 发送耗时 | 生产者调用Send方法发送消息的毫秒耗时。 |
|  | 状态 | 发送状态。 |
|  | Topic | Topic名称。 |
|  | Key | 阿里云AccessKey ID。 |

| 消息队列 |  |  |
|---|---|---|
| Topic |  |  |
|  | Tag | 可理解为Gmail中的标签，对消息进行再归类，方便Consumer指定过滤条件在RocketMQ服务器过滤。 |
|  | Region | 消息存储的Region信息，或者消费方机器所在的Region信息。 |
| 消费者 | 第一次 | 消费状态。 |
|  | IP | 消费者IP地址。 |
|  | 耗时 | 消息推送到客户端之后执行 consumeMessage方法的耗时。 |
|  | 投递时间 | 客户端执行consumeMessage方法开始消费消息时的时间戳。 |

表 2. 发送/消费状态

| 发送/消费状态 | 状态字段 | 说明 |
|---|---|---|
| 发送状态 | 发送成功 | 消息发送成功，服务端已经存储成功。 |
|  | 发送失败 | 消息发送失败，服务端没有存储消息，需要重试。 |
|  | 消息定时中 | 该消息是定时或者延时消息，且尚未到达投递时间。 |
|  | 事务未提交 | 该消息是事务消息，且尚未提交状态。 |
|  | 事务回滚 | 该消息是事务消息，并且已经回滚。 |
|  | 全部成功 | 该消息的所有投递都已成功消费。 |
|  | 部分成功 | 该消息投递中存在消费失败的情况， 或消费失败并重试成功的情况。 |
|  | 全部失败 | 该消息的所有投递都消费失败。 |

消息队列

| 消费状态 |  |  |
|---|---|---|
|  | 尚未消费 | 该消息尚未投递给任何消费方。 |
|  | 消费结果未返回 | 消费消息的方法尚未返回结果，或者被中断，导致本次消费结果未传回服务端。 |
|  | 消费成功 | 该消息已被成功消费。 |
|  | 消费失败 | 消费消息的方法主动返回失败标志， 或者是消费方法抛异常。 |

### 死信队列

死信队列用于处理无法被正常消费的消息，即死信消息。本文介绍如何查询、导出和重新发送进入死信队列的死信消息，以便您按需管理死信消息，避免消息漏处理。

**背景信息**

当一条消息初次消费失败，消息队列RocketMQ版会自动进行消息重试；达到最大重试次数后，若消费依然失败，则表明消费者在正常情况下无法正确地消费该消息，此时，消息队列RocketMQ版不会立刻将消息丢弃，而是将其发送到该消费者对应的特殊队列中。 在消息队列RocketMQ版中，这种正常情况下无法被消费的消息称为死信消息（Dead-Letter Message），存储死信消息的特殊队列称为死信队列（Dead-Letter Queue）。

**特性说明**

死信消息具有以下特性： 不会再被消费者正常消费。 有效期与正常消息相同，均为 7 天，7 天后会被自动删除。因此，请在死信消息产生后的 7 天内及时处理。 死信队列具有以下特性： 一个死信队列对应一个 Group ID，而不是对应单个消费者实例。 如果一个 Group ID 未产生死信消息，消息队列RocketMQ版不会为其创建相应的死信队列。 一个死信队列包含了对应 Group ID 产生的所有死信消息，不论该消息属于哪个 Topic。

**查询死信消息的方式**

| 查询方式 | 查询条件 | 查询类别 | 说明 |
|---|---|---|---|
| 按 Group ID 查询 | Group ID+时间段 | 范围查询 | 根据 Group ID 和时间范围，批量获取符合条件的所有消息；查询量大，不易匹配。 |

消息队列

| 按 Message ID 查询 | Group ID+Message ID | 精确查询 | 根据 Group ID 和 Message ID 可以精确定位任意一条消息。 |
|---|---|---|---|

**按 Group ID 查询死信消息**

您可以根据 Group ID 和死信消息产生的时间范围，批量查询该 Group ID 在某段时间内产生的所有死信消息。

**重要**

死信消息产生的时间是指一条消息在投递重试达到最大次数后被发送到死信队列的时间。
1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**死信队列**页签。
5. 单击按 **Group ID** **查询**页签。
6. 在**GroupId**的下拉列表中选择想要查找的 Group ID。
7. 单击**查询时间范围**右侧的时间选择框，选择想要查询的时间范围的起止日期和具体时间点。
8. 单击**查询**按钮。页面中会显示所有符合以上条件的死信消息。
9. 找到想要查看的死信消息，单击其**操作**列中的**查看详情**查看该消息的详细信息，包括其基本属性、**消息体**
**大小**和**投递状态**。

**按 Message ID 查询死信消息**

按 Message ID 查询消息属于精确查询。您可以根据 Group ID 与 Message ID 精确查询到任意一条消息。
1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**死信队列**页签。
5. 单击按 **Message ID** **查询**页签。
6. 在**GroupId**的下拉列表中选择想要查找的 Group ID。
7. 在**Message ID**的输入框中输入想要查找的消息的 Message ID。
8. 单击**查询**按钮。页面中会显示所有符合以上条件的死信消息。
9. 找到想要查看的死信消息，单击其**操作**列中的**查看详情**查看该消息的详细信息，包括其基本属性、**消息体**
**大小**和**投递状态**。

**导出死信消息**

若您暂时无法处理死信消息，可以在消息队列RocketMQ版控制台上将其导出，以免超过有效期。 消息队列RocketMQ版控制台提供对死信消息的单条导出和批量导出功能。导出的文件格式为 CSV。 导出的消息内容如下表所示。 消息队列

| 消息字段 | 字段含义 |
|---|---|
| instanceId | 实例的 ID。 |
| topic | 消息所属的 Topic。 |
| msgId | 消息的 ID。 |
| bornHost | 消息产生的地址。 |
| bornTimestamp | 消息产生的时间。 |
| storeTimestamp | 死信消息产生的时间。 |
| reconsumeTimes | 消费失败的次数。 |
| properties | 消息属性；JSON 格式。 |
| body | 消息体；base64 编码格式。 |
| bodyCRC | 消息体 CRC。 |

单条导出在消息队列RocketMQ版控制台按任意方式查询到死信消息后，在某条死信消息的**操作**列，单击**导出**，导出该条死信消息。 批量导出在消息队列RocketMQ版控制台按 Group ID 查询到死信消息后，勾选目标死信消息，然后单击页面下方的**批量导出**按钮，导出所有勾选的死信消息。

**重新发送死信消息**

一条消息进入死信队列，意味着某些因素导致消费者无法正常消费该消息，因此，通常需要您对其进行特殊处理。排查可疑因素并解决问题后，您可以在消息队列RocketMQ版控制台重新发送该消息，让消费者重新消费一次。

**重要**

死信消息被重新发送后，仍会在死信队列中存储三天，到期后再删除。 单条重发在消息队列RocketMQ版控制台按任意方式查询到死信消息后，在某条死信消息的**操作**列，单击**重新发** 送，重发该条死信消息。 批量重发消息队列在消息队列RocketMQ版控制台按 Group ID 查询到死信消息后，勾选目标死信消息，然后单击页面下方的**批量重发**按钮，重新发送所有勾选的死信消息。

### 资源报表

#### 资源报表概述

本文介绍如何使用资源报表对消息生产和消费信息进行查询。 资源报表是统计消息生产和消费数据的功能。通过该功能，您可查询以下数据： 按Topic查询：指定时间范围内发送至某Topic的消息总量或TPS。 按实例查询：指定时间范围内发送至某实例下所有Topic的消息总量或TPS。 按Group ID查询：指定时间范围内某Topic投递至某Group ID的消息总量或TPS。 按实例查询：指定时间范围内投递至实例下所有Group ID的消息总量或TPS。

#### 查看消息生产数据

可供查看的消息生产数据是在一定时间范围内某个Topic或指定实例下的所有Topic从Broker接收的消息的总量或者TPS。

**操作步骤**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**资源报表**页签。
5. 在**资源报表**页签，单击**消息生产**页签。
6. 在**资源类型**的下拉框中选择按照哪种资源类型查询消息生产数据，并指定其他信息，然后单击**查询**。

| 参数 | 说明 |
|---|---|
| 资源类型 | 分为实例和Topic。 选择实例查询指定实例下所有Topic接收的消息总量或TPS； 选择Topic查询指定Topic接收的消息总量或TPS。 |
| 当前实例 | 当资源类型为实例时显示，默认为当前实例的名称和ID，您无需输入。 |
| Topic | 当资源类型为Topic时显示，查询当前实例下指定Topic的消息生产数据。 |

消息队列

| 采集类型 | 分为总量和TPS。 总量提供每个周期内Topic接收的消息总量； TPS提供每个周期内Topic接收消息的平均TPS。 |
|---|---|
| 采集周期 | 包括1分钟、10分钟后、30分钟、1小时。采集周期决定了数据采集的时间间隔，周期越短，采集点越密集，消息消费数据越详细。 |
| 时间范围 | RocketMQ最多可以提供最近三天之内的消息的生产查询。 |

查询结果将以图表形式显示。

#### 查看消息消费数据

可供查看的消息消费数据是某个Topic在一个时间段内投递给某个Group ID的消息的总量或TPS。

**操作步骤**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**资源报表**页签。
5. 在**资源报表**页签，单击**消息消费**页签。
6. 在**资源类型**的下拉框中选择按照哪种资源类型查询消息消费数据，并指定其他信息，然后单击**查询**。

| 参数 | 说明 |
|---|---|
| 资源类型 | 分为实例和GroupId。 选择实例查询投递到指定实例下所有Group ID的消息总量或TPS； 选择GroupId查询指定Topic投递到指定Group ID的消息总量或TPS。 |
| 当前实例 | 资源类型为实例时显示，默认为当前实例的名称和ID，您无需输入。 |
| Group ID | 当资源类型为GroupId时显示，指定需要查询的Group ID。 |
| 采集类型 | 分为总量和TPS。 总量提供每个周期内投递给Group ID的消息总量； TPS提供每个周期内投递给Group ID的消息的平均TPS。 |
| 采集周期 | 包括1分钟、10分钟后、30分钟、1小时。采集周期决定了数据采集的时间间隔，周期越短，采集点越密集，消息消费数据越详细。 |

消息队列

| 时间范围 | RocketMQ最多可以提供最近三天之内的消息的消费查询。 |
|---|---|

查询结果以图表形式显示。

### 查看实例监控信息

在云监控中心，您可以通过查看监控图表，了解各实例的运行情况。本文介绍如何快速跳转到云监控查看实例监控信息。

**背景信息**

云监控中心提供了资源的实时监控、告警及通知服务，为您的产品和业务保驾护航。更多信息，请参见专有云文档中心《Apsara Uni-manager运营控制台用户指南》文档的**云监控****CMS** **用户指南** > **云监控****CMS**简介章节。

**操作步骤**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**监控**页签，查看目标实例的监控信息。

**说明**

您也可以单击**查看更多**，进入云监控CMS控制台查看更详细的实例监控信息。

| 项目 | 说明 |
|---|---|
| 监控粒度 | 实例监控粒度分为实例、Group、Topic和Topic&Group。 |
| 监控周期 | 您可以配置查看监控数据的时间段，即监控周期。取值范围： 按小时：1小时、3小时、6小时、12小时。 按天：1天、3天、7天、14天。 自定义：可以根据实际需要设置监控周期。支持快速选择近五分钟、近十分钟或近十五分钟。 |
| 监控指标 | 具体的监控指标说明，请参见专有云文档中心《Apsara Uni-manager运营控制台用户指南》文档的云监控CMS 用户指南 > 云产品监控 > 云监控指标说明章节。 说明默认展示各监控指标的平均值数据，你也可以根据实际需要修改为最大值或最小值数据。 |

### 查看实例操作日志

消息队列 RocketMQ实例的操作日志会详细记录每次操作的时间、地点及执行者，这些记录将被妥善存档。当您在管理或使用RocketMQ实例时遇到技术问题或故障，查阅这些操作记录将有助于快速定位问题的变更来源，从而提高故障排除的效率。此外，操作日志还可以用于评估故障的影响范围和责任认定等相关事项。

**说明**

1. 当前操作日志保存时长 7 天，如需调整，需管理员在配置-日志转存配置中操作。
2. 若通过转存设置延长保存时长，日志数据不会做前序时间数据补充。

**操作步骤**

1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**操作日志**页签。
5. 查看操作日志，默认会列出最近7天RocketMQ实例及其相关资源的所有操作记录。
您可以按**操作人**和**操作名称**等过滤条件进一步筛查出关心的操作记录。

**说明**

您也可以单击**操作**列的**操作详情**，在**操作详情信息**面板中查看更详细的日志信息。

### 管理账号授权

消息队列RocketMQ提供两种授权机制：跨云账号授权和RAM主子账号授权，可将Topic的发布和订阅权限授予其他阿里云账号（一级部门账号）或RAM用户（个人云平台账号）。

**注意事项**

基于安全访问控制原则，请优先采用子账号授权方式，尽量减少跨主账号之间的授权使用。 有命名空间的实例不支持在不同主账号之间进行授权。 消息队列

**跨云账号授权**

跨云账号授权指的是某阿里云账号授权给另一阿里云账号。具体操作步骤如下：
1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**Topic****管理**页签。
5. 在Topic列表中找到需要进行授权的Topic，单击其右侧**操作**列的**授权**。
6. 在**授权**窗口配置以下参数后，单击**确定**。

| 参数 | 说明 |
|---|---|
| Topic | 正在进行授权的Topic的名称，系统默认写入，您无需填写。 |
| 账号类型 | 此处选择主账号。 |
| 主账号ID | 输入被授权的阿里云账号ID。 |
| 授权类型 | 选择要授予该阿里云账号的权限，可选： 发布订阅发布和订阅 |

**RAM主子账号授权**

RAM主子账号授权指的是某阿里云账号授权给该账号所属的一个RAM用户。具体操作步骤如下：
1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**Topic****管理**页签。
5. 在Topic列表中找到需要进行授权的Topic，单击其右侧**操作**列的**授权**。
6. 在**授权**窗口配置以下参数后，单击**确定**。

| 参数 | 说明 |
|---|---|
| Topic | 正在进行授权的Topic的名称，系统默认写入，您无需填写。 |
| 账号类型 | 此处选择子账号。 |

消息队列

| 子账号名称 | 输入被授权的RAM用户的名称。 |
|---|---|
| 授权类型 | 选择要授予该RAM用户的权限，可选： 发布订阅发布和订阅 |

**说明**

被授权的RAM用户必须是该阿里云账号所属部门下的云平台账号。

**查看授权信息**

您可以在控制台查看每个Topic相关的授权记录和详细信息。具体操作步骤如下：
1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**Topic****管理**页签。
5. 在Topic列表中找到想要查看授权信息的Topic，单击其**操作**列的
图标，然后在下拉菜单中选择**查看授**
**权信息**，即可查看该Topic相关的授权操作记录和信息，包括**Topic**、**授权用户**、**授权类型**和**详细说明**。

**说明**

自己创建的Topic，无需给自己重复授权。 被授权的账号登录RocketMQ控制台后，可以查看被授权的Topic资源，但仍需创建Group ID，不能直接使用授权账号的Group ID。 被授权的Topic资源属于授权账号，因此被授权账号不可以对该Topic进行删除操作。 RAM主子账号授权方式中，被授权的RAM用户不可以创建Topic。 跨云账号授权方式中，被授权的阿里云账号可以创建Topic，但新创建的Topic和原授权的阿里云账号无关。

### 数据集成

#### Connector概述

RocketMQ提供全托管、免运维的Connector，用于RocketMQ和其他阿里云服务之间的数据同步。本文介绍Connector的功能描述、RocketMQ支持的Connector任务、使用说明以及功能优势。

**功能描述**

RocketMQ的Connector可实现RocketMQ和其他云服务的数据同步。RocketMQ的Connector包括以下两种类型： 如下图所示，RocketMQ为数据源，其他云服务为数据目标，Sink Connector可将RocketMQ的数据流消息队列出至其他云服务中。 如下图所示，其他云服务为数据源，RocketMQ为数据目标，Source Connector可将其他云服务的数据流入至RocketMQ中。

| Connector | 任务描述 | 文档 |
|---|---|---|
| MaxCompute Sink Connector | 将数据从RocketMQ导出至大数据计算服务MaxCompute。 | MaxCompute Sink Connector |

##### 使用说明

Connector运行时，会占用系统CPU、内存及I/O资源，以及数据源和数据目标的资源，请提前做好规格评估，确保资源充足。

**功能优势**

**业务无感知**

RocketMQ通过Connector和其他异构数据源进行消息同步时，业务链路可正常使用异步消息，业务无感知。

**配置简单易上手**

RocketMQ的Connector功能通过RocketMQ的控制台完成，全程操作可视化，配置无需额外复杂产品的支持。

#### MaxCompute Sink Connector

通过Connector可实现RocketMQ与其他阿里云服务之间的数据同步。本文介绍如何创建并部署 MaxCompute Sink Connector，将数据从RocketMQ实例的源Topic导入至MaxCompute的表中。

**前提条件**

RocketMQ：创建Topic。具体操作，请参见创建Topic。 大数据计算服务（MaxCompute）：创建表。具体操作，请参见大数据计算服务**《用户指南》**手册的**《创建表》**章节。 消息队列本文以创建名称为 `test_rocketmq` 的表为例，该表的建表语句如下：

**重要**

建表时，您可以根据您的需求自定义修改表的名称，但表的格式字段必须和以下内容保持一致。

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

)

```
PARTITIONED BY (
  pt STRING
);
```

##### 使用说明

Connector运行时，会占用系统CPU和存储资源，以及数据源和数据目标的资源，请提前做好规格评估，确保资源充足。
1. 登录RocketMQ控制台，在左侧导航栏单击**实例列表**。
2. 在**实例列表**页面顶部菜单栏中分别选择**组织**和**资源集**。
3. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页
面。
4. 在**实例详情**页面，单击**数据集成**页签。
5. 单击**MaxCompute Sink Connector**卡片。
6. 在**创建任务**配置向导中完成以下操作。
i. 在**配置基本信息**页签输入任务**名称**和**描述**，然后单击**下一步**。 ii. 在**配置数据源**页签，按需配置以下参数，然后单击**下一步**。

| 参数 | 描述 | 示例值 |
|---|---|---|
| 数据源 | 数据同步的源服务，固定为RocketMQ。 | RocketMQ |
| 实例 | RocketMQ的实例ID，即需要同步数据的源Topic所属实例的ID。 该参数值自动填充为您在步骤3中指定的实例ID，无需填写。 | MQ INST 1624605771445148 _ _ BfSh**** _ |
| Topic | RocketMQ的Topic名称，即指定将哪个Topic的数据发送到数据目标中。 | maxcompute sink input _ _ |

消息队列

| 消费初始位置 | 指定消息从源Topic中哪个消费位点开始往目标MaxCompute的表中同步。参数取值如下： 最早位点：表示Connector任务运行时，将从Topic中最早的消费位点开始同步消息数据。 最近位点：表示Connector任务运行时，将从Topic中的最新消费位点开始同步消息数据。 | 最早位点 |
|---|---|---|
| 过滤规则 | Connector任务支持按照Tag过滤消息数据。 若未设置过滤规则：指定的源 Topic中的所有消息都将被同步至目标源中。 若设置了过滤规则，则只同步指定源Topic中符合过滤规则的数据。 设置过滤规则时，您可以直接输入 Tag名称按Tag过滤。 例如您的消息Tag属性为 CartService，则直接输入 CartService ；如果需要过滤多个 Tag属性，则用双竖线（\|\|）隔开，例如 CartService\|\|Inventory\|\|Payment 。具体过滤方法请参见消息过滤。 | Cart\|\|Inventory\|\|Payment |
| 任务数 | 创建Connector任务的最大数量。 每个任务包含一个RocketMQ的消费者客户端，单个任务的消费性能 ≤3000 TPS。 取值范围：1～16的整数。 | 10 |
| 异常数据 Topic | 用于存储异常数据的 Topic，Connector会将转发失败的消息统一投递至该Topic中。 该参数无需填写，默认取值RocketMQ为当前Connector任务自动创建的Topic的名称。格式为connect-error-connector任务名称。 重要请勿删除RocketMQ为当前 Connector任务自动创建的异常数据Topic，删除 Connector任务时该Topic会被自动删除。 | connect-error-mqsink |

消息队列

| Connector Group ID | 用于消费Connector任务中同步消息数据的Group。 该参数无需填写，默认取值RocketMQ为当前Connector任务自动创建的Group。格式为 connect-connector任务名称。 重要请勿删除RocketMQ为当前 Connector任务自动创建的 Group，删除Connector任务时该Group会被自动删除。 | connect-mqsink |
|---|---|---|

iii. 在**配置目标源**页签，按需配置以下参数，然后单击**确定**。

| 参数 | 描述 | 示例值 |
|---|---|---|
| 目标源 | 数据同步的目标服务，固定为 MaxCompute。 | MaxCompute |
| MaxCompute表名 | MaxCompute的表名，即指定将数据源同步至MaxCompute的哪一个表中。 | test rocketmq _ |
| 分区粒度 | 将源数据写入MaxCompute的表中时，分区的切换频率。参数取值如下： 分钟：每分钟将数据写入一个新的分区。 小时：每小时将数据写入一个新的分区。 天：每天将数据写入一个新的分区。 | 分钟 |
| 连接地址 | MaxCompute服务的接入点。RocketMQ通过该接入点访问 MaxCompute服务。 获取方式，请参见大数据计算服务《开发指南》手册的《获取 Endpoint》章节。 | http://service.xxxx.shuguang. com/api |
| 工作空间 | MaxCompute的项目名称，即数据将被同步到的目标表所属项目的名称。 | connector test _ |

消息队列

| accessId | MaxCompute资源所属账号的AccessKey ID。 获取方式，请参见大数据计算服务《开发指南》手册的《获取 Accesskey》章节。 | j8geROUEAW1k**** |
|---|---|---|
| accessKey | MaxCompute资源所属账号的AccessKey Secret。 获取方式，请参见大数据计算服务《开发指南》手册的《获取 Accesskey》章节。 | AMx4ainrLWhT8jYUPHkdI4zY7 t**** |
| 重试次数 | 消息发送超时或异常时，可重新发送的最大次数。参数取值如下： 1 2 3 说明若达到重试次数消息还未发送成功，该消息将被投递至RocketMQ自动创建的异常数据Topic中。消息重试的更多信息，请参见《RocketMQ用户指南》的《消息重试》章节。 | 1 |
| TargetParams.超时时间 | 消息发送时的响应超时时间，若超过该参数设置的时长还未返回响应，消息将被重新投递。 参数取值：3000ms～ 30000ms，即3s～30s。 | 10 |

创建完成后，在**数据集成**页面的任务列表中可看到已创建的Connector，且状态为**待部署**。 Connector任务创建成功后，您需要部署该任务，部署成功后消息开始按照Connector任务中配置的规则进行同步。
1. 在**数据集成**页面的任务列表中，找到新创建的Connector任务，在其**操作**列单击**部署**。
2. 在弹出的**确认**对话框中，单击**确定**完成部署。
部署操作完成后，若任务状态显示为**待调度**或**部署中**，说明系统在调度后台资源执行部署任务。请稍等片刻，部署成功后任务状态会自动更新为**运行中**。
1. 在**数据集成**页面的任务列表中，找到待查询的Connector任务，在其**操作**列单击**详情**。
2. 在**任务详情**面板单击**概览**或**配置**页签。
消息队列若您暂时不希望某个Connector任务同步数据，您可以暂停该任务，暂停后该任务将立即停止同步数据；若

**重要**

Connector任务停止后将立即停止数据同步，重新恢复任务后，暂停期间产生的源数据不会被同步到数据目标。
1. 在**数据集成**页面的任务列表中，找到待暂停或恢复的Connector任务，在其**操作**列中单击**暂停**或**恢复**。
2. 在弹出的**确认**对话框中，单击**确定**。

**重要**

删除Connector任务后，该Connector指定的消息源到消息目标的数据同步将立即停止，请谨慎执行。
1. 在**数据集成**页面的任务列表中，找到待删除的Connector任务，在其**操作**列中单击**删除**。
2. 在弹出的**确认**对话框中，单击**确定**删除任务。
消息队列

## 消息路由

### Replicator

RocketMQ可通过Replicator消息路由功能进行集群间的数据消息同步，本文介绍如何配置Replicator消息路由任务。

**背景信息**

RocketMQ的Replicator消息路由功能常用于集群间的消息数据同步，通过路由规则动态规划消息的同步路径，使消息按照过滤条件从源节点同步到目标节点。实现跨集群、远距离、毫秒级消息实时同步，确保集群之间的数据一致性与完整性。 RocketMQ的Replicator消息路由功能的具体实现如下，以Topic维度进行单向同步，将源实例下指定的源 Topic的消息同步至目标实例下指定的目标Topic中。 更多信息，请参见消息路由。

**注意事项**

消息路由功能仅适用于有命名空间的实例。 消息路由不支持路由传递，例如集群A到集群B再到集群C，集群A的消息不会经过集群B再路由到集群C。 如有需要，请直接创建集群A到集群C的路由。 源Topic和目标Topic的消息类型需保持一致，如果源Topic是普通消息，则同步到的目标Topic也必须是普通消息。 创建路由任务的操作必须在目标集群所部署的生产环境中执行。例如集群A同步到集群B，则必须在集群B 的云环境中创建同步任务，消息源为集群A的信息，消息目标为集群B的信息。 同步的消息会占用源集群和目标集群的CPU、内存资源，以及目标集群的存储资源，请提前做好容量评估。

**前提条件**

已创建RocketMQ实例。具体操作，请参见创建实例。 已创建Topic。具体操作，请参见创建Topic。

**操作流程**

**步骤一：创建消息同步云**

创建路由任务前，需要先录入部署了RocketMQ集群的云环境的相关信息。包括RocketMQ服务端的接入点、域名、云环境所属账号的AK、SK等。RocketMQ将根据录入的云信息获取跨云访问RocketMQ资源的权限。

**步骤二：创建路由任务**

消息队列指定消息源和消息目标，设置过滤条件和同步位点等信息。

**步骤一：创建消息同步云**

1. 登录RocketMQ控制台。
2. 在左侧导航栏单击**消息路由** **> Replicator**。
3. 在**replicator**页面单击**云信息**页签，然后单击**创建消息同步云**。
4. 在弹出的**创建消息同步云**对话框中配置以下参数，然后单击**确定**。

**说明**

创建消息路由将占用消息集群的正常生产并消费消息的资源，请仔细做好扩容评估。

| 参数 | 说明 | 取值示例 |
|---|---|---|
| 云名称 | 消息同步云的名称，由您自定义输入。 说明云名称和MQ 实例 endpoint唯一确定一条多云信息，不允许重复。 云名称只能包含英文、数字、 短横线 （-）和下划线 （ ）。 _ 长度限制在3~64个字符之间。 | Center |
| AccessKey | 云环境所属账号的AccessKey ID。 请确保该账号角色为RocketMQ组织的管理员或具备实例和Topic读写权限的资源使用人。 获取Access Key，请参见《RocketMQ开发指南》手册的《获取AccessKey》章节。 | j8geROUEAW1k**** |
| 地域 | RocketMQ集群所部署的地域。 地域信息可登录RocketMQ控制台，在控制台上方的菜单栏中查看。 | cn-qingdao-****-d01 |
| Secret | 云环境所属账号的AccessKey Secret。 获取AccessKey Secret，请参见《RocketMQ开发指南》手册的《获取AccessKey》章节。 | AMx4ainrLWhT8jYUPHkdI4zY7t **** |

消息队列

| MQ 实例endpoint | RocketMQ服务的接入点。 获取RocketMQ的Endpoint，请参见本文中的参考信息。 | http://mq.server.****.com:808 0/rocketmq/nsaddr4client- internal |
|---|---|---|
| MQ API | RocketMQ控制台的访问接口。 参数格式为： http: {console.domain}/json 。 获取{console.domain}，请参见本文中的参考信息。 | http:mq.console.****.com/json |
| 备注 | 云环境信息的具体说明或备注，以作区分和记录。 | 中心节点 |

|  |  | http: |  |
|---|---|---|---|
|  | {console.domain}/json |  |  |

**步骤二：创建路由任务**

1. 登录RocketMQ控制台。
2. 在左侧导航栏单击**消息路由** **> Replicator**。
3. 在**replicator**页面单击**任务**页签，然后单击**创建任务**。
4. 在弹出的**创建任务**对话框中配置以下参数，然后单击**确定**。

| 参数 | 说明 |
|---|---|
| 消息源 | 消息同步云：选择需要同步消息的云名称。 源地域：RocketMQ集群所部署的地域。指定消息同步云后，该参数会自动关联，不需要输入。 源实例：选择需要同步的消息所属Topic的所在实例。 源Topic：选择需要同步的消息所属的Topic名称。 |
| 消息目标 | 消息同步云：选择消息将被同步到的同步云名称。 目标地域：RocketMQ集群所部署的地域。指定消息同步云后，该参数会自动关联，不需要输入。 目标实例：选择消息将被同步到的Topic所属实例。 目标Topic：选择消息将被同步到的Topic名称。 |
| 起始同步位点 | 指定消息从源Topic中哪个消费位点开始往目标Topic中同步。 默认为最大位点。即任务启动后，从最新写入源Topic的消息开始同步。 重要首次任务启动前，发送至源Topic中的消息不会同步至目标 Topic。 |

消息队列

| 过滤规则 | 若未设置过滤规则，指定的源Topic中的所有消息都将被同步至目标 Topic。 若设置了过滤规则，则只同步指定源Topic中符合过滤规则的消息。 设置过滤规则时，您可以直接输入Tag名称进行Tag过滤。 例如您的消息Tag属性为CartService，则直接输入 CartService ；如果需要过滤多个Tag属性，则用双竖线（\|\|）隔开，例如 CartService\|\|Inventroy\|\|Payment 。具体过滤方法请参见消息过滤。 |
|---|---|
| 描述 | 输入对该同步任务的具体描述或备注，以作区分和记录。 |

**修改云信息**

1. 在**replicator**页面单击**云信息**页签。
2. 在云信息列表中找到您需要修改的目标云信息，在其**备注**列单击
图标。
3. 在弹出的**修改描述**对话框中修改**备注，**然后单击**确定**。
4. 在弹出的提示对话框中仔细阅读提示信息并单击**确定**。

**删除云信息**

1. 在**replicator**页面单击**云信息**页签。
2. 在云信息列表中找到您需要删除的目标云信息，在其**操作**列单击**删除**。
3. 在弹出的提示对话框中仔细阅读提示信息并单击**确定**。

**启停路由任务**

1. 在**replicator**页面单击**任务**页签。
2. 在路由任务列表中找到您需要启停的任务，在其**操作**列单击**开始**启动任务，或单击**停止**暂停任务。

**修改路由任务**

**重要**

若您修改了任务的**过滤规则**，您需要先停止任务再启动任务，修改的内容才会生效。
1. 在**replicator**页面单击**任务**页签。
2. 在路由任务列表中找到您需要修改的任务，在其**操作**列单击**修改**。
3. 在弹出的**编辑任务**对话框中修改路由任务相关参数，然后单击**确定**。

**查询路由任务**

1. 在**replicator**页面单击**任务**页签。
2. 在路由任务列表中找到您需要查看的任务，在其**操作**列单击**详情**即可看到该任务的详细信息。
任务详细信息的关键字段说明如下：

|  | 参数 | 说明 |
|---|---|---|

消息队列

| 任务概览 | 任务状态 | 显示任务的当前状态： 创建中创建完成运行中已暂停 |
|---|---|---|
|  | 消息同步TPS | 每分钟统计一次消息同步的TPS值；TPS即平均每秒传输的消息数量。 |
|  | 消息堆积量 | 当前还没有来得及同步的消息数量。 |
|  | 最新同步时间 | 最近一次消息同步发生的时间。 |
| 任务详情 | 来源去向 | 显示任务的来源和去向。 |
|  | 起始同步位点 | 显示指定的起始同步位点。 |
|  | 过滤规则 | 显示指定的过滤规则。 |
| 消息详情 | 消息同步TPS | 每分钟统计一次消息同步的TPS值；TPS即平均每秒传输的消息数量。 |
|  | 消息延迟 | 当前同步到的位点和最新消息位点之间的时间差。 |
|  | 消息堆积量 | 当前还没有来得及同步的消息数量。 |

**删除路由任务**

**重要**

删除路由任务会同时停止该任务的运行。
1. 在**replicator**页面单击**任务**页签。
2. 在路由任务列表中找到您需要删除的任务，在其**操作**列单击**删除**。
3. 在弹出的提示对话框中仔细阅读提示信息，然后单击**确定**。

**参考信息**

**获取MQ实例endpoint和MQ API**

创建消息同步云时，需要输入指定云环境下RocketMQ服务的接入点和控制台API接口，即**MQ****实例**
**endpoint**和**MQ API**参数，您可以参考以下操作获取该参数值。
1. 登录Apsara Uni-manager运维控制台。
消息队列
2. 顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **运维工具**。
3. 在左侧导航栏，选择**运维工具** > **服务注册变量大盘**。
4. 在**服务注册变量大盘**页面，单击**高级筛选**。
5. 在**服务**文本框中输入 `mq` ，单击**搜索**。
6. 查看**MQ****实例****endpoint**。
i. 在 `mq-cai` 服务的**Service Registration**列中，单击图标。 ii. 单击 `mq-cai` 服务的**Service Registration**列的文本信息，在弹出的**注册变量**对话框中，查看到的**client.onsAddr**的参数值即为**MQ****实例****endpoint**的值。
7. 查看**MQ API**。
i. `mq-console` 服务的**Service Registration**列中，单击图标。 ii. 单击 `mq-console` 服务的**Service Registration**列的文本信息，在弹出的**注册变量**对话框中，查看到的**console.domain**的参数值加上前缀http://即为**MQ API**的值。

### Connector

#### ElasticSearch

RocketMQ可通过Elasticsearch消息路由功能实现不同Elasticsearch实例间的数据消息同步，本文介绍如

**背景信息**

RocketMQ的Elasticsearch消息路由功能常用于不同Elasticsearch实例间的消息数据同步，可将消息先由源Elasticsearch实例同步至指定RocketMQ实例，而后再由RocketMQ实例同步至目标Elasticsearch实

**前提条件**

已创建RocketMQ实例。具体操作，请参见创建实例。 已创建Topic。具体操作，请参见创建Topic。 已创建Elasticsearch实例。具体操作，请参见《**Elasticsearch** **用户指南》** > **创建集群**。

**操作流程**

**步骤一：创建 ES 实例信息**

创建路由任务前，需要先录入Elasticsearch实例的相关信息。包括Elasticsearch实例的地域、用户名、 密码和端点信息等。RocketMQ将根据录入的ES实例信息获取访问Elasticsearch资源的权限。

**步骤二：创建路由任务**

指定消息源和消息目标，设置描述等信息。

**步骤一：创建 ES 实例信息**

1. 登录RocketMQ控制台。
2. 在左侧导航栏单击**消息路由** **> Connector**。
3. 在**ElasticSearch**页签单击**云信息**页子签，然后单击**创建** **ES** **实例信息**。
4. 在弹出的**创建** **ES** **实例信息**对话框中配置以下参数，然后单击**确定**。
消息队列

| 参数 | 说明 |
|---|---|
| 云信息名称 | 云信息的名称，由您自定义输入。 |
| 地域 | ElasticSearch实例所在地域。 |
| 用户名 | 登录ElasticSearch实例所需的用户名信息。 |
| 密码 | 登录ElasticSearch实例所需的密码信息。 |
| ES 端点 | 用于连接ElasticSearch实例的端点信息，一般为其私网地址。 |
| 备注 | 云信息的具体说明或备注，以作区分和记录。 |

**步骤二：创建路由任务**

1. 登录RocketMQ控制台。
2. 在左侧导航栏单击**消息路由** **> Connector**。
3. 在**ElasticSearch**页签单击**任务**子页签，然后单击**创建任务**。
4. 在弹出的**创建任务**对话框中选择任务类型并配置相应参数，然后单击**确定**。
i. **Source****类型任务：**单击**Source**页签并配置以下参数：

**重要**

当前 ElasticSearch Source Connector 仅支持全量同步，暂不支持实时增量同步。任务执行完毕后请务必手动停止Source任务，以防在重启（如系统升级）时触发数据重复同步。

| 参数 | 说明 |
|---|---|
| ES 源 | ES 源：选择需要同步消息的ElasticSearch实例的云信息。 Index：输入源ElasticSearch实例的Index信息。 |
| MQ 目标 | 目标实例：选择消息将被同步到的Topic所属的RocketMQ实例。 目标Topic：选择消息将被同步到的Topic名称。 |
| 描述 | 输入对该同步任务的具体描述或备注，以作区分和记录。 |

消息队列 ii. **Sink****类型任务：**单击**Sink**页签并配置以下参数：

| 参数 | 说明 |
|---|---|
| MQ 源 | 源实例：选择需要同步的消息所属Topic的所在RocketMQ实例。 源Topic：选择需要同步的消息所属的Topic名称。 |
| ES 目标 | ES 目标：选择消息将被同步到的ElasticSearch实例。 Index：输入目标ElasticSearch实例的Index信息。 |
| 描述 | 输入对该同步任务的具体描述或备注，以作区分和记录。 |

**删除云信息**

1. 在**ElasticSearch**页签单击**云信息**子页签。
2. 在云信息列表中找到您需要删除的目标云信息，在其**操作**列单击**删除**。
3. 在弹出的提示对话框中仔细阅读提示信息并单击**确定**。

**启停路由任务**

1. 在**ElasticSearch**页签单击**任务**子页签。
2. 在路由任务列表中找到您需要启停的任务，在其**操作**列单击**开始**启动任务，或单击**停止**暂停任务。

**删除路由任务**

**重要**

删除路由任务会同时停止该任务的运行。
1. 在**ElasticSearch**页签单击**任务**子页签。
2. 在路由任务列表中找到您需要删除的任务，在其**操作**列单击**删除**。
3. 在弹出的提示对话框中仔细阅读提示信息，然后单击**确定**。

#### Redis

RocketMQ可通过Redis消息路由功能实现不同Redis实例间的数据消息同步，本文介绍如何配置Redis消息路由任务。

**背景信息**

RocketMQ的Redis消息路由功能支持将消息由RocketMQ实例同步至目标Redis实例。

**前提条件**

已创建RocketMQ实例。具体操作，请参见创建实例。 已创建Topic。具体操作，请参见创建Topic。 已创建Redis实例。具体操作，请参见**《云数据库** **Tair****（兼容** **Redis****）用户指南》** > **创建实例**。

**操作流程**

消息队列创建路由任务前，需要先录入Redis实例的相关信息。包括Redis实例的地址、端口号、密码和编号

**步骤二：创建路由任务**

指定消息源和消息目标，设置描述等信息。
1. 登录RocketMQ控制台。
2. 在左侧导航栏单击**消息路由** **> Connector**。
3. 单击**Redis**页签，然后单击**云信息**页子签，然后单击**创建** **Redis** **连接**。
4. 在弹出的**创建** **Redis** **连接**对话框中配置以下参数，然后单击**确定**。

| 参数 | 说明 |
|---|---|
| 连接名称 | 为该 Redis 连接设置一个便于识别和管理的别名。 |
| Redis 地址 | 输入 Redis 服务器的地址。 |
| Redis 端口 | 输入 Redis 服务监听的 TCP 端口号。 |
| Redis 密码 | 输入要连接的Redis实例的密码。 |
| Redis 数据库 | 选择要连接的逻辑数据库编号。 说明 Redis 默认支持 0~15 共 16 个库。 |
| 备注 | 云信息的具体说明或备注，以作区分和记录。 |

**步骤二：创建路由任务**

1. 在**Redis**页签，单击**任务**子页签，然后单击**创建任务**。
2. 在弹出的**创建任务**对话框中配置相应参数，然后单击**确定**。

| 参数 | 说明 |
|---|---|
| MQ 源 | 源实例：选择需要同步的消息所属Topic的所在RocketMQ实例。 源Topic：选择需要同步的消息所属的Topic名称。 |

消息队列

| Redis 目标 | Redis 连接：选择消息将被同步到的Redis连接。 Redis 命令：定义如何将消息内容写入 Redis中。可选值： SET HSET：当选择HSET时，还需要设置Hash字段。 LPUSH RPUSH SADD ZADD Key 策略：决定 Redis 中存储数据的 Key 如何生成。可选值： RECORD TOPIC TOPIC PARTITION _ CUSTOM：当选择CUSTOM时，还需要配置Key前缀，即 Key 的固定前缀部分。 Key 过期时间（秒）：为生成的 Redis Key 设置自动过期时间（单位：秒），防止内存无限增长。 |
|---|---|
| 描述 | 输入对该同步任务的具体描述或备注，以作区分和记录。 |

**删除云信息**

1. 在**Redis**页签单击**云信息**子页签。
2. 在云信息列表中找到您需要删除的目标云信息，在其**操作**列单击**删除**。
3. 在弹出的对话框中仔细阅读提示信息并单击**确定**。

**启停路由任务**

1. 在**Redis**页签单击**任务**子页签。
2. 在路由任务列表中找到您需要启停的任务，在其**操作**列单击**开始**启动任务，或单击**停止**暂停任务。

**删除路由任务**

**重要**

删除路由任务会同时停止该任务的运行。
**运行中**的任务不支持删除。
1. 在**Redis**页签单击**任务**子页签。
2. 在路由任务列表中找到您需要删除的任务，在其**操作**列单击**删除**。
3. 在弹出的对话框中仔细阅读提示信息，然后单击**确定**。

#### OSS

RocketMQ可通过OSS消息路由功能实现不同OSS存储空间之间的数据消息同步，本文介绍如何配置OSS消息路由任务。 消息队列

**背景信息**

RocketMQ的OSS消息路由功能支持将消息由RocketMQ实例同步至目标OSS中。

**前提条件**

已创建RocketMQ实例。具体操作，请参见创建实例。 已创建Topic。具体操作，请参见创建Topic。 已创建OSS存储空间。具体操作，请参见**《对象存储****用户指南》** > **创建存储空间**。

**操作流程**

配置OSS消息路由任务的操作流程如下：

**步骤一：创建OSS云信息**

创建路由任务前，需要先录入OSS存储空间的相关信息。包括OSS存储空间的Endpoint和存储空间名称等。RocketMQ将根据录入的OSS存储空间名称信息获取访问OSS资源的权限。

**步骤二：创建路由任务**

指定消息源和消息目标，设置描述等信息。

**步骤一：创建OSS云信息**

1. 登录RocketMQ控制台。
2. 在左侧导航栏单击**消息路由** **> Connector**。
3. 单击**OSS**页签，然后单击**云信息**页子签，然后单击**创建** **OSS** **云信息**。
4. 在弹出的**创建** **OSS** **云信息**对话框中配置以下参数，然后单击**确定**。

| 参数 | 说明 |
|---|---|
| 云信息名称 | 云信息的名称，由您自定义输入。 |
| OSS Endpoint | OSS 服务的地域访问域名。 |
| OSS Bucket | 要操作的存储空间名称。 |
| AccessKey ID | 输入拥有OSS 实例权限的账号的AccessKey ID。 获取方式请参见《RocketMQ开发指南》手册的《获取 AccessKey》章节。 |
| AccessKey Secret | 输入拥有OSS 实例权限的账号的AccessKey Secret。 获取方式请参见《RocketMQ开发指南》手册的《获取 AccessKey》章节。 |
| 备注 | 云信息的具体说明或备注，以作区分和记录。 |

**步骤二：创建路由任务**

1. 在**OSS**页签，单击**任务**子页签，然后单击**创建任务**。
消息队列
2. 在弹出的**创建任务**对话框中配置相应参数，然后单击**确定**。

| 参数 | 说明 |
|---|---|
| MQ 源 | 源实例：选择需要同步的消息所属Topic的所在RocketMQ实例。 源Topic：选择需要同步的消息所属的Topic名称。 |
| OSS 目标 | OSS 云信息：选择上一步创建的OSS云信息。 对象键前缀：定义写入 OSS 的文件路径前缀，用于组织目录结构。 压缩类型：选择输出文件的压缩格式。可选值： 不压缩：原始文本格式，如 .json , .txt 。 GZIP：高压缩比，适合日志类数据。 单文件最小记录数：输入必须大于 0。当累积消息数达到此值时，立即触发文件写入并轮换。 默认值： 10000 。 文件轮转间隔（毫秒）：输入必须大于 0。即使未达到最大记录数， 也强制每隔指定时间生成一个新文件。 默认值： 300000 （即 5 分钟）。 |
| 任务描述 | 输入对该同步任务的具体描述或备注，以作区分和记录。 |

**删除云信息**

1. 在**OSS**页签单击**云信息**子页签。
2. 在云信息列表中找到您需要删除的目标云信息，在其**操作**列单击**删除**。
3. 在弹出的对话框中仔细阅读提示信息并单击**确定**。

**启停路由任务**

1. 在**OSS**页签单击**任务**子页签。
2. 在路由任务列表中找到您需要启停的任务，在其**操作**列单击**开始**启动任务，或单击**停止**暂停任务。

**删除路由任务**

**重要**

删除路由任务会同时停止该任务的运行。
**运行中**的任务不支持删除。
1. 在**OSS**页签单击**任务**子页签。
2. 在路由任务列表中找到您需要删除的任务，在其**操作**列单击**删除**。
3. 在弹出的对话框中仔细阅读提示信息，然后单击**确定**。

#### MySQL

消息队列 RocketMQ可通过MySQL消息路由功能实现不同MySQL实例间的数据消息同步，本文介绍如何配置

**背景信息**

RocketMQ的MySQL消息路由功能支持将消息由RocketMQ实例同步至目标MySQL实例。

**前提条件**

已创建RocketMQ实例。具体操作，请参见实例管理。 已创建Topic。具体操作，请参见创建Topic。

**操作流程**

创建路由任务前，需要先录入MySQL实例的相关信息。包括MySQL实例的地址、用户名、密码

**步骤二：创建路由任务**

指定消息源和消息目标，设置描述等信息。
1. 登录RocketMQ控制台。
2. 在左侧导航栏单击**消息路由** **> Connector**。
3. 单击**MySQL**页签，然后单击**云信息**子页签，最后单击**创建** **MySQL** **连接**。
4. 在弹出的**创建** **MySQL** **连接**对话框中配置以下参数，然后单击**确定**。

| 参数 | 说明 |  |  |
|---|---|---|---|
| 连接名称 | 为该MySQL连接设置一个便于识别和管理的别名。 |  |  |
| MySQL 地址 | MySQL 连接地址，格式： host:port/database ，如 rm- xxx:3306/mydb 。 |  |  |
|  |  | rm- |  |

|  |  | host:port/database |
|---|---|---|
|  | xxx:3306/mydb |  |

消息队列

| 用户名 | 输入要连接的MySQL实例的用户名。 说明 CDC Source 使用 MySQL binlog 实时同步，源库账户需要以下权限： SELECT ：snapshot 全量读取表数据。 REPLICATION SLAVE ：连接 MySQL 读取 binlog 流。 REPLICATION CLIENT ：执行 SHOW MASTER STATUS 获取 binlog 位点。 RELOAD ：snapshot 时加全局读锁保证数据一致性。 |
|---|---|
| 密码 | 输入要连接的MySQL实例的密码。 |
| 备注 | 云信息的具体说明或备注，以作区分和记录。 |

**步骤二：创建路由任务**

1. 在**MySQL**页签，单击**任务**子页签，然后单击**创建任务**。
2. 在弹出的**创建任务**对话框中配置相应参数，然后单击**确定**。

| 参数 | 说明 |
|---|---|
| MySQL 源 | MySQL 连接：选择需要同步消息的MySQL连接信息。 同步表：输入需要同步消息的MySQL表。格式： database.table ，多表用逗号分隔。 |
| MQ 目标 | MQ 实例：选择消息将被同步到的Topic所属的RocketMQ实例。 Topic：选择消息将被同步到的Topic名称。 |
| 描述 | 输入对该同步任务的具体描述或备注，以作区分和记录。 |
| 高级配置 | 支持配置数据变换，更多信息请参见高级配置。 |

消息队列

| 参数 | 说明 |
|---|---|
| MQ 源 | MQ 实例：选择需要同步的消息所属Topic的所在RocketMQ实例。 Topic：选择需要同步的消息所属的Topic名称。 |
| MySQL 目标 | MySQL 连接：选择消息将被同步到的MySQL连接信息。 写入模式：选择数据写入 MySQL 的策略。 Upsert：当主键存在时更新记录，不存在时插入新记录。 Insert：仅插入新记录。 Update：仅更新。 主键字段：指定 MySQL 表中的主键字段名，多个字段用逗号分隔。 自动建表：是否允许系统在目标 MySQL 中自动创建不存在的表。 自动同步 DDL：是否同步源端的表结构变更（DDL）。 同步 DELETE：是否处理删除操作。 是：当接收到 DELETE 类型的消息时，在目标 MySQL 中执行对应的删除操作。 否：忽略 DELETE 消息，仅处理 INSERT/UPDATE。 消费起点：指定任务启动时的初始消费位置。可选择从最早消息开始和从最新消息开始。 |
| 描述 | 输入对该同步任务的具体描述或备注，以作区分和记录。 |
| 高级配置 | 支持配置数据变换，更多信息请参见高级配置。 |

**高级配置**

RocketMQ Connect 为 MySQL 场景内置 5 类单消息转换（SMT）能力，可在数据同步过程中对消息实时加工，无需修改上下游业务：

| 转换能力 | 作用 | 典型场景 |
|---|---|---|
| 字段重命名（Key）/字段重命名 （Value） | 基于正则批量修改字段名。 | 上下游列名不一致，如 user id → uid 。 _ |
| 命名风格转换（Value） | 一键切换命名风格（snake case ↔ _ camelCase 等）。 | Java 服务与数据仓库命名规范对齐。 |
| 置空字段（Value） | 按正则匹配字段名，将其值置为 NULL。 | 数据脱敏，如同步时清空手机号、身份证。 |

消息队列

| 行过滤（Value） | 按正则匹配字段值，命中则丢弃整条消息。 | 只同步指定业务数据，如仅同步某地区订单。 |
|---|---|---|

**核心价值**：
**零代码接入**：所有转换均通过配置完成，无需开发插件
**灵活组合**：多个转换可链式串联，满足复杂加工需求
**规范落地**：将数据脱敏、命名规范、过滤规则前置到同步链路，降低下游治理成本
单击**添加变换**，选择变换类型后，配置相关参数：

**说明**

支持添加多个数据变换，执行顺序为从上到下。
**字段重命名（****Key**）/**字段重命名（****Value**）

| 参数 | 说明 |
|---|---|
| 字段名匹配正则 | 输入一个正则表达式，用于匹配您想要重命名的原始字段名。 |
| 替换后的字段名 | 输入新的字段名称。如果字段名匹配正则匹配到了多个字段，此处的新名称将应用于所有匹配到的字段。 |
| 正则标志 | 设置正则表达式的匹配模式。 |

**行过滤（Value）**

| 参数 | 说明 |
|---|---|
| 值匹配正则（匹配则丢弃该消息） | 输入一个正则表达式。系统会检查目标字段的值，如果值与该正则表达式匹配，则触发过滤动作。 |
| 要检查的字段名（逗号分隔） | 指定需要应用上方值匹配正则（匹配则丢弃该消息）的一个或多个字段名称。 |

**命名风格转换（Value）**

| 参数 | 说明 |
|---|---|

消息队列

| 源命名风格 | 选择数据当前的字段命名格式。 LOWER UNDERSCORE _ LOWER CAMEL _ UPPER UNDERSCORE _ UPPER CAMEL _ LOWER HYPHEN _ |
|---|---|
| 目标命名风格 | 选择您希望转换成的目标格式。 LOWER UNDERSCORE _ LOWER CAMEL _ UPPER UNDERSCORE _ UPPER CAMEL _ LOWER HYPHEN _ |

**置空字段（Value）**

| 参数 | 说明 |
|---|---|
| 字段名匹配正则 | 输入一个正则表达式，用于匹配需要被置空的字段名称（Key）。 |
| 占位参数（无实际作用） | 预留字段，若当前版本暂无实际功能，保持默认或留空即可。 |

**删除连接信息**

1. 在**MySQL**页签单击**云信息**子页签。
2. 在云信息列表中找到您需要删除的目标云信息，在其**操作**列单击**删除**。
3. 在弹出的对话框中仔细阅读提示信息并单击**确定**。

**启停路由任务**

1. 在**MySQL**页签单击**任务**子页签。
2. 在路由任务列表中找到您需要启停的任务，在其**操作**列单击**开始**启动任务，或单击**停止**暂停任务。

**删除路由任务**

**重要**

删除路由任务会同时停止该任务的运行。
**运行中**的任务不支持删除。
1. 在**MySQL**页签单击**任务**子页签。
2. 在路由任务列表中找到您需要删除的任务，在其**操作**列单击**删除**。
3. 在弹出的对话框中仔细阅读提示信息，然后单击**确定**。
消息队列

## SDK使用指南

### SDK概述

本文介绍RocketMQ支持协议以及相关的多语言SDK。

**SDK协议及多语言**

RocketMQ支持的协议和多语言SDK如下表所示。

| 协议 | 语言 | SDK下载链接 | 示例代码 |
|---|---|---|---|
| TCP协议 | Java | mq-tcp-java-sdk | mq-tcp-samples-java |
|  | C/C++ | mq-tcp-csharp-sdk | mq-tcp-samples- csharp |
|  | .NET | mq-tcp-.net-sdk | mq-tcp-samples-.net |
| HTTP协议 | Java | mq-http-java-sdk | mq-http-samples-java |
|  | PHP | mq-http-php-sdk | mq-http-samples-php |
|  | Go | mq-http-go-sdk | mq-http-samples-go |
|  | Python | mq-http-python-sdk | mq-http-samples- python |
|  | Node.js | mq-http-nodejs-sdk | mq-http-samples- node.js |
|  | C# | mq-http-cpp-sdk | mq-http-samples-cpp |
|  | C++ | mq-http-csharp-sdk | mq-http-samples- csharp |

**协议使用须知**

由于RocketMQ提供的TCP协议客户端SDK和HTTP协议客户端SDK不同，所创建的同一个Group ID不能混用于TCP协议和HTTP协议。若您使用TCP协议的SDK收发消息，则您需要创建TCP协议类型的Group ID，不能使用HTTP协议类型的Group ID。 同一个RocketMQ实例分别提供TCP协议接入点和HTTP协议接入点，不同协议的接入点不能混用。若您使用TCP协议的SDK收发消息，则您需要获取实例的TCP协议接入点，不能使用HTTP协议的接入点。

### TCP协议SDK参考

消息队列

#### Demo工程

##### Demo工程概述

本Demo主要目的在于帮助初次接触RocketMQ的工程师，一步一步搭建RocketMQ测试工程。Demo程序以Java为例，包括普通消息、事务消息、定时消息的测试代码，以及相关Spring的配置示例。

##### Demo环境准备

**操作步骤**

安装IDE。 您可以使用IntelliJ IDEA或者Eclipse。本文以IntelliJ IDEA为例。 请在IntelliJ IDEA下载IDEA Ultimate版本，并参考IntelliJ IDEA说明进行安装。 解压即可看到本地新增了mq-demo-master文件夹。

##### Demo工程配置

**前提条件**

如果本地未安装JDK，请在Java SE Downloads下载安装。推荐使用JDK 8。

**操作步骤**

1. Demo工程文件导入IntelliJ IDEA。
消息队列 i. 在IntelliJ IDEA界面，单击**Import Project**，选择mq-demo-master文件夹。 图 1. 选择mq-demo-master文件夹 ii. 选择Import类型。 图 2. 选择Import类型 iii. 默认单击**Next**，直到导入完成。Demo工程需要加载依赖的JAR包，因此导入过程需要等待2-3分钟。
2. 创建资源。
请在RocketMQ控制台创建Topic、Group ID（GID）和鉴权所需的AccessKey（AK）。 i. 创建Topic和Group ID，更多详细信息，具体操作方式，请参见创建资源。 ii. AccessKey获取步骤如下： 要获取AccessKey ID和AccessKey Secret，请在Apsara Uni-manager运营控制台右上角，单击您的头像图标，选择**个人信息**即可在**阿里云****AccessKey**区域获取。
3. 配置Demo。
需要配置2个文件：MqConfig类和common.xml。 i. 按以下说明配置MqConfig类

```
public static final String TOPIC = “刚才创建的Topic。” public static final String GROUP_ID = “刚才创建的GID。” public static final String ACCESS_KEY = “您的AccessKey ID。” public static final String SECRET_KEY = “您的AccessKey Secret。”
```

public static final String NAMESRV_ADDR = “您的`RocketMQ`实例的`TCP`接入点，可在控制台获取。”

**说明**

要用哪个账号创建的Topic，就需要用这个账号的AccessKey ID和AccessKey Secret。 消息队列 ii. 配置common.xml。

```xml
 <props>
```

<prop key="AccessKey">XXX</prop> <!-- 使用前请修改这些资源信息 `-->`

```xml
 <prop key="SecretKey">XXX</prop>
 <prop key="GROUP_ID">XXX</prop>
 <prop key="Topic">XXX</prop>
 <prop key="NAMESRV_ADDR">XXX</prop>
</props>
```

##### 运行Demo

**以Main方式启动收发消息**

1. 运行SimpleMQProducer类发送消息。
2. 登录RocketMQ控制台，选择所需实例，在**实例详情**页面，单击**消息查询**页签，选择按**Topic****查询**，选择
Topic名称进行查询。可以看到消息已经发送至Topic。
3. 运行SimpleMQConsumer类接收消息。可以看到消息被接收打印的日志。因为有初始化，所以需等待
几秒，在生产环境中不会经常初始化。 在实例详情页面，单击**Group****管理**页签，选择目标Group ID，单击**操作**列的**消费者状态**。在**消费者状态**面

**以Spring方式启动收发消息**

1. 运行ProducerClient类发送消息。
2. 运行ConsumerClient类接收消息。
在实例详情页面，单击**Group****管理**页签，选择目标Group ID，单击**操作**列的**消费者状态**。在**消费者状态**面

**发送事务消息**

运行SimpleTransactionProducer类发送消息。

**说明**

LocalTransactionCheckerImpl类为本地事务check接口类。用于校验事务。具体内容请参见收发事务消息。 运行SimpleOrderConsumer类接收消息。 运行SimpleOrderProducer类发送消息。

**说明**

**发送定时（延时）消息**

运行MQTimerProducer类发送消息。延时3秒后投递。 消息队列

**说明**

您也可以指定一个精确的投递时间，最长定时时间为40天。具体内容请参见收发定时消息。

#### 客户端参数说明

本文介绍客户端参数。

| 参数名 | 使用端 | 默认值 | 建议值 | 用途 | 客户端版本 |
|---|---|---|---|---|---|
| AccessKey | 发送端/消费端 | 用户配置 | 用户配置 | 用于标识、校验用户身份 | >=1.2.7.Final |
| SecretKey | 发送端/消费端 | 用户配置 | 用户配置 | 用于标识、校验用户身份 | >=1.2.7.Final |
| NAMESRV AD _ DR | 发送端/消费端 | 部署后产生 | 部署后产生 | RocketMQ服务接入点 | >=1.2.7.Final |
| MsgTraceSwit ch | 发送端/消费端 | true | true | RocketMQ消息轨迹功能开关 | >=1.7.0.Final |
| GROUP ID _ | 发送端/消费端 | 控制台申请 | 控制台申请 | 标识Producer 和Consumer客户端所在分组。 与老版本的 PID/CID兼容 | >=1.7.8.Final |
| ProducerId | 发送端 | 控制台申请 | 控制台申请 | 标识Producer 客户端所在分组；普通消息无重要用途；事务消息时，一个 Producer客户端挂掉，服务器会回查同分组内其它Producer 客户端。 | >=1.2.7.Final |
| SendMsgTime outMillis | 发送端 | 5000 | 默认 | 消息发送超时时间，如果服务端在配置的对应时间内未ACK，则发送客户端认为该消息发送失败。 | >=1.2.7.Final |
| ConsumerId | 消费端 | 控制台申请 | 控制台申请 | 标识Consumer 客户端所在分组 | >=1.2.7.Final |

消息队列

| MessageMode l | 消费端 | CLUSTERING | 默认 | 消费模式，有两种： CLUSTERING ，集群消费，每条订阅消息只会被其中一个 Consumer客户端收到； BROADCASTI NG，广播消费，每条订阅的消息会被所有客户端收到。 | >=1.2.7.Final |
|---|---|---|---|---|---|
| ConsumeThre adNums | 消费端 | 动态调整的 20~64之间 | 根据业务情况调整 | 消费线程数量； 一般来说，单条消息消费的耗时越大，消费线程数也应该设置更大。 | >=1.2.7.Final |
| MaxReconsu meTimes | 消费端 | 16 | 默认 | 消息消费失败时的最大重试次数 | >=1.2.7.Final |
| ConsumeTim eout | 消费端 | 15 | 默认 | 设置每条消息消费的最大超时时间,超过这个时间，这条消息将会被视为消费失败，等下次重新投递再次消费。 每个业务需要设置一个合理的值，单位(分钟)。 | >=1.2.7.Final |
| PostSubscripti onWhenPull | 消费端 | false | 根据消费模式调整 | 是否每次请求都带上最新的订阅关系；广播消费时，配置为 true，避免因为订阅关系不一致导致部分消息收不到；集群消费时，强制要求订阅关系一致，该参数设置为 false。 | >=1.2.7.Final |
| ConsumeMes sageBatchMa xSize | 消费端 | 1 | 根据业务需要调整 | BatchConsum er每次批量消费的最大消息数量, 默认值为 1，允许自定义范围为[1, 32]，您的实际消费数量可以小于设置的最大消费数量。 | >=1.6.0.Final |

消息队列

| MaxCachedM essageAmoun t | 消费端 | 5000 | 根据机器内存调整 | Consumer允许在客户端中缓存的最大消息数量，默认值为 5000，设置过大可能会引起客户端OOM，取值范围为[100, 50000]。 | >=1.7.0.Final |
|---|---|---|---|---|---|
| MaxCachedM essageSizeIn MiB | 消费端 | 512 | 根据机器内存调整 | Consumer允许在客户端中缓存的最大消息容量，默认值为 512 MB，设置过大可能会引起客户端OOM， 取值范围为[16, 2048]。 | >=1.7.0.Final |

#### 客户端错误码说明

本文介绍收发消息相关的错误码及参考消息相关内容。

**收发消息相关的错误码**

| 状态码 | 状态标志 | 描述 | 原因&建议解决方案 | 服务端版本 |
|---|---|---|---|---|
| 13 | MESSAGE ILLEGA _ L | 消息校验不通过。 | 1. 检查消息体body 是否为空。 2. 检查消息 property长度是否超出 32767B。 3. 检查消息总长度是否超过4M。 | >=4.0.1 |
| 17 | TOPIC NOT EXIS _ _ T | 消息topic不存在。 | 1. 在RocketMQ控制台完成topic创建。 2. 重启应用。 详情请参见资源不存在中的《Topic 不存在》小节。 | >=4.0.1 |
| 26 | SUBSCRIPTION G _ ROUP NOT EXIST _ _ | Group ID不存在。 | 1. 在RocketMQ控制台完成Group ID创建。 2. 重启应用。 详情请参见资源不存在中的《Group ID不存在》小节。 | >=4.0.1 |

消息队列

| 24 | SUBSCRIPTION N _ OT EXIST _ | 订阅信息不存在。 | 1. 检查当前订阅组是否已正常启动上线。 2. 检查是否出现订阅关系不一致的情况。 | >=4.0.1 |
|---|---|---|---|---|
| 23 | SUBSCRIPTION P _ ARSE FAILED _ | 订阅表达式解析失败。 | 检查对应topic的订阅表达式、tag。 | >=4.0.1 |
| 25 | SUBSCRIPTION N _ OT LATEST _ | 订阅关系不一致。 | 该状态短暂出现自动恢复。 详情请参见订阅关系不一致。 | >=4.0.1 |
| 14 | SERVICE NOT AV _ _ AILABLE | 发消息服务不可用。 | 请求的broker下线中；请求的broker 状态异常，所以 broker不可写；请求的broker的状态为备机。 详情请参见使用异常中的《发消息失败》小节。 | >=4.0.1 |
| 16 | NO PERMISSION _ （发消息） | 请求无效。 | 当前请求的broker 禁写。 当前请求broker上该topic禁写。 当前请求broker不接受事务消息。 | >=4.0.1 |
| 16 | NO PERMISSION _ （收消息） | 请求无效。 | 当前请求的broker 禁读。 当前订阅组已禁读。 当前拉取的topic已禁读。 当前订阅组禁止广播消息。 | >=4.0.1 |
| 1 | SYSTEM ERROR _ | 系统异常。 | RocketMQ Broker 正在重启维护或者是服务器压力过大产生的短暂超时。 详情请参见使用异常中的《发消息失败》小节。 | >=4.0.1 |

消息队列

| 1 | SYSTEM ERROR _ （权限校验） | 权限校验失败。 | 检查是否有topic的发布/订阅权限。 | >=4.0.1 |
|---|---|---|---|---|
| 2 | SYSTEM BUSY _ | 系统忙，拒绝请求。 | RocketMQ Broker 正在重启维护或者是服务器压力过大产生的短暂超时。 详情请参见使用异常中的《发消息失败》小节。 | >=4.0.1 |

#### Java SDK

##### 使用说明

RocketMQ提供Java SDK实现消息发布与消息订阅。本文将详细介绍各接口的相关参数以及各接口的使用说明。 表 1. 通用参数

| 参数名 | 参数说明 |
|---|---|
| NAMESRV ADDR _ | 设置为TCP协议接入点，可从RocketMQ控制台的实例详情页面的网络管理页签获取。 |
| AccessKey | 您在账号管理控制台中创建的AccessKeyId，用于身份认证。 |
| SecretKey | 您在账号管理控制台中创建的AccessKeySecret，用于身份认证。 |
| OnsChannel | 用户渠道，默认为：ALIYUN。 |

表 2. 发送消息参数

| 参数名 | 参数说明 |
|---|---|
| SendMsgTimeoutMillis | 设置消息发送的超时时间，单位（毫秒），默认：3000。 |
| CheckImmunityTimeInSeconds（事务消息） | 设置事务消息第一次回查的最快时间，单位（秒）。 |
| shardingKey（顺序消息） | 顺序消息中用来计算不同分区的值。 |

消息队列表 3. 订阅消息参数说明

| 参数名 | 参数说明 |
|---|---|
| GROUP ID _ | 您在RocketMQ控制台上创建的Group ID。 |
| MessageModel | 设置Consumer实例的消费模式，默认为集群消费（值： CLUSTERING）；广播消费（BROADCASTING）。 |
| ConsumeThreadNums | 设置Consumer实例的消费线程数，默认：64。 |
| MaxReconsumeTimes | 设置消息消费失败的最大重试次数，默认：16。 |
| ConsumeTimeout | 设置每条消息消费的最大超时时间，超过设置时间则被视为消费失败，等下次重新投递再次消费。每个业务需要设置一个合理的值，单位（分钟）。默认：15。 |
| suspendTimeMillis（顺序消息） | 只适用于顺序消息，设置消息消费失败的重试间隔时间。 |
| maxCachedMessageAmount | 客户端本地的最大缓存消息数据，默认值：1000；单位：条。 |
| maxCachedMessageSizeInMiB | 客户端本地的最大缓存消息大小，取值范围：16 MB ~ 2 GB；默认值：512 MB。 |

消息队列

**消息收发代码示例**

##### 环境准备

运行本节描述的Java代码之前，请按以下步骤准备好环境。

**操作步骤**

1. 通过以下两种方式引入依赖（任选一种）：
Maven方式引入依赖：

```xml
<dependency>
    <groupId>com.aliyun.openservices</groupId>
   <artifactId>ons-client</artifactId>
   <version>1.8.4.Final</version>
</dependency>
```

下载依赖JAR包
2. 代码里涉及到的Topic和Group ID，需要到控制台上创建。
Message Tag可以完全由应用自定义，具体创建过程请参见创建资源。
3. 以TCP方式接入使用RocketMQ服务的应用程序需要部署在同一个地域的ECS上。

##### 日志配置

客户端日志用于记录客户端运行过程中的异常，帮助您快速定位和修复问题。本文介绍RocketMQ客户端日志的打印方式，以及默认和自定义配置。

**打印客户端日志**

消息队列 RocketMQ的Java SDK 1.7.8.Final已内置了日志实现，您无需在客户端应用中添加日志实现依赖即可打印RocketMQ客户端日志。 RocketMQ客户端日志的默认配置和如何修改默认配置，请参见下文的客户端日志配置部分。 RocketMQ的Java SDK 1.7.8.Final以下的旧版本不支持log4j2，只支持log4j、logback。您需要在pom.xml配置文件或者lib中添加对应的日志实现依赖来打印RocketMQ客户端日志。 依赖log4j或logback作为日志实现的示例代码如下所示。

**方式一：依赖log4j作为日志实现**

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

**方式二：依赖logback作为日志实现**

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

**说明**

应用中同时依赖log4j和logback的日志实现会造成日志冲突，从而导致客户端日志打印混乱。确保应用只依赖其中一个日志实现，是正确打印RocketMQ客户端日志的前提条件，建议您通过**mvn clean dependency:tree | grep log**命令进行排查。

**客户端日志配置**

RocketMQ 客户端支持自定义**日志保存路径**、**日志级别**以及**保存历史日志文件的最大个数**。考虑到日志传输以及阅读的便利性，暂不允许自定义**单个日志文件大小**，仍保持默认的64 MB。 各参数的配置说明如下： 消息队列

| 参数 | 说明 |
|---|---|
| 日志保存路径 | 请确保应用进程有对该路径写的权限，否则日志不会打印。 |
| 保存历史日志文件的最大个数 | 支持1到100之间的数值；若输入的值超出该范围或格式错误， 则系统默认保存10个。 |
| 日志级别 | 支持ERROR、WARN、INFO、DEBUG中任何一种，不匹配默认INFO。 |

**默认配置**

RocketMQ客户端启动后，会按照如下的默认配置生成日志文件： 日志保存路径： `/{user.home}/logs/ons.log` ，其中 `{user.home}` 是指启动当前Java进程的用户的根目录。 保存历史日志文件的最大个数：10个。 日志级别：INFO。 单个日志文件大小：64 MB。

**自定义配置**

**说明**

若要自定义RocketMQ客户端的日志配置，请升级到Java SDK 1.2.5版本及以上。 ons.client.logRoot：日志保存路径。 ons.client.logFileMaxIndex：保存历史日志文件的最大个数。 ons.client.logLevel：日志级别。

**示例**

您可在启动脚本中或者IDE的VM options中添加如下系统参数：

**Linux示例**

```
-Dons.client.logRoot=/home/admin/logs -Dons.client.logLevel=WARN - Dons.client.logFileMaxIndex=20
```

**Windows示例**

```
-Dons.client.logRoot=D:\logs -Dons.client.logLevel=WARN - Dons.client.logFileMaxIndex=20
```

其中，/home/admin/ 和 D:\ 仅为示例，请填写您实际的系统目录。

##### Spring 集成

###### Spring集成概述

消息队列本节介绍如何在Spring框架下用RocketMQ收发消息。主要包括三部分内容：普通消息生产者和Spring 集请确保同一个Group ID下所有Consumer实例的订阅关系保持一致，具体内容请参见订阅关系一致。 Spring框架下支持的配置参数和TCP Java一致，具体内容请参见使用说明。

###### 生产者与Spring集成

**操作步骤**

1. 在producer.xml中定义生产者Bean等信息。

```xml
<?xml version="1.0" encoding="UTF-8"?>
 <beans xmlns="http://www.springframework.org/schema/beans"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd">
     <bean id="producer" class="com.aliyun.openservices.ons.api.bean.ProducerBean" in
it-method="start" destroy-method="shutdown">
```

<property name="properties" > <!--生产者配置信息`-->`

```xml
             <props>
                 <prop key="AccessKey">XXX</prop>
                 <prop key="SecretKey">XXX</prop>
```

<!-- ons-client 版本是 `1.8.4.Final`，需要配置（从实例管理页面复制 `TCP` 协议接入点）

```xml
                 <prop key="NAMESRV_ADDR">XXX</prop>
                 -->
             </props>
         </property>
     </bean>
 </beans>
```

2. 通过已经与Spring集成好的生产者生产消息。
消息队列

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
```

* 生产者 `Bean` 配置在 `producer.xml` 中，可通过 `ApplicationContext` 获取或者直接注入到
其他类（比如具体的 `Controller`）中 `*/`

```
         ApplicationContext context = new
ClassPathXmlApplicationContext("producer.xml");
         Producer producer = (Producer) context.getBean("producer");
```

`//`循环发送消息

```
         for (int i = 0; i < 100; i++) {
             Message msg = new Message( //
```

`// Message` 所属的 `Topic`

```
                     "TopicTestMQ",
```

`// Message Tag` 可理解为 `Gmail` 中的标签，对消息进行再归类，方便 `Consumer` 指定过滤条件在 `RocketMQ` 的服务器过滤

```
                     "TagA",
```

`// Message Body` 可以是任何二进制形式的数据，`RocketMQ` 不做任何干预 `//` 需要 `Producer` 与 `Consumer` 协商好一致的序列化和反序列化方式

```
                     "Hello MQ".getBytes());
```

`//` 设置代表消息的业务关键属性，请尽可能全局唯一 `//` 以方便您在无法正常收到消息情况下，可通过控制台查询消息并补发 `//` 注意：不设置也不会影响消息正常收发

```
             msg.setKey("ORDERID_100");
```

`//` 发送消息，只要不抛异常就是成功

```java
             try {
                 SendResult sendResult = producer.send(msg);
                 assert sendResult != null;
                 System.out.println("send success: " + sendResult.getMessageId());
             }catch (ONSClientException e) {
                 System.out.println("发送失败");
             }
         }
     }
 }
```

###### 事务消息生产者与Spring集成

**背景信息**

**操作步骤**

1. 实现LocalTransactionChecker，如下所示。一个消息生产者只能有一个LocalTransactionChecker。
消息队列

```java
package demo; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.transaction.LocalTransactionChecker; import com.aliyun.openservices.ons.api.transaction.TransactionStatus; public class DemoLocalTransactionChecker implements LocalTransactionChecker {
    public TransactionStatus check(Message msg) {
```

`System.out.println("`开始回查本地事务状态"); return TransactionStatus.CommitTransaction; //根据本地事务状态检查结果返回不同的`Tra`

```
nsactionStatus
    }
}
```

2. 在transactionProducer.xml中定义事务消息生产者Bean等信息。
消息队列

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
```

<property name="properties" > <!--事务消息生产者配置信息`-->`

```xml
             <props>
                 <prop key="AccessKey">AKDEMO</prop>
                 <prop key="SecretKey">SKDEMO</prop>
                 <prop key="GROUP_ID">GID_DEMO</prop>
```

<!-- ons-client版本是`1.8.4.Final`，需要配置（从实例管理页面复制`TCP`协议接入点）

```xml
                 <prop key="NAMESRV_ADDR">XXX</prop>
                 -->
             </props>
         </property>
         <property name="localTransactionChecker" ref="localTransactionChecker">
</property>
     </bean>
 </beans>
```

3. 通过已经与Spring集成好的生产者生产事务消息。
消息队列

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
```

* 事务消息生产者`Bean`配置在`transactionProducer.xml`中，可通过`ApplicationContext`获取
或者直接注入到其他类（比如具体的`Controller`）中
* 请结合例子"发送事务消息"
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
```

`System.out.println("`执行本地事务"); return TransactionStatus.CommitTransaction; //根据本地事务执行结果来返回

```
不同的TransactionStatus
             }
         }, null);
     }
 }
```

###### 消费者与Spring集成

**操作步骤**

1. 创建MessageListener，如下所示。
消息队列

```java
package demo; import com.aliyun.openservices.ons.api.Action; import com.aliyun.openservices.ons.api.ConsumeContext; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.MessageListener; public class DemoMessageListener implements MessageListener {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println("Receive: " + message.getMsgID());
        try {
            //do something..
            return Action.CommitMessage;
        }catch (Exception e) {
```

`//`消费失败

```
            return Action.ReconsumeLater;
        }
    }
}
```

2. 在consumer.xml中定义消费者Bean等信息。

```xml
 <?xml version="1.0" encoding="UTF-8"?>
 <beans xmlns="http://www.springframework.org/schema/beans"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd">
     <bean id="msgListener" class="demo.DemoMessageListener"></bean> <!--Listener配置-
```

`->` <!-- Group ID订阅同一个`Topic`，可以创建多个`ConsumerBean-->`

```xml
     <bean id="consumer" class="com.aliyun.openservices.ons.api.bean.ConsumerBean" in
it-method="start" destroy-method="shutdown">
```

<property name="properties" > <!--消费者配置信息`-->`

```xml
             <props>
                 <prop key="GROUP_ID">GID_DEMO</prop> <!--请替换XXX-->
                 <prop key="AccessKey">AKDEMO</prop>
                 <prop key="SecretKey">SKDEMO</prop>
```

<!-- ons-client版本在`1.8.4.Final`，需要配置（从实例管理页面复制`TCP`协议接入点）

```xml
                 <prop key="NAMESRV_ADDR">XXX</prop>
```

消息队列

```
                 -->
```

<!--将消费者线程数固定为`50`个

```xml
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
                             <property name="expression" value="*"/><!--expression即Tag
```

，可以设置成具体的`Tag`，如 taga||tagb||tagc，也可设置成*。 *仅代表订阅所有`Tag`，不支持通配`-->`

```
                         </bean>
                     </key>
                 </entry>
```

<!--更多的订阅添加`entry`节点即可，如下所示`-->`

```xml
                 <entry value-ref="msgListener">
                     <key>
                         <bean
class="com.aliyun.openservices.ons.api.bean.Subscription">
                             <property name="topic" value="TopicTestMQ-Other"/> <!--订
```

阅另外一个`Topic -->`

```xml
                             <property name="expression" value="taga||tagb"/> <!-- 订阅
```

多个`Tag -->`

```
                         </bean>
                     </key>
</entry>
```

消息队列

```
                 </entry>
             </map>
         </property>
     </bean>
 </beans>
```

3. 运行已经与Spring集成好的消费者，如下所示。

```java
package demo; import org.springframework.context.ApplicationContext; import org.springframework.context.support.ClassPathXmlApplicationContext; public class ConsumeWithSpring {
    public static void main(String[] args) {
        /**
```

* 消费者`Bean`配置在`consumer.xml`中，可通过`ApplicationContext`获取或者直接注入到其他类(
比如具体的`Controller)`中 `*/`

```java
        ApplicationContext context = new
ClassPathXmlApplicationContext("consumer.xml");
        System.out.println("Consumer Started");
    }
}
```

##### 发送消息（三种方式）

###### 发送消息（三种方式）概述

RocketMQ发送消息有三种实现方式：可靠同步发送、可靠异步发送、单向（Oneway）发送。本节介绍每种实现的原理、使用场景以及三种实现的异同，同时提供代码示例以供参考。

**说明**

###### 可靠同步发送

**原理**

同步发送是指消息发送方发出数据后，会在收到接收方发回响应之后才发下一个数据包的通讯方式。 图 1. 同步发送消息队列

**应用场景**

此种方式应用场景非常广泛，例如重要通知邮件、报名短信通知、营销短信系统等。

**示例代码**

```java
import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.Producer; import com.aliyun.openservices.ons.api.SendResult; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import java.util.Properties; public class ProducerTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
```

`// AccessKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.AccessKey,"XXX");
```

`// SecretKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.SecretKey, "XXX");
```

`//`设置发送超时时间，单位毫秒

```
        properties.setProperty(PropertyKeyConst.SendMsgTimeoutMillis, "3000");
```

`//` 设置 `TCP` 接入域名，进入控制台的实例管理页面的“获取接入点信息”区域查看

```
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        Producer producer = ONSFactory.createProducer(properties);
```

`//` 在发送消息前，必须调用 `start` 方法来启动 `Producer`，只需调用一次即可

```
        producer.start();
```

`//`循环发送消息

```
        for (int i = 0; i < 10; i++){
            Message msg = new Message( //
```

`// Message` 所属的 `Topic`

```
                "TopicTestMQ",
```

`// Message Tag` 可理解为 `Gmail` 中的标签，对消息进行再归类，方便 `Consumer` 指定过滤条件在 `RocketMQ` 的服务器过滤

```
                "TagA",
```

`// Message Body` 可以是任何二进制形式的数据， `RocketMQ` 不做任何干预， `//` 需要 `Producer` 与 `Consumer` 协商好一致的序列化和反序列化方式消息队列

```
                "Hello MQ".getBytes());
```

`//` 设置代表消息的业务关键属性，请尽可能全局唯一。 `//` 以方便您在无法正常收到消息情况下，可通过阿里云服务器管理控制台查询消息并补发 `//` 注意：不设置也不会影响消息正常收发

```
            msg.setKey("ORDERID_" + i);
            try {
                SendResult sendResult = producer.send(msg);
```

`//` 同步发送消息，只要不抛异常就是成功

```java
                if (sendResult != null) {
                    System.out.println(new Date() + " Send mq message success. Topic is:
" + msg.getTopic() + " msgId is: " + sendResult.getMessageId());
                }
            }
            catch (Exception e) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理

```java
                System.out.println(new Date() + " Send mq message failed. Topic is:" + m
sg.getTopic());
                e.printStackTrace();
            }
        }
```

`//` 在应用退出前，销毁 `Producer` 对象 `//` 注意：如果不销毁也没有问题

```
        producer.shutdown();
    }
}
```

###### 可靠异步发送

**原理**

异步发送是指发送方发出数据后，不等接收方发回响应，接着发送下个数据包的通讯方式。RocketMQ的异步发送，需要您实现异步发送回调接口（SendCallback），在执行消息的异步发送时，应用不需要等待服务器响应即可直接返回，通过回调接口接收服务器响应，并对服务器的响应结果进行处理。 消息队列图 1. 异步发送

**应用场景**

异步发送一般用于链路耗时较长，对RT响应时间较为敏感的业务场景，例如视频上传后通知启动转码服务， 转码完成后通知推送转码结果等。

**示例代码**

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
```

`// AccessKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.AccessKey, "XXX");
```

`// SecretKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.SecretKey, "XXX");
```

`//`设置发送超时时间，单位毫秒

```
        properties.setProperty(PropertyKeyConst.SendMsgTimeoutMillis, "3000");
```

`//` 设置 `TCP` 接入域名，进入控制台的实例管理页面的“获取接入点信息”区域查看

```
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        Producer producer = ONSFactory.createProducer(properties);
```

`//` 在发送消息前，必须调用 `start` 方法来启动 `Producer`，只需调用一次即可。

```
        producer.start();
        Message msg = new Message(
```

`// Message` 所属的 `Topic`

```
                "TopicTestMQ",
```

`// Message Tag,`可理解为 `Gmail` 中的标签，对消息进行再归类，方便 `Consumer` 指定过滤条件在 `RocketMQ` 的服务器过滤

```
                "TagA",
```

`// Message Body`，任何二进制形式的数据，`RocketMQ` 不做任何干预，需要 `Producer` 与消息队列 `Consumer` 协商好一致的序列化和反序列化方式

```
                "Hello MQ".getBytes());
```

`//` 设置代表消息的业务关键属性，请尽可能全局唯一。以方便您在无法正常收到消息情况下，可通过控制台查询消息并补发。 `//` 注意：不设置也不会影响消息正常收发

```
        msg.setKey("ORDERID_100");
```

`//` 异步发送消息, 发送结果通过 `callback` 返回给客户端。

```java
        producer.sendAsync(msg, new SendCallback() {
            @Override
            public void onSuccess(final SendResult sendResult) {
```

`//` 消费发送成功

```java
                System.out.println("send message success. topic=" +
sendResult.getTopic() + ", msgId=" + sendResult.getMessageId());
            }
            @Override
            public void onException(OnExceptionContext context) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理

```java
                System.out.println("send message failed. topic=" + context.getTopic() +
", msgId=" + context.getMessageId());
            }
        });
```

`//` 在 `callback` 返回之前即可取得 `msgId`。

```java
        System.out.println("send message async. topic=" + msg.getTopic() + ", msgId=" +
msg.getMsgID());
```

`//` 在应用退出前，销毁 `Producer` 对象。注意：如果不销毁也没有问题

```
        producer.shutdown();
    }
```

###### 单向（Oneway）发送

**原理**

单向（Oneway）发送特点为只负责发送消息，不等待服务器回应且没有回调函数触发，即只发送请求不等待应答。此方式发送消息的过程耗时非常短，一般在微秒级别。 图 1. Oneway发送消息队列

**应用场景**

适用于某些耗时非常短，但对可靠性要求并不高的场景，例如日志收集。 下表概括了三者的特点和主要区别。

| 发送方式 | 发送TPS | 发送结果反馈 | 可靠性 |
|---|---|---|---|
| 同步发送 | 快 | 有 | 不丢失 |
| 异步发送 | 快 | 有 | 不丢失 |
| 单向发送 | 最快 | 无 | 可能丢失 |

**示例代码**

消息队列

```java
    import com.aliyun.openservices.ons.api.Message;
    import com.aliyun.openservices.ons.api.Producer;
    import com.aliyun.openservices.ons.api.ONSFactory;
    import com.aliyun.openservices.ons.api.PropertyKeyConst;
    import java.util.Properties;
    public static void main(String[] args) {
        Properties properties = new Properties();
```

`// AccessKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.AccessKey, "XXX");
```

`// SecretKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.SecretKey, "XXX");
```

`//`设置发送超时时间，单位毫秒

```
        properties.setProperty(PropertyKeyConst.SendMsgTimeoutMillis, "3000");
```

`//` 设置 `TCP` 接入域名，进入控制台的实例管理页面的“获取接入点信息”区域查看

```
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        Producer producer = ONSFactory.createProducer(properties);
```

`//` 在发送消息前，必须调用 `start` 方法来启动 `Producer`，只需调用一次即可。

```
        producer.start();
```

`//`循环发送消息

```
        for (int i = 0; i < 10; i++){
            Message msg = new Message(
```

`// Message` 所属的 `Topic`

```
                    "TopicTestMQ",
                    // Message Tag,
```

`//` 可理解为 `Gmail` 中的标签，对消息进行再归类，方便 `Consumer` 指定过滤条件在 `Ro` `cketMQ` 的服务器过滤

```
                    "TagA",
                    // Message Body
```

`//` 任何二进制形式的数据，`RocketMQ` 不做任何干预，需要 `Producer` 与 `Consumer` 协商好一致的序列化和反序列化方式

```
                    "Hello MQ".getBytes());
```

`//` 设置代表消息的业务关键属性，请尽可能全局唯一。 `//` 以方便您在无法正常收到消息情况下，可通过阿里云服务器管理控制台查询消息并补发。 `//` 注意：不设置也不会影响消息正常收发

```
            msg.setKey("ORDERID_" + i);
```

`//` 由于在 `oneway` 方式发送消息时没有请求应答处理，一旦出现消息发送失败，则会因为没有重试

```
            producer.sendOneway(msg);
        }
```

`//` 在应用退出前，销毁 `Producer` 对象 `//` 注意：如果不销毁也没有问题

```
        producer.shutdown();
    }
```

##### 发送消息（多线程）

RocketMQ的消费者和生产者客户端对象是线程安全的，可以在多个线程之间共享使用。 您可以在服务器上（或者多台服务器）部署多个生产者和消费者实例，也可以在同一个生产者或消费者实例里采用多线程发送或接收消息，从而提高消息发送或接收TPS。请避免为每个线程创建一个客户端实例。 消息队列在多线程之间共享Producer的示例代码如下：

```java
import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.Producer; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.SendResult; import java.util.Properties; public class SharedProducer {
    public static void main(String[] args) {
```

`// Producer` 实例配置初始化

```
        Properties properties = new Properties();
```

`//`您在控制台创建的 `Group ID`

```
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
```

`// AccessKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.AccessKey,"XXX");
```

`// SecretKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.SecretKey, "XXX");
```

`//`设置发送超时时间，单位毫秒

```
        properties.setProperty(PropertyKeyConst.SendMsgTimeoutMillis, "3000");
```

`//` 设置 `TCP` 接入域名，进入控制台的实例管理页面的“获取接入点信息”区域查看

```
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        final Producer producer = ONSFactory.createProducer(properties);
```

`//` 在发送消息前，必须调用 `start` 方法来启动 `Producer`，只需调用一次即可

```
        producer.start();
```

`//`创建的 `Producer` 和 `Consumer` 对象为线程安全的，可以在多线程间进行共享，避免每个线程创建一个实例。 `//`在 `thread` 和 `anotherThread` 中共享 `Producer` 对象，并发地发送消息至 `RocketMQ`。

```java
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Message msg = new Message( //
```

`// Message` 所属的 `Topic`

```
                    "TopicTestMQ",
```

`// Message Tag` 可理解为 `Gmail` 中的标签，对消息进行再归类，方便 `Consumer` 指定过滤条件在 `RocketMQ` 的服务器过滤

```
                    "TagA",
```

`// Message Body` 可以是任何二进制形式的数据， `RocketMQ` 不做任何干预， `//` 需要 `Producer` 与 `Consumer` 协商好一致的序列化和反序列化方式

```
                    "Hello MQ".getBytes());
                    SendResult sendResult = producer.send(msg);
```

`//` 同步发送消息，只要不抛异常就是成功

```java
                    if (sendResult != null) {
                        System.out.println(new Date() + " Send mq message success. Topic
is:" + MqConfig.TOPIC + " msgId is: " + sendResult.getMessageId());
                    }
                } catch (Exception e) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理

```java
                    System.out.println(new Date() + " Send mq message failed. Topic is:"
+ MqConfig.TOPIC);
                    e.printStackTrace();
                }
}
```

消息队列

```java
            }
        });
        thread.start();
        Thread anotherThread = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Message msg = new Message("TopicTestMQ", "TagA", "Hello MQ".getBytes
());
                    SendResult sendResult = producer.send(msg);
```

`//` 同步发送消息，只要不抛异常就是成功

```java
                    if (sendResult != null) {
                        System.out.println(new Date() + " Send mq message success. Topic
is:" + MqConfig.TOPIC + " msgId is: " + sendResult.getMessageId());
                    }
                } catch (Exception e) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理

```java
                    System.out.println(new Date() + " Send mq message failed. Topic is:"
+ MqConfig.TOPIC);
                    e.printStackTrace();
                }
            }
        });
        anotherThread.start();
```

`// Producer` 实例若不再使用时，可将 `Producer` 关闭，进行资源释放

```
        // producer.shutdown();
    }
}
```

##### 收发顺序消息

本文介绍顺序消息的收发及示例代码。 顺序消息（FIFO 消息）是RocketMQ提供的一种严格按照顺序来发布和消费的消息类型。本文提供使用 TCP协议下的Java SDK收发顺序消息的示例代码供您参考。具体内容请参见顺序消息。

**发送顺序消息示例代码**

```java
package com.aliyun.openservices.ons.example.order; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.SendResult; import com.aliyun.openservices.ons.api.order.OrderProducer; import java.util.Properties; public class ProducerClient {
    public static void main(String[] args) {
        Properties properties = new Properties();
```

`//` 您在控制台创建的`Group ID`。

```
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
```

`// AccessKeyId` 阿里云身份验证，在阿里云服务器管理控制台创建。

```
        properties.put(PropertyKeyConst.AccessKey, "XXX");
```

`//``AccessKeySecret`阿里云身份验证，在阿里云服务器管理控制台创建。 消息队列 `// AccessKeySecret` 阿里云身份验证在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.SecretKey, "XXX");
```

`//` 设置`TCP`接入域名，进入控制台的实例管理页面的“网络管理”页签查看。

```
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        OrderProducer producer = ONSFactory.createOrderProducer(properties);
```

`//` 在发送消息前，必须调用`start`方法来启动`Producer`，只需调用一次即可。

```
        producer.start();
        for (int i = 0; i < 10; i++) {
            String orderId = "biz_" + i % 10;
            Message msg = new Message(//
```

`// Message`所属的`Topic`。

```
                    "Order_global_topic",
```

`// Message Tag`，可理解为`Gmail`中的标签，对消息进行再归类，方便`Consumer`指定过滤条件在`RocketMQ`的服务器过滤。

```
                    "TagA",
```

`// Message Body`，可以是任何二进制形式的数据， `RocketMQ`不做任何干预，需要`Prod` `ucer`与`Consumer`协商好一致的序列化和反序列化方式。

```
                    "send order global msg".getBytes()
            );
```

`//` 设置代表消息的业务关键属性，请尽可能全局唯一。 `//` 以方便您在无法正常收到消息情况下，可通过控制台查询消息并补发。 `//` 注意：不设置也不会影响消息正常收发。

```
            msg.setKey(orderId);
```

`//` 顺序消息中区分不同分区的关键字段，`Sharding Key`与普通消息的`key`是完全不同的概念。

```
            String shardingKey = String.valueOf(orderId);
            try {
                SendResult sendResult = producer.send(msg, shardingKey);
```

`//` 发送消息，只要不抛异常就是成功

```java
                if (sendResult != null) {
                    System.out.println(new Date() + " Send mq message success. Topic is:
" + msg.getTopic() + " msgId is: " + sendResult.getMessageId());
                }
            }
            catch (Exception e) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理。

```java
                System.out.println(new Date() + " Send mq message failed. Topic is:" + m
sg.getTopic());
                e.printStackTrace();
            }
        }
```

`//` 在应用退出前，销毁`Producer`对象。 `//` 注意：如果不销毁也没有问题。

```
        producer.shutdown();
    }
}
```

**订阅顺序消息示例代码**

消息队列

```java
package com.aliyun.openservices.ons.example.order; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.order.ConsumeOrderContext; import com.aliyun.openservices.ons.api.order.MessageOrderListener; import com.aliyun.openservices.ons.api.order.OrderAction; import com.aliyun.openservices.ons.api.order.OrderConsumer; import java.util.Properties; public class ConsumerClient {
    public static void main(String[] args) {
        Properties properties = new Properties();
```

`//` 您在控制台创建的`Group ID`。

```
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
```

`// AccessKeyId` 阿里云身份验证，在阿里云服务器管理控制台创建。

```
        properties.put(PropertyKeyConst.AccessKey, "XXX");
```

`// AccessKeySecret` 阿里云身份验证，在阿里云服务器管理控制台创建。

```
        properties.put(PropertyKeyConst.SecretKey, "XXX");
```

`//` 设置`TCP`接入域名，进入控制台的实例管理页面的“网络管理”页签查看。

```
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
```

`//` 顺序消息消费失败进行重试前的等待时间，单位（毫秒），取值范围：`10`毫秒 ~ 1800毫秒

```
        properties.put(PropertyKeyConst.SuspendTimeMillis, "100");
```

`//` 消息消费失败时的最大重试次数

```
        properties.put(PropertyKeyConst.MaxReconsumeTimes, "20");
```

`//` 在订阅消息前，必须调用`start`方法来启动`Consumer`，只需调用一次即可。

```
        OrderConsumer consumer = ONSFactory.createOrderedConsumer(properties);
        consumer.subscribe(
```

`// Message` 所属的 `Topic`

```
                "Jodie_Order_Topic",
```

`//` 订阅指定 `Topic` 下的 `Tags`： `// 1. *` 表示订阅所有消息 // 2. TagA||TagB||TagC表示订阅`TagA`或`TagB`或`TagC`的消息。

```
                "*",
                new MessageOrderListener() {
                    /**
```

`* 1.` 消息消费处理失败或者处理出现异常，返回`OrderAction.Suspend<br>`。 `* 2.` 消息处理成功，返回`OrderAction.Success`。 `*/`

```java
                    @Override
                    public OrderAction consume(Message message, ConsumeOrderContext cont
ext) {
                        System.out.println(message);
                        return OrderAction.Success;
                    }
                });
        consumer.start();
    }
}
```

##### 收发事务消息

消息队列本文介绍事务消息的交互流程、收发方式、示例代码及回查机制。

**交互流程**

RocketMQ的事务消息交互流程如下图所示： 图 1. 事务消息交互流程图

**发送事务消息**

发送事务消息包含以下两个步骤：
1. 发送半事务消息（Half Message）及执行本地事务。示例代码如下：

```java
package com.alibaba.webx.TryHsf.app1; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.SendResult; import com.aliyun.openservices.ons.api.transaction.LocalTransactionExecuter; import com.aliyun.openservices.ons.api.transaction.TransactionProducer; import com.aliyun.openservices.ons.api.transaction.TransactionStatus; import java.util.Properties; import java.util.concurrent.TimeUnit; public class TransactionProducerClient {
```

private final static Logger log = ClientLogger.getLog(); // 您需要设置自己的日志，便于排查问题

```
 public static void main(String[] args) throws InterruptedException {
     final BusinessService businessService = new BusinessService(); // 本地业务
     Properties properties = new Properties();
```

`//` 您在控制台创建的 `Group ID` 注意：事务消息的 `Group ID` 不能与其他类型消息的 `Group ID` 共用

```
     properties.put(PropertyKeyConst.GROUP_ID, "XXX");
```

`// AcccessKeyId` 阿里云身份验证，在阿里云服务器管理控制台创建

```
     properties.put(PropertyKeyConst.AccessKey, "XXX");
```

`// AccessKeySecret` 阿里云身份验证，在阿里云服务器管理控制台创建

```
     properties.put(PropertyKeyConst.SecretKey, "XXX");
```

`//` 设置 `TCP` 接入域名，进入控制台的实例管理页面的“获取接入点信息”区域查看

```java
     properties.put(PropertyKeyConst.NAMESRV_ADDR,
       "XXX");
     TransactionProducer producer = ONSFactory.createTransactionProducer(properties,
             new LocalTransactionCheckerImpl());
     producer.start();
     Message msg = new Message("Topic", "TagA", "Hello MQ
transaction===".getBytes());
     try {
             SendResult sendResult = producer.send(msg, new
LocalTransactionExecuter() { @Override
```

消息队列

```java
                 @Override
                 public TransactionStatus execute(Message msg, Object arg) {
```

`//` 消息 `ID`（有可能消息体一样，但消息 `ID` 不一样，当前消息 `ID` 在控制台无法查询）

```
                     String msgId = msg.getMsgID();
```

`//` 消息体内容进行 `crc32`，也可以使用其它的如 `MD5`

```
                     long crc32Id = HashUtil.crc32Code(msg.getBody());
```

`//` 消息 `ID` 和 `crc32id` 主要是用来防止消息重复 `//` 如果业务本身是幂等的，可以忽略，否则需要利用 `msgId` 或 `crc32Id` 来做幂等 `//` 如果要求消息绝对不重复，推荐做法是对消息体 `body` 使用 `crc32` 或 `MD5` 来防止重复消息

```
                     Object businessServiceArgs = new Object();
                     TransactionStatus transactionStatus = TransactionStatus.Unknow;
                     try {
                         boolean isCommit =
                             businessService.execbusinessService(businessServiceArgs);
                         if (isCommit) {
```

`//` 本地事务成功则提交消息

```
                             transactionStatus = TransactionStatus.CommitTransaction;
                         } else {
```

`//` 本地事务失败则回滚消息

```java
                             transactionStatus =
TransactionStatus.RollbackTransaction;
                         }
                     } catch (Exception e) {
                         log.error("Message Id:{}", msgId, e);
                     }
                     System.out.println(msg.getMsgID());
                     log.warn("Message Id:{}transactionStatus:{}", msgId, transactionS
tatus.name());
                     return transactionStatus;
                 }
             }, null);
         }
         catch (Exception e) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理

```java
             System.out.println(new Date() + " Send mq message failed. Topic is:" +
msg.getTopic());
             e.printStackTrace();
         }
```

`// demo example` 防止进程退出(实际使用不需要这样)

```
     TimeUnit.MILLISECONDS.sleep(Integer.MAX_VALUE);
 }
}
```

2. 提交事务消息状态。
当本地事务执行完成（执行成功或执行失败），需要通知服务器当前消息的事务状态。通知方式有以下两种： 执行本地事务完成后提交。 执行本地事务一直没提交状态，等待服务器回查消息的事务状态。 事务状态有以下三种：
**TransactionStatus.CommitTransaction**提交事务，允许订阅方消费该消息。
消息队列
**TransactionStatus.RollbackTransaction**回滚事务，消息将被丢弃不允许消费。
**TransactionStatus.Unknow**无法判断状态，期待RocketMQ Broker向发送方再次询问该消息对
应的本地事务的状态。

```java
public class LocalTransactionCheckerImpl implements LocalTransactionChecker {
   private final static Logger log = ClientLogger.getLog();
   final  BusinessService businessService = new BusinessService();
   @Override
   public TransactionStatus check(Message msg) {
```

`//`消息 `ID`（有可能消息体一样，但消息 `ID` 不一样，当前消息属于半事务消息，所以消息 `ID` 在控制台无法查询）

```
       String msgId = msg.getMsgID();
```

`//`消息体内容进行 `crc32`，也可以使用其它的方法如 `MD5`

```
       long crc32Id = HashUtil.crc32Code(msg.getBody());
```

`//`消息 `ID`、消息本 `crc32Id` 主要是用来防止消息重复 `//`如果业务本身是幂等的，可以忽略，否则需要利用 `msgId` 或 `crc32Id` 来做幂等 `//`如果要求消息绝对不重复，推荐做法是对消息体使用 `crc32` 或 `MD5` 来防止重复消息 `//`业务自己的参数对象，这里只是一个示例，需要您根据实际情况来处理

```
       Object businessServiceArgs = new Object();
       TransactionStatus transactionStatus = TransactionStatus.Unknow;
       try {
           boolean isCommit =
businessService.checkbusinessService(businessServiceArgs);
           if (isCommit) {
```

`//`本地事务已成功则提交消息

```
               transactionStatus = TransactionStatus.CommitTransaction;
           } else {
```

`//`本地事务已失败则回滚消息

```
               transactionStatus = TransactionStatus.RollbackTransaction;
           }
       } catch (Exception e) {
           log.error("Message Id:{}", msgId, e);
       }
       log.warn("Message Id:{}transactionStatus:{}", msgId,
transactionStatus.name());
       return transactionStatus;
   }
 }
```

**工具类**

```java
import java.util.zip.CRC32; public class HashUtil {
    public static long crc32Code(byte[] bytes) {
        CRC32 crc32 = new CRC32();
        crc32.update(bytes);
        return crc32.getValue();
    }
}
```

**事务回查机制说明**

发送事务消息为什么必须要实现回查Check机制？ 消息队列当步骤1中半事务消息发送完成，但本地事务返回状态为**TransactionStatus.Unknow**，或者应用退出导致本地事务未提交任何状态时，从RocketMQ Broker的角度看，这条Half状态的消息的状态是未知的。因此RocketMQ Broker会定期要求发送方能Check该Half状态消息，并上报其最终状态。 Check被回调时，业务逻辑都需要做些什么？ RocketMQ事务消息的check方法里面，应该写一些检查事务一致性的逻辑。RocketMQ发送事务消息时需要实现**LocalTransactionChecker**接口，用来处理RocketMQ Broker主动发起的本地事务状态回查请求；因此在事务消息的Check方法中，需要完成两件事情： i. 检查该半事务消息对应的本地事务的状态（committed或rollback）； ii. 向RocketMQ Broker提交该半事务消息本地事务的状态。

**订阅事务消息**

事务消息的订阅与普通消息订阅一致，具体操作方式请参见订阅消息。

##### 收发延时消息

本文介绍延时消息的收发及代码示例。 延时消息用于指定消息发送到RocketMQ服务器端后，延时一段时间才被投递到客户端进行消费（例如3秒后才被消费），适用于解决一些消息生产和消费有时间窗口要求的场景，或者通过消息触发延迟任务的场景，类似于延迟队列。

**发送延时消息**

发送延时消息的示例代码如下：

```java
import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.Producer; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.SendResult; import java.util.Properties; public class ProducerDelayTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
```

`// AccessKeyId` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.AccessKey, "XXX");
```

`// AccessKeySecret` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.SecretKey, "XXX");
```

`//` 设置 `TCP` 接入域名，进入控制台的实例管理页面的“获取接入点信息”区域查看

```
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        Producer producer = ONSFactory.createProducer(properties);
```

`//` 在发送消息前，必须调用 `start` 方法来启动 `Producer`，只需调用一次即可。

```
        producer.start();
        Message msg = new Message( //
```

`//` 您在控制台创建的 `Topic`

```
                "Topic",
```

`// Message Tag,` 可理解为 `Gmail` 中的标签，对消息进行再归类，方便 `Consumer` 指定过滤条件在 `RocketMQ` 服务器过滤

```
                "tag",
```

`// Message Body` 可以是任何二进制形式的数据，`RocketMQ` 不做任何干预，需要 `Producer` 与 `Consumer` 协商好一致的序列化和反序列化方式

```
                "Hello MQ".getBytes());
```

消息队列 e o

```
Q.getBytes());
```

`//` 设置代表消息的业务关键属性，请尽可能全局唯一。 `//` 以方便您在无法正常收到消息情况下，可通过控制台查询消息并补发。 `//` 注意：不设置也不会影响消息正常收发

```
        msg.setKey("ORDERID_100");
        try {
```

`//` 延时消息，单位毫秒（`ms`），在指定延迟时间（当前时间之后）进行投递，例如消息在 3 秒后投递

```
            long delayTime = System.currentTimeMillis() + 3000;
```

`//` 设置消息需要被投递的时间

```
            msg.setStartDeliverTime(delayTime);
            SendResult sendResult = producer.send(msg);
```

`//` 同步发送消息，只要不抛异常就是成功

```java
            if (sendResult != null) {
            System.out.println(new Date() + " Send mq message success. Topic is:" +
msg.getTopic() + " msgId is: " + sendResult.getMessageId());
            }
            } catch (Exception e) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理

```java
            System.out.println(new Date() + " Send mq message failed. Topic is:" +
msg.getTopic());
            e.printStackTrace();
        }
```

`//` 在应用退出前，销毁 `Producer` 对象`<br>` `//` 注意：如果不销毁也没有问题

```
        producer.shutdown();
    }
}
```

**订阅延时消息**

延时消息的订阅方式与普通消息一致，具体操作方式请参见订阅消息。

##### 收发定时消息

本文介绍发送定时消息的场景及代码示例。 定时消息可以做到在指定时间戳之后才可被消费者消费，用于解决一些消息生产和消费有时间窗口要求的场景，或者通过消息触发定时任务的场景。

**发送定时消息**

发送定时消息的示例代码如下：

```java
import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.Producer; import com.aliyun.openservices.ons.api.PropertyKeyConst; import com.aliyun.openservices.ons.api.SendResult; import java.text.ParseException; import java.text.SimpleDateFormat; import java.util.Properties; public class ProducerDelayTest {
    public static void main(String[] args) {
Propertiesproperties=newProperties();
```

消息队列

```
        Properties properties = new Properties();
```

`// AccessKeyId` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.AccessKey, "XXX");
```

`// AccessKeySecret` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.SecretKey, "XXX");
```

`//` 设置 `TCP` 接入域名，进入控制台的实例管理页面的“获取接入点信息”区域查看

```
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
        Producer producer = ONSFactory.createProducer(properties);
```

`//` 在发送消息前，必须调用 `start` 方法来启动 `Producer`，只需调用一次即可。

```
        producer.start();
        Message msg = new Message( //
```

`// Message` 所属的 `Topic`

```
                "Topic",
```

`// Message Tag` 可理解为 `Gmail` 中的标签，对消息进行再归类，方便 `Consumer` 指定过滤条件在 `RocketMQ` 的服务器过滤

```
                "tag",
```

`// Message Body` 可以是任何二进制形式的数据，`RocketMQ` 不做任何干预，需要 `Producer` 与 `Consumer` 协商好一致的序列化和反序列化方式

```
                "Hello MQ".getBytes());
```

`//` 设置代表消息的业务关键属性，请尽可能全局唯一 `//` 以方便您在无法正常收到消息情况下，可通过控制台查询消息并补发。 `//` 注意：不设置也不会影响消息正常收发

```
        msg.setKey("ORDERID_100");
        try {
```

`//` 定时消息，单位毫秒（`ms`），在指定时间戳（当前时间之后）进行投递，例如 `2016-03-07` `16:21:00` 投递。如果被设置成当前时间戳之前的某个时刻，消息将立刻投递给消费者。

```
            long timeStamp = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").parse("2016-
03-07 16:21:00").getTime();
            msg.setStartDeliverTime(timeStamp);
```

`//` 发送消息，只要不抛异常就是成功

```java
            SendResult sendResult = producer.send(msg);
            System.out.println("Message Id:" + sendResult.getMessageId());
        }
        catch (Exception e) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理

```java
            System.out.println(new Date() + " Send mq message failed. Topic is:" +
msg.getTopic());
            e.printStackTrace();
        }
```

`//` 在应用退出前，销毁 `Producer` 对象 `//` 注意：如果不销毁也没有问题

```
        producer.shutdown();
    }
}
```

**订阅定时消息**

定时消息的订阅方式与普通消息一致，具体操作方式请参见订阅消息。

##### 订阅消息

本文介绍消息的订阅方式及示例代码。 消息队列请确保同一个Group ID下所有Consumer实例的订阅关系保持一致，具体内容请参见订阅

**说明**

关系一致。

**订阅方式**

RocketMQ支持以下两种订阅方式：
**集群订阅：**同一个Group ID所标识的所有Consumer平均分摊消费消息。例如某个Topic有9条消息，一
个Group ID有3个Consumer实例，那么在集群消费模式下每个实例平均分摊，只消费其中的3条消息。 `//` 集群订阅方式设置（不设置的情况下，默认为集群订阅方式）

```
 properties.put(PropertyKeyConst.MessageModel, PropertyValueConst.CLUSTERING);
```

**广播订阅：**同一个Group ID所标识的所有Consumer都会各自消费某条消息一次。例如某个Topic有9条
消息，一个Group ID有3个Consumer实例，那么在广播消费模式下每个实例都会各自消费9条消息。 `//` 广播订阅方式设置

```
 properties.put(PropertyKeyConst.MessageModel, PropertyValueConst.BROADCASTING);
```

**示例代码**

消息队列

```java
import com.aliyun.openservices.ons.api.Action; import com.aliyun.openservices.ons.api.ConsumeContext; import com.aliyun.openservices.ons.api.Consumer; import com.aliyun.openservices.ons.api.Message; import com.aliyun.openservices.ons.api.MessageListener; import com.aliyun.openservices.ons.api.ONSFactory; import com.aliyun.openservices.ons.api.PropertyKeyConst; import java.util.Properties; public class ConsumerTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
```

`//` 您在控制台创建的 `Group ID`

```
        properties.put(PropertyKeyConst.GROUP_ID, "XXX");
```

`// AccessKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.AccessKey, "XXX");
```

`// SecretKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        properties.put(PropertyKeyConst.SecretKey, "XXX");
```

`//` 设置 `TCP` 接入域名，进入控制台的实例管理页面的“获取接入点信息”区域查看

```
        properties.put(PropertyKeyConst.NAMESRV_ADDR,
          "XXX");
```

`//` 集群订阅方式 (默认)

```
          // properties.put(PropertyKeyConst.MessageModel,
PropertyValueConst.CLUSTERING);
```

`//` 广播订阅方式

```
          // properties.put(PropertyKeyConst.MessageModel,
PropertyValueConst.BROADCASTING);
        Consumer consumer = ONSFactory.createConsumer(properties);
        consumer.subscribe("TopicTestMQ", "TagA||TagB", new MessageListener() { //订阅多
```

个 `Tag`

```java
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
            }
        });
```

`//`订阅另外一个 `Topic`

```java
        consumer.subscribe("TopicTestMQ-Other", "*", new MessageListener() { //订阅全部
Tag
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
            }
        });
        consumer.start();
        System.out.println("Consumer Started");
    }
}
```

在广播消费模式下，您无法在控制台进行消息堆积查询。因此，您也可以创建多个Group

**说明**

#### C/C++ SDK

消息队列

##### C/C++ SDK环境准备

###### 环境准备概述

**说明**

代码里涉及到的Topic和Group ID需要到RocketMQ控制台上创建。Message Tag可以完全由应用自定义，具体操作方式请参见创建资源。 使用RocketMQ服务的应用程序需要部署在阿里云ECS上。

###### 下载SDK

本文为您介绍使用v2.0.0版本的C++ SDK接入RocketMQ所需完成的准备工作、使用说明以及注意事项，

**操作步骤**

1. 下载Linux版C++ SDK。
2. 下载完成后，解压压缩包。
解压完成后，会有如下目录结构： demos/ 包含了普通消息发送、Oneway消息发送、顺序消息发送、普通消息消费、顺序消息消费等例子，还包含了CMakeList.txt用于demos的编译和管理。 include/ 包含用户自己编写的程序需要的头文件。 lib/ 包含基于x86_64的动态库，分别为接口库（libonsclient4cpp.so）和内核库 （librocketmq_client_core.so）。 changelog 新版本发布解决的问题和引入的新特性列表。

###### 使用Linux C++ SDK

自2019年6月28日起，新版本的SDK将只提供动态库方案。RocketMQ的库文件在lib/目录下，需要业务方生成可执行文件时链接librocketmq_client_core.so和libonsclient4cpp.so。由于demos引入了C++ 11 的特性和使用CMake来管理，需要提前安装CMake 3.0以上版本和g++ 4.8及以上版本。

**动态解决方案**

由于 GCC 5.x 及以上版本引入了Dual ABI，编译链接时，请添加-
**D_GLIBCXX_USE_CXX11_ABI=0**编译选项。
demos的使用方法如下： 消息队列 `cd aliyun-mq-linux-cpp-sdk //`下载的 `SDK` 解压后的路径 `cd demos //`进入 `demos` 目录，修改 `demos` 文件，填入自己在 `RocketMQ` 控制台创建的 `Topic` 和 `Key` 等相关的信息 `cmake . //`检测依赖和生成编译脚本 `make` 执行编译操作 `cd bin //`到生成的可执行文件目录下运行程序

##### 收发普通消息

**发送普通消息**

请参考以下示例代码进行消息发送。

```
#include "ONSFactory.h"
#include "ONSClientException.h"
using namespace ons; int main() {
```

`//`创建`Producer`，并配置发送消息所必需的信息。

```
    ONSFactoryProperty factoryInfo;
    factoryInfo.setFactoryProperty(ONSFactoryProperty::ProducerId, "XXX");
```

`//`设置`TCP`接入域名，进入消息队列`RocketMQ`版控制台实例详情页面的接入点区域查看。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR, "XXX");
    factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics,"XXX" );
```

`//`消息内容。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::MsgContent, "XXX");
```

`//`请确保环境变量`ALIBABA_CLOUD_ACCESS_KEY_ID`、`ALIBABA_CLOUD_ACCESS_KEY_SECRET`已设置。 `//AccessKey ID`，阿里云身份验证标识。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"));
```

`//AccessKey Secret`，阿里云身份验证密钥。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
    //create producer;
    Producer *pProducer = ONSFactory::getInstance()->createProducer(factoryInfo);
```

`//`在发送消息前，必须调用`start`方法来启动`Producer`，只需调用一次即可。

```
    pProducer->start();
    Message msg(
```

`//`普通消息所属的`Topic`，切勿使用普通消息的`Topic`来收发其他类型的消息。

```
            factoryInfo.getPublishTopics(),
```

`//Message Tag`，可理解为`Gmail`中的标签，对消息进行再归类，方便`Consumer`指定过滤条件在消息队列`RocketMQ`版的服务器过滤。 `"T` `A"` 消息队列

```
            "TagA",
```

`//Message Body`，不能为空，消息队列`RocketMQ`版不做任何干预，需要`Producer`与`Consumer`协商好一致的序列化和反序列化方式。

```
            factoryInfo.getMessageContent()
    );
```

`//` 设置代表消息的业务关键属性，请尽可能全局唯一。 `//` 以方便您在无法正常收到消息情况下，可通过消息队列`RocketMQ`版控制台查询消息并补发。 `//` 注意：不设置也不会影响消息正常收发。

```
    msg.setKey("ORDERID_100");
```

`//`发送消息，只要不抛出异常，就代表发送成功。

```
    try
    {
        SendResultONS sendResult = pProducer->send(msg);
    }
    catch(ONSClientException & e)
    {
```

`//`自定义处理`exception`的细节。

```
    }
```

`//` 在应用退出前，必须销毁`Producer`对象，否则会导致内存泄露等问题。

```
    pProducer->shutdown();
    return 0;
}
```

**订阅普通消息**

订阅普通消息的说明和示例代码，具体操作方式请参见订阅消息。

##### 收发顺序消息

**发送顺序消息**

发送顺序消息的示例代码如下。

```
#include "ONSFactory.h"
#include "ONSClientException.h"
#include <iostream>
using namespace ons; int main() {
```

`//Producer`创建和正常工作的参数，必须输入。

```
    ONSFactoryProperty factoryInfo;
    factoryInfo.setFactoryProperty(ONSFactoryProperty::ProducerId, "XXX");//您在消息队列R
```

`ocketMQ`版控制台创建的`Group ID`。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR, "XXX"); //设置TCP接
    factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics,"XXX" );//您在消息队
```

列`RocketMQ`版控制台创建的`Topic`。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::MsgContent, "XXX");//消息内容。
    factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey, "XXX");//AccessKey ID
```

消息队列阿里云身份验证，在阿里云服务器管理控制台创建。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey, "XXX" );//AccessKey S
```

`ecret`阿里云身份验证，在阿里云服务器管理控制台创建。 `//`创建`Producer`。

```
    OrderProducer *pProducer = ONSFactory::getInstance()-
>createOrderProducer(factoryInfo);
```

`//`在发送消息前，必须调用`start`方法来启动`Producer`，只需调用一次即可。

```
    pProducer->start();
    Message msg(
                //Message Topic
                factoryInfo.getPublishTopics(),
```

`//Message Tag`，可理解为`Gmail`中的标签，对消息进行再归类，方便`Consumer`指定过滤条件

```
                "TagA",
```

`//Message Body`，任何二进制形式的数据，消息队列`RocketMQ`版不做任何干预，需要 `Producer`与`Consumer`协商好一致的序列化和反序列化方式。

```
                factoryInfo.getMessageContent()
    );
```

`//` 设置代表消息的业务属性，请尽可能全局唯一。 `//` 以方便您在无法正常收到消息情况下，可通过消息队列`RocketMQ`版控制台查询消息并补发。 `//` 注意：不设置也不会影响消息正常收发。

```
    msg.setKey("ORDERID_100");
```

`//` 顺序消息中区分不同分区的关键字段。

```
    std::string shardingKey = "abc";
```

`//`带有同一`Sharding Key`的消息会按照顺序发送。

```
    try
    {
```

`//`发送消息，只要不抛异常就是成功。

```
        SendResultONS sendResult = pProducer->send(msg, shardingKey);
    std::cout << "send success" << std::endl;
    }
    catch(ONSClientException & e)
    {
```

`//`添加对`exception`的处理。

```
    }
```

`//` 在应用退出前，必须销毁`Producer`对象，否则会导致内存泄露等问题。

```
    pProducer->shutdown();
    return 0;
}
```

**接收顺序消息**

接收顺序消息的示例代码如下。

```
#include "ONSFactory.h"
using namespace std; using namespace ons;
```

创建消费消息的实例消息队列 `//`创建消费消息的实例。 `//pushConsumer`拉取到消息后，会主动调用该实例的`consumeMessage`函数。

```
class ONSCLIENT_API MyMsgListener : public MessageOrderListener { public:
    MyMsgListener()
    {
    }
    virtual ~MyMsgListener()
    {
    }
    virtual OrderAction consume(Message &message, ConsumeOrderContext &context)
    {
```

`//`根据业务需求，消费消息。

```
        return Success; //CONSUME_SUCCESS;
    }
}; int main(int argc, char* argv[]) {
```

`//OrderConsumer`创建和工作需要的参数，必须输入。

```
    ONSFactoryProperty factoryInfo;
    factoryInfo.setFactoryProperty(ONSFactoryProperty::ConsumerId, "XXX");
    factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics,"XXX" );
```

`//`请确保环境变量`ALIBABA_CLOUD_ACCESS_KEY_ID`、`ALIBABA_CLOUD_ACCESS_KEY_SECRET`已设置。 `//AccessKey ID`，阿里云身份验证标识。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"));
```

`//AccessKey Secret`，阿里云身份验证密钥。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
```

`//`设置`TCP`接入域名，进入消息队列`RocketMQ`版控制台实例详情页面的接入点区域查看。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR, "XXX");
```

`//`创建`orderConsumer`。

```
    OrderConsumer* orderConsumer = ONSFactory::getInstance()-
>createOrderConsumer(factoryInfo);
    MyMsgListener  msglistener;
```

`//`指定`orderConsumer`订阅的消息`Topic`和消息`Tag`。

```
    orderConsumer->subscribe(factoryInfo.getPublishTopics(), "*",&msglistener );
```

`//`注册消息监听的处理实例，`orderConsumer`拉取到消息后，会调用该类的`consumeMessage`函数。 `//`启动`orderConsumer`。

```
    orderConsumer->start();
    for(volatile int i = 0; i < 1000000000; ++i) {
        //wait
    }
```

消息队列 `//`销毁`orderConsumer,` 在应用退出前，必须销毁`Consumer`对象，否则会导致内存泄露等问题。

```
    orderConsumer->shutdown();
   return 0;
}
```

##### 收发定时消息

定时消息可以做到在指定时间之后才可被消费者消费，用于解决一些消息生产和消费有时间窗口要求的场景，或者通过消息触发定时任务的场景，类似于延迟队列。

**发送定时消息**

发送定时消息的代码示例如下。

```
#include "ONSFactory.h"
#include "ONSClientException.h"
#include <windows.h>
using namespace ons; int main() {
```

`//`创建`Producer`，并配置发送消息所必需的信息。

```
    ONSFactoryProperty factoryInfo;
    factoryInfo.setFactoryProperty(ONSFactoryProperty::ProducerId, "XXX");
```

`//`设置`TCP`接入域名，进入消息队列`RocketMQ`版控制台实例详情页面的接入点区域查看。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR, "XXX");
    factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics,"XXX" );
```

`//`消息内容。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::MsgContent, "XXX");
```

`//`请确保环境变量`ALIBABA_CLOUD_ACCESS_KEY_ID`、`ALIBABA_CLOUD_ACCESS_KEY_SECRET`已设置。 `//AccessKey ID`，阿里云身份验证标识。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"));
```

`//AccessKey Secret`，阿里云身份验证密钥。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
    //create producer;
    Producer *pProducer = ONSFactory::getInstance()->createProducer(factoryInfo);
```

`//`在发送消息前，必须调用`start`方法来启动`Producer`，只需调用一次即可。

```
    pProducer->start();
    Message msg(
            //Message Topic
            factoryInfo.getPublishTopics(),
```

`//Message Tag`，可理解为`Gmail`中的标签，对消息进行再归类，方便`Consumer`指定过滤条件在消息队列R k`tMQ`版的服务器过滤消息队列息队列`RocketMQ`版的服务器过滤

```
            "TagA",
```

`//Message Body`，不能为空，消息队列`RocketMQ`版不做任何干预，需要`Producer`与`Consumer`协商好一致的序列化和反序列化方式。

```
            factoryInfo.getMessageContent()
    );
```

`//` 设置代表消息的业务关键属性，请尽可能全局唯一。 `//` 以方便您在无法正常收到消息情况下，可通过消息队列`RocketMQ`版控制台查询消息并补发。 `//` 注意：不设置也不会影响消息正常收发。

```
    msg.setKey("ORDERID_100");
```

`// deliver time`单位`ms`，指定一个时刻，在这个时刻之后消息才能被消费，这个例子表示`3s`后才能被消费。

```
    long deliverTime = GetTickCount64() + 3000;
    msg.setStartDeliverTime(deliverTime);
```

`//`发送消息，只要不抛出异常，就代表发送成功。

```
    try
    {
        SendResultONS sendResult = pProducer->send(msg);
    }
    catch(ONSClientException & e)
    {
```

`//`自定义处理`exception`的细节。

```
    }
```

`//` 在应用退出前，必须销毁`Producer`对象，否则会导致内存泄露等问题。

```
    pProducer->shutdown();
    return 0;
}
```

**订阅定时消息**

订阅定时消息的说明和示例代码，具体操作方式请参见订阅消息。

##### 收发事务消息

本文介绍事务消息的交互流程、收发方式、示例代码及回查机制。

**交互流程**

RocketMQ事务消息的交互流程如下图所示： 消息队列图 1. 事务消息交互流程图

**发送事务消息**

发送事务消息包含以下两个步骤：
1. 发送半事务消息（Half Message）及执行本地事务。示例代码如下：

```
#include "ONSFactory.h"
#include "ONSClientException.h"
using namespace ons;
    class MyLocalTransactionExecuter : LocalTransactionExecuter
    {
        MyLocalTransactionExecuter()
        {
        }
        ~MyLocalTransactionExecuter()
        {
        }
        virtual TransactionStatus execute(Message &value)
        {
```

`//` 消息`ID`（有可能消息体一样，但消息`ID`不一样，当前消息`ID`在消息队列`RocketMQ`版控制台无法查询。)

```
                string msgId = value.getMsgID();
```

`//` 消息体内容进行`crc32`，也可以使用其它的如`MD5`。 `//` 消息`ID`和`crc32id`主要是用来防止消息重复。 `//` 如果业务本身是幂等的，可以忽略，否则需要利用`msgId`或`crc32Id`来做幂等。 `//` 如果要求消息绝对不重复，推荐做法是对消息体`body`使用`crc32`或`MD5`来防止重复消息。

```
                TransactionStatus transactionStatus = Unknow;
                try {
```

`boolean isCommit =` 本地事务执行结果;

```
                    if (isCommit) {
```

`//` 本地事务成功、提交消息。

```
                        transactionStatus = CommitTransaction;
                    } else {
```

`//` 本地事务失败、回滚消息。

```
                        transactionStatus = RollbackTransaction;
                    }
                } catch (...) {
                    //exception handle
                }
                return transactionStatus；
        }
}
```

消息队列

```
    }
    int main(int argc, char* argv[])
    {
```

`//`创建`Producer`和发送消息所必需的信息。

```
        ONSFactoryProperty factoryInfo;
        factoryInfo.setFactoryProperty(ONSFactoryProperty::ProducerId, "XXX");
```

`//`设置`TCP`接入域名，进入消息队列`RocketMQ`版控制台实例详情页面的接入点区域查看。

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR, "XXX");
        factoryInfo.setFactoryProperty(ONSFactoryProperty::PublishTopics,"XXX" );
```

`//`消息内容。

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty::MsgContent, "XXX");
        //请确保环境变量ALIBABA_CLOUD_ACCESS_KEY_ID、ALIBABA_CLOUD_ACCESS_KEY_SECRET已设
```

置。 `//AccessKey ID`，阿里云身份验证标识。

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"));
```

`//AccessKey Secret`，阿里云身份验证密钥。

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
```

`//`创建`producer`，消息队列`RocketMQ`版不负责`pChecker`的释放，需要业务方自行释放资源。

```
        MyLocalTransactionChecker *pChecker = new MyLocalTransactionChecker();
        g_producer = ONSFactory::getInstance()-
>createTransactionProducer(factoryInfo,pChecker);
```

`//`在发送消息前，必须调用`start`方法来启动`Producer`，只需调用一次即可。

```
        pProducer->start();
        Message msg(
            //Message Topic
            factoryInfo.getPublishTopics(),
```

`//Message Tag`，可理解为`Gmail`中的标签，对消息进行再归类，方便`Consumer`指定过滤条件在

```
            "TagA",
```

`//Message Body`，不能为空，消息队列`RocketMQ`版不做任何干预，需要`Producer`与`Consumer` 协商好一致的序列化和反序列化方式。

```
            factoryInfo.getMessageContent()
        );
```

`//` 设置代表消息的业务关键属性，请尽可能全局唯一。 `//` 以方便您在无法正常收到消息情况下，可通过消息队列`RocketMQ`版控制台查询消息并补发。 `//` 注意：不设置也不会影响消息正常收发。

```
        msg.setKey("ORDERID_100");
```

`//`发送消息，只要不抛出异常，就代表发送成功。

```
        try
        {
```

`//`消息队列`RocketMQ`版不负责`pExecuter`的释放，需要业务方自行释放资源。

```
            MyLocalTransactionExecuter pExecuter = new MyLocalTransactionExecuter();
            SendResultONS sendResult = pProducer->send(msg,pExecuter);
        }
catch(ONSClientException&e)
```

消息队列

```
        catch(ONSClientException & e)
        {
```

`//`自定义处理`exception`的细节。

```
        }
```

`//` 在应用退出前，必须销毁`Producer`对象，否则会导致内存泄露等问题。

```
        pProducer->shutdown();
        return 0;
    }
```

2. 提交事务消息状态。
当本地事务执行完成（执行成功或执行失败），需要通知服务器当前消息的事务状态。通知方式有以下两种： 执行本地事务完成后提交。 执行本地事务一直没提交状态，等待服务器回查消息的事务状态。 事务状态有以下三种：
**TransactionStatus.CommitTransaction**提交事务，允许订阅方消费该消息；
**TransactionStatus.RollbackTransaction**回滚事务，消息将被丢弃不允许消费；
**TransactionStatus.Unknow**无法判断状态，期待RocketMQ Broker向发送方再次询问该消息对应
的本地事务的状态。 消息队列

```
 class MyLocalTransactionChecker : LocalTransactionChecker
 {
     MyLocalTransactionChecker()
     {
     }
     ~MyLocalTransactionChecker()
     {
     }
     virtual TransactionStatus check(Message &value)
     {
```

`//` 消息 `ID(`有可能消息体一样，但消息 `ID` 不一样, 当前消息 `ID` 在 `console` 控制无法查询)

```
         string msgId = value.getMsgID();
```

`//` 消息体内容进行 `crc32,` 也可以使用其它的如 `MD5` `//` 消息 `ID` 和 `crc32id` 主要是用来防止消息重复 `//` 如果业务本身是幂等的, 可以忽略, 否则需要利用 `msgId` 或 `crc32Id` 来做幂等 `//` 如果要求消息绝对不重复, 推荐做法是对消息体 `body` 使用 `crc32` 或 `MD5` 来防止重复消息.

```
         TransactionStatus transactionStatus = Unknow;
         try {
```

`boolean isCommit =` 本地事务执行结果;

```
             if (isCommit) {
```

`//` 本地事务成功、提交消息

```
                 transactionStatus = CommitTransaction;
             } else {
```

`//` 本地事务失败、回滚消息

```
                 transactionStatus = RollbackTransaction;
             }
         } catch(...) {
             //exception error
         }
         return transactionStatus；
     }
 }
```

**事务回查机制说明**

发送事务消息为什么必须要实现check机制？ 当步骤1发送半事务消息完成，但本地事务返回状态为**TransactionStatus.Unknow**时，亦或是应用退出导致本地事务未提交任何状态时，从RocketMQ Broker的角度看，这条半事务消息的状态是未知的，因此RocketMQ Broker会定期要求发送方能check该半事务消息，并上报其最终状态。 Check被回调时，业务逻辑都需要做些什么？ RocketMQ事务消息的check方法里面，应该写一些检查事务一致性的逻辑。RocketMQ发送事务消息时需要实现**LocalTransactionChecker**接口，用来处理RocketMQ Broker主动发起的本地事务状态回查请求；因此在事务消息的check方法中，需要完成两件事情： i. 检查该半事务消息对应的本地事务的状态（committed or rollback）； ii. 向RocketMQ Broker提交该半事务消息本地事务的状态。 本地事务的不同状态对半事务消息的影响？
**TransactionStatus.CommitTransaction**提交事务，允许订阅方消费该消息。
**TransactionStatus.RollbackTransaction**回滚事务，消息将被丢弃不允许消费。
**TransactionStatus.Unknow**无法判断状态，期待RocketMQ Broker向发送方再次询问该消息对
应的本地事务的状态。 消息队列具体代码详见**MyLocalTransactionChecker**的实现。

**订阅事务消息**

订阅事务消息的说明和示例代码，具体操作方式请参见订阅消息。

##### 订阅消息

本文介绍如何通过RocketMQ的SDK使用C/C++语言进行消息订阅。

**说明**

请确保同一个Group ID下所有Consumer实例的订阅关系保持一致，具体内容请参见订阅关系一致。

**订阅方式**

RocketMQ支持以下两种订阅方式：

**集群订阅：**

用于实现集群消费。集群消费是指同一个Group ID所标识的所有Consumer平均分摊消费消息。例如某个Topic有9条消息，一个Group ID有3个Consumer实例，那么在集群消费模式下每个实例平均分摊， 只消费其中的3条消息。 `//` 集群订阅方式设置（不设置的情况下，默认为集群订阅方式）

```
 factoryInfo.setFactoryProperty(ONSFactoryProperty:: MessageModel,
ONSFactoryProperty::CLUSTERING);
```

**广播订阅：**

用于实现广播消费。广播消费是指同一个Group ID所标识的所有Consumer都会各自消费某条消息一次。例如某个Topic有9条消息，一个Group ID有3个Consumer实例，那么在广播消费模式下每个实例都会各自消费9条消息。 `//` 广播订阅方式设置

```
 factoryInfo.setFactoryProperty(ONSFactoryProperty:: MessageModel,
ONSFactoryProperty::BROADCASTING);
```

**示例代码**

```
#include "ONSFactory.h"
#include <iostream>
#include <thread>
#include <mutex>
using namespace ons; std::mutex console_mtx; class ExampleMessageListener : public MessageListener { public:
    Action consume(Message& message, ConsumeContext& context) {
```

`//`此处为具体的消息处理过程，确认消息被处理成功请返回`CommitMessage`。 `//`如果有消费异常，或者期望重新消费，可以返回`ReconsumeLater`，消息将会在一段时间后重新投递。

```
        std::lock_guard<std::mutex> lk(console_mtx);
        std::cout << "Received a message. Topic: " << message.getTopic() << ", MsgId: "
<<messagegetMsgID()<<std::endl;
```

消息队列

```
        << message.getMsgID() << std::endl;
        return CommitMessage;
    }
}; int main(int argc, char* argv[]) {
    std::cout << "=======Before consuming messages=======" << std::endl;
    ONSFactoryProperty factoryInfo;
```

`//`请填写在阿里云消息队列`RocketMQ`版控制台上申请的`Group ID`，从实例化的版本开始，`ProducerId`和 `CounsumerId`已经统一，此处设置是为了接口保持向前兼容。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::ConsumerId, "GID_XXX");
```

`//`请确保环境变量`ALIBABA_CLOUD_ACCESS_KEY_ID`、`ALIBABA_CLOUD_ACCESS_KEY_SECRET`已设置。 `//AccessKey ID`，阿里云身份验证标识。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::AccessKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"));
```

`//AccessKey Secret`，阿里云身份验证密钥。

```
    factoryInfo.setFactoryProperty(ONSFactoryProperty::SecretKey,
getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
    factoryInfo.setFactoryProperty(ONSFactoryProperty::NAMESRV_ADDR,
"http://xxxxxxxxxxxxxxxx.aliyuncs.com:80");
    PushConsumer *consumer = ONSFactory::getInstance()-
>createPushConsumer(factoryInfo);
    const char* topic_1 = "topic-1";
```

`//` 订阅`topic-1`中`Tag`消息属性为`tag-1`的所有消息。

```
    const char* tag_1 = "tag-1";
    const char* topic_2 = "topic-2";
```

`//` 订阅`topic-2`的所有消息。

```
    const char* tag_2 = "*";
```

`//`请注册自定义侦听函数用来处理接收到的消息，并返回响应的处理结果。

```
    ExampleMessageListener * message_listener = new ExampleMessageListener();
    consumer->subscribe(topic_1, tag_1, message_listener);
    consumer->subscribe(topic_2, tag_2, message_listener);
```

`//`准备工作完成，必须调用启动函数，才可以正常工作。

```
    consumer->start();
```

`//`请保持线程常驻，不要执行`shutdown`操作。

```
    std::this_thread::sleep_for(std::chrono::milliseconds(60 * 1000));
    consumer->shutdown();
    delete message_listener;
    std::cout << "=======After consuming messages======" << std::endl;
    return 0;
}
```

#### 7.2.6. .NET SDK

消息队列

##### 7.2.6.1. .NET SDK环境准备

###### 环境准备概述

本文为您介绍使用.NET SDK方式接入RocketMQ的准备工作，以便后续使用.NET SDK收发消息。

**说明**

代码里涉及到的Topic和Group ID，需要到控制台上创建。Message Tag可以完全由应用自定义，具体创建过程可参见创建资源。 使用RocketMQ服务的应用程序需要部署在阿里云ECS上。

###### 下载SDK

RocketMQ提供的.NET版本是基于RocketMQ CPP版本的托管封装，这样能保证.NET完全不依赖于 Windows .NET公共库，内部采用C++多线程并发处理，保证.NET版本的高效稳定。

**背景信息**

在使用VS开发.NET的应用程序和类库时，默认的目标平台为“Any CPU”，即运行时可根据CPU类型自动选择X86或X64。拥有这样的能力是因为. NET编译后的程序集是基于IL的。在运行时，CLR才会将其JIT发射为X86或X64的机器码。而C或C++编译生成的DLL就是机器码。所以，其平台的决策是在编译时决定的。 通过编译选项的设置，我们将C/C++项目编译为X64的64位DLL，因此我们提供了包含VS2015编译的 release64位版本DLL。其他VS版本也可以使用。 C++ DLL 文件需要 Virtual C++ 2015 运行时环境安装包。如果没有安装 Visual

**说明**

Studio 2015 运行时环境，请执行 SDK 中提供的 vc_redist.x64.exe 来完成安装。

**操作步骤**

1. 下载依赖SDK包链接。
新用户或者不考虑升级成本的老用户请下载新版 SDK。新版Windows .NET SDK下载
2. 下载完成后，解压压缩包。
解压完成后，会有如下目录结构： demo/ 包含了普通消息发送、Oneway消息发送、顺序消息发送、普通消息消费、顺序消息消费等例子。 lib/ 底层的C++ DLL相关文件，以及Virtual C++ 2015运行时环境安装包。如果没有安装 Visual Studio 2015 运行时环境，需要拷贝安装 vc_redist.x64.exe，如下所示。

```
  64/
      NSClient4CPP.lib
      ONSClient4CPP.dll
      ONSClient4CPP.pdb
```

interface/ 封装PINVOKE调用的代码，需要包含到用户项目代码中。 SDK_GUIDE.pdf 消息队列 SDK环境准备文档和FAQ。 changelog 新版本发布解决的问题和引入的新特性列表。

###### 7.2.6.1.3. .NET SDK配置说明

本文介绍如何在Windows中使用.NET SDK 。

**操作步骤**

Visual Studio 2015环境下使用.NET SDK
1. 使用Visual Studio 2015创建自己的项目。
图 1. .NET SDK-1
2. 右键单击项目选择**添加**>**现存在项**将下载的SDK中的**interface**目录下的所有文件都添加进去。
图 2. .NET SDK-2
3. 右键单击项目选择**属性**，选择**配置管理器**。设置**活动解决方案配置**为**release**；设置**活动解决方案平**
台为**x64**。 消息队列
4. 编写测试程序，然后进行编译，最后将SDK下的dll放到和可执行文件同一级目录下，或者系统目录下即可
运行。 图 3. .NET SDK-3 SDK提供了设置好的Demo，直接打开工程进行编译即可。运行的时候将相关的DLL文

**说明**

件拷贝到和可执行文件同级目录下，如下图： 图 4. .NET SDK-4

**Visual Studio 2015配置ASP.NET使用RocketMQ SDK**

5. 使用VS2015创建一个ASP.NET的**Web Forms**项目。
图 5. .NET SDK-5 消息队列
6. 右键单击项目选择**属性**，选择**配置管理器**。设置**活动解决方案配置**为**release**；设置**活动解决方案平**
台为**x64**。 图 6. .NET SDK-6
7. 右键单击项目选择**添加**>**现存在项**，将下载的SDK中的interface目录下的所有文件都添加进去。
请参考上文中配置普通的.net 项目的步骤2。
8. 在**Global.asax.cs**文件中添加启动和关闭SDK的代码。
建议将SDK的代码封装成一个单例类，这样可以避免因为作用域的问题被垃圾回收器回

**说明**

收。SDK的example目录下提供了一个Example.cs，实现了一个简单的单例实现。您需要把 Example.cs包含到自己的项目中才能使用。 消息队列

```
using System; using System.Collections.Generic; using System.Linq; using System.Web; using System.Web.Optimization; using System.Web.Routing; using System.Web.Security; using System.Web.SessionState;
```

using ons; // 这个命名空间是`SDK`所在的命名空间 using test; // 这是一个简单封装`SDK`的类所在命名空间，见`SDK`的`example`目录下的`Example.cs`

```java
namespace WebApplication4 {
    public class Global : HttpApplication
    {
        void Application_Start(object sender, EventArgs e)
        {
            // Code that runs on application startup
            RouteConfig.RegisterRoutes(RouteTable.Routes);
            BundleConfig.RegisterBundles(BundleTable.Bundles);
            try
            {
```

`//` 启动`SDK`的代码，下面是简单封装`SDK`后的代码

```
                OnscSharp.CreateProducer();
                OnscSharp.StartProducer();
            }
            catch (Exception ex)
            {
```

`//`处理异常

```
            }
        }
        protected void Application_End(object sender, EventArgs e)
        {
            try
            {
```

`//` 关闭`SDK`的代码

```
              OnscSharp.ShutdownProducer();
            }
            catch (Exception ex)
            {
```

`//` 处理异常

```
            }
        }
    }
}
```

9. 编写测试程序，然后进行编译。
0. 将SDK下的dll 放到和可执行文件同一级目录下，或者系统目录下即可运行。
图 7. .NET SDK-7 消息队列
1. 依次单击**工具**>**选项**>**项目和解决方案**>**Web** **项目**，然后勾选对网站和项目使用**IIS Express**的64位
版。 图 8. .NET SDK-8 图 9. .NET SDK-9 消息队列

##### 收发普通消息

**发送普通消息**

您可以运行以下代码进行消息发送。请按说明正确设置相关参数。 消息队列

```java
using System; using ons; public class ProducerExampleForEx {
    public ProducerExampleForEx()
    {
    }
    static void Main(string[] args) {
```

`//` 配置账号, 从控制台获取设置

```
        ONSFactoryProperty factoryInfo = new ONSFactoryProperty();
```

`// AccessKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.AccessKey, "Your access
key");
```

`// SecretKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.SecretKey, "Your access
secret");
```

`//` 您在控制台创建的 `Group ID`

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.ProducerId, "GID_example");
```

`//` 您在控制台创建的 `Topic`

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.PublishTopics,
"T_example_topic_name");
```

`//` 设置 `TCP` 接入域名，进入控制台的实例管理页面的“获取接入点信息”区域查看

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.NAMESRV_ADDR,
"NameSrv_Addr");
```

`//` 设置日志路径

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.LogPath, "C://log");
```

`//` 创建生产者实例 `//` 说明：生产者实例是线程安全的，可用于发送不同 `Topic` 的消息。基本上，您每一个线程 `//` 只需要一个生产者实例

```
        Producer producer = ONSFactory.getInstance().createProducer(factoryInfo);
```

`//` 启动客户端实例

```
        producer.start();
```

`//` 创建消息对象

```
        Message msg = new Message(factoryInfo.getPublishTopics(), "tagA", "Example mess
age body");
        msg.setKey(Guid.NewGuid().ToString());
        for (int i = 0; i < 32; i++) {
            try
            {
                SendResultONS sendResult = producer.send(msg);
                Console.WriteLine("send success {0}", sendResult.getMessageId());
            }
            catch (Exception ex)
            {
                Console.WriteLine("send failure{0}", ex.ToString());
            }
        }
```

`//` 在您的线程即将退出时，关闭生产者实例

```
        producer.shutdown();
    }
}
```

### 订阅消息

消息队列订阅普通消息的说明和示例代码，具体操作方式请参见订阅消息。

##### 收发顺序消息

**发送顺序消息**

发送顺序消息的示例代码如下： 消息队列

```java
using System; using ons; public class OrderProducerExampleForEx {
    public OrderProducerExampleForEx()
    {
    }
    static void Main(string[] args) {
```

`//` 配置您的账号，以下设置均可从控制台获取

```
        ONSFactoryProperty factoryInfo = new ONSFactoryProperty();
```

`// AccessKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.AccessKey, "Your access
key");
```

`// SecretKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.SecretKey, "Your access
secret");
```

`//` 您在控制台创建的 `Group ID`

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.ProducerId, "GID_example");
```

`//` 您在控制台创建的 `Topic`

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.PublishTopics,
"T_example_topic_name");
```

`//` 设置 `TCP` 接入域名，进入控制台的实例管理页面的“获取接入点信息”区域查看

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.NAMESRV_ADDR,
"NameSrv_Addr");
```

`//` 设置日志路径

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.LogPath, "C://log");
```

`//` 创建生产者实例 `//` 说明：生产者实例是线程安全的，可用于发送不同 `Topic` 的消息。基本上，您每一个线程 `//` 只需要一个生产者实例

```
        OrderProducer producer =
ONSFactory.getInstance().createOrderProducer(factoryInfo);
```

`//` 启动客户端实例

```
        producer.start();
```

`//` 创建消息对象

```
        Message msg = new Message(factoryInfo.getPublishTopics(), "tagA", "Example mess
age body");
        string shardingKey = "App-Test";
        for (int i = 0; i < 32; i++) {
            try
            {
                SendResultONS sendResult = producer.send(msg, shardingKey);
                Console.WriteLine("send success {0}", sendResult.getMessageId());
            }
            catch (Exception ex)
            {
                Console.WriteLine("send failure{0}", ex.ToString());
            }
        }
```

`//` 在您的线程即将退出时，关闭生产者实例

```
        producer.shutdown();
    }
}
```

消息队列

**消费顺序消息**

消费顺序消息的示例代码如下：

```java
using System; using System.Text; using System.Threading; using ons; namespace demo {
    public class MyMsgOrderListener : MessageOrderListener
    {
        public MyMsgOrderListener()
        {
        }
        ~MyMsgOrderListener()
        {
        }
        public override ons.OrderAction consume(Message value, ConsumeOrderContext cont
ext)
        {
            Byte[] text = Encoding.Default.GetBytes(value.getBody());
            Console.WriteLine(Encoding.UTF8.GetString(text));
            return ons.OrderAction.Success;
        }
    }
    class OrderConsumerExampleForEx
    {
        static void Main(string[] args)
        {
```

`//` 配置您的账号，以下设置均可从控制台获取

```
            ONSFactoryProperty factoryInfo = new ONSFactoryProperty();
```

`// AccessKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
            factoryInfo.setFactoryProperty(ONSFactoryProperty.AccessKey, "Your access
key");
```

`// SecretKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
            factoryInfo.setFactoryProperty(ONSFactoryProperty.SecretKey, "Your access
secret");
```

`//` 您在控制台创建的 `Group ID`

```
            factoryInfo.setFactoryProperty(ONSFactoryProperty.ConsumerId,
"GID_example");
```

`//` 您在控制台创建的 `Topic`

```
            factoryInfo.setFactoryProperty(ONSFactoryProperty.PublishTopics,
"T_example_topic_name");
```

`//` 设置 `TCP` 接入域名，进入控制台的实例管理页面的“获取接入点信息”区域查看

```
            factoryInfo.setFactoryProperty(ONSFactoryProperty.NAMESRV_ADDR,
"NameSrv_Addr");
```

`//` 设置日志路径

```
            factoryInfo.setFactoryProperty(ONSFactoryProperty.LogPath, "C://log");
```

`//` 创建消费者实例

```
            OrderConsumer consumer =
ONSFactory.getInstance().createOrderConsumer(factoryInfo);
```

`//` 订阅 `Topic`

```
            consumer.subscribe(factoryInfo.getPublishTopics(), "*",new
MyMsgOrderListener());
```

消息队列 y g `//` 启动消费者实例

```
            consumer.start();
```

`//` 让主线程睡眠一段时间

```
            Thread.Sleep(30000);
```

`//` 不再使用时，关闭消费者实例

```
            consumer.shutdown();
        }
    }
}
```

##### 收发定时消息

定时消息可以做到在指定时间之后才可被消费者消费，用于解决一些消息生产和消费有时间窗口要求的场景，或者通过消息触发定时任务的场景，类似于延迟队列。

**发送定时消息**

发送定时消息的代码示例如下：

```
using System; using System.Collections.Generic; using System.Linq; using System.Text; using System.Runtime.InteropServices; using ons; namespace ons {
    class onscsharp
    {
        static void Main(string[] args)
        {
```

`//producer` 创建和正常工作的参数，必须输入

```
            ONSFactoryProperty factoryInfo = new ONSFactoryProperty();
            factoryInfo.setFactoryProperty(factoryInfo.ProducerId, "XXX ");//您在控制台创
```

建的 `Group ID`

```
            factoryInfo.setFactoryProperty(factoryInfo.NAMESRV_ADDR, "XXX"); //设置 TCP
```

接入域名，进入控制台的实例管理页面的“获取接入点信息”区域查看

```
            factoryInfo.setFactoryProperty(factoryInfo.PublishTopics, "XXX");//您在控制台
```

创建的 `Topic`

```
            factoryInfo.setFactoryProperty(factoryInfo.MsgContent, "XXX");//消息内容
            factoryInfo.setFactoryProperty(factoryInfo.AccessKey, "XXX");//AccessKey 阿
```

里云身份验证，在阿里云服务器管理控制台创建

```
            factoryInfo.setFactoryProperty(factoryInfo.SecretKey,"XXX");//SecretKey 阿里
```

云身份验证，在阿里云服务器管理控制台创建 `//`创建 `producer`

```
            ONSFactory onsfactory = new ONSFactory();
            Producer pProducer = onsfactory.getInstance().createProducer(factoryInfo);
```

`//`在发送消息前，必须调用 `start` 方法来启动 `Producer`，只需调用一次即可

```
            pProducer.start();
            Message msg = new Message(
                //Message Topic
                factoryInfo.getPublishTopics(),
                //Message Tag
"TagA",
```

消息队列

```
                TagA,
                //Message Body
                factoryInfo.getMessageContent()
            );
```

`//` 设置代表消息的业务关键属性，请尽可能全局唯一。 `//` 以方便您在无法正常收到消息情况下，可通过 `MQ Console` 查询消息并补发。 `//` 注意：不设置也不会影响消息正常收发

```
            msg.setKey("ORDERID_100");
```

`// deliver time` 单位 `ms`，指定一个时刻，在这个时刻之后才能被消费，这个例子表示`3s` 后才能被消费 `long deliverTime =` 获取系统当前时间(ms) + 3000;

```
            msg.setStartDeliverTime(deliverTime);
```

`//`发送消息，只要不抛出异常，就代表发送成功

```
            try
            {
                SendResultONS sendResult = pProducer.send(msg);
            }
            catch(ONSClientException e)
            {
```

`//`发送失败处理

```
            }
```

`//` 在应用退出前，必须销毁 `Producer` 对象，否则会导致内存泄露等问题

```
            pProducer.shutdown();
        }
    }
}
```

**订阅定时消息**

订阅定时消息的说明和示例代码，具体操作方式请参见订阅消息。

##### 收发事务消息

本文介绍事务消息的交互流程、收发方式、示例代码及回查机制。

**交互流程**

RocketMQ事务消息的交互流程如下图所示： 图 1. 事务消息交互流程

**发送事务消息**

发送事务消息包含以下两个步骤：
1. 发送半事务消息（Half Message）及执行本地事务。示例代码如下：
消息队列

```java
 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Runtime.InteropServices;
 using ons;
 namespace ons
 {
 public class MyLocalTransactionExecuter : LocalTransactionExecuter
 {
     public MyLocalTransactionExecuter()
     {
     }
     ~MyLocalTransactionExecuter()
     {
     }
     public override TransactionStatus execute(Message value)
     {
             Console.WriteLine("execute topic: {0}, tag:{1}, key:{2}, msgId:
{3},msgbody:{4}, userProperty:{5}",
             value.getTopic(), value.getTag(), value.getKey(), value.getMsgID(), value
.getBody(), value.getUserProperty("VincentNoUser"));
```

`//` 消息 `ID(`有可能消息体一样，但消息 `ID` 不一样。当前消息 `ID` 在控制台无法查询)

```
             string msgId = value.getMsgID();
```

`//` 消息体内容进行 `crc32,` 也可以使用其它的如 `MD5` `//` 消息 `ID` 和 `crc32id` 主要是用来防止消息重复 `//` 如果要求消息绝对不重复，推荐做法是对消息体 `body` 使用 `crc32`或 `MD5` 来防止重复消息

```
             TransactionStatus transactionStatus = TransactionStatus.Unknow;
             try {
```

`boolean isCommit =` 本地事务执行结果;

```
                 if (isCommit) {
```

`//` 本地事务成功则提交消息

```
                     transactionStatus = TransactionStatus.CommitTransaction;
                 } else {
```

`//` 本地事务失败则回滚消息

```
                     transactionStatus = TransactionStatus.RollbackTransaction;
                 }
             } catch (Exception e) {
                 //exception handle
             }
             return transactionStatus；
     }
 }
 class onscsharp
 {
     static void Main(string[] args)
     {
         ONSFactoryProperty factoryInfo = new ONSFactoryProperty();
         factoryInfo.setFactoryProperty(factoryInfo.NAMESRV_ADDR, "XXX");//设置 TCP 接
```

入域名，进入控制台的实例管理页面的“获取接入点信息”区域查看

```
         factoryInfo.setFactoryProperty(factoryInfo.ProducerId, "");//您在控制台创建的 G
roup ID
         factoryInfo.setFactoryProperty(factoryInfo.PublishTopics, "");// 您在控制台创建
```

的 `Topic` 消息队列

```
         factoryInfo.setFactoryProperty(factoryInfo.MsgContent, "");//message body
         factoryInfo.setFactoryProperty(factoryInfo.AccessKey, "");//AccessKey 阿里云身
```

份验证，在阿里云服务器管理控制台创建

```
         factoryInfo.setFactoryProperty(factoryInfo.SecretKey, "");//SecretKey 阿里云身
```

份验证，在阿里云服务器管理控制台创建

```
         //create transaction producer
         ONSFactory onsfactory = new ONSFactory();
         LocalTransactionChecker myChecker = new MyLocalTransactionChecker();
         TransactionProducer pProducer =
onsfactory.getInstance().createTransactionProducer(factoryInfo,ref myChecker);
```

`//` 在发送消息前，必须调用 `start` 方法来启动 `Producer`，只需调用一次即可，启动之后可以多线程并发发送消息

```
         pProducer.start();
             Message msg = new Message(
             //Message Topic
             factoryInfo.getPublishTopics(),
             //Message Tag
             "TagA",
             //Message Body
             factoryInfo.getMessageContent()
         );
```

`//` 设置代表消息的业务关键属性，请尽可能全局唯一 `//` 以方便您在无法正常收到消息情况下，可通过控制台查询消息并补发。 `//` 注意：不设置也不会影响消息正常收发

```
         msg.setKey("ORDERID_100");
```

`//` 发送消息，只要不抛出异常，就代表发送成功

```
         try
         {
             LocalTransactionExecuter myExecuter = new MyLocalTransactionExecuter();
             SendResultONS sendResult = pProducer.send(msg, ref myExecuter);
         }
         catch(ONSClientException e)
         {
             Console.WriteLine("\nexception of sendmsg:{0}",e.what() );
         }
```

`//` 在应用退出前，必须销毁 `Producer` 对象，否则会导致内存泄露等问题； `// shutdown` 之后不能重新 `start` 此 `producer`

```
         pProducer.shutdown();
     }
 }
 }
```

2. 提交事务消息状态。
当本地事务执行完成（执行成功或执行失败），需要通知服务器当前消息的事务状态。通知方式有以下两种： 执行本地事务完成后提交。 执行本地事务一直没提交状态，等待服务器回查消息的事务状态。 事务状态有以下三种：
**TransactionStatus.CommitTransaction**提交事务，允许订阅方消费该消息；
**TransactionStatus.RollbackTransaction**回滚事务，消息将被丢弃不允许消费；
消息队列
**TransactionStatus.Unknow**无法判断状态，期待RocketMQ Broker向发送方再次询问该消息对
应的本地事务的状态。

```java
    public class MyLocalTransactionChecker : LocalTransactionChecker
    {
        public MyLocalTransactionChecker()
        {
        }
        ~MyLocalTransactionChecker()
        {
        }
        public override TransactionStatus check(Message value)
        {
                Console.WriteLine("check topic: {0}, tag:{1}, key:{2}, msgId:
{3},msgbody:{4}, userProperty:{5}",
                value.getTopic(), value.getTag(), value.getKey(), value.getMsgID(), va
lue.getBody(), value.getUserProperty("VincentNoUser"));
```

`//` 消息 `ID(`有可能消息体一样，但消息 `ID` 不一样。当前消息 `ID` 在控制台无法查询)

```
                string msgId = value.getMsgID();
```

`//` 消息体内容进行 `crc32,` 也可以使用其它的如 `MD5` `//` 消息 `ID` 和 `crc32id` 主要是用来防止消息重复 `//` 如果业务本身是幂等的，可以忽略，否则需要利用 `msgId` 或 `crc32Id` 来做幂等 `//` 如果要求消息绝对不重复，推荐做法是对消息体 `body` 使用 `crc32`或 `MD5` 来防止重复消息

```
                TransactionStatus transactionStatus = TransactionStatus.Unknow;
                try {
```

`boolean isCommit =` 本地事务执行结果;

```
                    if (isCommit) {
```

`//` 本地事务成功、提交消息

```
                        transactionStatus = TransactionStatus.CommitTransaction;
                    } else {
```

`//` 本地事务失败、回滚消息

```
                        transactionStatus = TransactionStatus.RollbackTransaction;
                    }
                } catch (Exception e) {
                    //exception handle
                }
                return transactionStatus；
        }
        }
```

**事务回查机制说明**

发送事务消息为什么必须要实现check机制？ 当步骤1半事务消息发送完成，但本地事务返回状态为**TransactionStatus.Unknow**时，亦或是应用退出导致本地事务未提交任何状态时，从RocketMQ Broker的角度看，这条半事务消息的状态是未知的，因此RocketMQ Broker会定期要求发送方能check该半事务消息，并上报其最终状态。 Check被回调时，业务逻辑都需要做些什么？ RocketMQ事务消息的check方法里面，应该写一些检查事务一致性的逻辑。RocketMQ发送事务消息时需要实现**LocalTransactionChecker**接口，用来处理RocketMQ Broker主动发起的本地事务状态回查请求；因此在事务消息的check方法中，需要完成两件事情： i. 检查该半事务消息对应的本地事务的状态（committed or rollback）； ii. 向RocketMQ Broker提交该半事务消息本地事务的状态。 消息队列本地事务的不同状态对半事务消息的影响？
**TransactionStatus.CommitTransaction**提交事务，允许订阅方消费该消息；
**TransactionStatus.RollbackTransaction**回滚事务，消息将被丢弃不允许消费；
**TransactionStatus.Unknow**无法判断状态，期待RocketMQ Broker向发送方再次询问该消息对
应的本地事务的状态。 具体代码详见**MyLocalTransactionChecker**的实现。

**订阅事务消息**

订阅事务消息的说明和示例代码，具体操作方式请参见订阅消息。

##### 订阅消息

本文介绍如何通过RocketMQ SDK使用.NET语言进行消息订阅。

**说明**

请确保同一个Group ID下所有Consumer实例的订阅关系保持一致，具体内容请参见订阅关系一致。

**订阅方式**

RocketMQ支持以下两种订阅方式：
**集群订阅：**同一个Group ID所标识的所有Consumer平均分摊消费消息。例如某个Topic有9条消息，一
个Group ID有3个Consumer实例，那么在集群消费模式下每个实例平均分摊，只消费其中的3条消息。 `//` 集群订阅方式设置（不设置的情况下，默认为集群订阅方式）

```
 factoryInfo.setFactoryProperty(ONSFactoryProperty.MessageModel,
ONSFactoryProperty.CLUSTERING);
```

**广播订阅：**同一个Group ID所标识的所有Consumer都会各自消费某条消息一次。例如某个Topic有9条
消息，一个Group ID有3个Consumer实例，那么在广播消费模式下每个实例都会各自消费9条消息。 `//` 广播订阅方式设置

```
 factoryInfo.setFactoryProperty(ONSFactoryProperty.MessageModel,
ONSFactoryProperty.BROADCASTING);
```

**示例代码**

```
using System; using System.Threading; using System.Text; using ons;
```

`//` 从 `Broker` 拉取消息时要执行的回调函数

```java
public class MyMsgListener : MessageListener {
    public MyMsgListener()
    {
    }
    ~MyMsgListener()
    {
    }
    public override ons.Action consume(Message value, ConsumeContext context)
{
```

消息队列

```java
    {
        Byte[] text = Encoding.Default.GetBytes(value.getBody());
        Console.WriteLine(Encoding.UTF8.GetString(text));
        return ons.Action.CommitMessage;
    }
} public class ConsumerExampleForEx {
    public ConsumerExampleForEx()
    {
    }
    static void Main(string[] args) {
```

`//` 配置您的账号，以下设置均可从控制台获取

```
        ONSFactoryProperty factoryInfo = new ONSFactoryProperty();
```

`// AccessKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.AccessKey, "Your access
key");
```

`// SecretKey` 阿里云身份验证，在阿里云服务器管理控制台创建

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.SecretKey, "Your access
secret");
```

`//` 您在控制台创建的 `Group ID`

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.ConsumerId, "GID_example");
```

`//` 您在控制台创建的 `Topic`

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.PublishTopics,
"T_example_topic_name");
```

`//` 设置 `TCP` 接入域名，进入控制台的实例管理页面的“获取接入点信息”区域查看

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.NAMESRV_ADDR,
"NameSrv_Addr");
```

`//` 设置日志路径

```
        factoryInfo.setFactoryProperty(ONSFactoryProperty.LogPath, "C://log");
```

`//` 集群消费

```
        // factoryInfo.setFactoryProperty(ONSFactoryProperty:: MessageModel,
ONSFactoryProperty.CLUSTERING);
```

`//` 广播消费

```
        // factoryInfo.setFactoryProperty(ONSFactoryProperty:: MessageModel,
ONSFactoryProperty.BROADCASTING);
```

`//` 创建消费者实例

```
        PushConsumer consumer =
ONSFactory.getInstance().createPushConsumer(factoryInfo);
```

`//` 订阅 `Topics`

```
        consumer.subscribe(factoryInfo.getPublishTopics(), "*", new MyMsgListener());
```

`//` 启动客户端实例

```
        consumer.start();
```

`//`该设置仅供 `demo` 使用，实际生产中请保证进程不退出

```
        Thread.Sleep(300000);
```

`//` 在进程即将退出时，关闭消费者实例

```
        consumer.shutdown();
    }
}
```

### HTTP协议SDK参考

消息队列

#### 协议说明

##### 公共参数

本文介绍云消息队列 RocketMQ 版的HTTP请求Header中的公共请求参数和公共返回参数。

**公共请求头**

| 参数 | 是否必选 |  |  | 说明 |  |  |
|---|---|---|---|---|---|---|
| Authorization | 是 |  |  | 验证字符串，由 MQ+空格+ |  |  |
|  |  |  |  |  | MQ+空格+ |  |
|  |  |  |  | <AccessKeyId>+:+ |  |  |
|  |  |  |  | <Signature> |  |  |
| Content-Length | 是 |  |  | HTTP请求Body的长度。 |  |  |
| Content-Type | 是 |  |  | 请求内容的MIME类型，目前请求仅支持text/xml; charset=utf-8，即 MIME类型为XML，编码字符集为 UTF-8。 |  |  |
| Date | 是 |  |  | 请求的构造时间，目前只支持GMT 格式，如果和云消息队列 RocketMQ 版的服务器时间前后差异超过15分钟将返回本次请求非法。 |  |  |
| Host | 是 |  |  | 即在控制台实例详情页面的网络管理页签查看到的HTTP接入点。 |  |  |
| x-mq-version | 是 |  |  | 调用云消息队列 RocketMQ 版的版本号，当前版本为2015-06-06。 |  |  |
| Content-MD5 | 否 |  |  | HTTP消息体的MD5值。具体格式， 请参见Content-MD5 Header Field。 |  |  |

**公共返回头**

| 参数 | 说明 |
|---|---|
| Content-Length | HTTP响应Body的长度。 |
| Connection | HTTP连接状态。 |

消息队列

| Date | 响应的返回时间，GMT时间格式。 |
|---|---|
| x-mq-request-id | 此次请求的请求序列号。 |
| x-mq-version | API的版本编号，当前版本是2015-06-06。 |

##### 签名机制

云消息队列 RocketMQ 版会验证每个访问的HTTP请求。每个向云消息队列 RocketMQ 版提交的HTTP请求中都包含Authorization，Authorization又包含了签名（Signature）。本文介绍签名的生成机制。

**背景信息**

AccessKey ID和AccessKey Secret由阿里云官方颁发给访问者（可以通过阿里云管理控制台申请和管理），其中： AccessKey ID用于标识访问者的身份。 AccessKey Secret用于加密签名字符串和服务器端验证签名字符串的密钥，必须严格保密。 云消息队列 RocketMQ 版提供的HTTP服务通过使用AccessKey ID和AccessKey Secret进行对称加密的方法来验证请求的发送者身份。如果计算出来的验证码和提供的一样，即认为该请求是有效的；否则，将拒绝处理这次请求，并返回HTTP 403错误。 您必须在HTTP请求中增加Authorization的Header来包含签名信息，表明这个消息已被授权。

**获取方式**

Authorization信息的格式为：

```
 MQ <AccessKey ID>:<Signature>
```

Signature的生成方式如下所示。

```
Signature = base64(hmac-sha1(HTTP_METHOD + "\n"
                + "\n"+ CONTENT-TYPE + "\n"
                + DATE + "\n"
                + "x-mq-version:" + MQVersion + "\n"
                + CanonicalizedResource))
```

**HTTP_METHOD**：表示大写的HTTP Method（如PUT、GET、POST、DELETE）。
**CONTENT-TYPE**：表示请求内容的类型，即为text/xml; charset=utf-8。
**DATE**：表示此次操作的时间，不能为空，目前只支持GMT格式，示例：Thu, 07 Mar 2012 18:49:58
GMT。
**MQVersion**：表示云消息队列 RocketMQ 版接口的版本号，当前版本即为2015-06-06。
**CanonicalizedResource**：表示HTTP所请求资源的URI（统一资源标识符），如消费请求的URI
/topics/abc/messages?consumer=GID_abc。

**说明**

用来签名的字符串为UTF-8格式。 签名的方法用RFC 2104中定义的HMAC-SHA1方法，其中Key为AccessKey Secret。 消息队列

##### 发送消息API

**请求构造**

请求行

```
 POST /topics/TopicName/messages?ns=INSTANCE_ID HTTP/1.1
```

参数说明如下。

| 参数 | 是否必选 | 说明 |
|---|---|---|
| TopicName | 是 | 将消息发送至的Topic名称。 |
| ns | 否 | 实例ID，针对有命名空间的新建实例，该参数为必填。是否有命名空间可以在控制台实例详情页面查看。实例根据其是否有命名空间分为默认实例和新建实例： 默认实例：无命名空间，所有资源命名必需保证全局唯一。 新建实例：有命名空间，资源命名只需保证在该实例内唯一。 实例命名空间的更多信息，请参见资源隔离优化（实例化支持）。 |

请求内容（XML格式） 请求内容的参数说明如下。

| 参数 | 是否必选 | 说明 |
|---|---|---|
| MessageTag | 否 | 消息Tag。 |
| MessageBody | 是 | 消息内容。 |
| Properties | 否 | 消息属性。 |

属性（Properties）的序列化，其中特殊用途的键值说明如下：

```
格式： key1:value1|key2:value2|key3:value3
```

键值说明如下。

| 参数 | 类型 | 说明 |
|---|---|---|
| KEYS | String | 消息的Key。 |
| STARTDELIVERTIME __ | Long | 定时消息的定时绝对时间，UNIX 毫秒时间戳。 |
| TransCheckT __ | Long | 第一次事务消息的回查时间，相对时间，取值范围：10～300，单位：秒。 |

**响应构造**

响应行消息队列

```
 HTTP/1.1 201
```

响应内容响应内容的参数说明如下。

| 参数 | 类型 | 说明 |
|---|---|---|
| MessageId | String | 消息ID。 |
| MessageBodyMD5 | String | 消息内容的MD5。 |

**示例**

请求示例

```xml
<?xml version="1.0" encoding="UTF-8"?> <Message xmlns="http://mq.aliyuncs.com/doc/v1/">
    <MessageBody>a</MessageBody>
<MessageTag>Tag</MessageTag> <Properties>KEYS:MessageKey|__STARTDELIVERTIME:1571388173000</Properties> </Message>
```

响应示例

```xml
<Message xmlns="http://mq.aliyuncs.com/doc/v1/"> <MessageId>1E057D566EAD42A579935B5CD874****</MessageId> <MessageBodyMD5>0CC175B9C0F1B6A831C399E26977****</MessageBodyMD5> </Message>
```

##### 订阅消息API

**请求构造**

请求行

```
 GET /topics/TopicName/messages?
ns=INSTANCE_ID&consumer=GID&tag=taga&numOfMessages=3&waitseconds=3 HTTP/1.1
```

请求行总长度不能超过1024个字符。

**重要**

参数说明如下。

| 参数 | 是否必选 | 说明 |
|---|---|---|
| TopicName | 是 | 将消息发送至的Topic名称。 |

消息队列

| ns | 否 | 实例ID，针对有命名空间的新建实例，该参数为必填。 是否有命名空间可以在控制台实例详情页面查看。实例根据其是否有命名空间分为默认实例和新建实例： 默认实例：无命名空间，所有资源命名在该默认实例内需全局唯一。 新建实例：有命名空间，资源命名只需保证在该实例内唯一。 详细信息，请参见资源隔离优化 （实例化支持）。 |
|---|---|---|
| consumer | 是 | 消费者群组的标识，即Group ID。 |
| tag | 否 | 消息Tag。如果不指定Tag，则拉取所有消息。如果需要指定多个 Tag，则使用双竖线（\|\|）隔开，例如TagA\|\|TagB。 |
| numOfMessages | 是 | 一次最多消费多少条消息，取值范围：1～16。 |
| waitseconds | 否 | 长轮询时间，不填则为短轮询，取值范围：1～30，单位：秒。 |

请求内容（XML格式） 无

**响应构造**

有消息可消费响应行

```
 HTTP/1.1 200
```

消息队列响应内容响应内容的参数说明如下。

| 参数 | 类型 | 说明 |
|---|---|---|
| MessageId | String | 消息ID。 |
| MessageBodyMD5 | String | 消息内容的MD5。 |
| MessageBody | String | 消息内容。 |
| ReceiptHandle | String | 消息的句柄，用于确认消息消费成功，句柄仅使用一次，对于同一条消息如果存在重试每次拿到的句柄是不同的，消息句柄应该在到NextConsumeTime指定的时间之前使用。 |
| PublishTime | String | 消息的发送时间戳，单位：毫秒。 |
| FirstConsumeTime | String | 消息第一次消费的时间戳，单位： 毫秒。 |
| NextConsumeTime | String | 该消息再次被消费到（即重试）的绝对时间戳，单位：毫秒。 说明 HTTP协议下云消息队列 RocketMQ 版的消息重试机制为：无序消息每隔5分钟重试一次，顺序消息每隔1分钟重试一次，最多重试288次。 |
| ConsumedTimes | String | 消息被消费的次数。 |
| MessageTag | String | 消息Tag。 |
| Properties | String | 消息属性。 |

属性（Properties）的序列化，其中特殊用途的键值说明如下：

```
格式： key1:value1|key2:value2|key3:value3
```

键值说明如下：

| 参数 | 类型 | 说明 |
|---|---|---|
| KEYS | String | 消息的Key。 |
| STARTDELIVERTIME __ | Long | 表示定时消息的定时绝对时间，UNIX毫秒时间戳。 |
| TransCheckT __ | Long | 表示第一次事务消息的回查时间，相对时间，单位：秒，取值范围：10～300。 |

无消息可消费响应行

```
 HTTP/1.1 404
```

消息队列响应内容响应内容的参数说明如下。

| 参数 | 类型 | 说明 |
|---|---|---|
| Code | String | 错误代码，其中 MessageNotExist 表示没有消息可以消费，是正常的响应。 |
| Message | String | 错误内容。 |
| RequestId | String | 请求ID。 |
| HostId | String | 请求Host。 |

**响应示例**

有消息可消费

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

无消息可消费消息队列

```xml
<?xml version="1.0" ?> <Error xmlns="http://mq.aliyuncs.com/doc/v1">
  <Code>MessageNotExist</Code>
  <Message>Message not exist.</Message>
  <RequestId>5DAEE3FF463541AD6E0322EB</RequestId>
  <HostId>http://123.mqrest.cn-hangzhou.aliyuncs.com</HostId>
</Error>
```

##### 确认消息API

**请求构造**

请求行

```
 DELETE /topics/TopicName/messages?ns=INSTANCE_ID&consumer=GID HTTP/1.1
```

参数说明如下。

| 参数 | 是否必选 | 说明 |
|---|---|---|
| TopicName | 是 | 将消息发送至的Topic名称。 |
| ns | 否 | 实例ID，针对有命名空间的新建实例，该参数为必填。是否有命名空间可以在控制台实例详情页面查看。实例根据其是否有命名空间分为默认实例和新建实例： 默认实例：无命名空间，所有资源命名必需保证全局唯一。 新建实例：有命名空间，资源命名只需保证在该实例内唯一。 实例命名空间更多信息，请参见资源隔离优化（实例化支持）。 |
| consumer | 是 | 消费者群组标识，即Group ID。 |

请求内容（XML格式） 请求内容的参数说明如下。

| 参数 | 是否必选 | 说明 |
|---|---|---|
| ReceiptHandle | 是 | 通过订阅消息API获取到的消息句柄，用于确认消息是否消费成功； 句柄用且仅能使用一次，对于同一条消息如果存在重试每次拿到的句柄不同，消息句柄应在NextConsumeTime之前使用。 |

**响应构造**

请求成功响应行

```
 HTTP/1.1 204
```

消息队列响应内容无请求失败响应行

```
 HTTP/1.1 404
```

响应内容参见示例

**示例**

请求示例

```xml
<?xml version="1.0" encoding="UTF-8"?> <ReceiptHandles xmlns="http://mq.aliyuncs.com/doc/v1/"> <ReceiptHandle>1E057D5E6EAD42A57993704EC383****-MTI5NT****</ReceiptHandle> <ReceiptHandle>1E057D5E6EAD42A57993704EC383****-MTI5NT****</ReceiptHandle> <ReceiptHandle>1E057D5E6EAD42A57993704EC383****-MTI5NT****</ReceiptHandle> </ReceiptHandles>
```

响应示例请求的内容中没有句柄。

```xml
    <?xml version="1.0" ?>
    <Error xmlns="http://mq.aliyuncs.com/doc/v1">
<Code>MissingReceiptHandle</Code> <Message>ReceiptHandle is required.</Message> <RequestId>5DAEF2B9463541AD6E04490F</RequestId> <HostId>http://123.mqrest.cn-hangzhou.aliyuncs.com</HostId>
    </Error>
```

请求的句柄错误，错误的句柄是： `adfadfadf` 。

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

请求的句柄过期，即使用句柄确认消息的时候超过了消息的**NextConsumeTime**时间。

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

消息队列

#### Java SDK

##### 准备环境

**环境要求**

安装JDK 1.6或以上版本。更多信息，请参见安装JDK。 安装Maven。更多信息，请参见安装Maven。 通过Maven方式引入依赖，在pom.xml中添加以下依赖。

```xml
<dependency>
    <groupId>com.aliyun.mq</groupId>
    <artifactId>mq-http-sdk</artifactId>
    <version>X.X.X</version>
    <classifier>jar-with-dependencies</classifier>
</dependency>
```

**说明**

##### 收发普通消息

普通消息是指RocketMQ中无特性的消息，区别于有特性的定时和延时消息、顺序消息和事务消息。本文提

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送普通消息**

发送普通消息的示例代码如下。

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQProducer; import com.aliyun.mq.http.model.TopicMessage; import java.util.Date; public class Producer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
                "${HTTP_ENDPOINT}",
```

`//``AccessKey``ID`，阿里云身份验证，在`Apsara``Uni-manager`运营控制台获取。 消息队列

|  | // AccessKey ID，阿里云身份验证，在Apsara Uni-manager运营控制台获取。 "${ACCESS KEY}", _ // AccessKey Secret，阿里云身份验证，在Apsara Uni-manager运营控制台获取。 "${SECRET KEY}" _ ); // 消息所属的Topic，在RocketMQ控制台创建。 // 不同消息类型的Topic不能混用，例如普通消息的Topic只能用于收发普通消息，不能用于收发其他类型的消息。 final String topic = "${TOPIC}"; // Topic所属的实例ID，在RocketMQ控制台创建。 // 若实例有命名空间，则实例ID必须传入；若实例无命名空间，则实例ID传入null空值或字符串空值。实例的命名空间可以在RocketMQ控制台的实例详情页面查看。 final String instanceId = "${INSTANCE ID}"; _ // 获取Topic的生产者。 MQProducer producer; if (instanceId != null && instanceId != "") { producer = mqClient.getProducer(instanceId, topic); } else { producer = mqClient.getProducer(topic); } try { // 循环发送4条消息。 for (int i = 0; i < 4; i++) { TopicMessage pubMsg; // 普通消息。 pubMsg = new TopicMessage( // 消息内容。 "hello mq!".getBytes(), // 消息标签。 "A" ); // 设置消息的自定义属性。 pubMsg.getProperties().put("a", String.valueOf(i)); // 设置消息的Key。 pubMsg.setMessageKey("MessageKey"); // 同步发送消息，只要不抛异常就是成功。 TopicMessage pubResultMsg = producer.publishMessage(pubMsg); // 同步发送消息，只要不抛异常就是成功。 System.out.println(new Date() + " Send mq message success. Topic is:" + topic + ", msgId is: " + pubResultMsg.getMessageId() + ", bodyMD5 is: " + pubResultMsg.getMessageBodyMD5()); } } catch (Throwable e) { // 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理。 System.out.println(new Date() + " Send mq message failed. Topic is:" + topic); e.printStackTrace(); } mqClient.close(); } } |  |
|---|---|---|

消息队列

```
}
```

**订阅普通消息**

订阅普通消息的示例代码如下。

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQConsumer; import com.aliyun.mq.http.common.AckMessageException; import com.aliyun.mq.http.model.Message; import java.util.ArrayList; import java.util.List; public class Consumer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
                "${HTTP_ENDPOINT}",
```

`// AccessKey ID`，阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${ACCESS_KEY}",
```

`// AccessKey Secret`，阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${SECRET_KEY}"
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。 `//` 不同消息类型的`Topic`不能混用，例如普通消息的`Topic`只能用于收发普通消息，不能用于收发其他类型的消息。

```
        final String topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
        final String groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        final String instanceId = "${INSTANCE_ID}";
        final MQConsumer consumer;
        if (instanceId != null && instanceId != "") {
            consumer = mqClient.getConsumer(instanceId, topic, groupId, null);
        } else {
            consumer = mqClient.getConsumer(topic, groupId);
        }
```

`//` 在当前线程循环消费消息，建议多开个几个线程并发消费消息。

```
        do {
            List<Message> messages = null;
            try {
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息,则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回客户端。

```
                messages = consumer.consumeMessage(
```

`3,//` 一次最多消费3条消息（最多可设置为`16`条）。 `3//` 长轮询时间3秒（最多可设置为`30`秒）。 消息队列

```
                );
            } catch (Throwable e) {
                e.printStackTrace();
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e1) {
                    e1.printStackTrace();
                }
            }
```

`// Topic`中没有消息可消费。

```java
            if (messages == null || messages.isEmpty()) {
                System.out.println(Thread.currentThread().getName() + ": no new message,
continue!");
                continue;
            }
```

`//` 处理业务逻辑。

```java
            for (Message message : messages) {
                System.out.println("Receive message: " + message);
            }
```

`//` 消息重试时间到达前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费的时间戳都不一样。

```
            {
                List<String> handles = new ArrayList<String>();
                for (Message message : messages) {
                    handles.add(message.getReceiptHandle());
                }
                try {
                    consumer.ackMessage(handles);
                } catch (Throwable e) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```java
                    if (e instanceof AckMessageException) {
                        AckMessageException errors = (AckMessageException) e;
                        System.out.println("Ack message fail, requestId is:" +
errors.getRequestId() + ", fail handles:");
                        if (errors.getErrorMessages() != null) {
                            for (String errorHandle :errors.getErrorMessages().keySet())
{
                                System.out.println("Handle:" + errorHandle + ",
ErrorCode:" + errors.getErrorMessages().get(errorHandle).getErrorCode()
                                        + ", ErrorMsg:" +
errors.getErrorMessages().get(errorHandle).getErrorMessage());
                            }
                        }
                        continue;
                    }
                    e.printStackTrace();
                }
            }
        } while (true);
    }
}
```

消息队列

##### 收发顺序消息

顺序消息（FIFO消息）是RocketMQ提供的一种严格按照顺序来发布和消费的消息类型。本文提供使用

**背景信息**

顺序消息是RocketMQ提供的一种对消息发送和消费顺序有严格要求的消息。对于一个指定的Topic，消息严格按照先进先出（FIFO）的原则进行消息发布和消费，即先发布的消息先消费，后发布的消息后消费。 RocketMQ的顺序消息中，对于指定的一个Topic，所有消息根据Sharding Key进行区块分区，同一个分区内的消息按照严格的先进先出（FIFO）原则进行发布和消费。同一分区内的消息保证顺序，不同分区之间的消息顺序不做要求。因此RocketMQ的顺序消息也叫分区顺序消息。 更多信息，请参见顺序消息。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送顺序消息**

发送顺序消息的示例代码如下。

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQProducer; import com.aliyun.mq.http.model.TopicMessage; import java.util.Date; public class OrderProducer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
                "${HTTP_ENDPOINT}",
```

`// AccessKey ID`，阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${ACCESS_KEY}",
```

`// AccessKey Secret`，阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${SECRET_KEY}"
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。 `//` 不同消息类型的`Topic`不能混用，例如普通消息的`Topic`只能用于收发普通消息，不能用于收发其他类型的消息。

```
        final String topic = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        final String instanceId = "${INSTANCE_ID}";
```

`//`获取T i的生产者消息队列 `//` 获取`Topic`的生产者。

```
        MQProducer producer;
        if (instanceId != null && instanceId != "") {
            producer = mqClient.getProducer(instanceId, topic);
        } else {
            producer = mqClient.getProducer(topic);
        }
        try {
```

`//` 循环发送8条消息。

```
            for (int i = 0; i < 8; i++) {
                TopicMessage pubMsg = new TopicMessage(
```

`//` 消息内容。

```
                        "hello mq!".getBytes(),
```

`//` 消息标签。

```
                        "A"
                );
```

`//` 设置分区顺序消息的`Sharding Key`，用于标识不同的分区。`Sharding Key`与消息的`Key`是完全不同的概念。

```
                pubMsg.setShardingKey(String.valueOf(i % 2));
                pubMsg.getProperties().put("a", String.valueOf(i));
```

`//` 同步发送消息，只要不抛异常就是成功。

```
                TopicMessage pubResultMsg = producer.publishMessage(pubMsg);
```

`//` 同步发送消息，只要不抛异常就是成功。

```java
                System.out.println(new Date() + " Send mq message success. Topic is:" +
topic + ", msgId is: " + pubResultMsg.getMessageId()
                        + ", bodyMD5 is: " + pubResultMsg.getMessageBodyMD5());
            }
        } catch (Throwable e) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理。

```java
            System.out.println(new Date() + " Send mq message failed. Topic is:" +
topic);
            e.printStackTrace();
        }
        mqClient.close();
    }
}
```

**订阅顺序消息**

订阅顺序消息的示例代码如下。

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQConsumer; import com.aliyun.mq.http.common.AckMessageException; import com.aliyun.mq.http.model.Message; import java.util.ArrayList; import java.util.List; public class OrderConsumer {
```

消息队列

```
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
                "${HTTP_ENDPOINT}",
```

`// AccessKey ID`，阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${ACCESS_KEY}",
```

`// AccessKey Secret`，阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${SECRET_KEY}"
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。 `//`不同消息类型的`Topic`不能混用，例如普通消息的`Topic`只能用于收发普通消息，不能用于收发其他类型的消息。

```
        final String topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
        final String groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        final String instanceId = "${INSTANCE_ID}";
        final MQConsumer consumer;
        if (instanceId != null && instanceId != "") {
            consumer = mqClient.getConsumer(instanceId, topic, groupId, null);
        } else {
            consumer = mqClient.getConsumer(topic, groupId);
        }
```

`//` 在当前线程循环消费消息，建议多开个几个线程并发消费消息。

```
        do {
            List<Message> messages = null;
            try {
```

`//` 长轮询顺序消费消息, 拉取到的消息可能是多个分区的（对于分区顺序消息），一个分区内的消息一定是顺序的。 `//` 对于分区顺序消息，只要一个分区内存在没有被确认消费的消息，那么该分区下次还会消费到相同的消息。 `//` 对于一个分区，只有所有消息确认消费成功才能消费下一批消息。 `//` 长轮询表示如果`Topic`没有消息，则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则服务端立即返回响应。

```
                messages = consumer.consumeMessageOrderly(
```

`3, //` 一次最多消费3条消息（最多可设置为`16`条）。 `3 //` 长轮询时间为3秒（最多可设置为`30`秒）。

```
                );
            } catch (Throwable e) {
                e.printStackTrace();
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e1) {
                    e1.printStackTrace();
                }
            }
```

`// Topic`中没有消息可消费。

```
            if (messages == null || messages.isEmpty()) {
```

消息队列

```
(
```

g
||
g

```java
py()){
                System.out.println(Thread.currentThread().getName() + ": no new message,
continue!");
                continue;
            }
```

`//` 处理业务逻辑。

```java
            System.out.println("Receive " + messages.size() + " messages:");
            for (Message message : messages) {
                System.out.println(message);
                System.out.println("ShardingKey: " + message.getShardingKey() + ", a:"
+ message.getProperties().get("a"));
            }
```

`//` 消息重试时间到达前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
            {
                List<String> handles = new ArrayList<String>();
                for (Message message : messages) {
                    handles.add(message.getReceiptHandle());
                }
                try {
                    consumer.ackMessage(handles);
                } catch (Throwable e) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```java
                    if (e instanceof AckMessageException) {
                        AckMessageException errors = (AckMessageException) e;
                        System.out.println("Ack message fail, requestId is:" +
errors.getRequestId() + ", fail handles:");
                        if (errors.getErrorMessages() != null) {
                            for (String errorHandle :errors.getErrorMessages().keySet())
{
                                System.out.println("Handle:" + errorHandle + ",
ErrorCode:" + errors.getErrorMessages().get(errorHandle).getErrorCode()
                                        + ", ErrorMsg:" +
errors.getErrorMessages().get(errorHandle).getErrorMessage());
                            }
                        }
                        continue;
                    }
                    e.printStackTrace();
                }
            }
        } while (true);
    }
}
```

##### 收发定时消息和延时消息

**背景信息**

消息队列延时消息：Producer将消息发送到RocketMQRocketMQ服务端，但并不期望立马投递这条消息，而是延迟一定时间后才投递到Consumer进行消费，该消息即延时消息。 定时消息：Producer将消息发送到RocketMQ服务端，但并不期望立马投递这条消息，而是推迟到在当前时间点之后的某一个时间投递到Consumer进行消费，该消息即定时消息。 在HTTP协议下，定时消息和延时消息的代码配置相同，本质都是根据消息中的属性延迟固定时间后才投递给消费者。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送定时消息或延时消息**

发送定时消息或延时消息的示例代码如下。

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQProducer; import com.aliyun.mq.http.model.TopicMessage; import java.util.Date; public class Producer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
                "${HTTP_ENDPOINT}",
```

`// AccessKey ID`，阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${ACCESS_KEY}",
```

`// AccessKey Secret`，阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${SECRET_KEY}"
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。 `//`不同消息类型的`Topic`不能混用，例如普通消息的`Topic`只能用于收发普通消息，不能用于收发其他类型的消息。

```
        final String topic = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        final String instanceId = "${INSTANCE_ID}";
```

`//` 获取`Topic`的生产者。

```
        MQProducer producer;
        if (instanceId != null && instanceId != "") {
            producer = mqClient.getProducer(instanceId, topic);
        } else {
            producer = mqClient.getProducer(topic);
        }
        try {
```

消息队列

```
y{
```

`//` 循环发送4条消息。

```
            for (int i = 0; i < 4; i++) {
                TopicMessage pubMsg;
                pubMsg = new TopicMessage(
```

`//` 消息内容。

```
                "hello mq!".getBytes(),
```

`//` 消息标签。

```
                "A"
                 );
```

`//` 设置消息的自定义属性。

```
                 pubMsg.getProperties().put("a", String.valueOf(i));
```

`//` 设置消息的`Key`。

```
                 pubMsg.setMessageKey("MessageKey");
```

`//` 延时消息，发送时间为`10s`后。该参数格式为毫秒级别的时间戳。 `//` 若发送定时消息，设置该参数时需要计算定时时间与当前时间的时间差。

```
                 pubMsg.setStartDeliverTime(System.currentTimeMillis() + 10 * 1000);
```

`//` 同步发送消息，只要不抛异常就是成功。

```
             TopicMessage pubResultMsg = producer.publishMessage(pubMsg);
```

`//` 同步发送消息，只要不抛异常就是成功。

```java
             System.out.println(new Date() + " Send mq message success. Topic is:" +
topic + ", msgId is: " + pubResultMsg.getMessageId()
                        + ", bodyMD5 is: " + pubResultMsg.getMessageBodyMD5());
            }
        } catch (Throwable e) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理。

```java
            System.out.println(new Date() + " Send mq message failed. Topic is:" +
topic);
            e.printStackTrace();
        }
        mqClient.close();
    }
}
```

**订阅定时消息或延时消息**

订阅定时消息或延时消息的示例代码如下。

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQConsumer; import com.aliyun.mq.http.common.AckMessageException; import com.aliyun.mq.http.model.Message; import java.util.ArrayList; import java.util.List; public class Consumer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
```

消息队列 `//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
                "${HTTP_ENDPOINT}",
```

`// AccessKey ID`，阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${ACCESS_KEY}",
```

`// AccessKey Secret`，阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${SECRET_KEY}"
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。 `//` 不同消息类型的`Topic`不能混用，例如普通消息的`Topic`只能用于收发普通消息，不能用于收发其他类型的消息。

```
        final String topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
        final String groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        final String instanceId = "${INSTANCE_ID}";
        final MQConsumer consumer;
        if (instanceId != null && instanceId != "") {
            consumer = mqClient.getConsumer(instanceId, topic, groupId, null);
        } else {
            consumer = mqClient.getConsumer(topic, groupId);
        }
```

`//` 在当前线程循环消费消息，建议多开个几个线程并发消费消息。

```
        do {
            List<Message> messages = null;
            try {
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息,则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回客户端。

```
                messages = consumer.consumeMessage(
```

`3,//` 一次最多消费3条消息（最多可设置为`16`条）。 `3//` 长轮询时间3秒（最多可设置为`30`秒）。

```
                );
            } catch (Throwable e) {
                e.printStackTrace();
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e1) {
                    e1.printStackTrace();
                }
            }
```

`// Topic`中没有消息可消费。

```java
            if (messages == null || messages.isEmpty()) {
                System.out.println(Thread.currentThread().getName() + ": no new message,
continue!");
                continue;
            }
```

`//` 处理业务逻辑。 消息队列

```java
            for (Message message : messages) {
                System.out.println("Receive message: " + message);
            }
```

`//` 消息重试时间到达前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费的时间戳都不一样。

```
            {
                List<String> handles = new ArrayList<String>();
                for (Message message : messages) {
                    handles.add(message.getReceiptHandle());
                }
                try {
                    consumer.ackMessage(handles);
                } catch (Throwable e) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```java
                    if (e instanceof AckMessageException) {
                        AckMessageException errors = (AckMessageException) e;
                        System.out.println("Ack message fail, requestId is:" +
errors.getRequestId() + ", fail handles:");
                        if (errors.getErrorMessages() != null) {
                            for (String errorHandle :errors.getErrorMessages().keySet())
{
                                System.out.println("Handle:" + errorHandle + ",
ErrorCode:" + errors.getErrorMessages().get(errorHandle).getErrorCode()
                                        + ", ErrorMsg:" +
errors.getErrorMessages().get(errorHandle).getErrorMessage());
                            }
                        }
                        continue;
                    }
                    e.printStackTrace();
                }
            }
        } while (true);
    }
}
```

##### 收发事务消息

RocketMQ提供类似XA或Open XA的分布式事务功能，通过RocketMQ事务消息，能达到分布式事务的最

**背景信息**

事务消息的交互流程如下图所示。 消息队列更多信息，请参见事务消息。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送事务消息**

发送事务消息的示例代码如下。

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
                            + ", ErrorMsg:" +
errors.getErrorMessages().get(errorHandle).getErrorMessage());
                }
            }
        }
    }
    public static void main(String[] args) throws Throwable {
        MQClient mqClient = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
                "${HTTP_ENDPOINT}",
```

消息队列 `// AccessKey ID`，阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${ACCESS_KEY}",
```

`// AccessKey Secret`，阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${SECRET_KEY}"
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。 `//` 不同消息类型的`Topic`不能混用，例如普通消息的`Topic`只能用于收发普通消息，不能用于收发其他类型的消息。

```
        final String topic = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        final String instanceId = "${INSTANCE_ID}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
        final String groupId = "${GROUP_ID}";
        final MQTransProducer mqTransProducer = mqClient.getTransProducer(instanceId, t
opic, groupId);
        for (int i = 0; i < 4; i++) {
            TopicMessage topicMessage = new TopicMessage();
            topicMessage.setMessageBody("trans_msg");
            topicMessage.setMessageTag("a");
            topicMessage.setMessageKey(String.valueOf(System.currentTimeMillis()));
```

`//` 设置事务第一次回查的时间，为相对时间。单位：秒，取值范围：10~300。 `//` 第一次事务回查后如果消息没有提交或者回滚，则之后每隔`10s`左右会回查一次，共回查`24`小时。

```java
            topicMessage.setTransCheckImmunityTime(10);
            topicMessage.getProperties().put("a", String.valueOf(i));
            TopicMessage pubResultMsg = null;
            pubResultMsg = mqTransProducer.publishMessage(topicMessage);
            System.out.println("Send---->msgId is: " + pubResultMsg.getMessageId()
                    + ", bodyMD5 is: " + pubResultMsg.getMessageBodyMD5()
                    + ", Handle: " + pubResultMsg.getReceiptHandle()
            );
            if (pubResultMsg != null && pubResultMsg.getReceiptHandle() != null) {
                if (i == 0) {
```

`//` 发送完事务消息后能获取到半消息句柄，可以直接提交或回滚事务消息。

```java
                    try {
                        mqTransProducer.commit(pubResultMsg.getReceiptHandle());
                        System.out.println(String.format("MessageId:%s, commit", pubResu
ltMsg.getMessageId()));
                    } catch (Throwable e) {
```

`//` 如果提交或回滚事务消息时超过了`TransCheckImmunityTime`（针对发送事务消息的句柄）设置的时长，则会失败。

```
                        if (e instanceof AckMessageException) {
                            processCommitRollError(e);
                            continue;
                        }
                    }
                }
            }
        }
```

消息队列 `//` 客户端需要有一个线程或者进程来消费没有确认的事务消息。 `//` 启动一个线程来检查没有确认的事务消息。

```java
        Thread t = new Thread(new Runnable() {
            public void run() {
                int count = 0;
                while(true) {
                    try {
                        if (count == 3) {
                            break;
                        }
                        List<Message> messages = mqTransProducer.consumeHalfMessage(3, 3
);
                        if (messages == null) {
                            System.out.println("No Half message!");
                            continue;
                        }
                        System.out.println(String.format("Half----
>MessageId:%s,Properties:%s,Body:%s,Latency:%d",
                                messages.get(0).getMessageId(),
                                messages.get(0).getProperties(),
                                messages.get(0).getMessageBodyString(),
                                System.currentTimeMillis() -
messages.get(0).getPublishTime()));
                        for (Message message : messages) {
                            try {
                                if (Integer.valueOf(message.getProperties().get("a")) ==
1) {
```

`//` 确认提交事务消息。

```java
                                    mqTransProducer.commit(message.getReceiptHandle());
                                    count++;
                                    System.out.println(String.format("MessageId:%s, commi
t", message.getMessageId()));
                                } else if
(Integer.valueOf(message.getProperties().get("a")) == 2
                                        && message.getConsumedTimes() > 1) {
```

`//` 确认提交事务消息。

```java
                                    mqTransProducer.commit(message.getReceiptHandle());
                                    count++;
                                    System.out.println(String.format("MessageId:%s, commi
t", message.getMessageId()));
                                } else if
(Integer.valueOf(message.getProperties().get("a")) == 3) {
```

`//` 确认回滚事务消息。

```java
                                    mqTransProducer.rollback(message.getReceiptHandle());
                                    count++;
                                    System.out.println(String.format("MessageId:%s, rollb
ack", message.getMessageId()));
                                } else {
```

`//` 什么都不做，下次再检查。

```java
                                    System.out.println(String.format("MessageId:%s, unkno
wn", message.getMessageId()));
                                }
}catch(Throwablee){
```

消息队列

```
                            } catch (Throwable e) {
```

`//` 如果提交或回滚消息时超过了`TransCheckImmunityTime`（针对发送事务消息的句柄）或者超过`10s`（针对`consumeHalfMessage`的句柄）则会失败。

```java
                                processCommitRollError(e);
                            }
                        }
                    } catch (Throwable e) {
                        System.out.println(e.getMessage());
                    }
                }
            }
        });
        t.start();
        t.join();
        mqClient.close();
    }
}
```

**订阅事务消息**

订阅事务消息的示例代码如下。

```java
import com.aliyun.mq.http.MQClient; import com.aliyun.mq.http.MQConsumer; import com.aliyun.mq.http.common.AckMessageException; import com.aliyun.mq.http.model.Message; import java.util.ArrayList; import java.util.List; public class Consumer {
    public static void main(String[] args) {
        MQClient mqClient = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
                "${HTTP_ENDPOINT}",
```

`// AccessKey ID`，阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${ACCESS_KEY}",
```

`// AccessKey Secret`，阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${SECRET_KEY}"
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。 `//` 不同消息类型的`Topic`不能混用，例如普通消息的`Topic`只能用于收发普通消息，不能用于收发其他类型的消息。

```
        final String topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
        final String groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。 消息队列例的命名空间可以在`RocketMQ`控制台的实例详情页面查看

```
        final String instanceId = "${INSTANCE_ID}";
        final MQConsumer consumer;
        if (instanceId != null && instanceId != "") {
            consumer = mqClient.getConsumer(instanceId, topic, groupId, null);
        } else {
            consumer = mqClient.getConsumer(topic, groupId);
        }
```

`//` 在当前线程循环消费消息，建议多开个几个线程并发消费消息。

```
        do {
            List<Message> messages = null;
            try {
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息,则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回客户端。

```
                messages = consumer.consumeMessage(
```

`3,//` 一次最多消费3条消息（最多可设置为`16`条）。 `3//` 长轮询时间3秒（最多可设置为`30`秒）。

```
                );
            } catch (Throwable e) {
                e.printStackTrace();
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e1) {
                    e1.printStackTrace();
                }
            }
```

`// Topic`中没有消息可消费。

```java
            if (messages == null || messages.isEmpty()) {
                System.out.println(Thread.currentThread().getName() + ": no new message,
continue!");
                continue;
            }
```

`//` 处理业务逻辑。

```java
            for (Message message : messages) {
                System.out.println("Receive message: " + message);
            }
```

`//` 消息重试时间到达前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费的时间戳都不一样。

```
            {
                List<String> handles = new ArrayList<String>();
                for (Message message : messages) {
                    handles.add(message.getReceiptHandle());
                }
                try {
                    consumer.ackMessage(handles);
                } catch (Throwable e) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
                    if (e instanceof AckMessageException) {
```

消息队列

```java
                        AckMessageException errors = (AckMessageException) e;
                        System.out.println("Ack message fail, requestId is:" +
errors.getRequestId() + ", fail handles:");
                        if (errors.getErrorMessages() != null) {
                            for (String errorHandle :errors.getErrorMessages().keySet())
{
                                System.out.println("Handle:" + errorHandle + ",
ErrorCode:" + errors.getErrorMessages().get(errorHandle).getErrorCode()
                                        + ", ErrorMsg:" +
errors.getErrorMessages().get(errorHandle).getErrorMessage());
                            }
                        }
                        continue;
                    }
                    e.printStackTrace();
                }
            }
        } while (true);
    }
}
```

#### Go SDK

##### 准备环境

**环境要求**

安装Go。更多信息，请参见安装Go。 安装完成后，您可以执行 `go version` 命令查看Go语言版本。
1. 执行以下命令启用Go Modules。Go Modules更多信息，请参见Go Modules Reference。

```
go env -w GO111MODULE=on
```

2. 执行以下命令设置Go Modules代理。

```
go env -w GOPROXY=https://goproxy.cn,direct
```

3. 执行以下命令进行初始化，生成go.mod文件。

```
go mod init
```

4. 执行以下命令安装Go SDK。

##### 收发普通消息

普通消息是指RocketMQ中无特性的消息，区别于有特性的定时和延时消息、顺序消息和事务消息。本文提消息队列

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送普通消息**

发送普通消息的示例代码如下。 消息队列

```java
package main import (
    "fmt"
    "time"
    "strconv"
```

)

```
func main() {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
    endpoint := "${HTTP_ENDPOINT}"
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    accessKey := "${ACCESS_KEY}"
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    secretKey := "${SECRET_KEY}"
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
    topic := "${TOPIC}"
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    instanceId := "${INSTANCE_ID}"
    client := mq_http_sdk.NewAliyunMQClient(endpoint, accessKey, secretKey, "")
    mqProducer := client.GetProducer(instanceId, topic)
```

`//` 循环发送4条消息。

```
    for i := 0; i < 4; i++ {
        var msg mq_http_sdk.PublishMessageRequest
        msg = mq_http_sdk.PublishMessageRequest{
        MessageBody: "hello mq!",         //消息内容。
        MessageTag:  "",                  // 消息标签。
        Properties:  map[string]string{}, // 消息属性。
        }
```

`//` 设置消息的`Key`。

```
        msg.MessageKey = "MessageKey"
```

`//` 设置消息自定义属性。

```
        msg.Properties["a"] = strconv.Itoa(i)
        ret, err := mqProducer.PublishMessage(msg)
        if err != nil {
            fmt.Println(err)
            return
        } else {
            fmt.Printf("Publish ---->\n\tMessageId:%s, BodyMD5:%s, \n", ret.MessageId,
ret.MessageBodyMD5)
        }
        time.Sleep(time.Duration(100) * time.Millisecond)
    }
}
```

消息队列

**订阅普通消息**

订阅普通消息的示例代码如下。

```java
package main import (
    "fmt"
    "github.com/gogap/errors"
    "strings"
    "time"
```

)

```
func main() {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
    endpoint := "${HTTP_ENDPOINT}"
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    accessKey := "${ACCESS_KEY}"
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    secretKey := "${SECRET_KEY}"
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。 `//`不同消息类型的`Topic`不能混用，例如普通消息的`Topic`只能用于收发普通消息，不能用于收发其他类型的消息。

```
    topic := "${TOPIC}"
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    instanceId := "${INSTANCE_ID}"
```

`//` 您在控制台创建的`Group ID`。

```
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
                {
```

`//` 处理业务逻辑。

```
                    var handles []string
                    fmt.Printf("Consume %d messages---->\n", len(resp.Messages))
                    for _, v := range resp.Messages {
                        handles = append(handles, v.ReceiptHandle)
                        fmt.Printf("\tMessageID: %s, PublishTime: %d, MessageTag: %s\n"+
                            "\tConsumedTimes: %d, FirstConsumeTime: %d, NextConsumeTime:
%d\n"+
                            "\tBody: %s\n"+
                            "\tProps: %s\n",
```

消息队列 p ,

```
                            v.MessageId, v.PublishTime, v.MessageTag, v.ConsumedTimes,
                            v.FirstConsumeTime, v.NextConsumeTime, v.MessageBody,
v.Properties)
                    }
```

`// NextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
                    ackerr := mqConsumer.AckMessage(handles)
                    if ackerr != nil {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```json
                        fmt.Println(ackerr)
                        if errAckItems, ok := ackerr.(errors.ErrCode).Context()
["Detail"].([]mq_http_sdk.ErrAckItem); ok {
                           for _, errAckItem := range errAckItems {
                             fmt.Printf("\tErrorHandle:%s, ErrorCode:%s, ErrorMsg:%s\n",
                               errAckItem.ErrorHandle, errAckItem.ErrorCode,
errAckItem.ErrorMsg)
                           }
                        } else {
                           fmt.Println("ack err =", ackerr)
                        }
                        time.Sleep(time.Duration(3) * time.Second)
                    } else {
                        fmt.Printf("Ack ---->\n\t%s\n", handles)
                    }
                    endChan <- 1
                }
            case err := <-errChan:
                {
```

`// Topic`中没有消息可消费。

```
                    if strings.Contains(err.(errors.ErrCode).Error(), "MessageNotExist")
{
                        fmt.Println("\nNo new message, continue!")
                    } else {
                        fmt.Println(err)
                        time.Sleep(time.Duration(3) * time.Second)
                    }
                    endChan <- 1
                }
            case <-time.After(35 * time.Second):
                {
                    fmt.Println("Timeout of consumer message ??")
                    endChan <- 1
                }
            }
        }()
```

`//` 长轮询消费消息，网络超时时间默认为`35s`。 `//` 长轮询表示如果`Topic`没有消息，则客户端请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回响应。

```
        mqConsumer.ConsumeMessage(respChan, errChan,
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3, //` 长轮询时间`3s`（最多可设置为`30s`）。 消息队列 )

```
        <-endChan
    }
}
```

##### 收发顺序消息

顺序消息（FIFO消息）是RocketMQ提供的一种严格按照顺序来发布和消费的消息类型。本文提供使用

**背景信息**

顺序消息是RocketMQ提供的一种对消息发送和消费顺序有严格要求的消息。对于一个指定的Topic，消息严格按照先进先出（FIFO）的原则进行消息发布和消费，即先发布的消息先消费，后发布的消息后消费。 RocketMQ的顺序消息中，对于指定的一个Topic，所有消息根据Sharding Key进行区块分区，同一个分区内的消息按照严格的先进先出（FIFO）原则进行发布和消费。同一分区内的消息保证顺序，不同分区之间的消息顺序不做要求。因此RocketMQ的顺序消息也叫分区顺序消息。 更多信息，请参见顺序消息。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送顺序消息**

发送顺序消息的示例代码如下。

```java
package main import (
    "fmt"
    "time"
    "strconv"
```

)

```
func main() {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
    endpoint := "${HTTP_ENDPOINT}"
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    accessKey := "${ACCESS_KEY}"
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    secretKey := "${SECRET_KEY}"
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
    topic := "${TOPIC}"
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    instanceId := "${INSTANCE_ID}"
```

消息队列

```
    client := mq_http_sdk.NewAliyunMQClient(endpoint, accessKey, secretKey, "")
    mqProducer := client.GetProducer(instanceId, topic)
```

`//` 循环发送8条消息。

```
    for i := 0; i < 8; i++ {
        msg := mq_http_sdk.PublishMessageRequest{
            MessageBody: "hello mq!",         //消息内容。
            MessageTag:  "",                  // 消息标签。
            Properties:  map[string]string{}, // 消息属性。
        }
```

`//` 设置消息的`Key`。

```
        msg.MessageKey = "MessageKey"
```

`//` 设置消息的自定义属性。

```
        msg.Properties["a"] = strconv.Itoa(i)
```

`//` 设置分区顺序消息的`Sharding Key`，用于标识不同的分区。`Sharding Key`与消息的`Key`是完全不同的概念。

```
        msg.ShardingKey = strconv.Itoa(i % 2)
        ret, err := mqProducer.PublishMessage(msg)
        if err != nil {
            fmt.Println(err)
            return
        } else {
            fmt.Printf("Publish ---->\n\tMessageId:%s, BodyMD5:%s, \n", ret.MessageId,
ret.MessageBodyMD5)
        }
        time.Sleep(time.Duration(100) * time.Millisecond)
    }
}
```

**订阅顺序消息**

订阅顺序消息的示例代码如下。

```java
package main import (
    "fmt"
    "github.com/gogap/errors"
    "strings"
    "time"
```

)

```
func main() {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
    endpoint := "${HTTP_ENDPOINT}"
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    accessKey := "${ACCESS_KEY}"
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    secretKey := "${SECRET_KEY}"
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
topic:="${TOPIC}"
```

消息队列

```
    topic := "${TOPIC}"
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    instanceId := "${INSTANCE_ID}"
```

`//` 您在控制台创建的`Group ID`。

```
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
                {
```

`//` 处理业务逻辑。

```
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
                    }
```

`// NextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
                    ackerr := mqConsumer.AckMessage(handles)
                    if ackerr != nil {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```json
                        fmt.Println(ackerr)
                        if errAckItems, ok := ackerr.(errors.ErrCode).Context()
["Detail"].([]mq_http_sdk.ErrAckItem); ok {
                           for _, errAckItem := range errAckItems {
                              fmt.Printf("\tErrorHandle:%s, ErrorCode:%s,
ErrorMsg:%s\n",
                                 errAckItem.ErrorHandle, errAckItem.ErrorCode,
errAckItem.ErrorMsg)
                           }
                        } else {
                           fmt.Println("ack err =", ackerr)
                        }
                        time.Sleep(time.Duration(3) * time.Second)
}else{
```

消息队列

```
                    } else {
                        fmt.Printf("Ack ---->\n\t%s\n", handles)
                    }
                    endChan <- 1
                }
            case err := <-errChan:
                {
```

`// Topic`中没有消息可消费。

```
                    if strings.Contains(err.(errors.ErrCode).Error(), "MessageNotExist")
{
                        fmt.Println("\nNo new message, continue!")
                    } else {
                        fmt.Println(err)
                        time.Sleep(time.Duration(3) * time.Second)
                    }
                    endChan <- 1
                }
            case <-time.After(35 * time.Second):
                {
                    fmt.Println("Timeout of consumer message ??")
                    endChan <- 1
                }
            }
        }()
```

`//` 拉取到的消息可能是多个分区的（对于分区顺序消息），一个分区内的消息一定是顺序的。 `//` 对于分区顺序消息，只要一个分区内存在没有被确认消费的消息，那么该分区下次还会消费到相同的消息。 `//` 对于一个分区，只有所有消息确认消费成功才能消费下一批消息。 `//` 长轮询顺序消费消息, 网络超时时间为`35s`。 `//` 长轮询表示如果`Topic`没有消息，则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则服务端立即返回响应。

```
        mqConsumer.ConsumeMessageOrderly(respChan, errChan,
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3, //` 长轮询时间`3s`（最多可设置为`30s`）。 )

```
        <-endChan
    }
}
```

##### 收发定时消息和延时消息

**背景信息**

延时消息：Producer将消息发送到RocketMQRocketMQ服务端，但并不期望立马投递这条消息，而是延迟一定时间后才投递到Consumer进行消费，该消息即延时消息。 定时消息：Producer将消息发送到RocketMQ服务端，但并不期望立马投递这条消息，而是推迟到在当前时间点之后的某一个时间投递到Consumer进行消费，该消息即定时消息。 在HTTP协议下，定时消息和延时消息的代码配置相同，本质都是根据消息中的属性延迟固定时间后才投递给消费者。 消息队列

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送定时消息或延时消息**

发送定时消息或延时消息的示例代码如下。

```java
package main import (
    "fmt"
    "time"
    "strconv"
```

)

```
func main() {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
    endpoint := "${HTTP_ENDPOINT}"
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    accessKey := "${ACCESS_KEY}"
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    secretKey := "${SECRET_KEY}"
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
    topic := "${TOPIC}"
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    instanceId := "${INSTANCE_ID}"
    client := mq_http_sdk.NewAliyunMQClient(endpoint, accessKey, secretKey, "")
    mqProducer := client.GetProducer(instanceId, topic)
```

`//` 循环发送4条消息。

```
    for i := 0; i < 4; i++ {
        var msg mq_http_sdk.PublishMessageRequest
            msg = mq_http_sdk.PublishMessageRequest{
            MessageBody: "hello mq!",         // 消息内容。
            MessageTag:  "",                  // 消息标签。
            Properties:  map[string]string{}, // 消息属性。
            }
```

`//` 设置消息的`Key`。

```
            msg.MessageKey = "MessageKey"
```

`//` 设置消息自定义属性。

```
            msg.Properties["a"] = strconv.Itoa(i)
```

`//` 延时消息，发送时间为`10s`后。该参数格式为毫秒级别的时间戳。 `//` 若发送定时消息，设置该参数时需要计算定时时间与当前时间的时间差。

```
msgStartDelierTime timeNo()UTC()Uni()*1000+10*1000
```

消息队列

```
            msg.StartDeliverTime = time.Now().UTC().Unix() * 1000 + 10 * 1000
        ret, err := mqProducer.PublishMessage(msg)
        if err != nil {
            fmt.Println(err)
            return
        } else {
            fmt.Printf("Publish ---->\n\tMessageId:%s, BodyMD5:%s, \n", ret.MessageId,
ret.MessageBodyMD5)
        }
        time.Sleep(time.Duration(100) * time.Millisecond)
    }
}
```

**订阅定时消息或延时消息**

订阅定时消息或延时消息的示例代码如下。

```java
package main import (
    "fmt"
    "github.com/gogap/errors"
    "strings"
    "time"
```

)

```
func main() {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
    endpoint := "${HTTP_ENDPOINT}"
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    accessKey := "${ACCESS_KEY}"
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    secretKey := "${SECRET_KEY}"
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。 `//`不同消息类型的`Topic`不能混用，例如普通消息的`Topic`只能用于收发普通消息，不能用于收发其他类型的消息。

```
    topic := "${TOPIC}"
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    instanceId := "${INSTANCE_ID}"
```

`//` 您在控制台创建的`Group ID`。

```
    groupId := "${GROUP_ID}"
    client := mq_http_sdk.NewAliyunMQClient(endpoint, accessKey, secretKey, "")
    mqConsumer := client.GetConsumer(instanceId, topic, groupId, "")
    for {
        endChan := make(chan int)
respChan:=make(chanmqhttpsdkConsumeMessageResponse)
```

消息队列

```
        respChan : make(chan mq_http_sdk.ConsumeMessageResponse)
        errChan := make(chan error)
        go func() {
            select {
            case resp := <-respChan:
                {
```

`//` 处理业务逻辑。

```
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
                    }
```

`// NextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
                    ackerr := mqConsumer.AckMessage(handles)
                    if ackerr != nil {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```json
                        fmt.Println(ackerr)
                        if errAckItems, ok := ackerr.(errors.ErrCode).Context()
["Detail"].([]mq_http_sdk.ErrAckItem); ok {
                           for _, errAckItem := range errAckItems {
                             fmt.Printf("\tErrorHandle:%s, ErrorCode:%s, ErrorMsg:%s\n",
                               errAckItem.ErrorHandle, errAckItem.ErrorCode,
errAckItem.ErrorMsg)
                           }
                        } else {
                           fmt.Println("ack err =", ackerr)
                        }
                        time.Sleep(time.Duration(3) * time.Second)
                    } else {
                        fmt.Printf("Ack ---->\n\t%s\n", handles)
                    }
                    endChan <- 1
                }
            case err := <-errChan:
                {
```

`// Topic`中没有消息可消费。

```
                    if strings.Contains(err.(errors.ErrCode).Error(), "MessageNotExist")
{
                        fmt.Println("\nNo new message, continue!")
                    } else {
                        fmt.Println(err)
                        time.Sleep(time.Duration(3) * time.Second)
                    }
                    endChan <- 1
```

消息队列

```
                }
            case <-time.After(35 * time.Second):
                {
                    fmt.Println("Timeout of consumer message ??")
                    endChan <- 1
                }
            }
        }()
```

`//` 长轮询消费消息，网络超时时间默认为`35s`。 `//` 长轮询表示如果`Topic`没有消息，则客户端请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回响应。

```
        mqConsumer.ConsumeMessage(respChan, errChan,
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3, //` 长轮询时间`3s`（最多可设置为`30s`）。 )

```
        <-endChan
    }
}
```

##### 收发事务消息

RocketMQ提供类似XA或Open XA的分布式事务功能，通过RocketMQ事务消息，能达到分布式事务的最

**背景信息**

事务消息的交互流程如下图所示。 更多信息，请参见事务消息。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送事务消息**

发送事务消息的示例代码如下。

```java
package main
```

消息队列

```java
import (
    "fmt"
    "github.com/gogap/errors"
    "strconv"
    "strings"
    "time"
```

)

```
var loopCount = 0 func ProcessError(err error) {
```

`//` 如果`Commit`或`Rollback`时超过了`TransCheckImmunityTime`（针对发送事务消息的句柄）或者超过 `10s`（针对`consumeHalfMessage`的句柄），则`Commit`或`Rollback`失败。

```
    if err == nil {
        return
    }
    fmt.Println(err)
    for _, errAckItem := range err.(errors.ErrCode).Context()["Detail"].
([]mq_http_sdk.ErrAckItem) {
        fmt.Printf("\tErrorHandle:%s, ErrorCode:%s, ErrorMsg:%s\n",
            errAckItem.ErrorHandle, errAckItem.ErrorCode, errAckItem.ErrorMsg)
    }
} func ConsumeHalfMsg(mqTransProducer *mq_http_sdk.MQTransProducer) {
    for {
        if loopCount >= 10 {
            return
        }
        loopCount++
        endChan := make(chan int)
        respChan := make(chan mq_http_sdk.ConsumeMessageResponse)
        errChan := make(chan error)
        go func() {
            select {
            case resp := <-respChan:
                {
```

`//` 处理业务逻辑。

```
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
```

消息队列

```
                        var comRollErr error
                        if a == 1 {
```

`//` 确认提交事务消息。

```
                            comRollErr = (*mqTransProducer).Commit(v.ReceiptHandle)
                            fmt.Println("Commit---------->")
                        } else if a == 2 && v.ConsumedTimes > 1 {
```

`//` 确认提交事务消息。

```
                            comRollErr = (*mqTransProducer).Commit(v.ReceiptHandle)
                            fmt.Println("Commit---------->")
                        } else if a == 3 {
```

`//` 确认回滚事务消息。

```
                            comRollErr = (*mqTransProducer).Rollback(v.ReceiptHandle)
                            fmt.Println("Rollback---------->")
                        } else {
```

`//` 什么都不做，下次再检查。

```
                            fmt.Println("Unknown---------->")
                        }
                        ProcessError(comRollErr)
                    }
                    endChan <- 1
                }
            case err := <-errChan:
                {
```

`// Topic`中没有消息可消费。

```
                    if strings.Contains(err.(errors.ErrCode).Error(), "MessageNotExist")
{
                        fmt.Println("\nNo new message, continue!")
                    } else {
                        fmt.Println(err)
                        time.Sleep(time.Duration(3) * time.Second)
                    }
                    endChan <- 1
                }
            case <-time.After(35 * time.Second):
                {
                    fmt.Println("Timeout of consumer message ??")
                    return
                }
            }
        }()
```

`//` 长轮询检查半事务消息。 `//` 长轮询表示如果`Topic`没有消息则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回响应。

```
        (*mqTransProducer).ConsumeHalfMessage(respChan, errChan,
```

`3, //` 一次最多消费3条(最多可设置为`16`条)。 `3, //` 长轮询时间3秒（最多可设置为`30`秒）。 )

```
        <-endChan
    }
} func main() {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
    endpoint := "${HTTP_ENDPOINT}"
```

阿里云身份验证在运营控制台获取消息队列 `// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    accessKey := "${ACCESS_KEY}"
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    secretKey := "${SECRET_KEY}"
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。 `//`不同消息类型的`Topic`不能混用，例如普通消息的`Topic`只能用于收发普通消息，不能用于收发其他类型的消息。

```
    topic := "${TOPIC}"
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    instanceId := "${INSTANCE_ID}"
```

`//` 您在控制台创建的`Group ID`。

```
    groupId := "${GROUP_ID}"
    client := mq_http_sdk.NewAliyunMQClient(endpoint, accessKey, secretKey, "")
    mqTransProducer := client.GetTransProducer(instanceId, topic, groupId)
```

`//` 客户端需要有一个线程或者进程来消费没有确认的事务消息。 `//` 启动一个`Goroutines`来检查没有确认的事务消息。

```
    go ConsumeHalfMsg(&mqTransProducer)
```

`//` 发送4条事务消息，1条发送完就提交，其余3条通过检查半事务消息处理。

```
    for i := 0; i < 4; i++ {
        msg := mq_http_sdk.PublishMessageRequest{
            MessageBody:"I am transaction msg!",
            Properties: map[string]string{"a":strconv.Itoa(i)},
        }
```

`//` 设置事务第一次回查的时间，为相对时间。单位：秒，范围：10~300。 `//` 第一次事务回查后如果消息没有`Commit`或者`Rollback`，则之后每隔`10s`左右会回查一次，共回查`24`小时。

```
        msg.TransCheckImmunityTime = 10
        resp, pubErr := mqTransProducer.PublishMessage(msg)
        if pubErr != nil {
            fmt.Println(pubErr)
            return
        }
        fmt.Printf("Publish ---->\n\tMessageId:%s, BodyMD5:%s, Handle:%s\n",
            resp.MessageId, resp.MessageBodyMD5, resp.ReceiptHandle)
        if i == 0 {
```

`//` 发送完事务消息后能获取到半消息句柄，可以直接`Commit`或`Rollback`事务消息。

```
            ackErr := mqTransProducer.Commit(resp.ReceiptHandle)
            fmt.Println("Commit---------->")
            ProcessError(ackErr)
        }
    }
    for ; loopCount < 10 ; {
        time.Sleep(time.Duration(1) * time.Second)
    }
}
```

消息队列

**订阅事务消息**

订阅事务消息的示例代码如下。

```java
package main import (
    "fmt"
    "github.com/gogap/errors"
    "strings"
    "time"
```

)

```
func main() {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
    endpoint := "${HTTP_ENDPOINT}"
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    accessKey := "${ACCESS_KEY}"
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    secretKey := "${SECRET_KEY}"
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。 `//`不同消息类型的`Topic`不能混用，例如普通消息的`Topic`只能用于收发普通消息，不能用于收发其他类型的消息。

```
    topic := "${TOPIC}"
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    instanceId := "${INSTANCE_ID}"
```

`//` 您在控制台创建的`Group ID`。

```
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
                {
```

`//` 处理业务逻辑。

```
                    var handles []string
                    fmt.Printf("Consume %d messages---->\n", len(resp.Messages))
                    for _, v := range resp.Messages {
                        handles = append(handles, v.ReceiptHandle)
                        fmt.Printf("\tMessageID: %s, PublishTime: %d, MessageTag: %s\n"+
                            "\tConsumedTimes: %d, FirstConsumeTime: %d, NextConsumeTime:
%d\n"+
                            "\tBody: %s\n"+
                            "\tProps: %s\n",
```

消息队列 p ,

```
                            v.MessageId, v.PublishTime, v.MessageTag, v.ConsumedTimes,
                            v.FirstConsumeTime, v.NextConsumeTime, v.MessageBody,
v.Properties)
                    }
```

`// NextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
                    ackerr := mqConsumer.AckMessage(handles)
                    if ackerr != nil {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```json
                        fmt.Println(ackerr)
                        if errAckItems, ok := ackerr.(errors.ErrCode).Context()
["Detail"].([]mq_http_sdk.ErrAckItem); ok {
                           for _, errAckItem := range errAckItems {
                             fmt.Printf("\tErrorHandle:%s, ErrorCode:%s, ErrorMsg:%s\n",
                               errAckItem.ErrorHandle, errAckItem.ErrorCode,
errAckItem.ErrorMsg)
                           }
                        } else {
                           fmt.Println("ack err =", ackerr)
                        }
                        time.Sleep(time.Duration(3) * time.Second)
                    } else {
                        fmt.Printf("Ack ---->\n\t%s\n", handles)
                    }
                    endChan <- 1
                }
            case err := <-errChan:
                {
```

`// Topic`中没有消息可消费。

```
                    if strings.Contains(err.(errors.ErrCode).Error(), "MessageNotExist")
{
                        fmt.Println("\nNo new message, continue!")
                    } else {
                        fmt.Println(err)
                        time.Sleep(time.Duration(3) * time.Second)
                    }
                    endChan <- 1
                }
            case <-time.After(35 * time.Second):
                {
                    fmt.Println("Timeout of consumer message ??")
                    endChan <- 1
                }
            }
        }()
```

`//` 长轮询消费消息，网络超时时间默认为`35s`。 `//` 长轮询表示如果`Topic`没有消息，则客户端请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回响应。

```
        mqConsumer.ConsumeMessage(respChan, errChan,
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3, //` 长轮询时间`3s`（最多可设置为`30s`）。 消息队列 )

```
        <-endChan
    }
}
```

#### Python SDK

##### 准备环境

**环境要求**

安装Python。更多信息，请参见安装Python。安装的Python版本要求如下： 若您使用的SDK版本为v1.0.0，您需要安装大于等于2.5且小于3.0版本的Python。 若您使用的SDK版本大于v1.0.0，您需要安装2.5及以上版本的Python。 安装pip。更多信息，请参见安装pip。 Python 3.4及以上版本自带pip。若您安装的Python版本大于等于3.4，您可以不用单

**说明**

独安装pip。 安装完成后，您可以执行 `python -V` 命令查看Python语言版本。

**安装SDK**

```
pip install mq_http_sdk
```

##### 收发普通消息

普通消息是指RocketMQ中无特性的消息，区别于有特性的定时和延时消息、顺序消息和事务消息。本文提

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送普通消息**

发送普通消息的示例代码如下。 消息队列

```java
import sys from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_producer import * from mq_http_sdk.mq_client import * import time
```

# 初始化`client`。

```
mq_client = MQClient(
```

# 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
     "${HTTP_ENDPOINT}",
```

# AccessKey ID阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
     "${ACCESS_KEY}",
```

# AccessKey Secret阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    "${SECRET_KEY}"
```

)
# 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
topic_name = "${TOPIC}"
```

# Topic所属的实例`ID`，在`RocketMQ`控制台创建。
# 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空
间可以在`RocketMQ`控制台的实例详情页面查看。

```
instance_id = "${INSTANCE_ID}" producer = mq_client.get_producer(instance_id, topic_name)
```

# 循环发送4条消息。

```python
msg_count = 4 print("%sPublish Message To %s\nTopicName:%s\nMessageCount:%s\n" % (10 * "=", 10 * "=", topic_name, msg_count)) try:
    for i in range(msg_count):
            msg = TopicMessage(
```

# 消息内容。

```
                    "I am test message %s.hello" % i,
```

# 消息标签。

```
                    "tag %s" % i
```

)
# 设置消息的自定义属性。

```
            msg.put_property("a", "i")
```

# 设置消息的`Key`。

```python
            msg.set_message_key("MessageKey")
            re_msg = producer.publish_message(msg)
            print("Publish Message Succeed. MessageID:%s, BodyMD5:%s" %
(re_msg.message_id, re_msg.message_body_md5)) except MQExceptionBase as e:
    if e.type == "TopicNotExist":
         print("Topic not exist, please create it.")
         sys.exit(1)
    print("Publish Message Fail. Exception:%s" % e)
```

**订阅普通消息**

消息队列订阅普通消息的示例代码如下。

```
from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_consumer import * from mq_http_sdk.mq_client import *
```

# 初始化`client`。

```
mq_client = MQClient(
```

# 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
    "${HTTP_ENDPOINT}",
```

# AccessKey ID阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    "${ACCESS_KEY}",
```

# AccessKey Secret阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    "${SECRET_KEY}"
```

)
# 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
topic_name = "${TOPIC}"
```

# 您在`RocketMQ`控制台创建的`Group ID`。

```
group_id = "${GROUP_ID}"
```

# Topic所属的实例`ID`，在`RocketMQ`控制台创建。
# 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空
间可以在`RocketMQ`控制台的实例详情页面查看。

```
instance_id = "${INSTANCE_ID}" consumer = mq_client.get_consumer(instance_id, topic_name, group_id)
```

# 长轮询表示如果`Topic`没有消息，则客户端请求会在服务端挂起3秒，3秒内如果有消息可以消费则立即返回响应。
# 长轮询时间3秒（最多可设置为`30`秒）。

```
wait_seconds = 3
```

# 一次最多消费3条（最多可设置为`16`条）。

```python
batch = 3 print(("%sConsume And Ak Message From Topic%s\nTopicName:%s\nMQConsumer:%s\nWaitSeconds:%s\n" \
        % (10 * "=", 10 * "=", topic_name, group_id, wait_seconds)))
while True:
    try:
```

# 长轮询消费消息。

```python
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
```

# Topic中没有消息可消费。

```python
        if e.type == "MessageNotExist":
            print(("No new message! RequestId: %s" % e.req_id))
continue
```

消息队列

```python
            continue
        print(("Consume Message Fail! Exception:%s\n" % e))
        time.sleep(2)
        continue
```

# msg.next_consume_time前若不确认消息消费成功，则消息会被重复消费。
# 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```python
    try:
        receipt_handle_list = [msg.receipt_handle for msg in recv_msgs]
        consumer.ack_message(receipt_handle_list)
        print(("Ak %s Message Succeed.\n\n" % len(receipt_handle_list)))
    except MQExceptionBase as e:
        print(("\nAk Message Fail! Exception:%s" % e))
```

# 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```python
        if e.sub_errors:
            for sub_error in e.sub_errors:
                print(("\tErrorHandle:%s,ErrorCode:%s,ErrorMsg:%s" % \
                      (sub_error["ReceiptHandle"], sub_error["ErrorCode"],
sub_error["ErrorMessage"])))
```

##### 收发顺序消息

顺序消息（FIFO消息）是RocketMQ提供的一种严格按照顺序来发布和消费的消息类型。本文提供使用

**背景信息**

顺序消息是RocketMQ提供的一种对消息发送和消费顺序有严格要求的消息。对于一个指定的Topic，消息严格按照先进先出（FIFO）的原则进行消息发布和消费，即先发布的消息先消费，后发布的消息后消费。 RocketMQ的顺序消息中，对于指定的一个Topic，所有消息根据Sharding Key进行区块分区，同一个分区内的消息按照严格的先进先出（FIFO）原则进行发布和消费。同一分区内的消息保证顺序，不同分区之间的消息顺序不做要求。因此RocketMQ的顺序消息也叫分区顺序消息。 更多信息，请参见顺序消息。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送顺序消息**

发送顺序消息的示例代码如下。 消息队列

```java
import sys from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_producer import * from mq_http_sdk.mq_client import *
```

# 初始化`client`。

```
mq_client = MQClient(
```

# 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
     "${HTTP_ENDPOINT}",
```

# AccessKey ID阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
     "${ACCESS_KEY}",
```

# AccessKey Secret阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    "${SECRET_KEY}"
```

)
# 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
topic_name = "${TOPIC}"
```

# Topic所属的实例`ID`，在`RocketMQ`控制台创建。
# 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空
间可以在`RocketMQ`控制台的实例详情页面查看。

```
instance_id = "${INSTANCE_ID}" producer = mq_client.get_producer(instance_id, topic_name)
```

# 循环发送8条消息。

```python
msg_count = 8 print("%sPublish Message To %s\nTopicName:%s\nMessageCount:%s\n" % (10 * "=", 10 * "=", topic_name, msg_count)) try:
    for i in range(msg_count):
        msg = TopicMessage(
```

# 消息内容。

```
            "I am test message %s.hello" % i,
```

# 消息标签。

```
            "tag %s" % i
```

)
# 设置消息的自定义属性。

```
        msg.put_property("a", str(i))
```

# 设置分区顺序消息的`Sharding Key`，用于标识不同的分区。`Sharding Key`与消息的`Key`是完全不同的
概念。

```python
        msg.set_sharding_key(str(i % 3))
        re_msg = producer.publish_message(msg)
        print("Publish Message Succeed. MessageID:%s, BodyMD5:%s" % (re_msg.message_id,
re_msg.message_body_md5)) except MQExceptionBase as e:
    if e.type == "TopicNotExist":
        print("Topic not exist, please create it.")
        sys.exit(1)
    print("Publish Message Fail. Exception:%s" % e)
```

**订阅顺序消息**

消息队列订阅顺序消息的示例代码如下。

```
from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_consumer import * from mq_http_sdk.mq_client import *
```

# 初始化`client`。

```
mq_client = MQClient(
```

# 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
     "${HTTP_ENDPOINT}",
```

# AccessKey ID阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
     "${ACCESS_KEY}",
```

# AccessKey Secret阿里云身份验证，在`Apsara Uni-manager`运营控制台获取

```
    "${SECRET_KEY}"
```

)
# 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
topic_name = "${TOPIC}"
```

# 您在`RocketMQ`控制台创建的`Group ID`。

```
group_id = "${GROUP_ID}"
```

# Topic所属的实例`ID`，在`RocketMQ`控制台创建。
# 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空
间可以在`RocketMQ`控制台的实例详情页面查看。

```
instance_id = "${INSTANCE_ID}" consumer = mq_client.get_consumer(instance_id, topic_name, group_id)
```

# 长轮询顺序消费消息, 拉取到的消息可能是多个分区的（对于分区顺序消息），一个分区内的消息一定是顺序的。
# 对于分区顺序消息，只要一个分区内存在没有被确认消费的消息，那么该分区下次还会消费到相同的消息。
# 对于一个分区，只有所有消息确认消费成功才能消费下一批消息。
# 长轮询表示如果`Topic`没有消息，则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则服务端立即返回响应。

```
wait_seconds = 3
```

# 一次最多消费3条（最多可设置为`16`条）。

```python
batch = 3 print(("%sConsume And Ak Message From Topic%s\nTopicName:%s\nMQConsumer:%s\nWaitSeconds:%s\n" \
        % (10 * "=", 10 * "=", topic_name, group_id, wait_seconds)))
while True:
    try:
        recv_msgs = consumer.consume_message_orderly(batch, wait_seconds)
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
timesleep(2)
```

消息队列

```
        time.sleep(2)
        continue
```

# msg.next_consume_time前若不确认消息消费成功，则消息会被重复消费。
# 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```python
    try:
        receipt_handle_list = [msg.receipt_handle for msg in recv_msgs]
        consumer.ack_message(receipt_handle_list)
        print(("========>Ak %s Message Succeed.\n\n" % len(receipt_handle_list)))
    except MQExceptionBase as e:
        print(("\nAk Message Fail! Exception:%s" % e))
```

# 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```python
        if e.sub_errors:
            for sub_error in e.sub_errors:
                print(("\tErrorHandle:%s,ErrorCode:%s,ErrorMsg:%s" % \
                      (sub_error["ReceiptHandle"], sub_error["ErrorCode"],
sub_error["ErrorMessage"])))
```

##### 收发定时消息和延时消息

**背景信息**

延时消息：Producer将消息发送到RocketMQRocketMQ服务端，但并不期望立马投递这条消息，而是延迟一定时间后才投递到Consumer进行消费，该消息即延时消息。 定时消息：Producer将消息发送到RocketMQ服务端，但并不期望立马投递这条消息，而是推迟到在当前时间点之后的某一个时间投递到Consumer进行消费，该消息即定时消息。 在HTTP协议下，定时消息和延时消息的代码配置相同，本质都是根据消息中的属性延迟固定时间后才投递给消费者。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送定时消息或延时消息**

发送定时消息或延时消息的示例代码如下。

```java
import sys from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_producer import * from mq_http_sdk.mq_client import * import time
```

# 初始化`client`。

```
mq_client = MQClient(
```

# 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
     "${HTTP_ENDPOINT}",
```

#`AccessKey``ID`阿里云身份验证，在`Apsara``Uni``manager`运营控制台获取。
消息队列
# AccessKey ID阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
     "${ACCESS_KEY}",
```

# AccessKey Secret阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    "${SECRET_KEY}"
```

)
# 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
topic_name = "${TOPIC}"
```

# Topic所属的实例`ID`，在`RocketMQ`控制台创建。
# 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空
间可以在`RocketMQ`控制台的实例详情页面查看。

```
instance_id = "${INSTANCE_ID}" producer = mq_client.get_producer(instance_id, topic_name)
```

# 循环发送4条消息。

```python
msg_count = 4 print("%sPublish Message To %s\nTopicName:%s\nMessageCount:%s\n" % (10 * "=", 10 * "=", topic_name, msg_count)) try:
    for i in range(msg_count):
            msg = TopicMessage(
```

# 消息内容。

```
            "I am test message %s.hello" % i,
```

# 消息标签。

```
            "tag1"
```

)
# 设置属性。

```
            msg.put_property("a", "i")
```

# 设置消息的`Key`。

```
            msg.set_message_key("MessageKey")
```

# 延时消息，发送时间为`10s`后。该参数格式为毫秒级别的时间戳。
# 若发送定时消息，设置该参数时需要计算定时时间与当前时间的时间差。

```python
            msg.set_start_deliver_time(int(round(time.time() * 1000)) + 10 * 1000)
            re_msg = producer.publish_message(msg)
            print("Publish Timer Message Succeed. MessageID:%s, BodyMD5:%s" %
(re_msg.message_id, re_msg.message_body_md5)) except MQExceptionBase as e:
    if e.type == "TopicNotExist":
        print("Topic not exist, please create it.")
        sys.exit(1)
    print("Publish Message Fail. Exception:%s" % e)
```

**订阅定时消息或延时消息**

订阅定时消息或延时消息的示例代码如下。

```
from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_consumer import * from mq_http_sdk.mq_client import *
```

# 初始化`client`。

```
mq_client = MQClient(
```

#设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。
消息队列
# 设置`HTTP`协议客户端接入点
进入`RocketMQ`控制台实例详情页面的网络管理页签查看

```
    "${HTTP_ENDPOINT}",
```

# AccessKey ID阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    "${ACCESS_KEY}",
```

# AccessKey Secret阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    "${SECRET_KEY}"
```

)
# 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
topic_name = "${TOPIC}"
```

# 您在`RocketMQ`控制台创建的`Group ID`。

```
group_id = "${GROUP_ID}"
```

# Topic所属的实例`ID`，在`RocketMQ`控制台创建。
# 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空
间可以在`RocketMQ`控制台的实例详情页面查看。

```
instance_id = "${INSTANCE_ID}" consumer = mq_client.get_consumer(instance_id, topic_name, group_id)
```

# 长轮询表示如果`Topic`没有消息，则客户端请求会在服务端挂起3秒，3秒内如果有消息可以消费则立即返回响应。
# 长轮询时间3秒（最多可设置为`30`秒）。

```
wait_seconds = 3
```

# 一次最多消费3条（最多可设置为`16`条）。

```python
batch = 3 print(("%sConsume And Ak Message From Topic%s\nTopicName:%s\nMQConsumer:%s\nWaitSeconds:%s\n" \
        % (10 * "=", 10 * "=", topic_name, group_id, wait_seconds)))
while True:
    try:
```

# 长轮询消费消息。

```python
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
```

# Topic中没有消息可消费。

```python
        if e.type == "MessageNotExist":
            print(("No new message! RequestId: %s" % e.req_id))
            continue
        print(("Consume Message Fail! Exception:%s\n" % e))
        time.sleep(2)
        continue
```

# msg.next_consume_time前若不确认消息消费成功，则消息会被重复消费。
# 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
    try:
```

消息队列

```python
        receipt_handle_list = [msg.receipt_handle for msg in recv_msgs]
        consumer.ack_message(receipt_handle_list)
        print(("Ak %s Message Succeed.\n\n" % len(receipt_handle_list)))
    except MQExceptionBase as e:
        print(("\nAk Message Fail! Exception:%s" % e))
```

# 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```python
        if e.sub_errors:
            for sub_error in e.sub_errors:
                print(("\tErrorHandle:%s,ErrorCode:%s,ErrorMsg:%s" % \
                      (sub_error["ReceiptHandle"], sub_error["ErrorCode"],
sub_error["ErrorMessage"])))
```

##### 收发事务消息

RocketMQ提供类似XA或Open XA的分布式事务功能，通过RocketMQ事务消息，能达到分布式事务的最

**背景信息**

事务消息的交互流程如下图所示。 更多信息，请参见事务消息。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送事务消息**

发送事务消息的示例代码如下。

```java
#!/usr/bin/env python
# coding=utf8
import sys from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_producer import * from mq_http_sdk.mq_client import * import time import threading
```

# 初始化`client`。
消息队列

```
mq_client = MQClient(
```

# 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
     "${HTTP_ENDPOINT}",
```

# AccessKey ID阿里云身份验证，在阿里云`RAM`控制台创建。

```
     "${ACCESS_KEY}",
```

# AccessKey Secret阿里云身份验证，在阿里云`RAM`控制台创建。

```
    "${SECRET_KEY}"
```

)
# 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
topic_name = "${TOPIC}"
```

# 您在`RocketMQ`控制台创建的`Group ID`。

```
group_id = "${GROUP_ID}"
```

# Topic所属的实例`ID`，在`RocketMQ`控制台创建。
# 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空

```
instance_id = "${INSTANCE_ID}"
```

# 循环发送4条事务消息。

```python
msg_count = 4 print("%sPublish Transaction Message To %s\nTopicName:%s\nMessageCount:%s\n" \
      % (10 * "=", 10 * "=", topic_name, msg_count))
def process_trans_error(exp):
    print("\nCommit/Roll Transaction Message Fail! Exception:%s" % exp)
```

# 如果`Commit`或`Rollback`时超过了`TransCheckImmunityTime`（针对发送事务消息的句柄）或者超过`10s`（
针对`consumeHalfMessage`的句柄），则`Commit`或`Rollback`失败。

```python
    if exp.sub_errors:
        for sub_error in exp.sub_errors:
            print("\tErrorHandle:%s,ErrorCode:%s,ErrorMsg:%s" % \
                  (sub_error["ReceiptHandle"], sub_error["ErrorCode"],
sub_error["ErrorMessage"]))
```

# 客户端需要有一个线程或者进程来消费没有确认的事务消息。
# 启动一个线程来检查没有确认的事务消息。

```python
class ConsumeHalfMessageThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.count = 0
```

# 重新`New`一个`Client`

```
        self.mq_client = MQClient(
```

# 设置`HTTP`接入域名，进入`RocketMQ`控制台实例详情页面的`HTTP`接入点区域查看。

```
                "${HTTP_ENDPOINT}",
```

# AccessKey ID阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${ACCESS_KEY}",
```

# AccessKey Secret阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
                "${SECRET_KEY}"
```

)

```python
        self.trans_producer = self.mq_client.get_trans_producer(instance_id,
topic_name, group_id)
    def run(self):
        while 1:
```

消息队列

```python
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
                    if a == 1:
```

# 确认提交事务消息。

```python
                        self.trans_producer.commit(half_msg.receipt_handle)
                        self.count += 1
                        print("------>commit")
                    elif a == 2 and half_msg.consumed_times > 1:
```

# 确认提交事务消息。

```python
                        self.trans_producer.commit(half_msg.receipt_handle)
                        self.count += 1
                        print("------>commit")
                    elif a == 3:
```

# 确认回滚事务消息。

```python
                        self.trans_producer.rollback(half_msg.receipt_handle)
                        self.count += 1
                        print("------>rollback")
                    else:
```

# 什么都不做，下次再检查。

```python
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
```

消息队列

```
    for i in range(msg_count):
        msg = TopicMessage(
```

# 消息内容。

```
            "I am test message %s." % i,
```

# 消息标签。

```
            "tagA"
```

)
# 设置消息的自定义属性。

```
        msg.put_property("xy", i)
```

# 设置消息的`Key`。

```
        msg.set_message_key("MessageKey")
```

# 设置事务第一次回查的时间，为相对时间。单位：秒，范围：10~300。
# 第一次事务回查后如果消息没有`Commit`或者`Rollback`，则之后每隔`10s`左右会回查一次，共回查`24`小时
。

```python
        msg.set_trans_check_immunity_time(10)
        re_msg = trans_producer.publish_message(msg)
        print("Publish Transaction Message Succeed. MessageID:%s, BodyMD5:%s,
Handle:%s" \
              % (re_msg.message_id, re_msg.message_body_md5, re_msg.receipt_handle))
        time.sleep(1)
        if i == 0:
```

# 发送完事务消息后能获取到半消息句柄，可以直接`Commit`或`Rollback`事务消息。

```python
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

**订阅事务消息**

订阅事务消息的示例代码如下。

```
from mq_http_sdk.mq_exception import MQExceptionBase from mq_http_sdk.mq_consumer import * from mq_http_sdk.mq_client import *
```

# 初始化`client`。

```
mq_client = MQClient(
```

# 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
    "${HTTP_ENDPOINT}",
```

# AccessKey ID阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    "${ACCESS_KEY}",
```

# AccessKey Secret阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
    "${SECRET_KEY}"
```

) 消息队列 )
# 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
topic_name = "${TOPIC}"
```

# 您在`RocketMQ`控制台创建的`Group ID`。

```
group_id = "${GROUP_ID}"
```

# Topic所属的实例`ID`，在`RocketMQ`控制台创建。
# 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空
间可以在`RocketMQ`控制台的实例详情页面查看。

```
instance_id = "${INSTANCE_ID}" consumer = mq_client.get_consumer(instance_id, topic_name, group_id)
```

# 长轮询表示如果`Topic`没有消息，则客户端请求会在服务端挂起3秒，3秒内如果有消息可以消费则立即返回响应。
# 长轮询时间3秒（最多可设置为`30`秒）。

```
wait_seconds = 3
```

# 一次最多消费3条（最多可设置为`16`条）。

```python
batch = 3 print(("%sConsume And Ak Message From Topic%s\nTopicName:%s\nMQConsumer:%s\nWaitSeconds:%s\n" \
        % (10 * "=", 10 * "=", topic_name, group_id, wait_seconds)))
while True:
    try:
```

# 长轮询消费消息。

```python
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
```

# Topic中没有消息可消费。

```python
        if e.type == "MessageNotExist":
            print(("No new message! RequestId: %s" % e.req_id))
            continue
        print(("Consume Message Fail! Exception:%s\n" % e))
        time.sleep(2)
        continue
```

# msg.next_consume_time前若不确认消息消费成功，则消息会被重复消费。
# 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```python
    try:
        receipt_handle_list = [msg.receipt_handle for msg in recv_msgs]
        consumer.ack_message(receipt_handle_list)
        print(("Ak %s Message Succeed.\n\n" % len(receipt_handle_list)))
    except MQExceptionBase as e:
        print(("\nAk Message Fail! Exception:%s" % e))
```

#某些消息的句柄可能超时，会导致消息消费状态确认不成功。
消息队列
# 某些消息的句柄可能超时
会导致消息消费状态确认不成功

```python
        if e.sub_errors:
            for sub_error in e.sub_errors:
                print(("\tErrorHandle:%s,ErrorCode:%s,ErrorMsg:%s" % \
                      (sub_error["ReceiptHandle"], sub_error["ErrorCode"],
sub_error["ErrorMessage"])))
```

#### Node.js SDK

##### 准备环境

**环境要求**

安装Node.js 7.6.0或以上版本。更多信息，请参见安装Node.js。 安装完成后，您可以执行 `node -V` 命令查看Node.js语言版本。

```
npm i @aliyunmq/mq-http-sdk
```

##### 收发普通消息

普通消息是指RocketMQ中无特性的消息，区别于有特性的定时和延时消息、顺序消息和事务消息。本文提

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送普通消息**

发送普通消息的示例代码如下。 消息队列

```
const {
  MQClient,
  MessageProperties
} = require('@aliyunmq/mq-http-sdk');
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
const endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在阿里云`RAM`控制台创建。

```
const accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在阿里云`RAM`控制台创建。

```
const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret);
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
const topic = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
const instanceId = "${INSTANCE_ID}"; const producer = client.getProducer(instanceId, topic); (async function(){
  try {
```

`//` 循环发送4条消息。

```
    for(var i = 0; i < 4; i++) {
      let res;
      msgProps = new MessageProperties();
```

`//` 设置消息的自定义属性。

```
      msgProps.putProperty("a", i);
```

`//` 设置消息的`Key`。

```
      msgProps.messageKey("MessageKey");
      res = await producer.publishMessage("hello mq.", "", msgProps);
      console.log("Publish message: MessageID:%s,BodyMD5:%s", res.body.MessageId, res.b
ody.MessageBodyMD5);
    }
  } catch(e) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理。

```
    console.log(e)
  }
})();
```

**订阅普通消息**

订阅普通消息的示例代码如下。

```
const {
  MQClient
} = require('@aliyunmq/mq-http-sdk');
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
const endpoint = "${HTTPENDPOINT}";
```

消息队列 _ `// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
const accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret);
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
const topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
const groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
const instanceId = "${INSTANCE_ID}"; const consumer = client.getConsumer(instanceId, topic, groupId); (async function(){
```

`//` 循环消费消息。

```
  while(true) {
    try {
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息，则客户端请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回响应。

```
      res = await consumer.consumeMessage(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3 //` 长轮询时间3秒（最多可设置为`30`秒）。

```
          );
      if (res.code == 200) {
```

`//` 消息消费处理逻辑。

```
        console.log("Consume Messages, requestId:%s", res.requestId);
        const handles = res.body.map((message) => {
console.log("\tMessageId:%s,Tag:%s,PublishTime:%d,NextConsumeTime:%d,FirstConsumeTime:%d, nsumedTimes:%d,Body:%s" +
            ",Props:%j,MessageKey:%s,Prop-A:%s",
              message.MessageId, message.MessageTag, message.PublishTime, message.NextCo
nsumeTime, message.FirstConsumeTime, message.ConsumedTimes, message.MessageBody,message.Properties,message.MessageKey,message.Properties.a);
          return message.ReceiptHandle;
        });
```

`// message.NextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
        res = await consumer.ackMessage(handles);
        if (res.code != 204) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
          console.log("Ack Message Fail:");
          const failHandles = res.body.map((error)=>{
            console.log("\tErrorHandle:%s, Code:%s, Reason:%s\n", error.ReceiptHandle,
error.ErrorCode, error.ErrorMessage);
```

消息队列

```
            return error.ReceiptHandle;
          });
          handles.forEach((handle)=>{
            if (failHandles.indexOf(handle) < 0) {
              console.log("\tSucHandle:%s\n", handle);
            }
          });
        } else {
```

`//` 确认消息消费成功。

```
          console.log("Ack Message suc, RequestId:%s\n\t", res.requestId,
handles.join(','));
        }
      }
    } catch(e) {
      if (e.Code.indexOf("MessageNotExist") > -1) {
```

`//` 没有消息，则继续长轮询服务器。

```
        console.log("Consume Message: no new message, RequestId:%s, Code:%s",
e.RequestId, e.Code);
      } else {
        console.log(e);
      }
    }
  }
})();
```

##### 收发顺序消息

顺序消息（FIFO消息）是RocketMQ提供的一种严格按照顺序来发布和消费的消息类型。本文提供使用

**背景信息**

顺序消息是RocketMQ提供的一种对消息发送和消费顺序有严格要求的消息。对于一个指定的Topic，消息严格按照先进先出（FIFO）的原则进行消息发布和消费，即先发布的消息先消费，后发布的消息后消费。 RocketMQ的顺序消息中，对于指定的一个Topic，所有消息根据Sharding Key进行区块分区，同一个分区内的消息按照严格的先进先出（FIFO）原则进行发布和消费。同一分区内的消息保证顺序，不同分区之间的消息顺序不做要求。因此RocketMQ的顺序消息也叫分区顺序消息。 更多信息，请参见顺序消息。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送顺序消息**

发送顺序消息的示例代码如下。 消息队列

```
const {
  MQClient,
  MessageProperties
} = require('@aliyunmq/mq-http-sdk');
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
const endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
const accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret);
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
const topic = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
const instanceId = "${INSTANCE_ID}"; const producer = client.getProducer(instanceId, topic); (async function(){
  try {
```

`//` 循环发送8条消息。

```
    for(var i = 0; i < 8; i++) {
      msgProps = new MessageProperties();
```

`//` 设置消息的自定义属性。

```
      msgProps.putProperty("a", i);
```

`//` 设置分区顺序消息的`Sharding Key`，用于标识不同的分区。`Sharding Key`与消息的`Key`是完全不同的概念。

```
      msgProps.shardingKey(i % 2);
      res = await producer.publishMessage("hello mq.", "", msgProps);
      console.log("Publish message: MessageID:%s,BodyMD5:%s", res.body.MessageId, res.b
ody.MessageBodyMD5);
    }
  } catch(e) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理。

```
    console.log(e)
  }
})();
```

**订阅顺序消息**

订阅顺序消息的示例代码如下。

```
const {
  MQClient,
} = require('@aliyunmq/mq-http-sdk');
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
const endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。 消息队列

```
const accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret);
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
const topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
const groupId = "GID_http";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
const instanceId = "${INSTANCE_ID}"; const consumer = client.getConsumer(instanceId, topic, groupId); (async function(){
```

`//` 循环消费消息。

```
  while(true) {
    try {
```

`//` 长轮询顺序消费消息, 拉取到的消息可能是多个分区的（对于分区顺序消息），一个分区内的消息一定是顺序的。 `//` 对于分区顺序消息，只要一个分区内存在没有被确认消费的消息，那么该分区下次还会消费到相同的消息。 `//` 对于一个分区，只有所有消息确认消费成功才能消费下一批消息。 `//` 长轮询表示如果`Topic`没有消息，则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则服务端立即返回响应。

```
      res = await consumer.consumeMessageOrderly(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3 //` 长轮询时间3秒（最多可设置为`30`秒）。

```
          );
      if (res.code == 200) {
```

`//` 消息消费处理逻辑。

```
        console.log("Consume Messages, requestId:%s", res.requestId);
        const handles = res.body.map((message) => {
console.log("\tMessageId:%s,Tag:%s,PublishTime:%d,NextConsumeTime:%d,FirstConsumeTime:%d, nsumedTimes:%d,Body:%s" +
            ",Props:%j,ShardingKey:%s,Prop-A:%s,Tag:%s",
              message.MessageId, message.MessageTag, message.PublishTime, message.NextCo
nsumeTime, message.FirstConsumeTime, message.ConsumedTimes, message.MessageBody,message.Properties,message.ShardingKey,message.Properties.a,message.M sageTag);
          return message.ReceiptHandle;
        });
```

`// message.NextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
        res = await consumer.ackMessage(handles);
        if (res.code != 204) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
          console.log("Ack Message Fail:");
```

消息队列

```
          const failHandles = res.body.map((error)=>{
            console.log("\tErrorHandle:%s, Code:%s, Reason:%s\n", error.ReceiptHandle,
error.ErrorCode, error.ErrorMessage);
            return error.ReceiptHandle;
          });
          handles.forEach((handle)=>{
            if (failHandles.indexOf(handle) < 0) {
              console.log("\tSucHandle:%s\n", handle);
            }
          });
        } else {
```

`//` 消息确认消费成功。

```
          console.log("Ack Message suc, RequestId:%s\n\t", res.requestId,
handles.join(','));
        }
      }
    } catch(e) {
      if (e.Code.indexOf("MessageNotExist") > -1) {
```

`//` 没有消息，则继续长轮询服务器。

```
        console.log("Consume Message: no new message, RequestId:%s, Code:%s",
e.RequestId, e.Code);
      } else {
        console.log(e);
      }
    }
  }
})();
```

##### 收发定时消息和延时消息

**背景信息**

延时消息：Producer将消息发送到RocketMQRocketMQ服务端，但并不期望立马投递这条消息，而是延迟一定时间后才投递到Consumer进行消费，该消息即延时消息。 定时消息：Producer将消息发送到RocketMQ服务端，但并不期望立马投递这条消息，而是推迟到在当前时间点之后的某一个时间投递到Consumer进行消费，该消息即定时消息。 在HTTP协议下，定时消息和延时消息的代码配置相同，本质都是根据消息中的属性延迟固定时间后才投递给消费者。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送定时消息或延时消息**

发送定时消息或延时消息的示例代码如下。 消息队列

```
const {
  MQClient,
  MessageProperties
} = require('@aliyunmq/mq-http-sdk');
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
const endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
const accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret);
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
const topic = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
const instanceId = "${INSTANCE_ID}"; const producer = client.getProducer(instanceId, topic); (async function(){
  try {
```

`//` 循环发送4条消息。

```
    for(var i = 0; i < 4; i++) {
      let res;
      msgProps = new MessageProperties();
```

`//` 设置消息的自定义属性。

```
      msgProps.putProperty("a", i);
```

`//` 设置消息的`Key`。

```
      msgProps.messageKey("MessageKey");
```

`//` 延时消息，发送时间为`10s`后。该参数格式为毫秒级别的时间戳。 `//` 若发送定时消息，设置该参数时需要计算定时时间与当前时间的时间差。

```
      msgProps.startDeliverTime(Date.now() + 10 * 1000);
      res = await producer.publishMessage("hello mq. timer msg!", "TagA", msgProps);
      console.log("Publish message: MessageID:%s,BodyMD5:%s", res.body.MessageId, res.b
ody.MessageBodyMD5);
    }
  } catch(e) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理。

```
    console.log(e)
  }
})();
```

**订阅定时消息或延时消息**

订阅定时消息或延时消息的示例代码如下。

```
const {
  MQClient
} = require('@aliyunmq/mq-http-sdk');
```

消息队列 `//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
const endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
const accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret);
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
const topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
const groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
const instanceId = "${INSTANCE_ID}"; const consumer = client.getConsumer(instanceId, topic, groupId); (async function(){
```

`//` 循环消费消息。

```
  while(true) {
    try {
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息，则客户端请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回响应。

```
      res = await consumer.consumeMessage(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3 //` 长轮询时间3秒（最多可设置为`30`秒）。

```
          );
      if (res.code == 200) {
```

`//` 消息消费处理逻辑。

```
        console.log("Consume Messages, requestId:%s", res.requestId);
        const handles = res.body.map((message) => {
console.log("\tMessageId:%s,Tag:%s,PublishTime:%d,NextConsumeTime:%d,FirstConsumeTime:%d, nsumedTimes:%d,Body:%s" +
            ",Props:%j,MessageKey:%s,Prop-A:%s",
              message.MessageId, message.MessageTag, message.PublishTime, message.NextCo
nsumeTime, message.FirstConsumeTime, message.ConsumedTimes, message.MessageBody,message.Properties,message.MessageKey,message.Properties.a);
          return message.ReceiptHandle;
        });
```

`// message.NextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
        res = await consumer.ackMessage(handles);
        if (res.code != 204) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
          console.log("Ack Message Fail:");
```

消息队列

```
          const failHandles = res.body.map((error)=>{
            console.log("\tErrorHandle:%s, Code:%s, Reason:%s\n", error.ReceiptHandle,
error.ErrorCode, error.ErrorMessage);
            return error.ReceiptHandle;
          });
          handles.forEach((handle)=>{
            if (failHandles.indexOf(handle) < 0) {
              console.log("\tSucHandle:%s\n", handle);
            }
          });
        } else {
```

`//` 确认消息消费成功。

```
          console.log("Ack Message suc, RequestId:%s\n\t", res.requestId,
handles.join(','));
        }
      }
    } catch(e) {
      if (e.Code.indexOf("MessageNotExist") > -1) {
```

`//` 没有消息，则继续长轮询服务器。

```
        console.log("Consume Message: no new message, RequestId:%s, Code:%s",
e.RequestId, e.Code);
      } else {
        console.log(e);
      }
    }
  }
})();
```

##### 收发事务消息

RocketMQ提供类似XA或Open XA的分布式事务功能，通过RocketMQ事务消息，能达到分布式事务的最

**背景信息**

事务消息的交互流程如下图所示。 更多信息，请参见事务消息。

**前提条件**

您已完成以下操作： 消息队列创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送事务消息**

发送事务消息的示例代码如下。

```
const {
  MQClient,
  MessageProperties
} = require('@aliyunmq/mq-http-sdk');
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
const endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
const accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret);
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
const topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
const groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
const instanceId = "${INSTANCE_ID}"; const mqTransProducer = client.getTransProducer(instanceId, topic, groupId); async function processTransResult(res, msgId) {
    if (!res) {
        return;
    }
    if (res.code != 204) {
```

`//` 如果`Commit`或`Rollback`时超过了`TransCheckImmunityTime`（针对发送事务消息的句柄）或者超过`10` s（针对`consumeHalfMessage`的句柄），则`Commit`或`Rollback`失败。

```
      console.log("Commit/Rollback Message Fail:");
      const failHandles = res.body.map((error) => {
        console.log("\tErrorHandle:%s, Code:%s, Reason:%s\n", error.ReceiptHandle,
error.ErrorCode, error.ErrorMessage);
        return error.ReceiptHandle;
      });
    } else {
      console.log("Commit/Rollback Message suc!!! %s", msgId);
    }
} var halfMessageCount = 0; var halfMessageConsumeCount = 0; (async function(){
  try {
```

`//`循环发送条事务消息消息队列 `//` 循环发送4条事务消息。

```
    for(var i = 0; i < 4; i++) {
      let res;
      msgProps = new MessageProperties();
```

`//` 设置消息的自定义属性。

```
      msgProps.putProperty("a", i);
```

`//` 设置消息的`Key`。

```
      msgProps.messageKey("MessageKey");
```

`//` 设置事务第一次回查的时间，为相对时间。单位：秒，范围：10~300。 `//` 第一次事务回查后如果消息没有`Commit`或者`Rollback`，则之后每隔`10s`左右会回查一次，共回查`24`小时 。

```
      msgProps.transCheckImmunityTime(10);
      res = await mqTransProducer.publishMessage("hello mq.", "tagA", msgProps);
      console.log("Publish message: MessageID:%s,BodyMD5:%s,Handle:%s",
res.body.MessageId, res.body.MessageBodyMD5, res.body.ReceiptHandle);
      if (res && i == 0) {
```

`//` 发送完事务消息后能获取到半消息句柄，可以直接`Commit`或`Rollback`事务消息。

```
          const msgId = res.body.MessageId;
          res = await mqTransProducer.commit(res.body.ReceiptHandle);
          console.log("Commit msg when publish, %s", msgId);
```

`//` 如果`Commit`或`Rollback`时超过了`TransCheckImmunityTime`则会失败。

```
        processTransResult(res, msgId);
      }
    }
  } catch(e) {
```

`//` 消息发送失败，需要进行重试处理，可重新发送这条消息或持久化这条数据进行补偿处理。

```
    console.log(e)
  }
})();
```

`//` 客户端需要有一个线程或者进程来消费没有确认的事务消息。 `//` 检查没有确认的事务消息。

```
(async function() {
```

`//` 循环检查事务半消息，类似消费普通消息。

```
  while(halfMessageCount < 3 && halfMessageConsumeCount < 15) {
    try {
        halfMessageConsumeCount++;
      res = await mqTransProducer.consumeHalfMessage(3, 3);
      if (res.code == 200) {
```

`//` 消息消费处理逻辑。

```
        console.log("Consume Messages, requestId:%s", res.requestId);
        res.body.forEach(async (message) => {
console.log("\tMessageId:%s,Tag:%s,PublishTime:%d,NextConsumeTime:%d,FirstConsumeTime:%d, nsumedTimes:%d,Body:%s" +
            ",Props:%j,MessageKey:%s,Prop-A:%s",
              message.MessageId, message.MessageTag, message.PublishTime, message.NextCo
nsumeTime, message.FirstConsumeTime, message.ConsumedTimes, message.MessageBody,message.Properties,message.MessageKey,message.Properties.a);
          var propA = message.Properties && message.Properties.a ?
parseInt(message.Properties.a) : 0;
                  var opResp;
if(propA==1||(propA==2&&messageConsumedTimes>1)){
```

消息队列

```
                  if (propA == 1 || (propA == 2 && message.ConsumedTimes > 1)) {
                      opResp = await mqTransProducer.commit(message.ReceiptHandle);
                      console.log("Commit msg when check half, %s", message.MessageId);
                      halfMessageCount++;
                  } else if (propA == 3) {
                      opResp = await mqTransProducer.rollback(message.ReceiptHandle);
                      console.log("Rollback msg when check half, %s",
message.MessageId);
                      halfMessageCount++;
                  }
                  processTransResult(opResp, message.MessageId);
        });
      }
    } catch(e) {
      if (e.Code && e.Code.indexOf("MessageNotExist") > -1) {
```

`//` 没有消息，则继续长轮询服务器。

```
        console.log("Consume Transaction Half msg: no new message, RequestId:%s,
Code:%s", e.RequestId, e.Code);
      } else {
        console.log(e);
      }
    }
  }
})();
```

**订阅事务消息**

订阅事务消息的示例代码如下。

```
const {
  MQClient
} = require('@aliyunmq/mq-http-sdk');
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
const endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
const accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
const accessKeySecret = "${SECRET_KEY}"; var client = new MQClient(endpoint, accessKeyId, accessKeySecret);
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
const topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
const groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
const instanceId = "${INSTANCE_ID}"; const consumer = client.getConsumer(instanceId, topic, groupId); (async function(){
```

`//`循环消费消息。 消息队列 `//` 循环消费消息

```
  while(true) {
    try {
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息，则客户端请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回响应。

```
      res = await consumer.consumeMessage(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3 //` 长轮询时间3秒（最多可设置为`30`秒）。

```
          );
      if (res.code == 200) {
```

`//` 消息消费处理逻辑。

```
        console.log("Consume Messages, requestId:%s", res.requestId);
        const handles = res.body.map((message) => {
console.log("\tMessageId:%s,Tag:%s,PublishTime:%d,NextConsumeTime:%d,FirstConsumeTime:%d, nsumedTimes:%d,Body:%s" +
            ",Props:%j,MessageKey:%s,Prop-A:%s",
              message.MessageId, message.MessageTag, message.PublishTime, message.NextCo
nsumeTime, message.FirstConsumeTime, message.ConsumedTimes, message.MessageBody,message.Properties,message.MessageKey,message.Properties.a);
          return message.ReceiptHandle;
        });
```

`// message.NextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
        res = await consumer.ackMessage(handles);
        if (res.code != 204) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
          console.log("Ack Message Fail:");
          const failHandles = res.body.map((error)=>{
            console.log("\tErrorHandle:%s, Code:%s, Reason:%s\n", error.ReceiptHandle,
error.ErrorCode, error.ErrorMessage);
            return error.ReceiptHandle;
          });
          handles.forEach((handle)=>{
            if (failHandles.indexOf(handle) < 0) {
              console.log("\tSucHandle:%s\n", handle);
            }
          });
        } else {
```

`//` 确认消息消费成功。

```
          console.log("Ack Message suc, RequestId:%s\n\t", res.requestId,
handles.join(','));
        }
      }
    } catch(e) {
      if (e.Code.indexOf("MessageNotExist") > -1) {
```

`//` 没有消息，则继续长轮询服务器。

```
        console.log("Consume Message: no new message, RequestId:%s, Code:%s",
e.RequestId, e.Code);
      } else {
        console.log(e);
```

消息队列

```
      }
    }
  }
})();
```

#### PHP SDK

##### 准备环境

**环境要求**

安装PHP 5.5.0或以上版本，更多信息，请参见安装PHP。 安装Composer，更多信息，请参见安装Composer。 安装完成后，您可以执行 `php -v` 命令查看PHP语言版本。

**安装SDK**

1. 在您PHP安装目录下的composer.json文件中加入以下依赖：

```json
{
  "require": {
     "aliyunmq/mq-http-sdk": ">=1.0.3"
  }
}
```

2. 执行以下命令，通过Composer安装依赖。

```
composer install
```

##### 收发普通消息

普通消息是指RocketMQ中无特性的消息，区别于有特性的定时和延时消息、顺序消息和事务消息。本文提

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送普通消息**

发送普通消息的示例代码如下。

```
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; useMQ\MQClient;
```

消息队列

```java
use MQ\MQClient; class ProducerTest {
    private $client;
    private $producer;
    public function __construct()
    {
        $this->client = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${SECRET_KEY}"
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
        $topic = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        $instanceId = "${INSTANCE_ID}";
        $this->producer = $this->client->getProducer($instanceId, $topic);
    }
    public function run()
    {
        try
        {
            for ($i=1; $i<=4; $i++)
            {
                $publishMessage = new TopicMessage(
```

`//` 消息内容。

```
                "hello mq!"
                );
```

`//` 设置消息的自定义属性。

```
                $publishMessage->putProperty("a", $i);
```

`//` 设置消息的`Key`。

```
                $publishMessage->setMessageKey("MessageKey");
                $result = $this->producer->publishMessage($publishMessage);
                print "Send mq message success. msgId is:" . $result->getMessageId() . "
, bodyMD5 is:" . $result->getMessageBodyMD5() . "\n";
            }
        } catch (\Exception $e) {
            print_r($e->getMessage() . "\n");
        }
    }
}
```

消息队列

```
$instance = new ProducerTest(); $instance->run();
```

?>

**订阅普通消息**

订阅普通消息的示例代码如下。

```java
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; use MQ\MQClient; class ConsumerTest {
    private $client;
    private $producer;
    public function __construct()
    {
        $this->client = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${SECRET_KEY}"
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
        $topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
        $groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        $instanceId = "${INSTANCE_ID}";
        $this->consumer = $this->client->getConsumer($instanceId, $topic, $groupId);
    }
    public function run()
    {
```

`//` 在当前线程循环消费消息，建议多开个几个线程并发消费消息。

```
        while (True) {
            try {
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息,则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回客户端。 消息队列

```
                $messages = $this->consumer->consumeMessage(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3 //` 长轮询时间3秒（最多可设置为`30`秒）。

```
                );
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\MessageNotExistException) {
```

`// Topic`中没有消息可消费，继续轮询。

```
                    printf("No message, contine long polling!RequestId:%s\n", $e->getReq
uestId());
                    continue;
                }
                print_r($e->getMessage() . "\n");
                sleep(3);
                continue;
            }
            print "consume finish, messages:\n";
```

`//` 处理业务逻辑。

```
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
            }
```

// $message->getNextConsumeTime()前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
            print_r($receiptHandles);
            try {
                $this->consumer->ackMessage($receiptHandles);
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\AckMessageException) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
                    printf("Ack Error, RequestId:%s\n", $e->getRequestId());
                    foreach ($e->getAckMessageErrorItems() as $errorItem) {
                        printf("\tReceiptHandle:%s, ErrorCode:%s, ErrorMsg:%s\n", $error
Item->getReceiptHandle(), $errorItem->getErrorCode(), $errorItem->getErrorCode());
                    }
                }
            }
            print "ack finish\n";
        }
```

消息队列

```
    }
} $instance = new ConsumerTest(); $instance->run();
```

?>

##### 收发顺序消息

顺序消息（FIFO消息）是RocketMQ提供的一种严格按照顺序来发布和消费的消息类型。本文提供使用

**背景信息**

顺序消息是RocketMQ提供的一种对消息发送和消费顺序有严格要求的消息。对于一个指定的Topic，消息严格按照先进先出（FIFO）的原则进行消息发布和消费，即先发布的消息先消费，后发布的消息后消费。 RocketMQ的顺序消息中，对于指定的一个Topic，所有消息根据Sharding Key进行区块分区，同一个分区内的消息按照严格的先进先出（FIFO）原则进行发布和消费。同一分区内的消息保证顺序，不同分区之间的消息顺序不做要求。因此RocketMQ的顺序消息也叫分区顺序消息。 更多信息，请参见顺序消息。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送顺序消息**

发送顺序消息的示例代码如下。

```java
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; use MQ\MQClient; class ProducerTest {
    private $client;
    private $producer;
    public function __construct()
    {
        $this->client = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
"${SECRETKEY}"
```

消息队列

```
            ${SECRET_KEY}
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
        $topic = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        $instanceId = "${INSTANCE_ID}";
        $this->producer = $this->client->getProducer($instanceId, $topic);
    }
    public function run()
    {
        try
        {
            for ($i=1; $i<=4; $i++)
            {
                $publishMessage = new TopicMessage(
```

"hello mq!"// 消息内容。

```
                );
```

`//` 设置消息的自定义属性。

```
                $publishMessage->putProperty("a", $i);
```

`//` 设置分区顺序消息的`Sharding Key`，用于标识不同的分区。`Sharding Key`与消息的`Key`是完全不同的概念。

```
                $publishMessage->setShardingKey($i % 2);
                $result = $this->producer->publishMessage($publishMessage);
                print "Send mq message success. msgId is:" . $result->getMessageId() . "
, bodyMD5 is:" . $result->getMessageBodyMD5() . "\n";
            }
        } catch (\Exception $e) {
            print_r($e->getMessage() . "\n");
        }
    }
} $instance = new ProducerTest(); $instance->run();
```

?>

**订阅顺序消息**

订阅顺序消息的示例代码如下。

```
<?php require "vendor/autoload.php";
```

消息队列

```java
use MQ\Model\TopicMessage; use MQ\MQClient; class ConsumerTest {
    private $client;
    private $producer;
    public function __construct()
    {
        $this->client = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${SECRET_KEY}"
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
        $topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
        $groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        $instanceId = "${INSTANCE_ID}";
        $this->consumer = $this->client->getConsumer($instanceId, $topic, $groupId);
    }
    public function run()
    {
```

`//` 在当前线程循环消费消息，建议多开个几个线程并发消费消息。

```
        while (True) {
            try {
```

`//` 长轮询顺序消费消息, 拉取到的消息可能是多个分区的（对于分区顺序消息），一个分区内的消息一定是顺序的。 `//` 对于分区顺序消息，只要一个分区内存在没有被确认消费的消息，那么该分区下次还会消费到相同的消息。 `//` 对于一个分区，只有所有消息确认消费成功才能消费下一批消息。 `//` 长轮询表示如果`Topic`没有消息，则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则服务端立即返回响应。

```
                $messages = $this->consumer->consumeMessageOrderly(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3 //` 长轮询时间3秒（最多可设置为`30`秒）。

```
                );
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\MessageNotExistException) {
```

`//` 没有消息，则继续长轮询服务器。

```
                    printf("No message, contine long polling!RequestId:%s\n", $e->getReq
uestId());
                    continue;
                }
```

消息队列

```
                print_r($e->getMessage() . "\n");
                sleep(3);
                continue;
            }
            print "======>consume finish, messages:\n";
```

`//` 处理业务逻辑。

```
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
            }
```

// $message->getNextConsumeTime()前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
            print_r($receiptHandles);
            try {
                $this->consumer->ackMessage($receiptHandles);
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\AckMessageException) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
                    printf("Ack Error, RequestId:%s\n", $e->getRequestId());
                    foreach ($e->getAckMessageErrorItems() as $errorItem) {
                        printf("\tReceiptHandle:%s, ErrorCode:%s, ErrorMsg:%s\n", $error
Item->getReceiptHandle(), $errorItem->getErrorCode(), $errorItem->getErrorCode());
                    }
                }
            }
            print "=======>ack finish\n";
        }
    }
} $instance = new ConsumerTest(); $instance->run();
```

?> 消息队列

##### 收发定时消息和延时消息

**背景信息**

延时消息：Producer将消息发送到RocketMQRocketMQ服务端，但并不期望立马投递这条消息，而是延迟一定时间后才投递到Consumer进行消费，该消息即延时消息。 定时消息：Producer将消息发送到RocketMQ服务端，但并不期望立马投递这条消息，而是推迟到在当前时间点之后的某一个时间投递到Consumer进行消费，该消息即定时消息。 在HTTP协议下，定时消息和延时消息的代码配置相同，本质都是根据消息中的属性延迟固定时间后才投递给消费者。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送定时消息或延时消息**

发送定时消息或延时消息的示例代码如下。

```java
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; use MQ\MQClient; class ProducerTest {
    private $client;
    private $producer;
    public function __construct()
    {
        $this->client = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的接入点区域查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${SECRET_KEY}"
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
        $topic = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        $instanceId = "${INSTANCE_ID}";
```

消息队列

```
        $this->producer = $this->client->getProducer($instanceId, $topic);
    }
    public function run()
    {
        try
        {
            for ($i=1; $i<=4; $i++)
            {
                $publishMessage = new TopicMessage(
```

"hello mq!"// 消息内容。

```
                );
```

`//` 设置消息的自定义属性。

```
                $publishMessage->putProperty("a", $i);
```

`//` 设置消息的`Key`。

```
                $publishMessage->setMessageKey("MessageKey");
```

`//` 延时消息，发送时间为`10s`后。该参数格式为毫秒级别的时间戳。 `//` 若发送定时消息，设置该参数时需要计算定时时间与当前时间的时间差。

```
                $publishMessage->setStartDeliverTime(time() * 1000 + 10 * 1000);
                $result = $this->producer->publishMessage($publishMessage);
                print "Send mq message success. msgId is:" . $result->getMessageId() . "
, bodyMD5 is:" . $result->getMessageBodyMD5() . "\n";
            }
        } catch (\Exception $e) {
            print_r($e->getMessage() . "\n");
        }
    }
} $instance = new ProducerTest(); $instance->run();
```

?>

**订阅定时消息或延时消息**

订阅定时消息或延时消息的示例代码如下。

```java
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; use MQ\MQClient; class ConsumerTest {
    private $client;
```

消息队列 p

```java
    private $producer;
    public function __construct()
    {
        $this->client = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${SECRET_KEY}"
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
        $topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
        $groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        $instanceId = "${INSTANCE_ID}";
        $this->consumer = $this->client->getConsumer($instanceId, $topic, $groupId);
    }
    public function run()
    {
```

`//` 在当前线程循环消费消息，建议多开个几个线程并发消费消息。

```
        while (True) {
            try {
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息,则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回客户端。

```
                $messages = $this->consumer->consumeMessage(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3 //` 长轮询时间3秒（最多可设置为`30`秒）。

```
                );
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\MessageNotExistException) {
```

`// Topic`中没有消息可消费，继续轮询。

```
                    printf("No message, contine long polling!RequestId:%s\n", $e->getReq
uestId());
                    continue;
                }
                print_r($e->getMessage() . "\n");
                sleep(3);
                continue;
            }
            print "consume finish, messages:\n";
```

`//` 处理业务逻辑。 消息队列

```
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
            }
```

// $message->getNextConsumeTime()前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
            print_r($receiptHandles);
            try {
                $this->consumer->ackMessage($receiptHandles);
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\AckMessageException) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
                    printf("Ack Error, RequestId:%s\n", $e->getRequestId());
                    foreach ($e->getAckMessageErrorItems() as $errorItem) {
                        printf("\tReceiptHandle:%s, ErrorCode:%s, ErrorMsg:%s\n", $error
Item->getReceiptHandle(), $errorItem->getErrorCode(), $errorItem->getErrorCode());
                    }
                }
            }
            print "ack finish\n";
        }
    }
} $instance = new ConsumerTest(); $instance->run();
```

?>

##### 收发事务消息

RocketMQ提供类似XA或Open XA的分布式事务功能，通过RocketMQ事务消息，能达到分布式事务的最

**背景信息**

事务消息的交互流程如下图所示。 消息队列更多信息，请参见事务消息。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送事务消息**

发送事务消息的示例代码如下。

```java
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; use MQ\MQClient; class ProducerTest {
    private $client;
    private $transProducer;
    private $count;
    private $popMsgCount;
    public function __construct()
    {
        $this->client = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${SECRET_KEY}"
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
        $topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
        $groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实消息队列例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        $instanceId = "${INSTANCE_ID}";
        $this->transProducer = $this->client->getTransProducer($instanceId,$topic,
$groupId);
        $this->count = 0;
        $this->popMsgCount = 0;
    }
    function processAckError($e) {
        if ($e instanceof MQ\Exception\AckMessageException) {
```

`//` 如果`Commit`或`Rollback`时超过了`TransCheckImmunityTime`（针对发送事务消息的句柄）或者超过`NextConsumeTime`（针对`consumeHalfMessage`的句柄），则`Commit`或`Rollback`会失败。

```
            printf("Commit/Rollback Error, RequestId:%s\n", $e->getRequestId());
            foreach ($e->getAckMessageErrorItems() as $errorItem) {
                printf("\tReceiptHandle:%s, ErrorCode:%s, ErrorMsg:%s\n", $errorItem->ge
tReceiptHandle(), $errorItem->getErrorCode(), $errorItem->getErrorCode());
            }
        } else {
            print_r($e);
        }
    }
    function consumeHalfMsg() {
        while($this->count < 3 && $this->popMsgCount < 15) {
            $this->popMsgCount++;
            try {
                $messages = $this->transProducer->consumeHalfMessage(4, 3);
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\MessageNotExistException) {
                    print "no half transaction message\n";
                    continue;
                }
                print_r($e->getMessage() . "\n");
                sleep(3);
                continue;
            }
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
```

$ $ 消息队列

```
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
                    }
                } catch (\Exception $e) {
                    processAckError($e);
                }
            }
        }
    }
    public function run()
    {
```

`//` 循环发送4条事务消息。

```
        for ($i = 0; $i < 4; $i++) {
            $pubMsg = new TopicMessage("hello,mq");
```

`//` 设置消息的自定义属性。

```
            $pubMsg->putProperty("a", $i);
```

`//` 设置消息的`Key`。

```
            $pubMsg->setMessageKey("MessageKey");
```

`//` 设置事务第一次回查的时间，为相对时间。单位：秒，范围：10~300。 `//` 第一次事务回查后如果消息没有`Commit`或者`Rollback`，则之后每隔`10s`左右会回查一次，共回查2 4小时。

```
            $pubMsg->setTransCheckImmunityTime(10);
            $topicMessage = $this->transProducer->publishMessage($pubMsg);
            print "\npublish -> \n\t" . $topicMessage->getMessageId() . " " .
$topicMessage->getReceiptHandle() . "\n";
            if ($i == 0) {
                try {
```

`//` 发送完事务消息后能获取到半消息句柄，可以直接`Commit`或`Rollback`事务消息。

```
                    $this->transProducer->commit($topicMessage->getReceiptHandle());
                    print "\n commit transaction msg when publish: " . $topicMessage->ge
tMessageId() . "\n";
                } catch (\Exception $e) {
```

`//` 如果`Commit`或`Rollback`时超过了`TransCheckImmunityTime`则会失败。

```
                    processAckError($e);
                }
            }
        }
```

`//`客户端需要有一个线程或者进程来消费没有确认的事务消息。 消息队列 `//` 客户端需要有一个线程或者进程来消费没有确认的事务消息。 `//` 检查没有确认的事务消息。

```
        $this->consumeHalfMsg();
    }
} $instance = new ProducerTest(); $instance->run();
```

?>

**订阅事务消息**

订阅事务消息的示例代码如下。

```java
<?php require "vendor/autoload.php"; use MQ\Model\TopicMessage; use MQ\MQClient; class ConsumerTest {
    private $client;
    private $producer;
    public function __construct()
    {
        $this->client = new MQClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${SECRET_KEY}"
        );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
        $topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
        $groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
        $instanceId = "${INSTANCE_ID}";
        $this->consumer = $this->client->getConsumer($instanceId, $topic, $groupId);
    }
    public function run()
    {
```

`//` 在当前线程循环消费消息，建议多开个几个线程并发消费消息。

```
while(True){
```

消息队列

```
        while (True) {
            try {
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息,则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回客户端。

```
                $messages = $this->consumer->consumeMessage(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3 //` 长轮询时间3秒（最多可设置为`30`秒）。

```
                );
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\MessageNotExistException) {
```

`// Topic`中没有消息可消费，继续轮询。

```
                    printf("No message, contine long polling!RequestId:%s\n", $e->getReq
uestId());
                    continue;
                }
                print_r($e->getMessage() . "\n");
                sleep(3);
                continue;
            }
            print "consume finish, messages:\n";
```

`//` 处理业务逻辑。

```
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
            }
```

// $message->getNextConsumeTime()前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
            print_r($receiptHandles);
            try {
                $this->consumer->ackMessage($receiptHandles);
            } catch (\Exception $e) {
                if ($e instanceof MQ\Exception\AckMessageException) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
                    printf("Ack Error, RequestId:%s\n", $e->getRequestId());
                    foreach ($e->getAckMessageErrorItems() as $errorItem) {
                        printf("\tReceiptHandle:%s, ErrorCode:%s, ErrorMsg:%s\n", $error
Item->getReceiptHandle(), $errorItem->getErrorCode(), $errorItem->getErrorCode());
                    }
                }
            }
            print "ack finish\n";
```

消息队列

```
        }
    }
} $instance = new ConsumerTest(); $instance->run();
```

?>

#### C# SDK

##### 准备环境

**环境要求**

安装.NET。更多信息，请参见安装.NET。 安装Visual Studio 2015或以上版本。更多信息，请参见安装Visual Studio。 安装完成后，您可以执行 `dotnet --version` 命令查看.NET Core版本。
1. 下载C# SDK及工程文件到本地并解压。其中Aliyun_MQ_SDK为SDK所在目
录，Aliyun_MQ_SDK.sln为工程文件。
2. 使用Visual Studio打开Aliyun_MQ_SDK.sln文件导入工程。
3. 执行Samples.cs文件。在Aliyun_MQ_SDK工程中可以看到Samples.cs文件，该文件中提供了C# SDK
消息收发的示例代码，将代码中的示例值替换为您实际业务使用的参数值，然后保存并执行。

##### 收发普通消息

普通消息是指RocketMQ中无特性的消息，区别于有特性的定时和延时消息、顺序消息和事务消息。本文提

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送普通消息**

发送普通消息的示例代码如下。

```
using System; using System.Collections.Generic; using System.Threading;
```

消息队列

```java
using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ.Util; namespace Aliyun.MQ.Sample {
    public class ProducerSample
    {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```java
        private const string _endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _secretAccessKey = "${SECRET_KEY}";
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```java
        private const string _topicName = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```java
        private const string _instanceId = "${INSTANCE_ID}";
        private static MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        static MQProducer producer = _client.GetProducer(_instanceId, _topicName);
        static void Main(string[] args)
        {
            try
            {
```

`//` 循环发送4条消息。

```
                for (int i = 0; i < 4; i++)
                {
    TopicMessage sendMsg;
```

`//` 消息内容。

```
                sendMsg = new TopicMessage("hello mq");
```

`//` 设置消息的自定义属性。

```
                sendMsg.PutProperty("a", i.ToString());
```

`//` 设置消息的`Key`。

```
                sendMsg.MessageKey = "MessageKey";
                TopicMessage result = producer.PublishMessage(sendMsg);
                Console.WriteLine("publis message success:" + result);
                }
            }
            catch (Exception ex)
            {
                Console.Write(ex);
            }
        }
    }
}
```

消息队列

**订阅普通消息**

订阅普通消息的示例代码如下。

```java
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ; namespace Aliyun.MQ.Sample {
    public class ConsumerSample
    {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```java
        private const string _endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _secretAccessKey = "${SECRET_KEY}";
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```java
        private const string _topicName = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```java
        private const string _instanceId = "${INSTANCE_ID}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```java
        private const string _groupId = "${GROUP_ID}";
        private static MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        static MQConsumer consumer = _client.GetConsumer(_instanceId, _topicName, _grou
pId, null);
        static void Main(string[] args)
        {
```

`//` 在当前线程循环消费消息，建议多开个几个线程并发消费消息。

```
            while (true)
            {
                try
                {
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息,则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回客户端。

```
                    List<Message> messages = null;
                    try
                    {
                        messages = consumer.ConsumeMessage(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3 //` 长轮询时间3秒（最多可设置为`30`秒）。

```
                        );
                    }
                    catch (Exception exp1)
```

消息队列 p p

```
                    {
                        if (exp1 is MessageNotExistException)
                        {
                            Console.WriteLine(Thread.CurrentThread.Name + " No new messa
ge, " + ((MessageNotExistException)exp1).RequestId);
                            continue;
                        }
                        Console.WriteLine(exp1);
                        Thread.Sleep(2000);
                    }
                    if (messages == null)
                    {
                        continue;
                    }
                    List<string> handlers = new List<string>();
                    Console.WriteLine(Thread.CurrentThread.Name + " Receive Messages:");
```

`//` 处理业务逻辑。

```
                    foreach (Message message in messages)
                    {
                        Console.WriteLine(message);
                        Console.WriteLine("Property a is:" + message.GetProperty("a"));
                        handlers.Add(message.ReceiptHandle);
                    }
```

`// Message.nextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
                    try
                    {
                        consumer.AckMessage(handlers);
                        Console.WriteLine("Ack message success:");
                        foreach (string handle in handlers)
                        {
                            Console.Write("\t" + handle);
                        }
                        Console.WriteLine();
                    }
                    catch (Exception exp2)
                    {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
                        if (exp2 is AckMessageException)
                        {
                            AckMessageException ackExp = (AckMessageException)exp2;
                            Console.WriteLine("Ack message fail, RequestId:" +
ackExp.RequestId);
                            foreach (AckMessageErrorItem errorItem in ackExp.ErrorItems)
                            {
                                Console.WriteLine("\tErrorHandle:" +
errorItem.ReceiptHandle + ",ErrorCode:" + errorItem.ErrorCode + ",ErrorMsg:" + errorIte m.ErrorMessage);
                            }
                        }
                    }
                }
```

消息队列

```
                catch (Exception ex)
                {
                    Console.WriteLine(ex);
                    Thread.Sleep(2000);
                }
            }
        }
    }
}
```

##### 收发顺序消息

顺序消息（FIFO消息）是RocketMQ提供的一种严格按照顺序来发布和消费的消息类型。本文提供使用

**背景信息**

顺序消息是RocketMQ提供的一种对消息发送和消费顺序有严格要求的消息。对于一个指定的Topic，消息严格按照先进先出（FIFO）的原则进行消息发布和消费，即先发布的消息先消费，后发布的消息后消费。 RocketMQ的顺序消息中，对于指定的一个Topic，所有消息根据Sharding Key进行区块分区，同一个分区内的消息按照严格的先进先出（FIFO）原则进行发布和消费。同一分区内的消息保证顺序，不同分区之间的消息顺序不做要求。因此RocketMQ的顺序消息也叫分区顺序消息。 更多信息，请参见顺序消息。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送顺序消息**

发送顺序消息的示例代码如下。

```java
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ.Util; namespace Aliyun.MQ.Sample {
    public class OrderProducerSample
    {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```java
        private const string _endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _secretAccessKey = "${SECRET_KEY}";
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```java
        private const string _topicName = "${TOPIC}";
```

所属的实例在控制台创建 `//` 消息队列 `// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```java
        private const string _instanceId = "${INSTANCE_ID}";
        private static MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        static MQProducer producer = _client.GetProducer(_instanceId, _topicName);
        static void Main(string[] args)
        {
            try
            {
```

`//` 循环发送8条消息。

```
                for (int i = 0; i < 8; i++)
                {
```

`//` 消息内容和消息的`tag`。

```
                    TopicMessage sendMsg = new TopicMessage("hello mq", "tag");
```

`//` 设置消息的自定义属性。

```
                    sendMsg.PutProperty("a", i.ToString());
```

`//` 设置分区顺序消息的`Sharding Key`，用于标识不同的分区。`Sharding Key`与消息的K `ey`是完全不同的概念。

```
                    sendMsg.ShardingKey = (i % 2).ToString();
                    TopicMessage result = producer.PublishMessage(sendMsg);
                    Console.WriteLine("publis message success:" + result);
                }
            }
            catch (Exception ex)
            {
                Console.Write(ex);
            }
        }
    }
}
```

**订阅顺序消息**

订阅顺序消息的示例代码如下。

```java
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ; namespace Aliyun.MQ.Sample {
    public class OrderConsumerSample
{
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```java
        private const string _endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
privateconststring accessKeyId="${ACCESSKEY}";
```

消息队列

```java
        private const string _accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _secretAccessKey = "${SECRET_KEY}";
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```java
        private const string _topicName = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```java
        private const string _groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```java
private const string _instanceId = "${INSTANCE_ID}";
        private static MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        static MQConsumer consumer = _client.GetConsumer(_instanceId, _topicName, _grou
pId, null);
        static void Main(string[] args)
        {
```

`//` 在当前线程循环消费消息，建议多开个几个线程并发消费消息。

```
            while (true)
            {
                try
                {
```

`//` 长轮询顺序消费消息, 拉取到的消息可能是多个分区的（对于分区顺序消息），一个分区内的消息一定是顺序的。 `//` 对于分区顺序消息，只要一个分区内存在没有被确认消费的消息，那么该分区下次还会消费到相同的消息。 `//` 对于一个分区，只有所有消息确认消费成功才能消费下一批消息。 `//` 长轮询表示如果`Topic`没有消息，则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则服务端立即返回响应。

```
                    List<Message> messages = null;
                    try
                    {
                        messages = consumer.ConsumeMessageOrderly(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3 //` 长轮询时间3秒（最多可设置为`30`秒）。

```
                        );
                    }
                    catch (Exception exp1)
                    {
                        if (exp1 is MessageNotExistException)
                        {
                            Console.WriteLine(Thread.CurrentThread.Name + " No new messa
ge, " + ((MessageNotExistException)exp1).RequestId);
                            continue;
                        }
                        Console.WriteLine(exp1);
                        Thread.Sleep(2000);
                    }
                    if (messages == null)
                    {
continue;
```

消息队列

```
                        continue;
                    }
                    List<string> handlers = new List<string>();
                    Console.WriteLine(Thread.CurrentThread.Name + " Receive Messages:");
```

`//` 处理业务逻辑。

```
                    foreach (Message message in messages)
                    {
                        Console.WriteLine(message);
                        Console.WriteLine("Property a is:" + message.GetProperty("a"));
                        handlers.Add(message.ReceiptHandle);
                    }
```

`// Message.nextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
                    try
                    {
                        consumer.AckMessage(handlers);
                        Console.WriteLine("Ack message success:");
                        foreach (string handle in handlers)
                        {
                            Console.Write("\t" + handle);
                        }
                        Console.WriteLine();
                    }
                    catch (Exception exp2)
                    {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
                        if (exp2 is AckMessageException)
                        {
                            AckMessageException ackExp = (AckMessageException)exp2;
                            Console.WriteLine("Ack message fail, RequestId:" +
ackExp.RequestId);
                            foreach (AckMessageErrorItem errorItem in ackExp.ErrorItems)
                            {
                                Console.WriteLine("\tErrorHandle:" +
errorItem.ReceiptHandle + ",ErrorCode:" + errorItem.ErrorCode + ",ErrorMsg:" + errorIte m.ErrorMessage);
                            }
                        }
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex);
                    Thread.Sleep(2000);
                }
            }
        }
    }
}
```

消息队列

##### 收发定时消息和延时消息

**背景信息**

延时消息：Producer将消息发送到RocketMQRocketMQ服务端，但并不期望立马投递这条消息，而是延迟一定时间后才投递到Consumer进行消费，该消息即延时消息。 定时消息：Producer将消息发送到RocketMQ服务端，但并不期望立马投递这条消息，而是推迟到在当前时间点之后的某一个时间投递到Consumer进行消费，该消息即定时消息。 在HTTP协议下，定时消息和延时消息的代码配置相同，本质都是根据消息中的属性延迟固定时间后才投递给消费者。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送定时消息或延时消息**

发送定时消息或延时消息的示例代码如下。

```java
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ.Util; namespace Aliyun.MQ.Sample {
    public class ProducerSample
    {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```java
        private const string _endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _secretAccessKey = "${SECRET_KEY}";
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```java
        private const string _topicName = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```java
        private const string _instanceId = "${INSTANCE_ID}";
        private static MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        static MQProducer producer = _client.GetProducer(_instanceId, _topicName);
staticvoidMain(string[]args)
```

消息队列

```
        static void Main(string[] args)
        {
            try
            {
```

`//` 循环发送4条消息。

```
                for (int i = 0; i < 4; i++)
                {
                    TopicMessage sendMsg;
```

`//` 消息内容。

```
                    sendMsg = new TopicMessage("hello mq");
```

`//` 设置消息的自定义属性。

```
                    sendMsg.PutProperty("a", i.ToString());
```

`//` 延时消息，发送时间为`10s`后。该参数格式为毫秒级别的时间戳。 `//` 若发送定时消息，设置该参数时需要计算定时时间与当前时间的时间差。

```
                    sendMsg.StartDeliverTime = AliyunSDKUtils.GetNowTimeStamp() + 10 * 1
000;
                    TopicMessage result = producer.PublishMessage(sendMsg);
                    Console.WriteLine("publis message success:" + result);
                }
            }
            catch (Exception ex)
            {
                Console.Write(ex);
            }
        }
    }
}
```

**订阅定时消息或延时消息**

订阅定时消息或延时消息的示例代码如下。

```java
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ; namespace Aliyun.MQ.Sample {
    public class ConsumerSample
    {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```java
        private const string _endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _secretAccessKey = "${SECRET_KEY}";
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```java
        private const string _topicName = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实消息队列例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```java
        private const string _instanceId = "${INSTANCE_ID}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```java
        private const string _groupId = "${GROUP_ID}";
        private static MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        static MQConsumer consumer = _client.GetConsumer(_instanceId, _topicName, _grou
pId, null);
        static void Main(string[] args)
        {
```

`//` 在当前线程循环消费消息，建议多开个几个线程并发消费消息。

```
            while (true)
            {
                try
                {
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息,则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回客户端。

```
                    List<Message> messages = null;
                    try
                    {
                        messages = consumer.ConsumeMessage(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3 //` 长轮询时间3秒（最多可设置为`30`秒）。

```
                        );
                    }
                    catch (Exception exp1)
                    {
                        if (exp1 is MessageNotExistException)
                        {
                            Console.WriteLine(Thread.CurrentThread.Name + " No new messa
ge, " + ((MessageNotExistException)exp1).RequestId);
                            continue;
                        }
                        Console.WriteLine(exp1);
                        Thread.Sleep(2000);
                    }
                    if (messages == null)
                    {
                        continue;
                    }
                    List<string> handlers = new List<string>();
                    Console.WriteLine(Thread.CurrentThread.Name + " Receive Messages:");
```

`//` 处理业务逻辑。

```
                    foreach (Message message in messages)
                    {
                        Console.WriteLine(message);
                        Console.WriteLine("Property a is:" + message.GetProperty("a"));
                        handlers.Add(message.ReceiptHandle);
```

消息队列

```
                    }
```

`// Message.nextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
                    try
                    {
                        consumer.AckMessage(handlers);
                        Console.WriteLine("Ack message success:");
                        foreach (string handle in handlers)
                        {
                            Console.Write("\t" + handle);
                        }
                        Console.WriteLine();
                    }
                    catch (Exception exp2)
                    {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
                        if (exp2 is AckMessageException)
                        {
                            AckMessageException ackExp = (AckMessageException)exp2;
                            Console.WriteLine("Ack message fail, RequestId:" +
ackExp.RequestId);
                            foreach (AckMessageErrorItem errorItem in ackExp.ErrorItems)
                            {
                                Console.WriteLine("\tErrorHandle:" +
errorItem.ReceiptHandle + ",ErrorCode:" + errorItem.ErrorCode + ",ErrorMsg:" + errorIte m.ErrorMessage);
                            }
                        }
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex);
                    Thread.Sleep(2000);
                }
            }
        }
    }
}
```

##### 收发事务消息

RocketMQ提供类似XA或Open XA的分布式事务功能，通过RocketMQ事务消息，能达到分布式事务的最

**背景信息**

事务消息的交互流程如下图所示。 消息队列更多信息，请参见事务消息。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送事务消息**

发送事务消息的示例代码如下。

```java
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ.Util; namespace Aliyun.MQ.Sample {
    public class TransProducerSample
    {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```java
        private const string _endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _secretAccessKey = "${SECRET_KEY}";
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```java
        private const string _topicName = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```java
        private const string _instanceId = "${INSTANCE_ID}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```java
        private const string _groupId = "${GROUP_ID}";
        private static readonly MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        private static readonly MQTransProducer transProducer =
_client.GetTransProdcuer(_instanceId, _topicName, _groupId);
```

消息队列

```
        static void ProcessAckError(Exception exception)
        {
```

`//` 如果`Commit`或`Rollback`时超过了`TransCheckImmunityTime`（针对发送事务消息的句柄）或者超过`10s`（针对`consumeHalfMessage`的句柄），则`Commit`或`Rollback`会失败。

```
            if (exception is AckMessageException)
            {
                AckMessageException ackExp = (AckMessageException)exception;
                Console.WriteLine("Ack message fail, RequestId:" + ackExp.RequestId);
                foreach (AckMessageErrorItem errorItem in ackExp.ErrorItems)
                {
                    Console.WriteLine("\tErrorHandle:" + errorItem.ReceiptHandle + ",Err
orCode:" + errorItem.ErrorCode + ",ErrorMsg:" + errorItem.ErrorMessage);
                }
            }
        }
        static void ConsumeHalfMessage()
        {
            int count = 0;
            while (true)
            {
                if (count == 3)
                    break;
                try
                {
```

`//` 检查事务半消息，类似消费普通消息。

```
                    List<Message> messages = null;
                    try
                    {
                        messages = transProducer.ConsumeHalfMessage(3, 3);
                    } catch (Exception exp1) {
                        if (exp1 is MessageNotExistException)
                        {
                            Console.WriteLine(Thread.CurrentThread.Name + " No half mess
age, " + ((MessageNotExistException)exp1).RequestId);
                            continue;
                        }
                        Console.WriteLine(exp1);
                        Thread.Sleep(2000);
                    }
                    if (messages == null)
                        continue;
```

`//` 处理业务逻辑。

```
                    foreach (Message message in messages)
                    {
                        Console.WriteLine(message);
                        int a = int.Parse(message.GetProperty("a"));
                        uint consumeTimes = message.ConsumedTimes;
                        try {
                            if (a == 1) {
```

`//` 确认提交事务消息。

```
                                transProducer.Commit(message.ReceiptHandle);
```

消息队列

```
                                count++;
                                Console.WriteLine("Id:" + message.Id + ", commit");
                            } else if (a == 2 && consumeTimes > 1) {
```

`//` 确认提交事务消息。

```
                                transProducer.Commit(message.ReceiptHandle);
                                count++;
                                Console.WriteLine("Id:" + message.Id + ", commit");
                            } else if (a == 3) {
```

`//` 确认回滚事务消息。

```
                                transProducer.Rollback(message.ReceiptHandle);
                                count++;
                                Console.WriteLine("Id:" + message.Id + ", rollback");
                            } else {
```

`//` 什么都不做，下次再检查。

```
                                Console.WriteLine("Id:" + message.Id + ", unkonwn");
                            }
                        } catch (Exception ackError) {
                            ProcessAckError(ackError);
                        }
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex);
                    Thread.Sleep(2000);
                }
            }
        }
        static void Main(string[] args)
        {
```

`//` 客户端需要有一个线程或者进程来消费没有确认的事务消息。 `//` 启动一个线程来检查没有确认的事务消息。

```
            Thread consumeHalfThread = new Thread(ConsumeHalfMessage);
            consumeHalfThread.Start();
            try
            {
```

`//` 循环发送4条事务消息，第一条直接在发送完提交事务, 其它三条根据条件处理。

```
                for (int i = 0; i < 4; i++)
                {
                    TopicMessage sendMsg = new TopicMessage("trans_msg");
                    sendMsg.MessageTag = "a";
                    sendMsg.MessageKey = "MessageKey";
                    sendMsg.PutProperty("a", i.ToString());
```

`//` 设置事务第一次回查的时间，为相对时间。单位：秒，范围：10~300。 `//` 第一次事务回查后如果消息没有`Commit`或者`Rollback`，则之后每隔`10s`左右会回查一次 ，共回查`24`小时。

```
                    sendMsg.TransCheckImmunityTime = 10;
                    TopicMessage result = transProducer.PublishMessage(sendMsg);
                    Console.WriteLine("publis message success:" + result);
                    try {
                        if (!string.IsNullOrEmpty(result.ReceiptHandle) && i == 0)
{
```

消息队列

```
                        {
```

`//` 发送完事务消息后能获取到半消息句柄，可以直接`Commit`或`Rollback`事务消息。

```
                            transProducer.Commit(result.ReceiptHandle);
                            Console.WriteLine("Id:" + result.Id + ", commit");
                        }
                    } catch (Exception ackError) {
                        ProcessAckError(ackError);
                    }
                }
            } catch (Exception ex) {
                Console.Write(ex);
            }
            consumeHalfThread.Join();
        }
    }
}
```

**订阅事务消息**

订阅事务消息的示例代码如下。

```java
using System; using System.Collections.Generic; using System.Threading; using Aliyun.MQ.Model; using Aliyun.MQ.Model.Exp; using Aliyun.MQ; namespace Aliyun.MQ.Sample {
    public class ConsumerSample
    {
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```java
        private const string _endpoint = "${HTTP_ENDPOINT}";
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _accessKeyId = "${ACCESS_KEY}";
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```java
        private const string _secretAccessKey = "${SECRET_KEY}";
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```java
        private const string _topicName = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```java
        private const string _instanceId = "${INSTANCE_ID}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```java
        private const string _groupId = "${GROUP_ID}";
        private static MQClient _client = new Aliyun.MQ.MQClient(_accessKeyId,
_secretAccessKey, _endpoint);
        static MQConsumer consumer = _client.GetConsumer(_instanceId, _topicName, _grou
pId, null); staticvoidMain(string[]args)
```

消息队列

```
        static void Main(string[] args)
        {
```

`//` 在当前线程循环消费消息，建议多开个几个线程并发消费消息。

```
            while (true)
            {
                try
                {
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息,则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回客户端。

```
                    List<Message> messages = null;
                    try
                    {
                        messages = consumer.ConsumeMessage(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3 //` 长轮询时间3秒（最多可设置为`30`秒）。

```
                        );
                    }
                    catch (Exception exp1)
                    {
                        if (exp1 is MessageNotExistException)
                        {
                            Console.WriteLine(Thread.CurrentThread.Name + " No new messa
ge, " + ((MessageNotExistException)exp1).RequestId);
                            continue;
                        }
                        Console.WriteLine(exp1);
                        Thread.Sleep(2000);
                    }
                    if (messages == null)
                    {
                        continue;
                    }
                    List<string> handlers = new List<string>();
                    Console.WriteLine(Thread.CurrentThread.Name + " Receive Messages:");
```

`//` 处理业务逻辑。

```
                    foreach (Message message in messages)
                    {
                        Console.WriteLine(message);
                        Console.WriteLine("Property a is:" + message.GetProperty("a"));
                        handlers.Add(message.ReceiptHandle);
                    }
```

`// Message.nextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
                    try
                    {
                        consumer.AckMessage(handlers);
                        Console.WriteLine("Ack message success:");
                        foreach (string handle in handlers)
                        {
                            Console.Write("\t" + handle);
                        }
```

消息队列

```
                        Console.WriteLine();
                    }
                    catch (Exception exp2)
                    {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
                        if (exp2 is AckMessageException)
                        {
                            AckMessageException ackExp = (AckMessageException)exp2;
                            Console.WriteLine("Ack message fail, RequestId:" +
ackExp.RequestId);
                            foreach (AckMessageErrorItem errorItem in ackExp.ErrorItems)
                            {
                                Console.WriteLine("\tErrorHandle:" +
errorItem.ReceiptHandle + ",ErrorCode:" + errorItem.ErrorCode + ",ErrorMsg:" + errorIte m.ErrorMessage);
                            }
                        }
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex);
                    Thread.Sleep(2000);
                }
            }
        }
    }
}
```

#### C++ SDK

##### 准备环境

**环境要求**

安装SCons。更多信息，请参见安装SCons。 使用SCons，需要先安装Python 3.5或以上版本。更多信息，请参见安装Python。 安装Visual Studio 2015或以上版本。更多信息，请参见安装Visual Studio。 仅Windows系统需要安装Visual Studio，本文环境配置以Visual Studio 2019为例。

**说明**

1. 下载SDK到本地并解压。SDK下载链接，请参见SDK概述。
2. 在下载的SDK目录下，执行以下命令编译项目。

```
scons
```

3. 编译成功后，将SDK目录下的include和lib文件夹复制到您本地创建的C++项目目录下。
4. 在Visual Studio设置项目属性。右键单击项目，选择**属性**。
消息队列

**设置附加包含目录**

在项目属性页中，选择**配置属性** **> C/C++ >** **常规** > **附加包含目录**，将**附加包含目录**设置为步骤3中复制后的include文件夹路径。

**设置附加库目录**

在项目属性页中，选择**配置属性** > **链接器** > **常规** > **附加库目录**，将**附加库目录**设置为步骤3中复制后的lib文件夹路径，以及lib\windows\ {平台目录}文件夹路径。其中， {平台目录}根据您使用的操作系统选择，64位操作系统选择AMD64，32位操作系统选择I386。

**设置附加依赖项**

在项目属性页中，选择**配置属性** > **链接器** > **输入** > **附加依赖项**，将以下内容添加到**附加依赖项**中。 消息队列

```
mqcpp.lib libcurl.lib libcurl_debug.lib libeay32MT.lib libeay32MTd.lib ssleay32MT.lib ssleay32MTd.lib DbgHelp.lib User32.lib GDI32.lib Advapi32.lib
```

5. 将示例代码复制到项目文件中，并按照注释修改参数并保存。示例代码下载路径，请参见示例代码。
6. 单击
按钮开始编译。 以下操作以CentOS系统为例。

**说明**

1. 下载SDK到本地并解压。SDK下载链接，请参见SDK概述。
2. 分别执行以下命令安装 `libcurl-devel` 和 `openssl-devel` 库。

```bash
yum install libcurl-devel yum install openssl-devel
```

3. 在下载的SDK目录下，执行以下命令编译项目。

```
scons
```

4. 编译成功后，将SDK目录下的include和lib文件夹复制到您本地创建的C++项目目录下。
5. 将示例代码复制到您本地的项目文件中，并按照注释修改参数并保存。示例代码下载路径，请参见示例代
码。
6. 执行以下命令进行编译。
消息队列
# producer.cpp替换为您本地创建的项目文件名称。

```
g++ producer.cpp -o producer lib/libmqcpp.a -I include/ -lcurl -lcrypto
```

##### 收发普通消息

普通消息是指RocketMQ中无特性的消息，区别于有特性的定时和延时消息、顺序消息和事务消息。本文提

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送普通消息**

发送普通消息的示例代码如下。

```
#include <fstream>
#include <time.h>
#include "mq_http_sdk/mq_client.h"
using namespace std; using namespace mq::http::sdk; int main() {
    MQClient mqClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${SECRET_KEY}"
            );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
    string topic = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    string instanceId = "${INSTANCE_ID}";
    MQProducerPtr producer;
    if (instanceId == "") {
        producer = mqClient.getProducerRef(topic);
    } else {
        producer = mqClient.getProducerRef(instanceId, topic);
    }
    try {
```

`//` 循环发送4条消息。

```
for(inti i<4 i++)
```

消息队列

```
        for (int i = 0; i < 4; i++)
        {
            PublishMessageResponse pmResp;
```

`//` 消息内容。

```
            TopicMessage pubMsg("Hello, mq!have key!");
```

`//` 设置消息的自定义属性。

```
            pubMsg.putProperty("a",std::to_string(i));
```

`//` 设置消息的`Key`。

```
            pubMsg.setMessageKey("MessageKey" + std::to_string(i));
            producer->publishMessage(pubMsg, pmResp);
            cout << "Publish mq message success. Topic is: " << topic
                << ", msgId is:" << pmResp.getMessageId()
                << ", bodyMD5 is:" << pmResp.getMessageBodyMD5() << endl;
        }
    } catch (MQServerException& me) {
        cout << "Request Failed: " + me.GetErrorCode() << ", requestId is:" <<
me.GetRequestId() << endl;
        return -1;
    } catch (MQExceptionBase& mb) {
        cout << "Request Failed: " + mb.ToString() << endl;
        return -2;
    }
    return 0;
}
```

**订阅普通消息**

订阅普通消息的示例代码如下。

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
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
"${SECRETKEY}"
```

消息队列

```
            ${SECRET_KEY}
            );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
    string topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
    string groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    string instanceId = "${INSTANCE_ID}";
    MQConsumerPtr consumer;
    if (instanceId == "") {
        consumer = mqClient.getConsumerRef(topic, groupId);
    } else {
        consumer = mqClient.getConsumerRef(instanceId, topic, groupId, "");
    }
    do {
        try {
            std::vector<Message> messages;
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息,则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回客户端。

```
            consumer->consumeMessage(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3, //` 长轮询时间3秒（最多可设置为`30`秒）。

```
                    messages
            );
            cout << "Consume: " << messages.size() << " Messages!" << endl;
```

`//` 处理业务逻辑。

```
            std::vector<std::string> receiptHandles;
            for (std::vector<Message>::iterator iter = messages.begin();
                    iter != messages.end(); ++iter)
            {
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
            }
```

`//` 确认消息消费成功。 `// Message.NextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
            AckMessageResponse bdmResp;
            consumer->ackMessage(receiptHandles, bdmResp);
            if (!bdmResp.isSuccess()) {
```

消息队列 p `//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
                const std::vector<AckMessageFailedItem>& failedItems =
                    bdmResp.getAckMessageFailedItem();
                for (std::vector<AckMessageFailedItem>::const_iterator iter = failedItem
s.begin();
                        iter != failedItems.end(); ++iter)
                {
                    cout << "AckFailedItem: " << iter->errorCode
                        << "  " << iter->receiptHandle << endl;
                }
            } else {
                cout << "Ack: " << messages.size() << " messages suc!" << endl;
            }
        } catch (MQServerException& me) {
            if (me.GetErrorCode() == "MessageNotExist") {
                cout << "No message to consume! RequestId: " + me.GetRequestId() << endl
;
                continue;
            }
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
        }
    } while(true);
}
```

##### 收发顺序消息

顺序消息（FIFO消息）是RocketMQ提供的一种严格按照顺序来发布和消费的消息类型。本文提供使用

**背景信息**

顺序消息是RocketMQ提供的一种对消息发送和消费顺序有严格要求的消息。对于一个指定的Topic，消息严格按照先进先出（FIFO）的原则进行消息发布和消费，即先发布的消息先消费，后发布的消息后消费。 RocketMQ的顺序消息中，对于指定的一个Topic，所有消息根据Sharding Key进行区块分区，同一个分区内的消息按照严格的先进先出（FIFO）原则进行发布和消费。同一分区内的消息保证顺序，不同分区之间的消息顺序不做要求。因此RocketMQ的顺序消息也叫分区顺序消息。 更多信息，请参见顺序消息。

**前提条件**

消息队列您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。

**发送顺序消息**

发送顺序消息的示例代码如下。

```
//#include <iostream>
#include <fstream>
#include <time.h>
#include "mq_http_sdk/mq_client.h"
using namespace std; using namespace mq::http::sdk; int main() {
    MQClient mqClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${SECRET_KEY}"
            );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
    string topic = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    string instanceId = "${INSTANCE_ID}";
    MQProducerPtr producer;
    if (instanceId == "") {
        producer = mqClient.getProducerRef(topic);
    } else {
        producer = mqClient.getProducerRef(instanceId, topic);
    }
    try {
```

`//` 循环发送4条消息。

```
        for (int i = 0; i < 8; i++)
        {
            PublishMessageResponse pmResp;
```

`//` 消息内容。

```
            TopicMessage pubMsg("Hello, mq!order msg!");
```

`//` 设置分区顺序消息的`Sharding Key`，用于标识不同的分区。`Sharding Key`与消息的`Key`是完全不同的概念。

```
            pubMsg.setShardingKey(std::to_string(i % 2));
```

`//` 设置消息的自定义属性。

```
pubMsg.putProperty("a",std::tostring(i));
```

消息队列

```
pubsg.put opety(a,std::to_st g());
            producer->publishMessage(pubMsg, pmResp);
            cout << "Publish mq message success. Topic is: " << topic
                << ", msgId is:" << pmResp.getMessageId()
                << ", bodyMD5 is:" << pmResp.getMessageBodyMD5() << endl;
        }
    } catch (MQServerException& me) {
        cout << "Request Failed: " + me.GetErrorCode() << ", requestId is:" <<
me.GetRequestId() << endl;
        return -1;
    } catch (MQExceptionBase& mb) {
        cout << "Request Failed: " + mb.ToString() << endl;
        return -2;
    }
    return 0;
}
```

**订阅顺序消息**

订阅顺序消息的示例代码如下。

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
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${SECRET_KEY}"
            );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
    string topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
    string groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    string instanceId = "${INSTANCE_ID}";
```

消息队列

```
    MQConsumerPtr consumer;
    if (instanceId == "") {
        consumer = mqClient.getConsumerRef(topic, groupId);
    } else {
        consumer = mqClient.getConsumerRef(instanceId, topic, groupId, "");
    }
    do {
        try {
            std::vector<Message> messages;
```

`//` 长轮询顺序消费消息, 拉取到的消息可能是多个分区的（对于分区顺序消息），一个分区内的消息一定是顺序的。 `//` 对于分区顺序消息，只要一个分区内存在没有被确认消费的消息，那么该分区下次还会消费到相同的消息。 `//` 对于一个分区，只有所有消息确认消费成功才能消费下一批消息。 `//` 长轮询表示如果`Topic`没有消息，则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则服务端立即返回响应。

```
            consumer->consumeMessageOrderly(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3, //` 长轮询时间3秒（最多可设置为`30`秒）。

```
                    messages
            );
            cout << "Consume: " << messages.size() << " Messages!" << endl;
```

`//` 处理业务逻辑。

```
            std::vector<std::string> receiptHandles;
            for (std::vector<Message>::iterator iter = messages.begin();
                    iter != messages.end(); ++iter)
            {
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
            }
```

`//` 确认消息消费成功。 `// Message.NextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
            AckMessageResponse bdmResp;
            consumer->ackMessage(receiptHandles, bdmResp);
            if (!bdmResp.isSuccess()) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
                const std::vector<AckMessageFailedItem>& failedItems =
                    bdmResp.getAckMessageFailedItem();
                for (std::vector<AckMessageFailedItem>::const_iterator iter = failedItem
s.begin();
                        iter != failedItems.end(); ++iter)
```

消息队列

```
                {
                    cout << "AckFailedItem: " << iter->errorCode
                        << "  " << iter->receiptHandle << endl;
                }
            } else {
                cout << "Ack: " << messages.size() << " messages suc!" << endl;
            }
        } catch (MQServerException& me) {
            if (me.GetErrorCode() == "MessageNotExist") {
                cout << "No message to consume! RequestId: " + me.GetRequestId() << endl
;
                continue;
            }
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
        }
    } while(true);
}
```

##### 收发定时消息和延时消息

**背景信息**

延时消息：Producer将消息发送到RocketMQRocketMQ服务端，但并不期望立马投递这条消息，而是延迟一定时间后才投递到Consumer进行消费，该消息即延时消息。 定时消息：Producer将消息发送到RocketMQ服务端，但并不期望立马投递这条消息，而是推迟到在当前时间点之后的某一个时间投递到Consumer进行消费，该消息即定时消息。 在HTTP协议下，定时消息和延时消息的代码配置相同，本质都是根据消息中的属性延迟固定时间后才投递给消费者。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。 消息队列

**发送定时消息或延时消息**

发送定时消息或延时消息的示例代码如下。

```
#include <fstream>
#include <time.h>
#include "mq_http_sdk/mq_client.h"
using namespace std; using namespace mq::http::sdk; int main() {
    MQClient mqClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在阿里云`RAM`控制台创建。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在阿里云`RAM`控制台创建。

```
            "${SECRET_KEY}"
            );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
    string topic = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    string instanceId = "${INSTANCE_ID}";
    MQProducerPtr producer;
    if (instanceId == "") {
        producer = mqClient.getProducerRef(topic);
    } else {
        producer = mqClient.getProducerRef(instanceId, topic);
    }
    try {
```

`//` 循环发送4条消息。

```
        for (int i = 0; i < 4; i++)
        {
            PublishMessageResponse pmResp;
```

`//` 消息内容。

```
            TopicMessage pubMsg("Hello, mq!have key!");
```

`//` 设置消息的自定义属性。

```
            pubMsg.putProperty("a",std::to_string(i));
```

`//` 设置消息的`Key`。

```
            pubMsg.setMessageKey("MessageKey" + std::to_string(i));
```

`//` 延时消息，发送时间为`10s`后。该参数格式为毫秒级别的时间戳。 `//` 若发送定时消息，设置该参数时需要计算定时时间与当前时间的时间差。

```
            pubMsg.setStartDeliverTime(time(NULL) * 1000 + 10 * 1000);
            producer->publishMessage(pubMsg, pmResp);
            cout << "Publish mq message success. Topic is: " << topic
                << ", msgId is:" << pmResp.getMessageId()
```

消息队列 , g p pg g

```
                << ", bodyMD5 is:" << pmResp.getMessageBodyMD5() << endl;
        }
    } catch (MQServerException& me) {
        cout << "Request Failed: " + me.GetErrorCode() << ", requestId is:" <<
me.GetRequestId() << endl;
        return -1;
    } catch (MQExceptionBase& mb) {
        cout << "Request Failed: " + mb.ToString() << endl;
        return -2;
    }
    return 0;
}
```

**订阅定时消息或延时消息**

订阅定时消息或延时消息的示例代码如下。

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
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${SECRET_KEY}"
            );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
    string topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
    string groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    string instanceId = "${INSTANCE_ID}";
    MQConsumerPtr consumer;
    if (instanceId == "") {
```

消息队列

```
        consumer = mqClient.getConsumerRef(topic, groupId);
    } else {
        consumer = mqClient.getConsumerRef(instanceId, topic, groupId, "");
    }
    do {
        try {
            std::vector<Message> messages;
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息,则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回客户端。

```
            consumer->consumeMessage(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3, //` 长轮询时间3秒（最多可设置为`30`秒）。

```
                    messages
            );
            cout << "Consume: " << messages.size() << " Messages!" << endl;
```

`//` 处理业务逻辑。

```
            std::vector<std::string> receiptHandles;
            for (std::vector<Message>::iterator iter = messages.begin();
                    iter != messages.end(); ++iter)
            {
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
            }
```

`//` 确认消息消费成功。 `// Message.NextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
            AckMessageResponse bdmResp;
            consumer->ackMessage(receiptHandles, bdmResp);
            if (!bdmResp.isSuccess()) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
                const std::vector<AckMessageFailedItem>& failedItems =
                    bdmResp.getAckMessageFailedItem();
                for (std::vector<AckMessageFailedItem>::const_iterator iter = failedItem
s.begin();
                        iter != failedItems.end(); ++iter)
                {
                    cout << "AckFailedItem: " << iter->errorCode
                        << "  " << iter->receiptHandle << endl;
                }
            } else {
                cout << "Ack: " << messages.size() << " messages suc!" << endl;
            }
```

消息队列

```
        } catch (MQServerException& me) {
            if (me.GetErrorCode() == "MessageNotExist") {
                cout << "No message to consume! RequestId: " + me.GetRequestId() << endl
;
                continue;
            }
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
        }
    } while(true);
}
```

##### 收发事务消息

RocketMQ提供类似XA或Open XA的分布式事务功能，通过RocketMQ事务消息，能达到分布式事务的最

**背景信息**

事务消息的交互流程如下图所示。 更多信息，请参见事务消息。

**前提条件**

您已完成以下操作： 创建资源。代码中涉及的资源信息，例如实例、Topic和Group ID等，需要在控制台上提前创建。更多信息，请参见创建资源。 消息队列

**发送事务消息**

发送事务消息的示例代码如下。

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
using namespace std; using namespace mq::http::sdk; const int32_t pubMsgCount = 4; const int32_t halfCheckCount = 3; void processCommitRollError(AckMessageResponse& bdmResp, const std::string& messageId) {
    if (bdmResp.isSuccess()) {
        cout << "Commit/Roll Transaction Suc: " << messageId << endl;
        return;
    }
    const std::vector<AckMessageFailedItem>& failedItems =
        bdmResp.getAckMessageFailedItem();
    for (std::vector<AckMessageFailedItem>::const_iterator iter = failedItems.begin();
            iter != failedItems.end(); ++iter)
    {
        cout << "Commit/Roll Transaction ERROR: " << iter->errorCode
            << "  " << iter->receiptHandle << endl;
    }
}
#ifdef WIN32
unsigned __stdcall consumeHalfMessageThread(void *arg)
#else
void* consumeHalfMessageThread(void *arg)
#endif
{
    MQTransProducerPtr transProducer = *(MQTransProducerPtr*)(arg);
    int count = 0;
    do {
        std::vector<Message> halfMsgs;
        try {
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息,则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回客户端。

```
            transProducer->consumeHalfMessage(
```

`1, //` 一次最多消费1条（最多可设置为`16`条）。 `3, //` 长轮询时间3秒（最多可设置为`30`秒）。

```
                    halfMsgs
```

消息队列 g

```
                    );
        } catch (MQServerException& me) {
            if (me.GetErrorCode() == "MessageNotExist") {
                cout << "No half message to consume! RequestId: " + me.GetRequestId() <<
endl;
                continue;
            }
            cout << "Request Failed: " + me.GetErrorCode() + ".RequestId: " +
me.GetRequestId() << endl;
        }
        if (halfMsgs.size() == 0) {
            continue;
        }
        cout << "Consume Half: " << halfMsgs.size() << " Messages!" << endl;
```

`//` 处理事务半消息。

```
        std::vector<std::string> receiptHandles;
        for (std::vector<Message>::iterator iter = halfMsgs.begin();
                iter != halfMsgs.end(); ++iter)
        {
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
                }
            } else if(propA == "3") {
                cout << "Rollback msg.." << endl;
                transProducer->rollback(handle, bdmResp);
                count++;
            } else {
                transProducer->commit(handle, bdmResp);
                cout << "Unkown msg.." << endl;
            }
```

消息队列 `//` 如果`Commit`或`Rollback`时超过了`NextConsumeTime`的时间，则`Commit`或`Rollback`会失败。

```
            processCommitRollError(bdmResp, iter->getMessageId());
        }
    } while(count < halfCheckCount);
#ifdef WIN32
    return 0;
#else
    return NULL;
#endif
} int main() {
    MQClient mqClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${SECRET_KEY}"
            );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
    string topic = "${TOPIC}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    string instanceId = "${INSTANCE_ID}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
    string groupId = "${GROUP_ID}";
    MQTransProducerPtr transProducer;
    if (instanceId == "") {
        transProducer = mqClient.getTransProducerRef(topic, groupId);
    } else {
        transProducer = mqClient.getTransProducerRef(instanceId, topic, groupId);
    }
```

`//` 客户端需要有一个线程或者进程来消费没有确认的事务消息。 `//` 启动一个线程来检查没有确认的事务消息。

```
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
```

消息队列

```
        for (int i = 0; i < pubMsgCount; i++)
        {
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
```

`//` 发送完事务消息后能获取到半消息句柄，可以直接`Commit`或`Rollback`事务消息。 `//` 如果`Commit`或`Rollback`时超过了`TransCheckImmunityTime`的时间，则`Commit`或`Rollb` `ack`会失败。

```
                AckMessageResponse bdmResp;
                transProducer->commit(pmResp.getReceiptHandle(), bdmResp);
                processCommitRollError(bdmResp, pmResp.getMessageId());
            }
        }
    } catch (MQServerException& me) {
        cout << "Request Failed: " + me.GetErrorCode() << ", requestId is:" <<
me.GetRequestId() << endl;
    } catch (MQExceptionBase& mb) {
        cout << "Request Failed: " + mb.ToString() << endl;
    }
#ifdef WIN32
    WaitForSingleObject(thread, INFINITE);
    CloseHandle(thread);
#else
    pthread_join(thread, NULL);
#endif
    return 0;
}
```

**订阅事务消息**

订阅事务消息的示例代码如下。

```
#include <vector>
#include <fstream>
#include "mq_http_sdk/mq_client.h"
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif
using namespace std;
```

i

```
htt
```

`dk` 消息队列

```
using namespace mq::http::sdk; int main() {
    MQClient mqClient(
```

`//` 设置`HTTP`协议客户端接入点，进入`RocketMQ`控制台实例详情页面的网络管理页签查看。

```
            "${HTTP_ENDPOINT}",
```

`// AccessKey ID`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${ACCESS_KEY}",
```

`// AccessKey Secret`阿里云身份验证，在`Apsara Uni-manager`运营控制台获取。

```
            "${SECRET_KEY}"
            );
```

`//` 消息所属的`Topic`，在`RocketMQ`控制台创建。

```
    string topic = "${TOPIC}";
```

`//` 您在`RocketMQ`控制台创建的`Group ID`。

```
    string groupId = "${GROUP_ID}";
```

`// Topic`所属的实例`ID`，在`RocketMQ`控制台创建。 `//` 若实例有命名空间，则实例`ID`必须传入；若实例无命名空间，则实例`ID`传入`null`空值或字符串空值。实例的命名空间可以在`RocketMQ`控制台的实例详情页面查看。

```
    string instanceId = "${INSTANCE_ID}";
    MQConsumerPtr consumer;
    if (instanceId == "") {
        consumer = mqClient.getConsumerRef(topic, groupId);
    } else {
        consumer = mqClient.getConsumerRef(instanceId, topic, groupId, "");
    }
    do {
        try {
            std::vector<Message> messages;
```

`//` 长轮询消费消息。 `//` 长轮询表示如果`Topic`没有消息,则请求会在服务端挂起`3s`，`3s`内如果有消息可以消费则立即返回客户端。

```
            consumer->consumeMessage(
```

`3, //` 一次最多消费3条（最多可设置为`16`条）。 `3, //` 长轮询时间3秒（最多可设置为`30`秒）。

```
                    messages
            );
            cout << "Consume: " << messages.size() << " Messages!" << endl;
```

`//` 处理业务逻辑。

```
            std::vector<std::string> receiptHandles;
            for (std::vector<Message>::iterator iter = messages.begin();
                    iter != messages.end(); ++iter)
            {
                cout << "MessageId: " << iter->getMessageId()
                    << " PublishTime: " << iter->getPublishTime()
                    << " Tag: " << iter->getMessageTag()
                    << " Body: " << iter->getMessageBody()
                    << " FirstConsumeTime: " << iter->getFirstConsumeTime()
                    << " NextConsumeTime: " << iter->getNextConsumeTime()
<<"ConsumedTimes:"<<iter->getConsumedTimes()
```

消息队列

```
                    <<  ConsumedTimes:  << iter>getConsumedTimes()
                    << " Properties: " << iter->getPropertiesAsString()
                    << " Key: " << iter->getMessageKey() << endl;
                receiptHandles.push_back(iter->getReceiptHandle());
            }
```

`//` 确认消息消费成功。 `// Message.NextConsumeTime`前若不确认消息消费成功，则消息会被重复消费。 `//` 消息句柄有时间戳，同一条消息每次消费拿到的都不一样。

```
            AckMessageResponse bdmResp;
            consumer->ackMessage(receiptHandles, bdmResp);
            if (!bdmResp.isSuccess()) {
```

`//` 某些消息的句柄可能超时，会导致消息消费状态确认不成功。

```
                const std::vector<AckMessageFailedItem>& failedItems =
                    bdmResp.getAckMessageFailedItem();
                for (std::vector<AckMessageFailedItem>::const_iterator iter = failedItem
s.begin();
                        iter != failedItems.end(); ++iter)
                {
                    cout << "AckFailedItem: " << iter->errorCode
                        << "  " << iter->receiptHandle << endl;
                }
            } else {
                cout << "Ack: " << messages.size() << " messages suc!" << endl;
            }
        } catch (MQServerException& me) {
            if (me.GetErrorCode() == "MessageNotExist") {
                cout << "No message to consume! RequestId: " + me.GetRequestId() << endl
;
                continue;
            }
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
        }
    } while(true);
}
```

消息队列

## 最佳实践

### 集群消费和广播消费

**基本概念**

RocketMQ是基于发布订阅模型的消息系统。在RocketMQ消息系统中消息的订阅方订阅关注的Topic，以获取并消费消息。由于订阅方应用一般是分布式系统，以集群方式部署有多台机器。因此RocketMQ约定以下概念。
**集群：**RocketMQ约定使用相同Group ID的订阅者属于同一个集群，同一个集群下的订阅者消费逻辑必
须完全一致（包括Tag的使用），这些订阅者在逻辑上可以认为是一个消费节点。
**集群消费：**使用集群消费模式时，RocketMQ认为任意一条消息只需要被集群内的任意一个消费者处理即
可。
**广播消费：**使用广播消费模式时，RocketMQ会将每条消息推送给集群内所有注册过的客户端，保证消息
至少被每台机器消费一次。

**场景对比**

**集群消费模式：**

图 1. 集群消费模式

**适用场景及注意事项：**

消费端集群化部署，每条消息只需要被处理一次。 由于消费进度在服务端维护，可靠性更高。 集群消费模式下，每一条消息都只会被分发到一台机器上处理。如果需要被集群下的每一台机器都处理，请使用广播模式。 集群消费模式下，不保证每一次失败重投的消息路由到同一台机器上，因此处理消息时不应该做任何确定性假设。

**广播消费模式：**

图 2. 广播消费模式消息队列适用场景及注意事项： 广播消费模式下不支持顺序消息。 每条消息都需要被相同逻辑的多台机器处理。 消费进度在客户端维护，出现重复的概率稍大于集群模式。 广播模式下，RocketMQ保证每条消息至少被每台客户端消费一次，但是并不会对消费失败的消息进行失败重投，因此业务方需要关注消费失败的情况。 广播模式下，客户端每一次重启都会从最新消息消费。客户端在被停止期间发送至服务端的消息将会被自动跳过，请谨慎选择。 广播模式下，每条消息都会被大量的客户端重复处理，因此推荐尽可能使用集群模式。 目前仅Java客户端支持广播模式。 广播模式下服务端不维护消费进度，所以RocketMQ控制台不支持消息堆积查询、消息堆积报警和订阅关系查询功能。

**使用集群模式模拟广播模式**

如果业务需要使用广播模式，也可以创建多个Group ID，用于订阅同一个Topic。 图 3. 集群方式模拟广播模式使用场景及注意事项： 每条消息都需要被多台机器处理，每台机器的逻辑可以相同也可以不一样。 消费进度在服务端维护，可靠性高于广播模式。 对于一个Group ID来说，可以部署一个消费端实例，也可以部署多个消费端实例。当部署多个消费端实例时，实例之间又组成了集群模式（共同分担消费消息）。假设Group ID 1部署了三个消费者实例 C1、C2、C3，那么这三个实例将共同分担服务器发送给Group ID1的消息。同时，实例之间订阅关系必须保持一致。

### 消息过滤

本文介绍RocketMQ消费者如何根据Tag在RocketMQ服务端完成消息过滤。 消息队列 Tag，即消息标签、消息类型，用来区分某个RocketMQ的Topic下的消息分类。RocketMQ允许消费者按照Tag对消息进行过滤，确保消费者最终只消费到其关心的消息类型。 以下图所示电商交易场景为例，从客户下单到收到商品这一过程会生产一系列消息，例如订单创建消息 （order）、支付消息（pay）、物流消息（logistics）。这些消息会发送到Topic为Trade_Topic的队列中，被各个不同的系统所接收，例如支付系统、物流系统、交易成功率分析系统、实时计算系统等。其中， 物流系统只需接收物流类型的消息（logistics），而实时计算系统需要接收所有和交易相关（order、 pay、logistics）的消息。 图 1. 消息过滤

**说明**

针对消息归类，您可以选择创建多个Topic，或者在同一个Topic下创建多个Tag。但通常情况下，不同的Topic之间的消息没有必然的联系，而Tag则用来区分同一个Topic下相互关联的消息，例如全集和子集的关系、流程先后的关系。

**参考示例**

### 发送消息

发送消息时，每条消息必须指明Tag。

```
Message msg = new Message("MQ_TOPIC","TagA","Hello MQ".getBytes());
```

### 订阅消息

消息队列消费方式1 消费者如需订阅某Topic下所有类型的消息，Tag用 * 符号表示。

```java
consumer.subscribe("MQ_TOPIC", "*", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
    }
});
```

消费方式2 消费者如需订阅某Topic下某一种类型的消息，请明确标明Tag。

```java
consumer.subscribe("MQ_TOPIC", "TagA", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
    }
});
```

消费方式3 消费者如需订阅某Topic下多种类型的消息，请在多个Tag之间用 || 分隔。

```java
consumer.subscribe("MQ_TOPIC", "TagA||TagB", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
    }
});
```

消费方式4（错误示例） 同一个消费者多次订阅某个Topic下的Tag，以最后一次订阅的Tag为准。 `//`如下错误代码中，`consumer`只能接收到`MQ_TOPIC`下`TagB`的消息，而不能接收`TagA`的消息。

```java
consumer.subscribe("MQ_TOPIC", "TagA", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
    }
}); consumer.subscribe("MQ_TOPIC", "TagB", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
    }
});
```

### 订阅关系一致

RocketMQ里的一个Group ID代表一个Consumer实例群组。对于大多数分布式应用来说，一个Group ID 下通常会挂载多个Consumer实例。订阅关系一致指的是同一个Group ID下所有Consumer实例的处理逻消息队列由于RocketMQ的订阅关系主要由Topic+Tag共同组成，因此，保持订阅关系一致意味着同一个Group ID 下所有的实例需在以下两方面均保持一致： 订阅的Topic必须一致； 订阅的Topic中的Tag必须一致。

**订阅关系图片示例**

正确订阅关系示例在下图中，多个Group ID订阅了多个Topic，并且每个Group ID里的多个消费者实例的订阅关系保持了一致。 错误订阅关系图片示例在下图中，单个Group ID订阅了多个Topic，但是该Group ID里的多个消费者实例的订阅关系并没有保持一致。

**订阅关系代码示例**

错误订阅关系代码示例例一以下例子中，同一个Group ID下的两个实例订阅的Topic不一致。 消息队列 Consumer实例1-1：

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_1"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "*", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
    }
});
```

Consumer实例1-2：

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_1"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_B ", "*", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
    }
});
```

例二以下例子中，同一个Group ID下订阅Topic的Tag不一致。Consumer实例2-1订阅了TagA，而 Consumer实例2-2未指定Tag。 Consumer实例2-1：

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_2"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "TagA", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
    }
});
```

Consumer实例2-2：

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_2"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "*", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
    }
});
```

例三此例中，错误的原因有两个： 同一个Group ID下订阅Topic个数不一致。 消息队列同一个Group ID下订阅Topic的Tag不一致。 Consumer实例3-1：

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_3"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "TagA", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
    }
}); consumer.subscribe("jodie_test_B", "TagB", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
    }
});
```

Consumer实例3-2：

```java
Properties properties = new Properties(); properties.put(PropertyKeyConst.GROUP_ID, "GID_jodie_test_3"); Consumer consumer = ONSFactory.createConsumer(properties); consumer.subscribe("jodie_test_A", "TagB", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        System.out.println(message.getMsgID());
        return Action.CommitMessage;
    }
});
```

### 消费幂等

RocketMQ消费者在接收到消息以后，有必要根据业务上的唯一Key对消息做幂等处理的必要性。

**消费幂等的必要性**

在互联网应用中，尤其在网络不稳定的情况下，RocketMQ的消息有可能会出现重复，这个重复简单可以概括为以下两种情况： 发送时消息重复当一条消息已被成功发送到服务端并完成持久化，此时出现了网络闪断或者客户端宕机，导致服务端对客户端应答失败。如果此时生产者意识到消息发送失败并尝试再次发送消息，消费者后续会收到两条内容相同并且 Message ID 也相同的消息。 投递时消息重复消息消费的场景下，消息已投递到消费者并完成业务处理，当客户端给服务端反馈应答的时候网络闪断。 为了保证消息至少被消费一次，RocketMQ的服务端将在网络恢复后再次尝试投递之前已被处理过的消息，消费者后续会收到两条内容相同并且Message ID也相同的消息。 负载均衡时消息重复（包括但不限于网络抖动、Broker重启以及订阅方应用重启） 当RocketMQ的Broker或客户端重启、扩容或缩容时，会触发Rebalance，此时消费者可能会收到重复消息。

**处理建议**

消息队列因为Message ID有可能出现冲突（重复）的情况，所以真正安全的幂等处理，不建议以Message ID作为处理依据；最好的方式是以业务唯一标识作为幂等处理的关键依据，而业务的唯一标识可以通过Key设置到消息里面：

```
Message message = new Message(); message.setKey("ORDERID_100"); SendResult sendResult = producer.send(message);
```

订阅方收到消息时可以根据消息的Key进行幂等处理：

```
consumer.subscribe("ons_test", "*", new MessageListener() {
    public Action consume(Message message, ConsumeContext context) {
        String key = message.getKey()
```

`//` 根据业务唯一标识的 `key` 做幂等处理

```
    }
});
```

### 异地多活

依托于阿里云高速通道专线和MSHA（Multi-Site High Availability）异地多活平台，RocketMQ提供多活容灾功能，通过跨实例间数据的双向同步和业务切流能力，实现业务恢复和故障恢复解耦，保障故障场景下的业务连续性。本文介绍异地多活的概念、应用场景、功能优势和配置方法。

**什么是异地多活**

异地多活MSHA（Multi-Site High Availability），是在阿里巴巴电商业务环境演进出来的多活容灾架构解决方案，可以将业务恢复和故障恢复解耦。基于灵活的流量规则调度、跨域跨云管控、数据保护等能力，实现故障场景下的业务快速切换及恢复。 RocketMQ依赖于阿里云高速通道专线MSHA实现同地域及跨地域实例间的消息数据双向同步。和传统容灾不同的是，异地多活方案中，分布在不同中心单元的RocketMQ可以分别同时对外提供服务，不仅解决了容灾本身问题，还提升了业务连续性，并且实现了资源的异地扩展。 RocketMQ的异地多活具体实现如下： 消息队列杭州单元和上海单元分别部署了一套完整的业务系统。 MSHA接入层按照数据分流规则将业务数据路由到两个业务单元，杭州单元和上海单元的应用系统和 RocketMQ Broker集群各自处理对应地域的业务。 两个单元的Broker集群配置了异地多活功能，Broker集群A和Broker集群B间的数据实现了双向同步， 包括Topic数据、Group数据及消费位点等信息。正常情况下，杭州单元和上海单元只负责各自单元的业务，并且同时将各自单元的消息数据同步到对方单元的集群中进行容灾备份。 假设杭州单元发生灾害，整个业务系统出现故障，此时通过MSHA切流操作将整个杭州的业务切到上海单元，因为配置了异地多活，上海单元的Broker集群存储了杭州单元的业务数据，可以继续处理未完成的消息数据。在保证业务不中断的前提下排查故障并修复，做到先恢复业务再恢复故障。 当杭州单元故障恢复后，通过回切流量，将杭州单元的业务重新切回到杭州单元的系统处理，整个过程用户不感知故障，不影响用户业务体验。

**应用场景**

异地多活功能适用于以下典型业务场景： 按地域划分单元的业务场景，如物流业务。可以通过物流订单的地域将业务进行划分，将业务引流到不同地域的生产中心同时处理，提高资源利用率和业务并发度。 对业务数据可靠性有严格要求的业务场景，如金融证券等。当系统出现故障会对交易结果产生较大影响， 通过异地多活可以将业务快速切换到容灾站点，并且根据同步的数据继续处理未完成的消息。

**功能优势**

**可用性**

和传统容灾方案相比，异地多活方案中所有生产中心数据实现双向同步，并且均可对外提供服务，各中心分担业务流量，提高了资源使用率。

**故障快速恢复**

消息队列异地多活功能够有效保障业务连续性。当其中一个生产中心发生故障，区别于传统的解决思路，不是去排查、处理和修复故障，而是立即使用切流将业务切换到其他生产中心，保证业务的连续性，将业务恢复和故障恢复解耦。

**异地容量扩容**

业务高速发展，受限于单地有限资源，也存在资源存储、计算网络瓶颈等问题。在RocketMQ水平拓展能力的支撑下，使业务具备其它机房或者其它地域快速扩建的特性，减少成本浪费。

**配置方法**

配置RocketMQ异地多活的具体操作，请参见**《异地多活用户指南》**手册的**《多活配置**>**同城多活配置**>配
**置消息层》**章节。

### 同城容灾

RocketMQ现已支持同城容灾场景下的多芯跨可用区容灾和非对等容灾能力，本文介绍上述两种能力的需求背景、应用场景和功能优势。

**需求背景**

在当今快速发展的数字化商业环境中，企业对确保业务连续性和服务可用性的期望值不断提高，为了应对各种不可预见的风险如自然灾害、硬件故障、网络攻击等造成的威胁，构建一个具备高容灾能力的信息系统一直以来都是大中型企业的基本要求之一。然而对于RocketMQ产品来说，同城容灾能力在实际应用中仍具有以下挑战：
**非对等容灾：**目前阿里云同城容灾大部分产品都要求主备可用区进行对等部署（即服务器数量相同），而
在实际情况下，客户在主可用区部署大规模RocketMQ实例后，在新建备可用区时只需要对少数实例进行容灾即可。在这种情境下，由于RocketMQ要求主备可用区机器数量必须一致，就会大幅增加客户的成本并造成严重的资源浪费。
**多芯跨可用区容灾：**由于硬件国产化的要求，越来越多的客户希望能够支持同城容灾场景下的多集群混合
部署以实现供应链安全。

**应用场景**

为了解决上述难题，阿里云RocketMQ产品现已支持跨可用区多集群混合部署和非对等容灾能力，主要应用场景如下：

**场景1：容灾集群 + 主可用区单机房集群**

**场景2：容灾集群 + 备可用区单机房集群**

消息队列

**场景3：容灾集群 + 主可用区单机房集群 + 备可用区单机房集群**

**功能优势**

**资源利用**

传统容灾架构往往采用固定资源配比的主从模式，导致灾备集群在常态运行中存在显著资源闲置问题。与之相比，非对等集群能够更加灵活地进行资源分配，实现了资源的合理利用。

**多芯集群混部**

在多芯混部演进的背景下，多集群架构通过深度整合硬件特性，显著提升了异构计算场景下的系统效能。

**稳定性**

通过构建多层次资源隔离机制，多集群架构在保障系统稳定性方面展现出显著优势。单一集群发生故障时不影响其他集群的业务，实现故障域隔离。

### 消息路由

RocketMQ提供的消息路由功能可用于跨集群间的消息数据同步，实现集群间消息的一致性和完整性。本文介绍消息路由的概念、应用场景、功能优势和配置方法。

**什么消息路由**

RocketMQ的消息路由功能常用于跨集群间的消息同步，通过路由规则动态规划消息的同步路径，使消息按照过滤条件从源节点同步到目标节点。实现跨集群、远距离、毫秒级消息实时同步，确保集群之间的数据一致性与完整性。 RocketMQ消息路由的具体实现如下，以Topic维度进行单向同步，将源实例下指定的源Topic的消息同步至目标实例下指定的目标Topic中。 消息队列

**应用场景**

消息路由功能的典型应用场景如下：

**数据同步**

淘宝、天猫的业务遍布全球，每个国家或者地区的卖家发布产品后，需要审核后才能上线。商品审核作为中心系统，只部署在中国（例如上海），该场景下，需要把每个地域的上线消息都同步到上海处理，实现不同地域间集群的数据同步。

**容灾备份**

消息队列对于交易核心系统，商品中心琳琅满目的商品详情与价格随时有可能发生变化，需要实时同步到各个业务系统，为保证系统更高的可用性，可采用多地域（Region）的容灾备份方案，即便某个地域完全不可用，例如光纤被铲断等极端情况，仍可保持服务的连续性。

**功能优势**

**高性能**

RocketMQ消息路由可实现毫秒级实时同步、百万级TPS的传输能力。

**低成本**

无需额外拉通专线、无需升级改造、无需代码适配，应用无感知。

**易用性**

通过RocketMQ控制台进行界面化配置即可实现路由任务的管理。

**使用限制**

消息路由功能仅适用于有命名空间的实例。实例是否有命名空间，可在控制台**实例详情**页面的**实例信息**页签查看。

**配置方法**

RocketMQ消息路由功能的配置流程如下，详细信息，请参见控制台操作配置消息路由。

**步骤一：创建消息同步云**

创建路由任务前，需要先录入部署了RocketMQ集群的云环境的相关信息。包括RocketMQ服务端的接入点、域名、云环境所属账号的AK、SK等。RocketMQ将根据录入的云信息获取跨云访问RocketMQ资源的权限。

**步骤二：创建路由任务**

指定消息源和消息目标，设置过滤条件和同步位点等信息。 消息队列

## 产品使用问题

### 常见问题

#### 快速入门

本文简要概括了新手用户使用RocketMQ过程中可能遇到的问题。
1. 新创建的Group ID从哪里开始消费？
如果这个Group ID是第一次启动，则会忽略启动之前发送的消息，也就是忽略历史消息，从启动之后发送的消息开始消费。 如果这个Group ID是第二次启动，那么从上次消费的位置开始消费。 如果想从特定位置开始消费，可以通过RocketMQ控制台的消费位点重置功能，指定到具体的时间开始消费。每次重置只针对特定Group ID下的特定Topic，不会影响其他Group ID。
2. RocketMQ消费失败如何重新消费消息？

**集群消费方式**

消费业务逻辑代码如果返回Action.ReconsumerLater，或者NULL，或者抛出异常，消息都会走重试流程，至多重试16次，如果重试16次后，仍然失败，则消息丢弃。每次重试的间隔时间如下：

| 第几次重试 | 每次重试间隔时间 |
|---|---|
| 1 | 10秒 |
| 2 | 30秒 |
| 3 | 1分钟 |
| 4 | 2分钟 |
| 5 | 3分钟 |
| 6 | 4分钟 |
| 7 | 5分钟 |
| 8 | 6分钟 |
| 9 | 7分钟 |
| 10 | 8分钟 |
| 11 | 9分钟 |
| 12 | 10分钟 |
| 13 | 20分钟 |
| 14 | 30分钟 |
| 15 | 1小时 |
| 16 | 2小时 |

可以通过调用message.getReconsumeTimes()方法来获取消息的重试次数。 消息队列

**广播消费方式**

广播消费方式仍然能保证一条消息至少被消费一次，但消费失败后不做重试操作。
3. 消息发送了，但是没有收到怎么办？
RocketMQ提供了多种消息查询方式： 使用Topic按时间范围进行查询，可以查询到一段时间内某Topic收到的所有消息。 使用Topic和Message ID对消息进行精准查询。 使用Topic和Message Key较为精准地查询具有相同Message Key的一类消息。 上述方式可以查询到消息的具体内容以及消费情况，如果需要追踪一条消息从生产者发出到被消费者消费的整个链路中各个相关节点的时间地点，可以使用RocketMQ最新的消息轨迹查询功能，具体操作方式请
4. RocketMQ是否能保证消息不重复？
绝大多数情况下，消息是不重复的。作为一款分布式消息中间件，在网络抖动、应用处理超时等异常情况下，无法保证消息不重复，但是能保证消息不丢失。

#### 配置相关

RocketMQ配置相关的常见问题如下。
1. RocketMQ消息在服务器保存多长时间？
存储的消息最多保存3天，超过3天未消费的消息会被删除。
2. RocketMQ消息Body的长度限制是多少？
消息大小根据消息类型来限制。具体限制如下所述： 普通消息和顺序消息：4 MB 事务消息和定时/延时消息：64 KB
3. RocketMQ客户端如何设置消费线程数？
在启动Consumer时，设置一个ConsumeThreadNums属性即可。具体示例如下所示：

```
    public static void main(String[] args) {
        Properties properties = new Properties();
        properties.put(PropertyKeyConst.GROUP_ID, "GID_001");
        properties.put(PropertyKeyConst.AccessKey, "xxxxxxxxxxxx");
        properties.put(PropertyKeyConst.SecretKey, "xxxxxxxxxxxx");
        /**
```

* 设置消费端线程数固定为 `20`
`*/`

```java
        properties.put(PropertyKeyConst.ConsumeThreadNums,20);
        Consumer consumer =ONSFactory.createConsumer(properties);
        consumer.subscribe("TestTopic", "*", new MessageListener() {
            public Action consume(Message message, ConsumeContext context) {
                System.out.println("Receive: " + message);
                return Action.CommitMessage;
            }
        });
        consumer.start();
        System.out.println("Consumer Started");
    }
```

4. 由于.NET 客户端的配置问题，导致dll加载失败或者其他运行错误时如何处理？
具体操作方式请参见.NET SDK压缩包中的文档：SDK_GUIDE.pdf，确认工程配置与文档说明一致。 消息队列

#### 消息轨迹

RocketMQ消息轨迹常见问题如下。
1. 为什么查询不到轨迹数据？
当输入查询条件查不到轨迹数据时，请参考是否属于以下无法查询情况。 i. 消息轨迹目前支持Java客户端（版本至少为1.2.2） ii. 查询条件是否正确，Topic、Message ID、Message Key是否输入正确。 iii. 查询时间区间是否正确，为了提高查询速度，需要您输入消息的发送时间范围，如果查询不到，请尝试扩大时间范围重试。 iv. 如果确认上述情况无误还是无法查询到结果，请联系技术支持，并附带上日志文件，日志文件位于/home/{user}/logs/ons.log。 v. 如果确认上述情况无误还是无法查询到结果，请提交工单获得技术支持，并附带上日志文件，日志文件位于/home/{user}/logs/ons.log。
2. 确定已经消费了消息，但轨迹却显示没有消费，而且客户端IP和Group ID不符合实际情况？
出现该现象是由于客户端本身并没有升级到支持轨迹功能的版本，因此RocketMQ轨迹查询后端仅仅能够拿到部分不完整的轨迹数据，展现结果不正常，建议尽快升级客户端。消息轨迹的详细说明，请参见查询消息轨迹。
3. 消费者列表中为什么没有我的Group ID？
出现该情况的原因可能是消息的下游订阅方太多，轨迹图中空间有限，请将鼠标放在滚动条位置，滚动查看完整数据。
4. 之前的查询任务怎么看不到了？
为了防止历史查询任务太多，影响展示效果，RocketMQ会对您的历史查询任务做定期清理，默认只保留 7天以内的查询任务，如果出现历史任务看不到，请重新查询即可。

#### 告警处理

RocketMQ告警处理暂不可用。 由于专有云环境是孤岛环境，无法接通短信网关等公网环境接口，所以您在控制台看到监控报警模块暂不可用。

#### 顺序消息

RocketMQ顺序消息相关的常见问题如下。
1. **顺序消息是否支持集群消费和广播消费？**
顺序消息支持集群消费，不支持广播消费。
2. **同一条消息是否可以既是顺序消息，同时又支持定时消息、事务消息？**
不行。顺序消息、定时消息、事务消息是不同的消息类型，三者是互斥关系，不能叠加在一起使用。
3. **顺序消息的使用范围是什么？**
顺序消息是指在同一个Topic内保证顺序。
4. **顺序消息支持哪种消息发送方式？**

### 异常类别

消息队列

#### 使用异常

RocketMQ使用过程中可能遇到的异常问题如下。
1. 启动Producer、Consumer失败，Group ID重复。
可能产生的原因： 在同一个JVM里面使用同一个Group ID配置了多个Producer或Consumer实例，导致客户端启动失败。 建议解决方案： 按如下步骤操作： i. 确保在一个JVM进程中只启动了同一个Group ID的一个Producer或Consumer实例，即可以在一个 JVM进程中同时启动同一个Group ID的一个Producer和一个Consumer实例，但不能同时启动多个 Producer或Consumer实例。 ii. 重启应用。
2. 广播模式下，消费者启动加载JSON文件异常。
可能产生的原因： Fastjson版本太低导致广播消费者加载本地的offsets.json文件异常，导致启动失败。 建议解决方案： 将Fastjson的版本升级到ons-client所依赖的版本，保证本地的offsets.json能够被正常加载。默认情况下offsets.json在/home/{user}/.rocketmq_offsets/下。
3. 主动订阅消息，获取队列列表失败。
可能产生的原因： 可能未在控制台上创建该Topic，导致消费方启动时获取Topic的队列信息失败。 建议解决方案： 按如下步骤操作： ii. 在**实例列表**页面，根据实例名称找到目标实例，单击目标实例ID或右侧**操作**列的**详情**，进入**实例详情**页面。 iv. 单击**Group** **管理**页签，而后单击**创建** **Group ID**，按提示创建Group ID。 v. 重启应用。
4. 发消息失败。
发送消息尝试多次失败。 可能产生的原因： i. RocketMQ Broker向Producer返回了错误码，具体错误形式参见这个异常对应的嵌套异常； ii. RocketMQ Broker宕机后，Producer还未发现最新的Broker列表，会短暂报此异常； iii. Producer发送消息超时，一般由服务器压力过大或者网络不稳定导致。 建议解决方案： 按如下步骤操作： i. 报此异常是暂时的，可能是RocketMQ Broker正在重启维护或者是服务器压力过大产生的短暂超时， 请稍等一下再尝试。 ii. 如果一直尝试未果，请联系技术支持。
5. 未收录异常解决办法。
消息队列问题描述： 暂未收录任何异常。 建议解决方案： 请联系技术支持。
6. 消息显示Consumed，但消费端未感知到。
消息状态显示Consumed，但是消费端业务日志显示没有收到消息，这种问题一般是下面三个原因导致的。 业务代码在接收到消息后，不立即打印消息。 收到消息后，如果直接进入业务逻辑，一旦代码遗漏某个逻辑分支，就会导致消息信息没有被留在业务日志里，造成没有收到消息的假象。 建议您收到消息后，立刻打印消息信息留存messageId、timestamp、reconsumeTime等。 消费端部署了多个消费实例。 尤其是在调试阶段，消费端不可避免会多次重启，一旦多个消费进程同时存在（进程未退出），那么相当于进入集群的消费模式，多个消费实例会共同分担消费消息。以为没有收到的消息，其实是被另一个消费端接收了。 到RocketMQ控制台，进入**Group** **管理** > **消费者状态** > **连接信息**，会显示消费端的实例部署情况 （有几个消费实例，各自的连接IP等等），然后可以自行排查。 消息消费过程出现未被Catch的异常，导致消息被重新投递。

```java
public class MessageListenerImpl implements MessageListener {
    @Override
    public Action consume(Message message, ConsumeContext context) {
```

`//`消息处理逻辑抛出异常，消息将重试。

```
        doConsumeMessage(message);
```

`//`如果在`doConsumeMessage()`方法中出现未被`Catch`的异常，这行日志将不会打印。

```
        log.info("Receive Message, messageId:", message.getMsgID());
        return Action.CommitMessage;
    }
}
```

如果问题还未能解决，请提供本地SDK日志，联系售后技术支持。

#### 资源不存在

1. Group ID不存在
可能产生的原因： 未在控制台上创建该Group ID，导致使用该Group ID与RocketMQ Broker创建连接的时候，服务器校验不通过。 建议解决方案： 按如下步骤操作： 如果该Group ID已存在，则直接执行下一步。 如果该Group ID不存在，请先创建该Group ID，然后执行下一步。 ii. 重启应用。
2. 主机名不存在
消息队列可能产生的原因： 可能是无法正确获取主机名或者主机IP地址导致，请尝试使用此命令来证实：**hostname** 如果无法正常输出，就说明确实是此原因；如果可以正常输出，可能是其他原因，请联系技术支持。 建议解决方案： 按如下步骤操作： i. 在报错机器上执行查看主机名命令。

```
[root@iZ231wxgt6mZ ~]# hostname iZ231wxgt6mZ
```

如果执行命令报错，请检查是否给hostname定义了别名，例如在.bash_profile或者.bashrc中alias xxx=‘hostname’；或者命令路径不在$PATH下面。 ii. Ping主机。

```
[root@iZ231wxgt6mZ ~]# ping iZ231wxgt6mZ
```

如果无法正常ping通主机名，则需要将本机地址绑定到/etc/hosts文件中。默认ECS机器都会有一个本地地址和主机名的绑定关系，切勿手动地将其去除。 iii. 确认系统配置。 检查/etc/sysconfig/network中的记录的hostname是否和/etc/hosts中绑定的主机名一致，如果不一致请修改。如果需要修改/etc/sysconfig/network中的内容，修改后需要重启机器才能生效。建议不要随意修改系统文件里的配置，可能会引发一些其他异常问题。 以上三个步骤确认完毕后，客户端启动就不在会报UnknownHostException的异常了。

#### 状态不一致

1. 消息不合法

**可能产生的原因：**

一般是消息属性、消息内容不合法，不合法的情况有： 消息为空； 消息内容为空； 消息内容长度为 0； 消息内容超过限定长度。

**建议解决方案：**

请确保消息没有以上的不合法情况，并根据异常提示进行解决。
2. 参数不合法

**可能产生的原因：**

参数不合法的情况有以下几种：

| 嵌套的异常说明 | 异常描述 |
|---|---|
| consumeThreadMin Out of range [1, 1000] | 消费端线程数设置不合理 |
| consumeThreadMax Out of range [1, 1000] | 消费端线程数设置不合理 |
| messageListener is null | 未设置messageListener |

消息队列

| consumerGroup is null | 未设置Group ID |
|---|---|
| msg delay time more than 40 day | 定时消息延时不能超过40天 |

**建议解决方案：**

按照如下步骤操作： i. 按照异常提示修改客户端对应参数的配置，确保其在合理范围内。 ii. 重启应用。
3. 客户端状态异常

**可能产生的原因：**

i. 创建Consumer、Producer之后未显示调用start()方法来启动客户端。 ii. 创建Consumer、Producer之后start()过程有异常导致客户端启动失败。 iii. 创建Consumer、Producer并成功调用start()方法后，显示调用了shutdown()方法关闭了客户端。

**建议解决方案：**

按如下步骤操作： i. 确保创建Group ID之后调用start()，保证客户端处于启动状态。 ii. 查看ons.log判断在客户端在启动过程中是否有异常。

#### 4. 订阅关系不一致

**问题描述：**

在不同的JVM中启动了多个Consumer，并且给相同的Group ID配置了不同的Topic，或者是相同的

**错误代码示例：**

错误示例一：同一个Group ID（GID-MQ-FAQ）订阅的Topic不同（分别是MQ-FAQ-TOPIC-1、MQ- FAQ-TOPIC-2）。

**JVM-1上的代码：**

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
        }
    });
    consumer.start();
```

**JVM-2上的代码：**

消息队列

```java
     Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-2", "NM-MQ-FAQ", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
        }
    });
    consumer.start();
```

错误示例二：同一Group ID（GID-MQ-FAQ）订阅的Topic相同，但Tag不同（分别NM-MQ-FAQ- 1、NM-MQ-FAQ-2）。

**JVM-1上的代码：**

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ-1", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
        }
    });
    consumer.start();
```

**JVM-2上的代码：**

```java
     Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ-2", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
        }
    });
    consumer.start();
```

**建议解决方案：**

请确保在不同JVM中使用相同的Group ID启动多个Consumer时，配置的Topic和Tag是一致的。

### 故障处理

#### 非预期的客户端连接

**现象**

【现象1】：用户侧反馈部分消息发送后未收到，同时结合RocketMQ控制台操作：**消息轨迹** > **创建查询**
**任务** > 按**Message ID****查询**，发现部分消息已发送至Broker，但未投递给下游消费者。
【现象2】：用户侧反馈RocketMQ控制台：进入**Group** **管理** > **消费者状态** > **连接信息**查看，出现不在预期范围内的客户端IP，同时存在部分消息堆积只在非预期范围内的客户端上。 消息队列

**分析**

**分析方法**：在RocketMQ控制台选择**Group** **管理** > **消费者状态** > **连接信息**，页面中能展示目前GID下面
所有客户端的连接状态，可定位非预期客户端的IP地址、进程ID，需要确认对应进程加载的配置是正确的 （包括AK、SK、Topic、GID），否则会导致该客户端进程占用部分队列而无法正确消费消息的问题。
**原因**：在同—套环境中，以错误的方式（AK、SK、Topic等信息配置错误）启动了GID的客户端，导致该
客户端进程占用了Topic下的部分而无法正确消费消息，消息在服务端堆积，无法实时投递给下游正确的消费者。
**确认方式**：先根据连接状态定位有问题的进程，然后通过以及/{user.home}/logs/ons.log程序代码确认
配置的AK、SK、Topic等信息。
**恢复方法**：（快速恢复）可以先将有问题的客户端进程先关闭，此时之前堆积的消息会立马进行
Rebalance投递至正常的客户端，待定位到问题修复后再重启有问题的进程。

**验证**

用户侧反馈RocketMQ控制台：进入**Group** **管理** > **消费者状态** > **连接信息**查看，所有已连接的客户端都能在预期范围内，并能正常消费消息；同时**订阅关系是否**—致—栏显示是。

#### 订阅关系不一致

**问题描述**

Group ID订阅的部分消息未收到。登录RocketMQ控制台，选择**消息查询** > 按**Message ID****查询消** 息，消息显示已至少被消费—次，但从消费逻辑判断未消费。 登录RocketMQ控制台，选择**Group** **管理** > **消费者状态**，**订阅关系是否**—致一栏显示否。

**问题分析**

RocketMQ里的—个Group ID代表—个Consumer实例群组。对大多数分布式应用来说，—个Group ID下通常会挂载多个Consumer实例。订阅关系—致指，同—个Group ID下所有的Consumer实例的Topic和 Tag都必须完全—致。 若同一个Group ID下的Consumer实例配置了不同的 Topic，或是Topic相同但Tag不同，订阅关系就会不一致。—旦订阅关系不—致，消息消费的逻辑就会混乱，导致消息丢失。
**【原因**1**】：**配置了相同Group ID的不同客户端订阅的 Topic 不—致。
**错误示例：**同一个Group ID（GID-MQ-FAQ）订阅的Topic不同（分别是MQ-FAQ-TOPIC-1、MQ-FAQ-
TOPIC-2）。

**JVM-1上的代码：**

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
        }
    });
    consumer.start();
```

**JVM-2上的代码：**

消息队列

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-2", "NM-MQ-FAQ", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
        }
    });
    consumer.start();
```

**【原因**2**】：**同一个Group ID下的不同客户端订阅的Topic 相同，但Tag不同。
**错误示例：**同一Group ID（GID-MQ-FAQ）订阅的Topic 相同，但Tag不同（分别是 NM-MQ-FAQ-1、
NM-MQ-FAQ-2）。

**JVM-1上的代码：**

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ-1", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
        }
    });
    consumer.start();
```

**JVM-2上的代码：**

```java
    Properties properties = new Properties();
    properties.put(PropertyKeyConst.GROUP_ID, "GID-MQ-FAQ");
    Consumer consumer = ONSFactory.createConsumer(properties);
    consumer.subscribe("MQ-FAQ-TOPIC-1", "NM-MQ-FAQ-2", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println("Receive: " + message);
            return Action.CommitMessage;
        }
    });
    consumer.start();
```

**解决方案**

请按照如下步骤操作：
1. 检查不同客户端的订阅代码。保持配置相同Group ID的所有客户端的订阅关系—致，包括订阅的Topic与
Tag。
2. 重启所有客户端应用。

**结果验证**

消费者能接收到所有期望被接收的消息。 登录RocketMQ控制台，进入**Group** **管理** > **消费者状态**，**订阅关系是否**—致一栏显示是。

#### 消息堆积

消息队列本文介绍消息堆积的问题现象、分析方法、解决方案及验证方法。

**问题描述**

登录RocketMQ控制台，进入**Group** **管理** > **消费者状态**，**堆积量**一栏的值高于预期。 登录RocketMQ控制台，进入**消息轨迹** > **创建查询任务** > 按**Message ID****查询**，部分消息已发送至 Broker，但未投递给下游消费者。

**问题分析**

RocketMQ的消息发送至Broker后，配置了Group ID的客户端根据当前的消费位点从Broker拉取—部分消息到本地进行消费。消费过程中访问共享资源加锁、I/O和网络资源争抢、HTTP调用未设置超时时间等原因，都会导致单条消息的消费时间很长，消息开始在服务端堆积。 如果消息已经没有堆积，检查阈值是否设置过小导致消息堆积。

**解决方案**

**请按照如下方法进行问题排查和解决：**

登录RocketMQ控制台，进入**资源报表** > **消息消费**，查询历史消费记录。如果消息写入速度大于消息消费速度，调整业务代码或对消费者进行扩容。 在应用打印Jstack信息**jstack -l {PID} | grep ConsumeMessageThread** 。如果有消息阻塞现象，连续打印5次Jstack信息，确认消费线程卡在哪里，解决后可尝试重启应用观察消费是否恢复。

**结果验证**

在应用打印Jstack信息**jstack -l {PID} | grep ConsumeMessageThread** ，无消费线程阻塞现象。 登录RocketMQ控制台，进入**Group** **管理** > **消费者状态**，**实时消费速度**上升，**堆积量**下降。

#### Java进程的消息堆积

**问题现象**

在RocketMQ控制台的**消费者状态**页面，Group ID的实时消息堆积量的值高于预期，且性能明显下降。

**可能原因**

**解决方案**

1. 登录RocketMQ控制台，通过查看消费者状态获取消息堆积的消费者实例所对应的宿主机IP地址，并登录
该宿主机或容器。
2. 执行以下任意命令，查看并记录Java进程的PID。

```
ps -ef |grep java jps -lm
```

3. 执行以下命令，查看堆栈信息。

```
jstack -l pid > /tmp/pid.jstack
```

4. 执行以下命令，查看 `ConsumeMessageThread` 的信息，重点关注线程的状态及堆栈。

```
cat /tmp/pid.jstack|grep ConsumeMessageThread -A 10 --color
```

系统显示类似下图所示。 消息队列线程状态的解释说明请参见Java官方文档。 RocketMQ能支持10亿级别的消息堆积，不会因为消息堆积导致性能明显下降。如按以

**说明**

上操作还未解决因消息堆积而导致的性能下降问题，请附带以下信息联系运维人员：

|  | jmap -dump:format=b,file=heap.bin [$PID] |
|---|---|
| gzip heap.bin |  |

PID。 发生消息堆积的消费者客户端ons.log本地日志。 消费者客户端的版本。

#### 消息在客户端缓存导致应用OOM

本文介绍应用OOM的问题现象、分析方法、恢复方法及验证方法。

**现象**

【现象1】：在应用部署的机器上通过查看内存已消耗完。 【现象2】：在 `/{user.home}/logs/ons.log` 能搜索到“OutOfMemory”关键字。 【现象3】：用户侧反馈RocketMQ控制台：进入**Group** **管理** > **消费者状态**，**实时消息堆积量**—栏显示消息堆积较多，同时在连接状态—栏显示了各个已连接客户端的消息堆积，同时通过Jstack排查 `ConsumeMessageThread_` 线程无消费卡住。

**分析**

**分析方法**：RocketMQ的消费者会主动从Broker拉取消息，先缓存至客户端本地然后再将消息投放至业务
的消费逻辑；在1.7.0.Final版本之前，默认客户端最多会给每个topic的每个队列缓存1000条消息；假设每个topic的队列数是16 个（集群2主2备，每台broker上8个队列），该topic下单条消息平均大小64 KB， 那么最终该topic在客户端缓存的消息Size：16* 1000 * 64 KB = 1 GB，如果用户同时订阅了8个topic 都在客户端内存缓存消息，最终占用内存将超过用户的JVM配置，导致OOM。 【原因1】：依赖1.7.0.Final之前的ons-client版本，并且topic的平均消息大小超过4K，并且消息消费比较慢容易在客户端内存缓存消息。
**确认方式**：在 `/{user.home}/logs/ons.log` 能搜索到“OutOfMemory”关键字；或者通过 `jmap`
`-dump:live,format=b,file=heap.bin <pid>` 命令确认哪些对象占用了大量内存。
**恢复方案**：升级ons-client版本至1.7.0.Final及以上，同时给对应的ConsumerBean配合设置

```
 com.aliyun.openservices.ons.api.PropertyKeyConst#MaxCachedMess ageSizeInMiB 参数，
```

然后重启应用。 【原因2】：依赖1.7.0.Final及以后的ons-client版本，默认最大消耗内存512 MB（GID订阅的所有消息队列 topic缓存总和）；如果应用仍然出现OOM的现象，可通过在ConsumerBean启动时配

```
置 com.aliyun.openservices.ons.api.PropertyKeyConst#MaxCachedMessageSizeInMiB 参数自行
```

定义最大消耗内存（范围在16 MB ~ 2048 MB）。
**确认方式**：确认应用依赖的ons-client的版本，并通过JVM确认给进程分配的内存大小。
**恢复方案**：根据应用机器的内存使用清况给对应的ConsumerBean设

```
置 com.aliyun.openservices.ons.api.PropertyKeyConst#MaxCachedMess ageSizeInMiB 参数，
```

然后重启应用。

**验证**

【验证1】：在 `/{user.home}/logs/ons.log` 中“OutOfMemory”关键字不再出现。 【验证2】：进入**Group** **管理** > **消费者状态**，看到**实时消费速度**一栏的值上升，同时**实时消息堆积量**下降。
