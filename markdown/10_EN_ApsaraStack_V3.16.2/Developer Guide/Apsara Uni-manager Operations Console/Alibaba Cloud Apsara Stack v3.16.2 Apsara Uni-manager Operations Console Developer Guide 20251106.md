---
title: "Alibaba Cloud Apsara Stack v3.16.2 Apsara Uni-manager Operations Console Developer Guide"
product_version: "V3.16.2"
doc_version: "20251106"
pdf_pages: 65
source_pdf: "e619bdcaf233e7a9_Alibaba Cloud Apsara Stack v3.16.2 Apsara Uni-manager Operations Console Developer Guide 20251106.pd"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.16.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E7%BB%9F%E4%B8%80%E4%BA%91%E7%AE%A1/Alibaba%20Cloud%20Apsara%20Stack%20v3.16.2%20Apsara%20Uni-manager%20Operations%20Console%20Developer%20Guide%2020251106.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.16.2 Apsara Uni-manager Operations Console Developer Guide

## Table of Contents

- 1 Usage notes on development documentation
- 2 Preparations
  - 2.1 Log on to the Apsara Uni-manager Operations Console
  - 2.2 Obtain a region ID
  - 2.3 Obtain an AccessKey pair
  - 2.4 Obtain the service domain name
  - 2.5 Obtain the ASO Console SDKs
- 3 Call Examples for SDK for Java
  - 3.1 Getting started
  - 3.2 Use the SDK
    - 3.2.1 Install SDK for Java
    - 3.2.2 Configure authentication credentials
    - 3.2.3 Initiate a request
    - 3.2.4 Handle errors
- 4 API Reference
  - 4.1 Monitoring and alerting
    - 4.1.1 GetIncidentAlertList
    - 4.1.2 GetAlertList
  - 4.2 Inventory management
    - 4.2.1 GetOverview
    - 4.2.2 GetSlbInventoryInfo
    - 4.2.3 GetEcsInventoryList
    - 4.2.4 GetNasInventoryInfo
    - 4.2.5 GetOssInventoryInfo
    - 4.2.6 GetOtsInnerInventoryInfo
    - 4.2.7 GetRdsInventoryInfo
    - 4.2.8 GetSlsInnerInfo
  - 4.3 Resource management
    - 4.3.1 GetMachineList
    - 4.3.2 GetClusterListByProduct
    - 4.3.3 GetProductList
    - 4.3.4 GetCpuMetrics
    - 4.3.5 GetDiskMetrics
    - 4.3.6 GetIoMetrics
    - 4.3.7 GetLoadMetrics
    - 4.3.8 GetTrafficMetrics
    - 4.3.9 GetMemMetrics

notes on development document ation

## 1 Usage notes on development documentation

**development documentation**

This topic describes how to view the desired product development documentation when you use Apsara Stack API (ASAPI).

**Procedure**

You can follow the procedure described in the following figure to view the desired development documentation.

**Prerequisites**

The Apsara Stack version is obtained from an O&M personnel or operations administrator.

**Procedure**

You can go to the Apsara Stack documentation center and view the desired product documentation.
1. Go to the Apsara Stack Documentation Centerpage by using a browser.
2. Click the **Enterprise**, **Agility**, or **All-in-one** tab based on the Apsara Stack version that you
use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the name of the product that you want to view.
5. In the upper-right corner of the product documentation section, click **View Details** or
**Download PDF**.
ations

## 2 Preparations

### 2.1 Log on to the Apsara Uni-manager Operations Console

**manager Operations Console**

You can log on to the Apsara Uni-manager Operations console to obtain necessary personal data.

**Prerequisites**

The service domain name of the Apsara Uni-manager Operations Console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Operations Console in the address bar and press
Enter.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Letters
> Digits
> Special characters: ! @ # $ %

3. In the top navigation bar, click the user profile and select Personal information from the
drop-down list. Then, you can view the user information on the User Profile page.

### 2.2 Obtain a region ID

This topic describes how to obtain a region ID.

**Background information**

You must obtain a region ID before you call API operations of the Apsara Uni-manager Operations Console.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. On the left side of the top navigation bar, view the region ID.

### 2.3 Obtain an AccessKey pair

This topic describes how to obtain an AccessKey ID and AccessKey Secret. ations

**Background information**

You must obtain an AccessKey pair before you call API operations of the Apsara Uni-manager Operations Console. An AccessKey ID and an AccessKey secret are used to implement symmetric encryption and verify the identity of request senders. The AccessKey ID is used to identify a user and the AccessKey secret is a string that is used to encrypt the signature.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console and go to the User Profile page.
i. Log on to the Apsara Uni-manager Operations Console. ii. On the right side of the top navigation bar, click the user profile. iii. Select **Personal information** from the drop-down list.
2. On the User Profile page, view the AccessKey ID and AccessKey secret of the RAM user.

> **Note:** The AccessKey secret of an Apsara Stack tenant account cannot be displayed or used. Only the AccessKey secret of a RAM user can be displayed and used.

Only users who are assigned specific roles can use their AccessKey pairs to call specific API operations. For more information about roles, see Configure authentication credentials.
3. If no AccessKey pair of a RAM user is available, click **Create AccessKey Pair** to obtain an
AccessKey pair.

> **Note:** You can create a maximum of two AccessKey pairs for RAM users per account. The Create AccessKey Pair button is disabled after you create two AccessKey pairs.

### 2.4 Obtain the service domain name

**name**

This topic describes how to obtain the service domain name of the Apsara Uni-manager Operations Console.

**Background information**

You must obtain the intranet and Internet domain names before you call API operations of the Apsara Uni-manager Operation Console.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console and go to the User Profile page.
i. Log on to the Apsara Uni-manager Operations Console. ii. On the right side of the top navigation bar, click the profile image. iii. Select **Personal information** from the drop-down list.
2. Obtain the intranet and Internet domain names in the upper part of the **User Profile** page.
ations

### 2.5 Obtain the ASO Console SDKs

When you call API operations of a cloud service in Apsara Stack by using the POP gateway, you must use an SDK. This topic describes how to obtain the ASO Console SDKs. The ASO Console SDKs contain sample code and examples. The SDK for Java is provided. For more information, see Alibaba Cloud SDKs. We recommend that you use the SDK core library that is provided on the Alibaba Cloud official website. The SDK core library is shared by all cloud services and is compatible with Apsara Stack. amples for SDK for Java

## 3 Call Examples for SDK for Java

**Java**

### 3.1 Getting started

This topic describes how to obtain and use Apsara Uni-manager Operations Console SDK for Java.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained before you can use Apsara Stack SDK for Java. For more information, see Obtain an AccessKey pair. The two domain names of the Apsara Uni-manager Operations Console are obtained. For more information, see Obtain the service domain name. Apsara Stack SDK for Java 1.8 or a later version is used.

**Install the SDK**

If you use Apache Maven to manage a Java project, you need to only import the JAR file of Apsara Stack SDK for Java to the pom.xml file of the project. To use the Apsara Uni-manager Operations Console SDK, you must install the SDK core library and the SDK. We recommend that you use the core library version 4.5.17 or later, and use the SDK version 3.14.0.2. The following sample code provides an example on how to configure the pom.xml file.

```xml
<dependencies>
   <!--Required dependencies-->
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-uni-sdk</artifactId>
        <version>3.14.0.2</version>
        <scope>system</scope>
        <systemPath>${project.basedir}/libs/aliyun-java-uni-sdk-
3.14.0.2.jar</systemPath>
    </dependency>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-core</artifactId>
        <version>4.6.0</version>
    </dependency>
</dependencies>
```

**Use the SDK**

To use Apsara Stack SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.
The following sample code provides an example on how to call the GetOverview operation. amples for SDK for Java

```java
import com.aliyun.apsarabase.unisdk.SdkManager; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.asoops.model.v20220118.*; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.nrmops.model.v20220425.ListSwTotalRequest; import com.aliyuncs.nrmops.model.v20220425.ListSwTotalResponse; import com.aliyuncs.profile.DefaultProfile; import java.lang.reflect.InvocationTargetException; public class TestUniSDK {
    public static void main(String[] args) throws InvocationTargetException, IllegalAcc
sException, InstantiationException, ClientException {
        String region = "<yourRegion>";
        DefaultProfile profile = DefaultProfile.getProfile(
            region,
            "<yourAccessKeyId>",
            "<yourAccessKeySecret>"
```

);

