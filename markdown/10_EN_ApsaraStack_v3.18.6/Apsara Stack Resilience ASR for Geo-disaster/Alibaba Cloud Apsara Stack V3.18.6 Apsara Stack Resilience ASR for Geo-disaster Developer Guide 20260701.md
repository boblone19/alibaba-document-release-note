---
title: "Apsara Stack Resilience ASR for Geo-disaster Developer Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 360
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Apsara Stack Resilience ASR for Geo-disaster Developer Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%BC%82%E5%9C%B0%E5%AE%B9%E7%81%BEASRDR/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20Stack%20Resilience%20ASR%C2%A0for%C2%A0Geo-disaster%20Developer%20Guide%2020260701.pdf"
converter: line-classifier (PyMuPDF)
---

# Apsara Stack Resilience ASR for Geo-disaster Developer Guide 20260701

Apsara Stack Resilience ASR for Geo-disaster Developer

## Procedure for API calls

You can use the POP gateway to call API operations in ASR for Geo-disaster Recovery.

**Flowchart**

The following figure shows the flowchart for calling API operations in ASR for Geo-disaster Recovery.
1. Obtain API information.
For more information, see API Reference.
2. Obtain the AccessKey ID and AccessKey secret. For more information, see Obtain an
AccessKey pair.
3. Obtain the endpoint of ASR for Geo-disaster Recovery. For more information, see Obtain the
information and the endpoint of an API operation.
4. Obtain the region ID of ASR for Geo-disaster Recovery. For more information, see Obtain a
region ID.
5. Obtain the ASR for Geo-disaster Recovery SDK and SDK core library. For more information,
see Obtain the SDK package.
6. Call API operations in ASR for Geo-disaster Recovery.

**Note**

Only users who are granted the permissions of the operations administrator, organization administrator, global disaster recovery administrator, or organization disaster recovery administrator role can call API operations in ASR for Geo-disaster Recovery. ASR for Geo-disaster Developer Apsara Stack Resilience

## Preparations

### Obtain an AccessKey pair

This topic describes how to obtain an AccessKey ID and an AccessKey secret.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is a string that is used to encrypt a signature.

**Usage notes**

The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. We recommend that you use the AccessKey pairs of personal accounts to call API operations.

**Note**

Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations.

**If you need to obtain the AccessKey pair of your**

**personal account, make sure that the personal account**

**is assigned one of the following roles: operations**

**administrator, organization administrator, global**

**disaster recovery administrator, and organization**

**disaster recovery administrator. Otherwise, you may fail**

**to call API operations.**

**Obtain the AccessKey pair of a personal account**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, click the profile picture and select **User**
**Information**.
3. In the ****************** section, view the AccessKey ID and AccessKey secret of the
personal account.

**Important**

The AccessKey pair provides full access to cloud resources within your Apsara Stack tenant account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

Apsara Stack Resilience ASR for Geo-disaster Developer

**Warning**

The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. Click **Management AccessKey** on the right side of the page.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### Obtain the information and

**the endpoint of an API operation**

To call an API operation, you must obtain the information about the operation, including the service code, operation name, and API version.

**Background information**

The API information on the debugging page of the Apsara Uni-manager Management Console is for reference only. For more information about how to call API operations, see the ASR for Geo-disaster Recovery Developer Guide. If the information on the API Directory page is different from the information in the developer guide of a cloud service, the information in the developer guide takes precedence.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Development Tools > OpenAPI Explorer**
**> OpenAPI Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging**.
4. In the left-side navigation pane, select **ASR**.
5. Select an API version from the **Version** drop-down list.
6. In the API list, you can view all API operations of the current version.
7. Click the operation that you want to call. Obtain the information such as endpoint and
region ID on the Parameter tab. ASR for Geo-disaster Developer Apsara Stack Resilience

### Obtain an SDK

If you want to call the API operations of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) by using the POP gateway, you must obtain the SDK core library from SDK Center and integrate the SDK dependencies of ASR-DR. Obtain the SDK core library: Go to SDK Center and download the **SDK core library** for your programming language. Integrate the SDK dependencies of ASR-DR: For more information, see the documentation of Alibaba Cloud SDKs.

**Note**

We recommend that you use the SDK core library that is provided on the Alibaba Cloud official website. The SDK core library is shared by all cloud services and is compatible with Apsara Stack. ASR-DR SDK supports Java. Apsara Stack Resilience ASR for Geo-disaster Developer

## Use the SDK for Java

### Install the SDK for Java

This topic describes how to install Apsara Stack Resilience for Geo-disaster Recovery (ASR- DR) SDK for Java.

**Prerequisites**

Java Development Kit (JDK) 1.8 or later is installed.

**Install Apsara Stack SDK for Java**

If you use Apache Maven to manage a Java project, you need to only import the JAR files of Apsara Stack SDK for Java to the pom.xml file of the project. To call the SDK for Java, you must install the SDK core library and integrate the SDK dependencies of ASR-DR. We recommend that you use the SDK core library V4.5.17 or later and use the SDK for Java V1.0.0. The following sample code configures the pom.xml file for the SDK for Java:

```xml
<dependencies>
    <!--Required dependencies-->
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-asrdr</artifactId>
        <version>1.0.0</version>
    </dependency>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-core</artifactId>
        <version>4.6.0</version>
    </dependency>
</dependencies>
```

### Configure authentication

**credentials**

When you use Apsara Stack SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for identity verification. If you use the SDK for Java, you can use an AccessKey pair for identity verification. For more information about how to obtain an AccessKey ID and an AccessKey secret, an endpoint, and a region ID, see Obtain an AccessKey pair, Obtain an endpoint, and Obtain a region ID. If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as the credentials when you initialize the client.

**Important**

Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be exposed to risks. ASR for Geo-disaster Developer Apsara Stack Resilience

```
// Configure the endpoint of the API. DefaultProfile.addEndpoint(
    "<EndpointName>",    // The name of the endpoint. Example: Asrdr.
    "<RegionId>",      // The region ID.
    "<ProductCode>",     // The code of the cloud service. Example: Asrdr.
    "<Endpoint>"        // The endpoint of the cloud service.
); // Configure authentication credentials. DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",         // The region ID.
    "<yourAccessKeyID>",      // The AccessKey ID of your personal account.
    "<yourAccessKeySecret>",  // The AccessKey secret of your personal account.
);
```

**Note**

In the preceding sample code, replace the variables `<yourRegionID>` , `<yourAccessKeyID>` , and `<yourAccessKeySecret>` with actual values and remove the angle brackets (<>) from the code. You must call the API operations of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) as a user that is assigned one of the following roles: operations administrator, organization administrator, global disaster recovery administrator, and organization disaster recovery administrator.

### Initiate a request

This topic describes how to use the SDK for Java to initiate a request.
1. Create an AcsClient instance.

```
DefaultAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
Name the request in the ${apiName}Request format. Replace **${apiName}** with the name of the API operation that you want to call, such as DescribeBackupCloud.

```
DescribeBackupCloudRequest request = new DescribeBackupCloudRequest();
```

3. Initiate the request and obtain a response.

```java
// Initiate the request and view the response. DescribeBackupCloudResponse response = client.getAcsResponse(request); System.out.println(response.getData());
```

**Complete sample code**

The following sample code calls the `DescribeBackupCloud` operation of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR): Apsara Stack Resilience ASR for Geo-disaster Developer

```java
import com.aliyuncs.asrdr.model.v20220209.*; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.http.MethodType; import com.chenxue.product.api.base.ApiBaseInfo; import com.chenxue.product.api.base.ProductBaseApi; import com.google.gson.Gson; import org.slf4j.Logger; import org.slf4j.LoggerFactory; public class AsrdrApi extends ProductBaseApi {
    public void listPlanInstance(String planId, ApiBaseInfo apiBaseInfo) throws ClientE
xception {
      try {
        // Configure the endpoint of the API.
        DefaultProfile.addEndpoint(
            "<EndpointName>",    // The name of the endpoint. Example: Asrdr.
            "<RegionId>",      // The region ID.
            "<ProductCode>",     // The code of the cloud service. Example: Asrdr.
            "<Endpoint>"        // The endpoint of the cloud service.
        );
        // Configure authentication credentials.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",         // The region ID.
            "<yourAccessKeyID>",      // The AccessKey ID of your personal account.
            "<yourAccessKeySecret>",  // The AccessKey secret of your personal account.
        );
        // Construct the client.
        DefaultAcsClient client = new DefaultAcsClient(profile);
        //Construct request parameters.
        DescribeBackupCloudRequest request = new DescribeBackupCloudRequest();
        request.setMethod(MethodType.GET);
        request.setVersion("2022-02-09");
        request.setActionName("DescribeBackupCloud");
        // Call the API operation.
        DescribeBackupCloudResponse response = client.getAcsResponse(request);
        System.out.println(response.getData());
      }
    }
}
```

### Handle exceptions

If the server or client encounters an exception when you use the SDK for Java, the SDK returns the exception information. The exception information contains an error code and an error message. In most cases, you do not need to handle exceptions based on the exception information returned by the SDK for Java. You need to only handle server exceptions based on error messages generated on the server side. ServerException indicates a server exception. ASR for Geo-disaster Developer Apsara Stack Resilience ClientException indicates a client exception. For example, when the following exception occurs, you can modify the AccessKey ID based on the error message:

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

If you want to handle exceptions based on the exception information returned by the SDK for Java, you can use the following sample code:

```java
try {
    AcsResponse response = client.getAcsResponse(request);
    // Handle the response.
    // ...
} catch (ClientException e) {
    // Add your logic for handling exceptions.
    // For example, you can display the exception information.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    e.printStackTrace();
} catch (ServerException e) {
    e.printStackTrace();
}
```

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of ASR-DR. You do not need to specify this parameter. |
| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. You do not need to specify this parameter. |

Apsara Stack Resilience ASR for Geo-disaster Developer

## API reference

### Cloud instances

#### Cloud instance management

##### ListSupportProducts

Queries the cloud services that are supported by Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) in a region.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is a parameter of the Apsara Stack API (ASAPI). You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is a parameter of the Apsara Stack API. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is a parameter of the Apsara Stack API. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| CloudInsta nceId | Strin g | Quer y | Yes | ffe1********6d6d | The ID of the cloud instance. |
| RgnId | Strin g | Quer y | Yes | cn *** 01 _ _ | The region ID. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | ["RDS", "ECS"] | The cloud services that are supported by ASR-DR. |
| requestId | String | 75ef********dafe8 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
| success | Boolean | true | Indicates whether the request was successful. |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y1***R- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListSupportProducts &CloudInstanceId=ffe1********6d6d &RgnId=cn_***_01 &<Common request parameters>
```

Sample success responses `JSON` format

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8*****04bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). You do not need to specify this parameter. |
| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. You do not need to specify this parameter. |

ASR for Geo-disaster Developer Apsara Stack Resilience

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y1***R-1914.local",
 "code":"200",
 "data":"[\"RDS\", \"ECS\"]",
 "requestId":"75ef********dafe8",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y1***R-1914.local</nodeHost> <code>200</code> <data>[&quot;RDS&quot;, &quot;ECS&quot;]</data> <requestId>75ef********dafe8</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### DescribeCloudInstance

Queries the information about a cloud instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is a parameter of the Apsara Stack API (ASAPI). You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter is used to specify the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is a parameter of the Apsara Stack API. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is a parameter of the Apsara Stack API. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| CloudInsta nceId | Strin g | Quer y | Yes | ffe1********6d6d | The ID of the cloud instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| requestId | String | b870********433d | The request ID. |
|---|---|---|---|
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
| success | Boolean | true | Indicates whether the request was successful. |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y***6R- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The information about the resource. |
| - aliyunAccount Uid | String | 178511195726779 6 | The unique ID (UID) of the Apsara Stack tenant account to which the resource belongs. |
| -ownerUid | String | 239724*****88687 32 | The UID of the resource owner. |
| -creator | String | 2397245****88687 32 | The UID of the user who created the resource. |
| -lastModifier | String | 23972451****6873 2 | The UID of the user who last modified the resource. |
| - resourceRegio nId | String | cn-hangzhou | The region ID of the resource. |
| - resourceGroup Id | String | 103 | The ID of the resource group to which the resource belongs. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| -createdDate | Long | 1713514782222 | The time when the resource was created. |
|---|---|---|---|
| - lastModifiedDa te | Long | 1713514782222 | The time when the resource was last modified. |
| -instanceId | String | e25***8c-a02a- 455c-b957- 8dc****4ef58 | The instance ID of the resource. |
| - instanceName | String | XXX | The instance name of the resource. |
| -pk | String | 339944229200627 712 | The primary key of the cloud instance. |
| -cloudUniqueId | String | 0179 | The UID of the cloud. |
| -cloudOsType | String | ENTERPRISE | The edition of the cloud instance. Only ENTERPRISE may be returned, which indicates Apsara Stack. |
| -version | String | 1.0.0 | The version number of the cloud instance. |
| -consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. This type is generally used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. This type is generally used in cross- cloud disaster recovery scenarios. |
| - consoleApiEnd point | String | http://internal.API.c n-XXXXXXX | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| - adminCredenti alsId | String | **************32 32 | The credential ID of the cloud management administrator. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of an operations administrator. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as the operations administrator, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |
|---|---|---|---|
| - accountCrede ntialsId | String | **************72 00 | The credential ID of the organization account. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of a level-1 organization. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as an organization administrator. In the top navigation bar, click Enterprise. In the left-side navigation pane, choose Resources > Organizations. On the page that appears, obtain an AccessKey pair of a level-1 organization. |
| - internetDomai n | String | inter.example.com | The Internet domain name. |
| - intranetDomai n | String | intra.example.com | The internal domain name. |
| -status | String | REGULAR | The state of the cloud instance. Valid values: REGULAR: normal. NOT CONFIGURED: not configured. _ UNINITIALIZED: not initialized. The cloud instance is in this state if no administrator credentials are configured when you log on to ASR-DR for the first time. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCloudInstance &CloudInstanceId=ffe1********6d6d &<Common request parameters>
```

Apsara Stack Resilience ASR for Geo-disaster Developer Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y***6R-1914.local",
 "code":"200",
 "data":{
  "cloudUniqueId":"0179",
  "creator":"2397245****8868732",
  "lastModifiedDate":1713514782222,
  "instanceName":"XXX",
  "consoleApiEndpoint":"http://internal.API.cn-XXXXXXX",
  "resourceRegionId":"cn-hangzhou",
  "lastModifier":"23972451****68732",
  "adminCredentialsId":"3399442255****3232",
  "version":"1.0.0",
  "cloudOsType":"ENTERPRISE",
  "createdDate":1713514782222,
  "instanceId":"e25***8c-a02a-455c-b957-8dc****4ef58",
  "aliyunAccountUid":"1785111957267796",
  "internetDomain":"inter.example.com",
  "resourceGroupId":"103",
  "pk":"339944229200627712",
  "intranetDomain":"intra.example.com",
  "ownerUid":"239724*****8868732",
  "accountCredentialsId":"3399442290****7200",
  "consoleType":"ASCM",
  "status":"REGULAR"
 },
 "requestId":"b870********433d",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y***6R-1914.local</nodeHost> <code>200</code> <data>
 <cloudUniqueId>0179</cloudUniqueId>
 <creator>2397245****8868732</creator>
 <lastModifiedDate>1713514782222</lastModifiedDate>
 <instanceName>XXX</instanceName>
 <consoleApiEndpoint>http://internal.API.cn-XXXXXXX</consoleApiEndpoint>
 <resourceRegionId>cn-hangzhou</resourceRegionId>
 <lastModifier>23972451****68732</lastModifier>
 <adminCredentialsId>3399442255****3232</adminCredentialsId>
 <version>1.0.0</version>
 <cloudOsType>ENTERPRISE</cloudOsType>
 <createdDate>1713514782222</createdDate>
 <instanceId>e25***8c-a02a-455c-b957-8dc****4ef58</instanceId>
 <aliyunAccountUid>1785111957267796</aliyunAccountUid>
 <internetDomain>inter.example.com</internetDomain>
 <resourceGroupId>103</resourceGroupId>
 <pk>339944229200627712</pk>
 <intranetDomain>intra.example.com</intranetDomain>
 <ownerUid>239724*****8868732</ownerUid>
 <accountCredentialsId>3399442290****7200</accountCredentialsId>
 <consoleType>ASCM</consoleType>
 <status>REGULAR</status>
</data> <requestId>b870********433d</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### DescribeCloudCredentials

Queries various credentials of a cloud instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). You do not need to specify this parameter. |
|---|---|---|---|---|---|
| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. You do not need to specify this parameter. |
| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is a parameter of the Apsara Stack API (ASAPI). You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter is used to specify the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. |

Apsara Stack Resilience ASR for Geo-disaster Developer

|  |  |  |  |  | When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is a parameter of the Apsara Stack API. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is a parameter of the Apsara Stack API. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| CloudInsta nceId | Strin g | Quer y | Yes | ffe1********6d6d | The ID of the cloud instance. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Credential sLevel | Strin g | Quer y | Yes | user | The level of the credentials. Valid values: user: the credentials of a Resource Access Management (RAM) user. account: the credentials of a Apsara Stack tenant account. admin: the credentials of an operations administrator. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | b870********433d | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
| success | Boolean | ture | Indicates whether the request was successful. |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y***6R- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The credentials of the cloud instance. |
| - aliyunAccount Uid | String | 1785111***67796 | The unique ID (UID) of the Apsara Stack tenant account to which the resource belongs. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| -ownerUid | String | 2397****18988687 32 | The UID of the resource owner. |
|---|---|---|---|
| -creator | String | 2397****18988687 32 | The UID of the user who created the resource. |
| - resourceRegio nId | String | 2397****18988687 32 | The region ID of the resource. |
| - resourceGroup Id | String | 103 | The ID of the resource group to which the resource belongs. |
| -createdDate | Long | 1713514782222 | The time when the resource was created. |
| - lastModifiedDa te | Long | 1713514782222 | The time when the resource was last modified. |
| -id | String | 339944*****31872 00 | The credential ID of the organization account. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of a level-1 organization. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as an organization administrator. In the top navigation bar, click Enterprise. In the left-side navigation pane, choose Resources > Organizations. On the page that appears, obtain an AccessKey pair of a level-1 organization. |
| -type | String | security-token | The type of the credentials. Valid values: access-key: AccessKey ID & AccessKey Secret security-token: STS Token |
| -accessKeyId | String | AC4Gr9N****77grR | The AccessKey ID. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| - accessKeySecr et | String | cTJNbuS*****TVwy KkV5I | The AccessKey secret. The value is masked and cannot be directly used. |
|---|---|---|---|
| -securityToken | String | cTJNbuS3qE2****** **wyKkV5I | The STS token. The value is masked and cannot be directly used. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCloudCredentials &CloudInstanceId=ffe1********6d6d &CredentialsLevel=user &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y***6R-1914.local",
 "code":"200",
 "data":{
  "accessKeyId":"AC4Gr9N****77grR",
  "securityToken":"cTJNbuS3qE2********wyKkV5I",
  "creator":"2397****1898868732",
  "accessKeySecret":"cTJNbuS*****TVwyKkV5I",
  "createdDate":1713514782222,
  "lastModifiedDate":1713514782222,
  "aliyunAccountUid":"1785111***67796",
  "resourceRegionId":"2397****1898868732",
  "resourceGroupId":"103",
  "id":"339944*****3187200",
  "ownerUid":"2397****1898868732",
  "type":"security-token"
 },
 "requestId":"b870********433d",
 "success":false,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9*****bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). You do not need to specify this parameter. |
| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. You do not need to specify this parameter. |

ASR for Geo-disaster Developer Apsara Stack Resilience

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y***6R-1914.local</nodeHost> <code>200</code> <data>
 <accessKeyId>AC4Gr9N****77grR</accessKeyId>
 <securityToken>cTJNbuS3qE2********wyKkV5I</securityToken>
 <creator>2397****1898868732</creator>
 <accessKeySecret>cTJNbuS*****TVwyKkV5I</accessKeySecret>
 <createdDate>1713514782222</createdDate>
 <lastModifiedDate>1713514782222</lastModifiedDate>
 <aliyunAccountUid>1785111***67796</aliyunAccountUid>
 <resourceRegionId>2397****1898868732</resourceRegionId>
 <resourceGroupId>103</resourceGroupId>
 <id>339944*****3187200</id>
 <ownerUid>2397****1898868732</ownerUid>
 <type>security-token</type>
</data> <requestId>b870********433d</requestId> <success>false</success> <nodeIp>127.0.0.1</nodeIp>
```

##### SaveCloudCredentials

Saves the credentials of a cloud instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| CloudInsta nceId | Strin g | Body | Yes | ffe1********6d6 | The ID of the cloud instance. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Credential sLevel | Strin g | Body | Yes | user | The level of the credentials. Set the value to user . |
|---|---|---|---|---|---|
| Credential sAccessKe yId | Strin g | Body | Yes | AC4Gr9N***7grR | The AccessKey ID of your personal account. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as a regular user, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |
| Credential sAccessKe ySecret | Strin g | Body | Yes | *******************HTV wyKkV5I | The AccessKey secret of your personal account. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as a regular user, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | b870********433d | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
| success | Boolean | true | Indicates whether the request was successful. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Response parameters**

| code | String | 200 | The response code. |
|---|---|---|---|
| nodeHost | String | B-W0Y***6R- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The credentials of the cloud instance. |
| - aliyunAccount Uid | String | 1785111***67796 | The unique ID (UID) of the Apsara Stack tenant account to which the resource belongs. |
| -ownerUid | String | 2397****18988687 32 | The UID of the resource owner. |
| -creator | String | 2397****18988687 32 | The UID of the user who created the resource. |
| - resourceRegio nId | String | region 01 _ | The region ID of the resource. |
| - resourceGroup Id | String | 103 | The ID of the resource group to which the resource belongs. |
| -createdDate | Long | 1713514782222 | The time when the resource was created. |
| - lastModifiedDa te | Long | 1713514782222 | The time when the resource was last modified. |
| -id | String | 339944229******2 00 | The ID of the credentials. |
| -type | String | security-token | The type of the credentials. Valid values: access-key: AccessKey ID and AccessKey secret. security-token: Security Token Service (STS) token. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| -accessKeyId | String | CU********Yh | The AccessKey ID. |
|---|---|---|---|
| - accessKeySecr et | String | ClHm********Xxqf | The AccessKey secret. The value is masked and cannot be directly used. |
| -securityToken | String | cTJNbu********rQj4 WwHTVwyKkV5I | The STS token. The value is masked and cannot be directly used. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SaveCloudCredentials &****************************6d6 &CredentialsLevel=user &*********************************7grR &**********************************************HTVwyKkV5I &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y***6R-1914.local",
 "code":"200",
 "data":{
  "accessKeyId":"CU********Yh",
  "securityToken":"cTJNbu********rQj4WwHTVwyKkV5I",
  "creator":"2397****1898868732",
  "accessKeySecret":"ClHm********Xxqf",
  "createdDate":1713514782222,
  "lastModifiedDate":1713514782222,
  "aliyunAccountUid":"1785111***67796",
  "resourceRegionId":"region_01",
  "resourceGroupId":"103",
  "id":"339944229******200",
  "ownerUid":"2397****1898868732",
  "type":"security-token"
 },
 "requestId":"b870********433d",
 "success":"",
 "nodeIp":"127.0.0.1"
}
```

`XML` format

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). You do not need to specify this parameter. |
| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. You do not need to specify this parameter. |

Apsara Stack Resilience ASR for Geo-disaster Developer

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y***6R-1914.local</nodeHost> <code>200</code> <data>
 <accessKeyId>CU********Yh</accessKeyId>
 <securityToken>cTJNbu********rQj4WwHTVwyKkV5I</securityToken>
 <creator>2397****1898868732</creator>
 <accessKeySecret>ClHm********Xxqf</accessKeySecret>
 <createdDate>1713514782222</createdDate>
 <lastModifiedDate>1713514782222</lastModifiedDate>
 <aliyunAccountUid>1785111***67796</aliyunAccountUid>
 <resourceRegionId>region_01</resourceRegionId>
 <resourceGroupId>103</resourceGroupId>
 <id>339944229******200</id>
 <ownerUid>2397****1898868732</ownerUid>
 <type>security-token</type>
</data> <requestId>b870********433d</requestId> <success /> <nodeIp>127.0.0.1</nodeIp>
```

##### DescribeCloudInstanceByPage

Queries cloud instances by page.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| InstanceN ame | Strin g | Quer y | No | XXX | The name of the cloud instance that you want to query. This parameter is used to query data in fuzzy match mode. The value is not case- sensitive. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| psara Stack R | esilienc | e |  | ASR | for Geo-disaster Developer Guide·API referenc |
|---|---|---|---|---|---|

| InstanceId | Strin g | Quer y | No | 383********53c7 | The ID of the cloud instance that you want to query. This parameter is used to query data in exact match mode. |
|---|---|---|---|---|---|
| Status | Strin g | Quer y | No | REGULAR | The state of the cloud instance that you want to query. This parameter is used to query data in exact match mode. You can specify one or more states. Separate multiple states with commas ( , ). |
| PageNum | Integ er | Quer y | Yes | 55 | The page number. Pages start from page 1. |
| PageSize | Integ er | Quer y | Yes | 5 | The number of entries per page. |
| Sort | Strin g | Quer y | No | createdDate | The criterion by which cloud instances are sorted. Set the value to createdDate. |
| Order | Strin g | Quer y | No | DESC | The order in which cloud instances are sorted. Valid values: DESC: descending order. This is the default value. ASC: ascending order. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | 4383********53c7 | The request ID. |

