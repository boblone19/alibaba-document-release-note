---
title: "Alibaba Cloud Apsara Stack V3.18.3 CloudMonitor Developer Guide 20250304"
product_version: "V3.18.3"
doc_version: "20250304"
pdf_pages: 431
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 CloudMonitor Developer Guide 20250304.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E7%9B%91%E6%8E%A7CMS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20CloudMonitor%20Developer%20Guide%2020250304.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 CloudMonitor Developer Guide 20250304

## Table of Contents

- 1 API Reference
  - 1.1 Monitoring data on time series metrics of cloud services
    - 1.1.1 DescribeMetricLast
    - 1.1.2 DescribeMetricList
    - 1.1.3 DescribeMetricMetaList
    - 1.1.4 DescribeProjectMeta
    - 1.1.5 DescribeMetricData
    - 1.1.6 DescribeMetricTop
  - 1.2 Custom monitoring
    - 1.2.1 PutCustomMetric
    - 1.2.2 DescribeCustomMetricList
    - 1.2.3 DeleteCustomMetric
  - 1.3 Host monitoring
    - 1.3.1 DescribeMonitoringAgentStatuses
    - 1.3.2 DescribeMonitoringAgentHosts
    - 1.3.3 InstallMonitoringAgent
    - 1.3.4 DescribeMonitoringAgentProcesses
    - 1.3.5 PutMonitoringConfig
    - 1.3.6 DeleteMonitoringAgentProcess
    - 1.3.7 CreateMonitoringAgentProcess
    - 1.3.8 DescribeMonitoringConfig
    - 1.3.9 DescribeMonitoringAgentAccessKey
    - 1.3.10 UninstallMonitoringAgent
  - 1.4 Alert service
    - 1.4.1 DescribeAlertHistoryList
    - 1.4.2 DescribeMetricRuleList
    - 1.4.3 PutResourceMetricRule
    - 1.4.4 DescribeMetricRuleCount
    - 1.4.5 DeleteMetricRules
    - 1.4.6 DisableMetricRules
    - 1.4.7 DescribeAlertingMetricRuleResources
    - 1.4.8 DeleteMetricRuleResources
    - 1.4.9 EnableMetricRules
    - 1.4.10 DeleteContact
    - 1.4.11 DescribeMetricRuleTargets
    - 1.4.12 DescribeEventRuleList
    - 1.4.13 DescribeMetricRuleTemplateList
    - 1.4.14 DescribeContactList
    - 1.4.15 ApplyMetricRuleTemplate
    - 1.4.16 DescribeEventRuleTargetList
    - 1.4.17 DescribeMetricRuleTemplateAttribute
    - 1.4.18 DescribeEventRuleAttribute
    - 1.4.19 DescribeContactListByContactGroup
    - 1.4.20 PutContact
    - 1.4.21 PutContactGroup
    - 1.4.22 PutGroupMetricRule
    - 1.4.23 CreateMetricRuleResources
    - 1.4.24 DescribeContactGroupList
    - 1.4.25 DeleteMetricRuleTemplate
    - 1.4.26 PutEventRuleTargets
    - 1.4.27 CreateMetricRuleTemplate
    - 1.4.28 CreateGroupMetricRules
    - 1.4.29 PutResourceMetricRules
    - 1.4.30 DeleteEventRules
    - 1.4.31 ModifyMetricRuleTemplate
    - 1.4.32 PutMetricRuleTargets
  - 1.5 Event monitoring
    - 1.5.1 DescribeSystemEventHistogram
    - 1.5.2 DescribeSystemEventAttribute
    - 1.5.3 DescribeSystemEventCount
    - 1.5.4 SendDryRunSystemEvent
    - 1.5.5 PutCustomEvent
    - 1.5.6 DescribeSystemEventMetaList
    - 1.5.7 DescribeCustomEventCount
    - 1.5.8 DescribeCustomEventAttribute
  - 1.6 Application group
    - 1.6.1 DescribeMonitorGroups
    - 1.6.2 DescribeMonitorGroupInstances
    - 1.6.3 CreateMonitorGroupInstances
    - 1.6.4 DescribeUnhealthyHostAvailability
    - 1.6.5 DeleteMonitorGroupInstances
    - 1.6.6 DescribeMonitorGroupInstanceAttribute
    - 1.6.7 DescribeHostAvailabilityList
    - 1.6.8 CreateMonitorGroup
    - 1.6.9 DeleteMonitorGroup
    - 1.6.10 CreateHostAvailability
    - 1.6.11 CreateMonitorGroupNotifyPolicy
    - 1.6.12 DeleteHostAvailability
    - 1.6.13 DescribeMonitorGroupCategories
    - 1.6.14 ModifyMonitorGroupInstances
    - 1.6.15 ModifyHostAvailability
    - 1.6.16 PutMonitorGroupDynamicRule
    - 1.6.17 ModifyMonitorGroup
    - 1.6.18 DeleteMonitorGroupDynamicRule
    - 1.6.19 DeleteMonitorGroupNotifyPolicy
    - 1.6.20 DescribeMonitorGroupNotifyPolicyList
  - 1.7 Site monitoring
    - 1.7.1 DescribeSiteMonitorData
    - 1.7.2 DescribeSiteMonitorStatistics
    - 1.7.3 DescribeSiteMonitorList
    - 1.7.4 DescribeSiteMonitorISPCityList
    - 1.7.5 CreateSiteMonitor
    - 1.7.6 DescribeSiteMonitorAttribute
    - 1.7.7 DisableSiteMonitors
    - 1.7.8 EnableSiteMonitors
    - 1.7.9 DeleteSiteMonitors
    - 1.7.10 ModifySiteMonitor
- 2 Metrics for Apsara Stack services
  - 2.1 Elastic computing
    - 2.1.1 ECS
    - 2.1.2 BMCP nodes
    - 2.1.3 BMCP containers
  - 2.2 Database services
    - 2.2.1 ApsaraDB RDS
    - 2.2.2 ApsaraDB RDS (New)
    - 2.2.3 PolarDB
    - 2.2.4 PolarDB databases that use local SSDs
    - 2.2.5 PolarDB-X 2.0
      - 2.2.5.1 Compute nodes of PolarDB-X 2.0
      - 2.2.5.2 Data nodes of PolarDB-X 2.0
    - 2.2.6 PolarDB-X 1.0
    - 2.2.7 ApsaraDB for MongoDB (Old)
    - 2.2.8 ApsaraDB for MongoDB (New)
    - 2.2.9 Tair (Redis OSS-compatible) (Old)
    - 2.2.10 Tair (Redis OSS-compatible) (New)
    - 2.2.11 DTS
  - 2.3 Storage and CDN
    - 2.3.1 NAS
    - 2.3.2 OSS
    - 2.3.3 Tablestore
  - 2.4 Network
    - 2.4.1 NAT Gateway
    - 2.4.2 SLB
    - 2.4.3 EIP
    - 2.4.4 VPN Gateway
    - 2.4.5 DNS
  - 2.5 Application services
    - 2.5.1 API Gateway
  - 2.6 Middleware services
    - 2.6.1 ApsaraMQ for RocketMQ
  - 2.7 Big data
    - 2.7.1 Stream Computing (Blink)
    - 2.7.2 DataHub
  - 2.8 Security (Apsara Stack Security)
    - 2.8.1 Tenant-side bastion hosts
    - 2.8.2 Vulnerability scanner engines

## 1 API Reference

### 1.1 Monitoring data on time series metrics of cloud services

**metrics of cloud services**

#### 1.1.1 DescribeMetricLast

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

#### 1.1.2 DescribeMetricList

Queries the monitoring data of a time series metric for a cloud service within a specific period of time. For more information about the values of parameters such as Namespace, Project, Metric, Period, and Dimensions for each cloud service, see "Metrics for Apsara Stack services".

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetricLi st | The operation that you want to perform. Set the value to DescribeMetricList. |
| MetricName | String | Yes | cpu idle _ | The name of the monitoring metric. |
| Namespace | String | Yes | acs ecs dashbo _ _ ard | The namespace of the service. This parameter is used to differentiate services. Format: acs service name. _ |
| Dimensions | String | Yes | [{"instanceId": "i- abcdefgh12****" }] | The dimensions based on which the monitoring data of the specified resource is queried. The value is a collection of key-value pairs. A typical key-value pair is instanceId:XXXXXX. You can specify up to 10 instance IDs in each call. Each key or value can be 1 to 64 bytes in length. A key or value that contains more than 64 characters is truncated and the first 64 bytes are retained. The key and value can contain letters, digits, periods (.), hyphens (-), underscores ( ), forward _ slashes (/), and backslashes (\). Note If you set Dimensions to ordered strings in the request, the value of this parameter is a key-value map expressed in JSON strings. |

| EndTime | String | No | 2019-01-30 00:10:00 | The end of the time range to query. The following formats are supported: UNIX timestamp: the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. UTC time: the UTC time in the YYYY-MM-DDThh:mm:ssZ format. |   |
|---|---|---|---|---|---|
| Express | String | No | {"groupby": ["userId","instan ceId"]} | The expression that is used to calculate the query results in real time. Only the groupby expression is supported. This expression is similar to the GROUP BY statement that is used in databases. |   |
| Length | String | No | 1000 | The number of entries per page. Default value: 1000. |   |
| NextToken | String | No | 1576148535000 9dd70bb64cff1f 0fff750b08ffff07 3be5fb1e785e2 b020f1a949d5e a14aea7fed82f0 1dd87311 | The pagination token. Note You do not need to specify this parameter if you only want to query entries on the first page. This pagination token can be used as a request parameter to retrieve a new page of results. If null is returned, all query results are returned. |   |

|   | BY |
|---|---|

| Period | String | No | 60 | The interval at which the monitoring data is queried. Unit: seconds. Valid values: 60, 300, and 900, which represent 1 minute, 5 minutes, and 15 minutes, respectively. Note Specify this parameter based on your business requirements. For example, if you set this parameter to 60, only 1,000 records are returned, though a total of 1,440 records are generated. This is because the maximum number of records that can be returned for each query is 1,000. If you set this parameter to 300, 288 records are returned. |
|---|---|---|---|---|
| StartTime | String | No | 2019-01-30 00:00:00 | The beginning of the time range to query. The following formats are supported: UNIX timestamp: the number of seconds that have elapsed since 00:00:00 Thursday, January 1, 1970. UTC time: the UTC time in the YYYY-MM-DDThh:mm:ssZ format. Note The period specified by StartTime and EndTime includes the time point specified by EndTime but does not include the time point specified by StartTime. StartTime must be earlier than EndTime. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3121AE7D-4AFF- 4C25-8F1D- C8226EBB1F42 | The request ID. |

| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the request was successful. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. |
| NextToken | String | 15761441850009d d70bb64cff1f0fff6d 0b08ffff073be5fb1 e785e2b020f7fed9 b5e137bd810a6d6 cff5aee816 | The pagination token. Note You do not need to specify this parameter if you only want to query entries on the first page. This pagination token can be used as a request parameter to retrieve a new page of results. If null is returned, all query results are returned. |
| Period | String | 60 | The interval at which monitoring data was queried. Unit: seconds. Valid values: 60, 300, and 900. |
| Datapoints | String | [{"timestamp":154 8777660000,"userI d":"123","instanceI d":"i- abc","Minimum":9. 92,"Average":9.92, "Maximum":9.92}] | The monitoring data. |
| Message | String | Success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricList &MetricName=cpu_idle &Namespace=acs_ecs_dashboard &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Period>60</Period> <Datapoints> <timestamp>1490152860000</timestamp>
```

```xml
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
    <Average>99.42</Average>
</Datapoints>
```

`p`

```xml
<Datapoints>
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
   "userId":"123456789876****",
"instanceId":"i-abcdefgh12****"
```

```json
   instanceId:i-abcdefgh12****,
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
```

`a` `u`

```json
:00,
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

#### 1.1.3 DescribeMetricMetaList

Queries the descriptions of time series metrics that are supported by CloudMonitor. This operation is used together with DescribeMetricList or DescribeMetricLast.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetricM etaList | The operation that you want to perform. Set the value to DescribeMetricMetaList. |
| Namespace | String | Yes | acs kvstore _ | The namespace of the monitored service. You can call the DescribeProjectMeta operation to query the namespace of each service. |

