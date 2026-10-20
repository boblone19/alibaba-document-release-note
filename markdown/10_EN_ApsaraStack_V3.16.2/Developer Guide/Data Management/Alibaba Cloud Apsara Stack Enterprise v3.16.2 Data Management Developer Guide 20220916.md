---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Data Management Developer Guide 20220916"
product_version: "V3.16.2"
doc_version: "20220916"
pdf_pages: 232
source_pdf: "3e14f604ad4d0e11_Alibaba Cloud Apsara Stack Enterprise v3.16.2 Data Management Developer Guide 20220916.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/20230602/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20Data%20Management%20Developer%20Guide%2020220916.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 Data Management Developer Guide 20220916

## Table of Contents

- 1 Getting started
  - 1.1 Usage notes on development documentation
  - 1.2 Call an API operation
- 2 Preparations
  - 2.1 Log on to the API Tool console
  - 2.2 View the information about an API operation
  - 2.3 Obtain an AccessKey pair
  - 2.4 Obtain an STS AccessKey 3-tuple
  - 2.5 Obtain the endpoint of DMS
  - 2.6 Obtain an SDK installation package of DMS
- 3 Call examples for SDK for Java
  - 3.1 Get started with DMS SDK for Java
  - 3.2 Use SDK
    - 3.2.1 Install DMS SDK for Java
    - 3.2.2 Configure authentication credentials
    - 3.2.3 Configure connection requests
    - 3.2.4 Initiate a request
    - 3.2.5 Handle errors
- 4 Call examples for SDK for Python
  - 4.1 Get started with DMS SDK for Python
  - 4.2 Use SDK
    - 4.2.1 Install DMS SDK for Python
    - 4.2.2 Configure authentication credentials
    - 4.2.3 Set HTTPS requests
    - 4.2.4 Initiate a request
    - 4.2.5 Handle errors
- 5 Call examples for SDK for Go
  - 5.1 Get started with DMS SDK for Go
  - 5.2 Use SDK
    - 5.2.1 Install Go SDK
    - 5.2.2 Configure authentication credentials
    - 5.2.3 Initiate a request
    - 5.2.4 Handle errors
- 6 API Reference
  - 6.1 List of operations by function
  - 6.2 User management
    - 6.2.1 RegisterUser
    - 6.2.2 DisableUser
    - 6.2.3 EnableUser
    - 6.2.4 UpdateUser
    - 6.2.5 DeleteUser
    - 6.2.6 ListUsers
    - 6.2.7 ListUserTenants
    - 6.2.8 GetUserActiveTenant
    - 6.2.9 GetUser
  - 6.3 Instance management
    - 6.3.1 RegisterInstance
    - 6.3.2 ListInstances
    - 6.3.3 GetInstance
    - 6.3.4 UpdateInstance
    - 6.3.5 DeleteInstance
  - 6.4 Operation logs
    - 6.4.1 GetOpLog
  - 6.5 Approval processes
    - 6.5.1 ListWorkFlowTemplates
    - 6.5.2 ListWorkFlowNodes
  - 6.6 Metadata of databases and tables
    - 6.6.1 SearchDatabase
    - 6.6.2 SearchTable
    - 6.6.3 ListDatabases
    - 6.6.4 ListLogicDatabases
    - 6.6.5 ListTables
    - 6.6.6 ListLogicTables
    - 6.6.7 ListColumns
    - 6.6.8 ListIndexes
    - 6.6.9 GetDatabase
    - 6.6.10 GetLogicDatabase
    - 6.6.11 GetMetaTableDetailInfo
    - 6.6.12 GetTableDBTopology
    - 6.6.13 GetMetaTableColumn
    - 6.6.14 SyncDatabaseMeta
    - 6.6.15 SyncInstanceMeta
  - 6.7 Ticket operations
    - 6.7.1 General
      - 6.7.1.1 ApproveOrder
      - 6.7.1.2 CloseOrder
      - 6.7.1.3 GetApprovalDetail
      - 6.7.1.4 GetOrderBaseInfo
      - 6.7.1.5 ListOrders
      - 6.7.1.6 SubmitOrderApproval
      - 6.7.1.7 CreateOrder
    - 6.7.2 Data changes
      - 6.7.2.1 ExecuteDataCorrect
      - 6.7.2.2 GetDataCorrectBackupFiles
      - 6.7.2.3 GetDataCorrectOrderDetail
    - 6.7.3 Schema design
      - 6.7.3.1 CreatePublishGroupTask
    - 6.7.4 Data export
      - 6.7.4.1 ExecuteDataExport
      - 6.7.4.2 GetDataExportDownloadURL
      - 6.7.4.3 GetDataExportOrderDetail
  - 6.8 Permission management
    - 6.8.1 RevokeUserPermission
    - 6.8.2 ListDatabaseUserPermssions
    - 6.8.3 SetOwners
    - 6.8.4 ListUserPermissions
    - 6.8.5 GrantUserPermission
  - 6.9 Security management
    - 6.9.1 ListSensitiveColumns
    - 6.9.2 ListSensitiveColumnsDetail
  - 6.10 Data query
    - 6.10.1 ExecuteScript
- 7 Appendixes
  - 7.1 Process of API calls by using the ASAPI gateway
  - 7.2 Use the ASAPI gateway to make API calls
    - 7.2.1 Obtain an endpoint of ASAPI
    - 7.2.2 Generate an endpoint for ASAPI
    - 7.2.3 Obtain Apsara Stack SDKs
  - 7.3 STS overview
    - 7.3.1 What is STS?
    - 7.3.2 AssumeRole

## 1 Getting started

### 1.1 Usage notes on development documentation

documentation This topic describes how to view the desired product development documentation when you use Apsara Stack API (ASAPI). Prerequisites The Apsara Stack version is obtained from an O&M personnel or operations administrator. Procedure You can go to the Apsara Stack documentation center and view the desired product documentation.
1. Go to the Apsara Stack Documentation Centerpage by using a browser.
2. Click the Ent erprise, Agilit y, or All-in-one tab based on the Apsara Stack version that you use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the name of the product that you want to view.
5. In the upper-right corner of the product documentation section, click View Det ails or Download
PDF.

### 1.2 Call an API operation

Apsara Stack allows you to call API operations by using the Portable OpenAPI Proxy (POP) gateway or the Apsara Stack API (ASAPI) gateway. To ensure that Apsara Stack provides the same experience as the public cloud, API operations in Apsara Stack are called by using the POP gateway by default starting Apsara Stack Enterprise V3.16.0. This topic describes how to call API operations in Apsara Stack by using the POP gateway. Not e You can still use the ASAPI gateway to call API operations. For more information, see Process of API calls by using the ASAPI gateway, Generate an endpoint for ASAPI, and Obtain an ASAPI SDK. Flowchart Procedure
1. Obtain AccessKey credentials.
Obtain the AccessKey credentials that are required when you call an API operation. For more information, see Obtain an AccessKey pair or Obtain an STS AccessKey 3-tuple. Not e We recommend that you use the AccessKey pair of a personal account assigned by Resource Access Management (RAM) or a Security Token Service (STS) AccessKey 3-tuple to call the API operations of the Apsara Uni-manager Management Console and cloud services.
2. Obtain the region ID.
For more information, see Obtain the values of common header parameters.
3. Obtain the organization ID and resource set ID.
You must call an API operation to obtain the resource set ID. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Con sole Developer Guide. Not e When you call an API operation, set the `<x-acs-organizationid>` parameter to the organization ID that you obtained, and set the `<x-acs-resourcegroupid>` parameter to the resource set ID that you obtained. This way, you can query resources in the specified organization and resource set. If you do not set the `<x-acs-organizationid>` parameter, the organization to which the current user belongs is used by default. If you do not set the `<x-acs-resourcegroupid>` parameter, this parameter is left empty by default. If you specify a resource set ID, you must also specify an organization ID.
4. Obtain the API references.
Obtain the developer guide of the cloud service that you want to use. You can learn the features of API operations and how to call the API operations. For more information, see Usage notes on development documentation.
5. Obtain the endpoint of the cloud service.
6. Obtain an SDK of the cloud service and call an API operation.

## 2 Preparations

### 2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

### 2.2 View the information about an API operation

API operation This topic describes how to view the information about API operations. Before you use SDKs, you need to obtain service names, API operation names, and API versions. Context The API operations on the API Directory page are only for reference. For information about how to call API operations, see developer guide of the corresponding cloud service. If the information on the API Directory page is inconsistent with that in the developer guide of the corresponding cloud service, the information in the developer guide prevails. Procedure
1. Log on to the API Tool console.
2. In the left-side navigation pane, click API Direct ory.
3. On the API Direct ory page, select the required service from the drop-down list, enter a keyword
of an operation name in the search box, and then click Search.
4. View and record the service name, API operation name, and API version.

### 2.3 Obtain an AccessKey pair

AccessKey credentials are assigned by RAM or STS. You can use one type of AccessKey credential for authentication when you make an API request. This topic describes how to obtain an AccessKey pair that is assigned by RAM. Context An AccessKey pair is used to verify the identity of the request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. AccessKey credentials can be assigned by RAM or STS: An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An AccessKey 3-tuple that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an STS AccessKey 3-tuple. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions can occur.

> **Warning:** The AccessKey pair of a personal account is managed and controlled by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is authorized by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni- manager Management Console Developer Guide. |

| Parameter | Description |
|---|---|
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. Click the profile picture in the upper-right corner of the page and click User Inf ormat ion.
3. In the AccessKey Pair section, view the AccessKey pair of the personal account.
Not e An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within the current account. You must keep the AccessKey pair confidential. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Organizat ions.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you want
to obtain.
5. Click Management Accesskey on the right side of the page.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### 2.4 Obtain an STS AccessKey 3-tuple

This topic describes how to use STS to call API operations in Apsara Stack. Background information STS allows you to manage temporary credentials to your Apsara Stack resources. You can use STS to call API operations in Apsara Stack. An STS AccessKey 3-tuple consists of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to call API operations, you must specify an STS AccessKey 3-tuple. For more information about STS, see What is STS? Procedure
1. Obtain the `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click User Inf ormat ion. iii. Click View Current Role Policy. In the View Policies of Current Role dialog box, view your `RAM role` .
2. Obtain an STS AccessKey 3-tuple.
Not e In the following sample code, replace the parameters with the actual information. Delete the angle brackets (<>) in the final code. The following section describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <yourRoleSessionName>: Replace the parameter with the name of the current session. <yourRoleArn>: Replace the parameter with the Alibaba Cloud Resource Name (ARN) of your RAM role. <sts.aliyuns.com>: Replace the parameter with the STS endpoint.

```
public static void main(String[] args) {
    // Create and initialize a DefaultAcsClient instance.
    // Specify the region ID, AccessKey ID, and AccessKey secret.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKe
yID>", "<yourAccessKeySecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    String assumeRole = callAssumeRole(client);
    if (StringUtils.isEmpty(assumeRole)) return;
    JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
    JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
    // Obtain an STS AccessKey 3-tuple.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
```

`}`

```java
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace sts.aliyuns.com with the endpoint of STS. The format of an STS endpoint
is sts-vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace <yourRoleSessionName> with the name of the current session.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // Replace <yourRoleArn> with the ARN that you obtain in the previous step for the
RAM role.
    request.putQueryParameter("RoleArn", "<yourRoleArn>");
    try {
        CommonResponse response = client.getCommonResponse(request);
        return response.getData();
    } catch (ServerException e) {
        System.out.println(e.getErrCode());
        System.out.println(e.getErrMsg());
    } catch (ClientException e) {
        System.out.println(e.getErrCode());
        System.out.println(e.getErrMsg());
```

`}`

```
    return null;
