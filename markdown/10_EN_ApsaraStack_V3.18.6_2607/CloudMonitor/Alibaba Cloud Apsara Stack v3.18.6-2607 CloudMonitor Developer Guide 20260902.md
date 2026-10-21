---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 CloudMonitor Developer Guide 20260902"
product_version: "V3.18.6_2607"
doc_version: "20260902"
pdf_pages: 616
source_pdf: "bebe5a3985330071_Alibaba Cloud Apsara Stack v3.18.6-2607 CloudMonitor Developer Guide 20260902.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E7%9B%91%E6%8E%A7/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20CloudMonitor%20Developer%20Guide%2020260902.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 CloudMonitor Developer Guide 20260902

## Table of Contents

- 1 Preparations
  - 1.1 Obtain the endpoint
- 2 API Reference
  - 2.1 Monitoring data on time series metrics of cloud services
    - 2.1.1 DescribeMetricLast
    - 2.1.2 DescribeMetricList
    - 2.1.3 DescribeMetricMetaList
    - 2.1.4 DescribeProjectMeta
    - 2.1.5 DescribeMetricData
    - 2.1.6 DescribeMetricTop
    - 2.1.7 DescribeMetricTopList
    - 2.1.8 DescribeCloudProductResourceTypes
  - 2.2 Console view configuration
    - 2.2.1 DescribeConsoleViews
  - 2.3 Custom monitoring
    - 2.3.1 PutCustomMetric
    - 2.3.2 BatchDeleteCustomMetricMeta
    - 2.3.3 CreateCustomMetricMeta
    - 2.3.4 DescribeCustomMetricList
    - 2.3.5 DeleteCustomMetric
  - 2.4 Host monitoring
    - 2.4.1 NodeInstall
    - 2.4.2 DescribeArgusAgentInstallRecord
    - 2.4.3 DescribeMonitoringAgentStatuses
    - 2.4.4 DescribeMonitoringAgentHosts
    - 2.4.5 InstallMonitoringAgent
    - 2.4.6 DescribeMonitoringAgentProcesses
    - 2.4.7 PutMonitoringConfig
    - 2.4.8 DeleteMonitoringAgentProcess
    - 2.4.9 CreateMonitoringAgentProcess
    - 2.4.10 DescribeMonitoringConfig
    - 2.4.11 DescribeMonitoringAgentAccessKey
    - 2.4.12 UninstallMonitoringAgent
  - 2.5 Alert service
    - 2.5.1 DescribeAlertingMetricRuleResources
    - 2.5.2 PutResourceMetricRule
    - 2.5.3 DescribeAlertHistoryList
    - 2.5.4 DeleteMetricRuleTargets
    - 2.5.5 DescribeActiveMetricRuleList
    - 2.5.6 DescribeProductsOfActiveMetricRule
    - 2.5.7 DeleteMetricRuleResources
    - 2.5.8 DescribeMetricRuleList
    - 2.5.9 DescribeMetricRuleCount
    - 2.5.10 DeleteMetricRules
    - 2.5.11 DisableMetricRules
    - 2.5.12 EnableMetricRules
    - 2.5.13 DeleteContact
    - 2.5.14 DescribeMetricRuleTargets
    - 2.5.15 DescribeEventRuleList
    - 2.5.16 DescribeMetricRuleTemplateList
    - 2.5.17 DescribeContactList
    - 2.5.18 ApplyMetricRuleTemplate
    - 2.5.19 DescribeEventRuleTargetList
    - 2.5.20 DescribeMetricRuleTemplateAttribute
    - 2.5.21 DescribeEventRuleAttribute
    - 2.5.22 DescribeContactListByContactGroup
    - 2.5.23 PutContact
    - 2.5.24 DescribeMetricPromQLRange
    - 2.5.25 PutContactGroup
    - 2.5.26 PutGroupMetricRule
    - 2.5.27 CreateMetricRuleResources
    - 2.5.28 DescribeContactGroupList
    - 2.5.29 DeleteMetricRuleTemplate
    - 2.5.30 PutEventRuleTargets
    - 2.5.31 CreateMetricRuleTemplate
    - 2.5.32 CreateGroupMetricRules
    - 2.5.33 DeleteEventRules
    - 2.5.34 ModifyMetricRuleTemplate
    - 2.5.35 PutMetricRuleTargets
    - 2.5.36 DescribeDynamicThresholdBound
  - 2.6 Event monitoring
    - 2.6.1 DescribeSystemEventHistogram
    - 2.6.2 DescribeSystemEventAttribute
    - 2.6.3 DescribeSystemEventCount
    - 2.6.4 SendDryRunSystemEvent
    - 2.6.5 PutCustomEvent
    - 2.6.6 DescribeSystemEventMetaList
    - 2.6.7 DescribeCustomEventCount
    - 2.6.8 DescribeCustomEventAttribute
  - 2.7 Custom dashboard
    - 2.7.1 CreateDashboardFolder
    - 2.7.2 ModifyDashboardToFolder
    - 2.7.3 ModifyDashboardFolder
    - 2.7.4 DescribeDashboard
  - 2.8 Application group
    - 2.8.1 DescribeMonitorGroups
    - 2.8.2 DescribeMonitorGroupInstances
    - 2.8.3 CreateMonitorGroupInstances
    - 2.8.4 DescribeUnhealthyHostAvailability
    - 2.8.5 DeleteMonitorGroupInstances
    - 2.8.6 DescribeMonitorGroupInstanceAttribute
    - 2.8.7 DescribeHostAvailabilityList
    - 2.8.8 CreateMonitorGroup
    - 2.8.9 DeleteMonitorGroup
    - 2.8.10 CreateHostAvailability
    - 2.8.11 CreateMonitorGroupNotifyPolicy
    - 2.8.12 DeleteHostAvailability
    - 2.8.13 DescribeMonitorGroupCategories
    - 2.8.14 ModifyMonitorGroupInstances
    - 2.8.15 ModifyHostAvailability
    - 2.8.16 PutMonitorGroupDynamicRule
    - 2.8.17 ModifyMonitorGroup
    - 2.8.18 DeleteMonitorGroupDynamicRule
    - 2.8.19 DeleteMonitorGroupNotifyPolicy
    - 2.8.20 DescribeMonitorGroupNotifyPolicyList
    - 2.8.21 DescribeMonitorGroupDynamicRules
  - 2.9 Site monitoring
    - 2.9.1 DescribeSiteMonitorData
    - 2.9.2 DescribeSiteMonitorStatistics
    - 2.9.3 DescribeSiteMonitorList
    - 2.9.4 DescribeSiteMonitorISPCityList
    - 2.9.5 CreateSiteMonitor
    - 2.9.6 DescribeSiteMonitorAttribute
    - 2.9.7 DisableSiteMonitors
    - 2.9.8 EnableSiteMonitors
    - 2.9.9 DeleteSiteMonitors
    - 2.9.10 ModifySiteMonitor
    - 2.9.11 DescribeSiteMonitorQuota
  - 2.10 Alert center
    - 2.10.1 DescribeBatchDetectTaskWithAlertResult
    - 2.10.2 DescribeNotificationRules
    - 2.10.3 DescribeAlertList
    - 2.10.4 DeleteAlertFilterConfigBatch
    - 2.10.5 ModifyAlertFilterConfig
    - 2.10.6 DescribeAlertFilterConfig
    - 2.10.7 DeleteNotificationRules
    - 2.10.8 ModifyNotificationRule
    - 2.10.9 CreateAlertFilterConfig
    - 2.10.10 PutNotificationRule
  - 2.11 Data subscription
    - 2.11.1 CreateMetricPubSync
    - 2.11.2 UpdateMetricPubSync
    - 2.11.3 DeleteMetricPubSync
    - 2.11.4 DescribeMetricPubSyncs
  - 2.12 Log monitoring
    - 2.12.1 PutLogMonitor
    - 2.12.2 DeleteLogMonitor
    - 2.12.3 DescribeLogMonitorList
- 3 Metrics
  - 3.1 Elastic computing
    - 3.1.1 Kubernetes container monitoring
    - 3.1.2 ECS
    - 3.1.3 BMCP nodes
    - 3.1.4 BMCP containers
    - 3.1.5 Bare Metal Computing Platform (BMCP) (Container - Intelligent Computing Cluster)
    - 3.1.6 Bare Metal Computing Platform (BMCP)
    - 3.1.7 Bare Metal Management (BMS)
  - 3.2 Database services
    - 3.2.1 ApsaraDB RDS
    - 3.2.2 ApsaraDB RDS (New)
    - 3.2.3 PolarDB
    - 3.2.4 PolarDB databases that use local SSDs
    - 3.2.5 PolarDB-X 2.0
      - 3.2.5.1 Compute nodes of PolarDB-X 2.0
      - 3.2.5.2 Data nodes of PolarDB-X 2.0
    - 3.2.6 ApsaraDB for MongoDB (Old)
    - 3.2.7 ApsaraDB for MongoDB (New)
    - 3.2.8 Tair (Redis OSS-compatible) (Old)
    - 3.2.9 Tair (Redis OSS-compatible) (New)
    - 3.2.10 AnalyticDB for PostgreSQL
    - 3.2.11 AnalyticDB for PostgreSQL (new)
    - 3.2.12 DTS
      - 3.2.12.1 Data Transmission Service DTS(Tracking tasks)
      - 3.2.12.2 Data Transmission Service DTS (migration tasks)
      - 3.2.12.3 Data Transmission Service DTS (sync tasks)
    - 3.2.13 Lindorm
    - 3.2.14 Lindorm 2.0
  - 3.3 Storage and CDN
    - 3.3.1 NAS
    - 3.3.2 OSS
    - 3.3.3 CPFS
    - 3.3.4 APFS
    - 3.3.5 EFS-NAS file storage
  - 3.4 Network
    - 3.4.1 NAT Gateway
    - 3.4.2 SLB
    - 3.4.3 Application Load Balancer
    - 3.4.4 EIP
    - 3.4.5 VPN Gateway
    - 3.4.6 DNS
    - 3.4.7 Alibaba Cloud DNS - Tenant forwarded domain names
    - 3.4.8 Cloud Enterprise Network
  - 3.5 Middleware services
    - 3.5.1 ApsaraMQ for RocketMQ
    - 3.5.2 Message Queue (tiangong)
    - 3.5.3 ApsaraMQ for Kafka
    - 3.5.4 API Gateway
  - 3.6 Big data
    - 3.6.1 DataHub
    - 3.6.2 Alibaba Cloud Elasticsearch
    - 3.6.3 MaxCompute
    - 3.6.4 MaxCompute quota groups
  - 3.7 Security (Apsara Stack Security)
    - 3.7.1 Tenant-side bastion hosts
    - 3.7.2 Static data masking and watermarking
    - 3.7.3 Vulnerability scanner engines
    - 3.7.4 NFV Cloud Firewall
    - 3.7.5 Web Application Firewall
  - 3.8 AI and machine learning
    - 3.8.1 AI Studio (online service)
    - 3.8.2 AI Studio (model evaluation)
    - 3.8.3 AI Studio (Notebook modeling)
    - 3.8.4 AI Studio (task modeling)
    - 3.8.5 AI Studio (visual modeling)
    - 3.8.6 AI Studio for model tuning
    - 3.8.7 AI Studio (batch inference)
    - 3.8.8 AI Studio (online service group)
    - 3.8.9 AI Studio (Resource Pool)
    - 3.8.10 A-Speed (High-Performance Inference Service)
    - 3.8.11 Elastic Fault Tolerance Service

## 1 Preparations

### 1.1 Obtain the endpoint

This topic describes how to obtain the endpoint of CloudMonitor.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, select **Platform Operation** > **Apsara Infrastructure**
**Management** > **Resource Management**.
3. On the **Product & Cluster O&M** page, search for CMS and click **Cluster Details** in the
**Actions** column.
4. On the **Services** tab, click **Details** in the **Actions** column for cms.
5. On the **information of Component** page, select **Registration Variables**, search for
**metric.open.endpoint**, and view the value of the endpoint.

## 2 API Reference

### 2.1 Monitoring data on time series metrics of cloud services

**metrics of cloud services**

#### 2.1.1 DescribeMetricLast

Queries the latest monitoring data of a monitored object.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetricL ast | The operation that you want to perform. Set the value to DescribeMetricLast. |
| MetricName | String | Yes | CPUUtilization | The name of the monitoring metric. |
| Namespace | String | Yes | acs ecs dashbo _ _ ard | The namespace of the service. This parameter is used to differentiate services. Specify the value in the acs Service _ name format. |

| Dimensions | String | No | [{"instanceId":" XXXXXX"}] | The dimensions based on which the monitoring data of the specified resource is queried. The value is a collection of key- value pairs. A typical key- value pair is instanceId:XXXXXX . You can specify up to 20 instance IDs in each call. Each key or value can be 1 to 64 bytes in length. A key or value that contains more than 64 characters is truncated and the first 64 bytes are retained. The key and value can contain letters, digits, periods (.), hyphens (-), underscores ( ), forward slashes (/), _ and backslashes (\). Note If you set Dimensions to ordered strings in the request, the value of this parameter is a key-value map expressed in JSON strings. |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | key- |   |
|   |   |   |   |   | key- |   |   |
| StartTime | String | No | 2019-01-31 10:00:00 | The beginning of the time range to query. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. Note You can query data in a time range that spans 31 days at most within the last 270 days. |   |   |   |
| EndTime | String | No | 2019-01-31 10:10:00 | The end of the time range to query. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. Note You can query data within the last 270 days. |   |   |   |

|   | value |   |
|---|---|---|
|   | value |   |

| Express | String | No | {"groupby": ["userId","instan ceId"]} | The expression that is used to calculate the query results in real time. |
|---|---|---|---|---|
| Length | String | No | 1000 | The number of entries per page. Default value: 1000. |
| NextToken | String | No | 1576143285000 9dd70bb64cff1f 0fff6c0b08ffff07 3be5fb1e785e2 b020f7fed9b5e1 37bd810a6d6cff 5ae**** | The pagination token. If the number of results exceeds the maximum number of entries allowed per page, a pagination token is returned. This pagination token can be used as a request parameter to retrieve a new page of results. If a response does not contain pagination tokens, all query results are returned. |
| Period | String | No | 60 | The interval at which the monitoring data is queried. In most cases, the interval is the same as that for reporting metric data. Unit: seconds. If you do not specify this parameter, raw data is queried at the reporting interval specified when the corresponding metric was created. If a statistical period was specified for the corresponding alert rule, raw data is queried based on the statistical period. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 021472A6-25E3- 4094-8D00- BA4B6A5486C3 | The request ID. |
| Code | String | 200 | The HTTP status code. Note The HTTP status code 200 indicates that the request was successful. |

| Success | Boolean | true | Indicates whether the request was successful. |
|---|---|---|---|
| Period | String | 60 | The interval at which the monitoring data was queried. Unit: seconds. |
| NextToken | String | xxxxxx | The pagination token. |
| Datapoints | String | [{"timestamp":154 8777660000,"userI d":"123","instanceI d":"i- abc","Minimum":9. 92,"Average":9.92, "Maximum":9.92}] | The monitoring data. |
| Message | String | Success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricLast &MetricName=CPUUtilization &Namespace=acs_ecs_dashboard &<Common request parameters>
```

Sample success responses `XML` format

```xml
<QueryMetricListResponse>
    <Period>60</Period>
    <Datapoints>
        <Datapoints>
            <timestamp>1490152860000</timestamp>
            <Maximum>100</Maximum>
            <userId> 123456789876****</userId>
            <Minimum>93.1</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.52</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490152920000</timestamp>
            <Maximum>100</Maximum>
            <userId> 123456789876**** </userId>
            <Minimum>92.59</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.49</Average>
        </Datapoints>
        <Datapoints>
```

```xml
            <timestamp>1490152980000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>92.86</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.44</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153040000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>91.43</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.36</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153100000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>93.55</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.51</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153160000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>93.1</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.52</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153220000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>92.59</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.42</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153280000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>91.18</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.34</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153340000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>92.86</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.46</Average>
```

```xml
        </Datapoints>
        <Datapoints>
            <timestamp>1490153400000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>91.18</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.35</Average>
        </Datapoints>
    </Datapoints>
    <RequestId>6661EC50-8625-4161-B349-E0DD59002AB7</RequestId>
    <Success>true</Success>
    <Code>200</Code>
</QueryMetricListResponse>
```

`JSON` format `{`

```json
 "Period":"60",
 "Datapoints":[
```

`{`

```json
   "timestamp":1490152860000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.1,
   "Average":99.52
```

`},` `{`

```json
   "timestamp":1490152920000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.59,
   "Average":99.49
```

`},` `{`

```json
   "timestamp":1490152980000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.86,
   "Average":99.44
```

`},` `{`

```json
   "timestamp":1490153040000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.43,
   "Average":99.36
```

`},` `{`

```json
   "timestamp":1490153100000,
```

`p` `,`

```json
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.55,
   "Average":99.51
```

`},` `{`

```json
   "timestamp":1490153160000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.1,
   "Average":99.52
```

`},` `{`

```json
   "timestamp":1490153220000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.59,
   "Average":99.42
```

`},` `{`

```json
   "timestamp":1490153280000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.18,
   "Average":99.34
```

`},` `{`

```json
   "timestamp":1490153340000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.86,
   "Average":99.46
```

`},` `{`

```json
   "timestamp":1490153400000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.18,
   "Average":99.35
```

`}` `],`

```json
 "RequestId":"6A5F022D-AC7C-460E-94AE-B9E75083D027",
 "Success":true,
 "Code":"200"
```

`}`

#### 2.1.2 DescribeMetricList

Queries the monitoring data of a time series metric for a cloud service within a specified period of time. For more information about the values of parameters such as Namespace, Metric, Period, and Dimensions for each cloud service, see "Metrics for Apsara Stack services".

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetricLi st | The operation that you want to perform. Set the value to DescribeMetricList. |
| MetricName | String | Yes | cpu idle _ | The metric name. |
| Namespace | String | Yes | acs ecs dashbo _ _ ard | The namespace of the service. Format: acs <Service name>. _ |
| Dimensions | String | Yes | [{"instanceId": "i- abcdefgh12****" }] | The dimensions that specify the resources whose monitoring data you want to query. The value is a collection of key-value pairs. A typical key-value pair is instanceId:XXXXXX. You can specify up to 10 instance IDs in each request. Each key or value can be 1 to 64 bytes in length. A key or value that contains more than 64 characters is truncated and the first 64 bytes are retained. The key and value can contain letters, digits, periods (.), hyphens (-), underscores ( ), forward _ slashes (/), and backslashes (\). Note Dimensions must be formatted as a JSON string in a specific order. |

| EndTime | String | No | 2019-01-30 00:10:00 | The end of the time range to query. The following formats are supported: UNIX timestamp: the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. UTC time: the UTC time in the YYYY-MM-DDThh:mm:ssZ format. |   |
|---|---|---|---|---|---|
| Express | String | No | {"groupby": ["userId","instan ceId"]} | The expression that is used to calculate the query results in real time. Only the groupby expression is supported. This expression is similar to the GROUP BY statement that is used in databases. |   |
| Length | String | No | 1000 | The number of entries per page. Default value: 1000. |   |
| NextToken | String | No | 1576148535000 9dd70bb64cff1f 0fff750b08ffff07 3be5fb1e785e2 b020f1a949d5e a14aea7fed82f0 1dd87311 | The pagination token. Note You do not need to specify this parameter if you only want to obtain entries on the first page. The pagination token returned in a response can be used as an input parameter for obtaining entries on the next page. If a response contains no pagination tokens, all query results have been returned. |   |

|   | BY |
|---|---|

| Period | String | No | 60 | The interval at which the monitoring data is queried. Unit: seconds. Valid values: 60, 300, and 900, which represent 1 minute, 5 minutes, and 15 minutes, respectively. Note Specify this parameter based on your business requirements. For example, if you set this parameter to 60, only 1,000 records are returned, though a total of 1,440 records are generated. This is because the maximum number of records that can be returned for each query is 1,000. If you set this parameter to 300, 288 records are returned. |
|---|---|---|---|---|
| StartTime | String | No | 2019-01-30 00:00:00 | The beginning of the time range to query. The following formats are supported: UNIX timestamp: the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. UTC time: the UTC time in the YYYY-MM-DDThh:mm:ssZ format. Note The period specified by StartTime and EndTime includes the point in time specified by EndTime but does not include the point in time specified by StartTime. The start time must be earlier than the end time. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3121AE7D-4AFF- 4C25-8F1D- C8226EBB1F42 | The request ID. |

| Code | String | 200 | The HTTP status code. Note The HTTP status code 200 indicates that the request was successful. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. |
| NextToken | String | 15761441850009d d70bb64cff1f0fff6d 0b08ffff073be5fb1 e785e2b020f7fed9 b5e137bd810a6d6 cff5aee816 | The pagination token. Note You do not need to specify this parameter if you only want to obtain entries on the first page. The pagination token returned in a response can be used as an input parameter for obtaining entries on the next page. If a response contains no pagination tokens, all query results have been returned. |
| Period | String | 60 | The interval at which the monitoring data was queried. Unit: seconds. Valid values: 60, 300, and 900. |
| Datapoints | String | [{"timestamp":154 8777660000,"userI d":"123","instanceI d":"i- abc","Minimum":9. 92,"Average":9.92, "Maximum":9.92}] | The monitoring data. |
| Message | String | Success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricList &MetricName=cpu_idle &Namespace=acs_ecs_dashboard &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Period>60</Period>
```

```xml
<Datapoints>
    <timestamp>1490152860000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>93.1</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.52</Average>
</Datapoints> <Datapoints>
    <timestamp>1490152920000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>92.59</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.49</Average>
</Datapoints> <Datapoints>
    <timestamp>1490152980000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>92.86</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.44</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153040000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>91.43</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.36</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153100000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>93.55</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.51</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153160000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>93.1</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.52</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153220000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>92.59</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
```

```xml
    <Average>99.42</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153280000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>91.18</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.34</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153340000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>92.86</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.46</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153400000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>91.18</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.35</Average>
</Datapoints> <RequestId>6A5F022D-AC7C-460E-94AE-B9E75083D027</RequestId> <Success>true</Success> <Code>200</Code>
```

`JSON` format `{`

```json
 "Period":"60",
 "Datapoints":[
```

`{`

```json
   "timestamp":1490152860000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.1,
   "Average":99.52
```

`},` `{`

```json
   "timestamp":1490152920000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.59,
   "Average":99.49
```

`},` `{`

```json
   "timestamp":1490152980000,
   "Maximum":100,
```

```json
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.86,
   "Average":99.44
```

`},` `{`

```json
   "timestamp":1490153040000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.43,
   "Average":99.36
```

`},` `{`

```json
   "timestamp":1490153100000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.55,
   "Average":99.51
```

`},` `{`

```json
   "timestamp":1490153160000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.1,
   "Average":99.52
```

`},` `{`

```json
   "timestamp":1490153220000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.59,
   "Average":99.42
```

`},` `{`

```json
   "timestamp":1490153280000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.18,
   "Average":99.34
```

`},` `{`

```json
   "timestamp":1490153340000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.86,
   "Average":99.46
```

`},` `{`

```json
   "timestamp":1490153400000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.18,
   "Average":99.35
```

`}` `],`

```json
 "RequestId":"6A5F022D-AC7C-460E-94AE-B9E75083D027",
 "Success":true,
 "Code":"200"
```

`}`

#### 2.1.3 DescribeMetricMetaList

Queries monitoring item details, including metadata such as the metric name, statistical method, unit, description, dimension, and reporting period.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| MetricNam e | Strin g | Quer y | No | CPUUtilization | The name of the metric. The system supports exact matching. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. The count starts from 1. Default value: 1 |
| Namespac e | Strin g | Quer y | No | acs kvstore _ | The namespace of the metric. Namespaces are used to distinguish different products. The naming format is acs product name. You _ can call the DescribeProjectMeta operation to query the namespace value of each product. |

| Labels | Strin g | Quer y | No | [{"name":"productCatego ry","value":"kvstore old"} _ ] | Filter monitoring items by tag. The format is a JSON array. The element structure is {"name":"tag name","value":"tag value"}. The system supports tags including MetricCategory (monitoring item category), alertEnable (whether to enable alert), alertUnit (alert unit), unitFactor (unit conversion factor), minAlertPeriod (minimum alert period), and productCategory (product category). |
|---|---|---|---|---|---|
| PageSize | Integ er | Quer y | No | 30 | The number of entries to return on each page. Default value: 30. Valid values: 1 to 100 |

**API description**

Call this operation to query the metadata of monitoring items that Cloud Monitor (CMS) supports. You can use this operation to obtain the metric details of each cloud product, including the metric name, statistical method, unit, and dimension.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Resources | Array | [{"Namespace":"ac s ecs","MetricNam _ e":"CPUUtilization" }] | The list of monitoring item metadata. |
| -Namespace | String | acs ecs _ | The namespace of the metric, which is used to distinguish different products. The naming format is acs product name. _ |
| -MetricName | String | CPUUtilization | The name of the metric. |
| -Statistics | String | Average,Minimum, Maximum | The statistical method. Separate multiple statistical methods, such as Average, Minimum, Maximum, Sum, and Count, with commas. |
| -Unit | String | % | The unit. |

| -Description | String | CPU utilization | The description of the monitoring item. |
|---|---|---|---|
| - DescriptionJso n | String | {"en- us":"CPUUtilization" ,"zh-cn":"CPU使用率"} | The multilingual description of the monitoring item in JSON format. |
| -Dimensions | String | userId,instanceId | The monitoring dimension. Separate multiple dimensions, such as userId and instanceId, with commas. |
| -Periods | String | 60,300 | The reporting period in seconds. Separate multiple periods with commas. |
| -Labels | String | [{"name":"alertEna ble","value":"true" }] | The tag information in JSON array format, which includes the tag name and tag value. |
| -Version | String | 1.0 | The version of the monitoring item. |
| -SubProducts | String | ECS | The name of the sub-product. |
| RequestId | String | 15B664E7-1823- 4C84-A59B- 1A3BXXXXX | The request ID. |
| Success | Boolean | true | Indicates whether the request is successful. Valid values: true (success) and false (failure) |
| Code | String | 200 | The status code. A value of 200 indicates success. |
| Message | String | successful | The returned message. The system returns successful when the request succeeds. |
| TotalCount | String | 100 | The total number of records. |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Invalid parameters. |
| 403 | 403 | AccessForbidden | You do not have permissions to perform operations on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The system failed to process the request due to some unknown errors. |

#### 2.1.4 DescribeProjectMeta

Queries the information of monitored services in CloudMonitor. The information obtained by this operation includes the service description, namespace, and tags.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeProject Meta | The operation that you want to perform. Set the value to DescribeProjectMeta. |
| callerType | String | No | "" | The type of the API caller. |

|   |   |   |   |   |   | The tags that you specify to filter services. A tag of a metric is used as a special mark of alerts triggered by the metric. For example, a tag can specify the service specification to which an alert belongs and whether an alert rule can be configured for a metric. The format is [{"name":"Tag |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | [{"name":"Tag |   |
|   |   |   |   |   |   | name","value":"Tag value"}, |   |   |
|   |   |   |   |   |   | {"name":"Tag name","value":"Tag |   |   |
|   |   |   |   |   |   | value"}] |   |   |
| Labels |   | String | No | [{"name":"prod uct","value":"EC S"}] |   |   |   |   |
| PageNumber |   | Integer | No | 1 |   | The number of the page to return. Default value: 1. |   |   |

| PageSize | Integer | No | 30 | The number of entries per page. Default value: 30. Note Apsara Stack does not limit the value of this parameter. If you want to view all desired entries on a small number of pages, set this parameter to a greater value. |
|---|---|---|---|---|
| RequestId | string | No | sdsdsdd | The request ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. Note The HTTP status code 200 indicates that the request succeeded. |
| Message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| PageNumber | String | 1 | The page number. |
| PageSize | String | 10 | The number of entries per page. |
| RequestId | String | 4C2061B2-3B1B- 43BF-A4A4- C53426F479C0 | The request ID. |
| Resources | Array | None | The information of services found. |
| Resource | N/A | None | The information of the service. |
| Description | String | CDN | The description of the service. |

|   |   |   |   |   |   | The tags of metrics. You can specify tags of metrics to filter services. A tag of a metric is used as a special mark of alerts triggered by the metric. For example, a tag can specify the service specification to which an alert belongs and whether an alert rule can be configured for a metric. The format is [{"name":"Tag name","value":"Tag |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | [{"name":"Tag name","value":"Tag |   |
|   |   |   |   |   |   | value"},{"name":"Tag |   |   |
|   |   |   |   |   |   | name","value":"Tag value"}] |   |   |
|   | Labels | String |   |   | [{"groupFlag":true }] |   |   |   |
|   | Namespace | String |   |   | acs cdn _ | The namespace of the service, which is used to distinguish between services. The typical value format is acs Abbreviation of the service _ name . |   |   |
|   |   |   |   |   |   |   | acs Abbreviation of the service _ |   |
|   |   |   |   |   |   | name |   |   |
|   | Success | Boolean |   |   | true | Indicates whether the request was successful. |   |   |

| Total | String | 12 | The total number of entries. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeProjectMeta &<Common request parameters>
```

Sample success responses

> **Note:** The response content varies with the services that are actually monitored.

`JSON` format `{`

```json
 "PageNumber":1,
 "PageSize":5,
 "RequestId":"4C2061B2-3B1B-43BF-A4A4-C53426F479C0",
 "Success":true,
 "Code":200,
 "Total":62,
 "Resources":{
  "Resource":[{
     "Description": "ECS",
     "Labels": "[{\"name\":\"product\",\"value\":\"ECS\"},
{\"name\":\"productCategory\",\"value\":\"ecs,ecs_net_interface,hpc_node,hpc_cluster\"}, {\"name\":\"groupFlag\",\"value\":\"true\"},{\"name\":\"cnName\",\"value\":\"ECS\"},{\" name\":\"enName\",\"value\":\"ECS\"}]",
     "Namespace": "acs_ecs_dashboard"
```

`},` `]` `}` `}`

#### 2.1.5 DescribeMetricData

Queries the monitoring data of a metric for a specified cloud service.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Namespac e | Strin g | Query | Yes | acs ecs dashboard _ _ | The namespace of the cloud service. For more information about the namespaces of cloud services, see Appendix 1: Metrics. |
| MetricNa me | Strin g | Query | Yes | cpu idle _ | The metric that is used to monitor the cloud service. For more information about the metrics of cloud services, see Appendix 1: Metrics. |
| Period | Strin g | Query | No | 60 | The statistical period of the metric. Valid values: 15, 60, 900, and 3600. Unit: seconds. If this parameter is not specified, monitoring data is queried based on the period in which metric values are reported. For more information about the statistical period of a metric that is specified by the MetricName parameter, see Appendix 1: Metrics. |
|   |   |   |   |   | The start of the time range to query monitoring data. If the StartTime and EndTime parameters are not specified, the monitoring data of the last statistical period is queried. |

| Parame ter | Typ e | Locati on | Require d | Example | If the StartTime Deasncdr i pEtnidoTnime |
|---|---|---|---|---|---|
|   |   |   |   |   | parameters are |
| StartTime | Strin g | Query | No | 1618368900000 | specified, the monitoring data of the last statistical period in the specified time range is queried. The following examples demonstrate how to determine the period in which monitoring data is queried: If you set the Period parameter to 15, the specified time range must be less than or equal to 20 minutes. For example, if you set the StartTime parameter to 2021- 05-08 08:10:00 and the EndTime parameter to 2021- 05-08 08:30:00, the monitoring data of the last 15 seconds in the time range is queried. If you set the Period parameter to 60 or 900, the specified time range must be less than or equal to 2 hours. For example, if you set the Period parameter to 60, the StartTime parameter to 2021- 05-08 08:00:00, and the EndTime parameter to 2021- 05-08 10:00:00, the monitoring data of the last 60 seconds in the time range is queried. |

|   | StartTime |
|---|---|
| i pEtnidoTnime |   |

| Parame ter | Typ e | Locati on | Require d | Example | If you set the Desc rPieprtiioodn parameter to 3600, |
|---|---|---|---|---|---|
|   |   |   |   |   | the specified time range must be less than or equal to two days. For example, if you set the StartTime parameter to 2021- 05-08 08:00:00 and the EndTime parameter to 2021- 05-10 08:00:00, the monitoring data of the last 3,600 seconds in the time range is queried. The following formats are supported: UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970. UTC time: the UTC time that follows the YYYY-MM- DDThh:mm:ssZ format. You must set the StartTime parameter to a point in time that is later than |
|   |   |   |   |   | 00:00:00 UTC on The eTnhdu orsf dtahye, time rangeJa tnou qaurye r1y, 1970. monitOotrhinegrw diastea, .this parameter is If thinev a liSdt.artTime and EndTime parameters are not We recommend that specified, the you use UNIX monitoring data of the timestamps to last statistical period prevent time zone- rise lqauteedri eisds.u e s. If the StartTime and EndTime parameters are specified, the monitoring data of the last statistical period in the specified time range is queried. The following examples demonstrate how to determine the period in which monitoring data is queried: |
| 7 |   |   |   | > Do | cument Version: 2026090 |

|   | a liSdt.artTime |
|---|---|
| EndTime |   |

| Parame ter | Typ e | Locati on | Require d | Example | If you set the Desc rPieprtiioodn parameter to 15, |
|---|---|---|---|---|---|
|   |   |   |   |   | the specified time range must be less than or equal to 20 minutes. For example, if you set the StartTime parameter to 2021- 05-08 08:10:00 and the EndTime |
| EndTime | Strin g | Query | No | 1618368960000 | parameter to 2021- 05-08 08:30:00, the monitoring data of the last 15 seconds in the time range is queried. If you set the Period parameter to 60 or 900, the specified time range must be less than or equal to 2 hours. For example, if you set the Period parameter to 60, the StartTime parameter to 2021- 05-08 08:00:00, and the EndTime parameter to 2021- 05-08 10:00:00, the monitoring data of the last 60 seconds in the time range is queried. If you set the Period parameter to 3600, the specified time range must be less than or equal to two days. For example, if you set the StartTime parameter to 2021- 05-08 08:00:00 and the EndTime parameter to 2021- 05-10 08:00:00, the monitoring data of the last 3,600 seconds in the time range is queried. The following formats are supported: |

|   | Parame ter | Typ e | Locati on | Require d |   | Example |   | UNIX timestamp: the Densucmrbipert ioofn milliseconds that |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | have elapsed since 00:00:00 Thursday, January 1, 1970. UTC time: the UTC time that follows the YYYY-MM- DDThh:mm:ssZ format. We recommend that you use UNIX timestamps to prevent time zone- related issues. |   |   |
|   | Dimension s | Strin g | Query | No |   | [{"instanceId": "i- abcdefgh12****"}] |   | The dimensions that specify the resources whose monitoring data you want to query. Set the value to a collection of key-value pairs. A typical key- value pair is instanceId:i- 2ze2d6j5uhg20x47**** . You can query a maximum of 50 instances in a single request. |   |   |
|   |   |   |   |   |   |   |   |   | instanceId:i- |   |
|   |   |   |   |   |   |   |   | 2ze2d6j5uhg20x47**** |   |   |
|   | Express | Strin g | Query | No |   | {"groupby": ["userId","instanceId"]} |   | The expression that is used to compute the query results in real time. Only the groupby expression is supported. This expression is similar to the GROUP BY statement that is used in databases. |   |   |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Length | Strin g | Query | No | 1000 | The number of entries per page. Default value: 1000. The maximum value of the Length parameter in a request is 1440. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |
| RequestId | String | 6A5F022D-AC7C- 460E-94AE- B9E75083D027 | The request ID. |
| Datapoints | String | [{\"timestamp\":16 18368900000,\"Av erage\":95.829166 6666667,\"Minimu m\":65.48,\"Maxim um\":100.0}, {\"timestamp\":16 18368960000,\"Av erage\":95.868333 3333333,\"Minimu m\":67.84,\"Maxim um\":100.0}] | The monitoring data. The value includes the following fields: timestamp : the time when the alert was triggered. userId : the ID of the user for which the alert was triggered. instanceId : the ID of the instance for which the alert was triggered. Minimum , Average , and Maximum : the aggregation methods. |
| Period | String | 60 | The statistical period of the monitoring data. Valid values: 15, 60, 900, and 3600. Unit: seconds. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricData &Namespace=acs_ecs_dashboard &MetricName=cpu_idle &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"6A5F022D-AC7C-460E-94AE-B9E75083D027",
 "Period":"60",
 "Datapoints":"
[{\\\"timestamp\\\":1618368900000,\\\"Average\\\":95.8291666666667,\\\"Minimum\\\":65.48, \"Maximum\\\":100.0}, {\\\"timestamp\\\":1618368960000,\\\"Average\\\":95.8683333333333,\\\"Minimum\\\":67.84,\ "Maximum\\\":100.0}]",
 "Code":"200"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.1.6 DescribeMetricTop

Queries the latest monitoring data of a metric for a cloud service. The data can be sorted by a specified order.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|

| Period | Strin g | Quer y | No | 60 | The statistical period of the monitoring data. Valid values: 15, 60, 900, and 3600. Unit: seconds. If this parameter is not specified, monitoring data is queried based on the period in which metric values are reported. Statistical periods vary based on the metrics that are specified by MetricName . For more information, see Appendix 1: Metrics. |
|---|---|---|---|---|---|
| Namespac e | Strin g | Quer y | Yes | acs ecs dashboard _ _ | The namespace of the cloud service. For more information about the namespaces of cloud services, see Appendix 1: Metrics. |
| MetricNam e | Strin g | Quer y | Yes | cpu idle _ | The metric that is used to monitor the cloud service. For more information about metric names, see Appendix 1: Metrics. |
|   |   |   |   |   | The start of the time range to query monitoring data. If the StartTime and EndTime parameters are not specified, the monitoring data of the last statistical period is queried. If the StartTime and EndTime parameters are specified, the monitoring data of the last statistical period in the specified time range is queried. The following examples demonstrate how to determine the period in which monitoring data is queried: |

|   | StartTime |
|---|---|
| EndTime |   |

|   | StartTime |
|---|---|
| EndTime |   |

|   |   |   |   |   | If you set the Period parameter to 15, the specified time range must be less than or equal to 20 minutes. For example, if you set the StartTime parameter to 2021- 05-08 08:10:00 and the EndTime parameter to 2021- |
|---|---|---|---|---|---|
| StartTime | Strin g | Quer y | No | 2021-05-08 08:00:00 | 05-08 08:30:00, the monitoring data of the last 15 seconds in the time range is queried. If you set the Period parameter to 60 or 900, the specified time range must be less than or equal to 2 hours. For example, if you set the Period parameter to 60, the StartTime parameter to 2021-05-08 08:00:00, and the EndTime parameter to 2021-05-08 10:00:00, the monitoring data of the last 60 seconds in the time range is queried. If you set the Period parameter to 3600, the specified time range must be less than or equal to two days. For example, if you set the StartTime parameter to 2021-05-08 08:00:00 and the EndTime parameter to 2021-05-10 08:00:00, the monitoring data of the last 3,600 seconds in the time range is queried. The following formats are supported: UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970. |

|   |   |   |   |   | UTC time: the UTC time that follows the YYYY- MM-DDThh:mm:ssZ format. You must set the StartTime parameter to a point in time that is later than 00:00:00 UTC on Thursday, January 1, 1970. Otherwise, this parameter is invalid. We recommend that you use UNIX timestamps to prevent time zone-related issues. |
|---|---|---|---|---|---|
|   |   |   |   |   | The end of the time range to query monitoring data. If the StartTime and EndTime parameters are not specified, the monitoring data of the last statistical period is queried. If the StartTime and EndTime parameters are specified, the monitoring data of the last statistical period in the specified time range is queried. The following examples demonstrate how to determine the period in which monitoring data is queried: |

|   | StartTime |
|---|---|
| EndTime |   |

|   | StartTime |
|---|---|
| EndTime |   |

|   |   |   |   |   | If you set the Period parameter to 15, the specified time range must be less than or equal to 20 minutes. For example, if you set the StartTime parameter to 2021- 05-08 08:10:00 and the EndTime parameter to 2021- 05-08 08:30:00, the monitoring data of the last 15 seconds |
|---|---|---|---|---|---|
| EndTime | Strin g | Quer y | No | 2021-05-08 10:00:00 | in the time range is queried. If you set the Period parameter to 60 or 900, the specified time range must be less than or equal to 2 hours. For example, if you set the Period parameter to 60, the StartTime parameter to 2021-05-08 08:00:00, and the EndTime parameter to 2021-05-08 10:00:00, the monitoring data of the last 60 seconds in the time range is queried. If you set the Period parameter to 3600, the specified time range must be less than or equal to two days. For example, if you set the StartTime parameter to 2021-05-08 08:00:00 and the EndTime parameter to 2021-05-10 08:00:00, the monitoring data of the last 3,600 seconds in the time range is queried. The following formats are supported: UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970. |

|   |   |   |   |   |   |   |   |   | UTC time: the UTC time that follows the YYYY- MM-DDThh:mm:ssZ format. We recommend that you use UNIX timestamps to prevent time zone- related issues. |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Dimension s | Strin g | Quer y |   | No | [{"instanceId": "i- 2ze2d6j5uhg20x47****"} ] |   |   | The monitoring dimensions of the specified resource. Set the value to a collection of key:value pairs. Examples: {"userId":"1208863178 61****"} and {"instanceId":"i- |   |   |   |
|   |   |   |   |   |   |   |   |   |   | {"userId":"1208863178 |   |   |
|   |   |   |   |   |   |   | 2d6j5uhg20x47****"} |   | 61****"} |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | and |   |
|   |   |   |   |   |   |   |   |   | 2ze2d6j5uhg20x47****"} |   |   |   |
|   | OrgId | Strin g | Quer y |   | No | 1 |   |   | The organization ID. |   |   |   |
|   | ResourceId | Strin g | Quer y |   | No |   |   |   | The resource ID. |   |   |   |
|   | Orderby | Strin g | Quer y |   | No | Average |   |   | The field based on which data is sorted. Valid values: Average Minimum Maximum |   |   |   |
|   | OrderDesc | Strin g | Quer y |   | No | False |   |   | The sorting method. Valid values: True: sorts data in ascending order. False (default): sorts data in descending order. |   |   |   |

| Length | Strin g | Quer y | No | 10 | The number of entries per page. Default value: 10. The maximum value of the Length parameter in a request is 1440. |
|---|---|---|---|---|---|
| Express | Strin g | Quer y | No | {"groupby": ["userId","instanceId"]} | The expression that is used to compute the query results in real time. Only the groupby expression is supported. This expression is similar to the GROUP BY statement that is used in databases. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |
| RequestId | String | 3121AE7D-4AFF- 4C25-8F1D- C8226EBB1F42 | The request ID. |

| Datapoints | String | [{\"order\":1,\"time stamp\":16202875 20000,\"userId\":\" 120886317861**** \",\"instanceId\":\"i- j6ccf7d5fn335qpo* ***\",\"Average\":9 9.92,\"Minimum\":9 9.5,\"Maximum\":1 00.0,\" count\":1.0 _ }, {\"order\":2,\"times tamp\":162028752 0000,\"userId\":\"1 20886317861****\" ,\"instanceId\":\"i- 0xii2bvf42iqvxbp** **\",\"Average\":99. 91,\"Minimum\":99. 0,\"Maximum\":100 .0,\" count\":1.0}] _ | The monitoring data. |
|---|---|---|---|
| Period | String | 60 | The statistical period of the monitoring data. Unit: seconds. Valid values: 15, 60, 900, and 3600. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| Total | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricTop &Namespace=acs_ecs_dashboard &MetricName=cpu_idle &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"3121AE7D-4AFF-4C25-8F1D-C8226EBB1F42",
 "PageSize":"",
 "PageNumber":"",
 "Total":"",
 "Period":"60",
 "Datapoints":"
[{\\\"order\\\":1,\\\"timestamp\\\":1620287520000,\\\"userId\\\":\\\"120886317861****\\\" \\"instanceId\\\":\\\"ij6ccf7d5fn335qpo****\\\",\\\"Average\\\":99.92,\\\"Minimum\\\":99.5,\\\"Maximum\\\":100.0 \\"_count\\\":1.0}, {\\\"order\\\":2,\\\"timestamp\\\":1620287520000,\\\"userId\\\":\\\"120886317861****\\\", \"instanceId\\\":\\\"i- 0xii2bvf42iqvxbp****\\\",\\\"Average\\\":99.91,\\\"Minimum\\\":99.0,\\\"Maximum\\\":100.0 \\"_count\\\":1.0}]",
 "Code":"200"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.1.7 DescribeMetricTopList

Queries the data of top metrics within a specified time period.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| 9 |   |   |   | > D | ocument Version: 2026090 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion |   | Required | Example |   |   | Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| StartTime | Strin g | Quer y |   | Yes | 1640608200000 |   |   | The start time when the alert takes effect. |   |   |   |
| EndTime | Strin g | Quer y |   | Yes | 1640608200000 |   |   | The end time when the alert takes effect. |   |   |   |
| Dimension s | Strin g | Quer y |   | No | [{"instanceId": "i- abcdefgh12****"}] |   |   | The monitoring dimensions of the specific resource. Format: a collection of key:value pairs, such as {"userId":"1208863178 61****"} and {"instanceId":"i- |   |   |   |
|   |   |   |   |   |   |   |   |   | {"userId":"1208863178 |   |   |
|   |   |   |   |   |   | instanceId": "i- cdefgh12****"}] |   | 61****"} |   |   |   |
|   |   |   |   |   |   |   |   |   |   | and |   |
|   |   |   |   |   |   |   |   | 2ze2d6j5uhg20x47****"} |   |   |   |
| OrgId | Strin g | Quer y |   | No | "" |   |   | The organization. |   |   |   |
| ResourceId | Strin g | Quer y |   | No | eas-r-asdasdasd**** |   |   | The resource ID. |   |   |   |
| Orderby | Strin g | Quer y |   | Yes | Average |   |   | The sort field. Valid values: Average: the average value Minimum: the minimum value Maximum: the maximum value |   |   |   |
| OrderDesc | Strin g | Quer y |   | No | False |   |   | The sort order. Valid values: True: ascending order False (default): descending order |   |   |   |

| Category | Strin g | Quer y | No | ecs | The abbreviation of the cloud product name. Valid values of N: 1 to 200. To obtain the abbreviation of the cloud product name, see the metricCategory field in the Labels response parameter of the DescribeProjectMeta API. |
|---|---|---|---|---|---|
| Period | Strin g | Quer y | No | 60 | The aggregation period of the monitoring data. Unit: seconds. The value must be an integer multiple of 60. The default value is the original reporting period of the monitoring data. |
| Namespac e | Strin g | Quer y | Yes | acs ecs dashboard _ _ | The data namespace of the product, which is used to distinguish different products. Naming convention: acs product name. For _ more information, see the cloud product monitoring items section. |
| MetricNam e | Strin g | Quer y | Yes | cpu total _ | The name of the monitoring item. For more information, see the cloud product monitoring items section. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID returned by the cloud product. |
| NextToken | String | IWBjqMYSy0is7zSM Gu16**** | The token used to query the next page. |

| Datapoints | String | - | The list of alert rules. |
|---|---|---|---|
| Period | String | 60 | The aggregation period of the monitoring data. Unit: seconds. The default value is the minimum frequency corresponding to the monitoring item, and you do not need to specify this parameter in most cases. |
| Success | Boolean | true | Indicates whether the operation succeeded. Valid values: true: The operation succeeded. false: The operation failed. |
| Code | String | 200 | The status code. A value of 200 indicates success. |
| Message | String | Success | The returned message. The system returns a success message when the request succeeds, and returns the failure cause when the request fails. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricTopList &Namespace=acs_ecs_dashboard &MetricName=cpu_total &StartTime=1640608200000 &EndTime=1640608200000 &Orderby=Average &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "Message":"The request succeeded.",
 "RequestId":"ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
 "NextToken":"IWBjqMYSy0is7zSMGu16****",
 "Period":"60",
 "Datapoints":"-",
 "Code":"404",
 "Success":true
```

`}`

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | The parameter is in valid. |
| 403 | 403 | AccessForbidden | You do not have the permissions to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 |   | InternalError | The system failed to process the request due to some unknown errors. |

#### 2.1.8 DescribeCloudProductResourceTypes

Queries the list of resource types that cloud products support.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request succeeded. Valid values: true (success) and false (failure). |
| Code | Integer | 200 | The HTTP status code. A value of 200 indicates success. |
| Message | String | successful | The response message. The system returns "successful" when the request succeeds. |
| Data | String | [{"productCode":"e cs","resourceType" :"instance"}] | The list of cloud product resource types in JSON array format. |

| RequestId | String | 15B664E7-1823- 4C84-A59B- 1A3B**** | The request ID. |
|---|---|---|---|

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 500 | 500 | InternalError | The system failed to process the request due to some unknown errors. |
| 400 | 400 | ParameterInvalid | The request parameter is invalid. |
| 401 | 401 | AccessDeniedException | You do not have sufficient permissions to perform this operation. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

### 2.2 Console view configuration

#### 2.2.1 DescribeConsoleViews

Queries the configuration information of Cloud Monitor (CMS) console views.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Quer y | No | 1 | The page number. The starting value is 1. |

| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Valid values: 1 to 100 |
|---|---|---|---|---|---|

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4C467B38-391A- 4321-9C36- 1234567890AB | The unique ID of the request. |
| Success | Boolean | true | Indicates whether the request is successful. |
| Code | String | 200 | The error code. The system returns this code when the request fails. |
| Message | String | sucess | The error message. The system returns this message when the request fails. |
|   |   | { "Data": { "Data": [ { "Output": " {\"version4 0\": _ {\"productListConfi g\": {\"tableConfig\": {\"dataSource\": {\"filter\": [{\"component\":\"I nput\",\"name\":\" _ InstanceName \", _ __ \"title\":{\"intl\": {\"zh TW\":\"執行個 _ 體名稱 \",\"en US\":\"Insta _ nce Name\",\"zh CN\":\ _ "Instance Name\",\"ja JP\":\" _ インスタンス名 \"}}}, {\"component\":\"I nput\",\"name\":\" _ InstanceId \",\"tit _ __ le\":{\"intl\": {\"zh TW\":\"執行個 _ 體 Id\",\"en US\":\"Inst _ ance ID\",\"zh CN\":\"Inst _ ance ID\",\"ja JP\":\"イン _ スタンス ID\"}}}],\"paginati on\": |   |

|   |   | {\"pageSizeList\": [10,20,50],\"localP agination\":false,\" pageSize\":10},\"c olumns\": [{\"dataIndex\":\" __ InstanceId \",\"titl __ e\":{\"intl\": {\"zh TW\":\"執行個 _ 體 \",\"en US\":\"Insta _ nce\",\"zh CN\":\"In _ stance\",\"ja JP\":\" _ 例\"}},\"render\": {\"icon\":\"rds\",\"ic onColor\":\"B20\",\" description\":\" {{record. Instanc __ eName }}\"}}, __ {\"dataIndex\":\"Or ganizationName\",\ |   |
|---|---|---|---|
|   |   | "title\":{\"intl\": {\"zh TW\":\"組織 _ \",\"en US\":\"Orga _ nization\",\"zh CN\" _ :\"Organization\",\"j a JP\":\"組織\"}}}, _ {\"dataIndex\":\"En gine\",\"title\": {\"intl\": {\"zh TW\":\"資料庫 _ 類型 \",\"en US\":\"DB _ Type\",\"zh CN\":\" _ Database Engine\",\"ja JP\":\" _ DB タイプ \"}},\"render\": {\"value\":\" {{JSON.parse(reco rd. Detail ).Engin __ __ e}}\"}}, {\"dataIndex\":\"Re sourceSetName\",\ "title\":{\"intl\": {\"zh TW\":\"資源群 _ 組 \",\"en US\":\"Reso _ urce Group\",\"zh CN\":\ _ "Resource Set\",\"ja JP\":\"リ _ ソースグループ \"}}}, {\"dataIndex\":\"D BInstanceStatus\",\ "title\":{\"intl\": {\"zh TW\":\"運行狀 _ 態 \",\"en US\":\"Statu _ s\",\"zh CN\":\"Stat _ us\",\"ja JP\":\"ス _ テータス \"}},\"dataSource\" :[{\"label\": {\"intl\": |   |

|   |   | {\"zh TW\":\"建立中 _ \",\"en US\":\"Creat _ ing\",\"zh CN\":\"Cr _ eating\",\"ja JP\":\" _ 作成中 \"}},\"value\":\"CR EATING\"}, {\"label\":{\"intl\": {\"zh TW\":\"運行中 _ \",\"en US\":\"Runni _ ng\",\"zh CN\":\"Ru _ nning\",\"ja JP\":\" _ 実行中 \"}},\"value\":\"RU NNING\"}, {\"label\":{\"intl\": {\"zh TW\":\"刪除中 _ \",\"en US\":\"Delet _ ing\",\"zh CN\":\"D _ eleting\",\"ja JP\":\" _ 削除中 \"}},\"value\":\"DEL ETING\"},{\"label\": {\"intl\": {\"zh TW\":\"重啟中 _ \",\"en US\":\"Rebo _ oting\",\"zh CN\":\" _ Rebooting\",\"ja JP\ _ ":\"再起動中 \"}},\"value\":\"RE BOOTING\"}, {\"label\":{\"intl\": {\"zh TW\":\"升降級 _ 中 \",\"en US\":\"Upgr _ ading or degrading\",\"zh C _ N\":\"Upgrading or Downgrading\",\"ja JP\":\"アップグレー _ ドまたはダウング レードしています \"}},\"value\":\"DBI NSTANCECLASSCH ANGING\"}, {\"label\":{\"intl\": {\"zh TW\":\"恢複中 _ \",\"en US\":\"Reco _ vering\",\"zh CN\":\ _ "Recovering\",\"ja J _ P\":\"リカバリを進め ています \"}},\"value\":\"TR ANSING\"}, {\"label\":{\"intl\": {\"zh TW\":\"內外網 _ 切換中 \",\"en US\":\"Switc _ hing between intranet and the Internet\",\"zh CN\" _ :\"Switching Between Intranet and Internet\",\"ja JP\":\ _ "イントラネットとイ |   |
|---|---|---|---|

|   |   | ンターネットを切り 替えています \"}},\"value\":\"EN GINEVERSIONUPGR ADING\"}, {\"label\":{\"intl\": {\"zh TW\":\"備份恢 _ 複中 \",\"en US\":\"Back _ up recovering\",\"zh C _ N\":\"Backup and Restoration in Progress\",\"ja JP\": _ \"バックアップしてい ます \"}},\"value\":\"RES TORING\"}, {\"label\":{\"intl\": {\"zh TW\":\"數據匯 _ 入中 \",\"en US\":\"Impo _ rting data\",\"zh CN\":\"I _ mporting Data\",\"ja JP\":\"デ _ ータをインポート中 \"}},\"value\":\"IMP ORTING\"}, {\"label\":{\"intl\": {\"zh TW\":\"從其他 _ RDS執行個體導入數據中 \",\"en US\":\"Impo _ rting data from other RDS instances\",\"zh CN _ \":\"Importing Data from Other RDS Instances\",\"ja JP\" _ :\"他の RDS インス タンスからデータを インポートしていま す \"}},\"value\":\"IMP ORTINGFROMOTHE RS\"},{\"label\": {\"intl\": {\"zh TW\":\"內外網 _ 切換中 \",\"en US\":\"Switc _ hing between intranet and the Internet\",\"zh CN\" _ :\"Switching Between Intranet and Internet\",\"ja JP\":\ _ "イントラネットとパ ブリックネットワー クを切り替えていま す \"}},\"value\":\"DBI NSTANCENETTYPE CHANGING\"}, {\"label\":{\"intl\": |   |
|---|---|---|---|

|   |   | {\"zh TW\":\"容災切 _ 換中 \",\"en US\":\"Switc _ hing to disaster recovery\",\"zh CN\ _ ":\"DR Failover in Progress\",\"ja JP\": _ \"障害復旧を切り替え ています \"}},\"value\":\"GU ARDSWITCHING\"}, {\"label\":{\"intl\": {\"zh TW\":\"SLL修 _ 改\",\"en US\":\"SLL _ modification\",\"zh _ CN\":\"SSL Modifying\",\"ja JP\ _ ":\"SLLの変更 \"}},\"value\":\"SSL MODIFYING\"}, _ {\"label\":{\"intl\": {\"zh TW\":\"網絡創 _ 建 \",\"en US\":\"Netw _ ork creation\",\"zh CN\ _ ":\"Network Creating\",\"ja JP\": _ \"ネットワーク作成 \"}},\"value\":\"NE T CREATING\"}, _ {\"label\":{\"intl\": {\"zh TW\":\"帳戶模 _ 式升級 \",\"en US\":\"Acco _ unt mode upgrade\",\"zh CN\ _ ":\"Account Mode Upgrading\",\"ja JP\ _ ":\"アカウントモード のアップグレード \"}},\"value\":\"AC COUNT MODE UPG _ _ RADING\"}, {\"label\":{\"intl\": {\"zh TW\":\"內部克 _ 隆 \",\"en US\":\"Inter _ nal cloning\",\"zh CN\": _ \"Internal Cloning\",\"ja JP\":\ _ "内部クローニング \"}},\"value\":\"INS CLONING\"}],\"ren _ der\":{\"value\":\" {{ () => JSON.parse(record. Detail ).DBInsta __ __ nceStatus.toLocale UpperCase() }}\"}}, {\"dataIndex\":\"D BInstanceNetType\ ",\"title\":{\"intl\": {\"zh TW\":\"網路 _ |   |
|---|---|---|---|

|   |   | \",\"en US\":\"Netw _ ork\",\"zh CN\":\"N _ etwork\",\"ja JP\":\" _ ネットワーク \"}},\"dataSource\" :[{\"label\": {\"intl\": {\"zh TW\":\"公網 _ \",\"en US\":\"Inter _ net\",\"zh CN\":\"Int _ ernet\",\"ja JP\":\"イ _ ンターネット \"}},\"value\":\"INT ERNET\"}, {\"label\":{\"intl\": {\"zh TW\":\"內網 _ \",\"en US\":\"Intra _ net\",\"zh CN\":\"Int _ ranet\",\"ja JP\":\"イ _ ントラネット \"}},\"value\":\"INT RANET\"}],\"render \":{\"value\":\"{{ () => JSON.parse(record. Detail ).DBInsta __ __ nceNetType.toLoca leUpperCase() }}\"}}, {\"dataIndex\":\"cp u.Average\",\"title\" :{\"intl\": {\"zh TW\":\"CPU使 _ 用率 \",\"en US\":\"CPU _ Utilization\",\"zh C _ N\":\"CPU Utilization\",\"ja JP\ _ ":\"CPU 使用率 \"}},\"render\": {\"unit\":\"%\",\"isE mphasize\":true,\"v alue\":\"{{ (val) => val ? Number(val ?? 0).toFixed(2) : '-' }}\"}}, {\"dataIndex\":\"m emory.Average\",\" title\":{\"intl\": {\"zh TW\":\"記憶體 _ 使用量率 \",\"en US\":\"Mem _ ory Usage\",\"zh CN\":\ _ "Memory Utilization\",\"ja JP\ _ ":\"メモリ使用率 \"}},\"render\": {\"unit\":\"%\",\"isE mphasize\":true,\"v alue\":\"{{ (val) => val ? Number(val ?? 0).toFixed(2) : '-' }}\"}}, |   |
|---|---|---|---|

|   |   | {\"dataIndex\":\"dis k.Average\",\"title\" :{\"intl\": {\"zh TW\":\"磁盤使 _ 用率 \",\"en US\":\"DiskU _ tilization\",\"zh CN\ _ ":\"Disk Utilization\",\"ja JP\ _ ":\"ディスク使用量 \"}},\"render\": {\"unit\":\"%\",\"isE mphasize\":true,\"v alue\":\"{{ (val) => val ? Number(val ?? 0).toFixed(2) : '-' }}\"}}],\"actions\": [{\"request\": {\"product\":\"asc m\",\"action\":\"Dat aCenterSearch\",\" params\": {\"resourceTypes\" : [\"rds instance\"],\" _ organizationIds\": [\" {{context.Organiz ationIds}}\"],\"retu rnInstanceDetail\":\ "true\",\"sortField\" :\" CreateTime \" __ __ ,\"pageSize\":\" {{context.PageSiz e}}\",\"regionIds\": [\" {{context.Region} }\"],\"page\":\" {{context.PageNu mber}}\",\"type\":\ "Instance\"},\"versi on\":\"2019-05- 10\"},\"format\": {\"totalPath\":\"tot al\",\"dataPath\":\" details\"},\"actions\ ":[{\"request\": {\"product\":\"cms\ ",\"action\":\"Descri beMetricLast\",\"pa rams\": {\"MetricName\":\" CpuUsage\",\"Dime nsions\": [{\"instanceId\":\" {{record. Instanc __ eId }}\"}],\"Name __ space\":\"acs rds d _ _ ashboard\"},\"versi on\":\"2019-01- 01\"},\"requestCon fig\": {\"combo\":true},\" format\": {\"comboInterface |   |
|---|---|---|---|

|   |   | PrimaryKey\":\"inst anceId\",\"extendP ath\":\"cpu\",\"main InterfacePrimaryKe y\":\" InstanceId __ __ \",\"dataPath\":\"Da tapoints\"}}, {\"request\": {\"product\":\"cms\ ",\"action\":\"Descri beMetricLast\",\"pa rams\": {\"MetricName\":\" MemoryUsage\",\" Dimensions\": [{\"instanceId\":\" {{record. Instanc __ eId }}\"}],\"Name __ space\":\"acs rds d _ _ ashboard\"},\"versi on\":\"2019-01- 01\"},\"requestCon fig\": {\"combo\":true},\" format\": {\"comboInterface PrimaryKey\":\"inst anceId\",\"extendP ath\":\"memory\",\" mainInterfacePrim aryKey\":\" Instan __ ceId \",\"dataPath __ \":\"Datapoints\"}}, {\"request\": {\"product\":\"cms\ ",\"action\":\"Descri beMetricLast\",\"pa rams\": {\"MetricName\":\" DiskUsage\",\"Dime nsions\": [{\"instanceId\":\" {{record. Instanc __ eId }}\"}],\"Name __ space\":\"acs rds d _ _ ashboard\"},\"versi on\":\"2019-01- 01\"},\"requestCon fig\": {\"combo\":true},\" format\": {\"comboInterface PrimaryKey\":\"inst anceId\",\"extendP ath\":\"disk\",\"mai nInterfacePrimaryK ey\":\" InstanceId __ _ \",\"dataPath\":\"D _ atapoints\"}}]}]}} },\"baseProductCo nfig\": {\"instanceDataKe y\":\" InstanceId __ __ \",\"isMetamonSup ported\":true,\"nam espace\":\"acs rds _ _ |   |
|---|---|---|---|

|   |   | dashboard\",\"asc mCategory\":\"rds\ ",\"appGroupCateg ory\":\"RDS 1\",\ ____ "metricInstanceKey \":\"instanceId\",\"d imensionsIncludeR egion\":false,\"cate gory\":\"rds\",\"intl\ ":{\"intl\": {\"zh TW\":\"Apsar _ aDB RDS\",\"en US\":\"A _ psaraDB RDS\",\"zh CN\":\"A _ psaraDB RDS\",\"ja JP\":\"Ap _ saraDB RDS\"}},\"helperD oc\": {\"metricCode\":\" DOC.EMBED.CMS.3 \"},\"instanceData Desc\":\" Instance __ Name \"},\"produ __ ctDetailConfig\": {\"tabList\": [{\"subTabList\": [{\"subTabListIntl\" :{\"intl\": {\"zh TW\":\"執行個 _ 體 \",\"en US\":\"Insta _ nces\",\"zh CN\":\"I _ nstances\",\"ja JP\": _ \"インスタンスリスト \"}},\"sectionList\": [{\"sectionChartLis t\":[{\"chartList\": [{\"chartIntl\": {\"intl\": {\"zh TW\":\"磁盤使 _ 用率 \",\"en US\":\"Disk _ Usage\",\"zh CN\":\ _ "Disk Utilization\",\"ja JP\ _ ":\"ディスク使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "DiskUsage\",\"met ricIntl\":{\"intl\": {\"zh TW\":\"硬碟使 _ 用 \",\"en US\":\"Disk _ Usage\",\"zh CN\":\ _ "Disk |   |
|---|---|---|---|

|   |   | Usage\",\"ja JP\":\" _ ディスク使用量 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\":{\"Engine\": [\"MySQL\",\"SQLSe rver\",\"POLARDB\" ]},\"chartGroupBy\ ":[]},{\"chartIntl\": {\"intl\": {\"zh TW\":\"IOPS _ 使用率 \",\"en US\":\"IOPS _ Usage\",\"zh CN\":\ _ "IOPS Utilization\",\"ja JP\ _ ":\"IOPS 使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "IOPSUsage\",\"met ricIntl\":{\"intl\": {\"zh TW\":\"IOPS _ 使用率 \",\"en US\":\"IOPS _ Usage\",\"zh CN\":\ _ "IOPS Utilization\",\"ja JP\ _ ":\"IOPS 使用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\":{\"Engine\": [\"MySQL\",\"SQLSe rver\",\"POLARDB\" ]},\"chartGroupBy\ ":[]},{\"chartIntl\": {\"intl\": {\"zh TW\":\"串連數 _ 使用率 \",\"en US\":\"Conn _ ections Usage\",\"zh CN\":\ _ "Connection Usage\",\"ja JP\":\" _ 接続使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ |   |
|---|---|---|---|

|   |   | "ConnectionUsage\ ",\"metricIntl\": {\"intl\": {\"zh TW\":\"串連數 _ 使用率 \",\"en US\":\"Conn _ ections Usage\",\"zh CN\":\ _ "Connection Usage\",\"ja JP\":\" _ 接続使用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\":{\"Engine\": [\"MySQL\",\"SQLSe rver\",\"POLARDB\" ]},\"chartGroupBy\ ":[]},{\"chartIntl\": {\"intl\": {\"zh TW\":\"CPU使 _ 用率 \",\"en US\":\"CPU _ Utilization\",\"zh C _ N\":\"CPU Utilization\",\"ja JP\ _ ":\"CPU 使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "CpuUsage\",\"met ricIntl\":{\"intl\": {\"zh TW\":\"CPU使 _ 用率 \",\"en US\":\"CPU _ Utilization\",\"zh C _ N\":\"CPU Utilization\",\"ja JP\ _ ":\"CPU 使用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\":{\"Engine\": [\"MySQL\",\"SQLSe rver\",\"POLARDB\" ]},\"chartGroupBy\ ":[]},{\"chartIntl\": {\"intl\": {\"zh TW\":\"記憶體 _ 使用量率 \",\"en US\":\"Mem _ ory Usage\",\"zh CN\":\ _ "Memory Utilization\",\"ja JP\ _ ":\"メモリ使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic |   |
|---|---|---|---|

|   |   | s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "MemoryUsage\",\" metricIntl\": {\"intl\": {\"zh TW\":\"記憶體 _ 使用量率 \",\"en US\":\"Mem _ ory Usage\",\"zh CN\":\ _ "Memory Utilization\",\"ja JP\ _ ":\"メモリ使用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\":{\"Engine\": [\"MySQL\",\"POLAR DB\",\"SQLServer\"] },\"chartGroupBy\": []},{\"chartIntl\": {\"intl\": {\"zh TW\":\"MySQ _ L網路入流量 \",\"en US\":\"MySQ _ L Network Inbound Traffic\",\"zh CN\":\ _ "MySQL Inbound Traffic\",\"ja JP\":\" _ MySQL ネットワーク インバウンド交通 \"}},\"chartUnit\":\" bits/s\",\"chartStati stics\": [\"Average\",\"Mini mum\",\"Maximum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Mini mum\",\"Maximum\ "],\"metricName\":\ "MySQL NetworkIn _ New\",\"metricIntl\" :{\"intl\": {\"zh TW\":\"MySQ _ L網路入流量 \",\"en US\":\"MySQ _ L Network Inbound Traffic\",\"zh CN\":\ _ "MySQL Inbound Traffic\",\"ja JP\":\" _ MySQL ネットワーク インバウンド交通 \"}},\"metricUnit\": \"bits/s\"}],\"chartT ype\":\"line\",\"sho wProps\": {\"Engine\": |   |
|---|---|---|---|

|   |   | [\"MySQL\"]},\"char tGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"MySQ _ L網路出流量 \",\"en US\":\"MySQ _ L Network Outbound Traffic\",\"zh CN\":\ _ "MySQL Outbound Traffic\",\"ja JP\":\" _ MySQL ネットワーク アウトバウンド交通 \"}},\"chartUnit\":\" bits/s\",\"chartStati stics\": [\"Average\",\"Mini mum\",\"Maximum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Mini mum\",\"Maximum\ "],\"metricName\":\ "MySQL NetworkO _ utNew\",\"metricInt l\":{\"intl\": {\"zh TW\":\"MySQ _ L網路出流量 \",\"en US\":\"MySQ _ L Network Outbound Traffic\",\"zh CN\":\ _ "MySQL Outbound Traffic\",\"ja JP\":\" _ MySQL ネットワーク アウトバウンド交通 \"}},\"metricUnit\": \"bits/s\"}],\"chartT ype\":\"line\",\"sho wProps\": {\"Engine\": [\"MySQL\"]},\"char tGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"MySql _ 每秒查詢量 \",\"en US\":\"MySq _ l queries per second\",\"zh CN\": _ \"MySQL QPS\",\"ja JP\":\"1秒 _ あたりのmysqlクエ リ \"}},\"chartUnit\":\" count/s\",\"chartSta tistics\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"MySQL QPS\",\"metricIntl\ _ |   |
|---|---|---|---|

| Resource | Struct | ":{\"intl\": {\"zh TW\":\"MySql _ 每秒查詢量 \",\"en US\":\"MySq _ l queries per second\",\"zh CN\": _ \"MySQL QPS\",\"ja JP\":\"1秒 _ あたりのmysqlクエ リ \"}},\"metricUnit\": \"count/s\"}],\"char tType\":\"line\",\"sh owProps\": {\"Engine\": [\"MySQL\"]},\"char tGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"データ _ ベースエージェント- CPUの使用率 \",\"en US\":\"Dock _ er Cpu Usage\",\"zh CN\":\ _ "Database Proxy CPU Utilization\",\"ja JP\ _ ":\"Docker CPU使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"Docker CpuUsage\",\"metri cIntl\":{\"intl\": {\"zh TW\":\"データ _ ベースエージェント- CPUの使用率 \",\"en US\":\"Dock _ er Cpu Usage\",\"zh CN\":\ _ "Database Proxy CPU Utilization\",\"ja JP\ _ ":\"Docker CPU使用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\":{\"Engine\": [\"MySQL\"]},\"char tGroupBy\": [\"type\"]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"SQLS _ erver網路入流量 \",\"en US\":\"SQL _ Server network inbound | Resource data container |
|---|---|---|---|

|   |   | traffic\",\"zh CN\":\ _ "SQL Server Inbound Traffic\",\"ja JP\":\" _ SQL Server ネット ワークインバウンド 交通 \"}},\"chartUnit\":\" bits/s\",\"chartStati stics\": [\"Average\",\"Mini mum\",\"Maximum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Mini mum\",\"Maximum\ "],\"metricName\":\ "SQLServer Networ _ kInNew\",\"metricIn tl\":{\"intl\": {\"zh TW\":\"SQLS _ erver網路入流量 \",\"en US\":\"SQL _ Server network inbound traffic\",\"zh CN\":\ _ "SQL Server Inbound Traffic\",\"ja JP\":\" _ SQL Server ネット ワークインバウンド 交通 \"}},\"metricUnit\": \"bits/s\"}],\"chartT ype\":\"line\",\"sho wProps\": {\"Engine\": [\"SQLServer\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"SQLS _ erver網路出流量 \",\"en US\":\"SQL _ Server network outbound traffic\",\"zh CN\":\ _ "SQL Server Outbound Traffic\",\"ja JP\":\" _ SQL Server ネット ワークアウトバウン ド交通 \"}},\"chartUnit\":\" bits/s\",\"chartStati stics\": [\"Average\",\"Mini mum\",\"Maximum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Mini mum\",\"Maximum\ "],\"metricName\":\ "SQLServer Networ _ |   |
|---|---|---|---|

|   |   | kOutNew\",\"metric Intl\":{\"intl\": {\"zh TW\":\"SQLS _ erver網路出流量 \",\"en US\":\"SQL _ Server network outbound traffic\",\"zh CN\":\ _ "SQL Server Outbound Traffic\",\"ja JP\":\" _ SQL Server ネット ワークアウトバウン ド交通 \"}},\"metricUnit\": \"bits/s\"}],\"chartT ype\":\"line\",\"sho wProps\": {\"Engine\": [\"SQLServer\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"每CPU _ 平均活躍連接數 PG _ 雲盤 \",\"en US\":\"Aver _ age active connections per CPU PG cloud _ disk\",\"zh CN\":\"A _ verage Active Connections per CPU PG Cloud _ Disk\",\"ja JP\":\"Cp _ u pgクラウドディス _ クあたりの平均アク ティブ接続 \"}},\"chartUnit\":\" Count\",\"chartStati stics\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"Active Connections\",\"me tricIntl\":{\"intl\": {\"zh TW\":\"每CPU _ 平均活躍連接數 PG _ 雲盤 \",\"en US\":\"Aver _ age active connections per CPU PG cloud _ disk\",\"zh CN\":\"A _ verage Active Connections per CPU PG Cloud _ Disk\",\"ja JP\":\"Cp _ u pgクラウドディス _ クあたりの平均アク ティブ接続 \"}},\"metricUnit\": \"Count\"}],\"chart |   |
|---|---|---|---|

|   |   | Type\":\"line\",\"sh owProps\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"INOD _ E使用率 PG雲端硬碟 _ \",\"en US\":\"Inode _ Usage PG _ Disk\",\"zh CN\":\"I _ node Utilization PG _ Cloud Disk\",\"ja JP\":\"IN _ ODE 使用率 PG ク _ ラウドディスク \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"InodeU sage\",\"metricIntl\ ":{\"intl\": {\"zh TW\":\"INOD _ E使用率 PG雲端硬碟 _ \",\"en US\":\"Inode _ Usage PG _ Disk\",\"zh CN\":\"I _ node Utilization PG _ Cloud Disk\",\"ja JP\":\"IN _ ODE 使用率 PG ク _ ラウドディスク \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"只讀同 _ 步延遲 PG雲盤 _ \",\"en US\":\"Read _ -only synchronization delay PG cloud _ disk\",\"zh CN\":\"R _ ead-Only Synchronization Delay PG Cloud _ Disk\",\"ja JP\":\"読 _ み取り専用同期 delay pgクラウド _ |   |
|---|---|---|---|

|   |   | ディスク \"}},\"chartUnit\":\" Second\",\"chartSta tistics\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"ReadL ag\",\"metricIntl\": {\"intl\": {\"zh TW\":\"只讀同 _ 步延遲 PG雲盤 _ \",\"en US\":\"Read _ -only synchronization delay PG cloud _ disk\",\"zh CN\":\"R _ ead-Only Synchronization Delay PG Cloud _ Disk\",\"ja JP\":\"読 _ み取り専用同期 delay pgクラウド _ ディスク \"}},\"metricUnit\": \"Second\"}],\"char tType\":\"line\",\"sh owProps\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"資料庫 _ 年齡 PG雲端硬碟 _ \",\"en US\":\"Data _ base Age PG _ Disk\",\"zh CN\":\"D _ atabase Age PG _ Cloud Disk\",\"ja JP\":\"Da _ tabase Age PG クラ _ ウドディスク \"}},\"chartUnit\":\" xids\",\"chartStatist ics\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"DBAge \",\"metricIntl\": {\"intl\": {\"zh TW\":\"資料庫 _ 年齡 PG雲端硬碟 _ \",\"en US\":\"Data _ base Age PG _ Disk\",\"zh CN\":\"D _ atabase Age PG _ Cloud |   |
|---|---|---|---|

|   |   | Disk\",\"ja JP\":\"Da _ tabase Age PG クラ _ ウドディスク \"}},\"metricUnit\": \"xids\"}],\"chartTy pe\":\"line\",\"show Props\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"只讀流 _ 複製狀態 PG雲盤 _ \",\"en US\":\"Read _ -only Stream replication state pg cloud _ disk\",\"zh CN\":\"R _ ead-Only Streaming Replication Status PG Cloud _ Disk\",\"ja JP\":\"読 _ み取り専用ストリー ム複製state pgクラ _ ウドディスク \"}},\"chartUnit\":\" value\",\"chartStati stics\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"Stream ingStatus\",\"metri cIntl\":{\"intl\": {\"zh TW\":\"只讀流 _ 複製狀態 PG雲盤 _ \",\"en US\":\"Read _ -only Stream replication state pg cloud _ disk\",\"zh CN\":\"R _ ead-Only Streaming Replication Status PG Cloud _ Disk\",\"ja JP\":\"読 _ み取り専用ストリー ム複製state pgクラ _ ウドディスク \"}},\"metricUnit\": \"value\"}],\"chartT ype\":\"line\",\"sho wProps\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, |   |
|---|---|---|---|

|   |   | {\"chartIntl\": {\"intl\": {\"zh TW\":\"PG 連 _ _ 接數使用率 \",\"en US\":\"Pg c _ _ onnection usage\",\"zh CN\":\ _ "PG Connection _ Usage\",\"ja JP\":\"P _ g connectionの使用 _ 法 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"conn u _ sage\",\"metricIntl\ ":{\"intl\": {\"zh TW\":\"Conn _ _ usage\",\"en US\":\ _ "conn usage\",\"zh _ CN\":\"conn usage _ _ \",\"ja JP\":\"Conn _ _ usage\"}},\"metric Unit\":\"%\"}],\"cha rtType\":\"line\",\"s howProps\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"PG CP _ _ U使用率 \",\"en US\":\"PG C _ _ PU usage\",\"zh CN\":\ _ "PG CPU _ Utilization\",\"ja JP\ _ ":\"Pg cpu使用率 _ \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Value\"],\" chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Value\"],\" metricName\":\"cp u usage\",\"metricI _ ntl\":{\"intl\": {\"zh TW\":\"PG CP _ _ U使用率 \",\"en US\":\"PG C _ _ PU usage\",\"zh CN\":\ _ "PG CPU _ |   |
|---|---|---|---|

|   |   | Utilization\",\"ja JP\ _ ":\"Pg cpu使用率 _ \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"PG IO _ _ PS使用率 \",\"en US\":\"PG I _ _ OPS usage\",\"zh CN\":\ _ "PG IOPS _ Utilization\",\"ja JP\ _ ":\"Pg iopsの使用法 _ \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"iops us _ age\",\"metricIntl\": {\"intl\": {\"zh TW\":\"PG IO _ _ PS使用率 \",\"en US\":\"PG I _ _ OPS usage\",\"zh CN\":\ _ "PG IOPS _ Utilization\",\"ja JP\ _ ":\"Pg iopsの使用法 _ \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"PG 磁 _ _ 盤空間使用率 \",\"en US\":\"Pg di _ _ sk space usage\",\"zh CN\":\ _ "PG Disk Space _ Usage\",\"ja JP\":\"P _ g diskスペース使用 _ 量 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\"],\"cha |   |
|---|---|---|---|

|   |   | rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"local fs _ size usage\",\"me _ _ tricIntl\":{\"intl\": {\"zh TW\":\"PG 磁 _ _ 盤空間使用率 \",\"en US\":\"Pg di _ _ sk space usage\",\"zh CN\":\ _ "PG Disk Space _ Usage\",\"ja JP\":\"P _ g diskスペース使用 _ 量 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"PG 記 _ _ 憶體使用率 \",\"en US\":\"PG _ Memory Usage\",\"zh CN\":\ _ "PG Memory _ Utilization\",\"ja JP\ _ ":\"PG Memory Usage\"}},\"chartU nit\":\"%\",\"chartSt atistics\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"mem u _ sage\",\"metricIntl\ ":{\"intl\": {\"zh TW\":\"PG 記 _ _ 憶體使用率 \",\"en US\":\"PG _ Memory Usage\",\"zh CN\":\ _ "PG Memory _ Utilization\",\"ja JP\ _ ":\"PG Memory Usage\"}},\"metric Unit\":\"%\"}],\"cha rtType\":\"line\",\"s howProps\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": |   |
|---|---|---|---|

|   |   | {\"intl\": {\"zh TW\":\"磁盤使 _ 用率 \",\"en US\":\"Disk _ Usage\",\"zh CN\":\ _ "Disk Utilization\",\"ja JP\ _ ":\"ディスク使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "DiskUsage\",\"met ricIntl\":{\"intl\": {\"zh TW\":\"硬碟使 _ 用 \",\"en US\":\"Disk _ Usage\",\"zh CN\":\ _ "Disk Usage\",\"ja JP\":\" _ ディスク使用量 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"local ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"IOPS _ 使用率 \",\"en US\":\"IOPS _ Usage\",\"zh CN\":\ _ "IOPS Utilization\",\"ja JP\ _ ":\"IOPS 使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "IOPSUsage\",\"met ricIntl\":{\"intl\": {\"zh TW\":\"IOPS _ 使用率 \",\"en US\":\"IOPS _ Usage\",\"zh CN\":\ _ "IOPS Utilization\",\"ja JP\ _ |   |
|---|---|---|---|

|   |   | ":\"IOPS 使用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"local ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"串連數 _ 使用率 \",\"en US\":\"Conn _ ections Usage\",\"zh CN\":\ _ "Connection Usage\",\"ja JP\":\" _ 接続使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "ConnectionUsage\ ",\"metricIntl\": {\"intl\": {\"zh TW\":\"串連數 _ 使用率 \",\"en US\":\"Conn _ ections Usage\",\"zh CN\":\ _ "Connection Usage\",\"ja JP\":\" _ 接続使用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"local ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"CPU使 _ 用率 \",\"en US\":\"CPU _ Utilization\",\"zh C _ N\":\"CPU Utilization\",\"ja JP\ _ ":\"CPU 使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi |   |
|---|---|---|---|

|   |   | mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "CpuUsage\",\"met ricIntl\":{\"intl\": {\"zh TW\":\"CPU使 _ 用率 \",\"en US\":\"CPU _ Utilization\",\"zh C _ N\":\"CPU Utilization\",\"ja JP\ _ ":\"CPU 使用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"local ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"記憶體 _ 使用量率 \",\"en US\":\"Mem _ ory Usage\",\"zh CN\":\ _ "Memory Utilization\",\"ja JP\ _ ":\"メモリ使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "MemoryUsage\",\" metricIntl\": {\"intl\": {\"zh TW\":\"記憶體 _ 使用量率 \",\"en US\":\"Mem _ ory Usage\",\"zh CN\":\ _ "Memory Utilization\",\"ja JP\ _ ":\"メモリ使用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"local ssd\"],\"En _ gine\": |   |
|---|---|---|---|

|   |   | [\"PostgreSQL\"]},\" chartGroupBy\": []}]}],\"sectionIntl\" :{\"intl\": {}}}],\"dimensions Key\": [\"region\",\"instan ceId\"]}, {\"subTabListIntl\": {\"intl\": {\"zh TW\":\"慢 _ SQL\",\"en US\":\"S _ low SQL\",\"zh CN\":\"Sl _ ow SQL Query\",\"ja JP\":\" _ 慢 SQL\"}},\"sectionLi st\": [{\"sectionIntl\": {\"intl\": {}},\"sectionModul e\": {\"moduleResourc e\":[\" {{CDN DOMAIN}}/ _ teamix- components/rds- slow- sql/{{VERSION}}/ modules/rds-slow- sql.css\",\" {{CDN DOMAIN}}/ _ teamix- components/rds- slow- sql/{{VERSION}}/ modules/rds-slow- sql.js\"],\"moduleV ersion\":\"3.16.2\",\ "moduleName\":\"R dsSlowSql\",\"modu leParams\": {\"instanceId\":\" {{ InstanceId }} __ __ \"}}}]}],\"tabListInt l\":{\"intl\": {\"zh TW\":\"執行個 _ 體 \",\"en US\":\"Insta _ nces\",\"zh CN\":\"I _ nstances\",\"ja JP\": _ \"インスタンスリスト \"}}}]}}}", "ProductCategory": "rds" }]}} |   |
|---|---|---|---|
|   |   | { "Data": [ { "Output": " {\"version4 0\": _ {\"productListConfi g\": {\"tableConfig\": {\"dataSource\": {\"filter\": |   |

| Developer Guide·A | PI Reference |   | CloudMonito |
|---|---|---|---|
|   |   | [{\"component\":\"I nput\",\"name\":\" _ InstanceName \", _ __ \"title\":{\"intl\": {\"zh TW\":\"執行個 _ 體名稱 \",\"en US\":\"Insta _ nce Name\",\"zh CN\":\ _ "实例名称 \",\"ja JP\":\"インス _ タンス名\"}}}, {\"component\":\"I nput\",\"name\":\" _ InstanceId \",\"tit _ __ le\":{\"intl\": {\"zh TW\":\"執行個 _ 體 Id\",\"en US\":\"Inst _ ance ID\",\"zh CN\":\"实 _ 例Id\",\"ja JP\":\"イ _ ンスタンス ID\"}}}],\"paginati on\": {\"pageSizeList\": [10,20,50],\"localP agination\":false,\" pageSize\":10},\"c olumns\": [{\"dataIndex\":\" __ InstanceId \",\"titl __ e\":{\"intl\": {\"zh TW\":\"執行個 _ 體 \",\"en US\":\"Insta _ nce\",\"zh CN\":\"实 _ 例\",\"ja JP\":\"例 _ \"}},\"render\": {\"icon\":\"rds\",\"ic onColor\":\"B20\",\" description\":\" {{record. Instanc __ eName }}\"}}, __ {\"dataIndex\":\"Or ganizationName\",\ "title\":{\"intl\": {\"zh TW\":\"組織 _ \",\"en US\":\"Orga _ nization\",\"zh CN\" _ :\"组织 \",\"ja JP\":\"組織 _ \"}}}, {\"dataIndex\":\"En gine\",\"title\": {\"intl\": {\"zh TW\":\"資料庫 _ 類型 \",\"en US\":\"DB _ Type\",\"zh CN\":\" _ 数据库类型 \",\"ja JP\":\"DB タ _ イプ\"}},\"render\": {\"value\":\" {{JSON.parse(reco rd. Detail ).Engin __ __ |   |

|   |   | e}}\"}}, {\"dataIndex\":\"Re sourceSetName\",\ "title\":{\"intl\": {\"zh TW\":\"資源群 _ 組 \",\"en US\":\"Reso _ urce Group\",\"zh CN\":\ _ "资源集 \",\"ja JP\":\"リソー _ スグループ\"}}}, {\"dataIndex\":\"D BInstanceStatus\",\ "title\":{\"intl\": {\"zh TW\":\"運行狀 _ 態 \",\"en US\":\"Statu _ s\",\"zh CN\":\"运行 _ 状态\",\"ja JP\":\"ス _ テータス \"}},\"dataSource\" :[{\"label\": {\"intl\": {\"zh TW\":\"建立中 _ \",\"en US\":\"Creat _ ing\",\"zh CN\":\"创 _ 建中\",\"ja JP\":\"作 _ 成中 \"}},\"value\":\"CR EATING\"}, {\"label\":{\"intl\": {\"zh TW\":\"運行中 _ \",\"en US\":\"Runni _ ng\",\"zh CN\":\"运 _ 行中\",\"ja JP\":\"実 _ 行中 \"}},\"value\":\"RU NNING\"}, {\"label\":{\"intl\": {\"zh TW\":\"刪除中 _ \",\"en US\":\"Delet _ ing\",\"zh CN\":\"删 _ 除中\",\"ja JP\":\"削 _ 除中 \"}},\"value\":\"DEL ETING\"},{\"label\": {\"intl\": {\"zh TW\":\"重啟中 _ \",\"en US\":\"Rebo _ oting\",\"zh CN\":\" _ 重启中 \",\"ja JP\":\"再起動 _ 中 \"}},\"value\":\"RE BOOTING\"}, {\"label\":{\"intl\": {\"zh TW\":\"升降級 _ 中 \",\"en US\":\"Upgr _ ading or |   |
|---|---|---|---|
|   |   | degrading\",\"zh C _ N\":\"升降级中 \",\"ja JP\":\"アップ _ グレードまたはダウ ングレードしていま |   |

|   |   | す \"}},\"value\":\"DBI NSTANCECLASSCH ANGING\"}, {\"label\":{\"intl\": {\"zh TW\":\"恢複中 _ \",\"en US\":\"Reco _ vering\",\"zh CN\":\ _ "恢复中 \",\"ja JP\":\"リカバ _ リを進めています \"}},\"value\":\"TR ANSING\"}, {\"label\":{\"intl\": {\"zh TW\":\"內外網 _ 切換中 \",\"en US\":\"Switc _ hing between intranet and the Internet\",\"zh CN\" _ :\"内外网切换中 \",\"ja JP\":\"イント _ ラネットとインター ネットを切り替えて います \"}},\"value\":\"EN GINEVERSIONUPGR ADING\"}, {\"label\":{\"intl\": {\"zh TW\":\"備份恢 _ 複中 \",\"en US\":\"Back _ up recovering\",\"zh C _ N\":\"备份恢复中 \",\"ja JP\":\"バック _ アップしています \"}},\"value\":\"RES TORING\"}, {\"label\":{\"intl\": {\"zh TW\":\"數據匯 _ 入中 \",\"en US\":\"Impo _ rting data\",\"zh CN\":\" _ 数据导入中 \",\"ja JP\":\"データ _ をインポート中 \"}},\"value\":\"IMP ORTING\"}, {\"label\":{\"intl\": {\"zh TW\":\"從其他 _ RDS執行個體導入數據中 \",\"en US\":\"Impo _ rting data from other RDS instances\",\"zh CN _ \":\"从其他RDS实例导入数据中 \",\"ja JP\":\"他の _ RDS インスタンスか らデータをインポー トしています \"}},\"value\":\"IMP ORTINGFROMOTHE |   |
|---|---|---|---|

|   |   | RS\"},{\"label\": {\"intl\": {\"zh TW\":\"內外網 _ 切換中 \",\"en US\":\"Switc _ hing between intranet and the Internet\",\"zh CN\" _ :\"内外网切换中 \",\"ja JP\":\"イント _ ラネットとパブリッ クネットワークを切 り替えています \"}},\"value\":\"DBI NSTANCENETTYPE CHANGING\"}, {\"label\":{\"intl\": {\"zh TW\":\"容災切 _ 換中 \",\"en US\":\"Switc _ hing to disaster recovery\",\"zh CN\ _ ":\"容灾切换中 \",\"ja JP\":\"障害復 _ 旧を切り替えていま す \"}},\"value\":\"GU ARDSWITCHING\"}, {\"label\":{\"intl\": {\"zh TW\":\"SLL修 _ 改\",\"en US\":\"SLL _ modification\",\"zh _ CN\":\"SLL修改 \",\"ja JP\":\"SLLの _ 変更 \"}},\"value\":\"SSL MODIFYING\"}, _ {\"label\":{\"intl\": {\"zh TW\":\"網絡創 _ 建 \",\"en US\":\"Netw _ ork creation\",\"zh CN\ _ ":\"网络创建 \",\"ja JP\":\"ネット _ ワーク作成 \"}},\"value\":\"NE T CREATING\"}, _ {\"label\":{\"intl\": {\"zh TW\":\"帳戶模 _ 式升級 \",\"en US\":\"Acco _ unt mode upgrade\",\"zh CN\ _ ":\"帐户模式升级 \",\"ja JP\":\"アカウ _ ントモードのアップ グレード \"}},\"value\":\"AC COUNT MODE UPG _ _ RADING\"}, {\"label\":{\"intl\": {\"zh TW\":\"內部克 _ 隆 \",\"en US\":\"Inter _ nal |   |
|---|---|---|---|

|   |   | cloning\",\"zh CN\": _ \"内部克隆 \",\"ja JP\":\"内部ク _ ローニング \"}},\"value\":\"INS CLONING\"}],\"ren _ der\":{\"value\":\" {{ () => JSON.parse(record. Detail ).DBInsta __ __ nceStatus.toLocale UpperCase() }}\"}}, {\"dataIndex\":\"D BInstanceNetType\ ",\"title\":{\"intl\": {\"zh TW\":\"網路 _ \",\"en US\":\"Netw _ ork\",\"zh CN\":\"网 _ 络\",\"ja JP\":\"ネッ _ トワーク \"}},\"dataSource\" :[{\"label\": {\"intl\": {\"zh TW\":\"公網 _ \",\"en US\":\"Inter _ net\",\"zh CN\":\"公 _ 网\",\"ja JP\":\"イン _ ターネット \"}},\"value\":\"INT ERNET\"}, {\"label\":{\"intl\": {\"zh TW\":\"內網 _ \",\"en US\":\"Intra _ net\",\"zh CN\":\"内 _ 网\",\"ja JP\":\"イン _ トラネット \"}},\"value\":\"INT RANET\"}],\"render \":{\"value\":\"{{ () => JSON.parse(record. Detail ).DBInsta __ __ nceNetType.toLoca leUpperCase() }}\"}}, {\"dataIndex\":\"cp u.Average\",\"title\" :{\"intl\": {\"zh TW\":\"CPU使 _ 用率 \",\"en US\":\"CPU _ Utilization\",\"zh C _ N\":\"CPU使用率 \",\"ja JP\":\"CPU 使 _ 用率\"}},\"render\": {\"unit\":\"%\",\"isE mphasize\":true,\"v alue\":\"{{ (val) => val ? Number(val ?? 0).toFixed(2) : '-' }}\"}}, {\"dataIndex\":\"m emory.Average\",\" title\":{\"intl\": |   |
|---|---|---|---|

|   |   | {\"zh TW\":\"記憶體 _ 使用量率 \",\"en US\":\"Mem _ ory Usage\",\"zh CN\":\ _ "内存使用率 \",\"ja JP\":\"メモリ _ 使用率 \"}},\"render\": {\"unit\":\"%\",\"isE mphasize\":true,\"v alue\":\"{{ (val) => val ? Number(val ?? 0).toFixed(2) : '-' }}\"}}, {\"dataIndex\":\"dis k.Average\",\"title\" :{\"intl\": {\"zh TW\":\"磁盤使 _ 用率 \",\"en US\":\"DiskU _ tilization\",\"zh CN\ _ ":\"磁盘使用率 \",\"ja JP\":\"ディス _ ク使用量 \"}},\"render\": {\"unit\":\"%\",\"isE mphasize\":true,\"v alue\":\"{{ (val) => val ? Number(val ?? 0).toFixed(2) : '-' }}\"}}],\"actions\": [{\"request\": {\"product\":\"asc m\",\"action\":\"Dat aCenterSearch\",\" params\": {\"resourceTypes\" : [\"rds instance\"],\" _ organizationIds\": [\" {{context.Organiz ationIds}}\"],\"retu rnInstanceDetail\":\ "true\",\"sortField\" :\" CreateTime \" __ __ ,\"pageSize\":\" {{context.PageSiz e}}\",\"regionIds\": [\" {{context.Region} }\"],\"page\":\" {{context.PageNu mber}}\",\"type\":\ "Instance\"},\"versi on\":\"2019-05- 10\"},\"format\": {\"totalPath\":\"tot al\",\"dataPath\":\" details\"},\"actions\ ":[{\"request\": {\"product\":\"cms\ ",\"action\":\"Descri |   |
|---|---|---|---|

|   |   | beMetricLast\",\"pa rams\": {\"MetricName\":\" CpuUsage\",\"Dime nsions\": [{\"instanceId\":\" {{record. Instanc __ eId }}\"}],\"Name __ space\":\"acs rds d _ _ ashboard\"},\"versi on\":\"2019-01- 01\"},\"requestCon fig\": {\"combo\":true},\" format\": {\"comboInterface PrimaryKey\":\"inst anceId\",\"extendP ath\":\"cpu\",\"main InterfacePrimaryKe y\":\" InstanceId __ __ \",\"dataPath\":\"Da tapoints\"}}, {\"request\": {\"product\":\"cms\ ",\"action\":\"Descri beMetricLast\",\"pa rams\": {\"MetricName\":\" MemoryUsage\",\" Dimensions\": [{\"instanceId\":\" {{record. Instanc __ eId }}\"}],\"Name __ space\":\"acs rds d _ _ ashboard\"},\"versi on\":\"2019-01- 01\"},\"requestCon fig\": {\"combo\":true},\" format\": {\"comboInterface PrimaryKey\":\"inst anceId\",\"extendP ath\":\"memory\",\" mainInterfacePrim aryKey\":\" Instan __ ceId \",\"dataPath __ \":\"Datapoints\"}}, {\"request\": {\"product\":\"cms\ ",\"action\":\"Descri beMetricLast\",\"pa rams\": {\"MetricName\":\" DiskUsage\",\"Dime nsions\": [{\"instanceId\":\" {{record. Instanc __ eId }}\"}],\"Name __ space\":\"acs rds d _ _ ashboard\"},\"versi on\":\"2019-01- 01\"},\"requestCon fig\": {\"combo\":true},\" |   |
|---|---|---|---|

|   |   | format\": {\"comboInterface PrimaryKey\":\"inst anceId\",\"extendP ath\":\"disk\",\"mai nInterfacePrimaryK ey\":\" InstanceId __ _ \",\"dataPath\":\"D _ atapoints\"}}]}]}} },\"baseProductCo nfig\": {\"instanceDataKe y\":\" InstanceId __ __ \",\"isMetamonSup ported\":true,\"nam espace\":\"acs rds _ _ dashboard\",\"asc mCategory\":\"rds\ ",\"appGroupCateg ory\":\"RDS 1\",\ ____ "metricInstanceKey \":\"instanceId\",\"d imensionsIncludeR egion\":false,\"cate gory\":\"rds\",\"intl\ ":{\"intl\": {\"zh TW\":\"Apsar _ aDB RDS\",\"en US\":\"A _ psaraDB RDS\",\"zh CN\":\" _ 云数据库RDS版 \",\"ja JP\":\"Apsara _ DB RDS\"}},\"helperD oc\": {\"metricCode\":\" DOC.EMBED.CMS.3 \"},\"instanceData Desc\":\" Instance __ Name \"},\"produ __ ctDetailConfig\": {\"tabList\": [{\"subTabList\": [{\"subTabListIntl\" :{\"intl\": {\"zh TW\":\"執行個 _ 體 \",\"en US\":\"Insta _ nces\",\"zh CN\":\" _ 实例\",\"ja JP\":\"イ _ ンスタンスリスト \"}},\"sectionList\": [{\"sectionChartLis t\":[{\"chartList\": [{\"chartIntl\": {\"intl\": {\"zh TW\":\"磁盤使 _ 用率 \",\"en US\":\"Disk _ Usage\",\"zh CN\":\ _ "磁盘使用率 \",\"ja JP\":\"ディス _ ク使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic |   |
|---|---|---|---|

|   |   | s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "DiskUsage\",\"met ricIntl\":{\"intl\": {\"zh TW\":\"硬碟使 _ 用 \",\"en US\":\"Disk _ Usage\",\"zh CN\":\ _ "硬盘使用 \",\"ja JP\":\"ディス _ ク使用量 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\":{\"Engine\": [\"MySQL\",\"SQLSe rver\",\"POLARDB\" ]},\"chartGroupBy\ ":[]},{\"chartIntl\": {\"intl\": {\"zh TW\":\"IOPS _ 使用率 \",\"en US\":\"IOPS _ Usage\",\"zh CN\":\ _ "IOPS使用率 \",\"ja JP\":\"IOPS 使 _ 用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "IOPSUsage\",\"met ricIntl\":{\"intl\": {\"zh TW\":\"IOPS _ 使用率 \",\"en US\":\"IOPS _ Usage\",\"zh CN\":\ _ "IOPS使用率 \",\"ja JP\":\"IOPS 使 _ 用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\":{\"Engine\": [\"MySQL\",\"SQLSe rver\",\"POLARDB\" ]},\"chartGroupBy\ ":[]},{\"chartIntl\": {\"intl\": {\"zh TW\":\"串連數 _ 使用率 \",\"en US\":\"Conn _ |   |
|---|---|---|---|

|   |   | ections Usage\",\"zh CN\":\ _ "连接数使用率 \",\"ja JP\":\"接続使 _ 用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "ConnectionUsage\ ",\"metricIntl\": {\"intl\": {\"zh TW\":\"串連數 _ 使用率 \",\"en US\":\"Conn _ ections Usage\",\"zh CN\":\ _ "连接数使用率 \",\"ja JP\":\"接続使 _ 用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\":{\"Engine\": [\"MySQL\",\"SQLSe rver\",\"POLARDB\" ]},\"chartGroupBy\ ":[]},{\"chartIntl\": {\"intl\": {\"zh TW\":\"CPU使 _ 用率 \",\"en US\":\"CPU _ Utilization\",\"zh C _ N\":\"CPU使用率 \",\"ja JP\":\"CPU 使 _ 用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "CpuUsage\",\"met ricIntl\":{\"intl\": {\"zh TW\":\"CPU使 _ 用率 \",\"en US\":\"CPU _ Utilization\",\"zh C _ N\":\"CPU使用率 \",\"ja JP\":\"CPU 使 _ 用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr |   |
|---|---|---|---|

|   |   | ops\":{\"Engine\": [\"MySQL\",\"SQLSe rver\",\"POLARDB\" ]},\"chartGroupBy\ ":[]},{\"chartIntl\": {\"intl\": {\"zh TW\":\"記憶體 _ 使用量率 \",\"en US\":\"Mem _ ory Usage\",\"zh CN\":\ _ "内存使用率 \",\"ja JP\":\"メモリ _ 使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "MemoryUsage\",\" metricIntl\": {\"intl\": {\"zh TW\":\"記憶體 _ 使用量率 \",\"en US\":\"Mem _ ory Usage\",\"zh CN\":\ _ "内存使用率 \",\"ja JP\":\"メモリ _ 使用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\":{\"Engine\": [\"MySQL\",\"POLAR DB\",\"SQLServer\"] },\"chartGroupBy\": []},{\"chartIntl\": {\"intl\": {\"zh TW\":\"MySQ _ L網路入流量 \",\"en US\":\"MySQ _ L Network Inbound Traffic\",\"zh CN\":\ _ "MySQL网络入流量 \",\"ja JP\":\"MySQL _ ネットワークインバ ウンド交通 \"}},\"chartUnit\":\" bits/s\",\"chartStati stics\": [\"Average\",\"Mini mum\",\"Maximum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Mini mum\",\"Maximum\ "],\"metricName\":\ "MySQL NetworkIn _ |   |
|---|---|---|---|

|   |   | New\",\"metricIntl\" :{\"intl\": {\"zh TW\":\"MySQ _ L網路入流量 \",\"en US\":\"MySQ _ L Network Inbound Traffic\",\"zh CN\":\ _ "MySQL网络入流量 \",\"ja JP\":\"MySQL _ ネットワークインバ ウンド交通 \"}},\"metricUnit\": \"bits/s\"}],\"chartT ype\":\"line\",\"sho wProps\": {\"Engine\": [\"MySQL\"]},\"char tGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"MySQ _ L網路出流量 \",\"en US\":\"MySQ _ L Network Outbound Traffic\",\"zh CN\":\ _ "MySQL网络出流量 \",\"ja JP\":\"MySQL _ ネットワークアウト バウンド交通 \"}},\"chartUnit\":\" bits/s\",\"chartStati stics\": [\"Average\",\"Mini mum\",\"Maximum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Mini mum\",\"Maximum\ "],\"metricName\":\ "MySQL NetworkO _ utNew\",\"metricInt l\":{\"intl\": {\"zh TW\":\"MySQ _ L網路出流量 \",\"en US\":\"MySQ _ L Network Outbound Traffic\",\"zh CN\":\ _ "MySQL网络出流量 \",\"ja JP\":\"MySQL _ ネットワークアウト バウンド交通 \"}},\"metricUnit\": \"bits/s\"}],\"chartT ype\":\"line\",\"sho wProps\": {\"Engine\": [\"MySQL\"]},\"char tGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"MySql _ 每秒查詢量 \",\"en US\":\"MySq _ |   |
|---|---|---|---|

| -Data | Array | l queries per second\",\"zh CN\": _ \"MySQL每秒查询量 \",\"ja JP\":\"1秒あた _ りのmysqlクエリ \"}},\"chartUnit\":\" count/s\",\"chartSta tistics\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"MySQL QPS\",\"metricIntl\ _ ":{\"intl\": {\"zh TW\":\"MySql _ 每秒查詢量 \",\"en US\":\"MySq _ l queries per second\",\"zh CN\": _ \"MySQL每秒查询量 \",\"ja JP\":\"1秒あた _ りのmysqlクエリ \"}},\"metricUnit\": \"count/s\"}],\"char tType\":\"line\",\"sh owProps\": {\"Engine\": [\"MySQL\"]},\"char tGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"データ _ ベースエージェント- CPUの使用率 \",\"en US\":\"Dock _ er Cpu Usage\",\"zh CN\":\ _ "数据库代理-CPU使用率 \",\"ja JP\":\"Docker _ CPU使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"Docker CpuUsage\",\"metri cIntl\":{\"intl\": {\"zh TW\":\"データ _ ベースエージェント- CPUの使用率 \",\"en US\":\"Dock _ er Cpu Usage\",\"zh CN\":\ _ "数据库代理-CPU使用率 \",\"ja JP\":\"Docker _ CPU使用率 \"}},\"metricUnit\": \"%\"}],\"chartType | Console view configuration list |
|---|---|---|---|

|   |   | \":\"line\",\"showPr ops\":{\"Engine\": [\"MySQL\"]},\"char tGroupBy\": [\"type\"]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"SQLS _ erver網路入流量 \",\"en US\":\"SQL _ Server network inbound traffic\",\"zh CN\":\ _ "SQLServer网络入流量\",\"ja JP\":\"SQL _ Server ネットワーク インバウンド交通 \"}},\"chartUnit\":\" bits/s\",\"chartStati stics\": [\"Average\",\"Mini mum\",\"Maximum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Mini mum\",\"Maximum\ "],\"metricName\":\ "SQLServer Networ _ kInNew\",\"metricIn tl\":{\"intl\": {\"zh TW\":\"SQLS _ erver網路入流量 \",\"en US\":\"SQL _ Server network inbound traffic\",\"zh CN\":\ _ "SQLServer网络入流量\",\"ja JP\":\"SQL _ Server ネットワーク インバウンド交通 \"}},\"metricUnit\": \"bits/s\"}],\"chartT ype\":\"line\",\"sho wProps\": {\"Engine\": [\"SQLServer\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"SQLS _ erver網路出流量 \",\"en US\":\"SQL _ Server network outbound traffic\",\"zh CN\":\ _ "SQLServer网络出流量\",\"ja JP\":\"SQL _ Server ネットワーク アウトバウンド交通 \"}},\"chartUnit\":\" bits/s\",\"chartStati stics\": [\"Average\",\"Mini mum\",\"Maximum\ "],\"chartMetrics\": |   |
|---|---|---|---|

|   |   | [{\"metricStatistics \": [\"Average\",\"Mini mum\",\"Maximum\ "],\"metricName\":\ "SQLServer Networ _ kOutNew\",\"metric Intl\":{\"intl\": {\"zh TW\":\"SQLS _ erver網路出流量 \",\"en US\":\"SQL _ Server network outbound traffic\",\"zh CN\":\ _ "SQLServer网络出流量\",\"ja JP\":\"SQL _ Server ネットワーク アウトバウンド交通 \"}},\"metricUnit\": \"bits/s\"}],\"chartT ype\":\"line\",\"sho wProps\": {\"Engine\": [\"SQLServer\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"每CPU _ 平均活躍連接數 PG _ 雲盤 \",\"en US\":\"Aver _ age active connections per CPU PG cloud _ disk\",\"zh CN\":\" _ 每CPU平均活跃连接数 PG云盘 _ \",\"ja JP\":\"Cpu p _ _ gクラウドディスクあ たりの平均アクティ ブ接続 \"}},\"chartUnit\":\" Count\",\"chartStati stics\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"Active Connections\",\"me tricIntl\":{\"intl\": {\"zh TW\":\"每CPU _ 平均活躍連接數 PG _ 雲盤 \",\"en US\":\"Aver _ age active connections per CPU PG cloud _ disk\",\"zh CN\":\" _ 每CPU平均活跃连接数 PG云盘 _ \",\"ja JP\":\"Cpu p _ _ gクラウドディスクあ たりの平均アクティ ブ接続 |   |
|---|---|---|---|

|   |   | \"}},\"metricUnit\": \"Count\"}],\"chart Type\":\"line\",\"sh owProps\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"INOD _ E使用率 PG雲端硬碟 _ \",\"en US\":\"Inode _ Usage PG _ Disk\",\"zh CN\":\"I _ NODE使用率 PG云盘 _ \",\"ja JP\":\"INODE _ 使用率 PG クラウド _ ディスク \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"InodeU sage\",\"metricIntl\ ":{\"intl\": {\"zh TW\":\"INOD _ E使用率 PG雲端硬碟 _ \",\"en US\":\"Inode _ Usage PG _ Disk\",\"zh CN\":\"I _ NODE使用率 PG云盘 _ \",\"ja JP\":\"INODE _ 使用率 PG クラウド _ ディスク \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"只讀同 _ 步延遲 PG雲盤 _ \",\"en US\":\"Read _ -only synchronization delay PG cloud _ disk\",\"zh CN\":\" _ 只读同步延迟 PG云 _ 盘\",\"ja JP\":\"読み _ 取り専用同期 delay pgクラウド _ ディスク \"}},\"chartUnit\":\" |   |
|---|---|---|---|

|   |   | Second\",\"chartSta tistics\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"ReadL ag\",\"metricIntl\": {\"intl\": {\"zh TW\":\"只讀同 _ 步延遲 PG雲盤 _ \",\"en US\":\"Read _ -only synchronization delay PG cloud _ disk\",\"zh CN\":\" _ 只读同步延迟 PG云 _ 盘\",\"ja JP\":\"読み _ 取り専用同期 delay pgクラウド _ ディスク \"}},\"metricUnit\": \"Second\"}],\"char tType\":\"line\",\"sh owProps\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"資料庫 _ 年齡 PG雲端硬碟 _ \",\"en US\":\"Data _ base Age PG _ Disk\",\"zh CN\":\" _ 数据库年龄 PG云盘 _ \",\"ja JP\":\"Databa _ se Age PG クラウド _ ディスク \"}},\"chartUnit\":\" xids\",\"chartStatist ics\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"DBAge \",\"metricIntl\": {\"intl\": {\"zh TW\":\"資料庫 _ 年齡 PG雲端硬碟 _ \",\"en US\":\"Data _ base Age PG _ Disk\",\"zh CN\":\" _ 数据库年龄 PG云盘 _ \",\"ja JP\":\"Databa _ se Age PG クラウド _ ディスク \"}},\"metricUnit\": \"xids\"}],\"chartTy pe\":\"line\",\"show |   |
|---|---|---|---|

|   |   | Props\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"只讀流 _ 複製狀態 PG雲盤 _ \",\"en US\":\"Read _ -only Stream replication state pg cloud _ disk\",\"zh CN\":\" _ 只读流复制状态 PG _ 云盘\",\"ja JP\":\"読 _ み取り専用ストリー ム複製state pgクラ _ ウドディスク \"}},\"chartUnit\":\" value\",\"chartStati stics\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"Stream ingStatus\",\"metri cIntl\":{\"intl\": {\"zh TW\":\"只讀流 _ 複製狀態 PG雲盤 _ \",\"en US\":\"Read _ -only Stream replication state pg cloud _ disk\",\"zh CN\":\" _ 只读流复制状态 PG _ 云盘\",\"ja JP\":\"読 _ み取り専用ストリー ム複製state pgクラ _ ウドディスク \"}},\"metricUnit\": \"value\"}],\"chartT ype\":\"line\",\"sho wProps\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"PG 連 _ _ 接數使用率 \",\"en US\":\"Pg c _ _ onnection usage\",\"zh CN\":\ _ "PG 连接数使用率 _ \",\"ja JP\":\"Pg con _ _ nectionの使用法 \"}},\"chartUnit\":\" %\",\"chartStatistic |   |
|---|---|---|---|

|   |   | s\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"conn u _ sage\",\"metricIntl\ ":{\"intl\": {\"zh TW\":\"Conn _ _ usage\",\"en US\":\ _ "conn usage\",\"zh _ CN\":\"conn usage _ _ \",\"ja JP\":\"Conn _ _ usage\"}},\"metric Unit\":\"%\"}],\"cha rtType\":\"line\",\"s howProps\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"PG CP _ _ U使用率 \",\"en US\":\"PG C _ _ PU usage\",\"zh CN\":\ _ "PG CPU使用率 _ \",\"ja JP\":\"Pg cpu _ _ 使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Value\"],\" chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Value\"],\" metricName\":\"cp u usage\",\"metricI _ ntl\":{\"intl\": {\"zh TW\":\"PG CP _ _ U使用率 \",\"en US\":\"PG C _ _ PU usage\",\"zh CN\":\ _ "PG CPU使用率 _ \",\"ja JP\":\"Pg cpu _ _ 使用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": |   |
|---|---|---|---|

|   |   | {\"intl\": {\"zh TW\":\"PG IO _ _ PS使用率 \",\"en US\":\"PG I _ _ OPS usage\",\"zh CN\":\ _ "PG IOPS使用率 _ \",\"ja JP\":\"Pg iop _ _ sの使用法 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"iops us _ age\",\"metricIntl\": {\"intl\": {\"zh TW\":\"PG IO _ _ PS使用率 \",\"en US\":\"PG I _ _ OPS usage\",\"zh CN\":\ _ "PG IOPS使用率 _ \",\"ja JP\":\"Pg iop _ _ sの使用法 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"PG 磁 _ _ 盤空間使用率 \",\"en US\":\"Pg di _ _ sk space usage\",\"zh CN\":\ _ "PG 磁盘空间使用率 _ \",\"ja JP\":\"Pg disk _ _ スペース使用量 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"local fs _ size usage\",\"me _ _ tricIntl\":{\"intl\": {\"zh TW\":\"PG 磁 _ _ 盤空間使用率 \",\"en US\":\"Pg di _ _ sk space usage\",\"zh CN\":\ _ "PG 磁盘空间使用率 _ \",\"ja JP\":\"Pg disk _ _ |   |
|---|---|---|---|

|   |   | スペース使用量 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"PG 記 _ _ 憶體使用率 \",\"en US\":\"PG _ Memory Usage\",\"zh CN\":\ _ "PG 内存使用率 _ \",\"ja JP\":\"PG _ Memory Usage\"}},\"chartU nit\":\"%\",\"chartSt atistics\": [\"Average\"],\"cha rtMetrics\": [{\"metricStatistics \": [\"Average\"],\"met ricName\":\"mem u _ sage\",\"metricIntl\ ":{\"intl\": {\"zh TW\":\"PG 記 _ _ 憶體使用率 \",\"en US\":\"PG _ Memory Usage\",\"zh CN\":\ _ "PG 内存使用率 _ \",\"ja JP\":\"PG _ Memory Usage\"}},\"metric Unit\":\"%\"}],\"cha rtType\":\"line\",\"s howProps\": {\"DBInstanceStora geType\": [\"cloud ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"磁盤使 _ 用率 \",\"en US\":\"Disk _ Usage\",\"zh CN\":\ _ "磁盘使用率 \",\"ja JP\":\"ディス _ ク使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics |   |
|---|---|---|---|

|   |   | \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "DiskUsage\",\"met ricIntl\":{\"intl\": {\"zh TW\":\"硬碟使 _ 用 \",\"en US\":\"Disk _ Usage\",\"zh CN\":\ _ "硬盘使用 \",\"ja JP\":\"ディス _ ク使用量 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"local ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"IOPS _ 使用率 \",\"en US\":\"IOPS _ Usage\",\"zh CN\":\ _ "IOPS使用率 \",\"ja JP\":\"IOPS 使 _ 用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "IOPSUsage\",\"met ricIntl\":{\"intl\": {\"zh TW\":\"IOPS _ 使用率 \",\"en US\":\"IOPS _ Usage\",\"zh CN\":\ _ "IOPS使用率 \",\"ja JP\":\"IOPS 使 _ 用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"local ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"串連數 _ 使用率 |   |
|---|---|---|---|

|   |   | \",\"en US\":\"Conn _ ections Usage\",\"zh CN\":\ _ "连接数使用率 \",\"ja JP\":\"接続使 _ 用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "ConnectionUsage\ ",\"metricIntl\": {\"intl\": {\"zh TW\":\"串連數 _ 使用率 \",\"en US\":\"Conn _ ections Usage\",\"zh CN\":\ _ "连接数使用率 \",\"ja JP\":\"接続使 _ 用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"local ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"CPU使 _ 用率 \",\"en US\":\"CPU _ Utilization\",\"zh C _ N\":\"CPU使用率 \",\"ja JP\":\"CPU 使 _ 用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "CpuUsage\",\"met ricIntl\":{\"intl\": {\"zh TW\":\"CPU使 _ 用率 \",\"en US\":\"CPU _ Utilization\",\"zh C _ N\":\"CPU使用率 \",\"ja JP\":\"CPU 使 _ |   |
|---|---|---|---|

|   |   | 用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"local ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\":[]}, {\"chartIntl\": {\"intl\": {\"zh TW\":\"記憶體 _ 使用量率 \",\"en US\":\"Mem _ ory Usage\",\"zh CN\":\ _ "内存使用率 \",\"ja JP\":\"メモリ _ 使用率 \"}},\"chartUnit\":\" %\",\"chartStatistic s\": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"chartMetrics\": [{\"metricStatistics \": [\"Average\",\"Maxi mum\",\"Minimum\ "],\"metricName\":\ "MemoryUsage\",\" metricIntl\": {\"intl\": {\"zh TW\":\"記憶體 _ 使用量率 \",\"en US\":\"Mem _ ory Usage\",\"zh CN\":\ _ "内存使用率 \",\"ja JP\":\"メモリ _ 使用率 \"}},\"metricUnit\": \"%\"}],\"chartType \":\"line\",\"showPr ops\": {\"DBInstanceStora geType\": [\"local ssd\"],\"En _ gine\": [\"PostgreSQL\"]},\" chartGroupBy\": []}]}],\"sectionIntl\" :{\"intl\": {}}}],\"dimensions Key\": [\"region\",\"instan ceId\"]}, {\"subTabListIntl\": {\"intl\": {\"zh TW\":\"慢 _ SQL\",\"en US\":\"S _ low SQL\",\"zh CN\":\" _ 慢 |   |
|---|---|---|---|

|   |   | SQL\",\"ja JP\":\"慢 _ SQL\"}},\"sectionLi st\": [{\"sectionIntl\": {\"intl\": {}},\"sectionModul e\": {\"moduleResourc e\":[\" {{CDN DOMAIN}}/ _ teamix- components/rds- slow- sql/{{VERSION}}/ modules/rds-slow- sql.css\",\" {{CDN DOMAIN}}/ _ teamix- components/rds- slow- sql/{{VERSION}}/ modules/rds-slow- sql.js\"],\"moduleV ersion\":\"3.16.2\",\ "moduleName\":\"R dsSlowSql\",\"modu leParams\": {\"instanceId\":\" {{ InstanceId }} __ __ \"}}}]}],\"tabListInt l\":{\"intl\": {\"zh TW\":\"執行個 _ 體 \",\"en US\":\"Insta _ nces\",\"zh CN\":\" _ 实例\",\"ja JP\":\"イ _ ンスタンスリスト \"}}}]}}}", "ProductCategory": "rds" }]} |   |
|---|---|---|---|
| --Input | String | cpu usage _ | The input parameter of the monitoring item. |
| --Output | String | CPU Utilization | The display name of the monitoring item. |
| -- ProductCatego ry | String | cms | The product category identifier. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeConsoleViews &Common request parameters
```

Sample success responses `JSON` format `XML` format

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ParameterInvalid | Illegal parameters. |   |
| 403 | AccessForbidden | User not authorized to operate on the specified resource. |   |
| 404 | ResourceNotFound | The specified resource is not found. |   |
| 500 | InternalError | The request processing has failed due to some unknown error. |   |

**NDocument supplementary notes**

> **Important:** This API is intended only for querying CMS console view configurations. External users and third-party applications must not call it. Its behavior and parameters are subject to change at any time without backward compatibility guarantees.This API queries the view configuration information of the CMS console. External users and third-party applications must not call this API. The API behavior and parameters may change at any time, and backward compatibility is not guaranteed.

### 2.3 Custom monitoring

#### 2.3.1 PutCustomMetric

Reports monitoring data.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|

| MetricList | Repe atLis t | Quer y | Yes |   | The monitoring data. |
|---|---|---|---|---|---|
| -GroupId | Strin g |   | No | 12345 | The ID of the application group. Valid values of N: 1 to 21. If the metric does not belong to any application group, enter 0. |
| - MetricNam e | Strin g |   | No | cpu total _ | The metric name. Valid values of N: 1 to 21. For more information, see Appendix 1: Metrics. |
| - Dimension s | Strin g |   | No | {"sampleName1":"value1 ","sampleName2":"value2 "} | The dimensions that specify the resources whose monitoring data you want to query. Valid values of N: 1 to 21. Set the value to a collection of key-value pairs. A typical key-value pair is {"Key":"Value"} . The key or value must be 1 to 64 bytes in length. Excessive characters are truncated. The key or value can contain letters, digits, periods (.), hyphens (-), underscores ( ), forward _ slashes (/), and backslashes (\). Dimensions must be formatted as a JSON string in a specified order. |

| -Time | Strin g |   | No | 1508136760000 | The timestamp when the metric data is generated. Valid values of N: 1 to 21. The timestamp can be in one of the following formats: The UTC timestamp that is in the YYYY-MM- DDThh:mm:ssZ format. Example: 20171012T132456.888 +0800. The UNIX timestamp of the LONG type. Example: 1508136760000. |
|---|---|---|---|---|---|
| -Type | Strin g |   | No | 0 | The type of the reported data. Valid values of N: 1 to 21. Valid values: 0: reports raw data 1: reports aggregate data We recommend that you report aggregate data in both the aggregation periods of 60 s and 300 s. Otherwise, you cannot query monitoring data in a time span that is more than seven days. |
| -Period | Strin g |   | No | 60 | The aggregation period. Valid values of N: 1 to 21. Unit: seconds. Valid values: 60 and 300. If the Type parameter is set to 1, the Period parameter is required. |

| -Values | Strin g |   | No | {"value":10.5} | The collection of metric values. Valid values of N: 1 to 21. If the Type parameter is set to 0, the keys in this parameter must be set to the specified value. CloudMonitor aggregates raw data in each aggregation period to generate multiple statistical values, such as the maximum value, the count, and the total value. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 05B36C2C-5F6E- 48D5-8B41- CE36DD7EE8E0 | The request ID. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The request has failed due to a temporary failure of the server. | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutCustomMetric &MetricList=null &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The request has failed due to a temporary failure of the server.",
 "RequestId":"05B36C2C-5F6E-48D5-8B41-CE36DD7EE8E0",
 "Code":"200"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.3.2 BatchDeleteCustomMetricMeta

Deletes custom monitoring metrics in batches.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| CustomMe tricNameLi st | Repe atLis t | Quer y | Yes | ["custom metric 01","cus _ _ tom metric 02"] _ _ | The list of custom metric names to delete. You can specify up to 100 names. |

Batch delete metadata of custom monitoring metrics.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Code | Integer | 200 | The status code. A value of 200 indicates success. |
|---|---|---|---|
| Message | String | successful | The response message. The system returns successful when the request succeeds. |
| Success | Boolean | true | Indicates whether the request succeeds. Valid values: true (success) and false (failure) |
| RequestId | String | A]B664E7-1823- 4C84-A59B- 1A3BXXXX | The request ID. |

**Examples**

`JSON` format `{`

```json
  "RequestId": "ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
  "Success": true,
  "Code": 200,
  "Message": ""
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | 403 | InvalidAuthorization | Permission denied. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 400 | 400 | ParameterInvalid | %s |
| 406 | 406 | ExceedingQuota | %s |
| 500 | 500 | InternalError | The system failed to process the request due to some unknown errors. |

#### 2.3.3 CreateCustomMetricMeta

Creates metadata for custom monitoring metrics.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Metric | Strin g | Quer y | Yes | custom cpu total _ _ | The name of the metric, which must be globally unique, start with a letter, and contain only letters, digits, and underscores. The name can be up to 64 characters in length. |
| Period | Strin g | Quer y | Yes | 60 | The monitoring period. Unit: seconds. Valid values: 60, 300, 900, 1800, and 3600 |
| Descriptio n | Strin g | Quer y | Yes | CPU utilization | The description of the metric, which can be up to 500 characters in length. |
| Unit | Strin g | Quer y | Yes | ms | The unit of the metric, such as ms, count, or %. The unit can be up to 20 characters in length. |
| Dimension s | Repe atLis t | Quer y | Yes | ["userId","instanceId","gr oupId"] | The list of dimensions. You can specify up to 10 dimensions. The userId, instanceId, and groupId dimensions are required. A dimension name must start with a letter and contain only letters, digits, and underscores. The name can be up to 64 characters in length. |
| Statistics | Repe atLis t | Quer y | Yes | ["Average","Maximum"] | The list of statistical methods. You can specify up to five methods. Valid values: Average, Minimum, Maximum, Sum, and Value |

Create metadata for custom monitoring metrics.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code. A value of 200 indicates success. |
| Message | String | successful | The returned message. The system returns successful when the request succeeds. |
| Success | Boolean | true | Indicates whether the request succeeds. Valid values: true (success) and false (failure) |
| RequestId | String | 15B664E7-1823- 4C84-A59B- 1A3BXXXX | The request ID. |

**Examples**

`JSON` format `{`

```json
  "Code": 200,
  "Message": "successful",
  "RequestId": "15B664E7-1823-4C84-A59B-1A3BXXXX",
  "Success": true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | 403 | InvalidAuthorization | Permission denied. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 400 | 400 | ParameterInvalid | %s |
| 406 | 406 | ExceedingQuota | %s |

| 500 | 500 | InternalError | The system failed to process the request due to some unknown errors. |
|---|---|---|---|

#### 2.3.4 DescribeCustomMetricList

Queries the reported monitoring data.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupId | Strin g | Query | Yes | 7378**** | The ID of the application group. For information about how to query the IDs of application groups, see DescribeMonitorGroups. |
| MetricNa me | Strin g | Query | No | cpu total _ | The name of the custom metric. |
| Dimension | Strin g | Query | No | {sampleName1=value1 &sampleName2=value2 } | The dimensions that specify the resources whose monitoring data you want to query. |
| Md5 | Strin g | Query | No | 97c25982d9745a23127 6bff27469**** | The MD5 value of the HTTP request body. The MD5 value is a 128-bit hash value used to verify the uniqueness of the reported monitoring data. |
| PageNum ber | Strin g | Query | No | 1 | The page number. Pages start from page 1. Default value: 1. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page. Pages start from page 1. Default value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |
| RequestId | String | 1AF425E4-1DEA- 54F2-910A- 8117C9686140 | The request ID. |
| Result | String | {\"all\":0,\"size\":10 ,\"param\": {\"metric\":\" {\\\"metricName\\\" :\\\"cpu total\\\",\\\" _ groupId\\\":7378*** *,\\\"project\\\":\\\"a cs customMetric 1 _ _ 20886317861****\\ \",\\\"dimension\\\": \\\"sampleName1= value1&sampleNa me2=value2\\\",\\\" status\\\":1}\",\"ser vice\":\"metric- center.aliyun- inc.com\"},\"page\" :1,\"list\":[]} | The reported custom metrics that are found in the query. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCustomMetricList &GroupId=7378**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"1AF425E4-1DEA-54F2-910A-8117C9686140",
 "Code":"200",
 "Result":"{\\\"all\\\":0,\\\"size\\\":10,\\\"param\\\":{\\\"metric\\\":\\\"{\\\\\\\"me
tricName\\\\\\\":\\\\\\\"cpu_total\\\\\\\",\\\\\\\"groupId\\\\\\\":7378****,\\\\\\\"proje \\\\\\\":\\\\\\\"acs_customMetric_120886317861****\\\\\\\",\\\\\\\"dimension\\\\\\\":\\\\ \"sampleName1=value1&sampleName2=value2\\\\\\\",\\\\\\\"status\\\\\\\":1}\\\",\\\"service \":\\\"metric-center.aliyun-inc.com\\\"},\\\"page\\\":1,\\\"list\\\":[]}"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.3.5 DeleteCustomMetric

Deletes the reported monitoring data of a metric.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupId | Strin g | Query | Yes | 3607**** | The ID of the application group. |
| MetricNa me | Strin g | Query | Yes | AdvanceCredit | The metric name. |
| Md5 | Strin g | Query | No | 38796C8CFFEB8F89BB2 A626C7BD7**** | The MD5 value of the HTTP request body. The MD5 value is a 128-bit hash value used to verify the uniqueness of the reported monitoring data. Set the value to the MD5 value returned when you query the reported monitoring data. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| UUID | Strin g | Query | No | 5497633c-66c5-4eae- abaa-89db5adb**** | The ID of the request for reporting monitoring data. Set the value to the ID returned when you query the reported monitoring data. We recommend that you set the Md5 parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |
| RequestId | String | 05B36C2C-5F6E- 48D5-8B41- CE36DD7EE8E0 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteCustomMetric &GroupId=3607**** &MetricName=AdvanceCredit &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"05B36C2C-5F6E-48D5-8B41-CE36DD7EE8E0",
 "Code":"200"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

### 2.4 Host monitoring

#### 2.4.1 NodeInstall

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| UserId | Strin g | Quer y | Yes | 123 | The user ID. |
| InstanceId | Strin g | Quer y | Yes | i-abcdefgh12**** | The instance ID. Valid values of N: 1 to 2000. |
| Force | Bool ean | Quer y | No | true | Specifies whether to force the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | Integer | 500 | The status code. |
| ErrorMessage | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |

| Success | Boolean | true | Indicates whether the request was successful. |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | abc1234567890 |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=NodeInstall &UserId=123 &InstanceId=i-abcdefgh12**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
 "ErrorCode":500,
 "ErrorMessage":"success",
 "Success":true
```

`}` `XML` format

```xml
<RequestId>ACBDBB40-DFB6-4F4C-8957-51FFB233969C</RequestId> <ErrorCode>500</ErrorCode> <ErrorMessage>success</ErrorMessage> <Success>true</Success>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

Cms 2018-03-08

#### 2.4.2 DescribeArgusAgentInstallRecord

Queries the installation records of the Argus agent, such as the installation time and status.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | i-abcdefgh12**** | The instance ID. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |
| PageNum ber | Integ er | Query | No | 1 | The page number. |
| StartTime | Strin g | Query | No | 2023 | 01 |
| EndTime | Strin g | Query | No | 2023 | 01 |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | req | abc1234567890 |
| Code | String | 404 | The error code. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Resources | String | [{"id": "res1", "name": "Resource One"}, {"id": "res2", "name": "Resource Two"}] | The queried resources. |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

#### 2.4.3 DescribeMonitoringAgentStatuses

Queries the status of the CloudMonitor agent.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| InstanceId s | Strin g | Quer y | Yes | i-hp3dunahluwajv6f**** | The instance ID. Separate multiple instance IDs with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| NodeStatusList | Array |   | The host status information. |
| -InstanceId | String | i- hp3dunahluwajv6f* *** | The instance ID. |
| -AutoInstall | Boolean | true | Indicates whether the CloudMonitor agent is automatically installed. Valid values: true: The CloudMonitor agent is automatically installed. false: The CloudMonitor agent is not automatically installed. |

| -Status | String | running | The status of the CloudMonitor agent. Valid values: running: The CloudMonitor agent is running. stopped: The CloudMonitor agent is stopped. installing: The CloudMonitor agent is being installed. install faild: The CloudMonitor agent _ fails to be installed. abnormal: The CloudMonitor agent is not properly installed. not installed: The CloudMonitor agent is _ not installed. |
|---|---|---|---|
| -AgentVersion | String |   |   |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 6F8371DF-AB81- 41B8-9E1B- 5493B3FF0E4F | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMonitoringAgentStatuses &InstanceIds=i-hp3dunahluwajv6f**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"6F8371DF-AB81-41B8-9E1B-5493B3FF0E4F",
 "NodeStatusList":{
  "Status":"running",
  "AutoInstall":true,
  "InstanceId":"i-hp3dunahluwajv6f****"
```

`},`

```json
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.4.4 DescribeMonitoringAgentHosts

Queries all hosts within the current Alibaba Cloud account, including hosts on which the CloudMonitor agent is installed and uninstalled.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| KeyWord | Strin g | Query | No | host1 | The keyword that is used in fuzzy match. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| HostName | Strin g | Query | No | hostNam1 | The hostname. |
| InstanceId s | Strin g | Query | No | i- a3d1q1pm2f9yr29e**** | The instance ID. |
| SerialNum bers | Strin g | Query | No | a1ab31a3-1234-40f2- 9e95-c8caa8f0**** | The serial number of the host. After the CloudMonitor agent is installed on a host, a globally unique serial number is generated. A host that is not provided by Alibaba Cloud has a serial number instead of an instance ID. This parameter can be used in exact search for any monitored hosts. |
| PageNum ber | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. Valid values: 10 20 50 100 Alibaba Cloud does not limit the maximum value of this parameter. However, we recommend that you do not specify a large value to obtain all the instances on a page. If you specify a large value for this parameter, you may fail to obtain the instances due to a timeout error. |
| InstanceR egionId | Strin g | Query | No | cn-hangzhou | The region ID of the instance. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Status | Strin g | Query | No | Running | The status of the hosts that you want to query. Valid values: Running: queries the hosts that are running. Stopped: queries the hosts that are stopped, are not installed, or fail to be installed. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Hosts | Array |   | The information about the hosts. |
| -InstanceId | String | i- a2d5q7pm3f9yr21 2**** | The instance ID. |
| -SerialNumber | String | x12335-6cc8-4a22- 9f21-1a00a719**** | The serial number of the host. A host that is not provided by Alibaba Cloud has a serial number instead of an instance ID. This parameter can be used in exact search for any monitored hosts. |
| -HostName | String | hostIP | The hostname. |
| -AliUid | Long | 103201326074**** | The ID of the Alibaba Cloud account. |
| - OperatingSyst em | String | Linux | The operating system. |
| -IpGroup | String | 192.168.XX.XX | The IP address of the host. Multiple IP addresses are separated with commas (,). |
| -Region | String | cn-hangzhou | The region ID of the instance. |
| -AgentVersion | String | 3.4.6 | The version of the agent. |

| loudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -EipAddress | String | 192.168.XX.XX | The elastic IP address (EIP) of the host. |
| -EipId | String | eip- bp16i16k9gcezyfrp **** | The ID of the EIP. |
| -isAliyunHost | Boolean | true | Indicates whether the host is provided by Alibaba Cloud. Valid values: true: The host is provided by Alibaba Cloud. false: The host is not provided by Alibaba Cloud. |
| -NatIp | String | 192.168.XX.XX | The IP address of the Network Address Translation (NAT) gateway. |
| -NetworkType | String | vpc | The network type. |
| - InstanceTypeF amily | String | ecs.n4 | The type of the Elastic Compute Service (ECS) instance. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 63EEBB2A-9E51- 41E4-9E83- 5DE7F3B292E0 | The request ID. |
| PageTotal | Integer | 50 | The page number. |
| Total | Integer | 10 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMonitoringAgentHosts &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Hosts":{
  "OperatingSystem":"Linux",
  "isAliyunHost":true,
  "InstanceId":"i-a2d5q7pm3f9yr212****",
  "AgentVersion":"3.4.6",
  "InstanceTypeFamily":"ecs.n4",
  "NatIp":"192.168.XX.XX",
  "SerialNumber":"x12335-6cc8-4a22-9f21-1a00a719****",
  "NetworkType":"vpc",
  "EipAddress":"192.168.XX.XX",
  "Region":"cn-hangzhou",
  "EipId":"eip-bp16i16k9gcezyfrp****",
  "IpGroup":"192.168.XX.XX",
  "HostName":"hostIP",
  "AliUid":"103201326074****"
```

`},`

```json
 "RequestId":"63EEBB2A-9E51-41E4-9E83-5DE7F3B292E0",
 "Message":"The Request is not authorization.",
 "PageTotal":50,
 "Total":10,
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.4.5 InstallMonitoringAgent

Installs the CloudMonitor agent on one or more Elastic Compute Service (ECS) instances.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Force | Boole an | Query | No | true | Specifies whether to forcibly install the CloudMonitor agent. Valid values: true (default) false |
| InstanceId s | Repe atList | Query | Yes | i-m5e0k0bexac8tykr**** | The IDs of the ECS instances. Valid values of N: 1 to 10. You must specify either the InstallCommand or the InstanceIds parameter. |

|   |   |   | InstallCommand |
|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 0BDAF8A8-04DC- 5F0C-90E4- 724D42C41945 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=InstallMonitoringAgent &InstanceIds=i-m5e0k0bexac8tykr**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"0BDAF8A8-04DC-5F0C-90E4-724D42C41945",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.4.6 DescribeMonitoringAgentProcesses

Queries the processes of a specified resource.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | i-hp3hl3cx1pbahzy8**** | The instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| NodeProcesse s | Array |   | The processes. |
| -ProcessId | Long | 234567 | The process ID. |
| -InstanceId | String | i- hp3hl3cx1pbahzy8 **** | The instance ID. |
| -ProcessName | String | Nginx | The process name. |
| -ProcessUser | String | alice | The user who launches the process. |
| -Command | String | number | The command used to obtain the number of processes. Valid value: number . The number command obtains the number of processes that match the condition. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | C11C0E85-6862- 4F25-8D66- D6A5E0882984 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMonitoringAgentProcesses &InstanceId=i-hp3hl3cx1pbahzy8**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"C11C0E85-6862-4F25-8D66-D6A5E0882984",
 "NodeProcesses":{
  "ProcessName":"Nginx",
  "InstanceId":"i-hp3hl3cx1pbahzy8****",
  "Command":"number",
  "ProcessUser":"alice",
  "ProcessId":234567
```

`},`

```json
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.4.7 PutMonitoringConfig

Configures global settings for the CloudMonitor agent.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| AutoInstal l | Boole an | Query | No | true | Specifies whether to automatically install the CloudMonitor agent on existing Elastic Compute Service (ECS) instances. Valid values: true (default value) false |
| EnableInst allAgentN ewECS | Boole an | Query | No | true | Specifies whether to automatically install the CloudMonitor agent on new ECS instances. Valid values: true (default value) false |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | Specified parameter EnableInstallAgent NewECS is not valid. | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 109C8095-6FAD- 4DBB-B013- 6ED18CE4C0B1 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutMonitoringConfig &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"Specified parameter EnableInstallAgentNewECS is not valid.",
 "RequestId":"109C8095-6FAD-4DBB-B013-6ED18CE4C0B1",
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | InvalidParameter | The specified parameter is not valid. |
| 403 | 403 | InvalidAuthorization | The Request is not authorization. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.4.8 DeleteMonitoringAgentProcess

Disables the monitoring of a specified process on a specified instance.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | i-KpVny6l**** | The instance ID. |
| ProcessNa me | Strin g | Query | No | http | The process name. You must specify either the ProcessId or the ProcessName parameter. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessId | Strin g | Query | No | 123**** | The process ID. You must specify either the ProcessId or the ProcessName parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | The specified resource is not found. | The returned message. |
| RequestId | String | 971CC023-5A96- 452A-BB7C- 2483F948BCFD | The request ID. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMonitoringAgentProcess &InstanceId=i-KpVny6l**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"971CC023-5A96-452A-BB7C-2483F948BCFD",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.4.9 CreateMonitoringAgentProcess

Creates a task to monitor a process.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProcessNa me | Strin g | Query | No | java | The process name. |
| InstanceId | Strin g | Query | Yes | i-2ze51wjtwox01r8g**** | The instance ID. |
| ProcessUs er | Strin g | Query | No | admin | The user who launches the process. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | User not authorized to operate on the specified resource. | The returned message. |

| CloudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 0DFCB47D-E7E1- 4CBE-A381- 8339F7B300EF | The request ID. |
| Id | Long | 12345 | The process ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateMonitoringAgentProcess &InstanceId= i-2ze51wjtwox01r8g**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"User not authorized to operate on the specified resource.",
 "RequestId":"0DFCB47D-E7E1-4CBE-A381-8339F7B300EF",
 "Id":12345,
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.4.10 DescribeMonitoringConfig

Queries the global configurations of the CloudMonitor agent.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | F35654DB-0C9D- 4FB3-903F- 479BA7663061 | The request ID. |
| AutoInstall | Boolean | false | Specifies whether to automatically install the CloudMonitor agent on existing Elastic Compute Service (ECS) instances. Valid values: true false |
| EnableInstallA gentNewECS | Boolean | true | Specifies whether to automatically install the CloudMonitor agent on new ECS instances. Valid values: true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMonitoringConfig
```

Sample success responses `JSON` format `{`

```json
 "AutoInstall":false,
 "EnableInstallAgentNewECS":true,
 "RequestId":"F35654DB-0C9D-4FB3-903F-479BA7663061",
 "Message":"The Request is not authorization.",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | InvalidParameter | The specified parameter is not valid. |
| 403 | 403 | InvalidAuthorization | The Request is not authorization. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.4.11 DescribeMonitoringAgentAccessKey

Queries the AccessKey ID and AccessKey secret that are required to install the CloudMonitor agent on a third-party host.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C0F655E9-D793- 51E6-BD78- CABBCCFC1047 | The request ID. |
| AccessKey | String | E7A27f9**** | The AccessKey ID that is required to install the agent. |
| SecretKey | String | sBjNOUhLylrxMX- Xv1**** | The AccessKey secret that is required to install the agent. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMonitoringAgentAccessKey
```

Sample success responses `JSON` format `{`

```json
 "SecretKey":"sBjNOUhLylrxMX-Xv1****",
 "RequestId":"C0F655E9-D793-51E6-BD78-CABBCCFC1047",
 "Message":"The specified resource is not found.",
 "AccessKey":"E7A27f9****",
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.4.12 UninstallMonitoringAgent

Uninstalls the CloudMonitor agent from a third-party host.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | host-**** | The ID of the third-party host. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | Successfully | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 466902B9-2842- 40B0-B796- 00FE772B6EF3 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UninstallMonitoringAgent &InstanceId=host-**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"Successfully",
 "RequestId":"466902B9-2842-40B0-B796-00FE772B6EF3",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 412 | 4122 | AgentStateError | Expected agent running state is stopped. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

### 2.5 Alert service

#### 2.5.1 DescribeAlertingMetricRuleResources

Queries the resources that are associated with an alert rule.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RuleId | Strin g | Quer y | No | ruleId-xxxxxx | The ID of the alert rule. |
| GroupId | Strin g | Quer y | No | 123456 | The ID of the application group. |
| Namespac e | Strin g | Quer y | No | acs ecs dashboard _ _ | The namespace of the cloud service. |
| Page | Strin g | Quer y | No | 10 | The page number. |

| PageSize | Strin g | Quer y | No | 10 | The number of entries per page. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Resources | Array | - | The resources that are associated with the alert rule. |
| -RuleId | String | 123456 | The ID of the alert rule. |
| -RuleName | String | rule1 | The name of the alert rule. |
| -GroupId | String | 12345 | The ID of the application group. |
| -Resource | String | 12345 | The associated resource. |
| -Enable | String | true | Indicates whether the role is enabled. |
| -LastAlertTime | String | 1622427900000 | The time when the last alert was triggered for the resource. The value is a timestamp. Unit: milliseconds. |
| - LastModifyTim e | String | 1622827900000 | The time when the alert rule was updated. |
| -StartTime | String | 1622427900000 | The time when the alert rule started to take effect. |
| -MetricValues | String | {\"timestamp\":16 23727500000,\"Su m\":926,\"value\":4 63,\"Maximum\":46 3,\"Minimum\":463, \"Average\":463,\"S ampleCount\":2,\"u serId\":\"12088631 7861****\",\"region \":\"cn- huhehaote\",\"queu e\":\"test-0128\"} | The metric values that triggered the alert. The value is a JSON string. |
| -RetryTimes | String | 3 | The number of retries. |

| -Threshold | String | 5 | The alert threshold. |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID returned when CloudMonitor calls another cloud service. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | Integer | 200 | The HTTP status code. The status code 200 indicates that the request was successful. |
| Message | String | Success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| Total | Integer | 1000 | The total number of entries. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlertingMetricRuleResources &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
 "Message":"Success",
 "Total":1000,
 "Resources":[
```

`{`

```json
   "LastAlertTime":"1622427900000",
   "RuleId":"123456",
   "Resource":"12345",
   "StartTime":"1622427900000",
   "Enable":"true",
   "MetricValues":"
{\\\"timestamp\\\":1623727500000,\\\"Sum\\\":926,\\\"value\\\":463,\\\"Maximum\\\":463,\\ Minimum\\\":463,\\\"Average\\\":463,\\\"SampleCount\\\":2,\\\"userId\\\":\\\"120886317861
**\\\",\\\"region\\\":\\\"cn-huhehaote\\\",\\\"queue\\\":\\\"test-0128\\\"}",
   "LastModifyTime":"1622827900000",
   "RuleName":"rule1",
   "RetryTimes":"3",
   "GroupId":"12345",
   "Threshold":"5"
```

`}` `],`

```json
 "Code":200,
 "Success":true
```

`}` `XML` format

```xml
<RequestId>ACBDBB40-DFB6-4F4C-8957-51FFB233969C</RequestId> <Message>Success</Message> <Total>1000</Total> <Resources>
 <LastAlertTime>1622427900000</LastAlertTime>
 <RuleId>123456</RuleId>
 <Resource>12345</Resource>
 <StartTime>1622427900000</StartTime>
 <Enable>true</Enable>
 <MetricValues>
{\&quot;timestamp\&quot;:1623727500000,\&quot;Sum\&quot;:926,\&quot;value\&quot;:463,\&qu ;Maximum\&quot;:463,\&quot;Minimum\&quot;:463,\&quot;Average\&quot;:463,\&quot;SampleCoun &quot;:2,\&quot;userId\&quot;:\&quot;120886317861****\&quot;,\&quot;region\&quot;:\&quot; -huhehaote\&quot;,\&quot;queue\&quot;:\&quot;test-0128\&quot;}</MetricValues>
 <LastModifyTime>1622827900000</LastModifyTime>
 <RuleName>rule1</RuleName>
 <RetryTimes>3</RetryTimes>
 <GroupId>12345</GroupId>
 <Threshold>5</Threshold>
</Resources> <Code>200</Code> <Success>true</Success>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

Cms 2019-01-01

#### 2.5.2 PutResourceMetricRule

Creates or modifies an alert rule for resource monitoring.

**Authorization method**

You must use an AccessKey (AK) for signature authentication (authType=AK).

**Protocol and method**

Supported protocols: HTTP and HTTPS (recommend) Supported request methods: POST, GET, and PUT

**Considerations**

For the `Resources` parameter, you must pass a URL-encoded resource list in JSON format. The `Escalations.*` parameters configure alert threshold rules for different alert severity levels (Critical, Warn, and Info).

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.This API uses common request headers and has no special request headers. For more information, see the Common Request Parameter documentation.

**Request parameters**

| Paramete r | Typ e | Posi tion | Required | Example | Description |
|---|---|---|---|---|---|

| RuleId | Strin g | Quer y | Yes | rule-abc123 | The ID of the alert rule. For information about how to query the alert rule ID, see DescribeMetricRuleList. |
|---|---|---|---|---|---|
| RuleName | Strin g | Quer y | No | CPU utilization alert | The name of the alert rule. For information about how to query the alert rule name, see DescribeMetricRuleList. |
| MetricNam e | Strin g | Quer y | Yes | cpu total _ | The name of the monitoring item. For information about how to query the monitoring item name, see Cloud service monitoring items. |
| Resources | Strin g | Quer y | Yes | [{"instanceId":"i-xxxx"}] | The list of resources in JSON format. You must URL-encode this parameter. |
| ContactGr oups | Strin g | Quer y | Yes | group1,group2 | The alert contact groups. Separate multiple groups with commas (,). |
| Webhook | Strin g | Quer y | No | https://example.com/web hook | The callback URL to which the system sendsthat the system calls by sending a POST request when an alert is triggered. |
| EffectiveIn terval | Strin g | Quer y | No | 00:00-23:59 | The time period during which the alert rule takes effect. |
| NoEffectiv eInterval | Strin g | Quer y | No | 08:00-18:00 | The time period during which the system suppresses alert notifications. |
| SilenceTim e | Integ er | Quer y | No | 86400 | Default value: 86400. Unit: seconds. |
| Period | Strin g | Quer y | No | 300 | Default value: 300. This value specifies the aggregation period of monitoring data. Unit: seconds. |

| Interval | Strin g | Quer y | No | 60 | The number of consecutive probes. |
|---|---|---|---|---|---|
| EmailSubje ct | Strin g | Quer y | No | [Alert] High ECS CPU utilization | The subject of the alert email. |
| Escalation s.Critical.S tatistics | Strin g | Quer y | No | Average | The statistical method for the Critical level. |
| Escalation s.Critical.C omparison Operator | Strin g | Quer y | No | > | The comparison operator for the Critical level. |
| Escalation s.Critical.T hreshold | Strin g | Quer y | No | 90 | The threshold for the Critical level. |
| Escalation s.Critical.Ti mes | Integ er | Quer y | No | 3 | The number of consecutive triggers for the Critical level. |
| Escalation s.Critical.R ange | Integ er | Quer y | No | 3 | The threshold range that triggers an alert. The system triggers an alert when the metric falls within this range, such as exceeding the baseline for 10 consecutive samples. |
| Escalation s.Warn.Sta tistics | Strin g | Quer y | No | Average | The statistical method for the Warn level. |
| Escalation s.Warn.Co mparisonO perator | Strin g | Quer y | No | > | The comparison operator for the Warn level. |
| Escalation s.Warn.Thr eshold | Strin g | Quer y | No | 80 | The threshold for the Warn level. |

| Escalation s.Warn.Ti mes | Integ er | Quer y | No | 3 | The number of consecutive triggers for the Warn level. |
|---|---|---|---|---|---|
| Escalation s.Warn.Ra nge | Integ er | Quer y | No | 3 | The threshold range that triggers an alert. The system triggers an alert when the metric falls within this range, such as exceeding the baseline for 10 consecutive samples. |
| Escalation s.Info.Stati stics | Strin g | Quer y | No | Average | The statistical method for the Info level. |
| Escalation s.Info.Com parisonOp erator | Strin g | Quer y | No | > | The comparison operator for the Info level. |
| Escalation s.Info.Thre shold | Strin g | Quer y | No | 70 | The threshold for the Info level. |
| Escalation s.Info.Time s | Integ er | Quer y | No | 3 | The number of consecutive triggers for the Info level. |
| Escalation s.Info.Ran ge | Integ er | Quer y | No | 3 | The threshold range that triggers an alert. The system triggers an alert when the metric falls within this range, such as exceeding the baseline for 10 consecutive samples. |
| GroupId | Strin g | Quer y | No | 123456 | The ID of the application group. For information about how to obtain the application group ID, see DescribeMonitorGroups. |
| GroupNam e | Strin g | Quer y | No | testGroup124 | The name of the application group. |

| GroupType | Strin g | Quer y | No | custom | The type of the application group. Example: custom. |
|---|---|---|---|---|---|
| ResourceG roup | Integ er | Quer y | No | 2 | The ID of the resource group. |
| Departme nt | Integ er | Quer y | No | 3 | The ID of the department, which is the ID of the level-1 organization. |
| NoDataPoli cy | Strin g | Quer y | No | KEEP LAST STATE _ _ | The no-data policy. Valid values include KEEP LAST STATE, which _ _ instructs the system to keep the last state. |
| Composite Expression | Strin g | Quer y | No | { "ExpressionList": [ { "ComparisonOperator": "GreaterThanOrEqualToT hreshold", "MetricName": "cpu total", "Period": _ "15", "Statistics": "$Average", "Threshold": 100 }, { "ComparisonOperator": "GreaterThanOrEqualToT hreshold", "MetricName": "memory usedutilization" _ , "Period": "15", "Statistics": "$Average", "Threshold": 100 } ], "ExpressionListJoin": "\|\|", "Times": "5", "Level": "CRITICAL" } | The multi-metric alert expression. This parameter is a JSON format string that includes ExpressionList (the metric list), ExpressionListJoin (the logical operator, such as && or \|\|), Times (the number of consecutive times), and Level (the alert severity). You can use this parameter in multi-metric combined alert scenarios. |
| GroupBy | Strin g | Quer y | No | group | The grouping dimension of the alert rule. Valid values: group (by application group), user (by user), and instance (by instance). |
| Options | Strin g | Quer y | No | [] | The extended options for the rule. This parameter is a JSON string that passes additional configurations for the alert rule. |

| DynamicAl ertHistory DataRange | Integ er | Quer y | No | 7 | The number of days of historical data for dynamic threshold training. This parameter takes effect only when RuleType is DYNAMIC. Valid values include 7 (7 days), 14 (14 days), and 30 (30 days). More historical data improves model accuracy. We recommend that you set this parameter to 14. |
|---|---|---|---|---|---|
| DynamicAl ertSensitiv ity | Strin g | Quer y | No | HIGH | The alert sensitivity for dynamic thresholds. This parameter takes effect only when RuleType is DYNAMIC. Valid values: LOW (low sensitivity, which yields fewer false positives but more false negatives), MEDIUM (medium sensitivity), and HIGH (high sensitivity, which yields fewer false negatives but more false positives). |
| RuleType | Strin g | Quer y | No | DYNAMIC | The rule type. Valid values: STATIC (static threshold, the default value) and DYNAMIC (dynamic threshold/ or intelligent threshold). For a dynamic threshold rule, you must set both DynamicAlertSensitivity and DynamicAlertHistoryData Range, and set Escalations.*.Threshold to the dynamic threshold placeholder function. |
| Namespac e | Strin g | Quer y | Yes | acs ecs dashboard _ _ | The data namespace of the cloud service. This namespace distinguishes different cloud services. Naming format: acs ServiceName. _ |

**Parameter description**

`Resources` : mMust be a valid JSON array string. Each element must contain a resource identifier field such as instanceId. `Escalations.*` : Each alert severity level is configured independently. Alerts will not be triggered for any unconfigured levels.The three alert severity levels have independent configurations. The system does not trigger alerts for unconfigured severity levels. `SilenceTime` : After an alert rule triggers, the system does not send duplicate notifications during the cooldown period.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A3E5D7F1-8B2C- 4D9E-A1F0- 1234567890AB | The unique ID of the request. You can use this ID for troubleshooting. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| Code | String | 200 | The HTTP status code. A value of 200 indicates success. |
| Message | String | success | The error message. |

**Response description**

When `Success` is `false` , `Code` and `Message` contain specific error information. All fields follow the camelCase naming convention.

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=PutResourceMetricRule &RuleId=rule-abc123 &Namespace=acs_ecs_dashboard &MetricName=cpu_total &Resources=[{"instanceId":"i-xxxx"}] &ContactGroups=group1,group2 &Common request parameters
```

Sample success response `JSON` format `{`

```json
 "Message": {
  "parsererror": {
   "h3": [
    "This page contains the following errors:",
    "Below is a rendering of the page up to the first error."
```

`],`

```json
   "div": {
    "_style": "font-family:monospace;font-size:12px",
    "__text": "error on line 2 at column 1: Extra content at the end of the document"
```

`},`

```json
   "_style": "display: block; white-space: pre; border: 2px solid #c77; padding: 0 1em
0 1em; margin: 1em; background-color: #fdd; color: black"
```

`},`

```json
  "__text": "success"
```

`}` `}` `XML` format

```xml
<Message>
 <parsererror  style="display: block; white-space: pre; border: 2px solid #c77; padding
: 0 1em 0 1em; margin: 1em; background-color: #fdd; color: black">
  <h3>This page contains the following errors:</h3>
  <h3>Below is a rendering of the page up to the first error.</h3>
  <div  style="font-family:monospace;font-size:12px">error on line 2 at column 1: Extra
content at the end of the document</div>
 </parsererror>success</Message>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 406 | 406 | ExceedingQuota | Quota exceeded.Exceeding quota limits. |
| 400 | 400 | ParameterInvalid | Invalid parameters. |
| 499 | 499 | %s | %s |
| 204 | 204 | %s | %s |
| 206 | 206 | %s | %s |
| 503 | 503 | %s | %s |

| 400 | 400 | ParameterInvalid | Invalid parameters. |
|---|---|---|---|
| 500 | 500 | InternalError | Failed to process the request due to some unknown errors.An unknown error caused the request processing to fail. |
| 403 | 403 | InvalidAuthorization | Access denied due to iInsufficient permissions. Access Denied. |
| 404 | 404 | ResourceNotFound | The specified resource is not found does not exist. |
| 400 | 400 | ParameterInvalid | Invalid parameters.The parameters are invalid. |

**Additional information**

**Best practices**

Configure Critical and Warn alerts for critical resources. Set `SilenceTime` to an integer multiple of the monitoring period, such as 300 seconds. After you modify a rule, the new configuration takes effect in the next monitoring period.

#### 2.5.3 DescribeAlertHistoryList

Queries historical alerts.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RuleId | Strin g | Quer y | No | applyTemplate61dc81b5- d357-4cf6-a9b7- 9f83c1d5**** | The ID of the alert rule. For more information, see DescribeMetricRuleList. |

| RuleName | Strin g | Quer y | No | ECS Rule _ | The name of the alert rule. For more information, see DescribeMetricRuleList. |
|---|---|---|---|---|---|
| Namespac e | Strin g | Quer y | No | acs ecs dashboard _ _ | The namespace of the cloud service. For more information, see Metrics for Apsara Stack services. |
| MetricNam e | Strin g | Quer y | No | cpu total _ | The metric that is used to monitor the cloud service. For more information, see Metrics for Apsara Stack services. |
| GroupId | Strin g | Quer y | No | 7671**** | The ID of the application group. For more information, see DescribeMonitorGroups. |
| AlertStatus | Strin g | Quer y | No | 2 | Specifies whether alerts are muted. Valid values: 2 (default): Alerts are muted and are not triggered within the mute period, even if the alert condition is met. 0: Alerts are triggered or cleared. 1: The alert rule is ineffective. |
| State | Strin g | Quer y | No | ALARM | The alert status. Valid values: ALARM (default): Alerts are triggered. OK: No alerts are triggered. |
| Ascending | Bool ean | Quer y | No | true | The order of alerts. Valid values: true (default): reverse chronological order false: chronological order |

| StartTime | Strin g | Quer y | No | 1640237400000 | The start timestamp of the historical alerts that you want to query. Unit: milliseconds. |
|---|---|---|---|---|---|
| EndTime | Strin g | Quer y | No | 1640608200000 | The end timestamp of the historical alerts that you want to query. Unit: milliseconds. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10. |
| Page | Integ er | Quer y | No | 1 | The page number. Default value: 1 |
| InstanceId | Strin g | Quer y | No | i-abcdefgh12**** | The instance ID. |
| Level | Strin g | Quer y | No | CRITICAL | The alert level. |
| QueryAll | Bool ean | Quer y | No | 1 | N/A |
| ResourceG roup | Integ er | Quer y | No | ** | The resource set. |
| Departme nt | Integ er | Quer y | No | ** | The ID of the level-1 organization. |
| IncludeEve nt | Bool ean | Quer y | No | false | Specifies whether to query system event- triggered alerts. Default value: false. |
| Category | Strin g | Quer y | No | ecs | The product code. This parameter is valid only for system event- triggered alerts. |

**Response parameters**

| 55 |   |   | > Document Version: 2026090 |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AlarmHistoryLi st | Array | - | The details of historical alerts. |
| - ContactGroups | List | ECS Group _ | The alert contact groups. |
| -Contacts | List | - | The alert contacts. |
| -ContactALIIMs | List | - | The alert contact. |
| -ContactSmses | List | - | The mobile number of the alert contact. |
| -ContactMails | List | - | The email address of the alert contact. |
| -RuleId | String | applyTemplate61d c81b5-d357-4cf6- a9b7-9f83c1d5**** | The ID of the alert rule. |
| -AlertName | String | applyTemplate61d c81b5-d357-4cf6- a9b7-9f83c1d5**** | The ID of the alert rule. |
| -GroupId | String | 7671**** | The ID of the application group. |
| -Namespace | String | acs ecs dashboard _ _ | The namespace of the Alibaba Cloud service. |
| -MetricName | String | cpu total _ | The metric name. |
| -Dimensions | String | {\"instanceId\":\"i- bp1cqhiw1za2****\ "} | The resources that are monitored. |
| -Expression | String | $Average>=10 | The expression that is used to trigger alerts. |
| - EvaluationCou nt | Integer | 3 | The consecutive number of times for which the metric value meets the alert condition before an alert is triggered. |

| -Value | String | 10.58 | The metric value that was recorded when the alert was triggered or cleared. |
|---|---|---|---|
| -AlertTime | Long | 1640586600000 | The time when the alert was triggered. The value is a timestamp. Unit: milliseconds. |
| -LastTime | Long | 360133 | The duration of the alert. Unit: milliseconds. |
| -Level | String | P4 | The severity level and notification methods of the alert. Valid values: <props="china">- P2: Alert notifications are sent by using phone calls, text messages, emails, and DingTalk chatbots. <props="china">- P3: Alert notifications are sent by using text messages, emails, and DingTalk chatbots. <props="china">- P4: Alert notifications are sent by using emails and DingTalk chatbots. <props="china">- OK: No alerts are triggered. <props="intl">- P4: Alert notifications are sent by using emails and DingTalk chatbots. <props="intl">- OK: No alerts are triggered. <props="partner">- P4: Alert notifications are sent by using emails and DingTalk chatbots. <props="partner">- OK: No alerts are triggered. |
| -RuleName | String | ECS Rule _ | The name of the alert rule. |
| -AlertState | String | ALARM | The alert status. Valid values: ALARM: Alerts are triggered. OK: No alerts are triggered. |
| -Status | Integer | 2 | Indicates whether alerts are muted. Valid values: 2 (default): Alerts are muted and are not triggered within the mute period, even if the alert condition is met. 0: Alerts are triggered or cleared. 1: The alert rule is ineffective. |

| -Webhooks | String | https://www.aliyun. com | The callback URL. |
|---|---|---|---|
| - WebhookCode | String | - | The webhook code. |
| - InstanceName | String | i- bp1cqhiw1za2**** | The instance name. |
| -MetricData | String | xxx | The metric data. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The error message. |
| Total | String | 2 | The total number of entries. |
| RequestId | String | C3C69FBE-2262- 541F-A409- C52F380BAE63 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlertHistoryList &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "AlarmHistoryList":[
```

`{`

```json
   "Status":2,
   "ContactGroups":"",
   "RuleId":"applyTemplate61dc81b5-d357-4cf6-a9b7-9f83c1d5****",
   "EvaluationCount":3,
   "Dimensions":"{\\\"instanceId\\\":\\\"i-bp1cqhiw1za2****\\\"}",
   "ContactMails":"",
   "ContactSmses":"",
   "Namespace":"acs_ecs_dashboard",
   "AlertTime":1640586600000,
   "GroupId":"7671****",
   "InstanceName":"i-bp1cqhiw1za2****",
   "MetricName":"cpu_total",
   "Contacts":"",
   "Expression":"$Average>=10",
   "State":"ALARM",
   "Webhooks":"https://www.aliyun.com",
   "Value":"10.58",
   "Level":"P4",
   "PreLevel":"",
   "RuleName":"ECS_Rule",
   "LastTime":360133,
   "ContactALIIMs":""
```

`}` `],`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"C3C69FBE-2262-541F-A409-C52F380BAE63",
 "Total":"2",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |

| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
|---|---|---|---|
| 500 | DEFAULT | InternalError | The request processing has failed due to some unknown error. |

Cms 2019-01-01

#### 2.5.4 DeleteMetricRuleTargets

Deletes the resources that are associated with an alert rule. This operation supports only Message Service (MNS) resources.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RuleId | Strin g | Quer y | Yes | ruleId-xxxxxx | The ID of the alert rule. |
| TargetIds | Repe atLis t | Quer y | No | 12345 | The resource ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the request was successful. |
|---|---|---|---|
| Message | String | The Request is not authorization. | The error message. |
| RequestId | String | 786E92D2-AC66- 4250-B76F- F1E2FCDDBA1C | The request ID. |
| FailIds | Struct | 105 | The IDs of the resources that failed to be deleted. |
| -TargetIds | List | 12345 | The resource ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMetricRuleTargets &RuleId=ruleId-xxxxxx &TargetIds=12345 &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"786E92D2-AC66-4250-B76F-F1E2FCDDBA1C",
 "Code":"200",
 "Success":true,
 "FailIds":{
  "TargetIds":""
```

`}` `}`

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |

| CloudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| 400 | 400 | ParameterInvalid | Illegal parameters. |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 500 | DEFAULT | InternalError | The request processing has failed due to some unknown error. |

Cms 2019-01-01

#### 2.5.5 DescribeActiveMetricRuleList

Queries the alert rules associated with the proactive alerting feature.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| Product | Strin g | Quer y | Yes | ecs | The abbreviation of the cloud service name. The following services support proactive alerting: ecs: Elastic Compute Service (ECS) rds: ApsaraDB RDS slb: Server Load Balancer (SLB) redis standard: _ ApsaraDB for Redis of the standard architecture redis sharding: _ ApsaraDB for Redis of the cluster architecture redis splitrw: ApsaraDB _ for Redis of the read/write splitting architecture mongodb: ApsaraDB for MongoDB of the replica set architecture mongodb sharding: _ ApsaraDB for MongoDB of the sharded cluster architecture hbase: ApsaraDB for HBase elasticsearch: Elasticsearch opensearch: OpenSearch |
|---|---|---|---|---|---|
| Namespac e | Strin g | Quer y | Yes | acs ecs dashboard _ _ | The namespace of the Alibaba Cloud service. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Datapoints | Array | - | The queried alert rules. |
| -RuleId | String | a151cd6023eacee 2f0978e03863cc16 97c89508**** | The ID of the alert rule. |

| -Namespace | String | acs ecs dashboard _ _ | The namespace of the Alibaba Cloud service. For more information, see DescribeMetricRuleList. |
|---|---|---|---|
| -MetricName | String | cpu total _ | The metric name. |
| -Period | String | 60 | The aggregation period of monitoring data. Unit: seconds. The default value is the minimum aggregation period, indicating that the metric is polled at the highest frequency. Typically, you do not need to specify the minimum aggregation period. |
| - EffectiveInterv al | String | 00:00-23:59 | The period of time during which the alert rule is effective. |
| - NoEffectiveInt erval | String | 00:00-06:00 | The period of time during which the alert rule is ineffective. |
| -SilenceTime | String | 86400 | The mute period during which CloudMonitor does not resend an alert notification even if the alert condition is met. Unit: seconds. Default value: 86400. |
| -EnableState | Boolean | true | Indicates whether the alert rule is enabled. Valid values: true: The alert rule is enabled. false: The alert rule is disabled. |
| -AlertState | String | Enable | The status of the alert rule. |
| - ContactGroups | String | ECS Group _ | The alert contact groups. |
| -Webhook | String | http://www.aliyun.c om | The callback URL. |
| -RuleName | String | SystemDefault acs _ rds dashboard Cp _ _ _ uUsage | The name of the alert rule. |

| -Resources | String | [{"resource":" ALL _ "}] | The resources that are associated with the alert rule. A proactive alert rule is associated with all resources. The return value is fixed. |
|---|---|---|---|
| -GroupId | String | 12345 | The ID of the application group. |
| -GroupName | String | ECS Group _ | The name of the application group. |
| -Dimensions | String | "" | The dimensions that specify the resources whose metric data you want to query. The value is a collection of key-value pairs. A typical key-value pair is instanceId:XXXXXX . The key-value pairs can be 1 to 64 bytes in length. Excessive characters are truncated. The key and value can contain letters, digits, periods (.), hyphens (-), underscores ( ), forward slashes (/), and _ backslashes (\). Note Dimensions must be formatted as a JSON string in a specific order. |
| -SourceType | String | METRIC | The type of the alert rule. |
| -NoDataPolicy | String | KEEP LAST STATE _ _ | The method that is used to handle alerts when no monitoring data is found. Valid values: KEEP LAST STATE (default): performs _ _ no operation. INSUFFICIENT DATA: triggers an alert _ whose content is "Insufficient data". OK: considers the status normal. |
| - ExcludeTarget s | String | ["/admin","/api/priv ate"] | A list of excluded targets that are not processed. |
| -InstanceKey | String | 12345 | A unique key value used to identify a specific instance. |
| -Escalations | Struct | 1,2,3 | The conditions for triggering different levels of alerts. |

| --Info | Struct | 1 | The conditions for triggering Info-level alerts. |
|---|---|---|---|
| --- ComparisonOp erator | String | 1 | 1 |
| ---Statistics | String | 1 | 1 |
| ---Threshold | String | 1 | 1 |
| ---Times | String | 1 | 1 |
| ---Range | String | 1 | 1 |
| --Warn | Struct | 1 | The conditions for triggering Warn-level alerts. |
| --- ComparisonOp erator | String | 1 | 1 |
| ---Statistics | String | 1 | 1 |
| ---Threshold | String | 1 | 1 |
| ---Times | String | 1 | 1 |
| ---Range | String | 1 | 1 |
| --Critical | Struct | 1 | The conditions for triggering Critical-level alerts. |
| --- ComparisonOp erator | String | 1 | 1 |
| ---Statistics | String | 1 | 1 |
| ---Threshold | String | 1 | 1 |

| ---Times | String | 1 | 1 |
|---|---|---|---|
| ---Range | String | 1 | 1 |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The error message. |
| RequestId | String | F82E6667-7811- 4BA0-842F- 5B2DC42BBAAD | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeActiveMetricRuleList &Product=ecs &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"F82E6667-7811-4BA0-842F-5B2DC42BBAAD",
 "AlertList":[
```

`{`

```json
   "SilenceTime":"86400",
   "ContactGroups":"ECS_Group",
   "NoEffectiveInterval":"00:00-06:00",
   "MailSubject":"ECS_Bucket",
   "RuleId":"ruleIdxxxx",
   "Period":"60",
   "Dimensions":"\"\"",
   "EffectiveInterval":"00:00-23:59",
   "Namespace":"acs_ecs_dashboard",
```

```json
   "AlertState":"OK",
   "MetricName":"cpu_total",
   "Escalations":[
```

`{`

```json
     "Info":[
```

`{`

```json
       "ComparisonOperator":"",
       "Times":"",
       "Statistics":"",
       "Threshold":""
```

`}` `],`

```json
     "Critical":[
```

`{`

```json
       "ComparisonOperator":"",
       "Times":"",
       "Statistics":"",
       "Threshold":""
```

`}` `],`

```json
     "Warn":[
```

`{`

```json
       "ComparisonOperator":"",
       "Times":"",
       "Statistics":"",
       "Threshold":""
```

`}` `]` `}` `],`

```json
   "EnableState":true,
   "Webhook":"http://www.aliyun.com",
   "Resources":"[{\"resource\":\"_ALL\"}]",
   "RuleName":"myAlert"
```

`}` `],`

```json
 "Datapoints":[
```

`{`

```json
   "SilenceTime":"86400",
   "ContactGroups":"ECS_Group",
   "ComparisonOperator":">",
   "EndTime":"24",
   "RuleId":"a151cd6023eacee2f0978e03863cc1697c89508****",
   "StartTime":"00",
   "EvaluationCount":"3",
   "Period":"60",
   "Statistics":"Average",
   "Namespace":"acs_ecs_dashboard",
   "MetricName":"cpu_total",
   "State":"Enable",
   "Enable":"true",
   "Webhook":"http://www.aliyun.com",
   "RuleName":"SystemDefault_acs_rds_dashboard_CpuUsage",
   "Threshold":"90"
```

`}` `}` `],`

```json
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | InvalidParameter | The specified parameter is not valid. |
| 403 | 403 | InvalidAuthorization | The Request is not authorization. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

Cms 2019-01-01

#### 2.5.6 DescribeProductsOfActiveMetricRule

Queries the cloud services for which the proactive alerting feature is enabled.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AllProductInitM etricRuleList | Array | - | The cloud services for which the proactive alerting feature is enabled. |
| - AlertInitConfig List | Array | - | The alert rule configurations of the cloud services for which the proactive alerting feature is enabled. |

| -- EvaluationCou nt | String | 3 | The consecutive number of times for which the metric value meets the alert condition before an alert is triggered. |
|---|---|---|---|
| --MetricName | String | cpu total _ | The metric name. |
| --Namespace | String | acs ecs dashboard _ _ | The namespace of the Alibaba Cloud service. |
| --Period | String | 60 | The time interval. The value is the same as the interval at which metric data is reported. Unit: seconds. |
| --Statistics | String | Average | The method used to calculate the metric value based on which alerts are triggered. |
| --Level | String | CRITICAL | The alert level. |
| -- ComparisonOp erator | String | GreaterThanOrEqu alToThreshold | The comparison operator that is used to compare the metric value with the threshold for Critical-level alerts. |
| --Escalations | Struct | - | The threshold and the alert level. |
| ---Info | Struct | 1 or 0 | The conditions for triggering Info-level alerts. |
| ---- ComparisonOp erator | String | 1 | 1 |
| ----Statistics | String | 1 | 1 |
| ----Threshold | String | 1 | 1 |
| ----Times | String | 1 | 1 |
| ----Range | String | 1 | 1 |
| ---Warn | Struct | 1 | 1 |

| ---- ComparisonOp erator | String | 1 | 1 |
|---|---|---|---|
| ----Statistics | String | 1 | 1 |
| ----Threshold | String | 1 | 1 |
| ----Times | String | 1 | 1 |
| ----Range | String | 1 | 1 |
| ---Critical | Struct | 1 | 1 |
| ---- ComparisonOp erator | String | 1 | 1 |
| ----Statistics | String | 1 | 1 |
| ----Threshold | String | 1 | 1 |
| ----Times | String | 1 | 1 |
| ----Range | String | 1 | 1 |
| -Product | String | ecs | The abbreviation of the service name. |
| RequestId | String | F82E6667-7811- 4BA0-842F- 5B2DC42BBAAD | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

| Code | Integer | 200 | The HTTP status code. Note The status code 200 indicates that the request was successful. |
|---|---|---|---|
| Message | String | The Request is not authorization. | The error message. |
| Resource | String | ecs,rds | The cloud services for which the proactive alerting feature is enabled. Services are separated with commas (,). Valid values: ecs: Elastic Compute Service (ECS) rds: ApsaraDB RDS slb: Server Load Balancer (SLB) redis standard: ApsaraDB for Redis of _ the standard architecture redis sharding: ApsaraDB for Redis of _ the cluster architecture redis splitrw: ApsaraDB for Redis of the _ read/write splitting architecture mongodb: ApsaraDB for MongoDB of the replica set architecture mongodb sharding: ApsaraDB for _ MongoDB of the sharded cluster architecture hbase: ApsaraDB for HBase elasticsearch: Elasticsearch opensearch: OpenSearch |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeProductsOfActiveMetricRule
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"F82E6667-7811-4BA0-842F-5B2DC42BBAAD",
 "AllProductInitMetricRuleList":[
```

`{`

```json
   "AlertInitConfigList":[
```

`{`

```json
     "MetricName":"",
     "ComparisonOperator":"",
     "EvaluationCount":"",
     "Period":"",
     "Level":"",
     "Statistics":"",
     "Namespace":"",
     "Threshold":""
```

`}` `],`

```json
   "Product":"ecs"
```

`}` `],`

```json
 "Datapoints":"ecs,rds",
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | InvalidParameter | The specified parameter is not valid. |
| 403 | 403 | InvalidAuthorization | The Request is not authorization. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 500 | DEFAULT | InternalError | The request processing has failed due to some unknown error. |

Cms 2019-01-01

#### 2.5.7 DeleteMetricRuleResources

Disassociates resources from an alert rule.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RuleId | Strin g | Quer y | No | rr-bp18017n6iolv**** | The ID of the alert rule. |
| Resources | Strin g | Quer y | Yes | [{"instanceId":"i- uf6hm9lnlzsarrc7****"}] | The resources that are associated with the alert rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the request was successful. |
| Message | String | The alert does not exist. | The error message. |
| RequestId | String | D8A35882-90C6- 4F03-BBEB- 153C180398EA | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMetricRuleResources &RuleId=rr-bp18017n6iolv**** &Resources=[{"instanceId":"i-uf6hm9lnlzsarrc7****"}] &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The alert does not exist.",
 "RequestId":"D8A35882-90C6-4F03-BBEB-153C180398EA",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | DEFAULT | InternalError | The request processing has failed due to some unknown error. |

Cms 2019-01-01

#### 2.5.8 DescribeMetricRuleList

Queries a list of alert rules. This operation supports pagination.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Alarms | Array | [{...}] | The list of alert rules. |

| -RuleId | String | alarm rule 001 _ _ | The ID of the alert rule. |
|---|---|---|---|
| -Namespace | String | acs ecs dashboard _ _ | The namespace of the service. |
| -MetricName | String | CPUUtilization | The name of the metric. |
| -Period | String | 60 | The monitoring period in seconds. |
| - EffectiveInterv al | String | 00:00-23:59 | The effective time range in the HH:MM- HH:MM format. |
| - NoEffectiveInt erval | String | 00:00-06:00 | The time range during which the rule does not take effect. |
| -SilenceTime | String | 86400 | The silence period in seconds. |
| -EnableState | Boolean | true | Indicates whether the alert rule is enabled. |
| -AlertState | String | OK | The alert status. Valid values: OK, ALERT, and INSUFFICIENT DATA _ |
| - ContactGroups | String | default group _ | The alert contact group. |
| -Webhook | String | https://example.co m/webhook | The callback Uniform Resource Locator (URL). |
| -TraceResult | String | false | Indicates whether tracing is enabled. |
| -MailSubject | String | CloudMonitor Alert | The subject of the alert email. |
| -RuleName | String | ECS CPU Alert Rule | The name of the alert rule. |
| -Resources | String | [{"resource":" ALL _ ","region":"cn- wulan-env223- d01"}] | The list of resources for which alarts are generated in JSON array format. |
| -GroupId | String | 12345 | The ID of the application group. |

| -GroupName | String | ECS Group | The name of the application group. |
|---|---|---|---|
| -Dimensions | String | [{"userId":"123456 789","instanceId":"i -xxx"}] | The dimension information of the resource in JSON array format. |
| -SourceType | String | METRIC | The type of the data source. |
| -NoDataPolicy | String | KEEP LAST STATE _ _ | The processing policy when no data is available. |
| -Uuid | String | a1b2c3d4-e5f6- 7890-abcd- ef1234567890 | The unique ID of the alert rule. |
| -GroupBy | String | userId | The grouping field. |
| - ExcludeTarget s | String | [] | The list of excluded targets. |
| -InstanceKey | String | instanceId | The instance identity. |
| -Options | String | {} | The advanced configuration in JSON format. |
| - DynamicAlertS ensitivity | String | medium | The sensitivity of the dynamic alert. |
| - DynamicAlertH istoryDataRan ge | String | 7d | The historical data range of the dynamic alert. |
| -RuleType | String | METRIC | The type of the rule. |
| -TemplateId | Long | 10001 | The ID of the alert template. |
| - CompositeExp ression | Struct | {} | The composite expression configuration. |

| -- ExpressionList | Array | [{...}] | The list of expressions. |
|---|---|---|---|
| ---MetricName | String | CPUUtilization | The name of the metric. |
| ---Period | String | 60 | The monitoring period in seconds. |
| ---Statistics | String | Average | The statistical method. |
| --- ComparisonOp erator | String | GreaterThanThresh old | The comparison operator. |
| ---Threshold | String | 90 | The alert threshold. |
| --- RawExpressio n | String | $Average>90 | The raw expression. |
| ---Id | String | expr 001 _ | The expression ID. |
| --Level | String | CRITICAL | The alert severity. Valid values: CRITICAL, WARN, and INFO |
| -- ExpressionListJ oin | String | && | The logical operator between expressions. Valid values: && (AND) and \|\| (OR) |
| -- ExpressionRa w | String | $Average>90 | The content of the raw expression. |
| --Times | String | 3 | The number of consecutive triggers. |
| --N | String | 1 | The number of alert retries. |
| -Escalations | Struct | {} | The alert escalation rule configuration. |
| --Critical | Struct | {} | The critical-level alert configuration. |

| --- ComparisonOp erator | String | GreaterThanThresh old | The comparison operator. |
|---|---|---|---|
| ---Statistics | String | Average | The statistical method. |
| ---Threshold | String | 90 | The alert threshold. |
| ---Times | String | 3 | The number of consecutive triggers. |
| ---Range | String | {} | The value range. |
| --Warn | Struct | {} | The warning-level alert configuration. |
| --- ComparisonOp erator | String | GreaterThanThresh old | The comparison operator. |
| ---Statistics | String | Average | The statistical method. |
| ---Threshold | String | 90 | The alert threshold. |
| ---Times | String | 3 | The number of consecutive triggers. |
| ---Range | String | {} | The value range. |
| --Info | Struct | {} | The info-level alert configuration. |
| --- ComparisonOp erator | String | GreaterThanThresh old | The comparison operator. |
| ---Statistics | String | Average | The statistical method. |
| ---Threshold | String | 90 | The alert threshold. |
| ---Times | String | 3 | The number of consecutive triggers. |
| ---Range | String | {} | The value range. |

| CloudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| RequestId | String | 15B664E7-1823- 4C84-A59B- 1A3BXXXX | The request ID. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request is successful. Valid values: true (success) and false (failure). |
| Code | Integer | 200 | The status code. A value of 200 indicates success. |
| Message | String | successful | The returned message. |
| Total | String | 10 | The total number of alert rules. |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | InvalidParameter | The specified parameter is invalid. |
| 403 | 403 | InvalidAuthorization | The request is not authorized. |
| 500 | 500 | InternalError | The system failed to process the request due to some unknown errors. |

#### 2.5.9 DescribeMetricRuleCount

Queries the number of alert rules in each status.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Success | Boolean | true | Indicates whether the request is successful. Valid values: true (successful) and false (failed) |
|---|---|---|---|
| Code | String | 200 | The status code. A value of 200 indicates success. |
| Message | String | successful | The response message. The system returns successful when the request succeeds. |
| RequestId | String | 15B664E7-1823- 4C84-A59B- 1A3BXXXX | The request ID. |
| MetricRuleCou nt | Struct | {} | The number of alert rules in each status. |
| -Alarm | Integer | 5 | The number of rules in the Alarm state. |
| -Disable | Integer | 2 | The number of rules in the Disabled state. |
| -Nodata | Integer | 0 | The number of rules in the Nodata state. |
| -Ok | Integer | 10 | The number of rules in the Ok status. |
| -Total | Integer | 17 | The total number of alert rules. |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | The parameters is invalid. |
| 403 | 403 | InvalidAuthorization | Permission denied. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 402 | 402 | LimitExceeded | The quota for this customer has been reached. |

| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
|---|---|---|---|
| 500 | 500 | InternalError | The system failed to process the request due to some unknown errors. |

#### 2.5.10 DeleteMetricRules

Deletes specified alert rules.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request succeeded. Valid values: true (success) and false (failure). |
| Code | String | 200 | The status code. A value of 200 indicates success. |
| Message | String | successful | The response message. The system returns "successful" when the request succeeds. |
| RequestId | String | 15B664E7-1823- 4C84-A59B- 1A3BXXXX | The request ID. |

**Error codes**

| HttpCode | Error Code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Invalid parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

| 401 | 401 | AccessDeniedException | You do not have sufficient permissions to perform this operation. |
|---|---|---|---|
| 402 | 402 | LimitExceeded | The quota for this customer has been reached. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 500 | 500 | InternalError | The request processing failed due to some unknown errors. |

#### 2.5.11 DisableMetricRules

Disables an alert rule.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RuleId | Repe atLis t | Quer y | Yes | RuleId | The ID of the alert rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true or false | Indicates whether the request was successful. Valid values: true false |
| Code | String | 200 | The HTTP status code. The status code 200 indicates that the request was successful. |

| Message | String | Success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DisableMetricRules &RuleId=RuleId &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"Success",
 "RequestId":"ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
 "Code":"200",
 "Success":false
```

`}` `XML` format

```
<Message /> <RequestId /> <Code /> <Success />
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |

| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
|---|---|---|---|
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

Cms 2019-01-01

#### 2.5.12 EnableMetricRules

Enables alert rules.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RuleId | Repe atList | Query | Yes | ab05733c97b7ce239fb1 b53393dc1697c123**** | The ID of the alert rule. You can call the DescribeMetricRuleList operation to obtain the ID of the alert rule. Valid values of N: 1 to 100. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. |
| Code | String | 200 | The response code. |
| Message | String | success | The returned message. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FF38D33A-67C1- 40EB-AB65- FAEE**** | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableMetricRules &RuleId=ab05733c97b7ce239fb1b53393dc1697c123**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"FF38D33A-67C1-40EB-AB65-FAEE****",
 "Code":"200",
 "Success":true
```

`}` `XML` format

```xml
<Message>success</Message> <RequestId>FF38D33A-67C1-40EB-AB65-FAEE****</RequestId> <Code>200</Code> <Success>true</Success>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | %s | %s |
| 403 | 403 | %s | %s |
| 404 | 404 | %s | %s |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 500 | 500 | %s | %s |
| 503 | 503 | %s | %s |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 |   | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.13 DeleteContact

Deletes an alert contact.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ContactNa me | Strin g | Query | Yes | Zhang San | The name of the alert contact. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |
| RequestId | String | 50D4CFE1-01E5- 4543-939C- 18BC01E3EC1C | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteContact &ContactName=Zhang San &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"50D4CFE1-01E5-4543-939C-18BC01E3EC1C",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | InvalidParameterValue | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.14 DescribeMetricRuleTargets

Queries the resources that are associated with a specified alert rule.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RuleId | Strin g | Quer y | Yes | ae06917 75a8c43178ab6 _ 6**** | The ID of the alert rule. For more information about how to query the IDs of alert rules, see DescribeMetricRuleList. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Targets | Array |   | The information about the resources for which alerts are triggered. |

| -Id |   |   | String | 1 |   |   | The ID of the resource for which alerts are triggered. |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | The Alibaba Cloud Resource Name (ARN) of the resource. Format: acs:{Service |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | acs:{Service |   |
|   |   |   |   |   |   |   | name abbreviation}:{regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {userId}:/{Resource type}/{Resource |   |   |   |   |
|   |   |   |   |   |   |   | name}/message |   | . Example: |   |   |
| -Arn |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | hangzhou:120886317861****:/queues/tes |   |   |   |   |
|   |   |   |   |   |   |   | t123/message |   |   |   |   |
|   |   |   | String | acs:mns:cn- hangzhou:1208863 17861****:/queues /test/message |   |   |   |   |   |   |   |
| -Level |   |   | String | INFO |   |   | The alert level. Valid values: INFO WARN CRITICAL |   |   |   |   |
| Code |   |   | String | 200 |   |   | The response code. The status code 200 indicates that the request was successful. |   |   |   |   |
| Message |   |   | String | User not authorized to operate on the specified resource. |   |   | The returned message. |   |   |   |   |
| RequestId |   |   | String | 786E92D2-AC66- 4250-B76F- F1E2FCDDBA1C |   |   | The request ID. |   |   |   |   |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricRuleTargets &RuleId=ae06917_75a8c43178ab66**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"User not authorized to operate on the specified resource.",
 "RequestId":"786E92D2-AC66-4250-B76F-F1E2FCDDBA1C",
 "Targets":{
  "Level":"INFO",
  "Id":"1",
  "Arn":"acs:mns:cn-hangzhou:120886317861****:/queues/test/message"
```

`},`

```json
 "Code":"200"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.15 DescribeEventRuleList

Queries event-triggered alert rules.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| NamePrefi x | Strin g | Query | No | test | The name prefix of the event-triggered alert rule. |

| Developer Gui | de·API R | eference |   |   | CloudMonito |
|---|---|---|---|---|---|
| Parame ter | Typ e | Locati on | Require d | Example | Description |
| PageNum ber | Strin g | Query | No | 1 | The page number. Pages start from page 1. Default value: 1. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page. Pages start from page 1. Default value: 10. |
| GroupId | Strin g | Query | No | 7378**** | The ID of the application group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| EventRules | Array |   | The event-triggered alert rule. |
| -EventPattern | Array |   | The mode of the event-triggered alert rule. |
| --NameList | Normal | value | The event name. |
| --LevelList | Normal | value | The levels of the event-triggered alerts. |
| -- EventTypeList | Normal | value | The types of the event-triggered alert rules. |
| --Product | String | value | The abbreviation of the Alibaba Cloud service name. |
| -Name | String | test DefaultEventR _ ule 7378**** _ | The name of the event-triggered alert rule. |
| -GroupId | String | 7378**** | The ID of the application group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -EventType | String | SYSTEM | The type of the event-triggered alert rule. Valid values: SYSTEM: system event-triggered alert rule CUSTOM: custom event-triggered alert rule |
| -State | String | ENABLED | The status of the event-triggered alert rule. Valid values: ENABLED DISABLED |
| -Description | String | Default group event rule. | The description of the event-triggered alert rule. |
| - ContactGroups | String |   | The contact groups. |
| -Webhook | String |   | The API URL. |
| -RuleId | String |   | The rule ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | User not authorized to operate on the specified resource. | The returned message. |
| RequestId | String | D0E6D82B-16B5- 422A-8136- EE5BDC01E415 | The request ID. |
| Total | Integer | 21 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEventRuleList &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"User not authorized to operate on the specified resource.",
 "RequestId":"D0E6D82B-16B5-422A-8136-EE5BDC01E415",
 "Total":21,
 "EventRules":{
  "ContactGroups":"",
  "Description":"Default group event rule.",
  "EventType":"SYSTEM",
  "State":"ENABLED",
  "RuleId":"",
  "Webhook":"",
  "-EventPattern":{
   "NameList":"",
   "LevelList":"",
   "EventTypeList":"",
   "Product":""
```

`},`

```json
  "Name":"test_DefaultEventRule_7378****",
  "GroupId":"7378****"
```

`},`

```json
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | InvalidParameterValue | Illegal parameters. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.16 DescribeMetricRuleTemplateList

Queries alert templates.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Quer y | No | ECS Template1 _ | The name of the alert template. |
| Keyword | Strin g | Quer y | No | ECS | The keyword of the alert template name. |
| TemplateI d | Long | Quer y | No | 70**** | The ID of the alert template. |
| PageNumb er | Long | Quer y | No | 1 | The page number. Default value: 1. |
| PageSize | Long | Quer y | No | 10 | The number of entries per page. |
| History | Bool ean | Quer y | No | false | Specifies whether to display the history of applying the alert templates to application groups. Valid values: true false (default) |
| IsDefault | Bool ean | Quer y | No |   | The default value. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Templates | Array |   | The queried alert templates. |
| - ApplyHistories | Array |   | The history of applying the alert templates to application groups. |
| --GroupId | Long | 36070001 | The ID of the application group. |
| --GroupName | String | ECS Group _ | The name of the application group. |

| --ApplyTime | Long | 1646055898000 | The timestamp when the alert template was applied to the application group. Unit: milliseconds. |
|---|---|---|---|
| -Name | String | ECS Template1 _ | The name of the alert template. |
| -NameSpace | String |   | The name of the namespace. |
| -Description | String | ECS CPU utilization | The description of the alert template. |
| -RestVersion | Long | 0 | The version of the alert template. Default value: 0. |
| -TemplateId | Long | 70**** | The ID of the alert template. |
| -GmtCreate | Long | 1646018798000 | The timestamp when the alert template was created. Unit: milliseconds. |
| -GmtModified | Long | 1646054798000 | The timestamp when the alert template was modified. Unit: milliseconds. |
| RequestId | String | 659401C0-6214- 5C02-972A- CFA929D717B7 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The returned message. |
| Total | Integer | 2 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricRuleTemplateList &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"659401C0-6214-5C02-972A-CFA929D717B7",
 "Total":2,
 "Templates":{
  "GmtCreate":1646018798000,
  "Description":"ECS CPU utilization",
  "-ApplyHistories":{
   "GroupName":"",
   "ApplyTime":"",
   "GroupId":""
```

`},`

```json
  "GmtModified":1646054798000,
  "NameSpace":"",
  "RestVersion":0,
  "TemplateId":"70****",
  "Name":"ECS_Template1"
```

`},`

```json
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.17 DescribeContactList

Queries alert contacts.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | No | 10 | The number of entries per page. Default value: 100. |
| PageNum ber | Integ er | Query | No | 1 | The page number. Default value: 1. |
| ContactNa me | Strin g | Query | No | Alice | The name of the alert contact. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Contacts | Array |   | The alert contacts. |
| -Name | String | Alice | The name of the alert contact. |
| -Desc | String | ECS alert contact | The description. |
| -CreateTime | Long | 1552356159000 | The timestamp when the alert contact was created. Unit: milliseconds. |
| -UpdateTime | Long | 1552356159000 | The timestamp when the alert contact was updated. Unit: milliseconds. |
| -Channels | Struct | Channels | The alert notification methods. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| --SMS | String | value | The text message. |
| --Mail | String | value | The email address. |
| --AliIM | String | value | The TradeManager. |
| -- DingWebHook | String | value | DingWebHook |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The returned message. |
| Total | Integer | 15 | The total number of entries returned. |
| RequestId | String | 06D5ECC2-B9BE- 42A4-8FA3- 1A610FB08B83 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeContactList &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"06D5ECC2-B9BE-42A4-8FA3-1A610FB08B83",
 "Contacts":{
  "Desc":"ECS alert contact",
  "CreateTime":1552356159000,
  "UpdateTime":1552356159000,
  "-Channels":{
   "Mail":"",
   "AliIM":"",
   "DingWebHook":"",
   "SMS":""
```

`},`

```json
  "Name":"Alice"
```

`},`

```json
 "Total":15,
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.18 ApplyMetricRuleTemplate

Applies an alert template to an application group to generate an alert rule.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|

| SilenceTim e | Long | Quer y | No | 86400 | The mute period during which new alert notifications are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400. Only one alert notification is sent during a mute period even if the metric value exceeds the alert threshold during consecutive checks. |
|---|---|---|---|---|---|
| GroupId | Long | Quer y | Yes | 123456 | The ID of the application group. For more information about how to query the IDs of application groups, see DescribeMonitorGroups. |
| TemplateI ds | Strin g | Quer y | Yes | 700**** | The ID of the alert template. For more information about how to query the IDs of alert templates, see DescribeMetricRuleTempl ateList. |
| EnableStar tTime | Long | Quer y | No | 00 | The start of the time period during which the alert rule is effective. Valid values: 00 to 23. A value of 00 indicates 00:00 and a value of 23 indicates 23:00. |
| EnableEnd Time | Long | Quer y | No | 23 | The end of the time period during which the alert rule is effective. Valid values: 00 to 23. A value of 00 indicates 00:59 and a value of 23 indicates 23:59. |

| NotifyLeve l | Long | Quer y | No | 4 | The alert notification method. Valid values: China site: 2: Alert notifications are sent by using phone calls, text messages, emails, TradeManager messages, and DingTalk chatbots. 3: Alert notifications are sent by using text messages, emails, TradeManager messages, and DingTalk chatbots. 4: Alert notifications are sent by using TradeManager messages and DingTalk chatbots. International site: 4: Alert notifications are sent by using TradeManager messages and DingTalk chatbots. Site for virtual network operators (VNOs): 4: Alert notifications are sent by using TradeManager messages and DingTalk chatbots. |
|---|---|---|---|---|---|

| ApplyMode | Strin g | Quer y | No | GROUP INSTANCE FIRST _ _ | The mode in which the alert template is applied. Valid values: GROUP INSTANCE FIRS _ _ T: The metrics in the application group take precedence. If a metric specified in the alert template does not exist in the application group, the system does not generate an alert rule for the metric based on the alert template. ALARM TEMPLATE FIRS _ _ T: The metrics specified in the alert template take precedence. If a metric specified in the alert template does not exist in the application group, the system still generates an alert rule for the metric based on the alert template. |
|---|---|---|---|---|---|
| Webhook | Strin g | Quer y | No | https://www.aliyun.com | The callback URL to which a POST request is sent when an alert is triggered based on the alert rule. |
| ContactGr oups | Strin g | Quer y | No | 1 | The alert contact groups. |
| ResourceG roupId | Strin g | Quer y | No | 1 | The ID of the resource group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3F897F3C-020A- 4993-95B4- 63ABB84F83E6 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
|---|---|---|---|
| Message | String | The specified resource is not found. | The returned message. |
| Resource | Struct |   | The resources that are affected by the alert rule. |
| -AlertResults | Array |   | The resources that are affected by the alert rule. |
| --GroupId | Long | 123456 | The ID of the application group. |
| --RuleId | String | applyTemplate8ab 74c6b-9f27-47ab- 8841- de01dc08**** | The ID of the alert rule. |
| --Message | String | alert rule is creating, please wait a few minutes. | The returned message. |
| --RuleName | String | test123 | The name of the alert rule. |
| --Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| --Success | Boolean | value | Indicates whether the request was successful. Valid values: true false |
| -GroupId | Long | 123456 | The ID of the application group. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ApplyMetricRuleTemplate &GroupId=123456 &TemplateIds=700**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"3F897F3C-020A-4993-95B4-63ABB84F83E6",
 "Resource":{
  "-AlertResults":{
   "Message":"",
   "RuleId":"",
   "Code":"",
   "RuleName":"",
   "Success":"",
   "GroupId":""
```

`},`

```json
  "GroupId":""
```

`},`

```json
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.19 DescribeEventRuleTargetList

Queries the details of an event-triggered alert rule.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RuleName | Strin g | Quer y | Yes | testRule | The name of the event- triggered alert rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ContactParam eters | Array |   | The information about the alert contact groups that receive alert notifications. |
| - ContactGroup Name | String | Default alert contact group | The name of the alert contact group. |
| -Level | String | 3 | The alert notification methods. Valid values: China site: 2: Alert notifications are sent by using phone calls, text messages, DingTalk, and emails. 3: Alert notifications are sent by using text messages, DingTalk, and emails. 3: Alert notifications are sent by using DingTalk and emails. International site: 4: Alert notifications are sent by using DingTalk and emails. Site for virtual network operators (VNOs): 4: Alert notifications are sent by using DingTalk and emails. |
| -Id | String | 2 | The ID of the recipient. |
| FcParameters | Array |   | The information about the recipients in Function Compute. |
| -Region | String | cn-hangzhou | The region where Message Service (MNS) is deployed. |
| 05 |   |   | > Document Version: 2026090 |

|   | loudMonitor |   |   |   | Developer Guide·API Referenc |   |
|---|---|---|---|---|---|---|
|   | -ServiceName |   | String | service1 | The name of the Function Compute service. |   |
|   | - FunctionName |   | String | fcTest1 | The function name. |   |
|   | -Id |   | String | 2 | The ID of the recipient. |   |
|   | -Arn |   |   |   | The Alibaba Cloud Resource Name (ARN) of the function. Format: arn:acs:${Service}:${Region}:${Accou nt}:${ResourceType}/${ResourceId} . Fields: Service: the code of an Alibaba Cloud service Region: the region ID Account: the ID of an Alibaba Cloud account ResourceType: the resource type ResourceId: the resource ID |   |
|   |   |   |   |   |   | arn:acs:${Service}:${Region}:${Accou |
|   |   |   |   |   | nt}:${ResourceType}/${ResourceId} |   |
|   |   |   | String | acs:log:cn- hangzhou::project/ cms-log- mon***/logstore/cx xxx*** |   |   |
|   | MnsParameter s |   | Array |   | The information about the recipients in MNS. |   |
|   | -Region |   | String | cn-hangzhou | The region where MNS is deployed. |   |
|   | -Queue |   | String | testQueue | The name of the queue. |   |
|   | -Id |   | String | 2 | The ID of the recipient. |   |
|   | -Arn |   |   |   | The ARN of the function. Format: arn:acs:${Service}:${Region}:${Accou nt}:${ResourceType}/${ResourceId} . Fields: Service: the code of an Alibaba Cloud service Region: the region ID Account: the ID of an Alibaba Cloud account ResourceType: the resource type ResourceId: the resource ID |   |
|   |   |   |   |   |   | arn:acs:${Service}:${Region}:${Accou |
|   |   |   |   |   | nt}:${ResourceType}/${ResourceId} |   |
|   |   |   | String | acs:log:cn- hangzhou::project/ cms-log- mon***/logstore/cx xxx*** |   |   |
|   | > Document Versi |   | on: 20260902 |   | 20 |   |

| WebhookPara meters |   | Array |   | The information about the callback URLs that are used to receive alert notifications. |   |
|---|---|---|---|---|---|
| -Id |   | String | 2 | The ID of the recipient. |   |
| -Protocol |   | String | HTTP | The protocol type. |   |
| -Method |   | String | GET | The HTTP request method. Valid values: GET and POST. |   |
| -Url |   | String | http://www.aliyun.c om | The callback URL. |   |
| SlsParameters |   | Array |   | The information about the recipients in Simple Log Service. |   |
| -Id |   | String | 2 | The ID of the recipient. |   |
| -Region |   | String | cn-hangzhou | The region where MNS is deployed. |   |
| -Project |   | String | project test _ | The project name. |   |
| -LogStore |   | String | logstore test _ | The Logstore name. |   |
| -Arn |   |   |   | The ARN of the function. Format: arn:acs:${Service}:${Region}:${Accou nt}:${ResourceType}/${ResourceId} . Fields: Service: the code of an Alibaba Cloud service Region: the region ID Account: the ID of an Alibaba Cloud account ResourceType: the resource type ResourceId: the resource ID |   |
|   |   |   |   |   | arn:acs:${Service}:${Region}:${Accou |
|   |   |   |   | nt}:${ResourceType}/${ResourceId} |   |
|   |   | String | acs:log:cn- hangzhou::project/ cms-log- mon***/logstore/cx xxx*** |   |   |
| Code |   | String | 200 | The response code. The status code 200 indicates that the request was successful. |   |

| 07 |   |   | > Document Version: 2026090 |
|---|---|---|---|

| Message | String | The Request is not authorization. | The returned message. |
|---|---|---|---|
| RequestId | String | 87170bc7-e28a- 4c93-b9bf- 90a1dbe84736 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEventRuleTargetList &RuleName=testRule &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"87170bc7-e28a-4c93-b9bf-90a1dbe84736",
 "ContactParameters":{
  "ContactGroupName":"Default alert contact group",
  "Level":"3",
  "Id":"1"
```

`},`

```json
 "SlsParameters":{
  "Project":"project_test",
  "LogStore":"logstore_test",
  "Region":"cn-hangzhou",
  "Id":"4",
  "Arn":"acs:log:cn-hangzhou::project/cms-log-mo****/logstore/c***"
```

`},`

```json
 "WebhookParameters":{
  "Id":"5",
  "Method":"GET",
  "Protocol":"HTTP",
  "Url":"http://www.aliyun.com"
```

`},`

```json
 "FcParameters":{
  "FunctionName":"fcTest1",
  "ServiceName":"service1",
  "Region":"cn-qingdao",
  "Id":"3",
  "Arn":"acs:log:cn-hangzhou::project/cms-log-mon***/logstore/cxxxx***"
```

`},`

```json
 "Code":"200",
 "MnsParameters":{
  "Region":"cn-hangzhou",
  "Id":"2",
  "Arn":"acs:log:cn-hangzhou::project/cms-log-mon***/logstore/cxxxx***",
  "Queue":"testQueue"
```

`}` `}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | InvalidParameterValue | Illegal parameters. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.20 DescribeMetricRuleTemplateAttribute

Queries the details of an alert template.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Query | No | ECS Template1 _ | The name of the alert template. You must specify at least one of the Name and TemplateId parameters. For more information about how to query the names of alert templates, see DescribeMetricRuleTem plateList. |
| TemplateI d | Strin g | Query | No | 70**** | The ID of the alert template. You must specify at least one of the Name and TemplateId parameters. For more information about how to query the names of alert templates, see DescribeMetricRuleTem plateList. |
| IsSystemD efault | Boole an | Query | No | 1 | The default value. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8F3A82AD-DA92- 52B0-8EC6- C059D1C3839F | The request ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |
| Resource | Struct | Resource | The details of the alert template. |
| - AlertTemplate s | Array | AlertTemplates | The details of the alert templates. |
| --RuleName | String | ECS Rule _ | The name of the alert rule. |
| --Category | String | ecs | The abbreviation of the Alibaba Cloud service name. |
| --Namespace | String | acs ecs dashboard _ _ | The namespace of the Alibaba Cloud service. |
| --MetricName | String | cpu total _ | The metric name. |
| --Selector | String | {"disk":"/"} | The dimension of the alert. It is an extended field. |
| --Escalations | Struct |   | The threshold and the alert level. |
| ---Info | Struct |   | The conditions that trigger Info-level alerts. |
| ----Statistics | String | Average | The statistical method for Warn-level alerts. The valid values of the Statistics parameter vary based on services. For more information, see Appendix 1: Metrics. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ---- ComparisonOp erator | String | GreaterThanOrEqu alToThreshold | The comparison operator that is used to compare the metric value with the threshold for Critical-level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to the threshold GreaterThanThreshold: greater than the threshold LessThanOrEqualToThreshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
| ----Threshold | String | 90 | The threshold for Warn-level alerts. |
| ----Times | Integer | 5 | The consecutive number of times for which the metric value meets the alert condition before a Critical-level alert is triggered. |
| ----Range | Integer | 1 | The scope. |
| ---Warn | Struct |   | The conditions that trigger Warn-level alerts. |
| ----Statistics | String | Average | The statistical method for Warn-level alerts. The valid values of the Statistics parameter vary based on services. For more information, see Appendix 1: Metrics. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ---- ComparisonOp erator | String | GreaterThanOrEqu alToThreshold | The comparison operator that is used to compare the metric value with the threshold for Critical-level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to the threshold GreaterThanThreshold: greater than the threshold LessThanOrEqualToThreshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
| ----Threshold | String | 90 | The threshold for Warn-level alerts. |
| ----Times | Integer | 5 | The consecutive number of times for which the metric value meets the alert condition before a Critical-level alert is triggered. |
| ----Range | Integer | 1 | The scope. |
| ---Critical | Struct |   | The conditions that trigger Critical-level alerts. |
| ----Statistics | String | Average | The statistical method for Warn-level alerts. The valid values of the Statistics parameter vary based on services. For more information, see Appendix 1: Metrics. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ---- ComparisonOp erator | String | GreaterThanOrEqu alToThreshold | The comparison operator that is used to compare the metric value with the threshold for Critical-level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to the threshold GreaterThanThreshold: greater than the threshold LessThanOrEqualToThreshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
| ----Threshold | String | 90 | The threshold for Warn-level alerts. |
| ----Times | Integer | 5 | The consecutive number of times for which the metric value meets the alert condition before a Critical-level alert is triggered. |
| ----Range | Integer | 1 | The scope. |
| -Name | String | ECS Template1 _ | The name of the alert template. |
| -TemplateId | String | 70**** | The ID of the alert template. |
| -RestVersion | String | 1 | The version of the alert template. |
| -Description | String | ECS alert template | The description of the alert template. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricRuleTemplateAttribute &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"8F3A82AD-DA92-52B0-8EC6-C059D1C3839F",
 "Resource":{
  "Description":"",
  "-AlertTemplates":{
   "MetricName":"",
   "Category":"",
   "--Escalations":{
    "---Info":{
     "ComparisonOperator":"",
     "Times":"",
     "Range":"",
     "Statistics":"",
     "Threshold":""
```

`},`

```json
    "---Critical":{
     "ComparisonOperator":"",
     "Times":"",
     "Range":"",
     "Statistics":"",
     "Threshold":""
```

`},`

```json
    "---Warn":{
     "ComparisonOperator":"",
     "Times":"",
     "Range":"",
     "Statistics":"",
     "Threshold":""
```

`}` `},`

```json
   "RuleName":"",
   "Namespace":"",
   "Selector":""
```

`},`

```json
  "RestVersion":"",
  "TemplateId":"",
  "Name":""
```

`},`

```json
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.21 DescribeEventRuleAttribute

Queries the details of an event-triggered alert rule.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RuleName | Strin g | Quer y | Yes | testRule | The name of the event- triggered alert rule. For more information about how to query the names of event-triggered alert rules, see DescribeEventRuleList. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
|---|---|---|---|
| Message | String | The alert does not exist. | The returned message. |
| RequestId | String | 9AA3F210-C03D- 4C86-8DB6- 21C84FF692A1 | The request ID. |
| Result | Struct |   | The details of the event-triggered alert rule. |
| -Description | String | Default group event rule. | The description of the event-triggered alert rule. |
| -Name | String | test DefaultEventR _ ule 7378**** _ | The name of the event-triggered alert rule. |
| -EventType | String | SYSTEM | The event type. Valid values: SYSTEM: system event-triggered alert rule CUSTOM: custom event-triggered alert rule |
| -GroupId | String | 3607**** | The ID of the application group. |
| -State | String | ENABLED | The status of the event-triggered alert rule. Valid values: ENABLED DISABLED |
| -EventPattern | Struct |   | The event pattern. This parameter describes the trigger conditions of an event. |
| --NameList | Normal | Agent Status Runn _ _ ing | The event name. |
| --StatusList | Normal | Running | The event status. |

| --LevelList | Normal | ["CRITICAL","WARN "] | The level of the event-triggered alert rule. Valid values: CRITICAL WARN INFO |
|---|---|---|---|
| --Product | String | CloudMonitor | The name of the cloud service. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEventRuleAttribute &RuleName=testRule &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The alert does not exist.",
 "RequestId":"9AA3F210-C03D-4C86-8DB6-21C84FF692A1",
 "Code":"200",
 "Success":true,
 "Result":{
  "Description":"",
  "EventType":"",
  "State":"",
  "-EventPattern":{
   "NameList":"",
   "LevelList":"",
   "StatusList":"",
   "Product":""
```

`},`

```json
  "Name":"",
  "GroupId":""
```

`}` `}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | InvalidParameterValue | Illegal parameters. |

| 404 | 404 | ResourceNotFound | The specified resource is not found. |
|---|---|---|---|
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.22 DescribeContactListByContactGroup

Queries the alert contacts in an alert contact group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ContactGr oupName | Strin g | Query | Yes | CloudMonitor | The name of the alert contact group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Contacts | Array |   | The alert contacts that receive alert notifications. |
| -Name | String | Alice | The name of the alert contact. |
| -Desc | String | ECS | The description of the alert contact. |
| -CreateTime | Long | 1552314252000 | The time when the alert contact was created. |
| -UpdateTime | Long | 1552314252000 | The time when the alert contact was modified. |
| -Channels | Struct |   | The alert notification methods. |
| --SMS | String | 1333333**** | The mobile number of the alert contact. This parameter is valid only on the China site (aliyun.com). |

| CloudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |

| --Mail | String | alice@example.co m | The email address of the alert contact. |
|---|---|---|---|
| --AliIM | String | Alice | The TradeManager ID of the alert contact. This parameter is valid only on the China site (aliyun.com). |
| -- DingWebHook | String | https://oapi.dingtal k.com/robot/send? access token=9bf4 _ 4f8189597d07dfdd 7a123455ffc112*** * | The webhook URL of the DingTalk chatbot. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The group is not exists. | The returned message. |
| RequestId | String | 06D5ECC2-B9BE- 42A4-8FA3- 1A610FB08B83 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeContactListByContactGroup &ContactGroupName=CloudMonitor &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The group is not exists.",
 "RequestId":"06D5ECC2-B9BE-42A4-8FA3-1A610FB08B83",
 "Contacts":{
  "Desc":"ECS",
  "CreateTime":1552314252000,
  "UpdateTime":1552314252000,
  "-Channels":{
   "Mail":"alice@example.com",
   "AliIM":"Alice",
   "DingWebHook":"https://oapi.dingtalk.com/robot/send?
access_token=9bf44f8189597d07dfdd7a123455ffc112****",
   "SMS":"1333333****"
```

`},`

```json
  "Name":"Alice"
```

`},`

```json
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.23 PutContact

Creates or modifies an alert contact.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ContactNa me | Strin g | Query | Yes | Alice | The name of the alert contact. |

|   | CloudMonitor |   |   |   | Dev | eloper Guide·API Referenc | e |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Describe | Strin g | Query | Yes | ECS Instance _ | The description of the alert contact. |
| Channels. SMS | Strin g | Query | No | 1333333**** | The phone number of the alert contact. After you add or modify a phone number, the recipient receives a text message that contains an activation link. The system adds the recipient to the list of alert contacts only after the recipient activates the phone number. China site: At least one of the following alert notification targets must be specified: phone number, email address, webhook URL of the DingTalk chatbot, and TradeManager ID. International site: At least one of the following alert notification targets must be specified: email address and webhook URL of the DingTalk chatbot. Site for virtual network operators (VNOs): At least one of the following alert notification targets must be specified: email address and webhook URL of the DingTalk chatbot. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Channels. Mail | Strin g | Query | No | t***@aliyun.com | The email address of the alert contact. After you add or modify an email address, the recipient receives an email that contains an activation link. The system adds the recipient to the list of alert contacts only after the recipient activates the email address. China site: At least one of the following alert notification targets must be specified: phone number, email address, webhook URL of the DingTalk chatbot, and TradeManager ID. International site: At least one of the following alert notification targets must be specified: email address and webhook URL of the DingTalk chatbot. Site for VNOs: At least one of the following alert notification targets must be specified: email address and webhook URL of the DingTalk chatbot. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Channels. AliIM | Strin g | Query | No | Jim | The TradeManager ID of the alert contact. China site: At least one of the following alert notification targets must be specified: phone number, email address, webhook URL of the DingTalk chatbot, and TradeManager ID. International site: At least one of the following alert notification targets must be specified: email address and webhook URL of the DingTalk chatbot. Site for VNOs: At least one of the following alert notification targets must be specified: email address and webhook URL of the DingTalk chatbot. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Channels. DingWebH ook | Strin g | Query | No | https://oapi.dingtalk.com /robot/send? access token=7d49515 _ e8ebf21106a80a9cc4bb 3d247771305d52fb15d6 201234565**** | The webhook URL of the DingTalk chatbot. China site: At least one of the following alert notification targets must be specified: phone number, email address, webhook URL of the DingTalk chatbot, and TradeManager ID. International site: At least one of the following alert notification targets must be specified: email address and webhook URL of the DingTalk chatbot. Site for VNOs: At least one of the following alert notification targets must be specified: email address and webhook URL of the DingTalk chatbot. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | The Request is not authorization. | The returned message. |
| RequestId | String | 181C406E-9DE4- 484C-9C61- 37AE9A1A12EE | The request ID. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutContact &ContactName=Alice &Describe=ECS_Instance &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"181C406E-9DE4-484C-9C61-37AE9A1A12EE",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | InvalidParameterValue | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.24 DescribeMetricPromQLRange

Queries monitoring metric data within a specified time range by using PromQL syntax.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request is successful. Valid values: true (success) and false (failure) |
| Code | String | 200 | The status code. A value of 200 indicates success. |
| Message | String | successful | The response message. The system returns successful when the request succeeds. |
| RequestId | String | 15B664E7-1823- 4C84-A59B- 1A3BXXXX | The request ID. |
| Data | Map | {"result": [{"metric": {" name ":"CPU __ __ Utilization"},"value s": [[1625000000,"80. 5"]]}]} | The query result data. The API returns the data in PromQL format, including metric names and time series values. |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | The parameter is invalid. |
| 403 | 403 | AccessForbidden | You do not have the permissions to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The system failed to process the request due to some unknown errors. |

#### 2.5.25 PutContactGroup

Creates or modifies an alert contact group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ContactGr oupName | Strin g | Query | Yes | ECS Group _ | The name of the alert contact group. For information about how to query the names of alert contact groups, see DescribeContactGroupLi st. |
| Describe | Strin g | Query | Yes | ECS Alert Group _ _ | The description of the alert contact group. |
| ContactNa mes | Repe atList | Query | Yes | Alice | The name of the alert contact. Valid values of N: 1 to 100. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | Illegal parameters. | The returned message. |
| RequestId | String | B4E30DB6-F069- 5D0B-A589- 2A89F7D62A57 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutContactGroup &ContactGroupName=ECS_Group &Describe=ECS_Alert_Group &ContactNames=Alice &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"Illegal parameters.",
 "RequestId":"B4E30DB6-F069-5D0B-A589-2A89F7D62A57",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | InvalidParameterValue | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.26 PutGroupMetricRule

Creates or modifies an alert rule for an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Repe atList | Query | Yes | 1 | The ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The error message. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 461CF2CD-2FC3- 4B26-8645- 7BD27E7D0F1D | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutGroupMetricRule &GroupId=17285**** &RuleId=123456 &Category=ECS &Namespace=acs_ecs_dashboard &MetricName=cpu_total &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"461CF2CD-2FC3-4B26-8645-7BD27E7D0F1D",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |

|   | Developer Gu | ide·API Reference |   | CloudMonito | r |
|---|---|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 409 | 4092 | ResourceExist | Resources already exist. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.27 CreateMetricRuleResources

Associates resources with an alert rule.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| RuleId | Strin g | Query | No | i- 2ze3w55tr2rcpejpcfap 5 _ 9c96b85-0339-4f35- ba66-ae4e34d3**** | The ID of the alert rule. |
| Overwrite | Strin g | Query | No | false | Specifies whether to overwrite existing data. Valid values: true: The resources submitted this time overwrite the previously associated resources. false: The resources submitted this time do not overwrite the previously associated resources. The associated resources after submission include the previously associated resources and the resources submitted this time. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Resources | Strin g | Query | Yes | [{"instanceId":"i- a2d5q7pm3f9yr29e****" }] | The resources that are associated with the alert rule. Set the value to a JSON array. You can add up to 100 resources each time. An alert rule can be associated with up to 3,000 resources. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |
| RequestId | String | 0671A721-0D7A- 4F11-BB77- 2416325D65AB | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateMetricRuleResources &Resources=[{"instanceId":"i-a2d5q7pm3f9yr29e****"}] &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"0671A721-0D7A-4F11-BB77-2416325D65AB",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.28 DescribeContactGroupList

Queries alert contact groups.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | Quer y | Yes |   | The action. |
| PageSize | Integ er | Quer y | No | 1 | The number of entries per page. |
| PageNumb er | Integ er | Quer y | No | 10 | The page number. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ContactGroups | Normal |   | The alert contact groups. |

| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The returned message. |
| Total | Integer | 22 | The total number of entries returned. |
| RequestId | String | 916EE694-03C2- 47B6-85EE- 5054E3C168D3 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeContactGroupList &Action= &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "ContactGroups":"",
 "Message":"The Request is not authorization.",
 "RequestId":"916EE694-03C2-47B6-85EE-5054E3C168D3",
 "Total":22,
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |

| 403 | 403 | InvalidAuthorization | Permission denied |
|---|---|---|---|
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.29 DeleteMetricRuleTemplate

Deletes an alert template.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TemplateI d | Strin g | Query | Yes | 123**** | The ID of the alert template. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7B63F8CF-D48D- 4608-A402- 04FB5B2B4B6A | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |
| Resource | Struct |   | The template information. |
| -TemplateId | String | 123**** | The template ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMetricRuleTemplate &TemplateId=123**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"7B63F8CF-D48D-4608-A402-04FB5B2B4B6A",
 "Resource":{
  "TemplateId":"123****"
```

`},`

```json
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.30 PutEventRuleTargets

Adds or modifies the recipients to which alert notifications are sent based on an eventtriggered alert rule.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| RuleName | Strin g | Query | Yes | testEventRule | The name of the alert rule. |
| FcParame ters | Repe atList | Query | No |   | The information about the recipients in Function Compute. |
| -Id | Strin g |   | No | 5 | The ID of the recipient that receives alert notifications. Valid values of N: 1 to 5. |
| -Region | Strin g |   | No | cn-hangzhou | The region where Simple Log Service is deployed. Valid values of N: 1 to 5. |
| - ServiceNa me | Strin g |   | No | fc-test | The name of the Function Compute service. Valid values of N: 1 to 5. |
| - FunctionN ame | Strin g |   | No | fc-test | The function name. Valid values of N: 1 to 5. |
| -Arn | Strin g |   | No | acs:log:cn- hangzhou::project/cms- log- mon***/logstore/cxxxx** * | The Alibaba Cloud Resource Name (ARN) of the resource. Valid values of N: 1 to 5. Format: arn:acs:${Service}:${R egion}:${Account}:${R esourceType}/${Resour ceId}. Fields: Service: the code of a cloud service Region: the region ID Account: the ID of an Alibaba Cloud account ResourceType: the resource type ResourceId: the resource ID |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ContactPa rameters | Repe atList | Query | No |   | The information about the alert contact groups that receive alert notifications. |
| -Id | Strin g |   | No | 5 | The ID of the recipient that receives alert notifications. Valid values of N: 1 to 5. |
| - ContactGr oupName | Strin g |   | No | Default alert contact group | The name of the alert contact group. Valid values of N: 1 to 5. |
| -Level | Strin g |   | No | 3 | The alert notification methods. Valid values of N: 1 to 5. Valid values: China site: 2: Alert notifications are sent by using phone calls, text messages, DingTalk, and emails. 3: Alert notifications are sent by using text messages, DingTalk, and emails. 4: Alert notifications are sent by using DingTalk and emails. International site: 4: Alert notifications are sent by using DingTalk and emails. Site for virtual network operators (VNOs): 4: Alert notifications are sent by using DingTalk and emails. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| -Arn | Strin g |   | No | acs:log:cn- hangzhou::project/cms- log- mon***/logstore/cxxxx** * | The ARN of the resource. Valid values of N: 1 to 5. Format: arn:acs:${Service}:${R egion}:${Account}:${R esourceType}/${Resour ceId}. Fields: Service: the code of a cloud service Region: the region ID Account: the ID of an Alibaba Cloud account ResourceType: the resource type ResourceId: the resource ID |
| MnsParam eters | Repe atList | Query | No |   | The information about the recipients in Message Service (MNS). |
| -Id | Strin g |   | No | 5 | The ID of the recipient that receives alert notifications. Valid values of N: 1 to 5. |
| -Region | Strin g |   | No | cn-hangzhou | The region where Simple Log Service is deployed. Valid values of N: 1 to 5. |
| -Queue | Strin g |   | No | queue1 | The queue name. Valid values of N: 1 to 5. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| -Arn | Strin g |   | No | acs:log:cn- hangzhou::project/cms- log- mon***/logstore/cxxxx** * | The ARN of the resource. Valid values of N: 1 to 5. Format: arn:acs:${Service}:${R egion}:${Account}:${R esourceType}/${Resour ceId}. Fields: Service: the code of a cloud service Region: the region ID Account: the ID of an Alibaba Cloud account ResourceType: the resource type ResourceId: the resource ID |
| WebhookP arameters | Repe atList | Query | No |   | The information about the callback URLs that are used to receive alert notifications. |
| -Id | Strin g |   | No | 5 | The ID of the recipient that receives alert notifications. Valid values of N: 1 to 5. |
| -Protocol | Strin g |   | No | http | The protocol name. Valid values of N: 1 to 5. Valid values: http telnet ping |
| -Url | Strin g |   | No | http://www.aliyun.com | The callback URL. Valid values of N: 1 to 5. |
| -Method | Strin g |   | No | GET | The HTTP request method. Valid values of N: 1 to 5. Valid values: GET and POST. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| SlsParame ters | Repe atList | Query | No | value | The information about the recipients in Simple Log Service. |
| -Id | Strin g |   | No | 5 | The ID of the recipient that receives alert notifications. Valid values of N: 1 to 5. |
| -Region | Strin g |   | No | cn-hangzhou | The region where Simple Log Service is deployed. Valid values of N: 1 to 5. |
| -Project | Strin g |   | No | testproject | The name of the Simple Log Service project. Valid values of N: 1 to 5. |
| -LogStore | Strin g |   | No | testlogstore | The name of the Simple Log Service Logstore. Valid values of N: 1 to 5. |
| -Arn | Strin g |   | No | acs:log:cn- hangzhou::project/cms- log- mon***/logstore/cxxxx** * | The ARN of the resource. Valid values of N: 1 to 5. Format: arn:acs:${Service}:${R egion}:${Account}:${R esourceType}/${Resour ceId}. Fields: Service: the code of a cloud service Region: the region ID Account: the ID of an Alibaba Cloud account ResourceType: the resource type ResourceId: the resource ID |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| FailedContactP arameters | Array | value | This parameter is returned if the specified alert contact groups in the request failed to be created or modified. |

| loudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Id | Integer | 2 | The ID of the recipient. |
| - ContactGroup Name | String | Default alert contact group | The name of the alert contact group. |
| -Level | String | 3 | The alert notification methods. Valid values: China site: 2: Alert notifications are sent by using phone calls, text messages, DingTalk, and emails. 3: Alert notifications are sent by using text messages, DingTalk, and emails. 4: Alert notifications are sent by using DingTalk and emails. International site: 4: Alert notifications are sent by using DingTalk and emails. Site for VNOs: 4: Alert notifications are sent by using DingTalk and emails. |
| -Arn | String |   | The ARN of the resource. Valid values of N: 1 to 5. Format: arn:acs:${Service}:${Region}:${Account }:${ResourceType}/${ResourceId}. Fields: Service: the code of a cloud service Region: the region ID Account: the ID of an Alibaba Cloud account ResourceType: the resource type ResourceId: the resource ID |
| FailedMnsPara meters | Array |   | This parameter is returned if the specified queues in the request failed to be created or modified in MNS. |
| -Id | Integer | 2 | The ID of the recipient. |
| -Region | String | cn-hangzhou | The region ID. |
| -Queue | String | testQueue | The queue name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Arn | String |   | The ARN of the resource. Valid values of N: 1 to 5. Format: arn:acs:${Service}:${Region}:${Account }:${ResourceType}/${ResourceId}. Fields: Service: the code of a cloud service Region: the region ID Account: the ID of an Alibaba Cloud account ResourceType: the resource type ResourceId: the resource ID |
| FailedFcParam eters | Array |   | This parameter is returned if the specified functions in the request failed to be created or modified in Function Compute. |
| -Id | Integer | 2 | The ID of the recipient. |
| -Region | String | cn-hangzhou | The region ID. |
| -ServiceName | String | serviceTest1 | The name of the Function Compute service. |
| - FunctionName | String | functionTest1 | The function name. |
| -Arn | String |   | The ARN of the resource. Valid values of N: 1 to 5. Format: arn:acs:${Service}:${Region}:${Account }:${ResourceType}/${ResourceId}. Fields: Service: the code of a cloud service Region: the region ID Account: the ID of an Alibaba Cloud account ResourceType: the resource type ResourceId: the resource ID |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The returned message. |
| RequestId | String | 409C64DA-CF14- 45DF-B463- 471C790DD15A | The request ID. |
| FailedParamet erCount | String | 2 | The number of resources that failed to be created or modified. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutEventRuleTargets &RuleName=testEventRule &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"409C64DA-CF14-45DF-B463-471C790DD15A",
 "FailedMnsParameters":{
  "Region":"cn-hangzhou",
  "Id":2,
  "Arn":"acs:log:cn-hangzhou::project/cms-log-mon***/logstore/cxxxx***",
  "Queue":"testQueue"
```

`},`

```json
 "FailedFcParameters":{
  "FunctionName":"functionTest1",
  "ServiceName":"serviceTest1",
  "Region":"cn-hangzhou",
  "Id":1,
  "Arn":"acs:log:cn-hangzhou::project/cms-log-mon***/logstore/cxxxx***"
```

`},`

```json
 "FailedParameterCount":"2",
 "FailedContactParameters":{
  "ContactGroupName":"Default alert contact group",
  "Level":"3",
  "Id":2,
  "Arn":""
```

`},`

```json
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.31 CreateMetricRuleTemplate

Creates an alert template.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Quer y | Yes | Template1 | The name of the alert template. |
| Descriptio n | Strin g | Quer y | No | ECS Template1 _ | The description of the alert template. |
| AlertTempl ates | Repe atLis t | Quer y | No |   | The alert templates. |
| - MetricNam e | Strin g |   | Yes | cpu total _ | The metric name. Valid values of N: 1 to 200. For information about how to query metrics, see DescribeMetricMetaList or Appendix 1: Metrics. |
| -RuleName | Strin g |   | Yes | ECS Rule1 _ | The name of the alert rule. Valid values of N: 1 to 200. |
| -Category | Strin g |   | Yes | ecs | The abbreviation of the cloud service name. Valid values of N: 1 to 200. For information about how to query the abbreviations of cloud service names, see metricCategory in the response parameter Labels of the DescribeProjectMeta operation. |

| - Namespac e | Strin g |   | Yes | acs ecs dashboard _ _ | The namespace of the cloud service. Valid values of N: 1 to 200. For information about how to query the namespaces of cloud services, see DescribeMetricMetaList or Appendix 1: Metrics. |
|---|---|---|---|---|---|
| -Period | Integ er |   | No | 60 | The aggregation period of monitoring data. Unit: seconds. The default value is the minimum aggregation period. Generally, you do not need to specify the minimum aggregation period. Valid values of N: 1 to 200. |
| -Selector | Strin g |   | No | {"disk":"/"} | The dimension of the alert. It is an extended field. Valid values of N: 1 to 200. For example, an alert template is applied to an application group, this parameter is set to {"disk":"/"} , and the MetricName parameter is set to DiskUtilization . In this case, the generated alert rule is applied to the root disk partition ( "/" ) of all instances in the application group to which the alert template is applied. For more information about the values of extended fields, see DescribeMetricRuleT emplateAttribute. |

| - Escalation s.Critical.S tatistics | Strin g |   | No | Average | The statistical method for Critical-level alerts. Valid values of N: 1 to 200. The value of this parameter is determined by the Statistics column corresponding to the MetricName parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see Appendix 1: Metrics. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
|---|---|---|---|---|---|
|   |   |   |   |   | The operator that is used to compare the metric value with the threshold for Critical-level alerts. Valid values: GreaterThanOrEqualTo Threshold: greater than or equal to the threshold GreaterThanThreshold: greater than the threshold LessThanOrEqualToThr eshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterday: greater than the metric value at the same time yesterday |

| - Escalation s.Critical.C omparison Operator | Strin g |   | No | GreaterThanOrEqualToTh reshold | LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric |
|---|---|---|---|---|---|
|   |   |   |   |   | value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
| - Escalation s.Critical.T hreshold | Strin g |   | No | 30 | The threshold for Critical- level alerts. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |

| - Escalation s.Critical.Ti mes | Integ er |   | No | 3 | The consecutive number of times for which the metric value meets the alert condition before a Critical-level alert is triggered. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
|---|---|---|---|---|---|
| - Escalation s.Critical.R ange | Integ er |   | No | 1 | The scope of Critical-level alerts. |

| - Escalation s.Warn.Sta tistics | Strin g |   | No | Average | The statistical method for Warn-level alerts. Valid values of N: 1 to 200. The value of this parameter is determined by the Statistics column corresponding to the MetricName parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see Appendix 1: Metrics. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
|---|---|---|---|---|---|
|   |   |   |   |   | The operator that is used to compare the metric value with the threshold for Warn-level alerts. Valid values: GreaterThanOrEqualTo Threshold: greater than or equal to the threshold GreaterThanThreshold: greater than the threshold LessThanOrEqualToThr eshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterday: greater than the metric value at the same time yesterday |

| - Escalation s.Warn.Co mparisonO perator | Strin g |   | No | GreaterThanOrEqualToTh reshold | LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric |
|---|---|---|---|---|---|
|   |   |   |   |   | value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
| - Escalation s.Warn.Thr eshold | Strin g |   | No | 30 | The threshold for Warn- level alerts. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |

| - Escalation s.Warn.Ti mes | Integ er |   | No | 1 | The consecutive number of times for which the metric value meets the alert condition before a Warn-level alert is triggered. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
|---|---|---|---|---|---|
| - Escalation s.Warn.Ra nge | Integ er |   | No | 1 | The scope of the Warn- level alerts. |
| - Escalation s.Info.Stati stics | Strin g |   | No | Average | The statistical method for Info-level alerts. Valid values of N: 1 to 200. The value of this parameter is determined by the Statistics column corresponding to the MetricName parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see Appendix 1: Metrics. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |

| - Escalation s.Info.Com parisonOp erator | Strin g |   | No | GreaterThanOrEqualToTh reshold | The operator that is used to compare the metric value with the threshold for Info-level alerts. Valid values: GreaterThanOrEqualTo Threshold: greater than or equal to the threshold GreaterThanThreshold: greater than the threshold LessThanOrEqualToThr eshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
|---|---|---|---|---|---|

| - Escalation s.Info.Thre shold | Strin g |   | No | 20 | The threshold for Info- level alerts. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
|---|---|---|---|---|---|
| - Escalation s.Info.Time s | Integ er |   | No | 1 | The consecutive number of times for which the metric value meets the alert condition before an Info-level alert is triggered. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
| - Escalation s.Info.Ran ge | Integ er |   | No | 1 | The scope of the Info- level alerts. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9763ED1A-4D09- 41BF-851E- 310421750204 | The request ID. |

| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
|---|---|---|---|
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The returned message. |
| Id | Long | 12345 | The ID of the alert template. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateMetricRuleTemplate &Name=Template1 &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"9763ED1A-4D09-41BF-851E-310421750204",
 "Id":12345,
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |

| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
|---|---|---|---|
| 403 | 403 | InvalidClientTokenId | The X.509 certificate or cms access key ID provided does not exist in our records. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.32 CreateGroupMetricRules

Creates one or more alert rules for a specified application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupId | Long | Query | Yes | 3607**** | The ID of the application group. For information about how to query the IDs of application groups, see DescribeMonitorGroups. |
| GroupMet ricRules | Repe atList | Query | No |   | The metric rules for the application group. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| -Category | Strin g |   | Yes | ECS | The abbreviation of the cloud service name. Valid values of N: 1 to 200. For information about how to query the abbreviations of cloud service names, see metricCategory in the response parameter Labels of the DescribeProjectMeta operation. |
| - RuleName | Strin g |   | Yes | ECS Rule1 _ | The name of the alert rule. Valid values of N: 1 to 200. |
| -RuleId | Strin g | Query | Yes | 456789 | The ID of the alert rule. Valid values of N: 1 to 200. |
| - Namespac e | Strin g |   | Yes | acs ecs dashboard _ _ | The namespace of the cloud service. Valid values of N: 1 to 200. For information about how to query the namespaces of cloud services, see DescribeMetricMetaList or Appendix 1: Metrics. |
| - MetricNa me | Strin g |   | Yes | cpu total _ | The metric name. Valid values of N: 1 to 200. For information about how to query metric names, see DescribeMetricMetaList or Appendix 1: Metrics. |

| Parame ter | Typ e | Locati on | Require d |   | Example |   |   | Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| - Dimension s | Strin g |   | No |   | [{"instanceId":"i- m5e1qg6uo38rztr4****" }] |   |   | The dimension of the alert rule. Set the value to a set of key-value pairs, for example, userId:120886317861* *** or instanceId:i- m5e1qg6uo38rztr4**** . |   |   |   |
|   |   |   |   |   |   |   |   |   | userId:120886317861* |   |   |
|   |   |   |   |   |   | e1qg6uo38rztr4****" |   | *** |   |   |   |
|   |   |   |   |   |   |   |   |   |   | or |   |
|   |   |   |   |   |   |   |   | m5e1qg6uo38rztr4**** |   |   |   |
| - EffectiveIn terval | Strin g |   | No |   | 05:31-23:59 |   |   | The period of time during which the alert rule is effective. Valid values of N: 1 to 200. |   |   |   |
| - NoEffectiv eInterval | Strin g |   | No |   | 00:00-05:30 |   |   | The period of time during which the alert rule is ineffective. Valid values of N: 1 to 200. |   |   |   |
| - SilenceTi me | Integ er |   | No |   | 86400 |   |   | The mute period during which new alerts are not sent even if the trigger conditions are met. Valid values of N: 1 to 200. Unit: seconds. Default value: 86400. Minimum value: 3600. |   |   |   |
| -Period | Strin g |   | No |   | 60 |   |   | The aggregation period of the metric data. Valid values of N: 1 to 200. Set the Period parameter to an integral multiple of 60. Unit: seconds. Default value: 300. |   |   |   |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| -Interval | Strin g |   | No | 60 | The interval at which CloudMonitor checks whether the alert rule is triggered. Valid values of N: 1 to 200. Unit: seconds. The default value is the lowest frequency at which the metric is polled. We recommend that you set the interval to the data aggregation period. If the interval is shorter than the data aggregation period, alerts cannot be triggered due to insufficient data. |
| -Webhook | Strin g |   | No | https://www.aliyun.com | The callback URL. Valid values of N: 1 to 200. The callback URL must be accessible over the Internet. CloudMonitor pushes an alert notification to the specified callback URL by sending an HTTP POST request. Only the HTTP protocol is supported. |
| - EmailSubj ect | Strin g |   | No | ECS instance | The subject of the alert notification email. Valid values of N: 1 to 200. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Escalation s.Critical.S tatistics | Strin g | Query | No | Average | The statistical method for Critical-level alerts. Valid values of N: 1 to 200. The value of this parameter is determined by the Statistics column corresponding to the MetricName parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see Appendix 1: Metrics. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |
|   |   |   |   |   | The operator that is used to compare the metric value with the threshold for Critical- level alerts. Valid values: GreaterThanOrEqualT oThreshold: greater than or equal to the threshold GreaterThanThreshol d: greater than the threshold LessThanOrEqualToTh reshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the |

| Parame ter | Typ e | Locati on | Require d | Example | threshold DeGsrecartieprtTihoannYesterda y: greater than the |
|---|---|---|---|---|---|
| - |   |   |   |   | metric value at the same time yesterday LessThanYesterday: less than the metric value at the same |
| Escalation s.Critical. Comparis onOperato r | Strin g | Query | No | GreaterThanOrEqualToT hreshold | time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPerio d: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Escalation s.Critical.T hreshold | Strin g | Query | No | 90 | The threshold for Critical-level alerts. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |
| - Escalation s.Critical.T imes | Integ er | Query | No | 3 | The consecutive number of times for which the metric value meets the alert condition before a Critical-level alert is triggered. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Escalation s.Warn.St atistics | Strin g | Query | No | Average | The statistical method for Warn-level alerts. Valid values of N: 1 to 200. The value of this parameter is determined by the Statistics column corresponding to the MetricName parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see Appendix 1: Metrics. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |
|   |   |   |   |   | The operator that is used to compare the metric value with the threshold for Warn-level alerts. Valid values: GreaterThanOrEqualT oThreshold: greater than or equal to the threshold GreaterThanThreshol d: greater than the threshold LessThanOrEqualToTh reshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterda y: greater than the |

| Parame ter | Typ e | Locati on | Require d | Example | metric value at the Dessamcrei ptitmioe nyesterday LessThanYesterday: |
|---|---|---|---|---|---|
| - Escalation s.Warn.Co mparison Operator | Strin g | Query | No | GreaterThanOrEqualToT hreshold | less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week |
|   |   |   |   |   | LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPerio d: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |
| - Escalation s.Warn.Th reshold | Strin g | Query | No | 20 | The threshold for Warn- level alerts. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Escalation s.Warn.Ti mes | Integ er | Query | No | 3 | The consecutive number of times for which the metric value meets the alert condition before a Warn-level alert is triggered. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |
| - Escalation s.Info.Stati stics | Strin g | Query | No | Average | The statistical method for Info-level alerts. Valid values of N: 1 to 200. The value of this parameter is determined by the Statistics column corresponding to the MetricName parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see Appendix 1: Metrics. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |

| Parame ter | Typ e | Locati on | Require d | Example | The operator that is uDseesd ctroi pcotmiopnare the metric value with the |
|---|---|---|---|---|---|
| - Escalation s.Info.Co mparison Operator | Strin g | Query | No | GreaterThanOrEqualToT hreshold | threshold for Info-level alerts. Valid values: GreaterThanOrEqualT oThreshold: greater than or equal to the threshold GreaterThanThreshol d: greater than the threshold LessThanOrEqualToTh reshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterda y: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPerio d: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Escalation s.Info.Thre shold | Strin g | Query | No | 10 | The threshold for Info- level alerts. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |
| - Escalation s.Info.Tim es | Integ er | Query | No | 1 | The consecutive number of times for which the metric value meets the alert condition before an Info-level alert is triggered. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | The Request is not authorization. | The error message. |
| RequestId | String | 461CF2CD-2FC3- 4B26-8645- 7BD27E7D0F1D | The request ID. |
| Resources | Array |   | The alert rules. |
| -RuleId | String | 456789 | The ID of the alert rule. |

| CloudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -RuleName | String | ECS Rule1 _ | The name of the alert rule. |
| -Message | String | Metric not found. | The error message that is returned for the alert rule. |
| -Code | Integer | 200 | The status code that is returned for the alert rule. The status code 200 indicates that the alert rule is created. |
| -Success | Boolean | true | Indicates whether the alert rule is created. Valid values: true false |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateGroupMetricRules &GroupId=3607**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"461CF2CD-2FC3-4B26-8645-7BD27E7D0F1D",
 "Resources":{
  "Message":"Metric not found.",
  "RuleId":"456789",
  "Code":200,
  "RuleName":"ECS_Rule1",
  "Success":true
```

`},`

```json
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 412 | 4121 | ResourcesOverLimit | Resources over limit. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.33 DeleteEventRules

Deletes event-triggered alert rules.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| RuleName s | Repe atList | Query | Yes | rule1 | The name of the alert rule. Valid values of N: 1 to 20. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |
| RequestId | String | E5A72B5B-4F44- 438C-B68A- 147FD5DC53A8 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteEventRules &RuleNames=rule1 &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"E5A72B5B-4F44-438C-B68A-147FD5DC53A8",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | InvalidParameterValue | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.34 ModifyMetricRuleTemplate

Modifies an alert template.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TemplateI d | Long | Query | Yes | 123456 | The ID of the alert template. For more information about how to query the IDs of alert templates, see DescribeMetricRuleTem plateList. |
| Name | Strin g | Query | No | Template 123 _ | The name of the alert template. For more information about how to query the names of alert templates, see DescribeMetricRuleTem plateList. |
| Descriptio n | Strin g | Query | No | ECS template1 _ | The description of the alert template. |
| RestVersi on | Long | Query | Yes | 1 | The version of the alert template. The version changes with the number of times that the alert template is modified. For more information about how to query the versions of alert templates, see DescribeMetricRuleTem plateList. |
| AlertTemp lates | Repe atList | Query | No |   | The alert templates. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| - MetricNa me | Strin g |   | No | cpu total _ | The metric name. Valid values of N: 1 to 200. For information about how to query metrics, see DescribeMetricMetaList or Appendix 1: Metrics. |
| - RuleName | Strin g |   | No | Rule 123 _ | The name of the alert rule. Valid values of N: 1 to 200. |
| -Category | Strin g |   | No | ecs | The abbreviation of the cloud service name. Valid values of N: 1 to 200. For more information about how to query the abbreviations of cloud service names, see metricCategory in the response parameter Labels of the DescribeProjectMeta operation. |
| - Namespac e | Strin g |   | No | acs ecs dashboard _ _ | The namespace of the cloud service. Valid values of N: 1 to 200. For more information about how to query the namespaces of cloud services, see DescribeMetricMetaList or Appendix 1: Metrics. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| -Period | Integ er |   | No | 60 | The statistical period of the monitoring data. Valid values of N: 1 to 200. If the value is set to 300 seconds, the monitoring data is collected every 300 seconds. If the monitoring data is reported every 1 minute, the alert system calculates the average, maximum, and minimum values of the monitoring data of 5 minutes and checks whether the aggregated values exceed the threshold. To prevent unexpected alerts, we recommend that you set this parameter together with other parameters. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| -Selector | Strin g |   | No | {"disk":"/"} | The dimension of the alert. It is an extended field. Valid values of N: 1 to 200. For example, an alert template is applied to an application group, this parameter is set to {"disk":"/"} , and the MetricName parameter is set to DiskUtilization . In this case, the generated alert rule is applied to the root disk partition ( "/" ) of all instances in the application group to which the alert template is applied. For more information about the values of extended fields, see DescribeMetricRule TemplateAttribute. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Escalation s.Critical.S tatistics | Strin g |   | No | Average | The statistical method for Critical-level alerts. Valid values of N: 1 to 200. The value of this parameter is determined by the Statistics column corresponding to the MetricName parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see Appendix 1: Metrics. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |
|   |   |   |   |   | The operator that is used to compare the metric value with the threshold for Critical- level alerts. Valid values: GreaterThanOrEqualT oThreshold: greater than or equal to the threshold GreaterThanThreshol d: greater than the threshold LessThanOrEqualToTh reshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterda |

| Parame ter | Typ e | Locati on | Require d | Example | y: greater than the Demsectrriicp vtaiolune at the same time yesterday |
|---|---|---|---|---|---|
| - Escalation s.Critical. Comparis onOperato r | Strin g |   | No | GreaterThanOrEqualToT hreshold | LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week |
|   |   |   |   |   | LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPerio d: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |
| - Escalation s.Critical.T hreshold | Strin g |   | No | 30 | The threshold for Critical-level alerts. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Escalation s.Critical.T imes | Integ er |   | No | 2 | The consecutive number of times for which the metric value meets the alert condition before a Critical-level alert is triggered. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |
| - Escalation s.Critical. Range | Integ er |   | No | value | The scope of Critical- level alerts. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Escalation s.Warn.St atistics | Strin g |   | No | Average | The statistical method for Warn-level alerts. Valid values of N: 1 to 200. The value of this parameter is determined by the Statistics column corresponding to the MetricName parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see Appendix 1: Metrics. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Escalation s.Warn.Co mparison Operator | Strin g |   | No | GreaterThanOrEqualToT hreshold | The operator that is used to compare the metric value with the threshold for Warn-level alerts. Valid values: GreaterThanOrEqualT oThreshold: greater than or equal to the threshold GreaterThanThreshol d: greater than the threshold LessThanOrEqualToTh reshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterda y: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPerio d: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle Valid values of N: 1 to 200. |
| 79 |   |   |   | > Do | cument Version: 2026090 |

| Parame ter | Typ e | Locati on | Require d | Example |   | You must select at Delesacsrti ponteio onf the Critical, Warn, and |
|---|---|---|---|---|---|---|
| - Escalation s.Warn.Th reshold | Strin g |   | No | 30 | Info alert levels and Thes ptehcreifsyh tohled for Warn- levSetl aatliestritcss., ComparisonOperat Valoidr, vTahlrueessh oofld N, :a 1n dto 200T.imes parameters for the selected You must select at alert level. least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |   |
| - Escalation s.Warn.Ti mes | Integ er |   | No | 1 | The consecutive number of times for which the metric value meets the alert condition before a Warn-level alert is triggered. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |   |
| - |   |   |   |   |   |   |
| Escalation s.Warn.Ra nge | Integ er |   | No | value | The scope of the Warn- level alerts. |   |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Escalation s.Info.Stati stics | Strin g |   | No | Average | The statistical method for Info-level alerts. Valid values of N: 1 to 200. The value of this parameter is determined by the Statistics column corresponding to the MetricName parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see Appendix 1: Metrics. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Escalation s.Info.Co mparison Operator | Strin g |   | No | GreaterThanOrEqualToT hreshold | The operator that is used to compare the metric value with the threshold for Info-level alerts. Valid values: GreaterThanOrEqualT oThreshold: greater than or equal to the threshold GreaterThanThreshol d: greater than the threshold LessThanOrEqualToTh reshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterda y: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPerio d: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle Valid values of N: 1 to 200. |
| > Document V | ersion: 2 | 0260902 |   |   | 28 |

| Parame ter | Typ e | Locati on | Require d | Example |   | You must select at Delesacsrti ponteio onf the Critical, Warn, and |
|---|---|---|---|---|---|---|
| - Escalation s.Info.Thre shold | Strin g |   | No | 20 | Info alert levels and specify the The threshold for Info- Statistics, level alerts. ComparisonOperat Valoidr, vTahlrueessh ofld N, :a 1n dto 200T.imes parameters for the selected You must select at alert level. least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |   |
| - Escalation s.Info.Tim es | Integ er |   | No | 1 | The consecutive number of times for which the metric value meets the alert condition before an Info-level alert is triggered. Valid values of N: 1 to 200. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperat or, Threshold, and Times parameters for the selected alert level. |   |
| - |   |   |   |   |   |   |
| Escalation s.Info.Ran ge | Integ er |   | No | value | The scope of Info-level alerts. |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9E07117F-F6AE- 4F1C-81E8- 36FBB4892235 | The request ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyMetricRuleTemplate &TemplateId=123456 &RestVersion=1 &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"9E07117F-F6AE-4F1C-81E8-36FBB4892235",
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | InvalidClientTokenId | The X.509 certificate or cms access key ID provided does not exist in our records. |

| Developer Gui | de·API Reference |   | CloudMonito |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.35 PutMetricRuleTargets

Associates resources with a specified alert rule or modifies the resources that are associated with the alert rule.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| RuleId | Strin g | Query | Yes | ae06917 75a8c43178ab _ 66**** | The ID of the alert rule. For more information about how to query the IDs of alert rules, see DescribeMetricRuleList. |
| Targets | Repe atList | Query | Yes |   | The targets. |
| -Id | Strin g |   | No | 1 | The ID of the resource for which alerts are triggered. For more information about how to query the IDs of the resources for which alerts are triggered, see DescribeMetricRuleTarg ets. |

|   | Parame ter |   | Typ e |   | Locati on |   | Require d |   |   | Example |   |   | Description |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   | The Alibaba Cloud Resource Name (ARN) of the resource. For more information about how to query the ARNs of resources, see DescribeMetricRuleTarg ets. Format: acs:{Service |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | acs:{Service |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | name abbreviation}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | {regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | {userId}:/{Resource |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | type}/{Resource |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | name}/message |   |   | . |   |
|   | -Arn |   | Strin g |   |   |   |   |   |   |   |   |   | Example: |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | hangzhou:120886317861 |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | ****:/queues/test123/ |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | message |   |   |   |   |
|   |   |   |   |   |   |   | No |   |   | acs:mns:cn- hangzhou:12088631786 1****:/queues/test/mess age |   |   |   |   |   |   |   |

| Parame ter | Typ e | Locati on | Require d | Example | Description The alert level. Valid values: |
|---|---|---|---|---|---|
| -Level | Strin g |   | Yes | ["INFO", "WARN", "CRITICAL"] | INFO WARN CRITICAL |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The request processing has failed due to some unknown error. | The returned message. |
| RequestId | String | 6A569B0D-9055- 58AF-9E82- BAEAF95C0FD5 | The request ID. |
| FailData | Struct |   | The failed data. |
| -Targets | Array |   | The information about the resources for which alerts are triggered. |
| --Id | String | 1 | The ID of the resource for which alerts are triggered. For more information about how to query the IDs of the resources for which alerts are triggered, see DescribeMetricRuleTargets. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| --Arn | String | acs:mns:cn- hangzhou:1208863 17861****:/queues /test/message | The ARN of the resource. For more information about how to query the ARNs of resources, see DescribeMetricRuleTargets. Format: acs:{Service name abbreviation}: {regionId}:{userId}:/{Resource type}/{Resource name}/message. Example: acs:mns:cn- hangzhou:120886317861****:/queues/test 123/message. Fields: {Service name abbreviation}: the abbreviation of the service name. Valid value: mns. {userId}: the ID of the Alibaba Cloud account. {regionId}: the region ID of the message queue or topic. {Resource type}: the type of the resource that triggers the alert. Valid values: queues topics {Resource name}: the resource name. If the resource type is queues, the resource name is the queue name. If the resource type is topics, the resource name is the topic name. |
| --Level | String | ["INFO", "WARN", "CRITICAL"] | The alert level. Valid values: INFO WARN CRITICAL |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutMetricRuleTargets &RuleId=ae06917_75a8c43178ab66**** &Targets=null &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The request processing has failed due to some unknown error.",
 "RequestId":"6A569B0D-9055-58AF-9E82-BAEAF95C0FD5",
 "FailData":{
  "-Targets":{
   "Level":"[\"INFO\", \"WARN\", \"CRITICAL\"]",
   "Id":"1",
   "Arn":"acs:mns:cn-hangzhou:120886317861****:/queues/test/message"
```

`}` `},`

```json
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.5.36 DescribeDynamicThresholdBound

Queries the boundary values of the intelligent threshold (dynamic threshold) for a metric.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Datapoints | List | [{"timestamp":162 5000000000,"lowe rBound":10.5,"upp erBound":90.5}] | The list of intelligent threshold boundary data in JSON format, which includes timestamps, upper bounds, and lower bounds. |
|---|---|---|---|
| Code | String | 200 | The status code. A value of 200 indicates success. |
| Msg | String | successful | The response message. |
| Success | Boolean | true | Indicates whether the request succeeded. Valid values: true (success) and false (failure) |
| RequestId | String | 15B664E7-1823- 4C84-A59B- 1A3BXXXX | The request ID. |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | InvalidParameter | The parameter is invalid. |
| 403 | 403 | InvalidAuthorization | The request is not authorized. |
| 500 |   | InternalError | The system failed to process the request due to some unknown errors. |

### 2.6 Event monitoring

#### 2.6.1 DescribeSystemEventHistogram

Queries the number of times a system event occurred during each interval within a period of time.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| Product | Strin g | Quer y | No | OSS | The abbreviation of the service name. For more information about how to query the abbreviations of cloud service names, see DescribeSystemEven tMetaList. |
| EventType | Strin g | Quer y | No | Exception | The event type. For more information about how to query the types of system events, see DescribeSystemEven tMetaList. |
| Name | Strin g | Quer y | No | BucketIngressBandwidth | The event name. For more information about how to query the names of system events, see DescribeSystemEven tMetaList. |
| Level | Strin g | Quer y | No | CRITICAL | The level of the event. Valid values: CRITICAL WARN INFO |
| Status | Strin g | Quer y | No | normal | The event status. For more information about how to query the status of system events, see DescribeSystemEven tMetaList. |
| GroupId | Strin g | Quer y | No | 12345 | The ID of the application group. |

| SearchKey words | Strin g | Quer y | No | cms | The keywords that are used to search for the event. Valid values: If you want to search for the system event whose content contains a and b, set the value to a and b . If you want to search for the system event whose content contains a or b, set the value to a or b . |
|---|---|---|---|---|---|
| StartTime | Strin g | Quer y | No | 1552209685596 | The start time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| EndTime | Strin g | Quer y | No | 1552220485596 | The end time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Valid values: 1 to 1000000000. Default value: 1. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Valid values: 1 to 1000000000. Default value: 10. |

|   | b |
|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| SystemEventH istograms | Array |   | The information about the number of times the system event occurred during each interval of a time period. |

| -Count | Long | 2 | The number of times the system event occurred. |
|---|---|---|---|
| -StartTime | Long | 1552225770000 | The start time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -EndTime | Long | 1552225753000 | The end time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The returned message. |
| RequestId | String | 486029C9-53E1- 44B4-85A8- 16A571A043FD | The request ID. |
| Success | String | true | Indicates whether the request was successful. Valid values: true and false. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSystemEventHistogram &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "SystemEventHistograms":{
  "EndTime":1552225753000,
  "StartTime":1552225770000,
  "Count":2
```

`},`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"486029C9-53E1-44B4-85A8-16A571A043FD",
 "Code":"200",
 "Success":"true"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.6.2 DescribeSystemEventAttribute

Queries the details of a system event.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Product | Strin g | Query | No | oss | The abbreviation of the Alibaba Cloud service name. For information about how to obtain the abbreviations of Alibaba Cloud service names, see DescribeSystemEve ntMetaList. |
| EventType | Strin g | Query | No | Exception | The type of the system event. For information about how to obtain the types of system events, see DescribeSystemEve ntMetaList. |
| Name | Strin g | Query | No | BucketIngressBandwidth | The name of the system event. For information about how to obtain the names of system events, see DescribeSystemEve ntMetaList. |
| Level | Strin g | Query | No | CRITICAL | The level of the system event. Valid values: CRITICAL WARN INFO |
| Status | Strin g | Query | No | normal | The status of the system event. For information about how to obtain the status of system events, see DescribeSystemEve ntMetaList. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupId | Strin g | Query | No | 12346 | The ID of the application group. |
| SearchKey words | Strin g | Query | No | cms | The keywords that are used to search for the system event. Valid values: If you want to search for the system event whose content contains a and b, set the value to a and b . If you want to search for the system event whose content contains a or b, set the value to a or b . |
| StartTime | Strin g | Query | No | 1552199984949 | The start time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| EndTime | Strin g | Query | No | 1552221584949 | The end time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| PageNum ber | Integ er | Query | No | 1 | The page number. Valid values: 1 to 100000000. Default value: 1. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. Valid values: 1 to 100. Default value: 10. |

|   | b |
|---|---|

|   | b |
|---|---|

| Developer Gui | de·API R | eference |   |   | CloudMonito |
|---|---|---|---|---|---|
| Parame ter | Typ e | Locati on | Require d | Example | Description |
| Reverse | Boole an | Query | No |   | To reverse. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| SystemEvents | Array |   | The details of the system events. |
| -Content | String | [{"product":"Cloud Monitor","content": " {\"ipGroup\":\"112. 126.XX.XX,10.163. XX.XX\",\"tianjimon Version\":\"1.2.22\" }","groupId":"176,1 77,178,179,180,69 2,120812,1663836 ,96,2028302","time ":"1552209568000 ","resourceId":"acs: ecs:cn- beijing:173651113 438****:instance/i- 25k35****","level": "CRITICAL","status" :"stopped","instanc eName":"cmssitepr obebj- 6","name":"Agent _ Status Stopped","r _ egionId":"cn- beijing"}] | The details of the system event. |
| -Product | String | CloudMonitor | The abbreviation of the Alibaba Cloud service name. |
| -Name | String | Agent Status Stop _ _ ped | The name of the system event. |
| -GroupId | String | 12345 | The ID of the application group. |
| -Num | Long |   |   |
| -Level | String | WARN | The level of the system event. Valid values: CRITICAL WARN INFO |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Status | String | normal | The status of the system event. |
| -ResourceId | String | xxxxx-1 | The resource ID. |
| -RegionId | String | cn-hangzhou | The region ID. |
| - InstanceName | String | instanceId1 | The instance name. |
| -Time | Long | 1552199984000 | The time when the event occurred. The value is a timestamp. Unit: milliseconds. |
| Message | String | success | The returned message. If the request was successful, the value success is returned. If the request failed, an error message is returned. |
| RequestId | String | 60912C8D-B340- 4253-ADE7- 61ACDFD25CFC | The request ID. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Success | String | true | Indicates whether the request was successful. Valid values: true and false. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSystemEventAttribute &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "SystemEvents":{
  "Status":"normal",
  "InstanceName":"instanceId1",
  "ResourceId":"xxxxx-1",
  "Content":"[{\"product\":\"CloudMonitor\",\"content\":\"
{\\\"ipGroup\\\":\\\"112.126.XX.XX,10.163.XX.XX\\\",\\\"tianjimonVersion\\\":\\\"1.2.22\\ }\",\"groupId\":\"176,177,178,179,180,692,120812,1663836,96,2028302\",\"time\":\"15522095 000\",\"resourceId\":\"acs:ecs:cn-beijing:173651113438****:instance/i- 25k35****\",\"level\":\"CRITICAL\",\"status\":\"stopped\",\"instanceName\":\"cmssiteprobe -6\",\"name\":\"Agent_Status_Stopped\",\"regionId\":\"cn-beijing\"}]",
  "Num":"",
  "Product":"CloudMonitor",
  "Level":"WARN",
  "Time":1552199984000,
  "RegionId":"cn-hangzhou",
  "Name":"Agent_Status_Stopped",
  "GroupId":"12345"
```

`},`

```json
 "Message":"success",
 "RequestId":"60912C8D-B340-4253-ADE7-61ACDFD25CFC",
 "Code":"200",
 "Success":"true"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.6.3 DescribeSystemEventCount

Queries the number of times a system event of a cloud service has occurred.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Product | Strin g | Query | No | ECS | The name of the cloud service in which the system event occurred. You can call the DescribeSystemEventMe taList operation to obtain the value of the response parameter Product . The value of the Level parameter indicates the levels of system events that occurred for all cloud services in your Alibaba Cloud account. For more information, see DescribeSystemEventMe taList. |
| EventType | Strin g | Query | No | StatusNotification | The event type. You can call the DescribeSystemEventMe taList operation to obtain the value of the response parameter EventType . The value of the EventType parameter indicates the types of system events that occurred for all cloud services in your Alibaba Cloud account. For more information, see DescribeSystemEventMe taList. |
| Name | Strin g | Query | No | Instance:StateChange | The event name. You can call the DescribeSystemEventMe taList operation to obtain the value of the response parameter Name . The value of the Name parameter indicates the names of system events that occurred for all cloud services in your Alibaba Cloud account. For more information, see DescribeSystemEventMe taList. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Level | Strin g | Query | No | Info | The level of the event. Valid values: Critical Warn Info You can call the DescribeSystemEventMe taList operation to obtain the value of the response parameter Level . The value of the Level parameter indicates the levels of system events that occurred for all cloud services in your Alibaba Cloud account. For more information, see DescribeSystemEventMe taList. |
| Status | Strin g | Query | No | Normal | The event status. You can call the DescribeSystemEventMe taList operation to obtain the value of the response parameter Status . The value of the Status parameter indicates the status of system events that occurred for all cloud services in your Alibaba Cloud account. For more information, see DescribeSystemEventMe taList. |
| GroupId | Strin g | Query | No | 17285**** | The ID of the application group. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| SearchKey words | Strin g | Query | No | ECS | The keywords that are used to search for the system event. Valid values: If you want to search for the system event whose content contains a and b, set the value to a and b . If you want to search for the system event whose content contains a or b, set the value to a or b . |
| StartTime | Strin g | Query | No | 1635993541000 | The start of the time range to query. Unit: milliseconds. |
| EndTime | Strin g | Query | No | 1635993921000 | The end of the time range to query. Unit: milliseconds. |

|   | b |
|---|---|

|   | b |
|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| SystemEventC ounts | Array |   | The event details. |
| -Content | String | Notification of instance status change | The event description. |
| -Product | String | ECS | The name of the cloud service in which the system event occurred. |
| -Name | String | Instance:StateChan ge | The event name. |
| -GroupId | String | 17285**** | The ID of the application group. |
| -Num | Long | 3 | The number of times the event has occurred. |

| Developer Guide·A | PI Reference |   | CloudMonito |
|---|---|---|---|
| Parameter | Type | Example | Description |

| -Level | String | Info | The level of the event. Valid values: Critical Warn Info |
|---|---|---|---|
| -Status | String | Normal | The event status. |
| -ResourceId | String | i- rj99xc6cptkk64ml* *** | The resource ID. |
| -RegionId | String | cn-hangzhou | The region ID. |
| - InstanceName | String | ECS-test | The instance name. |
| -Time | Long | 1635993751000 | The time when the event occurred. The value is a timestamp. Unit: milliseconds. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned. |
| RequestId | String | C7A7B776-0ACE- 5A93-9B07- DE8008D9CCDF | The request ID. |
| Success | String | true | Indicates whether the request was successful. Valid values: true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSystemEventCount &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"C7A7B776-0ACE-5A93-9B07-DE8008D9CCDF",
 "SystemEventCounts":{
  "Status":"Normal",
  "InstanceName":"ECS-test",
  "ResourceId":"i-rj99xc6cptkk64ml****",
  "Content":"Notification of instance status change",
  "Num":3,
  "Product":"ECS",
  "Level":"Info",
  "Time":1635993751000,
  "RegionId":"cn-hangzhou",
  "Name":"Instance:StateChange",
  "GroupId":"17285****"
```

`},`

```json
 "Code":"200",
 "Success":"true"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.6.4 SendDryRunSystemEvent

Debugs system events for Alibaba Cloud resources.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Product | Strin g | Query | Yes | ecs | The name of the cloud service. For information about the system events supported by CloudMonitor for Alibaba Cloud services, see System events. |
| EventNam e | Strin g | Query | Yes | Agent Status Stopped _ _ | The event name. For more information, see DescribeSystemEve ntMetaList. |
| GroupId | Strin g | Query | No | 123456 | The ID of the application group. |
| EventCont ent | Strin g | Query | No | {"product":"CloudMonito r","resourceId":"acs:ecs: cn- hongkong:17365111343 8****:instance/{instance Id}","level":"CRITICAL","i nstanceName":"instance Name","regionId":"cn- hangzhou","name":"Age nt Status Stopped","con _ _ tent": {"ipGroup":"0.0.0.0,0.0. 0.1","tianjimonVersion":" 1.2.11"},"status":"stopp ed"} | The event content. The value of this parameter is a JSON object. We recommend that you include the product , resourceId , and regionId fields in the JSON object. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 486029C9-53E1- 44B4-85A8- 16A571A043FD | The request ID. |
| Success | String | true | Indicates whether the request was successful. Valid values: true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SendDryRunSystemEvent &Product=ecs &EventName=Agent_Status_Stopped &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"486029C9-53E1-44B4-85A8-16A571A043FD",
 "Code":"200",
 "Success":"true"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.6.5 PutCustomEvent

Reports custom events.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|
| EventInfo | Repe atList | Query | No |   |   | The event details. |   |   |
| - EventNam e | Strin g |   | No | myEvent |   | The event name. Valid values of N: 1 to 50. |   |   |
| -Content | Strin g |   | No | IOException |   | The event content. Valid values of N: 1 to 50. |   |   |
| -Time | Strin g |   | No | 20171013T170923.456 +0800 |   | The time when the event occurred. Format: yyyyMMddTHHmmss.SSSZ . Valid values of N: 1 to 50. You can also specify a UNIX timestamp. Example: 1552199984000. Unit: milliseconds. |   |   |
|   |   |   |   |   |   |   | yyyyMMddTHHmmss.SSSZ |   |
| -GroupId | Strin g |   | No | 123456 |   | The ID of the application group. Valid values of N: 0 to 50. Default value: 0. This value indicates that the event to be reported does not belong to any application group. |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 131DD9C8-9A32- 4428-AD2E- 4E3013B6E3A7 | The request ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutCustomEvent &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"131DD9C8-9A32-4428-AD2E-4E3013B6E3A7",
 "Code":"200"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.6.6 DescribeSystemEventMetaList

Queries the meta information about system events.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |   | The returned metadata information. |
| -Product | String | ADS | The abbreviation of the service name. |
| -Name | String | SelectFailureRate | The event name. |
| -NameDesc | String | High query failure rate | The description of the event name. |
| -Level | String | INFO | The alert level. Valid values: CRITICAL WARN INFO |
| -Status | String | failed | The event status. |
| -StatusDesc | String | Operation Failed | The description of the event status. |
| -EventType | String | Exception | The event type. Valid values: StatusNotification: fault notifications Exception: exceptions Maintenance: O&M |
| RequestId | String | A6582C8B-E67C- 4A19-BC15- EAEFEBDC7995 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSystemEventMetaList
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"A6582C8B-E67C-4A19-BC15-EAEFEBDC7995",
 "Data":{
  "Status":"failed",
  "StatusDesc":"Operation Failed",
  "NameDesc":"High query failure rate",
  "EventType":"Exception",
  "Product":"ADS",
  "Level":"INFO",
  "Name":"SelectFailureRate"
```

`},`

```json
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.6.7 DescribeCustomEventCount

Queries the number of times that a custom event occurred within a period of time.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Query | No | BABEL BUY _ | The event name. |
| Level | Strin g | Query | No | 123 | The level of the event. |
| EventId | Strin g | Query | No | 123 | The event ID. |
| GroupId | Strin g | Query | No | 12345 | The ID of the application group. |
| SearchKey words | Strin g | Query | No | cms | The keywords that are used to search for the event. If you need to query the event whose content contains A and B, set the value to A and B. If you need to query the event whose content contains A or B, set the value to A or B. |
| StartTime | Strin g | Query | No | 1552209685596 | The start time. The value is a UNIX timestamp. It is the number of seconds that have elapsed since 00:00:00 UTC, January 1, 1970. |
| EndTime | Strin g | Query | No | 1552220485596 | The end time. The value is a UNIX timestamp. It is the number of seconds that have elapsed since 00:00:00 UTC, January 1, 1970. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomEventC ounts | Array |   | The details of the custom event. |
| -Name | String | BABEL BUY _ | The event name. |

| CloudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| -Num | Integer | 20 | The number of events. |
| -Time | Long | 1552267615000 | The time when the event occurred. The value is a UNIX timestamp. It is the number of seconds that have elapsed since 00:00:00 UTC, January 1, 1970. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned. |
| RequestId | String | 60912C8D-B340- 4253-ADE7- 61ACDFD25CFC | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCustomEventCount &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "CustomEventCounts":{
  "Num":20,
  "Time":1552267615000,
  "Name":"BABEL_BUY"
```

`},`

```json
 "Message":"success",
 "RequestId":"60912C8D-B340-4253-ADE7-61ACDFD25CFC",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.6.8 DescribeCustomEventAttribute

Queries the details of a custom event.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Query | No | test123 | The event name. |
| Level | Strin g | Query | No | value | The event level. |
| EventId | Strin g | Query | No | 123**** | The event ID. |
| GroupId | Strin g | Query | No | 123**** | The ID of the application group. |
| SearchKey words | Strin g | Query | No | cms | The keywords that are used to search for the event. If you need to query the custom event whose content contains A and B, set the value to A and B. If you need to query the custom event whose content contains A or B, set the value to A or B. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| StartTime | Strin g | Query | No | 1552224365971 | The start time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| EndTime | Strin g | Query | No | 1552227965971 | The end time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| Reverse | Boole an | Query | No | 1 | To reverse. |
| PageNum ber | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 50 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomEvents | Array | value | The event details. |
| -Id | String | 123 | The event ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Content | String | requestId:4975A6F 3-19AC-4C01- BAD2- 034DA07FEBB5, info: {"autoPay":false,"a utoUseCoupon":fal se,"bid":"26842","b uyerId":118935342 242****,"commodit ies": [{"aliyunProduceC ode":"cms","charg eType":"PREPAY"," commodityCode":" cms call num","co _ _ mponents": [{"componentCode ":"phone count","i _ nstanceProperty": [{"code":"phone c _ ount","value":"500" }],"moduleAttrStat us":1}],"duration": 6,"free":false,"orde rParams": {"aliyunProduceCo de":"cms"},"orderT ype":"BUY","prePay PostCharge":false," pricingCycle":"Mon th","quantity":1,"re fundSpecCode":""," renewChange":fals e,"specCode":"cms call num","specU _ _ pdate":false,"syncT oSubscription":fals e,"upgradeInquireF inancialValue":true }],"fromApp":"com monbuy","orderPar ams": {"priceCheck":"tru e"},"payerId":1189 35342242****,"req uestId":"ade3ad32- f58b-45d7-add4- ac542be3d8ec","sk ipChannel":false,"u serId":1189353422 42****} | The content of the event. |
| -GroupId | String | 12345 | The ID of the application group. |
| -Name | String | BABEL CHECK _ | The event name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Time | String | 1552199984000 | The time when the event occurred. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | userId:1736511134 38**** and name:"BABEL CHE _ CK" | The returned message. |
| RequestId | String | 60912C8D-B340- 4253-ADE7- 61ACDFD25CFC | The request ID. |
| Success | String | true | Indicates whether the request was successful. Valid values: true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCustomEventAttribute &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "CustomEvents":{
  "Content":"requestId:4975A6F3-19AC-4C01-BAD2-034DA07FEBB5, info:
{\"autoPay\":false,\"autoUseCoupon\":false,\"bid\":\"26842\",\"buyerId\":118935342242**** "commodities\": [{\"aliyunProduceCode\":\"cms\",\"chargeType\":\"PREPAY\",\"commodityCode\":\"cms_call_nu ",\"components\":[{\"componentCode\":\"phone_count\",\"instanceProperty\": [{\"code\":\"phone_count\",\"value\":\"500\"}],\"moduleAttrStatus\":1}],\"duration\":6,\" ee\":false,\"orderParams\": {\"aliyunProduceCode\":\"cms\"},\"orderType\":\"BUY\",\"prePayPostCharge\":false,\"pricin ycle\":\"Month\",\"quantity\":1,\"refundSpecCode\":\"\",\"renewChange\":false,\"specCode\ \"cms_call_num\",\"specUpdate\":false,\"syncToSubscription\":false,\"upgradeInquireFinanc lValue\":true}],\"fromApp\":\"commonbuy\",\"orderParams\": {\"priceCheck\":\"true\"},\"payerId\":118935342242****,\"requestId\":\"ade3ad32-f58b-45 d7-add4-ac542be3d8ec\",\"skipChannel\":false,\"userId\":118935342242****}",
  "Time":"1552199984000",
  "Id":"123",
  "GroupId":"12345",
  "Name":"BABEL_CHECK"
```

`},`

```json
 "Message":"userId:173651113438**** and name:\"BABEL_CHECK\"",
 "RequestId":"60912C8D-B340-4253-ADE7-61ACDFD25CFC",
 "Code":"200",
 "Success":"true"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

### 2.7 Custom dashboard

#### 2.7.1 CreateDashboardFolder

Creates a dashboard folder.
**Rate limit**: The default API rate limit is 10,000 requests per second, and the default user
rate limit is 50 requests per second.
**API visibility**: This is a private API that only internal systems can call.
**Authentication method**: AccessKey authentication.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Integ er | Quer y | No | 1 | The organization ID. |
| FolderNam e | Strin g | Quer y | Yes | my dashboard folder _ _ | The name of the dashboard folder. |
| SourceTyp e | Strin g | Quer y | No | custom | The origin type of the resource. Example: custom |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4C467B38-391A- 5B8B-9B3D- 2C7D3F82B3D1 | The unique ID of the request. |
| Code | String | 200 | The business status code. A value of 200 indicates that the operation succeeded. |
| Success | Boolean | true | Indicates whether the operation succeeded. A value of true indicates success. |
| Resource | String | folder-12345 | The unique resource identifier of the newly created dashboard folder. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateDashboardFolder &FolderName=my_dashboard_folder &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"4C467B38-391A-5B8B-9B3D-2C7D3F82B3D1",
 "Resource":"folder-12345",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HttpCode | Error Code | Error message | Description |
|---|---|---|---|
| 400 | ParameterInvalid | Illegal parameters. | Invalid parameters. |
| 403 | AccessForbidden | User not authorized to operate on the specified resource. | You do not have the permissions to perform operations on the specified resource. |
| 404 | ResourceNotFound | The specified resource is not found. | The specified resource is not found. |
| 500 | InternalError | The request processing has failed due to some unknown error. | An internal error occurred. |

#### 2.7.2 ModifyDashboardToFolder

Moves one or more dashboards to a specified folder.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Integ er | Quer y | No | 123456 | The ID of the organization. This parameter identifies the Grafana organization. |

| BoardIdJso nArray | Strin g | Quer y | Yes | ["board 001", _ "board 002", _ "board 003"] _ | The list of dashboard IDs to move, specified in JSON array format. |
|---|---|---|---|---|---|
| FolderId | Strin g | Quer y | Yes | 654321 | The unique identifier of the destination folder. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233**** | The unique identifier of the request, which can be used for troubleshooting. |
| Code | String | 200 | The business error code. A value of 200 indicates success. Any other value indicates failure. |
| Success | Boolean | true | Indicates whether the operation succeeded. Valid values: true (success) and false (failure) |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyDashboardToFolder &BoardIdJsonArray=["board_001", "board_002", "board_003"] &FolderId=123 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
 "Code":"404",
 "Success":true
```

`}`

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| 500 |   | InternalError | The system failed to process the request due to some unknown errors. |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | The parameter is invalid. |
| 403 | 403 | AccessForbidden | You do not have the permissions to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

#### 2.7.3 ModifyDashboardFolder

Modifies the name of a specific dashboard folder.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Integ er | Quer y | No | 35 | The organization ID that identifies the organization to which the resource belongs. |
| FolderNam e | Strin g | Quer y | Yes | rdFolder | The name of the folder. The name must be 1 to 24 characters in length and can contain letters, digits, underscores ( ), _ periods (.), and hyphens (-). |
| FolderId | Strin g | Quer y | Yes | 123 | The unique ID of the folder to modify. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID that identifies a request and is used for troubleshooting and tracking. |
|---|---|---|---|
| Code | String | 404 | The business error code. Valid values: 200: The operation succeeded. Non-200: The operation failed. For specific error codes and descriptions, see the error message section. |
| Success | Boolean | true | Indicates whether the operation succeeded. Valid values: true: The operation succeeded. false: The operation failed. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyDashboardFolder &FolderName=rdFolder &FolderId=123 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
 "Code":"404",
 "Success":true
```

`}`

**Error codes**

| HttpCode | Error Code | Error message | Description |
|---|---|---|---|
| 500 |   | InternalError | The system failed to process the request due to some unknown errors. |
| 400 | 400 | ParameterInvalid | The request parameter is invalid. Check whether the parameter format, type, and value range meet the API requirements. |

| 403 | 403 | AccessForbidden | The user does not have the permissions to operate on the specified resource. Verify that the account permissions and resource ownership are correct. |
|---|---|---|---|
| 404 | 404 | ResourceNotFound | The specified resource is not found. Check whether the folder ID (folderId) is correct. |

#### 2.7.4 DescribeDashboard

Queries Cloud Monitor (CMS) dashboard information and filters dashboards by keyword, folder, and pagination.

**Protocol and timeout**

Supported protocols: HTTP and HTTPS Timeout: 5,000 milliseconds Request method: POST or GET

**Throttling policy**

Default QPS per user: 50 Default API QPS: 10,000 Throttling unit: seconds

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Valid values: 1 to 100 |
| SourceTyp e | Strin g | Quer y | No | custom | The source type of the dashboard. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Pages start from 1. |
| BoardId | Strin g | Quer y | No | board-abc | The ID of the dashboard to query. |

| DefaultBoa rd | Bool ean | Quer y | No | true | Specifies whether to query the default dashboard. |
|---|---|---|---|---|---|
| Departme nt | Integ er | Quer y | No | 100 | The organization ID, which is also the department ID. |
| AcceptLan guage | Strin g | Quer y | Yes | zh-CN | The language of the response content. Common values: zh-CN for Chinese and en-US for English |
| FolderId | Strin g | Quer y | No | folder-123 | The unique identifier of the folder to which the dashboard belongs. This parameter filters dashboards in a specific folder. |
| Keyword | Strin g | Quer y | No | Monitoring | The keyword in the dashboard name. Fuzzy match is supported. |

If you do not specify `RegionId` , the system uses `cn-hangzhou` by default.

|   | AcceptLanguage |   |
|---|---|---|
| US |   |   |
|   |   | for English |

`AcceptLanguage` is a required parameter. Common values: `zh-CN` for Chinese and `en-` Use the pagination parameters `PageNumber` and `PageSize` together.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4C4F-F9D3-4A1B- 9F1E- 1234567890AB | The unique ID of the request for troubleshooting. |
| Code | String | 200 | The business status code. A value of 200 indicates success. |
| Resources | String | [{"BoardId":"b- 1","Name":"Monito ring Dashboard"}] | The list of dashboard resources in JSON string format. |
| Success | Boolean | true | Indicates whether the request is successful. Valid values: true (success) and false (failure) |

**Examples**

Request example

```
http(s)://[Endpoint]/?Action=DescribeDashboard &AcceptLanguage=zh-CN &Common request parameters
```

Successful response example `JSON` format `{`

```json
 "RequestId":"4C4F-F9D3-4A1B-9F1E-1234567890AB",
 "Resources":"[{\"BoardId\":\"b-1\",\"Name\":\"Monitoring Dashboard\"}]",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ParameterInvalid | Illegal parameters. | The request parameters are invalid. Check the parameter format and value range. |
| 403 | AccessForbidden | User not authorized to operate on the specified resource. | The current user does not have permissions to access the specified resource. Verify the permission configuration. |
| 404 | ResourceNotFound | The specified resource is not found. | The requested resource is not found. Check the resource ID or path. |
| 500 | InternalError | The request processing has failed due to some unknown error. | An internal server error occurred. Try again later or contact technical support. |

**Notes**

1. The `Resources` field is a string in JSON format. You must parse it into an array of objects.
2. The gateway automatically injects internal system parameters such as ResourceOwnerId
and SecurityToken. You do not need to pass these parameters explicitly.
3. We recommend that you use the HTTPS protocol for API calls in production environments.

### 2.8 Application group

#### 2.8.1 DescribeMonitorGroups

Queries application groups.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| SelectCont actGroups | Bool ean | Quer y | No | true | Specifies whether to include the alert contact groups in the response. Valid values: true: The alert contact groups are included. false: The alert contact groups are excluded. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Pages start from page 1. Default value: 1. |
| PageSize | Integ er | Quer y | No | 30 | The number of entries per page. Pages start from page 1. Default value: 30. |
| Keyword | Strin g | Quer y | No | test | The search keyword. |
| InstanceId | Strin g | Quer y | No | i-abcdefgh12**** | The instance ID. This parameter is used to query the application group to which the specified instance belongs. |
| GroupNam e | Strin g | Quer y | No | testGroup124 | The name of the application group. |
| ResourceG roupId | Strin g | Quer y | No | 123 | The ID of the resource group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Resources | Array |   | The resources that are associated with the application group. |
| - ContactGroups | Array |   | The alert contact group. |
| --Name | String | test | The name. |
| -GroupId | Long | 12345 | The ID of the application group. |
| -GroupName | String | test123 | The name of the application group. |
| -ServiceId | String | 49**** | The ID of the Alibaba Cloud service. |
| -Type | String | custom | The type of the application group. Valid values: custom: a self-managed application group ehpc cluster: an application group that _ is synchronized from an Elastic High Performance Computing (E-HPC) cluster kubernetes: an application group that is synchronized from a Container Service for Kubernetes (ACK) cluster |
| -GmtModified | Long | 1603181891000 | The timestamp when the application group was modified. Unit: milliseconds. |
| -GmtCreate | Long | 1603181891000 | The timestamp when the application group was created. Unit: milliseconds. |
| -BindUrl | String | https://aliyun.com | The URL of the ACK cluster from which the application group is synchronized. |
| - ResourceGrou pId | Long | rg- aek2hopjh******* | The resource ID. |
| RequestId | String | F02B299A-D374- 4595-9F55- 7534D604F132 | The request ID. |

| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
|---|---|---|---|
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 30 | The number of entries per page. |
| Total | Integer | 10 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMonitorGroups &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"F02B299A-D374-4595-9F55-7534D604F132",
 "Message":"The specified resource is not found.",
 "PageSize":30,
 "PageNumber":1,
 "Total":10,
 "Resources":{
  "GroupName":"test123",
  "Type":"custom",
  "GmtCreate":1603181891000,
  "ResourceGroupId":"rg-aek2hopjh*******",
  "-ContactGroups":{
   "Name":""
```

`},`

```json
  "BindUrl":"https://aliyun.com",
  "GmtModified":1603181891000,
  "GroupId":12345,
  "ServiceId":"49****"
```

`},`

```json
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | AccessForbidden | The X.509 certificate or cms access key ID provided does not exist in our records. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |

| loudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
|---|---|---|---|
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.2 DescribeMonitorGroupInstances

Queries the resources in an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | No | 10 | The number of entries per page. Default value: 10. |
| PageNum ber | Integ er | Query | No | 1 | The page number. Default value: 1. |
| GroupId | Long | Query | Yes | 12345 | The ID of the application group. |
|   |   |   |   |   | The abbreviation of the service name. Valid values: ecs: Elastic Compute Service (ECS) instances provided by Alibaba Cloud and hosts not provided by Alibaba Cloud rds: ApsaraDB RDS ads: AnalyticDB slb: Server Load Balancer (SLB) vpc: Virtual Private Cloud (VPC) apigateway: API Gateway cdn: Alibaba Cloud |

| Parame ter | Typ e | Locati on | Require d | Example | Content Delivery DeNsectwrioprkt i(oCnDN) cs: Container Service |
|---|---|---|---|---|---|
|   |   |   |   |   | for Swarm dcdn: Dynamic Content Delivery |
| Category | Strin g | Query | No | ecs | Network (DCDN) ddos: Anti-DDoS eip: Elastic IP Address (EIP) elasticsearch emr: E-MapReduce ess: Auto Scaling hbase: ApsaraDB for HBase iot edge: Link IoT _ Edge k8s pod: pods in _ Container Service for Kubernetes (ACK) kvstore sharding: _ ApsaraDB for Redis (cluster architecture) kvstore splitrw: _ ApsaraDB for Redis (read/write splitting architecture) kvstore standard: _ ApsaraDB for Redis (standard architecture) memcache: ApsaraDB for Memcache mns: Message Service (MNS) mongodb: ApsaraDB for MongoDB of the replica set architecture mongodb cluster: _ ApsaraDB for MongoDB of the cluster architecture mongodb sharding: _ ApsaraDB for MongoDB of the sharded cluster architecture mq topic: MNS topics _ ocs: ApsaraDB for Memcache of earlier versions opensearch: OpenSearch oss: Object Storage Service (OSS) polardb: PolarDB petadata: HybridDB |

| Parame ter | Typ e | Locati on | Require d | Example | for MySQL Desscdcnr:i pSeticounre CDN (SCDN) |
|---|---|---|---|---|---|
|   |   |   |   |   | sharebandwidthpacka ges: Internet Shared Bandwidth sls: Simple Log Service vpn: VPN Gateway Valid values of N: 1 to 200. |
| Keyword | Strin g | Query | No | s1 | The keyword used to search for instances. Fuzzy search based on instance names is supported. |
| InstanceId s | Strin g | Query | No | i-x1234568 | The instance ID. You can query multiple instances by specifying multiple IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Resources | Array |   | The information about the resources in the application group. |
| -Id | Long | 12345 | The resource ID. |
| -RegionId | String | cn-hangzhou | The ID of the region where the instance resides. |
| -InstanceId | String | i-2ze3w55tr2r**** | The instance ID. |
| -Category | String | ecs | The abbreviation of the service name. |
| - InstanceName | String | hostIP | The instance name. |
| RequestId | String | 97F2A410-9412- 499C-9AD1- 76EF7EC02DF2 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| Total | Integer | 12 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMonitorGroupInstances &GroupId=12345 &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"97F2A410-9412-499C-9AD1-76EF7EC02DF2",
 "Message":"success",
 "PageSize":10,
 "PageNumber":1,
 "Total":12,
 "Resources":{
  "InstanceName":"hostIP",
  "Category":"ecs",
  "InstanceId":"i-2ze3w55tr2r****",
  "Id":12345,
  "RegionId":"cn-hangzhou"
```

`},`

```json
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | AccessForbidden | The X.509 certificate or cms access key ID provided does not exist in our records. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.3 CreateMonitorGroupInstances

Adds resources to an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| GroupId | Long | Quer y | Yes | 3607**** | The ID of the application group. |
| Instances | Repe atLis t | Quer y | Yes |   | The instances. |

| -Category | Strin g |   | Yes | ecs | The abbreviation of the cloud service name. For more information about how to query the abbreviations of cloud service names, see metricCategory in the response parameter Labels of the DescribeProjectMeta operation. |
|---|---|---|---|---|---|
| -InstanceId | Strin g |   | Yes | i-2ze26xj5wwy12**** | The instance ID. |
| -RegionId | Strin g |   | Yes | cn-hangzhou | The ID of the region where the instance resides. |
| - InstanceN ame | Strin g |   | Yes | test-instance-ecs | The instance name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1BC69FEB-56CD- 4555-A0E2- 02536A24A946 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateMonitorGroupInstances &GroupId=3607**** &Instances=null &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"1BC69FEB-56CD-4555-A0E2-02536A24A946",
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | InvalidClientTokenId | The X.509 certificate or cms access key ID provided does not exist in our records. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |

| Developer Gu | ide·API Reference |   | CloudMonito |
|---|---|---|---|

| 412 | 4121 | ResourcesOverLimit | Resources over limit. |
|---|---|---|---|
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.4 DescribeUnhealthyHostAvailability

Queries unhealthy instances.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| Id | Repe atLis t | Quer y | No | 123456 | The task ID. Valid values of N: 1 to 20. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| UnhealthyList | Array |   | The unhealthy instances that are detected by the specified availability monitoring tasks. |
| -InstanceList | Normal | ["1","2"] | The queried instances. |
| -Id | Long | 123456 | The task ID. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |

| Message | String | User not authorized to operate on the specified resource. | The returned message. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeUnhealthyHostAvailability &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"User not authorized to operate on the specified resource.",
 "RequestId":"ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
 "Code":"200",
 "Success":true,
 "UnhealthyList":{
  "Id":123456,
  "InstanceList":"[\"1\",\"2\"]"
```

`}` `}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |

| 404 | 404 | ResourceNotFound | The specified resource is not found. |
|---|---|---|---|
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.5 DeleteMonitorGroupInstances

Removes instances from an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| GroupId | Long | Quer y | Yes | 123456 | The ID of the application group. |
| InstanceId List | Strin g | Quer y | Yes | i-a2d5q7pm3f912****,i- a2d5q7pm3f222**** | The instances to be removed from the application group. Separate multiple instances with commas (,). You can remove a maximum of 20 instances from an application group at a time. |
|   |   |   |   |   | The abbreviation of the service name. Valid values: ECS: Elastic Compute Service (ECS) instances provided by Alibaba Cloud and hosts not provided by Alibaba Cloud RDS: ApsaraDB RDS ADS: AnalyticDB SLB: Server Load Balancer (SLB) VPC: Virtual Private Cloud (VPC) APIGATEWAY: API Gateway |

|   |   |   |   |   | CDN: Alibaba Cloud Content Delivery Network (CDN) CS: Container Service for Swarm DCDN: Dynamic Content Delivery |
|---|---|---|---|---|---|
| Category | Strin g | Quer y | Yes | ecs | Network (DCDN) DDoS: Anti-DDoS EIP: Elastic IP Address (EIP) ELASTICSEARCH: Elasticsearch EMR: E-MapReduce ESS: Auto Scaling HBASE: ApsaraDB for Hbase IOT EDGE: Link IoT _ Edge K8S POD: pods in _ Container Service for Kubernetes (ACK) KVSTORE SHARDING: _ ApsaraDB for Redis (cluster architecture) KVSTORE SPLITRW: _ ApsaraDB for Redis (read/write splitting architecture) KVSTORE STANDARD: _ ApsaraDB for Redis (standard architecture) MEMCACHE: ApsaraDB for Memcache MNS: Message Service (MNS) MONGODB: ApsaraDB for MongoDB of the replica set architecture MONGODB CLUSTER: _ ApsaraDB for MongoDB of the cluster architecture MONGODB SHARDING: _ ApsaraDB for MongoDB of the sharded cluster architecture MQ TOPIC: MNS topics _ OCS: ApsaraDB for Memcache of earlier versions OPENSEARCH: OpenSearch |

|   |   |   |   |   | OSS: Object Storage Service (OSS) POLARDB: PolarDB PETADATA: HybridDB for MySQL SCDN: Secure CDN (SCDN) SHAREBANDWIDTHPAC KAGES: Internet Shared Bandwidth SLS: Simple Log Service |
|---|---|---|---|---|---|

VPN: VPN Gateway

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5351B0F2-26A9- 4BC9-87FF- 1B74034D12C3 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMonitorGroupInstances &GroupId=123456 &InstanceIdList=i-a2d5q7pm3f912****,i-a2d5q7pm3f222**** &Category=ecs &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"5351B0F2-26A9-4BC9-87FF-1B74034D12C3",
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.6 DescribeMonitorGroupInstanceAttribute

Queries the details of the resources in an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| GroupId | Long | Quer y | Yes | 123456 | The ID of the application group. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Valid values: 1 to 1000000000. Default value: 1. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Valid values: 1 to 1000000000. Default value: 10. |

| Total | Bool ean | Quer y | No | true | Specifies whether to return the total number of resources in the specified application group. Valid values: true (default) false |
|---|---|---|---|---|---|
| Category | Strin g | Quer y | No | ecs | The abbreviation of the cloud service name. For more information about how to query the abbreviations of cloud service names, see the metricCategory tag in the response parameter Labels of the DescribeProjectMeta operation. |
| Keyword | Strin g | Quer y | No | portal | The keyword that is used to search for resources. |
| InstanceId s | Strin g | Quer y | No | i-m5e0k0bexac8tykr**** | The resource ID. Separate multiple resource IDs with commas (,). You can query the details about a maximum of 20 resources in each request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Resources | Array |   | The resources that are associated with the application group. |
| -Tags | Array |   | The tags of the resource. |
| --Key | String | key | The tag key. |
| --Value | String | value | The value. |
| - InstanceName | String | hostName | The instance name. |

| -InstanceId | String | i- m5e0k0bexac8tykr **** | The instance ID. |
|---|---|---|---|
| -Desc | String | desc test _ | The resource description. |
| -NetworkType | String | vpc | The network type. |
| -Category | String | ecs | The name of the cloud service. |
| -Dimension | String | {"instanceId":"i- m5e0k0bexac8tykr ****"} | The dimensions of the resource that is associated with the application group. |
| -Region | Struct |   | The region. |
| --RegionId | String | cn-wulan-env212- d01 | The unit. |
| -- AvailabilityZon e | String | value | The availability zone. |
| -Vpc | Struct |   | The information about the virtual private cloud (VPC). |
| -- VpcInstanceId | String | value | The VPC ID. |
| -- VswitchInstanc eId | String | value | The vSwitch ID. |
| RequestId | String | 9FB8EA79-7279- 4482-8D6D- 3D28EEDD871A | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
|---|---|---|---|
| Message | String | The specified resource is not found. | The returned message. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 2 | The number of entries per page. |
| Total | Integer | 12 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMonitorGroupInstanceAttribute &GroupId=123456 &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"9FB8EA79-7279-4482-8D6D-3D28EEDD871A",
 "Message":"The specified resource is not found.",
 "PageSize":2,
 "PageNumber":1,
 "Total":12,
 "Resources":{
  "InstanceName":"hostName",
  "Desc":"desc_test",
  "Category":"ecs",
  "-Region":{
   "AvailabilityZone":"",
   "RegionId":""
```

`},`

```json
  "InstanceId":"i-m5e0k0bexac8tykr****",
  "NetworkType":"vpc",
  "-Tags":{
   "Value":"",
   "Key":""
```

`},`

```json
  "-Vpc":{
   "VswitchInstanceId":"",
   "VpcInstanceId":""
```

`},`

```json
  "Dimension":"{\"instanceId\":\"i-m5e0k0bexac8tykr****\"}"
```

`},`

```json
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | AccessForbidden | The X.509 certificate or cms access key ID provided does not exist in our records. |

| 404 | 404 | ResourceNotFound | The specified resource is not found. |
|---|---|---|---|
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.7 DescribeHostAvailabilityList

Queries availability monitoring tasks.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| Id | Long | Quer y | No | 123456 | The ID of the availability monitoring task. |
| TaskName | Strin g | Quer y | No | ecs instance _ | The name of the availability monitoring task. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Pages start from page 1. Default value: 1. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Pages start from page 1. Default value: 10. |

| GroupId | Long | Quer y | No | 12345 | The ID of the application group. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TaskList | Array |   | The tasks. |
| -Instances | Normal |   | The instances. |
| -Id | Long | 123456 | The ID of the availability monitoring task. |
| -TaskName | String | ecs instance _ | The name of the availability monitoring task. |
| -TaskType | String | HTTP | The task type. Valid values: PING TELNET HTTP |
| -TaskScope | String | GROUP | The range of instances that are monitored by the availability monitoring task. Valid values: GROUP: All Elastic Compute Service (ECS) instances in the application group are monitored. GROUP SPEC INSTANCE: Specified ECS _ _ instances in the application group are monitored. |
| -Disabled | Boolean | false | Indicates whether the availability monitoring task is disabled. Valid values: true: The availability monitoring task is disabled. false: The availability monitoring task is enabled. |
| -GroupId | Long | 12345 | The ID of the application group. |
| -GroupName | String | Group ECS _ | The name of the application group. |

| -TaskOption | Struct |   | The task option. |
|---|---|---|---|
| --HttpURI | String | https://www.aliyun. com | The URI that you want to monitor. This parameter is required if the TaskType parameter is set to HTTP. |
| -- TelnetOrPingH ost | String | ssh.aliyun.com | The domain name or IP address that you want to monitor. |
| -- HttpResponse Charset | String | UTF-8 | The character set that is used in the HTTP response. |
| --HttpKeyword | String | OK | The response to the HTTP request. |
| --HttpMethod | String | GET | The HTTP request method. Valid values: GET POST HEAD |
| --HttpNegative | Boolean | true | The method to trigger an alert. The alert can be triggered based on whether the specified alert rule is included in the response body. Valid values: true: If the HTTP response body includes the alert rule, an alert is triggered. false: If the HTTP response does not include the alert rule, an alert is triggered. |
| --Interval | Integer | 60 | The interval at which detection requests are sent. Unit: seconds. |
| --HttpHeader | String |   | The HTTP request header. |
| -- HttpPostConte nt | String | params1=paramsV alue1 | The content of the HTTP POST request. |
| -AlertConfig | Struct |   | The configurations of the alert rule. |
| -- EscalationList | Array |   | The trigger conditions of the alert rule. |

| ---MetricName | String | HttpStatus | The metric name. Valid values: HttpStatus: HTTP status code HttpLatency: HTTP response time TelnetStatus: Telnet status code TelnetLatency: Telnet response time PingLostRate: Ping packet loss rate |
|---|---|---|---|
| ---Aggregate | String | value | The method used to calculate the metric values that trigger alerts. Valid values: Value: the value of the HTTP status code Average: the average HTTP response time Value: the value of the Telnet status code TelnetLatency: the average Telnet response time Average: the average Ping packet loss rate |
| ---Operator | String | = | The comparison operator that is used in the alert rule. Valid values: = < <= = |
| ---Value | String | 400 | The alert threshold. |
| ---Times | String | 3 | The consecutive number of times for which the metric value is measured before an alert is triggered. |
| --NotifyType | Integer | 1 | The alert notification methods. Valid values: 2: Alert notifications are sent by using phone calls, text messages, emails, and DingTalk chatbots. 1: Alert notifications are sent by using text messages, emails, and DingTalk chatbots. 0: Alert notifications are sent by using emails and DingTalk chatbots. |
| --StartTime | Integer | 0 | The start time. |
| --EndTime | Integer | 22 | The end time. |

| --SilenceTime | Integer | 86400 | The mute period during which new alerts are not sent even if the trigger conditions are met. Unit: seconds. |
|---|---|---|---|
| --WebHook | String | https://www.aliyun. com | The callback URL. CloudMonitor pushes an alert notification to the specified callback URL by sending an HTTP POST request. Only the HTTP protocol is supported. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 4A288E86-45C3- 4858-9DB0- 6D85B10BD92A | The request ID. |
| Total | Integer | 1 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeHostAvailabilityList &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"4A288E86-45C3-4858-9DB0-6D85B10BD92A",
 "TaskList":{
  "Instances":"",
  "GroupName":"Group_ECS",
  "TaskName":"ecs_instance",
  "-AlertConfig":{
   "NotifyType":1,
   "SilenceTime":86400,
   "--EscalationList":{
    "Operator":"=",
    "MetricName":"HttpStatus",
    "Times":"3",
    "Value":"400",
    "Aggregate":"value"
```

`},`

```json
   "EndTime":22,
   "StartTime":0,
   "WebHook":"https://www.aliyun.com"
```

`},`

```json
  "TaskScope":"GROUP",
  "TaskType":"HTTP",
  "Id":123456,
  "Disabled":false,
  "-TaskOption":{
   "HttpHeader":"",
   "HttpPostContent":"params1=paramsValue1
```

`",`

```json
   "TelnetOrPingHost":"ssh.aliyun.com
```

`",`

```json
   "HttpResponseCharset":"UTF-8
```

`",`

```json
   "HttpKeyword":"OK
```

`",`

```json
   "HttpURI":"https://www.aliyun.com
```

`",`

```json
   "HttpNegative":true,
   "HttpMethod":"GET",
   "Interval":60
```

`},`

```json
  "GroupId":12345
```

`},`

```json
 "Total":1,
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.8 CreateMonitorGroup

Creates an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupNa me | Strin g | Query | Yes | ECS Group _ | The name of the application group. |
| ContactGr oups | Strin g | Query | No | ECS Alert Group _ _ | The alert contact group. The alert notifications of the application group are sent to the alert contacts that belong to the alert contact group. An alert contact group can contain one or more alert contacts. For more information about how to create alert contacts and alert contact groups, see PutContact and PutContactGroup. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 83C89BA6-ABD4- 4398-A175- 83E86C47A001 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |
| GroupId | Long | 1234567 | The ID of the application group. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateMonitorGroup &GroupName=ECS_Group &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"83C89BA6-ABD4-4398-A175-83E86C47A001",
 "Code":200,
 "Success":true,
 "GroupId":1234567
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |

| Developer Gu | ide·API Reference |   | CloudMonito |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 409 | 4092 | ResourceExist | Resources already exist. |
| 412 | 4121 | ResourcesOverLimit | Resources over limit. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.9 DeleteMonitorGroup

Deletes an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupId | Long | Query | No | 123456 | The ID of the application group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CA35B3AE-4FFD- 4A33-AE67- 67EF68711EFA | The request ID. |

| CloudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. true false |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The returned message. |
| Group | Struct |   | The deleted application groups. |
| - ContactGroups | Array |   | The alert contact groups. |
| --Name | String | ECS Group _ | The name of the alert contact group. |
| -GroupName | String | ECS test _ | The name of the application group. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMonitorGroup &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Group":{
  "GroupName":"ECS_test",
  "-ContactGroups":{
   "Name":"ECS_Group"
```

`}` `},`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"CA35B3AE-4FFD-4A33-AE67-67EF68711EFA",
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 409 | 409 | ResourceConflict | Concurrent modification of resources. |
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | InvalidClientTokenId | The X.509 certificate or cms access key ID provided does not exist in our records. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.10 CreateHostAvailability

Creates an availability monitoring task.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupId | Long | Query | Yes | 123456 | The ID of the application group. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TaskName | Strin g | Query | Yes | task1 | The name of the availability monitoring task. The name must be 4 to 100 characters in length, and can contain letters, digits, and underscores ( ). _ |
| TaskScop e | Strin g | Query | No | GROUP | The range of the instances that are monitored by the availability monitoring task. Valid values: GROUP: All Elastic Compute Service (ECS) instances in the application group are monitored. GROUP SPEC INSTAN _ _ CE: Specified ECS instances in the application group are monitored. The TaskScope parameter must be used in combination with the InstanceList parameter. The InstanceList parameter specifies the ECS instances to be monitored. |
| TaskType | Strin g | Query | Yes | HTTP | The monitoring type of the availability monitoring task. Valid values: PING TELNET HTTP |
| TaskOptio n.HttpURI | Strin g | Query | No | https://www.aliyun.com | The URI that you want to monitor. This parameter is required if the TaskType parameter is set to HTTP. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TaskOptio n.TelnetOr PingHost | Strin g | Query | No | www.aliyun.com | The domain name or IP address that you want to monitor. This parameter is required if the TaskType parameter is set to PING or TELNET. |
| TaskOptio n.HttpRes ponseCha rset | Strin g | Query | No | UTF-8 | The character set that is used in the HTTP response. Valid value: UTF-8. |
| TaskOptio n.HttpRes ponseMat chContent | Strin g | Query | No | ok | The response to the HTTP request. |
| TaskOptio n.HttpMet hod | Strin g | Query | No | GET | The HTTP request method. Valid values: GET POST HEAD This parameter is required if the TaskType parameter is set to HTTP. |

| Parame ter | Typ e | Locati on | Require d |   | Example |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|
| TaskOptio n.HttpNeg ative | Boole an | Query | No |   | true |   | The method to trigger an alert. The alert can be triggered based on whether the specified alert rule is included in the response body. Valid values: true: If the HTTP response body includes the alert rule, an alert is triggered. false: If the HTTP response does not include the alert rule, an alert is triggered. This parameter is required if the TaskType parameter is set to HTTP. |   |   |
| TaskOptio n.Interval | Integ er | Query | No |   | 60 |   | The interval at which detection requests are sent. Unit: seconds. Valid values: 15, 30, 60, 120, 300, 900, 1800, and 3600. This parameter is available only for the CloudMonitor agent V3.5.1 or later. |   |   |
| TaskOptio n.HttpHea der | Strin g | Query | No |   |   |   | The header of the HTTP request. Format: Parameter name:Parameter value . Separate multiple parameters with carriage return characters. Example: params1:value1 params2:value2 |   |   |
|   |   |   |   |   |   |   |   | Parameter |   |
|   |   |   |   |   |   |   | name:Parameter |   |   |
|   |   |   |   |   |   |   | value |   |   |
|   |   |   |   |   | token:testTokenValue |   |   |   |   |
| TaskOptio n.HttpPost Content | Strin g | Query | No |   | params1=paramsValue1 |   | The content of the HTTP POST request. |   |   |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| AlertConfi g.NotifyTy pe | Integ er | Query | Yes | 0 | The alert notification methods. Valid values: China site: 2: Alert notifications are sent by using phone calls, text messages, emails, and DingTalk chatbots. 1: Alert notifications are sent by using text messages, emails, and DingTalk chatbots. 0: Alert notifications are sent by using emails and DingTalk chatbots. International site: 0: Alert notifications are sent by using emails and DingTalk chatbots. Site for virtual network operators (VNOs): 0: Alert notifications are sent by using emails and DingTalk chatbots. |

| Parame ter | Typ e | Locati on | Require d | Example |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|
| AlertConfi g.StartTim e | Integ er | Query | No | 0 |   | The start of the time period during which the alert rule is effective. Valid values: 0 to 23. For example, if the AlertConfig.StartTim e parameter is set to 0 and the AlertConfig.EndTime parameter is set to 22, the alert rule is effective from 00:00:00 to 22:00:00. Alert notifications are sent based on the specified threshold only if the alert rule is effective. |   |   |
|   |   |   |   |   |   |   | AlertConfig.StartTim |   |
|   |   |   |   |   |   | e |   |   |
| AlertConfi g.EndTim e | Integ er | Query | No | 22 |   | The end of the time period during which the alert rule is effective. Valid values: 0 to 23. For example, if the AlertConfig.StartTim e parameter is set to 0 and the AlertConfig.EndTime parameter is set to 22, the alert rule is effective from 00:00:00 to 22:00:00. Alert notifications are sent based on the specified threshold only if the alert rule is effective. |   |   |
|   |   |   |   |   |   |   | AlertConfig.StartTim |   |
|   |   |   |   |   |   | e |   |   |
| AlertConfi g.SilenceT ime | Integ er | Query | No | 86400 |   | The mute period during which new alerts are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400, which indicates one day. |   |   |
| AlertConfi g.WebHoo k | Strin g | Query | No | https://www.aliyun.com/ webhook.json |   | The callback URL. |   |   |

|   |   | AlertConfig.EndTime |
|---|---|---|

|   |   | AlertConfig.EndTime |
|---|---|---|

|   | Developer Gui | de·API R | eference |   |   | CloudMonito | r |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| AlertConfi gEscalatio nList | Repe atList | Query | Yes | value | The alert configuration escalation list. |
| - MetricNa me | Strin g |   | Yes | HttpStatus | The metric for which the alert feature is enabled. Valid values of N: 1 to 21. Valid values: HttpStatus: HTTP status code HttpLatency: HTTP response time TelnetStatus: Telnet status code TelnetLatency: Telnet response time PingLostRate: Ping packet loss rate |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Aggregate | Strin g |   | Yes | Value | The method used to calculate the metric values that trigger alerts. Valid values of N: 1 to 21. Valid values: HttpStatus: Value HttpLatency: Average TelnetStatus: Value TelnetLatency: Average PingLostRate: Average The value Value indicates the original value and is used for metrics such as status codes. The value Average indicates the average value and is used for metrics, such as the latency and packet loss rate. |
| -Times | Integ er |   | Yes | 3 | The consecutive number of times for which the metric value meets the alert condition before an alert is triggered. Valid values of N: 1 to 21. |

| Parame ter | Typ e | Locati on | Require d | Example |   | Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
| -Operator | Strin g |   | Yes | > |   | The comparison operator that is used in the alert rule. Valid values of N: 1 to 21. Valid values: > >= < <= = |   |   |   |
| -Value | Strin g |   | Yes | 90 |   | The alert threshold. Valid values of N: 1 to 21. |   |   |   |
| InstanceLi st | Repe atList | Query | No | i-absdfkwl321**** |   | The ECS instances that are monitored. Valid values of N: 1 to 21. This parameter is required if the TaskScope parameter is set to GROUP SPEC INST _ _ ANCE . |   |   |   |
|   |   |   |   |   |   |   |   | GROUP SPEC INST _ _ |   |
|   |   |   |   |   |   |   | ANCE |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID. |

| CloudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |

| TaskId | Long | 12345 | The ID of the availability monitoring task. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateHostAvailability &GroupId=123456 &TaskName=task1 &TaskType=HTTP &AlertConfig.NotifyType=0 &AlertConfigEscalationList=null &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "TaskId":12345,
 "Message":"The specified resource is not found.",
 "RequestId":"ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 409 | 4092 | ResourceExist | Resources already exist. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.11 CreateMonitorGroupNotifyPolicy

Creates a policy to pause alert notifications for an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| PolicyTyp e | Strin g | Query | Yes | PauseNotify | The policy type. Valid value: PauseNotify. |
| GroupId | Strin g | Query | Yes | 7301**** | The ID of the application group. |
| StartTime | Long | Query | Yes | 1622949300000 | The timestamp that indicates the start time of the validity period for the policy. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| EndTime | Long | Query | Yes | 1623208500000 | The timestamp that indicates the end time of the validity period for the policy. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | The Request is not authorization. | The returned message. |
| Success | String | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 13356BCA-3EC3- 4748-A771- 2064DA69AEF1 | The request ID. |
| Result | Integer | 1 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateMonitorGroupNotifyPolicy &PolicyType=PauseNotify &GroupId=7301**** &StartTime=1622949300000 &EndTime=1623208500000 &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"13356BCA-3EC3-4748-A771-2064DA69AEF1",
 "Code":"200",
 "Success":"true",
 "Result":1
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.12 DeleteHostAvailability

Deletes availability monitoring tasks.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Repe atList | Query | Yes | 12456 | The task ID. Valid values of N: 1 to 20. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| RequestId | String | 57C782E6-B235- 4842-AD2B- DB94961761EB | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteHostAvailability &Id=12456 &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"57C782E6-B235-4842-AD2B-DB94961761EB",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.13 DescribeMonitorGroupCategories

Queries the cloud services to which the resources in an application group belong and the number of resources that belong to each cloud service in the application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| GroupId | Long | Quer y | Yes | 123456 | The ID of the application group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9E0347B0-EBC3- 4769-A78D- D96F21C6BB52 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |
| MonitorGroup Categories | Struct |   | The cloud services to which the resources in the application group belong and the number of resources that belong to the cloud service. |
| - MonitorGroup Category | Array |   | The cloud services to which the resources in the application group belong and the number of resources that belong to the cloud service. |
| --Category | String | ECS | The abbreviation of the cloud service name. For more information about how to query the abbreviations of cloud service names, see metricCategory in the response parameter Labels of the DescribeProjectMeta operation. |
| --Count | Integer | 1 | The number of resources that belong to the cloud service. |
| -GroupId | Long | 123456 | The ID of the application group. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMonitorGroupCategories &GroupId=123456 &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"9E0347B0-EBC3-4769-A78D-D96F21C6BB52",
 "MonitorGroupCategories":{
  "-MonitorGroupCategory":{
   "Category":"ECS",
   "Count":1
```

`},`

```json
  "GroupId":123456
```

`},`

```json
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.14 ModifyMonitorGroupInstances

Modifies the resources that are added to an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupId | Long | Query | Yes | 12345 | The ID of the application group. |
| Instances | Repe atList | Query | Yes | value | The instances. |
| -Category | Strin g |   | Yes | ECS | The name and specifications of the service to which the instance in the application group belongs. Valid values: ECS: Elastic Compute Service (ECS) instances provided by Alibaba Cloud and hosts not provided by Alibaba Cloud RDS: ApsaraDB RDS ADS: AnalyticDB SLB: Server Load Balancer (SLB) VPC: Virtual Private Cloud (VPC) APIGATEWAY: API Gateway CDN: Alibaba Cloud Content Delivery Network (CDN) CS: Container Service for Swarm DCDN: Dynamic Content Delivery Network (DCDN) DDoS: Anti-DDoS EIP: Elastic IP Address (EIP) ELASTICSEARCH: Elasticsearch EMR: E-MapReduce ESS: Auto Scaling HBASE: ApsaraDB for Hbase IOT EDGE: Link IoT _ Edge K8S POD: pods in _ Container Service for Kubernetes (ACK) KVSTORE SHARDING: _ ApsaraDB for Redis (cluster architecture) KVSTORE SPLITRW: _ ApsaraDB for Redis |

| Parame ter | Typ e | Locati on | Require d | Example | (read/write splitting Deasrcchriitpecttiuorne) KVSTORE STANDARD: _ |
|---|---|---|---|---|---|
|   |   |   |   |   | ApsaraDB for Redis (standard architecture) MEMCACHE: ApsaraDB for Memcache MNS: Message Service (MNS) MONGODB: ApsaraDB for MongoDB of the replica set architecture MONGODB CLUSTER: _ ApsaraDB for MongoDB of the cluster architecture MONGODB SHARDIN _ G: ApsaraDB for MongoDB of the sharded cluster architecture MQ TOPIC: MNS _ topics OCS: ApsaraDB for Memcache of earlier versions OPENSEARCH: OpenSearch OSS: Object Storage Service (OSS) POLARDB: PolarDB PETADATA: HybridDB for MySQL |
|   |   |   |   |   | SCDN: Secure CDN (SCDN) SHAREBANDWIDTHPA CKAGES: Internet Shared Bandwidth SLS: Simple Log Service VPN: VPN Gateway. Valid values of N: 1 to 2000. |
| - InstanceId | Strin g |   | Yes | i-a2d5q7pm12**** | The instance ID. Valid values of N: 1 to 2000. |
| -RegionId | Strin g |   | Yes | cn-hangzhou | The region ID. Valid values of N: 1 to 2000. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| - InstanceN ame | Strin g |   | Yes | HostName | The instance name. Valid values of N: 1 to 2000. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FEC7EDB3-9B08- 4AC0-A42A- 329F5D14B95A | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. true false |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyMonitorGroupInstances &GroupId=12345 &Instances=null &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"FEC7EDB3-9B08-4AC0-A42A-329F5D14B95A",
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | AccessForbidden | The X.509 certificate or cms access key ID provided does not exist in our records. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 412 | 4121 | ResourcesOverLimit | Resources over limit. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.15 ModifyHostAvailability

Modifies an availability monitoring task.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupId | Long | Query | Yes | 123456 | The ID of the application group. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Long | Query | Yes | 12345 | The ID of the availability monitoring task. |
| TaskName | Strin g | Query | Yes | task2 | The name of the availability monitoring task. |
| TaskScop e | Strin g | Query | No | GROUP | The range of the instances that are monitored by the availability monitoring task. Valid values: GROUP: All Elastic Compute Service (ECS) instances in the application group are monitored. GROUP SPEC INSTAN _ _ CE: Specified ECS instances in the application group are monitored. The TaskScope parameter must be used in combination with the InstanceList parameter. The InstanceList parameter specifies the ECS instances to be monitored. |
| TaskOptio n.HttpURI | Strin g | Query | No | https://www.aliyun.com | The URI that you want to monitor. This parameter is required if the TaskType parameter is set to HTTP. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TaskOptio n.TelnetOr PingHost | Strin g | Query | No | www.aliyun.com | The domain name or IP address that you want to monitor. This parameter is required if the TaskType parameter is set to PING or TELNET. For more information about how to set the TaskType parameter, see CreateHostAvailabil ity. |
| TaskOptio n.HttpRes ponseCha rset | Strin g | Query | No | UTF-8 | The character set that is used in the HTTP response. Valid value: UTF-8. |
| TaskOptio n.HttpRes ponseMat chContent | Strin g | Query | No | ok | The response to the HTTP request. |
| TaskOptio n.HttpMet hod | Strin g | Query | No | GET | The HTTP request method. Valid values: GET POST HEAD This parameter is required if the TaskType parameter is set to HTTP. For more information about how to set the TaskType parameter, see CreateHostAvailabil ity. |

| Parame ter | Typ e | Locati on | Require d |   | Example |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|
| TaskOptio n.HttpNeg ative | Boole an | Query | No |   | true |   | The method to trigger an alert. The alert can be triggered based on whether the specified alert rule is included in the response body. Valid values: true: If the HTTP response body includes the alert rule, an alert is triggered. false: If the HTTP response does not include the alert rule, an alert is triggered. This parameter is required if the TaskType parameter is set to HTTP. For more information about how to set the TaskType parameter, see CreateHostAvailabil ity. |   |   |
| TaskOptio n.Interval | Integ er | Query | No |   | 60 |   | The interval at which detection requests are sent. Unit: seconds. Valid values: 15, 30, 60, 120, 300, 900, 1800, and 3600. This parameter is available only for the CloudMonitor agent V3.5.1 or later. |   |   |
| TaskOptio n.HttpHea der | Strin g | Query | No |   |   |   | The header of the HTTP request. Format: Parameter name:Parameter value . Separate multiple parameters with carriage return characters. Example: params1:value1 params2:value2 |   |   |
|   |   |   |   |   |   |   |   | Parameter |   |
|   |   |   |   |   |   |   | name:Parameter |   |   |
|   |   |   |   |   |   |   | value |   |   |
|   |   |   |   |   | params1:value1 |   |   |   |   |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TaskOptio n.HttpPost Content | Strin g | Query | No | params1=value1 | The content of the HTTP POST request. |
| AlertConfi g.NotifyTy pe | Integ er | Query | Yes | 0 | The alert notification methods. Valid values: China site: 2: Alert notifications are sent by using phone calls, text messages, emails, and DingTalk chatbots. 1: Alert notifications are sent by using text messages, emails, and DingTalk chatbots. 0: Alert notifications are sent by using emails and DingTalk chatbots. International site: 0: Alert notifications are sent by using emails and DingTalk chatbots. Site for virtual network operators (VNOs): 0: Alert notifications are sent by using emails and DingTalk chatbots. |

| Parame ter | Typ e | Locati on | Require d | Example |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|
| AlertConfi g.StartTim e | Integ er | Query | No | 0 |   | The start of the time period during which the alert rule is effective. Valid values: 0 to 23. For example, if the AlertConfig.StartTim e parameter is set to 0 and the AlertConfig.EndTime parameter is set to 22, the alert rule is effective from 00:00:00 to 22:00:00. Alert notifications are sent based on the specified threshold only if the alert rule is effective. |   |   |
|   |   |   |   |   |   |   | AlertConfig.StartTim |   |
|   |   |   |   |   |   | e |   |   |
| AlertConfi g.EndTim e | Integ er | Query | No | 22 |   | The end of the time period during which the alert rule is effective. Valid values: 0 to 23. For example, if the AlertConfig.StartTim e parameter is set to 0 and the AlertConfig.EndTime parameter is set to 22, the alert rule is effective from 00:00:00 to 22:00:00. Alert notifications are sent based on the specified threshold only if the alert rule is effective. |   |   |
|   |   |   |   |   |   |   | AlertConfig.StartTim |   |
|   |   |   |   |   |   | e |   |   |
| AlertConfi g.SilenceT ime | Integ er | Query | No | 86400 |   | The mute period during which new alerts are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400, which indicates one day. |   |   |
| AlertConfi g.WebHoo k | Strin g | Query | No | https://www.aliyun.com/ webhook.json |   | The callback URL. |   |   |

|   |   | AlertConfig.EndTime |
|---|---|---|

|   |   | AlertConfig.EndTime |
|---|---|---|

|   | CloudMonitor |   |   |   | Dev | eloper Guide·API Referenc | e |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| AlertConfi gEscalatio nList | Repe atList | Query | Yes |   | The alert configurations. |
| - MetricNa me | Strin g |   | Yes | HttpStatus | The metric for which the alert feature is enabled. Valid values of N: 1 to 21. Valid values: HttpStatus: HTTP status code HttpLatency: HTTP response time TelnetStatus: Telnet status code TelnetLatency: Telnet response time PingLostRate: Ping packet loss rate |
| - Aggregate | Strin g |   | Yes | Value | The method used to calculate the metric values that trigger alerts. Valid values of N: 1 to 21. The value of this parameter varies based on the metric. The following items show the correspondence between metrics and calculation methods: HttpStatus: Value HttpLatency: Average TelnetStatus: Value TelnetLatency: Average PingLostRate: Average The value Value indicates the original value and is used for metrics such as status codes. The value Average indicates the average value and is used for metrics, such as the latency and packet loss rate. |

| Parame ter | Typ e | Locati on | Require d | Example |   | Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
| -Times | Integ er |   | Yes | 3 |   | The consecutive number of times for which the metric value meets the alert condition before an alert is triggered. Valid values of N: 1 to 21. |   |   |   |
| -Operator | Strin g |   | Yes | > |   | The comparison operator that is used in the alert rule. Valid values of N: 1 to 21. Valid values: > >= < <= = |   |   |   |
| -Value | Strin g |   | Yes | 3 |   | The alert threshold. Valid values of N: 1 to 21. |   |   |   |
| InstanceLi st | Repe atList | Query | No | i-absdfkwl321**** |   | The ECS instances that are monitored. Valid values of N: 1 to 21. This parameter is required if the TaskScope parameter is set to GROUP SPEC INST _ _ ANCE . |   |   |   |
|   |   |   |   |   |   |   |   | GROUP SPEC INST _ _ |   |
|   |   |   |   |   |   |   | ANCE |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | The specified resource is not found. | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 16E815A3-47E1- 4290-87F9- D5C99471FF45 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyHostAvailability &GroupId=123456 &Id=12345 &TaskName=task2 &AlertConfig.NotifyType=0 &AlertConfigEscalationList=null &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"16E815A3-47E1-4290-87F9-D5C99471FF45",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |

| Developer Gu | ide·API Reference |   | CloudMonito |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 409 | 4092 | ResourceExist | Resources already exist. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.16 PutMonitorGroupDynamicRule

Creates or modifies an alert rule to dynamically add instances that meet the rule to an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| GroupId | Long | Quer y | Yes | 123456 | The ID of the application group. |
| GroupRule s | Repe atLis t | Quer y | Yes | value | None. |
| -Category | Strin g |   | Yes | ecs | The cloud service to which the alert rule is applied. Valid values of N: 1 to 3. Valid values: ecs: Elastic Compute Service (ECS) rds: ApsaraDB RDS slb: Server Load Balancer (SLB) |

| - FilterRelati on | Strin g |   | Yes | and | The logical operator used between conditional expressions in the alert rule. Valid values of N: 1 to 3. Valid values: and: The instances that meet all the conditional expressions are automatically added to the application group. or: The instances that meet one of the conditional expressions are automatically added to the application group. |
|---|---|---|---|---|---|
| -Filters | Repe atLis t | Quer y | Yes |   | The filters. |
| --Name | Strin g |   | Yes | hostName | The name of the field based on which instances are filtered. Valid values of N: 1 to 3. Only hostnames are supported. Example: hostName. |
| --Function | Strin g |   | Yes | contains | The method that is used to filter instances. Valid values of N: 1 to 3. Valid values: contains: contains notContains: does not contain startWith: starts with a prefix endWith: ends with a suffix |
| --Value | Strin g |   | Yes | nginx | The value to be matched with the specified field. Valid values of N: 1 to 3. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | 3E73F1AB-D195- 438A-BCA7- 2F4355789C58 | The request ID. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutMonitorGroupDynamicRule &GroupId=123456 &GroupRules=null &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"3E73F1AB-D195-438A-BCA7-2F4355789C58",
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |

| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
|---|---|---|---|
| 403 | 403 | AccessForbidden | The X.509 certificate or cms access key ID provided does not exist in our records. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 206 | 206 | 206 | 206 |
| 503 | 503 | 503 | 503 |
| 412 | 4121 | OverLimit | Matched instances count was over limit |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.17 ModifyMonitorGroup

Modifies an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupId | Strin g | Query | Yes | 123456 | The ID of the application group. |

| Developer Gui | de·API R | eference |   |   | CloudMonito |
|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupNa me | Strin g | Query | No | ecs group _ | The name of the application group. |
| Type | Strin g | Query | No | value | The type. |
| ContactGr oups | Strin g | Query | No | alarm ecs group _ _ | The alert contact group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C85A2870-5DF4- 4269-BC50- ECB5E4591A80 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyMonitorGroup &GroupId=123456 &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"C85A2870-5DF4-4269-BC50-ECB5E4591A80",
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 409 | 4092 | ResourceExist | Resources already exist. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.18 DeleteMonitorGroupDynamicRule

Deletes a rule that is used to dynamically add the instances of a service to an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupId | Long | Query | Yes | 123456 | The ID of the application group. |
| Category | Strin g | Query | Yes | ecs | The service to which the rule applies. Valid values: ecs, rds, and slb. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 56B4516A-EB44- 4C66-8854- 0393B35F636B | The request ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMonitorGroupDynamicRule &GroupId=123456 &Category=ecs &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"success",
 "RequestId":"56B4516A-EB44-4C66-8854-0393B35F636B",
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | AccessForbidden | The X.509 certificate or cms access key ID provided does not exist in our records. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

| CloudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.19 DeleteMonitorGroupNotifyPolicy

Deletes a policy that is used to pause alert notifications for an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| PolicyTyp e | Strin g | Query | Yes | PauseNotify | The policy type. Valid value: PauseNotify. |
| GroupId | Strin g | Query | No | 6780**** | The ID of the application group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The returned message. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | String | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | B7AF834D-D38B- 4A46-920B- FE974EB7E135 | The request ID. |
| Result | Integer | 1 | The number of affected rows. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMonitorGroupNotifyPolicy &PolicyType=PauseNotify &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"B7AF834D-D38B-4A46-920B-FE974EB7E135",
 "Code":"200",
 "Success":"true",
 "Result":1
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.20 DescribeMonitorGroupNotifyPolicyList

Queries the policies that are used to pause alert notifications for an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| PolicyTyp e | Strin g | Query | Yes | PauseNotify | The policy type. Valid value: PauseNotify. |
| PageNum ber | Integ er | Query | No | 1 | The page number. Default value: 1. |
| PageSize | Integ er | Query | No | 100 | The number of entries per page. Default value: 10. |
| GroupId | Strin g | Query | No | 6780**** | The ID of the application group. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| NotifyPolicyLis t | Array |   | The returned policies. |
| -Type | String | PauseNotify | The policy type. |
| -Id | String | 123**** | The policy ID. |
| -StartTime | Long | 1551761781273 | The start of the time range to query. Unit: milliseconds. |
| -EndTime | Long | 1551761781273 | The end of the time range to query. Unit: milliseconds. |
| -GroupId | String | 6780**** | The ID of the application group. |

| Parameter | Type | Examples | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The returned message. |
| Success | String | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 6072F026-C441- 41A6-B114- 35A1E8F8FDD3 | The request ID. |
| Total | Integer | 11 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMonitorGroupNotifyPolicyList &PolicyType=PauseNotify &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "NotifyPolicyList":{
  "Type":"PauseNotify",
  "EndTime":1551761781273,
  "StartTime":1551761781273,
  "Id":"123****",
  "GroupId":"6780****"
```

`},`

```json
 "Message":"The Request is not authorization.",
 "RequestId":"6072F026-C441-41A6-B114-35A1E8F8FDD3",
 "Total":11,
 "Code":"200",
 "Success":"true"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | InvalidAuthorization | Permission denied |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.8.21 DescribeMonitorGroupDynamicRules

Queries the dynamic rules of an application group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| GroupId | Long | Quer y | Yes | 123456 | The ID of the application group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Resource | Array | 12345 | The resources that are associated with the application group. |
| -Filters | Array | [{"Key":"KeyState" }] | The dynamic rules of the application group. |
| --Function | String | all | The function. |

| --Name | String | key1 | The key. |
|---|---|---|---|
| --Value | String | value1 | The value. |
| -GroupId | Long | 12345 | The ID of the application group. |
| -Category | String | ecs | The type of the cloud service to which the dynamic rule belongs. Valid values: ecs: Elastic Compute Service (ECS) rds: ApsaraDB RDS slb: Server Load Balancer (SLB) |
| -FilterRelation | String | and | The filter condition. Valid values: and: queries the instances that meet all alert rules. or: queries the instances that meet any alert rule. |
| RequestId | String | 2170B94A-1576- 4D65-900E- 2093037CDAF3 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | Integer | 200 | The HTTP status code. Note The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The error message. |
| PageNumber | Integer | 1 | The page number. |

| PageSize | Integer | 2 | The number of entries per page. |
|---|---|---|---|
| Total | Integer | 10 | The total number of entries. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMonitorGroupDynamicRules &GroupId=123456 &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The specified resource is not found.",
 "RequestId":"2170B94A-1576-4D65-900E-2093037CDAF3",
 "Resource":[
```

`{`

```json
   "Filters":[
```

`{`

```json
     "Function":"",
     "Value":"",
     "Name":""
```

`}` `],`

```json
   "FilterRelation":"and",
   "Category":"ecs"
```

`}` `],`

```json
 "Code":200,
 "Success":true
```

`}`

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | AccessForbidden | The X.509 certificate or cms access key ID provided does not exist in our records. |

| 404 | 404 | ResourceNotFound | The specified resource is not found. |
|---|---|---|---|
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |

Cms 2019-01-01

### 2.9 Site monitoring

#### 2.9.1 DescribeSiteMonitorData

Queries the fine-grained monitoring data of a site monitoring task.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TaskId | Strin g | Query | Yes | 49f7b317-7645-4cc9- 94fd-ea42e522**** | The task ID. |
| Type | Strin g | Query | No | metric | The type of the monitored object whose monitoring data is to be queried. Valid values: metric event |
| MetricNa me | Strin g | Query | Yes | Availability | The metric name. Valid values: Availability ResponseTime |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| StartTime | Strin g | Query | No | 1551579637000 | The start of the time range to query. The following formats are supported: UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970. UTC time: the UTC time that follows the YYYY-MM- DDThh:mm:ssZ format. |
| EndTime | Strin g | Query | No | 1551581437000 | The end of the time range to query. Valid values: UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970. UTC time: the UTC time that follows the YYYY-MM- DDThh:mm:ssZ format. |
| Period | Strin g | Query | No | 60 | The statistical period. The value is an integral multiple of 60. Unit: seconds. The default value equals the minimum interval at which detection requests are sent to the monitored address. |
| NextToke n | Strin g | Query | No | 49f7b317-7645-4cc9- 94fd- ea42e5220930ea42e52 20930ea42e522**** | The pagination token. |
| Length | Integ er | Query | No | 1000 | The number of data points to return. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | Successful | The returned message. |
| Success | String | true | Indicates whether the request was successful. Valid values: true and false. |
| RequestId | String | 3febb181-0d98- 4af9-8b04- 7faf36b048b9 | The request ID. |
| Data | String | [{"Maximum":247, "Mimimum":61,"Av erage":154,"userId ":"127067667954* ***","taskId":"49f7b 317-7645-4cc9- 94fd- ea42e522****","ti mestamp":155158 1760000}] | The monitoring data. |
| NextToken | String | ea42e5220930ea4 2e522**** | The pagination token. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSiteMonitorData &TaskId=49f7b317-7645-4cc9-94fd-ea42e522**** &MetricName=Availability &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "NextToken":"ea42e5220930ea42e522****",
 "RequestId":"3febb181-0d98-4af9-8b04-7faf36b048b9",
 "Message":"Successful",
 "Data":"
[{\"Maximum\":247,\"Mimimum\":61,\"Average\":154,\"userId\":\"127067667954****\",\"taskId :\"49f7b317-7645-4cc9-94fd-ea42e522****\",\"timestamp\":1551581760000}]",
 "Code":"200",
 "Success":"true"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | Forbidden | You are not authorized to operate the specified resource. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.9.2 DescribeSiteMonitorStatistics

Queries the statistics of a specified metric for a specified site monitoring task.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TaskId | Strin g | Query | Yes | ef4cdc8b-9dc7-43e7- 810e-f950e56c**** | The ID of the site monitoring task. For more information about how to query the IDs of site monitoring tasks, see DescribeSiteMonitorList. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TimeRang e | Strin g | Query | No | 1440 | The statistical period. Unit: minutes. Default value: 1440 (one day). Maximum value: 43200 (30 days). |
| StartTime | Strin g | Query | No | 1576142850527 | The start of the time range to query. Unit: milliseconds. The default value is 1 hour ahead of the current time. |
| MetricNa me | Strin g | Query | Yes | Availability | The metric name. Valid values: Availability ErrorRate ResponseTime |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | Successful | The returned message. |
| Success | String | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 3AD2724D-E317- 4BFB-B422- D6691D071BE1 | The request ID. |
| Data | Long | 100 | The statistics. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSiteMonitorStatistics &TaskId=ef4cdc8b-9dc7-43e7-810e-f950e56c**** &MetricName=Availability &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"Successful",
 "RequestId":"3AD2724D-E317-4BFB-B422-D6691D071BE1",
 "Data":100,
 "Code":"200",
 "Success":"true"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | 403 | Forbidden | You are not authorized to operate the specified resource. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.9.3 DescribeSiteMonitorList

Queries site monitoring tasks.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TaskId | Strin g | Query | No | a1ecd34a-8157-44d9- b060-14950837**** | The ID of the site monitoring task. |
| TaskType | Strin g | Query | No | HTTP | The protocol that is used by the site monitoring task. Valid values: HTTP, PING, TCP, UDP, DNS, SMTP, POP3, and FTP. |
| Keyword | Strin g | Query | No | site | The keyword to be matched. You can search for tasks by name or address. Fuzzy search is supported. |
| Page | Integ er | Query | No | 1 | The page number. Default value: 1. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. Default value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| SiteMonitors | Array |   | The site monitoring tasks. |
| -TaskId | String | f5783760-1b39- 4b6b-80e8- 453d962a**** | The ID of the site monitoring task. |
| -TaskType | String | TCP | The protocol that is used by the site monitoring task. Valid values: HTTP, PING, TCP, UDP, DNS, SMTP, POP3, and FTP. |
| -Address | String | https://aliyun.com | The URL or IP address that is monitored by the site monitoring task. |
| -TaskState | String | 1 | The task status. Valid values: 1: The task is enabled. 2: The task is disabled. |

| loudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -CreateTime | String | 2021-11-01 11:05:18 | The time when the site monitoring task was created. |
| -TaskName | String | New site monitoring task | The name of the site monitoring task. |
| -Interval | String | 1 | The interval at which detection requests are sent. Unit: minutes |
| -UpdateTime | String | 2022-03-08 17:14:31 | The time when the site monitoring task was updated. |
| -OptionsJson | Json |   | The extended options of the site monitoring task. The options vary based on the specified protocol. For more information, see CreateSiteMonitor. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | successful | The returned message. |
| Success | String | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | A80DB41C-AF6C- 50E1-ADB5- 66DCBA3D266B | The request ID. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| TotalCount | Integer | 1 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSiteMonitorList &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "TotalCount":1,
 "RequestId":"A80DB41C-AF6C-50E1-ADB5-66DCBA3D266B",
 "Message":"successful",
 "PageSize":10,
 "PageNumber":1,
 "Code":"200",
 "Success":"true",
 "SiteMonitors":{
  "TaskId":"f5783760-1b39-4b6b-80e8-453d962a****",
  "Address":"https://aliyun.com",
  "TaskName":"New site monitoring task",
  "OptionsJson":null,
  "TaskType":"TCP",
  "CreateTime":"2021-11-01 11:05:18",
  "UpdateTime":"2022-03-08 17:14:31",
  "TaskState":"1",
  "Interval":"1"
```

`}` `}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | Forbidden | You are not authorized to operate the specified resource. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.9.4 DescribeSiteMonitorISPCityList

Queries the detection points that are provided by carriers.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Isp | Strin g | Query | No | China Unicom | The name or ID of the carrier. Carrier names support fuzzy match. |
| City | Strin g | Query | No | Guiyang | The name or ID of the city. City names support fuzzy match. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| IspCityList | Array |   | The queried detection points. |
| -Isp | String | 232 | The carrier ID. |
| -City | String | 4 | The city ID. |
| - IspName.zh C _ N | String | China Unicom | The carrier name. This parameter is valid only on the China site (aliyun.com). |
| - CityName.zh _ CN | String | Guiyang | The city name. This parameter is valid only on the China site (aliyun.com). |
| -Region.zh CN _ | String | Guizhou | The province name. This parameter is valid only on the China site (aliyun.com). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - Country.zh CN _ | String | China | The country name. This parameter is valid only on the China site (aliyun.com). |
| -IspName.en | String | China-Unicom | The carrier name. |
| -CityName.en | String | Guiyang | The city name. |
| -Region.zh CN _ | String | Guizhou | The province name. This parameter is valid only on the China site (aliyun.com). |
| - Country.zh CN _ | String | China | The country name. This parameter is valid only on the China site (aliyun.com). |
| -Region.en | String | Guizhou | The province name. |
| -Country.en | String | China | The country name. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | successful | The returned message. |
| Success | String | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | B35D7D84-547B- 4E61-B909- 48A1F8A0C756 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSiteMonitorISPCityList &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"successful",
 "RequestId":"B35D7D84-547B-4E61-B909-48A1F8A0C756",
 "Code":"200",
 "Success":"true",
 "IspCityList":{
  "Country.zh_CN":"China",
  "Region.zh_CN":"Guizhou",
  "CityName.en":"Guiyang",
  "Isp":"232",
  "City":"4",
  "IspName.en":"China-Unicom",
  "IspName.zh_CN":"China Unicom",
  "Region.en":"Guizhou",
  "Country.en":"China",
  "CityName.zh_CN":"Guiyang",
```

`}` `}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.9.5 CreateSiteMonitor

Creates a site monitoring task.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Address | Strin g | Query | Yes | https://www.aliyun.com | The URL or IP address that is monitored by the task. |

|   | Parame ter |   | Typ e |   | Locati on | Require d |   | Example |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | TaskType |   | Strin g |   | Query | Yes |   | HTTP |   | The protocol that is used by the site monitoring task. Valid values: HTTP, HTTPS, PING, TCP, UDP, DNS, SMTP, POP3, and FTP. |   |   |
|   | TaskName |   | Strin g |   | Query | Yes |   | HanZhou ECS1 _ |   | The name of the site monitoring task. The name must be 4 to 100 characters in length, and can contain letters, digits, and underscores ( ). _ |   |   |
|   | Interval |   | Strin g |   | Query | No |   | 1 |   | The interval at which detection requests are sent. Valid values: 1, 5, 15, 30, and 60. Unit: minutes. Default value: 1. |   |   |
|   | IspCities |   | Strin g |   |   |   |   | [{"city":"546","isp":"465" }, |   | The information of the detection points. If you leave this parameter empty, the system randomly selects three detection points. The value is a JSON array. Example: [{"city":"546","isp" |   |   |
|   |   |   |   |   |   |   |   |   |   |   | [{"city":"546","isp" |   |
|   |   |   |   |   |   |   |   |   | city":"546","isp":"465" | :"465"}, |   |   |
|   |   |   |   |   |   |   |   | {"city":"572","isp":"465" |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | {"city":"572","isp":" |   |   |
|   |   |   |   |   | Query | No |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | }, |   | 465"}, |   |   |
|   |   |   |   |   |   |   |   | {"city":"738","isp":"465" |   | {"city":"738","isp":" |   |   |
|   |   |   |   |   |   |   |   | }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | 465"}] |   |   |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| OptionsJso n | Strin g | Query | No | {"time out":5000} _ | The extended options of the protocol that is used by the site monitoring task. The options vary based on the protocol. |
| AlertIds | Strin g | Query | No | SystemDefault acs ecs _ _ _ dashboard InternetOutR _ ate Percent _ | The ID of the alert rule. For more information about how to query the IDs of the existing alert rules in CloudMonitor, see DescribeMetricRuleList. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | Successful | The returned message. |
| Success | String | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 68192f5d-0d45- 4b98-9724- 892813f86c71 | The request ID. |
| AlertRule | String |   | The alert rule. |
| Data | Struct | value | The result of the site monitoring task. |
| - AttachAlertRes ult | Array |   | The result that is returned after you associate the existing alert rule with the site monitoring task. |
| --Message | String | successful | The message that is returned after you associate the existing alert rule with the site monitoring task. |

| Developer Guide·A | PI Reference |   | CloudMonito |
|---|---|---|---|
| Parameter | Type | Example | Description |

| --RequestId | String | 5dd33455-4f65- 4b0c-9200- 33d66f3f340b | The ID of the request that was sent to associate the existing alert rule with the site monitoring task. |
|---|---|---|---|
| --Code | String | 200 | The status code that is returned after you associate the existing alert rule with the site monitoring task. The status code 200 indicates that the request was successful. |
| --Success | String | true | Indicates whether the existing alert rule was associated with the site monitoring task. Valid values: true false |
| --RuleId | String | SystemDefault acs _ ecs dashboard Int _ _ _ ernetOutRate Perc _ ent | The ID of the alert rule. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateSiteMonitor &Address=https://www.aliyun.com &TaskType=HTTP &TaskName=HanZhou_ECS1 &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"Successful",
 "RequestId":"68192f5d-0d45-4b98-9724-892813f86c71",
 "Data":{
  "-AttachAlertResult":{
   "Message":"successful",
   "RequestId":"5dd33455-4f65-4b0c-9200-33d66f3f340b",
   "RuleId":"SystemDefault_acs_ecs_dashboard_InternetOutRate_Percent",
   "Code":"200",
   "Success":"true"
```

`}` `},`

```json
 "Code":"200",
 "Success":"true",
 "AlertRule":""
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | Forbidden | You are not authorized to operate the specified resource. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 600 | 600 | IllegalAddress | Illegal HTTP address |
| 605 | 605 | OperationError | Operation failed |
| 615 | 615 | TaskNotExists | Task does not exist |
| 650 | 650 | OperatorCityInvalid | Operator City invalid |
| 655 | 655 | OperatorCityInvalid | Operator City invalid |
| 660 | 660 | NameRepeat | Task name repeat |
| 680 | 680 | CreateAlarmError | Create alarm error |

| Developer Gui | de·API Reference |   | CloudMonito |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 695 | 695 | NameNotExists | Task name not exists |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.9.6 DescribeSiteMonitorAttribute

Queries the details of a site monitoring task.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TaskId | Strin g | Query | Yes | cc641dff-c19d-45f3- ad0a-818a0c4f**** | The ID of the site monitoring task. |
| IncludeAle rt | Boole an | Query | No | false | Specifies whether to return the information of the alert rules that are configured for the site monitoring task. Valid values: true: The system returns the information of the alert rules that are configured for the site monitoring task. false (default): The system does not return the information of the alert rules that are configured for the site monitoring task. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| MetricRules | Array | value | The information of the alert rules that are configured for the site monitoring task. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -RuleId | String | bf071ae 7b7aec38 _ 17b0fdf**** | The ID of the alert rule. |
| -RuleName | String | rule1 | The name of the alert rule. |
| -Namespace | String | acs networkmonito _ r | The namespace of the cloud service. |
| -MetricName | String | Availability | The metric name. |
| -OkActions | String | [ "CloudMonitor"] | The alert contact group that receives alert notifications. |
| -AlarmActions | String | CloudMonitor | The alert contact group to which alert notifications are sent. |
| -Statistics | String | Availability | The statistical method of the alert rule. Valid values: Availability: the percentage of available detection points AvailableNumber: the number of available detection points ErrorCodeMaximum: a status code for an alert ErrorCodeMinimum: all status codes for a set of alerts Average: response time |
| -ActionEnable | String | true | Indicates whether the alert rule is enabled. Valid values: true: The alert rule is enabled. false: The alert rule is disabled. |
| -Period | String | 15s | The time interval. The value is the same as the interval at which metric data is reported. Unit: seconds. If you specify a statistical period for the alert rule, data is queried based on the statistical period. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - ComparisonOp erator | String | GreaterThanYester day | The operator that is used to compare the metric value with the threshold in the alert rule. Valid values: >= > <= < = != GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
| -Threshold | String | 30 | The alert threshold. |
| - EvaluationCou nt | String | 3 | The consecutive number of times for which the metric value meets the alert condition before an alert is triggered. |
| -Level | String | 2 | The alert severity. Valid values: 1: critical 2: warning 3: information |
| -Expression | String | $Availability=30 | The expression that is used to trigger alerts. |
| -StateValue | String | OK | The alert status. Valid values: OK: The alert rule has no active alerts. ALARM: The alert rule has active alerts. |
| -Dimensions | String | [{"taskId": "cc641dff-c19d- 45f3-ad0a- 818a0c4f****" }] | The dimension of the alert rule. |

| loudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | successful | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | D17DF650-7EBD- 54D0-903A- 1D4E624D7402 | The request ID. |
| SiteMonitors | Struct |   | The details of the site monitoring task. |
| -IspCities | Array |   | The information of detection points. The information includes the carriers that provide the detection points and the cities where the detection points reside. |
| --CityName | String | Beijing | The city name. |
| --IspName | String | Alibaba Group | The carrier name. |
| --City | String | 738 | The city ID. |
| --Isp | String | 465 | The carrier ID. |
| -TaskType | String | HTTP | The protocol that is used by the site monitoring task. Valid values: HTTP, HTTPS, PING, TCP, UDP, DNS, SMTP, POP3, and FTP. |
| -Address | String | https://aliyun.com | The URL that is monitored by the site monitoring task. |
| -TaskState | String | 1 | The status of the site monitoring task. Valid values: 1: The task is enabled. 2: The task is disabled. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -TaskName | String | test123 | The name of the site monitoring task. |
| -Interval | String | 1 | The interval at which the site monitoring task is executed. Unit: minutes. Valid values: 1, 5, 15, 30, and 60. |
| -TaskId | String | cc641dff-c19d- 45f3-ad0a- 818a0c4f**** | The ID of the site monitoring task. |
| -OptionJson | Json |   | The extended options of the site monitoring task. The options vary based on the specified protocol. For more information, see CreateSiteMonitor. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSiteMonitorAttribute &TaskId=cc641dff-c19d-45f3-ad0a-818a0c4f**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "MetricRules":{
  "ComparisonOperator":"GreaterThanYesterday",
  "RuleId":"bf071ae_7b7aec3817b0fdf****",
  "Period":"15s",
  "EvaluationCount":"3",
  "Dimensions":"[{\"taskId\": \"cc641dff-c19d-45f3-ad0a-818a0c4f****\" }]",
  "Statistics":"Availability",
  "Namespace":"acs_networkmonitor",
  "AlarmActions":"CloudMonitor",
  "MetricName":"Availability",
  "OkActions":"[ \"CloudMonitor\"]",
  "Expression":"$Availability=30",
  "ActionEnable":"true",
  "StateValue":"OK",
  "Level":"2",
  "RuleName":"rule1",
  "Threshold":"30"
```

`},`

```json
 "Message":"successful",
 "RequestId":"D17DF650-7EBD-54D0-903A-1D4E624D7402",
 "Code":"200",
 "Success":true,
 "SiteMonitors":{
  "OptionJson":"",
  "-IspCities":{
   "IspName":"Alibaba Cloud",
   "Isp":"465",
   "CityName":"Beijing",
   "City":"738"
```

`},`

```json
  "TaskId":"cc641dff-c19d-45f3-ad0a-818a0c4f****",
  "Address":"https://aliyun.com",
  "TaskName":"test123",
  "TaskType":"HTTP",
  "TaskState":"1",
  "Interval":"1"
```

`}` `}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |

|   | Developer Gu | ide·API Reference |   | CloudMonito | r |
|---|---|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | 403 | Forbidden | You are not authorized to operate the specified resource. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 615 | 615 | Forbidden | Task Id does not exist |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.9.7 DisableSiteMonitors

Disables site monitoring tasks.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TaskIds | Strin g | Query | Yes | 49f7b317-7645-4cc9- 94fd- ea42e522****,49f7b317- 7645-4cc9-94fd- ea42e522**** | The ID of the site monitoring task. Separate multiple IDs with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | successful | The returned message. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | String | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 3fcd12e7-d387- 42ee-b77e- 661c775bb17f | The request ID. |
| Data | String | value | The number of detection points that are affected by the site monitoring tasks. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DisableSiteMonitors &TaskIds=49f7b317-7645-4cc9-94fd-ea42e522****,49f7b317-7645-4cc9-94fd-ea42e522**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"successful",
 "RequestId":"3fcd12e7-d387-42ee-b77e-661c775bb17f",
 "Data":null,
 "Code":"200",
 "Success":"true"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | Forbidden | You are not authorized to operate the specified resource. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |

| Developer Gu | ide·API Reference |   | CloudMonito |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.9.8 EnableSiteMonitors

Enables site monitoring tasks.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TaskIds | Strin g | Query | Yes | 49f7b317-7645-4cc9- 94fd- ea42e522****,49f7b317- 7645-4cc9-94fd- ea42e522**** | The ID of the site monitoring task. Separate multiple IDs with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | successful | The returned message. |
| Success | String | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 3fcd12e7-d387- 42ee-b77e- 661c775bb17f | The request ID. |

| CloudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | value | The number of detection points that are affected by the site monitoring tasks. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableSiteMonitors &TaskIds=49f7b317-7645-4cc9-94fd-ea42e522****,49f7b317-7645-4cc9-94fd-ea42e522**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"successful",
 "RequestId":"3fcd12e7-d387-42ee-b77e-661c775bb17f",
 "Data":null,
 "Code":"200",
 "Success":"true"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | Forbidden | You are not authorized to operate the specified resource. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.9.9 DeleteSiteMonitors

Deletes site monitoring tasks.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| TaskIds | Strin g | Query | Yes | 01adacc2-ece5-41b6- afa2- 3143ab5d****,43bd1ead -514f-4524-813e- 228ce091**** | The IDs of the site monitoring tasks that you want to delete. Separate multiple task IDs with commas (,). |
| IsDeleteAl arms | Boole an | Query | No | true | Specifies whether to delete the alert rules configured for the site monitoring tasks. Valid values: true (default) false |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | Success | The returned message. If the request was successful, "successful" is returned. If the request failed, an error message such as TaskId not found is returned. |
| Success | String | true | Indicates whether the request was successful. Valid values: true and false. |
| RequestId | String | 123BCC5D-8B63- 48EA-B747- 9A8995BE7AA6 | The request ID. |
| Data | String | value | The information about the site monitoring tasks that were deleted. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteSiteMonitors &TaskIds=01adacc2-ece5-41b6-afa2-3143ab5d****,43bd1ead-514f-4524-813e-228ce091**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"Success",
 "RequestId":"123BCC5D-8B63-48EA-B747-9A8995BE7AA6",
 "Data":null,
 "Code":"200",
 "Success":"true"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | Forbidden | You are not authorized to operate the specified resource. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.9.10 ModifySiteMonitor

Modifies a site monitoring task.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Address | Strin g | Query | No | http://www.aliyun.com | The URL or IP address that is monitored by the task. |
| TaskId | Strin g | Query | Yes | 2c8dbdf9-a3ab-46a1- 85a4-f094965e**** | The ID of the site monitoring task. |
| TaskName | Strin g | Query | No | HanZhou ECS2 _ | The name of the site monitoring task. The name must be 4 to 100 characters in length, and can contain letters, digits, and underscores ( ). _ |
| Interval | Strin g | Query | No | 1 | The interval at which detection requests are sent. Valid values: 1, 5, and 15. Unit: minutes. Default value: 1. |

|   | Parame ter |   | Typ e |   | Locati on | Require d |   | Example |   | Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   | The information of the detection points. The value is a JSON array. Example: [{"city":"546","isp" |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | [{"city":"546","isp" |   |   |
|   |   |   |   |   |   |   |   |   |   | :"465"}, |   |   |   |
|   |   |   |   |   |   |   |   |   |   | {"city":"572","isp":" |   |   |   |
|   |   |   |   |   |   |   |   |   |   | 465"}, |   |   |   |
|   |   |   |   |   |   |   |   |   |   | {"city":"738","isp":" |   |   |   |
|   |   |   |   |   |   |   |   |   |   | 465"}] |   |   |   |
|   | IspCities |   | Strin g |   | Query | No |   | [{"city":"546","isp":"465" }, {"city":"572","isp":"465" }, {"city":"738","isp":"465" }] |   |   |   |   |   |
|   | OptionsJso n |   | Strin g |   | Query | No |   | {"time out":5000} _ |   | The extended options of the protocol that is used by the site monitoring task. The options vary based on the protocol. |   |   |   |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| AlertIds | Strin g | Query | No | 49f7c317-7645-4cc9- 94fd-ea42e122**** | The ID of the alert rule. You can call the DescribeMetricRuleList operation to query the IDs of the existing alert rules in CloudMonitor. For more information, see DescribeMetricRuleList. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | successful | The returned message. |
| Success | String | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 68192f5d-0d45- 4b98-9724- 892813f86c71 | The request ID. |
| Data | String | value | The result of modifying the task. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifySiteMonitor &TaskId=2c8dbdf9-a3ab-46a1-85a4-f094965e**** &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"successful",
 "RequestId":"68192f5d-0d45-4b98-9724-892813f86c71",
 "Data":null,
 "Code":"200",
 "Success":"true"
```

`}`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | Forbidden | You are not authorized to operate the specified resource. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 600 | 600 | IllegalAddress | Illegal HTTP address |
| 605 | 605 | OperationError | Operation failed |
| 615 | 615 | TaskNotExists | Task does not exist |
| 650 | 650 | OperatorInvalid | Operator invalid |
| 650 | 650 | OperatorCityInvalid | Operator City invalid |
| 655 | 655 | OperatorCityInvalid | Operator City invalid |
| 660 | 660 | NameRepeat | Task name repeat |
| 680 | 680 | CreateAlarmError | Create alarm error |
| 695 | 695 | NameNotExists | Task name not exists |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.9.11 DescribeSiteMonitorQuota

Queries the quotas and version of site monitoring.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the request was successful. |
| Message | String | Success | The returned message. |
| Success | String | true | Indicates whether the request was successful. Valid values: true false |
| RequestId | String | 26860260-76C6- 404E-AB7A- EB98D36A6885 | The request ID. |
| Data | Struct | value | The quotas. |
| - SiteMonitorIdc Quota | Integer | 5 | The quota of detection points that are provided by Alibaba Cloud. Five detection points are provided for free. |
| - SiteMonitorOp eratorQuotaQu ota | Integer | 0 | The quota of detection points that are not provided by Alibaba Cloud. Default value: 0. |
| - SiteMonitorTas kQuota | Integer | 10 | The quota of site monitoring tasks. |
| - SiteMonitorQu otaTaskUsed | Integer | 6 | The used quota of site monitoring tasks. |

| - SiteMonitorVer sion | String | V1 | The version of site monitoring. Valid values: V1 V2 |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSiteMonitorQuota
```

Sample success responses `JSON` format `{`

```json
 "Message":"Success",
 "RequestId":"26860260-76C6-404E-AB7A-EB98D36A6885",
 "Data":{
  "SiteMonitorVersion":"V1",
  "SecondMonitor":false,
  "SiteMonitorQuotaTaskUsed":6,
  "SiteMonitorOperatorQuotaQuota":0,
  "SiteMonitorTaskQuota":10,
  "SiteMonitorIdcQuota":5
```

`},`

```json
 "Code":"200",
 "Success":"true"
```

`}`

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | Forbidden | You are not authorized to operate the specified resource. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |

| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
|---|---|---|---|
| 500 | DEFAULT | InternalError | The request processing has failed due to some unknown error. |

Cms 2019-01-01

### 2.10 Alert center

#### 2.10.1 DescribeBatchDetectTaskWithAlertResult

Queries the list of alert results for a batch detection task.
**Throttle description**: The system applies a default throttle limit of 10,000 requests per
second at the API level and 50 requests per second at the user level.
**Protocol support**: The API supports HTTP and HTTPS protocols with a timeout of 5,000
milliseconds.
**Request methods**: The API supports the GET or POST method.
**Prerequisites**: You must have read-only or higher permissions for the Cloud Monitor (CMS)
service.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Integ er | Quer y | No | 123456 | The ID of the department, which is the organization ID. |
| AcceptLan guage | Strin g | Quer y | Yes | zh-CN | The language type of the response content. Valid values: zh-CN (Chinese) and en-US (English) |

| PageNumb er | Integ er | Quer y | No | 1 | The page number for paginated queries. The value starts from 1. Default value: 1 |
|---|---|---|---|---|---|
| AppKey | Strin g | Quer y | No | your app key _ _ | The unique ID of the application. |
| PageSize | Integ er | Quer y | No | 10 | The number of records to display per page in paginated queries. Valid values: 1 to 100. Default value: 10 |

`PageNumber` and `PageSize` work together to implement pagination. We recommend that you set appropriate values to avoid excessively large data volumes in a single query. `AcceptLanguage` is a required parameter. The API returns an error if you do not specify this parameter.

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4C467B38-391A- 5B8B-AF9A- 1D3F3D3D3D3D | The unique ID of the request for troubleshooting. |
| Success | Boolean | true | Indicates whether the request is successful. A value of true indicates success, and a value of false indicates failure. |
|   |   | [ { "targetInstanceId": "", "cloudProductType ": "acs rocketmq das _ _ hboard", "userId": "1871****1297", "resultType": "OK" }, { "targetInstanceId": "", "cloudProductType ": "acs maxcompute" _ , "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "r-6adf****4b74", |   |

|   |   | "cloudProductType ": "acs kvstore", _ "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", |   |
|---|---|---|---|
|   |   | "targetInstanceId": "r-6ade****5604", "cloudProductType ": "acs kvstore", _ "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "r-6ad4****4184", "cloudProductType ": "acs kvstore", _ "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "r-6adf****c5f4", "cloudProductType ": "acs kvstore", _ "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "r-6ada****5284", "cloudProductType ": "acs kvstore", _ "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "r-6ada****c094", "cloudProductType ": "acs kvstore", _ "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "r-6ade****6224", "cloudProductType ": "acs kvstore", _ "appKey": "2", "userId": "1871****1297", "resultType": "OK" |   |

|   |   | }, { "orgFullId": "0.1.3", "targetInstanceId": "r-6ad3****86a4", "cloudProductType ": "acs kvstore", _ "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "targetInstanceId": "", "cloudProductType ": "acs dataworks da _ _ shboard", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "pc-6ad6****04zo", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "pc-6ad7****5ntk", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "pc-6adr****dr57", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "pc-6ad6****652v", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": |   |
|---|---|---|---|

|   |   | "pc-6adu****ll62", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "pc-6ado****dsoc", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "pc-6adt****y6b9", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "pc- 6adn****7899", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "pc- 6adm****877n", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "pc-6ad8****92sp", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": |   |
|---|---|---|---|

| Resources | String | "0.1.3", "targetInstanceId": "pc- 6adq****0580", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "pc-6ad6****l1dk", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "pc-6ad1****spo1", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "pc-6ad1****1ir8", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "pc-6adb****j1r0", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "pc-6ad7****jzhl", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" | The list of alert results in a JSON format string. You must parse the string before you use it. |
|---|---|---|---|

|   |   | }, { "orgFullId": "0.1.3", "targetInstanceId": "pc-6adf****04d5", "cloudProductType ": "acs polardb dash _ _ board", "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "vpc- 6ad7****rp85", "cloudProductType ": "acs vpc", _ "appKey": "2", "resultType": "NO TASK", _ "taskBizType": "vpc2VpcPing", "errorMsg": "maybe this vpc instance is not connected with other vpc or created just in time and meta data is not sync to cms, please wait." }, { "orgFullId": "0.1.3", "targetInstanceId": "dds- 6ad8****73a4", "cloudProductType ": "acs mongodb", _ "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "vpc-6ade****j5tt", "cloudProductType ": "acs vpc", _ "appKey": "2", "resultType": "NO TASK", _ "taskBizType": "vpc2VpcPing", "errorMsg": "maybe this vpc instance is not connected with other vpc or created just in time and meta data is not sync to cms, please wait." }, { "orgFullId": "0.1.3", "targetInstanceId": "dds- 6ada****1124", |   |
|---|---|---|---|

|   |   | "cloudProductType ": "acs mongodb", _ "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "dds- 6ade****7754", "cloudProductType ": "acs mongodb", _ "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "dds- 6ad7****f974", "cloudProductType ": "acs mongodb", _ "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "dds- 6ad1****e014", "cloudProductType ": "acs mongodb", _ "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "targetInstanceId": "", "cloudProductType ": "acs kafka", _ "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "rm- 6ad6****8y02", "cloudProductType ": "acs polardblocal", _ "appKey": "2", "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "gp-6ad5****nprq", "cloudProductType ": "acs hybriddb", _ "appKey": "2", |   |
|---|---|---|---|

|   |   | "userId": "1871****1297", "resultType": "OK" }, { "orgFullId": "0.1.3", "targetInstanceId": "dtsn****21ic", "cloudProductType ": "acs dts dashboar _ _ d", "appKey": "2", "userId": "1871****1297", "resultType": "NO DATA" }, { _ "orgFullId": "0.1.3", "targetInstanceId": "dtsu****q6ma", "cloudProductType ": "acs dts dashboar _ _ d", "appKey": "2", "userId": "1871****1297", "resultType": "NO DATA" }, { _ "orgFullId": "0.1.3", "targetInstanceId": "dtsj****a22v", "cloudProductType ": "acs dts dashboar _ _ d", "appKey": "2", "userId": "1871****1297", "resultType": "NO DATA" }, { _ "orgFullId": "0.1.3", "targetInstanceId": "dtsl****w7bh", "cloudProductType ": "acs dts sync", _ _ "appKey": "2", "userId": "1871****1297", "resultType": "NO DATA" }, { _ "targetInstanceId": "", "cloudProductType ": "acs ntr", _ "userId": "1871****1297", "resultType": "OK" } ] |   |
|---|---|---|---|
| Code | String | 200 | The business status code. A value of 200 indicates success, and a non-200 value indicates failure. For specific error codes, see the error information section. |

The `Resources` field is a JSON format string. After parsing, it becomes an array of objects. Each object contains information such as the job ID, alert count, and task status. For the specific field structure, refer to the business definition.

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeBatchDetectTaskWithAlertResult &AcceptLanguage=zh-CN &Common Request Parameter
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"4C467B38-391A-5B8B-AF9A-1D3F3D3D3D3D",
 "Resources":"[{\"taskId\":\"task-001\",\"alertCount\":5,\"status\":\"ALARM\"}]",
 "Code":"200",
 "Success":true
```

`}`

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The request processing has failed due to some unknown error. |
| 400 | ParameterInvalid | Illegal parameters. | The parameters are invalid. |
| 403 | AccessForbidden | User not authorized to operate on the specified resource. | You do not have permissions to perform operations on the specified resource. |
| 404 | ResourceNotFound | The specified resource is not found. | The specified resource is not found |

**Additional notes**

1. This API is a private API (visibility=Private). Before you call this API, make sure that your
account has the required access permissions.
2. The returned `Resources` content is a string. You must parse it into a JSON object before
you use it.
3. In a production environment, set appropriate pagination parameters to avoid performance
issues caused by pulling excessive data volumes in a single request.

#### 2.10.2 DescribeNotificationRules

Queries the information about a notification policy.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Status | Strin g | Quer y | No | normal | The status. |
| PageSize | Strin g | Quer y | Yes | 1000 | The number of entries per page. |
| KeyWords | Strin g | Quer y | No | 1 | The keywords. |
| AcceptLan guage | Strin g | Quer y | Yes | zh | The language of the response. |
| PageNumb er | Strin g | Quer y | Yes | 1 | The page number. |
| Departme nt | Strin g | Quer y | No | ** | The organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Code | Integer | 200 | The HTTP status code. |
| Message | String | Success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeNotificationRules &PageSize= &AcceptLanguage= &PageNumber= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
 "Message":"Success",
 "Data":{
  "Pages":"",
  "PageSize":"",
  "List":[
```

`{`

```json
    "Status":"",
    "GmtCreate":"",
    "Description":"",
    "AvailableTime":[
```

`{`

```json
      "Start":"",
      "End":""
```

`}` `],`

```json
    "FilterCondition":[
```

`{`

```json
      "FilterConditionList":[
```

`{`

```json
        "Operator":"",
        "ValueList":"",
        "Key":""
```

`}` `],`

```json
      "MatchType":""
```

`}` `],`

```json
    "Receivers":"",
    "GmtModified":"",
    "Id":"",
    "NotificationTrigger":[
```

`{`

```json
      "ExecTimes":"",
      "Type":"",
      "ExecInterval":"",
      "SilenceInterval":""
```

`}` `],`

```json
    "Webhook":[
```

`{`

```json
"RequestParam":"",
```

```
      RequestParam:
```

`,`

```json
      "ContentType":"",
      "CustomHeader":"",
      "Method":"",
      "BodyParamJson":"",
      "Url":"",
      "BodyParam":""
```

`}` `],`

```json
    "Name":""
```

`}` `],`

```json
  "CurrentPage":"",
  "Total":""
```

`},`

```json
 "Code":200,
 "Success":true
```

`}` `XML` format

```xml
<RequestId>ACBDBB40-DFB6-4F4C-8957-51FFB233969C</RequestId> <Message>Success</Message> <Data>
 <Pages  />
 <PageSize  />
 <List>
  <Status  />
  <GmtCreate  />
  <Description  />
  <AvailableTime>
   <Start  />
   <End  />
  </AvailableTime>
  <FilterCondition>
   <FilterConditionList>
    <Operator  />
    <ValueList  />
    <Key  />
   </FilterConditionList>
   <MatchType  />
  </FilterCondition>
  <Receivers  />
  <GmtModified  />
  <Id  />
  <NotificationTrigger>
   <ExecTimes  />
   <Type  />
   <ExecInterval  />
   <SilenceInterval  />
  </NotificationTrigger>
  <Webhook>
   <RequestParam  />
   <ContentType  />
   <CustomHeader  />
   <Method  />
   <BodyParamJson  />
   <Url  />
   <BodyParam  />
  </Webhook>
  <Name  />
 </List>
 <CurrentPage  />
 <Total  />
</Data> <Code>200</Code> <Success>true</Success>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| 400 | 400 | ParameterInvalid | Illegal parameters. |
|---|---|---|---|
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

Cms 2019-01-01

#### 2.10.3 DescribeAlertList

Retrieves the alert list.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AlertSourc e | Strin g | Quer y | No | cms | The alert source. Exact match. |
| AlertBizId | Strin g | Quer y | No | cms cpu high 16800000 _ _ _ 00000 | The system-generated business alert ID. Exact match. |
| Status | Strin g | Quer y | No | FIRING | The alert status. You can specify multiple values separated by commas. Valid values: FIRING (firing) and CLOSED (resolved) |
| Severity | Strin g | Quer y | No | CRITICAL | The severity. Exact match. Valid values: CRITICAL, HIGH, MEDIUM, and LOW |
| ItemName | Strin g | Quer y | No | i-bp1abc123456 | The name of the alert object. Exact match. |

| Summary | Strin g | Quer y | No | 磁盘使用率 | The alert description. Fuzzy match on both the summary and detail fields. |
|---|---|---|---|---|---|
| AlertProdu ct | Strin g | Quer y | No | acs ecs dashboard _ _ | The cloud product identifier. Exact match. |
| PageNum | Integ er | Quer y | Yes | 1 | The page number. Pages start from 1. |
| PageSize | Integ er | Quer y | Yes | 20 | The number of entries per page. |
| StartTime | Strin g | Quer y | No | 1700000000000 | The lower bound of the alert trigger time in milliseconds. This means start time must be later _ than or equal to StartTime. |
| EndTime | Strin g | Quer y | No | 1700086400000 | The upper bound of the alert trigger time in milliseconds. This means start time must be earlier _ than or equal to EndTime. If you do not specify this parameter, the system uses the current time by default. |
| Departme nt | Integ er | Quer y | Yes | 1234 | The department. |
| TagValue | Strin g | Quer y | No | production | The tag value or rule code. Fuzzy match on the tags or rule code field. _ |
| AlertIds | Strin g | Quer y | No | 1001,1002,1003 | The list of alert IDs. Separate multiple IDs with commas. Exact match. |
| RuleName | Strin g | Quer y | No | CPU使用率超过80% | The alert rule name. Fuzzy match. |

| AcceptLan guage | Strin g | Quer y | No | zh-CN | The preferred language of the requester. |
|---|---|---|---|---|---|
| ActiveStart Time | Strin g | Quer y | No | 1700000000000 | The start time for filtering active alerts in milliseconds. You must specify both this parameter and ActiveEndTime for the filter to take effect. |
| ActiveEnd Time | Strin g | Quer y | No | 1700086400000 | The end time for filtering active alerts in milliseconds. You must specify both this parameter and ActiveStartTime for the filter to take effect. |
| AppKey | Strin g | Quer y | No | myAppKey123 | The application identifier. Exact match. |

**Response parameters**

| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID returned by other cloud products. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the operation succeeded. |
| Code | String | 404 | The status code. |
| Message | String | Request succeeded | The error message. |
| TotalCount | String | 1 | The total number of records. |
| Data | Array | {"total":"100","tota lPage":"10","pageS ize":"10","page":"1 ","objectList":[]} | The returned alert data, including pagination information and the alert object list. |
| -Id | String | 100001 | The auto-increment primary key of the alert. |
| -AlertSource | String | cms | The alert source. |

| -AlertBizId | String | cms cpu high 168 _ _ _ 0000000000 | The business primary key of the alert. |
|---|---|---|---|
| -AlertKey | String | cms cpu rule i- _ _ _ bp1abc | The unique ID of the alert. This key combines the alert object and the rule, and is independent of time. |
| -Title | String | ECS instance CPU utilization too high | The alert title. |
| -DisplayName | String | CPU utilization | The frontend display name. |
| -RuleName | String | CPU utilization exceeds 80% | The alert rule name. |
| -RuleCode | String | cpu usage high _ _ | The alert rule code. |
| -ItemId | String | i-bp1abc123456 | The alert object identifier. |
| -ItemName | String | Production environment - Web server | The alert object name. |
| -ItemType | String | INSTANCE | The alert object type. |
| -ItemLayer | String | CLOUD | The alert layer. |
| -Product | String | acs ecs dashboard _ _ | The cloud product identifier. |
| -Severity | String | CRITICAL | The severity. Valid values: CRITICAL, HIGH, MEDIUM, and LOW |
| -Status | String | FIRING | The alert status. Valid values: FIRING (alerting) and CLOSED (restored) |
| -ProcessStatus | String | ACKNOWLEDGED | The manual processing status. |
| -Summary | String | CPU utilization remains above 80%. Current value: 95% | The alert description. |

| -Url | String | https://cms.console .aliyun.com/alert/d etail/100001 | The alert detail link. |
|---|---|---|---|
| -StartTime | Integer | 1700000000000 | The alert trigger time (in millisecond timestamp format). |
| -EndTime | Integer | 1700086400000 | The alert recovery time (in millisecond timestamp format). If the alert is still active, this field is populated with a placeholder future timestamp. |
| -ResolvedTime | Integer | 1700086400000 | The actual recovery time (in millisecond timestamp format). |
| -AckTime | Integer | 1700003600000 | The manual response time (in millisecond timestamp format). |
| -Duration | Integer | 86400000 | The duration (in milliseconds). |
| - MessageCount | Integer | 5 | The number of times the alert message triggered. |
| - FirstMessageTi me | Integer | 1700000000000 | The first trigger time (in millisecond timestamp format). |
| - LastMessageTi me | Integer | 1700080000000 | The most recent trigger time (in millisecond timestamp format). |
| -Tags | Json | {"region":"cn- hangzhou","env":" prod"} | The tag information. |
| -Detail | Json | {"metricName":"cp u total","threshold" _ :"80"} | The extended details. |
| -UserId | String | 123456 | The ID of the associated user. |
| -OrgId | String | 123456 | The ID of the organization. |

| - OrgNameByUs erId | String | Sub-organization A | The name of the organization corresponding to the user ID. |
|---|---|---|---|
| -AppKey | String | myAppKey123 | The application identifier. |
| -ResourceId | String | r-bp1abc123456 | The resource ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlertList &OrgId=123456 &PageNum=1 &PageSize=20 &Status=FIRING &Severity=CRITICAL &StartTime=1700000000000 &EndTime=1700086400000 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "TotalCount": "158",
  "RequestId": "ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
  "Message": "The request is successful.",
  "Code": "200",
  "Success": true,
  "Data": [
```

`{`

```json
      "Id": "100001",
      "AlertSource": "cms",
      "AlertBizId": "cms_cpu_high_1680000000000",
      "AlertKey": "cms_cpu_rule_i-bp1abc",
      "Title": "The CPU utilization of the ECS instance is excessively high.",
      "DisplayName": "CPU utilization",
      "RuleName": "CPU utilization exceeds 80%",
      "RuleCode": "cpu_usage_high",
      "ItemId": "i-bp1abc123456",
      "ItemName": "Production environment - Web server",
      "ItemType": "INSTANCE",
      "ItemLayer": "CLOUD",
      "Product": "acs_ecs_dashboard",
      "Severity": "CRITICAL",
      "Status": "FIRING",
      "ProcessStatus": "ACKNOWLEDGED",
      "Summary": "The CPU utilization continuously exceeds 80%. Current value: 95%.",
      "Url": "https://cms.console.aliyun.com/alert/detail/100001",
      "StartTime": 1700000000000,
      "EndTime": 1700086400000,
      "ResolvedTime": 1700086400000,
      "AckTime": 1700003600000,
      "Duration": 86400000,
      "MessageCount": 5,
      "FirstMessageTime": 1700000000000,
      "LastMessageTime": 1700080000000,
      "Tags": {
        "region": "cn-hangzhou",
        "env": "prod"
```

`},`

```json
      "Detail": {
        "metricName": "cpu_total",
        "threshold": "80"
```

`},`

```json
      "UserId": "123456",
      "OrgId": "123456",
      "OrgNameByUserId": "Sub-organization A",
      "AppKey": "myAppKey123",
      "ResourceId": "r-bp1abc123456"
```

`}` `]` `}` `XML` format

```xml
<TotalCount /> <RequestId /> <Message /> <Data>
 <EndTime  />
 <ProcessStatus  />
 <ItemType  />
 <Product  />
 <ItemId  />
 <Url  />
 <AlertBizId  />
 <ItemName  />
 <FirstMessageTime  />
 <RuleName  />
 <Tags  />
 <AlertKey  />
 <ItemLayer  />
 <Status  />
 <OrgNameByUserId  />
 <AckTime  />
 <StartTime  />
 <Title  />
 <ResolvedTime  />
 <Severity  />
 <Duration  />
 <AlertSource  />
 <OrgId  />
 <ResourceId  />
 <UserId  />
 <LastMessageTime  />
 <Summary  />
 <Id  />
 <RuleCode  />
 <MessageCount  />
 <Detail  />
</Data> <Code /> <Success />
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | The parameter is invalid. |
| 403 | 403 | AccessForbidden | The user does not have the permissions to perform operations on the specified resource. |

| 404 | 404 | ResourceNotFound | The specified resource is not found. |
|---|---|---|---|
| 500 | 500 | InternalError | The system failed to process the request due to some unknown errors. |

```html ```

#### 2.10.4 DeleteAlertFilterConfigBatch

Deletes a masking policy.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| IdList | Strin g | Query | Yes | 1 | The IDs. |
| Departme nt | Strin g | Query | Yes | ** | The organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID returned when CloudMonitor calls another cloud service. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Code | Integer | 404 | The HTTP status code. |
| Message | String | Success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteAlertFilterConfigBatch &IdList=1 &Department=** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"",
 "Message":"",
 "Code":"",
 "Success":""
```

`}` `XML` format

```
<RequestId /> <Message /> <Code /> <Success />
```

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.10.5 ModifyAlertFilterConfig

Updates a masking policy.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Query | Yes | 123456 | The ID of the application group. |
| Name | Strin g | Query | No | test123 | The name of the application group. |
| Departme nt | Strin g | Query | Yes | ** | The organization. |
| AlertSourc e | Strin g | Query | No | System Log | The source of the alert. |
| Descriptio n | Strin g | Query | No | ECS Template1 _ | The description of the alert template. |
| AlertNam e | Strin g | Query | No | ruleId-xxxxxx | The ID of the alert rule. |
| Forbid | Strin g | Query | No | 0/1 | Specifies whether to prohibit an operation. |
| Severity | Strin g | Query | No | information | The severity level. |
| Dimension | Strin g | Query | No | TENANT | The dimensions that specify the resources whose metric data you want to query. |
| Content | Strin g | Query | No | IOException | The event content. |
| AvailableT ime | Strin g | Query | No | 8 Hours | The period of time that a resource or service is available for use within 24 hours. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID returned when CloudMonitor calls another cloud service. |
| Success | Boolean | true | Indicates whether the request was successful. |

| CloudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| Code | Integer | 404 | The HTTP status code. |
| Message | String | Success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyAlertFilterConfig &Id=123456 &Department=** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"",
 "Message":"",
 "Code":"",
 "Success":""
```

`}` `XML` format

```
<RequestId /> <Message /> <Code /> <Success />
```

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.10.6 DescribeAlertFilterConfig

Queries masking policies.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum | Integ er | Query | Yes | 1 | The page number. |
| PageSize | Integ er | Query | Yes | 1000 | The number of entries per page. |
| Departme nt | Integ er | Query | Yes | ** | The organization. |
| Forbid | Boole an | Query | No | 0/1 | Specifies whether to prohibit an operation. |
| Name | Strin g | Query | No | test123 | The name of the application group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | abc1234567890 |
| Success | Boolean | true | Indicates whether the request was successful. |
| Code | String | 200 | The HTTP status code. |
| Message | String | Success | The returned message. |
| TotalCount | String | 1 | The total number of entries. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlertFilterConfig &PageNum= &PageSize= &Department= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "TotalCount":"",
 "RequestId":"",
 "Message":"",
 "Data":[
```

`{`

```json
   "Forbid":"",
   "OrgId":"",
   "Description":"",
   "AlertName":"",
   "AvailableTime":"",
   "UserId":"",
   "Content":"",
   "Severity":"",
   "Id":"",
   "Dimension":"",
   "AlertSource":"",
   "Name":""
```

`}` `],`

```json
 "Code":"",
 "Success":""
```

`}` `XML` format

```xml
<TotalCount /> <RequestId /> <Message /> <Data>
 <Forbid  />
 <OrgId  />
 <Description  />
 <AlertName  />
 <AvailableTime  />
 <UserId  />
 <Content  />
 <Severity  />
 <Id  />
 <Dimension  />
 <AlertSource  />
 <Name  />
</Data> <Code /> <Success />
```

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 2.10.7 DeleteNotificationRules

Deletes notification policies.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| IdList | Strin g | Query | Yes | 1 | The IDs. |

|   | CloudMonitor |   |   |   | Dev | eloper Guide·API Referenc | e |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Query | No | ** | The organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID returned when CloudMonitor calls another cloud service. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Code | Integer | 200 | The HTTP status code. |
| Message | String | Success | The returned message. |

`JSON` format `{`

```json
 "RequestId":"ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
 "Message":"Success",
 "Code":200,
 "Success":true
```

`}` `XML` format

```xml
<RequestId>ACBDBB40-DFB6-4F4C-8957-51FFB233969C</RequestId> <Message>Success</Message> <Code>200</Code> <Success>true</Success>
```

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

#### 2.10.8 ModifyNotificationRule

Updates a notification policy.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RuleId | Long | Query | Yes | ruleId-xxxxxx | The ID of the alert rule. |
| Name | Strin g | Query | No | test123 | The name of the application group. |
| Descriptio n | Strin g | Query | No | ECS Template1 _ | The description of the alert template. |
| Receivers | Strin g | Query | No | 123.qq.com | The alert recipients. |
| Status | Strin g | Query | No | normal | The event status. |
| AvailableT ime | Strin g | Query | Yes | All Day | The description. |
| FilterCond ition | Strin g | Query | No | [dbName:sys] | The filter condition. |
| Notificatio nTrigger | Strin g | Query | No | 09:00 | A notification is triggered when a new message is received. |
| AcceptLan guage | Strin g | Query | Yes | zh | The language of the response. Valid values: |
| Webhook | Strin g | Query | No | https://www.aliyun.com | The callback URL. |
| Departme nt | Strin g | Query | No | ** | The organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | abc1234567890 |
| Success | Boolean | true | Indicates whether the request was successful. |
| Code | Integer | 200 | The HTTP status code. |
| Message | String | Success | The returned message. |
| Id | String | 2 | The ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyNotificationRule &RuleId=ruleId-xxxxxx &AvailableTime=All Day &AcceptLanguage=zh &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"",
 "Message":"",
 "Id":"",
 "Code":"",
 "Success":""
```

`}` `XML` format

```
<RequestId /> <Message /> <Id /> <Code /> <Success />
```

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

#### 2.10.9 CreateAlertFilterConfig

Creates a masking policy.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Query | No | test123 | The name of the application group. |
| Departme nt | Strin g | Query | Yes | ** | The organization. |
| Descriptio n | Strin g | Query | No | ECS Template1 _ | The description of the alert template. |
| AlertSourc e | Strin g | Query | No | User Behavior | The source of the alert. |
| AlertNam e | Strin g | Query | No | ruleId-xxxxxx | The ID of the alert rule. |
| Severity | Strin g | Query | No | information | The severity level. |
| Dimension | Strin g | Query | No | {sampleName1=value1 &sampleName2=value2 } | The dimensions that specify the resources whose metric data you want to query. |
| Content | Strin g | Query | No | IOException | The event content. |
| AvailableT ime | Strin g | Query | No | 8 | The description. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID returned when CloudMonitor calls another cloud service. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Code | Integer | 404 | The HTTP status code. |
| Message | String | Success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateAlertFilterConfig &Department=** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
 "Message":"Success",
 "Code":404,
 "Success":true
```

`}` `XML` format

```xml
<RequestId>ACBDBB40-DFB6-4F4C-8957-51FFB233969C</RequestId> <Message>Success</Message> <Code>404</Code> <Success>true</Success>
```

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |

| Developer Gui | de·API Reference |   | CloudMonito |
|---|---|---|---|

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

#### 2.10.10 PutNotificationRule

Creates a notification policy.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Query | No | test123 | The name of the application group. |
| Descriptio n | Strin g | Query | No | ECS Template1 _ | The description of the alert template. |
| Receivers | Strin g | Query | No | 123.qq.com | The alert recipients. |
| Status | Strin g | Query | No | normal | The event status. |
| AvailableT ime | Strin g | Query | Yes | 8 Hours | The description. |
| FilterCond ition | Strin g | Query | No | [dbName:sys] | The filter condition. |
| Notificatio nTrigger | Strin g | Query | No | Geographical location | The notification trigger. |
| AcceptLan guage | Strin g | Query | Yes | zh | The language of the response. |
| Webhook | Strin g | Query | No | https://www.aliyun.com | The callback URL. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Code | Integer | 404 | The HTTP status code. |
| Message | String | Success | The returned message. |
| Id | String | 2 | The ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutNotificationRule &AvailableTime=8 Hours &AcceptLanguage=zh &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
 "Message":"Success",
 "Id":"2",
 "Code":404,
 "Success":true
```

`}` `XML` format

```xml
<RequestId>ACBDBB40-DFB6-4F4C-8957-51FFB233969C</RequestId> <Message>Success</Message> <Id>2</Id> <Code>404</Code> <Success>true</Success>
```

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |

| Developer Gu | ide·API Reference |   | CloudMonito |
|---|---|---|---|

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

### 2.11 Data subscription

#### 2.11.1 CreateMetricPubSync

Creates a data subscription task.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Integ er | Quer y | No | ** | The organization. |
| Name | Strin g | Quer y | Yes | test123 | The key. |
| ProjectNa meRegex | Strin g | Quer y | No | ProjectName | The project name. |
| MetricNam eRegex | Strin g | Quer y | No | MetricName | The metric name. |
| SlsProject | Strin g | Quer y | No | test-project | The SLS project. |
| SlsLogstor e | Strin g | Quer y | No | test-logstore | The SLS Logstore. |
| SlsAk | Strin g | Quer y | No | 4Fke8a2D1Xp9Bc3dG5f6 H | Ak |

| SlsSk | Strin g | Quer y | No | 1234567890abcdef | Sk |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | abc1234567890 |
| Code | String | 404 | The HTTP status code. |
| Message | String | Success | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Resource | String | 12345 | The resources. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateMetricPubSync &Name= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"",
 "Message":"",
 "Resource":"",
 "Code":"",
 "Success":""
```

`}` `XML` format

```
<RequestId /> <Message /> <Resource /> <Code /> <Success />
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

Cms 2019-01-01

#### 2.11.2 UpdateMetricPubSync

Updates a data subscription task.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Long | Query | Yes | 123456 | The task ID. |
| Departme nt | Integ er | Query | No | ** | The organization. |
| Name | Strin g | Query | Yes | test123 | The name. |
| ProjectNa meRegex | Strin g | Query | No | ProjectName | The project name. |
| MetricNa meRegex | Strin g | Query | No | MetricName | The metric name. |
| SlsProject | Strin g | Query | No | test-project | sls project |
| SlsLogstor e | Strin g | Query | No | test-logstore | sls log store |

| CloudMonitor |   |   |   | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SlsAk | Strin g | Query | No | 4321XXXXXXXXX1234 | Ak |
| SlsSk | Strin g | Query | No | xxxxxxxxxx | Sk |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID. |
| Code | String | 404 | The HTTP status code. |
| Message | String | Success | The returned message. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Resource | String | 12345 | The resources. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateMetricPubSync &Id=123456 &Name=test123 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"",
 "Message":"",
 "Resource":"",
 "Code":"",
 "Success":""
```

`}` `XML` format

```
<RequestId /> <Message /> <Resource /> <Code /> <Success />
```

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

#### 2.11.3 DeleteMetricPubSync

Deletes a data subscription task.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Integ er | Query | Yes | ** | The organization. |
| Id | Long | Query | Yes | 123456 | The task ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID. |
| Code | String | 404 | The HTTP status code. |
| Success | Boolean | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMetricPubSync &Department=** &Id=123456 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"",
 "Code":"",
 "Success":""
```

`}` `XML` format

```
<RequestId /> <Code /> <Success />
```

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

#### 2.11.4 DescribeMetricPubSyncs

Queries data subscription tasks.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Integ er | Query | Yes | "" | The organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ACBDBB40-DFB6- 4F4C-8957- 51FFB233969C | The request ID returned when CloudMonitor calls another cloud service. |
| Code | String | 200 | The HTTP status code. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Resources | String | [{"resource":" ALL _ "}] | The returned result. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricPubSyncs
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"ACBDBB40-DFB6-4F4C-8957-51FFB233969C",
 "Resources":"[{\"resource\":\"_ALL\"}]",
 "Code":"200",
 "Success":true
```

`}` `XML` format

```xml
<RequestId>ACBDBB40-DFB6-4F4C-8957-51FFB233969C</RequestId> <Resources>[{&quot;resource&quot;:&quot;_ALL&quot;}]</Resources> <Code>200</Code> <Success>true</Success>
```

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |

### 2.12 Log monitoring

#### 2.12.1 PutLogMonitor

Creates or modifies a log monitoring metric.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| LogId | Integ er | Query | No | 16**** | The ID of the log monitoring metric. |
| SlsRegionI d | Strin g | Query | No | cn-hangzhou | The region in which the Simple Log Service (SLS) project resides. |
| SlsProject | Strin g | Query | Yes | test-project | The name of the SLS project. |
| SlsLogstor e | Strin g | Query | Yes | test-logstore | The name of the SLS Logstore. |
| MetricNa me | Strin g | Query | Yes | cpu total _ | The metric name. For more information about the metrics for cloud services, see Appendix 1: Metrics. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| MetricExp ress | Strin g | Query | No | {"extend": {"errorPercent":"5XXNu mber/TotalNumber*100" }} | The extended field. The extended field allows you to perform basic operations on the aggregation results. For example, if you have calculated TotalNumber and 5XXNumber by aggregating the data. TotalNumber indicates the total number of HTTP requests, and 5XXNumber indicates the number of HTTP requests whose status code is greater than 499. You can calculate the server error rate by adding the following formula to the extended field: 5XXNumber/TotalNumbe r*100. JSON format: {"extend": {"errorPercent":"5XXNu mber/TotalNumber*100" }}. Description: extend: required. errorPercent: the alias of the field generated in the calculation result. You can specify the alias as needed. 5XXNumber/TotalNum ber*100: the calculation expression. |
| Unit | Strin g | Query | No | Percent | The unit. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ValueFilte rRelation | Strin g | Query | No | and | The logical operator that is used between log filter conditions. Valid values: and or Note The ValueFilterRelation and ValueFilter.N.Ke y parameters must be used in pair. |
| Tumbling windows | Strin g | Query | No | 60,300 | The size of the tumbling window for calculation. Unit: seconds. CloudMonitor performs aggregation for each tumbling window. |
| Aggregate s | Repe atList | Query | Yes | AVG | The aggregation logic. |
| - FieldNam e | Strin g |   | Yes | cpu | The name of the field that is specified as the dimension. Valid values of N: 1 to 10. |

|   |   |   | ValueFilter.N.Ke |   |
|---|---|---|---|---|
|   |   | y |   |   |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| -Function | Strin g |   | Yes | count | The function that is used to aggregate the log data of a statistical period. Valid values of N: 1 to 10. Valid values: count: counts the number sum: calculates the total value avg: calculates the average value max: calculates the maximum value min: calculates the minimum value countps: calculates the counted number of the specified field divided by the total number of seconds within the statistical period sumps: calculates the total value of the specified field divided by the total number of seconds within the statistical period distinct: calculates the number of unique values of the specified field within a statistical period |
| -Alias | Strin g |   | Yes | CPUUtilization | The alias of the dimension based on which the data is grouped. Valid values of N: 1 to 10. |
| Groupbys | Strin g | Query | No | 1 | The dimension based on which the data is grouped. This parameter is equivalent to the GROUP BY clause in SQL statements. If you do not specify a dimension, all data is aggregated based on the specified aggregate functions. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ValueFilte r | Repe atList | Query | No | v1 | The condition that is used to filter logs. The ValueFilter and ValueFilterRelation parameters are used in pair. The filter condition is equivalent to the WHERE clause in SQL statements. If no filter condition is specified, all logs are processed. Assume that logs contain the Level field, which may be set to Error. If you need to calculate the number of times that logs of the Error level appear every minute, you can set the filter condition to Level=Error and count the number of logs that meet this condition. |
| -Key | Strin g |   | No | lh source _ | The name of the log field that is used for matching in the filter condition. Valid values of N: 1 to 10. |
| -Value | Strin g |   | No | test | The field value to be matched in the filter condition. Valid values of N: 1 to 10. |
| -Operator | Strin g |   | No | Operator | The method that is used to match the field value. Valid values of N: 1 to 10. Valid values: contain : contains notContain : does not contain > : greater than < : less than >= : greater than or equal to <= : less than or equal to |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 91561287-0802- 5F9C-9BDE- 404C50D41B06 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | Integer | 200 | The HTTP status code. Note This parameter is deprecated. |
| Message | String | successful | The returned message. Sample result: If the request was successful, successful is returned. If the request failed, an error message is returned. Example: alias of aggreate must be set value. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 2 | The number of entries per page. |
| LogId | String | 16**** | The ID of the log monitoring metric. |

|   |   | alias of |
|---|---|---|
|   | aggreate must be set value. |   |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutLogMonitor &SlsRegionId=cn-hangzhou &SlsProject=test-project &SlsLogstore=test-logstore &MetricName=cpu_total &ValueFilterRelation=and &Aggregates=null &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "Message":"successful",
 "RequestId":"91561287-0802-5F9C-9BDE-404C50D41B06",
 "Code":"200",
 "LogId":"16****",
 "Success":true
```

`}` `XML` format

```xml
<Message>successful</Message> <RequestId>91561287-0802-5F9C-9BDE-404C50D41B06</RequestId> <Code>200</Code> <LogId>16****</LogId> <Success>true</Success>
```

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | %s |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 503 | 503 | %s | %s |
| 409 | 409 | %s | %s |
| 206 | 206 | %s | %s |
| 503 | 503 | %s | %s |
| 500 | DEFAULT | InternalError | The request processing has failed due to some unknown error. |

#### 2.12.2 DeleteLogMonitor

Deletes a log monitoring metric.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| LogId | Integ er | Query | Yes | 12345 | The ID of the log monitoring metric. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 42BFFC2B-5E4D- 4FDE-BCC6- E91EE33C5967 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| Code | Integer | 200 | The HTTP status code. Note The status code 200 indicates that the request was successful. |
| Message | String | metric not exist. | The error message. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 2 | The number of entries per page. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteLogMonitor &LogId=12345 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "Message":"metric not exist.",
 "RequestId":"42BFFC2B-5E4D-4FDE-BCC6-E91EE33C5967",
 "Code":"200",
 "Success":true
```

`}` `XML` format

```xml
<Message>metric not exist.</Message> <RequestId>42BFFC2B-5E4D-4FDE-BCC6-E91EE33C5967</RequestId> <Code>200</Code> <Success>true</Success>
```

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 401 | 401 | AccessDeniedException | You donot have sufficient access to perform this action. |
| 402 | 402 | LimitExceeded | The quota for this customer had been reached. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | %s | %s |
| 409 | 409 | %s | %s |
| 206 | 206 | %s | %s |
| 503 | 503 | %s | %s |
| 500 | DEFAULT | InternalError | The request processing has failed due to some unknown error. |

#### 2.12.3 DescribeLogMonitorList

Queries log monitoring metrics.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. Default value: 10. |
| SearchVal ue | Strin g | Query | No | test | The keyword that is used to search for log monitoring metrics. Fuzzy match is supported. |
| GroupId | Long | Query | No | 123456 | The ID of the application group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 01E90080-4300- 4FAA-B9AE- 161956BC350D | The request ID. |
| Message | String | successful | The returned message. |
| PageSize | Integer | 10 | The number of entries per page. |
| PageNumber | Integer | 1 | The page number. |
| Total | Long | 15 | The total number of entries. |
| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the request was successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLogMonitorList &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"01E90080-4300-4FAA-B9AE-161956BC350D",
 "Message":"successful",
 "PageSize":10,
 "PageNumber":1,
 "Total":15,
 "LogMonitorList":[
```

`{`

```json
   "MetricName":"cpu_total",
   "SlsProject":"sls-project-test****",
   "ValueFilter":[
```

`{`

```json
     "Operator":"",
     "Value":"",
     "Key":""
```

`}` `],`

```json
   "GmtCreate":1577766395000,
   "ValueFilterRelation":"and",
   "SlsLogstore":"testSlS****",
   "LogId":12345,
   "SlsRegionId":"cn-hangzhou",
   "GroupId":12345
```

`}` `],`

```json
 "Code":"200",
 "Success":true
```

`}` `XML` format

```xml
<RequestId>01E90080-4300-4FAA-B9AE-161956BC350D</RequestId> <Message>successful</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Total>15</Total> <LogMonitorList>
 <MetricName>cpu_total</MetricName>
 <SlsProject>sls-project-test****</SlsProject>
 <ValueFilter>
  <Operator  />
  <Value  />
  <Key  />
 </ValueFilter>
 <GmtCreate>1577766395000</GmtCreate>
 <ValueFilterRelation>and</ValueFilterRelation>
 <SlsLogstore>testSlS****</SlsLogstore>
 <LogId>12345</LogId>
 <SlsRegionId>cn-hangzhou</SlsRegionId>
 <GroupId>12345</GroupId>
</LogMonitorList> <Code>200</Code> <Success>true</Success>
```

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | 400 | ParameterInvalid | Illegal parameters. |
| 403 | 403 | AccessForbidden | User not authorized to operate on the specified resource. |
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 500 | DEFAULT | InternalError | The request processing has failed due to some unknown error. |

## 3 Metrics

This topic describes the metrics available for each service. CloudMonitor checks the availability of a service based on the metrics for the service. You can configure alarm rules and notification policies for these metrics to stay up-to-date on the running status and performance of monitored service instances. CloudMonitor can monitor resources of ECS, SLB, ApsaraDB for RDS, OSS, and KVStore for Redis. The following table lists the metrics for each service.

| Metric | Description | Apsara Stack service | Calculation formula | Remarks |
|---|---|---|---|---|
| CPU utilization | Measures the CPU utilization of an ECS instance. Unit: %. | ECS | CPU utilization of an ECS instance/Tot al CPU cores of the ECS instance | None |
| Memory usage | Measures the memory usage of an ECS instance. Unit: %. | ECS | Memory usage of an ECS instance/Tot al memory of the ECS instance | When you use the free or top command to query memory usage of a Linux ECS instance, you may find that the memory usage is inconsistent with the actual memory usage displayed in the Apsara Stack Cloud Management (ASCM) console. This is because when CloudMonitor is calculating the memory usage, it does not take the amount of memory used as cache into account. |
| Disk I/O read | Measures the volume of data read from an ECS instance disk per second. Unit: KB/s. | ECS | Total bytes read from an ECS instance disk/Statistic al period | For a Linux ECS instance, the disk I/O data can be obtained by using the iostat tool. If you find that the Linux ECS instance does not have any disk I/O data, check whether iostat has been installed in your ECS instance. If not, Redhat and CentOS users can use yum to install the tool, while Ubuntu and Debian users can use apt-get to install the tool. |
| Disk I/O write | Measures the volume of data written to an ECS instance disk per second. Unit: KB/s. | ECS | Total bytes written to an ECS instance disk/Statistic al period | None |
| Disk usage | Measures the disk usage of an ECS instance. Unit: %. | ECS | Used capacity of an ECS instance disk/Total capacity of the ECS instance disk | None |

| Developer Gui | de·Metrics |   |   | CloudMonito |
|---|---|---|---|---|

| Inbound traffic | Measures the inbound network traffic to an ECS instance per second. Unit: Kbit/s. | ECS | None | None |
|---|---|---|---|---|
| Outbound traffic | Measures the outbound network traffic from an ECS instance per second. Unit: Kbit/s. | ECS | None | When the purchased bandwidth is used up, access will fail or requests will slow down. On the monitoring chart, eth0 indicates the internal NIC of the ECS instance, and eth1 indicates the public NIC of the ECS instance. |
| Number of TCP connection s | Measures the total number of TCP connections established by an ECS instance. | ECS | None | None |
| Number of processes | While an alarm rule is configured with this metric, the number of specified processes is counted and the total number displayed. | ECS | None | To monitor the running conditions of processes in an ECS instance, configure an alarm rule with this metric to trigger the alarm when the number of running processes does not equal the actual number of processes. |
| Average load | Measures the average load value of a Linux ECS instance. | ECS | None | The average load value cannot be greater than 1. If your ECS instance has a multi-core processor, the average load value must be divided by the number of CPU cores and the obtained value must be smaller than 1. If the average load value is greater than 1, processes are queued up and the ECS instance slows down. |

> **Note:** For ECS instances, you must install a monitoring plug-in to collect metric data at the operating system level.
> Installation method: In the ECS instance list on the **CloudMonitor** page, select the instance to be monitored, and click **Batch Install** below the instance list.
> The monitoring chart displays monitoring data 5 to 10 minutes after the monitoring plug- in is installed.

Table 1. Metrics for ApsaraDB for RDS

| Metric | Description | Apsara Stack service | Calculation formula |
|---|---|---|---|
| CPU utilization | Measures the CPU utilization of an RDS instance. Unit: %. | ApsaraDB for RDS | CPU utilization of an RDS instance/Total CPU cores of the RDS instance |
| Memory usage | Measures the memory usage of an RDS instance. Unit: %. | ApsaraDB for RDS | Used memory of an RDS instance/Total memory of the RDS instance |
| Disk usage | Measures the disk usage of an RDS instance. Unit: %. | ApsaraDB for RDS | None |
| IOPS utilization | Measures the number of I/O requests for an RDS instance per second. Unit: %. | ApsaraDB for RDS | Number of I/O requests for an RDS instance/Statistical period |
| Connectio n utilization | Measures the number of connections between an application and an RDS instance per second. Unit: %. | ApsaraDB for RDS | Number of connections between an application and an RDS instance per second/Statistical period |

Table 2. Metrics for SLB

| Metric | Description | Apsara Stack service | Remarks |
|---|---|---|---|
| Number of outbound packets sent over a port per second | Measures the number of packets sent by an SLB instance per second. | SLB | None |
| Number of inbound packets received over a port per second | Measures the number of packets received by an SLB instance per second. | SLB | None |

| Amount of data received over a port per second | Measures the traffic consumed to access an SLB instance from the Internet. Unit: Kbit/s. | SLB | None |
|---|---|---|---|
| Amount of data sent over a port per second. | Measures the traffic consumed by an SLB instance to access the Internet. Unit: Kbit/s. | SLB | None |
| Number of active connectio ns on a port | Measures the number of connections in the ESTABLISHED state. | SLB | It can be interpreted as, but cannot be equivalent to, the concurrent connections. If persistent connections are used, a connection can transfer multiple file requests at one time. |
| Number of inactive connectio ns on a port | Measures the number of all TCP connections except connections in the ESTABLISHED state. | SLB | None |
| Number of new connectio ns on a port | Measures the average number of times that the status is SYN SENT at first _ for a TCP three-way handshake in the statistical period. | SLB | Number of New Port Connections, Number of Active Port Connections, and Number of Inactive Port Connections are all used to measure the number of requests for connecting a client to an SLB instance. |

Table 3. Metrics for OSS

| Metric | Description | Apsara Stack service |
|---|---|---|
| Number of reads | Measures the number of reads of an OSS bucket. | OSS |
| Number of internal errors | Measures the number of errors that occur on an OSS bucket. | OSS |
| Inbound traffic from the Internet | Measures the inbound traffic from the Internet to an OSS bucket per second. Unit: bytes. | OSS |
| Outbound traffic to the Internet | Measures the outbound traffic from an OSS bucket to the Internet per second. Unit: bytes. | OSS |
| Inbound traffic from the internal network | Measures the inbound traffic from the internal network to an OSS bucket per second. Unit: bytes. | OSS |
| Outbound traffic to the internal network | Measures the outbound traffic from an OSS bucket to the internal network per second. Unit: bytes. | OSS |
| Number of writes | Measures the number of writes of an OSS bucket. | OSS |

| Used storage space | Measures the used storage space of an OSS bucket. Unit: bytes. | OSS |
|---|---|---|
| Number of successful requests | Measures the number of requests with an HTTP status code of 200. | OSS |
| Valid request percentage | Measures the percentage of valid requests to all requests. | OSS |
| Number of valid requests | Measures the number of valid requests. | OSS |
| Inbound and outbound network traffic | Measures the inbound and outbound traffic on the Internet and internal network. | OSS |
| Number of requests with server-side errors | Measures the number of requests with server-side errors. | OSS |
| Percentage of requests with server-side errors | Measures the percentage of total requests whose status code is 4xx. | OSS |
| Percentage of requests with network errors | Measures the percentage of total requests with network errors. | OSS |
| Number of requests with client-side errors | Measures the number of requests with client-side errors. | OSS |
| Number of GET requests | Measures the number of HTTP GET requests. | OSS |
| Number of PUT requests | Measures the number of HTTP PUT requests. | OSS |
| Maximum latency of GetObject requests | Measures the maximum allowable latency of GetObject requests. | OSS |
| Maximum latency of HeadObject requests | Measures the maximum allowable latency of HeadObject requests. | OSS |
| Maximum latency of PutObject requests | Measures the maximum allowable latency of PutObject requests. | OSS |
| Maximum latency of PostObject requests | Measures the maximum allowable latency of PostObject requests. | OSS |

Table 4. Metrics for KVStore for Redis

| Metric | Description | Apsara Stack service | Unit |
|---|---|---|---|

| CPU utilization | Measures the CPU utilization of a KVStore for Redis instance. | KVStore for Redis | % |
|---|---|---|---|
| Memory usage | Measures the percentage of used memory to total memory. | KVStore for Redis | % |
| Used memory | Measures the amount of memory currently in use. | KVStore for Redis | Bytes |
| Number of used connections | Measures the total number of client connections. | KVStore for Redis | N/A |
| Percentage of used connections | Measures the percentage of total connections that are used. | KVStore for Redis | % |
| Write bandwidth | Measures the write traffic per second. | KVStore for Redis | Bytes/s |
| Read bandwidth | Measures the read traffic per second. | KVStore for Redis | Bytes/s |
| Number of failed operations per second | Measures the number of failed operations on a KVStore for Redis instance per second. | KVStore for Redis | N/A |
| Write bandwidth usage | Measures the percentage of total bandwidth used by write operations. | KVStore for Redis | % |
| Read bandwidth usage | Measures the percentage of total bandwidth used by read operations. | KVStore for Redis | % |
| Used QPS | Measures the number of queries per second (QPS). | KVStore for Redis | N/A |
| QPS usage | Measures the QPS utilization rate. | KVStore for Redis | % |
| Average response time | Measures the average response time. | KVStore for Redis | Milliseco nds |
| Maximum response time | Measures the maximum response time. | KVStore for Redis | Milliseco nds |
| Number of failed commands | Measures the number of failed commands. | KVStore for Redis | N/A |
| Hit rate | Measures the current hit rate. | KVStore for Redis | % |
| Inbound traffic | Measures the inbound traffic to a KVStore for Redis instance. | KVStore for Redis | Bytes |
| Inbound bandwidth usage | Measures the inbound bandwidth usage of a KVStore for Redis instance. | KVStore for Redis | % |
| Outbound traffic | Measures the outbound traffic from a KVStore for Redis instance. | KVStore for Redis | Bytes |
| Outbound bandwidth usage | Measures the outbound bandwidth usage of a KVStore for Redis instance. | KVStore for Redis | % |

### 3.1 Elastic computing

#### 3.1.1 Kubernetes container monitoring

This topic describes the metrics for Kubernetes container monitoring.

**Cluster**

Set **Namespace** to **acs_k8s**. Set **Period** to an integral multiple of **60**. Default value: 60. Unit: seconds.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| cluster.cpu.limit | cores | cluster.cpu.limit | user id and _ cluster name _ | The maximum number of CPU cores that can be used by a container. |
| cluster.cpu.requ est | cores | cluster.cpu.reque st | user id and _ cluster name _ | The minimum number of CPU cores requested by a container during scheduling. |
| cluster.cpu.usag e rate _ | cores | cluster.cpu.usage rate _ | user id and _ cluster name _ | The CPU utilization. |
| cluster.cpu.utiliz ation | % | cluster.cpu.utiliza tion | user id and _ cluster name _ | The CPU utilization of the cluster. |
| cluster.filesyste m.available | Bytes | cluster.filesystem .available | user id and _ cluster name _ | The size of the file system that is available to the cluster. |
| cluster.filesyste m.limit | Bytes | cluster.filesystem .limit | user id and _ cluster name _ | The maximum number of file systems in the cluster. |
| cluster.memory. limit | Bytes | cluster.memory.li mit | user id and _ cluster name _ | The maximum memory of the cluster. |
| cluster.memory. request | Bytes | cluster.memory.r equest | user id and _ cluster name _ | The memory requested by the cluster. |
| cluster.memory. utilization | % | cluster.memory.u tilization | user id and _ cluster name _ | The memory usage of the cluster. |

**node**

Set **Namespace** to **acs_k8s**. Set **Period** to an integral multiple of **60**. Default value: 60. Unit: seconds.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| node.cpu.alloca table | core | node.cpu.allocata ble | userId, cluster, and node | node.cpu.allocatable |
| node.cpu.capaci ty | core | node.cpu.capacit y | userId, cluster, and node | node.cpu.capacity |
| node.cpu.limit | core | node.cpu.limit | userId, cluster, and node | node.cpu.limit |
| node.cpu.overs ale rate _ | % | node.cpu.oversal e rate _ | userId, cluster, and node | The CPU overcommit rate of a node. |
| node.cpu.reque st | core | node.cpu.request | userId, cluster, and node | node.cpu.request |
| node.cpu.reserv ation | core | node.cpu.reserva tion | userId, cluster, and node | node.cpu.reservation |
| node.cpu.usage rate _ | core | node.cpu.usage r _ ate | userId, cluster, and node | node.cpu.usage rate _ |
| node.cpu.utiliza tion | % | node.cpu.utilizati on | userId, cluster, and node | node.cpu.utilization |
| node.filesystem .available | count | node.filesystem.a vailable | userId, cluster, and node | node.filesystem.available |
| node.filesystem .limit | count | node.filesystem.li mit | userId, cluster, and node | node.filesystem.limit |
| node.filesystem .usage | count | node.filesystem.u sage | userId, cluster, and node | node.filesystem.usage |
| node.memory.al locatable | GB | node.memory.all ocatable | userId, cluster, and node | node.memory.allocatable |
| node.memory.c apacity | count | node.memory.ca pacity | userId, cluster, and node | node.memory.capacity |

| node.memory.li mit | count | node.memory.lim it | userId, cluster, and node | node.memory.limit |
|---|---|---|---|---|
| node.memory. major page fau _ _ lts | count | node.memory.ma jor page faults _ _ | userId, cluster, and node | node.memory.major page _ _ faults |
| node.memory. major page fau _ _ lts rate _ | count | node.memory.ma jor page faults r _ _ _ ate | userId, cluster, and node | node.memory.major page _ _ faults rate _ |
| node.memory.o versale rate _ | % | node.memory.ov ersale rate _ | userId, cluster, and node | The memory overcommit rate of a node. |
| node.memory.p age faults _ | count | node.memory.pa ge faults _ | userId, cluster, and node | node.memory.page faults _ |
| node.memory.p age faults rate _ _ | count | node.memory.pa ge faults rate _ _ | userId, cluster, and node | node.memory.page faults _ _ rate |
| node.memory.r equest | count | node.memory.req uest | userId, cluster, and node | node.memory.request |
| node.memory.r eservation | count | node.memory.res ervation | userId, cluster, and node | node.memory.reservation |
| node.memory.rs s | count | node.memory.rss | userId, cluster, and node | node.memory.rss |
| node.memory.u sage | count | node.memory.us age | userId, cluster, and node | node.memory.usage |
| node.memory.u tilization | count | node.memory.util ization | userId, cluster, and node | node.memory.utilization |
| node.memory.w orking set _ | count | node.memory.wo rking set _ | userId, cluster, and node | node.memory.working set _ |
| node.network.rx errors _ | count | node.network.rx _ errors | userId, cluster, and node | node.network.rx errors _ |
| node.network.rx errors rate _ _ | % | node.network.rx _ errors rate _ | userId, cluster, and node | node.network.rx errors rat _ _ e |

| node.network.rx rate _ | bytes/s | node.network.rx _ rate | userId, cluster, and node | node.network.rx rate _ |
|---|---|---|---|---|
| node.network.tx errors rate _ _ | bytes/s | node.network.tx _ errors rate _ | userId, cluster, and node | node.network.tx errors rat _ _ e |
| node.network.tx rate _ | bytes/s | node.network.tx _ rate | userId, cluster, and node | node.network.tx rate _ |

**pod**

Set **Namespace** to **acs_k8s**. Set **Period** to an integral multiple of **60**. Default value: 60. Unit: seconds.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| pod.cpu.limit | core | pod.cpu.limit | userId, cluster, namespace, type, app, and pod | The maximum amount of CPU resources that can be used by a pod. |
| pod.cpu.oversal e rate _ | % | pod.cpu.oversale rate _ | userId, cluster, namespace, type, app, and pod | The CPU overcommit rate of a pod. |
| pod.cpu.request | core | pod.cpu.request | userId, cluster, namespace, type, app, and pod | The minimum amount of CPU resources requested by a pod. |
| pod.cpu.usage _ rate | core | pod.cpu.usage ra _ te | userId, cluster, namespace, type, app, and pod | The CPU usage of a pod. |
| pod.cpu.utilizati on(usage/limit) | % | pod.cpu.utilizatio n | userId, cluster, namespace, type, app, and pod | The CPU utilization of a pod. |
| pod.filesystem. available | B | pod.filesystem.av ailable | userId, cluster, namespace, type, app, and pod | The available size of the file system in a pod. |
| pod.filesystem.li mit | B | pod.filesystem.li mit | userId, cluster, namespace, type, app, and pod | The maximum size of file systems in a pod. |

| pod.filesystem. usage | bytes | pod.filesystem.us age | userId, cluster, namespace, type, app, and pod | The file system usage of a pod. |
|---|---|---|---|---|
| pod.filesystem. utilization | % | pod.filesystem.uti lization | userId, cluster, namespace, type, app, and pod | The file system utilization of a pod. |
| pod.memory.ca che | B | pod.memory.cac he | userId, cluster, namespace, type, app, and pod | The memory resource cache of a pod. |
| pod.filesystem.li mit | B | pod.filesystem.li mit | userId, cluster, namespace, type, app, and pod | The maximum size of file systems in a pod. |
| pod.memory.lim it | B | pod.memory.limit | userId, cluster, namespace, type, app, and pod | The maximum memory that can be allocated to a pod. |
| pod.memory.ov ersale rate(usa _ ge/request) | % | pod.memory.over sale rate _ | userId, cluster, namespace, type, app, and pod | The memory overcommit rate of a pod. |
| pod.memory.re quest | B | pod.memory.req uest | userId, cluster, namespace, type, app, and pod | The minimum amount of memory resources requested by a pod. |
| pod.memory.rss | B | pod.memory.rss | userId, cluster, namespace, type, app, and pod | The resident set size (RSS) of a pod. |
| pod.memory.uti lization(working set/limit) _ | % | pod.memory.utili zation | userId, cluster, namespace, type, app, and pod | The memory usage of a pod. |
| pod.memory.wo rking set _ | B | pod.memory.wor king set _ | userId, cluster, namespace, type, app, and pod | pod.memory.working set _ |
| pod.network.rx _ errors rate _ | B/s | pod.network.rx e _ rrors rate _ | userId, cluster, namespace, type, app, and pod | The rate at which receive errors occur in the network of a pod. |
| pod.network.rx _ rate | B/s | pod.network.rx r _ ate | userId, cluster, namespace, type, app, and pod | The rate at which a pod receives data. |

| pod.network.tx _ errors rate _ | B/s | pod.network.tx e _ rrors rate _ | userId, cluster, namespace, type, app, and pod | The rate at which send errors occur in the network of a pod. |
|---|---|---|---|---|
| pod.network.tx _ rate | B/s | pod.network.tx r _ ate | userId, cluster, namespace, type, app, and pod | The rate at which a pod sends data. |

**deployment**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| deployment.cpu .limit | core | deployment.cpu.l imit | userId, cluster, namespace, type, and app | The maximum amount of CPU resource that can be allocated to the Deployment. |
| deployment.cpu .usage rate _ | core | deployment.cpu. usage rate _ | userId, cluster, namespace, type, and app | The CPU resources used by the Deployment. |
| deployment.file system.availabl e | B | deployment.filesy stem.available | userId, cluster, namespace, type, and app | The size of the file system available to the Deployment. |
| deployment.file system.limit | B | deployment.filesy stem.limit | userId, cluster, namespace, type, and app | The maximum number of file systems that can be used by the Deployment. |
| deployment.file system.usage | bytes | deployment.filesy stem.usage | userId, cluster, namespace, type, and app | The file system usage of the Deployment. |
| deployment.file system.utilizatio n | % | deployment.filesy stem.utilization | userId, cluster, namespace, type, and app | The file system utilization of the Deployment. |
| deployment.me mory.limit | B | deployment.mem ory.limit | userId, cluster, namespace, type, and app | The maximum size of memory that can be allocated to the Deployment. |
| deployment.me mory.request | B | deployment.mem ory.request | userId, cluster, namespace, type, and app | The minimum amount of memory resources requested by the Deployment. |

| deployment.me mory.working s _ et | B | deployment.mem ory.working set _ | userId, cluster, namespace, type, and app | The working set memory of the Deployment. |
|---|---|---|---|---|
| deployment.net work.rx errors r _ _ ate | B/s | deployment.netw ork.rx errors rate _ _ | userId, cluster, namespace, type, and app | The rate at which receive errors occur in the network of the Deployment. |
| deployment.net work.rx errors r _ _ ate | B/s | deployment.netw ork.rx errors rate _ _ | userId, cluster, namespace, type, and app | The rate at which receive errors occur in the network of the Deployment. |
| deployment.net work.tx errors r _ _ ate | B/s | deployment.netw ork.tx errors rate _ _ | userId, cluster, namespace, type, and app | The rate at which send errors occur in the network of the Deployment. |

#### 3.1.2 ECS

This topic describes the metrics supported by Elastic Compute Service (ECS).

**Basic metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

> **Note:** The metrics described in the following table are collected from the virtual host layer and are slightly different from metrics collected in the operating system.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (ECS) CPU Utilization | % | CPUUtilization | userId and instanceId | The CPU utilization. |
| (ECS)InternetInRa te(Classic Network) | Bit/s | InternetInRate | userId and instanceId | The rate of inbound traffic over the Internet. |
| (ECS)IntranetInRa te | Bit/s | IntranetInRate | userId and instanceId | The rate of inbound traffic over the intranet. |
| (ECS)InternetOut Rate(Classic Network) | Bit/s | InternetOutRate | userId and instanceId | The rate of outbound traffic over the Internet. |

| (ECS)IntranetOut Rate | Bit/s | IntranetOutRate | userId and instanceId | The rate of outbound traffic over the intranet. |
|---|---|---|---|---|
| (ECS)DiskReadBP S | Bytes/s | DiskReadBPS | userId and instanceId | The number of bytes read from all disks per second. |
| (ECS)DiskWriteBP S | Bytes/s | DiskWriteBPS | userId and instanceId | The number of bytes written to all disks per second. |
| (ECS)DiskReadIO PS | Count/s | DiskReadIOPS | userId and instanceId | The number of read I/O operations per second (IOPS) of all disks. |
| (ECS)DiskWriteIO PS | Count/s | DiskWriteIOPS | userId and instanceId | The number of write IOPS of all disks. |

**Operating system-related metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 15. Default value: **15**. Unit: seconds.

> **Note:** To collect operating system-related metrics of ECS instances, you must install a monitoring plug-in.
> To install a monitoring plug-in, perform the following operations: In the left-side navigation pane of the CloudMonitor console, click Cloud Service Monitoring. On the Cloud product monitoring page, click ECS. On the **Host monitoring** page, select the instances that you want to monitor and click **Bulk install or upgrade plug-ins** below the instance list.
> Metric data is displayed in the monitoring chart in 5 to 10 minutes after the monitoring plug-in is installed.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Agent)cpu.total | % | cpu total _ | userId and instanceId | The CPU utilization. |
| (Agent)memory.u sed.utilization | % | memory usedutil _ ization | userId and instanceId | The memory usage. |

| (Agent)load.15m | N/A | load 15m _ | userId and instanceId | The system load in the last 15 minutes. Note This metric is not available for Windows. |
|---|---|---|---|---|
| (Agent)load.1m | N/A | load 1m _ | userId and instanceId | The system load in the last 1 minute. Note This metric is not available for Windows. |
| (Agent)load.5m | N/A | load 5m _ | userId and instanceId | The system load in the last 5 minutes. Note This metric is not available for Windows. |
| Host.diskusage.ut ilization | % | diskusage utiliza _ tion | userId, instanceId, and device | The disk usage. |
| (Agent)fs.inode.u tilization device _ | % | fs inodeutilizatio _ n | userId, instanceId, and device | The inode usage. Note This metric is available only for Linux. |
| (Agent)disk.read. bps device _ | Bytes/s | disk readbytes _ | userId, instanceId, and device | The number of bytes read from the disk per second. |

| (Agent)disk.read.i ops device _ | Count/s | disk readiops _ | userId, instanceId, and device | The number of read IOPS of the disk. |
|---|---|---|---|---|
| (Agent)disk.write. bps device _ | Bytes/s | disk writebytes _ | userId, instanceId, and device | The number of bytes written to the disk per second. |
| (Agent)disk.write. iops device _ | Count/s | disk writeiops _ | userId, instanceId, and device | The number of write IOPS of the disk. |
| (Agent)network.t cp.connection st _ ate | Count | net tcpconnectio _ n | userId, instanceId, and state | The number of TCP connections in each state. |
| (Agent)process.e xpend pid _ | N/A | process.expend | userId, instanceId, name, and pid | The detailed statistical metrics for the top 5 processes. |
| (Agent)process.c ount processnam _ e | Count | process.number | userId, instanceId, and processName | The number of matched processes. |
| io saturation | % | disk io util _ _ | userId, instanceId, and device | The I/O saturation. |
| Agent(zombie pr _ ocess number) _ | Count | zombieProcessNu mber | userId and instanceId | The total number of zombie processes. |
| Agent(total proce _ ss number) _ | Count | totalProcessNum ber | userId and instanceId | The total number of processes. |
| Agent(swap parti _ tion usage) _ | % | swapUtilization | userId and instanceId | The usage of the swap partition. |
| Agent(networkou t drop ratio) _ _ | % | networkout drop _ ratio _ | userId, instanceId, and device | The loss rate of packets that are sent by network interface controllers (NICs). |

| Agent(networkou t error ratio) _ _ | % | networkout error _ ratio _ | userId, instanceId, and device | The sending error rate of NICs. |
|---|---|---|---|---|
| Agent(networkin _ drop ratio) _ | % | networkin drop r _ _ atio | userId, instanceId, and device | The loss rate of packets that are received by NICs. |
| Agent(networkin _ error ratio) _ | % | networkin error r _ _ atio | userId, instanceId, and device | The receiving error rate of NICs. |

**GPU-related metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Agent)gpu.deco der.utilization gp _ uid | % | gpu decoder utili _ _ zation | userId, instanceId, and gpuId | The decoder usage of a GPU. |
| (Agent)gpu.enco der.utilization gp _ uid | % | gpu encoder utili _ _ zation | userId, instanceId, and gpuId | The encoder usage of a GPU. |
| (Agent)gpu.temp erature gpuid _ | °C | gpu gpu temper _ _ ature | userId, instanceId, and gpuId | The GPU temperature. |
| (Agent)gpu.used utilization gpuid _ | % | gpu gpu usedutil _ _ ization | userId, instanceId, and gpuId | The GPU utilization. |
| (Agent)gpu.mem ory.free.space gp _ uid | Bytes | gpu memory fre _ _ espace | userId, instanceId, and gpuId | The idle video memory of a GPU. |
| (Agent)gpu.mem ory.free.utilizatio n gpuid _ | % | gpu memory fre _ _ eutilization | userId, instanceId, and gpuId | The percentage of the idle video memory of a GPU. |

| (Agent)gpu.mem ory.used.space g _ puid | Bytes | gpu memory use _ _ dspace | userId, instanceId, and gpuId | The used video memory of a GPU. |
|---|---|---|---|---|
| gpu memory use _ _ dutilization | % | gpu memory use _ _ dutilization | userId, instanceId, and gpuId | The video memory usage of a GPU. |
| (Agent)gpu.powe r.readingspowerd raw gpuid _ | W | gpu power readi _ _ ngs power draw _ _ | userId, instanceId, and gpuId | The GPU power. |

**Disk-related metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Uni t | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Agent) Percentage of cloud disk usage | % | DiskSerialUsePercent | userId, instanceId, and id serial _ | The percentage of used disk capacity. |

**Network-related metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Inline NIC bandwidth | Bit/s | networkin rate avs _ _ | userId and instanceId | The number of bits that the NIC receives per second. |
| Outgoing NIC bandwidth | Bit/s | networkout rate avs _ _ | userId and instanceId | The number of bits that the NIC sends per second. |

| Number of network card incoming packets | Count/s | networkin packages _ avs _ | userId and instanceId | The number of packets that the NIC receives per second. |
|---|---|---|---|---|
| Number of outgoing network card packets | Count/s | networkout package _ s avs _ | userId and instanceId | The number of packets that the NIC sends per second. |
| Number of packets with network card inbound error | Count/s | networkin errorpack _ ages avs _ | userId and instanceId | The number of error packets that the NIC receives per second. |
| Network card outbound error packets | Count/s | networkout errorpac _ kages avs _ | userId and instanceId | The number of error packets that the NIC sends per second. |
| Number of network connections | Count | net tcpconnection a _ _ vs | userId and instanceId | The number of connections. |
| Enter VPC- broadband | Bit/s | VPC PublicTP Intern _ _ etInRate | userId and instanceId | The number of bits that the virtual private cloud (VPC) receives per second. |
| Outbound VPC- broadband | Bit/s | VPC PublicTP Intern _ _ etOutRate | userId and instanceId | The number of bits that the VPC sends per second. |
| ipv6 packet bit | Bit | ipv6 tx bytes sum _ _ _ | userId and instanceId | The number of bits of an outbound IPv6 packet. |
| ipv6 packet receiving bits | Bit | ipv6 rx bytes sum _ _ _ | userId and instanceId | The number of bits of an inbound IPv6 packet. |
| Number of ipv6 packages | Count | ipv6 tx packets su _ _ _ m | userId and instanceId | The number of outbound IPv6 packets. |

| Number of ipv6 packets received | Count | ipv6 rx packets su _ _ _ m | userId and instanceId | The number of inbound IPv6 packets. |
|---|---|---|---|---|
| Number of packets lost to ipv6 outbound security group | Count | ipv6 tx acl error su _ _ _ _ m | userId and instanceId | The number of outbound IPv6 packets dropped from the security group. |
| Number of packets lost to the security group in the direction of ipv6 | Count | ipv6 rx acl error su _ _ _ _ m | userId and instanceId | The number of inbound IPv6 packets dropped from the security group. |
| North-south traffic ipv6 statistics contract number | Count | ipv6 tx igw packets _ _ _ avg _ | userId and instanceId | The number of IPv6 packets that are sent in the north-south traffic. |
| North-south traffic ipv6 statistics number of packets received | Count | ipv6 rx igw packets _ _ _ avg _ | userId and instanceId | The number of IPv6 packets that are received in the north-south traffic. |
| North-South Traffic ipv6 Statistics Packet Bits | Bit/s | ipv6 tx igw bytes a _ _ _ _ vg | userId and instanceId | The number of bits of IPv6 packets that are sent per second in the north- south traffic. |
| North-South Traffic ipv6 Statistics Packet Receiving Bits | Bit/s | ipv6 rx igw bytes a _ _ _ _ vg | userId and instanceId | The number of bits of IPv6 packets that are received per second in the north-south traffic. |

#### 3.1.3 BMCP nodes

This topic describes the metrics for nodes in the Bare Metal Computing Power (BMCP) platform. Set the **Namespace** parameter to **acs_bms**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| NODE CPU USA _ _ GE | % | NODE CPU USAG _ _ E | instanceId | The CPU utilization. |
| NODE MEM US _ _ AGE | % | NODE MEM USA _ _ GE | instanceId | The memory usage. |
| NODE DISK US _ _ AGE | % | NODE DISK USA _ _ GE | instanceId | The disk usage. |
| NODE LOAD1 _ | value | NODE LOAD1 _ | instanceId | The system load in the last minute. |
| NODE LOAD5 _ | value | NODE LOAD5 _ | instanceId | The system load in the last 5 minutes. |
| NODE LOAD15 _ | value | NODE LOAD15 _ | instanceId | The system load in the last 15 minutes. |
| TCP ESTAB _ | Count | TCP ESTAB _ | instanceId | The number of TCP connections. |
| NETWORK RX _ | MB/s | NETWORK RX _ | instanceId | The outbound bandwidth. |
| NETWORK TX _ | MB/s | NETWORK TX _ | instanceId | The inbound bandwidth. |

**GPU-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| GPU TEMP _ | °C | GPU TEMP _ | instanceId | The GPU temperature. |
| GPU POWER US _ _ AGE | W | GPU POWER USA _ _ GE | instanceId | The GPU power. |
| GPU USAGE _ | % | GPU USAGE _ | instanceId | The GPU utilization. |
| GPU ENC USAG _ _ E | % | GPU ENC USAGE _ _ | instanceId | The encoder utilization of the GPU. |

| GPU DEC USAG _ _ E | % | GPU DEC USAGE _ _ | instanceId | The decoder utilization of the GPU. |
|---|---|---|---|---|
| GPU FB USAGE _ _ | % | GPU FB USAGE _ _ | instanceId | The memory usage of the GPU frame buffer. |
| GPU SM CLOCK _ _ | MHz | GPU SM CLOCK _ _ | instanceId | The frequency of the GPU Streaming Multiprocessor (SM) clock. |
| GPU MEM CLOC _ _ K | MHz | GPU MEM CLOCK _ _ | instanceId | The frequency of the GPU memory clock. |

**RDMA-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| rdma tx bytes _ _ | MB/s | rdma tx bytes _ _ | instanceId | The throughput sent over the Remote Direct Memory Access (RDMA) network. |
| rdma rx bytes _ _ | MB/s | rdma rx bytes _ _ | instanceId | The throughput received over the RDMA network. |
| rdma out of bu _ _ _ ffer | Count | rdma out of buff _ _ _ er | instanceId | The number of buffer overflows that occur in the RDMA network. |
| rdma out of se _ _ _ q | Count | rdma out of seq _ _ _ | instanceId | The number of out-of-order packets in the RDMA network. |
| rdma cqe error _ _ | Count | rdma cqe error _ _ | instanceId | The number of local completion queue entries (CQEs) with errors in the RDMA network. |
| rdma service m _ _ onitor rnr nak r _ _ _ etry err _ | Count | rdma service mo _ _ nitor rnr nak retr _ _ _ y err _ | instanceId | The number of Receiver Not Ready (RNR) Negative Acknowledgment (NAK) packets sent from the peer. |

#### 3.1.4 BMCP containers

This topic describes the metrics for containers in the Bare Metal Computing Power (BMCP) platform. Set the **Namespace** parameter to **acs_bmcp**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| NODE CPU USA _ _ GE | % | NODE CPU USAG _ _ E | instanceId | The CPU utilization. |
| NODE MEM US _ _ AGE | % | NODE MEM USA _ _ GE | instanceId | The memory usage. |
| NODE DISK US _ _ AGE | % | NODE DISK USA _ _ GE | instanceId | The disk usage. |
| NODE LOAD1 _ | Value | NODE LOAD1 _ | instanceId | The system load in the last minute. |
| NODE LOAD5 _ | Value | NODE LOAD5 _ | instanceId | The system load in the last 5 minutes. |
| NODE LOAD15 _ | Value | NODE LOAD15 _ | instanceId | The system load in the last 15 minutes. |
| TCP ESTAB _ | Count | TCP ESTAB _ | instanceId | The number of TCP connections. |
| NETWORK RX _ | MB/s | NETWORK RX _ | instanceId | The outbound bandwidth. |
| NETWORK TX _ | MB/s | NETWORK TX _ | instanceId | The inbound bandwidth. |

**GPU-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| GPU TEMP _ | °C | GPU TEMP _ | instanceId | The GPU temperature. |
| GPU POWER US _ _ AGE | W | GPU POWER USA _ _ GE | instanceId | The GPU power. |

| GPU USAGE _ | % | GPU USAGE _ | instanceId | The GPU utilization. |
|---|---|---|---|---|
| GPU ENC USAG _ _ E | % | GPU ENC USAGE _ _ | instanceId | The encoder utilization of the GPU. |
| GPU DEC USAG _ _ E | % | GPU DEC USAGE _ _ | instanceId | The decoder utilization of the GPU. |
| GPU FB USAGE _ _ | % | GPU FB USAGE _ _ | instanceId | The memory usage of the GPU frame buffer. |

**RDMA-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| rdma tx bytes _ _ | MB/s | rdma tx bytes _ _ | instanceId | The throughput sent over the Remote Direct Memory Access (RDMA) network. |
| rdma rx bytes _ _ | MB/s | rdma rx bytes _ _ | instanceId | The throughput received over the RDMA network. |
| rdma out of bu _ _ _ ffer | Count | rdma out of buff _ _ _ er | instanceId | The number of buffer overflows that occur in the RDMA network. |
| rdma out of se _ _ _ q | Count | rdma out of seq _ _ _ | instanceId | The number of out-of-order packets in the RDMA network. |
| rdma cqe error _ _ | Count | rdma cqe error _ _ | instanceId | The number of local completion queue entries (CQEs) with errors in the RDMA network. |
| rdma service m _ _ onitor rnr nak r _ _ _ etry err _ | Count | rdma service mo _ _ nitor rnr nak retr _ _ _ y err _ | instanceId | The number of Receiver Not Ready (RNR) Negative Acknowledgment (NAK) packets sent from the peer. |

#### 3.1.5 Bare Metal Computing Platform (BMCP) (Container - Intelligent Computing Cluster)

**(Container - Intelligent Computing Cluster)**

This topic describes the metrics for the Bare Metal Computing Platform (BMCP) (Container - Intelligent Computing Cluster). The **Namespace** is **acs_bmcp_ack**. The default **Period** is **60** seconds and can be set to any integer multiple of 60.

**Infrastructure monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| CPU utilization | % | NODE CPU USAG _ _ E | instanceId,userId | The CPU utilization. |
| Memory usage | % | NODE MEM USA _ _ GE | instanceId,userId | The memory usage. |
| Disk usage | % | NODE DISK USA _ _ GE | instanceId,userId | The disk usage. |
| System load 1 | value | NODE LOAD1 _ | instanceId,userId | The 1-minute average system load. |
| System load 5 | value | NODE LOAD5 _ | instanceId,userId | The 5-minute average system load. |
| System load 15 | value | NODE LOAD15 _ | instanceId,userId | The 15-minute average system load. |
| TCP connections | count | TCP ESTAB _ | instanceId,userId | The number of TCP connections. |
| Download bandwidth | MB/s | NETWORK RX _ | instanceId,userId | The download bandwidth. |
| Inbound bandwidth | MB/s | NETWORK TX _ | instanceId,userId | Inbound network bandwidth |

**GPU monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| GPU temperature | ° | GPU TEMP _ | instanceId,userId,g pu | The GPU temperature. |
| GPU power | W | GPU POWER USA _ _ GE | instanceId,userId,g pu | The GPU power usage. |

| GPU utilization | % | GPU USAGE _ | instanceId,userId,g pu | The GPU utilization. |
|---|---|---|---|---|
| GPU encoder utilization | % | GPU ENC USAGE _ _ | instanceId,userId,g pu | The GPU encoder utilization. |
| GPU decoder utilization | % | GPU DEC USAGE _ _ | instanceId,userId,g pu | The GPU decoder utilization. |
| GPU framebuffer usage | % | GPU FB USAGE _ _ | instanceId,userId | The GPU framebuffer usage. |

**RDMA monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| RDMA network send throughput | MB/s | rdma tx bytes _ _ | instanceId,minor,u serId | The RDMA network send throughput. |
| RDMA network receive throughput | MB/s | rdma rx bytes _ _ | instanceId,minor,u serId | The RDMA network receive throughput. |
| RDMA network buffer overflows | count | rdma out of buff _ _ _ er | instanceId,minor,u serId | The number of RDMA network buffer overflows. |
| RDMA network out-of-sequence datagrams | count | rdma out of seq _ _ _ | instanceId,minor,u serId | The number of out-of- sequence RDMA network datagrams. |
| RDMA local CQE errors | count | rdma cqe error _ _ | instanceId,minor,u serId | The number of local RDMA CQE errors. |
| Peer RNR NAK packets | count | rdma service mo _ _ nitor rnr nak retr _ _ _ y err _ | instanceId,minor,u serId | The number of peer RNR NAK packets. |

**Aspeed monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|

| Requests per second (QPS) | counts/ s | asllm num reque _ _ sts total _ | instanceId | The number of requests per second (QPS). |
|---|---|---|---|---|
| End-to-end latency | s | e2e request late _ _ ncy | instanceId,userId,instan ce name _ | The end-to-end latency. |
| Initial delay | s | time to first toke _ _ _ n | instanceId,userId,instan ce name _ | Initial delay. |
| Inter-token latency | s | inter token laten _ _ cy | instanceId,userId,instan ce name _ | The inter-token latency. |
| In-flight requests | count | num running req _ _ s | instanceId,userId,instan ce name _ | The number of in- flight requests. |
| Queued requests | count | num queue reqs _ _ | instanceId,userId,instan ce name _ | The number of queued requests. |
| Average prompt length | tokens | prompt tokens _ | instanceId,userId,instan ce name _ | The average prompt length. |
| Prefix cache hit ratio | % | cache hit rate _ _ | instanceId,userId,instan ce name _ | The prefix cache hit ratio. |
| Average generation length | tokens | generation token _ s | instanceId,userId,instan ce name _ | The average generation length. |
| Generation throughput | tokens/ s | gen throughput _ | instanceId,userId,instan ce name _ | The generation throughput. |
| KV cache usage | % | token usage _ | instanceId,userId,instan ce name _ | The KV cache usage. |

**Aspeed control plane monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| API requests per second (QPS) | counts/ s | aspeed asllm nu _ _ m requests total _ _ | instanceId,userId,in stance name _ | The number of API requests per second (QPS). |
| API end-to-end latency | s | aspeed apiserver _ request duration _ _ | instanceId,api | The API end-to-end latency. |

| API request success rate | % | aspeed apiserver _ requests succes _ _ s | instanceId,api | The API request success rate. |
|---|---|---|---|---|
| Total failed API workflows | count | aspeed apiserver _ workflow start f _ _ _ ailures total _ | instanceId,api | The total number of failed API workflows. |

#### 3.1.6 Bare Metal Computing Platform (BMCP)

This topic describes the metrics for Bare Metal Computing Platform (BMCP) (Bare Metal - Supercomputing Cluster). The **namespace** for these metrics is **acs_bmcp**. The default **period** is **60** seconds and can be set to any integer multiple of 60.

| Metric | Unit | Metric name | Dimensions | Description |
|---|---|---|---|---|
| CPU utilization | Percent | NODE CPU USAGE _ _ | instanceId,userId | The percentage of CPU resources in use. |
| Memory utilization | Percent | NODE MEM USAGE _ _ | instanceId,userId | The percentage of memory in use. |
| Disk utilization | Percent | NODE DISK USAGE _ _ | instanceId,userId | The percentage of disk space in use. |
| System load (load1) | Count | NODE LOAD1 _ | instanceId,userId | The average system load over the past minute. |
| System load (load5) | Count | NODE LOAD5 _ | instanceId,userId | The average system load over the past 5 minutes. |
| System load (load15) | Count | NODE LOAD15 _ | instanceId,userId | The average system load over the past 15 minutes. |
| Number of TCP connections | Count | TCP ESTAB _ | instanceId,userId | The number of TCP connections in the ESTABLISHED state. |

| Inbound network bandwidth | MB/s | NETWORK RX _ | instanceId,userId | The rate of incoming network traffic to the instance. |
|---|---|---|---|---|
| Outbound network bandwidth | MB/s | NETWORK TX _ | instanceId,userId | The rate of outgoing network traffic from the instance. |

#### 3.1.7 Bare Metal Management (BMS)

This topic describes the monitoring metrics for Bare Machine Service (BMS). The **Namespace** is **acs_cgw_bms**. The **Period** defaults to **60** seconds and can also be any multiple of 60.

**Infrastructure monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| CPU utilization | % | NODE CPU USAGE _ _ | instanceId,userId | The CPU utilization. |
| Memory usage | % | NODE MEM USAGE _ _ | instanceId,userId | The memory usage. |
| Disk usage | % | NODE DISK USAGE _ _ | instanceId,userId | The disk usage. |
| System load (1- minute average) | value | NODE LOAD1 _ | instanceId,userId | The 1-minute system load average. |
| System load (5- minute average) | value | NODE LOAD5 _ | instanceId,userId | The 5-minute system load average. |
| System load (15- minute average) | value | NODE LOAD15 _ | instanceId,userId | The 15-minute system load average. |
| TCP connections | counts | TCP ESTAB _ | instanceId,userId | The number of TCP connections. |
| Inbound bandwidth | MB/s | NETWORK RX _ | instanceId,userId | The inbound bandwidth. |

| Inbound bandwidth | MB/s | NETWORK TX _ | instanceId,userId | Inbound network bandwidth |
|---|---|---|---|---|

**GPU monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| GPU temperature | ° | GPU TEMP _ | instanceId,userId,gpu | The GPU temperature. |
| GPU power usage | W | GPU POWER USAGE _ _ | instanceId,userId,gpu | The GPU power usage. |
| GPU utilization | % | GPU USAGE _ | instanceId,userId,gpu | The GPU utilization. |
| GPU encoder utilization | % | GPU ENC USAGE _ _ | instanceId,userId,gpu | The GPU encoder utilization. |
| GPU decoder utilization | % | GPU DEC USAGE _ _ | instanceId,userId,gpu | The GPU decoder utilization. |
| GPU framebuffer usage | % | GPU FB USAGE _ _ | instanceId,userId,gpu | The GPU framebuffer usage. |
| GPU SM clock frequency | MHz | GPU SM CLOCK _ _ | instanceId,userId,gpu | The GPU Streaming Multiprocessor (SM) clock frequency. |
| GPU memory clock frequency | MHz | GPU MEM CLOCK _ _ | instanceId,userId,gpu | The GPU memory clock frequency. |

### 3.2 Database services

#### 3.2.1 ApsaraDB RDS

This topic describes the metrics supported by ApsaraDB RDS. By default, an old link is used for ApsaraDB RDS. The period of data collection is 60 to 300 seconds. Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of 60 in the range of 60 to 300). Default value: **60**. Unit: seconds. ApsaraDB RDS supports four types of engines: MySQL, SQL Server, PolarDB O, and PostgreSQL.

**ApsaraDB RDS for MySQL**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUtilization | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage. |
| NetworkInRate | Bit/s | MySQL NetworkI _ nNew | userId and instanceId | The inbound traffic to the ApsaraDB RDS for MySQL instance per second. |
| NetworkOutRate | Bit/s | MySQL NetworkO _ utNew | userId and instanceId | The outbound traffic from the ApsaraDB RDS for MySQL instance per second. |
| MySQL QPS _ | Count/s | MySQL QPS _ | userId and instanceId | The number of queries per second (QPS) for the ApsaraDB RDS for MySQL instance. |
| Docker Cpu Usage | % | DockerCpuUsage | userId and instanceId | The CPU utilization of the Docker container. |

**ApsaraDB RDS for SQL Server**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUtilization | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| NetworkInRate | Bit/s | SQLServer Netw _ orkInNew | userId and instanceId | The inbound traffic to the ApsaraDB RDS for SQL Server instance per second. |
| NetworkOutRate | Bit/s | SQLServer Netw _ orkOutNew | userId and instanceId | The outbound traffic from the ApsaraDB RDS for SQL Server instance per second. |

**ApsaraDB RDS for PolarDB O**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |

| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
|---|---|---|---|---|
| IOPSUtilization | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage. |

**ApsaraDB RDS for PostgreSQL**

**ApsaraDB RDS for PostgreSQL instances that use local SSDs**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsag e | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUtilization | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage. |

**ApsaraDB RDS for PostgreSQL instances that use cloud disks**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Average active connections per CPU PG cloud _ disk | Count | ActiveConnectio ns | userId and instanceId | The average number of active connections per CPU. |
| Inode Usage PG _ Disk | % | InodeUsage | userId and instanceId | The inode usage. |

| Read-only synchronization delay PG cloud _ disk | Seconds | ReadLag | userId and instanceId | The synchronization latency of the read-only instance. |
|---|---|---|---|---|
| Database Age PG Disk _ | xids | DBAge | userId and instanceId | The age of the database. |
| Read-only Stream replication state pg cloud _ disk | Value | StreamingStatus | userId and instanceId | The stream replication status of the read-only instance. Valid values: 0: disconnected. 1: normal. |
| Pg connection _ usage | % | conn usage _ | userId and instanceId | The connection utilization. |
| PG CPU usage _ | % | cpu usage _ | userId and instanceId | The CPU utilization. |
| PG IOPS usage _ | % | iops usage _ | userId and instanceId | The IOPS usage. |
| Pg disk space _ usage | % | local fs size usa _ _ _ ge | userId and instanceId | The disk usage. |
| PG Memory _ Usage | % | mem usage _ | userId and instanceId | The memory usage. |

#### 3.2.2 ApsaraDB RDS (New)

This topic describes the metrics supported by ApsaraDB RDS (New). ApsaraDB RDS supports a new link. Data is collected at 60-second intervals. Set the **Namespace** parameter to **acs_rds_dashboard**. The default value of the **Period** parameter is **60**. Unit: seconds. ApsaraDB RDS (New) supports three types of engines: MySQL, PolarDB O, and PostgreSQL.

**ApsaraDB RDS for MySQL**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| Connection Usage (New) | % | ConnectionUsage new _ | userId and instanceId | The connection utilization. |
|---|---|---|---|---|
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory usage (new) | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |
| MySQL Network inflow bandwidth (new) | Bit/s | MySQL NetworkI _ nNew new _ | userId and instanceId | The inbound traffic to the ApsaraDB RDS for MySQL instance per second. |
| MySQL Network outflow bandwidth (new) | Bit/s | MySQL NetworkO _ utNew new _ | userId and instanceId | The outbound traffic from the ApsaraDB RDS for MySQL instance per second. |
| MySQL queries per second (new) | Count/s | MySQL QPS new _ _ | userId and instanceId | The number of queries per second (QPS) for the ApsaraDB RDS for MySQL instance. |
| DataDelay | Seconds | DataDelay | userId and instanceId | The latency between primary and secondary instances. |
| RWDelay (New) | Seconds | RWDelay | userId, instanceId, and slave | The read and write latency. |
| ThreadsConnecte d | Count | ThreadsConnecte d | userId and instanceId | The number of thread connections. |

| Developer Guide·Met | rics |   |   | CloudMonito |
|---|---|---|---|---|

| ThreadsRunning | Count | ThreadsRunning | userId and instanceId | The number of active threads. |
|---|---|---|---|---|
| SlowQueriesPs | Count | SlowQueriesPs | userId and instanceId | The number of slow QPS. |
| Total Wait Time for Row Locks (New) | Milliseconds | InnodbRowLockW aits | userId and instanceId | The total wait time for row locks. |
| Average Wait Time for Row Locks (New) | Milliseconds | InnodbRowLockTi meAvg | userId and instanceId | The average wait time for row locks. |
| Row Lock Waits (New) | Count | InnodbRowLockW aits | userId and instanceId | The number of wait times for row locks. |
| Total Number of Connections (New) | Count | TotalConnections | userId and instanceId | The total number of connections. |

**ApsaraDB RDS for PolarDB O**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage new _ | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |

| Memory usage (new) | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |
|---|---|---|---|---|
| PPAS Primary/Standby Disconnect | Count | PPAS Replication _ Num | userId and instanceId | The number of disconnections between primary and secondary ApsaraDB RDS for PPAS instances. |
| PPAS primary/standby delay | Seconds | PPAS Replication _ Lag | userId and instanceId | The latency between primary and secondary ApsaraDB RDS for PPAS instances. |

**ApsaraDB RDS for PostgreSQL**

**ApsaraDB RDS for PostgreSQL instances that use local SSDs**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsag e new _ | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory usage (new) | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |
| PG primary/standby disconnection | Count | PG ReplicationN _ um | userId and instanceId | The number of connections between primary and secondary ApsaraDB RDS for PostgreSQL instances. |

| PG primary/standby delay | Seconds | PG ReplicationLa _ g | userId and instanceId | The latency between primary and secondary ApsaraDB RDS for PostgreSQL instances. |
|---|---|---|---|---|

**ApsaraDB RDS for PostgreSQL instances that use cloud disks**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Average number of active connections per CPU PG cloud _ disk (new) | Count | ActiveConnectio ns new _ | userId and instanceId | The average number of active connections per CPU. |
| Pg connection _ usage | % | conn usage _ | userId and instanceId | The connection utilization. |
| PG CPU usage _ | % | cpu usage _ | userId and instanceId | The CPU utilization. |
| PG IOPS usage _ | % | iops usage _ | userId and instanceId | The IOPS usage. |
| INODE usage PG _ cloud disk (new) | % | InodeUsage new _ | userId and instanceId | The inode usage. |
| Pg disk space _ usage | % | local fs size usa _ _ _ ge | userId and instanceId | The disk usage. |
| PG Memory _ Usage | % | mem usage _ | userId and instanceId | The memory usage. |
| Read-only synchronization delay PG cloud _ disk (new) | Seconds | ReadLag new _ | userId and instanceId | The synchronization latency of the read-only instance. |
| Database age PG cloud _ disk (new) | xids | DBAge new _ | userId and instanceId | The age of the database. |

| Read-only Stream Copy Status PG Cloud _ Disk (New) | Value | StreamingStatus new _ | userId and instanceId | The streaming replication status of the read-only instance. |
|---|---|---|---|---|
| Number of Primary/Seconda ry Connections (Value 0 indicates disconnected. Value 1 indicates connected.) | Count | PG ESSD Replic _ _ ationNum | userId and instanceId | The number of connections between primary and secondary ApsaraDB RDS for PostgreSQL instances. |
| PG cloud disk primary/sta _ ndby delay | Seconds | PG ESSD Replic _ _ ationLag | userId and instanceId | The latency between primary and secondary ApsaraDB RDS for PostgreSQL instances. |

#### 3.2.3 PolarDB

This topic describes the metrics supported by PolarDB. Set the **Namespace** paramter to **acs_polardb_dashboard**. Set the **Period** paramter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**PolarDB for MySQL**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (PolarDB-M) Connection Usage | % | ConnectionUsa ge new _ | userId and instanceId | The connection utilization. |
| (PolarDB-M) CPU usage | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| (PolarDB-M) Memory Usage | % | MemoryUsage _ new | userId and instanceId | The memory usage. |
| Number of active connections | Count | Active Session _ new _ | userId and instanceId | The number of active connections. |

| Storage Engine IO throughput per second | Count/s | Iops throughou _ t new _ | userId and instanceId | The I/O throughput of the storage engine per second. |
|---|---|---|---|---|
| Storage engine IO times per second | Count/s | Mps new _ | userId and instanceId | The number of I/O operations of the storage engine per second. |
| IO times per second | Count/s | DataIo Ps new _ _ | userId and instanceId | The number of I/O operations per second. |
| Queries Ps new _ _ | Count/s | Queries Ps ne _ _ w | userId and instanceId | The number of queries per second (QPS). |
| Slow queries per second | Count/s | SlowQueries Ps _ new _ | userId and instanceId | The number of slow queries per second. |
| TPS | Count/s | Tps M _ | userId and instanceId | The number of transactions per second (TPS). |

**PolarDB O**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (PolarDB-O)TPS | Count/s | Tps O _ | userId and instanceId | The TPS. |
| (PolarDB-O) database CPU usage | % | Cgroup Cpu To _ _ tal | userId and instanceId | The CPU utilization of the database. |
| Cgroup Mem Usage _ _ | % | Cgroup Mem U _ _ sage | userId and instanceId | The memory usage of the database. |
| (PolarDB-O) Connection Usage | % | Connection Rati _ o | userId and instanceId | The connection utilization. |
| (PolarDB-O) Connections | Count | Connections O _ | userId and instanceId | The number of connections. |
| (PolarDB-O) Active Connections | Count | Active Connecti _ ons | userId and instanceId | The number of active connections. |

| (PolarDB-O)PFS reads IOPS | Count | Pfsd Read Iops _ _ | userId and instanceId | The read IOPS of the Polar file system (PFS). |
|---|---|---|---|---|
| (PolarDB-O)PFS writes IOPS | Count | Pfsd Write Iops _ _ | userId and instanceId | The write IOPS of the PFS. |
| (PolarDB-O) Database Age | Count | Db Age _ | userId and instanceId | The age of the database. |
| (PolarDB-O) Local Disk Usage | % | Local Disk Usa _ _ ge | userId and instanceId | The local disk usage. |

#### 3.2.4 PolarDB databases that use local SSDs

This topic describes the metrics supported by PolarDB databases that use local SSDs. Set the **Namespace** parameter to **acs_polardblocal**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**PolarDB for MySQL**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsag e new _ | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The IOPS usage. |
| Memory usage (new) | % | MemoryUsage _ new | userId and instanceId | The memory usage. |
| MySQL Network inflow bandwidth (new) | Bit/s | MySQL Network _ InNew new _ | userId and instanceId | The inbound traffic to the PolarDB for MySQL instance per second. |

| MySQL Network outflow bandwidth (new) | Bit/s | MySQL Network _ OutNew new _ | userId and instanceId | The outbound traffic from the PolarDB for MySQL instance per second. |
|---|---|---|---|---|
| MySQL queries per second (new) | Count/s | MySQL QPS ne _ _ w | userId and instanceId | The number of queries per second for the PolarDB for MySQL instance. |
| DataDelay | Seconds | DataDelay | userId and instanceId | The latency between primary and secondary instances. |
| RWDelay (New) | Seconds | RWDelay | userId, instanceId, and slave | The read and write latency. |
| Threads Connected | Count | ThreadsConnect ed | userId and instanceId | The number of thread connections. |
| ThreadsRunning | Count | ThreadsRunning | userId and instanceId | The number of active threads. |
| SlowQueriesPs | Count | SlowQueriesPs | userId and instanceId | The number of slow queries per second (QPS). |
| Total Wait Time for Row Locks (New) | Millisecon ds | InnodbRowLock Time | userId and instanceId | The total wait time for row locks. |
| Average Wait Time for Row Locks (New) | Millisecon ds | InnodbRowLock TimeAvg | userId and instanceId | The average wait time for row locks. |
| Row Lock Waits (New) | Count | InnodbRowLock Waits | userId and instanceId | The number of wait times for row locks. |
| Total Number of Connections (New) | Count | TotalConnection s | userId and instanceId | The total number of connections. |
| Average number of active MySQL connections | Count/s | MySQL ActiveS _ ession | userId and instanceId | The average number of active connections to the PolarDB for MySQL instance. |
| Innodb row lock cur _ _ _ rent waits _ | Count | Innodb row loc _ _ k current waits _ _ | userId and instanceId | The number of sessions waiting for row locks. |

| mdl lock session _ _ | Count | mdl lock sessio _ _ n | userId and instanceId | The number of connections blocked by the MDL lock. |
|---|---|---|---|---|
| lock deadlocks _ | Count | lock deadlocks _ | userId and instanceId | The number of deadlocks. |

**PolarDB for Oracle and PolarDB for PostgreSQL**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsa ge new _ | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage ne _ w | userId and instanceId | The IOPS usage. |
| Memory usage (new) | % | MemoryUsage _ new | userId and instanceId | The memory usage. |
| PPAS Primary/Standby Disconnect | Count | PPAS Replicatio _ nNum | userId and instanceId | The number of disconnections between primary and secondary ApsaraDB RDS for PPAS instances. |
| PPAS primary/standby delay | Seconds | PPAS Replicatio _ nLag | userId and instanceId | The latency between primary and secondary ApsaraDB RDS for PPAS instances. |
| PG ActiveConnectio _ nsPerCpu | Count | PG ActiveConn _ ectionsPerCpu | userId and instanceId | The average number of active connections per core to the PolarDB for Oracle Enterprise Edition database that uses local disks. |

| PG Database age _ | xids | PG DBAge _ | userId and instanceId | The age of the PolarDB for Oracle Enterprise Edition database that uses local SSDs. |
|---|---|---|---|---|
| PG SwellTime _ | Seconds | PG SwellTime _ | userId and instanceId | The period during which the PolarDB for Oracle Enterprise Edition database that uses local SSDs experiences storage bloat. |
| PG CheckpointLaten _ cyMB | MB | PG Checkpoint _ LatencyMB | userId and instanceId | The size of data written to the PolarDB for Oracle Enterprise Edition database that uses local SSDs with a delay during a checkpoint process. |
| PG InactiveSlots _ | Count | PG InactiveSlot _ s | userId and instanceId | The number of times that the replication slot is disconnected in the PolarDB for Oracle Enterprise Edition database that uses local SSDs. |
| PG ReplayLatencyIn _ MB | MB | PG ReplayLate _ ncyInMB | userId and instanceId | The size of data written to the PolarDB for Oracle Enterprise Edition database that uses local SSDs with a delay. |

#### 3.2.5 PolarDB-X 2.0

##### 3.2.5.1 Compute nodes of PolarDB-X 2.0

This topic describes the metrics for the compute nodes of PolarDB-X 2.0. Set the **Namespace** parameter to **acs_drds**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU usage | % | CPUUtilization | userId and instanceId | The CPU utilization. |

| Number of connections | Count | ConnectionCount | userId and instanceId | The total number of sessions. |
|---|---|---|---|---|
| Average number of logical requests per second | Count | LogicQPS | userId and instanceId | The number of requests per second. |
| Average Logical Response Time | Millisec onds | LogicRT | userId and instanceId | The average response time of logical requests. |
| Memory Usage | % | MemoryUtilization | userId and instanceId | The memory usage. |
| Network input | Bit/s | NetworkInputTraffi c | userId and instanceId | The inbound bandwidth. |
| Network output | Bit/s | NetworkOutputTra ffic | userId and instanceId | The outbound bandwidth. |
| Average number of physical requests per second | Count | PhysicsQPS | userId and instanceId | The physical queries per second (QPS). |
| Average Physical Response Time | Millisec onds | PhysicsRT | userId and instanceId | The physical response time. |
| Number of active sessions | Count | ThreadCount | userId and instanceId | The number of active threads. |
| Heap memory usage | % | HeapMemoryUsag e | userId and instanceId | The heap memory usage. |
| Log directory size | Bytes | LogSize | userId and instanceId | The size of the log directory. |
| Number of errors per second | Count | SecondErrorCount | userId and instanceId | The number of errors per second. |
| Physical slow SQL per second | Count | SecondPhysicalSql Count | userId and instanceId | The number of physical slow SQL QPS. |
| Slow requests per second | Count | SecondRequestCo unt | userId and instanceId | The number of slow queries per second. |

| spill directory size | Bytes | SpillSize | userId and instanceId | The size of the spill directory. |
|---|---|---|---|---|
| Temporary directory size | Bytes | TmpSize | userId and instanceId | The size of the temporary directory. |

##### 3.2.5.2 Data nodes of PolarDB-X 2.0

This topic describes the metrics for the data nodes of PolarDB-X 2.0. Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of 60 in the range of 60 to 300. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage n _ ew | userId and instanceId | The connection utilization. |
| CPU Utilization (New) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk Usage (New) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS Usage (New) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory Utilization (New) | % | MemoryUsage new _ | userId and instanceId | The memory usage. |
| Inbound Bandwidth of an ApsaraDB RDS for MySQL Instance (New) | Bit/s | MySQL NetworkInN _ ew new _ | userId and instanceId | The inbound traffic to the MySQL data node per second. |
| Outbound Bandwidth of an ApsaraDB RDS for MySQL Instance (New) | Bit/s | MySQL NetworkOut _ New new _ | userId and instanceId | The outbound traffic from the MySQL data node per second. |
| QPS of an ApsaraDB RDS for MySQL Instance (New) | Count/ s | MySQL QPS new _ _ | userId and instanceId | The number of queries per second (QPS) on the MySQL data node. |

#### 3.2.6 ApsaraDB for MongoDB (Old)

This topic describes the metrics supported by ApsaraDB for MongoDB (Old). Set the **Namespace** parameter to **acs_mongodb**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | MetricName | Dimension | Description |
|---|---|---|---|---|
| CPU Utilization | % | CPUUtilization | userId, instanceId, and role | The CPU utilization. |
| MemoryUtilizatio n | % | MemoryUtilizatio n | userId, instanceId, and role | The memory usage. |
| DiskUtilization | % | DiskUtilization | userId, instanceId, and role | The disk usage. |
| IOPSUtilization | % | IOPSUtilization | userId, instanceId, and role | The IOPS usage. |
| Connection Usage | % | ConnectionUtiliza tion | userId, instanceId, and role | The connection utilization. |
| QPS | Count | QPS | userId, instanceId, and role | The number of queries per second (QPS). |
| UsedConnections | Count | ConnectionAmou nt | userId, instanceId, and role | The number of used connections. |

**Disk capacity-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| InstanceUsedDisk Space | Bytes | InstanceDiskAmo unt | userId, instanceId, and role | The disk space occupied by the instance. |

| LogUsedDiskSpac e | Bytes | DataDiskAmount | userId, instanceId, and role | The disk space occupied by data. |
|---|---|---|---|---|
| Disk Space Occupied by Logs | Bytes | LogDiskAmount | userId, instanceId, and role | The disk space occupied by logs. |

**Network request-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| IntranetIn | Bytes | IntranetIn | userId, instanceId, and role | The inbound traffic over the intranet. |
| IntranetOut | Bytes | IntranetOut | userId, instanceId, and role | The outbound traffic over the intranet. |
| Requests | Count | NumberRequests | userId, instanceId, and role | The number of requests. |

**Operation count-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| OpCounters for Command | Count | OpCommand | userId, instanceId, and role | The number of Command operations. |
| OpCounters for Delete | Count | OpDelete | userId, instanceId, and role | The number of Delete operations. |
| OpCounters for Getmore | Count | OpGetmore | userId, instanceId, and role | The number of Getmore operations. |
| OpCounters for Insert | Count | OpInsert | userId, instanceId, and role | The number of Insert operations. |

| OpCounters for Query | Count | OpQuery | userId, instanceId, and role | The number of Query operations. |
|---|---|---|---|---|
| OpCounters for Update | Count | OpUpdate | userId, instanceId, and role | The number of Update operations. |

#### 3.2.7 ApsaraDB for MongoDB (New)

This topic describes the metrics supported by ApsaraDB for MongoDB (New). Set the **Namespace** parameter to **acs_mongodb**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPUUtilization ne _ w | % | CPUUtilization ne _ w | userId, instanceId, and role | The CPU utilization. |
| MemoryUtilizatio n new _ | % | MemoryUtilizatio n new _ | userId, instanceId, and role | The memory usage. |
| Disk Usage (New) | % | DiskUtilization n _ ew | userId, instanceId, and role | The disk usage. |
| IOPSUtilization n _ ew | % | IOPSUtilization n _ ew | userId, instanceId, and role | The IOPS usage. |
| ConnectionUtiliza tion new _ | % | ConnectionUtiliza tion new _ | userId, instanceId, and role | The connection utilization. |
| Visits per second (new) | Count | QPS new _ | userId, instanceId, and role | The number of queries per second (QPS). |
| Connection Usage (New) | Count | ConnectionAmou nt new _ | userId, instanceId, and role | The number of used connections. |

| Current Total Connections (New) | Count | TotalConnections | userId, instanceId, and role | The total number of current connections. |
|---|---|---|---|---|

**Disk capacity-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| The amount of disk space occupied by the instance (new) | Bytes | InstanceDiskAmo unt new _ | userId, instanceId, and role | The disk space occupied by the instance. |
| Amount of disk space occupied by data (new) | Bytes | DataDiskAmount new _ | userId, instanceId, and role | The disk space occupied by data. |
| The amount of disk space occupied by the log (new) | Bytes | LogDiskAmount _ new | userId, instanceId, and role | The disk space occupied by logs. |

**Network request-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Intranet Inflow (New) | Bytes | IntranetIn new _ | userId, instanceId, and role | The inbound traffic over the intranet. |
| Intranet outbound traffic (new) | Bytes | IntranetOut new _ | userId, instanceId, and role | The outbound traffic over the intranet. |
| Number of requests (new) | Count | NumberRequests new _ | userId, instanceId, and role | The number of requests. |

**Operation count-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| Number of Command Operations (new) | Count | OpCommand ne _ w | userId, instanceId, and role | The number of Command operations. |
|---|---|---|---|---|
| Number of Delete operations (new) | Count | OpDelete new _ | userId, instanceId, and role | The number of Delete operations. |
| Number of Getmore operations (new) | Count | OpGetmore new _ | userId, instanceId, and role | The number of Getmore operations. |
| Number of Insert operations (new) | Count | OpInsert new _ | userId, instanceId, and role | The number of Insert operations. |
| Number of Query operations (new) | Count | OpQuery new _ | userId, instanceId, and role | The number of Query operations. |
| Number of Update operations (new) | Count | OpUpdate new _ | userId, instanceId, and role | The number of Update operations. |

**Basic metrics (Cluster Edition)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Cluster) CPU usage | % | CPUUtilization new _ cluster _ | userId, instanceId, and role | The CPU utilization. |
| (Cluster Version) Memory Usage | % | MemoryUtilization _ new cluster _ | userId, instanceId, and role | The memory usage. |
| (Cluster Edition) Disk Usage | % | DiskUtilization ne _ w cluster _ | userId, instanceId, and role | The disk usage. |
| (Cluster version) IOPS usage | % | IOPSUtilization ne _ w cluster _ | userId, instanceId, and role | The IOPS usage. |
| (Cluster Edition) Connection Usage | % | ConnectionUtilizati on new cluster _ _ | userId, instanceId, and role | The connection utilization. |
| (Cluster Version) Visits Per Second | Count | QPS new cluster _ _ | userId, instanceId, and role | The QPS. |

| (Cluster Edition) Connection Usage | Count | ConnectionAmount new cluster _ _ | userId, instanceId, and role | The number of used connections. |
|---|---|---|---|---|
| (Cluster Edition) Total Number of Connections | Count | TotalConnections _ cluster | userId, instanceId, and role | The total number of current connections. |

**Disk capacity-related metrics (Cluster Edition)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Cluster Edition) The amount of disk space occupied by the instance | Bytes | InstanceDiskAmoun t new cluster _ _ | userId, instanceId, and role | The disk space occupied by the instance. |
| (Cluster Edition) The amount of disk space occupied by data | Bytes | DataDiskAmount n _ ew cluster _ | userId, instanceId, and role | The disk space occupied by data. |
| (Cluster Edition) The amount of disk space occupied by logs | Bytes | LogDiskAmount ne _ w cluster _ | userId, instanceId, and role | The disk space occupied by logs. |

**Network request-related metrics (Cluster Edition)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Cluster Version) Intranet Inflow | Bytes | IntranetIn new cl _ _ uster | userId, instanceId, and role | The inbound traffic over the intranet. |
| (Cluster Version) Intranet outbound traffic | Bytes | IntranetOut new _ _ cluster | userId, instanceId, and role | The outbound traffic over the intranet. |
| (Cluster Version) Number of Requests | Coun t | NumberRequests new cluster _ _ | userId, instanceId, and role | The number of requests. |

**Operation count-related metrics (Cluster Edition)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Cluster Edition) Command Operation Times | Count | OpCommand _ new cluster _ | userId, instanceId, and role | The number of Command operations. |
| (Cluster version) Delete operations | Count | OpDelete ne _ w cluster _ | userId, instanceId, and role | The number of Delete operations. |
| (Cluster version) Getmore Operations | Count | OpGetmore n _ ew cluster _ | userId, instanceId, and role | The number of Getmore operations. |
| (Cluster version) Insert operations | Count | OpInsert new _ cluster _ | userId, instanceId, and role | The number of Insert operations. |
| (Cluster Version) Query Operation Times | Count | OpQuery new _ cluster _ | userId, instanceId, and role | The number of Query operations. |
| (Cluster Edition) Update Operation Times | Count | OpUpdate ne _ w cluster _ | userId, instanceId, and role | The number of Update operations. |

#### 3.2.8 Tair (Redis OSS-compatible) (Old)

This topic describes the metrics supported by Tair (Redis OSS-compatible) (Old). Set the **Namespace** parameter to **acs_kvstore**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | Metric | Dimensions | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| Failed Operations | Count | FailedCount | userId and instanceId | The number of failed operations. |

| Cache Inbound Bandwidth | Bytes/s | IntranetIn | userId and instanceId | The inbound traffic over the intranet. |
|---|---|---|---|---|
| Inbound Bandwidth Usage | % | IntranetInRatio | userId and instanceId | The inbound bandwidth usage. |
| Cache Outbound Bandwidth | Bytes/s | IntranetOut | userId and instanceId | The outbound traffic over the intranet. |
| Outbound Bandwidth Usage | % | IntranetOutRatio | userId and instanceId | The outbound bandwidth usage. |
| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage. |
| Used QPS | Count/s | UsedQPS | userId and instanceId | The number of used QPS. |

#### 3.2.9 Tair (Redis OSS-compatible) (New)

This topic describes the metrics supported by Tair (Redis OSS-compatible) (New). Set the **Namespace** parameter to **acs_kvstore**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Standard Edition instances and Read/write splitting instances**

**of Tair (Redis OSS-compatible)**

> **Note:** Tair (Redis OSS-compatible) Standard Edition instances and Tair (Redis OSS-compatible) Read/write splitting instances share a set of metrics.

| Console- based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Connections Usage (Standard Edition) | % | StandardConnectionU sage | userId and instanceId | The connection utilization. |

| Incoming Bandwidth (Standard Edition) | Kbit/s | StandardIntranetIn | userId and instanceId | The inbound bandwidth. |
|---|---|---|---|---|
| Incoming Bandwidth Utilization (Standard Edition) | % | StandardIntranetInRat io | userId and instanceId | The inbound bandwidth utilization. |
| Outgoing Bandwidth (Standard Edition) | Kbit/s | StandardIntranetOut | userId and instanceId | The outbound bandwidth. |
| Outgoing Bandwidth Usage (Standard Edition) | % | StandardIntranetOutR atio | userId and instanceId | The outbound bandwidth utilization. |
| Memory Usage (Standard Edition) | % | StandardMemoryUsag e | userId and instanceId | The memory usage. |
| QPS usage (standard version) | % | StandardQPSUsage | userId and instanceId | The queries per second (QPS) usage. |
| CPU usage (standard edition) | % | StandardCpuUsage | userId and instanceId | The CPU utilization. |
| Average Visits Per Second (Standard Edition) | Count/s | StandardUsedQPS | userId and instanceId | The average QPS. |
| Total QPS (Standard Edition) | Count/s | StandardTotalQps | userId and instanceId | The total QPS. |
| Current Total Connections (Standard Edition) | Count | StandardTotalConnec tions | userId and instanceId | The total number of current connections. |

**Tair (Redis OSS-compatible) instances that use the cluster**

**architecture**

| Console- based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (Cluster Edition) | % | ShardingConnec tionUsage | userId and instanceId | The connection utilization. |
| Incoming Bandwidth (Cluster Edition) | Kbit/s | ShardingIntranet In | userId and instanceId | The inbound bandwidth. |
| Outgoing Bandwidth (Cluster Edition) | Kbit/s | ShardingIntranet Out | userId and instanceId | The outbound bandwidth. |
| Incoming Bandwidth Usage (Cluster Edition) | % | ShardingIntranet InRatio | userId and instanceId | The inbound bandwidth utilization. |
| Outgoing Bandwidth Usage (Cluster Edition) | % | ShardingIntranet OutRatio | userId and instanceId | The outbound bandwidth utilization. |
| Memory Usage (Cluster Edition) | % | ShardingMemor yUsage | userId and instanceId | The memory usage. |
| QPS usage (cluster version) | % | ShardingQPSUsa ge | userId and instanceId | The QPS utilization. |
| CPU usage (Cluster Edition) | % | ShardingCpuUsa ge | userId and instanceId | The CPU utilization. |
| Average visits per second (cluster version) | Count/s | ShardingUsedQP S | userId and instanceId | The average QPS. |

| Total QPS (cluster version) | Count/s | ShardingTotalQp s | userId and instanceId | The total QPS. |
|---|---|---|---|---|
| Total Current Connections (Cluster Edition) | Count | ShardingTotalCo nnections | userId and instanceId | The total number of current connections. |

**Cluster Edition - Node**

| Console- based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Connections Usage (Node) | % | NodeConnection Usage | userId, instanceId, and nodeId | The connection utilization. |
| Incoming Bandwidth (Node) | Kbit/s | NodeIntranetIn | userId, instanceId, and nodeId | The inbound bandwidth. |
| Outgoing Bandwidth (Node) | Kbit/s | NodeIntranetOut | userId, instanceId, and nodeId | The outbound bandwidth. |
| Incoming Bandwidth Utilization (Node) | % | NodeIntranetInR atio | userId, instanceId, and nodeId | The inbound bandwidth usage. |
| Outgoing Bandwidth Utilization (Node) | % | NodeIntranetOut Ratio | userId, instanceId, and nodeId | The outbound bandwidth usage. |
| Memory Usage (Node) | % | NodeMemoryUs age | userId, instanceId, and nodeId | The memory usage. |
| QPS usage (node) | % | NodeQPSUsage | userId, instanceId, and nodeId | The QPS usage. |
| CPU usage (node) | % | NodeCpuUsage | userId, instanceId, and nodeId | The CPU utilization. |

| Average Visits Per Second (Node) | Count | NodeUsedQPS | userId, instanceId, and nodeId | The average QPS. |
|---|---|---|---|---|
| Total QPS (nodes) | Count/S | NodeTotalQps | userId, instanceId, and nodeId | The total QPS. |
| Total Current Connections (Nodes) | Count | NodeTotalConne ctions | userId, instanceId, and nodeId | The total number of current connections. |

#### 3.2.10 AnalyticDB for PostgreSQL

This topic describes the metrics supported by AnalyticDB for PostgreSQL.

#### 3.2.11 AnalyticDB for PostgreSQL (new)

This topic describes the metrics supported by AnalyticDB for PostgreSQL (new).

#### 3.2.12 DTS

This topic describes the metrics supported by Data Transmission Service (DTS). Set the **Namespace** parameter to **acs_dts_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console- based metric | unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ChangeTrackin gLatency | Seconds | ChangeTrackingLatenc y | userId and instanceId | The latency of the change tracking task. |
| Synchronizatio nLatency | Seconds | SynchronizationLatenc y | userId and instanceId | The latency of the data synchronization task. |
| MigrationLaten cy | Seconds | MigrationLatency | userId and instanceId | The latency of the data migration task. |

##### 3.2.12.1 Data Transmission Service DTS(Tracking tasks)

**tasks)**

This topic describes the metrics for Data Transmission Service DTS( tracking tasks). The value for **Namespace** is **acs_dts_dashboard**. The default value for **Period** is **60** seconds. The value must be a multiple of 60.

| Metric | Unit | MetricName | dimensions | Description |
|---|---|---|---|---|
| Tracking task latency | s | ChangeTrackingLatency | instanceId | The latency of the tracking task. |
| Failed data transmission tasks | Count | ChangeTrackingJobFailed | instanceId | The data transmission task failed. |
| Total number of tracking task instances | Count | SubscribeInstanceTotal | userId | The total number of tracking task instances. |
| Number of unavailable tracking task instances | Count | SubscribeInstanceUnavai lability | userId | The number of unavailable tracking task instances. |

##### 3.2.12.2 Data Transmission Service DTS (migration tasks)

**(migration tasks)**

This topic describes the metrics for Data Transmission Service DTS (migration tasks). The namespace is **acs_dts_dashboard**. The period is **60** seconds by default, or any multiple of 60.

| Metric | Unit | MetricName | dimensions | Description |
|---|---|---|---|---|
| Migration task latency | s | MigrationLatency | instanceId | The latency of the migration task. |
| Failed data transfer tasks | Count | MigrationJobFailed | instanceId | The data transmission task failed. |
| Total migration task instances | Count | MigrationInstanceTotal | userId | The total number of migration task instances. |
| Unavailable migration task instances | Count | MigrationInstanceUnavai lability | userId | The number of unavailable migration task instances. |

##### 3.2.12.3 Data Transmission Service DTS (sync tasks)

**tasks)**

This topic describes the metrics for Data Transmission Service DTS (sync tasks). The value for **Namespace** is **acs_dts_sync**. The default value for **Period** is **60** seconds, and it can be set to any integer multiple of 60.

| Metric | Unit | MetricName | dimensions | Description |
|---|---|---|---|---|
| Sync task latency | s | SynchronizationLatency | instanceId | The latency of the sync task. |
| Failed synchronization tasks | Count | SynchronizationJobFailed | instanceId | The data transmission job failed. |
| Total number of sync task instances | Count | SynchronizationInstance Total | userId | The total number of sync task instances. |
| Number of unavailable sync task instances | Count | SynchronizationInstance Unavailability | userId | The number of unavailable sync task instances. |

#### 3.2.13 Lindorm

This topic describes the metrics for Lindorm. The value for **Namespace** is **acs_lindorm**. The default value for **Period** is **60** seconds. The value can be any multiple of 60.

**LindormTable metrics**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Read requests - Read request volume | rows/s | WTEM RR readR _ _ equestVolume | instanceId | LindormTable metric: Read Request Count. |
| Read requests - Average read RT | ms | WTEM RR readA _ _ verageRT | instanceId | The average response time (RT) for read requests. |

| Read requests - Read traffic | value | WTEM RR readTr _ _ affic | instanceId | The read traffic. |
|---|---|---|---|---|
| Read requests - Get request volume | rows/s | WTEM RR getRe _ _ questVolume | instanceId | The number of Get requests per second. |
| Read requests - Average Get RT | ms | WTEM RR getAv _ _ erageRT | instanceId | The average RT for Get requests. |
| Read requests - P99 Get RT | ms | WTEM RR getP9 _ _ 9RT | instanceId | The 99th percentile RT for Get requests. |
| Read requests - Scan request volume | ops/s | WTEM RR scanR _ _ equestVolume | instanceId | LindormTable Metrics: Read Requests - Scan Requests |
| Read requests - Average Scan RT | ms | WTEM RR scanA _ _ verageRT | instanceId | The average RT for Scan requests. |
| Read requests - P99 Scan RT | ms | WTEM RR scanP _ _ 99RT | instanceId | The 99th percentile RT for Scan requests. |
| Write requests - Write request volume | ops/s | WTEM WR write _ _ RequestVolume | instanceId | The number of write requests per second. |
| Write requests - Average write RT | ms | WTEM WR write _ _ Requests | instanceId | The average RT for write requests. |
| Write requests - Write traffic | value | WTEM WR writeT _ _ raffic | instanceId | The write traffic. |
| Write requests - Total Put request volume | ops/s | WTEM WR putTo _ _ talRequestVolum e | instanceId | The total number of Put requests per second. |
| Write requests - Average Put RT | ms | WTEM WR putAv _ _ erageRT | instanceId | The average RT for Put requests. |
| Write requests - Put request volume | ops/s | WTEM WR putRe _ _ questVolume | instanceId | The number of Put requests per second. |

| Write requests - Number of times the Memstore upper limit was exceeded | counts | WTEM WR excee _ _ dingMemstoreUp perLimit | instanceId | The number of times the Memstore upper limit was exceeded. |
|---|---|---|---|---|
| Write requests - P99 Put RT | ms | WTEM WR putP9 _ _ 9RT | instanceId | The 99th percentile RT for Put requests. |
| SQLv2 - SQL connection count | counts | WTEM SQLv2 sQ _ _ LConnectionCoun t | instanceId | The number of SQL connections. |
| SQLv2 - SELECT request count | ops/s | WTEM SQLv2 sel _ _ ectRequestCount | instanceId | LindormTable metric— SQLv2 SELECT requests |
| SQLv2 - P99 time for SELECT requests | ms | WTEM SQLv2 sel _ _ ectP99RequestTi me | instanceId | The 99th percentile time consumed by SELECT requests. |
| SQLv2 - UPSERT request count | ops/s | WTEM SQLv2 up _ _ sertRequestCoun t | instanceId | The number of UPSERT requests per second. |
| SQLv2 - P99 time for UPSERT requests | ms | WTEM SQLv2 up _ _ sertP99RequestTi me | instanceId | The 99th percentile time consumed by UPSERT requests. |
| SQLv2 - DELETE request count | ops/s | WTEM SQLv2 del _ _ eteRequestCount | instanceId | The number of SQLv2- delete requests. |
| SQLv2 - P99 time for DELETE requests | ms | WTEM SQLv2 del _ _ eteP99RequestTi me | instanceId | The 99th percentile time consumed by DELETE requests. |
| Cluster payload - Number of regions in RS | counts | WTEM CL rSRegi _ _ onCount | instanceId | The number of regions in the RegionServer (RS). |
| Cluster payload - Handler queue length | counts | WTEM CL handle _ _ rQueueLength | instanceId | The length of the handler queue. |
| Cluster payload - Compaction queue length | counts | WTEM CL compa _ _ ctionQueueLengt h | instanceId | The length of the compaction queue. |

| SQLv2 - Median time for DELETE requests | ms | WTEM SQLv2 del _ _ eteMedianReque stTime | instanceId | The median time consumed by DELETE requests. |
|---|---|---|---|---|
| SQLv2 - Median time for UPSERT requests | ms | WTEM SQLv2 up _ _ sertMedianReque stTime | instanceId | The median time consumed by UPSERT requests. |
| SQLv2 - Median time for SELECT requests | ms | WTEM SQLv2 sel _ _ ectMedianReques tTime | instanceId | The median time consumed by SELECT requests. |

**LindormTSDB metrics**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Write volume | points/ s | TSEM WV _ | instanceId | The number of data points written per second. |
| Failed volume | points/ s | TSEM FV _ | instanceId | The number of data points that failed to be written per second. |
| Write request volume | ops/s | TSEM writeReque _ stVolume | instanceId | The number of write requests per second. |
| Average write RT | ms | TSEM writeAvera _ geRT | instanceId | The average RT for write requests. |
| P99 write RT | ms | TSEM writeRTP99 _ | instanceId | The 99th percentile RT for write requests. |
| Read request volume | ops/s | TSEM readReque _ stVolume | instanceId | The number of read requests per second. |
| Active SQL connections (A negative value indicates that no related metric is available) | counts | TSEM activeConn _ ectionsCount | instanceId | The number of active SQL connections. A negative value indicates that no related metric is available. |
| Active statement count | counts | TSEM activesStat _ ementCount | instanceId | The number of active statements. |

| Active ResultSet count | counts | TSEM activeResu _ ltSetCount | instanceId | The number of active ResultSets. |
|---|---|---|---|---|
| Number of inserted rows | rows/s | TSEM insertRowC _ ount | instanceId | The number of rows inserted per second. |
| Number of rows scanned for SELECT | rows/s | TSEM selectScan _ RowCount | instanceId | The number of rows scanned by SELECT statements per second. |
| SELECT request count | rows/s | TSEM selectRequ _ estCount | instanceId | The number of SELECT requests per second. |
| Average SELECT RT | ms | TSEM selectAver _ ageRT | instanceId | The average RT for SELECT requests. |
| P99 time for SELECT | ms | TSEM selectTime _ P99 | instanceId | The 99th percentile time consumed by SELECT statements. |
| Client connections | counts | TSEM clientConn _ ectionCount | instanceId | The number of client connections. |
| Average RT for multi-value API queries | ms | TSEM queryAver _ ageRT mquery _ | instanceId | The average RT for multi- value API queries. |
| Average RT for single-value API queries | ms | TSEM TSEM quer _ _ yAverageRT quer _ y | instanceId | The average RT for single- value API queries. |
| P99 RT for multi-value API queries | ms | TSEM queryRTP9 _ 9 mquery _ | instanceId | The 99th percentile RT for multi-value API queries. |
| P99 RT for single-value API queries | ms | TSEM queryRTP9 _ 9 query _ | instanceId | The 99th percentile RT for single-value API queries. |
| Timeline count | counts | TSEM timelineCo _ unt | instanceId | The number of timelines. |

**File engine metrics**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Storage (hot) usage - Storage used | MIB | FEM SU storageU _ _ sed | instanceId | The amount of hot storage used. |
| Storage (hot) usage - Total storage | MIB | FEM SU totalStor _ _ age | instanceId | The total amount of hot storage. |
| Storage (hot) usage - dfs fsnamesyst _ em capacitytot _ al (Lindorm multi-zone) | value | FEM SU dfs fsna _ _ _ mesystem capaci _ tytotal | instanceId | The total capacity of the file system. This metric is for Lindorm multi-zone deployments. |
| Storage (hot) usage - dfs fsnamesyst _ em capacityuse _ d (Lindorm multi-zone) | value | FEM SU dfs fsna _ _ _ mesystem capaci _ tyused | instanceId | The used capacity of the file system. This metric is for Lindorm multi-zone deployments. |
| Storage (hot) watermark | % | FEM sWatermark _ | instanceId | The watermark of hot storage. |
| NameNode operands (ops/s) - create file ops _ _ | ops/s | FEM NO create fi _ _ _ le ops _ | instanceId | The number of create file _ operations on the NameNode per second. |
| NameNode operands (ops/s) - delete file ops _ _ | ops/s | FEM NO delete fi _ _ _ le ops _ | instanceId | The number of delete file _ operations on the NameNode per second. |
| NameNode operands (ops/s) - add block ops _ _ | ops/s | FEM NO add blo _ _ _ ck ops _ | instanceId | The number of add block _ operations on the NameNode per second. |
| NameNode operands (ops/s) - get blockloc op _ _ s | ops/s | FEM NO _ | instanceId | The number of get blockloc operations on _ the NameNode per second. |

| NameNode operands (ops/s) - get file info op _ _ _ s | ops/s | FEM NO get file _ _ _ _ info ops _ | instanceId | The number of get file info _ _ operations on the NameNode per second. |
|---|---|---|---|---|
| NameNode operands (ops/s) - list dir ops _ _ | ops/s | FEM NO list dir _ _ _ _ ops | instanceId | The number of list dir _ operations on the NameNode per second. |
| NameNode operands (ops/s) - block report op _ _ s | ops/s | FEM NO block re _ _ _ port ops _ | instanceId | The number of block report operations on _ the NameNode per second. |
| DataNode read traffic | value | FEM dataNodeRe _ adTraffic | instanceId | The read traffic of the DataNode. |
| DataNode write traffic | value | FEM dataNodeWr _ iteTraffic | instanceId | The write traffic of the DataNode. |

#### 3.2.14 Lindorm 2.0

This topic describes the metrics for Lindorm 2.0. The value for **Namespace** is **acs_lindorm_multi_model**. The default value for **Period** is **60** seconds. This value can be any integer multiple of 60.

**Cluster overview**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| 5-minute average load (load5) | % | lindorm cluster s _ _ ystem load5 _ | instanceId,compon ent | The average system load over the last 5 minutes. |
| 1-minute average load (load1) | % | lindorm cluster s _ _ ystem load1 _ | instanceId,compon ent | The average system load over the last 1 minute. |
| CPU idle rate | % | lindorm cluster c _ _ pu usage idle _ _ | instanceId,compon ent | The percentage of time that the CPU is idle. |
| CPU WIO usage | % | lindorm cluster c _ _ pu usage iowait _ _ | instanceId,compon ent | The percentage of time that the CPU is waiting for I/O operations. |

| CPU usage (System) | % | lindorm cluster c _ _ pu usage system _ _ | instanceId,compon ent | System CPU utilization. |
|---|---|---|---|---|
| CPU usage (User) | % | lindorm cluster c _ _ pu usage user _ _ | instanceId,compon ent | The percentage of CPU time spent in user mode (User). |

**Compute engine**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Cumulative daily usage of the resource group | CU | Idps total cuh _ _ | instanceId,computeGr oup | The cumulative usage of the resource group for the current day. |
| Real-time memory usage of the resource group | GB | Idps memory scale b _ _ _ y compute group _ _ | instanceId,computeGr oup | The real-time memory usage of the resource group. |
| Real-time CPU usage of the resource group | core | Idps cpu scale by co _ _ _ _ mpute group _ | instanceId,computeGr oup | The real-time CPU usage of the resource group. |

**Search engine**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Doc count | Count | search node index level doc _ _ _ _ s count _ | instanceId | The number of documents. |
| Index doc store size | bytes | search node index level doc _ _ _ _ s total size in bytes _ _ _ _ | instanceId | The storage size of the index documents. |
| Field data cache details | MiB | search node cache field dat _ _ _ _ a cache memory size in byt _ _ _ _ _ es | instanceId | Details of the fielddata cache |
| Request cache details | MiB | search node cache request _ _ _ _ cache memory size in bytes _ _ _ _ | instanceId | View cache details. |
| Query cache details | MiB | search node cache query c _ _ _ _ ache memory size in bytes _ _ _ _ | instanceId | View cache details. |

| Active write thread details | You can choose | search node thread pool wri _ _ _ _ te active _ | instanceId | The number of active write threads. |
|---|---|---|---|---|
| Queued write thread details | You can choose | search node thread pool wri _ _ _ _ te queue _ | instanceId | The number of queued write threads. |
| Queued query thread details | Select | search node thread pool se _ _ _ _ arch queue _ | instanceId | The number of queued query threads. |
| Node query QPS | ms | lindorm search node indices _ _ _ search query rate _ _ _ | instanceId | The number of queries per second (QPS) for the node. |
| Active query thread details | Choose | search node thread pool se _ _ _ _ arch active _ | instanceId | Query the details of active threads. |
| Node fetch QPS | ops/sec | search node fetch qps _ _ _ | instanceId | The number of fetch operations per second for the node. |
| Node write TPS | ops/sec | search node write tps _ _ _ | instanceId | The number of write transactions per second (TPS) for the node. |

**LindormTable**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Compaction queue length | Count | lindorm ldserver compactionQ _ _ ueueSize prom _ | instanceId | The length of the compaction queue. |
| Handler queue length | Count | lindorm ldserver handlerQueue _ _ Size prom _ | instanceId | The length of the handler queue. |
| Number of regions in the RegionServer (RS) | Count | lindorm ldserver regions prom _ _ _ | instanceId | The number of regions in the RegionServer (RS). |
| Number of Put requests | ops/sec | lindorm ldserver putRequestLa _ _ tency num ops prom _ _ _ | instanceId | The number of Put requests per second. |

| Write traffic | Value | lindorm ldserver writeDataPer _ _ SecondKB prom _ | instanceId | The write traffic. |
|---|---|---|---|---|
| Number of write requests | ops/sec | lindorm ldserver writeRequests _ _ num ops prom _ _ _ | instanceId | The number of write requests per second. |
| Number of read requests | rows/se c | lindorm ldserver readRequests _ _ num ops prom _ _ _ | instanceId | The number of read requests per second. |
| Number of Get requests | rows/se c | lindorm ldserver getRequestLa _ _ tency num ops prom _ _ _ | instanceId | The number of Get requests per second. |
| Number of Scan requests | ops/sec | lindorm ldserver nextrpcReque _ _ stLatency num ops prom _ _ _ | instanceId | The number of Scan requests per second. |
| Read traffic | Value | lindorm ldserver readDataPerS _ _ econdKB prom _ | instanceId | The read traffic. |

**LindormTSDB**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Client connections | Count | tsdb reporter tsd connectionmg _ _ _ r connections open prom _ _ _ | instanceId | The number of client connections. |
| Number of Select requests | rows/se c | tsdb reporter tsql connector qu _ _ _ _ ery timer 1min prom _ _ _ | instanceId | The number of Select requests per second. |
| Number of active statements | Count | tsdb reporter tsql statement ac _ _ _ _ tive counter prom _ _ | instanceId | The number of active statements. |
| Number of active SQL connections (A negative value indicates that the metric is unavailable) | Count | tsdb reporter tsql connection a _ _ _ _ ctive counter prom _ _ | instanceId | The number of active SQL connections. A negative value indicates that this metric is not available. |

| Number of active ResultSets (SQL) | Count | tsdb reporter tsql resultset acti _ _ _ _ ve counter prom _ _ | instanceId | The number of active ResultSets for SQL queries. |
|---|---|---|---|---|

**Vector engine**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Number of VectorProxy client connections | Count | lindorm vector n _ _ ode proxy total _ _ _ connections | instanceId | The number of client connections to the VectorProxy. |
| Maximum Delete latency | ms | lindorm vector n _ _ ode vs delete m _ _ _ ax | instanceId | Delete the maximum latency setting. |
| Average Delete latency | ms | lindorm vector n _ _ ode vs delete m _ _ _ ean | instanceId | The average latency of Delete operations. |
| Maximum Get latency | ms | lindorm vector n _ _ ode vs get max _ _ _ | instanceId | The maximum latency of Get operations. |
| Average Get latency | ms | lindorm vector n _ _ ode vs get mean _ _ _ | instanceId | The average latency of Get operations. |
| Maximum GetDistance latency | ms | lindorm vector n _ _ ode vs getdistan _ _ ce max _ | instanceId | The maximum latency of GetDistance operations. |
| Average GetDistance latency | ms | lindorm vector n _ _ ode vs getdistan _ _ ce mean _ | instanceId | The average latency of GetDistance operations. |
| Maximum Put latency | ms | lindorm vector n _ _ ode vs put max _ _ _ | instanceId | The maximum latency of Put operations. |
| Average Put latency | ms | lindorm vector n _ _ ode vs put mea _ _ _ n | instanceId | The average latency of Put operations. |
| Maximum KnnSearch latency | ms | lindorm vector n _ _ ode vs knnsearc _ _ h max _ | instanceId | The maximum latency of KnnSearch operations. |

| Average KnnSearch latency | ms | lindorm vector n _ _ ode vs knnsearc _ _ h mean _ | instanceId | The average latency of KnnSearch operations. |
|---|---|---|---|---|

### 3.3 Storage and CDN

#### 3.3.1 NAS

This topic describes the metrics supported by File Storage NAS (NAS). Set the **Namespace** parameter to **acs_nas**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**File system-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Aligned Size | Bytes | AlignedSize | userId and fileSystemId | The data volume of General- purpose NAS file systems, excluding the Infrequent Access (IA) storage medium. |
| Storage Usage of IA Storage Medium | Bytes | SecondaryAligned Size | userId and fileSystemId | The data volume of the IA storage medium. |
| File Count | Bytes | FileCount | userId and fileSystemId | The number of files. |
| Read IOPS | Operations/ s | IopsRead | userId and fileSystemId | The average read IOPS per minute. |
| Write IOPS | Operations/ s | IopsWrite | userId and fileSystemId | The average write IOPS per minute. |
| Read Latency | Milliseconds | LatencyRead | userId and fileSystemId | The average read latency per minute. |

| Write Latency | Milliseconds | LatencyWrite | userId and fileSystemId | The average write latency per minute. |
|---|---|---|---|---|
| Metadata QPS | Requests/s | QpsMeta | userId and fileSystemId | The average QPS of metadata per minute. |
| Metadata delay | Milliseconds | LatencyMeta | userId and fileSystemId | The average latency of metadata. |
| Read Throughput | Bytes/s | ThruputRead | userId and fileSystemId | The average read throughput per minute. |
| Write Throughput | Bytes/s | ThruputWrite | userId and fileSystemId | The average write throughput per minute. |
| Maximum usable capacity | Bytes | Quota | userId and fileSystemId | The maximum available capacity. |
| Maximum number of files | Count | MaxFileCount | userId and fileSystemId | The maximum number of files. |
| ErrorRateRead | % | ErrorRateRead | userId and fileSystemId | The percentage of read operations in which errors occur. |
| ErrorRateWrite | % | ErrorRateWrite | userId and fileSystemId | The percentage of write operations in which errors occur. |
| ErrorRateMeta | % | ErrorRateMeta | userId and fileSystemId | The percentage of metadata- related operations in which errors occur. |

#### 3.3.2 OSS

This topic describes the metrics supported by Object Storage Service (OSS) Set the **Namespace** parameter to **acs_oss_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| RequestValidRate | % | RequestValidRat e | userId and BucketName | The rate of valid requests. |
| The number of valid requests. | Count | ValidRequestCou nt | userId and BucketName | The number of valid requests. |
| TotalRequestCou nt | Count | TotalRequestCou nt | userId and BucketName | The total number of requests. |
| Availability | % | Availability | userId and BucketName | The availability. Stay alert if this metric is lower than 100%. |
| InternetSend | Bytes | InternetSend | userId and BucketName | The outbound traffic over the Internet. |
| InternetRecv | Bytes | InternetRecv | userId and BucketName | The inbound traffic over the Internet. |
| IntranetSend | Bytes | IntranetSend | userId and BucketName | The outbound traffic over the intranet. |
| IntranetRecv | Bytes | IntranetRecv | userId and BucketName | The inbound traffic over the intranet. |
| CDNSend | Bytes | CdnSend | userId and BucketName | The CDN outbound traffic. |
| CDNRecv | Bytes | CdnRecv | userId and BucketName | The CDN inbound traffic. |

| SyncSend | Bytes | SyncSend | userId and BucketName | The outbound traffic that is generated when you use the cross-region replication feature. |
|---|---|---|---|---|
| SyncRecv | Bytes | SyncRecv | userId and BucketName | The inbound traffic that is generated when you use the cross-region replication feature. |
| MeteringStorage Utilization | Bytes | MeteringStorage Utilization | userId and BucketName | The size of the storage in use. |
| Storage Usage | % | MeteringStorage UtilizationPercent | userId and BucketName | The storage usage of the OSS bucket. |

**Request status-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ServerErrorCount | Count | ServerErrorCount | userId and BucketName | The number of requests with a server error. |
| ServerErrorRate | % | ServerErrorRate | userId and BucketName | The ratio of requests with a server error. |
| NetworkErrorCou nt | Count | NetworkErrorCou nt | userId and BucketName | The number of requests with a network error. |
| NetworkErrorRate | % | NetworkErrorRat e | userId and BucketName | The ratio of requests with a network error. |
| AuthorizationErro rCount | Count | AuthorizationErro rCount | userId and BucketName | The number of requests with an authorization error. |

| ResourceNotFoun dErrorCount | Count | ResourceNotFoun dErrorCount | userId and BucketName | The number of requests with an error indicating that resources cannot be found. |
|---|---|---|---|---|
| ClientTimeoutErr orCount | Count | ClientTimeoutErr orCount | userId and BucketName | The number of requests with a client timeout error. |
| ClientOtherErrorC ount | Count | ClientOtherError Count | userId and BucketName | The number of requests with other client errors. |
| AuthorizationErro rRate | % | AuthorizationErro rRate | userId and BucketName | The ratio of requests with an authorization error. |
| ResourceNotFoun dErrorRate | % | ResourceNotFoun dErrorRate | userId and BucketName | The ratio of requests with an error indicating that resources cannot be found. |
| Client Timeout Error Request Proportion | % | ClientTimeoutErr orRate | userId and BucketName | The ratio of requests with a client timeout error. |
| ClientOtherErrorR ate | % | ClientOtherError Rate | userId and BucketName | The ratio of requests with other client errors. |
| SuccessCount | Count | SuccessCount | userId and BucketName | The number of successful requests. |
| RedirectCount | Count | RedirectCount | userId and BucketName | The number of redirected requests. |
| SuccessRate | % | SuccessRate | userId and BucketName | The ratio of successful requests. |

| RedirectRate | % | RedirectRate | userId and BucketName | The ratio of redirected requests. |
|---|---|---|---|---|

**Maximum latency-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| MaxGetObjectE2 eLatency | Milliseconds | MaxGetObjectE2 eLatency | userId and BucketName | The maximum end-to-end (E2E) latency of GetObject requests. |
| MaxGetObjectSer verLatency | Milliseconds | MaxGetObjectSer verLatency | userId and BucketName | The maximum server latency of GetObject requests. |
| MaxHeadObjectE 2eLatency | Milliseconds | MaxHeadObjectE 2eLatency | userId and BucketName | The maximum E2E latency of HeadObject requests. |
| MaxHeadObjectS erverLatency | Milliseconds | MaxHeadObjectS erverLatency | userId and BucketName | The maximum server latency of HeadObject requests. |
| MaxPutObjectE2e Latency | Milliseconds | MaxPutObjectE2e Latency | userId and BucketName | The maximum E2E latency of PutObject requests. |
| MaxPutObjectSer verLatency | Milliseconds | MaxPutObjectSer verLatency | userId and BucketName | The maximum server latency of PutObject requests. |
| MaxAppendObjec tE2eLatency | Milliseconds | MaxAppendObjec tE2eLatency | userId and BucketName | The maximum E2E latency of AppendObject requests. |

| MaxAppendObjec tServerLatency | Milliseconds | MaxAppendObjec tServerLatency | userId and BucketName | The maximum server latency of AppendObject requests. |
|---|---|---|---|---|
| MaxUploadPartE2 eLatency | Milliseconds | MaxUploadPartE2 eLatency | userId and BucketName | The maximum E2E latency of UploadPart requests. |
| MaxUploadPartSe rverLatency | Milliseconds | MaxUploadPartSe rverLatency | userId and BucketName | The maximum server latency of UploadPart requests. |
| MaxUploadPartCo pyE2eLatency | Milliseconds | MaxUploadPartC opyE2eLatency | userId and BucketName | The maximum E2E latency of UploadPartCopy requests. |
| MaxUploadPartCo pyServerLatency | Milliseconds | MaxUploadPartC opyServerLatenc y | userId and BucketName | The maximum server latency of UploadPartCopy requests. |

**Metrics related to successful requests**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| GetObjectCount | Count | GetObjectCount | userId and BucketName | The number of successful GetObject requests. |
| HeadObjectCount | Count | HeadObjectCount | userId and BucketName | The number of successful HeadObject requests. |
| PostObjectCount | Count | PostObjectCount | userId and BucketName | The number of successful PostObject requests. |
| AppendObjectCo unt | Count | AppendObjectCo unt | userId and BucketName | The number of successful AppendObject requests. |

| UploadPartCount | Count | UploadPartCount | userId and BucketName | The number of successful UploadPart requests. |
|---|---|---|---|---|
| UploadPartCopyC ount | Count | UploadPartCopyC ount | userId and BucketName | The number of successful UploadPartCopy requests. |
| DeleteObjectCou nt | Count | DeleteObjectCou nt | userId and BucketName | The number of successful DeleteObject requests. |
| DeleteObjectsCo unt | Count | DeleteObjectsCo unt | userId and BucketName | The number of successful DeleteObjects requests. |

#### 3.3.3 CPFS

This topic describes the metrics supported by Cloud Parallel File Storage (CPFS). Set **Namespace** to **acs_cpfs**. Set **Period** to an integral multiple of 60. Default value: 60. Unit: seconds.

| Metric | Unit | MetricName | dimensions | Description |
|---|---|---|---|---|
| fs data total kb _ _ _ | kb | fs data total kb _ _ _ | instanceId | The total capacity of the file system. |
| fs data free kb _ _ _ | kb | fs data free kb _ _ _ | instanceId | The remaining capacity of the file system. |
| fs data used kb _ _ _ | kb | fs data used kb _ _ _ | instanceId | The used capacity of the file system. |
| fs data used util _ _ _ | % | fs data used util _ _ _ | instanceId | The percentage of free space in the file system. |
| fs throughput bytes _ _ _ read | B/s | fs throughput bytes r _ _ _ ead | instanceId | The read throughput of the file system. |

| fs throughput bytes _ _ _ written | B/s | fs throughput bytes w _ _ _ ritten | instanceId | The write throughput of the file system. |
|---|---|---|---|---|
| fs read iops _ _ | iops | fs read iops _ _ | instanceId | The read IOPS of the file system. |
| fs write iops _ _ | iops | fs write iops _ _ | instanceId | The write IOPS of the file system. |

#### 3.3.4 APFS

This topic describes the metrics of Apple File System (APFS) file systems. Set the **Namespace** parameter to **acs_apfs**. Set the **Period** parameter to the default value
**60** or an integer multiple of 60. Unit: seconds.

| Console metric | Unit | API metric | Dimension | Description |
|---|---|---|---|---|
| Total Capacity of the File System | byte | efs filesystem total bytes _ _ _ | instanceId | The total capacity of the file system. |
| Remaining Capacity of the File System | byte | efs filesystem free bytes _ _ _ | instanceId | The remaining capacity of the file system. |
| Used Capacity of the File System | byte | efs filesystem used bytes _ _ _ | instanceId | The used capacity of the file system. |
| used Ratio of the File System | % | efs filesystem used util _ _ _ | instanceId | The percentage of used capacity in the file system. |
| Read Bandwidth of the File System | byte/s | efs filesystem read throug _ _ _ hput | instanceId | The read throughput of the file system. |
| Write Bandwidth of the File System | byte/s | efs filesystem write throug _ _ _ hput | instanceId | The write throughput of the file system. |
| iops Read IOPS of the File System | iops | efs filesystem read iops _ _ _ | instanceId | The read IOPS of the file system. |

| iops Write IOPS of the File System | iops | efs filesystem write iops _ _ _ | instanceId | The write IOPS of the file system. |
|---|---|---|---|---|

#### 3.3.5 EFS-NAS file storage

This topic describes the metrics for NAS file storage. The default value of **Period** is **60** seconds, or any multiple of 60.

| Metric | Unit | Metric | Dimensions | Description |
|---|---|---|---|---|
| Read bandwidth | KB/s | ReadBandwidth | instanceId | Read bandwidth. |
| Write bandwidth | KB/s | WriteBandwidth | instanceId | Write bandwidth. |
| Read latency | us | ReadLatency | instanceId | Read latency. |
| Write latency | us | WriteLatency | instanceId | Write latency. |
| Data write OPS | IOPS | WriteOPS | instanceId | Data write OPS. |
| Data read OPS | IOPS | ReadOPS | instanceId | Data read OPS. |

### 3.4 Network

#### 3.4.1 NAT Gateway

This topic describes the metrics supported by NAT gateways. Set the **Namespace** parameter to **acs_nat_gateway**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Total number of sessions | Count | curr num _ | userId and instanceId | The total number of sessions. |

| Capacity Discard Connections (Cumulative Value) | Count | capacity drop _ | userId and instanceId | The number of capacity-dropped connections. |
|---|---|---|---|---|
| Number of new discarded connections (cumulative value) | Count | ratelimit drop _ | userId and instanceId | The number of new dropped connections. |
| Capacity Discard Connections Per Second | Count/s | capacity drop in _ _ c | userId and instanceId | The number of capacity-dropped connections per second. |
| Number of new and discarded connections per second | Count/s | ratelimit drop in _ _ c | userId and instanceId | The number of new dropped connections per second. |
| Number of new connections per second | Count/s | establish rate _ | userId and instanceId | The number of new connections per second. |

**SNAT-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| snet rx.rate _ | Bit/s | snet rx.rate _ | userId, instanceId, and snatentryId | The inbound bandwidth. |
| snet tx.rate _ | Bit/s | snet tx.rate _ | userId, instanceId, and snatentryId | The outbound bandwidth. |

#### 3.4.2 SLB

This topic describes the metrics supported by Server Load Balancer (SLB). Set the **Namespace** parameter to **acs_slb_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| InstanceActiveCon nection | Count | InstanceActiveConnec tion | userId and instanceId | The number of active TCP connections. |
|---|---|---|---|---|
| InstanceInactiveCo nnection | Count | InstanceInactiveConn ection | userId and instanceId | The number of inactive connections per second on the port. |
| InstanceMaxConne ction | Count/s | InstanceMaxConnecti on | userId and instanceId | The number of concurrent connections per second on the port. |
| InstanceNewConne ction | Count | InstanceNewConnecti on | userId and instanceId | The number of new TCP connections. |
| InstancePacketRX | Count/s | InstancePacketRX | userId and instanceId | The number of inbound packets per second. |
| InstancePacketTX | Count/s | InstancePacketTX | userId and instanceId | The number of outbound packets per second. |
| InternetInRate | Bit/s | InstanceTrafficRXNew | userId and instanceId | The inbound bandwidth. |
| InternetOutRate | Bit/s | InstanceTrafficTXNew | userId and instanceId | The outbound bandwidth. |
| UnhealthyServerCo unt | Count | InstanceUnhealthySer verCount | userId and instanceId | The number of unhealthy backend Elastic Compute Service (ECS) instances. |
| InstanceDropConne ction | Count/s | InstanceDropConnecti on | userId and instanceId | The number of connections dropped from the listener per second. |
| InstanceDropTraffic RX | Bit/s | InstanceDropTrafficR X | userId and instanceId | The number of inbound bits dropped from the listener per second. |

| InstanceDropTraffic RX | Bit/s | InstanceDropTrafficT X | userId and instanceId | The number of outbound bits dropped from the listener per second. |
|---|---|---|---|---|
| InstanceDropTraffic RX | Count/s | InstanceDropPacketR X | userId and instanceId | The number of inbound packets dropped from the listener per second. |
| InstanceDropPacke tTX | Count/s | InstanceDropPacketT X | userId and instanceId | The number of outbound packets dropped from the listener per second. |
| Seven-layer instance Qps | Reques ts/s | InstanceSevenFloorQ ps | userId and instanceId | The QPS at Layer 7. |
| InstanceFailConnec tion | Count | InstanceFailConnectio n | userId and instanceId | The number of failed connections on the instance. |

**Port-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| TCPActiveConnectio n | Count | ActiveConnection | userId, instanceId, and port | The number of active TCP connections per second. |
| TCPInactiveConnect ion | Count | InactiveConnectio n | userId, instanceId, and port | The number of inactive connections per second on the port. |
| MaxConnection | Count/s | MaxConnection | userId, instanceId, and port | The number of concurrent connections per second on the port. |
| TCPNewConnection | Count | NewConnection | userId, instanceId, and port | The number of new TCP connections. |
| PacketInPerSecond | Count/s | PacketRX | userId, instanceId, and port | The number of inbound packets per second. |

| PacketOutPerSecon d | Count/s | PacketTX | userId, instanceId, and port | The number of outbound packets per second. |
|---|---|---|---|---|
| IntranetInRate | Bit/s | TrafficRXNew | userId, instanceId, and port | The inbound bandwidth. |
| IntranetOutRate | Bit/s | TrafficTXNew | userId, instanceId, and port | The outbound bandwidth. |
| UnhealthyServerCo unt | Count | UnhealthyServerC ount | userId, instanceId, and port | The number of unhealthy backend ECS instances. |
| DropConnection | Count/s | DropConnection | userId, instanceId, and port | The number of connections dropped from a listener per second. |
| DropTrafficRX | Bit/s | DropTrafficRX | userId, instanceId, and port | The number of inbound bits dropped from the listener per second. |
| DropTrafficTX | Bit/s | DropTrafficTX | userId, instanceId, and port | The number of outbound bits dropped from the listener per second. |
| DropPacketRX | Count/s | DropPacketRX | userId, instanceId, and port | The number of inbound packets dropped from the listener per second. |
| DropPacketTX | Count/s | DropPacketTX | userId, instanceId, and port | The number of outbound packets dropped per second. |
| Seven layers Qps | Reques ts/s | SevenFloorQps | userId, instanceId, and port | The number of queries per second at Layer 7. |
| Number of connection failures per second | Count | FailConnection | userId, instanceId, and port | The number of failed connections per second. |

#### 3.4.3 Application Load Balancer

This topic describes the metrics for Application Load Balancer. The **Namespace** is **acs_alb**. The default **Period** is **60** seconds. You can also set the period to an integer multiple of 60.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Maximum concurrent connections | counts | conn concurrent _ | instanceId | The maximum number of concurrent connections for the ALB instance. |
| Failed backend TLS handshakes per second | count/s | ups tls cps fail _ _ _ | instanceId | The number of failed TLS handshakes per second on the backend servers of the ALB instance. |
| New connections per second | count/s | cps | instanceId | The number of new connections per second for the ALB instance. |
| Failed backend connections per second | count/s | upstream conn error _ _ | instanceId | The number of failed connections per second from the ALB instance to its backend servers. |
| Failed TLS handshakes per second | count/s | tls cps fail _ _ | instanceId | The number of failed TLS handshakes per second for the ALB instance. |
| Redirections per second | count/s | redirect count _ | instanceId | The number of redirections per second for the ALB instance. |
| Requests per second | count/s | qps | instanceId | The number of requests per second for the ALB instance. |
| Backend response time | ms | upstream rt _ | instanceId | The response time of the backend servers for the ALB instance. |
| Request latency | ms | rt | instanceId | The request latency of the ALB instance. |

| Outbound bandwidth | bps | bytes out _ | instanceId | The outbound bandwidth of the ALB instance. |
|---|---|---|---|---|
| Inbound bandwidth | bps | bytes in _ | instanceId | The inbound bandwidth of the ALB instance. |
| 2xx status codes per second | count/s | status code 2xx _ _ | instanceId | The number of 2xx status codes per second returned by the ALB instance. |
| 3xx status codes per second | count/s | status code 3XX _ _ | instanceId | The number of 3xx status codes per second returned by the ALB instance. |
| 4xx status codes per second | count/s | status code 4XX _ _ | instanceId | The number of 4xx status codes per second returned by the ALB instance. |
| An SLB instance supports 500 requests per second. | count/s | 500 count _ | instanceId | The number of 500 status codes per second returned by the ALB instance. |
| 502 status codes per second | count/s | 502 count _ | instanceId | The number of 502 status codes per second returned by the ALB instance. |
| 503 status codes per second | count/s | 503 count _ | instanceId | The number of 503 status codes per second returned by the ALB instance. |
| 504 status codes per second | count/s | 504 count _ | instanceId | The number of 504 status codes per second returned by the ALB instance. |
| 5xx status codes per second | count/s | status code 5xx _ _ | instanceId | The number of 5xx status codes per second returned by the ALB instance. |

| Backend 2xx status codes per second | count/s | upstream code 2xx _ _ | instanceId | The number of 2xx status codes per second returned by the backend servers of the ALB instance. |
|---|---|---|---|---|
| Backend 3xx status codes per second | count/s | upstream code 3XX _ _ | instanceId | The number of 3xx status codes per second returned by the backend servers of the ALB instance. |
| Backend 4xx status codes per second | count/s | upstream code 4XX _ _ | instanceId | The number of 4xx status codes per second returned by the backend servers of the ALB instance. |
| Backend 5xx status codes per second | count/s | upstream code 5XX _ _ | instanceId | The number of 5xx status codes per second returned by the backend servers of the ALB instance. |
| Number of healthy backend servers | counts | statusup | instanceId | The number of healthy backend servers for the ALB instance. |
| Number of unhealthy backend servers | counts | statusdown | instanceId | The number of unhealthy backend servers for the ALB instance. |

#### 3.4.4 EIP

This topic describes the metrics supported by Elastic IP Address (EIP). Set the **Namespace** parameter to **acs_vpc_eip**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| net rx.rate _ | Bit/s | net rx.rate _ | userId and instanceId | The inbound bandwidth. |

| net rxPkgs.rate _ | Count/s | net rxPkgs.rate _ | userId and instanceId | The rate of inbound packets. |
|---|---|---|---|---|
| net tx.rate _ | Bit/s | net tx.rate _ | userId and instanceId | The outbound bandwidth. |
| net txPkgs.rate _ | Count/s | net txPkgs.rate _ | userId and instanceId | The rate of outbound packets. |
| Out Ratelimit Drop Speed | Packets/s | out ratelimit dro _ _ p speed _ | userId and instanceId | The outbound packet loss rate. |
| In Ratelimit Drop Speed | Packets/s | in ratelimit drop _ _ speed _ | userId and instanceId | The inbound packet loss rate. |

#### 3.4.5 VPN Gateway

This topic describes the metrics supported by VPN Gateway. Set the **Namespace** parameter to **acs_vpn**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| IPSec.connection. rxPkgs | Packets/s | ipsec.rxPkgs | userId, instanceId, and ipsecId | The rate of inbound packets of the connection. |
| IPSec.connection. txpkgs | Packets/s | ipsec.txPkgs | userId, instanceId, and ipsecId | The rate of outbound packets of the connection. |
| IPSec.connection. rx.rate | Bit/s | ipsec rx.rate _ | userId, instanceId, and ipsecId | The number of inbound bits of the connection per second. |
| IPSec.connection. tx.rate | Bit/s | ipsec tx.rate _ | userId, instanceId, and ipsecId | The number of outbound bits of the connection per second. |

| SSL Client Count | Count | ssl client.count _ | userId and instanceId | The number of connections. |
|---|---|---|---|---|

#### 3.4.6 DNS

This topic describes the metrics supported by DNS. Set the **Namespace** parameter to **acs_dns_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Latency | Milliseco nds | Latency | userId and instanceId | The parsing latency. |
| ParsingSucceed ed | Count | ParsingSucceeded | userId and instanceId | The number of successfully parsed records. |
| Total number of analyses | Count | ParsingTotal | userId and instanceId | The total number of parsed records. |

#### 3.4.7 Alibaba Cloud DNS - Tenant forwarded domain names

**domain names**

This topic describes the metrics for tenant forwarded domain names in Alibaba Cloud DNS. The **Namespace** is **acs_dns_dashboard**. The default **Period** is **60** seconds. You can also set the period to an integer multiple of 60.

| Metric | Unit | MetricName | dimensions | Description |
|---|---|---|---|---|
| Number of client IPs | counts | client count _ | instanceId,client | The number of client IPs. |
| Domain name resolution success rate | % | ParsingSucceededRa te | instanceId | The success rate of domain name resolution. |
| Response time (qname) | ms | LatencybyQname | instanceId,qname | The response time. |
| Response time | ms | Latency | instanceId | The parsing latency. |

| Number of successful resolutions | counts | ParsingSucceeded | instanceId | The number of successful resolutions. |
|---|---|---|---|---|
| Number of successful resolutions (qname) | counts | ParsingSucceededby Qname | instanceId,qname | The number of successful resolutions. |
| Total number of resolutions | counts | ParsingTotal | instanceId | The total number of parses. |
| Total number of resolutions (qname) | counts | ParsingTotalbyQnam e | instanceId,qname | Total number of parses. |

#### 3.4.8 Cloud Enterprise Network

This topic lists the monitoring metrics for Cloud Enterprise Network. The **Namespace** is **acs_cbn**. The default **Period** is **60** seconds and can be any integer multiple of 60.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Transit Router inbound traffic rate | bps | TransitRouterInRate | instanceId,trInstan ceId,vpcId | This metric is the sum of the inbound traffic rates from all hosts within the VPC. |
| Transit Router outbound traffic rate | bps | TransitRouterOutRat e | instanceId,trInstan ceId,vpcId | This metric is the sum of the outbound traffic rates to all hosts within the VPC. |
| Transit Router inbound packet rate | pps | TransitRouterInPack etsRate | instanceId,trInstan ceId,vpcId | This metric is the sum of the inbound packet rates from all hosts within the VPC. |
| Transit Router outbound packet rate | pps | TransitRouterOutPac ketsRate | instanceId,trInstan ceId,vpcId | This metric is the sum of the outbound packet rates to all hosts within the VPC. |

| Transit Router packet loss rate | pps | TransitRouterPacket LossRate | instanceId,trInstan ceId,vpcId | The average packet loss rate on the VPC connection. |
|---|---|---|---|---|

### 3.5 Middleware services

#### 3.5.1 ApsaraMQ for RocketMQ

This topic describes the metrics supported by ApsaraMQ for RocketMQ. Set the **Namespace** parameter to **acs_rocketmq_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Message retention duration | Hour | MessageRetentio nPeriod | userId and instanceId | The retention period of the message. |
| ReceiveMessage CountPerInstance | Count/min | ReceiveMessage CountPerInstance | userId and instanceId | The number of messages that the consumer receives per minute. |
| SendMessageCou ntPerInstance | Count/min | SendMessageCou ntPerInstance | userId and instanceId | The number of messages that the producer sends per minute. |
| Consumer(Instan ce) receives messages TPS | Count/min | ReceiveMessage TPSPerInstance | userId and instanceId | The TPS for receiving messages by the consumer per minute. |
| Producer(Instanc e) sends messages TPS | Count/min | SendMessageTPS PerInstance | userId and instanceId | The TPS for sending messages by the producer per minute. |

**Group-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConsumerLagPer Gid | Count | ConsumerLag | userId, instanceId, and groupId | The number of accumulated messages. |
| ReceiveMessage CountPerGid | Count/min | ReceiveMessage CountPerGid | userId, instanceId, and groupId | The number of messages that the consumer receives per minute. |
| SendDLQMessag eCountPerGid | Count/min | SendDLQMessag eCountPerGid | userId, instanceId, and groupId | The number of dead-letter messages generated per minute. |
| Producer(GroupId ) Number of messages sent per minute | Count/min | SendMessageCou ntPerGid | userId, instanceId, and groupId | The number of messages that the producer sends per minute. |
| Consumer(GroupI d) receives message TPS | Count/min | ReceiveMessage TPSPerGid | userId, instanceId, and groupId | The TPS for receiving messages by the consumer per minute. |
| Producer(GroupId ) sends messages TPS | Count/min | SendMessageTPS PerGid | userId, instanceId, and groupId | The TPS for sending messages by the producer per minute. |

**Topic-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ReceiveMessage CountPerTopic | Count/min | ReceiveMessage CountPerTopic | userId, instanceId, and topic | The number of messages that the consumer receives per minute. |

| SendMessageCou ntPerTopic | Count/min | SendMessageCou ntPerTopic | userId, instanceId, and topic | The number of messages sent by the producer per minute. |
|---|---|---|---|---|
| Consumer(Topic) receives message TPS | Count/min | ReceiveMessage TPSPerTopic | userId, instanceId, and topic | The TPS for receiving messages by the consumer per minute. |
| Producer(Topic) sends messages TPS per minute | Count/min | SendMessageTPS PerTopic | userId, instanceId, and topic | The TPS for sending messages by the producer per minute. |

**Group and topic-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConsumerLagPer GidTopic | Count | ConsumerLagPer GidTopic | userId, instanceId, groupId, and topic | The number of accumulated messages. |
| ReceiveMessage CountPerGidTopic | Count/min | ReceiveMessage CountPerGidTopi c | userId, instanceId, groupId, and topic | The number of messages that the consumer receives per minute. |
| SendDLQMessag eCountPerGidTop ic | Count/min | SendDLQMessag eCountPerGidTop ic | userId, instanceId, groupId, and topic | The number of dead-letter messages generated per minute. |
| Producer(GroupId & Topic) Number of messages sent per minute | Count/min | SendMessageCou ntPerGidTopic | userId, instanceId, groupId, and topic | The number of messages that the producer sends per minute. |

#### 3.5.2 Message Queue (tiangong)

This topic describes the metrics for Message Queue (tiangong). The **Namespace** is acs_mqtiangong_dashboard. The default **Period** is **60** seconds. The period can be any integer multiple of 60 seconds.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Consumer group offset | counts | rocketmq group dif _ _ f | instanceId | The offset of the consumer group. |
| Consumer group retry offset | counts | rocketmq group re _ _ trydiff | instanceId | The retry offset of the consumer group. |
| Consumer group dead-letter queue offset | counts | rocketmq group dl _ _ qdiff | instanceId | The dead-letter queue offset of the consumer group. |
| Number of consumer group instances | counts | rocketmq group co _ _ unt | instanceId | The number of instances in the consumer group. |
| Number of producer instances | counts | rocketmq producer _ count _ | instanceId | The number of producer instances. |
| Producer message progress | counts | rocketmq producer _ offset _ | instanceId | The message progress of the producer. |
| Retry topic message progress | counts | rocketmq topic ret _ _ ry offset _ | instanceId | The message progress of the retry topic. |
| Delayed topic message progress | counts | rocketmq topic dlq _ _ offset _ | instanceId | The message progress of the delayed topic. |
| Messages sent per second by the producer | counts | rocketmq producer _ tps _ | instanceId | The number of messages sent per second by the producer. |
| Number of messages sent by the producer | counts | rocketmq producer _ message size _ _ | instanceId | The number of messages sent by the producer. |

| Messages consumed per second by the consumer | counts | rocketmq consume _ r tps _ | instanceId | The number of messages consumed per second by the consumer. |
|---|---|---|---|---|
| Messages consumed per second by the consumer group | counts | rocketmq group co _ _ nsume tps _ | instanceId | The number of messages consumed per second by the consumer group. |
| Number of message retries for the consumer topic | counts | rocketmq send bac _ _ k nums _ | instanceId | The number of message retries for the consumer topic. |
| Consumer group consumption latency | counts | rocketmq group ge _ _ t latency by storet _ _ _ ime | instanceId | The consumption latency of the consumer group. |
| Consumer group consumption progress | counts | rocketmq consume _ r offset _ | instanceId | The consumption progress of the consumer group. |
| Number of messages consumed by the consumer group | counts | rocketmq consume _ r message size _ _ | instanceId | The number of messages consumed by the consumer group. |
| Number of messages the client failed to consume | counts | rocketmq client co _ _ nsume fail msg co _ _ _ unt | instanceId | The number of messages that the client failed to consume. |
| Messages failed to be consumed per second by the client | counts | rocketmq client co _ _ nsume fail msg tp _ _ _ s | instanceId | The number of messages that the client fails to consume per second. |

| Messages successfully consumed per second by the client | counts | rocketmq client co _ _ nsume ok msg tps _ _ _ | instanceId | The number of messages successfully consumed per second by the client. |
|---|---|---|---|---|
| Average consumption time per message for the client | counts | rocketmq client co _ _ nsume rt _ | instanceId | The average time the client takes to consume a single message. |
| Client message pull latency | counts | rocketmq client co _ _ nsumer pull rt _ _ | instanceId | The latency of message pulls by the client. |
| Messages pulled per second by the client | counts | rocketmq client co _ _ nsumer pull tps _ _ | instanceId | The number of messages pulled per second by the client. |

#### 3.5.3 ApsaraMQ for Kafka

This topic describes the metrics supported by ApsaraMQ for Kafka.

#### 3.5.4 API Gateway

This topic describes the metrics for API Gateway. The value of **Namespace** is **acs_cop**. The default value of **Period** is **60** seconds. The value must be a multiple of 60.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| TCP bytes sent | B/s | envoy http downstream _ _ _ cx tx bytes total _ _ _ | instanceId | The number of TCP bytes sent. |
| TCP bytes received | B/s | envoy http downstream _ _ _ cx rx bytes total _ _ _ | instanceId | The number of TCP bytes received. |
| Upstream requests | req/s | envoy cluster upstream r _ _ _ q total _ | instanceId | The number of upstream requests. |

| Downstream requests | req/s | envoy http downstream r _ _ _ q total _ | instanceId | The number of downstream requests. |
|---|---|---|---|---|
| Average upstream response time | ms | envoy cluster upstream r _ _ _ q time average _ _ | instanceId | The average response time for upstream requests. |
| Average downstream response time | ms | envoy http downstream r _ _ _ q time average _ _ | instanceId | The average response time for downstream requests. |
| 99th percentile of upstream response time | ms | envoy cluster upstream r _ _ _ q time ninety nine perce _ _ _ _ ntile | instanceId,le | The 99th percentile of the response time for upstream requests. |
| 90th percentile of upstream response time | ms | envoy cluster upstream r _ _ _ q time ninety percentile _ _ _ | instanceId,le | The 90th percentile of the response time for upstream requests. |
| 50th percentile of upstream response time | ms | envoy cluster upstream r _ _ _ q time median _ _ | instanceId,le | The 50th percentile of the response time for upstream requests. |
| Downstream success rate | % | envoy http downstream r _ _ _ q success rate _ _ | instanceId | The success rate of downstream requests. |
| 99th percentile of downstream response time | ms | envoy http downstream r _ _ _ q time ninety nine perce _ _ _ _ ntile | instanceId,le | The 99th percentile of the response time for downstream requests. |
| 90th percentile of downstream response time | ms | envoy http downstream r _ _ _ q time ninety percentile _ _ _ | instanceId,le | The 90th percentile of the response time for downstream requests. |

| 50th percentile of downstream response time | ms | envoy http downstream r _ _ _ q time median _ _ | instanceId,le | The 50th percentile of the response time for downstream requests. |
|---|---|---|---|---|
| Upstream success rate | % | envoy cluster upstream r _ _ _ q success rate _ _ | instanceId | The success rate of upstream requests. |

### 3.6 Big data

#### 3.6.1 DataHub

This topic describes the metrics supported by DataHub. Set the **Namespace** parameter to **acs_datahub**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| subscription delay time | Seconds | subscribe delay _ | userId, regionId, project, topic, and subId | The latency between the time when a user subscribes to data and the current system time. |
| Consumption latency | Seconds | consume delay _ | userId, regionId, project, topic, and subId | The latency between the time when a user subscribes to data and the time when the lasted data is generated. |
| Number of accumulated messages | Count | record stacked _ | userId, regionId, project, topic, and subId | The amount of accumulated data to be consumed by the subscriber. |

#### 3.6.2 Alibaba Cloud Elasticsearch

#### 3.6.3 MaxCompute

This topic describes the metrics for MaxCompute. Set **Namespace** to **acs_maxcompute**. Set **Period** to an integral multiple of **60**. Default value: 60. Unit: seconds.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| project used file nu _ _ _ mber | count | project used file nu _ _ _ mber | userId,instanceId | The number of files used by the project. |
| project used rate _ _ | % | project used rate _ _ | userId,instanceId | The usage of the project space. |
| project max size _ _ | bytes | project max size _ _ | userId,instanceId | The maximum space of the project. |
| project used size _ _ | bytes | project used size _ _ | userId,instanceId | The space used by the project. |

#### 3.6.4 MaxCompute quota groups

This topic describes the metrics for MaxCompute quota groups. Set **Namespace** to **acs_maxcompute**. Set **Period** to an integral multiple of **60**. Default value: 60. Unit: seconds.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| quota max cpu _ _ | cu | quota max cpu _ _ | userId,instanceId | The maximum number of CPU cores in the quota group. |
| quota min cpu _ _ | cu | quota min cpu _ _ | userId,instanceId | The minimum number of CPU cores in the quota group. |
| quota used cpu _ _ | cu | quota used cpu _ _ | userId,instanceId | The number of CPU cores in use in the quota group. |
| quota max memory _ _ | GB | quota max memory _ _ | userId,instanceId | The maximum memory size in the quota group. |
| quota min memory _ _ | GB | quota min memory _ _ | userId,instanceId | The minimum memory size in the quota group. |

| quota used memory _ _ | GB | quota used memor _ _ y | userId,instanceId | The size of memory in use in the quota group. |
|---|---|---|---|---|
| quota used cpu rate _ _ _ | % | quota used cpu rat _ _ _ e | userId,instanceId | The CPU utilization of the quota group. |
| quota used memory _ _ _ rate | % | quota used memor _ _ y rate _ | userId,instanceId | The memory utilization of the quota group. |

### 3.7 Security (Apsara Stack Security)

**Security)**

#### 3.7.1 Tenant-side bastion hosts

This topic describes the metrics for tenant-side bastion hosts. Set the **Namespace** parameter to **acs_bastionhost**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**System-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (ECS)CPU usage | % | CPUUtilization | userId and instanceId | The CPU utilization. |
| CPU system usage | % | CPUSysUtilization | userId and instanceId | The CPU utilization in kernel mode. |
| CPU user usage | % | CPUSysUtilization | userId and instanceId | The CPU utilization in user mode. |
| (ECS) memory usage | % | MemoryUtilization | userId and instanceId | The memory usage. |
| (ECS) system load Load1 | Count/s | SystemLoad1 | userId and instanceId | The system load in the last minute. |
| (ECS) system load Load5 | Count/s | SystemLoad5 | userId and instanceId | The system load in the last 5 minutes. |

| (ECS) System load Load15 | Count/s | SystemLoad15 | userId and instanceId | The system load in the last 15 minutes. |
|---|---|---|---|---|
| (ECS) root directory disk usage | % | RootDiskUtilization | userId and instanceId | The disk usage of the root directory. |
| (ECS)Docker directory disk usage | % | DockerDiskUtilizatio n | userId and instanceId | The disk usage of the Docker directory. |
| (ECS) root directory disk remaining | GB | DfRootBfree | userId and instanceId | The available disk space of the root directory. |
| (ECS) root directory disk used | GB | DfRootUsed | userId and instanceId | The used disk space of the root directory. |
| (ECS) Total number of root directory disks | GB | DfRootBtotl | userId and instanceId | The total disk space of the root directory. |
| (ECS)Docker directory disk remaining | GB | DfDockerBfree | userId and instanceId | The available disk space of the Docker directory. |
| (ECS)Docker directory disk used | GB | DfDockerUsed | userId and instanceId | The used disk space of the Docker directory. |
| (ECS) Total number of Docker directory disks | GB | DfDockerBtotl | userId and instanceId | The total disk space of the Docker directory. |
| (ECS) root Inode usage | % | RootInodeUtilization | userId and instanceId | The inode usage of the root directory. |
| (ECS)Docker directory Inode usage | % | DockerInodeUtilizati on | userId and instanceId | The inode usage of the Docker directory. |
| (ECS) network ingress traffic | Bytes/s | TrafficBytin | userId and instanceId | The inbound traffic. |

| (ECS) network egress traffic | Bytes/s | TrafficBytout | userId and instanceId | The outbound traffic. |
|---|---|---|---|---|
| (ECS)tcp links | Count | TcpConnections | userId and instanceId | The number of TCP connections. |
| (ECS) number of processes | Count | ProcessNumber | userId and instanceId | The number of processes. |
| (ECS)NTP service offset | Second s | NtpOffset | userId and instanceId | The offset of the Network Time Protocol (NTP) service. |
| (ECS) Whether the Docker service is running properly | Count/s | DockerService | userId and instanceId | The status of the Docker service. Valid values: 0: The Docker service does not exist. 1: The Docker service exists. |

**Business-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CountSession | Count | CountSession | instanceId | The number of real- time sessions. |
| CountUser | Count | CountUser | instanceId | The number of users of the bastion host. |
| CountHost | Count | CountHost | instanceId | The number of hosts managed by the bastion host. |
| CountHostQuota | Count | CountHostQuota | instanceId | The quota of hosts that can be managed by the bastion host. |
| CountVisitPolicy | Count | CountVisitPolicy | instanceId | The number of access policies of the bastion host. |

| CountCommandP olicy | Count | CountCommandPolic y | instanceId | The number of command policies of the bastion host. |
|---|---|---|---|---|
| CountWorkorderP olicy | Count | CountWorkorderPolic y | instanceId | The number of ticket policies of the bastion host. |
| CountWarningDay Un | Count | CountWarningDayUn | instanceId | The number of alerts that the bastion host does not handle on the current day. |
| CountWarningDay | Count | CountWarningDay | instanceId | The total number of alerts on the current day. |
| NICBindWidthRx | Mbit/s | NICBindWidthRx | instanceId | The inbound bandwidth of the network interface controller (NIC). |
| NICBindWidthTx | Mbit/s | NICBindWidthTx | instanceId | The outbound bandwidth of the NIC. |
| CountAppServerR un | Count | CountAppServerRun | instanceId | The number of frontend hosts in the normal state. |
| CountAppServerF ault | Count | CountAppServerFault | instanceId | The number of frontend hosts in the abnormal state. |

**Health check-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| (Service) Service Health Check | Count/s | ServiceHealthCheck | userId and instanceId | The status of the health check service. Valid values: 0: The service does not work as expected. 1: The service works as expected. |
|---|---|---|---|---|

#### 3.7.2 Static data masking and watermarking

This topic describes the monitoring metrics for static data masking and watermarking.

#### 3.7.3 Vulnerability scanner engines

This topic describes the metrics for vulnerability scanner engines. Set the **Namespace** parameter to **acs_scanner**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**System-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (ECS)CPU usage | % | CPUUtilization | userId and instanceId | The CPU utilization. |
| CPU system usage | % | CPUSysUtilization | userId and instanceId | The CPU utilization in kernel mode. |
| CPU user usage | % | CPUUserUtilization | userId and instanceId | The CPU utilization in user mode. |
| (ECS) memory usage | % | MemoryUtilization | userId and instanceId | The memory usage. |
| (ECS) system load Load1 | Count/s | SystemLoad1 | userId and instanceId | The system load in the last minute. |
| (ECS) system load Load5 | Count/s | SystemLoad5 | userId and instanceId | The system load in the last 5 minutes. |
| (ECS) System load Load15 | Count/s | SystemLoad15 | userId and instanceId | The system load in the last 15 minutes. |

| (ECS) root directory disk usage | % | RootDiskUtilization | userId and instanceId | The disk usage of the root directory. |
|---|---|---|---|---|
| (ECS)Docker directory disk usage | % | DockerDiskUtilizatio n | userId and instanceId | The disk usage of the Docker directory. |
| (ECS)Docker directory disk remaining | GB | DfDockerBfree | userId and instanceId | The available disk space of the Docker directory. |
| (ECS)Docker directory disk used | GB | DfDockerUsed | userId and instanceId | The used disk space of the Docker directory. |
| (ECS) Total number of Docker directory disks | GB | DfDockerBtotl | userId and instanceId | The total disk space of the Docker directory. |
| (ECS) root directory disk remaining | GB | DfRootBfree | userId and instanceId | The available disk space of the root directory. |
| (ECS) root directory disk used | GB | DfRootUsed | userId and instanceId | The used disk space of the root directory. |
| (ECS) Total number of root directory disks | GB | DfRootBtotl | userId and instanceId | The total disk space of the root directory. |
| (ECS) root Inode usage | % | RootInodeUtilization | userId and instanceId | The inode usage of the root directory. |
| (ECS)Docker directory Inode usage | % | DockerInodeUtilizati on | userId and instanceId | The inode usage of the Docker directory. |
| (ECS) network ingress traffic | Bytes/s | TrafficBytin | userId and instanceId | The inbound traffic. |
| (ECS) network egress traffic | Bytes/s | TrafficBytout | userId and instanceId | The outbound traffic. |
| (ECS)tcp links | Count/s | TcpConnections | userId and instanceId | The number of TCP connections. |

| (ECS) number of processes | Count | ProcessNumber | userId and instanceId | The number of processes. |
|---|---|---|---|---|
| (ECS)NTP service offset | Second s | NtpOffset | userId and instanceId | The offset of the Network Time Protocol (NTP) service. |
| (ECS) Whether the Docker service is running properly | Count/s | DockerService | userId and instanceId | The status of the Docker service. Valid values: 0: The Docker service does not exist. 1: The Docker service exists. |

**Health check-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Service) Service Health Check | Count/s | ServiceHealthCheck | userId and instanceId | The status of the health check service. Valid values: 0: The service does not work as expected. 1: The service works as expected. |

#### 3.7.4 NFV Cloud Firewall

This topic describes the metrics for NFV Cloud Firewall. The value for **Namespace** is **acs_nfv**. The default value for **Period** is **60** seconds or any integer multiple of 60.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| (ECS) CPU utilization | % | CPUUtilization | instanceId | CPU utilization. |
| CPU system mode utilization | % | CPUSysUtilization | instanceId | CPU system mode utilization. |

| CPU user mode utilization | % | CPUUserUtilization | instanceId | CPU user mode utilization. |
|---|---|---|---|---|
| (ECS) memory usage | % | MemoryUtilization | instanceId | Memory usage. |
| (ECS) system load Load1 | count/s | SystemLoad1 | instanceId | System load Load1. |
| (ECS) system load Load5 | count/s | SystemLoad5 | instanceId | System load Load5. |
| (ECS) system load Load15 | count/s | SystemLoad15 | instanceId | System load Load15. |
| (ECS) root directory disk usage | % | RootDiskUtilization | instanceId | Root directory disk usage. |
| (ECS) Docker directory disk usage | % | DockerDiskUtilizatio n | instanceId | Docker directory disk usage. |
| (ECS) Docker directory free disk space | GIB/S | DfDockerBfree | instanceId | Free disk space in the Docker directory. |
| (ECS) Docker directory used disk space | GIB/S | DfDockerUsed | instanceId | Used disk space in the Docker directory. |
| (ECS) Docker directory total disk space | GIB/S | DfDockerBtotl | instanceId | Total disk space in the Docker directory. |
| (ECS) root directory free disk space | GIB/S | DfRootBfree | instanceId | Free disk space in the root directory. |
| (ECS) root directory used disk space | GIB/S | DfRootUsed | instanceId | Used disk space in the root directory. |
| (ECS) root directory total disk space | GIB/S | DfRootBtotl | instanceId | Total disk space in the root directory. |
| (ECS) root directory Inode usage | % | RootInodeUtilization | instanceId | Root directory Inode usage. |

| (ECS) Docker directory Inode usage | % | DockerInodeUtilizati on | instanceId | Docker directory Inode usage. |
|---|---|---|---|---|
| (ECS) network inbound traffic | BYTE/S | TrafficBytin | instanceId | Network inbound traffic. |
| (ECS) network outbound traffic | BYTE/S | TrafficBytout | instanceId | Network outbound traffic. |
| (ECS) network inbound packets | count/s | pktIn | instanceId | Network inbound packets. |
| (ECS) network outbound packets | count/s | pktOut | instanceId | Network outbound packets. |
| (ECS) network inbound error packets | count/s | pktErr | instanceId | Network inbound error packets. |
| (ECS) packet loss count | count/s | pktDrp | instanceId | Packet loss count. |
| (ECS) TCP connections | count/s | TcpConnections | instanceId | TCP connections. |
| (ECS) process count | count/s | pktDrp | instanceId | Process count. |
| (Service) service health check | count/s | health | instanceId | Service health check. |

#### 3.7.5 Web Application Firewall

This topic describes the metrics for Web Application Firewall. The value of **Namespace** is acs_wafonecs. The default value of **Period** is **60** seconds. You can set the period to any integer multiple of 60.

**System monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| (ECS) CPU usage | % | CPUUtilization | instanceId,ecsIn stanceId | CPU usage. |

| CPU system mode usage | % | CPUSysUtilization | instanceId,ecsIn stanceId | CPU usage in system mode. |
|---|---|---|---|---|
| CPU user mode usage | % | CPUUserUtilization | instanceId,ecsIn stanceId | CPU usage in user mode. |
| (ECS) memory usage | % | MemoryUtilization | instanceId,ecsIn stanceId | Memory usage. |
| (ECS) System load 1 | count/s | SystemLoad1 | instanceId,ecsIn stanceId | System load 1. |
| (ECS) System load 5 | count/s | SystemLoad5 | instanceId,ecsIn stanceId | System load 5. |
| (ECS) System load 15 | count/s | SystemLoad15 | instanceId,ecsIn stanceId | System load 15. |
| (ECS) Root directory disk usage | % | RootDiskUtilization | instanceId,ecsIn stanceId | Disk usage of the root directory. |
| (ECS) Docker directory disk usage | % | DockerDiskUtilizatio n | instanceId,ecsIn stanceId | Disk usage of the Docker directory. |
| (ECS) Docker directory free disk space | GiB/s | DfDockerBfree | instanceId,ecsIn stanceId | Free disk space in the Docker directory. |
| (ECS) Docker directory used disk space | GiB/s | DfDockerUsed | instanceId,ecsIn stanceId | Used disk space in the Docker directory. |
| (ECS) Docker directory total disk space | GiB/s | DfDockerBtotl | instanceId,ecsIn stanceId | Total disk space in the Docker directory. |
| (ECS) Root directory free disk space | GiB/s | DfRootBfree | instanceId,ecsIn stanceId | Free disk space in the root directory. |
| (ECS) Root directory used disk space | GiB/s | DfRootUsed | instanceId,ecsIn stanceId | Used disk space in the root directory. |
| (ECS) Root directory total disk space | GiB/s | DfRootBtotl | instanceId,ecsIn stanceId | Total disk space in the root directory. |

| (ECS) Root directory inode usage | % | RootInodeUtilization | instanceId,ecsIn stanceId | Inode usage of the root directory. |
|---|---|---|---|---|
| (ECS) Docker directory inode usage | % | DockerInodeUtilizati on | instanceId,ecsIn stanceId | Inode usage of the Docker directory. |
| (ECS) Inbound network traffic | bytes/s | TrafficBytin | instanceId,ecsIn stanceId | Inbound network traffic. |
| (ECS) Outbound network traffic | bytes/s | TrafficBytout | instanceId,ecsIn stanceId | Outbound network traffic. |
| (ECS) TCP connections | count/s | TcpConnections | instanceId,ecsIn stanceId | The number of TCP connections. |
| (ECS) Number of processes | bytes/s | ProcessNumber | instanceId,ecsIn stanceId | The number of processes. |
| (ECS) NTP service offset | ms | NtpOffset | instanceId,ecsIn stanceId | The NTP service offset. |
| (ECS) Docker service status | count/s | DockerService | instanceId,ecsIn stanceId | Indicates whether the Docker service is running normally. |

**Health check**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| (Service) health check | count/s | ServiceHealthCheck | instanceId,ecsIn stanceId | Service health check. |

### 3.8 AI and machine learning

#### 3.8.1 AI Studio (online service)

This topic describes the metrics of AI Studio (online service). Set **Namespace** to **acs_online_service**. Set **Period** to an integral multiple of 60. Default value: **60**. Unit: seconds.

**Task monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|

| loudMonitor |   |   | D | eveloper Guide·Metric |
|---|---|---|---|---|

| Task CPU Usage | core | task.cpu.usage rate _ .sum | taskId | The CPU usage of a task. |
|---|---|---|---|---|
| Task CPU Utilization | % | task.cpu.utilization | taskId | The CPU utilization of a task. |
| Task Working Memory Usage | Bytes | task.memory.workin g set.sum _ | taskId | The working memory usage of a task. |
| Task Memory Utilization | % | task.memory.utilizat ion | taskId | The memory utilization of a task. |
| Task Network Receiving Rate | B/s | task.network.rx rate _ | taskId | The rate at which the network of a task receives data. |
| Task Network Sending Rate | B/s | task.network.tx rate _ | taskId | The rate at which the network of a task sends data. |
| Task DCU Accelerator Card Utilization | % | task.dcu utilizationr _ ate | taskId | The DCU accelerator card utilization of a task. |
| Task DCU Memory Usage | Bytes | task.dcu usedmemo _ ry bytes _ | taskId | The DCU memory usage of a task. |
| Task DCU Memory Utilization | % | task.dcu usedmemo _ ry ratio _ | taskId | The DCU memory utilization of a task. |
| Task GPU Utilization | % | task.DCGM CUSTOM _ PROCESS SM UTIL _ _ _ | taskId | The GPU utilization of a task. |
| Task GPU Memory Usage | MiB | task.DCGM CUSTOM _ PROCESS MEM US _ _ _ ED | taskId | The GPU memory usage of a task. |
| Task GPU Memory Utilization | % | task.DCGM CUSTOM _ PROCESS MEM US _ _ _ ED RATIO _ | taskId | The GPU memory utilization of a task. |

**Pod monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Pod CPU Usage | core | pod.cpu.usage rate _ | taskId,pod name _ | The CPU usage of a pod. |
| Pod CPU Utilization | % | pod.cpu.utilization | taskId,pod name _ | The CPU utilization of a pod. |
| Pod Working Memory Usage | Bytes | pod.memory.workin g set _ | taskId,pod name _ | The working memory usage of a pod. |
| Pod Working Memory Utilization | % | pod.memory.utilizati on | taskId,pod name _ | The memory utilization of a pod. |
| Pod Network Receiving Rate | B/s | pod.network.rx rate _ | taskId,pod name _ | The rate at which a pod receives data. |
| Pod Network Sending Rate | B/s | pod.network.tx rate _ | taskId,pod name _ | The rate at which a pod sends data. |
| Pod DCU Accelerator Card Utilization | % | dcu utilizationrate _ | askId,pod name _ | The DCU accelerator card utilization of a pod. |
| Pod DCU Memory Usage | Bytes | dcu usedmemory b _ _ ytes | taskId,pod name _ | The DCU memory usage of a pod. |
| Pod DCU Memory Utilization | % | dcu usedmemory r _ _ atio | taskId,pod name _ | The DCU memory utilization of a pod. |
| Pod GPU Utilization | % | DCGM CUSTOM PR _ _ OCESS SM UTIL _ _ | taskId,pod name _ | The GPU utilization of a pod. |
| Pod GPU Memory Usage | MiB | DCGM CUSTOM PR _ _ OCESS MEM USED _ _ | taskId,pod name _ | The GPU memory usage of a pod. |
| Pod GPU Memory Utilization | % | DCGM CUSTOM PR _ _ OCESS MEM USED _ _ _ RATIO | taskId,pod name _ | The GPU memory utilization of a pod. |

#### 3.8.2 AI Studio (model evaluation)

This topic describes the metrics of AI Studio (model evaluation). Set **Namespace** to **acs_model_evaluation**. Set **Period** to an integral multiple of **60**. Default value: 60. Unit: seconds.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Task CPU Usage | core | task.cpu.usage r _ ate.sum | taskId | The CPU usage of a task. |
| Task CPU Utilization | % | task.cpu.utilizati on | taskId | The CPU utilization of a task. |
| Task Working Memory Usage | Bytes | task.memory.wo rking set.sum _ | taskId | The working memory usage of a task. |
| Task Memory Utilization | % | task.memory.util ization | taskId | The memory utilization of a task. |
| Task Network Receiving Rate | B/s | task.network.rx r _ ate | taskId | The rate at which the network of a task receives data. |
| Task Network Sending Rate | B/s | task.network.tx r _ ate | taskId | The rate at which the network of a task sends data. |
| Task DCU Accelerator Card Utilization | % | task.dcu utilizati _ onrate | taskId | The DCU accelerator card utilization of a task. |
| Task DCU Memory Usage | Bytes | task.dcu usedm _ emory bytes _ | taskId | The DCU memory usage of a task. |
| Task DCU Memory Utilization | % | task.dcu usedm _ emory bytes _ | taskId | The DCU memory utilization of a task. |
| Task GPU Utilization | % | task.DCGM CUS _ TOM PROCESS S _ _ M UTIL _ | taskId | The GPU utilization of a task. |
| Task GPU Memory Usage | MiB | task.DCGM CUS _ TOM PROCESS _ _ MEM USED _ | taskId | The GPU memory usage of a task. |

| Task GPU Memory Utilization | % | task.DCGM CUS _ TOM PROCESS _ _ MEM USED RATI _ _ O | taskId | The GPU memory utilization of a task. |
|---|---|---|---|---|

#### 3.8.3 AI Studio (Notebook modeling)

This topic describes the metrics of AI Studio (Notebook modeling). Set **Namespace** to **acs_notebook_modeling**. Set **Period** to an integral multiple of **60**. Default value: 60. Unit: seconds.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Task CPU Usage | core | task.cpu.usage r _ ate.sum | taskId | The CPU usage of a task. |
| Task CPU Utilization | % | task.cpu.utilizati on | taskId | The CPU utilization of a task. |
| Task Working Memory Usage | Bytes | task.memory.wo rking set.sum _ | taskId | The working memory usage of a task. |
| Task Memory Utilization | % | task.memory.util ization | taskId | The memory utilization of a task. |
| Task Network Receiving Rate | B/s | task.network.rx r _ ate | taskId | The rate at which the network of a task receives data. |
| Task Network Sending Rate | B/s | task.network.tx r _ ate | taskId | The rate at which the network of a task sends data. |
| Task DCU Accelerator Card Utilization | % | task.dcu utilizati _ onrate | instanceId | The DCU accelerator card utilization of a task. |
| Task DCU Memory Usage | Bytes | task.dcu usedm _ emory bytes _ | instanceId | The DCU memory usage of a task. |
| Task DCU Memory Utilization | % | task.dcu usedm _ emory ratio _ | instanceId | The DCU memory utilization of a task. |

| Task GPU Utilization | % | task.DCGM CUS _ TOM PROCESS S _ _ M UTIL _ | instanceId | The GPU utilization of a task. |
|---|---|---|---|---|
| Task GPU Memory Usage | MiB | task.DCGM CUS _ TOM PROCESS _ _ MEM USED _ | instanceId | The GPU memory usage of a task. |
| Task GPU Memory Utilization | % | task.DCGM CUS _ TOM PROCESS _ _ MEM USED RATI _ _ O | instanceId | The GPU memory utilization of a task. |

#### 3.8.4 AI Studio (task modeling)

This topic describes the metrics of AI Studio (task modeling). Set **Namespace** to **acs_task_modeling**. Set **Period** to an integral multiple of **60**. Default value: 60. Unit: seconds.

**Task monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Task CPU Usage | core | task.cpu.usage rate _ .sum | taskId | The CPU usage of a task. |
| Task CPU Utilization | % | task.cpu.utilization | taskId | The CPU utilization of a task. |
| Task Working Memory Usage | Bytes | task.memory.workin g set.sum _ | taskId | The working memory usage of a task. |
| Task Memory Utilization | % | task.memory.utilizat ion | taskId | The memory utilization of a task. |
| Task Network Receiving Rate | B/s | task.network.rx rate _ | taskId | The rate at which the network of a task receives data. |
| Task Network Sending Rate | B/s | task.network.tx rate _ | taskId | The rate at which the network of a task sends data. |
| Task DCU Accelerator Card Utilization | % | task.dcu utilizationr _ ate | taskId | The DCU accelerator card utilization of a task. |

| Developer Guide·Metrics |   |   |   | CloudMonito |
|---|---|---|---|---|

| Task DCU Memory Usage | Bytes | task.dcu usedmemo _ ry bytes _ | taskId | The DCU memory usage of a task. |
|---|---|---|---|---|
| Task DCU Memory Utilization | % | task.dcu usedmemo _ ry ratio _ | taskId | The DCU memory utilization of a task. |
| Task GPU Utilization | % | task.DCGM CUSTOM _ PROCESS SM UTIL _ _ _ | taskId | The GPU utilization of a task. |
| Task GPU Memory Usage | MiB | task.DCGM CUSTOM _ PROCESS MEM US _ _ _ ED | taskId | The GPU memory usage of a task. |
| Task GPU Memory Utilization | % | task.DCGM CUSTOM _ PROCESS MEM US _ _ _ ED RATIO _ | taskId | The GPU memory utilization of a task. |

**Pod monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Pod CPU Usage | core | pod.cpu.usage rate _ | taskId,pod name _ | The CPU usage of a pod. |
| Pod CPU Utilization | % | pod.cpu.utilization | taskId,pod name _ | The CPU utilization of a pod. |
| Pod Working Memory Usage | Bytes | pod.memory.workin g set _ | taskId,pod name _ | The working memory usage of a pod. |
| Pod Working Memory Utilization | % | pod.memory.utilizati on | taskId,pod name _ | The memory utilization of a pod. |
| Pod Network Receiving Rate | B/s | pod.network.rx rate _ | taskId,pod name _ | The rate at which a pod receives data. |
| Pod Network Sending Rate | B/s | pod.network.tx rate _ | taskId,pod name _ | The rate at which a pod sends data. |

| Pod DCU Accelerator Card Utilization | % | dcu utilizationrate _ | taskId,pod name _ | The DCU accelerator card utilization of a pod. |
|---|---|---|---|---|
| Pod DCU Memory Usage | Bytes | dcu usedmemory b _ _ ytes | taskId,pod name _ | The DCU memory usage of a pod. |
| Pod DCU Memory Utilization | % | dcu usedmemory r _ _ atio | taskId,pod name _ | The DCU memory utilization of a pod. |
| Pod GPU Utilization | % | DCGM CUSTOM PR _ _ OCESS SM UTIL _ _ | taskId,pod name _ | The GPU utilization of a pod. |
| Pod GPU Memory Usage | MiB | DCGM CUSTOM PR _ _ OCESS MEM USED _ _ | taskId,pod name _ | The GPU memory usage of a pod. |
| Pod GPU Memory Utilization | % | DCGM CUSTOM PR _ _ OCESS MEM USED _ _ _ RATIO | taskId,pod name _ | The GPU memory utilization of a pod. |

#### 3.8.5 AI Studio (visual modeling)

This topic describes the metrics of AI Studio (visual modeling). Set the **Namespace** parameter to **acs_pipeline_draft**. Set the **Period** parameter to the default value **60** or an integer multiple of 60. Unit: seconds.

| Console metric | Unit | API metric | Dimension | Description |
|---|---|---|---|---|
| Task CPU usage | core | task.cpu.usage rate. _ sum | taskId | The CPU usage of a task. |
| Task CPU utilization | % | task.cpu.utilization | taskId | The CPU utilization of a task. |
| Task working memory usage | Bytes | task.memory.working set.sum _ | taskId | The working memory usage of a task. |
| Task memory utilization | % | task.memory.utilizati on | taskId | The memory utilization of a task. |
| Task network receiving rate | B/s | task.network.rx rate _ | taskId | The rate at which the network of a task receives data. |

| Task network transmission rate | B/s | task.network.tx rate _ | taskId | The rate at which the network of a task transmits data. |
|---|---|---|---|---|
| Task DCU utilization | % | task.dcu utilizationra _ te | instanceId | The DCU utilization of a task. |
| Task DCU memory usage | Bytes | task.dcu usedmemor _ y bytes _ | instanceId | The DCU memory usage of a task. |
| Task DCU memory utilization | % | task.dcu usedmemor _ y ratio _ | instanceId | The DCU memory utilization of a task. |
| Task GPU utilization | % | task.DCGM CUSTOM _ _ PROCESS SM UTIL _ _ | instanceId | The GPU utilization of a task. |
| Task GPU memory usage | MiB | task.DCGM CUSTOM _ _ PROCESS MEM USED _ _ | instanceId | The GPU memory usage of a task. |
| Task GPU memory utilization | % | task.DCGM CUSTOM _ _ PROCESS MEM USED _ _ RATIO _ | instanceId | The GPU memory utilization of a task. |

#### 3.8.6 AI Studio for model tuning

This topic describes the metrics of AI Studio for model tuning. Set the **Namespace** parameter to **acs_finetune**. Set the **Period** parameter to the default value **60** or an integer multiple of 60. Unit: seconds.

| Console metric | Unit | API metric | Dimension | Description |
|---|---|---|---|---|
| task.cpu.usage rate.s _ um | core | task.cpu.usage rate _ .sum | taskId | The CPU usage of a task. |
| task.cpu.utilization | % | task.cpu.utilization | taskId | The CPU utilization of a task. |
| task.memory.working set.sum _ | Bytes | task.memory.workin g set.sum _ | taskId | The working memory usage of a task. |
| task.memory.utilizati on | % | task.memory.utilizat ion | taskId | The memory utilization of a task. |

| task.network.rx rate _ | B/s | task.network.rx rate _ | taskId | The rate at which the network of a task receives data. |
|---|---|---|---|---|
| task.network.tx rate _ | B/s | task.network.tx rate _ | taskId | The rate at which the network of a task transmits data. |
| task.dcu utilizationrat _ e | % | task.dcu utilizationr _ ate | instanceId | The DCU utilization of a task. |
| task.dcu usedmemor _ y bytes _ | Bytes | task.dcu usedmemo _ ry bytes _ | instanceId | The DCU memory usage of a task. |
| task.dcu usedmemor _ y ratio _ | % | task.dcu usedmemo _ ry ratio _ | instanceId | The DCU memory utilization of a task. |
| task.DCGM CUSTOM _ _ PROCESS SM UTIL _ _ | % | task.DCGM CUSTOM _ PROCESS SM UTIL _ _ _ | instanceId | The GPU utilization of a task. |
| task.DCGM CUSTOM _ _ PROCESS MEM USED _ _ | MiB | task.DCGM CUSTOM _ PROCESS MEM US _ _ _ ED | instanceId | The GPU memory usage of a task. |
| task.DCGM CUSTOM _ _ PROCESS MEM USED _ _ RATIO _ | % | task.DCGM CUSTOM _ PROCESS MEM US _ _ _ ED RATIO _ | instanceId | The GPU memory utilization of a task. |

#### 3.8.7 AI Studio (batch inference)

This topic describes the metrics of AI Studio (batch inference). Set the **Namespace** parameter to **acs_batch_inference**. Set the **Period** to the default value
**60** or an integer multiple of 60. Unit: seconds.

| Console metric | Unit | API metric | Dimension | Description |
|---|---|---|---|---|
| Task CPU usage | core | task.cpu.usage rate _ .sum | taskId | The CPU usage of a task. |
| Task CPU utilization | % | task.cpu.utilization | taskId | The CPU utilization of a task. |

| Task working memory usage | Bytes | task.memory.workin g set.sum _ | taskId | The working memory usage of a task. |
|---|---|---|---|---|
| Task memory utilization | % | task.memory.utilizat ion | taskId | The memory utilization of a task. |
| Task network receiving rate | B/s | task.network.rx rate _ | taskId | The rate at which the network of a task receives data. |
| Task network transmission rate | B/s | task.network.tx rate _ | taskId | The rate at which the network of a task transmits data. |
| Task DCU utilization | % | task.dcu utilizationr _ ate | instanceId | The DCU utilization of a task. |
| Task DCU memory usage | Bytes | task.dcu usedmemo _ ry bytes _ | instanceId | The DCU memory usage of a task. |
| Task DCU memory utilization | % | task.dcu usedmemo _ ry ratio _ | instanceId | The DCU memory utilization of a task. |
| Task GPU utilization | % | task.DCGM CUSTOM _ PROCESS SM UTIL _ _ _ | instanceId | The GPU utilization of a task. |
| Task GPU memory usage | MiB | task.DCGM CUSTOM _ PROCESS MEM US _ _ _ ED | instanceId | The GPU memory usage of a task. |
| Task GPU memory utilization | % | task.DCGM CUSTOM _ PROCESS MEM US _ _ _ ED RATIO _ | instanceId | The GPU memory utilization of a task. |

#### 3.8.8 AI Studio (online service group)

This topic describes the metrics of AI Studio (online service group). Set the **Namespace** parameter to **acs_online_service_group**. Set the **Period** parameter to the default value **60** or an integer multiple of 60. Unit: seconds.

| Console metric | Unit | API metric | Dimension | Description |
|---|---|---|---|---|

| Number of tokens input per second(sum) | Count/s | route upstream mo _ _ del consumer metri _ _ c input token sump _ _ _ m | serviceGroupId,t askId,ai consum _ er | The total number of input tokens per second. |
|---|---|---|---|---|
| Number of tokens input per second | Count/s | route upstream mo _ _ del consumer metri _ _ c input token _ _ | serviceGroupId,t askId,ai consum _ er,ai route _ | The number of input tokens per second. |
| Number of tokens output per second(sum) | Count/s | route upstream mo _ _ del consumer metri _ _ c output token sum _ _ _ pm | serviceGroupId,t askId,ai consum _ er | The total number of output tokens per second. |
| Number of tokens output per second | Count/s | route upstream mo _ _ del consumer metri _ _ c output token _ _ | serviceGroupId,t askId,ai consum _ er,ai route _ | The number of output tokens per second. |
| Response time(sum) | ms | route upstream mo _ _ del consumer metri _ _ c llm service durati _ _ _ on sumpm _ | serviceGroupId,t askId,ai consum _ er | The total response duration. |
| Response time | ms | route upstream mo _ _ del consumer metri _ _ c llm service durati _ _ _ on | serviceGroupId,t askId,ai consum _ er,ai route _ | The response duration. |
| QPS | Count | envoy cluster upstr _ _ eam rq _ | serviceGroupId,t askId | The number of queries per second (QPS). |
| request success rate | % | envoy cluster upstr _ _ eam rq succer rate _ _ _ | serviceGroupId,t askId | The request success rate. |

#### 3.8.9 AI Studio (Resource Pool)

This topic describes the metrics for AI Studio (Resource Pool). The **Namespace** value is **acs_resource_pool**. The default **Period** value is **60** seconds or any integer multiple of 60.

**CPU**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|

| CPU utilization at cluster level | % | cluster.cpu.utilizatio n | cluster | CPU utilization at cluster level. |
|---|---|---|---|---|
| CPU usage at cluster level | cores | cluster.cpu.usage ra _ te | cluster | CPU usage at cluster level. |
| CPU resource limit | cores | cluster.cpu.limit | cluster | CPU resource limit. |
| CPU resource request | cores | cluster.cpu.request | cluster | CPU resource request. |

**Memory**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Memory usage at cluster level | % | cluster.memory.utili zation | cluster | Memory usage at cluster level. |
| Memory request at cluster level | Bytes | cluster.memory.req uest | cluster | Memory request at cluster level. |
| Memory limit at cluster level | Bytes | cluster.memory.limi t | cluster | Memory limit at cluster level. |

**File system**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| File system limit at cluster level | Bytes | cluster.filesystem.li mit | cluster | File system limit at cluster level. |
| Available file system size at cluster level | Bytes | cluster.filesystem.av ailable | cluster | Available file system size at cluster level. |

**GPU**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| GPU memory usage at cluster level | MiB | cluster.DCGM CUST _ OM PROCESS MEM _ _ _ USED | cluster,device | GPU memory usage at cluster level. |

| GPU memory utilization at cluster level | % | cluster.DCGM CUST _ OM PROCESS MEM _ _ _ USED RATIO _ | cluster,device | GPU memory utilization at cluster level. |
|---|---|---|---|---|
| GPU utilization at cluster level | % | cluster.DCGM CUST _ OM PROCESS SM U _ _ _ TIL | cluster,device | GPU utilization at cluster level. |

#### 3.8.10 A-Speed (High-Performance Inference Service)

**Service)**

This topic describes the monitoring metrics for A-Speed (High-Performance Inference Service). The **Namespace** is **acs_aspeed**. The **Period** defaults to **60** seconds and can be set to any integer multiple of 60.

**Overview**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Requests per second (QPS) | reqps | asllm num requests _ _ total _ | instanceId,model name _ | The number of requests per second (QPS). |
| Running requests | short | num running reqs _ _ | instanceId,model name _ | The number of running requests. |
| Queued requests | short | num queue reqs _ _ | instanceId,model name _ | The number of queued requests. |
| KV Cache hit rate | percent | cache hit rate _ _ | instanceId,model name _ | The KV Cache hit rate. |
| KV Cache usage | percent | token usage _ | instanceId,model name _ | The KV Cache usage. |
| Total input token length | short | llm input tokens tot _ _ _ al | instanceId,model name _ | The total length of input tokens. |
| Average input token length | short | llm input tokens av _ _ _ g | instanceId,model name _ | The average length of input tokens. |

| Input token length P90 | short | llm input tokens p9 _ _ _ 0 | instanceId,model name _ | The 90th percentile of input token length. |
|---|---|---|---|---|
| Input token length P99 | short | llm input tokens p9 _ _ _ 9 | instanceId,model name _ | The 99th percentile of input token length. |
| Total output token length | short | llm output tokens t _ _ _ otal | instanceId,model name _ | The total length of output tokens. |
| Average output token length | short | llm output tokens a _ _ _ vg | instanceId,model name _ | The average length of output tokens. |
| Output token length P90 | short | llm output tokens p _ _ _ 90 | instanceId,model name _ | The 90th percentile of output token length. |
| Output token length P99 | short | llm output tokens p _ _ _ 99 | instanceId,model name _ | The 99th percentile of output token length. |
| Average E2E latency | short | llm e2e latency avg _ _ _ ms _ | instanceId,model name _ | The average end-to- end latency. |
| E2E latency P90 | short | llm e2e latency p90 _ _ _ ms _ | instanceId,model name _ | The 90th percentile of end-to-end latency. |
| E2E latency P99 | short | llm e2e latency p99 _ _ _ ms _ | instanceId,model name _ | The 99th percentile of end-to-end latency. |
| Average TTFT | short | llm ttft avg ms _ _ _ | instanceId,model name _ | The average time to first token (TTFT). |
| TTFT P50 | short | llm ttft p50 ms _ _ _ | instanceId,model name _ | The 50th percentile of time to first token (TTFT). |
| TTFT P90 | short | llm ttft p90 ms _ _ _ | instanceId,model name _ | The 90th percentile of time to first token (TTFT). |

| TTFT P99 | short | llm ttft p99 ms _ _ _ | instanceId,model name _ | The 99th percentile of time to first token (TTFT). |
|---|---|---|---|---|
| Average TPOT | short | llm tpot avg ms _ _ _ | instanceId,model name _ | The average time per output token (TPOT). |
| TPOT P90 | short | llm tpot p90 ms _ _ _ | instanceId,model name _ | The 90th percentile of time per output token (TPOT). |
| TPOT P99 | short | llm tpot p99 ms _ _ _ | instanceId,model name _ | The 99th percentile of time per output token (TPOT). |

**Decode view**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Running requests | short | llm running request _ _ s count _ | instanceId,model name,pod,role _ | The number of running requests. |
| Average output token throughput | short | llm output token th _ _ _ roughput per sec _ _ | instanceId,model name,pod,role _ | The average output token throughput. |
| Average TTFT | short | llm first ttft avg ms _ _ _ _ | instanceId,model name,pod,role _ | The average time to first token (TTFT). |
| TTFT P50 | short | llm first ttft p50 ms _ _ _ _ | instanceId,model name,pod,role _ | The 50th percentile of time to first token (TTFT). |
| TTFT P90 | short | llm first ttft p90 ms _ _ _ _ | instanceId,model name,pod,role _ | The 90th percentile of time to first token (TTFT). |
| TTFT P99 | short | llm first ttft p99 ms _ _ _ _ | instanceId,model name,pod,role _ | The 99th percentile of time to first token (TTFT). |
| Average TPOT | short | llm first tpot avg m _ _ _ _ s | instanceId,model name,pod,role _ | The average time per output token (TPOT). |

| TPOT P90 | short | llm first tpot p90 m _ _ _ _ s | instanceId,model name,pod,role _ | The 90th percentile of time per output token (TPOT). |
|---|---|---|---|---|
| TPOT P99 | short | llm first tpot p99 m _ _ _ _ s | instanceId,model name,pod,role _ | The 99th percentile of time per output token (TPOT). |
| KV Cache usage | short | llm gpu vram pool _ _ _ _ usage percent deco _ _ de | instanceId,model name,pod,role _ | The KV Cache usage during the decode phase. |

**Prefill view**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Input token throughput | short | llm input token thr _ _ _ oughput per sec _ _ | instanceId,model name,pod,role _ | The input token throughput. |
| Queued requests | short | llm queued request _ _ s count _ | instanceId,model name,pod,role _ | The number of queued requests during the prefill phase. |
| KV Cache hit rate | short | llm kv cache hit rat _ _ _ _ e percent _ | instanceId,model name,pod,role _ | The KV Cache hit rate during the prefill phase. |
| KV Cache usage | short | llm gpu vram pool _ _ _ _ usage percent prefi _ _ ll | instanceId,model name,pod,role _ | The KV Cache usage during the prefill phase. |

#### 3.8.11 Elastic Fault Tolerance Service

This topic lists the metrics for Elastic Fault Tolerance Service. The **Namespace** is **acs_kea**. The default **Period** is **60** seconds and must be an integer multiple of 60.

**Model monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Single-GPU TFLOPS | N/A | TFLOPS | instanceId | Measures the number of floating- point operations per second for a single GPU. |

| Training loss | N/A | Loss | instanceId | Measures the training loss. |
|---|---|---|---|---|

**Basic monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| CPU utilization | % | TASK CPU USAGE _ _ | instanceId,userId | Measures the CPU utilization. |
| Memory utilization | % | TASK MEM USAGE _ _ | instanceId,userId | Measures the memory utilization. |
| Disk utilization | % | TASK DISK USAGE _ _ | instanceId,userId | Measures the disk utilization. |
| 1-minute system load | short | TASK LOAD1 _ | instanceId,userId | Measures the average system load over the last 1 minute. |
| 5-minute system load | short | TASK LOAD5 _ | instanceId,userId | Measures the average system load over the last 5 minutes. |
| 15-minute system load | short | TASK LOAD15 _ | instanceId,userId | Measures the average system load over the last 15 minutes. |
| Network outbound bandwidth | MB/s | TASK NETWORK TX _ _ | instanceId,userId | Measures the outbound data transfer rate. |
| Network inbound bandwidth | MB/s | TASK NETWORK RX _ _ | instanceId,userId | Measures the inbound data transfer rate. |
| Number of TCP connections | short | TASK TCP ESTAB _ _ | instanceId,userId | Measures the number of TCP connections in the ESTABLISHED state. |

**GPU monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| GPU memory clock speed | Hz | TASK GPU MEM CL _ _ _ OCK | instanceId,userId ,gpu | Measures the GPU memory clock speed. |
| GPU SM clock speed | Hz | TASK GPU SM CLOC _ _ _ K | instanceId,userId ,gpu | Measures the streaming multiprocessor (SM) clock speed of the GPU. |
| GPU framebuffer usage | % | TASK GPU FB USAG _ _ _ E | instanceId,userId ,gpu | Measures the GPU framebuffer usage. |
| GPU decoder utilization | % | TASK GPU DEC USA _ _ _ GE | instanceId,userId ,gpu | Measures the percentage of time the GPU's decoder engine was active. |
| GPU encoder utilization | % | TASK GPU ENC USA _ _ _ GE | instanceId,userId ,gpu | Measures the percentage of time the GPU's encoder engine was active. |
| GPU utilization | % | TASK GPU USAGE _ _ | instanceId,userId ,gpu | Measures the percentage of time one or more GPU kernels were executing. |
| GPU power | W | TASK GPU POWER _ _ _ USAGE | instanceId,userId ,gpu | Measures the power consumption of the GPU. |
| GPU temperature | °C | TASK GPU TEMP _ _ | instanceId,userId ,gpu | Measures the core temperature of the GPU. |

**RDMA monitoring**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|

| Number of peer RNR NAK packets | short | TASK RDMA RNR N _ _ _ AK | instanceId,userId ,minor | Measures the number of received peer Receiver Not Ready (RNR) Negative Acknowledgment (NAK) packets. |
|---|---|---|---|---|
| Local RDMA CQE errors | short | TASK RDMA CQE ER _ _ _ ROR | instanceId,userId ,minor | Measures the number of local Completion Queue Entry (CQE) errors. |
| RDMA out-of- sequence datagrams | short | TASK RDMA OOS _ _ | instanceId,userId ,minor | Measures the number of out-of- sequence RDMA datagrams received. |
| RDMA buffer overruns | short | TASK RDMA OOB _ _ | instanceId,userId ,minor | Measures the number of RDMA buffer overruns. |
| RDMA network receive throughput | MB/s | TASK RDMA RX BYT _ _ _ ES | instanceId,userId ,minor | Measures the data receive rate over the RDMA network. |
| RDMA network transmit throughput | MB/s | TASK RDMA TX BYT _ _ _ ES | instanceId,userId ,minor | Measures the data transmit rate over the RDMA network. |
