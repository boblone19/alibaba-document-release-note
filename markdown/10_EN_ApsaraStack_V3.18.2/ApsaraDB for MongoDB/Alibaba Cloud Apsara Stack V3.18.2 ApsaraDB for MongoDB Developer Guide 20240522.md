---
title: "Alibaba Cloud Apsara Stack V3.18.2 ApsaraDB for MongoDB Developer Guide 20240522"
product_version: "V3.18.2"
doc_version: "20240522"
pdf_pages: 115
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 ApsaraDB for MongoDB Developer Guide 20240522.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/MongoDB/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20ApsaraDB%20for%20MongoDB%20Developer%20Guide%2020240522.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.2 ApsaraDB for MongoDB Developer Guide 20240522

## Table of Contents

- 1 Getting started
  - 1.1 Usage notes on development documentation
  - 1.2 Call API operations
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
    - 3.2.5 Troubleshooting
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
    - 5.2.1 Install the core package of SDK for Go
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
  - 8.1 Use the ASAPI gateway to call API operations
  - 8.2 Use the ASAPI gateway to make API calls
    - 8.2.1 Obtain the endpoint of ASAPI
    - 8.2.2 Obtain the ASAPI SDK
  - 8.3 STS overview
    - 8.3.1 What is STS?
    - 8.3.2 AssumeRole

## 1 Getting started

### 1.1 Usage notes on development documentation

This topic describes how to view the desired product development documentation when you use Apsara Stack API (ASAPI).

**Prerequisites**

The Apsara Stack version is obtained from an O&M personnel or operations administrator.

**Procedure**

You can go to the Apsara Stack documentation center and view the desired product documentation.
1. Go to the Apsara Stack Documentation Centerpage by using a browser.
2. Click the **Enterprise**, **Agility**, or **All-in-one** tab based on the Apsara Stack version that you use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the name of the product that you want to view.
5. In the upper-right corner of the product documentation section, click **View Details** or **Download PDF**.

### 1.2 Call API operations

Apsara Stack allows you to use POP Gateway or the Apsara Stack API (ASAPI) gateway to call Apsara Stack API operations. By default, Apsara Stack Enterprise V3.16.0 and later use POP Gateway to deliver the same user experience as in the Alibaba Cloud public cloud. This topic describes how to use POP Gateway to call Apsara Stack API operations. You can still use the ASAPI gateway to call Apsara Stack API operations in Apsara Stack that is earlier than V3.16.0. For more information, see Use the ASAPI gateway to call API operations, Obtain the endpoint of ASAPI, and Obtain the ASAPI SDK.

**Procedure**

1. Obtain an AccessKey pair.
For more information, see Obtain an AccessKey pair.

> **Note:** We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and Apsara Stack services.

2. Obtain the region ID.
For more information, see Obtain the values of common headers.
3. Obtain the organization ID and the resource set ID.
Obtain the organization ID by calling the GetOrganizationList operation. For more information, see GetOrganizationList in Apsara Uni-manager Manag ement Console Developer Guide. Obtain the resource set ID by calling the ListResourceGroup operation. For more information, see ListResourceGroup in Apsara Uni-manager Manage ment Console Developer Guide.

|   | Note When you call an API operation, you can specify the organization ID by using <x-acs-organizationid> and the resource set ID by using <x- acs-resourcegroupid> to query only resources that belong to the specified resource set and organization. If you do not specify the <x-acs-organizationid> parameter, the organization to which the current user belongs is used. If you do not specify the <x-acs-resourcegroupid> parameter, this parameter is left empty. If you specify a resource set ID, you must also specify an organization ID. |   |   |
|---|---|---|---|
|   |   | <x- |   |
|   | acs-resourcegroupid> |   |   |

4. View the developer guide of the cloud service that you want to use to learn how to make the API call.
Obtain the developer guide of the cloud service that you want to use. This way, you can learn the features of API operations and how to call the API operations. For more information, see Usage notes on development documentation.
5. Obtain the endpoint of ApsaraDB for MongoDB. For more information, see Obtain the endpoint of ApsaraDB for MongoDB.
6. Obtain the SDK package of ApsaraDB for MongoDB. For more information, see Obtain the SDKs of ApsaraDB for MongoDB.
7. Make an API call. For more information, see Getting started (Java), Getting started (Python), or Getting started (Go).

## 2 Preparations

### 2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press Enter.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Management Console from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Log On**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding operations in the following scenarios:
You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable MFA** topic in **Apsara Uni-manager Management** **Console User Guide**.

5. In the top navigation bar, choose **Products > Others > API Tool**.

### 2.2 View the API-related information

This topic describes how to view the API-related information. Before you use SDKs, you must obtain service names, API operation names, and API versions.

**Background information**

The API operations listed in API Reference are for reference only. For more information about how to call an API operation, see ApsaraDB for MongoDB Developer Guide.

**Procedure**

1. Log on to the API Tool console.
2. In the left-side navigation pane, click **API Tool**.
3. On the **API Directory** page, select Dds from the product name drop-down list or search for Dds in the product name field.
4. View and record the service name, API operation name, and API version.

### 2.3 Obtain an AccessKey pair

AccessKey pairs are assigned by Resource Access Management (RAM) or Security Token Service (STS). You can use one type of AccessKey pairs for authentication when you make an API request. This topic describes how to obtain an AccessKey pair assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. AccessKey pairs can be assigned by RAM or STS: An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An AccessKey 3-tuple that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

> **Warning:** The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |

| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For more information about how to obtain an organization ID, see the "GetOrganizationList" section in Apsara Uni-manager Management Console Developer Guide. |
|---|---|
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. For example, if you use ApsaraDB for MongoDB, you can obtain the instance ID from the instance list page of ApsaraDB for MongoDB. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, click the profile picture and then select **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of the personal account.

> **Note:** The AccessKey pair provides full permissions on cloud resources within your Alibaba Cloud account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you want to obtain.
5. On the right side of the page that appears, click **Management AccessKey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### 2.4 Obtain the values of common headers

You must provide multiple headers when you call Apsara Stack operations. This topic describes the headers and how to obtain the values of the headers. This topic also describes the return values of specific headers after you call Apsara Stack operations.

**Headers**

| Header | Description |
|---|---|
| x-acs-regionid | The ID of the region where the ApsaraDB for MongoDB instance resides. For more information about how to obtain region IDs, see the Obtain a region ID section of this topic. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For more information about how to obtain organization IDs, see the Obtain an organization ID section of this topic. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information about how to obtain resource set IDs, see the Obtain a resource set ID section of this topic. |
| x-acs-instanceid | The ID of the ApsaraDB for MongoDB instance on which you want to perform operations. For more information about how to obtain instance IDs, see the Obtain an instance ID section of this topic. |

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the required organization.
5. View the region ID in the **Regions** section.

**Obtain an organization ID**

You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide.

**Obtain an instance ID**

You can obtain the ID of an instance in a service console of the Apsara Uni-manager Management Console. In this example, the Elastic Compute Service (ECS) console is used. Perform the following operations to obtain the ID of an ECS instance:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Database Services** > **ApsaraDB for MongoDB**.
3. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster Instances** based on the instance type.
4. In the instance list that appears, find the instance whose ID you want to obtain and obtain its ID in the **Instance ID/Name** column.
The following additional response parameters are returned by default when you call operations to query the instances of cloud services.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

### 2.5 Obtain the endpoint of ApsaraDB for MongoDB

This topic describes how to obtain the endpoint of ApsaraDB for MongoDB.

**Background information**

To use POP Gateway to call Apsara Stack API operations, you must use a service endpoint. You can obtain a service endpoint from an Apsara Stack onsite O&M engineer or by performing the following operations:

**Procedure**

1. Log on to the Apsara Infrastructure Management console.
i. Go to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click **Products**. iii. Choose **Platform** >**Apsara Infrastructure Management**.
2. In the left-side navigation pane, click **Reports**.
3. On the **All Reports** page, search for `Registration Vars of Services` . In the report list that appears, click the name of the report.
4. On the **Registration Vars of Services** page, click the
icon next to **Service** and search for `MongoDB` .
5. Find the `mongodb-yaochi` service, right-click the **Service Registration** column, and then select **Show More** from the shortcut menu.
In the **Details** dialog box, obtain the **mongodb.openapi-inc.endpoint** value. This value is the endpoint of ApsaraDB for MongoDB.

> **Note:** The endpoint of ApsaraDB for MongoDB is in the mongodb-vpc.${global:region}.${global:internet-domain} format.

### 2.6 Obtain the SDKs of ApsaraDB for MongoDB

Before you use POP Gateway to call Apsara Stack API operations of ApsaraDB for MongoDB, you must obtain the SDKs of ApsaraDB for MongoDB. This topic describes how to obtain the SDKs of ApsaraDB for MongoDB.

| Programming language | Download URL of an ApsaraDB for MongoDB SDK | References |
|---|---|---|
| Alibaba Cloud SDK for Java | Alibaba Cloud MongoDB SDK for Java | Getting started (Java) |
| Alibaba Cloud SDK for Python | Alibaba Cloud MongoDB SDK for Python | Getting started (Python) |
| Alibaba Cloud SDK for Go | Alibaba Cloud MongoDB SDK for Go | Getting started (Go) |

> **Note:** We recommend that you use an SDK for Java, Python, or Go. If you use an SDK for a different programming language, the SDK may be incompatible with your system.

or SDK for Java

## 3 Call examples for SDK for Java

### 3.1 Getting started

This topic describes how to obtain and use Apsara Stack SDK for Java.

**Environment requirements**

An authorized Apsara Stack tenant account and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained before you can use Apsara Stack SDK for Java. You can obtain your AccessKey pair in the Apsara Uni-manager Management Console. For more information, see Obtain an AccessKey pair. For more information about how to obtain the endpoint of ApsaraDB for MongoDB, see Obtain the endpoint of ApsaraDB for MongoDB. Apsara Stack SDK for Java 1.8 or later is installed.

**Install Apsara Stack SDK for Java**

If you use Apache Maven to manage a Java project, you need to only import the JAR file of Apsara Stack SDK for Java to the pom.xml file of the project. To use an Apsara Stack SDK, you must install the SDK core library and the Apsara Stack SDK. We recommend that you use version 4.5.17 or later for the SDK core library. In this example, the SDK version 3.6.3 is used.

**Use Apsara Stack SDK for Java**

To use Apsara Stack SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and configure the required parameters.
3. Send the API request and handle the response or exception.