```

`}`
3. Use the AccessKey 3-tuple assigned by STS to call an operation of a service. The following sample
code provides an example on how to use the AccessKey 3-tuple assigned by STS to call the `DescribeZones` operation of ECS: Not e In the following sample code, replace the parameters with your actual information. Delete the angle brackets (<>) in the final code. The following section describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourStsAccesskeyID>: Replace the parameter with your AccessKey ID. <yourStsAccessKeySecret>: Replace the parameter with your AccessKey secret. <yourStsToken>. Replace the parameter with your security token. <yourResourceGroupID>: Replace the parameter with the resource set ID. <yourOrganizationID>: Replace the parameter with the organization ID.

```java
public static void main(String[] args) {
    // Replace <yourRegionID> with the region ID.
    // Replace <yourStsAccessKeyID> and <yourStsAccessKeySecret> with the AccessKey ID
and AccessKey secret of the 3-tuple obtained in the previous step.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAcces
skey>", "<yourStsAccessSecret>");
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
    // Replace <yourRegionID> with the region ID.
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
    // Replace <yourStsToken> with the security token of the 3-tuple obtained in the pr
evious step.
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
    // Optional. Replace the parameter with the resource set ID.
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
    // Required. Replace the parameter with the organization ID.
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

`}` `}`

### 2.5 Obtain the endpoint of DMS

This topic describes how to obtain the endpoint of Data Management (DMS). Background information To use the POP gateway to call API operations of a service in Apsara Stack, you must obtain endpoint of the service. You can obtain an endpoint from onsite Apsara Stack O&M engineers. You can also perform the following steps to obtain the endpoint. Procedure
1. Log on to the Apsara Infrastructure Management console.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for `Registration Vars of Services` and click the report name.
4. On the Regist rat ion Vars of Services page, click the
icon next to Service and search for

```
 dts-dtm .
```

5. Find the dts-dtm service, right-click in the Service Regist rat ion column, and then select Show
More from the shortcut menu. In the Det ails dialog box, view the value of dms_open_api_domain. The value indicates the endpoint of DMS.

### 2.6 Obtain an SDK installation package of DMS

package of DMS To call API operations of DMS in Apsara Stack by using the POP gateway, you must use an SDK. This topic provides links for you to download Alibaba Cloud SDKs.

| Language | Download URL | Ref erence |
|---|---|---|
| Alibaba Cloud SDK for Java | DMS SDK for Java Not e We recommend that you download DMS SDK for Java V1.18.0. | Get started with DMS SDK for Java |

| Language | Download URL | Ref erence |
|---|---|---|
| Alibaba Cloud SDK for Python | DMS SDK for Python | Get started with DMS SDK for Python |
| Alibaba Cloud SDK for Go | DMS SDK for Go | Get started with DMS SDK for Go |

Not e We recommend that you use an SDK for Java, Python, or Go. If you use SDKs for other programming languages, the SDKs may be incompatible with your system. SDK for Java

## 3 Call examples for SDK for Java

### 3.1 Get started with DMS SDK for Java

This topic describes how to obtain and use DMS SDK for Java. Prerequisites An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained. You can obtain an AccessKey pair in the Apsara Uni-manager Management Console. For more information, see Obtain an AccessKey pair. The endpoint of DMS is obtained. For more information, see Obtain the endpoint of DMS. Java Development Kit (JDK) 1.8 or later is installed. Install the SDK If you use Apache Maven to manage your Java project, you need to only import the JAR file to the pom.xml file of the project. To use DMS SDK for Java, you must install the SDK core library and the SDK. We recommend that you use the core library version 4.5.17 or later and use the SDK version 1.18.0. Use the SDK To use DMS SDK for Java, perform the following steps:
1. Create and initialize a DefaultAcsClient instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exception.
Not e In the following sample code, replace the parameters with the actual information. Delete the angle brackets (<>) in the final code. The following section describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <DMSProductCode>: Replace the parameter with the service code of DMS in Apsara Stack. <DMSProductEndpoint>: Replace the parameter with the endpoint of DMS in Apsara Stack. SDK for Java

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.dms_enterprise.model.v20181101.GetOpLogRequest; import com.aliyuncs.dms_enterprise.model.v20181101.GetOpLogResponse; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class GetOpLogSampleTest {
    public static void main(String[] args) {
        String regionId = "<yourRegionID>";
        String accessKey = "<yourAccessKeyID>";
        String secretKey = "<yourAccessKeySecret>";
        String product = "<DMSProductCode>";
        String endpoint = "<DMSProductEndpoint>";
        DefaultProfile.addEndpoint(regionId, product, endpoint);
        DefaultProfile profile = DefaultProfile.getProfile(regionId, accessKey, secretK
ey);
        IAcsClient client = new DefaultAcsClient(profile);
        GetOpLogRequest request = new GetOpLogRequest();
        request.setStartTime("2022-01-01 00:00:00");
        request.setEndTime("2022-01-02 00:00:00");
        request.setPageNumber(1);
        request.setPageSize(100);
        try {
            GetOpLogResponse response = client.getAcsResponse(request);
            System.out.println("RequestId: " + response.getRequestId());
            System.out.println("OpLogCount: " + response.getTotalCount());
```

`}`

```java
        catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

`}` `}` `}`

### 3.2 Use SDK

#### 3.2.1 Install DMS SDK for Java

This topic describes how to install and use DMS SDK for Java. Alibaba Cloud SDK for Java supports JDK 1.8 or later. You can install SDKs for Java by adding Maven dependencies or downloading Alibaba Cloud SDKs. SDK for Java To use DMS SDK for Java, you must install the core library of Alibaba Cloud SDK for Java and DMS SDK for Java. We recommend that you use the core library version 4.5.17 or later and use the SDK version 1.18.0. To use DMS SDK for Java, you must also add the following dependency to the pom.xml file. For information about the SDK version, see Obtain an SDK installation package of DMS.

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency> <!-- dms-enterprise java sdk --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-dms-enterprise</artifactId>
    <version>1.18.0</version>
</dependency>
```

#### 3.2.2 Configure authentication credentials

When you use Alibaba Cloud SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. DMS SDK for Java allows you to complete the authentication process by using an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as credentials when you initialize a client instance. Not e Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",          // Replace the parameter with the region ID.
    "<yourAccessKeyID>",      // Replace the parameter with your AccessKey ID.
    "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey secret.
```

Not e In the preceding sample code, replace the parameters with the actual information. Delete the angle brackets (<>) in the final code.

#### 3.2.3 Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements. SDK for Java Not e You must use actual values to replace the variables in the following sample code. Do not retain the angle brackets (<>) in the final code. The following list describes the variables: <readTimeout>: Specify the read timeout period based on your business requirements. Unit: milliseconds. <connectionTimeout>: Specify the connection timeout period based on your business requirements. Unit: milliseconds. <maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER. <maxRequests>: Specify the maximum number of requests based on your business requirements. The supported data type is INTEGER. <http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy.

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

This topic describes how to use DMS SDK for Java to initiate a request. Procedure
1. Create an AcsClient instance.

```
IAcsClient client = new DefaultAcsClient(profile);
```

SDK for Java
2. Create a request.
Name the request in the format of ${apiName}Request , where ${apiName} indicates the API operation name, such as GetOpLog. If multiple service SDKs are used, different requests may have the same name. You can differentiate the requests based on package names.

```
GetOpLogRequest request = new GetOpLogRequest(); request.setStartTime("2022-01-01 00:00:00"); request.setEndTime("2022-01-02 00:00:00"); request.setPageNumber(1); request.setPageSize(100);
```

3. Initiate the request and handle the response.

```
GetOpLogResponse response = client.getAcsResponse(request);
```

In normal cases, all returned fields are deserialized into the response. You can directly call `respons` `e.getXXX()` to obtain the response fields.

```
OpLogCount := response.getTotalCount()
```

If an exception occurs or you need to obtain the original HTTP response, call `doAction()` .

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

### 4.1 Get started with DMS SDK for Python

Python This topic describes how to obtain and use DMS SDK for Python. Prerequisites An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained. For more information, see Obtain an AccessKey pair. The endpoint of DMS is obtained. For more information, see Obtain the endpoint of DMS. Install DMS SDK for Python
1. Install the SDK core library.
If you use Python 2.x, run the following command to install the SDK core library:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the SDK core library:

```
pip3 install aliyun-python-sdk-core-v3
```

2. Install DMS SDK for Python.
If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-dms-enterprise
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-dms-enterprise
```

Use DMS SDK for Python To use DMS SDK for Python, perform the following steps:
1. Create a client instance. When you create a client instance, you must specify a region ID, an
AccessKey ID, and an AccessKey secret.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exception.
SDK for Python Not e In the following sample code, replace the parameters with the actual information. Delete the angle brackets (<>) in the final code. The following section describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <DMSProductCode>: Replace the parameter with the service code of DMS in Apsara Stack. <DMSProductEndpoint>: Replace the parameter with the endpoint of DMS in Apsara Stack.

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential from aliyunsdkdms_enterprise.request.v20181101.GetOpLogRequest import GetOpLogRequest credentials = AccessKeyCredential('<yourAccessKeyID>', '<yourAccessKeySecret>') client = AcsClient(region_id='<yourRegionID>', credential=credentials) request = GetOpLogRequest() request.set_accept_format('json') request.set_endpoint('<DMSProductEndpoint>') response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

### 4.2 Use SDK

#### 4.2.1 Install DMS SDK for Python

This topic describes how to install and use DMS SDK for Python. Alibaba Cloud SDK for Python supports Python 2.6.x, Python 2.7.x, Python 3.x, and later versions. You can install Alibaba Cloud SDK for Python by using pip. Not e To use the SDK for Python of a cloud service, you must install the core library of Alibaba Cloud SDK for Python. For example, if you want to use DMS SDK for Python, you must install the core library of Alibaba Cloud SDK for Python and DMS SDK for Python. If you use Python 2.x, run the following command to install the SDK core library:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the SDK core library:

```
pip3 install aliyun-python-sdk-core-v3
```

SDK for Python The following commands are used to install DMS SDK for Python. If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-dms-enterprise
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-dms-enterprise
```

#### 4.2.2 Configure authentication credentials

When you use Alibaba Cloud SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. DMS SDK for Python allows you to complete the authentication process by using an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as credentials when you initialize a client instance. Not ice Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

#### 4.2.3 Set HTTPS requests

The Python SDK supports using HTTP and HTTPS to initiate API requests. When using the Python SDK, you can specify a protocol (HTTP or HTTPS) for a specific request to use, or set a global default protocol for all requests to use. Not e The default protocol (HTTP or HTTPS) of a product takes precedence over the global default protocol you set. Add OpenSSL dependency HTTPS of the Python SDK depends on the OpenSSL support in Python. To use Alibaba Cloud SDK to send HTTPS requests, you must add OpenSSL support in Python.

| the | python -c "import ssl" | comm |
|---|---|---|
| ImportError: No module named ssl |   |   |

Run the `python -c "import ssl"` command to check if the Python environment supports OpenSSL. If the `ImportError: No module named ssl` error message does not appear, OpenSSL is supported in Python. If Python does not support OpenSSL, run the following command to install OpenSSL:

```
pip install pyopenssl
```

Set HTTP/HTTPS for a request SDK for Python See the following code example for reference to set the HTTPS call for an API:

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

This topic describes how to use DMS SDK for Python to initiate a request. Procedure
1. Import DMS SDK for Python.

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential from aliyunsdkdms_enterprise.request.v20181101.GetOpLogRequest import GetOpLogRequest
```

2. Create an AcsClient instance.

```
credentials = AccessKeyCredential('<yourAccessKeyID>', '<yourAccessKeySecret>') client = AcsClient(region_id='<yourRegionID>', credential=credentials)
```

3. Create a request.

```
request = GetOpLogRequest() request.set_accept_format('json') request.set_endpoint('<DMSProductEndpoint>')
```

4. Initiate the request and process the response.

```python
response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8')) response = clt.do_action_with_exception(request) print response
```

#### 4.2.5 Handle errors

If an error occurs on the server side or SDK side when you use the Python SDK, the Python SDK returns the corresponding exception message. An exception message contains the detailed error information, namely the error code and the error message. SDK for Python Generally, you are not required to handle the errors returned by the Python SDK. You are only required to handle the errors on the server side according to the error message. `ServerException` is the error message on the server side. `ClientException` is the error message on the SDK side. For example, if the following error occurs, modify the ID of AccessKey according to the detailed error message.

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

### 5.1 Get started with DMS SDK for Go

Alibaba Cloud SDK for Go allows you to access services without complex coding. This topic describes how to obtain and use DMS SDK for Go. Prerequisites An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. The endpoint of DMS is obtained. For more information, see Obtain the endpoint of DMS. Install the core package of Alibaba Cloud SDK for Go Alibaba Cloud SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

Use the SDK for Go To use the SDK for Go, perform the following steps:
1. Initialize a client instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exception.
Not e In the following sample code, replace the parameters with the actual information. Delete the angle brackets (<>) in the final code. The following section describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <DMSProductCode>: Replace the parameter with the service code of DMS in Apsara Stack. <DMSProductEndpoint>: Replace the parameter with the endpoint of DMS in Apsara Stack. SDK for Go

```java
package main import (
 "fmt"
   dms_enterprise "github.com/aliyun/alibaba-cloud-sdk-go/services/dms-enterprise"
```

`)`

```
func main() {
 client, err := dms_enterprise.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKey
ID>", "<yourAccessKeySecret>")
 request := dms_enterprise.CreateGetOpLogRequest()
 request.Scheme = "https"
    request.Domain = "<DMSProductEndpoint>"
 response, err := client.GetOpLog(request)
 if err != nil {
  fmt.Print(err.Error())
```

`}`

```
 fmt.Printf("response is %#v\n", response)
```

`}`
4. Optional. Switch to HTTP or HTTPS.

```
request.Scheme = "HTTPS"
```

### 5.2 Use SDK

#### 5.2.1 Install Go SDK

This topic describes how to install the Go SDK. The Alibaba Cloud Go SDK supports Go 1.7 or later versions. Install the Go SDK manually.
1. Download the source code of the Go SDK from the official site of Apsara Stack.
2. Extract the package to the directory where the GO_PATH file of the current user resides.

#### 5.2.2 Configure authentication credentials

When you use Alibaba Cloud SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. DMS SDK for Go allows you to complete the authentication process by using an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as credentials when you initialize a client instance. Not ice Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised. The following code provides an example on how to initialize a DMS client instance: SDK for Go

```
// Initialize a client instance. Client, err := dms-enterprise.NewClientWithAccessKey(
        "<yourRegionID>",                 // Replace the parameter with the region ID.
        "<yourAccessKeyID>",             // Replace the parameter with your AccessKey ID.
        "<yourAccessKeySecret>")        // Replace the parameter with your AccessKey secret
```

`.` Not e In the preceding sample code, replace the parameters with the actual information. Delete the angle brackets (<>) in the final code.

#### 5.2.3 Initiate a request

This topic describes how to use DMS SDK for Go to initiate a request. To use DMS SDK for Go to initiate a request, perform the following steps:
1. Import DMS SDK for Go.

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/dms-enterprise
```

2. Create a client instance that contains all API operations of DMS.
Not e In the following sample code, replace the parameters with the actual information. Delete the angle brackets (<>) in the final code.

```
Client,err := dms_enterprise.NewClientWithAccessKey( // Replace the parameter with the service name.
    "<yourRegionID>",  // Replace the parameter with the region ID.
    "<yourAccessKeyID>",  // Replace the parameter with your AccessKey ID.
    "<yourAccessKeySecret>")  // Replace the parameter with your AccessKey secret.
```

3. Call the `xxx.CreateXXXRequest` method to create a request.
Specify the method name in the ${service}.Create${apiName}Request format. ${service} specifies the service name in lowercase. Example: dms_enterprise. ${apiName} specifies the name of the API operation. Example: GetOpLog.

```
request := dms_enterprise.CreateGetOpLogRequest() request.Scheme = "https" request.Domain = "<DMSProductEndpoint>"
```

4. Initiate the request.

```
response, err := client.GetOpLog(request)
```

#### 5.2.4 Handle errors

SDK for Go When you use Alibaba Cloud SDK for Go, a `ClientError` or a `ServerError` is returned when an error occurs on the server side or on the SDK side. Both error types are included in `sdk.errors` . The errors conform to the standard Go error interface and can be handled in a similar way as standard Go errors. Troubleshooting You can use the following code to troubleshoot an error:

```
response,err := Client.DescribeInstances(request) if err != nil {
    // Obtain the error information.
   err.Error()
```

`}` ClientError After you send a request, if an error occurs on the SDK side and cannot be automatically handled, the SDK returns a `ClientError` . The following code shows how to determine and obtain the error message in a `ClientError` of DMS SDK for Go: Not ice If you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/dms-enterprise"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // The error package that you want to add.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

```
response, err := Client.ListInstances(request) if clientError, ok := err.(*errors.ClientError); ok{
    // Obtain the error code.
    clientError.ErrorCode()
    // Obtain the error message.
    clientError.Message()
    // Obtain the original error. The return value may be nil.
    clientError.OriginError()
```

`}` ServerError The SDK wraps an error returned by the server into a `ServerError` and returns the error to the client. In this case, you can still obtain the original HTTP response from the response. SDK for Go The following code shows how to determine and obtain the error message in a ServerError and Response of DMS SDK for Go: Not ice If you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/dms-enterprise" // Replace dms wit
h the name of the service.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // The error package that you want to add.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

```
response, err := Client.DescribeInstances(request) if serverError, ok := err.(*errors.ServerError); ok{
    // Obtain the error code.
    serverError.ErrorCode()
    // Obtain the error message.
    serverError.Message()
    // Obtain the original HTTP response.
    response.GetOriginHttpResponse()
```

`}`

## 6 API Reference

### 6.1 List of operations by function

The following tables describe the API operations available for use in Data Management (DMS). User management

| API | Description |
|---|---|
| RegisterUser | Adds a user. |
| DisableUser | Disables a user. |
| EnableUser | Enables a user. |
| UpdateUser | Updates the information about a user. |
| DeleteUser | Deletes a user. |
| ListUsers | Queries the details about users. |
| ListUserTenants | Queries tenants. |
| GetUserActiveTenant | Queries the details about a tenant. |
| GetUser | Queries the details about a user. |

Instance management

| API | Description |
|---|---|
| RegisterInstance | Adds a database instance. |
| ListInstances | Queries the details about instances. |
| GetInstance | Queries the details about an instance. |
| UpdateInstance | Updates the information about an instance and checks the connectivity of the instance. |
| DeleteInstance | Deletes instances that are managed by DMS. |

Operation logs

| API | Description |
|---|---|
| GetOpLog | Queries the details about operation logs that are generated in a specified period of time. |

Approval processes

| API | Description |
|---|---|
| ListWorkFlowTemplates | Queries approval templates. |
| ListWorkFlowNodes | Queries approval nodes. |

Metadata of databases and tables

| API | Description |
|---|---|
| SearchDatabase | Queries the details about a database. |
| SearchTable | Queries the details about a table. |
| ListDatabases | Queries the details about databases in an instance. |
| ListLogicDatabases | Queries the details about logical databases. |
| ListTables | Queries the details about tables in a database. |
| ListLogicTables | Queries the details about logical tables in a logical database. |
| ListColumns | Queries the details about columns in a table. |
| ListIndexes | Queries the details about indexes in a table. |
| GetDatabase | Queries the details about a database. |
| GetLogicDatabase | Queries the details about a logic database. |
| GetMetaTableDetailInfo | Queries the details about fields and indexes in a table. |
| GetTableDBTopology | Queries the topology of a table. |
| GetMetaTableColumn | Queries the details about fields in a table. |
| SyncDatabaseMeta | Synchronizes the metadata of a database dictionary. |
| SyncInstanceMeta | Synchronizes the metadata of all database dictionaries in an instance. |

Ticket operations

| Category | API | Description |
|---|---|---|
| General | ApproveOrder | Reviews a ticket. |
|   | CloseOrder | Closes a ticket. |
|   | GetApprovalDetail | Queries the details about an approval process for a ticket. |
|   | GetOrderBaseInfo | Queries the basic information about a ticket. |

| eveloper Guid |   |   |
|---|---|---|
|   | e·API Reference | Data Managemen |
| Category | API | Description |
|   | ListOrders | Queries the details about tickets. |
|   | SubmitOrderApproval | Submits a ticket for approval. |
|   | CreateOrder | Creates a ticket. |
| Data change | ExecuteDataCorrect | Executes a ticket that is used to modify data. |
|   | GetDataCorrectBackupFiles | Queries the download URL of an attachment that includes the backup files of data changes. |
|   | GetDataCorrectOrderDetail | Queries the details about a ticket that is used to modify data. |
| Schema design | CreatePublishGroupTask | Executes a ticket that is used to modify the schema design of a database. |
| Data export | ExecuteDataExport | Executes a ticket that is used to export data. |
|   | GetDataExportDownloadURL | Queries the download URL of an attachment that includes the exported data. |
|   | GetDataExportOrderDetail | Queries the details about a ticket that is used to export data. |

Permission management

| API | Description |
|---|---|
| RevokeUserPermission | Revokes the permissions of a user. |
| ListDatabaseUserPermssions | Queries the details about user permissions on the resources of a database. |
| SetOwners | Sets the owners of a database or table. |
| ListUserPermissions | Queries the permissions of a user on databases and tables. |
| GrantUserPermission | Grants a user the permissions on a database or table. |

Security management

| API | Description |
|---|---|
| ListSensitiveColumns | Queries sensitive columns. |
| ListSensitiveColumnsDetail | Queries the details about sensitive columns. |

Data query

| API | Description |
|---|---|
| ExecuteScript | Executes an SQL script. |

### 6.2 User management

#### 6.2.1 RegisterUser

Adds a user to your enterprise. The administ rat or of Data Management (DMS) Enterprise can call this operation to add users to DMS Enterprise. To check the users that assume the administrator role, perform the following steps: Log on to the DMS Enterprise console and choose System Management > User Management. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RegisterUser | The operation that you want to perform. Set the value to Regist erUser. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Uid | String | Yes | 12345678 | The ID of the Apsara Stack tenant account of the user that you want to add. |
| UserNick | String | No | dmstest | The name of the user. |
| RoleNames | String | No | USER,DBA | The roles that the user assumes. Valid values: USER: a common user DBA: a database administrator (DBA) ADMIN: an administrator SECURIT Y ADMIN: a security _ administrator Not e Default value: USER. You can specify one or more roles for the user. Separate multiple roles with commas (,). |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Mobile | String | No | 130000000xx | The contact number of the user. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | 403 | The returned error code. |
| ErrorMessage | String | The specified user already exists. | The returned error message. |
| RequestId | String | 34E01EDD-6A16- 4CF0-9541- C644D1BE01AA | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RegisterUser &Tid=-1 &Uid=12345678 &UserNick=dmstest &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RegisterUserResponse>
      <RequestId>ADE24A7C-DB8B-4D32-94AD-E50E3B921197</RequestId>
      <Success>true</Success>
</RegisterUserResponse>
```

`JSON` format `{`

```json
    "RequestId": "34E01EDD-6A16-4CF0-9541-C644D1BE01AA",
    "Success": true
```

`}`

#### 6.2.2 DisableUser

Disables an Apsara Stack tenant account. This operation is related to the disable user feature of Data Management (DMS). To use this feature, perform the following steps: Log on to the DMS console, choose System Management > User Management. The administrator of DMS Enterprise can call this operation to disable an Apsara Stack tenant account that is temporarily not used in DMS Enterprise. After an Apsara Stack tenant account is disabled, the permissions that are granted to the Apsara Stack tenant account are revoked. The data owner configurations and database administrator (DBA) configurations are also disabled. Not e This operation only stops an Apsara Stack tenant account from logging on to your DMS Enterprise console. The Apsara Stack tenant account is not disabled After an Apsara Stack tenant account is disabled, you cannot use the account to log on to your DMS Enterprise console until the account is enabled again. However, the disabled account still exists in DMS Enterprise. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DisableUser | The operation that you want to perform. Set the value to DisableUser. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Uid | String | Yes | 12345 | The ID of the Apsara Stack tenant account. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | 403 | The error code that is returned. |
| ErrorMessage | String | The specified user not exists. | The error message that is returned. |
| RequestId | String | 34E01EDD-6A16- 4CF0-9541- C644D1BE01AA | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeds. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DisableUser &Tid=-1 &Uid=12345 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DisableUserResponse>
    <RequestId>ADE24A7C-DB8B-4D32-94AD-E50E3B921197</RequestId>
    <Success>true</Success>
</DisableUserResponse>
```

`JSON` format `{`

```json
    "RequestId":"34E01EDD-6A16-4CF0-9541-C644D1BE01AA",
    "Success":true
```

`}`

#### 6.2.3 EnableUser

Enables a disabled Apsara Stack tenant account. This operation is related to the enable user feature of Data Management (DMS) Enterprise. To use this feature, perform the following steps: Log on to the DMS Enterprise console, choose System Management > User Management. The administrator of DMS Enterprise can call this operation to enable an Apsara Stack tenant account that is disabled in DMS Enterprise. After an Apsara Stack tenant account is enabled, you can use the account to log on to the DMS Enterprise console and perform the required operations. Not e This operation only removes the limit of a disabled Apsara Stack tenant account that cannot be used to log on to the DMS Enterprise console. Other operations that can be performed by the Apsara Stack tenant account are not affected. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EnableUser | The operation that you want to perform. Set the value to EnableUser. |
| Tid | Long | Yes | -1 | The ID of the tenant. |

|   | Data Management |   |   |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Uid | String | Yes | 12345 | The ID of the Apsara Stack tenant account. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | 403 | The returned error code. |
| ErrorMessage | String | The specified user not exists. | The returned error message. |
| RequestId | String | 34E01EDD-6A16- 4CF0-9541- C644D1BE01AA | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=EnableUser &Tid=-1 &Uid=12345 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<EnableUserResponse>
    <RequestId>ADE24A7C-DB8B-4D32-94AD-E50E3B921197</RequestId>
    <Success>true</Success>
</EnableUserResponse>
```

`JSON` format `{`

```json
    "RequestId": "34E01EDD-6A16-4CF0-9541-C644D1BE01AA",
    "Success": true
```

`}`

#### 6.2.4 UpdateUser

Updates the information of a user. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateUser | The operation that you want to perform. Set the value to Updat eUser. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Uid | Long | Yes | 123456789 | The ID of the user. |
| UserNick | String | No | test | The name of the user. |
| RoleNames | String | No | ADMIN,DBA | The roles that the user assumes. For more information about the valid values, see the Regist erUser operation. |
| Mobile | String | No | 188xxxxxxxx | The DingTalk ID or mobile number of the user. |
| MaxExecuteCount | Long | No | 1000 | The maximum number of queries that can be performed each day. |
| MaxResultCount | Long | No | 1000 | The maximum number of rows that can be queried each day. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |

|   | Data Management |   |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E9BEBF41-4F69- 4605-A5D5- A67955173941 | The ID of the request. |
| Success | Boolean | false | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UpdateUser &Tid=-1 &Uid=123456789 &UserNick=test &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>E9BEBF41-4F69-4605-A5D5-A67955173941</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "E9BEBF41-4F69-4605-A5D5-A67955173941",
  "Success": true
```

`}`

#### 6.2.5 DeleteUser

Deletes an Apsara Stack tenant account. This operation is related to the delete user feature of Data Management (DMS). To use this feature, perform the following steps: Log on to the DMS console, choose System Management > User Management. The administrator of DMS Enterprise can call this operation to delete an Apsara Stack tenant account that is no longer used in DMS Enterprise. After an Apsara Stack tenant account is deleted, the permissions that are granted to the Apsara Stack tenant account are revoked. The data owner configurations and database administrator (DBA) configurations are disabled. Not e This operation only removes the relationship between an Apsara Stack tenant account and your DMS Enterprise. The Apsara Stack tenant account is not deleted. After you delete an Apsara Stack tenant account, you cannot use this account to log on to DMS Enterprise until the account is recreated. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteUser | The operation that you want to perform. Set the value to Delet eUser. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Uid | String | Yes | 12345 | The ID of the Apsara Stack tenant account. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | 403 | The error code that is returned. |
| ErrorMessage | String | The specified user not exists. | The error message that is returned. |
| RequestId | String | 34E01EDD-6A16- 4CF0-9541- C644D1BE01AA | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeds. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteUser &Tid=-1 &Uid=12345 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteUserResponse>
    <RequestId>ADE24A7C-DB8B-4D32-94AD-E50E3B921197</RequestId>
    <Success>true</Success>
</DeleteUserResponse>
```

`JSON` format `{`

```json
    "RequestId":"34E01EDD-6A16-4CF0-9541-C644D1BE01AA",
    "Success":true
```

`}`

#### 6.2.6 ListUsers

Queries the details about users. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListUsers | The operation that you want to perform. Set the value to List Users. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Role | String | No | DBA | The role of users. For more information, see the description of the Regist erUser operation. |
| UserState | String | No | NORMAL | The status of users. Valid values: NORMAL: Users are normal. DISABLE: Users are disabled. DELETE: Uses are deleted. |
| SearchKey | String | No | test | The keyword that is used to search for users. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 50 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |

| eveloper Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 98D35416-2B92- 4CE5-8FD2- B1E61E165536 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TotalCount | Long | 1 | The total number of entries that are returned. |
| UserList | Array of User |   | The details about users. |
| User |   |   |   |
| CurExecuteCoun t | Long | 0 | The number of queries that are performed on the current day. |
| CurResultCount | Long | 0 | The number of rows that are queried on the current day. |
| LastLoginTime | String | 2020-02-02 00:00:00 | The last logon time. |
| MaxExecuteCou nt | Long | 1000 | The maximum number of queries that can be performed on the current day. |
| MaxResultCoun t | Long | 1000 | The maximum number of rows that can be queried on the current day. |
| Mobile | String | 188xxxxx | The DingTalk ID or mobile phone number of the user. |
| NickName | String | test | The name of the user. |
| ParentUid | String | 143214352 | The ID of the parent Apsara Stack tenant account of the user. |
| RoleIdList | List | 1 | The IDs of roles. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RoleNameList | List | ADMIN | The names of roles. |
| State | String | NORMAL | The status of the user. |
| Uid | String | 14324321533 | The ID of the Apsara Stack tenant account of the user. |
| UserId | String | 1 | The ID of the user. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListUsers &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UserList>
    <User>
        <RoleIdList>
            <RoleIds>3</RoleIds>
            <RoleIds>1</RoleIds>
        </RoleIdList>
        <State>NORMAL</State>
        <RoleNameList>
            <RoleNames>ADMIN</RoleNames>
            <RoleNames>USER</RoleNames>
        </RoleNameList>
        <NickName>xxx</NickName>
        <UserId>2</UserId>
        <Uid>111</Uid>
    </User>
    <User>
        <RoleIdList>
            <RoleIds>1</RoleIds>
            <RoleIds>3</RoleIds>
        </RoleIdList>
        <State>NORMAL</State>
        <RoleNameList>
            <RoleNames>USER</RoleNames>
            <RoleNames>ADMIN</RoleNames>
        </RoleNameList>
        <NickName>xxx[RAM user]</NickName>
        <ParentUid>111</ParentUid>
        <UserId>1</UserId>
        <Uid>111</Uid>
    </User>
</UserList> <TotalCount>2</TotalCount> <RequestId>2D346B20-BF4A-4C96-8295-DE8EB9BF5B90</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "UserList": {
    "User": [
```

`{`

```json
        "RoleIdList": {
          "RoleIds": [
```

`3,` `]` `},`

```json
        "State": "NORMAL",
        "RoleNameList": {
          "RoleNames": [
            "ADMIN",
            "USER"
```

`]` `},`

```json
        "NickName": "xxx",
        "UserId": 2,
        "Uid": "111"
```

`},` `{`

```json
        "RoleIdList": {
          "RoleIds": [
```

`1,` `]` `},`

```json
        "State": "NORMAL",
        "RoleNameList": {
          "RoleNames": [
            "USER",
            "ADMIN"
```

`]` `},`

```json
        "NickName": "xxx[RAM user]"
        "ParentUid": "111",
        "UserId": 1,
        "Uid": "111"
```

`}` `]` `},`

```json
  "TotalCount": 2,
  "RequestId": "2D346B20-BF4A-4C96-8295-DE8EB9BF5B90",
  "Success": true
```

`}`

#### 6.2.7 ListUserTenants

Queries tenants. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListUserTenants | The operation that you want to perform. Set the value to List UserT enant s. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where DMS resides. This parameter is used to call the operation. Not e Set this parameter to the ID of the region that is in proximity to your applications. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | CA1F4A4D-EE49- 472F-8DF9- F537101E263A | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TenantList | Array of Tenant |   | The tenants. |
| Status | String | ACTIVE | The status of the tenant. Valid values: ACTIVE: active. All users belong to this tenant. IN ACTIVE: inactive _ |
| TenantName | String | test | The name of the tenant. |
| Tid | Long | -1 | The ID of the tenant. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListUserTenants &RegionId=cn-hangzhou &<Common Request Parameters>
```

Sample success responses `XML` format

```xml
<RequestId>CA1F4A4D-EE49-472F-8DF9-F537101E263A</RequestId> <TenantList>
    <Status>ACTIVE</Status>
    <TenantName>test1</TenantName>
    <Tid>-1</Tid>
</TenantList> <TenantList>
    <Status>IN_ACTIVE</Status>
    <TenantName>test2</TenantName>
    <Tid>-2</Tid>
</TenantList> <TenantList>
    <Status>IN_ACTIVE</Status>
    <TenantName>tes</TenantName>
    <Tid>-3</Tid>
</TenantList>
```

`JSON` format `{`

```json
  "RequestId": "CA1F4A4D-EE49-472F-8DF9-F537101E263A",
  "TenantList": [
```

`{`

```json
      "Status": "ACTIVE",
      "TenantName": "test1",
      "Tid": -1
```

`},` `{`

```json
      "Status": "IN_ACTIVE",
      "TenantName": "test2",
      "Tid": -2
```

`},` `{`

```json
      "Status": "IN_ACTIVE",
      "TenantName": "tes",
      "Tid": -3
```

`}` `]` `}`

#### 6.2.8 GetUserActiveTenant

Queries the details about a tenant. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetUserActiveTen ant | The operation that you want to perform. Set the value to Get UserAct iveT enant . |
| RegionId | String | No | cn-hangzhou | The ID of the region where Data Management (DMS) resides. Not e Set this parameter to the ID of the region that is in proximity to your applications. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | E20EAB9F-A3DB- 42EC-BD0C- 102A886340F5 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| Tenant | Struct |   | The details about the tenant. |
| Status | String | ACTIVE | The status of the tenant. Valid values: ACTIVE: active IN ACTIVE: inactive _ |
| TenantName | String | test | The name of the tenant. |
| Tid | Long | -1 | The ID of the tenant. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetUserActiveTenant &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Tenant>
    <Status>ACTIVE</Status>
    <TenantName>test</TenantName>
    <Tid>-1</Tid>
</Tenant> <RequestId>E20EAB9F-A3DB-42EC-BD0C-102A886340F5</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "Tenant": {
    "Status": "ACTIVE",
    "TenantName": "test",
    "Tid": -1
```

`},`

```json
  "RequestId": "E20EAB9F-A3DB-42EC-BD0C-102A886340F5",
  "Success": true
```

`}`

#### 6.2.9 GetUser

Queries the details of a user. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetUser | The operation that you want to perform. Set the value to Get User. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Uid | String | No | 123344235 | The ID of the Apsara Stack tenant account of the user. |
| UserId | String | No | 1343 | The ID of the user. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | CFF30064-5985- 4ACB-B3F9- 9557596913C8 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| User | Struct |   | The information about the user. |
| CurExecuteCoun t | Long | 0 | The number of queries that were issued on the current day. |
| CurResultCount | Long | 0 | The number of rows that were queried on the current day. |
| LastLoginTime | String | 2020-02-02 00:00:00 | The last logon time. |
| MaxExecuteCou nt | Long | 1000 | The maximum number of queries that can be performed on the current day. |
| MaxResultCoun t | Long | 1000 | The maximum number of rows that can be queried on the current day. |
| Mobile | String | 138xxxxxxxx | The mobile phone number of the user. |
| NickName | String | nickName | The name of the user. |
| ParentUid | Long | 12345352 | The ID of the Apsara Stack tenant account. |
| RoleIdList | List | 1 | The IDs of the roles. |
| RoleNameList | List | Common user | The names of the roles. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| State | String | NORMAL | The status of the user. |
| Uid | String | 1243215435 | The ID of the Apsara Stack tenant account of the user. |
| UserId | String | 122 | The ID of the user. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetUser &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<User>
    <RoleIdList>
        <RoleIds>1</RoleIds>
        <RoleIds>4</RoleIds>
        <RoleIds>3</RoleIds>
        <RoleIds>2</RoleIds>
    </RoleIdList>
    <State>NORMAL</State>
    <RoleNameList>
        <RoleNames>Common user</RoleNames>
        <RoleNames>Security administrator</RoleNames>
        <AccountDescription>Administrator</AccountDescription>
        <RoleNames>DBA</RoleNames>
    </RoleNameList>
    <NickName>xxx</NickName>
    <ParentUid>114324325</ParentUid>
    <UserId>432143</UserId>
    <Uid>41234234324</Uid>
</User> <RequestId>CFF30064-5985-4ACB-B3F9-9557596913C8</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "User": {
    "RoleIdList": {
      "RoleIds": [
```

`1,` `4,` `3,` `]` `},`

```json
    "State": "NORMAL",
    "RoleNameList": {
      "RoleNames": [
        "Common user",
        "Security administrator",
        "Administrator",
        "DBA"
```

`]` `},`

```json
    "NickName": "xxx",
    "ParentUid": "114324325",
    "UserId": 432143,
    "Uid": "41234234324"
```

`},`

```json
  "RequestId": "CFF30064-5985-4ACB-B3F9-9557596913C8",
  "Success": true
```

`}`

### 6.3 Instance management

#### 6.3.1 RegisterInstance

Adds a database instance to your enterprise. The administ rat or and dat abase administ rat or (DBA) of Data Management (DMS) Enterprise can call this operation to add database instances to DMS Enterprise. To check users who assume the administrator or DBA role, perform the following steps: Log on to the DMS Enterprise console and choose System Management > User Management. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RegisterInstance | The operation that you want to perform. Set the value to Regist erInst ance. |
| Tid | Long | Yes | -1 | The ID of the tenant. |

| Data Management |   |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceType | String | Yes | MySQL | The type of the database instance. Valid values: MySQL SQLServer PostgreSQL Oracle DRDS OceanBase Mongo Redis |
| InstanceSource | String | Yes | RDS | The source of the database instance. Valid values: PUBLIC OWN: a self-managed _ database that is created in the public network. RDS: an ApsaraDB RDS instance. ECS OWN: a self-managed _ database that is created on an Elastic Compute Service (ECS) instance. VPC IDC: a self-managed database _ that is created in the Internet data center (IDC) of a virtual private cloud (VPC). |
| NetworkType | String | Yes | VPC | The type of the network. |
| EnvType | String | Yes | product | The type of the environment. Valid values: product: production environment dev: development environment pre: staging environment test: test environment sit: SIT environment uat: UAT environment pet: stress testing environment stag: STAG environment |
| Host | String | Yes | dmstest.rds.aliyu n.com | The host address of the required database. |

| eveloper Guide·API | Reference |   |   | Data Managemen |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Port | Integer | Yes | 3306 | The number of the port that is used to connect to the required database. |
| DatabaseUser | String | Yes | dmstest | The username of the account that is used to log on to the database. |
| DatabasePasswor d | String | Yes | password | The password of the account. |
| InstanceAlias | String | Yes | Test instance | The name of the instance. Specify a name that can help you identify and locate the instance. |
| DbaUid | Long | Yes | 12345678 | The ID of the Apsara Stack tenant account for the database administrator (DBA) of the instance. |
| SafeRule | String | Yes | Test | The name of the security rule that belongs to your enterprise. |
| QueryTimeout | Integer | Yes | 60 | The timeout period for the query. Unit: seconds. |
| ExportTimeout | Integer | Yes | 600 | The timeout period for the export. Unit: seconds. |
| EcsInstanceId | String | No | i-xxxxxxxxx | The ID of the ECS instance. Not e This parameter is required if the Inst anceSource parameter is set to ECS OWN. _ |
| VpcId | String | No | vpc- xxxxxxxxxxxxxxxx xxxxx | The ID of the VPC. Not e This parameter is required if the Inst anceSource parameter is set to VPC IDC. _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EcsRegion | String | No | cn-hangzhou | The region where the instance resides. Not e This parameter is required if the Inst anceSource parameter is set to RDS, ECS OWN, _ or VPC IDC. _ |
| Sid | String | No | dmstest | The system identifier (SID) of the database. Not e This parameter is required if the Inst anceT ype parameter is set to PostgreSQL or Oracle. |
| DataLinkName | String | No | dblink test _ | The name of the data link for cross- database queries. |
| DdlOnline | Integer | No | 2 | Specifies whether to enable the online data description language (DDL) service. This service is available only for the MySQL and PolarDB databases. 0: The service is disabled. 1: The native online DDL service takes precedence. 2: Data changes for the schema of lock-free DMS tables take precedence. |
| UseDsql | Integer | No | 1 | Specifies whether to enable the cross- database query feature for the instance. Valid values: 0: Disable the feature. 1: Enable the feature. |
| SkipTest | Boolean | No | true | Specifies whether to skip the connection test. Valid values: t rue: Skip the connection test. f alse: Perform the connection test. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | 404 | The returned error code. |
| ErrorMessage | String | The specified instance already exists. | The returned error message. |
| RequestId | String | F4E2A94B-604F- 43FF-93E7- F4EE3DCF412E | The ID of the request. Each request has a unique ID. |
| Success | Boolean | true | t rue: The request succeeded. f alse: The request failed. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RegisterInstance &Tid=-1 &InstanceType=MySQL &InstanceSource=RDS &NetworkType=VPC &EnvType=product &Host=dmstest.rds.aliyun.com &Port=3306 &DatabaseUser=dmstest &DatabasePassword=password &InstanceAlias=Test instance &DbaUid=12345678 &SafeRule=Test &QueryTimeout=60 &ExportTimeout=600 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RegisterInstanceResponse>
      <RequestId>D4F02899-CE79-4DFD-9893-5217DA70B363</RequestId>
      <Success>true</Success>
</RegisterInstanceResponse>
```

`JSON` format `{`

```json
    "RequestId": "F4E2A94B-604F-43FF-93E7-F4EE3DCF412E",
    "Success": true
```

`}` SDK for Python example The following example shows how to add an instance that resides in VPC.

```
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkdms_enterprise.request.v20181101.RegisterInstanceRequest import RegisterInsta nceRequest client = AcsClient(
    "<your-access-key-id>",
    "<your-access-key-secret>",
    "<your-region-id>"
```

`)`

```bash
# Example
request = RegisterInstanceRequest()
# The ID of the tenant.
request.set_Tid(1)
# The endpoint of the instance.
request.set_Host("192.168.16.113")
# The number of the port that is used to connect to the instance.
request.set_Port(3314)
# The type of the database, for example, MySQL.
request.set_InstanceType("MySQL")
# The source of the instance, for example, VPC_IDC.
request.set_InstanceSource("VPC_IDC")
# The network type, for example, VPC.
request.set_NetworkType("VPC") request.set_EnvType("PRODUCT")
# request.set_EcsInstanceId()
# The ID of the VPC to which the instance belongs.
request.set_VpcId("VPC ID of the instance")
# The region ID of the ECS instance in which the database resides, for example, cn-hangzhou
```

`.`

```bash
request.set_EcsRegion("Region ID of the ECS instance")
# request.set_Sid();
# The username of the account that is used to log on to the database.
request.set_DatabaseUser("Logon username of the database")
# The password of the account.
request.set_DatabasePassword("Logon password of the database")
# The alias of the instance. Specify an alias that helps you identify the related instance
in DMS Enterprise. request.set_InstanceAlias("Alias of the instance")
# The ID of the Apsara Stack tenant account for the database administrator (DBA) of the ins
tance. The user must first be added to DMS Enterprise by using the console or the required API operation. request.set_DbaUid(-1) request.set_SafeRule("Name of the security rule that is configured in DMS Enterprise") request.set_QueryTimeout(60) request.set_ExportTimeout(600) response = client.do_action_with_exception(request) print response
```

#### 6.3.2 ListInstances

Queries the details about instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListInstances | The operation that you want to perform. Set the value to List Inst ances. |
| Tid | Long | No | -1 | The ID of the tenant. |
| SearchKey | String | No | test | The keyword that is used to search for instances. |
| DbType | String | No | MySQL | The type of databases. |
| EnvType | String | No | product | The type of the environment to which instances belong. |
| InstanceSource | String | No | RDS | The source of instances. |
| NetType | String | No | VPC | The network environment of instances. For more information, see the description of the Regist erInst ance operation. |
| InstanceState | String | No | NORMAL | The status of instances. Valid values: NORMAL: Instances functions as expected. DISABLE: Instances are disabled. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 50 | The number of entries to return on each page. Maximum value: 100. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| InstanceList | Array of Instance |   | The instances. |
| Instance |   |   |   |
| DataLinkName | String | dblink test _ | The name of the data link for the instance. |
| DatabasePassw ord | String | ****** | The password of the account that is used to log on to the database. |
| DatabaseUser | String | dbUser | The username of the account that is used to log on to the database. |
| DbaId | String | 1 | The ID of the database administrator (DBA) for the instance. |
| DbaNickName | String | dbaName | The name of the DBA. |
| DdlOnline | Integer | 1 | The configuration of the online data description language (DDL) feature for the instance. |
| EcsInstanceId | String | xxx | The ID of the ECS instance. |
| EcsRegion | String | cn-hangzhou | The region to which the ECS instance belongs. |
| EnvType | String | product | The type of the environment to which the instance belongs. |
| ExportTimeout | Integer | 600 | The timeout period to export the instance. |
| Host | String | xxx.xxx.xxx.xxx | The endpoint of the instance. |
| InstanceAlias | String | test | The alias of the instance. |

| ata Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| InstanceId | String | 1 | The ID of the instance. |
| InstanceSource | String | RDS | The source of the instance. |
| InstanceType | String | mysql | The type of the database for the instance. |
| OwnerIdList | List | 1 | The IDs of the owners of the database. |
| OwnerNameList | List | 11 | The names of the owners of the database. |
| Port | Integer | 3306 | The number of the port that is used to connect to the instance. |
| QueryTimeout | Integer | 60 | The timeout period to query the instance. |
| SafeRuleId | String | 1 | The ID of the security rule for the instance. |
| Sid | String | test | The system identifier (SID) of the instance. |
| State | String | NORMAL | The status of the instance. |
| UseDsql | Integer | 1 | Indicates whether the cross-database query feature is enabled for the instance. |
| VpcId | String | xxx | The ID of the virtual private cloud (VPC) to which the instance belongs. |
| RequestId | String | B4B07137-F6AE- 4756-8474- 7F92BB6C4E04 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TotalCount | Long | 0 | The total number of entries that are returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListInstances &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>7</TotalCount> <RequestId>98D35416-2B92-4CE5-8FD2-B1E61E165536</RequestId> <Success>true</Success> <InstanceList> </InstanceList>
```

`JSON` format `{`

```json
  "TotalCount": 7,
  "RequestId": "98D35416-2B92-4CE5-8FD2-B1E61E165536",
  "Success": true,
  "InstanceList": {
    "Instance": [
```

`]` `}` `}`

#### 6.3.3 GetInstance

Queries the details about an instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetInstance | The operation that you want to perform. Set the value to Get Inst ance. |
| Host | String | Yes | xxxx.mysql.rds.ali yuncs.com | The endpoint of the instance. |
| Port | Integer | Yes | 3306 | The number of the port that is used to connect to the instance. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Sid | String | No | test | The system identifier (SID) of the instance. |

| D | ata Management |   |   |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| Instance | Struct |   | The details about the instance. |
| DataLinkName | String | test | The name of the data link for the instance. |
| DatabasePassw ord | String | ****** | The logon password of the instance. |
| DatabaseUser | String | dbuser | The logon username of the instance. |
| DbaId | String | 1 | The ID of the database administrator (DBA) for the instance. You can call the ListUsers operation to obtain the ID. |
| DbaNickName | String | dbaname | The name of the DBA for the instance. |
| DdlOnline | Integer | 1 | Indicates whether the online data description language (DDL) service is enabled for the instance. |
| EcsInstanceId | String | xxx | The ID of the ECS instance. |
| EcsRegion | String | cn-hangzhou | The ID of the region in which the instance resides. |
| EnvType | String | test | The type of the environment to which the instance belongs. |
| ExportTimeout | Integer | 600 | The timeout period to export the instance. |

| eveloper Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Host | String | xxx.rwlb.rds.aliyuncs .com | The endpoint of the instance. |
| InstanceAlias | String | test | The alias of the instance. |
| InstanceId | String | 1 | The ID of the instance. |
| InstanceSource | String | RDS | The source of the instance. |
| InstanceType | String | polardb | The database type of the instance. |
| OwnerIdList | List | 88656 | The IDs of the owners of the instance. |
| OwnerNameList | List | xxx | The names of the owners of the instance. |
| Port | Integer | 3306 | The number of the port that is used to connect to the instance. |
| QueryTimeout | Integer | 60 | The timeout period to query the instance. |
| SafeRuleId | String | 1 | The ID of the security rule of the instance. |
| Sid | String | test | The SID of the instance. |
| State | String | NORMAL | The status of the instance. |
| UseDsql | Integer | 1 | Indicates whether the cross-database query feature is enabled for the instance. |
| VpcId | String | xxx | The ID of the VPC to which the instance belongs. |
| RequestId | String | 8BE73E78-76E2- 46AA-970D- A4579A16CD4A | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetInstance &Host=xxxx.mysql.rds.aliyuncs.com &Port=3306 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Instance>
    <SafeRuleId>1037</SafeRuleId>
    <UseDsql>1</UseDsql>
    <EcsInstanceId>pc-xxx</EcsInstanceId>
    <QueryTimeout>80</QueryTimeout>
    <Host>xxx.rwlb.rds.aliyuncs.com</Host>
    <InstanceAlias>test</InstanceAlias>
    <InstanceSource>RDS</InstanceSource>
    <InstanceId>24710</InstanceId>
    <DataLinkName>dblink_test</DataLinkName>
    <EnvType>dev</EnvType>
    <DdlOnline>0</DdlOnline>
    <VpcId>vpc-xxx</VpcId>
    <InstanceType>polardb</InstanceType>
    <DbaId>104442</DbaId>
    <Port>3306</Port>
    <DbaNickName>test[RAM user]</DbaNickName>
    <State>NORMAL</State>
    <DatabaseUser>dmstest</DatabaseUser>
    <DatabasePassword>******</DatabasePassword>
    <EcsRegion>cn-hangzhou</EcsRegion>
    <ExportTimeout>300</ExportTimeout>
</Instance> <RequestId>8BE73E78-76E2-46AA-970D-A4579A16CD4A</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "Instance": {
    "SafeRuleId": 1037,
    "UseDsql": "1",
    "EcsInstanceId": "pc-xxx",
    "QueryTimeout": 80,
    "Host": "xxx.rwlb.rds.aliyuncs.com",
    "InstanceAlias": "test",
    "InstanceSource": "RDS",
    "InstanceId": 24710,
    "DataLinkName": "dblink_test",
    "EnvType": "dev",
    "DdlOnline": 0,
    "VpcId": "vpc-xxx",
    "InstanceType": "polardb",
    "DbaId": 104442,
    "Port": 3306,
    "DbaNickName": <DbaNickName>test[RAM user]</DbaNickName>
    "State": "NORMAL",
    "DatabaseUser": "dmstest",
    "DatabasePassword": "******",
    "EcsRegion": "cn-hangzhou",
    "ExportTimeout": 300
```

`},`

```json
  "RequestId": "8BE73E78-76E2-46AA-970D-A4579A16CD4A",
  "Success": true
```

`}`

#### 6.3.4 UpdateInstance

Updates the information about a database instance and checks the connectivity of the instance. Before you call this operation to update the information about an instance, we recommend that you call the GetInstance operation to obtain the complete information about the instance. Then, you can set the required parameters based on the information that you obtain. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateInstance | The operation that you want to perform. Set the value to Updat eInst ance. |
| DatabasePasswor d | String | Yes | ****** | The password of the database account. |

| ata Management |   |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DatabaseUser | String | Yes | dbuser | The username of the database account. |
| DbaId | String | Yes | 1 | The ID of the database administrator (DBA) for the instance. You can call the List Users operation to query the ID. |
| EnvType | String | Yes | test | The type of the environment to which the instance belongs. |
| ExportTimeout | Integer | Yes | 600 | The timeout period to export of the instance. |
| Host | String | Yes | xxxx.mysql.rds.ali yuncs.com | The endpoint of the instance. |
| InstanceAlias | String | Yes | test | The alias of the instance. |
| InstanceId | String | Yes | 1 | The ID of the instance. You can call the Get Inst ance operation to query the ID. |
| InstanceSource | String | Yes | RDS | The source of the instance. You can call the Regist erInst ance operation to query the source. |
| InstanceType | String | Yes | MySQL | The type of the instance. You can call the Regist erInst ance operation to query the type. |
| Port | Integer | Yes | 3306 | The port of the instance. |
| QueryTimeout | Integer | Yes | 60 | The timeout period to query the instance. |
| SafeRuleId | String | Yes | 1 | The ID of the security rule of the instance. |
| Tid | Long | Yes | -1 | The ID of the tenant. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EcsInstanceId | String | No | xxx | The ID of the ECS instance. |
| VpcId | String | No | xxx | The ID of the VPC to which the instance belongs. |
| EcsRegion | String | No | cn-hangzhou | The ID of the region in which the instance resides. |
| Sid | String | No | xxx | The system identifier (SID) of the instance. |
| DataLinkName | String | No | datalink test _ | The name of the data link for the instance. |
| DdlOnline | Integer | No | 1 | Specifies whether to enable the online data description language (DDL) service for the instance. For more information about the valid values, see the description of the Regist erInst ance operation. |
| UseDsql | Integer | No | 1 | Specifies whether to enable the cross- database query feature for the instance. |
| SkipTest | Boolean | No | true | Specifies whether to skip the connectivity check. Valid values: true: Skip the connectivity check. false: Perform the connectivity check. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | E9BEBF41-4F69- 4605-A5D5- A67955173941 | The ID of the request. |
| Success | Boolean | false | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UpdateInstance &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>E9BEBF41-4F69-4605-A5D5-A67955173941</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "E9BEBF41-4F69-4605-A5D5-A67955173941",
  "Success": true
```

`}`

#### 6.3.5 DeleteInstance

Removes a database instance from Data Management (DMS) Enterprise. This operation only removes a database instance from the DMS Enterprise console. The database instance is not disabled. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteInstance | The operation that you want to perform. Set the value to Delet eInst ance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Host | String | Yes | xxx.mysql.rds.aliy uncs.com | The endpoint of the database instance to be removed. |
| Port | Integer | Yes | 3306 | The connection port of the database instance to be removed. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Sid | String | No | testSid | The SID of the database instance to be removed. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | B4B07137-F6AE- 4756-8474- 7F92BB6C4E04 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteInstance &Host=xxx.mysql.rds.aliyuncs.com &Port=3306 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B4B07137-F6AE-4756-8474-7F92BB6C4E04</RequestId> <ErrorCode>UnknownError</ErrorCode> <ErrorMessage>UnknownError</ErrorMessage> <Success>true</Success>
```

