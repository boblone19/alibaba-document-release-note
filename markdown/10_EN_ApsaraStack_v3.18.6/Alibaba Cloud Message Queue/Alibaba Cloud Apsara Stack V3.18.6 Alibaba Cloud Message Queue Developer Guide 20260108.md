---
title: "Alibaba Cloud Message Queue Developer Guide 20260108"
product_version: "V3.18.6"
pdf_pages: 386
source_pdf: "e5599c91e48fd757_Alibaba Cloud Apsara Stack V3.18.6 Alibaba Cloud Message Queue Developer Guide 20260108.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97%20MQ/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Alibaba%20Cloud%20Message%20Queue%20Developer%20Guide%2020260108.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Message Queue Developer Guide 20260108

## Table of Contents

- 1 Prerequisites
  - 1.1 Obtain API information and its endpoint
  - 1.2 Obtain an AccessKey pair
  - 1.3 Obtain common header parameters
  - 1.4 Obtain STS access credentials
- 2 Calling private cloud APIs through a POP gateway
  - 2.1 Overview
  - 2.2 Preparations
  - 2.3 SDK for Java
- 3 API reference
  - 3.1 RocketMQ_API
    - 3.1.1 Updates
    - 3.1.2 Overview
      - 3.1.2.1 Intended audience and scenarios
      - 3.1.2.2 Scenarios and limits
      - 3.1.2.3 Basic principles
    - 3.1.3 Common parameters
      - 3.1.3.1 Common request parameters
      - 3.1.3.2 Common response parameters
    - 3.1.4 Common terms
      - 3.1.4.1 Account security
        - 3.1.4.1.1 AccessKey
        - 3.1.4.1.2 SecretKey
      - 3.1.4.2 Resource management
        - 3.1.4.2.1 Topic
        - 3.1.4.2.2 Group ID
    - 3.1.5 Error codes
    - 3.1.6 API reference
      - 3.1.6.1 Instance management
        - 3.1.6.1.1 QueryCommonGenRedirectUrl
        - 3.1.6.1.2 QueryTrendFlowLimit
        - 3.1.6.1.3 UnbindSystemTags
        - 3.1.6.1.4 CreateInstance
        - 3.1.6.1.5 BindSystemTags
        - 3.1.6.1.6 QuerySystemTagList
        - 3.1.6.1.7 DeleteInstance
        - 3.1.6.1.8 QueryInstanceBaseInfo
        - 3.1.6.1.9 QueryInstanceStatistics
        - 3.1.6.1.10 QueryInstanceList
        - 3.1.6.1.11 QueryRouterInstanceList
        - 3.1.6.1.12 UpdateInstance
        - 3.1.6.1.13 CheckFortestInstance
      - 3.1.6.2 Topic management
        - 3.1.6.2.1 CheckFortestTopic
        - 3.1.6.2.2 PageQueryTopicList
        - 3.1.6.2.3 CreateSubscription
        - 3.1.6.2.4 CreateTopic
        - 3.1.6.2.5 DeleteTopic
        - 3.1.6.2.6 DeleteSubscription
        - 3.1.6.2.7 QueryTrendTopicInputTps
        - 3.1.6.2.8 QueryTopicSubDetail
        - 3.1.6.2.9 QueryTopicStatus
        - 3.1.6.2.10 QueryTopicNameList
        - 3.1.6.2.11 QueryTopicListByGroupId
        - 3.1.6.2.12 QueryTopicList
        - 3.1.6.2.13 QueryTopic
        - 3.1.6.2.14 QuerySubscriptionList
        - 3.1.6.2.15 QuerySubscription
        - 3.1.6.2.16 QueryRouterTopicList
        - 3.1.6.2.17 UpdateTopicInfo
        - 3.1.6.2.18 UpdateTopic
        - 3.1.6.2.19 UpdateSubscription
        - 3.1.6.2.20 SearchSubscription
      - 3.1.6.3 Cluster management
        - 3.1.6.3.1 QueryClusterList
        - 3.1.6.3.2 QueryClusterCapacity
      - 3.1.6.4 Group management
        - 3.1.6.4.1 CreateGroup
        - 3.1.6.4.2 PageQueryGroupList
        - 3.1.6.4.3 DeleteGroup
        - 3.1.6.4.4 QueryGroupIdList
        - 3.1.6.4.5 QueryGroupSubDetail
        - 3.1.6.4.6 QueryGroupList
        - 3.1.6.4.7 QueryTrendGroupOutputTps
        - 3.1.6.4.8 UpdateGroupInfo
        - 3.1.6.4.9 UpdateGroupConsumer
      - 3.1.6.5 CloudInfo management
        - 3.1.6.5.1 QueryCloudInfoNoPage
        - 3.1.6.5.2 UpdateCloudInfo
        - 3.1.6.5.3 DeleteCloudInfo
        - 3.1.6.5.4 CreateCloudInfo
        - 3.1.6.5.5 QueryCloudInfo
      - 3.1.6.6 Message management
        - 3.1.6.6.1 PushMessage
        - 3.1.6.6.2 DownloadMessageBodyInDLQ
        - 3.1.6.6.3 DownloadMessageAllInDLQ
        - 3.1.6.6.4 DownloadMessage
        - 3.1.6.6.5 QueryMessageByPagedTopic
        - 3.1.6.6.6 QueryMessageByPagedDLQ
        - 3.1.6.6.7 QueryMessageByKey
        - 3.1.6.6.8 QueryMessageByIdInDLQ
        - 3.1.6.6.9 QueryMessageById
        - 3.1.6.6.10 TraceMessage
        - 3.1.6.6.11 SendMessage
        - 3.1.6.6.12 ResendMessageByIdInDLQ
      - 3.1.6.7 Empower management
        - 3.1.6.7.1 CheckFortestRamAction
        - 3.1.6.7.2 DeleteDauthToolByUserId
        - 3.1.6.7.3 CreateGroupEmpowerBySub
        - 3.1.6.7.4 CreateEmpowerBySub
        - 3.1.6.7.5 CreateEmpower
        - 3.1.6.7.6 QueryGroupEmpowerList
        - 3.1.6.7.7 QueryEmpowerList
        - 3.1.6.7.8 DeleteGroupEmpower
        - 3.1.6.7.9 DeleteEmpower
      - 3.1.6.8 MQTT management API
        - 3.1.6.8.1 DeleteMqttGroupId
        - 3.1.6.8.2 SendMqtt
        - 3.1.6.8.3 QueryMqttMsgTransTask
        - 3.1.6.8.4 CreateMqttInstanceStoreResource
        - 3.1.6.8.5 CreateMqttInstance
        - 3.1.6.8.6 CreateMqttGroupId
        - 3.1.6.8.7 PageQueryMqttInstanceStoreResource
        - 3.1.6.8.8 PageQueryMqttInstanceList
        - 3.1.6.8.9 PageQueryMqttGroupId
        - 3.1.6.8.10 DeleteMqttInstanceStoreResource
        - 3.1.6.8.11 DeleteMqttInstance
        - 3.1.6.8.12 QueryMqttInstanceReport
        - 3.1.6.8.13 QueryMqttInstanceList
        - 3.1.6.8.14 QueryMqttInstanceBaseInfo
        - 3.1.6.8.15 QueryMqttGroupIdList
        - 3.1.6.8.16 QueryMqttDeviceRunningInfo
        - 3.1.6.8.17 QueryMqttConnectionSum
        - 3.1.6.8.18 QueryMqttClientSetByTopic
        - 3.1.6.8.19 QueryMqttClientSetByGroupId
        - 3.1.6.8.20 QueryMqttTraceByTraceId
        - 3.1.6.8.21 QueryMqttMsgByPubInfo
        - 3.1.6.8.22 QueryMqttInstanceStoreResourceNameList
        - 3.1.6.8.23 QueryMqttInstanceStoreInstanceList
        - 3.1.6.8.24 UpdateMqttInstance
        - 3.1.6.8.25 ChangeMqttInstanceSpec
        - 3.1.6.8.26 BindMqttInstance
      - 3.1.6.9 Trace management
        - 3.1.6.9.1 QueryTraceMapByQueryId
        - 3.1.6.9.2 QueryPubTraceByQueryId
        - 3.1.6.9.3 PageQueryTraceListByUserId
        - 3.1.6.9.4 DeleteTraceQueryTask
        - 3.1.6.9.5 QueryTraceByMsgTopic
        - 3.1.6.9.6 QueryTraceByMsgKey
        - 3.1.6.9.7 QueryTraceByMsgId
      - 3.1.6.10 Consumer management
        - 3.1.6.10.1 CheckFortestConsumerId
        - 3.1.6.10.2 QueryAllConsumerAccumulation
        - 3.1.6.10.3 QueryConsumerTimespan
        - 3.1.6.10.4 QueryConsumerStatus
        - 3.1.6.10.5 QueryConsumerProgress
        - 3.1.6.10.6 QueryConsumerJstackInfo
        - 3.1.6.10.7 QueryConsumerConnection
        - 3.1.6.10.8 QueryConsumerAccumulate
        - 3.1.6.10.9 UpdateConsumerReadableByTopicAndGroup
        - 3.1.6.10.10 ResetConsumerOffset
        - 3.1.6.10.11 QueryUnitLatestConsumerTime
      - 3.1.6.11 MQ connector management
        - 3.1.6.11.1 ResumeMqConnector
        - 3.1.6.11.2 PauseMqConnector
        - 3.1.6.11.3 DeleteDeploymentMqConnector
        - 3.1.6.11.4 CreateDeploymentMqConnector
        - 3.1.6.11.5 DeployDeploymentMqConnector
        - 3.1.6.11.6 QueryMqConnectorSysResourceName
        - 3.1.6.11.7 QueryMqConnectorMetricsDetailList
        - 3.1.6.11.8 QueryMqConnectorInfoList
        - 3.1.6.11.9 QueryMqConnectorDeploymentList
        - 3.1.6.11.10 UpdateMqConnectorDeployment
      - 3.1.6.12 Router task management
        - 3.1.6.12.1 DeleteCloudRouterTask
        - 3.1.6.12.2 CreateRouterTask
        - 3.1.6.12.3 CreateRouterInnerTask
        - 3.1.6.12.4 CreateCloudRouterTask
        - 3.1.6.12.5 QueryCloudRouterTaskStats
        - 3.1.6.12.6 QueryCloudRouterTask
        - 3.1.6.12.7 QueryCloudRouterItems
        - 3.1.6.12.8 PageQueryCloudRouterTask
        - 3.1.6.12.9 DeleteRouterTask
        - 3.1.6.12.10 DeleteRouterInnerTask
        - 3.1.6.12.11 QueryRouterTask
        - 3.1.6.12.12 QueryRouterStat
        - 3.1.6.12.13 QueryRouterInnerTask
        - 3.1.6.12.14 QueryRouterInnerStat
        - 3.1.6.12.15 UpdateRouterFilterRule
        - 3.1.6.12.16 UpdateCloudRouterTask
        - 3.1.6.12.17 StopRouterTask
        - 3.1.6.12.18 StopCloudRouterTask
        - 3.1.6.12.19 StartRouterTask
        - 3.1.6.12.20 StartRouterInnerTask
        - 3.1.6.12.21 StartCloudRouterTask
        - 3.1.6.12.22 SearchRouterTask
        - 3.1.6.12.23 AddRouterInnerConfig
      - 3.1.6.13 VPC management
        - 3.1.6.13.1 CreateVpcTunnelInstanceSingleTunnel
        - 3.1.6.13.2 DeleteVpcTunnelInstanceSingleTunnel
        - 3.1.6.13.3 QueryVpcTunnelTunnelSwitch
        - 3.1.6.13.4 QueryVpcTunnelInstanceSingleTunnelList
      - 3.1.6.14 Region management
        - 3.1.6.14.1 QueryMetaData
        - 3.1.6.14.2 QueryCommonRegionData
        - 3.1.6.14.3 QueryRegionList
        - 3.1.6.14.4 QueryRegionConsoleUrlList
      - 3.1.6.15 UnitResetTask management
        - 3.1.6.15.1 CreateUnitResetTask
        - 3.1.6.15.2 QueryUnitResetTask
- 4 SDK reference
  - 4.1 RocketMQ_SDK
    - 4.1.1 Overview
    - 4.1.2 Messaging model
    - 4.1.3 Updates
    - 4.1.4 Transport protocol and character encoding
    - 4.1.5 Common classes and methods
      - 4.1.5.1 PropertyKeyConst
      - 4.1.5.2 ONSFactory
        - 4.1.5.2.1 createConsumer
        - 4.1.5.2.2 createBatchConsumer
        - 4.1.5.2.3 createOrderedConsumer
        - 4.1.5.2.4 createOrderProducer
        - 4.1.5.2.5 createProducer
        - 4.1.5.2.6 createTransactionProducer
      - 4.1.5.3 Message
        - 4.1.5.3.1 Overview
        - 4.1.5.3.2 Default message construction
        - 4.1.5.3.3 Message construction by using parameters (1)
        - 4.1.5.3.4 Message construction by using parameters (2)
        - 4.1.5.3.5 putUserProperties
        - 4.1.5.3.6 getUserProperties
        - 4.1.5.3.7 getTopic
        - 4.1.5.3.8 setTopic
        - 4.1.5.3.9 getTag
        - 4.1.5.3.10 setTag
        - 4.1.5.3.11 getKey
        - 4.1.5.3.12 setKey
        - 4.1.5.3.13 getMsgID
        - 4.1.5.3.14 setMsgID
        - 4.1.5.3.15 getReconsumeTimes
        - 4.1.5.3.16 setReconsumeTimes
        - 4.1.5.3.17 getBornTimestamp
        - 4.1.5.3.18 setBornTimestamp
        - 4.1.5.3.19 getBornHost
        - 4.1.5.3.20 setBornHost
        - 4.1.5.3.21 getStartDeliverTime
        - 4.1.5.3.22 setStartDeliverTime
        - 4.1.5.3.23 getShardingKey
        - 4.1.5.3.24 setShardingKey
      - 4.1.5.4 ONSClientException
        - 4.1.5.4.1 Default ONSClientException construction
        - 4.1.5.4.2 ONSClientException construction by using parameters (1)
        - 4.1.5.4.3 ONSClientException construction by using parameters (2)
        - 4.1.5.4.4 ONSClientException construction by using parameters (3)
      - 4.1.5.5 Message sending
        - 4.1.5.5.1 Overview
        - 4.1.5.5.2 SendResult
          - 4.1.5.5.2.1 Default SendResult construction
          - 4.1.5.5.2.2 getMessageId
          - 4.1.5.5.2.3 getTopic
          - 4.1.5.5.2.4 toString
        - 4.1.5.5.3 Producer
          - 4.1.5.5.3.1 Overview
          - 4.1.5.5.3.2 send
          - 4.1.5.5.3.3 sendOneway
          - 4.1.5.5.3.4 sendAsync
          - 4.1.5.5.3.5 isStarted
          - 4.1.5.5.3.6 isClosed
          - 4.1.5.5.3.7 start
          - 4.1.5.5.3.8 shutdown
        - 4.1.5.5.4 TransactionProducer
          - 4.1.5.5.4.1 send
          - 4.1.5.5.4.2 isStarted
          - 4.1.5.5.4.3 isClosed
          - 4.1.5.5.4.4 start
          - 4.1.5.5.4.5 shutdown
          - 4.1.5.5.4.6 LocalTransactionExecuter
          - 4.1.5.5.4.7 TransactionStatus
        - 4.1.5.5.5 OrderProducer
          - 4.1.5.5.5.1 send
          - 4.1.5.5.5.2 isStarted
          - 4.1.5.5.5.3 isClosed
          - 4.1.5.5.5.4 start
          - 4.1.5.5.5.5 shutdown
      - 4.1.5.6 Message subscription
        - 4.1.5.6.1 Overview
        - 4.1.5.6.2 Consumer
          - 4.1.5.6.2.1 Overview
          - 4.1.5.6.2.2 subscribe
          - 4.1.5.6.2.3 unsubscribe
          - 4.1.5.6.2.4 isStarted
          - 4.1.5.6.2.5 isClosed
          - 4.1.5.6.2.6 start
          - 4.1.5.6.2.7 shutdown
        - 4.1.5.6.3 MessageListener
          - 4.1.5.6.3.1 Overview
          - 4.1.5.6.3.2 consume
        - 4.1.5.6.4 Action
          - 4.1.5.6.4.1 Overview
          - 4.1.5.6.4.2 valueOf
          - 4.1.5.6.4.3 values
        - 4.1.5.6.5 PropertyValueConst
        - 4.1.5.6.6 OrderConsumer
          - 4.1.5.6.6.1 Overview
          - 4.1.5.6.6.2 subscribe
          - 4.1.5.6.6.3 unsubscribe
          - 4.1.5.6.6.4 isStarted
          - 4.1.5.6.6.5 isClosed
          - 4.1.5.6.6.6 start
          - 4.1.5.6.6.7 shutdown
        - 4.1.5.6.7 MessageOrderListener
          - 4.1.5.6.7.1 Overview
          - 4.1.5.6.7.2 consume
        - 4.1.5.6.8 OrderAction
          - 4.1.5.6.8.1 Overview
          - 4.1.5.6.8.2 valueOf
          - 4.1.5.6.8.3 values
        - 4.1.5.6.9 BatchConsumer
          - 4.1.5.6.9.1 Overview
          - 4.1.5.6.9.2 subscribe
          - 4.1.5.6.9.3 unsubscribe
          - 4.1.5.6.9.4 isStarted
          - 4.1.5.6.9.5 isClosed
          - 4.1.5.6.9.6 start
          - 4.1.5.6.9.7 shutdown
        - 4.1.5.6.10 BatchMessageListener
          - 4.1.5.6.10.1 Overview
          - 4.1.5.6.10.2 consume

## 1 Prerequisites

### 1.1 Obtain API information and its endpoint

**endpoint**

To call an API operation for a cloud product, you must obtain information about the operation, such as the product name (code), API operation name, and API version.

**Background information**

The API information in the API directory of the Apsara Uni-manager Management Console is for reference only. For detailed instructions on using an API operation, refer to the developer guide for the specific cloud product. If any inconsistencies exist, the information in the developer guide takes precedence.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top menu bar, choose **Products** > **Developer Tools** > **APIs and Tools** >
**Developer Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.
4. In the navigation pane on the left, select the desired cloud product.
5. From the **Version** drop-down list, select the target API version.
6. The page displays a list of all API operations for the current version.
7. Click a desired API operation. In the list of parameters, find the POP Endpoint information.

### 1.2 Obtain an AccessKey pair

You can use an AccessKey pair to authenticate API calls. AccessKey pairs support two authorization modes: Resource Access Management (RAM) and Security Token Service (STS). This topic describes how to obtain a RAM-authorized AccessKey pair.

**Background information**

An AccessKey pair is used to verify the identity of a requester. An AccessKey pair consists of an AccessKey ID and an AccessKey secret, which are used for symmetric encryption. The AccessKey ID identifies the user, and the AccessKey secret is used to encrypt the signature string. The two authorization modes for an AccessKey pair are as follows: An AccessKey ID and an AccessKey secret authorized by RAM for a third-party requester. An AccessKey ID, an AccessKey secret, and a security token authorized by STS for a thirdparty requester. For more information, see Obtain an STS AccessKey. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only operations administrators and administrators of level-1 organizations can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pair of a personal account to call APIs of the Apsara Uni-manager Management Console and cloud products. When you use a personal account AccessKey pair, you may need to add specific parameters to the request header to prevent errors related to insufficient permissions.

> **Warning:** A personal account AccessKey is a restricted key managed by the permission system of the Apsara Uni-manager Management Console. An organization AccessKey has higher permissions. An administrator must ensure that operations that use this key are secure.

| Parameter | Description |
|---|---|
| x-acs-regionid | The region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain the organization ID, see the Apsara Uni-manager Management Console Developer Guide topic GetOrganizationList. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain the resource set ID, see the Apsara Uni-manager Management Console Developer Guide topic ListResourceGroup. |
| x-acs-instanceid | The ID of the instance that you want to manage. For example, you can find the ID of an Elastic Compute Service (ECS) instance in the ECS instance list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner, click your profile picture, and then click **User Information**.
3. In the **AccessKey** section, you can view the AccessKey information for your account.

> **Note:** An AccessKey pair consists of an AccessKey ID and an AccessKey secret. This pair grants full access to your cloud resources. Keep your AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top menu bar, click **Enterprise**.
3. In the left navigation pane, choose **Resource Management > Organization**
**Management**.
4. In the organization chart, click the name of the target level-1 organization.
5. Click the **Management AccessKey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### 1.3 Obtain common header parameters

**parameters**

You must provide multiple header parameters when you call an API. This topic describes how to obtain these parameters and explains the response parameters.

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the navigation pane on the left, choose **Resource Management** > **Region**
**Management**.
4. Click the name of the target organization.
5. In the **Region List** on the right, find the Region ID in the **Region Name** column.

**Obtain an organization ID**

Call an API operation to obtain an organization ID. You can use the API debugging feature in the Apsara Uni-manager Management Console to obtain the ID.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Products** and choose **Developer Tools** > **API and Tools** >
**Developer Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.
4. Click the
button and choose **Platform** > **Apsara Uni-manager**. Set **Version** to **2019-**
**05-10**.
5. In the text box, enter `GetOrganizationList` to start online debugging. Set the name
parameter to the name of your target organization and initiate the call. After the call succeeds, find the organization ID in the **id** parameter on the **Call Result** tab. For more information, see the GetOrganizationList topic in the Apsara Uni-manager Management Con sole Developer Guide.

**Obtain a resource group ID**

Call an API operation to obtain a resource group ID. You can use the API debugging feature in the Apsara Uni-manager Management Console to obtain the ID.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Products** and choose **Developer Tools** > **API and Tools** >
**Developer Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.
4. Click the
button and choose **Platform** > **Apsara Uni-manager**. Set **Version** to **2019-**
**05-10**.
5. In the text box, enter `ListResourceGroup` to start online debugging. After the call
succeeds, find the resource group ID in the **id** parameter on the **Call Result** tab. For more information, see the ListResourceGroup topic in the Apsara Uni-manager Management Cons ole Developer Guide.

**Obtain an instance ID**

You can obtain an instance ID from the instance list of a cloud product in the Apsara Unimanager Management Console. This topic uses ApsaraMQ for RocketMQ as an example.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Middleware** > **Message Queue** >
**ApsaraMQ for RocketMQ**.
3. In the navigation pane on the left, click **Instance List**.
4. Find the ID in the **Instance ID** column.
When you call an API operation to query a list of resource instances for a cloud service, the following parameters are returned by default.

| Name | Description |
|---|---|
| ResourceGroupName | The name of the resource group. |
| ResourceGroup | The ID of the resource group. |

| DepartmentName | The name of the organization. |
|---|---|
| Department | The ID of the organization. |

### 1.4 Obtain STS access credentials

This topic describes how to use Security Token Service (STS) to call product APIs in Apsara Stack.

**Background information**

Security Token Service (STS) is an Alibaba Cloud service that provides temporary access permission management. You can use STS to call product APIs in Apsara Stack.

**Procedure**

1. You can obtain the `RAM Role` of the user.
i. Log on to the Apsara Uni-manager Management Console. ii. In the upper-right corner of the page, click the profile picture and select **User**
**Information**.
iii. Click **View Current Role Policy**. In the **Current Role Policy** dialog box, you can view the `RAM Role` .
2. Use the following code to obtain an AccessKey ID ( `stsAK` ), AccessKey secret ( `stsSK` ),
and Security Token Service token ( `stsToken` ) by assuming the RAM role.

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

3. Use the STS credentials to call cloud product APIs. The following example shows how to
initialize the credential client.

```java
import com.aliyun.credentials.Client; import com.aliyun.credentials.models.Config; // The following example shows how to initialize a credential client using an STS tok en. // This example does not include the procedure for obtaining an STS token. public class DemoStsTest {
    public static void main(String[] args) {
        Config credentialConfig = new Config();
        credentialConfig.setType("sts");
        // Replace this value with the AccessKey ID from the STS credentials obtained
in the previous step.
        credentialConfig.setAccessKeyId("your_AccessKeyId");
        // Replace this value with the AccessKey secret from the STS credentials obta
ined in the previous step.
        credentialConfig.setAccessKeySecret("your_AccessKeySecret");
        // Replace this value with the security token from the STS credentials obtain
ed in the previous step.
        credentialConfig.setSecurityToken("your_SecurityToken");
        Client credentialClient = new Client(credentialConfig);
        // You can now use the client to call APIs. For more information, see the rel
evant API documentation.
```

cloud APIs through a POP gatewa

## 2 Calling private cloud APIs through a POP gateway

**through a POP gateway**

### 2.1 Overview

You can use the point of presence (POP) gateway to call API operations in Apsara Stack in the same way as in Alibaba Cloud public cloud. This topic provides an overview.

**Background information**

By calling Apsara Stack API operations through the POP gateway, you can perform operations such as creating, deleting, modifying, and querying on management layer resources (such as instances, topics, and groups). The platform has encapsulated an SDK that supports the Java language. You can download this SDK from the platform to directly call Apsara Stack API operations. The SDK code examples for API operations in this document are for reference only. For complete usage steps and parameter descriptions of each API operation, see the SDK examples and OpenAPI documentation in the developer portal.

**Environment requirements**

Supports JDK8 through JDK19 Platform support: Linux, Mac, Windows

**Language**

Currently only the Java language is supported.

**Release notes**

**SDK version**

| Version number | Release date | Updates |
|---|---|---|
| 3.16.2-0 | 2024.09 | Released the Apsara Stack 3.16.2 SDK from which external API operations can be called. |

**API operations**

The API operations currently supported by the Apsara Stack Enterprise Edition SDK.

| API name | Version |
|---|---|
| BindSystemTags | 3.16.2-0 |
| CheckFortestConsumerId | 3.16.2-0 |

cloud APIs through a POP gatewa

| CheckFortestInstance | 3.16.2-0 |
|---|---|
| CheckFortestRamAction | 3.16.2-0 |
| CheckFortestTopic | 3.16.2-0 |
| CreateCloudInfo | 3.16.2-0 |
| CreateCloudRouterTask | 3.16.2-0 |
| CreateDeploymentMqConnector | 3.16.2-0 |
| CreateEmpower | 3.16.2-0 |
| CreateEmpowerBySub | 3.16.2-0 |
| CreateGroup | 3.16.2-0 |
| CreateGroupEmpowerBySub | 3.16.2-0 |
| CreateInstance | 3.16.2-0 |
| CreateTopic | 3.16.2-0 |
| CreateUnitResetTask | 3.16.2-0 |
| CreateVpcTunnelInstanceSingleTunnel | 3.16.2-0 |
| DeleteCloudInfo | 3.16.2-0 |
| DeleteCloudRouterTask | 3.16.2-0 |
| DeleteDeploymentMqConnector | 3.16.2-0 |
| DeleteEmpower | 3.16.2-0 |
| DeleteGroup | 3.16.2-0 |

cloud APIs through a POP gatewa