> **Note:** Replace the variables in the following sample code with actual values. Do not retain the angle brackets (<>) in the final code.
> Variables:
> <yourRegionID>: Replace this variable with your region ID.
> <yourAccessKeyID>: Replace this variable with your AccessKey ID.
> <yourAccessKeySecret>: Replace this variable with your AccessKey secret.
> <yourDBInstanceId>: Replace this variable with your ApsaraDB for MongoDB instance ID.

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.google.gson.Gson; import java.util.*; import com.aliyuncs.dds.model.v20151201.*; public class DescribeAccounts {
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>");
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

### 3.2 Use SDK

#### 3.2.1 Install ApsaraDB for MongoDB SDK for Java

This topic describes how to install and use ApsaraDB for MongoDB SDK for Java. Apsara Stack SDK for Java 1.8 or later is required. To install ApsaraDB for MongoDB SDK for Java, add Maven dependencies or download ApsaraDB for MongoDB SDKs. For more information, see Obtain the SDKs of ApsaraDB for MongoDB. To use ApsaraDB for MongoDB SDK for Java, you must install the core library of Apsara Stack SDK for Java and ApsaraDB for MongoDB SDK for Java. We recommend that you use version 4.5.17 or later for the core library of Apsara Stack SDK for Java. In this example, ApsaraDB for MongoDB SDK for Java uses version 3.6.3. For example, to use ApsaraDB for MongoDB SDK for Java, you must install the core library of Apsara Stack SDK for Java and ApsaraDB for MongoDB SDK for Java, and then add the following dependencies to the pom.xml file. For information about the SDK version number, see Obtain the SDKs of ApsaraDB for MongoDB. or SDK for Java

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

When you use Apsara Stack SDKs to access Apsara Stack services, you can use an AccessKey pair for identity verification. Apsara Stack SDK for Java supports identity verification based on AccessKey pairs. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you use an AccessKey pair to access Apsara Stack, you must configure your credential when initializing the client.

> **Note:** Do not disclose any code that may contain your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack account may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>")
```

> **Note:** You must use actual values to replace the variables in the preceding sample code. Do not retain the angle brackets (<>) in the final code. The following list describes the variables:
> <yourRegionID>: Replace it with the actual region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.

#### 3.2.3 Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements.

> **Note:** You must use actual values to replace the variables in the following sample code. Do not retain the angle brackets (<>) in the final code.
> The following list describes the variables:
> <readTimeout>: Specify the read timeout period based on your business requirements. Unit: milliseconds.
> <connectionTimeout>: Specify the connection timeout period based on your business requirements. Unit: milliseconds.
> <maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER.
> <maxRequests>: Specify the maximum number of requests based on your business requirements. The supported data type is INTEGER.
> <http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy.

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

or SDK for Java This topic describes how to use ApsaraDB for MongoDB SDK for Java to initiate a request.

**Procedure**

1. Create an ACS client.

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
The naming convention for requests is ${apiName}Request , where **${apiName}** indicates the API name, such as DescribeAccounts. When you use the SDKs of multiple services, different requests may share the same name. Make sure to differentiate different requests by their SDK.

```
DescribeAccountsRequest request = new DescribeAccountsRequest();
      request.setDBInstanceId("dds-********");
      request.setAccountName("root");
```

3. Initiate the request and handle the response.

```
DescribeAccountsResponse response = client.getAcsResponse(request);
```

In normal cases, all returned fields are deserialized into the response. You can directly call `response.getXXX()` to obtain the response fields.

```
AccountData := response.getData()
```

If an exception occurs or you need the original HTTP response, use `doAction()` to obtain the original response.

```
HttpResponse response = client.doAction(request);
```

#### 3.2.5 Troubleshooting

If the server or SDK encounters an error when you use SDK for Java, it returns an error response. The error response contains an error code and an error message. In most cases, you do not need to handle the errors returned by SDK for Java. You need to only handle the errors returned by the server based on error messages. `ServerException` indicates a server error. `ClientException` indicates an SDK error. For example, when the following error occurs, you can modify the AccessKey ID based on the error message to solve the problem:

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

If you want to handle SDK errors, refer to the following example to write your code:

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handle the response.
    // ...
}catch (ServerException e){
    // You can add your logic to handle errors.
    // For example, print the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If the error persists, you can submit a ticket with the request ID included.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // You can add your logic to handle errors.
    // For example, print the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

or SDK for Python

## 4 Call examples for SDK for Python

### 4.1 Getting started

This topic describes how to obtain and use ApsaraDB for MongoDB SDK for Python.

**Environment requirements**

An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain the endpoint of ApsaraDB for MongoDB, see Obtain the endpoint of ApsaraDB for MongoDB.
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

**Use ApsaraDB for MongoDB SDK for Python**

To use ApsaraDB for MongoDB SDK for Python, perform the following steps:
1. Create a client instance. When you create a client instance, you must obtain a region ID, AccessKey ID, and AccessKey secret.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exceptions.

> **Note:** In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code.
> The following list describes the variables:
> <yourRegionID>: Replace it with the actual region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID.

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential from aliyunsdkdds.request.v20151201.DescribeAccountsRequest import DescribeAccountsRequest credentials = AccessKeyCredential('<yourAccessKeyID>', '<yourAccessKeySecret>') client = AcsClient(region_id='<yourRegionID>', credential=credentials) request = DescribeAccountsRequest() request.set_accept_format('json') request.set_DBInstanceId("<yourDBInstanceId>") response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

### 4.2 Use SDK

#### 4.2.1 Install ApsaraDB for MongoDB SDK for Python

This topic describes how to install the core library of Apsara Stack SDK for Python and ApsaraDB for MongoDB SDK for Python.

**Background information**

To use a service SDK, you must install the core library of Apsara Stack SDK for Python. To use ApsaraDB for MongoDB SDK for Python, you must install the core library of Apsara Stack SDK for Python and ApsaraDB for MongoDB SDK for Python.

**Install the core library of Apsara Stack SDK for Python**

Apsara Stack SDK for Python supports Python 2.6.x, 2.7.x, as well as 3.x and later. You can use the pip command to install Apsara Stack SDK for Python. If you use Python 2.x, run the following command: or SDK for Python

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-core-v3
```

If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-dds
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-dds
```

#### 4.2.2 Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you can use an AccessKey pair for identity verification. Apsara Stack SDK for Python supports identity verification based on AccessKey pairs. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you use an AccessKey pair to access Apsara Stack, you must configure your credential when initializing the client.

> **Important:** Do not disclose any code that may contain your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack account may be compromised.

```
clt = client.AcsClient(<yourRegionID>, <yourAccessKeyID>, <yourAccessKeySecret>)
```

> **Note:** In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code. The following list describes the variables:
> <yourRegionID>: Replace it with the actual region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.

#### 4.2.3 Set HTTPS requests

Apsara Stack SDK for Python allows you to initiate API requests over HTTP and HTTPS. You can specify the HTTP or HTTPS protocol for a specific request, or set a global default protocol.

> **Note:** The default HTTP or HTTPS protocol of a service takes precedence over the global default protocol.

**Add OpenSSL support**

The HTTPS protocol support of Apsara Stack SDK for Python is based on the OpenSSL support in Python. To use Apsara Stack SDK for Python to send HTTPS requests, you must add OpenSSL support in Python. OpenSSL supports TLS 1.2 and later. Run the `python -c "import ssl"` command to check whether your Python environment supports OpenSSL. If the error message `ImportError: No module named ssl` is not returned, OpenSSL is already supported. Otherwise, run the following command to install it:

```
pip install pyopenssl
```

**Set the protocol to HTTP or HTTPS for a single request**

The following sample code provides an example on how to set HTTPS as the protocol for a request:

```bash
request = DescribeInstancesRequest() request.set_protocol_type("https")
# Set the value to https or http.
```

**Set a global default protocol**

The following sample code provides an example on how to set a global default protocol:

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request.
```

#### 4.2.4 Initiate a request

This topic describes how to use ApsaraDB for MongoDB SDK for Python to initiate a request. The DescribeAccounts operation is used in the example.

**Procedure**

1. Import ApsaraDB for MongoDB SDK for Python.

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential from aliyunsdkdds.request.v20151201.DescribeAccountsRequest import DescribeAccountsRequest
```

2. Create an ACS client.
or SDK for Python

> **Note:** The following list describes the variables:
> <yourRegionID>: Replace it with the actual region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.

```
credentials = AccessKeyCredential('<yourAccessKeyID>', '<yourAccessKeySecret>') client = AcsClient(region_id='<yourRegionID>', credential=credentials)
```

3. Create a request object.

> **Note:** <yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID.

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
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
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

or SDK for Go

## 5 Call examples for SDK for Go

### 5.1 Getting started

This topic describes how to obtain and use ApsaraDB for MongoDB SDK for Go.

**Environment requirements**

An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret.

**Install the core library of Apsara Stack SDK for Go.**

Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core library of Apsara Stack SDK for Go:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Use ApsaraDB for MongoDB SDK for Go**

The following code provides an example on how to use ApsaraDB for MongoDB SDK for Go.
1. Initialize a client instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exceptions.

> **Note:** In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code. The following list describes the variables:
> <yourRegionID>: Replace it with the actual region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID.

```java
package main import (
    "fmt"
      dds "github.com/aliyun/alibaba-cloud-sdk-go/services/dds"
```

`)`

```
func main() {
    client, err := dds.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>")
    request := dds.CreateDescribeAccountsRequest()
    request.Scheme = "https"
    request.DBInstanceId = "<yourDBInstanceId>"
    response, err := client.DescribeAccounts(request)
    if err != nil {
        fmt.Print(err.Error())
    fmt.Printf("response is %#v\n", response)
```

4. (Optional) Switch to HTTP or HTTPS.

```
request.Scheme = "HTTPS"
```

### 5.2 Use SDK

#### 5.2.1 Install the core package of SDK for Go

This topic describes how to install the core package of SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### 5.2.2 Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you can use an AccessKey pair for identity verification. Apsara Stack SDK for Go supports identity verification based on AccessKey pairs. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you use an AccessKey pair to access Apsara Stack, you must configure your credential when initializing the client.

> **Important:** Do not disclose any code that may contain your AccessKey pair. For example, your AccessKey pair may become disclosed if you commit your code to a public GitHub project, which could compromise your Alibaba Cloud account.

```
client, err := dds.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>")
```

or SDK for Go

> **Note:** In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code. The following list describes the variables:
> <yourRegionID>: Replace it with the actual region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.

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

> **Note:** You must use actual values to replace the variables in the following sample code. The angle brackets <> are not retained in the final code. The following list describes the variables:
> <yourRegionID>: Replace it with the actual region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID.

```
client, err := dds.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>")
```

3. Use the `xxx.CreateXXXRequest` method to create a request.
The naming convention for this method is ${service}.Create${apiName}Request . The **${service}** part specifies a service name. Service names must use lowercase letters. Example: dds. This value indicates ApsaraDB for MongoDB. The **${apiName}** part specifies an API name. Example: DescribeRegions.

> **Note:** <yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID.

```
request := dds.CreateDescribeAccountsRequest()
    request.Scheme = "https"
    request.DBInstanceId = "<yourDBInstanceId>"
```

4. Initiate the request.

```
response, err := client.DescribeAccounts(request)
```

#### 5.2.4 Handle errors

When you use Alibaba Cloud SDK for Go, a `ClientError` or a `ServerError` is returned when an error occurs on the server or SDK side. Both error types are included in `sdk.errors` . The errors conform to the standard Go error interface, so they can be handled in a similar way as standard Go errors. You can use the following code to handle the errors:

```
response, err := client.DescribeAccounts(request) if err != nil {
    fmt.Print(err.Error())
```

**ClientError**

If an error occurs in the SDK when you send a request and cannot be automatically handled, the SDK returns a `ClientError` . The following code provides an example on how to determine and obtain the error message in the `ClientError` :

> **Important:** When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/dds" // In the package, dds indicates ApsaraDB for MongoDB.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Error package that is added.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)` or SDK for Go

```
response, err := Client.DescribeAccounts(request) if clientError, ok := err.(*errors.ClientError); ok{
    // Obtain the error code.
    clientError.ErrorCode()
    // Obtain the error message.
    clientError.Message()
    // Obtain the original error. The return value may be nil.
    clientError.OriginError()
```

**ServerError**

When the server returns an error message, the SDK wraps the message into a `ServerError` and returns it to the client. In this case, you can still obtain the original HTTP response from the response. The following code provides an example on how to determine and obtain the error message in ServerError and Response:

> **Important:** When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/dds" // In the package, dds indicates ApsaraDB for MongoDB.
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

ns by function

## 6 List of operations by function

The following tables list the API operations available for use in ApsaraDB for MongoDB.

| Operation | Description |
|---|---|
| CreateDBInstance | Creates or clones an ApsaraDB for MongoDB replica set instance. |
| ModifyDBInstanceSpec | Modifies the specifications or storage capacity of an ApsaraDB for MongoDB standalone or replica set instance. |
| DeleteDBInstance | Releases an ApsaraDB for MongoDB instance. |
| CreateShardingDBInstance | Creates or clones an ApsaraDB for MongoDB sharded cluster instance. |
| CreateNode | Creates a shard or mongos node for an ApsaraDB for MongoDB sharded cluster instance. |
| DeleteNode | Deletes a shard or mongos node from an ApsaraDB for MongoDB sharded cluster instance. |
| ModifyNodeSpec | Changes the specifications or storage capacity of nodes in an ApsaraDB for MongoDB sharded cluster instance. |

| Operation | Description |
|---|---|
| MigrateToOtherZone | Migrates an ApsaraDB for MongoDB instance to another zone. |
| DescribeRegions | Queries the regions and zones in which an ApsaraDB for MongoDB instance can be created. |
| MigrateAvailableZone | Changes the zone of an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| DescribeAvailableResource | Queries the ApsaraDB for MongoDB instances that can be created in a specified zone. |

| Operation | Description |
|---|---|
| AllocatePublicNetworkAddress | Applies for a public endpoint for an ApsaraDB for MongoDB instance. |
| ReleasePublicNetworkAddress | Releases the public endpoint of an ApsaraDB for MongoDB instance. |
| ModifyInstanceVpcAuthMode | Enables or disables password-free access to an ApsaraDB for MongoDB instance over a virtual private cloud (VPC). |
| DescribeShardingNetworkAddress | Queries the connection information of an ApsaraDB for MongoDB sharded cluster instance. |
| ModifyDBInstanceConnectionString | Modifies the endpoint of an ApsaraDB for MongoDB instance. |
| ReleaseNodePrivateNetworkAddress | Releases the internal endpoint of a shard or Configserver node in an ApsaraDB for MongoDB sharded cluster instance. |

| Operation | Description |
|---|---|
| DescribeReplicaSetRole | Queries the role and connection information of an ApsaraDB for MongoDB instance. |
| DescribeKernelReleaseNotes | Queries the release notes of the minor database engine versions of an ApsaraDB for MongoDB instance. |
| DescribeAvailableEngineVersion | Queries the database engine versions to which an ApsaraDB for MongoDB instance can be upgraded. |
| DescribeDBInstances | Queries a list of ApsaraDB for MongoDB instances. |
| DescribeDBInstanceAttribute | Queries the details of an ApsaraDB for MongoDB instance. |
| DescribeRoleZoneInfo | Queries the roles and zones of nodes in an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| RestartDBInstance | Restarts an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceMaintainTime | Modifies the maintenance window of an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceDescription | Modifies the name of an ApsaraDB for MongoDB instance. |
| SwitchDBInstanceHA | Switches between the primary and secondary nodes in an ApsaraDB for MongoDB instance. |
| UpgradeDBInstanceEngineVersion | Upgrades the database engine version of an ApsaraDB for MongoDB instance. |
| UpgradeDBInstanceKernelVersion | Updates the minor database engine version of an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceNetExpireTime | Extends the retention period of the classic network endpoint of an ApsaraDB for MongoDB instance. |

ns by function

| Operation | Description |
|---|---|
| DescribeAccounts | Queries the information of database accounts of an ApsaraDB for MongoDB instance. |
| ResetAccountPassword | Resets the password of the root account of an ApsaraDB for MongoDB instance. |
| ModifyAccountDescription | Modifies the description of the root account of an ApsaraDB for MongoDB instance. |

**Whitelists and security groups**

| Operation | Description |
|---|---|
| DescribeSecurityGroupConfiguration | Queries the Elastic Compute Service (ECS) security groups associated with an ApsaraDB for MongoDB instance. |
| ModifySecurityGroupConfiguration | Modifies the ECS security groups associated with an ApsaraDB for MongoDB instance. |
| DescribeSecurityIps | Queries the IP address whitelists of an ApsaraDB for MongoDB instance. |
| ModifySecurityIps | Modifies the IP address whitelists of an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| DescribeDBInstanceTDEInfo | Queries whether transparent data encryption (TDE) is enabled for an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceTDE | Modifies the TDE status of an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| ModifyDBInstanceSSL | Modifies the Secure Sockets Layer (SSL) settings of an ApsaraDB for MongoDB instance. |
| DescribeDBInstanceSSL | Queries the SSL settings of an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| DescribeAuditRecords | Queries the audit log entries of an ApsaraDB for MongoDB instance. |
| DescribeAuditFiles | Queries the audit log files of an ApsaraDB for MongoDB instance. |
| DescribeAuditPolicy | Queries whether the audit log feature is enabled for an ApsaraDB for MongoDB instance. |
| ModifyAuditLogFilter | Modifies the type of audit logs that you want to collect from an ApsaraDB for MongoDB instance. |
| DescribeAuditLogFilter | Queries the types of audit logs that you want to collect from an ApsaraDB for MongoDB instance. |
| ModifyAuditPolicy | Enables or disables the audit log feature or specifies the log retention period for an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| DescribeSlowLogRecords | Queries the slow query log entries of an ApsaraDB for MongoDB instance. |
| DescribeErrorLogRecords | Queries the error log entries of an ApsaraDB for MongoDB instance. |
| DescribeRunningLogRecords | Queries the operational log entries of an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| DescribeDBInstancePerformance | Queries the performance data of an ApsaraDB for MongoDB instance. |
| DescribeDBInstanceMonitor | Queries the internal at which the performance monitoring data is collected from an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| DescribeParameterModificationHistory | Queries the parameter modification records of an ApsaraDB for MongoDB instance. |
| DescribeParameters | Queries the parameter settings of an ApsaraDB for MongoDB instance. |
| ModifyParameters | Modifies the parameters of an ApsaraDB for MongoDB instance. |

**Backup and restoration**

| Operation | Description |
|---|---|
| DescribeBackupPolicy | Queries the backup policy of an ApsaraDB for MongoDB instance. |

ns by function

| ModifyBackupPolicy | Modifies the backup policy of an ApsaraDB for MongoDB instance. |
|---|---|
| CreateBackup | Backs up an ApsaraDB for MongoDB instance. |
| DescribeBackups | Queries the backups of an ApsaraDB for MongoDB instance. |
| RestoreDBInstance | Restores data to the current ApsaraDB for MongoDB instance. |
| DescribeBackupDBs | Queries the databases that are backed up at a specified point in time or the databases in a specified backup set before you restore a database for an ApsaraDB for MongoDB instance. |

## 7 API Reference

### 7.1 Lifecycle management

#### 7.1.1 CreateDBInstance

Creates or clones an ApsaraDB for MongoDB replica set instance. For more information about instance types, see **Instance types** in **ApsaraDB for MongoDB Product Introduction**. To create sharded cluster instances, you can call the **CreateShardingDBInstance** operation.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDBInstance | The operation that you want to perform. Set the value to CreateDBInstance. |
| ClientToken | String | Yes | ETnLKlblzczshOTUbOCzxxxxx xxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value. You must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Engine | String | Yes | MongoDB | The database engine of the instance. Set the value to MongoDB. |
| EngineVersion | String | Yes | 4.0 | The database engine version of the instance. Valid values: 3.2, 3.4, 4.0, and 4.2. Note To call this operation to clone an instance, set this value to the database engine version of the source instance. |
| DBInstanceClass | String | Yes | dds.mongo.standard | The instance type. For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. |
| DBInstanceStorage | Integer | Yes | 10 | The storage space of the instance. Valid values: 10 to 3000. Unit: GB. The value must be a multiple of 10. Note The values that can be specified for this parameter are subject to the instance types. For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. |
| ZoneId | String | No | cn-hangzhou-b | The zone ID of the instance. You can call the DescribeRegions operation to query the most recent zone list. |
| DBInstanceDescription | String | No | Test database 1 | The name of the instance. It must be 2 to 256 characters in length and can contain digits, letters, underscores (), and _ hyphens (-). It must start with a letter. |
| SecurityIPList | String | No | 10.23.12.24/24 | The whitelist that contains the IP addresses that are allowed to access the instance. Separate multiple IP addresses with commas (,). Each IP address must be unique. A maximum of 1,000 IP addresses can be added. You can enter IP addresses such as 10.23.12.24 and CIDR blocks such as 10.23.12.24/24. /24 indicates that the prefix of the CIDR block is 24-bit long. You can replace 24 with a value within the range of 1 to 32. You can also enter the percent sign (%) or 0.0.0.0/0. Note If you enter the percent sign (%) or 0.0.0.0/0, all IP addresses can access the instance. This may introduce security risks to the instance. Proceed with caution. |
| AccountPassword | String | No | Alitest!159 | The password of the root account. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include !#$%^&amp;*()+-= _ The password must be 8 to 32 characters in length. |

| ChargeType | String | No | PrePaid | The billing method of the instance. Valid values: PostPaid: pay-as-you-go PrePaid: subscription Default value: pay-as-you-go Note If you set this parameter to PrePaid, you must also specify the Period parameter. |
|---|---|---|---|---|
| Period | Integer | No | 1 | The subscription period of the instance. Unit: months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8,9 , 12, 24, and 36. Note This parameter is valid and required only if you set the ChargeType parameter to PrePaid. |
| NetworkType | String | No | VPC | The network type of the instance. Valid values: classic vpc Default value: classic. Note If you set this parameter to vpc, you must also specify the VpcId and VSwitchId parameters. |
| VpcId | String | No | vpc-bpxxxxxxxx | The ID of the virtual private cloud (VPC). Note This parameter is valid only if you set the NetworkType parameter to VPC. |
| VSwitchId | String | No | vsw-bpxxxxxxxx | The ID of the vSwitch. Note This parameter is valid only if you set the NetworkType parameter to VPC. |
| SrcDBInstanceId | String | No | dds-bpxxxxxxxx | The ID of the source instance. This parameter can be specified only when this operation is called to clone instances. You must also specify the BackupId parameter or RestoreTime parameter. |
| BackupId | String | No | 32994xxxx | The ID of the backup set. This parameter can be specified only when this operation is called to clone instances. You must also specify the SrcDBInstanceId parameter. Note You can call the DescribeBackups operation to query the backup ID. |
| RestoreTime | String | No | 2019-03-13T12:11:14Z | The point in time to clone the instance. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Note This parameter can be specified only when this operation is called to clone instances. You must also specify the SrcDBInstanceId and BackupId parameters. You can set this parameter to a point in time in the last seven days. |
| BusinessInfo | String | No | {“ActivityId":"000000000"} | The business information. This is an additional parameter. |
| CouponNo | String | No | youhuiquanpromotionoptio _ _ nidforblank _ _ _ | The coupon code. Default value: youhuiquanpromotionoptionidforblank. _ _ _ _ _ |
| AutoRenew | String | No | true | Specifies whether to enable auto-renewal for the instance. Valid values: true: enables auto-renewal. false: disables auto-renewal. You must manually renew the instance. Default value: false. Note This parameter is valid only if you set the ChargeType parameter to PrePaid. |

| DatabaseNames | String | No | mongodbtest | The names of the databases. Note When you call this operation to clone an instance, you can set the databases that are specified by this parameter for cloning. Otherwise, all databases of the instance are cloned. |
|---|---|---|---|---|
| StorageEngine | String | No | WiredTiger | The storage engine of the instance. Set the value to WiredTiger. Note If you do not specify this parameter, WiredTiger is used. |
| ReplicationFactor | String | No | 3 | The number of nodes in the replica set instance. Valid values: 3, 5, and 7. Default value: 3. |
| ReadonlyReplicas | String | No | 1 | The number of read-only nodes. Valid values: 1 to 5. Note By default, this parameter is not specified and no read-only nodes are created. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |
| OrderId | String | 2033xxxxxxxxxxxx | The ID of the order. |
| RequestId | String | D8F1D721-6439-4257-A89C- F1E8E9C9624D | The ID of the request. |

```
http(s)://mongodb.example.com/?Action=CreateDBInstance &ClientToken=ETnLKlblzczshOTUbOCzxxxxxxxxxx &Engine=MongoDB &EngineVersion=4.0 &DBInstanceClass=dds.mongo.standard &DBInstanceStorage=10
```

| XML | format |
|---|---|
| <CreateDBInstanceResponse> <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId> <OrderId>2033xxxxxxxxxxxx</OrderId> <RequestId>D8F1D721-6439-4257-A89C-F1E8E9C9624D</RequestId> </CreateDBInstanceResponse> |   |

| JSON | format |
|---|---|
| { "DBInstanceId": "dds-bpxxxxxxxx", "OrderId": "2033xxxxxxxxxxxx", "RequestId": "D8F1D721-6439-4257-A89C-F1E8E9C9624D" } |   |

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InsufficientBalance | Your account does not have enough balance. | The error message returned because you do not have sufficient balance within your account. Add funds to your account and try again. |
| 403 | RealNameAuthenticationError | Your account has not passed the real-name authentication yet. | The error message returned because the specified user has not completed real-name verification. Complete real-name verification and try again. |
| 400 | InvalidCapacity.NotFound | The Capacity provided does not exist in our records. | The error message returned because the configured space is invalid. Check the specified parameter. |

| 400 | IdempotentParameterMismatch | Request uses a client token in a previous request but is not identical to that request. | The error message returned because the two specified requests use the same ClientToken value. |
|---|---|---|---|

#### 7.1.2 ModifyDBInstanceSpec

Modifies the specifications or storage capacity of an ApsaraDB for MongoDB replica set instance. This operation is applicable to replica set instances. You can call the **ModifyNodeSpec**, **CreateNode**, or **DeleteNode** operation to change the configurations of a sharded cluster instance. When you call this operation, you must configure the `x-acs-organizationid` , `x-acs-resourcegroupid` , and `x-acs-instanceid` header parameters to specify the organization ID, resource group ID, and instance ID. Otherwise, the call is directed to the root resource set and organization. For more information about the code, see SDK description in ApsaraDB for MongoDB Developer Guide.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanceSpec | The operation that you want to perform. Set the value to ModifyDBInstanceSpec. |
| DBInstanceId | String | Yes | dds-d1n4eab47879**** | The ID of the instance. |
| RegionId | String | No | cn-qd-agility14**** | The region ID of the instance. Note You can call the DescribeDBInstanceAttribute operation to query the region ID of the instance. |
| DBInstanceClass | String | No | dds.mongo.standard | The instance type. Note For more information, see Instance types in Apsara DB for MongoDB Product Introduction. You must specify either this parameter or the DBInstanceStorage parameter. |
| DBInstanceStorage | String | No | 50 | The storage space of the instance. Valid values: 10 to 3000. The value must be a multiple of 10. Unit: GB. Note The values that can be specified for this parameter are subject to the instance types. For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. You must specify either this parameter or the DBInstanceClass parameter. Storage capacity can be scaled down only on subscription replica set instances. The new storage capacity you specify must be greater than the used storage space. |
| OrderType | String | No | UPGRADE | The type of the change. Valid values: UPGRADE: upgrades the configurations of an instance. DOWNGRADE: downgrades the configurations of an instance. Default value: DOWNGRADE. Note This parameter is required when the ChargeType parameter is set to PostPaid. |
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment. Valid values: true: enables automatic payment. Make sure that you have sufficient balance within your account. false: disables automatic payment. Default value: true. |
| BusinessInfo | String | No | {“ActivityId":"000000000"} | The business information. |
| ReplicationFactor | String | No | 3 | The number of nodes in the instance. Valid values for replica set instances: 3, 5, and 7. Valid values for standalone instances: 1. |
| ReadonlyReplicas | String | No | 1 | The number of read-only nodes. Valid values: 1 to 5. |
| CouponNo | String | No | youhuiquanpromotionoptio _ _ nidforblank _ _ _ | The coupon code. Default value: youhuiquanpromotionoptionidforblank. _ _ _ _ _ |

| EffectiveTime | String | No | Immediately | The time when the new configurations take effect. Valid values: Immediately: The new configurations immediately take effect. MaintainTime: The new configurations take effect during the maintenance window of the instance. Default value: Immediately. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 20331066**** | The order ID of the instance. |
| RequestId | String | C5662998-62BE-4C7F-961D- 7DFE775D**** | The ID of the request. |

```
http(s)://mongodb.example.com/?Action=ModifyDBInstanceSpec &DBInstanceId=dds-d1n4eab47879****
```

| XML | format |
|---|---|
| <ModifyDBInstanceSpecResponse> <RequestId>C5662998-62BE-4C7F-961D-7DFE775D****</RequestId> <OrderId>20331066****</OrderId> </ModifyDBInstanceSpecResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "C5662998-62BE-4C7F-961D-7DFE775D****", "OrderId": "20331066****" } |   |

#### 7.1.3 DeleteDBInstance

Releases an ApsaraDB for MongoDB instance. The instance must be in the Running state when you call this operation. After an instance is released, all the data in the instance is deleted and cannot be restored. Proceed with caution. When you call this operation, you must configure the `x-acs-organizationid` , `x-acs-resourcegroupid` , and `x-acs-instanceid` header parameters to specify the organization ID, resource group ID, and instance ID. Otherwise, the call is directed to the root resource group and organization. For more information about the code, see SDK Description in ApsaraDB for MongoDB Developer Guide.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDBInstance | The operation that you want to perform. Set the value toDeleteDBInstance. |
| DBInstanceId | String | Yes | dds-d1n4eab47879**** | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOTUbOCz**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 72651AF9-7897-41A7-8B67- 6C15C7F2**** | The ID of the request. |

```
http(s)://mongodb.example.com/?Action=DeleteDBInstance &DBInstanceId=dds-d1n4eab47879****
```

```json
<DeleteDBInstanceResponse>
  <RequestId>72651AF9-7897-41A7-8B67-6C15C7F2****</RequestId>
</DeleteDBInstanceResponse>
  "RequestId": "72651AF9-7897-41A7-8B67-6C15C7F2****"
```

#### 7.1.4 CreateShardingDBInstance

Creates or clones an ApsaraDB for MongoDB sharded cluster instance. When you call this operation, you must configure the `x-acs-organizationid` , `x-acs-resourcegroupid` , and `x-acs-instanceid` header parameters to specify the organization ID, resource group ID, and instance ID. Otherwise, the call is directed to the root resource set and organization. For more information about the code, see SDK description in ApsaraDB for MongoDB Developer Guide.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateShardingDBInstance | The operation that you want to perform. Set the value to CreateShardingDBInstance. |
| AccountPassword | String | Yes | Alitest**** | The password of the root account. The encoding format must comply with the following rules: The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password can contain the following special characters: !#$%^&amp;*()+-= _ The password must be 8 to 32 characters in length. |
| Engine | String | Yes | MongoDB | The database engine of the instance. Set the value to MongoDB. |
| EngineVersion | String | Yes | 4.0 | The database engine version of the instance. Valid values: 3.0, 3.4, 4.0, and 4.2. Note If you call this operation to clone an instance, set the value to the database engine of the source instance. |
| RegionId | String | Yes | cn-qd-agility14**** | The region ID of the instance. Note You can call the DescribeRegions operation to query the available regions. |
| ZoneId | String | No | cn-qd-agility14- amtest110**** | The zone ID of the instance. Note You can call the DescribeRegions operation to query available zones. |
| Mongos.N.Class | String | No | dds.mongos.standard | The specifications of the mongos node. For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. N specifies the serial number of the mongos node for which the specification is specified. For example, Mongos.1.Class specifies the specification of the first mongos node. Mongos.2.Class specifies the specification of the second mongos node. Note You can configure the specifications of 2 to 32 mongos nodes. |

| ReplicaSet.N.Class | String | No | dds.shard.standard | The specifications of the shard node. For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. N specifies the serial number of the shard node for which the specification is specified. For example, ReplicaSet.1.Class specifies the specification of the first shard node. ReplicaSet.2.Class specifies the specification of the second shard node. Note You can specify the specifications of 2 to 32 shard nodes. |
|---|---|---|---|---|
| ReplicaSet.N.Storage | Integer | No | 20 | The storage capacity of the shard node. Valid values:1 0 to 2000. The value must be a multiple of 10. Unit: GB. The values that can be specified for this parameter are subject to the instance types. For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. N specifies the serial number of the shard node for which storage capacity is specified. For example, ReplicaSet.1.Storage specifies the storage capacity of the first shard. ReplicaSet.2.Storage specifies the storage capacity of the second shard. |
| ConfigServer.N.Class | String | No | dds.cs.mid | The specifications of the Configserver node. Valid value: dds.cs.mid. Note The specifications of the config server are fixed at 1 core and 2 GB memory. The value of N is fixed at 1. For example, set the value of ConfigServer.1.Class parameter to dds.cs.mid. |
| ConfigServer.N.Storage | Integer | No | 20 | The storage capacity of a Configserver node. Set the value to 20. Note The storage capacity is fixed as 20 GB. For example, set the value of ConfigServer.1.Storage parameter to 20. |
| DBInstanceDescription | String | No | Testdatabase1 | The name of the instance. The name must comply with the following naming conventions: The name must start with a letter, and can contain digits, letters, underscores (), and hyphens (-). _ The name must be 2 to 256 characters in length, |
| SecurityIPList | String | No | 10.23.12.24/24 | The whitelist that contains the IP addresses that are allowed to access the instance. Separate multiple IP addresses with commas (,). Each IP address must be unique. A maximum of 1,000 IP addresses can be added. You can enter IP addresses such as 10.23.12.24 and Classless Inter-Domain Routing (CIDR) blocks such as 10.23.12.24/24. /24 indicates the length of the CIDR block prefix. The prefix can be 1 to 32 bits in length. You can also enter the percent sign (%) or 0.0.0.0/0. Note If you enter the percent sign (%) or 0.0.0.0/0, all IP addresses can access the instance. This may introduce security risks to the instance. |
| ChargeType | String | No | PrePaid | The billing method of the instance. Valid values: Postpaid: pay-as-you-go Prepaid: subscription Default value: PostPaid. Note If you specify this parameter to PrePaid, you must also specify the Period parameter. |
| Period | Integer | No | 1 | The subscription period of the instance. Unit: months. Valid values: 1 to 9, 12, 24, and 36. Note This parameter takes effect only when you set the ChargeType parameter to PrePaid. |

| NetworkType | String | No | Classic | The type of network in which the instance resides. Default value: standard. Valid values: Classic VPC Default value: Classic. Note If you set the value to VPC, you must specify the VpcId and VSwitchId parameters. |
|---|---|---|---|---|
| VpcId | String | No | vpc-bp1q2qqm4vxo6e6zl**** | The ID of the VPC. Note This parameter is required when the NetworkType parameter is set to VPC. |
| VSwitchId | String | No | vsw-bp1buy0h9myt5i9e7**** | The ID of the vSwitch. Note This parameter is required when the NetworkType parameter is set to VPC. |
| SrcDBInstanceId | String | No | dds-bp1b47357f21**** | The ID of the source instance. Note This parameter is required only when this operation is called to clone instances. If you set this parameter, you must also specify the RestoreTime parameter. |
| RestoreTime | String | No | 2019-03-08T02:30:25Z | The point in time to which you want the cloned instance to restore. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Note This parameter is required only when this operation is called to clone instances. If you set this parameter, you must also specify the SrcDBInstanceId parameter. You can set this parameter to any point in time in the last seven days. |
| ClientToken | String | No | ETnLKlblzczshOTUbOCz**** | The client token that is used to ensure the idempotency of requests. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| StorageEngine | String | No | WiredTiger | The storage engine of the database. Only WiredTiger is supported. |
| AutoRenew | String | No | false | Specifies whether to enable automatic renewal for the instance. Valid values: true: enables automatic renewal. false: disables automatic renewal. You must renew the instance manually. Default value: false. Note This parameter is required when the ChargeType parameter is set to PrePaid. |
| ResourceGroupId | String | No | rg-acfm22cdcgc**** | The ID of the resource group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | dds-bp14ed961586**** | The ID of the instance. |
| OrderId | String | 20331066**** | The order ID of the instance. |
| RequestId | String | D8F1D721-6439-4257-A89C- F1E8E9C9**** | The ID of the request. |

```
http(s)://mongodb.example.com/?Action=CreateShardingDBInstance &AccountPassword=Alitest**** &Engine=MongoDB &EngineVersion=4.0 &RegionId=cn-qd-agility14****
```

| XML | format |
|---|---|
| <CreateShardingDBInstanceResponse> <RequestId>D8F1D721-6439-4257-A89C-F1E8E9C9****</RequestId> <DBInstanceId>dds-bp14ed961586****</DBInstanceId> <OrderId>20331066****</OrderId> </CreateShardingDBInstanceResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "D8F1D721-6439-4257-A89C-F1E8E9C9****", "DBInstanceId": "dds-bp14ed961586****", "OrderId": "20331066****" } |   |

#### 7.1.5 CreateNode

Creates a shard or mongos node for an ApsaraDB for MongoDB sharded cluster instance. This operation is applicable only to sharded cluster instances.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateNode | The operation that you want to perform. Set the value to CreateNode. |
| NodeClass | String | Yes | dds.shard.mid | The instance type of the shard or mongos node. |
| NodeType | String | Yes | shard | The type of the node. Valid values: shard mongos |
| DBInstanceId | String | Yes | dds-bp11501cd7b5**** | The ID of the sharded cluster instance. |
| NodeStorage | Integer | No | 10 | The disk storage capacity of the node. This parameter is required if you set the NodeType parameter to shard. Valid values: 10 to 2000. Unit: GB. The value of this parameter must be a multiple of 10. |
| ClientToken | String | No | ETnLKlblzczshOTUbOCzxxxxx xxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| FromApp | String | No | OpenApi | The source of the request. Valid values: OpenApi: the ApsaraDB for MongoDB API. mongobuy: the ApsaraDB for MongoDB console. _ |
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment for the instance. Valid values: true: enables automatic payment. Make sure that you have sufficient balance within your Alibaba Cloud account. false: disables automatic payment. You must pay for the instance in the ApsaraDB for MongoDB console. Default value: true. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NodeId | String | d-bp1b7bb3bbe1**** | The node ID. |
| OrderId | String | 2034**** | The order ID. |

| RequestId | String | 7D48FB19-20CA-4725-A870- 3D8F5CE69F14 | The request ID. |
|---|---|---|---|

```
http(s)://mongodb.example.com/?Action=CreateNode &NodeClass=dds.shard.mid &NodeType=shard &DBInstanceId=dds-bp11501cd7b5****
```

| XML | format |
|---|---|
| <RequestId>7D48FB19-20CA-4725-A870-3D8F5CE69F14</RequestId> <NodeId>d-bp1b7bb3bbe1****</NodeId> <OrderId>2034****</OrderId> |   |

| JSON | format |
|---|---|
| { "RequestId": "7D48FB19-20CA-4725-A870-3D8F5CE69F14", "NodeId": "d-bp1b7bb3bbe1****", "OrderId": "2034****" } |   |

#### 7.1.6 DeleteNode

Deletes a shard or mongos node from an ApsaraDB for MongoDB sharded cluster instance. Before you call this API operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements: The instance is in the running state. The instance is a sharded cluster instance. The number of shard or mongos nodes in the instance is greater than 2.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteNode | The operation that you want to perform. Set the value to DeleteNode. |
| DBInstanceId | String | Yes | dds-bp11501cd7b5**** | The instance ID. |
| NodeId | String | Yes | s-bp1713dece57**** | The ID of the shard or mongos node that you want to delete. You can call the DescribeDBInstanceAttribute operation to query the node ID. |
| ClientToken | String | No | ETnLKlblzczshOTUbOCz**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 2033**** | The order ID. |
| RequestId | String | 9F9BDE64-BF30-41F3-BD29- C19CE4AB3404 | The request ID. |
| TaskId | Integer | 111111111 | The task ID. |

```
http(s)://mongodb.example.com/?Action=DeleteNode &DBInstanceId=dds-bp11501cd7b5**** &NodeId=s-bp1713dece57****
```

```xml
<TaskId>111111111</TaskId> <RequestId>9F9BDE64-BF30-41F3-BD29-C19CE4AB3404</RequestId> <OrderId>2033****</OrderId>
```

| JSON | format |
|---|---|
| { "TaskId": 111111111, "RequestId": "9F9BDE64-BF30-41F3-BD29-C19CE4AB3404", "OrderId": "2033****" } |   |

#### 7.1.7 ModifyNodeSpec

You can call this operation to modify the specifications and storage capacity of the nodes in an ApsaraDB for MongoDB sharded cluster instance. This operation is applicable only to sharded cluster instances.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNodeSpec | The operation that you want to perform. Set the value to ModifyNodeSpec. |
| NodeId | String | Yes | d-bpxxxxxxxx | The ID of the shard or mongos node in the sharded cluster instance. You can call the DescribeDBInstanceAttribute operation to view the ID. Note If you set this parameter to the ID of a shard, you must also specify the NodeStorage parameter. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeClass | String | No | dds.shard.standard | The specifications of the mongos node. For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. Note You must specify this parameter or the NodeStorage parameter. |
| NodeStorage | Integer | No | 20 | The storage capacity for the shard node. Valid values: 10 to 2000. Unit: GB. The value must be a multiple of 10 GB. Note You must specify this parameter or the NodeClass parameter. This parameter is valid only if you set the NodeId parameter to the ID of a shard. |
| ClientToken | String | No | ETnLKlblzczshOTUbOCzxxxxx xxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment for the instance. Valid values: true: enables automatic payment. Make sure that your account has sufficient balance. false: disables automatic payment. You must perform the following operations to pay for the instance: Log on to the ApsaraDB for MongoDB console. In the top navigation bar, click Expenses. The Billing Management page appears. In the left-side navigation pane, click Bills. On the Unpaid tab, click Make a Payment in the Actions column for the bill that you want to pay. Default value: true. |
| EffectiveTime | String | No | Immediately | The time when the new settings take effect. Valid values: Immediately: The settings take effect immediately. MaintainTime: The settings take effect during the maintenance period of the instance. Default value: Immediately. |
| FromApp | String | No | OpenApi | The source of the request. Valid values: OpenApi: the ApsaraDB for MongoDB API mongobuy: the ApsaraDB for MongoDB console _ |

| OrderType | String | No | UPGRADE | The type of the order. Valid values: UPGRADE DOWNGRADE |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 2033xxxxxxxxx | The ID of the order. |
| RequestId | String | EFFC5788-8BB5-41B5-9F15- 9CFC5A0E8FCC | The ID of the request. |

```
http(s)://mongodb.aliyuncs.com/? Action=ModifyNodeSpec &NodeId=d-bpxxxxxxxx &NodeClass=dds.shard.standard &NodeStorage=20
```

| XML | format |
|---|---|
| <ModifyNodeSpecResponse> <OrderId>2033xxxxxxxxx</OrderId> <RequestId>EFFC5788-8BB5-41B5-9F15-9CFC5A0E8FCC</RequestId> </ModifyNodeSpecResponse> |   |

| JSON | format |
|---|---|
| { "OrderId": "2033xxxxxxxx", "RequestId": "EFFC5788-8BB5-41B5-9F15-9CFC5A0E8FCC" } |   |

### 7.2 Region management

#### 7.2.1 MigrateToOtherZone

You can call this operation to migrate an ApsaraDB for MongoDB instance to another zone. This operation is applicable only to replica set instances, but not to sharded cluster instances.

> **Note:** If you have applied for a public endpoint of the instance, you must first call the **ReleasePublicNetworkAddress** operation to release the public endpoint.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | MigrateToOtherZone | The operation that you want to perform. Set the value to MigrateToOtherZone. |
| InstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note You must specify the Vswitch parameter if the network type of the instance is VPC. |
| ZoneId | String | Yes | cn-hangzhou-b | The ID of the destination zone to which you want to migrate the MongoDB instance. Note The destination and source zones are in the same region. You can call the DescribeRegions operation to query the zone IDs. |
| EffectiveTime | String | No | Immediately | The time when the instance is migrated to the destination zone. Valid values: Immediately MaintainTime: The instance will be migrated during the maintenance period of the instance. Default value: Immediately. |

| VSwitchId | String | No | vsw-bpxxxxxxxx | The ID of the vSwitch in the destination zone. Note This parameter can be used only when the network type of the instance is VPC. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252-4A4A-ADDA- 5CB1BF63873D | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=MigrateToOtherZone &ZoneId=cn-hangzhou-b &EffectiveTime=Immediately
```

| XML | format |
|---|---|
| <RequestId>0FDDC511-7252-4A4A-ADDA-5CB1BF63873D</RequestId> |   |

| JSON | format |
|---|---|
| { "RequestId": "0FDDC511-7252-4A4A-ADDA-5CB1BF63873D" } |   |

#### 7.2.2 DescribeRegions

Queries the available regions and zones of an ApsaraDB for MongoDB instance. Before you call the CreateDBInstance or CreateShardingDBInstance operation to create an instance, you must call the DescribeRegions operation to query the available regions and zones of the instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of DdsRegion |   | The information of the regions. |
| DdsRegion |   |   |   |
| RegionId | String | cn-qingdao | The region ID. |
| Zones | Array of Zone |   | The information of the zones in the region. |
| Zone |   |   |   |
| VpcEnabled | Boolean | true | Indicates whether Virtual Private Cloud (VPC) is supported. Valid values: true false |
| ZoneId | String | cn-hangzhou-b | The zone ID. |
| RequestId | String | 4E46C22C-D3B7-4DB8-9C76- 63851BE68E20 | The request ID. |

```
http(s)://mongodb.example.com/?Action=DescribeRegions
```

| XML | format |
|---|---|
| <DescribeRegionsResponse> <RequestId>4E46C22C-D3B7-4DB8-9C76-63851BE68E20</RequestId> <Regions> <DdsRegion> <RegionId>cn-hangzhou</RegionId> <Zones> <Zone> <VpcEnabled>true</VpcEnabled> <ZoneId>cn-hangzhou-i</ZoneId> </Zone> <Zone> <VpcEnabled>true</VpcEnabled> <ZoneId>cn-hangzhou-b</ZoneId> </Zone> <Zone> <VpcEnabled>true</VpcEnabled> <ZoneId>cn-hangzhou-d</ZoneId> </Zone> <Zone> <VpcEnabled>true</VpcEnabled> <ZoneId>cn-hangzhou-f</ZoneId> </Zone> <Zone> <VpcEnabled>true</VpcEnabled> <ZoneId>cn-hangzhou-MAZ5(b,e,f)</ZoneId> </Zone> <Zone> <VpcEnabled>true</VpcEnabled> <ZoneId>cn-hangzhou-g</ZoneId> </Zone> </Zones> </DdsRegion> </Regions> </DescribeRegionsResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "4E46C22C-D3B7-4DB8-9C76-63851BE68E20", "Regions": { "DdsRegion": [ { "RegionId": "cn-hangzhou", "Zones": { "Zone": [ { "VpcEnabled": true, "ZoneId": "cn-hangzhou-i" }, { "VpcEnabled": true, "ZoneId": "cn-hangzhou-b" }, { "VpcEnabled": true, "ZoneId": "cn-hangzhou-d" }, { "VpcEnabled": true, "ZoneId": "cn-hangzhou-f" }, { "VpcEnabled": true, "ZoneId": "cn-hangzhou-MAZ5(b,e,f)" }, { "VpcEnabled": true, "ZoneId": "cn-hangzhou-g" } ] } } ] } } |   |

#### 7.2.3 MigrateAvailableZone

You can call this operation to change the zone of an ApsaraDB for MongoDB instance. This operation is applicable only to replica set instances, but not to sharded cluster instances.

> **Note:** If you have applied for a public endpoint of the instance, you must first call **ReleasePublicNetworkAddress** to release the public endpoint.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | MigrateAvailableZone | The operation that you want to perform. Set the value to MigrateAvailableZone. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note You must specify the Vswitch parameter if the network type of the instance is VPC. |
| ZoneId | String | Yes | cn-hangzhou-b | The ID of the destination zone to which you want to migrate the ApsaraDB for MongoDB instance. Note The destination zone must be in the same region as the current zone of the instance. You can call the DescribeRegions operation to view the zone IDs. |
| Vswitch | String | No | vsw-bpxxxxxxxx | The ID of the vSwitch in the destination zone. Note This parameter can be used only when the network type of the instance is VPC. |
| EffectiveTime | String | No | Immediately | The time when the instance is migrated to the destination zone. Valid values: Immediately: The instance will be migrated immediately. MaintainTime: The instance will be migrated during the maintenance period of the instance. Default value: Immediately. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252-4A4A-ADDA- 5CB1BF63873D | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=MigrateAvailableZone &ZoneId=cn-hangzhou-b &EffectiveTime=Immediately
```

| XML | format |
|---|---|
| <MigrateAvailableZoneResponse> <RequestId>0FDDC511-7252-4A4A-ADDA-5CB1BF63873D</RequestId> </MigrateAvailableZoneResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "0FDDC511-7252-4A4A-ADDA-5CB1BF63873D" } |   |

### 7.3 Resource management

#### 7.3.1 DescribeAvailableResource

You can call this operation to view the ApsaraDB for MongoDB instances that can be created in a specified zone.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeAvailableResource | The operation that you want to perform. Set the value to DescribeAvailableResource. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to view the region IDs. |
| ZoneId | String | No | cn-hangzhou-h | The zone ID of the instance. You can call the DescribeRegions operation to view the zone IDs. |
| InstanceChargeType | String | No | PrePaid | The billing method. Valid values: PrePaid: subscription. PostPaid: pay-as-you-go. Note Default value: PrePaid. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 344EE51D-8850-4935-B68B- 58A8F4DCE3BD | The ID of the request. |
| SupportedDBTypes | Array of SupportedDBType |   | The database type supported. |
| SupportedDBType |   |   |   |
| AvailableZones | Array of AvailableZone |   | The zone ID of the instance. |
| AvailableZone |   |   |   |
| RegionId | String | cn-hangzhou | The region ID of the instance. |
| SupportedEngineVersions | Array of SupportedEngineVersion |   | The versions of the storage engine. |
| SupportedEngineVersion |   |   |   |
| SupportedEngines | Array of SupportedEngine |   | The storage engine supported. |
| SupportedEngine |   |   |   |
| Engine | String | WiredTiger | The storage engine of the instance. |
| SupportedNodeTypes | Array of SupportedNodeType |   | The instance types supported. |
| SupportedNodeType |   |   |   |
| AvailableResources | Array of AvailableResource |   | The details of available resources. |
| AvailableResource |   |   |   |
| InstanceClass | String | dds.mongo.2xlarge | The category of the instance. |
| InstanceClassRemark | String | 8 vCPUs, 32 GiB (maximum connections: 8000 IOPS: 14000) | The instance type. |
| NetworkTypes | String | VPC | The network type of the instance. |
| NodeType | String | 3 | The number of nodes in the instance. |
| Version | String | 4.0 | The database engine version of the instance. |
| ZoneId | String | cn-hangzhou-h | The zone ID of the instance. |
| DbType | String | sharding | The database engine of the instance. |

```
http(s)://mongodb.example.com/? Action=DescribeAvailableResource &RegionId=cn-hangzhou
```

| XML | format |
|---|---|
| <RequestId>344EE51D-8850-4935-B68B-58A8F4DCE3BD</RequestId> <SupportedDBTypes> <DbType>sharding</DbType> </SupportedDBTypes> <SupportedDBTypes> <AvailableZones> <ZoneId>cn-hangzhou-h</ZoneId> <RegionId>cn-hangzhou</RegionId> </AvailableZones> <AvailableZones> <SupportedEngineVersions> <Version>4.0</Version> </SupportedEngineVersions> <SupportedEngineVersions> <SupportedEngines> <Engine>WiredTiger</Engine> </SupportedEngines> <SupportedEngines> <SupportedNodeTypes> <NetworkTypes>VPC</NetworkTypes> <NodeType>3</NodeType> </SupportedNodeTypes> <SupportedNodeTypes> <AvailableResources> <InstanceClassRemark>8 vCPUs, 32 GiB (maximum connections: 8000 IOPS: 14000)</InstanceClassRemark> <InstanceClass>dds.mongo.2xlarge</InstanceClass> </AvailableResources> </SupportedNodeTypes> </SupportedEngines> </SupportedEngineVersions> </AvailableZones> </SupportedDBTypes> |   |

| JSON | format |
|---|---|
| { "RequestId":"344EE51D-8850-4935-B68B-58A8F4DCE3BD", "SupportedDBTypes":[ { "DbType":"sharding" }, { "AvailableZones":[ { "ZoneId":"cn-hangzhou-h", "RegionId":"cn-hangzhou" }, { "SupportedEngineVersions":[ { "Version":"4.0" }, { "SupportedEngines":[ { "Engine":"WiredTiger" }, { "SupportedNodeTypes":[ { "NetworkTypes":"VPC", "NodeType":"3" }, { "AvailableResources":[ { "InstanceClassRemark":"8 vCPUs, 32 GiB (maximum connections: 8000 IOPS: 14000)", "InstanceClass":"dds.mongo.2xlarge" } ] } ] } ] } ] } ] } ] } |   |

### 7.4 Connection management

#### 7.4.1 AllocatePublicNetworkAddress

Applies for a public endpoint for an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocatePublicNetworkAddres s | The operation that you want to perform. Set the value to AllocatePublicNetworkAddress. |
| DBInstanceId | String | Yes | dds-bp11501cd7b5**** | The instance ID. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | s-bp1713dece57**** | The ID of the mongos, shard, or Configserver node in the sharded cluster instance. Note This parameter is available only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. You can call the DescribeDBInstanceAttribute operation to query the ID of the mongos, shard, or Configserver node. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B6D17591-B48B-4D31-9CD6- 9B9796B2270A | The request ID. |

```
http(s)://mongodb.aliyuncs.com/?Action=AllocatePublicNetworkAddress &DBInstanceId=dds-bp11501cd7b5****
```

| XML | format |
|---|---|
| <RequestId>B6D17591-B48B-4D31-9CD6-9B9796B2270A</RequestId> |   |

| JSON | format |
|---|---|
| { "RequestId": "B6D17591-B48B-4D31-9CD6-9B9796B2270A" } |   |

#### 7.4.2 ReleasePublicNetworkAddress

You can call this operation to release the public endpoint of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleasePublicNetworkAddres s | The operation that you want to perform. Set the value to ReleasePublicNetworkAddress. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |

| NodeId | String | No | s-bpxxxxxxxx | A sharded cluster instance consists of three components: mongos, shard, and Configserver. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. You can call the DescribeDBInstanceAttribute operation to view the ID of the mongos, shard, or Configserver node. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1D6AFE36-1AF5-4DE4-A954- 672159D4CC69 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ReleasePublicNetworkAddress &s-bpxxxxxxxx
```

| XML | format |
|---|---|
| <ReleasePublicNetworkAddressResponse> <RequestId>B6D17591-B48B-4D31-9CD6-9B9796B2270A</RequestId> </ReleasePublicNetworkAddressResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "1D6AFE36-1AF5-4DE4-A954-672159D4CC69" } |   |

#### 7.4.3 ModifyInstanceVpcAuthMode

You can call this operation to enable or disable password-free access from the same VPC as an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: A replica set or sharded cluster instance is used. The database engine version of the instance is MongoDB 4.0 or 4.2. You can call the **DescribeDBInstanceAttribute** operation to view the database engine version of the instance. If necessary, you can call the **UpgradeDBInstanceEngineVersion** operation to upgrade the database engine. The network type of the instance must be VPC.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyInstanceVpcAuthMode | The operation that you want to perform. Set the value to ModifyInstanceVpcAuthMode. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeDBInstanceAttribute operation to view the region ID of the instance. |
| NodeId | String | No | s-bpxxxxxxxx | The ID of the mongos node in the sharded cluster instance. Note This parameter is valid only if you select a sharded cluster instance. |
| VpcAuthMode | String | No | Open | Specifies whether to enable password-free access within the VPC. Valid values: Open: enables password-free access within the VPC. Close: disables password-free access within the VPC. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | BA51E9D9-B14A-4542-B6E6- 7DE00BECCB8C | The ID of the request. |
|---|---|---|---|

```
http(s)://mongodb.example.com/? Action=ModifyInstanceVpcAuthMode &VpcAuthMode=Open
```

| XML | format |
|---|---|
| <ModifyInstanceVpcAuthModeResponse> <RequestId>BA51E9D9-B14A-4542-B6E6-7DE00BECCB8C</RequestId> </ModifyInstanceVpcAuthModeResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "BA51E9D9-B14A-4542-B6E6-7DE00BECCB8C" } |   |

#### 7.4.4 DescribeShardingNetworkAddress

You can call this operation to view the connection information of an ApsaraDB for MongoDB sharded cluster instance. This operation supports sharded cluster instances only.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeShardingNetworkAd dress | The operation that you want to perform. Set the value to DescribeShardingNetworkAddress. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos, shard, and Configserver node in the sharded cluster instance. Note You can call the DescribeDBInstanceAttribute operation to view the ID of the mongos, shard, or Configserver node. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CompatibleConnections | Array of CompatibleConnection |   | An array that consists of the endpoints of DynamoDB instances. |
| CompatibleConnection |   |   |   |
| ExpiredTime | String | 2591963 | The remaining period of the classic network endpoint. Unit: seconds. |
| IPAddress | String | 10.140.xxx.xx | The IP address of the instance. |
| NetworkAddress | String | dds- bpxxxxxxxxxxxxxx.mongodb.rds. aliyuncs.com | The endpoint of the instance. |
| NetworkType | String | VPC | The network type of the endpoint. Valid values: VPC Classic Public |
| Port | String | 3717 | The port number. |
| VPCId | String | vpc-bpxxxxxxxx | The ID of the VPC. Note This parameter is returned when the network type is VPC. |

| VswitchId | String | vsw-bpxxxxxxxx | The ID of the vSwitch in the specified VPC. Note This parameter is returned when the network type is VPC. |
|---|---|---|---|
| NetworkAddresses | Array of NetworkAddress |   | An array that consists of the endpoints of ApsaraDB for MongoDB instances. |
| NetworkAddress |   |   |   |
| ExpiredTime | String | 2591963 | The remaining period of the classic network endpoint. Unit: seconds. |
| IPAddress | String | 10.140.xxx.xx | The IP address of the instance. |
| NetworkAddress | String | s- bpxxxxxxxx.mongodb.rds.aliyunc s.com | The endpoint of the instance. |
| NetworkType | String | VPC | The network type of the endpoint. VPC Classic Public |
| NodeId | String | s-bpxxxxxxxx | The ID of the mongos node. |
| NodeType | String | mongos | The type of the node. Valid values: mongos shard configserver |
| Port | String | 3717 | The port number. |
| Role | String | Primary | The role of the node. Valid values: Primary Secondary |
| VPCId | String | vpc-bpxxxxxxxx | The ID of the VPC. Note This parameter is returned when the network type is VPC. |
| VswitchId | String | vsw-bpxxxxxxxx | The ID of the vSwitch in the specified VPC. Note This parameter is returned when the network type is VPC. |
| RequestId | String | 18D8AAFD-6BEB-420F-8164- 810CB0C0AA39 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=DescribeShardingNetworkAddress
```

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

| JSON | format |
|---|---|
| { "CompatibleConnections":[ { "NetworkAddress":"dds-bpxxxxxxxxxxxxxx.mongodb.rds.aliyuncs.com", "VPCId":"vpc-bpxxxxxxxx", "NetworkType":"VPC", "ExpiredTime":"2591963", "Port":"3717", "IPAddress":"10.140.xxx.xx", "VswitchId":"vsw-bpxxxxxxxx" } ], "RequestId":"18D8AAFD-6BEB-420F-8164-810CB0C0AA39", "NetworkAddresses":[ { "Role":"Primary", "NetworkAddress":"s-bpxxxxxxxx.mongodb.rds.aliyuncs.com", "VPCId":"vpc-bpxxxxxxxx", "NetworkType":"VPC", "NodeType":"mongos", "ExpiredTime":"2591963", "Port":"3717", "NodeId":"s-bpxxxxxxxx", "IPAddress":"10.140.xxx.xx", "VswitchId":"vsw-bpxxxxxxxx" } ] } |   |

#### 7.4.5 ModifyDBInstanceConnectionString

You can call this operation to modify the connection string of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanceConnection String | The operation that you want to perform. Set the value to ModifyDBInstanceConnectionString. |
| CurrentConnectionString | String | Yes | s- bpxxxxxxxx.mongodb.rds.ali yuncs.com | The current connection string, which is to be modified. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NewConnectionString | String | Yes | aliyuntest111 | The new connection string. It must be 8 to 64 characters in length and can contain letters and digits. It must start with a lowercase letter. Note You only need to specify the prefix of the connection string. The content other than the prefix cannot be modified. |

| NodeId | String | No | s-bpxxxxxxxx | The ID of the mongos node in the sharded cluster instance. Only one mongos ID can be specified in each call. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FF36A84C-0694-42D0-861D- C383E8E4FAAF | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceConnectionString &CurrentConnectionString=s-bpxxxxxxxx.mongodb.rds.aliyuncs.com &NewConnectionString=aliyuntest111
```

| XML | format |
|---|---|
| <ModifyDBInstanceConnectionStringResponse> <RequestId>FF36A84C-0694-42D0-861D-C383E8E4FAAF</RequestId> </ModifyDBInstanceConnectionStringResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "FF36A84C-0694-42D0-861D-C383E8E4FAAF" } |   |

#### 7.4.6 ReleaseNodePrivateNetworkAddress

Releases the internal endpoint of a shard or Configserver node in an ApsaraDB for MongoDB sharded cluster instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleaseNodePrivateNetwork Address | The operation that you want to perform. Set the value to ReleaseNodePrivateNetworkAddress. |
| DBInstanceId | String | Yes | dds-bp1a7009eb24**** | The ID of the sharded cluster instance. Note You can call the DescribeDBInstanceAttribute operation to query the instance ID. |
| NodeId | String | Yes | d-bp128a003436**** | The ID of the shard or Configserver node. Note You can call the DescribeDBInstanceAttribute operation to query the ID of the shard or Configserver node. |
| NetworkType | String | No | VPC | The network type of the internal endpoint. Valid values: VPC: Virtual Private Cloud (VPC) Classic: classic network |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252-4A4A-ADDA- 5CB1BF63873D | The request ID. |

```
http(s)://mongodb.aliyuncs.com/?Action=ReleaseNodePrivateNetworkAddress &DBInstanceId=dds-bp1a7009eb24**** &NodeId=d-bp128a003436**** &NetworkType=VPC
```

```xml
<ReleaseNodePrivateNetworkAddressResponse>
      <RequestId>EFD65226-08CC-4C4D-B6A4-CB3C382F67B0</RequestId>
</ReleaseNodePrivateNetworkAddressResponse>
```

| JSON | format |
|---|---|
| { "RequestId":"0FDDC511-7252-4A4A-ADDA-5CB1BF63873D" } |   |

### 7.5 Instance information query

#### 7.5.1 DescribeReplicaSetRole

You can call this operation to view the role and connection information of an ApsaraDB for MongoDB instance. This operation is applicable only to replica set instances, but not to sharded cluster instances.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeReplicaSetRole | The operation that you want to perform. Set the value to DescribeReplicaSetRole. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DB4A0595-FCA9-437F-B2BB- 25DBFC009D3E | The ID of the request. |
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |
| ReplicaSets | Array of ReplicaSet |   | An array that consists of the information of replica set instance roles. |
| ReplicaSet |   |   |   |
| ConnectionDomain | String | dds- bpxxxxxxxx.mongodb.rds.aliyunc s.com | The endpoint of the node. |
| ConnectionPort | String | 3717 | The port of the node. |
| ExpiredTime | String | 1209582 | The remaining period of the classic network endpoint. Unit: seconds. |
| NetworkType | String | VPC | The network type of the endpoint. Valid values: VPC Classic Public |
| ReplicaSetRole | String | Primary | The role of the node in the replica set instance. Primary Secondary |
| RoleId | String | 651xxxxx | The role ID of the node. |

```
http(s)://mongodb.example.com/? Action=DescribeReplicaSetRole
```

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

| JSON | format |
|---|---|
| { "RequestId": "7762D0FF-F34D-4DAF-9D06-6C1C28CC98CD", "DBInstanceId": "dds-bpxxxxxxxx", "ReplicaSets": { "ReplicaSet": [ { "NetworkType": "Classic", "ConnectionPort": "3717", "ReplicaSetRole": "Primary", "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com", "ExpiredTime": "12xxxxx", "RoleId": "55xxxxx" }, { "NetworkType": "Classic", "ConnectionPort": "3717", "ReplicaSetRole": "Secondary", "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com", "ExpiredTime": "12xxxxx", "RoleId": "55xxxxx" }, { "NetworkType": "VPC", "ConnectionPort": "3717", "ReplicaSetRole": "Primary", "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com", "RoleId": "55xxxxx" }, { "NetworkType": "VPC", "ConnectionPort": "3717", "ReplicaSetRole": "Secondary", "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com", "RoleId": "55xxxxx" } ] } } |   |

#### 7.5.2 DescribeKernelReleaseNotes

You can call this operation to view the release notes of the minor database versions of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeKernelReleaseNotes | The operation that you want to perform. Set the value to DescribeKernelReleaseNotes. |
| KernelVersion | String | No | mongodb201805220.4.8 _ _ | The minor version of the database. Example: mongodb201805220.4.8. _ _ If you specify this parameter, a list of versions later than the version specified is returned. If you do not specify this parameter, a list of all versions is returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ReleaseNotes | Array of ReleaseNote |   | An array that consists of the information of version release notes. |
| ReleaseNote |   |   |   |
| KernelVersion | String | mongodb201806190.4.9 _ _ | The version of the database. |
| ReleaseNote | String | Released the balancer switch limit for a sharded set | The release notes. |
| RequestId | String | F01D4DDA-CB72-4083-B399- AF4642294FE6 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=DescribeKernelReleaseNotes
```

| XML | format |
|---|---|
| <RequestId>F01D4DDA-CB72-4083-B399-AF4642294FE6</RequestId> <ReleaseNotes> <ReleaseNote> <KernelVersion>mongodb_20180619_0.4.9</KernelVersion> <ReleaseNote>Released the balancer switch limit for a sharded set</ReleaseNote> </ReleaseNote> </ReleaseNotes> |   |

| JSON | format |
|---|---|
| { "RequestId":"F01D4DDA-CB72-4083-B399-AF4642294FE6", "ReleaseNotes": { "ReleaseNote":[ { "KernelVersion":"mongodb_20180619_0.4.9", "ReleaseNote":"Released the balancer limit for a sharded set" } ] } } |   |

#### 7.5.3 DescribeAvailableEngineVersion

You can call this operation to view the database engine versions that an ApsaraDB for MongoDB instance can be upgraded to.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAvailableEngineVers ion | The operation that you want to perform. Set the value to DescribeAvailableEngineVersion. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 52507B6B-003B-47A3-A0A3- 9FE992C7A243 | The ID of the request. |

| EngineVersions | List | {"EngineVersion": ["4.0" ]} | The databse engine versions that the ApsaraDB for MongoDB instance can be upgraded to. Note An empty string is returned if the latest version is being used. |
|---|---|---|---|

```
http(s)://mongodb.example.com/? Action=DescribeAvailableEngineVersion
```

| XML | format |
|---|---|
| <DescribeAvailableEngineVersionResponse> <EngineVersions> <EngineVersion>4.0</EngineVersion> </EngineVersions> <RequestId>52507B6B-003B-47A3-A0A3-9FE992C7A243</RequestId> </DescribeAvailableEngineVersionResponse> |   |

| JSON | format |
|---|---|
| { "EngineVersions": { "EngineVersion": [ "4.0" ] }, "RequestId": "52507B6B-003B-47A3-A0A3-9FE992C7A243" } |   |

#### 7.5.4 DescribeDBInstances

Queries the list of ApsaraDB for MongoDB instances. When you call this operation, you must configure the `x-acs-organizationid` , `x-acs-resourcegroupid` , and `x-acs-instanceid` header parameters to specify the organization ID, resource group ID, and instance ID. Otherwise, the call is directed to the root resource group and organization. For more information about the code, see SDK Description in ApsaraDB for MongoDB Developer Guide.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstances | The operation that you want to perform. Set the value to DescribeDBInstances. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| DBInstanceId | String | No | dds-d1n4eab47879**** | The ID of the instance. |
| ReplicationFactor | String | No | 3 | The number of nodes in the replica set instance. Valid values: 3, 5, and 7. |
| DBInstanceDescription | String | No | test | The description of the instance. |
| ExpireTime | String | No | 2019-12-26T16:00Z | The time when the instance expires. |
| DBInstanceStatus | String | No | ACTIVATION | The status of the instance. For more information, see Instance states in ApsaraDB for MongoDB Developer Guide. |
| DBInstanceType | String | No | replicate | The architecture of the instance. Valid values: sharding: sharded cluster instance replicate: replica set instance or standalone instance Default value: replicate. |

| DBInstanceClass | String | No | dds.mongo.mid | The instance type. Note For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. |
|---|---|---|---|---|
| Engine | String | No | MongoDB | The database engine of the instance. Set the value to MongoDB. |
| EngineVersion | String | No | 4.2 | The database engine version of the instance. Valid values: 3.0, 3.4, 4.0, and 4.2. |
| NetworkType | String | No | Classic | The network type of the instance. Valid values: Classic VPC Set the value to Classic. |
| VpcId | String | No | vpc-bp1q2qqm4vxo6e6zl**** | The ID of the virtual private cloud (VPC). |
| VSwitchId | String | No | vsw-bp1buy0h9myt5i9e7**** | The ID of the vSwitch in the VPC. |
| ChargeType | String | No | PostPaid | The billing method of the instance. Valid values: PrePaid: subscription PostPaid: pay-as-you-go |
| ZoneId | String | No | cn-qd-agility14- amtest110**** | The zone ID of the instance. Note You can call the DescribeRegions operation to query available zones. |
| Expired | String | No | true | Specifies whether the instance has expired. Valid values: true: The instance has expired. false: The instance has not expired. |
| ResourceGroupId | String | No | rg-acfm22cdcgc**** | The ID of the resource group. |
| Tag.N.Key | String | No | testdatabase | The key of tag N. Note Valid values of N: 1 to 20. The tag key cannot exceed 64 characters in length. The tag key cannot start with aliyun , acs: , http:// , or https:// . The tag key cannot be an empty string. |
| Tag.N.Value | String | No | apitest | The value of tag N. Note Valid values of N: 1 to 20. The tag value cannot exceed 128 characters in length. The tag value cannot start with aliyun , acs: , http:// , or https:// . The tag value can be an empty string. |

| acs: , | http:// |
|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstances | Array of DBInstance |   | Details about the instances. |
| DBInstance |   |   |   |
| ChargeType | String | PostPaid | The billing method of the instance. PrePaid: subscription PostPaid: pay-as-you-go |
| CreationTime | String | 2021-05-31T12:00:52Z | The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |

| DBInstanceClass | String | dds.mongo.mid | The instance type. Note For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. |
|---|---|---|---|
| DBInstanceDescription | String | Test database | The description of the instance. |
| DBInstanceId | String | dds-d1n4eab47879**** | The ID of the instance. |
| DBInstanceStatus | String | Running | The status of the instance. |
| DBInstanceStorage | Integer | 50 | The storage space of the instance. |
| DBInstanceType | String | replicate | The architecture of the instance. Valid values: sharding: sharded cluster instance replicate: replica set instance |
| DestroyTime | String | 2021-12-31T16:00:00Z | The time when the instance data was destroyed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Note Subscription instances are released seven days after expiration. After an instance is released, its data is deleted and cannot be restored. Pay-as-you-go instances are locked after the payment has been overdue for longer than 24 hours. Pay-as-you-go instances are released after the payment has been overdue for longer than seven days. The data of released instances is deleted and cannot be restored. |
| Engine | String | MongoDB | The database engine of the instance. |
| EngineVersion | String | 3.0 | The database engine version of the instance. |
| ExpireTime | String | 2019-11-25T16:00Z | The time when the instance expires. The time follows the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| KindCode | String | 1 | The kind code of the instance. Valid values: 0: physical machine 1: Elastic Compute Service (ECS) instance 2: Docker cluster 18: Kubernetes cluster |
| LastDowngradeTime | String | 20210708 | The time when the instance was last downgraded. |
| LockMode | String | unlock | Indicates whether the instance is locked. Valid values: Unlock: The instance is not locked. ManualLock: The instance is manually locked. LockByExpiration: The instance is automatically locked after it expires. LockByRestoration: The instance is automatically locked before it is rolled back. LockByDiskQuota: The instance is automatically locked after the storage space is exhausted. Released: The instance is released. You cannot unlock an instance that is released. After an instance is released, you can only use a backup to restore the data of the instance to a new instance. This process requires a long period of time. |
| MongosList | Array of MongosAttribute |   | Details about the mongos nodes. Note This parameter is returned if the instance is a sharded cluster instance. |
| MongosAttribute |   |   |   |
| NodeClass | String | dds.mongos.mid | The type of the mongos node. |
| NodeDescription | String | Test mongos node | The description of the mongos node. |
| NodeId | String | s-d1n849c1788f**** | The ID of the mongos node. |

| NetworkType | String | Classic | The network type of the instance. The value is fixed atC lassic. |
|---|---|---|---|
| RegionId | String | cn-qd-agility14**** | The region ID of the instance. |
| ReplicationFactor | String | 3 | The number of nodes in the instance. Note This parameter is returned if the instance is a replica set instance. |
| ResourceGroupId | String | rg-acfm22cdcgc**** | The ID of the resource group. |
| ShardList | Array of ShardAttribute |   | Details about the shard nodes. Note This parameter is returned if the instance is a sharded cluster instance. |
| ShardAttribute |   |   |   |
| NodeClass | String | dds.shard.mid | The type of the shard node. |
| NodeDescription | String | Test shard node | The description of the shard node. |
| NodeId | String | d-d1n753c91603**** | The ID of the shard node. |
| NodeStorage | Integer | 20 | The storage space of the shard node. Unit: GB. |
| Tags | Array of Tag |   | Details about the resource tags. |
| Tag |   |   |   |
| Key | String | test | The tag key of the resource. |
| Value | String | api | The tag value of the resource. |
| VpcAuthMode | String | Close | Indicates whether password-free access within the VPC is enabled. Valid values: Open: Password-free access is enabled. Close: Password-free access is disabled. |
| ZoneId | String | cn-qd-agility14-amtest110**** | The zone ID of the instance. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 30 | The number of entries returned per page. |
| RequestId | String | A10B8ECB-0BA0-4EC6-93A5- C65FDEDA**** | The ID of the request. |
| TotalCount | Integer | 1 | The number of instances in the query results. |

```
http(s)://mongodb.example.com/?Action=DescribeDBInstances
```

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

```json
  "TotalCount": "1",
  "PageSize": "30",
  "RequestId": "A10B8ECB-0BA0-4EC6-93A5-C65FDEDA****",
  "PageNumber": "1",
  "DBInstances": [
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
          "NodeClass": "dds.shard.mid",
          "NodeDescription": "Test shard node",
          "NodeStorage": "20",
          "NodeId": "d-d1n753c91603****"
```

`],`

```json
      "MongosList": [
          "NodeClass": "dds.mongos.mid",
          "NodeDescription": "Test mongos node",
          "NodeId": "s-d1n849c1788f****"
```

`],`

```json
      "Tags": [
          "Value": "api",
          "Key": "test"
```

`]` `]`

#### 7.5.5 DescribeDBInstanceAttribute

Queries the details of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstanceAttribute | The operation that you want to perform. Set the value to DescribeDBInstanceAttribute. |
| DBInstanceId | String | Yes | dds-bp11483712c1**** | The instance ID. |
| Engine | String | No | MongoDB | The database engine. Set the value to MongoDB. |
| ResourceGroupId | String | No | rg-acfmyiu4ekp**** | The ID of the resource group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C373EED9-5125-4DD9-89DB- FB1ECD2C2B4F | The request ID. |
| DBInstances | Array of DBInstance |   | The information of the instances. |
| DBInstance |   |   |   |
| CpuType | String | intel | The CPU type of the instance. |

| ChargeType | String | PostPaid | The billing method of the instance. This parameter is set to PostPaid. |
|---|---|---|---|
| ConfigserverList | Array of ConfigserverAttrib ute |   | The information of the Configserver nodes. Note This parameter is returned if the instance is a sharded cluster instance. |
| ConfigserverAttribute |   |   |   |
| ConnectString | String | mongodb://root:****@dds- bp11483712c1****-cs1730- pub.mongodb.rds.aliyuncs.com :3717 | The endpoint of the Configserver node. |
| MaxConnections | Integer | 8000 | The maximum number of connections to the Configserver node. |
| MaxIOPS | Integer | 8000 | The maximum IOPS of the Configserver node. |
| NodeClass | String | dds.cs.mid | The specifications of the Configserver node. |
| NodeDescription | String | testConfigserver | The name of the Configserver node. |
| NodeId | String | dds-bp11483712c1****-cs | The ID of the Configserver node. |
| NodeStorage | Integer | 20 | The storage capacity of the Configserver node. Unit: GB. |
| Port | Integer | 3717 | The port number that is used to connect to the Configserver node. |
| CreationTime | String | 2022-08-21T05:10:00Z | The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| CurrentKernelVersion | String | mongodb201809141.1.5 _ _ | The kernel version of the instance. |
| DBInstanceClass | String | dds.mongo.mid | The instance type. |
| DBInstanceDescription | String | ceshi | The instance name. |
| DBInstanceId | String | dds-bp11483712c1**** | The instance ID. |
| DBInstanceReleasePro tection | Boolean | false | Indicates whether the release protection feature is enabled for the instance. Valid values: true false (default) |
| DBInstanceStatus | String | Running | The instance status. Valid values: Creating: The instance is being created. Running: The instance is running. DBInstanceClassChanging: The instance is being upgraded or downgraded. DBInstanceNetTypeChanging: The network type of the instance is being changed. Deleting: The instance is being deleted. EngineVersionUpgrading: The instance is being upgraded. GuardSwitching: The instance is undergoing a failover for disaster recovery. HASwitching: The instance is undergoing a primary/secondary switchover. ImportingFromOthers: Data from other databases is being imported into the instance. LinkSwitching: The instance is undergoing a link switching. MinorVersionUpgrading: The minor version of the instance is being updated. NETCREATING: A network connection to the instance is being established. _ NETDELETING: A network connection to the instance is being deleted. _ NodeCreating: A node is being created for the instance. NodeDeleting: A node is being deleted from the instance. Rebooting: The instance is being restarted. Restoring: The instance is being restored from a backup. SSLModifying: The SSL certificate of the instance is being modified. TempDBInstanceCreating: A temporary instance is being created. Transing: The instance is being migrated. TransingToOthers: Databases in the instance are being migrated. |
| DBInstanceStorage | Integer | 10 | The storage capacity of the instance. Unit: GB. |
| DBInstanceType | String | replicate | The architecture of the instance. Valid values: replicate: The instance is a replica set instance. sharding: The instance is a sharded cluster instance |
| Engine | String | MongoDB | The database engine of the instance. |

| EngineVersion | String | 3.4 | The database engine version of the instance. Valid values: 4.2 4.0 3.4 3.0 Note Only replica set instances support MongoDB 3.0. |
|---|---|---|---|
| ExpireTime | String | None | N/A |
| KindCode | String | 0 | The specification type of the instance. Set the value to 0. The value 0 indicates physical machine. |
| LastDowngradeTime | String | 2022-08-28 | The time when the instance was last downgraded. The time follows the ISO 8601 standard in the yyyy-MM-dd format. The time is displayed in UTC. |
| LockMode | String | Unlock | The lock state of the instance. Valid values: Unlock: The instance is not locked. ManualLock: The instance is manually locked. LockByExpiration: The instance is locked upon expiration. LockByRestoration: The instance is locked for a rollback. LockByDiskQuota: The instance is automatically locked because the storage space is exhausted. Released: The instance is released. After an instance is released, the instance cannot be unlocked. You can only restore the backup data of the instance to a new instance. This process requires an extended period of time. |
| MaintainEndTime | String | 03:00Z | The end time of the maintenance window. The time follows the ISO 8601 standard in the HH:mmZ format. The time is displayed in UTC. |
| MaintainStartTime | String | 02:00Z | The start time of the maintenance window. The time follows the ISO 8601 standard in the HH:mmZ format. The time is displayed in UTC. |
| MaxConnections | Integer | 500 | The maximum number of connections to the instance. |
| MaxIOPS | Integer | 1000 | The maximum IOPS of the instance. |
| MongosList | Array of MongosAttribute |   | The information of the mongos nodes. Note This parameter is returned if the instance is a sharded cluster instance. |
| MongosAttribute |   |   |   |
| ConnectSting | String | s- bp1d8c262a158****.mongodb.r ds.aliyuncs.com | The endpoint of the mongos node. |
| MaxConnections | Integer | 1000 | The maximum number of connections to the mongos node. |
| MaxIOPS | Integer | 800 | The maximum IOPS of the mongos node. |
| NodeClass | String | dds.mongos.mid | The instance type of the mongos node. |
| NodeDescription | String | mongos1 | The name of the mongos node. |
| NodeId | String | s-bp1d8c262a158**** | The ID of the mongos node. |
| Port | Integer | 3717 | The port number that is used to connect to the mongos node. |
| VPCId | String | vpc-bp1n3i15v90el48nx**** | The Virtual Private Cloud (VPC) ID of the mongos node. |
| VSwitchId | String | vsw-bp1n3i15v90el48nx**** | The vSwitch ID of the mongos node. |
| VpcCloudInstanceId | String | s-bp1d8c262a158**** | The ID of the mongos node. |
| NetworkType | String | VPC | The network type of the instance. Valid values: classic: classic network. VPC: VPC. |
| ProtocolType | String | mongodb | The access protocol type of the instance. Valid values: mongodb |
| ReadonlyReplicas | String | 0 | The number of read-only nodes in the instance. The value is set to0 . The value 0 indicates that read-only nodes are not supported. |
| RegionId | String | cn-qingdao-env17-d01 | The region ID of the instance. |
| ReplacateId | String | bls-mgs**** | The ID of the BLS channel. |
| ReplicaSetName | String | test | The name of the replica set instance. Note This parameter is returned if the instance is a replica set instance. |
| ReplicaSets | Array of ReplicaSet |   | The information of the replica set instances. Note This parameter is returned if the instance is a replica set instance. |

| ReplicaSet |   |   |   |
|---|---|---|---|
| ConnectionDomain | String | dds- bp11483712c1****.mongodb.rd s.aliyuncs.com | The endpoint of the node. |
| ConnectionPort | String | 3717 | The port number that is used to connect to the node. |
| NetworkType | String | VPC | The network type of the node. Valid values: classic VPC |
| ReplicaSetRole | String | Primary | The node role. Valid values: Primary: primary node. Secondary: secondary node. |
| VPCCloudInstanceId | String | vpc-bp1jk5vwkcri27qme**** | The ID of the instance in the VPC. |
| VPCId | String | vpc-bp1jk5vwkcri27qme**** | The VPC ID. |
| VSwitchId | String | vsw-bp1jk5vwkcri27qme**** | The vSwitch ID. |
| ReplicationFactor | String | 3 | The number of nodes in the instance. |
| ResourceGroupId | String | rg-a7qme**** | The ID of the resource group to which the instance belongs. |
| ShardList | Array of ShardAttribute |   | The information of the shard nodes. Note This parameter is returned if the instance is a sharded cluster instance. |
| ShardAttribute |   |   |   |
| ConnectString | String | d- bp1af0680a9c6d3****.mongod b.rds.aliyuncs.com | The endpoint of the shard node. |
| MaxConnections | Integer | 8000 | The maximum number of connections to the shard node. |
| MaxIOPS | Integer | 8000 | The maximum IOPS of the shard node. |
| NodeClass | String | dds.shard.mid | The instance type of the shard node. |
| NodeDescription | String | testshard | The name of the shard node. |
| NodeId | String | d-bp16e09d9c5d**** | The ID of the shard node. |
| NodeStorage | Integer | 10 | The storage capacity of the shard node. Unit: GB. |
| Port | Integer | 3717 | The port number that is used to connect to the shard node. |
| StorageEngine | String | WiredTiger | The storage engine of the instance. |
| Tags | Array of Tag |   | The information of the instance tags. |
| Tag |   |   |   |
| Key | String | test | The tag key of the instance. |
| Value | String | api | The tag value of the instance. |
| VPCId | String | vpc-bp1jk5vwkcri27qme**** | The VPC ID. |
| VSwitchId | String | vsw-bp1oo2a7isyrb8igf**** | The vSwitch ID. |
| VpcAuthMode | String | NotSupport | Indicates whether password-free access over the VPC is enabled. Valid values: Open: Password-free access is enabled. Close: Password-free access is disabled. NotSupport: Password-free access is not supported. |
| ZoneId | String | cn-qingdao-ft154e- amtest154001-a | The zone ID of the instance. |

```
http(s)://mongodb.example.com/?Action=DescribeDBInstanceAttribute &DBInstanceId=dds-bp11483712c1****
```

```xml
<DescribeDBInstanceAttributeResponse>
  <RequestId>C373EED9-5125-4DD9-89DB-FB1ECD2C2B4F</RequestId>
  <DBInstances>
    <ResourceGroupId>rg-a7qme****</ResourceGroupId>
    <DBInstanceType>replicate</DBInstanceType>
    <ReplicaSetName>test</ReplicaSetName>
    <StorageEngine>WiredTiger</StorageEngine>
    <MaintainEndTime>03:00Z</MaintainEndTime>
    <DBInstanceId>dds-bp11483712c1****</DBInstanceId>
    <NetworkType>VPC</NetworkType>
    <LastDowngradeTime>2022-08-28</LastDowngradeTime>
    <DBInstanceStorage>10</DBInstanceStorage>
    <CpuType>intel</CpuType>
    <MaintainStartTime>02:00Z</MaintainStartTime>
    <Engine>MongoDB</Engine>
    <DBInstanceDescription>ceshi</DBInstanceDescription>
    <ReplacateId>bls-mgs****</ReplacateId>
    <DBInstanceReleaseProtection>false</DBInstanceReleaseProtection>
    <EngineVersion>3.4</EngineVersion>
    <MaxConnections>500</MaxConnections>
    <ReadonlyReplicas>0</ReadonlyReplicas>
    <ReplicationFactor>3</ReplicationFactor>
    <DBInstanceStatus>Running</DBInstanceStatus>
    <ZoneId>cn-qingdao-ft154e-amtest154001-a</ZoneId>
    <VPCId>vpc-bp1jk5vwkcri27qme****</VPCId>
    <DBInstanceClass>dds.mongo.mid</DBInstanceClass>
    <VSwitchId>vsw-bp1oo2a7isyrb8igf****</VSwitchId>
    <LockMode>Unlock</LockMode>
    <MaxIOPS>1000</MaxIOPS>
    <VpcAuthMode>NotSupport</VpcAuthMode>
    <ProtocolType>mongodb</ProtocolType>
    <CurrentKernelVersion>mongodb_20180914_1.1.5</CurrentKernelVersion>
    <ChargeType>PostPaid</ChargeType>
    <CreationTime>2022-08-21T05:10:00Z</CreationTime>
    <RegionId>cn-qingdao-env17-d01</RegionId>
    <ExpireTime>2022-09-21T05:10Z</ExpireTime>
    <KindCode>0</KindCode>
    <ShardList>
        <NodeClass>dds.shard.mid</NodeClass>
        <NodeDescription>testshard</NodeDescription>
        <MaxConnections>8000</MaxConnections>
        <Port>3717</Port>
        <NodeStorage>10</NodeStorage>
        <NodeId>d-bp16e09d9c5d****</NodeId>
        <ConnectString>d-bp1af0680a9c6d3****.mongodb.rds.aliyuncs.com</ConnectString>
        <MaxIOPS>8000</MaxIOPS>
    </ShardList>
    <ConfigserverList>
        <NodeClass>dds.cs.mid</NodeClass>
        <NodeDescription>testConfigserver</NodeDescription>
        <MaxConnections>8000</MaxConnections>
        <Port>3717</Port>
        <NodeStorage>20</NodeStorage>
        <NodeId>dds-bp11483712c1****</NodeId>
        <ConnectString>mongodb://root:****@dds-bp11483712c1****-cs1730-pub.mongodb.rds.aliyuncs.com:3717</ConnectString>
        <MaxIOPS>8000</MaxIOPS>
    </ConfigserverList>
    <MongosList>
        <ConnectSting>s-bp1d8c262a158****.mongodb.rds.aliyuncs.com</ConnectSting>
        <NodeClass>dds.mongos.mid</NodeClass>
        <NodeDescription>mongos1</NodeDescription>
        <MaxConnections>1000</MaxConnections>
        <VPCId>vpc-bp1n3i15v90el48nx****</VPCId>
        <VSwitchId>vsw-bp1n3i15v90el48nx****</VSwitchId>
        <Port>3717</Port>
        <NodeId>s-bp1d8c262a158****</NodeId>
        <VpcCloudInstanceId>s-bp1d8c262a158****</VpcCloudInstanceId>
        <MaxIOPS>800</MaxIOPS>
    </MongosList>
    <Tags>
        <Value>api</Value>
        <Key>test</Key>
    </Tags>
    <ReplicaSets>
        <ConnectionDomain>dds-bp11483712c1****.mongodb.rds.aliyuncs.com</ConnectionDomain>
        <ReplicaSetRole>Primary</ReplicaSetRole>
        <VPCCloudInstanceId>vpc-bp1jk5vwkcri27qme****</VPCCloudInstanceId>
        <VPCId>vpc-bp1jk5vwkcri27qme****</VPCId>
        <ConnectionPort>3717</ConnectionPort>
        <NetworkType>VPC</NetworkType>
        <VSwitchId>vsw-bp1jk5vwkcri27qme****</VSwitchId>
    </ReplicaSets>
  </DBInstances>
</DescribeDBInstanceAttributeResponse>
```

| JSON | format |
|---|---|
| { "RequestId": "C373EED9-5125-4DD9-89DB-FB1ECD2C2B4F", "DBInstances": { "ResourceGroupId": "rg-a7qme****", "DBInstanceType": "replicate", "ReplicaSetName": "test", "StorageEngine": "WiredTiger", "MaintainEndTime": "03:00Z", "DBInstanceId": "dds-bp11483712c1****", "NetworkType": "VPC", "LastDowngradeTime": "2022-08-28", "DBInstanceStorage": 10, "CpuType": "intel", "MaintainStartTime": "02:00Z", "Engine": "MongoDB", "DBInstanceDescription": "ceshi", "ReplacateId": "bls-mgs****", "DBInstanceReleaseProtection": false, "EngineVersion": 3.4, "MaxConnections": 500, "ReadonlyReplicas": 0, "ReplicationFactor": 3, "DBInstanceStatus": "Running", "ZoneId": "cn-qingdao-ft154e-amtest154001-a", "VPCId": "vpc-bp1jk5vwkcri27qme****", "DBInstanceClass": "dds.mongo.mid", "VSwitchId": "vsw-bp1oo2a7isyrb8igf****", "LockMode": "Unlock", "MaxIOPS": 1000, "VpcAuthMode": "NotSupport", "ProtocolType": "mongodb", "CurrentKernelVersion": "mongodb_20180914_1.1.5", "ChargeType": "PostPaid", "CreationTime": "2022-08-21T05:10:00Z", "RegionId": "cn-qingdao-env17-d01", "ExpireTime": "2022-09-21T05:10Z", "KindCode": 0, "ShardList": { "NodeClass": "dds.shard.mid", "NodeDescription": "testshard", "MaxConnections": 8000, "Port": 3717, "NodeStorage": 10, "NodeId": "d-bp16e09d9c5d****", "ConnectString": "d-bp1af0680a9c6d3****.mongodb.rds.aliyuncs.com", "MaxIOPS": 8000 }, "ConfigserverList": { "NodeClass": "dds.cs.mid", "NodeDescription": "testConfigserver", "MaxConnections": 8000, "Port": 3717, "NodeStorage": 20, "NodeId": "dds-bp11483712c1****", "ConnectString": "mongodb://root:****@dds-bp11483712c1****-cs1730-pub.mongodb.rds.aliyuncs.com:3717", "MaxIOPS": 8000 }, "MongosList": { "ConnectSting": "s-bp1d8c262a158****.mongodb.rds.aliyuncs.com", "NodeClass": "dds.mongos.mid", "NodeDescription": "mongos1", "MaxConnections": 1000, "VPCId": "vpc-bp1n3i15v90el48nx****", "VSwitchId": "vsw-bp1n3i15v90el48nx****", "Port": 3717, "NodeId": "s-bp1d8c262a158****", "VpcCloudInstanceId": "s-bp1d8c262a158****", "MaxIOPS": 800 }, "Tags": { "Value": "api", "Key": "test" }, "ReplicaSets": { "ConnectionDomain": "dds-bp11483712c1****.mongodb.rds.aliyuncs.com", "ReplicaSetRole": "Primary", "VPCCloudInstanceId": "vpc-bp1jk5vwkcri27qme****", "VPCId": "vpc-bp1jk5vwkcri27qme****", "ConnectionPort": 3717, "NetworkType": "VPC", "VSwitchId": "vsw-bp1jk5vwkcri27qme****" } }} |   |

#### 7.5.6 DescribeRoleZoneInfo

You can call this operation to view the roles and zones of nodes in an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRoleZoneInfo | The operation that you want to perform. Set the value to DescribeRoleZoneInfo. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 728B9A96-E262-4AE5-915E- 3A51CCE2FDA9 | The ID of the request. |
| ZoneInfos | Array of ZoneInfo |   | An array that consists of information of nodes in the zone. |
| ZoneInfo |   |   |   |
| InsName | String | dds-bpxxxxxxxx | The ID of the node. |
| NodeType | String | normal | The type of the node. Valid values: normal configServer shard mongos Note Valid value for replica set instances: normal. Valid values for sharded cluster instances: configServer, shard, and mongos. |
| RoleId | String | 83xxxxx | The ID of the role. |
| RoleType | String | Primary | The role of the node. Valid values: Primary Secondary Hidden |
| ZoneId | String | cn-hangzhou-e | The zone ID. |

```
http(s)://mongodb.example.com/? Action=DescribeRoleZoneInfo
```

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

| JSON | format |
|---|---|
| { "ZoneInfos": { "ZoneInfo": [ { "RoleType": "Primary", "NodeType": "normal", "InsName": "dds-bpxxxxxxxx", "ZoneId": "cn-hangzhou-e", "RoleId": "83xxxxx" }, { "RoleType": "Secondary", "NodeType": "normal", "InsName": "dds-bpxxxxxxxx", "ZoneId": "cn-hangzhou-f", "RoleId": "83xxxxx" }, { "RoleType": "Hidden", "NodeType": "normal", "InsName": "dds-bpxxxxxxxx", "ZoneId": "cn-hangzhou-b", "RoleId": "83xxxxx" } ] }, "RequestId": "728B9A96-E262-4AE5-915E-3A51CCE2FDA9" } |   |

### 7.6 Instance management

#### 7.6.1 RestartDBInstance

You can call this operation to restart an ApsaraDB for MongoDB instance. This operation can also be used to restart a shard or mongos node in a replica set instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RestartDBInstance | The operation that you want to perform. Set the value to RestartDBInstance. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard or mongos node in the sharded cluster instance. Note The sharded cluster instance will be restarted if this parameter is not specified. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 149C517D-B586-47BE-A107- 8673E0ED77C6 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=RestartDBInstance
```

| XML | format |
|---|---|
| <RestartDBInstanceResponse> <RequestId>149C517D-B586-47BE-A107-8673E0ED77C6</RequestId> </RestartDBInstanceResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "149C517D-B586-47BE-A107-8673E0ED77C6" } |   |

#### 7.6.2 ModifyDBInstanceMaintainTime

You can call this operation to modify the maintenance window of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanceMaintainTi me | The operation that you want to perform. Set the value to ModifyDBInstanceMaintainTime. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| MaintainEndTime | String | Yes | 02:00Z | The end time of the maintenance window. Specify the time in the HH:mmZ format. The time must be in UTC. Note The difference between the start time and end time must be one hour. For example, if MaintainStartTime is 01:00Z, MaintainEndTime must be 02:00Z. |
| MaintainStartTime | String | Yes | 01:00Z | The start time of the maintenance window. Specify the time in the HH:mmZ format. The time must be in UTC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A9310426-C763-42A2-A3AD- 70A8DA204531 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceMaintainTime &MaintainStartTime=01:00Z &MaintainEndTime=02:00Z
```

| XML | format |
|---|---|
| <ModifyDBInstanceMaintainTimeResponse> <RequestId>A9310426-C763-42A2-A3AD-70A8DA204531</RequestId> </ModifyDBInstanceMaintainTimeResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "A9310426-C763-42A2-A3AD-70A8DA204531" } |   |

#### 7.6.3 ModifyDBInstanceDescription

You can call this operation to change the name of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanceDescription | The operation that you want to perform. Set the value to ModifyDBInstanceDescription. |
| DBInstanceDescription | String | Yes | testdata | The name of the instance. Note The name cannot start with http:// or https://. The name must start with a letter. It can contain letters, underscores (), hyphens (-), _ and digits. It must be 2 to 256 characters in length. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you want to modify the name of a shard or mongos node in a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard or mongos node in the sharded cluster instance. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 06F8F642-4009-4FFC-80C4- 9D67DBF7B74E | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceDescription &DBInstanceDescription=testdata
```

| XML | format |
|---|---|
| <ModifyDBInstanceDescriptionResponse> <RequestId>06F8F642-4009-4FFC-80C4-9D67DBF7B74E</RequestId> </ModifyDBInstanceDescriptionResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "06F8F642-4009-4FFC-80C4-9D67DBF7B74E" } |   |

#### 7.6.4 SwitchDBInstanceHA

You can call this operation to switch between the primary and secondary nodes in an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation.

> **Note:** On replica set instances, the switch is performed between primary and secondary instances. On sharded cluster instances, the switch is performed between primary and secondary shard nodes.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SwitchDBInstanceHA | The operation that you want to perform. Set the value to SwitchDBInstanceHA. |

| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
|---|---|---|---|---|
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard node in the sharded cluster instance. Note If you set the DBInstanceId parameter to the ID of a sharded cluster instance, you must specify this parameter. |
| RoleIds | String | No | 972xxxx,972xxxx | The IDs of the roles that you want to switch. You can call the DescribeRoleZoneInfo operation to view the IDs and information of roles of nodes. Note Separate role IDs with commas (,). If this parameter is not specified, the primary and secondary nodes are switched. If you set the DBInstanceId parameter to the ID of a sharded cluster instance, the roles to be switched must belong to one shard node. |
| SwitchMode | Integer | No | 0 | The time when roles of the primary and secondary nodes are switched. Valid values: 0: The roles are switched immediately. 1: The roles are switched during the maintenance period. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 26BD4E5F-BDB4-47BA-B232- 413AA78CFA8F | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=SwitchDBInstanceHA
```

| XML | format |
|---|---|
| <SwitchDBInstanceHAResponse> <RequestId>26BD4E5F-BDB4-47BA-B232-413AA78CFA8F</RequestId> </SwitchDBInstanceHAResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "26BD4E5F-BDB4-47BA-B232-413AA78CFA8F" } |   |

#### 7.6.5 UpgradeDBInstanceEngineVersion

You can call this operation to upgrade the database version of an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation.

> **Note:** The available database versions are subject to the storage engine used by the instance. You can call the **DescribeAvailableEngineVersion** operation to view the available database versions.
> The database version cannot be downgraded after it is upgraded.
> The instance is automatically restarted for two to three times during the upgrade process. Make sure that you upgrade the instance during off-peak hours.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpgradeDBInstanceEngineVe rsion | The operation that you want to perform. Set the value to UpgradeDBInstanceEngineVersion. |

| EngineVersion | String | Yes | 4.2 | The new database engine version of the instance. Valid values: 3.4, 4.0, and 4.2. Note The new database engine version must be later than the current version. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C4907B00-A208-4E0C-A636- AA85140E406C | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=UpgradeDBInstanceEngineVersion &EngineVersion=4.0
```

| XML | format |
|---|---|
| <UpgradeDBInstanceEngineVersionResponse> <RequestId>C4907B00-A208-4E0C-A636-AA85140E406C</RequestId> </UpgradeDBInstanceEngineVersionResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "C4907B00-A208-4E0C-A636-AA85140E406C" } |   |

#### 7.6.6 UpgradeDBInstanceKernelVersion

You can call this operation to upgrade the minor database version of an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation.

> **Note:** The instance will be restarted once during the upgrade. Perform this operation during off-peak hours.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpgradeDBInstanceKernelVer sion | The operation that you want to perform. Set the value to UpgradeDBInstanceKernelVersion. |
| DBInstanceId | String | No | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 27B9A130-7C4B-40D9-84E8- 2FC081097AAC | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=UpgradeDBInstanceKernelVersion
```

| XML | format |
|---|---|
| <UpgradeDBInstanceKernelVersionResponse> <RequestId>27B9A130-7C4B-40D9-84E8-2FC081097AAC</RequestId> </UpgradeDBInstanceKernelVersionResponse> |   |

```json
 "RequestId": "27B9A130-7C4B-40D9-84E8-2FC081097AAC"
```

#### 7.6.7 ModifyDBInstanceNetExpireTime

You can call this operation to extend the retention period of the classic network of an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: The instance must be running. The network of the instance is in hybrid access mode.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanceNetExpireTi me | The operation that you want to perform. Set the value to ModifyDBInstanceNetExpireTime. |
| ClassicExpendExpiredDays | Integer | Yes | 30 | The retention period of the original classic network address. Valid values: 14, 30, 60, and 120. Unit: day. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| ConnectionString | String | No | dds- bpxxxxxxxx.mongodb.rds.ali yuncs.com | The connection address of the instance |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 459E7D5C-38DA-4E14-9C82- 5B5AF693DBAB | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceNetExpireTime &ClassicExpendExpiredDays=30
```

| XML | format |
|---|---|
| <ModifyDBInstanceNetExpireTimeResponse> <RequestId>459E7D5C-38DA-4E14-9C82-5B5AF693DBAB</RequestId> </ModifyDBInstanceNetExpireTimeResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "459E7D5C-38DA-4E14-9C82-5B5AF693DBAB" } |   |

### 7.7 Account management

#### 7.7.1 DescribeAccounts

You can call this operation to view the information of the database account of an ApsaraDB for MongoDB instance.

> **Note:** This operation can display only the information of the root account.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccounts | The operation that you want to perform. Set the value to DescribeAccounts. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| AccountName | String | No | root | The name of the account. Set the value to root. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Accounts | Array of Account |   | An array that consists of the information of accounts. |
| Account |   |   |   |
| AccountDescription | String | Administrator | The description of the account. |
| AccountName | String | root | The name of the account. |
| AccountStatus | String | Available | The status of the account. Unavailable Available |
| CharacterType | String | normal | The role of the account. Valid values: db: the shard node cs: the Configserver node mongos: the mongos node logic: the sharded cluster instance normal: the replica set instance |
| DBInstanceId | String | dds-bpxxxxxxxx | The name of the instance to which the account belongs. |
| RequestId | String | B562A65B-39AB-4EE8-8635- 5A222054FB35 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=DescribeAccounts
```

| XML | format |
|---|---|
| <DescribeAccountsResponse> <Accounts> <Account> <AccountStatus>Available</AccountStatus> <AccountDescription>Administrator</AccountDescription> <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId> <AccountName>root</AccountName> </Account> </Accounts> <RequestId>A806B0FC-CFCC-48D8-8AEC-34C892806B40</RequestId> </DescribeAccountsResponse> |   |

| JSON | format |
|---|---|
| { "Accounts": { "Account": [ { "AccountStatus": "Available", "AccountDescription": "Administrator", "DBInstanceId": "dds-bpxxxxxxxx", "AccountName": "root" } ] }, "RequestId": "A806B0FC-CFCC-48D8-8AEC-34C892806B40" } |   |

#### 7.7.2 ResetAccountPassword

You can call this operation to reset the password of the root account of an ApsaraDB for MongoDB instance.

> **Note:** This operation can reset only the password of the root account of an instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetAccountPassword | The operation that you want to perform. Set the value to ResetAccountPassword. |

| AccountName | String | Yes | root | The account for which you want to reset the password. Set the value to root. |
|---|---|---|---|---|
| AccountPassword | String | Yes | Ali! 123456 | The new password. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! # $ % ^ & * ( ) _ + - = #$%^&*()_+-= The password must be 8 to 32 characters in length. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

|   | % ^ & * ( ) _ + - = #$%^&*()_+-= |
|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 06CBD06E-ABC9-4121-AB93- 3C3820B3E7E6 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ResetAccountPassword &AccountName=root &AccountPassword=Ali! 123456
```

| XML | format |
|---|---|
| <ResetAccountPasswordResponse> <RequestId>06CBD06E-ABC9-4121-AB93-3C3820B3E7E6</RequestId> </ResetAccountPasswordResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "06CBD06E-ABC9-4121-AB93-3C3820B3E7E6" } |   |

#### 7.7.3 ModifyAccountDescription

You can call this operation to modify the description of the root account of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAccountDescription | The operation that you want to perform. Set the value to ModifyAccountDescription. |
| AccountDescription | String | Yes | superadmin | The description of the account. It cannot start with http:// or https://. The description must start with a letter. It must be 2 to 256 characters in length and can contain letters, digits, underscores (), and hyphens (-). _ |
| AccountName | String | Yes | root | The name of the account for which you want to modify the description. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 59DE9FC2-7B40-45CF-9011- 7327A8A771A2 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ModifyAccountDescription &AccountName=root &AccountDescription=superadmin
```

| XML | format |
|---|---|
| <RestoreDBInstanceResponse> <RequestId>59DE9FC2-7B40-45CF-9011-7327A8A771A2</RequestId> </RestoreDBInstanceResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "59DE9FC2-7B40-45CF-9011-7327A8A771A2" } |   |