|   |   |   |   |   |   | The tags of the metric. Specify the tags in the following format: [{"name":"Tag |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | [{"name":"Tag |   |
|   |   |   |   |   |   | name","value":"Tag value"}, |   |   |
|   |   |   |   |   |   | {"name":"Tag name","value":"Tag |   |   |
|   |   |   |   |   |   | value"}] |   |   |
| Labels |   | String | No | [{"name":"prod uctCategory","v alue":"kvstore o _ ld"}] |   |   |   |   |
| MetricName |   | String | No | CPUUtilization |   | The name of the metric. The metric with the specified name is matched. |   |   |
| PageNumber |   | Integer | No | 1 |   | The page number. Default value: 1. |   |   |
| PageSize |   | Integer | No | 30 |   | The number of entries per page. Default value: 30. |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. |
| Code | String | 200 | The status code. The value 200 indicates that the request is successful. |
| RequestId | String | 0CCE0AF0-053C- 4B13-A583- DC9A85785D49 | The request ID, which can be used for troubleshooting. |
| Message | String | success | The error message. |
| Resources |   |   | The information about metrics found. |

| Resource |   |   |   | The information about a metric found. |   |   |
|---|---|---|---|---|---|---|
| Description | String |   | CPUUtilization | The description of the metric. |   |   |
| Dimensions | String |   | instanceId | The dimensions of the metric. Multiple dimensions are separated by commas (,). |   |   |
| Labels | String |   |   | The tags of the metric. The value is a JSON string in the following format: [{"name":"Tag name","value":"Tag value"}] . The string can include repeated tag names. The following tag names are available: metricCategory: the category of the metric. alertEnable: indicates whether the alert is enabled. alertUnit: the unit of the metric in the alert. unitFactor: the factor for metric unit conversion. minAlertPeriod: the minimum interval at which the alert is reported. productCategory: the category of the service. |   |   |
|   |   |   |   |   | [{"name":"Tag name","value":"Tag |   |
|   |   |   | [{"name":"alertUni t","value":"Bytes"}, | value"}] |   |   |
|   |   |   | {"name":"minAlert Period","value":"60 "}, {"name":"metricCa tegory","value":"in stanceId"}, {"name":"instance Type","value":"disa ster"}, {"name":"is alarm _ ","value":"true"}, {"name":"productC ategory","value":"k vstore old"}] _ |   |   |   |
| MetricName | String |   | CPUUtilization | The name of the metric. |   |   |
| Namespace | String |   | acs kvstore _ | The namespace of the monitored service. The namespace is in the acs Service _ name format. |   |   |
| Periods | String |   | 60,300 | The statistical period of the metric. Multiple periods are separated by commas (,). Example: 15,60,900. |   |   |
| Statistics | String |   | Average,Minimum, Maximum | The statistical method of the metric. Multiple methods are separated by commas (,). Example: Maximum,Minimum,Average. |   |   |
| Unit | String |   | % | The unit of the metric. |   |   |
| TotalCount | String |   | 12 | The total number of entries returned. |   |   |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricMetaList &Namespace=acs_ecs_dashboard &<Common request parameters>
```

Sample success responses

> **Note:** The response content varies based on the monitored service.

`XML` format

```json
<DescribeMetricMetaListResponse>
    <TotalCount>120</TotalCount>
    <RequestId>EA94B362-973C-4D6B-BE94-6774E18915C2</RequestId>
    <Success>true</Success>
    <Code>200</Code>
    <Resources>
        <Resource>
            <Description>ECS.CPUUtilization</Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>CPUUtilization</MetricName>
            <Labels>[{"name":"alertUnit","value":"%"},
{"name":"alertDefault","value":"80"},{"name":"minAlertPeriod","value":"60"}, {"name":"metricCategory","value":"instanceId"},{"name":"is_alarm","value":"true"}]</Lab els>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>%</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Maximum,Minimum</Statistics>
            <MetricName>DiskReadBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},
{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"name": "metricCategory","value":"instanceId"},{"name":"is_alarm","value":"true"}]</Labels>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description>The read IOPS of the system disk</Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>DiskReadIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"instanceId"},{ "name":"is_alarm","value":"true"}]</Labels>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>Count/Second</Unit>
```

```json
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Maximum,Minimum</Statistics>
            <MetricName>DiskWriteBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},
{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"name": "metricCategory","value":"instanceId"},{"name":"is_alarm","value":"true"}]</Labels>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description>The write IOPS of the system disk</Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>DiskWriteIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"instanceId"},{ "name":"is_alarm","value":"true"}]</Labels>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>Count/Second</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupCPUUtilization</MetricName>
            <Labels>[{"name":"alertUnit","value":"%"},
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"groupId"}]</La bels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>%</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskReadBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},
{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"name": "metricCategory","value":"groupId"}]</Labels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskReadIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},
```

`{"`

```
""iAl
```

`tP`

```
id""
```

`l`

```
""60"}{"
```

`"``"`

```
tiCt
```

`"``"` `l` `"``"`

```
Id"}]</L
```

```json
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"groupId"}]</La bels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>Count/Second</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskWriteBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},
{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"name": "metricCategory","value":"groupId"}]</Labels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskWriteIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"groupId"}]</La bels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>Count/Second</Unit>
        </Resource>
    </Resources>
</DescribeMetricMetaListResponse>
```

`JSON` format `{`

```json
 "TotalCount":1853,
 "RequestId":"CDE9EAFF-D54E-4024-BBFC-B0AAC883143B",
 "Success":true,
 "Code":200,
 "Resources":{
  "Resource":[
```

`{`

```json
    "Description":"The disk size",
    "MetricName":"ads.diskSize",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"300\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"Mbytes\"}, {\"name\":\"productCategory\",\"value\":\"ads\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"workerId\"}]",
    "Dimensions":"userId,instanceId,tableSchema,workerId",
```

```json
    "Namespace":"acs_ads",
    "Periods":"300",
    "Unit":"Mbytes"
```

`},` `{`

```json
    "Description":"The used disk space",
    "MetricName":"ads.diskUsed",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"300\"}, {\"name\":\"metricCategory\",\"value\":\"workerId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId,tableSchema,workerId",
    "Namespace":"acs_ads",
    "Periods":"300",
    "Unit":"Mbytes"
```

`},` `{`

```json
    "Description":"The disk usage",
    "MetricName":"ads.diskUsedPercent",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},
{\"name\":\"minAlertPeriod\",\"value\":\"300\"}, {\"name\":\"metricCategory\",\"value\":\"workerId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId,tableSchema,workerId",
    "Namespace":"acs_ads",
    "Periods":"300",
    "Unit":"%"
```

`},` `{`

```json
    "Description":"The number of messages that are not consumed in the queue",
    "MetricName":"QueueMessageAccumulation",
    "Statistics":"Maximum",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"queue\"}]",
    "Dimensions":"userId,regionId,vhostName,queueName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"The number of new messages in the queue per minute",
    "MetricName":"QueueMessageInput",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"n ame\":\"unitFactor\",\"value\":\"1\"},{ \"name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"}, {\"name\":\"is_alarm\",\"value\":\"true\"},
```

\ \ \ \ \ \ \ \

```json
{\"name\":\"metricCategory\",\"value\":\"queue\"}]",
    "Dimensions":"userId,regionId,vhostName,queueName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"The number of messages that are not consumed in the queue",
    "MetricName":"QueueMessageOutput",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"queue\"}]",
    "Dimensions":"userId,regionId,vhostName,queueName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"The number of messages generated by the instance per minute",
    "MetricName":"VhostMessageInput",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"vhost\"}]",
    "Dimensions":"userId,regionId,vhostName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"The number of messages consumed by the instance per minute",
    "MetricName":"VhostMessageOutput",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"vhost\"}]",
    "Dimensions":"userId,regionId,vhostName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"Latency",
"Statistics":"Average"
```

```json
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"ms\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300,900",
    "Unit":"ms"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"SumQPS",
    "Statistics":"Count",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300,900",
    "Unit":"Count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"TrafficRX",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"KBytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300,900",
    "Unit":"KBytes"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"TrafficTX",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"KBytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300,900",
    "Unit":"KBytes"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"code2XX",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
```

```json
{\name\:\minAlertPeriod\,\value\:\60\}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300",
    "Unit":"count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"code4XX",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"tru\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300",
    "Unit":"count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"code5XX",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300",
    "Unit":"count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_rx.Pkgs",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"pps\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"pps"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_rx.rate",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1048576\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"},
```

```json
{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"bits/s"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_tx.Pkgs",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"pps\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"pps"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_tx.rate",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1048576\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"bits/s"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_tx.ratePercent",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"%"
```

`},` `{`

```json
    "Description":"The maximum network traffic per unit time",
    "MetricName":"BPS",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1000000\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"},
```

```json
{\"name\":\"unitFactor\",\"value\":\"1000\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"bits/s"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"GroupBPS",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1000000\"}, {\"name\":\"metricCategory\",\"value\":\"groupId\"}, {\"name\":\"unitFactor\",\"value\":\"1000\"}]",
    "Dimensions":"userId,groupId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"bits/s"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"GroupInternetOut",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1000000\"}, {\"name\":\"metricCategory\",\"value\":\"groupId\"}, {\"name\":\"unitFactor\",\"value\":\"1000\"}]",
    "Dimensions":"userId,groupId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"bytes"
```

`},` `{`

```json
    "Description":"The downstream traffic",
    "MetricName":"InternetOut",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1000000\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"unitFactor\",\"value\":\"1000\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"bytes"
```

`},` `{`

```json
    "Description":"The average number of accesses within the specified time range",
    "MetricName":"QPS",
    "Statistics":"Average,Minimum,Maximum",
```

```json
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"Count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"UserQPS",
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"alertDefault\",\"value\":\"Count\"}, {\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"userId\"}]",
    "Dimensions":"userId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":""
```

`},` `{`

```json
    "Description":"",
    "MetricName":"Usercode4xx",
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"userId\"}]",
    "Dimensions":"userId",
    "Namespace":"acs_cdn",
    "Periods":"60",
    "Unit":"Count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"Usercode5xx",
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"userId\"}]",
    "Dimensions":"userId",
    "Namespace":"acs_cdn",
    "Periods":"60",
    "Unit":"Count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"UserhitRate",
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"userId\"}]",
    "Dimensions":"userId",
"Namespace""acscdn"
```

```json
    "Namespace":"acs_cdn",
    "Periods":"60",
    "Unit":"%"
```

`},` `{`

```json
    "Description":"The percentage of 4XX HTTP status codes over total status codes with
in the specified time range",
    "MetricName":"code4xx",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"%"
```

`}` `]` `}` `}`

#### 1.1.4 DescribeProjectMeta

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
|   | Total | String |   |   | 12 | The total number of entries. |   |   |

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

#### 1.1.5 DescribeMetricData

Queries the monitoring data of a metric for a specified cloud service.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Namespac e | Strin g | Query | Yes | acs ecs dashboard _ _ | The namespace of the cloud service. For more information about the namespaces of cloud services, see Appendix 1: Metrics. |
| MetricNa me | Strin g | Query | Yes | cpu idle _ | The metric that is used to monitor the cloud service. For more information about the metrics of cloud services, see Appendix 1: Metrics. |
| Period | Strin g | Query | No | 60 | The statistical period of the metric. Valid values: 15, 60, 900, and 3600. Unit: seconds. If this parameter is not specified, monitoring data is queried based on the period in which metric values are reported. For more information about the statistical period of a metric that is specified by the MetricName parameter, see Appendix 1: Metrics. |
|   |   |   |   |   | The start of the time range to query monitoring data. If the StartTime and EndTime parameters are not specified, the monitoring data of the last statistical period is queried. |

| Parame ter | Typ e | Locati on | Require d | Example | If the StartTime Deasncdr i pEtnidoTnime parameters are |
|---|---|---|---|---|---|
| StartTime | Strin g | Query | No | 1618368900000 | specified, the monitoring data of the last statistical period in the specified time range is queried. The following examples demonstrate how to determine the period in which monitoring data is queried: If you set the Period parameter to 15, the specified time range must be less than or equal to 20 minutes. For example, if you set the StartTime parameter to 2021- 05-08 08:10:00 and the EndTime parameter to 2021- 05-08 08:30:00, the monitoring data of the last 15 seconds in the time range is queried. If you set the Period parameter to 60 or 900, the specified time range must be less than or equal to 2 hours. For example, if you set the Period parameter to 60, the StartTime parameter to 2021- 05-08 08:00:00, and the EndTime parameter to 2021- 05-08 10:00:00, the monitoring data of the last 60 seconds in the time range is queried. |

|   | StartTime |
|---|---|
| i pEtnidoTnime |   |

| Parame ter | Typ e | Locati on | Require d | Example | If you set the Desc rPieprtiioodn parameter to 3600, |
|---|---|---|---|---|---|
|   |   |   |   |   | the specified time range must be less than or equal to two days. For example, if you set the StartTime parameter to 2021- 05-08 08:00:00 and the EndTime parameter to 2021- 05-10 08:00:00, the monitoring data of the last 3,600 seconds in the time range is queried. The following formats are supported: UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970. UTC time: the UTC time that follows the YYYY-MM- DDThh:mm:ssZ format. You must set the StartTime parameter to a point in time that is later than 00:00:00 UTC on Thursday, January 1, 1970. Otherwise, this |
|   |   |   |   |   | parameter is invalid. The end of the time range to query moWneit orreicnogm dmatean.d that you use UNIX tIf i mth ee s ta mStpasr ttoTime panredv e nEtn tdimTiem ezo ne- rpealraatmede tisesrus easr.e not specified, the monitoring data of the last statistical period is queried. |
| > Document V | ersion: 2 | 0250304 |   |   | 4 |

|   | se UNIX ta mStpasr ttoTime |
|---|---|
| e nEtn tdimTiem ezo n |   |

| Parame ter | Typ e | Locati on | Require d | Example | If the StartTime Deasncdr i pEtnidoTnime parameters are |
|---|---|---|---|---|---|
|   |   |   |   |   | specified, the monitoring data of the last statistical period in the specified time |
| EndTime | Strin g | Query | No | 1618368960000 | range is queried. The following examples demonstrate how to determine the period in which monitoring data is queried: If you set the Period parameter to 15, the specified time range must be less than or equal to 20 minutes. For example, if you set the StartTime parameter to 2021- 05-08 08:10:00 and the EndTime parameter to 2021- 05-08 08:30:00, the monitoring data of the last 15 seconds in the time range is queried. If you set the Period parameter to 60 or 900, the specified time range must be less than or equal to 2 hours. For example, if you set the Period parameter to 60, the StartTime parameter to 2021- 05-08 08:00:00, and the EndTime parameter to 2021- 05-08 10:00:00, the monitoring data of the last 60 seconds in the time range is queried. |

|   | StartTime |
|---|---|
| i pEtnidoTnime |   |

|   | Parame ter | Typ e | Locati on | Require d |   | Example |   | If you set the Desc rPieprtiioodn parameter to 3600, |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | the specified time range must be less than or equal to two days. For example, if you set the StartTime parameter to 2021- 05-08 08:00:00 and the EndTime parameter to 2021- 05-10 08:00:00, the monitoring data of the last 3,600 seconds in the time range is queried. The following formats are supported: UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970. |   |   |
|   | Dimension s | Strin g | Query | No |   | [{"instanceId": "i- abcdefgh12****"}] |   | UTC time: the UTC The dimensions that time that follows the specify the resources YYYY-MM- whose monitoring data DDThh:mm:ssZ you want to query. format. Set the value to a We recommend collection of key-value that you use UNIX pairs. A typical key- timestamps to value pair is prevent time zone- instanceId:i- related issues. 2ze2d6j5uhg20x47**** . You can query a maximum of 50 instances in a single request. |   |   |
|   |   |   |   |   |   |   |   |   | prevent time zone- instanceId:i- related issues. |   |
|   |   |   |   |   |   |   |   | 2ze2d6j5uhg20x47**** |   |   |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Express | Strin g | Query | No | {"groupby": ["userId","instanceId"]} | The expression that is used to compute the query results in real time. Only the groupby expression is supported. This expression is similar to the GROUP BY statement that is used in databases. |
| Length | Strin g | Query | No | 1000 | The number of entries per page. Default value: 1000. The maximum value of the Length parameter in a request is 1440. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |
| RequestId | String | 6A5F022D-AC7C- 460E-94AE- B9E75083D027 | The request ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
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

#### 1.1.6 DescribeMetricTop

Queries the latest monitoring data of a metric for a cloud service. The data can be sorted by a specified order.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| Period | Strin g | Quer y | No | 60 | The statistical period of the monitoring data. Valid values: 15, 60, 900, and 3600. Unit: seconds. If this parameter is not specified, monitoring data is queried based on the period in which metric values are reported. Statistical periods vary based on the metrics that are specified by MetricName . For more information, see Appendix 1: Metrics. |

| Namespac e | Strin g | Quer y | Yes | acs ecs dashboard _ _ | The namespace of the cloud service. For more information about the namespaces of cloud services, see Appendix 1: Metrics. |
|---|---|---|---|---|---|
| MetricNam e | Strin g | Quer y | Yes | cpu idle _ | The metric that is used to monitor the cloud service. For more information about metric names, see Appendix 1: Metrics. |
|   |   |   |   |   | The start of the time range to query monitoring data. If the StartTime and EndTime parameters are not specified, the monitoring data of the last statistical period is queried. If the StartTime and EndTime parameters are specified, the monitoring data of the last statistical period in the specified time range is queried. The following examples demonstrate how to determine the period in which monitoring data is queried: If you set the Period parameter to 15, the specified time range must be less than or equal to 20 minutes. For example, if you set the StartTime parameter to 2021- 05-08 08:10:00 and the EndTime parameter to 2021- 05-08 08:30:00, the monitoring data of the last 15 seconds in the time range is queried. |

|   | StartTime |
|---|---|
| EndTime |   |

|   | StartTime |
|---|---|
| EndTime |   |

| StartTime | Strin g | Quer y | No | 2021-05-08 08:00:00 | If you set the Period parameter to 60 or 900, the specified time range must be less than or equal to 2 hours. For example, if you set the Period parameter to 60, the StartTime parameter to 2021-05-08 08:00:00, and the EndTime parameter to 2021-05-08 10:00:00, the monitoring data of the last 60 seconds in the time range is queried. If you set the Period parameter to 3600, the specified time range must be less than or equal to two days. For example, if you set the StartTime parameter to 2021-05-08 08:00:00 and the EndTime parameter to 2021-05-10 |
|---|---|---|---|---|---|
|   |   |   |   |   | 08:00:00, the monitoring data of the last 3,600 seconds in the time range is queried. The following formats are supported: UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970. UTC time: the UTC time that follows the YYYY- MM-DDThh:mm:ssZ format. You must set the StartTime parameter to a point in time that is later than 00:00:00 UTC on Thursday, January 1, 1970. Otherwise, this parameter is invalid. |

|   |   |   |   |   | We recommend that you use UNIX |
|---|---|---|---|---|---|
| EndTime | Strin g | Quer y | No | 2021-05-08 10:00:00 | timestamps to prevent Thtei mened z oonf eth-ree ltaimteed range to iqsusueerys .monitoring data. If the StartTime and EndTime parameters are not specified, the monitoring data of the last statistical period is queried. If the StartTime and EndTime parameters are specified, the monitoring data of the last statistical period in the specified time range is queried. The following examples demonstrate how to determine the period in which monitoring data is queried: If you set the Period parameter to 15, the specified time range must be less than or equal to 20 minutes. For example, if you set the StartTime parameter to 2021- 05-08 08:10:00 and the EndTime parameter to 2021- 05-08 08:30:00, the monitoring data of the last 15 seconds in the time range is queried. If you set the Period parameter to 60 or 900, the specified time range must be less than or equal to 2 hours. For example, if you set the Period parameter to 60, the StartTime parameter to 2021-05-08 08:00:00, and the EndTime parameter to 2021-05-08 10:00:00, the monitoring data of the last 60 seconds in the time range is queried. |

|   | StartTime |
|---|---|
| EndTime |   |

|   | StartTime |
|---|---|
| EndTime |   |

|   |   |   |   |   | If you set the Period parameter to 3600, the specified time range must be less than or equal to two days. For example, if you set the StartTime parameter to 2021-05-08 08:00:00 and the EndTime parameter to 2021-05-10 08:00:00, the monitoring data of the last 3,600 seconds in the time range is queried. The following formats are supported: UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970. UTC time: the UTC time that follows the YYYY- MM-DDThh:mm:ssZ format. We recommend that you use UNIX timestamps to prevent time zone- related issues. |
|---|---|---|---|---|---|

| Dimension s | Strin g | Quer y |   | No | [{"instanceId": "i- 2ze2d6j5uhg20x47****"} ] |   |   | The monitoring dimensions of the specified resource. Set the value to a collection of key:value pairs. Examples: {"userId":"1208863178 61****"} and {"instanceId":"i- |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   | {"userId":"1208863178 |   |   |
|   |   |   |   |   |   | 2d6j5uhg20x47****"} |   | 61****"} |   |   |   |
|   |   |   |   |   |   |   |   |   |   | and |   |
|   |   |   |   |   |   |   |   | 2ze2d6j5uhg20x47****"} |   |   |   |
| OrgId | Strin g | Quer y |   | No | 1 |   |   | The organization ID. |   |   |   |
| ResourceId | Strin g | Quer y |   | No |   |   |   | The resource ID. |   |   |   |
| Orderby | Strin g | Quer y |   | No | Average |   |   | The field based on which data is sorted. Valid values: Average Minimum Maximum |   |   |   |
| OrderDesc | Strin g | Quer y |   | No | False |   |   | The sorting method. Valid values: True: sorts data in ascending order. False (default): sorts data in descending order. |   |   |   |
| Length | Strin g | Quer y |   | No | 10 |   |   | The number of entries per page. Default value: 10. The maximum value of the Length parameter in a request is 1440. |   |   |   |

| Express | Strin g | Quer y | No | {"groupby": ["userId","instanceId"]} | The expression that is used to compute the query results in real time. Only the groupby expression is supported. This expression is similar to the GROUP BY statement that is used in databases. |
|---|---|---|---|---|---|
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

### 1.2 Custom monitoring

#### 1.2.1 PutCustomMetric

Reports monitoring data.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| MetricList | Repe atLis t | Quer y | Yes |   | The monitoring data. |
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

#### 1.2.2 DescribeCustomMetricList

Queries the reported monitoring data.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupId | Strin g | Query | Yes | 7378**** | The ID of the application group. For information about how to query the IDs of application groups, see DescribeMonitorGroups. |
| MetricNa me | Strin g | Query | No | cpu total _ | The name of the custom metric. |

| CloudMonitor |   |   |   | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|
| Parame ter | Typ e | Locati on | Require d | Example | Description |
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

| Parameter | Type | Example | Description |
|---|---|---|---|
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

| CloudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 1.2.3 DeleteCustomMetric

Deletes the reported monitoring data of a metric.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupId | Strin g | Query | Yes | 3607**** | The ID of the application group. |
| MetricNa me | Strin g | Query | Yes | AdvanceCredit | The metric name. |
| Md5 | Strin g | Query | No | 38796C8CFFEB8F89BB2 A626C7BD7**** | The MD5 value of the HTTP request body. The MD5 value is a 128-bit hash value used to verify the uniqueness of the reported monitoring data. Set the value to the MD5 value returned when you query the reported monitoring data. |
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

### 1.3 Host monitoring

#### 1.3.1 DescribeMonitoringAgentStatuses

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

#### 1.3.2 DescribeMonitoringAgentHosts

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

| Developer Guide·A | PI Reference |   | CloudMonito |
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

#### 1.3.3 InstallMonitoringAgent

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

#### 1.3.4 DescribeMonitoringAgentProcesses

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

#### 1.3.5 PutMonitoringConfig

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

#### 1.3.6 DeleteMonitoringAgentProcess

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

#### 1.3.7 CreateMonitoringAgentProcess

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

| Developer Guide·A | PI Reference |   | CloudMonito |
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

#### 1.3.8 DescribeMonitoringConfig

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

#### 1.3.9 DescribeMonitoringAgentAccessKey

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

#### 1.3.10 UninstallMonitoringAgent

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

### 1.4 Alert service

#### 1.4.1 DescribeAlertHistoryList

Queries historical alerts.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlertHis toryList | The operation that you want to perform. Set the value to DescribeAlertHistoryList. |
| RuleId | String | No | aaaabbb123 | The ID of the alert rule. |
| RuleName | String | No | My Alert Rule | The name of the alert rule. |
| Namespace | String | No | acs ecs dashboa _ _ rd | The namespace of the service. Note For more information, see DescribeMetricMetaList or Metrics. |

| MetricName | String | No | cpu total _ | The name of the metric. Note For more information, see DescribeMetricMetaList or Metrics. |
|---|---|---|---|---|
| GroupId | String | No | 123456 | The ID of the application group. |
| Status | String | No | 2 | Specifies whether to mute alerts. Valid values: 2: Alerts are muted and are not triggered within the silence period, even if the condition specified in the alert rule is met. 0: Alerts can be triggered. |
| State | String | No | ALARM | The alert status. Valid values: ALARM: Alerts are triggered. OK: No alerts are triggered. |
| Ascending | Boolean | No | true | The chronological order in which alerts are sorted. Default value: true. Valid values: true: the reverse chronological order. false: the chronological order. |
| StartTime | String | No | 1554085998000 | The beginning of the time range to query. This value is a UNIX timestamp that represents the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| EndTime | String | No | 1554085998000 | The end of the time range to query. This value is a UNIX timestamp that represents the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| PageSize | Integer | No | 10 | The number of entries per page. |

| Page | Integer | No | 1 | The page number. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 189B35DD-68BA- ******57F0BE12C885 | The request ID. |
| Code | String | 200 | The HTTP status code. The 200 HTTP status code indicates that the request was successful. |
| Success | Boolean | true | Indicates whether the request was successful. Default value: true. Valid values: true false |
| Total | String | 2 | The total number of returned entries. |
| AlarmHistoryList | Array |   | The details of historical alerts. |
| -AlertTime | Long | 1554105040000 | The time when the alert was triggered. |
| -ContactALIIMs | List | My TradeManager | The TradeManager accounts that receive alert notifications. |
| -ContactGroups | List | Alert Contact Groups | The alert contact groups. |
| -ContactMails | List | test@example.com | The email addresses that receive alert notifications. |
| -ContactSmses | List | 12345678900 | The mobile numbers to which the alert notifications were sent. |
| -Contacts | List | My Alert Contacts | The alert contacts. |

| -Dimensions | String | {"instanceId":"i- 2zebwilv3xfdg1****"} | The associated resources. |
|---|---|---|---|
| -EvaluationCount | Integer | 2 | The consecutive number of times for which the metric value is measured before the alert is triggered. |
| -Expression | String | $Average>=1 | The expression that is used to trigger alerts. |
| -GroupId | String | 123456 | The ID of the application group. |
| -InstanceName | String | ali-186xxxx123456 | The instance name. |
| -LastTime | Long | 347020693 | The time when the status last changed. |
| -Level | String | P3 | The alert level. Valid values: P2: Alert notifications are sent by using phone calls, text messages, emails, TradeManager, and DingTalk chatbots. P3: Alert notifications are sent by using text messages, emails, TradeManager, and DingTalk chatbots. P4: Alert notifications are sent by using emails and DingTalk chatbots. |
| -MetricName | String | cpu total _ | The name of the metric. Note For more information, see DescribeMetricMetaList or Metrics. |

| -Namespace | String | acs ecs dashboard _ _ | The namespace of the service. Note For more information, see DescribeMetricMetaList or Metrics. |
|---|---|---|---|
| -RuleId | String | d97a65a7-70d2-4a8a- 97bf-1a9147**** | The ID of the alert rule. |
| -RuleName | String | My Alert | The name of the alert rule. |
| -State | String | ALARM | The alert status. Valid values: ALARM: Alerts are triggered. OK: No alerts are triggered. |
| -Status | Integer | 2 | Indicates whether alerts are muted. Valid values: 2: Alerts are muted and are not triggered within the silence period, even if the condition specified in the alert rule is met. 0: Alerts can be triggered. |
| -Value | String | 5.39 | The threshold based on which the alert was triggered for the metric. |
| -Webhooks | String | http://www.****.com/we bhook.html | The callback URL. |
| Message | String | The Request is not authorization. | The message that is returned for the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlertHistoryList &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribeAlertHistoryList>
   <AlarmHistoryList>
      <AlarmHistory>
         <Value>4.41</Value>
         <LastTime>881140083</LastTime>
         <Webhooks></Webhooks>
         <ContactSmses></ContactSmses>
         <RuleName>test-auto-scaling-0001</RuleName>
         <GroupId>123456</GroupId>
         <AlertName>putNewAlarm_xxxxxx</AlertName>
         <EvaluationCount>1</EvaluationCount>
         <Status>2</Status>
         <AlertState>ALARM</AlertState>
         <MetricName>cpu_total#60</MetricName>
         <ContactMails></ContactMails>
         <AlertTime>1554986620000</AlertTime>
         <Dimensions>{"instanceId":"i-2******3"}</Dimensions>
         <RuleId>bfae2ca5b4e07d2c7278772eccda169808c7b****</RuleId>
         <Contacts></Contacts>
         <Namespace>acs_ecs</Namespace>
         <ContactALIIMs></ContactALIIMs>
         <ContactGroups></ContactGroups>
         <Expression>$Average&gt;=1</Expression>
         <Level>P3</Level>
         <InstanceName></InstanceName>
      </AlarmHistory>
      <AlarmHistory>
         <Value>2.13</Value>
         <LastTime>760058</LastTime>
         <Webhooks></Webhooks>
         <ContactSmses></ContactSmses>
         <RuleName>test-auto-scaling-0001</RuleName>
         <GroupId>123456</GroupId>
         <AlertName>putNewAlarm_us****</AlertName>
         <EvaluationCount>1</EvaluationCount>
         <Status>2</Status>
         <AlertState>ALARM</AlertState>
         <MetricName>cpu_total#60</MetricName>
         <ContactMails></ContactMails>
         <AlertTime>1554986620000</AlertTime>
         <Dimensions>{"instanceId":"i-2z*****"}</Dimensions>
         <RuleId>bfae2ca5b4e07d2c7278772eccda169808c7b****</RuleId>
         <Contacts></Contacts>
         <Namespace>acs_ecs</Namespace>
         <ContactALIIMs></ContactALIIMs>
         <ContactGroups></ContactGroups>
         <Expression>$Average&gt;=1</Expression>
         <Level>P3</Level>
         <InstanceName></InstanceName>
      </AlarmHistory>
   </AlarmHistoryList>
```

```xml
   <RequestId>FEBE3561-166F-******-020B26F30318</RequestId>
   <Success>true</Success>
   <Code>200</Code>
   <Total>102390</Total>
</DescribeAlertHistoryList>
```

JSON format

```xml
<DescribeAlertHistoryList>
   <AlarmHistoryList>
      <AlarmHistory>
         <Value>4.41</Value>
         <LastTime>881140083</LastTime>
         <Webhooks></Webhooks>
         <ContactSmses></ContactSmses>
         <RuleName>test-auto-scaling-0001</RuleName>
         <GroupId>123456</GroupId>
         <AlertName>putNewAlarm_xxxxxx</AlertName>
         <EvaluationCount>1</EvaluationCount>
         <Status>2</Status>
         <AlertState>ALARM</AlertState>
         <MetricName>cpu_total#60</MetricName>
         <ContactMails></ContactMails>
         <AlertTime>1554986620000</AlertTime>
         <Dimensions>{"instanceId":"i-2******3"}</Dimensions>
         <RuleId>bfae2ca5b4e07d2c7278772eccda169808c7b****</RuleId>
         <Contacts></Contacts>
         <Namespace>acs_ecs</Namespace>
         <ContactALIIMs></ContactALIIMs>
         <ContactGroups></ContactGroups>
         <Expression>$Average&gt;=1</Expression>
         <Level>P3</Level>
         <InstanceName></InstanceName>
      </AlarmHistory>
      <AlarmHistory>
         <Value>2.13</Value>
         <LastTime>760058</LastTime>
         <Webhooks></Webhooks>
         <ContactSmses></ContactSmses>
         <RuleName>test-auto-scaling-0001</RuleName>
         <GroupId>123456</GroupId>
         <AlertName>putNewAlarm_us****</AlertName>
         <EvaluationCount>1</EvaluationCount>
         <Status>2</Status>
         <AlertState>ALARM</AlertState>
         <MetricName>cpu_total#60</MetricName>
         <ContactMails></ContactMails>
         <AlertTime>1554986620000</AlertTime>
         <Dimensions>{"instanceId":"i-2z*****"}</Dimensions>
         <RuleId>bfae2ca5b4e07d2c7278772eccda169808c7b****</RuleId>
         <Contacts></Contacts>
         <Namespace>acs_ecs</Namespace>
         <ContactALIIMs></ContactALIIMs>
         <ContactGroups></ContactGroups>
```

```xml
         <Expression>$Average&gt;=1</Expression>
         <Level>P3</Level>
         <InstanceName></InstanceName>
      </AlarmHistory>
   </AlarmHistoryList>
   <RequestId>FEBE3561-166F-******-020B26F30318</RequestId>
   <Success>true</Success>
   <Code>200</Code>
   <Total>102390</Total>
</DescribeAlertHistoryList>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | InvalidAuthorization | InvalidAuthorization. | You do not have the required permissions. |
| 403 | InvalidAuthorization | Permission denied. | You do not have the required permissions. |
| 403 | NotAuthSLR | You are not authorized role AliyunServiceRoleFor CloudMonitor. | You do not grant the required permissions to the AliyunServiceRoleForCloudM onitor role. |
| 400 | ParameterInvalid | The parameter is missing or invalid. %s | The parameter is missing or invalid. |
| 404 | ResourceNotFound | The specified resource is not found. | The specified resource does not exist. |
| 429 | ResourceOverLimit | The resource has exceeded the limit. %s | The resource has reached or exceeded the upper limit. |

#### 1.4.2 DescribeMetricRuleList

Queries alert rules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeMetricR uleList | The operation that you want to perform. Set the value to DescribeMetricRuleList. |
|---|---|---|---|---|
| Namespace | String | No | acs ecs dashbo _ _ ard | The namespace of the cloud service. |
| MetricName | String | No | cpu total _ | The metric name. |
| EnableState | Boolean | No | true | Specifies whether to query enabled or disabled alert rules. Valid values: true: queries enabled alert rules. false: queries disabled alert rules. This parameter is empty by default, which indicates that both enabled and disabled alert rules are queried. |
| Page | String | No | 1 | The page number. Default value: 1. |
| PageSize | String | No | 10 | The number of entries per page. Default value: 10. |
| AlertState | String | No | ALARM | The status of the alert rule. Valid values: OK: No active alerts are triggered. ALARM: At least one alert is triggered. INSUFFICIENT DATA: No data is _ available. |

| Dimensions | String | No | {"instanceId":"i- xy123****"} | The dimensions that specify the resources whose monitoring data you want to query. Set the value to a collection of key-value pairs. A typical collection of key-value pairs is in the instanceId:XXXXXX format. The key and value can each be 1 to 64 bytes in length. Values that contain more than 64 characters are truncated. key and value contain letters, digits, periods (.), hyphens (-), underscores ( ), forward _ slashes (/), and backslashes (\). Note Dimensions must be formatted as a JSON string in a specific order. |
|---|---|---|---|---|
| RuleName | String | No | ECS CPU alert rule | The name of the alert rule. Note This parameter supports fuzzy match. |
| GroupId | String | No | 123456 | The ID of the application group. |
| RuleIds | String | No | a151cd6023eac ee2f0978e0386 3cc1697c89508 12**** | The ID of the alert rule. Note You can specify up to 20 IDs at a time. Separate multiple IDs with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0E657631-CD6C- 4C24-9637- 98D000B9272C | The request ID. |

| Code | Integer | 200 | The response code. Note The status code 200 indicates that the request was successful. |   |   |
|---|---|---|---|---|---|
| Total | String | 21 | The total number of entries returned. |   |   |
| Success | Boolean | true | Indicates whether the request was successful. |   |   |
| Alarms | Array | None | The alert rules. |   |   |
| Alarm | None | None | The alert rules. |   |   |
| AlertState | String | OK | The status of the alert rule. Valid values: OK: No active alerts are triggered. ALARM: At least one alert is triggered. INSUFFICIENT DATA: No data is _ available. |   |   |
| ContactGroups | String | Default alert contacts | The alert contacts that receive alert notifications. |   |   |
| Dimensions | String | {"userId":"4342" and "instanceId":"2123 12"} | The dimensions based on which the resources are queried. The value is set to a collection of key- value pairs. A typical collection of key-value pairs is in the instanceId:XXXXXX format. The key and value are 1 to 64 bytes in length. Values that contain more than 64 characters are truncated. key and value contain letters, digits, periods (.), hyphens (-), underscores ( ), _ forward slashes (/), and backslashes (\). Note Dimensions are formatted as a JSON string in a specific order. |   |   |
|   |   |   |   | key- |   |
| EffectiveInterv al | String | 00:00-23:59 | The period of time during which the alert rule is effective. |   |   |

|   | value |   |
|---|---|---|

| EnableState | Boolean | true | Indicates whether enabled or disabled alert rules are queried. Valid values: true: Enabled alert rules are queried. false: Disabled alert rules are queried. This parameter is empty by default, which indicates that both enabled and disabled alert rules are queried. |
|---|---|---|---|
| Escalations | None | None | The conditions for triggering different levels of alerts. |
| Critical | None | None | The conditions for triggering Critical-level alerts. |
| ComparisonOp erator | String | GreaterThanOrEqu alToThreshold | The operator that is used to compare the metric value with the threshold for Critical-level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to the threshold GreaterThanThreshold: greater than the threshold LessThanOrEqualToThreshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
| Statistics | String | Average | The statistical methods for Critical-level alerts. |
| Threshold | String | 90 | The threshold for Critical-level alerts. |

| Times | String | 3 | The consecutive number of times for which the metric value exceeds the threshold for Critical-level alerts before a Critical-level alert is triggered. |
|---|---|---|---|
| Info | None | None | The conditions for triggering Info-level alerts. |
| ComparisonOp erator | String | GreaterThanOrEqu alToThreshold | The operator that is used to compare the metric value with the threshold for Info- level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to the threshold GreaterThanThreshold: greater than the threshold LessThanOrEqualToThreshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
| Statistics | String | Average | The statistical methods for Info-level alerts. |
| Threshold | String | 90 | The threshold for Info-level alerts. |
| Times | String | 1 | The consecutive number of times for which the metric value exceeds the threshold for Info-level alerts before an Info-level alert is triggered. |
| Warn | None | None | The conditions for triggering Warn-level alerts. |

| ComparisonOp erator | String | GreaterThanOrEqu alToThreshold | The operator that is used to compare the metric value with the threshold for Warn- level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to the threshold GreaterThanThreshold: greater than the threshold LessThanOrEqualToThreshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
|---|---|---|---|
| Statistics | String | Average | The statistical methods for Warn-level alerts. |
| Threshold | String | 90 | The threshold for Warn-level alerts. |
| Times | String | 3 | The consecutive number of times for which the metric value exceeds the threshold for Warn-level alerts before a Warn-level alert is triggered. |
| GroupId | String | 123456 | The ID of the application group. |
| GroupName | String | My application group | The name of the application group. Note If the alert rule is associated with an application group, the name of the application group is returned. |
| MailSubject | String | An alert triggered | The subject of the alert notification email. |

| MetricName | String | cpu total _ | The metric name. |
|---|---|---|---|
| Namespace | String | acs ecs dashboard _ _ | The namespace of the service. |
| NoEffectiveInt erval | String | 00:00-23:59 | The period of time during which the alert rule is ineffective. |
| Period | String | 60 | The statistical period. |
| Resources | String | [{\"instanceId\":\"i- a2d5q7pm3f9yr29 e****\"}, {\"instanceId\":\"i- a2d5q7pm3f9yr29 e****\"} | The resources that are associated with the alert rule. |
| RuleId | String | a151cd6023eacee 2f0978e03863cc16 97c895012**** | The ID of the alert rule. |
| RuleName | String | My alert rule | The name of the alert rule. |
| SilenceTime | String | 86400 | The mute period during which new alert notifications are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400, which is equivalent to one day. Minimum value: 3600, which is equivalent to 1 hour. Only one alert notification is sent during each mute period even if the metric value continuously exceeds the threshold of the alert rule. |
| SourceType | String | METRIC | The type of the alert rule. Valid values: METRIC: the alert rule for time series metrics. EVENT: the alert rule for event-type metrics. This type is used in earlier versions and is deprecated. |
| Webhook | String | http://www.aliyun.c om | The callback URL. |
| Message | String | success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricRuleList &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Alarms>
    <Alarm>
        <Period>60</Period>
        <Statistics>Average</Statistics>
        <GroupName>Group name</GroupName>
        <Webhook/>
        <Subject>aaabbb</Subject>
        <EffectiveInterval>00:00-23:59</EffectiveInterval>
        <RuleName>My alert rule</RuleName>
        <NoEffectiveInterval/>
        <GroupId>3596360</GroupId>
        <EvaluationCount>3</EvaluationCount>
        <MetricName>cpu_total</MetricName>
        <Threshold>92</Threshold>
        <State>OK</State>
        <Enable>true</Enable>
        <SilenceTime>86400</SilenceTime>
        <Dimensions>[{}]</Dimensions>
        <RuleId>a151cd6023eacee2f0978e03863cc1697c89508e2b61****</RuleId>
        <Namespace>acs_ecs_dashboard</Namespace>
        <ContactGroups>Test</ContactGroups>
        <Escalations>
            <Critical>
                <Statistics>Average</Statistics>
                <Threshold>92</Threshold>
                <Times>3</Times>
                <ComparisonOperator>GreaterThanOrEqualToThreshold</ComparisonOperator>
            </Critical>
            <Info/>
            <Warn/>
        </Escalations>
        <ComparisonOperator>&gt;=</ComparisonOperator>
        <Resources>[{"instanceId":"i-a2d5q7pm3f12****"}]</Resources>
    </Alarm>
    <Alarm>
        <Period>60</Period>
        <Statistics>Average</Statistics>
        <GroupName>demo</GroupName>
        <Webhook/>
        <Subject>${serviceType}-${metricName}-
${levelDescription}Notification(${dimensions})</Subject>
        <EffectiveInterval>00:00-23:59</EffectiveInterval>
        <RuleName>xxxxxxxxxxxxxxx</RuleName>
```

```xml
        <NoEffectiveInterval/>
        <GroupId>12345</GroupId>
        <EvaluationCount>3</EvaluationCount>
        <MetricName>cpu_total</MetricName>
        <Threshold>90</Threshold>
        <State>OK</State>
        <Enable>true</Enable>
        <SilenceTime>86400</SilenceTime>
        <Dimensions>[{}]</Dimensions>
        <RuleId>alarmRule_uuid_adbe286748952b82c6a4ebe3a07521697bb706****</RuleId>
        <Namespace>acs_ecs_dashboard</Namespace>
        <ContactGroups>rongfei</ContactGroups>
        <Escalations>
            <Critical>
                <Statistics>Average</Statistics>
                <Threshold>6666</Threshold>
                <Times>3</Times>
                <ComparisonOperator>GreaterThanOrEqualToThreshold</ComparisonOperator>
            </Critical>
            <Info/>
            <Warn/>
        </Escalations>
        <ComparisonOperator>&gt;=</ComparisonOperator>
        <Resources>[{"instanceId":"host-fTcUci7****"}</Resources>
    </Alarm>
</Alarms> <RequestId>0F05309F-8863-4B2A-8F52-C6AA00E701B4</RequestId> <Success>true</Success> <Code>200</Code> <Total>102</Total>
```

`JSON` format `{`

```json
 "RequestId":"0F05309F-8863-4B2A-8F52-C6AA00E701B4",
 "Alarms":{
  "Alarm":[
```

`{`

```json
    "Period":60,
    "Statistics":"Average",
    "GroupName":"Group name",
    "Webhook":"",
    "Subject":"aaabbb",
    "EffectiveInterval":"00:00-23:59",
    "RuleName":"My alert rule",
    "NoEffectiveInterval":"",
    "GroupId":"3596360",
    "EvaluationCount":3,
    "MetricName":"cpu_total",
    "State":"OK",
    "Threshold":"92",
    "Enable":true,
    "SilenceTime":86400,
"Dimensions":"[{}]",
```

```json
    Dimensions:[{}],
    "RuleId":"a151cd6023eacee2f0978e03863cc1697c89508e2b61****",
    "Namespace":"acs_ecs_dashboard",
    "ContactGroups":"Test",
    "ComparisonOperator":">=",
    "Escalations":{
     "Critical":{
      "Statistics":"Average",
      "Threshold":"92",
      "Times":3,
      "ComparisonOperator":"GreaterThanOrEqualToThreshold"
```

`},`

```json
     "Info":{},
     "Warn":{}
```

`},`

```json
    "Resources":"[{\"instanceId\":\"i-a2d5q7pm3f12****\"}]"
```

`},` `{`

```json
    "Period":60,
    "Statistics":"Average",
    "GroupName":"demo",
    "Webhook":"",
    "Subject":"${serviceType}-${metricName}-
${levelDescription}Notification(${dimensions})",
    "EffectiveInterval":"00:00-23:59",
    "RuleName":"xxxxxxxxxxxxxxx",
    "NoEffectiveInterval":"",
    "GroupId":"12345",
    "EvaluationCount":3,
    "MetricName":"cpu_total",
    "State":"OK",
    "Threshold":"90",
    "Enable":true,
    "SilenceTime":86400,
    "Dimensions":"[{}]",
    "RuleId":"alarmRule_uuid_adbe286748952b82c6a4ebe3a07521697bb706****",
    "Namespace":"acs_ecs_dashboard",
    "ContactGroups":"rongfei",
    "ComparisonOperator":">=",
    "Escalations":{
     "Critical":{
      "Statistics":"Average",
      "Threshold":"6666",
      "Times":3,
      "ComparisonOperator":"GreaterThanOrEqualToThreshold"
```

`},`

```json
     "Info":{},
     "Warn":{}
```

`},`

```json
    "Resources":"[{\"instanceId\":\"host-fTcUci7****\"}"
```

`}` `]` `},`

```json
 "Success":true,
 "Code":"200",
```

```json
 "Total":102
```

`}`

#### 1.4.3 PutResourceMetricRule

Configures a threshold-triggered alert rule for a performance metric of a resource. For more information about example values of the cloud service parameters, such as `Namespace` , `MetricName` , and `Dimensions` , see Appendix 1: Metrics.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutResourceMet ricRule | The operation that you want to perform. Set the value to PutResourceMetricRule. |
| ContactGroups | String | Yes | Default alert contact group | The alert contact group. Note Separate multiple alert contact groups with commas (,). |
| MetricName | String | Yes | cpu total _ | The metric name. Note For more information, see Appendix 1: Metrics. |
| Namespace | String | Yes | acs ecs dashbo _ _ ard | The namespace of the cloud service. Note For more information, see Appendix 1: Metrics. |
| Resources | String | Yes | [{"instanceId":"x xxxxxx"}] | The resource for which an alert is triggered based on the alert rule. Note For more information, see Dimensions in Appendix 1: Metrics. |

| RuleId | String | Yes | a151cd6023eac ee2f0978e0386 3cc1697c89508 **** | The ID of the alert rule. Note The ID is generated by the caller. You can specify an existing ID to modify the corresponding alert rule or specify a new ID to create an alert rule. |
|---|---|---|---|---|
| RuleName | String | Yes | My alert rule | The name of the alert rule. |
| Webhook | String | No | http://ww.aliyun. com | The callback URL to which a POST request is sent when an alert is triggered based on the alert rule. |
| EffectiveInterv al | String | No | 00:00-23:59 | The time period during which the alert rule is effective. |
| NoEffectiveInt erval | String | No | 00:00-06:00 | The time period during which the alert rule is ineffective. |
| SilenceTime | Integer | No | 86400 | The mute period during which alerts are not reported even if the trigger conditions are met. Unit: seconds. Default value: 86400, which is equivalent to one day. Note Only one alert notification is sent during each mute period even if the metric value continuously exceeds the threshold of the alert rule. |
| Interval | String | No | 60 | The interval at which the system checks whether the alert rule is triggered. The default value is the lowest frequency at which the metric is polled. Unit: seconds. Note For more information about the frequency at which monitoring data is collected, see DescribeMetricMetaList. |

| EmailSubject | String | No |   | An alert triggered | The subject of the alert notification email. |   |   |
|---|---|---|---|---|---|---|---|
| Period | String | No |   | 60 | The aggregation cycle of monitoring data. The value is an integer multiple of 60. Unit: seconds. The default value is the frequency at which monitoring data is collected. |   |   |
| Escalations.Cri tical.Statistics | String | No |   | Average | The statistical methods for Critical- level alerts. |   |   |
| Escalations.Cri tical.Comparis onOperator | String | No |   |   | The operator that is used to compare the metric value with the threshold for Critical-level alerts. Valid values: GreaterThanOrEqualToThreshold : greater than or equal to the threshold GreaterThanThreshold : greater than the threshold LessThanOrEqualToThreshold : less than or equal to the threshold LessThanThreshold : less than the threshold NotEqualToThreshold : not equal to the threshold GreaterThanYesterday : greater than the metric value at the same time yesterday LessThanYesterday : less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek : less than the metric value at the same time last week GreaterThanLastPeriod : greater than the metric value in the last monitoring cycle LessThanLastPeriod : less than the metric value in the last monitoring cycle |   |   |
|   |   |   |   |   |   | GreaterThanOrEqualToThreshold |   |
|   |   |   |   | GreaterThanOrE qualToThreshold |   |   |   |
| Escalations.Cri tical.Threshold | String | No |   | 90 | The threshold for Critical-level alerts. |   |   |

| Escalations.Cri tical.Times | Integer | No |   | 3 | The consecutive number of times for which the metric value meets the alert condition before a Critical-level alert is triggered. |   |   |
|---|---|---|---|---|---|---|---|
| Escalations.Wa rn.Statistics | String | No |   | Average | The statistical methods for Warn- level alerts. |   |   |
| Escalations.Wa rn.Comparison Operator | String | No |   |   | The operator that is used to compare the metric value with the threshold for Warn-level alerts. Valid values: GreaterThanOrEqualToThreshold : greater than or equal to the threshold GreaterThanThreshold : greater than the threshold LessThanOrEqualToThreshold : less than or equal to the threshold LessThanThreshold : less than the threshold NotEqualToThreshold : not equal to the threshold GreaterThanYesterday : greater than the metric value at the same time yesterday LessThanYesterday : less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek : less than the metric value at the same time last week GreaterThanLastPeriod : greater than the metric value in the last monitoring cycle LessThanLastPeriod : less than the metric value in the last monitoring cycle |   |   |
|   |   |   |   |   |   | GreaterThanOrEqualToThreshold |   |
|   |   |   |   | GreaterThanOrE qualToThreshold |   |   |   |
| Escalations.Wa rn.Threshold | String | No |   | 90 | The threshold for Warn-level alerts. |   |   |

| Escalations.Wa rn.Times | Integer | No |   | 3 | The consecutive number of times for which the metric value meets the alert condition before a Warn-level alert is triggered. |   |   |
|---|---|---|---|---|---|---|---|
| Escalations.Inf o.Statistics | String | No |   | Average | The statistical methods for Info-level alerts. |   |   |
| Escalations.Inf o.Comparison Operator | String | No |   |   | The operator that is used to compare the metric value with the threshold for Info-level alerts. Valid values: GreaterThanOrEqualToThreshold : greater than or equal to the threshold GreaterThanThreshold : greater than the threshold LessThanOrEqualToThreshold : less than or equal to the threshold LessThanThreshold : less than the threshold NotEqualToThreshold : not equal to the threshold GreaterThanYesterday : greater than the metric value at the same time yesterday LessThanYesterday : less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek : less than the metric value at the same time last week GreaterThanLastPeriod : greater than the metric value in the last monitoring cycle LessThanLastPeriod : less than the metric value in the last monitoring cycle |   |   |
|   |   |   |   |   |   | GreaterThanOrEqualToThreshold |   |
|   |   |   |   | GreaterThanOrE qualToThreshold |   |   |   |
| Escalations.Inf o.Threshold | String | No |   | 90 | The threshold for Info-level alerts. |   |   |

| Escalations.Inf o.Times | Integer | No | 3 | The consecutive number of times for which the metric value meets the alert condition before an Info-level alert is triggered. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. Note The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |
| RequestId | String | 65D50468-ECEF- 48F1-A6E1- D952E89D9436 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutResourceMetricRule &ContactGroups=Default alert contact group &MetricName=cpu_total &Namespace=acs_ecs_dashboard &Resources=[{"instanceId":"xxxxxxx"}] &RuleId=a151cd6023eacee2f0978e03863cc1697c89508**** &RuleName=My alert rule &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Code>200</Code> <Message>success</Message> <RequestId>65D50468-ECEF-48F1-A6E1-D952E89D9436</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
 "Message":"success",
 "RequestId":"65D50468-ECEF-48F1-A6E1-D952E89D9436",
 "Success":true,
 "Code":"200"
```

`}`

#### 1.4.4 DescribeMetricRuleCount

Queries the number of alert rules in each state.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | No | DescribeMetricR uleCount | The operation that you want to perform. Set the value to DescribeMetricRuleCount. |
| MetricName | String | No | cpu total _ | The name of the metric for the query. |
| Namespace | String | No | acs ecs dashbo _ _ ard | The namespace of the service. You can call the DescribeMetricMetaList operation to query the namespaces of services. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The status code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The error message. |
| MetricRuleCou nt | None | None | The number of alert rules in each state. |
| Alarm | Integer | 5 | The number of alert rules based on which alerts are triggered. |
| Disable | Integer | 0 | The number of disabled alert rules. |
| Nodata | Integer | 0 | The number of alert rules for which status data is unavailable. |

| Ok | Integer | 40 | The number of alert rules for which active alerts are not triggered. |
|---|---|---|---|
| Total | Integer | 45 | The total number of alert rules. |
| RequestId | String | FF38D33A-67C1- 40EB-AB65- FAEE51EDB644 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricRuleCount &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeMetricRuleCountResponse>
      <Success>true</Success>
      <Code>200</Code>
      <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId>
      <MetricRuleCount>
            <Ok>40</Ok>
            <Disable>0</Disable>
            <Total>45</Total>
            <Nodata>0</Nodata>
            <Alarm>5</Alarm>
      </MetricRuleCount>
</DescribeMetricRuleCountResponse>
```

`JSON` format `{`

```json
 "RequestId":"FF38D33A-67C1-40EB-AB65-FAEE51EDB644",
 "Success":true,
 "Code":"200",
 "MetricRuleCount":{
  "Ok":40,
  "Disable":0,
  "Nodata":0,
  "Total":45,
  "Alarm":5
```

`}` `}`

#### 1.4.5 DeleteMetricRules

Deletes one or more alert rules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Id.N | RepeatL ist | Yes | ab05733c97b7c e239fb1b53393 dc1697c7e12*** * | The ID of the alert rule. |
| Action | String | No | DeleteMetricRul es | The operation that you want to perform. Set the value to DeleteMetricRules. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The status code. The value 200 indicates that the request is successful. |
| Message | String | success | The error message. |
| RequestId | String | E5599964-8D0D- 40DC-8E90- 27A619384B81 | The request ID, which can be used for troubleshooting. |
| Success | Boolean | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMetricRules &Id.1=ab05733c97b7ce239fb1b53393dc1697c7e12**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteMetricRulesResponse>
      <Code>200</Code>
      <Message>success</Message>
      <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId>
      <Success>true</Success>
</DeleteMetricRulesResponse>
```

`JSON` format `{`

```json
 "Message":"success",
 "RequestId":"E5599964-8D0D-40DC-8E90-27A619384B81",
 "Success":true,
 "Code":"200"
```

`}`

#### 1.4.6 DisableMetricRules

Disables one or more alert rules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DisableMetricRul es | The operation that you want to perform. Set the value to DisableMetricRules. |
| RuleId.N | RepeatL ist | Yes | ab05733c97b7c e239fb1b53393 dc1697c7e012** ** | The ID of the alert rule. Valid values of N: 1 to 20. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The status code. The value 200 indicates that the request is successful. |
| Message | String | success | The error message. |
| RequestId | String | FF38D33A-67C1- 40EB-AB65- FAEE51EDB644 | The request ID, which can be used for troubleshooting. |
| Success | Boolean | true | Indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DisableMetricRules &RuleId.1=ab05733c97b7ce239fb1b53393dc1697c7e012**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DisableMetricRulesResponse>
      <Code>200</Code>
      <Message>success</Message>
      <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId>
      <Success>true</Success>
</DisableMetricRulesResponse>
```

`JSON` format `{`

```json
 "Message":"success",
 "RequestId":"FF38D33A-67C1-40EB-AB65-FAEE51EDB644",
 "Success":true,
 "Code":"200"
```

`}`

#### 1.4.7 DescribeAlertingMetricRuleResources

Queries the resources that have active alerts triggered based on an alert rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlerting MetricRuleResou rces | The operation that you want to perform. Set the value to DescribeAlertingMetricRuleResources . |
| GroupId | String | No | 123456 | The ID of the application group. |
| Page | Integer | No | 1 | The page number. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries per page. Default value: 10. |

| RuleId | String | No | alerRuleId**** | The ID of the alert rule. Note You must configure at least one of the GroupId and RuleId parameters. If you configure both parameters, only entries that meet both conditions are returned. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B868619-77B4- 4623-AD64- 6181EA7CF8FA | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Code | Integer | 200 | The status code. Note The value 200 indicates that the request is successful. |
| Total | Integer | 1 | The total number of entries returned. |
| Resources | Array |   | The resources that are associated with the alert rule. |
| Resource |   |   | The information about a resource that is associated with the alert rule. |
| Enable | String | true | Indicates whether the alert rule is enabled. |
| GroupId | String | 123456 | The ID of the application group. Note If the alert rule is associated with an application group, the ID of the application group is returned in this parameter. |

| LastAlertTime | String | 1554718182000 | The time when an alert was last triggered for the resource based on the alert rule. This value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
|---|---|---|---|
| LastModifyTim e | String | 1554723762000 | The time when the resource was last modified. This value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| MetricValues | String | {"timestamp":155 4723720000,"Valu e":631} | The metric value that triggered the alert based on the alert rule. The value is a JSON string. |
| Resource | String | userId=177541323 192****,taskId=3** **,instanceId=i- bp1a0v6yzqrms01 k**** | The resource for which an alert was triggered based on the alert rule. |
| RetryTimes | String | 3 | The number of retries. |
| RuleId | String | alerRuleId**** | The ID of the alert rule. |
| RuleName | String | cpuAlert | The name of the alert rule. |
| StartTime | String | 1545901080000 | The time when the resource was associated with the alert rule. This value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| Threshold | String | 400 | The alert threshold. |
| Message | String | success | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlertingMetricRuleResources &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Total>1</Total> <Resources>
    <Resource>
        <Enable>true</Enable>
        <Resource>userId=12****,instanceId=i-bp1a012****</Resource>
        <RuleId>alerRuleId****</RuleId>
        <RetryTimes>3</RetryTimes>
        <LastAlertTime>1554718182000</LastAlertTime>
        <MetricValues>{"timestamp":1554723720000,"Value":631}</MetricValues>
        <LastModifyTime>1554723762000</LastModifyTime>
        <StartTime>1545901080000</StartTime>
        <RuleName>cpuAlert</RuleName>
        <Threshold>400</Threshold>
        <GroupId>123456</GroupId>
    </Resource>
</Resources> <Success>true</Success>
```

`JSON` format `{`

```json
 "Success":true,
 "Total":1,
 "Resources":{
  "Resource":[
```

`{`

```json
    "LastAlertTime":1554718182000,
    "Resource":"userId=12****,instanceId=i-bp1a012****",
    "Threshold":"400",
    "Enable":true,
    "LastModifyTime":1554723762000,
    "RuleId":"alerRuleId****",
    "MetricValues":"{\"timestamp\":1554723720000,\"Value\":631}",
    "RetryTimes":3,
    "StartTime":1545901080000,
    "RuleName":"cpuAlert",
    "GroupId":"123456"
```

`}` `]` `}` `}`

#### 1.4.8 DeleteMetricRuleResources

Disassociates resources from an alert rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteMetricRul eResources | The operation that you want to perform. Set the value to DeleteMetricRuleResources. |
| Resources | String | Yes | [{"instanceId":"* ****ixxxId1"}] | The resources that are associated with the alert rule. Set the value to a JSON array. |
| RuleId | String | No | rr- bp18017n6iolv* *** | The ID of the alert rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D8A35882-90C6- 4F03-BBEB- 153C180398EA | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Code | String | 200 | The status code. Note The value 200 indicates that the request is successful. |
| Message | String | success | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMetricRuleResources &Resources=[{"instanceId":"*****ixxxId1"}] &RuleId=rr-bp18017n6iolv**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>0671A721-0D7A-4F11-BB77-2416325D65AB</RequestId> <Success>true</Success> <Message>success</Message> <Code>200</Code>
```

`JSON` format `{`

```json
    "Message":"success",
    "RequestId":"0671A721-0D7A-4F11-BB77-2416325D65AB",
    "Success":true,
    "Code":"200"
```

`}`

#### 1.4.9 EnableMetricRules

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
| 500 |   | InternalError | The request processing has failed due to some unknown error. |

#### 1.4.10 DeleteContact

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

#### 1.4.11 DescribeMetricRuleTargets

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
| -Id | String | 1 | The ID of the resource for which alerts are triggered. |

|   |   |   |   |   |   |   | The Alibaba Cloud Resource Name (ARN) of the resource. Format: acs:{Service |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
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

#### 1.4.12 DescribeEventRuleList

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
|---|---|---|---|---|---|
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

#### 1.4.13 DescribeMetricRuleTemplateList

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

#### 1.4.14 DescribeContactList

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

#### 1.4.15 ApplyMetricRuleTemplate

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

#### 1.4.16 DescribeEventRuleTargetList

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
| 38 |   |   | > Document Version: 2025030 |

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
|   | > Document Versi |   | on: 20250304 |   | 13 |   |

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

| 40 |   |   | > Document Version: 2025030 |
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

#### 1.4.17 DescribeMetricRuleTemplateAttribute

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

#### 1.4.18 DescribeEventRuleAttribute

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

#### 1.4.19 DescribeContactListByContactGroup

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

#### 1.4.20 PutContact

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

#### 1.4.21 PutContactGroup

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

#### 1.4.22 PutGroupMetricRule

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
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The Request is not authorization. | The error message. |

| Developer Guide·A | PI Reference |   | CloudMonito |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
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
| 404 | 404 | ResourceNotFound | The specified resource is not found. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 409 | 4092 | ResourceExist | Resources already exist. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 1.4.23 CreateMetricRuleResources

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

#### 1.4.24 DescribeContactGroupList

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

#### 1.4.25 DeleteMetricRuleTemplate

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

#### 1.4.26 PutEventRuleTargets

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

| Developer Guide·A | PI Reference |   | CloudMonito |
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

#### 1.4.27 CreateMetricRuleTemplate

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

#### 1.4.28 CreateGroupMetricRules

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

| Developer Guide·A | PI Reference |   | CloudMonito |
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

#### 1.4.29 PutResourceMetricRules

Creates multiple alert rules for the specified metric of a specified resource.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|

| Rules | Repe atLis t | Quer y | Yes |   | The threshold-triggered alert rules. Valid values of N: 1 to 500. |
|---|---|---|---|---|---|
| -RuleId | Strin g | Quer y | Yes | a151cd6023eacee2f0978 e03863cc1697c89508*** * | The ID of the alert rule. Valid values of N: 1 to 500. You can specify a new ID or the ID of an existing alert rule. For more information about how to query IDs of alert rules, see DescribeMetricRuleList. If you specify a new ID, a threshold- triggered alert rule is created. |
| -RuleName | Strin g | Quer y | No | test123 | The name of the alert rule. Valid values of N: 1 to 500. You can specify a new name or the name of an existing alert rule. For more information about how to query the names of alert rules, see DescribeMetricRuleList. If you specify a new name, a threshold- triggered alert rule is created. |
| - Namespac e | Strin g | Quer y | Yes | acs ecs dashboard _ _ | The namespace of the cloud service. Valid values of N: 1 to 500. For more information about how to query the namespaces of cloud services, see Appendix 1: Metrics. |

| - MetricNam e | Strin g | Quer y |   | Yes | cpu total _ |   |   | The metric name. Valid values of N: 1 to 500. For more information about how to query metric names, see Appendix 1: Metrics. |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| -Resources | Strin g | Quer y |   |   |   |   |   | The resource information. Examples: [{"instanceId":"i- |   |   |   |
|   |   |   |   |   |   |   |   |   | [{"instanceId":"i- |   |   |
|   |   |   |   |   |   |   |   | uf6j91r34rnwawoo****"} |   |   |   |
|   |   |   |   |   |   |   |   | ] |   | and |   |
|   |   |   |   | Yes | [{"instanceId":"i- uf6j91r34rnwawoo****"}] |   |   |   |   |   |   |
|   |   |   |   |   |   | instanceId":"i- |   | 542****"}] |   |   |   |
| - ContactGr oups | Strin g | Quer y |   | Yes | ECS Group _ |   |   | The alert contact group. Alert notifications are sent to the alert contacts in the alert contact group. Valid values of N: 1 to 500. An alert contact group can contain one or more alert contacts. For more information about how to create alert contacts and alert contact groups, see PutContact and PutContactGroup. |   |   |   |
| -Webhook | Strin g | Quer y |   | No | https://alert.aliyun.com.c om:8080/callback |   |   | The callback URL to which a POST request is sent when an alert is triggered based on the alert rule. Valid values of N: 1 to 500. |   |   |   |

| - EffectiveIn terval | Strin g | Quer y | No | 00:00-23:59 | The time period during which the alert rule is effective. Valid values of N: 1 to 500. |
|---|---|---|---|---|---|
| - NoEffectiv eInterval | Strin g | Quer y | No | 00:00-06:00 | The time period during which the alert rule is ineffective. Valid values of N: 1 to 500. |
| - SilenceTim e | Integ er | Quer y | No | 86400 | The mute period during which new alert notifications are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400. Valid values of N: 1 to 500. If an alert is not cleared after the mute period ends, CloudMonitor resends an alert notification. |
| -Period | Strin g | Quer y | No | 60 | The statistical period of the metric. Unit: seconds. The default value is the interval at which the monitoring data of the metric is collected. Valid values of N: 1 to 500. For more information about how to query the statistical periods of metrics, see Appendix 1: Metrics. |

| -Interval | Strin g | Quer y | No | 60 | The interval at which alerts are triggered based on the alert rule. Unit: seconds. Valid values of N: 1 to 500. For more information about how to query the statistical periods of metrics, see Appendix 1: Metrics. |
|---|---|---|---|---|---|
| - EmailSubje ct | Strin g | Quer y | No | Alert for an ECS instance | The subject of the alert notification email. Valid values of N: 1 to 500. |
| - Escalation s.Critical.S tatistics | Strin g | Quer y | No | Average | The statistical methods for Critical-level alerts. Valid values of N: 1 to 500. The value of this parameter is determined by the Statistics column corresponding to the MetricName parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see Appendix 1: Metrics. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
|   |   |   |   |   | The operator that is used to compare the metric value with the threshold for Critical-level alerts. Valid values: |

| Developer Gui | de·API R | eference |   |   | CloudMonito |
|---|---|---|---|---|---|
| - Escalation s.Critical.C omparison Operator | Strin g | Quer y | No | GreaterThanOrEqualToTh reshold | GreaterThanOrEqualTo Threshold: greater than or equal to the threshold GreaterThanThreshold: greater than the threshold LessThanOrEqualToThr eshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle Valid values of N: 1 to 500. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |

| - Escalation s.Critical.T hreshold | Strin g | Quer y | No | 90 | The threshold for Critical- level alerts. Valid values of N: 1 to 500. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
|---|---|---|---|---|---|
| - Escalation s.Critical.Ti mes | Integ er | Quer y | No | 3 | The consecutive number of times for which the metric value meets the alert condition before a Critical-level alert is triggered. Valid values of N: 1 to 500. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |

| - Escalation s.Warn.Sta tistics | Strin g | Quer y | No | Average | The statistical methods for Warn-level alerts. Valid values of N: 1 to 500. The value of this parameter is determined by the Statistics column corresponding to the MetricName parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see Appendix 1: Metrics. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
|---|---|---|---|---|---|
|   |   |   |   |   | The operator that is used to compare the metric value with the threshold for Warn-level alerts. Valid values: GreaterThanOrEqualTo Threshold: greater than or equal to the threshold GreaterThanThreshold: greater than the threshold LessThanOrEqualToThr eshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterday: greater than the metric value at the same time yesterday |

| - Escalation s.Warn.Co mparisonO perator | Strin g | Quer y | No | GreaterThanOrEqualToTh reshold | LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric |
|---|---|---|---|---|---|
|   |   |   |   |   | value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle Valid values of N: 1 to 500. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
| - Escalation s.Warn.Thr eshold | Strin g | Quer y | No | 90 | The threshold for Warn- level alerts. Valid values of N: 1 to 500. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |

| - Escalation s.Warn.Ti mes | Integ er | Quer y | No | 3 | The consecutive number of times for which the metric value meets the alert condition before a Warn-level alert is triggered. Valid values of N: 1 to 500. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
|---|---|---|---|---|---|
| - Escalation s.Info.Stati stics | Strin g | Quer y | No | Average | The statistical methods for Info-level alerts. Valid values of N: 1 to 500. The value of this parameter is determined by the Statistics column corresponding to the MetricName parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see Appendix 1: Metrics. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
|   |   |   |   |   | The operator that is used to compare the metric value with the threshold for Info-level alerts. Valid values: |

| CloudMonitor |   |   |   | De | veloper Guide·API Referenc |
|---|---|---|---|---|---|
| - Escalation s.Info.Com parisonOp erator | Strin g | Quer y | No | GreaterThanOrEqualToTh reshold | GreaterThanOrEqualTo Threshold: greater than or equal to the threshold GreaterThanThreshold: greater than the threshold LessThanOrEqualToThr eshold: less than or equal to the threshold LessThanThreshold: less than the threshold NotEqualToThreshold: not equal to the threshold GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle Valid values of N: 1 to 500. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |

| - Escalation s.Info.Thre shold | Strin g | Quer y | No | 90 | The threshold for Info- level alerts. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |
|---|---|---|---|---|---|
| - Escalation s.Info.Time s | Integ er | Quer y | No | 3 | The consecutive number of times for which the metric value meets the alert condition before an Info-level alert is triggered. Valid values of N: 1 to 500. You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator , Threshold, and Times parameters for the selected alert level. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | The request processing has failed due to some unknown error. | The returned message. |
| RequestId | String | 15D1440E-BF24- 5A41-93E4- 36864635179E | The request ID. |

| FailedListResul t | Array |   | The alert rules that fail to be created for the resource. |
|---|---|---|---|
| -RuleId | String | a151cd6023eacee 2f0978e03863cc16 97c89508**** | The ID of the alert rule. |
| -Result | Struct |   | The alert rule that failed to be created. |
| --Code | String | 200 | The response code. |
| --Message | String | Success | The returned message. |
| --Success | Boolean | true | Indicates whether the request was successful. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutResourceMetricRules &Rules=null &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "Message":"The request processing has failed due to some unknown error.",
 "RequestId":"15D1440E-BF24-5A41-93E4-36864635179E",
 "FailedListResult":{
  "-Result":{
   "Message":"",
   "Code":"",
   "Success":""
```

`},`

```json
  "RuleId":"a151cd6023eacee2f0978e03863cc1697c89508****"
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

#### 1.4.30 DeleteEventRules

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

#### 1.4.31 ModifyMetricRuleTemplate

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
| 24 |   |   |   | > Do | cument Version: 2025030 |

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
| > Document V | ersion: 2 | 0250304 |   |   | 22 |

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

#### 1.4.32 PutMetricRuleTargets

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

### 1.5 Event monitoring

#### 1.5.1 DescribeSystemEventHistogram

Queries the number of times a system event occurred during each interval within a period of time.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| 34 |   |   |   | > D | ocument Version: 2025030 |
|---|---|---|---|---|---|

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

| -StartTime | Long | 1552225770000 | The start time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
|---|---|---|---|
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

#### 1.5.2 DescribeSystemEventAttribute

Queries the details of a system event.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Product | Strin g | Query | No | oss | The abbreviation of the Alibaba Cloud service name. For information about how to obtain the abbreviations of Alibaba Cloud service names, see DescribeSystemEve ntMetaList. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| EventType | Strin g | Query | No | Exception | The type of the system event. For information about how to obtain the types of system events, see DescribeSystemEve ntMetaList. |
| Name | Strin g | Query | No | BucketIngressBandwidth | The name of the system event. For information about how to obtain the names of system events, see DescribeSystemEve ntMetaList. |
| Level | Strin g | Query | No | CRITICAL | The level of the system event. Valid values: CRITICAL WARN INFO |
| Status | Strin g | Query | No | normal | The status of the system event. For information about how to obtain the status of system events, see DescribeSystemEve ntMetaList. |
| GroupId | Strin g | Query | No | 12346 | The ID of the application group. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| SearchKey words | Strin g | Query | No | cms | The keywords that are used to search for the system event. Valid values: If you want to search for the system event whose content contains a and b, set the value to a and b . If you want to search for the system event whose content contains a or b, set the value to a or b . |
| StartTime | Strin g | Query | No | 1552199984949 | The start time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| EndTime | Strin g | Query | No | 1552221584949 | The end time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| PageNum ber | Integ er | Query | No | 1 | The page number. Valid values: 1 to 100000000. Default value: 1. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. Valid values: 1 to 100. Default value: 10. |
| Reverse | Boole an | Query | No |   | To reverse. |

|   | b |
|---|---|

|   | b |
|---|---|

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
| -Status | String | normal | The status of the system event. |
| -ResourceId | String | xxxxx-1 | The resource ID. |
| -RegionId | String | cn-hangzhou | The region ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
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

#### 1.5.3 DescribeSystemEventCount

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

| loudMonitor |   |   | Developer Guide·API Referenc |
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

#### 1.5.4 SendDryRunSystemEvent

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

#### 1.5.5 PutCustomEvent

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

#### 1.5.6 DescribeSystemEventMetaList

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

#### 1.5.7 DescribeCustomEventCount

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

| Developer Guide·A | PI Reference |   | CloudMonito |
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

#### 1.5.8 DescribeCustomEventAttribute

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

### 1.6 Application group

#### 1.6.1 DescribeMonitorGroups

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
|---|---|---|---|
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

| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
|---|---|---|---|
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
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 1.6.2 DescribeMonitorGroupInstances

Queries the resources in an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | No | 10 | The number of entries per page. Default value: 10. |
| PageNum ber | Integ er | Query | No | 1 | The page number. Default value: 1. |
| GroupId | Long | Query | Yes | 12345 | The ID of the application group. |
|   |   |   |   |   | The abbreviation of the service name. Valid values: ecs: Elastic Compute Service (ECS) instances provided by Alibaba Cloud and hosts not provided by Alibaba Cloud rds: ApsaraDB RDS ads: AnalyticDB slb: Server Load Balancer (SLB) vpc: Virtual Private Cloud (VPC) apigateway: API Gateway cdn: Alibaba Cloud Content Delivery Network (CDN) cs: Container Service for Swarm dcdn: Dynamic Content Delivery Network (DCDN) ddos: Anti-DDoS eip: Elastic IP Address (EIP) elasticsearch emr: E-MapReduce ess: Auto Scaling hbase: ApsaraDB for HBase iot edge: Link IoT _ Edge k8s pod: pods in _ Container Service for Kubernetes (ACK) kvstore sharding: _ ApsaraDB for Redis (cluster architecture) |

| Parame Cteatregory | Typ Strin e g | Locati Qonuery | Require Ndo | Example ecs | kvstore splitrw: _ DeAspcsarirpaDtiBo fnor Redis (read/write splitting |
|---|---|---|---|---|---|
|   |   |   |   |   | architecture) kvstore standard: _ ApsaraDB for Redis (standard architecture) memcache: ApsaraDB for Memcache mns: Message Service (MNS) mongodb: ApsaraDB for MongoDB of the replica set architecture mongodb cluster: _ ApsaraDB for MongoDB of the cluster architecture mongodb sharding: _ ApsaraDB for MongoDB of the sharded cluster architecture mq topic: MNS topics _ ocs: ApsaraDB for Memcache of earlier versions opensearch: |
|   |   |   |   |   | OpenSearch oss: Object Storage Service (OSS) polardb: PolarDB petadata: HybridDB for MySQL scdn: Secure CDN (SCDN) sharebandwidthpacka ges: Internet Shared Bandwidth sls: Simple Log Service vpn: VPN Gateway Valid values of N: 1 to 200. |
| Keyword | Strin g | Query | No | s1 | The keyword used to search for instances. Fuzzy search based on instance names is supported. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
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
| Code | Integer | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | success | The returned message. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| Total | Integer | 12 | The total number of entries returned. |

| CloudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |

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

| Developer Gu | ide·API Reference |   | CloudMonito |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 1.6.3 CreateMonitorGroupInstances

Adds resources to an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| GroupId | Long | Quer y | Yes | 3607**** | The ID of the application group. |
| Instances | Repe atLis t | Quer y | Yes |   | The instances. |
| -Category | Strin g |   | Yes | ecs | The abbreviation of the cloud service name. For more information about how to query the abbreviations of cloud service names, see metricCategory in the response parameter Labels of the DescribeProjectMeta operation. |
| -InstanceId | Strin g |   | Yes | i-2ze26xj5wwy12**** | The instance ID. |

| -RegionId | Strin g |   | Yes | cn-hangzhou | The ID of the region where the instance resides. |
|---|---|---|---|---|---|
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
| 412 | 4121 | ResourcesOverLimit | Resources over limit. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 1.6.4 DescribeUnhealthyHostAvailability

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
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 1.6.5 DeleteMonitorGroupInstances

Removes instances from an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|

| GroupId | Long | Quer y | Yes | 123456 | The ID of the application group. |
|---|---|---|---|---|---|
| InstanceId List | Strin g | Quer y | Yes | i-a2d5q7pm3f912****,i- a2d5q7pm3f222**** | The instances to be removed from the application group. Separate multiple instances with commas (,). You can remove a maximum of 20 instances from an application group at a time. |
|   |   |   |   |   | The abbreviation of the service name. Valid values: ECS: Elastic Compute Service (ECS) instances provided by Alibaba Cloud and hosts not provided by Alibaba Cloud RDS: ApsaraDB RDS ADS: AnalyticDB SLB: Server Load Balancer (SLB) VPC: Virtual Private Cloud (VPC) APIGATEWAY: API Gateway CDN: Alibaba Cloud Content Delivery Network (CDN) CS: Container Service for Swarm DCDN: Dynamic Content Delivery Network (DCDN) DDoS: Anti-DDoS EIP: Elastic IP Address (EIP) ELASTICSEARCH: Elasticsearch EMR: E-MapReduce ESS: Auto Scaling HBASE: ApsaraDB for Hbase IOT EDGE: Link IoT _ Edge K8S POD: pods in _ Container Service for Kubernetes (ACK) |

| Category | Strin g | Quer y | Yes | ecs | KVSTORE SHARDING: _ ApsaraDB for Redis (cluster architecture) KVSTORE SPLITRW: _ ApsaraDB for Redis (read/write splitting architecture) KVSTORE STANDARD: _ ApsaraDB for Redis (standard architecture) MEMCACHE: ApsaraDB for Memcache MNS: Message Service (MNS) MONGODB: ApsaraDB for MongoDB of the replica set architecture MONGODB CLUSTER: _ ApsaraDB for MongoDB of the cluster architecture MONGODB SHARDING: _ ApsaraDB for MongoDB of the sharded cluster architecture MQ TOPIC: MNS topics _ OCS: ApsaraDB for Memcache of earlier versions OPENSEARCH: |
|---|---|---|---|---|---|
|   |   |   |   |   | OpenSearch OSS: Object Storage Service (OSS) POLARDB: PolarDB PETADATA: HybridDB for MySQL SCDN: Secure CDN (SCDN) SHAREBANDWIDTHPAC KAGES: Internet Shared Bandwidth SLS: Simple Log Service VPN: VPN Gateway |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | 5351B0F2-26A9- 4BC9-87FF- 1B74034D12C3 | The request ID. |
|---|---|---|---|
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

| Developer Gu | ide·API Reference |   | CloudMonito |
|---|---|---|---|

| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |
|---|---|---|---|

#### 1.6.6 DescribeMonitorGroupInstanceAttribute

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

| Category | Strin g | Quer y | No | ecs | The abbreviation of the cloud service name. For more information about how to query the abbreviations of cloud service names, see the metricCategory tag in the response parameter Labels of the DescribeProjectMeta operation. |
|---|---|---|---|---|---|
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
| -Desc | String | desc test _ | The resource description. |
| -NetworkType | String | vpc | The network type. |

| Developer Guide·A | PI Reference |   | CloudMonito |
|---|---|---|---|

| -Category | String | ecs | The name of the cloud service. |
|---|---|---|---|
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
| Message | String | The specified resource is not found. | The returned message. |

| PageNumber | Integer | 1 | The page number. |
|---|---|---|---|
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
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 1.6.7 DescribeHostAvailabilityList

Queries availability monitoring tasks.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|

| Id | Long | Quer y | No | 123456 | The ID of the availability monitoring task. |
|---|---|---|---|---|---|
| TaskName | Strin g | Quer y | No | ecs instance _ | The name of the availability monitoring task. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Pages start from page 1. Default value: 1. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Pages start from page 1. Default value: 10. |
| GroupId | Long | Quer y | No | 12345 | The ID of the application group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TaskList | Array |   | The tasks. |
| -Instances | Normal |   | The instances. |
| -Id | Long | 123456 | The ID of the availability monitoring task. |
| -TaskName | String | ecs instance _ | The name of the availability monitoring task. |
| -TaskType | String | HTTP | The task type. Valid values: PING TELNET HTTP |

| -TaskScope | String | GROUP | The range of instances that are monitored by the availability monitoring task. Valid values: GROUP: All Elastic Compute Service (ECS) instances in the application group are monitored. GROUP SPEC INSTANCE: Specified ECS _ _ instances in the application group are monitored. |
|---|---|---|---|
| -Disabled | Boolean | false | Indicates whether the availability monitoring task is disabled. Valid values: true: The availability monitoring task is disabled. false: The availability monitoring task is enabled. |
| -GroupId | Long | 12345 | The ID of the application group. |
| -GroupName | String | Group ECS _ | The name of the application group. |
| -TaskOption | Struct |   | The task option. |
| --HttpURI | String | https://www.aliyun. com | The URI that you want to monitor. This parameter is required if the TaskType parameter is set to HTTP. |
| -- TelnetOrPingH ost | String | ssh.aliyun.com | The domain name or IP address that you want to monitor. |
| -- HttpResponse Charset | String | UTF-8 | The character set that is used in the HTTP response. |
| --HttpKeyword | String | OK | The response to the HTTP request. |
| --HttpMethod | String | GET | The HTTP request method. Valid values: GET POST HEAD |

| --HttpNegative | Boolean | true | The method to trigger an alert. The alert can be triggered based on whether the specified alert rule is included in the response body. Valid values: true: If the HTTP response body includes the alert rule, an alert is triggered. false: If the HTTP response does not include the alert rule, an alert is triggered. |
|---|---|---|---|
| --Interval | Integer | 60 | The interval at which detection requests are sent. Unit: seconds. |
| --HttpHeader | String |   | The HTTP request header. |
| -- HttpPostConte nt | String | params1=paramsV alue1 | The content of the HTTP POST request. |
| -AlertConfig | Struct |   | The configurations of the alert rule. |
| -- EscalationList | Array |   | The trigger conditions of the alert rule. |
| ---MetricName | String | HttpStatus | The metric name. Valid values: HttpStatus: HTTP status code HttpLatency: HTTP response time TelnetStatus: Telnet status code TelnetLatency: Telnet response time PingLostRate: Ping packet loss rate |
| ---Aggregate | String | value | The method used to calculate the metric values that trigger alerts. Valid values: Value: the value of the HTTP status code Average: the average HTTP response time Value: the value of the Telnet status code TelnetLatency: the average Telnet response time Average: the average Ping packet loss rate |

| ---Operator | String | = | The comparison operator that is used in the alert rule. Valid values: = < <= = |
|---|---|---|---|
| ---Value | String | 400 | The alert threshold. |
| ---Times | String | 3 | The consecutive number of times for which the metric value is measured before an alert is triggered. |
| --NotifyType | Integer | 1 | The alert notification methods. Valid values: 2: Alert notifications are sent by using phone calls, text messages, emails, and DingTalk chatbots. 1: Alert notifications are sent by using text messages, emails, and DingTalk chatbots. 0: Alert notifications are sent by using emails and DingTalk chatbots. |
| --StartTime | Integer | 0 | The start time. |
| --EndTime | Integer | 22 | The end time. |
| --SilenceTime | Integer | 86400 | The mute period during which new alerts are not sent even if the trigger conditions are met. Unit: seconds. |
| --WebHook | String | https://www.aliyun. com | The callback URL. CloudMonitor pushes an alert notification to the specified callback URL by sending an HTTP POST request. Only the HTTP protocol is supported. |
| Code | String | 200 | The response code. The status code 200 indicates that the request was successful. |
| Message | String | The specified resource is not found. | The returned message. |

| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
|---|---|---|---|
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

#### 1.6.8 CreateMonitorGroup

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

| CloudMonitor |   |   | Developer Guide·API Referenc |
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

#### 1.6.9 DeleteMonitorGroup

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

| Developer Guide·A | PI Reference |   | CloudMonito |
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

#### 1.6.10 CreateHostAvailability

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

|   | CloudMonitor |   |   |   | Dev | eloper Guide·API Referenc | e |
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

| Developer Guide·A | PI Reference |   | CloudMonito |
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

#### 1.6.11 CreateMonitorGroupNotifyPolicy

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

#### 1.6.12 DeleteHostAvailability

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

#### 1.6.13 DescribeMonitorGroupCategories

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

#### 1.6.14 ModifyMonitorGroupInstances

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

#### 1.6.15 ModifyHostAvailability

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

|   | Developer Gui | de·API R | eference |   |   | CloudMonito | r |
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

| CloudMonitor |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 409 | 4092 | ResourceExist | Resources already exist. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 1.6.16 PutMonitorGroupDynamicRule

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

#### 1.6.17 ModifyMonitorGroup

Modifies an application group.

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupId | Strin g | Query | Yes | 123456 | The ID of the application group. |

| CloudMonitor |   |   |   | Dev | eloper Guide·API Referenc |
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

#### 1.6.18 DeleteMonitorGroupDynamicRule

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

| Developer Gu | ide·API Reference |   | CloudMonito |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 429 | 429 | ThrottlingException | The request was denied due to request throttling. |
| 406 | 406 | ExceedingQuota | Exceeding quota limits. |
| 409 | 4091 | ResourceConflict | Concurrent modification of resources. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error. |

#### 1.6.19 DeleteMonitorGroupNotifyPolicy

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

#### 1.6.20 DescribeMonitorGroupNotifyPolicyList

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

### 1.7 Site monitoring

#### 1.7.1 DescribeSiteMonitorData

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

#### 1.7.2 DescribeSiteMonitorStatistics

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

#### 1.7.3 DescribeSiteMonitorList

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

#### 1.7.4 DescribeSiteMonitorISPCityList

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

#### 1.7.5 CreateSiteMonitor

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

#### 1.7.6 DescribeSiteMonitorAttribute

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

#### 1.7.7 DisableSiteMonitors

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

#### 1.7.8 EnableSiteMonitors

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

#### 1.7.9 DeleteSiteMonitors

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

#### 1.7.10 ModifySiteMonitor

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

ra Stack services

## 2 Metrics for Apsara Stack services

**services**

The cloud services that are connected to CloudMonitor have different metrics. When you call CloudMonitor API operations to query the metrics of a cloud service, you must specify the metrics that are supported by the namespace of the cloud service, and specify the monitoring dimensions and intervals. The dimensions and intervals supported by each metric of a cloud service vary from each other.

**Usage notes**

You can call CloudMonitor API operations to query metric data within the last 31 days. The value of the **Dimensions** parameter is a JSON string in the format of `{"instanceId":"`

```
<Instance ID of an Apsara Stack service>"} .
```

When you call an API operation provided by CloudMonitor, you must specify the
**Namespace** and **Period** parameters.

### 2.1 Elastic computing

#### 2.1.1 ECS

This topic describes the metrics supported by Elastic Compute Service (ECS).

**Basic metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

> **Note:** The metrics described in the following table are collected from the virtual host layer and are slightly different from metrics collected in the operating system.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (ECS) CPU Utilization | % | CPUUtilization | userId and instanceId | The CPU utilization. |
| (ECS)InternetInRa te(Classic Network) | Bit/s | InternetInRate | userId and instanceId | The rate of inbound traffic over the Internet. |
| (ECS)IntranetInRa te | Bit/s | IntranetInRate | userId and instanceId | The rate of inbound traffic over the intranet. |

ra Stack services

| (ECS)InternetOut Rate(Classic Network) | Bit/s | InternetOutRate | userId and instanceId | The rate of outbound traffic over the Internet. |
|---|---|---|---|---|
| (ECS)IntranetOut Rate | Bit/s | IntranetOutRate | userId and instanceId | The rate of outbound traffic over the intranet. |
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

ra Stack services

| (Agent)cpu.total | % | cpu total _ | userId and instanceId | The CPU utilization. |
|---|---|---|---|---|
| (Agent)memory.u sed.utilization | % | memory usedutil _ ization | userId and instanceId | The memory usage. |
| (Agent)load.15m | N/A | load 15m _ | userId and instanceId | The system load in the last 15 minutes. Note This metric is not available for Windows. |
| (Agent)load.1m | N/A | load 1m _ | userId and instanceId | The system load in the last 1 minute. Note This metric is not available for Windows. |
| (Agent)load.5m | N/A | load 5m _ | userId and instanceId | The system load in the last 5 minutes. Note This metric is not available for Windows. |
| Host.diskusage.ut ilization | % | diskusage utiliza _ tion | userId, instanceId, and device | The disk usage. |

ra Stack services

| (Agent)fs.inode.u tilization device _ | % | fs inodeutilizatio _ n | userId, instanceId, and device | The inode usage. Note This metric is available only for Linux. |
|---|---|---|---|---|
| (Agent)disk.read. bps device _ | Bytes/s | disk readbytes _ | userId, instanceId, and device | The number of bytes read from the disk per second. |
| (Agent)disk.read.i ops device _ | Count/s | disk readiops _ | userId, instanceId, and device | The number of read IOPS of the disk. |
| (Agent)disk.write. bps device _ | Bytes/s | disk writebytes _ | userId, instanceId, and device | The number of bytes written to the disk per second. |
| (Agent)disk.write. iops device _ | Count/s | disk writeiops _ | userId, instanceId, and device | The number of write IOPS of the disk. |
| (Agent)network.t cp.connection st _ ate | Count | net tcpconnectio _ n | userId, instanceId, and state | The number of TCP connections in each state. |
| (Agent)process.e xpend pid _ | N/A | process.expend | userId, instanceId, name, and pid | The detailed statistical metrics for the top 5 processes. |
| (Agent)process.c ount processnam _ e | Count | process.number | userId, instanceId, and processName | The number of matched processes. |
| io saturation | % | disk io util _ _ | userId, instanceId, and device | The I/O saturation. |

ra Stack services

| Agent(zombie pr _ ocess number) _ | Count | zombieProcessNu mber | userId and instanceId | The total number of zombie processes. |
|---|---|---|---|---|
| Agent(total proce _ ss number) _ | Count | totalProcessNum ber | userId and instanceId | The total number of processes. |
| Agent(swap parti _ tion usage) _ | % | swapUtilization | userId and instanceId | The usage of the swap partition. |
| Agent(networkou t drop ratio) _ _ | % | networkout drop _ ratio _ | userId, instanceId, and device | The loss rate of packets that are sent by network interface controllers (NICs). |
| Agent(networkou t error ratio) _ _ | % | networkout error _ ratio _ | userId, instanceId, and device | The sending error rate of NICs. |
| Agent(networkin _ drop ratio) _ | % | networkin drop r _ _ atio | userId, instanceId, and device | The loss rate of packets that are received by NICs. |
| Agent(networkin _ error ratio) _ | % | networkin error r _ _ atio | userId, instanceId, and device | The receiving error rate of NICs. |

**GPU-related metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Agent)gpu.deco der.utilization gp _ uid | % | gpu decoder utili _ _ zation | userId, instanceId, and gpuId | The decoder usage of a GPU. |
| (Agent)gpu.enco der.utilization gp _ uid | % | gpu encoder utili _ _ zation | userId, instanceId, and gpuId | The encoder usage of a GPU. |
| (Agent)gpu.temp erature gpuid _ | °C | gpu gpu temper _ _ ature | userId, instanceId, and gpuId | The GPU temperature. |

ra Stack services

| (Agent)gpu.used utilization gpuid _ | % | gpu gpu usedutil _ _ ization | userId, instanceId, and gpuId | The GPU utilization. |
|---|---|---|---|---|
| (Agent)gpu.mem ory.free.space gp _ uid | Bytes | gpu memory fre _ _ espace | userId, instanceId, and gpuId | The idle video memory of a GPU. |
| (Agent)gpu.mem ory.free.utilizatio n gpuid _ | % | gpu memory fre _ _ eutilization | userId, instanceId, and gpuId | The percentage of the idle video memory of a GPU. |
| (Agent)gpu.mem ory.used.space g _ puid | Bytes | gpu memory use _ _ dspace | userId, instanceId, and gpuId | The used video memory of a GPU. |
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

ra Stack services

| Outgoing NIC bandwidth | Bit/s | networkout rate avs _ _ | userId and instanceId | The number of bits that the NIC sends per second. |
|---|---|---|---|---|
| Number of network card incoming packets | Count/s | networkin packages _ avs _ | userId and instanceId | The number of packets that the NIC receives per second. |
| Number of outgoing network card packets | Count/s | networkout package _ s avs _ | userId and instanceId | The number of packets that the NIC sends per second. |
| Number of packets with network card inbound error | Count/s | networkin errorpack _ ages avs _ | userId and instanceId | The number of error packets that the NIC receives per second. |
| Network card outbound error packets | Count/s | networkout errorpac _ kages avs _ | userId and instanceId | The number of error packets that the NIC sends per second. |
| Number of network connections | Count | net tcpconnection a _ _ vs | userId and instanceId | The number of connections. |
| Enter VPC- broadband | Bit/s | VPC PublicTP Intern _ _ etInRate | userId and instanceId | The number of bits that the virtual private cloud (VPC) receives per second. |
| Outbound VPC- broadband | Bit/s | VPC PublicTP Intern _ _ etOutRate | userId and instanceId | The number of bits that the VPC sends per second. |
| ipv6 packet bit | Bit | ipv6 tx bytes sum _ _ _ | userId and instanceId | The number of bits of an outbound IPv6 packet. |
| ipv6 packet receiving bits | Bit | ipv6 rx bytes sum _ _ _ | userId and instanceId | The number of bits of an inbound IPv6 packet. |

ra Stack services

| Number of ipv6 packages | Count | ipv6 tx packets su _ _ _ m | userId and instanceId | The number of outbound IPv6 packets. |
|---|---|---|---|---|
| Number of ipv6 packets received | Count | ipv6 rx packets su _ _ _ m | userId and instanceId | The number of inbound IPv6 packets. |
| Number of packets lost to ipv6 outbound security group | Count | ipv6 tx acl error su _ _ _ _ m | userId and instanceId | The number of outbound IPv6 packets dropped from the security group. |
| Number of packets lost to the security group in the direction of ipv6 | Count | ipv6 rx acl error su _ _ _ _ m | userId and instanceId | The number of inbound IPv6 packets dropped from the security group. |
| North-south traffic ipv6 statistics contract number | Count | ipv6 tx igw packets _ _ _ avg _ | userId and instanceId | The number of IPv6 packets that are sent in the north-south traffic. |
| North-south traffic ipv6 statistics number of packets received | Count | ipv6 rx igw packets _ _ _ avg _ | userId and instanceId | The number of IPv6 packets that are received in the north-south traffic. |
| North-South Traffic ipv6 Statistics Packet Bits | Bit/s | ipv6 tx igw bytes a _ _ _ _ vg | userId and instanceId | The number of bits of IPv6 packets that are sent per second in the north- south traffic. |
| North-South Traffic ipv6 Statistics Packet Receiving Bits | Bit/s | ipv6 rx igw bytes a _ _ _ _ vg | userId and instanceId | The number of bits of IPv6 packets that are received per second in the north-south traffic. |

#### 2.1.2 BMCP nodes

This topic describes the metrics for nodes in the Bare Metal Computing Power (BMCP) platform. ra Stack services Set the **Namespace** parameter to **acs_bms**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

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

ra Stack services

| GPU USAGE _ | % | GPU USAGE _ | instanceId | The GPU utilization. |
|---|---|---|---|---|
| GPU ENC USAG _ _ E | % | GPU ENC USAGE _ _ | instanceId | The encoder utilization of the GPU. |
| GPU DEC USAG _ _ E | % | GPU DEC USAGE _ _ | instanceId | The decoder utilization of the GPU. |
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

ra Stack services

| rdma service m _ _ onitor rnr nak r _ _ _ etry err _ | Count | rdma service mo _ _ nitor rnr nak retr _ _ _ y err _ | instanceId | The number of Receiver Not Ready (RNR) Negative Acknowledgment (NAK) packets sent from the peer. |
|---|---|---|---|---|

#### 2.1.3 BMCP containers

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

ra Stack services

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| GPU TEMP _ | °C | GPU TEMP _ | instanceId | The GPU temperature. |
| GPU POWER US _ _ AGE | W | GPU POWER USA _ _ GE | instanceId | The GPU power. |
| GPU USAGE _ | % | GPU USAGE _ | instanceId | The GPU utilization. |
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

ra Stack services

| rdma service m _ _ onitor rnr nak r _ _ _ etry err _ | Count | rdma service mo _ _ nitor rnr nak retr _ _ _ y err _ | instanceId | The number of Receiver Not Ready (RNR) Negative Acknowledgment (NAK) packets sent from the peer. |
|---|---|---|---|---|

### 2.2 Database services

#### 2.2.1 ApsaraDB RDS

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

ra Stack services

| NetworkOutRate | Bit/s | MySQL NetworkO _ utNew | userId and instanceId | The outbound traffic from the ApsaraDB RDS for MySQL instance per second. |
|---|---|---|---|---|
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

ra Stack services

**ApsaraDB RDS for PolarDB O**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
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

ra Stack services

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Average active connections per CPU PG cloud _ disk | Count | ActiveConnectio ns | userId and instanceId | The average number of active connections per CPU. |
| Inode Usage PG _ Disk | % | InodeUsage | userId and instanceId | The inode usage. |
| Read-only synchronization delay PG cloud _ disk | Seconds | ReadLag | userId and instanceId | The synchronization latency of the read-only instance. |
| Database Age PG Disk _ | xids | DBAge | userId and instanceId | The age of the database. |
| Read-only Stream replication state pg cloud _ disk | Value | StreamingStatus | userId and instanceId | The stream replication status of the read-only instance. Valid values: 0: disconnected. 1: normal. |
| Pg connection _ usage | % | conn usage _ | userId and instanceId | The connection utilization. |
| PG CPU usage _ | % | cpu usage _ | userId and instanceId | The CPU utilization. |
| PG IOPS usage _ | % | iops usage _ | userId and instanceId | The IOPS usage. |
| Pg disk space _ usage | % | local fs size usa _ _ _ ge | userId and instanceId | The disk usage. |
| PG Memory _ Usage | % | mem usage _ | userId and instanceId | The memory usage. |

ra Stack services

#### 2.2.2 ApsaraDB RDS (New)

This topic describes the metrics supported by ApsaraDB RDS (New). ApsaraDB RDS supports a new link. Data is collected at 60-second intervals. Set the **Namespace** parameter to **acs_rds_dashboard**. The default value of the **Period** parameter is **60**. Unit: seconds. ApsaraDB RDS (New) supports three types of engines: MySQL, PolarDB O, and PostgreSQL.

**ApsaraDB RDS for MySQL**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage new _ | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory usage (new) | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |
| MySQL Network inflow bandwidth (new) | Bit/s | MySQL NetworkI _ nNew new _ | userId and instanceId | The inbound traffic to the ApsaraDB RDS for MySQL instance per second. |
| MySQL Network outflow bandwidth (new) | Bit/s | MySQL NetworkO _ utNew new _ | userId and instanceId | The outbound traffic from the ApsaraDB RDS for MySQL instance per second. |
| MySQL queries per second (new) | Count/s | MySQL QPS new _ _ | userId and instanceId | The number of queries per second (QPS) for the ApsaraDB RDS for MySQL instance. |

ra Stack services

| DataDelay | Seconds | DataDelay | userId and instanceId | The latency between primary and secondary instances. |
|---|---|---|---|---|
| RWDelay (New) | Seconds | RWDelay | userId, instanceId, and slave | The read and write latency. |
| ThreadsConnecte d | Count | ThreadsConnecte d | userId and instanceId | The number of thread connections. |
| ThreadsRunning | Count | ThreadsRunning | userId and instanceId | The number of active threads. |
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

ra Stack services

| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
|---|---|---|---|---|
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory usage (new) | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |
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

ra Stack services

| Memory usage (new) | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |
|---|---|---|---|---|
| PG primary/standby disconnection | Count | PG ReplicationN _ um | userId and instanceId | The number of connections between primary and secondary ApsaraDB RDS for PostgreSQL instances. |
| PG primary/standby delay | Seconds | PG ReplicationLa _ g | userId and instanceId | The latency between primary and secondary ApsaraDB RDS for PostgreSQL instances. |

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

ra Stack services

| Read-only synchronization delay PG cloud _ disk (new) | Seconds | ReadLag new _ | userId and instanceId | The synchronization latency of the read-only instance. |
|---|---|---|---|---|
| Database age PG cloud _ disk (new) | xids | DBAge new _ | userId and instanceId | The age of the database. |
| Read-only Stream Copy Status PG Cloud _ Disk (New) | Value | StreamingStatus new _ | userId and instanceId | The streaming replication status of the read-only instance. |
| Number of Primary/Seconda ry Connections (Value 0 indicates disconnected. Value 1 indicates connected.) | Count | PG ESSD Replic _ _ ationNum | userId and instanceId | The number of connections between primary and secondary ApsaraDB RDS for PostgreSQL instances. |
| PG cloud disk primary/sta _ ndby delay | Seconds | PG ESSD Replic _ _ ationLag | userId and instanceId | The latency between primary and secondary ApsaraDB RDS for PostgreSQL instances. |

#### 2.2.3 PolarDB

This topic describes the metrics supported by PolarDB. Set the **Namespace** paramter to **acs_polardb_dashboard**. Set the **Period** paramter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**PolarDB for MySQL**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (PolarDB-M) Connection Usage | % | ConnectionUsa ge new _ | userId and instanceId | The connection utilization. |
| (PolarDB-M) CPU usage | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |

ra Stack services

| (PolarDB-M) Memory Usage | % | MemoryUsage _ new | userId and instanceId | The memory usage. |
|---|---|---|---|---|
| Number of active connections | Count | Active Session _ new _ | userId and instanceId | The number of active connections. |
| Storage Engine IO throughput per second | Count/s | Iops throughou _ t new _ | userId and instanceId | The I/O throughput of the storage engine per second. |
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

ra Stack services

| (PolarDB-O) Connections | Count | Connections O _ | userId and instanceId | The number of connections. |
|---|---|---|---|---|
| (PolarDB-O) Active Connections | Count | Active Connecti _ ons | userId and instanceId | The number of active connections. |
| (PolarDB-O)PFS reads IOPS | Count | Pfsd Read Iops _ _ | userId and instanceId | The read IOPS of the Polar file system (PFS). |
| (PolarDB-O)PFS writes IOPS | Count | Pfsd Write Iops _ _ | userId and instanceId | The write IOPS of the PFS. |
| (PolarDB-O) Database Age | Count | Db Age _ | userId and instanceId | The age of the database. |
| (PolarDB-O) Local Disk Usage | % | Local Disk Usa _ _ ge | userId and instanceId | The local disk usage. |

#### 2.2.4 PolarDB databases that use local SSDs

This topic describes the metrics supported by PolarDB databases that use local SSDs. Set the **Namespace** parameter to **acs_polardblocal**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**PolarDB for MySQL**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsag e new _ | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The IOPS usage. |
| Memory usage (new) | % | MemoryUsage _ new | userId and instanceId | The memory usage. |

ra Stack services

| MySQL Network inflow bandwidth (new) | Bit/s | MySQL Network _ InNew new _ | userId and instanceId | The inbound traffic to the PolarDB for MySQL instance per second. |
|---|---|---|---|---|
| MySQL Network outflow bandwidth (new) | Bit/s | MySQL Network _ OutNew new _ | userId and instanceId | The outbound traffic from the PolarDB for MySQL instance per second. |
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

ra Stack services

| Average number of active MySQL connections | Count/s | MySQL ActiveS _ ession | userId and instanceId | The average number of active connections to the PolarDB for MySQL instance. |
|---|---|---|---|---|
| Innodb row lock cur _ _ _ rent waits _ | Count | Innodb row loc _ _ k current waits _ _ | userId and instanceId | The number of sessions waiting for row locks. |
| mdl lock session _ _ | Count | mdl lock sessio _ _ n | userId and instanceId | The number of connections blocked by the MDL lock. |
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

ra Stack services

| PG ActiveConnectio _ nsPerCpu | Count | PG ActiveConn _ ectionsPerCpu | userId and instanceId | The average number of active connections per core to the PolarDB for Oracle Enterprise Edition database that uses local disks. |
|---|---|---|---|---|
| PG Database age _ | xids | PG DBAge _ | userId and instanceId | The age of the PolarDB for Oracle Enterprise Edition database that uses local SSDs. |
| PG SwellTime _ | Seconds | PG SwellTime _ | userId and instanceId | The period during which the PolarDB for Oracle Enterprise Edition database that uses local SSDs experiences storage bloat. |
| PG CheckpointLaten _ cyMB | MB | PG Checkpoint _ LatencyMB | userId and instanceId | The size of data written to the PolarDB for Oracle Enterprise Edition database that uses local SSDs with a delay during a checkpoint process. |
| PG InactiveSlots _ | Count | PG InactiveSlot _ s | userId and instanceId | The number of times that the replication slot is disconnected in the PolarDB for Oracle Enterprise Edition database that uses local SSDs. |
| PG ReplayLatencyIn _ MB | MB | PG ReplayLate _ ncyInMB | userId and instanceId | The size of data written to the PolarDB for Oracle Enterprise Edition database that uses local SSDs with a delay. |

#### 2.2.5 PolarDB-X 2.0

##### 2.2.5.1 Compute nodes of PolarDB-X 2.0

ra Stack services This topic describes the metrics for the compute nodes of PolarDB-X 2.0. Set the **Namespace** parameter to **acs_drds**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU usage | % | CPUUtilization | userId and instanceId | The CPU utilization. |
| Number of connections | Count | ConnectionCount | userId and instanceId | The total number of sessions. |
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

ra Stack services

| Number of errors per second | Count | SecondErrorCount | userId and instanceId | The number of errors per second. |
|---|---|---|---|---|
| Physical slow SQL per second | Count | SecondPhysicalSql Count | userId and instanceId | The number of physical slow SQL QPS. |
| Slow requests per second | Count | SecondRequestCo unt | userId and instanceId | The number of slow queries per second. |
| spill directory size | Bytes | SpillSize | userId and instanceId | The size of the spill directory. |
| Temporary directory size | Bytes | TmpSize | userId and instanceId | The size of the temporary directory. |

##### 2.2.5.2 Data nodes of PolarDB-X 2.0

This topic describes the metrics for the data nodes of PolarDB-X 2.0. Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of 60 in the range of 60 to 300. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage n _ ew | userId and instanceId | The connection utilization. |
| CPU Utilization (New) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk Usage (New) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS Usage (New) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory Utilization (New) | % | MemoryUsage new _ | userId and instanceId | The memory usage. |
| Inbound Bandwidth of an ApsaraDB RDS for MySQL Instance (New) | Bit/s | MySQL NetworkInN _ ew new _ | userId and instanceId | The inbound traffic to the MySQL data node per second. |

ra Stack services

| Outbound Bandwidth of an ApsaraDB RDS for MySQL Instance (New) | Bit/s | MySQL NetworkOut _ New new _ | userId and instanceId | The outbound traffic from the MySQL data node per second. |
|---|---|---|---|---|
| QPS of an ApsaraDB RDS for MySQL Instance (New) | Count/ s | MySQL QPS new _ _ | userId and instanceId | The number of queries per second (QPS) on the MySQL data node. |

#### 2.2.6 PolarDB-X 1.0

This topic describes the metrics supported by PolarDB-X 1.0. Set the **Namespace** parameter to **acs_polarx_drds**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU usage | % | CPUUtilization | useId and InstanceId | The CPU utilization. |
| Memory Usage | % | MemoryUtilizatio n | useId and InstanceId | The memory usage. |
| Network input | Bytes/s | NetworkInputTraf fic | useId and InstanceId | The inbound traffic. |
| Network output | Bytes/s | NetworkOutputTr affic | useId and InstanceId | The outbound traffic. |
| Average number of logical requests per second | Count | LogicQPS | useId and InstanceId | The average number of logical requests per second. |
| Average Logical Response Time | Millisec onds | LogicRT | useId and InstanceId | The average response time of logical requests. |
| Average number of physical requests per second | Count | PhysicsQPS | useId and InstanceId | The average number of physical requests per second. |

ra Stack services

| Average Physical Response Time | Millisec onds | PhysicsRT | useId and InstanceId | The average response time of physical requests. |
|---|---|---|---|---|
| Number of connections | Count | ConnectionCount | useId and InstanceId | The total number of sessions. |
| Number of active sessions | Count | ThreadCount | useId and InstanceId | The number of active sessions. |

#### 2.2.7 ApsaraDB for MongoDB (Old)

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

| Developer Guide·Met a Stack services | rics for Apsa |   |   | CloudMonito |
|---|---|---|---|---|

**Disk capacity-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| InstanceUsedDisk Space | Bytes | InstanceDiskAmo unt | userId, instanceId, and role | The disk space occupied by the instance. |
| LogUsedDiskSpac e | Bytes | DataDiskAmount | userId, instanceId, and role | The disk space occupied by data. |
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

ra Stack services

| OpCounters for Delete | Count | OpDelete | userId, instanceId, and role | The number of Delete operations. |
|---|---|---|---|---|
| OpCounters for Getmore | Count | OpGetmore | userId, instanceId, and role | The number of Getmore operations. |
| OpCounters for Insert | Count | OpInsert | userId, instanceId, and role | The number of Insert operations. |
| OpCounters for Query | Count | OpQuery | userId, instanceId, and role | The number of Query operations. |
| OpCounters for Update | Count | OpUpdate | userId, instanceId, and role | The number of Update operations. |

#### 2.2.8 ApsaraDB for MongoDB (New)

This topic describes the metrics supported by ApsaraDB for MongoDB (New). Set the **Namespace** parameter to **acs_mongodb**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPUUtilization ne _ w | % | CPUUtilization ne _ w | userId, instanceId, and role | The CPU utilization. |
| MemoryUtilizatio n new _ | % | MemoryUtilizatio n new _ | userId, instanceId, and role | The memory usage. |
| Disk Usage (New) | % | DiskUtilization n _ ew | userId, instanceId, and role | The disk usage. |
| IOPSUtilization n _ ew | % | IOPSUtilization n _ ew | userId, instanceId, and role | The IOPS usage. |

ra Stack services

| ConnectionUtiliza tion new _ | % | ConnectionUtiliza tion new _ | userId, instanceId, and role | The connection utilization. |
|---|---|---|---|---|
| Visits per second (new) | Count | QPS new _ | userId, instanceId, and role | The number of queries per second (QPS). |
| Connection Usage (New) | Count | ConnectionAmou nt new _ | userId, instanceId, and role | The number of used connections. |
| Current Total Connections (New) | Count | TotalConnections | userId, instanceId, and role | The total number of current connections. |

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

ra Stack services

| Intranet outbound traffic (new) | Bytes | IntranetOut new _ | userId, instanceId, and role | The outbound traffic over the intranet. |
|---|---|---|---|---|
| Number of requests (new) | Count | NumberRequests new _ | userId, instanceId, and role | The number of requests. |

**Operation count-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Command Operations (new) | Count | OpCommand ne _ w | userId, instanceId, and role | The number of Command operations. |
| Number of Delete operations (new) | Count | OpDelete new _ | userId, instanceId, and role | The number of Delete operations. |
| Number of Getmore operations (new) | Count | OpGetmore new _ | userId, instanceId, and role | The number of Getmore operations. |
| Number of Insert operations (new) | Count | OpInsert new _ | userId, instanceId, and role | The number of Insert operations. |
| Number of Query operations (new) | Count | OpQuery new _ | userId, instanceId, and role | The number of Query operations. |
| Number of Update operations (new) | Count | OpUpdate new _ | userId, instanceId, and role | The number of Update operations. |

**Basic metrics (Cluster Edition)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Cluster) CPU usage | % | CPUUtilization new _ cluster _ | userId, instanceId, and role | The CPU utilization. |

ra Stack services

| (Cluster Version) Memory Usage | % | MemoryUtilization _ new cluster _ | userId, instanceId, and role | The memory usage. |
|---|---|---|---|---|
| (Cluster Edition) Disk Usage | % | DiskUtilization ne _ w cluster _ | userId, instanceId, and role | The disk usage. |
| (Cluster version) IOPS usage | % | IOPSUtilization ne _ w cluster _ | userId, instanceId, and role | The IOPS usage. |
| (Cluster Edition) Connection Usage | % | ConnectionUtilizati on new cluster _ _ | userId, instanceId, and role | The connection utilization. |
| (Cluster Version) Visits Per Second | Count | QPS new cluster _ _ | userId, instanceId, and role | The QPS. |
| (Cluster Edition) Connection Usage | Count | ConnectionAmount new cluster _ _ | userId, instanceId, and role | The number of used connections. |
| (Cluster Edition) Total Number of Connections | Count | TotalConnections _ cluster | userId, instanceId, and role | The total number of current connections. |

**Disk capacity-related metrics (Cluster Edition)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Cluster Edition) The amount of disk space occupied by the instance | Bytes | InstanceDiskAmoun t new cluster _ _ | userId, instanceId, and role | The disk space occupied by the instance. |
| (Cluster Edition) The amount of disk space occupied by data | Bytes | DataDiskAmount n _ ew cluster _ | userId, instanceId, and role | The disk space occupied by data. |
| (Cluster Edition) The amount of disk space occupied by logs | Bytes | LogDiskAmount ne _ w cluster _ | userId, instanceId, and role | The disk space occupied by logs. |

**Network request-related metrics (Cluster Edition)**

ra Stack services

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

#### 2.2.9 Tair (Redis OSS-compatible) (Old)

This topic describes the metrics supported by Tair (Redis OSS-compatible) (Old). Set the **Namespace** parameter to **acs_kvstore**. Set the **Period** parameter to an integer ra Stack services multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | Metric | Dimensions | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| Failed Operations | Count | FailedCount | userId and instanceId | The number of failed operations. |
| Cache Inbound Bandwidth | Bytes/s | IntranetIn | userId and instanceId | The inbound traffic over the intranet. |
| Inbound Bandwidth Usage | % | IntranetInRatio | userId and instanceId | The inbound bandwidth usage. |
| Cache Outbound Bandwidth | Bytes/s | IntranetOut | userId and instanceId | The outbound traffic over the intranet. |
| Outbound Bandwidth Usage | % | IntranetOutRatio | userId and instanceId | The outbound bandwidth usage. |
| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage. |
| Used QPS | Count/s | UsedQPS | userId and instanceId | The number of used QPS. |

#### 2.2.10 Tair (Redis OSS-compatible) (New)

This topic describes the metrics supported by Tair (Redis OSS-compatible) (New). Set the **Namespace** parameter to **acs_kvstore**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Standard Edition instances and Read/write splitting instances**

**of Tair (Redis OSS-compatible)**

ra Stack services

> **Note:** Tair (Redis OSS-compatible) Standard Edition instances and Tair (Redis OSS-compatible) Read/write splitting instances share a set of metrics.

| Console- based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Connections Usage (Standard Edition) | % | StandardConnectionU sage | userId and instanceId | The connection utilization. |
| Incoming Bandwidth (Standard Edition) | Kbit/s | StandardIntranetIn | userId and instanceId | The inbound bandwidth. |
| Incoming Bandwidth Utilization (Standard Edition) | % | StandardIntranetInRat io | userId and instanceId | The inbound bandwidth utilization. |
| Outgoing Bandwidth (Standard Edition) | Kbit/s | StandardIntranetOut | userId and instanceId | The outbound bandwidth. |
| Outgoing Bandwidth Usage (Standard Edition) | % | StandardIntranetOutR atio | userId and instanceId | The outbound bandwidth utilization. |
| Memory Usage (Standard Edition) | % | StandardMemoryUsag e | userId and instanceId | The memory usage. |
| QPS usage (standard version) | % | StandardQPSUsage | userId and instanceId | The queries per second (QPS) usage. |
| CPU usage (standard edition) | % | StandardCpuUsage | userId and instanceId | The CPU utilization. |

ra Stack services

| Average Visits Per Second (Standard Edition) | Count/s | StandardUsedQPS | userId and instanceId | The average QPS. |
|---|---|---|---|---|
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

ra Stack services

| QPS usage (cluster version) | % | ShardingQPSUsa ge | userId and instanceId | The QPS utilization. |
|---|---|---|---|---|
| CPU usage (Cluster Edition) | % | ShardingCpuUsa ge | userId and instanceId | The CPU utilization. |
| Average visits per second (cluster version) | Count/s | ShardingUsedQP S | userId and instanceId | The average QPS. |
| Total QPS (cluster version) | Count/s | ShardingTotalQp s | userId and instanceId | The total QPS. |
| Total Current Connections (Cluster Edition) | Count | ShardingTotalCo nnections | userId and instanceId | The total number of current connections. |

**Cluster Edition - Node**

| Console- based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Connections Usage (Node) | % | NodeConnection Usage | userId, instanceId, and nodeId | The connection utilization. |
| Incoming Bandwidth (Node) | Kbit/s | NodeIntranetIn | userId, instanceId, and nodeId | The inbound bandwidth. |
| Outgoing Bandwidth (Node) | Kbit/s | NodeIntranetOut | userId, instanceId, and nodeId | The outbound bandwidth. |
| Incoming Bandwidth Utilization (Node) | % | NodeIntranetInR atio | userId, instanceId, and nodeId | The inbound bandwidth usage. |
| Outgoing Bandwidth Utilization (Node) | % | NodeIntranetOut Ratio | userId, instanceId, and nodeId | The outbound bandwidth usage. |

ra Stack services

| Memory Usage (Node) | % | NodeMemoryUs age | userId, instanceId, and nodeId | The memory usage. |
|---|---|---|---|---|
| QPS usage (node) | % | NodeQPSUsage | userId, instanceId, and nodeId | The QPS usage. |
| CPU usage (node) | % | NodeCpuUsage | userId, instanceId, and nodeId | The CPU utilization. |
| Average Visits Per Second (Node) | Count | NodeUsedQPS | userId, instanceId, and nodeId | The average QPS. |
| Total QPS (nodes) | Count/S | NodeTotalQps | userId, instanceId, and nodeId | The total QPS. |
| Total Current Connections (Nodes) | Count | NodeTotalConne ctions | userId, instanceId, and nodeId | The total number of current connections. |

#### 2.2.11 DTS

This topic describes the metrics supported by Data Transmission Service (DTS). Set the **Namespace** parameter to **acs_dts_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console- based metric | unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ChangeTrackin gLatency | Seconds | ChangeTrackingLatenc y | userId and instanceId | The latency of the change tracking task. |
| Synchronizatio nLatency | Seconds | SynchronizationLatenc y | userId and instanceId | The latency of the data synchronization task. |
| MigrationLaten cy | Seconds | MigrationLatency | userId and instanceId | The latency of the data migration task. |

### 2.3 Storage and CDN

#### 2.3.1 NAS

ra Stack services This topic describes the metrics supported by File Storage NAS (NAS). Set the **Namespace** parameter to **acs_nas**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

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
| Metadata QPS | Requests/s | QpsMeta | userId and fileSystemId | The average QPS of metadata per minute. |
| Metadata delay | Milliseconds | LatencyMeta | userId and fileSystemId | The average latency of metadata. |

ra Stack services

| Read Throughput | Bytes/s | ThruputRead | userId and fileSystemId | The average read throughput per minute. |
|---|---|---|---|---|
| Write Throughput | Bytes/s | ThruputWrite | userId and fileSystemId | The average write throughput per minute. |
| Maximum usable capacity | Bytes | Quota | userId and fileSystemId | The maximum available capacity. |
| Maximum number of files | Count | MaxFileCount | userId and fileSystemId | The maximum number of files. |
| ErrorRateRead | % | ErrorRateRead | userId and fileSystemId | The percentage of read operations in which errors occur. |
| ErrorRateWrite | % | ErrorRateWrite | userId and fileSystemId | The percentage of write operations in which errors occur. |
| ErrorRateMeta | % | ErrorRateMeta | userId and fileSystemId | The percentage of metadata- related operations in which errors occur. |

#### 2.3.2 OSS

This topic describes the metrics supported by Object Storage Service (OSS) Set the **Namespace** parameter to **acs_oss_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| RequestValidRate | % | RequestValidRat e | userId and BucketName | The rate of valid requests. |

ra Stack services

| The number of valid requests. | Count | ValidRequestCou nt | userId and BucketName | The number of valid requests. |
|---|---|---|---|---|
| TotalRequestCou nt | Count | TotalRequestCou nt | userId and BucketName | The total number of requests. |
| Availability | % | Availability | userId and BucketName | The availability. Stay alert if this metric is lower than 100%. |
| InternetSend | Bytes | InternetSend | userId and BucketName | The outbound traffic over the Internet. |
| InternetRecv | Bytes | InternetRecv | userId and BucketName | The inbound traffic over the Internet. |
| IntranetSend | Bytes | IntranetSend | userId and BucketName | The outbound traffic over the intranet. |
| IntranetRecv | Bytes | IntranetRecv | userId and BucketName | The inbound traffic over the intranet. |
| CDNSend | Bytes | CdnSend | userId and BucketName | The CDN outbound traffic. |
| CDNRecv | Bytes | CdnRecv | userId and BucketName | The CDN inbound traffic. |
| SyncSend | Bytes | SyncSend | userId and BucketName | The outbound traffic that is generated when you use the cross-region replication feature. |
| SyncRecv | Bytes | SyncRecv | userId and BucketName | The inbound traffic that is generated when you use the cross-region replication feature. |

ra Stack services

| MeteringStorage Utilization | Bytes | MeteringStorage Utilization | userId and BucketName | The size of the storage in use. |
|---|---|---|---|---|
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
| ClientTimeoutErr orCount | Count | ClientTimeoutErr orCount | userId and BucketName | The number of requests with a client timeout error. |
| ClientOtherErrorC ount | Count | ClientOtherError Count | userId and BucketName | The number of requests with other client errors. |

ra Stack services

| AuthorizationErro rRate | % | AuthorizationErro rRate | userId and BucketName | The ratio of requests with an authorization error. |
|---|---|---|---|---|
| ResourceNotFoun dErrorRate | % | ResourceNotFoun dErrorRate | userId and BucketName | The ratio of requests with an error indicating that resources cannot be found. |
| Client Timeout Error Request Proportion | % | ClientTimeoutErr orRate | userId and BucketName | The ratio of requests with a client timeout error. |
| ClientOtherErrorR ate | % | ClientOtherError Rate | userId and BucketName | The ratio of requests with other client errors. |
| SuccessCount | Count | SuccessCount | userId and BucketName | The number of successful requests. |
| RedirectCount | Count | RedirectCount | userId and BucketName | The number of redirected requests. |
| SuccessRate | % | SuccessRate | userId and BucketName | The ratio of successful requests. |
| RedirectRate | % | RedirectRate | userId and BucketName | The ratio of redirected requests. |

**Maximum latency-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| MaxGetObjectE2 eLatency | Milliseconds | MaxGetObjectE2 eLatency | userId and BucketName | The maximum end-to-end (E2E) latency of GetObject requests. |

ra Stack services

| MaxGetObjectSer verLatency | Milliseconds | MaxGetObjectSer verLatency | userId and BucketName | The maximum server latency of GetObject requests. |
|---|---|---|---|---|
| MaxHeadObjectE 2eLatency | Milliseconds | MaxHeadObjectE 2eLatency | userId and BucketName | The maximum E2E latency of HeadObject requests. |
| MaxHeadObjectS erverLatency | Milliseconds | MaxHeadObjectS erverLatency | userId and BucketName | The maximum server latency of HeadObject requests. |
| MaxPutObjectE2e Latency | Milliseconds | MaxPutObjectE2e Latency | userId and BucketName | The maximum E2E latency of PutObject requests. |
| MaxPutObjectSer verLatency | Milliseconds | MaxPutObjectSer verLatency | userId and BucketName | The maximum server latency of PutObject requests. |
| MaxAppendObjec tE2eLatency | Milliseconds | MaxAppendObjec tE2eLatency | userId and BucketName | The maximum E2E latency of AppendObject requests. |
| MaxAppendObjec tServerLatency | Milliseconds | MaxAppendObjec tServerLatency | userId and BucketName | The maximum server latency of AppendObject requests. |
| MaxUploadPartE2 eLatency | Milliseconds | MaxUploadPartE2 eLatency | userId and BucketName | The maximum E2E latency of UploadPart requests. |
| MaxUploadPartSe rverLatency | Milliseconds | MaxUploadPartSe rverLatency | userId and BucketName | The maximum server latency of UploadPart requests. |
| MaxUploadPartCo pyE2eLatency | Milliseconds | MaxUploadPartC opyE2eLatency | userId and BucketName | The maximum E2E latency of UploadPartCopy requests. |

ra Stack services

| MaxUploadPartCo pyServerLatency | Milliseconds | MaxUploadPartC opyServerLatenc y | userId and BucketName | The maximum server latency of UploadPartCopy requests. |
|---|---|---|---|---|

**Metrics related to successful requests**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| GetObjectCount | Count | GetObjectCount | userId and BucketName | The number of successful GetObject requests. |
| HeadObjectCount | Count | HeadObjectCount | userId and BucketName | The number of successful HeadObject requests. |
| PostObjectCount | Count | PostObjectCount | userId and BucketName | The number of successful PostObject requests. |
| AppendObjectCo unt | Count | AppendObjectCo unt | userId and BucketName | The number of successful AppendObject requests. |
| UploadPartCount | Count | UploadPartCount | userId and BucketName | The number of successful UploadPart requests. |
| UploadPartCopyC ount | Count | UploadPartCopyC ount | userId and BucketName | The number of successful UploadPartCopy requests. |
| DeleteObjectCou nt | Count | DeleteObjectCou nt | userId and BucketName | The number of successful DeleteObject requests. |
| DeleteObjectsCo unt | Count | DeleteObjectsCo unt | userId and BucketName | The number of successful DeleteObjects requests. |

ra Stack services

#### 2.3.3 Tablestore

This topic describes the metrics supported by Tablestore. Set the **Namespace** parameter to **acs_ots_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Instance VCU | Count/s | InstanceVCU | userId and instanceName | The virtual compute units (VCUs) of the instance. |
| Reserved VCU | Count/s | InstanceReserve dVCU | userId and instanceName | The reserved VCUs of the instance. |
| Internal Read CU | Count/s | InstanceFreeRea dCU NoOp _ | userId and instanceName | The internal read capacity units (CUs). |
| Internal Write CU | Count/s | InstanceFreeWrit eCU NoOp _ | userId and instanceName | The internal write CUs. |
| Over ReadCU | Count/s | InstanceOverRea dCU NoOp _ | userId and instanceName | The excess read CUs of the instance. |
| Over WriteCU | Count/s | InstanceOverWrit eCU NoOp _ | userId and instanceName | The excess write CUs of the instance. |
| Read CU | Count/s | InstanceReadCU _ NoOp | userId and instanceName | The operation read CUs. |
| Write CU | Count/s | InstanceWriteCU _ NoOp | userId and instanceName | The operation write CUs. |
| Total Request | Count/s | InstanceRequest Number NoOp _ | userId and instanceName | The total number of requests. |
| 2xx Request | Count/s | InstanceCount2x xNumber NoOp _ | userId and instanceName | The number of requests that return a 2XX HTTP status code. |

ra Stack services

| 429 Request | Count/s | InstanceCount42 9Number NoOp _ | userId and instanceName | The number of requests that return the HTTP status code 429. |
|---|---|---|---|---|
| 4xx Request | Count/s | InstanceCount4x xNumber NoOp _ | userId and instanceName | The number of requests that return a 4XX HTTP status code. |
| 5xx Request | Count/s | InstanceCount5x xNumber NoOp _ | userId and instanceName | The number of requests that return a 5XX HTTP status code. |
| Internet Inbound | Bytes/s | InstanceExtranetI n NoOp _ | userId and instanceName | The inbound traffic over the Internet. |
| Internet Outbound | Bytes/s | InstanceExtranet Out NoOp _ | userId and instanceName | The outbound traffic over the Internet. |
| Free Outbound Internet | Bytes/s | InstanceFreeExtr anetOut NoOp _ | userId and instanceName | The free outbound traffic over the Internet. |
| Total Rows | Count/s | InstanceRowCou nt NoOp _ | userId and instanceName | The total number of rows. |
| Failed Rows | Count/s | InstanceFailRowC ount NoOp _ | userId and instanceName | The number of failed rows. |
| Storage Size | Byte | StorageSize | userId and instanceName | The storage size. |

### 2.4 Network

#### 2.4.1 NAT Gateway

This topic describes the metrics supported by NAT gateways. Set the **Namespace** parameter to **acs_nat_gateway**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Instance-related metrics**

ra Stack services

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Total number of sessions | Count | curr num _ | userId and instanceId | The total number of sessions. |
| Capacity Discard Connections (Cumulative Value) | Count | capacity drop _ | userId and instanceId | The number of capacity-dropped connections. |
| Number of new discarded connections (cumulative value) | Count | ratelimit drop _ | userId and instanceId | The number of new dropped connections. |
| Capacity Discard Connections Per Second | Count/s | capacity drop in _ _ c | userId and instanceId | The number of capacity-dropped connections per second. |
| Number of new and discarded connections per second | Count/s | ratelimit drop in _ _ c | userId and instanceId | The number of new dropped connections per second. |
| Number of new connections per second | Count/s | establish rate _ | userId and instanceId | The number of new connections per second. |

**SNAT-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| snet rx.rate _ | Bit/s | snet rx.rate _ | userId, instanceId, and snatentryId | The inbound bandwidth. |
| snet tx.rate _ | Bit/s | snet tx.rate _ | userId, instanceId, and snatentryId | The outbound bandwidth. |

#### 2.4.2 SLB

This topic describes the metrics supported by Server Load Balancer (SLB). Set the **Namespace** parameter to **acs_slb_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds. ra Stack services

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| InstanceActiveCon nection | Count | InstanceActiveConnec tion | userId and instanceId | The number of active TCP connections. |
| InstanceInactiveCo nnection | Count | InstanceInactiveConn ection | userId and instanceId | The number of inactive connections per second on the port. |
| InstanceMaxConne ction | Count/s | InstanceMaxConnecti on | userId and instanceId | The number of concurrent connections per second on the port. |
| InstanceNewConne ction | Count | InstanceNewConnecti on | userId and instanceId | The number of new TCP connections. |
| InstancePacketRX | Count/s | InstancePacketRX | userId and instanceId | The number of inbound packets per second. |
| InstancePacketTX | Count/s | InstancePacketTX | userId and instanceId | The number of outbound packets per second. |
| InternetInRate | Bit/s | InstanceTrafficRXNew | userId and instanceId | The inbound bandwidth. |
| InternetOutRate | Bit/s | InstanceTrafficTXNew | userId and instanceId | The outbound bandwidth. |
| UnhealthyServerCo unt | Count | InstanceUnhealthySer verCount | userId and instanceId | The number of unhealthy backend Elastic Compute Service (ECS) instances. |
| InstanceDropConne ction | Count/s | InstanceDropConnecti on | userId and instanceId | The number of connections dropped from the listener per second. |

ra Stack services

| InstanceDropTraffic RX | Bit/s | InstanceDropTrafficR X | userId and instanceId | The number of inbound bits dropped from the listener per second. |
|---|---|---|---|---|
| InstanceDropTraffic RX | Bit/s | InstanceDropTrafficT X | userId and instanceId | The number of outbound bits dropped from the listener per second. |
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

ra Stack services

| PacketInPerSecond | Count/s | PacketRX | userId, instanceId, and port | The number of inbound packets per second. |
|---|---|---|---|---|
| PacketOutPerSecon d | Count/s | PacketTX | userId, instanceId, and port | The number of outbound packets per second. |
| IntranetInRate | Bit/s | TrafficRXNew | userId, instanceId, and port | The inbound bandwidth. |
| IntranetOutRate | Bit/s | TrafficTXNew | userId, instanceId, and port | The outbound bandwidth. |
| UnhealthyServerCo unt | Count | UnhealthyServerC ount | userId, instanceId, and port | The number of unhealthy backend ECS instances. |
| DropConnection | Count/s | DropConnection | userId, instanceId, and port | The number of connections dropped from a listener per second. |
| DropTrafficRX | Bit/s | DropTrafficRX | userId, instanceId, and port | The number of inbound bits dropped from the listener per second. |
| DropTrafficTX | Bit/s | DropTrafficTX | userId, instanceId, and port | The number of outbound bits dropped from the listener per second. |
| DropPacketRX | Count/s | DropPacketRX | userId, instanceId, and port | The number of inbound packets dropped from the listener per second. |
| DropPacketTX | Count/s | DropPacketTX | userId, instanceId, and port | The number of outbound packets dropped per second. |
| Seven layers Qps | Reques ts/s | SevenFloorQps | userId, instanceId, and port | The number of queries per second at Layer 7. |

ra Stack services

| Number of connection failures per second | Count | FailConnection | userId, instanceId, and port | The number of failed connections per second. |
|---|---|---|---|---|

#### 2.4.3 EIP

This topic describes the metrics supported by Elastic IP Address (EIP). Set the **Namespace** parameter to **acs_vpc_eip**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| net rx.rate _ | Bit/s | net rx.rate _ | userId and instanceId | The inbound bandwidth. |
| net rxPkgs.rate _ | Count/s | net rxPkgs.rate _ | userId and instanceId | The rate of inbound packets. |
| net tx.rate _ | Bit/s | net tx.rate _ | userId and instanceId | The outbound bandwidth. |
| net txPkgs.rate _ | Count/s | net txPkgs.rate _ | userId and instanceId | The rate of outbound packets. |
| Out Ratelimit Drop Speed | Packets/s | out ratelimit dro _ _ p speed _ | userId and instanceId | The outbound packet loss rate. |
| In Ratelimit Drop Speed | Packets/s | in ratelimit drop _ _ speed _ | userId and instanceId | The inbound packet loss rate. |

#### 2.4.4 VPN Gateway

This topic describes the metrics supported by VPN Gateway. Set the **Namespace** parameter to **acs_vpn**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| IPSec.connection. rxPkgs | Packets/s | ipsec.rxPkgs | userId, instanceId, and ipsecId | The rate of inbound packets of the connection. |

ra Stack services

| IPSec.connection. txpkgs | Packets/s | ipsec.txPkgs | userId, instanceId, and ipsecId | The rate of outbound packets of the connection. |
|---|---|---|---|---|
| IPSec.connection. rx.rate | Bit/s | ipsec rx.rate _ | userId, instanceId, and ipsecId | The number of inbound bits of the connection per second. |
| IPSec.connection. tx.rate | Bit/s | ipsec tx.rate _ | userId, instanceId, and ipsecId | The number of outbound bits of the connection per second. |
| SSL Client Count | Count | ssl client.count _ | userId and instanceId | The number of connections. |

#### 2.4.5 DNS

This topic describes the metrics supported by DNS. Set the **Namespace** parameter to **acs_dns_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Latency | Milliseco nds | Latency | userId and instanceId | The parsing latency. |
| ParsingSucceed ed | Count | ParsingSucceeded | userId and instanceId | The number of successfully parsed records. |
| Total number of analyses | Count | ParsingTotal | userId and instanceId | The total number of parsed records. |

### 2.5 Application services

#### 2.5.1 API Gateway

This topic describes the metrics supported by API Gateway. Set the **Namespace** parameter to **acs_apigateway_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds. ra Stack services

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Latency | Milliseconds | Latency | userId and apiUid | The response time. |
| SumQPS | Count | SumQPS | userId and apiUid | The total queries per second (QPS). |
| TrafficRX | KB | TrafficRX | userId and apiUid | The inbound traffic. |
| TrafficTX | KB | TrafficTX | userId and apiUid | The outbound traffic. |
| code2XX Number | Count | code2XX | userId and apiUid | The number of times a 2XX HTTP status code is returned. |
| code4XX Number | Count | code4XX | userId and apiUid | The number of times a 4XX HTTP status code is returned. |
| code5XX Number | Count | code5XX | userId and apiUid | The number of times a 5XX HTTP status code is returned. |

### 2.6 Middleware services

#### 2.6.1 ApsaraMQ for RocketMQ

This topic describes the metrics supported by ApsaraMQ for RocketMQ. Set the **Namespace** parameter to **acs_rocketmq_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

ra Stack services

| Message retention duration | Hour | MessageRetentio nPeriod | userId and instanceId | The retention period of the message. |
|---|---|---|---|---|
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

ra Stack services

| Producer(GroupId ) Number of messages sent per minute | Count/min | SendMessageCou ntPerGid | userId, instanceId, and groupId | The number of messages that the producer sends per minute. |
|---|---|---|---|---|
| Consumer(GroupI d) receives message TPS | Count/min | ReceiveMessage TPSPerGid | userId, instanceId, and groupId | The TPS for receiving messages by the consumer per minute. |
| Producer(GroupId ) sends messages TPS | Count/min | SendMessageTPS PerGid | userId, instanceId, and groupId | The TPS for sending messages by the producer per minute. |

**Topic-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ReceiveMessage CountPerTopic | Count/min | ReceiveMessage CountPerTopic | userId, instanceId, and topic | The number of messages that the consumer receives per minute. |
| SendMessageCou ntPerTopic | Count/min | SendMessageCou ntPerTopic | userId, instanceId, and topic | The number of messages sent by the producer per minute. |
| Consumer(Topic) receives message TPS | Count/min | ReceiveMessage TPSPerTopic | userId, instanceId, and topic | The TPS for receiving messages by the consumer per minute. |
| Producer(Topic) sends messages TPS per minute | Count/min | SendMessageTPS PerTopic | userId, instanceId, and topic | The TPS for sending messages by the producer per minute. |

**Group and topic-related metrics**

| 22 |   |   | > Documen | t Version: 2025030 |
|---|---|---|---|---|

ra Stack services

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConsumerLagPer GidTopic | Count | ConsumerLagPer GidTopic | userId, instanceId, groupId, and topic | The number of accumulated messages. |
| ReceiveMessage CountPerGidTopic | Count/min | ReceiveMessage CountPerGidTopi c | userId, instanceId, groupId, and topic | The number of messages that the consumer receives per minute. |
| SendDLQMessag eCountPerGidTop ic | Count/min | SendDLQMessag eCountPerGidTop ic | userId, instanceId, groupId, and topic | The number of dead-letter messages generated per minute. |
| Producer(GroupId & Topic) Number of messages sent per minute | Count/min | SendMessageCou ntPerGidTopic | userId, instanceId, groupId, and topic | The number of messages that the producer sends per minute. |

### 2.7 Big data

#### 2.7.1 Stream Computing (Blink)

This topic describes the metrics supported by Stream Computing (Blink) Set the **Namespace** parameter to **acs_blink**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimensions | Description |
|---|---|---|---|---|
| FetchedDelay | Seconds | FetchedDelay | userId, regionId, projectName, and jobName | The processing latency. |
| Response Delay | % | inputDelay | userId, regionId, projectName, and jobName | The service latency. |

ra Stack services

| Read RPS | rps | ParserTpsRate | userId, regionId, projectName, and jobName | The read records per second (RPS). |
|---|---|---|---|---|
| Write RPS | RPS | SinkOutTpsRate | userId, regionId, projectName, and jobName | The write RPS. |
| FailoverRate | % | TaskFailoverRate | userId, regionId, projectName, and jobName | The failover rate. |

#### 2.7.2 DataHub

This topic describes the metrics supported by DataHub. Set the **Namespace** parameter to **acs_datahub**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| subscription delay time | Seconds | subscribe delay _ | userId, regionId, project, topic, and subId | The latency between the time when a user subscribes to data and the current system time. |
| Consumption latency | Seconds | consume delay _ | userId, regionId, project, topic, and subId | The latency between the time when a user subscribes to data and the time when the lasted data is generated. |
| Number of accumulated messages | Count | record stacked _ | userId, regionId, project, topic, and subId | The amount of accumulated data to be consumed by the subscriber. |

### 2.8 Security (Apsara Stack Security)

**Security)**

#### 2.8.1 Tenant-side bastion hosts

This topic describes the metrics for tenant-side bastion hosts. ra Stack services Set the **Namespace** parameter to **acs_bastionhost**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

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
| (ECS) root directory disk usage | % | RootDiskUtilization | userId and instanceId | The disk usage of the root directory. |
| (ECS)Docker directory disk usage | % | DockerDiskUtilizatio n | userId and instanceId | The disk usage of the Docker directory. |
| (ECS) root directory disk remaining | GB | DfRootBfree | userId and instanceId | The available disk space of the root directory. |
| (ECS) root directory disk used | GB | DfRootUsed | userId and instanceId | The used disk space of the root directory. |

ra Stack services

| (ECS) Total number of root directory disks | GB | DfRootBtotl | userId and instanceId | The total disk space of the root directory. |
|---|---|---|---|---|
| (ECS)Docker directory disk remaining | GB | DfDockerBfree | userId and instanceId | The available disk space of the Docker directory. |
| (ECS)Docker directory disk used | GB | DfDockerUsed | userId and instanceId | The used disk space of the Docker directory. |
| (ECS) Total number of Docker directory disks | GB | DfDockerBtotl | userId and instanceId | The total disk space of the Docker directory. |
| (ECS) root Inode usage | % | RootInodeUtilization | userId and instanceId | The inode usage of the root directory. |
| (ECS)Docker directory Inode usage | % | DockerInodeUtilizati on | userId and instanceId | The inode usage of the Docker directory. |
| (ECS) network ingress traffic | Bytes/s | TrafficBytin | userId and instanceId | The inbound traffic. |
| (ECS) network egress traffic | Bytes/s | TrafficBytout | userId and instanceId | The outbound traffic. |
| (ECS)tcp links | Count | TcpConnections | userId and instanceId | The number of TCP connections. |
| (ECS) number of processes | Count | ProcessNumber | userId and instanceId | The number of processes. |
| (ECS)NTP service offset | Second s | NtpOffset | userId and instanceId | The offset of the Network Time Protocol (NTP) service. |

ra Stack services

| (ECS) Whether the Docker service is running properly | Count/s | DockerService | userId and instanceId | The status of the Docker service. Valid values: 0: The Docker service does not exist. 1: The Docker service exists. |
|---|---|---|---|---|

**Business-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CountSession | Count | CountSession | instanceId | The number of real- time sessions. |
| CountUser | Count | CountUser | instanceId | The number of users of the bastion host. |
| CountHost | Count | CountHost | instanceId | The number of hosts managed by the bastion host. |
| CountHostQuota | Count | CountHostQuota | instanceId | The quota of hosts that can be managed by the bastion host. |
| CountVisitPolicy | Count | CountVisitPolicy | instanceId | The number of access policies of the bastion host. |
| CountCommandP olicy | Count | CountCommandPolic y | instanceId | The number of command policies of the bastion host. |
| CountWorkorderP olicy | Count | CountWorkorderPolic y | instanceId | The number of ticket policies of the bastion host. |

ra Stack services

| CountWarningDay Un | Count | CountWarningDayUn | instanceId | The number of alerts that the bastion host does not handle on the current day. |
|---|---|---|---|---|
| CountWarningDay | Count | CountWarningDay | instanceId | The total number of alerts on the current day. |
| NICBindWidthRx | Mbit/s | NICBindWidthRx | instanceId | The inbound bandwidth of the network interface controller (NIC). |
| NICBindWidthTx | Mbit/s | NICBindWidthTx | instanceId | The outbound bandwidth of the NIC. |
| CountAppServerR un | Count | CountAppServerRun | instanceId | The number of frontend hosts in the normal state. |
| CountAppServerF ault | Count | CountAppServerFault | instanceId | The number of frontend hosts in the abnormal state. |

**Health check-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Service) Service Health Check | Count/s | ServiceHealthCheck | userId and instanceId | The status of the health check service. Valid values: 0: The service does not work as expected. 1: The service works as expected. |

