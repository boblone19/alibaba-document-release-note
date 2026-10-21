---
title: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Message Queue Developer Guide 20241105"
product_version: "V3.18.3"
doc_version: "20241105"
pdf_pages: 103
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Message Queue Developer Guide 20241105.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97MQ/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Alibaba%20Cloud%20Message%20Queue%20Developer%20Guide%2020241105.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Message Queue Developer Guide 20241105

## Table of Contents

- 1 Preparations
  - 1.1 Obtain API information and the endpoint of an API operation
  - 1.2 Obtain an AccessKey pair
  - 1.3 Obtain the values of common header parameters
  - 1.4 Obtain access credentials assigned by STS
  - 1.5 Obtain the endpoint of Message Queue for Apache RocketMQ
- 2 API reference
  - 2.1 RocketMQ_API
    - 2.1.1 Updates
    - 2.1.2 Overview
      - 2.1.2.1 Intended audience and scenarios
      - 2.1.2.2 Scenarios and limits
      - 2.1.2.3 Basic principles
    - 2.1.3 Common parameters
      - 2.1.3.1 Common request parameters
      - 2.1.3.2 Common response parameters
    - 2.1.4 Common terms
      - 2.1.4.1 Account security
        - 2.1.4.1.1 AccessKey
        - 2.1.4.1.2 SecretKey
      - 2.1.4.2 Resource management
        - 2.1.4.2.1 Topic
        - 2.1.4.2.2 Group ID
    - 2.1.5 Error codes
    - 2.1.6 API reference
      - 2.1.6.1 Region management
        - 2.1.6.1.1. /json/region/list
      - 2.1.6.2 Cluster management
        - 2.1.6.2.1. /json/cluster/list
      - 2.1.6.3 Instance management
        - 2.1.6.3.1. /json/vpcTunnel/tunnelSwitch
        - 2.1.6.3.2. /json/instance/baseInfo
        - 2.1.6.3.3. /json/instance/create
        - 2.1.6.3.4. /json/instance/delete
        - 2.1.6.3.5. /json/instance/list
        - 2.1.6.3.6. /json/instance/update
      - 2.1.6.4 Topic management
        - 2.1.6.4.1. /json/topic/create
        - 2.1.6.4.2. /json/topic/delete
        - 2.1.6.4.3. /json/topic/get
        - 2.1.6.4.4. /json/topic/listInPage
        - 2.1.6.4.5. /json/topic/update
        - 2.1.6.4.6. /json/topic/listNames
        - 2.1.6.4.7. /json/topic/subDetail
      - 2.1.6.5 Group management
        - 2.1.6.5.1. /json/group/create
        - 2.1.6.5.2. /json/group/delete
        - 2.1.6.5.3. /json/group/list
        - 2.1.6.5.4. /json/group/subDetail
        - 2.1.6.5.5. /json/group/consumerUpdate
      - 2.1.6.6 Consumption management
        - 2.1.6.6.1. /json/consumer/accumulate
        - 2.1.6.6.2. /json/consumer/status
        - 2.1.6.6.3. /json/consumer/getConnection
        - 2.1.6.6.4. /json/consumer/timespan
        - 2.1.6.6.5. /json/consumer/resetoffset
      - 2.1.6.7 Message query
        - 2.1.6.7.1. /json/message/trace
        - 2.1.6.7.2. /json/message/getById
        - 2.1.6.7.3. /json/message/getByKey
        - 2.1.6.7.4. /json/message/getByPagedTopic
      - 2.1.6.8 Publishing and subscription statistics
        - 2.1.6.8.1. /json/trend/topicInputTps
        - 2.1.6.8.2. /json/trend/groupOutputTps
      - 2.1.6.9 Authorization management
        - 2.1.6.9.1. /json/empower/create
        - 2.1.6.9.2. /json/empower/createBySub
        - 2.1.6.9.3. /json/empower/delete
        - 2.1.6.9.4. /json/empower/list
      - 2.1.6.10 Dead-letter queue management
        - 2.1.6.10.1. /json/message/getByIdInDLQ
        - 2.1.6.10.2. /json/message/getByPagedDLQ
        - 2.1.6.10.3. /json/message/resendByIdInDLQ
- 3 SDK reference
  - 3.1 文档标题缺失，请补全后重新导出
    - 3.1.1 Overview
    - 3.1.2 Messaging model
    - 3.1.3 Updates
    - 3.1.4 Transport protocol and character encoding
    - 3.1.5 Common classes and methods
      - 3.1.5.1 PropertyKeyConst
      - 3.1.5.2 ONSFactory
        - 3.1.5.2.1 createConsumer
        - 3.1.5.2.2 createBatchConsumer
        - 3.1.5.2.3 createOrderedConsumer
        - 3.1.5.2.4 createOrderProducer
        - 3.1.5.2.5 createProducer
        - 3.1.5.2.6 createTransactionProducer
      - 3.1.5.3 Message
        - 3.1.5.3.1 Overview
        - 3.1.5.3.2 Default message construction
        - 3.1.5.3.3 Message construction by using parameters (1)
        - 3.1.5.3.4 Message construction by using parameters (2)
        - 3.1.5.3.5 putUserProperties
        - 3.1.5.3.6 getUserProperties
        - 3.1.5.3.7 getTopic
        - 3.1.5.3.8 setTopic
        - 3.1.5.3.9 getTag
        - 3.1.5.3.10 setTag
        - 3.1.5.3.11 getKey
        - 3.1.5.3.12 setKey
        - 3.1.5.3.13 getMsgID
        - 3.1.5.3.14 setMsgID
        - 3.1.5.3.15 getReconsumeTimes
        - 3.1.5.3.16 setReconsumeTimes
        - 3.1.5.3.17 getBornTimestamp
        - 3.1.5.3.18 setBornTimestamp
        - 3.1.5.3.19 getBornHost
        - 3.1.5.3.20 setBornHost
        - 3.1.5.3.21 getStartDeliverTime
        - 3.1.5.3.22 setStartDeliverTime
        - 3.1.5.3.23 getShardingKey
        - 3.1.5.3.24 setShardingKey
      - 3.1.5.4 ONSClientException
        - 3.1.5.4.1 Default ONSClientException construction
        - 3.1.5.4.2 ONSClientException construction by using parameters (1)
        - 3.1.5.4.3 ONSClientException construction by using parameters (2)
        - 3.1.5.4.4 ONSClientException construction by using parameters (3)
      - 3.1.5.5 Message sending
        - 3.1.5.5.1 Overview
        - 3.1.5.5.2 SendResult
          - 3.1.5.5.2.1 Default SendResult construction
          - 3.1.5.5.2.2 getMessageId
          - 3.1.5.5.2.3 getTopic
          - 3.1.5.5.2.4 toString
        - 3.1.5.5.3 Producer
          - 3.1.5.5.3.1 Overview
          - 3.1.5.5.3.2 send
          - 3.1.5.5.3.3 sendOneway
          - 3.1.5.5.3.4 sendAsync
          - 3.1.5.5.3.5 isStarted
          - 3.1.5.5.3.6 isClosed
          - 3.1.5.5.3.7 start
          - 3.1.5.5.3.8 shutdown
        - 3.1.5.5.4 TransactionProducer
          - 3.1.5.5.4.1 send
          - 3.1.5.5.4.2 isStarted
          - 3.1.5.5.4.3 isClosed
          - 3.1.5.5.4.4 start
          - 3.1.5.5.4.5 shutdown
          - 3.1.5.5.4.6 LocalTransactionExecuter
          - 3.1.5.5.4.7 TransactionStatus
        - 3.1.5.5.5 OrderProducer
          - 3.1.5.5.5.1 send
          - 3.1.5.5.5.2 isStarted
          - 3.1.5.5.5.3 isClosed
          - 3.1.5.5.5.4 start
          - 3.1.5.5.5.5 shutdown
      - 3.1.5.6 Message subscription
        - 3.1.5.6.1 Overview
        - 3.1.5.6.2 Consumer
          - 3.1.5.6.2.1 Overview
          - 3.1.5.6.2.2 subscribe
          - 3.1.5.6.2.3 unsubscribe
          - 3.1.5.6.2.4 isStarted
          - 3.1.5.6.2.5 isClosed
          - 3.1.5.6.2.6 start
          - 3.1.5.6.2.7 shutdown
        - 3.1.5.6.3 MessageListener
          - 3.1.5.6.3.1 Overview
          - 3.1.5.6.3.2 consume
        - 3.1.5.6.4 Action
          - 3.1.5.6.4.1 Overview
          - 3.1.5.6.4.2 valueOf
          - 3.1.5.6.4.3 values
        - 3.1.5.6.5 PropertyValueConst
        - 3.1.5.6.6 OrderConsumer
          - 3.1.5.6.6.1 Overview
          - 3.1.5.6.6.2 subscribe
          - 3.1.5.6.6.3 unsubscribe
          - 3.1.5.6.6.4 isStarted
          - 3.1.5.6.6.5 isClosed
          - 3.1.5.6.6.6 start
          - 3.1.5.6.6.7 shutdown
        - 3.1.5.6.7 MessageOrderListener
          - 3.1.5.6.7.1 Overview
          - 3.1.5.6.7.2 consume
        - 3.1.5.6.8 OrderAction
          - 3.1.5.6.8.1 Overview
          - 3.1.5.6.8.2 valueOf
          - 3.1.5.6.8.3 values
        - 3.1.5.6.9 BatchConsumer
          - 3.1.5.6.9.1 Overview
          - 3.1.5.6.9.2 subscribe
          - 3.1.5.6.9.3 unsubscribe
          - 3.1.5.6.9.4 isStarted
          - 3.1.5.6.9.5 isClosed
          - 3.1.5.6.9.6 start
          - 3.1.5.6.9.7 shutdown
        - 3.1.5.6.10 BatchMessageListener
          - 3.1.5.6.10.1 Overview
          - 3.1.5.6.10.2 consume

## 1 Preparations

### 1.1 Obtain API information and the endpoint of an API operation

**the endpoint of an API operation**

To call an API operation of a cloud service, you must familiarize yourself with the information about the operation, including the service code, operation name, and API version.

**Background information**

The API information on the debugging page in the Apsara Uni-manager Management Console is for reference only. For information about how to call API operations, see the developer guides of cloud services. If the information on the debugging page is different from that in the developer guide of a cloud service, the information in the developer guide shall prevail.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI**
**Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging**.
4. In the left-side navigation pane, select the cloud service that you want to manage.
5. Select an API version from the **Version** drop-down list.
6. In the API operation list, view all API operations of the current version.
7. Click the API operation that you want to call. Obtain the endpoint from the Endpoint
parameter on the Parameter tab.

### 1.2 Obtain an AccessKey pair

An AccessKey pair that consists of an AccessKey ID and an AccessKey secret is used to implement symmetric encryption to verify the identity of a request sender. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. This topic describes how to obtain an AccessKey pair that is assigned by Resource Access Management (RAM).

**Prerequisites**

An account that assumes the operations administrator or level-1 organization administrator role is obtained. Only operations administrators or level-1 organization administrators can obtain the AccessKey pairs of organizations.

**Background information**

Access credentials can be assigned by RAM or Security Token Service (STS). RAM: assigns an AccessKey pair that consists of an AccessKey ID and an AccessKey secret. STS: assigns an access credential that consists of an AccessKey ID, an AccessKey secret, and a security token. This topic describes how to obtain an AccessKey pair that is assigned by RAM. For information about how to obtain an access credential that is assigned by STS, see Obtain access credentials assigned by STS. We recommend that you use the AccessKey pairs of personal accounts to call the API operations of the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error message that indicates insufficient permissions may appear.

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID. Example: cn-hangzhou-*. |
| x-acs-organizationid | The organization ID in the Apsara Uni-manager Management Console. For information about how to obtain an organization ID, see the "GetOrganizationList" section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The resource set ID in the Apsara Uni-manager Management Console. For information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to perform an operation on an Elastic Compute Service (ECS) instance, obtain the ECS instance ID from the ECS instance list. |

> **Warning:** The AccessKey pair of a personal account is managed and limited by the permission system of the Apsara Uni-manager Management Console. If you want to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the page that appears, move the pointer over the profile
picture, and click **User Information**.
3. In the **AccessKey** section, view the AccessKey pair of your personal account.

> **Note:** An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair provides full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. On the right side of the page that appears, click **Management AccessKey**.
6. In the message that appears, view the AccessKey pair of the organization.

### 1.3 Obtain the values of common header parameters

**header parameters**

You must provide multiple header parameters when you call API operations in Apsara Stack. This topic describes how to obtain the values of common header parameters. This topic also explains the response parameters that are returned after you call API operations.

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. On the Regions page, find the organization that you want to view and click its name in the
organization tree.
5. In the **Regions** list, obtain the region ID from the **Region Name** column.

**Obtain an organization ID**

You must call a specific API operation to obtain the organization ID. You can obtain the organization ID by using the online debugging feature in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI**
**Explorer**.
3. In the top navigation bar of the **OpenAPI Explorer** page, choose **API Integration** > **API**
**Debugging**.
4. Move the pointer over the
icon and choose **Platform** > **Apsara Uni-manager**. Select
**2019-05-10** from the **Version** drop-down list.
5. Search for the `GetOrganizationList` operation and debug the operation online. Set the
name parameter to the name of the organization that you want to query and click Initiate Call. Obtain the organization ID from the **id** parameter on the **Call Result** tab. For more information about this operation, see the GetOrganizationList section of Apsara Uni-manage r Operations Console Developer Guide.

**Obtain a resource set ID**

You must call a specific API operation to obtain the resource set ID. You can obtain the resource set ID by using the online debugging feature in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI**
**Explorer**.
3. In the top navigation bar of the **OpenAPI Explorer** page, choose **API Integration** > **API**
**Debugging**.
4. Move the pointer over the
icon and choose **Platform** > **Apsara Uni-manager**. Select
**2019-05-10** from the **Version** drop-down list.
5. Search for the `ListResourceGroup` operation and debug the operation online. Obtain the
resource set ID from the **id** parameter on the **Call Result** tab. For more information about this operation, see the ListResourceGroup section of Apsara Uni-manager Operations Console Developer Guide.