### 7.8 IP whitelists and security groups

#### 7.8.1 DescribeSecurityGroupConfiguration

You can call this operation to view ECS security groups to which an ApsaraDB for MongoDB instance is added.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurityGroupConfig uration | The operation that you want to perform. Set the value to DescribeSecurityGroupConfiguration. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of RdsEcsSecurityGroupRel |   | The information list of the ECS security group. |
| RdsEcsSecurityGroupRel |   |   |   |
| NetType | String | vpc | The network type of the ECS security group. Valid values: vpc classic |
| RegionId | String | cn-hangzhou | The region ID of the ECS security group. |
| SecurityGroupId | String | sg-bpxxxxxxxx | The ID of the ECS security group. |
| RequestId | String | 3C4A2494-85C4-45C5-93CF- 548DB3375193 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=DescribeSecurityGroupConfiguration
```

| XML | format |
|---|---|
| <Items> <RdsEcsSecurityGroupRel> <SecurityGroupId>sg-bpxxxxxxxx</SecurityGroupId> <RegionId>cn-hangzhou</RegionId> <NetType>classic</NetType> </RdsEcsSecurityGroupRel> </Items> <RequestId>D18F5B88-ACA6-470E-9493-384412EDD902</RequestId> |   |

```json
 "Items": {
  "RdsEcsSecurityGroupRel": [
    "SecurityGroupId": "sg-bpxxxxxxxx",
    "RegionId": "cn-hangzhou",
    "NetType": "classic"
```

`]` `},`

```json
 "RequestId": "D18F5B88-ACA6-470E-9493-384412EDD902"