#### 2.8.2 Vulnerability scanner engines

ra Stack services This topic describes the metrics for vulnerability scanner engines. Set the **Namespace** parameter to **acs_scanner**. Set the **Period** parameter to an integer multiple of 60. Default value: **60**. Unit: seconds.

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
| (ECS)Docker directory disk usage | % | DockerDiskUtilizatio n | userId and instanceId | The disk usage of the Docker directory. |
| (ECS)Docker directory disk remaining | GB | DfDockerBfree | userId and instanceId | The available disk space of the Docker directory. |
| (ECS)Docker directory disk used | GB | DfDockerUsed | userId and instanceId | The used disk space of the Docker directory. |

ra Stack services

| (ECS) Total number of Docker directory disks | GB | DfDockerBtotl | userId and instanceId | The total disk space of the Docker directory. |
|---|---|---|---|---|
| (ECS) root directory disk remaining | GB | DfRootBfree | userId and instanceId | The available disk space of the root directory. |
| (ECS) root directory disk used | GB | DfRootUsed | userId and instanceId | The used disk space of the root directory. |
| (ECS) Total number of root directory disks | GB | DfRootBtotl | userId and instanceId | The total disk space of the root directory. |
| (ECS) root Inode usage | % | RootInodeUtilization | userId and instanceId | The inode usage of the root directory. |
| (ECS)Docker directory Inode usage | % | DockerInodeUtilizati on | userId and instanceId | The inode usage of the Docker directory. |
| (ECS) network ingress traffic | Bytes/s | TrafficBytin | userId and instanceId | The inbound traffic. |
| (ECS) network egress traffic | Bytes/s | TrafficBytout | userId and instanceId | The outbound traffic. |
| (ECS)tcp links | Count/s | TcpConnections | userId and instanceId | The number of TCP connections. |
| (ECS) number of processes | Count | ProcessNumber | userId and instanceId | The number of processes. |
| (ECS)NTP service offset | Second s | NtpOffset | userId and instanceId | The offset of the Network Time Protocol (NTP) service. |

ra Stack services

| (ECS) Whether the Docker service is running properly | Count/s | DockerService | userId and instanceId | The status of the Docker service. Valid values: 0: The Docker service does not exist. 1: The Docker service exists. |
|---|---|---|---|---|

**Health check-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Service) Service Health Check | Count/s | ServiceHealthCheck | userId and instanceId | The status of the health check service. Valid values: 0: The service does not work as expected. 1: The service works as expected. |
