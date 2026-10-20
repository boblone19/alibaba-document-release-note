---
title: "Realtime Compute for Apache Flink (Compute-Storage Separation Edition) Developer Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 370
source_pdf: "6fbe874eebbdd54b_Alibaba Cloud Apsara Stack V3.18.6 Realtime Compute for Apache Flink (Compute-Storage Separation Edi"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AE%9E%E6%97%B6%E8%AE%A1%E7%AE%97FLink/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Realtime%20Compute%20for%20Apache%20Flink%20%28Compute-Storage%20Separation%20Edition%29%20Developer%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Realtime Compute for Apache Flink (Compute-Storage Separation Edition) Developer Guide 20260701

## Table of Contents

- 1 Preparations
  - 1.1 Obtain API information and its endpoint
  - 1.2 Obtain common header parameters
  - 1.3 Obtain an AccessKey pair
  - 1.4 Obtain access credentials assigned by STS
- 2 Use POP to make API calls
  - 2.1 SDK for Java
  - 2.2 SDK for Go
  - 2.3 SDK for Python
- 3 AppManager API
  - 3.1 Definition
    - 3.1.1 CommitDeploymentDraft
    - 3.1.2 CreateDeployment
    - 3.1.3 CreateDeploymentDraft
    - 3.1.4 CreateFolder
    - 3.1.5 CreateSavepoint
    - 3.1.6 CreateSessionCluster
    - 3.1.7 DeleteArtifact
    - 3.1.8 DeleteDeployment
    - 3.1.9 DeleteFolder
    - 3.1.10 DeleteSessionCluster
    - 3.1.11 ExecuteSqlScript
    - 3.1.12 GetArtifactMetadata
    - 3.1.13 GetFolderById
    - 3.1.14 GetRootFolderByType
    - 3.1.15 GetDeployment
    - 3.1.16 GetDeploymentDefaults
    - 3.1.17 GetGlobalDeploymentDefaults
    - 3.1.18 GetSessionClusterByName
    - 3.1.19 ListArtifacts
    - 3.1.20 ListDeployments
    - 3.1.21 ListDeploymentTargets
    - 3.1.22 ListJobs
    - 3.1.23 ListNamespaces
    - 3.1.24 ListDeploymentDrafts
    - 3.1.25 ListSavepoints
    - 3.1.26 ListSessionClusters
    - 3.1.27 UpdateDeployment
    - 3.1.28 UpdateDeploymentDesiredState
    - 3.1.29 UpdateDeploymentDraft
    - 3.1.30 UpdateSessionCluster
    - 3.1.31 UpdateSessionClusterDesiredState
    - 3.1.32 UploadArtifactByOSSUrl
    - 3.1.33 UpdateFolder
    - 3.1.34 ValidateSqlScript
    - 3.1.35 ValidateDeploymentDraft
    - 3.1.36 ListTables
    - 3.1.37 ListCatalogs
    - 3.1.38 ListFunctions
    - 3.1.39 GetDatabase
    - 3.1.40 DatabaseExists
    - 3.1.41 CreateConnector
    - 3.1.42 CreateFormat
    - 3.1.43 CreateMember
    - 3.1.44 CreateSecretValue
    - 3.1.45 CreateUdfArtifact
    - 3.1.46 DeleteConnector
    - 3.1.47 DeleteDeploymentDraft
    - 3.1.48 DeleteFormat
    - 3.1.49 DeleteMember
    - 3.1.50 DeleteSecretValue
    - 3.1.51 DeleteUdfArtifact
    - 3.1.52 ExecuteSqlscriptsStatements
    - 3.1.53 ForcefullyCreateLock
    - 3.1.54 FunctionExists
    - 3.1.55 GenerateResourcePlan
    - 3.1.56 GetCatalog
    - 3.1.57 GetDefaultDatabase
    - 3.1.58 GetDeploymentDraftById
    - 3.1.59 GetDeploymentDraftByName
    - 3.1.60 GetDeploymentDraftResourcePlan
    - 3.1.61 GetDeploymentDraftResourcePlanWithBestEffort
    - 3.1.62 GetFunction
    - 3.1.63 GetResourcePlan
    - 3.1.64 GetTable
    - 3.1.65 GetUdfArtifact
    - 3.1.66 ListConnectors
    - 3.1.67 ListDatabases
    - 3.1.68 ListFlinkVersions
    - 3.1.69 ListFormats
    - 3.1.70 ListSecretValues
    - 3.1.71 ParseConnector
    - 3.1.72 ParseFormat
    - 3.1.73 SearchFoldersByKeyword
    - 3.1.74 SetDeploymentResourceMode
    - 3.1.75 TableExists
    - 3.1.76 UpdateConnector
    - 3.1.77 UpdateFormat
    - 3.1.78 UpdateMember
    - 3.1.79 UpdateUdfArtifact
    - 3.1.80 CreateNamespace
    - 3.1.81 DescribeNamespaces
    - 3.1.82 GetCluster
    - 3.1.83 UpdateNamespace
    - 3.1.84 DeleteNamespace
  - 3.2 API examples
    - 3.2.1 Examples
    - 3.2.2 pom.xml
- 4 Flink SQL reference
  - 4.1 Overview
  - 4.2 Keywords
  - 4.3 Create a data view
  - 4.4 Basic concepts
    - 4.4.1 Watermark
    - 4.4.2 Computed column
    - 4.4.3 Time attribute
  - 4.5 Subscription
    - 4.5.1 INSERT INTO statement
  - 4.6 Query statements
  - 4.7 Window functions
    - 4.7.1 Overview
    - 4.7.2 Tumbling window
    - 4.7.3 Sliding window
    - 4.7.4 Session window
    - 4.7.5 OVER windows
  - 4.8 Built-in functions
    - 4.8.1 Overview
    - 4.8.2 Scalar functions
      - 4.8.2.1 BITAND
      - 4.8.2.2 BITNOT
      - 4.8.2.3 BITOR
      - 4.8.2.4 BITXOR
      - 4.8.2.5 CONV
      - 4.8.2.6 DATEDIFF
      - 4.8.2.7 DATE_ADD
      - 4.8.2.8 DATE_FORMAT
      - 4.8.2.9 DATE_FORMAT_TZ
      - 4.8.2.10 DATE_SUB
      - 4.8.2.11 FROM_UNIXTIME
      - 4.8.2.12 ISNAN
      - 4.8.2.13 JSON_VALUE
      - 4.8.2.14 KEYVALUE
      - 4.8.2.15 MURMUR_HASH
      - 4.8.2.16 MURMUR_HASH_64
      - 4.8.2.17 PARSE_URL
      - 4.8.2.18 REGEXP
      - 4.8.2.19 REGEXP_REPLACE
      - 4.8.2.20 SPLIT_INDEX
      - 4.8.2.21 TO_DATE
      - 4.8.2.22 TO_TIMESTAMP_TZ
      - 4.8.2.23 UNIX_TIMESTAMP
    - 4.8.3 Table-valued functions
      - 4.8.3.1 GENERATE_SERIES
      - 4.8.3.2 JSON_TUPLE
      - 4.8.3.3 MULTI_KEYVALUE
      - 4.8.3.4 STRING_SPLIT
    - 4.8.4 Aggregate functions
      - 4.8.4.1 APPROX_COUNT_DISTINCT
      - 4.8.4.2 FIRST_VALUE
      - 4.8.4.3 LAST_VALUE
  - 4.9 User-defined functions (JAR)
    - 4.9.1 Overview
    - 4.9.2 User-defined scalar function (UDF)
    - 4.9.3 User-defined aggregate function (UDAF)
    - 4.9.4 User-defined table-valued function (UDTF)
  - 4.10 User-defined functions (Python)
    - 4.10.1 Overview
    - 4.10.2 User-defined scalar function (UDF)
    - 4.10.3 User-defined aggregate function (UDAF)
    - 4.10.4 User-defined table-valued function (UDTF)
  - 4.11 Machine learning functions
    - 4.11.1 CLUSTER_SERVING

tions

## 1 Preparations

Like Alibaba Cloud Public Cloud, Alibaba Cloud Apsara Stack supports API calls through the POP Gateway. This topic describes the preparations you must complete before making an API call.

### 1.1 Obtain API information and its endpoint

**endpoint**

To call an API through the POP Gateway, you must understand relevant information about the Cloud Service OpenAPI. This topic describes two methods for obtaining the endpoint of a cloud service.

**Background information**

To ensure that Apsara Stack provides the same user experience as the Public Cloud, we recommend that you call Apsara Stack APIs through the POP Gateway.

> **Note:** The API information in the API catalog of the Apsara Uni-manager Management Console serves only as a reference for API calls. For specific API usage, refer to the development guide of the corresponding cloud service. In case of inconsistency, the development guide takes precedence.

**Procedure**

**Obtain an endpoint by using OpenAPI Explorer**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Products** > **Development Tools** > **OpenAPI Explorer**.
3. On the **OpenAPI Explorer** page, select **API Integration** > **API Debugging**.
4. In the left-side navigation pane, select the target cloud service.
5. In the **Version** drop-down list, select the target API version.
6. Browse all API operations available in the current version from the API list below.
7. Select the corresponding API operation and obtain the POP endpoint information of the cloud
service under the parameter name. tions

**Obtain an endpoint by using Apsara Infrastructure Management**

When calling an Apsara Stack API through the POP Gateway, you must use the endpoint of the business domain of the cloud service. You can obtain the endpoint from Alibaba Cloud on-site O&M engineers. You can also obtain the endpoint yourself. This topic uses API Gateway as an example to describe how to obtain the endpoint of the business domain of a cloud service.
1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, select **Platform Operartion** > **Apsara Infrastructure**
**Management** > **O&M Tools**.
3. In the left-side navigation pane, select **O&M Tools** > **Service Registration Variable**
**Dashboard**.
4. On the **Service Registration Variable Dashboard** page, click **Advanced Filter**.
5. In the Service Registration text box, enter `apigateway` and click **Search**.
icon.
6. In the **Service Registration** column of the `apigateway` service, click the
7. Click the text in the **Service Registration** column of the `apigateway` service. In the
**Registration Variables** dialog box that appears, view the value of
apigateway.openapi.endpoint, which is the `endpoint` .

### 1.2 Obtain common header parameters

**parameters**

When calling an API, you must provide multiple header parameters such as the region ID, organization ID, resource set ID, and instance ID. This topic describes how to obtain these parameters and explains some return values after API calls

**Obtain a region ID**

1. Log in to the Apsara Uni-manager Management Console as an administrator.
tions
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, select **Resources** > **Regions**.
4. Click the name of the target organization.
5. In the **Regions** list on the right, view the **region name**. The region name is the region ID.

**Obtain an organization ID**

You must call an API operation to obtain an organization ID. You can use the online debugging feature in the Apsara Uni-manager Management Console to quickly obtain the organization ID.
1. Log in to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, select **Products** > **Development Tools** > **OpenAPI Explorer**.
3. On the **OpenAPI Explorer** page, select **API Integration** > **API Debugging**.
4. Click the
button, select **Platform** > **Apsara Uni-manager**, and set **Version** to 2024-09- 12.
5. Enter `GetOrganizationList` in the search box for online debugging. Enter the name of the
target organization in the name parameter and initiate the call. After the call succeeds, view the information about **id** in **Call Result**. The value of id is the organization ID. For more information about the API operation, see the GetOrganizationList section in Apsara Uni-manager Managemen t Console Developer Guide.

**Obtain a resource set ID**

You must call an API operation to obtain a resource set ID. You can use the online debugging feature in the Apsara Uni-manager Management Console to quickly obtain the resource set ID.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, select **Products** > **Development Tools** > **OpenAPI Explorer**.
3. On the **OpenAPI Explorer** page, select **API Integration** > **API Debugging**.
4. Click the
button, select **Platform** > **Apsara Uni-manager**, and set **Version** to 2024-09- 12.
5. Enter `ListResourceGroup` in the search box for online debugging. After the call succeeds, view
the information about **id** in **Call Result**. The value of id is the resource set ID. For more information about the API operation, see the ListResourceGroup section in Apsara Uni-Manager Management Console Developer Guide.

**Obtain an instance ID**

You can obtain an instance ID from the cloud service instance list in the Apsara Uni-manager Management Console. The following steps use API Gateway as an example:
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Products** > **Development Tools** > **API Gateway**.
3. In the left-side navigation pane, click **Instances**.
4. In the instance list, view the **instance ID**.

**Response parameters**

After you call a List API operation related to cloud service resource instances, the system returns the following parameters by default.

| Name | Description |
|---|---|

tions

| ResourceGroupName | The name of the resource set. |
|---|---|
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

### 1.3 Obtain an AccessKey pair

AccessKey pairs are classified into AccessKey pairs assigned by Resource Access Management (RAM) and those assigned by Security Token Service (STS). You can use either type of AccessKey pair for authentication when you call operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. You can use RAM or STS to assign an AccessKey pair for authentication. Use RAM to assign an AccessKey ID and an AccessKey secret to a third party. Use STS to assign an AccessKey ID, an AccessKey secret, and a security token to a third party. For more information, see Obtain an AccessKey pair assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only operations administrators and the administrators of level-1 organizations can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

> **Warning:** The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide. |

tions

| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |
|---|---|

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, click the profile picture and then click **User**
**Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of your account.

> **Note:** An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. Click **Management Accesskey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### 1.4 Obtain access credentials assigned by STS

**assigned by STS**

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

STS allows you to manage temporary access credentials for your Apsara Stack resources. You can use STS to call API operations.

**Procedure**

1. Obtain the Apsara Stack Resource Name (ARN) of your `Resource Access Management (RAM)`
`role` . i. Log on to the Apsara Uni-manager Management Console. tions ii. In the upper-right corner of the homepage, click the profile picture and then click **User**
**Information**.
iii. On the page that appears, click **View Current Role Policy**.

| RAM role . |   |
|---|---|
| cret ( | stsSK |

In the **View Policies of Current Role** dialog box, view the ARN of your `RAM role` .
2. Use the following code to obtain an AccessKey ID ( `stsAK` ), AccessKey secret ( `stsSK` ), and
STS token ( `stsToken` ) by assuming the `RAM role` .

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
3. Use the access credentials assigned by STS to call an API operation of a cloud service. In this
example, the Elastic Compute Service (ECS) API is used. tions

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
        asClient.setSdkSource("test");
  // Call an API operation of ECS.
        String ecsRes = DescribeZones(asClient,<stsAK>,<stsSK>,<stsToken>);
```

`}`

```
public static String DescribeZones(ASClient asClient, String stsAK, String stsSK, String stsToken) {
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

`}` P to make API calls

## 2 Use POP to make API calls

### 2.1 SDK for Java

Before you use an SDK for Java to call the API of a cloud service over the point of presence (POP) gateway, you must check the style of the service API. A service API can be of the Remote Procedure Call (RPC) or Resource-Oriented Architecture (ROA) style.

**Usage notes**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample Code** in the top navigation bar.

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues. Proceed with caution. The following sample code provides an example on how to call RPC APIs. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");
        // Ignore SSL certificate validation.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the connection timeout period.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and specify the request parameters.
        CommonRequest request = new CommonRequest();
//Specifytherequestmethod.
```

P to make API calls

```java
        // Specify the request method.
        request.setSysMethod(MethodType.POST);
        // Specify the service endpoint.
        request.setSysDomain("<apigatewayEndpoint>");
        // Specify the API version.
        request.setSysVersion("2016-07-14");
        // Specify the service code.
        request.setSysLocationProduct("apigateway");
        // Specify the name of the API operation.
        request.setSysAction("DescribeApiGroups");
        // If you use Security Token Service (STS) to call RPC API operations, you must spec
ify the SecurityToken parameter.
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");
        // Specify service-related parameters.
        request.putQueryParameter("PageSize", "10");
        request.putQueryParameter("PageNumber", "1");
        // Required. The call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0 and
earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. The instance ID. This parameter is required for modify and delete opera
tions.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
        try {
            // Initiate the request and handle the response or exceptions.
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

`}` `}` `}` The following sample code provides an example on how to call ROA APIs. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06-07. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException;
```

P to make API calls

```java
import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");
        // Ignore SSL certificate validation.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the connection timeout period.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and specify the request parameters.
        CommonRequest request = new CommonRequest();
        // Set the request protocol to HTTPS.
        request.setSysProtocol(ProtocolType.HTTP);
        // Specify the request method.
        request.setSysMethod(MethodType.GET);
        // Specify the service endpoint.
        request.setSysDomain("<crEndpoint>");
        // Specify the API version.
        request.setSysVersion("2016-06-07");
        // Specify the uriPattern parameter, which is required for ROA APIs.
        request.setSysUriPattern("/namespace");
        // Specify the service code.
        request.setSysLocationProduct("cr");
        // Specify the name of the API operation.
        request.setSysAction("GetNamespaceList");
        // Required. The call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0 and
earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. The instance ID. This parameter is required for modify and delete opera
tions.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
        // If you use access credentials assigned by STS to call ROA API operations, you
must add the x-acs-security-token field to the header.
        // request.putHeadParameter("x-acs-security-token", "<your-securitytoken>");
        try {
```

P to make API calls

```java
            // Initiate the request and handle the response or exceptions.
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

`}` `}` `}`

> **Important:** By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported.
> To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be ignored in the test environment, you can specify the following setting:

Java

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Disable certificate verification for the client. clientConfig.setIgnoreSSLCerts(true)
```

### 2.2 SDK for Go

This topic describes how to use SDK for Go over the point of presence (POP) gateway.

**Usage notes**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample Code** in the top navigation bar.

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues. Proceed with caution.

**Background information**

Remote Procedure Call (RPC) and Resource-Oriented Architecture (ROA) APIs are supported. The following sample code provides an example on how to call RPC APIs. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. P to make API calls Sample code:

```java
package main import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-RegionID>", "<AccessKey ID>", "<AccessK
ey Secret>")
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<ApigatewayEndpoint>"
    request.Version = "2016-07-14"
    request.ApiName = "DescribeApiGroups"
    request.Product = "apigateway"
    // If you use Security Token Service (STS) to call RPC API operations, you must specify
the SecurityToken parameter.
    // request.QueryParams["SecurityToken"]="<your-SecurityToken>"
    // Required. The call source.
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0 and
earlier.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource set ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
    // Optional. The instance ID. This parameter is required for modify and delete
operations.
    // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}` The following sample code provides an example on how to call ROA APIs. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06-07. Sample code: P to make API calls

```java
package main import (
 "fmt"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
 "os"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-regionid>", "<yourAccessKeyId>", "<your
AccessSecret>")
 request := requests.NewCommonRequest()
 request.Method = "GET"
 request.Domain = "<crEndpoint>"
 request.Version = "2016-06-07"
 request.ApiName = "GetNamespaceList"
 request.Product = "cr"
 request.PathPattern = "/namespace"
 // If you use STS to call ROA API operations, you must specify the x-acs-security-token he
ader.
 // request.Headers["x-acs-security-token"] = "<your-SecurityToken>"
 // Required. The call source.
 request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0 and
earlier.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource set ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
 // Optional. The instance ID. This parameter is required for modify and delete operations.
 // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
 response, err := client.ProcessCommonRequest(request)
 if err != nil {
  panic(err)
```

`}`

```
 fmt.Print(response.GetHttpContentString())
```

`}`

**Proxy configuration**

You can configure proxies for API calls in one of the following ways: Configure proxies by using environment variables. Set the HTTP_PROXY, HTTPS_PROXY, or NO_PROXY environment variable. Sample code: P to make API calls

```java
import (
    "os"
```

`)`

```
func main(){
 os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // Set the HTTP_PROXY environment
variable.
 os.Setenv("HTTPS_PROXY", "https://x.x.x.x:xxxx") // Set the HTTPS_PROXY environment
variable.
```

`}` Configure proxies on the client. Sample code:

```
// The proxies that are configured on the client take precedence over those that are configured by using environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Configure the HTTP proxy. client.GetHttpProxy() // Query the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Configure the HTTPS proxy. client.GetHttpsProxy() // Query the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Configure the proxy whitelist. client.GetNoProxy() // Query the proxy whitelist.
```

**SSL verification**

You can configure SSL verification for requests. If you set the HTTPSInsecure parameter to `true` , certificate verification is disabled. To ensure connection security, we recommend that you enable certificate verification. If you set the HTTPSInsecure parameter to `false` , certificate verification is enabled. By default, certificate authority (CA) certificates on the operating systems are used.

**Default value**

```
 false
```

**Configuration methods**

> **Important:** By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be ignored in the test environment, you can specify the following settings:

```
// If you configure the HTTPSInsecure parameter for a request, the setting takes effect only on the current request. request.SetHTTPSInsecure(true) // Set the HTTPSInsecure parameter t o true for the request. isInsecure := request.GetHTTPSInsecure() // Query the setting of the HTTPSInsecure parameter for the request.
```

P to make API calls If you do not configure the HTTPSInsecure parameter for a request, the setting for a client takes effect.

```
// If you configure the HTTPSInsecure parameter for the client, the setting takes effect on all requests that are initiated by the client. client.SetHTTPSInsecure(true) // Set the HTTPSInsecure parameter to t rue for the client. isInsecure := client.GetHTTPSInsecure() // Query the setting of the HTTPSInsecure parameter for the client.
```

### 2.3 SDK for Python

This topic describes how to use SDK for Python over the point of presence (POP) gateway.

**Usage notes**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample Code** in the top navigation bar.

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues.Proceed with caution.

**Background information**

Only remote procedure call (RPC) APIs are supported. The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

```java
from aliyunsdkcore.client import AcsClient import os from aliyunsdkcore.request import CommonRequest
# Create an AcsClient instance.
client = AcsClient(
    "<AccessKey ID>",
    "<AccessKey Secret>",
    "<your-RegionID>",
    timeout=1000,  # Specify the timeout period.
    verify=False, # Disable SSL certificate verification. To enable SSL certificate verifica
tion, specify verify='<The path of the certificate>'.
```

);

```python
# Set the following parameters for the HTTPS request protocol:
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def describe_api_groups():
```

P to make API calls

```bash
    # Create an API request and specify the required parameters.
    request = CommonRequest()
    # If you use Security Token Service (STS) to call RPC API operations, you must specify
the SecurityToken parameter.
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-SecurityToken>"};
    params = {"PageSize":"10","PageNumber":"1"};
    request.set_query_params(params)
    headers = {
        # Required. The call source.
        "x-acs-caller-sdk-source":"ApiTestDemo",
        # Optional. The region ID. This parameter is required for Apsara Stack Enterprise Ed
ition V3.15.0 and earlier.
        "x-acs-regionid":"<your-RegionID>",
        # Optional. The resource set ID.
        "x-acs-resourcegroupid":"<your-ResourceGroupID>",
        # Required. The organization ID.
        "x-acs-organizationid":"<your-OrganizationID>"
        # Optional. The instance ID. This parameter is required for modify and delete
operations.
        # "x-acs-instanceid":"<your-InstanceID>"
```

`}`

```python
    request.set_headers(headers)
    request.set_version("2016-07-14")
    request.set_action_name("DescribeApiGroups")
    request.set_endpoint("<ApigatewayEndpoint>")   // Replace <ApigatewayEndpoint> with the
actual endpoint.
    request.set_product("apigateway")
    request.set_method("POST")
    # Initiate the API request and display the response.
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    describe_api_groups()
```

**Proxy configuration**

You can configure a proxy for API calls by setting the HTTP_PROXY or HTTPS_PROXY environment variable. Sample code:

```bash
# Configure the HTTPS proxy.
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# Configure the HTTP proxy.
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

**HTTPS configuration**

This section describes related configurations for sending API requests over HTTPS. P to make API calls

**Use HTTPS**

By default, the SDKs use HTTPS as the request protocol.

```
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # The region ID.
```

`)`

```
request = DescribeInstancesRequest() request.set_protocol_type('https') # Set the protocol to HTTPS. client.do_action_with_exception(request)
```

**Disable certificate verification**

> **Important:** By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported.
> To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be ignored in the test environment, you can set the `verify` parameter to false.

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # The region ID.
    verify=False  # Disable SSL certificate verification.
```

`)`

**Enable certificate verification**

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # The region ID.
    verify='./cacert.pem'  # The path of the certificate authority (CA) certificate.
```

`)`

## 3 AppManager API

### 3.1 Definition

#### 3.1.1 CommitDeploymentDraft

Use the CommitDeploymentDraft API to publish a deployment. After publishing, you can manage it.

**Request parameters**

Request path: POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/[deploymentDraftId]/commit

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| workspace | workspace | Normal | String | Path | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| paramsJson | paramsJson | Normal | String | Body | No |
| deploymentDr aftId | deploymentDr aftId | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type | Output null values | Backend parameter |
|---|---|---|---|---|
| data | Normal | String | No | data |
| requestId | Normal | String | No | requestId |
| success | Normal | Boolean | No | success |

#### 3.1.2 CreateDeployment

Use the CreateDeployment API to create a deployment.

**Request parameters**

Request path: /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments

| Parameter | Backend parameter | Structure type | Type | Position |
|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host |
| namespace | namespace | Normal | String | Path |
| paramsJson | paramsJson | Normal | String | Body |
| workspace | workspace | Normal | String | Path |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |
| data | Normal | String |

**HTTP request example**

Request body `{`

```json
    "spec": {
        "template": {
            "spec": {
                "artifact": {
                    "kind": "JAR",
                    "jarUri": "oss://qiqi-
zp/multioss/artifacts/namespaces/test/TopSpeedWindowing.jar",
                    "entryClass": null,
                    "mainArgs": null,
                    "flinkVersion": "1.11",
                    "flinkImageTag": "1.11.1-vvr-2.0.1"
```

`},`

```json
                "parallelism": 1,
                "resources": {
                    "jobmanager": {
                        "cpu": 1,
                        "memory": "1G"
```

`},`

```json
                    "taskmanager": {
                        "cpu": 1,
                        "memory": "2G"
```

`}` `},`

```json
                "logging": {
                    "loggingProfile": "default",
                    "log4jLoggers": {
                        "": "INFO"
```

`}` `},`

```json
                "flinkConfiguration": {
                    "execution.checkpointing.interval": "10s",
                    "execution.checkpointing.externalized-checkpoint-retention": "RETAIN_ON_C
ANCELLATION"
```

`}` `}` `},`

```json
        "deploymentTargetId": "3965ca94-2fa9-47ee-818b-ff89ddf4ba4f",
        "state": "CANCELLED",
        "upgradeStrategy": {
            "kind": "STATEFUL"
```

`},`

```json
        "restoreStrategy": {
            "kind": "LATEST_STATE",
            "allowNonRestoredState": false
```

`},`

```json
        "maxSavepointCreationAttempts": 4,
        "maxJobCreationAttempts": 4
```

`},`

```json
    "metadata": {
        "name": "lxg-test"
```

`}` `}`

#### 3.1.3 CreateDeploymentDraft

Use the CreateDeploymentDraft API to create a deployment draft.

**Request parameters**

Request path: POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| workspace | workspace | Normal | String | Path | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| paramsJson | paramsJson | Normal | String | Body | No |

**Response parameters**

| Parameter | Structure type | Data type | Output null values | Backend parameter |
|---|---|---|---|---|
| data | Normal | String | No | data |
| requestId | Normal | String | No | requestId |
| success | Normal | Boolean | No | success |

#### 3.1.4 CreateFolder

Use the CreateFolder API to create a folder. You can create drafts within the folder.

**Request parameters**

Request path: POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| workspace | workspace | Normal | String | Path | Yes |

| namespace | namespace | Normal | String | Path | Yes |
|---|---|---|---|---|---|
| paramsJson | paramsJson | Normal | String | Body | No |

**Response parameters**

| Parameter | Structure type | Data type | Output null values | Backend parameter |
|---|---|---|---|---|
| data | Normal | String | No | data |
| requestId | Normal | String | No | requestId |
| success | Normal | Boolean | No | success |

#### 3.1.5 CreateSavepoint

Use the CreateSavepoint API to manually create a savepoint for a running deployment.

**Request parameters**

Request path: /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/savepoints

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Header | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| paramsJson | paramsJson | Normal | String | Body | No |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |
| data | Normal | String |

**HTTP request example**

Request body `{`

```json
    "metadata": {
        "deploymentId": "367d6a04-319c-4110-9a94-911addc6522e"
```

`}` `}`

#### 3.1.6 CreateSessionCluster

Use the CreateSessionCluster API to create a session cluster.

**Request parameters**

Request path: POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/sessionclusters

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| workspace | workspace | Normal | String | Path | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| paramsJson | paramsJson | Normal | String | Body | No |

**Response parameters**

| Parameter | Structure type | Data type | Output null values | Backend parameter |
|---|---|---|---|---|
| data | Normal | String | No | data |
| requestId | Normal | String | No | requestId |
| success | Normal | Boolean | No | success |

#### 3.1.7 DeleteArtifact

Use the DeleteArtifact API to delete the target data file.

**Request parameters**

Request path: /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:delete

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|

| RegionId | RegionId | Normal | String | Host | Yes |
|---|---|---|---|---|---|
| namespace | namespace | Normal | String | Path | Yes |
| filename | filename | Normal | String | Query | Yes |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |

**HTTP request example**

Request body

```
filename: frauddetection-0.1.jar
```

#### 3.1.8 DeleteDeployment

Use the DeleteDeployment API to delete a job that is not running.

**Request Parameters**

Request path: /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| deploymentId | deploymentId | Normal | String | Path | Yes |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Type |
|---|---|---|
| requestId | Normal | String |

#### 3.1.9 DeleteFolder

Call DeleteFolder to delete a folder on the data development page.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request syntax**

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders/[folderId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env188-d01 | The name of the region. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain this ID in one of the following ways: By calling ListNamespaces. From the workspace details page in the fully managed Flink development console. |
| namespace | Strin g | Path | Yes | flinkteam | The name of the project space where the job resides. |
| folderId | Strin g | Path | Yes | 123 | The ID of the folder. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The ID of the request. |
| success | Boolean | true | Indicates whether the request succeeded. |

Sample requests

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders/[folderId] HTTP/1.1 &RegionId=cn-wulan-env188-d01 &workspace=default &namespace=flinkteam &folderId=123 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

ververica 2020-05-01

#### 3.1.10 DeleteSessionCluster

Use the DeleteSessionCluster API to delete a session cluster that is not running.

**Request parameters**

Request path: DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/sessionclusters/[name]

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| workspace | workspace | Normal | String | Path | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| name | name | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type | Output null values | Backend parameter |
|---|---|---|---|---|

| requestId | Normal | String | No | requestId |
|---|---|---|---|---|
| success | Normal | Boolean | No | success |

#### 3.1.11 ExecuteSqlScript

Use the ExecuteSqlScript API to execute SQL statements.

**Request parameters**

Request path: /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:execute

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| paramsJson | paramsJson | Normal | String | Body | No |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |
| data | Normal | String |

**HTTP request example**

Request body `{`

```json
    "statement": "CREATE TABLE RANDOM_TABLE01(`name` STRING) with
('connector.type'='random','type'='random')"
```

`}`

#### 3.1.12 GetArtifactMetadata

Use the GetArtifactMetadata API to view resource information by file name.

**Request parameters**

Request path: /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:getMetadata

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| filename | filename | Normal | String | Query | Yes |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |
| data | Normal | String |

#### 3.1.13 GetFolderById

Use the GetFolderById API to view subfolders under a specific folder and job drafts under those subfolders by its ID.

**Request parameters**

Request path: GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders/[folderId]

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| workspace | workspace | Normal | String | Path | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| folderId | folderId | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type | Output null values | Backend parameter |
|---|---|---|---|---|
| data | Normal | String | No | data |
| requestId | Normal | String | No | requestId |
| success | Normal | Boolean | No | success |

#### 3.1.14 GetRootFolderByType

Use the GetRootFolderByType API to view all subfolders under the root folder and job drafts under those subfolders, based on the folder type.

**Request parameters**

Request path: GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders/roots/[type]

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| workspace | workspace | Normal | String | Path | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| type | type | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type | Output null values | Backend parameter |
|---|---|---|---|---|
| data | Normal | String | No | data |
| requestId | Normal | String | No | requestId |
| success | Normal | Boolean | No | success |

#### 3.1.15 GetDeployment

Use the GetDeployment API to view job information by job ID.

**Request parameters**

Request Path: /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| deploymentId | deploymentId | Normal | String | Path | Yes |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |
| data | Normal | String |

#### 3.1.16 GetDeploymentDefaults

Use the GetDeploymentDefaults API to retrieve the default configuration for jobs in the current project workspace.

**Request parameters**

Request path: /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdefaults

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|

| requestId | Normal | String |
|---|---|---|
| data | Normal | String |

#### 3.1.17 GetGlobalDeploymentDefaults

Use the GetGlobalDeploymentDefaults API to retrieve the default configuration information for jobs in the current cluster.

**Request parameters**

Request path: /pop/workspaces/[workspace]/api/v1/global-deployment-defaults

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| namespace | namespace | Normal | String | Header | Yes |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |
| data | Normal | String |

#### 3.1.18 GetSessionClusterByName

Use the GetSessionClusterByName API to retrieve information about a session cluster by its name.

**Request parameters**

Request path: GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/sessionclusters/[name]

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| workspace | workspace | Normal | String | Path | Yes |

| namespace | namespace | Normal | String | Path | Yes |
|---|---|---|---|---|---|
| name | name | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type | Output null values | Backend parameter |
|---|---|---|---|---|
| data | Normal | String | No | data |
| requestId | Normal | String | No | requestId |
| success | Normal | Boolean | No | success |

#### 3.1.19 ListArtifacts

Use the ListArtifacts API to view the list of artifacts.

**Request parameters**

Request path: /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:list

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |
| data | Normal | String |

#### 3.1.20 ListDeployments

Use the ListDeployments API to view the job list.

**Request parameters**

Request path: /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |
| data | Normal | String |

#### 3.1.21 ListDeploymentTargets

Use the ListDeploymentTargets API to view the list of job deployment targets.

**Request parameters**

Request path: /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-targets

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |
| data | Normal | String |

#### 3.1.22 ListJobs

Use the ListJobs API to view the list of jobs under a deployment by specifying the DeploymentId.

**Request Parameters**

Request Path: /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/jobs

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| deploymentId | deploymentId | Normal | String | Query | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |
| data | Normal | String |

#### 3.1.23 ListNamespaces

Use the ListNamespaces API to view the list of project spaces.

**Request parameters**

Request path: /pop/namespaces/v1/namespaces

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |

| data | Normal | String |
|---|---|---|

#### 3.1.24 ListDeploymentDrafts

Use the ListDeploymentDrafts API to view a list of job drafts.

**Request parameters**

Request path: GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| workspace | workspace | Normal | String | Path | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| light | light | Normal | Boolean | Query | Yes |

**Response parameters**

| Parameter | Structure type | Data type | Output empty values | Backend parameter |
|---|---|---|---|---|
| data | Normal | String | No | data |
| requestId | Normal | String | No | requestId |
| success | Normal | Boolean | No | success |

#### 3.1.25 ListSavepoints

Use the ListSavepoints API to view the Savepoint list for a target job based on its DeploymentId.

**Request Parameters**

Request Path: /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/savepoints

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |

| namespace | namespace | Normal | String | Path | Yes |
|---|---|---|---|---|---|
| deploymentId | deploymentId | Normal | String | Query | Yes |
| jobId | jobId | Normal | String | Query | No |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |
| data | Normal | String |

#### 3.1.26 ListSessionClusters

Use the ListSessionClusters API to view the list of session clusters.

**Request parameters**

Request path: GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/sessionclusters

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| workspace | workspace | Normal | String | Path | Yes |
| namespace | namespace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type | Output null values | Backend parameter |
|---|---|---|---|---|
| data | Normal | String | No | data |
| requestId | Normal | String | No | requestId |
| success | Normal | Boolean | No | success |

#### 3.1.27 UpdateDeployment

Use the UpdateDeployment API to modify a job and perform related operations.

**Request parameters**

Request Path: /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/patch

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| deploymentId | deploymentId | Normal | String | Path | Yes |
| paramsJson | paramsJson | Normal | String | Body | No |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |
| data | Normal | Integer |

**HTTP request example**

Request body `{`

```json
    "kind": "Deployment",
    "apiVersion": "v1",
    "metadata": {
        "id": "8711257b-f51f-4c71-a5c2-b9ea62466540",
        "name": "lxg-sdk-test-4",
        "namespace": "test",
        "createdAt": "2020-09-23T22:11:09Z",
        "modifiedAt": "2020-09-23T22:11:09Z",
        "labels": {},
        "annotations": {
            "creator": "vvp_pe",
            "com.dataartisans.appmanager.controller.deployment.spec.version": "1",
            "priority": "5",
            "com.dataartisans.appmanager.controller.deployment.transitioning.since": "160089
9068676",
```

```json
            "modifier": "vvp_pe",
            "com.dataartisans.appmanager.controller.deployment.transitioning": "true"
```

`},`

```json
        "resourceVersion": 15
```

`},`

```json
    "spec": {
        "state": "RUNNING",
        "upgradeStrategy": {
            "kind": "STATEFUL"
```

`},`

```json
        "restoreStrategy": {
            "kind": "LATEST_STATE",
            "allowNonRestoredState": false
```

`},`

```json
        "deploymentTargetId": "3965ca94-2fa9-47ee-818b-ff89ddf4ba4f",
        "maxSavepointCreationAttempts": 4,
        "maxJobCreationAttempts": 4,
        "template": {
            "metadata": {
                "annotations": {
                    "flink.security.ssl.enabled": "false",
                    "flink.queryable-state.enabled": "false"
```

`}` `},`

```json
            "spec": {
                "artifact": {
                    "kind": "JAR",
                    "jarUri": "oss://qiqi-zp/multioss/artifacts/namespaces/test/job-1.0-
SNAPSHOT2.jar",
                    "flinkVersion": "1.11",
                    "flinkImageRegistry": "reg.docker.alibaba-inc.com/bigdata-k8s",
                    "flinkImageRepository": "flink",
                    "flinkImageTag": "1.11.1-vvr-2.0.1",
                    "entryClass": null,
                    "mainArgs": null
```

`},`

```json
                "parallelism": 2,
                "resources": {
                    "jobmanager": {
                        "cpu": 1,
                        "memory": "1G"
```

`},`

```json
                    "taskmanager": {
                        "cpu": 1,
                        "memory": "2G"
```

`}` `},`

```json
                "flinkConfiguration": {
                    "execution.checkpointing.interval": "10s",
                    "execution.checkpointing.externalized-checkpoint-retention": "RETAIN_ON_C
ANCELLATION",
                    "execution.checkpointing.min-pause": "10s"
```

`},`

```json
                "logging": {
                    "loggingProfile": "default",
                    "log4jLoggers": {
                        "": "INFO"
```

`}` `}` `}` `}` `},`

```json
    "status": {
        "state": "RUNNING",
        "running": {
            "jobId": "0e39214f-97d6-4c02-a696-4a42ecce8398",
            "transitionTime": "2020-09-23T22:11:54.049905Z",
            "conditions": [
```

`{`

```json
                    "type": "ClusterUnreachable",
                    "status": "False",
                    "message": "Job last observed in RUNNING status.",
                    "reason": "FlinkJobStatusOk",
                    "lastTransitionTime": "2020-09-23T22:11:57.483262Z",
                    "lastUpdateTime": "2020-09-23T22:11:57.483262Z"
```

`},` `{`

```json
                    "type": "JobFailing",
                    "status": "False",
                    "message": "Observed less than 3 Flink job restarts (0) in the last 10 m
inutes.",
                    "reason": "BelowThreshold",
                    "lastTransitionTime": "2020-09-24T09:13:19.793986Z",
                    "lastUpdateTime": "2020-09-24T09:13:19.793986Z"
```

`},` `{`

```json
                    "type": "JobUnstable",
                    "status": "False",
                    "message": "Observed less than 3 Flink job restarts (0) in the last 60 m
inutes.",
                    "reason": "BelowThreshold",
                    "lastTransitionTime": "2020-09-24T09:13:19.793986Z",
                    "lastUpdateTime": "2020-09-24T09:13:19.793986Z"
```

`}` `]` `}` `}` `}`

#### 3.1.28 UpdateDeploymentDesiredState

Use the UpdateDeploymentDesiredState API to modify the running status of a job. This API enables you to manage the status of jobs.

**Request parameters**

Request path: /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/state

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|

| RegionId | RegionId | Normal | String | Host | Yes |
|---|---|---|---|---|---|
| namespace | namespace | Normal | String | Path | Yes |
| deploymentId | deploymentId | Normal | String | Path | Yes |
| paramsJson | paramsJson | Normal | String | Body | No |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |
| data | Normal | String |

**HTTP request example**

Request body `{`

```json
    "spec": {
        "state": "RUNNING"
```

`}` `}`

#### 3.1.29 UpdateDeploymentDraft

Use the UpdateDeploymentDraft API to modify a job draft. This API enables you to manage a job.

**Request parameters**

Request path: PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/[deploymentDraftId]/patch

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| workspace | workspace | Normal | String | Path | Yes |
| namespace | namespace | Normal | String | Path | Yes |

| paramsJson | paramsJson | Normal | String | Body | No |
|---|---|---|---|---|---|
| deploymentDr aftId | deploymentDr aftId | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type | Output null values | Backend parameter |
|---|---|---|---|---|
| data | Normal | String | No | data |
| requestId | Normal | String | No | requestId |
| success | Normal | Boolean | No | success |

#### 3.1.30 UpdateSessionCluster

Use the UpdateSessionCluster API to modify a session cluster.

**Request parameters**

Request path: PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/sessionclusters/[name]/patch

| Parameter | Backend parameter name | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| workspace | workspace | Normal | String | Path | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| paramsJson | paramsJson | Normal | String | Body | No |
| name | name | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type | Output null value | Backend parameter name |
|---|---|---|---|---|
| data | Normal | String | No | data |

| requestId | Normal | String | No | requestId |
|---|---|---|---|---|
| success | Normal | Boolean | No | success |

#### 3.1.31 UpdateSessionClusterDesiredState

Use the UpdateSessionClusterDesiredState API to modify the running status of a session cluster. This API enables you to manage the operational status of a session cluster.

**Request parameters**

Request path: PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/sessionclusters/[name]/state

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| workspace | workspace | Normal | String | Path | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| paramsJson | paramsJson | Normal | String | Body | No |
| name | name | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type | Output null values | Backend parameter |
|---|---|---|---|---|
| data | Normal | String | No | data |
| requestId | Normal | String | No | requestId |
| success | Normal | Boolean | No | success |

#### 3.1.32 UploadArtifactByOSSUrl

Call the UpdateFolder API to update folders on the data development page.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request syntax**

```
POST /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:uploadByOSSUrl HTT P/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env188-d01 | The name of the region. |
| namespace | Strin g | Path | Yes | flinkteam | The name of the project space where the job resides. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain it in one of the following ways: By calling ListNamespaces. From the workspace details page in the fully managed Flink console. |
| paramsJson | Strin g | Body | No | { "name": "namespaces/flinkteam/for mats/customized-csv", "type": "customized-csv", "source": true, "sink": false, "properties": [ { "key": "format.column-delimiter", "required": false, "defaultValue": ",", "description": "" } ], "dependencies": [ "hdfs:///tmp/myformats/cus tomized-csv-demo-1.0- SNAPSHOT.jar" ] } | The execution parameters in the SQL script form. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The ID of the request. |
| data | String | { "success": true, "message": "", "plan": "" } | The detailed information. |

| success | Boolean | true | Indicates whether the request succeeded. |
|---|---|---|---|

Sample requests

```
POST /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:uploadByOSSUrl HTT P/1.1
```

`{`

```json
"RegionId":"cn-wulan-env188-d01", "namespace":"flinkteam", "workspace":"default"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{  \"success\": true,  \"message\": \"\",  \"plan\": \"\"}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data>{
  &quot;success&quot;: true,
  &quot;message&quot;: &quot;&quot;,
  &quot;plan&quot;: &quot;&quot;
}</data>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <success>true</success>
```

ververica 2020-05-01

#### 3.1.33 UpdateFolder

Call UpdateFolder to update a folder on the data development page.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request syntax**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders/[folderId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | UpdateFolder | The system-specified parameter. |
| RegionId | Strin g | Host | Yes | cn-wulan-env188-d01 | The name of the region. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the workspace ID in one of the following ways: By calling ListNamespaces. From the workspace details page in the fully managed Flink console. |
| namespace | Strin g | Path | Yes | flinkteam | The name of the project space where the job resides. |
| folderId | Strin g | Path | Yes | 123 | The ID of the folder. |
| paramsJson | Strin g | Body | No | { "name": "namespaces/flinkteam/for mats/customized-csv", "type": "customized-csv", "source": true, "sink": false, "properties": [ { "key": "format.column- delimiter", "required": false, "defaultValue": ",", "description": "" } ], "dependencies": [ "hdfs:///tmp/myformats/cu stomized-csv-demo-1.0- SNAPSHOT.jar" ] } | The execution parameters in the SQL script form. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request succeeded. |
| data | String | { "success": true, "message": "", "plan": "" } | The detailed information. |

| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The ID of the request. |
|---|---|---|---|

Sample requests

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders/[folderId] HTTP/1.1
```

`{`

```json
"Action":"UpdateFolder", "RegionId":"cn-wulan-env188-d01", "workspace":"default", "namespace":"flinkteam", "folderId":"123"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{  \"success\": true,  \"message\": \"\",  \"plan\": \"\"}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
```

`}` `XML` format

```xml
<data>{
  &quot;success&quot;: true,
  &quot;message&quot;: &quot;&quot;,
  &quot;plan&quot;: &quot;&quot;
}</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

ververica 2020-05-01

#### 3.1.34 ValidateSqlScript

Use the ValidateSqlScript API to validate SQL statements.

**Request parameters**

Request path: /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:validate

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|

| RegionId | RegionId | Normal | String | Host | Yes |
|---|---|---|---|---|---|
| namespace | namespace | Normal | String | Path | Yes |
| paramsJson | paramsJson | Normal | String | Body | No |
| workspace | workspace | Normal | String | Path | Yes |

**Response parameters**

| Parameter | Structure type | Data type |
|---|---|---|
| requestId | Normal | String |
| data | Normal | String |

**HTTP request example**

Request body `{`

```json
    "statement": "CREATE TABLE RANDOM_TABLE02(`name` STRING) with
('connector.type'='random','type'='random')"
```

`}`

#### 3.1.35 ValidateDeploymentDraft

Use the ValidateDeploymentDraft API to validate SQL statements in a draft.

**Request parameters**

Request path: POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/validate

| Parameter | Backend parameter | Structure type | Type | Position | Required |
|---|---|---|---|---|---|
| RegionId | RegionId | Normal | String | Host | Yes |
| workspace | workspace | Normal | String | Path | Yes |
| namespace | namespace | Normal | String | Path | Yes |
| paramsJson | paramsJson | Normal | String | Body | No |

**Response parameters**

| Parameter | Structure type | Data type | Output null values | Backend parameter |
|---|---|---|---|---|
| data | Normal | String | No | data |
| requestId | Normal | String | No | requestId |
| success | Normal | Boolean | No | success |

#### 3.1.36 ListTables

Queries a list of tables in a catalog.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listTables HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | ververica | The name of the namespace to which the deployment belongs. |
| cat | String | Path | Yes | vvp | The name of the catalog. |

|   |   |   |   |   | nk (Co Editio | mpute-Storage Separation n) Developer Guide·AppM nager AP | a I |
|---|---|---|---|---|---|---|---|

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| database | String | Query | Yes | default | The name of the database in the catalog. |
| RegionId | String | Host | Yes | cn-wulan-env230-d01 | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | 202107221428- KKE3K857WS | The request ID. |
| data | String | {"tables": [{"name":"blackhole ","schema": {"column": [{"name":"id","type" :"VARCHAR(214748 3647)","expression": ""}],"watermarkSpe c":[]},"properties": {"connector":"black hole"},"comment":" "}, {"name":"blackhole sink","schema": _ {"column": [{"name":"name","t ype":"VARCHAR(214 7483647)","expressi on":""}, {"name":"score","ty pe":"BIGINT","expre ssion":""}],"waterm arkSpec": []},"properties": {"connector":"black hole"},"comment":" blackhole sink table"}]} | The detailed information. |

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listTables HTTP/1.1
```

Sample success responses `JSON` format `{`

```json
  "requestId": "202107221428-KKE3K857WS",
  "success": true,
  "data": {
    "tables": [
```

`{`

```json
        "name": "blackhole",
        "schema": {
          "column": [
```

`{`

```json
              "name": "id",
              "type": "VARCHAR(2147483647)",
              "expression": ""
```

`}` `],`

```json
          "watermarkSpec": []
```

`},`

```json
        "properties": {
          "connector": "blackhole"
```

`},`

```json
        "comment": ""
```

`},` `{`

```json
        "name": "blackhole_sink",
        "schema": {
          "column": [
```

`{`

```json
              "name": "name",
              "type": "VARCHAR(2147483647)",
              "expression": ""
```

`},` `{`

```json
              "name": "score",
              "type": "BIGINT",
              "expression": ""
```

`}` `],`

```json
          "watermarkSpec": []
```

`},`

```json
        "properties": {
          "connector": "blackhole"
```

`},`

```json
        "comment": "blackhole sink table"
```

`}` `]` `}` `}` `XML` format

```xml
<requestId>202107221428-KKE3K857WS</requestId> <success>true</success> <data>
 <tables>
  <name>blackhole</name>
  <schema>
   <column>
    <name>id</name>
    <type>VARCHAR(2147483647)</type>
    <expression  />
   </column>
   <watermarkSpec  />
  </schema>
  <properties>
   <connector>blackhole</connector>
  </properties>
  <comment  />
 </tables>
 <tables>
  <name>blackhole_sink</name>
  <schema>
   <column>
    <name>name</name>
    <type>VARCHAR(2147483647)</type>
    <expression  />
   </column>
   <column>
    <name>score</name>
    <type>BIGINT</type>
    <expression  />
   </column>
   <watermarkSpec  />
  </schema>
  <properties>
   <connector>blackhole</connector>
  </properties>
  <comment>blackhole sink table</comment>
 </tables>
</data>
```

#### 3.1.37 ListCatalogs

Queries a list of catalogs in a namespace in a workspace.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | String | Path | Yes | ververica | The name of the namespace to which the deployment belongs. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | {"@type":"type.goo gleapis.com/vvp.sql. catalog.v1beta2.List CatalogsResponse", "catalogs": [{"name":"namespa ces/flinkteam/catalo gs/vvp","properties" : {"defaultDatabase": "default","type":"vvp "}}]} | The detailed data. |
| requestId | String | 31F99ADC-B72E- 4BA1-AD32- B938D5A57532 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs HTTP/1.1 &RegionId= &namespace= &workspace= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "requestId": "31F99ADC-B72E-4BA1-AD32-B938D5A57532",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.ListCatalogsResponse",
    "catalogs": [
```

`{`

```json
        "name": "namespaces/flinkteam/catalogs/vvp",
        "properties": {
          "defaultDatabase": "default",
          "type": "vvp"
```

`}` `}` `]` `}` `}` `XML` format

```xml
<requestId>31F99ADC-B72E-4BA1-AD32-B938D5A57532</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.ListCatalogsResponse</@type>
 <catalogs>
  <name>namespaces/flinkteam/catalogs/vvp</name>
  <properties>
   <defaultDatabase>default</defaultDatabase>
   <type>vvp</type>
  </properties>
 </catalogs>
</data>
```

#### 3.1.38 ListFunctions

Queries a list of user-defined functions (UDFs).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listFunction HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | String | Path | Yes | ververica | The name of the namespace to which the deployment belongs. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| cat | String | Path | Yes | vvp | The name of the catalog. |
| database | String | Query | Yes | default | The name of the database in the catalog. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | {"@type":"type.goo gleapis.com/vvp.sql. catalog.v1beta2.List FunctionsResponse" ,"functions": [{"name":"Timesta mpProbe","classNa me":"com.alibaba.bl ink.udtf.TimestampP robe","functionLang uage":"FUNCTION L _ ANGUAGE JAVA","fu _ nctionType":"FUNCT ION TYPE FLINK","d _ _ escription":"This is a user-defined function"}, {"name":"Transform Udtf","className":" com.alibaba.blink.u dtf.TransformUdtf"," functionLanguage":" FUNCTION LANGUA _ GE JAVA","functionT _ ype":"FUNCTION TY _ PE FLINK","descripti _ on":"This is a user- defined function"}]} | The detailed data. |
| requestId | String | 0ADBBDD0-E2E9- 4611-98C6- 6767A3AB87D2 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listFunction HTTP/1.1
```

Sample success responses `JSON` format `{`

```json
  "requestId": "0ADBBDD0-E2E9-4611-98C6-6767A3AB87D2",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.ListFunctionsResponse",
    "functions": [
```

`{`

```json
        "name": "TimestampProbe",
        "className": "com.alibaba.blink.udtf.TimestampProbe",
        "functionLanguage": "FUNCTION_LANGUAGE_JAVA",
        "functionType": "FUNCTION_TYPE_FLINK",
        "description": "This is a user-defined function"
```

`},` `{`

```json
        "name": "TransformUdtf",
        "className": "com.alibaba.blink.udtf.TransformUdtf",
        "functionLanguage": "FUNCTION_LANGUAGE_JAVA",
        "functionType": "FUNCTION_TYPE_FLINK",
        "description": "This is a user-defined function"
```

`}` `]` `}` `}` `XML` format

```xml
<requestId>0ADBBDD0-E2E9-4611-98C6-6767A3AB87D2</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.ListFunctionsResponse</@type>
 <functions>
  <name>TimestampProbe</name>
  <className>com.alibaba.blink.udtf.TimestampProbe</className>
  <functionLanguage>FUNCTION_LANGUAGE_JAVA</functionLanguage>
  <functionType>FUNCTION_TYPE_FLINK</functionType>
  <description>This is a user-defined function</description>
 </functions>
 <functions>
  <name>TransformUdtf</name>
  <className>com.alibaba.blink.udtf.TransformUdtf</className>
  <functionLanguage>FUNCTION_LANGUAGE_JAVA</functionLanguage>
  <functionType>FUNCTION_TYPE_FLINK</functionType>
  <description>This is a user-defined function</description>
 </functions>
</data>
```

#### 3.1.39 GetDatabase

Queries the information about a database in a catalog by name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getDatabase HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env230-d01 | The region ID. |
| namespac e | String | Path | Yes | ververica | The name of the namespace to which the deployment belongs. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| cat | String | Path | Yes | vvp | The name of the catalog. |
| database | String | Query | Yes | default | The name of the database. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | {"@type":"type.goo gleapis.com/vvp.sql. catalog.v1beta2.Get DatabaseResponse", "database": {"name":"default"," properties": {},"comment":"The default database"},"succes s":true,"message":"" } | The detailed information. |
| requestId | String | C345CF08-769F- 4C28-A60F- 6C8A30FEAFA6 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getDatabase HTTP/1.1 &RegionId= &namespace= &workspace= &cat= &database= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "requestId": "C345CF08-769F-4C28-A60F-6C8A30FEAFA6",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.GetDatabaseResponse",
    "database": {
      "name": "default",
      "properties": {},
      "comment": "The default database"
```

`},`

```json
    "success": true,
    "message": ""
```

`}` `}` `XML` format

```xml
<requestId>C345CF08-769F-4C28-A60F-6C8A30FEAFA6</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.GetDatabaseResponse</@type>
 <database>
  <name>default</name>
  <properties  />
  <comment>The default database</comment>
 </database>
 <success>true</success>
 <message  />
</data>
```

#### 3.1.40 DatabaseExists

Checks whether a database in a catalog exists.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:databaseExis HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env188-d01 | The region ID. |
| namespac e | String | Path | Yes | ververica | The name of the namespace to which the deployment belongs. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| cat | String | Path | Yes | vvp | The name of the catalog. |
| database | String | Query | Yes | default | The name of the database in the catalog. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.DatabaseExi stsResponse", "exists": true } | The detailed information. |
| requestId | String | 41CAB2BF-B428- 4240-A746- 1F6CE6DE36B3 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:databaseExis HTTP/1.1 &RegionId= &namespace= &workspace= &cat= &database= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "requestId": "41CAB2BF-B428-4240-A746-1F6CE6DE36B3",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.DatabaseExistsResponse",
    "exists": true
```

`}` `}` `XML` format

```xml
<requestId>41CAB2BF-B428-4240-A746-1F6CE6DE36B3</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.DatabaseExistsResponse</@type>
 <exists>true</exists>
</data>
```

#### 3.1.41 CreateConnector

Creates a connector.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| paramsJso n | String | Body | No | { "type": "hologres-fix", "name": "namespaces/flinkteam/c onnectors/hologres-fix", "packaged": false, "source": true, "sink": true, "lookup": true, "dependencies": [ "hdfs:///tmp/myconnector s/ververica-connector- hologres-1.15-vvr-6.0- fix.jar" ], "supportedFormats": [ "json", "csv" ], "properties": [ { "key": "connector", "required": true, "defaultValue": "hologres-fix", "description": "", "definesFormat": false }, { "key": "dbname", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "endpoint", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "tablename", "required": true, "defaultValue": "", "description": "", "definesFormat": false } ] } | The information about the connector to be created, including connector type, connector name, supported connection parameters, whether the connector can be used as the source or sink node, supported formats, and dependent JAR packages. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| data | String | { "connector": { "lookup": true, "supportedFormats" : [ "json", "csv" ], "environments": [], "sink": true, "name": "namespaces/flinkte am/connectors/holo gres-fix", "source": true, "type": "hologres-fix", "properties": [ { "defaultValue": "hologres-fix", "description": "", "definesFormat": false, "key": "connector", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "dbname", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "endpoint", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "tablename", "required": true } ], "packaged": false, "dependencies": [ "hdfs:///tmp/myconn ectors/ververica- connector-hologres- 1.15-vvr-6.0-fix.jar" ] }, "@type": "type.googleapis.co m/vvp.sql.v1beta1.C reateConnectorResp onse" } | The details of the created connector. |
| requestId | String | 86E24541-89EE- 46F9-84CE- 0EC888B9414A | The request ID. |

Sample requests

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1
```

`{`

```json
"RegionId":"", "workspace":"", "namespace":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "connector": {
      "lookup": true,
      "supportedFormats": [
        "json",
        "csv"
```

`],`

```json
      "environments": [],
      "sink": true,
      "name": "namespaces/flinkteam/connectors/hologres-fix",
      "source": true,
      "type": "hologres-fix",
      "properties": [
```

`{`

```json
          "defaultValue": "hologres-fix",
          "description": "",
          "definesFormat": false,
          "key": "connector",
          "required": true
```

`},` `{`

```json
          "defaultValue": "",
          "description": "",
          "definesFormat": false,
          "key": "dbname",
          "required": true
```

`},` `{`

```json
          "defaultValue": "",
          "description": "",
          "definesFormat": false,
          "key": "endpoint",
          "required": true
```

`},` `{`

```json
          "defaultValue": "",
          "description": "",
          "definesFormat": false,
          "key": "tablename",
          "required": true
```

`}` `],`

```json
      "packaged": false,
      "dependencies": [
        "hdfs:///tmp/myconnectors/ververica-connector-hologres-1.15-vvr-6.0-fix.jar"
```

`]` `},`

```
    "@type": "type.googleapis.com/vvp.sql.v1beta1.CreateConnectorResponse"
```

`},`

```json
  "success": true,
  "requestId": "86E24541-89EE-46F9-84CE-0EC888B9414A"
```

`}` `XML` format

```xml
<data>
 <connector>
  <lookup>true</lookup>
  <supportedFormats>json</supportedFormats>
  <supportedFormats>csv</supportedFormats>
  <environments  />
  <sink>true</sink>
  <name>namespaces/flinkteam/connectors/hologres-fix</name>
  <source>true</source>
  <type>hologres-fix</type>
  <properties>
   <defaultValue>hologres-fix</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>connector</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>dbname</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>endpoint</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>tablename</key>
   <required>true</required>
  </properties>
  <packaged>false</packaged>
  <dependencies>hdfs:///tmp/myconnectors/ververica-connector-hologres-1.15-vvr-6.0-
fix.jar</dependencies>
 </connector>
 <@type>type.googleapis.com/vvp.sql.v1beta1.CreateConnectorResponse</@type>
</data> <success>true</success> <requestId>86E24541-89EE-46F9-84CE-0EC888B9414A</requestId>
```

#### 3.1.42 CreateFormat

Creates a format.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| paramsJso n | String | Body | No | { "name": "namespaces/flinkteam/fo rmats/customized-csv", "type": "customized-csv", "source": true, "sink": false, "properties": [ { "key": "format.column- delimiter", "required": false, "defaultValue": ",", "description": "" } ], "dependencies": [ "hdfs:///tmp/myformats/cu stomized-csv-demo-1.0- SNAPSHOT.jar" ] } | The information about the format to be created. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.v1beta1.C reateFormatRespon se", "format": { "sink": false, "name": "namespaces/flinkte am/formats/customi zed-csv", "source": true, "type": "customized-csv", "properties": [ { "defaultValue": ",", "description": "", "definesFormat": false, "key": "format.column- delimiter", "required": false } ], "packaged": false, "dependencies": [ "hdfs:///tmp/myform ats/customized-csv- demo-1.0- SNAPSHOT.jar" ] } } | The details of the created format. |
| requestId | String | 0ED81455-6971- 4EBA-BBD4- 3F686175080D | The request ID. |

Sample requests

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats HTTP/1.1
```

`{`

```json
"RegionId":"", "workspace":"", "namespace":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "@type": "type.googleapis.com/vvp.sql.v1beta1.CreateFormatResponse",
    "format": {
      "sink": false,
      "name": "namespaces/flinkteam/formats/customized-csv",
      "source": true,
      "type": "customized-csv",
      "properties": [
```

`{`

```json
          "defaultValue": ",",
          "description": "",
          "definesFormat": false,
          "key": "format.column-delimiter",
          "required": false
```

`}` `],`

```json
      "packaged": false,
      "dependencies": [
        "hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar"
```

`]` `}` `},`

```json
  "success": true,
  "requestId": "0ED81455-6971-4EBA-BBD4-3F686175080D"
```

`}` `XML` format

```xml
<data>
 <@type>type.googleapis.com/vvp.sql.v1beta1.CreateFormatResponse</@type>
 <format>
  <sink>false</sink>
  <name>namespaces/flinkteam/formats/customized-csv</name>
  <source>true</source>
  <type>customized-csv</type>
  <properties>
   <defaultValue>,</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>format.column-delimiter</key>
   <required>false</required>
  </properties>
  <packaged>false</packaged>
  <dependencies>hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar</dependencies>
 </format>
</data> <success>true</success> <requestId>0ED81455-6971-4EBA-BBD4-3F686175080D</requestId>
```

#### 3.1.43 CreateMember

Grants a user permissions on a namespace.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
POST /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| paramsJson | Strin g | Body | No | { "role": "viewer", "member": "242425410145292209" } | The authorization information. Valid values of role: viewer, owner, and editor. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespace | Strin g | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| RegionId | Strin g | Host | Yes | cn-wulan-env188-d01 | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | E3D311D5-77CB- 452F-B9EA- C215C8201363 | The request ID. |

| data | String | { "@type": "type.googleapis.co m/vvp.members.v1. CreateMemberResp onse", "member": { "role": "viewer", "member": "user:24242541014 5292209" } } | The detailed authorization information. |
|---|---|---|---|

Sample requests

```
POST /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1
```

`{`

```json
"workspace":"", "namespace":"", "RegionId":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "@type": "type.googleapis.com/vvp.members.v1.CreateMemberResponse",
    "member": {
      "role": "viewer",
      "member": "user:242425410145292209"
```

`}` `},`

```json
  "success": true,
  "requestId": "E3D311D5-77CB-452F-B9EA-C215C8201363"
```

`}` `XML` format

```xml
<data>
 <@type>type.googleapis.com/vvp.members.v1.CreateMemberResponse</@type>
 <member>
  <role>viewer</role>
  <member>user:242425410145292209</member>
 </member>
</data> <success>true</success> <requestId>E3D311D5-77CB-452F-B9EA-C215C8201363</requestId>
```

ververica 2020-05-01

#### 3.1.44 CreateSecretValue

Creates a variable.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1
```

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-qingdao-env17e-d01 | The region ID. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespace | Strin g | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| paramsJson | Strin g | Body | No | { "metadata": { "name": "secretKey" }, "spec": { "kind": "Plain", "value": "secretValue" } } | The variable information, such as name and value. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| data | String | { "metadata": { "createdAt": "2024- 03- 11T03:32:51.57826 4Z", "modifiedAt": "2024-03- 11T03:32:51.57826 4Z", "resourceVersion": 1, "name": "secretKey", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "modifier": "229852610122763 813", "creatorName": "flinkadmin", "modifierName": "flinkadmin" }, "id": "6a17fb60-78df- 46f5-a6e2- 671ce61f8e6c", "labels": {} }, "apiVersion": "v1", "kind": "SecretValue", "spec": { "kind": "Plain", "value": "secretValue" } } | The detailed data. |
|---|---|---|---|
| requestId | String | 19E71203-97A1- 4355-8C25- D566CA823F95 | The request ID. |

Sample requests

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1
```

`{`

```json
"RegionId":"", "workspace":"", "namespace":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "metadata": {
      "createdAt": "2024-03-11T03:32:51.578264Z",
      "modifiedAt": "2024-03-11T03:32:51.578264Z",
      "resourceVersion": 1,
      "name": "secretKey",
      "namespace": "flinkteam",
      "annotations": {
        "creator": "229852610122763813",
        "modifier": "229852610122763813",
        "creatorName": "flinkadmin",
        "modifierName": "flinkadmin"
```

`},`

```json
      "id": "6a17fb60-78df-46f5-a6e2-671ce61f8e6c",
      "labels": {}
```

`},`

```json
    "apiVersion": "v1",
    "kind": "SecretValue",
    "spec": {
      "kind": "Plain",
      "value": "secretValue"
```

`}` `},`

```json
  "success": true,
  "requestId": "19E71203-97A1-4355-8C25-D566CA823F95"
```

`}` `XML` format

```xml
<data>
 <metadata>
  <createdAt>2024-03-11T03:32:51.578264Z</createdAt>
  <modifiedAt>2024-03-11T03:32:51.578264Z</modifiedAt>
  <resourceVersion>1</resourceVersion>
  <name>secretKey</name>
  <namespace>flinkteam</namespace>
  <annotations>
   <creator>229852610122763813</creator>
   <modifier>229852610122763813</modifier>
   <creatorName>flinkadmin</creatorName>
   <modifierName>flinkadmin</modifierName>
  </annotations>
  <id>6a17fb60-78df-46f5-a6e2-671ce61f8e6c</id>
  <labels  />
 </metadata>
 <apiVersion>v1</apiVersion>
 <kind>SecretValue</kind>
 <spec>
  <kind>Plain</kind>
  <value>secretValue</value>
 </spec>
</data> <success>true</success> <requestId>19E71203-97A1-4355-8C25-D566CA823F95</requestId>
```

ververica 2020-05-01

#### 3.1.45 CreateUdfArtifact

Creates a user-defined function (UDF).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts HTTP/1.1
```

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-*******-env***-d01 | The region ID. |
| paramsJson | Strin g | Body | No | { "name": "metric- transform-227", "jarUrl": "hdfs:///tmp/udf/metric- transform-2.2.7- shaded.jar" } | The UDF name and the path of the JAR package used to create the UDF. Make sure that the specified JAR package exists. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespace | Strin g | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| data | String | { "@type": "type.googleapis.co m/vvp.sql.v1beta1.C reateUdfArtifactRes ponse", "collidingClasses": [], "udfArtifact": { "dependencyJarUris" : [], "udfClasses": [ { "functionNames": [], "udfArtifactName": "namespaces/flinkte am/udfartifacts/metr ic-transform-227", "className": "com.alibaba.blink.u dtf.TimestampProbe ", "classType": "UDF TYPE SCALAR _ _ " }, { "functionNames": [], "udfArtifactName": "namespaces/flinkte am/udfartifacts/metr ic-transform-227", "className": "com.alibaba.blink.u dtf.TransformUdtf", "classType": "UDF TYPE TABLE" _ _ } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "createTime": "2024-03- 11T02:54:24.82276 6Z", "uploader": "229852610122763 813", "jarUpdateTime": "2024-03- 11T02:54:24.82276 6Z", "name": "namespaces/flinkte am/udfartifacts/metr ic-transform-227", "namespace": "flinkteam", "jarUrl": "hdfs:///tmp/udf/met ric-transform-2.2.7- shaded.jar", "updateTime": "2024-03- 11T02:54:24.82276 6Z" } } | The detailed information. |
|---|---|---|---|
| requestId | String | 8F0CFB56-7CE8- 45AA-A788- 41B7D2504E5F | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts HTTP/1.1
```

`{`

```json
"RegionId":"", "workspace":"", "namespace":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "@type": "type.googleapis.com/vvp.sql.v1beta1.CreateUdfArtifactResponse",
    "collidingClasses": [],
    "udfArtifact": {
      "dependencyJarUris": [],
      "udfClasses": [
```

`{`

```json
          "functionNames": [],
          "udfArtifactName": "namespaces/flinkteam/udfartifacts/metric-transform-227",
          "className": "com.alibaba.blink.udtf.TimestampProbe",
          "classType": "UDF_TYPE_SCALAR"
```

`},` `{`

```json
          "functionNames": [],
          "udfArtifactName": "namespaces/flinkteam/udfartifacts/metric-transform-227",
          "className": "com.alibaba.blink.udtf.TransformUdtf",
          "classType": "UDF_TYPE_TABLE"
```

`}` `],`

```json
      "artifactType": "ARTIFACT_TYPE_JAVA",
      "createTime": "2024-03-11T02:54:24.822766Z",
      "uploader": "229852610122763813",
      "jarUpdateTime": "2024-03-11T02:54:24.822766Z",
      "name": "namespaces/flinkteam/udfartifacts/metric-transform-227",
      "namespace": "flinkteam",
      "jarUrl": "hdfs:///tmp/udf/metric-transform-2.2.7-shaded.jar",
      "updateTime": "2024-03-11T02:54:24.822766Z"
```

`}` `},`

```json
  "requestId": "8F0CFB56-7CE8-45AA-A788-41B7D2504E5F",
  "success": true
```

`}` `XML` format

```xml
<data>
 <@type>type.googleapis.com/vvp.sql.v1beta1.CreateUdfArtifactResponse</@type>
 <collidingClasses  />
 <udfArtifact>
  <dependencyJarUris  />
  <udfClasses>
   <functionNames  />
   <udfArtifactName>namespaces/flinkteam/udfartifacts/metric-transform-227</udfArtifactName>
   <className>com.alibaba.blink.udtf.TimestampProbe</className>
   <classType>UDF_TYPE_SCALAR</classType>
  </udfClasses>
  <udfClasses>
   <functionNames  />
   <udfArtifactName>namespaces/flinkteam/udfartifacts/metric-transform-227</udfArtifactName>
   <className>com.alibaba.blink.udtf.TransformUdtf</className>
   <classType>UDF_TYPE_TABLE</classType>
  </udfClasses>
  <artifactType>ARTIFACT_TYPE_JAVA</artifactType>
  <createTime>2024-03-11T02:54:24.822766Z</createTime>
  <uploader>229852610122763813</uploader>
  <jarUpdateTime>2024-03-11T02:54:24.822766Z</jarUpdateTime>
  <name>namespaces/flinkteam/udfartifacts/metric-transform-227</name>
  <namespace>flinkteam</namespace>
  <jarUrl>hdfs:///tmp/udf/metric-transform-2.2.7-shaded.jar</jarUrl>
  <updateTime>2024-03-11T02:54:24.822766Z</updateTime>
 </udfArtifact>
</data> <requestId>8F0CFB56-7CE8-45AA-A788-41B7D2504E5F</requestId> <success>true</success>
```

ververica 2020-05-01

#### 3.1.46 DeleteConnector

Deletes a custom connector.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HTTP /1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| name | String | Path | Yes | hologres-fix | The name of the connector that you want to delete. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | 7113AD53-5192- 46E5-B592- 81175BAF7F54 | The request ID. |

Sample requests

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HTTP /1.1 &RegionId= &workspace= &name= &namespace= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "success": true,
  "requestId": "7113AD53-5192-46E5-B592-81175BAF7F54"
```

`}` `XML` format

```xml
<success>true</success> <requestId>7113AD53-5192-46E5-B592-81175BAF7F54</requestId>
```

#### 3.1.47 DeleteDeploymentDraft

Deletes a draft.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-drafts/[deployme ntDraftId] HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| deploymen tDraftId | String | Path | Yes | afb75048-590a-4ac3- 84d4-96f873b14659 | The ID of the draft that you want to delete. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| data | String | { "metadata": { "createdAt": "2024- 03-13T01:46:23Z", "modifiedAt": "2024-03- 13T01:56:47Z", "resourceVersion": 26, "name": "mytable", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "modifier": "229852610122763 813", "creatorName": "flinkadmin", "comment": "", "modifierName": "flinkadmin", "priority": "5" }, "id": "afb75048- 590a-4ac3-84d4- 96f873b14659", "parentId": "99d3a304-a14b- 32da-945c- 765bb687aa61", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentDraft", "spec": { "template": { "metadata": { "annotations": { "flink.queryable- state.enabled": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "sqlScript": "-- ******************** ******************** ******************** ********-- -- Author: Write your name here -- Created Time: 2024-03-13 09:46:19 -- Description: Write your description here -- ******************** ******************** ******************** ********-- |   |

| data Parameter | String Type | INSERT INTO Example `vvp`.`default`.print | The draft details. Description |
|---|---|---|---|
|   |   | Sink SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM `vvp`.`default`.data genSource; ", "imageUserDefined" : false, "versionName": "vvr-6.0.0-flink- 1.15" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 2.0 }, "taskmanager": { "memory": "4Gi", "cpu": 2.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration": { "execution.checkpoi nting.interval": "180s", "execution.checkpoi nting.min-pause": "180s" } } }, "restoreStrategy": { "kind": |   |
|   |   | "LATEST STATE", _ "allowNonRestoredS tate": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "maxSavepointCreat ionAttempts": 4, "maxJobCreationAtt empts": 1, "deploymentTargetI d": "f2ed6708-a7e1- 4e86-a99e- 327fac9265c2" } } |   |
| requestId | String | 374ECDF6-D148- 4A78-9548- F550EA53255A | The request ID. |

Sample requests

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-drafts/[deployme ntDraftId] HTTP/1.1 &RegionId= &workspace= &namespace= &deploymentDraftId= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "data": {
    "metadata": {
      "createdAt": "2024-03-13T01:46:23Z",
      "modifiedAt": "2024-03-13T01:56:47Z",
      "resourceVersion": 26,
      "name": "mytable",
      "namespace": "flinkteam",
      "annotations": {
        "creator": "229852610122763813",
        "modifier": "229852610122763813",
        "creatorName": "flinkadmin",
        "comment": "",
        "modifierName": "flinkadmin",
        "priority": "5"
```

`},`

```json
      "id": "afb75048-590a-4ac3-84d4-96f873b14659",
      "parentId": "99d3a304-a14b-32da-945c-765bb687aa61",
      "labels": {}
```

`},`

```json
    "apiVersion": "v1",
    "kind": "DeploymentDraft",
    "spec": {
      "template": {
        "metadata": {
          "annotations": {
            "flink.queryable-state.enabled": "false"
```

`}` `},`

```json
        "spec": {
          "artifact": {
            "kind": "SQLSCRIPT",
            "sqlScript": "--
********************************************************************---- Author:         Wri
te your name here-- Created Time: 2024-03-13 09:46:19-- Description: Write your descrip tion here--********************************************************************--INSERT INTO `vvp`.`default`.printSinkSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM `vvp`.`default`.datagenSource;",
            "imageUserDefined": false,
            "versionName": "vvr-6.0.0-flink-1.15"
```

`},`

```json
          "parallelism": 1,
          "batchMode": false,
```

`"` `"` `{`

```json
          "resources": {
            "jobmanager": {
              "memory": "4Gi",
              "cpu": 2.0
```

`},`

```json
            "taskmanager": {
              "memory": "4Gi",
              "cpu": 2.0
```

`}` `},`

```json
          "logging": {
            "log4jLoggers": {
              "": "INFO"
```

`},`

```json
            "logReservePolicy": {
              "expirationDays": 7,
              "openHistory": true
```

`},`

```json
            "loggingProfile": "default"
```

`},`

```json
          "flinkConfiguration": {
            "execution.checkpointing.interval": "180s",
            "execution.checkpointing.min-pause": "180s"
```

`}` `}` `},`

```json
      "restoreStrategy": {
        "kind": "LATEST_STATE",
        "allowNonRestoredState": false
```

`},`

```json
      "state": "CANCELLED",
      "upgradeStrategy": {
        "kind": "STATELESS"
```

`},`

```json
      "maxSavepointCreationAttempts": 4,
      "maxJobCreationAttempts": 1,
      "deploymentTargetId": "f2ed6708-a7e1-4e86-a99e-327fac9265c2"
```

`}` `},`

```json
  "success": true,
  "requestId": "374ECDF6-D148-4A78-9548-F550EA53255A"
```

`}` `XML` format

```xml
<data>
 <metadata>
  <createdAt>2024-03-13T01:46:23Z</createdAt>
  <modifiedAt>2024-03-13T01:56:47Z</modifiedAt>
  <resourceVersion>26</resourceVersion>
  <name>mytable</name>
  <namespace>flinkteam</namespace>
  <annotations>
   <creator>229852610122763813</creator>
   <modifier>229852610122763813</modifier>
   <creatorName>flinkadmin</creatorName>
   <comment  />
```

`/`

```xml
   <modifierName>flinkadmin</modifierName>
   <priority>5</priority>
  </annotations>
  <id>afb75048-590a-4ac3-84d4-96f873b14659</id>
  <parentId>99d3a304-a14b-32da-945c-765bb687aa61</parentId>
  <labels  />
 </metadata>
 <apiVersion>v1</apiVersion>
 <kind>DeploymentDraft</kind>
 <spec>
  <template>
   <metadata>
    <annotations>
     <flink.queryable-state.enabled>false</flink.queryable-state.enabled>
    </annotations>
   </metadata>
   <spec>
    <artifact>
     <kind>SQLSCRIPT</kind>
     <sqlScript>--********************************************************************--
-- Author: Write your name here -- Created Time: 2024-03-13 09:46:19 -- Description: Write your description here --********************************************************************-- INSERT INTO `vvp`.`default`.printSink SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens FROM
  `vvp`.`default`.datagenSource;
     </sqlScript>
     <imageUserDefined>false</imageUserDefined>
     <versionName>vvr-6.0.0-flink-1.15</versionName>
    </artifact>
    <parallelism>1</parallelism>
    <batchMode>false</batchMode>
    <resources>
     <jobmanager>
      <memory>4Gi</memory>
      <cpu>2</cpu>
     </jobmanager>
     <taskmanager>
      <memory>4Gi</memory>
      <cpu>2</cpu>
     </taskmanager>
    </resources>
    <logging>
     <log4jLoggers>
      <>INFO</>
     </log4jLoggers>
     <logReservePolicy>
      <expirationDays>7</expirationDays>
      <openHistory>true</openHistory>
     </logReservePolicy>
     <loggingProfile>default</loggingProfile>
    </logging>
    <flinkConfiguration>
<execution.checkpointing.interval>180s</execution.checkpointing.interval>
```

```xml
     <execution.checkpointing.interval>180s</execution.checkpointing.interval>
     <execution.checkpointing.min-pause>180s</execution.checkpointing.min-pause>
    </flinkConfiguration>
   </spec>
  </template>
  <restoreStrategy>
   <kind>LATEST_STATE</kind>
   <allowNonRestoredState>false</allowNonRestoredState>
  </restoreStrategy>
  <state>CANCELLED</state>
  <upgradeStrategy>
   <kind>STATELESS</kind>
  </upgradeStrategy>
  <maxSavepointCreationAttempts>4</maxSavepointCreationAttempts>
  <maxJobCreationAttempts>1</maxJobCreationAttempts>
  <deploymentTargetId>f2ed6708-a7e1-4e86-a99e-327fac9265c2</deploymentTargetId>
 </spec>
</data> <success>true</success> <requestId>374ECDF6-D148-4A78-9548-F550EA53255A</requestId>
```

#### 3.1.48 DeleteFormat

Deletes a format.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HTTP/1.
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env****-d01 | The region ID. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| name | String | Path | Yes | customized-csv | The name of the format that you want to delete. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | EC30D915-1E89- 4B66-B1AA- C5D161DAB50D | The request ID. |

Sample requests

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HTTP/1. &RegionId= &workspace= &name= &namespace= &Common request parameters
```

Sample success responses `JSON` format

```json
{"requestId":"EC30D915-1E89-4B66-B1AA-C5D161DAB50D"}
```

`XML` format

```xml
<requestId>EC30D915-1E89-4B66-B1AA-C5D161DAB50D</requestId>
```

#### 3.1.49 DeleteMember

Revokes the permissions on a namespace from a user.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
DELETE /pop/workspaces/[workspace]/members/v1/namespaces/[namespace]/members/[member] HTTP/1
```

`.1`

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespace | Strin g | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| member | Strin g | Path | Yes | user:24242541014529220 9 | The information about the user from whom you want to revoke permissions. Format: user:${uid}. |
| RegionId | Strin g | Host | Yes | cn-wulan-env188-d01 | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| requestId | String | 8AA170D4-F4D1- 4E90-A02D- 0CC211BE8171 | The request ID. |
|---|---|---|---|

Sample requests

```
DELETE /pop/workspaces/[workspace]/members/v1/namespaces/[namespace]/members/[member] HTTP/1
```

`.1`

```
&workspace= &namespace= &member= &RegionId= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "success": true,
  "requestId": "8AA170D4-F4D1-4E90-A02D-0CC211BE8171"
```

`}` `XML` format

```xml
<success>true</success> <requestId>8AA170D4-F4D1-4E90-A02D-0CC211BE8171</requestId>
```

ververica 2020-05-01

#### 3.1.50 DeleteSecretValue

Deletes a variable.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values/[name] HTTP/1
```

`.1`

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|

| RegionId | Strin g | Host | Yes | cn-qingdao-env17e-d01 | The region ID. |
|---|---|---|---|---|---|
| namespace | Strin g | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| name | Strin g | Path | No | secretKey | The name of the variable. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | 1CCA8A71-98C6- 491B-9A2D- ADDFC0939294 | The request ID. |

Sample requests

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values/[name] HTTP/1
```

`.1`

```
&RegionId= &namespace= &workspace= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "success": true,
  "requestId": "1CCA8A71-98C6-491B-9A2D-ADDFC0939294"
```

`}` `XML` format

```xml
<success>true</success> <requestId>1CCA8A71-98C6-491B-9A2D-ADDFC0939294</requestId>
```

ververica 2020-05-01

#### 3.1.51 DeleteUdfArtifact

Deletes a user-defined function (UDF).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env188-d01 | The region ID. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |

| namespace | Strin g | Path | Yes | ververica | The name of the namespace to which the deployment belongs. |
|---|---|---|---|---|---|
| udfArtifactN ame | Strin g | Path | Yes | metric-transform-227- shaded | The name of the UDF. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "referencedClasses" : [], "@type": "type.googleapis.co m/vvp.sql.v1beta1.D eleteUdfArtifactResp onse" } | The detailed information. |
| requestId | String | 07E49735-A389- 4853-AFBA- 28F9EB0EFDC4 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1 &RegionId= &workspace= &namespace= &udfArtifactName= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "data": {
    "referencedClasses": [],
    "@type": "type.googleapis.com/vvp.sql.v1beta1.DeleteUdfArtifactResponse"
```

`},`

```json
  "requestId": "07E49735-A389-4853-AFBA-28F9EB0EFDC4",
  "success": true
```

`}` `XML` format

```xml
<data>
 <referencedClasses  />
 <@type>type.googleapis.com/vvp.sql.v1beta1.DeleteUdfArtifactResponse</@type>
</data> <requestId>07E49735-A389-4853-AFBA-28F9EB0EFDC4</requestId> <success>true</success>
```

ververica 2020-05-01

#### 3.1.52 ExecuteSqlscriptsStatements

Manages functions.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:execute-multi HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| paramsJso n | String | Body | No | {"executeFunctionStr": ["DROP FUNCTION `TimestampProbe`"]} | The SQL script. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.v1beta1.L istUdfArtifactsRespo nse", "udfArtifacts": [ { "name": "namespaces/flinkte am/udfartifacts/metr ic-transform-227", "jarUrl": "hdfs:///tmp/udf/met ric-transform-2.2.7- shaded.jar", "udfClasses": [ { "className": "com.alibaba.blink.u dtf.TimestampProbe ", "classType": "UDF TYPE SCALAR _ _ ", "udfArtifactName": "namespaces/flinkte am/udfartifacts/metr ic-transform-227", "functionNames": [ "TimestampProbe" ] } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "dependencyJarUris" : [], "uploader": "229852610122763 813", "namespace": "namespaces/flinkte am", "createTime": "2024-03- 11T02:54:25Z", "updateTime": "2024-03- 11T02:54:25Z", "jarUpdateTime": "2024-03- 11T02:54:25Z" } ] } | The detailed information about the functions. |
| requestId | String | 151E1A19-091A- 4317-ADF9- FDD81C735414 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:execute-multi HTTP/1.1
```

`{`

```json
"RegionId":"", "workspace":"", "namespace":""
```

`}` Sample success responses `JSON` format `{`

```json
  "requestId": "151E1A19-091A-4317-ADF9-FDD81C735414",
  "success": true,
  "data": {
    "@type": "type.googleapis.com/vvp.sql.v1beta1.ListUdfArtifactsResponse",
    "udfArtifacts": [
```

`{`

```json
        "name": "namespaces/flinkteam/udfartifacts/metric-transform-227",
        "jarUrl": "hdfs:///tmp/udf/metric-transform-2.2.7-shaded.jar",
        "udfClasses": [
```

`{`

```json
            "className": "com.alibaba.blink.udtf.TimestampProbe",
            "classType": "UDF_TYPE_SCALAR",
            "udfArtifactName": "namespaces/flinkteam/udfartifacts/metric-transform-227",
            "functionNames": [
              "TimestampProbe"
```

`]` `}` `],`

```json
        "artifactType": "ARTIFACT_TYPE_JAVA",
        "dependencyJarUris": [],
        "uploader": "229852610122763813",
        "namespace": "namespaces/flinkteam",
        "createTime": "2024-03-11T02:54:25Z",
        "updateTime": "2024-03-11T02:54:25Z",
        "jarUpdateTime": "2024-03-11T02:54:25Z"
```

`}` `]` `}` `}` `XML` format

```xml
<requestId>151E1A19-091A-4317-ADF9-FDD81C735414</requestId> <success>true</success> <data>
 <@type>type.googleapis.com/vvp.sql.v1beta1.ListUdfArtifactsResponse</@type>
 <udfArtifacts>
  <name>namespaces/flinkteam/udfartifacts/metric-transform-227</name>
  <jarUrl>hdfs:///tmp/udf/metric-transform-2.2.7-shaded.jar</jarUrl>
  <udfClasses>
   <className>com.alibaba.blink.udtf.TimestampProbe</className>
   <classType>UDF_TYPE_SCALAR</classType>
   <udfArtifactName>namespaces/flinkteam/udfartifacts/metric-transform-227</udfArtifactName>
   <functionNames>TimestampProbe</functionNames>
  </udfClasses>
  <artifactType>ARTIFACT_TYPE_JAVA</artifactType>
  <dependencyJarUris  />
  <uploader>229852610122763813</uploader>
  <namespace>namespaces/flinkteam</namespace>
  <createTime>2024-03-11T02:54:25Z</createTime>
  <updateTime>2024-03-11T02:54:25Z</updateTime>
  <jarUpdateTime>2024-03-11T02:54:25Z</jarUpdateTime>
 </udfArtifacts>
</data>
```

#### 3.1.53 ForcefullyCreateLock

Locks a resource such as a draft.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/locks HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| workspace | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| resourceTy pe | String | Query | No | DeploymentDraft | The type of the resource to be locked. To lock a draft, set the parameter to DeploymentDraft. |
| resourceId | String | Query | No | c6f157ac-60b9-4b38- 8bad-d435387cfd59 | The ID of the resource to be locked. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | 69DEC7C2-BCE5- 4E80-8CDA- FE7ADE09AAAD | The request ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "metadata": { "createdAt": "2024- 03- 12T10:16:35.16403 4Z", "modifiedAt": "2024-03- 12T10:16:35.16403 4Z", "namespace": "flinkteam", "id": "ec62ce3c-fe33- 383e-8b31- 2fe9d89af2af" }, "apiVersion": "v1", "kind": "Lock", "spec": { "holderName": "flinkadmin", "holderId": "229852610122763 813" } } | The details of the locked resource. |

Sample requests

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/locks HTTP/1.1
```

`{`

```json
"RegionId":"", "namespace":"", "workspace":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "metadata": {
      "createdAt": "2024-03-12T10:16:35.164034Z",
      "modifiedAt": "2024-03-12T10:16:35.164034Z",
      "namespace": "flinkteam",
      "id": "ec62ce3c-fe33-383e-8b31-2fe9d89af2af"
```

`},`

```json
    "apiVersion": "v1",
    "kind": "Lock",
    "spec": {
      "holderName": "flinkadmin",
      "holderId": "229852610122763813"
```

`}` `},`

```json
  "success": true,
  "requestId": "69DEC7C2-BCE5-4E80-8CDA-FE7ADE09AAAD"
```

`}` `XML` format

```xml
<data>
 <metadata>
  <createdAt>2024-03-12T10:16:35.164034Z</createdAt>
  <modifiedAt>2024-03-12T10:16:35.164034Z</modifiedAt>
  <namespace>flinkteam</namespace>
  <id>ec62ce3c-fe33-383e-8b31-2fe9d89af2af</id>
 </metadata>
 <apiVersion>v1</apiVersion>
 <kind>Lock</kind>
 <spec>
  <holderName>flinkadmin</holderName>
  <holderId>229852610122763813</holderId>
 </spec>
</data> <success>true</success> <requestId>69DEC7C2-BCE5-4E80-8CDA-FE7ADE09AAAD</requestId>
```

#### 3.1.54 FunctionExists

Checks whether a function exists.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:functionExis HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | String | Path | Yes | ververica | The name of the namespace to which the deployment belongs. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| cat | String | Path | Yes | vvp | The name of the catalog. |
| database | String | Query | Yes | default | The name of the database. |
| function | String | Query | Yes | TransformUdtf | The name of the function. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.FunctionExis tsResponse", "exists": true } | The detailed information. |
| requestId | String | D96DD415-AD97- 4EBA-832E- 99FADB6A4F87 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:functionExis HTTP/1.1 &RegionId= &namespace= &workspace= &cat= &database= &function= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "requestId": "D96DD415-AD97-4EBA-832E-99FADB6A4F87",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.FunctionExistsResponse",
    "exists": true
```

`}` `}` `XML` format

```xml
<requestId>D96DD415-AD97-4EBA-832E-99FADB6A4F87</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.FunctionExistsResponse</@type>
 <exists>true</exists>
</data>
```

#### 3.1.55 GenerateResourcePlan

Creates a resource configuration plan for a deployment.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/resource_ an:generate HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env188-d01 | The region ID. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| deploymen tId | String | Path | Yes | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | The deployment ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "success": true, "plan": " {\"ssgProfiles\": [{\"name\":\"default \",\"cpu\":0.2,\"heap\ ":\"768 mb\",\"offHeap\":\"3 2 mb\",\"managed\": {},\"extended\": {}}],\"nodes\": [{\"id\":1,\"type\":\"S treamExecTableSou rceScan\",\"desc\":\" Source: datahub table[4]\",\ _ "profile\": {\"group\":\"default\ ",\"parallelism\":1,\" maxParallelism\":32 768,\"minParallelism \":1}}, {\"id\":2,\"type\":\"St reamExecCalc\",\"de sc\":\"Calc[5]\",\"pro file\": {\"group\":\"default\ ",\"parallelism\":1,\" maxParallelism\":32 768,\"minParallelism \":1}}, {\"id\":3,\"type\":\"St reamExecSink\",\"de sc\":\"Sink: kafka table[6]\",\"pr _ ofile\": {\"group\":\"default\ ",\"parallelism\":1,\" maxParallelism\":32 768,\"minParallelism \":1}}],\"edges\": [{\"source\":1,\"targ et\":2,\"mode\":\"PIP ELINED\",\"strategy\ ":\"FORWARD\"}, {\"source\":2,\"targe t\":3,\"mode\":\"PIPE LINED\",\"strategy\": \"FORWARD\"}],\"ve rtices\": {\"717c7b8afebbfb7 137f6f0f99beb2a94\ ":[1,2,3]}}" } | The details of the resource configuration plan. |
| requestId | String | 58091710-5895- 4111-A4FF- BEA51550A359 | The request ID. |

Sample requests

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/resource_ an:generate HTTP/1.1
```

`{`

```json
"RegionId":"", "workspace":"", "namespace":"", "deploymentId":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "success": true,
    "plan": "{\"ssgProfiles\":[{\"name\":\"default\",\"cpu\":0.2,\"heap\":\"768 mb\",\"offHe
ap\":\"32 mb\",\"managed\":{},\"extended\":{}}],\"nodes\": [{\"id\":1,\"type\":\"StreamExecTableSourceScan\",\"desc\":\"Source: datahub_table[4]\",\"profile\": {\"group\":\"default\",\"parallelism\":1,\"maxParallelism\":32768,\"minParallelism\":1}},{\" id\":2,\"type\":\"StreamExecCalc\",\"desc\":\"Calc[5]\",\"profile\": {\"group\":\"default\",\"parallelism\":1,\"maxParallelism\":32768,\"minParallelism\":1}},{\" id\":3,\"type\":\"StreamExecSink\",\"desc\":\"Sink: kafka_table[6]\",\"profile\":{\"group\": \"default\",\"parallelism\":1,\"maxParallelism\":32768,\"minParallelism\":1}}],\"edges\":[{\ "source\":1,\"target\":2,\"mode\":\"PIPELINED\",\"strategy\":\"FORWARD\"},{\"source\":2,\"ta rget\":3,\"mode\":\"PIPELINED\",\"strategy\":\"FORWARD\"}],\"vertices\": {\"717c7b8afebbfb7137f6f0f99beb2a94\":[1,2,3]}}"
```

`},`

```json
  "success": true,
  "requestId": "58091710-5895-4111-A4FF-BEA51550A359"
```

`}` `XML` format

```xml
<data>
 <success>true</success>
 <plan>{&quot;ssgProfiles&quot;:
[{&quot;name&quot;:&quot;default&quot;,&quot;cpu&quot;:0.2,&quot;heap&quot;:&quot;768 mb&quo t;,&quot;offHeap&quot;:&quot;32 mb&quot;,&quot;managed&quot;:{},&quot;extended&quot;:{}}],&q uot;nodes&quot;: [{&quot;id&quot;:1,&quot;type&quot;:&quot;StreamExecTableSourceScan&quot;,&quot;desc&quot;:&qu ;Source: datahub_table[4]&quot;,&quot;profile&quot;: {&quot;group&quot;:&quot;default&quot;,&quot;parallelism&quot;:1,&quot;maxParallelism&quot;:32 8,&quot;minParallelism&quot;:1}}, {&quot;id&quot;:2,&quot;type&quot;:&quot;StreamExecCalc&quot;,&quot;desc&quot;:&quot;Calc[5]&q t;,&quot;profile&quot;: {&quot;group&quot;:&quot;default&quot;,&quot;parallelism&quot;:1,&quot;maxParallelism&quot;:32 8,&quot;minParallelism&quot;:1}}, {&quot;id&quot;:3,&quot;type&quot;:&quot;StreamExecSink&quot;,&quot;desc&quot;:&quot;Sink: k afka_table[6]&quot;,&quot;profile&quot;: {&quot;group&quot;:&quot;default&quot;,&quot;parallelism&quot;:1,&quot;maxParallelism&quot;:32 8,&quot;minParallelism&quot;:1}}],&quot;edges&quot;: [{&quot;source&quot;:1,&quot;target&quot;:2,&quot;mode&quot;:&quot;PIPELINED&quot;,&quot;strat y&quot;:&quot;FORWARD&quot;}, {&quot;source&quot;:2,&quot;target&quot;:3,&quot;mode&quot;:&quot;PIPELINED&quot;,&quot;strate &quot;:&quot;FORWARD&quot;}],&quot;vertices&quot;: {&quot;717c7b8afebbfb7137f6f0f99beb2a94&quot;:[1,2,3]}}</plan> </data> <success>true</success> <requestId>58091710-5895-4111-A4FF-BEA51550A359</requestId>
```

#### 3.1.56 GetCatalog

Queries the information about a catalog.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getCatalog HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env188-d01 | The region ID. |
| namespac e | String | Path | Yes | ververica | The name of the namespace to which the deployment belongs. |

| Realtime Com k (Compute- dition) Devel | pute for A Storage S oper Guid | pache Fli eparation e·AppMa |   |   |   |
|---|---|---|---|---|---|

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| cat | String | Path | Yes | vvp | The name of the catalog. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.GetCatalogR esponse", "catalog": { "name": "namespaces/flinkte am/catalogs/vvp", "properties": { "defaultDatabase": "default", "type": "vvp" } } } | The detailed information. |
| requestId | String | 0AFF0B61-35A5- 46D9-930F- 3826DCA3D3F9 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getCatalog HTTP/1.1 &RegionId= &namespace= &workspace= &cat= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "requestId": "0AFF0B61-35A5-46D9-930F-3826DCA3D3F9",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.GetCatalogResponse",
    "catalog": {
      "name": "namespaces/flinkteam/catalogs/vvp",
      "properties": {
        "defaultDatabase": "default",
        "type": "vvp"
```

`}` `}` `}` `}` `XML` format

```xml
<requestId>0AFF0B61-35A5-46D9-930F-3826DCA3D3F9</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.GetCatalogResponse</@type>
 <catalog>
  <name>namespaces/flinkteam/catalogs/vvp</name>
  <properties>
   <defaultDatabase>default</defaultDatabase>
   <type>vvp</type>
  </properties>
 </catalog>
</data>
```

#### 3.1.57 GetDefaultDatabase

Queries the information about the default database in a catalog.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getDefaultDa base HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env188-d01 | The region ID. |
| namespac e | String | Path | Yes | ververica | The name of the namespace to which the deployment belongs. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| cat | String | Path | Yes | vvp | The name of the catalog. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.GetDefaultD atabaseResponse", "database": "default" } | The detailed information. |
| requestId | String | 59F6950E-FC05- 495E-A286- 08C111EC7A4B | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getDefaultDa base HTTP/1.1 &RegionId= &namespace= &workspace= &cat= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "requestId": "59F6950E-FC05-495E-A286-08C111EC7A4B",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.GetDefaultDatabaseResponse",
    "database": "default"
```

`}` `}` `XML` format

```xml
<requestId>59F6950E-FC05-495E-A286-08C111EC7A4B</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.GetDefaultDatabaseResponse</@type>
 <database>default</database>
</data>
```

#### 3.1.58 GetDeploymentDraftById

Queries the information about a draft by ID.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/[deploymentDraftId] HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env188-d01 | The region ID. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| deploymen tDraftId | String | Path | Yes | c6f157ac-60b9-4b38- 8bad-d435387cfd59 | The draft ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
|   |   | { "metadata": { "createdAt": "2024- 03-12T06:11:40Z", "modifiedAt": "2024-03- 12T06:12:11Z", "resourceVersion": 5, "name": "sqljob", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "modifier": "229852610122763 813", "creatorName": "flinkadmin", "comment": "", "modifierName": "flinkadmin", "deployment.draft.r eferenced.deployme nt.id": "d0b3abf0- 4bfe-46b1-a324- 5b7def580c00", "priority": "5" }, "lock": { "metadata": { "createdAt": "2024- |   |

| Parameter | Type | 03-12T06:11:40Z", Example "modifiedAt": | Description |
|---|---|---|---|
|   |   | "2024-03- 12T06:11:40Z", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "modifier": "229852610122763 813" }, "id": "ec62ce3c-fe33- 383e-8b31- 2fe9d89af2af" }, |   |
| data | String | "apiVersion": "v1", "kind": "Lock", "spec": { "holderName": "flinkadmin", "holderId": "229852610122763 813" } }, "id": "c6f157ac-60b9- 4b38-8bad- d435387cfd59", "parentId": "99d3a304-a14b- 32da-945c- 765bb687aa61", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentDraft", "spec": { "template": { "metadata": { "annotations": { "flink.queryable- state.enabled": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "sqlScript": "-- ******************** ******************** ******************** ********-- -- Author: Write your name here -- Created Time: 2024-03-12 14:11:38 -- Description: Write your description here -- ******************** ******************** ******************** ********-- CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( \u0027connector\u0 027 \u003d \u0027datagen\u00 27 | The information about the draft. |

| Parameter | Type | ); Example CREATE | Description |
|---|---|---|---|
|   |   | TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( \u0027connector\u0 027 \u003d \u0027print\u0027 ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ ", "imageUserDefined" : false, "versionName": "vvr-6.0.0-flink- 1.15" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 2.0 }, "taskmanager": { "memory": "4Gi", "cpu": 2.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration": { "execution.checkpoi nting.interval": "180s", "execution.checkpoi nting.min-pause": "180s" } } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestoredS tate": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "maxSavepointCreat ionAttempts": 4, "maxJobCreationAtt empts": 1, "deploymentTargetI d": "f2ed6708-a7e1- 4e86-a99e- |   |

| Parameter | Type | 327fac9265c2" } } Example | Description |
|---|---|---|---|
| requestId | String | 3EB9FFF4-A3A1- 4B85-89B4- 5987D4551AD9 | The request ID. |

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/[deploymentDraftId] HTTP/1.1 &RegionId= &workspace= &namespace= &deploymentDraftId= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "data": {
    "metadata": {
      "createdAt": "2024-03-12T06:11:40Z",
      "modifiedAt": "2024-03-12T06:12:11Z",
      "resourceVersion": 5,
      "name": "sqljob",
      "namespace": "flinkteam",
      "annotations": {
        "creator": "229852610122763813",
        "modifier": "229852610122763813",
        "creatorName": "flinkadmin",
        "comment": "",
        "modifierName": "flinkadmin",
        "deployment.draft.referenced.deployment.id": "d0b3abf0-4bfe-46b1-a324-5b7def580c00",
        "priority": "5"
```

`},`

```json
      "lock": {
        "metadata": {
          "createdAt": "2024-03-12T06:11:40Z",
          "modifiedAt": "2024-03-12T06:11:40Z",
          "namespace": "flinkteam",
          "annotations": {
            "creator": "229852610122763813",
            "modifier": "229852610122763813"
```

`},`

```json
          "id": "ec62ce3c-fe33-383e-8b31-2fe9d89af2af"
```

`},`

```json
        "apiVersion": "v1",
        "kind": "Lock",
        "spec": {
          "holderName": "flinkadmin",
          "holderId": "229852610122763813"
```

`}` `},`

```json
      "id": "c6f157ac-60b9-4b38-8bad-d435387cfd59",
```

```json
      "parentId": "99d3a304-a14b-32da-945c-765bb687aa61",
      "labels": {}
```

`},`

```json
    "apiVersion": "v1",
    "kind": "DeploymentDraft",
    "spec": {
      "template": {
        "metadata": {
          "annotations": {
            "flink.queryable-state.enabled": "false"
```

`}` `},`

```json
        "spec": {
          "artifact": {
            "kind": "SQLSCRIPT",
            "sqlScript": "--
********************************************************************---- Author:         Wri
te your name here-- Created Time: 2024-03-12 14:11:38-- Description: Write your descrip tion here--********************************************************************--CREATE TEMP ORARY TABLE `datahub_table` (strname VARCHAR)with ( \u0027connector\u0027 \u003d \u0027da tagen\u0027 );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( \u0027connector\u0027 \u003d \u0027print\u0027 );INSERT INTO kafka_tableSELECT SUBSTRING (s trname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table ;",
            "imageUserDefined": false,
            "versionName": "vvr-6.0.0-flink-1.15"
```

`},`

```json
          "parallelism": 1,
          "batchMode": false,
          "resources": {
            "jobmanager": {
              "memory": "4Gi",
              "cpu": 2.0
```

`},`

```json
            "taskmanager": {
              "memory": "4Gi",
              "cpu": 2.0
```

`}` `},`

```json
          "logging": {
            "log4jLoggers": {
              "": "INFO"
```

`},`

```json
            "logReservePolicy": {
              "expirationDays": 7,
              "openHistory": true
```

`},`

```json
            "loggingProfile": "default"
```

`},`

```json
          "flinkConfiguration": {
            "execution.checkpointing.interval": "180s",
            "execution.checkpointing.min-pause": "180s"
```

`}` `}` `},`

```json
      "restoreStrategy": {
        "kind": "LATEST_STATE",
```

```json
        "allowNonRestoredState": false
```

`},`

```json
      "state": "CANCELLED",
      "upgradeStrategy": {
        "kind": "STATELESS"
```

`},`

```json
      "maxSavepointCreationAttempts": 4,
      "maxJobCreationAttempts": 1,
      "deploymentTargetId": "f2ed6708-a7e1-4e86-a99e-327fac9265c2"
```

`}` `},`

```json
  "success": true,
  "requestId": "3EB9FFF4-A3A1-4B85-89B4-5987D4551AD9"
```

`}` `XML` format

```xml
<data>
 <metadata>
  <createdAt>2024-03-12T06:11:40Z</createdAt>
  <modifiedAt>2024-03-12T06:12:11Z</modifiedAt>
  <resourceVersion>5</resourceVersion>
  <name>sqljob</name>
  <namespace>flinkteam</namespace>
  <annotations>
   <creator>229852610122763813</creator>
   <modifier>229852610122763813</modifier>
   <creatorName>flinkadmin</creatorName>
   <comment  />
   <modifierName>flinkadmin</modifierName>
   <deployment.draft.referenced.deployment.id>d0b3abf0-4bfe-46b1-a324-
5b7def580c00</deployment.draft.referenced.deployment.id>
   <priority>5</priority>
  </annotations>
  <lock>
   <metadata>
    <createdAt>2024-03-12T06:11:40Z</createdAt>
    <modifiedAt>2024-03-12T06:11:40Z</modifiedAt>
    <namespace>flinkteam</namespace>
    <annotations>
     <creator>229852610122763813</creator>
     <modifier>229852610122763813</modifier>
    </annotations>
    <id>ec62ce3c-fe33-383e-8b31-2fe9d89af2af</id>
   </metadata>
   <apiVersion>v1</apiVersion>
   <kind>Lock</kind>
   <spec>
    <holderName>flinkadmin</holderName>
    <holderId>229852610122763813</holderId>
   </spec>
  </lock>
  <id>c6f157ac-60b9-4b38-8bad-d435387cfd59</id>
  <parentId>99d3a304-a14b-32da-945c-765bb687aa61</parentId>
  <labels  />
 </metadata>
<apiVersion>v1</apiVersion>
```

```xml
 <apiVersion>v1</apiVersion>
 <kind>DeploymentDraft</kind>
 <spec>
  <template>
   <metadata>
    <annotations>
     <flink.queryable-state.enabled>false</flink.queryable-state.enabled>
    </annotations>
   </metadata>
   <spec>
    <artifact>
     <kind>SQLSCRIPT</kind>
     <sqlScript>--********************************************************************--
-- Author: Write your name here -- Created Time: 2024-03-12 14:11:38 -- Description: Write your description here --********************************************************************-- CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR) with (
    &#x27;connector&#x27; = &#x27;datagen&#x27;
```

);

```
CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT) with (
    &#x27;connector&#x27; = &#x27;print&#x27;
```

);

```xml
INSERT INTO kafka_table SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens FROM
  datahub_table;
     </sqlScript>
     <imageUserDefined>false</imageUserDefined>
     <versionName>vvr-6.0.0-flink-1.15</versionName>
    </artifact>
    <parallelism>1</parallelism>
    <batchMode>false</batchMode>
    <resources>
     <jobmanager>
      <memory>4Gi</memory>
      <cpu>2</cpu>
     </jobmanager>
     <taskmanager>
      <memory>4Gi</memory>
      <cpu>2</cpu>
     </taskmanager>
    </resources>
    <logging>
     <log4jLoggers>
      <>INFO</>
     </log4jLoggers>
     <logReservePolicy>
      <expirationDays>7</expirationDays>
      <openHistory>true</openHistory>
     </logReservePolicy>
     <loggingProfile>default</loggingProfile>
    </logging>
<flikC
```

`fi` `ti` `>`

```xml
    <flinkConfiguration>
     <execution.checkpointing.interval>180s</execution.checkpointing.interval>
     <execution.checkpointing.min-pause>180s</execution.checkpointing.min-pause>
    </flinkConfiguration>
   </spec>
  </template>
  <restoreStrategy>
   <kind>LATEST_STATE</kind>
   <allowNonRestoredState>false</allowNonRestoredState>
  </restoreStrategy>
  <state>CANCELLED</state>
  <upgradeStrategy>
   <kind>STATELESS</kind>
  </upgradeStrategy>
  <maxSavepointCreationAttempts>4</maxSavepointCreationAttempts>
  <maxJobCreationAttempts>1</maxJobCreationAttempts>
  <deploymentTargetId>f2ed6708-a7e1-4e86-a99e-327fac9265c2</deploymentTargetId>
 </spec>
</data> <success>true</success> <requestId>3EB9FFF4-A3A1-4B85-89B4-5987D4551AD9</requestId>
```

#### 3.1.59 GetDeploymentDraftByName

Queries the information about a draft by name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/name/[deploymentDraftName] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |

| workspace | Strin g | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
|---|---|---|---|---|---|
| namespace | Strin g | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| deployment DraftName | Strin g | Path | Yes | sqljob | The name of the draft. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

|   |   | { "metadata": {}, "apiVersion": "v1", "kind": "DeploymentDraftLi st", "items": [ { "metadata": { "createdAt": "2024- 03-12T06:11:40Z", "modifiedAt": "2024-03- 12T06:12:11Z", "resourceVersion": 5, "name": "sqljob", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "modifier": "229852610122763 813", "creatorName": "flinkadmin", "comment": "", "modifierName": "flinkadmin", "deployment.draft.r eferenced.deployme nt.id": "d0b3abf0- 4bfe-46b1-a324- 5b7def580c00", "priority": "5" }, "lock": { "metadata": { "createdAt": "2024- 03-12T06:11:40Z", "modifiedAt": "2024-03- 12T06:11:40Z", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "modifier": "229852610122763 813" }, "id": |   |
|---|---|---|---|

| data | String | "ec62ce3c-fe33- 383e-8b31- 2fe9d89af2af" }, "apiVersion": "v1", "kind": "Lock", "spec": { "holderName": "flinkadmin", "holderId": "229852610122763 813" } }, "id": "c6f157ac-60b9- 4b38-8bad- d435387cfd59", "parentId": "99d3a304-a14b- 32da-945c- 765bb687aa61", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentDraft", "spec": { "template": { "metadata": { "annotations": { "flink.queryable- state.enabled": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "sqlScript": "-- ******************** ******************** ******************** ********-- -- Author: Write your name here -- Created Time: 2024-03-12 14:11:38 -- Description: Write your description here -- ******************** ******************** ******************** ********-- CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( \u0027connector\u0 027 \u003d \u0027datagen\u00 27 ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) | The details of the draft. |
|---|---|---|---|

|   |   | with ( \u0027connector\u0 027 \u003d \u0027print\u0027 ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ ", "imageUserDefined" : false, "versionName": "vvr-6.0.0-flink- 1.15" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 2.0 }, "taskmanager": { "memory": "4Gi", "cpu": 2.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration": { "execution.checkpoi nting.interval": "180s", "execution.checkpoi nting.min-pause": "180s" } } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestoredS tate": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "maxSavepointCreat ionAttempts": 4, "maxJobCreationAtt empts": 1, "deploymentTargetI d": "f2ed6708-a7e1- 4e86-a99e- 327fac9265c2" } } ] } |   |
|---|---|---|---|

| requestId | String | AB731F2D-2B11- 4C4B-A45F- F419ED5CECBF | The request ID. |
|---|---|---|---|

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/name/[deploymentDraftName] HTTP/1.1 &RegionId= &workspace= &namespace= &deploymentDraftName= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "data": {
    "metadata": {},
    "apiVersion": "v1",
    "kind": "DeploymentDraftList",
    "items": [
```

`{`

```json
        "metadata": {
          "createdAt": "2024-03-12T06:11:40Z",
          "modifiedAt": "2024-03-12T06:12:11Z",
          "resourceVersion": 5,
          "name": "sqljob",
          "namespace": "flinkteam",
          "annotations": {
            "creator": "229852610122763813",
            "modifier": "229852610122763813",
            "creatorName": "flinkadmin",
            "comment": "",
            "modifierName": "flinkadmin",
            "deployment.draft.referenced.deployment.id": "d0b3abf0-4bfe-46b1-a324-
5b7def580c00",
            "priority": "5"
```

`},`

```json
          "lock": {
            "metadata": {
              "createdAt": "2024-03-12T06:11:40Z",
              "modifiedAt": "2024-03-12T06:11:40Z",
              "namespace": "flinkteam",
              "annotations": {
                "creator": "229852610122763813",
                "modifier": "229852610122763813"
```

`},`

```json
              "id": "ec62ce3c-fe33-383e-8b31-2fe9d89af2af"
```

`},`

```json
            "apiVersion": "v1",
            "kind": "Lock",
            "spec": {
              "holderName": "flinkadmin",
              "holderId": "229852610122763813"
```

`}` `},`

```json
          "id": "c6f157ac-60b9-4b38-8bad-d435387cfd59",
          "parentId": "99d3a304-a14b-32da-945c-765bb687aa61",
          "labels": {}
```

`},` `},`

```json
        "apiVersion": "v1",
        "kind": "DeploymentDraft",
        "spec": {
          "template": {
            "metadata": {
              "annotations": {
                "flink.queryable-state.enabled": "false"
```

`}` `},`

```json
            "spec": {
              "artifact": {
                "kind": "SQLSCRIPT",
                "sqlScript": "--
********************************************************************---- Author:         Wri
te your name here-- Created Time: 2024-03-12 14:11:38-- Description: Write your descrip tion here--********************************************************************--CREATE TEMP ORARY TABLE `datahub_table` (strname VARCHAR)with ( \u0027connector\u0027 \u003d \u0027da tagen\u0027 );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( \u0027connector\u0027 \u003d \u0027print\u0027 );INSERT INTO kafka_tableSELECT SUBSTRING (s trname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table ;",
                "imageUserDefined": false,
                "versionName": "vvr-6.0.0-flink-1.15"
```

`},`

```json
              "parallelism": 1,
              "batchMode": false,
              "resources": {
                "jobmanager": {
                  "memory": "4Gi",
                  "cpu": 2.0
```

`},`

```json
                "taskmanager": {
                  "memory": "4Gi",
                  "cpu": 2.0
```

`}` `},`

```json
              "logging": {
                "log4jLoggers": {
                  "": "INFO"
```

`},`

```json
                "logReservePolicy": {
                  "expirationDays": 7,
                  "openHistory": true
```

`},`

```json
                "loggingProfile": "default"
```

`},`

```json
              "flinkConfiguration": {
                "execution.checkpointing.interval": "180s",
                "execution.checkpointing.min-pause": "180s"
```

`}` `}` `},`

```json
          "restoreStrategy": {
            "kind": "LATEST_STATE",
            "allowNonRestoredState": false
```

`},`

```json
"state":"CANCELLED",
```

```json
          state: CANCELLED,
          "upgradeStrategy": {
            "kind": "STATELESS"
```

`},`

```json
          "maxSavepointCreationAttempts": 4,
          "maxJobCreationAttempts": 1,
          "deploymentTargetId": "f2ed6708-a7e1-4e86-a99e-327fac9265c2"
```

`}` `}` `]` `},`

```json
  "success": true,
  "requestId": "AB731F2D-2B11-4C4B-A45F-F419ED5CECBF"
```

`}` `XML` format

```xml
<data>
 <metadata  />
 <apiVersion>v1</apiVersion>
 <kind>DeploymentDraftList</kind>
 <items>
  <metadata>
   <createdAt>2024-03-12T06:11:40Z</createdAt>
   <modifiedAt>2024-03-12T06:12:11Z</modifiedAt>
   <resourceVersion>5</resourceVersion>
   <name>sqljob</name>
   <namespace>flinkteam</namespace>
   <annotations>
    <creator>229852610122763813</creator>
    <modifier>229852610122763813</modifier>
    <creatorName>flinkadmin</creatorName>
    <comment  />
    <modifierName>flinkadmin</modifierName>
    <deployment.draft.referenced.deployment.id>d0b3abf0-4bfe-46b1-a324-
5b7def580c00</deployment.draft.referenced.deployment.id>
    <priority>5</priority>
   </annotations>
   <lock>
    <metadata>
     <createdAt>2024-03-12T06:11:40Z</createdAt>
     <modifiedAt>2024-03-12T06:11:40Z</modifiedAt>
     <namespace>flinkteam</namespace>
     <annotations>
      <creator>229852610122763813</creator>
      <modifier>229852610122763813</modifier>
     </annotations>
     <id>ec62ce3c-fe33-383e-8b31-2fe9d89af2af</id>
    </metadata>
    <apiVersion>v1</apiVersion>
    <kind>Lock</kind>
    <spec>
     <holderName>flinkadmin</holderName>
     <holderId>229852610122763813</holderId>
    </spec>
   </lock>
   <id>c6f157ac-60b9-4b38-8bad-d435387cfd59</id>
```

```xml
   <parentId>99d3a304-a14b-32da-945c-765bb687aa61</parentId>
   <labels  />
  </metadata>
  <apiVersion>v1</apiVersion>
  <kind>DeploymentDraft</kind>
  <spec>
   <template>
    <metadata>
     <annotations>
      <flink.queryable-state.enabled>false</flink.queryable-state.enabled>
     </annotations>
    </metadata>
    <spec>
     <artifact>
      <kind>SQLSCRIPT</kind>
      <sqlScript>--********************************************************************--
-- Author: Write your name here -- Created Time: 2024-03-12 14:11:38 -- Description: Write your description here --********************************************************************-- CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR) with (
    &#x27;connector&#x27; = &#x27;datagen&#x27;
```

);

```
CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT) with (
    &#x27;connector&#x27; = &#x27;print&#x27;
```

);

```xml
INSERT INTO kafka_table SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens FROM
  datahub_table;
      </sqlScript>
      <imageUserDefined>false</imageUserDefined>
      <versionName>vvr-6.0.0-flink-1.15</versionName>
     </artifact>
     <parallelism>1</parallelism>
     <batchMode>false</batchMode>
     <resources>
      <jobmanager>
       <memory>4Gi</memory>
       <cpu>2</cpu>
      </jobmanager>
      <taskmanager>
       <memory>4Gi</memory>
       <cpu>2</cpu>
      </taskmanager>
     </resources>
     <logging>
      <log4jLoggers>
       <>INFO</>
      </log4jLoggers>
      <logReservePolicy>
       <expirationDays>7</expirationDays>
       <openHistory>true</openHistory>
```

```xml
      </logReservePolicy>
      <loggingProfile>default</loggingProfile>
     </logging>
     <flinkConfiguration>
      <execution.checkpointing.interval>180s</execution.checkpointing.interval>
      <execution.checkpointing.min-pause>180s</execution.checkpointing.min-pause>
     </flinkConfiguration>
    </spec>
   </template>
   <restoreStrategy>
    <kind>LATEST_STATE</kind>
    <allowNonRestoredState>false</allowNonRestoredState>
   </restoreStrategy>
   <state>CANCELLED</state>
   <upgradeStrategy>
    <kind>STATELESS</kind>
   </upgradeStrategy>
   <maxSavepointCreationAttempts>4</maxSavepointCreationAttempts>
   <maxJobCreationAttempts>1</maxJobCreationAttempts>
   <deploymentTargetId>f2ed6708-a7e1-4e86-a99e-327fac9265c2</deploymentTargetId>
  </spec>
 </items>
</data> <success>true</success> <requestId>AB731F2D-2B11-4C4B-A45F-F419ED5CECBF</requestId>
```

ververica 2020-05-01

#### 3.1.60 GetDeploymentDraftResourcePlan

Queries the information about the resource configuration plan of a draft.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/[deploymentDraftId]/resource_plan HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| deploymen tDraftId | String | Path | Yes | c6f157ac-60b9-4b38- 8bad-d435387cfd59 | The draft ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| data | String | { "success": true, "message": "", "plan": "" } | The details of the resource configuration plan. |
| requestId | String | 49D8D2CA-51A8- 43FE-820A- F44970A83159 | The request ID. |

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/[deploymentDraftId]/resource_plan HTTP/1.1 &RegionId= &workspace= &namespace= &deploymentDraftId= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "data": {
    "success": true,
    "message": "",
    "plan": ""
```

`},`

```json
  "success": true,
  "requestId": "49D8D2CA-51A8-43FE-820A-F44970A83159"
```

`}` `XML` format

```xml
<data>
 <success>true</success>
 <message  />
 <plan  />
</data> <success>true</success> <requestId>49D8D2CA-51A8-43FE-820A-F44970A83159</requestId>
```

#### 3.1.61 GetDeploymentDraftResourcePlanWithBestEffort

Queries the information about a resource configuration plan.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-drafts/[deployment DraftId]/resource_plan:best-effort-merge HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| deploymen tDraftId | String | Path | Yes | c6f157ac-60b9-4b38- 8bad-d435387cfd59 | The draft ID. |
| deploymen tId | String | Query | No | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | The deployment ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "success": true, "plan": " {\"ssgProfiles\": [{\"name\":\"default \",\"cpu\":0.2,\"heap\ ":\"768 mb\",\"offHeap\":\"3 2 mb\",\"managed\": {},\"extended\": {}}],\"nodes\": [{\"id\":1,\"type\":\"S treamExecTableSou rceScan\",\"desc\":\" Source: datahub table[11]\", _ \"profile\": {\"group\":\"default\ ",\"parallelism\":1,\" maxParallelism\":32 768,\"minParallelism \":1}}, {\"id\":2,\"type\":\"St reamExecCalc\",\"de sc\":\"Calc[12]\",\"pr ofile\": {\"group\":\"default\ ",\"parallelism\":1,\" maxParallelism\":32 768,\"minParallelism \":1}}, {\"id\":3,\"type\":\"St reamExecSink\",\"de sc\":\"Sink: kafka table[13]\",\"p _ rofile\": {\"group\":\"default\ ",\"parallelism\":1,\" maxParallelism\":32 768,\"minParallelism \":1}}],\"edges\": [{\"source\":1,\"targ et\":2,\"mode\":\"PIP ELINED\",\"strategy\ ":\"FORWARD\"}, {\"source\":2,\"targe t\":3,\"mode\":\"PIPE LINED\",\"strategy\": \"FORWARD\"}],\"ve rtices\": {\"717c7b8afebbfb7 137f6f0f99beb2a94\ ":[1,2,3]}}" } | The resource configuration details. |
| requestId | String | 3B46A3C8-2D6A- 4DE6-8468- E6A72E7E5FE8 | The request ID. |

Sample requests

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-drafts/[deployment DraftId]/resource_plan:best-effort-merge HTTP/1.1
```

`{`

```json
"RegionId":"", "workspace":"", "namespace":"", "deploymentDraftId":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "success": true,
    "plan": "{\"ssgProfiles\":[{\"name\":\"default\",\"cpu\":0.2,\"heap\":\"768 mb\",\"offHe
ap\":\"32 mb\",\"managed\":{},\"extended\":{}}],\"nodes\": [{\"id\":1,\"type\":\"StreamExecTableSourceScan\",\"desc\":\"Source: datahub_table[11]\",\"profile\": {\"group\":\"default\",\"parallelism\":1,\"maxParallelism\":32768,\"minParallelism\":1}},{\" id\":2,\"type\":\"StreamExecCalc\",\"desc\":\"Calc[12]\",\"profile\": {\"group\":\"default\",\"parallelism\":1,\"maxParallelism\":32768,\"minParallelism\":1}},{\" id\":3,\"type\":\"StreamExecSink\",\"desc\":\"Sink: kafka_table[13]\",\"profile\":{\"group\" :\"default\",\"parallelism\":1,\"maxParallelism\":32768,\"minParallelism\":1}}],\"edges\":[{ \"source\":1,\"target\":2,\"mode\":\"PIPELINED\",\"strategy\":\"FORWARD\"},{\"source\":2,\"t arget\":3,\"mode\":\"PIPELINED\",\"strategy\":\"FORWARD\"}],\"vertices\":{\"717c7b8afebbfb71 37f6f0f99beb2a94\":[1,2,3]}}"
```

`},`

```json
  "success": true,
  "requestId": "3B46A3C8-2D6A-4DE6-8468-E6A72E7E5FE8"
```

`}` `XML` format

```xml
<data>
 <success>true</success>
 <plan>{&quot;ssgProfiles&quot;:
[{&quot;name&quot;:&quot;default&quot;,&quot;cpu&quot;:0.2,&quot;heap&quot;:&quot;768 mb&quo t;,&quot;offHeap&quot;:&quot;32 mb&quot;,&quot;managed&quot;:{},&quot;extended&quot;:{}}],&q uot;nodes&quot;: [{&quot;id&quot;:1,&quot;type&quot;:&quot;StreamExecTableSourceScan&quot;,&quot;desc&quot;:&qu ;Source: datahub_table[11]&quot;,&quot;profile&quot;: {&quot;group&quot;:&quot;default&quot;,&quot;parallelism&quot;:1,&quot;maxParallelism&quot;:32 8,&quot;minParallelism&quot;:1}}, {&quot;id&quot;:2,&quot;type&quot;:&quot;StreamExecCalc&quot;,&quot;desc&quot;:&quot;Calc[12]& ot;,&quot;profile&quot;: {&quot;group&quot;:&quot;default&quot;,&quot;parallelism&quot;:1,&quot;maxParallelism&quot;:32 8,&quot;minParallelism&quot;:1}}, {&quot;id&quot;:3,&quot;type&quot;:&quot;StreamExecSink&quot;,&quot;desc&quot;:&quot;Sink: k afka_table[13]&quot;,&quot;profile&quot;: {&quot;group&quot;:&quot;default&quot;,&quot;parallelism&quot;:1,&quot;maxParallelism&quot;:32 8,&quot;minParallelism&quot;:1}}],&quot;edges&quot;: [{&quot;source&quot;:1,&quot;target&quot;:2,&quot;mode&quot;:&quot;PIPELINED&quot;,&quot;strat y&quot;:&quot;FORWARD&quot;}, {&quot;source&quot;:2,&quot;target&quot;:3,&quot;mode&quot;:&quot;PIPELINED&quot;,&quot;strate &quot;:&quot;FORWARD&quot;}],&quot;vertices&quot;: {&quot;717c7b8afebbfb7137f6f0f99beb2a94&quot;:[1,2,3]}}</plan> </data> <success>true</success> <requestId>3B46A3C8-2D6A-4DE6-8468-E6A72E7E5FE8</requestId>
```

#### 3.1.62 GetFunction

Queries the details of a function.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getFunction HTTP/1.1
```

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env188-d01 | The region ID. |

| namespace | Strin g | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
|---|---|---|---|---|---|
| workspace | Strin g | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| cat | Strin g | Path | Yes | vvp | The name of the catalog. |
| database | Strin g | Quer y | Yes | default | The name of the database. |
| function | Strin g | Quer y | Yes | TransformUdtf | The name of the function. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.GetFunction Response", "function": { "name": "TransformUdtf", "className": "com.alibaba.blink.u dtf.TransformUdtf", "functionLanguage": "FUNCTION LANGUA _ GE JAVA", _ "functionType": "FUNCTION TYPE FL _ _ INK", "description": "This is a user- defined function" }, "success": true, "message": "" } | The detailed information. |

| requestId | String | DD2A9970-CED3- 4AD6-B0F6- 8DFDD84AC6AC | The request ID. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getFunction HTTP/1.1 &RegionId= &namespace= &workspace= &cat= &database= &function= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "requestId": "DD2A9970-CED3-4AD6-B0F6-8DFDD84AC6AC",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.GetFunctionResponse",
    "function": {
      "name": "TransformUdtf",
      "className": "com.alibaba.blink.udtf.TransformUdtf",
      "functionLanguage": "FUNCTION_LANGUAGE_JAVA",
      "functionType": "FUNCTION_TYPE_FLINK",
      "description": "This is a user-defined function"
```

`},`

```json
    "success": true,
    "message": ""
```

`}` `}` `XML` format

```xml
<requestId>DD2A9970-CED3-4AD6-B0F6-8DFDD84AC6AC</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.GetFunctionResponse</@type>
 <function>
  <name>TransformUdtf</name>
  <className>com.alibaba.blink.udtf.TransformUdtf</className>
  <functionLanguage>FUNCTION_LANGUAGE_JAVA</functionLanguage>
  <functionType>FUNCTION_TYPE_FLINK</functionType>
  <description>This is a user-defined function</description>
 </function>
 <success>true</success>
 <message  />
</data>
```

ververica 2020-05-01

#### 3.1.63 GetResourcePlan

Queries the information about the resource configuration plan of a deployment.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/resource_ an HTTP/1.1
```

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |

| workspace | Strin g | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
|---|---|---|---|---|---|
| namespace | Strin g | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| deployment Id | Strin g | Path | Yes | d0b3abf0-4bfe-46b1-a324- 5b7def580c00 | The deployment ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| data | String | { "success": true, "message": "", "plan": "" } | The details of the resource configuration plan. |
| requestId | String | 87589423-CE39- 470D-81EA- 5AB477CF4CD4 | The request ID. |

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/resource_ an HTTP/1.1 &RegionId= &workspace= &namespace= &deploymentId= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "data": {
    "success": true,
    "message": "",
    "plan": ""
```

`},`

```json
  "success": true,
  "requestId": "87589423-CE39-470D-81EA-5AB477CF4CD4"
```

`}` `XML` format

```xml
<data>
 <success>true</success>
 <message  />
 <plan  />
</data> <success>true</success> <requestId>87589423-CE39-470D-81EA-5AB477CF4CD4</requestId>
```

ververica 2020-05-01

#### 3.1.64 GetTable

Queries the information about a table.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getTable H TTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | String | Path | Yes | ververica | The name of the namespace to which the deployment belongs. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| cat | String | Path | Yes | vvp | The name of the catalog. |
| database | String | Query | Yes | default | The name of the database. |
| table | String | Query | Yes | mydatahub | The name of the table. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.GetTableRes ponse", "table": { "name": "mydatahub", "schema": { "column": [ { "name": "strname", "type": "VARCHAR(2147483 647)", "expression": "" } ], "watermarkSpec": [] }, "properties": { "accessId": "SVw******PtL", "endpoint": "https://datahub.cn- wulan-env188- d01.dh.inter.env188 .shuguang.com", "connector": "datahub", "accessKey": "RfE******VMB", "project": "datahub", "topic": "mysource" }, "comment": "" }, "success": true, "message": "" } | The detailed information. |
| requestId | String | FCB6D11E-8FAA- 48F7-8E25- 28218A6878F5 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getTable H TTP/1.1 &RegionId= &namespace= &workspace= &cat= &database= &table= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "requestId": "FCB6D11E-8FAA-48F7-8E25-28218A6878F5",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.GetTableResponse",
    "table": {
      "name": "mydatahub",
      "schema": {
        "column": [
```

`{`

```json
            "name": "strname",
            "type": "VARCHAR(2147483647)",
            "expression": ""
```

`}` `],`

```json
        "watermarkSpec": []
```

`},`

```json
      "properties": {
        "accessId": "SVw******PtL",
        "endpoint": "https://datahub.cn-wulan-env188-d01.dh.inter.env188.shuguang.com",
        "connector": "datahub",
        "accessKey": "RfE******VMB",
        "project": "datahub",
        "topic": "mysource"
```

`},`

```json
      "comment": ""
```

`},`

```json
    "success": true,
    "message": ""
```

`}` `}` `XML` format

```xml
<requestId>FCB6D11E-8FAA-48F7-8E25-28218A6878F5</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.GetTableResponse</@type>
 <table>
  <name>mydatahub</name>
  <schema>
   <column>
    <name>strname</name>
    <type>VARCHAR(2147483647)</type>
    <expression  />
   </column>
   <watermarkSpec  />
  </schema>
  <properties>
   <accessId>SVw******PtL</accessId>
   <endpoint>https://datahub.cn-wulan-env188-d01.dh.inter.env188.shuguang.com</endpoint>
   <connector>datahub</connector>
   <accessKey>RfE******VMB</accessKey>
   <project>datahub</project>
   <topic>mysource</topic>
  </properties>
  <comment  />
 </table>
 <success>true</success>
 <message  />
</data>
```

#### 3.1.65 GetUdfArtifact

Queries the information about a user-defined function (UDF).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-*****-env***-d01 | The region ID. |

| requireFunc tionNames | Boole an | Quer y | Yes | true | Specifies whether to return the UDF name. |
|---|---|---|---|---|---|
| workspace | Strin g | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespace | Strin g | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| udfArtifactN ame | Strin g | Path | Yes | metric-transform-227- shaded | The name of the UDF. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

|   |   | { "@type": "type.googleapis.co m/vvp.sql.v1beta1.G etUdfArtifactRespon se", "udfArtifact": { "dependencyJarUris" : [], "udfClasses": [ { "functionNames": [ "TimestampProbe" ], "udfArtifactName": "namespaces/flinkte am/udfartifacts/metr ic-transform-227- shaded", "className": "com.alibaba.blink.u |   |
|---|---|---|---|
| data | String | dtf.TimestampProbe ", "classType": "UDF TYPE SCALAR _ _ " }, { "functionNames": [ "TransformUdtf" ], "udfArtifactName": "namespaces/flinkte am/udfartifacts/metr ic-transform-227- shaded", "className": "com.alibaba.blink.u dtf.TransformUdtf", "classType": "UDF TYPE TABLE" _ _ } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "createTime": "2024-03- 08T08:13:54Z", "uploader": "223474909869445 380", "jarUpdateTime": "2024-03- 08T08:13:57Z", "name": "namespaces/flinkte am/udfartifacts/metr ic-transform-227- shaded", "namespace": "namespaces/flinkte am", "jarUrl": "hdfs:///vvp/data/sql - artifacts/namespace s/flinkteam/udfs/met ric-transform-227- shaded/2024-03- 08T08-13- 54.732313Z/metric- transform-2.2.7- shaded.jar", "updateTime": "2024-03- 08T08:13:57Z" } } | The detailed information. |

| requestId | String | C44A1880-5138- 4204-9165- DC65C4B059C2 | The request ID. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1 &RegionId= &requireFunctionNames= &workspace= &namespace= &udfArtifactName= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "data": {
    "@type": "type.googleapis.com/vvp.sql.v1beta1.GetUdfArtifactResponse",
    "udfArtifact": {
      "dependencyJarUris": [],
      "udfClasses": [
```

`{`

```json
          "functionNames": [
            "TimestampProbe"
```

`],`

```json
          "udfArtifactName": "namespaces/flinkteam/udfartifacts/metric-transform-227-shaded"
```

`,`

```json
          "className": "com.alibaba.blink.udtf.TimestampProbe",
          "classType": "UDF_TYPE_SCALAR"
```

`},` `{`

```json
          "functionNames": [
            "TransformUdtf"
```

`],`

```json
          "udfArtifactName": "namespaces/flinkteam/udfartifacts/metric-transform-227-shaded"
```

`,`

```json
          "className": "com.alibaba.blink.udtf.TransformUdtf",
          "classType": "UDF_TYPE_TABLE"
```

`}` `],`

```json
      "artifactType": "ARTIFACT_TYPE_JAVA",
      "createTime": "2024-03-08T08:13:54Z",
      "uploader": "223474909869445380",
      "jarUpdateTime": "2024-03-08T08:13:57Z",
      "name": "namespaces/flinkteam/udfartifacts/metric-transform-227-shaded",
      "namespace": "namespaces/flinkteam",
      "jarUrl": "hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/udfs/metric-transform-2
27-shaded/2024-03-08T08-13-54.732313Z/metric-transform-2.2.7-shaded.jar",
      "updateTime": "2024-03-08T08:13:57Z"
```

`}` `},`

```json
  "requestId": "C44A1880-5138-4204-9165-DC65C4B059C2",
  "success": true
```

`}` `XML` format

```xml
<data>
 <@type>type.googleapis.com/vvp.sql.v1beta1.GetUdfArtifactResponse</@type>
 <udfArtifact>
  <dependencyJarUris  />
  <udfClasses>
   <functionNames>TimestampProbe</functionNames>
   <udfArtifactName>namespaces/flinkteam/udfartifacts/metric-transform-227-shaded</udfArtifa
ctName>
   <className>com.alibaba.blink.udtf.TimestampProbe</className>
   <classType>UDF_TYPE_SCALAR</classType>
  </udfClasses>
  <udfClasses>
   <functionNames>TransformUdtf</functionNames>
   <udfArtifactName>namespaces/flinkteam/udfartifacts/metric-transform-227-shaded</udfArtifa
ctName>
   <className>com.alibaba.blink.udtf.TransformUdtf</className>
   <classType>UDF_TYPE_TABLE</classType>
  </udfClasses>
  <artifactType>ARTIFACT_TYPE_JAVA</artifactType>
  <createTime>2024-03-08T08:13:54Z</createTime>
  <uploader>223474909869445380</uploader>
  <jarUpdateTime>2024-03-08T08:13:57Z</jarUpdateTime>
  <name>namespaces/flinkteam/udfartifacts/metric-transform-227-shaded</name>
  <namespace>namespaces/flinkteam</namespace>
  <jarUrl>hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/udfs/metric-transform-227-
shaded/2024-03-08T08-13-54.732313Z/metric-transform-2.2.7-shaded.jar</jarUrl>
  <updateTime>2024-03-08T08:13:57Z</updateTime>
 </udfArtifact>
</data> <requestId>C44A1880-5138-4204-9165-DC65C4B059C2</requestId> <success>true</success>
```

ververica 2020-05-01

#### 3.1.66 ListConnectors

Queries a list of connectors.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "connectors": [ { "lookup": false, "supportedFormats" : [], "environments": [ "PUBLIC CLOUD", _ "PRIVATE CLOUD", _ "ALIBABA GROUP", _ "VVC CLOUD" ], _ "sink": false, "name": "namespaces/flinkte am/connectors/data gen", "source": true, "type": "datagen", "properties": [ { "defaultValue": "", "description": "Must be set to \u0027datagen\u00 27 to configure this connector.", "definesFormat": false, "key": "connector", "required": true }, { "defaultValue": "", "description": "Rows per second to control the emit rate, default 10000L.", "definesFormat": false, "key": "rows- per-second", "required": false }, { "defaultValue": "", "description": "Total number of rows to emit. By default, the source is unbounded.", "definesFormat": false, "key": "number-of-rows", "required": false } ], "packaged": true, "dependencies": [] } ], "@type": "type.googleapis.co m/vvp.sql.v1beta1.L istConnectorsRespo nse" } | The detailed data. |
| requestId | String | A62F262E-3055- 490B-B17B- 0C6BF83C4BE6 | The request ID. |

Sample requests

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1 &RegionId= &workspace= &namespace= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "data": {
    "connectors": [
```

`{`

```json
        "lookup": false,
        "supportedFormats": [],
        "environments": [
          "PUBLIC_CLOUD",
          "PRIVATE_CLOUD",
          "ALIBABA_GROUP",
          "VVC_CLOUD"
```

`],`

```json
        "sink": false,
        "name": "namespaces/flinkteam/connectors/datagen",
        "source": true,
        "type": "datagen",
        "properties": [
```

`{`

```json
            "defaultValue": "",
            "description": "Must be set to \u0027datagen\u0027 to configure this
connector.",
            "definesFormat": false,
            "key": "connector",
            "required": true
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Rows per second to control the emit rate, default 10000L.",
            "definesFormat": false,
            "key": "rows-per-second",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Total number of rows to emit. By default, the source is unbounde
d.",
            "definesFormat": false,
            "key": "number-of-rows",
            "required": false
```

`}` `],`

```json
        "packaged": true,
        "dependencies": []
```

`}` `],`

```
    "@type": "type.googleapis.com/vvp.sql.v1beta1.ListConnectorsResponse"
```

`},`

```json
  "success": true,
  "requestId": "A62F262E-3055-490B-B17B-0C6BF83C4BE6"
```

`}` `XML` format

```xml
<data>
 <connectors>
  <lookup>false</lookup>
  <supportedFormats  />
  <environments>PUBLIC_CLOUD</environments>
  <environments>PRIVATE_CLOUD</environments>
  <environments>ALIBABA_GROUP</environments>
  <environments>VVC_CLOUD</environments>
  <sink>false</sink>
  <name>namespaces/flinkteam/connectors/datagen</name>
  <source>true</source>
  <type>datagen</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;datagen&#x27; to configure this connector.</description
```

`>`

```xml
   <definesFormat>false</definesFormat>
   <key>connector</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Rows per second to control the emit rate, default 10000L.</description>
   <definesFormat>false</definesFormat>
   <key>rows-per-second</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Total number of rows to emit. By default, the source is unbounded.</descript
ion>
   <definesFormat>false</definesFormat>
   <key>number-of-rows</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies  />
 </connectors>
 <@type>type.googleapis.com/vvp.sql.v1beta1.ListConnectorsResponse</@type>
</data> <success>true</success> <requestId>A62F262E-3055-490B-B17B-0C6BF83C4BE6</requestId>
```

#### 3.1.67 ListDatabases

Queries a list of databases in a catalog.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listDatabase HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env188-d01 | The region ID. |
| namespac e | String | Path | Yes | ververica | The name of the namespace to which the deployment belongs. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| cat | String | Path | Yes | vvp | The name of the catalog. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.ListDatabase sResponse", "databases": [ { "name": "default", "properties": {}, "comment": "The default database" } ] } | The detailed information. |
| requestId | String | 76F325D7-3EC4- 4E34-81A8- 18B92D7EE606 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listDatabase HTTP/1.1
```

Sample success responses `JSON` format `{`

```json
  "requestId": "76F325D7-3EC4-4E34-81A8-18B92D7EE606",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.ListDatabasesResponse",
    "databases": [{
      "name": "default",
      "properties": {
```

`},`

```json
      "comment": "The default database"
```

`}]` `}` `}` `XML` format

```xml
<requestId>76F325D7-3EC4-4E34-81A8-18B92D7EE606</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.ListDatabasesResponse</@type>
 <databases>
  <name>default</name>
  <properties  />
  <comment>The default database</comment>
 </databases>
</data>
```

#### 3.1.68 ListFlinkVersions

Queries a list of Flink engine versions.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/api/v1/flink-version-meta.json HTTP/1.1
```

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-*****-env***-d01 | The region ID. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
|   |   | { "defaultFlinkVersion Name": "vvr-6.0.0- flink-1.15", "flinkVersionMetada tas": [ { "supportFindUsedCa talogs": false, "useForJarFineGrain ed": false, "versionName": "vvr-3.0.9-flink- 1.12", "flinkVersion": "1.12", "useForSqlDeploym ents": true, "labels": {}, "features": { "supportFindUsedCa talogs": false, "supportDynamicLo gLevel": false, "supportDagExpansi on": false, "useForJarFineGrain ed": false, "supportNativeSave point": false, "supportStateComp atibility": false, "supportNativeK8s": false, "supportJvmDebug": false, "supportLogArchive" |   |

|   |   | : false, "useForSqlDeploym ents": true, "supportLogPaging": false }, "tarUrl": "hdfs:///vvp/data/sql - artifacts/namespace s/default/packaged- vvr-dist/vvr-3.0.9- flink-1.12/vvr-3.0.9- flink-1.12- dist.tar.gz", "supportStateComp atibility": false, "defaultFor": [], "imageTag": "1.12.0-vvr-3.0.9- 1109", "vvrVersion": "3.0.9", "status": |   |
|---|---|---|---|
| data | String | "DEPRECATED" }, { "supportFindUsedCa talogs": true, "useForJarFineGrain ed": false, "versionName": "vvr-4.0.18-flink- 1.13", "flinkVersion": "1.13", "useForSqlDeploym ents": true, "labels": {}, "features": { "supportFindUsedCa talogs": true, "supportDynamicLo gLevel": true, "supportDagExpansi on": false, "useForJarFineGrain ed": false, "supportNativeSave point": false, "supportStateComp atibility": true, "supportNativeK8s": false, "supportJvmDebug": true, "supportLogArchive" : true, "useForSqlDeploym ents": true, "supportLogPaging": true }, "tarUrl": "hdfs:///vvp/data/sql - artifacts/namespace s/default/packaged- vvr-dist/vvr-4.0.18- flink-1.13/vvr- 4.0.18-flink-1.13- dist.tar.gz", "supportStateComp atibility": true, "defaultFor": [], "imageTag": "1.13.0-vvr-4.0.18- 22", "vvrVersion": "4.0.18", "status": | The detailed information. |

|   |   | "DEPRECATED" }, { "supportFindUsedCa talogs": true, "useForJarFineGrain ed": false, "versionName": "vvr-6.0.0-flink- 1.15", "flinkVersion": "1.15", "useForSqlDeploym ents": true, "labels": {}, "features": { "supportFindUsedCa talogs": true, "supportDynamicLo gLevel": true, "supportDagExpansi on": false, "useForJarFineGrain ed": false, "supportNativeSave point": false, "supportStateComp atibility": true, "supportNativeK8s": false, "supportJvmDebug": true, "supportLogArchive" : true, "useForSqlDeploym ents": true, "supportLogPaging": true }, "tarUrl": "hdfs:///vvp/data/sql - artifacts/namespace s/default/packaged- vvr-dist/vvr-6.0.7- flink-1.15/vvr-6.0.7- flink-1.15- dist.tar.gz", "supportStateComp atibility": true, "defaultFor": [], "imageTag": "1.15.0-vvr-6.0.7- 29", "vvrVersion": "6.0.7", "status": "STABLE" } ] } |   |
|---|---|---|---|
| requestId | String | 63269B06-8027- 4CD0-9AB5- D9791B185B82 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/flink-version-meta.json HTTP/1.1 &RegionId= &workspace= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "data": {
    "defaultFlinkVersionName": "vvr-6.0.0-flink-1.15",
    "flinkVersionMetadatas": [
```

`{`

```json
        "supportFindUsedCatalogs": false,
        "features": {
          "supportFindUsedCatalogs": false,
          "supportDynamicLogLevel": false,
          "supportDagExpansion": false,
          "useForJarFineGrained": false,
          "supportNativeSavepoint": false,
          "supportStateCompatibility": false,
          "supportNativeK8s": false,
          "supportJvmDebug": false,
          "supportLogArchive": false,
          "useForSqlDeployments": false,
          "supportLogPaging": false
```

`},`

```json
        "useForJarFineGrained": false,
        "supportStateCompatibility": false,
        "defaultFor": [],
        "versionName": "vvr-1.0.8-flink-1.10",
        "imageTag": "1.10.0-vvr-1.0.8-1",
        "flinkVersion": "1.10",
        "vvrVersion": "1.0.8",
        "useForSqlDeployments": false,
        "status": "DEPRECATED",
        "labels": {}
```

`},` `{`

```json
        "supportFindUsedCatalogs": false,
        "features": {
          "supportFindUsedCatalogs": false,
          "supportDynamicLogLevel": false,
          "supportDagExpansion": false,
          "useForJarFineGrained": false,
          "supportNativeSavepoint": false,
          "supportStateCompatibility": false,
          "supportNativeK8s": false,
          "supportJvmDebug": false,
          "supportLogArchive": false,
          "useForSqlDeployments": false,
          "supportLogPaging": false
```

`},`

```json
        "useForJarFineGrained": false,
        "supportStateCompatibility": false,
"defaultFor":[],
```

```json
deauto :[],
        "versionName": "vvr-2.1.10-flink-1.11",
        "imageTag": "1.11.0-vvr-2.1.10-1151",
        "flinkVersion": "1.11",
        "vvrVersion": "2.1.10",
        "useForSqlDeployments": false,
        "status": "DEPRECATED",
        "labels": {}
```

`},` `{`

```json
        "supportFindUsedCatalogs": false,
        "useForJarFineGrained": false,
        "versionName": "vvr-3.0.9-flink-1.12",
        "flinkVersion": "1.12",
        "useForSqlDeployments": true,
        "labels": {},
        "features": {
          "supportFindUsedCatalogs": false,
          "supportDynamicLogLevel": false,
          "supportDagExpansion": false,
          "useForJarFineGrained": false,
          "supportNativeSavepoint": false,
          "supportStateCompatibility": false,
          "supportNativeK8s": false,
          "supportJvmDebug": false,
          "supportLogArchive": false,
          "useForSqlDeployments": true,
          "supportLogPaging": false
```

`},`

```json
        "tarUrl": "hdfs:///vvp/data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-3
.0.9-flink-1.12/vvr-3.0.9-flink-1.12-dist.tar.gz",
        "supportStateCompatibility": false,
        "defaultFor": [],
        "imageTag": "1.12.0-vvr-3.0.9-1109",
        "vvrVersion": "3.0.9",
        "status": "DEPRECATED"
```

`},` `{`

```json
        "supportFindUsedCatalogs": true,
        "useForJarFineGrained": false,
        "versionName": "vvr-4.0.18-flink-1.13",
        "flinkVersion": "1.13",
        "useForSqlDeployments": true,
        "labels": {},
        "features": {
          "supportFindUsedCatalogs": true,
          "supportDynamicLogLevel": true,
          "supportDagExpansion": false,
          "useForJarFineGrained": false,
          "supportNativeSavepoint": false,
          "supportStateCompatibility": true,
          "supportNativeK8s": false,
          "supportJvmDebug": true,
          "supportLogArchive": true,
          "useForSqlDeployments": true,
          "supportLogPaging": true
```

`},`

```json
"tarUrl":"hdfs:///vvp/data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-4
```

```json
        tarUrl: hdfs:///vvp/data/sqlartifacts/namespaces/default/packagedvvrdist/vvr4
.0.18-flink-1.13/vvr-4.0.18-flink-1.13-dist.tar.gz",
        "supportStateCompatibility": true,
        "defaultFor": [],
        "imageTag": "1.13.0-vvr-4.0.18-22",
        "vvrVersion": "4.0.18",
        "status": "DEPRECATED"
```

`},` `{`

```json
        "supportFindUsedCatalogs": true,
        "useForJarFineGrained": false,
        "versionName": "vvr-6.0.0-flink-1.15",
        "flinkVersion": "1.15",
        "useForSqlDeployments": true,
        "labels": {},
        "features": {
          "supportFindUsedCatalogs": true,
          "supportDynamicLogLevel": true,
          "supportDagExpansion": false,
          "useForJarFineGrained": false,
          "supportNativeSavepoint": false,
          "supportStateCompatibility": true,
          "supportNativeK8s": false,
          "supportJvmDebug": true,
          "supportLogArchive": true,
          "useForSqlDeployments": true,
          "supportLogPaging": true
```

`},`

```json
        "tarUrl": "hdfs:///vvp/data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-6
.0.7-flink-1.15/vvr-6.0.7-flink-1.15-dist.tar.gz",
        "supportStateCompatibility": true,
        "defaultFor": [],
        "imageTag": "1.15.0-vvr-6.0.7-29",
        "vvrVersion": "6.0.7",
        "status": "STABLE"
```

`}` `]` `},`

```json
  "requestId": "63269B06-8027-4CD0-9AB5-D9791B185B82",
  "success": true
```

`}` `XML` format

```xml
<data>
 <defaultFlinkVersionName>vvr-6.0.0-flink-1.15</defaultFlinkVersionName>
 <flinkVersionMetadatas>
  <supportFindUsedCatalogs>false</supportFindUsedCatalogs>
  <features>
   <supportFindUsedCatalogs>false</supportFindUsedCatalogs>
   <supportDynamicLogLevel>false</supportDynamicLogLevel>
   <supportDagExpansion>false</supportDagExpansion>
   <useForJarFineGrained>false</useForJarFineGrained>
   <supportNativeSavepoint>false</supportNativeSavepoint>
   <supportStateCompatibility>false</supportStateCompatibility>
   <supportNativeK8s>false</supportNativeK8s>
   <supportJvmDebug>false</supportJvmDebug>
```

```xml
   <supportLogArchive>false</supportLogArchive>
   <useForSqlDeployments>false</useForSqlDeployments>
   <supportLogPaging>false</supportLogPaging>
  </features>
  <useForJarFineGrained>false</useForJarFineGrained>
  <supportStateCompatibility>false</supportStateCompatibility>
  <defaultFor  />
  <versionName>vvr-1.0.8-flink-1.10</versionName>
  <imageTag>1.10.0-vvr-1.0.8-1</imageTag>
  <flinkVersion>1.10</flinkVersion>
  <vvrVersion>1.0.8</vvrVersion>
  <useForSqlDeployments>false</useForSqlDeployments>
  <status>DEPRECATED</status>
  <labels  />
 </flinkVersionMetadatas>
 <flinkVersionMetadatas>
  <supportFindUsedCatalogs>false</supportFindUsedCatalogs>
  <features>
   <supportFindUsedCatalogs>false</supportFindUsedCatalogs>
   <supportDynamicLogLevel>false</supportDynamicLogLevel>
   <supportDagExpansion>false</supportDagExpansion>
   <useForJarFineGrained>false</useForJarFineGrained>
   <supportNativeSavepoint>false</supportNativeSavepoint>
   <supportStateCompatibility>false</supportStateCompatibility>
   <supportNativeK8s>false</supportNativeK8s>
   <supportJvmDebug>false</supportJvmDebug>
   <supportLogArchive>false</supportLogArchive>
   <useForSqlDeployments>false</useForSqlDeployments>
   <supportLogPaging>false</supportLogPaging>
  </features>
  <useForJarFineGrained>false</useForJarFineGrained>
  <supportStateCompatibility>false</supportStateCompatibility>
  <defaultFor  />
  <versionName>vvr-2.1.10-flink-1.11</versionName>
  <imageTag>1.11.0-vvr-2.1.10-1151</imageTag>
  <flinkVersion>1.11</flinkVersion>
  <vvrVersion>2.1.10</vvrVersion>
  <useForSqlDeployments>false</useForSqlDeployments>
  <status>DEPRECATED</status>
  <labels  />
 </flinkVersionMetadatas>
 <flinkVersionMetadatas>
  <supportFindUsedCatalogs>false</supportFindUsedCatalogs>
  <useForJarFineGrained>false</useForJarFineGrained>
  <versionName>vvr-3.0.9-flink-1.12</versionName>
  <flinkVersion>1.12</flinkVersion>
  <useForSqlDeployments>true</useForSqlDeployments>
  <labels  />
  <features>
   <supportFindUsedCatalogs>false</supportFindUsedCatalogs>
   <supportDynamicLogLevel>false</supportDynamicLogLevel>
   <supportDagExpansion>false</supportDagExpansion>
   <useForJarFineGrained>false</useForJarFineGrained>
   <supportNativeSavepoint>false</supportNativeSavepoint>
   <supportStateCompatibility>false</supportStateCompatibility>
   <supportNativeK8s>false</supportNativeK8s>
   <supportJvmDebug>false</supportJvmDebug>
```

```xml
   <supportLogArchive>false</supportLogArchive>
   <useForSqlDeployments>true</useForSqlDeployments>
   <supportLogPaging>false</supportLogPaging>
  </features>
  <tarUrl>hdfs:///vvp/data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-3.0.9-
flink-1.12/vvr-3.0.9-flink-1.12-dist.tar.gz</tarUrl>
  <supportStateCompatibility>false</supportStateCompatibility>
  <defaultFor  />
  <imageTag>1.12.0-vvr-3.0.9-1109</imageTag>
  <vvrVersion>3.0.9</vvrVersion>
  <status>DEPRECATED</status>
 </flinkVersionMetadatas>
 <flinkVersionMetadatas>
  <supportFindUsedCatalogs>true</supportFindUsedCatalogs>
  <useForJarFineGrained>false</useForJarFineGrained>
  <versionName>vvr-4.0.18-flink-1.13</versionName>
  <flinkVersion>1.13</flinkVersion>
  <useForSqlDeployments>true</useForSqlDeployments>
  <labels  />
  <features>
   <supportFindUsedCatalogs>true</supportFindUsedCatalogs>
   <supportDynamicLogLevel>true</supportDynamicLogLevel>
   <supportDagExpansion>false</supportDagExpansion>
   <useForJarFineGrained>false</useForJarFineGrained>
   <supportNativeSavepoint>false</supportNativeSavepoint>
   <supportStateCompatibility>true</supportStateCompatibility>
   <supportNativeK8s>false</supportNativeK8s>
   <supportJvmDebug>true</supportJvmDebug>
   <supportLogArchive>true</supportLogArchive>
   <useForSqlDeployments>true</useForSqlDeployments>
   <supportLogPaging>true</supportLogPaging>
  </features>
  <tarUrl>hdfs:///vvp/data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-4.0.18-
flink-1.13/vvr-4.0.18-flink-1.13-dist.tar.gz</tarUrl>
  <supportStateCompatibility>true</supportStateCompatibility>
  <defaultFor  />
  <imageTag>1.13.0-vvr-4.0.18-22</imageTag>
  <vvrVersion>4.0.18</vvrVersion>
  <status>DEPRECATED</status>
 </flinkVersionMetadatas>
 <flinkVersionMetadatas>
  <supportFindUsedCatalogs>true</supportFindUsedCatalogs>
  <useForJarFineGrained>false</useForJarFineGrained>
  <versionName>vvr-6.0.0-flink-1.15</versionName>
  <flinkVersion>1.15</flinkVersion>
  <useForSqlDeployments>true</useForSqlDeployments>
  <labels  />
  <features>
   <supportFindUsedCatalogs>true</supportFindUsedCatalogs>
   <supportDynamicLogLevel>true</supportDynamicLogLevel>
   <supportDagExpansion>false</supportDagExpansion>
   <useForJarFineGrained>false</useForJarFineGrained>
   <supportNativeSavepoint>false</supportNativeSavepoint>
   <supportStateCompatibility>true</supportStateCompatibility>
   <supportNativeK8s>false</supportNativeK8s>
   <supportJvmDebug>true</supportJvmDebug>
   <supportLogArchive>true</supportLogArchive>
```

```xml
   <useForSqlDeployments>true</useForSqlDeployments>
   <supportLogPaging>true</supportLogPaging>
  </features>
  <tarUrl>hdfs:///vvp/data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-6.0.7-
flink-1.15/vvr-6.0.7-flink-1.15-dist.tar.gz</tarUrl>
  <supportStateCompatibility>true</supportStateCompatibility>
  <defaultFor  />
  <imageTag>1.15.0-vvr-6.0.7-29</imageTag>
  <vvrVersion>6.0.7</vvrVersion>
  <status>STABLE</status>
 </flinkVersionMetadatas>
</data> <requestId>63269B06-8027-4CD0-9AB5-D9791B185B82</requestId> <success>true</success>
```

ververica 2020-05-01

#### 3.1.69 ListFormats

Queries a list of formats.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env188-d01 | The region ID. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| udfArtifact Name | String | Path | Yes | myudf | The name of the user- defined function (UDF). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "formats": [ { "sink": true, "name": "namespaces/flinkte am/formats/avro", "source": true, "type": "avro", "properties": [ { "defaultValue": "", "description": "Must be set to \u0027avro\u0027 to configure this format.", "definesFormat": false, "key": "format", "required": true } ], "packaged": true, "dependencies": [ "hdfs:///vvp/data/sql - artifacts/namespace s/ververica/connect ors/vvr-6.0.7-flink- 1.15/opt/formats/avr o/flink-sql-avro-1.15- vvr-6.0.7- SNAPSHOT.jar" ] } ], "@type": "type.googleapis.co m/vvp.sql.v1beta1.L istFormatsResponse " } | The detailed information. |
| requestId | String | 6BFF2035-B5FB- 4E1A-8F32- 4CA636417A3D | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1
```

Sample success responses `JSON` format `{`

```json
  "data": {
    "formats": [
```

`{`

```json
        "sink": true,
        "name": "namespaces/flinkteam/formats/avro",
        "source": true,
        "type": "avro",
```

```json
        "properties": [
```

`{`

```json
            "defaultValue": "",
            "description": "Must be set to \u0027avro\u0027 to configure this format.",
            "definesFormat": false,
            "key": "format",
            "required": true
```

`}` `],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/avro/flink-sql-avro-1.15-vvr-6.0.7-SNAPSHOT.jar"
```

`]` `},` `{`

```json
        "sink": true,
        "name": "namespaces/flinkteam/formats/avro-confluent",
        "source": true,
        "type": "avro-confluent",
        "properties": [
```

`{`

```json
            "defaultValue": "",
            "description": "Must be set to \u0027avro-confluent\u0027 to configure this form
at.",
            "definesFormat": false,
            "key": "format",
            "required": true
```

`},` `{`

```json
            "defaultValue": "",
            "description": "The URL of the Confluent Schema Registry to fetch/register schem
as.",
            "definesFormat": false,
            "key": "schema-registry.url",
            "required": true
```

`},` `{`

```json
            "defaultValue": "",
            "description": "The Confluent Schema Registry subject under which to register th
e schema used by this format during serialization. Required for sink table.",
            "definesFormat": false,
            "key": "schema-registry.subject",
            "required": false
```

`}` `],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/avro-confluent/flink-sql-avro-confluent-registry-1.15-vvr-6.0.7- SNAPSHOT.jar"
```

`]` `},` `{`

```json
        "sink": true,
        "name": "namespaces/flinkteam/formats/canal-json",
        "source": true,
```

```json
        "type": "canal-json",
        "properties": [
```

`{`

```json
            "defaultValue": "",
            "description": "Must be set to \u0027canal-json\u0027 to configure this
format.",
            "definesFormat": false,
            "key": "format",
            "required": true
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional flag to skip fields and rows with parse errors instead
of failing; fields are set to null in case of errors, false by default.",
            "definesFormat": false,
            "key": "ignore-parse-errors",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional flag to use Jackson Stream API to deserialize json obje
ct, which brings 30% performance gain.",
            "definesFormat": false,
            "key": "fast-deserialization",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional flag to specify timestamp format, SQL by default. Optio
n ISO-8601 will parse input timestamp in \"yyyy-MM-ddTHH:mm:ss.s{precision}\" format and out put timestamp in the same format. Option SQL will parse input timestamp in \"yyyy-MM-dd HH:m m:ss.s{precision}\" format and output timestamp in the same format.",
            "definesFormat": false,
            "key": "timestamp-format.standard",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Only read changelog rows which match the specific database (by c
omparing the \"database\" meta field in the record).",
            "definesFormat": false,
            "key": "database.include",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Only read changelog rows which match the specific table (by comp
aring the \"table\" meta field in the record).",
            "definesFormat": false,
            "key": "table.include",
            "required": false
```

`}` `],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar"
```

`]` `},` `{`

```json
        "sink": true,
        "name": "namespaces/flinkteam/formats/csv",
        "source": true,
        "type": "csv",
        "properties": [
```

`{`

```json
            "defaultValue": "",
            "description": "Must be set to \u0027csv\u0027 to configure this format.",
            "definesFormat": false,
            "key": "format",
            "required": true
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional field delimiter character (\u0027,\u0027 by default).",
            "definesFormat": false,
            "key": "field-delimiter",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional flag to disabled quote character for enclosing field va
lues (false by default). If true, quote-character can not be set.",
            "definesFormat": false,
            "key": "disable-quote-character",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional quote character for enclosing field values
(\u0027\"\u0027 by default).",
            "definesFormat": false,
            "key": "quote-character",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional flag to ignore comment lines that start with
\u0027#\u0027(disabled by default); if enabled, make sure to also ignore parse errors to allow empty rows.",
            "definesFormat": false,
            "key": "allow-comments",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional flag to skip fields and rows with parse errors instead
of failing; fields are set to null in case of errors.",
            "definesFormat": false,
            "key": "ignore-parse-errors",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
```

```json
            "description": "Optional array element delimiter string for separating array and
row element values (\u0027;\u0027 by default).",
            "definesFormat": false,
            "key": "array-element-delimiter",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional escape character for escaping values (disabled by defau
lt).",
            "definesFormat": false,
            "key": "escape-character",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional null literal string that is interpreted as a null value
(disabled by default).",
            "definesFormat": false,
            "key": "null-literal",
            "required": false
```

`}` `],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/csv/flink-csv-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar"
```

`]` `},` `{`

```json
        "sink": true,
        "name": "namespaces/flinkteam/formats/debezium-avro-confluent",
        "source": true,
        "type": "debezium-avro-confluent",
        "properties": [
```

`{`

```json
            "defaultValue": "",
            "description": "Must be set to \u0027debezium-avro-confluent\u0027 to configure
this format.",
            "definesFormat": false,
            "key": "format",
            "required": true
```

`},` `{`

```json
            "defaultValue": "",
            "description": "The URL of the Confluent Schema Registry to fetch/register schem
as.",
            "definesFormat": false,
            "key": "url",
            "required": true
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Basic auth credentials source for Schema Registry.",
            "definesFormat": false,
            "key": "basic-auth.credentials-source",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Basic auth user info for schema registry.",
            "definesFormat": false,
            "key": "basic-auth.user-info",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Bearer auth credentials source for Schema Registry.",
            "definesFormat": false,
            "key": "bearer-auth.credentials-source",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Bearer auth token for Schema Registry.",
            "definesFormat": false,
            "key": "bearer-auth.token",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Properties map that is forwarded to the underlying Schema Regist
ry. This is useful for options that are not officially exposed via Flink config options. However, note that Flink options have higher precedence.",
            "definesFormat": false,
            "key": "properties",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Location / File of SSL keystore.",
            "definesFormat": false,
            "key": "ssl.keystore.location",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Password for SSL keystore",
            "definesFormat": false,
            "key": "ssl.keystore.password",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Location / File of SSL truststore.",
            "definesFormat": false,
            "key": "ssl.truststore.location",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Password for SSL truststore.",
            "definesFormat": false,
            "key": "ssl.truststore.password",
```

`y` `p` `,`

```json
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "The Confluent Schema Registry subject under which to register th
e schema used by this format during serialization. By default, \u0027kafka\u0027 and \u0027upsert-kafka\u0027 connectors use \u0027\u003ctopic_name\u003e-value\u0027 or \u0027\u 003ctopic_name\u003e-key\u0027 as the default subject name if this format is used as the value or key format. But for other connectors (e.g. \u0027filesystem\u0027), the subject option is required when used as sink.",
            "definesFormat": false,
            "key": "subject",
            "required": false
```

`}` `],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/avro-confluent/flink-sql-avro-confluent-registry-1.15-vvr-6.0.7- SNAPSHOT.jar"
```

`]` `},` `{`

```json
        "sink": true,
        "name": "namespaces/flinkteam/formats/debezium-json",
        "source": true,
        "type": "debezium-json",
        "properties": [
```

`{`

```json
            "defaultValue": "",
            "description": "Must be set to \u0027debezium-json\u0027 to configure this forma
t.",
            "definesFormat": false,
            "key": "format",
            "required": true
```

`},` `{`

```json
            "defaultValue": "",
            "description": "When setting up a Debezium Kafka Connect, users can enable a Kaf
ka configuration \u0027value.converter.schemas.enable\u0027 to include schema in the message . This option indicates the Debezium JSON data include the schema in the message or not. Default is false.",
            "definesFormat": false,
            "key": "schema-include",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional flag to skip fields and rows with parse errors instead
of failing; fields are set to null in case of errors, false by default.",
            "definesFormat": false,
            "key": "ignore-parse-errors",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
"description":"OptionalflagtouseJacksonStreamAPItodeserializejsonobje
```

```json
            description: Optional flag to use Jackson Stream API to deserialize json obje
ct, which brings 30% performance gain.",
            "definesFormat": false,
            "key": "fast-deserialization",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional flag to specify timestamp format, SQL by default. Optio
n ISO-8601 will parse input timestamp in \"yyyy-MM-ddTHH:mm:ss.s{precision}\" format and out put timestamp in the same format. Option SQL will parse input timestamp in \"yyyy-MM-dd HH:m m:ss.s{precision}\" format and output timestamp in the same format.",
            "definesFormat": false,
            "key": "timestamp-format.standard",
            "required": false
```

`}` `],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar"
```

`]` `},` `{`

```json
        "sink": true,
        "name": "namespaces/flinkteam/formats/json",
        "source": true,
        "type": "json",
        "properties": [
```

`{`

```json
            "defaultValue": "",
            "description": "Must be set to \u0027json\u0027 to configure this format.",
            "definesFormat": false,
            "key": "format",
            "required": true
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional flag to specify whether to fail if a field is missing o
r not, false by default.",
            "definesFormat": false,
            "key": "fail-on-missing-field",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional flag to skip fields and rows with parse errors instead
of failing. Fields are set to null in case of errors, false by default.",
            "definesFormat": false,
            "key": "ignore-parse-errors",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional flag to use Jackson Stream API to deserialize json obje
ct, which brings 30% performance gain.",
            "definesFormat": false,
"key":"fast-deserialization"
```

```json
            key: fastdeserialization,
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional flag to specify timestamp format, SQL by default. Optio
n ISO-8601 will parse input timestamp in \"yyyy-MM-ddTHH:mm:ss.s{precision}\" format and out put timestamp in the same format. Option SQL will parse input timestamp in \"yyyy-MM-dd HH:m m:ss.s{precision}\" format and output timestamp in the same format.",
            "definesFormat": false,
            "key": "timestamp-format.standard",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional flag to recursively flatten the JSON OBJECT field into
columns in the top level schema. For a better understanding, the name of the flattened column will be composed of the path to get the column. For example, the field `col` in the json \"{ \\\"nested\\\": {\\\"col\\\": true} }\" is `nested.col` in the flattened schema. If the flattened field names get conflicts, currently the JsonParser will throw the exception t o stop the execution. Please use the option \"json.ignore-parse-errors\" to ignore the parse errors.",
            "definesFormat": false,
            "key": "infer-schema.flatten-nested-columns.enable",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Optional flag to infer primitive types as string type.",
            "definesFormat": false,
            "key": "infer-schema.primitive-as-string",
            "required": false
```

`}` `],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar"
```

`]` `},` `{`

```json
        "sink": true,
        "name": "namespaces/flinkteam/formats/maxwell-json",
        "source": true,
        "type": "maxwell-json",
        "properties": [
```

`{`

```json
            "defaultValue": "",
            "description": "Must be set to \u0027maxwell-json\u0027 to configure this format
.",
            "definesFormat": false,
            "key": "format",
            "required": true
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Skip fields and rows with parse errors instead of failing. Field
saresettonullincaseoferrors"
```

```json
s are set to null in case of errors.",
            "definesFormat": false,
            "key": "ignore-parse-errors",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Specify the input and output timestamp format. Currently support
ed values are \u0027SQL\u0027 and \u0027ISO-8601\u0027. Option \u0027SQL\u0027 will parse in put timestamp in \"yyyy-MM-dd HH:mm:ss.s{precision}\" format, e.g \u00272020-12-30 12:13:14. 123\u0027 and output timestamp in the same format. Option \u0027ISO-8601\u0027will parse input timestamp in \"yyyy-MM-ddTHH:mm:ss.s{precision}\" format, e.g \u00272020-12-30T12:13:1 4.123\u0027 and output timestamp in the same format.",
            "definesFormat": false,
            "key": "timestamp-format.standard",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Specify string literal to replace null key when \u0027maxwell-js
on.map-null-key.mode\u0027 is LITERAL.",
            "definesFormat": false,
            "key": "map-null-key.literal",
            "required": false
```

`}` `],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar"
```

`]` `},` `{`

```json
        "sink": true,
        "name": "namespaces/flinkteam/formats/orc",
        "source": true,
        "type": "orc",
        "properties": [
```

`{`

```json
            "defaultValue": "",
            "description": "Must be set to \u0027orc\u0027 to configure this format.",
            "definesFormat": false,
            "key": "format",
            "required": true
```

`}` `],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/orc/flink-sql-orc-1.15-vvr-6.0.7-SNAPSHOT.jar"
```

`]` `},` `{`

```json
        "sink": true,
        "name": "namespaces/flinkteam/formats/parquet",
        "source": true,
        "type": "parquet",
```

`"` `ti` `"` `[`

```json
        "properties": [
```

`{`

```json
            "defaultValue": "",
            "description": "Must be set to \u0027parquet\u0027 to configure this format.",
            "definesFormat": false,
            "key": "format",
            "required": true
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Use UTC timezone or local timezone to the conversion between epo
ch time and LocalDateTime. Hive 0.x/1.x/2.x use local timezone. But Hive 3.x use UTC timezone.",
            "definesFormat": false,
            "key": "utc-timezone",
            "required": false
```

`}` `],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/parquet/flink-sql-parquet-1.15-vvr-6.0.7-SNAPSHOT.jar"
```

`]` `},` `{`

```json
        "sink": true,
        "name": "namespaces/flinkteam/formats/raw",
        "source": true,
        "type": "raw",
        "properties": [
```

`{`

```json
            "defaultValue": "",
            "description": "Must be set to \u0027raw\u0027 to configure this format.",
            "definesFormat": false,
            "key": "format",
            "required": true
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Specify the charset to encode the text string. \u0027UTF-8\u0027
will be used by default.",
            "definesFormat": false,
            "key": "charset",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "Specify the endianness to encode the bytes of numeric value. Val
id values are \u0027big-endian\u0027 and \u0027little-endian\u0027. \u0027big-endian\u0027 will be used by default.",
            "definesFormat": false,
            "key": "endianness",
            "required": false
```

`}` `],`

```json
        "packaged": true,
        "dependencies": []
```

`}` `],`

```
    "@type": "type.googleapis.com/vvp.sql.v1beta1.ListFormatsResponse"
```

`},`

```json
  "success": true,
  "requestId": "6BFF2035-B5FB-4E1A-8F32-4CA636417A3D"
```

`}` `XML` format

```xml
<data>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/avro</name>
  <source>true</source>
  <type>avro</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;avro&#x27; to configure this format.</description>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/avro/flink-sql-avro-1.15-vvr-6.0.7-SNAPSHOT.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/avro-confluent</name>
  <source>true</source>
  <type>avro-confluent</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;avro-confluent&#x27; to configure this format.</descrip
tion>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>The URL of the Confluent Schema Registry to fetch/register schemas.
</description>
   <definesFormat>false</definesFormat>
   <key>schema-registry.url</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>The Confluent Schema Registry subject under which to register the schema
used by this format during serialization. Required for sink table.</description>
   <definesFormat>false</definesFormat>
   <key>schema-registry.subject</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
```

```xml
pacagedtue/pacaged
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/avro-confluent/flink-sql-avro-confluent-registry-1.15-vvr-6.0.7- SNAPSHOT.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/canal-json</name>
  <source>true</source>
  <type>canal-json</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;canal-json&#x27; to configure this format.</description
```

`>`

```xml
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to skip fields and rows with parse errors instead of failing;
fields are set to null in case of errors, false by default.</description>
   <definesFormat>false</definesFormat>
   <key>ignore-parse-errors</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to use Jackson Stream API to deserialize json object, which br
ings 30% performance gain.</description>
   <definesFormat>false</definesFormat>
   <key>fast-deserialization</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to specify timestamp format, SQL by default. Option ISO-8601
will parse input timestamp in &quot;yyyy-MM-ddTHH:mm:ss.s{precision}&quot; format and output timestamp in the same format. Option SQL will parse input timestamp in &quot;yyyy-MMdd HH:mm:ss.s{precision}&quot; format and output timestamp in the same format. </description>
   <definesFormat>false</definesFormat>
   <key>timestamp-format.standard</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Only read changelog rows which match the specific database (by comparing
the &quot;database&quot; meta field in the record).</description>
   <definesFormat>false</definesFormat>
   <key>database.include</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Only read changelog rows which match the specific table (by comparing the &q
uot;table&quot; meta field in the record).</description> <definesFormat>false</definesFormat>
```

```xml
   <definesFormat>false</definesFormat>
   <key>table.include</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/csv</name>
  <source>true</source>
  <type>csv</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;csv&#x27; to configure this format.</description>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional field delimiter character (&#x27;,&#x27; by default).</description>
   <definesFormat>false</definesFormat>
   <key>field-delimiter</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to disabled quote character for enclosing field values (false
by default). If true, quote-character can not be set.</description>
   <definesFormat>false</definesFormat>
   <key>disable-quote-character</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional quote character for enclosing field values (&#x27;&quot;&#x27; by d
efault).</description>
   <definesFormat>false</definesFormat>
   <key>quote-character</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to ignore comment lines that start with &#x27;#&#x27;(disabled
by default); if enabled, make sure to also ignore parse errors to allow empty rows.</descrip tion>
   <definesFormat>false</definesFormat>
   <key>allow-comments</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to skip fields and rows with parse errors instead of failing;
fields are set to null in case of errors.</description>
   <definesFormat>false</definesFormat>
<key>ignore-parse-errors</key>
```

```xml
   <key>ignore-parse-errors</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional array element delimiter string for separating array and row element
values (&#x27;;&#x27; by default).</description>
   <definesFormat>false</definesFormat>
   <key>array-element-delimiter</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional escape character for escaping values (disabled by default).
</description>
   <definesFormat>false</definesFormat>
   <key>escape-character</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional null literal string that is interpreted as a null value (disabled b
y default).</description>
   <definesFormat>false</definesFormat>
   <key>null-literal</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/csv/flink-csv-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/debezium-avro-confluent</name>
  <source>true</source>
  <type>debezium-avro-confluent</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;debezium-avro-confluent&#x27; to configure this format.
</description>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>The URL of the Confluent Schema Registry to fetch/register schemas.
</description>
   <definesFormat>false</definesFormat>
   <key>url</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Basic auth credentials source for Schema Registry.</description>
   <definesFormat>false</definesFormat>
   <key>basic-auth.credentials-source</key>
<reqired>false</reqired>
```

```xml
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Basic auth user info for schema registry.</description>
   <definesFormat>false</definesFormat>
   <key>basic-auth.user-info</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Bearer auth credentials source for Schema Registry.</description>
   <definesFormat>false</definesFormat>
   <key>bearer-auth.credentials-source</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Bearer auth token for Schema Registry.</description>
   <definesFormat>false</definesFormat>
   <key>bearer-auth.token</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Properties map that is forwarded to the underlying Schema Registry. This is
useful for options that are not officially exposed via Flink config options. However, note that Flink options have higher precedence.</description>
   <definesFormat>false</definesFormat>
   <key>properties</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Location / File of SSL keystore.</description>
   <definesFormat>false</definesFormat>
   <key>ssl.keystore.location</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Password for SSL keystore</description>
   <definesFormat>false</definesFormat>
   <key>ssl.keystore.password</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Location / File of SSL truststore.</description>
   <definesFormat>false</definesFormat>
   <key>ssl.truststore.location</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Password for SSL truststore.</description>
   <definesFormat>false</definesFormat>
```

`k` `l`

```
d/k
```

```xml
   <key>ssl.truststore.password</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>The Confluent Schema Registry subject under which to register the schema
used by this format during serialization. By default, &#x27;kafka&#x27; and &#x27;upsertkafka&#x27; connectors use &#x27;&lt;topic_name&gt;-value&#x27; or &#x27;&lt;topic_name&gt;key&#x27; as the default subject name if this format is used as the value or key format. But for other connectors (e.g. &#x27;filesystem&#x27;), the subject option is required when used as sink.</description>
   <definesFormat>false</definesFormat>
   <key>subject</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/avro-confluent/flink-sql-avro-confluent-registry-1.15-vvr-6.0.7- SNAPSHOT.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/debezium-json</name>
  <source>true</source>
  <type>debezium-json</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;debezium-json&#x27; to configure this format.</descript
ion>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>When setting up a Debezium Kafka Connect, users can enable a Kafka configura
tion &#x27;value.converter.schemas.enable&#x27; to include schema in the message. This option indicates the Debezium JSON data include the schema in the message or not. Default is false.</description>
   <definesFormat>false</definesFormat>
   <key>schema-include</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to skip fields and rows with parse errors instead of failing;
fields are set to null in case of errors, false by default.</description>
   <definesFormat>false</definesFormat>
   <key>ignore-parse-errors</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to use Jackson Stream API to deserialize json object, which br
ings 30% performance gain.</description>
   <definesFormat>false</definesFormat>
   <key>fast-deserialization</key>
```

```xml
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to specify timestamp format, SQL by default. Option ISO-8601
will parse input timestamp in &quot;yyyy-MM-ddTHH:mm:ss.s{precision}&quot; format and output timestamp in the same format. Option SQL will parse input timestamp in &quot;yyyy-MMdd HH:mm:ss.s{precision}&quot; format and output timestamp in the same format. </description>
   <definesFormat>false</definesFormat>
   <key>timestamp-format.standard</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/json</name>
  <source>true</source>
  <type>json</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;json&#x27; to configure this format.</description>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to specify whether to fail if a field is missing or not, false
by default.</description>
   <definesFormat>false</definesFormat>
   <key>fail-on-missing-field</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to skip fields and rows with parse errors instead of failing.
Fields are set to null in case of errors, false by default.</description>
   <definesFormat>false</definesFormat>
   <key>ignore-parse-errors</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to use Jackson Stream API to deserialize json object, which br
ings 30% performance gain.</description>
   <definesFormat>false</definesFormat>
   <key>fast-deserialization</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to specify timestamp format, SQL by default. Option ISO-8601
will parse input timestamp in &quot;yyyy-MM-ddTHH:mm:ss.s{precision}&quot; format and
```

```xml
output timestamp in the same format. Option SQL will parse input timestamp in &quot;yyyy-MMdd HH:mm:ss.s{precision}&quot; format and output timestamp in the same format. </description>
   <definesFormat>false</definesFormat>
   <key>timestamp-format.standard</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to recursively flatten the JSON OBJECT field into columns in t
he top level schema. For a better understanding, the name of the flattened column will be c omposed of the path to get the column. For example, the field `col` in the json &quot;{ \&quot;nested\&quot;: {\&quot;col\&quot;: true} }&quot; is `nested.col` in the flattened sch ema. If the flattened field names get conflicts, currently the JsonParser will throw the exception to stop the execution. Please use the option &quot;json.ignore-parse-errors&quot; to ignore the parse errors.</description>
   <definesFormat>false</definesFormat>
   <key>infer-schema.flatten-nested-columns.enable</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to infer primitive types as string type.</description>
   <definesFormat>false</definesFormat>
   <key>infer-schema.primitive-as-string</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/maxwell-json</name>
  <source>true</source>
  <type>maxwell-json</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;maxwell-json&#x27; to configure this format.</descripti
on>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Skip fields and rows with parse errors instead of failing. Fields are set
to null in case of errors.</description>
   <definesFormat>false</definesFormat>
   <key>ignore-parse-errors</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Specify the input and output timestamp format. Currently supported values ar
e &#x27;SQL&#x27; and &#x27;ISO-8601&#x27;. Option &#x27;SQL&#x27; will parse input timestam p in &quot;yyyy-MM-dd HH:mm:ss.s{precision}&quot; format, e.g &#x27;2020-12-30 12:13:14.123&
```

```xml
#x27; and output timestamp in the same format. Option &#x27;ISO-8601&#x27;will parse input t
imestamp in &quot;yyyy-MM-ddTHH:mm:ss.s{precision}&quot; format, e.g &#x27;2020-12- 30T12:13:14.123&#x27; and output timestamp in the same format.</description>
   <definesFormat>false</definesFormat>
   <key>timestamp-format.standard</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Specify string literal to replace null key when &#x27;maxwell-json.map-null-
key.mode&#x27; is LITERAL.</description>
   <definesFormat>false</definesFormat>
   <key>map-null-key.literal</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/orc</name>
  <source>true</source>
  <type>orc</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;orc&#x27; to configure this format.</description>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/orc/flink-sql-orc-1.15-vvr-6.0.7-SNAPSHOT.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/parquet</name>
  <source>true</source>
  <type>parquet</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;parquet&#x27; to configure this format.</description>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Use UTC timezone or local timezone to the conversion between epoch time and
LocalDateTime. Hive 0.x/1.x/2.x use local timezone. But Hive 3.x use UTC timezone. </description>
   <definesFormat>false</definesFormat>
   <key>utc-timezone</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
```

```xml
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/parquet/flink-sql-parquet-1.15-vvr-6.0.7-SNAPSHOT.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/raw</name>
  <source>true</source>
  <type>raw</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;raw&#x27; to configure this format.</description>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Specify the charset to encode the text string. &#x27;UTF-8&#x27; will be use
d by default.</description>
   <definesFormat>false</definesFormat>
   <key>charset</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Specify the endianness to encode the bytes of numeric value. Valid values ar
e &#x27;big-endian&#x27; and &#x27;little-endian&#x27;. &#x27;big-endian&#x27; will be used by default.</description>
   <definesFormat>false</definesFormat>
   <key>endianness</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies  />
 </formats>
 <@type>type.googleapis.com/vvp.sql.v1beta1.ListFormatsResponse</@type>
</data> <success>true</success> <requestId>6BFF2035-B5FB-4E1A-8F32-4CA636417A3D</requestId>
```

#### 3.1.70 ListSecretValues

Queries a list of variables.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1
```

**Request parameters**

| Parameter | Type | Type | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-qingdao-env***-d01 | The region ID. |
| namespace | Strin g | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | 5CC1B23C-CCA3- 4283-B275- 0F969CDFD34F | The request ID. |

| data | String | { "metadata": { "totalSize": 1, "totalPage": 1 }, "apiVersion": "v1", "kind": "SecretValueList", "items": [ { "metadata": { "createdAt": "2024- 03-11T03:07:09Z", "modifiedAt": "2024-03- 11T03:07:09Z", "resourceVersion": 1, "name": "secretkey", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "modifier": "229852610122763 813", "creatorName": "flinkadmin", "modifierName": "flinkadmin" }, "id": "6dd63491-f0bf- 4af3-a38e- 7001d479addc", "labels": {} }, "apiVersion": "v1", "kind": "SecretValue", "spec": { "kind": "Plain", "value": "******" } } ] } | The detailed data. |
|---|---|---|---|

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1 &RegionId= &namespace= &workspace= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "data": {
    "metadata": {
      "totalSize": 1,
      "totalPage": 1
```

`},`

```json
    "apiVersion": "v1",
    "kind": "SecretValueList",
    "items": [
```

`{`

```json
        "metadata": {
          "createdAt": "2024-03-11T03:07:09Z",
          "modifiedAt": "2024-03-11T03:07:09Z",
          "resourceVersion": 1,
          "name": "secretkey",
          "namespace": "flinkteam",
          "annotations": {
            "creator": "229852610122763813",
            "modifier": "229852610122763813",
            "creatorName": "flinkadmin",
            "modifierName": "flinkadmin"
```

`},`

```json
          "id": "6dd63491-f0bf-4af3-a38e-7001d479addc",
          "labels": {}
```

`},`

```json
        "apiVersion": "v1",
        "kind": "SecretValue",
        "spec": {
          "kind": "Plain",
          "value": "******"
```

`}` `}` `]` `},`

```json
  "success": true,
  "requestId": "5CC1B23C-CCA3-4283-B275-0F969CDFD34F"
```

`}` `XML` format

```xml
<data>
 <metadata>
  <totalSize>1</totalSize>
  <totalPage>1</totalPage>
 </metadata>
 <apiVersion>v1</apiVersion>
 <kind>SecretValueList</kind>
 <items>
  <metadata>
   <createdAt>2024-03-11T03:07:09Z</createdAt>
   <modifiedAt>2024-03-11T03:07:09Z</modifiedAt>
   <resourceVersion>1</resourceVersion>
   <name>secretkey</name>
   <namespace>flinkteam</namespace>
   <annotations>
    <creator>229852610122763813</creator>
    <modifier>229852610122763813</modifier>
    <creatorName>flinkadmin</creatorName>
    <modifierName>flinkadmin</modifierName>
   </annotations>
   <id>6dd63491-f0bf-4af3-a38e-7001d479addc</id>
   <labels  />
  </metadata>
  <apiVersion>v1</apiVersion>
  <kind>SecretValue</kind>
  <spec>
   <kind>Plain</kind>
   <value>******</value>
  </spec>
 </items>
</data> <success>true</success> <requestId>5CC1B23C-CCA3-4283-B275-0F969CDFD34F</requestId>
```

ververica 2020-05-01

#### 3.1.71 ParseConnector

Parses custom connectors.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors:analyze-jars HTTP/1.1
```

**Request parameters**

| Parameter | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-*****-env***-d01 | The region ID. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| paramsJson | Strin g | Body | No | {"jarUris": ["hdfs:///vvp/data/sql- artifacts/namespaces/flinkt eam/custom- connectors/2024-03- 12T01-50- 56.079896Z/ververica- connector-hologres-1.15- vvr-6.0-fix.jar"]} | The paths of the custom connector JAR packages to be parsed. |
| namespace | Strin g | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
|   |   | {"connectors": [{"lookup":false,"su pportedFormats": [],"environments": [],"sink":true,"name" :"namespaces/flinkt eam/connectors/hol ogres- fix","source":true,"ty pe":"hologres- fix","properties": [{"defaultValue":"10 ","description":"","d efinesFormat":false, "key":"poolsize","re quired":false}, |   |

|   |   | {"defaultValue":"fal |   |
|---|---|---|---|
|   |   | se","description":""," definesFormat":false ,"key":"async","requ ired":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"cacheReloadTi meBlackList","requir ed":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"password","req uired":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"bhclientignor ebeforeupdate","req uired":false}, {"defaultValue":"10 00","description":"", "definesFormat":fals e,"key":"jdbcretrysle epinitms","required" :false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"insertifnotexi sts","required":false }, {"defaultValue":"25 6","description":""," definesFormat":false ,"key":"jdbcscanfetc hsize","required":fal se}, {"defaultValue":"- 1","description":""," definesFormat":false ,"key":"starttimems" ,"required":false}, {"defaultValue":"tru e","description":""," definesFormat":false ,"key":"jdbcenabled efaultfornotnullcolu mn","required":false }, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"binlog","requ ired":false}, {"defaultValue":"10 0","description":""," definesFormat":false ,"key":"binlogbatchr eadsize","required": false}, {"defaultValue":"50 0","description":""," definesFormat":false ,"key":"clientmaxpa use","required":fals e}, {"defaultValue":"2", |   |

|   |   | "description":"","defi nesFormat":false,"k ey":"errorcount","re quired":false}, {"defaultValue":"25 6","description":""," definesFormat":false ,"key":"jdbcwritebat chsize","required":fa lse}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"jdbcuselegac yputhandler","requir ed":false}, {"defaultValue":"12 8","description":""," definesFormat":false ,"key":"jdbcreadbatc hsize","required":fal se}, {"defaultValue":"4", "description":"","defi nesFormat":false,"k ey":"bhclientthread pool","required":fals e}, {"defaultValue":"1", "description":"","defi nesFormat":false,"k ey":"jdbcreadretryc ount","required":fals e}, {"defaultValue":"10 0000","description": "","definesFormat":f alse,"key":"cacheSiz e","required":false}, {"defaultValue":"10 000","description":"" ,"definesFormat":fal se,"key":"maxinque ue","required":false }, {"defaultValue":"10 0000","description": "","definesFormat":f alse,"key":"maxRow Count","required":fa lse}, {"defaultValue":"60 0000","description": "","definesFormat":f alse,"key":"bhclient asynctimeout","requ ired":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"enable direc _ t connect","required _ ":false}, {"defaultValue":"10 0","description":""," definesFormat":false ,"key":"rpcrequeste veryfailures","requir ed":false}, {"defaultValue":"fal |   |
|---|---|---|---|

|   |   | se","description":""," definesFormat":false ,"key":"usebhclient mode","required":fal se}, {"defaultValue":"tru e","description":""," definesFormat":false ,"key":"enablethrottl e","required":false}, {"defaultValue":"3", "description":"","defi nesFormat":false,"k ey":"connectionsize" ,"required":false}, {"defaultValue":"0", "description":"","defi nesFormat":false,"k ey":"jdbcreadtimeou tms","required":fals e}, {"defaultValue":"10 ","description":"","d efinesFormat":false, "key":"jdbcretrycou nt","required":false} , {"defaultValue":"Ex ception","descriptio n":"","definesFormat ":false,"key":"action oninsert","required": false}, {"defaultValue":"hol ogres- fix","description":""," definesFormat":false ,"key":"connector"," required":true}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"username","req uired":false}, {"defaultValue":"10 ","description":"","d efinesFormat":false, "key":"bhclientread erqueue","required" :false}, {"defaultValue":"1", "description":"","defi nesFormat":false,"k ey":"maxconcurrenc ypershard","require d":false}, {"defaultValue":"20 48","description":"", "definesFormat":fals e,"key":"bhclientasy ncqueue","required" :false}, {"defaultValue":"\\u 0002","description": "","definesFormat":f alse,"key":"arraydeli miter","required":fal se}, {"defaultValue":"2", "description":"","defi |   |
|---|---|---|---|

|   |   | nesFormat":false,"k ey":"bhclientwriterb atch","required":fals e}, {"defaultValue":"10 00","description":"", "definesFormat":fals e,"key":"sqlretryinte rval","required":fals e}, {"defaultValue":"90 000","description":"" ,"definesFormat":fal se,"key":"bhclientti meout","required":f alse}, {"defaultValue":"20 97152","description ":"","definesFormat" :false,"key":"jdbcwri tebatchbytesize","re quired":false}, {"defaultValue":"10 00","description":"", "definesFormat":fals e,"key":"binlogretryi ntervalms","require d":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"fieldnametol ower","required":fal se}, {"defaultValue":"tru e","description":""," definesFormat":false ,"key":"ignoredelete ","required":false}, {"defaultValue":"60 000","description":"" ,"definesFormat":fal se,"key":"storerpcti meout","required":f alse}, {"defaultValue":"def ault","description":"" ,"definesFormat":fal se,"key":"resource _ group","required":fa lse}, {"defaultValue":"10 0","description":""," definesFormat":false ,"key":"clientpause", "required":false}, {"defaultValue":"ins ertOrIgnore","descri ption":"","definesFor mat":false,"key":"m utatetype","required ":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"disablebinlo g","required":false}, {"defaultValue":"AL L","description":"","d efinesFormat":false, |   |
|---|---|---|---|

| data | String | "key":"cache","requi red":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"sink.parallelism ","required":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"jdbcbinlogslotn ame","required":fals e}, {"defaultValue":"10 0","description":""," definesFormat":false ,"key":"asynccapacit y","required":false}, {"defaultValue":"10 0","description":""," definesFormat":false ,"key":"cacheScanLi mit","required":false }, {"defaultValue":"20 971520","descriptio n":"","definesFormat ":false,"key":"jdbcwr itebatchtotalbytesiz e","required":false}, {"defaultValue":"5", "description":"","defi nesFormat":false,"k ey":"rpcretries","req uired":false}, {"defaultValue":"10 24","description":"", "definesFormat":fals e,"key":"bhclientrea derbatch","required ":false}, {"defaultValue":"60 000","description":"" ,"definesFormat":fal se,"key":"jdbcmetac achettl","required":f alse}, {"defaultValue":"tru e","description":""," definesFormat":false ,"key":"splitstrategy" ,"required":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"partitionrout er","required":false} , {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"connectionpool name","required":fal se}, {"defaultValue":"60 000","description":"" ,"definesFormat":fal se,"key":"jdbcconne ctionmaxidlems","re quired":false}, | The parsing results. |
|---|---|---|---|

|   |   | {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"dbname","requi red":true}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"enabletypen ormalization","requi red":false}, {"defaultValue":"26 2144","description": "","definesFormat":f alse,"key":"splitdata size","required":fals e}, {"defaultValue":"60 000","description":"" ,"definesFormat":fal se,"key":"binlogrequ esttimeoutms","req uired":false}, {"defaultValue":"32 ","description":"","d efinesFormat":false, "key":"splitlength","r equired":false}, {"defaultValue":"18 0000","description": "","definesFormat":f alse,"key":"asynctim eoutms","required":f alse}, {"defaultValue":"bin ary","description":"", "definesFormat":fals e,"key":"jdbccopyfor mat","required":fals e}, {"defaultValue":"50 00","description":"", "definesFormat":fals e,"key":"jdbcretrysle epstepms","required ":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"userpcmode","r equired":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"cdcmode","r equired":false}, {"defaultValue":"tru e","description":""," definesFormat":false ,"key":"enableBinar yCache","required":f alse}, {"defaultValue":"10 000","description":"" ,"definesFormat":fal se,"key":"jdbcwritefl ushinterval","requir ed":false}, {"defaultValue":"10 0","description":""," |   |
|---|---|---|---|

|   |   | definesFormat":false ,"key":"shardrpcretri es","required":false }, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"partial- insert.enabled","req uired":false}, {"defaultValue":"60 ","description":"","d efinesFormat":false, "key":"jdbcscantime outseconds","requir ed":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"insertorupda te","required":false} , {"defaultValue":"10 00","description":"", "definesFormat":fals e,"key":"scanbatchsi ze","required":false }, {"defaultValue":"1", "description":"","defi nesFormat":false,"k ey":"asynccallbackp ool","required":false }, {"defaultValue":":"," description":"","defi nesFormat":false,"k ey":"primarykeysep" ,"required":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"createpartta ble","required":false }, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"reportmetric s","required":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"starttime","req uired":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"useholohub mode","required":fal se}, {"defaultValue":"un ordered","descriptio n":"","definesFormat ":false,"key":"asyncr esultorder","require d":false}, {"defaultValue":"25 6","description":""," definesFormat":false |   |
|---|---|---|---|

|   |   | ,"key":"jdbcreadbatc hqueuesize","requir ed":false}, {"defaultValue":"- 1","description":""," definesFormat":false ,"key":"jdbcmetaaut orefreshfactor","req uired":false}, {"defaultValue":"10 ","description":"","d efinesFormat":false, "key":"binlogmaxret rytimes","required":f alse}, {"defaultValue":"no ne","description":"", "definesFormat":fals e,"key":"sdkmode"," required":false}, {"defaultValue":"92 2337203685477580 7","description":""," definesFormat":false ,"key":"cacheTTLMs ","required":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"upsertsource ","required":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"bhclientignor edelete","required":f alse}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"remove- u0000-in- text.enabled","requi red":false}, {"defaultValue":"ear liestOffset","descript ion":"","definesForm at":false,"key":"binl ogstartupmode","re quired":false}, {"defaultValue":"10 0","description":""," definesFormat":false ,"key":"sqlretries","r equired":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"supportcolu mnstorageformat"," required":false}, {"defaultValue":"10 ","description":"","d efinesFormat":false, "key":"channelthrea dcount","required":f alse}, {"defaultValue":"fal se","description":""," definesFormat":false |   |
|---|---|---|---|

|   |   | ,"key":"ignorenullwh enupdate","required ":false}, {"defaultValue":"str eam","description":" ","definesFormat":fa lse,"key":" tablena __ me ","required":fal __ se}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"nullvalues","re quired":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"endpoint","req uired":true}, {"defaultValue":"10 000","description":"" ,"definesFormat":fal se,"key":"refreshint erval","required":fal se}, {"defaultValue":"\\u 0002","description": "","definesFormat":f alse,"key":"field deli _ miter","required":fal se}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"enable filter _ push down","requir _ _ ed":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"tablename","re quired":true}, {"defaultValue":"tru e","description":""," definesFormat":false ,"key":"cacheEmpty ","required":false}, {"defaultValue":"pu blic","description":"" ,"definesFormat":fal se,"key":"schemana me","required":false }, {"defaultValue":"60 0","description":""," definesFormat":false ,"key":"jdbcscantran sactionsessiontimeo utseconds","require d":false}],"package d":false,"dependenc ies": ["hdfs:///vvp/data/sq l- artifacts/namespace s/flinkteam/custom- connectors/2024- 03-12T01-50- 56.079896Z/ververi ca-connector- |   |
|---|---|---|---|

|   |   | hologres-1.15-vvr- 6.0- fix.jar"]}],"@type":"t ype.googleapis.com/ vvp.sql.v1beta1.Ana lyzeConnectorJarsRe sponse","duplicated SourceFactoriesCon nectors": [],"duplicatedSinkFa ctoriesConnectors": []} |   |
|---|---|---|---|
| requestId | String | 05AEEA60-8B59- 4CCD-9F35- B27EE47F4D4E | The request ID. |

Sample requests

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors:analyze-jars HTTP/1.1
```

`{`

```json
"RegionId":"", "workspace":"", "namespace":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "connectors": [
```

`{`

```json
        "lookup": false,
        "supportedFormats": [],
        "environments": [],
        "sink": true,
        "name": "namespaces/flinkteam/connectors/hologres-fix",
        "source": true,
        "type": "hologres-fix",
        "properties": [
```

`{`

```json
            "defaultValue": "10",
            "description": "",
            "definesFormat": false,
            "key": "poolsize",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "async",
            "required": false
```

`},` `,` `{`

```json
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "cacheReloadTimeBlackList",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "password",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "bhclientignorebeforeupdate",
            "required": false
```

`},` `{`

```json
            "defaultValue": "1000",
            "description": "",
            "definesFormat": false,
            "key": "jdbcretrysleepinitms",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "insertifnotexists",
            "required": false
```

`},` `{`

```json
            "defaultValue": "256",
            "description": "",
            "definesFormat": false,
            "key": "jdbcscanfetchsize",
            "required": false
```

`},` `{`

```json
            "defaultValue": "-1",
            "description": "",
            "definesFormat": false,
            "key": "starttimems",
            "required": false
```

`},` `{`

```json
            "defaultValue": "true",
            "description": "",
            "definesFormat": false,
            "key": "jdbcenabledefaultfornotnullcolumn",
            "required": false
```

`},` `{` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "binlog",
            "required": false
```

`},` `{`

```json
            "defaultValue": "100",
            "description": "",
            "definesFormat": false,
            "key": "binlogbatchreadsize",
            "required": false
```

`},` `{`

```json
            "defaultValue": "500",
            "description": "",
            "definesFormat": false,
            "key": "clientmaxpause",
            "required": false
```

`},` `{`

```json
            "defaultValue": "2",
            "description": "",
            "definesFormat": false,
            "key": "errorcount",
            "required": false
```

`},` `{`

```json
            "defaultValue": "256",
            "description": "",
            "definesFormat": false,
            "key": "jdbcwritebatchsize",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "jdbcuselegacyputhandler",
            "required": false
```

`},` `{`

```json
            "defaultValue": "128",
            "description": "",
            "definesFormat": false,
            "key": "jdbcreadbatchsize",
            "required": false
```

`},` `{`

```json
            "defaultValue": "4",
            "description": "",
            "definesFormat": false,
            "key": "bhclientthreadpool",
            "required": false
```

`},` `{`

```json
"defaultValue":"1",
```

```json
            defaultValue: 1,
            "description": "",
            "definesFormat": false,
            "key": "jdbcreadretrycount",
            "required": false
```

`},` `{`

```json
            "defaultValue": "100000",
            "description": "",
            "definesFormat": false,
            "key": "cacheSize",
            "required": false
```

`},` `{`

```json
            "defaultValue": "10000",
            "description": "",
            "definesFormat": false,
            "key": "maxinqueue",
            "required": false
```

`},` `{`

```json
            "defaultValue": "100000",
            "description": "",
            "definesFormat": false,
            "key": "maxRowCount",
            "required": false
```

`},` `{`

```json
            "defaultValue": "600000",
            "description": "",
            "definesFormat": false,
            "key": "bhclientasynctimeout",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "enable_direct_connect",
            "required": false
```

`},` `{`

```json
            "defaultValue": "100",
            "description": "",
            "definesFormat": false,
            "key": "rpcrequesteveryfailures",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "usebhclientmode",
            "required": false
```

`},` `{`

```json
            "defaultValue": "true",
"description":""
```

```
            description:
```

`,`

```json
            "definesFormat": false,
            "key": "enablethrottle",
            "required": false
```

`},` `{`

```json
            "defaultValue": "3",
            "description": "",
            "definesFormat": false,
            "key": "connectionsize",
            "required": false
```

`},` `{`

```json
            "defaultValue": "0",
            "description": "",
            "definesFormat": false,
            "key": "jdbcreadtimeoutms",
            "required": false
```

`},` `{`

```json
            "defaultValue": "10",
            "description": "",
            "definesFormat": false,
            "key": "jdbcretrycount",
            "required": false
```

`},` `{`

```json
            "defaultValue": "Exception",
            "description": "",
            "definesFormat": false,
            "key": "actiononinsert",
            "required": false
```

`},` `{`

```json
            "defaultValue": "hologres-fix",
            "description": "",
            "definesFormat": false,
            "key": "connector",
            "required": true
```

`},` `{`

```json
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "username",
            "required": false
```

`},` `{`

```json
            "defaultValue": "10",
            "description": "",
            "definesFormat": false,
            "key": "bhclientreaderqueue",
            "required": false
```

`},` `{`

```json
            "defaultValue": "1",
            "description": "",
"definesFormat" false
```

```json
            "definesFormat": false,
            "key": "maxconcurrencypershard",
            "required": false
```

`},` `{`

```json
            "defaultValue": "2048",
            "description": "",
            "definesFormat": false,
            "key": "bhclientasyncqueue",
            "required": false
```

`},` `{`

```json
            "defaultValue": "\u0002",
            "description": "",
            "definesFormat": false,
            "key": "arraydelimiter",
            "required": false
```

`},` `{`

```json
            "defaultValue": "2",
            "description": "",
            "definesFormat": false,
            "key": "bhclientwriterbatch",
            "required": false
```

`},` `{`

```json
            "defaultValue": "1000",
            "description": "",
            "definesFormat": false,
            "key": "sqlretryinterval",
            "required": false
```

`},` `{`

```json
            "defaultValue": "90000",
            "description": "",
            "definesFormat": false,
            "key": "bhclienttimeout",
            "required": false
```

`},` `{`

```json
            "defaultValue": "2097152",
            "description": "",
            "definesFormat": false,
            "key": "jdbcwritebatchbytesize",
            "required": false
```

`},` `{`

```json
            "defaultValue": "1000",
            "description": "",
            "definesFormat": false,
            "key": "binlogretryintervalms",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
```

`"k` `"`

```
"fild
```

`l` `"`

```json
            "key": "fieldnametolower",
            "required": false
```

`},` `{`

```json
            "defaultValue": "true",
            "description": "",
            "definesFormat": false,
            "key": "ignoredelete",
            "required": false
```

`},` `{`

```json
            "defaultValue": "60000",
            "description": "",
            "definesFormat": false,
            "key": "storerpctimeout",
            "required": false
```

`},` `{`

```json
            "defaultValue": "default",
            "description": "",
            "definesFormat": false,
            "key": "resource_group",
            "required": false
```

`},` `{`

```json
            "defaultValue": "100",
            "description": "",
            "definesFormat": false,
            "key": "clientpause",
            "required": false
```

`},` `{`

```json
            "defaultValue": "insertOrIgnore",
            "description": "",
            "definesFormat": false,
            "key": "mutatetype",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "disablebinlog",
            "required": false
```

`},` `{`

```json
            "defaultValue": "ALL",
            "description": "",
            "definesFormat": false,
            "key": "cache",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "sink.parallelism",
```

```json
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "jdbcbinlogslotname",
            "required": false
```

`},` `{`

```json
            "defaultValue": "100",
            "description": "",
            "definesFormat": false,
            "key": "asynccapacity",
            "required": false
```

`},` `{`

```json
            "defaultValue": "100",
            "description": "",
            "definesFormat": false,
            "key": "cacheScanLimit",
            "required": false
```

`},` `{`

```json
            "defaultValue": "20971520",
            "description": "",
            "definesFormat": false,
            "key": "jdbcwritebatchtotalbytesize",
            "required": false
```

`},` `{`

```json
            "defaultValue": "5",
            "description": "",
            "definesFormat": false,
            "key": "rpcretries",
            "required": false
```

`},` `{`

```json
            "defaultValue": "1024",
            "description": "",
            "definesFormat": false,
            "key": "bhclientreaderbatch",
            "required": false
```

`},` `{`

```json
            "defaultValue": "60000",
            "description": "",
            "definesFormat": false,
            "key": "jdbcmetacachettl",
            "required": false
```

`},` `{`

```json
            "defaultValue": "true",
            "description": "",
            "definesFormat": false,
            "key": "splitstrategy",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "partitionrouter",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "connectionpoolname",
            "required": false
```

`},` `{`

```json
            "defaultValue": "60000",
            "description": "",
            "definesFormat": false,
            "key": "jdbcconnectionmaxidlems",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "dbname",
            "required": true
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "enabletypenormalization",
            "required": false
```

`},` `{`

```json
            "defaultValue": "262144",
            "description": "",
            "definesFormat": false,
            "key": "splitdatasize",
            "required": false
```

`},` `{`

```json
            "defaultValue": "60000",
            "description": "",
            "definesFormat": false,
            "key": "binlogrequesttimeoutms",
            "required": false
```

`},` `{`

```json
            "defaultValue": "32",
            "description": "",
            "definesFormat": false,
            "key": "splitlength",
            "required": false
```

`},` `{`

```json
            "defaultValue": "180000",
            "description": "",
            "definesFormat": false,
            "key": "asynctimeoutms",
            "required": false
```

`},` `{`

```json
            "defaultValue": "binary",
            "description": "",
            "definesFormat": false,
            "key": "jdbccopyformat",
            "required": false
```

`},` `{`

```json
            "defaultValue": "5000",
            "description": "",
            "definesFormat": false,
            "key": "jdbcretrysleepstepms",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "userpcmode",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "cdcmode",
            "required": false
```

`},` `{`

```json
            "defaultValue": "true",
            "description": "",
            "definesFormat": false,
            "key": "enableBinaryCache",
            "required": false
```

`},` `{`

```json
            "defaultValue": "10000",
            "description": "",
            "definesFormat": false,
            "key": "jdbcwriteflushinterval",
            "required": false
```

`},` `{`

```json
            "defaultValue": "100",
            "description": "",
            "definesFormat": false,
            "key": "shardrpcretries",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "partial-insert.enabled",
            "required": false
```

`},` `{`

```json
            "defaultValue": "60",
            "description": "",
            "definesFormat": false,
            "key": "jdbcscantimeoutseconds",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "insertorupdate",
            "required": false
```

`},` `{`

```json
            "defaultValue": "1000",
            "description": "",
            "definesFormat": false,
            "key": "scanbatchsize",
            "required": false
```

`},` `{`

```json
            "defaultValue": "1",
            "description": "",
            "definesFormat": false,
            "key": "asynccallbackpool",
            "required": false
```

`},` `{`

```json
            "defaultValue": ":",
            "description": "",
            "definesFormat": false,
            "key": "primarykeysep",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "createparttable",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "reportmetrics",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
```

```json
            "description": "",
            "definesFormat": false,
            "key": "starttime",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "useholohubmode",
            "required": false
```

`},` `{`

```json
            "defaultValue": "unordered",
            "description": "",
            "definesFormat": false,
            "key": "asyncresultorder",
            "required": false
```

`},` `{`

```json
            "defaultValue": "256",
            "description": "",
            "definesFormat": false,
            "key": "jdbcreadbatchqueuesize",
            "required": false
```

`},` `{`

```json
            "defaultValue": "-1",
            "description": "",
            "definesFormat": false,
            "key": "jdbcmetaautorefreshfactor",
            "required": false
```

`},` `{`

```json
            "defaultValue": "10",
            "description": "",
            "definesFormat": false,
            "key": "binlogmaxretrytimes",
            "required": false
```

`},` `{`

```json
            "defaultValue": "none",
            "description": "",
            "definesFormat": false,
            "key": "sdkmode",
            "required": false
```

`},` `{`

```json
            "defaultValue": "9223372036854775807",
            "description": "",
            "definesFormat": false,
            "key": "cacheTTLMs",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
```

`p` `,`

```json
            "definesFormat": false,
            "key": "upsertsource",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "bhclientignoredelete",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "remove-u0000-in-text.enabled",
            "required": false
```

`},` `{`

```json
            "defaultValue": "earliestOffset",
            "description": "",
            "definesFormat": false,
            "key": "binlogstartupmode",
            "required": false
```

`},` `{`

```json
            "defaultValue": "100",
            "description": "",
            "definesFormat": false,
            "key": "sqlretries",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "supportcolumnstorageformat",
            "required": false
```

`},` `{`

```json
            "defaultValue": "10",
            "description": "",
            "definesFormat": false,
            "key": "channelthreadcount",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "ignorenullwhenupdate",
            "required": false
```

`},` `{`

```json
            "defaultValue": "stream",
            "description": "",
"definesFormat":false,
```

```json
            definesFormat: false,
            "key": "__tablename__",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "nullvalues",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "endpoint",
            "required": true
```

`},` `{`

```json
            "defaultValue": "10000",
            "description": "",
            "definesFormat": false,
            "key": "refreshinterval",
            "required": false
```

`},` `{`

```json
            "defaultValue": "\u0002",
            "description": "",
            "definesFormat": false,
            "key": "field_delimiter",
            "required": false
```

`},` `{`

```json
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "enable_filter_push_down",
            "required": false
```

`},` `{`

```json
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "tablename",
            "required": true
```

`},` `{`

```json
            "defaultValue": "true",
            "description": "",
            "definesFormat": false,
            "key": "cacheEmpty",
            "required": false
```

`},` `{`

```json
            "defaultValue": "public",
            "description": "",
            "definesFormat": false,
"key":"schemaname"
```

```json
            key: schemaname,
            "required": false
```

`},` `{`

```json
            "defaultValue": "600",
            "description": "",
            "definesFormat": false,
            "key": "jdbcscantransactionsessiontimeoutseconds",
            "required": false
```

`}` `],`

```json
        "packaged": false,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/custom-connectors/2024-03-12T
01-50-56.079896Z/ververica-connector-hologres-1.15-vvr-6.0-fix.jar"
```

`]` `}` `],`

```json
    "@type": "type.googleapis.com/vvp.sql.v1beta1.AnalyzeConnectorJarsResponse",
    "duplicatedSourceFactoriesConnectors": [],
    "duplicatedSinkFactoriesConnectors": []
```

`},`

```json
  "success": true,
  "requestId": "05AEEA60-8B59-4CCD-9F35-B27EE47F4D4E"
```

`}` `XML` format

```xml
<data>
 <connectors>
  <lookup>false</lookup>
  <supportedFormats  />
  <environments  />
  <sink>true</sink>
  <name>namespaces/flinkteam/connectors/hologres-fix</name>
  <source>true</source>
  <type>hologres-fix</type>
  <properties>
   <defaultValue>10</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>poolsize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>async</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>cacheReloadTimeBlackList</key>
   <required>false</required>
```

```xml
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>password</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientignorebeforeupdate</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcretrysleepinitms</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>insertifnotexists</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>256</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcscanfetchsize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>-1</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>starttimems</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>true</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcenabledefaultfornotnullcolumn</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>binlog</key>
   <required>false</required>
  </properties>
```

```xml
  <properties>
   <defaultValue>100</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>binlogbatchreadsize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>500</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>clientmaxpause</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>2</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>errorcount</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>256</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcwritebatchsize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcuselegacyputhandler</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>128</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcreadbatchsize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>4</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientthreadpool</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcreadretrycount</key>
   <required>false</required>
  </properties>
  <properties>
```

`p` `p`

```xml
   <defaultValue>100000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>cacheSize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>10000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>maxinqueue</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>maxRowCount</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>600000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientasynctimeout</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>enable_direct_connect</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>rpcrequesteveryfailures</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>usebhclientmode</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>true</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>enablethrottle</key>
   <required>false</required>
  </properties>
  <properties>
<defaultValue>3</defaultValue>
```

```xml
deautaue3/deautaue
   <description  />
   <definesFormat>false</definesFormat>
   <key>connectionsize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>0</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcreadtimeoutms</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>10</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcretrycount</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>Exception</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>actiononinsert</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>hologres-fix</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>connector</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>username</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>10</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientreaderqueue</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>maxconcurrencypershard</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>2048</defaultValue>
<description
```

`/>`

```xml
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientasyncqueue</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue></defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>arraydelimiter</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>2</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientwriterbatch</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>sqlretryinterval</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>90000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclienttimeout</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>2097152</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcwritebatchbytesize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>binlogretryintervalms</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>fieldnametolower</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>true</defaultValue>
   <description  />
<definesFormat>false</definesFormat>
```

```xml
   <definesFormat>false</definesFormat>
   <key>ignoredelete</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>60000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>storerpctimeout</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>default</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>resource_group</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>clientpause</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>insertOrIgnore</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>mutatetype</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>disablebinlog</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>ALL</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>cache</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>sink.parallelism</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
<ke>jdbcbinlogslotname</ke>
```

```xml
   <key>jdbcbinlogslotname</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>asynccapacity</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>cacheScanLimit</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>20971520</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcwritebatchtotalbytesize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>5</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>rpcretries</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1024</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientreaderbatch</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>60000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcmetacachettl</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>true</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>splitstrategy</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>partitionrouter</key>
```

`i`

```
dfl
```

`/` `i` `d`

```xml
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>connectionpoolname</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>60000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcconnectionmaxidlems</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>dbname</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>enabletypenormalization</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>262144</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>splitdatasize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>60000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>binlogrequesttimeoutms</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>32</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>splitlength</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>180000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>asynctimeoutms</key>
   <required>false</required>
```

```xml
  </properties>
  <properties>
   <defaultValue>binary</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbccopyformat</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>5000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcretrysleepstepms</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>userpcmode</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>cdcmode</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>true</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>enableBinaryCache</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>10000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcwriteflushinterval</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>shardrpcretries</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>partial-insert.enabled</key>
   <required>false</required>
  </properties>
```

```xml
  <properties>
   <defaultValue>60</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcscantimeoutseconds</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>insertorupdate</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>scanbatchsize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>asynccallbackpool</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>:</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>primarykeysep</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>createparttable</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>reportmetrics</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>starttime</key>
   <required>false</required>
  </properties>
  <properties>
```

```xml
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>useholohubmode</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>unordered</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>asyncresultorder</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>256</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcreadbatchqueuesize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>-1</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcmetaautorefreshfactor</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>10</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>binlogmaxretrytimes</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>none</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>sdkmode</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>9223372036854775807</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>cacheTTLMs</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>upsertsource</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
```

```xml
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientignoredelete</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>remove-u0000-in-text.enabled</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>earliestOffset</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>binlogstartupmode</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>sqlretries</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>supportcolumnstorageformat</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>10</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>channelthreadcount</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>ignorenullwhenupdate</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>stream</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>__tablename__</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
```

```xml
   <definesFormat>false</definesFormat>
   <key>nullvalues</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>endpoint</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue>10000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>refreshinterval</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue></defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>field_delimiter</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>enable_filter_push_down</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>tablename</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue>true</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>cacheEmpty</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>public</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>schemaname</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>600</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
```

`/`

```xml
   <key>jdbcscantransactionsessiontimeoutseconds</key>
   <required>false</required>
  </properties>
  <packaged>false</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/custom-connectors/2024-0
3-12T01-50-56.079896Z/ververica-connector-hologres-1.15-vvr-6.0-fix.jar</dependencies>
 </connectors>
 <@type>type.googleapis.com/vvp.sql.v1beta1.AnalyzeConnectorJarsResponse</@type>
 <duplicatedSourceFactoriesConnectors  />
 <duplicatedSinkFactoriesConnectors  />
</data> <success>true</success> <requestId>05AEEA60-8B59-4CCD-9F35-B27EE47F4D4E</requestId>
```

ververica 2020-05-01

#### 3.1.72 ParseFormat

Parses formats.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats:analyze-jars HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env188-d01 | The region ID. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| paramsJso n | String | Body | No | { "jarUris": [ "hdfs:///vvp/data/sql- artifacts/namespaces/ver verica/connectors/vvr- 6.0.7-flink- 1.15/opt/formats/csv/flink- csv-1.15-vvr-6.0.7- SNAPSHOT-sql-jar.jar" ] } | The format JAR packages to be parsed. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| data | String | { "duplicatedSinkFact oriesFormats": [], "formats": [], "@type": "type.googleapis.co m/vvp.sql.v1beta1.A nalyzeFormatJarsRe sponse", "duplicatedFilesyste mFormatFactoriesFo rmats": [], "duplicatedSourceFa ctoriesFormats": [] } | The parsing results. |
| requestId | String | C95A189B-7314- 48BF-90B0- 2F27D1C8816F | The request ID. |

Sample requests

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats:analyze-jars HTTP/1.1
```

`{`

```json
"RegionId":"", "workspace":"", "namespace":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "duplicatedSinkFactoriesFormats": [],
    "formats": [],
    "@type": "type.googleapis.com/vvp.sql.v1beta1.AnalyzeFormatJarsResponse",
    "duplicatedFilesystemFormatFactoriesFormats": [],
    "duplicatedSourceFactoriesFormats": []
```

`},`

```json
  "success": true,
  "requestId": "C95A189B-7314-48BF-90B0-2F27D1C8816F"
```

`}` `XML` format

```xml
<data>
 <duplicatedSinkFactoriesFormats  />
 <formats  />
 <@type>type.googleapis.com/vvp.sql.v1beta1.AnalyzeFormatJarsResponse</@type>
 <duplicatedFilesystemFormatFactoriesFormats  />
 <duplicatedSourceFactoriesFormats  />
</data> <success>true</success> <requestId>C95A189B-7314-48BF-90B0-2F27D1C8816F</requestId>
```

#### 3.1.73 SearchFoldersByKeyword

Queries the details of a folder by keyword.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env188-d01 | The region ID. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| paramsJso n | String | Body | No | null | The parameters in the request body. |
| keyword | String | Query | No | my | The keyword for the query. |
| type | String | Query | No | development | The type. Set the value to development. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| data | String | [ { "name": "myfolder", "id": "e777f423-b4de- 434c-a6db- 23e88e080a5e", "type": "Folder" } ] | The details of the folder. |
| requestId | String | B29F2776-C7FF- 4740-9284- 1821297B0085 | The request ID. |

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders HTTP/1.1 &RegionId= &workspace= &namespace= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "data": [
```

`{`

```json
      "name": "myfolder",
      "id": "e777f423-b4de-434c-a6db-23e88e080a5e",
      "type": "Folder"
```

`}` `],`

```json
  "success": true,
  "requestId": "B29F2776-C7FF-4740-9284-1821297B0085"
```

`}` `XML` format

```xml
<data>
 <name>myfolder</name>
 <id>e777f423-b4de-434c-a6db-23e88e080a5e</id>
 <type>Folder</type>
</data> <success>true</success> <requestId>B29F2776-C7FF-4740-9284-1821297B0085</requestId>
```

#### 3.1.74 SetDeploymentResourceMode

Sets the resource configuration mode of a deployment.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/set-res ource HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |

|   |   |   |   | nk (Co Editio | mpute-Storage Separation n) Developer Guide·AppM nager AP |
|---|---|---|---|---|---|

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| deploymen tId | String | Path | Yes | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | The deployment ID. |
| paramsJso n | String | Body | No | { "deploymentResourceMod eBase": { "kind": "auto" } } | The resource configuration mode. Valid values of kind: auto, fine- grained, and coarse- grained. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
|   |   | { "metadata": { "createdAt": "2024- 03-12T06:12:17Z", "modifiedAt": "2024-03- 12T06:44:00.82332 3Z", "resourceVersion": 15, "name": "sqljob", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "resource- plan.has.migrated": "true", "deployment.has.de ployed": "false", "deployment.source -type": "EDITOR", "deployment.parent. |   |

| Parameter | Type | id": "", "modifier": Example "229852610122763 | Description |
|---|---|---|---|
|   |   | 813", "creatorName": "flinkadmin", "priority": "5", "priority.class.name ": "", |   |
|   |   | "autopilot.mode": "monitor", "com.dataartisans.a ppmanager.controll er.deployment.spec. version": "3", "deployment.refere nced.deployment.dr aft.history.version": "1", "x-namespace- owner-master-uid": "105291012272990 9", "default.resource- setting.has.migrate d": "true", "deployment.exec- plan.uri": "hdfs:///vvp/data/pla n/namespaces/flinkt eam/deployment/d0 b3abf0-4bfe-46b1- a324- 5b7def580c00/exec Plan.json", "deployment.refere nced.deployment.dr aft.id": "c6f157ac- 60b9-4b38-8bad- d435387cfd59", "comment": "", "modifierName": "flinkadmin", "taker": "default- cluster \| 0", "deployment.refere nced.deployment.dr aft.history.id": "1fbfefd4-9b1c- 4e94-b6ad- 268a5c6b64cd" }, "workspaceName": "default", "id": "d0b3abf0-4bfe- 46b1-a324- 5b7def580c00", "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type" : "auto", "job.resource.total. memory.byte": "8589934592", "job.resource.total.c pu": "4.0", "native.kubernetes. |   |

| Parameter | Type | mode": "true", Example "flink.queryable- | Description |
|---|---|---|---|
| data | String | state.enabled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.15.0-vvr-6.0.7- 29", "kind": "SQLSCRIPT", "sqlScript": "-- ******************** ******************** ******************** ********-- -- Author: Write your name here -- Created Time: 2024-03-12 14:11:38 -- Description: Write your description here -- ******************** ******************** ******************** ********-- CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( \u0027connector\u0 027 \u003d \u0027datagen\u00 27 ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( \u0027connector\u0 027 \u003d \u0027print\u0027 ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ ", "imageUserDefined" : false, "flinkImageRegistry" : "cn-qingdao- env17e-d01- reg.docker.intra.env 17e.shuguang.com: 80/ververica-paas", "versionName": "vvr-6.0.0-flink- 1.15", "flinkImageReposito | The detailed data. |

| Parameter | Type | ry": "vvr", Example "flinkVersion": | Description |
|---|---|---|---|
|   |   | "1.15" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 2.0 }, "taskmanager": { "memory": "4Gi", "cpu": 2.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration": { "execution.checkpoi nting.interval": "180s", "execution.checkpoi nting.min-pause": "180s" } } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestoredS tate": false }, "state": "RUNNING", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCreat ionAttempts": 4, "maxJobCreationAtt empts": 1, "deploymentTargetI d": "f2ed6708-a7e1- 4e86-a99e- 327fac9265c2" }, "status": { "startTime": 0, "state": "RUNNING", "endTime": 0 } } |   |
| requestId | String | BCC13432-238D- 41D7-B0A6- 582241A6B572 | The request ID. |

Sample requests

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/set-res ource HTTP/1.1
```

`{`

```json
"RegionId":"", "workspace":"", "namespace":"", "deploymentId":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "metadata": {
      "createdAt": "2024-03-12T06:12:17Z",
      "modifiedAt": "2024-03-12T06:44:00.823323Z",
      "resourceVersion": 15,
      "name": "sqljob",
      "namespace": "flinkteam",
      "annotations": {
        "creator": "229852610122763813",
        "resource-plan.has.migrated": "true",
        "deployment.has.deployed": "false",
        "deployment.source-type": "EDITOR",
        "deployment.parent.id": "",
        "modifier": "229852610122763813",
        "creatorName": "flinkadmin",
        "priority": "5",
        "priority.class.name": "",
        "autopilot.mode": "monitor",
        "com.dataartisans.appmanager.controller.deployment.spec.version": "3",
        "deployment.referenced.deployment.draft.history.version": "1",
        "x-namespace-owner-master-uid": "1052910122729909",
        "default.resource-setting.has.migrated": "true",
        "deployment.exec-plan.uri":
"hdfs:///vvp/data/plan/namespaces/flinkteam/deployment/d0b3abf0-4bfe-46b1-a324-5b7def580c00/ execPlan.json",
        "deployment.referenced.deployment.draft.id": "c6f157ac-60b9-4b38-8bad-d435387cfd59",
        "comment": "",
        "modifierName": "flinkadmin",
        "taker": "default-cluster | 0",
        "deployment.referenced.deployment.draft.history.id": "1fbfefd4-9b1c-4e94-b6ad-268a5c
6b64cd"
```

`},`

```json
      "workspaceName": "default",
      "id": "d0b3abf0-4bfe-46b1-a324-5b7def580c00",
      "labels": {}
```

`},`

```json
    "apiVersion": "v1",
    "kind": "Deployment",
    "spec": {
      "template": {
        "metadata": {
          "annotations": {
```

`a`

```
otatos:{
            "flink.resource.type": "auto",
            "job.resource.total.memory.byte": "8589934592",
            "job.resource.total.cpu": "4.0",
            "native.kubernetes.mode": "true",
            "flink.queryable-state.enabled": "false"
```

`}` `},`

```json
        "spec": {
          "artifact": {
            "flinkImageTag": "1.15.0-vvr-6.0.7-29",
            "kind": "SQLSCRIPT",
            "sqlScript": "--
********************************************************************---- Author:         Wri
te your name here-- Created Time: 2024-03-12 14:11:38-- Description: Write your descrip tion here--********************************************************************--CREATE TEMP ORARY TABLE `datahub_table` (strname VARCHAR)with ( \u0027connector\u0027 \u003d \u0027da tagen\u0027 );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( \u0027connector\u0027 \u003d \u0027print\u0027 );INSERT INTO kafka_tableSELECT SUBSTRING (s trname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table ;",
            "imageUserDefined": false,
            "flinkImageRegistry": "cn-qingdao-env17e-d01-
reg.docker.intra.env17e.shuguang.com:80/ververica-paas",
            "versionName": "vvr-6.0.0-flink-1.15",
            "flinkImageRepository": "vvr",
            "flinkVersion": "1.15"
```

`},`

```json
          "parallelism": 1,
          "batchMode": false,
          "resources": {
            "jobmanager": {
              "memory": "4Gi",
              "cpu": 2.0
```

`},`

```json
            "taskmanager": {
              "memory": "4Gi",
              "cpu": 2.0
```

`}` `},`

```json
          "logging": {
            "log4jLoggers": {
              "": "INFO"
```

`},`

```json
            "logReservePolicy": {
              "expirationDays": 7,
              "openHistory": true
```

`},`

```json
            "loggingProfile": "default"
```

`},`

```json
          "flinkConfiguration": {
            "execution.checkpointing.interval": "180s",
            "execution.checkpointing.min-pause": "180s"
```

`}` `}` `},`

```json
      "restoreStrategy": {
"kind":"LATESTSTATE",
```

```json
        kind: LATEST_STATE,
        "allowNonRestoredState": false
```

`},`

```json
      "state": "RUNNING",
      "upgradeStrategy": {
        "kind": "NONE"
```

`},`

```json
      "maxSavepointCreationAttempts": 4,
      "maxJobCreationAttempts": 1,
      "deploymentTargetId": "f2ed6708-a7e1-4e86-a99e-327fac9265c2"
```

`},`

```json
    "status": {
      "startTime": 0,
      "state": "RUNNING",
      "endTime": 0
```

`}` `},`

```json
  "success": true,
  "requestId": "BCC13432-238D-41D7-B0A6-582241A6B572"
```

`}` `XML` format

```xml
<data>
 <metadata>
  <createdAt>2024-03-12T06:12:17Z</createdAt>
  <modifiedAt>2024-03-12T06:44:00.823323Z</modifiedAt>
  <resourceVersion>15</resourceVersion>
  <name>sqljob</name>
  <namespace>flinkteam</namespace>
  <annotations>
   <creator>229852610122763813</creator>
   <resource-plan.has.migrated>true</resource-plan.has.migrated>
   <deployment.has.deployed>false</deployment.has.deployed>
   <deployment.source-type>EDITOR</deployment.source-type>
   <deployment.parent.id />
   <modifier>229852610122763813</modifier>
   <creatorName>flinkadmin</creatorName>
   <priority>5</priority>
   <priority.class.name />
   <autopilot.mode>monitor</autopilot.mode>
<com.dataartisans.appmanager.controller.deployment.spec.version>3</com.dataartisans.appmanager ontroller.deployment.spec.version> <deployment.referenced.deployment.draft.history.version>1</deployment.referenced.deployment.dr t.history.version>
   <x-namespace-owner-master-uid>1052910122729909</x-namespace-owner-master-uid>
   <default.resource-setting.has.migrated>true</default.resource-setting.has.migrated>
   <deployment.exec-plan.uri>hdfs:///vvp/data/plan/namespaces/flinkteam/deployment/d0b3abf0-
4bfe-46b1-a324-5b7def580c00/execPlan.json</deployment.exec-plan.uri>
   <deployment.referenced.deployment.draft.id>c6f157ac-60b9-4b38-8bad-
d435387cfd59</deployment.referenced.deployment.draft.id>
   <comment  />
   <modifierName>flinkadmin</modifierName>
   <taker>default-cluster | 0</taker>
   <deployment.referenced.deployment.draft.history.id>1fbfefd4-9b1c-4e94-b6ad-268a5c6b64cd</
```

```xml
deployment.referenced.deployment.draft.history.id>
  </annotations>
  <workspaceName>default</workspaceName>
  <id>d0b3abf0-4bfe-46b1-a324-5b7def580c00</id>
  <labels  />
 </metadata>
 <apiVersion>v1</apiVersion>
 <kind>Deployment</kind>
 <spec>
  <template>
   <metadata>
    <annotations>
     <flink.resource.type>auto</flink.resource.type>
     <job.resource.total.memory.byte>8589934592</job.resource.total.memory.byte>
     <job.resource.total.cpu>4.0</job.resource.total.cpu>
     <native.kubernetes.mode>true</native.kubernetes.mode>
     <flink.queryable-state.enabled>false</flink.queryable-state.enabled>
    </annotations>
   </metadata>
   <spec>
    <artifact>
     <flinkImageTag>1.15.0-vvr-6.0.7-29</flinkImageTag>
     <kind>SQLSCRIPT</kind>
     <sqlScript>--********************************************************************--
-- Author: Write your name here -- Created Time: 2024-03-12 14:11:38 -- Description: Write your description here --********************************************************************-- CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR) with (
    &#x27;connector&#x27; = &#x27;datagen&#x27;
```

);

```
CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT) with (
    &#x27;connector&#x27; = &#x27;print&#x27;
```

);

```xml
INSERT INTO kafka_table SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens FROM
  datahub_table;
     </sqlScript>
     <imageUserDefined>false</imageUserDefined>
     <flinkImageRegistry>cn-qingdao-env17e-d01-
reg.docker.intra.env17e.shuguang.com:80/ververica-paas</flinkImageRegistry>
     <versionName>vvr-6.0.0-flink-1.15</versionName>
     <flinkImageRepository>vvr</flinkImageRepository>
     <flinkVersion>1.15</flinkVersion>
    </artifact>
    <parallelism>1</parallelism>
    <batchMode>false</batchMode>
    <resources>
     <jobmanager>
      <memory>4Gi</memory>
      <cpu>2</cpu>
     </jobmanager>
```

```xml
     <taskmanager>
      <memory>4Gi</memory>
      <cpu>2</cpu>
     </taskmanager>
    </resources>
    <logging>
     <log4jLoggers>
      <>INFO</>
     </log4jLoggers>
     <logReservePolicy>
      <expirationDays>7</expirationDays>
      <openHistory>true</openHistory>
     </logReservePolicy>
     <loggingProfile>default</loggingProfile>
    </logging>
    <flinkConfiguration>
     <execution.checkpointing.interval>180s</execution.checkpointing.interval>
     <execution.checkpointing.min-pause>180s</execution.checkpointing.min-pause>
    </flinkConfiguration>
   </spec>
  </template>
  <restoreStrategy>
   <kind>LATEST_STATE</kind>
   <allowNonRestoredState>false</allowNonRestoredState>
  </restoreStrategy>
  <state>RUNNING</state>
  <upgradeStrategy>
   <kind>NONE</kind>
  </upgradeStrategy>
  <maxSavepointCreationAttempts>4</maxSavepointCreationAttempts>
  <maxJobCreationAttempts>1</maxJobCreationAttempts>
  <deploymentTargetId>f2ed6708-a7e1-4e86-a99e-327fac9265c2</deploymentTargetId>
 </spec>
 <status>
  <startTime>0</startTime>
  <state>RUNNING</state>
  <endTime>0</endTime>
 </status>
</data> <success>true</success> <requestId>BCC13432-238D-41D7-B0A6-582241A6B572</requestId>
```

#### 3.1.75 TableExists

Checks whether a table exists.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:tableExists HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | String | Path | Yes | ververica | The name of the namespace to which the deployment belongs. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| cat | String | Path | Yes | vvp | The name of the catalog. |
| database | String | Query | Yes | default | The name of the database. |
| table | String | Query | Yes | mydatahub | The name of the table. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.TableExistsR esponse", "exists": true } | The detailed information. |
| requestId | String | 39253EC3-B674- 4B11-AD97- C221D6DB1003 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:tableExists HTTP/1.1 &RegionId= &namespace= &workspace= &cat= &database= &table= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "requestId": "39253EC3-B674-4B11-AD97-C221D6DB1003",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.TableExistsResponse",
    "exists": true
```

`}` `}` `XML` format

```xml
<requestId>39253EC3-B674-4B11-AD97-C221D6DB1003</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.TableExistsResponse</@type>
 <exists>true</exists>
</data>
```

#### 3.1.76 UpdateConnector

Modifies the information about a custom connector.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HTTP/1.
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| name | String | Path | Yes | hologres-fix | The name of the connector whose information you want to modify. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| paramsJso n | String | Body | No | { "type": "hologres-fix", "name": "namespaces/flinkteam/c onnectors/hologres-fix", "packaged": false, "source": true, "sink": true, "lookup": false, "dependencies": [ "hdfs:///vvp/data/sql- artifacts/namespaces/flink team/custom- connectors/2024-03- 11T05-51- 25.289740Z/ververica- connector-hologres-1.15- vvr-6.0-fix.jar" ], "supportedFormats": [ "json","csv" ], "properties": [ { "key": "connector", "required": true, "defaultValue": "hologres-fix", "description": "", "definesFormat": false }, { "key": "dbname", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "endpoint", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "tablename", "required": true, "defaultValue": "", "description": "", "definesFormat": false } ] } | The modified parameters. These parameters are used to declare the properties of the connector, such as connector type, connector name, required connection parameters, whether the connector can be used as the data source or data sink, and the dependent JAR packages. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "affectedTables": [], "connector": { "lookup": true, "supportedFormats" : [ "json", "csv" ], "environments": [], "sink": true, "name": "namespaces/flinkte am/connectors/holo gres-fix", "source": true, "type": "hologres-fix", "properties": [ { "defaultValue": "hologres-fix", "description": "", "definesFormat": false, "key": "connector", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "dbname", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "endpoint", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "tablename", "required": true } ], "packaged": false, "dependencies": [ "hdfs:///vvp/data/sql - artifacts/namespace s/flinkteam/custom- connectors/2024- 03-11T05-51- 25.289740Z/ververi ca-connector- hologres-1.15-vvr- 6.0-fix.jar" ] }, "@type": "type.googleapis.co m/vvp.sql.v1beta1.U pdateConnectorRes ponse" } | The detailed data. |
| requestId | String | 4FA46133-1C97- 4B48-96E3- 3B7DFFFEC707 | The request ID. |

Sample requests

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HTTP/1.
```

`{`

```json
"RegionId":"", "workspace":"", "name":"", "namespace":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "affectedTables": [],
    "connector": {
      "lookup": true,
      "supportedFormats": [
        "json",
        "csv"
```

`],`

```json
      "environments": [],
      "sink": true,
      "name": "namespaces/flinkteam/connectors/hologres-fix",
      "source": true,
      "type": "hologres-fix",
      "properties": [
```

`{`

```json
          "defaultValue": "hologres-fix",
          "description": "",
          "definesFormat": false,
          "key": "connector",
          "required": true
```

`},` `{`

```json
          "defaultValue": "",
          "description": "",
          "definesFormat": false,
          "key": "dbname",
          "required": true
```

`},` `{`

```json
          "defaultValue": "",
          "description": "",
          "definesFormat": false,
          "key": "endpoint",
          "required": true
```

`},` `{`

```json
          "defaultValue": "",
          "description": "",
          "definesFormat": false,
          "key": "tablename",
          "required": true
```

`}` `],`

```json
      "packaged": false,
      "dependencies": [
        "hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/custom-connectors/2024-03-11T05
-51-25.289740Z/ververica-connector-hologres-1.15-vvr-6.0-fix.jar"
```

`]` `},`

```
    "@type": "type.googleapis.com/vvp.sql.v1beta1.UpdateConnectorResponse"
```

`},`

```json
  "success": true,
  "requestId": "4FA46133-1C97-4B48-96E3-3B7DFFFEC707"
```

`}` `XML` format

```xml
<data>
 <affectedTables  />
 <connector>
  <lookup>true</lookup>
  <supportedFormats>json</supportedFormats>
  <supportedFormats>csv</supportedFormats>
  <environments  />
  <sink>true</sink>
  <name>namespaces/flinkteam/connectors/hologres-fix</name>
  <source>true</source>
  <type>hologres-fix</type>
  <properties>
   <defaultValue>hologres-fix</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>connector</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>dbname</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>endpoint</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>tablename</key>
   <required>true</required>
  </properties>
  <packaged>false</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/custom-connectors/2024-0
3-11T05-51-25.289740Z/ververica-connector-hologres-1.15-vvr-6.0-fix.jar</dependencies>
 </connector>
 <@type>type.googleapis.com/vvp.sql.v1beta1.UpdateConnectorResponse</@type>
</data> <success>true</success> <requestId>4FA46133-1C97-4B48-96E3-3B7DFFFEC707</requestId>
```

#### 3.1.77 UpdateFormat

Modifies the information about a format, such as whether the format can be used as the data source or data sink, format parameter, and dependent JAR packages.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| name | String | Path | Yes | customized-csv | The name of the format whose information you want to modify. |
| paramsJso n | String | Body | No | { "name": "namespaces/flinkteam/fo rmats/customized-csv", "type": "customized-csv", "source": true, "sink": false, "properties": [ { "key": "format.column- delimiter", "required": false, "defaultValue": ",", "description": "" } ], "dependencies": [ "hdfs:///tmp/myformats/cu stomized-csv-demo-1.0- SNAPSHOT.jar" ] } | The modified parameters. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| data | String | { "affectedTables": [], "@type": "type.googleapis.co m/vvp.sql.v1beta1.U pdateFormatRespon se", "format": { "sink": false, "name": "namespaces/flinkte am/formats/customi zed-csv", "source": true, "type": "customized-csv", "properties": [ { "defaultValue": ",", "description": "", "definesFormat": false, "key": "format.column- delimiter", "required": false } ], "packaged": false, "dependencies": [ "hdfs:///tmp/myform ats/customized-csv- demo-1.0- SNAPSHOT.jar" ] } } | The details of the format after modification. |
| requestId | String | 208EF7F3-647B- 4701-BCAD- 6A14FC4696FC | The request ID. |

Sample requests

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HTTP/1.1
```

`{`

```json
"RegionId":"", "workspace":"", "name":"", "namespace":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "affectedTables": [],
    "@type": "type.googleapis.com/vvp.sql.v1beta1.UpdateFormatResponse",
    "format": {
      "sink": false,
      "name": "namespaces/flinkteam/formats/customized-csv",
      "source": true,
      "type": "customized-csv",
      "properties": [
```

`{`

```json
          "defaultValue": ",",
          "description": "",
          "definesFormat": false,
          "key": "format.column-delimiter",
          "required": false
```

`}` `],`

```json
      "packaged": false,
      "dependencies": [
        "hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar"
```

`]` `}` `},`

```json
  "success": true,
  "requestId": "208EF7F3-647B-4701-BCAD-6A14FC4696FC"
```

`}` `XML` format

```xml
<data>
 <affectedTables  />
 <@type>type.googleapis.com/vvp.sql.v1beta1.UpdateFormatResponse</@type>
 <format>
  <sink>false</sink>
  <name>namespaces/flinkteam/formats/customized-csv</name>
  <source>true</source>
  <type>customized-csv</type>
  <properties>
   <defaultValue>,</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>format.column-delimiter</key>
   <required>false</required>
  </properties>
  <packaged>false</packaged>
  <dependencies>hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar</dependencies>
 </format>
</data> <success>true</success> <requestId>208EF7F3-647B-4701-BCAD-6A14FC4696FC</requestId>
```

#### 3.1.78 UpdateMember

Modifies the permissions of a user.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
PUT /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| paramsJso n | String | Body | No | { "role": "owner", "member": "242425410145292209" } | The modified parameters. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| RegionId | String | Host | Yes | cn-wulan-env188-d01 | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | 29F07013-6BE2- 4F99-90B6- 9E27BF2A26C4 | The request ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.members.v1. UpdateMemberResp onse", "member": { "role": "owner", "member": "user:24242541014 5292209" } } | The permissions of the user after modification. |

Sample requests

```
PUT /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1
```

`{`

```json
"workspace":"", "namespace":"", "RegionId":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "@type": "type.googleapis.com/vvp.members.v1.UpdateMemberResponse",
    "member": {
      "role": "owner",
      "member": "user:242425410145292209"
```

`}` `},`

```json
  "success": true,
  "requestId": "29F07013-6BE2-4F99-90B6-9E27BF2A26C4"
```

`}` `XML` format

```xml
<data>
 <@type>type.googleapis.com/vvp.members.v1.UpdateMemberResponse</@type>
 <member>
  <role>owner</role>
  <member>user:242425410145292209</member>
 </member>
</data> <success>true</success> <requestId>29F07013-6BE2-4F99-90B6-9E27BF2A26C4</requestId>
```

#### 3.1.79 UpdateUdfArtifact

Modifies a user-defined function (UDF) JAR file.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| paramsJso n | String | Body | No | { "jarUrl": "hdfs:///vvp/data/sql- artifacts/namespaces/flink team/udfs/metric- transform-227- shaded/2024-03-08T08- 13-54.732313Z/metric- transform-2.2.7- shaded.jar" } | The modified parameters. |
| workspace | String | Path | Yes | default | The ID of the workspace to which the deployment belongs. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the development console of Realtime Compute for Apache Flink. |
| namespac e | String | Path | Yes | flinkteam | The name of the namespace to which the deployment belongs. |
| udfArtifact Name | String | Path | Yes | metric-transform-227- shaded | The name of the UDF. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "missingClasses": [], "@type": "type.googleapis.co m/vvp.sql.v1beta1.U pdateUdfArtifactRes ponse", "collidingClasses": [], "udfArtifact": { "dependencyJarUris" : [], "udfClasses": [ { "functionNames": [], "udfArtifactName": "namespaces/flinkte am/udfartifacts/metr ic-transform-227- shaded", "className": "com.alibaba.blink.u dtf.TimestampProbe ", "classType": "UDF TYPE SCALAR _ _ " }, { "functionNames": [], "udfArtifactName": "namespaces/flinkte am/udfartifacts/metr ic-transform-227- shaded", "className": "com.alibaba.blink.u dtf.TransformUdtf", "classType": "UDF TYPE TABLE" _ _ } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "createTime": "2024-03- 08T08:13:54Z", "uploader": "223474909869445 380", "jarUpdateTime": "2024-03- 08T09:04:22.53111 3Z", "name": "namespaces/flinkte am/udfartifacts/metr ic-transform-227- shaded", "namespace": "namespaces/flinkte am", "jarUrl": "hdfs:///vvp/data/sql - artifacts/namespace s/flinkteam/udfs/met ric-transform-227- shaded/2024-03- 08T08-13- 54.732313Z/metric- transform-2.2.7- shaded.jar", "updateTime": "2024-03- 08T09:04:22.53111 3Z" } } | The detailed information. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | A2E6AB81-9FA6- 48EE-BF0D- 3829017F3C14 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

Sample requests

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1
```

`{`

```json
"RegionId":"", "workspace":"", "namespace":"", "udfArtifactName":""
```

`}` Sample success responses `JSON` format `{`

```json
  "data": {
    "missingClasses": [],
    "@type": "type.googleapis.com/vvp.sql.v1beta1.UpdateUdfArtifactResponse",
    "collidingClasses": [],
    "udfArtifact": {
      "dependencyJarUris": [],
      "udfClasses": [
```

`{`

```json
          "functionNames": [],
          "udfArtifactName": "namespaces/flinkteam/udfartifacts/metric-transform-227-shaded"
```

`,`

```json
          "className": "com.alibaba.blink.udtf.TimestampProbe",
          "classType": "UDF_TYPE_SCALAR"
```

`},` `{`

```json
          "functionNames": [],
          "udfArtifactName": "namespaces/flinkteam/udfartifacts/metric-transform-227-shaded"
```

`,`

```json
          "className": "com.alibaba.blink.udtf.TransformUdtf",
          "classType": "UDF_TYPE_TABLE"
```

`}` `],`

```json
      "artifactType": "ARTIFACT_TYPE_JAVA",
      "createTime": "2024-03-08T08:13:54Z",
      "uploader": "223474909869445380",
      "jarUpdateTime": "2024-03-08T09:04:22.531113Z",
      "name": "namespaces/flinkteam/udfartifacts/metric-transform-227-shaded",
      "namespace": "namespaces/flinkteam",
      "jarUrl": "hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/udfs/metric-transform-2
27-shaded/2024-03-08T08-13-54.732313Z/metric-transform-2.2.7-shaded.jar",
      "updateTime": "2024-03-08T09:04:22.531113Z"
```

`}` `},`

```json
  "requestId": "A2E6AB81-9FA6-48EE-BF0D-3829017F3C14",
  "success": true
```

`}` `XML` format

```xml
<data>
 <missingClasses  />
 <@type>type.googleapis.com/vvp.sql.v1beta1.UpdateUdfArtifactResponse</@type>
 <collidingClasses  />
 <udfArtifact>
  <dependencyJarUris  />
  <udfClasses>
   <functionNames  />
   <udfArtifactName>namespaces/flinkteam/udfartifacts/metric-transform-227-shaded</udfArtifa
ctName>
   <className>com.alibaba.blink.udtf.TimestampProbe</className>
   <classType>UDF_TYPE_SCALAR</classType>
  </udfClasses>
  <udfClasses>
   <functionNames  />
   <udfArtifactName>namespaces/flinkteam/udfartifacts/metric-transform-227-shaded</udfArtifa
ctName>
   <className>com.alibaba.blink.udtf.TransformUdtf</className>
   <classType>UDF_TYPE_TABLE</classType>
  </udfClasses>
  <artifactType>ARTIFACT_TYPE_JAVA</artifactType>
  <createTime>2024-03-08T08:13:54Z</createTime>
  <uploader>223474909869445380</uploader>
  <jarUpdateTime>2024-03-08T09:04:22.531113Z</jarUpdateTime>
  <name>namespaces/flinkteam/udfartifacts/metric-transform-227-shaded</name>
  <namespace>namespaces/flinkteam</namespace>
  <jarUrl>hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/udfs/metric-transform-227-
shaded/2024-03-08T08-13-54.732313Z/metric-transform-2.2.7-shaded.jar</jarUrl>
  <updateTime>2024-03-08T09:04:22.531113Z</updateTime>
 </udfArtifact>
</data> <requestId>A2E6AB81-9FA6-48EE-BF0D-3829017F3C14</requestId> <success>true</success>
```

#### 3.1.80 CreateNamespace

Creates a namespace.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
POST /flink/namespace/create HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env188-d01 | The region ID. |

| n E n | k (Compute- dition) Devel ager API | Storage S oper Guid | eparation e·AppMa |   |   |   |   |
|---|---|---|---|---|---|---|---|

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| name | String | Path | Yes | blinkteam | The name of the namespace. |
| cpuBrand | String | Path | Yes | Intel | The CPU type of the namespace. Deployments in the namespace are scheduled to machines of the specified CPU type. |
| region | String | Path | No | cn-wulan-env188-d01 | The region ID. |
| allocateCu | String | Path | Yes | 10 | The number of reserved compute units (CUs) of the namespace. |
| ownerUid | String | Path | Yes | 229852610122763813 | The UID of the resource owner. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | E39BDDB3-7017- 410E-9A79- EF50218BEDBA | The request ID. |
| data | String | blinkteam | The name of the created namespace. |

Sample requests

```
POST /flink/namespace/create HTTP/1.1
```

`{`

```json
"RegionId":"", "name":"", "allocateCu":"", "ownerUid":""
```

`}` Sample success responses `JSON` format `{`

```json
  "eagleEyeTraceId": "0a11353617103145127224622d00c1",
  "asapiSuccess": true,
  "asapiRequestId": "E39BDDB3-7017-410E-9A79-EF50218BEDBA",
  "data": "blinkteam",
  "success": true,
  "requestId": "E39BDDB3-7017-410E-9A79-EF50218BEDBA"
```

`}` `XML` format

```xml
<eagleEyeTraceId>0a11353617103145127224622d00c1</eagleEyeTraceId> <asapiSuccess>true</asapiSuccess> <asapiRequestId>E39BDDB3-7017-410E-9A79-EF50218BEDBA</asapiRequestId> <data>blinkteam</data> <success>true</success> <requestId>E39BDDB3-7017-410E-9A79-EF50218BEDBA</requestId>
```

#### 3.1.81 DescribeNamespaces

Queries a list of namespaces.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /flink/namespace/list HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env188-d01 | The region ID. |
| region | String | Path | No | cn-wulan-env188-d01 | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array | { "data": [ { "Uid": "229852610122763 813", "MemUsed": "40802189312", "CpuBrand": "Intel", "CreateTime": 1710122900722, "Region": "cn- qingdao-env***- d01", "GuaranteeQuota": "15", "RoleBindings": " [{\"members\": [\"user:2298526101 22763813\"],\"role\" :\"owner\"}, {\"members\": [\"user:1052910122 729909\"],\"role\":\" owner\"}]", "VvpPortal": "realtime-compute- cn-qingdao-env17e- d01.console.con.env 17e.shuguang.com", "CpuUsed": "12.0", "Queue": "k8s- flinkteam", "Members": " [{\"member\":\"user :105291012272990 9\",\"role\":\"owner\" }, {\"member\":\"user: 2298526101227638 13\",\"role\":\"owner \"}]", "Name": "flinkteam" } ], "success": true, "requestId": "A26F6DD1-A0BE- 4842-BF85- E24E60E9019D" } | The returned data. |
| -Region | String | cn-qingdao-env17e- d01 | The region ID. |
| -Cluster | String | default | The cluster name. |
| -Queue | String | k8s-blinkteam | The queue name. |
| -Name | String | blinkteam | The name of the namespace. |
| -CpuBrand | String | Intel | The CPU type of the namespace. Deployments in the namespace are scheduled to machines of the specified CPU type. For hybrid deployment, the chips must be of the same architecture. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -CreateTime | Long | 1710314513015 | The time when the namespace was created. |
| - GuaranteeQuot a | String | 10 | The resource quota. |
| -Uid | String | 2298526101227638 13 | The UID of the resource owner. |
| -RoleBindings | String | [{\"members\": [\"user:2298526101 22763813\"],\"role\" :\"owner\"}, {\"members\": [\"user:1052910122 729909\"],\"role\":\" owner\"}] | The user-role mappings. |
| -Members | String | [{\"member\":\"user :105291012272990 9\",\"role\":\"owner\" }, {\"member\":\"user: 2298526101227638 13\",\"role\":\"owner \"}] | The authorization information. |
| -CpuUsed | String | 0 | The CPU usage. |
| -MemUsed | String | 0 | The used memory. |
| -VvpPortal | String | realtime-compute- xxxxxconsole.con.xx xxx.com | The URL of the Realtime Compute for Apache Flink console. |
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | A26F6DD1-A0BE- 4842-BF85- E24E60E9019D | The request ID. |

Sample requests

```
GET /flink/namespace/list HTTP/1.1 &RegionId= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "data": [
```

`{`

```json
      "MemUsed": "0.0",
      "CpuBrand": "Intel",
      "CreateTime": 1710314513015,
      "Region": "cn-qingdao-env***-d01",
      "GuaranteeQuota": "15",
      "RoleBindings": "[{\"members\":[\"user:229852610122763813\"],\"role\":\"owner\"},{\"me
mbers\":[\"user:1052910122729909\"],\"role\":\"owner\"}]",
      "VvpPortal": "realtime-compute-cn-qingdao-env***-d01.console.con.env***.shuguang.com",
      "CpuUsed": "0.0",
      "Queue": "k8s-blinkteam",
      "Members": "[{\"member\":\"user:1052910122729909\",\"role\":\"owner\"},
{\"member\":\"user:229852610122763813\",\"role\":\"owner\"}]",
      "Name": "blinkteam"
```

`},` `{`

```json
      "Uid": "229852610122763813",
      "MemUsed": "40802189312",
      "CpuBrand": "Intel",
      "CreateTime": 1710122900722,
      "Region": "cn-qingdao-env17e-d01",
      "GuaranteeQuota": "15",
      "RoleBindings": "[{\"members\":[\"user:229852610122763813\"],\"role\":\"owner\"},{\"me
mbers\":[\"user:1052910122729909\"],\"role\":\"owner\"}]",
      "VvpPortal": "realtime-compute-cn-qingdao-env***-d01.console.con.env***.shuguang.com",
      "CpuUsed": "12.0",
      "Queue": "k8s-flinkteam",
      "Members": "[{\"member\":\"user:1052910122729909\",\"role\":\"owner\"},
{\"member\":\"user:229852610122763813\",\"role\":\"owner\"}]",
      "Name": "flinkteam"
```

`}` `],`

```json
  "success": true,
  "requestId": "A26F6DD1-A0BE-4842-BF85-E24E60E9019D"
```

`}` `XML` format

```xml
<data>
 <MemUsed>0.0</MemUsed>
 <CpuBrand>Intel</CpuBrand>
 <CreateTime>1710314513015</CreateTime>
 <Region>cn-qingdao-env***-d01</Region>
 <GuaranteeQuota>15</GuaranteeQuota>
 <RoleBindings>[{&quot;members&quot;:
[&quot;user:229852610122763813&quot;],&quot;role&quot;:&quot;owner&quot;},{&quot;members&quo t;:[&quot;user:1052910122729909&quot;],&quot;role&quot;:&quot;owner&quot;}]</RoleBindings>
 <VvpPortal>realtime-compute-cn-qingdao-env***-
d01.console.con.env***.shuguang.com</VvpPortal>
 <CpuUsed>0.0</CpuUsed>
 <Queue>k8s-blinkteam</Queue>
 <Members>
[{&quot;member&quot;:&quot;user:1052910122729909&quot;,&quot;role&quot;:&quot;owner&quot;},{ &quot;member&quot;:&quot;user:229852610122763813&quot;,&quot;role&quot;:&quot;owner&quot;}]< /Members>
 <Name>blinkteam</Name>
</data> <data>
 <Uid>229852610122763813</Uid>
 <MemUsed>40802189312</MemUsed>
 <CpuBrand>Intel</CpuBrand>
 <CreateTime>1710122900722</CreateTime>
 <Region>cn-qingdao-env***-d01</Region>
 <GuaranteeQuota>15</GuaranteeQuota>
 <RoleBindings>[{&quot;members&quot;:
[&quot;user:229852610122763813&quot;],&quot;role&quot;:&quot;owner&quot;},{&quot;members&quo t;:[&quot;user:1052910122729909&quot;],&quot;role&quot;:&quot;owner&quot;}]</RoleBindings>
 <VvpPortal>realtime-compute-cn-qingdao-env***-
d01.console.con.env***.shuguang.com</VvpPortal>
 <CpuUsed>12.0</CpuUsed>
 <Queue>k8s-flinkteam</Queue>
 <Members>
[{&quot;member&quot;:&quot;user:1052910122729909&quot;,&quot;role&quot;:&quot;owner&quot;},{ &quot;member&quot;:&quot;user:229852610122763813&quot;,&quot;role&quot;:&quot;owner&quot;}]< /Members>
 <Name>flinkteam</Name>
</data> <success>true</success> <requestId>A26F6DD1-A0BE-4842-BF85-E24E60E9019D</requestId>
```

#### 3.1.82 GetCluster

Queries the information about a cluster.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
GET /flink/cluster/get HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env188-d01 | The region ID. |
| region | String | Path | No | cn-wulan-env188-d01 | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | A2A95BB4-44FE- 407D-8486- 80B3BD5B4779 | The request ID. |
| data | String | { "data": { "clusterResources": [ { "cpuBrand": "Intel", "cpuTotal": 189.0, "memTotal": 751.77, "memRequest": 177.0, "allocatedCu": "133.0", "cpuRequest": 55.22 } ], "enableNetworkPolic y": true }, "success": true, "requestId": "A2A95BB4-44FE- 407D-8486- 80B3BD5B4779" } | The resource information about the cluster. |

Sample requests

```
GET /flink/cluster/get HTTP/1.1 &RegionId= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "data": {
    "clusterResources": [
```

`{`

```json
        "cpuBrand": "Intel",
        "cpuTotal": 189.0,
        "memTotal": 751.77,
        "memRequest": 177.0,
        "allocatedCu": "133.0",
        "cpuRequest": 55.22
```

`}` `],`

```json
    "enableNetworkPolicy": true
```

`},`

```json
  "success": true,
  "requestId": "A2A95BB4-44FE-407D-8486-80B3BD5B4779"
```

`}` `XML` format

```xml
<data>
 <clusterResources>
  <cpuBrand>Intel</cpuBrand>
  <cpuTotal>189</cpuTotal>
  <memTotal>751.77</memTotal>
  <memRequest>177</memRequest>
  <allocatedCu>133.0</allocatedCu>
  <cpuRequest>55.22</cpuRequest>
 </clusterResources>
 <enableNetworkPolicy>true</enableNetworkPolicy>
</data> <success>true</success> <requestId>A2A95BB4-44FE-407D-8486-80B3BD5B4779</requestId>
```

#### 3.1.83 UpdateNamespace

Modifies the resources of a namespace.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
PUT /flink/namespace/update HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env230-d01 | The region ID. |

| dition) Devel ager API | oper Guid | e·AppMa |   |   |   |
|---|---|---|---|---|---|

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| name | String | Path | Yes | blinkteam | The name of the namespace. |
| region | String | Path | No | cn-wulan-env230-d01 | The region ID. |
| allocateCu | String | Path | Yes | 15 | The number of reserved compute units (CUs). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | 53F11F14-0514- 4B46-9C59- 270F3C94DCD3 | The request ID. |
| data | String | blinkteam | The name of the namespace. |

Sample requests

```
PUT /flink/namespace/update HTTP/1.1
```

`{`

```json
"RegionId":"", "name":"", "allocateCu":""
```

`}` Sample success responses `JSON` format `{`

```json
  "eagleEyeTraceId": "0a112ca217103152416904683d00c8",
  "asapiSuccess": true,
  "asapiRequestId": "53F11F14-0514-4B46-9C59-270F3C94DCD3",
  "data": "blinkteam",
  "success": true,
  "requestId": "53F11F14-0514-4B46-9C59-270F3C94DCD3"
```

`}` `XML` format

```xml
<eagleEyeTraceId>0a112ca217103152416904683d00c8</eagleEyeTraceId> <asapiSuccess>true</asapiSuccess> <asapiRequestId>53F11F14-0514-4B46-9C59-270F3C94DCD3</asapiRequestId> <data>blinkteam</data> <success>true</success> <requestId>53F11F14-0514-4B46-9C59-270F3C94DCD3</requestId>
```

#### 3.1.84 DeleteNamespace

Deletes a namespace.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request syntax**

```
DELETE /flink/namespace/delete HTTP/1.1
```

**Request parameters**

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| name | String | Path | Yes | blinkteam | The name of the namespace that you want to delete. |
| region | String | Path | No | cn-wulan-env230-d01 | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CCF11162-0068- 4302-B226- 403D46673F0F | The request ID. |
| data | String | blinkteam | The name of the deleted namespace. |

Sample requests

```
DELETE /flink/namespace/delete HTTP/1.1 &RegionId= &name= &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "eagleEyeTraceId": "0a11353617103175009232076d00c1",
  "asapiSuccess": true,
  "asapiRequestId": "CCF11162-0068-4302-B226-403D46673F0F",
  "data": "blinkteam",
  "success": true,
  "requestId": "CCF11162-0068-4302-B226-403D46673F0F"
```

`}` `XML` format

```xml
<eagleEyeTraceId>0a11353617103175009232076d00c1</eagleEyeTraceId> <asapiSuccess>true</asapiSuccess> <asapiRequestId>CCF11162-0068-4302-B226-403D46673F0F</asapiRequestId> <data>blinkteam</data> <success>true</success> <requestId>CCF11162-0068-4302-B226-403D46673F0F</requestId>
```

### 3.2 API examples

#### 3.2.1 Examples

This topic describes API examples.

**Notes**

You must parse all interfaces that returns Resp by using a fixed method. All PUT and POST requests must include the content-type header and use the built-in JsonUtil for serialization.

**Sample code**

```java
package sample; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.http.FormatType; import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.profile.IClientProfile; import com.aliyuncs.ververica.model.v20200501.*; import com.fasterxml.jackson.core.JsonProcessingException; import com.fasterxml.jackson.core.type.TypeReference; import com.ververica.common.model.ResultModel; import com.ververica.common.model.deployment.Artifact; import com.ververica.common.model.deployment.Deployment; import com.ververica.common.model.deployment.DeploymentState; import com.ververica.common.model.namespace.Namespace;
```

```java
import com.ververica.common.params.*; import com.ververica.common.resp.*; import com.ververica.common.util.JsonUtil; import com.ververica.common.util.SdkUtil; import java.util.List; public class SdkSample {
    /**
     * Normal format:
     * {
     * "requestId":"202008030937-4TFJR5MK2R",
     * "success": true, # When this value is true, the result shows only requestId. When fal
se, it throws reason and message.
     * "message": "",
     * "reason": "",
     * "data": Data content (Object)
     * }
```

`*/`

```
    public static void main(String[] args) throws JsonProcessingException, ClientException {
        String regionId = "cn-hangzhou";
        DefaultProfile.addEndpoint(regionId, "ververica", "ververica-share.aliyuncs.com");
        IClientProfile profile = DefaultProfile.getProfile(regionId, "**************", "****
************");
        DefaultAcsClient client = new DefaultAcsClient(profile);
        /**
         Currently supports the following 4 regions:
         ververica-share.cn-hangzhou.aliyuncs.com
         ververica-share.cn-shanghai.aliyuncs.com
         ververica-share.cn-shenzhen.aliyuncs.com
         ververica-share.cn-beijing.aliyuncs.com
```

`*/`

```
        String deploymentId = "placeholder";
        // namespace/deploymentId depends on actual environment job configuration.
        // Get list of namespaces.
        ListNamespacesRequest listNamespacesRequest = new ListNamespacesRequest();
        listNamespacesRequest.setSysVersion("2024-11-18");
        ResultModel<ListNamespacesResp> listNamespacesRespResultModel =
JsonUtil.toBean(SdkUtil.getHttpContentString(client,
                listNamespacesRequest), new TypeReference<ResultModel<ListNamespacesResp>>()
```

`{`

```java
        });
        List<Namespace> namespaceList =
listNamespacesRespResultModel.getData().getNamespaces();
        System.out.println(JsonUtil.toJson(namespaceList));
        String workspaceName = namespaceList.get(0).getWorkspace();
        String namespace = namespaceList.get(0).getName();
        // Get deployment.
        GetDeploymentRequest getDeploymentRequest = new GetDeploymentRequest();
        getDeploymentRequest.setWorkspace(workspaceName);
        getDeploymentRequest.setNamespace(namespace);
        getDeploymentRequest.setDeploymentId(deploymentId);
        getDeploymentRequest.setSysVersion("2024-11-18");
        String data = client.doAction(getDeploymentRequest).getHttpContentString();
        System.out.println(data);
        ResultModel<GetDeploymentResp> getDeploymentRespResultModel = JsonUtil.toBean(data,
new TypeReference<ResultModel<GetDeploymentResp>>() {
```

```java
        });
        Deployment deployment = getDeploymentRespResultModel.getData();
        deployment.getMetadata().getAnnotations().put("update-flag", "zdbox");
        deployment.getMetadata().getLabels().put("key2", "value2");
        deployment.getSpec().setState(DeploymentState.RUNNING);
        // Update deployment state.
        UpdateDeploymentDesiredStateParams updateDeploymentDesiredStateParams = new UpdateDe
ploymentDesiredStateParams();
        updateDeploymentDesiredStateParams.setState(DeploymentState.CANCELLED);
        UpdateDeploymentDesiredStateRequest
                updateDeploymentDesiredStateRequest = new
UpdateDeploymentDesiredStateRequest();
        updateDeploymentDesiredStateRequest.setWorkspace(workspaceName);
        updateDeploymentDesiredStateRequest.setNamespace(namespace);
        updateDeploymentDesiredStateRequest.setDeploymentId(deploymentId);
updateDeploymentDesiredStateRequest.setParamsJson(JsonUtil.toJson(updateDeploymentDesiredState rams));
        updateDeploymentDesiredStateRequest.setHttpContentType(FormatType.JSON);
        updateDeploymentDesiredStateRequest.setSysVersion("2024-11-18");
System.out.println(client.doAction(updateDeploymentDesiredStateRequest).getHttpContentString()
        ResultModel<UpdateDeploymentDesiredStateResp>
                updateDeploymentDesiredStateRespResultModel =
JsonUtil.toBean(client.doAction(updateDeploymentDesiredStateRequest).getHttpContentString(),
                        new TypeReference<ResultModel<UpdateDeploymentDesiredStateResp>>() {
                        });
        System.out.println(JsonUtil.toJson(updateDeploymentDesiredStateRespResultModel));
        // Create savepoint: If data is empty, the trigger failed. Check the message.
        /**
         * Success includes data field with return data: {"data":{"metadata":
{"createdAt":"2020-08-18T07:04:40.379926Z","jobId":"d0d6720f-00ac-47cc-8d54-7d88a4d7b446","m odifiedAt":"2020-08-18T07:04:40.379926Z","deploymentId":"0cb796fc-2641-488e-bde8-52b2199c574 7","origin":"USER_REQUEST","resourceVersion":1,"namespace":"test","annotations":{"com.dataar tisans.appmanager.controller.deployment.spec.version":"4"},"id":"c4e40dc9-69c7-4ba0-8add-5f8 62ecb00ef"},"apiVersion":"v1","kind":"Savepoint","spec":{"savepointLocation":"oss://qiqi-zp/ vvp/flink-savepoints/namespaces/test/deployments/0cb796fc-2641-488e-bde8-52b2199c5747/c4e40d c9-69c7-4ba0-8add-5f862ecb00ef"},"status":{"state":"STARTED"}},"requestId":"188B1FFC-2729-45 8E-A404-D3CD5D972DA0"}
         * Failure has no data field and includes a message: {"RequestId":"B545121D-ED4C-4E7
1-9D76-CBD510A04E5B","HostId":"ververica-share.cnshanghai.aliyuncs.com","Code":"BadRequest","Message":"No active job for a deployment."}
```

`*/`

```
        CreateSavepointRequest
                createSavepointRequest = new CreateSavepointRequest();
        createSavepointRequest.setWorkspace(workspaceName);
        createSavepointRequest.setNamespace(namespace);
        CreateSavepointParams createSavepointParams
                = new CreateSavepointParams();
        createSavepointParams.setDeploymentId(deploymentId);
        createSavepointRequest.setParamsJson(JsonUtil.toJson(createSavepointParams));
        createSavepointRequest.setHttpContentType(FormatType.JSON);
```

```java
        createSavepointRequest.setSysVersion("2024-11-18");
        System.out.println(client.doAction(createSavepointRequest).getHttpContentString());
        ResultModel<CreateSavepointResp> savepoint =
JsonUtil.toBean(client.doAction(createSavepointRequest).getHttpContentString(),
                        new TypeReference<ResultModel<CreateSavepointResp>>() {
                        });
        System.out.println(JsonUtil.toJson(savepoint));
        // Get list of savepoints.
        ListSavepointsRequest listSavepointsRequest
                = new
                ListSavepointsRequest();
        listSavepointsRequest.setWorkspace(workspaceName);
        listSavepointsRequest.setNamespace(namespace);
        listSavepointsRequest.setDeploymentId(deploymentId);
        listSavepointsRequest.setSysVersion("2024-11-18");
        ResultModel<ListSavepointsResp> savepoints =
JsonUtil.toBean(client.doAction(listSavepointsRequest).getHttpContentString(), new TypeRefer ence<ResultModel<ListSavepointsResp>>() {
                });
        System.out.println(JsonUtil.toJson(savepoints.getData().getSavepoints()));
        System.out.println(JsonUtil.toJson(savepoints.getData().getSavepoints().size()));
        // Get list of jobs.
        ListJobsRequest listJobsRequest = new ListJobsRequest();
        listJobsRequest.setWorkspace(workspaceName);
        listJobsRequest.setNamespace(namespace);
        listJobsRequest.setDeploymentId(deploymentId);
        listJobsRequest.setSysVersion("2024-11-18");
        ResultModel<ListJobsResp> jobs =
                JsonUtil.toBean(client.doAction(listJobsRequest).getHttpContentString(), new
TypeReference<ResultModel<ListJobsResp>>() {
                });
        System.out.println(JsonUtil.toJson(jobs.getData().getJobs()));
        // Get list of deployment targets.
        ListDeploymentTargetsRequest
                listDeploymentTargetsRequest = new ListDeploymentTargetsRequest();
        listDeploymentTargetsRequest.setWorkspace(workspaceName);
        listDeploymentTargetsRequest.setNamespace(namespace);
        listDeploymentTargetsRequest.setSysVersion("2024-11-18");
        ResultModel<ListDeploymentTargetsResp> deploymentTargets =
JsonUtil.toBean(client.doAction(listDeploymentTargetsRequest).getHttpContentString(),
                        new TypeReference<ResultModel<ListDeploymentTargetsResp>>() {
                        });
System.out.println(JsonUtil.toJson(deploymentTargets.getData().getDeploymentTargets()));
        // Validate SQL syntax. On success, validationResult is
'VALIDATION_RESULT_VALID_INSERT_QUERY' or 'VALIDATION_RESULT_VALID_DDL_STATEMENT'. Otherwise , check errorDetails.
        ValidateSqlScriptRequest
                validateSqlScriptRequest = new ValidateSqlScriptRequest();
        validateSqlScriptRequest.setWorkspace(workspaceName);
        validateSqlScriptRequest.setNamespace(namespace);
        ValidateSqlScriptParams
```

`q` `p`

```java
                validateSqlScriptParams = new ValidateSqlScriptParams();
        validateSqlScriptParams.setStatement("CREATE TABLE RANDOM_TABLE(`name` STRING) with
('connector'='random','type'='random')");
        validateSqlScriptRequest.setParamsJson(JsonUtil.toJson(validateSqlScriptParams));
        validateSqlScriptRequest.setHttpContentType(FormatType.JSON);
        validateSqlScriptRequest.setSysVersion("2024-11-18");
        ResultModel<ValidateSqlScriptResp>
                validateSqlScriptRespResultModel =
JsonUtil.toBean(SdkUtil.getHttpContentString(client,
                validateSqlScriptRequest), new
TypeReference<ResultModel<ValidateSqlScriptResp>>() {
        });
        System.out.println(JsonUtil.toJson(validateSqlScriptRespResultModel));
        // Execute DDL operation: If successful,
data.result='RESULT_SUCCESS|RESULT_SUCCESS_WITH_ROWS'. Otherwise, check message.
        ExecuteSqlScriptRequest
                executeSqlScriptRequest = new ExecuteSqlScriptRequest();
        executeSqlScriptRequest.setWorkspace(workspaceName);
        executeSqlScriptRequest.setNamespace(namespace);
        ExecuteSqlScriptParams executeSqlScriptParams
                = new
                ExecuteSqlScriptParams();
        executeSqlScriptParams.setStatement("create table abaaaa (a varchar) with ('connecto
r' = 'random', 'type' = 'random');");
        executeSqlScriptParams.setStatement("show tables;");
        executeSqlScriptRequest.setParamsJson(JsonUtil.toJson(executeSqlScriptParams));
        executeSqlScriptRequest.setHttpContentType(FormatType.JSON);
        executeSqlScriptRequest.setSysVersion("2024-11-18");
        ResultModel<ExecuteSqlScriptResp>
                executeSqlScriptRespResultModel =
JsonUtil.toBean(client.doAction(executeSqlScriptRequest).getHttpContentString(),
                new TypeReference<ResultModel<ExecuteSqlScriptResp>>() {
                });
        System.out.println(JsonUtil.toJson(executeSqlScriptRespResultModel));
        // Create deployment (SQL job).
        GetGlobalDeploymentDefaultsRequest getGlobalDeploymentDefaultsRequest
                = new
                GetGlobalDeploymentDefaultsRequest();
        getGlobalDeploymentDefaultsRequest.setWorkspace(workspaceName);
        getGlobalDeploymentDefaultsRequest.setNamespace(namespace);
System.out.println(client.doAction(getGlobalDeploymentDefaultsRequest).getHttpContentString())
        getGlobalDeploymentDefaultsRequest.setSysVersion("2024-11-18");
        ResultModel<GetGlobalDeploymentDefaultsResp> globalDefaults =
JsonUtil.toBean(client.doAction(getGlobalDeploymentDefaultsRequest).getHttpContentString(),
                        new TypeReference<ResultModel<GetGlobalDeploymentDefaultsResp>>() {
                        });
        System.out.println(JsonUtil.toJson(globalDefaults.getData()));
        Deployment.DeploymentSpec spec =
                globalDefaults.getData().getSpec();
        spec.setState(DeploymentState.RUNNING);
        // SQL job.
        Artifact.SqlScriptArtifact
                sqlScriptArtifact = new
Artifact.SqlScriptArtifact();
```

`t`

```
act.SqSc
```

`pt` `t`

```java
act();
        sqlScriptArtifact.setSqlScript("INSERT INTO PRINT_TABLE SELECT /* comments */ UPPER(
name) FROM RANDOM_TABLE");
        spec.getTemplate().getSpec().setArtifact(sqlScriptArtifact);
        // To create a DataStream job, pass a different Artifact.
        Artifact.JarArtifact jarArtifact = new
                Artifact.JarArtifact();
        jarArtifact.setJarUri("oss://qiqi-zp/multioss/artifacts/namespaces/test/job-1.0-SNAP
SHOT2.jar");
        // spec.getTemplate().getSpec().setArtifact(jarArtifact);
        CreateDeploymentParams
                createDeploymentParams = new CreateDeploymentParams();
        Deployment.DeploymentMetadata metadata = new
                Deployment.DeploymentMetadata();
        metadata.setName("lxg-sdk-sql-test-5");
        spec.setDeploymentTargetId("3965ca94-2fa9-47ee-818b-ff89ddf4ba4f");
        createDeploymentParams.setMetadata(metadata);
        createDeploymentParams.setSpec(spec);
        CreateDeploymentRequest
                createDeploymentRequest = new CreateDeploymentRequest();
        createDeploymentRequest.setWorkspace(workspaceName);
        createDeploymentRequest.setNamespace(namespace);
        String paramsStr = JsonUtil.toJson(createDeploymentParams);
        System.out.printf("##########params:\n%s\n", paramsStr);
        createDeploymentRequest.setParamsJson(paramsStr);
        createDeploymentRequest.setHttpContentType(FormatType.JSON);
        createDeploymentRequest.setSysVersion("2024-11-18");
        System.out.println(client.doAction(createDeploymentRequest).getHttpContentString());
        ResultModel<CreateDeploymentResp>
                createDeploymentRespResultModel =
JsonUtil.toBean(client.doAction(createDeploymentRequest).getHttpContentString(),
                new TypeReference<ResultModel<CreateDeploymentResp>>() {
                });
        System.out.println(JsonUtil.toJson(createDeploymentRespResultModel));
        // Get list of artifacts.
        ListArtifactsRequest listArtifactsRequest = new
                ListArtifactsRequest();
        listArtifactsRequest.setWorkspace(workspaceName);
        listArtifactsRequest.setNamespace(namespace);
        listArtifactsRequest.setSysVersion("2024-11-18");
        ResultModel<ListArtifactsResp> artifacts =
JsonUtil.toBean(client.doAction(listArtifactsRequest).getHttpContentString(), new TypeRefere nce<ResultModel<ListArtifactsResp>>() {
                });
        System.out.println(JsonUtil.toJson(artifacts));
        // Get artifact.
        GetArtifactMetadataRequest
                getArtifactMetadataRequest = new GetArtifactMetadataRequest();
        getArtifactMetadataRequest.setWorkspace(workspaceName);
        getArtifactMetadataRequest.setNamespace(namespace);
        getArtifactMetadataRequest.setFilename("flip-75-demo-1.0-SNAPSHOT-1.jar");
        getArtifactMetadataRequest.setSysVersion("2024-11-18");
Systemoutprintln(clientdoAction(getArtifactMetadataRequest)getHttpContentString());
```

```java
System.out.println(client.doAction(getArtifactMetadataRequest).getHttpContentString());
        ResultModel<GetArtifactMetadataResp> artifact =
JsonUtil.toBean(client.doAction(getArtifactMetadataRequest).getHttpContentString(),
                        new TypeReference<ResultModel<GetArtifactMetadataResp>>() {
                        });
        System.out.println(JsonUtil.toJson(artifact));
        // Delete artifact.
        DeleteArtifactRequest deleteArtifactRequest
                = new
                DeleteArtifactRequest();
        deleteArtifactRequest.setWorkspace(workspaceName);
        deleteArtifactRequest.setNamespace(namespace);
        deleteArtifactRequest.setFilename("flip-75-demo-1.0-SNAPSHOT-1.jar");
        deleteArtifactRequest.setSysVersion("2024-11-18");
        DeleteArtifactResponse
                deleteArtifactResponse = client.getAcsResponse(deleteArtifactRequest);
        System.out.println(JsonUtil.toJson(deleteArtifactResponse));
        // Get list of deployments.
        ListDeploymentsRequest listDeploymentsRequest
                = new
                ListDeploymentsRequest();
        listDeploymentsRequest.setWorkspace(workspaceName);
        listDeploymentsRequest.setNamespace(namespace);
        listDeploymentsRequest.setSysVersion("2024-11-18");
        ResultModel<ListDeploymentsResp> deployments =
JsonUtil.toBean(client.doAction(listDeploymentsRequest).getHttpContentString(),
                        new TypeReference<ResultModel<ListDeploymentsResp>>() {
                        });
        System.out.println(JsonUtil.toJson(deployments));
        // Delete deployment. Specify an existing DeploymentId whose state is CANCELLED.
        DeleteDeploymentRequest
                deleteDeploymentRequest = new DeleteDeploymentRequest();
        deleteDeploymentRequest.setWorkspace(workspaceName);
        deleteDeploymentRequest.setNamespace(namespace);
        deleteDeploymentRequest.setDeploymentId(deploymentId);
        deleteDeploymentRequest.setSysVersion("2024-11-18");
        DeleteDeploymentResponse
                deleteDeploymentResponse = client.getAcsResponse(deleteDeploymentRequest);
        System.out.println(JsonUtil.toJson(deleteDeploymentResponse));
```

`}` `}`

> **Note:** For detailed sample code, contact Alibaba Cloud technical support.

#### 3.2.2 pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?> <project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-
4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.aliyun</groupId>
    <artifactId>vvp-sdk-sample-java</artifactId>
    <version>0.0.1</version>
    <properties>
        <junit.version>4.12</junit.version>
        <slf4j.version>1.7.25</slf4j.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.5.3</version>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>1.7.25</version>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-log4j12</artifactId>
            <version>1.7.25</version>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-ververica</artifactId>
            <version>0.0.3-SNAPSHOT</version>
            <classifier>shaded</classifier>
        </dependency>
</dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.1</version>
                <configuration>
                    <source>8</source>
                    <target>8</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

QL reference

## 4 Flink SQL reference

### 4.1 Overview

Flink SQL is a real-time computing SQL system designed to simplify the computing model of Realtime Compute for Apache Flink and to decrease the requirements for user skills. Flink SQL complies with standard SQL semantics. Flink SQL has the following benefits: Low development cost. Flink SQL enables you to implement complex and ever-changing business logic by using simple SQL statements instead of thousands of lines of Apache Storm code. Low maintenance cost. Flink SQL eliminates the need for you to maintain thousands of lines of Storm code. When you use Apache Storm code, system exceptions, errors, or even breakdown may occur and cause data inaccuracies. Flink SQL features specified semantics to resolve the preceding issues. Realtime Compute for Apache Flink has the following advantages: Data accuracy. Realtime Compute for Apache Flink provides unique exactly-once semantics to ensure data accuracy in various failover scenarios. Performance optimization. Realtime Compute for Apache Flink integrates SQL optimization logic to translate SQL code into highly efficient underlying Apache Storm code that can be used by universal developers. This helps to improve SQL coding efficiency. Programming extensibility. Realtime Compute for Apache Flink supports user-defined functions (UDFs). You can customize functions to implement a custom business logic or a logic that cannot be achieved by SQL statements. System scalability. Realtime Compute for Apache Flink supports auto scaling upon data surges (for example, during Double 11) while ensuring task and system stability.

### 4.2 Keywords

This topic describes Flink SQL keywords. For more information about SQL reserved keywords for Apache Flink 1.11, visit Reserved Keywords.

> **Note:** To define a Flink SQL keyword in a DDL statement, surround the keyword with backticks ('), such as `value` .

### 4.3 Create a data view

This topic describes how to create a data view in Realtime Compute for Apache Flink to simplify the development process.

**Background information**

If your business logic is complex and you need to write nested statements in DML statements, it can be difficult to locate problems. To simplify the development process, you can define a data view and write nested statements to the data view.

> **Note:** A data view displays a logical table that describes the computing logic without storing physical data.

**Syntax**

QL reference

```
CREATE TEMPORARY VIEW viewName AS [ (columnName[ , columnName]* ) ] queryStatement;
```

viewName: the name of the view. columnName: the name of the field. queryStatement: the alias of the nested statement.

```
CREATE TEMPORARY VIEW tmp_view AS SELECT
```

`*`

```
FROM
    datagen_source;
INSERT INTO
    rds_output
SELECT
```

`r,` `t,` `c,` `u`

```
FROM
    tmp_view;
```

### 4.4 Basic concepts

#### 4.4.1 Watermark

Realtime Compute performs window aggregation on data based on time attributes. In jobs that use window functions with Event Time, you must declare the Watermark method in the data source table. WATERMARK defines the event time attribute of a table. Its syntax is WATERMARK FOR rowtime_column_name AS watermark_strategy_expression. The rowtime_column_name parameter designates an existing column as the event time marker for the table. This column must be of the TIMESTAMP(3) type, reside at the top level of the schema, and may also be a computed column. The watermark_strategy_expression parameter defines the strategy for generating watermarks. It allows any non-query expression—including computed columns—to calculate the watermark. The return type of the expression must be TIMESTAMP(3), representing elapsed time since the Epoch. The system emits a watermark only if it is non-null and greater than the previously emitted local watermark (to ensure monotonic increase). The framework computes the watermark generation expression for every record. Periodically, the framework emits the largest watermark generated, provided it differs from the last emitted watermark, is not null, and exceeds the last emitted watermark. Watermarks emit at intervals configured by pipeline.auto-watermark-interval. If the interval is 0 ms, the system generates a watermark for every record and emits it when it is not null and greater than the last emitted watermark. When you use event time semantics, the table must include an event time attribute and a watermark strategy. Flink provides several common watermark strategies: Strictly ascending timestamps: WATERMARK FOR rowtime_column AS rowtime_column. The system emits a watermark equal to the maximum timestamp observed so far. Rows with timestamps greater than this maximum are not considered late. Ascending timestamps: WATERMARK FOR rowtime_column AS rowtime_column - INTERVAL '0.001' SECOND. QL reference The system emits a watermark equal to the maximum timestamp observed so far minus one millisecond. Rows with timestamps greater than or equal to this maximum are not considered late. Bounded-out-of-order timestamps: WATERMARK FOR rowtime_column AS rowtime_column - INTERVAL 'string' timeUnit. The system emits a watermark equal to the maximum timestamp observed so far minus a specified delay. For example, WATERMARK FOR rowtime_column AS rowtime_column - INTERVAL '5' SECOND implements a 5-second delay watermark strategy.

```
CREATE TABLE Orders (
 user BIGINT,
 product STRING,
 order_time TIMESTAMP(3),
 WATERMARK FOR order_time AS order_time -INTERVAL '5' SECOND
) WITH ( . . . );
```

**Summary of watermark usage**

A watermark means all events with timestamps `t'< t` have already occurred. If a watermark `t` takes effect, the system discards all subsequent records with Event Time less than `t` (currently, Realtime Compute discards these late-arriving data; future versions will support user configuration to allow updates from later data). For out-of-order streams, watermarks are critical. Even if some events arrive late, they do not excessively compromise the accuracy of window computations. In parallel data streams, when an operator has multiple input streams, the operator uses the minimum Event Time among all input streams as its Event Time.

#### 4.4.2 Computed column

A computed column uses data from other columns to calculate the value for its own column. If your source table does not contain a column of the TIMESTAMP type, you can use a computed column to convert data from fields of other types.

**Concept of computed columns**

A computed column is a virtual column and is not physically stored in a table. You can use expressions, built-in functions, or user-defined functions to calculate the value of a computed column based on data from other columns. In Flink SQL, you can use computed columns as ordinary fields.

**Use cases of computed columns**

QL reference Currently, the Event Time (also known as rowtime) column for Watermark supports only the TIMESTAMP type (supporting the LONG type in the future). You can define a watermark only in the DDL statement of a source table. If no column of the TIMESTAMP type exists in your source table, you can use a computed column to convert data from fields of other types.

**Syntax of computed columns**

```
column_name AS computed_column_expression
```

**Examples of computed columns**

The rowtime field for a watermark must be of the TIMESTAMP data type. Realtime Compute for Apache Flink currently supports the TIMESTAMP data type with millisecond precision, which corresponds to a 13-digit Unix timestamp. If the TIME field in DataHub is at microsecond precision (16-digit Unix timestamp), you can use a computed column to convert it into a 13-digit timestamp, as shown in the following example.

```
CREATE TABLE test_stream(
  a INT,
  b BIGINT,
  `TIME` BIGINT,
  ts AS TO_TIMESTAMP(TIME/1000), -- Use a computed column to convert a 16-digit timestamp
into a 13-digit timestamp.
  WATERMARK FOR ts AS WITHOFFSET(ts, 1000)
) WITH (
  'connector' = 'datahub',
  ...
```

); In the preceding example, the `TIME` field in the source table contains time information and is of the BIGINT type. The system uses the computed column feature to convert the `TIME` field into the `ts` field of the TIMESTAMP type, and then uses the `ts` field as the rowtime field for the watermark.

#### 4.4.3 Time attribute

This topic introduces the Event Time and Processing Time data types that Flink SQL supports. Flink SQL supports two time types: Event Time and Processing Time. Event Time: The event time you provide (usually the original creation time of the data). Event Time must be data you provide in the schema. Processing Time: The local system time when the system processes the event. The following figure shows the positions of different time attributes in the real-time computing process. QL reference Based on the definitions in the preceding figure, Ingestion Time and Processing Time are time attributes that the system adds to streaming records. You cannot control them. Event Time is a time attribute carried by the streaming record itself. Due to data disorder, network jitter, or other reasons, a record with Event Time of t1 (corresponding to partition1) may be processed by Flink later than a record with Event Time of t2 (corresponding to partition2), where t2 > t1.

**Event Time**

Event Time is also called rowtime. You must declare the Event Time attribute in the DDL of the source table. You can declare a field in the source table as Event Time. Currently, only a field of the TIMESTAMP type (supporting LONG type in the future) can be declared as a rowtime field. If the field is not of the TIMESTAMP type, you must use a Computed column to construct a TIMESTAMP-type column based on an existing column. However, data may arrive out of sequence due to data disorder, network jitter or other reasons, so you must explicitly define a Watermark calculation method when defining a rowtime field. The following example shows how to use a window function to aggregate data based on Event Time.

```
CREATE TABLE tt_stream(
  a VARCHAR,
  b VARCHAR,
  c TIMESTAMP,
  WATERMARK wk1 FOR c as withOffset(c, 1000)  --watermark calculation method
) WITH (
  'connector' = 'sls',
  'topic' = 'yourTopicName',
  'accessId' = 'yourAccessId',
  'accessKey' = 'yourAccessSecret'
```

);

```
CREATE TABLE rds_output(
  id VARCHAR,
  c TIMESTAMP,
  f TIMESTAMP,
  cnt BIGINT
) WITH (
  'connector' = 'rds',
  'url' = 'jdbc:mysql://****3306/test',
  'tableName' = 'yourTableName',
  'userName' = 'yourUserName',
  'password' = 'yourPassword'
```

);

```
INSERT INTO rds_output SELECT a AS id,
     SESSION_START(c, INTERVAL '1' SECOND) AS c,
     CAST(SESSION_END(c, INTERVAL '1' SECOND) AS TIMESTAMP) AS f,
     COUNT(a) AS cnt
FROM tt_stream GROUP BY SESSION(c, INTERVAL '1' SECOND), a
```

**Processing Time**

Processing Time is generated by the system and does not exist in your raw data. You must explicitly define a Processing Time column in the declaration of your source table.

```
filedName as PROCTIME()
```

QL reference The following example shows how to use a window function to aggregate data based on Processing Time.

```
CREATE TABLE mq_stream (
  a VARCHAR,
  b VARCHAR,
  c BIGINT,
  d AS PROCTIME()   ---Explicitly define a Processing Time column in the declaration of the
source table. ) WITH (
  'connector' = 'mq',
  'topic' = 'yourTopic',
  'accessId' = 'yourAccessId',
  'accessKey' = 'yourAccessSecret'
```

);

```
CREATE TABLE rds_output (
  id VARCHAR,
  c TIMESTAMP,
  f TIMESTAMP,
  cnt BIGINT
) with (
  'connector' = 'rds',
  'url' = 'yourDatebaseURL',
  'tableName' = 'yourDatabasTableName',
  'userName' = 'yourUserName',
  'password' = 'yourPassword'
```

);

```
INSERT INTO rds_output SELECT a AS id,
     SESSION_START(d, INTERVAL '1' SECOND) AS c,
     SESSION_END(d, INTERVAL '1' SECOND) AS f,
     COUNT(a) AS cnt
FROM mq_stream GROUP BY SESSION(d, INTERVAL '1' SECOND), a
```

**Propagation of time attribute fields**

Currently, a time attribute field loses its time attribute after either of the following two operations: Non-window GROUP BY Join of two streams If you continue to use the time attribute field for window function operations after either of these operations, an error similar to `org.apache.flink.table.api.ValidationException: Window can only`

```
be defined over a time attribute column. occurs.
```

### 4.5 Subscription

The subscription billing method allows you to use resources only after you pay for the resources. You must make a payment based on the subscription duration when you purchase resources. This billing method is suitable for long-term stable business for which the resource usage cycle can be estimated. This topic describes the billing rules, billing cycles, and unit prices in different regions of the subscription billing method. QL reference

| Item | Description |
|---|---|
| Billing rule | For more information about the unit prices in different regions, seeU nit prices in different regions. Important The subscription duration in the formula is measured in months. You can view the fees on the buy page. The number of compute units (CUs) consumed for management is fixed to 2. For example, the unit prices of management resources and computing resources are both USD 45.94 per CU per month. If you want to create a workspace that uses 8 CUs as computing resources and set the subscription duration to three months, the fee for creating the workspace in the Intel X86 architecture is USD 1378.2, which is calculated by using the following formula: Fee for management resources + Fee for computing resources = 2 CUs × USD 45.94 per CU per month × 3 months + 8 CUs × USD 45.94 per CU per month × 3 months = USD 275.64 + USD 1102.56 = USD 1378.2. |
| Billing cycle | The billing cycle (based on UTC+8:00) of a subscription workspace is the subscription duration of the workspace. The billing cycle starts from the time (accurate to the second) when the subscription workspace is activated or renewed and ends at 00:00:00 the next day after the expiration date. |
| Resource changes for an expired subscription instance | The impact on your business varies based on the time period after the subscription workspace expires. For more information, see Resource availability for an expired subscription. |
| Renewal | If you want to continue using a subscription workspace after it expires, you can renew the workspace. For more information, see Renewals. Note If you do not renew your workspace at the earliest opportunity, your workspace is released after it expires. To ensure service continuity, we recommend that you renew your workspace at the earliest opportunity. For more information about the resource changes for an expired subscription workspace, see Resource availability for an expired subscription. If your account has overdue payments, your workspace cannot be automatically renewed. Top up your account and manually renew the workspace. |
| Refund | You make a payment based on the subscription duration when you purchase a subscription workspace. If you no longer require the workspace due to changes in business requirements, you can submit a ticket to unsubscribe from the workspace and apply for a refund. For more information about the operations and rules, see Refund policy. |
| Resource scaling | After you create a subscription workspace, you can modify the resource configurations of your workspace to scale the workspace. For more information, see Reconfigure resources. |

QL reference

**Unit prices in different regions**

> **Important:** You can obtain the actual price on the buy page.

**Billing for the Intel X86 architecture**

Unit prices of management resources of a workspace in the Intel X86 architecture

| Region | Unit price (USD per CU per hour) |
|---|---|
| Singapore | 45.94 |
| Japan (Tokyo) | 50.95 |
| Germany (Frankfurt) | 48.40 |
| Indonesia (Jakarta) | 42.23 |
| US (Silicon Valley) | 37.35 |
| Malaysia (Kuala Lumpur) | 42.23 |
| UK (London) | 44.66 |
| China (Hong Kong) | 47.55 |
| China (Beijing), China (Shanghai), China (Hangzhou), and China (Shenzhen) | 31.26 |
| China (Zhangjiakou) | 28.83 |

Unit prices of computing resources of a namespace in the Intel X86 architecture

| Region | Unit price in a single zone (USD per CU per month) | Unit price across zones (USD per CU per month) |
|---|---|---|
| Singapore | 45.94 |   |
| Japan (Tokyo) | 50.95 |   |
| Germany (Frankfurt) | 48.40 |   |

|   |   | Cross-zone high availability not supported |
|---|---|---|
| Indonesia (Jakarta) | 42.23 |   |
| US (Silicon Valley) | 37.35 |   |
| Malaysia (Kuala Lumpur) | 42.23 |   |
| UK (London) | 44.66 |   |
| China (Hong Kong) | 47.55 | 66.57 |
| China (Beijing), China (Shanghai), China (Hangzhou), and China (Shenzhen) | 31.26 | 43.764 |
| China (Zhangjiakou) | 28.83 | 40.362 |

**Billing for the YiTian ARM architecture**

Unit prices of management resources of a workspace in the YiTian ARM architecture

| Region | Unit price (USD per CU per month) |
|---|---|
| China (Hangzhou) | 31.26 |

Unit prices of computing resources of a namespace in the YiTian ARM architecture

| Region | Unit price (USD per CU per month) |
|---|---|
| China (Hangzhou) | 21 |

**Resource changes for an expired subscription instance**

A subscription workspace has a validity period based on the subscription duration that you specify when you purchase the workspace. After the subscription duration of a subscription workspace ends, you can no longer use the workspace. If you do not renew the workspace within a specified period of time, the workspace is automatically released. The following figure shows the resource changes for an expired workspace and related operations. Manual renewal or autorenewal to extend the validity period of the The service cannot service be restored. You must reactivate the service. Service in Service More than 15 Resources Service Within 15 days days after after expiration use expired suspended released expiration Service QL reference

| Payment status |   | Suspension policy | Solution |
|---|---|---|---|
| Before the workspace expires |   | The system sends notifications to you by email or text message. | Renew the workspace. After the renewal is successful, you can continue using the workspace. For more information, see Renewals. |
| After the workspac e expires | Within 15 days after the workspace expires | You cannot access the workspace. The deployments that are running in the workspace stop running. | Renew the workspace. After the renewal is successful, you can continue using the workspace. For more information, see Renewals. |
|   | 15 days after the workspace expires | The workspace is automatically released. The deployment data of the workspace is deleted and cannot be restored. Note Resources such as the JAR packages that you upload are not deleted and are stored in your Object Storage Service (OSS) buckets. | You cannot restore the instance. |

**References**

For more information about how to change the billing method of a workspace from subscription to pay-as-you-go, see Switch from subscription to pay-as-you-go. For more information about how to create a workspace, see Activate Realtime Compute for Apache Flink.

#### 4.5.1 INSERT INTO statement

This topic describes how to write data to one or more sinks in a job.

**Example of how to write data to a sink**

Source table

```
CREATE TABLE datagen_source (
  name VARCHAR,
  score BIGINT
) WITH (
  'connector' = 'datagen'
```

); Result table QL reference

```
create table blackhole_sink(
  name VARCHAR,
  score BIGINT
) WITH (
  'connector' = 'blackhole'
```

); DML

```
INSERT INTO blackhole_sink SELECT UPPER(name), score FROM datagen_source;
```

**Example of how to write data to multiple sinks**

Source table

```
CREATE TABLE datagen_source (
  name VARCHAR,
  score BIGINT
) WITH (
  'connector' = 'datagen'
```

); Result table A

```
CREATE TABLE blackhole_sinkA(
  name VARCHAR,
  score BIGINT
) WITH (
  'connector' = 'blackhole'
```

); Result table B

```
CREATE TABLE blackhole_sinkB(
  name VARCHAR,
  score BIGINT
) WITH (
  'connector' = 'blackhole'
```

); DML In this example, data is written to two sinks.

```
BEGIN STATEMENT SET; -- This is required when you write data to multiple sinks. INSERT INTO blackhole_sinkA
  SELECT UPPER(name), sum(score)
  FROM datagen_source
  GROUP BY UPPER(name);
INSERT INTO blackhole_sinkB
  SELECT LOWER(name), max(score)
  FROM datagen_source
  GROUP BY LOWER(name);
END; -- This is required when you write data to multiple sinks.
```

> **Note:** The statement that writes data to multiple sinks must start with **BEGIN** **STATEMENT SET;** and end with **END;**.

QL reference

### 4.6 Query statements

This topic describes the query statements provided by Flink. For more information about the query statements provided by Apache Flink 1.11, visit Queries.

### 4.7 Window functions

This topic describes the window functions, time attributes, and window types supported by Flink SQL. Flink SQL supports aggregation over infinite windows. You do not need to explicitly define windows in SQL statements. Flink SQL also supports aggregation over a specific window. For example, if you want to count the number of users who clicked a URL in the previous minute, you can define a window to collect data about user clicks in the previous minute. Then, you can compute the data in the window to obtain the result. Flink SQL supports window aggregates and over aggregates. This topic describes window aggregates. Window aggregates support the windows that are defined based on the following time attributes: event time and processing time. The TUMBLE, HOP, and SESSION window functions are supported for each time attribute.

> **Warning:** The TUMBLE, HOP, and SESSION functions cannot be used with the LAST_VALUE, FIRST_VALUE, or TopN function. If you use these window functions with the LAST_VALUE, FIRST_VALUE, or TopN function, the data becomes out of order and is discarded. As a result, the output data is abnormal.

**Time attributes**

Flink SQL supports two time attributes: event time and processing time. For more information about time attributes, see Time attributes. Flink aggregates data in windows based on the time attributes. The windowing method varies based on the time attributes. Event time: the event time that you provide in the data store. The system closes a window based on the watermark that is generated based on the event time of the data. A window ends only when the value of the watermark is later than the time when the window closes. The output data is generated when the window ends. The window generates output data only if the data that triggers the window to end flows into Flink. The watermark value for a single subtask increments. If multiple subtasks run or multiple source tables exist, the minimum watermark value is used.

> **Important:** If an out-of-order data record in which the time is later than the current time exists in a source table or no data exists in a subtask or a partition of a source table, the window may not be terminated and the output data may be abnormal. To avoid this issue, you must specify an offset based on the out-of-order data and make sure that data exists in all subtasks and all partitions of the source table. If no data exists in a subtask or a partition of the source table, the watermark cannot advance and the window cannot be terminated in a timely manner. In this case, you can add
> `table.exec.source.idle-timeout: 10s` to the Other Configuration field in the Parameters section of the Configuration tab on the Deployments page to trigger the termination of the window. For more information about this parameter, see Configuration.
> After data is processed by using GROUP BY, JOIN operations on two data streams, or OVER window nodes, the watermark property is lost and the event time can no longer be used for windowing.

QL reference Processing time: the local system time at which the system processes an event. The processing time is generated by Flink and does not exist in your raw data. Therefore, you must explicitly define a Processing Time column.

> **Note:** The processing time is affected by the speed at which events reach Flink and the order in which data is processed in Flink. Therefore, the results of each backtrack may be different.

**Cascading windows**

The event time attribute of the rowtime column no longer takes effect after a window operation is complete. You can use a helper function such as `TUMBLE_ROWTIME` , `HOP_ROWTIME` , or `SESSION_ROWTIME` to obtain `max(rowtime)` of the rowtime column in a window. You can use the obtained value as the rowtime of the time window. The value is `window_end - 1` and is of the TIMESTAMP data type. The TIMESTAMP value has the rowtime attribute. For example, if the time span of a window is `[00:00, 00:15)` , `00:14:59.999` is returned. In the following example, 1-hour tumbling windows are used to aggregate data based on the aggregation results of 1-minute tumbling windows. This helps you meet various window requirements. QL reference

```
CREATE TEMPORARY TABLE user_clicks(
  username varchar,
  click_url varchar,
  eventtime varchar,
  ts AS TO_TIMESTAMP(eventtime),
  WATERMARK FOR ts AS ts - INTERVAL '2' SECOND   -- Define a watermark for rowtime.
) with (
  'connector'='sls',
  ...
```

);

```
CREATE TEMPORARY TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
  'connector'='datahub'        -- Simple Log Service allows you to export only VARCHAR-type
DDL statements. Therefore, DataHub is used to store data.
  ...
```

);

```
CREATE TEMPORARY VIEW one_minute_window_output AS SELECT
  TUMBLE_ROWTIME(ts, INTERVAL '1' MINUTE) as rowtime,  -- Use TUMBLE_ROWTIME as the
aggregation time of the level-two window.
  username,
  COUNT(click_url) as cnt
FROM user_clicks GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE),username; BEGIN statement set; INSERT INTO tumble_output SELECT
  TUMBLE_START(rowtime, INTERVAL '1' HOUR),
  TUMBLE_END(rowtime, INTERVAL '1' HOUR),
  username,
  SUM(cnt)
FROM one_minute_window_output GROUP BY TUMBLE(rowtime, INTERVAL '1' HOUR), username; END;
```

**Intermediate data**

The intermediate data of a window is divided into two types: keyed state and timer. The two types of data can be stored in different storage media. You can select different storage combinations based on the characteristics of your deployment. The following table describes the supported storage combinations.

| Storage for keyed state | Storage medium for timers |
|---|---|
| GeminiStateBackend | Memory |

QL reference

| HashMapStateBackend | Memory |
|---|---|
| RocksDBStateBackend | Memory |
| RocksDBStateBackend | File |

For more information about state storage backends, see GeminiStateBackend and HashMapStateBackend. Timers are mainly used to trigger expired windows. If the memory is sufficient, you can store the timers in the memory for better performance. If a large number of timers exist or memory resources are insufficient, you can use RocksDBStateBackend to store the timers in a RocksDB file.

#### 4.7.1 Overview

This topic describes the window functions, time attributes, and window types that Flink SQL supports. Flink SQL supports aggregation over infinite windows. Windows do not need to be explicitly defined in SQL statements. Flink SQL also supports aggregation over a specific window. For example, to count the number of users who clicked a URL in the last minute, you can define a window to collect data about user clicks for the previous minute. Then, you can compute the data in the window to obtain the result. Flink SQL supports window aggregates and over aggregates. This topic describes window aggregates. Window aggregates support the windows that are defined based on the following two time attributes: event time and processing time. For each time attribute, Flink SQL supports three window types: tumbling window, sliding window, and session window.

**Time attributes**

Flink SQL supports two time attributes: event time and processing time. Realtime Compute for Apache Flink aggregates data in windows based on these time attributes. The event time attribute specifies the time when each data entry is created. It is provided in the schema. The processing time attribute specifies the local system time at which the system processes an event.

> **Note:** For more information about the time attributes in Apache Flink, visit Time Attributes.

**Cascading windows**

The event time attribute of the rowtime column no longer takes effect after a window operation is complete. You can use a helper function such as `TUMBLE_ROWTIME` , `HOP_ROWTIME` , or `SESSION_ROWTIME` to obtain `max(rowtime)` of the rowtime column in a window. You can use the obtained value as the rowtime of the time window. The value is `window_end - 1` and is of the TIMESTAMP data type. The TIMESTAMP value has the rowtime attribute. For example, if the time span of a window is `[00:00, 00:15)` , `00:14:59.999` is returned. In the following example, 1-hour tumbling windows are used to aggregate data based on the aggregation results of 1-minute tumbling windows. This helps you meet various window requirements. QL reference

```
CREATE TEMPORARY TABLE user_clicks(
  username varchar,
  click_url varchar,
  eventtime varchar,
  ts AS TO_TIMESTAMP(eventtime),
  WATERMARK FOR ts AS ts - INTERVAL '2' SECOND   -- Define a watermark for the rowtime.
) with (
  'connector'='sls',
  ...
```

);

```
CREATE TEMPORARY TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
  'connector'='datahub'        -- Log Service allows you to export only VARCHAR-type DDL sta
tements. Therefore, DataHub is used for storage.
  ...
```

);

```
CREATE TEMPORARY VIEW one_minute_window_output AS SELECT
  TUMBLE_ROWTIME(ts, INTERVAL '1' MINUTE) as rowtime,  -- Use TUMBLE_ROWTIME as the
aggregation time of the level-two window.
  username,
  COUNT(click_url) as cnt
FROM user_clicks GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE),username; BEGIN statement set; INSERT INTO tumble_output SELECT
  TUMBLE_START(rowtime, INTERVAL '1' HOUR),
  TUMBLE_END(rowtime, INTERVAL '1' HOUR),
  username,
  SUM(cnt)
FROM one_minute_window_output GROUP BY TUMBLE(rowtime, INTERVAL '1' HOUR), username; END;
```

#### 4.7.2 Tumbling window

This topic describes how to use the Flink rolling window function. QL reference A tumbling window (TUMBLE) assigns each element to a window of a specified size. Typically, a tumbling window has a fixed size and windows do not overlap. For example, if you specify a 5minute tumbling window, an infinite stream of data divides into windows such as `[0:00, 0:05)` , `[0:05, 0:10)` , `[0:10, 0:15)` , and so on. The following figure shows a 30-second tumbling window.

**Syntax**

Use the TUMBLE function in the GROUP BY clause to define a tumbling window.

```xml
TUMBLE(<time-attr>, <size-interval>) <size-interval>: INTERVAL 'string' timeUnit
```

> **Note:** The `<time-attr>` parameter must be a valid time attribute field in the time stream, specified as either Processing Time or Event Time. For more information about how to define Time attributes, see Overview.

**Identifier functions**

Use an identifier function to select the start time or end time of a window. The time attribute of the window supports aggregation for downstream windows.

| Window identifier function |   | Return type | Description |
|---|---|---|---|
| TUMBLE START(time- _ |   | TIMESTAMP | Returns the start time of the window (inclusive). For example, for the window [00:10, 00:15) , the function returns 00:10 . |
|   | TUMBLE START(time- _ |   |   |
| attr, size- |   |   |   |
| interval) |   |   |   |

QL reference

| TUMBLE END(time- |   | TIMESTAMP | Returns the end time of the window (inclusive). For example, for the window [00:00, 00:15] , the function returns 00:15 . |
|---|---|---|---|
|   | TUMBLE END(time- |   |   |
| _ attr, size- | _ |   |   |
| interval) |   |   |   |
| TUMBLE ROWTIME(time _ |   | TIMESTAMP(rowtime- attr) | Returns the end time of the window (exclusive). For example, for the window [00:00, 00:15] , the function returns 00:14:59.999 . The return value is a rowtime attribute, which means you can perform time-based operations on this field, such as cascading windows. You can use this function only on Event Time-based windows. For more information, see Cascading windows. |
|   | TUMBLE ROWTIME(time _ |   |   |
| -attr, size- |   |   |   |
| interval) |   |   |   |
| TUMBLE PROCTIME(tim _ |   | TIMESTAMP(rowtime- attr) | Returns the end time of the window (exclusive). For example, for the window [00:00, 00:15] , the function returns 00:14:59.999 . The return value is a proctime attribute, which meands you can perform time-based operations on this field, such as cascading windows. You can use this function only on Processing Time-based windows. For more information, see Cascading windows. |
|   | TUMBLE PROCTIME(tim _ |   |   |
| e-attr, size- |   |   |   |
| interval) |   |   |   |

**Example of using Event Time to count clicks per minute for each**

**user on a specified website**

Test data

| username (VARCHAR) | click url (VARCHAR) _ | ts (TIMESTAMP) |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

Test statement QL reference

```
CREATE TEMPORARY TABLE user_clicks(
  username varchar,
  click_url varchar,
  eventtime varchar,
  ts AS TO_TIMESTAMP(eventtime),
  WATERMARK FOR ts AS ts - INTERVAL '2' SECOND  --Define watermark for Rowtime.
) with (
  'connector'='sls',
  ...
```

);

```
CREATE TEMPORARY TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
  'connector'='datahub'          --SLS currently supports only VARCHAR-type DDL for output
, so use DataHub for storage.
  ...
```

);

```
INSERT INTO tumble_output SELECT TUMBLE_START(ts, INTERVAL '1' MINUTE) as window_start, TUMBLE_END(ts, INTERVAL '1' MINUTE) as window_end, username, COUNT(click_url) FROM user_clicks GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE),username;
```

Test results

|   | window start _ (TIMESTAMP) |   |   |   | window end _ (TIMESTAMP) |   |   | username (VARCHAR) | clicks (BIGINT) |
|---|---|---|---|---|---|---|---|---|---|
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 3 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | J |   |
|   | 10:00:00.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:01:00.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 2 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | J |   |
|   | 10:01:00.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:02:00.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Timo | 1 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | T |   |
|   | 10:02:00.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:03:00.0 |   |   |   |   |

**Example of using Processing Time to count clicks per minute for**

**each user on a specified website**

Test data

| username (VARCHAR) | click url (VARCHAR) _ |
|---|---|

QL reference

| Jark | http://taobao.com/xxx |
|---|---|
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Timo | http://taobao.com/xxx |

Test statement

```
CREATE TEMPORARY TABLE window_test (
  username   VARCHAR,
  click_url  VARCHAR,
  ts as PROCTIME()
) WITH (
  'connector'='sls',
  ...
```

);

```
CREATE TEMPORARY TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
  'connector'='datahub'              -- Currently, SLS supports only VARCHAR-type DDL for
output, so use DataHub for storage.
  ...
```

);

```
INSERT INTO tumble_output SELECT TUMBLE_START(ts, INTERVAL '1' MINUTE), TUMBLE_END(ts, INTERVAL '1' MINUTE), username, COUNT(click_url) FROM window_test GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE), username;
```

Test results

| window start _ (TIMESTAMP) | window end _ (TIMESTAMP) | username (VARCHAR) | clicks (BIGINT) |
|---|---|---|---|

QL reference

|   | 2019-04-11 |   |   |   |   |   |   |   |   | Jark | 5 |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   | 2019-04-11 |   |   |   |   | 2 | 019-04-11 |   |   |   |
|   | 14:43:00.00 |   |   |   |   |   |   |   |   |   |   |
|   |   |   | 0 |   |   | 14:44:00.000 |   |   |   |   |   |
|   | 2019-04-11 |   |   |   |   |   |   |   |   | Timo | 1 |
|   |   | 2019-04-11 |   |   |   |   | 20 |   | 19-04-11 | Tim |   |
|   | 14:43:00.00 |   |   |   |   |   |   |   |   |   |   |
|   |   |   | 0 |   |   | 14:44:00.000 |   |   |   |   |   |

#### 4.7.3 Sliding window

This topic describes how to use the Flink sliding window function. A sliding window (HOP) differs from a tumbling window in that its windows can overlap. A sliding window has two parameters: **slide** and **size**. The **slide** parameter defines the step size for each slide. The **size** parameter defines the window size.
**slide < size**: Windows overlap, and the system assigns each element to multiple windows.
**slide = size**: This setting is equivalent to a tumbling window (TUMBLE).
**slide > size**: This setting is equivalent to a hopping window. Windows do not overlap and have
gaps between them. In most cases, most elements fit into multiple window scenarios because windows overlap. Therefore, sliding windows are useful for calculating moving averages. For example, to calculate the average value of data from the past 5 minutes and update it every 10 seconds, set **slide** to 10 seconds and **size** to 5 minutes. The following figure shows a sliding window with a 30-second interval and a 1-minute window size. QL reference

**Function syntax**

Use the HOP function in the GROUP BY clause to define a sliding window.

```xml
HOP(<time-attr>, <slide-interval>,<size-interval>) <slide-interval>: INTERVAL 'string' timeUnit <size-interval>: INTERVAL 'string' timeUnit
```

> **Note:** The `<time-attr>` parameter must be a valid time attribute field in the stream, specified as either Processing Time or Event Time. For more information about how to define Time attributes, see Overview.

**Identifier functions**

Use a sliding window identifier function to select the start time or end time of a window. The time attribute of the window supports aggregation for downstream windows.

|   | Window identifier function |   | Return type | Description |
|---|---|---|---|---|
|   | HOP START(<time- _ |   |   | Returns the start time of the window (inclusive). For example, for the window [00:10, 00:15) , the function returns 00:10 . |
|   |   | HOP START(<time- _ |   | Returns the sta |
|   | attr>, <slide- |   |   |   |
|   |   |   | TIMESTAMP |   |
|   |   |   | TIMES |   |
|   | interval>, <size- |   |   |   |
|   | interval>) |   |   |   |
|   | HOP END(<time- _ |   |   | Returns the end time of the window (inclusive). For example, for the window [00:00, 00:15) , the function returns 00:15 . |
|   |   | HOP END(<time- _ |   | Returns the |
|   | attr>, <slide- |   |   |   |
|   |   |   | TIMESTAMP |   |
|   |   |   | TIMES |   |
|   | interval>, <size- |   |   |   |
|   | interval>) |   |   |   |
|   | HOP ROWTIME(<time- _ |   |   | Returns the end time of the window (exclusive). For example, for the window [00:00, 00:15) , the function returns 00:14:59.999 . The return value is a rowtime attribute, which means can perform time-based operations on this field, such as Cascading windows. You can use this function only on Event Time-based windows. |
|   |   | HOP ROWTIME(<time- _ |   | example, for the |
|   | attr>, <slide- |   | TIMESTAMP (rowtime- |   |
|   | interval>, <size- |   | attr) |   |
|   | interval>) |   |   |   |
|   | HOP PROCTIME(<time- _ |   |   | Returns the end time of the window (exclusive). For example, for the window [00:00, 00:15) , the function returns 00:14:59.999 . The return value is a proctime attribute, which meands you can perform time-based operations on this field, such as Cascading windows. You can use this function only on Processing Time-based windows. |
|   |   | HOP PROCTIME(<time- _ |   | example, for the w |
|   | attr>, <slide- |   | TIMESTAMP (rowtime- |   |
|   | interval>, <size- |   | attr) |   |
|   | interval>) |   |   |   |

|   | [00:10, 00:15) |
|---|---|
| 00:10 |   |

|   | [00:00, 00:15) |
|---|---|
| 00:15 |   |

Count the number of clicks for each user over the past minute. Update the count every 30 seconds. This means the system uses a 1-minute window and slides it every 30 seconds. Test data QL reference

| username (VARCHAR) | click url (VARCHAR) _ | ts (TIMESTAMP) |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

Test statement

```
CREATE TEMPORARY TABLE user_clicks (
  username VARCHAR,
  click_url VARCHAR,
  eventtime VARCHAR,
  ts AS TO_TIMESTAMP(eventtime),
  WATERMARK FOR ts AS ts - INTERVAL '2' SECOND  --Define a watermark for Rowtime.
) with (
  'connector'='sls',
  ...
```

);

```
CREATE TEMPORARY TABLE hop_output (
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
  'connector'='datahub'           --SLS currently supports only VARCHAR-type DDL for outpu
t, so use DataHub for storage.
  ...
```

);

```
INSERT INTO
    hop_output
SELECT
    HOP_START (ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE),
    HOP_END (ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE),
    username,
    COUNT (click_url)
FROM
    user_clicks
GROUP BY
    HOP (ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE),username;
```

QL reference Test results

|   | window start _ (TIMESTAMP) |   |   |   | window end _ (TIMESTAMP) |   |   | username (VARCHAR) | clicks (BIGINT) |
|---|---|---|---|---|---|---|---|---|---|
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 2 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | J |   |
|   | 09:59:30.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:00:30.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 3 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | J |   |
|   | 10:00:00.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:01:00.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 2 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | J |   |
|   | 10:00:30.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:01:30.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 2 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | J |   |
|   | 10:01:00.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:02:00.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 1 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | J |   |
|   | 10:01:30.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:02:30.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Timo | 1 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | T |   |
|   | 10:02:00.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:03:00.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Timo | 1 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | T |   |
|   | 10:02:30.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:03:30.0 |   |   |   |   |

The HOP window cannot read the time when data enters. The start time of the first window shifts backward. **Shift duration = Window duration - Step size** . See the following table for examples.

| Window duration (seconds ) | Step size (seconds) |   | Event Time |   |   |   | StartTime of the first window |   |   |   |   | EndTime of the first window |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 120 | 30 |   | 2019-07-31 |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   | 2019-07-31 |   |   |   | 20 | 19-07-31 |   |   |   | 20 | 19-07-31 |   |
|   |   |   | 10:00:00 |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   | .0 |   | 09:58:30 |   |   | .0 |   | 10:00:30.0 |   |   |   |
| 60 | 10 |   | 2019-07-31 |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   | 2019-07-31 |   |   |   | 20 | 19-07-31 |   |   |   | 20 | 19-07-31 |   |
|   |   |   | 10:00:00 |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   | .0 |   | 09:59:10 |   |   | .0 |   | 10:00:10.0 |   |   |   |

#### 4.7.4 Session window

This topic describes how to use the Flink session window function. QL reference A session window (SESSIOIN) groups elements by SESSION activity. Unlike tumbling windows and sliding windows, a session window has no overlapping windows or fixed window size. Instead, the system closes the window when it no longer receives elements within a fixed time period, which indicates a session break. You can configure a session window with a gap interval which defines the length of the inactive period. For example, a data stream representing mouse click activity may have long idle periods interspersed with bursts of clicks. If data arrives after the specified gap interval, the system starts a new window. The following figure shows an example of session windows. Each key forms different windows due to different data distributions.

**Function syntax**

Use the SESSION function in the GROUP BY clause to define a session window.

```xml
SESSION(<time-attr>, <gap-interval>) <gap-interval>: INTERVAL 'string' timeUnit
```

**Note**

`<time-attr>` must be a valid time attribute field in the data stream, specified as either Processing Time or Event Time. For more information about how to define Time attributes, see Overview.

**Identifier functions**

Use an identifier function to select the start time or end time of a window. The time attribute of the window supports aggregation for downstream windows. QL reference

| Window identifier function |   | Return type | Description |   |   |
|---|---|---|---|---|---|
| SESSION START(<time _ |   |   | Returns the start time of the window (inclusive). For example, for a window [00:10,00:15) , the function returns 00:10 , which is the time of the first record in this session window. |   |   |
|   | SESSION START(<time _ |   |   |   |   |
| -attr>, <gap- |   |   |   |   |   |
|   |   | T |   |   |   |
| interval>) |   |   |   |   |   |
| SESSION END(<time- _ |   | Timestamp | Returns the end time of the window (inclusive). For example, for a window [00:00,00:15) , the function returns 00:15 , which is the time of the last record in this session window plus <gap- interval> . |   |   |
|   | SESSION END(<time- _ |   |   |   |   |
| attr>, <gap- |   |   |   |   |   |
| interval>) |   |   |   | <gap- |   |
| SESSION ROWTIME(<ti _ |   |   | Returns the end time of the window (exclusive). For example, for a window [00:00,00:15) , the function returns 00:14:59.999 . The return value is a rowtime attribute, which means you can perform time-based operations on this field, such as Cascading windows. You can use this function only on Event Time-based windows. |   |   |
|   | SESSION ROWTIME(<ti _ | Timestamp (rowtime- |   |   |   |
| me-attr>, <gap- |   | Tim |   |   |   |
|   |   | attr |   |   |   |
| interval>) |   |   |   |   |   |
| SESSION PROCTIME(<t _ |   |   | Returns the end time of the window (exclusive). For example, for a window [00:00,00:15) , the function returns 00:14:59.999 . The return value is a proctime attribute, which means you can perform time-based operations on this field, such as Cascading windows. You can use this function only on Processing Time-based windows. |   |   |
|   | SESSION PROCTIME(<t _ | Timestamp (rowtime- | f |   |   |
| ime-attr>, <gap- |   | Time |   |   |   |
|   |   | attr) |   |   |   |
| interval>) |   |   |   |   |   |

|   | interval> |
|---|---|

|   | [00:00,00:15) |
|---|---|
| 00:14:59.999 |   |

|   | [00:00,00:15) |
|---|---|
| 00:14:59.999 |   |

Count the number of clicks for each user during each active session. The session timeout duration is 30 seconds. Test data

| username (VARCHAR) | click url (VARCHAR) _ | ts (TIMESTAMP) |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |

QL reference

| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |
|---|---|---|

Test statement

```
CREATE TEMPORARY TABLE user_clicks(
  username varchar,
  click_url varchar,
  eventtime varchar,
  ts AS TO_TIMESTAMP(eventtime),
  WATERMARK FOR ts AS ts - INTERVAL '2' SECOND  --Define a watermark for Rowtime.
) with (
  'connector'='sls',
  ...
```

);

```
CREATE TEMPORARY TABLE session_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
  'connector'='datahub'           --SLS currently supports only VARCHAR-type DDL for outpu
t, so use DataHub for storage.
  ...
```

);

```
INSERT INTO session_output SELECT SESSION_START(ts, INTERVAL '30' SECOND), SESSION_END(ts, INTERVAL '30' SECOND), username, COUNT(click_url) FROM user_clicks GROUP BY SESSION(ts, INTERVAL '30' SECOND), username;
```

Test results

|   | window start _ (TIMESTAMP) |   |   |   | window end _ (TIMESTAMP) |   |   | username (VARCHAR) | clicks (BIGINT) |
|---|---|---|---|---|---|---|---|---|---|
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 2 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | J |   |
|   | 10:00:00.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:00:40.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 2 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | J |   |
|   | 10:00:49.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:01:35.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 1 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | J |   |
|   | 10:01:58.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:02:28.0 |   |   |   |   |

QL reference

|   | 2017-10-10 |   |   |   |   |   |   | Timo | 1 |
|---|---|---|---|---|---|---|---|---|---|
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | T |   |
|   | 10:02:10.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:02:40.0 |   |   |   |   |

#### 4.7.5 OVER windows

An OVER window is a standard window used in traditional databases. Over aggregates are different from window aggregates that are based on GROUP BY clauses. If streaming data uses OVER windows, each element corresponds to an OVER window. An OVER window can be determined based on an actual row or an actual value (timestamp value) of an element. Elements of a stream may be distributed across multiple windows. In a stream that uses OVER windows, each element corresponds to an OVER window and triggers data computing once. The row determined by each element that triggers computing is the last row of the window where the element is located. In the underlying implementation of Realtime Compute for Apache Flink, data for OVER windows is centrally managed. Only one copy of the data is stored. Logically, an OVER window is created for each element. Realtime Compute for Apache Flink calculates the data for each OVER window and then deletes the data that is no longer used after the calculation is complete.

**Syntax**

```
SELECT
    agg1(col1) OVER (definition1) AS colName,
    ...
    aggN(colN) OVER (definition1) AS colNameN
FROM Tab1;
```

agg1(col1): aggregates input data based on the col1 column specified by GROUP BY. OVER (definition1): defines an OVER window. AS colName: specifies the alias of a column.

> **Note:** OVER (definition1) for agg1 through aggN must be the same.
> The alias specified by AS can be queried by using an outer SQL statement.

**Window types**

In Flink SQL, OVER windows are defined in compliance with standard SQL syntax. Traditional OVER windows are not classified into fine-grained window types. OVER windows are classified into the following two types based on how computed rows are determined: ROWS OVER windows: Each row of elements is treated as a new computed row. A new window is generated for each row. RANGE OVER windows: All rows of elements with the same timestamp are treated as one computed row and are assigned to the same window.

**Attributes**

| Orthogonal attribute | Description | proctime | eventtime |
|---|---|---|---|
| ROWS OVER Window | A window is determined based on the actual row of an element. | Supported | Supported |

QL reference

| RANGE OVER Window | A window is determined based on the timestamp value of an element. | Supported | Supported |
|---|---|---|---|

**ROWS OVER windows**

For a ROWS OVER window, each element is assigned to a window. Syntax

```
SELECT
    agg1(col1) OVER(
     [PARTITION BY (value_expression1,..., value_expressionN)]
     ORDER BY timeCol
     ROWS
     BETWEEN (UNBOUNDED | rowCount) PRECEDING AND CURRENT ROW) AS colName, ...
FROM Tab1;
```

value_expression: specifies the value expression used for partitioning. timeCol: specifies the time field used to sort elements. rowCount: specifies the number of rows that precede the current row. This example describes bounded ROWS OVER windows. Assume that an on-sale product table contains item IDs, item types, on-sale time, and prices. Calculate the highest price among the three products similar to the current product before the current product is on sale. Test data

| Item ID | Item type | On-sale time | Price |
|---|---|---|---|
| ITEM001 | Electronic | 2017-11-11 10:01:00 | 20 |
| ITEM002 | Electronic | 2017-11-11 10:02:00 | 50 |
| ITEM003 | Electronic | 2017-11-11 10:03:00 | 30 |
| ITEM004 | Electronic | 2017-11-11 10:03:00 | 60 |
| ITEM005 | Electronic | 2017-11-11 10:05:00 | 40 |
| ITEM006 | Electronic | 2017-11-11 10:06:00 | 20 |
| ITEM007 | Electronic | 2017-11-11 10:07:00 | 70 |
| ITEM008 | Clothes | 2017-11-11 10:08:00 | 20 |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:01:00 |   |   |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:02:00 |   |   |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:03:00 |   |   |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:03:00 |   |   |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:05:00 |   |   |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:06:00 |   |   |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:07:00 |   |   |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:08:00 |   |   |

QL reference Test statements

```
CREATE TEMPORARY TABLE tmall_item(
  itemID VARCHAR,
  itemType VARCHAR,
  eventtime varchar,
  onSellTime AS TO_TIMESTAMP(eventtime),
  price DOUBLE,
  WATERMARK FOR onSellTime AS onSellTime - INTERVAL '0' SECOND  -- Define a watermark
for the rowtime. ) WITH (
  'connector' = 'sls',
   ...
```

);

```
SELECT
    itemID,
    itemType,
    onSellTime,
    price,
    MAX(price) OVER (
        PARTITION BY itemType
        ORDER BY onSellTime
        ROWS BETWEEN 2 preceding AND CURRENT ROW) AS maxPrice
FROM tmall_item;
```

Test results

| itemID | itemType | onSellTime | price | maxPrice |
|---|---|---|---|---|
| ITEM001 | Electronic | 2017-11-11 10:01:00 | 20 | 20 |
| ITEM002 | Electronic | 2017-11-11 10:02:00 | 50 | 50 |
| ITEM003 | Electronic | 2017-11-11 10:03:00 | 30 | 50 |
| ITEM004 | Electronic | 2017-11-11 10:03:00 | 60 | 60 |
| ITEM005 | Electronic | 2017-11-11 10:05:00 | 40 | 60 |
| ITEM006 | Electronic | 2017-11-11 10:06:00 | 20 | 60 |
| ITEM007 | Electronic | 2017-11-11 10:07:00 | 70 | 70 |
| ITEM008 | Clothes | 2017-11-11 10:08:00 | 20 | 20 |

|   |   | 2017-11-11 |
|---|---|---|
| ronic | 10:01:00 |   |

|   |   | 2017-11-11 |
|---|---|---|
| ronic | 10:02:00 |   |

|   |   | 2017-11-11 |
|---|---|---|
| ronic | 10:03:00 |   |

|   |   | 2017-11-11 |
|---|---|---|
| ronic | 10:03:00 |   |

|   |   | 2017-11-11 |
|---|---|---|
| ronic | 10:05:00 |   |

|   |   | 2017-11-11 |
|---|---|---|
| ronic | 10:06:00 |   |

|   |   | 2017-11-11 |
|---|---|---|
| ronic | 10:07:00 |   |

|   |   | 2017-11-11 |
|---|---|---|
| es | 10:08:00 |   |

**RANGE OVER windows**

QL reference For a RANGE OVER window, all elements with the same timestamp are assigned to the same window. Syntax

```
SELECT
    agg1(col1) OVER(
     [PARTITION BY (value_expression1,..., value_expressionN)]
     ORDER BY timeCol
     RANGE
     BETWEEN (UNBOUNDED | timeInterval) PRECEDING AND CURRENT ROW) AS colName,
... FROM Tab1;
```

value_expression: specifies the value expression used for partitioning. timeCol: specifies the time field used to sort elements. timeInterval: specifies the time interval between the time of the current row and that of the element row to which it can be traced back. This example describes bounded RANGE OVER windows. Assume that an on-sale product table contains item IDs, item types, on-sale time, and prices. Calculate the highest price among similar products that are on sale 2 minutes earlier than the current product. Test data

| Item ID | Item type | On-sale time | Price |
|---|---|---|---|
| ITEM001 | Electronic | 2017-11-11 10:01:00 | 20 |
| ITEM002 | Electronic | 2017-11-11 10:02:00 | 50 |
| ITEM003 | Electronic | 2017-11-11 10:03:00 | 30 |
| ITEM004 | Electronic | 2017-11-11 10:03:00 | 60 |
| ITEM005 | Electronic | 2017-11-11 10:05:00 | 40 |
| ITEM006 | Electronic | 2017-11-11 10:06:00 | 20 |
| ITEM007 | Electronic | 2017-11-11 10:07:00 | 70 |
| ITEM008 | Clothes | 2017-11-11 10:08:00 | 20 |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:01:00 |   |   |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:02:00 |   |   |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:03:00 |   |   |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:03:00 |   |   |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:05:00 |   |   |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:06:00 |   |   |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:07:00 |   |   |

|   |   | 2017-11-11 |   |
|---|---|---|---|
|   | 10:08:00 |   |   |

QL reference Test statements

```
CREATE TEMPORARY TABLE tmall_item(
  itemID VARCHAR,
  itemType VARCHAR,
  eventtime varchar,
  onSellTime AS TO_TIMESTAMP(eventtime),
  price DOUBLE,
  WATERMARK FOR onSellTime AS onSellTime - INTERVAL '0' SECOND  -- Define a watermark
for the rowtime. ) WITH (
  'connector' = 'sls',
   ...
```

);

```
SELECT
    itemID,
    itemType,
    onSellTime,
    price,
    MAX(price) OVER (
        PARTITION BY itemType
        ORDER BY onSellTime
        RANGE BETWEEN INTERVAL '2' MINUTE preceding AND CURRENT ROW) AS maxPrice
FROM tmall_item;
```

Test results

| itemID | itemType | onSellTime | price | maxPrice |
|---|---|---|---|---|
| ITEM001 | Electronic | 2017-11-11 10:01:00 | 20 | 20 |
| ITEM002 | Electronic | 2017-11-11 10:02:00 | 50 | 50 |
| ITEM003 | Electronic | 2017-11-11 10:03:00 | 30 | 50 |
| ITEM004 | Electronic | 2017-11-11 10:03:00 | 60 | 60 |
| ITEM005 | Electronic | 2017-11-11 10:05:00 | 40 | 60 |
| ITEM006 | Electronic | 2017-11-11 10:06:00 | 20 | 40 |
| ITEM007 | Electronic | 2017-11-11 10:07:00 | 70 | 70 |
| ITEM008 | Clothes | 2017-11-11 10:08:00 | 20 | 20 |

|   |   | 2017-11-11 | 20 |
|---|---|---|---|
| nic | 10:01:00 |   |   |

|   |   | 2017-11-11 | 50 |
|---|---|---|---|
| nic | 10:02:00 |   |   |

|   |   | 2017-11-11 | 30 |
|---|---|---|---|
| nic | 10:03:00 |   |   |

|   |   | 2017-11-11 | 60 |
|---|---|---|---|
| nic | 10:03:00 |   |   |

|   |   | 2017-11-11 | 40 |
|---|---|---|---|
| nic | 10:05:00 |   |   |

|   |   | 2017-11-11 | 20 |
|---|---|---|---|
| nic | 10:06:00 |   |   |

|   |   | 2017-11-11 | 70 |
|---|---|---|---|
| nic | 10:07:00 |   |   |

|   |   | 2017-11-11 | 20 |
|---|---|---|---|
| s | 10:08:00 |   |   |

### 4.8 Built-in functions

QL reference

#### 4.8.1 Overview

This topic introduces the built-in functions that Realtime Compute for Apache Flink provides for data transformation. Flink V1.11: See Built-in functions in Flink V1.11. Flink V1.12: See Built-in functions in Flink V1.12.

> **Note:** Fully managed Flink VVR 3.0.0 adds some built-in functions based on Flink V1.12. For more information, see Scalar functions.
> If no built-in function meets your requirements, implement a user-defined function. For more information about user-defined functions, see Overview.

#### 4.8.2 Scalar functions

##### 4.8.2.1 BITAND

This topic describes how to use the BITAND function to perform a bitwise AND operation.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
INT BITAND(INT number1,INT number2)
```

> **Note:** The input and output parameters are both of the INT type.

**Input parameters**

| Parameter | Data type |
|---|---|
| number1 | INT |
| number2 | INT |

Test data

| a(INT) | b(INT) |
|---|---|
| 2 | 3 |

Test statements

```
SELECT BITAND(a, b) as intt FROM T1;
```

Test result

**intt(INT)**

QL reference

##### 4.8.2.2 BITNOT

This topic describes how to use the BITNOT function to perform a bitwise NOT operation.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
INT BITNOT(INT number)
```

> **Note:** The input and output parameters are both of the INT type.

**Input parameters**

| Parameter | Data type |
|---|---|
| number | INT |

Test data

**a(INT)**

Test statements

```
SELECT BITNOT(a) as var1 FROM T1;
```

Test result

**var1(INT)**

##### 4.8.2.3 BITOR

This topic describes how to use the BITOR function to perform a bitwise OR operation.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
INT BITOR(INT number1, INT number2)
```

**Input parameters**

| Parameter | Data type |
|---|---|

QL reference

| number1 | INT |
|---|---|
| number2 | INT |

> **Note:** The input and output parameters are both of the INT type.

Test data

| a(INT) | b(INT) |
|---|---|
| 2 | 3 |

Test statements

```
SELECT BITOR(a, b) as var1 FROM T1;
```

Test result

**var1(INT)**

##### 4.8.2.4 BITXOR

This topic describes how to use the BITXOR function to perform a bitwise XOR operation.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
INT BITXOR(INT number1, INT number2)
```

**Input parameters**

| Parameter | Data type |
|---|---|
| number1 | INT |
| number2 | INT |

> **Note:** The input and output parameters are both of the INT type.

Test data

| a(INT) | b(INT) |
|---|---|
| 2 | 3 |

Test statements QL reference

```
SELECT BITXOR(a, b) as var1 FROM T1;
```

Test result

**var1(INT)**

##### 4.8.2.5 CONV

This topic describes how to use the CONV function. This function performs base conversation on numeric values or characters.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.
> The **CONV()** function works with the 64-bit precision.

**Syntax**

```
VARCHAR CONV(BIGINT number, INT FROM_BASE, INT TO_BASE)
```

`or`

```
VARCHAR CONV(VARCHAR number, INT FROM_BASE, INT TO_BASE)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| number | BIGINT or VARCHAR | Note If the value of the number parameter is NULL or an invalid character, NULL is returned. |
| FROM BASE _ | INT | Valid values: [2, 36]. |
| TO BASE _ | INT | Positive valid values: [2, 36]. Negative valid values: [-36, -2]. |

Test data

| id(INT) | x(BIGINT) | y (VARCHAR) |
|---|---|---|
| 1 | 12L | '12' |
| 2 | 10L | '10' |
| 3 | 0L | 'test' |
| 4 | NULL | NULL |

Test statements QL reference

```
SELECT id, conv(x, 10, 16) as var1, conv(y, 10, 2) as var2 FROM T1;
```

Test result

| id(INT) | var1(VARCHAR) | var2(VARCHAR) |
|---|---|---|
| 1 | C | 1100 |
| 2 | A | 1010 |
| 3 | 0 | NULL |
| 4 | NULL | NULL |

##### 4.8.2.6 DATEDIFF

The topic describes how to use the DATEDIFF function. This function calculates the difference between two date values.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
INT DATEDIFF(VARCHAR enddate, VARCHAR startdate) INT DATEDIFF(TIMESTAMP enddate, VARCHAR startdate) INT DATEDIFF(VARCHAR enddate, TIMESTAMP startdate) INT DATEDIFF(TIMESTAMP enddate, TIMESTAMP startdate)
```

**Input parameters**

| Parameter | Data type |
|---|---|
| startdate | TIMESTAMP or VARCHAR |
| enddate | TIMESTAMP or VARCHAR |

> **Note:** A date of the VARCHAR type is in the **yyyy-MM-dd** or **yyyy-MM-dd HH:mm:ss** format.
> If an input parameter is NULL or a parsing error occurs, NULL is returned.

Test data

| datetime1(VARCHAR) | datetime2(VARCHAR) | nullstr(VARCHAR) |
|---|---|---|
| 2017-10-15 00:00:00 | 2017-09-15 00:00:00 | NULL |

Test statements QL reference

```
SELECT DATEDIFF(datetime1, datetime2) as int1,
        DATEDIFF(TIMESTAMP '2017-10-15 23:00:00',datetime2) as int2,
        DATEDIFF(datetime2,TIMESTAMP '2017-10-15 23:00:00') as int3,
        DATEDIFF(datetime2,nullstr) as int4,
        DATEDIFF(nullstr,TIMESTAMP '2017-10-15 23:00:00') as int5,
        DATEDIFF(nullstr,datetime2) as int6,
        DATEDIFF(TIMESTAMP '2017-10-15 23:00:00',TIMESTAMP '2017-9-15 00:00:00')as int7
FROM T1;
```

Test result

| int1(INT) | int2(INT) | int3(INT) | int4(INT) | int5(INT) | int6(INT) | int7(INT) |
|---|---|---|---|---|---|---|
| 30 | 30 | -30 | NULL | NULL | NULL | 30 |

##### 4.8.2.7 DATE_ADD

This topic describes how to use the DATE_ADD function. This function returns the date after the specified number of days is added to a date.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
VARCHAR DATE_ADD(VARCHAR startdate, INT days) VARCHAR DATE_ADD(TIMESTAMP time, INT days)
```

**Input parameters**

| Parameter | Data type |
|---|---|
| startdate | TIMESTAMP or VARCHAR Note A date of the VARCHAR type is in the yyyy-MM-dd or yyyy-MM-dd HH:mm:ss format. |
| time | TIMESTAMP |
| days | INT |

> **Note:** If an input parameter is NULL or a parsing error occurs, NULL is returned.

Test data

| datetime1(VATCHAR) | nullstr(VATCHAR) |
|---|---|
| 2017-09-15 00:00:00 | null |

Test statements QL reference

```
SELECT DATE_ADD(datetime1, 30) as var1,
 DATE_ADD(TIMESTAMP '2017-09-15 23:00:00',30) as var2,
 DATE_ADD(nullstr,30) as var3
FROM T1;
```

Test result

| var1(VARCHAR) | var2(VARCHAR) | var3(VARCHAR) |
|---|---|---|
| 2017-10-15 | 2017-10-15 | null |

##### 4.8.2.8 DATE_FORMAT

This topic describes how to use the DATE_FORMAT function. This function converts a date value of the STRING type from a format into a specific format.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
VARCHAR DATE_FORMAT(TIMESTAMP time, VARCHAR to_format) VARCHAR DATE_FORMAT(VARCHAR date, VARCHAR to_format) VARCHAR DATE_FORMAT(VARCHAR date, VARCHAR from_format, VARCHAR to_format)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| time | TIMESTAMP | The source string. |
| date | VARCHAR | The source string. The default format is yyyy-MM- dd HH:mm:ss. |
| from format _ | VARCHAR | The original format. This parameter is optional. The default format is yyyy-MM-dd hh:mm:ss. |
| to format _ | VARCHAR | The format of the output date. |

> **Note:** If an input parameter is NULL or a parsing error occurs, NULL is returned.

Test data

| date1(VARCHAR) | datetime1(VARCHAR) | nullstr(VARCHAR) |
|---|---|---|
| 0915-2017 | 2017-09-15 00:00:00 | NULL |

Test statements QL reference

```
SELECT DATE_FORMAT(datetime1, 'yyMMdd') as var1,
 DATE_FORMAT(nullstr, 'yyMMdd') as var2,
 DATE_FORMAT(datetime1, nullstr) as var3,
 DATE_FORMAT(date1, 'MMdd-yyyy', nullstr) as var4,
 DATE_FORMAT(date1, 'MMdd-yyyy', 'yyyyMMdd') as var5,
 DATE_FORMAT(TIMESTAMP '2017-09-15 23:00:00', 'yyMMdd') as var6
FROM T1;
```

Test result

| var1(VARCH AR) | var2(VARCH AR) | var3(VARCH AR) | var4(VARCH AR) | var5(VARCH AR) | var6(VARCH AR) |
|---|---|---|---|---|---|
| 170915 | null | null | null | 20170915 | 170915 |

##### 4.8.2.9 DATE_FORMAT_TZ

This topic describes how to use the DATE_FORMAT_TZ function. This function converts data of the timestamp type into a string of the specified type based on the specified time zone.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
VARCHAR DATE_FORMAT_TZ(TIMESTAMP timestamp, VARCHAR format, VARCHAR timezone) VARCHAR DATE_FORMAT_TZ(TIMESTAMP timestamp, VARCHAR timezone)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| timestamp | TIMESTAMP | The data type of time. |
| format | VARCHAR | The format of the output date, for example, yyyy- MM-dd HH:mm:ss. |
| timezone | VARCHAR | The time zone, for example, Asia/Shanghai. |

Test data

| timestamp1(TIMESTAMP) | format1(VARCHAR) | timezone1(VARCHAR) |
|---|---|---|
| 0 | yyyy-MM-dd HH:mm:ss | Asia/Shanghai |

Test statements

```
SELECT
   DATE_FORMAT_TZ(timestamp1, format1, timezone1) as var1,
   DATE_FORMAT_TZ(timestamp1, timezone1) as var2
FROM T1;
```

Test result

| var1(VARCHAR) | var2(VARCHAR) |
|---|---|

QL reference

| 1970-01-01 08:00:00 | 1970-01-01 08:00:00 |
|---|---|

##### 4.8.2.10 DATE_SUB

The topic describes how to use the DATE_SUB function. This function subtracts specific days from a date and then returns the obtained date.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
VARCHAR DATE_SUB(VARCHAR startdate, INT days) VARCHAR DATE_SUB(TIMESTAMP time, INT days)
```

**Input parameters**

| Parameter | Data type |
|---|---|
| startdate | VARCHAR Note A date of the VARCHAR type is in the yyyy-MM-dd or yyyy-MM-dd HH:mm:ss format. |
| time | TIMESTAMP |
| days | INT |

> **Note:** If one of the input parameters is NULL or a parsing error occurs, the return value is NULL.

Test data

| date1(VARCHAR) | nullstr(VARCHAR) |
|---|---|
| 2017-10-15 | NULL |

Test statements

```
SELECT DATE_SUB(date1, 30) as var1,
 DATE_SUB(TIMESTAMP '2017-10-15 23:00:00',30) as var2,
 DATE_SUB(nullstr,30) as var3
FROM T1;
```

Test result

| var1(VARCHAR) | var2(VARCHAR) | var3(VARCHAR) |
|---|---|---|
| 2017-09-15 | 2017-09-15 | NULL |

##### 4.8.2.11 FROM_UNIXTIME

QL reference This topic describes how to use the FROM_UNIXTIME function. This function returns a date of the VARCHAR type.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
VARCHAR FROM_UNIXTIME(BIGINT unixtime, VARCHAR format)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| unixtime | BIGINT | The timestamp. Unit: seconds. |
| format | VARCHAR | The format of logs. This parameter is optional. The default format is yyyy-MM-dd HH:mm:ss. |

> **Note:** If an input parameter is NULL or a parsing error occurs, NULL is returned.

Test data

| unixtime1(BIGINT) | nullstr(VARCHAR) |
|---|---|
| 1505404800 | NULL |

Test statements

```
SELECT FROM_UNIXTIME(unixtime1) as var1,
 FROM_UNIXTIME(unixtime1,'MMdd-yyyy') as var2,
 FROM_UNIXTIME(unixtime1,nullstr) as var3
FROM T1;
```

Test result

| var1(VARCHAR) | var2(VARCHAR) | var3(VARCHAR) |
|---|---|---|
| 2017-09-15 00:00:00 | 0915-2017 | NULL |

##### 4.8.2.12 ISNAN

This topic describes how to use the ISNAN function. This function checks whether the specified floating-point number is NAN (Not a number). This function is similar to the Double.isNan() or Float.isNan() function in Java.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
BOOLEAN ISNAN(DOUBLE d) BOOLEAN ISNAN(FLOAT f)
```

QL reference

**Input parameters**

| Parameter | Data type |
|---|---|
| d | DOUBLE |
| f | FLOAT |

Test dataTable 1. T1

| d | f |
|---|---|
| 0.1 | 0.1 |
| 0 | 0 |

Test statements

```
SELECT ISNAN(CAST(d AS DOUBLE)) as d1, ISNAN(CAST(f AS FLOAT)) as d2 FROM T1;
```

Test result

| d1(BOOLEAN) | d2(BOOLEAN) |
|---|---|
| false | false |
| false | false |

##### 4.8.2.13 JSON_VALUE

This topic describes how to use the JSON_VALUE function. This function extracts the expression of the specified path from a JSON string.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
VARCHAR JSON_VALUE(VARCHAR content, VARCHAR path)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| content | VARCHAR | The JSON object that you want to parse. |

QL reference

| path | VARCHAR | The expression of the specified path. You must use single quotation marks (') in a custom path. Example: JSON VALUE(json,'$.passenger name') AS _ _ ABC The following symbols are supported in a path: $: indicates the root object. []: indicates the array subscript. *: indicates the array wildcard characters. .: indicates child elements. |
|---|---|---|

> **Note:** If the input parameters contain invalid JSON or NULL values, NULL is returned.

Test data Table 1. T1

| id(INT) | json(VARCHAR) | path1(VARCHAR) |
|---|---|---|
| 1 | [10, 20, [30, 40]] | $[2][*] |
| 2 | {"aaa":"bbb","ccc": {"ddd":"eee","fff":"ggg","hhh": ["h0","h1","h2"]},"iii":"jjj"} | $.ccc.hhh[*] |
| 3 | {"aaa":"bbb","ccc": {"ddd":"eee","fff":"ggg",hhh": ["h0","h1","h2"]},"iii":"jjj"} | $.ccc.hhh[1] |
| 4 | [10, 20, [30, 40]] | NULL |
| 5 | NULL | $[2][*] |
| 6 | "{xx]" | "$[2][*]" |

Test statements

```
SELECT
    id,
    JSON_VALUE(json, path1) AS `value`
FROM
    T1;
```

Test result

| id (INT) | value (VARCHAR) |
|---|---|
| 1 | [30,40] |
| 2 | ["h0","h1","h2"] |
| 3 | H1 |
| 4 | NULL |
| 5 | NULL |

QL reference

| 6 | NULL |
|---|---|

##### 4.8.2.14 KEYVALUE

This topic describes how to use the KEYVALUE function. This function splits a string into key-value pairs based on the split1 delimiter, and splits the key-value pairs based on the split2 delimiter. The value that corresponds to the key is returned.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
VARCHAR KEYVALUE(VARCHAR str, VARCHAR split1, VARCHAR split2, VARCHAR key_name)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| str | VARCHAR | The string that you want to split. |
| split1 | VARCHAR | The split1 delimiter that splits the specified string into key-value pairs. |
| split2 | VARCHAR | The split2 delimiter that splits the key-value pairs. |
| key name _ | VARCHAR | The name of the key. |

> **Note:** If the split1 or split2 parameter is NULL, NULL is returned.
> If the str or key_name parameter is NULL, NULL is returned.
> If no key is found, NULL is returned.
> If multiple key-value pairs exist, the value that first matches the key is returned.

Test dataTable 1. T1

| str(VARCHAR) | split1(VARCHAR) | split2(VARCHAR) | key1(VARCHAR) |
|---|---|---|---|
| k1=v1;k2=v2 | ; | = | k2 |
| NULL | ; | \| | : |
| k1:v1\|k2:v2 | NULL | = | : |
| k1:v1\|k2:v2 | \| | = | NULL |
| k1:v1\|k2:v2 | \| | = | : |

Test statements

```
SELECT KEYVALUE(str, split1, split2, key1) as `result` FROM T1;
```

QL reference Test result

**result(VARCHAR)**

v2 NULL NULL NULL NULL

##### 4.8.2.15 MURMUR_HASH

The topic describes how to use the MURMUR_HASH function. This function specifies the 32-bit hash value for a parameter by using the hash32x86 method.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
INT MURMUR_HASH(value)
```

**Input parameters**

| Parameter | Data type |
|---|---|
| value | VARCHAR or a numeric value |

**Example 1**

Test dataTable 1. T1

**value**

This is a test String. NULL test Test statements

```
SELECT MURMUR_HASH(value) as intt FROM T1;
```

Test result

**intt(VARCHAR)**

740959099 NULL 271330425 QL reference

**Example 2**

Test dataTable 2. T2

**str**

### 4.5 Subscription

NULL Test statements

```
SELECT MURMUR_HASH(CAST(str AS FLOAT)) as intt FROM T2;
```

Test result

**intt(VARCHAR)**

-2130121231 NULL 1863595885

##### 4.8.2.16 MURMUR_HASH_64

The topic describes how to use the MURMUR_HASH_64 function. This function specifies the 64-bit hash value for a parameter by using the hash128x64 method.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
BIGINT MURMUR_HASH_64(value)
```

**Input parameters**

| Parameter | Data type |
|---|---|
| value | VARCHAR or a numeric value |

**Example 1**

Test dataTable 1. T1

**value**

This is a test String. NULL test Test statements QL reference

```
SELECT MURMUR_HASH_64(value) as big FROM T1;
```

Test result

**big(VARCHAR)**

2706826604463634835 NULL 5010266691562018262

**Example 2**

Test dataTable 2. T2

**value**

### 4.5 Subscription

NULL Test statements

```
SELECT MURMUR_HASH_64(CAST(value AS FLOAT)) as big FROM T2;
```

Test result

**big(VARCHAR)**

8033179276572534397 NULL -6697622088025985219

##### 4.8.2.17 PARSE_URL

The topic describes how to use the PARSE_URL function. This function parses a specific part of a URL and returns the obtained value.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
VARCHAR PARSE_URL(VARCHAR urlStr, VARCHAR partToExtract [, VARCHAR key])
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|

QL reference

| urlStr | VARCHAR | The URL that you want to parse. Note If the value of urlStr is NULL, NULL is returned. |
|---|---|---|
| partToExtract | VARCHAR | The part that you want to parse from the URL. Valid values: HOST PATH QUERY REF PROTOCOL FILE AUTHORITY USERINFO |
| key | VARCHAR | The name of the key whose value you want to extract. This parameter is optional. |

Test data

| url1(VARCHAR) | nullstr(VARCHAR) |
|---|---|
| http://facebook.com/path/p1.php?query=1 | NULL |

Test statements

```
SELECT PARSE_URL(url1, 'QUERY', 'query') as var1,
       PARSE_URL(url1, 'QUERY') as var2,
       PARSE_URL(url1, 'HOST') as var3,
       PARSE_URL(url1, 'PATH') as var4,
       PARSE_URL(url1, 'REF') as var5,
       PARSE_URL(url1, 'PROTOCOL') as var6,
       PARSE_URL(url1, 'FILE') as var7,
       PARSE_URL(url1, 'AUTHORITY') as var8,
       PARSE_URL(nullstr, 'QUERY') as var9,
       PARSE_URL(url1, 'USERINFO') as var10,
       PARSE_URL(nullstr, 'QUERY', 'query') as var11
FROM T1;
```

Test result

| var1( VARC HAR) | var2( VARC HAR) | var3( VARC HAR) | var4( VARC HAR) | var5( VARC HAR) | var6( VARC HAR) | var7( VARC HAR) | var8( VARC HAR) | var9( VARC HAR) | var1 0(VA RCH AR) | var1 1(VA RCH AR) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | query =1 | faceb ook.c om | /path/ p1.ph p | NULL | http | /path/ p1.ph p? query =1 | faceb ook.c om | NULL | NULL | NULL |

QL reference

##### 4.8.2.18 REGEXP

This topic describes how to use the REGEXP function. This function searches a specified string by using a regular expression and returns a Boolean value based on the matching result.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
BOOLEAN REGEXP(VARCHAR str, VARCHAR pattern)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| str | VARCHAR | The specified string. |
| pattern | VARCHAR | The specified pattern. |

> **Note:** If the string or pattern parameter is empty or NULL, false is returned.

Test dataTable 1. T1

| str1(VARCHAR) | pattern1(VARCHAR) |
|---|---|
| k1=v1;k2=v2 | k2* |
| k1:v1\|k2:v2 | k3 |
| NULL | k3 |
| k1:v1\|k2:v2 | NULL |
| k1:v1\|k2:v2 | ( |

Test statements

```
SELECT REGEXP(str1, pattern1) AS result FROM T1;
```

Test result

**result(BOOLEAN)**

true false false false false QL reference

##### 4.8.2.19 REGEXP_REPLACE

This topic describes how to use the REGEXP_REPLACE function. This function replaces the specified string with the desired string and returns a new string.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
VARCHAR REGEXP_REPLACE(VARCHAR str, VARCHAR pattern, VARCHAR replacement)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| str | VARCHAR | The specified string. |
| pattern | VARCHAR | The original string that you want to replace. |
| replacement | VARCHAR | The string that is used to replace the original string. |

> **Important:** If an input parameter is NULL or the regular expression is invalid, NULL is returned.
> The system parses the pattern and replacement parameters into regular expressions. The regular expressions are processed by using Java Pattern. Therefore, the pattern and replacement parameters must follow the syntax for Java Regex.

Test data Table 1. T1

| str1(VARCHAR) | pattern1(VARCHAR) | replace1(VARCHAR) |
|---|---|---|
| 2014-03-13 | - | " |
| " | - | " |
| 2014-03-13 | '' | s |
| 2014-03-13 | ( | s |
| 100-200 | (\d+) | num |

Test statements

```
SELECT REGEXP_REPLACE(str1, pattern1, replace1) as result FROM T1;
```

Test result

**result(VARCHAR)**

20140313 Empty string QL reference s2s0s1s4s-s0s3s-s1s3s null num-num

##### 4.8.2.20 SPLIT_INDEX

This topic describes how to use the SPLIT_INDEX function. This function splits a string into several segments based on the specified delimiter and returns the field at the specified position.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
VARCHAR SPLIT_INDEX(VARCHAR str, VARCHAR sep, INT index)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| str | VARCHAR | The string that you want to split. |
| sep | VARCHAR | The delimiter. |
| index | INT | The field position. The index starts from 0. Note If no field is obtained, NULL is returned. |

> **Note:** If an input parameter is set to NULL, NULL is returned.

Test dataTable 1. T1

| str(VARCHAR) | sep(VARCHAR) | index(INT) |
|---|---|---|
| Jack,John,Mary | , | 2 |
| Jack,John,Mary | , | 3 |
| Jack,John,Mary | NULL | 0 |
| NULL | , | 0 |

Test statements

```
SELECT SPLIT_INDEX(str, sep, index) as var1 FROM T1;
```

Test result

**var1(VARCHAR)**

QL reference Mary NULL NULL NULL

##### 4.8.2.21 TO_DATE

The topic describes how to use the TO_DATE function. This function converts a date value from the INT or VARCHAR type to the DATE type.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
Date TO_DATE(INT time) Date TO_DATE(VARCHAR date) Date TO_DATE(VARCHAR date,VARCHAR format)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| time | INT | The number of days that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| date | VARCHAR | The default format is yyyy-MM-dd. |
| format | VARCHAR | The date format. |

Test dataTable 1. T1

| date1(INT) | date2(VARCHAR) | date3(VARCHAR) |
|---|---|---|
| 100 | 2017-09-15 | 20170915 |

Test statements

```
SELECT TO_DATE(date1) as var1,
 TO_DATE(date2) as var2,
 TO_DATE(date3,'yyyyMMdd') as var3
FROM T1;
```

Test result

| var1(DATE) | var2(DATE) | var3(DATE) |
|---|---|---|
| 1970-04-11 | 2017-09-15 | 2017-09-15 |

##### 4.8.2.22 TO_TIMESTAMP_TZ

QL reference This topic describes how to use the TO_TIMESTAMP_TZ function. This function converts a date value of the VARCHAR type into the TIMESTAMP type based on the specified time zone.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
TIMESTAMP TO_TIMESTAMP_TZ(VARCHAR date, VARCHAR timezone) TIMESTAMP TO_TIMESTAMP_TZ(VARCHAR date, VARCHAR format, VARCHAR timezone)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| timezone | VARCHAR | The time zone, for example, Asia/Shanghai. |
| date | VARCHAR | The default format is yyyy-MM-dd HH:mm:ss. |
| format | VARCHAR | The date format. |

Test dataTable 1. T1

| timestamp1(VARCHAR) | format1(VARCHAR) | timezone1(VARCHAR) |
|---|---|---|
| 1970-01-01 00:00:00 | yyyy-MM-dd HH:mm:ss | Asia/Shanghai |

Test statements

```
SELECT
     UNIX_TIMESTAMP(TO_TIMESTAMP_TZ(timestamp1, timezone1)) as var1,
     UNIX_TIMESTAMP(TO_TIMESTAMP_TZ(timestamp1, format1, timezone1)) as var2
FROM T1;
```

Test result

| var1(BIGINT) | var2(BIGINT) |
|---|---|
| -28800 | -28800 |

##### 4.8.2.23 UNIX_TIMESTAMP

This topic describes how to use the UNIX_TIMESTAMP function. This function converts a date value into a UNIX timestamp.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
BIGINT UNIX_TIMESTAMP(VARCHAR date) BIGINT UNIX_TIMESTAMP(TIMESTAMP timestamp) BIGINT UNIX_TIMESTAMP(VARCHAR date, VARCHAR format)
```

**Input parameters**

QL reference

| Parameter | Data type | Description |
|---|---|---|
| timestamp | TIMESTAMP | N/A. |
| date | VARCHAR | The default date format is yyyy-MM-dd HH:mm:ss . |
| format | VARCHAR | The default date format is yyyy-MM-dd hh:mm:ss . |

|   | HH:mm:ss |
|---|---|

|   | hh:mm:ss |
|---|---|

Test data Table 1. T1

| date1(VARCHAR) | date2(VARCHAR) |
|---|---|
| 2021-03-25 00:00:00 | 1970-01-01 00:00:00 |

Test statements

```
SELECT UNIX_TIMESTAMP(to_timestamp_tz(date1)) as big1,
       UNIX_TIMESTAMP(date2) as big2
FROM T1;
```

Test result

| big1(BIGINT) | big2 (BIGINT) |
|---|---|
| 1616601600 | -28800 |

#### 4.8.3 Table-valued functions

##### 4.8.3.1 GENERATE_SERIES

This topic describes how to use the GENERATE_SERIES function. This function generates a series of padding data based on the rule of from, from+1, from+2 ... to-1.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
GENERATE_SERIES(INT from, INT to)
```

**Input parameters**

| Parameter | Data type |
|---|---|
| from | The lower boundary of a series of values (including the lower boundary). This parameter is of the INT type. |
| to | The upper boundary of a series of values (excluding the upper boundary). This parameter is of the INT type. |

QL reference Test data Table 1. T1

| s(INT) | e(INT) |
|---|---|
| 1 | 3 |
| -2 | 1 |

Test statements

```
SELECT s, e, v FROM T1, lateral table(GENERATE_SERIES(s, e)) as v;
```

Test result

| s(INT) | e(INT) | v(INT) |
|---|---|---|
| 1 | 3 | 1 |
| 1 | 3 | 2 |
| -2 | 1 | -2 |
| -2 | 1 | -1 |
| -2 | 1 | 0 |

##### 4.8.3.2 JSON_TUPLE

This topic describes how to use the JSON_TUPLE function. This function retrieves the values that are represented by each path string from a JSON string.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
JSON_TUPLE(str, path1, path2 ..., pathN)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| str | VARCHAR | The JSON string. |
| path1 to pathN | VARCHAR | A path string, which does not start with a dollar sign ( $ ). |

Test data Table 1. T1

| d(VARCHAR) | s(VARCHAR) |
|---|---|
| {"qwe":"asd","qwe2":"asd2","qwe3":"asd3"} | qwe3 |

QL reference

| {"qwe":"asd4","qwe2":"asd5","qwe3":"asd3"} | qwe2 |
|---|---|

Test statements

```
SELECT d, v FROM T1, lateral table(JSON_TUPLE(d, 'qwe', s)) AS T(v);
```

Test result

| d(VARCHAR) | v(VARCHAR) |
|---|---|
| {"qwe":"asd","qwe2":"asd2","qwe3":"asd3"} | asd |
| {"qwe":"asd","qwe2":"asd2","qwe3":"asd3"} | asd3 |
| {"qwe":"asd4","qwe2":"asd5","qwe3":"asd3"} | asd4 |
| {"qwe":"asd4","qwe2":"asd5","qwe3":"asd3"} | asd5 |

##### 4.8.3.3 MULTI_KEYVALUE

This topic describes how to use the MULTI_KEYVALUE function. This function splits a string into key-value pairs based on the key-value pair delimiter specified by split1, splits a key-value pair based on the delimiter specified by split2, and returns the values of key_name1 and key_name2.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
MULTI_KEYVALUE(VARCHAR str, VARCHAR split1, VARCHAR split2, VARCHAR key_name1, VARCHAR key_n ame2, ...)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| str | VARCHAR | The string that you want to split. |
| split1 | VARCHAR | The key-value pair delimiter. If the value of split1 is NULL, spaces are used as key-value pair delimiters. If the length of split1 is greater than 1, split1 represents only a set of delimiters, in which each character represents a valid delimiter. |
| split2 | VARCHAR | The key-value delimiter. If the value of split2 is NULL, spaces are used as key-value delimiters. If the length of split2 is greater than 1, split2 represents only a set of delimiters, in which each character represents a valid delimiter. |
| key name1, _ key name2, ... _ | VARCHAR | The list of keys whose values you want to obtain. |

QL reference Test data Table 1. T1

| str(VARCHAR) | split1(VARCHAR ) | split2(VARCHAR ) | key1(VARCHAR) | key2(VARCHAR) |
|---|---|---|---|---|
| k1=v1;k2=v2 | ; | = | k1 | k2 |
| NULL | ; | = | k1 | k2 |
| k1:v1;k2:v2 | ; | : | k1 | k3 |
| k1:v1;k2:v2 | ; | = | k1 | k2 |
| k1:v1;k2:v2 | , | : | k1 | k2 |
| k1:v1;k2=v2 | ; | : | k1 | k2 |
| k1:v1abck2:v2 | abc | : | k1 | k2 |
| k1:v1;k2=v2 | ; | := | k1 | k2 |
| k1:v1 k2:v2 | NULL | : | k1 | k2 |
| k1 v1;k2 v2 | ; | NULL | k1 | k2 |

Test statements

```
SELECT c1, c2 FROM T1, lateral table(MULTI_KEYVALUE(str, split1, split2, key1, key2)) as T(c1, c2);
```

Test result

| c1(VARCHAR) | c2(VARCHAR) |
|---|---|
| v1 | v2 |
| NULL | NULL |
| v1 | NULL |
| NULL | NULL |
| NULL | NULL |
| v1 | NULL |
| v1 | v2 |
| v1 | v2 |
| v1 | v2 |
| v1 | v2 |

##### 4.8.3.4 STRING_SPLIT

This topic describes how to use the STRING_SPLIT function. This function splits a string into substrings based on the specified delimiter and returns a list of substrings. QL reference

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
string_split(string, separator)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| string | VARCHAR | The string that you want to split. |
| separator | VARCHAR | The delimiter. Note The delimiter must be a single string. |

> **Note:** If the value of a string is NULL, an empty row is returned.
> If the string contains two or more consecutive delimiters, an empty substring that does not contain characters is returned.
> If the string does not contain the specified delimiter, the whole string that you want to split is returned.

Test data Table 1. T1

| d(varchar) | s(varchar) |
|---|---|
| abc-bcd | - |
| hhh | - |

Test statements

```
SELECT d,v FROM T1, lateral table(string_split(d, s)) as T(v);
```

Test result

| d(varchar) | v(varchar) |
|---|---|
| abc-bcd | abc |
| abc-bcd | bcd |
| hhh | hhh |

#### 4.8.4 Aggregate functions

##### 4.8.4.1 APPROX_COUNT_DISTINCT

QL reference This topic describes how to use the APPROX_COUNT_DISTINCT function to improve the performance of your jobs.

> **Important:** This topic applies only to Ververica Platform (VVP) 2.4.0, Ververica Runtime (VVR) 3.0.0, and later.

**Background information**

When you optimize the COUNT DISTINCT function, distinct key information must be saved in the state data of the aggregate node. If a large number of distinct keys exist, the read/write overhead of state data is high. This situation causes a bottleneck in job performance optimization. In many cases, accurate computation is not necessary. If you want to achieve high job performance at the expense of a small portion of accuracy, you can use the **APPROX_COUNT_DISTINCT** function.
**APPROX_COUNT_DISTINCT** supports miniBatch and local-global optimization on the aggregate
node. When you use this function, make sure that the following requirements are met: The input data does not contain retract messages. A large number of distinct keys, such as unique visitors (UVs), exist. The
**APPROX_COUNT_DISTINCT** function cannot bring obvious benefits if only a small number of
distinct keys exist.

**Syntax**

```
APPROX_COUNT_DISTINCT(col [, accuracy])
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| col | All data types | The name of the field. |
| accuracy | FLOAT | The computation accuracy. This parameter is optional. A larger value indicates a higher accuracy, which leads to a higher state overhead. A higher state overhead weakens the performance of the APPROX COUNT DISTINCT function. Valid values: _ _ (0.0, 1.0). Default value: 0.99. |

Test dataTable 1. T1

| a (VARCHAR) | c (BIGINT) |
|---|---|
| Hi | 1 |
| Hi | 2 |
| Hi | 3 |
| Hi | 4 |
| Hi | 5 |
| Hi | 6 |

Test statement QL reference

```
SELECT
```

`a,`

```
  APPROX_COUNT_DISTINCT(b) as b,
  APPROX_COUNT_DISTINCT(b, 0.9) as c
FROM T1 GROUP BY a;
```

Test result

| a (VARCHAR) | b (BIGINT) | c (BIGINT) |
|---|---|---|
| Hi | 6 | 6 |

##### 4.8.4.2 FIRST_VALUE

This topic describes how to use the FIRST_VALUE function. This function returns the first non-null record of a data stream.

> **Important:** This topic applies only to Ververica Platform (VVP) 2.4.0, Ververica Runtime (VVR) 3.0.0, and later.

**Syntax**

```
FIRST_VALUE( T value ) FIRST_VALUE( T value, BIGINT order )
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| value | Any data type | A data stream. Note If all input data is NULL, NULL is returned. |
| order | BIGINT | The non-null record that has the smallest order value is considered the first non-null record. |

> **Important:** All input parameters must be of the same data type.

Test data Table 1. T1

| a(BIGINT) | b(INT) | c(VARCHAR) |
|---|---|---|
| 1 | 1 | Hello |
| 2 | 2 | Hello |
| 3 | 3 | Hello |
| 4 | 4 | Hello |
| 5 | 5 | Hello |

QL reference

| 6 | 6 | Hello |
|---|---|---|
| 7 | 7 | NULL |
| 8 | 7 | Hello World |
| 9 | 8 | Hello World |
| 10 | 20 | Hello World |

Test statement

```
SELECT c,FIRST_VALUE(b) OVER (PARTITION BY c ORDER BY PROCTIME() RANGE UNBOUNDED PRECEDING) AS var1 FROM T1;
```

Test results

| c(VARCHAR) | var1(INT) |
|---|---|
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| NULL | 7 |
| Hello World | 7 |
| Hello World | 7 |
| Hello World | 7 |

##### 4.8.4.3 LAST_VALUE

This topic describes how to use the LAST_VALUE function. This function returns the last non-null record of a data stream.

> **Important:** This topic applies only to Ververica Platform (VVP) 2.4.0, Ververica Runtime (VVR) 3.0.0, and later.

**Syntax**

```
T LAST_VALUE(T value) T LAST_VALUE(T value, BIGINT order)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|

QL reference

| value | Any data type | A data stream. |
|---|---|---|
| order | BIGINT | The non-null record that has the largest order value is considered the last non-null record. |

> **Important:** All input parameters must be of the same data type.

Test data Table 1. T1

| a(BIGINT) | b(INT) | c(VARCHAR) |
|---|---|---|
| 1 | 1 | Hello |
| 2 | 2 | Hello |
| 3 | 3 | Hello |
| 4 | 4 | Hello |
| 5 | 5 | Hello |
| 6 | 6 | Hello |
| 7 | 7 | NULL |
| 8 | 7 | Hello World |
| 9 | 8 | Hello World |
| 10 | 20 | Hello World |

Test statement

```
SELECT c,LAST_VALUE(b) OVER (PARTITION BY c ORDER BY PROCTIME() RANGE UNBOUNDED PRECEDING) AS var1 FROM T1;
```

Test results

| c(VARCHAR) | var1(INT) |
|---|---|
| Hello | 1 |
| Hello | 2 |
| Hello | 3 |
| Hello | 4 |
| Hello | 5 |
| Hello | 6 |
| NULL | 7 |
| Hello World | 7 |

QL reference

| Hello World | 8 |
|---|---|
| Hello World | 20 |

### 4.9 User-defined functions (JAR)

#### 4.9.1 Overview

This topic describes notes, classification, definition, and parameter-passing methods for developing Flink user-defined functions.

**Notes**

To avoid conflicts between JAR package dependencies, note the following guidelines when developing user-defined functions: Ensure that the Flink version you select on the draft development page matches the Flink version specified in your Pom dependencies. Set the scope of all Flink-related dependencies to provided, that is, add `<scope>provided</scope>` to each relevant dependency. Package all other third-party dependencies using the Shade method. For details about Shade packaging, see Apache Maven Shade Plugin.

**User-defined function classification**

Flink supports the following three types of user-defined functions.

| Classification | Description |
|---|---|
| UDF (user-defined scalar function) | A user-defined scalar function maps zero, one, or multiple scalar values to a new scalar value. The input and output have a one-to-one relationship, meaning the function reads one row of data and produces one output value. For more information, see User-defined scalar function (UDF). |
| UDAF (user-defined aggregation function) | A user-defined aggregation function aggregates multiple records into a single record. The input and output have a one- to-one relationship, meaning the function aggregates multiple input records into one output value. For more information, see User-defined aggregate function (UDAF). |
| UDTF (user-defined table-valued function) | A user-defined table-valued function accepts zero, one, or multiple scalar values as input parameters (which can be variable-length). Similar to custom-defined scalar functions but different in output, a table-valued function can return any number of rows, not just a single value. Each returned row may consist of one or more columns. A single function call can produce multiple rows or columns of data. For more information, see User-defined table-valued function (UDTF). |

**Pass parameters to user-defined functions**

If you need to modify certain parameter value in your user-defined function later, directly editing the UDF code becomes cumbersome. In this case, configure the parameter in the **Additional**
**Dependencies** configuration item of the fully managed Flink console, then reference it within
your UDF code. You can subsequently update the parameter value directly in the Flink console for rapid adjustments. QL reference User-defined functions provide an optional open(FunctionContext context) method. The FunctionContext object supports parameter passing, enabling the passing of custom configuration items through it. Follow these steps to pass parameters to user-defined functions:
1. Add the parameter and its value in **Additional Dependencies** of the **Configuration** panel on
the right side of the draft development page. Sample code:

```
maxJobCreationAttempts: value
```

2. Retrieve the user-defined function parameter in your UDF code using ConfigOptions.key().
Sample code:

```
String strValue = context.getJobParameter("key","default_value"); Integer intValue = Integer.parseInt(context.getJobParameter("key","default_value"));
```

If the function parameter is in key-value format, you must use the FunctionContext#getJobParameter method to obtain the value of the pipeline.global-jobparameters configuration item. When defining key-value pairs in pipeline.global-job-parameters, separate keys and values with a colon (:), and separate different key-value pairs with commas (,). If a key or value contains a colon or comma, enclose it with double quotation marks ("). If a key or value also contains double quotation marks, escape them by doubling the character (""). Sample code:

```
pipeline.global-job-parameters: 'json1:"{k1:""value1""}",json2:"k2"'
```

This configuration defines the following map.

| Key | Value |
|---|---|
| json1 | {k1:""value1""} |
| json2 | k2 |

You can now retrieve each item in the map using FunctionContext#getJobParameter.

```
context.getJobParameter("json1", null); // Returns the string {k1:""value1""} context.getJobParameter("json2", null); // Returns the string k2
```

**Register a user-defined function**

User-defined functions are categorized as global or job-level. Registration methods are described below: Global user-defined functions i. Log on to the Realtime Compute for Apache Flink console. ii. In the left-side navigation pane, click **SQL Editor**. iii. On the **UDFs** tab, click the icon. QL reference iv. Upload the user-defined function JAR file. You can upload the user-defined function JAR file using either of the following methods:
**Upload a file**: Click **Click to select** next to **Select a file**, then choose your target user-
defined function JAR file. If dependencies exist, click **Click to select** next to **Dependencies** and select the files your user-defined function JAR depends on.
**External URL**: Enter the external URL address.

> **Note:** Your user-defined function JAR file is uploaded to the sql-artifacts directory in the OSS bucket you selected. Additionally, the Realtime Compute for Apache Flink development console parses the JAR file to detect classes implementing Flink UDF, UDAF, and UDTF interfaces, then automatically extracts class names and populates the Function Name field.
> For Java-based UDFs, dependencies can be packaged into the user-defined function JAR package or uploaded separately via the dependencies option.
> When the user-defined function file or its dependencies are large, we recommend uploading via an external URL. Note that if the external URL points to an OSS bucket, dependency files must reside in the sql-artifacts/namespaces/{namespace} directory.

v. Click **Confirm**. On the **SQL Editor** page, you can view all successfully registered UDFs in the **UDFs** list on the left. Job-level user-defined functions Global user-defined functions (catalog functions) default to parsing with the latest Flink version during registration. If you use a global user-defined function in a deployment while selecting a non-latest Flink version in advanced configuration, compatibility issues may arise. To resolve this, you may implement your UDF code according to the engine version required by your deployment and register it as a job-level user-defined function. Follow this process: i. Upload the user-defined function JAR package. In the left-side navigation pane, click **Artifacts** > **Upload Artifact** and upload the userdefined function JAR package. ii. Specify the job-level user-defined function in your deployment. In the **Additional Dependencies** configuration item of your deployment, specify the userdefined function JAR package. iii. Register the user-defined function. QL reference Use the `CREATE TEMPORARY FUNCTION` syntax to register a job-level user-defined function.

```
CREATE TEMPORARY FUNCTION MyScalarFunc AS 'com.test.MyScalarFunc';
```

#### 4.9.2 User-defined scalar function (UDF)

This topic describes how to develop, register, and use user-defined scalar functions (UDFs) in Flink. A user-defined scalar function (UDF) maps zero, one, or multiple scalar values to a new scalar value. The input and output have a one-to-one relationship, meaning the function reads one row of data and writes one output value.

**Develop a UDF**

> **Note:** Flink provides Python UDX examples to help you quickly develop UDXs. These examples include implementations of Python UDFs, Python user-defined aggregate functions (UDAFs), and Python user-defined table-valued functions (UDTFs). They come with a pre-configured development environment for the corresponding version, so you do not need to set up the environment yourself.

1. Download and decompress the ASI_UDX_Demo example to your local machine.
After decompression, the system generates the **ASI_UDX-main** folder, containing the following items:
**pom.xml**: This is the project-level configuration file that primarily describes the Maven
coordinates, dependencies, rules that developers must follow, defect management systems, organizations, licenses, and other project-related factors.
**\ASI_UDX-main\src\main\java\ASI_UDF\ASI_UDF.java**: This is the Java code for the UDF
example.
2. In IntelliJ IDEA, click **File > Open** to open the decompressed **ASI_UDX-main** folder.
3. Double-click to open \ASI_UDX-main\src\main\java\ASI_UDF, then configure **ASI_UDF.java** as
needed. In this sample code, **ASI_UDF.java** already contains the code that retrieves characters from position begin to end in each row of data.

```java
package ASI_UDF; import org.apache.flink.table.functions.ScalarFunction; public class ASI_UDF extends ScalarFunction {
    public String eval(String s, Integer begin, Integer end) {
        return s.substring(begin, end);
```

`}` `}`
4. Double-click to open \ASI_UDX-main\, then configure **pom.xml**.
In this sample code, the **pom.xml** file already includes dependency information for the main JAR packages of Flink 1.11. If your business: Does not depend on other JAR packages: You do not need to configure the **pom.xml** file. Proceed with the next step. QL reference Depends on other JAR packages: Add the required JAR package dependency information to the
**pom.xml** file.
The main JAR package dependencies for Flink 1.11 are as follows.

```xml
<dependencies>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-java_2.12</artifactId>
            <version>1.11.0</version>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table</artifactId>
            <version>1.11.0</version>
            <type>pom</type>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-core</artifactId>
            <version>1.11.0</version>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table-common</artifactId>
            <version>1.11.0</version>
        </dependency>
    </dependencies>
```

5. Run the following command in the directory where **pom.xml** resides to package the files.

```
mvn package -Dcheckstyle.skip
```

A JAR package named **ASI_UDX-1.0-SNAPSHOT.jar** appears in the \ASI_UDX-main\target\ directory, indicating that you have completed UDF development.

**Register a UDF**

For the UDF registration process, see the Managing UDFs section in Alibaba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide.

**Use a UDF**

After registering a UDF, you can use it to perform the following steps:
1. Develop a Flink SQL draft. For more information, see the Develop a SQL draft section in Alibaba
Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide. Retrieve characters from position 2 to 4 in field a of each row in the ASI_UDF_Source table. The sample code is as follows. QL reference

```
CREATE TEMPORARY TABLE ASI_UDF_Source (
  a VARCHAR,
  b INT,
  c INT
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE ASI_UDF_Sink (
  a VARCHAR
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO ASI_UDF_Sink SELECT ASI_UDF('a',2,4) FROM ASI_UDF_Source;
```

2. On the **Dewployments** page, click **Start** in the **Actions** column corresponding to the target
deployment. After starting the deployment, each row in the ASI_UDF_Sink table receives characters from position 2 to 4 in field a of each row in the ASI_UDF_Source table.

#### 4.9.3 User-defined aggregate function (UDAF)

This topic describes how to develop, register, and use user-defined aggregate functions (UDAFs) in Flink. A user-defined aggregate function (UDAF) aggregates multiple records into one record. The input and output have a one-to-one relationship, meaning the function aggregates multiple input records into one output value.

**Develop a UDAF**

> **Note:** Flink provides Python UDX examples to help you quickly develop UDXs. These examples include implementations of Python UDFs, Python user-defined aggregate functions (UDAFs), and Python user-defined table-valued functions (UDTFs). They come with a pre-configured development environment for the corresponding version, so you do not need to set up the environment yourself.

1. Download and decompress the ASI_UDX_Demo example to your local machine.
After decompression, the system generates the **ASI_UDX-main** folder, containing the following items:
**pom.xml**: This is the project-level configuration file that primarily describes Maven
coordinates, dependencies, rules that developers must follow, defect management systems, organizations, licenses, and all other project-related factors.
**\ASI_UDX-main\src\main\java\ASI_UDAF\ASI_UDAF.java**: This is the Java code for the
UDAF example.
2. In IntelliJ IDEA, click **file > open** to open the decompressed **ASI_UDX-main**.
3. Double-click to open \ASI_UDX-main\src\main\java\ASI_UDAF, then configure **ASI_UDAF.java** as
needed. QL reference In this sample code, **ASI_UDAF.java** already contains the code that sums current and historical data. For instance, if the first data point is 1, the second is 2, and the third is 3, then the first result is 1, the second is 3, and the third is 6.

```java
package ASI_UDAF; import org.apache.flink.table.functions.AggregateFunction; public class ASI_UDAF{
    public static class AcSum {
        public long sum;
```

`}`

```java
    public static class WeightedSum extends AggregateFunction<Long, AcSum> {
        @Override
        public Long getValue(AcSum acSum) {
            return acSum.sum;
```

`}`

```java
        @Override
        public AcSum createAccumulator() {
            AcSum acCount = new AcSum();
            acCount.sum = 0;
            return acCount;
```

`}`

```
        public void accumulate(AcSum acc, long acSum) {
            acc.sum += acSum;
```

`}` `}` `}`
4. Double-click to open \ASI_UDX-main\, then configure **pom.xml**.
In this sample code, the **pom.xml** file already includes dependency information for the main JAR packages of Flink 1.11. If your business: Does not depend on other JAR packages: You do not need to configure the **pom.xml** file. Proceed with the next step. Depends on other JAR packages: Add the required JAR package dependency information to the
**pom.xml** file.
The main JAR package dependencies for Flink 1.11 are as follows. QL reference

```xml
<dependencies>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-java_2.12</artifactId>
            <version>1.11.0</version>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table</artifactId>
            <version>1.11.0</version>
            <type>pom</type>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-core</artifactId>
            <version>1.11.0</version>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table-common</artifactId>
            <version>1.11.0</version>
        </dependency>
    </dependencies>
```

5. Run the following command in the directory where **pom.xml** resides to package the files.

```
mvn package -Dcheckstyle.skip
```

A JAR package named **ASI_UDX-1.0-SNAPSHOT.jar** appears in the \ASI_UDX-main\target\ directory, indicating that you have completed UDAF development.

**Register a UDAF**

For the UDAF registration process, see the Managing UDFs section in Alibaba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide.

**Use a UDAF**

After registering a UDAF, you can use it to perform the following steps.
1. Develop a Flink SQL draft. For more information, see the Develop a SQL draft section in Alibaba
Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide. Obtain the sum of the current and historical data in field "a" of the ASI_UDAF_Source table. The sample code is as follows. QL reference

```
CREATE TEMPORARY TABLE ASI_UDAF_Source (
  a   BIGINT
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE ASI_UDAF_Sink (
  sum  BIGINT
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO ASI_UDAF_Sink SELECT `ASI_UDAF$WeightedSum`(a) FROM ASI_UDAF_Source;
```

2. On the **Deployments** page, click **Start** in the **Actions** column for the target deployment.
After starting the deployment, each row in the ASI_UDAF_Sink table receives the sum of the current and historical data in field "a" of the ASI_UDAF_Source table.

#### 4.9.4 User-defined table-valued function (UDTF)

**(UDTF)**

This topic describes how to develop, register, and use user-defined table-valued functions (UDTFs) in Flink. A user-defined table-valued function (UDTF) accepts zero, one, or multiple scalar values as input parameters (which can be variable-length). Similar to custom-defined scalar functions but different in output, a table-valued function can return any number of rows, not just a single value. Each returned row may consist of one or more columns. A single function call can produce multiple rows or columns of data.

**Develop a UDTF**

> **Note:** Flink provides Python UDX examples to help you quickly develop UDXs. These examples include implementations of Python UDFs, Python user-defined aggregate functions (UDAFs), and Python user-defined table-valued functions (UDTFs). They come with a pre-configured development environment for the corresponding version, so you do not need to set up the environment yourself.

1. Download and decompress the ASI_UDX_Demo example to your local machine.
After decompression, the system generates the **ASI_UDX-main** folder, containing the following items:
**pom.xml**: This is the project-level configuration file that primarily describes the Maven
coordinates, dependencies, rules that developers must follow, defect management systems, organizations, licenses, and all other project-related factors.
**\ASI_UDX-main\src\main\java\ASI_UDF\ASI_UDTF.java**: This is the Java code for the UDTF
example.
2. In IntelliJ IDEA, click **file > open** to open the decompressed **ASI_UDX-main**.
3. Double-click to open \ASI_UDX-main\src\main\java\ASI_UDTF, then modify **ASI_UDTF.java** file as
needed. QL reference In this sample code, the **ASI_UDTF.java** already contains the code that splits a single string into multiple columns by using a pipe character (|).

```java
package ASI_UDTF; import org.apache.flink.api.java.tuple.Tuple2; import org.apache.flink.table.functions.TableFunction; public class ASI_UDTF extends TableFunction<Tuple2<String,String>> {
    public void eval(String str){
        String[] split = str.split("\\|");
        String name = split[0];
        String place = split[1];
        Tuple2<String,String> tuple2 = Tuple2.of(name,place);
        collect(tuple2);
```

`}` `}`
4. Double-click to open \ASI_UDX-main\, then configure **pom.xml**.
In this sample code, the **pom.xml** file already includes dependency information for the main JAR packages of Flink 1.11. If your business: Does not depend on other JAR packages: You do not need to configure the **pom.xml** file. Proceed with the next step. Depends on other JAR packages: Add the required JAR package dependency information to the
**pom.xml** file.
The main JAR package dependencies for Flink 1.11 are as follows.

```xml
<dependencies>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-java_2.12</artifactId>
            <version>1.11.0</version>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table</artifactId>
            <version>1.11.0</version>
            <type>pom</type>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-core</artifactId>
            <version>1.11.0</version>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table-common</artifactId>
            <version>1.11.0</version>
        </dependency>
    </dependencies>
```

5. Run the following command in the directory where **pom.xml** resides to package the file.

```
mvn package -Dcheckstyle.skip
```

QL reference The JAR package named **ASI_UDX-1.0-SNAPSHOT.jar** appears in the \ASI_UDX-main\target\ directory, indicating that you have completed the UDTF development.

**Register a UDTF**

For the UDTF registration process, see the Managing UDFs section in Alibaba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide.

**Use a UDTF**

After registering a UDTF, you can use it to perform the following steps:
1. Develop a Flink SQL draft. For more information, see the Develop a SQL draft section in Alibaba
Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide. Split each string in the message field of the ASI_UDTF_Source table into multiple columns by using a pipe character (|). The sample code is as follows:

```
CREATE TEMPORARY TABLE ASI_UDTF_Source (
  `message`  VARCHAR
) WITH (
  'connector'='datagen'
```

);

```
CREATE TEMPORARY TABLE ASI_UDTF_Sink (
  name  VARCHAR,
  place  VARCHAR
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO ASI_UDTF_Sink SELECT name,place FROM ASI_UDTF_Source,lateral table(ASI_UDTF(`message`)) as T(name,place);
```

2. On the **Deployments** page, click **Start** in the **Actions** column corresponding to the target
deployment. After starting the deployment, the ASI_UDTF_Sink table receives data from the message field of the ASI_UDTF_Source table, which is split into multiple columns by using a pipe character (|).

### 4.10 User-defined functions (Python)

**(Python)**

#### 4.10.1 Overview

Flink supports using Python user-defined functions in SQL deployments. This topic describes the classification, definition, and dependencies of Flink user-defined functions (UDX), and explains how to debug and tune them.

**UDX classification**

Flink supports the following three types of user-defined functions.

| UDX type | Description |
|---|---|

QL reference

| UDF (user-defined scalar function) | A user-defined scalar function maps zero, one, or multiple scalar values to a new scalar value. The input and output have a one-to- one relationship, meaning the function reads one row of data and produces one output value. For more information, see User-defined scalar function (UDF). |
|---|---|
| UDAF (user-defined aggregation function) | A user-defined aggregation function aggregates multiple records into one record. The input and output have a many-to-one relationship, meaning the function aggregates multiple input records into one output value. For more information, see User- defined aggregate function (UDAF). |
| UDTF (user-defined table-valued function) | A user-defined table-valued function takes zero, one, or multiple scalar values as input parameters (which can be variable-length). Similar to custom-defined scalar functions but different in output, a table-valued function can return any number of rows, not just a single value. Each returned row can consist of one or more columns. A single function call can produce multiple rows or columns of data. For more information, see User-defined table-valued function (UDTF). |

**Dependency**

The Flink cluster pre-installs common Python packages such as Pandas, NumPy, and PyArrow. You can view the list of third-party Python packages installed in the Flink cluster on the **Develop a**
**draft** section in Alibaba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation
Edition) Developer Guide. In addition, you can also use other types of third-party Python packages in Python user-defined functions. Note that if you use non-preinstalled third-party Python packages, you must upload them as dependency files when registering the Python UDF. For more information, see **Manage**
**UDFs** and **Use Python dependencies** in Alibaba Cloud Realtime Compute for Apache Flink
(Compute-Storage Separation Edition) User Guide.

**Debugging**

You can output log information by using Logging in the code implementation of Python userdefined functions to facilitate issue diagnosis. The following example shows how to do this.

```python
@udf(result_type=DataTypes.BIGINT()) def add(i, j):
  logging.info("hello world")
  return i + j
```

After generating logs, you can view them in the TaskManager log files.

**Tuning**

Use the Pandas library In addition to standard Python user-defined functions, Flink also supports Pandas user-defined functions. For Pandas user-defined functions, the types of input data are data structures defined in Pandas, such as pandas.Series and pandas.DataFrame. You can use high-performance Python libraries like Pandas and NumPy within Pandas user-defined functions to develop highperformance user-defined functions. For more information, see Vectorized User-defined Functions. Configure the following parameters QL reference The performance of Python user-defined functions depends largely on their implementation. If you encounter performance issues, optimize the implementation of the Python user-defined functions as much as possible. In addition, the performance of Python user-defined functions is also affected by the values of the following parameters.

| Parameter | Description |
|---|---|
| python.fn-execution.bundle.size | Python UDF computation is asynchronous. During execution, Java operators asynchronously send data to the Python process for processing. Before sending data to the Python process, Java operators cache the data and send it only after reaching a certain threshold. The python.fn-execution.bundle.size parameter controls the maximum number of data records that can be cached. The default value is 100,000, measured in number of records. |
| python.fn-execution.bundle.time | This parameter controls the maximum caching time for data. Computation of cached data triggers when either the number of cached records reaches the threshold defined by python.fn- execution.bundle.size or the caching time reaches the threshold defined by python.fn-execution.bundle.time. The default value is 1,000, measured in milliseconds. |
| python.fn- execution.arrow.batch.size | When you use Pandas UDFs, this parameter defines the maximum number of data records that a single Arrow batch can hold. The default value is 10,000. Note The value of python.fn-execution.arrow.batch.size cannot exceed that of python.fn-execution.bundle.size. |

> **Note:** Larger values for these three parameters are not always better. If you set these parameters too high, checkpoint operations may need to process excessive amount of data, leading to prolonged checkpoint durations or even checkpoint failures. For more details about these parameters, see Configuration.

#### 4.10.2 User-defined scalar function (UDF)

This topic describes the limits, development, registration, and usage of Python user-defined scalar functions (UDFs). A user-defined scalar function (UDF) maps zero, one, or multiple scalar values to a new scalar value. The input and output have a one-to-one relationship, meaning the function reads one row of data and writes one output value.

**Limits**

Realtime Compute for Apache Flink is subject to deployment environments and network environments. Therefore, when you develop Python UDFs, note the following limits: Only open-source Flink V1.12 and later are supported. The Flink cluster pre-installs Python 3.7.9. Therefore, you must develop code in Python 3.7.9. QL reference Flink runs in JDK 1.8. If your Python deployment depends on third-party JAR packages, make sure that the JAR packages are compatible with JDK 1.8. Only open-source Scala V2.11 is supported. If your Python deployment depends on third-party JAR packages, make sure that you use JAR package dependencies corresponding to Scala V2.11.

**Develop a UDF**

> **Note:** Flink provides Python UDX examples to help you quickly develop UDXs. These examples include implementations of Python UDFs, Python user-defined aggregate functions (UDAFs), and Python user-defined table-valued functions (UDTFs). This topic uses Windows as an example to describe how to develop a UDF.

1. Download and decompress the python_demo-master example to your computer.
2. In PyCharm, click **file > open** to open the decompressed **python_demo-master**.
3. Double-click to open \python_demo-master\udx\udfs.py. Then, modify **udfs.py** as needed.
In sample code, **sub_string** defines the code for obtaining characters from position begin to end in each piece of data.

```python
from pyflink.table import DataTypes from pyflink.table.udf import udf @udf(result_type=DataTypes.STRING()) def sub_string(s: str, begin: int, end: int):
    return s[begin:end]
```

4. Run the following command in the directory where udx resides (that is, the \python_demo-
master directory) to package files.

```
zip -r python_demo.zip udx
```

A ZIP package named **python_demo.zip** appears in the \python_demo-master\ directory, indicating that you have completed the development of the Python UDF.

**Register a UDF**

For the UDF registration process, see the Managing UDFs section in Alibaba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide.

**Use a UDF**

After registering a UDF, you can use the UDF to perform the following steps:
1. Develop a Flink SQL draft. For more information, see the Develop a SQL draft section in Alibaba
Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide. Obtain characters from position 2 to 4 in field a of each row in the ASI_UDF_Source table. Sample code: QL reference

```
CREATE TEMPORARY TABLE ASI_UDF_Source (
  a VARCHAR,
  b INT,
  c INT
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE ASI_UDF_Sink (
  a VARCHAR
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO ASI_UDF_Sink SELECT ASI_UDF(a,2,4) FROM ASI_UDF_Source;
```

2. On the **Deployments** page, click **Start** in the **Actions** column corresponding to the deployment
that you want to manage. After starting the deployment, each row in the ASI_UDF_Sink table receives characters from position 2 to 4 in field a of each row in the ASI_UDF_Source table.

#### 4.10.3 User-defined aggregate function (UDAF)

This topic describes the limits, development, registration, and usage of Python user-defined aggregate functions (UDAFs). A user-defined aggregate function (UDAF) aggregates multiple records into one record. The input and output have a many-to-one relationship, meaning the function aggregates multiple input records into one output value.

**Limits**

Realtime Compute for Apache Flink is subject to deployment environments and network environments. Therefore, when you develop Python UDFs, note the following limits: Only open-source Flink V1.12 and later are supported. The Flink cluster pre-installs Python 3.7.9. Therefore, you must develop code in Python 3.7.9. Flink runs in JDK 1.8. If your Python deployment depends on third-party JAR packages, make sure that the JAR packages are compatible with JDK 1.8. Only open-source Scala V2.11 is supported. If your Python deployment depends on third-party JAR packages, make sure that you use JAR package dependencies corresponding to Scala V2.11.

**Develop a UDAF**

> **Note:** Flink provides Python UDX examples to help you quickly develop UDXs. These examples include implementations of Python ser-defined scalar functions (UDFs), Python UDAFs, and Python user-defined table-valued functions (UDTFs). This topic uses Windows as an example to describe how to develop a UDAF.

1. Download and decompress the python_demo-master example to your computer.
2. In PyCharm, click **file > open** to open the decompressed **python_demo-master**.
QL reference
3. Double-click and open \python_demo-master\udx\udafs.py, then configure **udafs.py** as needed.
In this sample code, **weighted_avg** defines the code that calculates the weighted average of current and historical data.

```python
from pyflink.common import Row from pyflink.table import AggregateFunction, DataTypes from pyflink.table.udf import udaf class WeightedAvg(AggregateFunction):
    def create_accumulator(self):
        # Row(sum, count)
        return Row(0, 0)
    def get_value(self, accumulator: Row) -> float:
        if accumulator[1] == 0:
            return 0
        else:
            return accumulator[0] / accumulator[1]
    def accumulate(self, accumulator: Row, value, weight):
        accumulator[0] += value * weight
        accumulator[1] += weight
    def retract(self, accumulator: Row, value, weight):
        accumulator[0] -= value * weight
        accumulator[1] -= weight
weighted_avg = udaf(f=WeightedAvg(),
                    result_type=DataTypes.DOUBLE(),
                    accumulator_type=DataTypes.ROW([
                        DataTypes.FIELD("f0", DataTypes.BIGINT()),
                        DataTypes.FIELD("f1", DataTypes.BIGINT())]))
```

4. Run the following command in the directory where udx resides (that is, the \python_demo-
master directory) to package the files.

```
zip -r python_demo.zip udx
```

A ZIP package named **python_demo.zip** appears in the \python_demo-master\ directory, indicating that you have completed the development of the Python UDAF.

**Register a UDAF**

For the UDFA registration process, see the Managing UDFs section in Alibaba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide.

**Use a UDAF**

After registering a UDAF, you can use the UDAF to perform the following steps:
1. Develop a Flink SQL draft. For more information, see the Develop a SQL draft section in Alibaba
Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide. The following sample code obtains the weighted average of the current and historical data in field a of the ASI_UDAF_Source table, using field b as the weight. QL reference

```
CREATE TEMPORARY TABLE ASI_UDAF_Source (
  a   BIGINT,
  b   BIGINT
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE ASI_UDAF_Sink (
  avg_value  DOUBLE
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO ASI_UDAF_Sink SELECT weighted_avg(a, b) FROM ASI_UDAF_Source;
```

2. On the **Deployments** page, click **Start** in the **Actions** column corresponding to the target
deployment. After starting the deployment, each row in the ASI_UDAF_Sink table receives the weighted average of the current and historical data in field a of the ASI_UDAF_Source table, using field b as the weight.

#### 4.10.4 User-defined table-valued function (UDTF)

**(UDTF)**

This topic describes the limits, development, registration, and usage of Python user-defined tablevalued functions (UDTFs). A user-defined table-valued function (UDTF) accepts zero, one, or multiple scalar values as input parameters (which can be variable-length parameters). A table-valued function can return any number of rows as output, not just a single value. Each returned row can consist of one or more columns. One function call can produce multiple rows or columns of data. UDTFs are similar to user-defined scalar functions but differ in their output structure.

**Limits**

Realtime Compute for Apache Flink is subject to deployment environments and network environments. Therefore, when you develop Python UDFs, note the following limits: Only open-source Flink V1.12 and later are supported. The Flink cluster pre-installs Python 3.7.9. Therefore, you must develop code in Python 3.7.9. Flink runs in JDK 1.8. If your Python deployment depends on third-party JAR packages, make sure that the JAR packages are compatible with JDK 1.8. Only open-source Scala V2.11 is supported. If your Python deployment depends on third-party JAR packages, make sure that you use JAR package dependencies corresponding to Scala V2.11.

**Develop a UDTF**

QL reference

> **Note:** Flink provides Python UDX examples to help you quickly develop UDXs. These examples include implementations of Python ser-defined scalar functions (UDFs), Python user-defined aggregate functions (UDAFs), and Python UDTFs. This topic uses Windows as an example to describe how to develop a UDTF.

1. Download and decompress the python_demo-master example to your computer.
2. In PyCharm, click **file > open** to open the decompressed **python_demo-master**.
3. Double-click and open \python_demo-master\udx\udtfs.py, then modify the content of the
**udtfs.py** file as needed.
In this sample code, **split** defines code that splits a single string into multiple columns by using a pipe character (|) as the delimiter.

```python
from pyflink.table import DataTypes from pyflink.table.udf import udtf @udtf(result_types=[DataTypes.STRING(), DataTypes.STRING()]) def split(s: str):
    splits = s.split("|")
    yield splits[0], splits[1]
```

4. Run the following command in the directory where udx resides (that is, the \python_demo
directory) to package the files.

```
zip -r python_demo.zip udx
```

A ZIP package named **python_demo.zip** appears in the \python_demo\ directory, indicating that you have completed the development of the Python UDTF.

**Register a UDTF**

For the UDTF registration process, see the Managing UDFs section in Alibaba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide.

**Use a UDTF**

After registering a UDTF, you can use it to perform the following steps:
1. Develop a Flink SQL draft. For more information, see the Develop a SQL draft section in Alibaba
Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide. The message field of each row in the ASI_UDTF_Source table is concatenated with the string "aa" with a pipe character (|), and then split into multiple column using a pipe character (|). The sample code is as follows: QL reference

```
CREATE TEMPORARY TABLE ASI_UDTF_Source (
  `message`  VARCHAR
) WITH (
  'connector'='datagen'
```

);

```
CREATE TEMPORARY TABLE ASI_UDTF_Sink (
  name  VARCHAR,
  place  VARCHAR
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO ASI_UDTF_Sink SELECT name,place FROM ASI_UDTF_Source,lateral table(split(concat_ws('|', `message`, 'aa'))) as T(name,place
```

);
2. On the **Deployments** page, click **Start** in the **Actions** column corresponding to the target
deployment. After starting the deployment, the ASI_UDTF_Sink table receives two columns of data. These two columns are generated by splitting the concatenation of the message field in the ASI_UDTF_Source table and the "aa" field using a pipe character (|).

### 4.11 Machine learning functions

#### 4.11.1 CLUSTER_SERVING

This topic describes how to use the machine learning function CLUSTER_SERVING to implement online inference. The Tensorflow SavedMode model with the format of input_shape=(?,128) is used in this topic.

**Limits**

This topic applies only to Ververica Platform (VVP) 2.4.2 and later.

**Background information**

Analytics Zoo is an open source big data analytics and artificial intelligence (AI) platform developed by Intel®. Analytics Zoo supports machine learning training and inference of the distributed TensorFlow and PyTorch models. It improves the performance of deep learning workloads by using the Intel® OpenVINO tool suite and Deep Learning Boost instruction set. Cluster Serving is a distributed inference solution of Analytics Zoo. It can be deployed on Apache Flink clusters for distributed computing. Cluster Serving can implement end-to-end distributed machine learning inference without having to manually write machine learning code. For more information about Analytics Zoo, see Analytics Zoo. Cluster Serving integrates some of its features into the built-in functions of Flink and supports various inference models, such as TensorFlow, PyTorch, and OpenVINO. You can directly call the CLUSTER_SERVING function in the console of fully managed Flink to perform distributed machine learning inference. When you use the CLUSTER_SERVING function, you need only to provide model files and data files to complete the end-to-end application of machine learning.

**Syntax**

```
CLUSTER_SERVING(uri, `data`)
```

**Input parameters**

QL reference

| Parameter | Data type | Description |
|---|---|---|
| uri | String | The data ID. |
| data | String | The returned data. |

Test dataTable 1. input.csv

| uri(String) | data(String) |
|---|---|
| my-data | 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 |

Test procedure i. Log on to the Object Storage Service (OSS) console and upload the test data file input.csv to the oss://***/ directory. ii. Log on to the console of fully managed Flink. Create a source table and a result table, load the specified model, and then insert the online inference data of the CLUSTER_SERVING function into the result table.

```
CREATE TEMPORARY TABLE ClusterServingInput(
   uri STRING,
  `data` STRING
) WITH (
   'connector' = 'filesystem',
   'path' = 'oss://alink-vvp/artifacts/namespaces/test-module-default/input.csv',
   'format' = 'csv'
```

);

```
CREATE TEMPORARY TABLE ClusterServingOutput (
   uri1 STRING,
   data1 STRING
 ) WITH (
   'connector' = 'print'
```

);

```
LOAD MODULE `cluster-serving`; INSERT INTO ClusterServingOutput SELECT cluster_serving(uri, `data`) FROM ClusterServing Input;
```

iii. Add the following configuration to the **Additional Configuration** section on the **Advanced** tab of the job and to the **Additional Configuration** section on the Create Session Cluster page, and then click **Save**.

```
pipeline.global-job-parameters: '"modelPath:""[Directory of your model file]"""'
```

modelPath indicates the OSS directory in which your model file is stored, such as oss://***/tf_auto/. iv. On the Deployments page, find the required job and click **Start** in the **Actions** column. Test results QL reference

| uri1 | data1 |
|---|---|
| 0.03932024,0.017788976,-2.2538425E- 4,0.021853039,0.030905273,0.052324444,0.053021688,0.08776946 ,0.0625467,0.12149326,0.048770625,0.04533424,0.09271586,0.023 119276,0.0037812046,0.052707616,0.029312208,0.023519568,0.07 501668,0.037939064,0.06363185,0.04994791,0.08504477,0.069405 96,0.052632406,0.028651983,0.02205597,0.05861686,0.040175162 ,0.04682718,0.05283319,0.01967535,0.111778766,0.03182444,0.04 509241,0.09942829,0.009491239,0.038903005,0.11488753,0.01950 3327,0.0346709,0.060727723,0.03718308,0.1295206,0.04292037,0. 13272661,0.009957914,0.050370887,0.03016096,0.067269124,0.09 981682,0.08606887,0.085193545,0.041775055,0.02956512,0.02714 2545,0.09836763,0.029330501,0.040107135,0.0753366,0.06851786 4,0.020111244,0.086271614,0.04449262,0.107297346,0.07932708, 0.036529146,0.014892701,0.08245985,0.04272034,0.076421194,0. 035283472,0.028554386,0.019374546,0.048012834,0.011391987,0. 028220229,0.054405782,0.037807927,0.085761145,0.07974813,0.0 4150249,- 0.017132144,0.08219319,0.019887058,0.034193676,0.06221051,0. 07516215,0.0598385,0.09159884,0.038117558,0.05329266,0.02103 8251,0.072046585,0.05561088,0.017538168,0.025691401,0.085806 02,0.02225845,0.117060736,0.060743354,0.11840888,0.065381594 ,0.08059649,0.045638822,0.06399781,0.011646094,0.043574452,0. 123603456,0.045708194,0.05672055,0.08402837,0.118181005,0.09 657015,0.08259893,0.0010145458,0.031954847,0.07388758,0.0353 80267,0.070080444,0.06764534,0.058731187,0.022044828,0.09435 9346,0.05559277,0.032255664,0.07360537,0.11992536 | 128 |