| DeleteGroupEmpower | 3.16.2-0 |
|---|---|
| DeleteInstance | 3.16.2-0 |
| DeleteTopic | 3.16.2-0 |
| DeleteTraceQueryTask | 3.16.2-0 |
| DeleteVpcTunnelInstanceSingleTunnel | 3.16.2-0 |
| DeployDeploymentMqConnector | 3.16.2-0 |
| DownloadMessage | 3.16.2-0 |
| DownloadMessageAllInDLQ | 3.16.2-0 |
| DownloadMessageBodyInDLQ | 3.16.2-0 |
| PageQueryCloudRouterTask | 3.16.2-0 |
| PageQueryGroupList | 3.16.2-0 |
| PageQueryTopicList | 3.16.2-0 |
| PageQueryTraceListByUserId | 3.16.2-0 |
| PauseMqConnector | 3.16.2-0 |
| PushMessage | 3.16.2-0 |
| QueryAllConsumerAccumulation | 3.16.2-0 |
| QueryCloudInfo | 3.16.2-0 |
| QueryCloudRouterItems | 3.16.2-0 |
| QueryCloudRouterTask | 3.16.2-0 |

cloud APIs through a POP gatewa

| QueryCloudRouterTaskStats | 3.16.2-0 |
|---|---|
| QueryClusterCapacity | 3.16.2-0 |
| QueryClusterList | 3.16.2-0 |
| QueryCommonGenRedirectUrl | 3.16.2-0 |
| QueryCommonRegionData | 3.16.2-0 |
| QueryConsumerAccumulate | 3.16.2-0 |
| QueryConsumerConnection | 3.16.2-0 |
| QueryConsumerJstackInfo | 3.16.2-0 |
| QueryConsumerProgress | 3.16.2-0 |
| QueryConsumerStatus | 3.16.2-0 |
| QueryConsumerTimespan | 3.16.2-0 |
| QueryEmpowerList | 3.16.2-0 |
| QueryGroupEmpowerList | 3.16.2-0 |
| QueryGroupIdList | 3.16.2-0 |
| QueryGroupList | 3.16.2-0 |
| QueryGroupSubDetail | 3.16.2-0 |
| QueryInstanceBaseInfo | 3.16.2-0 |
| QueryInstanceList | 3.16.2-0 |
| QueryInstanceStatistics | 3.16.2-0 |

cloud APIs through a POP gatewa

| QueryMessageById | 3.16.2-0 |
|---|---|
| QueryMessageByIdInDLQ | 3.16.2-0 |
| QueryMessageByKey | 3.16.2-0 |
| QueryMessageByPagedDLQ | 3.16.2-0 |
| QueryMessageByPagedTopic | 3.16.2-0 |
| QueryMetaData | 3.16.2-0 |
| QueryMqConnectorDeploymentList | 3.16.2-0 |
| QueryMqConnectorInfoList | 3.16.2-0 |
| QueryMqConnectorMetricsDetailList | 3.16.2-0 |
| QueryMqConnectorSysResourceName | 3.16.2-0 |
| QueryPubTraceByQueryId | 3.16.2-0 |
| QueryRegionConsoleUrlList | 3.16.2-0 |
| QueryRegionList | 3.16.2-0 |
| QueryRouterInstanceList | 3.16.2-0 |
| QueryRouterTopicList | 3.16.2-0 |
| QuerySubscriptionList | 3.16.2-0 |
| QuerySystemTagList | 3.16.2-0 |
| QueryTopic | 3.16.2-0 |
| QueryTopicList | 3.16.2-0 |

cloud APIs through a POP gatewa

| QueryTopicListByGroupId | 3.16.2-0 |
|---|---|
| QueryTopicNameList | 3.16.2-0 |
| QueryTopicStatus | 3.16.2-0 |
| QueryTopicSubDetail | 3.16.2-0 |
| QueryTraceByMsgId | 3.16.2-0 |
| QueryTraceByMsgKey | 3.16.2-0 |
| QueryTraceByMsgTopic | 3.16.2-0 |
| QueryTraceMapByQueryId | 3.16.2-0 |
| QueryTrendFlowLimit | 3.16.2-0 |
| QueryTrendGroupOutputTps | 3.16.2-0 |
| QueryTrendTopicInputTps | 3.16.2-0 |
| QueryUnitLatestConsumerTime | 3.16.2-0 |
| QueryUnitResetTask | 3.16.2-0 |
| QueryVpcTunnelInstanceSingleTunnelList | 3.16.2-0 |
| QueryVpcTunnelTunnelSwitch | 3.16.2-0 |
| ResendMessageByIdInDLQ | 3.16.2-0 |
| ResetConsumerOffset | 3.16.2-0 |
| ResumeMqConnector | 3.16.2-0 |
| SearchRouterTask | 3.16.2-0 |

cloud APIs through a POP gatewa

| SearchSubscription | 3.16.2-0 |
|---|---|
| SendMessage | 3.16.2-0 |
| StartCloudRouterTask | 3.16.2-0 |
| StopCloudRouterTask | 3.16.2-0 |
| TraceMessage | 3.16.2-0 |
| UnbindSystemTags | 3.16.2-0 |
| UpdateCloudInfo | 3.16.2-0 |
| UpdateCloudRouterTask | 3.16.2-0 |
| UpdateConsumerReadableByTopicAndGroup | 3.16.2-0 |
| UpdateGroupConsumer | 3.16.2-0 |
| UpdateGroupInfo | 3.16.2-0 |
| UpdateInstance | 3.16.2-0 |
| UpdateMqConnectorDeployment | 3.16.2-0 |
| UpdateTopic | 3.16.2-0 |
| UpdateTopicInfo | 3.16.2-0 |

### 2.2 Preparations

You can use the point of presence (POP) gateway to call API operations in Apsara Stack in the same way that you call them in the Alibaba Cloud public cloud. This topic describes the required preparations.

**Background information**

The POP gateway lets you call API operations in Apsara Stack, which provides a convenient and consistent experience similar to that of the Alibaba Cloud public cloud.

**Obtain service endpoints**

cloud APIs through a POP gatewa

**Obtain an endpoint from the Developer Portal**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Developer Tools** > **API and Tools** >
**Developer Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.
4. In the navigation pane on the left, select the target cloud service.
5. From the **Version** drop-down list, select the target API version.
6. In the API list, you can view all API operations for the current version.
7. Click an API operation. Then, find the POP Endpoint value in the parameter list.

**Obtain an endpoint from Apsara Infrastructure Management**

To call API operations in Apsara Stack using the POP gateway, you must obtain the business domain endpoint for the service. You can obtain the endpoint from an Apsara Stack on-site operations and maintenance (O&M) engineer or obtain it yourself.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform O&M** > **Apsara Infrastructure Management**
> **O&M Tools**.

3. In the navigation pane on the left, choose **O&M Tools** > **Service Registration Variable**
**Dashboard**.
4. On the **Service Registration Variable Dashboard** page, click **Advanced Filter**.
5. In the Service Registration text box, enter `ons_bizapi_endpoint` , and then click **Search**.
cloud APIs through a POP gatewa icon.
6. In the Service Registration column for the `mq-console` service, click the
7. Click the text in the Service Registration column for the `mq-console` service. In the
**Registration Variables** dialog box that appears, find the value of ons_bizapi_endpoint.
This value is the `Endpoint` .

**Obtain common parameters**

Calling API operations using the POP gateway requires common parameters, such as organization ID, resource set ID, Region ID, and instance ID. For more information, see Obtain common header parameters.

### 2.3 SDK for Java

This topic provides examples of how to use the Premium software development kit (SDK) to call APIs over the POP gateway.

**Installation instructions**

**Obtain the SDK package from Developer Portal**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Developer Tools** > **API and Tools** >
**Developer Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **SDK Sample**.
4. Click the
button, choose **Middleware** > **Message Queue (MQ)**, and set **Version** to
**2018-02-05**.
5. From the **SDK Type** drop-down list, select **Premium Edition** and Java.
6. The sample code is displayed. Click **Download Full Project** to obtain the sample project
and the SDK package.

**Import the SDK package**

1. Create a Maven project in one of the following ways.
Method 1: Add a Maven project in IDEA. Method 2: Convert an existing project to a Maven project. i. Right-click the project that you want to convert and select **Add Framework Support...**. ii. Select **Maven** and click **OK**.
2. Create a lib folder in the root directory of the project. Obtain the SDK package from the
Developer Portal and place it in the lib folder, as shown in the following figure.
3. In the pom.xml file of the project, add the Java SDK dependency.
cloud APIs through a POP gatewa

```xml
<dependencies>
    <dependency>
        <groupId>com.aliyun.apsarastack</groupId>
        <artifactId>aliyun-java-sdk-ons</artifactId>
        <version>3.18.3-0</version>
        <scope>system</scope>
        <systemPath>${project.basedir}/lib/aliyun-java-sdk-ons-3.18.3-
0.jar</systemPath>
    </dependency>
</dependencies>
```

4. Check the Maven pane on the right side of IDEA.
If the dependency is displayed as shown in the following figure, the dependency has been imported.

**Code example**

The following example shows how to call the `QueryInstanceList` API to query a list of MQ instances.

```java
import com.aliyun.ons_inner20180205.Client; import com.aliyun.ons_inner20180205.models.QueryInstanceListRequest; import com.aliyun.ons_inner20180205.models.QueryInstanceListResponse; import com.aliyun.tea.TeaException; import com.aliyun.teaopenapi.models.Config; import com.aliyun.teautil.models.ExtendsParameters; import com.aliyun.teautil.models.RuntimeOptions; import java.util.HashMap; import java.util.Map; public class sample {
    public static void main(String[] args) throws Exception {
        // 1. Initialize the com.aliyun.teaopenapi.models.Config object.
        Config config = new Config()
                // The region ID.
                .setRegionId("<your-regionId>")
                // Your AccessKey ID.
                .setAccessKeyId("<AccessKey ID>")
                // Your AccessKey secret.
                .setAccessKeySecret("<AccessKey Secret>")
                // You can set a proxy for requests during client initialization using
Config. Replace the sample value as needed.
                .setHttpProxy("http://127.0.0.1:9898");
        // The domain name to access. You can obtain the Endpoint from the API debuggin
g page in Developer Portal.
        config.endpoint = "<your Endpoint>";
        // 2. Instantiate a client from the com.aliyun.ons_inner20180205.Client class.
Subsequent request and response objects are obtained from com.aliyun.ons_inner20180205.models.
        Client client = new Client(config);
        // 3. Configure runtime parameters.
RuntimeOptionsruntime=newRuntimeOptions();
```

cloud APIs through a POP gatewa

```java
        RuntimeOptions runtime  new RuntimeOptions();
        Map<String, String> headers = new HashMap<>();
        // The organization ID.
        headers.put("x-acs-organizationid", "<your-organizationId>");
        // The resource group ID.
        headers.put("x-acs-resourcegroupid", "<your-resourcegroupId>");
        // The role ID.
        headers.put("x-acs-roleId", "<your-roleId>");
        runtime.setExtendsParameters(new ExtendsParameters().setHeaders(headers));
        // You can configure a proxy for the current request using runtime parameters (
RuntimeOptions). Proxy configurations in RuntimeOptions have a higher priority than tho se in the client. Select a method as needed.
        runtime.setHttpProxy("http://127.0.0.1:9898");
        runtime.ignoreSSL = true;
        runtime.setConnectTimeout(3000);
        runtime.setReadTimeout(30000);
        // 4. Set the parameters for the request object. The properties of the class co
rrespond to the required API parameters. For more information, see the specific API document.
        QueryInstanceListRequest request = new QueryInstanceListRequest();
        // This is a sample value. Specify the parameter as needed.
        request.setNeedResourceInfo(true);
        // This is a sample value. Specify the parameter as needed.
        request.setOnsSessionId("your_value");
        // This is a sample value. Specify the parameter as needed.
        request.setOnsRegionId("your_value");
        // This is a sample value. Specify the parameter as needed.
        request.setPreventCache(System.currentTimeMillis());
        try{
            // 5. Obtain the response that corresponds to the request from the client o
bject.
            QueryInstanceListResponse response =
client.queryInstanceListWithOptions(request, runtime);
            // 6. Call the corresponding properties in the response to obtain the
returned parameter values. For example, to obtain the request ID:
            String requestId = response.body.getRequestId();
            // The printed result is for demonstration purposes only. Replace it as
needed.
            System.out.println(com.aliyun.teautil.Common.toJSONString(response));
        } catch (TeaException error) {
            // Use catch() to handle errors.
            // The error is printed for demonstration purposes only. Handle exceptions
with caution. Do not ignore exceptions in your project.
            System.out.println(error.message);
        } catch (Exception _error) {
            // Use catch() to handle errors.
            TeaException error = new TeaException(_error.getMessage(), _error);
            // The error is printed for demonstration purposes only. Handle exceptions
with caution. Do not ignore exceptions in your project.
            System.out.println(error.getMessage());
```

cloud APIs through a POP gatewa

**Step description**

1. Initialize the com.aliyun.teaopenapi.models.Config object. The Config object stores
configurations such as the AccessKey ID, AccessKey secret, and Endpoint. For more information about how to obtain this information, see Obtain an AccessKey and Obtain API information and the Endpoint.

```
Config config = new Config() // Your AccessKey ID .setAccessKeyId(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")) // Your AccessKey secret .setAccessKeySecret(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")); // The domain name to access config.endpoint = "************";
```

2. Instantiate a client by creating a client object from the
com.aliyun.ons_inner20180205.Client class. Subsequent request and response objects are obtained from the com.aliyun.ons_inner20180205.models package.

```
Client client = new Client(config);
```

3. Create a Request object for the corresponding API. The class uses the API method name +
Request naming convention. Example:

```
QueryInstanceListRequest request = new QueryInstanceListRequest();
```

4. Set the parameters for the request object. The properties of the request class correspond to
the required API parameters.

```
request.SourceRegionId = "your_value"; // This is a sample value. Specify the paramet er as needed. request.RegionId = "your_value"; // This is a sample value. Specify the parameter as needed.
```

5. Obtain the response that corresponds to the request from the client object.

```java
QueryInstanceListResponse response = client.queryInstanceListWithOptions(request, run time); System.out.println(new Gson().toJson(response.Body));
```

6. Call the corresponding properties in the response to retrieve the returned parameter
values. For example, to retrieve the request ID:

```
String requestId = response.Body.requestId;
```

7. Use catch() to handle errors.

```
catch (Exception e) {
    e.printStackTrace();
```

## 3 API reference

### 3.1 RocketMQ_API

#### 3.1.1 Updates

This topic describes the updates of ApsaraMQ for RocketMQ from V3.8.0 to V3.18.3 to help you get started with the updated version.

**Optimization of resource isolation by instance**

ApsaraMQ for RocketMQ provides instances for multi-tenancy isolation. Each user can purchase multiple instances and logically isolate them from each other. To ensure the compatibility with the existing resources of existing users, ApsaraMQ for RocketMQ provides the following types of instances and namespaces: Default instances, which are compatible with the existing resources of existing users This type of instance has no separate namespace. Resource names must be globally unique within and across all instances. By default, an instance without a namespace is automatically generated for the existing resources of each existing user. If no existing resources are available, you can create at most one instance without a namespace. You can configure the endpoint, which can be obtained from the **Instances** page in the ApsaraMQ for RocketMQ console.

```
// Recommended configuration: properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxxx"); // Compatible configuration, which is not recommended. We recommend that you update this configuration to the recommended configuration: properties.put(PropertyKeyConst.ONSAddr, "xxxx");
```

New instances A new instance has a separate namespace. Resource names must be unique within an instance but can be the same across different instances. You can configure the endpoint, which can be obtained from the **Instances** page in the ApsaraMQ for RocketMQ console.

```
// Recommended configuration: properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxx");
```

A RocketMQ client must be updated to the following latest versions for different programming languages: Java: V1.8.7.1.Final C and C++: V2.0.0 .NET: V1.1.3

**Optimization of resource application**

Previously, ApsaraMQ for RocketMQ resources consisted of topics, producer IDs, and consumer IDs. Each two of the resources have a many-to-many relationship, which was difficult to comprehend. Each time you created a topic, you must associate the topic with a producer ID and a consumer ID. This process was too complex for medium- and large-sized enterprise customers. To optimize user experience and help new users get started, the resource application process has been simplified. The resource application process has been optimized in the following aspects: Topic management, which is unchanged You need to apply for a topic. A topic is used to classify messages. It is the primary classifier. You do not need to apply for a producer ID. Producer IDs and consumer IDs are integrated into group IDs. In the ApsaraMQ for RocketMQ console, the Producers module has been removed. The Producers and Consumers modules have been integrated into the Groups module. You do not need to associate a producer ID or consumer ID with a topic. Instead, you need only to apply for a group ID and associate it with a topic in the code. Compatibility: The list of producer IDs is no longer displayed. This does not affect the current services. The consumer IDs that start with CID- or CID_ and that you have applied for can still be used and can be set in the **PropertyKeyConst.ConsumerId** or
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

#### 3.1.2 Overview

##### 3.1.2.1 Intended audience and scenarios

ApsaraMQ for RocketMQ provides you with API operations to help you manage resources. Different from the SDKs for production, API operations are used to manage the resources of ApsaraMQ for RocketMQ, such as topics and group IDs. API operations are intended for those who: Are familiar with the main features of the ApsaraMQ for RocketMQ console. Require a management and control tool similar to the console and have a need for custom management and control features.

##### 3.1.2.2 Scenarios and limits

1. Due to the implementation principles of API operations, the caller must be able to access
the domain name of the ApsaraMQ for RocketMQ console. Otherwise, the call may fail.
2. The underlying layer of API operations is based on HTTP, with average performance and
efficiency. Therefore, API operations are applicable only to management and control scenarios. Do not use them in mass production scenarios with high concurrency.

##### 3.1.2.3 Basic principles

The underlying layer of API operations provides services based on HTTP. Each time you call an API operation, you send an HTTP request from the HTTP client to the backend service of ApsaraMQ for RocketMQ for execution. You can encapsulate parameters in an HTTP request and send the request to call an API operation. The execution results are returned in a response. The request and response are encoded in UTF-8. The service endpoint in the HTTP request is the domain name of the ApsaraMQ for RocketMQ console.

#### 3.1.3 Common parameters

##### 3.1.3.1 Common request parameters

The HTTP client calls ApsaraMQ for RocketMQ API operations based on HTTPS. Common request parameters must be included in all API requests and sent to the backend service of ApsaraMQ for RocketMQ for permission verification. The following table describes common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| accesskey _ | String | Yes | The AccessKey ID of your account. |
| preventCache __ | Long | Yes | The parameter that is used for cross-site request forgery (CSRF) verification. Set this parameter to the current system time. Unit: milliseconds. |
| regionId _ | String | Yes (except for the operation that is used to query region IDs) | The ID of the current region. |
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

##### 3.1.3.2 Common response parameters

The HTTP client sends an HTTP request to the backend service of ApsaraMQ for RocketMQ. The backend service processes the request and then returns results in an HTTP response to the client in the same way. In normal cases, the HTTP status code is 200 in the response. The returned content is contained in the body as a JSON string. The client needs to parse the JSON string to determine whether the call is successful. JSON format:

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

Response parameters: code: the HTTP status code. A value of 200 indicates that the call is successful. Other values indicate that the call fails. currentPage: the page number of the returned page if the request is a paged query. dynamicMessage: the error message. message: the processing result. pageSize: the number of entries returned per page if the request is a paged query. success: indicates whether the call is successful. data: the returned service data. The value is also a JSON string. If the return results of the current request contain service data, you must reverse parse the content in the JSON format. RequestId: the unique ID of the request. The value is a string.

#### 3.1.4 Common terms

##### 3.1.4.1 Account security

###### 3.1.4.1.1 AccessKey

The AccessKey ID of the account that you use to access Alibaba Cloud services. You can obtain your AccessKey ID from the console. When you call an API operation, the AccessKey ID is included in the API request and sent to the backend service of ApsaraMQ for RocketMQ for identity authentication. You can call ApsaraMQ for RocketMQ API operations to manage resources only within your account.

###### 3.1.4.1.2 SecretKey

The AccessKey secret of the account that you use to access Alibaba Cloud services. You can obtain your AccessKey secret from the console. When you call an API operation, the AccessKey secret is included in the API request and used to calculate the signature string of the API request. The backend service of ApsaraMQ for RocketMQ uses the AccessKey secret to verify the signature string of the API request for authentication.

##### 3.1.4.2 Resource management

###### 3.1.4.2.1 Topic

A classifier that is used to classify messages. Messages in ApsaraMQ for RocketMQ are stored by topic. Topics are among the most important resources in ApsaraMQ for RocketMQ. In ApsaraMQ for RocketMQ, topics are globally unique.

###### 3.1.4.2.2 Group ID

The ID of a group. A group consists of producers or consumers that produce or consume messages of the same type and publish or subscribe to messages based on the same logic. If group IDs for consumers or existing consumer IDs are created by a RAM user, both the RAM user and the Apsara Stack tenant account to which the RAM user belongs have permissions on these resources. If group IDs for consumers or existing consumer IDs are created by an Apsara Stack tenant account, only the Apsara Stack tenant account has permissions on these resources. Its RAM users have no permissions on these resources. For more information about the changes in the use of existing producer IDs, existing consumer IDs, and group IDs, see Updates.

#### 3.1.5 Error codes

If a ApsaraMQ for RocketMQ API operation is successfully called, HTTP status code 200 is returned to the client. If the call fails, error codes and descriptions are returned. You can find solutions based on the error codes that are described in the following table.

| Error code | Problem description and cause | Solution |
|---|---|---|
| ONS SYSTEM ERROR _ _ | An error has occurred at the backend of ApsaraMQ for RocketMQ. | Submit a ticket to contact the technical support staff of ApsaraMQ for RocketMQ. |
| ONS SERVICE UNSUPPORTED _ _ | The API operation is not supported in the specified region. | Contact the technical support staff of ApsaraMQ for RocketMQ to confirm whether the operation is supported. |
| ONS INVOKE ERROR _ _ | The API operation failed to be called. | Contact the technical support staff of ApsaraMQ for RocketMQ. |
| BIZ FIELD CHECK INVALID _ _ _ | Parameters failed the verification. | Check whether the specified request parameters are valid based on the API reference. |
| BIZ TOPIC NOT FOUND _ _ _ | The topic does not exist. | Check whether the specified topic is valid or whether the topic is created. |
| BIZ SUBSCRIPTION NOT FOUND _ _ _ | The group ID of the subscription does not exist. | Check whether the group ID is created or whether the query conditions are valid. |
| BIZ PUBLISHER EXISTED _ _ | The specified group ID already exists. | Use a new group ID and try again. |
| BIZ SUBSCRIPTION EXISTED _ _ | The specified group ID already exists. | Use a new group ID and try again. |

| BIZ CONSUMER NOT ONLINE _ _ _ | The consumer that is identified by the specified group ID is offline. | Ensure that the consumer is online and try again. |
|---|---|---|
| BIZ NO MESSAGE _ _ | No messages match the query conditions. | Check the query conditions and check whether messages are sent based on the query conditions. |
| BIZ REGION NOT FOUND _ _ _ | The requested region does not exist. | Check whether the specified region ID is valid. |
| BIZ TOPIC EXISTED _ _ | The specified topic already exists. | Use a new topic name and try again. |
| BIZ PRODUCER ID BELONG TO OTHER US _ _ _ _ _ _ ER | The specified group ID is occupied by another user. | Use a new group ID and try again. |
| BIZ CONSUMER ID BELONG TO OTHER US _ _ _ _ _ _ ER | The specified group ID is occupied by another user. | Use a new group ID and try again. |
| BIZ PUBLISH INFO NOT FOUND _ _ _ _ | The requested group ID does not exist. | Check whether the group ID exists or whether the query conditions are valid. |
| EMPOWER EXIST ERROR _ _ | The specified authorization already exists. | Check the request parameters and try again or query the authorization first. |
| EMPOWER OWNER CHECK ERROR _ _ _ | The current user is not the owner of the authorized topic. | Check the ownership of the resource. |

#### 3.1.6 API reference

##### 3.1.6.1 Instance management

###### 3.1.6.1.1 QueryCommonGenRedirectUrl

Generates a generic redirection URL for ApsaraMQ for RocketMQ operations.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The region identifier of the Ons service, which is used to specify the region node of the message service. |
| PreventCa che | Long | Quer y | Yes | 324234234 | Prevents the browser from caching page content. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| Key | Strin g | Quer y | Yes | TestKey | The tag key. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID that identifies a client session when you use Alibaba Cloud Open Notification Service (ONS). This parameter ensures context consistency for message communication. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The interface status or POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryCommonGenRedirectUrl &OnsRegionId=REGION_001 &PreventCache=324234234 &Key=TestKey &Common request parameters
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.1.2 QueryTrendFlowLimit

Queries trend data for traffic throttling in ApsaraMQ for RocketMQ.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information about common request headers, see Common request parameters.

| > Document V | ersion: 2 | 026010 | 8 |   | 4 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The region identifier of the Ons service, which is used to specify the geographic region of the message service. |
| PreventCa che | Long | Quer y | Yes | 234234234 | Prevents the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| Type | Integ er | Quer y | No | 1 | The type. |
| MessageTy pe | Strin g | Quer y | Yes | RAW | The message type. |
| Period | Integ er | Quer y | No | 1 | The epoch. |
| BeginTime | Long | Quer y | No | 2022 | The start time. |
| EndTime | Long | Quer y | No | 1706668721 | The end time. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID for a session between a client and the server in Alibaba Cloud Open Notification Service (ONS). The client generates this ID to track and manage the sending and receiving of messages. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The interface status or POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryTrendFlowLimit &InstanceId=bastionhost-12****** &OnsRegionId=Region001 &PreventCache=234234234 &MessageType=RAW
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.1.3 UnbindSystemTags

Detaches system tags from a specified instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION001 | The region ID of the Ons service, which specifies the geographic region where the message service is located. |
| PreventCa che | Long | Quer y | Yes | 32424234234 | Prevents the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| TagOwner Uid | Long | Quer y | Yes | 123xxxx | The Alibaba Cloud account ID of the tag owner. |
| TagKeys | Strin g | Quer y | No | ["k1","k2"] | The tag keys. |
| Scope | Strin g | Quer y | No | 11 | The scope of the organization. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=UnbindSystemTags &OnsRegionId=REGION001 &PreventCache=32424234234 &InstanceId=bastionhost-12****** &TagOwnerUid=123xxxx
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.1.4 CreateInstance

Creates an instance.

**Request headers**

This operation uses common request headers. Special request headers are not required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The region identifier of the Ons service, which specifies the geographic region where the message service is located. |
| PreventCa che | Long | Quer y | No | 23232323 | Prevents browsers and servers from caching data to ensure that each request retrieves the latest content. |
| InstanceN ame | Strin g | Quer y | Yes | myinstance | The name of the instance. |
| Remark | Strin g | Quer y | No | remark | The remarks about the instance. |

| TopicCapa city | Integ er | Quer y | No | 50 | The maximum number of topics that can be created in the instance. Valid values: 25, 50, 100, 300, and 500. This parameter applies only to ApsaraMQ for RocketMQ Platinum Edition instances. |
|---|---|---|---|---|---|
| MaxSendT ps | Long | Quer y | No | 1000 | The maximum number of messages that can be sent per second. |
| MaxReceiv eTps | Long | Quer y | No | 1000 | The maximum number of messages that can be received per second. |
| Cluster | Strin g | Quer y | No | tianji-A-006b | The name of the cluster. |
| Independe ntNaming | Bool ean | Quer y | No | true | Specifies whether the instance has a namespace. Valid values: true: The instance has an independent namespace. Resource names must be unique within the instance but can be duplicated across different instances. false: The instance does not have an independent namespace. Resource names must be globally unique within or across instances. |
| Tags | Strin g | Quer y | No | tag1 | The tags. |
| Scope | Strin g | Quer y | No | 11 | The scope of the organization. |
| TagOwner Uid | Long | Quer y | No | 123xxxx | The ID of the Alibaba Cloud account to which the tag belongs. |