```java
        IAcsClient client = new DefaultAcsClient(profile);
        String internetDomain = "<yourInternetDomain>";
        String intranetDomain = "<yourIntranetDomain>";
        boolean isCenterRegion = true;  // Set this parameter based on the value of r
egion.
        SdkManager sdkManager = new SdkManager(internetDomain, intranetDomain, region,
CenterRegion);
        System.out.println("ListSwTotalRequest");
        ListSwTotalRequest listSwTotalRequest = sdkManager.getModel(ListSwTotalRequest.
ass);
        ListSwTotalResponse listSwTotalResponse = client.getAcsResponse(listSwTotalRequ
t);
        System.out.println(listSwTotalResponse.getData().get(0).getHostName());
        System.out.println("GetOssInventoryInfo");
        GetOssInventoryInfoRequest getOssInventoryInfoRequest = sdkManager.getModel(Get
sInventoryInfoRequest.class);
        GetOssInventoryInfoResponse getOssInventoryInfoResponse = client.getAcsResponse
etOssInventoryInfoRequest);
        System.out.println(getOssInventoryInfoResponse.getData().getOverview().getDisk_
main());
```

### 3.2 Use the SDK

#### 3.2.1 Install SDK for Java

amples for SDK for Java This topic describes how to install and use Apsara Uni-manager Operations Console SDK for Java. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK. For more information, visit Alibaba Cloud SDKs. To use Apsara Uni-manager Operations Console SDK for Java, you must install the SDK core library and the SDK. We recommend that you use the core library version 4.5.17 or later, and use the SDK version 3.16.2.0.

```xml
<dependencies>
    <! --Required dependencies-->
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-asoops</artifactId>
        <version>3.16.2.0</version>
        <scope>system</scope>
        <systemPath>${project.basedir}/libs/aliyun-java-sdk-asoops-
3.16.2.0.jar</systemPath>
    </dependency>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-core</artifactId>
        <version>4.6.0</version>
    </dependency>
</dependencies>
```

#### 3.2.2 Configure authentication credentials

When you use an Apsara Stack SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. Apsara Stack SDK for Java supports identity verification based on an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as the credentials when you initialize the client.

> **Note:** Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be exposed to risks.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",          // Enter the region ID.
    "<yourAccessKeyID>",      // Enter your AccessKey ID.
    "<yourAccessKeySecret>"    // Enter your AccessKey secret.