`JSON` format

```json
{"RequestId":"B4B07137-F6AE-4756-8474-7F92BB6C4E04","ErrorCode":"UnknownError","ErrorMessag e":"UnknownError","Success":"true"}
```

### 6.4 Operation logs

#### 6.4.1 GetOpLog

Queries the details about operation logs that are generated in a specified period. The administ rat or and securit y administ rat or roles of an account can all this operation. For more information about account roles, see User management. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetOpLog | The operation that you want to perform. Set the value to Get OpLog. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| StartTime | String | Yes | 2018-11-01 10:00:00 | The start of the time range to query. The time must be specified in the yyyy- MM-ddTHH:mm:ssZ format. |
| EndTime | String | Yes | 2018-11-01 11:00:00 | The end of the time range to query. The time must be specified in the yyyy- MM-ddTHH:mm:ssZ format. |
| PageNumber | Integer | Yes | 3 | The number of the page to return. Pages start from page 1. |
| PageSize | Integer | Yes | 30 | The number of entries to return on each page. Valid values: 30 50 100 |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Module | String | No | PERMISSION | The function module that specifies the type of operation logs that you want to return. If you do not set this parameter, all operation logs that are generated in the specified time range are returned. Valid values: PERMISSION: permissions OWNER: data owner SQL CONSOLE: data query _ SQL CONSOLE EXPORT : query _ _ result export DAT A CHANGE: data change _ DAT A EXPORT : data export _ SQL REVIEW: SQL review _ DT SYNC: database and table _ synchronization DT DET AIL: database and table _ details DB T ASK: task management _ INST ANCE MANAGE: instance _ management USER MANAGE: user management _ SECURIT Y RULE: security rules _ CONFIG MANAGE: configuration _ management RESOURCE AUT H: resource _ authorization ACCESS WHIT E IP: access to IP _ _ whitelists |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | 403 | The returned error code. |
| ErrorMessage | String | The specified request parameter is invalid. | The error message that is returned. |

| ata Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| OpLogDetails | Array of OpLogDetail |   | The details about operation logs. |
| OpLogDetail |   |   |   |
| Database | String | dmstest prod data _ _ base@dmstest.rds.. . [Test instance] | The endpoint of the database. A value is returned for this parameter only when the database type is set to LocalInst ance. Not e |
| Module | String | PERMISSION | The function module. |
| OpContent | String | Apply for permissions | The details about the operation. |
| OpTime | String | 2018-11-01 10:00:00 | The time when the operation was performed. |
| OrderId | Long | 1 | The ID of the ticket or task. Not e |
| UserId | Long | 12345678 | The ID of the Apsara Stack tenant account. |
| UserNick | String | dmstest | The name of the user. |
| RequestId | String | 47D56208-DB1D- 4FD3-BE32- 300E43185488 | The ID of the request. Each request has a unique ID. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TotalCount | Long | 22 | The total number of operation logs. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetOpLog &Tid=-1 &StartTime=2018-11-01 10:00:00 &EndTime=2018-11-01 11:00:00 &PageNumber=3 &PageSize=30 &<Common request parameters>
```

Sample success response `XML` format

```xml
<OpLogDetails>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS s
tore_capacity FROM information_schema.tables WHERE table_type = &amp;#39;BASE TABLE&amp;#39 ; AND `table_schema` = &amp;#39;dmstest_database&amp;#39; AND `table_name` = &amp;#39;multi _db_multi_tbl&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:04:10</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS s
tore_capacity FROM information_schema.tables WHERE table_type = &amp;#39;BASE TABLE&amp;#39 ; AND `table_schema` = &amp;#39;dmstest_database&amp;#39; AND `table_name` = &amp;#39;multi _db_multi_tbl&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:04:06</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 24.)show topology FROM multi_db_multi_tbl</
OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:03:55</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS s
tore_capacity FROM information_schema.tables WHERE table_type = &amp;#39;BASE TABLE&amp;#39 ; AND `table_schema` = &amp;#39;dmstest_database&amp;#39; AND `table_name` = &amp;#39;user_ log3&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:02:59</OpTime>
        <Module>Data query</Module>
```

`q` `y``/`

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS s
tore_capacity FROM information_schema.tables WHERE table_type = &amp;#39;BASE TABLE&amp;#39 ; AND `table_schema` = &amp;#39;dmstest_database&amp;#39; AND `table_name` = &amp;#39;user_ log3&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 20:02:49</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 1.)show CREATE TABLE user_log3</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:34:05</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 9.)SELECT `TABLE_NAME` FROM information_sch
ema.tables WHERE TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmst est_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:33:54</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>Creates an SQL task. Task ID: 5486.</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:26:57</OpTime>
        <Module>Task management</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>Creates an SQL task. Task ID: 5485.</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:23:55</OpTime>
        <Module>Task management</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>Creates an SQL task. Task ID: 5484.</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:23:30</OpTime>
        <Module>Task management</Module>
    </OpLogDetail>
```

```xml
    <OpLogDetail>
        <OpContent>Creates an SQL task. Task ID: 5483.</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:23:11</OpTime>
        <Module>Task management</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 1.)show CREATE TABLE multi_db_single_tbl</O
pContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:22:30</OpTime>
        <Module>SQL_CONSOLE</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 2.)SELECT `TABLE_NAME` FROM information_sch
ema.tables WHERE TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmst est_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:22:15</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 2.)SELECT `TABLE_NAME` FROM information_sch
ema.tables WHERE TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmst est_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:19:31</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>Creates an SQL task. Task ID: 5482.</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:19:25</OpTime>
        <Module>Task management</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 1.)SELECT `TABLE_NAME` FROM information_sch
ema.tables WHERE TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmst est_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:18:57</OpTime>
        <Module>Data query</Module>
```

```xml
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>Creates an SQL task. Task ID: 5481.</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:18:46</OpTime>
        <Module>Task management</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 0.)SELECT `TABLE_NAME` FROM information_sch
ema.tables WHERE TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmst est_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:04:13</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 0.)SELECT `TABLE_NAME` FROM information_sch
ema.tables WHERE TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmst est_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 14:04:08</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>(Successful. Number of rows: 0.)SELECT `TABLE_NAME` FROM information_sch
ema.tables WHERE TABLE_TYPE = &amp;#39;BASE TABLE&amp;#39; AND table_schema = &amp;#39;dmst est_database&amp;#39;</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 12:11:41</OpTime>
        <Module>Data query</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>The administrator or DBA changes the owner of a database. Database name:
dmstest_database@dmstest.rds...(test)</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
        <OpTime>2018-11-22 12:11:14</OpTime>
        <Module>Data owner</Module>
    </OpLogDetail>
    <OpLogDetail>
        <OpContent>The administrator or DBA changes the owner of a database. Database name:
dmstest_prod_database@dmstest.rds...(test)</OpContent>
        <UserNick>dmstest</UserNick>
        <Database>dmstest_prod_database@dmstest.rds...(test)</Database>
        <UserId>12345678</UserId>
```

`O` `i`

```
20181122121107/O
```

`i`

```xml
        <OpTime>2018-11-22 12:11:07</OpTime>
        <Module>Data owner</Module>
    </OpLogDetail>
</OpLogDetails> <TotalCount>22</TotalCount> <RequestId>47D56208-DB1D-4FD3-BE32-300E43185488</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
 "OpLogDetails": {
  "OpLogDetail": [{
   "OpContent": "(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS sto
re_capacity FROM information_schema.tables WHERE table_type = &#39;BASE TABLE&#39; AND `tab le_schema` = &#39;dmstest_database&#39; AND `table_name` = &#39;multi_db_multi_tbl&#39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 20:04:10",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS sto
re_capacity FROM information_schema.tables WHERE table_type = &#39;BASE TABLE&#39; AND `tab le_schema` = &#39;dmstest_database&#39; AND `table_name` = &#39;multi_db_multi_tbl&#39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 20:04:06",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 24.)show topology FROM multi_db_multi_tbl",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 20:03:55",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS sto
re_capacity FROM information_schema.tables WHERE table_type = &#39;BASE TABLE&#39; AND `tab le_schema` = &#39;dmstest_database&#39; AND `table_name` = &#39;user_log3&#39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 20:02:59",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 1.)SELECT (data_length + index_length) AS sto
re_capacity FROM information_schema.tables WHERE table_type = &#39;BASE TABLE&#39; AND `tab le_schema` = &#39;dmstest_database&#39; AND `table_name` = &#39;user_log3&#39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 20:02:49",
```

```json
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 1.)show CREATE TABLE user_log3",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:34:05",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 9.)SELECT `TABLE_NAME` FROM information_schem
a.tables WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&# 39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:33:54",
   "Module": "Data query"
  }, {
   "OpContent": "Creates an SQL task. Task ID: 5486.",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:26:57",
   "Module": "Task management"
  }, {
   "OpContent": "Creates an SQL task. Task ID: 5485.",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:23:55",
   "Module": "Task management"
  }, {
   "OpContent": "Creates an SQL task. Task ID: 5484.",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:23:30",
   "Module": "Task management"
  }, {
   "OpContent": "Creates an SQL task. Task ID: 5483.",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:23:11",
   "Module": "Task management"
  }, {
   "OpContent": "(Successful. Number of rows:1)show CREATE TABLE multi_db_single_tbl",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:22:30",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 2.)SELECT `TABLE_NAME` FROM information_schem
```

```json
a.tables WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&# 39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:22:15",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 2.)SELECT `TABLE_NAME` FROM information_schem
a.tables WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&# 39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:19:31",
   "Module": "Data query"
  }, {
   "OpContent": "Creates an SQL task. Task ID: 5482.",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:19:25",
   "Module": "Task management"
  }, {
   "OpContent": "(Successful. Number of rows: 1.)SELECT `TABLE_NAME` FROM information_schem
a.tables WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&# 39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:18:57",
   "Module": "Data query"
  }, {
   "OpContent": "Creates an SQL task. Task ID: 5481.",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:18:46",
   "Module": "Task management"
  }, {
   "OpContent": "(Successful. Number of rows: 0.)SELECT `TABLE_NAME` FROM information_schem
a.tables WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&# 39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:04:13",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 0.)SELECT `TABLE_NAME` FROM information_schem
a.tables WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&# 39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
```

