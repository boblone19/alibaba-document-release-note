---
title: "Application Real-time Monitoring Service Developer Guide 20250619"
product_version: "V3.18.6"
pdf_pages: 110
source_pdf: "70f0cfc14273028b_Alibaba Cloud Apsara Stack V3.18.6 Application Real-time Monitoring Service Developer Guide 20250619"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%BA%94%E7%94%A8%E5%AE%9E%E6%97%B6%E7%9B%91%E6%8E%A7%E6%9C%8D%E5%8A%A1%20ARMS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Application%20Real-time%20Monitoring%20Service%20Developer%20Guide%2020250619.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Application Real-time Monitoring Service Developer Guide 20250619

## Table of Contents

- 1 Overview
- 2 Postman request examples
- 3 Dataset query
  - 3.1 Overview
  - 3.2 Description of request parameters
  - 3.3 API reference
  - 3.4 Response code
- 4 Event set query
- 5 API Reference
  - 5.1 Log on to the Apsara Uni-manager Management Console
  - 5.2 Obtain AccessKey pairs of an organization
  - 5.3 Application Monitoring
    - 5.3.1 ConfigApp
    - 5.3.2 SaveTraceAppConfig
    - 5.3.3 GetTrace
    - 5.3.4 GetTraceApp
    - 5.3.5 GetStack
    - 5.3.6 ListTraceApps
    - 5.3.7 SearchTraceAppByName
    - 5.3.8 SearchTraceAppByPage
    - 5.3.9 SearchTraces
    - 5.3.10 SearchTracesByPage
    - 5.3.11 QueryMetric
    - 5.3.12 DeleteTraceApp
    - 5.3.13 GetArmsAgentDownLoadUrl
    - 5.3.14 DescribeTraceLicenseKey
    - 5.3.15 DescribeTraceLocation
  - 5.4 Alerting
    - 5.4.1 UpdateAlertRule
    - 5.4.2 DeleteAlertRules
    - 5.4.3 SearchAlertRules
    - 5.4.4 CreateAlertContact
    - 5.4.5 DeleteAlertContact
    - 5.4.6 UpdateAlertContact
    - 5.4.7 SearchAlertContact
    - 5.4.8 CreateAlertContactGroup
    - 5.4.9 DeleteAlertContactGroup
    - 5.4.10 UpdateAlertContactGroup
    - 5.4.11 SearchAlertContactGroup
    - 5.4.12 StartAlert
    - 5.4.13 StopAlert
    - 5.4.14 SearchEvents
    - 5.4.15 SearchAlertHistories

## 1 Overview

This document is the ARMS Developer Guide, which focuses on how to use ARMS RESTful API to query datasets and how to use ES RESTful API to query event sets. This document contains the following information: Parameter description: ARMS API specifications, including detailed descriptions of API paths, methods, input parameters, and response parameters. Response Code: Descriptions of the responses returned when API calls encounter errors. Detailed interface information and usage examples: Including general dataset queries, dataset drill down queries, multi-dimension dataset queries, and WhereIn condition dataset query interfaces. Common query interfaces and syntax for event sets. t examples

## 2 Postman request examples

Before using ARMS Open API and ES API, you can test them with the third-party software Postman to ensure access to dataset and event set data. Figure 1. Testing ARMS Open API with Postman Figure 2. Testing ES Rest API with Postman

## 3 Dataset query

### 3.1 Overview

This chapter describes the parameters, interfaces, and response codes related to dataset queries.

### 3.2 Description of request parameters

**parameters**

This topic describes the specific meaning of API request fields for ARMS dataset query.

> **Note:** List[String] indicates the string returned after the toString() method is called on a List.

| Field name | Field type | Description | Required | Note |
|---|---|---|---|---|
| datasetId | Long | The dataset ID | Yes |   |
| minTime | Long | The start time of the query | Yes |   |
| maxTime | Long | The end time of the query | Yes |   |
| intervalInSec | Integer | The time interval of data segments | Yes |   |
| measures | List[String] | The list of metrics to query | No | The list supports a maximum of 3 elements. If the list is empty, all metric data is returned. |
| isDrillDown | Boolean | Specifies whether to drill down | No |   |
| dimensions | List[String] | The query dimensions | No |   |
| whereInKey | String | The key field for Where In conditional query | No |   |

| whereInValues | List[String] | The key field values for Where In conditional query | No |   |
|---|---|---|---|---|
| requiredDims | List[String] | The required dimensions for general datasets | No |   |
| optionalDims | List[String] | The optional dimensions for general datasets | No |   |
| orderByKey | String | The orderBy metric | No |   |
| limit | Integer | The maximum number of returned entries | No |   |
| reduceTail | Boolean | Specifies whether to merge data beyond the limit | No |   |
| userId _ | String | The user ID |   | In Apsara Stack, userId is the same _ as the username. For example, the user ID of the ARMS administrator is arms admin. _ |

### 3.3 API reference

This topic provides examples of ARMS dataset query APIs. The following examples use Java Apache HTTP Client and Python scripts to send HTTP Post requests to obtain data. You can also select other languages as needed, such as Ruby.

**Dataset query API**

You can call this API to query general dataset data. This topic provides Java and Python examples.

**Java Apache HTTP request example**

```java
import org.apache.http.HttpResponse; import org.apache.http.NameValuePair; import org.apache.http.client.HttpClient; import org.apache.http.client.entity.UrlEncodedFormEntity; import org.apache.http.client.methods.HttpPost; import org.apache.http.impl.client.HttpClientBuilder; import org.apache.http.message.BasicNameValuePair; import org.junit.Test; import java.io.BufferedReader; import java.io.InputStreamReader; import java.util.ArrayList; import java.util.List; public class GeneralQueryTest {
    public static final String url =
"http://***.**.**.**:8099/dataset/GeneralQuery.json";
    @Test
    public void GeneralQueryTest() throws Exception {
        HttpClient client = HttpClientBuilder.create().build();
        HttpPost post = new HttpPost(url);
        // add header
        post.setHeader("Content-Type", "application/x-www-form-urlencoded");
        // add post parameters
        List<NameValuePair> urlParameters = new ArrayList<>();
        urlParameters.add(new BasicNameValuePair("datasetId", "1837"));
        urlParameters.add(new BasicNameValuePair("isDrillDown", "false"));
        urlParameters.add(new BasicNameValuePair("maxTime", "1494851400000"));
        urlParameters.add(new BasicNameValuePair("intervalInSec", "60"));
        urlParameters.add(new BasicNameValuePair("minTime", "1494850980000"));
        urlParameters.add(new BasicNameValuePair("_userId", "11************596"));
        urlParameters.add(new BasicNameValuePair("dateStr", "date"));
        urlParameters.add(new BasicNameValuePair("measures", "MAX_load_load1"));
        post.setEntity(new UrlEncodedFormEntity(urlParameters));
        // send post
        HttpResponse response = client.execute(post);
        // analyse result
        BufferedReader rd = new BufferedReader(
                new InputStreamReader(response.getEntity().getContent()));
        StringBuffer result = new StringBuffer();
        String line = "";
        while ((line = rd.readLine()) != null) {
            result.append(line);
```

**Python request example**

```java
#!/usr/bin/python
#-*-coding:utf-8 -*-
import httplib, urllib try:
        params = urllib.urlencode({'datasetId': '1837',
                                   'isDrillDown': 'false',
                                   'maxTime': '1494851400000',
                                   'intervalInSec': '60',
                                   'minTime': '1494850980000',
                                   '_userId': '11***********96',
                                   'dateStr': 'date',
                                   'measures': 'MAX_load_load1'
```

`})`

```json
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        conn = httplib.HTTPConnection("***:**:**:**",8099)
        conn.request("POST", "/dataset/GeneralQuery.json", params, headers)
        response = conn.getresponse()
        print response.read()
except Exception,e:
        print str(e)
finally:
        if conn:
                conn.close()
```

**Drill down dataset query API**

This example code is basically the same as the **Java Apache HTTP request example** code in the Dataset query API. You only need to modify one line of code.

```
urlParameters.add(new BasicNameValuePair("isDrillDown", "false"));
```

Should be modified to:

```
urlParameters.add(new BasicNameValuePair("isDrillDown", "true"));
```

**Drill down dataset multi-dimension query API**

This example code is basically the same as the **Java Apache HTTP request example** code in the Dataset query API. You only need to add the following code:

```
Map<String, String> dimension = new LinkedMap(); dimension.put("value", "hz"); dimension.put("key", "area"); dimension.put("type", "ALL"); List<Map<String, String>> dimensions = Lists.newArrayList(); dimensions.add(dimension);
```

**WHERE IN condition dataset query API**

This example code is basically the same as the **Java Apache HTTP request example** code in the Dataset query API. You only need to add the following code:

```
urlParameters.add(new BasicNameValuePair("whereInKey","area"); List<String> whereInValues = new ArrayList<>(); whereInValues.add("hz"); whereInValues.add("bj"); urlParameters.add(new BasicNameValuePair("whereInValues", whereInValues.toString()));
```

**General dataset query API**

This example code is basically the same as the **Java Apache HTTP request example** code in the Dataset query API. You only need to add the following code:

```
Map<String, String> optionalDim = Maps.newTreeMap(); optionalDim.put("value", "hz"); optionalDim.put("key", "area"); optionalDim.put("type", "ALL"); List<Map<String, String>> optionalDims = Lists.newArrayList(); optionalDims.add(optionalDim);
```

### 3.4 Response code

This topic describes response content and corresponding troubleshooting methods. The general response results returned by the API include the following content:

| Name | Description |
|---|---|
| code | Error code |
| data | Specific information of ARMS query results |
| message | Error message |
| success | Whether the operation is successful (true or false) |

**ErrMsg dataset does not exist**

`{`

```json
    "code": 200,
    "data": "{\"actualSizeFromDB\":0,\"errMsg\":\"Dataset ID does not exist!\",\
    "message": "success",
    "success": true
```

Solutions: Verify whether the dataset ID is spelled correctly and whether the dataset ID belongs to the user in ARMS.

**ErrMsg query result is empty**

`{`

```json
    "code": 200,
    "data": "{\"actualSizeFromDB\":0,\"errMsg\":\"Query result is empty\",\
    "message": "success",
    "success": true
```

Solutions:
1. Verify whether data exists between the requested start time and end time.
2. If a dimension is selected, verify whether data exists for that dimension.
3. Verify whether _userId is set incorrectly. In Apsara Stack, _userId is the same as the
username.

**Code 500**

This code indicates an internal ARMS error. Solution: Contact ARMS developers.

**Code 200**

This code indicates that the access was processed successfully.

## 4 Event set query

**Request parameters**

ARMS event sets rely on ElasticSearch as the underlying dependency. You can directly use ElasticSearch Rest API to query and operate data. When performing queries or other operations, you must specify the following parameters:

|   | Description | Note |
|---|---|---|
| ES machine IP | IP address of the ES cluster machine | You can query the IP address in the region.yaml configuration file of the corresponding machine in arms-console |
| Index | The underlying storage index of the event set | The method to obtain the index is described below |
| Type | The type of the underlying storage index of the event set | The type value is fixed as arms event _ |

**How to obtain the index of an event set**

Before obtaining the index of an event set, you need to obtain the user ID, event set ID, and event set name.
1. Obtain the user ID.
2. Obtain the event set ID by viewing the event set list interface on the event search page in
the browser. The indexes of event sets are divided into the following two types: Daily rolling index Value rule: arms_event_user ID_event set ID_event set name_time Example: arms_event_1098370038733503_198_envent_2018-03-28 Alias index Value rule: arms_alias_user ID_event set ID_event set name_time Example: event_alias_1098370038733503_198_envent

**Query API**

The Rest API query interface is:

```
http://IP:9200/index/arms_event/_search
```

Or:

```
http://IP:9200/index/_search
```

For query syntax, see the official ES website.

## 5 API Reference

### 5.1 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

You need to obtain the endpoint of the Apsara Uni-manager Management Console from the deployment personnel. A browser is available. We recommend using Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press Enter.

> **Note:** You can click the current language in the upper-right corner to switch to another language.
> The Authorized Login button is displayed only when a global IdP is configured in third-party authentication. You can customize the name of the Authorized Login button based on your requirements.

Enteryourusernameandpassword
2. Enter your username and password.

> **Note:** Obtain the username and password for the Apsara Uni-manager Management Console from the operations administrator.
> The first time you log on to the Apsara Uni-manager Management Console, you must change your account password as prompted. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %

3. Click **Account Logon**.
4. If your account has multi-factor authentication (MFA) enabled, perform the corresponding
operations in the following scenarios:

**First logon after the administrator enforces MFA**

a. On the Bind Virtual MFA Device page, bind an MFA device as prompted. b. Re-enter your account and password as described in Step 2, and click **Account Login**. c. Enter the 6-digit MFA code and click **Authenticate**.

**You have enabled and bound MFA**

Enter the 6-digit MFA code and click **Authenticate**.

**Note**

For more information about how to bind and enable MFA, see Manage multi-factor authentication.

**Related operations**

**Forgot password**

1. If you forget your logon password, click **Forget Password** below the password input box.
2. On the Forgot Password page, enter your **Account Name**, **Email Address**, and verification
code, and then click **Confirm**.

> **Note:** You can use the username of your account and the email address that was used to create the account.
> A password reset link will be sent to your email. You can enter a new password after accessing the link.

### 5.2 Obtain AccessKey pairs of an organization

**organization**

An AccessKey pair that consists of an AccessKey ID and an AccessKey secret is used to implement symmetric encryption. This helps you verify the identity of a requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain the AccessKey pair of an organization.

**Prerequisites**

Only operations administrators and level-1 organization administrators can obtain AccessKey pairs for organization accounts.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. On the **Enterprise** page, choose **Resource Management > Organizations** in the left-
side navigation pane.
4. In the left-side navigation pane of the **Organizations** page, click the name of the level -1
organization that you want to manage. On the page that appears, click **Manage**
**AccessKey** in the upper-right corner.
5. In the dialog box that appears, obtain the AccessKey ID and AccessKey secret of the
organization.

> **Note:** You must use the AccessKey pair of an organization that is enabled when you call this operation. If the AccessKey pair is disabled, you cannot call API operations.

### 5.3 Application Monitoring

#### 5.3.1 ConfigApp

Turns on or turns off the main switch of an ARMS agent, or queries the status of the main switch.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConfigApp | The operation that you want to perform. Set the value to ConfigApp. |

| AppIds | String | Yes | iioe7jcnuk@582 846f37******,atc 889zkcf@d8dee dfa9bf****** | The ID of the application, which is the pid. Separate multiple PIDs with commas (,). |
|---|---|---|---|---|
| Enable | String | Yes | true | Specifies whether to turn on or off the main switch of the agent. The monitoring stops after the switch is turned off. If you do not specify this parameter, the main switch status of the ARMS agent is queried. true: enables the Agent master switch. false: disables the master switch for the agent. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | abc@def success\nghi@jkl success\n | The result of turning on or off the main switch of the agent or the main switch status of the agent. |
| RequestId | String | 16AF921B-8187- 489F-9913- 43C808B4**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ConfigApp &AppIds=iioe7jcnuk@582846f37******,atc889zkcf@d8deedfa9bf****** &Enable=true &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>16AF921B-8187-489F-9913-43C808B4****</RequestId> <Data>abc@def success\nghi@jkl success\n</Data>
 JSON format