```

#### 7.8.2 ModifySecurityGroupConfiguration

You can call this operation to modify the ECS Security group that is bound to an ApsaraDB for MongoDB instance.

> **Note:** For a sharded cluster instance, the bound ECS security group takes effect only for the mongos node.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySecurityGroupConfigur ation | The operation that you want to perform. Set the value toModifySecurityGroupConfiguration. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| SecurityGroupId | String | Yes | sg-bpxxxxxxxx | The ID of the ECS security group. Note Only one ECS Security Group can be bound to an instance. You can view the security groups in the specified region by calling theDescribeSecurityGroup operation of ECS. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E062C482-1A4B-469E-938C- 96D28CFAE42E | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ModifySecurityGroupConfiguration &SecurityGroupId=sg-bpxxxxxxxx
```

| XML | format |
|---|---|
| <RequestId>E062C482-1A4B-469E-938C-96D28CFAE42E</RequestId> |   |

| JSON | format |
|---|---|
| { "RequestId": "E062C482-1A4B-469E-938C-96D28CFAE42E" } |   |

#### 7.8.3 DescribeSecurityIps

You can call this operation to view the IP whitelist of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurityIps | The operation that you want to perform. Set the value to DescribeSecurityIps. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| SecurityIpGroups | Array of SecurityIpGroup |   | An array that consists of the information of IP whitelists. |
| SecurityIpGroup |   |   |   |
| SecurityIpGroupAttribute | String | hidden | The attribute of the IP whitelist. This parameter is empty by default. |
| SecurityIpGroupName | String | default | The name of the whitelist. |
| SecurityIpList | String | 47.xxx.xxx.xx,100.xxx.xxx.0/24 | The IP addresses in the whitelist. |
| SecurityIps | String | 47.xxx.xxx.xx,100.xxx.xxx.0/24 | The IP addresses in the default whitelist. |
| RequestId | String | FC724D23-2962-479E-ABB1- 606C935AE7FD | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=DescribeSecurityIps
```

| XML | format |
|---|---|
| <DescribeSecurityIpsResponse> <SecurityIpGroups> <SecurityIpGroup> <SecurityIpList>114.xxx.xxx.xx</SecurityIpList> <SecurityIpGroupAttribute></SecurityIpGroupAttribute> <SecurityIpGroupName>allowserver</SecurityIpGroupName> </SecurityIpGroup> <SecurityIpGroup> <SecurityIpList>47.xxx.xxx.xx,100.xxx.xxx.0/24</SecurityIpList> <SecurityIpGroupAttribute></SecurityIpGroupAttribute> <SecurityIpGroupName>default</SecurityIpGroupName> </SecurityIpGroup> </SecurityIpGroups> <SecurityIps>47.xxx.xxx.xx,100.xxx.xxx.0/24</SecurityIps> <RequestId>FC724D23-2962-479E-ABB1-606C935AE7FD</RequestId> </DescribeSecurityIpsResponse> |   |

| JSON | format |
|---|---|
| { "SecurityIpGroups": { "SecurityIpGroup": [ { "SecurityIpList": "114.xxx.xxx.xx", "SecurityIpGroupAttribute": "", "SecurityIpGroupName": "allowserver" }, { "SecurityIpList": "47.xxx.xxx.xx,100.xxx.xxx.0/24", "SecurityIpGroupAttribute": "", "SecurityIpGroupName": "default" } ] }, "SecurityIps": "47.xxx.xxx.xx,100.xxx.xxx.0/24", "RequestId": "FC724D23-2962-479E-ABB1-606C935AE7FD" } |   |

#### 7.8.4 ModifySecurityIps

You can call this operation to modify the IP whitelist of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySecurityIps | The operation that you want to perform. Set the value to ModifySecurityIps. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| SecurityIps | String | Yes | 10.23.12.24/24,10.22.22.22 | The IP addresses in an IP whitelist. Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to a whitelist. You can add IP addresses in one of the following two formats: IP addresses. Example: 10.23.12.24. Classless Inter-Domain Routing (CIDR) blocks, such as 10.23.12.24/24. /24 indicates the length of the IP address prefix in the CIDR block. An IP address prefix can contain 1 to 32 bits. |
|---|---|---|---|---|
| ModifyMode | String | No | Append | The method of modification. Valid values: Cover: overwrites the whitelist. Append: appends data to the whitelist. Delete: deletes the whitelist. The default value is Cover. |
| SecurityIpGroupName | String | No | allowserver | The name of the IP whitelist to be modified. The default value is default. |
| SecurityIpGroupAttribute | String | No | test | The attributes of an IP whitelist. It can contain a maximum of 120 characters in length and can contain uppercase letters, lowercase letters, and digits. This parameter is empty by default. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 61B05CCF-EBAB-4BF3-BA67- D77256A721E2 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ModifySecurityIps &SecurityIps=10.23.12.24/24,10.22.22.22
```

