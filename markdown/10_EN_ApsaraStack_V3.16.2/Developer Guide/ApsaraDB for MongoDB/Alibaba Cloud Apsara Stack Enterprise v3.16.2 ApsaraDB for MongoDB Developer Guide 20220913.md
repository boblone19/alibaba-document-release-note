---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 ApsaraDB for MongoDB Developer Guide"
product_version: "V3.16.2"
doc_version: "20220913"
pdf_pages: 221
source_pdf: "62916d8b6b6ac546_Alibaba Cloud Apsara Stack Enterprise v3.16.2 ApsaraDB for MongoDB Developer Guide 20220913.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.16.2_intl_en/%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97%2B%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20ApsaraDB%20for%20MongoDB%20Developer%20Guide%2020220913.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 ApsaraDB for MongoDB Developer Guide

## Table of Contents

- 1 Getting started
  - 1.1 Usage notes on development documentation
  - 1.2 Process of API calls
- 2 Preparations
  - 2.1 Log on to the API Tool console
  - 2.2 View the API-related information
  - 2.3 Obtain an AccessKey pair
  - 2.4 Obtain the values of common headers
  - 2.5 Obtain the endpoint of ApsaraDB for MongoDB
  - 2.6 Obtain the SDKs of ApsaraDB for MongoDB
- 3 Call examples for SDK for Java
  - 3.1 Getting started
  - 3.2 Use SDK
    - 3.2.1 Install ApsaraDB for MongoDB SDK for Java
    - 3.2.2 Configure authentication credentials
    - 3.2.3 Configure connection requests
    - 3.2.4 Initiate a request
    - 3.2.5 Handle errors
- 4 Call examples for SDK for Python
  - 4.1 Getting started
  - 4.2 Use SDK
    - 4.2.1 Install ApsaraDB for MongoDB SDK for Python
    - 4.2.2 Configure authentication credentials
    - 4.2.3 Set HTTPS requests
    - 4.2.4 Initiate a request
    - 4.2.5 Handle errors
- 5 Call examples for SDK for Go
  - 5.1 Getting started
  - 5.2 Use SDK
    - 5.2.1 Install Go SDK
    - 5.2.2 Configure authentication credentials
    - 5.2.3 Initiate a request
    - 5.2.4 Handle errors
- 6 List of operations by function
- 7 API Reference
  - 7.1 Lifecycle management
    - 7.1.1 CreateDBInstance
    - 7.1.2 ModifyDBInstanceSpec
    - 7.1.3 DeleteDBInstance
    - 7.1.4 CreateShardingDBInstance
    - 7.1.5 CreateNode
    - 7.1.6 DeleteNode
    - 7.1.7 ModifyNodeSpec
  - 7.2 Region management
    - 7.2.1 MigrateToOtherZone
    - 7.2.2 DescribeRegions
    - 7.2.3 MigrateAvailableZone
  - 7.3 Resource management
    - 7.3.1 DescribeAvailableResource
  - 7.4 Connection management
    - 7.4.1 AllocatePublicNetworkAddress
    - 7.4.2 ReleasePublicNetworkAddress
    - 7.4.3 ModifyInstanceVpcAuthMode
    - 7.4.4 DescribeShardingNetworkAddress
    - 7.4.5 ModifyDBInstanceConnectionString
    - 7.4.6 ReleaseNodePrivateNetworkAddress
  - 7.5 Instance information query
    - 7.5.1 DescribeReplicaSetRole
    - 7.5.2 DescribeKernelReleaseNotes
    - 7.5.3 DescribeAvailableEngineVersion
    - 7.5.4 DescribeDBInstances
    - 7.5.5 DescribeDBInstanceAttribute
    - 7.5.6 DescribeRoleZoneInfo
  - 7.6 Instance management
    - 7.6.1 RestartDBInstance
    - 7.6.2 ModifyDBInstanceMaintainTime
    - 7.6.3 ModifyDBInstanceDescription
    - 7.6.4 SwitchDBInstanceHA
    - 7.6.5 UpgradeDBInstanceEngineVersion
    - 7.6.6 UpgradeDBInstanceKernelVersion
    - 7.6.7 ModifyDBInstanceNetExpireTime
  - 7.7 Account management
    - 7.7.1 DescribeAccounts
    - 7.7.2 ResetAccountPassword
    - 7.7.3 ModifyAccountDescription
  - 7.8 IP whitelists and security groups
    - 7.8.1 DescribeSecurityGroupConfiguration
    - 7.8.2 ModifySecurityGroupConfiguration
    - 7.8.3 DescribeSecurityIps
    - 7.8.4 ModifySecurityIps
  - 7.9 Key management
    - 7.9.1 DescribeDBInstanceTDEInfo
    - 7.9.2 ModifyDBInstanceTDE
  - 7.10 SSL encryption
    - 7.10.1 ModifyDBInstanceSSL
    - 7.10.2 DescribeDBInstanceSSL
  - 7.11 Audit logs
    - 7.11.1 DescribeAuditRecords
    - 7.11.2 DescribeAuditFiles
    - 7.11.3 DescribeAuditPolicy
    - 7.11.4 ModifyAuditLogFilter
    - 7.11.5 DescribeAuditLogFilter
    - 7.11.6 ModifyAuditPolicy
  - 7.12 Log management
    - 7.12.1 DescribeSlowLogRecords
    - 7.12.2 DescribeErrorLogRecords
    - 7.12.3 DescribeRunningLogRecords
  - 7.13 Performance monitoring management
    - 7.13.1 DescribeDBInstancePerformance
    - 7.13.2 DescribeDBInstanceMonitor
  - 7.14 Parameter management
    - 7.14.1 DescribeParameterModificationHistory
    - 7.14.2 DescribeParameters
    - 7.14.3 ModifyParameters
  - 7.15 Backup and recovery
    - 7.15.1 DescribeBackupPolicy
    - 7.15.2 ModifyBackupPolicy
    - 7.15.3 CreateBackup
    - 7.15.4 DescribeBackups
    - 7.15.5 RestoreDBInstance
    - 7.15.6 DescribeBackupDBs
  - 7.16 Instance states
- 8 Appendixes
  - 8.1 Call the ASAPI gateway
  - 8.2 Use the ASAPI gateway to make API calls
    - 8.2.1 Obtain an endpoint of ASAPI
    - 8.2.2 Obtain Apsara Stack SDKs
  - 8.3 STS overview
    - 8.3.1 What is STS?
    - 8.3.2 AssumeRole

## 1 Getting started

### 1.1 Usage notes on development documentation

documentation This topic describes how to view the desired product development documentation when you use Apsara Stack API (ASAPI). Prerequisites The Apsara Stack version is obtained from an O&M personnel or operations administrator. Procedure You can go to the Apsara Stack documentation center and view the desired product documentation.
1. Go to the Apsara Stack Documentation Center page by using a browser.
2. Click the Ent erprise, Agilit y, or All-in-one tab based on the Apsara Stack version that you use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the name of the product that you want to view.
5. In the upper-right corner of the product documentation section, click View Det ails or Download
PDF.

### 1.2 Process of API calls

You can use POP Gateway or the Apsara Stack API (ASAPI) gateway to call Apsara Stack API operations. Since Apsara Stack Enterprise V3.16.0, POP Gateway is used by default to ensure that the user experience is consistent with that in Alibaba Cloud public cloud. This topic describes how to use POP Gateway to call Apsara Stack API operations. You can continue to use the ASAPI gateway to call API operations in Apsara Stack that is earlier than V3.16.0. For more information, see Process of API calls by using the ASAPI gateway, Generate an endpoint for ASAPI, and Obtain Apsara Stack SDKs. Procedure
1. Obtain an AccessKey pair.
Obtain the AccessKey pair that is required for the API call. For more information, see Obtain an AccessKey pair or Obtain an STS AccessKey pair assigned by STS. We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services.
2. Obtain the region ID.
For more information about how to obtain the value of the RegionID parameter, see Obtain the values of common headers.
3. Obtain the organization ID and resource set ID.
You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide. You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide. When you call an API operation, set the `<x-acs-organizationid>` parameter to the organization ID that you obtained, and set the `<x-acs-resourcegroupid>` parameter to the resource set ID that you obtained. This way, you can query resources in the specified organization and resource set. If you do not set the `<x-acs-organizationid>` parameter, the organization to which the current user belongs is queried. If you do not set the `<x-acs-resourcegroupid>` parameter, this parameter is left empty by default. If you specify a resource set, you must also specify an organization ID.
4. View the developer guide of the cloud service that you want to use to learn how to make the API
call. Obtain the developer guide of the cloud service that you want to use. This way, you can learn the features of API operations and how to call the API operations. For more information, see Usage notes on development documentation.
5. Obtain the endpoint of ApsaraDB for MongoDB. For more information, see Obtain the endpoint of
ApsaraDB for MongoDB.
6. Obtain the SDK package of ApsaraDB for MongoDB. For more information, see Obtain the SDKs of
ApsaraDB for MongoDB.
7. Make an API call. For more information, see Getting started (Java), Getting started (Python), or
Getting started (Go).

## 2 Preparations

### 2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

### 2.2 View the API-related information

This topic describes how to view the API-related information. Before you use SDKs, you must obtain service names, API operation names, and API versions. Context The API operations listed in API Reference are for reference only. For more information about how to call an API operation, see ApsaraDB for MongoDB Developer Guide. Procedure
1. Log on to the API Tool console.
2. In the left-side navigation pane, click API T ool.
3. On the API Direct ory page, select Dds from the product name drop-down list or search for Dds in
the product name field.
4. View and record the service name, API operation name, and API version.

### 2.3 Obtain an AccessKey pair

AccessKey pairs are classified into AccessKey pairs assigned by Resource Access Management (RAM) and those assigned by Security Token Service (STS). You can use either type of AccessKey pair for authentication when you call operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM. Context An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. You can use RAM or STS to assign an AccessKey pair for authentication. Use RAM to assign an AccessKey ID and an AccessKey secret to a third party. Use STS to assign an AccessKey ID, an AccessKey secret, and a security token to a third party. For more information, see Obtain an AccessKey pair assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only operations administrators and the administrators of level-1 organizations can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur. Warning The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. For example, if you use ApsaraDB for MongoDB, you can obtain the instance ID from the instance list page of ApsaraDB for MongoDB. |

Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, click the profile picture and then click User
Inf ormat ion.
3. In the AccessKey Pair section, view the AccessKey pair of your account.
An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Organizat ions.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you want
to obtain.
5. Click Management Accesskey.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### 2.4 Obtain the values of common headers

headers You must provide multiple headers when you call Apsara Stack operations. This topic describes the headers and how to obtain the values of the headers. This topic also describes the return values of specific headers after you call Apsara Stack operations. Headers

| Header | Descript ion |
|---|---|

| Header | Descript ion |
|---|---|
| x-acs-regionid | The ID of the region where the ApsaraDB for MongoDB instance resides. For more information about how to obtain region IDs, see the Obtain a region ID section of this topic. |
| x-acs-organizat ionid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see the Obtain an organization ID section of this topic. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see the Obtain a resource set ID section of this topic. |
| x-acs-inst anceid | The ID of the ApsaraDB for MongoDB instance on which you want to perform operations. For more information about how to obtain instance IDs, see the Obtain an instance ID section of this topic. |

Obtain a region ID
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Regions.
4. Click the name of the required organization.
5. View the region ID in the Regions section.
Obtain an organization ID You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide. Obtain a resource set ID You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide. Obtain an instance ID You can obtain the ID of an instance in a service console of the Apsara Uni-manager Management Console. In this example, the Elastic Compute Service (ECS) console is used. Perform the following operations to obtain the ID of an ECS instance:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Product s > Dat abase Services > ApsaraDB f or MongoDB.
3. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances
based on the instance type.
4. In the instance list that appears, find the instance whose ID you want to obtain and obtain its ID in
the Inst ance ID/Name column. Response parameters The following additional response parameters are returned by default when you call operations to query the instances of cloud services.

| Paramet er | Descript ion |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

### 2.5 Obtain the endpoint of ApsaraDB for MongoDB

for MongoDB This topic describes how to obtain the endpoint of ApsaraDB MongoDB. Background To use POP Gateway to call Apsara Stack API operations, you must use a service endpoint. You can obtain a service endpoint from an Apsara Stack onsite O&M engineer or by performing the following operations: Procedure
1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click Product s. iii. Choose Plat f orm >Apsara Inf rast ruct ure Management Framework.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for `Registration Vars of Services` and click the report name.
4. On the Regist rat ion Vars of Services page, click the
icon next to Service and search for

```
 MongoDB .
```

5. Find the `mongodb-yaochi` service, right-click the Service Regist rat ion column, and then select
Show More from the shortcut menu. In the Det ails dialog box, obtain the mongodb.openapi-inc.endpoint value. This value is the endpoint of ApsaraDB for MongoDB.

### 2.6 Obtain the SDKs of ApsaraDB for MongoDB

MongoDB Before you use POP Gateway to call Apsara Stack API operations of ApsaraDB for MongoDB, you must obtain the SDKs of ApsaraDB for MongoDB. This topic describes how to obtain the SDKs of ApsaraDB for MongoDB.

| Programming language | Download URL of an ApsaraDB f or MongoDB SDK | Ref erences |
|---|---|---|
| Alibaba Cloud SDK for Java | Alibaba Cloud MongoDB SDK for Java | Getting started (Java) |
| Alibaba Cloud SDK for Python | Alibaba Cloud MongoDB SDK for Python | Getting started (Python) |
| Alibaba Cloud SDK for Go | Alibaba Cloud MongoDB SDK for Go | Getting started (Go) |

We recommend that you use an SDK for Java, Python, or Go. If you use an SDK for a different programming language, the SDK may be incompatible with your system. SDK for Java

## 3 Call examples for SDK for Java

### 3.1 Getting started