| CpuArch | Strin g | Quer y | No | x86 64 _ | The CPU architecture supported by the driver. Valid values: armv7 armv7-hf aarch64 x86-64 x86 |
|---|---|---|---|---|---|
| CpuId | Strin g | Quer y | No | cpu1 | The chip ID. |
| CpuBrand | Strin g | Quer y | No | Apple M1 | The CPU brand. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The call was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the request. This can be an API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |

Request example

```
http(s)://[Endpoint]/?Action=CreateInstance &OnsRegionId=Region001 &InstanceName=myinstance
```

Sample successful response

```json
 "Data":{},
```

###### 3.1.6.1.5 BindSystemTags

Attaches system tags to a message queue instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The identifier of a specific geographic or logical region. |
| PreventCa che | Long | Quer y | Yes | 34234242 | Prevents the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| Tags | Strin g | Quer y | Yes | tag1,tag2 | The tags. |
| Scope | Strin g | Quer y | No | 11 | The scope of the organization. |
| TagOwner Uid | Long | Quer y | Yes | 123xxxx | The Alibaba Cloud account ID of the tag owner. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API operation or a POP error code. |
| Message | String | success | Additional information |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=BindSystemTags &OnsRegionId=Region001 &PreventCache=34234242 &InstanceId=bastionhost-12****** &Tags=tag1,tag2 &TagOwnerUid=123xxxx
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.1.6 QuerySystemTagList

Queries a list of system tags.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The region identifier of the Ons service, which specifies the geographic region where the message service is located. |
| PreventCa che | Long | Quer y | Yes | 3424234 | Prevents the browser or system from caching data to ensure that the latest content is retrieved for each request. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| Scope | Strin g | Quer y | No | 11 | The scope of the organization. |
| TagOwner Uid | Long | Quer y | Yes | 123xxxx | The Alibaba Cloud account ID to which the tag belongs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The interface status or POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QuerySystemTagList &OnsRegionId=Region001 &PreventCache=3424234 &InstanceId=bastionhost-12****** &TagOwnerUid=123xxxx &Common request parameters
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.1.7 DeleteInstance

Deletes the specified message queue instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region01 | An identifier for a specific geographic or logical area that differentiates between service areas or data centers. |
| PreventCa che | Long | Quer y | Yes | 2321423 | A parameter used to prevent the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | INTEGER | 200 | The interface status or POP error code. |
| Message | String | success | Additional information. |

Sample request

```
http(s)://[Endpoint]/?Action=DeleteInstance &OnsRegionId=Region01 &PreventCache=2321423 &InstanceId=bastionhost-12****** <Common request parameters>
```

Sample response

###### 3.1.6.1.8 QueryInstanceBaseInfo

Queries the basic information about a specified Message Service instance, including the instance ID, name, status, and specifications.

**Request headers**

This operation does not have special request headers. For more information about common request headers, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The ID of the region where Message Service is deployed. |
| PreventCa che | Long | Quer y | Yes | 65443334456 | Prevents the use of cached data. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |

| OnsSessio nId | Strin g | Quer y | No | abc123xyz | A unique ID that identifies a client session in Open Notification Service (ONS). It is used to track and manage the message sending and receiving procedure. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The interface status or POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryInstanceBaseInfo &OnsRegionId=REGION_001 &PreventCache=65443334456 &InstanceId=bastionhost-12******
```

Sample success response

###### 3.1.6.1.9 QueryInstanceStatistics

Queries the runtime statistics for a specified message instance. The statistics include the number of messages, topics, and consumer groups.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region identifier of the Ons service, which specifies the geographic region where the message service is located. |
| PreventCa che | Long | Quer y | Yes | 6553356777 | You can enable the cache prevention feature to ensure that each request bypasses the local cache and retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| EndTime | Long | Quer y | No | 1706668721 | The end time. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID of a client session in Alibaba Cloud Open Notification Service (ONS). This ID ensures message ordering and idempotent. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |

| Code | Integer | 200 | The interface status or POP error code. |
|---|---|---|---|
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |

Example request

```
http(s)://[Endpoint]/?Action=QueryInstanceStatistics &OnsRegionId=region123 &PreventCache=6553356777 &InstanceId=bastionhost-12******
```

Example response

```json
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.1.10 QueryInstanceList

Queries the list of ApsaraMQ for RocketMQ instances.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| RegionId | Strin g | Host | No | cn-hangzhou | The ID of the region. |
|---|---|---|---|---|---|
| OnsRegion Id | Strin g | Quer y | Yes | REGION12345 | The region identifier of the Ons service, which specifies the geographic region where the message service is located. |
| PreventCa che | Long | Quer y | Yes | 4534534534 | Prevents the browser from caching the response. This ensures that each request retrieves the latest data from the server. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID of an ONS session. This ID is used to track and manage message sending and receiving. |
| NeedReso urceInfo | Bool ean | Quer y | No | true | Specifies whether to return resource statistics, such as the number of topics and groups in the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was succeeful. false: The request failed. |
| Code | Integer | 200 | The interface status or POP error code. |

| Message | String | success | Additional information. |
|---|---|---|---|

Sample request

```
http(s)://[Endpoint]/?Action=QueryInstanceList &OnsRegionId=REGION12345 &PreventCache=4534534534
```

Sample responses

```json
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.1.11 QueryRouterInstanceList

Queries a list of routing instances for ApsaraMQ for RocketMQ.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | region1 | The ID of the region in Message Service. This ID distinguishes different service deployment areas. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 8767767755 | A timestamp used to prevent the browser from returning cached data. This ensures that each request retrieves the latest content. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID of a client session in the Message Queue service. This ID is used to track and manage message consumption or production sessions. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The interface status or POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryRouterInstanceList &OnsRegionId=region1 &PreventCache=8767767755
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.1.12 UpdateInstance

Updates the configuration of an ApsaraMQ for RocketMQ instance.

**Request headers**

No special request headers are required for this operation. For more information about common request headers, see Common parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | hangzhou | The unique identifier for a specific region. It is used to distinguish between different geographical regions in Message Service and other cloud services. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 24234234 | A timestamp used to prevent browser caching. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| InstanceN ame | Strin g | Quer y | No | myinstance | The name of the instance. |
| Remark | Strin g | Quer y | No | remark | The remarks for the instance. |
| TopicCapa city | Integ er | Quer y | No | 50 | The maximum number of topics that can be created in the instance. Valid values: 25, 50, 100, 300, and 500. This parameter applies only to ApsaraMQ for RocketMQ Platinum Edition instances. |
| MaxSendT ps | Long | Quer y | No | 1000 | The maximum number of send requests per second. |
| MaxReceiv eTps | Long | Quer y | No | 1000 | The maximum number of transaction requests that the system can receive per second. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
|---|---|---|---|
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |

Sample request

```
http(s)://[Endpoint]/?Action=UpdateInstance &OnsRegionId=hangzhou &PreventCache=24234234 &InstanceId=bastionhost-12****** &Common request parameters
```

Sample responses

```json
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.1.13 CheckFortestInstance

Checks the status of and permissions on a test instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information about common request headers, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region identifier of the Ons service, which specifies the geographic region where the message service is located. |
| PreventCa che | Long | Quer y | Yes | 23423424 | Prevents the browser from caching page content. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| AuthAction Name | Strin g | Quer y | Yes | SessionRefresh | Verify whether the user has the RAM permission action name for the specified operation permission on the instance resource. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The status of the API call or the POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=CheckForTestInstance &OnsRegionId=region123 &PreventCache= &InstanceId=bastionhost-12****** &AuthActionName=SessionRefresh &CommonRequestParameters
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

##### 3.1.6.2 Topic management

###### 3.1.6.2.1 CheckFortestTopic

Used to verify that the Topic was created and that the current user has the specified publish/subscribe permissions in the Test environment.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | The region identifier of the Ons service, which specifies the geographic region where the message service is located. |
| PreventCa che | Long | Quer y | Yes | 234234234 | Prevents the browser from caching page content to ensure that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | Yes | test | The topic name. |
| Relation | Integ er | Quer y | Yes | 6 | Specify the type of Topic permission relationship to be verified, including OWNER (OWNER = 1), publish permission (PUB = 2), subscribe permission (SUB = 4), and publish and subscribe permission (PUB SUB = 6). _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=CheckFortestTopic &OnsRegionId=REGION01 &PreventCache= &Topic=test &Relation=6
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.2.2 PageQueryTopicList

Queries a paginated list of topics in ApsaraMQ for RocketMQ.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The region identifier of the Ons service, which specifies the geographic region where the message service is located. |
| PreventCa che | Long | Quer y | Yes | 32423424 | A timestamp used to prevent browser caching. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| CurrentPa ge | Integ er | Quer y | No | 1 | The page number of the current page during paging query. |
| PageSize | Integ er | Quer y | No | 10 | The number of rows per page that are set for paging queries. Default value: 10. |
| Search | Strin g | Quer y | No | 1 1 1 1 1 _ _ _ _ | Search. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID of a client session in ONS. This ID is used to track and manage message consumption or production sessions. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The interface status or POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=PageQueryTopicList &OnsRegionId=Region001 &PreventCache=32423424
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.2.3 CreateSubscription

API for creating subscription relationships.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region1 | The ID of the region. It distinguishes different service areas or data centers. |
| PreventCa che | Long | Quer y | Yes | 2332424232 | Prevents browsers or servers from caching data. This ensures that each request retrieves the latest content. |
| ConsumerI d | Strin g | Quer y | Yes | kafka-test | The name of the group. The name must meet the following requirements: It can contain only letters, digits, hyphens (-), and underscores ( ). It must contain at _ least one letter or digit. The length must be 3 to 128 characters. If the name exceeds 128 characters, it is automatically truncated. The group name cannot be modified after it is created. |
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
|---|---|---|---|
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The interface status or POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=CreateSubscription &OnsRegionId=region1 &PreventCache=2332424232 &ConsumerId=kafka-test &Topic=test
```

Successful response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.2.4 CreateTopic

Creates a new message topic.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The region ID of the ONS service. This specifies the geographical region where the service is located. |
| PreventCa che | Long | Quer y | Yes | 32342342 | Prevents the browser or system from caching data. This ensures that each request retrieves the latest content. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
| OrderType | Integ er | Quer y | No | 1 | The order type. |
| Remark | Strin g | Quer y | No | remark | The remark. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |

| Message | String | success | Additional information. |
|---|---|---|---|
| Data | String | [{}] | The returned data. |

Request example

```
http(s)://[Endpoint]/?Action=CreateTopic &OnsRegionId=Region001 &PreventCache=32342342 &Topic=test
```

Successful response example

```json
 "Data":"[{}]",
```

###### 3.1.6.2.5 DeleteTopic

Deletes a specified message topic.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region identifier of the Ons service, which specifies the geographic region where the message service is located. |

| PreventCa che | Long | Quer y | Yes | 223432442 | Prevents the browser or system from caching data. This ensures that each request retrieves the latest content. |
|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |

Request example

```
http(s)://[Endpoint]/?Action=DeleteTopic &OnsRegionId=region123 &PreventCache=223432442 &Topic=test
```

Successful response example

```json
 "Data":"[{}]",
```

###### 3.1.6.2.6 DeleteSubscription

Deletes a subscription relationship in ApsaraMQ for RocketMQ.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | qingdao | The description. |
| PreventCa che | Long | Quer y | Yes | 2333333 | Prevents the client or server from caching the response. This ensures that each request retrieves the latest data. |
| ConsumerI d | Strin g | Quer y | Yes | kafka-test | The name of the group. The value must meet the following requirements: It can contain only letters, digits, hyphens (-), and underscores ( ). It must contain at _ least one letter or digit. The length must be between 3 and 128 characters. If the length exceeds 128 characters, the name is automatically truncated. The group name cannot be modified after it is created. |

| Topic | Strin g | Quer y | No | test | The name of the topic. |
|---|---|---|---|---|---|

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries returned. |

Request example

```
http(s)://[Endpoint]/?Action=DeleteSubscription &OnsRegionId=qingdao &PreventCache=2333333 &ConsumerId=kafka-test &Common request parameters
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.2.7 QueryTrendTopicInputTps

Queries the trend of Transactions Per Second (TPS) for messages sent to a topic, which indicates the trend in message production volume.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | ExampleRegion01 | Identifies the region id. |
| PreventCa che | Long | Quer y | Yes | 6454433343 | Prevents the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
| Type | Integ er | Quer y | No | 1 | The type. |
| Period | Integ er | Quer y | No | 1 | Epoch. |
| BeginTime | Long | Quer y | No | 2022 | The start time. |
| EndTime | Long | Quer y | No | 1706668721 | The end time. |

| OnsSessio nId | Strin g | Quer y | No | ABC123XYZ789 | The unique ID of a client session in Open Notification Service (ONS). This ID is used to track and manage message push sessions. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryTrendTopicInputTps &OnsRegionId=ExampleRegion01 &PreventCache=6454433343 &InstanceId=bastionhost-12****** &Topic=test
```

Response example

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.2.8 QueryTopicSubDetail

Queries the subscription relationship details for a specified topic, including information about all consumer groups that subscribe to the topic.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The ID of the sample region to identify a specific message service area. |
| PreventCa che | Long | Quer y | Yes | 23432423 | Prevents the client or server from caching the response. This ensures that each request retrieves the latest content. |

| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
|---|---|---|---|---|---|
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | Identifies the session between the client and the server to ensure context consistency during message transmission. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryTopicSubDetail &OnsRegionId=Region001 &PreventCache=23432423 &InstanceId=bastionhost-12****** &Topic=test &Common request parameters
```

Sample response

```json
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.2.9 QueryTopicStatus

Queries the message status of a specified topic. The status includes statistics information, such as the total number of messages and the last send time.

**Request header**

This operation uses common request headers and does not require special request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region1 | Indicates the identifier of a specific region, which is used to distinguish different service areas or geographical locations. |
| PreventCa che | Long | Quer y | Yes | 1231231231 | A timestamp used to prevent browser caching. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |

| Developer Gui | de·API re | ference |   | Al | ibaba Cloud Message Queu |
|---|---|---|---|---|---|

| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryTopicStatus &OnsRegionId=region1 &PreventCache=1231231231 &Topic=test
```

Sample responses

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.2.10 QueryTopicNameList

Queries a list of topic names in ApsaraMQ for RocketMQ.

**Request header**

This operation has no special request headers. For more information about common request headers, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The unique ID of the region. This ID distinguishes different service or data regions. |
| PreventCa che | Long | Quer y | Yes | 23132132 | Used to prevent the browser from caching page content. This parameter forces the browser to fetch the latest data from the server for each request. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |

| Developer Gui | de·API re | ference |   | Al | ibaba Cloud Message Queue |
|---|---|---|---|---|---|

| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID of a client session in the Message Queue service. This ID maintains the connection state between the client and the server. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryTopicNameList &OnsRegionId=region123 &PreventCache=23132132
```

Sample response

```json
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.2.11 QueryTopicListByGroupId

Queries a list of topics by consumer group ID.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | ons1234567890 | The unique identifier of a region. This ID is used to distinguish between different service areas or data centers. |
| PreventCa che | Long | Quer y | Yes | 2312313 | Prevents the browser or system from using cached data. This ensures that each request retrieves the latest content. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | 1 | The consumer group ID. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID of a client session in ApsaraMQ for RocketMQ. This ID is used to maintain the connection status of a producer or consumer. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryTopicListByGroupId &OnsRegionId=ons1234567890 &PreventCache=2312313 &InstanceId=bastionhost-12****** &GroupId=1
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.2.12 QueryTopicList

Queries the list of topics in ApsaraMQ for RocketMQ.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | RegionUS | The region identifier of the Ons service, which specifies the geographic region or logical partition of the message service. |
| PreventCa che | Long | Quer y | Yes | 23123131 | Prevents the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | No | test | The topic name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |

| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
|---|---|---|---|
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryTopicList &OnsRegionId=RegionUS &PreventCache=23123131
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.2.13 QueryTopic

Queries information about topics.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | hangzhou | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
| PreventCa che | Long | Quer y | Yes | 23134124 | Prevents the client or server from caching the response. This ensures that each request returns the most up-to-date data. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | No | test | The topic name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |

| Code | Integer | 200 | The status code of the API operation or a POP error code. |
|---|---|---|---|
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryTopic &OnsRegionId=hangzhou &PreventCache=23134124
```

Response examples

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.2.14 QuerySubscriptionList

Queries the list of subscriptions for ApsaraMQ for RocketMQ.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| 3 |   |   |   | > D | ocument Version: 2026010 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | Represents a specific geographic region or logical region identifier, which is used to distinguish different service regions or data center locations. |
| PreventCa che | Long | Quer y | Yes | 23324124 | A parameter used to prevent the browser from caching content. This ensures that each request retrieves the latest data from the server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QuerySubscriptionList &OnsRegionId=REGION_001 &PreventCache=23324124
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.2.15 QuerySubscription

Queries the details of a subscription in ApsaraMQ for RocketMQ.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | This is used to distinguish between geographical or logical areas. |

| PreventCa che | Long | Quer y | Yes | 23423424242 | Prevents the browser from caching content. This ensures that each request retrieves the latest data from the server. |
|---|---|---|---|---|---|
| ConsumerI d | Strin g | Quer y | Yes | kafka-test | The consumer ID. |
| Topic | Strin g | Quer y | Yes | test | The topic name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QuerySubscription &OnsRegionId=Region001 &PreventCache=23423424242 &ConsumerId=kafka-test &Topic=test
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.2.16 QueryRouterTopicList

Queries a list of routing topics in ApsaraMQ for RocketMQ.

**Request headers**

This operation uses only common request headers. For more information, see the common request parameters document.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | shenzhen | The identifier for a specific geographic or logical region. |
| PreventCa che | Long | Quer y | Yes | 34234234234 | Prevents the client or server from caching the response. This ensures that each request fetches the latest data directly from the server. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |

| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID that identifies a client session in Alibaba Cloud Message Service (ONS). |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The data returned. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request is successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryRouterTopicList &OnsRegionId=shenzhen &PreventCache=34234234234 &Common request parameters
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.2.17 UpdateTopicInfo

Updates the information about a specified topic in ApsaraMQ for RocketMQ.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The identifier of a specific geographic or logical region. This is used to distinguish different service areas or data centers. |
| PreventCa che | Long | Quer y | Yes | 4353453 | A timestamp used to prevent the client or server from caching the response. This ensures that the latest data is retrieved for each request. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | Yes | test | The topic name. |
| Remark | Strin g | Quer y | Yes | remark | The remarks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=UpdateTopicInfo &OnsRegionId=region123 &PreventCache=4353453 &InstanceId=bastionhost-12****** &Topic=test &Remark=remark
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.2.18 UpdateTopic

Updates the configuration of a topic in ApsaraMQ for RocketMQ.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The ID of a geographic or logical region. It distinguishes different service areas or data centers. |
| PreventCa che | Long | Quer y | Yes | 2343243234 | Prevents the browser or system from caching data. This ensures that each request retrieves the latest content. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
| Perm | Integ er | Quer y | No | 6 | Sets the read/write permissions for the topic. Valid values: 6: read and write. 4: write forbidden. 2: read forbidden. |
| UnitFlag | Bool ean | Quer y | No | 0x80 | Indicates that the unit is invalid. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or the POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The data returned. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=UpdateTopic &OnsRegionId=Region001 &PreventCache=2343243234 &Topic=test
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.2.19 UpdateSubscription

The API interface that updates the subscription relationship.

**Request header**

This operation uses common request headers. No special request headers are used. For more information, see Common request parameters.

| Parameter name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The identifier for the region. |
| PreventCa che | Long | Quer y | Yes | 23423423423 | Prevents the browser or system from using cached data. This ensures that the latest content is retrieved with each request. |
| ConsumerI d | Strin g | Quer y | Yes | kafka-test | The ID of the consumer. |
| ReadEnabl e | Bool ean | Quer y | Yes | true | Specifies whether to enable message reading. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

| Success | Boolean | true | The status of the response. true: The request is successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The status of the API operation or a POP error code. |
| Message | String | success | The content of the message. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number. |

Sample request

```
http(s)://[Endpoint]/?Action=UpdateSubscription &OnsRegionId=REGION_001 &PreventCache=23423423423 &ConsumerId=kafka-test &ReadEnable=true
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.2.20 SearchSubscription

Queries subscription relationships in ApsaraMQ for RocketMQ.

**Request headers**

This operation has no special request headers. For more information about common request headers, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The ID of the region. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | Identifies the region id. |
| PreventCa che | Long | Quer y | Yes | 324234243 | A timestamp used to prevent the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| Search | Strin g | Quer y | Yes | 1 1 1 1 1 _ _ _ _ | Search box. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API operation or a POP error code. |
| Message | String | success | Additional information |

| Total | Long | 1 | The total number of entries. |
|---|---|---|---|

Sample request

```
http(s)://[Endpoint]/?Action=SearchSubscription &OnsRegionId=Region001 &PreventCache=324234243 &Search=1_1_1_1_1
```

Sample successful response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

##### 3.1.6.3 Cluster management

###### 3.1.6.3.1 QueryClusterList

Retrieves a list of clusters for ApsaraMQ for RocketMQ

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
|---|---|---|---|---|---|
| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | The unique identifier for a specific region. This parameter distinguishes different service areas or data centers. |
| PreventCa che | Long | Quer y | No | 3224234 | Prevents the browser or system from caching data. This ensures that each request retrieves the latest content. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryClusterList &OnsRegionId=REGION01 &Common request parameters
```

Sample successful response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.3.2 QueryClusterCapacity

Queries the capacity information of a specified cluster. This information includes capacity limits, such as the maximum number of subjects, maximum sending transactions per second (TPS), and maximum receiving TPS.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see the Common Request Parameters document.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region identifier of the Ons service, which specifies the geographic region where the service is located. |
| PreventCa che | Long | Quer y | No | 334545775433 | Prevents the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| Cluster | Strin g | Quer y | Yes | tianji-A-006b | The cluster name. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
|---|---|---|---|
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryClusterCapacity &OnsRegionId=region123 &Cluster=tianji-A-006b
```

Successful response example

```json
 "Total":1,
 "Data":{},
```

##### 3.1.6.4 Group management

###### 3.1.6.4.1 CreateGroup

Creates a new consumer group.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | hangzhou | The ID of the region for the ONS service. This parameter specifies the geographical location of the resource. |
| PreventCa che | Long | Quer y | Yes | 32342342 | Prevents the browser or server from caching data. This ensures that each request retrieves the latest content. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | 1 | The ID of the application group. |
| GroupType | Strin g | Quer y | No | ip | The type of the security group. Valid values: normal: a basic security group. enterprise: an advanced security group. |
| Remark | Strin g | Quer y | No | remark | The remarks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The status code of the API call or a POP error code. |
| Message | String | success | Additional information about the response. |
| Data | String | [{}] | The data returned in the response. |
| Total | Long | 1 | The total number of entries returned. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateGroup &OnsRegionId=hangzhou &PreventCache=32342342 &GroupId=1
```

Sample successful response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.4.2 PageQueryGroupList

Queries a paginated list of groups in ApsaraMQ for RocketMQ.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| 11 |   |   |   | > D | ocument Version: 2026010 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | Represents a specific region identifier, which is used to distinguish different regions or data centers. |
| PreventCa che | Long | Quer y | Yes | 234234234 | A parameter that prevents the browser or system from caching data. This ensures that each request retrieves the latest content. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| CurrentPa ge | Integ er | Quer y | No | 1 | The page number of the current page during paging query. |
| PageSize | Integ er | Quer y | No | 10 | The number of rows per page that are set for paging queries. |
| GroupType | Strin g | Quer y | No | type | The group type. |
| Search | Strin g | Quer y | No | 1 1 1 1 1 _ _ _ _ | Search box |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | A unique ID that identifies a session between the client and the server. It is used to maintain message order and session state. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| Data | String | [{}] | The returned data. |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=PageQueryGroupList &OnsRegionId=region123 &PreventCache=234234234 &InstanceId=bastionhost-12******
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.4.3 DeleteGroup

Delete a message queue consumption group.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region ID of the ONS service. This parameter specifies the geographic region of the service. |
| PreventCa che | Long | Quer y | Yes | 324242344 | A timestamp used to prevent the client or server from caching the response. This ensures that each request retrieves the latest data. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | 1 | The application group ID. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |

| Total | Long | 1 | The total number of entries. |
|---|---|---|---|

Request example

```
http(s)://[Endpoint]/?Action=DeleteGroup &OnsRegionId=region123 &PreventCache=324242344 &InstanceId=bastionhost-12****** &GroupId=1
```

Successful response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.4.4 QueryGroupIdList

Queries a list of all group IDs for a specified instance.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The unique identifier for a specific region in Message Service. |

| PreventCa che | Long | Quer y | Yes | 3445345345 | A parameter used to prevent the browser from caching content. This ensures that each request retrieves the latest data from the server. |
|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique session identifier for communication between the client and the server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or the POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryGroupIdList &OnsRegionId=region123 &PreventCache=3445345345 &InstanceId=bastionhost-12******
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.4.5 QueryGroupSubDetail

Queries the complete subscription details for a consumer group.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region identifier for Message Service (ONS). This parameter specifies the geographic region or logical partition of the service. |

| PreventCa che | Long | Quer y | Yes | 1232131231 | Prevents the browser or system from using cached data. This ensures that each request retrieves the latest content. |
|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | GID-1 | The group ID. |
| OnsSessio nId | Strin g | Quer y | No | 1234567890 | Identifies a session connection between the client and the server. This ensures contextual consistency for message communication. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryGroupSubDetail &OnsRegionId=region123 &PreventCache=1232131231 &InstanceId=bastionhost-12****** &GroupId=GID-1
```

Response example

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.4.6 QueryGroupList

Queries a list of consumer groups in ApsaraMQ for RocketMQ.

**Request header**

No special request headers are required for this operation. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | CN01 | The region identifier of the Ons service, which specifies the geographic region or logical partition of the message service. |

| PreventCa che | Long | Quer y | Yes | 3242431 | Prevents the browser or server from caching data. This ensures that you retrieve the latest content with each request. |
|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | No | 1 | The ID of the application group. |
| GroupType | Strin g | Quer y | No | ip | The group type. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryGroupList &OnsRegionId=CN01 &PreventCache=3242431
```

Response examples

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.4.7 QueryTrendGroupOutputTps

Queries the trend data of message consumption, measured in Transactions Per Second (TPS), for a consumer group. This data shows changes in consumption capacity.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | An identifier for a specific geographic or logical region. It is used to distinguish between different service areas or data centers. |
| PreventCa che | Long | Quer y | Yes | 342342342 | A parameter used to prevent the client from using a cached response. This ensures that you retrieve the latest data from the server. |

| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
|---|---|---|---|---|---|
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
| GroupId | Strin g | Quer y | Yes | 1 | The ID of the group. |
| Type | Integ er | Quer y | No | 1 | The type. |
| Period | Integ er | Quer y | No | 1 | The period. |
| BeginTime | Long | Quer y | No | 2022 | The start time. |
| EndTime | Long | Quer y | No | 1706668721 | The end time. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | Identifies a session connection between the client and the server. It is used for sequential message processing and state maintenance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API or a POP error code. |
| Message | String | success | Additional information. |

| Data | Map | {} | The data returned. |
|---|---|---|---|
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryTrendGroupOutputTps &OnsRegionId=Region001 &PreventCache=342342342 &InstanceId=bastionhost-12****** &Topic=test &GroupId=1
```