`"U`

```
Id" 12345678
```

```json
   "UserId": 12345678,
   "OpTime": "2018-11-22 14:04:08",
   "Module": "Data query"
  }, {
   "OpContent": "(Successful. Number of rows: 0.)SELECT `TABLE_NAME` FROM information_schem
a.tables WHERE TABLE_TYPE = &#39;BASE TABLE&#39; AND table_schema = &#39;dmstest_database&# 39;",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 12:11:41",
   "Module": "Data query"
  }, {
   "OpContent": "The administrator or DBA edits the database owner. Database name: dmstest_
prod_database@dmstest.rds...",
   "UserNick": "dmstest",
   "Database": "dmstest_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 12:11:14",
   "Module": "Data owner"
  }, {
   "OpContent": "The administrator or DBA edits the database owner. Database name: dmstest_
prod_database@dmstest.rds...",
   "UserNick": "dmstest",
   "Database": "dmstest_prod_database@dmstest.rds...(test)",
   "UserId": 12345678,
   "OpTime": "2018-11-22 12:11:07",
   "Module": "Data owner"
```

`}]` `},`

```json
 "TotalCount": 22,
 "RequestId": "47D56208-DB1D-4FD3-BE32-300E43185488",
 "Success": true
```

`}` SDK example For more information about how to use the SDK, see the Alibaba Cloud SDK for Python. Example:

```
from aliyunsdkcore.client import AcsClient from aliyunsdkdms_enterprise.request.v20181101.GetOpLogRequest import GetOpLogRequest client = AcsClient(
    "<your-access-key-id>",
   "<your-access-key-secret>",
   "<your-region-id>"
```

`)`

```
request = GetOpLogRequest() request.set_Tid("Enter the tenant ID of your enterprise") request.set_StartTime("2018-11-20 00:00:00") request.set_EndTime("2018-11-23 00:00:00") request.set_PageNumber(1) request.set_PageSize(50) response = client.do_action_with_exception(request) print response
```

### 6.5 Approval processes

#### 6.5.1 ListWorkFlowTemplates

Queries the details about approval templates. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListWorkFlowTe mplates | The operation that you want to perform. Set the value to List WorkFlowT emplat es. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| SearchName | String | No | Admin | The name that is used to search for approval templates. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |

| D | ata Management |   |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 41067071-0243- 4AAB-B3CF- 4DE6D54F53B4 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| WorkFlowTemp lates | Array of WorkFlowTemp late |   | The approval templates. |
| WorkFlowTemp late |   |   |   |
| Comment | String | test | The remarks. |
| CreateUserId | Long | 1234 | The ID of the creator. |
| Enabled | String | Y | Indicates whether the approval template is enabled. Valid values: Y: enabled N: disabled |
| IsSystem | Integer | 1 | Indicates whether the approval template is predefined by the system. Valid values: 1: The approval template is predefined by the system. 0: The approval template is not predefined by the system. |
| TemplateId | Long | 12345 | The ID of the approval template. |
| TemplateName | String | Admin | The name of the approval template. |
| WorkflowNode s | Array of WorkflowNode |   | The details about approval nodes. |
| WorkflowNode |   |   |   |
| Comment | String | test | The remarks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateUserId | Long | 1234 | The ID of the creator. |
| NodeId | Long | 123 | The ID of the approval node. |
| NodeName | String | test | The name of the approval node. |
| NodeType | String | SYS | The type of the approval node. Valid values: SYS: The approval node is predefined by the system. USER LIST: The approval node is created _ by a user. |
| Position | Integer | 1 | The order. |
| TemplateId | Long | 12345 | The ID of the approval template. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListWorkFlowTemplates &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>41067071-0243-4AAB-B3CF-4DE6D54F53B4</RequestId> <Success>true</Success> <WorkFlowTemplates>
    <WorkFlowTemplate>
        <Comment>The system-defined approval workflow. Only an administrator is included in
the approval workflow to review requests.</Comment>
        <WorkFlowNodes>
            <WorkFlowNode>
                <Comment>The system-defined node that is dynamically generated. Requests ar
e reviewed by an administrator.</Comment>
                <NodeName>Admin</NodeName>
                <Position>0</Position>
                <NodeType>SYS</NodeType>
                <NodeId>3763</NodeId>
                <TemplateId>6243</TemplateId>
            </WorkFlowNode>
        </WorkFlowNodes>
```

`<T`

```
ltN >Adi</T ltN
```

`>`

```xml
        <TemplateName>Admin</TemplateName>
        <Enabled>Y</Enabled>
        <IsSystem>1</IsSystem>
        <TemplateId>6243</TemplateId>
    </WorkFlowTemplate>
    <WorkFlowTemplate>
        <Comment>The system-defined approval workflow. Each request must be reviewed by the
data owner, DBA, and admin in sequence.</Comment>
        <WorkflowNodes>
            <WorkFlowNode>
                <Comment>The system-defined node that is dynamically generated. The owner o
f the resources that you want to manage is required to review the related requests.</Commen
```

`t>`

```xml
                <NodeName>Owner</NodeName>
                <Position>0</Position>
                <NodeType>SYS</NodeType>
                <NodeId>3762</NodeId>
                <TemplateId>6244</TemplateId>
            </WorkFlowNode>
            <WorkFlowNode>
                <Comment>The system-defined node that is dynamically generated. The DBA of
the resources that you want to manage is required to review the related requests.</Comment>
                <NodeName>DBA</NodeName>
                <Position>0</Position>
                <NodeType>SYS</NodeType>
                <NodeId>3761</NodeId>
                <TemplateId>6244</TemplateId>
            </WorkFlowNode>
            <WorkFlowNode>
                <Comment>The system-defined node that is dynamically generated. Requests ar
e reviewed by an administrator.</Comment>
                <NodeName>Admin</NodeName>
                <Position>0</Position>
                <NodeType>SYS</NodeType>
                <NodeId>3763</NodeId>
                <TemplateId>6244</TemplateId>
            </WorkFlowNode>
        </WorkflowNodes>
        <TemplateName>Owner--&gt;DBA--&gt;Admin</TemplateName>
        <Enabled>Y</Enabled>
        <IsSystem>1</IsSystem>
        <TemplateId>6244</TemplateId>
    </WorkFlowTemplate>
</WorkFlowTemplates>
```

`JSON` format `{`

```json
  "RequestId": "41067071-0243-4AAB-B3CF-4DE6D54F53B4",
  "Success": true,
  "WorkFlowTemplates": {
    "WorkFlowTemplate": [
```

`{`

```json
        "Comment": "The system-defined approval workflow. Only an administrator is included
```

```json
in the approval workflow to review requests.",
        "WorkFlowNodes": {
          "WorkFlowNode": [
```

`{`

```json
              "Comment": "The system-defined node that is dynamically generated. Requests a
re reviewed by an administrator.",
              "NodeName": "Admin",
              "Position": 0,
              "NodeType": "SYS",
              "NodeId": 3763,
              "TemplateId": 6243
```

`}` `]` `},`

```json
        "TemplateName": "Admin",
        "Enabled": "Y",
        "IsSystem": 1,
        "TemplateId": 6243
```

`},` `{`

```json
        "Comment": "The system-defined approval workflow. Each request must be reviewed by
the data owner, DBA, and admin in sequence.",
        "WorkflowNodes": {
          "WorkFlowNode": [
```

`{`

```json
              "Comment": ">The system-defined node that is dynamically generated. The owner
of the resources that you want to manage is required to review the related requests.",
              "NodeName": "Owner",
              "Position": 0,
              "NodeType": "SYS",
              "NodeId": 3762,
              "TemplateId": 6244
```

`},` `{`

```json
              "Comment": "The system-defined node that is dynamically generated. The DBA of
the resources that you want to manage is required to review the related requests.",
              "NodeName": "DBA",
              "Position": 0,
              "NodeType": "SYS",
              "NodeId": 3761,
              "TemplateId": 6244
```

`},` `{`

```json
              "Comment": "The system-defined node that is dynamically generated. Requests a
re reviewed by an administrator.",
              "NodeName": "Admin",
              "Position": 0,
              "NodeType": "SYS",
              "NodeId": 3763,
              "TemplateId": 6244
```

`}` `]` `},`

```json
        "TemplateName": "Owner-->DBA-->Admin",
```

```json
        "Enabled": "Y",
        "IsSystem": 1,
        "TemplateId": 6244
```

`}` `]` `}` `}`

#### 6.5.2 ListWorkFlowNodes

Queries the details about approval nodes. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListWorkFlowNod es | The operation that you want to perform. Set the value to List WorkFlowNodes. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| SearchName | String | No | admin | The name that is used to search for approval nodes. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | CFD8FE00-36D9- 4C1B-940D- 65A7B73D9066 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| WorkflowNode s | Array of WorkflowNode |   | The details about approval nodes. |
| WorkflowNode |   |   |   |

| Developer Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AuditUsers | Array of AuditUser |   | The details about approvers. |
| AuditUser |   |   |   |
| NickName | String | test | The name of the approver. |
| RealName | String | test | The real name of the approver. |
| UserId | Long | 123 | The ID of the approver. The ID is different from the ID of the Apsara Stack tenant account of the approver. |
| Comment | String | test | The remarks. |
| CreateUserId | Long | 123 | The ID of the creator. The ID is different from the ID of the Apsara Stack tenant account of the creator. |
| CreateUserNick Name | String | test | The name of the creator. |
| NodeId | Long | 123 | The ID of the node. |
| NodeName | String | test | The name of the node. |
| NodeType | String | SYS | The type of the node. Valid values: SYS: The node is pre-defined by the system. USER LIST: The node is created by a user. _ |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListWorkFlowNodes &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<WorkFlowNodes>
    <WorkflowNode>
        <Comment>This is a system-defined node that is dynamically generated. All requests
are reviewed by an administrator.</Comment>
        <NodeName>Admin</NodeName>
        <NodeType>SYS</NodeType>
        <NodeId>3763</NodeId>
        <AuditUsers>
        </AuditUsers>
    </WorkflowNode>
</WorkFlowNodes> <RequestId>CFD8FE00-36D9-4C1B-940D-65A7B73D9066</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "WorkFlowNodes": {
    "WorkflowNode": [
```

`{`

```json
        "Comment": "This is a system-defined node that is dynamically generated. All reques
ts are reviewed by an administrator.",
        "NodeName": "Admin",
        "NodeType": "SYS",
        "NodeId": 3763,
        "AuditUsers": {
          "AuditUser": []
```

`}` `}` `]` `},`

```json
  "RequestId": "CFD8FE00-36D9-4C1B-940D-65A7B73D9066",
  "Success": true
```

`}`

### 6.6 Metadata of databases and tables

tables

#### 6.6.1 SearchDatabase

Queries the details about databases. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SearchDatabase | The operation that you want to perform. Set the value to SearchDat abase. |
| PageNumber | Integer | Yes | 1 | The number of the page to return. |
| SearchKey | String | Yes | testdb | The keyword that is used to search for databases. |
| Tid | Long | Yes | 1 | The ID of the tenant. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| EnvType | String | No | product | The environment of the database. |
| SearchRange | String | No | HAS PERMSSION _ | The range of databases. Valid values: HAS PERMSSION: databases on _ which the current user has permissions OWNER: databases that are owned by the current user MY FOCUS: databases that are _ followed by the current user UNKNOWN: all databases |
| SearchTarget | String | No | SINGLE DB _ | The category of databases. Valid values: DB: all databases. SINGLE DB: single databases. _ LOGIC DB: logical databases. _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DbType | String | No | MySQL | The type of databases. Valid values: MySQL SQLServer Post greSQL Oracle DRDS OceanBase Mongo Redis |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | E0D21075-CD3E- 4D98-8264- FD8AD04A63B6 | The ID of the request. |
| SearchDatabas eList | Array of SearchDatabas e |   | The details about databases. |
| SearchDatabas e |   |   |   |
| Alias | String | test | The alias of the database. |
| DatabaseId | String | 1 | The ID of the database. |
| DatalinkName | String | datalink name _ | The name of the data link for the database. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DbType | String | mysql | The type of the database. Valid values: MySQL SQLServer Post greSQL Oracle DRDS OceanBase Mongo Redis |
| DbaId | String | 1 | The ID of the database administrator (DBA) for the database. |
| Encoding | String | utf8 | The encoding of the database. |
| EnvType | String | product | The type of the environment to which the database belongs. |
| Host | String | xxx.xxx.xxx.xxx | The endpoint of the instance to which the database belongs. |
| Logic | Boolean | false | Indicates whether the database is a logical database. Valid values: t rue: The database is a logical database. f alse: The database is not a logical database. |
| OwnerIdList | List | 1 | The IDs of the owners of the database. |
| OwnerNameList | List | user1 | The names of the owners of the database. |
| Port | Integer | 3306 | The port number of the instance to which the database belongs. |
| SchemaName | String | test | The name of the database. |
| SearchName | String | test@xxx.xxx.xxx.xxx :3306 | The name that is used to search for the database. |

| Data Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Sid | String | testSid | The system identifier (SID) of the instance to which the database belongs. |
| TotalCount | Long | 1 | The total number of entries that are returned. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SearchDatabase &PageNumber=1 &SearchKey=testdb &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>1</TotalCount> <RequestId>E0D21075-CD3E-4D98-8264-FD8AD04A63B6</RequestId> <SearchDatabaseList>
    <SearchDatabase>
        <Encoding>utf8mb4</Encoding>
        <Host>pc-xxx.mysql.polardb.rds.aliyuncs.com</Host>
        <DbType>polardb</DbType>
        <EnvType>dev</EnvType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>88656</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <Logic>false</Logic>
        <DbaId>88653</DbaId>
        <OwnerNameList>
            <OwnerNames>dmstest</OwnerNames>
            <OwnerNames>xx</OwnerNames>
            <OwnerNames>xx[RAM user]</OwnerNames>
        </OwnerNameList>
        <Port>3306</Port>
        <DatabaseId>117567</DatabaseId>
        <Alias>xx offline database</Alias>
        <SearchName>xxx@pc-xxx.mysql.polardb.rds.aliyuncs.com:3306[xx offline database]</Se
archName>
        <DatalinkName>dblink_38</DatalinkName>
        <SchemaName>xxx_0000</SchemaName>
    </SearchDatabase>
</SearchDatabaseList> <Success>true</Success>
```

`JSON` format `{`

```json
  "TotalCount": 1,
  "RequestId": "E0D21075-CD3E-4D98-8264-FD8AD04A63B6",
  "SearchDatabaseList": {
    "SearchDatabase": [
```

`{`

```json
        "Encoding": "utf8mb4",
        "Host": "pc-xxx.mysql.polardb.rds.aliyuncs.com",
        "DbType": "polardb",
        "EnvType": "dev",
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            88656,
            104442
```

`]` `},`

```json
        "Logic": false,
        "DbaId": 88653,
        "OwnerNameList": {
          "OwnerNames": [
            "dmstest",
            "xx",
            "xx[RAM user]"
```

`]` `},`

```json
        "Port": 3306,
        "DatabaseId": 117567,
        "Alias": "xx offline database",
        "SearchName": "xxx@pc-xxx.mysql.polardb.rds.aliyuncs.com:3306[xx offline database]"
```

`,`

```json
        "DatalinkName": "dblink_38",
        "SchemaName": "xxx_0000"
```

`}` `]` `},`

```json
  "Success": true
```

`}`

#### 6.6.2 SearchTable

Queries the details about tables. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SearchTable | The operation that you want to perform. Set the value to SearchT able. |

| D | eveloper Guide·API | Reference |   |   | Data Managemen | t |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tid | Long | No | 1 | The ID of the tenant. |
| SearchKey | String | No | test | The keyword that is used to search for tables. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| EnvType | String | No | PRODUCT | The type of the environment to which the database belongs. |
| SearchTarget | String | No | LOGIC TABLE _ | The type of tables to be queried. Valid values: T ABLE: all tables SINGLE T ABLE: physical tables _ LOGIC T ABLE: logical tables _ |
| SearchRange | String | No | OWNER | The permission that is required on tables to be queried. Valid values: HAS PERMSSION: tables on which _ the current user has permissions. OWNER: tables that are owned by the current user. MY FOCUS: tables that are _ followed by the current user. UNKNOWN: all tables. |
| DbType | String | No | MySQL | The type of the database. Valid values: MySQL SQLServer Post greSQL Oracle DRDS OceanBase Mongo Redis |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ReturnGuid | Boolean | No | false | Specifies whether to return the globally unique identifier (GUID) of each table. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 1489257F-1B5D- 4B5B-89EF- 923C12CEEBD1 | The ID of the request. |
| SearchTableList | Array of SearchTable |   | The details about the tables. |
| SearchTable |   |   |   |
| DBSearchName | String | test | The name that is used to search for the database to which the table belongs. |
| DatabaseId | String | 1 | The ID of the database to which the table belongs. |
| DbName | String | test | The name of the database. |
| DbType | String | mysql | The type of the database. Valid values: MySQL SQLServer Post greSQL Oracle DRDS OceanBase Mongo Redis |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | test | The description. |
| Encoding | String | utf8 | The encoding of the table. |
| Engine | String | innodb | The engine of the table. |
| EnvType | String | test | The type of the environment. |
| Logic | Boolean | false | Indicates whether the table is a logical table. Valid values: t rue: The table is a logical table. f alse: The table is not a logical table. |
| OwnerIdList | List | 1 | The IDs of the owners of the table. |
| OwnerNameList | List | user | The names of the owners of the table. |
| TableGuid | String | IDB L 9032.db- _ _ test.yuyang test _ | The GUID of the table. |
| TableId | String | 1 | The ID of the table. |
| TableName | String | test table _ | The name of the table. |
| TableSchemaN ame | String | test@xxx.xxx.xxx.xxx :3306 | The name of the database to which the table belongs. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TotalCount | Long | 1 | The total number of entries that are returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SearchTable &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SearchTableList>
    <SearchTable>
        <TableGuid>IDB_L_9032.db-test.yuyang_test</TableGuid>
        <Logic>false</Logic>
        <TableSchemaName>xxx_0000</TableSchemaName>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DBSearchName>xxx_0000@pc-xxx.mysql.polardb.rds.aliyuncs.com:3306[xxx offline datab
ase]</DBSearchName>
        <DatabaseId>117567</DatabaseId>
        <Encoding>utf8mb4</Encoding>
        <TableName>test_aaaa</TableName>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>88656</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <EnvType>dev</EnvType>
        <Engine>InnoDB</Engine>
        <TableId>18396767</TableId>
    </SearchTable>
</SearchTableList> <TotalCount>1</TotalCount> <RequestId>1489257F-1B5D-4B5B-89EF-923C12CEEBD1</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "SearchTableList": {
    "SearchTable": [
```

`{`

```json
        "TableGuid" : "IDB_L_9032.db-test.yuyang_test",
        "Logic": false,
        "TableSchemaName": "xxx_0000",
        "OwnerNameList": {
          "OwnerNames": [
            "xxx",
            "xxx",
            "xxx"
```

`]` `},`

```json
        "DBSearchName": "xxx_0000@pc-xxx.mysql.polardb.rds.aliyuncs.com:3306[xxx offline da
tabase]",
        "DatabaseId": 117567,
        "Encoding": "utf8mb4",
        "TableName": "test_aaaa",
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            88656,
            104442
```

`]` `},`

```json
        "EnvType": "dev",
        "Engine": "InnoDB",
        "TableId": 18396767
```

`}` `]` `},`

```json
  "TotalCount": 1,
  "RequestId": "1489257F-1B5D-4B5B-89EF-923C12CEEBD1",
  "Success": true
```

`}`

#### 6.6.3 ListDatabases

Queries the details of databases in an instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListDatabases | The operation that you want to perform. Set the value to List Dat abases. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceId | String | Yes | 1 | The instance ID. You can obtain the instance ID from the instance information that is returned by the List Inst ances operation. The instance ID is different from the ID of an ApsaraDB RDS instance. |
| PageNumber | Integer | Yes | 1 | The number of the page to return. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DatabaseList | Array of Database |   | The details of databases. |
| Database |   |   |   |
| CatalogName | String | 1 | The name of the database catalog. Not e If the database type is PostgreSQL, the value indicates the name of the PostgreSQL database. |
| DatabaseId | String | 1 | The ID of the database. |
| DbType | String | mysql | The type of the database. |
| DbaId | String | 1 | The ID of the DBA to which the database belongs. |
| DbaName | String | dba user _ | The name of the DBA to which the database belongs. |

| eveloper Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Encoding | String | utf-8 | The encoding of the database. |
| EnvType | String | dev | The type of the environment to which the database belongs. |
| Host | String | xxx.xxx.xxx.xxx | The endpoint of the instance. |
| InstanceId | String | 1 | The ID of the instance to which the database belongs. |
| OwnerIdList | List | 1 | The IDs of database owners. |
| OwnerNameList | List | owner name _ | The names of database owners. |
| Port | Integer | 3306 | The connection port of the instance. |
| SchemaName | String | test | The name of the database. |
| SearchName | String | test@xxx.xxx.xxx.xxx :3306 | The name that is used to search for the database. |
| Sid | String | test | The ID of the instance to which the database belongs. |
| State | String | NORMAL | The status of the database. Valid values: NORMAL: The database is normal. DISABLE: The database is disabled. OFFLINE: The database is unpublished. NOT EXIST: The database does not exist. _ |
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | 5541CDA6-F674- 435C-81BD- 40C2FB926CE3 | The ID of the request. |

| Data Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request succeeds. |
| TotalCount | Long | 1 | The total number of databases that belong to the instance. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListDatabases &InstanceId=1 &PageNumber=1 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>1</TotalCount> <RequestId>5541CDA6-F674-435C-81BD-40C2FB926CE3</RequestId> <Success>true</Success> <DatabaseList>
    <Database>
        <Encoding>utf8</Encoding>
        <Host>pc-xxx.rwlb.rds.aliyuncs.com</Host>
        <InstanceId>24710</InstanceId>
        <DbType>polardb</DbType>
        <EnvType>product</EnvType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
        </OwnerIdList>
        <DbaId>104442</DbaId>
        <OwnerNameList>
            <OwnerNames>dmstest</OwnerNames>
        </OwnerNameList>
        <Port>3306</Port>
        <DatabaseId>116366</DatabaseId>
        <State>NORMAL</State>
        <SearchName>xxx_test@pc-xxx.rwlb.rds.aliyuncs.com:3306【xxx_test】</SearchName>
        <DbaName>xxx[RAM user]</DbaName>
        <SchemaName>xxx_test</SchemaName>
    </Database>
</DatabaseList>
```

`JSON` format `{`

```json
  "TotalCount": 1,
  "RequestId": "5541CDA6-F674-435C-81BD-40C2FB926CE3",
  "Success": true,
  "DatabaseList": {
    "Database": [
```

`{`

```json
        "Encoding": "utf8",
        "Host": "pc-xxx.rwlb.rds.aliyuncs.com",
        "InstanceId": 24710,
        "DbType": "polardb",
        "EnvType": "product",
        "OwnerIdList": {
          "OwnerIds": [
            88653
```

`]` `},`

```json
        "DbaId": 104442,
        "OwnerNameList": {
          "OwnerNames": [
            "dmstest"
```

`]` `},`

```json
        "Port": 3306,
        "DatabaseId": 116366,
        "State": "NORMAL",
        "SearchName": "xxx_test@pc-xxx.rwlb.rds.aliyuncs.com:3306【xxx_test】",
        "DbaName": "xxx[RAM user]",
        "SchemaName": "xxx_test"
```

`}` `]` `}` `}`

#### 6.6.4 ListLogicDatabases

Queries the details about logical databases. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListLogicDatabas es | The operation that you want to perform. Set the value to List LogicDat abases. |
| PageNumber | Integer | Yes | 1 | The number of the page to return. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tid | Long | Yes | -1 | The ID of the tenant. |
| PageSize | Integer | No | 50 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| LogicDatabaseL ist | Array of LogicDatabase |   | The details about logical databases. |
| LogicDatabase |   |   |   |
| DatabaseId | String | 1 | The ID of the logical database. |
| DbType | String | mysql | The type of the logical database. |
| EnvType | String | test | The type of the environment to which the logical database belongs. |
| Logic | Boolean | true | Indicates whether the database is a logical database. The value is set to true. |
| OwnerIdList | List | 1 | The IDs of the owners of the logical database. |
| OwnerNameList | List | owner name _ | The names of the owners of the logical database. |
| SchemaName | String | logic db _ | The name of the logical database. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| SearchName | String | loigc db _ | The name that is used to search for the logical database. |
| RequestId | String | BAD154C0-DA38- 48FA-97AB- E72912EEAA24 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TotalCount | Long | 13 | The total number of logical databases. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListLogicDatabases &PageNumber=1 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>13</TotalCount> <RequestId>BAD154C0-DA38-48FA-97AB-E72912EEAA24</RequestId> <LogicDatabaseList>
    <LogicDatabase>
        <Logic>true</Logic>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DatabaseId>257</DatabaseId>
        <SearchName>test_db(This is a logical database.)</SearchName>
        <DbType>mysql</DbType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
        </OwnerIdList>
        <EnvType>dev</EnvType>
        <SchemaName>test_db</SchemaName>
    </LogicDatabase>
    <LogicDatabase>
        <Logic>true</Logic>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DatabaseId>258</DatabaseId>
        <SearchName>xxx_test(This is a logical database.)</SearchName>
        <DbType>mysql</DbType>
        <OwnerIdList>
            <OwnerIds>88656</OwnerIds>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>101252</OwnerIds>
        </OwnerIdList>
        <EnvType>product</EnvType>
        <SchemaName>idb_test</SchemaName>
    </LogicDatabase>
</LogicDatabaseList> <Success>true</Success>
```

`JSON` format `{`

```json
  "TotalCount": 13,
  "RequestId": "BAD154C0-DA38-48FA-97AB-E72912EEAA24",
  "LogicDatabaseList": {
    "LogicDatabase": [
```