**Obtain an instance ID**

You can obtain the ID of an instance in the cloud service console of the Apsara Uni-manager Management Console. For example, to obtain the ID of an API gateway, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > Application Services > API Gateway.
3. In the left-side navigation pane, click **Instances**.
4. View the **instance ID** in the instance list.
The following table describes the additional response parameters that are returned by default when you call API operations to query the instances of Apsara Stack services.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of an organization. |

### 1.4 Obtain access credentials assigned by STS

**assigned by STS**

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

STS allows you to manage temporary access credentials for your Apsara Stack resources. You can use STS to call API operations.

**Procedure**

1. Obtain the Apsara Stack Resource Name (ARN) of your `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. In the upper-right corner of the homepage, click the profile picture and then click **User**
**Information**.
iii. On the page that appears, click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view the ARN of your `RAM role` .
2. Use the following code to obtain an AccessKey ID ( `stsAK` ), an AccessKey secret
( `stsSK` ), and an STS token ( `stsToken` ) by assuming the `RAM role` .

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
     // Specify the description of the call source.
        asClient.setSdkSource("test");
     // Specify the ARN.
        String assumeRole = AssumeRole(asClient, "<RAM Role>");
        JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
        JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
        // Obtain the access credentials assigned by STS.
        String stsAK = credentials.getString("AccessKeyId");
        String stsSK = credentials.getString("AccessKeySecret");
        String stsToken = credentials.getString("SecurityToken");
```

`}`

```
public static String AssumeRole(ASClient asClient, String roleArn) {
        Map<String, String> headers = new HashMap<>();
        Map<String, Object> reqParams = new HashMap<>();
        reqParams.put("action", "AssumeRole");
        reqParams.put("Product", "Sts");
        reqParams.put("Version", "2015-04-01");
        reqParams.put("regionId", regionId);
     // The AccessKey ID of the current user.
        reqParams.put("AccessKeyId", <The AccessKey ID of the current user>);
     // The AccessKey secret of the current user.
        reqParams.put("AccessKeySecret", <The AccessKey secret of the current user>);
        reqParams.put("roleSessionName", "StsUser");
        reqParams.put("roleArn", roleArn);
        return asClient.doRequest(endpoint, headers, reqParams);
```

`}`
3. Use the access credentials assigned by STS to call an API operation of a cloud service. In
this example, an operation of Elastic Compute Service (ECS) is called.

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
        asClient.setSdkSource("test");
  // Call an API operation of ECS.
        String ecsRes = DescribeZones(asClient,<stsAK>,<stsSK>,<stsToken>);