| XML | format |
|---|---|
| <ModifySecurityIpsResponse> <RequestId>61B05CCF-EBAB-4BF3-BA67-D77256A721E2</RequestId> </ModifySecurityIpsResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "61B05CCF-EBAB-4BF3-BA67-D77256A721E2" } |   |

### 7.9 Key management

#### 7.9.1 DescribeDBInstanceTDEInfo

You can call this operation to view whether TDE is enabled for an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: A replica set or sharded cluster instance is used. The storage engine of the instance is WiredTiger. The database engine version of the instance is 4.0 or 4.2. If the database engine version of your instance is earlier than 4.0, you can call the
**UpgradeDBInstanceEngineVersion** operation to upgrade the database engine.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstanceTDEInfo | The operation that you want to perform. Set the value to DescribeDBInstanceTDEInfo. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | F4DD0E29-361B-42F2-9301- B0048CCCE5D6 | The ID of the request. |
|---|---|---|---|
| TDEStatus | String | enabled | The TDE status. Valid values: enabled disabled |

```
http(s)://mongodb.example.com/? Action=DescribeDBInstanceTDEInfo
```

| XML | format |
|---|---|
| <TDEStatus>enabled</TDEStatus> <RequestId>F4DD0E29-361B-42F2-9301-B0048CCCE5D6</RequestId> |   |