Sample responses

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.4.8 UpdateGroupInfo

Updates information about a group in ApsaraMQ for RocketMQ.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| 23 |   |   |   | > D | ocument Version: 2026010 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The identifier for a specific region. This parameter distinguishes different service areas or data centers. |
| PreventCa che | Long | Quer y | Yes | 423423423 | Instructs the system or browser not to cache the current request or resource. This ensures that each request retrieves the latest data directly from the server. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | 1 | The consumer group ID. |
| Remark | Strin g | Quer y | Yes | remark | The remarks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |

| Data | String | [{}] | The returned data. |
|---|---|---|---|
| Total | Long | 1 | The total number. |

Sample request

```
http(s)://[Endpoint]/?Action=UpdateGroupInfo &OnsRegionId=region123 &PreventCache=423423423 &GroupId=1 &Remark=remark
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.4.9 UpdateGroupConsumer

Updates the configuration of a specified consumer group in ApsaraMQ for RocketMQ.

**Request headers**

This operation does not have special request headers. For more information about common request headers, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
|---|---|---|---|---|---|
| OnsRegion Id | Strin g | Quer y | Yes | region1 | The id used to distinguish deployment environments in different regions. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | 1 | The ID of the consumer group. |
| ReadEnabl e | Bool ean | Quer y | No | true | Specifies whether to enable message reading. |
| UnitFlag | Bool ean | Quer y | No | 0x80 | The UnitFlag. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number. |

Sample request

```
http(s)://[Endpoint]/?Action=UpdateGroupConsumer &OnsRegionId=region1 &GroupId=1 &Common request parameters
```

Sample responses

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

##### 3.1.6.5 CloudInfo management

###### 3.1.6.5.1 QueryCloudInfoNoPage

Query cloud information (no paging) API.

**Request headers**

This operation uses common request headers and does not require special request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | region123 | The ID of a geographic or logical region. This ID distinguishes different service areas or data centers. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 342432324 | Prevents the browser or system from caching data to ensure that each request retrieves the latest content. |
| CloudInfoK ey | Strin g | Quer y | No | anotherExample | An identifier for the related data. |
| OnsSessio nId | Strin g | Quer y | No | 1234567890 | The unique ID of a client session in the ApsaraMQ for RocketMQ (ONS) service. It maintains the connection state between a producer or consumer and the server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryCloudInfoNoPage &OnsRegionId=region123 &PreventCache=342432324
```

Successful response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.5.2 UpdateCloudInfo

Updates the information about a specified cloud instance.

**Request headers**

This operation uses only common request headers. For more information, see Common parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The ID of a geographic or logical region. This ID distinguishes different service areas or data centers. |
| PreventCa che | Long | Quer y | Yes | 234234234 | Prevents the browser or system from using cached data. This ensures that each request retrieves the latest content. |

| CloudNam e | Strin g | Quer y | No | 212e | The name of the cloud instance. |
|---|---|---|---|---|---|
| AddRegion Id | Strin g | Quer y | No | 1001 | The ID of the new region. It uniquely identifies a new geographic or logical region within the system. |
| CloudId | Strin g | Quer y | Yes | ffe1********6d6d | The ID of the cloud instance. |
| Ak | Strin g | Quer y | No | LTAIpY33******** | The AccessKey ID. |
| Sk | Strin g | Quer y | No | USER01 | Secret Key ID. |
| MqEndPoin t | Strin g | Quer y | No | ssl://broker1.test.org:888 3 | The endpoint of the message queue service. It includes the protocol, hostname, and port. |
| ConsoleEn dPoint | Strin g | Quer y | No | https://console.example.c om | The endpoint of the console service. |
| Remark | Strin g | Quer y | No | remark | The remarks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information. |

| Data | String | [{}] | The returned data. |
|---|---|---|---|

Example request

```
http(s)://[Endpoint]/?Action=UpdateCloudInfo &OnsRegionId=region123 &PreventCache=234234234 &CloudId=ffe1********6d6d
```

Example responses

```json
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.5.3 DeleteCloudInfo

Deletes information about a specified cloud instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | Region001 | A unique identifier for a specific region. It is used to distinguish between different services or data regions. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 2312342342 | Instructs the client or server not to cache the response content. This ensures that the latest data is retrieved for each request. |
| CloudId | Strin g | Quer y | Yes | ffe1********6d6d | The cloud instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |

Request example

```
http(s)://[Endpoint]/?Action=DeleteCloudInfo &OnsRegionId=Region001 &PreventCache=2312342342 &CloudId=ffe1********6d6d
```

Response example

```json
 "Data":"[{}]",
```

###### 3.1.6.5.4 CreateCloudInfo

Creates a cloud instance for ApsaraMQ for RocketMQ.

**Request headers**

This API operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
| PreventCa che | Long | Quer y | No | 234234234 | Prevents the browser or system from caching data to ensure that each request retrieves the latest content. |
| CloudNam e | Strin g | Quer y | Yes | 212e | The name of the cloud instance. |
| AddRegion Id | Strin g | Quer y | Yes | 1001 | Indicates the ID of the newly added region to identify the newly added geographic region or service range. |
| Ak | Strin g | Quer y | Yes | LTAIpY33******** | The AccessKey ID. |

| Sk | Strin g | Quer y | Yes | 123456 | The unique identifier for the user session. |
|---|---|---|---|---|---|
| MqEndPoin t | Strin g | Quer y | Yes | failover://[tcp://host1:616 16,tcp://host2:61616] | The endpoint of the Message Queue (MQ) service on the local host. This parameter is typically used for message communication in development environments. |
| ConsoleEn dPoint | Strin g | Quer y | Yes | https://console.example.c om | The endpoint of the console service. It is used to access the system administration interface from a browser. |
| Remark | Strin g | Quer y | Yes | remark | The remark. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API operation or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateCloudInfo &OnsRegionId=region123 &CloudName=212e &AddRegionId=1001 &Ak=LTAIpY33******** &Sk=123456 &MqEndPoint=failover://[tcp://host1:61616,tcp://host2:61616] &ConsoleEndPoint=https://console.example.com &Remark=remark
```

Sample success response

```json
 "Data":"[{}]",
```

###### 3.1.6.5.5 QueryCloudInfo

Queries a paginated list of Alibaba Cloud services that are related to Message Queue.

**Request headers**

This operation does not have special request headers. For more information about common request headers, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
| PreventCa che | Long | Quer y | Yes | 213123123 | A parameter that prevents the browser from caching content. This ensures that each request fetches the latest data from the server. |

| CurrentPa ge | Integ er | Quer y | Yes | 1 | The page number of the current page during paging query. |
|---|---|---|---|---|---|
| PageSize | Integ er | Quer y | Yes | 10 | The number of entries to return on each page for a paged query. Default value: 10. |
| CloudInfoK ey | Strin g | Quer y | No | CREATED AT _ | A unique identifier. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID of a client session in the Message Queue service. This ID is used to track and manage the session state. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryCloudInfo &OnsRegionId=REGION_001 &PreventCache=213123123 &CurrentPage=1 &PageSize=10
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

##### 3.1.6.6 Message management

###### 3.1.6.6.1 PushMessage

You can use the PushMessage API to push messages to a specified consumer group in ApsaraMQ for RocketMQ.

**Request header**

This operation uses common request headers and has no special request headers. For more information, see Common parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The unique identifier for a specific region. This parameter distinguishes between different region configurations or deployment environments. |

| PreventCa che | Long | Quer y | Yes | 324243242 | Prevents the browser from caching page content. This ensures that each request retrieves the latest data from the server. |
|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | 1 | The application group ID. |
| Topic | Strin g | Quer y | Yes | test | The topic name. |
| ClientId | Strin g | Quer y | Yes | GID test@@@test _ | The backup client ID. |
| MsgId | Strin g | Quer y | Yes | 0BC16699165C03B925D B8A404E2D**** | The message ID of the m essage to query. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number. |

Request example

```
http(s)://[Endpoint]/?Action=PushMessage &OnsRegionId=REGION_001 &PreventCache=324243242 &GroupId=1 &Topic=test &ClientId=GID_test@@@test &MsgId=0BC16699165C03B925DB8A404E2D****
```

Response examples

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.6.2 DownloadMessageBodyInDLQ

Downloads the message body of a specified message from a dead-letter queue.

**Request headers**

This operation uses common request headers. No special request headers are used. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region identifier of the Ons service, which specifies the geographic region where the message service is located. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 6262355332 | Prevents the browser or system from caching data. This ensures that the latest content is retrieved with each request. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | GID-01 | The ID of the consumer group. |
| MsgId | Strin g | Quer y | Yes | 0BC16699165C03B925D B8A404E2D**** | The ID of the Message to be queried, that is, Message ID. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | A unique ID that identifies a client session in the Message Queue service. This ID maintains the connection state between the client and the server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |

| Data | String | [{}] | The returned data. |
|---|---|---|---|
| Total | Long | 1 | The total number. |

Sample request

```
http(s)://[Endpoint]/?Action=DownloadMessageBodyInDLQ &OnsRegionId=region123 &PreventCache=6262355332 &InstanceId=bastionhost-12****** &GroupId=GID-01 &MsgId=0BC16699165C03B925DB8A404E2D****
```

Sample response (success)

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.6.3 DownloadMessageAllInDLQ

Downloads a batch of messages from a dead-letter queue.

**Request headers**

This API operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The identifier of a specific geographical or logical region. |

| PreventCa che | Long | Quer y | Yes | 23423423424 | Instructs the system or browser not to cache the current request or resource. This ensures that each request retrieves the latest content directly from the server. |
|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | GID-01 | The group ID. |
| MsgId | Strin g | Quer y | Yes | 0BC16699165C03B925D B8A404E2D**** | The message ID of the m essage to query. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The identifier for a session between the client and the server in Alibaba Cloud Message Service (ONS). It is used to associate and manage the process of sending and receiving messages. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=DownloadMessageAllInDLQ &OnsRegionId=region123 &PreventCache=23423423424 &InstanceId=bastionhost-12****** &GroupId=GID-01 &MsgId=0BC16699165C03B925DB8A404E2D**** &Common request parameters
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.6.4 DownloadMessage

Download the API interface for the specified message.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the Common request parameters document.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | A unique identifier for a specific area. This parameter is used to distinguish between different areas where the endpoint is deployed or data centers. |

| PreventCa che | Long | Quer y | Yes | 23432432 | Prevents the browser or system from using cached data. This ensures that each request retrieves the latest content from the server. |
|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | Yes | test | The topic name. |
| MsgId | Strin g | Quer y | Yes | 0BC16699165C03B925D B8A404E2D**** | The message ID of the m essage to query. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID that identifies a client session in the ONS service. This ID is used to maintain the connection state of the producer or consumer. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |

Sample request

```
http(s)://[Endpoint]/?Action=DownloadMessage &OnsRegionId=Region001 &PreventCache=23432432 &InstanceId=bastionhost-12****** &Topic=test &MsgId=0BC16699165C03B925DB8A404E2D****
```

Sample response

```json
 "Data":"[{}]",
```

###### 3.1.6.6.5 QueryMessageByPagedTopic

Queries a paginated list of messages in a specified topic.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region identifier of the Ons service, which specifies the geographic region where the service is located. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | Yes | test | The topic name. |

| TaskId | Strin g | Quer y | No | 123456 | The task ID. |
|---|---|---|---|---|---|
| BeginTime | Long | Quer y | Yes | 1570852800000 | The start time. |
| EndTime | Long | Quer y | Yes | 1704938400 | The end time. |
| CurrentPa ge | Integ er | Quer y | No | 1 | The page number of the current page during paging query. |
| PageSize | Integ er | Quer y | Yes | 10 | The number of rows per page that are set for paging queries. Default value: 10. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique identifier for the current ONS session. This ID is used to track and manage the process of sending and receiving messages. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryMessageByPagedTopic &OnsRegionId=region123 &Topic=test &BeginTime=1570852800000 &EndTime=1704938400 &PageSize=10
```

Response example

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.6.6 QueryMessageByPagedDLQ

Performs a paged query for messages in a dead-letter queue (DLQ).

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | region1 | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 3244523452 | A parameter to prevent the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | GID-01 | The group ID. |
| TaskId | Strin g | Quer y | No | 123456 | The task ID. |
| CurrentPa ge | Integ er | Quer y | No | 1 | The page number of the current page during paging query. |
| PageSize | Integ er | Quer y | No | 10 | The number of rows per page that are set for paging queries. Default value: 10. |
| BeginTime | Long | Quer y | No | 2022 | The start time. |
| EndTime | Long | Quer y | No | 1706668721 | The end time. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique identifier for a session between the client and the server. It is used to track and manage message sending and consumption. |

| > Document Versi | on: 20260108 |   | 14 |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | An additional message. |
| Data | Map | {} | The data returned. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryMessageByPagedDLQ &OnsRegionId=region1 &PreventCache=3244523452 &InstanceId=bastionhost-12****** &GroupId=GID-01 &Common request parameters
```

Sample response

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.6.7 QueryMessageByKey

Queries messages based on message keys.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region01 | The ID of the sample region to identify a specific region in the message service. |
| PreventCa che | Long | Quer y | Yes | 3453434534 | A timestamp used to prevent browser caching. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
| Key | Strin g | Quer y | Yes | TestKey | The message key. |

| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID of a client session in Message Service. This ID distinguishes different producer or consumer sessions. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryMessageByKey &OnsRegionId=region01 &PreventCache=3453434534 &Topic=test &Key=TestKey
```

Sample responses

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.6.8 QueryMessageByIdInDLQ

Queries the details of a specific message in a dead-letter queue (DLQ) by its message ID.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region1 | The region identifier for the Open Notification Service (ONS). This parameter specifies the geographical region where the resource is located. |
| PreventCa che | Long | Quer y | Yes | 5353453533 | Prevents the browser from caching the page content. This ensures that each request retrieves the latest data from the server. |

| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
|---|---|---|---|---|---|
| GroupId | Strin g | Quer y | Yes | GID-01 | The group ID. |
| MsgId | Strin g | Quer y | Yes | 0BC16699165C03B925D B8A404E2D**** | The message ID of the m essage to query. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | A unique identifier for a session or request in ONS. It is used to track and manage the process of sending and receiving messages. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryMessageByIdInDLQ &OnsRegionId=region1 &PreventCache=5353453533 &InstanceId=bastionhost-12****** &GroupId=GID-01 &MsgId=0BC16699165C03B925DB8A404E2D****
```

Sample responses

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.6.9 QueryMessageById

Queries the details of a specific message by its message ID.

**Request headers**

This operation uses only common request headers. For more information, see the common request parameters document.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | REGION001 | The identifier for a specific region. This parameter distinguishes different service areas or data centers. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 2342424 | Prevents the browser or system from using cached data. This ensures that each request retrieves the latest content. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The ID of the instance. |
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
| MsgId | Strin g | Quer y | Yes | 0BC16699165C03B925D B8A404E2D**** | The message ID of the m essage to query. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique session identifier for communication between the client and the service. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The data returned. |

Request example

```
http(s)://[Endpoint]/?Action=QueryMessageById &OnsRegionId=REGION001 &PreventCache=2342424 &InstanceId=bastionhost-12****** &Topic=test &MsgId=0BC16699165C03B925DB8A404E2D****
```

Response example

```json
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.6.10 TraceMessage

Queries the trace of a message to track its path through a message queue.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The unique identifier for a region. This ID is used to distinguish between different service areas or data centers. |

| PreventCa che | Long | Quer y | Yes | 23424234234 | Prevents the browser from caching page content. This ensures that each request retrieves the latest data from the server. |
|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | Yes | test | The topic name. |
| MsgId | Strin g | Quer y | Yes | 0BC16699165C03B925D B8A404E2D**** | The message ID of the m essage to query. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID for a session or request in ApsaraMQ for RocketMQ (ONS). This ID is used to track and manage the sending and receiving of messages. |
| NeedDeliv eryResult | Bool ean | Quer y | No | false | Specifies whether a delivery result is required. This is often used to indicate that a process or task needs to return a final result to the caller or system. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API or a POP error code. |

| Message | String | success | Additional information. |
|---|---|---|---|
| Total | Long | 1 | The total number. |

Request example

```
http(s)://[Endpoint]/?Action=TraceMessage &OnsRegionId=region123 &PreventCache=23424234234 &Topic=test &MsgId=0BC16699165C03B925DB8A404E2D****
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.6.11 SendMessage

Sends messages to ApsaraMQ for RocketMQ.

**Request headers**

This operation uses common request headers. No special request headers are used. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
|---|---|---|---|---|---|
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The ID of the sample region to identify a specific region in the message service. |
| PreventCa che | Long | Quer y | Yes | 2342342342 | Prevents the browser or system from caching data to ensure that each request retrieves the latest content. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | Yes | test | The topic name. |
| Tag | Strin g | Quer y | No | Tag1 | A list of tags. |
| Key | Strin g | Quer y | No | TestKey | The tag key. |
| Message | Strin g | Quer y | Yes | ***** | The message content. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |

| Data | String | [{}] | The returned data. |
|---|---|---|---|

Request example

```
http(s)://[Endpoint]/?Action=SendMessage &OnsRegionId=region123 &PreventCache=2342342342 &Topic=test &Message=*****
```

Sample successful response

```json
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.6.12 ResendMessageByIdInDLQ

Resends a message in a dead-letter queue.

**Request header**

This operation has no special request headers. For more information about common request headers, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | hangzhou | The unique identifier for a region in Message Service. This ID distinguishes different geographical or logical regions. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 423423424 | Prevents the browser or system from using cached data. This ensures that each request retrieves the latest content. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | 1 | The consumer group ID. |
| MsgId | Strin g | Quer y | Yes | 0BC16699165C03B925D B8A404E2D**** | The message ID of the m essage to query. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number. |

Request example

```
http(s)://[Endpoint]/?Action=ResendMessageByIdInDLQ &OnsRegionId=hangzhou &PreventCache=423423424 &InstanceId=bastionhost-12****** &GroupId=1 &MsgId=0BC16699165C03B925DB8A404E2D****
```

Successful response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

##### 3.1.6.7 Empower management

###### 3.1.6.7.1 CheckFortestRamAction

Verifies the RAM permissions in a test environment.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region identifier of the Ons service, which specifies the geographic region where the service is located. |
|---|---|---|---|---|---|
| ResourceId | Strin g | Quer y | Yes | eas-r-asdasdasd**** | The resource ID. |
| AuthAction Name | Strin g | Quer y | Yes | RevokePermission | he system requires users to provide additional authentication information. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | The additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=CheckFortestRamAction &OnsRegionId=ExampleValue &ResourceId=eas-r-asdasdasd**** &AuthActionName=RevokePermission
```

Sample successful response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.7.2 DeleteDauthToolByUserId

Deletes an authorization tool by user ID.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| UserId | Strin g | Quer y | Yes | agent@ccc-test | The user ID. |
| SleepSeco nd | Integ er | Quer y | Yes | 3 | Indicates that a program or process sleeps for 3 seconds. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |

| Code | Integer | 200 | The API status code or a POP error code. |
|---|---|---|---|
| Message | String | success | Additional information. |
| Data | String | [{}] | The data returned. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=DeleteDauthToolByUserId &UserId=agent@ccc-test &SleepSecond=3
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.7.3 CreateGroupEmpowerBySub

Grants a RAM user permissions on a specified consumer group in ApsaraMQ for RocketMQ.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The region identifier of the Ons service, which specifies the geographic region where the service is located. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 2343242342 | Prevents the browser or system from caching data. This ensures that each request retrieves the latest content. |
| EmpowerU ser | Strin g | Quer y | Yes | exportUserData | Permission to reset user passwords. |
| GroupId | Strin g | Quer y | Yes | 1 | Application group ID. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The data returned. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateGroupEmpowerBySub &OnsRegionId=REGION_001 &PreventCache=2343242342 &EmpowerUser=exportUserData &GroupId=1 &InstanceId=bastionhost-12******
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.7.4 CreateEmpowerBySub

Grants permissions on ApsaraMQ for RocketMQ to a specified RAM user.

**Request headers**

This operation uses only common request headers. For more information, see Common parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | qingdao | A unique identifier that represents a specific region and is used to distinguish different geographic or logical regions. |
| PreventCa che | Long | Quer y | Yes | 34242342 | Prevents the browser or server from caching data. This ensures that the latest content is retrieved with each request. |

| EmpowerU ser | Strin g | Quer y | Yes | revokeRole | The user to whom you want to grant permissions. |
|---|---|---|---|---|---|
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
| Relation | Integ er | Quer y | Yes | 6 | The relationship type. Valid values: Equal: Equal to. Unequal: Not equal to. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=CreateEmpowerBySub &OnsRegionId=qingdao &PreventCache=34242342 &EmpowerUser=revokeRole &Topic=test &Relation=6
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.7.5 CreateEmpower

Creates an authorization for ApsaraMQ for RocketMQ.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The region identifier of the Ons service, which specifies the geographic region where the message service is located. |
| PreventCa che | Long | Quer y | Yes | 23423424 | A timestamp used to prevent the browser from caching content. This ensures that each request retrieves the latest data from the server. |

| EmpowerU ser | Strin g | Quer y | Yes | revokeRole | You can revoke permissions from a user role. |
|---|---|---|---|---|---|
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
| Relation | Integ er | Quer y | Yes | 6 | The relationship for the user group. Valid values: Equal: Equal to. Unequal: Not equal to. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateEmpower &OnsRegionId=Region001 &PreventCache= &EmpowerUser=revokeRole &Topic=test &Relation=6
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.7.6 QueryGroupEmpowerList

Queries the authorization list for a specified instance and consumer group.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The region identifier of the Ons service, which specifies the geographic region where the service is located. |
| GroupId | Strin g | Quer y | Yes | 1 | The ID of the consumer group. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or the POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryGroupEmpowerList &OnsRegionId=Region001 &GroupId=1 &InstanceId=bastionhost-12******
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.7.7 QueryEmpowerList

Queries the authorization list for ApsaraMQ for RocketMQ.

**Request headers**

This operation uses only common request headers. For more information, see the Common request parameters document.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | Indicates region 1, which is usually used to identify different geographic regions or logical partitions. It is suitable for Region Division in scenarios such as message queue and service deployment. |
| Topic | Strin g | Quer y | No | test | The topic name. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| OnsSessio nId | Strin g | Quer y | No | 1234567890 | The session ID. It identifies the connection between a client and the server to ensure message ordering and maintain state. |

| 73 |   |   | > Document Version: 2026010 |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or the POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryEmpowerList &OnsRegionId=REGION01
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.7.8 DeleteGroupEmpower

Deletes an authorization group in ApsaraMQ for RocketMQ.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | hangzhou | Primary Region 1 is used to distinguish different service deployment regions. |
| PreventCa che | Long | Quer y | Yes | 32423423424 | A timestamp used to prevent the browser or server from caching data. This ensures that each request retrieves the latest content. |
| EmpowerU ser | Strin g | Quer y | No | user123 | The user who has permissions to view, edit, manage personal account information, and publish content. |
| GroupId | Strin g | Quer y | Yes | 1 | The ID of the application group. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number. |

Sample request

```
http(s)://[Endpoint]/?Action=DeleteGroupEmpower &OnsRegionId=hangzhou &PreventCache=32423423424 &GroupId=1 &InstanceId=bastionhost-12******
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.7.9 DeleteEmpower

Deletes the authorization for a specified topic in ApsaraMQ for RocketMQ.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| > Document V | ersion: 2 | 026010 | 8 |   | 17 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The unique identifier of the business group. This ID distinguishes between different geographical or logical regions in Message Service. |
| PreventCa che | Long | Quer y | Yes | 63636363 | A timestamp used to prevent the browser from caching the response. This ensures that you retrieve the latest data from the server for each request. |
| EmpowerU ser | Strin g | Quer y | No | ExampleValue | This user has permissions to view, edit, manage task assignment, and track progress within a specified project. |
| Topic | Strin g | Quer y | Yes | test | The topic name. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code. A POP error code is returned if the call fails. |

| Message | String | success | Additional information. |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=DeleteEmpower &OnsRegionId=Region001 &PreventCache=63636363 &Topic=test &Common request parameters
```

Successful response example

```json
 "Total":1,
 "Data":"[{}]",
```

##### 3.1.6.8 MQTT management API

###### 3.1.6.8.1 DeleteMqttGroupId

Deletes the specified MQTT group ID.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 123123123 | Instructs the system or browser not to cache the current request. This ensures that the latest content is retrieved directly from the server for each request. |
| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
| GroupId | Strin g | Quer y | No | 1 | The ID of the application group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=DeleteMqttGroupId &OnsRegionId=Region001 &PreventCache=123123123 &MqttInstanceId=post-cn-7mz2d******
```

Sample successful response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.8.2 SendMqtt

The interface that sends messages through the specified MQTT instance.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
| PreventCa che | Long | Quer y | Yes | 3423423424 | Prevents the browser or system from using cached data. This ensures that each request retrieves the latest content. |

| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
|---|---|---|---|---|---|
| FirstTopic | Strin g | Quer y | No | Technology | The first topic. |
| SecondTop ic | Strin g | Quer y | No | UserBehavior | The second topic. |
| Qos | Integ er | Quer y | No | 0 | Specify how to send the message. |
| CleanSessi on | Bool ean | Quer y | No | false | Specifies whether to start a clean session. |
| Body | Strin g | Quer y | No | An image binary file | The request body. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=SendMqtt &OnsRegionId=region123 &PreventCache=3423423424 &MqttInstanceId=post-cn-7mz2d******
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.3 QueryMqttMsgTransTask

Queries the history of publish and subscribe operations for an MQTT message transmission task.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | qingdao | A unique identifier used to distinguish different service or geographical areas. |

| PreventCa che | Long | Quer y | Yes | 23423423 | Prevents the browser or system from using cached data. This ensures that each request retrieves the latest content from the server. |
|---|---|---|---|---|---|
| ConsoleTy pe | Strin g | Quer y | Yes | DesktopConsole | The console type. |
| QueryType | Strin g | Quer y | Yes | 1 | The query type. |
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
| SecondTop ic | Strin g | Quer y | No | test2 | The secondary topic. |
| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
| MsgType | Strin g | Quer y | No | text | The message type. |
| Qos | Integ er | Quer y | No | 0 | The Quality of Service (QoS) level. |
| BeginTime | Long | Quer y | No | 2022 | The start time. |
| EndTime | Long | Quer y | No | 1707118672 | The end time. |
| Period | Long | Quer y | No | 1 | The period. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
|---|---|---|---|
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the response or a POP error code. |
| Message | String | success | Additional information |
| Data | Map | {} | The data returned. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryMqttMsgTransTask &OnsRegionId=qingdao &PreventCache=23423423 &ConsoleType=DesktopConsole &QueryType=1 &Topic=test &MqttInstanceId=post-cn-7mz2d******
```

Sample successful response

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.4 CreateMqttInstanceStoreResource

Creates a storage resource for an MQTT instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The identifier for the region. |
| PreventCa che | Long | Quer y | Yes | 234242 | Prevents the client or server from caching the response. This ensures that each request retrieves the latest data from the source server. |
| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
| StoreType | Integ er | Quer y | Yes | 2 | The type of external storage. This parameter is fixed to `oss`. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |

| Topic | Strin g | Quer y | Yes | test | The topic name. |
|---|---|---|---|---|---|
| OrderType | Integ er | Quer y | No | 1 | The order type. |
| Remark | Strin g | Quer y | No | remark | The remarks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=CreateMqttInstanceStoreResource &OnsRegionId=REGION_001 &PreventCache=234242 &MqttInstanceId=post-cn-7mz2d****** &StoreType=2 &Topic=test
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.8.5 CreateMqttInstance

Creates a Message Queuing Telemetry Transport (MQTT) instance to enable access to ApsaraMQ for RocketMQ using the MQTT protocol.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region1 | The ID of the logical region. |
| PreventCa che | Long | Quer y | Yes | 342342342 | Prevents the browser from caching page content to ensure that the latest data is retrieved from the server for each request. |
| InstanceN ame | Strin g | Quer y | No | myinstance | The name of the instance. |
| Remark | Strin g | Quer y | No | remark | The remarks. |
| MaxConn | Long | Quer y | Yes | 5000 | The maximum number of connections for the instance specification. |

| MaxSub | Long | Quer y | Yes | 3 | The maximum number of subscriptions or subkeys per system or program is 5. |
|---|---|---|---|---|---|
| MaxDownT ps | Long | Quer y | Yes | 150 | The maximum number of downstream transactions per second (TPS). This parameter measures the processing capability of the system under high payloads. |
| MaxUpTps | Long | Quer y | Yes | 150 | The maximum number of upstream transactions per second (TPS). |
| Independe ntNaming | Bool ean | Quer y | Yes | true | Specifies whether the instance has a namespace. Valid values: true: The instance has an independent namespace. Resource names must be unique within the instance but can be the same across different instances. false: The instance does not have an independent namespace. Resource names must be globally unique, both within the instance and across different instances. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |

| Code | Integer | 200 | The status code of the API operation or a POP error code. |
|---|---|---|---|
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number. |

Request example

```
http(s)://[Endpoint]/?Action=CreateMqttInstance &OnsRegionId=region1 &PreventCache=342342342 &MaxConn=5000 &MaxSub=3 &MaxDownTps=150 &MaxUpTps=150 &IndependentNaming=true
```

Successful response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.8.6 CreateMqttGroupId

Creates an MQTT group ID.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|

| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
|---|---|---|---|---|---|
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The ID of the region where the Message Service is located. |
| PreventCa che | Long | Quer y | Yes | 23342342 | Prevents the browser or system from using cached data. This ensures that each request retrieves the latest content. |
| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
| GroupId | Strin g | Quer y | No | 1 | The application group ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request is successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=CreateMqttGroupId &OnsRegionId=region123 &PreventCache=23342342 &MqttInstanceId=post-cn-7mz2d******
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.8.7 PageQueryMqttInstanceStoreResource

Performs a paged query on the storage resources of MQTT instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information about common request headers, see Common parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | ExampleRegion01 | The region ID for the Ons service specifies the geographic region of the resource. |
| PreventCa che | Long | Quer y | Yes | 32423 | A timestamp that is used to prevent the browser from caching data. This ensures that each request retrieves the latest content. |

| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
|---|---|---|---|---|---|
| StoreType | Integ er | Quer y | Yes | oss | External storage type |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| CurrentPa ge | Integ er | Quer y | No | 1 | The page number of the current page during paging query. |
| PageSize | Integ er | Quer y | No | 10 | The number of rows per page that are set for paging queries. |
| Search | Strin g | Quer y | No | 1 1 1 1 1 _ _ _ _ | The search keyword. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | API status code or POP error code. |
| Message | String | success | Additional information |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=PageQueryMqttInstanceStoreResource &OnsRegionId=ExampleRegion01 &PreventCache=32423 &MqttInstanceId=post-cn-7mz2d****** &StoreType=oss &InstanceId=bastionhost-12****** <Common request parameters>
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.8.8 PageQueryMqttInstanceList

Queries a paginated list of MQTT instances.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | It is used to distinguish different service deployment areas. |
| PreventCa che | Long | Quer y | Yes | 234234234 | Prevents the browser or server from using cached data. This ensures that each request retrieves the latest content. |

| CurrentPa ge | Integ er | Quer y | No | 1 | The page number of the current page during paging query. |
|---|---|---|---|---|---|
| PageSize | Integ er | Quer y | No | 10 | The number of rows per page that are set for paging queries. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=PageQueryMqttInstanceList &OnsRegionId=REGION_001 &PreventCache=234234234
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.8.9 PageQueryMqttGroupId

Performs a paged query to retrieve a list of group IDs for MQTT instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region01 | The region identifier of the Ons service, which is used to specify the geographic region of the message service. |
| PreventCa che | Long | Quer y | Yes | 234241212 | Prevents the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
| Search | Strin g | Quer y | No | 1 1 1 1 1 _ _ _ _ | The search keyword. |
| CurrentPa ge | Integ er | Quer y | No | 1 | The page number of the current page during paging query. |

| PageSize | Integ er | Quer y | No | 10 | The number of rows per page that are set for paging queries. |
|---|---|---|---|---|---|
| IsFuzzy | Bool ean | Quer y | No | false | Indicates that the results or conditions are determinate. |
| Type | Integ er | Quer y | No | 1 | The type. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the interface or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=PageQueryMqttGroupId &OnsRegionId=Region01 &PreventCache=234241212 &MqttInstanceId=post-cn-7mz2d******
```

Successful response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.8.10 DeleteMqttInstanceStoreResource

Deletes the storage resource for a specified MQTT instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The identifier of a specific region, used to distinguish between different regions or service nodes. |
| PreventCa che | Long | Quer y | Yes | 53534342534 | A timestamp used to prevent the browser from using cached data. This ensures that you retrieve the latest data from the server with each request. |
| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
| StoreType | Integ er | Quer y | Yes | 1 | The type of external storage. This is fixed to oss. |

| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
|---|---|---|---|---|---|
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | API status or POP error code. |
| Message | String | success | Additional information |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=DeleteMqttInstanceStoreResource &OnsRegionId=region123 &PreventCache=53534342534 &MqttInstanceId=post-cn-7mz2d****** &StoreType=1 &Topic=test
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.8.11 DeleteMqttInstance

Deletes the specified MQTT instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region identifier of the Ons service, which specifies the geographic region where the service is located. |
| PreventCa che | Long | Quer y | Yes | 234234324 | Prevents the browser or server from caching data to ensure that each request retrieves the latest content. |
| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=DeleteMqttInstance &OnsRegionId=region123 &PreventCache=234234324 &MqttInstanceId=post-cn-7mz2d******
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.8.12 QueryMqttInstanceReport

Queries the runtime report statistics for MQTT instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|

| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
|---|---|---|---|---|---|
| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | The unique identifier for a specific region. This parameter is used in Message Service to distinguish between different geographical or logical areas. |
| PreventCa che | Long | Quer y | Yes | 234234242 | Prevents the browser from caching page content. This ensures that each request retrieves the latest data from the server. |
| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
| BeginTime | Long | Quer y | Yes | 2022 | The start time. |
| EndTime | Long | Quer y | Yes | 1706668721 | The end time. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |

| Data | Map | {} | The returned data. |
|---|---|---|---|
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryMqttInstanceReport &OnsRegionId=REGION01 &PreventCache=234234242 &MqttInstanceId=post-cn-7mz2d****** &BeginTime=2022 &EndTime=1706668721
```

Sample success response

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.13 QueryMqttInstanceList

Queries a list of MQTT instances in a specified region.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| > Document V | ersion: 2 | 026010 | 8 |   | 20 |
|---|---|---|---|---|---|

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The ID of the region where Message Service is deployed. It is used to distinguish resources in different regions. |
| PreventCa che | Long | Quer y | Yes | 23423423 | Prevents the browser from caching content. This ensures that the latest data is retrieved from the server for each request. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID of the session. It is used to track and manage the session in Message Service. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API call or a POP error code. |
| Message | String | success | Additional information. |

Request example

```
http(s)://[Endpoint]/?Action=QueryMqttInstanceList &OnsRegionId=Region001 &PreventCache=23423423
```

Response examples

```json
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.14 QueryMqttInstanceBaseInfo

Queries the basic information for MQTT instance, such as the instance ID, name, and specifications.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The region where the ONS endpoint is deployed. |

| PreventCa che | Long | Quer y | Yes | 34234242 | A timestamp that is used to prevent the browser and system from caching data. This ensures that the latest data is retrieved for each request. |
|---|---|---|---|---|---|
| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryMqttInstanceBaseInfo &OnsRegionId=Region001 &PreventCache=34234242 &MqttInstanceId=post-cn-7mz2d******
```

Sample response

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.15 QueryMqttGroupIdList

Queries all group IDs in a specified for MQTT instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the Common request parameters document.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION US 01 _ _ | The unique identifier for a region. This ID distinguishes different geographical or logical regions. |
| PreventCa che | Long | Quer y | Yes | 763465327325 | Prevents the browser from caching content. This ensures that each request retrieves the latest data from the server. |

| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryMqttGroupIdList &OnsRegionId=REGION_US_01 &PreventCache=763465327325 &MqttInstanceId=post-cn-7mz2d******
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.16 QueryMqttDeviceRunningInfo

Queries the running status of an MQTT device.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The ID of a geographic or logical area. This ID is used to distinguish between different service areas or data centers. |
| PreventCa che | Long | Quer y | Yes | true | Specifies whether to disable the cache. If you set this parameter to true, each request retrieves the latest data from the server and does not use the local cache. |

| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
|---|---|---|---|---|---|
| ClientId | Strin g | Quer y | No | ClientID | The client ID. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryMqttDeviceRunningInfo &OnsRegionId=region123 &PreventCache=true &MqttInstanceId=post-cn-7mz2d****** &Common request parameters
```

Sample successful response

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.17 QueryMqttConnectionSum

Queries statistics and trend data for MQTT connections.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | An identifier for a specific geographic or logical region. It is used to distinguish between different service areas or data centers. |
| PreventCa che | Long | Quer y | Yes | 234235234243 | Indicates that the client or server should not cache the response data. This ensures that the latest content is retrieved for each request. |

| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
|---|---|---|---|---|---|
| BeginTime | Long | Quer y | No | 2022 | The start time. |
| EndTime | Long | Quer y | No | 2022 | The end time. |
| GroupId | Strin g | Quer y | No | 1 | The group ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryMqttConnectionSum &OnsRegionId=REGION01 &PreventCache=234235234243 &MqttInstanceId=post-cn-7mz2d******
```

Sample responses

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.18 QueryMqttClientSetByTopic

Queries information about the clients that subscribe to an MQTT topic.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The ID of the region. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The identifier of the area. This parameter is used to distinguish between different service areas or data centers. |
| PreventCa che | Long | Quer y | Yes | 124241212 | Prevents the browser from caching content. This ensures that the latest data is retrieved from the server with each request. |

| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
|---|---|---|---|---|---|
| FirstTopic | Strin g | Quer y | No | Technology | The first topic. |
| SecondTop ic | Strin g | Quer y | No | UserBehavior | The second topic. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryMqttClientSetByTopic &OnsRegionId=region123 &PreventCache=124241212 &MqttInstanceId=post-cn-7mz2d******
```

Response example

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.19 QueryMqttClientSetByGroupId

Queries information about a collection of online clients based on an MQTT Group ID.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The unique identifier of a specific region in the ONS service. |
| PreventCa che | Long | Quer y | Yes | 23214142 | Prevents the browser or system from using cached data. This ensures that the latest content is retrieved for each request. |
| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |

| Developer Gui | de·API re | ference |   | Al | ibaba Cloud Message Queue |
|---|---|---|---|---|---|

| GroupId | Strin g | Quer y | No | GIG-01 | The group ID. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API operation or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryMqttClientSetByGroupId &OnsRegionId=REGION_001 &PreventCache=23214142 &MqttInstanceId=post-cn-7mz2d******
```

Response example

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data/> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.20 QueryMqttTraceByTraceId

Queries the MQTT message traces for a specified Trace ID.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | hangzhou | The identifier for a specific geographic or logical region. |
| PreventCa che | Long | Quer y | Yes | 324242342 | Prevents the browser from caching page content. This ensures that the latest data is retrieved from the server for each request. |
| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |

| Developer Gui | de·API re | ference |   | Al | ibaba Cloud Message Queue |
|---|---|---|---|---|---|

| Topic | Strin g | Quer y | No | test | The name of the topic. |
|---|---|---|---|---|---|
| TraceId | Strin g | Quer y | No | 0a98a334170226880502 075****** | The trace ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryMqttTraceByTraceId &OnsRegionId=hangzhou &PreventCache=324242342 &MqttInstanceId=post-cn-7mz2d******
```

Sample successful response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.21 QueryMqttMsgByPubInfo

Queries MQTT messages based on publication information.

**Request headers**

This operation uses common request headers. Special request headers are not required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | The identifier for a specific geographic or logical region. |
| PreventCa che | Long | Quer y | Yes | 2342342 | A timestamp used to prevent the browser from caching the response. This ensures that you retrieve the latest data. |
| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |

| BeginTime | Long | Quer y | No | 2022 | The beginning of the time range to query. |
|---|---|---|---|---|---|
| EndTime | Long | Quer y | No | 1706668721 | The end of the time range to query. |
| Topic | Strin g | Quer y | No | test | The name of the topic. |
| ClientId | Strin g | Quer y | No | test | The ID of the client. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The data returned. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API operation or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryMqttMsgByPubInfo &OnsRegionId=REGION01 &PreventCache=2342342 &MqttInstanceId=post-cn-7mz2d******
```

Sample responses

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.22 QueryMqttInstanceStoreResourceNameList

Queries the list of instance storage resource names for MQTT instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region01 | The ID of a specific area in Message Service. This ID distinguishes different geographical or logical areas. |
| PreventCa che | Long | Quer y | Yes | 234234234 | A timestamp used to prevent the browser from caching page content. This ensures that each request retrieves the latest data from the server. |

| Developer Gui | de·API re | ference |   | Al | ibaba Cloud Message Queu |
|---|---|---|---|---|---|

| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
|---|---|---|---|---|---|
| StoreType | Integ er | Quer y | Yes | 3 | The type of external storage. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryMqttInstanceStoreResourceNameList &OnsRegionId=region01 &PreventCache=234234234 &MqttInstanceId=post-cn-7mz2d****** &StoreType=3 &InstanceId=bastionhost-12****** &Common request parameters
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.23 QueryMqttInstanceStoreInstanceList

Queries the storage instances of an MQTT instance.

**Request header**

This operation uses only common request headers. For more information, see Common parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The ID of the region. |

| OnsRegion Id | Strin g | Quer y | Yes | Region001 | A unique identifier that represents a specific region and is used to distinguish different geographic or logical regions. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 723635625425 | Prevents the browser from caching page content. This ensures that each request retrieves the latest data from the server. |
| StoreType | Integ er | Quer y | No | 2 | The type of external storage. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The response data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryMqttInstanceStoreInstanceList &OnsRegionId=Region001 &PreventCache=723635625425
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.24 UpdateMqttInstance

Updates the details of a specified MQTT instance.

**Request headers**

This operation uses common request headers and does not require special request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The ID of the region. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION06 | The unique identifier for a specific region. This parameter is used to distinguish between different geographical or logical areas. |
| PreventCa che | Long | Quer y | Yes | 2424324234 | Prevents browsers or systems from using cached data. This ensures that each request retrieves the latest content. |

| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
|---|---|---|---|---|---|
| MqttInstan ceName | Strin g | Quer y | Yes | myMqtt | The name of the instance. |
| Remark | Strin g | Quer y | Yes | remark | The remarks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=UpdateMqttInstance &OnsRegionId=REGION06 &PreventCache=2424324234 &MqttInstanceId=post-cn-7mz2d****** &MqttInstanceName=myMqtt &Remark=remark
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.25 ChangeMqttInstanceSpec

Changes the instance type for MQTT instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The unique identifier for a region in Message Service. It ensures regional fencing and optimizes service deployment and data transmission. |
| PreventCa che | Long | Quer y | Yes | 2342342 | Prevents the browser or system from caching data. This ensures that each request retrieves the latest content. |

| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
|---|---|---|---|---|---|
| MaxConn | Long | Quer y | Yes | 5000 | The maximum number of connections for the instance type. |
| MaxSub | Long | Quer y | Yes | 5 | Indicates that the maximum number of subscriptions allowed in a system or application is 5. |
| MaxDownT ps | Long | Quer y | Yes | 150 | Indicates that the maximum downstream transaction processing rate of the system is 150 transactions per second. |
| MaxUpTps | Long | Quer y | Yes | 150 | The maximum number of uploaded transactions that the system can process per unit time is 150 per second. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | API status or a POP error code. |
| Message | String | success | Additional information |
| Data | String | [{}] | The returned data. |

| Total | Long | 1 | The total number of entries. |
|---|---|---|---|

Request example

```
http(s)://[Endpoint]/?Action=ChangeMqttInstanceSpec &OnsRegionId=region123 &PreventCache=2342342 &MqttInstanceId=post-cn-7mz2d****** &MaxConn=5000 &MaxSub=5 &MaxDownTps=150 &MaxUpTps=150
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.8.26 BindMqttInstance

ind an MQTT instance to ApsaraMQ for RocketMQ.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
|---|---|---|---|---|---|
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The region identifier of the Ons service, which specifies the geographic region where the instance is located. |
| PreventCa che | Long | Quer y | Yes | 3242423 | A timestamp used to prevent browser caching. This ensures that each request retrieves the latest data from the server. |
| MqttInstan ceId | Strin g | Quer y | Yes | post-cn-7mz2d****** | The ID of the instance to which the CA certificate is bound, that is, the ID of the MQTT instance. |
| StoreType | Integ er | Quer y | Yes | 2 | he type of external storage. This is fixed as oss. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number. |

Sample request

```
http(s)://[Endpoint]/?Action=BindMqttInstance &OnsRegionId=REGION_001 &PreventCache=3242423 &MqttInstanceId=post-cn-7mz2d****** &StoreType=2 &InstanceId=bastionhost-12******
```

Sample response

```json
 "Total":1,
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Code>200</Code> <Success>true</Success>
```

##### 3.1.6.9 Trace management

###### 3.1.6.9.1 QueryTraceMapByQueryId

Retrieves the complete event chain diagram of a message trace based on a query ID. This diagram shows the full path of the message, from the time it is sent until it is consumed.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | Indicates the region ID used in the message service to specify the geographic region where the resource is located. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 3665454 | Prevents the browser from caching page content. This ensures that the latest data is retrieved from the server for each request. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| QueryId | Strin g | Quer y | Yes | 123 | The unique ID of the query. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The ID of the session between the client and the server. This ID is used for ordered message processing and state persistence. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryTraceMapByQueryId &OnsRegionId=REGION01 &PreventCache=3665454 &InstanceId=bastionhost-12****** &QueryId=123
```

Sample response

```json
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.9.2 QueryPubTraceByQueryId

Retrieves the details of a message publishing trace based on a query ID.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The identifier of a specific geographic or logical region. |

| PreventCa che | Long | Quer y | Yes | 231241431 | Prevents the browser or system from caching data. This ensures that each request retrieves the latest content from the server. |
|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| QueryId | Strin g | Quer y | Yes | 123 | The query ID. This is the unique identifier for the query. |
| CurrentPa ge | Integ er | Quer y | No | 1 | The number of the current page. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID that identifies a client session when you use Alibaba Cloud Open Notification Service (ONS). This ID is used to track and manage message consumption or production sessions. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API operation or a POP error code. |
| Message | String | success | Additional information. |

| Data | Map | {} | The returned data. |
|---|---|---|---|

Example request

```
http(s)://[Endpoint]/?Action=QueryPubTraceByQueryId &OnsRegionId=Region001 &PreventCache=231241431 &InstanceId=bastionhost-12****** &QueryId=123 &Common request parameters
```

Example responses

```json
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.9.3 PageQueryTraceListByUserId

Queries a paginated list of message traces for a user.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The unique identifier for a region. This ID is used to distinguish between different geographical or logical areas. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 32423432424 | A parameter used to prevent browsers or systems from caching data. This ensures that each request retrieves the latest content. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries to return on each page for a paged query. Default value: 10. |
| CurrentPa ge | Integ er | Quer y | No | 1 | The page number of the current page during paging query. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID of a push notification session in Open Notification Service (ONS). This ID is used to track and manage the lifecycle of a message push. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |

| Code | Integer | 200 | The API status or POP error code. |
|---|---|---|---|
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Example request

```
http(s)://[Endpoint]/?Action=PageQueryTraceListByUserId &OnsRegionId=Region001 &PreventCache=32423432424 &InstanceId=bastionhost-12******
```

Example of a successful response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.9.4 DeleteTraceQueryTask

The API interface that deletes the message trace query task.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 234555333232 | A timestamp used to prevent the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| QueryId | Strin g | Quer y | Yes | 27296756265288364915 7096685**** | The query ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |

Sample request

```
http(s)://[Endpoint]/?Action=DeleteTraceQueryTask &OnsRegionId=REGION_001 &PreventCache=234555333232 &InstanceId=bastionhost-12****** &QueryId=272967562652883649157096685****
```

Sample response

```json
 "Data":"[{}]",
```

###### 3.1.6.9.5 QueryTraceByMsgTopic

Queries message traces by topic.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | ExampleRegion01 | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
| PreventCa che | Long | Quer y | Yes | 231243123423 | A timestamp that prevents the browser or server from caching data. This ensures that each request retrieves the latest content. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |

| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
|---|---|---|---|---|---|
| BeginTime | Long | Quer y | No | 2022 | The start time. |
| EndTime | Long | Quer y | Yes | 1706668721 | The end time. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | A unique ID that identifies a client session in the Message Queue service. This ID is used to track and manage the process of sending and receiving messages. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryTraceByMsgTopic &OnsRegionId=ExampleRegion01 &PreventCache=231243123423 &InstanceId=bastionhost-12****** &Topic=test &EndTime=1706668721
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.9.6 QueryTraceByMsgKey

Queries a message trace by message key.

**Request header**

This operation requires only common request headers. For more information, see Common parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | region123 | The ID of the geographic or logical region. It is used to distinguish different service areas or data centers. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 342342423 | Prevents the browser from caching page content. This ensures that the latest data is retrieved from the server with each request. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | Yes | test | The topic name. |
| MsgKey | Strin g | Quer y | Yes | ORDERID 100 _ | The message key of the message that you want to query. |
| BeginTime | Long | Quer y | No | 2022 | The start time. |
| EndTime | Long | Quer y | Yes | 1706668721 | The end time. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID that identifies a client session in the Message Queue (MSMQ) service. It is used to maintain the connection status between the client and the server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryTraceByMsgKey &OnsRegionId=region123 &PreventCache=342342423 &InstanceId=bastionhost-12****** &Topic=test &MsgKey=ORDERID_100 &EndTime=1706668721
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.9.7 QueryTraceByMsgId

Queries the message trace for a specified message ID.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION001 | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
| PreventCa che | Long | Quer y | Yes | 23232423 | Prevents the browser from caching page content. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
| MsgId | Strin g | Quer y | Yes | 0BC16699165C03B925D B8A404E2D**** | The message ID of the m essage to query. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID that identifies a client session in the Message Queue service. It maintains the connection status between the client and the server. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
|---|---|---|---|
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryTraceByMsgId &OnsRegionId=REGION001 &PreventCache=23232423 &InstanceId=bastionhost-12****** &Topic=test &MsgId=0BC16699165C03B925DB8A404E2D****
```

Sample successful response

```json
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

##### 3.1.6.10 Consumer management

###### 3.1.6.10.1 CheckFortestConsumerId

Checks whether a consumer ID is valid in the test environment.

**Request headers**

No special request headers are required for this operation. For more information about common request headers, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
| PreventCa che | Long | Quer y | Yes | 2342424 | Prevents the response from being cached. This ensures that each request retrieves the latest data. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | No | 1 | The ID of the application group. |
| ConsumerI d | Strin g | Quer y | No | kafka-test | The name of the Group. The possible values are: It can contain only letters, digits, hyphens (-), and underscores ( ). It must contain at _ least one letter or digit. The length must be 3 to 128 characters. If the name is longer than 128 characters, it is automatically truncated. The group name cannot be changed after it is created. |

| Relation | Integ er | Quer y | Yes | 6 | The relationship of the user group. Valid values: Equal: Equal to. Unequal: Not equal to. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API call or a POP error code. |
| Message | String | success | Additional information |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=CheckFortestConsumerId &OnsRegionId=region123 &PreventCache=2342424 &Relation=6
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.10.2 QueryAllConsumerAccumulation

Queries the message accumulation status of a specified consumer group across all message queues in a specific topic.

**Request headers**

This operation uses only common request headers. For more information, see the Common request parameters document.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
| Topic | Strin g | Quer y | Yes | test | The topic name. |
| GroupId | Strin g | Quer y | Yes | GID-test | The group ID. |
| InstanceId | Strin g | Quer y | No | ccc-test | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
|---|---|---|---|
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryAllConsumerAccumulation &OnsRegionId=Region001 &Topic=test &GroupId=GID-test &Common request parameters
```

Sample response

```json
 "Total":1,
 "Data":{},
```

###### 3.1.6.10.3 QueryConsumerTimespan

Queries the consumption time span for a specified consumer group on a specific topic. This operation returns time-related metrics, such as the earliest and latest consumption times and consumption latency.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
| PreventCa che | Long | Quer y | Yes | 464563643 | A timestamp used to prevent browser caching. It ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | 1 | The group ID. |
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | A unique ID that identifies a client session in the ONS service. It maintains the connection state between the producer or consumer and the server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryConsumerTimespan &OnsRegionId=Region001 &PreventCache=464563643 &InstanceId=bastionhost-12****** &GroupId=1 &Topic=test
```

Sample response

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.10.4 QueryConsumerStatus

Queries the overall status of a specified consumer group. The status includes key operational metrics such as online status, consumer TPS, message accumulation, consumption latency, and subscription relationship consistency.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the documentation about common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The region identifier of the Ons service, which specifies the geographic region where the service is located. |
| PreventCa che | Long | Quer y | Yes | 223435434 | Prevents the browser or server from using cached data. This ensures that each request retrieves the latest information. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | 1 | The group ID. |
| Detail | Bool ean | Quer y | No | true | Content. |
| NeedJstack | Bool ean | Quer y | No | true | Specifies whether to print Jstack information. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID of a client session in the ONS service. This ID distinguishes different producer or consumer sessions. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request succeeded. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryConsumerStatus &OnsRegionId=REGION_001 &PreventCache=223435434 &InstanceId=bastionhost-12****** &GroupId=1
```

Response example

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.10.5 QueryConsumerProgress

Queries the consumption progress of a specified consumer group. This includes details such as the consumer offset, message accumulation, and last consumption time for each message queue.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see the common request parameters document.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | hangzhou | The region identifier of the Ons service, which specifies the geographic region where the service is located. |
| PreventCa che | Long | Quer y | Yes | 23424234242 | A timestamp used to prevent the browser from using cached data. This ensures that each request retrieves the latest content from the server. |
| GroupId | Strin g | Quer y | No | GID-01 | The group ID. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| ConsumerI d | Strin g | Quer y | No | kafka-test | The consumer ID. |

| OnsSessio nId | Strin g | Quer y | No | abc123xyz | Identifies the session between the client and the server. This session is used for ordered message processing and state management. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request is successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryConsumerProgress &OnsRegionId=hangzhou &PreventCache=23424234242 &lt;Common request parameters>
```