**Response parameters**

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y****R- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The information about the resource. |
| -rows | Array |  | The queried entries. |
| -- aliyunAccount Uid | String | 1785111***67796 | The ID of the Apsara Stack tenant account to which the resource belongs. |
| --ownerUid | String | 2397****18988687 32 | The unique ID (UID) of the resource owner. |
| --creator | String | 2397****18988687 32 | The UID of the user who created the resource. |
| --lastModifier | String | 2397****18988687 32 | The UID of the user who last modified the resource. |
| -- resourceRegio nId | String | region 01 _ | The region ID of the resource. |
| -- resourceGroup Id | String | 103 | The ID of the resource group to which the resource belongs. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| --createdDate | Long | 1713514782222 | The time when the resource was created. |
|---|---|---|---|
| -- lastModifiedDa te | Long | 1713514782222 | The time when the resource was last modified. |
| --instanceId | String | ffe1********6d6 | The ID of the cloud instance. |
| -- instanceName | String | OSS1 | The name of the cloud instance. |
| --pk | String | 339944******6277 12 | The primary key of the cloud instance. |
| -- cloudUniqueId | String | 0179 | The UID of the cloud. |
| --cloudOsType | String | ENTERPRISE | The edition of the cloud instance. Only ENTERPRISE may be returned, which indicates Apsara Stack. |
| --version | String | 1.0.0 | The version number of the cloud instance. |
| --consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. This type is generally used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. This type is generally used in cross- cloud disaster recovery scenarios. |
| -- consoleApiEnd point | String | http://internal.API- XXXXXX | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| -- adminCredenti alsId | String | 339944225551583 232 | The credential ID of the cloud management administrator. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of an operations administrator. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as the operations administrator, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |
|---|---|---|---|
| -- accountCrede ntialsId | String | 339944229083187 200 | The credential ID of the organization account. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of a level-1 organization. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as an organization administrator. In the top navigation bar, click Enterprise. In the left-side navigation pane, choose Resources > Organizations. On the page that appears, obtain an AccessKey pair of a level-1 organization. |
| -- internetDomai n | String | inter.example.com | The Internet domain name. |
| -- intranetDomai n | String | intra.example.com | The internal domain name. |
| --status | String | REGULAR | The status of the cloud instance. Valid values: REGULAR: normal. NOT CONFIGURED: not configured. _ UNINITIALIZED: not initialized. The cloud instance is in this state if no administrator credentials are configured when you log on to ASR-DR for the first time. |
| -pageNum | Integer | 4 | The page number. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| -pageSize | Integer | 5 | The number of entries per page. This parameter indicates the expected number of entries per page. The value is the same as the value of the corresponding parameter specified in the request. If the actual length of the returned rows parameter is less than the value of this parameter, the last page is returned. |
|---|---|---|---|
| -total | Integer | 20 | The total number of entries that meet query conditions. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCloudInstanceByPage &PageNum=55 &PageSize=5 &<Common request parameters>
```

Sample success responses `JSON` format ASR for Geo-disaster Developer Apsara Stack Resilience

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****R-1914.local",
 "code":"200",
 "data":{
  "total":20,
  "-rows":{
   "cloudUniqueId":"0179",
   "creator":"2397****1898868732",
   "lastModifiedDate":1713514782222,
   "instanceName":"OSS1",
   "consoleApiEndpoint":"http://internal.API-XXXXXX",
   "resourceRegionId":"region_01",
   "lastModifier":"2397****1898868732",
   "adminCredentialsId":"339944225551583232",
   "version":"1.0.0",
   "cloudOsType":"ENTERPRISE",
   "createdDate":1713514782222,
   "instanceId":"ffe1********6d6",
   "aliyunAccountUid":"1785111***67796",
   "internetDomain":"inter.example.com",
   "resourceGroupId":"103",
   "pk":"339944******627712",
   "intranetDomain":"intra.example.com",
   "ownerUid":"2397****1898868732",
   "accountCredentialsId":"339944229083187200",
   "consoleType":"ASCM",
   "status":"REGULAR"
  },
  "pageSize":5,
  "pageNum":4
 },
 "requestId":"4383********53c7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****R-1914.local</nodeHost> <code>200</code> <data>
 <total>20</total>
 <-rows>
  <cloudUniqueId>0179</cloudUniqueId>
  <creator>2397****1898868732</creator>
  <lastModifiedDate>1713514782222</lastModifiedDate>
  <instanceName>OSS1</instanceName>
  <consoleApiEndpoint>http://internal.API-XXXXXX</consoleApiEndpoint>
  <resourceRegionId>region_01</resourceRegionId>
  <lastModifier>2397****1898868732</lastModifier>
  <adminCredentialsId>339944225551583232</adminCredentialsId>
  <version>1.0.0</version>
  <cloudOsType>ENTERPRISE</cloudOsType>
  <createdDate>1713514782222</createdDate>
  <instanceId>ffe1********6d6</instanceId>
  <aliyunAccountUid>1785111***67796</aliyunAccountUid>
  <internetDomain>inter.example.com</internetDomain>
  <resourceGroupId>103</resourceGroupId>
  <pk>339944******627712</pk>
  <intranetDomain>intra.example.com</intranetDomain>
  <ownerUid>2397****1898868732</ownerUid>
  <accountCredentialsId>339944229083187200</accountCredentialsId>
  <consoleType>ASCM</consoleType>
  <status>REGULAR</status>
 </-rows>
 <pageSize>5</pageSize>
 <pageNum>4</pageNum>
</data> <requestId>4383********53c7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### DescribeLocalCloudInstance

Queries the information about the cloud instance that corresponds to the cloud on which Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) is deployed.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9*****bca | The ID of the primary cloud instance. This is a common parameter of ASR-DR. You do not need to specify this parameter. |
|---|---|---|---|---|---|
| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. You do not need to specify this parameter. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | b870********433d | The request ID. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y***6R- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The information about the resource. |
| - aliyunAccount Uid | String | 17851119****7796 | The ID of the Apsara Stack tenant account to which the resource belongs. |
| -ownerUid | String | 2397245*****8687 32 | The unique ID (UID) of the resource owner. |
| -creator | String | 2397245*****8687 32 | The UID of the user who created the resource. |
| -lastModifier | String | 2397245*****8687 32 | The UID of the user who last modified the resource. |
| - resourceRegio nId | String | cn-hangzhou | The region ID of the resource. |
| - resourceGroup Id | String | 103 | The ID of the resource group to which the resource belongs. |
| -createdDate | Long | 1713514782222 | The time when the resource was created. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| - lastModifiedDa te | Long | 1713514782222 | The time when the resource was last modified. |
|---|---|---|---|
| -instanceId | String | e250008c-a02a- 455c-****- 8dcb6ea4ef58 | The ID of the cloud instance. |
| - instanceName | String | XXX | The name of the cloud instance. |
| -pk | String | 339****292006277 12 | The primary key of the cloud instance. |
| -cloudUniqueId | String | 0179 | The UID of the cloud. |
| -cloudOsType | String | ENTERPRISE | The edition of the cloud instance. Only ENTERPRISE may be returned, which indicates Apsara Stack. |
| -version | String | 1.0.0 | The version number of the cloud instance. |
| -consoleType | String | ASRDR | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |
| - consoleApiEnd point | String | http://internal.API- XXXXXX | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| - adminCredenti alsId | String | *************832 32 | The credential ID of the cloud management administrator. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of an operations administrator. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as the operations administrator, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |
|---|---|---|---|
| - accountCrede ntialsId | String | *************832 32 | The credential ID of the organization account. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of a level-1 organization. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as an organization administrator. In the top navigation bar, click Enterprise. In the left-side navigation pane, choose Resources > Organizations. On the page that appears, obtain an AccessKey pair of a level-1 organization. |
| - internetDomai n | String | inter.example.com | The Internet domain name. |
| - intranetDomai n | String | intra.example.com | The internal domain name. |
| -status | String | REGULAR | The status of the cloud instance. Valid values: REGULAR: normal. NOT CONFIGURED: not configured. _ UNINITIALIZED: not initialized. The cloud instance is in this state if no administrator credentials are configured when you log on to ASR-DR for the first time. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLocalCloudInstance &<Common request parameters>
```

Apsara Stack Resilience ASR for Geo-disaster Developer Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y***6R-1914.local",
 "code":"200",
 "data":{
  "cloudUniqueId":"0179",
  "creator":"2397245*****868732",
  "lastModifiedDate":1713514782222,
  "instanceName":"XXX",
  "consoleApiEndpoint":"http://internal.API-XXXXXX",
  "resourceRegionId":"cn-hangzhou",
  "lastModifier":"2397245*****868732",
  "adminCredentialsId":"339944225****83232",
  "version":"1.0.0",
  "cloudOsType":"ENTERPRISE",
  "createdDate":1713514782222,
  "instanceId":"e250008c-a02a-455c-****-8dcb6ea4ef58",
  "aliyunAccountUid":"17851119****7796",
  "internetDomain":"inter.example.com",
  "resourceGroupId":"103",
  "pk":"339****29200627712",
  "intranetDomain":"intra.example.com",
  "ownerUid":"2397245*****868732",
  "accountCredentialsId":"339944225****83232",
  "consoleType":"ASRDR",
  "status":"REGULAR"
 },
 "requestId":"b870********433d",
 "success":"",
 "nodeIp":"127.0.0.1"
}
```

`XML` format

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a*****04bca | The ID of the primary cloud instance. This is a common parameter of ASR-DR. You do not need to specify this parameter. |

ASR for Geo-disaster Developer Apsara Stack Resilience

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y***6R-1914.local</nodeHost> <code>200</code> <data>
 <cloudUniqueId>0179</cloudUniqueId>
 <creator>2397245*****868732</creator>
 <lastModifiedDate>1713514782222</lastModifiedDate>
 <instanceName>XXX</instanceName>
 <consoleApiEndpoint>http://internal.API-XXXXXX</consoleApiEndpoint>
 <resourceRegionId>cn-hangzhou</resourceRegionId>
 <lastModifier>2397245*****868732</lastModifier>
 <adminCredentialsId>339944225****83232</adminCredentialsId>
 <version>1.0.0</version>
 <cloudOsType>ENTERPRISE</cloudOsType>
 <createdDate>1713514782222</createdDate>
 <instanceId>e250008c-a02a-455c-****-8dcb6ea4ef58</instanceId>
 <aliyunAccountUid>17851119****7796</aliyunAccountUid>
 <internetDomain>inter.example.com</internetDomain>
 <resourceGroupId>103</resourceGroupId>
 <pk>339****29200627712</pk>
 <intranetDomain>intra.example.com</intranetDomain>
 <ownerUid>2397245*****868732</ownerUid>
 <accountCredentialsId>339944225****83232</accountCredentialsId>
 <consoleType>ASRDR</consoleType>
 <status>REGULAR</status>
</data> <requestId>b870********433d</requestId> <success /> <nodeIp>127.0.0.1</nodeIp>
```

##### DescribeLocalRegion

Queries the information about the region in which Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) resides.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. You do not need to specify this parameter. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | b870********433d | The request ID. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Response parameters**

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y***6R- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The returned data. |
| -pk | String | 33994****2006277 12 | The primary key of the region data in ASR- DR. |
| -regionId | String | cn-hangzhou | The region ID. |
| -regionName | String | region 01 _ | The name of the region. |
| -regionType | String | CENTRAL | The type of the region. Valid values: CENTRAL UNIT |
| -consoleType | String | ASRDR | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| - consoleApiEnd point | String | http://internal.APIle .cn-xxxxxxx | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |
|---|---|---|---|
| -cloudInstance | Struct |  | The information about the cloud instance. |
| -- aliyunAccount Uid | String | 1785111****67796 | The ID of the Apsara Stack tenant account to which the resource belongs. |
| --ownerUid | String | 2397*****8988687 32 | The unique ID (UID) of the resource owner. |
| --creator | String | 2397*****8988687 32 | The UID of the user who created the resource. |
| --lastModifier | String | 2397*****8988687 32 | The UID of the user who last modified the resource. |
| -- resourceRegio nId | String | region 01 _ | The region ID of the resource. |
| -- resourceGroup Id | String | 103 | The ID of the resource group to which the resource belongs. |
| --createdDate | Long | 1713514782222 | The time when the resource was created. |
| -- lastModifiedDa te | Long | 1713514782222 | The time when the resource was last modified. |
| --instanceId | String | e250008c-a02a- 455c-b957- 8d*****ef58 | The instance ID of the resource. |
| -- instanceName | String | XXX | The instance name of the resource. |
| --pk | String | 339944229200627 712 | The primary key of the cloud instance. |
| -- cloudUniqueId | String | 0179 | The UID of the cloud. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| --cloudOsType | String | ENTERPRISE | The edition of the cloud instance. Only ENTERPRISE may be returned, which indicates Apsara Stack. |
|---|---|---|---|
| --version | String | 1.0.0 | The version number of the cloud instance. |
| --consoleType | String | ASRDR | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |
| -- consoleApiEnd point | String | http://internal.exa mple.cn-xxxxxxx | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |
| -- adminCredenti alsId | String | 339944225551583 232 | The credential ID of the cloud management administrator. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of an operations administrator. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as the operations administrator, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |
| -- accountCrede ntialsId | String | 339944225551583 232 | The credential ID of the organization account. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of a level-1 organization. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as an organization administrator. In the top navigation bar, click Enterprise. In the left-side navigation pane, choose Resources > Organizations. On the page that appears, obtain an AccessKey pair of a level-1 organization. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| -- internetDomai n | String | inter.example.com | The Internet domain name. |
|---|---|---|---|
| -- intranetDomai n | String | intra.example.com | The internal domain name. |
| --status | String | REGULAR | The status of the cloud instance. Valid values: REGULAR: normal. NOT CONFIGURED: not configured. _ UNINITIALIZED: not initialized. The cloud instance is in this state if no administrator credentials are configured when you log on to ASR-DR for the first time. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLocalRegion &<Common request parameters>
```

Sample success responses `JSON` format Apsara Stack Resilience ASR for Geo-disaster Developer

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y***6R-1914.local",
 "code":"200",
 "data":{
  "regionId":"cn-hangzhou",
  "regionType":"CENTRAL",
  "consoleApiEndpoint":"http://internal.example.cn-xxxxxxx",
  "regionName":"region_01",
  "pk":"33994****200627712",
  "-cloudInstance":{
   "cloudUniqueId":"0179",
   "creator":"2397*****898868732",
   "lastModifiedDate":1713514782222,
   "instanceName":"XXX",
   "consoleApiEndpoint":"http://internal.example.cn-xxxxxxx",
   "resourceRegionId":"region_01",
   "lastModifier":"2397*****898868732",
   "adminCredentialsId":"339944225551583232",
   "version":"1.0.0",
   "cloudOsType":"ENTERPRISE",
   "createdDate":1713514782222,
   "instanceId":"e250008c-a02a-455c-b957-8d*****ef58",
   "aliyunAccountUid":"1785111****67796",
   "internetDomain":"inter.example.com",
   "resourceGroupId":"103",
   "pk":"339944229200627712",
   "intranetDomain":"intra.example.com",
   "ownerUid":"2397*****898868732",
   "accountCredentialsId":"339944225551583232",
   "consoleType":"ASRDR",
   "status":"REGULAR"
  },
  "consoleType":"ASRDR"
 },
 "requestId":"b870********433d",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y***6R-1914.local</nodeHost> <code>200</code> <data>
 <regionId>cn-hangzhou</regionId>
 <regionType>CENTRAL</regionType>
 <consoleApiEndpoint>http://internal.example.cn-xxxxxxx</consoleApiEndpoint>
 <regionName>region_01</regionName>
 <pk>33994****200627712</pk>
 <-cloudInstance>
  <cloudUniqueId>0179</cloudUniqueId>
  <creator>2397*****898868732</creator>
  <lastModifiedDate>1713514782222</lastModifiedDate>
  <instanceName>XXX</instanceName>
  <consoleApiEndpoint>http://internal.example.cn-xxxxxxx</consoleApiEndpoint>
  <resourceRegionId>region_01</resourceRegionId>
  <lastModifier>2397*****898868732</lastModifier>
  <adminCredentialsId>339944225551583232</adminCredentialsId>
  <version>1.0.0</version>
  <cloudOsType>ENTERPRISE</cloudOsType>
  <createdDate>1713514782222</createdDate>
  <instanceId>e250008c-a02a-455c-b957-8d*****ef58</instanceId>
  <aliyunAccountUid>1785111****67796</aliyunAccountUid>
  <internetDomain>inter.example.com</internetDomain>
  <resourceGroupId>103</resourceGroupId>
  <pk>339944229200627712</pk>
  <intranetDomain>intra.example.com</intranetDomain>
  <ownerUid>2397*****898868732</ownerUid>
  <accountCredentialsId>339944225551583232</accountCredentialsId>
  <consoleType>ASRDR</consoleType>
  <status>REGULAR</status>
 </-cloudInstance>
 <consoleType>ASRDR</consoleType>
</data> <requestId>b870********433d</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### ListRegions

Queries the available regions of a cloud instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). You do not need to specify this parameter. |
|---|---|---|---|---|---|
| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. You do not need to specify this parameter. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| CloudInsta nceId | Strin g | Quer y | Yes | 383********53c7 | The ID of the cloud instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array |  | The response data. |
| -pk | String | 33994****2006277 12 | The primary key of the region data in ASR- DR. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Response parameters**

| -regionId | String | cn-hangzhou | The region ID. |
|---|---|---|---|
| -regionName | String | region 01 _ | The name of the region. |
| -regionType | String | UNIT | The type of the region. Valid values: CENTRAL UNIT |
| -consoleType | String | ASRDR | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |
| - consoleApiEnd point | String | http://internal.exa mple-XXXXXX | The endpoint of the cloud management API in the region. |
| -cloudInstance | Struct |  | The information about the cloud instance. |
| -- aliyunAccount Uid | String | 1785111****67796 | The ID of the Apsara Stack tenant account to which the resource belongs. |
| --ownerUid | String | 2397*****8988687 32 | The unique ID (UID) of the resource owner. |
| --creator | String | 2397*****8988687 32 | The UID of the user who created the resource. |
| --lastModifier | String | 2397*****8988687 32 | The UID of the user who last modified the resource. |
| -- resourceRegio nId | String | region 01 _ | The region ID of the resource. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| -- resourceGroup Id | String | 103 | The ID of the resource group to which the resource belongs. |
|---|---|---|---|
| --createdDate | Long | 1713514782222 | The time when the resource was created. |
| -- lastModifiedDa te | Long | 1713514782222 | The time when the resource was last modified. |
| --instanceId | String | e250008c-a02a- 455c-b957- 8d*****ef58 | The ID of the cloud instance. |
| -- instanceName | String | XXX | The name of the cloud instance. |
| --pk | String | 339944229200627 712 | The primary key of the cloud instance. |
| -- cloudUniqueId | String | 0179 | The UID of the cloud. |
| --cloudOsType | String | ENTERPRISE | The edition of the cloud instance. Only ENTERPRISE may be returned, which indicates Apsara Stack. |
| --version | String | 1.0.0 | The version number of the cloud instance. |
| --consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| -- consoleApiEnd point | String | http://internal.exa mple-XXXXXX | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |
|---|---|---|---|
| -- adminCredenti alsId | String | 339944225551583 232 | The credential ID of the cloud management administrator. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of an operations administrator. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as the operations administrator, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |
| -- accountCrede ntialsId | String | 339944225551583 232 | The credential ID of the organization account. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of a level-1 organization. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as an organization administrator. In the top navigation bar, click Enterprise. In the left-side navigation pane, choose Resources > Organizations. On the page that appears, obtain an AccessKey pair of a level-1 organization. |
| -- internetDomai n | String | inter.example.com | The Internet domain name. |
| -- intranetDomai n | String | intra.example.com | The internal domain name. |
| --status | String | REGULAR | The status of the cloud instance. Valid values: REGULAR: normal. NOT CONFIGURED: not configured. _ UNINITIALIZED: not initialized. The cloud instance is in this state if no administrator credentials are configured when you log on to ASR-DR for the first time. |
| requestId | String | 4383********53c7 | The request ID. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y****R- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
&CloudInstanceId=383********53c7 &<Common request parameters>
```

Sample success responses `JSON` format Apsara Stack Resilience ASR for Geo-disaster Developer

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****R-1914.local",
 "code":"200",
 "data":{
  "regionId":"cn-hangzhou",
  "regionType":"UNIT",
  "consoleApiEndpoint":"http://internal.example-XXXXXX",
  "regionName":"region_01",
  "pk":"33994****200627712",
  "-cloudInstance":{
   "cloudUniqueId":"0179",
   "creator":"2397*****898868732",
   "lastModifiedDate":1713514782222,
   "instanceName":"XXX",
   "consoleApiEndpoint":"http://internal.example-XXXXXX",
   "resourceRegionId":"region_01",
   "lastModifier":"2397*****898868732",
   "adminCredentialsId":"339944225551583232",
   "version":"1.0.0",
   "cloudOsType":"ENTERPRISE",
   "createdDate":1713514782222,
   "instanceId":"e250008c-a02a-455c-b957-8d*****ef58",
   "aliyunAccountUid":"1785111****67796",
   "internetDomain":"inter.example.com",
   "resourceGroupId":"103",
   "pk":"339944229200627712",
   "intranetDomain":"intra.example.com",
   "ownerUid":"2397*****898868732",
   "accountCredentialsId":"339944225551583232",
   "consoleType":"ASCM",
   "status":"REGULAR"
  },
  "consoleType":"ASRDR"
 },
 "requestId":"4383********53c7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format ASR for Geo-disaster Developer Apsara Stack Resilience

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****R-1914.local</nodeHost> <code>200</code> <data>
 <regionId>cn-hangzhou</regionId>
 <regionType>UNIT</regionType>
 <consoleApiEndpoint>http://internal.API.cn-
region**.example.com/API/v3</consoleApiEndpoint>
 <regionName>region_01</regionName>
 <pk>33994****200627712</pk>
 <-cloudInstance>
  <cloudUniqueId>0179</cloudUniqueId>
  <creator>2397*****898868732</creator>
  <lastModifiedDate>1713514782222</lastModifiedDate>
  <instanceName>XXX</instanceName>
  <consoleApiEndpoint>http://internal.API.cn-
region**.example.com/API/v3APIsoleApiEndpoint>
  <resourceRegionId>region_01</resourceRegionId>
  <lastModifier>2397*****898868732</lastModifier>
  <adminCredentialsId>339944225551583232</adminCredentialsId>
  <version>1.0.0</version>
  <cloudOsType>ENTERPRISE</cloudOsType>
  <createdDate>1713514782222</createdDate>
  <instanceId>e250008c-a02a-455c-b957-8d*****ef58</instanceId>
  <aliyunAccountUid>1785111****67796</aliyunAccountUid>
  <internetDomain>inter.example.com</internetDomain>
  <resourceGroupId>103</resourceGroupId>
  <pk>339944229200627712</pk>
  <intranetDomain>intra.example.com</intranetDomain>
  <ownerUid>2397*****898868732</ownerUid>
  <accountCredentialsId>339944225551583232</accountCredentialsId>
  <consoleType>ASCM</consoleType>
  <status>REGULAR</status>
 </-cloudInstance>
 <consoleType>ASRDR</consoleType>
</data> <requestId>4383********53c7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### RemoveCloudInstance

Deletes a cloud instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). You do not need to specify this parameter. |
| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. You do not need to specify this parameter. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| CloudInsta nceId | Strin g | Quer y | Yes | ffe1********6d6d | The ID of the cloud instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | 75ef********dafe8 | The request ID. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Response parameters**

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y1***R- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RemoveCloudInstance &CloudInstanceId=ffe1********6d6d &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y1***R-1914.local",
 "code":"200",
 "requestId":"75ef********dafe8",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y1***R-1914.local</nodeHost> <code>200</code> <requestId>75ef********dafe8</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

ASR for Geo-disaster Developer Apsara Stack Resilience

### Protection groups

#### Protection group management

##### CreateProtectGroup

Creates a protection group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| MainCloudI d | Strin g | Quer y | Yes | ffe1********6d6d | The ID of the primary cloud. |
| BackupClo udId | Strin g | Quer y | Yes | 0d3a********2cd3 | The ID of the secondary cloud. |
| MainRegio nId | Strin g | Quer y | Yes | cn-xxxx-d01 | The ID of the primary region. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| BackupRe gionId | Strin g | Quer y | Yes | cn-xxxx-d01 | The ID of the secondary region. |
|---|---|---|---|---|---|
| ProtectGro upName | Strin g | Quer y | Yes | openapi-test | The name of the protection group. |
| Direction | Strin g | Quer y | Yes | FORWARD | The direction of the protection group. Valid values: FORWARD REVERSE |
| Descriptio n | Strin g | Quer y | No | test | The description of the protection group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | 5daf********f0c7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The information about the protection group. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| - protectGroupI d | String | 379e********98c7 | The ID of the protection group. |
|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateProtectGroup &MainCloudId=ffe1********6d6d &BackupCloudId=0d3a********2cd3 &MainRegionId=cn-xxxx-d01 &BackupRegionId=cn-xxxx-d01 &ProtectGroupName=openapi-test &Direction=FORWARD &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "data":{
  "protectGroupId":"379e********98c7"
 },
 "requestId":"5daf********f0c7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <data>
 <protectGroupId>379e********98c7</protectGroupId>
</data> <requestId>5daf********f0c7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### UpdateProtectGroup

Updates a protection group.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is a parameter of the Apsara Stack API. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is a parameter of the Apsara Stack API. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is a parameter of the Apsara Stack API. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| ProtectGro upId | Strin g | Quer y | Yes | 379e********98c7 | The ID of the protection group. |
| ProtectGro upName | Strin g | Quer y | Yes | OSS1 | The name of the protection group. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Descriptio n | Strin g | Quer y | No | XXX protection group | The description of the protection group. |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateProtectGroup &ProtectGroupId=379e********98c7 &ProtectGroupName=OSS1 &<Common request parameters>
```

Sample success responses `JSON` format

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### RemoveProtectGroup

Deletes a protection group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is a parameter of the Apsara Stack API. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is a parameter of the Apsara Stack API. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is a parameter of the Apsara Stack API. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| ProtectGro upId | Strin g | Quer y | Yes | 379e********98c7 | The ID of the protection group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Response parameters**

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RemoveProtectGroup &ProtectGroupId=379e********98c7 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AsrMainCl oudInstan ceId | Strin g | Query | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

ASR for Geo-disaster Developer Apsara Stack Resilience

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### DescribeProtectGroup

Queries the information about a protection group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AsrMainRe gionId | Strin g | Query | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Query | No | 3 | The organization ID. This is an API parameter of the Apsara Uni- manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Resource Group | Strin g | Query | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
| ProtectGr oupId | Strin g | Query | Yes | 379e********98c7 | The ID of the protection group. |
| PageNum | Integ er | Query | Yes | 55 | The page number. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | Yes | 5 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The information about the resource. |
| - aliyunAccount Uid | String | 167333***8012 | The ID of the Apsara Stack tenant account to which the resource belongs. |
| -ownerUid | String | 21733******12 | The unique ID (UID) of the resource owner. |
| -creator | String | 2173333****12 | The UID of the user who created the resource. |
| -lastModifier | String | 217333***12 | The UID of the user who last modified the resource. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| SR for Geo-disast Guide·API referen | er Developer ce |  | Apsara Stack Resilienc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - resourceRegio nId | String | guangzhou region _ _ 01 | The region ID of the resource. |
| - resourceGroup Id | String | fe1********6d6d | The ID of the resource group. |
| -createdDate | Long | 1673333258000 | The time when the resource was created. |
| - lastModifiedDa te | Long | 1673333258012 | The time when the resource was last modified. |
| -instanceId | String | 79e********98c7 | The instance ID of the resource. |
| - instanceName | String | OSS1 | The instance name of the resource. |
| - protectGroupI d | String | 379e********98c7 | The ID of the protection group. |
| -name | String | openapi-test | The name of the protection group. |
| -direction | String | FORWARD | The direction of the protection group. Valid values: FORWARD REVERSE |
| -description | String | Protection group for XXX business application | The description of the protection group. |
| -mainRegionId | String | region-1 | The region ID of the primary cloud. |
| - backupRegionI d | String | region-2 | The region ID of the secondary cloud. |
| - mainOrganizat ionName | String | asrdr | The organization name of the primary cloud. |
| - backupOrganiz ationName | String | asrdr | The organization name of the secondary cloud. |
| - mainOrganizat ionId | Integer | 9 | The organization ID of the primary cloud. |

| psara Stack Resil | ience |  | ASR for Geo-disaster Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - backupOrganiz ationId | Integer | 6 | The organization ID of the secondary cloud. |
| -maxRPO | Long | 9000 | The maximum data latency of the protection group. Unit: milliseconds. |
| -aveRPO | Long | 8000 | The average data latency of the protection group. Unit: milliseconds. |
| -aveProgress | String | 100 | The average synchronization progress of synchronization entities in the protection group. |
| -canChange | Boolean | true | Indicates whether the protection group can be modified and migrated. |
| - sourceTenantI d | Long | 1666665 | The source organization ID of DataWorks. This parameter is returned if DataWorks synchronization entities exist in the protection group. |
| -destTenantId | Long | 133434 | The destination organization ID of DataWorks. This parameter is returned if DataWorks synchronization entities exist in the protection group. |
| -protectState | String | PROTECT | The protection status of the protection group. Valid values: PROTECT SUSPEND REPROTECT REPROTECT FAIL _ REDO PROTECT START _ PROTECT FAIL _ PLAN EXECUTION _ PLAN FAIL _ DESTROY PROTECT IDLE _ STOP START |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - rpoAlarmLevel | String | WARN | The alert level. If the synchronization latency of the protection group is higher than the specified threshold, WARN is returned. Otherwise, NORMAL is returned. Valid values: WARN and NORMAL. |
| -createTime | Long | 1673333258000 | The time when the protection group was created. |
| -priority | Struct |  | The information about the synchronization entities. |
| --rows | Normal |  | The synchronization entities, in the JSON format. |
| --total | Integer | 12 | The total number of entries returned. |
| --pageSize | Integer | 10 | The number of entries per page. The value is set to 10. |
| --pageNum | Integer | 1 | The page number. The value is an integer. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeProtectGroup &ProtectGroupId=379e********98c7 &PageNum=55 &PageSize=5 &<Common request parameters>
```