```

`}`

```
public static String DescribeZones(ASClient asClient, String stsAK, String stsSK, Str ing stsToken) {
        Map<String, String> headers = new HashMap<>();
        Map<String, Object> reqParams = new HashMap<>();
        reqParams.put("action", "DescribeZones");
        reqParams.put("Product", "Ecs");
        reqParams.put("Version", "2014-05-26");
        reqParams.put("regionId", "<your-RegionID>");
        // Specify the AccessKey ID, AccessKey secret, and STS token.
        reqParams.put("AccessKeyId", <stsAK>);
        reqParams.put("AccessKeySecret", <stsSK>);
        reqParams.put("SecurityToken", <stsToken>);
        return asClient.doRequest(endpoint, headers, reqParams, HttpMethod.GET);
```

`}`

### 1.5 Obtain the endpoint of Message Queue for Apache RocketMQ

**Message Queue for Apache**

**RocketMQ**

This topic describes how to obtain the endpoint of RocketMQ. To use the POP gateway to call the API operations of an Apsara Stack service, you must specify the endpoint of the Apsara Stack service. You can contact an onsite O&M engineer of Apsara Stack to obtain a service endpoint. You can also use the method provided in this topic to obtain a service endpoint.

**Procedure**

1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Platforms > Apsara Infrastructure**
**Management Framework**.
2. In the left-side navigation pane, click **Reports**.
`Registration Vars of Services`. In the report list that
3. On the **All Reports** page, search for
appears, click the name of the report. `mq`.
4. On the **Registration Vars of Services** page, click
next to **Service** and search for
5. Find the **mq-console** service, right-click the **Service Registration** column, and then
select **Show More** from the shortcut menu. On the **Details** page, the value of the **ons_innerapi_endpoint** parameter indicates the endpoint of RocketMQ.

## 2 API reference

### 2.1 RocketMQ_API

#### 2.1.1 Updates

This topic describes the updates of Message Queue for Apache RocketMQ from V3.8.0 to V3.8.1 to help you get started with the updated version.

**Optimization of resource isolation by instance**

Message Queue for Apache RocketMQ provides instances for multi-tenancy isolation. Each user can purchase multiple instances and logically isolate them from each other. To ensure the compatibility with the existing resources of existing users, Message Queue for Apache RocketMQ provides the following types of instances and namespaces: Default instances, which are compatible with the existing resources of existing users This type of instance has no separate namespace. Resource names must be globally unique within and across all instances. By default, an instance without a namespace is automatically generated for the existing resources of each existing user. If no existing resources are available, you can create at most one instance without a namespace. You can configure the endpoint, which can be obtained from the **Instances** page in the Message Queue for Apache RocketMQ console.

```
// Recommended configuration: properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxxx"); // Compatible configuration, which is not recommended. We recommend that you update this configuration to the recommended configuration: properties.put(PropertyKeyConst.ONSAddr, "xxxx");
```

New instances A new instance has a separate namespace. Resource names must be unique within an instance but can be the same across different instances. You can configure the endpoint, which can be obtained from the **Instances** page in the Message Queue for Apache RocketMQ console.

```
// Recommended configuration: properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxx");
```

A RocketMQ client must be updated to the following latest versions for different programming languages: Java: V1.8.7.1.Final C and C++: V2.0.0 .NET: V1.1.3

**Optimization of resource application**

Previously, Message Queue for Apache RocketMQ resources consisted of topics, producer IDs, and consumer IDs. Each two of the resources have a many-to-many relationship, which was difficult to comprehend. Each time you created a topic, you must associate the topic with a producer ID and a consumer ID. This process was too complex for medium- and large-sized enterprise customers. To optimize user experience and help new users get started, the resource application process has been simplified. The resource application process has been optimized in the following aspects: Topic management, which is unchanged You need to apply for a topic. A topic is used to classify messages. It is the primary classifier. You do not need to apply for a producer ID. Producer IDs and consumer IDs are integrated into group IDs. In the Message Queue for Apache RocketMQ console, the Producers module has been removed. The Producers and Consumers modules have been integrated into the Groups module. You do not need to associate a producer ID or consumer ID with a topic. Instead, you need only to apply for a group ID and associate it with a topic in the code. Compatibility: The list of producer IDs is no longer displayed. This does not affect the current services. The consumer IDs that start with CID- or CID_ and that you have applied for can still be used and can be set in the **PropertyKeyConst.ConsumerId** or
**PropertyKeyConst.GROUP_ID** parameter of the code.
Sample code

> **Note:** We recommend that you update a RocketMQ client to the following latest versions for different programming languages:

Java: V1.8.7.1.Final C and C++: V2.0.0 .NET: V1.1.3

> Existing producer IDs or consumer IDs can still be used and do not affect the current services. However, we recommend that you update your instance configuration to the recommended configuration.

Recommended configuration: Integrate producer IDs and consumer IDs into group IDs.

```
// Set the PropertyKeyConst.GROUP_ID parameter. The original PropertyKeyConst.ProducerId and PropertyKeyConst.ConsumerId parameters are deprecat ed. properties.put(PropertyKeyConst.GROUP_ID, "The original CID-XXX or the GID-XXX");
```

Compatible configuration: Use a producer ID to identify a producer and a consumer ID to identify a consumer.

```
// When you create a producer, you must set the PropertyKeyConst.ProducerId paramet er. properties.put(PropertyKeyConst.ProducerId, "The original PID-XXX or the GID-XXX"); // When you create a consumer, you must set the PropertyKeyConst.ConsumerId paramet er. properties.put(PropertyKeyConst.ConsumerId, "The original CID-XXX or the GID-XXX");
```

#### 2.1.2 Overview

##### 2.1.2.1 Intended audience and scenarios

Message Queue for Apache RocketMQ provides you with API operations to help you manage resources. Different from the SDKs for production, API operations are used to manage the resources of Message Queue for Apache RocketMQ, such as topics and group IDs. API operations are intended for those who: Are familiar with the main features of the Message Queue for Apache RocketMQ console. Require a management and control tool similar to the console and have a need for custom management and control features.

##### 2.1.2.2 Scenarios and limits

1. Due to the implementation principles of API operations, the caller must be able to access
the domain name of the Message Queue for Apache RocketMQ console. Otherwise, the call may fail.
2. The underlying layer of API operations is based on HTTP, with average performance and
efficiency. Therefore, API operations are applicable only to management and control scenarios. Do not use them in mass production scenarios with high concurrency.

##### 2.1.2.3 Basic principles

The underlying layer of API operations provides services based on HTTP. Each time you call an API operation, you send an HTTP request from the HTTP client to the backend service of Message Queue for Apache RocketMQ for execution. You can encapsulate parameters in an HTTP request and send the request to call an API operation. The execution results are returned in a response. The request and response are encoded in UTF-8. The service endpoint in the HTTP request is the domain name of the Message Queue for Apache RocketMQ console.

#### 2.1.3 Common parameters

##### 2.1.3.1 Common request parameters

The HTTP client calls Message Queue for Apache RocketMQ API operations based on HTTPS. Common request parameters must be included in all API requests and sent to the backend service of Message Queue for Apache RocketMQ for permission verification. The following table describes common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| accesskey _ | String | Yes | The AccessKey ID of your account. |
| preventCache __ | Long | Yes | The parameter that is used for cross-site request forgery (CSRF) verification. Set this parameter to the current system time. Unit: milliseconds. |

| regionId _ | String | Yes (except for the operation that is used to query region IDs) | The ID of the current region. |
|---|---|---|---|
| signature _ | String | Yes | The signature string of the request. |

The **_********** parameter must specify the region where you want to manage resources. The default value is mq-private for private domains and Apsara Stack. The **_*********** parameter specifies the signature string that is obtained from signature calculation. During signature calculation, other parameters in the HTTPS request are arranged to create a string-to-sign. Then, the string-to-sign is calculated and signed based on the AccessKey secret of your account.

**Signature calculation example**

Assume that the original HTTPS request is:

```
https://mq.console.${global:internet-domain}/json/topic/create
```

> **Note:** To access the region in single-region deployment or access the central region in multi- region deployment, use ${global:internet-domain} to specify the domain name to be accessed. To access a regular region in multi-region deployment, use ${global:region}.${global:internet-domain} to specify the domain name to be accessed.

The request contains the following parameters, including common parameters and operationspecific parameters:

**Key_2=Value_2&Key_1=Value_1&Key_3=Value_3**

Then, the original request URL is:

```
https://mq.console.${global:internet-domain}/json/topic/create? Key_2=Value_2&Key_1=Value_1&Key_3=Value_3
```

Sort the keys **Key_2, Key_1, and Key_3** in alphabetical order and connect the corresponding values in the same order to form a string. The sorting result of the keys is Key_1, Key_2, Key_3 and the value string is Value1Value2Value3. Then, the string-to-sign is Value1Value2Value3. Use the AccessKey secret of your account to sign the string-to-sign by using the HMAC-SHA1 algorithm. Then, the signature string is obtained. Function libraries are available for the implementation of the HMAC algorithm in different programming languages. You can search for one as required. For example, the following method can be used in Linux:

```
echo -n 'Value1Value2Value3' | openssl dgst -hmac 'Your AccessKey secret' -sha1 -binary
| base64
```

Assume that the final result is: eqweq+adwe23****=. Replace "+" with "%2B", "=" with "%3D", and "/" with "%2F" by using curl commands. Otherwise, an authentication failure is reported after the characters are automatically escaped. The signed HTTPS request is:

```
https://mq.console.${global:internet-domain}/json/topic/create? Key_2=Value_2&Key_1=Value_1&Key_3=Value_3&_signature= eqweq%2Badwe23****%3D
```

##### 2.1.3.2 Common response parameters

The HTTP client sends an HTTP request to the backend service of Message Queue for Apache RocketMQ. The backend service processes the request and then returns results in an HTTP response to the client in the same way. In normal cases, the HTTP status code is 200 in the response. The returned content is contained in the body as a JSON string. The client needs to parse the JSON string to determine whether the call is successful. JSON format: `{`

```json
    "code": 200,
    "currentPage": 0,
    "data": { },
    "dynamicCode": "",
    "dynamicMessage": "",
    "message": "operation success",
    "pageSize": 0,
    "requestId": "",
    "status": "SUCCESS",
    "success": true,
    "total": 0
```

`}` Response parameters: code: the HTTP status code. A value of 200 indicates that the call is successful. Other values indicate that the call fails. currentPage: the page number of the returned page if the request is a paged query. dynamicMessage: the error message. message: the processing result. pageSize: the number of entries returned per page if the request is a paged query. success: indicates whether the call is successful. data: the returned service data. The value is also a JSON string. If the return results of the current request contain service data, you must reverse parse the content in the JSON format. RequestId: the unique ID of the request. The value is a string.

#### 2.1.4 Common terms

##### 2.1.4.1 Account security

###### 2.1.4.1.1 AccessKey

The AccessKey ID of the account that you use to access Alibaba Cloud services. You can obtain your AccessKey ID from the console. When you call an API operation, the AccessKey ID is included in the API request and sent to the backend service of Message Queue for Apache RocketMQ for identity authentication. You can call Message Queue for Apache RocketMQ API operations to manage resources only within your account.

###### 2.1.4.1.2 SecretKey

The AccessKey secret of the account that you use to access Alibaba Cloud services. You can obtain your AccessKey secret from the console. When you call an API operation, the AccessKey secret is included in the API request and used to calculate the signature string of the API request. The backend service of Message Queue for Apache RocketMQ uses the AccessKey secret to verify the signature string of the API request for authentication.

##### 2.1.4.2 Resource management

###### 2.1.4.2.1 Topic

A classifier that is used to classify messages. Messages in Message Queue for Apache RocketMQ are stored by topic. Topics are among the most important resources in Message Queue for Apache RocketMQ. In Message Queue for Apache RocketMQ, topics are globally unique.

###### 2.1.4.2.2 Group ID

The ID of a group. A group consists of producers or consumers that produce or consume messages of the same type and publish or subscribe to messages based on the same logic. If group IDs for consumers or existing consumer IDs are created by a RAM user, both the RAM user and the Apsara Stack tenant account to which the RAM user belongs have permissions on these resources. If group IDs for consumers or existing consumer IDs are created by an Apsara Stack tenant account, only the Apsara Stack tenant account has permissions on these resources. Its RAM users have no permissions on these resources. For more information about the changes in the use of existing producer IDs, existing consumer IDs, and group IDs, see Updates.

#### 2.1.5 Error codes

If a Message Queue for Apache RocketMQ API operation is successfully called, HTTP status code 200 is returned to the client. If the call fails, error codes and descriptions are returned. You can find solutions based on the error codes that are described in the following table.

| Error code | Problem description and cause | Solution |
|---|---|---|
| ONS SYSTEM ERROR _ _ | An error has occurred at the backend of Message Queue for Apache RocketMQ. | Submit a ticket to contact the technical support staff of Message Queue for Apache RocketMQ. |

| ONS SERVICE UNSUPPORTED _ _ | The API operation is not supported in the specified region. | Contact the technical support staff of Message Queue for Apache RocketMQ to confirm whether the operation is supported. |
|---|---|---|
| ONS INVOKE ERROR _ _ | The API operation failed to be called. | Contact the technical support staff of Message Queue for Apache RocketMQ. |
| BIZ FIELD CHECK INVALID _ _ _ | Parameters failed the verification. | Check whether the specified request parameters are valid based on the API reference. |
| BIZ TOPIC NOT FOUND _ _ _ | The topic does not exist. | Check whether the specified topic is valid or whether the topic is created. |
| BIZ SUBSCRIPTION NOT FOUND _ _ _ | The group ID of the subscription does not exist. | Check whether the group ID is created or whether the query conditions are valid. |
| BIZ PUBLISHER EXISTED _ _ | The specified group ID already exists. | Use a new group ID and try again. |
| BIZ SUBSCRIPTION EXISTED _ _ | The specified group ID already exists. | Use a new group ID and try again. |
| BIZ CONSUMER NOT ONLINE _ _ _ | The consumer that is identified by the specified group ID is offline. | Ensure that the consumer is online and try again. |
| BIZ NO MESSAGE _ _ | No messages match the query conditions. | Check the query conditions and check whether messages are sent based on the query conditions. |
| BIZ REGION NOT FOUND _ _ _ | The requested region does not exist. | Check whether the specified region ID is valid. |
| BIZ TOPIC EXISTED _ _ | The specified topic already exists. | Use a new topic name and try again. |
| BIZ PRODUCER ID BELONG TO OTHER US _ _ _ _ _ _ ER | The specified group ID is occupied by another user. | Use a new group ID and try again. |
| BIZ CONSUMER ID BELONG TO OTHER US _ _ _ _ _ _ ER | The specified group ID is occupied by another user. | Use a new group ID and try again. |

| BIZ PUBLISH INFO NOT FOUND _ _ _ _ | The requested group ID does not exist. | Check whether the group ID exists or whether the query conditions are valid. |
|---|---|---|
| EMPOWER EXIST ERROR _ _ | The specified authorization already exists. | Check the request parameters and try again or query the authorization first. |
| EMPOWER OWNER CHECK ERROR _ _ _ | The current user is not the owner of the authorized topic. | Check the ownership of the resource. |

#### 2.1.6 API reference

##### 2.1.6.1 Region management

###### 2.1.6.1.1. /json/region/list

Queries region IDs. The queried region IDs are used as the value of the common request parameter _regionId for other operations.

**Scenarios**

You can call this operation to query region IDs. The queried region IDs are used as the value of the common request parameter _regionId for other operations. For more information about common request parameters, see Common request parameters. For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | List(RegionDo) | The query results. |

| Parameter | Type | Description |
|---|---|---|
| id | Long | The number in the database. |
| regionId | String | The ID of the region. Example: cn-hangzhou. |
| regionName | String | The name of the region. Example: China (Hangzhou). |

##### 2.1.6.2 Cluster management

###### 2.1.6.2.1. /json/cluster/list

Queries clusters. When you create an instance, you must use a cluster name to specify the relationship between the instance and the cluster. You can call this operation to query cluster names. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| regionId _ | String | Yes | The ID of the region where you want to query clusters. |

For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | List<ClusterInfoDo> | The query results. |

**ClusterInfoDo**

| Parameter | Type | Description |
|---|---|---|
| regionId | String | The ID of the region where the cluster resides. |
| cluster | String | The name of the cluster. |
| createTime | String | The time when the cluster was created. |
| modifyTime | String | The last time when the cluster was modified. |

##### 2.1.6.3 Instance management

###### 2.1.6.3.1. /json/vpcTunnel/tunnelSwitch

Switches the network access mode for virtual private clouds (VPCs) in a cluster and applies for a virtual IP address (VIP) in the specified access mode for RocketMQ brokers and RocketMQ Name Servers in the cluster.

**Scenarios**

An instance provides two network access modes for VPCs: Single Tunnel and Any Tunnel.
**Important notes**:
The network access mode for VPCs is switched in a specified cluster. This affects all topics in which messages are being sent and received in the cluster. Therefore, check the impact scope before you call this operation. After the network access mode for VPCs is switched in a cluster, change the configuration of all clients that are connected to the cluster to the return value of this operation: properties.put(PropertyKeyConst.NAMESRV_ADDR,"Return value"); For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| tunnelType | String | Yes | The network access mode for VPCs. Valid values: anyTunnel and singleTunnel. |
| instanceId | String | Yes | The ID of the instance whose network access mode for VPCs you want to switch. |
| slbUrl | String | No | The endpoint of the Server Load Balancer (SLB) API. |
| force | Boolean | No | Specifies whether to forcibly switch the network access mode for VPCs. A value of true indicates that the network access mode for VPCs is forcibly switched regardless of whether RocketMQ brokers are processing messages in the cluster. A value of false indicates that the switching is blocked if the sum of the transactions per second (TPS) for receiving messages and the TPS for sending messages is greater than 10 on a single RocketMQ broker. Default value: false. |
| vSwitchId | String | No | The VPC in which the VIP in Single Tunnel mode is created. This parameter takes effect only when the tunnelType parameter is set to singleTunnel. If you have only one VPC or the tunnelType parameter is set to anyTunnel, this parameter can be left unspecified. |

The VIP of RocketMQ Name Servers is returned in the JSON format. You must change the configuration of all clients that are connected to the cluster to properties.put(PropertyKeyConst.NAMESRV_ADDR,"Return value");. Then, restart your application to make the configuration take effect.

###### 2.1.6.3.2. /json/instance/baseInfo

Queries the basic information about an instance, including the endpoints for sending and receiving messages. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance. |

For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| InstanceBaseInfo | InstanceBaseInfo | The information about the instance. |

**InstanceBaseInfo**

| Parameter | Type | Description |
|---|---|---|
| instanceId | String | The ID of the instance. |
| instanceName | String | The name of the instance. |
| independentNaming | Boolean | Indicates whether the instance has a namespace. Valid values: true: The instance has a separate namespace. Resource names must be unique within an instance but can be the same across different instances. false: The instance has no separate namespace. Resource names must be globally unique within and across all instances. You can view the information about the namespace on the Instance Details page in the Message Queue for Apache RocketMQ console. For more information about namespaces, see Updates. |

| Endpoints | Endpoints | The endpoints for various protocols. |
|---|---|---|
| maxSendTps | Long | The maximum TPS for sending messages in the instance. |
| maxReceiveTps | Long | The maximum TPS for receiving messages in the instance. |
| topicCapacity | Integer | The maximum number of topics that can be created in the instance. |

**Endpoints**

| Parameter | Type | Required | Description |
|---|---|---|---|
| tcpEndpoint | String | No | The Message Queue for Apache RocketMQ endpoint for TCP. |

###### 2.1.6.3.3. /json/instance/create

Creates an instance.

> **Note:** By default, you must use your Apsara Stack tenant account to call this operation. RAM users can call this operation only after they are authorized.
> A region can contain up to 500 instances.
> The name of an instance must be unique in the region where the instance is deployed.

For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| cluster | String | Yes | The cluster in which you want to create the instance. |
| instanceName | String | Yes | The name of the instance. The name must be 3 to 64 characters in length. |

| independentNaming | Boolean | Yes | Specifies whether the instance has a namespace. Valid values: true: The instance has a separate namespace. Resource names must be unique within an instance but can be the same across different instances. false: The instance has no separate namespace. Resource names must be globally unique within and across all instances. You can view the information about the namespace on the Instance Details page in the Message Queue for Apache RocketMQ console. For more information about namespaces, see Updates. |
|---|---|---|---|
| remark | String | No | The description of the instance. You can leave this parameter unspecified. |
| maxSendTps | Long | Yes | The maximum TPS for sending messages in the instance. |
| maxReceiveTps | Long | Yes | The maximum TPS for receiving messages in the instance. |
| topicCapacity | Integer | No | The maximum number of topics that can be created in the instance. |

For more information about common response parameters, see Common response parameters.

###### 2.1.6.3.4. /json/instance/delete

Deletes an instance.

> **Note:** By default, you must use your Apsara Stack tenant account to call this operation. RAM users can call this operation only after they are authorized.
> An instance can be deleted only when it has no topics or group IDs.

For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance. |

For more information about common response parameters, see Common response parameters.

###### 2.1.6.3.5. /json/instance/list

Queries all instances in the current environment.

**Scenarios**

You can call this operation to query the information about all instances for instance management. For more information about common request parameters, see Common request parameters. For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | List(InstanceVO) | The information about all existing instances. |

| Parameter | Type | Description |
|---|---|---|
| instanceId | String | The ID of the instance. |
| instanceName | String | The name of the instance. |

| namespaceRulesType | Boolean | Indicates whether the instance has a namespace. Valid values: true: The instance has a separate namespace. Resource names must be unique within an instance but can be the same across different instances. false: The instance has no separate namespace. Resource names must be globally unique within and across all instances. You can view the information about the namespace on the Instance Details page in the Message Queue for Apache RocketMQ console. For more information about namespaces, see Updates. |
|---|---|---|

###### 2.1.6.3.6. /json/instance/update

Updates the name and description of an instance.

> **Note:** By default, you must use your Apsara Stack tenant account to call this operation. RAM users can call this operation only after they are authorized.
> A region can contain up to 500 instances.
> The name of an instance must be unique in the region where the instance is deployed.

For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance. |
| instanceName | String | No | The name of the instance. The name must be 3 to 64 characters in length. If you do not specify this parameter, the name of the instance is not updated. Note The instance name must be unique in a region. |

| remark | String | No | The description of the instance. If you do not specify this parameter, the description of the instance is not updated. |
|---|---|---|---|

For more information about common response parameters, see Common response parameters.

##### 2.1.6.4 Topic management

###### 2.1.6.4.1. /json/topic/create

Creates a topic in a region.

**Scenarios**

You can call this operation when new topics are required to publish new applications or implement service logic. By default, you must use your Apsara Stack tenant account to call this operation. RAM users can call this operation only after they are authorized. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|

| topic | String | Yes | The name of the topic that you want to create. Note CID and GID are the reserved fields of a group ID. A topic name cannot start with CID or GID. If a namespace is configured for the instance where you want to create the topic, the topic name must be unique within the instance but can be the same as topic names in other instances. If no namespace is configured for the instance where you want to create the topic, the topic name must be globally unique within the instance and across instances and regions. |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance where the topic you want to create resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| orderType | Integer | Yes | The type of message in the topic. Note 0: regular message 1: partitionally ordered message 2: globally ordered message 4: transactional message 5: scheduled or delayed message |
| remark | String | No | The description of the topic. You can leave this parameter unspecified. |

For more information about common response parameters, see Common response parameters.

**Examples**

Signature calculation method for the _signature parameter. For more information, see Common request parameters. Example:

```
echo -n '1498029701000ACCESSKEY_XXXonsConsolemq-privateTOPIC_XXX' | openssl dgst -hmac 'SECRETKET_XXX' -sha1 -binary | base64
```

Call method:

```bash
curl http://mq.console.example.com//json/topic/create? _accesskey=ACCESSKEY_XXX&__preventCache=1498029701000&_platform=onsConsole&_regionId=mqprivate&topic=TOPIC_XXX&_signature=8DqV%2BrOBzOd0M2SNj3Acuqn****%3D
```

> **Note:** Contact an administrator to obtain the project-specific domain name, and replace example.com with the actual domain name.

Sample response:

```json
{"code":200,"currentPage":0,"data": {},"dynamicCode":"","dynamicMessage":"","helpUrl":null,"message":"operation success","pageSize":0,"requestId":"","status":"SUCCESS","success":true,"total":0}
```

###### 2.1.6.4.2. /json/topic/delete

Deletes a topic within your account.

**Scenarios**

You can call this operation when you need to recycle resources. For example, when applications are deleted, you need to recycle relevant resources. After a topic is deleted, the backend of Message Queue for Apache RocketMQ recycles the resources of the topic. This process is time-consuming. Therefore, we recommend that you do not create a topic immediately after you delete one. If a topic fails to be deleted, troubleshoot the issue based on the returned error code.

> **Important:** The operation to delete a topic results in the cleanup of all subscriptions under the topic. Proceed with caution.

For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| topic | String | Yes | The name of the topic that you want to delete. |

| instanceId | String | Yes | The ID of the instance where the topic you want to delete resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
|---|---|---|---|

For more information about common response parameters, see Common response parameters.

###### 2.1.6.4.3. /json/topic/get

Queries a topic.

**Scenarios**

You can call this operation to query the basic information about a topic, such as the owner and status. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| topic | String | Yes | The name of the topic that you want to query. |
| instanceId | String | Yes | The ID of the instance where the topic you want to query resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |

For more information about common response parameters, see Common response parameters.

###### 2.1.6.4.4. /json/topic/listInPage

Queries one or more topics within your account by page.

**Scenarios**

You can call this operation to query the information about one or more topics within your account by page. You can call the listNames operation to query the names of all topics, and then call this operation to query the detailed information about topics. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| search | String | No | The name of the topic that you want to query. |
| currentPage | Integer | No | The number of the page to return. Default value: 1. |
| pageSize | Integer | No | The number of topics to return on each page. Default value: 20. |
| instanceId | String | Yes | The ID of the instance for which you want to query topics. |

The specified number of topics on the specified page is returned in the JSON format.

###### 2.1.6.4.5. /json/topic/update

Configures the read/write mode for a topic.

**Scenarios**

By default, you must use your Apsara Stack tenant account to call this operation. RAM users can call this operation only after they are authorized. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance where the topic you want to configure resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |

| topic | String | Yes | The name of the topic that you want to configure. A topic name must be unique within your account even across different regions. |
|---|---|---|---|
| perm | Integer | Yes | The read/write mode that you want to configure for the topic. Valid values: 6: Both read and write operations are supported. 4: Write operations are prohibited. 2: Read operations are prohibited. |

For more information about common response parameters, see Common response parameters.

###### 2.1.6.4.6. /json/topic/listNames

Queries the names of all topics within your account. You can use this operation together with the listInPage operation to query the detailed information about all topics.

**Scenarios**

You can call this operation to query the names of all topics within your account. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance for which you want to query the names of topics. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |

The names of all topics that are created within your account are returned in the JSON format.

###### 2.1.6.4.7. /json/topic/subDetail

Queries the online consumer groups that have subscribed to a topic.

**q**

**p**

For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance where the topic you want to query resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| topic | String | Yes | The name of the topic that you want to query. |

For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | Data | The returned data. |

**Data**

| Parameter | Type | Description |
|---|---|---|
| topic | String | The name of the topic. |
| SubscriptionDataList | List<SubscriptionDataListItem> | The information about online consumer groups. |

**SubscriptionDataListItem**

| Parameter | Type | Description |
|---|---|---|
| groupId | String | The ID of the group that has subscribed to the topic. |
| subString | String | The subscription string. |
| messageModel | String | The consumption mode. Valid values: CLUSTERING: clustering consumption BROADCASTING: broadcasting consumption |

##### 2.1.6.5 Group management

###### 2.1.6.5.1. /json/group/create

Creates a group ID.

**Usage notes**

When you call this operation, take note of the following items: If group IDs for consumers or existing consumer IDs are created by a RAM user, both the RAM user and the Apsara Stack tenant account to which the RAM user belongs have permissions on these resources. If group IDs for consumers or existing consumer IDs are created by an Apsara Stack tenant account, only the Apsara Stack tenant account has permissions on these resources. Its RAM users have no permissions on these resources. For more information about the changes in the use of existing producer IDs, existing consumer IDs, and group IDs, see Updates. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance where the group ID you want to create resides. |
| groupId | String | Yes | The group ID that you want to create. Take note of the following items: The group ID must start with GID or _ GID- and can contain letters, digits, hyphens (-), and underscores ( ). _ The group ID must be 5 to 64 characters in length. Note The group ID cannot be modified after it is created. |
| remark | String | No | The description of the group ID. |

For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|

| remark | String | The description of the group ID. |
|---|---|---|

###### 2.1.6.5.2. /json/group/delete

Deletes a group ID that is created after you call the /json/group/create operation. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance where the group ID you want to delete resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| groupId | String | Yes | The group ID that you want to delete. |

For more information about common response parameters, see Common response parameters.

###### 2.1.6.5.3. /json/group/list

Queries one or more group IDs. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|

| instanceId | String | Yes | The ID of the instance for which you want to query group IDs. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
|---|---|---|---|
| groupId | String | No | The group ID that you want to query. If you do not specify this parameter, all group IDs are queried. |

For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | List(SubscribeInfoDo) | The subscription information. |

**SubscribeInfoDo**

| Parameter | Type | Description |
|---|---|---|
| owner | String | The owner of the group ID. |
| instanceId | String | The ID of the instance. |
| groupId | String | The ID of the consumer group. |

| independentNaming | Boolean | Indicates whether the instance has a namespace. Valid values: true: The instance has a separate namespace. Resource names must be unique within an instance but can be the same across different instances. false: The instance has no separate namespace. Resource names must be globally unique within and across all instances. You can view the information about the namespace on the Instance Details page in the Message Queue for Apache RocketMQ console. For more information about namespaces, see Updates. |
|---|---|---|
| remark | String | The description of the group ID. |

###### 2.1.6.5.4. /json/group/subDetail

Queries the topics to which a group has subscribed. No data can be queried if the group is offline. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance where the group ID you want to query resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| groupId | String | Yes | The group ID that you want to query. |

For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | Data | The returned data. |

**Data**

| Parameter | Type | Description |
|---|---|---|
| groupId | String | The group ID that you queried. |
| online | Boolean | Indicates whether the group was online. |
| messageModel | String | The consumption mode. Valid values: CLUSTERING: clustering consumption BROADCASTING: broadcasting consumption |
| SubscriptionDataList | List<SubscriptionDataListItem> | The information about topics. No data can be queried if the group was offline. |

**SubscriptionDataListItem**

| Parameter | Type | Description |
|---|---|---|
| topic | String | The name of the topic. |
| subString | String | The subscription string. |

###### 2.1.6.5.5. /json/group/consumerUpdate

Configures the read permissions on messages for a consumer group that is identified by a group ID. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|

| instanceId | String | Yes | The ID of the instance where the group ID you want to configure resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
|---|---|---|---|
| groupId | String | Yes | The group ID for which you want to configure the read permissions on messages. |
| readEnable | Boolean | Yes | Specifies whether to grant the read permissions on messages. |

For more information about common response parameters, see Common response parameters.

##### 2.1.6.6 Consumption management

###### 2.1.6.6.1. /json/consumer/accumulate

Queries the message accumulation of a consumer group. The queried information includes the number of unconsumed messages and the consumption latency of the consumer group.

**Scenarios**

You can call this operation to query the information about message accumulation in the production environment where you need to know the consumption progress of consumer groups. You can use the queried information to analyze message consumption and consumption latency. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|

| instanceId | String | Yes | The ID of the instance where the group ID you want to query resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
|---|---|---|---|
| groupId | String | Yes | The group ID that you want to query. |
| detail | Boolean | No | Specifies whether to query the detailed information about message accumulation, including the message accumulation details of each queue. |

For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | Data | The information about message accumulation. |

**Data**

| Parameter | Type | Description |
|---|---|---|
| onLine | Boolean | Indicates whether the group was online. The group was online if one of the consumer instances that are identified by the group ID was online. Valid values: true: online false: offline |
| totalDiff | Long | The total number of accumulated messages in all the topics to which the group has subscribed. |
| consumeTps | Float | The total TPS for the messages that were received by the consumer instances that are identified by the group ID. |
| lastTimestamp | Long | The production time of the last message that was consumed by the consumer instances that are identified by the group ID. |
| delayTime | Long | The maximum message consumption latency of the consumer instances that are identified by the group ID. |

| DetailInTopicList | List(OnsConsumerAccumulateR esponse.Data.DetailInTopicDo) | The detailed information about topics. |
|---|---|---|

**DetailInTopicList**

| Parameter | Type | Description |
|---|---|---|
| topic | String | The name of the topic. |
| totalDiff | Long | The number of accumulated messages in the topic. |
| lastTimestamp | Long | The production time of the last message that was consumed in the topic. |
| delayTime | Long | The maximum consumption latency of messages in the topic. |

###### 2.1.6.6.2. /json/consumer/status

Queries the detailed information about a group ID, including the subscription consistency, consumption TPS, load balancing, and consumer connection status.

**Scenarios**

> **Important:** You can call this operation to troubleshoot abnormal consumption after you confirm whether messages are accumulated and whether consumers are online. You can check whether subscriptions are consistent for a group ID and whether load balancing is normal, and query the jstack information of online consumers.
> This operation uses a lot of backend methods for data aggregation. Therefore, the system responds slowly. We recommend that you do not frequently call this operation.

For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance where the group ID you want to query resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| groupId | String | Yes | The group ID that you want to query. |

| detail | Boolean | No | Specifies whether to query detailed information. Valid values: true: queries detailed information. You can obtain the detailed information from the ConsumerConnectionInfoList and DetailInTopicList parameters in the response. false: does not query detailed information. The ConsumerConnectionInfoList and DetailInTopicList parameters are empty in the response. Default value: false. |
|---|---|---|---|
| needJstack | Boolean | No | Specifies whether to display jstack information. Valid values: true: displays jstack information. You can obtain the jstack information from the Jstack parameter in the response. false: does not display jstack information. The Jstack parameter is empty in the response. Default value: false. Note If you need to display jstack information, make sure that the detail parameter in the request is set to true. |

For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | ConsumerStatusDo | The query results. |

**ConsumerStatusDo**

| Parameter | Type | Description |
|---|---|---|
| online | Boolean | Indicates whether the group was online. |
| totalDiff | Long | The total number of accumulated messages in the consumer group. |
| consumeTps | Long | The total consumption TPS. |
| lastTimestamp | Long | The latest consumption time. |
| delayTime | Long | The consumption latency. |
| consumeModel | Long | The consumption mode. |

| subscriptionSame | Boolean | Indicates whether subscriptions were consistent. |
|---|---|---|
| rebalanceOK | Boolean | Indicates whether load balancing was normal. Valid values: true: normal false: abnormal |
| ConnectionSet | List(ConnectionDo) | The information about online consumers in the consumer group. |
| DetailInTopicList | List(DetailInTopicDo) | The consumption status of topics. If you need to query detailed information, make sure that the detail parameter in the request is set to true. Otherwise, the return value of this parameter is empty. |
| ConsumerConnectionInfoList | List(ConsumerConnectionInfoD o) | The detailed information about online consumers in the consumer group, including the jstack information and consumption response time (RT). If you need to query detailed information, make sure that the detail parameter in the request is set to true. Otherwise, the return value of this parameter is empty. |

**ConnectionDo**

| Parameter | Type | Description |
|---|---|---|
| clientId | String | The ID of the consumer instance. |
| clientAddr | String | The address and port of the consumer instance. |
| language | String | The language of the client where the consumer instance resides. |
| version | String | The version of the client where the consumer instance resides. |
| remoteIP | String | The host IP address or public IP address. |

**DetailInTopicDo**

| Parameter | Type | Description |
|---|---|---|
| topic | String | The name of the topic. |

| totalDiff | Long | The number of accumulated messages in the topic. |
|---|---|---|
| lastTimestamp | Long | The latest consumption time. |
| delayTime | Long | The consumption latency. |

**ConsumerConnectionInfoDo**

| Parameter | Type | Description |
|---|---|---|
| clientId | String | The ID of the consumer instance. |
| connection | String | The connection information. |
| language | String | The language of the client where the consumer instance resides. |
| version | String | The version of the client where the consumer instance resides. |
| consumeModel | String | The consumption mode. Valid values: CLUSTERING: clustering consumption BROADCASTING: broadcasting consumption |
| consumeType | String | The way in which the consumer instance consumes messages. Valid values: PUSH: The RocketMQ broker pushes messages to the consumer instance. PULL: The consumer instance pulls messages from the RocketMQ broker. |
| threadCount | Integer | The number of consumption threads. |
| startTimeStamp | Long | The start time of consumption. |
| lastTimeStamp | Long | The latest consumption time. |
| SubscriptionSet | List(SubscriptionData) | The information about subscriptions. |
| RunningDataList | List(ConsumerRunningDataDo) | The real-time statistics. |
| Jstack | List(ThreadTrackDo) | The jstack information. |

**SubscriptionData**

| Parameter | Type | Description |
|---|---|---|

| topic | String | The name of the topic to which the group has subscribed. |
|---|---|---|
| subString | String | The subscription string of the topic. |
| subVersion | Long | The subscription version. The value is automatically incremented and of the LONG type. |
| tagsSet | List(String) | The information about the tags to which the group has subscribed. |

**ConsumerRunningDataDo**

| Parameter | Type | Description |
|---|---|---|
| groupId | String | The group ID of the consumer. |
| topic | String | The name of the topic to which the group has subscribed. |
| rt | Float | The consumption RT. Unit: milliseconds. |
| okTps | Float | The TPS of successful message consumption. |
| failedTps | Float | The TPS of message consumption failures. |
| failedCountPerHour | Long | The number of messages that failed to be consumed per hour. |

**ThreadTrackDo**

| Parameter | Type | Description |
|---|---|---|
| thread | String | The name of the thread. |
| trackList | List(String) | The jstack information. |

###### 2.1.6.6.3. /json/consumer/getConnection

Queries the connection information about the consumer instances that are identified by a group ID.

**Scenarios**

You can call this operation to check whether the consumer instances that are identified by a group ID are online and query the detailed connection information. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance where the group ID you want to query resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| groupId | String | Yes | The group ID that you want to query. |

| Parameter | Type | Description |
|---|---|---|
| data | List(ConnectionDo) | The connection information for the group ID. |

**ConnectionDo**

| Name | Type | Description |
|---|---|---|
| clientId | String | The ID of the consumer instance. |
| clientAddr | String | The address and port of the consumer instance. |
| language | String | The language of the client where the consumer instance resides. |
| version | String | The version of the client where the consumer instance resides. |
| remoteIP | String | The host IP address or public IP address. |

###### 2.1.6.6.4. /json/consumer/timespan

Queries the timestamps of messages and the latest time of consumption in a topic to which a group has subscribed.

**Scenarios**

You can call this operation to query the latest time and earliest time of messages in a topic on a RocketMQ broker, and the last consumption time of consumers. This operation is used to display the consumption progress, and can be used together with the /json/consumer/accumulate operation. For more information, see /json/consumer/accumulate. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance where the group ID you want to query resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| groupId | String | Yes | The group ID that you want to query. |
| topic | String | Yes | The topic to which the group has subscribed. |

For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | Data | The query results. |

**Data**

| Parameter | Type | Description |
|---|---|---|
| topic | String | The name of the topic that you queried. |
| minTimeStamp | Long | The time when the latest message was stored in the topic. |
| maxTimeStamp | Long | The time when the earliest message was stored in the topic. |

| consumeTimeStamp | Long | The latest time when the group consumed a message in the topic. |
|---|---|---|

###### 2.1.6.6.5. /json/consumer/resetoffset

Resets a consumer offset to a timestamp for a group ID.

**Scenarios**

You can call this operation to clear accumulated messages or reset the consumption progress. You can clear accumulated messages by using one of the following methods: Clear all messages. Clear the messages that are sent before a specified point in time. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance where the group ID you want to query resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| groupId | String | Yes | The group ID that you want to query. |
| topic | String | Yes | The name of the topic for which you want to reset the consumer offset. |
| type | Integer | Yes | The method that is used to clear accumulated messages. Valid values: 0: clears all messages. 1: clears the messages that are sent before a specified point in time. |

| resetTime | Long | No | The timestamp to which the consumption progress is reset. This parameter takes effect only when the type parameter is set to 1. |
|---|---|---|---|

For more information about common response parameters, see Common response parameters.

##### 2.1.6.7 Message query

###### 2.1.6.7.1. /json/message/trace

Queries whether a message has been consumed based on the message ID.

**Scenarios**

This operation is implemented based on the internal offset mechanism of Message Queue for Apache RocketMQ. In most cases, the results are valid. However, if you have reset the consumer offset or cleared messages, the results may be invalid. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance where the message you want to query resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| topic | String | Yes | The topic to which the message belongs. |
| msgId | String | Yes | The ID of the message. |

For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|

| data | List(MessageTrack) | The query results. |
|---|---|---|

**MessageTrack**

| Parameter | Type | Description |
|---|---|---|
| instanceId | String | The ID of the instance. |
| consumerGroup | String | The name of the consumer group. |
| trackType | String | The status of the message. Valid values: CONSUMED: The message was consumed. CONSUMED BUT FILTERED: _ _ The message was filtered. NOT CONSUME YET: The _ _ message was not consumed. NOT ONLINE: The consumer _ instance was offline. UNKNOWN: Other unknown issues occurred. |
| exceptionDesc | String | The description of an exception. |

###### 2.1.6.7.2. /json/message/getById

Queries a message based on the message ID and queries whether the message has been consumed. The queried information about the message includes the sending time, RocketMQ broker, and properties such as the key and tag.

**Scenarios**

You can call this operation to query the information about a message based on the message ID. This is an exact match. You can obtain the message ID from the SendResult parameter that is returned after the message is sent. Therefore, you must store the results that are returned after each message is sent. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|

| instanceId | String | Yes | The ID of the instance where the message you want to query resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
|---|---|---|---|
| msgId | String | Yes | The ID of the message that you want to query. |
| topic | String | Yes | The topic to which the message belongs. |

For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | Data | The query results. |

**Data**

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic to which the message belongs. |
| propertyList | List(MessageProperty) | The properties of the message. |
| body | String | The body of the message. |
| storeSize | Integer | The size of the message. |
| bornTimestamp | Long | The time when the message was generated. |
| bornHost | String | The producer that generated the message. |
| storeTimestamp | Long | The time when the RocketMQ broker stored the message. |
| storeHost | String | The RocketMQ broker that stored the message. |

| msgId | String | The ID of the message. |
|---|---|---|
| bodyCRC | Integer | The cyclic redundancy check (CRC) value of the message body. |
| reconsumeTimes | Integer | The number of message consumption retries. |

###### 2.1.6.7.3. /json/message/getByKey

Queries messages by using fuzzy match based on the topic and message key.

**Scenarios**

You can call this operation to query the information about messages based on the message key. This is a fuzzy match. A key may not be unique for a message. Therefore, the return results may contain multiple messages. This operation is applicable to scenarios where you cannot obtain message IDs. In these scenarios, perform the following steps:
1. Call this operation to query message IDs by using fuzzy match.
2. Call the /json/message/getById operation to query a message based on the message ID. For
more information, see /json/message/getById. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance where the messages you want to query reside. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| topic | String | Yes | The topic to which the messages belong. |
| key | String | Yes | The key of the messages. |

For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | List(OnsRestMessageDo) | The query results. |

**OnsRestMessageDo**

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic to which the message belongs. |
| propertyList | List(MessageProperty) | The properties of the message. |
| body | String | The body of the message. |
| storeSize | Integer | The size of the message. |
| bornTimestamp | Long | The time when the message was generated. |
| bornHost | String | The producer that generated the message. |
| storeTimestamp | Long | The time when the RocketMQ broker stored the message. |
| storeHost | String | The RocketMQ broker that stored the message. |
| msgId | String | The ID of the message. |
| bodyCRC | Integer | The CRC value of the message body. |
| reconsumeTimes | Integer | The number of message consumption retries. |

###### 2.1.6.7.4. /json/message/getByPagedTopic

Queries all messages in a topic within a period of time by page.

**Scenarios**

You can call this operation to query messages based on the topic and time range. This is a range query. The query results are displayed on multiple pages. This operation is applicable only when message IDs and message keys are unavailable. However, we recommend that you shorten the time range to query. Otherwise, excessive messages may be returned and affect your troubleshooting efficiency. To call this operation, perform the following steps:
1. Specify the topic, start time, end time, and size of each page to query messages by page. If
matched messages are found, the first page of the messages, total number of pages, and query task ID are returned by default.
2. Query messages that are not displayed on the first page based on the returned query task
ID for the first query. When you query the messages, specify the query task ID and current page number. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance where the messages you want to query reside. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| topic | String | Yes | The topic to which the messages belong. |
| beginTime | Long | Yes | The beginning of the time range to query. |
| endTime | Long | Yes | The end of the time range to query. |
| taskId | String | No | The ID of the query task. This parameter is not required for the first query but is required to query messages subsequently. You can obtain the value of this parameter from the previous return results. |
| currentPage | Integer | Yes | The number of the page to return. Valid values: 1 to 50. |
| pageSize | Integer | No | The number of entries to return on each page. Valid values: 5 to 50. Default value: 20. |

For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|

| MsgFoundDo | MsgFoundDo | The query results. |
|---|---|---|

**MsgFoundDo**

| Parameter | Type | Description |
|---|---|---|
| taskId | String | The ID of the query task that is returned for the first query. This ID is used to query messages subsequently. |
| maxPageCount | Long | The total number of pages returned. |
| currentPage | Long | The page number of the returned page. |
| data | List(OnsRestMessageDo) | The information about the messages that are displayed on the current page. The return results are the same as those of the /json/message/getById operation. |

##### 2.1.6.8 Publishing and subscription statistics

###### 2.1.6.8.1. /json/trend/topicInputTps

Queries the statistics about messages that are written to a topic within a period of time.

**Scenarios**

You can call this operation to query online message statistics for a specified topic, and query the number of messages that are written or the TPS curve within a specified period of time.

> **Important:** If the message volume is small and messages are unevenly distributed for your application, the TPS curve may be flat. We recommend that you query the total number of messages that are written to the topic.

For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|

| instanceId | String | Yes | The ID of the instance where the topic you want to query resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
|---|---|---|---|
| topic | String | Yes | The name of the topic that you want to query. |
| beginTime | Long | Yes | The beginning of the time range to query. Unit: milliseconds. |
| endTime | Long | Yes | The end of the time range to query. Unit: milliseconds. |
| period | Long | Yes | The sampling period. Unit: minutes. Valid values: 1, 5, and 10. |
| type | Integer | Yes | The type of statistics that you want to query. Valid values: 0: queries the number of messages that are written to the specified topic within the specified period of time. 1: queries the TPS curve within the specified period of time. |

| Parameter | Type | Description |
|---|---|---|
| data | Data | The returned data. |

**Data**

| Parameter | Type | Description |
|---|---|---|
| title | String | The name of the table. |

| records | List(StatsDataDo) | The collected statistics. |
|---|---|---|

**StatsDataDo**

| Parameter | Type | Description |
|---|---|---|
| x | Long | The x-axis that represents the timestamp. Unit: milliseconds. |
| y | Float | The y-axis that represents the data, which is the TPS or total number of messages. |

###### 2.1.6.8.2. /json/trend/groupOutputTps

Queries the statistics about messages that are consumed by a group within a period of time.

**Scenarios**

When the system generates consumption statistics online, you can call this operation to query the following statistics based on a specified group ID: The statistical curve of the total number of consumed messages The statistical curve of the TPS for message consumption

> **Important:** If the message volume is small and messages are unevenly distributed for your application, the TPS curve may be flat. We recommend that you query the total number of consumed messages.

For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance where the group ID you want to query resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| topic | String | Yes | The name of the topic that you want to query. |

| groupId | String | Yes | The group ID that you want to query. |
|---|---|---|---|
| beginTime | Long | Yes | The beginning of the time range to query. Unit: milliseconds. |
| endTime | Long | Yes | The end of the time range to query. Unit: milliseconds. |
| period | Long | Yes | The sampling period. Unit: minutes. Valid values: 1, 5, and 10. |
| type | Integer | Yes | The type of statistics that you want to query. Valid values: 0: queries the statistical curve of the total number of consumed messages. 1: queries the statistical curve of the TPS for message consumption. |

For more information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | Data | The returned data. |

**Data**

| Parameter | Type | Description |
|---|---|---|
| title | String | The name of the table. |
| records | List(StatsDataDo) | The collected statistics. |

**StatsDataDo**

| Parameter | Type | Description |
|---|---|---|
| x | Long | The x-axis that represents the timestamp. Unit: milliseconds. |
| y | Float | The y-axis that represents the data, which is the TPS or total number of messages. |

##### 2.1.6.9 Authorization management

###### 2.1.6.9.1. /json/empower/create

Authorizes another Apsara Stack tenant account to use a topic, including the permissions to publish and subscribe to messages.

**Scenarios**

In Message Queue for Apache RocketMQ, a topic belongs to the owner account that is used to create the topic. If another Apsara Stack tenant account needs to use the topic, the owner can call this operation to grant the permissions to publish and subscribe to messages to the Apsara Stack tenant account.

> **Note:** Three types of permissions are supported for authorization: publishing, subscription, and publishing and subscription.
> The account that is used to grant permissions must be the owner account of the topic. Permissions are granted to an Apsara Stack tenant account.
> After permissions are granted, the Apsara Stack tenant account still needs to create its own group ID for subscribing to and receiving messages instead of using the group ID that is created by the owner account.

For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance. |
| empowerUser | Long | Yes | The user ID of the Apsara Stack tenant account to be authorized. |
| topic | String | Yes | The topic whose permissions you want to grant. The topic must belong to you. |
| relation | Integer | Yes | The type of permission to be granted. Valid values: 2: the permissions to publish messages 4: the permissions to subscribe to messages 6: the permissions to publish and subscribe to messages |

The returned data is null.

###### 2.1.6.9.2. /json/empower/createBySub

Authorizes a RAM user to use a topic, including the permissions to publish and subscribe to messages.

**Scenarios**

In Message Queue for Apache RocketMQ, a topic belongs to the owner account that is used to create the topic. If a RAM user needs to use the topic, the owner can call this operation to grant the permissions to publish and subscribe to messages to the RAM user.

> **Note:** Three types of permissions are supported for authorization: publishing, subscription, and publishing and subscription.
> The account that is used to grant permissions must be the owner account of the topic. Permissions are granted to a RAM user.
> After permissions are granted, the RAM user still needs to create its own group ID for subscribing to and receiving messages instead of using the group ID that is created by the owner account.

For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance. |
| empowerUser | Long | Yes | The ID of the RAM user to be authorized. |
| topic | String | Yes | The topic whose permissions you want to grant. The topic must belong to you. |
| relation | Integer | Yes | The type of permission to be granted. Valid values: 2: the permissions to publish messages 4: the permissions to subscribe to messages 6: the permissions to publish and subscribe to messages |

The returned data is null.

###### 2.1.6.9.3. /json/empower/delete

Deletes an existing authorization to revoke the topic access permissions that are granted to an account.

**Scenarios**

After the permissions to access a topic are granted to an account, the owner of the topic can call this operation to revoke the granted permissions.

> **Note:** The account that is used to call this operation must be the owner account of the topic.
> The authorization information to be deleted must exist.

For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance. |
| empowerUser | Long | Yes | The user ID of the authorized account. A RAM user ID is supported. |
| topic | String | Yes | The topic whose permissions are granted. The topic must belong to you. |

The returned data is null.

###### 2.1.6.9.4. /json/empower/list

Queries the authorization information about a topic.

**Scenarios**

The owner of a topic can query whether the topic access permissions are granted to a specific account and query the type of granted permission. For more information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The ID of the instance. |
| empowerUser | Long | Yes | The user ID of the authorized account. A RAM user ID is supported. |
| topic | String | Yes | The topic whose permissions are granted. The topic must belong to you. |

The authorization information about the topic is returned in the JSON format, including the authorized account and type of granted permission.

##### 2.1.6.10 Dead-letter queue management

###### 2.1.6.10.1. /json/message/getByIdInDLQ

Queries a dead-letter message based on the message ID. The queried information about the dead-letter message includes the storage time, message body, and properties such as the key and tag. You can call this operation to query the information about a dead-letter message based on the message ID. This is an exact match. You can obtain the message ID from the SendResult parameter that is returned after the message is sent. You can also call the /json/message/getByPagedDLQ operation to query message IDs.

| Parameter | Type | Required | Description |
|---|---|---|---|
| InstanceId | String | Yes | The ID of the instance where the message you want to query resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| GroupId | String | Yes | The group ID that you want to query. |
| MsgId | String | Yes | The ID of the message that you want to query. |

Table 1. Data

| Parameter | Type | Description |
|---|---|---|
| Topic | String | The topic to which the message belongs. |
| PropertyList | List(MessageProperty) | The properties of the message. |
| Body | String | The body of the message. |
| StoreSize | Integer | The size of the message. |
| BornTimestamp | Long | The time when the message was generated. |
| BornHost | String | The producer that generated the message. |
| StoreTimestamp | Long | The time when the RocketMQ broker stored the message. |
| StoreHost | String | The RocketMQ broker that stored the message. |
| MsgId | String | The ID of the message. |
| BodyCRC | Integer | The CRC value of the message body. |

| ReconsumeTimes | Integer | The number of message consumption retries. |
|---|---|---|

###### 2.1.6.10.2. /json/message/getByPagedDLQ

Queries all dead-letter messages in a group within a period of time by page. You can call this operation to query dead-letter messages based on the group ID. This is a range query. The query results are displayed on multiple pages. This operation is applicable only when message IDs are unavailable. However, we recommend that you shorten the time range to query. Otherwise, excessive messages may be returned and affect your troubleshooting efficiency. To call this operation, perform the following steps:
1. Specify the group ID, start time, end time, and size of each page to query messages by
page. If matched messages are found, the first page of the messages, total number of pages, and query task ID are returned by default.
2. Query messages that are not displayed on the first page based on the returned query task
ID for the first query. When you query the messages, specify the query task ID and current page number.

| Parameter | Type | Required | Description |
|---|---|---|---|
| InstanceId | String | Yes | The ID of the instance where the messages you want to query reside. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| GroupId | String | Yes | The group ID that you want to query. |
| BeginTime | Long | Yes | The beginning of the time range to query. |
| EndTime | Long | Yes | The end of the time range to query. |

| TaskId | String | No | The ID of the query task. This parameter is not required for the first query but is required to query messages subsequently. You can obtain the value of this parameter from the previous return results. |
|---|---|---|---|
| CurrentPage | Integer | Yes | The number of the page to return. Valid values: 1 to 50. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 5 to 50. Default value: 20. |

| Parameter | Type | Description |
|---|---|---|
| MsgFoundDo | MsgFoundDo | The query results. |

Table 1. MsgFoundDo

| Parameter | Type | Description |
|---|---|---|
| TaskId | String | The ID of the query task that is returned for the first query. This ID is used to query messages subsequently. |
| MaxPageCount | Long | The total number of pages returned. |
| CurrentPage | Long | The page number of the returned page. |
| Data | List(OnsRestMessageDo) | The information about the messages that are displayed on the current page. The return results are the same as those of the /json/message/getByIdInDLQ operation. |

###### 2.1.6.10.3. /json/message/resendByIdInDLQ

Resends a dead-letter message based on the message ID so that the message can be consumed again by the same consumer. You can call this operation to allow a dead-letter message to be consumed by the same consumer again. A dead-letter message is a message that still fails to be consumed after the number of consumption retries reaches the upper limit. If the message still cannot be consumed after you resend it, a message with the same message ID is added to the corresponding deadletter queue. You can query the message ID on the Dead-letter Queues page in the Message Queue for Apache RocketMQ console or by calling API operations. You can determine the number of consumption failures for a message after you resend it, based on the number of messages with the same message ID.

> **Important:** A dead-letter message is a message that still fails to be consumed after the number of consumption retries reaches the upper limit. This generally means that the consumption logic may have errors. Therefore, first identify the causes of the consumption failures, and then call this operation to resend the message.
> Message Queue for Apache RocketMQ does not manage the status of dead-letter messages after you resend them. Messages that are consumed after you call this operation are not removed from corresponding dead-letter queues. You must manually manage dead-letter messages and determine whether to resend a dead- letter message. This way, you do not need to repeatedly resend dead-letter messages that are consumed.

| Parameter | Type | Required | Description |
|---|---|---|---|
| InstanceId | String | Yes | The ID of the instance where the message you want to query resides. If your instance has no namespace, you can leave this parameter unspecified. If your instance has a namespace, you must specify this parameter. For more information about namespaces, see Updates. |
| MsgId | String | Yes | The ID of the message that you want to query. |
| GroupId | String | Yes | The group ID that you want to query. |

For more information about common response parameters, see Common response parameters.

## 3 SDK reference

### 3.1 文档标题缺失，请补全后重新导出

#### 3.1.1 Overview

Message Queue for Apache RocketMQ is an important component of distributed systems. This service supports asynchronous communication for application decoupling and load shifting, and provides high performance, high availability, high scalability, and eventual consistency. This document describes how to manage a message queuing service between RocketMQ applications and the message queuing server during data transmission. This document provides the specifications that the service complies with and the common API operations that are used to manage the service. This document is suitable for scenarios in which messages are transmitted over the TCP protocol by using Message Queue for Apache RocketMQ SDK for Java.

#### 3.1.2 Messaging model

Message Queue for Apache RocketMQ supports the publish-subscribe model. A producer can publish a message to a broker, and multiple consumers can subscribe to a topic on the broker. The following figure shows the messaging model. Figure 1. Publish-subscribe model

#### 3.1.3 Updates

This topic describes the updates of Message Queue for Apache RocketMQ from V3.8.0 to V3.8.1 to help you get started with the updated version.

**Optimization of resource isolation by instance**

Message Queue for Apache RocketMQ provides instances for multi-tenancy isolation. Each user can purchase multiple instances and logically isolate them from each other. To ensure the compatibility with the existing resources of existing users, Message Queue for Apache RocketMQ provides the following types of instances and namespaces: Default instances, which are compatible with the existing resources of existing users This type of instance has no separate namespace. Resource names must be globally unique within and across all instances. By default, an instance without a namespace is automatically generated for the existing resources of each existing user. If no existing resources are available, you can create at most one instance without a namespace. You can configure the endpoint, which can be obtained from the **Instances** page in the Message Queue for Apache RocketMQ console.

```
// Recommended configuration: properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxxx"); // Compatible configuration, which is not recommended. We recommend that you update this configuration to the recommended configuration: properties.put(PropertyKeyConst.ONSAddr, "xxxx");
```

New instances A new instance has a separate namespace. Resource names must be unique within an instance but can be the same across different instances. You can configure the endpoint, which can be obtained from the **Instances** page in the Message Queue for Apache RocketMQ console.

```
// Recommended configuration: properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxx");
```

A RocketMQ client must be updated to the following latest versions for different programming languages: Java: V1.8.7.1.Final C and C++: V2.0.0 .NET: V1.1.3

**Optimization of resource application**

Previously, Message Queue for Apache RocketMQ resources consisted of topics, producer IDs, and consumer IDs. Each two of the resources have a many-to-many relationship, which was difficult to comprehend. Each time you created a topic, you must associate the topic with a producer ID and a consumer ID. This process was too complex for medium- and large-sized enterprise customers. To optimize user experience and help new users get started, the resource application process has been simplified. The resource application process has been optimized in the following aspects: Topic management, which is unchanged You need to apply for a topic. A topic is used to classify messages. It is the primary classifier. You do not need to apply for a producer ID. Producer IDs and consumer IDs are integrated into group IDs. In the Message Queue for Apache RocketMQ console, the Producers module has been removed. The Producers and Consumers modules have been integrated into the Groups module. You do not need to associate a producer ID or consumer ID with a topic. Instead, you need only to apply for a group ID and associate it with a topic in the code. Compatibility: The list of producer IDs is no longer displayed. This does not affect the current services. The consumer IDs that start with CID- or CID_ and that you have applied for can still be used and can be set in the **PropertyKeyConst.ConsumerId** or
**PropertyKeyConst.GROUP_ID** parameter of the code.
Sample code

> **Note:** We recommend that you update a RocketMQ client to the following latest versions for different programming languages:

Java: V1.8.7.1.Final C and C++: V2.0.0 .NET: V1.1.3

> Existing producer IDs or consumer IDs can still be used and do not affect the current services. However, we recommend that you update your instance configuration to the recommended configuration.

Recommended configuration: Integrate producer IDs and consumer IDs into group IDs.

```
// Set the PropertyKeyConst.GROUP_ID parameter. The original PropertyKeyConst.ProducerId and PropertyKeyConst.ConsumerId parameters are deprecat ed. properties.put(PropertyKeyConst.GROUP_ID, "The original CID-XXX or the GID-XXX");
```

Compatible configuration: Use a producer ID to identify a producer and a consumer ID to identify a consumer.

```
// When you create a producer, you must set the PropertyKeyConst.ProducerId paramet er. properties.put(PropertyKeyConst.ProducerId, "The original PID-XXX or the GID-XXX"); // When you create a consumer, you must set the PropertyKeyConst.ConsumerId paramet er. properties.put(PropertyKeyConst.ConsumerId, "The original CID-XXX or the GID-XXX");
```

#### 3.1.4 Transport protocol and character encoding

**encoding**

The underlying layer of ApsaraMQ for RocketMQ SDKs provides services based on the TCP protocol. User requests and responses in ApsaraMQ for RocketMQ use UTF-8 character encoding.

**Transport layer encryption**

ApsaraMQ for RocketMQ instances support Transport Layer Security (TLS) 1.2 and later. You can configure parameters in an SDK to determine whether to use encrypted transport layer links.
**Configuration method**: When you start the client program, set the JVM attributes to
determine whether to use the encrypted transport layer link. The startup command is **java -**
**Dtls.enable=true**. By default, TLS links are disabled. If you set the value to true, encrypted
transport layer links are enabled.

#### 3.1.5 Common classes and methods

##### 3.1.5.1 PropertyKeyConst

The following table lists the main fields of this class.

| Parameter | Type | Default value | Description |
|---|---|---|---|
| AccessKey | String | - | The AccessKey ID that you created in the Apsara Uni-manager Management Console for identity verification. |
| SecretKey | String | - | The AccessKey secret that you created in the Apsara Uni-manager Management Console for identity verification. |
| OnsChannel | String | ALIYUN | The user channel. Valid values: ALIYUN and CLOUD. ALIYUN stands for Apsara Stack. CLOUD stands for CloudTmall. |
| NAMESRV ADDR _ | String | - | The TCP endpoint that is used to connect to the Message Queue for Apache RocketMQ instance. |
| GROUP ID _ | String | - | The group ID that you created in the Message Queue for Apache RocketMQ console. This group ID identifies a type of producers or consumers. |
| MessageModel | String | CLUSTERING | The consumption mode for the consumer instance. Valid values: CLUSTERING and BROADCASTING. |
| ConsumeThreadNums | String | 64 | The number of consumer threads. |
| MaxReconsumeTimes | String | 16 | The maximum number of delivery retries that can be performed when a message fails to be consumed. |
| ConsumeTimeout | String | 15 | The timeout period for consuming each message. If the time for consuming a message exceeds the specified timeout period, the message fails to be consumed and is redelivered after a retry interval. Configure an appropriate value for each type of application. Unit: minute. |
| ConsumeMessageBatc hMaxSize | String | 1 | The maximum number of messages that can be consumed in each batch. The actual number of consumed messages in a batch can be smaller than the value of this parameter. The value must be an integer from 1 to 32. The default value is 1. |

| CheckImmunityTimeIn Seconds | String | 30 | The shortest time for which the system waits before checking the status of a transactional message for the first time. Unit: seconds. |
|---|---|---|---|
| shardingKey | String | - | The partition key that is used to determine the partitions to which ordered messages are distributed. |
| suspendTimeMillis | String | 3000 | The retry interval for ordered messages that fail to be consumed. Unit: milliseconds. |

##### 3.1.5.2 ONSFactory

###### 3.1.5.2.1 createConsumer

Syntax: static Consumer createConsumer(Properties properties) Description: You can call this operation to create a consumer instance that consumes multiple types of messages in Message Queue for Apache RocketMQ. These message types include normal messages, scheduled messages, delayed messages, and transactional messages. Request parameter

| Parameter | Type | Description |
|---|---|---|
| properties | Properties | For more information, see the description of PropertyKeyConst. Required properties: PropertyKeyConst.NAMESRV ADDR, _ PropertyKeyConst.ConsumerId, PropertyKeyConst.AccessKey, and PropertyKeyConst.SecretKey. Optional properties: PropertyKeyConst.ConsumeThreadNums and PropertyKeyConst.ConsumeTimeout. |

Response parameter

| Parameter | Description |
|---|---|
| Consumer | The consumer instance that consumes multiple types of messages in Message Queue for Apache RocketMQ. These message types include normal messages, scheduled messages, transactional messages, and delayed messages. |

###### 3.1.5.2.2 createBatchConsumer

Syntax: static BatchConsumer createBatchConsumer(Properties properties) Description: You can call this operation to create consumer instances in Message Queue for RocketMQ (RocketMQ) in batches. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| properties | Properties | For more information, see the description of PropertyKeyConst. Required properties: PropertyKeyConst.NAMESRV ADDR, _ PropertyKeyConst.GROUP ID, PropertyKeyConst.AccessKey, _ and PropertyKeyConst.SecretKey Optional properties: PropertyKeyConst.ConsumeThreadNums, PropertyKeyConst.ConsumeTimeout, and PropertyKeyConst.ConsumeMessageBatchMaxSize |

Response:

| Type | Description |
|---|---|
| BatchConsumer | BatchConsumer |

###### 3.1.5.2.3 createOrderedConsumer

Syntax: static OrderConsumer createOrderedConsumer(Properties properties) Description: You can call this operation to create a consumer instance for consuming ordered messages in Message Queue for RocketMQ (RocketMQ). Request parameters:

| Parameter | Type | Description |
|---|---|---|
| properties | properties | For more information, see the description of PropertyKeyConst. Required properties: PropertyKeyConst.NAMESRV ADDR, _ PropertyKeyConst.GROUP ID, PropertyKeyConst.AccessKey, _ and PropertyKeyConst.SecretKey Optional properties: PropertyKeyConst.ConsumeThreadNums and PropertyKeyConst.ConsumeTimeout |

Response:

| Type | Description |
|---|---|
| OrderConsumer | The consumer instance of ordered messages in RocketMQ. |

###### 3.1.5.2.4 createOrderProducer

Syntax: static OrderProducer createOrderProducer(Properties properties) Description: You can call this operation to create a producer instance for sending ordered messages in Message Queue for RocketMQ (RocketMQ). Request parameters:

| Parameter | Type | Description |
|---|---|---|

| properties | Properties | For more information, see the description of PropertyKeyConst. Required properties: PropertyKeyConst.NAMESRV ADDR, _ PropertyKeyConst.GROUP ID, PropertyKeyConst.AccessKey, _ PropertyKeyConst.SecretKey, and PropertyKeyConst.ShardingKey Optional properties: PropertyKeyConst.SendMsgTimeoutMillis |
|---|---|---|

Response:

| Type | Description |
|---|---|
| OrderProducer | The producer instance of ordered messages in RocketMQ. |

###### 3.1.5.2.5 createProducer

Syntax: static Producer createProducer(Properties properties) Description: You can call this operation to create a producer instance that publishes normal messages, scheduled messages, and delayed messages in Message Queue for Apache RocketMQ. Request parameter

| Parameter | Type | Description |
|---|---|---|
| properties | Properties | For more information, see the description of PropertyKeyConst. Required properties: PropertyKeyConst.NAMESRV ADDR, _ PropertyKeyConst.GROUP ID, _ PropertyKeyConst.AccessKey, and PropertyKeyConst.SecretKey. Optional properties: PropertyKeyConst.SendMsgTimeoutMillis. |

Response parameter

| Parameter | Description |
|---|---|
| Producer | The producer instance that publishes normal messages, scheduled messages, and delayed messages in Message Queue for Apache RocketMQ. |

###### 3.1.5.2.6 createTransactionProducer

Syntax: static TransactionProducer createTransactionProducer(Properties properties, LocalTransactionChecker checker) Description: You can call this operation to create a producer instance for sending distributed transactional messages in Message Queue for RocketMQ (RocketMQ). Request parameters:

| Parameter | Type | Description |
|---|---|---|

| properties | Properties | For more information, see the description of PropertyKeyConst. Required properties: PropertyKeyConst.NAMESRV ADDR, _ PropertyKeyConst.GROUP ID, _ PropertyKeyConst.AccessKey, and PropertyKeyConst.SecretKey Optional properties: PropertyKeyConst.SendMsgTimeoutMillis and PropertyKeyConst.CheckImmunityTimeInSeconds |
|---|---|---|
| checker | LocalTransactionCh ecker | For more information, see the description of LocalTransactionChecker. |

Response:

| Type | Description |
|---|---|
| TransactionProducer | The producer instance of transactional messages in RocketMQ. |

##### 3.1.5.3 Message

###### 3.1.5.3.1 Overview

It is a message that you want to send. A valid message must contain the topic, body, optional tags, and message key.

> **Note:** The length of the custom key-value pair for a message is not constrained, but all custom key-value pairs cannot exceed 32,767 bytes after they are serialized.


###### 3.1.5.3.2 Default message construction

Syntax: Message() Description: You can call this operation to create a message by using the default constructor. Request parameters: none

###### 3.1.5.3.3 Message construction by using parameters (1)

**parameters (1)**

Syntax: public Message(String topic, String tag, String key, byte body) Description: You can call this operation to create a message by specifying parameters. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the message. It cannot exceed 255 characters in length. The message topic can contain uppercase letters (A-Z), lowercase letters (a-z), digits (0- 9), hyphens (-), and underscores ( ). _ |

| tag | String | The message tag, which must be a valid identifier. The tag must be as short as possible and easy to understand. |
|---|---|---|
| key | String | The key of the message. |
| body | byte | The message body. It cannot exceed 4 MB by default, including message attributes that cannot exceed 8 KB. For more information about the message body, see the cluster deployment documentation. |

###### 3.1.5.3.4 Message construction by using parameters (2)

**parameters (2)**

Syntax: public Message(String topic, String tags, byte body) Description: You can call this operation to create a message by specifying parameters. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the message. It cannot exceed 255 characters in length. The message topic can contain uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), hyphens (-), and underscores ( ). _ |
| tags | String | The message tag, which must be a valid identifier. The tag must be as short as possible and easy to understand. |
| body | byte | The message body. It cannot exceed 4 MB by default, including message attributes that cannot exceed 8 KB. For more information about the message body, see the cluster deployment documentation. |

###### 3.1.5.3.5 putUserProperties

Syntax: public void putUserProperties(String key, String value) Description: You can call this operation to add a custom property key-value pair that can be obtained when the message is consumed. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| key | String | The custom property key. |
| value | String | The custom property value. |

Response: none

###### 3.1.5.3.6 getUserProperties

Syntax: public String getUserProperties(String key) Description: You can call this operation to obtain the custom property value. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| key | String | The custom property key. |

Response:

| Type | Description |
|---|---|
| String | The custom property value. |

###### 3.1.5.3.7 getTopic

Syntax: public String getTopic() Description: You can call this operation to obtain the topic of the messages. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The topic of the messages. |

###### 3.1.5.3.8 setTopic

Syntax: public void setTopic(String topic) Description: You can call this operation to set the topic of the messages. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the messages. |

Response: none

###### 3.1.5.3.9 getTag

Syntax: public String getTag() Description: You can call this operation to obtain the message tag. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The tag of the message. |

###### 3.1.5.3.10 setTag

Syntax: public void setTag(String tag) Description: You can call this operation to set the message tag. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| tag | String | The tag of the message. |

Response: none

###### 3.1.5.3.11 getKey

Description: You can call this operation to obtain the message key. Syntax: public String getKey() Request parameters: none Response:

| Type | Description |
|---|---|
| String | The key of the message. |

###### 3.1.5.3.12 setKey

Syntax: public void setKey(String key) Description: You can call this operation to set the message key. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| key | String | The key of the message. |

Response: none

###### 3.1.5.3.13 getMsgID

Syntax: public String getMsgID() Description: You can call this operation to obtain the message ID. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The ID of the message. |

###### 3.1.5.3.14 setMsgID

Syntax: public void setMsgID(String msgid) Description: You can call this operation to set the message ID. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| msgid | String | The ID of the message. |

Response: none

###### 3.1.5.3.15 getReconsumeTimes

Syntax: public int getReconsumeTimes() Description: You can call this operation to obtain the number of retries after a message has failed to be consumed. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The number of retries. |

###### 3.1.5.3.16 setReconsumeTimes

Syntax: public void setReconsumeTimes(int value) Description: You can call this operation to set the number of retries to consume a message. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| value | int | The number of retries. |

Response: none

###### 3.1.5.3.17 getBornTimestamp

Syntax: public long getBornTimestamp() Description: You can call this operation to obtain the message production time. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The production time of the message. |

###### 3.1.5.3.18 setBornTimestamp

Syntax: public void setBornTimestamp(long value) Description: You can call this operation to set the message production time. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| value | long | The production time of the message. |

Response: none

###### 3.1.5.3.19 getBornHost

Syntax: public String getBornHost() Description: You can call this operation to retrieve the message production host. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The host that produced the message. |

###### 3.1.5.3.20 setBornHost

Syntax: public void setBornHost(String value) Description: You can call this operation to set the message production host. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| value | long | The host that produces the message. |

Response: none

###### 3.1.5.3.21 getStartDeliverTime

Syntax: public long getStartDeliverTime() Description: You can call this operation to obtain the start time for delivering scheduled messages. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The start time for delivering scheduled messages. |

###### 3.1.5.3.22 setStartDeliverTime

Syntax: public void setStartDeliverTime(long value) Description: You can call this operation to set the delivery time (absolute time) of scheduled messages with a maximum latency of 40 days. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| value | long | The start time for delivering scheduled messages. |

Response: none

###### 3.1.5.3.23 getShardingKey

Syntax: public long getShardingKey() Description: You can call this operation to obtain the sharding key for ordered messages. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The sharding key for ordered messages. |

###### 3.1.5.3.24 setShardingKey

Syntax: public void setShardingKey(String value) Description: You can call this operation to set the sharding key for ordered messages. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| String | long | The sharding key for ordered messages. |

Response: none

##### 3.1.5.4 ONSClientException

###### 3.1.5.4.1 Default ONSClientException construction

Syntax: public ONSClientException() Description: Uses the default exception constructor to construct ONSClientException. Request parameters: none

###### 3.1.5.4.2 ONSClientException construction by using parameters (1)

**using parameters (1)**

Syntax: public ONSClientException(String message) Description: Uses the exception constructor to construct ONSClientException by using parameters.

| Parameter | Type | Description |
|---|---|---|
| message | String | The exception information that needs to be exposed. |

###### 3.1.5.4.3 ONSClientException construction by using parameters (2)

**using parameters (2)**

Syntax: public ONSClientException(Throwable cause) Description: Uses the exception constructor to construct ONSClientException by using parameters.

| Parameter | Type | Description |
|---|---|---|
| message | String | The exception information that needs to be exposed. |

###### 3.1.5.4.4 ONSClientException construction by using parameters (3)

**using parameters (3)**

Syntax: public ONSClientException(String message, Throwable cause) Description: Uses the exception constructor to construct ONSClientException by using parameters.

| Parameter | Type | Description |
|---|---|---|
| message | String | The exception information that needs to be exposed. |
| cause | Throwable | The exception information that needs to be exposed. |

##### 3.1.5.5 Message sending

###### 3.1.5.5.1 Overview

This topic describes the methods for sending various types of messages in Message Queue for Apache RocketMQ. The following figure shows the methods and parameters for different message types. Figure 1. Methods and parameters for publishing messages

###### 3.1.5.5.2 SendResult

###### 3.1.5.5.2.1 Default SendResult construction

Syntax: public SendResult() Description: Uses the default constructor to create a message sending result object. Request parameters: none

###### 3.1.5.5.2.2 getMessageId

Syntax: public long getMessageId() Description: Queries the ID of a message that is sent. Request parameters: none

| Type | Description |
|---|---|
| String | The ID of the sent message. |

###### 3.1.5.5.2.3 getTopic

Syntax: public String getTopic() Description: Queries the topic to which a message that is sent belongs. Request parameters: none

| Type | Description |
|---|---|
| String | The topic of the sent message. |

###### 3.1.5.5.2.4 toString

Syntax: public String toString() Description: Serializes a message sending result. Request parameters: none

| Type | Description |
|---|---|
| String | The serialized string of the message sending result. |

###### 3.1.5.5.3 Producer

###### 3.1.5.5.3.1 Overview

You can use a producer instance to send regular messages, scheduled messages, or delayed messages. Thread security: All implementation classes of a producer instance are thread-secure. Multiple threads can be used to send messages concurrently. A producer instance can send messages under multiple topics. In normal cases, a producer instance is efficient enough to complete all the message sending tasks by using relevant methods. No more instances need to be created. Regular messages can be sent in reliable synchronous, reliable asynchronous, or one-way mode.

###### 3.1.5.5.3.2 send

Syntax: public SendResult send(Message message) Description: Sends a regular message, scheduled message, or delayed message in synchronous mode. The message is sent if no exception is thrown.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The message that you want to send. |

| Parameter | Description |
|---|---|
| SendResult | The sending result that is returned, including the message ID and topic. |

###### 3.1.5.5.3.3 sendOneway

Syntax: public void sendOneway(Message message) Description: Sends a regular message, scheduled message, or delayed message in one-way mode. In this mode, if the RocketMQ broker does not respond, you cannot know whether the message is sent to the broker.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The message that you want to send. |

Response parameters: none

###### 3.1.5.5.3.4 sendAsync

Syntax: public void sendAsync(Message message, SendCallback sendCallback) Description: Sends a regular message, scheduled message, or delayed message in asynchronous callback mode.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The message that you want to send. |
| sendCallback | SendCallback | The callback function to be called after the message is sent. |

Response parameters: none

###### 3.1.5.5.3.5 isStarted

Syntax: public boolean isStarted() Description: Checks whether an instance is enabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is enabled. A value of true indicates that the instance is enabled. A value of false indicates that the instance is not enabled. |

###### 3.1.5.5.3.6 isClosed

Syntax: public boolean isClosed() Description: Checks whether an instance is disabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is disabled. A value of true indicates that the instance is disabled. A value of false indicates that the instance is not disabled. |

###### 3.1.5.5.3.7 start

Syntax: public void start() Description: Enables a producer instance to send messages. Request parameters: none Response parameters: none

###### 3.1.5.5.3.8 shutdown

Syntax: public void shutdown() Description: Disables a producer instance from sending messages. Request parameters: none Response parameters: none

###### 3.1.5.5.4 TransactionProducer

###### 3.1.5.5.4.1 send

Syntax: SendResult send(Message message, LocalTransactionExecuter executer, Object arg) Description: Sends a transactional message. The process of sending a transactional message consists of the following three steps: The producer instance first sends a half message to the RocketMQ broker. The producer instance starts a local transaction by using an executor. The RocketMQ broker commits or rolls back the half message that is sent in Step 1 based on the result of the local transaction in Step 2.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The transactional message that you want to send. |
| executer | LocalTransactionExecuter | The local transaction executor. For more information, see the LocalTransactionExecuter class. |
| arg | Object | A custom parameter. This parameter can be used for the local transaction executor. |

| Parameter | Description |
|---|---|
| SendResult | The sending result that is returned, including the message ID and topic. |

###### 3.1.5.5.4.2 isStarted

Syntax: public boolean isStarted() Description: Checks whether an instance is enabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is enabled. A value of true indicates that the instance is enabled. A value of false indicates that the instance is not enabled. |

###### 3.1.5.5.4.3 isClosed

Syntax: public boolean isClosed() Description: Checks whether an instance is disabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is disabled. A value of true indicates that the instance is disabled. A value of false indicates that the instance is not disabled. |

###### 3.1.5.5.4.4 start

Syntax: public void start() Description: Enables a producer instance to send transactional messages. Request parameters: none Response parameters: none

###### 3.1.5.5.4.5 shutdown

Syntax: public void shutdown() Description: Disables a producer instance from sending transactional messages. Request parameters: none Response parameters: none

###### 3.1.5.5.4.6 LocalTransactionExecuter

execute Syntax: TransactionStatus execute(Message msg, Object arg) Description: Starts a local transaction. This method is called by applications.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The transactional message that you want to send. |
| arg | Object | The custom parameter that is specified by the send method. |

| Parameter | Description |
|---|---|
| TransactionStatus | The result of the local transaction that is returned. The transaction may be in the Commit, Rollback, or unknown state. |

###### 3.1.5.5.4.7 TransactionStatus

The result of a local transaction that corresponds to a half message. The transaction may be in the Commit, Rollback, or unknown state. Enumeration

| Value | Description |
|---|---|
| CommitTransaction | The transaction is committed. Then, the RocketMQ broker delivers the half message to the consumer. |
| RollbackTransaction | The transaction is rolled back. Then, the RocketMQ broker deletes the half message and does not deliver it to the consumer. |
| Unknow | The transaction is in the unknown state. Generally, this value is used when you are not sure whether the transaction is successful or fails. The RocketMQ broker periodically checks the transactions that are in the unknown state. |

###### 3.1.5.5.5 OrderProducer

###### 3.1.5.5.5.1 send

Syntax: SendResult send(Message message, String shardingKey) Description: Sends an ordered message.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The ordered message that you want to send. |
| shardingKey | String | The selectivity factor for the ordered message. A specific message queue is selected based on the value of the shardingKey parameter. |

| Parameter | Description |
|---|---|
| SendResult | The sending result that is returned, including the message ID and topic. |

###### 3.1.5.5.5.2 isStarted

Syntax: public boolean isStarted() Description: Checks whether an instance is enabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is enabled. A value of true indicates that the instance is enabled. A value of false indicates that the instance is not enabled. |

###### 3.1.5.5.5.3 isClosed

Syntax: public boolean isClosed() Description: Checks whether an instance is disabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is disabled. A value of true indicates that the instance is disabled. A value of false indicates that the instance is not disabled. |

###### 3.1.5.5.5.4 start

Syntax: public void start() Description: Enables a producer instance to send ordered messages. Request parameters: none Response parameters: none

###### 3.1.5.5.5.5 shutdown

Syntax: public void shutdown() Description: Disables a producer instance from sending ordered messages. Request parameters: none Response parameters: none

##### 3.1.5.6 Message subscription

###### 3.1.5.6.1 Overview

This topic describes the methods for subscribing to various types of messages in Message Queue for Apache RocketMQ. The following figure shows the methods and parameters for different message types. Figure 1. Methods and parameters for subscribing to messages

###### 3.1.5.6.2 Consumer

###### 3.1.5.6.2.1 Overview

You can use a consumer instance to subscribe to regular messages, transactional messages, scheduled messages, or delayed messages.

###### 3.1.5.6.2.2 subscribe

Syntax: public void subscribe(String topic, String subExpression, MessageListener listener) Description: Subscribes to regular messages, transactional messages, scheduled messages, or delayed messages.

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the messages. |
| subExpression | String | The filter expression for subscribing to messages. The RocketMQ broker filters messages based on this expression. Only OR (\|\|) operations are supported. Example 1: "tag1 \|\| tag2 \|\| tag3"; Example 2: When the subExpression parameter is set to null or *, all messages are subscribed to. |
| listener | MessageListener | The message listener for callbacks. |

Response parameters: none

###### 3.1.5.6.2.3 unsubscribe

Syntax: void unsubscribe(String topic) Description: Cancels the subscription to a specific topic.

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the messages. |

Response parameters: none

###### 3.1.5.6.2.4 isStarted

Syntax: public boolean isStarted() Description: Checks whether an instance is enabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is enabled. A value of true indicates that the instance is enabled. A value of false indicates that the instance is not enabled. |

###### 3.1.5.6.2.5 isClosed

Syntax: public boolean isClosed() Description: Checks whether an instance is disabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is disabled. A value of true indicates that the instance is disabled. A value of false indicates that the instance is not disabled. |

###### 3.1.5.6.2.6 start

Syntax: public void start() Description: Enables a consumer instance. Request parameters: none Response parameters: none

###### 3.1.5.6.2.7 shutdown

Syntax: public void shutdown() Description: Disables a consumer instance. Request parameters: none Response parameters: none

###### 3.1.5.6.3 MessageListener

###### 3.1.5.6.3.1 Overview

A consumer registers a message listener to subscribe to messages. Thread security requirements: A message listener can be concurrently used by multiple threads of a consumer. You must ensure the security of concurrency.

###### 3.1.5.6.3.2 consume

Syntax: Action consume(Message message, ConsumeContext context) Description: Consumes messages. This method is called by applications. Unstable network conditions such as network jitter may result in message duplication. In this case, the consumer can perform idempotent processing for services that are sensitive to duplicated messages.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The message that you want to consume. |
| context | ConsumeContext | The context of the consumption. For more information, see ConsumeContext in the code. |

| Parameter | Description |
|---|---|
| Action | The result of the consumption. Consumption failed: An exception is thrown or Action.ReconsumeLater is returned. Action.ReconsumeLater indicates null. Consumption succeeded: Action.CommitMessage is returned. |

###### 3.1.5.6.4 Action

###### 3.1.5.6.4.1 Overview

The result of the consumption that is returned for a message. Enumeration

| Value | Type | Description |
|---|---|---|
| CommitMessage | String | The message is consumed. The consumer continues to consume the next message. |
| ReconsumeLater | String | The consumer failed to consume the message. The consumer requests the RocketMQ broker to redeliver the failed message later and continues to consume another message. |

###### 3.1.5.6.4.2 valueOf

Syntax: public static Action valueOf(String name) Description: Returns an enumerated constant of an enumerated type with the specified name. The specified string must exactly match the ID that is used to declare the enumerated constant. No extra space is allowed.

| Parameter | Type | Description |
|---|---|---|
| name | String | The name of the enumerated constant to return. |

| Parameter | Description |
|---|---|
| Action | The enumerated constant with the specified name that is returned. |

Exceptions

| Exception | Description |
|---|---|
| IllegalArgumentException | This exception is thrown because the enumerated type does not have an enumerated constant with the specified name. |
| NullPointerException | This exception is thrown because the value of the request parameter is null. |

###### 3.1.5.6.4.3 values

Syntax: public static Action[] values() Description: Returns an array of constants in the declared order of constants of an enumerated type. Request parameters: none

| Parameter | Description |
|---|---|
| Action[] | The array of constants in the declared order of constants of the enumerated type that is returned. |

###### 3.1.5.6.5 PropertyValueConst

The constant that specifies the consumption mode. Enumeration

| Value | Type | Description |
|---|---|---|
| BROADCASTING | String | The broadcasting consumption mode. |
| CLUSTERING | String | The clustering consumption mode. |

###### 3.1.5.6.6 OrderConsumer

###### 3.1.5.6.6.1 Overview

You can use a consumer instance of ordered messages to subscribe to messages in first in, first out (FIFO) order.

###### 3.1.5.6.6.2 subscribe

Syntax: void subscribe(String topic, String subExpression, MessageOrderListener listener) Description: Subscribes to ordered messages.

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the messages. |
| subExpression | String | The filter expression for subscribing to messages. The RocketMQ broker filters messages based on this expression. Only OR (\|\|) operations are supported. Example 1: "tag1 \|\| tag2 \|\| tag3"; Example 2: When the subExpression parameter is set to null or *, all messages are subscribed to. |
| listener | MessageOrd erListener | The message listener for callbacks. |

Response parameters: none

###### 3.1.5.6.6.3 unsubscribe

Syntax: void unsubscribe(String topic) Description: Cancels the subscription to a specific topic.

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the messages. |

Response parameters: none

###### 3.1.5.6.6.4 isStarted

Syntax: public boolean isStarted() Description: Checks whether an instance is enabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is enabled. A value of true indicates that the instance is enabled. A value of false indicates that the instance is not enabled. |

###### 3.1.5.6.6.5 isClosed

Syntax: public boolean isClosed() Description: Checks whether an instance is disabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is disabled. A value of true indicates that the instance is disabled. A value of false indicates that the instance is not disabled. |

###### 3.1.5.6.6.6 start

Syntax: public void start() Description: Enables a consumer instance. Request parameters: none Response parameters: none

###### 3.1.5.6.6.7 shutdown

Syntax: public void shutdown() Description: Disables a consumer instance. Request parameters: none Response parameters: none

###### 3.1.5.6.7 MessageOrderListener

###### 3.1.5.6.7.1 Overview

A consumer registers an ordered message listener to subscribe to ordered messages. Thread security requirements: A message listener can be concurrently used by multiple threads of a consumer. You must ensure the security of concurrency.

###### 3.1.5.6.7.2 consume

Syntax: OrderAction consume(Message message, ConsumeOrderContext context) Description: Consumes messages. This method is called by applications. Unstable network conditions such as network jitter may result in message duplication. In this case, the consumer can perform idempotent processing for services that are sensitive to duplicated messages.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The message that you want to consume. |
| context | ConsumeOrderContext | The context of the consumption. For more information, see ConsumeOrderContext in the code. |

| Parameter | Description |
|---|---|
| OrderAction | The result of the consumption. Consumption failed: An exception is thrown or Action.Suspend is returned. Action.Suspend indicates null. Consumption succeeded: Action.Success is returned. |

###### 3.1.5.6.8 OrderAction

###### 3.1.5.6.8.1 Overview

The result of the consumption that is returned for an ordered message. Enumeration

| Value | Type | Description |
|---|---|---|
| Success | String | The message is consumed. The consumer continues to consume the next message. |
| Suspend | String | The consumer failed to consume the message. The current queue is suspended. |

###### 3.1.5.6.8.2 valueOf

Syntax: public static OrderAction valueOf(String name) Description: Returns an enumerated constant of an enumerated type with the specified name. The specified string must exactly match the ID that is used to declare the enumerated constant. No extra space is allowed.

| Parameter | Type | Description |
|---|---|---|
| name | String | The name of the enumerated constant to return. |

| Parameter | Description |
|---|---|
| OrderAction | The enumerated constant with the specified name that is returned. |

Exceptions

| Exception | Description |
|---|---|
| IllegalArgumentException | This exception is thrown because the enumerated type does not have an enumerated constant with the specified name. |
| NullPointerException | This exception is thrown because the value of the request parameter is null. |

###### 3.1.5.6.8.3 values

Syntax: public static OrderAction[] values() Description: Returns an array of constants in the declared order of constants of an enumerated type. Request parameters: none

| Parameter | Description |
|---|---|
| OrderAction[] | The array of constants in the declared order of constants of the enumerated type that is returned. |

###### 3.1.5.6.9 BatchConsumer

###### 3.1.5.6.9.1 Overview

You can use a batch consumer instance to subscribe to multiple messages at a time.

###### 3.1.5.6.9.2 subscribe

Syntax: void subscribe(String topic, String subExpression, BatchMessageListener listener) Description: Subscribes to regular messages, transactional messages, scheduled messages, or delayed messages.

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the messages. |
| subExpression | String | The filter expression for subscribing to messages. The RocketMQ broker filters messages based on this expression. Only OR (\|\|) operations are supported. Example 1: "tag1 \|\| tag2 \|\| tag3"; Example 2: When the subExpression parameter is set to null or *, all messages are subscribed to. |
| listener | BatchMess ageListener | The message listener for callbacks. |

Response parameters: none

###### 3.1.5.6.9.3 unsubscribe

Syntax: void unsubscribe(String topic) Description: Cancels the subscription to a specific topic.

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the messages. |

Response parameters: none

###### 3.1.5.6.9.4 isStarted

Syntax: public boolean isStarted() Description: Checks whether an instance is enabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is enabled. A value of true indicates that the instance is enabled. A value of false indicates that the instance is not enabled. |

###### 3.1.5.6.9.5 isClosed

Syntax: public boolean isClosed() Description: Checks whether an instance is disabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is disabled. A value of true indicates that the instance is disabled. A value of false indicates that the instance is not disabled. |

###### 3.1.5.6.9.6 start

Syntax: public void start() Description: Enables a consumer instance. Request parameters: none Response parameters: none

###### 3.1.5.6.9.7 shutdown

Syntax: public void shutdown() Description: Disables a consumer instance. Request parameters: none Response parameters: none

###### 3.1.5.6.10 BatchMessageListener

###### 3.1.5.6.10.1 Overview

A consumer registers a batch message listener to consume multiple messages at a time. Thread security requirements: A message listener can be concurrently used by multiple threads of a consumer. You must ensure the security of concurrency.

###### 3.1.5.6.10.2 consume

Syntax: Action consume(Message message, ConsumeContext context) Description: Consumes multiple messages at a time. This method is called by applications. Unstable network conditions such as network jitter may result in message duplication. In this case, the consumer can perform idempotent processing for services that are sensitive to duplicated messages.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The messages that you want to consume. |
| context | ConsumeContext | The context of the consumption. For more information, see ConsumeContext in the code. |

| Parameter | Description |
|---|---|
| Action | The result of the consumption. Consumption failed: An exception is thrown or Action.ReconsumeLater is returned. Action.ReconsumeLater indicates null. Consumption succeeded: Action.CommitMessage is returned. |