Sample responses

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.10.6 QueryConsumerJstackInfo

Queries the thread stack information of a consumer in ApsaraMQ for RocketMQ.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The unique identifier of a specific area. This parameter is used to distinguish different regions or data centers. |
| PreventCa che | Long | Quer y | Yes | 2342342342 | Prevents the browser from caching page content. This ensures that each request retrieves the latest data from the server. |
| ConsumerI d | Strin g | Quer y | No | kafka-test | The consumer ID. |

| libaba Cloud | Message | Queue |   | De | veloper Guide·API referenc |
|---|---|---|---|---|---|

| GroupId | Strin g | Quer y | No | 1 | The consumer group ID. |
|---|---|---|---|---|---|
| ClientId | Strin g | Quer y | Yes | test | The client ID. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The ID of the session between the client and the server. This parameter ensures message ordering and maintains the session state. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryConsumerJstackInfo &OnsRegionId=region123 &PreventCache=2342342342 &ClientId=GID_test@@@test
```

Sample successful response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.10.7 QueryConsumerConnection

Queries the connection information for a specified consumer group. The information includes a list of online consumer client connections and their details.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region01 | The identifier of a specific geographic or logical region. |

| PreventCa che | Long | Quer y | Yes | 324234242 | Prevents the browser or system from caching data. This ensures that each request retrieves the latest content. |
|---|---|---|---|---|---|
| GroupId | Strin g | Quer y | Yes | GID-01 | The group ID. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryConsumerConnection &OnsRegionId=region01 &PreventCache=324234242 &GroupId=GID-01 &Common request parameters
```

Sample success response

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.10.8 QueryConsumerAccumulate

Queries the message accumulation for a specified consumer group. The response includes the total number of accumulated messages and the accumulation details for each topic.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region01 | The ID of the region where the Message Service instance is located. |

| PreventCa che | Long | Quer y | Yes | 12312313 | A timestamp used to prevent the browser from caching content. This ensures that each request retrieves the latest data from the server. |
|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | GID-1 | The ID of the consumer group. |
| Detail | Bool ean | Quer y | No | true | Details |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryConsumerAccumulate &OnsRegionId=region01 &PreventCache=12312313 &GroupId=GID-1
```

Sample success response

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.10.9 UpdateConsumerReadableByTopicAndGroup

Updates the read status of a topic for a specified consumer group.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The identifier for a specific region. This distinguishes different service areas or data centers. |
|---|---|---|---|---|---|
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
| GroupId | Strin g | Quer y | Yes | 1 | The ID of the consumer group. |
| ReadEnabl e | Bool ean | Quer y | Yes | true | You can set the message reading switch. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=UpdateConsumerReadableByTopicAndGroup &OnsRegionId=Region001 &Topic=test &GroupId=1 &ReadEnable=true
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.10.10 ResetConsumerOffset

Resets the consumer offset for ApsaraMQ for RocketMQ.

**Request headers**

No special request headers are used in this operation. For more information about common request headers, see Common request parameters.

| Parameter name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |

| PreventCa che | Long | Quer y | Yes | 2342342342 | Prevents the browser or system from caching data. This ensures that each request retrieves the latest content from the server. |
|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
| GroupId | Strin g | Quer y | Yes | 1 | The ID of the consumer group. |
| Topic | Strin g | Quer y | Yes | test | The name of the topic. |
| Type | Integ er | Quer y | No | 1 | The type. |
| ResetTime | Long | Quer y | No | 2022-10-29 01:06:24 | The reset time. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number. |

Sample request

```
http(s)://[Endpoint]/?Action=ResetConsumerOffset &OnsRegionId=region123 &PreventCache=2342342342 &InstanceId=bastionhost-12****** &GroupId=1 &Topic=test
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.10.11 QueryUnitLatestConsumerTime

Queries the latest consumption time for a consumer group on a specific topic and instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | region123 | The logical ID of an area in Message Service. Use this ID to distinguish between different service areas or data centers. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | No | 98765545 | Prevents the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| Topic | Strin g | Quer y | Yes | test | The topic name. |
| GroupId | Strin g | Quer y | Yes | 1 | The consumer group ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the operation or a POP error code. |
| Message | String | success | Additional information about the request. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryUnitLatestConsumerTime &OnsRegionId=region123 &Topic=test &GroupId=1
```

Sample responses

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

##### 3.1.6.11 MQ connector management

###### 3.1.6.11.1 ResumeMqConnector

Resumes a Message Queue (MQ) connector.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Quer y | No | test | The connector name. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID. |
|---|---|---|---|---|---|
| Id | Strin g | Quer y | No | 1 | The connector ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The region identifier specifies the geographic region where an ONS service resource is located. |
| PreventCa che | Long | Quer y | Yes | 24234234 | A timestamp used to prevent the browser from caching the response. This ensures that each request retrieves the latest data from the server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | API status code or POP error code. |
| Message | String | success | Additional information |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=ResumeMqConnector &OnsRegionId=Region001 &PreventCache=24234234
```

Successful response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.11.2 PauseMqConnector

Pauses a Message Queue (MQ) connector.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | The identifier of a specific business group or geographic area. This parameter is used in Message Service to differentiate configurations or resources in different regions. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 324234234242 | Instructs the client or server not to cache the response. This ensures that each request retrieves the latest data. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The HTTP status code or a POP error code. |
| Message | String | success | Additional information about the request. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=PauseMqConnector &OnsRegionId=REGION01 &PreventCache=324234234242
```

Successful response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.11.3 DeleteDeploymentMqConnector

Deletes a deployment connector in Message Queue.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Quer y | No | test | The name of the configuration item. The name must start with a letter and can contain digits, letters, and hyphens (-). The name can be up to 63 characters long. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region12345 | An identifier for a region in an Alibaba Cloud service or Message Queue. It distinguishes between different geographical areas or logical partitions. |

| PreventCa che | Long | Quer y | Yes | 23442342432 | Prevents the browser from caching page content. This ensures that each request retrieves the latest data from the server. |
|---|---|---|---|---|---|

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=DeleteDeploymentMqConnector &OnsRegionId=Region12345 &PreventCache=23442342432
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.11.4 CreateDeploymentMqConnector

Creates a Message Queue deployment connector.

**Request headers**

This operation uses only common request headers. For more information, see the common request parameters document.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Quer y | No | test | The name of the configuration item. The name must start with a letter. It can contain digits, letters, and hyphens (-). The name can be up to 63 characters long. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| Type | Strin g | Quer y | No | 1 | The type of confidential configuration. The following types are supported: Opaque: A user- defined data type. kubernetes.io/tls: A TLS certificate type. |
| SourcePar ams | Strin g | Quer y | No | {"key1": "value1", "key2": 123, "key3": true} | The parameters to pass in the request. These parameters are typically in a key-value format and contain the information required to call the operation. |

| TargetPara ms | Strin g | Quer y | Yes | {"key1":"value1", "key2":"value2"} | The target parameters, specified as a collection of key-value pairs. Each key represents a parameter name, and its value is the specific value or configuration for that parameter. |
|---|---|---|---|---|---|
| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | The region ID of the ONS service. This parameter specifies the geographical region where the resource is located. |
| PreventCa che | Long | Quer y | Yes | 7336353563 | Prevents the client or server from caching the response. This ensures that each request retrieves the latest data directly from the server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the operation or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateDeploymentMqConnector &TargetParams={"key1":"value1", "key2":"value2"} &OnsRegionId=REGION01 &PreventCache=7336353563
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.11.5 DeployDeploymentMqConnector

Deploys a Message Queue (MQ) connector.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Quer y | No | test | The name. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The region identifier for the Message Queue service. It specifies the geographical region where the resource is located. |

| PreventCa che | Long | Quer y | Yes | 234234234 | Prevents the browser from caching page content. This ensures that the latest data is retrieved from the server with each request. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API operation or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=DeployDeploymentMqConnector &OnsRegionId=REGION_001 &PreventCache=234234234
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.11.6 QueryMqConnectorSysResourceName

Generates system resource names, such as error-handling topics and consumer groups, for a Message Queue (MQ) connector task.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Quer y | No | test | Name |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | nanjing | The identifier for a specific region. This parameter is used to distinguish between different service areas or data centers. |
| PreventCa che | Long | Quer y | Yes | 12321313231 | Prevents the browser or system from using cached data. This ensures that each request retrieves the latest content from the source. |

| 77 |   |   | > Document Version: 2026010 |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryMqConnectorSysResourceName &OnsRegionId=nanjing &PreventCache=12321313231
```

Response example

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.11.7 QueryMqConnectorMetricsDetailList

Queries a list of metric details for an MSMQ connector.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The ID of the region. A region is a specific geographic area or data center. |
| PreventCa che | Long | Quer y | Yes | 2323434235242 | A timestamp used to prevent the browser from using cached data. This ensures that each request retrieves the latest content. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The interface status or a POP error code. |

| Message | String | success | Additional information. |
|---|---|---|---|
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryMqConnectorMetricsDetailList &OnsRegionId=REGION_001 &PreventCache=2323434235242
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.11.8 QueryMqConnectorInfoList

Queries a list of Message Queue (MQ) connectors.

**Request header**

This API operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The ID of the region. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 2323432423 | Prevents the browser from caching the content. This ensures that you retrieve the latest data from the server with each request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryMqConnectorInfoList &OnsRegionId=REGION_001 &PreventCache=2323432423
```

Sample successful response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.11.9 QueryMqConnectorDeploymentList

Queries the list of deployments for a Message Queue (MQ) connector.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the common request parameters document.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | The ID of the region where the instance is located. |
| PreventCa che | Long | Quer y | Yes | 32532545543 | Prevents the browser from caching page content. This forces each request to retrieve the latest data from the server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |

| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
|---|---|---|---|
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryMqConnectorDeploymentList &OnsRegionId=REGION01 &PreventCache=32532545543
```

Sample responses

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.11.10 UpdateMqConnectorDeployment

Updates the deployment configuration of a Message Queue (MQ) connector.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Quer y | No | test | The name. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| Type | Strin g | Quer y | No | 1 | The type. |
| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID. |
| Id | Strin g | Quer y | No | 1 | The ID. |
| SourcePar ams | Strin g | Quer y | No | {"key1": "value1", "key2": 123, "key3": true} | A collection of dynamic parameters for the API call. This parameter passes required information for the request, such as filter conditions and configuration details. |
| TargetPara ms | Strin g | Quer y | Yes | {"age": 25, "gender": "male", "location": "Shanghai"} | A collection of target parameters. |
| OnsRegion Id | Strin g | Quer y | Yes | singapore | The logical area identity in Message Service. It is used to distinguish message clusters in different regions. |
| PreventCa che | Long | Quer y | Yes | 23423423 | Prevents the browser from caching page content. This ensures that the latest data is retrieved from the server with each request. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=UpdateMqConnectorDeployment &TargetParams={"age": 25, "gender": "male", "location": "Shanghai"} &OnsRegionId=singapore &PreventCache=23423423
```

Successful response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

##### 3.1.6.12 Router task management

###### 3.1.6.12.1 DeleteCloudRouterTask

Deletes a specified cloud routing task.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION08 | The identifier of a specific business group or geographic area. This parameter is used in Message Service to differentiate configurations or resources in different regions. |
| PreventCa che | Long | Quer y | Yes | 4535354353 | Prevents the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| CloudRout erTaskId | Strin g | Quer y | No | task12345 | The task identifier. This is a unique ID for a routing task, used to track and manage routing operations. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=DeleteCloudRouterTask &OnsRegionId=REGION08 &PreventCache=4535354353
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.12.2 CreateRouterTask

Creates a message routing task that you can use to forward messages across regions or instances.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region ID of the ONS service. This ID specifies the geographical region where the resource is located. |
| PreventCa che | Long | Quer y | Yes | 1213123213 | A timestamp used to prevent the browser from caching page content. This ensures that each request retrieves the latest data from the server. |
| TaskDesc | Strin g | Quer y | No | task-desc | The description of the task. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| TaskKey | Strin g | Quer y | No | taskKey | A unique identifier for the task type. |
| FilterType | Strin g | Quer y | No | Tag | The message filtering type. |
| FilterRule | Strin g | Quer y | No | {"field":"status","operator ":"=","value":"active"} | A rule used to filter for records where the status is "active". |
| FilterPrope rty | Strin g | Quer y | No | NOT | The categorization property used to filter objects. |

| SrcTopic | Strin g | Quer y |   | Yes | /x7aWKW9***/testDataTo DataHub/user/update |   | The source topic that is subscribed to. For example: SrcTopic.1=/x7aWKW9** |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | SrcTopic.1=/x7aWKW9** |   |
|   |   |   |   |   |   |   | **/testDataToDataHub/u |   |   |
|   |   |   |   |   |   |   | ser/update |   |   |
| SrcRegion | Strin g | Quer y |   | Yes | cn-beijing |   | The region where the source instance is located. |   |   |
| SrcInstanc eId | Strin g | Quer y |   | No | 1 |   | The ID of the source project. |   |   |
| DesTopic | Strin g | Quer y |   | Yes | user logon _ |   | The destination topic describes the user identity verification procedure in the system. |   |   |
| DesRegion | Strin g | Quer y |   | Yes | Asia |   | The destination region. For example, the Asia- Pacific region, which includes countries and regions in Asia and around the Pacific Ocean. |   |   |
| DesInstanc eId | Strin g | Quer y |   | No | example123 |   | The ID of the destination instance. An instance ID is a unique identifier for an instance, commonly used in cloud computing or system administration. |   |   |
| OffsetFrom Type | Strin g | Quer y |   | Yes | ExampleValue |   | descriptive information. |   |   |
| OffsetFrom GroupId | Strin g | Quer y |   | No | 1001 |   | The group ID from which to start calculating the offset. |   |   |
| OffsetFrom Timestam p | Long | Quer y |   | No | 1630425600000 |   | The timestamp from which to start calculating the offset. This is a UNIX timestamp in milliseconds. |   |   |

| 89 |   |   | > Document Version: 2026010 |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateRouterTask &OnsRegionId=region123 &PreventCache=1213123213 &SrcTopic=/x7aWKW9***/testDataToDataHub/user/update &SrcRegion=cn-beijing &DesTopic=user_logon &DesRegion=ap-southeast-1 &OffsetFromType=ExampleValue
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.12.3 CreateRouterInnerTask

Creates an internal message routing task.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | ExampleRegion01 | The unique identifier for a region. This ID is used to distinguish different service areas or data centers. |
| TaskDesc | Strin g | Quer y | No | task-desc | The description of the task. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| TaskKey | Strin g | Quer y | No | EX003 | The identifier of the task. |
| FilterType | Strin g | Quer y | No | Tag | The message filtering type. |
| FilterRule | Strin g | Quer y | No | {"field": "status", "value": "active", "operator": "="} | The rule for filtering based on a specified field. The example shows how to filter for records where status is equal to active. |
| FilterPrope rty | Strin g | Quer y | No | Date | Used to filter based on user roles, such as administrator or regular user. |

| SrcTopic | Strin g | Quer y |   |   |   |   | The source topic that is subscribed to. For example: SrcTopic.1=/x7aWKW9** |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | SrcTopic.1=/x7aWKW9** |   |
|   |   |   |   |   |   |   | **/testDataToDataHub/u |   |   |
|   |   |   | Quer y | Yes | /x7aWKW9***/testDataTo DataHub/user/update |   |   |   |   |
|   |   |   |   |   |   |   | ser/update |   |   |
| SrcRegion | Strin g | Quer y |   | Yes | cn-beijing |   | The region where the source instance is located. |   |   |
| SrcInstanc eId | Strin g | Quer y |   | No | 1 |   | The ID of the source project. |   |   |
| DesTopic | Strin g | Quer y |   | Yes | UserLogon |   | Describes the process of user identity verification in the system. |   |   |
| DesRegion | Strin g | Quer y |   | Yes | OC |   | The destination region for a global user base. |   |   |
| DesInstanc eId | Strin g | Quer y |   | No | 1234567890 |   | The unique identifier of the destination instance. It specifies the instance for the operation. |   |   |
| OffsetFrom Type | Strin g | Quer y |   | No | 256 |   | The offset is calculated from the end of the data. |   |   |
| OffsetFrom GroupId | Strin g | Quer y |   | No | 1001 |   | The offset is calculated starting from the element with the group ID 1001. |   |   |
| OffsetFrom Timestam p | Long | Quer y |   | No | 1630435200000 |   | The offset from this timestamp. It is typically used to mark the start of a time point. |   |   |

| NeedSrcIn stance | Bool ean | Quer y | Yes | true | Specifies whether a source instance is required for the current operation or task. For example, you must specify a source instance when you copy or migrate data. |
|---|---|---|---|---|---|
| NeedDesIn stance | Bool ean | Quer y | Yes | true | You should periodically back up important data from the server to a secure location to prevent data loss or corruption. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=CreateRouterInnerTask &OnsRegionId=ExampleRegion01 &SrcTopic=/x7aWKW9***/testDataToDataHub/user/update &SrcRegion=cn-beijing &DesTopic=UserLogon &DesRegion=OC &NeedSrcInstance=true &NeedDesInstance=true
```

Successful response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.12.4 CreateCloudRouterTask

Creates a cross-cloud routing task for cross-cloud communication between message queues.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SrcCloudId | Strin g | Quer y | Yes | 1001 | The unique identifier for the source cloud platform. This ID distinguishes different cloud service providers or cloud instances. |
| DesCloudI d | Strin g | Quer y | Yes | CLD123456 | The unique identifier for the destination cloud platform. This ID distinguishes different cloud service providers or cloud environments. |

| RegionId | Strin g | Quer y |   | No | cn-hangzhou |   | The region ID. |   |   |
|---|---|---|---|---|---|---|---|---|---|
| OnsRegion Id | Strin g | Quer y |   | Yes | REGION001 |   | A specific identifier for a region. This ID distinguishes different regions or data centers. |   |   |
| PreventCa che | Long | Quer y |   | Yes | 33333332223 |   | A timestamp or random number used to prevent the browser or system from using cached data. This ensures that each request retrieves the latest content. |   |   |
| TaskDesc | Strin g | Quer y |   | No | task-desc |   | The description of the task. The description must be 2 to 256 characters long and cannot start with http:// or https://. |   |   |
| TaskKey | Strin g | Quer y |   | No | task003 |   | This is example task 003. |   |   |
| FilterType | Strin g | Quer y |   | No | Tag |   | The message filtering type. |   |   |
| FilterRule | Strin g | Quer y |   | No | {"field": "category", "operator": "!=", "value": "expired"} |   | The rule for filtering messages. |   |   |
| FilterPrope rty | Strin g | Quer y |   | No | Tag |   | The property to use for filtering. |   |   |
| SrcTopic | Strin g | Quer y |   | Yes | /x7aWKW9***/testDataTo DataHub/user/update |   | The source topic that is subscribed to. For example: SrcTopic.1=/x7aWKW9** |   |   |
|   |   |   |   |   |   |   |   | SrcTopic.1=/x7aWKW9** |   |
|   |   |   |   |   |   |   | **/testDataToDataHub/u |   |   |
|   |   |   |   |   |   |   | ser/update |   |   |
| SrcRegion | Strin g | Quer y |   | Yes | cn-beijing |   | The region of the source instance. |   |   |
| SrcInstanc eId | Strin g | Quer y |   | No | 1 |   | The ID of the source instance. |   |   |

| DesTopic | Strin g | Quer y | Yes | UserLogon | This topic describes the identity verification procedure for users in the system. |
|---|---|---|---|---|---|
| DesRegion | Strin g | Quer y | Yes | SG | This represents the Singapore region. |
| DesInstanc eId | Strin g | Quer y | No | inst123456 | The unique identifier of the destination instance. |
| OffsetFrom Type | Strin g | Quer y | Yes | ExampleValue | Indicates a type identity offset by 500 units from the base position. |
| OffsetFrom GroupId | Strin g | Quer y | No | 1001 | The group ID from which to start calculating the offset. This parameter is used when you specify a group offset for message consumption. |
| OffsetFrom Timestam p | Long | Quer y | No | 1630425600000 | The offset from the timestamp, which marks a specific point in time. |
| NeedSrcIn stance | Bool ean | Quer y | No | true | Specifies whether a source instance is required for the operation. This is often used for data migration, replication, or conditional logic. |
| NeedDesIn stance | Bool ean | Quer y | No | true | An instance object implements user identity verification and system access control. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code or a service error code. |
| Message | String | success | Additional information returned. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateCloudRouterTask &SrcCloudId=1001 &SrcRegion=cn-beijing &SrcTopic=/x7aWKW9***/testDataToDataHub/user/update &DesCloudId=CLD123456 &DesRegion=SG &DesTopic=user_logon &OnsRegionId=REGION001 &OffsetFromType=SampleValue &PreventCache=
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.12.5 QueryCloudRouterTaskStats

Queries the performance statistics of a cloud router task, such as Transactions Per Second (TPS), message discrepancies, and latency.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | The unique identifier for a region. This parameter distinguishes between different geographical or logical regions. |
| PreventCa che | Long | Quer y | Yes | true | Prevents the browser from caching page content to ensure that the latest data is retrieved from the server with each request. |
| CloudRout erTaskId | Strin g | Quer y | No | 123456 | The ID of a specific cloud router task. This ID uniquely tracks and manages the task. |
| FromDate | Long | Quer y | Yes | 2020-03-06T02:58:16Z | The start time. |
| ToDate | Long | Quer y | Yes | 1560134212326 | The end time. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The ID of a session between the client and the server. This ID is used for sequential message processing and session state maintenance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryCloudRouterTaskStats &OnsRegionId=REGION01 &PreventCache=true &FromDate=2020-03-06T02:58:16Z &ToDate=1560134212326
```

Response example

```json
 "Total":1,
 "Data":{},
```

###### 3.1.6.12.6 QueryCloudRouterTask

Queries the details of a specified cloud router task.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| 99 |   |   |   | > D | ocument Version: 2026010 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The identifier of a specific business group or geographic area. This parameter is used in Message Service to differentiate configurations or resources in different regions. |
| PreventCa che | Long | Quer y | Yes | true | Prevents the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| CloudRout erTaskId | Strin g | Quer y | No | TR20231001120000 | The ID of the cloud router task. This ID is used to uniquely track and manage the lifecycle and operation records for the task. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID of a session or connection. This ID is used to track and manage session states in Message Service. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |

| Code | Integer | 200 | The status code of the API or the POP error code. |
|---|---|---|---|
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryCloudRouterTask &OnsRegionId=region123 &PreventCache=true &Common request parameters
```

Response example

```json
 "Total":1,
 "Data":{},
```

###### 3.1.6.12.7 QueryCloudRouterItems

Queries the items of a cloud router task.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The unique ID that identifies a specific area in the ONS service. This ID is used to differentiate between service areas or instances. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 343532334 | Instructs the client or server not to cache the response. This ensures that each request retrieves the latest data. |
| CloudId | Strin g | Quer y | No | ffe1********6d6d | The cloud instance ID. |
| QueryRegi onId | Strin g | Quer y | No | cn-hangzhou | The ID of the region where the VPC associated with the zone is located. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID that identifies a session between the client and the server when you use Alibaba Cloud Open Notification Service (ONS). This ID is typically generated when the client is initialized or connects to the server. It is used for context tracking and session management during message communication. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The status code of the API operation or the POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryCloudRouterItems &OnsRegionId=Region001 &PreventCache=343532334 &Common request parameters
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.12.8 PageQueryCloudRouterTask

Performs a paged query to retrieve a list of cloud routing tasks.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
|---|---|---|---|---|---|
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The identifier of a specific business group or geographic area. This parameter is used in Message Service to differentiate configurations or resources in different regions. |
| PreventCa che | Long | Quer y | Yes | 3423424324 | A timestamp used to prevent browser caching. This ensures that each request retrieves the latest data. |
| CurrentPa ge | Integ er | Quer y | Yes | 1 | When conducting pagination queries, the page number of the current page. |
| PageSize | Integ er | Quer y | Yes | 10 | The number of entries to return on each page. |
| TaskKey | Strin g | Quer y | No | key1 | The task identifier. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The session ID. It identifies the connection between the client and the server to ensure message ordering and maintain state. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=PageQueryCloudRouterTask &OnsRegionId=region123 &PreventCache=3423424324 &CurrentPage=1 &PageSize=10
```

Sample successful response

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.12.9 DeleteRouterTask

Deletes the specified routing task.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
|---|---|---|---|---|---|
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The unique identifier for a specific region. This identifier is used to distinguish between different geographical or logical regions. |
| PreventCa che | Long | Quer y | Yes | 234234234 | A value used to prevent the browser or system from caching data. This ensures that each request retrieves the latest content. |
| TaskId | Strin g | Quer y | No | 123456 | The task ID. |
| TaskKey | Strin g | Quer y | No | common | The custom string identifier of the Router task, which can be used as an alternative to TaskId to query, start, stop, or delete cross- region message routing tasks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |

| Message | String | success | Additional information. |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number. |

Request example

```
http(s)://[Endpoint]/?Action=DeleteRouterTask &OnsRegionId=Region001 &PreventCache=234234234
```

Successful response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.12.10 DeleteRouterInnerTask

Deletes the specified task.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The unique ID that identifies a specific geographic area in Message Service. This ID is often used for region- based partition configurations in Message Service. |
|---|---|---|---|---|---|
| TaskId | Long | Quer y | Yes | 123456 | The task ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API call or the POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number. |

Request example

```
http(s)://[Endpoint]/?Action=DeleteRouterInnerTask &OnsRegionId=Region001 &TaskId=123456
```

Successful response example

```json
 "Total":1,
 "Data":"[{}]",
```

###### 3.1.6.12.11 QueryRouterTask

Queries the status and details of a message routing task.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | The identifier of a specific business group or geographic area. This parameter is used in Message Service to differentiate configurations or resources in different regions. |
| PreventCa che | Long | Quer y | Yes | 78766544 | Prevents the browser from caching page content. This ensures that the latest data is retrieved from the secondary server for each request. |
| TaskId | Strin g | Quer y | No | 123456 | The task ID. |
| TaskKey | Strin g | Quer y | No | AUTHENTICATE USER _ | The task key. |

| OnsSessio nId | Strin g | Quer y | No | abc123xyz | When you use Alibaba Cloud Open Notification Service (ONS), this parameter specifies the unique ID of a client session. This ID ensures the integrity and contextual association of message communication. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryRouterTask &OnsRegionId=REGION01 &PreventCache=78766544
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.12.12 QueryRouterStat

Queries the performance statistics for message routing.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | EU01 | The unique identifier of a region. This parameter is used to distinguish between different geographical or logical regions. |
| PreventCa che | Long | Quer y | Yes | 978654545 | Prevents the browser or server from caching data. This ensures that each request retrieves the latest content. |
| TaskId | Strin g | Quer y | Yes | 123456 | The task ID. |

| libaba Cloud | Message | Queue |   | De | veloper Guide·API referenc |
|---|---|---|---|---|---|

| FromDate | Long | Quer y | Yes | 1560134212326 | The start time. |
|---|---|---|---|---|---|
| ToDate | Long | Quer y | Yes | 1560134212326 | The end time. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID that identifies a client session when you use Alibaba Cloud Open Notification Service (ONS). This ID associates sent and received messages within the same session. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code for the API call or a POP error code. |
| Message | String | success | Additional information |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryRouterStat &OnsRegionId=EU01 &PreventCache=978654545 &TaskId=123456 &FromDate=1560134212326 &ToDate=1560134212326
```