| JSON | format |
|---|---|
| { "TDEStatus":"enabled", "RequestId":"F4DD0E29-361B-42F2-9301-B0048CCCE5D6" } |   |

#### 7.9.2 ModifyDBInstanceTDE

You can call this operation to modify the transparent data encryption (TDE) status of an ApsaraDB for MongoDB instance. Before data files are written to disks, transparent data encryption (TDE) encrypts the data files. When data files are loaded from disks to the memory, TDE decrypts the data files.

> **Note:** After TDE is enabled, it cannot be disabled.

Before you call this operation, make sure that the following requirements are met: A replica set or sharded cluster instance is used. The storage engine of the instance is WiredTiger. The database engine version of the instance is 4.0 or 4.2. If the database engine version is earlier than 4.0, you can call the
**UpgradeDBInstanceEngineVersion** operation to upgrade the database engine.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanceTDE | The operation that you want to perform. Set the value to ModifyDBInstanceTDE. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| TDEStatus | String | Yes | enabled | The TDE status. Set the value to Enabled. Note After TDE is enabled, it cannot be disabled. Proceed with caution. |
| EncryptorName | String | No | aes-256-cbc | The encryption method. Set the value to aes-256-cbc. Note This parameter is valid only when you set the TEDStatus parameter to enabled. |
| EncryptionKey | String | No | 749c1df7-xxxx-xxxx-xxxx- xxxxxxxxxxxx | The custom key. |

| RoleARN | String | No | acs:ram::123456789012****: role/adminrole | The ARN of the role. It is in the format of acs:ram::$accountID:role/$roleName . Note $accountID : indicates the ID of the Alibaba Cloud account that owns the RAM role. To view the account ID, log on to the Alibaba Cloud Management Console, move your pointer over your profile picture in the upper-right corner, and then click Security Settings. $roleName : indicates the name of the RAM role. To view the RAM role name, perform the following steps: Log on to the RAM console. In the left-side navigation pane, click RAM Roles. In the RAM Role Name column on the page that appears, you can view the name of the RAM role. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 434D7127-6229-4355-BA50- 7A3685A725DF | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceTDE &TDEStatus=enabled
```

| XML | format |
|---|---|
| <ModifyDBInstanceTDEResponse> <RequestId>434D7127-6229-4355-BA50-7A3685A725DF</RequestId> </ModifyDBInstanceTDEResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "434D7127-6229-4355-BA50-7A3685A725DF" } |   |

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectDBInstanceState | Current DB instance state does not support this operation. | The error message returned because the operation is not supported while the instance is in its current state. Check whether the specified parameters are correct. |
| 403 | IncorrectDBInstanceLockMode | Current DB instance lock mode does not support this operation. | The error message returned because the instance is locked. |

### 7.10 SSL encryption

#### 7.10.1 ModifyDBInstanceSSL

You can call this operation to modify the SSL settings of an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. A replica set instance is used. The database engine version of the instance is 3.4, 4.0, or 4.2.

> **Note:** Whenever you enable or disable SSL encryption, or update the SSL certificate, the instance will restart. We recommend that you call this operation during off-peak hours.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanceSSL | The operation that you want to perform. Set the value to DescribeDBInstanceSSL. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| SSLAction | String | Yes | Open | The operation that you perform for the SSL feature. Valid values: Open: enables SSL encryption. Close: disables SSL encryption. Update: updates the SSL certificate. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6D806B11-078F-4154-BF9F- 844F56D08964 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceSSL &SSLAction=Open
```

| XML | format |
|---|---|
| <ModifyDBInstanceSSLResponse> <RequestId>6D806B11-078F-4154-BF9F-844F56D08964</RequestId> </ModifyDBInstanceSSLResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "6D806B11-078F-4154-BF9F-844F56D08964" } |   |

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectDBInstanceState | Current DB instance state does not support this operation. | The error message returned because the operation is not supported while the instance is in its current state. Check whether the specified parameters are correct. |
| 403 | IncorrectDBInstanceLockMode | Current DB instance lock mode does not support this operation. | The error message returned because the instance is locked. |

#### 7.10.2 DescribeDBInstanceSSL

You can call this operation to view the SSL settings of an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: The primary instance must be in the Running state. A replica set instance is used. The database engine version of the instance is 3.4, 4.0, or 4.2.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstanceSSL | The operation that you want to perform. Set the value to DescribeDBInstanceSSL. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| SSLExpiredTime | String | 2020-03-11T02:28:25Z | The time when the SSL certificate expires. The time is in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| RequestId | String | 36BB1BC2-789C-4BBA-A519- C5B388E4B0D4 | The ID of the request. |
| SSLStatus | String | Open | The status of the SSL feature. Valid values: Open: The SSL feature is enabled. Closed: The SSL feature is disabled. |

| CertCommonName | String | dds- bpxxxxxxxx.mongodb.rds.exampl e.com | The name of the SSL certificate. |
|---|---|---|---|

```
http(s)://mongodb.example.com/? Action=DescribeDBInstanceSSL
```

| XML | format |
|---|---|
| <DescribeDBInstanceSSLResponse> <SSLExpiredTime>2020-03-11T02:28:25Z</SSLExpiredTime> <RequestId>36BB1BC2-789C-4BBA-A519-C5B388E4B0D4</RequestId> <SSLStatus>Open</SSLStatus> <CertCommonName>dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com</CertCommonName> </DescribeDBInstanceSSLResponse> |   |

| JSON | format |
|---|---|
| { "SSLExpiredTime":"2020-03-11T02:28:25Z", "SSLStatus":"Open", "RequestId":"36BB1BC2-789C-4BBA-A519-C5B388E4B0D4", "CertCommonName":"dds-bpxxxxxxxx.mongodb.rds.example.com" } |   |

### 7.11 Audit logs

#### 7.11.1 DescribeAuditRecords

You can call this operation to view the audit logs of ApsaraDB for MongoDB instances. When you call this operation, ensure that the audit log feature of the instance is enabled. Otherwise, the operation returns an empty audit log.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditRecords | The operation that you want to perform. Set the value to DescribeAuditRecords. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| EndTime | String | Yes | 2019-03-13T13:11:14Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| StartTime | String | Yes | 2019-03-13T12:11:14Z | The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the sharded cluster instance. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
| Database | String | No | testdatabase | The name of the database. If you do not specify this parameter, this operation returns audit logs of all databases. |
| User | String | No | root | The account of the database. If you do not specify this parameter, this operation returns audit logs of all accounts. |

| Form | String | No | Stream | The form of the audit log entry returend. Valid values: File: returns a log file. If this parameter is set to File, only common parameters are returned. In this case, you must call the DescribeAuditFiles operation to view the download URL of the log file. Stream: returns data streams. Default value: Stream. |
|---|---|---|---|---|
| QueryKeywords | String | No | slow | The keywords used for a query. Separate multiple keywords with spaces. You can specify a maximum of 10 keywords. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| OrderType | String | No | asc | The order of time in which the log entries to return are sorted. Valid values: asc: The log entries are sorted by time in ascending order. desc: The log entries are sorted by time in descending order. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of SQLRecord |   | An array that consists of the information of the audit log entries. |
| SQLRecord |   |   |   |
| AccountName | String | root | The account of the database. |
| DBName | String | test123 | The name of the database. |
| ExecuteTime | String | 2019-03-11T03:30:27Z | The time when the statement was executed. The time is in they yyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| HostAddress | String | 11.xxx.xxx.xxx | The IP address of the client. |
| ReturnRowCounts | Long | 2 | The number of entries returned. |
| Syntax | String | { \"atype\" : \"createCollection\", \"param\" : { \"ns\" : \"123.test1\" }, \"result\": \"OK\" } | The statement that was executed. |
| TableName | String | C1 | The name of the collection. |
| ThreadID | String | 140682188297984 | The ID of the thread. |
| TotalExecutionTimes | Long | 700 | The duration of the statement execution. Unit: microseconds. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCount | Integer | 30 | The maximum number of records on the current page. |
| RequestId | String | 3278BEB8-503B-4E46-8F7E- D26E040C9769 | The ID of the request. |
| TotalRecordCount | Integer | 40 | The total number of entries. |

```
http(s)://mongodb.example.com/? Action=DescribeAuditRecords &StartTime=2019-03-13T12:11:14Z &EndTime=2019-03-13T13:11:14Z
```

```xml
<TotalRecordCount>40</TotalRecordCount> <PageRecordCount>30</PageRecordCount> <RequestId>3278BEB8-503B-4E46-8F7E-D26E040C9769</RequestId> <PageNumber>1</PageNumber> <Items>
    <TableName>C1</TableName>
    <ThreadID>140682188297984</ThreadID>
    <ExecuteTime>2019-03-11T03:30:27Z</ExecuteTime>
    <ReturnRowCounts>2</ReturnRowCounts>
    <DBName>test123</DBName>
    <TotalExecutionTimes>700</TotalExecutionTimes>
    <Syntax>{ \"atype\" : \"createCollection\", \"param\" : { \"ns\" : \"123.test1\" }, \"result\": \"OK\" }</Syntax>
    <HostAddress>11.xxx.xxx.xxx</HostAddress>
    <AccountName>root</AccountName>
</Items>
```

| JSON | format |
|---|---|
| { "TotalRecordCount":"40", "PageRecordCount":"30", "RequestId":"3278BEB8-503B-4E46-8F7E-D26E040C9769", "PageNumber":"1", "Items":[ { "TableName":"C1", "ThreadID":"140682188297984", "ExecuteTime":"2019-03-11T03:30:27Z", "ReturnRowCounts":"2", "DBName":"test123", "TotalExecutionTimes":"700", "Syntax":"{ \\\"atype\\\" : \\\"createCollection\\\", \\\"param\\\" : { \\\"ns\\\" : \\\"123.test1\\\" }, \\\"result\\\": \\\"OK\\\" }", "HostAddress":"11.xxx.xxx.xxx", "AccountName":"root" } ] } |   |

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidEndTime.Format | Specified end time is not valid. | The error message returned when the end time is invalid. Check the format of the specified time. |

#### 7.11.2 DescribeAuditFiles

You can call this operation to view the audit log files of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditFiles | The operation that you want to perform. Set the value to DescribeAuditFiles. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the specified cluster instance. Note If you do not specify this parameter, the audit logs of all mongos and shard nodes will be returned. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |
| Items | Array of LogFile |   | An array that consists of the information of audit log files. |

| LogFile |   |   |   |
|---|---|---|---|
| FileID | Integer | 406505 | The ID of the file. |
| LogDownloadURL | String | http://xxxxxxxx.oss-cn- hangzhou.aliyuncs.com/custinsxx xxxx/custinsxxxxxxxxxxxx.csv _ | The download URL for audit log files. Note If the download URL is unavailable, this parameter is empty. |
| LogEndTime | String | 2019-03-12T09:23:15Z | The end of the time range for the audit log files displayed. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| LogSize | Long | 98 | The size of the audit log file. Unit: bytes. |
| LogStartTime | String | 2019-03-11T08:19:29Z | The beginning of the time range for the audit log files displayed. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| LogStatus | String | Success | The status of the audit log file. Success: The audit log file is archived. Failed: The audit log file failed to be archived. Generating: The audit log file is being archived. Initializing: Archiving is not started. |
| PageNumber | Integer | 1 | The page number of the page returned. |
| PageRecordCount | Integer | 1 | The number of entries on the current page. |
| RequestId | String | F8CA8312-530A-413A-9129- F2BB32A8D404 | The ID of the request. |
| TotalRecordCount | Integer | 1 | The total number of entries. |

```
http(s)://mongodb.example.com/? Action=DescribeAuditFiles
```

| XML | format |
|---|---|
| <DescribeAuditFilesResponse> <Items> <LogFile> <LogStartTime>2019-03-11T08:19:29Z</LogStartTime> <LogEndTime>2019-03-12T09:23:15Z</LogEndTime> <LogStatus>Success</LogStatus> <FileID>406505</FileID> <LogDownloadURL>http://xxxxxxxx.oss-cn-hangzhou.aliyuncs.com/custinsxxxxxx/custinsxxxxxx_xxxxxx.csv</LogDownloadURL> <LogSize>98</LogSize> </LogFile> </Items> <PageNumber>1</PageNumber> <TotalRecordCount>1</TotalRecordCount> <RequestId>F8CA8312-530A-413A-9129-F2BB32A8D404</RequestId> <PageRecordCount>1</PageRecordCount> </DescribeAuditFilesResponse> |   |

```json
 "Items": {
  "LogFile": [
    "LogStartTime": "2019-03-11T08:19:29Z",
    "LogEndTime": "2019-03-12T09:23:15Z",
    "LogStatus": "Success",
    "FileID": 406505,
    "LogDownloadURL": "http://xxxxxxxx.oss-cn-hangzhou.aliyuncs.com/custinsxxxxxx/custinsxxxxxx_xxxxxx.csv",
    "LogSize": 98
```

`]` `},`

```json
 "PageNumber": 1,
 "TotalRecordCount": 1,
 "RequestId": "F8CA8312-530A-413A-9129-F2BB32A8D404",
 "PageRecordCount": 1
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidDBInstanceClass.NotFound | Specified DB instance class is not found. | The error message returned because the specified instance type does not exist. Verify the specified instance type. |
| 403 | IncorrectDBInstanceType | Current DB instance type does not support this operation. | The error message returned because the operation is not supported by the current instance type. |

#### 7.11.3 DescribeAuditPolicy

You can call this operation to view whether the log audit feature is enabled for an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditPolicy | The operation that you want to perform. Set the value to DescribeAuditPolicy. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogAuditStatus | String | Enable | The status of the log audit feature. Valid values: Enable Disabled Default value: Disabled. |
| RequestId | String | 111E7B16-0A87-4CBA-B271- F34AD61E099F | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=DescribeAuditPolicy
```

| XML | format |
|---|---|
| <DescribeAuditPolicyResponse> <LogAuditStatus>Enable</LogAuditStatus> <RequestId>111E7B16-0A87-4CBA-B271-F34AD61E099F</RequestId> </DescribeAuditPolicyResponse> |   |

| JSON | format |
|---|---|
| { "LogAuditStatus": "Enable", "RequestId": "111E7B16-0A87-4CBA-B271-F34AD61E099F" } |   |

#### 7.11.4 ModifyAuditLogFilter

You can call this operation to modify the type of audit logs to be collected from ApsaraDB for MongoDB instances. The instance must be in the running state when you call this operation. This operation is applicable only to replica set instances, but not to sharded cluster instances.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAuditLogFilter | The operation that you want to perform. Set the value to ModifyAuditLogFilter. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| Filter | String | Yes | insert,query,update,delete | The type of the audit log entries to be collected. Valid values: admin: O&M and management operations slow: slow queries query: query operations insert: insert operations update: update operations delete: delete operations command: protocol commands such as the aggregate method |
| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E209BE2B-F264-4B9D-81F6- A5A5FB1FBF28 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ModifyAuditLogFilter &Filter=insert,query,update,delete
```

| XML | format |
|---|---|
| <ModifyAuditLogFilterResponse> <RequestId>E209BE2B-F264-4B9D-81F6-A5A5FB1FBF28</RequestId> </ModifyAuditLogFilterResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "E209BE2B-F264-4B9D-81F6-A5A5FB1FBF28" } |   |

#### 7.11.5 DescribeAuditLogFilter

You can call this operation to view the types of audit logs collected from ApsaraDB for MongoDB instances. The instance must be in the running state when you call this operation.

> **Note:** This operation is applicable only to replica set instances, but not to sharded cluster instances.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditLogFilter | The operation that you want to perform. Set the value to DescribeAuditLogFilter. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Filter | String | admin,slow,insert,query,update,d elete,command | The type of the audit log entries. Valid values: admin: O&M and management operations slow: slow queries query: query operations insert: insert operations update: update operations delete: delete operations command: protocol commands such as the aggregate method |
| RequestId | String | D7C8BA0C-9350-487D-9B70- D69AF27FB1EB | The ID of the request. |
| RoleType | String | primary | The role of the node. |

```
http(s)://mongodb.aliyuncs.com/? Action=DescribeAuditLogFilter
```

| XML | format |
|---|---|
| <DescribeAuditLogFilterResponse> <Filter>admin,slow,insert,query,update,delete,command</Filter> <RoleType></RoleType> <RequestId>D7C8BA0C-9350-487D-9B70-D69AF27FB1EB</RequestId> </DescribeAuditLogFilterResponse> |   |

| JSON | format |
|---|---|
| { "Filter": "admin,slow,insert,query,update,delete,command", "RoleType": "", "RequestId": "D7C8BA0C-9350-487D-9B70-D69AF27FB1EB" } |   |

#### 7.11.6 ModifyAuditPolicy

You can call this operation to enable or disable the audit log feature or set the retention period of audit logs for an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAuditPolicy | The operation that you want to perform. Set the value to ModifyAuditPolicy. |
| AuditStatus | String | Yes | enable | The status of the audit log feature. Valid values: enable disabled |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| StoragePeriod | Integer | No | 30 | The retention period of audit logs. Unit: day. Valid values:1 to 30. Default value: 30. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DC04D812-F18D-4568-9B88- F260D9590116 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ModifyAuditPolicy &AuditStatus=enable
```

| XML | format |
|---|---|
| <ModifyAuditPolicyResponse> <RequestId>DC04D812-F18D-4568-9B88-F260D9590116</RequestId> </ModifyAuditPolicyResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "DC04D812-F18D-4568-9B88-F260D9590116" } |   |

### 7.12 Log management

#### 7.12.1 DescribeSlowLogRecords

Queries the slow query logs of an ApsaraDB for MongoDB instance within a specific period of time.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSlowLogRecords | The operation that you want to perform. Set the value to DescribeSlowLogRecords. |
| StartTime | String | Yes | 2022-09-05T12:10Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm.ssZ format. The time must be in UTC. Note This parameter specifies the time when the slow query is executed, rather than the time when the slow query is logged. |
| EndTime | String | Yes | 2022-09-06T12:10Z | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm.ssZ format. The time must be in UTC. Note The end time must be later than the start time. The end time must be within 24 hours from the start time. Otherwise, the query fails. |
| DBInstanceId | String | Yes | dds-bp1366caac83**** | The instance ID. Note You can call the DescribeDBInstanceAttribute operation to query the instance ID. If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bp18b06ebc21**** | The ID of the shard node. Note You can call the DescribeDBInstanceAttribute operation to query the ID of the shard node. This parameter is available only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
| DBName | String | No | admin | The name of the database. Note If you do not specify this parameter, the slow query logs of all databases are queried. |
| PageSize | Integer | No | 30 | The number of entries per page. Valid values:3 0 to 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The page number. Pages start from page 1. Default value: 1. |
| OrderType | String | No | asc | The order of time in which the log entries to return are sorted. Valid values: asc: The log entries are sorted by time in ascending order. desc (default): The log entries are sorted by time in descending order. |
| ResourceGroupId | String | No | rg-acfmyiu4ekp**** | The ID of the resource group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MongoDB | The database engine. |