```

); amples for SDK for Java

|   | Note In the preceding sample code, replace the variables with actual values based on your needs and remove the angle brackets (<>) from the final code. Only users who are assigned specific roles can use their AccessKey pairs to call specific API operations. However, the users who are assigned the OAM super administrator role can call all the API operations. |   |   |
|---|---|---|---|
|   |   | OAM super |   |
|   | administrator |   |   |

| API operation | Supported role |
|---|---|
| GetAlertList | ASO System Administrator, ASO Product Devops, ASO Daily Devops, ASO Duty Officer, and ASO Devops Readonly |
| GetIncidentAlertList | ASO System Administrator, ASO Product Devops, ASO Daily Devops, ASO Duty Officer, and ASO Devops Readonly |
| GetOverview | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetEcsInventoryList | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetNasInventoryInfo | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetOssInventoryInfo | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetOtsInnerInventoryInfo | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetRdsInventoryInfo | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetSlbInventoryInfo | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetSlsInnerInfo | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetMachineList | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |

|   | Apsara Uni-manager Operations Console Developer Guide·Call E amples for SDK for Jav |
|---|---|

| API operation | Supported role |
|---|---|
| GetClusterListByProduct | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetProductList | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetCpuMetrics | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetDiskMetrics | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetIoMetrics | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetLoadMetrics | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetTrafficMetrics | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |
| GetMemMetrics | ASO System Administrator, ASO Product Devops, ASO Daily Devops, and ASO Devops Readonly |

#### 3.2.3 Initiate a request

This topic describes how to use the ASO Console SDKs to initiate a request.

**Procedure**

1. Create an AcsClient.

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Initialize SdkManager.
SdkManager receives all O&M requests sent from API gateways. The following parameters are required to initialize the SdkManager: `internetDomain` , `intranetDomain` , `region` , and `isCenterRegion` . For more information about how to set the first three parameters, see Obtain a region ID and Obtain the service domain name.

| isCenterRegion isCenterRegion to | based o true |
|---|---|

| ent. If | region | is |
|---|---|---|
| isCenterRegion |   |   |

Set `isCenterRegion` based on your environment. If `region` is set to the central region, set isCenterRegion to `true` . Otherwise, set `isCenterRegion` to `false` . amples for SDK for Java

```
String internetDomain = "<yourInternetDomain>"; // Enter your Internet domain. String intranetDomain = "<yourIntranetDomain>"; // Enter your intranet domain. boolean isCenterRegion = true; // Enter a boolean value based on the value of region. SdkManager sdkManager = new SdkManager(internetDomain, intranetDomain, region, isCent erRegion);
```

3. Create a request by using SdkManager.
Name the request in the format of ${apiName}Request , where **${apiName}** indicates the name of an API operation, such as GetOverview. When SDKs include API operations of multiple services, different requests may have the same name. You can differentiate the requests based on package names.

```
GetOverviewRequest getOverviewRequest = sdkManager.getModel(GetOverviewRequest.class);
```

4. Initiate the request and handle the response.

```java
// Initiate a request and view the result. try {
    GetOverviewResponse acsResponse = client.getAcsResponse(getOverviewRequest);
    String zoneName = acsResponse.getData().getEcs().get(0).getZoneName();
    System.out.println(zoneName);
} catch (Exception e) {
    e.printStackTrace();
```

#### 3.2.4 Handle errors

If the server or SDK encounters an error when you use the Java SDK, the SDK returns an error response. The error response contains an error code and an error message. In most cases, you do not need to handle the errors returned by the Java SDK. You only need to handle server errors based on error messages generated on the server side. `ServerException` indicates a server error. `ClientException` indicates an error returned by the SDK. For example, if the following error occurs, you can modify the AccessKey ID based on the error message:

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

If you want to handle the SDK errors returned by the SDK, refer to the following example to write your code: amples for SDK for Java

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handle the response.
    // ...
} catch (ClientException e) {
    // You can add your error handling logic here.
    // For example, display the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    e.printStackTrace();
} catch (ServerException e) {
    e.printStackTrace();
```

## 4 API Reference

### 4.1 Monitoring and alerting

#### 4.1.1 GetIncidentAlertList

Queries alerts. Call this operation instead of the `GetAlertList` operation to query alerts.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Syntax**

```
GET /openapi/popResource/aso/incident/api/alert/list HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| page | Integer | Quer y | No | 1 | The number of the page to return. |
| pageSize | Integer | Quer y | No | 20 | The number of entries to return on each page. |
| keywords | String | Quer y | No | ecs | The alert keyword that is used for fuzzy search. |
| code | String | Quer y | No | CPUHigh | The alert code. |
| statusList.N | Repeat List | Quer y | No | 0 | The alert status. Valid values: 0: not handled 1: processing 2: closed |
| level | Integer | Quer y | No | 1 | The severity level of the alert. Valid values: 1: P1 2: P2 3: P3 4: P4 |

| startTimeMin | Integer | Quer y | No | 1920001300 | The beginning of the time range to query alerts. The value must be a timestamp. Unit: seconds. |
|---|---|---|---|---|---|
| startTimeMax | Integer | Quer y | No | 1920001300 | The end of the time range to query alerts. The value must be a timestamp. Unit: seconds. |
| source | String | Quer y | No | tianjimon | The data source. |
| product | String | Quer y | No | aso | The service that triggered the alert. |
| orderByStartTi meAsc | Boolea n | Quer y | No | true | Specifies whether to sort the alerts in ascending order based on the time when they are triggered. |

The following items describe how to obtain specific alerts about physical servers:

| : Set code to hardware monitor new . _ _ ame is hardware monitor new alarm _ _ _ SasRaidMonitor . | hardware monitor new _ _ |   | . |
|---|---|---|---|
| SasRaidMonitor |   |   |   |
|   |   | . |   |

```
 DiskBackplaneMonitor  or  SasRaidMonitor .
```

| to | hardware monitor new _ _ | . In |
|---|---|---|
| hardware monitor new alarm _ _ _ |   |   |

| de to | hardware monitor new . _ _ |
|---|---|
| hardware monitor new alarm _ _ _ |   |

| to | hardware monitor new _ _ | . I |
|---|---|---|
| hardware monitor new alarm _ _ _ |   |   |

Memory status: Set code to `hardware_monitor_new` . In the returned result, find the data entry whose alertName is `hardware_monitor_new_alarm` and monitor is `MemoryMonitor` .

| e to | hardware monitor new _ _ | . |
|---|---|---|
| hardware monitor new alarm _ _ _ |   |   |

| to | hardware monitor new . _ _ | In |
|---|---|---|
| hardware monitor new alarm _ _ _ |   |   |

|   | ntp cluster host _ _ |
|---|---|
| host ntp sync state alarm _ _ _ _ |   |

NTP offset: Set code to `ntp_cluster_host` . In the returned result, find the data entry whose

|   | check pangu disk error _ _ _ |
|---|---|
| check pangu disk error _ _ _ |   |

Apsara Distributed File System damaged disk: Set code to `check_pangu_disk_error` . In the returned result, find the data entry whose alertName is `check_pangu_disk_error` .

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| cost | Long | 30 | The time spent on querying alerts. Unit: milliseconds. |

| data | Map | {"totalPage":2478 6,"pageSize":1,"tot al":24786,"page":1 ,"objectList": [{"id":844934,"star tTime":"2022-02- 24T08:33:29.000+ 0000","endTime":" 1970-01- 01T00:00:00.000+ 0000","duration":3 7197,"message":"T ianji SR Postcheck failed Alarm- 01.100.2000.0000 2","code":"tj client _ proxy machine sr _ _ _ monitor state","m _ _ etricName":"tj clie _ nt proxy machine _ _ _ sr monitor state"," _ _ metricProject":"tjm tianji","alarmNam _ e":"private.C ECS- _ XXX-X- XXcc tianji postch _ _ eck monitor alarm _ _ tianji sub- __ _ tianjiclient","alarm Rule":"$level==\"e rror\"\|\|$level==\"E RROR\"\|\|$level==\" FATAL\"\|\|$level==\ "fatal\"","currentVa lue":" {\"level\":\"error\"} ","source":"tianjim on","type":"metric" ,"dimensions": [{"key":"cluster","v alue":"ECS-XX-X- XXXX","standard":t rue}],"level":1,"sta tus":0,"alarmCount ":1,"handleUserNa me":"","shield":fals e,"region":"cn-XX- XX- XX","product":"ecs ","cluster":"ECS- XX-X- XXXX","service":"ti anji","serverRole":" ","hostname":"","ch eckInterval":0,"last AlarmTime":"2022- 02- 24T08:33:29.000+ 0000"}]} | The returned results. |
|---|---|---|---|
| eagleEyeTrace Id | String | 0acd10a61654599 3190765214d002a | The EagleEye ID. |

| errorCode | String | "" | The error code. |
|---|---|---|---|
| errorStack | String | "" | The stack where the error occurred. |
| msg | String | "" | The error message. |
| success | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |
| version | String | v1 | The version of the internal API. |

The data parameter includes the following fields: totalPage: The total number of returned pages. pageSize: The number of data entries returned on each page. total: The total number of returned alerts. page: The page number. objectList: The returned alerts. id: The alert ID. startTime: The time when the alert was triggered. endTime: The time when the alert was closed. duration: The duration of the alert. message: The alert message. code: The alert code. metricName: The metric name. metricProject: The monitored project. alarmName: The name of the alert. alarmRule: The rule that describes how the alert is triggered. currentValue: The current value. source: The alert source. type: The type of the alert. dimensions: The alert dimensions. key: The dimension key. value: The dimension value. standard: Indicates whether the dimension is a standard dimension. level: The severity level of the alert. The values 1 to 4 indicate P1 to P4. status: The status of the alert. 0 indicates that the alert is not handled, 1 indicates that the alert is being processed, and 2 indicates that the alert is closed. alarmCount: The number of alerts. handleUserName: The user who handled the alert. shield: Indicates whether the alert is blocked. region: The ID of the region. product: The name of the product. cluster: The name of the cluster. service: The name of the service. hostname: The hostname of the node. checkInterval: The interval at which the system checks for alerts. lastAlarmTime: The last time when an alert was triggered.

**Examples**

Sample requests

```
GET /openapi/popResource/aso/incident/api/alert/list HTTP/1.1
```

Sample success responses `JSON` format

```json
    "msg": "\"\"",
    "eagleEyeTraceId": "0acd10a616545993190765214d002a",
    "cost": "30",
    "data": "
{\"totalPage\":24786,\"pageSize\":1,\"total\":24786,\"page\":1,\"objectList\":[{\"id\": 844934,\"startTime\":\"2022-02-24T08:33:29.000+0000\",\"endTime\":\"1970-01- 01T00:00:00.000+0000\",\"duration\":37197,\"message\":\"Tianji SR Postcheck failed Alar
```

`m-`

```
01.100.2000.00002\",\"code\":\"tj_client_proxy_machine_sr_monitor_state\",\"metricName\": tj_client_proxy_machine_sr_monitor_state\",\"metricProject\":\"tjm_tianji\",\"alarmName\" "private.C_ECS-XXX-X-XXcc_tianji_postcheck_monitor_alarm__tianji_subtianjiclient\",\"alarmRule\":\"$level==\\\"error\\\"||$level==\\\"ERROR\\\"||$level==\\\" TAL\\\"||$level==\\\"fatal\\\"\",\"currentValue\":\" {\\\"level\\\":\\\"error\\\"}\",\"source\":\"tianjimon\",\"type\":\"metric\",\"dimensions :[{\"key\":\"cluster\",\"value\":\"ECS-XX-X- XXXX\",\"standard\":true}],\"level\":1,\"status\":0,\"alarmCount\":1,\"handleUserName\":\ ",\"shield\":false,\"region\":\"cn-XX-XX-XX\",\"product\":\"ecs\",\"cluster\":\"ECS-XX-
```

`X-`

```json
XXXX\",\"service\":\"tianji\",\"serverRole\":\"\",\"hostname\":\"\",\"checkInterval\":0,\ astAlarmTime\":\"2022-02-24T08:33:29.000+0000\"}]}",
    "success": "true",
    "errorCode": "\"\"",
    "version": "v1",
    "errorStack": "\"\""
```

#### 4.1.2 GetAlertList

Queries the list of alerts.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Request syntax**

```
GET /openapi/popResource/aso/fullview/popapi/getAlertList HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| startTime | String | Quer y | Yes | 2021-12-01 00:00:00 | The beginning of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format. |
| endTime | String | Quer y | Yes | 2021-12-01 00:00:00 | The end of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format. |
| page | Integer | Quer y | Yes | 1 | The number of the page to return. |
| pageSize | Integer | Quer y | Yes | 15 | The number of entries to return on each page. |
| type | String | Quer y | No | metric | The alert type. Valid values: metric event |
| level | Integer | Quer y | No | 1 | The severity level of the alert. Valid values: 0 to 5. |
| alertName | String | Quer y | No | alert a _ | The name of the alert. |
| metricName | String | Quer y | No | aso a _ | The monitored metric. |
| alertProduct | String | Quer y | No | oss | The name of the product. |
| cluster | String | Quer y | No | OssHybridClus ter-X-XX-XX | The name of the cluster. |
| service | String | Quer y | No | tianji | The name of the service. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The returned code. 200 indicates that the call was successful. |
|---|---|---|---|
| cost | Long | 30 | The time spent on querying alerts. Unit: milliseconds. |
| data | Struct |   | The returned data. |
| currentPage | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 15 | The number of entries returned per page. |
| result | Array of result |   | The returned result set. |
| alarmId | String | 02.305.0101.0000 5 | The ID of the alert. |
| alertCount | Integer | 1 | The number of historical alerts. |
| alertName | String | alert name _ | The name of the alert. |
| changeRecord | String | [{\"key\":\"Start\",\" time\":1590393226 471,\"value\":\"SER IOUS\"}, {\"key\":\"Recover\ ",\"time\":1590402 946453,\"value\":\" RECOVER\"}] | The record of modifications. |
| cluster | String | OssXX-XX-XX | The name of the cluster. |
| contacts | Array of contacts |   | Details about the contacts to which the alert was sent. |
| combinationTy pe | Integer | 1 |   |
| department | String | dept1 | The department. |
| dingding | String | 1234567 | The DingTalk account of the contact. |
| dingdingNotifi cationOn | Boolean | true | The DingTalk notification status. |

| dutyEndTime | Long | 1592358292430 | The point in time at which the work shift ends. |
|---|---|---|---|
| dutyStartTime | Long | 1592358292430 | The point in time at which the work shift starts. |
| email | String | "" | The email address of the contact. |
| emailNotificati onOn | Boolean | true | The email notification status. |
| id | Integer | 1 | The ID of the primary key. |
| levels | List | null | The severity level of the alert. |
| levelsJson | String | "" | The severity level of the alert in the JSON format. |
| product | String | "" | The name of the product. |
| products | List | "" | The list of products. |
| productsJson | String | "" | The list of products in the JSON format. |
| region | String | "" | The name of the region. |
| role | String | "" | The role of the contact. |
| telephone | String | "" | The phone number of the contact. |
| telephoneNotif icationOn | Boolean | true | The phone notification status. |
| username | String | admin | The username. |
| dataSource | String | tianjimon | The data source. |
| dimensions | String | {\"cluster\":\"Oss2L 54Cluster-X-XX- XX\",\"serverrole\": \"oss- service.OssCluster Monitor#\",\"host\" :\"vm010017XXXX\ "} | The alert information. |

| eventLevel | String | P3 | The level of the event. |
|---|---|---|---|
| eventSource | Map | "" | The event source. |
| eventStatus | String | Done | The status of the event. |
| eventType | Integer | 1 | The type of the event. |
| hashCode | String | 295452124 | The hash code of the alert event. |
| id | Integer | 46082 | The ID of the alert event. |
| lastTime | Long | 1295964673 | The duration of the alert event. Unit: milliseconds. |
| message | String | The read and write latency of requests at the frontend of an OSS cluster exceeds the threshold. The threshold is 1,000 ms. | The error message. |
| metricName | String | oss service- _ cluster error code _ _ _ from chiji _ | The monitored metric. |
| metricProject | String | tjm oss service _ _ | The product to which the object belongs. |
| metricType | String | METRIC | The type of the event. |
| notifyFlag | Boolean | true | Indicates whether the notification flag was enabled. |
| processTime | Long | 1590393226471 | The time at which the alert was handled. |
| product | String | "" | The name of the product. |
| region | String | "" | The name of the region. |
| service | String | oss-service | The name of the service. |
| startTime | Long | 1590393226471 | The time when the alert was triggered. |

| type | String | test | The type of the alert. |
|---|---|---|---|
| updateTime | Long | 1590393226471 | The time when the alert status was updated. |
| total | Integer | 200 | The total number of returned data entries. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| message | String | success | The error message. |
| requestId | String | fccbab1d-a496- 4ae6-88e8- 83557f883a85 | The ID of the request. |
| successRespo nse | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/fullview/popapi/getAlertList HTTP/1.1
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": {
        "total": "200",
        "pageSize": "15",
        "currentPage": "1",
        "result": [
                "lastTime": "1295964673",
                "cluster": "OssXX-XX-XX",
                "metricName": "oss_service-cluster_error_code_from_chiji",
                "eventSource": "\"\"",
                "type": "test",
                "processTime": "1590393226471",
                "metricType": "METRIC",
"changeRecord":"
```

```json
                changeRecord:
[{\\\"key\\\":\\\"Start\\\",\\\"time\\\":1590393226471,\\\"value\\\":\\\"SERIOUS\\\"},{ \\\"key\\\":\\\"Recover\\\",\\\"time\\\":1590402946453,\\\"value\\\":\\\"RECOVER\\\"}]",
                "eventLevel": "P3",
                "alertName": "alert_name",
                "hashCode": "295452124",
                "alarmId": "02.305.0101.00005",
                "startTime": "1590393226471",
                "id": "46082",
                "notifyFlag": "true",
                "product": "\"\"",
                "updateTime": "1590393226471",
                "eventType": "1",
                "message": "The read and write latency of requests at the frontend of an
OSS cluster exceeds the threshold 1,000 ms.",
                "metricProject": "tjm_oss_service",
                "alertCount": "1",
                "service": "oss-service",
                "eventStatus": "Done",
                "region": "\"\"",
                "dataSource": "tianjimon",
                "dimensions": "{\\\"cluster\\\":\\\"Oss2L54Cluster-X-XX-XX\\\",\\\"serve
rrole\\\":\\\"oss-service.OssClusterMonitor#\\\",\\\"host\\\":\\\"vm010017XXXX\\\"}",
                "contacts": [
                        "product": "\"\"",
                        "role": "\"\"",
                        "dutyStartTime": "1592358292430",
                        "levelsJson": "\"\"",
                        "telephone": "\"\"",
                        "dingding": "1234567",
                        "dutyEndTime": "1592358292430",
                        "productsJson": "\"\"",
                        "dingdingNotificationOn": "true",
                        "combinationType": "1",
                        "telephoneNotificationOn": "true",
                        "id": "1",
                        "emailNotificationOn": "true",
                        "region": "\"\"",
                        "department": "dept1",
                        "email": "\"\"",
                        "username": "admin",
                        "products": "\"\"",
                        "levels": "null"
```

`]` `]` `},`

```json
    "level": "\"\"",
    "requestId": "fccbab1d-a496-4ae6-88e8-83557f883a85",
    "message": "success",
    "key": "\"\""
```

### 4.2 Inventory management

#### 4.2.1 GetOverview

Queries the inventory overview.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getOverview HTTP/1.1
```

**Request parameters**

None

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned code. 200 indicates that the call was successful. |
| cost | Long | 30 | The time spent on querying the inventory information. Unit: milliseconds. |
| data | Struct |   | The returned data. |
| ecs | Array of ecs |   | The Elastic Compute Service (ECS) inventory information. |
| flavors | Array of JSONArray |   | The list of ECS instance specifications. |
| flavor | String | ecs.sn1ne.8xlarge | The ECS instance specification. |
| soldAmount | Integer | 3 | The number of sold resources. |
| totalAmount | Integer | 8 | The number of total resources. |
| vendibleAmou nt | Integer | 5 | The number of available resources. |

| zoneId | Integer | 132 | The ID of the region. |
|---|---|---|---|
| zoneName | String | ECS-XX-XX-XX-X | The name of the region. |
| nas | Struct |   | The Apsara File Storage NAS (NAS) inventory information. |
| clusters | Map | {"StandardNasClus ter-XX-XX-XX": {"disk usage":"9.3 _ 00003","disk used" _ :"13250.83","disk t _ otal":"142482.0","d isk remain":"1292 _ 31.17"}} | The information about the cluster. |
| oss | Struct |   | The Object Storage Service (OSS) inventory information. |
| overview | Struct |   | The inventory information. |
| cluster | String | "" | The information about the cluster. |
| disk remain _ | Float | 945318.56 | The free space of the disk. |
| disk total _ | Float | 1064488 | The total capacity of the disk. |
| disk usage _ | Float | 11.195 | The usage of the disk in percentage. |
| disk used _ | Float | 119169.43 | The used space of the disk. |
| ots | Struct |   | The Tablestore inventory information. |
| overview | Struct |   | The inventory information. |
| cluster | String | "" | The information about the cluster. |
| disk remain _ | Float | 347621.84 | The free space of the disk. |
| disk total _ | Float | 389886 | The total capacity of the disk. |
| disk usage _ | Float | 10.840136 | The usage of the disk in percentage. |

| disk used _ | Float | 42264.17 | The used space of the disk. |
|---|---|---|---|
| rds | Struct |   | The ApsaraDB RDS inventory information. |
| engines | Map | {"hawq": {"mem used":"0.0 _ ","cpu used":"0.0", _ "mem usage":"0.0 _ ","disk total":"0.0", _ "disk used":"0.0"," _ disk remain":"0.0", _ "cpu remain":"0.0" _ ,"disk usage":"0.0", _ "mem remain":"0. _ 0","cpu total":"0.0" _ ,"cpu usage":"0.0", _ "mem total":"0.0"} _ } | The information about ApsaraDB RDS inventory on each engine. |
| overview | Struct |   | The information about the total ApsaraDB RDS inventory. |
| cluster | String | "" | The information about the cluster. |
| disk remain _ | Float | 55302 | The free space of the disk. |
| disk total _ | Float | 82826 | The total capacity of the disk. |
| disk usage _ | Float | 33.23232 | The usage of the disk in percentage. |
| disk used _ | Float | 27525 | The used space of the disk. |
| slb | Map | {"INTERNET": {"ip usage":"8.984 _ 375","ip used":"23 _ ","ip remain":"233" _ ,"ip total":"256","ty _ pe":"INTERNET"},"I NTRANET": {"ip usage":"14.33 _ 59375","ip used":" _ 367","ip remain":" _ 2193","ip total":"2 _ 560","type":"INTRA NET"}} | The Server Load Balancer (SLB) inventory information. |
| sls | Struct |   | The Log Service inventory information. |
| overview | Struct |   | The inventory information. |

| cluster | String | "" | The information about the cluster. |
|---|---|---|---|
| disk remain _ | Float | 245040.0 | The free space of the disk. |
| disk total _ | Float | 266122.0 | The total capacity of the disk. |
| disk usage _ | Float | 7.9219303 | The usage of the disk in percentage. |
| disk used _ | Float | 21082.0 | The used space of the disk. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| message | String | success | The error message. |
| requestId | String | c6cb0637-40a1- 4ac0-abe7- ad45efc848ac | The ID of the request. |
| successRespo nse | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getOverview HTTP/1.1 OpsProduct: ASOOps
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": {
        "slb": "{\"INTERNET\":
{\"ip_usage\":\"8.984375\",\"ip_used\":\"23\",\"ip_remain\":\"233\",\"ip_total\":\"256\", type\":\"INTERNET\"},\"INTRANET\": {\"ip_usage\":\"14.3359375\",\"ip_used\":\"367\",\"ip_remain\":\"2193\",\"ip_total\":\"25 \",\"type\":\"INTRANET\"}}",
        "ecs": [
```

```json
                "zoneId": "132",
                "zoneName": "ECS-XX-XX-XX-X",
                "flavors": [
                        "flavor": "ecs.sn1ne.8xlarge",
                        "totalAmount": "8",
                        "vendibleAmount": "5",
                        "soldAmount": "3"
```

`]` `],`

```json
        "rds": {
            "engines": "{\"hawq\":
{\"mem_used\":\"0.0\",\"cpu_used\":\"0.0\",\"mem_usage\":\"0.0\",\"disk_total\":\"0.0\",\ isk_used\":\"0.0\",\"disk_remain\":\"0.0\",\"cpu_remain\":\"0.0\",\"disk_usage\":\"0.0\", mem_remain\":\"0.0\",\"cpu_total\":\"0.0\",\"cpu_usage\":\"0.0\",\"mem_total\":\"0.0\"}}"
            "overview": {
                "cluster": "\"\"",
                "disk_used": "27525",
                "disk_total": "82826",
                "disk_remain": "55302",
                "disk_usage": "33.23232"
```

`},`

```json
        "sls": {
            "overview": {
                "cluster": "\"\"",
                "disk_used": "21082.0",
                "disk_total": "266122.0",
                "disk_remain": "245040.0",
                "disk_usage": "7.9219303"
```

`},`

```json
        "ots": {
            "overview": {
                "cluster": "\"\"",
                "disk_used": "42264.17",
                "disk_total": "389886",
                "disk_remain": "347621.84",
                "disk_usage": "10.840136"
```

`},`

```json
        "nas": {
            "clusters": "{\"StandardNasCluster-XX-XX-XX\":
{\"disk_usage\":\"9.300003\",\"disk_used\":\"13250.83\",\"disk_total\":\"142482.0\",\"dis remain\":\"129231.17\"}}"
```

`},`

```json
        "oss": {
            "overview": {
                "cluster": "\"\"",
                "disk_used": "119169.43",
                "disk_total": "1064488",
```

```json
                "disk_remain": "945318.56",
                "disk_usage": "11.195"
```

`},`

```json
    "level": "\"\"",
    "requestId": "c6cb0637-40a1-4ac0-abe7-ad45efc848ac",
    "message": "success",
    "key": "\"\""
```

#### 4.2.2 GetSlbInventoryInfo

Queries SLB inventory information.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getSlbInventoryInfo HTTP/1.1
```

**Request parameters**

None

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned code. 200 indicates that the call was successful. |
| cost | Long | 30 | The time spent on querying SLB inventory information. Unit: milliseconds. |
| data | Map | {"INTERNET": {"ip usage":"5.078 _ 125","ip used":"26 _ ","ip remain":"486" _ ,"ip total":"512","ty _ pe":"INTERNET"},"I NTRANET": {"ip usage":"22.97 _ 3633","ip used":"9 _ 41","ip remain":"3 _ 155","ip total":"40 _ 96","type":"INTRAN ET"}} | The returned data. |
| key | String | "" | The keyword of the error. |

| level | String | "" | The error level. |
|---|---|---|---|
| message | String | success | The error message. |
| requestId | String | 56bb6208-89f0- 4b62-a2e6- 5204db52fcf5 | The ID of the request. |
| successRespo nse | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getSlbInventoryInfo HTTP/1.1
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": "{\"INTERNET\":
{\"ip_usage\":\"5.078125\",\"ip_used\":\"26\",\"ip_remain\":\"486\",\"ip_total\":\"512\", type\":\"INTERNET\"},\"INTRANET\": {\"ip_usage\":\"22.973633\",\"ip_used\":\"941\",\"ip_remain\":\"3155\",\"ip_total\":\"409 ",\"type\":\"INTRANET\"}}",
    "level": "\"\"",
    "requestId": "56bb6208-89f0-4b62-a2e6-5204db52fcf5",
    "message": "success",
    "key": "\"\""
```

#### 4.2.3 GetEcsInventoryList

Queries ECS inventory information.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Request syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getEcsInventoryList HTTP/1.1
```

**Request parameters**

None

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned code. 200 indicates that the call was successful. |
| cost | Long | 30 | The time spent on querying the inventory information. Unit: milliseconds. |
| data | Array of JSONArray |   | The returned data. |
| flavors | Array of JSONArray |   | The list of ECS instance types. |
| flavor | String | ecs.mn4v2.2xlarge | The type of the ECS instance. |
| soldAmount | Integer | 4 | The sold resources. |
| totalAmount | Integer | 48 | The total resources. |
| vendibleAmou nt | Integer | 44 | The available resources. |
| zoneId | Integer | 131 | The ID of the region. |
| zoneName | String | ECS-XX-XX-XX | The name of the region. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| message | String | "" | The error message. |
| requestId | String | 8d526115-1347- 4fba-8d48- 6fe267701983 | The ID of the request. |
| successRespo nse | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getEcsInventoryList HTTP/1.1 OpsProduct: ASOOps
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": [
            "zoneId": "131",
            "zoneName": "ECS-XX-XX-XX",
            "flavors": [
                    "flavor": "ecs.mn4v2.2xlarge",
                    "totalAmount": "48",
                    "vendibleAmount": "44",
                    "soldAmount": "4"
```

`]` `],`

```json
    "level": "\"\"",
    "requestId": "8d526115-1347-4fba-8d48-6fe267701983",
    "message": "\"\"",
    "key": "\"\""
```

#### 4.2.4 GetNasInventoryInfo

Queries NAS inventory information.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Request syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getNasInventoryInfo HTTP/1.1
```

**Request parameters**

None

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned code. 200 indicates that the call was successful. |
| cost | Long | 30 | The time spent on querying the inventory information. Unit: milliseconds. |
| data | Struct |   | The returned data. |
| clusters | Map | {"StandardNasClus ter-XX-XX-XX": {"disk usage":"9.3 _ 00003","disk used" _ :"13250.83","disk t _ otal":"142482.0","d isk remain":"1292 _ 31.17"}} | The information about the cluster. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| message | String | "" | The error message. |
| requestId | String | adb1a2e2-ccea- 4701-ac0b- cb1fe6034c17 | The ID of the request. |
| successRespo nse | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getNasInventoryInfo HTTP/1.1 OpsProduct: ASOOps
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": {
        "clusters": "{\"StandardNasCluster-XX-XX-XX\":
{\"disk_usage\":\"9.300003\",\"disk_used\":\"13250.83\",\"disk_total\":\"142482.0\",\"dis remain\":\"129231.17\"}}"
```

`},`

```json
    "level": "\"\"",
    "requestId": "adb1a2e2-ccea-4701-ac0b-cb1fe6034c17",
    "message": "\"\"",
    "key": "\"\""
```

#### 4.2.5 GetOssInventoryInfo

Queries OSS inventory information.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getOssInventoryInfo HTTP/1.1
```

**Request parameters**

None

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned code. 200 indicates that the call was successful. |
| cost | Long | 30 | The time spent on querying OSS inventory information. Unit: milliseconds. |
| data | Struct |   | The returned data. |
| overview | Struct |   | The OSS inventory information. |
| cluster | String | "" | The information about the cluster. |
| disk remain _ | Float | 945318.56 | The free space of the disk. |

| Console Develope rence | r Guide·API Ref |   |   |
|---|---|---|---|

| disk total _ | Float | 119169.43 | The total capacity of the disk. |
|---|---|---|---|
| disk usage _ | Float | 11.195 | The usage of the disk in percentage. |
| disk used _ | Float | 119169.43 | The used space of the disk. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| message | String | "" | The error message. |
| requestId | String | 9ac36287-3ba4- 4f94-a7de- ac14e91d0c1c | The ID of the request. |
| successRespo nse | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getOssInventoryInfo HTTP/1.1 OpsProduct: ASOOps
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": {
        "overview": {
            "cluster": "\"\"",
            "disk_used": "119169.43",
            "disk_total": "119169.43",
            "disk_remain": "945318.56",
            "disk_usage": "11.195"
```

`},`

```json
    "level": "\"\"",
    "requestId": "9ac36287-3ba4-4f94-a7de-ac14e91d0c1c",
    "message": "\"\"",
    "key": "\"\""
```

#### 4.2.6 GetOtsInnerInventoryInfo

Queries Tablestore inventory information.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getOtsInnerInventoryInfo HTTP/1.1
```

**Request parameters**

None

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned code. 200 indicates that the call was successful. |
| cost | Long | 30 | The time spent on querying OTS inventory information. Unit: milliseconds. |
| data | Struct |   | The returned data. |
| overview | Struct |   | The Tablestore inventory information. |

| cluster | String | "" | The information about the cluster. |
|---|---|---|---|
| disk remain _ | Float | 347621.84 | The free space of the disk. |
| disk total _ | Float | 389886 | The total capacity of the disk. |
| disk usage _ | Float | 10.840136 | The usage of the disk in percentage. |
| disk used _ | Float | 42264.17 | The used space of the disk. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| message | String | success | The error message. |
| requestId | String | 466f9e0f-d0a8- 4290-860b- dda9f792e438 | The ID of the request. |
| successRespo nse | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getOtsInnerInventoryInfo HTTP/1.1 OpsProduct: ASOOps
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": {
        "overview": {
            "cluster": "\"\"",
            "disk_used": "42264.17",
            "disk_total": "389886",
            "disk_remain": "347621.84",
            "disk_usage": "10.840136"
```

`},`

```json
    "level": "\"\"",
    "requestId": "466f9e0f-d0a8-4290-860b-dda9f792e438",
    "message": "success",
    "key": "\"\""
```

#### 4.2.7 GetRdsInventoryInfo

Queries ApsaraDB RDS inventory information.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getRdsInventoryInfo HTTP/1.1
```

**Request parameters**

None

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned code. 200 indicates that the call was successful. |
| cost | Long | 30 | The time spent on querying ApsaraDB RDS inventory information. Unit: milliseconds. |
| data | Struct |   | The returned data. |

| engines | Map | {"hawq": {"mem used":"0.0 _ ","cpu used":"0.0", _ "mem usage":"0.0 _ ","disk total":"0.0", _ "disk used":"0.0"," _ disk remain":"0.0", _ "cpu remain":"0.0" _ ,"disk usage":"0.0", _ "mem remain":"0. _ 0","cpu total":"0.0" _ ,"cpu usage":"0.0", _ "mem total":"0.0"} _ } | The information about ApsaraDB RDS inventory on each engine. |
|---|---|---|---|
| overview | Struct |   | The information about the total ApsaraDB RDS inventory. |
| cpu remain _ | Float | 1.0 | The available CPU capacity. |
| cpu total _ | Float | 1.0 | The total CPU capacity. |
| cpu usage _ | Float | 0 | The CPU utilization. |
| cpu used _ | Float | 0 | The used CPU capacity. |
| disk remain _ | Float | 55302 | The free space of the disk. |
| disk total _ | Float | 82826 | The total capacity of the disk. |
| disk usage _ | Float | 33.23232 | The usage of the disk in percentage. |
| disk used _ | Float | 27525 | The used space of the disk. |
| mem remain _ | Float | 100.0 | The available memory size. |
| mem total _ | Float | 200.0 | The total size of memory. |
| mem usage _ | Float | 50.0 | The memory usage in percentage. |
| mem used _ | Float | 100.0 | The amount of used memory. |
| key | String | "" | The keyword of the error. |

| level | String | "" | The error level. |
|---|---|---|---|
| message | String | success | The error message. |
| requestId | String | c6cb0637-40a1- 4ac0-abe7- ad45efc848ac | The ID of the request. |
| successRespo nse | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getRdsInventoryInfo HTTP/1.1 OpsProduct: ASOOps
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": {
        "engines": "{\"hawq\":
{\"mem_used\":\"0.0\",\"cpu_used\":\"0.0\",\"mem_usage\":\"0.0\",\"disk_total\":\"0.0\",\ isk_used\":\"0.0\",\"disk_remain\":\"0.0\",\"cpu_remain\":\"0.0\",\"disk_usage\":\"0.0\", mem_remain\":\"0.0\",\"cpu_total\":\"0.0\",\"cpu_usage\":\"0.0\",\"mem_total\":\"0.0\"}}"
        "overview": {
            "mem_used": "100.0",
            "cpu_used": "0",
            "mem_usage": "50.0",
            "disk_used": "27525",
            "disk_total": "82826",
            "disk_remain": "55302",
            "cpu_remain": "1.0",
            "disk_usage": "33.23232",
            "mem_remain": "100.0",
            "cpu_total": "1.0",
            "cpu_usage": "0",
            "mem_total": "200.0"
```

`},`

```json
    "level": "\"\"",
    "requestId": "c6cb0637-40a1-4ac0-abe7-ad45efc848ac",
    "message": "success",
    "key": "\"\""
```

#### 4.2.8 GetSlsInnerInfo

Queries the Log Service inventory information.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getSlsInnerInfo HTTP/1.1
```

**Request parameters**

None

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The returned code. 200 indicates that the call was successful. |
|---|---|---|---|
| cost | Long | 30 | The time spent on querying the inventory information. Unit: milliseconds. |
| data | Struct |   | The returned data. |
| overview | Struct |   | The information overview. |
| cluster | String | "" | The information about the cluster. |
| disk remain _ | Float | 245040 | The free space of the disk. |
| disk total _ | Float | 266122 | The total capacity of the disk. |
| disk usage _ | Float | 7.9219303 | The usage of the disk in percentage. |
| disk used _ | Float | 21082 | The used space of the disk. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| message | String | success | The error message. |
| requestId | String | aae56eb7-74db- 423b-b563- 18ffd8f249ed | The ID of the request. |
| successRespo nse | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getSlsInnerInfo HTTP/1.1
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": {
        "overview": {
            "cluster": "\"\"",
            "disk_used": "21082",
            "disk_total": "266122",
            "disk_remain": "245040",
            "disk_usage": "7.9219303"
```

`},`

```json
    "level": "\"\"",
    "requestId": "aae56eb7-74db-423b-b563-18ffd8f249ed",
    "message": "success",
    "key": "\"\""
```

### 4.3 Resource management

#### 4.3.1 GetMachineList

Queries physical machines.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getMachineList HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| pageNum | Integer | Quer y | No | 1 | The number of the page to return. |
| pageSize | Integer | Quer y | No | 10 | The number of entries to return on each page. |
| project | String | Quer y | No | oss | The name of the product. |

| cluster | String | Quer y | No | OssHybridClus ter-A- 20211201- 001a | The name of the cluster. |
|---|---|---|---|---|---|
| idc | String | Quer y | No | amtest144 | The data center. |
| OpsProduct | String | Head er | No | ASO | The name of the cloud service. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | [{"machine type fr _ _ om manufacturer": _ "","node group":"", _ "cluster":"ansClust er-A-20220209- 001e","project":"an s","max docker nu _ _ mber":"0","sm na _ me":"VM","action _ params":"","nic inf _ o":"","rack unit id" _ _ :"","spec":" {}","TianjiCluster": "ansCluster-A- 20220209- 001e","ecs region" _ :"","guarantee bra _ ndname":"vm dock _ er","is vm":"true"," _ hostname":"vm010 128008055","hw _ mem":"1331","dat e purchase":"","uni _ form type":"","acti _ on name":"","mod _ el":"","security do _ main":"","state":"G OOD","ip config":"" _ ,"machine type wit _ _ h nic type":"VM"," _ _ npod":"ASW.10GE- 2","vm host tag":"" _ _ ,"big container nu _ _ mber":"0","idc":"a mtest128"}] | The returned data. |
| errorDetail | String | null |   |
| errorMsg | String | null |   |
| pageNum | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 20 | The number of data entries returned on each page. |

| responseCode | String | 200 | The error code. |
|---|---|---|---|
| result | String | success | success indicates that the request succeeded and failed indicates that the request failed. |
| return subCod _ e | String | null | The error message. An empty string is returned if the request is successful. |
| return subMsg _ | String | null | The error details. An empty string is returned if the request is successful. |
| totalRows | Long | 100 | The total number of returned data entries. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getMachineList HTTP/1.1
```

Sample success responses `JSON` format

```json
    "return_subCode": "null",
    "result": "success",
    "data": "
[{\"machine_type_from_manufacturer\":\"\",\"node_group\":\"\",\"cluster\":\"ansCluster- A-20220209- 001e\",\"project\":\"ans\",\"max_docker_number\":\"0\",\"sm_name\":\"VM\",\"action_params :\"\",\"nic_info\":\"\",\"rack_unit_id\":\"\",\"spec\":\" {}\",\"TianjiCluster\":\"ansCluster-A-20220209- 001e\",\"ecs_region\":\"\",\"guarantee_brandname\":\"vm_docker\",\"is_vm\":\"true\",\"hos ame\":\"vm010128008055\",\"hw_mem\":\"1331\",\"date_purchase\":\"\",\"uniform_type\":\"\" "action_name\":\"\",\"model\":\"\",\"security_domain\":\"\",\"state\":\"GOOD\",\"ip_confi ":\"\",\"machine_type_with_nic_type\":\"VM\",\"npod\":\"ASW.10GE- 2\",\"vm_host_tag\":\"\",\"big_container_number\":\"0\",\"idc\":\"amtest128\"}]",
    "return_subMsg": "null",
    "pageSize": "20",
    "errorDetail": "null",
    "totalRows": "100",
    "pageNum": "1",
    "errorMsg": "null",
    "responseCode": "200"
```

#### 4.3.2 GetClusterListByProduct

Queries cluster information of a product.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getClusterListByProduct HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| pageNum | Integer | Quer y | No | 1 | The number of the page to return. |
| pageSize | Integer | Quer y | No | 10 | The number of entries to return on each page. |
| project | String | Quer y | No | oss | The name of the product. |
| OpsProduct | String | Head er | No | ASO | The name of the cloud service. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | {"opsapi": ["opsapiCluster-A- 20220209- 0016"],"baseServic eAll": ["NetworkBaseServ iceCluster-A- 20220209- 0014","StandardCl oudCluster-A- 20220209- 0015"],"ans": ["ansCluster-A- 20220209-001e"]} | The returned data. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| pageNum | Integer | 1 | The page number. |

| pageSize | Integer | 10 | The number of data entries returned on each page. |
|---|---|---|---|
| responseCode | String | 200 | The error code. |
| result | String | success | success indicates that the request succeeded and failed indicates that the request failed. |
| return subCod _ e | String | "" | The error message. An empty string is returned if the request is successful. |
| return subMsg _ | String | "" | The returned error message. An empty string is returned if the request is successful. |
| totalRows | Long | 29 | The total number of returned data entries. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getClusterListByProduct HTTP/1.1
```

Sample success responses `JSON` format

```json
    "return_subCode": "\"\"",
    "result": "success",
    "data": "{\"opsapi\":[\"opsapiCluster-A-20220209-0016\"],\"baseServiceAll\":[\"Netw
orkBaseServiceCluster-A-20220209-0014\",\"StandardCloudCluster-A-20220209-0015\"],\"ans \":[\"ansCluster-A-20220209-001e\"]}",
    "return_subMsg": "\"\"",
    "pageSize": "10",
    "errorDetail": "\"\"",
    "totalRows": "29",
    "pageNum": "1",
    "errorMsg": "\"\"",
    "responseCode": "200"
```

#### 4.3.3 GetProductList

Queries all products.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getProductList HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| OpsProduct | String | Head er | No | ASO | The name of the cloud service. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | [\"ans\",\"asa\",\"as cm\",\"asd\",\"aso\" ,\"astc\",\"baseServ iceAll\",\"buffer\",\" cms\",\"config- assist\",\"ecs\"] | The returned data. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| pageNum | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 10 | The number of data entries returned on each page. |
| responseCode | String | 200 | The error code. |
| result | String | success | success indicates that the request succeeded and failed indicates that the request failed. |
| return subCod _ e | String | null | The error message. An empty string is returned if the request is successful. |
| return subMsg _ | String | null | The returned error message. An empty string is returned if the request is successful. |

| totalRows | Long | 13 | The total number of returned data entries. |
|---|---|---|---|

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getProductList HTTP/1.1 OpsProduct: Common request header
```

Sample success responses `JSON` format

```json
    "return_subCode": "null",
    "result": "success",
    "data": "
[\\\"ans\\\",\\\"asa\\\",\\\"ascm\\\",\\\"asd\\\",\\\"aso\\\",\\\"astc\\\",\\\"baseServic ll\\\",\\\"buffer\\\",\\\"cms\\\",\\\"config-assist\\\",\\\"ecs\\\"]",
    "return_subMsg": "null",
    "pageSize": "10",
    "errorDetail": "\"\"",
    "totalRows": "13",
    "pageNum": "1",
    "errorMsg": "\"\"",
    "responseCode": "200"
```

#### 4.3.4 GetCpuMetrics

Queries the CPU utilization.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Request syntax**

```
GET /openapi/popResource/aso/psm/metrics/cpu HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| action | String | Quer y | Yes | util avg _ | The metric that you want to query. |

| hostname | String | Quer y | Yes | m54a01212.cl oud.a04.amtes t11 | The host name. |
|---|---|---|---|---|---|
| startTime | String | Quer y | Yes | 16383487391 66 | The beginning of the time range to query. |
| endTime | String | Quer y | Yes | 16383523391 66 | The end of the time range to query. |
| interval | String | Quer y | No | 60 | The time interval. Unit: seconds. Default value: 60. |
| OpsProduct | String | Head er | No | ASO | The name of the cloud service. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned code. 200 indicates that the call was successful. |
| cost | Long | 54 | The time spent on querying the memory usage. Unit: milliseconds. |
| data | Map | {"data":{"series": [{"data": [0.4,0.3,0.4,0.3,0.4] ,"name":"util avg" _ }],"categories": [1638352080000,1 638352140000,16 38352200000,163 8352260000,1638 352320000]},"type ":"CPU"} | The returned data. |
| key | String | null | The keyword of the error. |
| level | String | null | The error level. |
| message | String | success | The error message. |
| requestId | String | 201a065d-d03a- 4d33-b9ac- 2d9fba9ec6b9 | The ID of the request. |
| successRespo nse | Boolean | true | true indicates that the call succeeded and false indicates that the call failed. |

**Examples**

Sample requests

```json
GET /openapi/popResource/aso/psm/metrics/cpu HTTP/1.1 OpsProduct: Common request header "action": "", "endTime": "", "hostname": "", "startTime": ""
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "54",
    "data": "{\"data\":{\"series\":[{\"data\":
[0.4,0.3,0.4,0.3,0.4],\"name\":\"util_avg\"}],\"categories\": [1638352080000,1638352140000,1638352200000,1638352260000,1638352320000]},\"type\":\"CPU\"
```

`,`

```json
    "level": "null",
    "requestId": "201a065d-d03a-4d33-b9ac-2d9fba9ec6b9",
    "message": "success",
    "key": "null"
```

#### 4.3.5 GetDiskMetrics

Queries disk usage metrics.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Syntax**

```
GET /openapi/popResource/aso/psm/metrics/disk HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| hostname | String | Quer y | Yes | m54a01212.cl oud.a04.amtes t11 | The host name. |

| startTime | String | Quer y | Yes | 16383487391 66 | The beginning of the time range to query. |
|---|---|---|---|---|---|
| endTime | String | Quer y | Yes | 16383523391 66 | The end of the time range to query. |
| action | String | Quer y | Yes | util avg _ | The metric you want to query. |
| interval | String | Quer y | No | 60 | The time interval. Unit: seconds. Default value: 60. |
| OpsProduct | String | Head er | No | ASO | The name of the cloud service. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned code. 200 indicates that the call was successful. |
| cost | Long | 30 | The time spent on querying disk usage metrics. Unit: milliseconds. |
| data | Map | {"data":{"series": [{"data": [7.8,7.8,7.8,7.8,7.8] ,"name":"util avg" _ }],"categories": [1638348780000,1 638348840000,16 38348900000,163 8348960000,1638 349020000]},"type ":"DISK"} | The returned data. |
| key | String | null | The keyword of the error. |
| level | String | null | The error level. |
| message | String | success | The error message. |
| requestId | String | c1310a2c-56e0- 4ca4-8de0- 87b842a47a9e | The ID of the request. |
| successRespo nse | Boolean | true | true indicates that the call succeeded and false indicates that the call failed. |

**Examples**

Sample requests

```json
GET /openapi/popResource/aso/psm/metrics/disk HTTP/1.1 OpsProduct: Common request header "action": "", "endTime": "", "hostname": "", "startTime": ""
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": "{\"data\":{\"series\":[{\"data\":
[7.8,7.8,7.8,7.8,7.8],\"name\":\"util_avg\"}],\"categories\": [1638348780000,1638348840000,1638348900000,1638348960000,1638349020000]},\"type\":\"DISK\
```

`",`

```json
    "level": "null",
    "requestId": "c1310a2c-56e0-4ca4-8de0-87b842a47a9e",
    "message": "success",
    "key": "null"
```

#### 4.3.6 GetIoMetrics

Queries disk I/O.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Syntax**

```
GET /openapi/popResource/aso/psm/metrics/io HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| hostname | String | Quer y | Yes | m54a01212.cl oud.a04.amtes t11 | The host name. |

| startTime | String | Quer y | Yes | 16383487391 66 | The beginning of the time range to query. |
|---|---|---|---|---|---|
| endTime | String | Quer y | Yes | 16383523391 66 | The end of the time range to query. |
| action | String | Quer y | Yes | util avg _ | The metric you want to query. |
| interval | String | Quer y | No | 60 | The time interval. Unit: seconds. Default value: 60. |
| OpsProduct | String | Head er | No | ASO | The name of the cloud service. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned code. 200 indicates that the call was successful. |
| cost | Long | 30 | The time spent on querying the disk I/O. Unit: milliseconds. |
| data | Map | {"data":{"series": [{"data": [0,0,0,0,0],"name": "util avg"}],"categ _ ories": [1638348780000,1 638348840000,16 38348900000,163 8348960000,1638 349020000,16383 49080000]},"type" :"IO"} | The returned data. |
| key | String | null | The keyword of the error. |
| level | String | null | The error level. |
| message | String | success | The error message. |
| requestId | String | db6ab7b0-f435- 4d2a-80f7- 529750fabf98 | The ID of the request. |
| successRespo nse | Boolean | true | true indicates that the call succeeded and false indicates that the call failed. |

**Examples**

Sample requests

```json
GET /openapi/popResource/aso/psm/metrics/io HTTP/1.1 "hostname": "m54a01212.cloud.a04.amtest11", "startTime": "1638348739166", "endTime": "1638352339166", "action": "util_avg"
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": "{\"data\":{\"series\":[{\"data\":
[0,0,0,0,0],\"name\":\"util_avg\"}],\"categories\": [1638348780000,1638348840000,1638348900000,1638348960000,1638349020000,1638349080000]},\" pe\":\"IO\"}",
    "level": "null",
    "requestId": "db6ab7b0-f435-4d2a-80f7-529750fabf98",
    "message": "success",
    "key": "null"
```

#### 4.3.7 GetLoadMetrics

Queries system load metrics.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Syntax**

```
GET /openapi/popResource/aso/psm/metrics/load HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| hostname | String | Quer y | Yes | m54a01212.cl oud.a04.amtes t11 | The host name. |

| startTime | String | Quer y | Yes | 16383487391 66 | The beginning of the time range to query. |
|---|---|---|---|---|---|
| endTime | String | Quer y | Yes | 16383523391 66 | The end of the time range to query. |
| action | String | Quer y | Yes | load1 avg _ | The metric you want to query. |
| interval | String | Quer y | No | 60 | The time interval. Unit: seconds. Default value: 60. |
| OpsProduct | String | Head er | No | ASO | The name of the cloud service. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned code. 200 indicates that the call was successful. |
| cost | Long | 30 | The time spent on querying system load metrics. Unit: milliseconds. |
| data | Map | {"data":{"series": [{"data": [1.1,1.1,1,1.2,1.4]," name":"load1 avg" _ }],"categories": [1638348780000,1 638348840000,16 38348900000,163 8348960000,1638 349020000]},"type ":"LOAD"} | The returned data. |
| key | String | null | The keyword of the error. |
| level | String | null | The error level. |
| message | String | success | The error message. |
| requestId | String | e15eef8f-69e4- 47fc-ade7- 8274622447d2 | The ID of the request. |
| successRespo nse | Boolean | true | true indicates that the call succeeded and false indicates that the call failed. |

**Examples**

Sample requests

```json
GET /openapi/popResource/aso/psm/metrics/load HTTP/1.1 "hostname": "m54a01212.cloud.a04.amtest11", "startTime": "1638348739166", "endTime": "1638352339166", "action": "load1_avg"
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": "{\"data\":{\"series\":[{\"data\":
[1.1,1.1,1,1.2,1.4],\"name\":\"load1_avg\"}],\"categories\": [1638348780000,1638348840000,1638348900000,1638348960000,1638349020000]},\"type\":\"LOAD\
```

`",`

```json
    "level": "null",
    "requestId": "e15eef8f-69e4-47fc-ade7-8274622447d2",
    "message": "success",
    "key": "null"
```

#### 4.3.8 GetTrafficMetrics

Queries the traffic metrics of a host.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Request syntax**

```
GET /openapi/popResource/aso/psm/metrics/traffic HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| hostname | String | Quer y | Yes | m54a01212.cl oud.a04.amtes t11 | The host name. |

| startTime | String | Quer y | Yes | 16383487391 66 | The beginning of the time range to query. |
|---|---|---|---|---|---|
| endTime | String | Quer y | Yes | 16383523391 66 | The end of the time range to query. |
| action | String | Quer y | Yes | ifin avg _ | The metric that you want to query. |
| interval | String | Quer y | No | 60 | The time interval. Unit: seconds. Default value: 60. |
| OpsProduct | String | Head er | No | ASO | The name of the cloud service. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned code. 200 indicates that the call was successful. |
| cost | Long | 30 | The time spent on querying the traffic metrics. Unit: milliseconds. |
| data | Map | {"data":{"series": [{"data": [2.77,3.08,2.96,2.9 6,2.63],"name":"ifi n avg"}],"categori _ es": [1638348780000,1 638348840000,16 38348900000,163 8348960000,1638 349020000]},"type ":"TRAFFIC"} | The returned data. |
| key | String | null | The keyword of the error. |
| level | String | null | The error level. |
| message | String | success | The error message. |
| requestId | String | 0067966f-d480- 4628-b8c5- a467ea7ffdbf | The ID of the request. |

| successRespo nse | Boolean | true | true indicates that the call succeeded and false indicates that the call failed. |
|---|---|---|---|

**Examples**

Sample requests

```json
GET /openapi/popResource/aso/psm/metrics/traffic HTTP/1.1 OpsProduct: Common request header "action": "", "endTime": "", "hostname": "", "startTime": ""
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": "{\"data\":{\"series\":[{\"data\":
[2.77,3.08,2.96,2.96,2.63],\"name\":\"ifin_avg\"}],\"categories\": [1638348780000,1638348840000,1638348900000,1638348960000,1638349020000]},\"type\":\"TRAFF \"}",
    "level": "null",
    "requestId": "0067966f-d480-4628-b8c5-a467ea7ffdbf",
    "message": "success",
    "key": "null"
```

#### 4.3.9 GetMemMetrics

Queries the memory usage.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Syntax**

```
GET /openapi/popResource/aso/psm/metrics/mem HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|

| hostname | String | Quer y | Yes | m54a01212.cl oud.a04.amtes t11 | The host name. |
|---|---|---|---|---|---|
| startTime | String | Quer y | Yes | 16383487391 66 | The beginning of the time range to query. |
| endTime | String | Quer y | Yes | 16383523391 66 | The end of the time range to query. |
| action | String | Quer y | Yes | util avg _ | The metric you want to query. |
| interval | String | Quer y | No | 60 | The time interval. Unit: seconds. Default value: 60. |
| OpsProduct | String | Head er | No | ASO | The name of the cloud service. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned code. 200 indicates that the call was successful. |
| cost | Long | 30 | The time spent on querying the memory usage. Unit: milliseconds. |
| data | Map | {"data":{"series": [{"data": [10.7,10.7,10.7,10. 7,10.7],"name":"uti l avg"}],"categorie _ s": [1638348780000,1 638348840000,16 38348900000,163 8348960000,1638 349020000]},"type ":"MEM"} | The returned data. |
| key | String | null | The keyword of the error. |
| level | String | null | The error level. |
| message | String | success | The error message. |

| requestId | String | 48b17b90-621a- 460c-92b4- f2fdd376b287 | The ID of the request. |
|---|---|---|---|
| successRespo nse | Boolean | true | true indicates that the call succeeded and false indicates that the call failed. |

**Examples**

Sample requests

```json
GET /openapi/popResource/aso/psm/metrics/mem HTTP/1.1 OpsProduct: Common request header "action": "", "endTime": "", "hostname": "", "startTime": ""
```

Sample success responses `JSON` format

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": "{\"data\":{\"series\":[{\"data\":
[10.7,10.7,10.7,10.7,10.7],\"name\":\"util_avg\"}],\"categories\": [1638348780000,1638348840000,1638348900000,1638348960000,1638349020000]},\"type\":\"MEM\"
```

`,`

```json
    "level": "null",
    "requestId": "48b17b90-621a-460c-92b4-f2fdd376b287",
    "message": "success",
    "key": "null"
```