```

`{`

```json
    "RequestId": "16AF921B-8187-489F-9913-43C808B4****",
    "Data": "abc@def success\\nghi@jkl success\\n"
```

#### 5.3.2 SaveTraceAppConfig

Modifies the settings of Application Monitoring, such as trace sampling and agent switch settings.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SaveTraceAppC onfig | The operation that you want to perform. Set the value to SaveTraceAppConfig. |
| Pid | String | Yes | a2n80plglh@74 5eddx | The process identifier (PID) of the application. |
| Settings.N.Key | String | Yes | sampling.enable | The key of the setting that you want to modify. For more information about the supported settings, see the following sections. Trace sampling settings Main switch settings Threshold setting Advanced Settings Thread setting Memory snapshot settings URL convergence settings Business log association settings Business monitoring settings |
| Settings.N.Value | String | Yes | true | The value of the setting that you want to modify. For more information about the supported settings, see the following sections. Trace sampling settings Main switch settings Threshold setting Advanced Settings Thread setting Memory snapshot settings URL convergence settings Business log association settings Business monitoring settings |
| RegionId | String | No | cn-hangzhou | Required. The ID of the region. |

**Call trace sampling fields**

| Key | Response parameters | Value |
|---|---|---|
| sampling.enable | Specifies whether to turn on the sampling switch. | Valid values: - true : turn on the sampling switch. - false : Turn off the sampling switch, the call chain function will be turned off. |
| sampling.rate | The sampling rate. If you increase the sample rate, additional system resources may be consumed. The maximum number of records collected per second is limited. When 100 records are collected per second, the overhead is about 300m memory. To adjust the maximum number of collections per second, you can modify the throttling threshold. | Valid values: 0 to 100. Default value: 10. |

**Master Switch Field Description**

| Key | Response parameters | Value |
|---|---|---|
| enable | Specifies whether to turn on the main switch of agents. | Valid values: - true : Turn on the main switch of the agent. - false : Turn off the main switch of the agent. |
| agent.logger.level | Log-Level Configuration | Valid values: - DEBUG - INFO - WARN - ERROR |

| dubbo.enable mongodb.enable hsf.enable httpclient3.enable httpclient4.enable jdkhttp.enable jetty.enable mybatis.enable mysql.enable okhttp.enable oracle.enable postgresql.enable redis.enable spring.enable springboot.enable tomcat.enable lettuc.enable grpc.enable thrift.enable hystrix.enable rxjava.enable googlehttpclient.enable | Plug-in switch | Valid values: - true - false |
|---|---|---|

**Threshold field description**

| Key | Response parameters | Value |
|---|---|---|
| thresholds.limit | The throttling threshold. The maximum number of requests that the Agent can process per second. | Default value: 100. Maximum value: 2000. |
| thresholds.interface | The response time threshold of the interface. When the response time of an interface is greater than the threshold, the interface is marked as a slow call. | Default value: 500. Unit: ms. Maximum value: 2000. |
| thresholds.sql | The threshold for slow SQL queries. If the duration of an SQL query exceeds the threshold, the query is marked as a slow SQL statement. | Default value: 500. Unit: ms. Maximum value: 2000. |

**Advanced Field Description**

| Key | Response parameters | Value |
|---|---|---|
| defined.excludeurl | The filtering of invalid API calls. | Separate multiple API calls with commas (,). Example: /service/taobao,/service/status. |
| callstack.maxLength | The maximum length of the method stack. | This value indicates the number of entries. Maximum value: 400. Default value: 128. |
| exception.stacktrace | Similar Exception Stack Differentiation Depth | The stack depth used to distinguish exceptions of the same type. Generally, this parameter is set to the depth of the first difference call. Maximum value: 100. |
| callsql.maxLength | The maximum length of the collected SQL statement. | This value indicates the number of characters. Valid values: 256 to 4096. Default value: 1024. |
| jdbc.tracesqlbindvalue | Collect SQL Bind Values | Captures the value of the variable bound to the PrepareStatement parameter and takes effect without restarting the application. Valid values: - true - false |
| jdbc.tracesqlraw | Indicates whether the original SQL statement is displayed. | Only the SQL statement is truncated without additional processing. Valid values: - true - false |

| exception.whitelist | The filtering of exceptions. | Use a regular expression to match the full name of an exception class. Separate multiple exceptions with commas (,). Example: java.lang.InterrupetedException ,java.lang.IndexOutOfBoundsEx ception. The exceptions of the categories that you specify are not displayed in the charts on the Application Details and Exceptions Diagnosis pages. |
|---|---|---|
| error.skip | The filtering of errors. | By default, status code greater than 400 are counted as the number of errors. You can set the status code to be ignored. Separate multiple error codes with commas (,), for example, 429 or 429,512. This key is supported by the ARMS agent V2.5.7.2 or later. |
| spanV3.enable | New format of call chain | Adopts a new storage format that supports chronological ordering of call chains. Valid values: - true (default) - false |
| compress.enable | Call chain compression | Indicates whether to simplify repeated calls, such as for loops, to take effect without the need to restart the application. Valid values: - true - false |
| param.maxLength | Maximum length of request input parameters | The default value is 512 characters. The maximum length supported is 2048 characters and the minimum length is 256 characters. |
| quantile.enable | quantile statistics | Indicates whether the quantile statistics feature is enabled. Valid values: - true - false |

| AIAlert.enable | The agent version must be V2.5.8 or later. | Emergency alerts such as thread deadlocks and OOM alerts are supported. Valid values: - true - false |
|---|---|---|
| threadpoolmonitor.enable | Thread pool monitoring | You can monitor the thread pool metrics of frameworks such as Tomcat, Dubbo, and HSF. Upgrade the agent version to the latest version. Valid values: - true - false Restart the application to take effect. |
| rabbitmq.client.consumer.class es | RabbitMQ custom consumer | By setting the class name of a custom consumer or the class name that contains an anonymous internal consumer, you can see the call link of that consumer. You can specify multiple class names and separate them with commas (,). Restart the application to take effect. |
| kafka.consumer.entryPoint | Kafka custom consumers | By setting the class name of a custom consumer or the class name that contains an anonymous internal consumer, you can see the call link of that consumer. You can specify multiple class names and separate them with commas (,). Restart the application to take effect. |

| convergence.dneReq2Error.ena ble | 404 Request Convergence Switch | The default value is true, which converges the 404 request to /error. In this case, the interface call shows the converged interface /error (the call link cannot be queried), and the call link record is the original interface name. Valid values: - true - false |
|---|---|---|

**Thread field description**

| Key | Response parameters | Value |
|---|---|---|
| tprof.enableThreadProfiler | Specifies whether to turn on the main switch of thread profiling. | Valid values: - true : Turn on the thread profiling master control switch. - false : Turn off the thread profiling master switch. If you turn on this switch, the native method stacks of slow API calls are automatically saved. |
| tprof.threadProfilerSlowInteracti onRt | The time threshold to trigger the listener for slow API calls. | Default value: 2000. Unit: milliseconds. If the amount of time consumed by slow API calls exceeds the threshold, thread profiling is enabled. We recommend that you set the value to the 99th percentile of the amount of time consumed. If you set a value smaller than 2000, the CPU consumption is increased. We recommend that you set a value greater than or equal to 500. Unit: milliseconds. The maximum value is 10000ms. |
| tprof.enableThreadStackRecord er | Specifies whether to enable the thread diagnostics method stack. | Valid values: - true : enables the thread diagnosis method stack. - false : Disables the thread diagnostics method stack. If you enable this feature, the method stack is collected every 5 minutes. |

**URL convergence fields**

| Key | Response parameters | Value |
|---|---|---|
| convergence.enable | Specifies whether to enable the URL convergence feature. | Valid values: - true : enables converged URLs. - false : Disable converged URLs. |
| convergence.minServerSize | The convergence threshold. | The default value is 1000. If the value is greater than this threshold, convergence is performed. |
| convergence.pattern | The regular expression of convergence rules. | You can use regular expressions to set convergence rules. Separate multiple regular expressions with commas (,). Example:/service/(.*?)/demo. |
| convergence.excludes | Exclusion rules | You can use regular expressions to set exclusion rules. Separate multiple regular expressions with commas (,). Example:/service/\d +/demo. |

**Description of fields associated with business logs**

| Key | Response parameters | Value |
|---|---|---|
| logging.enable | Specifies whether to turn on the switch that associates trace IDs with business logs. | Valid values: - true : Turn on Associate Business Logs with TraceId. - false : Turn off Associate Business Logs with TraceId. If you turn on this switch, trace IDs are automatically generated in the business logs of an application. This setting takes effect after you restart the application. Logging utilities such as Log4j, Log4j2, and Logback are supported. You must add %X{EagleEye- TraceID} to the log layout to generate trace IDs. |

| SLS.project | The Log Service project that stores the business logs generated in the current region. | You can specify the name of the Log Service project that stores the business logs generated in the current region. |
|---|---|---|
| SLS.logStore | The Log Service Logstore that stores the business logs generated in the current region. | You can specify the name of the Log Service Logstore that stores the business logs generated in the current region. |
| SLS.index | The type of indexes of business logs generated in the current region. | Valid values: If full-text index is specified, this parameter is not specified. If you want to use a field- specific index, use the name of the field as the value. For example: SLS.index: tag. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | success | Indicates whether the request was successful. |
| RequestId | String | 78901766-3806- 4E96-8E47- CFEF59E4**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SaveTraceAppConfig &Pid=a2n80plglh@745eddx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>78901766-3806-4E96-8E47-CFEF59E4****</RequestId> <Data>success</Data>
 JSON format
```

`{`

```json
    "RequestId": "78901766-3806-4E96-8E47-CFEF59E4****",
    "Data": "success"
```

#### 5.3.3 GetTrace

Queries the details of a trace.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetTrace | The operation that you want to perform. Set the value to GetTrace. |
| RegionId | String | Yes | cn-beijing | The ID of the region. |
| TraceID | String | Yes | ac14001a15954 493811405707d **** | The unique ID of the trace. |

**Response parameters**

| Parameter | Type | Example | Details |
|---|---|---|---|
| RequestId | String | 1E2B6A4C-6B83- 4062-8B6F- AEEC1F****** | The request ID. |
| Spans | Array of Span |   | The spans that are contained in the trace. |
| Duration | Long | 1000 | The duration. Unit: milliseconds. |
| HaveStack | Boolean | false | Indicates whether a method stack was provided. true : There is a method stack. false : No method stack. |
| LogEventList | Array of LogEvent |   | The log events. |
| TagEntryList | Array of TagEntry |   | The tags. |
| Key | String | logLevel | The tag key of the log event. |

| Value | String | Warning | The tag value in the log event. |
|---|---|---|---|
| Timestamp | Long | 158368320204700 0 | The timestamp when the log event was generated. |
| OperationNam e | String | /api/demo | The name of the traced span. |
| ParentSpanId | String | 18 | The ID of the parent span. |
| ResultCode | String | 200 | The status code returned. |
| RpcId | String | 1.1 | The parent-child and sibling relationship between spans. For example, span 1.1 is the parent of span 1.1.1, and span 1.1.2 and span 1.1.1 are siblings. |
| RpcType | Integer | 101 | The type of the function call. 101: indicates that the client calls 102: indicates that the server calls 103: indicates that the producer calls the 104: indicates that the consumer calls 105: indicates a DB call 106: indicates an Xtrace Other call _ |
| ServiceIp | String | 192.168.XX.XX | The IP address of the server where the span resides. |
| ServiceName | String | server1 | The name of the application. |
| SpanId | String | fec891bb8f**** | The ID of the span. |
| TagEntryList | Array of TagEntry |   | The list of tag items. |
| Key | String | logLevel | The tag key of the span. |
| Value | String | Warning | The tag value in the span. |
| Timestamp | Long | 158368320204700 0 | The timestamp generated when the span was generated. |
| TraceID | String | ac14001a1595449 3811405707d**** | The unique ID of the trace. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetTrace &RegionId=cn-beijing &TraceID=ac14001a15954493811405707d**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>1E2B6A4C-6B83-4062-8B6F-AEEC1F******</RequestId> <Spans>
    <HaveStack>false</HaveStack>
    <ParentSpanId>18</ParentSpanId>
    <ServiceIp>192.168.XX.XX</ServiceIp>
    <ServiceName>server1</ServiceName>
    <OperationName>/api/demo</OperationName>
    <RpcType>101</RpcType>
    <RpcId>1.1</RpcId>
    <TraceID>ac14001a15954493811405707d****</TraceID>
    <Duration>1000</Duration>
    <Timestamp>1583683202047000</Timestamp>
    <ResultCode>200</ResultCode>
    <SpanId>fec891bb8f****</SpanId>
    <TagEntryList>
        <Value>Warning</Value>
        <Key>logLevel</Key>
    </TagEntryList>
    <LogEventList>
        <Timestamp>1583683202047000</Timestamp>
        <TagEntryList>
            <Value>Warning</Value>
            <Key>logLevel</Key>
        </TagEntryList>
    </LogEventList>
</Spans>
 JSON format
```

`{`

```json
    "RequestId": "1E2B6A4C-6B83-4062-8B6F-AEEC1F******",
    "Spans": {
        "HaveStack": false,
        "ParentSpanId": 18,
        "ServiceIp": "192.168.XX.XX",
        "ServiceName": "server1",
        "OperationName": "/api/demo",
        "RpcType": 101,
        "RpcId": 1.1,
        "TraceID": "ac14001a15954493811405707d****",
        "Duration": 1000,
        "Timestamp": 1583683202047000,
        "ResultCode": 200,
        "SpanId": "fec891bb8f****",
        "TagEntryList": {
            "Value": "Warning",
            "Key": "logLevel"
```

`},`

```json
        "LogEventList": {
            "Timestamp": 1583683202047000,
            "TagEntryList": {
                "Value": "Warning",
                "Key": "logLevel"
```

#### 5.3.4 GetTraceApp

Queries the details of a application monitoring task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetTraceApp | The operation that you want to perform. Set the value to GetTraceApp. |
| Pid | String | Yes | b590lhguqs@d8 deedfa9bf**** | The process identifier (PID) of the application. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |

**Response parameters**

| Parameter | Type | Example | Details |
|---|---|---|---|

| RequestId | String | D80ADAAC-8C32- 5479-BD14- C28CF832**** | The request ID. |
|---|---|---|---|
| TraceApp | Struct |   | The returned struct. |
| AppId | Long | 123 | The application ID. |
| AppName | String | arms-k8s-demo | The name of the application. |
| CreateTime | Long | 1576599253000 | The timestamp that indicates the time when the pod was created. |
| Labels | List | [ "test", "123123123", "uat" ], | The application tag. |
| Pid | String | b590lhguqs@d8de edfa9bf**** | The process identifier (PID) of the application. |
| RegionId | String | cn-hangzhou | The region ID of the resource. |
| Show | Boolean | true | Indicates whether the application is displayed in the Application Real-Time Monitoring Service (ARMS) console. Valid values: true false: does not display the image. Note If the advanced monitoring feature is not enabled in the EDAS console, the application is displayed as false . |
| Type | String | TRACE | The type of the monitoring task. Only the application monitoring type TRACE is supported. |
| UpdateTime | Long | 1635700348000 | The timestamp generated when the task information was updated. |
| UserId | String | 113197164949**** | The ID of the Resource Access Management (RAM) user that you use. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetTraceApp &Pid=b590lhguqs@d8deedfa9bf**** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>D80ADAAC-8C32-5479-BD14-C28CF832****</RequestId> <TraceApp>
    <Type>TRACE</Type>
    <AppId>123</AppId>
    <UserId>113197164949****</UserId>
    <CreateTime>1576599253000</CreateTime>
    <UpdateTime>1635700348000</UpdateTime>
    <Show>true</Show>
    <Pid>b590lhguqs@d8deedfa9bf****</Pid>
    <RegionId>cn-hangzhou</RegionId>
    <AppName>arms-k8s-demo</AppName>
    <Labels>[ "test", "123123123", "uat" ],</Labels>
</TraceApp>
 JSON format
```

`{`

```json
    "RequestId": "D80ADAAC-8C32-5479-BD14-C28CF832****",
    "TraceApp": {
        "Type": "TRACE",
        "AppId": 123,
        "UserId": "113197164949****",
        "CreateTime": 1576599253000,
        "UpdateTime": 1635700348000,
        "Show": true,
        "Pid": "b590lhguqs@d8deedfa9bf****",
        "RegionId": "cn-hangzhou",
        "AppName": "arms-k8s-demo",
        "Labels": "[ \"test\", \"123123123\", \"uat\" ],"
```

#### 5.3.5 GetStack

Queries the information of a method stack.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | GetStack | The operation that you want to perform. Set the value to GetStack. |
|---|---|---|---|---|
| Pid | String | Yes | eb4zdose6v@36 bab313a****** | The process identifier (PID) of the application. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
| RpcID | String | Yes | 1.1 | The parent-child and sibling relationship between spans. For example, span 1.1 is the parent of span 1.1.1, and span 1.1.2 and span 1.1.1 are siblings. |
| TraceID | String | Yes | 0a58006116414 70044457853** **** | The trace ID. You can log on to the ARMS console and choose application monitoring > Multi- dimensional Query. |

**Response parameters**

| Parameter | Type | Example | Details |
|---|---|---|---|
| RequestId | String | B34C3A43-A901- 5F94-9DAD- 758CE4****** | The request ID. |
| StackInfo | Array of StackInfo |   | The information of the method stack. |
| Api | String | /api/state | The operation that you want to perform. |
| Duration | Long | 1000 | The duration. Unit: milliseconds. |
| Exception | String | java.lang.NullPoint erException | The error message. |
| ExtInfo | Struct |   | The extended information about the vulnerability. |
| Info | String | input=254275&am p; | The content of the custom parameter. |
| Type | String | 41 | The type of the custom parameter. |

| Line | String | 34 | The number of rows in the method stack information. |
|---|---|---|---|
| RpcId | String | 1.1 | The parent-child and sibling relationship between spans. For example, span 1.1 is the parent of span 1.1.1, and span 1.1.2 and span 1.1.1 are siblings. |
| ServiceName | String | /com/test | The service name. |
| StartTime | Long | 1618382700761 | The timestamp when the method entry was called. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetStack &Pid=eb4zdose6v@36bab313a****** &RegionId=cn-hangzhou &RpcID=1.1 &TraceID=0a5800611641470044457853****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B34C3A43-A901-5F94-9DAD-758CE4******</RequestId> <StackInfo>
    <Line>34</Line>
    <ServiceName>/com/test</ServiceName>
    <RpcId>1.1</RpcId>
    <StartTime>1618382700761</StartTime>
    <Duration>1000</Duration>
    <Api>/api/state</Api>
    <Exception>java.lang.NullPointerException</Exception>
    <ExtInfo>
        <Type>41</Type>
        <Info>input=254275&amp;</Info>
    </ExtInfo>
</StackInfo>
 JSON format
```

`{`

```json
    "RequestId": "B34C3A43-A901-5F94-9DAD-758CE4******",
    "StackInfo": {
        "Line": 34,
        "ServiceName": "/com/test",
        "RpcId": 1.1,
        "StartTime": 1618382700761,
        "Duration": 1000,
        "Api": "/api/state",
        "Exception": "java.lang.NullPointerException",
        "ExtInfo": {
            "Type": 41,
            "Info": "input=254275&amp;"
```

#### 5.3.6 ListTraceApps

Queries all Application Monitoring tasks in a specified region.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListTraceApps | The operation that you want to perform. Set the value to ListTraceApps. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code that is returned for the request. Valid values: 2XX : Success 3XX : Redirect 4XX : Request Error 5XX : Server Error |
| Message | String | Internal error. Please try again. Contact the DingTalk service account if the issue persists after multiple retries. | The error message returned if the request parameters are invalid. |

| RequestId | String | 40B10E04-81E8- 4643-970D- F1B38F2E**** | The request ID. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true : The operation is successful. false : Operation failed |
| TraceApps | Array of TraceApp |   | The list of Application Monitoring tasks. |
| AppId | Long | 123 | The application ID. |
| AppName | String | test-app | The name of the application. |
| CreateTime | Long | 1529667762000 | The timestamp that indicates the time when the pod was created. |
| Labels | List | prod | The application tag. |
| Pid | String | a5f9bdeb-2627- 4dbe-9247-**** | The process identifier (PID) of the application. |
| RegionId | String | cn-hangzhou | The region ID of the resource. |
| Show | Boolean | true | Indicates whether the application is displayed in the Application Real-Time Monitoring Service (ARMS) console. Valid values: true : display false : not displayed Note If the advanced monitoring feature is not enabled in the EDAS console, the application is displayed as false . |
| Type | String | TRACE | The type of the monitoring task. Only the application monitoring type TRACE is supported. |
| UpdateTime | Long | 1529667762000 | The timestamp generated when the task information was updated. |

| UserId | String | 113197164949**** | The ID of the Resource Access Management (RAM) user that you use. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListTraceApps &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TraceApps>
    <Type>TRACE</Type>
    <AppId>123</AppId>
    <UserId>113197164949****</UserId>
    <CreateTime>1529667762000</CreateTime>
    <UpdateTime>1529667762000</UpdateTime>
    <Show>true</Show>
    <Pid>a5f9bdeb-2627-4dbe-9247-****</Pid>
    <RegionId>cn-hangzhou</RegionId>
    <AppName>test-app</AppName>
    <Labels>prod</Labels>
</TraceApps> <Message>Internal error. Please try again. Contact the DingTalk service account if the issue persists after multiple retries.</Message> <RequestId>40B10E04-81E8-4643-970D-F1B38F2E****</RequestId> <Code>200</Code> <Success>true</Success>
 JSON format
```

`{`

```json
    "TraceApps": {
        "Type": "TRACE",
        "AppId": 123,
        "UserId": "113197164949****",
        "CreateTime": 1529667762000,
        "UpdateTime": 1529667762000,
        "Show": true,
        "Pid": "a5f9bdeb-2627-4dbe-9247-****",
        "RegionId": "cn-hangzhou",
        "AppName": "test-app",
        "Labels": "prod"
```

`},`

```json
    "Message": "Internal error. Please try again. Contact the DingTalk service account
if the issue persists after multiple retries.",
    "RequestId": "40B10E04-81E8-4643-970D-F1B38F2E****",
    "Code": 200,
    "Success": true
```

#### 5.3.7 SearchTraceAppByName

Queries application monitoring jobs by application name.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SearchTraceApp ByName | The operation that you want to perform. Set the value to SearchTraceAppByName. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
| TraceAppName | String | Yes | test-app | The name of the application. |

**Response parameters**

| Parameter | Type | Example | Details |
|---|---|---|---|
| RequestId | String | F7781D4A-2818- 41E7-B7BB- 79D809E9**** | The request ID. |
| TraceApps | Array of TraceApp |   | The information about the application monitoring job. |
| AppId | Long | 123 | The application ID. |

| AppName | String | test-app | The name of the application. |
|---|---|---|---|
| CreateTime | Long | 1593486786000 | The timestamp that indicates the time when the pod was created. |
| Labels | List | prod | The application tag. |
| Pid | String | a5f9bdeb-2627- 4dbe-9247-**** | The process identifier (PID) of the application. |
| RegionId | String | cn-hangzhou | The region ID of the resource. |
| Show | Boolean | true | Indicates whether the application is displayed in the Application Real-Time Monitoring Service (ARMS) console. Valid values: true false: does not display the image. Note If the advanced monitoring feature is not enabled in the EDAS console, the application is displayed as false . |
| Type | String | TRACE | The type of the monitoring task. Only the application monitoring type TRACE is supported. |
| UpdateTime | Long | 1593486786000 | The timestamp generated when the task information was updated. |
| UserId | String | 113197164949**** | The ID of the Resource Access Management (RAM) user that you use. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SearchTraceAppByName &RegionId=cn-hangzhou &TraceAppName=test-app &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TraceApps>
    <Type>TRACE</Type>
    <AppId>123</AppId>
    <UserId>113197164949****</UserId>
    <CreateTime>1593486786000</CreateTime>
    <UpdateTime>1593486786000</UpdateTime>
    <Show>true</Show>
    <Pid>a5f9bdeb-2627-4dbe-9247-****</Pid>
    <RegionId>cn-hangzhou</RegionId>
    <AppName>test-app</AppName>
    <Labels>prod</Labels>
</TraceApps> <RequestId>F7781D4A-2818-41E7-B7BB-79D809E9****</RequestId>
 JSON format
```

`{`

```json
    "TraceApps": {
        "Type": "TRACE",
        "AppId": 123,
        "UserId": "113197164949****",
        "CreateTime": 1593486786000,
        "UpdateTime": 1593486786000,
        "Show": true,
        "Pid": "a5f9bdeb-2627-4dbe-9247-****",
        "RegionId": "cn-hangzhou",
        "AppName": "test-app",
        "Labels": "prod"
```

`},`

```json
    "RequestId": "F7781D4A-2818-41E7-B7BB-79D809E9****"
```

#### 5.3.8 SearchTraceAppByPage

Queries application monitoring jobs by page.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SearchTraceApp ByPage | The operation that you want to perform. Set the value to SearchTraceAppByPage. |
| PageNumber | Integer | Yes | 1 | Optional. The page number of the query result. If you do not specify this parameter, the default value is 1. |

| PageSize | Integer | Yes | 10 | Optional. The number of items on each page of the query result. If this parameter is not specified, the default value is 10. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
| TraceAppName | String | Yes | test-app | Optional. The name of the application. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageBean | Struct |   | The information returned on the current page. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| TotalCount | Integer | 3 | The total number of entries returned. |
| TraceApps | Array of TraceApp |   | The information about the application monitoring job. |
| AppId | Long | 123 | The application ID. |
| AppName | String | test-app | The name of the application. |
| CreateTime | Long | 1531291867000 | The timestamp that indicates the time when the pod was created. |
| Labels | List | prod | The application tag. |
| Pid | String | atc889zkcf@d8dee dfa9bf**** | The process identifier (PID) of the application. |
| RegionId | String | cn-hangzhou | The region ID of the resource. |

| Show | Boolean | true | Indicates whether the application is displayed in the Application Real-Time Monitoring Service (ARMS) console. Valid values: true false: does not display the image. Note If the advanced monitoring feature is not enabled in the EDAS console, the application is displayed as false . |
|---|---|---|---|
| Type | String | TRACE | The type of the monitoring task. Only the application monitoring type TRACE is supported. |
| UpdateTime | Long | 1531291867000 | The timestamp generated when the task information was updated. |
| UserId | String | 113197164949**** | The user ID. |
| RequestId | String | 4B446DF2-3DDD- 4B5B-8E3F- D5225120**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SearchTraceAppByPage &PageNumber=1 &PageSize=10 &RegionId=cn-hangzhou &TraceAppName=test-app &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PageBean>
    <TotalCount>3</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <TraceApps>
        <Type>TRACE</Type>
        <AppId>123</AppId>
        <UserId>113197164949****</UserId>
        <CreateTime>1531291867000</CreateTime>
        <UpdateTime>1531291867000</UpdateTime>
        <Show>true</Show>
        <Pid>atc889zkcf@d8deedfa9bf****</Pid>
        <RegionId>cn-hangzhou</RegionId>
        <AppName>test-app</AppName>
        <Labels>prod</Labels>
    </TraceApps>
</PageBean> <RequestId>4B446DF2-3DDD-4B5B-8E3F-D5225120****</RequestId>
 JSON format
```

`{`

```json
    "PageBean": {
        "TotalCount": 3,
        "PageSize": 10,
        "PageNumber": 1,
        "TraceApps": {
            "Type": "TRACE",
            "AppId": 123,
            "UserId": "113197164949****",
            "CreateTime": 1531291867000,
            "UpdateTime": 1531291867000,
            "Show": true,
            "Pid": "atc889zkcf@d8deedfa9bf****",
            "RegionId": "cn-hangzhou",
            "AppName": "test-app",
            "Labels": "prod"
```

`},`

```json
    "RequestId": "4B446DF2-3DDD-4B5B-8E3F-D5225120****"
```

#### 5.3.9 SearchTraces

Queries traces by time, application name, IP address, span name, and tag. A maximum of 100 data entries can be returned each time this operation is called. If you want to query full data, we recommend that you use **SearchTracesByPage**.

**Request parameters**

| 5 |   |   |   | > Document Version: 2025061 |
|---|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SearchTraces | The operation that you want to perform. Set the value to SearchTraces. |
| EndTime | Long | Yes | 1595210400000 | The end of the time range to query. Unit: milliseconds. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
| StartTime | Long | Yes | 1595174400000 | The beginning of the time range to query. Unit: milliseconds. |
| ServiceName | String | No | arms-k8s-demo- subcomponent | The name of the application. |
| OperationName | String | No | /demo/queryNot ExistDB/11 | The name of the span. |
| MinDuration | Long | No | 2 | The minimum amount of time consumed by traces. Unit: milliseconds. |
| Tag.N.Key | String | No | http.status code _ | The key of tag N. |
| Tag.N.Value | String | No | 200 | The tag value. |
| Reverse | Boolean | No | false | Specifies whether to sort the query results in chronological order or reverse chronological order. The default value is false . Valid values: true: reverse chronological order false: ascending order. |
| ServiceIp | String | No | 172.20.XX.X | The IP address that corresponds to the span. |
| ExclusionFilters. N.Key | String | No | http.status code _ | The key that is used to filter the query results. |
| ExclusionFilters. N.Value | String | No | 404 | The value of the key that is used to filter the query results. |

**Response parameters**

| Parameter | Type | Example | Details |
|---|---|---|---|
| RequestId | String | 4C518054-852F- 4023-ABC1- 4AF95FF7**** | The request ID. |
| TraceInfos | Array of TraceInfo |   | The details of the returned traces. |
| Duration | Long | 6 | The amount of time consumed by the trace. Unit: milliseconds. |
| OperationNam e | String | /demo/queryNotExi stDB/11 | The name of the span. |
| ServiceIp | String | 172.20.XX.X | The IP address of the server where the span resides. |
| ServiceName | String | arms-k8s-demo- subcomponent | The name of the application. |
| Timestamp | Long | 1595174436993 | The timestamp when the span was generated. |
| TraceID | String | ac1400a11595174 4369937024d**** | The trace ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SearchTraces &EndTime=1595210400000 &RegionId=cn-hangzhou &StartTime=1595174400000 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>4C518054-852F-4023-ABC1-4AF95FF7****</RequestId> <TraceInfos>
    <ServiceIp>172.20.XX.X</ServiceIp>
    <ServiceName>arms-k8s-demo-subcomponent</ServiceName>
    <OperationName>/demo/queryNotExistDB/11</OperationName>
    <TraceID>ac1400a115951744369937024d****</TraceID>
    <Duration>6</Duration>
    <Timestamp>1595174436993</Timestamp>
</TraceInfos>
 JSON format
```

`{`

```json
    "RequestId": "4C518054-852F-4023-ABC1-4AF95FF7****",
    "TraceInfos": {
        "ServiceIp": "172.20.XX.X",
        "ServiceName": "arms-k8s-demo-subcomponent",
        "OperationName": "/demo/queryNotExistDB/11",
        "TraceID": "ac1400a115951744369937024d****",
        "Duration": 6,
        "Timestamp": 1595174436993
```

#### 5.3.10 SearchTracesByPage

Queries all existing traces by time, application name, IP address, span name, or tag.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SearchTracesBy Page | The operation that you want to perform. Set the value to SearchTracesByPage. |
| EndTime | Long | Yes | 1595210400000 | The end of the time range to query. Unit: milliseconds. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
| StartTime | Long | Yes | 1595174400000 | The beginning of the time range to query. Unit: milliseconds. |
| ServiceName | String | No | arms-k8s-demo- subcomponent | The name of the application. |
| OperationName | String | No | /demo/queryNot ExistDB/11 | The name of the traced span. |
| MinDuration | Long | No | 2 | The minimum amount of time consumed by traces. Unit: milliseconds. |
| Reverse | Boolean | No | false | Specifies whether to sort the query results in chronological order or reverse chronological order. Default value: false. true: indicates reverse chronological order. false: indicates positive order. |

| ServiceIp | String | No | 172.20.XX.XX | The IP address of the host where the application resides. |
|---|---|---|---|---|
| ExclusionFilters. N.Key | String | No | http.status code _ | The key that is used to filter the query results. |
| ExclusionFilters. N.Value | String | No | 404 | The value of the key that is used to filter the query results. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. Maximum value: 100. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageBean | Struct |   | The returned data. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| Total | Integer | 10 | The total number of returned entries. |
| TraceInfos | Array of TraceInfo |   | The details of the returned traces. |
| Duration | Long | 679 | The amount of time consumed by the trace. Unit: milliseconds. |
| OperationNam e | String | /demo/queryExcept ion/12 | The name of the traced span. |
| ServiceIp | String | 172.20.XX.XX | The IP address of the host where the application resides. |
| ServiceName | String | arms-k8s-demo- subcomponent | The name of the application. |
| Timestamp | Long | 1595174436994 | The timestamp. |
| TraceID | String | ac1400a11595174 4369947025d**** | The trace ID. |

| RequestId | String | 4C518054-852F- 4023-ABC1- 4AF95FF7**** | The ID of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SearchTracesByPage &EndTime=1595210400000 &RegionId=cn-hangzhou &StartTime=1595174400000 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PageBean>
    <PageSize>5</PageSize>
    <PageNumber>1</PageNumber>
    <Total>10</Total>
    <TraceInfos>
        <ServiceIp>172.20.XX.XX</ServiceIp>
        <ServiceName>arms-k8s-demo-subcomponent</ServiceName>
        <OperationName>/demo/queryException/12</OperationName>
        <TraceID>ac1400a115951744369947025d****</TraceID>
        <Duration>679</Duration>
        <Timestamp>1595174436994</Timestamp>
    </TraceInfos>
</PageBean> <RequestId>4C518054-852F-4023-ABC1-4AF95FF7****</RequestId>
 JSON format
```

`{`

```json
    "PageBean": {
        "PageSize": 5,
        "PageNumber": 1,
        "Total": 10,
        "TraceInfos": {
            "ServiceIp": "172.20.XX.XX",
            "ServiceName": "arms-k8s-demo-subcomponent",
            "OperationName": "/demo/queryException/12",
            "TraceID": "ac1400a115951744369947025d****",
            "Duration": 679,
            "Timestamp": 1595174436994
```

`},`

```json
    "RequestId": "4C518054-852F-4023-ABC1-4AF95FF7****"
```

#### 5.3.11 QueryMetric

Queries a metric.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryMetric | The operation that you want to perform. Set the value to QueryMetric. |
| EndTime | Long | Yes | 1575622455686 | The end of the time range to query. Unit: milliseconds. |
| IntervalInSec | Integer | Yes | 60000 | The time interval between the data shards that you want to query. Unit: milliseconds. Minimum value: 60000. |
| Measures.N | RepeatL ist | Yes | count | The measurement data of the corresponding metric. For more information about query fields, see the supplementary description below. |
| Metric | String | Yes | appstat.incall | The name of the metric. For more information about supported metrics, see the supplementary description below. |
| StartTime | Long | Yes | 1575561600000 | The timestamp of the start time of the time range to query. The timestamp is accurate to milliseconds. |
| OrderBy | String | No | count | The field based on which you want to sort the returned entries. |
| Limit | Integer | No | 100 | The number of data records to return. The maximum value is 10000. |
| Filters.N.Key | String | No | pid | The key of the filter field. You must add the pid. |
| Filters.N.Value | String | No | xxx@74xxx | The value of the field that you want to use to filter the returned entries. |

| Dimensions.N | RepeatL ist | No | RT | The dimension that corresponds to the metric. For more information about query fields, see the supplementary description below. |
|---|---|---|---|---|
| Order | String | No | ASC | The order in which you want to sort the returned entries. Valid values: ASC: ascending order DESC: The entries are sorted in descending order. |
| RegionId | String | No | cn-beijing | The ID of the region. |
| ProxyUserId | String | No | testefgag12 | The ID of the proxy user. |
| ConsistencyData Key | String | No | - | Apsara Stack does not support this parameter. |
| ConsistencyQuer yStrategy | String | No | - | Apsara Stack does not support this parameter. |

**Application monitoring metrics that can be queried**

> **Note:** request parameters **Filters** must add `pid` and `regionId` conditions. If you know the specific query conditions, you should pass the values into the **Filters** parameters to limit the range of query results. If you do not know the specific query conditions, you can pass the dimensions in the following table to the **Dimensions** parameter to obtain a list of all possible values of the dimension.

| Metric | Description | Dimension | Measure |
|---|---|---|---|

| appstat.vm | A collection of common metrics that are shown in the JVM monitoring chart on the application details page. These metrics are related to GCs, heap memory, non- heap memory, and threads. | pid rootIp | GCs: youngGcCount: the number of GCs in the young generation oldGcCount: the number of full heap GCs (Full GCs) youngGcTime: the amount of time consumed to monitor GCs in the young generation oldGcTime: the amount of time consumed to monitor Full GCs youngGcCountInsta nt: the instantaneous value of the number of GCs in the young generation oldGcCountInstant: the instantaneous value of the number of Full GCs youngGcTimeInstant : the instantaneous value of the amount of time consumed to monitor GCs in the young generation oldGcTimeInstant: the instantaneous value of the amount of time consumed to monitor Full GCs |
|---|---|---|---|

| appstat.vm | A collection of common metrics that are shown in the JVM monitoring chart on the application details page. These metrics are related to GCs, heap memory, non- heap memory, and threads. | pid rootIp | Heap memory and non-heap memory: EdenSpace: the eden space in the young generation OldGen: the old generation survivorSpace: the survivor space in the young generation metaSpace: metaspace nonHeapCommitted: the non-heap memory nonHeapInit: the initial value of the non-heap memory nonHeapMax: the maximum value of the non-heap memory nonHeapUsed: the usage of the non- heap memory directUsed: the used size of direct buffer _ in external memory directCapacity: the total amount of direct buffer in the off-heap memory |
|---|---|---|---|

| appstat.vm | A collection of common metrics that are shown in the JVM monitoring chart on the application details page. These metrics are related to GCs, heap memory, non- heap memory, and threads. | pid rootIp | Threads: threadCount: the total number of threads threadNewCount: the number of new threads threadDeadlockCou nt: the number of deadlocked threads in the JVM threadRunnableCou nt: the number of runnable threads in the JVM threadTerminatedCo unt: the number of terminated threads threadTimedWaitCo unt: the number of threads in the timed waiting state _ threadWaitCount: the number of threads in the waiting state threadBlockedCount : the number of blocked threads |
|---|---|---|---|
| appstat.host | A collection of metrics for host monitoring. These metrics are related to instances, CPU, physical memory, disk, load, network traffic, and network packets. | pid rootIp | instanceCount: the number of instances |

| appstat.host | A collection of metrics for host monitoring. These metrics are related to instances, CPU, physical memory, disk, load, network traffic, and network packets. | pid rootIp | CPU: systemCpuIdle: the percentage of idle CPU in the last 5 seconds, which is not displayed in the ARMS console systemCpuSystem: the percentage of CPU occupied by the system in the last 5 seconds systemCpuUser: the percentage of CPU occupied by users in the last 5 seconds systemCpuIoWait: the percentage of CPU consumed for I/O waiting in the last 5 seconds |
|---|---|---|---|
| appstat.host | A collection of metrics for host monitoring. These metrics are related to instances, CPU, physical memory, disk, load, network traffic, and network packets. | pid rootIp | Physical memory: systemMemFree: current system free memory (KB) systemMemUsed: the used memory of the current system (KB) systemMemTotal: the total memory of the current system (KB), which is not displayed on the console page. systemMemBuffers: the amount of memory in the buffer cache systemMemCached: the amount of memory in the page cache |

| appstat.host | A collection of metrics for host monitoring. These metrics are related to instances, CPU, physical memory, disk, load, network traffic, and network packets. | pid rootIp | Disks: systemDiskFree: the size of free disk space in bytes systemDiskUsedRati o: the usage of the disk space SystemDiskTotal: the total size of disk space in bytes, which is not displayed in the ARMS console |
|---|---|---|---|
| appstat.host | A collection of metrics for host monitoring. These metrics are related to instances, CPU, physical memory, disk, load, network traffic, and network packets. | pid rootIp | systemLoad: the load |

| appstat.host | A collection of metrics for host monitoring. These metrics are related to instances, CPU, physical memory, disk, load, network traffic, and network packets. | pid rootIp | Network: systemNetInPackets : the average number of packets received over the network per second in the last 30 seconds systemNetOutPacke ts: the average number of packets sent over the network per second in the last 30 seconds systemNetInErrs: Average number of errors received over the network per second in the last 30 seconds systemNetOutErrs: the average number of errors sent over the network per second in the last 30 seconds systemNetInBytes: the average number of bytes received over the network per second in the last 30 seconds systemNetOutBytes: the average number of bytes sent over the network per second in the last 30 seconds |
|---|---|---|---|
| appstat.database | A collection of metrics for database calls. | pid rpcType: the type of the call endpoint: The database endpoint, which is localhost: 3306 destId: The database name is arms. | rt: the response time count: the number of requests. error: the number of errors. resultsize: This metric is available only when MySQL 5.x is used. slowcount: the number of slow calls. |

| appstat.incall | A collection of metrics related to application details. | pid rpcType rootIp rpc ppid | rt: the response time count: the number of requests. error: the number of errors exception: the number of exceptions errorrate: the error rate qps: the number of queries per second |
|---|---|---|---|
| appstat.exception | A collection of metrics related to exceptions. | pid rpc endpoint excepType excepInfo | rt: the response time count: the number of requests. error: the number of errors |
| appstat.sql | A collection of metrics related to slow SQL queries. | pid rpc endpoint sqlId | rt: the response time count: the number of requests. error: the number of errors slow: the number of slow calls. |
| appstat.mq.send | A collection of metrics related to message sending by using Message Queue | N/A | rt: the response time count: the number of requests. error: the number of errors delay: the latency in scheduling |
| appstat.mq.receive | A collection of metrics related to message receiving by using Message Queue | N/A | rt: the response time count: the number of requests. error: the number of errors delay: the latency in scheduling |
| appstat.schedulerx | A collection of metrics related to SchedulerX calls. | pid rpcType rootIp rpc | count: the number of requests |

| appstat.elasticsearch | A collection of metrics related to Elasticsearch calls. | rpc endpoint opType: the type of the operation such as index and search operations. This dimension is supported only when RestHighLevelClient is used Elasticsearch of RestHighLevelClient and RestLowLevelClient. | count: the number of requests |
|---|---|---|---|
| appstat.redis | A collection of metrics related to ApsaraDB for Redis calls. | pid rpcType endpoint opType rpc | count: the number of requests |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | String | { "RequestId": "E2373982-D8CD- 413D-B991- 8EB678C01B4F", "Data": "{\"data\": [{\"date\":1583686 800000,\"count\":0 ,\"rt\":0,\"rpc\":\"chi ldSpan3\"}} | The returned statistics. |
| RequestId | String | 1E2B6A4C-6B83- 4062-8B6F- AEEC1FC47DED | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=QueryMetric &EndTime=1575622455686 &IntervalInSec=60 &Measures.1=count &Metric=appstat.incall &StartTime=1575561600000 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>1E2B6A4C-6B83-4062-8B6F-AEEC1FC47DED</RequestId> <Data>{ "RequestId": "E2373982-D8CD-413D-B991-8EB678C01B4F", "Data": "{\"data\":[{\"dat e\":1583686800000,\"count\":0,\"rt\":0,\"rpc\":\"childSpan3\"}}</Data>
 JSON format
```

`{`

```json
    "RequestId": "1E2B6A4C-6B83-4062-8B6F-AEEC1FC47DED",
    "Data": "{ \"RequestId\": \"E2373982-D8CD-413D-B991-8EB678C01B4F\", \"Data\": \"{\\
\"data\\\": [{\\\"date\\\":1583686800000,\\\"count\\\":0,\\\"rt\\\":0,\\\"rpc\\\":\\\"childSpan3\\\"}
```

#### 5.3.12 DeleteTraceApp

Deletes an application based on a specified process identifier (PID) and application type.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteTraceApp | The operation that you want to perform. Set the value to DeleteTraceApp. |
| Pid | String | Yes | 9w0sc5gxxz@ed csd447c2f**** | The process identifier (PID) of the application. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
| Type | String | Yes | TRACE | The type of the application that you want to delete. You can specify only the application monitoring type TRACE. |
| AppId | String | No | 5406** | The ID of the application to be deleted. You can call the SearchTraceAppByName operation to query the ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Data | String | { "RequestId": "46355DD8-FC56- 40C5-BFC6- 269DE4F9****", "Data": " {\"code\":200,\"dat a\":\" {\\\"code\\\":200 ,\\ "data\\\":true ,\\ "errorCode \\"s\":\\\\\" The application is deleted, and \\\\\ "\" the application is deleted. true,\\\"traceId\\\":\\ \"0 bc0594d15954826 692915817e**** \\\\"}\", " errorCode\": " The application is deleted ", " message\": " The application is deleted ", " success\":true,\"tra ceId\":\" 0ab264691595482 669****} "\ | The response in JSON format, including the HTTP status code, error code, response message, and trace ID. |
|---|---|---|---|
| RequestId | String | 46355DD8-FC56- 40C5-BFC6- 269DE4F9**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteTraceApp &Pid=9w0sc5gxxz@edcsd447c2f**** &RegionId=cn-hangzhou &Type=TRACE &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>46355DD8-FC56-40C5-BFC6-269DE4F9****</RequestId> <Data>{ "RequestId": "46355DD8-FC56-40C5-BFC6-269DE4F9****", "Data": " {\"code\":200,\"data\":\"{\\\"code\\\":200,\\\"data\\\":true ,\\ "errorCode\\\":\\ "The application is deleted \\" successfully \\\",\\\"message \\ "true,\\\"traceId\\\":\\\"0 bc0594d15954826692915817e**** \\\\ "}\", "errorCode\": "The application is deleted", "m essage\": "The application is deleted", "success\":true,\"traceId\": "0ab2646915954826692568137d
```

**** /}"

```
 JSON format
```

`{`

```json
    "RequestId": "46355DD8-FC56-40C5-BFC6-269DE4F9****",
    "Data": "{ \"RequestId\": \"46355DD8-FC56-40C5-BFC6-269DE4F9****\", \"Data\": \"{\\
\"code\\\":200 ,\\ "data \\":\\\"{\\\\\\" code \\\\\\\\\ ":200 ,\\\\\\\\\" data \\\\":t rue ,\\\\\\\\" errorCode \\\\\\\\\ ":\\\\\\\ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \\\\\true,\\\"traceId\\\":\\\"0ab2646915954826692568137d****\\\"}\" }"
```

#### 5.3.13 GetArmsAgentDownLoadUrl

You can call the GetArmsAgentDownLoadUrl operation to obtain the download link of the agent package.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetArmsAgentD ownLoadUrl | The operation that you want to perform. Set the value to GetArmsAgentDownLoadUrl. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ArmsAgentDo wnloadUrl | String | http://arms.console .inter.env66.shugu ang.com/download /ArmsAgent.zip | The download link of the Agent installation package. |
| RequestId | String | 46355DD8-FC56- 40C5-BFC6- 269DE4F9**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetArmsAgentDownLoadUrl &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ArmsAgentDownloadUrl>http://arms.console.inter.env66.shuguang.com/download/ArmsAgent.zip ArmsAgentDownloadUrl> <RequestId>46355DD8-FC56-40C5-BFC6-269DE4F9****</RequestId>
```

```
 JSON format
```

`{`

```json
    "ArmsAgentDownloadUrl":
"http://arms.console.inter.env66.shuguang.com/download/ArmsAgent.zip",
    "RequestId": "46355DD8-FC56-40C5-BFC6-269DE4F9****"
```

#### 5.3.14 DescribeTraceLicenseKey

Queries the license key.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeTraceLi censeKey | The operation that you want to perform. Set the value to DescribeTraceLicenseKey. |
| RegionId | String | No | cn-hangzhou | Required. The ID of the region. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| LicenseKey | String | b590lhguqs@3a75 d95f218**** | The license key for the application. |
| RequestId | String | 29053944-6FE5- 4240-8927- 10095ECE**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeTraceLicenseKey &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>29053944-6FE5-4240-8927-10095ECE****</RequestId> <LicenseKey>b590lhguqs@3a75d95f218****</LicenseKey>
 JSON format
```

`{`

```json
    "RequestId": "29053944-6FE5-4240-8927-10095ECE****",
    "LicenseKey": "b590lhguqs@3a75d95f218****"
```

#### 5.3.15 DescribeTraceLocation

You can call the DescribeTraceLocation operation to query the region where the application resides.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeTraceLo cation | The operation that you want to perform. Set the value to DescribeTraceLocation. |
| RegionId | String | No | cn-hangzhou | The region ID of the resource. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RegionConfigs | Array of RegionConfig |   | The information about the specified region. |
| RegionNo | String | cn-hangzhou | The region ID of the resource. |
| Url | String | arms.console.inter. env66.shuguang.c om | The console link of the application. |
| RequestId | String | 46355DD8-FC56- 40C5-BFC6- 269DE4F9**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeTraceLocation &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>46355DD8-FC56-40C5-BFC6-269DE4F9****</RequestId> <RegionConfigs>
    <RegionNo>cn-hangzhou</RegionNo>
    <Url>arms.console.inter.env66.shuguang.com</Url>
</RegionConfigs>
 JSON format
```

`{`

```json
    "RequestId": "46355DD8-FC56-40C5-BFC6-269DE4F9****",
    "RegionConfigs": {
        "RegionNo": "cn-hangzhou",
        "Url": "arms.console.inter.env66.shuguang.com"
```

### 5.4 Alerting

#### 5.4.1 UpdateAlertRule

You can call the UpdateAlertRule operation to update an alert rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateAlertRule | The operation that you want to perform. Set the value to UpdateAlertRule. |
| AlertId | Long | Yes | 1234567 | The ID of the alert rule. You can call the SearchAlertRules operation to query the ID of the alert rule. The corresponding response parameter is Id. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
|   |   |   | [ { "contactGroupId s": "381", "alertType": 5, "alarmContext": { "subTitle": "", "content": "Alarm name: $Alarm name \nFilter condition: $Filter condition: $Filter \nAlarm time: $Alarm time |   |

| TemplageAlertC onfig | String | Yes | \nAlarm content: $Alarm content \nNote: The alarm is being continuously alerted before receiving the recovery email. We will remind you again in 24 hours! " }, "alertLevel": "WARN", "metricParam": { "appId": "70901", "pid": "atc889zkcf@d8 deedfa9bf****", "type": "TXN", "dimensions": [ { "type": "STATIC", "value": "\\\/hello test ap _ _ i address key ", _ " rpc" } ] }, "alertWay": [ "SMS", "MAIL", "DING ROBOT" _ ], "alertRule": { "rules": [ { "measure": "appstat.txn.rt", "alias": " ingress call response time ms ", _ "aggregates": "AVG", " valueValue ": " 1, "" CURRENT GTE" _ } ], "operator": "\|" }, "title": " Alarm template name ", "config": " {\"continuous\":f alse,\"dataRevisi on\":2,\"ownerId \":\"1234123412 34\"}", "notice": { "noticeStartTime ": 1480521600000 ": "startTime 1480521600000 , "endTime": 1480607940000 , "noticeEndTime" : 1480607940000 }, "status": "NON" } ] | The configurations of the alert template based on which you want to create an alert rule. The value must be a JSON string. |
|---|---|---|---|---|

| ContactGroupIds | String | No | [123, 234] | The ID of the alert contact group. |
|---|---|---|---|---|
| IsAutoStart | Boolean | No | true | Specifies whether to enable the alert rule after it is created. true: automatically starts the alert rule. false: does not automatically start the alert rule. This is the default value. |

**Supplementary note on parameter TemplageAlertConfig**

**Example and description of alert template JSON strings**

`[` `{`

```json
    "contactGroupIds": "381",                         // The ID of the alert contact gro
up. Multiple IDs are separated by commas (,). You can ignore this parameter in the aler t template configuration. The value is automatically generated when ARMS creates the al ert rule based on the alert template.
    "alertType": 5,                                // The alert type. Valid values: 4 and
5. A value of 4 indicates browser monitoring. A value of 5 indicates application monito
ring.
    "alarmContext": {                                // The template of the alert
notification.
      "subTitle": "",
      "content": "Alert name: $alert name\nFilter condition: $filter\nAlert time:
$alert time\nAlert content: $alert content\nNote: The alert remains being triggered unt il a reply email is received. The system will remind you 24 hours later."
```

`},`

```json
    "alertLevel": "WARN",                              // The alert severity. Valid value
s: FATAL, ERROR, and WARN.
    "metricParam": {
      "appId": "70901",                              // The ID of the associated
application. You can specify an arbitrary value in the alert template configuration. Th e actual value is automatically generated when ARMS creates the alert rule based on the alert template.
      "pid": "atc889zkcf@d8deedfa9bf****",            // The PID of the associated appli
cation. You can specify an arbitrary value in the alert template configuration. The act ual value is automatically generated when ARMS creates the alert rule based on the aler t template.
      "type": "TXN",                                   // The type of the alert metric. F
or more information, see the following section.
      "dimensions": [                                 // The information about the associ
ated dimension. For more information, see the following section.
```

`{`

```json
          "type": "STATIC",
          "value": "\/hello_test_api_address\/test1",
          "key": "rpc"
```

`]` `},`

```json
    "alertWay": [                                      // The notification method. Valid
values: SMS, MAIL, and DING_ROBOT.
      "SMS",
      "MAIL",
      "DING_ROBOT"
```

`],`

```json
    "alertRule": {
      "rules": [                                          // The conditions of the alert
rule.
```

`{`

```json
          "measure": "appstat.txn.rt",                     // The metric based on which
alerts are triggered. For more information, see the following section.
          "alias": "the response time of API calls in milliseconds",                 //
The display parameter of the alert metric. You do not need to set this parameter for an alert template.
          "aggregates": "AVG",                            // The aggregation logic of the
alert rule. Valid values: AVG, SUM, MIN, and MAX.
          "nValue": 1,                                    // The time range to query.
          "value": 1,                                     // The threshold of the conditi
on.
          "operator": "CURRENT_GTE"                       // The operation logic of the
condition. Valid values: CURRENT_GTE: greater than or equal to. CURRENT_LTE: less than or equal to. PREVIOUS_UP: the minute-to-minute increase percentage. PREVIOUS_DOWN: the minute-to-minute decrease percentage. HOH_UP: the increase percentage compared with the previous hour. HOH_DOWN: the decrease percentage compared with the previous hour. DOD_U P: the increase percentage compared with the last day. DOD_DOWN: the decrease percentag e compared with the last day.
```

`],`

```json
      "operator": "|"                                    // The logical operator between
conditions. Valid values: &: AND. |: OR.
```

`},`

```json
    "title": "Template alert name",                              // The alert name. An
alert rule name in the format of {title}-Application name is generated when ARMS create s the alert rule based on the alert template.
    "config": "{\"continuous\":false,\"dataRevision\":2,\"ownerId\":\"123412341234\"}",
// If the continuous parameter is set to true, ARMS sends alert notifications without i nterruption. If the continuous parameter is set to false, an alert silence period of 24 hours is enabled. The dataRevision parameter specifies the data revision policy to be u sed if no data is obtained or the data is null. Valid values: 0: overwrites the data by using the value 0. 1: overwrites the data by using the value 1. 2: overwrites the data by using the value null, which means that no alert is triggered if no data exists.
    "notice": { // The unix timestamp ms timestamp. The noticeStartTime and
noticeEndTime timestamps indicate the notification time range. The startTime and endTim e parameters indicate the effective time range of the alert. The timestamp is converted to a timestamp that indicates the current day. For example, the 1565964097071 timestamp corresponds to 2019-08-16 22:01:37.
      "noticeStartTime": 1480521600000,
      "startTime": 1480521600000,
      "endTime": 1480607940000,
      "noticeEndTime": 1480607940000
```

`},`

```json
    "status": "NON"                                        // The status of the alert rul
e. You can ignore this parameter in the alert template configuration. The value is auto
```

`e.`

```
ouca goet spaaete teaettepateco guato.
```

`e`

```
aue sauto matically generated when ARMS creates the alert rule based on the alert template.
```

`]`

**Description of Measure, Dimension, and metricParam.type in an alert template**

Each alarm belongs to a type and is controlled by **metricParam.type** fields. Each type of alert rules can use a dimension for the conditions. You can configure multiple alert rules (alertRule) for each type of alarm, and you can configure multiple data request metrics of this type for calculation for each **alertRule**. The **Dimensions.type** contains the following optional values:

| STATIC |   |
|---|---|
| ALL | : Tr |

`STATIC` : The **dimensions.value** is required to match this dimension value. `ALL` : Traverses all dimension values and determines the interface name in turn based on the metrics of all interface names of this interface. The interface name is reflected in the alarm content if the threshold is triggered. In this case, you do not need to specify a
**dimensions.value**.
`DISABLE` : aggregates all dimension values into one value (sum). In this case, you do not need to specify a **dimensions.value**.

**Alert Metric Value Enumeration**

Alert type (metricParam.type): txn Dimension (dimensions.key): rpc Metrics (alertRule.rules.measure): appstat.txn.rt: the response time of API calls (Unit: milliseconds) appstat.txn.count: the number of API calls appstat.txn.errcount: the number of API call errors Alert type (metricParam.type): txn_type Dimension (dimensions.key): rpcType Metrics (alertRule.rules.measure): appstat.incall.rt: the response time of API calls for the services that are provided by the application, in milliseconds appstat.incall.count: the number of API calls for the services that are provided by the application appstat.incall.error: the number of API call errors for the services that are provided by the application appstat.outcall.rt: the response time of API calls for the services on which the application depends, in milliseconds appstat.outcall.count: the number of API calls for the services on which the application depends appstat.outcall.error: the number of API call errors for the services on which the application depends Alert type (metricParam.type): DB Dimension (dimensions.key): endpoint Metrics (alertRule.rules.measure): appstat.database.rt: the response time of API calls for the database appstat.database.count: the number of API calls for the database appstat.database.errcount: the number of API call errors for the database Alert type (metricParam.type): jvm Dimension(dimensionskey):rootIp Dimension (dimensions.key): rootIp Metrics (alertRule.rules.measure): appstat.jvm.heap_used: the total memory space in the JVM heap (Unit: bytes) appstat.jvm.GcPsScavengeCount: the number of garbage collections (GCs) in JVM appstat.jvm.GcPsMarkSweepCount: the number of tag deletions in JVM appstat.jvm.GcG1OldGenCount: the number of Garbage-First (G1) GCs in the old generation appstat.jvm.GcG1YoungGenCount: the number of G1 GCs in the young generation appstat.jvm.gc.YoungGcCountInstant: the number of GCs in the young generation appstat.jvm.gc.OldGcCountInstant: the number of full heap GCs (Full GCs) in JVM appstat.jvm.gc.YoungGcTimeInstant: the time that is consumed for the GCs in the young generation (Unit: milliseconds) appstat.jvm.gc.OldGcTimeInstant: the time that is consumed for the Full GCs in JVM (Unit: milliseconds) appstat.jvm.ThreadCount: the total number of JVM threads appstat.jvm.non_heap_used: the used space of the non-heap JVM memory (Unit: bytes) appstat.jvm.non_heap_max: the maximum space of the non-heap JVM memory (Unit: bytes) appstat.jvm.non_heap_init: the initial space of the non-heap JVM memory (Unit: bytes) appstat.jvm.non_heap_committed: the submitted space of the non-heap JVM memory (Unit: bytes) Alert type (metricParam.type): host Dimension (dimensions.key): rootIp Metrics (alertRule.rules.measure): appstat.jvm.SystemCpuUser: the CPU usage of the host (Unit: percentage) appstat.jvm.SystemMemFree: the idle memory space of the host (Unit: bytes) appstat.jvm.SystemDiskFree: the idle disk space of the host (Unit: bytes) appstat.jvm.SystemNetInErrs: the number of error messages that are received by the host appstat.jvm.SystemNetOutErrs: the number of error messages that are sent by the host appstat.jvm.SystemLoad: the system load of the host Alert type (metricParam.type): exception Dimension (dimensions.key): rpc Metrics (alertRule.rules.measure): appstat.exception.rt: the response time of abnormal API calls for the application (Unit: milliseconds) appstat.exception.count: the number of abnormal API calls for the application

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AlertId | Long | 1234567 | The ID of the alert rule. |
| Data | String | - | The information that is returned. |

| RequestId | String | 6A9AEA84-7186- 4D8D-B498- 4585C6A2**** | The ID of the alert rule. |
|---|---|---|---|

**Examples**

Sample requests

```json
http(s)://[Endpoint]/?Action=UpdateAlertRule &AlertId=1234567 &RegionId=cn-hangzhou &TemplageAlertConfig=[ { "contactGroupIds": "381", "alertType": 5, "alarmContext": { "s ubTitle": "", "content": "Alarm name: $Alarm name \nFilter condition: $Filter \nAlarm t ime: $Alarm time \nAlarm content: $Alarm content \nNote: Before the alarm received the recovery email, the alarm is ongoing and will remind you again after 24 hours! " }, "al ertLevel": "WARN", "metricParam": { "appId": "70901", "pid": "atc889zkcf@d8deedfa9bf****", "type": "TXN", "dimensions": [ { "type": "STATIC", "value ": "\\\/hello_test_api_address key ", " rpc" } ] }, "alertWay": [ "SMS", "MAIL", "DING_ ROBOT" ], "alertRule": { "rules": [ { "measure": "appstat.txn.rt", "alias": " ingress c all response time_ms ", "aggregates": "AVG", " valueValue ": " 1, "" CURRENT_GTE" } ], "operator": "|" }, "title": " Alarm template name ", "config": " {\"continuous\":false,\"dataRevision\":2,\"ownerId\":\"123412341234\"}", "notice": { "n oticeStartTime": 1480521600000": "startTime 1480521600000, "endTime": 1480607940000, "n oticeEndTime": 1480607940000 }, "status": "NON" } ] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AlertId>1234567</AlertId> <RequestId>6A9AEA84-7186-4D8D-B498-4585C6A2****</RequestId> <Data>-</Data>
 JSON format
```

`{`

```json
    "AlertId": 1234567,
    "RequestId": "6A9AEA84-7186-4D8D-B498-4585C6A2****",
    "Data": "-"
```

#### 5.4.2 DeleteAlertRules

Deletes alert rules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DeleteAlertRules | The operation that you want to perform. Set the value to DeleteAlertRules. |
|---|---|---|---|---|
| AlertIds | String | Yes | [123, 234] | The IDs of the alert rules that you want to delete. The format is JSONArray. Example:[123, 234]. You can call the SearchAlertRules operation to obtain the ID of the alert rule. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| IsSuccess | Boolean | true | Indicates whether the alert rule was deleted. true: The task is deleted. false: The synthetic monitoring task failed to be deleted. |
| RequestId | String | C21AB7CF-B7AF- 410F-BD61- 82D1567F**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteAlertRules &AlertIds=[123, 234] &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>C21AB7CF-B7AF-410F-BD61-82D1567F****</RequestId>
 JSON format
```

`{`

```json
    "IsSuccess": true,
    "RequestId": "C21AB7CF-B7AF-410F-BD61-82D1567F****"
```

#### 5.4.3 SearchAlertRules

Queries alert rules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SearchAlertRule s | The operation that you want to perform. Set the value to SearchAlertRules. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the alert data. |
| Title | String | No | AlertRuleTitle | The name of the alert rule. |
| Type | String | No | 5 | The type of the alert rule. Valid values: 1: custom monitoring and alert rules based on drill-down datasets. 3: custom monitoring and alert rules based on tiled datasets. 5: application monitoring alert rules. 100: System alarm. 102: An emergency alert is applied by default. |
| CurrentPage | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 10. |
| Pid | String | No | atc889zkcf@d8d eedfa9bf**** | The process identifier (PID) of the application that is associated with the alert rule. |
| AppType | String | No | TRACE | The type of the application that is associated with the alert rule. Valid values: TRACE ALL: all alert rules _ TRACE: application monitoring alert rules XTRACE: Tracing Analysis alert rules |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageBean | Struct |   | The returned struct. |
| AlertRules | Array of AlertRuleEntity |   | The details of the alert rules. |
| AlarmContext | Struct |   | The format of the alert notification. |
| AlarmContent SubTitle | String | TestSubTitle | The sub-title of the alert notification content. |
| AlarmContent Template | String | Alert name: $alert name\nFilter condition: $filter\nAlert time: $alert time\nAlert content: $alert content\nNote: The alert is continuously triggered until a reply email is received. The system will remind you 24 hours later. | The template of the alert notification. |
| Content | String | Alert name: $alert name\nFilter condition: $filter\nAlert time: $alert time\nAlert content: $alert content\nNote: The alert is continuously triggered until a reply email is received. The system will remind you 24 hours later. | The content of the alert notification. |
| SubTitle | String | test | The sub-title of the alert notification. |
| AlertLevel | String | WARN | The alert notification level. Valid value: WARN. |
| AlertRule | Struct |   | The conditions of alert rules. Multiple conditions are separated by the AND or OR logical operators. |
| Operator | String | \| | The logical operator between conditions. Valid values: & indicates AND logic. \| indicates OR logic. |

| Rules | Array of Rule |   | The condition of the alert rule. |
|---|---|---|---|
| Aggregates | String | AVG | The aggregation logic of the alert rule. Valid values: AVG: average per minute SUM: sum values per minute MAX: maximum value per minute MIN: minimum value per minute |
| Alias | String | response time ms _ | The display text of the alert metric. |
| Measure | String | appstat.jvm.Syste mDiskFree | The metric based on which alerts are triggered. For more information, see the following supplement. |
| NValue | Integer | 5 | The time range when data is requested. Unit: minutes. For example, the value 5 indicates that the alert rule applies to the data in the last 5 minutes. |
| Operator | String | CURRENT GTE _ | The operation logic of the condition. Valid values: CURRENT GTE: greater than or equal to _ CURRENT LTE: less than or equal to _ PREVIOUS UP: increase in percentage _ compared with the previous period PREVIOUS DOWN: decrease in _ percentage compared with the previous period HOH UP: increase in percentage _ compared with the same period in the previous hour HOH DOWN: decrease in percentage _ compared with the same period in the previous hour DOD UP: increase in percentage _ compared with the same period in the previous day DOD DOWN: decrease in percentage _ compared with the same period in the previous day |
| Value | Float | 30 | The threshold of the condition. |
| AlertTitle | String | TestAlertRule | The name of the alert rule. |

| AlertType | Integer | 5 | The type of the alert rule. Valid values: 1: custom monitoring and alert rules based on drill-down datasets. 3: custom monitoring and alert rules based on tiled datasets. 5: application monitoring alert rules. 100: System alarm. 102: An emergency alert is applied by default. |
|---|---|---|---|
| AlertVersion | Integer | 1 | The version of the alert rule. Default value: 1. |
| AlertWay | List | MAIL | The notification method of the alerts. Valid values: SMS MAIL: email DING ROBOT: DingTalk robot _ WEBHOOK: webhook |
| AlertWays | List | ["MAIL", "SMS", "DING ROBOT"] _ | The notification method of the alerts. Valid values: SMS MAIL: email DING ROBOT: DingTalk robot _ WEBHOOK: webhook |
| Config | String | {\"continuous\":tru e,\"dataRevision\": 2} | The configuration items of the alert rule. The value is a JSON string. continuous values include: true: alerts are sent every minute. false: turns on the alert silence period switch. dataRevision indicates the data revision policy when no data is obtained or the data is null, including: 0: zero fill policy. 1: Complements a policy. 2: null is added (null is added by default). No data is processed and no alarm event is generated when no data is found. |
| ContactGroupI dList | String | 381*,572* | The ID of the contact group. Multiple IDs are separated by commas (,). |

| ContactGroupI ds | String | [123, 234] | The IDs of the alert contact groups. The value must be a JSON array. |
|---|---|---|---|
| CreateTime | Long | 1579508519683 | The timestamp when the alert rule was created. |
| Id | Long | 123 | The ID of the alert rule. |
| MetricParam | Struct |   | The information about the application that is associated with the alert rule. |
| AppGroupId | String | DEFAULT | The ID of the application sub group associated with the alert. |
| AppId | String | 123 | The auto-increment ID of the Application Real-Time Monitoring Service (ARMS) application. You can ignore this ID. |
| Dimensions | Array of Dimension |   | The dimensions in the condition. |
| Key | String | rootIp | The key of the dimension. Valid values: rpc: interface name rpcType: the type of the API call, such as HTTP and DUBBO. endpoint: the name of the database. rootIp: the IP address of the machine. |
| Type | String | DISABLED | The type of the dimension. Valid values: STATIC: You must specify dimensions.value to match the value of this dimension. ALL: traverses all dimension values and determines which interface triggers the alarm based on the metrics of all interface names. The interface name is reflected in the alarm content. In this case, you do not need to specify dimensions.value. DISABLE: aggregates all dimension values into one value (sum). In this case, you do not need to specify dimensions.value. |
| Value | String | "127.0.XX.XX" | The value of the dimension. |
| Pid | String | 9870ca99-8105- 4da7-a3a4- d72dd1b1**** | The PID of the application that is associated with the alert rule. |

| Type | String | DB | The type of the metric. txn: the number of application monitoring calls txn type: application monitoring call _ type statistics db: database metric jvm:JVM monitoring host: host monitoring exception: abnormal interface call |
|---|---|---|---|
| Notice | Struct |   | The time ranges when the alert rule takes effect and when alert notifications are sent. |
| EndTime | Long | 1480607940000 | The end of the time range when the alert rule takes effect within 24 hours per day. This value is a UNIX timestamp. The year, month, and day that are indicated by the timestamp do not take effect. Only the hour, minute, and second take effect. |
| NoticeEndTim e | Long | 1480607940000 | The end of the time range when alert notifications are sent based on the alert rule within 24 hours per day. This value is a UNIX timestamp. The year, month, and day that are indicated by the timestamp are not displayed in this value. Only the hour, minute, and second are displayed. |
| NoticeStartTim e | Long | 1480521600000 | The beginning of the time range when alert notifications are sent based on the alert rule within 24 hours per day. This value is a UNIX timestamp. The year, month, and day that are indicated by the timestamp are not displayed in this value. Only the hour, minute, and second are displayed. |
| StartTime | Long | 1480521600000 | The beginning of the time range when the alert rule takes effect within 24 hours per day. This value is a UNIX timestamp. The year, month, and day that are indicated by the timestamp are not displayed in this value. Only the hour, minute, and second are displayed. |
| RegionId | String | cn-hangzhou | The ID of the region to which the alert rule belongs. |

| Status | String | RUNNING | The status of the alert rule. RUNNING indicates running, STOPPED indicates stopped. |
|---|---|---|---|
| TaskId | Long | 123 | The ID of the ARMS task that is associated with the alert rule. |
| TaskStatus | String | "" | The status of the task. It is an internal parameter. |
| Title | String | AlertTest | The alert name. |
| UpdateTime | Long | 1480521600000 | The timestamp when the alert rule was updated. |
| UserId | String | 113197164949**** | The ID of the user to which the alert rule belongs. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries to return on each page. |
| TotalCount | Integer | 13 | The total number of entries returned. |
| RequestId | String | 34ED024E-9E31- 434A-9E4E- D9D15C3**** | The request ID. |

|   | RUNNING |
|---|---|
| STOPPED |   |

**Alert metrics**

Alert type (metricParam.type): txn Dimension (dimensions.key): rpc Metrics (alertRule.rules.measure): appstat.txn.rt: the response time of API calls (Unit: milliseconds) appstat.txn.count: the number of API calls appstat.txn.errcount: the number of API call errors Alert type (metricParam.type): txn_type Dimension (dimensions.key): rpcType Metrics (alertRule.rules.measure): appstat.inbound.rt: the response time of API calls for services that are provided by the application (Unit: milliseconds) appstat.inbound.count: the number of API calls for services that are provided by the application appstat.inbound.error: the number of API call errors for services that are provided by the application appstat.outbound.rt: the response time of API calls for services on which the application depends (Unit: milliseconds) appstat.outbound.count: the number of API calls for services on which the application depends appstat.outbound.error: the number of API call errors for services on which the application depends Alert type (metricParam.type): db Dimension (dimensions.key): endpoint Metrics (alertRule.rules.measure): appstat.database.rt: the response time of API calls for the database appstat.database.count: the number of API calls for the database appstat.database.errcount: the number of API call errors for the database Alert type (metricParam.type): jvm Dimension (dimensions.key): rootIp Metrics (alertRule.rules.measure): appstat.jvm.heap_used: the total memory space in the JVM heap (Unit: bytes) appstat.jvm.GcPsScavengeCount: the number of garbage collections (GCs) in JVM appstat.jvm.GcPsMarkSweepCount: the number of tag deletions in JVM appstat.jvm.GcG1OldGenCount: the number of Garbage-First (G1) GCs in the old generation appstat.jvm.GcG1YoungGenCount: the number of G1 GCs in the young generation appstat.jvm.gc.YoungGcCountInstant: the number of GCs in the young generation appstat.jvm.gc.OldGcCountInstant: the number of full heap GCs (Full GCs) in JVM appstat.jvm.gc.YoungGcTimeInstant: the time that is consumed for the GCs in the young generation (Unit: milliseconds) appstat.jvm.gc.OldGcTimeInstant: the time that is consumed for the Full GCs in JVM (Unit: milliseconds) appstat.jvm.ThreadCount: the total number of JVM threads appstat.jvm.non_heap_used: the used space of the non-heap JVM memory (Unit: bytes) appstat.jvm.non_heap_max: the maximum space of the non-heap JVM memory (Unit: bytes) appstat.jvm.non_heap_init: the initial space of the non-heap JVM memory (Unit: bytes) appstat.jvm.non_heap_committed: the submitted space of the non-heap JVM memory (Unit: bytes) Alert type (metricParam.type): host Dimension (dimensions.key): rootIp Metrics (alertRule.rules.measure): appstat.jvm.SystemCpuUser: the CPU usage of the host (Unit: percentage) appstat.jvm.SystemMemFree: the idle memory space of the host (Unit: bytes) appstat.jvm.SystemDiskFree: the idle disk space of the host (Unit: bytes) appstat.jvm.SystemNetInErrs: the number of error messages that are received by the host appstat.jvm.SystemNetOutErrs: the number of error messages that are sent by the host appstat.jvm.SystemLoad: the system load of the host Alert type (metricParam.type): exception Dimension (dimensions.key): rpc Metrics (alertRule.rules.measure): appstat.exception.rt: the response time of abnormal API calls for the application (Unit: milliseconds) appstat.exception.count: the number of abnormal API calls for the application

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SearchAlertRules &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PageBean>
    <TotalCount>13</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <AlertRules>
        <Status>RUNNING</Status>
        <TaskId>123</TaskId>
        <AlertVersion>1</AlertVersion>
        <ContactGroupIds>[123, 234]</ContactGroupIds>
        <Config>{\"continuous\":true,\"dataRevision\":2}</Config>
        <CreateTime>1579508519683</CreateTime>
        <Title>AlertTest</Title>
        <TaskStatus>""</TaskStatus>
        <AlertType>5</AlertType>
        <ContactGroupIdList>381*,572*</ContactGroupIdList>
        <UserId>113197164949****</UserId>
        <UpdateTime>1480521600000</UpdateTime>
        <AlertTitle>TestAlertRule</AlertTitle>
        <AlertLevel>WARN</AlertLevel>
        <RegionId>cn-hangzhou</RegionId>
        <Id>123</Id>
        <AlertWays>["MAIL", "SMS", "DING_ROBOT"]</AlertWays>
        <AlertWay>MAIL</AlertWay>
        <AlarmContext>
            <AlarmContentTemplate>Alert name: $Alert name\nFilter condition:
```

```xml
$Filter\nAlert time: $Alert time\nAlert content: $Alert content\nNote: The alert persis ts until a reply email is received. The system will remind you again in 24 hours. </Ala rmContentTemplate>
            <AlarmContentSubTitle>TestSubTitle</AlarmContentSubTitle>
            <Content>Alert name: $Alert name\nFilter condition: $Filter\nAlert time:
$Alert time\nAlert content: $Alert content\nNote: The alert persists until a reply emai l is received. The system will remind you again in 24 hours. </Content>
            <SubTitle>test</SubTitle>
        </AlarmContext>
        <AlertRule>
            <Operator>|</Operator>
            <Rules>
                <Operator>CURRENT_GTE</Operator>
                <NValue>5</NValue>
                <Aggregates>AVG</Aggregates>
                <Alias>response time_ms</Alias>
                <Value>30</Value>
                <Measure>appstat.jvm.SystemDiskFree</Measure>
            </Rules>
        </AlertRule>
        <MetricParam>
            <Type>DB</Type>
            <AppId>123</AppId>
            <AppGroupId>DEFAULT</AppGroupId>
            <Pid>9870ca99-8105-4da7-a3a4-d72dd1b1****</Pid>
            <Dimensions>
                <Type>DISABLED</Type>
                <Value>"127.0.XX.XX"</Value>
                <Key>rootIp</Key>
            </Dimensions>
        </MetricParam>
        <Notice>
            <EndTime>1480607940000</EndTime>
            <NoticeStartTime>1480521600000</NoticeStartTime>
            <StartTime>1480521600000</StartTime>
            <NoticeEndTime>1480607940000</NoticeEndTime>
        </Notice>
    </AlertRules>
</PageBean> <RequestId>34ED024E-9E31-434A-9E4E-D9D15C3****</RequestId>
 JSON format
```

`{`

```json
    "PageBean": {
        "TotalCount": 13,
        "PageSize": 10,
        "PageNumber": 1,
        "AlertRules": {
            "Status": "RUNNING",
            "TaskId": 123,
            "AlertVersion": 1,
            "ContactGroupIds": "[123, 234]",
            "Config": "{\\\"continuous\\\":true,\\\"dataRevision\\\":2}",
```

```json
            "CreateTime": 1579508519683,
            "Title": "AlertTest",
            "TaskStatus": "\"\"",
            "AlertType": 5,
            "ContactGroupIdList": "381*,572*",
            "UserId": "113197164949****",
            "UpdateTime": 1480521600000,
            "AlertTitle": "TestAlertRule",
            "AlertLevel": "WARN",
            "RegionId": "cn-hangzhou",
            "Id": 123,
            "AlertWays": "[\"MAIL\", \"SMS\", \"DING_ROBOT\"]",
            "AlertWay": "MAIL",
            "AlarmContext": {
                "AlarmContentTemplate": "Alert name: $Alert name\nFilter condition: $Fil
ter\nAlert time: $Alert time\nAlert content: $Alert content\nNote: The alert persists u ntil a reply email is received. The system will remind you again in 24 hours."
                "AlarmContentSubTitle": "TestSubTitle",
                "Content": "Alert name: $Alert name \\nFilter condition: $Filter \\nAler
t time: $Alert time \\nAlert content: $Alert content \\nNote: The alert is ongoing befo re you receive a recovery email. You will be reminded again after 24 hours! ",
                "SubTitle": "test"
```

`},`

```json
            "AlertRule": {
                "Operator": "|",
                "Rules": {
                    "Operator": "CURRENT_GTE",
                    "NValue": 5,
                    "Aggregates": "AVG",
                    "Alias": "response time_ms",
                    "Value": 30,
                    "Measure": "appstat.jvm.SystemDiskFree"
```

`},`

```json
            "MetricParam": {
                "Type": "DB",
                "AppId": 123,
                "AppGroupId": "DEFAULT",
                "Pid": "9870ca99-8105-4da7-a3a4-d72dd1b1****",
                "Dimensions": {
                    "Type": "DISABLED",
                    "Value": "\"127.0.XX.XX\"",
                    "Key": "rootIp"
```

`},`

```json
            "Notice": {
                "EndTime": 1480607940000,
                "NoticeStartTime": 1480521600000,
                "StartTime": 1480521600000,
                "NoticeEndTime": 1480607940000
```

`},`

```json
    "RequestId": "34ED024E-9E31-434A-9E4E-D9D15C3****"
```

#### 5.4.4 CreateAlertContact

Creates an alert contact.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateAlertCont act | The operation that you want to perform. Set the value to CreateAlertContact. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
| ContactName | String | Yes | JohnDoe | Required. The name of the alert contact. |
| PhoneNum | String | Yes | 1381111**** | The mobile number of the alert contact. At least one of PhoneNum, Email, and DingRobotWebhookUrl must be filled in. |
| Email | String | Yes | someone@exam ple.com | The email address of the alert contact. At least one of PhoneNum, Email, and DingRobotWebhookUrl must be filled in. |
| DingRobotWebh ookUrl | String | Yes | https://oapi.ding talk.com/robot/s end? access token=9 _ 1f2f6**** | The webhook URL of the DingTalk chatbot. At least one of PhoneNum, Email, and DingRobotWebhookUrl must be filled in. Note In the DingTalk Robot Security Settings section, set the Custom keyword parameter to Alarm. |
| SystemNoc | Boolean | No | true | Indicates whether the alert contact receives system notifications. Valid values: true: receives system notifications. false: does not receive system notifications. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| ContactId | String | 12345 | The ID of the alert contact. |
|---|---|---|---|
| RequestId | String | E9C9DA3D-10FE- 472E-9EEF- 2D0A3E41**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateAlertContact &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>E9C9DA3D-10FE-472E-9EEF-2D0A3E41****</RequestId> <ContactId>12345</ContactId>
 JSON format
```

`{`

```json
    "RequestId": "E9C9DA3D-10FE-472E-9EEF-2D0A3E41****",
    "ContactId": 12345
```

#### 5.4.5 DeleteAlertContact

Deletes an alert contact.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAlertCont act | The operation that you want to perform. Set the value to DeleteAlertContact. |
| ContactId | Long | Yes | 123 | The ID of the alert contact to be deleted. You can call the SearchAlertContact interface to query the contact ID. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| IsSuccess | Boolean | true | Indicates whether the contact was deleted. true: The shipper is deleted. false: The shipper fails to be deleted. |
| RequestId | String | 78901766-3806- 4E96-8E47- CFEF59E4**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteAlertContact &ContactId=123 &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>78901766-3806-4E96-8E47-CFEF59E4****</RequestId>
 JSON format
```

`{`

```json
    "IsSuccess": true,
    "RequestId": "78901766-3806-4E96-8E47-CFEF59E4****"
```

#### 5.4.6 UpdateAlertContact

Updates an alert contact.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateAlertCont act | The operation that you want to perform. Set the value to UpdateAlertContact. |

| ContactId | Long | Yes | 123 | The ID of the alert contact to be updated. You can call the SearchAlertContact operation to query the ID. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
| ContactName | String | Yes | John Doe | Required. Change the name of the alert contact to this name. |
| PhoneNum | String | Yes | 1381111**** | The new mobile phone number of the alert contact. You must specify at least one of the following parameters: PhoneNum, Email, and DingRobotWebhookUrl. Note If you do not specify this parameter, the original mobile phone number of the alert contact is deleted. If you specify this parameter, the original mobile phone number of the alert contact is updated. |
| Email | String | Yes | someone@exam ple.com | The new email address of the alert contact. You must specify at least one of the following parameters: PhoneNum, Email, and DingRobotWebhookUrl. Note If you do not specify this parameter, the original mobile phone number of the alert contact is deleted. If you specify this parameter, the original mobile phone number of the alert contact is updated. |
| DingRobotWebh ookUrl | String | Yes | https://oapi.ding talk.com/robot/s end? access token=9 _ 1f2f6**** | Change the DingTalk robot webhook URL of the alert contact to this value. You must specify at least one of the following parameters: PhoneNum, Email, and DingRobotWebhookUrl. Note If you do not specify this parameter, the original mobile phone number of the alert contact is deleted. If you specify this parameter, the original mobile phone number of the alert contact is updated. |

| SystemNoc | Boolean | No | true | Indicates whether the alert contact receives system notifications. Valid values: true: receives system notifications. false: does not receive system notifications. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| IsSuccess | Boolean | true | Indicates whether the update was successful. Valid values: true: The alert contact was updated. false: The update failed. |
| RequestId | String | 1A474FF8-7861- 4D00-81B5- 5BC3DA4E**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateAlertContact &ContactId=123 &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>1A474FF8-7861-4D00-81B5-5BC3DA4E****</RequestId>
 JSON format
```

`{`

```json
    "IsSuccess": true,
    "RequestId": "1A474FF8-7861-4D00-81B5-5BC3DA4E****"
```

#### 5.4.7 SearchAlertContact

Queries alert contacts.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | SearchAlertCont act | The operation that you want to perform. Set the value to SearchAlertContact. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
| ContactName | String | No | John Doe | The name of the alert contact. |
| Phone | String | No | 1381111***** | The mobile number of the alert contact. |
| Email | String | No | someone@exam ple.com | The email address of the alert contact. |
| CurrentPage | String | No | 1 | The number of the page to return. |
| PageSize | String | No | 20 | The number of entries to return on each page. |
| ContactIds | String | No | [12345] | The ID of the alert contact. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageBean | Struct |   | The returned struct. |
| Contacts | Array of Contact |   | The information about the alert contacts. |
| ContactId | Long | 123 | The ID of the contact. |
| ContactName | String | John Doe | The name of the alert contact. |
| CreateTime | Long | 1572349025000 | The timestamp when the alert contact was created. |
| DingRobot | String | https://oapi.dingtal k.com/robot/send? access token=91f2 _ f6**** | The webhook URL of the DingTalk chatbot. |
| Email | String | someone@exampl e.com | The email address of the alert contact. |

| Phone | String | 13197164949**** | The user ID. |
|---|---|---|---|
| SystemNoc | Boolean | false | Indicates whether the alert contact receives system notifications. Valid values: true: receives system notifications. false: does not receive system notifications. |
| UpdateTime | Long | 1580258717000 | The timestamp when the alert contact was updated. |
| UserId | String | 1131971649*** | The user ID. |
| Webhook | String | {\"body\":\"{ \\\"msg type\\\": _ \\\"text\\\", \\\"content\\\": { \\\"text\\\": \\\"$content\\\" } }\",\"header\": {\"Arms-Content- Type\":\"json\"},\" method\":\"post\",\ "params\": {},\"url\":\"https://* **",\"userId\":\"113 1971649***\"}", | The information about the webhook. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 23 | The total number of returned entries. |
| RequestId | String | 21E85B16-75A6- 429A-9F65- 8AAC9A54**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SearchAlertContact &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PageBean>
    <TotalCount>23</TotalCount>
    <PageSize>20</PageSize>
    <PageNumber>1</PageNumber>
    <Contacts>
        <Email>someone@example.com</Email>
        <UserId>1131971649***</UserId>
        <Phone>13197164949****</Phone>
        <CreateTime>1572349025000</CreateTime>
        <UpdateTime>1580258717000</UpdateTime>
        <Webhook>{\"body\":\"{ \\\"msg_type\\\": \\\"text\\\", \\\"content\\\": {
\\\"text\\\": \\\"$content\\\" } }\",\"header\":{\"Arms-Content- Type\":\"json\"},\"method\":\"post\",\"params\": {},\"url\":\"https://***",\"userId\":\"1131971649***\"}",</Webhook>
        <ContactId>123</ContactId>
        <DingRobot>https://oapi.dingtalk.com/robot/send?access_token=91f2f6****
</DingRobot>
        <SystemNoc>false</SystemNoc>
        <ContactName>John Doe</ContactName>
    </Contacts>
</PageBean> <RequestId>21E85B16-75A6-429A-9F65-8AAC9A54****</RequestId>
 JSON format
```

`{`

```json
    "PageBean": {
        "TotalCount": 23,
        "PageSize": 20,
        "PageNumber": 1,
        "Contacts": {
            "Email": "someone@example.com",
            "UserId": "1131971649***",
            "Phone": "13197164949****",
            "CreateTime": 1572349025000,
            "UpdateTime": 1580258717000,
            "Webhook": "{\\\"body\\\":\\\"{ \\\\\\\"msg_type\\\\\\\": \\\\\\\"text\\\\\\
\", \\\\\\\"content\\\\\\\": { \\\\\\\"text\\\\\\\": \\\\\\\"$content\\\\\\\" } }\\\",\ \\"header\\\":{\\\"Arms-Content- Type\\\":\\\"json\\\"},\\\"method\\\":\\\"post\\\",\\\"params\\\": {},\\\"url\\\":\\\"https://***\",\\\"userId\\\":\\\"1131971649***\\\"}\",",
            "ContactId": 123,
            "DingRobot": "https://oapi.dingtalk.com/robot/send?
access_token=91f2f6****",
            "SystemNoc": false,
            "ContactName": "John Doe"
```

`},`

```json
    "RequestId": "21E85B16-75A6-429A-9F65-8AAC9A54****"
```

#### 5.4.8 CreateAlertContactGroup

Creates an alert contact group.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateAlertCont actGroup | The operation that you want to perform. Set the value to CreateAlertContactGroup. |
| ContactGroupNa me | String | Yes | TestGroup | The name of the alert contact group. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
| ContactIds | String | No | 12* 23* 34* | The ID of the contact to be included in the alert contact group. Separate multiple contact IDs with spaces. You can call the SearchAlertContact interface to query the contact ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ContactGroupI d | String | 446* | The ID of the alert contact group. |
| RequestId | String | 70675725-8F11- 4817-8106- CFE0AD71**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateAlertContactGroup &ContactGroupName=TestGroup &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ContactGroupId>446*</ContactGroupId> <RequestId>70675725-8F11-4817-8106-CFE0AD71****</RequestId>
 JSON format
```

`{`

```json
    "ContactGroupId": "446*",
    "RequestId": "70675725-8F11-4817-8106-CFE0AD71****"
```

#### 5.4.9 DeleteAlertContactGroup

Deletes an alert contact group.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAlertCont actGroup | The operation that you want to perform. Set the value to DeleteAlertContactGroup. |
| ContactGroupId | Long | Yes | 123 | The ID of the contact group to be deleted. You can call the SearchAlertContactGroup interface to query the contact group ID. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| IsSuccess | Boolean | true | Indicates whether the alert contact group was deleted. true: The shipper is deleted. false: The shipper fails to be deleted. |
| RequestId | String | C21AB7CF-B7AF- 410F-BD61- 82D1567F**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteAlertContactGroup &ContactGroupId=123 &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>C21AB7CF-B7AF-410F-BD61-82D1567F****</RequestId>
 JSON format
```

`{`

```json
    "IsSuccess": true,
    "RequestId": "C21AB7CF-B7AF-410F-BD61-82D1567F****"
```

#### 5.4.10 UpdateAlertContactGroup

Updates an alert contact group.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateAlertCont actGroup | The operation that you want to perform. Set the value to UpdateAlertContactGroup. |
| ContactGroupId | Long | Yes | 123 | The ID of the contact group to be updated. You can call the SearchAlertContactGroup interface to query the contact group ID. |
| ContactGroupNa me | String | Yes | TestGroup | The new name of the contact group. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
| ContactIds | String | Yes | 12* 23* 34* | Required. The ID of the contact to be included in the alert contact group. Separate multiple contact IDs with spaces. You can call the SearchAlertContact interface to query the contact ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| IsSuccess | Boolean | true | Indicates whether the contact group was updated. true: The update was successful. false: The update failed. |

| RequestId | String | 9319A57D-2D9E- 472A-B69B- CF3CD16D**** | The ID of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateAlertContactGroup &ContactGroupId=123 &ContactGroupName=TestGroup &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>9319A57D-2D9E-472A-B69B-CF3CD16D****</RequestId>
 JSON format
```

`{`

```json
    "IsSuccess": true,
    "RequestId": "9319A57D-2D9E-472A-B69B-CF3CD16D****"
```

#### 5.4.11 SearchAlertContactGroup

Queries alert contact groups.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SearchAlertCont actGroup | The operation that you want to perform. Set the value to SearchAlertContactGroup. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
| ContactGroupNa me | String | No | TestGroup | The name of the alert contact group. |
| ContactName | String | No | John Doe | The name of the alert contact. |

| ContactId | Long | No | 123 | The ID of the alert contact. You can call the SearchAlertContact interface to query the contact ID. |
|---|---|---|---|---|
| ContactGroupIds | String | No | 746 | The ID of the alert contact group. You can query multiple contact group IDs at the same time. Separate contact group IDs with commas (,). |
| IsDetail | Boolean | No | true | Specifies whether to return all the alert contacts in the queried alert contact group. Default value: false. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ContactGroups | Array of ContactGroup |   | The information about the alert contact group. |
| ContactGroupI d | Long | 746 | The ID of the alert contact group. |
| ContactGroup Name | String | TestGroup | The name of the alert contact group. |
| Contacts | Array of Contact |   | The information about the alert contacts. |
| ContactId | Long | 123 | The ID of the contact. |
| ContactName | String | John Doe | The name of the alert contact. |
| CreateTime | Long | 1572349025000 | The timestamp when the alert contact was created. |
| DingRobot | String | https://oapi.dingtal k.com/robot/send? access token=91f2 _ f6**** | The webhook URL of the DingTalk chatbot. |
| Email | String | someone@exampl e.com | The email address of the alert contact. |
| Phone | String | 1381111**** | The mobile number of the alert contact. |

| SystemNoc | Boolean | false | Indicates whether the alert contact receives system notifications. Valid values: true: receives system notifications. false: does not receive system notifications. |
|---|---|---|---|
| UpdateTime | Long | 1580258717000 | The timestamp when the alert contact was updated. |
| UserId | String | 113197164949**** | The user ID. |
| CreateTime | Long | 1529668855000 | The timestamp that indicates the time when the pod was created. |
| UpdateTime | Long | 1529668855000 | The timestamp generated when the task information was updated. |
| UserId | String | 113197164949**** | The user ID. |
| RequestId | String | 4D6C358A-A58B- 4F4B-94CE- F5AAF023**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SearchAlertContactGroup &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ContactGroups>
    <ContactGroupId>746</ContactGroupId>
    <ContactGroupName>TestGroup</ContactGroupName>
    <UserId>113197164949****</UserId>
    <CreateTime>1529668855000</CreateTime>
    <UpdateTime>1529668855000</UpdateTime>
    <Contacts>
        <Email>someone@example.com</Email>
        <UserId>113197164949****</UserId>
        <Phone>1381111****</Phone>
        <CreateTime>1572349025000</CreateTime>
        <UpdateTime>1580258717000</UpdateTime>
        <ContactId>123</ContactId>
        <DingRobot>https://oapi.dingtalk.com/robot/send?access_token=91f2f6****
</DingRobot>
        <SystemNoc>false</SystemNoc>
        <ContactName>John Doe</ContactName>
    </Contacts>
</ContactGroups> <RequestId>4D6C358A-A58B-4F4B-94CE-F5AAF023****</RequestId>
 JSON format
```

`{`

```json
    "ContactGroups": {
        "ContactGroupId": 746,
        "ContactGroupName": "TestGroup",
        "UserId": "113197164949****",
        "CreateTime": 1529668855000,
        "UpdateTime": 1529668855000,
        "Contacts": {
            "Email": "someone@example.com",
            "UserId": "113197164949****",
            "Phone": "1381111****",
            "CreateTime": 1572349025000,
            "UpdateTime": 1580258717000,
            "ContactId": 123,
            "DingRobot": "https://oapi.dingtalk.com/robot/send?
access_token=91f2f6****",
            "SystemNoc": false,
            "ContactName": "John Doe"
```

`},`

```json
    "RequestId": "4D6C358A-A58B-4F4B-94CE-F5AAF023****"
```

#### 5.4.12 StartAlert

Starts an alert rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartAlert | The operation that you want to perform. Set the value to StartAlert. |
| AlertId | String | Yes | 1610*** | The ID of the alert rule. You can call the SearchAlertRules operation to query the ID of the alert rule. The corresponding response parameter is Id. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| IsSuccess | Boolean | true | Indicates whether the request was successful. Valid values: true: The operation is successful. false: The operation failed. |
| RequestId | String | 27E653FA-5958- 45BE-8AA9- 14D884DC**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=StartAlert &AlertId=1610*** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>27E653FA-5958-45BE-8AA9-14D884DC****</RequestId>
 JSON format
```

`{`

```json
    "IsSuccess": true,
    "RequestId": "27E653FA-5958-45BE-8AA9-14D884DC****"
```

#### 5.4.13 StopAlert

You can call this operation to stop an alert rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StopAlert | The operation that you want to perform. Set the value to StopAlert. |
| AlertId | String | Yes | 1610*** | The ID of the alert rule. You can call the SearchAlertRules operation to query the ID of the alert rule. The corresponding response parameter is Id. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| IsSuccess | Boolean | true | Indicates whether the request was successful. Valid values: true: The operation is successful. false: The operation failed. |
| RequestId | String | 27E653FA-5958- 45BE-8AA9- 14D884DC**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=StopAlert &AlertId=1610*** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>27E653FA-5958-45BE-8AA9-14D884DC****</RequestId>
 JSON format
```

`{`

```json
    "IsSuccess": true,
    "RequestId": "27E653FA-5958-45BE-8AA9-14D884DC****"
```

#### 5.4.14 SearchEvents

Queries alert event records.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SearchEvents | The operation that you want to perform. Set the value to SearchEvents. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
| AlertId | Long | No | 123 | The ID of the alert rule. You can call the SearchAlertRules operation to query the ID of the alert rule. The ID corresponds to the Id in the response parameters. |
| Pid | String | No | atc889zkcf@d8d eedfa9bf**** | The ID of the application associated with the alert. |
| CurrentPage | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 10. |
| AppType | String | No | TRACE | The type of the application that is associated with the alert rule. Valid values: TRACE ALL: all alert rules _ TRACE: application monitoring alert rules XTRACE: Tracing Analysis alert rules |

| AlertType | Integer | No | 5 | The type of the alert rule. Valid values: 1: custom monitoring and alert rules based on drill-down datasets. 3: custom monitoring and alert rules based on tiled datasets. 5: application monitoring alert rules. 100: System alarm. |
|---|---|---|---|---|
| IsTrigger | Integer | No | 1 | Specifies whether the alert event is triggered. If you do not set this parameter, all alert events are queried. Valid values: 1: trigger 0: not triggered |
| StartTime | Long | No | 1595565300000 | The beginning of the time range to query. Specify a UNIX timestamp of the LONG data type, in milliseconds. The default value is 10 minutes before the current time. |
| EndTime | Long | No | 1595568970000 | The end of the time range to query. The value is a UNIX timestamp of the LONG data type. Unit: milliseconds. The default value is the current time. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| IsTrigger | Integer | 1 | Indicates whether the alert event is triggered. 1: trigger 0: not triggered |
| PageBean | Struct |   | The returned struct. |
| Event | Array of Event |   | The information about the alert events. |
| AlertId | Long | 123 | The ID of the alert rule that is associated with the event. |
| AlertName | String | alertName | The name of the alert rule that is associated with the event. |

| AlertRule | String | {\"operator\":\"&\", \"rules\": [{\"aggregates\":\" AVG\",\"alias\":\"JV M ThreadCount\",\" _ measure\":\"appsta t.jvm.ThreadCount\ ",\"nValue\":1,\"ope rator\":\"HOH DOW _ N\",\"value\":50.0}] } | The condition of the alert rule. |
|---|---|---|---|
| AlertType | Integer | 5 | The type of the alert rule. Valid values: 1: custom monitoring and alert rules based on drill-down datasets. 3: custom monitoring and alert rules based on tiled datasets. 5: application monitoring alert rules. 100: System alarm. |
| EventLevel | String | 1 | The severity level of the event. Valid values: |
| EventTime | Long | 1595569020000 | The timestamp when the event occurred. |
| Id | Long | 123 | The ID of the note. |
| Links | List | [ "http://arms.consol e.aliyun.com/apm? startTime=159556 5300000&endTime =1595569246633 &regionId=cn- hangzhou&pid=*** *" ] | The list of event URLs. |
| Message | String | unknow emergency alarm \nip:172. XX.XX \nApplication name=test\nRegio n=cn-shenzhen \nException information= {"timestamp": "1615447972235" } | The event content. The value is a JSON string. The key indicates a dimension and the value indicates the alert content in the dimension. |
| PageNumber | Integer | 1 | The number of the page to return. |
| PageSize | Integer | 10 | The number of entries to return on each page. |

| TotalCount | Integer | 2 | The total number of entries returned. |
|---|---|---|---|
| RequestId | String | 32940175-181B- 4B93-966E- 4BB69176**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SearchEvents &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PageBean>
    <TotalCount>2</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Event>
        <EventLevel>1</EventLevel>
        <AlertType>5</AlertType>
        <AlertId>123</AlertId>
        <AlertName>alertName</AlertName>
        <Message>unknow emergency alarm \nip:172. XX.XX \nApplication
name=test\nRegion=cn-shenzhen \nException information ={\ "timestamp\":\"1615447972235\"}</Message>
        <EventTime>1595569020000</EventTime>
        <Id>123</Id>
        <AlertRule>{\"operator\":\"&\",\"rules\":
[{\"aggregates\":\"AVG\",\"alias\":\"Total number of JVM_threads \",\"measure\":\"appstat.jvm.ThreadCount\",\"nValue\":1,\"operator\": "HOH_DOWN", "valu e":50.0}]}</AlertRule>
        <Links>[ "http://arms.console.aliyun.com/apm?
startTime=1595565300000&amp;endTime=1595569246633&amp;regionId=cnhangzhou&amp;pid=****" ]</Links>
    </Event>
</PageBean> <RequestId>32940175-181B-4B93-966E-4BB69176****</RequestId> <IsTrigger>1</IsTrigger>
 JSON format
```

`{`

```json
    "PageBean": {
        "TotalCount": 2,
        "PageSize": 10,
        "PageNumber": 1,
        "Event": {
            "EventLevel": 1,
            "AlertType": 5,
            "AlertId": 123,
            "AlertName": "alertName",
            "Message": "unknow emergency alarm \\nip:172. XX.XX\\nApplication name=test\
\nRegion=cn-shenzhen \\nException information ={\\\" timestamp\\\":\\" 1615447972235\\\"}",
            "EventTime": 1595569020000,
            "Id": 123,
            "AlertRule": "{\\\"operator\\\":\\\"& \\\\ ",\\" rules\\\":
[\\\"aggregates\\\":\\\\" \\\ "\Value\\\" \\"\\" \\\"\\\" \\\"\\\" \\\\"\\\Value\\" \\\ \\\\\\\\\\\"" "\\\\\\\\" 50.0}]}",
            "Links": "[ \"http://arms.console.aliyun.com/apm?
startTime=1595565300000&amp;endTime=1595569246633&amp;regionId=cnhangzhou&amp;pid=****\" ]"
```

`},`

```json
    "RequestId": "32940175-181B-4B93-966E-4BB69176****",
    "IsTrigger": 1
```

#### 5.4.15 SearchAlertHistories

Queries the alert records of an alert rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SearchAlertHisto ries | The operation that you want to perform. Set the value to SearchAlertHistories. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the resource. |
| AlertId | Long | No | 123 | The ID of the alert rule. You can call the SearchAlertRules operation to query the ID of the alert rule. The ID corresponds to the Id in the response parameters. |

| AlertType | Integer | No | 5 | The type of the alert rule. Valid values: 1: custom monitoring and alert rules based on drill-down datasets. 3: custom monitoring and alert rules based on tiled datasets. 5: application monitoring alert rules. 100: System alarm. |
|---|---|---|---|---|
| CurrentPage | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 10. |
| StartTime | Long | No | 1595568910000 | The beginning of the time range to query. The value is a UNIX timestamp of the LONG data type. Unit: milliseconds. The default value is 10 minutes before the current time. |
| EndTime | Long | No | 1579499626000 | The end of the time range to query. The value is a UNIX timestamp of the LONG data type. Unit: milliseconds. The default value is the current time. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageBean | Struct |   | The returned struct. |
| AlarmHistories | Array of AlarmHistory |   | The list of alarm history objects. |
| AlarmContent | String | "Alert name: Alert1\nAlert time: 2020-07-24 12:14:00\nAlert content: A total of four alerts are triggered: ****" | The content of the alert. |
| AlarmRespons eCode | Integer | 200 | The status code returned for alert delivery. |

| AlarmSources | String | https://oapi.dingtal k.com/robot/send? access token=91f2 _ f65002fefe0ab9b7 1e6590c5ca50434 8cad742ff01e9c8a b204439ca**** | The alert webhook, such as the webhook URL of a DingTalk chatbot. |
|---|---|---|---|
| AlarmTime | Long | 1595564179000 | The time when the alert was sent. |
| AlarmType | Integer | 5 | The type of the alert rule. Valid values: 1: custom monitoring and alert rules based on drill-down datasets. 3: custom monitoring and alert rules based on tiled datasets. 5: application monitoring alert rules. 100: System alarm. |
| Emails | String | someone@exampl e.com | The email address that receives alerts. |
| Id | Long | 123 | The ID of the alert sending record. |
| Phones | String | 1381111**** | The mobile phone number that receives the alert. |
| StrategyId | String | "" | The status of the task. It is an internal parameter. |
| Target | String | "" | The status of the task. It is an internal parameter. |
| UserId | String | 113197164949**** | The user ID. |
| PageNumber | Integer | 1 | The number of the page to return. |
| PageSize | Integer | 10 | The number of entries to return on each page. |
| TotalCount | Integer | 2 | The total number of entries returned. |
| RequestId | String | 2FC13182-B9AF- 4E6B-BE51- 72669B7C**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SearchAlertHistories &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PageBean>
    <TotalCount>2</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <AlarmHistories>
        <Target>""</Target>
        <Phones>1381111****</Phones>
        <AlarmTime>1595564179000</AlarmTime>
        <UserId>113197164949****</UserId>
        <AlarmResponseCode>200</AlarmResponseCode>
        <AlarmType>5</AlarmType>
        <StrategyId>""</StrategyId>
        <AlarmContent>"Alert name: Alert1\nAlert time: 2020-07-24 12:14:00\nAlert
content: A total of four alerts are triggered: ****"</AlarmContent>
        <Emails>someone@example.com</Emails>
        <Id>123</Id>
        <AlarmSources>https://oapi.dingtalk.com/robot/send?
access_token=91f2f65002fefe0ab9b71e6590c5ca504348cad742ff01e9c8ab204439ca****</AlarmSou rces>
    </AlarmHistories>
</PageBean> <RequestId>2FC13182-B9AF-4E6B-BE51-72669B7C****</RequestId>
 JSON format
```

`{`

```json
    "PageBean": {
        "TotalCount": 2,
        "PageSize": 10,
        "PageNumber": 1,
        "AlarmHistories": {
            "Target": "\"\"",
            "Phones": "1381111****",
            "AlarmTime": 1595564179000,
            "UserId": "113197164949****",
            "AlarmResponseCode": 200,
            "AlarmType": 5,
            "StrategyId": "\"\"",
            "AlarmContent": "\"Alert name: Alert1\\nAlert time: 2020-07-24 12:14:00\\nAl
ert content: A total of four alerts are triggered: ****\"",
            "Emails": "someone@example.com",
            "Id": 123,
            "AlarmSources": "https://oapi.dingtalk.com/robot/send?
access_token=91f2f65002fefe0ab9b71e6590c5ca504348cad742ff01e9c8ab204439ca****"
```

`},`

```json
    "RequestId": "2FC13182-B9AF-4E6B-BE51-72669B7C****"
```