| Items | Array of LogRecords |   | The details of the slow query logs. |
|---|---|---|---|
| LogRecords |   |   |   |
| AccountName | String | root | The account of the database. |
| DBName | String | admin | The name of the database. |
| DocsExamined | Long | 1000000 | The number of documents scanned during the execution of the slow query. |
| ExecutionStartTime | String | 2022-09-06T01:41:28Z | The beginning of the queried time range. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| HostAddress | String | 192.168.XX.XX | The IP address of the client that connects to the database. |
| KeysExamined | Long | 0 | The data entries that are scanned during indexing. |
| QueryTimes | String | 600 | The execution duration of the query. Unit: milliseconds. |
| ReturnRowCounts | Long | 0 | The number of rows returned as the result of the slow query. |
| SQLText | String | {\"op\":\"query\",\"ns\":\"mongod btest.customer\",\"query\": {\"find\":\"customer\",\"filter\": {\"name\":\"jack\"}}} | The SQL statement that is executed as part of the slow query. |
| TableName | String | C1 | The name of the collection. |
| PageNumber | Integer | 1 | The page number. |
| PageRecordCount | Integer | 1 | The number of slow query logs on the page. |
| RequestId | String | 414A4E5-4C36-4461-95FC- 23757A20B5F8 | The request ID. |
| TotalRecordCount | Integer | 1 | The total number of entries. |

```
http(s)://mongodb.example.com/?Action=DescribeSlowLogRecords &StartTime=2022-09-05T12:10Z &EndTime=2022-09-06T12:10Z &DBInstanceId=dds-bp1366caac83**** &NodeId=d-bp18b06ebc21**** &DBName=admin
```

| XML | format |
|---|---|
| <TotalRecordCount>1</TotalRecordCount> <PageRecordCount>1</PageRecordCount> <RequestId>414A4E5-4C36-4461-95FC-23757A20B5F8</RequestId> <PageNumber>1</PageNumber> <Items> <LogRecords> <TableName>C1</TableName> <QueryTimes>600</QueryTimes> <ExecutionStartTime>2022-09-06T01:41:28Z</ExecutionStartTime> <ReturnRowCounts>0</ReturnRowCounts> <KeysExamined>0</KeysExamined> <DBName>mongodbtest</DBName> <DocsExamined>1000000</DocsExamined> <HostAddress>192.168.XX.XX</HostAddress> <AccountName>root</AccountName> <SQLText>{\"op\":\"query\",\"ns\":\"mongodbtest.customer\",\"query\":{\"find\":\"customer\",\"filter\":{\"name\":\"jack\"}}}</SQLText> </LogRecords> </Items> <Engine>MongoDB</Engine> |   |

```json
    "TotalRecordCount": "1",
    "PageRecordCount": "1",
    "RequestId": "414A4E5-4C36-4461-95FC-23757A20B5F8",
    "PageNumber": "1",
    "Items": {
        "LogRecords": [{
            "TableName": "C1",
            "QueryTimes": "600",
            "ExecutionStartTime": "2022-09-06T01:41:28Z",
            "ReturnRowCounts": "0",
            "KeysExamined": "0",
            "DBName": "mongodbtest",
            "DocsExamined": "1000000",
            "HostAddress": "192.168.XX.XX",
            "AccountName": "root",
            "SQLText": "{\\\"op\\\":\\\"query\\\",\\\"ns\\\":\\\"mongodbtest.customer\\\",\\\"query\\\":
{\\\"find\\\":\\\"customer\\\",\\\"filter\\\":{\\\"name\\\":\\\"jack\\\"}}}"
```

`}]` `},`

```json
    "Engine": "MongoDB"
```

#### 7.12.2 DescribeErrorLogRecords

You can call this operation to view the error logs of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeErrorLogRecords | The operation that you want to perform. Set the value to DescribeErrorLogRecords. |
| StartTime | String | Yes | 2019-01-01T12:10Z | The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-01-02T12:10Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you specify this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the sharded cluster instance. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary Note If you set NodeId to the ID of a mongos node, the value of this parameter must be primary. |
| DBName | String | No | mongodbtest | The name of the database. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 to 100 |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MongoDB | The database engine. |

| Items | Array of LogRecords |   | An array that consists of the information of log entries. |
|---|---|---|---|
| LogRecords |   |   |   |
| Category | String | NETWORK | The category of the log entry. |
| ConnInfo | String | conn18xxxxxx | The log connection information. |
| Content | String | xxxxxxxx | The content of the log entry. |
| CreateTime | String | 2019-02-26T12:09:34Z | The time when the log entry was generated. The time is in they yyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Id | Integer | 1111111111 | The ID of the log entry. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCount | Integer | 1 | The number of entries returned on each page. |
| RequestId | String | 68BCBEC2-1E66-471F-A1A8- E3C60C0A80B0 | The ID of the request. |
| TotalRecordCount | Integer | 1 | The total number of entries. |

```
http(s)://mongodb.example.com/? Action=DescribeErrorLogRecords &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z
```

| XML | format |
|---|---|
| <DescribeErrorLogRecordsResponse> <Items> <LogRecords> <Category>NETWORK</Category> <CreateTime>2019-02-26T12:09:34Z</CreateTime> <ConnInfo>conn18xxxxxx</ConnInfo> <Content>xxxxxxxx</Content> </LogRecords> </Items> <PageNumber>1</PageNumber> <TotalRecordCount>2</TotalRecordCount> <RequestId>68BCBEC2-1E66-471F-A1A8-E3C60C0A80B0</RequestId> </DescribeErrorLogRecordsResponse> |   |

| JSON | format |
|---|---|
| { "TotalRecordCount":"1", "PageRecordCount":"1", "RequestId":"68BCBEC2-1E66-471F-A1A8-E3C60C0A80B0", "PageNumber":"1", "Items":{ "LogRecords":[ { "ConnInfo":"conn18xxxxxx", "Category":"NETWORK", "Id":"1111111111", "Content":"xxxxxxxx", "CreateTime":"2019-02-26T12:09:34Z" } ] },"Engine":"MongoDB" } |   |

#### 7.12.3 DescribeRunningLogRecords

You can call this operation to view the operational logs of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRunningLogRecords | The operation that you want to perform. Set the value to DescribeRunningLogRecords. |
| StartTime | String | Yes | 2019-01-01T12:10Z | The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-01-02T12:10Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the sharded cluster instance. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
| DBName | String | No | mongodbtest | The name of the database. |
| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary Note If you set NodeId to the ID of a mongos node, the value of RoleType must be primary. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 to 100 |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| OrderType | String | No | asc | The order of time in which the log entries to return are sorted. Valid values: asc: The log entries are sorted by time in ascending order. desc: The log entries are sorted by time in descending order. |
| ResourceGroupId | String | No | rg-axxxxxxx | The ID of the resource group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MongoDB | The database engine. |
| Items | Array of LogRecords |   | An array that consists of the information of log entries. |
| LogRecords |   |   |   |
| Category | String | NETWORK | The category of the log entry. |
| ConnInfo | String | conn18xxxxxx | The log connection information. |
| Content | String | end connection 11.xxx.xxx.xx:3xxxx (0 connections now open)\n | The content of the log entry. |
| CreateTime | String | 2019-02-26T12:09:34Z | The time when the log entry was generated. The time is in they yyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Id | Integer | 1111111111 | The ID of the log entry. |
| PageNumber | Integer | 1 | The page number of the page returned. |

| PageRecordCount | Integer | 30 | The number of entries returned on each page. |
|---|---|---|---|
| RequestId | String | 45D2B592-DEBA-4347-BBF3- 47FF6C97DBBC | The ID of the request. |
| TotalRecordCount | Integer | 2 | The total number of entries. |

```
http(s)://mongodb.example.com/? Action=DescribeRunningLogRecords &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z
```

| XML | format |
|---|---|
| <DescribeRunningLogRecordsResponse> <Items> <LogRecords> <Category>-</Category> <CreateTime>2019-02-26T12:09:34Z</CreateTime> <ConnInfo>conn18xxxxxx</ConnInfo> <Content> end connection 11.xxx.xxx.xx:3xxxx (0 connections now open) </Content> </LogRecords> <LogRecords> <Category>NETWORK</Category> <CreateTime>2019-02-26T12:09:34Z</CreateTime> <ConnInfo>thread1</ConnInfo> <Content>connection accepted from 11.xxx.xxx.xx:3xxxx #1862051 (11 connections now open)</Content> </LogRecords> </Items> <PageNumber>1</PageNumber> <TotalRecordCount>2</TotalRecordCount> <RequestId>45D2B592-DEBA-4347-BBF3-47FF6C97DBBC</RequestId> </DescribeRunningLogRecordsResponse> |   |

| JSON | format |
|---|---|
| { "Items": { "LogRecords": [ { "Category": "-", "CreateTime": "2019-02-26T12:09:34Z", "ConnInfo": "conn18xxxxxx", "Content": "end connection 11.xxx.xxx.xx:3xxxx (0 connections now open)\n" }, { "Category": "NETWORK", "CreateTime": "2019-02-26T12:09:34Z", "ConnInfo": "thread1", "Content": "connection accepted from 11.xxx.xxx.xx:3xxxx #1862051 (11 connections now open)" } ] }, "PageNumber": 1, "TotalRecordCount": 2, "RequestId": "45D2B592-DEBA-4347-BBF3-47FF6C97DBBC" } |   |

### 7.13 Performance monitoring management

#### 7.13.1 DescribeDBInstancePerformance

You can call this operation to view the performance data of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInstancePerforma nce | The operation that you want to perform. Set the value to DescribeDBInstancePerformance. |

| Key | String | Yes | MongoDBDetailedSpaceUsa _ ge | The performance metric. Valid values: CpuUsage: the CPU utilization percentage MemoryUsage: the memory usage percentage MongoDBIOPS: the IOPS usage _ IOPSUsage: the IOPS usage percentage. MongoDBDetailedSpaceUsage: the disk usage. _ DiskUsage : the disk usage percentage MongoDBOpcounters : the operation QPS _ MongoDBConnections : the number of connections _ MongoDBCursors : the number of cursors _ MongoDBNetwork : the network traffic _ MongoDBGlobalLockCurrentQueue : the global lock _ _ _ _ waiting queues MongoDBWtCache : the WiredTiger storage _ _ Note Separate multiple metrics with commas (,). |
|---|---|---|---|---|
| StartTime | String | Yes | 2019-03-11T12:30Z | The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-03-11T12:30Z | The end of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in a sharded cluster instance. You can specify this parameter to view the performance of a single node. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
| ReplicaSetRole | String | No | Primary | The role of the node. Valid values: Primary Secondary Note If you set the DBInstanceId parameter to the ID of a standalone instance, the value of this parameter can only be Primary. |
| RoleId | String | No | 60xxxxx | The role ID of a node in a instance. You can call the DescribeReplicaSetRole operation to view role IDs. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 267F98DC-367D-4F20-B137- 8B5B664D1C5D | The ID of the request. |
| StartTime | String | 2019-03-11T12:20Z | The beginning of the time range to query. The time is in the yyyy-MM- ddTHH:mmZ format. The time is displayed in UTC. |
| EndTime | String | 2019-03-11T12:30Z | The beginning of the time range to query. The time is in the yyyy-MM- ddTHH:mmZ format. The time is displayed in UTC. |
| PerformanceKeys | Array of PerformanceKey |   | An array that consists of the information of performance metrics. |
| PerformanceKey |   |   |   |
| Key | String | MongoDBDetailedSpaceUsage _ | Performance metric. |
| PerformanceValues | Array of PerformanceValue |   | An array that consists of the values of performance metrics. |
| PerformanceValue |   |   |   |

| Date | String | 2019-03-11T12:21:51Z | The date and time when the value is generated. |
|---|---|---|---|
| Value | String | 0.6 | The value of a performance metric. |
| Unit | String | MB | The unit of the performance metric. |
| ValueFormat | String | cpuusage _ | The format of the performance metric value. If the performance metric contains multiple fields, the fields are separated with ampersands (&). For example, if you query disk usage, the returned ValueFormat is inssize&amp;datasize&amp;logsize. _ _ _ |
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the request. |
| Engine | String | MongoDB | The database engine. It is fixed to MongoDB. |

```
http(s)://mongodb.example.com/? Action=DescribeDBInstancePerformance &Key=MongoDB_DetailedSpaceUsage &StartTime=2019-03-11T12:30Z &EndTime=2019-03-11T12:30Z
```

| XML | format |
|---|---|
| <PerformanceKeys> <ValueFormat>cpu_usage</ValueFormat> <Unit>MB</Unit> <Key>MongoDB_DetailedSpaceUsage</Key> </PerformanceKeys> <PerformanceKeys> <PerformanceValues> <Value>0.6</Value> <Date>2019-03-11T12:21:51Z</Date> </PerformanceValues> </PerformanceKeys> <EndTime>2019-03-11T12:30Z</EndTime> <RequestId>267F98DC-367D-4F20-B137-8B5B664D1C5D</RequestId> <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId> <StartTime>2019-03-11T12:20Z</StartTime> <Engine>MongoDB</Engine> |   |

| JSON | format |
|---|---|
| { "PerformanceKeys":[ { "ValueFormat":"cpu_usage", "Unit":"MB", "Key":"MongoDB_DetailedSpaceUsage" }, { "PerformanceValues":[ { "Value":"0.6", "Date":"2019-03-11T12:21:51Z" } ] } ], "EndTime":"2019-03-11T12:30Z", "RequestId":"267F98DC-367D-4F20-B137-8B5B664D1C5D", "DBInstanceId":"dds-bpxxxxxxxx", "StartTime":"2019-03-11T12:20Z", "Engine":"MongoDB" } |   |

#### 7.13.2 DescribeDBInstanceMonitor

You can call this operation to set the collection frequency of monitoring data for an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeDBInstanceMonitor | The operation that you want to perform. Set the value to DescribeDBInstanceMonitor. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Granularity | String | 300 | The collection frequency of monitoring data. The value is fixed to3 00 . Unit: seconds. |
| RequestId | String | EFD65226-08CC-4C4D-B6A4- CB3C382F67B0 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=DescribeDBInstanceMonitor
```

| XML | format |
|---|---|
| <Granularity>300</Granularity> <RequestId>EFD65226-08CC-4C4D-B6A4-CB3C382F67B0</RequestId> |   |

| JSON | format |
|---|---|
| { "Granularity": 300, "RequestId": "EFD65226-08CC-4C4D-B6A4-CB3C382F67B0" } |   |

### 7.14 Parameter management

#### 7.14.1 DescribeParameterModificationHistory

You can call this operation to view the parameter modification records of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeParameterModificati onHistory | The operation that you want to perform. Set the value to DescribeParameterModificationHistroy. |
| StartTime | String | Yes | 2019-01-01T12:10Z | The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-01-02T12:10Z | The end of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| CharacterType | String | Yes | db | The role of the instance. Valid values: db: the shard node cs: the Configserver node mongos: the mongos node logic: the sharded cluster instance |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard in the specified sharded cluster instance. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |

| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeDBInstanceAttribute operation to query the region ID of the instance. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| HistoricalParameters | Array of HistoricalParameter |   | An array that consists of the information of parameter modification records. |
| HistoricalParameter |   |   |   |
| ModifyTime | String | 2019-03-12T07:58:24Z | The time when the parameter was modified. The time is in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| NewParameterValue | String | 200 | The parameter value after modification. |
| OldParameterValue | String | 100 | The parameter value before modification. |
| ParameterName | String | operationProfiling.slowOpThresho ldMs | The name of the modified parameter. |
| RequestId | String | B1BB6E0E-B4EF-4145-81FA- A07719860248 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=DescribeParameterModificationHistory &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z
```

| XML | format |
|---|---|
| <DescribeParameterModificationHistoryResponse> <HistoricalParameters> <HistoricalParameter> <OldParameterValue>100</OldParameterValue> <ModifyTime>2019-03-12T07:58:24Z</ModifyTime> <NewParameterValue>200</NewParameterValue> <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName> </HistoricalParameter> </HistoricalParameters> <RequestId>B1BB6E0E-B4EF-4145-81FA-A07719860248</RequestId> </DescribeParameterModificationHistoryResponse> |   |

| JSON | format |
|---|---|
| { "HistoricalParameters": { "HistoricalParameter": [ { "OldParameterValue": "100", "ModifyTime": "2019-03-12T07:58:24Z", "NewParameterValue": "200", "ParameterName": "operationProfiling.slowOpThresholdMs" } ] }, "RequestId": "B1BB6E0E-B4EF-4145-81FA-A07719860248" } |   |

#### 7.14.2 DescribeParameters

You can call this operation to view parameter configurations of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeParameters | The operation that you want to perform. Set the value toDescribeParameters. |

| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
|---|---|---|---|---|
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard in the specified sharded cluster instance. Note This parameter is only valid when you set theDBInstanceIdparameter to the ID of a sharded cluster instance. |
| CharacterType | String | No | mongos | The type of the database account. Valid values: mongos: The account that can be used to log on to a mongos node shard: The account that can be used to log on to a shard node |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConfigParameters | Array of Parameter |   | An array that consists of the information of configured parameters. |
| Parameter |   |   |   |
| CheckingCode | String | [0-65536] | The valid values of the parameter. |
| ForceRestart | Boolean | true | Indicates whether a restart is required for parameter modifications to take effect. false: A restart is not required. Modifications take effect immediately after they are made. true: A restart is required for modifications to take effect. |
| ModifiableStatus | Boolean | true | Indicates whether the parameter is modifiable. false true |
| ParameterDescription | String | The threshold in milliseconds at which the database profiler considers a query slow, default is 100. | The description of the parameter. |
| ParameterName | String | operationProfiling.slowOpThresho ldMs | The name of the parameter. |
| ParameterValue | String | 200 | The value of the parameter. |
| RequestId | String | 3ADD0C7D-2D2A-4F15-88FF- E7AC9B9FDCC8 | The ID of the request. |
| RunningParameters | Array of Parameter |   | An array that consists of the information of instance parameters that have taken effect. |
| Parameter |   |   |   |
| CheckingCode | String | [33554432-268435456] | The valid values of the parameter. |
| ForceRestart | String | false | Indicates whether a restart is required for parameter modifications to take effect. false: A restart is not required. Modifications take effect immediately after they are made. true: A restart is required for modifications to take effect. |
| ModifiableStatus | String | true | Indicates whether the parameter is modifiable. false true |
| ParameterDescription | String | The maximum memory bytes that sort stage may use, default is 33554432(i.e. 32MB) | The description of the parameter. |
| ParameterName | String | setParameter.internalQueryExec MaxBlockingSortBytes | The name of the parameter. |
| ParameterValue | String | 33554432 | The value of the parameter. |

| EngineVersion | String | 4.0 | The engine version of the instance. |
|---|---|---|---|
| Engine | String | mongodb | The database engine of the instance. Default value: mongodb. |

```
http(s)://mongodb.example.com/? Action=DescribeParameters
```

| XML | format |
|---|---|
| <DescribeParametersResponse> <ConfigParameters> <Parameter> <ParameterDescription>The threshold in milliseconds at which the database profiler considers a query slow, default is 100. </ ParameterDescription> <ParameterValue>200</ParameterValue> <CheckingCode>[0-65536]</CheckingCode> <ForceRestart>false</ForceRestart> <ModifiableStatus>true</ModifiableStatus> <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName> </Parameter> </ConfigParameters> <RequestId>3ADD0C7D-2D2A-4F15-88FF-E7AC9B9FDCC8</RequestId> <RunningParameters> <Parameter> <ParameterDescription></ParameterDescription> <ParameterValue>zlib</ParameterValue> <CheckingCode>snappy\|zlib\|disabled</CheckingCode> <ForceRestart>true</ForceRestart> <ModifiableStatus>true</ModifiableStatus> <ParameterName>net.compression.compressors</ParameterName> </Parameter> <Parameter> <ParameterDescription>The level of database profiling, which inserts information about operation performance into the system.profile collection. 'off' for no profiling, 'slowOp' for only includes slow operations, 'all' for includes all operations, default is ' slowOp'. </ParameterDescription> <ParameterValue>slowOp</ParameterValue> <CheckingCode>off\|slowOp\|all</CheckingCode> <ForceRestart>false</ForceRestart> <ModifiableStatus>true</ModifiableStatus> <ParameterName>operationProfiling.mode</ParameterName> </Parameter> <Parameter> <ParameterDescription>The threshold in milliseconds at which the database profiler considers a query slow, default is 100. </ ParameterDescription> <ParameterValue>220</ParameterValue> <CheckingCode>[0-65536]</CheckingCode> <ForceRestart>false</ForceRestart> <ModifiableStatus>true</ModifiableStatus> <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName> </Parameter> <Parameter> <ParameterDescription>The expiration threshold in milliseconds for idle cursors before MongoDB removes them; i.e. MongoDB rem oves cursors that have been idle for the specified cursorTimeoutMillis. default is 600000(i.e. 10 minutes)</ParameterDescription> <ParameterValue>600000</ParameterValue> <CheckingCode>[1-2147483647]</CheckingCode> <ForceRestart>false</ForceRestart> <ModifiableStatus>true</ModifiableStatus> <ParameterName>setParameter.cursorTimeoutMillis</ParameterName> </Parameter> <Parameter> <ParameterDescription>The maximum memory bytes that sort stage may use, default is 33554432(i.e. 32MB)</ParameterDescription> <ParameterValue>33554432</ParameterValue> <CheckingCode>[33554432-268435456]</CheckingCode> <ForceRestart>false</ForceRestart> <ModifiableStatus>true</ModifiableStatus> <ParameterName>setParameter.internalQueryExecMaxBlockingSortBytes</ParameterName> </Parameter> </RunningParameters> <EngineVersion>4.0</EngineVersion> <Engine>mongodb</Engine> </DescribeParametersResponse> |   |

```json
    "ConfigParameters": {
        "Parameter": [
                "ParameterDescription": "The threshold in milliseconds at which the database profiler considers a query slow, default is 100.",
                "ParameterValue": "200",
                "CheckingCode": "[0-65536]",
                "ForceRestart": false,
                "ModifiableStatus": true,
                "ParameterName": "operationProfiling.slowOpThresholdMs"
```

`]` `},`

```json
    "RequestId": "3ADD0C7D-2D2A-4F15-88FF-E7AC9B9FDCC8",
    "RunningParameters": {
        "Parameter": [
                "ParameterDescription": "",
                "ParameterValue": "zlib",
                "CheckingCode": "snappy|zlib|disabled",
                "ForceRestart": "true",
                "ModifiableStatus": "true",
                "ParameterName": "net.compression.compressors"
```

`},`

```json
                "ParameterDescription": "The level of database profiling, which inserts information about operation performance into the system
.profile collection. 'off' for no profiling, 'slowOp' for only includes slow operations, 'all' for includes all operations, default is 'slowOp '.",
                "ParameterValue": "slowOp",
                "CheckingCode": "off|slowOp|all",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "operationProfiling.mode"
```

`},`

```json
                "ParameterDescription": "The threshold in milliseconds at which the database profiler considers a query slow, default is 100.",
                "ParameterValue": "220",
                "CheckingCode": "[0-65536]",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "operationProfiling.slowOpThresholdMs"
```

`},`

```json
                "ParameterDescription": "The expiration threshold in milliseconds for idle cursors before MongoDB removes them; i.e. MongoDB re
moves cursors that have been idle for the specified cursorTimeoutMillis. default is 600000(i.e. 10 minutes)",
                "ParameterValue": "600000",
                "CheckingCode": "[1-2147483647]",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "setParameter.cursorTimeoutMillis"
```

`},`

```json
                "ParameterDescription": "The maximum memory bytes that sort stage may use, default is 33554432(i.e. 32MB)",
                "ParameterValue": "33554432",
                "CheckingCode": "[33554432-268435456]",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "setParameter.internalQueryExecMaxBlockingSortBytes"
```

`]` `},`

```json
    "EngineVersion": "4.0",
    "Engine": "mongodb"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidDBInstanceClass.NotFound | Specified DB instance class is not found. | The error message returned when the specified instance type does not exists. Verify the specified instance type. |
| 403 | IncorrectDBInstanceType | Current DB instance type does not support this operation. | The error message returned when the current operation is not supported by the instance type of the specified instance. |

#### 7.14.3 ModifyParameters

You can call this operation to modify the parameters of an AsparaDB for MongoDB instance. The instance must be in the running state when you call this operation.

> **Note:** If some of the modified parameters take effect only after the instance is restarted, the instance is automatically restarted after the operation is complete. You can call the **DescribeParameterTemplates** operation to query the parameters that take effect only after the instance is restarted.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyParameters | The operation that you want to perform. Set the value toModifyParameters. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| Parameters | String | Yes | {"operationProfiling.slowOpT hresholdMs":"300"} | The parameters to be modified and their new values. Set this parameter to a JSON string. For example, set the parameter in the {"name":"value","name":"value2"} format. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the specified sharded cluster instance. Note This parameter is only valid when you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
| CharacterType | String | No | db | The role of the instance. Valid values: db: the shard node cs: the Configserver node mongos: the mongos node logic: the sharded cluster instance |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 36923CC2-DDAB-4B48-A144- DA92C1E19537 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ModifyParameters &Parameters={"operationProfiling.slowOpThresholdMs":"300"}
```

| XML | format |
|---|---|
| <ModifyParametersResponse> <RequestId>36923CC2-DDAB-4B48-A144-DA92C1E19537</RequestId> </ModifyParametersResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "36923CC2-DDAB-4B48-A144-DA92C1E19537" } |   |

### 7.15 Backup and recovery

#### 7.15.1 DescribeBackupPolicy

You can call this operation to view the backup policy of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackupPolicy | The operation that you want to perform. Set the value to DescribeBackupPolicy. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupRetentionPeriod | String | 7 | The backup retention period. Unit: days. |
| PreferredBackupPeriod | String | Monday,Wednesday,Friday,Sunda y | The period of backup. Valid values: Monday Tuesday Thursday Friday Saturday Sunday |
| PreferredBackupTime | String | 20:00Z-21:00Z | The time when the data was backed up. The time is in the HH:mmZ-HH:mmZ format. The time is displayed in UTC. |
| PreferredNextBackupTime | String | 2020-05-13T22:56Z | The next backup time. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| RequestId | String | C2C283A1-1CC4-4DD9-B985- 3811E0244A45 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=DescribeBackupPolicy DBInstanceId=dds-bpxxxxxxxx
```

| XML | format |
|---|---|
| <PreferredBackupPeriod>Monday,Wednesday,Friday,Sunday</PreferredBackupPeriod> <RequestId>C2C283A1-1CC4-4DD9-B985-3811E0244A45</RequestId> <PreferredBackupTime>20:00Z-21:00Z</PreferredBackupTime> <PreferredNextBackupTime>2020-05-13T22:56Z</PreferredNextBackupTime> <BackupRetentionPeriod>7</BackupRetentionPeriod> |   |

| JSON | format |
|---|---|
| { "PreferredBackupPeriod":"Monday,Wednesday,Friday,Sunday", "RequestId":"C2C283A1-1CC4-4DD9-B985-3811E0244A45", "PreferredBackupTime":"20:00Z-21:00Z", "PreferredNextBackupTime":"2020-05-13T22:56Z", "BackupRetentionPeriod":"7" } |   |

#### 7.15.2 ModifyBackupPolicy

You can call this operation to modify the backup policy of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBackupPolicy | The operation that you want to perform. Set the value to ModifyBackupPolicy. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| PreferredBackupPeriod | String | Yes | Monday,Wednesday,Friday,S unday | The period of backup. Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday Note Separate multiple values with commas (,). |

| PreferredBackupTime | String | Yes | 03:00Z-04:00Z | The time to back up data. Specify the time in the HH:mmZ-HH:mmZ format. The time must be in UTC. Note The maximum period is 1 hour. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 644A359C-B871-4DD3-97B5- ED91EF5809C2 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=ModifyBackupPolicy &PreferredBackupPeriod=Monday,Wednesday,Friday,Sunday &PreferredBackupTime=03:00Z-04:00Z
```

| XML | format |
|---|---|
| <ModifyBackupPolicyResponse> <RequestId>644A359C-B871-4DD3-97B5-ED91EF5809C2</RequestId> </ModifyBackupPolicyResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "644A359C-B871-4DD3-97B5-ED91EF5809C2" } |   |