`{`

```json
        "Logic": true,
        "OwnerNameList": {
          "OwnerNames": [
            "xxx"
```

`]` `},`

```json
        "DatabaseId": 257,
        "SearchName": "test_db(This is a logical database)",
        "DbType": "mysql",
        "OwnerIdList": {
          "OwnerIds": [
            88653
```

`]` `},`

```json
        "EnvType": "dev",
        "SchemaName": "test_db"
```

`},` `{`

```json
        "Logic": true,
        "OwnerNameList": {
          "OwnerNames": [
            "xxx",
            "xxx",
            "xxx"
```

`]` `},`

```json
        "DatabaseId": 258,
        "SearchName": "xxx_test(This is a logical database)",
        "DbType": "mysql",
        "OwnerIdList": {
          "OwnerIds": [
            88656,
            88653,
            101252
```

`]` `},`

```json
        "EnvType": "product",
        "SchemaName": "idb_test"
```

`}` `]` `},`

```json
  "Success": true
```

`}`

#### 6.6.5 ListTables

Queries the details of tables in a database. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListTables | The operation that you want to perform. Set the value to List T ables. |
| DatabaseId | String | Yes | 1 | The ID of the database. |
| PageNumber | Integer | Yes | 1 | The number of the page to return. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| SearchName | String | No | test | The keyword that is used to query tables. Prefix match is used. |
| ReturnGuid | Boolean | No | true | Specifies whether to return the GUID of the table. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | B16FB618-5E96- 4FFD-BB0D- 490C890A4030 | The ID of the request. |
| Success | Boolean | true | Indicates whether the call succeeded. |
| TableList | Array of Table |   | The details about the tables. |

| eveloper Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Table |   |   |   |
| DatabaseId | String | 1 | The ID of the database. |
| Description | String | test | The description of the table. |
| Encoding | String | utf8 | The encoding of the table. |
| Engine | String | innodb | The engine of the table. |
| NumRows | Long | 1 | The number of rows in the table. This is a statistical value and does not indicate the actual number of rows. |
| OwnerIdList | List | 1 | The IDs of the table owners. |
| OwnerNameList | List | owner name _ | The nicknames of the table owners. |
| StoreCapacity | Long | 1024 | The storage space that is occupied by the table. This is a statistical value and does not indicate the accurate storage space. |
| TableGuid | String | IDB 308302.yuyang _ _ test.test ch _ | The GUID of the table. |
| TableId | String | 1 | The ID of the table. |
| TableName | String | test | The name of the table. |
| TableSchemaN ame | String | test db _ | The name of the database to which the table belongs. |
| TableType | String | NORMAL | The type of the table. Default value: NORMAL. |
| TotalCount | Long | 12 | The total number of tables that meet the query conditions. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListTables &DatabaseId=1 &PageNumber=1 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TableList>
    <Table>
        <TableSchemaName>yuyang_test</TableSchemaName>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DatabaseId>116367</DatabaseId>
        <Encoding>utf8mb4</Encoding>
        <NumRows>3</NumRows>
        <StoreCapacity>1</StoreCapacity>
        <TableName>base_user</TableName>
        <TableGuid>IDB_18396363.yuyang_test.base_user</TableGuid>
        <TableType>NORMAL</TableType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <Engine>InnoDB</Engine>
        <TableId>18396363</TableId>
    </Table>
    <Table>
        <TableSchemaName>yuyang_test</TableSchemaName>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <DatabaseId>116367</DatabaseId>
        <Encoding>utf8mb4</Encoding>
        <NumRows>2</NumRows>
        <StoreCapacity>1</StoreCapacity>
        <TableName>biz_orders</TableName>
        <TableType>NORMAL</TableType>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <Engine>InnoDB</Engine>
        <TableId>18390459</TableId>
    </Table>
</TableList> <TotalCount>12</TotalCount> <RequestId>B16FB618-5E96-4FFD-BB0D-490C890A4030</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "TableList": {
    "Table": [
```

`{`

```json
        "TableSchemaName": "yuyang_test",
        "OwnerNameList": {
```

```json
          "OwnerNames": [
            "xxx",
            "xxx"
```

`]` `},`

```json
        "DatabaseId": 116367,
        "Encoding": "utf8mb4",
        "NumRows": 3,
        "StoreCapacity": 1,
        "TableName": "base_user",
        "TableGuid": "IDB_18396363.yuyang_test.base_user",
        "TableType": "NORMAL",
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            104442
```

`]` `},`

```json
        "Engine": "InnoDB",
        "TableId": 18396363
```

`},` `{`

```json
        "TableSchemaName": "yuyang_test",
        "OwnerNameList": {
          "OwnerNames": [
            "xxx",
            "xxx"
```

`]` `},`

```json
        "DatabaseId": 116367,
        "Encoding": "utf8mb4",
        "NumRows": 2,
        "StoreCapacity": 1,
        "TableName": "biz_orders",
        "TableType": "NORMAL",
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            104442
```

`]` `},`

```json
        "Engine": "InnoDB",
        "TableId": 18390459
```

`}` `]` `},`

```json
  "TotalCount": 12,
  "RequestId": "B16FB618-5E96-4FFD-BB0D-490C890A4030",
  "Success": true
```

`}`

#### 6.6.6 ListLogicTables

Queries the details of logical tables in a logical database. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListLogicTables | The operation that you want to perform. Set the value to List LogicT ables. |
| DatabaseId | String | Yes | 1 | The ID of the logical database. |
| PageNumber | Integer | Yes | 1 | The number of the page to return. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| SearchName | String | No | test | The keyword that is used to query logical tables. Prefix match is used. |
| ReturnGuid | Boolean | No | true | Specifies whether to return the GUID of the table. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| LogicTableList | Array of LogicTable |   | The details of logical tables. |
| LogicTable |   |   |   |
| DatabaseId | String | 1 | The ID of the logical database. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Logic | Boolean | true | Indicates whether the table is a logical table. Default value: true. |
| OwnerIdList | List | 1 | The IDs of owners for the logical table. |
| OwnerNameList | List | owner name _ | The nicknames of owners for the logical table. |
| SchemaName | String | yuyang test _ | The logical database to which the logical table belongs. |
| TableCount | String | 4 | The number of subtables. |
| TableExpr | String | test[1-4] | The expression of the logical table. |
| TableGuid | String | IDB L 308302.yuyan _ _ g test.test ch _ _ | The GUID of the logical table. |
| TableId | String | 1 | The ID of the logical table. |
| TableName | String | test | The name of the logical table. |
| RequestId | String | F1E6484F-9DF1- 4406-9BDE- 0861C4629B69 | The ID of the request. |
| Success | Boolean | true | Indicates whether the call succeeded. |
| TotalCount | Long | 1 | The total number of logical tables that meet the query conditions. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListLogicTables &DatabaseId=1 &PageNumber=1 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>1</TotalCount> <RequestId>F1E6484F-9DF1-4406-9BDE-0861C4629B69</RequestId> <LogicTableList>
    <LogicTable>
        <Logic>true</Logic>
        <OwnerNameList>
            <OwnerNames>xxx</OwnerNames>
            <OwnerNames>xxx</OwnerNames>
        </OwnerNameList>
        <TableExpr>t[1-4]</TableExpr>
        <DatabaseId>267</DatabaseId>
        <SchemaName>yuyang_test</SchemaName>
        <TableName>t</TableName>
        <TableGuid>IDB_L_3057.yuyang_test.t</TableGuid>
        <TableCount>4</TableCount>
        <OwnerIdList>
            <OwnerIds>88653</OwnerIds>
            <OwnerIds>104442</OwnerIds>
        </OwnerIdList>
        <TableId>3057</TableId>
    </LogicTable>
</LogicTableList> <Success>true</Success>
```

`JSON` format `{`

```json
  "TotalCount": 1,
  "RequestId": "F1E6484F-9DF1-4406-9BDE-0861C4629B69",
  "LogicTableList": {
    "LogicTable": [
```

`{`

```json
        "Logic": true,
        "OwnerNameList": {
          "OwnerNames": [
            "xxx",
            "xxx"
```

`]` `},`

```json
        "TableExpr": "t[1-4]",
        "DatabaseId": 267,
        "SchemaName": "yuyang_test",
        "TableName": "t",
        "TableGuid": "IDB_L_3057.yuyang_test.t",
        "TableCount": 4,
        "OwnerIdList": {
          "OwnerIds": [
            88653,
            104442
```

`]` `},`

```json
        "TableId": 3057
```

`}` `]` `},`

```json
  "Success": true
```

`}`

#### 6.6.7 ListColumns

Queries the details about columns in a table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListColumns | The operation that you want to perform. Set the value to List Columns. |
| Logic | Boolean | Yes | false | Specifies whether the table is a logical table. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TableId | String | Yes | 1 | The ID of the table. |
| Tid | Long | Yes | 0 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ColumnList | Array of Column |   | The details about columns. |
| Column |   |   |   |
| AutoIncrement | Boolean | false | Indicates whether the column is an auto- increment column. Valid values: true: The column is an auto-increment column. false: The column is not an auto- increment column. |
| ColumnId | String | 1 | The ID of the column. |
| ColumnName | String | name | The name of the column. |
| ColumnType | String | varchar | The type of the column. |
| DataLength | Long | 32 | The length of the column. |
| DataPrecision | Integer | 0 | The precision of the column. |
| DataScale | Integer | 0 | The scale of the column. |
| DefaultValue | String | def value _ | The default value of the column. |
| Description | String | test | The description of the column. |

| Data Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| FunctionType | String | default | The type of the masking algorithm that is used for the column. Valid values: null: No masking algorithm is used. DEFAULT: A full masking algorithm is used. FIX POS: The fixed position is masked. _ FIX CHAR: The fixed characters are _ replaced. |
| Nullable | Boolean | true | Indicates whether the column can be null. |
| SecurityLevel | String | INNER | The security level of the field. Valid values: INNER SENSITIVE CONFIDENTIAL |
| Sensitive | Boolean | false | Indicates whether the field is a sensitive field. |
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 0AD9AC55-5873- 474A-9F33- 4285806A3619 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListColumns &Logic=false &TableId=1 &Tid=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ColumnList>
    <Column>
        <ColumnId>314036829</ColumnId>
        <DataScale>0</DataScale>
        <Sensitive>false</Sensitive>
        <Description>Primary key ID</Description>
        <DataPrecision>20</DataPrecision>
        <ColumnType>bigint(20) unsigned</ColumnType>
        <ColumnName>id</ColumnName>
        <SecurityLevel>INNER</SecurityLevel>
        <AutoIncrement>true</AutoIncrement>
        <Nullable>false</Nullable>
    </Column>
    <Column>
        <ColumnId>314036830</ColumnId>
        <Sensitive>false</Sensitive>
        <Description>Creation time</Description>
        <DefaultValue>CURRENT_TIMESTAMP</DefaultValue>
        <ColumnType>datetime</ColumnType>
        <ColumnName>gmt_create</ColumnName>
        <SecurityLevel>INNER</SecurityLevel>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>false</Nullable>
    </Column>
    <Column>
        <ColumnId>314036831</ColumnId>
        <Sensitive>false</Sensitive>
        <Description>Modification time</Description>
        <DefaultValue>CURRENT_TIMESTAMP</DefaultValue>
        <ColumnType>datetime</ColumnType>
        <ColumnName>gmt_modified</ColumnName>
        <SecurityLevel>INNER</SecurityLevel>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>false</Nullable>
    </Column>
    <Column>
        <ColumnId>314036832</ColumnId>
        <Sensitive>false</Sensitive>
        <Description>base_user</Description>
        <ColumnType>varchar(64)</ColumnType>
        <DataLength>64</DataLength>
        <ColumnName>user_name</ColumnName>
        <SecurityLevel>INNER</SecurityLevel>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>true</Nullable>
    </Column>
</ColumnList> <RequestId>0AD9AC55-5873-474A-9F33-4285806A3619</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "ColumnList": {
    "Column": [
```

`{`

```json
        "ColumnId": 314036829,
        "DataScale": 0,
        "Sensitive": false,
        "Description": "Primary key ID",
        "DataPrecision": 20,
        "ColumnType": "bigint(20) unsigned",
        "ColumnName": "id",
        "SecurityLevel": "INNER",
        "AutoIncrement": true,
        "Nullable": false
```

`},` `{`

```json
        "ColumnId": 314036830,
        "Sensitive": false,
        "Description": "Creation time",
        "DefaultValue": "CURRENT_TIMESTAMP",
        "ColumnType": "datetime",
        "ColumnName": "gmt_create",
        "SecurityLevel": "INNER",
        "AutoIncrement": false,
        "Nullable": false
```

`},` `{`

```json
        "ColumnId": 314036831,
        "Sensitive": false,
        "Description": "Modification time",
        "DefaultValue": "CURRENT_TIMESTAMP",
        "ColumnType": "datetime",
        "ColumnName": "gmt_modified",
        "SecurityLevel": "INNER",
        "AutoIncrement": false,
        "Nullable": false
```

`},` `{`

```json
        "ColumnId": 314036832,
        "Sensitive": false,
        "Description": "base_user",
        "ColumnType": "varchar(64)",
        "DataLength": 64,
        "ColumnName": "user_name",
        "SecurityLevel": "INNER",
        "AutoIncrement": false,
        "Nullable": true
```

`}` `]` `},`

```json
  "RequestId": "0AD9AC55-5873-474A-9F33-4285806A3619",
  "Success": true
```

`}`

#### 6.6.8 ListIndexes

Queries the details of indexes for a table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListIndexes | The operation that you want to perform. Set the value to List Indexes. |
| Logic | Boolean | Yes | false | Specifies whether the table is a logical table. |
| TableId | String | Yes | 1 | The ID of the table. |
| Tid | Long | Yes | 0 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| IndexList | Array of Index |   | The details of indexes. |
| Index |   |   |   |
| IndexComment | String | test | The description of each index. |
| IndexId | String | 1 | The ID of the index. |
| IndexName | String | idx test _ | The name of the index. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IndexType | String | Primary | The type of the index. Valid values: Primary Unique Normal FullText Spatial |
| TableId | String | 1 | The ID of the table. |
| RequestId | String | 1F4DE2F1-5B47- 462A-A973- E02EB7AF386B | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeds. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListIndexes &Logic=false &TableId=1 &Tid=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>1F4DE2F1-5B47-462A-A973-E02EB7AF386B</RequestId> <IndexList>
    <Index>
        <IndexComment/>
        <IndexType>Primary</IndexType>
        <IndexName>PRIMARY</IndexName>
        <IndexId>49331416</IndexId>
        <TableId>18396274</TableId>
    </Index>
</IndexList> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "1F4DE2F1-5B47-462A-A973-E02EB7AF386B",
  "IndexList": {
    "Index": [
```

`{`

```json
        "IndexComment": "",
        "IndexType": "Primary",
        "IndexName": "PRIMARY",
        "IndexId": 49331416,
        "TableId": 18396274
```

`}` `]` `},`

```json
  "Success": true
```

`}`

#### 6.6.9 GetDatabase

Queries the details about a database. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetDatabase | The operation that you want to perform. Set the value to Get Dat abase. |
| Host | String | Yes | xxx.xxx.xxx.xxx | The endpoint of the instance. |
| Port | Integer | Yes | 3306 | The port that is used to connect to the instance. |
| SchemaName | String | Yes | test db _ | The name of the database. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Sid | String | No | test sid _ | The system identifier (SID) of the instance. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Database | Struct |   | The details about the database. |
| CatalogName | String | def | The name of the database catalog. Not e If the database type is PostgreSQL, the value indicates the name of the PostgreSQL database. |
| DatabaseId | String | 1 | The ID of the database. |
| DbType | String | mysql | The type of the database. |
| DbaId | String | 1 | The ID of the database administrator (DBA). |
| DbaName | String | dba name _ | The name of the DBA. |
| Encoding | String | utf8mb4 | The encoding of the database. |
| EnvType | String | test | The type of the environment to which the database belongs. |
| Host | String | xxx.xxx.xxx.xxx | The endpoint of the instance. |
| InstanceId | String | 1 | The ID of the instance. |
| OwnerIdList | List | 1 | The IDs of the owners of the database. |
| OwnerNameList | List | test | The names of the owners of the database. |
| Port | Integer | 3306 | The number of the port that is used to connect to the instance. |
| SchemaName | String | test db _ | The name of the schema. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| SearchName | String | test db@xxx.xxx.xxx _ .xxx:3306 | The name that is used to search for the database. |
| Sid | String | test sid _ | The system identifier (SID) of the instance. |
| State | String | NORMAL | The status of the database. For more information about the valid values, see the List Dat abases operation. |
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 3CDB8601-AD74- 4A47-8114- 08E08CD6319D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetDatabase &Host=xxx.xxx.xxx.xxx &Port=3306 &SchemaName=test_db &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Database>
    <Encoding>utf8mb4</Encoding>
    <Host>pc-xxx.rwlb.rds.aliyuncs.com</Host>
    <InstanceId>24710</InstanceId>
    <DbType>polardb</DbType>
    <OwnerIdList>
        <OwnerIds>88653</OwnerIds>
        <OwnerIds>104442</OwnerIds>
    </OwnerIdList>
    <EnvType>product</EnvType>
    <DbaId>104442</DbaId>
    <OwnerNameList>
        <OwnerNames>xxx</OwnerNames>
        <OwnerNames>xxx[RAM user]</OwnerNames>
    </OwnerNameList>
    <Port>3306</Port>
    <DatabaseId>116367</DatabaseId>
    <State>NORMAL</State>
    <SearchName>xxx_test@pc-xxx.rwlb.rds.aliyuncs.com:3306[xxx_test]</SearchName>
    <DbaName>xxx[RAM user]</DbaName>
    <SchemaName>xxx_test</SchemaName>
</Database> <RequestId>3CDB8601-AD74-4A47-8114-08E08CD6319D</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "Database": {
    "Encoding": "utf8mb4",
    "Host": "pc-xxx.rwlb.rds.aliyuncs.com",
    "InstanceId": 24710,
    "DbType": "polardb",
    "OwnerIdList": {
      "OwnerIds": [
        88653,
        104442
```

`]` `},`

```json
    "EnvType": "product",
    "DbaId": 104442,
    "OwnerNameList": {
      "OwnerNames": [
        "xxx",
        "xxx[RAM user]"
```

`]` `},`

```json
    "Port": 3306,
    "DatabaseId": 116367,
    "State": "NORMAL",
    "SearchName": <SearchName>xxx_test@pc-xxx.rwlb.rds.aliyuncs.com:3306[xxx_test]</SearchN
ame>
    "DbaName": "xxx[RAM user]"
    "SchemaName": "xxx_test"
```

`},`

```json
  "RequestId": "3CDB8601-AD74-4A47-8114-08E08CD6319D",
  "Success": true
```

`}`

#### 6.6.10 GetLogicDatabase

Queries the details about a logical database. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetLogicDatabas e | The operation that you want to perform. Set the value to Get LogicDat abase. |
| DbId | String | Yes | 1 | The ID of the logical database. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tid | Long | Yes | 0 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| LogicDatabase | Struct |   | The details about the logical database. |
| DatabaseId | String | 1 | The ID of the logical database. |
| DbType | String | mysql | The type of the database. |
| EnvType | String | dev | The type of the environment to which the database belongs. |
| Logic | Boolean | true | Indicates whether the database is a logical database. The value is fixed to true. |
| OwnerIdList | List | 1 | The IDs of the owners of the database. |
| OwnerNameList | List | owner name _ | The names of the owners of the database. |
| SchemaName | String | test logic db _ _ | The name of the logical database. |
| SearchName | String | test logic db[xxx] _ _ | The name that is used to search for the logical database. |
| RequestId | String | 90260530-565C- 42B9-A6E8- 893481FE6AB6 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetLogicDatabase &DbId=1 &Tid=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<LogicDatabase>
    <Logic>true</Logic>
    <OwnerNameList>
        <OwnerNames>xxx</OwnerNames>
        <OwnerNames>xxx</OwnerNames>
        <OwnerNames>xxx</OwnerNames>
    </OwnerNameList>
    <DatabaseId>265</DatabaseId>
    <SearchName>test_logic_db(xxx)</SearchName>
    <DbType>mysql</DbType>
    <OwnerIdList>
        <OwnerIds>88653</OwnerIds>
        <OwnerIds>97787</OwnerIds>
        <OwnerIds>88654</OwnerIds>
    </OwnerIdList>
    <EnvType>dev</EnvType>
    <SchemaName>test_logic_db</SchemaName>
</LogicDatabase> <RequestId>90260530-565C-42B9-A6E8-893481FE6AB6</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "LogicDatabase": {
    "Logic": true,
    "OwnerNameList": {
      "OwnerNames": [
        "xxx",
        "xxx",
        "xxx"
```

`]` `},`

```json
    "DatabaseId": 265,
    "SearchName": "test_logic_db(xxx)",
    "DbType": "mysql",
    "OwnerIdList": {
      "OwnerIds": [
        88653,
        97787,
        88654
```

`]` `},`

```json
    "EnvType": "dev",
    "SchemaName": "test_logic_db"
```

`},`

```json
  "RequestId": "90260530-565C-42B9-A6E8-893481FE6AB6",
  "Success": true
```

`}`

#### 6.6.11 GetMetaTableDetailInfo

Queries the details of a table. These details include columns and indexes. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetMetaTableDet ailInfo | The operation that you want to perform. Set the value to Get Met aT ableDet ailInf o. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TableGuid | String | Yes | IDB L 9032.db- _ _ test.yuyang test _ | The globally unique identifier (GUID) of the table in DMS. Not e To obtain the GUID of a logical database, set the Ret urnGuid parameter to t rue when you call the List LogicT ables operation. To obtain the GUID of a logical database, set the Ret urnGuid parameter to t rue when you call the List T ables operation. |
| Tid | Long | No | 123 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DetailInfo | Struct |   | The details of the table. |
| ColumnList | Array of Column |   | The columns. |
| AutoIncrement | Boolean | true | Indicates whether the column is an auto- increment column. Valid values: true: The column is an auto-increment column. false: The column is not an auto- increment column. |
| ColumnId | String | 191234849 | The ID of the column. |
| ColumnName | String | id | The name of the column. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ColumnType | String | bigint(20) unsigned | The data type of the column. Example: Bigint ,Int , or Varchar. |
| DataLength | Integer | 0 | The length of the column. |
| DataPrecision | Integer | 0 | The precision of the column. |
| DataScale | Integer | 0 | The scale of the column. |
| Description | String | test | The description of the column. |
| Nullable | Boolean | false | Indicates whether the column is nullable. Valid values: true: The column is nullable. false: The column is not nullable. |
| Position | String | 1 | The position of the column in the table. |
| IndexList | Array of Index |   | The indexes. |
| IndexColumns | List | id,name | The indexed columns. |
| IndexId | String | 123 | The ID of the index. |
| IndexName | String | PRIMARY | The name of the index. |
| IndexType | String | Primary | The type of the index. Example: Primary, Unique, or Normal. |
| Unique | Boolean | false | Indicates whether the index is unique. Valid values: true: The index is unique. false: The index is not unique. |
| ErrorCode | String | UnknownError | The error code that is returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | E881CB2F-DE42- 42E5-90EB- 8B3173DCB9B9 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeds. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetMetaTableDetailInfo &TableGuid=IDB_L_9032.db-test.yuyang_test &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>E881CB2F-DE42-42E5-90EB-8B3173DCB9B9</RequestId> <DetailInfo>
    <ColumnList>
        <ColumnId>191234849</ColumnId>
        <ColumnName>id</ColumnName>
        <Description>test</Description>
        <ColumnType>bigint(20) unsigned</ColumnType>
        <Position>1</Position>
        <AutoIncrement>true</AutoIncrement>
        <DataScale>0</DataScale>
        <DataPrecision>20</DataPrecision>
        <Nullable>false</Nullable>
    </ColumnList>
    <ColumnList>
        <ColumnId>191234850</ColumnId>
        <ColumnName>gmt_create</ColumnName>
        <Description>test</Description>
        <ColumnType>datetime</ColumnType>
        <Position>2</Position>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>false</Nullable>
    </ColumnList>
    <ColumnList>
        <ColumnId>191234851</ColumnId>
        <ColumnName>gmt_modified</ColumnName>
        <Description>test</Description>
        <ColumnType>datetime</ColumnType>
        <Position>3</Position>
        <AutoIncrement>false</AutoIncrement>
        <Nullable>false</Nullable>
    </ColumnList>
    <IndexList>
        <IndexName>PRIMARY</IndexName>
        <IndexId>33008763</IndexId>
        <IndexColumns>id</IndexColumns>
        <Unique>false</Unique>
        <IndexType>Primary</IndexType>
    </IndexList>
</DetailInfo> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "E881CB2F-DE42-42E5-90EB-8B3173DCB9B9",
  "DetailInfo": {
    "ColumnList": [
```

`{`

```json
        "ColumnId": 191234849,
        "ColumnName": "id",
        "Description": "test",
        "ColumnType": "bigint(20) unsigned",
        "Position": 1,
        "AutoIncrement": true,
        "DataScale": 0,
        "DataPrecision": 20,
        "Nullable": false
```

`},` `{`

```json
        "ColumnId": 191234850,
        "ColumnName": "gmt_create",
        "Description": "test",
        "ColumnType": "datetime",
        "Position": 2,
        "AutoIncrement": false,
        "Nullable": false
```

`},` `{`

```json
        "ColumnId": 191234851,
        "ColumnName": "gmt_modified",
        "Description": "test",
        "ColumnType": "datetime",
        "Position": 3,
        "AutoIncrement": false,
        "Nullable": false
```

`}` `],`

```json
    "IndexList": [
```

`{`

```json
        "IndexName": "PRIMARY",
        "IndexId": 33008763,
        "IndexColumns": [
          "id"
```

`],`

```json
        "Unique": false,
        "IndexType": "Primary"
```

`}` `]` `},`

```json
  "Success": true