Sample success responses `JSON` format Apsara Stack Resilience ASR for Geo-disaster Developer

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "data":{
  "protectState":"PROTECT",
  "instanceName":"OSS1",
  "resourceRegionId":"guangzhou_region_01",
  "lastModifier":"217333***12",
  "description":"Protection group for XXX business application",
  "backupOrganizationId":6,
  "mainRegionId":"region-1",
  "canChange":true,
  "instanceId":"79e********98c7",
  "aliyunAccountUid":"167333***8012",
  "resourceGroupId":"fe1********6d6d",
  "protectGroupId":"379e********98c7",
  "mainOrganizationId":9,
  "backupRegionId":"region-2",
  "-priority":{
   "total":12,
   "pageSize":10,
   "rows":"",
   "pageNum":1
  },
  "direction":"FORWARD",
  "creator":"2173333****12",
  "maxRPO":9000,
  "lastModifiedDate":1673333258012,
  "aveProgress":"100",
  "backupOrganizationName":"asrdr",
  "destTenantId":133434,
  "rpoAlarmLevel":"WARN",
  "createdDate":1673333258000,
  "aveRPO":8000,
  "createTime":1673333258000,
  "sourceTenantId":1666665,
  "name":"openapi-test",
  "ownerUid":"21733******12",
  "mainOrganizationName":"asrdr"
 },
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format ASR for Geo-disaster Developer Apsara Stack Resilience

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <data>
 <protectState>PROTECT</protectState>
 <instanceName>OSS1</instanceName>
 <resourceRegionId>guangzhou_region_01</resourceRegionId>
 <lastModifier>217333***12</lastModifier>
 <description>Protection group for XXX business application</description>
 <backupOrganizationId>6</backupOrganizationId>
 <mainRegionId>region-1</mainRegionId>
 <canChange>true</canChange>
 <instanceId>79e********98c7</instanceId>
 <aliyunAccountUid>167333***8012</aliyunAccountUid>
 <resourceGroupId>fe1********6d6d</resourceGroupId>
 <protectGroupId>379e********98c7</protectGroupId>
 <mainOrganizationId>9</mainOrganizationId>
 <backupRegionId>region-2</backupRegionId>
 <-priority>
  <total>12</total>
  <pageSize>10</pageSize>
  <rows  />
  <pageNum>1</pageNum>
 </-priority>
 <direction>FORWARD</direction>
 <creator>2173333****12</creator>
 <maxRPO>9000</maxRPO>
 <lastModifiedDate>1673333258012</lastModifiedDate>
 <aveProgress>100</aveProgress>
 <backupOrganizationName>asrdr</backupOrganizationName>
 <destTenantId>133434</destTenantId>
 <rpoAlarmLevel>WARN</rpoAlarmLevel>
 <createdDate>1673333258000</createdDate>
 <aveRPO>8000</aveRPO>
 <createTime>1673333258000</createTime>
 <sourceTenantId>1666665</sourceTenantId>
 <name>openapi-test</name>
 <ownerUid>21733******12</ownerUid>
 <mainOrganizationName>asrdr</mainOrganizationName>
</data> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### ListProtectGroup

Queries protection groups.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |
| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Request parameters**

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| ProtectGro upId | Strin g | Quer y | No | 379e********98c7 | The ID of the protection group. |
| ProtectGro upIds | Strin g | Quer y | No | 379e********98c7,224g** ******d43c | The IDs of the protection groups. Separate multiple IDs with commas (,). |
| ProtectGro upName | Strin g | Quer y | No | ProtectGroup1 | The name of the protection group. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Direction | Strin g | Quer y | No | FORWARD | The direction of the protection group. Valid values: FORWARD REVERSE |
|---|---|---|---|---|---|
| Type | Strin g | Quer y | No | type | The type of the protection group. This is an extended parameter. |
| Status | Strin g | Quer y | No | PROTECT | The status of the protection group. |
| MainRegio nId | Strin g | Quer y | No | region-1 | The region ID of the primary cloud. |
| BackupRe gionId | Strin g | Quer y | No | region-2 | The region ID of the secondary cloud. |
| Sort | Strin g | Quer y | No | createdDate | The sorting field. Set the value to createdDate. |
| Order | Strin g | Quer y | No | ASC | The sorting order. Valid values: ASC DESC |
| PageNum | Integ er | Quer y | Yes | 10 | The page number. Specify an integer. |
| PageSize | Integ er | Quer y | Yes | 1 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
|---|---|---|---|
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The queried protection groups. |
| -rows | Array |  | The number of rows. |
| -- aliyunAccount Uid | String | 1673*****8012 | The ID of the Apsara Stack tenant account to which the resource belongs. |
| --ownerUid | String | 21733*****012 | The unique ID (UID) of the resource owner. |
| --creator | String | 21733*****012 | The UID of the user who created the resource. |
| --lastModifier | String | 21733*****012 | The UID of the user who last modified the resource. |
| -- resourceRegio nId | String | cn-hangzhou | The region ID of the resource. |
| -- resourceGroup Id | String | rs-1223 | The ID of the resource group. |
| --createdDate | Long | 1673333258000 | The time when the resource was created. |
| -- lastModifiedDa te | Long | 1673333258012 | The time when the resource was last modified. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| psara Stack Resil | ience |  | ASR for Geo-disaster Developer Guide·API referenc |
|---|---|---|---|

| --instanceId | String | 79e********98c7 | The instance ID of the resource. |
|---|---|---|---|
| -- instanceName | String | OSS1 | The instance name of the resource. |
| -- protectGroupI d | String | 379e********98c7 | The ID of the protection group. |
| --name | String | openapi-test | The name of the protection group. |
| --direction | String | FORWARD | The direction of the protection group. Valid values: FORWARD REVERSE |
| --description | String | Protection group for XXX business application | The description of the protection group. |
| --mainCloudId | String | cn 01 _ | The ID of the primary cloud. |
| --maxRPO | Long | 0 | The maximum data synchronization latency. Unit: milliseconds. |
| --rpoMillis | Long | 0 | The maximum data synchronization latency. Unit: milliseconds. |
| --aveRPO | Long | 0 | The average data synchronization latency. Unit: milliseconds. |
| --aveProgress | String | 100 | The progress of full data synchronization. |

| --protectState | String | PROTECT | The protection status of the protection group. Valid values: PROTECT SUSPEND REPROTECT REPROTECT FAIL _ REDO PROTECT START _ PROTECT FAIL _ PLAN EXECUTION _ PLAN FAIL _ DESTROY PROTECT IDLE _ STOP START |
|---|---|---|---|
| -- rpoAlarmLevel | String | WARN | The alert level. If the synchronization latency of the protection group is higher than the specified threshold, WARN is returned. Otherwise, NORMAL is returned. Valid values: WARN and NORMAL. |
| --gmtCreate | Long | 123666000012 | The time when the protection group was created. |
| -- syncEntityNum | Integer | 12 | The number of synchronization entities. |
| -- latestSwitchOv erPlan | Struct |  | The details of the last switchover or failover. |
| ---taskInfos | Array |  | The details of the tasks. |
| ----taskNum | Integer | 20 | The total number of tasks. |
| ----taskName | String | TASK | The name of the task. |
| ----ipAddr | String | 127.0.0.1 | The IP address of the node that ran the task. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| ---- taskDescriptio n | String | XXX failover task | The description of the task. |
|---|---|---|---|
| ----taskType | String | handover | The type of the task. |
| ----priority | Integer | 3 | The priority of the task. |
| ----stage | String | S1 | The stage of the task. Valid values: S1 S2 |
| ----startTime | Long | 1673333258000 | The time when the task started. |
| ---- durationInMilli s | Long | 1200 | The duration of the task. Unit: milliseconds. |
| ----progress | String | 100 | The progress of the switch. |
| ----status | String | IDLE | The status of the switch. Valid values: IDLE RUNNING |
| ---planId | String | 79e********98c7 | The switch ID. |
| ---planName | String | plan1 | The name of the switch. |
| ---description | String | Failover 1 for XXX | The description of the switch. |
| --- protectGroupI d | String | 379e********98c7 | The ID of the protection group. |
| --- protectGroupN ame | String | openapi-test | The name of the protection group. |
| --- resourceGroup Name | String | resourceGroup1 | The name of the resource group. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| --- deploymentId | String |  | A reserved parameter. |
|---|---|---|---|
| ---createTime | String | 1673333258000 | The time when the switch was created. |
| ---status | String | IDLE | The status of the switch. Valid values: IDLE RUNNING |
| ---stepStatus | String | IDLE | The status of the next step. |
| ---planType | String | FAILOVER | The type of the switch. Valid values: FAILOVER SWITCHOVER |
| --- planInstanceN um | String | 2 | The total number of instances involved. |
| --- latestPlanInsta nceId | String | 2b22********92c7 | The ID of the latest involved instance. |
| ---entityType | String |  | A reserved parameter. |
| ---planStatus | String | IDLE | The status of the switch. Valid values: IDLE RUNNING |
| ---cloudId | String | 79e********98c7 | The cloud ID. |
| --- failoverMode | String |  | A reserved parameter. |
| -- latestSwitchBa ckPlan | Struct |  | The details of the last switchback or failback. |
| ---taskInfos | Array |  | The details of the tasks. |
| ----taskNum | Integer | 20 | The total number of tasks. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| ----taskName | String | TASK | The name of the task. |
|---|---|---|---|
| ----ipAddr | String | 127.0.0.1 | The IP address of the node that ran the task. |
| ---- taskDescriptio n | String | XXX failback task | The description of the task. |
| ----taskType | String | handover | The type of the task. |
| ----priority | Integer | 3 | The priority of the task. |
| ----stage | String | S1 | The stage of the task. Valid values: S1 S2 |
| ----startTime | Long | 1673333258000 | The time when the task started. |
| ---- durationInMilli s | Long | 1200 | The duration of the task. Unit: milliseconds. |
| ----progress | String | 100 | The progress of the switch. |
| ----status | String | IDLE | The status of the switch. Valid values: IDLE RUNNING |
| ---planId | String | 79e********98c7 | The switch ID. |
| ---planName | String | plan1 | The name of the switch. |
| ---description | String | Failback 1 for XXX | The description of the switch. |
| --- protectGroupI d | String | 379e********98c7 | The ID of the protection group. |
| --- protectGroupN ame | String | openapi-test | The name of the protection group. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| --- resourceGroup Name | String | resourceGroup1 | The name of the resource group. |
|---|---|---|---|
| --- deploymentId | String |  | A reserved parameter. |
| ---createTime | String | 1673333258000 | The time when the switch was created. |
| ---status | String | IDLE | The status of the switch. Valid values: IDLE RUNNING |
| ---stepStatus | String | IDLE | The status of the next step. |
| ---planType | String | FAILBACK | The type of the switch. Valid values: FAILBACK SWITCHBACK |
| --- planInstanceN um | String | 2 | The total number of instances involved. |
| --- latestPlanInsta nceId | String | 2b22********92c7 | The ID of the latest involved instance. |
| ---entityType | String |  | A reserved parameter. |
| ---planStatus | String | IDLE | The status of the switch. Valid values: IDLE RUNNING |
| ---cloudId | String | 79e********98c7 | The cloud ID. |
| --- failoverMode | String |  | A reserved parameter. |
| -pageNum | Integer | 10 | The number of entries per page. |
| -pageSize | Integer | 1 | The page number. The value is an integer. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| -total | Integer | 50 | The total number of entries returned. |
|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

**Examples**

Sample requests

```
&PageNum=10 &PageSize=1 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "data":{
  "total":50,
  "-rows":{
   "protectState":"PROTECT",
   "syncEntityNum":12,
   "instanceName":"OSS1",
   "resourceRegionId":"cn-hangzhou",
   "--latestSwitchOverPlan":{
    "planInstanceNum":"2",
    "failoverMode":"",
    "resourceGroupName":"resourceGroup1",
    "planType":"FAILOVER",
    "entityType":"",
    "latestPlanInstanceId":"2b22********92c7",
    "planName":"plan1",
    "description":"Failover 1 for XXX",
    "planStatus":"IDLE",
    "protectGroupName":"openapi-test",
    "---taskInfos":{
     "taskType":"handover",
     "stage":"S1",
     "durationInMillis":1200,
     "taskDescription":"XXX failover task",
     "progress":"100",
     "taskName":"TASK",
     "startTime":1673333258000,
     "priority":3,
     "taskNum":20,
     "ipAddr":"127.0.0.1",
     "status":"IDLE"
    },
    "createTime":"1673333258000",
    "deploymentId":"",
    "cloudId":"79e********98c7",
```

ASR for Geo-disaster Developer Apsara Stack Resilience ,

```json
    "planId":"79e********98c7",
    "protectGroupId":"379e********98c7",
    "stepStatus":"IDLE",
    "status":"IDLE"
   },
   "lastModifier":"21733*****012",
   "description":"Protection group for XXX business application",
   "mainCloudId":"cn_01",
   "instanceId":"79e********98c7",
   "aliyunAccountUid":"1673*****8012",
   "resourceGroupId":"rs-1223",
   "--latestSwitchBackPlan":{
    "planInstanceNum":"2",
    "failoverMode":"",
    "resourceGroupName":"resourceGroup1",
    "planType":"FAILBACK",
    "entityType":"",
    "latestPlanInstanceId":"2b22********92c7",
    "planName":"plan1",
    "description":"Failback 1 for XXX",
    "planStatus":"IDLE",
    "protectGroupName":"openapi-test",
    "---taskInfos":{
     "taskType":"handover",
     "stage":"S1",
     "durationInMillis":1200,
     "taskDescription":"XXX failback task",
     "progress":"100",
     "taskName":"TASK",
     "startTime":1673333258000,
     "priority":3,
     "taskNum":20,
     "ipAddr":"127.0.0.1",
     "status":"IDLE"
    },
    "createTime":"1673333258000",
    "deploymentId":"",
    "cloudId":"79e********98c7",
    "planId":"79e********98c7",
    "protectGroupId":"379e********98c7",
    "stepStatus":"IDLE",
    "status":"IDLE"
   },
   "protectGroupId":"379e********98c7",
   "direction":"FORWARD",
   "creator":"21733*****012",
   "maxRPO":0,
   "lastModifiedDate":1673333258012,
   "rpoMillis":0,
   "gmtCreate":123666000012,
   "aveProgress":"100",
   "rpoAlarmLevel":"WARN",
   "createdDate":1673333258000,
   "aveRPO":0,
```

Apsara Stack Resilience ASR for Geo-disaster Developer

```json
   "name":"openapi-test",
   "ownerUid":"21733*****012"
  },
  "pageSize":1,
  "pageNum":10
 },
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <data>
 <total>50</total>
 <-rows>
  <protectState>PROTECT</protectState>
  <syncEntityNum>12</syncEntityNum>
  <instanceName>OSS1</instanceName>
  <resourceRegionId>cn-hangzhou</resourceRegionId>
  <--latestSwitchOverPlan>
   <planInstanceNum>2</planInstanceNum>
   <failoverMode  />
   <resourceGroupName>resourceGroup1</resourceGroupName>
   <planType>FAILOVER</planType>
   <entityType  />
   <latestPlanInstanceId>2b22********92c7</latestPlanInstanceId>
   <planName>plan1</planName>
   <description>Failover 1 for XXX</description>
   <planStatus>IDLE</planStatus>
   <protectGroupName>openapi-test</protectGroupName>
   <---taskInfos>
    <taskType>handover</taskType>
    <stage>S1</stage>
    <durationInMillis>1200</durationInMillis>
    <taskDescription>XXX failover task</taskDescription>
    <progress>100</progress>
    <taskName>TASK</taskName>
    <startTime>1673333258000</startTime>
    <priority>3</priority>
    <taskNum>20</taskNum>
    <ipAddr>127.0.0.1</ipAddr>
    <status>IDLE</status>
   </---taskInfos>
   <createTime>1673333258000</createTime>
   <deploymentId  />
   <cloudId>79e********98c7</cloudId>
   <planId>79e********98c7</planId>
   <protectGroupId>379e********98c7</protectGroupId>
   <stepStatus>IDLE</stepStatus>
   <status>IDLE</status>
```

ASR for Geo-disaster Developer Apsara Stack Resilience

```xml
status /status
  </--latestSwitchOverPlan>
  <lastModifier>21733*****012</lastModifier>
  <description>Protection group for XXX business application</description>
  <mainCloudId>cn_01</mainCloudId>
  <instanceId>79e********98c7</instanceId>
  <aliyunAccountUid>1673*****8012</aliyunAccountUid>
  <resourceGroupId>rs-1223</resourceGroupId>
  <--latestSwitchBackPlan>
   <planInstanceNum>2</planInstanceNum>
   <failoverMode  />
   <resourceGroupName>resourceGroup1</resourceGroupName>
   <planType>FAILBACK</planType>
   <entityType  />
   <latestPlanInstanceId>2b22********92c7</latestPlanInstanceId>
   <planName>plan1</planName>
   <description>Failback 1 for XXX</description>
   <planStatus>IDLE</planStatus>
   <protectGroupName>openapi-test</protectGroupName>
   <---taskInfos>
    <taskType>handover</taskType>
    <stage>S1</stage>
    <durationInMillis>1200</durationInMillis>
    <taskDescription>XXX failback task</taskDescription>
    <progress>100</progress>
    <taskName>TASK</taskName>
    <startTime>1673333258000</startTime>
    <priority>3</priority>
    <taskNum>20</taskNum>
    <ipAddr>127.0.0.1</ipAddr>
    <status>IDLE</status>
   </---taskInfos>
   <createTime>1673333258000</createTime>
   <deploymentId  />
   <cloudId>79e********98c7</cloudId>
   <planId>79e********98c7</planId>
   <protectGroupId>379e********98c7</protectGroupId>
   <stepStatus>IDLE</stepStatus>
   <status>IDLE</status>
  </--latestSwitchBackPlan>
  <protectGroupId>379e********98c7</protectGroupId>
  <direction>FORWARD</direction>
  <creator>21733*****012</creator>
  <maxRPO>0</maxRPO>
  <lastModifiedDate>1673333258012</lastModifiedDate>
  <rpoMillis>0</rpoMillis>
  <gmtCreate>123666000012</gmtCreate>
  <aveProgress>100</aveProgress>
  <rpoAlarmLevel>WARN</rpoAlarmLevel>
  <createdDate>1673333258000</createdDate>
  <aveRPO>0</aveRPO>
  <name>openapi-test</name>
  <ownerUid>21733*****012</ownerUid>
 </-rows>
 <pageSize>1</pageSize>
```

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