#### 7.15.3 CreateBackup

You can call this operation to manually back up an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBackup | The operation that you want to perform. Set the value to CreateBackup. |
| DBInstanceId | String | Yes | d-bpxxxxxxxx | The ID of the instance. |
| BackupMethod | String | No | Logical | The backup method of the instance. Default value: Physical. Valid values: Logical Physical |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupId | String | 5664xxxx | The ID of the backup set. |
| RequestId | String | 7016B12F-7F64-40A4-BAFF- 013F02AC82FC | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=CreateBackup DBInstanceId=dds-bpxxxxxxxx
```

| XML | format |
|---|---|
| <CreateBackupResponse> <RequestId>7016B12F-7F64-40A4-BAFF-013F02AC82FC</RequestId> <BackupId>5664xxxx</BackupId> </CreateBackupResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "7016B12F-7F64-40A4-BAFF-013F02AC82FC", "BackupId": "5664xxxx" } |   |

#### 7.15.4 DescribeBackups

You can call this operation to view the backups of an ApsaraDB for MongoDB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackups | The operation that you want to perform. Set the value to DescribeBackups. |
| StartTime | String | Yes | 2019-03-12T12:00Z | The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-03-13T12:00Z | The end of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard node in the sharded cluster instance. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
| BackupId | String | No | 12345678 | The ID of the backup set. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 30 | The number of entries returned per page. |
| RequestId | String | 8925E66F-1971-4C8C-90A7- F93BF1867E25 | The ID of the request. |
| TotalCount | Integer | 1 | The total number of backup sets. |
| Backups | Array of Backup |   | An array that consists of the information of backup sets. |
| Backup |   |   |   |
| BackupDBNames | String | mongodbtest,new,test | The name of the database that has been backed up. |
| BackupDownloadURL | String | http://xxxxx.oss-cn- hangzhou.aliyuncs.com/xxxxx/hin sxxxxxdataxxxxx.tar.gz _ _ | The Internet download URL of the backup file. If the download URL is unavailable, this parameter is an empty string. |
| BackupEndTime | String | 2019-03-13T04:34:57Z | The end of the backup time range. The time is in they yyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| BackupId | Integer | 11111111 | The ID of the backup set. |

| BackupIntranetDownload URL | String | http://xxxxx.oss-cn-hangzhou- internal.example.com/xxxxx/xxxx x.tar.gz | The internal download URL of the backup file. Note You can download the backup file by using this URL on the Elastic Compute Service (ECS) instance that is connected to the ApsaraDB for MongoDB instance. The ECS instance and ApsaraDB for MongoDB instance must be in the classic network of the same region or in the same virtual private cloud (VPC). |
|---|---|---|---|
| BackupMethod | String | Physical | The backup method. Valid values: Snapshot Physical Logical |
| BackupMode | String | Automated | The backup mode. Valid values: Automated Manual |
| BackupSize | Long | 335520510 | The size of the backup file. Unit: bytes. |
| BackupStartTime | String | 2019-03-13T04:32:42Z | The beginning of the backup time range. The time is in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| BackupStatus | String | Success | The status of the backup. Valid values: Success: The backup task is successful. Failed: The backup task failed. |
| BackupType | String | FullBackup | The backup type. Valid values: FullBackup: full backup. IncrementalBackup: incremental backup. |

```
http(s)://mongodb.example.com/? Action=DescribeBackups &StartTime=2019-03-12T12:00Z &EndTime=2019-03-13T12:00Z
```

| XML | format |
|---|---|
| <TotalCount>1</TotalCount> <PageSize>30</PageSize> <RequestId>8925E66F-1971-4C8C-90A7-F93BF1867E25</RequestId> <PageNumber>1</PageNumber> <Backups> <BackupMethod>Physical</BackupMethod> <BackupDownloadURL>http://xxxxx.oss-cn-hangzhou.aliyuncs.com/xxxxx/hinsxxxxx_data_xxxxx.tar.gz</BackupDownloadURL> <BackupIntranetDownloadURL>http://xxxxx.oss-cn-hangzhou-internal.example.com/xxxxx/xxxxx.tar.gz</BackupIntranetDownloadURL> <BackupSize>335520510</BackupSize> <BackupMode>Automated</BackupMode> <BackupEndTime>2019-03-13T04:34:57Z</BackupEndTime> <BackupStartTime>2019-03-13T04:32:42Z</BackupStartTime> <BackupType>FullBackup</BackupType> <BackupId>11111111</BackupId> <BackupDBNames>mongodbtest,new,test</BackupDBNames> <BackupStatus>Success</BackupStatus> </Backups> |   |

```json
    "TotalCount":"1",
    "PageSize":"30",
    "RequestId":"8925E66F-1971-4C8C-90A7-F93BF1867E25",
    "PageNumber":"1",
    "Backups":[
            "BackupMethod":"Physical",
            "BackupDownloadURL":"http://xxxxx.oss-cn-hangzhou.aliyuncs.com/xxxxx/hinsxxxxx_data_xxxxx.tar.gz",
            "BackupIntranetDownloadURL":"http://xxxxx.oss-cn-hangzhou-internal.example.com/xxxxx/xxxxx.tar.gz",
            "BackupSize":"335520510",
            "BackupMode":"Automated",
            "BackupEndTime":"2019-03-13T04:34:57Z",
            "BackupStartTime":"2019-03-13T04:32:42Z",
            "BackupType":"FullBackup",
            "BackupId":"11111111",
            "BackupDBNames":"mongodbtest,new,test",
            "BackupStatus":"Success"
```

`]`

#### 7.15.5 RestoreDBInstance

Restores data to the current ApsaraDB for MongoDB instance. This operation is applicable only to replica set instances. Standalone instances and sharded cluster instances are not supported. You can clone a standalone instance by creating an instance from a backup set. You can clone a sharded cluster instance by calling the CreateShardingDBInstance operation.

> **Note:** This operation overwrites the data of the current instance, and the data cannot be restored. Proceed with caution.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RestoreDBInstance | The operation that you want to perform. Set the value to RestoreDBInstance. |
| BackupId | Integer | Yes | 11111111 | The ID of the backup set. Note You can call the DescribeBackups operation to query the backup set ID. |
| DBInstanceId | String | Yes | dds-bp11501cd7b5**** | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 973DCB8F-56B3-4102-8777- 3A90495927F7 | The request ID. |

```
http(s)://mongodb.example.com/?Action=RestoreDBInstance &BackupId=11111111 &DBInstanceId=dds-bp11501cd7b5****
```

| XML | format |
|---|---|
| <RestoreDBInstanceResponse> <RequestId>973DCB8F-56B3-4102-8777-3A90495927F7</RequestId> </RestoreDBInstanceResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "973DCB8F-56B3-4102-8777-3A90495927F7" } |   |

#### 7.15.6 DescribeBackupDBs

You can call this operation to view the databases at a specified time or the databases in a specified backup set before you restore a database for an ApsaraDB for MongoDB instance.

> **Note:** You can call the **CreateDBInstance** operation to restore a database for an ApsaraDB for MongoDB instance.

Before you call this operation, make sure that the following requirements are met: A replica set instance is used. The database engine version of the instance must be **3.0**, **3.4**, **4.0**, or **4.2**.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackupDBs | The operation that you want to perform. Set the value to DescribeBackupDBs. |
| SourceDBInstance | String | Yes | dds-bpxxxxxxxx | The ID of the source instance. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| RestoreTime | String | No | 2019-08-22T12:00:00Z | The point in time at which the instance will be restored. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Note It can be any time within the past seven days. The time must be earlier than the current time, but later than the time when the database was created. You must specify either this parameter or the BackupId parameter. |
| BackupId | String | No | 5664xxxx | The ID of the backup set. Note You can call the DescribeBackups operation to view the backup ID. You must specify this parameter or the RestoreTime parameter. |
| ResourceGroupId | String | No | rg-axxxxxxxx | The ID of the resource group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Databases | Array of Database |   | An array that consists of inforamtion of databases. |
| Database |   |   |   |
| DBName | String | mongodbtest | The name of the database. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| TotalCount | Integer | 5 | The number of databases. |
| PageSize | Integer | 30 | The number of entries returned on each page. |
| RequestId | String | 1AF0AD89-ED4F-44AD-B65F- BFC1D5CD9455 | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=DescribeBackupDBs &SourceDBInstance=dds-bpxxxxxxxx &RestoreTime=2019-08-22T12:00:00Z
```

```xml
<TotalCount>5</TotalCount> <Databases>
    <DBName>mongodbtest</DBName>
</Databases> <PageSize>30</PageSize> <RequestId>1AF0AD89-ED4F-44AD-B65F-BFC1D5CD9455</RequestId> <PageNumber>1</PageNumber>
```

| JSON | format |
|---|---|
| { "TotalCount":"5", "Databases":[ { "DBName":"mongodbtest" } ], "PageSize":"30", "RequestId":"1AF0AD89-ED4F-44AD-B65F-BFC1D5CD9455", "PageNumber":"1" } |   |

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectDBInstanceType | Current DB instance type does not support this operation. | The error message returned when the current operation is not supported by the instance type of the specified instance. |

### 7.16 Instance states

This topic descries the instance states of ApsaraDB for MongoDB instances.

| State | Description |
|---|---|
| Creating | The instance is being created. |
| DBInstanceClassChanging | The instance specifications are being changed. |
| DBInstanceNetTypeChanging | The network type of the instance is being changed. |
| Deleting | The instance is being deleted. |
| EngineVersionUpgrading | The database engine version of the instance is being upgraded. |
| GuardSwitching | The instance is undergoing a disaster-triggered failover. |
| HASwitching | The instance is undergoing a primary/secondary switching. |
| Importing | Data is being imported into the instance. |
| ImportingFromOthers | A database is being imported into the instance. |
| LinkSwitching | The instance is undergoing a link switching. |
| MinorVersionUpgrading | The minor version of the instance is being upgraded. |
| NETCREATING _ | A network connection to the instance is being created. |
| NETDELETING _ | A network connection to the instance is being deleted. |
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

### 8.1 Use the ASAPI gateway to call API operations

You can use the Apsara Stack API (ASAPI) gateway to call the API operations of most Apsara Stack services. This topic describes how to call API operations by using the ASAPI gateway and provides links to references.

**Flowchart**

**Procedure**

1. Obtain the ASAPI SDK.
Before you use the ASAPI gateway to call an API operation, you must obtain the ASAPI SDK. For more information, see Obtain the ASAPI SDK.
2. Obtain the endpoint of the ASAPI gateway. For more information, see Obtain the endpoint of ASAPI.
3. Obtain an AccessKey pair.
Obtain the AccessKey pair that is required to call an API operation.

> **Note:** We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services.

4. Obtain a region ID.
Obtain the region ID that is required to call an API operation.
5. Obtain an organization ID and a resource set ID.
You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager M anagement Console Developer Guide. You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Man agement Console Developer Guide.

> **Note:** When you call an API operation, you can specify the organization ID and resource set ID by using the <x-acs-organizationid> and <x-acs- resourcegroupid> parameters to query specified resources.
> If you do not specify the <x-acs-organizationid> parameter, the organization to which the current user belongs is used.
> If you do not specify the <x-acs-resourcegroupid> parameter, this parameter is left empty by default. If you specify a resource set ID, you must also specify an organization ID.

6. Refer to the API reference.
Obtain the developer guide of the Apsara Stack service that you want to use. You can learn what features API operations provide and how to call the API operations.
7. Use the ASAPI SDK to call API operations.
After you complete the preceding steps, you can use the ASAPI SDK to call API operations. For more information about how to use SDKs for different languages, see the relevant topics. The following example shows how to call the DescribeInstances operation of Elastic Compute Service (ECS) by using SDK for Java:

```java
public static void main(String[] args) {
    ASClient client = new ASClient();
    // Specify the caller. The caller is recorded in logs.
    client.setSdkSource("autoTest");
    // Configure request parameters.
    Map<String, Object> parameters = new HashMap<String, Object>();;
    parameters.put("Product", "Ecs");// Specify the POP code. Use the same POP code as the corresponding API directory.
    parameters.put("Action", "DescribeInstances"); // Specify the name of the API operation. Use the same letter case as the corresponding A
PI directory.
    parameters.put("Version", "2014-05-26"); // Specify the API version.
    // Specify the region ID that you obtained.
    parameters.put("RegionId", "xxx");
    // Specify your AccessKey ID and AccessKey secret.
    parameters.put("AccessKeyId", "xxx");
    parameters.put("AccessKeySecret", "xxx");
    // Add the parameters based on the API reference. Take note that the parameters are case-sensitive.
    parameters.put("PageNumber",1);
    parameters.put("PageSize",10);
    Map<String,String> headers=new HashMap<>();
    // Specify the organization ID in the Apsara Uni-manager Management Console.
    headers.put("x-acs-organizationid","3");
    // Specify the resource set ID in the Apsara Uni-manager Management Console.
    //headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>");
    // Specify the endpoint of the ASAPI gateway.
    String endpoint="https://public.asapi.xxx.xxx/asapi/v3";
    // Initiate the request.
    String result = client.doPost(endpoint,headers, parameters);
    // Display the results.
    System.out.println(JSONObject.toJSONString(JSONObject.parseObject(result), SerializerFeature.PrettyFormat));
```

### 8.2 Use the ASAPI gateway to make API calls

#### 8.2.1 Obtain the endpoint of ASAPI

This topic describes three methods that you can use to obtain an endpoint of Apsara Stack API (ASAPI). This topic also describes how to verify the endpoi

**Methods**

**Method 1: Use Registration Vars of Services to obtain an endpoint**

1. Log on to the Apsara Infrastructure Management Console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click **Products**. iii. Choose **Platforms** > **Apsara Infrastructure Management Framework**.
2. In the left-side navigation pane, click **Reports**.
3. On the **All Reports** page, search for `Registration Vars of Services` . In the report list that appears, click the name of the report.
4. On the **Registration Vars of Services** page, click the
icon to the right of **Service** and enter `asapi` in the search box.
5. Find the asapi service, right-click the service in the **Service Registration** column, and then select **Show More** from the shortcut menu.
In the **Details** dialog box, obtain the value of **asapi.public.endpoint**.
6. Generate an endpoint for ASAPI in the following format:

```
https://<asapi.public.endpoint>/asapi/v3
```

**Method 2: Use cluster resources to generate an endpoint**

1. Log on to the Apsara Infrastructure Management Console.
2. Go to the cluster operations page.
i. In the left-side navigation pane, choose **Operations** > **Cluster Operations**. ii. In the **Cluster** search box, enter `ascm` . iii. In the **Actions** column, click **Operations**.
3. Obtain the domain value.
i. Click the **Cluster Resources** tab. ii. In the **Name** field, search for `asapi_dns_public` . iii. In the **Application Parameter** column, click **Details**. In the **Application Parameter** message, obtain the value of the **domain** parameter.
4. Generate an endpoint for ASAPI in the following format:

```
https://<domain>/asapi/v3
```

**Method 3: Concatenate strings to generate an endpoint**

You can concatenate strings to generate an endpoint in the following format:

```
https://public.asapi.<region>.<internet-domain>/asapi/v3
```

| Note 1. Replace <region> with your actual region ID. 2. Replace <internet- domain> with the root domain of your Apsara Stack service. To obtain the root domain, contact Apsara Stack O&M engineers. Make sure that you u domain parameter instead of the intranet-domain parameter. |   |   |   |   |
|---|---|---|---|---|
| Example: if the region value is | cn-****-****-d01 | and the internet-domain value is | inter.****.****.com | , |

the following endpoint is used as a reference:

```
https://public.asapi.cn-****-****-d01.inter.****.****.com/asapi/v3
```

**Verify the endpoint**

Enter the following code. If you cannot access the endpoint, the endpoint is unavailable. You can use the historical endpoint.

| curl https://public.asapi.${global:region}.${global:internet-domain}/api/version -k |   |
|---|---|
| Note ${global:region} and ${global:internet-domain} are variables. You must replace these variables with the actual values that you obtained. |   |

Available endpoint example: Unavailable endpoint example:

**Historical endpoint**

Only the HTTP protocol is supported. The historical endpoint is suffixed with `intranet-domain` and is in the following format:

| http://server.asapi.${global:region}.${global:intranet-domain}/asapi/v3 |   |
|---|---|
| Note ${global:region} and ${global:intranet-domain} are variables. You must replace these variables with the actual values that you obtained. |   |

**Procedure**

To obtain the actual values of the ${global:region}, ${global:internet-domain}, and ${global:intranet-domain} variables, perform the following steps:
1. In the address bar, enter region-id.aso.intranet-domain-id.com URL and press the Enter key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the current page.

2. Enter your username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from the deployment personnel or an administrator.

The first time that you log on to the Apsara Uni-manager Operations Console, change the password of your username as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters, such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password must be 10 to 20 characters in length.
3. Click **Log On** to log on to the **Apsara Uni-manager Operations Console**.
4. In the top navigation bar, choose **Products** > **Platforms** > **Apsara Infrastructure Management Framework** to go to the Apsara Infrastructure Ma
5. In the left-side navigation pane, choose **Operations** > **Cluster Operations**.
6. On the **Cluster Operations** page, enter **ascm-A** in the Cluster field and click the search icon. Click the cluster name in the **Cluster** column.
7. Click the **Cluster Configuration** tab.
8. On the **File Info** tab of **Cluster Configuration**, click **kv.conf**.
9. In the right window of the displayed page, press Ctrl+F to search for the values of the region, internet-domain, and intranet-domain parameters.
Replace ${global:region} with the obtained region value, ${global:internet-domain} with the obtained internetdomain value, and ${global:intranet-domain} with the obtained intranet-domain value.

> **Note:** Do not include ${global:} in the endpoint of ASAPI that you want to use.

#### 8.2.2 Obtain the ASAPI SDK

Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls.

**Public environment**

If you use the public environment, you can go to the Apsara Stack documentation page and download the ASAPI SDK in the **Other Resources** section at the lower part of the page.

**Private environment**

If you use the private environment, you must switch to the public environment and then go to the Apsara Stack documentation page. At the lower part of the page, download the ASAPI SDK in the **Other Resources** section. Table 1. ASAPI SDK for Java

| greopId | artifactId | version |
|---|---|---|
| com.alibaba | alicrypto-java-aliyun | 1.0.4 |
| com.alibaba | fastjson | 1.2.68 |
| org.bouncycastle | bcprov-jdk15to18 | 1.66 |
| org.bouncycastle | bcpkix-jdk15on | 1.65 |
| org.bouncycastle | bcprov-jdk15on | 1.65 |
| com.aliyun | gmsse | 1.1.0 |
| org.apache.commons | commons-lang3 | 3.0 |
| commons-codec | commons-codec | 1.11 |
| commons-logging | commons-logging | 1.2 |
| org.apache.httpcomponents | httpcore | 4.4.11 |
| org.apache.httpcomponents | httpclient | 4.5.7 |

Table 2. ASAPI SDK for Python

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

> **Note:** You can use the version for each package listed in the preceding table or a later version.

### 8.3 STS overview

#### 8.3.1 What is STS?

Apsara Stack Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed for Apsara Stack resource access only by using an STS token. When an STS token is issued, you can specify a validity period and access permissions for the STS token.

**Use an STS token to assume a RAM role**

An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and use the STS token to access Apsara Stack resources.

**Benefits**

STS tokens reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify a validity period for an STS token. The token automatically becomes invalid when it expires. You do not need to rotate STS tokens on a regular basis. You can attach custom policies to STS tokens for flexible and fine-grained authorization.

#### 8.3.2 AssumeRole

Obtains a Security Token Service (STS) token that is used by a RAM user to assume a RAM role. In this example, an Apsara Stack tenant account is used as the trusted entity of the RAM role.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::123456789012****:r ole/adminrole | The Apsara Stack Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Apsara Stack tenant account. |
| RoleSessionName | String | Yes | alice | The name of the role session. Set this parameter based on your business requirements. In most cases, you can set this parameter to the identity of the user who calls the operation. For example, specify a username. In ActionTrail logs, you can distinguish the users who assume the same RAM role to perform operations based on the value of the RoleSessionName parameter. This way, you can perform user- specific auditing. The name must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (). _ |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"} | The policy that specifies the permissions of the STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. The policy must be 1 to 1,024 characters in length. |

**Responses**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71-4EF5-88FA- F32781734A7F | The ID of the request. |
| Credentials | None | None | The access credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuKg5U1**** | The AccessKey ID. |
| AccessKeySecret | String | ***************************************** | The AccessKey secret. |
| SecurityToken | String | ******** | The security token. |
| Expiration | String | 2015-04-09T11:52:19Z | The time when the STS token expires. |
| AssumedRoleUser | None | None | The temporary identity that you use to assume the RAM role. |
| Arn | String | acs:ram::123456789012****:role/ adminrole/alice | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495****:alice | The ID of the temporary identity that you use to assume the RAM role. |

**Add Project Object Model (POM) dependencies**

The Alibaba Cloud core library is required. Perform the following steps to add the Alibaba Cloud core library to POM:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

**Call an API operation to obtain the STS AccessKey 3-tuple.**

In the following sample code, the `Sts::AssumeRole::2015-04-01` operation is used to obtain the 3-tuple.

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        // Replace "sts.aliyuns.com" with the actual endpoint of STS. In most cases, the endpoint is in the following format: sts-
vpc.${global:region}.${global:internet-domain}.
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        // Replace "<yourRoleSessionName>" with the alias that you specify for the current role session.
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
        // Replace "<yourRoleArn>" with the actual ARN that you obtained for the RAM role in the preceding step.
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
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: " + stsToken);
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

**Call examples**

In the following sample code, the `DescribeZones` operation in Elastic Compute Service (ECS) is used.

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
        // Replace "<yourRegionID>" with the actual region ID.
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the AccessKey ID and secret in the 3-tuple that you obtained in
the preceding step.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccessKey>", "<yourStsAccessKeySecret>");
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
        // Replace "<yourStsToken>" with the STS token in the 3-tuple that you obtained in the preceding step.
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
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleArn | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleSessionName | The parameter RoleSessionName is wrongly formed. | The error message returned because the value of the RoleSessionName parameter is in an invalid format. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (). _ |
| 400 | InvalidParameter.DurationSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the DurationSeconds parameter is invalid. The minimum value is 900, and the maximum value is equal to the value of the MaxSessionDuration parameter. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter.PolicyGrammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the policy is invalid. |
| 400 | InvalidParameter.PolicySize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error occurred. |