```

`}`

#### 6.6.12 GetTableDBTopology

Queries the topology of a table. This operation is available only for logical databases. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetTableDBTopol ogy | The operation that you want to perform. Set the value to Get T ableDBT opology. |
| TableGuid | String | Yes | IDB L 9032.db- _ _ test.yuyang test _ | The globally unique identifier (GUID) of a table in Data Management (DMS). Not e To obtain the GUID of a table in a logical database, set the Ret urnGuid parameter to t rue when you call the List LogicT ables operation. To obtain the GUID of a table in a physical database, set the Ret urnGuid parameter to t rue when you call the List T ables operation. |
| Tid | Long | No | 123 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The ID of the region where Data Management (DMS) resides. Not e Set this parameter to the ID of the region that is in proximity to your applications. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBTopology | Struct |   | The topology information about the database. |
| DataSourceList | Array of DataSource |   | The data sources. |

| eveloper Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|
| Parameter | Type | Example | Description |
| DatabaseList | Array of Database |   | The physical databases. |
| DbId | String | 489347 | The ID of the database. |
| DbName | String | db-test | The name of the database. |
| DbType | String | mysql | The type of the database. |
| EnvType | String | pre | The type of the environment. Valid values: product: production environment dev: development environment pre: staging environment test: test environment sit: SIT environment uat: UAT environment pet: stress testing environment stag: STAG environment |
| TableList | Array of Table |   | The physical tables. |
| TableId | String | 151977812 | The ID of the table. |
| TableName | String | yuyang test 0000 _ _ | The name of the table. |
| TableType | String | NORMAL | The type of the table. This is a reserved parameter. |
| DbType | String | mysql | The type of the database. |
| Host | String | xxx.mysql.polardb.r ds.aliyuncs.com | The endpoint of the data source. |
| Port | Integer | 3306 | The port that is used to connect to the data source. |
| Sid | String | def | The system identifier (SID) of the data source. |

| Data Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TableGuid | String | IDB L 9032.db- _ _ test.yuyang test _ | The GUID of the table in DMS. |
| TableName | String | yuyang test _ | The name of the table. Not e If a logical table is queried, the name of the logical table is returned. If a physical table is queried, the name of the physical table is returned. |
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 853F7FD4-D922- 4EFB-931C- D253EF159E06 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetTableDBTopology &TableGuid=IDB_L_9032.db-test.yuyang_test &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>55B7CF50-4610-4707-B2B2-5EF2BE000367</RequestId> <DBTopology>
    <TableName>yuyang_test</TableName>
    <TableGuid>IDB_L_9032.db-test.yuyang_test</TableGuid>
    <DataSourceList>
        <DatabaseList>
            <DbId>489347</DbId>
            <DbName>db-test</DbName>
            <TableList>
                <TableId>151977811</TableId>
                <TableName>yuyang_test_0000</TableName>
            </TableList>
            <TableList>
                <TableId>151977812</TableId>
                <TableName>yuyang_test_0001</TableName>
            </TableList>
            <TableList>
                <TableId>151977813</TableId>
                <TableName>yuyang_test_0002</TableName>
            </TableList>
            <TableList>
                <TableId>151977814</TableId>
                <TableName>yuyang_test_0003</TableName>
            </TableList>
            <TableList>
                <TableId>151977815</TableId>
                <TableName>yuyang_test_0004</TableName>
            </TableList>
            <EnvType>dev</EnvType>
            <DbType>polardb</DbType>
        </DatabaseList>
        <Port>3306</Port>
        <Host>xxx.mysql.polardb.rds.aliyuncs.com</Host>
        <DbType>polardb</DbType>
    </DataSourceList>
</DBTopology> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "55B7CF50-4610-4707-B2B2-5EF2BE000367",
  "DBTopology": {
    "TableName": "yuyang_test",
    "TableGuid": "IDB_L_9032.db-test.yuyang_test",
    "DataSourceList": [
```

`{`

```json
        "DatabaseList": [
```

`{`

```json
            "DbId": 489347,
            "DbName": "db-test",
            "TableList": [
```

`{`

```json
                "TableId": 151977811,
                "TableName": "yuyang_test_0000"
```

`},` `{`

```json
                "TableId": 151977812,
                "TableName": "yuyang_test_0001"
```

`},` `{`

```json
                "TableId": 151977813,
                "TableName": "yuyang_test_0002"
```

`},` `{`

```json
                "TableId": 151977814,
                "TableName": "yuyang_test_0003"
```

`},` `{`

```json
                "TableId": 151977815,
                "TableName": "yuyang_test_0004"
```

`}` `],`

```json
            "EnvType": "dev",
            "DbType": "polardb"
```

`}` `],`

```json
        "Port": 3306,
        "Host": "xxx.mysql.polardb.rds.aliyuncs.com",
        "DbType": "polardb"
```

`}` `]` `},`

```json
  "Success": true
```

`}`

#### 6.6.13 GetMetaTableColumn

Queries the details about columns in a table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetMetaTableCol umn | The operation that you want to perform. Set the value to Get Met aT ableColumn. |
| TableGuid | String | Yes | IDB L 11345.yuya _ _ ng test.base use _ _ r | The globally unique identifier (GUID) of a table in Data Management (DMS). Not e To obtain the GUID of a table in a logical database, set the Ret urnGuid parameter to t rue when you call the List LogicT ables operation. To obtain the GUID of a table in a physical database, set the Ret urnGuid parameter to t rue when you call the List T ables operation. |
| Tid | Long | No | 123 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ColumnList | Array of Column |   | The columns. |
| AutoIncrement | Boolean | true | Indicates whether the column is an auto- increment column. Valid values: t rue: The column is an auto-increment column. f alse: The column is not an auto- increment column. |
| ColumnId | String | 191234849 | The ID of the column. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ColumnName | String | id | The name of the column. |
| ColumnType | String | bigint(20) unsigned | The data type of the column. Examples: Bigint , Int , and Varchar. |
| DataLength | Integer | 0 | The length of the column. |
| DataPrecision | Integer | 0 | The precision of data in the column. |
| DataScale | Integer | 0 | The scale of data in the column. |
| Description | String | test | The description of the column. |
| Nullable | Boolean | false | Indicates whether the column is empty. Valid values: t rue: The column is empty. f alse: The column is not empty. |
| Position | Integer | 1 | The order of the column in the table. |
| PrimaryKey | String | true | Indicates whether the column is the primary key. t rue: The column is the primary key. f alse: The column is not the primary key. |
| SecurityLevel | String | INNER | The sensitivity level of the column. Valid values: INNER SENSIT IVE CONFIDENT IAL |
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 2B581A5E-D4FE- 4F77-BADE- DD944D7BEBE2 | The ID of the request. |

|   | Developer Guide·AP | I Reference |   | Data Managemen | t |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetMetaTableColumn &TableGuid=IDB_L_11345.yuyang_test.base_user &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetMetaTableColumnResponse>
      <RequestId>2B581A5E-D4FE-4F77-BADE-DD944D7BEBE2</RequestId>
      <ErrorCode>UnknownError</ErrorCode>
      <ColumnList>
            <ColumnId>191234849</ColumnId>
            <ColumnName>id</ColumnName>
            <Description>test</Description>
            <ColumnType>bigint(20) unsigned</ColumnType>
            <Position>1</Position>
            <AutoIncrement>true</AutoIncrement>
            <SecurityLevel>INNER</SecurityLevel>
            <DataScale>0</DataScale>
            <DataLength>0</DataLength>
            <DataPrecision>0</DataPrecision>
            <PrimaryKey>true</PrimaryKey>
            <Nullable>false</Nullable>
      </ColumnList>
      <ErrorMessage>UnknownError</ErrorMessage>
      <Success>true</Success>
</GetMetaTableColumnResponse>
```

`JSON` format `{`

```json
 "RequestId": "2B581A5E-D4FE-4F77-BADE-DD944D7BEBE2",
 "ErrorCode": "UnknownError",
 "ColumnList": [{
  "ColumnId": "191234849",
  "ColumnName": "id",
  "Description": "test",
  "ColumnType": "bigint(20) unsigned",
  "Position": "1",
  "AutoIncrement": "true",
  "SecurityLevel": "INNER",
  "DataScale": "0",
  "DataLength": "0",
  "DataPrecision": "0",
  "PrimaryKey": "true",
  "Nullable": "false"
 }],
 "ErrorMessage": "UnknownError",
 "Success": "true"
```

`}`

#### 6.6.14 SyncDatabaseMeta

Synchronizes the metadata of a database dictionary. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SyncDatabaseMet a | The operation that you want to perform. Set the value to SyncDat abaseMet a. |
| DbId | String | Yes | 123 | The ID of the database. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Logic | Boolean | No | false | Specifies whether the database is a logical database. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SyncDatabaseMeta &DbId=123 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
```

`}`

#### 6.6.15 SyncInstanceMeta

Synchronizes the metadata of all database dictionaries in an instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SyncInstanceMeta | The operation that you want to perform. Set the value to SyncInst anceMet a. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceId | String | Yes | 1234 | The ID of the instance. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| IgnoreTable | Boolean | No | true | Specifies whether to skip synchronization for the metadata of table dictionaries. Valid values: true false |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SyncInstanceMeta &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
```

`}`

### 6.7 Ticket operations

#### 6.7.1 General

##### 6.7.1.1 ApproveOrder

Reviews a ticket. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ApproveOrder | The operation that you want to perform. Set the value to ApproveOrder. |
| ApprovalType | String | Yes | agree | The action that you want to perform on the ticket. Valid values: AGREE CANCEL REJECT |
| Tid | Long | Yes | -1 | The ID of the tenant. Not e To view the ID of the tenant, perform the following steps: Log on to the Data Management (DMS) console. Move the pointer over the profile picture in the upper-right corner of the page. |
| WorkflowInstanc eId | Long | Yes | 1234 | The ID of the approval process. You can call the Get OrderBaseInf o operation to obtain the ID. The ID is available only for a ticket that is pending approval. The value of this parameter is an integer that is greater than zero. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region ID. |
| Comment | String | No | test | The remarks. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ApproveOrder &ApprovalType=agree &Tid=-1 &WorkflowInstanceId=1234 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D",
  "Success": true
```

`}`

##### 6.7.1.2 CloseOrder

Closes a ticket. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CloseOrder | The operation that you want to perform. Set the value to CloseOrder. |
| CloseReason | String | Yes | close reason | The reason why the ticket is closed. |
| OrderId | Long | Yes | 1343 | The ID of the ticket. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the call succeeds. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CloseOrder &CloseReason=close reason &OrderId=1343 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D",
  "Success": true
```

`}`

##### 6.7.1.3 GetApprovalDetail

Queries the approval details of a ticket. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetApprovalDetai l | The operation that you want to perform. Set the value to Get ApprovalDet ail. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| WorkflowInstanc eId | Long | Yes | 12345 | The ID of the approval process. You can call the Get OrderBaseInf o operation to obtain the ID. The ID is available only for a ticket that is pending approval. The value of this parameter is an integer that is greater than zero. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ApprovalDetail | Struct |   | The details of the approval process. |
| AuditId | Long | 277 | The ID of the approval process. |
| CurrentHandler s | Array of CurrentHandler |   | The information of the reviewer. |

| eveloper Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentHandler |   |   |   |
| Id | Long | 1 | The ID of the user. |
| NickName | String | nickName | The name of the user. |
| Description | String | test | The description of the approval process. |
| OrderId | Long | 1234 | The ID of the ticket. |
| OrderType | String | DATA EXPORT _ | The type of the ticket. |
| ReasonList | List | ["reason1"] | The reason for the review result. |
| Title | String | Data export ticket- 1234 | The title of the approval process. |
| WorkflowInsCo de | String | APPROVED | The status code of the approval process. |
| WorkflowNode s | Array of WorkflowNode |   | The details of approval nodes. |
| WorkflowNode |   |   |   |
| AuditUserIdList | List | 104442 | The IDs of reviewers. |
| NodeName | String | DBA | The name of the approval node. |
| OperateComme nt | String | Reason: approved | The remarks of the review. |
| OperateTime | String | 2019-10-15 13:47:54 | The time when the ticket was reviewed. |
| OperatorId | Long | 13434 | The ID of the reviewer. |
| WorkflowInsCo de | String | APPROVED | The status code of the approval process. |
| ErrorCode | String | UnknownError | The returned error code. |

| Data Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetApprovalDetail &Tid=-1 &WorkflowInstanceId=12345 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ApprovalDetail>
    <Description>xxx</Description>
    <WorkflowInsCode>APPROVED</WorkflowInsCode>
    <CurrentHandlers>
    </CurrentHandlers>
    <OrderId>737047</OrderId>
    <OrderType>DATA_EXPORT</OrderType>
    <ReasonList>
        <Reasons>xxx</Reasons>
    </ReasonList>
    <AuditId>277</AuditId>
    <Title>Data export ticket-737047</Title>
    <WorkflowNodes>
        <WorkflowNode>
            <OperatorId>104442</OperatorId>
            <WorkflowInsCode>APPROVED</WorkflowInsCode>
            <OperateComment>Reason: approved</OperateComment>
            <AuditUserIdList>
                <AuditUserIds>104442</AuditUserIds>
            </AuditUserIdList>
            <OperateTime>2019-10-15 13:47:54</OperateTime>
            <NodeName>DBA</NodeName>
        </WorkflowNode>
    </WorkflowNodes>
</ApprovalDetail> <RequestId>FE8EE2F1-4880-46BC-A704-5CF63EAF9A04</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "ApprovalDetail": {
    "Description": "xxx",
    "WorkflowInsCode": "APPROVED",
    "CurrentHandlers": {
      "CurrentHandler": []
```

`},`

```json
    "OrderId": 737047,
    "OrderType": "DATA_EXPORT",
    "ReasonList": {
      "Reasons": [
        "xxx"
```

`]` `},`

```json
    "AuditId": 277,
    "Title": "Data export ticket-737047",
    "WorkflowNodes": {
      "WorkflowNode": [
```

`{`

```json
          "OperatorId": 104442,
          "WorkflowInsCode": "APPROVED",
          "OperateComment": "Reason: approved",
          "AuditUserIdList": {
            "AuditUserIds": [
              104442
```

`]` `},`

```json
          "OperateTime": "2019-10-15 13:47:54",
          "NodeName": "DBA"
```

`}` `]` `}` `},`

```json
  "RequestId": "FE8EE2F1-4880-46BC-A704-5CF63EAF9A04",
  "Success": true
```

`}`

##### 6.7.1.4 GetOrderBaseInfo

Queries the basic information about a ticket. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetOrderBaseInfo | The operation that you want to perform. Set the value to Get OrderBaseInf o. |

| ata Management |   |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| OrderId | Long | Yes | 12345 | The ID of the ticket. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| OrderBaseInfo | Struct |   | The basic information about the ticket. |
| Comment | String | test | The remarks. |
| Committer | String | xxx | The applicant. |
| CommitterId | Long | 1 | The ID of the applicant. Note: The ID is different from the Apsara Stack tenant account ID of the applicant. |
| CreateTime | String | 2019-10-10 00:00:00 | The time when the ticket was created. |
| LastModifyTim e | String | 2019-10-10 00:00:00 | The last time when the ticket was modified. |
| OrderId | Long | 12345 | The ID of the ticket. |
| PluginType | String | DC COMMON _ | The type of the ticket. For more information, see the "Request parameters" section of the Creat eOrder topic. |
| RelatedUserList | List | 1,2,3 | The IDs of the operators that are related to the ticket. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RelatedUserNic kList | List | a,b,c | The names of the operators that are related to the ticket. |
| StatusCode | String | success | The status code of the ticket. Valid values: new: The ticket is created. toaudit: The ticket is being reviewed. Approved: The ticket is approved. reject: The ticket is rejected. processing: The request to create the ticket is being processed. success: The request to create the ticket is processed. closed: The ticket is closed. |
| StatusDesc | String | success | The description of the status. |
| WorkflowInstan ceId | Long | 1 | The ID of the approval process. |
| WorkflowStatu sDesc | String | approved | The description of the approval process. |
| RequestId | String | 7133DF67-5B25- 460F-8285- C4CC93472C2F | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetOrderBaseInfo &OrderId=12345 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<OrderBaseInfo>
    <Comment>test</Comment>
    <CreateTime>2019-10-10 00:00:00</CreateTime>
    <LastModifyTime>2019-10-10 00:00:00</LastModifyTime>
    <OrderId>12345</OrderId>
    <CommitterId>1</CommitterId>
    <PluginType>DC_COMMON</PluginType>
    <StatusCode>success</StatusCode>
    <RelatedUserNickList>
        <UserNicks>a,b,c</UserNicks>
    </RelatedUserNickList>
    <StatusDesc>success</StatusDesc>
    <WorkflowStatusDesc>approved</WorkflowStatusDesc>
    <WorkflowInstanceId>1</WorkflowInstanceId>
    <Committer>xxx</Committer>
    <RelatedUserList>
        <UserIds>1,2,3</UserIds>
    </RelatedUserList>
</OrderBaseInfo> <RequestId>7133DF67-5B25-460F-8285-C4CC93472C2F</RequestId> <ErrorCode>UnknownError</ErrorCode> <ErrorMessage>UnknownError</ErrorMessage> <Success>true</Success>
```

`JSON` format

```json
{"OrderBaseInfo":{"Comment":"test","CreateTime":"2019-10-10 00:00:00","LastModifyTime":"201 9-10-10 00:00:00","OrderId":"12345","CommitterId":"1","PluginType":"DC_COMMON","StatusCode" :"success","RelatedUserNickList":{"UserNicks":"a,b,c"},"StatusDesc":"success","WorkflowStat usDesc":"approved","WorkflowInstanceId":"1","Committer":"xxx","RelatedUserList":{"UserIds": "1,2,3"}},"RequestId":"7133DF67-5B25-460F-8285-C4CC93472C2F","ErrorCode":"UnknownError","Er rorMessage":"UnknownError","Success":"true"}
```

##### 6.7.1.5 ListOrders

Queries the details of tickets. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListOrders | The operation that you want to perform. Set the value to List Orders. |
| Tid | Long | No | -1 | The ID of the tenant. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PluginType | String | No | DC COMMON _ | The type of tickets. Valid values: PERM APPLY: the tickets that are _ used to apply for permissions. OWNER APPLY: the tickets that are _ used to assume the ownership of resources. DATA CORRECT: the tickets that are _ used to change data. NDDL: the tickets that are used to change the schema design of databases. DATA TRACK: the tickets that are _ used to trace data. TABLE SYNC: the tickets that are _ used to synchronize databases or tables. DATA EXPORT: the tickets that are _ used to export data. SENSITIVITY: the tickets that are used to change the level of sensitive columns. |
| OrderResultType | String | No | AS ADMIN _ | The range of tickets to be queried. Valid values: AS ADMIN: all tickets. _ AS COMMITTER: the tickets that are _ submitted by the current user. AS HANDLER: the tickets to be _ processed by the current user. AS OWNER: the tickets that are _ processed by the current user. AS Related: the tickets that are _ related to the current user. |
| SearchDateType | String | No | CREATE TIME _ | The time condition. Valid values: CREATE TIME: the time when tickets _ are created. MODIFY TIME: the time when tickets _ are modified. |
| StartTime | String | No | 2019-10-10 00:00:00 | The start of the time range. |
| EndTime | String | No | 2019-10-10 00:00:00 | The end of the time range. |

| D | ata Management |   |   |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SearchContent | String | No | test | The keyword that is used to search for tickets. |
| OrderStatus | String | No | ALL | The status of tickets. Valid values: ALL: The tickets of all statuses are included. FINISHED: The tickets are completed. RUNNING: The tickets are being processed. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| Orders | Array of Order |   | The details about the tickets. |
| Order |   |   |   |
| Comment | String | test | The remarks of the ticket. |
| Committer | String | test | The user who submitted the ticket. |
| CommitterId | Long | 1 | The ID of the user who submitted the ticket. |
| CreateTime | String | 2019-10-10 00:00:00 | The time when the ticket was created. |
| LastModifyTim e | String | 2019-10-10 00:00:00 | The last time when the ticket was modified. |

| Developer Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | Long | 1432 | The ID of the ticket. |
| PluginType | String | DC COMMON _ | The type of the ticket. |
| StatusCode | String | success | The status of the ticket. |
| StatusDesc | String | success | The status description of the ticket. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TotalCount | Long | 100 | The total number of entries that are returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListOrders &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>5</TotalCount> <RequestId>7AC17A86-9E6F-484B-AE8D-F9416986A108</RequestId> <Orders>
    <Order>
        <StatusCode>success</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[RAM user]</Committer>
        <StatusDesc>Data is changed.</StatusDesc>
        <LastModifyTime>2019-11-19 13:53:05</LastModifyTime>
        <CreateTime>2019-11-19 13:52:36</CreateTime>
        <OrderId>737160</OrderId>
        <Comment>A test ticket that is used to change data</Comment>
        <CommitterId>104442</CommitterId>
    </Order>
    <Order>
        <StatusCode>new</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[RAM user]</Committer>
<Stt
```

`D`

```
>Th tikti
```

`t` `b`

```
bittdf l</Stt
```

`D` `>`

```xml
        <StatusDesc>The ticket is to be submitted for approval.</StatusDesc>
        <LastModifyTime>2019-10-29 20:51:37</LastModifyTime>
        <CreateTime>2019-10-29 20:51:36</CreateTime>
        <OrderId>737116</OrderId>
        <Comment>Create a test ticket to change data</Comment>
        <CommitterId>104442</CommitterId>
    </Order>
    <Order>
        <StatusCode>closed</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[RAM user]</Committer>
        <StatusDesc>The ticket is closed: Database-level operations are not supported.</Sta
tusDesc>
        <LastModifyTime>2019-10-20 22:09:38</LastModifyTime>
        <CreateTime>2019-10-20 22:08:19</CreateTime>
        <OrderId>737089</OrderId>
        <Comment>The test ticket that is used to create a database</Comment>
        <CommitterId>104442</CommitterId>
    </Order>
    <Order>
        <StatusCode>new</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[RAM user]</Committer>
        <StatusDesc>Failed to perform the pre-check.</StatusDesc>
        <LastModifyTime>2019-09-30 16:58:35</LastModifyTime>
        <CreateTime>2019-09-30 16:58:34</CreateTime>
        <OrderId>737016</OrderId>
        <Comment>Test</Comment>
        <CommitterId>104442</CommitterId>
    </Order>
    <Order>
        <StatusCode>success</StatusCode>
        <PluginType>DC_COMMON</PluginType>
        <Committer>xxx[RAM user]</Committer>
        <StatusDesc>Data is changed.</StatusDesc>
        <LastModifyTime>2019-08-17 14:07:54</LastModifyTime>
        <CreateTime>2019-08-17 14:07:42</CreateTime>
        <OrderId>736774</OrderId>
        <Comment>The ticket that is used to change common data</Comment>
        <CommitterId>104442</CommitterId>
    </Order>
</Orders> <Success>true</Success>
```

`JSON` format `{`

```json
  "TotalCount": 5,
  "RequestId": "7AC17A86-9E6F-484B-AE8D-F9416986A108",
  "Orders": {
    "Order": [
```

`{`

```json
        "StatusCode": "success",
        "PluginType": "DC_COMMON",
```

```json
        "Committer": "xxx[RAM user]"
        "StatusDesc": "Data is changed.",
        "LastModifyTime": "2019-11-19 13:53:05",
        "CreateTime": "2019-11-19 13:52:36",
        "OrderId": 737160,
        "Comment": "The test ticket that is used to change data",
        "CommitterId": 104442
```

`},` `{`

```json
        "StatusCode": "new",
        "PluginType": "DC_COMMON",
        "Committer": "xxx[RAM user]"
        "StatusDesc": "The ticket is to be submitted for approval.",
        "LastModifyTime": "2019-10-29 20:51:37",
        "CreateTime": "2019-10-29 20:51:36",
        "OrderId": 737116,
        "Comment": "Create a test ticket to change data",
        "CommitterId": 104442
```

`},` `{`

```json
        "StatusCode": "closed",
        "PluginType": "DC_COMMON",
        "Committer": "xxx[RAM user]"
        "StatusDesc": "The ticket is closed: Database-level operations are not supported.",
        "LastModifyTime": "2019-10-20 22:09:38",
        "CreateTime": "2019-10-20 22:08:19",
        "OrderId": 737089,
        "Comment": "A test ticket that is used to create a database",
        "CommitterId": 104442
```

`},` `{`

```json
        "StatusCode": "new",
        "PluginType": "DC_COMMON",
        "Committer": "xxx[RAM user]"
        "StatusDesc": "Failed to perform the pre-check.",
        "LastModifyTime": "2019-09-30 16:58:35",
        "CreateTime": "2019-09-30 16:58:34",
        "OrderId": 737016,
        "Comment": "Test",
        "CommitterId": 104442
```

`},` `{`

```json
        "StatusCode": "success",
        "PluginType": "DC_COMMON",
        "Committer": "xxx[RAM user]"
        "StatusDesc": "Data is changed.",
        "LastModifyTime": "2019-08-17 14:07:54",
        "CreateTime": "2019-08-17 14:07:42",
        "OrderId": 736774,
        "Comment": "The ticket that is used to change common data",
        "CommitterId": 104442
```

`}` `]` `},`

```json
  "Success": true
```

`}`

##### 6.7.1.6 SubmitOrderApproval

Submits a ticket for approval. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SubmitOrderAppr oval | The operation that you want to perform. Set the value to Submit OrderApproval. |
| OrderId | Long | Yes | 12345 | The ID of the ticket. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SubmitOrderApproval &OrderId=12345 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7AC17A86-9E6F-484B-AE8D-F9416986A108</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "7AC17A86-9E6F-484B-AE8D-F9416986A108",
  "Success": true