This topic describes how to obtain and use ApsaraDB for MongoDB SDK for Java. Environment requirements An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. For more information about how to obtain the endpoint of ApsaraDB for MongoDB, see Obtain the endpoint of a cloud service. Apsara Stack SDK for Java 1.8 or later is installed. Install Apsara Stack SDK for Java If you use Apache Maven to manage Java projects, you need to only import JAR files to the pom.xml file of the projects. To use an ApsaraDB for MongoDB SDK, you must install the SDK core library and the ApsaraDB for MongoDB SDK. We recommend that you use version 4.5.17 or later for the SDK core library. In this example, the ApsaraDB for MongoDB SDK uses version 3.6.3. Use Apsara Stack SDK for Java Perform the following operations to use Apsara Stack SDK for Java:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exceptions.
You must use actual values to replace the variables in the following sample code. Do not retain the angle brackets (<>) in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID. SDK for Java

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.google.gson.Gson; import java.util.*; import com.aliyuncs.dds.model.v20151201.*; public class DescribeAccounts {
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAcce
ssKeyID>", "<yourAccessKeySecret>");
        IAcsClient client = new DefaultAcsClient(profile);
        DescribeAccountsRequest request = new DescribeAccountsRequest();
        request.setDBInstanceId("<yourDBInstanceId>");
        try {
            DescribeAccountsResponse response = client.getAcsResponse(request);
            System.out.println(new Gson().toJson(response));
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

`}` `}` `}`

### 3.2 Use SDK

#### 3.2.1 Install ApsaraDB for MongoDB SDK for Java

This topic describes how to install and use ApsaraDB for MongoDB SDK for Java. Apsara Stack SDK for Java 1.8 or later is required. To install ApsaraDB for MongoDB SDK for Java, add Maven dependencies or download ApsaraDB for MongoDB SDKs. For more information, see Obtain the SDKs of ApsaraDB for MongoDB. To use ApsaraDB for MongoDB SDK for Java, you must install the core library of Apsara Stack SDK for Java and ApsaraDB for MongoDB SDK for Java. We recommend that you use version 4.5.17 or later for the core library of Apsara Stack SDK for Java. In this example, ApsaraDB for MongoDB SDK for Java uses version 3.6.3. For example, to use ApsaraDB for MongoDB SDK for Java, you must install the core library of Apsara Stack SDK for Java and ApsaraDB for MongoDB SDK for Java, and then add the following dependencies to the pom.xml file. For information about the SDK version number, see Obtain the SDKs of ApsaraDB for MongoDB. SDK for Java

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency> <!-- dds java sdk --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-dds</artifactId>
    <version>3.6.3</version>
</dependency>
```

#### 3.2.2 Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you can use an AccessKey pair for identity verification. Apsara Stack SDK for Java supports identity verification based on AccessKey pairs. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you use an AccessKey pair to access Apsara Stack, you must configure your credential when initializing the client. Do not disclose any code that may contain your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack account may be compromised.

```xml
DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", " <yourAccessKeySecret>")
```

You must use actual values to replace the variables in the preceding sample code. Do not retain the angle brackets (<>) in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret.

#### 3.2.3 Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements. SDK for Java You must use actual values to replace the variables in the following sample code. Do not retain the angle brackets (<>) in the final code. The following list describes the variables: <readTimeout>: Specify the read timeout period based on your business requirements. Unit: milliseconds. <connectionTimeout>: Specify the connection timeout period based on your business requirements. Unit: milliseconds. <maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER. <maxRequests>: Specify the maximum number of requests based on your business requirements. The supported data type is INTEGER. <http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy.

```
// Obtain the HttpClientConfig object. HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Specify whether to ignore certificates. clientConfig.setIgnoreSSLCerts(true); // (Optional) Specify the read timeout period. Unit: milliseconds. clientConfig.setReadTimeoutMillis(<readTimeout>); // (Optional) Specify the connection timeout period. Unit: milliseconds. clientConfig.setConnectionTimeoutMillis(<connectionTimeout>); // (Optional) Specify the maximum number of requests that are supported by each server. The supported data type is INTEGER. clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>); // (Optional) Specify the maximum number of requests. The supported data type is INTEGER. clientConfig.setMaxRequests(<maxRequests>); // (Optional) Specify the protocol type. clientConfig.setProtocolType(ProtocolType.HTTP); /** (Optional) Specify whether to configure the proxy based on your business requirements. The following code is available: clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`Or`

```
clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>"); Replace https://192.168.XX.XX:33XX with the actual IP address and port of the proxy.
```

`*/`

```
profile.setHttpClientConfig(clientConfig);
```

#### 3.2.4 Initiate a request

This topic describes how to use ApsaraDB for MongoDB SDK for Java to initiate a request. Procedure
1. Create an ACS client.

```
IAcsClient client = new DefaultAcsClient(profile);
```

SDK for Java
2. Create a request.
The naming convention for requests is ${apiName}Request , where ${apiName} indicates the API name, such as DescribeAccounts. When you use the SDKs of multiple services, different requests may share the same name. Make sure to differentiate different requests by their SDK.

```
DescribeAccountsRequest request = new DescribeAccountsRequest();
      request.setDBInstanceId("dds-********");
      request.setAccountName("root");
```

3. Initiate the request and handle the response.

```
DescribeAccountsResponse response = client.getAcsResponse(request);
```

In normal cases, all returned fields are deserialized into the response. You can directly call `respons` `e.getXXX()` to obtain the response fields.

```
AccountData := response.getData()
```

If an exception occurs or you need the original HTTP response, use `doAction()` to obtain the original response.

```
HttpResponse response = client.doAction(request);
```

#### 3.2.5 Handle errors

If an error occurs on the server side or SDK side, the Apsara Stack Java SDK returns the corresponding exception message. An exception message contains the detailed error information, namely the error code and the error message. Generally, you are not required to handle the errors returned by the Apsara Stack Java SDK. You are only required to handle the errors on the server side according to the error message. `ServerException` is the error message on the server side. `ClientException` is the error message on the SDK side. For example, if the following error occurs, modify the ID of AccessKey according to the detailed error message.

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

To handle the errors returned by the Apsara Stack Java SDK, see the following code example for reference: SDK for Java

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handle the response.
    // ...
}catch (ServerException e){
    // Add your own error handling logic here.
    // For example, print the detailed error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If the problem is tricky, open a ticket and provide the RequestId for us.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // Add your own error handling logic here.
    // For example, print the detailed error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

`}` SDK for Python

## 4 Call examples for SDK for Python

Python

### 4.1 Getting started

This topic describes how to obtain and use ApsaraDB for MongoDB SDK for Python. Environment requirements An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain the endpoint of ApsaraDB for MongoDB, see Obtain the endpoint of ApsaraDB for MongoDB. Install ApsaraDB for MongoDB SDK for Python
1. Install the SDK core library.
If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-core-v3
```

2. Install ApsaraDB for MongoDB SDK for Python.
If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-dds
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-dds
```

Use ApsaraDB for MongoDB SDK for Python To use ApsaraDB for MongoDB SDK for Python, perform the following steps:
1. Create a client instance. When you create a client instance, you must obtain a region ID, AccessKey
ID, and AccessKey secret.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exceptions.
SDK for Python In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID.

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential from aliyunsdkdds.request.v20151201.DescribeAccountsRequest import DescribeAccountsRequ est credentials = AccessKeyCredential('<yourAccessKeyID>', '<yourAccessKeySecret>') client = AcsClient(region_id='<yourRegionID>', credential=credentials) request = DescribeAccountsRequest() request.set_accept_format('json') request.set_DBInstanceId("<yourDBInstanceId>") response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

### 4.2 Use SDK

#### 4.2.1 Install ApsaraDB for MongoDB SDK for Python

Python This topic describes how to install the core library of Apsara Stack SDK for Python and ApsaraDB for MongoDB SDK for Python. Background information To use a service SDK, you must install the core library of Apsara Stack SDK for Python. To use ApsaraDB for MongoDB SDK for Python, you must install the core library of Apsara Stack SDK for Python and ApsaraDB for MongoDB SDK for Python. Install the core library of Apsara Stack SDK for Python Apsara Stack SDK for Python supports Python 2.6.x, 2.7.x, as well as 3.x and later. You can use the pip command to install Apsara Stack SDK for Python. If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-core
```

SDK for Python If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-core-v3
```

Install ApsaraDB for MongoDB SDK for Python If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-dds
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-dds
```

#### 4.2.2 Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you can use an AccessKey pair for identity verification. Apsara Stack SDK for Python supports identity verification based on AccessKey pairs. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you use an AccessKey pair to access Apsara Stack, you must configure your credential when initializing the client. Not ice Do not disclose any code that may contain your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack account may be compromised.

```
clt = client.AcsClient(<yourRegionID>, <yourAccessKeyID>, <yourAccessKeySecret>)
```

In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret.

#### 4.2.3 Set HTTPS requests

The Python SDK supports using HTTP and HTTPS to initiate API requests. When using the Python SDK, you can specify a protocol (HTTP or HTTPS) for a specific request to use, or set a global default protocol for all requests to use. The default protocol (HTTP or HTTPS) of a product takes precedence over the global default protocol you set. SDK for Python Add OpenSSL dependency HTTPS of the Python SDK depends on the OpenSSL support in Python. To use Alibaba Cloud SDK to send HTTPS requests, you must add OpenSSL support in Python. Run the `python -c "import ssl"` command to check if the Python environment supports OpenSSL. If the `ImportError: No module named ssl` error message does not appear, OpenSSL is supported in Python. If Python does not support OpenSSL, run the following command to install OpenSSL:

```
pip install pyopenssl
```

Set HTTP/HTTPS for a request See the following code example for reference to set the HTTPS call for an API:

```bash
request = CreateInstanceRequest.CreateInstanceRequest() request.set_protocol_type("https")
# Value: "https" or "http"
```

Set global default protocol for all requests See the following code example for reference to set the global default protocol for all requests:

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request.
```

#### 4.2.4 Initiate a request

This topic describes how to use ApsaraDB for MongoDB SDK for Python to initiate a request. The DescribeAccounts operation is used in the example. Procedure
1. Import ApsaraDB for MongoDB SDK for Python.

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential from aliyunsdkdds.request.v20151201.DescribeAccountsRequest import DescribeAccountsRequ est
```

2. Create an ACS client.
SDK for Python The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret.

```
credentials = AccessKeyCredential('<yourAccessKeyID>', '<yourAccessKeySecret>') client = AcsClient(region_id='<yourRegionID>', credential=credentials)
```

3. Create a request object.
<yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID.

```
request = DescribeAccountsRequest() request.set_accept_format('json') request.set_DBInstanceId("<yourDBInstanceId>")
```

4. Initiate the request and process the response.

```python
response = client.do_action_with_exception(request)
# python2:  print response
print(str(response, encoding='utf-8'))
```

#### 4.2.5 Handle errors

If an error occurs on the server side or SDK side when you use the Python SDK, the Python SDK returns the corresponding exception message. An exception message contains the detailed error information, namely the error code and the error message. Generally, you are not required to handle the errors returned by the Python SDK. You are only required to handle the errors on the server side according to the error message. `ServerException` is the error message on the server side. `ClientException` is the error message on the SDK side. For example, if the following error occurs, modify the ID of AccessKey according to the detailed error message.

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAcce ssKeyId.NotFound Specified access key is not found.
```

To handle the errors returned by the Python SDK, see the following code example for reference:

```bash
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
    # Add your own error handling logic here.
    # For example, print the detailed error message.
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

SDK for Go

## 5 Call examples for SDK for Go

### 5.1 Getting started

This topic describes how to obtain and use ApsaraDB for MongoDB SDK for Go. Environment requirements An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. Install the core library of Apsara Stack SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core library of Apsara Stack SDK for Go:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

Use ApsaraDB for MongoDB SDK for Go The following code provides an example on how to use ApsaraDB for MongoDB SDK for Go.
1. Initialize a client instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exceptions.
In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID. SDK for Go

```java
package main import (
    "fmt"
      dds "github.com/aliyun/alibaba-cloud-sdk-go/services/dds"
```

`)`

```
func main() {
    client, err := dds.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<
yourAccessKeySecret>")
    request := dds.CreateDescribeAccountsRequest()
    request.Scheme = "https"
    request.DBInstanceId = "<yourDBInstanceId>"
    response, err := client.DescribeAccounts(request)
    if err != nil {
        fmt.Print(err.Error())
```

`}`

```
    fmt.Printf("response is %#v\n", response)
```

`}`
4. (Optional) Switch to HTTP or HTTPS.

```
request.Scheme = "HTTPS"
```

### 5.2 Use SDK

#### 5.2.1 Install Go SDK

This topic describes how to install the Go SDK. The Alibaba Cloud Go SDK supports Go 1.7 or later versions. Install the Go SDK manually.
1. Download the source code of the Go SDK from the official site of Apsara Stack.
2. Extract the package to the directory where the GO_PATH file of the current user resides.

#### 5.2.2 Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you can use an AccessKey pair for identity verification. Apsara Stack SDK for Go supports identity verification based on AccessKey pairs. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you use an AccessKey pair to access Apsara Stack, you must configure your credential when initializing the client. Not ice Do not disclose any code that may contain your AccessKey pair. For example, your AccessKey pair may become disclosed if you commit your code to a public GitHub project, which could compromise your Alibaba Cloud account.

```
client, err := dds.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<yourAcce ssKeySecret>")
```

SDK for Go In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret.

#### 5.2.3 Initiate a request

This topic describes how to use ApsaraDB for MongoDB SDK for Go to initiate a request. Use ApsaraDB for MongoDB SDK for Go to initiate a request.
1. Import ApsaraDB for MongoDB SDK for Go.

```java
package main import (
    "fmt"
      dds "github.com/aliyun/alibaba-cloud-sdk-go/services/dds"
```

`)`
2. Create a service client that contains all API operations of the service.
You must use actual values to replace the variables in the following sample code. The angle brackets <> are not retained in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID.

```
client, err := dds.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<your AccessKeySecret>")
```

3. Use the `xxx.CreateXXXRequest` method to create a request.
The naming convention for this method is ${service}.Create${apiName}Request . The ${service} part specifies a service name. Service names must use lowercase letters. Example: dds. This value indicates ApsaraDB for MongoDB. The ${apiName} part specifies an API name. Example: DescribeRegions. <yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID.

```
request := dds.CreateDescribeAccountsRequest()
    request.Scheme = "https"
    request.DBInstanceId = "<yourDBInstanceId>"
```

SDK for Go
4. Initiate the request.

```
response, err := client.DescribeAccounts(request)
```

#### 5.2.4 Handle errors

When you use Alibaba Cloud SDK for Go, a `ClientError` or a `ServerError` is returned when an error occurs on the server or SDK side. Both error types are included in `sdk.errors` . The errors conform to the standard Go error interface, so they can be handled in a similar way as standard Go errors. Handle errors You can use the following code to handle the errors:

```
response, err := client.DescribeAccounts(request) if err != nil {
    fmt.Print(err.Error())
```

`}` ClientError If an error occurs in the SDK when you send a request and cannot be automatically handled, the SDK returns a `ClientError` . The following code provides an example on how to determine and obtain the error message in the

```
 ClientError :
```

Not ice When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/dds" // In the package, dds indica
tes ApsaraDB for MongoDB.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Error package that is added.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

```
response, err := Client.DescribeAccounts(request) if clientError, ok := err.(*errors.ClientError); ok{
    // Obtain the error code.
    clientError.ErrorCode()
    // Obtain the error message.
    clientError.Message()
    // Obtain the original error. The return value may be nil.
    clientError.OriginError()
```

`}` SDK for Go ServerError When the server returns an error message, the SDK wraps the message into a `ServerError` and returns it to the client. In this case, you can still obtain the original HTTP response from the response. The following code provides an example on how to determine and obtain the error message in ServerError and Response: Not ice When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/dds" // In the package, dds indica
tes ApsaraDB for MongoDB.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Error package that is added.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

```
response, err := Client.DescribeAccounts(request) if serverError, ok := err.(*errors.ServerError); ok{
    // Obtain the error code.
    serverError.ErrorCode()
    // Obtain the error message.
    serverError.Message()
    // Obtain the original HTTP response.
    response.GetOriginHttpResponse()
```

`}` by function

## 6 List of operations by function

The following tables list API operations available for use in ApsaraDB for MongoDB. Lifecycle management

| Operation | Description |
|---|---|
| CreateDBInstance | Creates and clones an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceSpec | Modifies the specifications or storage capacity of an ApsaraDB for MongoDB standalone or replica set instance. |
| DeleteDBInstance | Releases an ApsaraDB for MongoDB instance. |
| CreateShardingDBInstance | Creates or clones an ApsaraDB for MongoDB sharded cluster instance. |
| CreateNode | Creates a shard or mongos node for an ApsaraDB for MongoDB sharded cluster instance. |
| DeleteNode | Deletes a shard or mongos node in an ApsaraDB for MongoDB sharded cluster instance. |
| ModifyNodeSpec | Modifies the specifications or storage capacity of an ApsaraDB for MongoDB sharded cluster instance. |

Region management

| Operation | Description |
|---|---|
| MigrateToOtherZone | Migrates an ApsaraDB for MongoDB instance to another zone. |
| DescribeRegions | Views the regions and zones that an ApsaraDB for MongoDB instance can be created. |
| MigrateAvailableZone | Changes the zone of an ApsaraDB for MongoDB instance. |

Resource management

| Operation | Description |
|---|---|
| DescribeAvailableResource | Views the instances that can be created in a specified zone. |

Connection management

| Operation | Description |
|---|---|
| AllocatePublicNetworkAddress | Applies for a public endpoint of an ApsaraDB for MongoDB instance. |
| ReleasePublicNetworkAddress | Releases the public endpoint of an ApsaraDB for MongoDB instance. |

| psaraDB for MongoDB | Developer Guide·List of operations |
|---|---|

by function

| Operation | Description |
|---|---|
| ModifyInstanceVpcAuthMode | Enables or disables password-free access to an ApsaraDB for MongoDB instance from the same VPC. |
| DescribeShardingNetworkAddress | Views the connection information of an ApsaraDB for MongoDB sharded cluster instance. |
| ModifyDBInstanceConnectionStrin g | Modifies the connection string of an ApsaraDB for MongoDB instance. |
| ReleaseNodePrivateNetworkAddr ess | Releases the internal endpoint of the shard or Configserver node of a sharded cluster instance. |

Instance information query

| Operation | Description |
|---|---|
| DescribeReplicaSetRole | Views the roles of an ApsaraDB for MongoDB instance and their connection information. |
| DescribeKernelReleaseNotes | Views the release notes of the minor database engine versions of an ApsaraDB for MongoDB instance. |
| DescribeAvailableEngineVersion | Views the database engine versions that an ApsaraDB for MongoDB instance can be upgraded to. |
| DescribeDBInstances | Views the list of ApsaraDB for MongoDB instances. |
| DescribeDBInstanceAttribute | Views the details of an ApsaraDB for MongoDB instance. |
| DescribeRoleZoneInfo | Views the roles and zones of nodes in an ApsaraDB for MongoDB instance. |

Instance management

| Operation | Description |
|---|---|
| RestartDBInstance | Restarts an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceMaintainTime | Modifies the maintenance window of an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceDescription | Changes the name of an ApsaraDB for MongoDB instance. |
| SwitchDBInstanceHA | Switches between the primary and secondary nodes in an ApsaraDB for MongoDB instance. |
| UpgradeDBInstanceEngineVersion | Upgrades the database engine version of an ApsaraDB for MongoDB instance. |
| UpgradeDBInstanceKernelVersion | Upgrades the minor database engine version of an ApsaraDB for MongoDB instance. |

| eveloper Guide·List of operations y function | ApsaraDB for MongoD |
|---|---|

| Operation | Description |
|---|---|
| ModifyDBInstanceNetExpireTime | Extends the retention period of the classic network endpoint of an ApsaraDB for MongoDB instance. |

Account management

| Operation | Description |
|---|---|
| DescribeAccounts | Views the database accounts of an ApsaraDB for MongoDB instance. |
| ResetAccountPassword | Resets the password of the root account of an ApsaraDB for MongoDB instance. |
| ModifyAccountDescription | Modifies the description of the root account of an ApsaraDB for MongoDB instance. |

Whitelists and security groups

| Operation | Description |
|---|---|
| DescribeSecurityGroupConfigurati on | Views the ECS security groups to which an ApsaraDB RDS instance is added. |
| ModifySecurityGroupConfiguratio n | Modifies an ECS security group to which an ApsaraDB RDS instance is added. |
| DescribeSecurityIps | Views the IP whitelists of an ApsaraDB for MongoDB instance. |
| ModifySecurityIps | Modifies an IP whitelist of an ApsaraDB for MongoDB instance. |

Key management

| Operation | Description |
|---|---|
| DescribeDBInstanceTDEInfo | Views whether TDE is enabled for an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceTDE | Modifies the transparent data encryption (TDE) status of an ApsaraDB for MongoDB instance. |

SSL encryption

| Operation | Description |
|---|---|
| ModifyDBInstanceSSL | Modifies the SSL settings of an ApsaraDB for MongoDB instance. |
| DescribeDBInstanceSSL | Views the SSL settings of an ApsaraDB for MongoDB instance. |

Audit logs by function

| Operation | Description |
|---|---|
| DescribeAuditRecords | View the audit log entries of an ApsaraDB for MongoDB instance. |
| DescribeAuditFiles | Views the audit log files of an ApsaraDB for MongoDB instance. |
| DescribeAuditPolicy | Views whether the audit log feature is enabled for an ApsaraDB for MongoDB instance. |
| ModifyAuditLogFilter | Modifies the type of audit log entries that you want to collect for an ApsaraDB for MongoDB instance. |
| DescribeAuditLogFilter | Views the types of audit log entries collected for an ApsaraDB for MongoDB instance. |
| ModifyAuditPolicy | Enables or disables the audit log feature or set the log retention period for an ApsaraDB for MongoDB instance. |

Log management

| Operation | Description |
|---|---|
| DescribeSlowLogRecords | Views the slow query log entries of an ApsaraDB for MongoDB instance. |
| DescribeErrorLogRecords | Views the error log entries of an ApsaraDB for MongoDB instance. |
| DescribeRunningLogRecords | Views the operational log entries of an ApsaraDB for MongoDB instance. |

Performance monitoring management

| Operation | Description |
|---|---|
| DescribeDBInstancePerformance | Views the performance data of an ApsaraDB for MongoDB instance. |
| DescribeDBInstanceMonitor | Views the collection frequency of monitoring data for an ApsaraDB for MongoDB instance. |

Parameter management

| Operation | Description |
|---|---|
| DescribeParameterModificationHi story | Views the modification records of ApsaraDB for MongoDB instance parameters. |
| DescribeParameters | Views parameter configurations of an ApsaraDB for MongoDB instance. |
| ModifyParameters | Modifies the parameters of an AsparaDB for MongoDB instance. |

Backup and recovery by function

| Operation | Description |
|---|---|
| DescribeBackupPolicy | Views the backup policy of an ApsaraDB for MongoDB instance. |
| ModifyBackupPolicy | Modifies the backup policy of an ApsaraDB for MongoDB instance. |
| CreateBackup | Manually backs up an ApsaraDB for MongoDB instance. |
| DescribeBackups | Views the backup sets of an ApsaraDB for MongoDB instance. |
| RestoreDBInstance | Restores data to the current ApsaraDB for MongoDB instance. |
| DescribeBackupDBs | Views the databases at a specified point in time or the databases in a specified backup set before you restore a database for an ApsaraDB for MongoDB instance. |

## 7 API Reference

### 7.1 Lifecycle management

#### 7.1.1 CreateDBInstance

Creates or clones an ApsaraDB for MongoDB replica set instance. For more information about instance types, see Inst ance t ypes in ApsaraDB f or MongoDB Product Int roduct ion. To create sharded cluster instances, you can call the Creat eShardingDBInst ance operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDBInstance | The operation that you want to perform. Set the value to Creat eDBInst ance. |
| ClientToken | String | Yes | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value. You must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Engine | String | Yes | MongoDB | The database engine of the instance. Set the value to MongoDB. |
| EngineVersion | String | Yes | 4.0 | The database engine version of the instance. Valid values: 3.2, 3.4, 4.0, and 4.2. Not e To call this operation to clone an instance, set this value to the database engine version of the source instance. |
| DBInstanceClass | String | Yes | dds.mongo.stan dard | The instance type. For more information, see Inst ance t ypes in ApsaraDB f or MongoDB Product Int roduct ion. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceStorag e | Integer | Yes | 10 | The storage space of the instance. Valid values: 10 to 3000. Unit: GB. The value must be a multiple of 10. Not e The values that can be specified for this parameter are subject to the instance types. For more information, see Inst ance t ypes in ApsaraDB f or MongoDB Product Int roduct ion. |
| ZoneId | String | No | cn-hangzhou-b | The zone ID of the instance. You can call the DescribeRegions operation to query the most recent zone list. |
| DBInstanceDescri ption | String | No | Test database 1 | The name of the instance. It must be 2 to 256 characters in length and can contain digits, letters, underscores ( ), _ and hyphens (-). It must start with a letter. |
| SecurityIPList | String | No | 10.23.12.24/24 | The whitelist that contains the IP addresses that are allowed to access the instance. Separate multiple IP addresses with commas (,). Each IP address must be unique. A maximum of 1,000 IP addresses can be added. You can enter IP addresses such as 10.23.12.24 and CIDR blocks such as 10.23.12.24/24. /24 indicates that the prefix of the CIDR block is 24-bit long. You can replace 24 with a value within the range of 1 to 32. You can also enter the percent sign (%) or 0.0.0.0/0. Not e If you enter the percent sign (%) or 0.0.0.0/0, all IP addresses can access the instance. This may introduce security risks to the instance. Proceed with caution. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccountPassword | String | No | Alitest!159 | The password of the root account. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include !#$%^&amp;*() +-= _ The password must be 8 to 32 characters in length. |
| ChargeType | String | No | PrePaid | The billing method of the instance. Valid values: Post Paid: pay-as-you-go PrePaid: subscription Default value: pay-as-you-go Not e If you set this parameter to PrePaid, you must also specify the Period parameter. |
| Period | Integer | No | 1 | The subscription period of the instance. Unit: months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, and 36. Not e This parameter is valid and required only if you set the ChargeT ype parameter to PrePaid. |
| NetworkType | String | No | VPC | The network type of the instance. Valid values: classic vpc Default value: classic. Not e If you set this parameter to vpc, you must also specify the VpcId and VSwit chId parameters. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpcId | String | No | vpc-bpxxxxxxxx | The ID of the virtual private cloud (VPC). Not e This parameter is valid only if you set the Net workT ype parameter to VPC. |
| VSwitchId | String | No | vsw-bpxxxxxxxx | The ID of the vSwitch. Not e This parameter is valid only if you set the Net workT ype parameter to VPC. |
| SrcDBInstanceId | String | No | dds-bpxxxxxxxx | The ID of the source instance. This parameter can be specified only when this operation is called to clone instances. You must also specify the BackupId parameter or Rest oreT ime parameter. |
| BackupId | String | No | 32994xxxx | The ID of the backup set. This parameter can be specified only when this operation is called to clone instances. You must also specify the SrcDBInst anceId parameter. Not e You can call the DescribeBackups operation to query the backup ID. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RestoreTime | String | No | 2019-03- 13T12:11:14Z | The point in time to clone the instance. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. Not e This parameter can be specified only when this operation is called to clone instances. You must also specify the SrcDBInst anceId and BackupId parameters. You can set this parameter to a point in time in the last seven days. |
| BusinessInfo | String | No | {“ActivityId":"00 0000000"} | The business information. This is an additional parameter. |
| CouponNo | String | No | youhuiquan pro _ motion option id _ _ for blank _ _ | The coupon code. Default value: youhuiquan promot ion opt ion id _ _ _ _ f or blank. _ |
| AutoRenew | String | No | true | Specifies whether to enable auto- renewal for the instance. Valid values: t rue: enables auto-renewal. f alse: disables auto-renewal. You must manually renew the instance. Default value: false. Not e This parameter is valid only if you set the ChargeType parameter to PrePaid. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DatabaseNames | String | No | mongodbtest | The names of the databases. Not e When you call this operation to clone an instance, you can set the databases that are specified by this parameter for cloning. Otherwise, all databases of the instance are cloned. |
| StorageEngine | String | No | WiredTiger | The storage engine of the instance. Set the value to WiredT iger. Not e If you do not specify this parameter, WiredT iger is used. |
| ReplicationFactor | String | No | 3 | The number of nodes in the replica set instance. Valid values: 3, 5, and 7. Default value: 3. |
| ReadonlyReplicas | String | No | 1 | The number of read-only nodes. Valid values: 1 t o 5. Not e By default, this parameter is not specified and no read-only nodes are created. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |
| OrderId | String | 2033xxxxxxxxxxxx | The ID of the order. |

| psaraDB for Mong | oDB |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D8F1D721-6439- 4257-A89C- F1E8E9C9624D | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/?Action=CreateDBInstance &ClientToken=ETnLKlblzczshOTUbOCzxxxxxxxxxx &Engine=MongoDB &EngineVersion=4.0 &DBInstanceClass=dds.mongo.standard &DBInstanceStorage=10 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateDBInstanceResponse>
      <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId>
      <OrderId>2033xxxxxxxxxxxx</OrderId>
      <RequestId>D8F1D721-6439-4257-A89C-F1E8E9C9624D</RequestId>
</CreateDBInstanceResponse>
```

`JSON` format `{`

```json
    "DBInstanceId": "dds-bpxxxxxxxx",
    "OrderId": "2033xxxxxxxxxxxx",
    "RequestId": "D8F1D721-6439-4257-A89C-F1E8E9C9624D"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InsufficientBalance | Your account does not have enough balance. | The error message returned because you do not have sufficient balance within your account. Add funds to your account and try again. |
| 403 | RealNameAuthentica tionError | Your account has not passed the real-name authentication yet. | The error message returned because the specified user has not completed real-name verification. Complete real-name verification and try again. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidCapacity.NotF ound | The Capacity provided does not exist in our records. | The error message returned because the configured space is invalid. Check the specified parameter. |
| 400 | IdempotentParamet erMismatch | Request uses a client token in a previous request but is not identical to that request. | The error message returned because the two specified requests use the same ClientToken value. |

#### 7.1.2 ModifyDBInstanceSpec

Modifies the specifications or storage capacity of an ApsaraDB for MongoDB replica set instance. This operation is applicable to replica set instances. You can call the Modif yNodeSpec, Creat eNode, or Delet eNode operation to change the configurations of a sharded cluster instance. When you call this operation, you must configure the `x-acs-organizationid` , `x-acs-resourcegrou` `pid` , and `x-acs-instanceid` header parameters to specify the organization ID, resource group ID, and instance ID. Otherwise, the call is directed to the root resource set and organization. For more information about the code, see SDK description in ApsaraDB for MongoDB Developer Guide. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance Spec | The operation that you want to perform. Set the value to Modif yDBInst anceSpec. |
| DBInstanceId | String | Yes | dds- d1n4eab47879*** * | The ID of the instance. |
| RegionId | String | No | cn-qd- agility14**** | The region ID of the instance. Not e You can call the DescribeDBInst anceAt t ribut e operation to query the region ID of the instance. |

| Parameter | Type | Required | Example | Description |   |   |   |
|---|---|---|---|---|---|---|---|
| DBInstanceClass | String | No | dds.mongo.stan dard | The instance type. Not e For more information, see I nstance types in ApsaraDB for MongoDB Product Intro duction. You must specify either this parameter or the DB InstanceStorage parameter. |   |   |   |
|   |   |   |   |   | DB |   |   |
| DBInstanceStorag e | String | No | 50 | The storage space of the instance. Valid values: 10 to 3000. The value must be a multiple of 10. Unit: GB. Not e The values that can be specified for this parameter are subject to the instance types. For more information, see Inst ance types in ApsaraDB for MongoDB Product Introduc tion. You must specify either this parameter or the DB InstanceClass parameter. Storage capacity can be scaled down only on subscription replica set instances. The new storage capacity you specify must be greater than the used storage space. |   |   |   |

| DB |   |   |
|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| OrderType | String | No | UPGRADE | The type of the change. Valid values: UPGRADE: upgrades the configurations of an instance. DOWNGRADE: downgrades the configurations of an instance. Default value: DOWNGRADE. Not e This parameter is required when the ChargeType parameter is set to Post Paid. |
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment. Valid values: t rue: enables automatic payment. Make sure that you have sufficient balance within your account. f alse: disables automatic payment. Default value: t rue. |
| BusinessInfo | String | No | {“ActivityId":"00 0000000"} | The business information. |
| ReplicationFactor | String | No | 3 | The number of nodes in the instance. Valid values for replica set instances: 3, 5, and 7. Valid values for standalone instances: 1. |
| ReadonlyReplicas | String | No | 1 | The number of read-only nodes. Valid values: 1 to 5. |
| CouponNo | String | No | youhuiquan pro _ motion option id _ _ for blank _ _ | The coupon code. Default value: youhuiquan promot ion opt ion id _ _ _ _ f or blank. _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EffectiveTime | String | No | Immediately | The time when the new configurations take effect. Valid values: Immediat ely: The new configurations immediately take effect. Maint ainT ime: The new configurations take effect during the maintenance window of the instance. Default value: Immediat ely. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 20331066**** | The order ID of the instance. |
| RequestId | String | C5662998-62BE- 4C7F-961D- 7DFE775D**** | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/?Action=ModifyDBInstanceSpec &DBInstanceId=dds-d1n4eab47879**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceSpecResponse>
  <RequestId>C5662998-62BE-4C7F-961D-7DFE775D****</RequestId>
  <OrderId>20331066****</OrderId>
</ModifyDBInstanceSpecResponse>
```

`JSON` format `{`

```json
  "RequestId": "C5662998-62BE-4C7F-961D-7DFE775D****",
  "OrderId": "20331066****"
```

`}`

#### 7.1.3 DeleteDBInstance

Releases an ApsaraDB for MongoDB instance. The instance must be in the Running state when you call this operation. After an instance is released, all the data in the instance is deleted and cannot be restored. Proceed with caution. When you call this operation, you must configure the `x-acs-organizationid` , `x-acs-resourcegrou` `pid` , and `x-acs-instanceid` header parameters to specify the organization ID, resource group ID, and instance ID. Otherwise, the call is directed to the root resource group and organization. For more information about the code, see SDK Description in ApsaraDB for MongoDB Developer Guide. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDBInstance | The operation that you want to perform. Set the value toDelet eDBInst ance. |
| DBInstanceId | String | Yes | dds- d1n4eab47879*** * | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCz**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 72651AF9-7897- 41A7-8B67- 6C15C7F2**** | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/?Action=DeleteDBInstance &DBInstanceId=dds-d1n4eab47879**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteDBInstanceResponse>
  <RequestId>72651AF9-7897-41A7-8B67-6C15C7F2****</RequestId>
</DeleteDBInstanceResponse>
```

`JSON` format `{`

```json
  "RequestId": "72651AF9-7897-41A7-8B67-6C15C7F2****"
```

`}`

#### 7.1.4 CreateShardingDBInstance

Creates or clones an ApsaraDB for MongoDB sharded cluster instance. When you call this operation, you must configure the `x-acs-organizationid` , `x-acs-` `resourcegroupid` , and `x-acs-instanceid` header parameters to specify the organization ID, resource group ID, and instance ID. Otherwise, the call is directed to the root resource set and organization. For more information about the code, see SDK description in ApsaraDB for MongoDB Developer Guide. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateShardingDB Instance | The operation that you want to perform. Set the value to Creat eShardingDBInst ance. |
| AccountPassword | String | Yes | Alitest**** | The password of the root account. The encoding format must comply with the following rules: The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password can contain the following special characters: !#$%^&amp;*() +-= _ The password must be 8 to 32 characters in length. |
| Engine | String | Yes | MongoDB | The database engine of the instance. Set the value to MongoDB. |

| D | eveloper Guide·API | Reference |   |   | ApsaraDB for MongoD | B |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EngineVersion | String | Yes | 4.0 | The database engine version of the instance. Valid values: 3.0, 3.4, 4.0, and 4.2. Not e If you call this operation to clone an instance, set the value to the database engine of the source instance. |
| RegionId | String | Yes | cn-qd- agility14**** | The region ID of the instance. Not e You can call the DescribeRegions operation to query the available regions. |
| ZoneId | String | No | cn-qd-agility14- amtest110**** | The zone ID of the instance. Not e You can call the DescribeRegions operation to query available zones. |
| Mongos.N.Class | String | No | dds.mongos.stan dard | The specifications of the mongos node. For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. N specifies the serial number of the mongos node for which the specification is specified. For example, Mongos.1.Class specifies the specification of the first mongos node. Mongos.2.Class specifies the specification of the second mongos node. Not e You can configure the specifications of 2 to 32 mongos nodes. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ReplicaSet.N.Clas s | String | No | dds.shard.standa rd | The specifications of the shard node. For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. N specifies the serial number of the shard node for which the specification is specified. For example, ReplicaSet .1.Class specifies the specification of the first shard node. ReplicaSet .2.Class specifies the specification of the second shard node. Not e You can specify the specifications of 2 to 32 shard nodes. |
| ReplicaSet.N.Stor age | Integer | No | 20 | The storage capacity of the shard node. Valid values: 10 to 2000. The value must be a multiple of 10. Unit: GB. The values that can be specified for this parameter are subject to the instance types. For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. N specifies the serial number of the shard node for which storage capacity is specified. For example, ReplicaSet .1.St orage specifies the storage capacity of the first shard. ReplicaSet .2.St orage specifies the storage capacity of the second shard. |
| ConfigServer.N.Cl ass | String | No | dds.cs.mid | The specifications of the Conf igserver node. Valid value: dds.cs.mid. Not e The specifications of the config server are fixed at 1 core and 2 GB memory. The value of N is fixed at 1. For example, set the value of ConfigServer.1.Class parameter to dds.cs.mid. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ConfigServer.N.St orage | Integer | No | 20 | The storage capacity of a Conf igserver node. Set the value to 20. Not e The storage capacity is fixed as 20 GB. For example, set the value of ConfigServer.1.Storage parameter to 20. |
| DBInstanceDescri ption | String | No | Testdatabase1 | The name of the instance. The name must comply with the following naming conventions: The name must start with a letter, and can contain digits, letters, underscores ( ), and hyphens (-). _ The name must be 2 to 256 characters in length, |
| SecurityIPList | String | No | 10.23.12.24/24 | The whitelist that contains the IP addresses that are allowed to access the instance. Separate multiple IP addresses with commas (,). Each IP address must be unique. A maximum of 1,000 IP addresses can be added. You can enter IP addresses such as 10.23.12.24 and Classless Inter- Domain Routing (CIDR) blocks such as 10.23.12.24/24. /24 indicates the length of the CIDR block prefix. The prefix can be 1 to 32 bits in length. You can also enter the percent sign (%) or 0.0.0.0/0. Not e If you enter the percent sign (%) or 0.0.0.0/0, all IP addresses can access the instance. This may introduce security risks to the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ChargeType | String | No | PrePaid | The billing method of the instance. Valid values: Post paid: pay-as-you-go Prepaid: subscription Default value: Post Paid. Not e If you specify this parameter to PrePaid, you must also specify the Period parameter. |
| Period | Integer | No | 1 | The subscription period of the instance. Unit: months. Valid values: 1 to 9, 12, 24, and 36. Not e This parameter takes effect only when you set the ChargeType parameter to PrePaid. |
| NetworkType | String | No | Classic | The type of network in which the instance resides. Default value: standard. Valid values: Classic VPC Default value: Classic. Not e If you set the value to VPC, you must specify the VpcId and VSwitchId parameters. |
| VpcId | String | No | vpc- bp1q2qqm4vxo6 e6zl**** | The ID of the VPC. Not e This parameter is required when the NetworkType parameter is set to VPC. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VSwitchId | String | No | vsw- bp1buy0h9myt5i 9e7**** | The ID of the vSwitch. Not e This parameter is required when the NetworkType parameter is set to VPC. |
| SrcDBInstanceId | String | No | dds- bp1b47357f21*** * | The ID of the source instance. Not e This parameter is required only when this operation is called to clone instances. If you set this parameter, you must also specify the RestoreTime parameter. |
| RestoreTime | String | No | 2019-03- 08T02:30:25Z | The point in time to which you want the cloned instance to restore. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Not e This parameter is required only when this operation is called to clone instances. If you set this parameter, you must also specify the SrcDBInstanceId parameter. You can set this parameter to any point in time in the last seven days. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | ETnLKlblzczshOT UbOCz**** | The client token that is used to ensure the idempotency of requests. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| StorageEngine | String | No | WiredTiger | The storage engine of the database. Only WiredT iger is supported. |
| AutoRenew | String | No | false | Specifies whether to enable automatic renewal for the instance. Valid values: t rue: enables automatic renewal. f alse: disables automatic renewal. You must renew the instance manually. Default value: f alse. Not e This parameter is required when the ChargeType parameter is set to PrePaid. |
| ResourceGroupId | String | No | rg- acfm22cdcgc**** | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | dds- bp14ed961586**** | The ID of the instance. |
| OrderId | String | 20331066**** | The order ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D8F1D721-6439- 4257-A89C- F1E8E9C9**** | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/?Action=CreateShardingDBInstance &AccountPassword=Alitest**** &Engine=MongoDB &EngineVersion=4.0 &RegionId=cn-qd-agility14**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateShardingDBInstanceResponse>
  <RequestId>D8F1D721-6439-4257-A89C-F1E8E9C9****</RequestId>
  <DBInstanceId>dds-bp14ed961586****</DBInstanceId>
  <OrderId>20331066****</OrderId>
</CreateShardingDBInstanceResponse>
```

`JSON` format `{`

```json
  "RequestId": "D8F1D721-6439-4257-A89C-F1E8E9C9****",
  "DBInstanceId": "dds-bp14ed961586****",
  "OrderId": "20331066****"
```

`}`

#### 7.1.5 CreateNode

You can call this operation to create the shard or mongos node for an ApsaraDB for MongoDB sharded cluster instances. This operation is applicable only to sharded cluster instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateNode | The operation that you want to perform. Set the value to Creat eNode. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NodeClass | String | Yes | dds.shard.mid | The specification of the shard or mongos node. For more information, see Instance types. |
| NodeType | String | Yes | shard | The type of the node. Valid values: shard mongos |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the sharded cluster instance. |
| NodeStorage | Integer | No | 10 | The storage capacity of the node. You must specify this parameter if you set the NodeT ype parameter to shard. Valid values: 10 to 2000. Unit: GB. The value must be a multiple of 10 GB. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| FromApp | String | No | OpenApi | The source of the request. Valid values: OpenApi: the ApsaraDB for MongoDB API mongo buy: the ApsaraDB for _ MongoDB console |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment for the instance. Valid values: t rue: enables automatic payment. Make sure that your account has sufficient balance. f alse: disables automatic payment. You must perform the following operations to pay for the instance: Log on to the ApsaraDB for MongoDB console. In the top navigation bar, click Expenses. The Billing Management page appears. In the left-side navigation pane, click Bills. On the Unpaid tab, click Make a Payment in the Actions column for the bill that you want to pay. Default value: t rue. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NodeId | String | d-bpxxxxxxxxxxxxxx | The ID of the node. |
| OrderId | String | 2034xxxxxxxx | The ID of the order. |
| RequestId | String | 7D48FB19-20CA- 4725-A870- 3D8F5CE69F14 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=CreateNode &NodeClass=dds.shard.mid &NodeType=shard &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateNodeResponse>
   <OrderId>2034xxxxxxxx</OrderId>
   <RequestId>7D48FB19-20CA-4725-A870-3D8F5CE69F14</RequestId>
</CreateNodeResponse>
```

`JSON` format `{`

```json
 "OrderId": "2034xxxxxxxx",
 "RequestId": "7D48FB19-20CA-4725-A870-3D8F5CE69F14"
```

`}`

#### 7.1.6 DeleteNode

You can call this operation to delete a shard or mongos in an ApsaraDB for MongoDB sharded cluster instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. A sharded cluster instance is used. The number of shard or mongos nodes in the instance must be greater than two. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteNode | The operation that you want to perform. Set the value to Delet eNode. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeId | String | Yes | s-bpxxxxxxxx | The ID of the shard or mongos node to be deleted. You can call the DescribeDBInstanceAttribute operation to view the ID. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 2033xxxxxxxxxxxx | The ID of the order. |
| RequestId | String | 9F9BDE64-BF30- 41F3-BD29- C19CE4AB3404 | The ID of the request. |
| TaskId | Integer | 111111111 | The ID of the task. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DeleteNode &NodeId=s-bpxxxxxxxx &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteNodeResponse>
   <RequestId>9F9BDE64-BF30-41F3-BD29-C19CE4AB3404</RequestId>
   <TaskId>111111111</TaskId>
</DeleteNodeResponse>
```

`JSON` format `{`

```json
    "RequestId": "9F9BDE64-BF30-41F3-BD29-C19CE4AB3404",
    "TaskId": 111111111
```

`}`

#### 7.1.7 ModifyNodeSpec

You can call this operation to modify the specifications and storage capacity of the nodes in an ApsaraDB for MongoDB sharded cluster instance. This operation is applicable only to sharded cluster instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNodeSpec | The operation that you want to perform. Set the value to Modif yNodeSpec. |
| NodeId | String | Yes | d-bpxxxxxxxx | The ID of the shard or mongos node in the sharded cluster instance. You can call the DescribeDBInst anceAt t ribut e operation to view the ID. Not e If you set this parameter to the ID of a shard, you must also specify the NodeSt orage parameter. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeClass | String | No | dds.shard.standa rd | The specifications of the mongos node. For more information, see Inst ance t ypes in ApsaraDB for MongoDB Product Introduction. Not e You must specify this parameter or the NodeSt orage parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NodeStorage | Integer | No | 20 | The storage capacity for the shard node. Valid values: 10 to 2000. Unit: GB. The value must be a multiple of 10 GB. Not e You must specify this parameter or the NodeClass parameter. This parameter is valid only if you set the NodeId parameter to the ID of a shard. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment for the instance. Valid values: t rue: enables automatic payment. Make sure that your account has sufficient balance. f alse: disables automatic payment. You must perform the following operations to pay for the instance: Log on to the ApsaraDB for MongoDB console. In the top navigation bar, click Expenses. The Billing Management page appears. In the left-side navigation pane, click Bills. On the Unpaid tab, click Make a Payment in the Actions column for the bill that you want to pay. Default value: t rue. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EffectiveTime | String | No | Immediately | The time when the new settings take effect. Valid values: Immediat ely: The settings take effect immediately. Maint ainT ime: The settings take effect during the maintenance period of the instance. Default value: Immediat ely. |
| FromApp | String | No | OpenApi | The source of the request. Valid values: OpenApi: the ApsaraDB for MongoDB API mongo buy: the ApsaraDB for _ MongoDB console |
| OrderType | String | No | UPGRADE | The type of the order. Valid values: UPGRADE DOWNGRADE |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 2033xxxxxxxxx | The ID of the order. |
| RequestId | String | EFFC5788-8BB5- 41B5-9F15- 9CFC5A0E8FCC | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.aliyuncs.com/? Action=ModifyNodeSpec &NodeId=d-bpxxxxxxxx &DBInstanceId=dds-bpxxxxxxxx &NodeClass=dds.shard.standard &NodeStorage=20 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyNodeSpecResponse>
   <OrderId>2033xxxxxxxxx</OrderId>
   <RequestId>EFFC5788-8BB5-41B5-9F15-9CFC5A0E8FCC</RequestId>
</ModifyNodeSpecResponse>
```

`JSON` format `{`

```json
    "OrderId": "2033xxxxxxxx",
    "RequestId": "EFFC5788-8BB5-41B5-9F15-9CFC5A0E8FCC"
```

`}`

### 7.2 Region management

#### 7.2.1 MigrateToOtherZone

You can call this operation to migrate an ApsaraDB for MongoDB instance to another zone. This operation is applicable only to replica set instances, but not to sharded cluster instances. If you have applied for a public endpoint of the instance, you must first call the ReleasePublicNet workAddress operation to release the public endpoint. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | MigrateToOtherZ one | The operation that you want to perform. Set the value to Migrat eT oOt herZone. |
| InstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e You must specify the Vswit ch parameter if the network type of the instance is VPC. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ZoneId | String | Yes | cn-hangzhou-b | The ID of the destination zone to which you want to migrate the MongoDB instance. Not e The destination and source zones are in the same region. You can call the DescribeRegions operation to query the zone IDs. |
| EffectiveTime | String | No | Immediately | The time when the instance is migrated to the destination zone. Valid values: Immediat ely Maint ainT ime: The instance will be migrated during the maintenance period of the instance. Default value: Immediat ely. |
| VSwitchId | String | No | vsw-bpxxxxxxxx | The ID of the vSwitch in the destination zone. Not e This parameter can be used only when the network type of the instance is VPC. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252- 4A4A-ADDA- 5CB1BF63873D | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=MigrateToOtherZone &DBInstanceId=dds-bpxxxxxxxx &ZoneId=cn-hangzhou-b &EffectiveTime=Immediately &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>0FDDC511-7252-4A4A-ADDA-5CB1BF63873D</RequestId>
```

`JSON` format `{`

```json
 "RequestId": "0FDDC511-7252-4A4A-ADDA-5CB1BF63873D"
```

`}`

#### 7.2.2 DescribeRegions

You can call this operation to view the regions and zones that an ApsaraDB for MongoDB instance can be created. Before you call the CreateDBInstance or CreateShardingDBInstance operation to create an instance, you must call this operation to view the regions and zones that the that ApsaraDB for MongoDB instance can be created. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of DdsRegion |   | An array that consists of the information of regions. |
| DdsRegion |   |   |   |
| RegionId | String | cn-qingdao | The ID of the region. |

| psaraDB for Mong | oDB |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Zones | Array of Zone |   | An array that consists of the information of zones. |
| Zone |   |   |   |
| VpcEnabled | Boolean | true | Indicates whether VPC is supported. Valid values: t rue f alse |
| ZoneId | String | cn-hangzhou-b | The ID of the zone. |
| RequestId | String | 4E46C22C-D3B7- 4DB8-9C76- 63851BE68E20 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeRegions &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRegionsResponse>
   <RequestId>4E46C22C-D3B7-4DB8-9C76-63851BE68E20</RequestId>
   <Regions>
      <DdsRegion>
         <RegionId>cn-hangzhou</RegionId>
         <Zones>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-i</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-b</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-d</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-f</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-MAZ5(b,e,f)</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-g</ZoneId>
            </Zone>
         </Zones>
      </DdsRegion>
   </Regions>
</DescribeRegionsResponse>
```

`JSON` format `{`

```json
 "RequestId": "4E46C22C-D3B7-4DB8-9C76-63851BE68E20",
 "Regions": {
  "DdsRegion": [
```

`{`

```json
    "RegionId": "cn-hangzhou",
    "Zones": {
     "Zone": [
```

`{`

```json
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-i"
```

`},` `{`

```json
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-b"
```

`},` `{`

```json
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-d"
```

`},` `{`

```json
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-f"
```

`},` `{`

```json
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-MAZ5(b,e,f)"
```

`},` `{`

```json
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-g"
```

`}` `]` `}` `}` `]` `}` `}`

#### 7.2.3 MigrateAvailableZone

You can call this operation to change the zone of an ApsaraDB for MongoDB instance. This operation is applicable only to replica set instances, but not to sharded cluster instances. If you have applied for a public endpoint of the instance, you must first call ReleasePublicNet workAddress to release the public endpoint. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | MigrateAvailable Zone | The operation that you want to perform. Set the value to Migrat eAvailableZone. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e You must specify the Vswit ch parameter if the network type of the instance is VPC. |
| ZoneId | String | Yes | cn-hangzhou-b | The ID of the destination zone to which you want to migrate the ApsaraDB for MongoDB instance. Not e The destination zone must be in the same region as the current zone of the instance. You can call the DescribeRegions operation to view the zone IDs. |
| Vswitch | String | No | vsw-bpxxxxxxxx | The ID of the vSwitch in the destination zone. Not e This parameter can be used only when the network type of the instance is VPC. |
| EffectiveTime | String | No | Immediately | The time when the instance is migrated to the destination zone. Valid values: Immediat ely: The instance will be migrated immediately. Maint ainT ime: The instance will be migrated during the maintenance period of the instance. Default value: Immediat ely. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252- 4A4A-ADDA- 5CB1BF63873D | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=MigrateAvailableZone &DBInstanceId=dds-bpxxxxxxxx &ZoneId=cn-hangzhou-b &EffectiveTime=Immediately &<Common request parameters>
```

Sample success responses `XML` format

```xml
<MigrateAvailableZoneResponse>
   <RequestId>0FDDC511-7252-4A4A-ADDA-5CB1BF63873D</RequestId>
</MigrateAvailableZoneResponse>
```

`JSON` format `{`

```json
 "RequestId": "0FDDC511-7252-4A4A-ADDA-5CB1BF63873D"
```

`}`

### 7.3 Resource management

#### 7.3.1 DescribeAvailableResource

You can call this operation to view the ApsaraDB for MongoDB instances that can be created in a specified zone. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAvailable Resource | The operation that you want to perform. Set the value to DescribeAvailableResource. |
| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to view the region IDs. |

| D | eveloper Guide·API | Reference |   |   | ApsaraDB for MongoD | B |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ZoneId | String | No | cn-hangzhou-h | The zone ID of the instance. You can call the DescribeRegions operation to view the zone IDs. |
| InstanceChargeTy pe | String | No | PrePaid | The billing method. Valid values: PrePaid: subscription. PostPaid: pay-as-you-go. Not e Default value: PrePaid. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 344EE51D-8850- 4935-B68B- 58A8F4DCE3BD | The ID of the request. |
| SupportedDBTy pes | Array of SupportedDBTy pe |   | The database type supported. |
| SupportedDBTy pe |   |   |   |
| AvailableZones | Array of AvailableZone |   | The zone ID of the instance. |
| AvailableZone |   |   |   |
| RegionId | String | cn-hangzhou | The region ID of the instance. |
| SupportedEngi neVersions | Array of SupportedEngi neVersion |   | The versions of the storage engine. |
| SupportedEngi neVersion |   |   |   |
| SupportedEngi nes | Array of SupportedEngi ne |   | The storage engine supported. |
| SupportedEngi ne |   |   |   |

| A | psaraDB for Mong | oDB |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | WiredTiger | The storage engine of the instance. |
| SupportedNod eTypes | Array of SupportedNod eType |   | The instance types supported. |
| SupportedNod eType |   |   |   |
| AvailableResour ces | Array of AvailableResour ce |   | The details of available resources. |
| AvailableResour ce |   |   |   |
| InstanceClass | String | dds.mongo.2xlarge | The category of the instance. |
| InstanceClassRe mark | String | 8 vCPUs, 32 GiB (maximum connections: 8000 IOPS: 14000) | The instance type. |
| NetworkTypes | String | VPC | The network type of the instance. |
| NodeType | String | 3 | The number of nodes in the instance. |
| Version | String | 4.0 | The database engine version of the instance. |
| ZoneId | String | cn-hangzhou-h | The zone ID of the instance. |
| DbType | String | sharding | The database engine of the instance. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAvailableResource &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>344EE51D-8850-4935-B68B-58A8F4DCE3BD</RequestId> <SupportedDBTypes>
    <DbType>sharding</DbType>
</SupportedDBTypes> <SupportedDBTypes>
    <AvailableZones>
        <ZoneId>cn-hangzhou-h</ZoneId>
        <RegionId>cn-hangzhou</RegionId>
    </AvailableZones>
    <AvailableZones>
        <SupportedEngineVersions>
            <Version>4.0</Version>
        </SupportedEngineVersions>
        <SupportedEngineVersions>
            <SupportedEngines>
                <Engine>WiredTiger</Engine>
            </SupportedEngines>
            <SupportedEngines>
                <SupportedNodeTypes>
                    <NetworkTypes>VPC</NetworkTypes>
                    <NodeType>3</NodeType>
                </SupportedNodeTypes>
                <SupportedNodeTypes>
                    <AvailableResources>
                        <InstanceClassRemark>8 vCPUs, 32 GiB (maximum connections: 8000 IOP
S: 14000)</InstanceClassRemark>
                        <InstanceClass>dds.mongo.2xlarge</InstanceClass>
                    </AvailableResources>
                </SupportedNodeTypes>
            </SupportedEngines>
        </SupportedEngineVersions>
    </AvailableZones>
</SupportedDBTypes>
```

`JSON` format `{`

```json
    "RequestId":"344EE51D-8850-4935-B68B-58A8F4DCE3BD",
    "SupportedDBTypes":[
```

`{`

```json
            "DbType":"sharding"
```

`},` `{`

```json
            "AvailableZones":[
```

`{`

```json
                    "ZoneId":"cn-hangzhou-h",
                    "RegionId":"cn-hangzhou"
```

`},` `{`

```json
                    "SupportedEngineVersions":[
```

`{`

```json
                            "Version":"4.0"
```

`},` `{`

```json
                            "SupportedEngines":[
```

`{`

```json
                                    "Engine":"WiredTiger"
```

`},` `{`

```json
                                    "SupportedNodeTypes":[
```

`{`

```json
                                            "NetworkTypes":"VPC",
                                            "NodeType":"3"
```

`},` `{`

```json
                                            "AvailableResources":[
```

`{`

```json
                                                    "InstanceClassRemark":"8 vCPUs, 32 GiB
(maximum connections: 8000 IOPS: 14000)",
                                                    "InstanceClass":"dds.mongo.2xlarge"
```

`}` `]` `}` `]` `}` `]` `}` `]` `}` `]` `}` `]` `}`

### 7.4 Connection management

#### 7.4.1 AllocatePublicNetworkAddress

You can call this operation to assign a public endpoint to an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocatePublicNet workAddress | The operation that you want to perform. Set the value to Allocat ePublicNet workAddress. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | s-bpxxxxxxxx | The ID of the mongos, shard, or Configserver node in the sharded cluster instance. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. You can call the DescribeDBInstanceAttribut e operation to view the ID of the mongos, shard, or Configserver node. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B6D17591-B48B- 4D31-9CD6- 9B9796B2270A | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.aliyuncs.com/? Action=AllocatePublicNetworkAddress &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AllocatePublicNetworkAddressResponse>
   <RequestId>B6D17591-B48B-4D31-9CD6-9B9796B2270A</RequestId>
</AllocatePublicNetworkAddressResponse>
```

`JSON` format `{`

```json
 "RequestId": "B6D17591-B48B-4D31-9CD6-9B9796B2270A"
```

`}`

#### 7.4.2 ReleasePublicNetworkAddress

You can call this operation to release the public endpoint of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleasePublicNet workAddress | The operation that you want to perform. Set the value to ReleasePublicNet workAddress. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NodeId | String | No | s-bpxxxxxxxx | A sharded cluster instance consists of three components: mongos, shard, and Configserver. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. You can call the DescribeDBInst anceAt t ri but e operation to view the ID of the mongos, shard, or Configserver node. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1D6AFE36-1AF5- 4DE4-A954- 672159D4CC69 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ReleasePublicNetworkAddress &DBInstanceId=dds-bpxxxxxxxx &s-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ReleasePublicNetworkAddressResponse>
   <RequestId>B6D17591-B48B-4D31-9CD6-9B9796B2270A</RequestId>
</ReleasePublicNetworkAddressResponse>
```

`JSON` format `{`

```json
 "RequestId": "1D6AFE36-1AF5-4DE4-A954-672159D4CC69"
```

`}`

#### 7.4.3 ModifyInstanceVpcAuthMode

You can call this operation to enable or disable password-free access from the same VPC as an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: A replica set or sharded cluster instance is used. The database engine version of the instance is MongoDB 4.0 or 4.2. You can call the DescribeDBInst anceAt t ribut e operation to view the database engine version of the instance. If necessary, you can call the UpgradeDBInst anceEngineVersion operation to upgrade the database engine. The network type of the instance must be VPC. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyInstanceVp cAuthMode | The operation that you want to perform. Set the value to Modif yInst anceVpcAut hMode. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeDBInst anceAt t ribut e operation to view the region ID of the instance. |
| NodeId | String | No | s-bpxxxxxxxx | The ID of the mongos node in the sharded cluster instance. Not e This parameter is valid only if you select a sharded cluster instance. |
| VpcAuthMode | String | No | Open | Specifies whether to enable password- free access within the VPC. Valid values: Open: enables password-free access within the VPC. Close: disables password-free access within the VPC. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | BA51E9D9-B14A- 4542-B6E6- 7DE00BECCB8C | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyInstanceVpcAuthMode &DBInstanceId=dds-bpxxxxxxxx &VpcAuthMode=Open &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyInstanceVpcAuthModeResponse>
      <RequestId>BA51E9D9-B14A-4542-B6E6-7DE00BECCB8C</RequestId>
</ModifyInstanceVpcAuthModeResponse>
```

`JSON` format `{`

```json
    "RequestId": "BA51E9D9-B14A-4542-B6E6-7DE00BECCB8C"
```

`}`

#### 7.4.4 DescribeShardingNetworkAddress

You can call this operation to view the connection information of an ApsaraDB for MongoDB sharded cluster instance. This operation supports sharded cluster instances only. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSharding NetworkAddress | The operation that you want to perform. Set the value to DescribeShardingNet workAddress. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos, shard, and Configserver node in the sharded cluster instance. Not e You can call the DescribeDBInst anceAt t ribut e operation to view the ID of the mongos, shard, or Configserver node. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CompatibleCon nections | Array of CompatibleCon nection |   | An array that consists of the endpoints of DynamoDB instances. |
| CompatibleCon nection |   |   |   |
| ExpiredTime | String | 2591963 | The remaining period of the classic network endpoint. Unit: seconds. |
| IPAddress | String | 10.140.xxx.xx | The IP address of the instance. |
| NetworkAddres s | String | dds- bpxxxxxxxxxxxxxx.m ongodb.rds.aliyuncs .com | The endpoint of the instance. |
| NetworkType | String | VPC | The network type of the endpoint. Valid values: VPC Classic Public |
| Port | String | 3717 | The port number. |
| VPCId | String | vpc-bpxxxxxxxx | The ID of the VPC. Not e This parameter is returned when the network type is VPC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VswitchId | String | vsw-bpxxxxxxxx | The ID of the vSwitch in the specified VPC. Not e This parameter is returned when the network type is VPC. |
| NetworkAddres ses | Array of NetworkAddres s |   | An array that consists of the endpoints of ApsaraDB for MongoDB instances. |
| NetworkAddres s |   |   |   |
| ExpiredTime | String | 2591963 | The remaining period of the classic network endpoint. Unit: seconds. |
| IPAddress | String | 10.140.xxx.xx | The IP address of the instance. |
| NetworkAddres s | String | s- bpxxxxxxxx.mongod b.rds.aliyuncs.com | The endpoint of the instance. |
| NetworkType | String | VPC | The network type of the endpoint. VPC Classic Public |
| NodeId | String | s-bpxxxxxxxx | The ID of the mongos node. |
| NodeType | String | mongos | The type of the node. Valid values: mongos shard conf igserver |
| Port | String | 3717 | The port number. |
| Role | String | Primary | The role of the node. Valid values: Primary Secondary |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VPCId | String | vpc-bpxxxxxxxx | The ID of the VPC. Not e This parameter is returned when the network type is VPC. |
| VswitchId | String | vsw-bpxxxxxxxx | The ID of the vSwitch in the specified VPC. Not e This parameter is returned when the network type is VPC. |
| RequestId | String | 18D8AAFD-6BEB- 420F-8164- 810CB0C0AA39 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeShardingNetworkAddress &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CompatibleConnections>
    <NetworkAddress>dds-bpxxxxxxxxxxxxxx.mongodb.rds.aliyuncs.com</NetworkAddress>
    <VPCId>vpc-bpxxxxxxxx</VPCId>
    <NetworkType>VPC</NetworkType>
    <ExpiredTime>2591963</ExpiredTime>
    <Port>3717</Port>
    <IPAddress>10.140.xxx.xx</IPAddress>
    <VswitchId>vsw-bpxxxxxxxx</VswitchId>
</CompatibleConnections> <RequestId>18D8AAFD-6BEB-420F-8164-810CB0C0AA39</RequestId> <NetworkAddresses>
    <Role>Primary</Role>
    <NetworkAddress>s-bpxxxxxxxx.mongodb.rds.aliyuncs.com</NetworkAddress>
    <VPCId>vpc-bpxxxxxxxx</VPCId>
    <NetworkType>VPC</NetworkType>
    <NodeType>mongos</NodeType>
    <ExpiredTime>2591963</ExpiredTime>
    <Port>3717</Port>
    <NodeId>s-bpxxxxxxxx</NodeId>
    <IPAddress>10.140.xxx.xx</IPAddress>
    <VswitchId>vsw-bpxxxxxxxx</VswitchId>
</NetworkAddresses>
```

`JSON` format `{`

```json
    "CompatibleConnections":[
```

`{`

```json
            "NetworkAddress":"dds-bpxxxxxxxxxxxxxx.mongodb.rds.aliyuncs.com",
            "VPCId":"vpc-bpxxxxxxxx",
            "NetworkType":"VPC",
            "ExpiredTime":"2591963",
            "Port":"3717",
            "IPAddress":"10.140.xxx.xx",
            "VswitchId":"vsw-bpxxxxxxxx"
```

`}` `],`

```json
    "RequestId":"18D8AAFD-6BEB-420F-8164-810CB0C0AA39",
    "NetworkAddresses":[
```

`{`

```json
            "Role":"Primary",
            "NetworkAddress":"s-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
            "VPCId":"vpc-bpxxxxxxxx",
            "NetworkType":"VPC",
            "NodeType":"mongos",
            "ExpiredTime":"2591963",
            "Port":"3717",
            "NodeId":"s-bpxxxxxxxx",
            "IPAddress":"10.140.xxx.xx",
            "VswitchId":"vsw-bpxxxxxxxx"
```

`}` `]` `}`

#### 7.4.5 ModifyDBInstanceConnectionString

You can call this operation to modify the connection string of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance ConnectionString | The operation that you want to perform. Set the value to Modif yDBInst anceConnect ionSt ring . |
| CurrentConnectio nString | String | Yes | s- bpxxxxxxxx.mong odb.rds.aliyuncs. com | The current connection string, which is to be modified. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NewConnectionSt ring | String | Yes | aliyuntest111 | The new connection string. It must be 8 to 64 characters in length and can contain letters and digits. It must start with a lowercase letter. Not e You only need to specify the prefix of the connection string. The content other than the prefix cannot be modified. |
| NodeId | String | No | s-bpxxxxxxxx | The ID of the mongos node in the sharded cluster instance. Only one mongos ID can be specified in each call. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FF36A84C-0694- 42D0-861D- C383E8E4FAAF | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceConnectionString &CurrentConnectionString=s-bpxxxxxxxx.mongodb.rds.aliyuncs.com &NewConnectionString=aliyuntest111 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceConnectionStringResponse>
   <RequestId>FF36A84C-0694-42D0-861D-C383E8E4FAAF</RequestId>
</ModifyDBInstanceConnectionStringResponse>
```

`JSON` format `{`

```json
 "RequestId": "FF36A84C-0694-42D0-861D-C383E8E4FAAF"
```

`}`

#### 7.4.6 ReleaseNodePrivateNetworkAddress

You can call this operation to release the internal endpoint of the shard or Configserver node of a sharded cluster instance. This operation is only applicable to sharded cluster instances. For more information, see Release endpoints of shard or Configserver nodes. This operation releases the internal endpoint of the node. If you have also applied for a public endpoint of the node and want to release it, you can call the ReleasePublicNetworkAddress operation to release the public endpoint. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleaseNodePriva teNetworkAddres s | The operation that you want to perform. Set the value to ReleaseNodePrivat eNet workAddre ss. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the sharded cluster instance. |
| NodeId | String | Yes | d-bpxxxxxxxx | The ID of the shard or Configserver node. Not e You can call the DescribeDBInstanceAttribute operation to query the ID of the shard or Configserver node. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NetworkType | String | Yes | VPC | The network type of the internal endpoint. Valid values: VPC Classic Not e You can call the Describeshardingendpoint address operation to query the network type of the internal endpoint. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252- 4A4A-ADDA- 5CB1BF63873D | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.aliyuncs.com/? Action=ReleaseNodePrivateNetworkAddress &DBInstanceId=dds-bpxxxxxxxx &NodeId=d-bpxxxxxxxx &NetworkType=VPC &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ReleaseNodePrivateNetworkAddressResponse>
   <RequestId>EFD65226-08CC-4C4D-B6A4-CB3C382F67B0</RequestId>
</ReleaseNodePrivateNetworkAddressResponse>
```

`JSON` format `{`

```json
 "RequestId":"0FDDC511-7252-4A4A-ADDA-5CB1BF63873D"
```

`}`

### 7.5 Instance information query

#### 7.5.1 DescribeReplicaSetRole

You can call this operation to view the role and connection information of an ApsaraDB for MongoDB instance. This operation is applicable only to replica set instances, but not to sharded cluster instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeReplicaS etRole | The operation that you want to perform. Set the value to DescribeReplicaSet Role. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DB4A0595-FCA9- 437F-B2BB- 25DBFC009D3E | The ID of the request. |
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |
| ReplicaSets | Array of ReplicaSet |   | An array that consists of the information of replica set instance roles. |
| ReplicaSet |   |   |   |
| ConnectionDom ain | String | dds- bpxxxxxxxx.mongod b.rds.aliyuncs.com | The endpoint of the node. |
| ConnectionPort | String | 3717 | The port of the node. |
| ExpiredTime | String | 1209582 | The remaining period of the classic network endpoint. Unit: seconds. |
| NetworkType | String | VPC | The network type of the endpoint. Valid values: VPC Classic Public |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ReplicaSetRole | String | Primary | The role of the node in the replica set instance. Primary Secondary |
| RoleId | String | 651xxxxx | The role ID of the node. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeReplicaSetRole &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeReplicaSetRoleResponse>
   <RequestId>7762D0FF-F34D-4DAF-9D06-6C1C28CC98CD</RequestId>
   <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId>
   <ReplicaSets>
      <ReplicaSet>
         <NetworkType>Classic</NetworkType>
         <ConnectionPort>3717</ConnectionPort>
         <ReplicaSetRole>Primary</ReplicaSetRole>
         <ConnectionDomain>dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
         <ExpiredTime>12xxxxx</ExpiredTime>
         <RoleId>55xxxxx</RoleId>
      </ReplicaSet>
      <ReplicaSet>
         <NetworkType>Classic</NetworkType>
         <ConnectionPort>3717</ConnectionPort>
         <ReplicaSetRole>Secondary</ReplicaSetRole>
         <ConnectionDomain>dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
         <ExpiredTime>12xxxxx</ExpiredTime>
         <RoleId>55xxxxx</RoleId>
      </ReplicaSet>
      <ReplicaSet>
         <NetworkType>VPC</NetworkType>
         <ConnectionPort>3717</ConnectionPort>
         <ReplicaSetRole>Primary</ReplicaSetRole>
         <ConnectionDomain>dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
         <RoleId>55xxxxx</RoleId>
      </ReplicaSet>
      <ReplicaSet>
         <NetworkType>VPC</NetworkType>
         <ConnectionPort>3717</ConnectionPort>
         <ReplicaSetRole>Secondary</ReplicaSetRole>
         <ConnectionDomain>dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
         <RoleId>55xxxxx</RoleId>
      </ReplicaSet>
   </ReplicaSets>
</DescribeReplicaSetRoleResponse>
```

`JSON` format `{`

```json
 "RequestId": "7762D0FF-F34D-4DAF-9D06-6C1C28CC98CD",
 "DBInstanceId": "dds-bpxxxxxxxx",
 "ReplicaSets": {
  "ReplicaSet": [
```

`{`

```json
    "NetworkType": "Classic",
    "ConnectionPort": "3717",
    "ReplicaSetRole": "Primary",
    "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
    "ExpiredTime": "12xxxxx",
    "RoleId": "55xxxxx"
```

`},` `{`

```json
    "NetworkType": "Classic",
    "ConnectionPort": "3717",
    "ReplicaSetRole": "Secondary",
    "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
    "ExpiredTime": "12xxxxx",
    "RoleId": "55xxxxx"
```

`},` `{`

```json
    "NetworkType": "VPC",
    "ConnectionPort": "3717",
    "ReplicaSetRole": "Primary",
    "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
    "RoleId": "55xxxxx"
```

`},` `{`

```json
    "NetworkType": "VPC",
    "ConnectionPort": "3717",
    "ReplicaSetRole": "Secondary",
    "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
    "RoleId": "55xxxxx"
```

`}` `]` `}` `}`

#### 7.5.2 DescribeKernelReleaseNotes

You can call this operation to view the release notes of the minor database versions of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeKernelRel easeNotes | The operation that you want to perform. Set the value to DescribeKernelReleaseNot es. |
| KernelVersion | String | No | mongodb 20180 _ 522 0.4.8 _ | The minor version of the database. Example: mongodb 20180522 0.4.8. _ _ If you specify this parameter, a list of versions later than the version specified is returned. If you do not specify this parameter, a list of all versions is returned. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ReleaseNotes | Array of ReleaseNote |   | An array that consists of the information of version release notes. |
| ReleaseNote |   |   |   |
| KernelVersion | String | mongodb 20180619 _ 0.4.9 _ | The version of the database. |
| ReleaseNote | String | Released the balancer switch limit for a sharded set | The release notes. |
| RequestId | String | F01D4DDA-CB72- 4083-B399- AF4642294FE6 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeKernelReleaseNotes &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>F01D4DDA-CB72-4083-B399-AF4642294FE6</RequestId> <ReleaseNotes>
    <ReleaseNote>
        <KernelVersion>mongodb_20180619_0.4.9</KernelVersion>
        <ReleaseNote>Released the balancer switch limit for a sharded set</ReleaseNote>
    </ReleaseNote>
</ReleaseNotes>
```

`JSON` format `{`

```json
    "RequestId":"F01D4DDA-CB72-4083-B399-AF4642294FE6",
    "ReleaseNotes":
```

`{`

```json
        "ReleaseNote":[
```

`{`

```json
                "KernelVersion":"mongodb_20180619_0.4.9",
                "ReleaseNote":"Released the balancer limit for a sharded set"
```

`}` `]` `}` `}`

#### 7.5.3 DescribeAvailableEngineVersion

You can call this operation to view the database engine versions that an ApsaraDB for MongoDB instance can be upgraded to. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAvailable EngineVersion | The operation that you want to perform. Set the value to DescribeAvailableEngineVersion. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 52507B6B-003B- 47A3-A0A3- 9FE992C7A243 | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EngineVersions | List | {"EngineVersion": ["4.0" ]} | The databse engine versions that the ApsaraDB for MongoDB instance can be upgraded to. Not e An empty string is returned if the latest version is being used. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAvailableEngineVersion &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAvailableEngineVersionResponse>
   <EngineVersions>
      <EngineVersion>4.0</EngineVersion>
   </EngineVersions>
   <RequestId>52507B6B-003B-47A3-A0A3-9FE992C7A243</RequestId>
</DescribeAvailableEngineVersionResponse>
```

`JSON` format `{`

```json
 "EngineVersions": {
  "EngineVersion": [
   "4.0"
```

`]` `},`

```json
 "RequestId": "52507B6B-003B-47A3-A0A3-9FE992C7A243"
```

`}`

#### 7.5.4 DescribeDBInstances

Queries the list of ApsaraDB for MongoDB instances. When you call this operation, you must configure the `x-acs-organizationid` , `x-acs-` `resourcegroupid` , and `x-acs-instanceid` header parameters to specify the organization ID, resource group ID, and instance ID. Otherwise, the call is directed to the root resource group and organization. For more information about the code, see SDK Description in ApsaraDB for MongoDB Developer Guide. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ces | The operation that you want to perform. Set the value to DescribeDBInst ances. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| DBInstanceId | String | No | dds- d1n4eab47879*** * | The ID of the instance. |
| ReplicationFactor | String | No | 3 | The number of nodes in the replica set instance. Valid values: 3, 5, and 7. |
| DBInstanceDescri ption | String | No | test | The description of the instance. |
| ExpireTime | String | No | 2019-12- 26T16:00Z | The time when the instance expires. |
| DBInstanceStatus | String | No | ACTIVATION | The status of the instance. For more information, see Instance states in ApsaraDB for MongoDB Developer Guide. |
| DBInstanceType | String | No | replicate | The architecture of the instance. Valid values: sharding: sharded cluster instance replicat e: replica set instance or standalone instance Default value: replicat e. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceClass | String | No | dds.mongo.mid | The instance type. Not e For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. |
| Engine | String | No | MongoDB | The database engine of the instance. Set the value to MongoDB. |
| EngineVersion | String | No | 4.2 | The database engine version of the instance. Valid values: 3.0, 3.4, 4.0, and 4.2. |
| NetworkType | String | No | Classic | The network type of the instance. Valid values: Classic VPC Set the value to Classic. |
| VpcId | String | No | vpc- bp1q2qqm4vxo6 e6zl**** | The ID of the virtual private cloud (VPC). |
| VSwitchId | String | No | vsw- bp1buy0h9myt5i 9e7**** | The ID of the vSwitch in the VPC. |
| ChargeType | String | No | PostPaid | The billing method of the instance. Valid values: PrePaid: subscription Post Paid: pay-as-you-go |
| ZoneId | String | No | cn-qd-agility14- amtest110**** | The zone ID of the instance. Not e You can call the DescribeRegions operation to query available zones. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Expired | String | No | true | Specifies whether the instance has expired. Valid values: t rue: The instance has expired. f alse: The instance has not expired. |
| ResourceGroupId | String | No | rg- acfm22cdcgc**** | The ID of the resource group. |
| Tag.N.Key | String | No | testdatabase | The key of tag N. Not e Valid values of N: 1 to 20. The tag key cannot exceed 64 characters in length. The tag key cannot start with aliyun , acs: , http:// , or https:/ / . The tag key cannot be an empty string. |
| Tag.N.Value | String | No | apitest | The value of tag N. Not e Valid values of N: 1 to 20. The tag value cannot exceed 128 characters in length. The tag value cannot start with aliyun , acs: , http:// , or https:/ / . The tag value can be an empty string. |

|   |   | aliyun |
|---|---|---|
|   | http:// |   |
| / |   |   |

|   |   | aliyun |
|---|---|---|
|   | http:// |   |
| / |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstances | Array of DBInstance |   | Details about the instances. |
| DBInstance |   |   |   |

| A | psaraDB for Mong | oDB |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ChargeType | String | PostPaid | The billing method of the instance. PrePaid: subscription Post Paid: pay-as-you-go |
| CreationTime | String | 2021-05- 31T12:00:52Z | The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DBInstanceClas s | String | dds.mongo.mid | The instance type. Not e For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. |
| DBInstanceDesc ription | String | Test database | The description of the instance. |
| DBInstanceId | String | dds- d1n4eab47879**** | The ID of the instance. |
| DBInstanceStat us | String | Running | The status of the instance. |
| DBInstanceStor age | Integer | 50 | The storage space of the instance. |
| DBInstanceType | String | replicate | The architecture of the instance. Valid values: sharding: sharded cluster instance replicat e: replica set instance |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DestroyTime | String | 2021-12- 31T16:00:00Z | The time when the instance data was destroyed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Not e Subscription instances are released seven days after expiration. After an instance is released, its data is deleted and cannot be restored. Pay-as-you-go instances are locked after the payment has been overdue for longer than 24 hours. Pay-as-you-go instances are released after the payment has been overdue for longer than seven days. The data of released instances is deleted and cannot be restored. |
| Engine | String | MongoDB | The database engine of the instance. |
| EngineVersion | String | 3.0 | The database engine version of the instance. |
| ExpireTime | String | 2019-11-25T16:00Z | The time when the instance expires. The time follows the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| KindCode | String | 1 | The kind code of the instance. Valid values: 0: physical machine 1: Elastic Compute Service (ECS) instance 2: Docker cluster 18: Kubernetes cluster |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LastDowngrade Time | String | 20210708 | The time when the instance was last downgraded. |
| LockMode | String | unlock | Indicates whether the instance is locked. Valid values: Unlock: The instance is not locked. ManualLock: The instance is manually locked. LockByExpirat ion: The instance is automatically locked after it expires. LockByRest orat ion: The instance is automatically locked before it is rolled back. LockByDiskQuot a: The instance is automatically locked after the storage space is exhausted. Released: The instance is released. You cannot unlock an instance that is released. After an instance is released, you can only use a backup to restore the data of the instance to a new instance. This process requires a long period of time. |
| MongosList | Array of MongosAttribut e |   | Details about the mongos nodes. Not e This parameter is returned if the instance is a sharded cluster instance. |
| MongosAttribut e |   |   |   |
| NodeClass | String | dds.mongos.mid | The type of the mongos node. |
| NodeDescriptio n | String | Test mongos node | The description of the mongos node. |
| NodeId | String | s-d1n849c1788f**** | The ID of the mongos node. |
| NetworkType | String | Classic | The network type of the instance. The value is fixed at Classic. |
| RegionId | String | cn-qd-agility14**** | The region ID of the instance. |

| eveloper Guide·AP | I Reference |   | ApsaraDB for MongoD |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ReplicationFact or | String | 3 | The number of nodes in the instance. Not e This parameter is returned if the instance is a replica set instance. |
| ResourceGroupI d | String | rg-acfm22cdcgc**** | The ID of the resource group. |
| ShardList | Array of ShardAttribute |   | Details about the shard nodes. Not e This parameter is returned if the instance is a sharded cluster instance. |
| ShardAttribute |   |   |   |
| NodeClass | String | dds.shard.mid | The type of the shard node. |
| NodeDescriptio n | String | Test shard node | The description of the shard node. |
| NodeId | String | d-d1n753c91603**** | The ID of the shard node. |
| NodeStorage | Integer | 20 | The storage space of the shard node. Unit: GB. |
| Tags | Array of Tag |   | Details about the resource tags. |
| Tag |   |   |   |
| Key | String | test | The tag key of the resource. |
| Value | String | api | The tag value of the resource. |
| VpcAuthMode | String | Close | Indicates whether password-free access within the VPC is enabled. Valid values: Open: Password-free access is enabled. Close: Password-free access is disabled. |
| ZoneId | String | cn-qd-agility14- amtest110**** | The zone ID of the instance. |

| psaraDB for Mong | oDB |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 30 | The number of entries returned per page. |
| RequestId | String | A10B8ECB-0BA0- 4EC6-93A5- C65FDEDA**** | The ID of the request. |
| TotalCount | Integer | 1 | The number of instances in the query results. |

Examples Sample requests

```
http(s)://mongodb.example.com/?Action=DescribeDBInstances &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstancesResponse>
  <TotalCount>1</TotalCount>
  <PageSize>30</PageSize>
  <RequestId>A10B8ECB-0BA0-4EC6-93A5-C65FDEDA****</RequestId>
  <PageNumber>1</PageNumber>
  <DBInstances>
        <EngineVersion>3.0</EngineVersion>
        <ReplicationFactor>3</ReplicationFactor>
        <DBInstanceStatus>Running</DBInstanceStatus>
        <ZoneId>cn-qd-agility14-amtest110****</ZoneId>
        <ResourceGroupId>rg-acfm22cdcgc****</ResourceGroupId>
        <DBInstanceClass>dds.mongo.mid</DBInstanceClass>
        <DestroyTime>2021-12-31T16:00:00Z</DestroyTime>
        <DBInstanceType>replicate</DBInstanceType>
        <LockMode>unlock</LockMode>
        <DBInstanceId>dds-d1n4eab47879****</DBInstanceId>
        <VpcAuthMode>Close</VpcAuthMode>
        <NetworkType>Classic</NetworkType>
        <ChargeType>PostPaid</ChargeType>
        <LastDowngradeTime>20210708</LastDowngradeTime>
        <DBInstanceStorage>50</DBInstanceStorage>
        <CreationTime>2021-05-31T12:00:52Z</CreationTime>
        <RegionId>cn-qd-agility14****</RegionId>
        <ExpireTime>2019-11-25T16:00Z</ExpireTime>
        <KindCode>1</KindCode>
        <Engine>MongoDB</Engine>
        <DBInstanceDescription>Test database</DBInstanceDescription>
        <ShardList>
              <NodeClass>dds.shard.mid</NodeClass>
              <NodeDescription>Test shard node</NodeDescription>
              <NodeStorage>20</NodeStorage>
              <NodeId>d-d1n753c91603****</NodeId>
        </ShardList>
        <MongosList>
              <NodeClass>dds.mongos.mid</NodeClass>
              <NodeDescription>Test mongos node</NodeDescription>
              <NodeId>s-d1n849c1788f****</NodeId>
        </MongosList>
        <Tags>
              <Value>api</Value>
              <Key>test</Key>
        </Tags>
  </DBInstances>
</DescribeDBInstancesResponse>
```

`JSON` format `{`

```json
  "TotalCount": "1",
  "PageSize": "30",
  "RequestId": "A10B8ECB-0BA0-4EC6-93A5-C65FDEDA****",
  "PageNumber": "1",
  "DBInstances": [
```

`{`

```json
      "EngineVersion": "3.0",
      "ReplicationFactor": "3",
      "DBInstanceStatus": "Running",
      "ZoneId": "cn-qd-agility14-amtest110****",
      "ResourceGroupId": "rg-acfm22cdcgc****",
      "DBInstanceClass": "dds.mongo.mid",
      "DestroyTime": "2021-12-31T16:00:00Z",
      "DBInstanceType": "replicate",
      "LockMode": "unlock",
      "DBInstanceId": "dds-d1n4eab47879****",
      "VpcAuthMode": "Close",
      "NetworkType": "Classic",
      "ChargeType": "PostPaid",
      "LastDowngradeTime": "20210708",
      "DBInstanceStorage": "50",
      "CreationTime": "2021-05-31T12:00:52Z",
      "RegionId": "cn-qd-agility14****",
      "ExpireTime": "2019-11-25T16:00Z",
      "KindCode": "1",
      "Engine": "MongoDB",
      "DBInstanceDescription": "Test database",
      "ShardList": [
```

`{`

```json
          "NodeClass": "dds.shard.mid",
          "NodeDescription": "Test shard node",
          "NodeStorage": "20",
          "NodeId": "d-d1n753c91603****"
```

`}` `],`

```json
      "MongosList": [
```

`{`

```json
          "NodeClass": "dds.mongos.mid",
          "NodeDescription": "Test mongos node",
          "NodeId": "s-d1n849c1788f****"
```

`}` `],`

```json
      "Tags": [
```

`{`

```json
          "Value": "api",
          "Key": "test"
```

`}` `]` `}` `]` `}`

#### 7.5.5 DescribeDBInstanceAttribute

You can call this operation to view the details of a MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceAttribute | The operation that you want to perform. Set the value to DescribeDBInst anceAt t ribut e. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| Engine | String | No | MongoDB | The database engine. Set the value to MongoDB. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C373EED9-5125- 4DD9-89DB- FB1ECD2C2B4F | The ID of the request. |
| DBInstances | Array of DBInstance |   | An array that consists of the information of the instance. |
| DBInstance |   |   |   |
| ChargeType | String | PostPaid | The billing method of the instance. PrePaid: subscription Post Paid: pay-as-you-go |
| ConfigserverLis t | Array of ConfigserverAtt ribute |   | An array that consists of the information of Configserve nodes. Not e This parameter is returned if the instance type is sharded cluster. |
| ConfigserverAtt ribute |   |   |   |

| A | psaraDB for Mong | oDB |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConnectString | String | mongodb://root:** **@dds- bpxxxxxxxxxxxxxx- cs1730- pub.mongodb.rds.al iyuncs.com:3717 | The connection string URI of the Configserver node. |
| MaxConnection s | Integer | 0 | The maximum number of connections of the Configserver node. |
| MaxIOPS | Integer | 1000 | The maximum input/output operations per second (IOPS) of the Configserver node. |
| NodeClass | String | dds.cs.mid | The specifications of the Configserver node. |
| NodeDescriptio n | String | testConfigserver | The name of the Configserver node. |
| NodeId | String | dds- bpxxxxxxxxxxxxxx-cs | The ID of the Configserver node. |
| NodeStorage | Integer | 20 | The storage capacity of the Configserver node. |
| Port | Integer | 3717 | The port of the Configserver node. |
| CreationTime | String | 2018-11- 21T05:10:00Z | The time when the instance was created. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| CurrentKernelV ersion | String | mongodb 20180914 _ 1.1.5 _ | The minor version of the current database of the instance. |
| DBInstanceClas s | String | dds.mongo.mid | The instance type. |
| DBInstanceDesc ription | String | Test | The name of the instance. |
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceRele aseProtection | Boolean | true | Indicates whether release protection is enabled for the instance. Valid values: t rue: Release protection is enabled. f alse: Release protection is disabled. |
| DBInstanceStat us | String | Running | The status of the instance. For more information, see Inst ance t ypes in ApsaraDB for MongoDB Product Introduction. |
| DBInstanceStor age | Integer | 10 | The storage capacity of the instance. |
| DBInstanceType | String | replicate | The architecture type of the instance. replicat e: replica set instance sharding: sharded cluster instance |
| Engine | String | MongoDB | The database engine of the instance. |
| EngineVersion | String | 3.4 | The version of the database engine. |
| ExpireTime | String | 2019-04-08T16:00Z | The time when the subscription instance expires. The time is in the yyyy-MM- ddTHH:mmZ format. The time is displayed in UTC. Not e This parameter is returned if the instance billing method is subscription. |
| KindCode | String | 1 | The kind code of the instance. Valid values: 0: physical machine 1: Elastic Compute Service (ECS) 2: Docker cluster 18: Kubernetes cluster |
| LastDowngrade Time | String | 2019-03-08 | The last time when the instance was downgraded. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LockMode | String | Unlock | Indicates whether the instance is locked. Valid values: Unlock: The instance is not locked. ManualLock: The instance has been manually locked. LockByExpirat ion: The instance has been locked upon expiration. LockByRest orat ion: The instance has been locked for a rollback. LockByDiskQuot a: The instance has been automatically locked because its storage space is exhausted. Released: The instance has been released. You cannot unlock a released instance. After an instance is released, you can only use a backup to restore the data of the instance to a new instance. This process requires a long time. |
| MaintainEndTim e | String | 03:00Z | The end time of the maintenance window. The time is in the HH:mmZ format. The time is displayed in UTC. |
| MaintainStartTi me | String | 02:00Z | The start time of the maintenance window. The time is in the HH:mmZ format. The time is displayed in UTC. |
| MaxConnection s | Integer | 500 | The maximum number of connections of the instance. |
| MaxIOPS | Integer | 1000 | The maximum IOPS of the instance. |
| MongosList | Array of MongosAttribut e |   | An array that consists of the information of mongos nodes. Not e This parameter is returned if the instance type is sharded cluster. |
| MongosAttribut e |   |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConnectSting | String | s- bpxxxxxxxx.mongod b.rds.aliyuncs.com | The endpoint of the mongos node. |
| MaxConnection s | Integer | 1000 | The maximum number of connections of the mongos node. |
| MaxIOPS | Integer | 0 | The maximum IOPS of the mongos node. |
| NodeClass | String | dds.mongos.mid | The specifications of the mongos node. |
| NodeDescriptio n | String | mongos1 | The name of the mongos node. |
| NodeId | String | s-bpxxxxxxxx | The ID of the mongos node. |
| Port | Integer | 3717 | The port of the mongos node. |
| VPCId | String | vpc- bp1xxxxxxxxxxxxxxx xxx | The VPC ID of the mongos node. |
| VSwitchId | String | vsw- bp1xxxxxxxxxxxxxxx xxx | The vSwitch ID of the mongos node. |
| VpcCloudInstan ceId | String | s-bp1xxxxxxxxxxxxx | The ID of the VPC instance for the mongos ID. |
| NetworkType | String | VPC | The network type of the instance. Valid values: Classic VPC |
| ProtocolType | String | mongodb | The access protocol type of the instance. Valid values: mongodb: the MongoDB protocol dynamodb: the DynamoDB protocol |
| ReadonlyReplic as | String | 0 | The number of read-only nodes in the instance. |

| psaraDB for Mong | oDB |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RegionId | String | cn-hangzhou | The region ID of the instance. |
| ReplacateId | String | bls-mxxxxxxxx | The BLS channel ID of the instance. |
| ReplicaSetNam e | String | mgset-10xxxxxxxx | The name of the replica set instance. Not e This parameter is returned if the instance type is replica set. |
| ReplicaSets | Array of ReplicaSet |   | The information list of the replica set. Not e This parameter is returned if the instance type is replica set. |
| ReplicaSet |   |   |   |
| ConnectionDom ain | String | dds- bpxxxxxxxx.mongod b.rds.aliyuncs.com | The endpoint of the node. |
| ConnectionPort | String | ConnectionPort | The port of the node. |
| NetworkType | String | VPC | The network type of the node. Valid values: Classic VPC |
| ReplicaSetRole | String | Primary | The role of the node. Primary Secondary |
| VPCCloudInstan ceId | String | vpc-xxxxxxxx | The ID of the VPC instance for the node. |
| VPCId | String | vpc-bpxxxxxxxx | The VPC ID of the node. |
| VSwitchId | String | vsw-bpxxxxxxxx | The vSwitch ID of the node. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ReplicationFact or | String | 3 | The number of nodes in the instance. Not e This parameter is returned if the instance type is replica set. |
| ResourceGroupI d | String | rg-axxxxxxxx | The ID of the resource group to which the instance belongs. |
| ShardList | Array of ShardAttribute |   | An array that consists of the information of shard nodes. Not e This parameter is returned if the instance type is sharded cluster. |
| ShardAttribute |   |   |   |
| ConnectString | String | d- bpxxxxxxxxxxxxxxxxx x.mongodb.rds.aliyu ncs.com | The endpoint of the shard node. |
| MaxConnection s | Integer | 8000 | The maximum number of connections of the shard node. |
| MaxIOPS | Integer | 8000 | The maximum IOPS of the shard node. |
| NodeClass | String | dds.shard.mid | The specifications of the shard node. |
| NodeDescriptio n | String | testshard | The name of the shard node. |
| NodeId | String | d-bpxxxxxxxx | The ID of the shard node. |
| NodeStorage | Integer | 10 | The storage capacity of the shard node. |
| Port | Integer | 3717 | The port of the shard node. |
| StorageEngine | String | WiredTiger | The storage engine of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Tags | Array of Tag |   | An array that consists of the information of instance tags. |
| Tag |   |   |   |
| Key | String | test | The key of the instance tag. |
| Value | String | api | The value of the instance tag. |
| VPCCloudInstan ceIds | String | s-bp1xxxxxxxxxxxxx | The ID of the VPC instance for the instance. |
| VPCId | String | vpc-bpxxxxxxxx | The ID of the VPC. |
| VSwitchId | String | vsw-bpxxxxxxxx | The ID of the vSwitch in the specified VPC. |
| VpcAuthMode | String | Open | Indicates whether password-free access within the VPC is enabled. Valid values: Open: Password-free access is enabled. Close: Password-free access is disabled. Not Support : Password-free access is not supported. |
| ZoneId | String | cn-hangzhou-b | The zone ID of the instance. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeDBInstanceAttribute &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>C373EED9-5125-4DD9-89DB-FB1ECD2C2B4F</RequestId> <DBInstances>
    <VPCCloudInstanceIds>s-bp1xxxxxxxxxxxxx</VPCCloudInstanceIds>
    <ResourceGroupId>rg-axxxxxxxx</ResourceGroupId>
    <DBInstanceType>replicate</DBInstanceType>
    <ReplicaSetName>mgset-10xxxxxxxx</ReplicaSetName>
    <StorageEngine>WiredTiger</StorageEngine>
    <MaintainEndTime>03:00Z</MaintainEndTime>
```

```xml
    <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId>
    <NetworkType>VPC</NetworkType>
    <LastDowngradeTime>2019-03-08</LastDowngradeTime>
    <DBInstanceStorage>10</DBInstanceStorage>
    <MaintainStartTime>02:00Z</MaintainStartTime>
    <Engine>MongoDB</Engine>
    <DBInstanceDescription>Test</DBInstanceDescription>
    <ReplacateId>bls-mxxxxxxxx</ReplacateId>
    <DBInstanceReleaseProtection>true</DBInstanceReleaseProtection>
    <EngineVersion>3.4</EngineVersion>
    <MaxConnections>500</MaxConnections>
    <ReadonlyReplicas>0</ReadonlyReplicas>
    <ReplicationFactor>3</ReplicationFactor>
    <DBInstanceStatus>Running</DBInstanceStatus>
    <ZoneId>cn-hangzhou-b</ZoneId>
    <VPCId>vpc-bpxxxxxxxx</VPCId>
    <DBInstanceClass>dds.mongo.mid</DBInstanceClass>
    <VSwitchId>vsw-bpxxxxxxxx</VSwitchId>
    <LockMode>Unlock</LockMode>
    <MaxIOPS>1000</MaxIOPS>
    <VpcAuthMode>Open</VpcAuthMode>
    <ProtocolType>mongodb</ProtocolType>
    <CurrentKernelVersion>mongodb_20180914_1.1.5</CurrentKernelVersion>
    <ChargeType>PostPaid</ChargeType>
    <CreationTime>2018-11-21T05:10:00Z</CreationTime>
    <RegionId>cn-hangzhou</RegionId>
    <ExpireTime>2019-04-08T16:00Z</ExpireTime>
    <KindCode>1</KindCode>
</DBInstances> <DBInstances>
    <ShardList>
        <NodeClass>dds.shard.mid</NodeClass>
        <NodeDescription>testshard</NodeDescription>
        <MaxConnections>8000</MaxConnections>
        <Port>3717</Port>
        <NodeStorage>10</NodeStorage>
        <NodeId>d-bpxxxxxxxx</NodeId>
        <ConnectString>d-bpxxxxxxxxxxxxxxxxxx.mongodb.rds.example.com</ConnectString>
        <MaxIOPS>8000</MaxIOPS>
    </ShardList>
    <ConfigserverList>
        <NodeClass>dds.cs.mid</NodeClass>
        <NodeDescription>testConfigserver</NodeDescription>
        <MaxConnections>0</MaxConnections>
        <Port>3717</Port>
        <NodeStorage>20</NodeStorage>
        <NodeId>dds-bpxxxxxxxxxxxxxx-cs</NodeId>
        <ConnectString>mongodb://root:****@dds-bpxxxxxxxxxxxxxx-cs1730-pub.mongodb.rds.exam
ple.com:3717</ConnectString>
        <MaxIOPS>1000</MaxIOPS>
    </ConfigserverList>
    <MongosList>
        <ConnectSting>s-bpxxxxxxxx.mongodb.rds.example.com</ConnectSting>
        <NodeClass>dds.mongos.mid</NodeClass>
```

```xml
        <NodeDescription>mongos1</NodeDescription>
        <MaxConnections>1000</MaxConnections>
        <VPCId>vpc-bp1xxxxxxxxxxxxxxxxxx</VPCId>
        <VSwitchId>vsw-bp1xxxxxxxxxxxxxxxxxx</VSwitchId>
        <Port>3717</Port>
        <NodeId>s-bpxxxxxxxx</NodeId>
        <VpcCloudInstanceId>s-bp1xxxxxxxxxxxxx</VpcCloudInstanceId>
        <MaxIOPS>0</MaxIOPS>
    </MongosList>
    <Tags>
        <Value>api</Value>
        <Key>test</Key>
    </Tags>
    <ReplicaSets>
        <ConnectionDomain>dds-bpxxxxxxxx.mongodb.rds.example.com</ConnectionDomain>
        <ReplicaSetRole>Primary</ReplicaSetRole>
        <VPCCloudInstanceId>vpc-xxxxxxxx</VPCCloudInstanceId>
        <VPCId>vpc-bpxxxxxxxx</VPCId>
        <ConnectionPort>ConnectionPort</ConnectionPort>
        <NetworkType>VPC</NetworkType>
        <VSwitchId>vsw-bpxxxxxxxx</VSwitchId>
    </ReplicaSets>
</DBInstances>
```

`JSON` format `{`

```json
    "RequestId":"C373EED9-5125-4DD9-89DB-FB1ECD2C2B4F",
    "DBInstances":[
```

`{`

```json
            "VPCCloudInstanceIds":"s-bp1xxxxxxxxxxxxx",
            "ResourceGroupId":"rg-axxxxxxxx",
            "DBInstanceType":"replicate",
            "ReplicaSetName":"mgset-10xxxxxxxx",
            "StorageEngine":"WiredTiger",
            "MaintainEndTime":"03:00Z",
            "DBInstanceId":"dds-bpxxxxxxxx",
            "NetworkType":"VPC",
            "LastDowngradeTime":"2019-03-08",
            "DBInstanceStorage":"10",
            "MaintainStartTime":"02:00Z",
            "Engine":"MongoDB",
            "DBInstanceDescription":"Test",
            "ReplacateId":"bls-mxxxxxxxx",
            "DBInstanceReleaseProtection":"true",
            "EngineVersion":"3.4",
            "MaxConnections":"500",
            "ReadonlyReplicas":"0",
            "ReplicationFactor":"3",
            "DBInstanceStatus":"Running",
            "ZoneId":"cn-hangzhou-b",
            "VPCId":"vpc-bpxxxxxxxx",
            "DBInstanceClass":"dds.mongo.mid",
"VSwitchId":"vsw-bpxxxxxxxx",
```

```json
            VSwitchId:vswbpxxxxxxxx,
            "LockMode":"Unlock",
            "MaxIOPS":"1000",
            "VpcAuthMode":"Open",
            "ProtocolType":"mongodb",
            "CurrentKernelVersion":"mongodb_20180914_1.1.5",
            "ChargeType":"PostPaid",
            "CreationTime":"2018-11-21T05:10:00Z",
            "RegionId":"cn-hangzhou",
            "ExpireTime":"2019-04-08T16:00Z",
            "KindCode":"1"
```

`},` `{`

```json
            "ShardList":[
```

`{`

```json
                    "NodeClass":"dds.shard.mid",
                    "NodeDescription":"testshard",
                    "MaxConnections":"8000",
                    "Port":"3717",
                    "NodeStorage":"10",
                    "NodeId":"d-bpxxxxxxxx",
                    "ConnectString":"d-bpxxxxxxxxxxxxxxxxxx.mongodb.rds.example.com",
                    "MaxIOPS":"8000"
```

`}` `],`

```json
            "ConfigserverList":[
```

`{`

```json
                    "NodeClass":"dds.cs.mid",
                    "NodeDescription":"testConfigserver",
                    "MaxConnections":"0",
                    "Port":"3717",
                    "NodeStorage":"20",
                    "NodeId":"dds-bpxxxxxxxxxxxxxx-cs",
                    "ConnectString":"mongodb://root:****@dds-bpxxxxxxxxxxxxxx-cs1730-pub.mo
ngodb.rds.example.com:3717",
                    "MaxIOPS":"1000"
```

`}` `],`

```json
            "MongosList":[
```

`{`

```json
                    "ConnectSting":"s-bpxxxxxxxx.mongodb.rds.example.com",
                    "NodeClass":"dds.mongos.mid",
                    "NodeDescription":"mongos1",
                    "MaxConnections":"1000",
                    "VPCId":"vpc-bp1xxxxxxxxxxxxxxxxxx",
                    "VSwitchId":"vsw-bp1xxxxxxxxxxxxxxxxxx",
                    "Port":"3717",
                    "NodeId":"s-bpxxxxxxxx",
                    "VpcCloudInstanceId":"s-bp1xxxxxxxxxxxxx",
                    "MaxIOPS":"0"
```

`}` `],`

```json
            "Tags":[
```

`{`

```json
                    "Value":"api",
```

```json
                    "Key":"test"
```

`}` `],`

```json
            "ReplicaSets":[
```

`{`

```json
                    "ConnectionDomain":"dds-bpxxxxxxxx.mongodb.rds.example.com",
                    "ReplicaSetRole":"Primary",
                    "VPCCloudInstanceId":"vpc-xxxxxxxx",
                    "VPCId":"vpc-bpxxxxxxxx",
                    "ConnectionPort":"ConnectionPort",
                    "NetworkType":"VPC",
                    "VSwitchId":"vsw-bpxxxxxxxx"
```

`}` `]` `}` `]` `}`

#### 7.5.6 DescribeRoleZoneInfo

You can call this operation to view the roles and zones of nodes in an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRoleZon eInfo | The operation that you want to perform. Set the value to DescribeRoleZoneInf o. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 728B9A96-E262- 4AE5-915E- 3A51CCE2FDA9 | The ID of the request. |
| ZoneInfos | Array of ZoneInfo |   | An array that consists of information of nodes in the zone. |
| ZoneInfo |   |   |   |
| InsName | String | dds-bpxxxxxxxx | The ID of the node. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NodeType | String | normal | The type of the node. Valid values: normal conf igServer shard mongos Not e Valid value for replica set instances: normal. Valid values for sharded cluster instances: conf igServer, shard, and mongos. |
| RoleId | String | 83xxxxx | The ID of the role. |
| RoleType | String | Primary | The role of the node. Valid values: Primary Secondary Hidden |
| ZoneId | String | cn-hangzhou-e | The zone ID. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeRoleZoneInfo &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRoleZoneInfoResponse>
   <ZoneInfos>
      <ZoneInfo>
         <RoleType>Primary</RoleType>
         <NodeType>normal</NodeType>
         <InsName>dds-bpxxxxxxxx</InsName>
         <ZoneId>cn-hangzhou-e</ZoneId>
         <RoleId>83xxxxx</RoleId>
      </ZoneInfo>
      <ZoneInfo>
         <RoleType>Secondary</RoleType>
         <NodeType>normal</NodeType>
         <InsName>dds-bpxxxxxxxx</InsName>
         <ZoneId>cn-hangzhou-f</ZoneId>
         <RoleId>83xxxxx</RoleId>
      </ZoneInfo>
      <ZoneInfo>
         <RoleType>Hidden</RoleType>
         <NodeType>normal</NodeType>
         <InsName>dds-bpxxxxxxxx</InsName>
         <ZoneId>cn-hangzhou-b</ZoneId>
         <RoleId>83xxxxx</RoleId>
      </ZoneInfo>
   </ZoneInfos>
   <RequestId>728B9A96-E262-4AE5-915E-3A51CCE2FDA9</RequestId>
</DescribeRoleZoneInfoResponse>
```

`JSON` format `{`

```json
 "ZoneInfos": {
  "ZoneInfo": [
```

`{`

```json
    "RoleType": "Primary",
    "NodeType": "normal",
    "InsName": "dds-bpxxxxxxxx",
    "ZoneId": "cn-hangzhou-e",
    "RoleId": "83xxxxx"
```

`},` `{`

```json
    "RoleType": "Secondary",
    "NodeType": "normal",
    "InsName": "dds-bpxxxxxxxx",
    "ZoneId": "cn-hangzhou-f",
    "RoleId": "83xxxxx"
```

`},` `{`

```json
    "RoleType": "Hidden",
    "NodeType": "normal",
    "InsName": "dds-bpxxxxxxxx",
    "ZoneId": "cn-hangzhou-b",
    "RoleId": "83xxxxx"
```

`}` `]` `},`

```json
 "RequestId": "728B9A96-E262-4AE5-915E-3A51CCE2FDA9"
```

`}`

### 7.6 Instance management

#### 7.6.1 RestartDBInstance

You can call this operation to restart an ApsaraDB for MongoDB instance. This operation can also be used to restart a shard or mongos node in a replica set instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RestartDBInstanc e | The operation that you want to perform. Set the value to Rest art DBInst ance. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard or mongos node in the sharded cluster instance. Not e The sharded cluster instance will be restarted if this parameter is not specified. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 149C517D-B586- 47BE-A107- 8673E0ED77C6 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=RestartDBInstance &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RestartDBInstanceResponse>
   <RequestId>149C517D-B586-47BE-A107-8673E0ED77C6</RequestId>
</RestartDBInstanceResponse>
```

`JSON` format `{`

```json
 "RequestId": "149C517D-B586-47BE-A107-8673E0ED77C6"
```

`}`

#### 7.6.2 ModifyDBInstanceMaintainTime

You can call this operation to modify the maintenance window of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance MaintainTime | The operation that you want to perform. Set the value to Modif yDBInst anceMaint ainT ime. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| MaintainEndTime | String | Yes | 02:00Z | The end time of the maintenance window. Specify the time in the HH:mmZ format. The time must be in UTC. Not e The difference between the start time and end time must be one hour. For example, if Maint ainSt art T ime is 01:00Z, Maint ainEndT ime must be 02:00Z. |
| MaintainStartTim e | String | Yes | 01:00Z | The start time of the maintenance window. Specify the time in the HH:mmZ format. The time must be in UTC. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A9310426-C763- 42A2-A3AD- 70A8DA204531 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceMaintainTime &MaintainStartTime=01:00Z &MaintainEndTime=02:00Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceMaintainTimeResponse>
   <RequestId>A9310426-C763-42A2-A3AD-70A8DA204531</RequestId>
</ModifyDBInstanceMaintainTimeResponse>
```

`JSON` format `{`

```json
 "RequestId": "A9310426-C763-42A2-A3AD-70A8DA204531"
```

`}`

#### 7.6.3 ModifyDBInstanceDescription

You can call this operation to change the name of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance Description | The operation that you want to perform. Set the value to Modif yDBInst anceDescript ion. |
| DBInstanceDescri ption | String | Yes | testdata | The name of the instance. Not e The name cannot start with http:// or https://. The name must start with a letter. It can contain letters, underscores ( ), hyphens (- _ ), and digits. It must be 2 to 256 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you want to modify the name of a shard or mongos node in a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard or mongos node in the sharded cluster instance. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 06F8F642-4009- 4FFC-80C4- 9D67DBF7B74E | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceDescription &DBInstanceDescription=testdata &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceDescriptionResponse>
   <RequestId>06F8F642-4009-4FFC-80C4-9D67DBF7B74E</RequestId>
</ModifyDBInstanceDescriptionResponse>
```

`JSON` format `{`

```json
 "RequestId": "06F8F642-4009-4FFC-80C4-9D67DBF7B74E"
```

`}`

#### 7.6.4 SwitchDBInstanceHA

You can call this operation to switch between the primary and secondary nodes in an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation. On replica set instances, the switch is performed between primary and secondary instances. On sharded cluster instances, the switch is performed between primary and secondary shard nodes. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SwitchDBInstance HA | The operation that you want to perform. Set the value to Swit chDBInst anceHA. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard node in the sharded cluster instance. Not e If you set the DBInst anceId parameter to the ID of a sharded cluster instance, you must specify this parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RoleIds | String | No | 972xxxx,972xxxx | The IDs of the roles that you want to switch. You can call the DescribeRoleZoneInf o operation to view the IDs and information of roles of nodes. Not e Separate role IDs with commas (,). If this parameter is not specified, the primary and secondary nodes are switched. If you set the DBInst anceId parameter to the ID of a sharded cluster instance, the roles to be switched must belong to one shard node. |
| SwitchMode | Integer | No | 0 | The time when roles of the primary and secondary nodes are switched. Valid values: 0: The roles are switched immediately. 1: The roles are switched during the maintenance period. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 26BD4E5F-BDB4- 47BA-B232- 413AA78CFA8F | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=SwitchDBInstanceHA &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SwitchDBInstanceHAResponse>
   <RequestId>26BD4E5F-BDB4-47BA-B232-413AA78CFA8F</RequestId>
</SwitchDBInstanceHAResponse>
```

`JSON` format `{`

```json
 "RequestId": "26BD4E5F-BDB4-47BA-B232-413AA78CFA8F"
```

`}`

#### 7.6.5 UpgradeDBInstanceEngineVersion

You can call this operation to upgrade the database version of an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation. The available database versions are subject to the storage engine used by the instance. You can call the DescribeAvailableEngineVersion operation to view the available database versions. The database version cannot be downgraded after it is upgraded. The instance is automatically restarted for two to three times during the upgrade process. Make sure that you upgrade the instance during off-peak hours. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpgradeDBInstan ceEngineVersion | The operation that you want to perform. Set the value to UpgradeDBInst anceEngineVersion. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EngineVersion | String | Yes | 4.2 | The new database engine version of the instance. Valid values: 3.4, 4.0, and 4.2. Not e The new database engine version must be later than the current version. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C4907B00-A208- 4E0C-A636- AA85140E406C | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=UpgradeDBInstanceEngineVersion &EngineVersion=4.0 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UpgradeDBInstanceEngineVersionResponse>
   <RequestId>C4907B00-A208-4E0C-A636-AA85140E406C</RequestId>
</UpgradeDBInstanceEngineVersionResponse>
```

`JSON` format `{`

```json
 "RequestId": "C4907B00-A208-4E0C-A636-AA85140E406C"
```

`}`

#### 7.6.6 UpgradeDBInstanceKernelVersion

You can call this operation to upgrade the minor database version of an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation. The instance will be restarted once during the upgrade. Perform this operation during off-peak hours. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpgradeDBInstan ceKernelVersion | The operation that you want to perform. Set the value to UpgradeDBInst anceKernelVersion. |
| DBInstanceId | String | No | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 27B9A130-7C4B- 40D9-84E8- 2FC081097AAC | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=UpgradeDBInstanceKernelVersion &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UpgradeDBInstanceKernelVersionResponse>
   <RequestId>27B9A130-7C4B-40D9-84E8-2FC081097AAC</RequestId>
</UpgradeDBInstanceKernelVersionResponse>
```

`JSON` format `{`

```json
 "RequestId": "27B9A130-7C4B-40D9-84E8-2FC081097AAC"
```

`}`

#### 7.6.7 ModifyDBInstanceNetExpireTime

You can call this operation to extend the retention period of the classic network of an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: The instance must be running. The network of the instance is in hybrid access mode. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance NetExpireTime | The operation that you want to perform. Set the value to Modif yDBInst anceNet ExpireT ime. |
| ClassicExpendExpi redDays | Integer | Yes | 30 | The retention period of the original classic network address. Valid values: 14, 30, 60, and 120. Unit: day. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| ConnectionString | String | No | dds- bpxxxxxxxx.mong odb.rds.aliyuncs. com | The connection address of the instance |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 459E7D5C-38DA- 4E14-9C82- 5B5AF693DBAB | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceNetExpireTime &ClassicExpendExpiredDays=30 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceNetExpireTimeResponse>
   <RequestId>459E7D5C-38DA-4E14-9C82-5B5AF693DBAB</RequestId>
</ModifyDBInstanceNetExpireTimeResponse>
```

`JSON` format `{`

```json
 "RequestId": "459E7D5C-38DA-4E14-9C82-5B5AF693DBAB"
```

`}`

### 7.7 Account management

#### 7.7.1 DescribeAccounts

You can call this operation to view the information of the database account of an ApsaraDB for MongoDB instance. This operation can display only the information of the root account. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccounts | The operation that you want to perform. Set the value to DescribeAccount s. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| AccountName | String | No | root | The name of the account. Set the value to root . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Accounts | Array of Account |   | An array that consists of the information of accounts. |
| Account |   |   |   |
| AccountDescrip tion | String | Administrator | The description of the account. |
| AccountName | String | root | The name of the account. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccountStatus | String | Available | The status of the account. Unavailable Available |
| CharacterType | String | normal | The role of the account. Valid values: db: the shard node cs: the Configserver node mongos: the mongos node logic: the sharded cluster instance normal: the replica set instance |
| DBInstanceId | String | dds-bpxxxxxxxx | The name of the instance to which the account belongs. |
| RequestId | String | B562A65B-39AB- 4EE8-8635- 5A222054FB35 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAccounts &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAccountsResponse>
   <Accounts>
      <Account>
         <AccountStatus>Available</AccountStatus>
         <AccountDescription>Administrator</AccountDescription>
         <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId>
         <AccountName>root</AccountName>
      </Account>
   </Accounts>
   <RequestId>A806B0FC-CFCC-48D8-8AEC-34C892806B40</RequestId>
</DescribeAccountsResponse>
```

`JSON` format `{`

```json
    "Accounts": {
        "Account": [
```

`{`

```json
                "AccountStatus": "Available",
                "AccountDescription": "Administrator",
                "DBInstanceId": "dds-bpxxxxxxxx",
                "AccountName": "root"
```

`}` `]` `},`

```json
    "RequestId": "A806B0FC-CFCC-48D8-8AEC-34C892806B40"
```

`}`

#### 7.7.2 ResetAccountPassword

You can call this operation to reset the password of the root account of an ApsaraDB for MongoDB instance. This operation can reset only the password of the root account of an instance. Request parameters

| Parameter | Type | Required |   | Example | Description |   |
|---|---|---|---|---|---|---|
| Action | String | Yes |   | ResetAccountPas sword | The operation that you want to perform. Set the value to Reset Account Password. |   |
| AccountName | String | Yes |   | root | The account for which you want to reset the password. Set the value to root . |   |
| AccountPassword | String | Yes |   | Ali! 123456 | The new password. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! # $ % ^ & * ( ) + _ - = #$%^&*() +-= _ The password must be 8 to 32 characters in length. |   |
|   |   |   |   |   |   | ! # $ % ^ & * ( ) + _ |
|   |   |   |   |   | - = #$%^&*() +-= _ |   |
| DBInstanceId | String | Yes |   | dds-bpxxxxxxxx | The ID of the instance. |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 06CBD06E-ABC9- 4121-AB93- 3C3820B3E7E6 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ResetAccountPassword &AccountName=root &AccountPassword=Ali! 123456 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ResetAccountPasswordResponse>
   <RequestId>06CBD06E-ABC9-4121-AB93-3C3820B3E7E6</RequestId>
</ResetAccountPasswordResponse>
```

`JSON` format `{`

```json
 "RequestId": "06CBD06E-ABC9-4121-AB93-3C3820B3E7E6"
```

`}`

#### 7.7.3 ModifyAccountDescription

You can call this operation to modify the description of the root account of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAccountDe scription | The operation that you want to perform. Set the value to Modif yAccount Descript ion. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AccountDescripti on | String | Yes | superadmin | The description of the account. It cannot start with http:// or https://. The description must start with a letter. It must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and hyphens _ (-). |
| AccountName | String | Yes | root | The name of the account for which you want to modify the description. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 59DE9FC2-7B40- 45CF-9011- 7327A8A771A2 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyAccountDescription &AccountName=root &AccountDescription=superadmin &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RestoreDBInstanceResponse>
   <RequestId>59DE9FC2-7B40-45CF-9011-7327A8A771A2</RequestId>
</RestoreDBInstanceResponse>
```

`JSON` format `{`

```json
 "RequestId": "59DE9FC2-7B40-45CF-9011-7327A8A771A2"
```

`}`

### 7.8 IP whitelists and security groups

#### 7.8.1 DescribeSecurityGroupConfiguration

You can call this operation to view ECS security groups to which an ApsaraDB for MongoDB instance is added. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurityG roupConfiguratio n | The operation that you want to perform. Set the value to DescribeSecurit yGroupConf igurat io n. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of RdsEcsSecurity GroupRel |   | The information list of the ECS security group. |
| RdsEcsSecurity GroupRel |   |   |   |
| NetType | String | vpc | The network type of the ECS security group. Valid values: vpc classic |
| RegionId | String | cn-hangzhou | The region ID of the ECS security group. |
| SecurityGroupId | String | sg-bpxxxxxxxx | The ID of the ECS security group. |
| RequestId | String | 3C4A2494-85C4- 45C5-93CF- 548DB3375193 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeSecurityGroupConfiguration &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Items>
    <RdsEcsSecurityGroupRel>
        <SecurityGroupId>sg-bpxxxxxxxx</SecurityGroupId>
        <RegionId>cn-hangzhou</RegionId>
        <NetType>classic</NetType>
    </RdsEcsSecurityGroupRel>
</Items> <RequestId>D18F5B88-ACA6-470E-9493-384412EDD902</RequestId>
```

`JSON` format `{`

```json
 "Items": {
  "RdsEcsSecurityGroupRel": [
```

`{`

```json
    "SecurityGroupId": "sg-bpxxxxxxxx",
    "RegionId": "cn-hangzhou",
    "NetType": "classic"
```

`}` `]` `},`

```json
 "RequestId": "D18F5B88-ACA6-470E-9493-384412EDD902"
```

`}`

#### 7.8.2 ModifySecurityGroupConfiguration

You can call this operation to modify the ECS Security group that is bound to an ApsaraDB for MongoDB instance. For a sharded cluster instance, the bound ECS security group takes effect only for the mongos node. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySecurityGr oupConfiguration | The operation that you want to perform. Set the value toModif ySecurit yGroupConf igurat i on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| SecurityGroupId | String | Yes | sg-bpxxxxxxxx | The ID of the ECS security group. Not e Only one ECS Security Group can be bound to an instance. You can view the security groups in the specified region by calling theDescribeSecurit yGrou p operation of ECS. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E062C482-1A4B- 469E-938C- 96D28CFAE42E | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifySecurityGroupConfiguration &DBInstanceId=dds-bpxxxxxxxx &SecurityGroupId=sg-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>E062C482-1A4B-469E-938C-96D28CFAE42E</RequestId>
```

`JSON` format `{`

```json
    "RequestId": "E062C482-1A4B-469E-938C-96D28CFAE42E"
```

`}`

#### 7.8.3 DescribeSecurityIps

You can call this operation to view the IP whitelist of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurityI ps | The operation that you want to perform. Set the value to DescribeSecurit yIps. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| SecurityIpGroup s | Array of SecurityIpGroup |   | An array that consists of the information of IP whitelists. |
| SecurityIpGroup |   |   |   |
| SecurityIpGroup Attribute | String | hidden | The attribute of the IP whitelist. This parameter is empty by default. |
| SecurityIpGroup Name | String | default | The name of the whitelist. |
| SecurityIpList | String | 47.xxx.xxx.xx,100.xxx .xxx.0/24 | The IP addresses in the whitelist. |
| SecurityIps | String | 47.xxx.xxx.xx,100.xxx .xxx.0/24 | The IP addresses in the default whitelist. |
| RequestId | String | FC724D23-2962- 479E-ABB1- 606C935AE7FD | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeSecurityIps &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSecurityIpsResponse>
   <SecurityIpGroups>
      <SecurityIpGroup>
         <SecurityIpList>114.xxx.xxx.xx</SecurityIpList>
         <SecurityIpGroupAttribute></SecurityIpGroupAttribute>
         <SecurityIpGroupName>allowserver</SecurityIpGroupName>
      </SecurityIpGroup>
      <SecurityIpGroup>
         <SecurityIpList>47.xxx.xxx.xx,100.xxx.xxx.0/24</SecurityIpList>
         <SecurityIpGroupAttribute></SecurityIpGroupAttribute>
         <SecurityIpGroupName>default</SecurityIpGroupName>
      </SecurityIpGroup>
   </SecurityIpGroups>
   <SecurityIps>47.xxx.xxx.xx,100.xxx.xxx.0/24</SecurityIps>
   <RequestId>FC724D23-2962-479E-ABB1-606C935AE7FD</RequestId>
</DescribeSecurityIpsResponse>
```

`JSON` format `{`

```json
 "SecurityIpGroups": {
  "SecurityIpGroup": [
```

`{`

```json
    "SecurityIpList": "114.xxx.xxx.xx",
    "SecurityIpGroupAttribute": "",
    "SecurityIpGroupName": "allowserver"
```

`},` `{`

```json
    "SecurityIpList": "47.xxx.xxx.xx,100.xxx.xxx.0/24",
    "SecurityIpGroupAttribute": "",
    "SecurityIpGroupName": "default"
```

`}` `]` `},`

```json
 "SecurityIps": "47.xxx.xxx.xx,100.xxx.xxx.0/24",
 "RequestId": "FC724D23-2962-479E-ABB1-606C935AE7FD"
```

`}`

#### 7.8.4 ModifySecurityIps

You can call this operation to modify the IP whitelist of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySecurityIps | The operation that you want to perform. Set the value to Modif ySecurit yIps. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| SecurityIps | String | Yes | 10.23.12.24/24,1 0.22.22.22 | The IP addresses in an IP whitelist. Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to a whitelist. You can add IP addresses in one of the following two formats: IP addresses. Example: 10.23.12.24. Classless Inter-Domain Routing (CIDR) blocks, such as 10.23.12.24/24. /24 indicates the length of the IP address prefix in the CIDR block. An IP address prefix can contain 1 to 32 bits. |
| ModifyMode | String | No | Append | The method of modification. Valid values: Cover: overwrites the whitelist. Append: appends data to the whitelist. Delet e: deletes the whitelist. The default value is Cover. |
| SecurityIpGroupN ame | String | No | allowserver | The name of the IP whitelist to be modified. The default value is def ault . |
| SecurityIpGroupAt tribute | String | No | test | The attributes of an IP whitelist. It can contain a maximum of 120 characters in length and can contain uppercase letters, lowercase letters, and digits. This parameter is empty by default. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 61B05CCF-EBAB- 4BF3-BA67- D77256A721E2 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifySecurityIps &SecurityIps=10.23.12.24/24,10.22.22.22 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifySecurityIpsResponse>
   <RequestId>61B05CCF-EBAB-4BF3-BA67-D77256A721E2</RequestId>
</ModifySecurityIpsResponse>
```

`JSON` format `{`

```json
 "RequestId": "61B05CCF-EBAB-4BF3-BA67-D77256A721E2"
```

`}`

### 7.9 Key management

#### 7.9.1 DescribeDBInstanceTDEInfo

You can call this operation to view whether TDE is enabled for an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: A replica set or sharded cluster instance is used. The storage engine of the instance is WiredTiger. The database engine version of the instance is 4.0 or 4.2. If the database engine version of your instance is earlier than 4.0, you can call the UpgradeDBInst anceEngineVersion operation to upgrade the database engine. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceTDEInfo | The operation that you want to perform. Set the value to DescribeDBInst anceT DEInf o. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F4DD0E29-361B- 42F2-9301- B0048CCCE5D6 | The ID of the request. |
| TDEStatus | String | enabled | The TDE status. Valid values: enabled disabled |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeDBInstanceTDEInfo &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TDEStatus>enabled</TDEStatus> <RequestId>F4DD0E29-361B-42F2-9301-B0048CCCE5D6</RequestId>
```

`JSON` format `{`

```json
    "TDEStatus":"enabled",
    "RequestId":"F4DD0E29-361B-42F2-9301-B0048CCCE5D6"
```

`}`

#### 7.9.2 ModifyDBInstanceTDE

You can call this operation to modify the transparent data encryption (TDE) status of an ApsaraDB for MongoDB instance. Before data files are written to disks, transparent data encryption (TDE) encrypts the data files. When data files are loaded from disks to the memory, TDE decrypts the data files. After TDE is enabled, it cannot be disabled. Before you call this operation, make sure that the following requirements are met: A replica set or sharded cluster instance is used. The storage engine of the instance is WiredTiger. The database engine version of the instance is 4.0 or 4.2. If the database engine version is earlier than 4.0, you can call the UpgradeDBInst anceEngineVersion operation to upgrade the database engine. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance TDE | The operation that you want to perform. Set the value to Modif yDBInst anceT DE. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| TDEStatus | String | Yes | enabled | The TDE status. Set the value to Enabled. Not e After TDE is enabled, it cannot be disabled. Proceed with caution. |
| EncryptorName | String | No | aes-256-cbc | The encryption method. Set the value to aes-256-cbc. Not e This parameter is valid only when you set the T EDSt at us parameter to enabled. |
| EncryptionKey | String | No | 749c1df7-xxxx- xxxx-xxxx- xxxxxxxxxxxx | The custom key. |

| Parameter | Type |   | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
| RoleARN | String |   |   |   | The ARN of the role. It is in the format of acs:ram::$accountID:role/$roleN ame . Not e $accountID : indicates the ID of the Alibaba Cloud account that owns the RAM role. To view the account ID, log on to the Alibaba Cloud Management Console, move your pointer over your profile picture in the upper-right corner, and then click Security Settings. $roleName : indicates the name of the RAM role. To view the RAM role name, perform the following steps: Log on to the RAM console. In the left-side navigation pane, click RAM Roles. In the RAM Role Name column on the page that appears, you can view the name of the RAM role. |   |   |
|   |   |   |   |   |   | acs:ram::$accountID:role/$roleN |   |
|   |   |   |   |   | ame |   |   |
|   |   |   | No | acs:ram::123456 789012****:role/ adminrole |   |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 434D7127-6229- 4355-BA50- 7A3685A725DF | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceTDE &DBInstanceId=dds-bpxxxxxxxx &TDEStatus=enabled &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceTDEResponse>
   <RequestId>434D7127-6229-4355-BA50-7A3685A725DF</RequestId>
</ModifyDBInstanceTDEResponse>
```

`JSON` format `{`

```json
 "RequestId": "434D7127-6229-4355-BA50-7A3685A725DF"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectDBInstanceS tate | Current DB instance state does not support this operation. | The error message returned because the operation is not supported while the instance is in its current state. Check whether the specified parameters are correct. |
| 403 | IncorrectDBInstanceL ockMode | Current DB instance lock mode does not support this operation. | The error message returned because the instance is locked. |

### 7.10 SSL encryption

#### 7.10.1 ModifyDBInstanceSSL

You can call this operation to modify the SSL settings of an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. A replica set instance is used. The database engine version of the instance is 3.4, 4.0, or 4.2. Whenever you enable or disable SSL encryption, or update the SSL certificate, the instance will restart. We recommend that you call this operation during off-peak hours. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstance SSL | The operation that you want to perform. Set the value to DescribeDBInst anceSSL. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SSLAction | String | Yes | Open | The operation that you perform for the SSL feature. Valid values: Open: enables SSL encryption. Close: disables SSL encryption. Updat e: updates the SSL certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6D806B11-078F- 4154-BF9F- 844F56D08964 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceSSL &DBInstanceId=dds-bpxxxxxxxx &SSLAction=Open &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceSSLResponse>
   <RequestId>6D806B11-078F-4154-BF9F-844F56D08964</RequestId>
</ModifyDBInstanceSSLResponse>
```

`JSON` format `{`

```json
 "RequestId": "6D806B11-078F-4154-BF9F-844F56D08964"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectDBInstanceS tate | Current DB instance state does not support this operation. | The error message returned because the operation is not supported while the instance is in its current state. Check whether the specified parameters are correct. |
| 403 | IncorrectDBInstanceL ockMode | Current DB instance lock mode does not support this operation. | The error message returned because the instance is locked. |

#### 7.10.2 DescribeDBInstanceSSL

You can call this operation to view the SSL settings of an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: The primary instance must be in the Running state. A replica set instance is used. The database engine version of the instance is 3.4, 4.0, or 4.2. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceSSL | The operation that you want to perform. Set the value to DescribeDBInst anceSSL. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| SSLExpiredTime | String | 2020-03- 11T02:28:25Z | The time when the SSL certificate expires. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| RequestId | String | 36BB1BC2-789C- 4BBA-A519- C5B388E4B0D4 | The ID of the request. |
| SSLStatus | String | Open | The status of the SSL feature. Valid values: Open: The SSL feature is enabled. Closed: The SSL feature is disabled. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CertCommonNa me | String | dds- bpxxxxxxxx.mongod b.rds.example.com | The name of the SSL certificate. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeDBInstanceSSL &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceSSLResponse>
   <SSLExpiredTime>2020-03-11T02:28:25Z</SSLExpiredTime>
   <RequestId>36BB1BC2-789C-4BBA-A519-C5B388E4B0D4</RequestId>
   <SSLStatus>Open</SSLStatus>
   <CertCommonName>dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com</CertCommonName>
</DescribeDBInstanceSSLResponse>
```

`JSON` format `{`

```json
    "SSLExpiredTime":"2020-03-11T02:28:25Z",
    "SSLStatus":"Open",
    "RequestId":"36BB1BC2-789C-4BBA-A519-C5B388E4B0D4",
    "CertCommonName":"dds-bpxxxxxxxx.mongodb.rds.example.com"
```

`}`

### 7.11 Audit logs

#### 7.11.1 DescribeAuditRecords

You can call this operation to view the audit logs of ApsaraDB for MongoDB instances. When you call this operation, ensure that the audit log feature of the instance is enabled. Otherwise, the operation returns an empty audit log. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditRec ords | The operation that you want to perform. Set the value to DescribeAudit Records. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| EndTime | String | Yes | 2019-03- 13T13:11:14Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. |
| StartTime | String | Yes | 2019-03- 13T12:11:14Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the sharded cluster instance. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |
| Database | String | No | testdatabase | The name of the database. If you do not specify this parameter, this operation returns audit logs of all databases. |
| User | String | No | root | The account of the database. If you do not specify this parameter, this operation returns audit logs of all accounts. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Form | String | No | Stream | The form of the audit log entry returend. Valid values: File: returns a log file. If this parameter is set to File, only common parameters are returned. In this case, you must call the DescribeAudit Files operation to view the download URL of the log file. St ream: returns data streams. Default value: St ream. |
| QueryKeywords | String | No | slow | The keywords used for a query. Separate multiple keywords with spaces. You can specify a maximum of 10 keywords. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| OrderType | String | No | asc | The order of time in which the log entries to return are sorted. Valid values: asc: The log entries are sorted by time in ascending order. desc: The log entries are sorted by time in descending order. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of SQLRecord |   | An array that consists of the information of the audit log entries. |
| SQLRecord |   |   |   |
| AccountName | String | root | The account of the database. |

| eveloper Guide·AP | I Reference |   | ApsaraDB for MongoD |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBName | String | test123 | The name of the database. |
| ExecuteTime | String | 2019-03- 11T03:30:27Z | The time when the statement was executed. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| HostAddress | String | 11.xxx.xxx.xxx | The IP address of the client. |
| ReturnRowCoun ts | Long | 2 | The number of entries returned. |
| Syntax | String | { \"atype\" : \"createCollection\" , \"param\" : { \"ns\" : \"123.test1\" }, \"result\": \"OK\" } | The statement that was executed. |
| TableName | String | C1 | The name of the collection. |
| ThreadID | String | 140682188297984 | The ID of the thread. |
| TotalExecution Times | Long | 700 | The duration of the statement execution. Unit: microseconds. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 30 | The maximum number of records on the current page. |
| RequestId | String | 3278BEB8-503B- 4E46-8F7E- D26E040C9769 | The ID of the request. |
| TotalRecordCo unt | Integer | 40 | The total number of entries. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAuditRecords &StartTime=2019-03-13T12:11:14Z &EndTime=2019-03-13T13:11:14Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalRecordCount>40</TotalRecordCount> <PageRecordCount>30</PageRecordCount> <RequestId>3278BEB8-503B-4E46-8F7E-D26E040C9769</RequestId> <PageNumber>1</PageNumber> <Items>
    <TableName>C1</TableName>
    <ThreadID>140682188297984</ThreadID>
    <ExecuteTime>2019-03-11T03:30:27Z</ExecuteTime>
    <ReturnRowCounts>2</ReturnRowCounts>
    <DBName>test123</DBName>
    <TotalExecutionTimes>700</TotalExecutionTimes>
    <Syntax>{ \"atype\" : \"createCollection\", \"param\" : { \"ns\" : \"123.test1\" }, \"r
esult\": \"OK\" }</Syntax>
    <HostAddress>11.xxx.xxx.xxx</HostAddress>
    <AccountName>root</AccountName>
</Items>
```

`JSON` format `{`

```json
    "TotalRecordCount":"40",
    "PageRecordCount":"30",
    "RequestId":"3278BEB8-503B-4E46-8F7E-D26E040C9769",
    "PageNumber":"1",
    "Items":[
```

`{`

```json
            "TableName":"C1",
            "ThreadID":"140682188297984",
            "ExecuteTime":"2019-03-11T03:30:27Z",
            "ReturnRowCounts":"2",
            "DBName":"test123",
            "TotalExecutionTimes":"700",
            "Syntax":"{ \\\"atype\\\" : \\\"createCollection\\\", \\\"param\\\" : { \\\"ns\
\\" : \\\"123.test1\\\" }, \\\"result\\\": \\\"OK\\\" }",
            "HostAddress":"11.xxx.xxx.xxx",
            "AccountName":"root"
```

`}` `]` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidEndTime.Form at | Specified end time is not valid. | The error message returned when the end time is invalid. Check the format of the specified time. |

#### 7.11.2 DescribeAuditFiles

You can call this operation to view the audit log files of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditFile s | The operation that you want to perform. Set the value to DescribeAudit Files. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the specified cluster instance. Not e If you do not specify this parameter, the audit logs of all mongos and shard nodes will be returned. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of LogFile |   | An array that consists of the information of audit log files. |
| LogFile |   |   |   |
| FileID | Integer | 406505 | The ID of the file. |
| LogDownloadU RL | String | http://xxxxxxxx.oss -cn- hangzhou.aliyuncs.c om/custinsxxxxxx/c ustinsxxxxxx xxxxxx. _ csv | The download URL for audit log files. Not e If the download URL is unavailable, this parameter is empty. |
| LogEndTime | String | 2019-03- 12T09:23:15Z | The end of the time range for the audit log files displayed. The time is in the yyyy-MM- ddTHH:mmZ format. The time is displayed in UTC. |
| LogSize | Long | 98 | The size of the audit log file. Unit: bytes. |
| LogStartTime | String | 2019-03- 11T08:19:29Z | The beginning of the time range for the audit log files displayed. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| LogStatus | String | Success | The status of the audit log file. Success: The audit log file is archived. Failed: The audit log file failed to be archived. Generat ing: The audit log file is being archived. Init ializing: Archiving is not started. |
| PageNumber | Integer | 1 | The page number of the page returned. |
| PageRecordCou nt | Integer | 1 | The number of entries on the current page. |
| RequestId | String | F8CA8312-530A- 413A-9129- F2BB32A8D404 | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalRecordCo unt | Integer | 1 | The total number of entries. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAuditFiles &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAuditFilesResponse>
   <Items>
      <LogFile>
         <LogStartTime>2019-03-11T08:19:29Z</LogStartTime>
         <LogEndTime>2019-03-12T09:23:15Z</LogEndTime>
         <LogStatus>Success</LogStatus>
         <FileID>406505</FileID>
         <LogDownloadURL>http://xxxxxxxx.oss-cn-hangzhou.aliyuncs.com/custinsxxxxxx/custins
xxxxxx_xxxxxx.csv</LogDownloadURL>
         <LogSize>98</LogSize>
      </LogFile>
   </Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>1</TotalRecordCount>
   <RequestId>F8CA8312-530A-413A-9129-F2BB32A8D404</RequestId>
   <PageRecordCount>1</PageRecordCount>
</DescribeAuditFilesResponse>
```

`JSON` format `{`

```json
 "Items": {
  "LogFile": [
```

`{`

```json
    "LogStartTime": "2019-03-11T08:19:29Z",
    "LogEndTime": "2019-03-12T09:23:15Z",
    "LogStatus": "Success",
    "FileID": 406505,
    "LogDownloadURL": "http://xxxxxxxx.oss-cn-hangzhou.aliyuncs.com/custinsxxxxxx/custinsxx
xxxx_xxxxxx.csv",
    "LogSize": 98
```

`}` `]` `},`

```json
 "PageNumber": 1,
 "TotalRecordCount": 1,
 "RequestId": "F8CA8312-530A-413A-9129-F2BB32A8D404",
 "PageRecordCount": 1
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidDBInstanceCla ss.NotFound | Specified DB instance class is not found. | The error message returned because the specified instance type does not exist. Verify the specified instance type. |
| 403 | IncorrectDBInstance Type | Current DB instance type does not support this operation. | The error message returned because the operation is not supported by the current instance type. |

#### 7.11.3 DescribeAuditPolicy

You can call this operation to view whether the log audit feature is enabled for an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditPoli cy | The operation that you want to perform. Set the value to DescribeAudit Policy. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogAuditStatus | String | Enable | The status of the log audit feature. Valid values: Enable Disabled Default value: Disabled. |
| RequestId | String | 111E7B16-0A87- 4CBA-B271- F34AD61E099F | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAuditPolicy &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAuditPolicyResponse>
   <LogAuditStatus>Enable</LogAuditStatus>
   <RequestId>111E7B16-0A87-4CBA-B271-F34AD61E099F</RequestId>
</DescribeAuditPolicyResponse>
```

`JSON` format `{`

```json
 "LogAuditStatus": "Enable",
 "RequestId": "111E7B16-0A87-4CBA-B271-F34AD61E099F"
```

`}`

#### 7.11.4 ModifyAuditLogFilter

You can call this operation to modify the type of audit logs to be collected from ApsaraDB for MongoDB instances. The instance must be in the running state when you call this operation. This operation is applicable only to replica set instances, but not to sharded cluster instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAuditLogFi lter | The operation that you want to perform. Set the value to Modif yAudit LogFilt er. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| Filter | String | Yes | insert,query,upda te,delete | The type of the audit log entries to be collected. Valid values: admin: O&M and management operations slow: slow queries query: query operations insert : insert operations updat e: update operations delet e: delete operations command: protocol commands such as the aggregate method |
| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E209BE2B-F264- 4B9D-81F6- A5A5FB1FBF28 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyAuditLogFilter &Filter=insert,query,update,delete &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyAuditLogFilterResponse>
   <RequestId>E209BE2B-F264-4B9D-81F6-A5A5FB1FBF28</RequestId>
</ModifyAuditLogFilterResponse>
```

`JSON` format `{`

```json
 "RequestId": "E209BE2B-F264-4B9D-81F6-A5A5FB1FBF28"
```

`}`

#### 7.11.5 DescribeAuditLogFilter

You can call this operation to view the types of audit logs collected from ApsaraDB for MongoDB instances. The instance must be in the running state when you call this operation. This operation is applicable only to replica set instances, but not to sharded cluster instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditLog Filter | The operation that you want to perform. Set the value to DescribeAudit LogFilt er. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Filter | String | admin,slow,insert,q uery,update,delete, command | The type of the audit log entries. Valid values: admin: O&M and management operations slow: slow queries query: query operations insert : insert operations updat e: update operations delet e: delete operations command: protocol commands such as the aggregate method |
| RequestId | String | D7C8BA0C-9350- 487D-9B70- D69AF27FB1EB | The ID of the request. |
| RoleType | String | primary | The role of the node. |

Examples Sample requests

```
http(s)://mongodb.aliyuncs.com/? Action=DescribeAuditLogFilter &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAuditLogFilterResponse>
   <Filter>admin,slow,insert,query,update,delete,command</Filter>
   <RoleType></RoleType>
   <RequestId>D7C8BA0C-9350-487D-9B70-D69AF27FB1EB</RequestId>
</DescribeAuditLogFilterResponse>
```

`JSON` format `{`

```json
 "Filter": "admin,slow,insert,query,update,delete,command",
 "RoleType": "",
 "RequestId": "D7C8BA0C-9350-487D-9B70-D69AF27FB1EB"
```

`}`

#### 7.11.6 ModifyAuditPolicy

You can call this operation to enable or disable the audit log feature or set the retention period of audit logs for an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAuditPolicy | The operation that you want to perform. Set the value to Modif yAudit Policy. |
| AuditStatus | String | Yes | enable | The status of the audit log feature. Valid values: enable disabled |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| StoragePeriod | Integer | No | 30 | The retention period of audit logs. Unit: day. Valid values: 1 to 30. Default value: 30. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DC04D812-F18D- 4568-9B88- F260D9590116 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyAuditPolicy &AuditStatus=enable &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyAuditPolicyResponse>
   <RequestId>DC04D812-F18D-4568-9B88-F260D9590116</RequestId>
</ModifyAuditPolicyResponse>
```

`JSON` format `{`

```json
 "RequestId": "DC04D812-F18D-4568-9B88-F260D9590116"
```

`}`

### 7.12 Log management

#### 7.12.1 DescribeSlowLogRecords

You can call this operation to view the slow operation log details of the ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSlowLog Records | The operation that you want to perform. Set the value to DescribeSlowLogRecords. |
| StartTime | String | Yes | 2019-02- 24T12:10Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-02- 26T12:10Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy- MM-ddTHH:mmZ format. The time must be in UTC. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard. Not e This parameter is only valid when you set the DBInst anceId parameter to the ID of a sharded cluster instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBName | String | No | mongodbtest | The name of the database. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 to 100. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| OrderType | String | No | asc | The order of time in which the log entries to return are sorted. Valid values: asc: The log entries are sorted by time in ascending order. desc: The log entries are sorted by time in descending order. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MongoDB | The database engine. |
| Items | Array of LogRecords |   | An array that consists of the information of operational log entries. |
| LogRecords |   |   |   |
| AccountName | String | root | The name of the user who performed the operation. |
| DBName | String | mongodbtest | The name of the database. |
| DocsExamined | Long | 1000000 | The number of documents scanned during the operation. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ExecutionStartT ime | String | 2019-02- 25T01:41:28Z | The start time of the operation. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. |
| HostAddress | String | 47.xxx.xxx.xx | The host IP address that you use to connect to a database. |
| KeysExamined | Long | 0 | The data records that are scanned during indexing. |
| QueryTimes | String | 600 | The execution duration of the statement. Unit: milliseconds. |
| ReturnRowCoun ts | Long | 0 | The number of entries returned. |
| SQLText | String | {\"op\":\"query\",\" ns\":\"mongodbtes t.customer\",\"quer y\": {\"find\":\"custome r\",\"filter\": {\"name\":\"jack\"}}} | The SQL statement that is executed during the slow query operation. |
| TableName | String | C1 | The name of the collection. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 1 | The number of slow query log entries returned on the page. |
| RequestId | String | 414A4E5-4C36- 4461-95FC- 23757A20B5F8 | The ID of the request. |
| TotalRecordCo unt | Integer | 1 | The total number of entries. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeSlowLogRecords &StartTime=2019-02-24T12:10Z &EndTime=2019-02-26T12:10Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalRecordCount>1</TotalRecordCount> <PageRecordCount>1</PageRecordCount> <RequestId>414A4E5-4C36-4461-95FC-23757A20B5F8</RequestId> <PageNumber>1</PageNumber> <Items>
    <LogRecords>
        <TableName>C1</TableName>
        <QueryTimes>600</QueryTimes>
        <ExecutionStartTime>2019-02-25T01:41:28Z</ExecutionStartTime>
        <ReturnRowCounts>0</ReturnRowCounts>
        <KeysExamined>0</KeysExamined>
        <DBName>mongodbtest</DBName>
        <DocsExamined>1000000</DocsExamined>
        <HostAddress>47.xxx.xxx.xx</HostAddress>
        <AccountName>root</AccountName>
        <SQLText>{\"op\":\"query\",\"ns\":\"mongodbtest.customer\",\"query\":{\"find\":\"cu
stomer\",\"filter\":{\"name\":\"jack\"}}}</SQLText>
    </LogRecords>
</Items> <Engine>MongoDB</Engine>
```

`JSON` format `{`

```json
 "TotalRecordCount": "1",
 "PageRecordCount": "1",
 "RequestId": "414A4E5-4C36-4461-95FC-23757A20B5F8",
 "PageNumber": "1",
 "Items": {
  "LogRecords": [{
   "TableName": "C1",
   "QueryTimes": "600",
   "ExecutionStartTime": "2019-02-25T01:41:28Z",
   "ReturnRowCounts": "0",
   "KeysExamined": "0",
   "DBName": "mongodbtest",
   "DocsExamined": "1000000",
   "HostAddress": "47.xxx.xxx.xx",
   "AccountName": "root",
   "SQLText": "{\\\"op\\\":\\\"query\\\",\\\"ns\\\":\\\"mongodbtest.customer\\\",\\\"query\
\\":{\\\"find\\\":\\\"customer\\\",\\\"filter\\\":{\\\"name\\\":\\\"jack\\\"}}}"
```

`}]` `},`

```json
 "Engine": "MongoDB"
```

`}`

#### 7.12.2 DescribeErrorLogRecords

You can call this operation to view the error logs of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeErrorLog Records | The operation that you want to perform. Set the value to DescribeErrorLogRecords. |
| StartTime | String | Yes | 2019-01- 01T12:10Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-01- 02T12:10Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy- MM-ddTHH:mmZ format. The time must be in UTC. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you specify this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the sharded cluster instance. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |
| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary Not e If you set NodeId to the ID of a mongos node, the value of this parameter must be primary. |
| DBName | String | No | mongodbtest | The name of the database. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 to 100 |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MongoDB | The database engine. |
| Items | Array of LogRecords |   | An array that consists of the information of log entries. |
| LogRecords |   |   |   |
| Category | String | NETWORK | The category of the log entry. |
| ConnInfo | String | conn18xxxxxx | The log connection information. |
| Content | String | xxxxxxxx | The content of the log entry. |
| CreateTime | String | 2019-02- 26T12:09:34Z | The time when the log entry was generated. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Id | Integer | 1111111111 | The ID of the log entry. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCou nt | Integer | 1 | The number of entries returned on each page. |
| RequestId | String | 68BCBEC2-1E66- 471F-A1A8- E3C60C0A80B0 | The ID of the request. |
| TotalRecordCo unt | Integer | 1 | The total number of entries. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeErrorLogRecords &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeErrorLogRecordsResponse>
   <Items>
      <LogRecords>
         <Category>NETWORK</Category>
         <CreateTime>2019-02-26T12:09:34Z</CreateTime>
         <ConnInfo>conn18xxxxxx</ConnInfo>
         <Content>xxxxxxxx</Content>
      </LogRecords>
   </Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>2</TotalRecordCount>
   <RequestId>68BCBEC2-1E66-471F-A1A8-E3C60C0A80B0</RequestId>
</DescribeErrorLogRecordsResponse>
```

`JSON` format `{`

```json
    "TotalRecordCount":"1",
    "PageRecordCount":"1",
    "RequestId":"68BCBEC2-1E66-471F-A1A8-E3C60C0A80B0",
    "PageNumber":"1",
    "Items":{
        "LogRecords":[
```

`{`

```json
                "ConnInfo":"conn18xxxxxx",
                "Category":"NETWORK",
                "Id":"1111111111",
                "Content":"xxxxxxxx",
                "CreateTime":"2019-02-26T12:09:34Z"
```

`}` `]`

```
    },"Engine":"MongoDB"
```

`}`

#### 7.12.3 DescribeRunningLogRecords

You can call this operation to view the operational logs of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRunningL ogRecords | The operation that you want to perform. Set the value to DescribeRunningLogRecords. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StartTime | String | Yes | 2019-01- 01T12:10Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-01- 02T12:10Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy- MM-ddTHH:mmZ format. The time must be in UTC. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the sharded cluster instance. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |
| DBName | String | No | mongodbtest | The name of the database. |
| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary Not e If you set NodeId to the ID of a mongos node, the value of RoleT ype must be primary. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 to 100 |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| OrderType | String | No | asc | The order of time in which the log entries to return are sorted. Valid values: asc: The log entries are sorted by time in ascending order. desc: The log entries are sorted by time in descending order. |
| ResourceGroupId | String | No | rg-axxxxxxx | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MongoDB | The database engine. |
| Items | Array of LogRecords |   | An array that consists of the information of log entries. |
| LogRecords |   |   |   |
| Category | String | NETWORK | The category of the log entry. |
| ConnInfo | String | conn18xxxxxx | The log connection information. |
| Content | String | end connection 11.xxx.xxx.xx:3xxxx (0 connections now open)\n | The content of the log entry. |
| CreateTime | String | 2019-02- 26T12:09:34Z | The time when the log entry was generated. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Id | Integer | 1111111111 | The ID of the log entry. |

| A | psaraDB for Mong | oDB |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the page returned. |
| PageRecordCou nt | Integer | 30 | The number of entries returned on each page. |
| RequestId | String | 45D2B592-DEBA- 4347-BBF3- 47FF6C97DBBC | The ID of the request. |
| TotalRecordCo unt | Integer | 2 | The total number of entries. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeRunningLogRecords &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRunningLogRecordsResponse>
   <Items>
      <LogRecords>
         <Category>-</Category>
         <CreateTime>2019-02-26T12:09:34Z</CreateTime>
         <ConnInfo>conn18xxxxxx</ConnInfo>
         <Content>
    end connection 11.xxx.xxx.xx:3xxxx (0 connections now open)
   </Content>
      </LogRecords>
      <LogRecords>
         <Category>NETWORK</Category>
         <CreateTime>2019-02-26T12:09:34Z</CreateTime>
         <ConnInfo>thread1</ConnInfo>
         <Content>connection accepted from 11.xxx.xxx.xx:3xxxx #1862051 (11 connections now
open)</Content>
      </LogRecords>
   </Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>2</TotalRecordCount>
   <RequestId>45D2B592-DEBA-4347-BBF3-47FF6C97DBBC</RequestId>
</DescribeRunningLogRecordsResponse>
```

`JSON` format `{`

```json
    "Items": {
        "LogRecords": [
```

`{`

```json
                "Category": "-",
                "CreateTime": "2019-02-26T12:09:34Z",
                "ConnInfo": "conn18xxxxxx",
                "Content": "end connection 11.xxx.xxx.xx:3xxxx (0 connections now open)\n"
```

`},` `{`

```json
                "Category": "NETWORK",
                "CreateTime": "2019-02-26T12:09:34Z",
                "ConnInfo": "thread1",
                "Content": "connection accepted from 11.xxx.xxx.xx:3xxxx #1862051 (11 conne
ctions now open)"
```

`}` `]` `},`

```json
    "PageNumber": 1,
    "TotalRecordCount": 2,
    "RequestId": "45D2B592-DEBA-4347-BBF3-47FF6C97DBBC"
```

`}`

### 7.13 Performance monitoring management

management

#### 7.13.1 DescribeDBInstancePerformance

You can call this operation to view the performance data of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan cePerformance | The operation that you want to perform. Set the value to DescribeDBInst ancePerf ormance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Key | String | Yes | MongoDB Detaile _ dSpaceUsage | The performance metric. Valid values: CpuUsage: the CPU utilization percentage MemoryUsage: the memory usage percentage MongoDB IOPS: the IOPS usage _ IOPSUsage: the IOPS usage percentage. MongoDB Det ailedSpaceUsage: _ the disk usage. DiskUsage : the disk usage percentage MongoDB Opcount ers : the _ operation QPS MongoDB Connect ions : the _ number of connections MongoDB Cursors : the number of _ cursors MongoDB Net work : the network _ traffic MongoDB Global Lock Current _ _ _ _ Queue : the global lock waiting queues MongoDB Wt Cache : the _ _ WiredTiger storage Not e Separate multiple metrics with commas (,). |
| StartTime | String | Yes | 2019-03- 11T12:30Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-03- 11T12:30Z | The end of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in a sharded cluster instance. You can specify this parameter to view the performance of a single node. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |
| ReplicaSetRole | String | No | Primary | The role of the node. Valid values: Primary Secondary Not e If you set the DBInst anceId parameter to the ID of a standalone instance, the value of this parameter can only be Primary. |
| RoleId | String | No | 60xxxxx | The role ID of a node in a instance. You can call the DescribeReplicaSet Role operation to view role IDs. Not e This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 267F98DC-367D- 4F20-B137- 8B5B664D1C5D | The ID of the request. |

| psaraDB for Mong | oDB |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| StartTime | String | 2019-03-11T12:20Z | The beginning of the time range to query. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| EndTime | String | 2019-03-11T12:30Z | The beginning of the time range to query. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| PerformanceKe ys | Array of PerformanceKe y |   | An array that consists of the information of performance metrics. |
| PerformanceKe y |   |   |   |
| Key | String | MongoDB DetailedS _ paceUsage | Performance metric. |
| PerformanceVa lues | Array of PerformanceVa lue |   | An array that consists of the values of performance metrics. |
| PerformanceVa lue |   |   |   |
| Date | String | 2019-03- 11T12:21:51Z | The date and time when the value is generated. |
| Value | String | 0.6 | The value of a performance metric. |
| Unit | String | MB | The unit of the performance metric. |
| ValueFormat | String | cpu usage _ | The format of the performance metric value. If the performance metric contains multiple fields, the fields are separated with ampersands (& ). For example, if you query disk usage, the returned ValueFormat is ins size& amp;dat a size& amp;log size. _ _ _ |
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MongoDB | The database engine. It is fixed to MongoDB. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeDBInstancePerformance &Key=MongoDB_DetailedSpaceUsage &StartTime=2019-03-11T12:30Z &EndTime=2019-03-11T12:30Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PerformanceKeys>
    <ValueFormat>cpu_usage</ValueFormat>
    <Unit>MB</Unit>
    <Key>MongoDB_DetailedSpaceUsage</Key>
</PerformanceKeys> <PerformanceKeys>
    <PerformanceValues>
        <Value>0.6</Value>
        <Date>2019-03-11T12:21:51Z</Date>
    </PerformanceValues>
</PerformanceKeys> <EndTime>2019-03-11T12:30Z</EndTime> <RequestId>267F98DC-367D-4F20-B137-8B5B664D1C5D</RequestId> <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId> <StartTime>2019-03-11T12:20Z</StartTime> <Engine>MongoDB</Engine>
```

`JSON` format `{`

```json
    "PerformanceKeys":[
```

`{`

```json
            "ValueFormat":"cpu_usage",
            "Unit":"MB",
            "Key":"MongoDB_DetailedSpaceUsage"
```

`},` `{`

```json
            "PerformanceValues":[
```

`{`

```json
                    "Value":"0.6",
                    "Date":"2019-03-11T12:21:51Z"
```

`}` `]` `}` `],`

```json
    "EndTime":"2019-03-11T12:30Z",
    "RequestId":"267F98DC-367D-4F20-B137-8B5B664D1C5D",
    "DBInstanceId":"dds-bpxxxxxxxx",
    "StartTime":"2019-03-11T12:20Z",
    "Engine":"MongoDB"
```

`}`

#### 7.13.2 DescribeDBInstanceMonitor

You can call this operation to set the collection frequency of monitoring data for an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstan ceMonitor | The operation that you want to perform. Set the value to DescribeDBInst anceMonit or. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Granularity | String | 300 | The collection frequency of monitoring data. The value is fixed to 300 . Unit: seconds. |
| RequestId | String | EFD65226-08CC- 4C4D-B6A4- CB3C382F67B0 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeDBInstanceMonitor &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Granularity>300</Granularity> <RequestId>EFD65226-08CC-4C4D-B6A4-CB3C382F67B0</RequestId>
```

`JSON` format `{`

```json
 "Granularity": 300,
 "RequestId": "EFD65226-08CC-4C4D-B6A4-CB3C382F67B0"
```

`}`

### 7.14 Parameter management

#### 7.14.1 DescribeParameterModificationHistory

You can call this operation to view the parameter modification records of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeParamet erModificationHis tory | The operation that you want to perform. Set the value to DescribeParamet erModif icat ionHis t roy. |
| StartTime | String | Yes | 2019-01- 01T12:10Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-01- 02T12:10Z | The end of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| CharacterType | String | Yes | db | The role of the instance. Valid values: db: the shard node cs: the Configserver node mongos: the mongos node logic: the sharded cluster instance |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard in the specified sharded cluster instance. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeDBInst anceAt t ribut e operation to query the region ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| HistoricalParam eters | Array of HistoricalParam eter |   | An array that consists of the information of parameter modification records. |
| HistoricalParam eter |   |   |   |
| ModifyTime | String | 2019-03- 12T07:58:24Z | The time when the parameter was modified. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| NewParameter Value | String | 200 | The parameter value after modification. |

| Developer Guide·AP | I Reference |   | ApsaraDB for MongoD |
|---|---|---|---|
| Parameter | Type | Example | Description |
| OldParameterV alue | String | 100 | The parameter value before modification. |
| ParameterNam e | String | operationProfiling.sl owOpThresholdMs | The name of the modified parameter. |
| RequestId | String | B1BB6E0E-B4EF- 4145-81FA- A07719860248 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeParameterModificationHistory &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeParameterModificationHistoryResponse>
   <HistoricalParameters>
      <HistoricalParameter>
         <OldParameterValue>100</OldParameterValue>
         <ModifyTime>2019-03-12T07:58:24Z</ModifyTime>
         <NewParameterValue>200</NewParameterValue>
         <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName>
      </HistoricalParameter>
   </HistoricalParameters>
   <RequestId>B1BB6E0E-B4EF-4145-81FA-A07719860248</RequestId>
</DescribeParameterModificationHistoryResponse>
```

`JSON` format `{`

```json
 "HistoricalParameters": {
  "HistoricalParameter": [
```

`{`

```json
    "OldParameterValue": "100",
    "ModifyTime": "2019-03-12T07:58:24Z",
    "NewParameterValue": "200",
    "ParameterName": "operationProfiling.slowOpThresholdMs"
```

`}` `]` `},`

```json
 "RequestId": "B1BB6E0E-B4EF-4145-81FA-A07719860248"
```

`}`

#### 7.14.2 DescribeParameters

You can call this operation to view parameter configurations of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeParamet ers | The operation that you want to perform. Set the value toDescribeParamet ers. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard in the specified sharded cluster instance. Not e This parameter is only valid when you set theDBInst anceIdparameter to the ID of a sharded cluster instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CharacterType | String | No | mongos | The type of the database account. Valid values: mongos: The account that can be used to log on to a mongos node shard: The account that can be used to log on to a shard node |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConfigParamet ers | Array of Parameter |   | An array that consists of the information of configured parameters. |
| Parameter |   |   |   |
| CheckingCode | String | [0-65536] | The valid values of the parameter. |
| ForceRestart | Boolean | true | Indicates whether a restart is required for parameter modifications to take effect. f alse: A restart is not required. Modifications take effect immediately after they are made. t rue: A restart is required for modifications to take effect. |
| ModifiableStat us | Boolean | true | Indicates whether the parameter is modifiable. f alse t rue |
| ParameterDescr iption | String | The threshold in milliseconds at which the database profiler considers a query slow, default is 100. | The description of the parameter. |
| ParameterNam e | String | operationProfiling.sl owOpThresholdMs | The name of the parameter. |
| ParameterValu e | String | 200 | The value of the parameter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3ADD0C7D-2D2A- 4F15-88FF- E7AC9B9FDCC8 | The ID of the request. |
| RunningParame ters | Array of Parameter |   | An array that consists of the information of instance parameters that have taken effect. |
| Parameter |   |   |   |
| CheckingCode | String | [33554432- 268435456] | The valid values of the parameter. |
| ForceRestart | String | false | Indicates whether a restart is required for parameter modifications to take effect. f alse: A restart is not required. Modifications take effect immediately after they are made. t rue: A restart is required for modifications to take effect. |
| ModifiableStat us | String | true | Indicates whether the parameter is modifiable. f alse t rue |
| ParameterDescr iption | String | The maximum memory bytes that sort stage may use, default is 33554432(i.e. 32MB) | The description of the parameter. |
| ParameterNam e | String | setParameter.intern alQueryExecMaxBloc kingSortBytes | The name of the parameter. |
| ParameterValu e | String | 33554432 | The value of the parameter. |
| EngineVersion | String | 4.0 | The engine version of the instance. |
| Engine | String | mongodb | The database engine of the instance. Default value: mongodb. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeParameters &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeParametersResponse>
      <ConfigParameters>
            <Parameter>
                  <ParameterDescription>The threshold in milliseconds at which the database
profiler considers a query slow, default is 100. </ParameterDescription>
                  <ParameterValue>200</ParameterValue>
                  <CheckingCode>[0-65536]</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName>
            </Parameter>
      </ConfigParameters>
      <RequestId>3ADD0C7D-2D2A-4F15-88FF-E7AC9B9FDCC8</RequestId>
      <RunningParameters>
            <Parameter>
                  <ParameterDescription></ParameterDescription>
                  <ParameterValue>zlib</ParameterValue>
                  <CheckingCode>snappy|zlib|disabled</CheckingCode>
                  <ForceRestart>true</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>net.compression.compressors</ParameterName>
            </Parameter>
            <Parameter>
                  <ParameterDescription>The level of database profiling, which inserts info
rmation about operation performance into the system.profile collection. 'off' for no profil ing, 'slowOp' for only includes slow operations, 'all' for includes all operations, default is 'slowOp'. </ParameterDescription>
                  <ParameterValue>slowOp</ParameterValue>
                  <CheckingCode>off|slowOp|all</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>operationProfiling.mode</ParameterName>
            </Parameter>
            <Parameter>
                  <ParameterDescription>The threshold in milliseconds at which the database
profiler considers a query slow, default is 100. </ParameterDescription>
                  <ParameterValue>220</ParameterValue>
                  <CheckingCode>[0-65536]</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName>
            </Parameter>
            <Parameter>
                  <ParameterDescription>The expiration threshold in milliseconds for idle c
ursors before MongoDB removes them; i.e. MongoDB removes cursors that have been idle for th e specified cursorTimeoutMillis. default is 600000(i.e. 10 minutes)</ParameterDescription>
```

`p` `(` `)``/` `p`

```xml
                  <ParameterValue>600000</ParameterValue>
                  <CheckingCode>[1-2147483647]</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>setParameter.cursorTimeoutMillis</ParameterName>
            </Parameter>
            <Parameter>
                  <ParameterDescription>The maximum memory bytes that sort stage may use, d
efault is 33554432(i.e. 32MB)</ParameterDescription>
                  <ParameterValue>33554432</ParameterValue>
                  <CheckingCode>[33554432-268435456]</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>setParameter.internalQueryExecMaxBlockingSortBytes</Parame
terName>
            </Parameter>
      </RunningParameters>
      <EngineVersion>4.0</EngineVersion>
      <Engine>mongodb</Engine>
</DescribeParametersResponse>
```

`JSON` format `{`

```json
    "ConfigParameters": {
        "Parameter": [
```

`{`

```json
                "ParameterDescription": "The threshold in milliseconds at which the databas
e profiler considers a query slow, default is 100.",
                "ParameterValue": "200",
                "CheckingCode": "[0-65536]",
                "ForceRestart": false,
                "ModifiableStatus": true,
                "ParameterName": "operationProfiling.slowOpThresholdMs"
```

`}` `]` `},`

```json
    "RequestId": "3ADD0C7D-2D2A-4F15-88FF-E7AC9B9FDCC8",
    "RunningParameters": {
        "Parameter": [
```

`{`

```json
                "ParameterDescription": "",
                "ParameterValue": "zlib",
                "CheckingCode": "snappy|zlib|disabled",
                "ForceRestart": "true",
                "ModifiableStatus": "true",
                "ParameterName": "net.compression.compressors"
```

`},` `{`

```json
                "ParameterDescription": "The level of database profiling, which inserts inf
ormation about operation performance into the system.profile collection. 'off' for no profi ling, 'slowOp' for only includes slow operations, 'all' for includes all operations, defaul t is 'slowOp'.",
```

`"P` `t` `V``l` `"` `"``l` `O``"`

```json
                "ParameterValue": "slowOp",
                "CheckingCode": "off|slowOp|all",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "operationProfiling.mode"
```

`},` `{`

```json
                "ParameterDescription": "The threshold in milliseconds at which the databas
e profiler considers a query slow, default is 100.",
                "ParameterValue": "220",
                "CheckingCode": "[0-65536]",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "operationProfiling.slowOpThresholdMs"
```

`},` `{`

```json
                "ParameterDescription": "The expiration threshold in milliseconds for idle
cursors before MongoDB removes them; i.e. MongoDB removes cursors that have been idle for t he specified cursorTimeoutMillis. default is 600000(i.e. 10 minutes)",
                "ParameterValue": "600000",
                "CheckingCode": "[1-2147483647]",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "setParameter.cursorTimeoutMillis"
```

`},` `{`

```json
                "ParameterDescription": "The maximum memory bytes that sort stage may use,
default is 33554432(i.e. 32MB)",
                "ParameterValue": "33554432",
                "CheckingCode": "[33554432-268435456]",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "setParameter.internalQueryExecMaxBlockingSortBytes"
```

`}` `]` `},`

```json
    "EngineVersion": "4.0",
    "Engine": "mongodb"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidDBInstanceCla ss.NotFound | Specified DB instance class is not found. | The error message returned when the specified instance type does not exists. Verify the specified instance type. |
| 403 | IncorrectDBInstance Type | Current DB instance type does not support this operation. | The error message returned when the current operation is not supported by the instance type of the specified instance. |

#### 7.14.3 ModifyParameters

You can call this operation to modify the parameters of an AsparaDB for MongoDB instance. The instance must be in the running state when you call this operation. If some of the modified parameters take effect only after the instance is restarted, the instance is automatically restarted after the operation is complete. You can call the DescribeParamet erT emplat es operation to query the parameters that take effect only after the instance is restarted. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyParameter s | The operation that you want to perform. Set the value toModif yParamet ers. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| Parameters | String | Yes | {"operationProfili ng.slowOpThresh oldMs":"300"} | The parameters to be modified and their new values. Set this parameter to a JSON string. For example, set the parameter in the {"name":"value","name":"value2"} format. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the specified sharded cluster instance. Not e This parameter is only valid when you set the DBInst anceId parameter to the ID of a sharded cluster instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CharacterType | String | No | db | The role of the instance. Valid values: db: the shard node cs: the Configserver node mongos: the mongos node logic: the sharded cluster instance |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 36923CC2-DDAB- 4B48-A144- DA92C1E19537 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyParameters &DBInstanceId=dds-bpxxxxxxxx &Parameters={"operationProfiling.slowOpThresholdMs":"300"} &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyParametersResponse>
      <RequestId>36923CC2-DDAB-4B48-A144-DA92C1E19537</RequestId>
</ModifyParametersResponse>
```

`JSON` format `{`

```json
    "RequestId": "36923CC2-DDAB-4B48-A144-DA92C1E19537"
```

`}`

### 7.15 Backup and recovery

#### 7.15.1 DescribeBackupPolicy

You can call this operation to view the backup policy of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackupP olicy | The operation that you want to perform. Set the value to DescribeBackupPolicy. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupRetentio nPeriod | String | 7 | The backup retention period. Unit: days. |
| PreferredBacku pPeriod | String | Monday,Wednesday, Friday,Sunday | The period of backup. Valid values: Monday T uesday T hursday Friday Sat urday Sunday |
| PreferredBacku pTime | String | 20:00Z-21:00Z | The time when the data was backed up. The time is in the HH:mmZ-HH:mmZ format. The time is displayed in UTC. |
| PreferredNextB ackupTime | String | 2020-05-13T22:56Z | The next backup time. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| RequestId | String | C2C283A1-1CC4- 4DD9-B985- 3811E0244A45 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeBackupPolicy DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PreferredBackupPeriod>Monday,Wednesday,Friday,Sunday</PreferredBackupPeriod> <RequestId>C2C283A1-1CC4-4DD9-B985-3811E0244A45</RequestId> <PreferredBackupTime>20:00Z-21:00Z</PreferredBackupTime> <PreferredNextBackupTime>2020-05-13T22:56Z</PreferredNextBackupTime> <BackupRetentionPeriod>7</BackupRetentionPeriod>
```

`JSON` format `{`

```json
    "PreferredBackupPeriod":"Monday,Wednesday,Friday,Sunday",
    "RequestId":"C2C283A1-1CC4-4DD9-B985-3811E0244A45",
    "PreferredBackupTime":"20:00Z-21:00Z",
    "PreferredNextBackupTime":"2020-05-13T22:56Z",
    "BackupRetentionPeriod":"7"
```

`}`

#### 7.15.2 ModifyBackupPolicy

You can call this operation to modify the backup policy of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBackupPoli cy | The operation that you want to perform. Set the value to Modif yBackupPolicy. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| PreferredBackupP eriod | String | Yes | Monday,Wednesd ay,Friday,Sunday | The period of backup. Valid values: Monday T uesday Wednesday T hursday Friday Sat urday Sunday Not e Separate multiple values with commas (,). |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PreferredBackupT ime | String | Yes | 03:00Z-04:00Z | The time to back up data. Specify the time in the HH:mmZ-HH:mmZ format. The time must be in UTC. Not e The maximum period is 1 hour. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 644A359C-B871- 4DD3-97B5- ED91EF5809C2 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyBackupPolicy &DBInstanceId=dds-bpxxxxxxxx &PreferredBackupPeriod=Monday,Wednesday,Friday,Sunday &PreferredBackupTime=03:00Z-04:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyBackupPolicyResponse>
   <RequestId>644A359C-B871-4DD3-97B5-ED91EF5809C2</RequestId>
</ModifyBackupPolicyResponse>
```

`JSON` format `{`

```json
 "RequestId": "644A359C-B871-4DD3-97B5-ED91EF5809C2"
```

`}`

#### 7.15.3 CreateBackup

You can call this operation to manually back up an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBackup | The operation that you want to perform. Set the value to Creat eBackup. |
| DBInstanceId | String | Yes | d-bpxxxxxxxx | The ID of the instance. |
| BackupMethod | String | No | Logical | The backup method of the instance. Default value: Physical. Valid values: Logical Physical |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupId | String | 5664xxxx | The ID of the backup set. |
| RequestId | String | 7016B12F-7F64- 40A4-BAFF- 013F02AC82FC | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=CreateBackup DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateBackupResponse>
   <RequestId>7016B12F-7F64-40A4-BAFF-013F02AC82FC</RequestId>
   <BackupId>5664xxxx</BackupId>
</CreateBackupResponse>
```

`JSON` format `{`

```json
    "RequestId": "7016B12F-7F64-40A4-BAFF-013F02AC82FC",
    "BackupId": "5664xxxx"
```

`}`

#### 7.15.4 DescribeBackups

You can call this operation to view the backups of an ApsaraDB for MongoDB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackups | The operation that you want to perform. Set the value to DescribeBackups. |
| StartTime | String | Yes | 2019-03- 12T12:00Z | The beginning of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-03- 13T12:00Z | The end of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Not e If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard node in the sharded cluster instance. Not e This parameter is valid only if you set the DBInst anceId parameter to the ID of a sharded cluster instance. |
| BackupId | String | No | 12345678 | The ID of the backup set. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 30 | The number of entries returned per page. |
| RequestId | String | 8925E66F-1971- 4C8C-90A7- F93BF1867E25 | The ID of the request. |
| TotalCount | Integer | 1 | The total number of backup sets. |
| Backups | Array of Backup |   | An array that consists of the information of backup sets. |
| Backup |   |   |   |
| BackupDBName s | String | mongodbtest,new,t est | The name of the database that has been backed up. |
| BackupDownlo adURL | String | http://xxxxx.oss- cn- hangzhou.aliyuncs.c om/xxxxx/hinsxxxxx data xxxxx.tar.gz _ _ | The Internet download URL of the backup file. If the download URL is unavailable, this parameter is an empty string. |
| BackupEndTime | String | 2019-03- 13T04:34:57Z | The end of the backup time range. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| BackupId | Integer | 11111111 | The ID of the backup set. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupIntranet DownloadURL | String | http://xxxxx.oss- cn-hangzhou- internal.example.co m/xxxxx/xxxxx.tar.g z | The internal download URL of the backup file. Not e You can download the backup file by using this URL on the Elastic Compute Service (ECS) instance that is connected to the ApsaraDB for MongoDB instance. The ECS instance and ApsaraDB for MongoDB instance must be in the classic network of the same region or in the same virtual private cloud (VPC). |
| BackupMethod | String | Physical | The backup method. Valid values: Snapshot Physical Logical |
| BackupMode | String | Automated | The backup mode. Valid values: Aut omat ed Manual |
| BackupSize | Long | 335520510 | The size of the backup file. Unit: bytes. |
| BackupStartTim e | String | 2019-03- 13T04:32:42Z | The beginning of the backup time range. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| BackupStatus | String | Success | The status of the backup. Valid values: Success: The backup task is successful. Failed: The backup task failed. |
| BackupType | String | FullBackup | The backup type. Valid values: FullBackup: full backup. Increment alBackup: incremental backup. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeBackups &StartTime=2019-03-12T12:00Z &EndTime=2019-03-13T12:00Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>1</TotalCount> <PageSize>30</PageSize> <RequestId>8925E66F-1971-4C8C-90A7-F93BF1867E25</RequestId> <PageNumber>1</PageNumber> <Backups>
    <BackupMethod>Physical</BackupMethod>
    <BackupDownloadURL>http://xxxxx.oss-cn-hangzhou.aliyuncs.com/xxxxx/hinsxxxxx_data_xxxxx
.tar.gz</BackupDownloadURL>
    <BackupIntranetDownloadURL>http://xxxxx.oss-cn-hangzhou-internal.example.com/xxxxx/xxxx
x.tar.gz</BackupIntranetDownloadURL>
    <BackupSize>335520510</BackupSize>
    <BackupMode>Automated</BackupMode>
    <BackupEndTime>2019-03-13T04:34:57Z</BackupEndTime>
    <BackupStartTime>2019-03-13T04:32:42Z</BackupStartTime>
    <BackupType>FullBackup</BackupType>
    <BackupId>11111111</BackupId>
    <BackupDBNames>mongodbtest,new,test</BackupDBNames>
    <BackupStatus>Success</BackupStatus>
</Backups>
```

`JSON` format `{`

```json
    "TotalCount":"1",
    "PageSize":"30",
    "RequestId":"8925E66F-1971-4C8C-90A7-F93BF1867E25",
    "PageNumber":"1",
    "Backups":[
```

`{`

```json
            "BackupMethod":"Physical",
            "BackupDownloadURL":"http://xxxxx.oss-cn-hangzhou.aliyuncs.com/xxxxx/hinsxxxxx_
data_xxxxx.tar.gz",
            "BackupIntranetDownloadURL":"http://xxxxx.oss-cn-hangzhou-internal.example.com/
xxxxx/xxxxx.tar.gz",
            "BackupSize":"335520510",
            "BackupMode":"Automated",
            "BackupEndTime":"2019-03-13T04:34:57Z",
            "BackupStartTime":"2019-03-13T04:32:42Z",
            "BackupType":"FullBackup",
            "BackupId":"11111111",
            "BackupDBNames":"mongodbtest,new,test",
            "BackupStatus":"Success"
```

`}` `]` `}`

#### 7.15.5 RestoreDBInstance

You can call this operation to restore data to the current ApsaraDB for MongoDB instance. This operation is applicable only to replica set instances, but not to standalone instances or sharded cluster instances. You also can use the following methods to clone an instance: Create an instance from a backup to clone a standalone instance. Call the CreateShardingDBInstance operation to clone a sharded cluster instance. This operation overwrites the data of the current instance, and the data cannot be recovered. Proceed with caution. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RestoreDBInstanc e | The operation that you want to perform. Set the value to Rest oreDBInst ance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BackupId | Integer | Yes | 11111111 | The ID of the backup set. Not e You can call the DescribeBackups operation to view the backup ID. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 973DCB8F-56B3- 4102-8777- 3A90495927F7 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=RestoreDBInstance &BackupId=11111111 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RestoreDBInstanceResponse>
   <RequestId>973DCB8F-56B3-4102-8777-3A90495927F7</RequestId>
</RestoreDBInstanceResponse>
```

`JSON` format `{`

```json
 "RequestId": "973DCB8F-56B3-4102-8777-3A90495927F7"
```

`}`

#### 7.15.6 DescribeBackupDBs

You can call this operation to view the databases at a specified time or the databases in a specified backup set before you restore a database for an ApsaraDB for MongoDB instance. You can call the Creat eDBInst ance operation to restore a database for an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: A replica set instance is used. The database engine version of the instance must be 3.0, 3.4, 4.0, or 4.2. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackupD Bs | The operation that you want to perform. Set the value to DescribeBackupDBs. |
| SourceDBInstance | String | Yes | dds-bpxxxxxxxx | The ID of the source instance. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| RestoreTime | String | No | 2019-08- 22T12:00:00Z | The point in time at which the instance will be restored. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Not e It can be any time within the past seven days. The time must be earlier than the current time, but later than the time when the database was created. You must specify either this parameter or the BackupId parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BackupId | String | No | 5664xxxx | The ID of the backup set. Not e You can call the DescribeBackups operation to view the backup ID. You must specify this parameter or the Rest oreT ime parameter. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Databases | Array of Database |   | An array that consists of inforamtion of databases. |
| Database |   |   |   |
| DBName | String | mongodbtest | The name of the database. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| TotalCount | Integer | 5 | The number of databases. |
| PageSize | Integer | 30 | The number of entries returned on each page. |
| RequestId | String | 1AF0AD89-ED4F- 44AD-B65F- BFC1D5CD9455 | The ID of the request. |

Examples Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeBackupDBs &SourceDBInstance=dds-bpxxxxxxxx &RestoreTime=2019-08-22T12:00:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>5</TotalCount> <Databases>
    <DBName>mongodbtest</DBName>
</Databases> <PageSize>30</PageSize> <RequestId>1AF0AD89-ED4F-44AD-B65F-BFC1D5CD9455</RequestId> <PageNumber>1</PageNumber>
```

`JSON` format `{`

```json
    "TotalCount":"5",
    "Databases":[
```

`{`

```json
            "DBName":"mongodbtest"
```

`}` `],`

```json
    "PageSize":"30",
    "RequestId":"1AF0AD89-ED4F-44AD-B65F-BFC1D5CD9455",
    "PageNumber":"1"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectDBInstance Type | Current DB instance type does not support this operation. | The error message returned when the current operation is not supported by the instance type of the specified instance. |

### 7.16 Instance states

This topic descries the instance states of ApsaraDB for MongoDB instances.

| State | Description |
|---|---|
| Creating | The instance is being created. |
| DBInstanceClassChanging | The instance specifications are being changed. |

| eveloper Guide·API Reference | ApsaraDB for MongoD |
|---|---|

| State | Description |
|---|---|
| DBInstanceNetTypeChanging | The network type of the instance is being changed. |
| Deleting | The instance is being deleted. |
| EngineVersionUpgrading | The database engine version of the instance is being upgraded. |
| GuardSwitching | The instance is undergoing a disaster-triggered failover. |
| HASwitching | The instance is undergoing a primary/secondary switching. |
| Importing | Data is being imported into the instance. |
| ImportingFromOthers | A database is being imported into the instance. |
| LinkSwitching | The instance is undergoing a link switching. |
| MinorVersionUpgrading | The minor version of the instance is being upgraded. |
| NET CREATING _ | A network connection to the instance is being created. |
| NET DELETING _ | A network connection to the instance is being deleted. |
| NodeCreating | A node is being created in the instance. |
| NodeDeleting | A node is being deleted in the instance. |
| Rebooting | The instance is being restarted. |
| Restoring | The cluster is being restored from the backup. |
| Running | The cluster is running. |
| SSLModifying | The SSL status of the instance is changing. |
| TempDBInstanceCreating | A node is being deleted in the instance. |
| Transing | The instance is being migrated. |
| TransingToOthers | A database in the instance is being migrated. |

## 8 Appendixes

### 8.1 Call the ASAPI gateway

You can use the Apsara Stack API (ASAPI) gateway to call API operations of most Apsara Stack services. This topic describes how to call API operations by using the ASAPI gateway and provides links to references. Flowchart Procedure
1. Obtain ASAPI SDK.
Before you use ASAPI to call an API operation, you must obtain ASAPI SDK. For more information, see Obtain ASAPI SDK.
2. Obtain the endpoint of ASAPI. For more information, see Obtain the endpoint of ASAPI .
3. Obtain an AccessKey pair.
Obtain the AccessKey pair that is required when you call an API operation. We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services.
4. Obtain the region ID.
Obtain the region ID that is required when you call an API operation.
5. Obtain the organization ID and resource set ID.
You must call an API operation to obtain an organization ID. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management C onsole Developer Guide. You must call an API operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Con sole Developer Guide. When you call an API operation, you can specify the organization ID and resource set ID by using the <x-acs-organizationid> and <x-acs-resourcegroupid> parameters. This allows you to query specified resources. If you do not set the <x-acs-organizationid> parameter, the organization to which the current user belongs is used by default. If you do not set the <x-acs-resourcegroupid> parameter, it is empty by default. If you specify a resource set ID, you must also specify an organization ID.
6. Refer to API references.
Obtain the developer guide of the cloud service that you want to use. You can learn the features of API operations and how to call the API operations. For more information, see Use developer guides.
7. Use ASAPI SDK to call API operations.
After you complete the preceding preparations, you can use ASAPI SDK to call API operations. For more information about how to use SDKs for different languages, see the relevant topics. The following example shows how to call the DescribeInstances operation of Elastic Compute Service (ECS) by using SDK for Java:

```java
public static void main(String[] args) {
    ASClient client = new ASClient();
    // Specify the caller. The caller is recorded in logs.
    client.setSdkSource("autoTest");
    // Configure request parameters.
    Map<String, Object> parameters = new HashMap<String, Object>();;
    parameters.put("Product", "Ecs");// Specify the POP code, which is the same as the
POP code in the corresponding API directory.
    parameters.put("Action", "DescribeInstances"); // Specify the name of the API opera
tion. Use the same case as the case in the corresponding API directory.
    parameters.put("Version", "2014-05-26"); // Specify the API version.
    // Specify the region ID that you obtained.
    parameters.put("RegionId", "xxx");
    // Specify the AccessKey ID and AccessKey secret that you obtained.
    parameters.put("AccessKeyId", "xxx");
    parameters.put("AccessKeySecret", "xxx");
    // Add the parameters based on the API documentation. Take note that the parameters
are case-sensitive.
    parameters.put("PageNumber",1);
    parameters.put("PageSize",10);
    Map<String,String> headers=new HashMap<>();
    // Specify the organization ID in the Apsara Uni-manager Management Console.
    headers.put("x-acs-organizationid","3");
    // Specify the resource set ID in the Apsara Uni-manager Management Console.
    //headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>");
    // Specify the endpoint of ASAPI.
    String endpoint="https://public.asapi.xxx.xxx/asapi/v3";
    // Initiate a request.
    String result = client.doPost(endpoint,headers, parameters);
    // Display the results.
    System.out.println(JSONObject.toJSONString(JSONObject.parseObject(result), Serializ
erFeature.PrettyFormat));
```

`}`

### 8.2 Use the ASAPI gateway to make API calls

API calls

#### 8.2.1 Obtain an endpoint of ASAPI

This topic describes three methods that you can use to obtain an endpoint of Apsara Stack API (ASAPI) and how to verify the endpoint. Methods Method 1: Use Registration Vars of Services to obtain an endpoint
1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click Product s. iii. Choose Plat f orms > Apsara Inf rast ruct ure Management Framework.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for `Registration Vars of Services` and click the report name.
4. On the Regist rat ion Vars of Services page, click the
icon next to Service and search for `asapi` .
5. Find the asapi service, right-click in the Service Regist rat ion column, and then select Show More
from the shortcut menu. In the Det ails dialog box, obtain the value of asapi.public.endpoint .
6. Generate an endpoint of ASAPI based on the following format:

```
https://<asapi.public.endpoint>/asapi/v3
```

Method 2: Use cluster resources to generate an endpoint
1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click Product s. iii. Choose Plat f orms > Apsara Inf rast ruct ure Management Framework.
2. Go to the Clusters page.
i. In the left-side navigation pane, choose Operat ions > Clust er Operat ions. ii. In the Clust er search box, enter `ascm` . iii. Click Operat ions in the Act ions column.
3. Obtain the value of the domain parameter.
i. Click the Clust er Resources tab. ii. In the Name field, search for `asapi_dns_public` . iii. Click Det ails in the Applicat ion Paramet er column. In the Applicat ion Paramet er message, obtain the value of the domain parameter.
4. Generate an endpoint of ASAPI based on the following format:

```
https://<domain>/asapi/v3
```

Method 3: Concatenate strings to generate an endpoint You can also concatenate strings to generate an endpoint based on the following format:

```
https://public.asapi.<region>.<internet-domain>/asapi/v3
```

1. Replace <region> with the actual region ID.
2. Replace <internet-domain> with the root domain of your Apsara Stack service. To obtain the
root domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internetdomain parameter instead of the intranet-domain parameter. If the region value is `cn-****-****-d01` and the int ernet -domain value is `inter.****.****.com` , the following endpoint is used:

```
https://public.asapi.cn-****-****-d01.inter.****.****.com/asapi/v3
```

Verify the endpoint Enter the following code. If you cannot access the endpoint, the endpoint is unavailable. You can use the historical endpoint.

```bash
 curl https://public.asapi.${global:region}.${global:internet-domain}/api/version -k
```

${global:region} and ${global:internet-domain} are variables. You must replace them with the actual values that you obtained. Available endpoint example: Unavailable endpoint example: Historical endpoint Only the HTTP protocol is supported. The historical endpoint is suffixed with `intranet-domain` and in the following format:

```
 http://server.asapi.${global:region}.${global:intranet-domain}/asapi/v3
```

${global:region} and ${global:intranet-domain} are variables. You must replace them with the actual values that you obtained. Procedure To obtain the actual values of the variables ${global:region}, ${global:internet-domain}, and ${global:intranet-domain}, perform the following operations:
1. In the address bar, enter the region-id.aso.intranet-domain-id.com URL and press the Enter key.
You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Obtain the username and password used to log on to the Apsara Uni-manager Operations Console from the deployment personnel or an administrator. When you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password is 10 to 20 characters in length.
3. Click Log On to log on to the Apsara Uni-manager Operat ions Console.
4. In the top navigation bar, choose Product s > Plat f orms > Apsara Inf rast ruct ure Management
Framework to go to Apsara Infrastructure Management.
5. In the left-side navigation pane, choose Operat ions > Clust er Operat ions.
6. On the Clust ers page, enter ascm-A in the Cluster search box to find the cluster. Click the cluster
name.
7. On the Clust er Dashboard page, click Operat ions Menu > Conf igurat ion Files.
8. In the File List window on the left side of the Clust er Conf igurat ion page, click kv.conf , click the
file content in the right window, and then press Ctrl + F. Search for region, internet-domain, and intranet-domain. Replace ${global:region} with the obtained region value, ${global:internet-domain} with the obtained internet-domain value, and ${global:intranet-domain} with the obtained intranet-domain value. ${global:} is not included in the endpoint of ASAPI that you can use.

#### 8.2.2 Obtain Apsara Stack SDKs

Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. Public environment If you are using the public environment, you can go to the Apsara Stack documentation page and download the Apsara Stack SDKs in the Ot her Resources section at the lower part of the page. Private environment If you are using the private environment, you must switch to the public environment and then go to the Apsara Stack documentation page. At the lower part of the page, download the Apsara Stack SDKs in the Ot her Resources section. Apsara Stack SDK for Java

| greopId | artifactId | Version |
|---|---|---|
| com.alibaba | alicrypto-java-aliyun | 1.0.4 |
| com.alibaba | fastjson | 1.2.68 |

| D | eveloper Guide·Appendixes |   | ApsaraDB for MongoD | B |
|---|---|---|---|---|

| greopId | artifactId | Version |
|---|---|---|
| org.bouncycastle | bcprov-jdk15to18 | 1.66 |
| org.bouncycastle | bcpkix-jdk15on | 1.65 |
| org.bouncycastle | bcprov-jdk15on | 1.65 |
| com.aliyun | gmsse | 1.1.0 |
| org.apache.commons | commons-lang3 | 3.0 |
| commons-codec | commons-codec | 1.11 |
| commons-logging | commons-logging | 1.2 |
| org.apache.httpcomponents | httpcore | 4.4.11 |
| org.apache.httpcomponents | httpclient | 4.5.7 |

Apsara Stack SDK for Python

| Package | Version |
|---|---|
| aliyun-python-sdk-core | 2.13.35 |
| certifi | 2021.5.30 |
| cffi | 1.14.6 |
| charset-normalizer | 2.0.4 |
| cryptography | 3.4.8 |
| idna | 3.2 |
| jmespath | 0.10.0 |
| pycparser | 2.20 |
| requests | 2.26.0 |
| urllib3 | 1.26.6 |

You can use the version for each package listed in the preceding table or a later version.

### 8.3 STS overview

#### 8.3.1 What is STS?

Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and RAM roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed to access Apsara Stack resources by using an issued STS token. When the STS token is issued, you can specify a validity period and access permissions for the STS token. Use a RAM user to obtain an STS token An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and can use the STS token to access Apsara Stack resources. Benefits STS tokens help reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify the validity period for STS tokens. After STS tokens expire, they become invalid. Therefore, you do not need to rotate the STS tokens on a regular basis. You can attach custom policies to STS tokens for flexible and fine-grained authorization.

#### 8.3.2 AssumeRole

Obtains a Security Token Service (STS) token that is used by a RAM user to assume a RAM role. In this example, an Apsara Stack tenant account is used as the trusted entity of the RAM role. Request parameters

| Paramet er | T ype | Requi red | Example | Descript ion |
|---|---|---|---|---|
| Act ion | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::1234567 89012****:role/ad minrole | The Apsara Stack Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Apsara Stack tenant account. |

| Paramet er | T ype | Requi red | Example | Descript ion |
|---|---|---|---|---|
| RoleSessionNam e | String | Yes | alice | The name of the role session. Set this parameter based on your business requirements. In most cases, you can set this parameter to the identity of the user who calls the operation. For example, specify a username. In ActionTrail logs, you can distinguish the users who assume the same RAM role to perform operations based on the value of the RoleSessionName parameter. This way, you can perform user-specific auditing. The name must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource ": ["*"]}],"Version":"1 "} | The policy that specifies the permissions of the STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. The policy must be 1 to 1,024 characters in length. |

Responses

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| Request Id | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | The ID of the request. |
| Credent ials | None | None | The access credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuKg5 U1**** | The AccessKey ID. |

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| AccessKeySecret | String | ****************************************** | The AccessKey secret. |
| Securit yT oken | String | ******** | The security token. |
| Expirat ion | String | 2015-04- 09T11:52:19Z | The time when the STS token expires. |
| AssumedRoleUser | None | None | The temporary identity that you use to assume the RAM role. |
| Arn | String | acs:ram::123456789 012****:role/adminr ole/alice | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495**** :alice | The ID of the temporary identity that you use to assume the RAM role. |

Examples Add Project Object Model (POM) dependencies The Alibaba Cloud core library is required. Perform the following steps to add the Alibaba Cloud core library to POM:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

Call an API operation to obtain the STS AccessKey 3-tuple. In the following sample code, the `Sts::AssumeRole::2015-04-01` operation is used to obtain the 3tuple.

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; importcomaliyuncsexceptionsClientException;
```

```java
import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKe
yID>", "<yourAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        // Replace "sts.aliyuns.com" with the actual endpoint of STS. In most cases, the en
dpoint is in the following format: sts-vpc.${global:region}.${global:internet-domain}.
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        // Replace "<yourRoleSessionName>" with the alias that you specify for the current
role session.
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
        // Replace "<yourRoleArn>" with the actual ARN that you obtained for the RAM role i
n the preceding step.
        request.putQueryParameter("RoleArn", "<yourRoleArn>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            String assumeRole = response.getData();
            if (StringUtils.isEmpty(assumeRole)) return;
            JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
            JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
            // Obtain the STS AccessKey 3-tuple.
            String stsAK = credentials.getString("AccessKeyId");
            String stsSK = credentials.getString("AccessKeySecret");
            String stsToken = credentials.getString("SecurityToken");
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: " + st
sToken);
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

`}` `}` `}` `}` Call examples In the following sample code, the `DescribeZones` operation in Elastic Compute Service (ECS) is used.

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
        // Replace "<yourRegionID>" with the actual region ID.
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the AccessKey I
D and secret in the 3-tuple that you obtained in the preceding step.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAcces
sKey>", "<yourStsAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        request.setSysDomain("ecs.aliyuns.com");
        request.setSysProduct("Ecs");
        request.setSysAction("DescribeZones");
        request.setSysVersion("2014-05-26");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        //Replace "<yourRegionID>" with the actual region ID.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
        // Replace "<yourStsToken>" with the STS token in the 3-tuple that you obtained in
the preceding step.
        request.putQueryParameter("SecurityToken", "<yourStsToken>");
        // Optional. Specify the resource set ID.
        // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
        // Required. Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

```java
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

`}` `}` `}` Error codes

| Ht t pCode | Error code | Error message | Descript ion |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleAr n | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleSe ssionName | The parameter RoleSessionName is wrongly formed. | The error message returned because the value of the RoleSessionName parameter is in an invalid format. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| 400 | InvalidParameter.Durati onSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the Durat ionSeconds parameter is invalid. The minimum value is 900, and the maximum value is equal to the value of the MaxSessionDurat ion parameter. |

| Ht t pCode | Error code | Error message | Descript ion |
|---|---|---|---|
| 400 | InvalidParameter.PolicyG rammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the policy is invalid. |
| 400 | InvalidParameter.PolicyS ize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error occurred. |