```xml
 <pageNum>10</pageNum>
</data> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### StartProtectGroup

Starts a protection group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| ProtectGro upId | Strin g | Quer y | Yes | 379e********98c7 | The ID of the protection group. |
| Direction | Strin g | Quer y | Yes | FORWARD | The direction of the protection group. Valid values: FORWARD REVERSE |

Apsara Stack Resilience ASR for Geo-disaster Developer

| IsStop | Bool ean | Quer y | No | true | Specifies whether to stop the synchronization entity configuration process. Valid values: true false |
|---|---|---|---|---|---|
| SyncEntiti es | Strin g | Quer y | Yes |  | The configurations of the synchronization entity. For more information, see the following configurations. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Common parameters of synchronization entities**

```json
{ "protectGroupId":"379e********98c7", // The ID of the protection group. "mainCloudId":"379e********98c7", // The ID of the primary cloud instance. "backupCloudId":"379e********98c7", // The ID of the secondary cloud instance. "srcRegionId":"rn-hangzhou", // The region ID of the primary cloud. "dstRegionId":"cn-beijing", // The region ID of the secondary cloud. "mainInstanceId":"rm-xxdsss", // The ID of the cloud service instance in the primary cl oud. "backupInstanceId":"rm-xxdsss", // The ID of the cloud service instance in the secondar y cloud. "mainInstanceName":"ApsaraDB RDS instance name", // The name of the cloud service insta nce in the primary cloud. "backupInstanceName":"ApsaraDB RDS instance name", // The name of the cloud service ins tance in the secondary cloud. "syncType": "FULL", // The type of synchronization. Valid values: FULL and HOT. "priorityNumber": "1", // The priority. }
```

**RDS-MySQL**

Apsara Stack Resilience ASR for Geo-disaster Developer

```json
{ "entityType": "RDS" "roAccounts":"[{"dbName": "a", "readonlyAccounts" : "u1,u2,u3"}]", // The read-only acc ounts. "syncObjects":"[{"dbName": "a", "excludeTables" : "t1,t2,t3"}]", // The objects to be s ynchronized. "checkpoint":"1714121073", // The UNIX timestamp. Unit: seconds. This parameter takes e ffect only when syncType is set to HOT. "srcSuperAccount":"rds_admin", // The name of the privileged account of the primary ins tance. "srcSuperPassword":"rds_passd", // The password of the privileged account of the primar y instance. "dstSuperAccount":"rds_admin", // The name of the privileged account of the secondary i nstance. "dstSuperPassword":"rds_passd", // The password of the privileged account of the second ary instance. }
```

**ADB3**

```json
{ "entityType": "ADB3" "mainAccountName":"rds_admin", // The name of the account used to synchronize data from or to the primary instance. "mainAccountPassword":"rds_passd", // The password of the account used to synchronize d ata from or to the primary instance. "backupAccountName":"rds_admin", // The name of the account used to synchronize data fr om or to the secondary instance. "backupAccountPassword":"rds_passd", // The password of the account used to synchronize data from or to the secondary instance. }
```

**Cross-cloud DNS**

ASR for Geo-disaster Developer Apsara Stack Resilience

```json
{
    "entityType": "DNS", // The type of the synchronization entity.
    "srcZoneId": "e39d0b92-0cb8-****-b426-16d7d617ce66", // The ID of the primary domai
n name.
    "zoneName": "xxx.xxx.com.", // The primary domain name.
    "mainInstanceId": "b9698b3f-0c13-****-aa50-751e23afe730", // The DNS record ID of t
he primary domain name.
    "mainInstanceName": "cx", // The DNS record name of the primary domain name.
    "backupInstanceId": "b9698b3f-0c13-4751-****-751e23afe730", // The DNS record ID of
the secondary domain name.
    "backupInstanceName": "cx", // The DNS record name of the secondary domain name.
    "lineIds": "default", // The name of the DNS line.
    "rrSet": [
        "*.*.*.* 0",
        "*.*.*.* 100"
    ], // The values of the DNS record.
    "type": "A", // The type of the DNS record.
    "ttl": 30 // The time to live (TTL) of the DNS record.
}
```

**DNS within Cloud**

```json
{
    "entityType": "GLOBALDNS", // The type of the synchronization entity.
    "srcZoneId": "5ba01d2b-56 ae-****-8257-cc88bc****5b", // The ID of the primary doma
in name.
    "dstZoneId": "5ba01d2b-56ae-****-8257-cc88bc****5b", // The ID of the secondary dom
ain name.
    "zoneName": "xxx.com.", // The primary/secondary domain name.
    "mainInstanceId": "f0fd1f88-a598-436e-****-4c3772d****a", // The DNS record ID of t
he primary domain name.
    "mainInstanceName": "main", // The DNS record name of the primary domain name.
    "backupInstanceId": "f0fd1f88-a598-436e-****-4c377****64a", // The DNS record ID of
the secondary domain name.
    "backupInstanceName": "back", // The DNS record name of the secondary domain name.
    "lineIds": "default", // The name of the DNS line.
    "rrSet": [
        "xxx1.xxx.com. 0",
        "xxx2.xxx.com. 100"
    ], // The values of the DNS record.
    "type": "CNAME", // The type of the DNS record.
    "ttl": 30 // The TTL of the DNS record.
}
```

**DRDS**

Apsara Stack Resilience ASR for Geo-disaster Developer

```json
{ "entityType": "DRDS" "dstDrdsDBPassword": "db_passd" // The password of the destination database. "roAccounts":"[{"dbName": "a", "readonlyAccounts" : "u1,u2,u3"}]", // The read-only acc ounts. "syncObjects":"[{"dbName": "a", "excludeTables" : "t1,t2,t3"}]", // The objects to be s ynchronized. "checkpoint":"1714121073", // The UNIX timestamp. Unit: seconds. }
```

**ECS**

```json
{ "entityType": "ECS" "reuseHdrPg": false // Specifies whether to reuse the Hybrid Disaster Recovery (HDR) pr otection group. "hdrProtectGroupId": "err_id" // The ID of the HDR protection group. You can leave this parameter empty. "sitePairMainZoneId":"zoneID", // The zone ID of the primary region. "sitePairBackupZoneId":"zoneID", // The zone ID of the secondary region. "mainVpcId":"1714121073", // The virtual private cloud (VPC) ID of the primary region. "backupVpcId":"1714121073", // The VPC ID of the secondary region. "mainVSwitchId":"zoneID", // The vSwitch ID of the primary region. "backupVSwitchId":"zoneID", // The vSwitch ID of the secondary region. "mainSecurityGroupId":"1714121073", // The security group ID of the primary region. "backupSecurityGroupId":"1714121073", // The security group ID of the secondary region. "expectRpo": 200, // The expected latency of data synchronization. "replicaBandwidth": 1009, // The available bandwidth. "reuseSitePair": false, // Specifies whether to reuse the site pair. "sitePairId":"zoneID", // The ID of the site pair to be reused. You can leave this para meter empty. "mainEcsId":"id,id", // The Elastic Compute Service (ECS) instance IDs of the primary r egion. Separate multiple IDs with commas (,). "backupEcsId":"id,id", // The ECS instance IDs of the secondary region. Separate multip le IDs with commas (,). }
```

**Hologres**

```json
{ "entityType": "HOLOGRES" }
```

**Lindorm**

```json
{ "entityType": "LINDORM" "ltsId":"lts-test", // The Lindorm Tunnel Service (LTS) instance ID. "checkpoint":"1714121073" // The UNIX timestamp. Unit: seconds. }
```

ASR for Geo-disaster Developer Apsara Stack Resilience

**MongoDB**

```json
{ "entityType": "MONGODB" "roAccounts":"[{"dbName": "a", "readonlyAccounts" : "u1,u2,u3"}]", // The read-only acc ounts. "syncObjects":"[{"dbName": "a", "excludeTables" : "t1,t2,t3"}]", // The objects to be s ynchronized. "checkpoint":"1714121073", // The UNIX timestamp. Unit: seconds. "mainShardAccount":"rds_admin", // The name of the shard account of the primary instanc
```

`e.`

```json
"mainShardPassword":"rds_passd", // The password of the shard account of the primary in stance. "backupShardAccount":"rds_admin", // The name of the shard account of the secondary ins tance. "backupShardPassword":"rds_passd", // The password of the shard account of the secondar y instance. }
```

**MQ**

```json
{ "entityType": "MQ" "mqTopics":"t1,t2" // The names of topics. Separate multiple names with commas (,). }
```

**DataWorks**

```json
{ "entityType": "ODPS" "cloudScene":"MULTIPLE_CLOUD/MULTIPLE_REGION" // The cloud scenario. Valid values: MULT IPLE_CLOUD and MULTIPLE_REGION. "mainTenantId": "Org-11783", // The primary tenant ID of DataWorks. "backupTenantId": "Org-11783", // The secondary tenant ID of DataWorks. "mainEngineName": "odsp-1,odsp-2", // The names of MaxCompute projects in the primary c loud. Separate multiple names with commas (,). "backupEngineName": "odps-1,odps-2", // The names of MaxCompute projects in the seconda ry cloud. Separate multiple names with commas (,). "syncTime": 1600 // The synchronization interval. Unit: seconds. "dataworkPolicy": "" // The synchronization policy of DataWorks resources. "maxComputePolicy": "" // The synchronization policy of MaxCompute resources. "nodeId": "" // The ID of the MaxCompute node. "nodeType": "" // The type of the MaxCompute node. }
```

**OSS**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED |

Apsara Stack Resilience ASR for Geo-disaster Developer

```json
{ "entityType": "OSS" "objectPrefixList":"[prefix,prefix2]" // The prefixes of the objects to be synchronized
```

.

```json
"replicationAction": "ALL/DELETE" // The operations to be synchronized. Valid values: A LL and PUT. }
```

**CDSOSS**

```json
{ "entityType": "CDSOSS" "objectPrefixList":"[prefix,prefix2]" // The prefixes of the objects to be synchronized
```

.

```json
"replicationAction": "ALL/DELETE" // The operations to be synchronized. Valid values: A LL and PUT. }
```

**OTS**

```json
{ "entityType": "OTS" "tables":"t1,t2" // The names of the tables to be synchronized. Separate multiple names with commas (,). "checkpoint": "1714121073" // The UNIX timestamp. Unit: seconds. }
```

**Redis**

```json
{ "entityType": "REDIS" "roAccounts":"[{"dbName": "a", "readonlyAccounts" : "u1,u2,u3"}]", // The read-only acc ounts. "checkpoint":"1714121073", // The UNIX timestamp. Unit: seconds. }
```

**Response parameters**

| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
|---|---|---|---|
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
&ProtectGroupId=379e********98c7 &Direction=FORWARD &SyncEntities= &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### StopProtectGroup

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer Stops a protection group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| ProtectGro upId | Strin g | Quer y | Yes | 379e********98c7 | The ID of the protection group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
&ProtectGroupId=379e********98c7 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### ReprotectProtectGroup

Reprotects a protection group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| ProtectGro upIds | Strin g | Quer y | Yes | 379e********98c7 | The ID of the protection group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ReprotectProtectGroup &ProtectGroupIds=379e********98c7 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### GetStartupProtectGroupDetail

Queries the information about a started protection group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| ProtectGro upId | Strin g | Quer y | Yes | 379e********98c7 | The ID of the protection group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The returned data. |
| - protectGroupS tartDto | Array |  | The information about the protection group. |
| -- rdsEngineInfoL ist | Array |  | The engines of ApsaraDB RDS. |
| ---entityId | String | 379e********98c7 | The ID of the synchronization entity. |
| ---engineName | String | 1.0.0 | The engine version. |
| ---engineName | String | 1.0.0 | The engine version. |
| -- protectGroupI d | String | 379e********98c7 | The ID of the protection group. |
| --name | String | OSS | The name of the protection group. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| --direction | String | FORWARD | The direction of the protection group. Valid values: FORWARD REVERSE |
|---|---|---|---|
| --description | String | Protection group for XXX business application | The description of the protection group. |
| --mainCloudId | String | 79e********98c7 | The ID of the primary cloud. |
| -- backupCloudId | Long | 12 | The ID of the secondary cloud. |
| -- mainRegionId | Long | 33 | The region ID of the primary cloud. |
| -- backupRegionI d | String | region-2 | The region ID of the secondary cloud. |
| --syncEntities | String |  | A reserved parameter. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetStartupProtectGroupDetail &ProtectGroupId=379e********98c7 &<Common request parameters>
```

Sample success responses `JSON` format ASR for Geo-disaster Developer Apsara Stack Resilience

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "data":{
  "-protectGroupStartDto":{
   "mainCloudId":"79e********98c7",
   "syncEntities":"",
   "name":"OSS",
   "description":"Protection group for XXX business application",
   "backupCloudId":12,
   "--rdsEngineInfoList":{
    "entityId":"379e********98c7",
    "engineName":"1.0.0"
   },
   "protectGroupId":"379e********98c7",
   "backupRegionId":"region-2",
   "mainRegionId":33,
   "direction":"FORWARD"
  }
 },
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <data>
 <-protectGroupStartDto>
  <mainCloudId>79e********98c7</mainCloudId>
  <syncEntities  />
  <name>OSS</name>
  <description>Protection group for XXX business application</description>
  <backupCloudId>12</backupCloudId>
  <--rdsEngineInfoList>
   <entityId>379e********98c7</entityId>
   <engineName>1.0.0</engineName>
  </--rdsEngineInfoList>
  <protectGroupId>379e********98c7</protectGroupId>
  <backupRegionId>region-2</backupRegionId>
  <mainRegionId>33</mainRegionId>
  <direction>FORWARD</direction>
 </-protectGroupStartDto>
</data> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

#### Synchronization entity management

##### AddSyncEntity

Adds a synchronization entity.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| ProtectGro upId | Strin g | Quer y | Yes | 379e********98c7 | The ID of the protection group. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Direction | Strin g | Quer y | Yes | FORWARD | The direction of the protection group. Valid values: FORWARD REVERSE |
|---|---|---|---|---|---|
| IsStop | Bool ean | Quer y | Yes | true | Specifies whether to stop data synchronization. Valid values: true false |
| SyncEntiti es | Strin g | Quer y | Yes | - | The configurations of the synchronization entity. For more information, see the following configurations. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Common parameters of synchronization entities**

```json
{ "protectGroupId":"379e********98c7", // The ID of the protection group. "mainCloudId":"379e********98c7", // The ID of the primary cloud instance. "backupCloudId":"379e********98c7", // The ID of the secondary cloud instance. "srcRegionId":"rn-hangzhou", // The region ID of the primary cloud. "dstRegionId":"cn-beijing", // The region ID of the secondary cloud. "mainInstanceId":"rm-xxdsss", // The ID of the cloud service instance in the primary cl oud. "backupInstanceId":"rm-xxdsss", // The ID of the cloud service instance in the secondar y cloud. "mainInstanceName":"ApsaraDB RDS instance name", // The name of the cloud service insta nce in the primary cloud. "backupInstanceName":"ApsaraDB RDS instance name", // The name of the cloud service ins tance in the secondary cloud. "syncType": "FULL", // The type of synchronization. Valid values: FULL and HOT. "priorityNumber": "1", // The priority. }
```

**ApsaraDB RDS for MySQL**

Apsara Stack Resilience ASR for Geo-disaster Developer

```json
{ "entityType": "RDS" "roAccounts":"[{"dbName": "a", "readonlyAccounts" : "u1,u2,u3"}]", // The read-only acc ounts. "syncObjects":"[{"dbName": "a", "excludeTables" : "t1,t2,t3"}]", // The objects to be s ynchronized. "checkpoint":"1714121073", // The UNIX timestamp. Unit: seconds. This parameter takes e ffect only when syncType is set to HOT. "srcSuperAccount":"rds_admin", // The name of the privileged account of the primary ins tance. "srcSuperPassword":"rds_passd", // The password of the privileged account of the primar y instance. "dstSuperAccount":"rds_admin", // The name of the privileged account of the secondary i nstance. "dstSuperPassword":"rds_passd", // The password of the privileged account of the second ary instance. }
```

**AnalyticDB for MySQL V3.0**

```json
{ "entityType": "ADB3" "mainAccountName":"rds_admin", // The name of the account used to synchronize data from or to the primary instance. "mainAccountPassword":"rds_passd", // The password of the account used to synchronize d ata from or to the primary instance. "backupAccountName":"rds_admin", // The name of the account used to synchronize data fr om or to the secondary instance. "backupAccountPassword":"rds_passd", // The password of the account used to synchronize data from or to the secondary instance. }
```

**Cross-cloud DNS**

ASR for Geo-disaster Developer Apsara Stack Resilience

```json
{
    "entityType": "DNS", // The type of the synchronization entity.
    "srcZoneId": "e39d0b92-0cb8-4074-****-16d7d6****66", // The ID of the primary domai
n name.
    "zoneName": "xxx.xxx.com.", // The primary domain name.
    "mainInstanceId": "b9698b3f-0c13-****-aa50-751e****e730", // The DNS record ID of t
he primary domain name.
    "mainInstanceName": "cx", // The DNS record name of the primary domain name.
    "backupInstanceId": "b9698b3f-0c13-****-aa50-751e23****30", // The DNS record ID of
the secondary domain name.
    "backupInstanceName": "cx", // The DNS record name of the secondary domain name.
    "lineIds": "default", // The name of the DNS line.
    "rrSet": [
        "*.*.*.* 0",
        "*.*.*.* 100"
    ], // The values of the DNS record.
    "type": "A", // The type of the DNS record.
    "ttl": 30 // The time to live (TTL) of the DNS record.
}
```

**DNS within Cloud**

```json
{
    "entityType": "GLOBALDNS", // The type of the synchronization entity.
    "srcZoneId": "5ba01d2b-56ae-****-8257-cc****6d155b", // The ID of the primary domai
n name.
    "dstZoneId": "5ba01d2b-56ae-****-8257-cc88b****55b", // The ID of the secondary dom
ain name.
    "zoneName": "xxx.com.", // The primary/secondary domain name.
    "mainInstanceId": "f0fd1f88-****-436e-b8b1-4c377****64a", // The DNS record ID of t
he primary domain name.
    "mainInstanceName": "main", // The DNS record name of the primary domain name.
    "backupInstanceId": "f0fd1f88-****-436e-b8b1-4c377****64a", // The DNS record ID of
the secondary domain name.
    "backupInstanceName": "back", // The DNS record name of the secondary domain name.
    "lineIds": "default", // The name of the DNS line.
    "rrSet": [
        "xxx1.xxx.com. 0",
        "xxx2.xxx.com. 100"
    ], // The values of the DNS record.
    "type": "CNAME", // The type of the DNS record.
    "ttl": 30 // The TTL of the DNS record.
}
```

**DRDS**

Apsara Stack Resilience ASR for Geo-disaster Developer

```json
{ "entityType": "DRDS" "dstDrdsDBPassword": "db_passd" // The password of the destination database. "roAccounts":"[{"dbName": "a", "readonlyAccounts" : "u1,u2,u3"}]", // The read-only acc ounts. "syncObjects":"[{"dbName": "a", "excludeTables" : "t1,t2,t3"}]", // The objects to be s ynchronized. "checkpoint":"1714121073", // The UNIX timestamp. Unit: seconds. }
```

**ECS**

```json
{ "entityType": "ECS" "reuseHdrPg": false // Specifies whether to reuse the Hybrid Disaster Recovery (HDR) pr otection group. "hdrProtectGroupId": "err_id" // The ID of the HDR protection group. You can leave this parameter empty. "sitePairMainZoneId":"zoneID", // The zone ID of the primary region. "sitePairBackupZoneId":"zoneID", // The zone ID of the secondary region. "mainVpcId":"1714121073", // The virtual private cloud (VPC) ID of the primary region. "backupVpcId":"1714121073", // The VPC ID of the secondary region. "mainVSwitchId":"zoneID", // The vSwitch ID of the primary region. "backupVSwitchId":"zoneID", // The vSwitch ID of the secondary region. "mainSecurityGroupId":"1714121073", // The security group ID of the primary region. "backupSecurityGroupId":"1714121073", // The security group ID of the secondary region. "expectRpo": 200, // The expected latency of data synchronization. "replicaBandwidth": 1009, // The available bandwidth. "reuseSitePair": false, // Specifies whether to reuse the site pair. "sitePairId":"zoneID", // The ID of the site pair to be reused. You can leave this para meter empty. "mainEcsId":"id,id", // The Elastic Compute Service (ECS) instance IDs of the primary r egion. Separate multiple IDs with commas (,). "backupEcsId":"id,id", // The ECS instance IDs of the secondary region. Separate multip le IDs with commas (,). }
```

**Hologres**

```json
{ "entityType": "HOLOGRES" }
```

**Lindorm**

```json
{ "entityType": "LINDORM" "ltsId":"lts-test", // The Lindorm Tunnel Service (LTS) instance ID. "checkpoint":"1714121073" // The UNIX timestamp. Unit: seconds. }
```

ASR for Geo-disaster Developer Apsara Stack Resilience

**ApsaraDB for MongoDB**

```json
{ "entityType": "MONGODB" "roAccounts":"[{"dbName": "a", "readonlyAccounts" : "u1,u2,u3"}]", // The read-only acc ounts. "syncObjects":"[{"dbName": "a", "excludeTables" : "t1,t2,t3"}]", // The objects to be s ynchronized. "checkpoint":"1714121073", // The UNIX timestamp. Unit: seconds. "mainShardAccount":"rds_admin", // The name of the shard account of the primary instanc
```

`e.`

```json
"mainShardPassword":"rds_passd", // The password of the shard account of the primary in stance. "backupShardAccount":"rds_admin", // The name of the shard account of the secondary ins tance. "backupShardPassword":"rds_passd", // The password of the shard account of the secondar y instance. }
```

**ApsaraMQ**

```json
{ "entityType": "MQ" "mqTopics":"t1,t2" // The names of topics. Separate multiple names with commas (,). }
```

**DataWorks**

```json
{ "entityType": "ODPS" "cloudScene":"MULTIPLE_CLOUD/MULTIPLE_REGION" // The cloud scenario. Valid values: MULT IPLE_CLOUD and MULTIPLE_REGION. "mainTenantId": "Org-11783", // The primary tenant ID of DataWorks. "backupTenantId": "Org-11783", // The secondary tenant ID of DataWorks. "mainEngineName": "odsp-1,odsp-2", // The names of MaxCompute projects in the primary c loud. Separate multiple names with commas (,). "backupEngineName": "odps-1,odps-2", // The names of MaxCompute projects in the seconda ry cloud. Separate multiple names with commas (,). "syncTime": 1600 // The synchronization interval. Unit: seconds. "dataworkPolicy": "" // The synchronization policy of DataWorks resources. "maxComputePolicy": "" // The synchronization policy of MaxCompute resources. "nodeId": "" // The ID of the MaxCompute node. "nodeType": "" // The type of the MaxCompute node. }
```

**OSS**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED |

Apsara Stack Resilience ASR for Geo-disaster Developer

```json
{ "entityType": "OSS" "objectPrefixList":"[prefix,prefix2]" // The prefixes of the objects to be synchronized
```

.

```json
"replicationAction": "ALL/DELETE" // The operations to be synchronized. Valid values: A LL and PUT. }
```

**CDS-OSS**

```json
{ "entityType": "CDSOSS" "objectPrefixList":"[prefix,prefix2]" // The prefixes of the objects to be synchronized
```

.

```json
"replicationAction": "ALL/DELETE" // The operations to be synchronized. Valid values: A LL and PUT. }
```

**Tablestore**

```json
{ "entityType": "OTS" "tables":"t1,t2" // The names of the tables to be synchronized. Separate multiple names with commas (,). "checkpoint": "1714121073" // The UNIX timestamp. Unit: seconds. }
```

**ApsaraDB for Redis**

```json
{ "entityType": "REDIS" "roAccounts":"[{"dbName": "a", "readonlyAccounts" : "u1,u2,u3"}]", // The read-only acc ounts. "checkpoint":"1714121073", // The UNIX timestamp. Unit: seconds. }
```

**Response parameters**

| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
|---|---|---|---|
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
&ProtectGroupId=379e********98c7 &Direction=FORWARD &IsStop=true &SyncEntities=- &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

##### RemoveSyncEntity

Removes a synchronization entity.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| EntityId | Strin g | Quer y | Yes | e1********6d6d | The ID of the synchronization entity. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
&EntityId=e1********6d6d &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

#### Protection group switch

##### DescribeProtectGroupSwitch

Queries the information about a protection group switch, such as a switchover or switchback. This operation does not support failover or failback.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AsrMainCl oudInstan ceId | Strin g | Query | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AsrMainRe gionId | Strin g | Query | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Query | No | 3 | The organization ID. This is an API parameter of the Apsara Uni- manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Resource Group | Strin g | Query | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
| PlanId | Strin g | Query | No | bc6********00e7 | The ID of the switch. If you specify this parameter, the ProtectGroupId and SwitchType parameters are invalid. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProtectGr oupId | Strin g | Query | No | 379e********98c7 | The ID of the protection group. To use this parameter, the values of the PlanInstanceId and PlanId parameters must be empty. |
| SwitchTyp e | Strin g | Query | No | SWITCHOVER | The switch type. To use this parameter, the values of the PlanInstanceId and PlanId parameters must be empty. Valid values: SWITCHOVER SWITCHBACK |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct | - | The returned data. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| A | SR for Geo-disast Guide·API referen | er Developer ce |  | Apsara Stack Resilienc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -planTasks | Array | - | The details of the tasks that involve switchover or switchback in the protection group. |
| --taskNum | Integer | 12 | The number of tasks. |
| --taskName | String | Task1 | The name of the task. |
| --ipAddr | String | 127.0.0.1 | The IP address of the node that ran the task. |
| -- taskDescriptio n | String | XXX task | The description of the task. |
| --taskType | String | SWITCH | The type of the task. |
| --priority | Integer | 1 | The priority of the task. |
| --stage | String | S1 | The stage of the task. This parameter is returned only for the tasks that are run for the switchover of synchronization entities. Valid values: S1 and S2. |
| -planId | String | bc6********00e7 | The ID of the switchover or switchback. |
| -planName | String | Plan1 | The name of the switchover or switchback. |
| -planType | String | FAILOVER | The type of the switch. Valid values: FAILOVER FAILBACK SWITCHOVER SWITCHBACK |
| -description | String | XXX switch | The description of the switchover or switchback. |
| - protectGroupI d | String | 379e********98c7 | The ID of the protection group. |
| - protectGroupN ame | String | ProtectGroup1 | The name of the protection group. |

| A | psara Stack Resil | ience |  | ASR for Geo-disaster Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -createTime | String | 1673333258000 | The time when the switchover or switchback was created. |
| -mainRegionId | String | Region 01 _ | The region ID of the primary cloud. |
| - backupRegionI d | String | Region 02 _ | The region ID of the secondary cloud. |
| - priorityInfoMa p | Map | - | The order in which synchronization entities are switched in the switchover or switchback. |
| - relevancePlanI d | String | bc6********00e7 | The ID of the switchover or switchback. |
| - relevancePlan Name | String | Plan1 | The name of the switchover or switchback. |
| -mainCloudId | String | ebc6********00e7 | The ID of the primary cloud. |
| - backupCloudId | String | ebc6********00e8 | The ID of the secondary cloud. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeProtectGroupSwitch &<Common request parameters>
```

Sample success responses `JSON` format ASR for Geo-disaster Developer Apsara Stack Resilience

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "data":{
  "planType":"FAILOVER",
  "planName":"Plan1",
  "description":"XXX switch",
  "backupCloudId":"ebc6********00e8",
  "mainRegionId":"Region_01",
  "planTasks":{
   "taskType":"SWITCH",
   "stage":"S1",
   "taskDescription":"XXX task",
   "taskName":"Task1",
   "priority":1,
   "taskNum":12,
   "ipAddr":"127.0.0.1"
  },
  "priorityInfoMap":"",
  "mainCloudId":"ebc6********00e7",
  "protectGroupName":"ProtectGroup1",
  "createTime":"1673333258000",
  "relevancePlanName":"Plan1",
  "relevancePlanId":"bc6********00e7",
  "planId":"bc6********00e7",
  "protectGroupId":"379e********98c7",
  "backupRegionId":"Region_02"
 },
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <data>
 <planType>FAILOVER</planType>
 <planName>Plan1</planName>
 <description>XXX switch </description>
 <backupCloudId>ebc6********00e8</backupCloudId>
 <mainRegionId>Region_01</mainRegionId>
 <planTasks>
  <taskType>SWITCH</taskType>
  <stage>S1</stage>
  <taskDescription>XXX task</taskDescription>
  <taskName>Task1</taskName>
  <priority>1</priority>
  <taskNum>12</taskNum>
  <ipAddr>127.0.0.1</ipAddr>
 </planTasks>
 <priorityInfoMap  />
 <mainCloudId>ebc6********00e7</mainCloudId>
 <protectGroupName>ProtectGroup1</protectGroupName>
 <createTime>1673333258000</createTime>
 <relevancePlanName>Plan1</relevancePlanName>
 <relevancePlanId>bc6********00e7</relevancePlanId>
 <planId>bc6********00e7</planId>
 <protectGroupId>379e********98c7</protectGroupId>
 <backupRegionId>Region_02</backupRegionId>
</data> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### DescribeProtectGroupSwitchInstance

Queries the details of a protection group switch instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AsrMainCl oudInstan ceId | Strin g | Query | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AsrMainRe gionId | Strin g | Query | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Query | No | 3 | The organization ID. This is a parameter of the Apsara Stack API. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Resource Group | Strin g | Query | No | 3 | The ID of the resource set. This is a parameter of the Apsara Stack API. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | No | cn-hangzhou | The region ID of the resource. This is a parameter of the Apsara Stack API. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
| PlanInstan ceId | Strin g | Query | No | fs6********2dd4 | The ID of the switchover or switchback instance. If this parameter is specified, the PlanId, ProtectGroupId, and SwitchType parameters are invalid. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PlanId | Strin g | Query | No | bc6********00e7 | The switchover or switchback ID. To use this parameter, the value of the PlanInstanceId parameter must be empty. If you specify this parameter, the ProtectGroupId and SwitchType parameters are invalid. |
| ProtectGr oupId | Strin g | Query | No | 379e********98c7 | The ID of the protection group. To use this parameter, the values of the PlanInstanceId and PlanId parameters must be empty. |
| SwitchTyp e | Strin g | Query | No | SWITCHOVER | The switch type. To use this parameter, the values of the PlanInstanceId and PlanId parameters must be empty. Valid values: SWITCHOVER SWITCHBACK |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

Apsara Stack Resilience ASR for Geo-disaster Developer To call this operation, we recommend that you use the **ProtectGroupId** and **SwitchType** parameters.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct | - | The returned data. |
| -taskInfos | Array | - | The task execution information. |
| --startTime | Long | 1714360563 | The time when the task started. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -- durationInMilli s | Long | 10 | The duration of the task. Unit: milliseconds. |
| --progress | String | 0 | The progress of the switch. Only a value of 0 or 100 is returned. |
| --status | String | SUCCESS | The state of the switch. Valid values: SUCCESS NOTRUNNING RUNNING |
| --taskNum | Integer | 1 | The task ID. |
| --taskName | String | Task1 | The name of the task. |
| --ipAddr | String | 127.0.0.1 | The IP address of the node that ran the task. |
| -- taskDescriptio n | String | XXX task | The description of the task. |
| --taskType | String | SWITCH | The type of the task. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| A | psara Stack Resil | ience |  | ASR for Geo-disaster Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --priority | Integer | 1 | The priority of the task. |
| --stage | String | S1 | The stage of the task. This parameter is returned only for the tasks that are run for the switchover or failover of synchronization entities. Valid values: S1 and S2. |
| - currentTaskSt ep | String | 2 | The ID of the task that is running. |
| -restTime | String | 5000 | The estimated remaining execution time of the task. Unit: milliseconds. |
| - priorityInfoMa p | Map | - | The information about synchronization entities, in the JSON format. |
| - planInstanceSt atus | String | RUNNING | The state of the switch instance. Valid values: RUNNING SUCCESS |
| - planInstanceId | String | ebc6********00e7 | The ID of the switch instance. |
| -estimateTime | String | 100000 | The estimated completion time of the task. |
| -progress | String | 100 | The progress of the task. |
| -startTime | Long | 1714360563 | The time when the task started. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -endTime | Long | 1714360563 | The time when the task stopped. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| - activitiProInsId | String | - | A reserved parameter. This parameter is not returned. |

| SR for Geo-disast | er Developer |  |  |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -mainRegionId | String | cn-beijing | The region ID of the primary cloud. |
| - backupRegionI d | String | cn-hangzhou | The region ID of the secondary cloud. |
| -number | String | 2 | The sequence number of the task. |
| -continueTime | String | 10 | The duration of the task. |
| -rtoTime | String | 200000 | The execution duration of the task. Unit: milliseconds. |
| -planId | String | 3df6********00e7 | The switch ID. |
| -planName | String | Plan1 | The name of the switch. |
| -description | String | Plan1-DESC | The description of the switch. |
| - protectGroupI d | String | f46g********f9k2 | The ID of the protection group. |
| - protectGroupN ame | String | PG-NAME | The name of the protection group. |
| - resourceGroup Name | String | res-xx | The name of the resource group. |
| -deploymentId | String | 2 | A reserved parameter. |
| -createTime | String | 1714360563231 | The time when the resource group was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -status | String | IDLE | The state of the switch. Valid values: IDLE RUNNING |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -stepStatus | String | RUNNING | The execution state of the task. Valid values: RUNNING SUCCESS FAILED |
| -planType | String | SWITCHOVER | The type of the switch. Valid values: SWITCHOVER SWITCHBACK |
| - planInstanceN um | String | 2 | The instance ID. |
| - latestPlanInsta nceId | String | ebc6********00e7 | The ID of the previous switch instance. |
| -entityType | String | - | A reserved parameter. |
| -planStatus | String | IDLE | The state of the switch. Valid values: IDLE RUNNING |
| -cloudId | String | ebc6********00e7 | The cloud ID. |
| -failoverMode | String | - | A reserved parameter. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeProtectGroupSwitchInstance &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "data":{
  "continueTime":"10",
  "failoverMode":"-",
  "planName":"Plan1",
  "description":"Plan1-DESC",
```

"l

```
Stt ""IDLE"
```

ASR for Geo-disaster Developer Apsara Stack Resilience

```json
  "planStatus":"IDLE",
  "taskInfos":{
   "taskType":"SWITCH",
   "stage":"S1",
   "durationInMillis":10,
   "taskDescription":"XXX task",
   "progress":"0",
   "startTime":1714360563,
   "taskName":"Task1",
   "priority":1,
   "taskNum":1,
   "ipAddr":"127.0.0.1",
   "status":"SUCCESS"
  },
  "mainRegionId":"cn-beijing",
  "priorityInfoMap":"",
  "number":"2",
  "currentTaskStep":"2",
  "deploymentId":"2",
  "cloudId":"ebc6********00e7",
  "startTime":1714360563,
  "planId":"3df6********00e7",
  "protectGroupId":"f46g********f9k2",
  "backupRegionId":"cn-hangzhou",
  "stepStatus":"RUNNING",
  "planInstanceId":"ebc6********00e7",
  "planInstanceNum":"2",
  "restTime":"5000",
  "resourceGroupName":"res-xx",
  "planType":"SWITCHOVER",
  "estimateTime":"100000",
  "rtoTime":"200000",
  "entityType":"-",
  "latestPlanInstanceId":"ebc6********00e7",
  "planInstanceStatus":"RUNNING",
  "activitiProInsId":"-",
  "protectGroupName":"PG-NAME",
  "createTime":"1714360563231",
  "progress":"100",
  "endTime":1714360563,
  "status":"IDLE"
 },
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format Apsara Stack Resilience ASR for Geo-disaster Developer

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <data>
 <continueTime>10</continueTime>
 <failoverMode>-</failoverMode>
 <planName>Plan1</planName>
 <description>Plan1-DESC</description>
 <planStatus>IDLE</planStatus>
 <taskInfos>
  <taskType>SWITCH</taskType>
  <stage>S1</stage>
  <durationInMillis>10</durationInMillis>
  <taskDescription>XXX task</taskDescription>
  <progress>0</progress>
  <startTime>1714360563</startTime>
  <taskName>Task1</taskName>
  <priority>1</priority>
  <taskNum>1</taskNum>
  <ipAddr>127.0.0.1</ipAddr>
  <status>SUCCESS</status>
 </taskInfos>
 <mainRegionId>cn-beijing</mainRegionId>
 <priorityInfoMap  />
 <number>2</number>
 <currentTaskStep>2</currentTaskStep>
 <deploymentId>2</deploymentId>
 <cloudId>ebc6********00e7</cloudId>
 <startTime>1714360563</startTime>
 <planId>3df6********00e7</planId>
 <protectGroupId>f46g********f9k2</protectGroupId>
 <backupRegionId>cn-hangzhou</backupRegionId>
 <stepStatus>RUNNING</stepStatus>
 <planInstanceId>ebc6********00e7</planInstanceId>
 <planInstanceNum>2</planInstanceNum>
 <restTime>5000</restTime>
 <resourceGroupName>res-xx</resourceGroupName>
 <planType>SWITCHOVER</planType>
 <estimateTime>100000</estimateTime>
 <rtoTime>200000</rtoTime>
 <entityType>-</entityType>
 <latestPlanInstanceId>ebc6********00e7</latestPlanInstanceId>
 <planInstanceStatus>RUNNING</planInstanceStatus>
 <activitiProInsId>-</activitiProInsId>
 <protectGroupName>PG-NAME</protectGroupName>
 <createTime>1714360563231</createTime>
 <progress>100</progress>
 <endTime>1714360563</endTime>
 <status>IDLE</status>
</data> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AsrMainCl oudInstan ceId | Strin g | Query | No | f8f72032-5e49-4a38- 9750-f8a*****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

ASR for Geo-disaster Developer Apsara Stack Resilience

##### StartProtectGroupSwitch

Starts protection group switchover or switchback.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AsrMainRe gionId | Strin g | Query | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|  |  |  |  |  | The organization ID. This is a parameter of the Apsara Stack API. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Parame Dteerpartme nt | Typ Setrin g | Positi on Query | Require d No | Example 3 | indicate that the Deresscoruirpctei odones not exist. If you do not |
|---|---|---|---|---|---|
|  |  |  |  |  | specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account |
|  |  |  |  |  | within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Resource Group | Strin g | Query | No | 3 | The ID of the resource set. This is a parameter of the Apsara Stack API. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | No | cn-hangzhou | The region ID of the resource. This is a parameter of the Apsara Stack API. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
| PlanId | Strin g | Body | No | e3f4*******dj8s | The switch ID of the protection group. If this parameter is specified, the ProtectGroupId and SwitchType parameters are invalid. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProtectGr oupId | Strin g | Body | No | d19k*******9xj7 | The ID of the protection group. To specify the ProtectGroupId and SwitchType parameters, the PlanId parameter must be empty. |
| SwitchTyp e | Strin g | Body | No | SWITCHOVER | The switch type. To specify the ProtectGroupId and SwitchType parameters, the PlanId parameter must be empty. Valid values: SWITCHOVER SWITCHBACK |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct | - | The returned data. |
| - planInstanceId | String | ebc6********00e7 | The ID of the switch instance that was started. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=StartProtectGroupSwitch &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "data":{
  "planInstanceId":"ebc6********00e7"
 },
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <data>
 <planInstanceId>ebc6********00e7</planInstanceId>
</data> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

### Disaster recovery plans

#### Plan management

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

##### DeleteRecoveryPlan

Deletes a disaster recovery plan.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| Id | Long | Quer y | Yes | 379****31233246 | The ID of the disaster recovery plan that you want to delete. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | a62a********bcd1 | The request ID. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteRecoveryPlan &Id=379****31233246 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "requestId":"a62a********bcd1",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <requestId>a62a********bcd1</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### GetRecoveryPlan

Queries the information about a disaster recovery plan.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| Id | Long | Quer y | Yes | 1234567 | The ID of the disaster recovery plan. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | 123456789 | The request ID. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. |
| nodeHost | String | localhost:8080 | The name of the node that processed the request. |
| nodeIp | String | 192.168.1.1 | The IP address of the node that processed the request. |
| data | Struct |  | The data of the disaster recovery plan. |
| -sequence | Normal |  | The steps of the disaster recovery plan, in the JSON format. |
| - relatedProtect Groups | Array |  | The protection groups that are associated with the disaster recovery plan. |
| -- aliyunAccount Uid | String | 1785******267796 | The unique ID (UID) of the Apsara Stack tenant account to which the protection group belongs. |
| --ownerUid | String | 2397******988687 32 | The UID of the protection group owner. |
| --creator | String | 2397******988687 32 | The UID of the user who created the protection group. |
| --lastModifier | String | 2397******988687 32 | The UID of the user who last modified the protection group. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| -- resourceRegio nId | String | cn-hangzhou | The region ID of the protection group. |
|---|---|---|---|
| -- resourceGroup Id | String | 103 | The ID of the resource group to which the protection group belongs. |
| --createdDate | Long | 1713514782222 | The time when the protection group was created. |
| -- lastModifiedDa te | Long | 1713514782222 | The time when the protection group was last modified. |
| --instanceId | String | e250008c-a02a- 455c-b957- 8*****4ef58 | The ID of the protection group. |
| --id | String | e250008c-a02a- 455c-b957- 8*****4ef58 | The ID of the protection group. |
| --name | String | name1 | The name of the protection group. |
| - aliyunAccount Uid | String | 1785111957*****2 36 | The UID of the Apsara Stack tenant account to which the resource belongs. |
| -ownerUid | String | 239724*****88687 32 | The UID of the resource owner. |
| -creator | String | 239724*****88687 32 | The UID of the user who created the resource. |
| -lastModifier | String | 239724*****88687 32 | The UID of the user who last modified the resource. |
| - resourceRegio nId | String | cn-hangzhou | The region ID of the resource. |
| - resourceGroup Id | String | 103 | The ID of the resource group to which the resource belongs. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| -createdDate | Long | 1713514782222 | The time when the resource was created. |
|---|---|---|---|
| - lastModifiedDa te | Long | 1713514782222 | The time when the resource was last modified. |
| -instanceId | String | e250008c-a02a- 455c-b957- 8d*****ef58 | The instance ID of the resource. |
| -id | String | e250008c-a02a- 455c-b957- 8d*****ef58 | The ID of the disaster recovery plan. |
| -name | String | MyInstance | The name of the disaster recovery plan. |
| -type | String | DRILL ONLY _ | The type of the disaster recovery plan. Valid values: DRILL ONLY _ DRILL AND DR _ _ |
| -stability | String | GREEN | The stability of the disaster recovery plan. Valid values: GREEN: stable. GRAY: unknown. RED: unstable. |
| -description | String | This is an example instance. | The description of the disaster recovery plan. |
| -mainRegion | Struct |  | The information about the primary region. |
| --pk | String | 33994422***27712 | The primary key of the primary cloud instance. |
| --regionId | String | cn-guznagxi | The region ID of the primary cloud. |
| --regionName | String | guznagxi | The region name of the primary cloud. |
| --regionType | String | UNIT | The type of the region. Valid values: CENTRAL UNIT |

ASR for Geo-disaster Developer Apsara Stack Resilience

| --consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |
|---|---|---|---|
| -- consoleApiEnd point | String | http://example.co m/******** | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |
| -- cloudInstance | Struct |  | The information about the primary cloud instance. |
| --- aliyunAccount Uid | String | 178511195******9 6 | The UID of the Apsara Stack tenant account to which the primary cloud instance belongs. |
| ---ownerUid | String | 23972451*****687 32 | The UID of the owner of the primary cloud instance. |
| ---creator | String | 23972451*****687 32 | The UID of the user who created the primary cloud instance. |
| ---lastModifier | String | 23972451*****687 32 | The UID of the user who last modified the primary cloud instance. |
| --- resourceRegio nId | String | cn-hangzhou | The region ID of the primary cloud instance. |
| --- resourceGroup Id | String | 103 | The ID of the resource group to which the primary cloud instance belongs. |
| ---createdDate | Long | 1704366334000 | The time when the primary cloud instance was created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| --- lastModifiedDa te | Long | 1704366334000 | The time when the primary cloud instance was last modified. |
|---|---|---|---|
| ---instanceId | String | e250008c-a02a- 455c-b957- 8d*****4ef58 | The ID of the primary cloud instance. |
| --- instanceName | String | XXX | The name of the primary cloud instance. |
| ---pk | String | 339944229200627 712 | The primary key of the primary cloud instance. |
| --- cloudUniqueId | String | 0179 | The UID of the primary cloud. |
| ---cloudOsType | String | ENTERPRISE | The edition of the primary cloud instance. Only ENTERPRISE may be returned, which indicates Apsara Stack. |
| ---version | String | 1.0.0 | The version number of the primary cloud instance. |
| ---consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |
| --- consoleApiEnd point | String | http://example.co m/******** | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| --- adminCredenti alsId | String | 339944225551583 232 | The credential ID of the cloud management administrator. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of an operations administrator. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as the operations administrator, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |
|---|---|---|---|
| --- accountCrede ntialsId | String | 339944229083187 200 | The credential ID of the organization account. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of a level-1 organization. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as an organization administrator. In the top navigation bar, click Enterprise. In the left-side navigation pane, choose Resources > Organizations. On the page that appears, obtain an AccessKey pair of a level-1 organization. |
| --- internetDomai n | String | inter.***.shuguang. com | The Internet domain name. |
| --- intranetDomai n | String | intra.***.shuguang. com | The internal domain name. |
| ---status | String | REGULAR | The status of the primary cloud instance. Valid values: REGULAR: normal. NOT CONFIGURED: not configured. _ UNINITIALIZED: not initialized. The cloud instance is in this state if no administrator credentials are configured when you log on to ASR-DR for the first time. |
| -backupRegion | Struct |  | The information about the secondary region. |
| --pk | String | 33994422***27712 | The primary key of the secondary cloud instance. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| --regionId | String | cn-guznagxi | The region ID of the secondary cloud. |
|---|---|---|---|
| --regionName | String | guznagxi | The region name of the secondary cloud. |
| --regionType | String | UNIT | The type of the region. Valid values: CENTRAL UNIT |
| --consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |
| -- consoleApiEnd point | String | http://example.co m/******** | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |
| -- cloudInstance | Struct |  | The information about the secondary cloud instance. |
| --- aliyunAccount Uid | String | 178511195******9 6 | The UID of the Apsara Stack tenant account to which the secondary cloud instance belongs. |
| ---ownerUid | String | 23972451*****687 32 | The UID of the owner of the secondary cloud instance. |
| ---creator | String | 23972451*****687 32 | The UID of the user who created the secondary cloud instance. |
| ---lastModifier | String | 23972451*****687 32 | The UID of the user who last modified the secondary cloud instance. |
| --- resourceRegio nId | String | cn-hangzhou | The region ID of the secondary cloud instance. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| --- resourceGroup Id | String | 103 | The ID of the resource group to which the secondary cloud instance belongs. |
|---|---|---|---|
| ---createdDate | Long | 1704366334000 | The time when the secondary cloud instance was created. |
| --- lastModifiedDa te | Long | 1704366334000 | The time when the secondary cloud instance was last modified. |
| ---instanceId | String | e250008c-a02a- 455c-b957- 8d*****4ef58 | The ID of the secondary cloud instance. |
| --- instanceName | String | XXX | The name of the secondary cloud instance. |
| ---pk | String | 339944229200627 712 | The primary key of the secondary cloud instance. |
| --- cloudUniqueId | String | 0179 | The UID of the secondary cloud. |
| ---cloudOsType | String | ENTERPRISE | The edition of the secondary cloud instance. Only ENTERPRISE may be returned, which indicates Apsara Stack. |
| ---version | String | 1.0.0 | The version number of the secondary cloud instance. |
| ---consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |
| --- consoleApiEnd point | String | http://example.co m/******** | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| --- adminCredenti alsId | String | 339944225551583 232 | The credential ID of the cloud management administrator. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of an operations administrator. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as the operations administrator, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |
|---|---|---|---|
| --- accountCrede ntialsId | String | 339944229083187 200 | The credential ID of the organization account. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of a level-1 organization. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as an organization administrator. In the top navigation bar, click Enterprise. In the left-side navigation pane, choose Resources > Organizations. On the page that appears, obtain an AccessKey pair of a level-1 organization. |
| --- internetDomai n | String | inter.***.shuguang. com | The Internet domain name. |
| --- intranetDomai n | String | intra.***.shuguang. com | The internal domain name. |
| ---status | String | REGULAR | The status of the secondary cloud instance. Valid values: REGULAR: normal. NOT CONFIGURED: not configured. _ UNINITIALIZED: not initialized. The cloud instance is in this state if no administrator credentials are configured when you log on to ASR-DR for the first time. |
| -latestTask | Struct |  | The status of the task that was last run for the plan. If null is returned, no task is run for the plan. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| -- sequenceTask s | Normal |  | The tasks that were run for steps, in the JSON format. |
|---|---|---|---|
| --taskId | String | 21 | The task ID. |
| -- recoveryPlanId | String | 19 | The ID of the disaster recovery plan. |
| --createsAt | Long | 1675393101718 | The time when the task was created. |
| --runsAt | Long | 1675393101718 | The time when the task started. |
| --completesAt | Long | 1675393101720 | The time when the task was complete. |
| --status | String | PENDING | The status of the task. Valid values: PENDING INITIALIZING RUNNING SWITCHING OVER _ WAITING RECOVER _ SWITCHING BACK _ ABORTING ABORTED TIMEOUT FAILED COMPLETED |
| --statusMsg | String | Development test ABCD | The description of the task. |
| -- exceptionThro wn | Boolean | true | Indicates whether an exception was thrown when the task was running. Valid values: true false |
| -- exceptionMsg | String | 400 | The error message returned if an exception was thrown. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| --nodeId | String | Local 001 _ | The ID of the node that was processing the task. |
|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
&Id=1234567 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"localhost:8080",
 "code":"200",
 "data":{
  "-backupRegion":{
   "regionId":"cn-guznagxi",
   "regionType":"UNIT",
   "consoleApiEndpoint":"http://example.com/********",
   "regionName":"guznagxi",
   "pk":"33994422***27712",
   "--cloudInstance":{
    "cloudUniqueId":"0179",
    "creator":"23972451*****68732",
    "lastModifiedDate":1704366334000,
    "instanceName":" XXX",
    "consoleApiEndpoint":"http://example.com/********",
    "resourceRegionId":"cn-hangzhou",
    "lastModifier":"23972451*****68732",
    "adminCredentialsId":"339944225551583232",
    "version":"1.0.0",
    "cloudOsType":"ENTERPRISE",
    "createdDate":1704366334000,
    "instanceId":"e250008c-a02a-455c-b957-8d*****4ef58",
    "aliyunAccountUid":"178511195******96",
    "internetDomain":"inter.***.shuguang.com",
    "resourceGroupId":"103",
    "pk":"339944229200627712",
    "intranetDomain":"intra.***.shuguang.com",
    "ownerUid":"23972451*****68732",
    "accountCredentialsId":"339944229083187200",
    "consoleType":"ASCM",
    "status":"REGULAR"
   },
   "consoleType":"ASCM"
  },
  "creator":"239724*****8868732",
  "lastModifiedDate":1713514782222,
"-mainRegion":{
```

Apsara Stack Resilience ASR for Geo-disaster Developer

```json
mainRegion:{
   "regionId":"cn-guznagxi",
   "regionType":"UNIT",
   "consoleApiEndpoint":"http://example.com/********",
   "regionName":"guznagxi",
   "pk":"33994422***27712",
   "--cloudInstance":{
    "cloudUniqueId":"0179",
    "creator":"23972451*****68732",
    "lastModifiedDate":1704366334000,
    "instanceName":" XXX",
    "consoleApiEndpoint":"http://example.com/********",
    "resourceRegionId":"cn-hangzhou",
    "lastModifier":"23972451*****68732",
    "adminCredentialsId":"339944225551583232",
    "version":"1.0.0",
    "cloudOsType":"ENTERPRISE",
    "createdDate":1704366334000,
    "instanceId":"e250008c-a02a-455c-b957-8d*****4ef58",
    "aliyunAccountUid":"178511195******96",
    "internetDomain":"inter.***.shuguang.com",
    "resourceGroupId":"103",
    "pk":"339944229200627712",
    "intranetDomain":"intra.***.shuguang.com",
    "ownerUid":"23972451*****68732",
    "accountCredentialsId":"339944229083187200",
    "consoleType":"ASCM",
    "status":"REGULAR"
   },
   "consoleType":"ASCM"
  },
  "resourceRegionId":"cn-hangzhou",
  "lastModifier":"239724*****8868732",
  "description":"This is an example instance.",
  "type":"DRILL_ONLY",
  "-relatedProtectGroups":{
   "creator":"2397******98868732",
   "createdDate":1713514782222,
   "instanceId":"e250008c-a02a-455c-b957-8*****4ef58",
   "lastModifiedDate":1713514782222,
   "aliyunAccountUid":"1785******267796",
   "resourceRegionId":"cn-hangzhou",
   "name":"name1",
   "lastModifier":"2397******98868732",
   "resourceGroupId":"103",
   "id":"e250008c-a02a-455c-b957-8*****4ef58",
   "ownerUid":"2397******98868732"
  },
  "sequence":"",
  "createdDate":1713514782222,
  "instanceId":"e250008c-a02a-455c-b957-8d*****ef58",
  "aliyunAccountUid":"1785111957*****236",
  "name":"MyInstance",
  "resourceGroupId":"103",
  "id":"e250008c-a02a-455c-b957-8d*****ef58",
```

ASR for Geo-disaster Developer Apsara Stack Resilience ,

```json
  "-latestTask":{
   "createsAt":1675393101718,
   "completesAt":1675393101720,
   "exceptionThrown":true,
   "exceptionMsg":"400",
   "statusMsg":"Development test ABCD",
   "runsAt":1675393101718,
   "sequenceTasks":"",
   "nodeId":"Local_001",
   "taskId":"21",
   "recoveryPlanId":"19",
   "status":"PENDING"
  },
  "ownerUid":"239724*****8868732",
  "stability":"GREEN"
 },
 "requestId":"123456789",
 "success":true,
 "nodeIp":"192.168.1.1"
}
```

`XML` format

```xml
<result>SUCCESS</result> <nodeHost>localhost:8080</nodeHost> <code>200</code> <data>
 <-backupRegion>
  <regionId>cn-guznagxi</regionId>
  <regionType>UNIT</regionType>
  <consoleApiEndpoint>http://example.com/********</consoleApiEndpoint>
  <regionName>guznagxi</regionName>
  <pk>33994422***27712</pk>
  <--cloudInstance>
   <cloudUniqueId>0179</cloudUniqueId>
   <creator>23972451*****68732</creator>
   <lastModifiedDate>1704366334000</lastModifiedDate>
   <instanceName> XXX</instanceName>
   <consoleApiEndpoint>http://example.com/********</consoleApiEndpoint>
   <resourceRegionId>cn-hangzhou</resourceRegionId>
   <lastModifier>23972451*****68732</lastModifier>
   <adminCredentialsId>339944225551583232</adminCredentialsId>
   <version>1.0.0</version>
   <cloudOsType>ENTERPRISE</cloudOsType>
   <createdDate>1704366334000</createdDate>
   <instanceId>e250008c-a02a-455c-b957-8d*****4ef58</instanceId>
   <aliyunAccountUid>178511195******96</aliyunAccountUid>
   <internetDomain>inter.***.shuguang.com</internetDomain>
   <resourceGroupId>103</resourceGroupId>
   <pk>339944229200627712</pk>
   <intranetDomain>intra.***.shuguang.com</intranetDomain>
   <ownerUid>23972451*****68732</ownerUid>
   <accountCredentialsId>339944229083187200</accountCredentialsId>
<consoleType>ASCM</consoleType>
```

Apsara Stack Resilience ASR for Geo-disaster Developer

```xml
   <consoleType>ASCM</consoleType>
   <status>REGULAR</status>
  </--cloudInstance>
  <consoleType>ASCM</consoleType>
 </-backupRegion>
 <creator>239724*****8868732</creator>
 <lastModifiedDate>1713514782222</lastModifiedDate>
 <-mainRegion>
  <regionId>cn-guznagxi</regionId>
  <regionType>UNIT</regionType>
  <consoleApiEndpoint>http://example.com/********</consoleApiEndpoint>
  <regionName>guznagxi</regionName>
  <pk>33994422***27712</pk>
  <--cloudInstance>
   <cloudUniqueId>0179</cloudUniqueId>
   <creator>23972451*****68732</creator>
   <lastModifiedDate>1704366334000</lastModifiedDate>
   <instanceName> XXX</instanceName>
   <consoleApiEndpoint>http://example.com/********</consoleApiEndpoint>
   <resourceRegionId>cn-hangzhou</resourceRegionId>
   <lastModifier>23972451*****68732</lastModifier>
   <adminCredentialsId>339944225551583232</adminCredentialsId>
   <version>1.0.0</version>
   <cloudOsType>ENTERPRISE</cloudOsType>
   <createdDate>1704366334000</createdDate>
   <instanceId>e250008c-a02a-455c-b957-8d*****4ef58</instanceId>
   <aliyunAccountUid>178511195******96</aliyunAccountUid>
   <internetDomain>inter.***.shuguang.com</internetDomain>
   <resourceGroupId>103</resourceGroupId>
   <pk>339944229200627712</pk>
   <intranetDomain>intra.***.shuguang.com</intranetDomain>
   <ownerUid>23972451*****68732</ownerUid>
   <accountCredentialsId>339944229083187200</accountCredentialsId>
   <consoleType>ASCM</consoleType>
   <status>REGULAR</status>
  </--cloudInstance>
  <consoleType>ASCM</consoleType>
 </-mainRegion>
 <resourceRegionId>cn-hangzhou</resourceRegionId>
 <lastModifier>239724*****8868732</lastModifier>
 <description>This is an example instance.</description>
 <type>DRILL_ONLY</type>
 <-relatedProtectGroups>
  <creator>2397******98868732</creator>
  <createdDate>1713514782222</createdDate>
  <instanceId>e250008c-a02a-455c-b957-8*****4ef58</instanceId>
  <lastModifiedDate>1713514782222</lastModifiedDate>
  <aliyunAccountUid>1785******267796</aliyunAccountUid>
  <resourceRegionId>cn-hangzhou</resourceRegionId>
  <name>name1</name>
  <lastModifier>2397******98868732</lastModifier>
  <resourceGroupId>103</resourceGroupId>
  <id>e250008c-a02a-455c-b957-8*****4ef58</id>
  <ownerUid>2397******98868732</ownerUid>
</-relatedProtectGroups>
```

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

```xml
 </relatedProtectGroups>
 <sequence  />
 <createdDate>1713514782222</createdDate>
 <instanceId>e250008c-a02a-455c-b957-8d*****ef58</instanceId>
 <aliyunAccountUid>1785111957*****236</aliyunAccountUid>
 <name>MyInstance</name>
 <resourceGroupId>103</resourceGroupId>
 <id>e250008c-a02a-455c-b957-8d*****ef58</id>
 <-latestTask>
  <createsAt>1675393101718</createsAt>
  <completesAt>1675393101720</completesAt>
  <exceptionThrown>true</exceptionThrown>
  <exceptionMsg>400</exceptionMsg>
  <statusMsg>Development test ABCD</statusMsg>
  <runsAt>1675393101718</runsAt>
  <sequenceTasks  />
  <nodeId>Local_001</nodeId>
  <taskId>21</taskId>
  <recoveryPlanId>19</recoveryPlanId>
  <status>PENDING</status>
 </-latestTask>
 <ownerUid>239724*****8868732</ownerUid>
 <stability>GREEN</stability>
</data> <requestId>123456789</requestId> <success>true</success> <nodeIp>192.168.1.1</nodeIp>
```

Asrdr 2023-10-01

##### ListRecoveryPlanByPage

Queries a list of disaster recovery plans by page.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |
|---|---|---|---|---|---|
| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is a parameter of the Apsara Stack API. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is a parameter of the Apsara Stack API. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is a parameter of the Apsara Stack API. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| InstanceId | Long | Quer y | No | e250008c-a02a-455c- b957-8*****4ef58 | The ID of the disaster recovery plan. This parameter is used to query data in exact match mode. |
| Name | Strin g | Quer y | No | OSS switchover plan | The name of the disaster recovery plan. This parameter is used to query data in fuzzy match mode. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Type | Strin g | Quer y | No | DRILL ONLY _ | The type of the disaster recovery plan. This parameter is used to query data in exact match mode. Valid values: DRILL ONLY _ DRILL AND DR _ _ |
|---|---|---|---|---|---|
| LatestTask Status | Strin g | Quer y | No | RUNNING | The state of the disaster recovery plan. This parameter is used to query data in exact match mode. You can specify one or more values. Separate multiple values with commas ( , ). A value of NAN specifies that plans that are not run are queried. |
| Sort | Strin g | Quer y | No | createdDate | The sorting field. Set the value to createdDate. |
| Order | Strin g | Quer y | No | ASC | The sorting order. Valid values: ASC DESC |
| PageNum | Integ er | Quer y | Yes | 1 | The page number. Pages start from page 1. |
| PageSize | Integ er | Quer y | Yes | 10 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The returned data. |
| -rows | Array |  | The queried results. |
| --sequence | Normal |  | The steps of the disaster recovery plan, in the JSON format. |
| -- relatedProtect Groups | Array |  | The protection groups that are associated with the disaster recovery plan. |
| --- aliyunAccount Uid | String | 1785******267796 | The unique ID (UID) of the Apsara Stack tenant account to which the protection group belongs. |
| ---ownerUid | String | 2397******988687 32 | The UID of the protection group owner. |
| ---creator | String | 2397******988687 32 | The UID of the user who created the protection group. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| ---lastModifier | String | 2397******988687 32 | The UID of the user who last modified the protection group. |
|---|---|---|---|
| --- resourceRegio nId | String | cn-hangzhou | The region ID of the protection group. |
| --- resourceGroup Id | String | 103 | The ID of the resource group to which the protection group belongs. |
| ---createdDate | Long | 1713514782222 | The time when the protection group was created. |
| --- lastModifiedDa te | Long | 1713514782222 | The time when the protection group was last modified. |
| ---instanceId | String | e250008c-a02a- 455c-b957- 8*****4ef58 | The ID of the protection group. |
| ---id | String | e250008c-a02a- 455c-b957- 8*****4ef58 | The ID of the protection group. |
| ---name | String | name1 | The name of the protection group. |
| -- aliyunAccount Uid | String | 1785111957*****2 36 | The UID of the Apsara Stack tenant account to which the resource belongs. |
| --ownerUid | String | 239724*****88687 32 | The UID of the resource owner. |
| --creator | String | 239724*****88687 32 | The UID of the user who created the resource. |
| --lastModifier | String | 239724*****88687 32 | The UID of the user who last modified the resource. |
| -- resourceRegio nId | String | cn-hangzhou | The region ID of the resource. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| -- resourceGroup Id | String | 103 | The ID of the resource group to which the resource belongs. |
|---|---|---|---|
| --createdDate | Long | 1713514782222 | The time when the resource was created. |
| -- lastModifiedDa te | Long | 1713514782222 | The time when the resource was last modified. |
| --instanceId | String | e250008c-a02a- 455c-b957- 8d*****ef58 | The instance ID of the resource. |
| --id | String | e250008c-a02a- 455c-b957- 8d*****ef58 | The ID of the disaster recovery plan. |
| --name | String | MyInstance | The name of the disaster recovery plan. |
| --type | String | DRILL ONLY _ | The type of the disaster recovery plan. Valid values: DRILL ONLY _ DRILL AND DR _ _ |
| --stability | String | GREEN | The stability of the disaster recovery plan. Valid values: GREEN: stable. GRAY: unknown. RED: unstable. |
| --description | String | This is an example instance. | The description of the disaster recovery plan. |
| --mainRegion | Struct |  | The information about the primary region. |
| ---pk | String | 33994422***27712 | The primary key of the primary cloud instance. |
| ---regionId | String | cn-guznagxi | The region ID of the primary cloud. |
| ---regionName | String | guznagxi | The region name of the primary cloud. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| ---regionType | String | CENTRAL | The type of the region. Valid values: CENTRAL UNIT |
|---|---|---|---|
| ---consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. This type is generally used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. This type is generally used in cross- cloud disaster recovery scenarios. |
| --- consoleApiEnd point | String | http://internal.exa mple.com-XXXXX | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |
| --- cloudInstance | Struct |  | The information about the primary cloud instance. |
| ---- aliyunAccount Uid | String | 178511195******9 6 | The UID of the Apsara Stack tenant account to which the primary cloud instance belongs. |
| ----ownerUid | String | 23972451*****687 32 | The UID of the owner of the primary cloud instance. |
| ----creator | String | 23972451*****687 32 | The UID of the user who created the primary cloud instance. |
| ----lastModifier | String | 23972451*****687 32 | The UID of the user who last modified the primary cloud instance. |
| ---- resourceRegio nId | String | cn-hangzhou | The region ID of the secondary cloud instance. |
| ---- resourceGroup Id | String | 103 | The ID of the resource group to which the primary cloud instance belongs. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| ---- createdDate | Long | 1673333258000 | The time when the primary cloud instance was created. |
|---|---|---|---|
| ---- lastModifiedDa te | Long | 1673333258012 | The time when the primary cloud instance was last modified. |
| ----instanceId | String | 79e********98c7 | The ID of the primary cloud instance. |
| ---- instanceName | String | XXX | The name of the primary cloud instance. |
| ----pk | String | 339944229200627 712 | The primary key of the secondary cloud instance. |
| ---- cloudUniqueId | String | 0179 | The UID of the primary cloud. |
| ---- cloudOsType | String | ENTERPRISE | The edition of the cloud instance. Only ENTERPRISE may be returned, which indicates Apsara Stack. |
| ----version | String | 1.0.0 | The version number of the primary cloud instance. |
| ---- consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. This type is generally used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. This type is generally used in cross- cloud disaster recovery scenarios. |
| ---- consoleApiEnd point | String | http://internal.exa mple.com-XXXXX | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| ---- adminCredenti alsId | String | 339944225551583 232 | The credential ID of the cloud management administrator. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of an operations administrator. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as the operations administrator, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |
|---|---|---|---|
| ---- accountCrede ntialsId | String | 339944229083187 200 | The credential ID of the organization account. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of a level-1 organization. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as an organization administrator. In the top navigation bar, click Enterprise. In the left-side navigation pane, choose Resources > Organizations. On the page that appears, obtain an AccessKey pair of a level-1 organization. |
| ---- internetDomai n | String | inter.***.example.c om | The Internet domain name. |
| ---- intranetDomai n | String | intra.***.example.c om | The internal domain name. |
| ----status | String | REGULAR | The state of the cloud instance. Valid values: REGULAR: normal. NOT CONFIGURED: not configured. _ UNINITIALIZED: not initialized. The cloud instance is in this state if no administrator credentials are configured when you log on to ASR-DR for the first time. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| -- backupRegion | Struct |  | The information about the secondary region. |
|---|---|---|---|
| ---pk | String | 33994422***27712 | The primary key of the secondary cloud instance. |
| ---regionId | String | cn-guznagxi | The region ID of the secondary cloud. |
| ---regionName | String | guznagxi | The region name of the secondary cloud. |
| ---regionType | String | CENTRAL | The type of the region. Valid values: CENTRAL UNIT |
| ---consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. This type is generally used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. This type is generally used in cross- cloud disaster recovery scenarios. |
| --- consoleApiEnd point | String | http://internal.exa mple.com-XXXXX | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |
| --- cloudInstance | Struct |  | The information about the secondary cloud instance. |
| ---- aliyunAccount Uid | String | 178511195******9 6 | The UID of the Apsara Stack tenant account to which the secondary cloud instance belongs. |
| ----ownerUid | String | 23972451*****687 32 | The UID of the owner of the secondary cloud instance. |
| ----creator | String | 23972451*****687 32 | The UID of the user who created the secondary cloud instance. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| ----lastModifier | String | 23972451*****687 32 | The UID of the user who last modified the secondary cloud instance. |
|---|---|---|---|
| ---- resourceRegio nId | String | cn-hangzhou | The region ID of the secondary cloud instance. |
| ---- resourceGroup Id | String | 103 | The ID of the resource group to which the secondary cloud instance belongs. |
| ---- createdDate | Long | 1673333258000 | The time when the secondary cloud instance was created. |
| ---- lastModifiedDa te | Long | 1673333258012 | The time when the secondary cloud instance was last modified. |
| ----instanceId | String | 79e********98c7 | The ID of the secondary cloud instance. |
| ---- instanceName | String | XXX | The name of the secondary cloud instance. |
| ----pk | String | 339944229200627 712 | The primary key of the secondary cloud instance. |
| ---- cloudUniqueId | String | 0179 | The UID of the secondary cloud. |
| ---- cloudOsType | String | ENTERPRISE | The edition of the cloud instance. Only ENTERPRISE may be returned, which indicates Apsara Stack. |
| ----version | String | 1.0.0 | The version number of the secondary cloud instance. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| ---- consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. This type is generally used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. This type is generally used in cross- cloud disaster recovery scenarios. |
|---|---|---|---|
| ---- consoleApiEnd point | String | http://internal.exa mple.com-XXXXX | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |
| ---- adminCredenti alsId | String | 339944225551583 232 | The credential ID of the cloud management administrator. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of an operations administrator. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as the operations administrator, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |
| ---- accountCrede ntialsId | String | 339944229083187 200 | The credential ID of the organization account. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of a level-1 organization. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as an organization administrator. In the top navigation bar, click Enterprise. In the left-side navigation pane, choose Resources > Organizations. On the page that appears, obtain an AccessKey pair of a level-1 organization. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| ---- internetDomai n | String | inter.***.example.c om | The Internet domain name. |
|---|---|---|---|
| ---- intranetDomai n | String | intra.***.example.c om | The internal domain name. |
| ----status | String | REGULAR | The state of the cloud instance. Valid values: REGULAR: normal. NOT CONFIGURED: not configured. _ UNINITIALIZED: not initialized. The cloud instance is in this state if no administrator credentials are configured when you log on to ASR-DR for the first time. |
| --latestTask | Struct |  | The state of the task that was last run for the plan. If null is returned, no task is run for the plan. |
| --- sequenceTask s | Normal |  | The tasks that were run for steps, in the JSON format. |
| ---taskId | String | 21 | The task ID. |
| --- recoveryPlanId | String | 19 | The ID of the disaster recovery plan. |
| ---createsAt | Long | 1675393101718 | The time when the task was created. |
| ---runsAt | Long | 1675393101718 | The time when the task started. |
| ---completesAt | Long | 1675393101720 | The time when the task was complete. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| ---status | String | PENDING | The state of the task. Valid values: PENDING INITIALIZING RUNNING SWITCHING OVER _ WAITING RECOVER _ SWITCHING BACK _ ABORTING ABORTED TIMEOUT FAILED COMPLETED |
|---|---|---|---|
| ---statusMsg | String | Development test ABCD | The description of the task. |
| --- exceptionThro wn | Boolean | true | Indicates whether an exception was thrown when the task was running. Valid values: true false |
| --- exceptionMsg | String | 400 | The error message returned if an exception was thrown. |
| ---nodeId | String | Local 001 _ | The ID of the node that was processing the task. |
| -pageNum | Integer | 1 | The page number. |
| -pageSize | Integer | 10 | The number of entries per page. This parameter indicates the expected number of entries per page. The value is the same as the value of the corresponding parameter specified in the request. If the actual length of the returned rows parameter is less than the value of this parameter, the last page is returned. |
| -total | Integer | 55 | The total number of entries that meet query conditions. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Apsara Stack Resilience ASR for Geo-disaster Developer Sample requests

```
http(s)://[Endpoint]/?Action=ListRecoveryPlanByPage &PageNum=1 &PageSize=10 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "data":{
  "total":55,
  "-rows":{
   "creator":"239724*****8868732",
   "lastModifiedDate":1713514782222,
   "resourceRegionId":"cn-hangzhou",
   "lastModifier":"239724*****8868732",
   "description":"This is an example instance.",
   "--backupRegion":{
    "regionId":"cn-guznagxi",
    "regionType":"CENTRAL",
    "consoleApiEndpoint":"http://internal.example.com-XXXXX",
    "regionName":"guznagxi",
    "---cloudInstance":{
     "cloudUniqueId":"0179",
     "creator":"23972451*****68732",
     "lastModifiedDate":1673333258012,
     "instanceName":"XXX",
     "consoleApiEndpoint":"http://internal.example.com-XXXXX",
     "resourceRegionId":"cn-hangzhou",
     "lastModifier":"23972451*****68732",
     "adminCredentialsId":"339944225551583232",
     "version":"1.0.0",
     "cloudOsType":"ENTERPRISE",
     "createdDate":1673333258000,
     "instanceId":"79e********98c7",
     "aliyunAccountUid":"178511195******96",
     "internetDomain":"inter.***.example.com",
     "resourceGroupId":"103",
     "pk":"339944229200627712",
     "intranetDomain":"intra.***.example.com",
     "ownerUid":"23972451*****68732",
     "accountCredentialsId":"339944229083187200",
     "consoleType":"ASCM",
     "status":"REGULAR"
    },
    "pk":"33994422***27712",
    "consoleType":"ASCM"
   },
"type":"DRILLONLY",
```

ASR for Geo-disaster Developer Apsara Stack Resilience

```json
   type:DRILL_ONLY,
   "--latestTask":{
    "createsAt":1675393101718,
    "completesAt":1675393101720,
    "exceptionThrown":true,
    "exceptionMsg":"400",
    "statusMsg":"Development test ABCD",
    "runsAt":1675393101718,
    "sequenceTasks":"",
    "nodeId":"Local_001",
    "taskId":"21",
    "recoveryPlanId":"19",
    "status":"PENDING"
   },
   "sequence":"",
   "--relatedProtectGroups":{
    "creator":"2397******98868732",
    "createdDate":1713514782222,
    "instanceId":"e250008c-a02a-455c-b957-8*****4ef58",
    "lastModifiedDate":1713514782222,
    "aliyunAccountUid":"1785******267796",
    "resourceRegionId":"cn-hangzhou",
    "name":"name1",
    "lastModifier":"2397******98868732",
    "resourceGroupId":"103",
    "id":"e250008c-a02a-455c-b957-8*****4ef58",
    "ownerUid":"2397******98868732"
   },
   "createdDate":1713514782222,
   "instanceId":"e250008c-a02a-455c-b957-8d*****ef58",
   "aliyunAccountUid":"1785111957*****236",
   "name":"MyInstance",
   "resourceGroupId":"103",
   "id":"e250008c-a02a-455c-b957-8d*****ef58",
   "--mainRegion":{
    "regionId":"cn-guznagxi",
    "regionType":"CENTRAL",
    "consoleApiEndpoint":"http://internal.example.com-XXXXX",
    "regionName":"guznagxi",
    "---cloudInstance":{
     "cloudUniqueId":"0179",
     "creator":"23972451*****68732",
     "lastModifiedDate":1673333258012,
     "instanceName":"XXX",
     "consoleApiEndpoint":"http://internal.example.com-XXXXX",
     "resourceRegionId":"cn-hangzhou",
     "lastModifier":"23972451*****68732",
     "adminCredentialsId":"339944225551583232",
     "version":"1.0.0",
     "cloudOsType":"ENTERPRISE",
     "createdDate":1673333258000,
     "instanceId":"79e********98c7",
     "aliyunAccountUid":"178511195******96",
     "internetDomain":"inter.***.example.com",
     "resourceGroupId":"103",
```

Apsara Stack Resilience ASR for Geo-disaster Developer p ,

```json
     "pk":"339944229200627712",
     "intranetDomain":"intra.***.example.com",
     "ownerUid":"23972451*****68732",
     "accountCredentialsId":"339944229083187200",
     "consoleType":"ASCM",
     "status":"REGULAR"
    },
    "pk":"33994422***27712",
    "consoleType":"ASCM"
   },
   "ownerUid":"239724*****8868732",
   "stability":"GREEN"
  },
  "pageSize":10,
  "pageNum":1
 },
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <data>
 <total>55</total>
 <-rows>
  <creator>239724*****8868732</creator>
  <lastModifiedDate>1713514782222</lastModifiedDate>
  <resourceRegionId>cn-hangzhou</resourceRegionId>
  <lastModifier>239724*****8868732</lastModifier>
  <description>This is an example instance.</description>
  <--backupRegion>
   <regionId>cn-guznagxi</regionId>
   <regionType>CENTRAL</regionType>
   <consoleApiEndpoint>http://internal.example.com-XXXXX</consoleApiEndpoint>
   <regionName>guznagxi</regionName>
   <---cloudInstance>
    <cloudUniqueId>0179</cloudUniqueId>
    <creator>23972451*****68732</creator>
    <lastModifiedDate>1673333258012</lastModifiedDate>
    <instanceName>XXX</instanceName>
    <consoleApiEndpoint>http://internal.example.com-XXXXX</consoleApiEndpoint>
    <resourceRegionId>cn-hangzhou</resourceRegionId>
    <lastModifier>23972451*****68732</lastModifier>
    <adminCredentialsId>339944225551583232</adminCredentialsId>
    <version>1.0.0</version>
    <cloudOsType>ENTERPRISE</cloudOsType>
    <createdDate>1673333258000</createdDate>
    <instanceId>79e********98c7</instanceId>
    <aliyunAccountUid>178511195******96</aliyunAccountUid>
<internetDomain>inter***examplecom</internetDomain>
```

ASR for Geo-disaster Developer Apsara Stack Resilience

```xml
    <internetDomain>inter.***.example.com</internetDomain>
    <resourceGroupId>103</resourceGroupId>
    <pk>339944229200627712</pk>
    <intranetDomain>intra.***.example.com</intranetDomain>
    <ownerUid>23972451*****68732</ownerUid>
    <accountCredentialsId>339944229083187200</accountCredentialsId>
    <consoleType>ASCM</consoleType>
    <status>REGULAR</status>
   </---cloudInstance>
   <pk>33994422***27712</pk>
   <consoleType>ASCM</consoleType>
  </--backupRegion>
  <type>DRILL_ONLY</type>
  <--latestTask>
   <createsAt>1675393101718</createsAt>
   <completesAt>1675393101720</completesAt>
   <exceptionThrown>true</exceptionThrown>
   <exceptionMsg>400</exceptionMsg>
   <statusMsg>Development test ABCD</statusMsg>
   <runsAt>1675393101718</runsAt>
   <sequenceTasks  />
   <nodeId>Local_001</nodeId>
   <taskId>21</taskId>
   <recoveryPlanId>19</recoveryPlanId>
   <status>PENDING</status>
  </--latestTask>
  <sequence  />
  <--relatedProtectGroups>
   <creator>2397******98868732</creator>
   <createdDate>1713514782222</createdDate>
   <instanceId>e250008c-a02a-455c-b957-8*****4ef58</instanceId>
   <lastModifiedDate>1713514782222</lastModifiedDate>
   <aliyunAccountUid>1785******267796</aliyunAccountUid>
   <resourceRegionId>cn-hangzhou</resourceRegionId>
   <name>name1</name>
   <lastModifier>2397******98868732</lastModifier>
   <resourceGroupId>103</resourceGroupId>
   <id>e250008c-a02a-455c-b957-8*****4ef58</id>
   <ownerUid>2397******98868732</ownerUid>
  </--relatedProtectGroups>
  <createdDate>1713514782222</createdDate>
  <instanceId>e250008c-a02a-455c-b957-8d*****ef58</instanceId>
  <aliyunAccountUid>1785111957*****236</aliyunAccountUid>
  <name>MyInstance</name>
  <resourceGroupId>103</resourceGroupId>
  <id>e250008c-a02a-455c-b957-8d*****ef58</id>
  <--mainRegion>
   <regionId>cn-guznagxi</regionId>
   <regionType>CENTRAL</regionType>
   <consoleApiEndpoint>http://internal.example.com-XXXXX</consoleApiEndpoint>
   <regionName>guznagxi</regionName>
   <---cloudInstance>
    <cloudUniqueId>0179</cloudUniqueId>
    <creator>23972451*****68732</creator>
<lastModifiedDate>1673333258012</lastModifiedDate>
```

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

```xml
astod edate 673333580 /astod edate
    <instanceName>XXX</instanceName>
    <consoleApiEndpoint>http://internal.example.com-XXXXX</consoleApiEndpoint>
    <resourceRegionId>cn-hangzhou</resourceRegionId>
    <lastModifier>23972451*****68732</lastModifier>
    <adminCredentialsId>339944225551583232</adminCredentialsId>
    <version>1.0.0</version>
    <cloudOsType>ENTERPRISE</cloudOsType>
    <createdDate>1673333258000</createdDate>
    <instanceId>79e********98c7</instanceId>
    <aliyunAccountUid>178511195******96</aliyunAccountUid>
    <internetDomain>inter.***.example.com</internetDomain>
    <resourceGroupId>103</resourceGroupId>
    <pk>339944229200627712</pk>
    <intranetDomain>intra.***.example.com</intranetDomain>
    <ownerUid>23972451*****68732</ownerUid>
    <accountCredentialsId>339944229083187200</accountCredentialsId>
    <consoleType>ASCM</consoleType>
    <status>REGULAR</status>
   </---cloudInstance>
   <pk>33994422***27712</pk>
   <consoleType>ASCM</consoleType>
  </--mainRegion>
  <ownerUid>239724*****8868732</ownerUid>
  <stability>GREEN</stability>
 </-rows>
 <pageSize>10</pageSize>
 <pageNum>1</pageNum>
</data> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### SaveRecoveryPlan

Creates or modifies a disaster recovery plan.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |
|---|---|---|---|---|---|
| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| A | psara Stack R | esilienc | e |  | ASR | for Geo-disaster Developer Guide·API referenc | e |
|---|---|---|---|---|---|---|---|
|  | Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |  |

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
|  |  |  |  |  | The data of the disaster recovery plan, in the JSON format. { "name": "Plan name", "type": "DRILL AND DR", _ _ "mainRegion": { "regionId": "cn-hangzhou" |

Apsara Stack Resilience ASR for Geo-disaster Developer

|  |  |  |  |  |  | g }, "backupRegion": { "regionId": "cn-shanghai" }, "description": "Drill plan", "sequence": [ { "strategy": { "onSucceed": { "silenceExpression" : "1d", "action": "NEXT", "type": "action" }, "onFailed": { "silenceExpression" : "0", "action": "ABORT", "type": "action" }, "type": "pg" }, "description": "Switchover", "pg": { "id": "Protection group ID" }, "type": "switch-over" }, { "id": 27, "strategy": { "silenceExpression" : "0", "action": |  |
|---|---|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

|  |  |  |  | { "name": "Plan name", "type": "DRILL AND DR", _ _ "mainRegion": { "regionId": "cn-hangzhou" }, "backupRegion": { "regionId": "cn-shanghai" }, "description": "Drill plan", "sequence": [ { "strategy": { "onSucceed": { "silenceExpression": "1d", "action": "NEXT", "type": "action" }, "onFailed": { "silenceExpression": "0", "action": "ABORT", "type": "action" }, "type": "pg" }, "description": "Switchover", "pg": { "id": "Protection group ID" }, "type": "switch-over" }, { "id": 27, "strategy": { "silenceExpression": "0", "action": "HOLD", "type": "action" }, "description": "Manual checkpoint", "type": "checkpoint" }, { "id": 26, "strategy": { "onSucceed": { "silenceExpression": "1d", "action": "NEXT", "type": "action" }, "onPartialSucceed": { |  | "HOLD", "type": "action" }, "description": "Manual checkpoint", "type": "checkpoint" }, { "id": 26, "strategy": { "onSucceed": { "silenceExpression" : "1d", "action": "NEXT", "type": "action" }, "onPartialSucceed": { "silenceExpression" : "1d", "action": "NEXT", "type": "action" }, "onFailed": { "silenceExpression" : "0", "action": "ABORT", "type": "action" }, "type": "concurrent" }, "description": "Concurrent steps", "subSequence": [ |  |
|---|---|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| Data | Strin g | Body | Yes | "silenceExpression": "1d", "action": "NEXT", "type": "action" }, "onFailed": { "silenceExpression": "0", "action": "ABORT", "type": "action" }, "type": "concurrent" }, "description": "Concurrent steps", "subSequence": [ { "strategy": { "onSucceed": { "silenceExpression": "1d", "action": "NEXT", "type": "action" }, "onFailed": { "silenceExpression": "0", "action": "ABORT", "type": "action" }, "type": "pg" }, "description": "Switchover", "pg": { "id": "Protection group ID" }, "type": "switch-over" }, { "strategy": { "onSucceed": { "silenceExpression": "1d", "action": "NEXT", "type": "action" }, "onFailed": { "silenceExpression": "0", "action": "ABORT", "type": "action" }, "type": "pg" }, "description": "Switchover", "pg": { "id": "Protection group ID" }, "type": "switch-over" } ], "type": "concurrent" }, { "strategy": { "silenceExpression": "0", "action": "HOLD", "type": "action" }, "description": "Primary cloud status checkpoint", "type": "checkpoint-main-cloud- status" }, { "strategy": { "onSucceed": { "silenceExpression": "0", "action": "NEXT", "type": "action" }, "onFailed": { "silenceExpression": "0", "action": "ABORT", "type": "action" }, "type": "pg" }, "description": "Switchback", "pg": { "id": "Protection group ID" }, "type": "switch-back" } ] } |  | { "strategy": { "onSucceed": { "silenceExpression" : "1d", "action": "NEXT", "type": "action" }, "onFailed": { "silenceExpression" : "0", "action": "ABORT", "type": "action" }, "type": "pg" }, "description": "Switchover", "pg": { "id": "Protection group ID" }, "type": "switch-over" }, { "strategy": { "onSucceed": { "silenceExpression" : "1d", "action": "NEXT", "type": "action" }, "onFailed": { "silenceExpression" "0" |  |
|---|---|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

|  |  |  |  |  |  | : "0", "action": "ABORT", "type": "action" }, "type": "pg" }, "description": "Switchover", "pg": { "id": "Protection group ID" }, "type": "switch-over" } ], "type": "concurrent" }, { "strategy": { "silenceExpression" : "0", "action": "HOLD", "type": "action" }, "description": "Primary cloud status checkpoint", "type": "checkpoint-main- cloud-status" }, { "strategy": { "onSucceed": { "silenceExpression" : "0", "action": "NEXT", "type": "action" |  |
|---|---|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

|  |  |  |  |  | action }, "onFailed": { "silenceExpression" : "0", "action": "ABORT", "type": "action" }, "type": "pg" }, "description": "Switchback", "pg": { "id": "Protection group ID" }, "type": "switch-back" } ] } |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
| success | Boolean | true | Indicates whether the request was successful. true false |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Response parameters**

| code | String | 200 | The response code. |
|---|---|---|---|
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The data of the saved disaster recovery plan. |
| -sequence | Normal |  | The steps of the disaster recovery plan, in the JSON format. |
| - relatedProtect Groups | Array |  | The protection groups that are associated with the disaster recovery plan. |
| -- aliyunAccount Uid | String | 1785******267796 | The unique ID (UID) of the Apsara Stack tenant account to which the protection group belongs. |
| --ownerUid | String | 2397******988687 32 | The UID of the protection group owner. |
| --creator | String | 2397******988687 32 | The UID of the user who created the protection group. |
| --lastModifier | String | 2397******988687 32 | The UID of the user who last modified the protection group. |
| -- resourceRegio nId | String | cn-hangzhou | The region ID of the protection group. |
| -- resourceGroup Id | String | 103 | The ID of the resource group to which the protection group belongs. |
| --createdDate | Long | 1713514782222 | The time when the protection group was created. |
| -- lastModifiedDa te | Long | 1713514782222 | The time when the protection group was last modified. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| --instanceId | String | e250008c-a02a- 455c-b957- 8*****4ef58 | The ID of the protection group. |
|---|---|---|---|
| --id | String | e250008c-a02a- 455c-b957- 8*****4ef58 | The ID of the protection group. |
| --name | String | name1 | The name of the protection group. |
| - aliyunAccount Uid | String | 1785111957*****2 36 | The UID of the Apsara Stack tenant account to which the resource belongs. |
| -ownerUid | String | 239724*****88687 32 | The UID of the resource owner. |
| -creator | String | 239724*****88687 32 | The UID of the user who created the resource. |
| -lastModifier | String | 239724*****88687 32 | The UID of the user who last modified the resource. |
| - resourceRegio nId | String | cn-hangzhou | The region ID of the resource. |
| - resourceGroup Id | String | 103 | The ID of the resource group to which the resource belongs. |
| -createdDate | Long | 1713514782222 | The time when the resource was created. |
| - lastModifiedDa te | Long | 1713514782222 | The time when the resource was last modified. |
| -instanceId | String | e250008c-a02a- 455c-b957- 8d*****ef58 | The instance ID of the resource. |
| -id | String | e250008c-a02a- 455c-b957- 8d*****ef58 | The ID of the disaster recovery plan. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| -name | String | name2 | The name of the disaster recovery plan. |
|---|---|---|---|
| -type | String | security-token | The type of the disaster recovery plan. Valid values: DRILL ONLY _ DRILL AND DR _ _ |
| -stability | String | GREEN | The stability of the disaster recovery plan. Valid values: GREEN: stable. GRAY: unknown. RED: unstable. |
| -description | String | Test the switchback step performed by calling an API operation | The description of the disaster recovery plan. |
| -mainRegion | Struct |  | The information about the primary region. |
| --pk | String | 33994422***27712 | The primary key of the primary cloud instance. |
| --regionId | String | cn-guznagxi | The region ID of the primary cloud. |
| --regionName | String | guznagxi | The region name of the primary cloud. |
| --regionType | String | CENTRAL | The type of the region. Valid values: CENTRAL UNIT |
| --consoleType | String | ASRDR | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| -- consoleApiEnd point | String | http://internal.exa mple.com-xxxxxx | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |
|---|---|---|---|
| -- cloudInstance | Struct |  | The information about the primary cloud instance. |
| --- aliyunAccount Uid | String | 178511195******9 6 | The UID of the Apsara Stack tenant account to which the primary cloud instance belongs. |
| ---ownerUid | String | 23972451*****687 32 | The UID of the owner of the primary cloud instance. |
| ---creator | String | 23972451*****687 32 | The UID of the user who created the primary cloud instance. |
| ---lastModifier | String | 23972451*****687 32 | The UID of the user who last modified the primary cloud instance. |
| --- resourceRegio nId | String | cn-hangzhou | The region ID of the primary cloud instance. |
| --- resourceGroup Id | String | 103 | The ID of the resource group to which the primary cloud instance belongs. |
| ---createdDate | Long | 1704366334000 | The time when the primary cloud instance was created. |
| --- lastModifiedDa te | Long | 1704366334000 | The time when the primary cloud instance was last modified. |
| ---instanceId | String | e250008c-a02a- 455c-b957- 8d*****4ef58 | The ID of the primary cloud instance. |
| --- instanceName | String | XXX | The name of the primary cloud instance. |
| ---pk | String | 339944229200627 712 | The primary key of the primary cloud instance. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| --- cloudUniqueId | String | 0179 | The UID of the primary cloud. |
|---|---|---|---|
| ---cloudOsType | String | ENTERPRISE | The edition of the primary cloud instance. Only ENTERPRISE may be returned, which indicates Apsara Stack. |
| ---version | String | 1.0.0 | The version number of the primary cloud instance. |
| ---consoleType | String | ASRDR | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |
| --- consoleApiEnd point | String | http://internal.exa mple.com-xxxxxx | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |
| --- adminCredenti alsId | String | 339944225551583 232 | The credential ID of the cloud management administrator. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of an operations administrator. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as the operations administrator, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| --- accountCrede ntialsId | String | 339944229083187 200 | The credential ID of the organization account. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of a level-1 organization. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as an organization administrator. In the top navigation bar, click Enterprise. In the left-side navigation pane, choose Resources > Organizations. On the page that appears, obtain an AccessKey pair of a level-1 organization. |
|---|---|---|---|
| --- internetDomai n | String | inter.***.shuguang. com | The Internet domain name. |
| --- intranetDomai n | String | intra.***.shuguang. com | The internal domain name. |
| ---status | String | REGULAR | The status of the cloud instance. Valid values: REGULAR: normal. NOT CONFIGURED: not configured. _ UNINITIALIZED: not initialized. The cloud instance is in this state if no administrator credentials are configured when you log on to ASR-DR for the first time. |
| -backupRegion | Struct |  | The information about the secondary region. |
| --pk | String | 33994422***27712 | The primary key of the secondary cloud instance. |
| --regionId | String | cn-guznagxi | The region ID of the secondary cloud. |
| --regionName | String | guznagxi | The region name of the secondary cloud. |
| --regionType | String | CENTRAL | The type of the region. Valid values: CENTRAL UNIT |

ASR for Geo-disaster Developer Apsara Stack Resilience

| --consoleType | String | ASRDR | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |
|---|---|---|---|
| -- consoleApiEnd point | String | http://internal.exa mple.com-xxxxxx | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |
| -- cloudInstance | Struct |  | The information about the secondary cloud instance. |
| --- aliyunAccount Uid | String | 178511195******9 6 | The UID of the Apsara Stack tenant account to which the secondary cloud instance belongs. |
| ---ownerUid | String | 23972451*****687 32 | The UID of the owner of the secondary cloud instance. |
| ---creator | String | 23972451*****687 32 | The UID of the user who created the secondary cloud instance. |
| ---lastModifier | String | 23972451*****687 32 | The UID of the user who last modified the secondary cloud instance. |
| --- resourceRegio nId | String | cn-hangzhou | The region ID of the secondary cloud instance. |
| --- resourceGroup Id | String | 103 | The ID of the resource group to which the secondary cloud instance belongs. |
| ---createdDate | Long | 1704366334000 | The time when the secondary cloud instance was created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| --- lastModifiedDa te | Long | 1704366334000 | The time when the secondary cloud instance was last modified. |
|---|---|---|---|
| ---instanceId | String | e250008c-a02a- 455c-b957- 8d*****4ef58 | The ID of the secondary cloud instance. |
| --- instanceName | String | XXX | The name of the secondary cloud instance. |
| ---pk | String | 339944229200627 712 | The primary key of the secondary cloud instance. |
| --- cloudUniqueId | String | 0179 | The UID of the secondary cloud. |
| ---cloudOsType | String | ENTERPRISE | The edition of the secondary cloud instance. Only ENTERPRISE may be returned, which indicates Apsara Stack. |
| ---version | String | 1.0.0 | The version number of the secondary cloud instance. |
| ---consoleType | String | ASRDR | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |
| --- consoleApiEnd point | String | http://internal.exa mple.com-xxxxxx | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| --- adminCredenti alsId | String | 339944225551583 232 | The credential ID of the cloud management administrator. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of an operations administrator. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as the operations administrator, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |
|---|---|---|---|
| --- accountCrede ntialsId | String | 339944229083187 200 | The credential ID of the organization account. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of a level-1 organization. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as an organization administrator. In the top navigation bar, click Enterprise. In the left-side navigation pane, choose Resources > Organizations. On the page that appears, obtain an AccessKey pair of a level-1 organization. |
| --- internetDomai n | String | inter.***.shuguang. com | The Internet domain name. |
| --- intranetDomai n | String | intra.***.shuguang. com | The internal domain name. |
| ---status | String | REGULAR | The status of the cloud instance. Valid values: REGULAR: normal. NOT CONFIGURED: not configured. _ UNINITIALIZED: not initialized. The cloud instance is in this state if no administrator credentials are configured when you log on to ASR-DR for the first time. |
| -latestTask | Struct |  | The status of the task that was last run for the plan. If null is returned, no task is run for the plan. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| -- sequenceTask s | Normal |  | The tasks that were run for steps, in the JSON format. |
|---|---|---|---|
| --taskId | String | 21 | The task ID. |
| -- recoveryPlanId | String | 19 | The ID of the disaster recovery plan. |
| --createsAt | Long | 1675393101718 | The time when the task was created. |
| --runsAt | Long | 1675393101718 | The time when the task started. |
| --completesAt | Long | 1675393101720 | The time when the task was complete. |
| --status | String | COMPLETED | The status of the task. Valid values: PENDING INITIALIZING RUNNING SWITCHING OVER _ WAITING RECOVER _ SWITCHING BACK _ ABORTING ABORTED TIMEOUT FAILED COMPLETED |
| --statusMsg | String | Development test ABCD | The description of the task. |
| -- exceptionThro wn | Boolean | true | Indicates whether an exception was thrown when the task was running. Valid values: true false |
| -- exceptionMsg | String | 400 | The error message returned if an exception was thrown. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| --nodeId | String | Local 001 _ | The ID of the node that was processing the task. |
|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

**Examples**

Sample requests

```json
```json
&Data={
  "taskId": 21,
  "recoveryPlanId": 19,
  "runMode": "DR",
  "creatorAliyunAccountUid": "12312340234",
  "creatorUid": "12312340234",
  "createsAt": 1675344396594,
  "runsAt": 1675344403422,
  "completesAt": 1675393201720,
  "status": "COMPLETED",
  "statusMsg": "The task is complete",
  "exceptionThrown": false,
  "exceptionMsg": "",
  "nodeId": "aaa-bbb-ccc",
  "loggerId": 123,
  "loggerToken": "xxx-xxx-xxx",
  "sequenceTasks": [
    {
      "sequenceTaskId": 35,
      "sequenceId": 55,
      "recoveryTaskId": 21,
      "runsAt": 1675344413421,
      "silencingAt": 1675344418423,
      "status": "COMPLETED",
      "statusMsg": "Development test ABCD",
      "protectGroupId": "Protection group ID",
      "switchSucceed": false,
      "switchId": "b9b***96-8a5b-4fc2-b292-af9c*****0ee",
      "switchTaskId": "97***d37-2361-47e8-8a63-c3c*****b501",
      "sequenceType": "switch-over"
    }
```

]

```
} &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "data":{
"-backupRegion":{
```

ASR for Geo-disaster Developer Apsara Stack Resilience

```json
backupRegion:{
   "regionId":"cn-guznagxi",
   "regionType":"CENTRAL",
   "consoleApiEndpoint":"http://internal.example.com-xxxxxx",
   "regionName":"guznagxi",
   "pk":"33994422***27712",
   "--cloudInstance":{
    "cloudUniqueId":"0179",
    "creator":"23972451*****68732",
    "lastModifiedDate":1704366334000,
    "instanceName":"XXX",
    "consoleApiEndpoint":"http://internal.example.com-xxxxxx",
    "resourceRegionId":"cn-hangzhou",
    "lastModifier":"23972451*****68732",
    "adminCredentialsId":"339944225551583232",
    "version":"1.0.0",
    "cloudOsType":"ENTERPRISE",
    "createdDate":1704366334000,
    "instanceId":"e250008c-a02a-455c-b957-8d*****4ef58",
    "aliyunAccountUid":"178511195******96",
    "internetDomain":"inter.***.shuguang.com",
    "resourceGroupId":"103",
    "pk":"339944229200627712",
    "intranetDomain":"intra.***.shuguang.com",
    "ownerUid":"23972451*****68732",
    "accountCredentialsId":"339944229083187200",
    "consoleType":"ASRDR",
    "status":"REGULAR"
   },
   "consoleType":"ASRDR"
  },
  "creator":"239724*****8868732",
  "lastModifiedDate":1713514782222,
  "-mainRegion":{
   "regionId":"cn-guznagxi",
   "regionType":"CENTRAL",
   "consoleApiEndpoint":"http://internal.example.com-xxxxxx",
   "regionName":"guznagxi",
   "pk":"33994422***27712",
   "--cloudInstance":{
    "cloudUniqueId":"0179",
    "creator":"23972451*****68732",
    "lastModifiedDate":1704366334000,
    "instanceName":"XXX",
    "consoleApiEndpoint":"http://internal.example.com-xxxxxx",
    "resourceRegionId":"cn-hangzhou",
    "lastModifier":"23972451*****68732",
    "adminCredentialsId":"339944225551583232",
    "version":"1.0.0",
    "cloudOsType":"ENTERPRISE",
    "createdDate":1704366334000,
    "instanceId":"e250008c-a02a-455c-b957-8d*****4ef58",
    "aliyunAccountUid":"178511195******96",
    "internetDomain":"inter.***.shuguang.com",
    "resourceGroupId":"103",
```

Apsara Stack Resilience ASR for Geo-disaster Developer p ,

```json
    "pk":"339944229200627712",
    "intranetDomain":"intra.***.shuguang.com",
    "ownerUid":"23972451*****68732",
    "accountCredentialsId":"339944229083187200",
    "consoleType":"ASRDR",
    "status":"REGULAR"
   },
   "consoleType":"ASRDR"
  },
  "resourceRegionId":"cn-hangzhou",
  "lastModifier":"239724*****8868732",
  "description":"Test the switchback step performed by calling an API operation",
  "type":"security-token",
  "-relatedProtectGroups":{
   "creator":"2397******98868732",
   "createdDate":1713514782222,
   "instanceId":"e250008c-a02a-455c-b957-8*****4ef58",
   "lastModifiedDate":1713514782222,
   "aliyunAccountUid":"1785******267796",
   "resourceRegionId":"cn-hangzhou",
   "name":"name1",
   "lastModifier":"2397******98868732",
   "resourceGroupId":"103",
   "id":"e250008c-a02a-455c-b957-8*****4ef58",
   "ownerUid":"2397******98868732"
  },
  "sequence":"",
  "createdDate":1713514782222,
  "instanceId":"e250008c-a02a-455c-b957-8d*****ef58",
  "aliyunAccountUid":"1785111957*****236",
  "name":"name2",
  "resourceGroupId":"103",
  "id":"e250008c-a02a-455c-b957-8d*****ef58",
  "-latestTask":{
   "createsAt":1675393101718,
   "completesAt":1675393101720,
   "exceptionThrown":true,
   "exceptionMsg":"400",
   "statusMsg":"Development test ABCD",
   "runsAt":1675393101718,
   "sequenceTasks":"",
   "nodeId":"Local_001",
   "taskId":"21",
   "recoveryPlanId":"19",
   "status":"COMPLETED"
  },
  "ownerUid":"239724*****8868732",
  "stability":"GREEN"
 },
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

ASR for Geo-disaster Developer Apsara Stack Resilience `XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <data>
 <-backupRegion>
  <regionId>cn-guznagxi</regionId>
  <regionType>CENTRAL</regionType>
  <consoleApiEndpoint>http://internal.example.com-xxxxxx</consoleApiEndpoint>
  <regionName>guznagxi</regionName>
  <pk>33994422***27712</pk>
  <--cloudInstance>
   <cloudUniqueId>0179</cloudUniqueId>
   <creator>23972451*****68732</creator>
   <lastModifiedDate>1704366334000</lastModifiedDate>
   <instanceName>XXX</instanceName>
   <consoleApiEndpoint>http://internal.example.com-xxxxxx</consoleApiEndpoint>
   <resourceRegionId>cn-hangzhou</resourceRegionId>
   <lastModifier>23972451*****68732</lastModifier>
   <adminCredentialsId>339944225551583232</adminCredentialsId>
   <version>1.0.0</version>
   <cloudOsType>ENTERPRISE</cloudOsType>
   <createdDate>1704366334000</createdDate>
   <instanceId>e250008c-a02a-455c-b957-8d*****4ef58</instanceId>
   <aliyunAccountUid>178511195******96</aliyunAccountUid>
   <internetDomain>inter.***.shuguang.com</internetDomain>
   <resourceGroupId>103</resourceGroupId>
   <pk>339944229200627712</pk>
   <intranetDomain>intra.***.shuguang.com</intranetDomain>
   <ownerUid>23972451*****68732</ownerUid>
   <accountCredentialsId>339944229083187200</accountCredentialsId>
   <consoleType>ASRDR</consoleType>
   <status>REGULAR</status>
  </--cloudInstance>
  <consoleType>ASRDR</consoleType>
 </-backupRegion>
 <creator>239724*****8868732</creator>
 <lastModifiedDate>1713514782222</lastModifiedDate>
 <-mainRegion>
  <regionId>cn-guznagxi</regionId>
  <regionType>CENTRAL</regionType>
  <consoleApiEndpoint>http://internal.example.com-xxxxxx</consoleApiEndpoint>
  <regionName>guznagxi</regionName>
  <pk>33994422***27712</pk>
  <--cloudInstance>
   <cloudUniqueId>0179</cloudUniqueId>
   <creator>23972451*****68732</creator>
   <lastModifiedDate>1704366334000</lastModifiedDate>
   <instanceName>XXX</instanceName>
   <consoleApiEndpoint>http://internal.example.com-xxxxxx</consoleApiEndpoint>
   <resourceRegionId>cn-hangzhou</resourceRegionId>
   <lastModifier>23972451*****68732</lastModifier>
   <adminCredentialsId>339944225551583232</adminCredentialsId>
```

Apsara Stack Resilience ASR for Geo-disaster Developer

```xml
   <version>1.0.0</version>
   <cloudOsType>ENTERPRISE</cloudOsType>
   <createdDate>1704366334000</createdDate>
   <instanceId>e250008c-a02a-455c-b957-8d*****4ef58</instanceId>
   <aliyunAccountUid>178511195******96</aliyunAccountUid>
   <internetDomain>inter.***.shuguang.com</internetDomain>
   <resourceGroupId>103</resourceGroupId>
   <pk>339944229200627712</pk>
   <intranetDomain>intra.***.shuguang.com</intranetDomain>
   <ownerUid>23972451*****68732</ownerUid>
   <accountCredentialsId>339944229083187200</accountCredentialsId>
   <consoleType>ASRDR</consoleType>
   <status>REGULAR</status>
  </--cloudInstance>
  <consoleType>ASRDR</consoleType>
 </-mainRegion>
 <resourceRegionId>cn-hangzhou</resourceRegionId>
 <lastModifier>239724*****8868732</lastModifier>
 <description>Test the switchback step performed by calling an API
operation</description>
 <type>security-token</type>
 <-relatedProtectGroups>
  <creator>2397******98868732</creator>
  <createdDate>1713514782222</createdDate>
  <instanceId>e250008c-a02a-455c-b957-8*****4ef58</instanceId>
  <lastModifiedDate>1713514782222</lastModifiedDate>
  <aliyunAccountUid>1785******267796</aliyunAccountUid>
  <resourceRegionId>cn-hangzhou</resourceRegionId>
  <name>name1</name>
  <lastModifier>2397******98868732</lastModifier>
  <resourceGroupId>103</resourceGroupId>
  <id>e250008c-a02a-455c-b957-8*****4ef58</id>
  <ownerUid>2397******98868732</ownerUid>
 </-relatedProtectGroups>
 <sequence  />
 <createdDate>1713514782222</createdDate>
 <instanceId>e250008c-a02a-455c-b957-8d*****ef58</instanceId>
 <aliyunAccountUid>1785111957*****236</aliyunAccountUid>
 <name>name2</name>
 <resourceGroupId>103</resourceGroupId>
 <id>e250008c-a02a-455c-b957-8d*****ef58</id>
 <-latestTask>
  <createsAt>1675393101718</createsAt>
  <completesAt>1675393101720</completesAt>
  <exceptionThrown>true</exceptionThrown>
  <exceptionMsg>400</exceptionMsg>
  <statusMsg>Development test ABCD</statusMsg>
  <runsAt>1675393101718</runsAt>
  <sequenceTasks  />
  <nodeId>Local_001</nodeId>
  <taskId>21</taskId>
  <recoveryPlanId>19</recoveryPlanId>
  <status>COMPLETED</status>
 </-latestTask>
<onerUid>239724*****8868732</onerUid>
```

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

ASR for Geo-disaster Developer Apsara Stack Resilience

```xml
 <ownerUid>239724*****8868732</ownerUid>
 <stability>GREEN</stability>
</data> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

#### Plan execution

##### ExecRecoveryTask

Runs a disaster recovery plan.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| RecoveryPl anId | Long | Body | Yes | 379e********98c7 | The ID of the disaster recovery plan. |
| RunMode | Strin g | Body | No | DRILL | The mode in which the disaster recovery plan is run. Valid values: DRILL DR |

| 90 |  |  | > Document Version: 2026070 |
|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | a62a********bcd1 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Long | 1245789352 | The task ID. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Examples**

Sample requests

```
&RecoveryPlanId=379e********98c7 &<Common request parameters>
```

Sample success responses `JSON` format

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "data":1245789352,
 "requestId":"a62a********bcd1",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <data>1245789352</data> <requestId>a62a********bcd1</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### AbortRecoveryTask

Aborts a task that is run for a disaster recovery plan.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |
|---|---|---|---|---|---|
| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| TaskId | Long | Body | Yes | 12345 | The task ID. |
| Message | Strin g | Body | No | The plan is canceled. | The reason for aborting the disaster recovery plan or other necessary information. |
| Force | Bool ean | Body | No | true | Specifies whether to forcibly abort the task. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

**Examples**

Sample requests

```
&TaskId=12345 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

ASR for Geo-disaster Developer Apsara Stack Resilience `XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### GetRecoveryTask

Queries the information about a task that is run for a disaster recovery plan.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| TaskId | Long | Quer y | Yes | 379e********98c7 | The task ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | a62a********bcd1 | The request ID. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Response parameters**

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The returned data. |
| - sequenceTask s | Normal |  | The tasks that were run for steps, in the JSON format. |
| -taskId | String | 14 | The task ID. |
| - recoveryPlanId | String | 21 | The ID of the disaster recovery plan. |
| - recoveryPlanN ame | String | recoveryPlan1 | The name of the disaster recovery plan. |
| -runMode | String | DRILL | The mode in which the disaster recovery plan is run. Valid values: DRILL DR |
| - creatorAliyunA ccountUid | String | 2397******988687 32 | The unique ID (UID) of the Apsara Stack tenant account that is used to create the task. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| -createsAt | Long | 1713514782222 | The time when the task was created. |
|---|---|---|---|
| -runsAt | Long | 1713514782222 | The time when the task started. |
| -completesAt | Long | 1713514782225 | The time when the task was complete. |
| -status | String | PENDING | The status of the task. Valid values: PENDING INITIALIZING RUNNING SWITCHING OVER _ WAITING RECOVER _ SWITCHING BACK _ ABORTING ABORTED TIMEOUT FAILED COMPLETED |
| -statusMsg | String | Development test ABCD | The description of the task. |
| - exceptionThro wn | Boolean | true | Indicates whether an exception was thrown when the task was running. Valid values: true false |
| -exceptionMsg | String | 400 | The error message returned if an exception was thrown. |
| -nodeId | String | Local 001 _ | The ID of the node that was processing the task. |
| - sequenceCoun t | Integer | 2 | The number of steps included in the task. Only root steps are counted. |
| -loggerId | Long | 1232342443 | The ID of the task logger. |
| -loggerToken | String | XXX-XXX-XXX | The credentials for querying task logs. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| -statistic | Struct |  | The statistics about tasks. |
|---|---|---|---|
| --taskId | String | 14 | The task ID. |
| --durationMillis | Long | 0 | The duration of the task. Unit: milliseconds. |
| --succeed | Boolean | true | Indicates whether the task was successful. |
| --accordExpect | Boolean | true | Indicates whether the results meet expectations. |
| --evaluation | String | The drill is successful. | The conclusion of the drill. |
| --reportFileId | String | 1 | The report file ID of the drill. |
| --execCount | Integer | 21 | The total number of tasks that were run for the plan as of the current task. |
| -- execSucceedC ount | Integer | 5 | The total number of tasks that were successfully run for the plan as of the current task. |
| -- protectGroupT otalCount | Integer | 1 | The total number of protection groups included in the task. |
| -- protectGroupS witchOverTota lCount | Integer | 1 | The total number of protection groups that involve switchover or failover in the task. |
| -- protectGroupS witchBackTota lCount | Integer | 1 | The total number of protection groups that involve switchback or failback in the task. |
| -- protectGroupS witchOverSucc eedCount | Integer | 1 | The total number of protection groups whose switchover or failover was successful in the task. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| -- protectGroupS witchBackSucc eedCount | Integer | 1 | The total number of protection groups whose switchback or failback was successful in the task. |
|---|---|---|---|
| -- instanceTotalC ount | Integer | 1 | The total number of synchronization entities included in the task. |
| -- instanceSwitch OverTotalCoun t | Integer | 1 | The total number of synchronization entities that involve switchover or failover in the task. |
| -- instanceSwitch BackTotalCoun t | Integer | 1 | The total number of synchronization entities that involve switchback or failback in the task. |
| -- instanceRpoQ ualifiedCount | Integer | 1 | The number of synchronization entities whose synchronization latency meets expectations. |
| -- instanceSwitch OverDurationQ ualifiedCount | Integer | 1 | The number of synchronization entities whose switchover or failover duration meets expectations. |
| -- instanceSwitch BackDuration QualifiedCount | Integer | 1 | The number of synchronization entities whose switchback or failback duration meets expectations. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
&TaskId=379e********98c7 &<Common request parameters>
```

Sample success responses `JSON` format Apsara Stack Resilience ASR for Geo-disaster Developer

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "data":{
  "createsAt":1713514782222,
  "creatorAliyunAccountUid":"2397******98868732",
  "sequenceTasks":"",
  "runMode":"DRILL",
  "loggerToken":"XXX-XXX-XXX",
  "completesAt":1713514782225,
  "exceptionThrown":true,
  "exceptionMsg":"400",
  "sequenceCount":2,
  "statusMsg":"Development test ABCD",
  "recoveryPlanName":"recoveryPlan1",
  "runsAt":1713514782222,
  "-statistic":{
   "reportFileId":"1",
   "instanceTotalCount":1,
   "protectGroupSwitchOverSucceedCount":1,
   "protectGroupTotalCount":1,
   "instanceSwitchOverTotalCount":1,
   "execCount":21,
   "durationMillis":0,
   "protectGroupSwitchOverTotalCount":1,
   "instanceRpoQualifiedCount":1,
   "accordExpect":true,
   "instanceSwitchBackDurationQualifiedCount":1,
   "evaluation":"The drill is successful.",
   "instanceSwitchOverDurationQualifiedCount":1,
   "instanceSwitchBackTotalCount":1,
   "succeed":true,
   "protectGroupSwitchBackTotalCount":1,
   "execSucceedCount":5,
   "taskId":"14",
   "protectGroupSwitchBackSucceedCount":1
  },
  "loggerId":1232342443,
  "nodeId":"Local_001",
  "taskId":"14",
  "recoveryPlanId":"21",
  "status":"PENDING"
 },
 "requestId":"a62a********bcd1",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format ASR for Geo-disaster Developer Apsara Stack Resilience

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <data>
 <createsAt>1713514782222</createsAt>
 <creatorAliyunAccountUid>2397******98868732</creatorAliyunAccountUid>
 <sequenceTasks  />
 <runMode>DRILL</runMode>
 <loggerToken>XXX-XXX-XXX</loggerToken>
 <completesAt>1713514782225</completesAt>
 <exceptionThrown>true</exceptionThrown>
 <exceptionMsg>400</exceptionMsg>
 <sequenceCount>2</sequenceCount>
 <statusMsg>Development test ABCD</statusMsg>
 <recoveryPlanName>recoveryPlan1</recoveryPlanName>
 <runsAt>1713514782222</runsAt>
 <-statistic>
  <reportFileId>1</reportFileId>
  <instanceTotalCount>1</instanceTotalCount>
  <protectGroupSwitchOverSucceedCount>1</protectGroupSwitchOverSucceedCount>
  <protectGroupTotalCount>1</protectGroupTotalCount>
  <instanceSwitchOverTotalCount>1</instanceSwitchOverTotalCount>
  <execCount>21</execCount>
  <durationMillis>0</durationMillis>
  <protectGroupSwitchOverTotalCount>1</protectGroupSwitchOverTotalCount>
  <instanceRpoQualifiedCount>1</instanceRpoQualifiedCount>
  <accordExpect>true</accordExpect>
<instanceSwitchBackDurationQualifiedCount>1</instanceSwitchBackDurationQualifiedCount>
  <evaluation>The drill is successful.</evaluation>
<instanceSwitchOverDurationQualifiedCount>1</instanceSwitchOverDurationQualifiedCount>
  <instanceSwitchBackTotalCount>1</instanceSwitchBackTotalCount>
  <succeed>true</succeed>
  <protectGroupSwitchBackTotalCount>1</protectGroupSwitchBackTotalCount>
  <execSucceedCount>5</execSucceedCount>
  <taskId>14</taskId>
  <protectGroupSwitchBackSucceedCount>1</protectGroupSwitchBackSucceedCount>
 </-statistic>
 <loggerId>1232342443</loggerId>
 <nodeId>Local_001</nodeId>
 <taskId>14</taskId>
 <recoveryPlanId>21</recoveryPlanId>
 <status>PENDING</status>
</data> <requestId>a62a********bcd1</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### GetRecoveryPlanSnapshot

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer Queries the snapshot data of a disaster recovery plan. Snapshot data refers to the status of the disaster recovery plan data at the moment when a task begins execution for a disaster recovery plan.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| TaskId | Long | Quer y | Yes | 379e********98c7 | The task ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | a62a********bcd1 | The request ID. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The snapshot data of the disaster recovery plan. |
| -sequence | Normal |  | The steps of the disaster recovery plan, in the JSON format. |
| - relatedProtect Groups | Array |  | The protection groups that are associated with the disaster recovery plan. |
| -- aliyunAccount Uid | String | 1785******267796 | The unique ID (UID) of the Apsara Stack tenant account to which the protection group belongs. |
| --ownerUid | String | 2397******988687 32 | The UID of the protection group owner. |
| --creator | String | 2397******988687 32 | The UID of the user who created the protection group. |
| --lastModifier | String | 2397******988687 32 | The UID of the user who last modified the protection group. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| -- resourceRegio nId | String | cn-hangzhou | The region ID of the protection group. |
|---|---|---|---|
| -- resourceGroup Id | String | fe1********6d6d | The ID of the resource group to which the protection group belongs. |
| --createdDate | Long | 1673333258000 | The time when the resource was created. |
| -- lastModifiedDa te | Long | 1673333258012 | The time when the resource was last modified. |
| --instanceId | String | 79e********98c7 | The ID of the protection group. |
| --id | String | 79e********98c7 | The ID of the protection group. |
| --name | String | name1 | The name of the protection group. |
| - aliyunAccount Uid | String | 1785111957*****2 36 | The UID of the Apsara Stack tenant account to which the resource belongs. |
| -ownerUid | String | 239724*****88687 32 | The UID of the resource owner. |
| -creator | String | 239724*****88687 32 | The UID of the user who created the resource. |
| -lastModifier | String | 239724*****88687 32 | The UID of the user who last modified the resource. |
| - resourceRegio nId | String | cn-hangzhou | The region ID of the resource. |
| - resourceGroup Id | String | 103 | The ID of the resource group to which the resource belongs. |
| -createdDate | Long | 1713514782222 | The time when the resource was created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| - lastModifiedDa te | Long | 1713514782222 | The time when the resource was last modified. |
|---|---|---|---|
| -instanceId | String | e250008c-a02a- 455c-b957- 8d*****ef58 | The instance ID of the resource. |
| -id | String | e250008c-a02a- 455c-b957- 8d*****ef58 | The ID of the disaster recovery plan. |
| -name | String | MyInstance | The name of the disaster recovery plan. |
| -type | String | DRILL ONLY _ | The type of the disaster recovery plan. Valid values: DRILL ONLY _ DRILL AND DR _ _ |
| -stability | String | GREEN | The stability of the disaster recovery plan. Valid values: GREEN: stable. GRAY: unknown. RED: unstable. |
| -description | String | This is an example instance. | The description of the disaster recovery plan. |
| -mainRegion | Struct |  | The information about the primary region. |
| --pk | String | 33994422***27712 | The primary key of the primary cloud instance. |
| --regionId | String | cn-guznagxi | The region ID of the primary cloud. |
| --regionName | String | guznagxi | The region name of the primary cloud. |
| --regionType | String | CENTRAL | The type of the region. Valid values: CENTRAL UNIT |

ASR for Geo-disaster Developer Apsara Stack Resilience

| --consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |
|---|---|---|---|
| -- consoleApiEnd point | String | http://internal.exa mple.com.xxxxx | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |
| -- cloudInstance | Struct |  | The information about the primary cloud instance. |
| --- aliyunAccount Uid | String | 178511195******9 6 | The UID of the Apsara Stack tenant account to which the primary cloud instance belongs. |
| ---ownerUid | String | 23972451*****687 32 | The UID of the owner of the primary cloud instance. |
| ---creator | String | 23972451*****687 32 | The UID of the user who created the primary cloud instance. |
| ---lastModifier | String | 23972451*****687 32 | The UID of the user who last modified the primary cloud instance. |
| --- resourceRegio nId | String | cn-hangzhou | The region ID of the primary cloud instance. |
| --- resourceGroup Id | String | 103 | The ID of the resource group to which the primary cloud instance belongs. |
| ---createdDate | Long | 1704366334000 | The time when the primary cloud instance was created. |
| --- lastModifiedDa te | Long | 1704366334000 | The time when the primary cloud instance was last modified. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| ---instanceId | String | e250008c-a02a- 455c-b957- 8d*****4ef58 | The ID of the primary cloud instance. |
|---|---|---|---|
| --- instanceName | String | XXX | The name of the primary cloud instance. |
| ---pk | String | 339944229200627 712 | The primary key of the primary cloud instance. |
| --- cloudUniqueId | String | 0179 | The UID of the primary cloud. |
| ---cloudOsType | String | ENTERPRISE | The edition of the primary cloud instance. Only ENTERPRISE may be returned, which indicates Apsara Stack. |
| ---version | String | 1.0.0 | The version number of the primary cloud instance. |
| ---consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |
| --- consoleApiEnd point | String | http://internal.exa mple.com.xxxxx | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| --- adminCredenti alsId | String | 339944225551583 232 | The credential ID of the cloud management administrator. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of an operations administrator. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as the operations administrator, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |
|---|---|---|---|
| --- accountCrede ntialsId | String | 339944225551583 232 | The credential ID of the organization account. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of a level-1 organization. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as an organization administrator. In the top navigation bar, click Enterprise. In the left-side navigation pane, choose Resources > Organizations. On the page that appears, obtain an AccessKey pair of a level-1 organization. |
| --- internetDomai n | String | inter.***.shuguang. com | The Internet domain name. |
| --- intranetDomai n | String | intra.***.shuguang. com | The internal domain name. |
| ---status | String | REGULAR | The status of the primary cloud instance. Valid values: REGULAR: normal. NOT CONFIGURED: not configured. _ UNINITIALIZED: not initialized. The cloud instance is in this state if no administrator credentials are configured when you log on to ASR-DR for the first time. |
| -backupRegion | Struct |  | The information about the secondary region. |
| --pk | String | 33994422***27712 | The primary key of the secondary cloud instance. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| --regionId | String | cn-guznagxi | The region ID of the secondary cloud. |
|---|---|---|---|
| --regionName | String | guznagxi | The region name of the secondary cloud. |
| --regionType | String | CENTRAL | The type of the region. Valid values: CENTRAL UNIT |
| --consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |
| -- consoleApiEnd point | String | http://internal.exa mple.com.xxxxx | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |
| -- cloudInstance | Struct |  | The information about the secondary cloud instance. |
| --- aliyunAccount Uid | String | 178511195******9 6 | The UID of the Apsara Stack tenant account to which the secondary cloud instance belongs. |
| ---ownerUid | String | 23972451*****687 32 | The UID of the owner of the secondary cloud instance. |
| ---creator | String | 23972451*****687 32 | The UID of the user who created the secondary cloud instance. |
| ---lastModifier | String | 23972451*****687 32 | The UID of the user who last modified the secondary cloud instance. |
| --- resourceRegio nId | String | cn-hangzhou | The region ID of the secondary cloud instance. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| --- resourceGroup Id | String | 103 | The ID of the resource group to which the secondary cloud instance belongs. |
|---|---|---|---|
| ---createdDate | Long | 1704366334000 | The time when the secondary cloud instance was created. |
| --- lastModifiedDa te | Long | 1704366334000 | The time when the secondary cloud instance was last modified. |
| ---instanceId | String | e250008c-a02a- 455c-b957- 8d*****4ef58 | The ID of the secondary cloud instance. |
| --- instanceName | String | XXX | The name of the secondary cloud instance. |
| ---pk | String | 339944229200627 712 | The primary key of the secondary cloud instance. |
| --- cloudUniqueId | String | 0179 | The UID of the secondary cloud. |
| ---cloudOsType | String | ENTERPRISE | The edition of the secondary cloud instance. Only ENTERPRISE may be returned, which indicates Apsara Stack. |
| ---version | String | 1.0.0 | The version number of the secondary cloud instance. |
| ---consoleType | String | ASCM | The type of cloud management. Valid values: ASCM: The API of the Apsara Uni- manager Management Console is used. The endpoint of the API is used as the endpoint of the cloud management API. In most cases, this type is used in cross- region disaster recovery scenarios. ASRDR: The API of ASR-DR is used. The endpoint of the ASR-DR API is used as the endpoint of the cloud management API. In most cases, this type is used in cross-cloud disaster recovery scenarios. |
| --- consoleApiEnd point | String | http://internal.exa mple.com.xxxxx | The endpoint of the cloud management API. The value of this parameter depends on the value of the consoleType parameter. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| --- adminCredenti alsId | String | 339944225551583 232 | The credential ID of the cloud management administrator. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of an operations administrator. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as the operations administrator, click the profile picture in the upper-right corner, and then select User Information. On the page that appears, obtain an AccessKey pair in the AccessKey Pair section. |
|---|---|---|---|
| --- accountCrede ntialsId | String | 339944225551583 232 | The credential ID of the organization account. The credential ID is automatically generated based on the AccessKey ID and AccessKey secret of a level-1 organization. To obtain an AccessKey pair, log on to the Apsara Uni-manager Management Console as an organization administrator. In the top navigation bar, click Enterprise. In the left-side navigation pane, choose Resources > Organizations. On the page that appears, obtain an AccessKey pair of a level-1 organization. |
| --- internetDomai n | String | inter.***.shuguang. com | The Internet domain name. |
| --- intranetDomai n | String | intra.***.shuguang. com | The internal domain name. |
| ---status | String | REGULAR | The status of the secondary cloud instance. Valid values: REGULAR: normal. NOT CONFIGURED: not configured. _ UNINITIALIZED: not initialized. The cloud instance is in this state if no administrator credentials are configured when you log on to ASR-DR for the first time. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Apsara Stack Resilience ASR for Geo-disaster Developer Sample requests

```
http(s)://[Endpoint]/?Action=GetRecoveryPlanSnapshot &TaskId=379e********98c7 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "data":{
  "-backupRegion":{
   "regionId":"cn-guznagxi",
   "regionType":"CENTRAL",
   "consoleApiEndpoint":"http://internal.example.com.xxxxx",
   "regionName":"guznagxi",
   "pk":"33994422***27712",
   "--cloudInstance":{
    "cloudUniqueId":"0179",
    "creator":"23972451*****68732",
    "lastModifiedDate":1704366334000,
    "instanceName":"XXX",
    "consoleApiEndpoint":"http://internal.example.com.xxxxx",
    "resourceRegionId":"cn-hangzhou",
    "lastModifier":"23972451*****68732",
    "adminCredentialsId":"339944225551583232",
    "version":"1.0.0",
    "cloudOsType":"ENTERPRISE",
    "createdDate":1704366334000,
    "instanceId":"e250008c-a02a-455c-b957-8d*****4ef58",
    "aliyunAccountUid":"178511195******96",
    "internetDomain":"inter.***.shuguang.com",
    "resourceGroupId":"103",
    "pk":"339944229200627712",
    "intranetDomain":"intra.***.shuguang.com",
    "ownerUid":"23972451*****68732",
    "accountCredentialsId":"339944225551583232",
    "consoleType":"ASCM",
    "status":"REGULAR"
   },
   "consoleType":"ASCM"
  },
  "creator":"239724*****8868732",
  "lastModifiedDate":1713514782222,
  "-mainRegion":{
   "regionId":"cn-guznagxi",
   "regionType":"CENTRAL",
   "consoleApiEndpoint":"http://internal.example.com.xxxxx",
   "regionName":"guznagxi",
   "pk":"33994422***27712",
"--cloudInstance":{
```

ASR for Geo-disaster Developer Apsara Stack Resilience

```json
cloudInstance:{
    "cloudUniqueId":"0179",
    "creator":"23972451*****68732",
    "lastModifiedDate":1704366334000,
    "instanceName":"XXX",
    "consoleApiEndpoint":"http://internal.example.com.xxxxx",
    "resourceRegionId":"cn-hangzhou",
    "lastModifier":"23972451*****68732",
    "adminCredentialsId":"339944225551583232",
    "version":"1.0.0",
    "cloudOsType":"ENTERPRISE",
    "createdDate":1704366334000,
    "instanceId":"e250008c-a02a-455c-b957-8d*****4ef58",
    "aliyunAccountUid":"178511195******96",
    "internetDomain":"inter.***.shuguang.com",
    "resourceGroupId":"103",
    "pk":"339944229200627712",
    "intranetDomain":"intra.***.shuguang.com",
    "ownerUid":"23972451*****68732",
    "accountCredentialsId":"339944225551583232",
    "consoleType":"ASCM",
    "status":"REGULAR"
   },
   "consoleType":"ASCM"
  },
  "resourceRegionId":"cn-hangzhou",
  "lastModifier":"239724*****8868732",
  "description":"This is an example instance.",
  "type":"DRILL_ONLY",
  "-relatedProtectGroups":{
   "creator":"2397******98868732",
   "createdDate":1673333258000,
   "instanceId":"79e********98c7",
   "lastModifiedDate":1673333258012,
   "aliyunAccountUid":"1785******267796",
   "resourceRegionId":"cn-hangzhou",
   "name":"name1",
   "lastModifier":"2397******98868732",
   "resourceGroupId":"fe1********6d6d",
   "id":"79e********98c7",
   "ownerUid":"2397******98868732"
  },
  "sequence":"",
  "createdDate":1713514782222,
  "instanceId":"e250008c-a02a-455c-b957-8d*****ef58",
  "aliyunAccountUid":"1785111957*****236",
  "name":"MyInstance",
  "resourceGroupId":"103",
  "id":"e250008c-a02a-455c-b957-8d*****ef58",
  "ownerUid":"239724*****8868732",
  "stability":"GREEN"
 },
 "requestId":"a62a********bcd1",
 "success":true,
 "nodeIp":"127.0.0.1"
```

Apsara Stack Resilience ASR for Geo-disaster Developer p

```
}
```

`XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <data>
 <-backupRegion>
  <regionId>cn-guznagxi</regionId>
  <regionType>CENTRAL</regionType>
  <consoleApiEndpoint>http://internal.example.com.xxxxx</consoleApiEndpoint>
  <regionName>guznagxi</regionName>
  <pk>33994422***27712</pk>
  <--cloudInstance>
   <cloudUniqueId>0179</cloudUniqueId>
   <creator>23972451*****68732</creator>
   <lastModifiedDate>1704366334000</lastModifiedDate>
   <instanceName>XXX</instanceName>
   <consoleApiEndpoint>http://internal.example.com.xxxxx</consoleApiEndpoint>
   <resourceRegionId>cn-hangzhou</resourceRegionId>
   <lastModifier>23972451*****68732</lastModifier>
   <adminCredentialsId>339944225551583232</adminCredentialsId>
   <version>1.0.0</version>
   <cloudOsType>ENTERPRISE</cloudOsType>
   <createdDate>1704366334000</createdDate>
   <instanceId>e250008c-a02a-455c-b957-8d*****4ef58</instanceId>
   <aliyunAccountUid>178511195******96</aliyunAccountUid>
   <internetDomain>inter.***.shuguang.com</internetDomain>
   <resourceGroupId>103</resourceGroupId>
   <pk>339944229200627712</pk>
   <intranetDomain>intra.***.shuguang.com</intranetDomain>
   <ownerUid>23972451*****68732</ownerUid>
   <accountCredentialsId>339944225551583232</accountCredentialsId>
   <consoleType>ASCM</consoleType>
   <status>REGULAR</status>
  </--cloudInstance>
  <consoleType>ASCM</consoleType>
 </-backupRegion>
 <creator>239724*****8868732</creator>
 <lastModifiedDate>1713514782222</lastModifiedDate>
 <-mainRegion>
  <regionId>cn-guznagxi</regionId>
  <regionType>CENTRAL</regionType>
  <consoleApiEndpoint>http://internal.example.com.xxxxx</consoleApiEndpoint>
  <regionName>guznagxi</regionName>
  <pk>33994422***27712</pk>
  <--cloudInstance>
   <cloudUniqueId>0179</cloudUniqueId>
   <creator>23972451*****68732</creator>
   <lastModifiedDate>1704366334000</lastModifiedDate>
   <instanceName>XXX</instanceName>
   <consoleApiEndpoint>http://internal.example.com.xxxxx</consoleApiEndpoint>
<resourceRegionId>cn-hangzhou</resourceRegionId>
```

ASR for Geo-disaster Developer Apsara Stack Resilience

```xml
   <resourceRegionId>cn-hangzhou</resourceRegionId>
   <lastModifier>23972451*****68732</lastModifier>
   <adminCredentialsId>339944225551583232</adminCredentialsId>
   <version>1.0.0</version>
   <cloudOsType>ENTERPRISE</cloudOsType>
   <createdDate>1704366334000</createdDate>
   <instanceId>e250008c-a02a-455c-b957-8d*****4ef58</instanceId>
   <aliyunAccountUid>178511195******96</aliyunAccountUid>
   <internetDomain>inter.***.shuguang.com</internetDomain>
   <resourceGroupId>103</resourceGroupId>
   <pk>339944229200627712</pk>
   <intranetDomain>intra.***.shuguang.com</intranetDomain>
   <ownerUid>23972451*****68732</ownerUid>
   <accountCredentialsId>339944225551583232</accountCredentialsId>
   <consoleType>ASCM</consoleType>
   <status>REGULAR</status>
  </--cloudInstance>
  <consoleType>ASCM</consoleType>
 </-mainRegion>
 <resourceRegionId>cn-hangzhou</resourceRegionId>
 <lastModifier>239724*****8868732</lastModifier>
 <description>This is an example instance.</description>
 <type>DRILL_ONLY</type>
 <-relatedProtectGroups>
  <creator>2397******98868732</creator>
  <createdDate>1673333258000</createdDate>
  <instanceId>79e********98c7</instanceId>
  <lastModifiedDate>1673333258012</lastModifiedDate>
  <aliyunAccountUid>1785******267796</aliyunAccountUid>
  <resourceRegionId>cn-hangzhou</resourceRegionId>
  <name>name1</name>
  <lastModifier>2397******98868732</lastModifier>
  <resourceGroupId>fe1********6d6d</resourceGroupId>
  <id>79e********98c7</id>
  <ownerUid>2397******98868732</ownerUid>
 </-relatedProtectGroups>
 <sequence  />
 <createdDate>1713514782222</createdDate>
 <instanceId>e250008c-a02a-455c-b957-8d*****ef58</instanceId>
 <aliyunAccountUid>1785111957*****236</aliyunAccountUid>
 <name>MyInstance</name>
 <resourceGroupId>103</resourceGroupId>
 <id>e250008c-a02a-455c-b957-8d*****ef58</id>
 <ownerUid>239724*****8868732</ownerUid>
 <stability>GREEN</stability>
</data> <requestId>a62a********bcd1</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### CompleteSequence

Completes a step when you run a disaster recovery plan.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| TaskId | Long | Body | Yes | 14 | The task ID of the disaster recovery plan. |
| SequenceT askId | Long | Body | Yes | 21 | The task ID of the step. |
| Message | Strin g | Body | No | Manually confirm the step | The remarks. |

| > Document Versi | on: 20260701 |  | 33 |
|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
| success | Boolean | true | Indicates whether the request was successful. |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Examples**

Sample requests

```
&TaskId=14 &SequenceTaskId=21 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AsrMainCl oudInstan ceId | Strin g | Query | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

Apsara Stack Resilience ASR for Geo-disaster Developer

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### ListRecoveryTaskDataByPage

Queries a list of tasks that are run for disaster recovery plans by page.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AsrMainRe gionId | Strin g | Query | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Query | No | 3 | The organization ID. This is a parameter of the Apsara Stack API. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Resource Group | Strin g | Query | No | 3 | The ID of the resource set. This is a parameter of the Apsara Stack API. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | No | cn-hangzhou | The region ID of the resource. This is a parameter of the Apsara Stack API. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console page. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RunMode | Strin g | Query | No | DRILL | The mode in which the disaster recovery plan is run. This parameter is used to query data in exact match mode. Valid values: DRILL DR |
| RecoveryP lanId | Long | Query | No | 12467733*****0098 | The ID of the disaster recovery plan. This parameter is used to query data in exact match mode. |
| RecoveryP lanName | Strin g | Query | No | RecoveryPlan1 | The name of the disaster recovery plan. This parameter is used to query data in fuzzy match mode. |
| Status | Strin g | Query | No | PENDING | The state of the task. This parameter is used to query data in exact match mode. You can specify one or more states. Separate multiple states with commas ( , ). Valid values: PENDING INITIALIZING RUNNING SWITCHING OVER _ WAITING RECOVER _ SWITCHING BACK _ ABORTING ABORTED TIMEOUT FAILED COMPLETED |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AccordExp ect | Strin g | Query | No | true | Specifies whether the results of the disaster recovery plan meet expectations. Valid values: true false NAN |
| CountSeq uence | Boole an | Query | No | true | Specifies whether to count the number of steps. Valid values: true -false |
| PageNum | Integ er | Query | Yes | 1 | The page number. Pages start from page 1. |
| PageSize | Integ er | Query | Yes | 10 | The number of entries per page. |
| Sort | Strin g | Query | No | createsAt | The sorting field. Valid values: createsAt: sorts tasks by the time when the task was created. completesAt: sorts tasks by the time when the task was complete. Incomplete tasks are always ranked first regardless of whether tasks are sorted in ascending or descending order. |
| Order | Strin g | Query | No | DESC | The sorting order. Valid values: DESC ASC |

| Parameter | Type | Example | Description |
|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
| success | Boolean | true | Indicates whether the request was successful. |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |
| data | Struct |  | The returned data. |
| -rows | Array |  | The queried entries. |
| -- sequenceTask s | Normal |  | The tasks that were run for steps, in the JSON format. |
| --taskId | String | 14 | The task ID. |
| -- recoveryPlanId | String | 21 | The ID of the disaster recovery plan. |
| -- recoveryPlanN ame | String | recoveryPlan1 | The name of the disaster recovery plan. |
| --runMode | String | DRILL | The mode in which the disaster recovery plan is run. Valid values: DRILL DR |

ASR for Geo-disaster Developer Apsara Stack Resilience

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- creatorAliyunA ccountUid | String | 2397******988687 32 | The unique ID (UID) of the Apsara Stack tenant account that is used to create the task. |
| -- creatorAliyunA ccountUid | String | 2397******988687 32 | The UID of the Apsara Stack tenant account that is used to create the task. |
| --createsAt | Long | 1713514782222 | The time when the task was created. |
| --runsAt | Long | 1713514782222 | The time when the task started. |
| --completesAt | Long | 1713514782225 | The time when the task was complete. |
| --status | String | PENDING | The state of the task. Valid values: PENDING INITIALIZING RUNNING SWITCHING OVER _ WAITING RECOVER _ SWITCHING BACK _ ABORTING ABORTED TIMEOUT FAILED COMPLETED |
| --statusMsg | String | Development test ABCD | The description of the task. |
| -- exceptionThro wn | Boolean | true | Indicates whether an exception was thrown when the task was running. Valid values: true false |
| -- exceptionMsg | String | 400 | The error message returned if an exception was thrown. |
| --nodeId | String | Local 001 _ | The ID of the node that was processing the task. |
| -- sequenceCoun t | Integer | 12 | The number of steps included in the task. Only the root step is counted. |

Apsara Stack Resilience ASR for Geo-disaster Developer

| A | SR for Geo-disast Guide·API referen | er Developer ce |  | Apsara Stack Resilienc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --loggerId | Long | 1232342443 | The ID of the task logger. |
| --loggerToken | String | xxx-xxx-xxx | The credentials for querying task logs. |
| --statistic | Struct |  | The statistics about tasks. |
| ---taskId | String | 12 | The task ID. |
| --- durationMillis | Long | 0 | The duration of the task, in milliseconds. |
| ---succeed | Boolean | true | Indicates whether the task was successful. |
| --- accordExpect | Boolean | true | Indicates whether the results meet expectations. |
| ---evaluation | String | The drill is successful. | The conclusion of the drill. |
| ---reportFileId | String | 1 | The report file ID of the drill. |
| ---execCount | Integer | 21 | The total number of tasks that were run for the plan as of the current task. |
| --- execSucceedC ount | Integer | 5 | The total number of tasks that were successfully run for the plan as of the current task. |
| --- protectGroupT otalCount | Integer | 1 | The total number of protection groups included in the task. |
| --- protectGroupS witchOverTota lCount | Integer | 1 | The total number of protection groups that involve switchover or failover in the task. |
| --- protectGroupS witchBackTota lCount | Integer | 1 | The total number of protection groups that involve switchback or failback in the task. |
| --- protectGroupS witchOverSucc eedCount | Integer | 1 | The total number of protection groups whose switchover or failover was successful in the task. |

| psara Stack Resil | ience |  | ASR for Geo-disaster Developer |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --- protectGroupS witchBackSucc eedCount | Integer | 1 | The total number of protection groups whose switchback or failback was successful in the task. |
| --- instanceTotalC ount | Integer | 1 | The total number of synchronization entities included in the task. |
| --- instanceSwitch OverTotalCoun t | Integer | 1 | The total number of synchronization entities that involve switchover or failover in the task. |
| --- instanceSwitch BackTotalCoun t | Integer | 1 | The total number of synchronization entities that involve switchback or failback in the task. |
| --- instanceRpoQ ualifiedCount | Integer | 1 | The number of synchronization entities whose synchronization latency meets expectations. |
| --- instanceSwitch OverDurationQ ualifiedCount | Integer | 1 | The number of synchronization entities whose switchover or failover duration meets expectations. |
| --- instanceSwitch BackDuration QualifiedCount | Integer | 1 | The number of synchronization entities whose switchback or failback duration meets expectations. |
| -pageNum | Integer | 1 | The page number. |
| -pageSize | Integer | 10 | The number of entries per page. This parameter indicates the expected number of entries per page. The value is the same as the value of the corresponding parameter specified in the request. If the actual length of the returned rows parameter is less than the value of this parameter, the last page is returned. |
| -total | Integer | 55 | The total number of entries that meet query conditions. |

**Examples**

Sample requests ASR for Geo-disaster Developer Apsara Stack Resilience

```
http(s)://[Endpoint]/?Action=ListRecoveryTaskDataByPage &PageNum=1 &PageSize=10 &<Common request parameters>
```

Sample success responses `JSON` format Apsara Stack Resilience ASR for Geo-disaster Developer

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "data":{
  "total":55,
  "-rows":{
   "createsAt":1713514782222,
   "creatorAliyunAccountUid":"2397******98868732",
   "sequenceTasks":"",
   "runMode":"DRILL",
   "loggerToken":"xxx-xxx-xxx",
   "completesAt":1713514782225,
   "exceptionThrown":true,
   "exceptionMsg":"400",
   "sequenceCount":12,
   "statusMsg":"Development test ABCD",
   "recoveryPlanName":"recoveryPlan1",
   "runsAt":1713514782222,
   "loggerId":1232342443,
   "nodeId":"Local_001",
   "taskId":"14",
   "recoveryPlanId":"21",
   "--statistic":{
    "reportFileId":"1",
    "instanceTotalCount":1,
    "protectGroupSwitchOverSucceedCount":1,
    "protectGroupTotalCount":1,
    "instanceSwitchOverTotalCount":1,
    "execCount":21,
    "durationMillis":0,
    "protectGroupSwitchOverTotalCount":1,
    "instanceRpoQualifiedCount":1,
    "accordExpect":true,
    "instanceSwitchBackDurationQualifiedCount":1,
    "evaluation":"The drill is successful.",
    "instanceSwitchOverDurationQualifiedCount":1,
    "instanceSwitchBackTotalCount":1,
    "succeed":true,
    "protectGroupSwitchBackTotalCount":1,
    "execSucceedCount":5,
    "taskId":"12",
    "protectGroupSwitchBackSucceedCount":1
   },
   "status":"PENDING"
  },
  "pageSize":10,
  "pageNum":1
 },
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

ASR for Geo-disaster Developer Apsara Stack Resilience `XML` format Apsara Stack Resilience ASR for Geo-disaster Developer

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <data>
 <total>55</total>
 <-rows>
  <createsAt>1713514782222</createsAt>
  <creatorAliyunAccountUid>2397******98868732</creatorAliyunAccountUid>
  <sequenceTasks  />
  <runMode>DRILL</runMode>
  <loggerToken>xxx-xxx-xxx</loggerToken>
  <completesAt>1713514782225</completesAt>
  <exceptionThrown>true</exceptionThrown>
  <exceptionMsg>400</exceptionMsg>
  <sequenceCount>12</sequenceCount>
  <statusMsg>Development test ABCD</statusMsg>
  <recoveryPlanName>recoveryPlan1</recoveryPlanName>
  <runsAt>1713514782222</runsAt>
  <loggerId>1232342443</loggerId>
  <nodeId>Local_001</nodeId>
  <taskId>14</taskId>
  <recoveryPlanId>21</recoveryPlanId>
  <--statistic>
   <reportFileId>1</reportFileId>
   <instanceTotalCount>1</instanceTotalCount>
   <protectGroupSwitchOverSucceedCount>1</protectGroupSwitchOverSucceedCount>
   <protectGroupTotalCount>1</protectGroupTotalCount>
   <instanceSwitchOverTotalCount>1</instanceSwitchOverTotalCount>
   <execCount>21</execCount>
   <durationMillis>0</durationMillis>
   <protectGroupSwitchOverTotalCount>1</protectGroupSwitchOverTotalCount>
   <instanceRpoQualifiedCount>1</instanceRpoQualifiedCount>
   <accordExpect>true</accordExpect>
<instanceSwitchBackDurationQualifiedCount>1</instanceSwitchBackDurationQualifiedCount>
   <evaluation>The drill is successful.</evaluation>
<instanceSwitchOverDurationQualifiedCount>1</instanceSwitchOverDurationQualifiedCount>
   <instanceSwitchBackTotalCount>1</instanceSwitchBackTotalCount>
   <succeed>true</succeed>
   <protectGroupSwitchBackTotalCount>1</protectGroupSwitchBackTotalCount>
   <execSucceedCount>5</execSucceedCount>
   <taskId>12</taskId>
   <protectGroupSwitchBackSucceedCount>1</protectGroupSwitchBackSucceedCount>
  </--statistic>
  <status>PENDING</status>
 </-rows>
 <pageSize>10</pageSize>
 <pageNum>1</pageNum>
</data> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

ASR for Geo-disaster Developer Apsara Stack Resilience

##### RerunSequence

Retries a step when you run a disaster recovery plan.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| TaskId | Long | Body | Yes | 12467733*****0098 | The task ID of the disaster recovery plan. |
| SequenceT askId | Long | Body | Yes | 47632984***3240 | The task ID of the step. |
| Message | Strin g | Body | No | Retry the step | The remarks. |

| 52 |  |  | > Document Version: 2026070 |
|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
| success | Boolean | true | Indicates whether the request was successful. |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Examples**

Sample requests

```
&TaskId=12467733*****0098 &SequenceTaskId=47632984***3240 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

`XML` format

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AsrMainClo udInstance Id | Strin g | Quer y | No | f8f72032-5e49-4a38- 9750-f8a9****4bca | The ID of the primary cloud instance. This is a common parameter of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR). When you query or modify a resource, this parameter determines the primary cloud instance to which the resource belongs. If the primary cloud instance to which the resource to be queried or modified belongs is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary cloud instance in which the resource is to be created. |

ASR for Geo-disaster Developer Apsara Stack Resilience

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```

##### SkipSequence

Skips a step when you run a disaster recovery plan.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| AsrMainRe gionId | Strin g | Quer y | No | cn-hangzhou | The ID of the primary region. This is a common parameter of ASR-DR. When you query or modify a resource, this parameter determines the primary region in which the resource resides. If the primary region in which the resource to be queried or modified resides is different from that specified by this parameter, an error is reported to indicate that the resource does not exist. When you create a resource, this parameter determines the primary region in which the resource is to be created. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| Departme nt | Strin g | Quer y | No | 3 | The organization ID. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the organization that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the organization that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the Apsara Stack tenant account to which the resource belongs. If the resource to be queried or modified is not within the Apsara Stack tenant account to which the organization belongs, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified within the Apsara Stack tenant account to which your organization belongs. When you create a resource, this parameter determines the Apsara Stack tenant account within which the resource is to be created. If you do not specify this parameter, the resource is created within the Apsara Stack tenant account to which your organization belongs. |
|---|---|---|---|---|---|

ASR for Geo-disaster Developer Apsara Stack Resilience

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the resource set that is visible to you. If you use the Apsara Uni- manager Management Console, you can specify the ID of the resource set that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the resource group to which the resource belongs. If the resource to be queried or modified does not belong to the resource group, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in all resource groups that are visible to you. When you create a resource, this parameter determines the resource group in which the resource is to be created. If you do not specify this parameter, the resource does not belong to a resource group. |
|---|---|---|---|---|---|

Apsara Stack Resilience ASR for Geo-disaster Developer

| RegionId | Strin g | Quer y | No | cn-hangzhou | The region ID of the resource. This is an API parameter of the Apsara Uni-manager Management Console. You can specify only the ID of the region that is visible to you. If you use the Apsara Uni-manager Management Console, you can specify the ID of the region that is selected in the top navigation bar of the console. When you query or modify a resource, this parameter determines the region in which the resource resides. If the resource to be queried or modified does not reside in the region, an error is reported to indicate that the resource does not exist. If you do not specify this parameter, the resource is queried or modified in the region of the node that processes the request. When you create a resource, this parameter determines the region in which the resource is to be created. If you do not specify this parameter, the resource is created in the region of the node that processes the request. |
|---|---|---|---|---|---|
| TaskId | Long | Body | Yes | 3dcc********9f64 | The task ID of the disaster recovery plan. |
| SequenceT askId | Long | Body | Yes | 432nd****3d8r | The task ID of the step. |
| Message | Strin g | Body | No | Skip the step | The remarks. |

ASR for Geo-disaster Developer Apsara Stack Resilience

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ebc6********00e7 | The request ID. |
| result | String | SUCCESS | Indicates whether the request was successful. Valid values: SUCCESS FAILED This parameter is maintained for compatibility and has the same meaning as the success parameter. We recommend that you use the success parameter. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true false |
| code | String | 200 | The response code. |
| nodeHost | String | B-W0Y****- 1914.local | The name of the node that processed the request. |
| nodeIp | String | 127.0.0.1 | The IP address of the node that processed the request. |

Apsara Stack Resilience ASR for Geo-disaster Developer

**Examples**

Sample requests

```
&TaskId=3dcc********9f64 &SequenceTaskId=432nd****3d8r &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "result":"SUCCESS",
 "nodeHost":"B-W0Y****-1914.local",
 "code":"200",
 "requestId":"ebc6********00e7",
 "success":true,
 "nodeIp":"127.0.0.1"
}
```

ASR for Geo-disaster Developer Apsara Stack Resilience `XML` format

```xml
<result>SUCCESS</result> <nodeHost>B-W0Y****-1914.local</nodeHost> <code>200</code> <requestId>ebc6********00e7</requestId> <success>true</success> <nodeIp>127.0.0.1</nodeIp>
```