```

`}`

##### 6.7.1.7 CreateOrder

Creates a ticket. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateOrder | The operation that you want to perform. Set the value to Creat eOrder. |
| Comment | String | Yes | test | The description of the ticket. |
| PluginParam | Json | Yes | {} | The parameter that is used to create a ticket. This parameter consists of a set of parameters that are included in a JSON string. The settings of these parameters are subject to the type of the ticket. For more information, see the "Instructions for the PluginParam parameter" section. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PluginType | String | Yes | DATA EXPORT _ | The type of the ticket. Valid values: DC COMMON: a ticket that is used to _ change common data. DC CHUNK: a ticket that is used to _ change lock-free data. DC CRON CLEAR: a ticket that is _ _ used to change historical data. NDDL: a ticket that is used to change the schema design. DATA EXPORT: a ticket that is used _ to export data. PERM APPLY: a ticket that is used to _ request a permission. OWNER APPLY: a ticket that is used _ to request the ownership of a resource. |
| RelatedUserList | String | Yes | 1,2,3 | The IDs of the operators that are related to the ticket. Separate multiple IDs with commas (,). |
| Tid | Long | No | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Instructions for the PluginParam parameter

```json
json
# Change common data
"pluginParam" : {
    "classify" : "Test", // The classification of the reason.
    "estimateAffectRows" : 1, // The estimated number of affected rows.
    "execSql" : "update base_op_log set id=1 where id=1;", // The SQL statement to be execu
ted.
    "dbItemList" : [ { // The details of databases on which the operation is performed.
      "dbId" : 179694,
      "logic" : false
    } ],
    "rbSQL" : "update base_op_log set id=1 where id=1;", // The SQL statement to run for ro
llback.
    "rbAttachmentName" : null, // The attachment of the SQL statement to run for rollback.
    "sqlType" : "TEXT", // The type of the SQL file to run for data change. Valid values: T
EXT and ATTACHMENT.
    "rbSQLType" : "TEXT", // The type of the SQL file to run for rollback. Valid values: TE
XT and ATTACHMENT.
    "attachmentName" : // The attachment of the SQL statement to run for data change.
```

`}`

```json
# Change lock-free data
"pluginParam" : {
    "Classify":"Test"
    "execSQL" : "update base_op_log set op_type=op_type where 1=1;", // The SQL statement t
o be executed.
    "dbItemList" : [ {
      "dbId": 179719, // The ID of the database from which data is exported.
      "logic" : false
    } ]
```

`}`

```json
# Clear historical data
"pluginParam" : {
    "duration" : 10, // The duration. Unit: hours. Default value: 0.
    "specifyDuration" : true, // Specifies whether to set a duration. Valid values: true (y
es) and false (no). Default value: false.
    "Classify":"Test"
    "cronFormat" : "0 1 21 * * ?", // The expression that is used to schedule the execution
of the operation.
    "execSql" : null,
    "dbItemList" : [ {
      "dbId": 179719, // The ID of the database on which the operation is performed.
      "logic" : false
    } ],
    "cronClearItemList" : [ {
      "filterSQL" : null, // The filter conditions.
      "columnName" : "gmt_create", // The time field.
      "remainDays" : 60, // The retention period.
      "tableName" : "base_app" // The table name.
    } ]
```

`}`

```json
json
# Change the schema design
"pluginParam": {
    "title": "test", // The title.
    "description": "test", // The description.
    "dbId": 118989, // The ID of the required database.
    "logic": false, // Specifies whether the database is a logical database.
    "relatedIds": [], // The IDs of operators that are related to the change.
```

`}`

```json
json
# Export data
"pluginParam" : {
  "classify": "Classification of the reason", // The classification of the reason.
  "dbId": 179719, // The ID of the database from which data is exported.
  "exeSQL": "select 1", // Export data by using the SQL statement.
  "logic": false, // Specifies whether the database is a logical database.
  "ignoreAffectRows": false, // Specifies whether to ignore the affected rows.
  "affectRows": 1, // The estimated number of affected rows.
  "ignoreAffectRowsReason": "" // Specifies whether to ignore the affected rows.
```

`}` Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateOrderRes ult | List | 123 | The ID of the ticket that is created. |
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the call succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateOrder &Comment=test &PluginParam={} &PluginType=DATA_EXPORT &RelatedUserList=1,2,3 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D</RequestId> <CreateOrderResult>
    <OrderIds>123</OrderIds>
</CreateOrderResult> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "427688B8-ADFB-4C4E-9D45-EF5C1FD6E23D",
  "CreateOrderResult": {
    "OrderIds": [123]
```

`},`

```json
  "Success": true
```

`}`

#### 6.7.2 Data changes

##### 6.7.2.1 ExecuteDataCorrect

Creates a ticket to modify data. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ExecuteDataCorre ct | The operation that you want to perform. Set the value to Execut eDat aCorrect . |
| OrderId | Long | Yes | 123 | The ID of the ticket. |
| Tid | String | No | -1 | The ID of the tenant. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ActionDetail | Json | No | { "startTime" : null, "endTime" : null, "transaction" : false, "backupData" : true } | The parameters that are required to perform the operation. json "actionDetail" : { "startTime" : null, // The start of the required time range. If you want to immediately modify data , you do not need to set the parameter. "endTime" : null, // The end of the required time range. If you want to immediately modify data , you do not need to set the parameter. "transaction" : false, // Specifies whether to run the modification task as a transaction. "backupData" : true // Specifies whether to back up data. } |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ExecuteDataCorrect &OrderId=123 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7133DF67-5B25-460F-8285-C4CC93472C2F</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "7133DF67-5B25-460F-8285-C4CC93472C2F",
  "Success": true
```

`}`

##### 6.7.2.2 GetDataCorrectBackupFiles

Queries the download URL of an attachment that includes the backup files of data changes. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetDataCorrectBa ckupFiles | The operation that you want to perform. Set the value to Get Dat aCorrect BackupFiles. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| OrderId | Long | Yes | 12345 | The ID of the ticket. |
| Tid | Long | No | -1 | The ID of the tenant. |
| ActionDetail | Json | No | {} | The parameters that are required to perform the operation. You do not need to specify this parameter. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataCorrectBac kupFiles | List | xxx | The download URL of the attachment that includes backup files. |
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetDataCorrectBackupFiles &OrderId=12345 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DataCorrectBackupFiles>
    <FileUrl>https://xxx.oss-cn-hangzhou.aliyuncs.com/xxx.zip?Expires=1574382979&amp;OSSAcc
essKeyId=wSa97B52GzF4fGqu&amp;Signature=ykWSysajKcQjXjG0X4ApOQvlIXQ%3D</FileUrl> </DataCorrectBackupFiles> <RequestId>4AFF4109-FEFB-44E8-96A3-923B1FA8C46E</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "DataCorrectBackupFiles": {
    "FileUrl": [
      "https://xxx.oss-cn-hangzhou.aliyuncs.com/xxx.zip?Expires=1574382979&OSSAccessKeyId=w
Sa97B52GzF4fGqu&Signature=ykWSysajKcQjXjG0X4ApOQvlIXQ%3D"
```

`]` `},`

```json
  "RequestId": "4AFF4109-FEFB-44E8-96A3-923B1FA8C46E",
  "Success": true
```

`}`

##### 6.7.2.3 GetDataCorrectOrderDetail

Queries the details about a ticket that is used to modify data. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetDataCorrectOr derDetail | The operation that you want to perform. Set the value to Get Dat aCorrect OrderDet ail. |
| OrderId | Long | Yes | 12345 | The ID of the ticket. |
| Tid | Long | No | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataCorrectOrd erDetail | Struct |   | The details about the ticket. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DatabaseList | Array of Database |   | The details about the database whose data is modified. |
| Database |   |   |   |
| DbId | Integer | 123456 | The ID of the database. |
| DbType | String | mysql | The type of the database. |
| EnvType | String | product | The type of the environment to which the database belongs. |
| Logic | Boolean | false | Indicates whether the database is a logical database. |
| SearchName | String | xxx@xxx:3306 | The name that is used to search for the logical database. |
| OrderDetail | Struct |   | The details about the ticket. |
| ActualAffectRo ws | Long | 100 | The number of rows that are affected by the system check. |
| AttachmentNa me | String | xxx | The attachment that includes the executed SQL statement. |
| Classify | String | test | The category of the reason for the data change. |
| EstimateAffect Rows | Long | 100 | The estimated number of affected rows. |
| ExeSQL | String | update t1 set name = 'xxx' where id <= 100 | The SQL statement that is executed. |
| IgnoreAffectRo ws | Boolean | false | Indicates whether the pre-check is ignored. |
| IgnoreAffectRo wsReason | String | test | The reason why the pre-check is ignored. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RbAttachment Name | String | test | The attachment that includes the SQL statement used to roll back the updated data. |
| RbSQL | String | empty | The SQL statement that is specified to roll back the updated data. |
| RbSQLType | String | text | The type of the attachment file. Valid values: TEXT ATTACHMENT |
| SqlType | String | text | The type of the SQL statement. Valid values: TEXT ATTACHMENT |
| PreCheckDetail | Array of TaskCheckDO |   | The details about the precheck task. |
| TaskCheckDO |   |   |   |
| CheckStatus | String | SUCCESS | The status of the precheck task. Valid values: WAITING: The ticket is pending check. RUNNING: The ticket is being checked. SUCCESS: The ticket is checked. FAIL: The ticket fails to be checked. |
| CheckStep | String | PERMISSION CHECK _ | The check step. Valid values: SQL PARSE: The system parses the SQL _ statement. SQL TYPE CHECK: The system checks the _ _ type of the SQL statement. PERMISSION CHECK: The system checks the _ permissions of the SQL statement. ROW CHECK: The system checks the _ number of rows. |
| UserTip | String | tip messsage | The message that appears when a check step is executed. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetDataCorrectOrderDetail &OrderId=12345 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>ACE263E5-CF5F-44DD-A7B1-42C5E78E9650</RequestId> <DataCorrectOrderDetail>
    <PreCheckDetail>
        <TaskCheckDO>
            <CheckStatus>SUCCESS</CheckStatus>
            <CheckStep>SQL_PARSE</CheckStep>
        </TaskCheckDO>
        <TaskCheckDO>
            <CheckStatus>SUCCESS</CheckStatus>
            <CheckStep>SQL_TYPE_CHECK</CheckStep>
        </TaskCheckDO>
        <TaskCheckDO>
            <CheckStatus>SUCCESS</CheckStatus>
            <CheckStep>PERMISSION_CHECK</CheckStep>
        </TaskCheckDO>
        <TaskCheckDO>
            <CheckStatus>SUCCESS</CheckStatus>
            <UserTip>This is a statistical value that is generated by the system. The actua
l number of affected rows is subject to the SQL statement that is executed.</UserTip>
            <CheckStep>ROW_CHECK</CheckStep>
        </TaskCheckDO>
    </PreCheckDetail>
    <OrderDetail>
        <ActualAffectRows>0</ActualAffectRows>
        <RbSQLType>TEXT</RbSQLType>
        <ExeSQL>update base_user set id = 1 where id = 1;</ExeSQL>
        <EstimateAffectRows>1</EstimateAffectRows>
        <SqlType>TEXT</SqlType>
        <Classify>test</Classify>
        <IgnoreAffectRowsReason/>
    </OrderDetail>
</DataCorrectOrderDetail> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "ACE263E5-CF5F-44DD-A7B1-42C5E78E9650",
  "DataCorrectOrderDetail": {
    "PreCheckDetail": {
      "TaskCheckDO": [
```

`{`

```json
          "CheckStatus": "SUCCESS",
          "CheckStep": "SQL_PARSE"
```

`},` `{`

```json
          "CheckStatus": "SUCCESS",
          "CheckStep": "SQL_TYPE_CHECK"
```

`},` `{`

```json
          "CheckStatus": "SUCCESS",
          "CheckStep": "PERMISSION_CHECK"
```

`},` `{`

```json
          "CheckStatus": "SUCCESS",
          "UserTip": "This is a statistical value that is generated by the system. The actu
al number of affected rows is subject to the SQL statement that is executed.",
          "CheckStep": "ROW_CHECK"
```

`}` `]` `},`

```json
    "OrderDetail": {
      "ActualAffectRows": 0,
      "RbSQLType": "TEXT",
      "ExeSQL": "update base_user set id = 1 where id = 1;",
      "EstimateAffectRows": 1,
      "SqlType": "TEXT",
      "Classify": "test",
      "IgnoreAffectRowsReason": ""
```

`}` `},`

```json
  "Success": true
```

`}`

#### 6.7.3 Schema design

##### 6.7.3.1 CreatePublishGroupTask

Creates a ticket to modify the schema design of a database. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreatePublishGro upTask | The operation that you want to perform. Set the value to Creat ePublishGroupT ask. |
| DbId | Integer | Yes | 12345 | The ID of the database for which you want to modify the schema design. |
| Logic | Boolean | Yes | false | Specifies whether the database is a logical database. |
| OrderId | Long | Yes | 142435 | The ID of the ticket. |
| PublishStrategy | String | Yes | IMMEDIATELY | The policy to modify the schema design. Valid values: IMMEDIATELY: immediately modifies the schema design. REGULARLY: modifies the schema design at a scheduled time. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| PlanTime | String | No | 2019-10-10 00:00:00 | The time to modify the schema design. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TaskId | Long | 413452 | The ID of the task. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreatePublishGroupTask &DbId=12345 &Logic=false &OrderId=142435 &PublishStrategy=IMMEDIATELY &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>78C93646-D9B1-4E6E-B5FD-C69F94A7905A</RequestId> <Success>true</Success> <TaskId>13424</TaskId>
```

`JSON` format `{`

```json
  "RequestId": "78C93646-D9B1-4E6E-B5FD-C69F94A7905A",
  "Success": true,
  "TaskId": 13424
```

`}`

#### 6.7.4 Data export

##### 6.7.4.1 ExecuteDataExport

Executes a ticket to export data. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ExecuteDataExpo rt | The operation that you want to perform. Set the value to Execut eDat aExport . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ActionDetail | Json | Yes | { "fileType": "CSV", "encoding": "" } | The parameters that are required to perform the operation: json { "fileType": "CSV", // The format of the file to which the data is exported. "encoding": "" // The encoding of the file. } |
| OrderId | Long | Yes | 1234 | The ID of the ticket. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | FE8EE2F1-4880- 46BC-A704- 5CF63EAF9A04 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?ActionDetail={ "fileType": "CSV", "encoding": "" } &OrderId=1234 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>FE8EE2F1-4880-46BC-A704-5CF63EAF9A04</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "FE8EE2F1-4880-46BC-A704-5CF63EAF9A04",
  "Success": true
```

`}`

##### 6.7.4.2 GetDataExportDownloadURL

Queries the download URL of the file that includes export results for a data export ticket. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetDataExportDo wnloadURL | The operation that you want to perform. Set the value to Get Dat aExport DownloadURL. |
| OrderId | Long | Yes | 12345 | The ID of the ticket. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DownloadURLR esult | Struct |   | The details about the file that includes export results. |
| HasResult | Boolean | true | Indicates whether a file is available for download. |
| TipMessage | String | tip message | The message that indicates an exception. |
| URL | String | xxx | The download URL of the file that includes export results. |

| Developer Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|
| Parameter | Type | Example | Description |

| ErrorCode | String | UnknownError | The error code that is returned. |
|---|---|---|---|
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetDataExportDownloadURL &OrderId=12345 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DownloadURLResult>
    <URL>https://dms-idb-hangzhou.oss-cn-hangzhou.aliyuncs.com/xxx.zip?Expires=1574384313&a
mp;OSSAccessKeyId=wSa97B52GzF4fGqu&amp;Signature=HQQWBRSKiVV6cupugh1/eAVSqXg%3D</URL>
    <HasResult>true</HasResult>
</DownloadURLResult> <RequestId>4BF24EA5-9013-4C85-AE68-6C23AF5E0097</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "DownloadURLResult": {
    "URL": "https://dms-idb-hangzhou.oss-cn-hangzhou.aliyuncs.com/xxx.zip?Expires=157438431
3&OSSAccessKeyId=wSa97B52GzF4fGqu&Signature=HQQWBRSKiVV6cupugh1/eAVSqXg%3D",
    "HasResult": true
```

`},`

```json
  "RequestId": "4BF24EA5-9013-4C85-AE68-6C23AF5E0097",
  "Success": true
```

`}`

##### 6.7.4.3 GetDataExportOrderDetail

Queries the details about a ticket that is used to export data. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetDataExportOr derDetail | The operation that you want to perform. Set the value to Get Dat aExport OrderDet ail. |
| OrderId | Long | Yes | 123456 | The ID of the ticket. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| DataExportOrd erDetail | Struct |   | The details about the ticket. |
| KeyInfo | Struct |   | The status information. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| JobStatus | String | EXPORT SUCCESS _ | The status of the ticket. Valid values: PRE CHECKING: The ticket is being pre- _ checked. PRE CHECK SUCCESS: The ticket is pre- _ _ checked. PRE CHECK FAIL: The ticket fails to be pre- _ _ checked. WAITING APPLY AUDIT: The ticket is being _ _ submitted for approval. APPLY AUDIT SUCESS: The ticket is _ _ submitted for approval. ENABLE EXPORT: The ticket is approved. _ Data can be exported. WAITING EXPORT: The data is pending _ export. DOING EXPORT: The data is being _ exported. EXPORT FAIL: The data fails to be _ exported. EXPORT SUCCESS: The data is exported. _ |
| PreCheckId | Long | 123 | The ID of the precheck task. |
| OrderDetail | Struct |   | The details about the ticket. |
| ActualAffectRo ws | Long | 1 | The number of rows that are affected by the system check. |
| Classify | String | text | The category of the reason for the data export. |
| Database | String | xxx@xxx:3306 | The database from which data is exported. |
| DbId | Integer | 123 | The ID of the database. |
| EnvType | String | test | The type of the environment to which the database belongs. |
| ExeSQL | String | select 1 | The SQL statement that is executed to export data. |

| Data Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| IgnoreAffectRo ws | Boolean | false | Indicates whether the affected rows are skipped. |
| IgnoreAffectRo wsReason | String | empty | The reason why the pre-check is skipped. |
| Logic | Boolean | false | Indicates whether the database is a logical database. |
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 427688B8-ADFB- 4C4E-9D45- EF5C1FD6E23D | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GetDataExportOrderDetail &OrderId=123456 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DataExportOrderDetail>
    <KeyInfo>
        <PreCheckId>15544</PreCheckId>
        <JobStatus>EXPORT_SUCCESS</JobStatus>
    </KeyInfo>
    <OrderDetail>
        <Logic>false</Logic>
        <ActualAffectRows>1</ActualAffectRows>
        <ExeSQL>select 1;</ExeSQL>
        <Database>yuyang_test@xxx:3306[yuyang_test_xxx]China (Hangzhou) non-modular databas
e</Database>
        <IgnoreAffectRows>false</IgnoreAffectRows>
        <DbId>116367</DbId>
        <Classify>Test</Classify>
        <EnvType>product</EnvType>
    </OrderDetail>
</DataExportOrderDetail> <RequestId>78C93646-D9B1-4E6E-B5FD-C69F94A7905A</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "DataExportOrderDetail": {
    "KeyInfo": {
      "PreCheckId": 15544,
      "JobStatus": "EXPORT_SUCCESS"
```

`},`

```json
    "OrderDetail": {
      "Logic": false,
      "ActualAffectRows": 1,
      "ExeSQL": "select 1;",
      "Database": <Database>yuyang_test@xxx:3306[yuyang_test_xxx]China (Hangzhou) non-modul
ar database</Database>
      "IgnoreAffectRows": false,
      "DbId": 116367,
      "Classify": "Test",
      "EnvType": "product"
```

`}` `},`

```json
  "RequestId": "78C93646-D9B1-4E6E-B5FD-C69F94A7905A",
  "Success": true
```

`}`

### 6.8 Permission management

#### 6.8.1 RevokeUserPermission

Revokes the permissions on a specified resource from a user. Request parameters q p

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RevokeUserPermi ssion | The operation that you want to perform. Set the value to RevokeUserPermission. |
| DbId | String | Yes | 142345 | The ID of the database. |
| DsType | String | Yes | DATABASE | The type of resources. For more information, see the description of the Grant UserPermission operation. |
| PermTypes | String | Yes | QUERY | The type of permissions. For more information, see the description of the Grant UserPermission operation. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| UserAccessId | String | Yes | 123 | The ID of the user permission. |
| UserId | String | Yes | 1234 | The ID of the user. You can call the Get User operation to obtain the ID. Not e The ID is different from the ID of the Apsara Stack tenant account of the user. |
| Logic | Boolean | No | false | Specifies whether the database is a logical database. Valid values: true false |
| TableId | String | No | 1342345 | The ID of the table. This parameter is required if you grant permissions on a table to a user. |
| TableName | String | No | table name _ | The name of the table. This parameter is required if you grant permissions on a table to a user. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RevokeUserPermission &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
```

`}`

#### 6.8.2 ListDatabaseUserPermssions

Queries the permissions of users on a database. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListDatabaseUser Permssions | The operation that you want to perform. Set the value to List Dat abaseUserPermssions. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DbId | String | Yes | 123 | The ID of the database. |
| PermType | String | Yes | DATABASE | The type of the permission. Valid values: DATABASE: permissions on databases. TABLE: permissions on tables. COLUMN: permissions on columns. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| Logic | Boolean | No | false | Specifies whether the database is a logical database. |
| UserName | String | No | search user nam _ _ e | The nickname of the user. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | 68075D06-7406- 4887-83A7- F558A4D28C13 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeds. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 1 | The total number of entries that meet the query conditions. |
| UserPermission s | Array of UserPermission |   | The details of user permissions. |
| UserPermission |   |   |   |
| Alias | String | instance alias _ | The alias of the instance. |
| ColumnName | String | column name _ | The name of the field. |
| DbId | String | 1234 | The ID of the database. |
| DbType | String | mysql | The type of the database. |
| DsType | String | DATABASE | The type of resources on which the user has permissions. |
| EnvType | String | product | The type of the environment to which the database belongs. |
| InstanceId | String | 1443 | The ID of the instance. |
| Logic | Boolean | false | Specifies whether the database is a logical database. |
| PermDetails | Array of PermDetail |   | The details of permissions. |
| PermDetail |   |   |   |
| CreateDate | String | 2019-12-12 00:00:00 | The time when the permission was created. |
| ExpireDate | String | 2020-12-12 00:00:00 | The time when the permission expires. |
| ExtraData | String | DEFAULT | The extra information. This parameter is reserved. |
| OriginFrom | String | xxx grant | The entity that authorizes the permission. |

| Data Management |   |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |

| PermType | String | QUERY | The type of the permission. Valid values: QUERY: the query permission. EXPORT: the export permission. CORRECT: the change permission. |
|---|---|---|---|
| UserAccessId | String | 13434 | The ID of the authorization record. |
| SchemaName | String | xxx@xxxx:3306 | The name of the schema. |
| SearchName | String | xxx | The name that is used to search for the database. |
| TableId | String | 42345 | The ID of the table. |
| TableName | String | table name _ | The name of the table. |
| UserId | String | 14324 | The ID of the user. |
| UserNickName | String | user nick name _ _ | The name of the user. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListDatabaseUserPermssions &DbId=123 &PermType=DATABASE &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UserPermissions>
    <UserPermission>
        <Logic>false</Logic>
        <UserNickName>xxx</UserNickName>
        <DsType>DATABASE</DsType>
        <Alias>beihe_ent_prod</Alias>
        <PermDetails>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390915</UserAccessId>
                <PermType>QUERY</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390916</UserAccessId>
                <PermType>EXPORT</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390917</UserAccessId>
                <PermType>CORRECT</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
        </PermDetails>
        <InstanceId>1434</InstanceId>
        <SearchName>xxx@xxxx:3306</SearchName>
        <DbId>123434</DbId>
        <UserId>432423</UserId>
        <DbType>drds</DbType>
        <EnvType>product</EnvType>
        <SchemaName>xxx</SchemaName>
    </UserPermission>
</UserPermissions> <TotalCount>1</TotalCount> <RequestId>68075D06-7406-4887-83A7-F558A4D28C13</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "UserPermissions": {
    "UserPermission": [
```

`{`

```json
        "Logic": false,
        "UserNickName": "xxx",
        "DsType": "DATABASE",
        "Alias": "beihe_ent_prod",
        "PermDetails": {
          "PermDetail": [
```

`{`

```json
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390915",
              "PermType": "QUERY",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
```

`},` `{`

```json
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390916",
              "PermType": "EXPORT",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
```

`},` `{`

```json
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390917",
              "PermType": "CORRECT",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
```

`}` `]` `},`

```json
        "InstanceId": 1434,
        "SearchName": "xxx@xxxx:3306",
        "DbId": 123434,
        "UserId": 432423,
        "DbType": "drds",
        "EnvType": "product",
        "SchemaName": "xxx"
```

`}` `]` `},`

```json
  "TotalCount": 1,
  "RequestId": "68075D06-7406-4887-83A7-F558A4D28C13",
  "Success": true
```

`}`

#### 6.8.3 SetOwners

Sets the owners of a database or a table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetOwners | The operation that you want to perform. Set the value to Set Owners. |
| OwnerIds | String | Yes | 123, 456 | The IDs of the owners. Separate multiple IDs with commas (,). |
| OwnerType | String | Yes | DATABASE | The type of the owner. Valid values: DATABASE: an owner of physical databases. LOGIC DATABASE: an owner of _ logical databases. TABLE: an owner of physical tables. LOGIC TABLE: an owner of logical _ tables. |
| ResourceId | String | Yes | 123 | The ID of the resource. The ID is based on the value of the OwnerT ype parameter. Valid values for the OwnerT ype parameter: DATABASE: physical databases. LOGIC DATABASE: logical databases. _ TABLE: physical tables. LOGIC TABLE: logical tables. _ |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | The ID of the request. |

|   | Data Management |   |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetOwners &OwnerIds=123, 456 &OwnerType=DATABASE &ResourceId=123 &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
```