Response examples

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.12.13 QueryRouterInnerTask

Queries details of an internal message routing task, such as its status, source, and destination.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | The identifier of a specific business group or geographic area. This parameter is used in Message Service to differentiate configurations or resources in different regions. |
|---|---|---|---|---|---|
| TaskId | Long | Quer y | Yes | 123456 | The task ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API operation status or a POP error code. |
| Message | String | success | Additional information |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryRouterInnerTask &OnsRegionId=REGION01 &TaskId=123456
```

Sample responses

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.12.14 QueryRouterInnerStat

Queries the runtime statistics of a message routing task, such as Transactions Per Second (TPS) and latency.

**Request header**

This API operation uses only common request headers. For more information, see the Common request parameters document.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | hangzhou | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
| PreventCa che | Long | Quer y | Yes | 3423424 | Prevents the browser from caching content. This ensures that each request retrieves the latest data from the server. |

| TaskId | Strin g | Quer y | Yes | 123456 | The task ID. |
|---|---|---|---|---|---|
| FromDate | Long | Quer y | Yes | 2020-03-06T02:58:16Z | The start time. |
| ToDate | Long | Quer y | Yes | 2020-03-17T02:26:28Z | The end time. |
| OnsSessio nId | Strin g | Quer y | No | ABC123XYZ789 | A unique ID that identifies a client session in the ApsaraMQ for RocketMQ service. It is used to maintain the connection status of a producer or consumer. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=QueryRouterInnerStat &OnsRegionId=hangzhou &PreventCache=3423424 &TaskId=123456 &FromDate=2020-03-06T02:58:16Z &ToDate=2020-03-17T02:26:28Z
```

Response example

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.12.15 UpdateRouterFilterRule

Updates a filter rule for message routing.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The ID of the region. |

| OnsRegion Id | Strin g | Quer y | Yes | hangzhou | The identifier of a specific business group or geographic area. This parameter is used in Message Service to differentiate configurations or resources in different regions. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 23342424234 | A parameter used to instruct the system or browser not to cache the current request. This ensures that each request retrieves the latest content directly from the server. |
| TaskId | Strin g | Quer y | No | 123456 | The ID of the task. |
| TaskKey | Strin g | Quer y | No | taskKey | A unique identifier. |
| FilterType | Strin g | Quer y | No | Tag | The type of message filtering. |
| FilterRule | Strin g | Quer y | Yes | {"field":"status","operator ":"=","value":"active"} | The filter rule. |
| FilterPrope rty | Strin g | Quer y | No | Date | The condition for filtering fields. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code or a POP error code. |

| Message | String | success | Additional information. |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=UpdateRouterFilterRule &OnsRegionId=hangzhou &PreventCache=23342424234 &FilterRule={"field":"status","operator":"=","value":"active"}
```

Sample responses

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.12.16 UpdateCloudRouterTask

Updates the configuration of a cloud router task in ApsaraMQ for RocketMQ.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | hangzhou | The identifier for a specific geographic or logical region. |
| PreventCa che | Long | Quer y | Yes | 453453535 | Prevents the browser from caching page content. This ensures that each request retrieves the latest data from the server. |
| CloudRout erTaskId | Strin g | Quer y | No | TR20231001120000 | The unique identifier of the cloud router task. |
| TaskDesc | Strin g | Quer y | No | task-desc | The task description. |
| FilterType | Strin g | Quer y | No | Tag | The message filtering type. |
| FilterRule | Strin g | Quer y | Yes | {"field":"status","operator ":"=","value":"active"} | The filter rule. |
| FilterPrope rty | Strin g | Quer y | No | Status | Filters the role field in the query results, such as administrator or regular user. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The status code of the API operation or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The data returned. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=UpdateCloudRouterTask &OnsRegionId=hangzhou &PreventCache=453453535 &FilterRule={"field":"status","operator":"=","value":"active"}
```

Sample successful response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.12.17 StopRouterTask

Stops a message routing task.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The identifier of a specific business group or geographic area. This parameter is used in Message Service to differentiate configurations or resources in different regions. |
| PreventCa che | Long | Quer y | Yes | 342342342 | Prevents the browser from caching page content. This ensures that the latest data is retrieved from the server for each request. |
| TaskId | Strin g | Quer y | No | 123456 | The task ID. |
| TaskKey | Strin g | Quer y | No | EX001 | The task key. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |

| Code | Integer | 200 | The status code of the operation or a POP error code. |
|---|---|---|---|
| Message | String | success | Additional information. |
| Data | String | [{}] | The response data. |
| Total | Long | 1 | The total number. |

Request example

```
http(s)://[Endpoint]/?Action=StopRouterTask &OnsRegionId=region123 &PreventCache=342342342
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.12.18 StopCloudRouterTask

Stops a specified cloud router task.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | shenzhen | The ID of the region where the ONS service is deployed. This parameter specifies the geographical location of the resource. |
| PreventCa che | Long | Quer y | Yes | 234234242 | A timestamp used to prevent the client or server from caching the response. This ensures that each request retrieves the latest content. |
| CloudRout erTaskId | Strin g | Quer y | No | task12345 | The unique ID of the cloud router task. This ID is used to track and manage a specific routing task. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=StopCloudRouterTask &OnsRegionId=shenzhen &PreventCache=234234242
```

Sample responses

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.12.19 StartRouterTask

Starts a message routing task.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The ID of a specific geographic or logical region. This ID distinguishes different data centers or areas where the endpoint is deployed. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | Yes | 4242342 | Prevents the browser or server from using cached data. This ensures that each request retrieves the latest content. |
| TaskId | Strin g | Quer y | No | 123456 | The task ID. |
| TaskKey | Strin g | Quer y | No | EX003 | The task key. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the operation or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Example request

```
http(s)://[Endpoint]/?Action=StartRouterTask &OnsRegionId=Region001 &PreventCache=4242342
```

Example of a successful response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.12.20 StartRouterInnerTask

Starts an internal routing task in ApsaraMQ for RocketMQ.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |

| TaskId | Long | Quer y | No | 123456 | The task ID. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=StartRouterInnerTask &OnsRegionId=REGION01
```

Sample response

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.12.21 StartCloudRouterTask

Starts a cloud routing task in ApsaraMQ for RocketMQ.

**Request headers**

This operation uses only common request headers. For more information, see Common parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The ID of the region. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The identifier of a specific business group or geographic area. This parameter is used in Message Service to differentiate configurations or resources in different regions. |
| PreventCa che | Long | Quer y | Yes | 3242342342 | A parameter that prevents the browser from caching page content. This ensures that each request retrieves the latest data from the server. |
| CloudRout erTaskId | Strin g | Quer y | No | task12345 | The unique ID of a routing configuration update task. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
|---|---|---|---|
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number. |

Sample request

```
http(s)://[Endpoint]/?Action=StartCloudRouterTask &OnsRegionId=Region001 &PreventCache=3242342342
```

Sample responses

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.12.22 SearchRouterTask

This API operation searches for message routing tasks.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see the Common request parameters document.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region ID for the Open Notification Service (ONS) service. This parameter specifies the geographical region where the resource is located. |
| PreventCa che | Long | Quer y | Yes | 234234234 | Indicates that the client or server must not cache the response. This ensures that each request retrieves the latest data directly from the server. |
| SrcTopic | Strin g | Quer y | No | test | The source topic that is subscribed to. |
| SrcRegion | Strin g | Quer y | No | cn-beijing | The region where the source instance is located. |
| SrcInstanc eId | Strin g | Quer y | No | 1 | The ID of the source instance. |
| DesTopic | Strin g | Quer y | No | user logon _ | The destination topic that is subscribed to. |
| DesRegion | Strin g | Quer y | No | OCEANIA | The region where the destination instance is located. |

| DesInstanc eId | Strin g | Quer y | No | example123 | The unique ID of the destination instance. This parameter specifies the instance on which to perform the operation. |
|---|---|---|---|---|---|
| PageNo | Integ er | Quer y | Yes | 1 | The page number. |
| PageSize | Integ er | Quer y | Yes | 10 | The number of entries to return on each page for a paged query. Default value: 10. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID of a client session in the ONS service. This ID distinguishes different message session connections. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API operation status or a POP error code. |
| Message | String | success | Additional information. |
| Total | Long | 1 | The total number of entries. |

Request example

```
http(s)://[Endpoint]/?Action=SearchRouterTask &OnsRegionId=region123 &PreventCache=234234234 &PageNo=1 &PageSize=10
```

Response example

```json
 "Total":1,
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.12.23 AddRouterInnerConfig

Adds an internal routing configuration to ApsaraMQ for RocketMQ.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | The unique ID of a region, such as East China or North China. This ID distinguishes deployments in different geographical areas within Message Service. |
|---|---|---|---|---|---|
| OnsAddr | Strin g | Quer y | Yes | 192.168.1.100:9876 | The IP address and port number of a running Open Notification Service (ONS) server. This is used for communication in Message Service. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or the POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=AddRouterInnerConfig &OnsRegionId=REGION01 &OnsAddr=192.168.1.100:9876
```

Sample success response

```json
 "Total":1,
 "Data":"[{}]",
```

##### 3.1.6.13 VPC management

###### 3.1.6.13.1 CreateVpcTunnelInstanceSingleTunnel

Create an API interface for a single VPC tunnel instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region3 | The identifier of a specific business group or geographic area. This parameter is used in Message Service to differentiate configurations or resources in different regions. |
| PreventCa che | Long | Quer y | Yes | 3223424234 | Prevents the browser or server from caching the response. This ensures that each request returns the latest data. |
| VpcId | Strin g | Quer y | Yes | vpc- 4uftp58qtzn7t663xajtj | The VPC ID. |
| VpcName | Strin g | Quer y | Yes | Vpc-1 | The VPC name. |

| VSwitchId | Strin g | Quer y | Yes | vsw- bp1s5fnvk4gn2tws0**** | The vSwitch ID. |
|---|---|---|---|---|---|
| Cluster | Strin g | Quer y | Yes | slbCluster-A-20231203- 005b | The cluster name. |
| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API operation or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateVpcTunnelInstanceSingleTunnel &OnsRegionId=region3 &PreventCache=3223424234 &VpcId=vpc-4uftp58qtzn7t663xajtj &VpcName=Vpc-1 &VSwitchId=vsw-bp1s5fnvk4gn2tws0**** &Cluster=slbCluster-A-20231203-005b &InstanceId=bastionhost-12******
```

Sample response

```json
 "Data":"[{}]",
```

###### 3.1.6.13.2 DeleteVpcTunnelInstanceSingleTunnel

Deletes the specified VPC tunnel instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION01 | The identifier of a specific business group or geographic area. This parameter is used in Message Service to differentiate configurations or resources in different regions. |
| PreventCa che | Long | Quer y | Yes | 23423424 | A timestamp used to prevent browser caching. This ensures that each request retrieves the latest data from the server. |
| VpcId | Strin g | Quer y | Yes | vpc- 4uftp58qtzn7t663xajtj | The VPC ID. |
| VSwitchId | Strin g | Quer y | No | vsw- bp1s5fnvk4gn2tws0**** | The vSwitch ID. |
| Cluster | Strin g | Quer y | Yes | slbCluster-A-20231203- 005b | The cluster name. |

| InstanceId | Strin g | Quer y | Yes | bastionhost-12****** | The instance ID. |
|---|---|---|---|---|---|

| Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status code of the API call or a POP error code. |
| Message | String | success | Additional information |
| Data | String | [{}] | The data returned. |

Request example

```
http(s)://[Endpoint]/?Action=DeleteVpcTunnelInstanceSingleTunnel &OnsRegionId=REGION01 &PreventCache=23423424 &VpcId=vpc-4uftp58qtzn7t663xajtj &Cluster=slbCluster-A-20231203-005b &InstanceId=bastionhost-12******
```

Example of a successful response

```json
 "Data":"[{}]",
```

###### 3.1.6.13.3 QueryVpcTunnelTunnelSwitch

The API that queries the status of the VPC tunnel switch.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
| PreventCa che | Long | Quer y | Yes | 342342342 | Prevents the browser or server from using cached data. This ensures that each request retrieves the latest content. |
| VSwitchId | Strin g | Quer y | No | vsw- bp1s5fnvk4gn2tws0**** | The vSwitch ID. |
| Cluster | Strin g | Quer y | Yes | slbCluster-A-20231203- 005b | The cluster name. |
| TunnelTyp e | Strin g | Quer y | Yes | Any tunnel _ | The tunnel type. |
| Force | Bool ean | Quer y | Yes | false | Specifies whether to force the operation. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |
| Data | String | [{}] | The returned data. |

Request example

```
http(s)://[Endpoint]/?Action=QueryVpcTunnelTunnelSwitch &OnsRegionId=Region001 &PreventCache=342342342 &Cluster=slbCluster-A-20231203-005b &TunnelType=Any_tunnel &Force=false
```

Successful response example

```json
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.13.4 QueryVpcTunnelInstanceSingleTunnelList

Queries a list of individual tunnels in a VPC tunnel instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The identifier for a specific region. It distinguishes different geographical or logical areas. |
| PreventCa che | Long | Quer y | Yes | 2342342 | Prevents the browser or server from using cached data. This ensures that each request returns the latest content. |
| VpcId | Strin g | Quer y | No | vpc- 4uftp58qtzn7t663xajtj | The VPC ID. |
| VSwitchId | Strin g | Quer y | No | vsw- bp1s5fnvk4gn2tws0**** | The vSwitch ID. |
| Cluster | Strin g | Quer y | Yes | slbCluster-A-20231203- 005b | The cluster name. |
| InstanceId | Strin g | Quer y | No | bastionhost-12****** | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | [{}] | The returned data. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The status of the API operation or a POP error code. |
| Message | String | success | Additional information. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryVpcTunnelInstanceSingleTunnelList &OnsRegionId=region123 &PreventCache=2342342 &Cluster=slbCluster-A-20231203-005b
```

Sample response

```json
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

##### 3.1.6.14 Region management

###### 3.1.6.14.1 QueryMetaData

Queries system metadata.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | region123 | The region identifier of the Ons service, which specifies the geographic region where the resource is located. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | A unique ID that identifies a client session in the Message Queue service. It is used to track and manage the sending and receiving of messages. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryMetaData &OnsRegionId=region123
```

Sample success response

```json
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data /> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.14.2 QueryCommonRegionData

Queries common data for a specified region. This data includes configuration information, such as whether the region supports creating shared instances.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | Region001 | The region ID for the ONS service. This specifies the geographic region where the resource is located. |

| PreventCa che | Long | Quer y | Yes | 21312313 | Prevents the browser or system from caching data. This ensures that each request retrieves the latest content. |
|---|---|---|---|---|---|
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID of a client session in Open Notification Service (ONS). It distinguishes different message session connections. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | Map | {} | Additional information. |
| Data | Map | {} | The returned data. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryCommonRegionData &OnsRegionId=Region001 &PreventCache=21312313
```

Sample success response

```json
 "Message":{},
 "Data":{},
```

###### 3.1.6.14.3 QueryRegionList

Query the list of regions supported by the ApsaraMQ for RocketMQ.

**Request headers**

This operation does not have special request headers. For more information about common request headers, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The identifier of a specific business group or geographic area. This parameter is used in Message Service to differentiate configurations or resources in different regions. |
| PreventCa che | Long | Quer y | Yes | 86676756456465 | Prevents the browser from caching resources and forces each request to retrieve the latest content from the server. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The unique ID that identifies a client session in Message Service. It is used to track and manage the sending and receiving of messages. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| Data | String | [{}] | The returned data. |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status or a POP error code. |
| Message | String | success | Additional information. |

Request example

```
http(s)://[Endpoint]/?Action=QueryRegionList &OnsRegionId=REGION_001 &PreventCache=86676756456465
```

Response example

```json
 "Data":"[{}]",
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data>[{}]</Data> <Code>200</Code> <Success>true</Success>
```

###### 3.1.6.14.4 QueryRegionConsoleUrlList

Retrieves a list of console URLs for each region. You can use these URLs to navigate to the console in a specific region.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| OnsRegion Id | Strin g | Quer y | Yes | REGION 001 _ | The identifier of a specific business group or geographic area. This parameter is used in Message Service to differentiate configurations or resources in different regions. |
| PreventCa che | Long | Quer y | Yes | true | Prevents the browser from caching content. This ensures that each request retrieves the latest data from the server. |
| OnsSessio nId | Strin g | Quer y | No | abc123xyz | The session ID used to track and manage the user's session status in Open Notification Service (ONS). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The API status code or a POP error code. |

| Message | String | success | Additional information. |
|---|---|---|---|
| Data | Map | {} | The returned data. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryRegionConsoleUrlList &OnsRegionId=REGION_001 &PreventCache=true
```

Sample success response

```json
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Data /> <Code>200</Code> <Success>true</Success>
```

##### 3.1.6.15 UnitResetTask management

###### 3.1.6.15.1 CreateUnitResetTask

Creates a reset task for a specified topic and consumer group.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|

| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
|---|---|---|---|---|---|
| OnsRegion Id | Strin g | Quer y | Yes | region1 | The identifier of a specific business group or geographic area. This parameter is used in Message Service to differentiate configurations or resources in different regions. |
| PreventCa che | Long | Quer y | Yes | 24232424324 | Prevents the client or server from caching the response. This ensures that each request returns the latest data. |
| InstanceId | Strin g | Quer y | No | ccc-test | The instance ID. |
| GroupId | Strin g | Quer y | Yes | GID-1 | The application group ID. |
| Topic | Strin g | Quer y | Yes | 123456 | The topic name. |
| UnitRuleVe rsion | Long | Quer y | Yes | 3.0.0 | The upgraded rule expression syntax now supports more complex combinations of conditions. |
| OffsetTime stamp | Long | Quer y | Yes | 1696845600 | The UNIX timestamp. |
| AllUnitInfo | Strin g | Quer y | Yes | {"unit id": "U001", _ "name": "infantry", "attack": 10, "defense": 5, "health": 50} | Information about all unit types. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code or a POP error code. |
| Message | String | success | Additional information |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateUnitResetTask &OnsRegionId=region1 &PreventCache=24232424324 &GroupId=GID-1 &Topic=123456 &UnitRuleVersion=3.0.0 &OffsetTimestamp=1696845600 &AllUnitInfo={"unit_id": "U001", "name": "infantry", "attack": 10, "defense": 5, "healt h": 50}
```

Sample response

###### 3.1.6.15.2 QueryUnitResetTask

Queries the execution status and details of a specified unit reset task.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

| OnsRegion Id | Strin g | Quer y | Yes | region1 | The identifier of the Message Service area. This is used to distinguish different service deployment areas. |
|---|---|---|---|---|---|
| PreventCa che | Long | Quer y | No | true | Enables the cache prevention feature. This ensures that each request retrieves the latest data from the server and avoids using the local cache. |
| TaskId | Strin g | Quer y | Yes | 123456 | The task ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | The status of the response. true: The request was successful. false: The request failed. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| Data | Map | {} | The returned data. |
| Total | Long | 1 | The total number of entries. |

Sample request

```
http(s)://[Endpoint]/?Action=QueryUnitResetTask &OnsRegionId=region1 &TaskId=123456 &Common request parameters
```

Sample response

```json
 "Total":1,
 "Data":{},
```

`XML` format

```xml
<RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId> <Message>success</Message> <Total>1</Total> <Data /> <Code>200</Code> <Success>true</Success>
```

## 4 SDK reference

### 4.1 RocketMQ_SDK

#### 4.1.1 Overview

ApsaraMQ for RocketMQ is an important component of distributed systems. This service supports asynchronous communication for application decoupling and load shifting, and provides high performance, high availability, high scalability, and eventual consistency. This document describes how to manage a message queuing service between RocketMQ applications and the message queuing server during data transmission. This document provides the specifications that the service complies with and the common API operations that are used to manage the service. This document is suitable for scenarios in which messages are transmitted over the TCP protocol by using ApsaraMQ for RocketMQ SDK for Java.

#### 4.1.2 Messaging model

ApsaraMQ for RocketMQ supports the publish-subscribe model. A producer can publish a message to a broker, and multiple consumers can subscribe to a topic on the broker. The following figure shows the messaging model. Figure 1. Publish-subscribe model

#### 4.1.3 Updates

This topic describes the updates of ApsaraMQ for RocketMQ from V3.8.0 to V3.18.3 to help you get started with the updated version.

**Optimization of resource isolation by instance**

ApsaraMQ for RocketMQ provides instances for multi-tenancy isolation. Each user can purchase multiple instances and logically isolate them from each other. To ensure the compatibility with the existing resources of existing users, ApsaraMQ for RocketMQ provides the following types of instances and namespaces: Default instances, which are compatible with the existing resources of existing users This type of instance has no separate namespace. Resource names must be globally unique within and across all instances. By default, an instance without a namespace is automatically generated for the existing resources of each existing user. If no existing resources are available, you can create at most one instance without a namespace. You can configure the endpoint, which can be obtained from the **Instances** page in the ApsaraMQ for RocketMQ console.

```
// Recommended configuration: properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxxx"); // Compatible configuration, which is not recommended. We recommend that you update this configuration to the recommended configuration: properties.put(PropertyKeyConst.ONSAddr, "xxxx");
```

New instances A new instance has a separate namespace. Resource names must be unique within an instance but can be the same across different instances. You can configure the endpoint, which can be obtained from the **Instances** page in the ApsaraMQ for RocketMQ console.

```
// Recommended configuration: properties.put(PropertyKeyConst.NAMESRV_ADDR, "xxx");
```

A RocketMQ client must be updated to the following latest versions for different programming languages: Java: V1.8.7.1.Final C and C++: V2.0.0 .NET: V1.1.3

**Optimization of resource application**

Previously, ApsaraMQ for RocketMQ resources consisted of topics, producer IDs, and consumer IDs. Each two of the resources have a many-to-many relationship, which was difficult to comprehend. Each time you created a topic, you must associate the topic with a producer ID and a consumer ID. This process was too complex for medium- and large-sized enterprise customers. To optimize user experience and help new users get started, the resource application process has been simplified. The resource application process has been optimized in the following aspects: Topic management, which is unchanged You need to apply for a topic. A topic is used to classify messages. It is the primary classifier. You do not need to apply for a producer ID. Producer IDs and consumer IDs are integrated into group IDs. In the ApsaraMQ for RocketMQ console, the Producers module has been removed. The Producers and Consumers modules have been integrated into the Groups module. You do not need to associate a producer ID or consumer ID with a topic. Instead, you need only to apply for a group ID and associate it with a topic in the code. Compatibility: The list of producer IDs is no longer displayed. This does not affect the current services. The consumer IDs that start with CID- or CID_ and that you have applied for can still be used and can be set in the **PropertyKeyConst.ConsumerId** or
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

#### 4.1.4 Transport protocol and character encoding

**encoding**

The underlying layer of ApsaraMQ for RocketMQ SDKs provides services based on the TCP protocol. User requests and responses in ApsaraMQ for RocketMQ use UTF-8 character encoding.

**Transport layer encryption**

ApsaraMQ for RocketMQ instances support Transport Layer Security (TLS) 1.2 and later. You can configure parameters in an SDK to determine whether to use encrypted transport layer links.
**Configuration method**: When you start the client program, set the JVM attributes to
determine whether to use the encrypted transport layer link. The startup command is **java -**
**Dtls.enable=true**. By default, TLS links are disabled. If you set the value to true, encrypted
transport layer links are enabled.

#### 4.1.5 Common classes and methods

##### 4.1.5.1 PropertyKeyConst

The following table lists the main fields of this class.

| Parameter | Type | Default value | Description |
|---|---|---|---|
| AccessKey | String | - | The AccessKey ID that you created in the Apsara Uni-manager Management Console for identity verification. |
| SecretKey | String | - | The AccessKey secret that you created in the Apsara Uni-manager Management Console for identity verification. |
| OnsChannel | String | ALIYUN | The user channel. Valid values: ALIYUN and CLOUD. ALIYUN stands for Apsara Stack. CLOUD stands for CloudTmall. |
| NAMESRV ADDR _ | String | - | The TCP endpoint that is used to connect to the ApsaraMQ for RocketMQ instance. |
| GROUP ID _ | String | - | The group ID that you created in the ApsaraMQ for RocketMQ console. This group ID identifies a type of producers or consumers. |
| MessageModel | String | CLUSTERING | The consumption mode for the consumer instance. Valid values: CLUSTERING and BROADCASTING. |
| ConsumeThreadNums | String | 64 | The number of consumer threads. |
| MaxReconsumeTimes | String | 16 | The maximum number of delivery retries that can be performed when a message fails to be consumed. |

| ConsumeTimeout | String | 15 | The timeout period for consuming each message. If the time for consuming a message exceeds the specified timeout period, the message fails to be consumed and is redelivered after a retry interval. Configure an appropriate value for each type of application. Unit: minute. |
|---|---|---|---|
| ConsumeMessageBatc hMaxSize | String | 1 | The maximum number of messages that can be consumed in each batch. The actual number of consumed messages in a batch can be smaller than the value of this parameter. The value must be an integer from 1 to 32. The default value is 1. |
| CheckImmunityTimeIn Seconds | String | 30 | The shortest time for which the system waits before checking the status of a transactional message for the first time. Unit: seconds. |
| shardingKey | String | - | The partition key that is used to determine the partitions to which ordered messages are distributed. |
| suspendTimeMillis | String | 3000 | The retry interval for ordered messages that fail to be consumed. Unit: milliseconds. |

##### 4.1.5.2 ONSFactory

###### 4.1.5.2.1 createConsumer

Syntax: static Consumer createConsumer(Properties properties) Description: You can call this operation to create a consumer instance that consumes multiple types of messages in ApsaraMQ for RocketMQ. These message types include normal messages, scheduled messages, delayed messages, and transactional messages. Request parameter

| Parameter | Type | Description |
|---|---|---|

| properties | Properties | For more information, see the description of PropertyKeyConst. Required properties: PropertyKeyConst.NAMESRV ADDR, _ PropertyKeyConst.ConsumerId, PropertyKeyConst.AccessKey, and PropertyKeyConst.SecretKey. Optional properties: PropertyKeyConst.ConsumeThreadNums and PropertyKeyConst.ConsumeTimeout. |
|---|---|---|

Response parameter

| Parameter | Description |
|---|---|
| Consumer | The consumer instance that consumes multiple types of messages in ApsaraMQ for RocketMQ. These message types include normal messages, scheduled messages, transactional messages, and delayed messages. |

###### 4.1.5.2.2 createBatchConsumer

Syntax: static BatchConsumer createBatchConsumer(Properties properties) Description: You can call this operation to create consumer instances in ApsaraMQ for RocketMQ (RocketMQ) in batches. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| properties | Properties | For more information, see the description of PropertyKeyConst. Required properties: PropertyKeyConst.NAMESRV ADDR, _ PropertyKeyConst.GROUP ID, PropertyKeyConst.AccessKey, _ and PropertyKeyConst.SecretKey Optional properties: PropertyKeyConst.ConsumeThreadNums, PropertyKeyConst.ConsumeTimeout, and PropertyKeyConst.ConsumeMessageBatchMaxSize |

Response:

| Type | Description |
|---|---|
| BatchConsumer | BatchConsumer |

###### 4.1.5.2.3 createOrderedConsumer