`}`

#### 6.8.4 ListUserPermissions

Queries the permissions of a user on databases and tables. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListUserPermissio ns | The operation that you want to perform. Set the value to List UserPermissions. |
| PermType | String | Yes | DATABASE | The type of resources on which the user has permissions. For more information, see List Dat abaseUserPermssions. |
| Tid | Long | Yes | -1 | The ID of the tenant. |

| eveloper Guide·API | Reference |   |   | Data Managemen |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UserId | String | Yes | 13435 | The ID of the user. The user ID is the same as the user ID that is specfied in the Get User operation. The user ID is different from the ID of your Apsara Stack tenant account. |
| DatabaseName | String | No | db name _ | The name of the database. |
| Logic | Boolean | No | false | Specifies whether the database is a logical database. Valid values: true false |
| EnvType | String | No | dev | The type of the environment to which the database belongs. |
| DbType | String | No | MySQL | The type of the database. |
| PageNumber | Integer | No | 1 | The number of the page to return |
| PageSize | Integer | No | 1 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | C51420E3-144A- 4A94-B473- 8662FCF4AD10 | The ID of the request. |
| Success | Boolean | true | Indicates whether the call succeeded. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 6 | The total number of entries that meet the query conditions. |
| UserPermission s | Array of UserPermission |   | The details of user permissions. |
| UserPermission |   |   |   |
| Alias | String | instance alias _ | The alias of the instance. |
| ColumnName | String | column name _ | The name of the field. |
| DbId | String | 1324 | The ID of the database. |
| DbType | String | mysql | The type of the database. |
| DsType | String | DATABASE | The type of resources on which the user has permissions. |
| EnvType | String | dev | The type of the environment to which the database belongs. |
| InstanceId | String | 134 | The ID of the instance. |
| Logic | Boolean | false | Indicates whether the database is a logical database. Valid values: true false |
| PermDetails | Array of PermDetail |   | The details of permissions. |
| PermDetail |   |   |   |
| CreateDate | String | 2019-12-12 00:00:00 | The time when the permission was authorized. |
| ExpireDate | String | 2020-12-12 00:00:00 | The time when the permission expires. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ExtraData | String | xxx | The additional data. This parameter is reserved. |
| OriginFrom | String | xxx | The entity that authorizes the permission. |
| PermType | String | QUERY | The type of the permission. |
| UserAccessId | String | 1345 | The ID of the authorization record. |
| SchemaName | String | test db _ | The name of a database. |
| SearchName | String | test db@xxx:3306 _ | The name that is used to search for the database. |
| TableId | String | 13434 | The ID of the table. |
| TableName | String | test table _ | The name of the table. |
| UserId | String | 423245 | The ID of the user. |
| UserNickName | String | nick name _ | The name of the user. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListUserPermissions &PermType=DATABASE &Tid=-1 &UserId=13435 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UserPermissions>
    <UserPermission>
        <Logic>false</Logic>
        <UserNickName>xxx</UserNickName>
        <DsType>DATABASE</DsType>
        <Alias>xxx_ent_dev</Alias>
        <PermDetails>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390913</UserAccessId>
                <PermType>EXPORT</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
            <PermDetail>
                <ExpireDate>2020-10-31 00:00:00</ExpireDate>
                <UserAccessId>390914</UserAccessId>
                <PermType>CORRECT</PermType>
                <OriginFrom>xxx</OriginFrom>
                <CreateDate>2019-11-21 15:07:45</CreateDate>
            </PermDetail>
        </PermDetails>
        <InstanceId>24671</InstanceId>
        <SearchName>xxx@xxx:3306</SearchName>
        <DbId>111369</DbId>
        <UserId>88658</UserId>
        <DbType>drds</DbType>
        <EnvType>dev</EnvType>
        <SchemaName>xxx_ent_dev</SchemaName>
    </UserPermission>
</UserPermissions> <TotalCount>6</TotalCount> <RequestId>C51420E3-144A-4A94-B473-8662FCF4AD10</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "UserPermissions": {
    "UserPermission": [
```

`{`

```json
        "Logic": false,
        "UserNickName": "xxx",
        "DsType": "DATABASE",
        "Alias": "xxx_ent_dev",
        "PermDetails": {
          "PermDetail": [
```

`{`

```json
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390913",
              "PermType": "EXPORT",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
```

`},` `{`

```json
              "ExpireDate": "2020-10-31 00:00:00",
              "UserAccessId": "390914",
              "PermType": "CORRECT",
              "OriginFrom": "xxx",
              "CreateDate": "2019-11-21 15:07:45"
```

`}` `]` `},`

```json
        "InstanceId": 24671,
        "SearchName": "xxx@xxx:3306",
        "DbId": 111369,
        "UserId": 88658,
        "DbType": "drds",
        "EnvType": "dev",
        "SchemaName": "xxx_ent_dev"
```

`}` `]` `},`

```json
  "TotalCount": 6,
  "RequestId": "C51420E3-144A-4A94-B473-8662FCF4AD10",
  "Success": true
```

`}`

#### 6.8.5 GrantUserPermission

Grants permissions on a database or a table to a user. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GrantUserPermiss ion | The operation that you want to perform. Set the value to Grant UserPermission. |
| DbId | String | Yes | 1234 | The ID of the database. |
| DsType | String | Yes | DATABASE | The type of the permissions. Valid values: DATABASE: permissions on physical databases LOGIC DATABASE: permissions on _ logical databases TABLE: permissions on physical databases LOGIC TABLE: permissions on logical _ tables |
| ExpireDate | String | Yes | 2019-12-12 00:00:00 | The time when the permissions expire. |
| PermTypes | String | Yes | QUERY, EXPORT, CORRECT | The type of the permission. Separate multiple permission types with commas (,). Valid values: QUERY: the query permission EXPORT: the export permission CORRECT: the change permission |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| UserId | String | Yes | 12345 | The ID of the user. You can call the Get User operation to obtain the user ID. The user ID is different from the Apsara Stack tenant account ID of the user. |
| Logic | Boolean | No | false | Specifies whether the database is a logical database. |
| TableId | String | No | 1324245 | The ID of the table. This parameter is required when you grant permissions on a table. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TableName | String | No | table name _ | The name of the table. This parameter is required when you grant permissions on a table. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | A99CD576-1E18- 4E86-931E- C3CCE56DC030 | The ID of the request. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=GrantUserPermission &DbId=1234 &DsType=DATABASE &ExpireDate=2019-12-12 00:00:00 &PermTypes=QUERY, EXPORT, CORRECT &Tid=-1 &UserId=12345 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>A99CD576-1E18-4E86-931E-C3CCE56DC030</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "A99CD576-1E18-4E86-931E-C3CCE56DC030",
  "Success": true
```

`}`

### 6.9 Security management

#### 6.9.1 ListSensitiveColumns

Queries sensitive columns. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListSensitiveColu mns | The operation that you want to perform. Set the value to List Sensit iveColumns. |
| Tid | Long | Yes | -1 | The ID of the tenant. |
| SchemaName | String | No | test | The name of the database. |
| TableName | String | No | test | The name of the table. |
| ColumnName | String | No | test | The name of the column. |
| SecurityLevel | String | No | SENSITIVE | The sensitivity level of the column. Valid values: INNER SENSITIVE CONFIDENTIAL |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 0E714EF1-E617- 4BBC-A3D2- 9552063BA942 | The ID of the request. |
| SensitiveColum nList | Array of SensitiveColum n |   | The sensitive columns. |
| SensitiveColum n |   |   |   |
| ColumnCount | Long | 1 | The number of columns. |
| ColumnName | String | test | The name of the column. |
| FunctionType | String | DEFAULT | The type of the desensitization algorithm. Valid values: DEFAULT: All characters are masked. This is the default value. FIX POS: The fixed position is masked. _ FIX CHAR: The fixed characters are _ masked. |
| SchemaName | String | test | The name of the database. |
| SecurityLevel | String | SENSITIVE | The sensitivity level of the column. |
| TableName | String | test | The name of the table. |
| Success | Boolean | true | Indicates whether the request succeeded. |
| TotalCount | Long | 10 | The total number of entries that are returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListSensitiveColumns &Tid=-1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>5</TotalCount> <RequestId>0E714EF1-E617-4BBC-A3D2-9552063BA942</RequestId> <SensitiveColumnList>
    <SensitiveColumn>
        <TableName>yuyang_test</TableName>
        <ColumnName>c1</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>SENSITIVE</SecurityLevel>
        <SchemaName>testdb</SchemaName>
    </SensitiveColumn>
    <SensitiveColumn>
        <TableName>yuyang_test_luanma</TableName>
        <ColumnName>c1</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>SENSITIVE</SecurityLevel>
        <SchemaName>testdb</SchemaName>
    </SensitiveColumn>
    <SensitiveColumn>
        <TableName>yuyang_test</TableName>
        <ColumnName>id</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>SENSITIVE</SecurityLevel>
        <SchemaName>testdb</SchemaName>
    </SensitiveColumn>
    <SensitiveColumn>
        <TableName>yuyang_test_luanma</TableName>
        <ColumnName>id</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>SENSITIVE</SecurityLevel>
        <SchemaName>testdb</SchemaName>
    </SensitiveColumn>
    <SensitiveColumn>
        <TableName>yuyang_test_json</TableName>
        <ColumnName>id</ColumnName>
        <ColumnCount>0</ColumnCount>
        <SecurityLevel>CONFIDENTIAL</SecurityLevel>
        <SchemaName>test_demo</SchemaName>
    </SensitiveColumn>
</SensitiveColumnList> <Success>true</Success>
```

`JSON` format `{`

```json
  "TotalCount": 5,
  "RequestId": "0E714EF1-E617-4BBC-A3D2-9552063BA942",
  "SensitiveColumnList": {
    "SensitiveColumn": [
```

`{`

```json
        "TableName": "yuyang_test",
        "ColumnName": "c1",
        "ColumnCount": 0,
        "SecurityLevel": "SENSITIVE",
        "SchemaName": "testdb"
```

`},` `{`

```json
        "TableName": "yuyang_test_luanma",
        "ColumnName": "c1",
        "ColumnCount": 0,
        "SecurityLevel": "SENSITIVE",
        "SchemaName": "testdb"
```

`},` `{`

```json
        "TableName": "yuyang_test",
        "ColumnName": "id",
        "ColumnCount": 0,
        "SecurityLevel": "SENSITIVE",
        "SchemaName": "testdb"
```

`},` `{`

```json
        "TableName": "yuyang_test_luanma",
        "ColumnName": "id",
        "ColumnCount": 0,
        "SecurityLevel": "SENSITIVE",
        "SchemaName": "testdb"
```

`},` `{`

```json
        "TableName": "yuyang_test_json",
        "ColumnName": "id",
        "ColumnCount": 0,
        "SecurityLevel": "CONFIDENTIAL",
        "SchemaName": "test_demo"
```

`}` `]` `},`

```json
  "Success": true
```

`}`

#### 6.9.2 ListSensitiveColumnsDetail

Queries the details of sensitive fields. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListSensitiveColu mnsDetail | The operation that you want to perform. Set the value to List Sensit iveColumnsDet ail. |
| ColumnName | String | Yes | test | The name of the field. |
| SchemaName | String | Yes | test | The name of the database. |
| TableName | String | Yes | test | The name of the table. |
| Tid | Long | Yes | 1 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The returned error code. |
| ErrorMessage | String | UnknownError | The returned error message. |
| RequestId | String | 7629888F-C9FB- 4D16-A7D3- B443FE06FBD4 | The ID of the request. |
| SensitiveColum nsDetailList | Array of SensitiveColum nsDetail |   | The details about the sensitive fields. |
| SensitiveColum nsDetail |   |   |   |
| ColumnDescript ion | String | test | The description of the field. |
| ColumnName | String | test | The name of the field. |
| ColumnType | String | varchar(32) | The data type of the field. |
| DbId | Long | 124 | The ID of the database. |

| Developer Guide·AP | I Reference |   | Data Managemen |
|---|---|---|---|
| Parameter | Type | Example | Description |
| DbType | String | mysql | The type of the database. |
| EnvType | String | product | The type of the environment to which the database belongs. |
| Logic | Boolean | false | Indicates whether the database is a logical database. |
| SchemaName | String | test | The name of the database. |
| SearchName | String | test@xxx:3306 | The name that is used to search for the database. |
| TableName | String | test | The name of the table. |
| Success | Boolean | true | Indicates whether the request succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListSensitiveColumnsDetail &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7629888F-C9FB-4D16-A7D3-B443FE06FBD4</RequestId> <SensitiveColumnsDetailList>
    <SensitiveColumnsDetail>
        <TableName>king_info</TableName>
        <ColumnName>mobile</ColumnName>
        <ColumnType>varchar(64)</ColumnType>
        <SearchName>p***@xxx.mysql.rds.aliyuncs.com:3306【xxx】</SearchName>
        <ColumnDescription>mobile</ColumnDescription>
        <DbId>8511149</DbId>
        <Logic>false</Logic>
        <SchemaName>poc_prod</SchemaName>
        <EnvType>product</EnvType>
        <DbType>mysql</DbType>
    </SensitiveColumnsDetail>
</SensitiveColumnsDetailList> <Success>true</Success>
```

`JSON` format `{`

```json
  "RequestId": "7629888F-C9FB-4D16-A7D3-B443FE06FBD4",
  "SensitiveColumnsDetailList": {
    "SensitiveColumnsDetail": [
```

`{`

```json
        "TableName": "king_info",
        "ColumnName": "mobile",
        "ColumnType": "varchar(64)",
        "SearchName": "p***@xxx.mysql.rds.aliyuncs.com:3306【xxx】",
        "ColumnDescription": "mobile",
        "DbId": 8511149,
        "Logic": false,
        "SchemaName": "poc_prod",
        "EnvType": "product",
        "DbType": "mysql"
```

`}` `]` `},`

```json
  "Success": true
```

`}`

### 6.10 Data query

#### 6.10.1 ExecuteScript

Executes SQL statements. This operation is available only for instances that are managed in the security collaboration mode. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ExecuteScript | The operation that you want to perform. Set the value to Execut eScript . |
| DbId | Integer | Yes | 123 | The ID of the database. Not e You can obtain the database ID from the Dat abaseId parameter that is returned by the Get Dat abase operation. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Logic | Boolean | Yes | false | A Boolean value that indicates whether the database to be affected is a logical database. |
| Script | String | Yes | select dt from report daily _ | The SQL statements to be executed. Data query language (DQL) statements, data definition language (DDL) statements, and data manipulation language (DML) statements are supported. The control mode of the instance that you want to query determines whether you can execute DDL and DML statements. |
| Tid | Long | No | 234 | The ID of the tenant. |
| RegionId | String | No | cn-hangzhou | The region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrorCode | String | UnknownError | The error code that is returned. |
| ErrorMessage | String | UnknownError | The error message that is returned. |
| RequestId | String | FE8EE2F1-4880- 46BC-A704- 5CF63EAF9A04 | The ID of the request. |
| Results | Array of Result |   | The results that are returned by the SQL statements in the format of an array. Each entry in the array indicates the result of an SQL statement. |
| ColumnNames | List | ["col1", "col2"] | The fields that are returned by the SQL statement. |
| Message | String | UnknownError | The error message that is returned if the call fails. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RowCount | Long | 1 | The total number of entries that are returned. |
| Rows | List | [{"col1": "value1", "col2":"value2"}] | The rows that are returned by the SQL statement. |
| Success | Boolean | true | Indicates whether the SQL statement is executed. |
| Success | Boolean | true | Indicates whether the call succeeded. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ExecuteScript &DbId=123 &Logic=false &Script=select dt from report_daily &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>FE8EE2F1-4880-46BC-A704-5CF63EAF9A04</RequestId> <Results>
    <Message>UnknownError</Message>
    <RowCount>1</RowCount>
    <Success>true</Success>
</Results> <Results>
    <ColumnNames>["col1", "col2"]</ColumnNames>
    <Rows>[{"col1": "value1", "col2":"value2"}]</Rows>
</Results> <ErrorCode>UnknownError</ErrorCode> <ErrorMessage>UnknownError</ErrorMessage> <Success>true</Success>
```

`JSON` format

```json
{"RequestId":"FE8EE2F1-4880-46BC-A704-5CF63EAF9A04","Results":[{"Message":"UnknownError","R owCount":"1","Success":"true"},{"ColumnNames":"[\"col1\", \"col2\"]","Rows":"[{\"col1\": \" value1\", \"col2\":\"value2\"}]"}],"ErrorCode":"UnknownError","ErrorMessage":"UnknownError" ,"Success":"true"}
```

## 7 Appendixes

### 7.1 Process of API calls by using the ASAPI gateway

ASAPI gateway You can use the ASAPI gateway to call API operations of most Apsara Stack services. This topic describes how to call API operations by using the ASAPI gateway and provides links to references. Flowchart Procedure
1. Obtain an ASAPI SDK.
Before you use ASAPI to call an API operation, you must obtain ASAPI SDK for Java or ASAPI SDK for Python. For more information, see Obtain an ASAPI SDK.
2. Obtain the endpoint of ASAPI. For more information, see Generate an endpoint for ASAPI.
3. Obtain AccessKey credentials.
Obtain AccessKey credentials that are required when you call an API operation. Not e We recommend that you use the AccessKey pair of your Apsara Stack tenant account to call the API operations of the Apsara Uni-manager Management Console and cloud services.
4. Obtain the region ID.
Obtain the region ID that is required when you call an API operation.
5. Obtain the organization ID and resource set ID.
You must call an API operation to obtain the resource set ID. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Con sole Developer Guide. Not e When you call an API operation, you can specify the organization ID and resource set ID by using the <x-acs-organizationid> and <x-acs-resourcegroupid> parameters. This way, you can query specified resources. If you do not set the <x-acs-organizationid> parameter, the organization to which the current user belongs is used by default. If you do not set the <x-acs-resourcegroupid> parameter, the parameter is left empty. If you specify a resource set ID, you must also specify an organization ID.
6. Refer to the API reference.
Obtain the developer guide of the cloud service that you want to use. You can learn the features of API operations and how to call the API operations. For more information, see Usage notes on development documentation.
7. Use the obtained ASAPI SDK to call API operations.
After you complete the preceding steps, you can use the ASAPI SDK to call API operations. For more information about how to use SDKs for different languages, see the relevant topics. The following example shows how to call the DescribeInstances operation of ECS by using SDK for Java:

```java
public static void main(String[] args) {
    ASClient client = new ASClient();
    // Specify the caller. The caller is recorded in logs.
    client.setSdkSource("autoTest");
    // Set request parameters.
    Map<String, Object> parameters = new HashMap<String, Object>();
    parameters.put("Product", "dms-enterprise");// The POP code, which is the same as t
he POP code in the corresponding API directory.
    parameters.put("Action", "GetOpLog"); // The name of the API operation. The name is
case-sensitive and must be the same as that in the API directory.
    parameters.put("Version", "2014-05-26"); // The API version.
    // Specify the region ID that you obtained.
    parameters.put("RegionId", "xxx");
    // Specify your AccessKey ID and AccessKey secret.
    parameters.put("AccessKeyId", "xxx");
    parameters.put("AccessKeySecret", "xxx");
    // Add the parameters based on the relevant API reference. The parameters are case-
sensitive.
    parameters.put("PageNumber",1);
    parameters.put("PageSize",10);
    Map<String,String> headers=new HashMap<>();
    // Specify the organization ID in the Apsara Uni-manager Management Console.
    headers.put("x-acs-organizationid","3");
    // Specify the resource set ID in the Apsara Uni-manager Management Console.
    //headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>");
    // Specify the endpoint of ASAPI.
    String endpoint="https://public.asapi.xxx.xxx/asapi/v3";
    // Initiate the request.
    String result = client.doPost(endpoint,headers, parameters);
    // Display the results.
    System.out.println(JSONObject.toJSONString(JSONObject.parseObject(result), Serializ
erFeature.PrettyFormat));
```

`}`

### 7.2 Use the ASAPI gateway to make API calls

API calls

#### 7.2.1 Obtain an endpoint of ASAPI

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

Not e
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

Not e ${global:region} and ${global:internet-domain} are variables. You must replace them with the actual values that you obtained. Available endpoint example: Unavailable endpoint example: Historical endpoint Only the HTTP protocol is supported. The historical endpoint is suffixed with `intranet-domain` and in the following format:

```
 http://server.asapi.${global:region}.${global:intranet-domain}/asapi/v3
```

Not e ${global:region} and ${global:intranet-domain} are variables. You must replace them with the actual values that you obtained. Procedure To obtain the actual values of the variables ${global:region}, ${global:internet-domain}, and ${global:intranet-domain}, perform the following operations:
1. In the address bar, enter the region-id.aso.intranet-domain-id.com URL and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password used to log on to the Apsara Uni-manager Operations Console from the deployment personnel or an administrator. When you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password is 10 to 20 characters in length.
3. Click Log On to log on to the Apsara Uni-manager Operat ions Console.
4. In the top navigation bar, choose Product s > Plat f orms > Apsara Inf rast ruct ure Management
Framework to go to Apsara Infrastructure Management.
5. In the left-side navigation pane, choose Operat ions > Clust er Operat ions.
6. On the Clust ers page, enter ascm-A in the Cluster search box to find the cluster. Click the cluster
name.
7. On the Clust er Dashboard page, click Operat ions Menu > Conf igurat ion Files.
8. In the File List window on the left side of the Clust er Conf igurat ion page, click kv.conf , click the
file content in the right window, and then press Ctrl + F. Search for region, internet-domain, and intranet-domain. Replace ${global:region} with the obtained region value, ${global:internet-domain} with the obtained internet-domain value, and ${global:intranet-domain} with the obtained intranet-domain value. Not e ${global:} is not included in the endpoint of ASAPI that you can use.

#### 7.2.2 Generate an endpoint for ASAPI

This topic describes how to generate an endpoint for ASAPI.
1. Log on to the OPS1 server.
2. Run the following command to obtain three different domain names:

```bash
kubectl get ingress -n ascm |grep asapiserver
```

3. Record the domain name that starts with `public` and use the domain name as the value of
`domain` in the next step.
4. Generate an endpoint for ASAPI in the following format:

```
https://<domain>/asapi/v3
```

#### 7.2.3 Obtain Apsara Stack SDKs

Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. Public environment If you are using the public environment, you can go to the Apsara Stack documentation page and download the Apsara Stack SDKs in the Ot her Resources section at the lower part of the page. Private environment If you are using the private environment, you must switch to the public environment and then go to the Apsara Stack documentation page. At the lower part of the page, download the Apsara Stack SDKs in the Ot her Resources section. Apsara Stack SDK for Java

| greopId | artifactId | Version |
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

| Developer Guide·Appendixes | Data Managemen |
|---|---|

| Package | Version |
|---|---|
| pycparser | 2.20 |
| requests | 2.26.0 |
| urllib3 | 1.26.6 |

Not e You can use the version for each package listed in the preceding table or a later version.

### 7.3 STS overview

#### 7.3.1 What is STS?

STS allows you to manage temporary credentials to your Apsara Stack resources. RAM provides RAM users and roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed to access Apsara Stack resources by using an STS token. When an STS token is issued, you can specify a validity period and access permissions for the STS token. Use an STS token to assume a RAM role An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and use the STS token to access Apsara Stack resources. Benefits STS tokens reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify a validity period for an STS token. The token automatically becomes invalid when it expires. You do not need to rotate STS tokens on a regular basis. You can attach custom policies to STS tokens for flexible and fine-grained authorization.

#### 7.3.2 AssumeRole

Obtains a Security Token Service (STS) token that is used by a RAM user to assume a RAM role. In this example, an Apsara Stack tenant account is used as the trusted entity of the RAM role. Request parameters

| Paramet er | T ype | Requi red | Example | Descript ion |
|---|---|---|---|---|
| Act ion | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |

| Data Management |   |   |   | Developer Guide·Appendixe |
|---|---|---|---|---|

| Paramet er | T ype | Requi red | Example | Descript ion |
|---|---|---|---|---|
| RoleArn | String | Yes | acs:ram::1234567 89012****:role/ad minrole | The Apsara Stack Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Apsara Stack tenant account. |
| RoleSessionNam e | String | Yes | alice | The name of the role session. Set this parameter based on your business requirements. In most cases, you can set this parameter to the identity of the user who calls the operation. For example, specify a username. In ActionTrail logs, you can distinguish the users who assume the same RAM role to perform operations based on the value of the RoleSessionName parameter. This way, you can perform user-specific auditing. The name must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource ": ["*"]}],"Version":"1 "} | The policy that specifies the permissions of the STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. The policy must be 1 to 1,024 characters in length. |

Responses

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| Request Id | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | The ID of the request. |
| Credent ials | None | None | The access credentials. |

| Developer Guide·Append | ixes |   | Data Managemen |
|---|---|---|---|

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| AccessKeyId | String | STS.L4aBSCSJVMuKg5 U1**** | The AccessKey ID. |
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
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest;
```

```
potco.a yucs.Co
```

`o`

```java
equest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
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
```

```java
            System.out.println(e.getErrMsg());
```

`}` `}` `}` Call examples In the following sample code, the `DescribeZones` operation in Elastic Compute Service (ECS) is used.

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
```

```java
            System.out.println(response.getData());
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
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

| Ht t pCode | Error code | Error message | Descript ion |
|---|---|---|---|
| 400 | InvalidParameter.Durati onSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the Durat ionSeconds parameter is invalid. The minimum value is 900, and the maximum value is equal to the value of the MaxSessionDurat ion parameter. |
| 400 | InvalidParameter.PolicyG rammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the policy is invalid. |
| 400 | InvalidParameter.PolicyS ize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error occurred. |