Syntax: static OrderConsumer createOrderedConsumer(Properties properties) Description: You can call this operation to create a consumer instance for consuming ordered messages in ApsaraMQ for RocketMQ (RocketMQ). Request parameters:

| Parameter | Type | Description |
|---|---|---|
| properties | properties | For more information, see the description of PropertyKeyConst. Required properties: PropertyKeyConst.NAMESRV ADDR, _ PropertyKeyConst.GROUP ID, PropertyKeyConst.AccessKey, _ and PropertyKeyConst.SecretKey Optional properties: PropertyKeyConst.ConsumeThreadNums and PropertyKeyConst.ConsumeTimeout |

Response:

| Type | Description |
|---|---|
| OrderConsumer | The consumer instance of ordered messages in RocketMQ. |

###### 4.1.5.2.4 createOrderProducer

Syntax: static OrderProducer createOrderProducer(Properties properties) Description: You can call this operation to create a producer instance for sending ordered messages in ApsaraMQ for RocketMQ (RocketMQ). Request parameters:

| Parameter | Type | Description |
|---|---|---|
| properties | Properties | For more information, see the description of PropertyKeyConst. Required properties: PropertyKeyConst.NAMESRV ADDR, _ PropertyKeyConst.GROUP ID, PropertyKeyConst.AccessKey, _ PropertyKeyConst.SecretKey, and PropertyKeyConst.ShardingKey Optional properties: PropertyKeyConst.SendMsgTimeoutMillis |

Response:

| Type | Description |
|---|---|
| OrderProducer | The producer instance of ordered messages in RocketMQ. |

###### 4.1.5.2.5 createProducer

Syntax: static Producer createProducer(Properties properties) Description: You can call this operation to create a producer instance that publishes normal messages, scheduled messages, and delayed messages in ApsaraMQ for RocketMQ. Request parameter

| Parameter | Type | Description |
|---|---|---|
| properties | Properties | For more information, see the description of PropertyKeyConst. Required properties: PropertyKeyConst.NAMESRV ADDR, _ PropertyKeyConst.GROUP ID, _ PropertyKeyConst.AccessKey, and PropertyKeyConst.SecretKey. Optional properties: PropertyKeyConst.SendMsgTimeoutMillis. |

Response parameter

| Parameter | Description |
|---|---|
| Producer | The producer instance that publishes normal messages, scheduled messages, and delayed messages in ApsaraMQ for RocketMQ. |

###### 4.1.5.2.6 createTransactionProducer

Syntax: static TransactionProducer createTransactionProducer(Properties properties, LocalTransactionChecker checker) Description: You can call this operation to create a producer instance for sending distributed transactional messages in ApsaraMQ for RocketMQ (RocketMQ). Request parameters:

| Parameter | Type | Description |
|---|---|---|

| properties | Properties | For more information, see the description of PropertyKeyConst. Required properties: PropertyKeyConst.NAMESRV ADDR, _ PropertyKeyConst.GROUP ID, _ PropertyKeyConst.AccessKey, and PropertyKeyConst.SecretKey Optional properties: PropertyKeyConst.SendMsgTimeoutMillis and PropertyKeyConst.CheckImmunityTimeInSeconds |
|---|---|---|
| checker | LocalTransactionC hecker | For more information, see the description of LocalTransactionChecker. |

Response:

| Type | Description |
|---|---|
| TransactionProducer | The producer instance of transactional messages in RocketMQ. |

##### 4.1.5.3 Message

###### 4.1.5.3.1 Overview

It is a message that you want to send. A valid message must contain the topic, body, optional tags, and message key.

> **Note:** The length of the custom key-value pair for a message is not constrained, but all custom key-value pairs cannot exceed 32,767 bytes after they are serialized.


###### 4.1.5.3.2 Default message construction

Syntax: Message() Description: You can call this operation to create a message by using the default constructor. Request parameters: none

###### 4.1.5.3.3 Message construction by using parameters (1)

**parameters (1)**

Syntax: public Message(String topic, String tag, String key, byte body) Description: You can call this operation to create a message by specifying parameters. Request parameters:

| Parameter | Type | Description |
|---|---|---|

| topic | String | The topic of the message. It cannot exceed 255 characters in length. The message topic can contain uppercase letters (A-Z), lowercase letters (a-z), digits (0- 9), hyphens (-), and underscores ( ). _ |
|---|---|---|
| tag | String | The message tag, which must be a valid identifier. The tag must be as short as possible and easy to understand. |
| key | String | The key of the message. |
| body | byte | The message body. It cannot exceed 4 MB by default, including message attributes that cannot exceed 8 KB. For more information about the message body, see the cluster deployment documentation. |

###### 4.1.5.3.4 Message construction by using parameters (2)

**parameters (2)**

Syntax: public Message(String topic, String tags, byte body) Description: You can call this operation to create a message by specifying parameters. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the message. It cannot exceed 255 characters in length. The message topic can contain uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), hyphens (-), and underscores ( ). _ |
| tags | String | The message tag, which must be a valid identifier. The tag must be as short as possible and easy to understand. |
| body | byte | The message body. It cannot exceed 4 MB by default, including message attributes that cannot exceed 8 KB. For more information about the message body, see the cluster deployment documentation. |

###### 4.1.5.3.5 putUserProperties

Syntax: public void putUserProperties(String key, String value) Description: You can call this operation to add a custom property key-value pair that can be obtained when the message is consumed. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| key | String | The custom property key. |
| value | String | The custom property value. |

Response: none

###### 4.1.5.3.6 getUserProperties

Syntax: public String getUserProperties(String key) Description: You can call this operation to obtain the custom property value. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| key | String | The custom property key. |

Response:

| Type | Description |
|---|---|
| String | The custom property value. |

###### 4.1.5.3.7 getTopic

Syntax: public String getTopic() Description: You can call this operation to obtain the topic of the messages. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The topic of the messages. |

###### 4.1.5.3.8 setTopic

Syntax: public void setTopic(String topic) Description: You can call this operation to set the topic of the messages. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the messages. |

Response: none

###### 4.1.5.3.9 getTag

Syntax: public String getTag() Description: You can call this operation to obtain the message tag. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The tag of the message. |

###### 4.1.5.3.10 setTag

Syntax: public void setTag(String tag) Sy a pubc o dse ag(S gag) Description: You can call this operation to set the message tag. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| tag | String | The tag of the message. |

Response: none

###### 4.1.5.3.11 getKey

Description: You can call this operation to obtain the message key. Syntax: public String getKey() Request parameters: none Response:

| Type | Description |
|---|---|
| String | The key of the message. |

###### 4.1.5.3.12 setKey

Syntax: public void setKey(String key) Description: You can call this operation to set the message key. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| key | String | The key of the message. |

Response: none

###### 4.1.5.3.13 getMsgID

Syntax: public String getMsgID() Description: You can call this operation to obtain the message ID. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The ID of the message. |

###### 4.1.5.3.14 setMsgID

Syntax: public void setMsgID(String msgid) Description: You can call this operation to set the message ID. Request parameters:

| Parameter | Type | Description |
|---|---|---|

| msgid | String | The ID of the message. |
|---|---|---|

Response: none

###### 4.1.5.3.15 getReconsumeTimes

Syntax: public int getReconsumeTimes() Description: You can call this operation to obtain the number of retries after a message has failed to be consumed. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The number of retries. |

###### 4.1.5.3.16 setReconsumeTimes

Syntax: public void setReconsumeTimes(int value) Description: You can call this operation to set the number of retries to consume a message. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| value | int | The number of retries. |

Response: none

###### 4.1.5.3.17 getBornTimestamp

Syntax: public long getBornTimestamp() Description: You can call this operation to obtain the message production time. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The production time of the message. |

###### 4.1.5.3.18 setBornTimestamp

Syntax: public void setBornTimestamp(long value) Description: You can call this operation to set the message production time. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| value | long | The production time of the message. |

Response: none

###### 4.1.5.3.19 getBornHost

Syntax: public String getBornHost() Description: You can call this operation to retrieve the message production host. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The host that produced the message. |

###### 4.1.5.3.20 setBornHost

Syntax: public void setBornHost(String value) Description: You can call this operation to set the message production host. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| value | long | The host that produces the message. |

Response: none

###### 4.1.5.3.21 getStartDeliverTime

Syntax: public long getStartDeliverTime() Description: You can call this operation to obtain the start time for delivering scheduled messages. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The start time for delivering scheduled messages. |

###### 4.1.5.3.22 setStartDeliverTime

Syntax: public void setStartDeliverTime(long value) Description: You can call this operation to set the delivery time (absolute time) of scheduled messages with a maximum latency of 40 days. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| value | long | The start time for delivering scheduled messages. |

Response: none

###### 4.1.5.3.23 getShardingKey

Syntax: public long getShardingKey() Description: You can call this operation to obtain the sharding key for ordered messages. Request parameters: none Response:

| Type | Description |
|---|---|
| String | The sharding key for ordered messages. |

###### 4.1.5.3.24 setShardingKey

Syntax: public void setShardingKey(String value) Description: You can call this operation to set the sharding key for ordered messages. Request parameters:

| Parameter | Type | Description |
|---|---|---|
| String | long | The sharding key for ordered messages. |

Response: none

##### 4.1.5.4 ONSClientException

###### 4.1.5.4.1 Default ONSClientException construction

Syntax: public ONSClientException() Description: Uses the default exception constructor to construct ONSClientException. Request parameters: none

###### 4.1.5.4.2 ONSClientException construction by using parameters (1)

**using parameters (1)**

Syntax: public ONSClientException(String message) Description: Uses the exception constructor to construct ONSClientException by using parameters.

| Parameter | Type | Description |
|---|---|---|
| message | String | The exception information that needs to be exposed. |

###### 4.1.5.4.3 ONSClientException construction by using parameters (2)

**using parameters (2)**

Syntax: public ONSClientException(Throwable cause) Description: Uses the exception constructor to construct ONSClientException by using parameters.

| Parameter | Type | Description |
|---|---|---|
| message | String | The exception information that needs to be exposed. |

###### 4.1.5.4.4 ONSClientException construction by using parameters (3)

**using parameters (3)**

Syntax: public ONSClientException(String message, Throwable cause) Description: Uses the exception constructor to construct ONSClientException by using parameters.

| Parameter | Type | Description |
|---|---|---|
| message | String | The exception information that needs to be exposed. |
| cause | Throwable | The exception information that needs to be exposed. |

##### 4.1.5.5 Message sending

###### 4.1.5.5.1 Overview

This topic describes the methods for sending various types of messages in ApsaraMQ for RocketMQ. The following figure shows the methods and parameters for different message types. Figure 1. Methods and parameters for publishing messages

###### 4.1.5.5.2 SendResult

###### 4.1.5.5.2.1 Default SendResult construction

Syntax: public SendResult() Description: Uses the default constructor to create a message sending result object. Request parameters: none

###### 4.1.5.5.2.2 getMessageId

Syntax: public long getMessageId() Description: Queries the ID of a message that is sent. Request parameters: none

| Type | Description |
|---|---|
| String | The ID of the sent message. |

###### 4.1.5.5.2.3 getTopic

Syntax: public String getTopic() Description: Queries the topic to which a message that is sent belongs. Request parameters: none

| Type | Description |
|---|---|
| String | The topic of the sent message. |

###### 4.1.5.5.2.4 toString

Syntax: public String toString() Description: Serializes a message sending result. Request parameters: none

| Type | Description |
|---|---|
| String | The serialized string of the message sending result. |

###### 4.1.5.5.3 Producer

###### 4.1.5.5.3.1 Overview

You can use a producer instance to send regular messages, scheduled messages, or delayed messages. Thread security: All implementation classes of a producer instance are thread-secure. Multiple threads can be used to send messages concurrently. A producer instance can send messages under multiple topics. In normal cases, a producer instance is efficient enough to complete all the message sending tasks by using relevant methods. No more instances need to be created. Regular messages can be sent in reliable synchronous, reliable asynchronous, or one-way mode.

###### 4.1.5.5.3.2 send

Syntax: public SendResult send(Message message) Description: Sends a regular message, scheduled message, or delayed message in synchronous mode. The message is sent if no exception is thrown.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The message that you want to send. |

| Parameter | Description |
|---|---|
| SendResult | The sending result that is returned, including the message ID and topic. |

###### 4.1.5.5.3.3 sendOneway

Syntax: public void sendOneway(Message message) Description: Sends a regular message, scheduled message, or delayed message in one-way mode. In this mode, if the RocketMQ broker does not respond, you cannot know whether the message is sent to the broker.

| Parameter | Type | Description |
|---|---|---|

| message | Message | The message that you want to send. |
|---|---|---|

Response parameters: none

###### 4.1.5.5.3.4 sendAsync

Syntax: public void sendAsync(Message message, SendCallback sendCallback) Description: Sends a regular message, scheduled message, or delayed message in asynchronous callback mode.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The message that you want to send. |
| sendCallback | SendCallback | The callback function to be called after the message is sent. |

Response parameters: none

###### 4.1.5.5.3.5 isStarted

Syntax: public boolean isStarted() Description: Checks whether an instance is enabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is enabled. A value of true indicates that the instance is enabled. A value of false indicates that the instance is not enabled. |

###### 4.1.5.5.3.6 isClosed

Syntax: public boolean isClosed() Description: Checks whether an instance is disabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is disabled. A value of true indicates that the instance is disabled. A value of false indicates that the instance is not disabled. |

###### 4.1.5.5.3.7 start

Syntax: public void start() Description: Enables a producer instance to send messages. Request parameters: none Response parameters: none

###### 4.1.5.5.3.8 shutdown

Syntax: public void shutdown() Description: Disables a producer instance from sending messages. Request parameters: none Response parameters: none

###### 4.1.5.5.4 TransactionProducer

###### 4.1.5.5.4.1 send

Syntax: SendResult send(Message message, LocalTransactionExecuter executer, Object arg) Description: Sends a transactional message. The process of sending a transactional message consists of the following three steps: The producer instance first sends a half message to the RocketMQ broker. The producer instance starts a local transaction by using an executor. The RocketMQ broker commits or rolls back the half message that is sent in Step 1 based on the result of the local transaction in Step 2.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The transactional message that you want to send. |
| executer | LocalTransactionExecuter | The local transaction executor. For more information, see the LocalTransactionExecuter class. |
| arg | Object | A custom parameter. This parameter can be used for the local transaction executor. |

| Parameter | Description |
|---|---|
| SendResult | The sending result that is returned, including the message ID and topic. |

###### 4.1.5.5.4.2 isStarted

Syntax: public boolean isStarted() Description: Checks whether an instance is enabled. Request parameters: none

| Type | Description |
|---|---|

| boolean | Indicates whether the instance is enabled. A value of true indicates that the instance is enabled. A value of false indicates that the instance is not enabled. |
|---|---|

###### 4.1.5.5.4.3 isClosed

Syntax: public boolean isClosed() Description: Checks whether an instance is disabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is disabled. A value of true indicates that the instance is disabled. A value of false indicates that the instance is not disabled. |

###### 4.1.5.5.4.4 start

Syntax: public void start() Description: Enables a producer instance to send transactional messages. Request parameters: none Response parameters: none

###### 4.1.5.5.4.5 shutdown

Syntax: public void shutdown() Description: Disables a producer instance from sending transactional messages. Request parameters: none Response parameters: none

###### 4.1.5.5.4.6 LocalTransactionExecuter

execute Syntax: TransactionStatus execute(Message msg, Object arg) Description: Starts a local transaction. This method is called by applications.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The transactional message that you want to send. |
| arg | Object | The custom parameter that is specified by the send method. |

| Parameter | Description |
|---|---|
| TransactionStatus | The result of the local transaction that is returned. The transaction may be in the Commit, Rollback, or unknown state. |

| veloper Guide·SDK reference | Alibaba Cloud Message Queu |
|---|---|

###### 4.1.5.5.4.7 TransactionStatus

The result of a local transaction that corresponds to a half message. The transaction may be in the Commit, Rollback, or unknown state. Enumeration

| Value | Description |
|---|---|
| CommitTransaction | The transaction is committed. Then, the RocketMQ broker delivers the half message to the consumer. |
| RollbackTransaction | The transaction is rolled back. Then, the RocketMQ broker deletes the half message and does not deliver it to the consumer. |
| Unknow | The transaction is in the unknown state. Generally, this value is used when you are not sure whether the transaction is successful or fails. The RocketMQ broker periodically checks the transactions that are in the unknown state. |

###### 4.1.5.5.5 OrderProducer

###### 4.1.5.5.5.1 send

Syntax: SendResult send(Message message, String shardingKey) Description: Sends an ordered message.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The ordered message that you want to send. |
| shardingKey | String | The selectivity factor for the ordered message. A specific message queue is selected based on the value of the shardingKey parameter. |

| Parameter | Description |
|---|---|
| SendResult | The sending result that is returned, including the message ID and topic. |

###### 4.1.5.5.5.2 isStarted

Syntax: public boolean isStarted() p () Description: Checks whether an instance is enabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is enabled. A value of true indicates that the instance is enabled. A value of false indicates that the instance is not enabled. |

###### 4.1.5.5.5.3 isClosed

Syntax: public boolean isClosed() Description: Checks whether an instance is disabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is disabled. A value of true indicates that the instance is disabled. A value of false indicates that the instance is not disabled. |

###### 4.1.5.5.5.4 start

Syntax: public void start() Description: Enables a producer instance to send ordered messages. Request parameters: none Response parameters: none

###### 4.1.5.5.5.5 shutdown

Syntax: public void shutdown() Description: Disables a producer instance from sending ordered messages. Request parameters: none Response parameters: none

##### 4.1.5.6 Message subscription

###### 4.1.5.6.1 Overview

This topic describes the methods for subscribing to various types of messages in ApsaraMQ for RocketMQ. The following figure shows the methods and parameters for different message types. Figure 1. Methods and parameters for subscribing to messages

###### 4.1.5.6.2 Consumer

###### 4.1.5.6.2.1 Overview

You can use a consumer instance to subscribe to regular messages, transactional messages, scheduled messages, or delayed messages.

###### 4.1.5.6.2.2 subscribe

Syntax: public void subscribe(String topic, String subExpression, MessageListener listener) Description: Subscribes to regular messages, transactional messages, scheduled messages, or delayed messages.

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the messages. |
| subExpression | String | The filter expression for subscribing to messages. The RocketMQ broker filters messages based on this expression. Only OR (\|\|) operations are supported. Example 1: "tag1 \|\| tag2 \|\| tag3"; Example 2: When the subExpression parameter is set to null or *, all messages are subscribed to. |
| listener | MessageListener | The message listener for callbacks. |

Response parameters: none

###### 4.1.5.6.2.3 unsubscribe

Syntax: void unsubscribe(String topic) Description: Cancels the subscription to a specific topic.

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the messages. |

Response parameters: none

###### 4.1.5.6.2.4 isStarted

Syntax: public boolean isStarted() Description: Checks whether an instance is enabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is enabled. A value of true indicates that the instance is enabled. A value of false indicates that the instance is not enabled. |

###### 4.1.5.6.2.5 isClosed

Syntax: public boolean isClosed() Description: Checks whether an instance is disabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is disabled. A value of true indicates that the instance is disabled. A value of false indicates that the instance is not disabled. |

###### 4.1.5.6.2.6 start

Syntax: public void start() Description: Enables a consumer instance. Request parameters: none Response parameters: none

###### 4.1.5.6.2.7 shutdown

Syntax: public void shutdown() Description: Disables a consumer instance. Request parameters: none Response parameters: none

###### 4.1.5.6.3 MessageListener

###### 4.1.5.6.3.1 Overview

A consumer registers a message listener to subscribe to messages. Thread security requirements: A message listener can be concurrently used by multiple threads of a consumer. You must ensure the security of concurrency.

###### 4.1.5.6.3.2 consume

Syntax: Action consume(Message message, ConsumeContext context) Description: Consumes messages. This method is called by applications. Unstable network conditions such as network jitter may result in message duplication. In this case, the consumer can perform idempotent processing for services that are sensitive to duplicated messages.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The message that you want to consume. |
| context | ConsumeContext | The context of the consumption. For more information, see ConsumeContext in the code. |

| Parameter | Description |
|---|---|
| Action | The result of the consumption. Consumption failed: An exception is thrown or Action.ReconsumeLater is returned. Action.ReconsumeLater indicates null. Consumption succeeded: Action.CommitMessage is returned. |

###### 4.1.5.6.4 Action

###### 4.1.5.6.4.1 Overview

The result of the consumption that is returned for a message. Enumeration

| Value | Type | Description |
|---|---|---|
| CommitMessage | String | The message is consumed. The consumer continues to consume the next message. |
| ReconsumeLater | String | The consumer failed to consume the message. The consumer requests the RocketMQ broker to redeliver the failed message later and continues to consume another message. |

###### 4.1.5.6.4.2 valueOf

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

###### 4.1.5.6.4.3 values

Syntax: public static Action[] values() Description: Returns an array of constants in the declared order of constants of an enumerated type. Request parameters: none

| Parameter | Description |
|---|---|
| Action[] | The array of constants in the declared order of constants of the enumerated type that is returned. |

###### 4.1.5.6.5 PropertyValueConst

The constant that specifies the consumption mode. Enumeration

| Value | Type | Description |
|---|---|---|
| BROADCASTING | String | The broadcasting consumption mode. |
| CLUSTERING | String | The clustering consumption mode. |

###### 4.1.5.6.6 OrderConsumer

###### 4.1.5.6.6.1 Overview

You can use a consumer instance of ordered messages to subscribe to messages in first in, first out (FIFO) order.

###### 4.1.5.6.6.2 subscribe

Syntax: void subscribe(String topic, String subExpression, MessageOrderListener listener) Description: Subscribes to ordered messages. Parameters:

| Name | Type | Description |
|---|---|---|
| topic | String | The message topic. |
| subExpression | String | The filter expression for subscribing to messages. The RocketMQ server filters messages based on this expression. Only OR (\|\|) operations are supported. Example 1: "tag1 \|\| tag2 \|\| tag3". Example 2: If subExpression is null or *, all messages are subscribed to. |
| listener | MessageOrd erListener | The message callback listener. |

Response parameters: none

###### 4.1.5.6.6.3 unsubscribe

Syntax: void unsubscribe(String topic) Description: Cancels the subscription to a specific topic.

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the messages. |

Response parameters: none

###### 4.1.5.6.6.4 isStarted

Syntax: public boolean isStarted() Description: Checks whether an instance is enabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is enabled. A value of true indicates that the instance is enabled. A value of false indicates that the instance is not enabled. |

###### 4.1.5.6.6.5 isClosed

Syntax: public boolean isClosed() Description: Checks whether an instance is disabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is disabled. A value of true indicates that the instance is disabled. A value of false indicates that the instance is not disabled. |

###### 4.1.5.6.6.6 start

Syntax: public void start() Description: Enables a consumer instance. Request parameters: none Response parameters: none

###### 4.1.5.6.6.7 shutdown

Syntax: public void shutdown() Description: Disables a consumer instance. Request parameters: none Response parameters: none

###### 4.1.5.6.7 MessageOrderListener

###### 4.1.5.6.7.1 Overview

A consumer registers an ordered message listener to subscribe to ordered messages. Thread security requirements: A message listener can be concurrently used by multiple threads of a consumer. You must ensure the security of concurrency.

###### 4.1.5.6.7.2 consume

Syntax: OrderAction consume(Message message, ConsumeOrderContext context) Description: Consumes messages. This method is called by applications. Unstable network conditions such as network jitter may result in message duplication. In this case, the consumer can perform idempotent processing for services that are sensitive to duplicated messages.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The message that you want to consume. |
| context | ConsumeOrderContext | The context of the consumption. For more information, see ConsumeOrderContext in the code. |

| Parameter | Description |
|---|---|

| OrderAction | The result of the consumption. Consumption failed: An exception is thrown or Action.Suspend is returned. Action.Suspend indicates null. Consumption succeeded: Action.Success is returned. |
|---|---|

###### 4.1.5.6.8 OrderAction

###### 4.1.5.6.8.1 Overview

The result of the consumption that is returned for an ordered message. Enumeration

| Value | Type | Description |
|---|---|---|
| Success | String | The message is consumed. The consumer continues to consume the next message. |
| Suspend | String | The consumer failed to consume the message. The current queue is suspended. |

###### 4.1.5.6.8.2 valueOf

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

###### 4.1.5.6.8.3 values

Syntax:publicstaticOrderAction[]values() Syntax: public static OrderAction[] values() Description: Returns an array of constants in the declared order of constants of an enumerated type. Request parameters: none

| Parameter | Description |
|---|---|
| OrderAction[] | The array of constants in the declared order of constants of the enumerated type that is returned. |

###### 4.1.5.6.9 BatchConsumer

###### 4.1.5.6.9.1 Overview

You can use a batch consumer instance to subscribe to multiple messages at a time.

###### 4.1.5.6.9.2 subscribe

Syntax: void subscribe(String topic, String subExpression, BatchMessageListener listener) Description: Subscribes to regular messages, transactional messages, scheduled messages, or delayed messages. Parameters:

| Name | Type | Description |
|---|---|---|
| topic | String | The message topic. |
| subExpression | String | The filter expression string for the subscription. The RocketMQ server filters messages based on this expression. Only the OR (\|\|) operator is supported. Example 1: "tag1 \|\| tag2 \|\| tag3". Example 2: If subExpression is null or *, all messages are subscribed. |
| listener | BatchMess ageListener | The message callback listener. |

Response parameters: none

###### 4.1.5.6.9.3 unsubscribe

Syntax: void unsubscribe(String topic) Description: Cancels the subscription to a specific topic.

| Parameter | Type | Description |
|---|---|---|
| topic | String | The topic of the messages. |

Response parameters: none

###### 4.1.5.6.9.4 isStarted

Syntax: public boolean isStarted() Description: Checks whether an instance is enabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is enabled. A value of true indicates that the instance is enabled. A value of false indicates that the instance is not enabled. |

###### 4.1.5.6.9.5 isClosed

Syntax: public boolean isClosed() Description: Checks whether an instance is disabled. Request parameters: none

| Type | Description |
|---|---|
| boolean | Indicates whether the instance is disabled. A value of true indicates that the instance is disabled. A value of false indicates that the instance is not disabled. |

###### 4.1.5.6.9.6 start

Syntax: public void start() Description: Enables a consumer instance. Request parameters: none Response parameters: none

###### 4.1.5.6.9.7 shutdown

Syntax: public void shutdown() Description: Disables a consumer instance. Request parameters: none Response parameters: none

###### 4.1.5.6.10 BatchMessageListener

###### 4.1.5.6.10.1 Overview

A consumer registers a batch message listener to consume multiple messages at a time. Thread security requirements: A message listener can be concurrently used by multiple threads of a consumer. You must ensure the security of concurrency.

###### 4.1.5.6.10.2 consume

Syntax: Action consume(Message message, ConsumeContext context) Description: Consumes multiple messages at a time. This method is called by applications. Unstable network conditions such as network jitter may result in message duplication. In this case, the consumer can perform idempotent processing for services that are sensitive to duplicated messages.

| Parameter | Type | Description |
|---|---|---|
| message | Message | The messages that you want to consume. |
| context | ConsumeContext | The context of the consumption. For more information, see ConsumeContext in the code. |

| Parameter | Description |
|---|---|
| Action | The result of the consumption. Consumption failed: An exception is thrown or Action.ReconsumeLater is returned. Action.ReconsumeLater indicates null. Consumption succeeded: Action.CommitMessage is returned. |
