---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Realtime Compute Realtime Compute for Apache Flink (Compute-Storage Separation Edition) Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 452
source_pdf: "2f8dc42d491d41ce_Alibaba Cloud Apsara Stack v3.18.6-2607 Realtime Compute Realtime Compute for Apache Flink (Compute-"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%AE%9E%E6%97%B6%E8%AE%A1%E7%AE%97Flink%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Realtime%20Compute%20Realtime%20Compute%20for%20Apache%20Flink%20%28Compute-Storage%20Separation%20Edition%29%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Realtime Compute Realtime Compute for Apache Flink (Compute-Storage Separation Edition) Developer Guide 20260828

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
    - 3.1.1 API version differences and usage guidelines for Flink (Compute-Storage Separation Edition)
    - 3.1.2 Compute-storage separation v1
      - 3.1.2.1 ValidateSqlScript
      - 3.1.2.2 UploadArtifactByOSSUrl
      - 3.1.2.3 UpdateUdfArtifact
      - 3.1.2.4 UpdateMember
      - 3.1.2.5 UpdateFormat
      - 3.1.2.6 UpdateDeploymentDesiredState
      - 3.1.2.7 UpdateDeployment
      - 3.1.2.8 UpdateConnector
      - 3.1.2.9 TableExists
      - 3.1.2.10 SetDeploymentResourceMode
      - 3.1.2.11 ParseFormat
      - 3.1.2.12 ParseConnector
      - 3.1.2.13 ListTables
      - 3.1.2.14 ListSessionClusters
      - 3.1.2.15 ListSecretValues
      - 3.1.2.16 ListSavepoints
      - 3.1.2.17 ListNamespaces
      - 3.1.2.18 ListFunctions
      - 3.1.2.19 ListFormats
      - 3.1.2.20 ListFlinkVersions
      - 3.1.2.21 ListDeploymentTargets
      - 3.1.2.22 ListDeployments
      - 3.1.2.23 ListDatabases
      - 3.1.2.24 ListConnectors
      - 3.1.2.25 ListCatalogs
      - 3.1.2.26 ListArtifacts
      - 3.1.2.27 GetUdfArtifact
      - 3.1.2.28 GetTable
      - 3.1.2.29 GetResourcePlan
      - 3.1.2.30 GetGlobalDeploymentDefaults
      - 3.1.2.31 GetFunction
      - 3.1.2.32 GetDeploymentDefaults
      - 3.1.2.33 GetDeployment
      - 3.1.2.34 GetDefaultDatabase
      - 3.1.2.35 GetDatabase
      - 3.1.2.36 GetCatalog
      - 3.1.2.37 GetArtifactMetadata
      - 3.1.2.38 GenerateResourcePlan
      - 3.1.2.39 FunctionExists
      - 3.1.2.40 ForcefullyCreateLock
      - 3.1.2.41 ExecuteSqlscriptsStatements
      - 3.1.2.42 ExecuteSqlScript
      - 3.1.2.43 DeployDeploymentDraft
      - 3.1.2.44 DeleteUdfArtifact
      - 3.1.2.45 DeleteSecretValue
      - 3.1.2.46 DeleteMember
      - 3.1.2.47 DeleteFormat
      - 3.1.2.48 DeleteFolder
      - 3.1.2.49 DeleteDeployment
      - 3.1.2.50 DeleteConnector
      - 3.1.2.51 DeleteArtifact
      - 3.1.2.52 DatabaseExists
      - 3.1.2.53 CreateUdfArtifact
      - 3.1.2.54 CreateSecretValue
      - 3.1.2.55 CreateSavepoint
      - 3.1.2.56 CreateMember
      - 3.1.2.57 CreateFormat
      - 3.1.2.58 CreateDeployment
      - 3.1.2.59 CreateConnector
      - 3.1.2.60 CreateFolder
      - 3.1.2.61 ListJobs
      - 3.1.2.62 ReplaceDeployment
    - 3.1.3 Compute-storage separation v2
      - 3.1.3.1 ValidateSqlStatement
      - 3.1.3.2 UpdateMember
      - 3.1.3.3 UpdateDeployment
      - 3.1.3.4 StopJob
      - 3.1.3.5 StartJobWithParams
      - 3.1.3.6 StartJob
      - 3.1.3.7 ListSavepoints
      - 3.1.3.8 ListJobs
      - 3.1.3.9 ListEngineVersionMetadata
      - 3.1.3.10 ListDeploymentTargets
      - 3.1.3.11 GetSavepoint
      - 3.1.3.12 GetMember
      - 3.1.3.13 GetLatestJobStartLog
      - 3.1.3.14 GetJob
      - 3.1.3.15 GetGenerateResourcePlanResult
      - 3.1.3.16 GetDeployment
      - 3.1.3.17 GenerateResourcePlanWithFlinkConfAsync
      - 3.1.3.18 DeleteVariable
      - 3.1.3.19 DeleteSavepoint
      - 3.1.3.20 DeleteMember
      - 3.1.3.21 DeleteJob
      - 3.1.3.22 DeleteDeployment
      - 3.1.3.23 CreateVariable
      - 3.1.3.24 CreateSavepoint
      - 3.1.3.25 CreateMember
      - 3.1.3.26 CreateDeployment
      - 3.1.3.27 FlinkApiProxy
      - 3.1.3.28 ListDeployments
      - 3.1.3.29 ListMembers
      - 3.1.3.30 ListVariables
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
7. Select the corresponding API operation and obtain the POP endpoint information of the
cloud service under the parameter name. tions

**Obtain an endpoint by using Apsara Infrastructure**

**Management**

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

When calling an API, you must provide multiple header parameters such as the region ID, organization ID, resource set ID, and instance ID. This topic describes how to obtain these parameters and explains some return values after API calls tions

**Obtain a region ID**

1. Log in to the Apsara Uni-manager Management Console as an administrator.
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
button, select **Platform** > **Apsara Uni-manager**, and set **Version** to 2024- 09-12.
5. Enter `GetOrganizationList` in the search box for online debugging. Enter the name of the
target organization in the name parameter and initiate the call. After the call succeeds, view the information about **id** in **Call Result**. The value of id is the organization ID. For more information about the API operation, see the GetOrganizationList section in Apsara Un i-manager Management Console Developer Guide.

**Obtain a resource set ID**

You must call an API operation to obtain a resource set ID. You can use the online debugging feature in the Apsara Uni-manager Management Console to quickly obtain the resource set ID.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, select **Products** > **Development Tools** > **OpenAPI Explorer**.
3. On the **OpenAPI Explorer** page, select **API Integration** > **API Debugging**.
4. Click the
button, select **Platform** > **Apsara Uni-manager**, and set **Version** to 2024- 09-12.
5. Enter `ListResourceGroup` in the search box for online debugging. After the call succeeds,
view the information about **id** in **Call Result**. The value of id is the resource set ID. For more information about the API operation, see the ListResourceGroup section in Apsara Uni- Manager Management Console Developer Guide.

**Obtain an instance ID**

You can obtain an instance ID from the cloud service instance list in the Apsara Uni-manager Management Console. The following steps use API Gateway as an example:
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Products** > **Development Tools** > **API Gateway**.
3. In the left-side navigation pane, click **Instances**.
4. In the instance list, view the **instance ID**.
tions

**Response parameters**

After you call a List API operation related to cloud service resource instances, the system returns the following parameters by default.

| Name | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

### 1.3 Obtain an AccessKey pair

AccessKey pairs are classified into AccessKey pairs assigned by Resource Access Management (RAM) and those assigned by Security Token Service (STS). You can use either type of AccessKey pair for authentication when you call operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. You can use RAM or STS to assign an AccessKey pair for authentication. Use RAM to assign an AccessKey ID and an AccessKey secret to a third party. Use STS to assign an AccessKey ID, an AccessKey secret, and a security token to a third party. For more information, see Obtain an AccessKey pair assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only operations administrators and the administrators of level-1 organizations can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

> **Warning:** The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |

tions

| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
|---|---|
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

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

tions This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

STS allows you to manage temporary access credentials for your Apsara Stack resources. You can use STS to call API operations.

**Procedure**

1. Obtain the Apsara Stack Resource Name (ARN) of your `Resource Access Management (RAM)`
`role` . i. Log on to the Apsara Uni-manager Management Console. ii. In the upper-right corner of the homepage, click the profile picture and then click **User**
**Information**.
iii. On the page that appears, click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view the ARN of your `RAM role` .

|   | stsAK |
|---|---|
| RAM role |   |

2. Use the following code to obtain an AccessKey ID ( `stsAK` ), AccessKey secret ( `stsSK` ),
and STS token ( `stsToken` ) by assuming the `RAM role` . tions

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
3. Use the access credentials assigned by STS to call an API operation of a cloud service. In
this example, the Elastic Compute Service (ECS) API is used. tions

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
        asClient.setSdkSource("test");
  // Call an API operation of ECS.
        String ecsRes = DescribeZones(asClient,<stsAK>,<stsSK>,<stsToken>);
```

`}`

```
public static String DescribeZones(ASClient asClient, String stsAK, String stsSK, Str ing stsToken) {
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

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample**
**Code** in the top navigation bar.

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues. Proceed with caution.

**Examples**

The following sample code provides an example on how to call RPC APIs. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code:

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
```

P to make API calls

```java
        // Create an API request and specify the request parameters.
        CommonRequest request = new CommonRequest();
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
        // If you use Security Token Service (STS) to call RPC API operations, you must
specify the SecurityToken parameter.
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");
        // Specify service-related parameters.
        request.putQueryParameter("PageSize", "10");
        request.putQueryParameter("PageNumber", "1");
        // Required. The call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0
and earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. The instance ID. This parameter is required for modify and delete
operations.
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

`}` `}` `}` The following sample code provides an example on how to call ROA APIs. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06- 07. Sample code: P to make API calls

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
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
        // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0
and earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. The instance ID. This parameter is required for modify and delete
```

P to make API calls

```java
operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
        // If you use access credentials assigned by STS to call ROA API operations, yo
u must add the x-acs-security-token field to the header.
        // request.putHeadParameter("x-acs-security-token", "<your-securitytoken>");
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

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample**
**Code** in the top navigation bar.
P to make API calls

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues. Proceed with caution.

**Background information**

Remote Procedure Call (RPC) and Resource-Oriented Architecture (ROA) APIs are supported.

**Examples**

The following sample code provides an example on how to call RPC APIs. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code: P to make API calls

```java
package main import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-RegionID>", "<AccessKey ID>", "<Ac
cessKey Secret>")
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<ApigatewayEndpoint>"
    request.Version = "2016-07-14"
    request.ApiName = "DescribeApiGroups"
    request.Product = "apigateway"
    // If you use Security Token Service (STS) to call RPC API operations, you must spe
cify the SecurityToken parameter.
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
    // Optional. The instance ID. This parameter is required for modify and delete oper
ations.
    // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}` The following sample code provides an example on how to call ROA APIs. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06- 07. Sample code: P to make API calls

```java
package main import (
 "fmt"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
 "os"
```

`)`

```xml
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-regionid>", "<yourAccessKeyId>", "
<yourAccessSecret>")
 request := requests.NewCommonRequest()
 request.Method = "GET"
 request.Domain = "<crEndpoint>"
 request.Version = "2016-06-07"
 request.ApiName = "GetNamespaceList"
 request.Product = "cr"
 request.PathPattern = "/namespace"
 // If you use STS to call ROA API operations, you must specify the x-acs-security-
token header.
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
 // Optional. The instance ID. This parameter is required for modify and delete operati
ons.
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
 os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // Set the HTTP_PROXY environment var
iable.
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

P to make API calls

```
// If you configure the HTTPSInsecure parameter for a request, the setting takes effect only on the current request. request.SetHTTPSInsecure(true) // Set the HTTPSInsecure parame ter to true for the request. isInsecure := request.GetHTTPSInsecure() // Query the setting of the HTT PSInsecure parameter for the request.
```

If you do not configure the HTTPSInsecure parameter for a request, the setting for a client takes effect.

```
// If you configure the HTTPSInsecure parameter for the client, the setting takes effec t on all requests that are initiated by the client. client.SetHTTPSInsecure(true) // Set the HTTPSInsecure parameter to true for the client. isInsecure := client.GetHTTPSInsecure() // Query the setting of the HTTPSI nsecure parameter for the client.
```

### 2.3 SDK for Python

This topic describes how to use SDK for Python over the point of presence (POP) gateway.

**Usage notes**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample**
**Code** in the top navigation bar.

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
```

P to make API calls

```
    "<your-RegionID>",
    timeout=1000,  # Specify the timeout period.
    verify=False, # Disable SSL certificate verification. To enable SSL certificate ver
ification, specify verify='<The path of the certificate>'.
```

);

```python
# Set the following parameters for the HTTPS request protocol:
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def describe_api_groups():
    # Create an API request and specify the required parameters.
    request = CommonRequest()
    # If you use Security Token Service (STS) to call RPC API operations, you must spec
ify the SecurityToken parameter.
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-
SecurityToken>"};
    params = {"PageSize":"10","PageNumber":"1"};
    request.set_query_params(params)
    headers = {
        # Required. The call source.
        "x-acs-caller-sdk-source":"ApiTestDemo",
        # Optional. The region ID. This parameter is required for Apsara Stack Enterpri
se Edition V3.15.0 and earlier.
        "x-acs-regionid":"<your-RegionID>",
        # Optional. The resource set ID.
        "x-acs-resourcegroupid":"<your-ResourceGroupID>",
        # Required. The organization ID.
        "x-acs-organizationid":"<your-OrganizationID>"
        # Optional. The instance ID. This parameter is required for modify and delete o
perations.
        # "x-acs-instanceid":"<your-InstanceID>"
```

`}`

```python
    request.set_headers(headers)
    request.set_version("2016-07-14")
    request.set_action_name("DescribeApiGroups")
    request.set_endpoint("<ApigatewayEndpoint>")   // Replace <ApigatewayEndpoint> with
the actual endpoint.
    request.set_product("apigateway")
    request.set_method("POST")
    # Initiate the API request and display the response.
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    describe_api_groups()
```

P to make API calls

**Proxy configuration**

You can configure a proxy for API calls by setting the HTTP_PROXY or HTTPS_PROXY environment variable. Sample code:

```bash
# Configure the HTTPS proxy.
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# Configure the HTTP proxy.
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

**HTTPS configuration**

This section describes related configurations for sending API requests over HTTPS.

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

P to make API calls

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # The region ID.
    verify='./cacert.pem'  # The path of the certificate authority (CA) certificate.
```

`)`

## 3 AppManager API

### 3.1 Definition

#### 3.1.1 API version differences and usage guidelines for Flink (Compute-Storage Separation Edition)

**guidelines for Flink (Compute-Storage**

**Separation Edition)**

This topic describes the differences, applicable scenarios, and usage guidelines for the two API versions (v1 and v2) currently available in Flink (Compute-Storage Separation Edition). It aims to help developers select the most suitable API version based on their specific business needs.

**Version description**

Flink (Compute-Storage Separation Edition) currently provides two sets of APIs. Flink (Compute-Storage Separation Edition) v1 APIs: This early API version runs stably in legacy business workloads. Flink (Compute-Storage Separation Edition) v2 APIs: This newly designed API version provides more comprehensive features, better scalability, and continuous future evolution. The complete API capabilities are jointly provided by both v1 and v2. While some features are implemented in both versions, their interface definitions and parameters differ.

**Usage guidelines**

**For new projects (v2 recommended)**

Available APIs: v1 and v2. When a feature is available in both versions, always choose v2. The v2 version will be continuously iterated and maintained. All new features will be introduced in v2. Adopting v2 from the start ensures better long-term support and continuous technical evolution.

**For legacy projects (continue with v1)**

Available APIs: v1 and v2. If your current business is already built on v1 and running stably, there is no need to actively migrate when a feature is available on both v1 and v2. Please continue using v1. The v1 version will no longer receive new features or non-critical updates. It will only be maintained for compatibility with existing workloads.

**Future evolution plan**

The v1 version will be gradually phased out and will no longer receive feature updates or optimizations. The v2 version will continue to be iterated and serves as the primary API standard for Flink (Compute-Storage Separation Edition).

#### 3.1.2 Compute-storage separation v1

##### 3.1.2.1 ValidateSqlScript

Call ValidateSqlScript to verify the correctness of an SQL script and return the verification result.

**Request headers**

This API uses common request headers and does not require special request headers. For more information, see the common request parameters documentation.

**Syntax**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:validate HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |
| paramsJso n | Strin g | Body | No | { "statement": "Drop TABLE `vvp`.`default`.`test`" } | The execution parameter, which is the SQL script. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the workspace ID by using one of the following methods: Call ListNamespaces to obtain the workspace ID. View the workspace details in the Fully Managed Flink development console. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

| Realtime Compute |   |   | nk (Compute-Storage Separation Edition) Developer Guide·AppM nager AP |
|---|---|---|---|
| Parameter | Type | Example | Description |
| data | String | { "validationResult": "VALIDATION RESU _ LT VALID DDL STA _ _ _ TEMENT" } | The detailed information. |
| success | Boolean | true | Indicates whether the request succeeded. |

**Examples**

Sample requests

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:validate HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "workspace":"default"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{\"validationResult\":\"VALIDATION_RESULT_VALID_DDL_STATEMENT\"}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data>{&quot;validationResult&quot;:&quot;VALIDATION_RESULT_VALID_DDL_STATEMENT&quot;}< /data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.2 UploadArtifactByOSSUrl

Updates folders on the data development page.

**Request headers**

The UploadArtifactByOSSUrl operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
POST /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:uploadByOSSUrl HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
| paramsJso n | Strin g | Body | No | {"filename":"", "ossUrl":""} | The execution parameters for SQL scripts. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

| data | String | { "@type": "type.googleapis.c om/vvp.artifacts.v1 .CreateArtifactResp onse", "artifact": { "filename": "TopSpeedWindowi ng.jar", "content": "******", "namespace": "namespaces/flinkt eam", "uploader": "20678996188752 3346", "createTime": "2026-04- 30T03:06:24Z", "uri": "oss://flink- fullymanaged- apmd99ri0du673/a rtifacts/namespace s/flinkteam/TopSpe edWindowing.jar", "size": "11957" } } | The detailed information. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
POST /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:uploadByOSSUrl HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "workspace":"default"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.artifacts.v1.CreateArtifactResponse\",\"artifact\": {\"filename\":\"TopSpeedWindowing.jar\",\"content\":\"******\",\"namespace\":\"namespaces linkteam\",\"uploader\":\"206789961887523346\",\"createTime\":\"2026-04- 30T03:06:24Z\",\"uri\":\"oss://flink-fullymanagedapmd99ri0du673/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar\",\"size\":\"11957\"}
```

`,`

```json
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.artifacts.v1.CreateArtifactResponse&quot &quot;artifact&quot;: {&quot;filename&quot;:&quot;TopSpeedWindowing.jar&quot;,&quot;content&quot;:&quot;******& ot;,&quot;namespace&quot;:&quot;namespaces/flinkteam&quot;,&quot;uploader&quot;:&quot;206 9961887523346&quot;,&quot;createTime&quot;:&quot;2026-04- 30T03:06:24Z&quot;,&quot;uri&quot;:&quot;oss://flink-fullymanagedapmd99ri0du673/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar&quot;,&quot;size&quot &quot;11957&quot;}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.3 UpdateUdfArtifact

Modifies a UDF JAR package.

**Request headers**

The UpdateUdfArtifact operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| paramsJso n | Strin g | Body | No | { "jarUrl": "http://flink- resource.oss-cn-wulan- env**-d01- a.intra.env**.shuguang.c om/udx/metric-transform- 2.2.7-shaded.jar" } | The change parameters. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |

| udfArtifact Name | Strin g | Path | Yes | metric-transform-227- shaded | The UDF name. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "missingClasses": [], "@type": "type.googleapis.c om/vvp.sql.v1beta 1.UpdateUdfArtifac tResponse", "collidingClasses": [], "udfArtifact": { "dependencyJarUri s": [], "udfClasses": [ { "functionNames": [], "udfArtifactName": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227-shaded", "className": "com.alibaba.blink. udtf.TimestampPro be", "classType": "UDF TYPE SCALA _ _ R" }, { "functionNames": [], "udfArtifactName": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227-shaded", "className": "com.alibaba.blink. udtf.TransformUdtf ", "classType": "UDF TYPE TABLE" _ _ } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "createTime": "2024-03- 08T08:13:54Z", "uploader": "22347490986944 5380", "jarUpdateTime": "2024-03- 08T09:04:22.5311 13Z", "name": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227-shaded", "namespace": "namespaces/flinkt | The detailed information. |

|   |   | eam", "jarUrl": "hdfs:///vvp/data/s ql- artifacts/namespac es/flinkteam/udfs/ metric-transform- 227-shaded/2024- 03-08T08-13- 54.732313Z/metric -transform-2.2.7- shaded.jar", "updateTime": "2024-03- 08T09:04:22.5311 13Z" } } |   |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactN e] HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam", "udfArtifactName":"metric-transform-227-shaded"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{\"missingClasses\":
[],\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.UpdateUdfArtifactResponse\",\"collidin lasses\":[],\"udfArtifact\":{\"dependencyJarUris\":[],\"udfClasses\": [{\"functionNames\":[],\"udfArtifactName\":\"namespaces/flinkteam/udfartifacts/metric-t ransform-227shaded\",\"className\":\"com.alibaba.blink.udtf.TimestampProbe\",\"classType\":\"UDF_TYPE CALAR\"},{\"functionNames\": [],\"udfArtifactName\":\"namespaces/flinkteam/udfartifacts/metric-transform-227-shaded\ ",\"className\":\"com.alibaba.blink.udtf.TransformUdtf\",\"classType\":\"UDF_TYPE_TABLE\" ,\"artifactType\":\"ARTIFACT_TYPE_JAVA\",\"createTime\":\"2024-03- 08T08:13:54Z\",\"uploader\":\"223474909869445380\",\"jarUpdateTime\":\"2024-03-08T09:04 :22.531113Z\",\"name\":\"namespaces/flinkteam/udfartifacts/metric-transform-227-shaded\ ",\"namespace\":\"namespaces/flinkteam\",\"jarUrl\":\"hdfs:///vvp/data/sqlartifacts/namespaces/flinkteam/udfs/metric-transform-227-shaded/2024-03-08T08-13-54.732 313Z/metric-transform-2.2.7-shaded.jar\",\"updateTime\":\"2024-03- 08T09:04:22.531113Z\"}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data>{&quot;missingClasses&quot;: [],&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.UpdateUdfArtifactResponse& ot;,&quot;collidingClasses&quot;:[],&quot;udfArtifact&quot;: {&quot;dependencyJarUris&quot;:[],&quot;udfClasses&quot;:[{&quot;functionNames&quot;:[] ,&quot;udfArtifactName&quot;:&quot;namespaces/flinkteam/udfartifacts/metric-transform-2 shaded&quot;,&quot;className&quot;:&quot;com.alibaba.blink.udtf.TimestampProbe&quot;,&quo classType&quot;:&quot;UDF_TYPE_SCALAR&quot;},{&quot;functionNames&quot;: [],&quot;udfArtifactName&quot;:&quot;namespaces/flinkteam/udfartifacts/metric-transform shaded&quot;,&quot;className&quot;:&quot;com.alibaba.blink.udtf.TransformUdtf&quot;,&quot lassType&quot;:&quot;UDF_TYPE_TABLE&quot;}],&quot;artifactType&quot;:&quot;ARTIFACT_TYPE_ VA&quot;,&quot;createTime&quot;:&quot;2024-03- 08T08:13:54Z&quot;,&quot;uploader&quot;:&quot;223474909869445380&quot;,&quot;jarUpdateTim quot;:&quot;2024-03- 08T09:04:22.531113Z&quot;,&quot;name&quot;:&quot;namespaces/flinkteam/udfartifacts/metric transform-227shaded&quot;,&quot;namespace&quot;:&quot;namespaces/flinkteam&quot;,&quot;jarUrl&quot;:&q t;hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/udfs/metric-transform-227-shaded/ 2024-03-08T08-13-54.732313Z/metric-transform-2.2.7shaded.jar&quot;,&quot;updateTime&quot;:&quot;2024-03-08T09:04:22.531113Z&quot;}}</data
```

`>`

```xml
<requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.4 UpdateMember

Call UpdateMember to change the business permissions of a specified user.

**Request headers**

This API uses common request headers and does not have special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
PUT /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| paramsJso n | Strin g | Body | No | { "role": "viewer", "member": "242425410145292209" } | The parameter used to change the business permissions of a user. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call ListNamespaces. View the workspace details in the Realtime Compute for Apache Flink fully managed development console. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The name of the region. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | 29F07013-6BE2- 4F99-90B6- 9E27BF2A26C4 | The request ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.members.v 1.UpdateMemberR esponse", "member": { "role": "owner", "member": "user:2424254101 45292209" } } | The detailed information about the business permissions of the user after the change. |

**Examples**

Request example

```
PUT /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1
```

`{`

```json
"workspace":"default", "namespace":"flinkteam", "RegionId":"cn-wulan-env***-d01"
```

`}` Successful response example `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.members.v1.UpdateMemberResponse\",\"member\":{\"ro le\":\"owner\",\"member\":\"user:242425410145292209\"}}",
 "success":true,
 "requestId":"29F07013-6BE2-4F99-90B6-9E27BF2A26C4"
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.members.v1.UpdateMemberResponse&quot;,&q t;member&quot;: {&quot;role&quot;:&quot;owner&quot;,&quot;member&quot;:&quot;user:242425410145292209&quot }</data> <success>true</success> <requestId>29F07013-6BE2-4F99-90B6-9E27BF2A26C4</requestId>
```

##### 3.1.2.5 UpdateFormat

Call UpdateFormat to modify a format. The modification includes whether the format can act as a source or a sink, format parameters, and dependent JAR packages.

**Request headers**

This API uses common request headers and does not have special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HTTP/
```

### 1.1 Obtain API information and its endpoint

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call ListNamespaces. View the workspace details in the Realtime Compute for Apache Flink fully managed development console. |
| name | Strin g | Path | Yes | customized-csv | The name of the format to modify. |
| paramsJso n | Strin g | Body | No | { "name": "namespaces/flinkteam/f ormats/customized-csv", "type": "customized- csv", "source": true, "sink": false, "properties": [ { "key": "format.column- delimiter", "required": false, "defaultValue": ",", "description": "" } ], "dependencies": [ "hdfs:///tmp/myformats/ customized-csv-demo- 1.0-SNAPSHOT.jar" ] } | The parameters for modifying the format. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| Realtime Compute |   |   | nk (Compute-Storage Separation Edition) Developer Guide·AppM nager AP |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "affectedTables": [], "@type": "type.googleapis.c om/vvp.sql.v1beta 1.UpdateFormatRe sponse", "format": { "sink": false, "name": "namespaces/flinkt eam/formats/custo mized-csv", "source": true, "type": "customized-csv", "properties": [ { "defaultValue": ",", "description": "", "definesFormat": false, "key": "format.column- delimiter", "required": false } ], "packaged": false, "dependencies": [ "hdfs:///tmp/myfor mats/customized- csv-demo-1.0- SNAPSHOT.jar" ] } } | The detailed information about the format after the modification. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

**Examples**

Request example

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HTTP/
```

### 1.1 Obtain API information and its endpoint

`{`

```json
"RegionId":"cn-wulan-env***-d01", "workspace":"default", "name":"customized-csv", "namespace":"flinkteam"
```

`}` Successful response example `JSON` format `{`

```json
 "data":"{\"affectedTables\":
[],\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.UpdateFormatResponse\",\"format\":{\ "sink\":false,\"name\":\"namespaces/flinkteam/formats/customizedcsv\",\"source\":true,\"type\":\"customized-csv\",\"properties\": [{\"defaultValue\":\",\",\"description\":\"\",\"definesFormat\":false,\"key\":\"format.co mn-delimiter\",\"required\":false}],\"packaged\":false,\"dependencies\": [\"hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar\"]}}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
```

`}` `XML` format

```xml
<data>{&quot;affectedTables&quot;: [],&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.UpdateFormatResponse&quot; quot;format&quot;: {&quot;sink&quot;:false,&quot;name&quot;:&quot;namespaces/flinkteam/formats/customizedcsv&quot;,&quot;source&quot;:true,&quot;type&quot;:&quot;customizedcsv&quot;,&quot;properties&quot;: [{&quot;defaultValue&quot;:&quot;,&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;format.columndelimiter&quot;,&quot;required&quot;:false}],&quot;packaged&quot;:false,&quot;dependencie quot;:[&quot;hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar&quot;]}}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

##### 3.1.2.6 UpdateDeploymentDesiredState

Call UpdateDeploymentDesiredState to update the desired state of a deployment in Realtime Compute.

**Request headers**

This API uses common request headers and does not require special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/stat HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |

| ealtime Com | pute |   |   | Realti nk (Co | me Compute for Apache Fl mpute-Storage Separation |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |
| deployme ntId | Strin g | Path | Yes | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | The job ID. |
| paramsJso n | Strin g | Body | No | {"state": "CANCELLED"} | The execution parameters and SQL scripts. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call ListNamespaces to obtain the ID. Obtain the ID from the workspace details in the Realtime Compute for Apache Flink development console. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
|   |   | { "metadata": { "createdAt": "2026-04- 24T03:47:01Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:58:25.5252 84Z", "resourceVersion": 172, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "creator": "23540697665705 7054", "resource- plan.has.migrated" : "true", "storage.disaster.r po": "1800", |   |

| Parameter | Type | "deployment.sourc Example e-type": "EDITOR", | Description |
|---|---|---|---|
|   |   | "deployment.has.d eployed": "false", "deployment.paren t.id": "", "modifier": "23540697665705 7054", |   |
|   |   | "creatorName": "flinkadmin", "plan.uri": "deployment/a3d8 8b2a-e076-4491- 86f2- 5a81ea4c7300/res ourcePlan.json", "priority": "5", "priority.class.nam e": "flink-p5", "migration.display. enabled": "false", "deployment.exec- plan.uri.valid": "true", "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "13", "default.resource- setting.has.migrate d": "true", "deployment.refere nced.deployment.d raft.history.version ": "1", "deployment.exec- plan.uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/fli nk- jobs/namespaces/fl inkteam/jobs/c944 e978-5cb9-4879- 8312- c0872ee50182/exe cPlan.json", "deployment.refere nced.deployment.d raft.id": "cee26b6e-d03b- 4a03-a628- a6fe665c525e", "resources.from.jo b.has.migrated": "true", "taker": " \| vvp-0", "modifierName": "flinkadmin", "deployment.refere nced.deployment.d raft.history.id": "561a6a3d-7858- 4056-acfb- ad0cdec09e55" }, "id": "a3d88b2a- |   |

| Parameter | Type | e076-4491-86f2- Example 5a81ea4c7300", | Description |
|---|---|---|---|
| data | String | "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type ": "fine-grained", "job.resource.total. memory.byte": "3724541952", "job.resource.total. cpu": "0.7", "native.kubernetes .mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.e nabled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.17.0-vvr-8.0.7- manifest-251107", "kind": "SQLSCRIPT", "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;", _ "imageUserDefined ": false, "flinkImageRegistr y": "cn-wulan- | The detailed information. |

| Parameter | Type | env35-d01- Example reg.docker.intra.en | Description |
|---|---|---|---|
|   |   | v35.shuguang.com :80/ververica- paas", "versionName": "vvr-8.0.7-flink- 1.17", "flinkImageReposit ory": "vvr", "flinkVersion": "1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration" : {} } }, "restoreStrategy": { "kind": "FROM SAVEPOINT _ ", "allowNonRestored State": false, "savepointId": "5cea0d88-303d- 44e5-a96e- 47f7217723d7" }, "state": "CANCELLED", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1, "deploymentTarget Id": "a89ff052- 38c6-4fd3-9b91- e9c53f8ee019" }, "status": { "startTime": 1777002980004, "state": "RUNNING", "endTime": 0 } } |   |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample request

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/stat HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7def580c00", "workspace":"default"
```

`}` Sample success response `JSON` format `{`

```json
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:47:01Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:58:25.525284Z\",\"resourceVersion\":172,\"name\":\"sqlJob\",\"namespace\":\"flinkte \",\"annotations\":{\"creator\":\"235406976657057054\",\"resourceplan.has.migrated\":\"true\",\"storage.disaster.rpo\":\"1800\",\"deployment.source-type \":\"EDITOR\",\"deployment.has.deployed\":\"false\",\"deployment.parent.id\":\"\",\"modif r\":\"235406976657057054\",\"creatorName\":\"flinkadmin\",\"plan.uri\":\"deployment/a3d88 a-e076-4491-86f2- 5a81ea4c7300/resourcePlan.json\",\"priority\":\"5\",\"priority.class.name\":\"flink-p5\ ",\"migration.display.enabled\":\"false\",\"deployment.execplan.uri.valid\":\"true\",\"com.dataartisans.appmanager.controller.deployment.spec.versio ":\"13\",\"default.resourcesetting.has.migrated\":\"true\",\"deployment.referenced.deployment.draft.history.version\ \"1\",\"deployment.exec-plan.uri\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flink-jobs /namespaces/flinkteam/jobs/c944e978-5cb9-4879-8312c0872ee50182/execPlan.json\",\"deployment.referenced.deployment.draft.id\":\"cee26b6e-d 03b-4a03-a628-a6fe665c525e\",\"resources.from.job.has.migrated\":\"true\",\"taker\":\"
| vvp-
0\",\"modifierName\":\"flinkadmin\",\"deployment.referenced.deployment.draft.history.id\" "561a6a3d-7858-4056-acfb-ad0cdec09e55\"},\"id\":\"a3d88b2a-e076-4491-86f2- 5a81ea4c7300\",\"labels\":{}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\":{\ "template\":{\"metadata\":{\"annotations\":{\"flink.resource.type\":\"fine-grained\",\" job.resource.total.memory.byte\":\"3724541952\",\"job.resource.total.cpu\":\"0.7\",\"nati .kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\":{\"artifa ct\":{\"flinkImageTag\":\"1.17.0-vvr-8.0.7-manifest- 251107\",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'connector' = 'datagen'\);\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\);\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-wulan-env35-d01 -reg.docker.intra.env35.shuguang.com:80/ververica-paas\",\"versionName\":\"vvr-8.0.7-fl ink- 1.17\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.17\"},\"parallelism\":1,\"ba hMode\":false,\"resources\":{\"jobmanager\": {\"memory\":\"2Gi\",\"cpu\":0.5},\"taskmanager\": {\"memory\":\"3Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfig ation\":{}}},\"restoreStrategy\": {\"kind\":\"FROM_SAVEPOINT\",\"allowNonRestoredState\":false,\"savepointId\":\"5cea0d88- 303d-44e5-a96e-47f7217723d7\"},\"state\":\"CANCELLED\",\"upgradeStrategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"dep ymentTargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"},\"status\": {\"startTime\":1777002980004,\"state\":\"RUNNING\",\"endTime\":0}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<dt>{&
```

`t`

```
tdt&
```

`t` `{&` `t`

```
tdAt&
```

`t` `&`

```
t202604
```

|   | <data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:47:01Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot &quot;2026-04- 24T03:58:25.525284Z&quot;,&quot;resourceVersion&quot;:172,&quot;name&quot;:&quot;sqlJob&q t;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;resource- plan.has.migrated&quot;:&quot;true&quot;,&quot;storage.disaster.rpo&quot;:&quot;1800&quot &quot;deployment.source- type&quot;:&quot;EDITOR&quot;,&quot;deployment.has.deployed&quot;:&quot;false&quot;,&quot eployment.parent.id&quot;:&quot;&quot;,&quot;modifier&quot;:&quot;235406976657057054&quot &quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;plan.uri&quot;:&quot;deployment/a3d8 2a-e076-4491-86f2- 5a81ea4c7300/resourcePlan.json&quot;,&quot;priority&quot;:&quot;5&quot;,&quot;priority.cl s.name&quot;:&quot;flink- p5&quot;,&quot;migration.display.enabled&quot;:&quot;false&quot;,&quot;deployment.exec- plan.uri.valid&quot;:&quot;true&quot;,&quot;com.dataartisans.appmanager.controller.deploy nt.spec.version&quot;:&quot;13&quot;,&quot;default.resource- setting.has.migrated&quot;:&quot;true&quot;,&quot;deployment.referenced.deployment.draft. story.version&quot;:&quot;1&quot;,&quot;deployment.exec- plan.uri&quot;:&quot;oss://flink-fullymanaged-9cuwr9g7y1hl19/flink- jobs/namespaces/flinkteam/jobs/c944e978-5cb9-4879-8312- c0872ee50182/execPlan.json&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&q t;cee26b6e-d03b-4a03-a628- a6fe665c525e&quot;,&quot;resources.from.job.has.migrated&quot;:&quot;true&quot;,&quot;tak &quot;:&quot; \| vvp- 0&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;deployment.referenced.deplo ent.draft.history.id&quot;:&quot;561a6a3d-7858-4056-acfb- ad0cdec09e55&quot;},&quot;id&quot;:&quot;a3d88b2a-e076-4491-86f2- 5a81ea4c7300&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;s c&quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;:{&quot;fli nk.resource.type&quot;:&quot;fine- grained&quot;,&quot;job.resource.total.memory.byte&quot;:&quot;3724541952&quot;,&quot;job esource.total.cpu&quot;:&quot;0.7&quot;,&quot;native.kubernetes.mode&quot;:&quot;true&quo ,&quot;flink.queryable- state.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false& ot;}},&quot;spec&quot;:{&quot;artifact&quot;:{&quot;flinkImageTag&quot;:&quot;1.17.0-vv r-8.0.7-manifest- 251107&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;CREATE TEMPORARY TABLE `datahub table` (strname VARCHAR)with ( &#x27;connector&#x27; = &#x2 _ 7;datagen&#x27;);CREATE TEMPORARY TABLE `kafka table` (strname VARCHAR, lens BIGINT)wit _ h ( &#x27;connector&#x27; = &#x27;print&#x27;);INSERT INTO kafka tableSELECT SUBSTRI _ NG (strname, 0, 10) AS strname, CAST (CHAR LENGTH (strname) AS BIGINT) AS lensFROM dat _ ahub table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&quot _ n-wulan-env35-d01-reg.docker.intra.env35.shuguang.com:80/ververica- paas&quot;,&quot;versionName&quot;:&quot;vvr-8.0.7-flink- 1.17&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quo 1.17&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;: {&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;2Gi&quot;,&quot;cpu&quot;:0.5},&quot;taskmanager&quot;:{&quot ;memory&quot;:&quot;3Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&q t;default&quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;:{&quot ;kind&quot;:&quot;FROM SAVEPOINT&quot; &quot;allowNonRestoredState&quot;:false &quot;save |   |
|---|---|---|

```xml
;kind&quot;:&quot;FROM_SAVEPOINT&quot;,&quot;allowNonRestoredState&quot;:false,&quot;save intId&quot;:&quot;5cea0d88-303d-44e5-a96e- 47f7217723d7&quot;},&quot;state&quot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJ CreationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9b91-e 9c53f8ee019&quot;},&quot;status&quot;: {&quot;startTime&quot;:1777002980004,&quot;state&quot;:&quot;RUNNING&quot;,&quot;endTime& ot;:0}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.7 UpdateDeployment

Call UpdateDeployment to update a deployed job.

**Request headers**

This API uses common request headers and does not require special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/patc HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project that contains the job. |
| deployme ntId | Strin g | Path | Yes | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | The job ID. |
|   |   |   |   | { "metadata": { "id": "7325ac07-e466-4c1b- b598-311c6f2c103b", "name": "sqlJob", "namespace": "flinkteam", "workspace": "9cuwr9g7y1hl19", "createdAt": "2026-04- 28T01:59:31Z", "modifiedAt": "2026-04- 28T02:07:18Z", "labels": {}, "annotations": { "creator": "235406976657057054" , "resource- plan.has.migrated": |   |

| Parame ter | Typ e | Positi on | Require d | "true", "Esxtoarmagpe.ldeisaster.rpo": "1800", | Description |
|---|---|---|---|---|---|
| paramsJso n | Strin g | Body | No | "deployment.has.deploy ed": "false", "deployment.source- type": "EDITOR", "deployment.parent.id": "", "modifier": "235406976657057054" , "creatorName": "flinkadmin", "plan.uri": "deployment/7325ac07- e466-4c1b-b598- 311c6f2c103b/resourceP lan.json", "priority": "5", "priority.class.name": "flink-p5", "migration.display.enabl ed": "false", "com.dataartisans.appm anager.controller.deploy ment.spec.version": "5", "default.resource- setting.has.migrated": "true", "deployment.referenced. deployment.draft.history .version": "3", "deployment.referenced. deployment.draft.id": "cee26b6e-d03b-4a03- a628-a6fe665c525e", "modifierName": "flinkadmin", "taker": " \| vvp-0", "deployment.referenced. deployment.draft.history .id": "5bfca9e9-a50d- 483b-bad5- 1e1d5315acaf", "one- time.retry": "false", "stop-with- savepoint.enabled": false }, "resourceVersion": 9 }, "spec": { "state": "SUSPENDED", "upgradeStrategy": { "kind": "NONE" }, "restoreStrategy": { "kind": "LATEST STATE" _ }, "deploymentTargetId": "a89ff052-38c6-4fd3- 9b91-e9c53f8ee019", "maxSavepointCreation Attempts": 4, "maxJobCreationAttempt s": 1, "template": { "metadata": { "annotations": { "flink.resource.type": "fine-grained", "job.resource.total.mem ory.byte": "0", | The execution parameters and SQL script. |

| Parame ter | Typ e | Positi on | Require d | "job.resource.total.cpu": "E0x.0a"m, ple "native.kubernetes.mod | Description |
|---|---|---|---|---|---|
|   |   |   |   | e": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.enable d": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "versionName": "vvr- 8.0.7-flink-1.17", "imageUserDefined": false, "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;", _ "flinkVersion": "1.17", "flinkImageTag": "1.17.0-vvr-8.0.7- manifest-251107", "flinkImageRegistry": "cn-wulan-env**-d01- reg.docker.intra.env**.s huguang.com:80/ververi ca-paas", "flinkImageRepository": "vvr" }, "parallelism": 1, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "flinkConfiguration": {}, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "batchMode": false } } }, "status": { "state": "SUSPENDED", "startTime": |   |

| Parame | Typ | Positi | Require | 1777341571990, "EexnadmTimpele": 0 } } | Description |
|---|---|---|---|---|---|
| ter | e | on | d |   |   |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace that contains the job. You can obtain the ID in one of the following ways: Call ListNamespaces. View the workspace details in the Realtime Compute for Apache Flink fully managed development console. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
|   |   | { "metadata": { "createdAt": "2026-04- 24T03:47:01Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:56:19.5561 47Z", "resourceVersion": 134, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "storage.disaster.r po": "1800", "deployment.sourc e-type": "EDITOR", "modifier": "23540697665705 7054", "creatorName": "flinkadmin", "one- time.retry": "false", "priority.class.nam e": "flink-p5", "deployment.exec- plan.uri.valid": "true", "default.resource- setting.has.migrate d": "true", "deployment.exec- plan.uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/fli |   |

| Parameter | Type | nk- Example jobs/namespaces/fl | Description |
|---|---|---|---|
|   |   | inkteam/jobs/f736b bd6-c9cf-48ab- 973a- 9653bb0f8c0a/exe cPlan.json", "deployment.refere nced.deployment.d raft.id": "cee26b6e-d03b- 4a03-a628- a6fe665c525e", "resources.from.jo b.has.migrated": "true", "taker": " \| vvp-0", "creator": "23540697665705 7054", "resource- plan.has.migrated" : "true", "restore- from.savepoint-id": "5cea0d88-303d- 44e5-a96e- |   |
|   |   | 47f7217723d7", "stop-with- savepoint.enabled" : "false", "deployment.has.d eployed": "false", "deployment.paren t.id": "", "plan.uri": "deployment/a3d8 8b2a-e076-4491- 86f2- 5a81ea4c7300/res ourcePlan.json", "priority": "5", "migration.display. enabled": "false", "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "11", "deployment.refere nced.deployment.d raft.history.version ": "1", "modifierName": "flinkadmin", "deployment.refere nced.deployment.d raft.history.id": "561a6a3d-7858- 4056-acfb- ad0cdec09e55" }, "id": "a3d88b2a- e076-4491-86f2- 5a81ea4c7300", "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { |   |

| Parameter | Type | "annotations": { Example "flink.resource.type | Description |
|---|---|---|---|
| data | Integer | ": "fine-grained", "job.resource.total. memory.byte": "0", "job.resource.total. cpu": "0.0", "native.kubernetes .mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.e nabled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.17.0-vvr-8.0.7- manifest-251107", "kind": "SQLSCRIPT", "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;", _ "imageUserDefined ": false, "flinkImageRegistr y": "cn-wulan- env35-d01- reg.docker.intra.en v35.shuguang.com :80/ververica- paas", "versionName": "vvr-8.0.7-flink- 1.17", "flinkImageReposit ory": "vvr", | The detailed information. |

| Parameter | Type | "flinkVersion": Example "1.17" }, | Description |
|---|---|---|---|
|   |   | "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration" : {} } }, "restoreStrategy": { "kind": "FROM SAVEPOINT _ ", "allowNonRestored State": false, "savepointId": "5cea0d88-303d- 44e5-a96e- 47f7217723d7" }, "state": "SUSPENDED", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1, "deploymentTarget Id": "a89ff052- 38c6-4fd3-9b91- e9c53f8ee019" }, "status": { "startTime": 1777002791356, "state": "SUSPENDED", "endTime": 0 } } |   |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/patc HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7def580c00", "workspace":"default"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:47:01Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:56:19.556147Z\",\"resourceVersion\":134,\"name\":\"sqlJob\",\"namespace\":\"flinkte \",\"annotations\":{\"storage.disaster.rpo\":\"1800\",\"deployment.sourcetype\":\"EDITOR\",\"modifier\":\"235406976657057054\",\"creatorName\":\"flinkadmin\",\"on time.retry\":\"false\",\"priority.class.name\":\"flink-p5\",\"deployment.exec-plan.uri. valid\":\"true\",\"default.resource-setting.has.migrated\":\"true\",\"deployment.exec-p lan.uri\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flinkjobs/namespaces/flinkteam/jobs/f736bbd6-c9cf-48ab-973a- 9653bb0f8c0a/execPlan.json\",\"deployment.referenced.deployment.draft.id\":\"cee26b6e-d 03b-4a03-a628-a6fe665c525e\",\"resources.from.job.has.migrated\":\"true\",\"taker\":\"
| vvp-0\",\"creator\":\"235406976657057054\",\"resource-
plan.has.migrated\":\"true\",\"restore-from.savepoint-id\":\"5cea0d88-303d-44e5-a96e-47 f7217723d7\",\"stop-withsavepoint.enabled\":\"false\",\"deployment.has.deployed\":\"false\",\"deployment.parent.i ":\"\",\"plan.uri\":\"deployment/a3d88b2a-e076-4491-86f2- 5a81ea4c7300/resourcePlan.json\",\"priority\":\"5\",\"migration.display.enabled\":\"false ,\"com.dataartisans.appmanager.controller.deployment.spec.version\":\"11\",\"deployment.r erenced.deployment.draft.history.version\":\"1\",\"modifierName\":\"flinkadmin\",\"deploy nt.referenced.deployment.draft.history.id\":\"561a6a3d-7858-4056-acfbad0cdec09e55\"},\"id\":\"a3d88b2a-e076-4491-86f2-5a81ea4c7300\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\":{\"template\":{\"metadata\": {\"annotations\":{\"flink.resource.type\":\"finegrained\",\"job.resource.total.memory.byte\":\"0\",\"job.resource.total.cpu\":\"0.0\",\"n ive.kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\":{\"artifa ct\":{\"flinkImageTag\":\"1.17.0-vvr-8.0.7-manifest- 251107\",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'connector' = 'datagen'\);\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\);\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-wulan-env35-d01 -reg.docker.intra.env35.shuguang.com:80/ververica-paas\",\"versionName\":\"vvr-8.0.7-fl ink- 1.17\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.17\"},\"parallelism\":1,\"ba hMode\":false,\"resources\":{\"jobmanager\": {\"memory\":\"2Gi\",\"cpu\":0.5},\"taskmanager\": {\"memory\":\"3Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfig ation\":{}}},\"restoreStrategy\": {\"kind\":\"FROM_SAVEPOINT\",\"allowNonRestoredState\":false,\"savepointId\":\"5cea0d88- 303d-44e5-a96e-47f7217723d7\"},\"state\":\"SUSPENDED\",\"upgradeStrategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"dep ymentTargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"},\"status\": {\"startTime\":1777002791356,\"state\":\"SUSPENDED\",\"endTime\":0}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

| <data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:47:01Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot &quot;2026-04- 24T03:56:19.556147Z&quot;,&quot;resourceVersion&quot;:134,&quot;name&quot;:&quot;sqlJob&q t;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;storage.disaster.rpo&quot;:&quot;1800&quot;,&quot;deployment.source- type&quot;:&quot;EDITOR&quot;,&quot;modifier&quot;:&quot;235406976657057054&quot;,&quot;c atorName&quot;:&quot;flinkadmin&quot;,&quot;one- time.retry&quot;:&quot;false&quot;,&quot;priority.class.name&quot;:&quot;flink-p5&quot; ,&quot;deployment.exec-plan.uri.valid&quot;:&quot;true&quot;,&quot;default.resource-set ting.has.migrated&quot;:&quot;true&quot;,&quot;deployment.exec- plan.uri&quot;:&quot;oss://flink-fullymanaged-9cuwr9g7y1hl19/flink- jobs/namespaces/flinkteam/jobs/f736bbd6-c9cf-48ab-973a- 9653bb0f8c0a/execPlan.json&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&q t;cee26b6e-d03b-4a03-a628- a6fe665c525e&quot;,&quot;resources.from.job.has.migrated&quot;:&quot;true&quot;,&quot;tak &quot;:&quot; \| vvp- 0&quot;,&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;resource- plan.has.migrated&quot;:&quot;true&quot;,&quot;restore-from.savepoint- id&quot;:&quot;5cea0d88-303d-44e5-a96e-47f7217723d7&quot;,&quot;stop-with- savepoint.enabled&quot;:&quot;false&quot;,&quot;deployment.has.deployed&quot;:&quot;false uot;,&quot;deployment.parent.id&quot;:&quot;&quot;,&quot;plan.uri&quot;:&quot;deployment/ d88b2a-e076-4491-86f2- 5a81ea4c7300/resourcePlan.json&quot;,&quot;priority&quot;:&quot;5&quot;,&quot;migration.d play.enabled&quot;:&quot;false&quot;,&quot;com.dataartisans.appmanager.controller.deploym t.spec.version&quot;:&quot;11&quot;,&quot;deployment.referenced.deployment.draft.history. rsion&quot;:&quot;1&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;deploymen referenced.deployment.draft.history.id&quot;:&quot;561a6a3d-7858-4056-acfb- ad0cdec09e55&quot;},&quot;id&quot;:&quot;a3d88b2a-e076-4491-86f2- 5a81ea4c7300&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;s c&quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;:{&quot;fli nk.resource.type&quot;:&quot;fine- grained&quot;,&quot;job.resource.total.memory.byte&quot;:&quot;0&quot;,&quot;job.resource otal.cpu&quot;:&quot;0.0&quot;,&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot; ink.queryable- state.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false& ot;}},&quot;spec&quot;:{&quot;artifact&quot;:{&quot;flinkImageTag&quot;:&quot;1.17.0-vv r-8.0.7-manifest- 251107&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;CREATE TEMPORARY TABLE `datahub table` (strname VARCHAR)with ( &#x27;connector&#x27; = &#x2 _ 7;datagen&#x27;);CREATE TEMPORARY TABLE `kafka table` (strname VARCHAR, lens BIGINT)wit _ h ( &#x27;connector&#x27; = &#x27;print&#x27;);INSERT INTO kafka tableSELECT SUBSTRI _ NG (strname, 0, 10) AS strname, CAST (CHAR LENGTH (strname) AS BIGINT) AS lensFROM dat _ ahub table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&quot _ n-wulan-env35-d01-reg.docker.intra.env35.shuguang.com:80/ververica- paas&quot;,&quot;versionName&quot;:&quot;vvr-8.0.7-flink- 1.17&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quo 1.17&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;: {&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;2Gi&quot;,&quot;cpu&quot;:0.5},&quot;taskmanager&quot;:{&quot ;memory&quot;:&quot;3Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&q |   |
|---|---|

```xml
t;default&quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;:{&quot ;kind&quot;:&quot;FROM_SAVEPOINT&quot;,&quot;allowNonRestoredState&quot;:false,&quot;save intId&quot;:&quot;5cea0d88-303d-44e5-a96e- 47f7217723d7&quot;},&quot;state&quot;:&quot;SUSPENDED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJ CreationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9b91-e 9c53f8ee019&quot;},&quot;status&quot;: {&quot;startTime&quot;:1777002791356,&quot;state&quot;:&quot;SUSPENDED&quot;,&quot;endTim quot;:0}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

```html ```

##### 3.1.2.8 UpdateConnector

Call UpdateConnector to modify the information of a custom connector.

**Request headers**

This API uses common request headers and does not require special request headers. For more information, see Common request parameters.

**Syntax**

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HT TP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call ListNamespaces. View the workspace details in the Realtime Compute for Apache Flink fully managed development console. |
| name | Strin g | Path | Yes | hologres-fix | The name of the connector to modify. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| paramsJso n | Strin g | Body | No | { "type": "hologres-fix", "name": "namespaces/flinkteam/ connectors/hologres-fix", "packaged": false, "source": true, "sink": true, "lookup": false, "dependencies": [ "hdfs:///vvp/data/sql- artifacts/namespaces/fli nkteam/custom- connectors/2024-03- 11T05-51- 25.289740Z/ververica- connector-hologres- 1.15-vvr-6.0-fix.jar" ], "supportedFormats": [ "json","csv" ], "properties": [ { "key": "connector", "required": true, "defaultValue": "hologres-fix", "description": "", "definesFormat": false }, { "key": "dbname", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "endpoint", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "tablename", "required": true, "defaultValue": "", "description": "", "definesFormat": false } ] } | The modification parameters declare the properties of the connector, such as the type name, required connection parameters, source and sink capabilities, and dependent JAR packages. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "affectedTables": [], "connector": { "lookup": true, "supportedFormats ": [ "json", "csv" ], "environments": [], "sink": true, "name": "namespaces/flinkt eam/connectors/ho logres-fix", "source": true, "type": "hologres- fix", "properties": [ { "defaultValue": "hologres-fix", "description": "", "definesFormat": false, "key": "connector", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "dbname", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "endpoint", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "tablename", "required": true } ], "packaged": false, "dependencies": [ "hdfs:///vvp/data/s ql- artifacts/namespac es/flinkteam/custo m- connectors/2024- 03-11T05-51- 25.289740Z/verver ica-connector- hologres-1.15-vvr- 6.0-fix.jar" ] }, "@type": "type.googleapis.c om/vvp.sql.v1beta 1.UpdateConnector Response" } | The detailed data. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | 4FA46133-1C97- 4B48-96E3- 3B7DFFFEC707 | The request ID. |

**Examples**

Sample requests

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HT TP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "workspace":"default", "name":"hologres-fix", "namespace":"flinkteam"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{\"affectedTables\":[],\"connector\":{\"lookup\":true,\"supportedFormats\":[\"
json\",\"csv\"],\"environments\": [],\"sink\":true,\"name\":\"namespaces/flinkteam/connectors/hologresfix\",\"source\":true,\"type\":\"hologres-fix\",\"properties\": [{\"defaultValue\":\"hologresfix\",\"description\":\"\",\"definesFormat\":false,\"key\":\"connector\",\"required\":tru
```

`,`

```json
{\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"dbname\",\" quired\":true}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"endpoint\", required\":true}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"tablename\" "required\":true}],\"packaged\":false,\"dependencies\":[\"hdfs:///vvp/data/sql-artifact s/namespaces/flinkteam/custom-connectors/2024-03-11T05-51-25.289740Z/ververica-connecto r-hologres-1.15-vvr-6.0fix.jar\"]},\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.UpdateConnectorResponse\"}",
 "success":true,
 "requestId":"4FA46133-1C97-4B48-96E3-3B7DFFFEC707"
```

`}` `XML` format

```xml
<data>{&quot;affectedTables&quot;:[],&quot;connector&quot;: {&quot;lookup&quot;:true,&quot;supportedFormats&quot;: [&quot;json&quot;,&quot;csv&quot;],&quot;environments&quot;: [],&quot;sink&quot;:true,&quot;name&quot;:&quot;namespaces/flinkteam/connectors/hologresfix&quot;,&quot;source&quot;:true,&quot;type&quot;:&quot;hologresfix&quot;,&quot;properties&quot;:[{&quot;defaultValue&quot;:&quot;hologresfix&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFormat&quot;:false,&quot;key& ot;:&quot;connector&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;dbname&quot;,&quot;required&quot;:true},{&quot;d efaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFormat&q t;:false,&quot;key&quot;:&quot;endpoint&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;tablename&quot;,&quot;required&quot;:true}],&quot; ckaged&quot;:false,&quot;dependencies&quot;:[&quot;hdfs:///vvp/data/sqlartifacts/namespaces/flinkteam/custom-connectors/2024-03-11T05-51-25.289740Z/ververicaconnector-hologres-1.15-vvr-6.0fix.jar&quot;]},&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.UpdateConnect Response&quot;}</data> <success>true</success> <requestId>4FA46133-1C97-4B48-96E3-3B7DFFFEC707</requestId>
```

```html ```

##### 3.1.2.9 TableExists

Checks whether a table exists.

**Request headers**

The TableExists operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:tableEx ts HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | ververica | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |

| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
|---|---|---|---|---|---|
| cat | Strin g | Path | Yes | vvp | The catalog name. |
| database | Strin g | Quer y | Yes | default | The database name. |
| table | Strin g | Quer y | Yes | mydatahub | The table name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.TableExist sResponse", "exists": true } | The detailed information. |
| requestId | String | 39253EC3-B674- 4B11-AD97- C221D6DB1003 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:tableEx ts HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &database=default &table=mydatahub &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.TableExistsResponse\",\"exists\" rue}",
 "requestId":"39253EC3-B674-4B11-AD97-C221D6DB1003",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.TableExistsResponse& ot;,&quot;exists&quot;:true}</data> <requestId>39253EC3-B674-4B11-AD97-C221D6DB1003</requestId> <success>true</success>
```

##### 3.1.2.10 SetDeploymentResourceMode

Call SetDeploymentResourceMode to set the resourceMode of a job.

**Request headers**

This API uses common request headers and does not require special request headers. For more information, see Common request parameters.

**Syntax**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/setresource HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call ListNamespaces to obtain the ID. View the workspace details in the Realtime Compute for Apache Flink console. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |
| deployme ntId | Strin g | Path | Yes | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | The job ID. |
| paramsJso n | Strin g | Body | No | { "deploymentResourceM odeBase": { "kind": "auto" } } | The request parameter. Valid values of kind: auto, fine-grained, and coarse-grained. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
|   |   | { "metadata": { "createdAt": "2024-03- 12T06:12:17Z", "modifiedAt": "2024-03- 12T06:44:00.8233 23Z", "resourceVersion": 15, "name": "sqljob", "namespace": "flinkteam", "annotations": { "creator": "22985261012276 3813", "resource- plan.has.migrated" : "true", "deployment.has.d eployed": "false", "deployment.sourc e-type": "EDITOR", "deployment.paren t.id": "", "modifier": "22985261012276 3813", "creatorName": "flinkadmin", "priority": "5", "priority.class.nam e": "", "autopilot.mode": "monitor", "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "3", |   |

| Parameter | Type | "deployment.refere Example nced.deployment.d | Description |
|---|---|---|---|
|   |   | raft.history.version ": "1", "x- namespace-owner- master-uid": "10529101227299 09", "default.resource- setting.has.migrate d": "true", "deployment.exec- plan.uri": "hdfs:///vvp/data/pl an/namespaces/flin kteam/deployment/ d0b3abf0-4bfe- 46b1-a324- 5b7def580c00/exe cPlan.json", "deployment.refere nced.deployment.d raft.id": "c6f157ac- 60b9-4b38-8bad- |   |
|   |   | d435387cfd59", "comment": "", "modifierName": "flinkadmin", "taker": "default- cluster \| 0", "deployment.refere nced.deployment.d raft.history.id": "1fbfefd4-9b1c- 4e94-b6ad- 268a5c6b64cd" }, "workspaceName": "default", "id": "d0b3abf0-4bfe- 46b1-a324- 5b7def580c00", "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type ": "auto", "job.resource.total. memory.byte": "8589934592", "job.resource.total. cpu": "4.0", "native.kubernetes .mode": "true", "flink.queryable- state.enabled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.15.0-vvr-6.0.7- 29", "kind": "SQLSCRIPT", |   |

| Parameter | Type | "sqlScript": "-- Example ******************* | Description |
|---|---|---|---|
| data | String | ******************* ******************* ***********-- -- Author: Write your name here -- Created Time: 2024-03-12 14:11:38 -- Description: Write your description here -- ******************* ******************* ******************* ***********-- CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( \u0027connector\u 0027 \u003d \u0027datagen\u0 027 ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( \u0027connector\u 0027 \u003d \u0027print\u0027 ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ ", "imageUserDefined ": false, "flinkImageRegistr y": "cn-qingdao- env17e-d01- reg.docker.intra.en v17e.shuguang.co m:80/ververica- paas", "versionName": "vvr-6.0.0-flink- 1.15", "flinkImageReposit ory": "vvr", | The detailed data. |

| Parameter | Type | "flinkVersion": Example "1.15" }, | Description |
|---|---|---|---|
|   |   | "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 2.0 }, "taskmanager": { "memory": "4Gi", "cpu": 2.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration" : { "execution.checkp ointing.interval": "180s", "execution.checkp ointing.min-pause": "180s" } } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestored State": false }, "state": "RUNNING", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1, "deploymentTarget Id": "f2ed6708- a7e1-4e86-a99e- 327fac9265c2" }, "status": { "startTime": 0, "state": "RUNNING", "endTime": 0 } } |   |
| requestId | String | BCC13432-238D- 41D7-B0A6- 582241A6B572 | The request ID. |

**Examples**

Sample request

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/setresource HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7def580c00"
```

`}` Sample success response `JSON` format `{`

```json
 "data":"{\"metadata\":{\"createdAt\":\"2024-03-12T06:12:17Z\",\"modifiedAt\":\"2024-03
```

`-`

```json
12T06:44:00.823323Z\",\"resourceVersion\":15,\"name\":\"sqljob\",\"namespace\":\"flinktea ",\"annotations\":{\"creator\":\"229852610122763813\",\"resourceplan.has.migrated\":\"true\",\"deployment.has.deployed\":\"false\",\"deployment.sourcetype\":\"EDITOR\",\"deployment.parent.id\":\"\",\"modifier\":\"229852610122763813\",\"cre orName\":\"flinkadmin\",\"priority\":\"5\",\"priority.class.name\":\"\",\"autopilot.mode\ \"monitor\",\"com.dataartisans.appmanager.controller.deployment.spec.version\":\"3\",\"de oyment.referenced.deployment.draft.history.version\":\"1\",\"x-namespace-owner-master-u id\":\"1052910122729909\",\"default.resourcesetting.has.migrated\":\"true\",\"deployment.execplan.uri\":\"hdfs:///vvp/data/plan/namespaces/flinkteam/deployment/d0b3abf0-4bfe-46b1-a 5b7def580c00/execPlan.json\",\"deployment.referenced.deployment.draft.id\":\"c6f157ac-6 0b9-4b38-8badd435387cfd59\",\"comment\":\"\",\"modifierName\":\"flinkadmin\",\"taker\":\"default-clu ster | 0\",\"deployment.referenced.deployment.draft.history.id\":\"1fbfefd4-9b1c-4e94-b 6ad-268a5c6b64cd\"},\"workspaceName\":\"default\",\"id\":\"d0b3abf0-4bfe-46b1-a324-5b7d ef580c00\",\"labels\":{}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\":{\"tem plate\":{\"metadata\":{\"annotations\": {\"flink.resource.type\":\"auto\",\"job.resource.total.memory.byte\":\"8589934592\",\"job esource.total.cpu\":\"4.0\",\"native.kubernetes.mode\":\"true\",\"flink.queryable-state .enabled\":\"false\"}},\"spec\":{\"artifact\":{\"flinkImageTag\":\"1.15.0-vvr-6.0.7-29\ ",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"--
********************************************************************--\-- Author:
Write your name here\-- Created Time: 2024-03-12 14:11:38\-- Description: Write your description here\--
********************************************************************--\CREATE TEMPORARY
TABLE `datahub_table` (strname VARCHAR)\with (\ \\u0027connector\\u0027 \\u003d \\u0 027datagen\\u0027\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIG INT)\with (\ \\u0027connector\\u0027 \\u003d \\u0027print\\u0027\ );\\INSERT INTO k afka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-qingdao-env17e -d01-reg.docker.intra.env17e.shuguang.com:80/ververica-paas\",\"versionName\":\"vvr-6.0 .0-flink- 1.15\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.15\"},\"parallelism\":1,\"ba hMode\":false,\"resources\":{\"jobmanager\": {\"memory\":\"4Gi\",\"cpu\":2.0},\"taskmanager\": {\"memory\":\"4Gi\",\"cpu\":2.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfig ation\":{\"execution.checkpointing.interval\":\"180s\",\"execution.checkpointing.min-pa use\":\"180s\"}}},\"restoreStrategy\": {\"kind\":\"LATEST_STATE\",\"allowNonRestoredState\":false},\"state\":\"RUNNING\",\"upgra Strategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"dep ymentTargetId\":\"f2ed6708-a7e1-4e86-a99e-327fac9265c2\"},\"status\": {\"startTime\":0,\"state\":\"RUNNING\",\"endTime\":0}}",
 "success":true,
 "requestId":"BCC13432-238D-41D7-B0A6-582241A6B572"
```

`}` `XML` format

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2024-03- 12T06:12:17Z&quot;,&quot;modifiedAt&quot;:&quot;2024-03- 12T06:44:00.823323Z&quot;,&quot;resourceVersion&quot;:15,&quot;name&quot;:&quot;sqljob&qu ;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;229852610122763813&quot;,&quot;resourceplan.has.migrated&quot;:&quot;true&quot;,&quot;deployment.has.deployed&quot;:&quot;false& ot;,&quot;deployment.sourcetype&quot;:&quot;EDITOR&quot;,&quot;deployment.parent.id&quot;:&quot;&quot;,&quot;modifie quot;:&quot;229852610122763813&quot;,&quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot riority&quot;:&quot;5&quot;,&quot;priority.class.name&quot;:&quot;&quot;,&quot;autopilot. de&quot;:&quot;monitor&quot;,&quot;com.dataartisans.appmanager.controller.deployment.spec ersion&quot;:&quot;3&quot;,&quot;deployment.referenced.deployment.draft.history.version&q t;:&quot;1&quot;,&quot;x-namespace-owner-masteruid&quot;:&quot;1052910122729909&quot;,&quot;default.resourcesetting.has.migrated&quot;:&quot;true&quot;,&quot;deployment.execplan.uri&quot;:&quot;hdfs:///vvp/data/plan/namespaces/flinkteam/deployment/d0b3abf0-4bf e-46b1-a324- 5b7def580c00/execPlan.json&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&q t;c6f157ac-60b9-4b38-8badd435387cfd59&quot;,&quot;comment&quot;:&quot;&quot;,&quot;modifierName&quot;:&quot;flinka in&quot;,&quot;taker&quot;:&quot;default-cluster | 0&quot;,&quot;deployment.referenced.deployment.draft.history.id&quot;:&quot;1fbfefd4-9b 1c-4e94-b6ad- 268a5c6b64cd&quot;},&quot;workspaceName&quot;:&quot;default&quot;,&quot;id&quot;:&quot;d0 abf0-4bfe-46b1-a324-5b7def580c00&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;s c&quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;:{&quot;fli nk.resource.type&quot;:&quot;auto&quot;,&quot;job.resource.total.memory.byte&quot;:&quot; 89934592&quot;,&quot;job.resource.total.cpu&quot;:&quot;4.0&quot;,&quot;native.kubernetes ode&quot;:&quot;true&quot;,&quot;flink.queryablestate.enabled&quot;:&quot;false&quot;}},&quot;spec&quot;:{&quot;artifact&quot;:{&quot;f linkImageTag&quot;:&quot;1.15.0-vvr-6.0.7- 29&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;--*********
***********************************************************---- Author:         Write yo
ur name here-- Created Time: 2024-03-12 14:11:38-- Description: Write your description here--********************************************************************- -CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)with ( \u0027connector\u0027 \u003d \u0027datagen\u0027 );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( \u0027connector\u0027 \u003d \u00 27print\u0027 );INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, C AST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&q t;cn-qingdao-env17e-d01-reg.docker.intra.env17e.shuguang.com:80/ververica-paas&quot;,&q uot;versionName&quot;:&quot;vvr-6.0.0-flink- 1.15&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quo 1.15&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;: {&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:2.0},&quot;taskmanager&quot;:{&quot ;memory&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:2.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&q t;default&quot;},&quot;flinkConfiguration&quot;:
```

```xml
{&quot;execution.checkpointing.interval&quot;:&quot;180s&quot;,&quot;execution.checkpoint g.min-pause&quot;:&quot;180s&quot;}}},&quot;restoreStrategy&quot;: {&quot;kind&quot;:&quot;LATEST_STATE&quot;,&quot;allowNonRestoredState&quot;:false},&quot tate&quot;:&quot;RUNNING&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJ CreationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;f2ed6708-a7e1-4e86-a99e-3 27fac9265c2&quot;},&quot;status&quot;: {&quot;startTime&quot;:0,&quot;state&quot;:&quot;RUNNING&quot;,&quot;endTime&quot;:0}}< /data> <success>true</success> <requestId>BCC13432-238D-41D7-B0A6-582241A6B572</requestId>
```

##### 3.1.2.11 ParseFormat

Call ParseFormat to parse a format.

**Request headers**

This API uses common request headers and requires no special request headers. For more information, see the Common Request Parameter document.

**Syntax**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats:analyze-jar s HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call ListNamespaces to obtain the ID. View the workspace details in the Realtime Compute for Apache Flink fully managed development console. |
| paramsJso n | Strin g | Body | No | { "jarUris": [ "http://flink- resource.oss-cn-wulan- env**-d01- a.intra.env**.shuguang.c om/format/customized- csv-demo-1.0- SNAPSHOT.jar" ] } | The list of format JAR packages to parse. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| data | String | { "duplicatedSinkFac toriesFormats": [], "formats": [], "@type": "type.googleapis.c om/vvp.sql.v1beta 1.AnalyzeFormatJar sResponse", "duplicatedFilesyst emFormatFactories Formats": [], "duplicatedSourceF actoriesFormats": [] } | The details of the format parsing result. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

**Examples**

Sample request

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats:analyze-jar s HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam"
```

`}` Sample success response `JSON` format `{`

```json
 "data":"{\"duplicatedSinkFactoriesFormats\":[],\"formats\":
[],\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.AnalyzeFormatJarsResponse\",\"duplicat FilesystemFormatFactoriesFormats\":[],\"duplicatedSourceFactoriesFormats\":[]}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
```

`}` `XML` format

```xml
<data>{&quot;duplicatedSinkFactoriesFormats&quot;:[],&quot;formats&quot;: [],&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.AnalyzeFormatJarsResponse& ot;,&quot;duplicatedFilesystemFormatFactoriesFormats&quot;: [],&quot;duplicatedSourceFactoriesFormats&quot;:[]}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

##### 3.1.2.12 ParseConnector

Call ParseConnector to customize connector parsing.

**Request headers**

This API uses common request headers and requires no special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors:analyzejars HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call the ListNamespaces operation to obtain the ID. View the workspace details in the Realtime Compute for Apache Flink fully managed console. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| paramsJso n | Strin g | Body | No | {"jarUris": ["http://flink- resource.oss-cn-wulan- env**-d01- a.intra.env**.shuguang.c om/connectors/ververica -connector-hologres- 1.15-vvr-6.0-fix.jar"]} | The list of custom connector JAR package paths to parse. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |

**Response data**

| success | Boolean | true | Indicates whether the request is successful. |
|---|---|---|---|
|   |   | {"connectors": [{"lookup":false,"s upportedFormats": [],"environments": [],"sink":true,"nam e":"namespaces/fli nkteam/connectors /hologres- fix","source":true,"t ype":"hologres- fix","properties": [{"defaultValue":"1 0","description":""," definesFormat":fals e,"key":"poolsize"," required":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"async", "required":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"cacheReloa dTimeBlackList","re quired":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"password","r equired":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"bhclien tignorebeforeupdat e","required":false }, {"defaultValue":"1 000","description": "","definesFormat": |   |

|   |   | false,"key":"jdbcret rysleepinitms","req uired":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"insertif notexists","require d":false}, {"defaultValue":"2 56","description":"" ,"definesFormat":fa lse,"key":"jdbcscan fetchsize","require d":false}, {"defaultValue":"- 1","description":""," definesFormat":fals e,"key":"starttime ms","required":fals e}, {"defaultValue":"tr ue","description":"" ,"definesFormat":fa lse,"key":"jdbcenab ledefaultfornotnullc olumn","required":f alse}, |   |
|---|---|---|---|
|   |   | {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"binlog", "required":false}, {"defaultValue":"1 00","description":"" ,"definesFormat":fa lse,"key":"binlogba tchreadsize","requi red":false}, {"defaultValue":"5 00","description":"" ,"definesFormat":fa lse,"key":"clientma xpause","required" :false}, {"defaultValue":"2" ,"description":"","d efinesFormat":false ,"key":"errorcount" ,"required":false}, {"defaultValue":"2 56","description":"" ,"definesFormat":fa lse,"key":"jdbcwrite batchsize","require d":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"jdbcuse legacyputhandler", "required":false}, {"defaultValue":"1 28","description":"" ,"definesFormat":fa lse,"key":"jdbcread |   |

|   |   | batchsize","require d":false}, {"defaultValue":"4" ,"description":"","d efinesFormat":false ,"key":"bhclientthr eadpool","required ":false}, {"defaultValue":"1" ,"description":"","d efinesFormat":false ,"key":"jdbcreadret rycount","required" :false}, {"defaultValue":"1 00000","descriptio n":"","definesForm at":false,"key":"cac heSize","required": false}, {"defaultValue":"1 0000","description" :"","definesFormat" :false,"key":"maxin queue","required":f alse}, {"defaultValue":"1 00000","descriptio n":"","definesForm at":false,"key":"ma xRowCount","requi red":false}, {"defaultValue":"6 00000","descriptio n":"","definesForm at":false,"key":"bhc lientasynctimeout", "required":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"enable _ direct connect","re _ quired":false}, {"defaultValue":"1 00","description":"" ,"definesFormat":fa lse,"key":"rpcreque steveryfailures","re quired":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"usebhcl ientmode","require d":false}, {"defaultValue":"tr ue","description":"" ,"definesFormat":fa lse,"key":"enableth rottle","required":f alse}, {"defaultValue":"3" ,"description":"","d efinesFormat":false ,"key":"connection |   |
|---|---|---|---|

|   |   | size","required":fal se}, {"defaultValue":"0" ,"description":"","d efinesFormat":false ,"key":"jdbcreadti meoutms","require d":false}, {"defaultValue":"1 0","description":""," definesFormat":fals e,"key":"jdbcretryc ount","required":fal se}, {"defaultValue":"E xception","descript ion":"","definesFor mat":false,"key":"a ctiononinsert","req uired":false}, {"defaultValue":"h ologres- fix","description":"" ,"definesFormat":fa lse,"key":"connect or","required":true }, {"defaultValue":"", "description":"","de finesFormat":false, "key":"username"," required":false}, {"defaultValue":"1 0","description":""," definesFormat":fals e,"key":"bhclientre aderqueue","requir ed":false}, {"defaultValue":"1" ,"description":"","d efinesFormat":false ,"key":"maxconcurr encypershard","req uired":false}, {"defaultValue":"2 048","description": "","definesFormat": false,"key":"bhclien tasyncqueue","req uired":false}, {"defaultValue":"\\ u0002","descriptio n":"","definesForm at":false,"key":"arr aydelimiter","requi red":false}, {"defaultValue":"2" ,"description":"","d efinesFormat":false ,"key":"bhclientwrit erbatch","required" :false}, {"defaultValue":"1 000","description": "","definesFormat": false,"key":"sqlretr |   |
|---|---|---|---|

|   |   | yinterval","require d":false}, {"defaultValue":"9 0000","description" :"","definesFormat" :false,"key":"bhclie nttimeout","require d":false}, {"defaultValue":"2 097152","descripti on":"","definesFor mat":false,"key":"j dbcwritebatchbyte size","required":fal se}, {"defaultValue":"1 000","description": "","definesFormat": false,"key":"binlogr etryintervalms","re quired":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"fieldna metolower","requir ed":false}, {"defaultValue":"tr ue","description":"" ,"definesFormat":fa lse,"key":"ignorede lete","required":fal se}, {"defaultValue":"6 0000","description" :"","definesFormat" :false,"key":"storer pctimeout","requir ed":false}, {"defaultValue":"d efault","description ":"","definesFormat ":false,"key":"resou rce group","requir _ ed":false}, {"defaultValue":"1 00","description":"" ,"definesFormat":fa lse,"key":"clientpa use","required":fals e}, {"defaultValue":"in sertOrIgnore","des cription":"","define sFormat":false,"ke y":"mutatetype","r equired":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"disable binlog","required":f alse}, {"defaultValue":"A LL","description":"" ,"definesFormat":fa |   |
|---|---|---|---|

| data | String | lse,"key":"cache","r equired":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"sink.paralleli sm","required":fals e}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"jdbcbinlogsl otname","required" :false}, {"defaultValue":"1 00","description":"" ,"definesFormat":fa lse,"key":"asyncca pacity","required":f alse}, {"defaultValue":"1 00","description":"" ,"definesFormat":fa lse,"key":"cacheSc anLimit","required" :false}, {"defaultValue":"2 0971520","descript ion":"","definesFor mat":false,"key":"j dbcwritebatchtotal bytesize","required ":false}, {"defaultValue":"5" ,"description":"","d efinesFormat":false ,"key":"rpcretries"," required":false}, {"defaultValue":"1 024","description": "","definesFormat": false,"key":"bhclien treaderbatch","req uired":false}, {"defaultValue":"6 0000","description" :"","definesFormat" :false,"key":"jdbcm etacachettl","requi red":false}, {"defaultValue":"tr ue","description":"" ,"definesFormat":fa lse,"key":"splitstrat egy","required":fal se}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"partitio nrouter","required" :false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"connectionp | Custom connector parsing details. |
|---|---|---|---|

|   |   | oolname","required ":false}, {"defaultValue":"6 0000","description" :"","definesFormat" :false,"key":"jdbcco nnectionmaxidlems ","required":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"dbname","r equired":true}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"enablet ypenormalization", "required":false}, {"defaultValue":"2 62144","descriptio n":"","definesForm at":false,"key":"spli tdatasize","require d":false}, {"defaultValue":"6 0000","description" :"","definesFormat" :false,"key":"binlog requesttimeoutms" ,"required":false}, {"defaultValue":"3 2","description":""," definesFormat":fals e,"key":"splitlength ","required":false}, {"defaultValue":"1 80000","descriptio n":"","definesForm at":false,"key":"asy nctimeoutms","req uired":false}, {"defaultValue":"bi nary","description" :"","definesFormat" :false,"key":"jdbcco pyformat","require d":false}, {"defaultValue":"5 000","description": "","definesFormat": false,"key":"jdbcret rysleepstepms","re quired":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"userpcmode ","required":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"cdcmod e","required":false }, {"defaultValue":"tr |   |
|---|---|---|---|

|   |   | ue","description":"" ,"definesFormat":fa lse,"key":"enableBi naryCache","requir ed":false}, {"defaultValue":"1 0000","description" :"","definesFormat" :false,"key":"jdbcw riteflushinterval","r equired":false}, {"defaultValue":"1 00","description":"" ,"definesFormat":fa lse,"key":"shardrpc retries","required": false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"partial- insert.enabled","re quired":false}, {"defaultValue":"6 0","description":""," definesFormat":fals e,"key":"jdbcscanti meoutseconds","re quired":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"insertor update","required": false}, {"defaultValue":"1 000","description": "","definesFormat": false,"key":"scanba tchsize","required": false}, {"defaultValue":"1" ,"description":"","d efinesFormat":false ,"key":"asynccallba ckpool","required": false}, {"defaultValue":":", "description":"","de finesFormat":false, "key":"primarykeys ep","required":fals e}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"createp arttable","required ":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"report metrics","required" :false}, {"defaultValue":"", |   |
|---|---|---|---|

|   |   | "description":"","de finesFormat":false, "key":"starttime","r equired":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"useholo hubmode","require d":false}, {"defaultValue":"u nordered","descrip tion":"","definesFor mat":false,"key":"a syncresultorder","r equired":false}, {"defaultValue":"2 56","description":"" ,"definesFormat":fa lse,"key":"jdbcread batchqueuesize","r equired":false}, {"defaultValue":"- 1","description":""," definesFormat":fals e,"key":"jdbcmetaa utorefreshfactor","r equired":false}, {"defaultValue":"1 0","description":""," definesFormat":fals e,"key":"binlogmax retrytimes","requir ed":false}, {"defaultValue":"n one","description": "","definesFormat": false,"key":"sdkmo de","required":fals e}, {"defaultValue":"9 223372036854775 807","description": "","definesFormat": false,"key":"cacheT TLMs","required":fa lse}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"upserts ource","required":f alse}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"bhclien tignoredelete","req uired":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"remove -u0000-in- text.enabled","req uired":false}, |   |
|---|---|---|---|

|   |   | {"defaultValue":"e arliestOffset","desc ription":"","defines Format":false,"key" :"binlogstartupmod e","required":false }, {"defaultValue":"1 00","description":"" ,"definesFormat":fa lse,"key":"sqlretrie s","required":false} , {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"support columnstorageform at","required":false }, {"defaultValue":"1 0","description":""," definesFormat":fals e,"key":"channelthr eadcount","require d":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"ignoren ullwhenupdate","re quired":false}, {"defaultValue":"st ream","description ":"","definesFormat ":false,"key":" tab __ lename ","require __ d":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"nullvalues"," required":false}, {"defaultValue":"", "description":"","de finesFormat":false, "key":"endpoint","r equired":true}, {"defaultValue":"1 0000","description" :"","definesFormat" :false,"key":"refres hinterval","require d":false}, {"defaultValue":"\\ u0002","descriptio n":"","definesForm at":false,"key":"fiel d delimiter","requir _ ed":false}, {"defaultValue":"fa lse","description":" ","definesFormat":f alse,"key":"enable _ filter push down"," _ _ required":false}, |   |
|---|---|---|---|

|   |   | {"defaultValue":"", "description":"","de finesFormat":false, "key":"tablename", "required":true}, {"defaultValue":"tr ue","description":"" ,"definesFormat":fa lse,"key":"cacheEm pty","required":fals e}, {"defaultValue":"p ublic","description" :"","definesFormat" :false,"key":"schem aname","required": false}, {"defaultValue":"6 00","description":"" ,"definesFormat":fa lse,"key":"jdbcscan transactionsessiont imeoutseconds","r equired":false}],"p ackaged":false,"de pendencies": ["hdfs:///vvp/data/s ql- artifacts/namespac es/flinkteam/custo m- connectors/2024- 03-12T01-50- 56.079896Z/verver ica-connector- hologres-1.15-vvr- 6.0- fix.jar"]}],"@type":" |   |
|---|---|---|---|
| requestId | String | type.googleapis.co m05/AvvEpE.As6q0l.-v81Bb5e9ta-1. A4CnaClDyz-9eFC3o5n-nectorJ aBr2s7REeEs4p7oFn4sDe"4,E"dupl icatedSourceFactor | The request ID. |

iesConnectors":

**Examples**

[],"duplicatedSinkF actoriesConnectors Sample request ":[]}

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors:analyzejars HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam"
```

`}` Sample success response `JSON` format `{`

```json
 "data":"{\"connectors\":[{\"lookup\":false,\"supportedFormats\":[],\"environments\":[]
,\"sink\":true,\"name\":\"namespaces/flinkteam/connectors/hologresfix\",\"source\":true,\"type\":\"hologres-fix\",\"properties\":
```

```
fix\,\source\:true,\type\:\hologresfix\,\properties\: [{\"defaultValue\":\"10\",\"description\":\"\",\"definesFormat\":false,\"key\":\"poolsize ,\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"async\ \"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"cacheReload meBlackList\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"password\", required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclie ignorebeforeupdate\",\"required\":false}, {\"defaultValue\":\"1000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcret sleepinitms\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"insert notexists\",\"required\":false}, {\"defaultValue\":\"256\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcscan tchsize\",\"required\":false},{\"defaultValue\":\"- 1\",\"description\":\"\",\"definesFormat\":false,\"key\":\"starttimems\",\"required\":fal
```

`},`

```
{\"defaultValue\":\"true\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcena edefaultfornotnullcolumn\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"binlog ,\"required\":false}, {\"defaultValue\":\"100\",\"description\":\"\",\"definesFormat\":false,\"key\":\"binlogba hreadsize\",\"required\":false}, {\"defaultValue\":\"500\",\"description\":\"\",\"definesFormat\":false,\"key\":\"clientma ause\",\"required\":false}, {\"defaultValue\":\"2\",\"description\":\"\",\"definesFormat\":false,\"key\":\"errorcount ,\"required\":false}, {\"defaultValue\":\"256\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcwrit atchsize\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcus egacyputhandler\",\"required\":false}, {\"defaultValue\":\"128\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcread tchsize\",\"required\":false}, {\"defaultValue\":\"4\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclientth adpool\",\"required\":false}, {\"defaultValue\":\"1\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcreadre ycount\",\"required\":false}, {\"defaultValue\":\"100000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"cache ze\",\"required\":false}, {\"defaultValue\":\"10000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"maxinq ue\",\"required\":false}, {\"defaultValue\":\"100000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"maxRo ount\",\"required\":false}, {\"defaultValue\":\"600000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhcli tasynctimeout\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"enable irect_connect\",\"required\":false}, {\"defaultValue\":\"100\",\"description\":\"\",\"definesFormat\":false,\"key\":\"rpcreque everyfailures\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"usebhc entmode\",\"required\":false}, {\"defaultValue\":\"true\",\"description\":\"\",\"definesFormat\":false,\"key\":\"enablet ottle\",\"required\":false},
```

`,` `q` `,`

```
{\"defaultValue\":\"3\",\"description\":\"\",\"definesFormat\":false,\"key\":\"connection ze\",\"required\":false}, {\"defaultValue\":\"0\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcreadti outms\",\"required\":false}, {\"defaultValue\":\"10\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcretry unt\",\"required\":false}, {\"defaultValue\":\"Exception\",\"description\":\"\",\"definesFormat\":false,\"key\":\"ac ononinsert\",\"required\":false},{\"defaultValue\":\"hologresfix\",\"description\":\"\",\"definesFormat\":false,\"key\":\"connector\",\"required\":tru
```

`,`

```
{\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"username\", required\":false}, {\"defaultValue\":\"10\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclientr derqueue\",\"required\":false}, {\"defaultValue\":\"1\",\"description\":\"\",\"definesFormat\":false,\"key\":\"maxconcurr cypershard\",\"required\":false}, {\"defaultValue\":\"2048\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclien syncqueue\",\"required\":false}, {\"defaultValue\":\"\\\\u0002\",\"description\":\"\",\"definesFormat\":false,\"key\":\"ar ydelimiter\",\"required\":false}, {\"defaultValue\":\"2\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclientwr erbatch\",\"required\":false}, {\"defaultValue\":\"1000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"sqlretr nterval\",\"required\":false}, {\"defaultValue\":\"90000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclie timeout\",\"required\":false}, {\"defaultValue\":\"2097152\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbc itebatchbytesize\",\"required\":false}, {\"defaultValue\":\"1000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"binlogr ryintervalms\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"fieldn etolower\",\"required\":false}, {\"defaultValue\":\"true\",\"description\":\"\",\"definesFormat\":false,\"key\":\"ignored ete\",\"required\":false}, {\"defaultValue\":\"60000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"storer timeout\",\"required\":false}, {\"defaultValue\":\"default\",\"description\":\"\",\"definesFormat\":false,\"key\":\"reso ce_group\",\"required\":false}, {\"defaultValue\":\"100\",\"description\":\"\",\"definesFormat\":false,\"key\":\"clientpa e\",\"required\":false}, {\"defaultValue\":\"insertOrIgnore\",\"description\":\"\",\"definesFormat\":false,\"key\" "mutatetype\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"disabl inlog\",\"required\":false}, {\"defaultValue\":\"ALL\",\"description\":\"\",\"definesFormat\":false,\"key\":\"cache\", required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"sink.parall ism\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcbinlogs tname\",\"required\":false}, {\"defaultValue\":\"100\",\"description\":\"\",\"definesFormat\":false,\"key\":\"asynccap ity\",\"required\":false}, {\"defaultValue\":\"100\",\"description\":\"\",\"definesFormat\":false,\"key\":\"cacheSca imit\",\"required\":false},
```

```
{\"defaultValue\":\"20971520\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdb ritebatchtotalbytesize\",\"required\":false}, {\"defaultValue\":\"5\",\"description\":\"\",\"definesFormat\":false,\"key\":\"rpcretries ,\"required\":false}, {\"defaultValue\":\"1024\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclien eaderbatch\",\"required\":false}, {\"defaultValue\":\"60000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcme cachettl\",\"required\":false}, {\"defaultValue\":\"true\",\"description\":\"\",\"definesFormat\":false,\"key\":\"splitst tegy\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"partit nrouter\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"connectionp lname\",\"required\":false}, {\"defaultValue\":\"60000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcco ectionmaxidlems\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"dbname\",\" quired\":true}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"enable penormalization\",\"required\":false}, {\"defaultValue\":\"262144\",\"description\":\"\",\"definesFormat\":false,\"key\":\"split tasize\",\"required\":false}, {\"defaultValue\":\"60000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"binlog questtimeoutms\",\"required\":false}, {\"defaultValue\":\"32\",\"description\":\"\",\"definesFormat\":false,\"key\":\"splitleng \",\"required\":false}, {\"defaultValue\":\"180000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"async meoutms\",\"required\":false}, {\"defaultValue\":\"binary\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcc yformat\",\"required\":false}, {\"defaultValue\":\"5000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcret sleepstepms\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"userpcmode\ \"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"cdcmod ",\"required\":false}, {\"defaultValue\":\"true\",\"description\":\"\",\"definesFormat\":false,\"key\":\"enableB aryCache\",\"required\":false}, {\"defaultValue\":\"10000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcwr eflushinterval\",\"required\":false}, {\"defaultValue\":\"100\",\"description\":\"\",\"definesFormat\":false,\"key\":\"shardrpc tries\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"partia insert.enabled\",\"required\":false}, {\"defaultValue\":\"60\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcscant eoutseconds\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"insert update\",\"required\":false}, {\"defaultValue\":\"1000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"scanbat size\",\"required\":false}, {\"defaultValue\":\"1\",\"description\":\"\",\"definesFormat\":false,\"key\":\"asynccallb kpool\",\"required\":false}, {\"defaultValue\":\":\",\"description\":\"\",\"definesFormat\":false,\"key\":\"primarykey p\",\"required\":false},
```

```
{\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"create rttable\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"report trics\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"starttime\" "required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"usehol ubmode\",\"required\":false}, {\"defaultValue\":\"unordered\",\"description\":\"\",\"definesFormat\":false,\"key\":\"as cresultorder\",\"required\":false}, {\"defaultValue\":\"256\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcread tchqueuesize\",\"required\":false},{\"defaultValue\":\"- 1\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcmetaautorefreshfactor\",\" quired\":false}, {\"defaultValue\":\"10\",\"description\":\"\",\"definesFormat\":false,\"key\":\"binlogmax trytimes\",\"required\":false}, {\"defaultValue\":\"none\",\"description\":\"\",\"definesFormat\":false,\"key\":\"sdkmode ,\"required\":false}, {\"defaultValue\":\"9223372036854775807\",\"description\":\"\",\"definesFormat\":false,\" y\":\"cacheTTLMs\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"upsert urce\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"bhclie ignoredelete\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"remove u0000-in-text.enabled\",\"required\":false}, {\"defaultValue\":\"earliestOffset\",\"description\":\"\",\"definesFormat\":false,\"key\" "binlogstartupmode\",\"required\":false}, {\"defaultValue\":\"100\",\"description\":\"\",\"definesFormat\":false,\"key\":\"sqlretri \",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"suppor olumnstorageformat\",\"required\":false}, {\"defaultValue\":\"10\",\"description\":\"\",\"definesFormat\":false,\"key\":\"channelth adcount\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"ignore llwhenupdate\",\"required\":false}, {\"defaultValue\":\"stream\",\"description\":\"\",\"definesFormat\":false,\"key\":\"__tab name__\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"nullvalues\ \"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"endpoint\", required\":true}, {\"defaultValue\":\"10000\",\"description\":\"\",\"definesFormat\":false,\"key\":\"refres nterval\",\"required\":false}, {\"defaultValue\":\"\\\\u0002\",\"description\":\"\",\"definesFormat\":false,\"key\":\"fi d_delimiter\",\"required\":false}, {\"defaultValue\":\"false\",\"description\":\"\",\"definesFormat\":false,\"key\":\"enable ilter_push_down\",\"required\":false}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"tablename\" "required\":true}, {\"defaultValue\":\"true\",\"description\":\"\",\"definesFormat\":false,\"key\":\"cacheEm y\",\"required\":false}, {\"defaultValue\":\"public\",\"description\":\"\",\"definesFormat\":false,\"key\":\"schem ame\",\"required\":false}, {\"df ltVl \"\"600\"\"d iti \"\"\"\"dfi
```

`F`

```
t\"fl \"k \"\"jdb
```

```json
{\"defaultValue\":\"600\",\"description\":\"\",\"definesFormat\":false,\"key\":\"jdbcscan ansactionsessiontimeoutseconds\",\"required\":false}],\"packaged\":false,\"dependencies\" [\"hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/custom-connectors/2024-03-12T01- 50-56.079896Z/ververica-connector-hologres-1.15-vvr-6.0fix.jar\"]}],\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.AnalyzeConnectorJarsResponse ,\"duplicatedSourceFactoriesConnectors\":[],\"duplicatedSinkFactoriesConnectors\":[]}",
 "success":true,
 "requestId":"05AEEA60-8B59-4CCD-9F35-B27EE47F4D4E"
```

`}` `XML` format

```xml
<data>{&quot;connectors&quot;:[{&quot;lookup&quot;:false,&quot;supportedFormats&quot;:[ ],&quot;environments&quot;: [],&quot;sink&quot;:true,&quot;name&quot;:&quot;namespaces/flinkteam/connectors/hologresfix&quot;,&quot;source&quot;:true,&quot;type&quot;:&quot;hologresfix&quot;,&quot;properties&quot;: [{&quot;defaultValue&quot;:&quot;10&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;poolsize&quot;,&quot;required&quot;:false},{& quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;async&quot;,&quot;required&quot;:false},{&quo t;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesForma quot;:false,&quot;key&quot;:&quot;cacheReloadTimeBlackList&quot;,&quot;required&quot;:fal
```

`},`

```
{&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;password&quot;,&quot;required&quot;:false},{&quo t;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;bhclientignorebeforeupdate&quot;,&quot;required&qu ;:false}, {&quot;defaultValue&quot;:&quot;1000&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;jdbcretrysleepinitms&quot;,&quot;required&quot false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;insertifnotexists&quot;,&quot;required&quot;: lse}, {&quot;defaultValue&quot;:&quot;256&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;jdbcscanfetchsize&quot;,&quot;required&quot;:fa e},{&quot;defaultValue&quot;:&quot;- 1&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFormat&quot;:false,&quot;key&qu ;:&quot;starttimems&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;true&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;jdbcenabledefaultfornotnullcolumn&quot;,&quot; quired&quot;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;binlog&quot;,&quot;required&quot;:false},{& quot;defaultValue&quot;:&quot;100&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;binlogbatchreadsize&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;500&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;clientmaxpause&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;2&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;errorcount&quot;,&quot;required&quot;:false},{& quot;defaultValue&quot;:&quot;256&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;jdbcwritebatchsize&quot;,&quot;required&quot;:fal
```

`},`

```
{&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;jdbcuselegacyputhandler&quot;,&quot;required& ot;:false}, {&quot;defaultValue&quot;:&quot;128&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;jdbcreadbatchsize&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;4&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;bhclientthreadpool&quot;,&quot;required&quot;:fal
```

`},`

```
{&quot;defaultValue&quot;:&quot;1&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;jdbcreadretrycount&quot;,&quot;required&quot;:fal
```

`},`

```
{&quot;defaultValue&quot;:&quot;100000&quot;,&quot;description&quot;:&quot;&quot;,&quot;d inesFormat&quot;:false,&quot;key&quot;:&quot;cacheSize&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;10000&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;maxinqueue&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;100000&quot;,&quot;description&quot;:&quot;&quot;,&quot;d inesFormat&quot;:false,&quot;key&quot;:&quot;maxRowCount&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;600000&quot;,&quot;description&quot;:&quot;&quot;,&quot;d inesFormat&quot;:false,&quot;key&quot;:&quot;bhclientasynctimeout&quot;,&quot;required&qu ;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;enable_direct_connect&quot;,&quot;required&qu ;:false}, {&quot;defaultValue&quot;:&quot;100&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;rpcrequesteveryfailures&quot;,&quot;required&qu ;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;usebhclientmode&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;true&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;enablethrottle&quot;,&quot;required&quot;:fals
```

`,`

```
{&quot;defaultValue&quot;:&quot;3&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;connectionsize&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;0&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;jdbcreadtimeoutms&quot;,&quot;required&quot;:fals
```

`,`

```
{&quot;defaultValue&quot;:&quot;10&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;jdbcretrycount&quot;,&quot;required&quot;:false} {&quot;defaultValue&quot;:&quot;Exception&quot;,&quot;description&quot;:&quot;&quot;,&quo definesFormat&quot;:false,&quot;key&quot;:&quot;actiononinsert&quot;,&quot;required&quot; alse},{&quot;defaultValue&quot;:&quot;hologresfix&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFormat&quot;:false,&quot;key& ot;:&quot;connector&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;username&quot;,&quot;required&quot;:false},{&quo t;defaultValue&quot;:&quot;10&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFor t&quot;:false,&quot;key&quot;:&quot;bhclientreaderqueue&quot;,&quot;required&quot;:false} {&quot;defaultValue&quot;:&quot;1&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;maxconcurrencypershard&quot;,&quot;required&quot; alse}, {&quot;defaultValue&quot;:&quot;2048&quot;,&quot;description&quot;:&quot;&quot;,&quot;def
```

```
esFormat&quot;:false,&quot;key&quot;:&quot;bhclientasyncqueue&quot;,&quot;required&quot;: lse}, {&quot;defaultValue&quot;:&quot;\\u0002&quot;,&quot;description&quot;:&quot;&quot;,&quot; finesFormat&quot;:false,&quot;key&quot;:&quot;arraydelimiter&quot;,&quot;required&quot;:f se}, {&quot;defaultValue&quot;:&quot;2&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;bhclientwriterbatch&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;1000&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;sqlretryinterval&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;90000&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;bhclienttimeout&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;2097152&quot;,&quot;description&quot;:&quot;&quot;,&quot; finesFormat&quot;:false,&quot;key&quot;:&quot;jdbcwritebatchbytesize&quot;,&quot;required uot;:false}, {&quot;defaultValue&quot;:&quot;1000&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;binlogretryintervalms&quot;,&quot;required&quo :false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;fieldnametolower&quot;,&quot;required&quot;:f se}, {&quot;defaultValue&quot;:&quot;true&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;ignoredelete&quot;,&quot;required&quot;:false} {&quot;defaultValue&quot;:&quot;60000&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;storerpctimeout&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;default&quot;,&quot;description&quot;:&quot;&quot;,&quot; finesFormat&quot;:false,&quot;key&quot;:&quot;resource_group&quot;,&quot;required&quot;:f se}, {&quot;defaultValue&quot;:&quot;100&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;clientpause&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;insertOrIgnore&quot;,&quot;description&quot;:&quot;&quot; quot;definesFormat&quot;:false,&quot;key&quot;:&quot;mutatetype&quot;,&quot;required&quot false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;disablebinlog&quot;,&quot;required&quot;:fals
```

`,`

```
{&quot;defaultValue&quot;:&quot;ALL&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;cache&quot;,&quot;required&quot;:false},{&quo t;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesForma quot;:false,&quot;key&quot;:&quot;sink.parallelism&quot;,&quot;required&quot;:false},{& quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFo at&quot;:false,&quot;key&quot;:&quot;jdbcbinlogslotname&quot;,&quot;required&quot;:false} {&quot;defaultValue&quot;:&quot;100&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;asynccapacity&quot;,&quot;required&quot;:false} {&quot;defaultValue&quot;:&quot;100&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;cacheScanLimit&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;20971520&quot;,&quot;description&quot;:&quot;&quot;,&quot efinesFormat&quot;:false,&quot;key&quot;:&quot;jdbcwritebatchtotalbytesize&quot;,&quot;re ired&quot;:false}, {&quot;defaultValue&quot;:&quot;5&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;rpcretries&quot;,&quot;required&quot;:false},{& quot;defaultValue&quot;:&quot;1024&quot;&quot;description&quot;:&quot;&quot;&quot;defin
```

```
quot;defaultValue&quot;:&quot;1024&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;bhclientreaderbatch&quot;,&quot;required&quot;:f se}, {&quot;defaultValue&quot;:&quot;60000&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;jdbcmetacachettl&quot;,&quot;required&quot;:f se}, {&quot;defaultValue&quot;:&quot;true&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;splitstrategy&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;partitionrouter&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;connectionpoolname&quot;,&quot;required&quot;:fals
```

`,`

```
{&quot;defaultValue&quot;:&quot;60000&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;jdbcconnectionmaxidlems&quot;,&quot;required& ot;:false}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;dbname&quot;,&quot;required&quot;:true},{&quot;d efaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFor t&quot;:false,&quot;key&quot;:&quot;enabletypenormalization&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;262144&quot;,&quot;description&quot;:&quot;&quot;,&quot;d inesFormat&quot;:false,&quot;key&quot;:&quot;splitdatasize&quot;,&quot;required&quot;:fal
```

`},`

```
{&quot;defaultValue&quot;:&quot;60000&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;binlogrequesttimeoutms&quot;,&quot;required&q t;:false}, {&quot;defaultValue&quot;:&quot;32&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;splitlength&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;180000&quot;,&quot;description&quot;:&quot;&quot;,&quot;d inesFormat&quot;:false,&quot;key&quot;:&quot;asynctimeoutms&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;binary&quot;,&quot;description&quot;:&quot;&quot;,&quot;d inesFormat&quot;:false,&quot;key&quot;:&quot;jdbccopyformat&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;5000&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;jdbcretrysleepstepms&quot;,&quot;required&quot false}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;userpcmode&quot;,&quot;required&quot;:false},{&q uot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;cdcmode&quot;,&quot;required&quot;:false},{&qu ot;defaultValue&quot;:&quot;true&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;enableBinaryCache&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;10000&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;jdbcwriteflushinterval&quot;,&quot;required&q t;:false}, {&quot;defaultValue&quot;:&quot;100&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;shardrpcretries&quot;,&quot;required&quot;:fals
```

`,`

```
{&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;partialinsert.enabled&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;60&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin
```

```
{&quot;defaultValue&quot;:&quot;60&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;jdbcscantimeoutseconds&quot;,&quot;required&quot false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;insertorupdate&quot;,&quot;required&quot;:fal
```

`},`

```
{&quot;defaultValue&quot;:&quot;1000&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;scanbatchsize&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;1&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;asynccallbackpool&quot;,&quot;required&quot;:fals
```

`,`

```
{&quot;defaultValue&quot;:&quot;:&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;primarykeysep&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;createparttable&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;reportmetrics&quot;,&quot;required&quot;:fals
```

`,`

```
{&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;starttime&quot;,&quot;required&quot;:false},{&qu ot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;define ormat&quot;:false,&quot;key&quot;:&quot;useholohubmode&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;unordered&quot;,&quot;description&quot;:&quot;&quot;,&quo definesFormat&quot;:false,&quot;key&quot;:&quot;asyncresultorder&quot;,&quot;required&quo :false}, {&quot;defaultValue&quot;:&quot;256&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;jdbcreadbatchqueuesize&quot;,&quot;required&quo :false},{&quot;defaultValue&quot;:&quot;- 1&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFormat&quot;:false,&quot;key&qu ;:&quot;jdbcmetaautorefreshfactor&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;10&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;binlogmaxretrytimes&quot;,&quot;required&quot;:f se}, {&quot;defaultValue&quot;:&quot;none&quot;,&quot;description&quot;:&quot;&quot;,&quot;def esFormat&quot;:false,&quot;key&quot;:&quot;sdkmode&quot;,&quot;required&quot;:false},{& quot;defaultValue&quot;:&quot;9223372036854775807&quot;,&quot;description&quot;:&quot;&qu ;,&quot;definesFormat&quot;:false,&quot;key&quot;:&quot;cacheTTLMs&quot;,&quot;required&q t;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;upsertsource&quot;,&quot;required&quot;:false {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;bhclientignoredelete&quot;,&quot;required&quo :false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;remove-u0000-intext.enabled&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;earliestOffset&quot;,&quot;description&quot;:&quot;&quot; quot;definesFormat&quot;:false,&quot;key&quot;:&quot;binlogstartupmode&quot;,&quot;requir &quot;:false}, {&quot;defaultValue&quot;:&quot;100&quot;,&quot;description&quot;:&quot;&quot;,&quot;defi sFormat&quot;:false,&quot;key&quot;:&quot;sqlretries&quot;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;supportcolumnstorageformat&quot;,&quot;requir &quot;:false},
```

```
{&quot;defaultValue&quot;:&quot;10&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;channelthreadcount&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;ignorenullwhenupdate&quot;,&quot;required&quo :false}, {&quot;defaultValue&quot;:&quot;stream&quot;,&quot;description&quot;:&quot;&quot;,&quot;d inesFormat&quot;:false,&quot;key&quot;:&quot;__tablename__&quot;,&quot;required&quot;:fal
```

`},`

```xml
{&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;nullvalues&quot;,&quot;required&quot;:false},{&q uot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFor t&quot;:false,&quot;key&quot;:&quot;endpoint&quot;,&quot;required&quot;:true},{&quot;de faultValue&quot;:&quot;10000&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesForm &quot;:false,&quot;key&quot;:&quot;refreshinterval&quot;,&quot;required&quot;:false},{& quot;defaultValue&quot;:&quot;\\u0002&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;field_delimiter&quot;,&quot;required&quot;:fa e}, {&quot;defaultValue&quot;:&quot;false&quot;,&quot;description&quot;:&quot;&quot;,&quot;de nesFormat&quot;:false,&quot;key&quot;:&quot;enable_filter_push_down&quot;,&quot;required& ot;:false}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;tablename&quot;,&quot;required&quot;:true},{&quo t;defaultValue&quot;:&quot;true&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesF mat&quot;:false,&quot;key&quot;:&quot;cacheEmpty&quot;,&quot;required&quot;:false},{&qu ot;defaultValue&quot;:&quot;public&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;schemaname&quot;,&quot;required&quot;:false},{ &quot;defaultValue&quot;:&quot;600&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;jdbcscantransactionsessiontimeoutseconds&quot;,& ot;required&quot;:false}],&quot;packaged&quot;:false,&quot;dependencies&quot;:[&quot;hd fs:///vvp/data/sql-artifacts/namespaces/flinkteam/custom-connectors/2024-03-12T01-50-56 .079896Z/ververica-connector-hologres-1.15-vvr-6.0fix.jar&quot;]}],&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.AnalyzeConne orJarsResponse&quot;,&quot;duplicatedSourceFactoriesConnectors&quot;: [],&quot;duplicatedSinkFactoriesConnectors&quot;:[]}</data> <success>true</success> <requestId>05AEEA60-8B59-4CCD-9F35-B27EE47F4D4E</requestId>
```

##### 3.1.2.13 ListTables

Views catalog tables.

**Request headers**

The ListTables operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listTab s HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
| namespac e | Strin g | Path | Yes | ververica | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| cat | Strin g | Path | Yes | vvp | The catalog name. |
| database | Strin g | Quer y | Yes | default | The name of the database under the catalog. |
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | 202107221428- KKE3K857WS | The request ID. |

| data | String | {"tables": [{"name":"blackhol e","schema": {"column": [{"name":"id","typ e":"VARCHAR(2147 483647)","expressi on":""}],"watermar kSpec": []},"properties": {"connector":"blac khole"},"comment" :""}, {"name":"blackhol e sink","schema": _ {"column": [{"name":"name"," type":"VARCHAR(2 147483647)","expr ession":""}, {"name":"score","t ype":"BIGINT","exp ression":""}],"wate rmarkSpec": []},"properties": {"connector":"blac khole"},"comment" :"blackhole sink table"}]} | The detailed information. |
|---|---|---|---|

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listTab s HTTP/1.1 &workspace=default &namespace=ververica &cat=vvp &database=default &RegionId=cn-wulan-env***-d01 &Common Request Parameter
```

Sample success responses `JSON` format `{`

```json
 "data":"{\"tables\":[{\"name\":\"blackhole\",\"schema\":{\"column\":
[{\"name\":\"id\",\"type\":\"VARCHAR(2147483647)\",\"expression\":\"\"}],\"watermarkSpec\ []},\"properties\":{\"connector\":\"blackhole\"},\"comment\":\"\"}, {\"name\":\"blackhole_sink\",\"schema\":{\"column\": [{\"name\":\"name\",\"type\":\"VARCHAR(2147483647)\",\"expression\":\"\"}, {\"name\":\"score\",\"type\":\"BIGINT\",\"expression\":\"\"}],\"watermarkSpec\":[]},\"p roperties\":{\"connector\":\"blackhole\"},\"comment\":\"blackhole sink table\"}]}",
 "requestId":"202107221428-KKE3K857WS"
```

`}` `XML` format

```xml
<data>{&quot;tables&quot;:[{&quot;name&quot;:&quot;blackhole&quot;,&quot;schema&quot;:{ &quot;column&quot;: [{&quot;name&quot;:&quot;id&quot;,&quot;type&quot;:&quot;VARCHAR(2147483647)&quot;,&quot; pression&quot;:&quot;&quot;}],&quot;watermarkSpec&quot;:[]},&quot;properties&quot;:{&qu ot;connector&quot;:&quot;blackhole&quot;},&quot;comment&quot;:&quot;&quot;},{&quot;name &quot;:&quot;blackhole_sink&quot;,&quot;schema&quot;:{&quot;column&quot;: [{&quot;name&quot;:&quot;name&quot;,&quot;type&quot;:&quot;VARCHAR(2147483647)&quot;,&quo expression&quot;:&quot;&quot;}, {&quot;name&quot;:&quot;score&quot;,&quot;type&quot;:&quot;BIGINT&quot;,&quot;expression& ot;:&quot;&quot;}],&quot;watermarkSpec&quot;:[]},&quot;properties&quot;: {&quot;connector&quot;:&quot;blackhole&quot;},&quot;comment&quot;:&quot;blackhole sink table&quot;}]}</data> <requestId>202107221428-KKE3K857WS</requestId>
```

##### 3.1.2.14 ListSessionClusters

Call ListSessionClusters to list all session clusters in a specified workspace and namespace.

**Request headers**

This API uses common request headers and does not require special request headers. For more information, see the common request parameters documentation.

**Syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/sessionclusters HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the workspace ID by using one of the following methods: Call ListNamespaces to obtain the workspace ID. View the workspace details in the Fully Managed Flink development console. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "metadata": {}, "apiVersion": "v1", "kind": "SessionClusterList ", "items": [] } | The detailed information. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| success | Boolean | true | Indicates whether the request succeeded. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/sessionclusters HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &namespace=flinkteam &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"{\"metadata\":
{},\"apiVersion\":\"v1\",\"kind\":\"SessionClusterList\",\"items\":[]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data>{&quot;metadata&quot;: {},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;SessionClusterList&quot;, uot;items&quot;:[]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.15 ListSecretValues

Obtains a list of variables (as listed on the Variables page in the console).

**Request headers**

The ListSecretValues operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | 5CC1B23C-CCA3- 4283-B275- 0F969CDFD34F | The request ID. |

| data | String | { "metadata": { "totalSize": 1, "totalPage": 1 }, "apiVersion": "v1", "kind": "SecretValueList", "items": [ { "metadata": { "createdAt": "2024-03- 11T03:07:09Z", "modifiedAt": "2024-03- 11T03:07:09Z", "resourceVersion": 1, "name": "secretkey", "namespace": "flinkteam", "annotations": { "creator": "22985261012276 3813", "modifier": "22985261012276 3813", "creatorName": "flinkadmin", "modifierName": "flinkadmin" }, "id": "6dd63491- f0bf-4af3-a38e- 7001d479addc", "labels": {} }, "apiVersion": "v1", "kind": "SecretValue", "spec": { "kind": "Plain", "value": "******" } } ] } | The detailed information. |
|---|---|---|---|

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"{\"metadata\":
{\"totalSize\":1,\"totalPage\":1},\"apiVersion\":\"v1\",\"kind\":\"SecretValueList\",\"it s\":[{\"metadata\":{\"createdAt\":\"2024-03-11T03:07:09Z\",\"modifiedAt\":\"2024-03-11T 03:07:09Z\",\"resourceVersion\":1,\"name\":\"secretkey\",\"namespace\":\"flinkteam\",\"an tations\": {\"creator\":\"229852610122763813\",\"modifier\":\"229852610122763813\",\"creatorName\":\ linkadmin\",\"modifierName\":\"flinkadmin\"},\"id\":\"6dd63491-f0bf-4af3-a38e-7001d479a ddc\",\"labels\":{}},\"apiVersion\":\"v1\",\"kind\":\"SecretValue\",\"spec\":{\"kind\": \"Plain\",\"value\":\"******\"}}]}",
 "success":true,
 "requestId":"5CC1B23C-CCA3-4283-B275-0F969CDFD34F"
```

`}` `XML` format

```xml
<data>{&quot;metadata&quot;: {&quot;totalSize&quot;:1,&quot;totalPage&quot;:1},&quot;apiVersion&quot;:&quot;v1&quot;,& ot;kind&quot;:&quot;SecretValueList&quot;,&quot;items&quot;:[{&quot;metadata&quot;:{&qu ot;createdAt&quot;:&quot;2024-03-11T03:07:09Z&quot;,&quot;modifiedAt&quot;:&quot;2024-0 11T03:07:09Z&quot;,&quot;resourceVersion&quot;:1,&quot;name&quot;:&quot;secretkey&quot;,& ot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;229852610122763813&quot;,&quot;modifier&quot;:&quot;2298526101 763813&quot;,&quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;modifierName&quot;:&quo flinkadmin&quot;},&quot;id&quot;:&quot;6dd63491-f0bf-4af3-a38e- 7001d479addc&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;SecretValue&quot;,&quot; ec&quot;:{&quot;kind&quot;:&quot;Plain&quot;,&quot;value&quot;:&quot;******&quot;}}]}</ data> <success>true</success> <requestId>5CC1B23C-CCA3-4283-B275-0F969CDFD34F</requestId>
```

##### 3.1.2.16 ListSavepoints

Call ListSavepoints to get a list of job snapshots.

**Request headers**

This API operation uses common request headers and requires no special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/savepoints HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |
| deployme ntId | Strin g | Query | Yes | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | The job ID. |
| jobId | Strin g | Query | No | 5af678c0-7db0-4650- 94c2-d2604f0a**** | The job instance ID. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the workspace ID by using one of the following methods: Call ListNamespaces to obtain the workspace ID. View the workspace details in the Realtime Compute for Apache Flink fully managed development console. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
|   |   | { "metadata": {}, "apiVersion": "v1", "kind": "SavepointList", "items": [{ "metadata": { "createdAt": "2026-04- 24T03:55:16Z", "jobId": "f736bbd6- c9cf-48ab-973a- 9653bb0f8c0a", "workspace": "9cuwr9g7y1hl19", "nativeFormat": false, "modifiedAt": "2026-04- 24T03:55:19Z", "deploymentId": "a3d88b2a-e076- 4491-86f2- 5a81ea4c7300", "origin": "USER REQUEST", _ |   |

| Parameter | Type | "resourceVersion": Example 2, "namespace": | Description |
|---|---|---|---|
|   |   | "flinkteam", "annotations": { "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "9", "taker": " \| vvp-0" |   |
| data | String | }, "comment": "", "id": "5cea0d88- 303d-44e5-a96e- 47f7217723d7" }, "apiVersion": "v1", "kind": "Savepoint", "spec": { "flinkSavepointId": "fc2e33c1-8132- 516f-2923- 7371060fb449", "savepointLocation ": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/fli nk- savepoints/namesp aces/flinkteam/dep loyments/a3d88b2 a-e076-4491-86f2- 5a81ea4c7300/5ce a0d88-303d-44e5- a96e- 47f7217723d7/sav epoint-f736bb- f467305080c0" }, "status": { "state": "COMPLETED" } }, { "metadata": { "createdAt": "2026-04- 24T03:52:08Z", "jobId": "e5c412be- c160-460a-9d7b- 0b7111c77e15", "workspace": "9cuwr9g7y1hl19", "nativeFormat": false, "modifiedAt": "2026-04- 24T03:52:13Z", "deploymentId": "a3d88b2a-e076- 4491-86f2- 5a81ea4c7300", "origin": "USER REQUEST", _ "resourceVersion": 2, "namespace": "flinkteam", "annotations": { "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "6", "taker": " \| vvp-0" | The detailed information. |

| Parameter | Type | }, "comment": "", Example "id": "58778df9- | Description |
|---|---|---|---|
|   |   | 5082-4da3-9890- d531fcc1200d" }, "apiVersion": "v1", "kind": "Savepoint", "spec": { "flinkSavepointId": "3ac331a3-6ef9- d8f7-e3e8- e3d5b2649180", "savepointLocation ": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/fli nk- savepoints/namesp aces/flinkteam/dep loyments/a3d88b2 a-e076-4491-86f2- 5a81ea4c7300/587 78df9-5082-4da3- 9890- d531fcc1200d/sav epoint-e5c412- 8a27e8210de8" }, "status": { "state": "COMPLETED" } }] |   |
| requestId | String | } CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/savepoints HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7def580c00 &workspace=default &Common Request Parameter
```

Sample success responses `JSON` format `{`

```json
 "data":"{\"metadata\":{},\"apiVersion\":\"v1\",\"kind\":\"SavepointList\",\"items\":[{
\"metadata\":{\"createdAt\":\"2026-04-24T03:55:16Z\",\"jobId\":\"f736bbd6-c9cf-48ab-973
```

`a-`

```json
9653bb0f8c0a\",\"workspace\":\"9cuwr9g7y1hl19\",\"nativeFormat\":false,\"modifiedAt\":\"2 6-04-24T03:55:19Z\",\"deploymentId\":\"a3d88b2a-e076-4491-86f2- 5a81ea4c7300\",\"origin\":\"USER_REQUEST\",\"resourceVersion\":2,\"namespace\":\"flinktea ",\"annotations\": {\"com.dataartisans.appmanager.controller.deployment.spec.version\":\"9\",\"taker\":\"
| vvp-0\"},\"comment\":\"\",\"id\":\"5cea0d88-303d-44e5-a96e-
47f7217723d7\"},\"apiVersion\":\"v1\",\"kind\":\"Savepoint\",\"spec\": {\"flinkSavepointId\":\"fc2e33c1-8132-516f-2923- 7371060fb449\",\"savepointLocation\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flink-sa vepoints/namespaces/flinkteam/deployments/a3d88b2a-e076-4491-86f2- 5a81ea4c7300/5cea0d88-303d-44e5-a96e-47f7217723d7/savepoint-f736bbf467305080c0\"},\"status\":{\"state\":\"COMPLETED\"}},{\"metadata\": {\"createdAt\":\"2026-04-24T03:52:08Z\",\"jobId\":\"e5c412be-c160-460a-9d7b-0b7111c77e1 5\",\"workspace\":\"9cuwr9g7y1hl19\",\"nativeFormat\":false,\"modifiedAt\":\"2026-04-24 T03:52:13Z\",\"deploymentId\":\"a3d88b2a-e076-4491-86f2- 5a81ea4c7300\",\"origin\":\"USER_REQUEST\",\"resourceVersion\":2,\"namespace\":\"flinktea ",\"annotations\": {\"com.dataartisans.appmanager.controller.deployment.spec.version\":\"6\",\"taker\":\"
| vvp-0\"},\"comment\":\"\",\"id\":\"58778df9-5082-4da3-9890-
d531fcc1200d\"},\"apiVersion\":\"v1\",\"kind\":\"Savepoint\",\"spec\": {\"flinkSavepointId\":\"3ac331a3-6ef9-d8f7-e3e8e3d5b2649180\",\"savepointLocation\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flink-sa vepoints/namespaces/flinkteam/deployments/a3d88b2a-e076-4491-86f2- 5a81ea4c7300/58778df9-5082-4da3-9890-d531fcc1200d/savepoint-e5c412- 8a27e8210de8\"},\"status\":{\"state\":\"COMPLETED\"}}]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data>{&quot;metadata&quot;: {},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;SavepointList&quot;,&quot tems&quot;:[{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:55:16Z&quot;,&quot;jobId&quot;:&quot;f736bbd6-c9cf-48ab-973a- 9653bb0f8c0a&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;nativeFormat&qu ;:false,&quot;modifiedAt&quot;:&quot;2026-04- 24T03:55:19Z&quot;,&quot;deploymentId&quot;:&quot;a3d88b2a-e076-4491-86f2- 5a81ea4c7300&quot;,&quot;origin&quot;:&quot;USER_REQUEST&quot;,&quot;resourceVersion&quot 2,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;com.dataartisans.appmanager.controller.deployment.spec.version&quot;:&quot;9&quot; quot;taker&quot;:&quot; | vvp- 0&quot;},&quot;comment&quot;:&quot;&quot;,&quot;id&quot;:&quot;5cea0d88-303d-44e5-a96e- 47f7217723d7&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Savepoin quot;,&quot;spec&quot;:{&quot;flinkSavepointId&quot;:&quot;fc2e33c1-8132-516f-2923-7371 060fb449&quot;,&quot;savepointLocation&quot;:&quot;oss://flink-fullymanaged-9cuwr9g7y1h l19/flink-savepoints/namespaces/flinkteam/deployments/a3d88b2a-e076-4491-86f2-5a81ea4c7 300/5cea0d88-303d-44e5-a96e-47f7217723d7/savepoint-f736bbf467305080c0&quot;},&quot;status&quot;:{&quot;state&quot;:&quot;COMPLETED&quot;}},{&quo t;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:52:08Z&quot;,&quot;jobId&quot;:&quot;e5c412be-c160-460a-9d7b- 0b7111c77e15&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;nativeFormat&qu ;:false,&quot;modifiedAt&quot;:&quot;2026-04- 24T03:52:13Z&quot;,&quot;deploymentId&quot;:&quot;a3d88b2a-e076-4491-86f2- 5a81ea4c7300&quot;,&quot;origin&quot;:&quot;USER_REQUEST&quot;,&quot;resourceVersion&quot 2,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;com.dataartisans.appmanager.controller.deployment.spec.version&quot;:&quot;6&quot; quot;taker&quot;:&quot; | vvp- 0&quot;},&quot;comment&quot;:&quot;&quot;,&quot;id&quot;:&quot;58778df9-5082-4da3-9890d531fcc1200d&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Savepoin quot;,&quot;spec&quot;:{&quot;flinkSavepointId&quot;:&quot;3ac331a3-6ef9-d8f7-e3e8-e3d5 b2649180&quot;,&quot;savepointLocation&quot;:&quot;oss://flink-fullymanaged-9cuwr9g7y1h l19/flink-savepoints/namespaces/flinkteam/deployments/a3d88b2a-e076-4491-86f2-5a81ea4c7 300/58778df9-5082-4da3-9890-d531fcc1200d/savepoint-e5c412- 8a27e8210de8&quot;},&quot;status&quot;:{&quot;state&quot;:&quot;COMPLETED&quot;}}]}</da ta> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.17 ListNamespaces

Lists all namespaces in a region.

**Request headers**

The ListNamespaces operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/namespaces/v1/namespaces HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| data | String | { "@type": "type.googleapis.c om/vvp.namespace s.v1.ListNamespac esResponse", "namespaces": [{ "roleBindings": [{ "role": "owner", "members": ["user:2354069766 5705****"] }, { "role": "owner", "members": ["user:1664076657 00****"] }], "cluster": "", "isHa": false, "workspace": "9cuwr9g7y1hl19", "cpuBrand": "Intel", "previewSessionCl usterName": "", "createTime": "2026-04- 24T03:33:43.6806 26Z", "lifecyclePhase": "LIFECYCLE PHASE _ ACTIVE", "name": _ "namespaces/flinkt eam", "labels": {} }] } | The detailed information. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
GET /pop/namespaces/v1/namespaces HTTP/1.1 &RegionId=cn-wulan-env***-d01 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.namespaces.v1.ListNamespacesResponse\",\"namespaces\ [{\"roleBindings\":[{\"role\":\"owner\",\"members\":[\"user:23540697665705****\"]},{\"r ole\":\"owner\",\"members\": [\"user:166407665700****\"]}],\"cluster\":\"\",\"isHa\":false,\"workspace\":\"9cuwr9g7y1h 9\",\"cpuBrand\":\"Intel\",\"previewSessionClusterName\":\"\",\"createTime\":\"2026-04- 24T03:33:43.680626Z\",\"lifecyclePhase\":\"LIFECYCLE_PHASE_ACTIVE\",\"name\":\"namespaces linkteam\",\"labels\":{}}]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.namespaces.v1.ListNamespacesResponse&quo ,&quot;namespaces&quot;:[{&quot;roleBindings&quot;: [{&quot;role&quot;:&quot;owner&quot;,&quot;members&quot;: [&quot;user:23540697665705****&quot;]}, {&quot;role&quot;:&quot;owner&quot;,&quot;members&quot;: [&quot;user:166407665700****&quot;]}],&quot;cluster&quot;:&quot;&quot;,&quot;isHa&quot;:f se,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;cpuBrand&quot;:&quot;Intel&quot &quot;previewSessionClusterName&quot;:&quot;&quot;,&quot;createTime&quot;:&quot;2026-04
```

`-`

```xml
24T03:33:43.680626Z&quot;,&quot;lifecyclePhase&quot;:&quot;LIFECYCLE_PHASE_ACTIVE&quot;,& ot;name&quot;:&quot;namespaces/flinkteam&quot;,&quot;labels&quot;:{}}]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.18 ListFunctions

Call ListFunctions to obtain a list of user-defined functions (UDFs).

**Request headers**

This API uses common request headers and requires no special request headers. For more information, see Common Request Parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listFun ions HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The name of the region. |
| namespac e | Strin g | Path | Yes | ververica | The name of the project where the job resides. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call ListNamespaces to obtain the ID. Obtain the ID from the workspace details in the Fully Managed Flink development console. |
| cat | Strin g | Path | Yes | vvp | The name of the catalog. |
| database | Strin g | Query | Yes | default | The name of the catalog database. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | {"@type":"type.go ogleapis.com/vvp.s ql.catalog.v1beta2. ListFunctionsRespo nse","functions": [{"name":"Timesta mpProbe","classNa me":"com.alibaba. blink.udtf.Timesta mpProbe","function Language":"FUNCT ION LANGUAGE JA _ _ VA","functionType" :"FUNCTION TYPE _ _ FLINK","description ":"This is a user- defined function"}, {"name":"Transfor mUdtf","className ":"com.alibaba.blin k.udtf.TransformUd tf","functionLangua ge":"FUNCTION LA _ NGUAGE JAVA","fu _ nctionType":"FUNC TION TYPE FLINK", _ _ "description":"This is a user-defined function"}]} | The detailed data. |
| requestId | String | 0ADBBDD0-E2E9- 4611-98C6- 6767A3AB87D2 | The request ID. |
| success | Boolean | true | Indicates whether the request succeeds. |

**Examples**

Request example

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listFun ions HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &database=default &Common request parameters
```

Successful response example `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.ListFunctionsResponse\",\"functi s\": [{\"name\":\"TimestampProbe\",\"className\":\"com.alibaba.blink.udtf.TimestampProbe\",\"f ctionLanguage\":\"FUNCTION_LANGUAGE_JAVA\",\"functionType\":\"FUNCTION_TYPE_FLINK\",\"des iption\":\"This is a user-defined function\"}, {\"name\":\"TransformUdtf\",\"className\":\"com.alibaba.blink.udtf.TransformUdtf\",\"func onLanguage\":\"FUNCTION_LANGUAGE_JAVA\",\"functionType\":\"FUNCTION_TYPE_FLINK\",\"descri ion\":\"This is a user-defined function\"}]}",
 "requestId":"0ADBBDD0-E2E9-4611-98C6-6767A3AB87D2",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.ListFunctionsRespons quot;,&quot;functions&quot;: [{&quot;name&quot;:&quot;TimestampProbe&quot;,&quot;className&quot;:&quot;com.alibaba.bli .udtf.TimestampProbe&quot;,&quot;functionLanguage&quot;:&quot;FUNCTION_LANGUAGE_JAVA&quot &quot;functionType&quot;:&quot;FUNCTION_TYPE_FLINK&quot;,&quot;description&quot;:&quot;Th is a user-defined function&quot;}, {&quot;name&quot;:&quot;TransformUdtf&quot;,&quot;className&quot;:&quot;com.alibaba.blink dtf.TransformUdtf&quot;,&quot;functionLanguage&quot;:&quot;FUNCTION_LANGUAGE_JAVA&quot;,& ot;functionType&quot;:&quot;FUNCTION_TYPE_FLINK&quot;,&quot;description&quot;:&quot;This is a user-defined function&quot;}]}</data> <requestId>0ADBBDD0-E2E9-4611-98C6-6767A3AB87D2</requestId> <success>true</success>
```

##### 3.1.2.19 ListFormats

Views the formats list.

**Request headers**

The ListFormats operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |

| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| data | String | { "formats": [ { "sink": true, "name": "namespaces/flinkt eam/formats/avro", "source": true, "type": "avro", "properties": [ { "defaultValue": "", "description": "Must be set to \u0027avro\u0027 to configure this format.", "definesFormat": false, "key": "format", "required": true } ], "packaged": true, "dependencies": [ "hdfs:///vvp/data/s ql- artifacts/namespac es/ververica/conne ctors/vvr-6.0.7- flink- 1.15/opt/formats/a vro/flink-sql-avro- 1.15-vvr-6.0.7- SNAPSHOT.jar" ] } ], "@type": "type.googleapis.c om/vvp.sql.v1beta 1.ListFormatsResp onse" } | The detailed information. |

| requestId | String | 6BFF2035-B5FB- 4E1A-8F32- 4CA636417A3D | The request ID. |
|---|---|---|---|

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &namespace=flinkteam &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"{\"formats\":
[{\"sink\":true,\"name\":\"namespaces/flinkteam/formats/avro\",\"source\":true,\"type\":\ vro\",\"properties\":[{\"defaultValue\":\"\",\"description\":\"Must be set to \\u0027av ro\\u0027 to configure this format.\",\"definesFormat\":false,\"key\":\"format\",\"required\":true}],\"packaged\":tru \"dependencies\":[\"hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr- 6.0.7-flink-1.15/opt/formats/avro/flink-sql-avro-1.15-vvr-6.0.7- SNAPSHOT.jar\"]}],\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.ListFormatsResponse\"}"
 "success":true,
 "requestId":"6BFF2035-B5FB-4E1A-8F32-4CA636417A3D"
```

`}` `XML` format

```xml
<data>{&quot;formats&quot;: [{&quot;sink&quot;:true,&quot;name&quot;:&quot;namespaces/flinkteam/formats/avro&quot;,&q t;source&quot;:true,&quot;type&quot;:&quot;avro&quot;,&quot;properties&quot;:[{&quot;de faultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;Must be set to \u0027avro\u0027 to configure this format.&quot;,&quot;definesFormat&quot;:false,&quot;key&quot;:&quot;format&quot;,&quot;re ired&quot;:true}],&quot;packaged&quot;:true,&quot;dependencies&quot;: [&quot;hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1 .15/opt/formats/avro/flink-sql-avro-1.15-vvr-6.0.7- SNAPSHOT.jar&quot;]}],&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.ListFor tsResponse&quot;}</data> <success>true</success> <requestId>6BFF2035-B5FB-4E1A-8F32-4CA636417A3D</requestId>
```

##### 3.1.2.20 ListFlinkVersions

Call ListFlinkVersions to obtain the list of Flink engine versions.

**Request headers**

This API uses common request headers and does not require special request headers. For more information, see the Common Request Parameters document.

**Syntax**

```
GET /pop/workspaces/[workspace]/api/v1/flink-version-meta.json HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain this ID in one of the following ways: Call ListNamespaces to obtain the ID. Obtain the ID from the workspace details page in the Realtime Compute for Apache Flink fully managed development console. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
|   |   | { "defaultFlinkVersio nName": "vvr- 6.0.0-flink-1.15", "flinkVersionMetad atas": [ { "supportFindUsedC atalogs": false, "useForJarFineGrai ned": false, "versionName": "vvr-3.0.9-flink- 1.12", "flinkVersion": "1.12", "useForSqlDeploy ments": true, "labels": {}, "features": { "supportFindUsedC atalogs": false, "supportDynamicL ogLevel": false, "supportDagExpan |   |

| Parameter | Type | sion": false, Example "useForJarFineGrai | Description |
|---|---|---|---|
|   |   | ned": false, "supportNativeSav epoint": false, "supportStateCom patibility": false, "supportNativeK8s" : false, "supportJvmDebug |   |
| data | String | ": false, "supportLogArchiv e": false, "useForSqlDeploy ments": true, "supportLogPaging ": false }, "tarUrl": "hdfs:///vvp/data/s ql- artifacts/namespac es/default/package d-vvr-dist/vvr- 3.0.9-flink- 1.12/vvr-3.0.9- flink-1.12- dist.tar.gz", "supportStateCom patibility": false, "defaultFor": [], "imageTag": "1.12.0-vvr-3.0.9- 1109", "vvrVersion": "3.0.9", "status": "DEPRECATED" }, { "supportFindUsedC atalogs": true, "useForJarFineGrai ned": false, "versionName": "vvr-4.0.18-flink- 1.13", "flinkVersion": "1.13", "useForSqlDeploy ments": true, "labels": {}, "features": { "supportFindUsedC atalogs": true, "supportDynamicL ogLevel": true, "supportDagExpan sion": false, "useForJarFineGrai ned": false, "supportNativeSav epoint": false, "supportStateCom patibility": true, "supportNativeK8s" : false, "supportJvmDebug ": true, "supportLogArchiv | The detailed information. |

| Parameter | Type | e": true, Example "useForSqlDeploy | Description |
|---|---|---|---|
|   |   | ments": true, "supportLogPaging ": true }, "tarUrl": "hdfs:///vvp/data/s ql- artifacts/namespac es/default/package d-vvr-dist/vvr- 4.0.18-flink- 1.13/vvr-4.0.18- flink-1.13- dist.tar.gz", "supportStateCom patibility": true, "defaultFor": [], "imageTag": "1.13.0-vvr-4.0.18- 22", "vvrVersion": "4.0.18", "status": "DEPRECATED" }, { "supportFindUsedC atalogs": true, "useForJarFineGrai ned": false, "versionName": "vvr-6.0.0-flink- 1.15", "flinkVersion": "1.15", "useForSqlDeploy ments": true, "labels": {}, "features": { "supportFindUsedC atalogs": true, "supportDynamicL ogLevel": true, "supportDagExpan sion": false, "useForJarFineGrai ned": false, "supportNativeSav epoint": false, "supportStateCom patibility": true, "supportNativeK8s" : false, "supportJvmDebug ": true, "supportLogArchiv e": true, "useForSqlDeploy ments": true, "supportLogPaging ": true }, "tarUrl": "hdfs:///vvp/data/s ql- artifacts/namespac es/default/package d-vvr-dist/vvr- 6.0.7-flink- 1.15/vvr-6.0.7- flink-1.15- |   |
| > Document Versi | on: 20260828 |   | 12 |

| Parameter | Type | dist.tar.gz", Example "supportStateCom | Description |
|---|---|---|---|
|   |   | patibility": true, "defaultFor": [], "imageTag": "1.15.0-vvr-6.0.7- 29", "vvrVersion": |   |
| requestId | String | "6.0.7", "status": 63269B06-8027- "STABLE" } ] } 4CD0-9AB5- D9791B185B82 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/flink-version-meta.json HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"{\"defaultFlinkVersionName\":\"vvr-6.0.0-flink-
1.15\",\"flinkVersionMetadatas\": [{\"supportFindUsedCatalogs\":false,\"useForJarFineGrained\":false,\"versionName\":\"vvr- 3.0.9-flink-1.12\",\"flinkVersion\":\"1.12\",\"useForSqlDeployments\":true,\"labels\":{ },\"features\": {\"supportFindUsedCatalogs\":false,\"supportDynamicLogLevel\":false,\"supportDagExpansion :false,\"useForJarFineGrained\":false,\"supportNativeSavepoint\":false,\"supportStateComp ibility\":false,\"supportNativeK8s\":false,\"supportJvmDebug\":false,\"supportLogArchive\ false,\"useForSqlDeployments\":true,\"supportLogPaging\":false},\"tarUrl\":\"hdfs:///vvp/ ta/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-3.0.9-flink-1.12/vvr-3.0.9-fl ink-1.12-dist.tar.gz\",\"supportStateCompatibility\":false,\"defaultFor\": [],\"imageTag\":\"1.12.0-vvr-3.0.9- 1109\",\"vvrVersion\":\"3.0.9\",\"status\":\"DEPRECATED\"}, {\"supportFindUsedCatalogs\":true,\"useForJarFineGrained\":false,\"versionName\":\"vvr- 4.0.18-flink-1.13\",\"flinkVersion\":\"1.13\",\"useForSqlDeployments\":true,\"labels\": {},\"features\": {\"supportFindUsedCatalogs\":true,\"supportDynamicLogLevel\":true,\"supportDagExpansion\" alse,\"useForJarFineGrained\":false,\"supportNativeSavepoint\":false,\"supportStateCompat ility\":true,\"supportNativeK8s\":false,\"supportJvmDebug\":true,\"supportLogArchive\":tr ,\"useForSqlDeployments\":true,\"supportLogPaging\":true},\"tarUrl\":\"hdfs:///vvp/data/s -artifacts/namespaces/default/packaged-vvr-dist/vvr-4.0.18-flink-1.13/vvr-4.0.18-flink- 1.13-dist.tar.gz\",\"supportStateCompatibility\":true,\"defaultFor\": [],\"imageTag\":\"1.13.0-vvr-4.0.18- 22\",\"vvrVersion\":\"4.0.18\",\"status\":\"DEPRECATED\"}, {\"supportFindUsedCatalogs\":true,\"useForJarFineGrained\":false,\"versionName\":\"vvr- 6.0.0-flink-1.15\",\"flinkVersion\":\"1.15\",\"useForSqlDeployments\":true,\"labels\":{ },\"features\": {\"supportFindUsedCatalogs\":true,\"supportDynamicLogLevel\":true,\"supportDagExpansion\" alse,\"useForJarFineGrained\":false,\"supportNativeSavepoint\":false,\"supportStateCompat ility\":true,\"supportNativeK8s\":false,\"supportJvmDebug\":true,\"supportLogArchive\":tr ,\"useForSqlDeployments\":true,\"supportLogPaging\":true},\"tarUrl\":\"hdfs:///vvp/data/s -artifacts/namespaces/default/packaged-vvr-dist/vvr-6.0.7-flink-1.15/vvr-6.0.7-flink-1. 15-dist.tar.gz\",\"supportStateCompatibility\":true,\"defaultFor\": [],\"imageTag\":\"1.15.0-vvr-6.0.7- 29\",\"vvrVersion\":\"6.0.7\",\"status\":\"STABLE\"}]}",
 "requestId":"63269B06-8027-4CD0-9AB5-D9791B185B82",
 "success":true
```

`}` `XML` format

```xml
<data>{&quot;defaultFlinkVersionName&quot;:&quot;vvr-6.0.0-flink- 1.15&quot;,&quot;flinkVersionMetadatas&quot;: [{&quot;supportFindUsedCatalogs&quot;:false,&quot;useForJarFineGrained&quot;:false,&quot; rsionName&quot;:&quot;vvr-3.0.9-flink- 1.12&quot;,&quot;flinkVersion&quot;:&quot;1.12&quot;,&quot;useForSqlDeployments&quot;:tru &quot;labels&quot;:{},&quot;features&quot;: {&quot;supportFindUsedCatalogs&quot;:false,&quot;supportDynamicLogLevel&quot;:false,&quot upportDagExpansion&quot;:false,&quot;useForJarFineGrained&quot;:false,&quot;supportNative vepoint&quot;:false,&quot;supportStateCompatibility&quot;:false,&quot;supportNativeK8s&qu ;:false,&quot;supportJvmDebug&quot;:false,&quot;supportLogArchive&quot;:false,&quot;useFo qlDeployments&quot;:true,&quot;supportLogPaging&quot;:false},&quot;tarUrl&quot;:&quot;hdf ///vvp/data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-3.0.9-flink-1.12/vvr -3.0.9-flink-1.12dist.tar.gz&quot;,&quot;supportStateCompatibility&quot;:false,&quot;defaultFor&quot;:[] ,&quot;imageTag&quot;:&quot;1.12.0-vvr-3.0.9- 1109&quot;,&quot;vvrVersion&quot;:&quot;3.0.9&quot;,&quot;status&quot;:&quot;DEPRECATED&q t;}, {&quot;supportFindUsedCatalogs&quot;:true,&quot;useForJarFineGrained&quot;:false,&quot;ve ionName&quot;:&quot;vvr-4.0.18-flink- 1.13&quot;,&quot;flinkVersion&quot;:&quot;1.13&quot;,&quot;useForSqlDeployments&quot;:tru &quot;labels&quot;:{},&quot;features&quot;: {&quot;supportFindUsedCatalogs&quot;:true,&quot;supportDynamicLogLevel&quot;:true,&quot;s portDagExpansion&quot;:false,&quot;useForJarFineGrained&quot;:false,&quot;supportNativeSa point&quot;:false,&quot;supportStateCompatibility&quot;:true,&quot;supportNativeK8s&quot; alse,&quot;supportJvmDebug&quot;:true,&quot;supportLogArchive&quot;:true,&quot;useForSqlD loyments&quot;:true,&quot;supportLogPaging&quot;:true},&quot;tarUrl&quot;:&quot;hdfs:///v /data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-4.0.18-flink-1.13/vvr-4.0. 18-flink-1.13dist.tar.gz&quot;,&quot;supportStateCompatibility&quot;:true,&quot;defaultFor&quot;:[], &quot;imageTag&quot;:&quot;1.13.0-vvr-4.0.18- 22&quot;,&quot;vvrVersion&quot;:&quot;4.0.18&quot;,&quot;status&quot;:&quot;DEPRECATED&qu ;}, {&quot;supportFindUsedCatalogs&quot;:true,&quot;useForJarFineGrained&quot;:false,&quot;ve ionName&quot;:&quot;vvr-6.0.0-flink- 1.15&quot;,&quot;flinkVersion&quot;:&quot;1.15&quot;,&quot;useForSqlDeployments&quot;:tru &quot;labels&quot;:{},&quot;features&quot;: {&quot;supportFindUsedCatalogs&quot;:true,&quot;supportDynamicLogLevel&quot;:true,&quot;s portDagExpansion&quot;:false,&quot;useForJarFineGrained&quot;:false,&quot;supportNativeSa point&quot;:false,&quot;supportStateCompatibility&quot;:true,&quot;supportNativeK8s&quot; alse,&quot;supportJvmDebug&quot;:true,&quot;supportLogArchive&quot;:true,&quot;useForSqlD loyments&quot;:true,&quot;supportLogPaging&quot;:true},&quot;tarUrl&quot;:&quot;hdfs:///v /data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-6.0.7-flink-1.15/vvr-6.0.7 -flink-1.15dist.tar.gz&quot;,&quot;supportStateCompatibility&quot;:true,&quot;defaultFor&quot;:[], &quot;imageTag&quot;:&quot;1.15.0-vvr-6.0.7- 29&quot;,&quot;vvrVersion&quot;:&quot;6.0.7&quot;,&quot;status&quot;:&quot;STABLE&quot;}] </data> <requestId>63269B06-8027-4CD0-9AB5-D9791B185B82</requestId> <success>true</success>
```

##### 3.1.2.21 ListDeploymentTargets

Call ListDeploymentTargets to obtain the list of deployment targets.

**Request headers**

This API uses common request headers and requires no special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-targets HTTP/1
```

`.1`

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project that contains the job. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace that contains the job. You can obtain the ID by using one of the following methods: Call ListNamespaces to obtain the ID. Obtain the ID from the workspace details in the Flink Serverless development console. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "metadata": {}, "apiVersion": "v1", "kind": "DeploymentTarge tList", "items": [{ "metadata": { "createdAt": "2026-04- 24T03:33:44Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:33:44Z", "resourceVersion": 1, "name": "dt- flinkteam", "namespace": "flinkteam", "annotations": { "creator": "14949745101258 46", "modifier": "14949745101258 46", "creatorName": "null", "modifierName": "null" }, "id": "a89ff052-38c6- 4fd3-9b91- e9c53f8ee019", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentTarge t", "ha": false, "spec": { "kubernetes": { "namespace": "flinkteam" }, "kind": "kubernetes", "state": "ONLINE" } }] } | The details. |
| success | Boolean | true | Indicates whether the request succeeds. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-targets HTTP/1
```

`.1`

```
&RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"{\"metadata\":
{},\"apiVersion\":\"v1\",\"kind\":\"DeploymentTargetList\",\"items\":[{\"metadata\":{\" createdAt\":\"2026-04- 24T03:33:44Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:33:44Z\",\"resourceVersion\":1,\"name\":\"dtflinkteam\",\"namespace\":\"flinkteam\",\"annotations\": {\"creator\":\"1494974510125846\",\"modifier\":\"1494974510125846\",\"creatorName\":\"nul ",\"modifierName\":\"null\"},\"id\":\"a89ff052-38c6-4fd3-9b91e9c53f8ee019\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"DeploymentTarget\",\"ha\":false,\"spec\":{\"kubern etes\":{\"namespace\":\"flinkteam\"},\"kind\":\"kubernetes\",\"state\":\"ONLINE\"}}]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data>{&quot;metadata&quot;: {},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;DeploymentTargetList&quot &quot;items&quot;:[{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04-24T03:33: 44Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot;:&quot;2 6-04-24T03:33:44Z&quot;,&quot;resourceVersion&quot;:1,&quot;name&quot;:&quot;dt-flinkte am&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;:{&quot;cre ator&quot;:&quot;1494974510125846&quot;,&quot;modifier&quot;:&quot;1494974510125846&quot; quot;creatorName&quot;:&quot;null&quot;,&quot;modifierName&quot;:&quot;null&quot;},&quot; &quot;:&quot;a89ff052-38c6-4fd3-9b91-e9c53f8ee019&quot;,&quot;labels&quot;:{}},&quot;ap iVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;DeploymentTarget&quot;,&quot;ha&quot false,&quot;spec&quot;:{&quot;kubernetes&quot;: {&quot;namespace&quot;:&quot;flinkteam&quot;},&quot;kind&quot;:&quot;kubernetes&quot;,&qu ;state&quot;:&quot;ONLINE&quot;}}]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.22 ListDeployments

Call ListDeployments to get the list of deployed jobs.

**Request headers**

This API uses common request headers and has no special request headers. For more information, see the Common request parameters documentation.

**Syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the workspace ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the Realtime Compute for Apache Flink fully managed development console. |
| pageSize | Strin g | Query | No | 10 | The pagination parameter that specifies the number of entries per page. Maximum value: 100. Minimum value: 1. Default value: 10. |
| pageIndex | Strin g | Query | No | 1 | The pagination parameter that specifies the page number. Minimum value: 1. Default value: 1. |
| sortName | Strin g | Query | No | ["age", "name"] | The list of fields by which to sort, such as age and name. |
| sortOrder | Strin g | Query | No | DESC | The sort order. DESC: descending order. ASC: ascending order. Default value: DESC. |
| creator | Strin g | Query | No | 235406976657057054 | The creator of the rule. |

| ealtime Com | pute |   |   | Realti nk (Co Editio | me Compute for Apache Fl mpute-Storage Separation n) Developer Guide·AppM |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| modifier | Strin g | Query | No | yunduntest | The user who last modified the rule. |
| priority | Strin g | Query | No | 1 | The route priority. A value of 1 indicates the highest priority. A larger value indicates a lower priority. |
| deployme ntId | Strin g | Query | No | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | The job ID. |
| name | Strin g | Query | No | blinkteam | The namespace name. |
| status | Strin g | Query | No | 1 | The status. |
| state | Strin g | Query | No | false | The running state of the playbook: true: The workflow is published. false: The workflow is disabled. |
| batchMod e | Strin g | Query | No | true | Specifies whether to disable batch processing mode. This mode applies to scenarios where you process tasks or data one by one. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
|   |   | { "metadata": { "totalSize": 1, "totalPage": 1 }, "apiVersion": "v1", "kind": "DeploymentList", "items": [{ "metadata": { "createdAt": "2026-04- 30T03:54:19Z", |   |

| dition) Developer ager API | Guide·AppMa |   |   |
|---|---|---|---|
| Parameter | Type | "workspace": Example "9cuwr9g7y1hl19", | Description |
|   |   | "modifiedAt": "2026-04- 30T05:38:17Z", "resourceVersion": 4, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "creator": "23540697665705 7054", "resource- plan.has.migrated" : "true", "storage.disaster.r po": "1800", "deployment.has.d eployed": "false", "deployment.sourc e-type": "EDITOR", "deployment.paren t.id": "", "modifier": "23540697665705 7054", "creatorName": "flinkadmin", "plan.uri": "deployment/9151 0cd2-9d21-463a- abf4- 9c608d23e92e/res ourcePlan.json", "priority": "5", "priority.class.nam e": "flink-p5", "migration.display. enabled": "false", "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "2", "default.resource- setting.has.migrate d": "true", "deployment.refere nced.deployment.d raft.history.version ": "7", "deployment.refere nced.deployment.d raft.id": "cee26b6e-d03b- 4a03-a628- a6fe665c525e", "modifierName": "flinkadmin", "taker": " \| vvp-0", "deployment.refere nced.deployment.d raft.history.id": "c7819685-3abe- 4115-a26b- d40e73c58856" }, "id": "91510cd2- |   |

| Parameter | Type | 9d21-463a-abf4- Example 9c608d23e92e", | Description |
|---|---|---|---|
| data | String | "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type ": "fine-grained", "native.kubernetes .mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.e nabled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.17.0-vvr-8.0.7- manifest-251107", "kind": "SQLSCRIPT", "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;", _ "imageUserDefined ": false, "flinkImageRegistr y": "cn-wulan- env**-d01- reg.docker.intra.en | The detailed information. |
|   |   | v**.shuguang.com: 80/ververica-paas", "versionName": |   |

| Parameter | Type | "vvr-8.0.7-flink- Example 1.17", | Description |
|---|---|---|---|
|   |   | "flinkImageReposit ory": "vvr", "flinkVersion": "1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration" : {} } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestored State": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1, "deploymentTarget Id": "a89ff052- 38c6-4fd3-9b91- e9c53f8ee019" }, "status": { "startTime": 0, "state": "CANCELLED", "endTime": 0 } }] } |   |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

**Examples**

Sample request

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default &Common Request Parameter
```

Sample success response `JSON` format `{`

```json
 "data":"{\"metadata\":
{\"totalSize\":1,\"totalPage\":1},\"apiVersion\":\"v1\",\"kind\":\"DeploymentList\",\"ite \":[{\"metadata\":{\"createdAt\":\"2026-04- 30T03:54:19Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 30T05:38:17Z\",\"resourceVersion\":4,\"name\":\"sqlJob\",\"namespace\":\"flinkteam\",\"an tations\":{\"creator\":\"235406976657057054\",\"resourceplan.has.migrated\":\"true\",\"storage.disaster.rpo\":\"1800\",\"deployment.has.deployed\ \"false\",\"deployment.sourcetype\":\"EDITOR\",\"deployment.parent.id\":\"\",\"modifier\":\"235406976657057054\",\"cre orName\":\"flinkadmin\",\"plan.uri\":\"deployment/91510cd2-9d21-463a-abf4- 9c608d23e92e/resourcePlan.json\",\"priority\":\"5\",\"priority.class.name\":\"flink-p5\ ",\"migration.display.enabled\":\"false\",\"com.dataartisans.appmanager.controller.deploy nt.spec.version\":\"2\",\"default.resourcesetting.has.migrated\":\"true\",\"deployment.referenced.deployment.draft.history.version\ \"7\",\"deployment.referenced.deployment.draft.id\":\"cee26b6e-d03b-4a03-a628-a6fe665c5 25e\",\"modifierName\":\"flinkadmin\",\"taker\":\" | vvp- 0\",\"deployment.referenced.deployment.draft.history.id\":\"c7819685-3abe-4115-a26b-d40 e73c58856\"},\"id\":\"91510cd2-9d21-463a-abf4-9c608d23e92e\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\":{\"template\":{\"metadata\": {\"annotations\":{\"flink.resource.type\":\"finegrained\",\"native.kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\":{\"artifa ct\":{\"flinkImageTag\":\"1.17.0-vvr-8.0.7-manifest- 251107\",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'connector' = 'datagen'\);\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\);\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-wulan-env**-d01 -reg.docker.intra.env**.shuguang.com:80/ververica-paas\",\"versionName\":\"vvr-8.0.7-fl ink- 1.17\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.17\"},\"parallelism\":1,\"ba hMode\":false,\"resources\":{\"jobmanager\": {\"memory\":\"2Gi\",\"cpu\":0.5},\"taskmanager\": {\"memory\":\"3Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfig ation\":{}}},\"restoreStrategy\": {\"kind\":\"LATEST_STATE\",\"allowNonRestoredState\":false},\"state\":\"CANCELLED\",\"upg deStrategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"dep ymentTargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"},\"status\": {\"startTime\":0,\"state\":\"CANCELLED\",\"endTime\":0}}]}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
```

`}` `XML` format

```xml
<data>{&quot;metadata&quot;:
```

|   | <data>{&quot;metadata&quot;: {&quot;totalSize&quot;:1,&quot;totalPage&quot;:1},&quot;apiVersion&quot;:&quot;v1&quot;,& ot;kind&quot;:&quot;DeploymentList&quot;,&quot;items&quot;:[{&quot;metadata&quot;:{&quo t;createdAt&quot;:&quot;2026-04- 30T03:54:19Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot &quot;2026-04- 30T05:38:17Z&quot;,&quot;resourceVersion&quot;:4,&quot;name&quot;:&quot;sqlJob&quot;,&quo namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;resource- plan.has.migrated&quot;:&quot;true&quot;,&quot;storage.disaster.rpo&quot;:&quot;1800&quot &quot;deployment.has.deployed&quot;:&quot;false&quot;,&quot;deployment.source-type&quot ;:&quot;EDITOR&quot;,&quot;deployment.parent.id&quot;:&quot;&quot;,&quot;modifier&quot;:& ot;235406976657057054&quot;,&quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;plan.uri uot;:&quot;deployment/91510cd2-9d21-463a-abf4- 9c608d23e92e/resourcePlan.json&quot;,&quot;priority&quot;:&quot;5&quot;,&quot;priority.cl s.name&quot;:&quot;flink- p5&quot;,&quot;migration.display.enabled&quot;:&quot;false&quot;,&quot;com.dataartisans.a manager.controller.deployment.spec.version&quot;:&quot;2&quot;,&quot;default.resource-s etting.has.migrated&quot;:&quot;true&quot;,&quot;deployment.referenced.deployment.draft.h tory.version&quot;:&quot;7&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&q t;cee26b6e-d03b-4a03-a628- a6fe665c525e&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;taker&quot;:&quo \| vvp- 0&quot;,&quot;deployment.referenced.deployment.draft.history.id&quot;:&quot;c7819685-3a be-4115-a26b-d40e73c58856&quot;},&quot;id&quot;:&quot;91510cd2-9d21-463a-abf4-9c608d23e 92e&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;s c&quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;:{&quot;fli nk.resource.type&quot;:&quot;fine- grained&quot;,&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;flink.queryable- state.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false& ot;}},&quot;spec&quot;:{&quot;artifact&quot;:{&quot;flinkImageTag&quot;:&quot;1.17.0-vv r-8.0.7-manifest- 251107&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;CREATE TEMPORARY TABLE `datahub table` (strname VARCHAR)with ( &#x27;connector&#x27; = &#x2 _ 7;datagen&#x27;);CREATE TEMPORARY TABLE `kafka table` (strname VARCHAR, lens BIGINT)wit _ h ( &#x27;connector&#x27; = &#x27;print&#x27;);INSERT INTO kafka tableSELECT SUBSTRI _ NG (strname, 0, 10) AS strname, CAST (CHAR LENGTH (strname) AS BIGINT) AS lensFROM dat _ ahub table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&quot _ n-wulan-env**-d01-reg.docker.intra.env**.shuguang.com:80/ververica- paas&quot;,&quot;versionName&quot;:&quot;vvr-8.0.7-flink- 1.17&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quo 1.17&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;: {&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;2Gi&quot;,&quot;cpu&quot;:0.5},&quot;taskmanager&quot;:{&quot ;memory&quot;:&quot;3Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&q t;default&quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;:{&quot ;kind&quot;:&quot;LATEST STATE&quot;,&quot;allowNonRestoredState&quot;:false},&quot;state _ uot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJ CreationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9b91-e 9c53f8ee019&quot;},&quot;status&quot;: {&quot;startTime&quot;:0,&quot;state&quot;:&quot;CANCELLED&quot;,&quot;endTime&quot;:0}}] |   |
|---|---|---|
| 1 | 34 > Document Version: 20260828 |   |

```xml
{&quot;startTime&quot;:0,&quot;state&quot;:&quot;CANCELLED&quot;,&quot;endTime&quot;:0}}] </data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

##### 3.1.2.23 ListDatabases

Call ListDatabases to view the databases under a catalog.

**Request headers**

This API uses common request headers and does not require special request headers. For more information, see the common request parameters documentation.

**Syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listDat ases HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | ververica | The name of the project where the job resides. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the workspace ID by using one of the following methods: Call ListNamespaces to obtain the workspace ID. View the workspace details in the Fully Managed Flink development console. |
| cat | Strin g | Path | Yes | vvp | The name of the catalog. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.ListDataba sesResponse", "databases": [ { "name": "default", "properties": {}, "comment": "The default database" } ] } | The detailed information. |
| requestId | String | 76F325D7-3EC4- 4E34-81A8- 18B92D7EE606 | The request ID. |
| success | Boolean | true | Indicates whether the request succeeded. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listDat ases HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.ListDatabasesResponse\",\"databa s\":[{\"name\":\"default\",\"properties\":{},\"comment\":\"The default database\"}]}",
 "requestId":"76F325D7-3EC4-4E34-81A8-18B92D7EE606",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.ListDatabasesRespons quot;,&quot;databases&quot;: [{&quot;name&quot;:&quot;default&quot;,&quot;properties&quot;: {},&quot;comment&quot;:&quot;The default database&quot;}]}</data> <requestId>76F325D7-3EC4-4E34-81A8-18B92D7EE606</requestId> <success>true</success>
```

##### 3.1.2.24 ListConnectors

Call ListConnectors to get the list of connectors.

**Request headers**

This API uses common request headers and has no special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the workspace ID by using one of the following methods: Call ListNamespaces to obtain the workspace ID. View the workspace details on the Realtime Compute for Apache Flink fully managed development console. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request succeeded. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "connectors": [ { "lookup": false, "supportedFormats ": [], "environments": [ "PUBLIC CLOUD", _ "PRIVATE CLOUD", _ "ALIBABA GROUP", _ "VVC CLOUD" ], _ "sink": false, "name": "namespaces/flinkt eam/connectors/da tagen", "source": true, "type": "datagen", "properties": [ { "defaultValue": "", "description": "Must be set to \u0027datagen\u0 027 to configure this connector.", "definesFormat": false, "key": "connector", "required": true }, { "defaultValue": "", "description": "Rows per second to control the emit rate, default 10000L.", "definesFormat": false, "key": "rows- per-second", "required": false }, { "defaultValue": "", "description": "Total number of rows to emit. By default, the source is unbounded.", "definesFormat": false, "key": "number-of-rows", "required": false } ], "packaged": true, "dependencies": [] } ], "@type": "type.googleapis.c om/vvp.sql.v1beta 1.ListConnectorsRe sponse" } | The detailed data. |
| requestId | String | A62F262E-3055- 490B-B17B- 0C6BF83C4BE6 | The request ID. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &namespace=flinkteam &Common Request Parameter
```

Sample success responses `JSON` format `{`

```json
 "data":"{\"connectors\":[{\"lookup\":false,\"supportedFormats\":[],\"environments\":[\
"PUBLIC_CLOUD\",\"PRIVATE_CLOUD\",\"ALIBABA_GROUP\",\"VVC_CLOUD\"],\"sink\":false,\"name\ \"namespaces/flinkteam/connectors/datagen\",\"source\":true,\"type\":\"datagen\",\"proper es\":[{\"defaultValue\":\"\",\"description\":\"Must be set to \\u0027datagen\\u0027 to configure this connector.\",\"definesFormat\":false,\"key\":\"connector\",\"required\":true},{\"defaul tValue\":\"\",\"description\":\"Rows per second to control the emit rate, default 10000 L.\",\"definesFormat\":false,\"key\":\"rows-per-second\",\"required\":false},{\"default Value\":\"\",\"description\":\"Total number of rows to emit. By default, the source is unbounded.\",\"definesFormat\":false,\"key\":\"number-ofrows\",\"required\":false}],\"packaged\":true,\"dependencies\": []}],\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.ListConnectorsResponse\"}",
 "success":true,
 "requestId":"A62F262E-3055-490B-B17B-0C6BF83C4BE6"
```

`}` `XML` format

```xml
<data>{&quot;connectors&quot;:[{&quot;lookup&quot;:false,&quot;supportedFormats&quot;:[ ],&quot;environments&quot;: [&quot;PUBLIC_CLOUD&quot;,&quot;PRIVATE_CLOUD&quot;,&quot;ALIBABA_GROUP&quot;,&quot;VVC_C UD&quot;],&quot;sink&quot;:false,&quot;name&quot;:&quot;namespaces/flinkteam/connectors/d agen&quot;,&quot;source&quot;:true,&quot;type&quot;:&quot;datagen&quot;,&quot;properties& ot;:[{&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;Must be set t o \u0027datagen\u0027 to configure this connector.&quot;,&quot;definesFormat&quot;:false,&quot;key&quot;:&quot;connector&quot;,&q t;required&quot;:true}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;Rows per second to control the emit rate, default 10000L.&quot;,&quot;definesFormat&quot;:false,&quot;key&quot;:&quot;rows-per-second&quo t;,&quot;required&quot;:false}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;Total number of ro ws to emit. By default, the source is unbounded.&quot;,&quot;definesFormat&quot;:false,&quot;key&quot;:&quot;number-of-rows&q uot;,&quot;required&quot;:false}],&quot;packaged&quot;:true,&quot;dependencies&quot;:[] }],&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.ListConnectorsResponse&quo }</data> <success>true</success> <requestId>A62F262E-3055-490B-B17B-0C6BF83C4BE6</requestId>
```

##### 3.1.2.25 ListCatalogs

Call ListCatalogs to retrieve the list of catalogs in a specified namespace of a specified workspace.

**Request headers**

This API uses common request headers and requires no special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs HTTP/1.
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | ververica | The name of the project that contains the job. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call ListNamespaces to obtain the ID. Obtain the ID from the workspace details page in the fully managed Flink development console. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | {"@type":"type.go ogleapis.com/vvp.s ql.catalog.v1beta2. ListCatalogsRespon se","catalogs": [{"name":"namesp aces/flinkteam/cat alogs/vvp","propert ies": {"defaultDatabase ":"default","type":" vvp"}}]} | The detailed data. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | 31F99ADC-B72E- 4BA1-AD32- B938D5A57532 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Request example

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs HTTP/1. &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &Common request parameters
```

Successful response example `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.ListCatalogsResponse\",\"catalog ":[{\"name\":\"namespaces/flinkteam/catalogs/vvp\",\"properties\": {\"defaultDatabase\":\"default\",\"type\":\"vvp\"}}]}",
 "requestId":"31F99ADC-B72E-4BA1-AD32-B938D5A57532",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.ListCatalogsResponse uot;,&quot;catalogs&quot;: [{&quot;name&quot;:&quot;namespaces/flinkteam/catalogs/vvp&quot;,&quot;properties&quot;: {&quot;defaultDatabase&quot;:&quot;default&quot;,&quot;type&quot;:&quot;vvp&quot;}}]}</ data> <requestId>31F99ADC-B72E-4BA1-AD32-B938D5A57532</requestId> <success>true</success>
```

##### 3.1.2.26 ListArtifacts

Lists all artifacts in a workspace and the namespaces.

**Request headers**

The ListArtifacts operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:list HTTP /1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

| data | String | { "@type": "type.googleapis.c om/vvp.artifacts.v1 .ListArtifactsRespo nse", "artifacts": [{ "filename": "TopSpeedWindowi ng.jar", "size": "0", "createTime": "2026-04- 29T09:20:14Z", "uploader": "23540697665705 7054", "namespace": "namespaces/flinkt eam", "uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/ar tifacts/namespaces /flinkteam/TopSpee dWindowing.jar", "content": "" }] } | The detailed information. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:list HTTP /1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.artifacts.v1.ListArtifactsResponse\",\"artifacts\": [{\"filename\":\"TopSpeedWindowing.jar\",\"size\":\"0\",\"createTime\":\"2026-04-29T09: 20:14Z\",\"uploader\":\"235406976657057054\",\"namespace\":\"namespaces/flinkteam\",\"uri :\"oss://flink-fullymanaged- 9cuwr9g7y1hl19/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar\",\"content\":\"\"}]}
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.artifacts.v1.ListArtifactsResponse&quot; quot;artifacts&quot;: [{&quot;filename&quot;:&quot;TopSpeedWindowing.jar&quot;,&quot;size&quot;:&quot;0&quot;,& ot;createTime&quot;:&quot;2026-04- 29T09:20:14Z&quot;,&quot;uploader&quot;:&quot;235406976657057054&quot;,&quot;namespace&qu ;:&quot;namespaces/flinkteam&quot;,&quot;uri&quot;:&quot;oss://flink-fullymanaged-9cuwr 9g7y1hl19/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar&quot;,&quot;content&quot;: uot;&quot;}]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.27 GetUdfArtifact

Call GetUdfArtifact to retrieve detailed information about a UDF.

**Request headers**

This API uses common request headers and does not require special request headers. For more information, see the Common Request Parameter document.

**Syntax**

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactN e] HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| requireFu nctionNa mes | Boole an | Query | Yes | true | Specifies whether to return function names. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call ListNamespaces. View the workspace details in the Flink fully managed development console. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |

|   | Realtime Com | pute |   |   | Realti nk (Co Editio | me Compute for Apache Fl mpute-Storage Separation n) Developer Guide·AppM nager AP | i a I |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| udfArtifact Name | Strin g | Path | Yes | metric-transform-227- shaded | The name of the UDF. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.v1beta 1.GetUdfArtifactRe sponse", "udfArtifact": { "dependencyJarUri s": [], "udfClasses": [ { "functionNames": [ "TimestampProbe" ], "udfArtifactName": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227-shaded", "className": "com.alibaba.blink. udtf.TimestampPro be", "classType": "UDF TYPE SCALA _ _ R" }, { "functionNames": [ "TransformUdtf" ], "udfArtifactName": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227-shaded", "className": "com.alibaba.blink. udtf.TransformUdtf ", "classType": "UDF TYPE TABLE" _ _ } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "createTime": "2024-03- 08T08:13:54Z", "uploader": "22347490986944 5380", "jarUpdateTime": "2024-03- 08T08:13:57Z", "name": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227-shaded", "namespace": "namespaces/flinkt eam", "jarUrl": | The detailed information. |

| Parameter | Type | "hdfs:///vvp/data/s Example ql- | Description |
|---|---|---|---|
|   |   | artifacts/namespac es/flinkteam/udfs/ metric-transform- 227-shaded/2024- 03-08T08-13- 54.732313Z/metric -transform-2.2.7- shaded.jar", "updateTime": "2024-03- 08T08:13:57Z" } } |   |
| requestId | String | C44A1880-5138- 4204-9165- DC65C4B059C2 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Request example

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactN e] HTTP/1.1 &RegionId=cn-wulan-env***-d01 &requireFunctionNames=true &workspace=default &namespace=flinkteam &udfArtifactName=metric-transform-227-shaded &Common request parameters
```

Successful response example `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.GetUdfArtifactResponse\",\"udfArtifact\" {\"dependencyJarUris\":[],\"udfClasses\":[{\"functionNames\": [\"TimestampProbe\"],\"udfArtifactName\":\"namespaces/flinkteam/udfartifacts/metric-tra nsform-227shaded\",\"className\":\"com.alibaba.blink.udtf.TimestampProbe\",\"classType\":\"UDF_TYPE CALAR\"},{\"functionNames\": [\"TransformUdtf\"],\"udfArtifactName\":\"namespaces/flinkteam/udfartifacts/metric-tran sform-227shaded\",\"className\":\"com.alibaba.blink.udtf.TransformUdtf\",\"classType\":\"UDF_TYPE_ BLE\"}],\"artifactType\":\"ARTIFACT_TYPE_JAVA\",\"createTime\":\"2024-03- 08T08:13:54Z\",\"uploader\":\"223474909869445380\",\"jarUpdateTime\":\"2024-03-08T08:13 :57Z\",\"name\":\"namespaces/flinkteam/udfartifacts/metric-transform-227shaded\",\"namespace\":\"namespaces/flinkteam\",\"jarUrl\":\"hdfs:///vvp/data/sql-artif acts/namespaces/flinkteam/udfs/metric-transform-227-shaded/2024-03-08T08-13-54.732313Z/ metric-transform-2.2.7-shaded.jar\",\"updateTime\":\"2024-03-08T08:13:57Z\"}}",
 "requestId":"C44A1880-5138-4204-9165-DC65C4B059C2",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.GetUdfArtifactResponse&quot; quot;udfArtifact&quot;:{&quot;dependencyJarUris&quot;:[],&quot;udfClasses&quot;:[{&quot ;functionNames&quot;: [&quot;TimestampProbe&quot;],&quot;udfArtifactName&quot;:&quot;namespaces/flinkteam/udfar facts/metric-transform-227shaded&quot;,&quot;className&quot;:&quot;com.alibaba.blink.udtf.TimestampProbe&quot;,&quo classType&quot;:&quot;UDF_TYPE_SCALAR&quot;},{&quot;functionNames&quot;: [&quot;TransformUdtf&quot;],&quot;udfArtifactName&quot;:&quot;namespaces/flinkteam/udfart acts/metric-transform-227shaded&quot;,&quot;className&quot;:&quot;com.alibaba.blink.udtf.TransformUdtf&quot;,&quot lassType&quot;:&quot;UDF_TYPE_TABLE&quot;}],&quot;artifactType&quot;:&quot;ARTIFACT_TYPE_ VA&quot;,&quot;createTime&quot;:&quot;2024-03- 08T08:13:54Z&quot;,&quot;uploader&quot;:&quot;223474909869445380&quot;,&quot;jarUpdateTim quot;:&quot;2024-03- 08T08:13:57Z&quot;,&quot;name&quot;:&quot;namespaces/flinkteam/udfartifacts/metric-tran sform-227shaded&quot;,&quot;namespace&quot;:&quot;namespaces/flinkteam&quot;,&quot;jarUrl&quot;:&q t;hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/udfs/metric-transform-227-shaded/ 2024-03-08T08-13-54.732313Z/metric-transform-2.2.7shaded.jar&quot;,&quot;updateTime&quot;:&quot;2024-03-08T08:13:57Z&quot;}}</data> <requestId>C44A1880-5138-4204-9165-DC65C4B059C2</requestId> <success>true</success>
```

##### 3.1.2.28 GetTable

Call GetTable to retrieve table information.

**Request headers**

This API uses common request headers and requires no special request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getTabl HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | ververica | The name of the project where the job resides. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the workspace ID by using one of the following methods: Call ListNamespaces to obtain the workspace ID. View the workspace ID in the workspace details on the Fully Managed Flink development console. |
| cat | Strin g | Path | Yes | vvp | The catalog name. |
| database | Strin g | Query | Yes | default | The database name. |
| table | Strin g | Query | Yes | mydatahub | The table name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.GetTableR esponse", "table": { "name": "mydatahub", "schema": { "column": [ { "name": "strname", "type": "VARCHAR(214748 3647)", "expression": "" } ], "watermarkSpec": [] }, "properties": { "accessId": "SVw******PtL", "endpoint": "https://datahub.cn -wulan-env188- d01.dh.inter.env18 8.shuguang.com", "connector": "datahub", "accessKey": "RfE******VMB", "project": "datahub", "topic": "mysource" }, "comment": "" }, "success": true, "message": "" } | The detailed information. |
| requestId | String | FCB6D11E-8FAA- 48F7-8E25- 28218A6878F5 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getTabl HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &database=default &table=mydatahub &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.GetTableResponse\",\"table\":{ \"name\":\"mydatahub\",\"schema\":{\"column\": [{\"name\":\"strname\",\"type\":\"VARCHAR(2147483647)\",\"expression\":\"\"}],\"watermark ec\":[]},\"properties\": {\"accessId\":\"SVw******PtL\",\"endpoint\":\"https://datahub.cn-wulan-env188-d01.dh.in ter.env188.shuguang.com\",\"connector\":\"datahub\",\"accessKey\":\"RfE******VMB\",\"proj t\":\"datahub\",\"topic\":\"mysource\"},\"comment\":\"\"},\"success\":true,\"message\":\" }",
 "requestId":"FCB6D11E-8FAA-48F7-8E25-28218A6878F5",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.GetTableResponse&quo ,&quot;table&quot;:{&quot;name&quot;:&quot;mydatahub&quot;,&quot;schema&quot;:{&quot;co lumn&quot;: [{&quot;name&quot;:&quot;strname&quot;,&quot;type&quot;:&quot;VARCHAR(2147483647)&quot;,& ot;expression&quot;:&quot;&quot;}],&quot;watermarkSpec&quot;: []},&quot;properties&quot;: {&quot;accessId&quot;:&quot;SVw******PtL&quot;,&quot;endpoint&quot;:&quot;https://datahub n-wulan-env188d01.dh.inter.env188.shuguang.com&quot;,&quot;connector&quot;:&quot;datahub&quot;,&quot;ac ssKey&quot;:&quot;RfE******VMB&quot;,&quot;project&quot;:&quot;datahub&quot;,&quot;topic& ot;:&quot;mysource&quot;},&quot;comment&quot;:&quot;&quot;},&quot;success&quot;:true,&quo message&quot;:&quot;&quot;}</data> <requestId>FCB6D11E-8FAA-48F7-8E25-28218A6878F5</requestId> <success>true</success>
```

##### 3.1.2.29 GetResourcePlan

Obtains the resource configuration plan for a deployment.

**Request headers**

The GetResourcePlan operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/reso ce_plan HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| deploymen tId | Strin g | Path | Yes | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | The deployment ID of the job. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| data | String | { "success": true, "message": "", "plan": "" } | The detailed information of the resource configuration plan for the job. |
| requestId | String | 87589423-CE39- 470D-81EA- 5AB477CF4CD4 | The request ID. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/reso ce_plan HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &namespace=flinkteam &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7def580c00 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"{\"success\":true,\"message\":\"\",\"plan\":\"\"}",
 "success":true,
 "requestId":"87589423-CE39-470D-81EA-5AB477CF4CD4"
```

`}` `XML` format

```xml
<data> {&quot;success&quot;:true,&quot;message&quot;:&quot;&quot;,&quot;plan&quot;:&quot;&quot;} </data> <success>true</success> <requestId>87589423-CE39-470D-81EA-5AB477CF4CD4</requestId>
```

##### 3.1.2.30 GetGlobalDeploymentDefaults

Call the GetGlobalDeploymentDefaults operation to obtain the global deployment default configurations in the Realtime Compute service.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Header | Yes | flinkteam | The name of the project to which the job belongs. |

**Syntax**

```
GET /pop/workspaces/[workspace]/api/v1/global-deployment-defaults HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Path | Yes | default | The ID of the workspace to which the job belongs. You can obtain the ID by using one of the following methods: Call the ListNamespaces operation to obtain the ID. Obtain the ID from the workspace details in the Realtime Compute for Apache Flink development console. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "apiVersion": "v1", "kind": "GlobalDeployment Defaults", "spec": { "template": { "metadata": { "annotations": { "native.kubernetes .mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.e nabled": "false" } }, "spec": { "artifact": { "kind": "JAR", "imageUserDefined ": false }, "parallelism": 1, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 1.0 }, "taskmanager": { "memory": "4Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration" : {} } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestored State": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1 } } | The detailed information. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/global-deployment-defaults HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"{\"apiVersion\":\"v1\",\"kind\":\"GlobalDeploymentDefaults\",\"spec\":{\"templ
ate\":{\"metadata\":{\"annotations\": {\"native.kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\":{\"artifa ct\":{\"kind\":\"JAR\",\"imageUserDefined\":false},\"parallelism\":1,\"resources\":{\"j obmanager\":{\"memory\":\"4Gi\",\"cpu\":1.0},\"taskmanager\": {\"memory\":\"4Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfig ation\":{}}},\"restoreStrategy\": {\"kind\":\"LATEST_STATE\",\"allowNonRestoredState\":false},\"state\":\"CANCELLED\",\"upg deStrategy\": {\"kind\":\"STATELESS\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1}
```

`,`

```json
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;GlobalDeploymentDefaults&qu ;,&quot;spec&quot;:{&quot;template&quot;:{&quot;metadata&quot;: {&quot;annotations&quot;: {&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;flink.queryablestate.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false& ot;}},&quot;spec&quot;:{&quot;artifact&quot;: {&quot;kind&quot;:&quot;JAR&quot;,&quot;imageUserDefined&quot;:false},&quot;parallelism&q t;:1,&quot;resources&quot;:{&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:1.0},&quot;taskmanager&quot;:{&quot ;memory&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&q t;default&quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;:{&quot ;kind&quot;:&quot;LATEST_STATE&quot;,&quot;allowNonRestoredState&quot;:false},&quot;state uot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;STATELESS&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot axJobCreationAttempts&quot;:1}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.31 GetFunction

Call GetFunction to view the details of a function.

**Request headers**

This API uses common request headers and requires no special request headers. For more information, see Common Request Parameter.

**Syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getFunc on HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project to which the job belongs. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call ListNamespaces to obtain the ID. Obtain the ID from the workspace details in the Fully Managed Flink development console. |
| cat | Strin g | Path | Yes | vvp | The name of the catalog. |
| database | Strin g | Query | Yes | default | The name of the database. |
| function | Strin g | Query | Yes | TransformUdtf | The name of the function. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.GetFuncti onResponse", "function": { "name": "TransformUdtf", "className": "com.alibaba.blink. udtf.TransformUdtf ", "functionLanguage ": "FUNCTION LANGU _ AGE JAVA", _ "functionType": "FUNCTION TYPE F _ _ LINK", "description": "This is a user-defined function" }, "success": true, "message": "" } | The detailed information. |
| requestId | String | DD2A9970-CED3- 4AD6-B0F6- 8DFDD84AC6AC | The ID of the request. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Request example

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getFunc on HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default &cat=vvp &database=default &function=TransformUdtf &Common request parameters
```

Successful response example `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.GetFunctionResponse\",\"function
```

`:`

```json
{\"name\":\"TransformUdtf\",\"className\":\"com.alibaba.blink.udtf.TransformUdtf\",\"func onLanguage\":\"FUNCTION_LANGUAGE_JAVA\",\"functionType\":\"FUNCTION_TYPE_FLINK\",\"descri ion\":\"This is a user-defined function\"},\"success\":true,\"message\":\"\"}",
 "requestId":"DD2A9970-CED3-4AD6-B0F6-8DFDD84AC6AC",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.GetFunctionResponse& ot;,&quot;function&quot;: {&quot;name&quot;:&quot;TransformUdtf&quot;,&quot;className&quot;:&quot;com.alibaba.blink dtf.TransformUdtf&quot;,&quot;functionLanguage&quot;:&quot;FUNCTION_LANGUAGE_JAVA&quot;,& ot;functionType&quot;:&quot;FUNCTION_TYPE_FLINK&quot;,&quot;description&quot;:&quot;This is a user-defined function&quot;},&quot;success&quot;:true,&quot;message&quot;:&quot;&quot;}</data> <requestId>DD2A9970-CED3-4AD6-B0F6-8DFDD84AC6AC</requestId> <success>true</success>
```

##### 3.1.2.32 GetDeploymentDefaults

Queries the default deployment configurations of a workspace and its namespaces in Realtime Compute for Apache Flink.

**Request headers**

The GetDeploymentDefaults operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-defaults HTTP/
```

### 1.1 Obtain API information and its endpoint

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |

| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
|---|---|---|---|---|---|
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

| data | String | { "metadata": { "createdAt": "2026-04- 24T03:46:53Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:46:53Z", "resourceVersion": 1, "name": "stream", "namespace": "flinkteam", "annotations": { "deployment.defau lts.type": "stream", "creator": "system", "modifier": "system" }, "id": "690e3396-700a- 4b77-9fcf- d14a592f****", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentDefau lts", "spec": { "template": { "spec": { "resources": {}, "flinkConfiguration" : { "execution.checkp ointing.interval": "180s", "table.exec.state.ttl ": "36 h", "restart- strategy.fixed- delay.delay": "10 s", "restart- strategy.fixed- delay.attempts": "2147483647", "execution.checkp ointing.min-pause": "180s", "restart- strategy": "fixed- delay" } } } } } | The detailed information. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-defaults HTTP/
```

### 1.1 Obtain API information and its endpoint

```
&RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:46:53Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:46:53Z\",\"resourceVersion\":1,\"name\":\"stream\",\"namespace\":\"flinkteam\",\"an tations\": {\"deployment.defaults.type\":\"stream\",\"creator\":\"system\",\"modifier\":\"system\"}, id\":\"690e3396-700a-4b77-9fcf-d14a592f****\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"DeploymentDefaults\",\"spec\":{\"template\":{\"spe c\":{\"resources\":{},\"flinkConfiguration\": {\"execution.checkpointing.interval\":\"180s\",\"table.exec.state.ttl\":\"36 h\",\"rest art-strategy.fixed-delay.delay\":\"10 s\",\"restart-strategy.fixeddelay.attempts\":\"2147483647\",\"execution.checkpointing.minpause\":\"180s\",\"restart-strategy\":\"fixed-delay\"}}}}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:46:53Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot &quot;2026-04- 24T03:46:53Z&quot;,&quot;resourceVersion&quot;:1,&quot;name&quot;:&quot;stream&quot;,&quo namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;deployment.defaults.type&quot;:&quot;stream&quot;,&quot;creator&quot;:&quot;system uot;,&quot;modifier&quot;:&quot;system&quot;},&quot;id&quot;:&quot;690e3396-700a-4b77-9 fcf-d14a592f****&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;DeploymentDefaults&quot; quot;spec&quot;:{&quot;template&quot;:{&quot;spec&quot;:{&quot;resources&quot;:{},&quot ;flinkConfiguration&quot;: {&quot;execution.checkpointing.interval&quot;:&quot;180s&quot;,&quot;table.exec.state.ttl uot;:&quot;36 h&quot;,&quot;restart-strategy.fixed-delay.delay&quot;:&quot;10 s&quot;,& quot;restart-strategy.fixeddelay.attempts&quot;:&quot;2147483647&quot;,&quot;execution.checkpointing.min-pause&quo t;:&quot;180s&quot;,&quot;restart-strategy&quot;:&quot;fixed-delay&quot;}}}}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.33 GetDeployment

Call GetDeployment to retrieve deployed jobs.

**Request headers**

This API uses common request headers and requires no special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HT TP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |
| deployme ntId | Strin g | Path | Yes | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | The ID of the job. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call ListNamespaces to obtain the ID. Obtain the ID from the workspace details in the Realtime Compute for Apache Flink fully managed development console. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
|   |   | { "metadata": { "createdAt": "2026-04- 24T03:47:01Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:58:26Z", "resourceVersion": 174, "name": "sqlJob", "namespace": |   |

| Parameter | Type | "flinkteam", Example "annotations": { | Description |
|---|---|---|---|
|   |   | "creator": "23540697665705 7054", "resource- plan.has.migrated" : "true", "storage.disaster.r po": "1800", "deployment.sourc e-type": "EDITOR", "deployment.has.d eployed": "false", "deployment.paren t.id": "", "modifier": "23540697665705 7054", "creatorName": "flinkadmin", "plan.uri": "deployment/a3d8 8b2a-e076-4491- 86f2- 5a81ea4c7300/res ourcePlan.json", "priority": "5", "priority.class.nam e": "flink-p5", "migration.display. enabled": "false", "deployment.exec- plan.uri.valid": "true", "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "13", "default.resource- setting.has.migrate d": "true", "deployment.refere nced.deployment.d raft.history.version ": "1", "deployment.exec- plan.uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/fli nk- jobs/namespaces/fl inkteam/jobs/c944 e978-5cb9-4879- 8312- c0872ee50182/exe cPlan.json", "deployment.refere nced.deployment.d raft.id": "cee26b6e-d03b- 4a03-a628- a6fe665c525e", "resources.from.jo b.has.migrated": "true", "taker": " \| vvp-0", |   |

| Parameter | Type | "modifierName": Example "flinkadmin", | Description |
|---|---|---|---|
| data | String | "deployment.refere nced.deployment.d raft.history.id": "561a6a3d-7858- 4056-acfb- ad0cdec09e55" }, "id": "a3d88b2a- e076-4491-86f2- 5a81ea4c7300", "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type ": "fine-grained", "job.resource.total. memory.byte": "0", "job.resource.total. cpu": "0.0", "native.kubernetes .mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.e nabled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.17.0-vvr-8.0.7- manifest-251107", "kind": "SQLSCRIPT", "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH | The detailed information. |
|   |   | _ |   |

| Parameter | Type | (strname) AS Example BIGINT) AS lens | Description |
|---|---|---|---|
|   |   | FROM datahub table;", _ "imageUserDefined ": false, "flinkImageRegistr y": "cn-wulan- env35-d01- reg.docker.intra.en v35.shuguang.com :80/ververica- paas", "versionName": "vvr-8.0.7-flink- 1.17", "flinkImageReposit ory": "vvr", "flinkVersion": "1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration" : {} } }, "restoreStrategy": { "kind": "FROM SAVEPOINT _ ", "allowNonRestored State": false, "savepointId": "5cea0d88-303d- 44e5-a96e- 47f7217723d7" }, "state": "CANCELLED", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1, "deploymentTarget Id": "a89ff052- 38c6-4fd3-9b91- e9c53f8ee019" }, "status": { "startTime": 1777002980004, "state": |   |

| Parameter | Type | "CANCELLED", Example "endTime": 0 } } | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Request example

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HT TP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7def580c00 &workspace=default &Common request parameters
```

Successful response example `JSON` format `{`

```json
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:47:01Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:58:26Z\",\"resourceVersion\":174,\"name\":\"sqlJob\",\"namespace\":\"flinkteam\",\" notations\":{\"creator\":\"235406976657057054\",\"resourceplan.has.migrated\":\"true\",\"storage.disaster.rpo\":\"1800\",\"deployment.source-type \":\"EDITOR\",\"deployment.has.deployed\":\"false\",\"deployment.parent.id\":\"\",\"modif r\":\"235406976657057054\",\"creatorName\":\"flinkadmin\",\"plan.uri\":\"deployment/a3d88 a-e076-4491-86f2- 5a81ea4c7300/resourcePlan.json\",\"priority\":\"5\",\"priority.class.name\":\"flink-p5\ ",\"migration.display.enabled\":\"false\",\"deployment.execplan.uri.valid\":\"true\",\"com.dataartisans.appmanager.controller.deployment.spec.versio ":\"13\",\"default.resourcesetting.has.migrated\":\"true\",\"deployment.referenced.deployment.draft.history.version\ \"1\",\"deployment.exec-plan.uri\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flink-jobs /namespaces/flinkteam/jobs/c944e978-5cb9-4879-8312c0872ee50182/execPlan.json\",\"deployment.referenced.deployment.draft.id\":\"cee26b6e-d 03b-4a03-a628-a6fe665c525e\",\"resources.from.job.has.migrated\":\"true\",\"taker\":\"
| vvp-
0\",\"modifierName\":\"flinkadmin\",\"deployment.referenced.deployment.draft.history.id\" "561a6a3d-7858-4056-acfb-ad0cdec09e55\"},\"id\":\"a3d88b2a-e076-4491-86f2- 5a81ea4c7300\",\"labels\":{}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\":{\ "template\":{\"metadata\":{\"annotations\":{\"flink.resource.type\":\"fine-grained\",\" job.resource.total.memory.byte\":\"0\",\"job.resource.total.cpu\":\"0.0\",\"native.kubern es.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\":{\"artifa ct\":{\"flinkImageTag\":\"1.17.0-vvr-8.0.7-manifest- 251107\",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'connector' = 'datagen'\);\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\);\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-wulan-env35-d01 -reg.docker.intra.env35.shuguang.com:80/ververica-paas\",\"versionName\":\"vvr-8.0.7-fl ink- 1.17\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.17\"},\"parallelism\":1,\"ba hMode\":false,\"resources\":{\"jobmanager\": {\"memory\":\"2Gi\",\"cpu\":0.5},\"taskmanager\": {\"memory\":\"3Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfig ation\":{}}},\"restoreStrategy\": {\"kind\":\"FROM_SAVEPOINT\",\"allowNonRestoredState\":false,\"savepointId\":\"5cea0d88- 303d-44e5-a96e-47f7217723d7\"},\"state\":\"CANCELLED\",\"upgradeStrategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"dep ymentTargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"},\"status\": {\"startTime\":1777002980004,\"state\":\"CANCELLED\",\"endTime\":0}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<dt>{&
```

`t`

```
tdt&
```

`t` `{&` `t`

```
tdAt&
```

`t` `&`

```
t202604
```

|   | <data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:47:01Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot &quot;2026-04- 24T03:58:26Z&quot;,&quot;resourceVersion&quot;:174,&quot;name&quot;:&quot;sqlJob&quot;,&q t;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;resource- plan.has.migrated&quot;:&quot;true&quot;,&quot;storage.disaster.rpo&quot;:&quot;1800&quot &quot;deployment.source- type&quot;:&quot;EDITOR&quot;,&quot;deployment.has.deployed&quot;:&quot;false&quot;,&quot eployment.parent.id&quot;:&quot;&quot;,&quot;modifier&quot;:&quot;235406976657057054&quot &quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;plan.uri&quot;:&quot;deployment/a3d8 2a-e076-4491-86f2- 5a81ea4c7300/resourcePlan.json&quot;,&quot;priority&quot;:&quot;5&quot;,&quot;priority.cl s.name&quot;:&quot;flink- p5&quot;,&quot;migration.display.enabled&quot;:&quot;false&quot;,&quot;deployment.exec- plan.uri.valid&quot;:&quot;true&quot;,&quot;com.dataartisans.appmanager.controller.deploy nt.spec.version&quot;:&quot;13&quot;,&quot;default.resource- setting.has.migrated&quot;:&quot;true&quot;,&quot;deployment.referenced.deployment.draft. story.version&quot;:&quot;1&quot;,&quot;deployment.exec- plan.uri&quot;:&quot;oss://flink-fullymanaged-9cuwr9g7y1hl19/flink- jobs/namespaces/flinkteam/jobs/c944e978-5cb9-4879-8312- c0872ee50182/execPlan.json&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&q t;cee26b6e-d03b-4a03-a628- a6fe665c525e&quot;,&quot;resources.from.job.has.migrated&quot;:&quot;true&quot;,&quot;tak &quot;:&quot; \| vvp- 0&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;deployment.referenced.deplo ent.draft.history.id&quot;:&quot;561a6a3d-7858-4056-acfb- ad0cdec09e55&quot;},&quot;id&quot;:&quot;a3d88b2a-e076-4491-86f2- 5a81ea4c7300&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;s c&quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;:{&quot;fli nk.resource.type&quot;:&quot;fine- grained&quot;,&quot;job.resource.total.memory.byte&quot;:&quot;0&quot;,&quot;job.resource otal.cpu&quot;:&quot;0.0&quot;,&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot; ink.queryable- state.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false& ot;}},&quot;spec&quot;:{&quot;artifact&quot;:{&quot;flinkImageTag&quot;:&quot;1.17.0-vv r-8.0.7-manifest- 251107&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;CREATE TEMPORARY TABLE `datahub table` (strname VARCHAR)with ( &#x27;connector&#x27; = &#x2 _ 7;datagen&#x27;);CREATE TEMPORARY TABLE `kafka table` (strname VARCHAR, lens BIGINT)wit _ h ( &#x27;connector&#x27; = &#x27;print&#x27;);INSERT INTO kafka tableSELECT SUBSTRI _ NG (strname, 0, 10) AS strname, CAST (CHAR LENGTH (strname) AS BIGINT) AS lensFROM dat _ ahub table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&quot _ n-wulan-env35-d01-reg.docker.intra.env35.shuguang.com:80/ververica- paas&quot;,&quot;versionName&quot;:&quot;vvr-8.0.7-flink- 1.17&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quo 1.17&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;: {&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;2Gi&quot;,&quot;cpu&quot;:0.5},&quot;taskmanager&quot;:{&quot ;memory&quot;:&quot;3Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&q t;default&quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;:{&quot ;kind&quot;:&quot;FROM SAVEPOINT&quot; &quot;allowNonRestoredState&quot;:false &quot;save |   |
|---|---|---|

```xml
;kind&quot;:&quot;FROM_SAVEPOINT&quot;,&quot;allowNonRestoredState&quot;:false,&quot;save intId&quot;:&quot;5cea0d88-303d-44e5-a96e- 47f7217723d7&quot;},&quot;state&quot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJ CreationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9b91-e 9c53f8ee019&quot;},&quot;status&quot;: {&quot;startTime&quot;:1777002980004,&quot;state&quot;:&quot;CANCELLED&quot;,&quot;endTim quot;:0}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.34 GetDefaultDatabase

Obtains the default database under a catalog.

**Request headers**

The GetDefaultDatabase operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getDefa tDatabase HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | ververica | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
| cat | Strin g | Path | Yes | vvp | The catalog name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.GetDefaul tDatabaseRespons e", "database": "default" } | The detailed information. |
| requestId | String | 59F6950E-FC05- 495E-A286- 08C111EC7A4B | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getDefa tDatabase HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.GetDefaultDatabaseResponse\",\"d abase\":\"default\"}",
 "requestId":"59F6950E-FC05-495E-A286-08C111EC7A4B",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.GetDefaultDatabaseRe onse&quot;,&quot;database&quot;:&quot;default&quot;}</data> <requestId>59F6950E-FC05-495E-A286-08C111EC7A4B</requestId> <success>true</success>
```

##### 3.1.2.35 GetDatabase

Queries the detailed information of a database under a catalog.

**Request headers**

The GetDatabase operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getData se HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | ververica | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
| cat | Strin g | Path | Yes | vvp | The catalog name. |
| database | Strin g | Quer y | Yes | default | The database name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| data | String | {"@type":"type.go ogleapis.com/vvp.s ql.catalog.v1beta2. GetDatabaseRespo nse","database": {"name":"default", "properties": {},"comment":"Th e default database"},"succe ss":true,"message" :""} | The detailed information. |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getData se HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &database=default &Common Request Parameter
```

Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.GetDatabaseResponse\",\"database :{\"name\":\"default\",\"properties\":{},\"comment\":\"The default database\"},\"success\":true,\"message\":\"\"}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.GetDatabaseResponse& ot;,&quot;database&quot;:{&quot;name&quot;:&quot;default&quot;,&quot;properties&quot;:{ },&quot;comment&quot;:&quot;The default database&quot;},&quot;success&quot;:true,&quot;message&quot;:&quot;&quot;}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.36 GetCatalog

Views the catalog information.

**Request headers**

The GetCatalog operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getCata g HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | ververica | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
| cat | Strin g | Path | Yes | vvp | The catalog name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.GetCatalo gResponse", "catalog": { "name": "namespaces/flinkt eam/catalogs/vvp", "properties": { "defaultDatabase": "default", "type": "vvp" } } } | The detailed information. |
|---|---|---|---|
| requestId | String | 0AFF0B61-35A5- 46D9-930F- 3826DCA3D3F9 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getCata g HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.GetCatalogResponse\",\"catalog\" {\"name\":\"namespaces/flinkteam/catalogs/vvp\",\"properties\": {\"type\":\"vvp\",\"defaultDatabase\":\"default\"}}}",
 "requestId":"0AFF0B61-35A5-46D9-930F-3826DCA3D3F9",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.GetCatalogResponse&q t;,&quot;catalog&quot;: {&quot;name&quot;:&quot;namespaces/flinkteam/catalogs/vvp&quot;,&quot;properties&quot;: {&quot;type&quot;:&quot;vvp&quot;,&quot;defaultDatabase&quot;:&quot;default&quot;}}}</d ata> <requestId>0AFF0B61-35A5-46D9-930F-3826DCA3D3F9</requestId> <success>true</success>
```

##### 3.1.2.37 GetArtifactMetadata

Call GetArtifactMetadata to obtain the metadata of a specified file in Realtime Compute.

**Request headers**

This API operation uses common request headers and has no special request headers. For more information, see Common Request Parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:getMetadata H TTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |
| filename | Strin g | Query | Yes | test.csv | The name of the file. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call ListNamespaces to obtain the ID. Obtain the ID from the workspace details in the Flink fully managed development console. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| data | String | { "artifact": { "filename": "TopSpeedWindowi ng.jar", "size": "0", "createTime": "2026-04- 29T09:20:14Z", "uploader": "23540697665705 7054", "namespace": "namespaces/flinkt eam", "uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/ar tifacts/namespaces /flinkteam/TopSpee dWindowing.jar", "content": "" }, "@type": "type.googleapis.c om/vvp.artifacts.v1 .GetArtifactMetada taResponse" } | The detailed information. |
| success | Boolean | true | Indicates whether the request succeeds. |

**Examples**

Request example

```
GET /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:getMetadata H TTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &filename=test.csv &workspace=default &Common request parameters
```

Successful response example `JSON` format `{`

```json
 "data":"{\"artifact\":
{\"filename\":\"TopSpeedWindowing.jar\",\"size\":\"0\",\"createTime\":\"2026-04-29T09:2 0:14Z\",\"uploader\":\"235406976657057054\",\"namespace\":\"namespaces/flinkteam\",\"uri\ \"oss://flink-fullymanaged- 9cuwr9g7y1hl19/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar\",\"content\":\"\"},\ type\":\"type.googleapis.com/vvp.artifacts.v1.GetArtifactMetadataResponse\"}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data>{&quot;artifact&quot;: {&quot;filename&quot;:&quot;TopSpeedWindowing.jar&quot;,&quot;size&quot;:&quot;0&quot;,&q t;createTime&quot;:&quot;2026-04- 29T09:20:14Z&quot;,&quot;uploader&quot;:&quot;235406976657057054&quot;,&quot;namespace&qu ;:&quot;namespaces/flinkteam&quot;,&quot;uri&quot;:&quot;oss://flink-fullymanaged-9cuwr 9g7y1hl19/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar&quot;,&quot;content&quot;: uot;&quot;},&quot;@type&quot;:&quot;type.googleapis.com/vvp.artifacts.v1.GetArtifactMetad aResponse&quot;}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.38 GenerateResourcePlan

Generates a resource configuration plan for a deployment.

**Request headers**

The GenerateResourcePlan operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/reso ce_plan:generate HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |

| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| deploymen tId | Strin g | Path | Yes | d0b3abf0-4bfe-46b1- a324-5b7def58**** | The deployment ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| data | String | { "success": true, "plan": " {\"ssgProfiles\": [{\"name\":\"defaul t\",\"cpu\":0.2,\"hea p\":\"768 mb\",\"offHeap\":\" 32 mb\",\"managed\": {},\"extended\": {}}],\"nodes\": [{\"id\":1,\"type\":\" StreamExecTableS ourceScan\",\"desc\ ":\"Source: datahub table[4]\", _ \"profile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\": 32768,\"minParalle lism\":1}}, {\"id\":2,\"type\":\" StreamExecCalc\",\ "desc\":\"Calc[5]\",\ "profile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\": 32768,\"minParalle lism\":1}}, {\"id\":3,\"type\":\" StreamExecSink\",\ "desc\":\"Sink: kafka table[6]\",\"p _ rofile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\": 32768,\"minParalle lism\":1}}],\"edges \": [{\"source\":1,\"tar get\":2,\"mode\":\" PIPELINED\",\"strat egy\":\"FORWARD\" }, {\"source\":2,\"targ et\":3,\"mode\":\"PI PELINED\",\"strateg y\":\"FORWARD\"}] ,\"vertices\": {\"717c7b8afebbfb 7137f6f0f99beb2a 94\":[1,2,3]}}" } | The detailed information of the resource configuration plan. |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD****" | The request ID. |

**Examples**

Sample requests

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/reso ce_plan:generate HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7def58****"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{\"success\":true,\"plan\":\"{\\\"ssgProfiles\\\":
[{\\\"name\\\":\\\"default\\\",\\\"cpu\\\":0.2,\\\"heap\\\":\\\"768 mb\\\",\\\"offHeap\\\":\\\"32 mb\\\",\\\"managed\\\":{},\\\"extended\\\": {}}],\\\"nodes\\\": [{\\\"id\\\":1,\\\"type\\\":\\\"StreamExecTableSourceScan\\\",\\\"desc\\\":\\\"Source: datahub_table[4]\\\",\\\"profile\\\": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"min rallelism\\\":1}}, {\\\"id\\\":2,\\\"type\\\":\\\"StreamExecCalc\\\",\\\"desc\\\":\\\"Calc[5]\\\",\\\"profil \\": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"min rallelism\\\":1}}, {\\\"id\\\":3,\\\"type\\\":\\\"StreamExecSink\\\",\\\"desc\\\":\\\"Sink: kafka_table[6]\\\",\\\"profile\\\": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"min rallelism\\\":1}}],\\\"edges\\\": [{\\\"source\\\":1,\\\"target\\\":2,\\\"mode\\\":\\\"PIPELINED\\\",\\\"strategy\\\":\\\"F WARD\\\"}, {\\\"source\\\":2,\\\"target\\\":3,\\\"mode\\\":\\\"PIPELINED\\\",\\\"strategy\\\":\\\"FO ARD\\\"}],\\\"vertices\\\":{\\\"717c7b8afebbfb7137f6f0f99beb2a94\\\":[1,2,3]}}\"}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****\""
```

`}` `XML` format

```xml
<data>{&quot;success&quot;:true,&quot;plan&quot;:&quot;{\&quot;ssgProfiles\&quot;:[{\&q uot;name\&quot;:\&quot;default\&quot;,\&quot;cpu\&quot;:0.2,\&quot;heap\&quot;:\&quot;768 mb\&quot;,\&quot;offHeap\&quot;:\&quot;32 mb\&quot;,\&quot;managed\&quot;: {},\&quot;extended\&quot;:{}}],\&quot;nodes\&quot;: [{\&quot;id\&quot;:1,\&quot;type\&quot;:\&quot;StreamExecTableSourceScan\&quot;,\&quot;de \&quot;:\&quot;Source: datahub_table[4]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParallel m\&quot;:32768,\&quot;minParallelism\&quot;:1}}, {\&quot;id\&quot;:2,\&quot;type\&quot;:\&quot;StreamExecCalc\&quot;,\&quot;desc\&quot;:\& ot;Calc[5]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParallel m\&quot;:32768,\&quot;minParallelism\&quot;:1}}, {\&quot;id\&quot;:3,\&quot;type\&quot;:\&quot;StreamExecSink\&quot;,\&quot;desc\&quot;:\& ot;Sink: kafka_table[6]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParallel m\&quot;:32768,\&quot;minParallelism\&quot;:1}}],\&quot;edges\&quot;: [{\&quot;source\&quot;:1,\&quot;target\&quot;:2,\&quot;mode\&quot;:\&quot;PIPELINED\&quot \&quot;strategy\&quot;:\&quot;FORWARD\&quot;}, {\&quot;source\&quot;:2,\&quot;target\&quot;:3,\&quot;mode\&quot;:\&quot;PIPELINED\&quot; &quot;strategy\&quot;:\&quot;FORWARD\&quot;}],\&quot;vertices\&quot;: {\&quot;717c7b8afebbfb7137f6f0f99beb2a94\&quot;:[1,2,3]}}&quot;}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****&quot;</requestId>
```

##### 3.1.2.39 FunctionExists

Checks whether a function is registered.

**Request headers**

The FunctionExists operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:functio xists HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |

| namespac e | Strin g | Path | Yes | ververica | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
|---|---|---|---|---|---|
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
| cat | Strin g | Path | Yes | vvp | The catalog name. |
| database | Strin g | Quer y | Yes | default | The database name. |
| function | Strin g | Quer y | Yes | TransformUdtf | The function name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.FunctionE xistsResponse", "exists": true } | The detailed information. |
| requestId | String | D96DD415-AD97- 4EBA-832E- 99FADB6A4F87 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:functio xists HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &database=default &function=TransformUdtf &Common Request Parameter
```

Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.FunctionExistsResponse\",\"exist ":true}",
 "requestId":"D96DD415-AD97-4EBA-832E-99FADB6A4F87",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.FunctionExistsRespon &quot;,&quot;exists&quot;:true}</data> <requestId>D96DD415-AD97-4EBA-832E-99FADB6A4F87</requestId> <success>true</success>
```

##### 3.1.2.40 ForcefullyCreateLock

Locks a resource (typically a draft).

**Request headers**

The ForcefullyCreateLock operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/locks HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |

| namespac e | Strin g | Path | Yes | default | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
|---|---|---|---|---|---|
| workspace | Strin g | Path | Yes | flinkteam | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
| resourceTy pe | Strin g | Quer y | No | DeploymentDraft | The type of the resource to lock. To lock a draft, set this parameter to DeploymentDraft. |
| resourceId | Strin g | Quer y | No | c6f157ac-60b9-4b38- 8bad-d435387cfd59 | The ID of the resource to lock. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | 69DEC7C2-BCE5- 4E80-8CDA- FE7ADE09AAAD | The request ID. |

| data | String | { "metadata": { "createdAt": "2024-03- 12T10:16:35.1640 34Z", "modifiedAt": "2024-03- 12T10:16:35.1640 34Z", "namespace": "flinkteam", "id": "ec62ce3c-fe33- 383e-8b31- 2fe9d89af2af" }, "apiVersion": "v1", "kind": "Lock", "spec": { "holderName": "flinkadmin", "holderId": "22985261012276 3813" } } | The details of the resource lock. |
|---|---|---|---|

**Examples**

Sample requests

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/locks HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "namespace":"default", "workspace":"flinkteam"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{\"metadata\":{\"createdAt\":\"2024-03-
12T10:16:35.164034Z\",\"modifiedAt\":\"2024-03- 12T10:16:35.164034Z\",\"namespace\":\"flinkteam\",\"id\":\"ec62ce3c-fe33-383e-8b31-2fe9 d89af2af\"},\"apiVersion\":\"v1\",\"kind\":\"Lock\",\"spec\": {\"holderName\":\"flinkadmin\",\"holderId\":\"229852610122763813\"}}",
 "success":true,
 "requestId":"69DEC7C2-BCE5-4E80-8CDA-FE7ADE09AAAD"
```

`}` `XML` format

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2024-03- 12T10:16:35.164034Z&quot;,&quot;modifiedAt&quot;:&quot;2024-03- 12T10:16:35.164034Z&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;id&quot;:&quo ec62ce3c-fe33-383e-8b31- 2fe9d89af2af&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Lock&quo ,&quot;spec&quot;: {&quot;holderName&quot;:&quot;flinkadmin&quot;,&quot;holderId&quot;:&quot;229852610122763 3&quot;}}</data> <success>true</success> <requestId>69DEC7C2-BCE5-4E80-8CDA-FE7ADE09AAAD</requestId>
```

##### 3.1.2.41 ExecuteSqlscriptsStatements

Manages a function.

**Request headers**

The ExecuteSqlscriptsStatements operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:executemulti HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| paramsJso n | Strin g | Body | No | {"executeFunctionStr": ["DROP FUNCTION `TimestampProbe`"]} | Execution parameters specifying a list of SQL scripts. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.v1beta 1.ListUdfArtifactsR esponse", "udfArtifacts": [ { "name": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227", "jarUrl": "hdfs:///tmp/udf/me tric-transform- 2.2.7-shaded.jar", "udfClasses": [ { "className": "com.alibaba.blink. udtf.TimestampPro be", "classType": "UDF TYPE SCALA _ _ R", "udfArtifactName": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227", "functionNames": [ "TimestampProbe" ] } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "dependencyJarUri s": [], "uploader": "22985261012276 3813", "namespace": "namespaces/flinkt eam", "createTime": "2024-03- 11T02:54:25Z", "updateTime": "2024-03- 11T02:54:25Z", "jarUpdateTime": "2024-03- 11T02:54:25Z" } ] } | The detailed information about the function. |
| requestId | String | 151E1A19-091A- 4317-ADF9- FDD81C735414 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:executemulti HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.ListUdfArtifactsResponse\",\"udfArtifact ":[{\"name\":\"namespaces/flinkteam/udfartifacts/metric-transform- 227\",\"jarUrl\":\"hdfs:///tmp/udf/metric-transform-2.2.7-shaded.jar\",\"udfClasses\":[ {\"className\":\"com.alibaba.blink.udtf.TimestampProbe\",\"classType\":\"UDF_TYPE_SCALAR\ \"udfArtifactName\":\"namespaces/flinkteam/udfartifacts/metric-transform- 227\",\"functionNames\": [\"TimestampProbe\"]}],\"artifactType\":\"ARTIFACT_TYPE_JAVA\",\"dependencyJarUris\":[] ,\"uploader\":\"229852610122763813\",\"namespace\":\"namespaces/flinkteam\",\"createTime\ \"2024-03-11T02:54:25Z\",\"updateTime\":\"2024-03- 11T02:54:25Z\",\"jarUpdateTime\":\"2024-03-11T02:54:25Z\"}]}",
 "requestId":"151E1A19-091A-4317-ADF9-FDD81C735414",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.ListUdfArtifactsResponse&quo ,&quot;udfArtifacts&quot;: [{&quot;name&quot;:&quot;namespaces/flinkteam/udfartifacts/metric-transform-227&quot;,& quot;jarUrl&quot;:&quot;hdfs:///tmp/udf/metric-transform-2.2.7shaded.jar&quot;,&quot;udfClasses&quot;: [{&quot;className&quot;:&quot;com.alibaba.blink.udtf.TimestampProbe&quot;,&quot;classType uot;:&quot;UDF_TYPE_SCALAR&quot;,&quot;udfArtifactName&quot;:&quot;namespaces/flinkteam/u artifacts/metric-transform-227&quot;,&quot;functionNames&quot;: [&quot;TimestampProbe&quot;]}],&quot;artifactType&quot;:&quot;ARTIFACT_TYPE_JAVA&quot;,&q t;dependencyJarUris&quot;: [],&quot;uploader&quot;:&quot;229852610122763813&quot;,&quot;namespace&quot;:&quot;namesp es/flinkteam&quot;,&quot;createTime&quot;:&quot;2024-03- 11T02:54:25Z&quot;,&quot;updateTime&quot;:&quot;2024-03- 11T02:54:25Z&quot;,&quot;jarUpdateTime&quot;:&quot;2024-03-11T02:54:25Z&quot;}]}</data> <requestId>151E1A19-091A-4317-ADF9-FDD81C735414</requestId> <success>true</success>
```

##### 3.1.2.42 ExecuteSqlScript

Executes SQL scripts to manage realtime compute tasks.

**Request headers**

The ExecuteSqlScript operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:execute HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| paramsJso n | Strin g | Body | No | {"statement":"Drop TABLE `vvp`.`default`.`test`"} | The execution parameters for SQL scripts. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

| data | String | { "@type": "type.googleapis.c om/vvp.sql.v1beta 1.ExecuteStateme ntsResponse", "responses": [{ "result": "RESULT SUCCESS _ ", "errorMessages": [] }] } | The detailed information. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:execute HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "workspace":"default"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.ExecuteStatementsResponse\",\"responses\ [{\"result\":\"RESULT_SUCCESS\",\"errorMessages\":[]}]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.ExecuteStatementsResponse&qu ;,&quot;responses&quot;: [{&quot;result&quot;:&quot;RESULT_SUCCESS&quot;,&quot;errorMessages&quot;:[]}]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.43 DeployDeploymentDraft

Call the DeployDeploymentDraft API to deploy a Realtime Compute job to the specified workspace and namespace.

**Request headers**

This API uses common request headers and does not require special request headers. For more information, see the Common Request Parameter document.

**Syntax**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-drafts/deploy HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID in one of the following ways: Call ListNamespaces to obtain the ID. Obtain the ID from the workspace details in the Realtime Compute for Apache Flink fully managed development console. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |
|   |   |   |   | { "metadata": { "createdAt": "2026-04- 24T03:46:53Z", "workspace": "9cuwr9g7y1hl19", "resourceVersion": 32, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "migration.display.enabl ed": "false", "creator": "235406976657057054" , "modifier": "235406976657057054" , "creatorName": "flinkadmin", "modifierName": "flinkadmin", "priority": "5", "deployment.draft.refere nced.deployment.id": "7325ac07-e466-4c1b- b598-311c6f2c103b" }, "labels": {}, "lock": { "metadata": { |   |

| Parame ter | Typ e | Positi on | Require d | "createdAt": "2026-04- 2E4xTa0m3:p46le:53Z", "workspace": | Description |
|---|---|---|---|---|---|
|   |   |   |   | "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:46:53Z", "namespace": "flinkteam", "annotations": { "creator": "235406976657057054" , "modifier": |   |
| paramsJso n | Strin g | Body | No | "235406976657057054" }, "id": "313fde08-4b44- 38b5-99c4- 7f3038449796" }, "apiVersion": "v1", "kind": "Lock", "spec": { "holderName": "flinkadmin", "holderId": "235406976657057054" } }, "id": "cee26b6e- d03b-4a03-a628- a6fe665c525e", "parentId": "cd1562be- 02ed-32cf-945b- 9769afe4c55e", "description": "cd1562be-02ed-32cf- 945b-9769afe4c55e" }, "spec": { "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "restoreStrategy": { "kind": "LATEST STATE" _ }, "deploymentTargetId": "a89ff052-38c6-4fd3- 9b91-e9c53f8ee019", "maxSavepointCreation Attempts": 4, "maxJobCreationAttempt s": 1, "template": { "metadata": { "annotations": { "flink.resource.type": "fine-grained", "native.kubernetes.mod e": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.enable d": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "versionName": "vvr- 8.0.7-flink-1.17", "imageUserDefined": false, "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); | The execution parameters and the SQL script. |

| Parame ter | Typ e | Positi on | Require d | CREATE TEMPORARY TEAxBaLmE p`klaefka _table` (strname VARCHAR, lens | Description |
|---|---|---|---|---|---|
|   |   |   |   | BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;" }, _ "parallelism": 1, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "flinkConfiguration": {}, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "batchMode": false } } } } |   |

**Response data**

| success | Boolean | true | Indicates whether the request is successful. |
|---|---|---|---|
| data | String |   | Details. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

**Examples**

Sample request

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-drafts/deploy HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam"
```

`}` Sample success response `JSON` format `XML` format

##### 3.1.2.44 DeleteUdfArtifact

Deletes a UDF.

**Request headers**

The DeleteUdfArtifact operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactN e] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
| namespac e | Strin g | Path | Yes | ververica | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| udfArtifact Name | Strin g | Path | Yes | metric-transform-227- shaded | The UDF name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| data | String | { "referencedClasses ": [], "@type": "type.googleapis.c om/vvp.sql.v1beta 1.DeleteUdfArtifact Response" } | The detailed information. |
|---|---|---|---|
| requestId | String | 07E49735-A389- 4853-AFBA- 28F9EB0EFDC4 | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactN e] HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &namespace=ververica &udfArtifactName=metric-transform-227-shaded &Common Request Parameter
```

Sample success responses `JSON` format `{`

```json
 "data":"{\"referencedClasses\":
[],\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.DeleteUdfArtifactResponse\"}",
 "requestId": "07E49735-A389-4853-AFBA-28F9EB0EFDC4",
 "success":true
```

`}` `XML` format

```xml
<data>{&quot;referencedClasses&quot;: [],&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.DeleteUdfArtifactResponse& ot;}</data> <requestId>07E49735-A389-4853-AFBA-28F9EB0EFDC4</requestId> <success>true</success>
```

##### 3.1.2.45 DeleteSecretValue

Deletes a variable.

**Request headers**

The DeleteSecretValue operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values/[name] H TTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Host | Yes | cn-qingdao- env***-d01 | The region ID. |
| namespace | String | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| workspace | String | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
| name | String | Path | No | secretKey | The variable name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | 1CCA8A71-98C6- 491B-9A2D- ADDFC0939294 | The request ID. |

**Examples**

Sample requests

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values/[name] H TTP/1.1 &RegionId=cn-qingdao-env***-d01 &namespace=flinkteam &workspace=default &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "success":true,
 "requestId":"1CCA8A71-98C6-491B-9A2D-ADDFC0939294"
```

`}` `XML` format

```xml
<success>true</success> <requestId>1CCA8A71-98C6-491B-9A2D-ADDFC0939294</requestId>
```

##### 3.1.2.46 DeleteMember

Call DeleteMember to revoke the business authorization of a specified user.

**Request headers**

This API uses common request headers and does not have special request headers. For more information, see the common request parameter documentation.

**Syntax**

```
DELETE /pop/workspaces/[workspace]/members/v1/namespaces/[namespace]/members/[member] H TTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call ListNamespaces to obtain the ID. Obtain the ID from the workspace details in the Realtime Compute for Apache Flink fully managed development console. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |
| member | Strin g | Path | Yes | user:242425410145292 209 | The information about the user whose authorization you want to revoke. Format: user:${uid}. |
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The name of the region. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | 8AA170D4-F4D1- 4E90-A02D- 0CC211BE8171 | The request ID. |

**Examples**

Sample requests

```
DELETE /pop/workspaces/[workspace]/members/v1/namespaces/[namespace]/members/[member] H TTP/1.1 &workspace=default &namespace=flinkteam &member=user:242425410145292209 &RegionId=cn-wulan-env***-d01 &Common Request Parameter
```

Sample success responses `JSON` format `{`

```json
 "success":true,
 "requestId":"8AA170D4-F4D1-4E90-A02D-0CC211BE8171"
```

`}` `XML` format

```xml
<success>true</success> <requestId>8AA170D4-F4D1-4E90-A02D-0CC211BE8171</requestId>
```

##### 3.1.2.47 DeleteFormat

Call DeleteFormat to delete a format.

**Request headers**

This API uses common request headers and does not have special request headers. For more information, see Common Request Parameters.

**Syntax**

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HT TP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call ListNamespaces to obtain the ID. Obtain the ID from the workspace details in the Realtime Compute for Apache Flink fully managed development console. |
| name | Strin g | Path | Yes | customized-csv | The name of the format to delete. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | EC30D915-1E89- 4B66-B1AA- C5D161DAB50D | The request ID. |

**Examples**

Request example

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HT TP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &name=customized-csv &namespace=flinkteam &Common request parameters
```

Successful response example `JSON` format `{`

```json
 "requestId":"EC30D915-1E89-4B66-B1AA-C5D161DAB50D"
```

`}` `XML` format

```xml
<requestId>EC30D915-1E89-4B66-B1AA-C5D161DAB50D</requestId>
```

##### 3.1.2.48 DeleteFolder

Deletes a folder on the data development page.

**Request headers**

The DeleteFolder operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders/[folderId] HTT P/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
|---|---|---|---|---|---|
| folderId | Strin g | Path | Yes | 123 | The folder ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders/[folderId] HTT P/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &namespace=flinkteam &folderId=123 &Common request parameters
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

##### 3.1.2.49 DeleteDeployment

Deletes a deployment resource and releases related workloads and associated components.

**Request headers**

The DeleteDeployment operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HT TP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| deploymen tId | Strin g | Path | Yes | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | The job ID. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HT TP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7def580c00 &workspace=default &Common request parameters
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

##### 3.1.2.50 DeleteConnector

Deletes a custom connector.

**Request headers**

The DeleteConnector operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

| name | Strin g | Path | Yes | hologres-fix | The name of the connector to delete. |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | 7113AD53-5192- 46E5-B592- 81175BAF7F54 | The request ID. |

**Examples**

Sample requests

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &name=hologres-fix &namespace=flinkteam &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "success":true,
 "requestId":"7113AD53-5192-46E5-B592-81175BAF7F54"
```

`}` `XML` format

```xml
<success>true</success> <requestId>7113AD53-5192-46E5-B592-81175BAF7F54</requestId>
```

##### 3.1.2.51 DeleteArtifact

Deletes an artifact file in Realtime Compute for Apache Flink.

**Request headers**

The DeleteArtifact operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
DELETE /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:delete HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| filename | Strin g | Quer y | Yes | test.csv | The file name. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
DELETE /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:delete HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &filename=test.csv &workspace=default &Common request parameters
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

##### 3.1.2.52 DatabaseExists

Checks whether a database exists under a catalog.

**Request headers**

The DatabaseExists operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:databas xists HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | ververica | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |

| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
|---|---|---|---|---|---|
| cat | Strin g | Path | Yes | vvp | The catalog name. |
| database | Strin g | Quer y | Yes | default | The name of the database under a catalog. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.catalog. v1beta2.Database ExistsResponse", "exists": true } | The detailed information. |
| requestId | String | 41CAB2BF-B428- 4240-A746- 1F6CE6DE**** | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:databas xists HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=ververica &workspace=default &cat=vvp &database=default &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.catalog.v1beta2.DatabaseExistsResponse\",\"exist ":true}",
 "requestId":"41CAB2BF-B428-4240-A746-1F6CE6DE****",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.catalog.v1beta2.DatabaseExistsRespon &quot;,&quot;exists&quot;:true}</data> <requestId>41CAB2BF-B428-4240-A746-1F6CE6DE****</requestId> <success>true</success>
```

##### 3.1.2.53 CreateUdfArtifact

Call CreateUdfArtifact to create a UDF.

**Request headers**

This API uses common request headers and does not require special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts HTTP/1
```

`.1`

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-qingdao-env***-d01 | The region ID. |
| paramsJso n | Strin g | Body | No | {"name": "metric- transform-2.2.7- shaded", "jarUrl": "http://flink- resource.oss-cn-wulan- env**-d01- a.intra.env**.shuguang.c om/udx/metric- transform-2.2.7- shaded.jar"} | The UDF parameters. Specify the storage path of the JAR package and the name of the UDF to create. Note: The UDF JAR at the specified path must exist. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID by using one of the following methods: Call the ListNamespaces operation. View the workspace details in the Realtime Compute for Apache Flink fully managed development console. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.c om/vvp.sql.v1beta 1.CreateUdfArtifact Response", "collidingClasses": [], "udfArtifact": { "dependencyJarUri s": [], "udfClasses": [ { "functionNames": [], "udfArtifactName": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227", "className": "com.alibaba.blink. udtf.TimestampPro be", "classType": "UDF TYPE SCALA _ _ R" }, { "functionNames": [], "udfArtifactName": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227", "className": "com.alibaba.blink. udtf.TransformUdtf ", "classType": "UDF TYPE TABLE" _ _ } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "createTime": "2024-03- 11T02:54:24.8227 66Z", "uploader": "22985261012276 3813", "jarUpdateTime": "2024-03- 11T02:54:24.8227 66Z", "name": "namespaces/flinkt eam/udfartifacts/m etric-transform- 227", "namespace": "flinkteam", "jarUrl": "hdfs:///tmp/udf/me tric-transform- 2.2.7-shaded.jar", "updateTime": "2024-03- 11T02:54:24.8227 66Z" } } | The detailed information. |
| requestId | String | 8F0CFB56-7CE8- 45AA-A788- 41B7D2504E5F | The request ID. |

| Realtime Compute |   |   | nk (Compute-Storage Separation Edition) Developer Guide·AppM nager AP |
|---|---|---|---|
| Parameter | Type | Example | Description |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts HTTP/1
```

`.1` `{`

```json
"RegionId":"cn-qingdao-env***-d01", "workspace":"default", "namespace":"flinkteam"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.CreateUdfArtifactResponse\",\"collidingC sses\":[],\"udfArtifact\":{\"dependencyJarUris\":[],\"udfClasses\":[{\"functionNames\": [],\"udfArtifactName\":\"namespaces/flinkteam/udfartifacts/metric-transform-227\",\"cla ssName\":\"com.alibaba.blink.udtf.TimestampProbe\",\"classType\":\"UDF_TYPE_SCALAR\"},{ \"functionNames\":[],\"udfArtifactName\":\"namespaces/flinkteam/udfartifacts/metric-tra nsform- 227\",\"className\":\"com.alibaba.blink.udtf.TransformUdtf\",\"classType\":\"UDF_TYPE_TAB \"}],\"artifactType\":\"ARTIFACT_TYPE_JAVA\",\"createTime\":\"2024-03- 11T02:54:24.822766Z\",\"uploader\":\"229852610122763813\",\"jarUpdateTime\":\"2024-03-1 1T02:54:24.822766Z\",\"name\":\"namespaces/flinkteam/udfartifacts/metric-transform-227\ ",\"namespace\":\"flinkteam\",\"jarUrl\":\"hdfs:///tmp/udf/metric-transform-2.2.7-shade d.jar\",\"updateTime\":\"2024-03-11T02:54:24.822766Z\"}}",
 "requestId":"8F0CFB56-7CE8-45AA-A788-41B7D2504E5F",
 "success":true
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.CreateUdfArtifactResponse&qu ;,&quot;collidingClasses&quot;:[],&quot;udfArtifact&quot;: {&quot;dependencyJarUris&quot;:[],&quot;udfClasses&quot;:[{&quot;functionNames&quot;:[] ,&quot;udfArtifactName&quot;:&quot;namespaces/flinkteam/udfartifacts/metric-transform-2 27&quot;,&quot;className&quot;:&quot;com.alibaba.blink.udtf.TimestampProbe&quot;,&quot;cl sType&quot;:&quot;UDF_TYPE_SCALAR&quot;},{&quot;functionNames&quot;: [],&quot;udfArtifactName&quot;:&quot;namespaces/flinkteam/udfartifacts/metric-transform
```

`-`

```xml
227&quot;,&quot;className&quot;:&quot;com.alibaba.blink.udtf.TransformUdtf&quot;,&quot;cl sType&quot;:&quot;UDF_TYPE_TABLE&quot;}],&quot;artifactType&quot;:&quot;ARTIFACT_TYPE_JAV quot;,&quot;createTime&quot;:&quot;2024-03- 11T02:54:24.822766Z&quot;,&quot;uploader&quot;:&quot;229852610122763813&quot;,&quot;jarUp teTime&quot;:&quot;2024-03- 11T02:54:24.822766Z&quot;,&quot;name&quot;:&quot;namespaces/flinkteam/udfartifacts/metric transform- 227&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;jarUrl&quot;:&quot;hdfs:///tm udf/metric-transform-2.2.7-shaded.jar&quot;,&quot;updateTime&quot;:&quot;2024-03-11T02: 54:24.822766Z&quot;}}</data> <requestId>8F0CFB56-7CE8-45AA-A788-41B7D2504E5F</requestId> <success>true</success>
```

##### 3.1.2.54 CreateSecretValue

Adds a variable.

**Request headers**

The CreateSecretValue operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
|---|---|---|---|---|---|
| paramsJso n | Strin g | Body | No | { "metadata": { "name": "flink access id", _ _ "workspace": "9cuwr9g7y1hl19", "namespace": "flinkteam" }, "spec": { "kind": "Plain", "value": "flink access key" } } _ _ | Request parameters specifying the variable name and values. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| data | String | { "eagleEyeTraceId": "0a2318ab177734 16617444310d**** ", "asapiSuccess": true, "asapiRequestId": "5EBEB7CA-1133- 4746-8132- A35DC078****", "data": { "metadata": { "createdAt": "2026-04- 28T02:01:01.7911 72Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 28T02:01:01.7911 72Z", "resourceVersion": 1, "name": "flink access id", _ _ "namespace": "flinkteam", "annotations": { "creator": "23540697665705 ****", "modifier": "23540697665705 ****", "creatorName": "flinkadmin", "modifierName": "flinkadmin" }, "id": "c73a06e7- c2d2-4d78-9dbe- 87413280****", "labels": {} }, "apiVersion": "v1", "kind": "SecretValue", "spec": { "kind": "Plain", "value": "flink access key" _ _ } } | The detailed information. |
|---|---|---|---|
| requestId | String | 19E71203-97A1- 4355-8C25- D566CA82**** | The request ID. |

**Examples**

Sample requests

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"
{\"eagleEyeTraceId\":\"0a2318ab17773416617444310d****\",\"asapiSuccess\":true,\"asapiRequ tId\":\"5EBEB7CA-1133-4746-8132-A35DC078****\",\"data\":{\"metadata\": {\"createdAt\":\"2026-04- 28T02:01:01.791172Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04-28T02:0 1:01.791172Z\",\"resourceVersion\":1,\"name\":\"flink_access_id\",\"namespace\":\"flinkte \",\"annotations\": {\"creator\":\"23540697665705****\",\"modifier\":\"23540697665705****\",\"creatorName\":\ linkadmin\",\"modifierName\":\"flinkadmin\"},\"id\":\"c73a06e7-c2d2-4d78-9dbe-87413280*
***\",\"labels\":{}},\"apiVersion\":\"v1\",\"kind\":\"SecretValue\",\"spec\":{\"kind\":
\"Plain\",\"value\":\"flink_access_key\"}}",
 "success":true,
 "requestId":"19E71203-97A1-4355-8C25-D566CA82****"
```

`}` `XML` format

```xml
<data> {&quot;eagleEyeTraceId&quot;:&quot;0a2318ab17773416617444310d****&quot;,&quot;asapiSucces quot;:true,&quot;asapiRequestId&quot;:&quot;5EBEB7CA-1133-4746-8132- A35DC078****&quot;,&quot;data&quot;:{&quot;metadata&quot;: {&quot;createdAt&quot;:&quot;2026-04- 28T02:01:01.791172Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modified &quot;:&quot;2026-04- 28T02:01:01.791172Z&quot;,&quot;resourceVersion&quot;:1,&quot;name&quot;:&quot;flink_acce _id&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;:{&quot;cr eator&quot;:&quot;23540697665705****&quot;,&quot;modifier&quot;:&quot;23540697665705****& ot;,&quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;modifierName&quot;:&quot;flinkad n&quot;},&quot;id&quot;:&quot;c73a06e7-c2d2-4d78-9dbe- 87413280****&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;SecretValue&quot;,&quot; ec&quot;: {&quot;kind&quot;:&quot;Plain&quot;,&quot;value&quot;:&quot;flink_access_key&quot;}}</d ata> <success>true</success> <requestId>19E71203-97A1-4355-8C25-D566CA82****</requestId>
```

##### 3.1.2.55 CreateSavepoint

Creates a savepoint, which marks a rollback point within a transaction.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Hea der | Yes | cn-wulan-env***-d01 | The region ID. |

**Syntax**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/savepoints HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| paramsJso n | Strin g | Body | No | { "deploymentId": "7325ac07-e466-4c1b- b598-311c6f2c103b" } | Execution parameters specifying a list of SQL scripts. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| data | String | { "metadata": { "createdAt": "2026-04- 28T02:13:28.2772 78Z", "jobId": "bf735437-b3ea- 4d1a-847e- bbacd144****", "workspace": "9cuwr9g7y1hl19", "nativeFormat": false, "modifiedAt": "2026-04- 28T02:13:28.2772 78Z", "deploymentId": "7325ac07-e466- 4c1b-b598- 311c6f2c103b", "origin": "USER REQUEST", _ "resourceVersion": 1, "namespace": "flinkteam", "annotations": { "com.dataartisans. appmanager.contr oller.deployment.s pec.version": "10", "taker": " \| vvp-0" }, "id": "425dfb74- 2bbb-4879-8273- 0b087a97****" }, "apiVersion": "v1", "kind": "Savepoint", "spec": { "savepointLocation ": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/fli nk- savepoints/namesp aces/flinkteam/dep loyments/7325ac0 7-e466-4c1b-b598- 311c6f2c103b/425 dfb74-2bbb-4879- 8273- 0b087a97b502" }, "status": { "state": "STARTED" } } | The detailed information. |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

| success | Boolean | true | Indicates whether the request is successful. |
|---|---|---|---|

**Examples**

Sample requests

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/savepoints HTTP/1.1
```

`{`

```json
"namespace":"flinkteam", "workspace":"default"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
28T02:13:28.277278Z\",\"jobId\":\"bf735437-b3ea-4d1a-847ebbacd144****\",\"workspace\":\"9cuwr9g7y1hl19\",\"nativeFormat\":false,\"modifiedAt\":\"2 6-04-28T02:13:28.277278Z\",\"deploymentId\":\"7325ac07-e466-4c1b-b598- 311c6f2c103b\",\"origin\":\"USER_REQUEST\",\"resourceVersion\":1,\"namespace\":\"flinktea ",\"annotations\": {\"com.dataartisans.appmanager.controller.deployment.spec.version\":\"10\",\"taker\":\"
| vvp-0\"},\"id\":\"425dfb74-2bbb-4879-8273-
0b087a97****\"},\"apiVersion\":\"v1\",\"kind\":\"Savepoint\",\"spec\": {\"savepointLocation\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flinksavepoints/namespaces/flinkteam/deployments/7325ac07-e466-4c1b-b598- 311c6f2c103b/425dfb74-2bbb-4879-8273-0b087a97b502\"},\"status\": {\"state\":\"STARTED\"}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 28T02:13:28.277278Z&quot;,&quot;jobId&quot;:&quot;bf735437-b3ea-4d1a-847ebbacd144****&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;nativeFormat&qu ;:false,&quot;modifiedAt&quot;:&quot;2026-04- 28T02:13:28.277278Z&quot;,&quot;deploymentId&quot;:&quot;7325ac07-e466-4c1b-b598-311c6f 2c103b&quot;,&quot;origin&quot;:&quot;USER_REQUEST&quot;,&quot;resourceVersion&quot;:1,&q t;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;com.dataartisans.appmanager.controller.deployment.spec.version&quot;:&quot;10&quot &quot;taker&quot;:&quot; | vvp-0&quot;},&quot;id&quot;:&quot;425dfb74-2bbb-4879-8273-0b 087a97****&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Savepoint& ot;,&quot;spec&quot;:{&quot;savepointLocation&quot;:&quot;oss://flink-fullymanaged-9cuw r9g7y1hl19/flink-savepoints/namespaces/flinkteam/deployments/7325ac07-e466-4c1b-b598-31 1c6f2c103b/425dfb74-2bbb-4879-8273-0b087a97b502&quot;},&quot;status&quot;: {&quot;state&quot;:&quot;STARTED&quot;}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.56 CreateMember

Call CreateMember to assign business permissions to a user in a specified namespace.

**Request headers**

This API operation uses common request headers and does not have special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
POST /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| paramsJso n | Strin g | Body | No | { "role": "viewer", "member": "242425410145292209" } | The authorization information of the user. This parameter grants specified business permissions to a specified user. Valid permission values: viewer, owner, and editor. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the workspace ID by using one of the following methods: Call ListNamespaces to obtain the workspace ID. View the workspace ID in the workspace details on the Flink Serverless development console. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The name of the region. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | E3D311D5-77CB- 452F-B9EA- C215C8201363 | The ID of the request. |
| data | String | { "@type": "type.googleapis.c om/vvp.members.v 1.CreateMemberRe sponse", "member": { "role": "viewer", "member": "user:2424254101 45292209" } } | The detailed information about the business authorization of the user. |

**Examples**

Sample requests

```
POST /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1
```

`{`

```json
"workspace":"default", "namespace":"flinkteam", "RegionId":"cn-wulan-env***-d01"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.members.v1.CreateMemberResponse\",\"member\":{\"ro le\":\"viewer\",\"member\":\"user:242425410145292209\"}}",
 "success":true,
 "requestId":"E3D311D5-77CB-452F-B9EA-C215C8201363"
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.members.v1.CreateMemberResponse&quot;,&q t;member&quot;: {&quot;role&quot;:&quot;viewer&quot;,&quot;member&quot;:&quot;user:242425410145292209&quo }}</data> <success>true</success> <requestId>E3D311D5-77CB-452F-B9EA-C215C8201363</requestId>
```

##### 3.1.2.57 CreateFormat

Creates a format.

**Request headers**

The CreateFormat operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |

| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| paramsJso n | Strin g | Body | No | {"creator": "", "sink": false, "modifier": "", "name": "namespaces/flinkteam/fo rmats/customized-csv", "creator name": "", _ "source": true, "modifier name": "", _ "type": "customized-csv", "version name": "", _ "properties": [{"defaultValue": ",", "description": "", "definesFormat": false, "key": "format.column- delimiter", "required": false}], "packaged": false, "dependencies": ["http://flink-resource.oss- cn-wulan-env**-d01- a.intra.env**.shuguang.c om/format/customized- csv-demo-1.0- SNAPSHOT.jar"]} | Parameters for creating custom formats. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| data | String | { "@type": "type.googleapis.c om/vvp.sql.v1beta 1.CreateFormatRes ponse", "format": { "sink": false, "name": "namespaces/flinkt eam/formats/custo mized-csv", "source": true, "type": "customized-csv", "properties": [ { "defaultValue": ",", "description": "", "definesFormat": false, "key": "format.column- delimiter", "required": false } ], "packaged": false, "dependencies": [ "hdfs:///tmp/myfor mats/customized- csv-demo-1.0- SNAPSHOT.jar" ] } } | The details of the new format. |
|---|---|---|---|
| requestId | String | 0ED81455-6971- 4EBA-BBD4- 3F686175080D | The request ID. |

**Examples**

Sample requests

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.CreateFormatResponse\",\"format\":{\"s ink\":false,\"name\":\"namespaces/flinkteam/formats/customizedcsv\",\"source\":true,\"type\":\"customized-csv\",\"properties\": [{\"defaultValue\":\",\",\"description\":\"\",\"definesFormat\":false,\"key\":\"format.co mn-delimiter\",\"required\":false}],\"packaged\":false,\"dependencies\": [\"hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar\"]}}",
 "success":true,
 "requestId":"0ED81455-6971-4EBA-BBD4-3F686175080D"
```

`}` `XML` format

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.CreateFormatResponse&quot;,& ot;format&quot;: {&quot;sink&quot;:false,&quot;name&quot;:&quot;namespaces/flinkteam/formats/customizedcsv&quot;,&quot;source&quot;:true,&quot;type&quot;:&quot;customizedcsv&quot;,&quot;properties&quot;: [{&quot;defaultValue&quot;:&quot;,&quot;,&quot;description&quot;:&quot;&quot;,&quot;defin Format&quot;:false,&quot;key&quot;:&quot;format.columndelimiter&quot;,&quot;required&quot;:false}],&quot;packaged&quot;:false,&quot;dependencie quot;:[&quot;hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar&quot;]}}</data> <success>true</success> <requestId>0ED81455-6971-4EBA-BBD4-3F686175080D</requestId>
```

##### 3.1.2.58 CreateDeployment

Call CreateDeployment to create a deployed job.

**Request headers**

This API uses common request headers and requires no special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The name of the region. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |

| ealtime Com | pute |   |   | Realti nk (Co Editio | me Compute for Apache Fl mpute-Storage Separation n) Developer Guide·AppM |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| paramsJso n | Strin g | Body | No | { "name": "namespaces/flinkteam/f ormats/customized-csv", "type": "customized- csv", "source": true, "sink": false, "properties": [ { "key": "format.column- delimiter", "required": false, "defaultValue": ",", "description": "" } ], "dependencies": [ "hdfs:///tmp/myformats/ customized-csv-demo- 1.0-SNAPSHOT.jar" ] } | The execution parameters and SQL scripts. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID in one of the following ways: Call ListNamespaces to obtain the ID. Obtain the ID from the workspace details page in the Realtime Compute for Apache Flink fully managed development console. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The Request ID. |
|   |   | { "metadata": { "createdAt": "2026-04- 24T03:46:53.3424 84Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:46:53.3424 84Z", "resourceVersion": 1, "name": "sqlJob", "namespace": "flinkteam", |   |

|   |   | "annotations": { |   |
|---|---|---|---|
| Parameter | Type | Example "migration.display. | Description |
| data | String | enabled": "false", "creator": "23540697665705 7054", "modifier": "23540697665705 7054", "creatorName": "flinkadmin", "modifierName": "flinkadmin", "priority": "5" }, "description": "cd1562be-02ed- 32cf-945b- 9769afe4c55e", "lock": { "metadata": { "createdAt": "2026-04- 24T03:46:53Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:46:53Z", "namespace": "flinkteam", "annotations": { "creator": "23540697665705 7054", "modifier": "23540697665705 7054" }, "id": "313fde08-4b44- 38b5-99c4- 7f3038449796" }, "apiVersion": "v1", "kind": "Lock", "spec": { "holderName": "flinkadmin", "holderId": "23540697665705 7054" } }, "id": "cee26b6e-d03b- 4a03-a628- a6fe665c525e", "parentId": "cd1562be-02ed- 32cf-945b- 9769afe4c55e", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentDraft" , "spec": { "template": { "metadata": { "annotations": { "native.kubernetes .mode": "true", "flink.queryable- state.enabled": "false", | The detailed information. |

| Parameter | Type | "flink.security.ssl.e Example nabled": "false" } | Description |
|---|---|---|---|
|   |   | }, "spec": { "artifact": { "kind": "SQLSCRIPT", "sqlScript": "INSERT INTO mySink SELECT SUBSTRING(a,0,10) AS a, CAST(CHAR LENGT _ H(a) AS BIGINT) as cnt FROM mySource;", "imageUserDefined ": false, "versionName": "vvr-8.0.7-flink- 1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 1.0 }, "taskmanager": { "memory": "4Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration" : {} } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestored State": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "maxSavepointCre ationAttempts": 4, "maxJobCreationAt tempts": 1, "deploymentTarget Id": "a89ff052- 38c6-4fd3-9b91- |   |

e9c53f8ee019" } }

**Examples**

Sample requests

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "workspace":"default"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:46:53.342484Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04-24T03:4 6:53.342484Z\",\"resourceVersion\":1,\"name\":\"sqlJob\",\"namespace\":\"flinkteam\",\"an tations\": {\"migration.display.enabled\":\"false\",\"creator\":\"235406976657057054\",\"modifier\": 235406976657057054\",\"creatorName\":\"flinkadmin\",\"modifierName\":\"flinkadmin\",\"pri ity\":\"5\"},\"description\":\"cd1562be-02ed-32cf-945b-9769afe4c55e\",\"lock\":{\"metad ata\":{\"createdAt\":\"2026-04- 24T03:46:53Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:46:53Z\",\"namespace\":\"flinkteam\",\"annotations\": {\"creator\":\"235406976657057054\",\"modifier\":\"235406976657057054\"},\"id\":\"313fde0 4b44-38b5-99c4-7f3038449796\"},\"apiVersion\":\"v1\",\"kind\":\"Lock\",\"spec\":{\"hold erName\":\"flinkadmin\",\"holderId\":\"235406976657057054\"}},\"id\":\"cee26b6e-d03b-4a 03-a628-a6fe665c525e\",\"parentId\":\"cd1562be-02ed-32cf-945b- 9769afe4c55e\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"DeploymentDraft\",\"spec\":{\"template\":{\"metada ta\":{\"annotations\":{\"native.kubernetes.mode\":\"true\",\"flink.queryable-state.enab led\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\":{\"artifact\":{\"ki nd\":\"SQLSCRIPT\",\"sqlScript\":\"INSERT INTO mySink SELECT SUBSTRING(a,0,10) AS a, CA ST(CHAR_LENGTH(a) AS BIGINT) as cnt FROM mySource;\",\"imageUserDefined\":false,\"versionName\":\"vvr-8.0.7-flink- 1.17\"},\"parallelism\":1,\"batchMode\":false,\"resources\":{\"jobmanager\": {\"memory\":\"4Gi\",\"cpu\":1.0},\"taskmanager\": {\"memory\":\"4Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfig ation\":{}}},\"restoreStrategy\": {\"kind\":\"LATEST_STATE\",\"allowNonRestoredState\":false},\"state\":\"CANCELLED\",\"upg deStrategy\": {\"kind\":\"STATELESS\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1, deploymentTargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"}}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
```

`}` `XML` format

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:46:53.342484Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modified &quot;:&quot;2026-04- 24T03:46:53.342484Z&quot;,&quot;resourceVersion&quot;:1,&quot;name&quot;:&quot;sqlJob&quo ,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;migration.display.enabled&quot;:&quot;false&quot;,&quot;creator&quot;:&quot;235406 6657057054&quot;,&quot;modifier&quot;:&quot;235406976657057054&quot;,&quot;creatorName&qu ;:&quot;flinkadmin&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;priority&q t;:&quot;5&quot;},&quot;description&quot;:&quot;cd1562be-02ed-32cf-945b- 9769afe4c55e&quot;,&quot;lock&quot;:{&quot;metadata&quot;: {&quot;createdAt&quot;:&quot;2026-04- 24T03:46:53Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot &quot;2026-04- 24T03:46:53Z&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;modifier&quot;:&quot;2354069766 057054&quot;},&quot;id&quot;:&quot;313fde08-4b44-38b5-99c4- 7f3038449796&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Lock&quo ,&quot;spec&quot;: {&quot;holderName&quot;:&quot;flinkadmin&quot;,&quot;holderId&quot;:&quot;235406976657057 4&quot;}},&quot;id&quot;:&quot;cee26b6e-d03b-4a03-a628a6fe665c525e&quot;,&quot;parentId&quot;:&quot;cd1562be-02ed-32cf-945b- 9769afe4c55e&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;DeploymentDraft&quot;,&q t;spec&quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;:{&quo t;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;flink.queryablestate.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false& ot;}},&quot;spec&quot;:{&quot;artifact&quot;: {&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;INSERT INTO mySink SELECT SUBSTRING(a,0,10) AS a, CAST(CHAR_LENGTH(a) AS BIGINT) as cnt FROM mySource;&quot;,&quot;imageUserDefined&quot;:false,&quot;versionName&quot;:&quot;vvr-8. 0.7-flink- 1.17&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;: {&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:1.0},&quot;taskmanager&quot;:{&quot ;memory&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;: {&quot;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&q t;default&quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;:{&quot ;kind&quot;:&quot;LATEST_STATE&quot;,&quot;allowNonRestoredState&quot;:false},&quot;state uot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;STATELESS&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot axJobCreationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9 b91-e9c53f8ee019&quot;}}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

##### 3.1.2.59 CreateConnector

Creates a connector.

**Request headers**

The CreateConnector operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |

| paramsJso n | Strin g | Body | No | { "type": "hologres-fix", "name": "namespaces/flinkteam/c onnectors/hologres-fix", "packaged": false, "source": true, "sink": true, "lookup": false, "dependencies": [ "hdfs:///vvp/data/sql- artifacts/namespaces/flin kteam/custom- connectors/2024-03- 11T05-51- 25.289740Z/ververica- connector-hologres-1.15- vvr-6.0-fix.jar" ], "supportedFormats": [ "json","csv" ], "properties": [ { "key": "connector", "required": true, "defaultValue": "hologres-fix", "description": "", "definesFormat": false }, { "key": "dbname", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "endpoint", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "tablename", "required": true, "defaultValue": "", "description": "", "definesFormat": false } ] } | Parameters of the new connector, including: type, name, supported connection parameters, source and sink capabilities, supported data formats, and dependent JAR paths. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| ager API |   |   |   |
|---|---|---|---|
| data | String | { "connector": { "lookup": true, "supportedFormats ": [ "json", "csv" ], "environments": [], "sink": true, "name": "namespaces/flinkt eam/connectors/ho logres-fix", "source": true, "type": "hologres- fix", "properties": [ { "defaultValue": "hologres-fix", "description": "", "definesFormat": false, "key": "connector", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "dbname", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "endpoint", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "tablename", "required": true } ], "packaged": false, "dependencies": [ "hdfs:///tmp/mycon nectors/ververica- connector- hologres-1.15-vvr- 6.0-fix.jar" ] }, "@type": "type.googleapis.c om/vvp.sql.v1beta 1.CreateConnector Response" } | The details of the new connector. |
| 32 |   |   | > Document Version: 2026082 |

| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
|---|---|---|---|

**Examples**

Sample requests

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{\"connector\":{\"lookup\":true,\"supportedFormats\":
[\"json\",\"csv\"],\"environments\": [],\"sink\":true,\"name\":\"namespaces/flinkteam/connectors/hologresfix\",\"source\":true,\"type\":\"hologres-fix\",\"properties\": [{\"defaultValue\":\"hologresfix\",\"description\":\"\",\"definesFormat\":false,\"key\":\"connector\",\"required\":tru
```

`,`

```json
{\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"dbname\",\" quired\":true}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"endpoint\", required\":true}, {\"defaultValue\":\"\",\"description\":\"\",\"definesFormat\":false,\"key\":\"tablename\" "required\":true}],\"packaged\":false,\"dependencies\": [\"hdfs:///tmp/myconnectors/ververica-connector-hologres-1.15-vvr-6.0fix.jar\"]},\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.CreateConnectorResponse\"}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
```

`}` `XML` format

```xml
<data>{&quot;connector&quot;:{&quot;lookup&quot;:true,&quot;supportedFormats&quot;:[&qu ot;json&quot;,&quot;csv&quot;],&quot;environments&quot;: [],&quot;sink&quot;:true,&quot;name&quot;:&quot;namespaces/flinkteam/connectors/hologresfix&quot;,&quot;source&quot;:true,&quot;type&quot;:&quot;hologresfix&quot;,&quot;properties&quot;:[{&quot;defaultValue&quot;:&quot;hologresfix&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFormat&quot;:false,&quot;key& ot;:&quot;connector&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;dbname&quot;,&quot;required&quot;:true},{&quot;d efaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;definesFormat&q t;:false,&quot;key&quot;:&quot;endpoint&quot;,&quot;required&quot;:true}, {&quot;defaultValue&quot;:&quot;&quot;,&quot;description&quot;:&quot;&quot;,&quot;defines rmat&quot;:false,&quot;key&quot;:&quot;tablename&quot;,&quot;required&quot;:true}],&quot; ckaged&quot;:false,&quot;dependencies&quot;:[&quot;hdfs:///tmp/myconnectors/ververica-c onnector-hologres-1.15-vvr-6.0fix.jar&quot;]},&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.CreateConnect Response&quot;}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

##### 3.1.2.60 CreateFolder

Call CreateFolder to create a folder on the data development page.

**Request headers**

This operation uses common request headers and does not require special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The name of the region. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the ID in one of the following ways: Call ListNamespaces to obtain the ID. Obtain the ID from the workspace details in the fully managed Flink development console. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |
| paramsJso n | Strin g | Body | No | { "metadata": { "parentId": "cd1562be- 02ed-32cf-945b- 9769afe4****", "name": "changsha", "namespace": "flinkteam" } } | The execution parameters and SQL scripts. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the business request succeeded. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "eagleEyeTraceId": "0a2318ab177734 16555583153d**** ", "asapiSuccess": true, "asapiRequestId": "A11B1055-5AB7- 4AB4-AEB0- 32947AEB****", "data": { "metadata": { "createdAt": "2026-04- 28T02:00:55.598** **", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 28T02:00:55.598** **", "namespace": "flinkteam", "name": "changsha", "annotations": { "creator": "23540697665705 ****", "modifier": "23540697665705 ****", "creatorName": "flinkadmin", "modifierName": "flinkadmin" }, "id": "6b252d46- 8653-4d69-9183- 1a16b5a8****", "type": "development", "parentId": "cd1562be-02ed- 32cf-945b- 9769afe4****" }, "apiVersion": "v1", "kind": "Folder", "spec": { "children": [] } } | When success is false, the system returns a null value. When success is true, the system returns the authorization information. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

**Examples**

Sample requests

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders HTTP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"
{\"eagleEyeTraceId\":\"0a2318ab17773416555583153d****\",\"asapiSuccess\":true,\"asapiRequ tId\":\"A11B1055-5AB7-4AB4-AEB0-32947AEB****\",\"data\":{\"metadata\": {\"createdAt\":\"2026-04- 28T02:00:55.598****\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04-28T02:0 0:55.598****\",\"namespace\":\"flinkteam\",\"name\":\"changsha\",\"annotations\":{\"cre ator\":\"23540697665705****\",\"modifier\":\"23540697665705****\",\"creatorName\":\"flink min\",\"modifierName\":\"flinkadmin\"},\"id\":\"6b252d46-8653-4d69-9183- 1a16b5a8****\",\"type\":\"development\",\"parentId\":\"cd1562be-02ed-32cf-945b-9769afe4
****\"},\"apiVersion\":\"v1\",\"kind\":\"Folder\",\"spec\":{\"children\":[]}}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
```

`}` `XML` format

```xml
<data> {&quot;eagleEyeTraceId&quot;:&quot;0a2318ab17773416555583153d****&quot;,&quot;asapiSucces quot;:true,&quot;asapiRequestId&quot;:&quot;A11B1055-5AB7-4AB4-AEB0- 32947AEB****&quot;,&quot;data&quot;:{&quot;metadata&quot;: {&quot;createdAt&quot;:&quot;2026-04- 28T02:00:55.598****&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modified &quot;:&quot;2026-04- 28T02:00:55.598****&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;name&quot;:&q t;changsha&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;23540697665705****&quot;,&quot;modifier&quot;:&quot;2354069766 05****&quot;,&quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;modifierName&quot;:&quo flinkadmin&quot;},&quot;id&quot;:&quot;6b252d46-8653-4d69-9183- 1a16b5a8****&quot;,&quot;type&quot;:&quot;development&quot;,&quot;parentId&quot;:&quot;cd 62be-02ed-32cf-945b- 9769afe4****&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Folder&q t;,&quot;spec&quot;:{&quot;children&quot;:[]}}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

##### 3.1.2.61 ListJobs

Obtains a list of job instances.

**Request headers**

The ListJobs operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Syntax**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/jobs HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| deploymen tId | Strin g | Quer y | Yes | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | The job ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| workspace | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | {"success": true,"message": "","plan": ""} | The detailed information. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/jobs HTTP/1.1 &RegionId=cn-wulan-env***-d01 &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7def580c00 &namespace=flinkteam &workspace=default &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"{\"success\": true,\"message\": \"\",\"plan\": \"\"}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
```

`}` `XML` format

```xml
<data>{&quot;success&quot;: true,&quot;message&quot;: &quot;&quot;,&quot;plan&quot;: &q uot;&quot;}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

##### 3.1.2.62 ReplaceDeployment

Call ReplaceDeployment to replace an existing deployment in Realtime Compute.

**Request headers**

This API uses common request headers and does not require special request headers. For more information, see the Common Request Parameter documentation.

**Syntax**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HT TP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wulan-env***-d01 | The region ID. |
| namespac e | Strin g | Path | Yes | flinkteam | The name of the project where the job resides. |
| deployme ntId | Strin g | Path | Yes | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | The ID of the job. |

| k (Compute- dition) Devel ager API | Storage S oper Gui | eparation de·AppMa |   |   | Realtime Comput |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| paramsJso n | Strin g | Body | No | {"name":"jarjob","engin eVersion":"vvr-11.5.0- flink- 1.20","executionMode":" STREAMING","imageUse rDefined":false,"deploy mentTarget": {"mode":"PER JOB","na _ me":"dt- flinkteam"},"artifact": {"kind":"JAR","jarArtifact ":{"jarUri":"oss://flink- fullymanaged- apmd99ri0du673/artifac ts/namespaces/flinktea m/TopSpeedWindowing.j ar"}},"kerberosConfig": {"kerberosEnabled":fals e},"namespace":"flinkte am"} | The execution parameters and SQL script. |
| workspac e | Strin g | Path | Yes | default | The ID of the workspace where the job resides. You can obtain the workspace ID by using one of the following methods: Call ListNamespaces to obtain the workspace ID. View the workspace details in the Realtime Compute for Apache Flink console. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request succeeded. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
|   |   | { "deploymentId" : "7f4143a2-2eee- 4c5c-8803- a50d388514ac", "name" : "jarjob", "executionMode" : "STREAMING", "streamingResourc eSetting" : { "resourceSettingM ode" : "BASIC", |   |

|   |   |   | Edition) Developer Guide·AppM nager AP |
|---|---|---|---|
| Parameter | Type | "basicResourceSett Example ing" : { | Description |
| data | Integer | "parallelism" : 1, "jobmanagerResou rceSettingSpec" : { "cpu" : 1.0, "memory" : "4Gi" }, "taskmanagerReso urceSettingSpec" : { "cpu" : 1.0, "memory" : "4Gi" } } }, "kerberosConfig" : { "kerberosEnabled" : false }, "labels" : { }, "engineVersion" : "vvr-11.5.0-flink- 1.20", "referencedDeploy mentDraftId" : "", "deploymentHasCh anged" : true, "taker" : " \| vvp-0", "priority" : 5, "resourceTuning" : { "mode" : "none", "resourceTuningId" : "", "resourceTuningNa me" : "", "scheduledPlanIsCa ncelling" : false }, "autopilot" : { "mode" : "", "recommendation" : "", "ignoreRecommen dation" : "" }, "deploymentTarget " : { "mode" : "PER JOB", "name" _ : "dt-flinkteam" }, "artifact" : { "kind" : "JAR", "jarArtifact" : { "jarUri" : "oss://flink- fullymanaged- apmd99ri0du673/a rtifacts/namespace s/flinkteam/TopSpe edWindowing.jar" } }, "flinkConf" : { "execution.checkp ointing.interval" : "180s", "restart- strategy.fixed- delay.attempts" : "2147483647", "table.exec.state.ttl " : "36 h", "restart- strategy" : "fixed- delay", "execution.checkp | The detailed information. |

| Parameter | Type | ointing.min-pause" Example : "180s", "restart- | Description |
|---|---|---|---|
|   |   | strategy.fixed- delay.delay" : "10 s" }, "logging" : { "loggingProfile" : "default", "log4jLoggers" : [ { "loggerName" : "", "loggerLevel" : "INFO" } ], "logReservePolicy" : { "openHistory" : true, "expirationDays" : 7 } }, "jobSummary" : { "starting" : 0, "running" : 0, "cancelling" : 0, "cancelled" : 0, "finished" : 0, "failed" : 0 }, "workspace" : "apmd99ri0du673" , "namespace" : "flinkteam", "creator" : "20678996188752 3346", "creatorName" : "flinkadmin", "modifier" : "20678996188752 3346", "modifierName" : "flinkadmin", "createdAt" : 1777526754, "modifiedAt" : |   |

1777526754 }

**Examples**

Request example

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HT TP/1.1
```

`{`

```json
"RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7def580c00", "workspace":"default"
```

`}` Successful response example `JSON` format `{`

```json
 "data":"{\"deploymentId\":\"7f4143a2-2eee-4c5c-8803-
a50d388514ac\",\"name\":\"jarjob\",\"executionMode\":\"STREAMING\",\"streamingResourceSet ng\":{\"resourceSettingMode\":\"BASIC\",\"basicResourceSetting\": {\"parallelism\":1,\"jobmanagerResourceSettingSpec\": {\"cpu\":1.0,\"memory\":\"4Gi\"},\"taskmanagerResourceSettingSpec\": {\"cpu\":1.0,\"memory\":\"4Gi\"}}},\"kerberosConfig\": {\"kerberosEnabled\":false},\"labels\":{},\"engineVersion\":\"vvr-11.5.0-flink-1.20\",\ "referencedDeploymentDraftId\":\"\",\"deploymentHasChanged\":true,\"taker\":\" | vvp-0\ ",\"priority\":5,\"resourceTuning\": {\"mode\":\"none\",\"resourceTuningId\":\"\",\"resourceTuningName\":\"\",\"scheduledPlanI ancelling\":false},\"autopilot\": {\"mode\":\"\",\"recommendation\":\"\",\"ignoreRecommendation\":\"\"},\"deploymentTarget\ {\"mode\":\"PER_JOB\",\"name\":\"dt-flinkteam\"},\"artifact\": {\"kind\":\"JAR\",\"jarArtifact\":{\"jarUri\":\"oss://flink-fullymanagedapmd99ri0du673/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar\"}},\"flinkConf\":{ \"execution.checkpointing.interval\":\"180s\",\"restart-strategy.fixeddelay.attempts\":\"2147483647\",\"table.exec.state.ttl\":\"36 h\",\"restart-strategy\": \"fixed-delay\",\"execution.checkpointing.min-pause\":\"180s\",\"restartstrategy.fixed-delay.delay\":\"10 s\"},\"logging\": {\"loggingProfile\":\"default\",\"log4jLoggers\": [{\"loggerName\":\"\",\"loggerLevel\":\"INFO\"}],\"logReservePolicy\": {\"openHistory\":true,\"expirationDays\":7}},\"jobSummary\": {\"starting\":0,\"running\":0,\"cancelling\":0,\"cancelled\":0,\"finished\":0,\"failed\": ,\"workspace\":\"apmd99ri0du673\",\"namespace\":\"flinkteam\",\"creator\":\"2067899618875 346\",\"creatorName\":\"flinkadmin\",\"modifier\":\"206789961887523346\",\"modifierName\" "flinkadmin\",\"createdAt\":1777526754,\"modifiedAt\":1777526754}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
```

`}` `XML` format

```xml
<data>{&quot;deploymentId&quot;:&quot;7f4143a2-2eee-4c5c-8803a50d388514ac&quot;,&quot;name&quot;:&quot;jarjob&quot;,&quot;executionMode&quot;:&quot;ST AMING&quot;,&quot;streamingResourceSetting&quot;: {&quot;resourceSettingMode&quot;:&quot;BASIC&quot;,&quot;basicResourceSetting&quot;:{&q uot;parallelism&quot;:1,&quot;jobmanagerResourceSettingSpec&quot;: {&quot;cpu&quot;:1.0,&quot;memory&quot;:&quot;4Gi&quot;},&quot;taskmanagerResourceSetting ec&quot;: {&quot;cpu&quot;:1.0,&quot;memory&quot;:&quot;4Gi&quot;}}},&quot;kerberosConfig&quot;:{ &quot;kerberosEnabled&quot;:false},&quot;labels&quot;: {},&quot;engineVersion&quot;:&quot;vvr-11.5.0-flink- 1.20&quot;,&quot;referencedDeploymentDraftId&quot;:&quot;&quot;,&quot;deploymentHasChange quot;:true,&quot;taker&quot;:&quot; | vvp- 0&quot;,&quot;priority&quot;:5,&quot;resourceTuning&quot;: {&quot;mode&quot;:&quot;none&quot;,&quot;resourceTuningId&quot;:&quot;&quot;,&quot;resour TuningName&quot;:&quot;&quot;,&quot;scheduledPlanIsCancelling&quot;:false},&quot;autopilo quot;: {&quot;mode&quot;:&quot;&quot;,&quot;recommendation&quot;:&quot;&quot;,&quot;ignoreRecomm dation&quot;:&quot;&quot;},&quot;deploymentTarget&quot;: {&quot;mode&quot;:&quot;PER_JOB&quot;,&quot;name&quot;:&quot;dtflinkteam&quot;},&quot;artifact&quot;: {&quot;kind&quot;:&quot;JAR&quot;,&quot;jarArtifact&quot;: {&quot;jarUri&quot;:&quot;oss://flink-fullymanagedapmd99ri0du673/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar&quot;}},&quot;flinkCo &quot;:{&quot;execution.checkpointing.interval&quot;:&quot;180s&quot;,&quot;restart-str ategy.fixeddelay.attempts&quot;:&quot;2147483647&quot;,&quot;table.exec.state.ttl&quot;:&quot;36 h &quot;,&quot;restart-strategy&quot;:&quot;fixeddelay&quot;,&quot;execution.checkpointing.minpause&quot;:&quot;180s&quot;,&quot;restart-strategy.fixed-delay.delay&quot;:&quot;10 s& quot;},&quot;logging&quot;: {&quot;loggingProfile&quot;:&quot;default&quot;,&quot;log4jLoggers&quot;: [{&quot;loggerName&quot;:&quot;&quot;,&quot;loggerLevel&quot;:&quot;INFO&quot;}],&quot;lo eservePolicy&quot;: {&quot;openHistory&quot;:true,&quot;expirationDays&quot;:7}},&quot;jobSummary&quot;:{&q uot;starting&quot;:0,&quot;running&quot;:0,&quot;cancelling&quot;:0,&quot;cancelled&quot; ,&quot;finished&quot;:0,&quot;failed&quot;:0},&quot;workspace&quot;:&quot;apmd99ri0du673& ot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;creator&quot;:&quot;206789961887523 6&quot;,&quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;modifier&quot;:&quot;2067899 887523346&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;createdAt&quot;:177 26754,&quot;modifiedAt&quot;:1777526754}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

#### 3.1.3 Compute-storage separation v2

##### 3.1.3.1 ValidateSqlStatement

Validates the SQL statements in the Realtime Compute for Apache Flink engine.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Syntax**

```
POST /api/v2/namespaces/[namespace]/sql-statement/validate HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |

| Parameter | Type | Position |   | Required |   | Example |   | Description |
|---|---|---|---|---|---|---|---|---|
| body | String | wholebody |   | Yes |   | {'statemen |   |   |
|   |   |   |   |   |   |   | {'statemen | The SQL |
|   |   |   |   |   | Yes | t': 'SELECT |   |   |
|   |   |   |   |   |   |   |   | st |
|   |   |   |   |   |   | 1'} |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| reason | String | "" | The error cause. A null value is returned if the service runs normally. |
| eagleEyeTrace Id | String | 0a1129361783048 3500182**** | The EagleEye trace ID. |
| asapiSuccess | Boolean | true | Indicates that the operation call is successful with expected results and no errors. |

| asapiRequestI d | String | CF3A87DE-268D- 4E4B-865F- CCC91**** | The ASAPI request ID. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| data | String | { "validationResult": "VALIDATION RESU _ LT VALID SELECT _ _ _ QUERY", "success": true, "message": "SQL validate success", "errorDetails": { "columnNumber": 0, "endLineNumber": 0, "invalidFlinkConf": [], "endColumnNumbe r": 0, "lineNumber": 0, "message": "" } } | If the value of success is false, a null value is returned. If the value of success is true, the detailed information is returned. |
| errorCode | String | "" | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |
| errorMessage | String | "" | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |
| httpCode | Integer | 200 | The HTTP status code. |
| message | String | "" | The additional information. |

**Examples**

Sample requests

```
POST /api/v2/namespaces/[namespace]/sql-statement/validate HTTP/1.1
```

`{`

```json
"namespace":"default-namespace", "body":"{'statement': 'SELECT 1'}"
```

`}` Sample success responses `JSON` format `{`

```json
 "reason":"",
 "eagleEyeTraceId":"0a11293617830483500182****",
 "asapiSuccess":true,
 "asapiRequestId":"CF3A87DE-268D-4E4B-865F-CCC91****",
 "data":"{    \"validationResult\": \"VALIDATION_RESULT_VALID_SELECT_QUERY\",
\"success\": true, \"message\": \"SQL validate success\", \"errorDetails\": { \"columnNumber\": 0, \"endLineNumber\": 0, \"invalidFlinkConf\": [], \"en dColumnNumber\": 0, \"lineNumber\": 0, \"message\": \"\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200,
 "message":""
```

`}` `XML` format

```xml
<reason /> <eagleEyeTraceId>0a11293617830483500182****</eagleEyeTraceId> <asapiSuccess>true</asapiSuccess> <asapiRequestId>CF3A87DE-268D-4E4B-865F-CCC91****</asapiRequestId> <data>{
    &quot;validationResult&quot;: &quot;VALIDATION_RESULT_VALID_SELECT_QUERY&quot;,
    &quot;success&quot;: true,
    &quot;message&quot;: &quot;SQL validate success&quot;,
    &quot;errorDetails&quot;: {
      &quot;columnNumber&quot;: 0,
      &quot;endLineNumber&quot;: 0,
      &quot;invalidFlinkConf&quot;: [],
      &quot;endColumnNumber&quot;: 0,
      &quot;lineNumber&quot;: 0,
      &quot;message&quot;: &quot;&quot;
```

`}`

```xml
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
 <message  />
```

##### 3.1.3.2 UpdateMember

Updates the member information in a namespace.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Syntax**

```
PUT /gateway/v2/namespaces/[namespace]/members HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |

| Parameter | Type |   | Position |   | Required |   | Example |   | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|
| body | string |   | wholebody |   |   |   | {'member': |   |   |   |
|   |   |   |   |   |   |   |   | {'member': |   |   |
|   |   |   |   |   |   |   | '23136675424 |   | The detailed |   |
|   |   |   |   |   |   |   |   |   | information |   |
|   |   |   |   | ody | No |   |   |   |   |   |
|   |   |   |   |   |   |   | 6****', |   | about the |   |
|   |   |   |   |   |   |   | 'role': |   | mem |   |
|   |   |   |   |   |   |   | 'VIEWER'} |   |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
|---|---|---|---|
| data | String | { "member": "2313667542****", "role": "viewer" } | If the value of success is false, a null value is returned. If the value of success is true, the detailed information is returned. |
| errorCode | String | "" | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |
| errorMessage | String | "" | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
PUT /gateway/v2/namespaces/[namespace]/members HTTP/1.1
```

`{`

```json
"namespace":"default-namespace"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{    \"member\": \"2313667542****\",    \"role\": \"viewer\"  }",
"success":true, "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****", "errorMessage":"", "errorCode":"", "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;member&quot;: &quot;2313667542****&quot;,
    &quot;role&quot;: &quot;viewer&quot;
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.3 UpdateDeployment

Update the deployment configuration or application version for smooth service upgrades and change management.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Syntax**

```
PUT /api/v2/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the project. |
| deployme ntId | Strin g | Path | Yes | d0b3abf0-4bfe-46b1- a324-5b7d**** | The ID of the job. |

|   | Parameter |   |   | Type |   | Position |   | Required |   |   | Example |   | Descriptio n |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   | {"artifact |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | {"artifact |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ": |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | {"kind":"SQL |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | SCRIPT","sql |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Artifact": |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | {"sqlScript" |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | :"CREATE |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | TEMPORARY |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | TABLE |   |   |   |

| (st |   |
|---|---|

|   |   | Parameter |   | Type |   |   | Position |   |   |   |   | Required |   |   |   |   |   | rname |   |   |   | Descriptio n |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | uired |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Exampl VARCHAR) |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | with ( |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ' = |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 'datagen' |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ); |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | TEMPORARY |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | TABLE |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | e |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | _ (strname |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | VARCHAR, |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | lens |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | BIGINT) |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | with ( |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ' = |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 'print' |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ); |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | kafka table _ |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | SUBSTRING |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | (strname, |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 0, 10) AS |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | strname, |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | CAST |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | (CHAR LENGTH _ |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | (strname) |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | AS BIGINT) |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | AS lens |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | FROM |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ble; |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | r":"20877848 |   |   |   |   |   |

|   | Parameter |   | Type |   |   |   |   | 2972****","c |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   | Position |   |   |   | Descriptio |
|   |   |   |   |   |   |   | Required | Example reatorName": | n |
|   |   |   |   |   |   |   |   | "flinkadmin" |   |
|   |   |   |   |   |   |   |   | ,"deployment |   |
|   |   |   |   |   |   |   |   | HasChanged": |   |
|   |   |   |   |   |   |   |   | true,"deploy |   |
|   |   |   |   |   |   |   |   | mentId":"1e3 |   |
|   |   |   |   |   |   |   |   | 2fa1e-fd0e- |   |
|   |   |   |   |   |   |   |   | 48e6-81d2- |   |
|   |   |   |   |   |   |   |   | fa66443****" |   |
|   |   |   |   |   |   |   |   | ,"deployment |   |
|   |   |   |   |   |   |   |   | Target": |   |
|   |   |   |   |   |   |   |   | {"mode":"PER |   |
|   |   |   |   |   |   |   |   | JOB","name" _ |   |
|   |   |   |   |   |   |   |   | :"dt- |   |
|   |   |   |   |   |   |   |   | flinkteam"}, |   |
|   |   |   |   |   |   |   |   | "engineVersi |   |
|   |   |   |   |   |   |   |   | on":"vvr- |   |
|   |   |   |   |   |   |   |   | 8.0.7- |   |
|   |   |   |   |   |   |   |   | flink- |   |
|   |   |   |   |   |   |   |   | 1.17","execu |   |
|   |   |   |   |   |   |   |   | tionMode":"S |   |
|   |   |   |   |   |   |   |   | TREAMING","f |   |
|   |   |   |   |   |   |   |   | linkConf": |   |
|   |   |   |   |   |   |   |   | {"execution. |   |
|   |   |   |   |   |   |   |   | checkpointin |   |
|   |   |   |   |   |   |   |   | g.interval": |   |
|   |   |   |   |   |   |   |   | "180s","exec |   |
|   |   |   |   |   |   |   |   | ution.checkp |   |
|   |   |   |   |   |   |   |   | ointing.min- |   |
|   |   |   |   |   |   |   |   | pause":"180s |   |
|   |   |   |   |   |   |   |   |   | The job |
|   |   |   |   |   |   |   |   | ","restart- |   |
|   | body |   | string |   | wholebody |   | Yes |   | content to |
|   |   |   |   |   |   |   |   | strategy":"f | update. |
|   |   |   |   |   |   |   |   | ixed- |   |
|   |   |   |   |   |   |   |   | delay","rest |   |
|   |   |   |   |   |   |   |   | art- |   |
|   |   |   |   |   |   |   |   | strategy.fix |   |
|   |   |   |   |   |   |   |   | ed- |   |
|   |   |   |   |   |   |   |   | delay.attemp |   |
|   |   |   |   |   |   |   |   | ts":"214748* |   |
|   |   |   |   |   |   |   |   | ***","restar |   |
|   |   |   |   |   |   |   |   | t- |   |
|   |   |   |   |   |   |   |   | strategy.fix |   |
|   |   |   |   |   |   |   |   | ed- |   |
|   |   |   |   |   |   |   |   | delay.delay" |   |
|   |   |   |   |   |   |   |   | :"10 |   |
|   |   |   |   |   |   |   |   | s","table.ex |   |
|   |   |   |   |   |   |   |   | ec.state.ttl |   |
|   |   |   |   |   |   |   |   | ":"36 |   |
|   |   |   |   |   |   |   |   | h"},"jobSumm |   |
|   |   |   |   |   |   |   |   | ary": |   |
|   |   |   |   |   |   |   |   | {"cancelled" |   |
|   |   |   |   |   |   |   |   | :0,"cancelli |   |

|   |   |   |   | ng":0,"faile |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | Descriptio |   |
| Parameter | Type | Position | Required | Example d":0,"finish |   | n |   |
|   |   |   |   | ed":0,"runni |   |   |   |
|   |   |   |   | ng":0,"start |   |   |   |
|   |   |   |   | ing":0},"log |   |   |   |
|   |   |   |   | ging": |   |   |   |
|   |   |   |   | {"log4jLogge |   |   |   |
|   |   |   |   | rs": |   |   |   |
|   |   |   |   | [{"loggerLev |   |   |   |
|   |   |   |   | el":"INFO"," |   |   |   |
|   |   |   |   | loggerName": |   |   |   |
|   |   |   |   | ""}],"logRes |   |   |   |
|   |   |   |   | ervePolicy": |   |   |   |
|   |   |   |   | {"expiration |   |   |   |
|   |   |   |   | Days":7,"ope |   |   |   |
|   |   |   |   | nHistory":tr |   |   |   |
|   |   |   |   | ue},"logging |   |   |   |
|   |   |   |   | Profile":"de |   |   |   |
|   |   |   |   | fault"},"mod |   |   |   |
|   |   |   |   | ifier":"2087 |   |   |   |
|   |   |   |   | 7848297216** |   |   |   |
|   |   |   |   | **","modifie |   |   |   |
|   |   |   |   | rName":"flin |   |   |   |
|   |   |   |   | kadmin","nam |   |   |   |
|   |   |   |   | e":"sqlJob", |   |   |   |
|   |   |   |   | "namespace": |   |   |   |
|   |   |   |   | "flinkteam", |   |   |   |
|   |   |   |   | "streamingRe |   |   |   |
|   |   |   |   | sourceSettin |   |   |   |
|   |   |   |   | g": |   |   |   |
|   |   |   |   | {"basicResou |   |   |   |
|   |   |   |   | rceSetting": |   |   |   |
|   |   |   |   | {"jobmanager |   |   |   |
|   |   |   |   | ResourceSett |   |   |   |
|   |   |   |   | ingSpec": |   |   |   |
|   |   |   |   | {"cpu":1.0," |   |   |   |
|   |   |   |   | memory":"4Gi |   |   |   |
|   |   |   |   | "},"parallel |   |   |   |
|   |   |   |   | ism":1,"task |   |   |   |
|   |   |   |   | managerResou |   |   |   |
|   |   |   |   | rceSettingSp |   |   |   |
|   |   |   |   | ec": |   |   |   |
|   |   |   |   | {"cpu":1.0," |   |   |   |
|   |   |   |   | memory":"4Gi |   |   |   |
|   |   |   |   | "}},"resourc |   |   |   |
|   |   |   |   | eSettingMode |   |   |   |
|   |   |   |   | ":"BASIC"}} |   |   |   |

| Parameter | Type | Position | Required |   |   | xample | Descriptio n |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   | E |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The Request ID. |
|   |   | { "artifact": { "kind": "SQLSCRIPT", "sqlArtifact": { "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO |   |

| Parameter | Type | kafka table Exam_ple SELECT | Description |
|---|---|---|---|
|   |   | SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ " } }, "creator": |   |
| data | String | "208778482972*** *", "creatorName": "flinkadmin", "deploymentHasCh anged": true, "deploymentId": "f9d616ef-4422- 42b5-b95c- f691d44****", "deploymentTarget ": { "mode": "PER JOB", _ "name": "dt- flinkteam" }, "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "flinkConf": { "execution.checkp ointing.interval": "180s", "table.exec.state.ttl ": "36 h", "restart- strategy.fixed- delay.delay": "10 s", "restart- strategy": "fixed- delay", "restart- strategy.fixed- delay.attempts": "21474****", "execution.checkp ointing.min-pause": "180s" }, "jobSummary": { "cancelled": 0, "cancelling": 0, "failed": 0, "finished": 0, "running": 0, "starting": 0 }, "logging": { "log4jLoggers": [ { "loggerLevel": "INFO", "loggerName": "" } ], "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, | If success is false, the system returns a null value. If success is true, the system returns detailed data. |

| Parameter | Type | "modifier": Example "20877848297**** | Description |
|---|---|---|---|
|   |   | ", "modifierName": "flinkadmin", "name": "sqlJob", "namespace": "flinkteam", "streamingResourc eSetting": { "basicResourceSett ing": { "jobmanagerResou rceSettingSpec": { "cpu": 1.0, "memory": "4Gi" }, "parallelism": 1, "taskmanagerReso urceSettingSpec": { "cpu": 1.0, "memory": "4Gi" } }, "resourceSettingM ode": "BASIC" } } |   |
| errorCode | String | "" | If success is false, this value is not empty and indicates the business Error Code. If success is true, this value is empty. |
| errorMessage | String | "" | If success is false, the system returns the business error message. If success is true, the system returns a null value. |
| httpCode | Integer | 200 | The HTTP Status Code. |

**Examples**

Request example

```
PUT /api/v2/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1
```

`{`

```json
"namespace":"default-namespace", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7d****", "body":"{"artifact":{"kind":"SQLSCRIPT","sqlArtifact":{"sqlScript":"CREATE TEMPORARY TA BLE `datahub_table` (strname VARCHAR)with ( 'connector' = 'datagen' );CREATE TEMPOR ARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( 'connector' = 'pri nt' );INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CH AR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;"}},"creator":"208778482972****","creatorName":"flinkadmin","deploymentHasC nged":true,"deploymentId":"1e32fa1e-fd0e-48e6-81d2-fa66443****","deploymentTarget":{"mo de":"PER_JOB","name":"dt-flinkteam"},"engineVersion":"vvr-8.0.7-flink- 1.17","executionMode":"STREAMING","flinkConf": {"execution.checkpointing.interval":"180s","execution.checkpointing.minpause":"180s","restart-strategy":"fixed-delay","restart-strategy.fixeddelay.attempts":"214748****","restart-strategy.fixed-delay.delay":"10 s","table.exec.state.ttl":"36 h"},"jobSummary": {"cancelled":0,"cancelling":0,"failed":0,"finished":0,"running":0,"starting":0},"logging" {"log4jLoggers":[{"loggerLevel":"INFO","loggerName":""}],"logReservePolicy": {"expirationDays":7,"openHistory":true},"loggingProfile":"default"},"modifier":"208778482 216****","modifierName":"flinkadmin","name":"sqlJob","namespace":"flinkteam","streamingRe urceSetting":{"basicResourceSetting":{"jobmanagerResourceSettingSpec": {"cpu":1.0,"memory":"4Gi"},"parallelism":1,"taskmanagerResourceSettingSpec":{"cpu":1.0, "memory":"4Gi"}},"resourceSettingMode":"BASIC"}}"
```

`}` Successful response example `JSON` format `{`

```json
 "data":"{    \"artifact\": {      \"kind\": \"SQLSCRIPT\",      \"sqlArtifact\": {
\"sqlScript\": \"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'c onnector' = 'datagen'\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\ );\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ data hub_table;\\" } }, \"creator\": \"208778482972****\", \"creatorName\": \"flinkadmin\", \"deploymentHasChanged\": true, \"deploymentId\": \"f9d616ef-4422 -42b5-b95c-f691d44****\", \"deploymentTarget\": { \"mode\": \"PER_JOB\", \" name\": \"dt-flinkteam\" }, \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMode\": \"STREAMING\", \"flinkConf\": { \"execution.checkpointing.interval\": \"180s\", \"table.exec.state.ttl\": \"36 h\" , \"restart-strategy.fixed-delay.delay\": \"10 s\", \"restart-strategy\": \"fi xed-delay\", \"restart-strategy.fixed-delay.attempts\": \"21474****\", \"execution.checkpointing.min-pause\": \"180s\" }, \"jobSummary\": { \"cancelled\": 0, \"cancelling\": 0, \"failed\": 0, \"finished\": 0, \"running\": 0, \"starting\": 0 }, \"logging\": { \"log4jLoggers\": [ { \"loggerLevel\": \"INFO\", \"loggerName\": \"\" } ], \"logReservePolicy\": { \"expirationDays\": 7, \"openHistory\": true }, \"loggingProfile\": \"default\" }, \"modifier\": \"20877848297****\", \ "modifierName\": \"flinkadmin\", \"name\": \"sqlJob\", \"namespace\": \"flinkteam\", \"streamingResourceSetting\": { \"basicResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \"taskmanagerResourceSettingSpec\": { \"cp u\": 1.0, \"memory\": \"4Gi\" } }, \"resourceSettingMode\": \" BASIC\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;artifact&quot;: {
      &quot;kind&quot;: &quot;SQLSCRIPT&quot;,
      &quot;sqlArtifact&quot;: {
        &quot;sqlScript&quot;: &quot;CREATE TEMPORARY TABLE `datahub_table` (strname VA
RCHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27; );CREATE TEMPORARY TABLE ` kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;prin t&#x27; );INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (C HAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;
```

`}` `},`

```
    &quot;creator&quot;: &quot;208778482972****&quot;,
    &quot;creatorName&quot;: &quot;flinkadmin&quot;,
    &quot;deploymentHasChanged&quot;: true,
    &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f691d44****&quot;,
    &quot;deploymentTarget&quot;: {
      &quot;mode&quot;: &quot;PER_JOB&quot;,
      &quot;name&quot;: &quot;dt-flinkteam&quot;
```

`}` `},`

```
    &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
    &quot;executionMode&quot;: &quot;STREAMING&quot;,
    &quot;flinkConf&quot;: {
      &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
      &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
      &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;,
      &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
      &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;21474****&quot;,
      &quot;execution.checkpointing.min-pause&quot;: &quot;180s&quot;
```

`},`

```
    &quot;jobSummary&quot;: {
      &quot;cancelled&quot;: 0,
      &quot;cancelling&quot;: 0,
      &quot;failed&quot;: 0,
      &quot;finished&quot;: 0,
      &quot;running&quot;: 0,
      &quot;starting&quot;: 0
```

`},`

```
    &quot;logging&quot;: {
      &quot;log4jLoggers&quot;: [
```

`{`

```
          &quot;loggerLevel&quot;: &quot;INFO&quot;,
          &quot;loggerName&quot;: &quot;&quot;
```

`}` `],`

```
      &quot;logReservePolicy&quot;: {
        &quot;expirationDays&quot;: 7,
        &quot;openHistory&quot;: true
```

`},`

```
      &quot;loggingProfile&quot;: &quot;default&quot;
```

`},`

```
    &quot;modifier&quot;: &quot;20877848297****&quot;,
    &quot;modifierName&quot;: &quot;flinkadmin&quot;,
    &quot;name&quot;: &quot;sqlJob&quot;,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;streamingResourceSetting&quot;: {
      &quot;basicResourceSetting&quot;: {
        &quot;jobmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
```

`},`

```
        &quot;parallelism&quot;: 1,
        &quot;taskmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
```

`}` `},`

```
      &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
```

`}`

```xml
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
<errorCode
```

`/>`

```xml
 <errorCode  />
 <httpCode>200</httpCode>
```

```html ```

##### 3.1.3.4 StopJob

Stops a job instance.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Request syntax**

```
POST /api/v2/namespaces/[namespace]/jobs/[jobId]:stop HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the project. |
| jobId | Strin g | Path | Yes | 5af678c0-7db0-4650- 94c2-d2604f0a**** | The ID of the job instance. |

| Parameter | Type | Position |   | Required |   | Example |   | Descriptio n |
|---|---|---|---|---|---|---|---|---|
| body | String | wholebody |   | Yes |   | {'stopStra |   | The parameters for stopping a job instance. |
|   |   |   |   |   |   |   | {'stopStra | The parameters |
|   |   |   |   |   |   | tegy': |   |   |
|   |   |   |   |   |   |   |   | f |
|   |   |   |   |   |   | 'NONE'} |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
|   |   | { "artifact": { "kind": "SQLSCRIPT", |   |

| Realtime Compute |   |   | Edition) Developer Guide·AppM nager AP |
|---|---|---|---|
| Parameter | Type | "sqlArtifact": { Example "sqlScript": | Description |
| data | String | "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ " } }, "creator": "208778482972*** *", "creatorName": "flinkadmin", "deploymentId": "5ef6cbcf-9df1- 4d54-ab32- 0a2c81****", "deploymentName ": "sqlJob", "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "flinkConf": { "table.exec.operat or-name.max- length": "10240", "env.java.opts.job manager": "- Xloggc:/opt/flink/lo g/jobmanager- gc.log - XX:+UseGCLogFile Rotation - XX:NumberOfGCLo gFiles=2 - XX:GCLogFileSize= 50M", "***":"***" }, "jobId": "65eb3696-db7d- 4a58-9851- cda26f252924", | If success is false, the system returns a null value. If success is true, the system returns detailed data. |
| > Document Versi | on: 20260828 |   | 26 |

| Parameter | Type | "logging": { Example "log4j2Configuratio | Description |
|---|---|---|---|
|   |   | nTemplate": " |   |
| errorCode | String | "" | If success is false, this value is not empty and indicates the business error code. If success is true, this value is empty. |
| errorMessage | String | "" | If success is false, the system returns the business error message. If success is true, the system returns a null value. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
POST /api/v2/namespaces/[namespace]/jobs/[jobId]:stop HTTP/1.1
```

`{`

```json
"namespace":"default-namespace", "jobId":"5af678c0-7db0-4650-94c2-d2604f0a****", "body":"{'stopStrategy': 'NONE'}"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{    \"artifact\": {      \"kind\": \"SQLSCRIPT\",      \"sqlArtifact\": {
\"sqlScript\": \"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'c onnector' = 'datagen'\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\ );\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ data hub_table;\\" } }, \"creator\": \"208778482972****\", \"creatorName\": \"flinkadmin\", \"deploymentId\": \"5ef6cbcf-9df1-4d54-ab32-0a2c81****\", \"deploymentName\": \"sqlJob\", \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMode\": \"STREAMING\", \"flinkConf\": { \"table.exec.operatorname.max-length\": \"10240\", \"env.java.opts.jobmanager\": \"- Xloggc:/opt/flink/log/jobmanager-gc.log -XX:+UseGCLogFileRotation - XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M\", \"***\":\"***\" }, \"jobId \": \"65eb3696-db7d-4a58-9851-cda26f252924\", \"logging\": { \"log4j2ConfigurationTemplate\": \"<?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" *** *\\", \"log4jLoggers\": [ { \"loggerLevel\": \"INFO\", \"l oggerName\": \"\" } ], \"logReservePolicy\": { \"expirationDays\": 7, \"openHistory\": true } }, \"metric\": { \ "totalCpu\": 2.0, \"totalMemoryByte\": 85899**** }, \"modifier\": \"2087784829721****\", \"modifierName\": \"flinkadmin\", \"namespace\": \"flinkteam\", \"restoreStrategy\": { \"kind\": \"NONE\" }, \"startTime\": 178305****, \"status\": { \"currentJobStatus\": \"RUNNING\", \"running\": { \"observedFlinkJobRestarts\": 0, \"observedFlinkJobStatus\": \"RUNNING\" } }, \"streamingResourceSetting\": { \"basicResourceSetting\": { \"job managerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \"taskmanagerResourceSettingSpec\": { \"cp u\": 1.0, \"memory\": \"4Gi\" } }, \"resourceSettingMode\": \" BASIC\" }, \"userFlinkConf\": { \"execution.checkpointing.interval\": \"180s\", \"table.exec.state.ttl\": \"36 h\", \"restart-strategy.fixeddelay.delay\": \"10 s\", \"restart-strategy\": \"fixed-delay\", \"restartstrategy.fixed-delay.attempts\": \"214748****\", \"execution.checkpointing.min-pau se\": \"180s\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;artifact&quot;: {
      &quot;kind&quot;: &quot;SQLSCRIPT&quot;,
      &quot;sqlArtifact&quot;: {
        &quot;sqlScript&quot;: &quot;CREATE TEMPORARY TABLE `datahub_table` (strname VA
RCHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27; );CREATE TEMPORARY TABLE ` kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;prin t&#x27; );INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (C HAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;
```

`}` `},`

```
    &quot;creator&quot;: &quot;208778482972****&quot;,
```

`&` `t` `t` `N` `&` `t` `&`

```
tflikdi&
```

`t`

```
    &quot;creatorName&quot;: &quot;flinkadmin&quot;,
    &quot;deploymentId&quot;: &quot;5ef6cbcf-9df1-4d54-ab32-0a2c81****&quot;,
    &quot;deploymentName&quot;: &quot;sqlJob&quot;,
    &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
    &quot;executionMode&quot;: &quot;STREAMING&quot;,
    &quot;flinkConf&quot;: {
      &quot;table.exec.operator-name.max-length&quot;: &quot;10240&quot;,
      &quot;env.java.opts.jobmanager&quot;: &quot;-Xloggc:/opt/flink/log/jobmanager-gc.
log -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M&quot;,
      &quot;***&quot;:&quot;***&quot;
```

`},`

```
    &quot;jobId&quot;: &quot;65eb3696-db7d-4a58-9851-cda26f252924&quot;,
    &quot;logging&quot;: {
      &quot;log4j2ConfigurationTemplate&quot;: &quot;&lt;?xml version=\&quot;1.0\&quot;
encoding=\&quot;UTF-8\&quot; ****&quot;,
      &quot;log4jLoggers&quot;: [
```

`{`

```
          &quot;loggerLevel&quot;: &quot;INFO&quot;,
          &quot;loggerName&quot;: &quot;&quot;
```

`}` `],`

```
      &quot;logReservePolicy&quot;: {
        &quot;expirationDays&quot;: 7,
        &quot;openHistory&quot;: true
```

`}` `},`

```
    &quot;metric&quot;: {
      &quot;totalCpu&quot;: 2.0,
      &quot;totalMemoryByte&quot;: 85899****
```

`},`

```
    &quot;modifier&quot;: &quot;2087784829721****&quot;,
    &quot;modifierName&quot;: &quot;flinkadmin&quot;,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;restoreStrategy&quot;: {
      &quot;kind&quot;: &quot;NONE&quot;
```

`},`

```
    &quot;startTime&quot;: 178305****,
    &quot;status&quot;: {
      &quot;currentJobStatus&quot;: &quot;RUNNING&quot;,
      &quot;running&quot;: {
        &quot;observedFlinkJobRestarts&quot;: 0,
        &quot;observedFlinkJobStatus&quot;: &quot;RUNNING&quot;
```

`}` `},`

```
    &quot;streamingResourceSetting&quot;: {
      &quot;basicResourceSetting&quot;: {
        &quot;jobmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
```

`},`

```
        &quot;parallelism&quot;: 1,
        &quot;taskmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
```

`}` `}` `},`

```
      &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
```

`},`

```
    &quot;userFlinkConf&quot;: {
      &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
      &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
      &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;,
      &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
      &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;214748****&quot;,
      &quot;execution.checkpointing.min-pause&quot;: &quot;180s&quot;
```

`}`

```xml
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.5 StartJobWithParams

Start a job instance.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Syntax**

```
POST /api/v2/namespaces/[namespace]/jobs:start HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the project. |

| Parameter | Type | Position | Required | Example | Descriptio n |
|---|---|---|---|---|---|

|   |   | Parameter |   | Type |   |   | Position |   |   | Required |   | Example |   | Descriptio n |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   | body |   | String |   |   |   |   |   |   |   | {'deployme |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | {'deployme |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | ntId': |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | '0ba1ce1c- |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 6cf1-4763- |   | The startup |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 8d45- |   | parameters of |   |
|   |   |   |   |   | ring |   | wholebody |   |   | No |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 244f9****', |   | the job |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 'restoreStra |   | instance. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | tegy': |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | {'kind': |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 'NONE'}} |   |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
|   |   | { "artifact": { "kind": "SQLSCRIPT", "sqlArtifact": { "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ | If success is false, the system returns a |

| data Parameter | String Type | " } }, "creator": Example "20877848297**** | null value. Description If success is true, the system returns |
|---|---|---|---|
|   |   | ", "creatorName": "flinkadmin", "deploymentId": "b74e0fc1-914b- 4009-b11c- 52e6278****", "deploymentName ": "sqlJob", "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "flinkConf": { "table.exec.operat or-name.max- length": "10240", "env.java.opts.job | detailed data. |
|   |   | manager": "- Xloggc:/opt/flink/lo g/jobmanager- gc.log - XX:+UseGCLogFile Rotation - XX:NumberOfGCLo gFiles=2 - XX:GCLogFileSize= 50M", "***":"***" }, "jobId": "003fbc67- 1c8c-4147-9bf4- 19da2****7", "logging": { "log4j2Configuratio nTemplate": " |   |
| errorCode | String | "" | If success is false, this value is not empty and indicates the business error code. If success is true, this value is empty. |
| errorMessage | String | "" | If success is false, the system returns the business error message. If success is true, the system returns a null value. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
POST /api/v2/namespaces/[namespace]/jobs:start HTTP/1.1
```

`{`

```json
"namespace":"default-namespace"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{    \"artifact\": {      \"kind\": \"SQLSCRIPT\",      \"sqlArtifact\": {
\"sqlScript\": \"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'c onnector' = 'datagen'\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\ );\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ data hub_table;\\" } }, \"creator\": \"20877848297****\", \"creatorName\": \"fl inkadmin\", \"deploymentId\": \"b74e0fc1-914b-4009-b11c-52e6278****\", \"deploymentName\": \"sqlJob\", \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMode\": \"STREAMING\", \"flinkConf\": { \"table.exec.operatorname.max-length\": \"10240\", \"env.java.opts.jobmanager\": \"- Xloggc:/opt/flink/log/jobmanager-gc.log -XX:+UseGCLogFileRotation - XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M\", \"***\":\"***\" }, \"jobId \": \"003fbc67-1c8c-4147-9bf4-19da2****7\", \"logging\": { \"log4j2ConfigurationTemplate\": \"<?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" *** *\\", \"log4jLoggers\": [ { \"loggerLevel\": \"INFO\", \"l oggerName\": \"\" } ], \"logReservePolicy\": { \"expirationDays\": 7, \"openHistory\": true } }, \"modifier\": \"2087 78482972****\", \"modifierName\": \"flinkadmin\", \"namespace\": \"flinkteam\", \"restoreStrategy\": { \"kind\": \"NONE\" }, \"startTime\": 1783059223, \"status\": { \"currentJobStatus\": \"STARTING\" }, \"streamingResourceSetting\": { \"basicResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \"taskmanagerResourceSettingSpec\": { \"cp u\": 1.0, \"memory\": \"4Gi\" } }, \"resourceSettingMode\": \" BASIC\" }, \"userFlinkConf\": { \"execution.checkpointing.interval\": \"180s\", \"table.exec.state.ttl\": \"36 h\", \"restart-strategy.fixeddelay.delay\": \"10 s\", \"restart-strategy\": \"fixed-delay\", \"restartstrategy.fixed-delay.attempts\": \"214748****\", \"execution.checkpointing.min-pau se\": \"180s\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;artifact&quot;: {
      &quot;kind&quot;: &quot;SQLSCRIPT&quot;,
      &quot;sqlArtifact&quot;: {
        &quot;sqlScript&quot;: &quot;CREATE TEMPORARY TABLE `datahub_table` (strname VA
RCHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27; );CREATE TEMPORARY TABLE ` kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;prin t&#x27; );INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (C HAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;
```

`}` `},`

```
&quot;creator&quot;:&quot;20877848297****&quot;
```

```
    &quot;creator&quot;: &quot;20877848297****&quot;,
    &quot;creatorName&quot;: &quot;flinkadmin&quot;,
    &quot;deploymentId&quot;: &quot;b74e0fc1-914b-4009-b11c-52e6278****&quot;,
    &quot;deploymentName&quot;: &quot;sqlJob&quot;,
    &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
    &quot;executionMode&quot;: &quot;STREAMING&quot;,
    &quot;flinkConf&quot;: {
      &quot;table.exec.operator-name.max-length&quot;: &quot;10240&quot;,
      &quot;env.java.opts.jobmanager&quot;: &quot;-Xloggc:/opt/flink/log/jobmanager-gc.
log -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M&quot;,
      &quot;***&quot;:&quot;***&quot;
```

`},`

```
    &quot;jobId&quot;: &quot;003fbc67-1c8c-4147-9bf4-19da2****7&quot;,
    &quot;logging&quot;: {
      &quot;log4j2ConfigurationTemplate&quot;: &quot;&lt;?xml version=\&quot;1.0\&quot;
encoding=\&quot;UTF-8\&quot; ****&quot;,
      &quot;log4jLoggers&quot;: [
```

`{`

```
          &quot;loggerLevel&quot;: &quot;INFO&quot;,
          &quot;loggerName&quot;: &quot;&quot;
```

`}` `],`

```
      &quot;logReservePolicy&quot;: {
        &quot;expirationDays&quot;: 7,
        &quot;openHistory&quot;: true
```

`}` `},`

```
    &quot;modifier&quot;: &quot;208778482972****&quot;,
    &quot;modifierName&quot;: &quot;flinkadmin&quot;,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;restoreStrategy&quot;: {
      &quot;kind&quot;: &quot;NONE&quot;
```

`},`

```
    &quot;startTime&quot;: 1783059223,
    &quot;status&quot;: {
      &quot;currentJobStatus&quot;: &quot;STARTING&quot;
```

`},`

```
    &quot;streamingResourceSetting&quot;: {
      &quot;basicResourceSetting&quot;: {
        &quot;jobmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
```

`},`

```
        &quot;parallelism&quot;: 1,
        &quot;taskmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
```

`}` `},`

```
      &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
```

`},`

```
    &quot;userFlinkConf&quot;: {
      &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
      &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
&quot;restart-strategy.fixed-delay.delay&quot;:&quot;10s&quot;,
```

```
      &quot;restartstrategy.fixeddelay.delay&quot;: &quot;10 s&quot;,
      &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
      &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;214748****&quot;,
      &quot;execution.checkpointing.min-pause&quot;: &quot;180s&quot;
```

`}`

```xml
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.6 StartJob

Start a job instance.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Syntax**

```
POST /api/v2/namespaces/[namespace]/jobs HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the project. |

| Parameter | Type | Position | Required | Example | Descriptio n |
|---|---|---|---|---|---|

|   | Parameter |   | Type |   |   | Position |   | Required |   | Example |   | Descriptio n |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   | {'deployme |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | {'deployme |   |   |
|   |   |   |   |   |   |   |   |   |   | ntId':'7e3f3 |   |   |   |
|   |   |   |   |   |   |   |   |   |   | e05-337a- |   |   |   |
|   |   |   |   |   |   |   |   |   |   | 47a0-b944- |   |   |   |
|   |   |   |   |   |   |   |   |   |   | b41e3****',' |   |   |   |
|   |   |   |   |   |   |   |   |   |   | resourceSett |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ingSpec': |   |   |   |
|   |   |   |   |   |   |   |   |   |   | {'streamingR |   |   |   |
|   |   |   |   |   |   |   |   |   |   | esourceSetti |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ng': |   |   |   |
|   |   |   |   |   |   |   |   |   |   | {'basicResou |   |   |   |
|   |   |   |   |   |   |   |   |   |   | rceSetting': |   |   |   |
|   |   |   |   |   |   |   |   |   |   | {'jobmanager |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ResourceSett |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ingSpec': |   | The |   |
|   |   |   |   |   |   |   |   |   |   |   |   | parameters |   |
|   | body |   | String |   |   | wholebody |   | Yes |   | {'cpu':'1.0' |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | for starting |   |
|   |   |   |   |   |   |   |   |   |   | ,'memory':'4 |   | an instance. |   |
|   |   |   |   |   |   |   |   |   |   | Gi'},'parall |   |   |   |
|   |   |   |   |   |   |   |   |   |   | elism':1,'ta |   |   |   |
|   |   |   |   |   |   |   |   |   |   | skmanagerRes |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ourceSetting |   |   |   |
|   |   |   |   |   |   |   |   |   |   | Spec': |   |   |   |
|   |   |   |   |   |   |   |   |   |   | {'cpu':'1.0' |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ,'memory':'4 |   |   |   |
|   |   |   |   |   |   |   |   |   |   | Gi'}},'resou |   |   |   |
|   |   |   |   |   |   |   |   |   |   | rceSettingMo |   |   |   |
|   |   |   |   |   |   |   |   |   |   | de':'BASIC'} |   |   |   |
|   |   |   |   |   |   |   |   |   |   | },'restoreSt |   |   |   |
|   |   |   |   |   |   |   |   |   |   | rategy': |   |   |   |
|   |   |   |   |   |   |   |   |   |   | {'kind':'NON |   |   |   |
|   |   |   |   |   |   |   |   |   |   | E'}} |   |   |   |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
|   |   | { "artifact": { "kind": "SQLSCRIPT", "sqlArtifact": { "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname |   |

| Realtime Compute k (Compute-Stor dition) Developer ager API | for Apache Fli age Separation Guide·AppMa |   | Realtime Comput |
|---|---|---|---|
| Parameter | Type | VARCHAR) Example with ( | Description |
| data | String | 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ " } }, "creator": "208778482972*** *", "creatorName": "flinkadmin", "deploymentId": "f9d616ef-4422- 42b5-b95c- f691d****5", "deploymentName ": "sqlJob", "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "flinkConf": { "table.exec.operat or-name.max- length": "10240", "env.java.opts.job manager": "- Xloggc:/opt/flink/lo g/jobmanager- gc.log - XX:+UseGCLogFile Rotation - XX:NumberOfGCLo gFiles=2 - XX:GCLogFileSize= 50M", "***":"***" }, "jobId": "fa1b89ca- 908b-4cd5-b5b1- bb0ac****", "logging": { "log4j2Configuratio nTemplate": " | If success is false, the system returns a null value. If success is true, the system returns detailed data. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | If success is false, this value is not empty and indicates the business error code. If success is true, this value is empty. |
| errorMessage | String | "" | If success is false, the system returns the business error message. If success is true, the system returns a null value. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Request example

```
POST /api/v2/namespaces/[namespace]/jobs HTTP/1.1
```

`{`

```json
"namespace":"default-namespace", "body":"{'deploymentId':'7e3f3e05-337a-47a0-b944-b41e****','resourceSettingSpec':{'stre amingResourceSetting':{'basicResourceSetting':{'jobmanagerResourceSettingSpec':{'cpu':' 1.0','memory':'4Gi'},'parallelism':1,'taskmanagerResourceSettingSpec': {'cpu':'1.0','memory':'4Gi'}},'resourceSettingMode':'BASIC'}},'restoreStrategy':{'kind' :'NONE'}}"
```

`}` Successful response example `JSON` format `{`

```json
 "data":"{    \"artifact\": {      \"kind\": \"SQLSCRIPT\",      \"sqlArtifact\": {
\"sqlScript\": \"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'c onnector' = 'datagen'\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\ );\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ data hub_table;\\" } }, \"creator\": \"208778482972****\", \"creatorName\": \"flinkadmin\", \"deploymentId\": \"f9d616ef-4422-42b5-b95c-f691d****5\", \"deploymentName\": \"sqlJob\", \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMode\": \"STREAMING\", \"flinkConf\": { \"table.exec.operatorname.max-length\": \"10240\", \"env.java.opts.jobmanager\": \"- Xloggc:/opt/flink/log/jobmanager-gc.log -XX:+UseGCLogFileRotation - XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M\", \"***\":\"***\" }, \"jobId \": \"fa1b89ca-908b-4cd5-b5b1-bb0ac****\", \"logging\": { \"log4j2ConfigurationTemplate\": \"<?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" *** *\\", \"log4jLoggers\": [ { \"loggerLevel\": \"INFO\", \"l oggerName\": \"\" } ], \"logReservePolicy\": { \"expirationDays\": 7, \"openHistory\": true } }, \"modifier\": \"2087 78482972****\", \"modifierName\": \"flinkadmin\", \"namespace\": \"flinkteam\", \"restoreStrategy\": { \"kind\": \"NONE\" }, \"startTime\": 1783051000, \"status\": { \"currentJobStatus\": \"STARTING\" }, \"streamingResourceSetting\": { \"basicResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \"taskmanagerResourceSettingSpec\": { \"cp u\": 1.0, \"memory\": \"4Gi\" } }, \"resourceSettingMode\": \" BASIC\" }, \"userFlinkConf\": { \"execution.checkpointing.interval\": \"180s\", \"table.exec.state.ttl\": \"36 h\", \"restart-strategy.fixeddelay.delay\": \"10 s\", \"restart-strategy\": \"fixed-delay\", \"restartstrategy.fixed-delay.attempts\": \"214748****\", \"execution.checkpointing.min-pau se\": \"180s\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;artifact&quot;: {
      &quot;kind&quot;: &quot;SQLSCRIPT&quot;,
      &quot;sqlArtifact&quot;: {
        &quot;sqlScript&quot;: &quot;CREATE TEMPORARY TABLE `datahub_table` (strname VA
RCHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27; );CREATE TEMPORARY TABLE ` kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;prin t&#x27; );INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (C HAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;
```

`}` `},`

```
    &quot;creator&quot;: &quot;208778482972****&quot;,
    &quot;creatorName&quot;: &quot;flinkadmin&quot;,
    &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f691d****5&quot;,
```

`&` `t``d` `l` `tN` `&` `t` `&` `t`

```
lJb&
```

`t`

```
    &quot;deploymentName&quot;: &quot;sqlJob&quot;,
    &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
    &quot;executionMode&quot;: &quot;STREAMING&quot;,
    &quot;flinkConf&quot;: {
      &quot;table.exec.operator-name.max-length&quot;: &quot;10240&quot;,
      &quot;env.java.opts.jobmanager&quot;: &quot;-Xloggc:/opt/flink/log/jobmanager-gc.
log -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M&quot;,
      &quot;***&quot;:&quot;***&quot;
```

`},`

```
    &quot;jobId&quot;: &quot;fa1b89ca-908b-4cd5-b5b1-bb0ac****&quot;,
    &quot;logging&quot;: {
      &quot;log4j2ConfigurationTemplate&quot;: &quot;&lt;?xml version=\&quot;1.0\&quot;
encoding=\&quot;UTF-8\&quot; ****&quot;,
      &quot;log4jLoggers&quot;: [
```

`{`

```
          &quot;loggerLevel&quot;: &quot;INFO&quot;,
          &quot;loggerName&quot;: &quot;&quot;
```

`}` `],`

```
      &quot;logReservePolicy&quot;: {
        &quot;expirationDays&quot;: 7,
        &quot;openHistory&quot;: true
```

`}` `},`

```
    &quot;modifier&quot;: &quot;208778482972****&quot;,
    &quot;modifierName&quot;: &quot;flinkadmin&quot;,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;restoreStrategy&quot;: {
      &quot;kind&quot;: &quot;NONE&quot;
```

`},`

```
    &quot;startTime&quot;: 1783051000,
    &quot;status&quot;: {
      &quot;currentJobStatus&quot;: &quot;STARTING&quot;
```

`},`

```
    &quot;streamingResourceSetting&quot;: {
      &quot;basicResourceSetting&quot;: {
        &quot;jobmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
```

`},`

```
        &quot;parallelism&quot;: 1,
        &quot;taskmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
```

`}` `},`

```
      &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
```

`},`

```
    &quot;userFlinkConf&quot;: {
      &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
      &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
      &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;,
      &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
      &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;214748****&quot;,
&quot;executioncheckpointingmin-pause&quot;:&quot;180s&quot;
```

```
      &quot;execution.checkpointing.minpause&quot;: &quot;180s&quot;
```

`}`

```xml
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.7 ListSavepoints

Get a list of job snapshots and recent system checkpoints.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Syntax**

```
GET /api/v2/namespaces/[namespace]/savepoints HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the project. |
| deployme ntId | Strin g | Query | No | d0b3abf0-4bfe-46b1- a324-5b7de**** | The ID of the job. |
| jobId | Strin g | Query | No | 5af678c0-7db0-4650- 94c2-d2604f0a**** | The ID of the instance. |
| pageSize | Integ er | Query | No | 10 | The number of entries to return on each page. Valid values: 1 to 100. Default value: 10. |
| pageIndex | Integ er | Query | No | 1 | The page number. Minimum value: 1. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The ID of the request. |
| data | String | [ { "createdAt": 17830****, "deploymentId": "f9d616ef-4422- 42b5-b95c- f691d4****", "description": "", "jobId": "fa1b89ca- 908b-4cd5-b5b1- bb0ac74****", "modifiedAt": 178305****, "namespace": "flinkteam", "nativeFormat": false, "savepointId": "f1702682-c180- 4799-954a- e3217****", "savepointLocation ": "oss://flink- fullymanaged- ttor1krb1mjo85/flin k- savepoints/namesp aces/flinkteam/dep loyments/f9d616ef- ****", "savepointOrigin": "USER REQUEST", _ "status": { "state": "STARTED" }, "stopWithDrainEna bled": false } ] | If success is false, the system returns a null value. If success is true, the system returns detailed data. |
| errorCode | String | "" | If success is false, this value is not empty and indicates the business error code. If success is true, this value is empty. |
| errorMessage | String | "" | If success is false, the system returns the business error message. If success is true, the system returns a null value. |
| httpCode | Integer | 200 | The HTTP status code. |
| totalSize | Integer | 1 | The total number of entries. |

| dition) Developer ager API | Guide·AppMa |   | Realtime Comput |
|---|---|---|---|
| Parameter | Type | Example | Description |
| pageIndex | Integer | 1 | The page number. |
| pageSize | Integer | 10 | The number of entries to return on each page. |

**Examples**

Sample requests

```
GET /api/v2/namespaces/[namespace]/savepoints HTTP/1.1 &namespace=default-namespace &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "totalSize":1,
 "data":"[    {      \"createdAt\": 17830****,      \"deploymentId\": \"f9d616ef-4422-
42b5-b95c-f691d4****\", \"description\": \"\", \"jobId\": \"fa1b89ca-908b- 4cd5-b5b1-bb0ac74****\", \"modifiedAt\": 178305****, \"namespace\": \"flinkteam\", \"nativeFormat\": false, \"savepointId\": \"f1702682-c180- 4799-954a-e3217****\", \"savepointLocation\": \"oss://flink-fullymanagedttor1krb1mjo85/flink-savepoints/namespaces/flinkteam/deployments/f9d616ef-****\", \"savepointOrigin\": \"USER_REQUEST\", \"status\": { \"state\": \"STARTED\" }, \"stopWithDrainEnabled\": false } ]",
 "pageIndex":1,
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "pageSize":10,
 "httpCode":200
```

`}` `XML` format

```xml
<totalSize>1</totalSize> <data>[
```

`{`

```
      &quot;createdAt&quot;: 17830****,
      &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f691d4****&quot;,
      &quot;description&quot;: &quot;&quot;,
      &quot;jobId&quot;: &quot;fa1b89ca-908b-4cd5-b5b1-bb0ac74****&quot;,
      &quot;modifiedAt&quot;: 178305****,
      &quot;namespace&quot;: &quot;flinkteam&quot;,
      &quot;nativeFormat&quot;: false,
      &quot;savepointId&quot;: &quot;f1702682-c180-4799-954a-e3217****&quot;,
      &quot;savepointLocation&quot;: &quot;oss://flink-fullymanaged-
ttor1krb1mjo85/flink-savepoints/namespaces/flinkteam/deployments/f9d616ef-****&quot;,
      &quot;savepointOrigin&quot;: &quot;USER_REQUEST&quot;,
      &quot;status&quot;: {
        &quot;state&quot;: &quot;STARTED&quot;
```

`},`

```
      &quot;stopWithDrainEnabled&quot;: false
```

`}`

```xml
  ]</data>
 <pageIndex>1</pageIndex>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <pageSize>10</pageSize>
 <httpCode>200</httpCode>
```

##### 3.1.3.8 ListJobs

Queries information about all job instances of a deployed job.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Syntax**

```
GET /api/v2/namespaces/[namespace]/jobs HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the project workspace. |

| k (Compute- dition) Devel ager API | Storage S oper Gui | eparation de·AppMa |   |   | Realtime Comput |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | Description |
| pageIndex | Integ er | Query | No | 1 | The page number for pagination. The minimum value is 1. The default value is 1. |
| pageSize | Integ er | Query | No | 10 | The number of items per page for pagination. The maximum value is 100. The minimum value is 1. The default value is 10. |
| deployme ntId | Strin g | Query | Yes | d0b3abf0-4bfe-46b1- a324-5b7d**** | The ID of the job. |
| sortName | Strin g | Query | No | gmt create _ | The sorting rule. Valid values: gmt create (creation _ time) job id (job ID) _ status (status) |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | [ { "artifact": { "kind": "SQLSCRIPT" }, "creator": "20877848297**** ", "creatorName": "flinkadmin", "deploymentId": "91cf243c-7a10- 4728-ba77- c22313****", "deploymentName ": "sqlJob", "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "jobId": "4f86148c- fc32-40df-9047- b9f418****", "metric": { "totalCpu": 2.0, "totalMemoryByte" : 858993**** }, "modifier": "208778482972*** *", "modifierName": "flinkadmin", "namespace": "flinkteam", "restoreStrategy": { "kind": "NONE" }, "startTime": 178330****, "status": { "currentJobStatus": "RUNNING", "running": { "observedFlinkJobR estarts": 0, "observedFlinkJobS tatus": "RUNNING" } }, "streamingResourc eSetting": { "basicResourceSett ing": { "jobmanagerResou rceSettingSpec": { "cpu": 1.0, "memory": "4Gi" }, "parallelism": 1, "taskmanagerReso urceSettingSpec": { "cpu": 1.0, "memory": "4Gi" } }, "resourceSettingM ode": "BASIC" } } ] | If success is false, the API returns a null value. If success is true, the API returns detailed data. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | If success is false, this value is not empty and indicates the business error code. If success is true, this value is empty. |
| errorMessage | String | "" | If success is false, the API returns the business error message. If success is true, the API returns a null value. |
| httpCode | Integer | 200 | The HTTP status code. |
| totalSize | Integer | 1 | The total number of items. |
| pageIndex | Integer | 1 | The page index for pagination, which indicates the requested page number. |
| pageSize | Integer | 10 | The number of items per page for pagination, which indicates the number of items on the requested page. |

**Examples**

Sample request

```
GET /api/v2/namespaces/[namespace]/jobs HTTP/1.1 &namespace=default-namespace &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7d**** &Common request parameters
```

Sample success response `JSON` format `{`

```json
 "totalSize":1,
 "data":"[    {      \"artifact\": {        \"kind\": \"SQLSCRIPT\"      },
\"creator\": \"20877848297****\", \"creatorName\": \"flinkadmin\", \"deploymentId\": \"91cf243c-7a10-4728-ba77-c22313****\", \"deploymentName\": \"sq lJob\", \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMode\": \"STREAMING\", \"jobId\": \"4f86148c-fc32-40df-9047-b9f418****\", \"metric\": { \"totalCpu\": 2.0, \"totalMemoryByte\": 858993**** }, \"modifier\": \"208778482972****\", \"modifierName\": \"flinkadmin\", \"namespace\": \"flinkteam\", \"restoreStrategy\": { \"kind\": \"NONE\" }, \"startTime\": 178330****, \"status\": { \"currentJobStatus\": \"RUN NING\", \"running\": { \"observedFlinkJobRestarts\": 0, \"obser vedFlinkJobStatus\": \"RUNNING\" } }, \"streamingResourceSetting\": { \"basicResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"c pu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \"taskmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \" 4Gi\" } }, \"resourceSettingMode\": \"BASIC\" } } ]",
 "pageIndex":1,
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "pageSize":10,
 "httpCode":200
```

`}` `XML` format

```xml
<totalSize>1</totalSize> <data>[
```

`{`

```
      &quot;artifact&quot;: {
        &quot;kind&quot;: &quot;SQLSCRIPT&quot;
```

`},`

```
      &quot;creator&quot;: &quot;20877848297****&quot;,
      &quot;creatorName&quot;: &quot;flinkadmin&quot;,
      &quot;deploymentId&quot;: &quot;91cf243c-7a10-4728-ba77-c22313****&quot;,
      &quot;deploymentName&quot;: &quot;sqlJob&quot;,
      &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
      &quot;executionMode&quot;: &quot;STREAMING&quot;,
      &quot;jobId&quot;: &quot;4f86148c-fc32-40df-9047-b9f418****&quot;,
      &quot;metric&quot;: {
        &quot;totalCpu&quot;: 2.0,
        &quot;totalMemoryByte&quot;: 858993****
```

`},`

```
      &quot;modifier&quot;: &quot;208778482972****&quot;,
      &quot;modifierName&quot;: &quot;flinkadmin&quot;,
      &quot;namespace&quot;: &quot;flinkteam&quot;,
      &quot;restoreStrategy&quot;: {
        &quot;kind&quot;: &quot;NONE&quot;
```

`},`

```
      &quot;startTime&quot;: 178330****,
      &quot;status&quot;: {
```

`&` `t`

```
tJbStt
```

`&` `t` `&`

```
tRUNNING&
```

`t`

```
        &quot;currentJobStatus&quot;: &quot;RUNNING&quot;,
        &quot;running&quot;: {
          &quot;observedFlinkJobRestarts&quot;: 0,
          &quot;observedFlinkJobStatus&quot;: &quot;RUNNING&quot;
```

`}` `},`

```
      &quot;streamingResourceSetting&quot;: {
        &quot;basicResourceSetting&quot;: {
          &quot;jobmanagerResourceSettingSpec&quot;: {
            &quot;cpu&quot;: 1.0,
            &quot;memory&quot;: &quot;4Gi&quot;
```

`},`

```
          &quot;parallelism&quot;: 1,
          &quot;taskmanagerResourceSettingSpec&quot;: {
            &quot;cpu&quot;: 1.0,
            &quot;memory&quot;: &quot;4Gi&quot;
```

`}` `},`

```
        &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
```

`}` `}`

```xml
  ]</data>
 <pageIndex>1</pageIndex>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <pageSize>10</pageSize>
 <httpCode>200</httpCode>
```

```html ```

##### 3.1.3.9 ListEngineVersionMetadata

Obtains the list of engine versions that the system supports.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Syntax**

```
GET /api/v2/engine-version-meta.json HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-wulan-env188-d01 | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| data | String |   | If the value of success is false, a null value is returned. If the value of success is true, the detailed information is returned. |

|   |   | { "defaultEngineVers ion": "vvr-11.5.0- flink-1.20", "engineVersionMet adata": [ { "engineVersion": "vvr-6.0.0-flink- 1.15", "features": { "supportNativeSav epoint": true, "useForSqlDeploy ments": true }, "status": "DEPRECATED" }, { "engineVersion": "vvr-11.5.0-flink- 1.20", "features": { "supportNativeSav epoint": true, "useForSqlDeploy ments": true }, "status": "STABLE" }, { "engineVersion": "vvr-4.0.18-flink- |   |
|---|---|---|---|
|   |   | 1.13", "features": { "supportNativeSav epoint": true, "useForSqlDeploy |   |
| errorCode | String | ments": true }, "status": "DEPRECATED" }, {"" "engineVersion": "vvr-8.0.7-flink- 1.17", "features": { "supportNativeSav | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |
| errorMessage | String | epoint": true, "useForSqlDeploy ments": true }, ""s"tatus": "STABLE" } ] } | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
GET /api/v2/engine-version-meta.json HTTP/1.1 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"{    \"defaultEngineVersion\": \"vvr-11.5.0-flink-1.20\",
\"engineVersionMetadata\": [ { \"engineVersion\": \"vvr-6.0.0-flink-1.15\", \"features\": { \"supportNativeSavepoint\": true, \"useForSqlDeployments\": true }, \"status\": \"DEPRECATED\" }, { \"engineVersion\": \"vvr-11.5.0-flink-1.20\", \"features\": { \ "supportNativeSavepoint\": true, \"useForSqlDeployments\": true }, \"status\": \"STABLE\" }, { \"engineVersion\": \"vvr-4.0.18-flink-1.13\ ", \"features\": { \"supportNativeSavepoint\": true, \"useForSqlDeployments\": true }, \"status\": \"DEPRECATED\" }, { \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"features\": { \" supportNativeSavepoint\": true, \"useForSqlDeployments\": true }, \"status\": \"STABLE\" } ] }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;defaultEngineVersion&quot;: &quot;vvr-11.5.0-flink-1.20&quot;,
    &quot;engineVersionMetadata&quot;: [
```

`{`

```
        &quot;engineVersion&quot;: &quot;vvr-6.0.0-flink-1.15&quot;,
        &quot;features&quot;: {
          &quot;supportNativeSavepoint&quot;: true,
          &quot;useForSqlDeployments&quot;: true
```

`},`

```
        &quot;status&quot;: &quot;DEPRECATED&quot;
```

`},` `{`

```
        &quot;engineVersion&quot;: &quot;vvr-11.5.0-flink-1.20&quot;,
        &quot;features&quot;: {
          &quot;supportNativeSavepoint&quot;: true,
          &quot;useForSqlDeployments&quot;: true
```

`},`

```
        &quot;status&quot;: &quot;STABLE&quot;
```

`},` `{`

```
        &quot;engineVersion&quot;: &quot;vvr-4.0.18-flink-1.13&quot;,
        &quot;features&quot;: {
          &quot;supportNativeSavepoint&quot;: true,
          &quot;useForSqlDeployments&quot;: true
```

`},`

```
        &quot;status&quot;: &quot;DEPRECATED&quot;
```

`},` `{`

```
        &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
        &quot;features&quot;: {
          &quot;supportNativeSavepoint&quot;: true,
          &quot;useForSqlDeployments&quot;: true
```

`},`

```
        &quot;status&quot;: &quot;STABLE&quot;
```

`}` `]`

```xml
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.10 ListDeploymentTargets

Obtains a list of clusters in which deployments can be deployed. The cluster can be a session cluster or a per-job cluster.

**Request headers**

| 88 |   |   |   | > D | ocument Version: 2026082 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Syntax**

```
GET /api/v2/namespaces/[namespace]/deployment-targets HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| pageSize | Integ er | Quer y | No | 10 | The number of entries per page. Valid values: 1 to 100. Default value: 10. |
| pageIndex | Integ er | Quer y | No | 1 | The page number. Minimum value: 1. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

| data | String | [ { "name": "dt- flinkteam", "namespace": "flinkteam" } ] | If the value of success is false, a null value is returned. If the value of success is true, the detailed information is returned. |
|---|---|---|---|
| errorCode | String | "" | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |
| errorMessage | String | "" | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |
| httpCode | Integer | 200 | The HTTP status code. |
| totalSize | Integer | 1 | The total number of entries. |

**Examples**

Sample requests

```
GET /api/v2/namespaces/[namespace]/deployment-targets HTTP/1.1 &namespace=default-namespace &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "totalSize":1,
 "data":"[    {      \"name\": \"dt-flinkteam\",      \"namespace\": \"flinkteam\"    }
]", "success":true, "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****", "errorMessage":"", "errorCode":"", "httpCode":200
```

`}` `XML` format

```xml
<totalSize>1</totalSize> <data>[
```

`{`

```
      &quot;name&quot;: &quot;dt-flinkteam&quot;,
      &quot;namespace&quot;: &quot;flinkteam&quot;
```

`}`

```xml
  ]</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.11 GetSavepoint

Obtains the details of snapshots and system checkpoints.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Syntax**

```
GET /api/v2/namespaces/[namespace]/savepoints/[savepointId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| savepointI d | Strin g | Path | Yes | 907a8f0e-4f6c-412b- 8a5e-7d4a065b**** | The savepoint ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| data | String | { "createdAt": 178305****, "deploymentId": "f9d616ef-4422- 42b5-b95c- f691d44****5", "description": "", "jobId": "fa1b89ca- 908b-4cd5-b5b1- bb0****4", "modifiedAt": 178****, "namespace": "flinkteam", "nativeFormat": false, "savepointId": "f1702682-c180- 4799-954a- e3217e****", "savepointLocation ": "oss://flink- fullymanaged- ttor1krb1mjo85/flin k- savepoints/namesp aces/flinkteam/dep loyments/f9d616ef- 44****", "savepointOrigin": "USER REQUEST", _ "status": { "state": "STARTED" }, "stopWithDrainEna bled": false } | If the value of success is false, a null value is returned. If the value of success is true, the detailed information is returned. |
| errorCode | String | "" | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |
| errorMessage | String | "" | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |

| httpCode | Integer | 200 | The HTTP status code. |
|---|---|---|---|

**Examples**

Sample requests

```
GET /api/v2/namespaces/[namespace]/savepoints/[savepointId] HTTP/1.1 &namespace=default-namespace &savepointId=907a8f0e-4f6c-412b-8a5e-7d4a065b**** &Common request parameter
```

Sample success responses `JSON` format `{`

```json
 "data":"{    \"createdAt\": 178305****,    \"deploymentId\": \"f9d616ef-4422-42b5-b95c
-f691d44****5\", \"description\": \"\", \"jobId\": \"fa1b89ca-908b-4cd5-b5b1-bb0*
***4\",    \"modifiedAt\": 178****,    \"namespace\": \"flinkteam\",
\"nativeFormat\": false, \"savepointId\": \"f1702682-c180-4799-954a-e3217e****\", \"savepointLocation\": \"oss://flink-fullymanaged-ttor1krb1mjo85/flinksavepoints/namespaces/flinkteam/deployments/f9d616ef-44****\", \"savepointOrigin\": \"USER_REQUEST\", \"status\": { \"state\": \"STARTED\" }, \"stopWithDrainEnabled\": false }", "success":true, "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****", "errorMessage":"", "errorCode":"", "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;createdAt&quot;: 178305****,
    &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f691d44****5&quot;,
    &quot;description&quot;: &quot;&quot;,
    &quot;jobId&quot;: &quot;fa1b89ca-908b-4cd5-b5b1-bb0****4&quot;,
    &quot;modifiedAt&quot;: 178****,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;nativeFormat&quot;: false,
    &quot;savepointId&quot;: &quot;f1702682-c180-4799-954a-e3217e****&quot;,
    &quot;savepointLocation&quot;: &quot;oss://flink-fullymanaged-ttor1krb1mjo85/flink-
savepoints/namespaces/flinkteam/deployments/f9d616ef-44****&quot;,
    &quot;savepointOrigin&quot;: &quot;USER_REQUEST&quot;,
    &quot;status&quot;: {
      &quot;state&quot;: &quot;STARTED&quot;
```

`},`

```xml
    &quot;stopWithDrainEnabled&quot;: false
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.12 GetMember

Views the user authorization details.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Syntax**

```
GET /gateway/v2/namespaces/[namespace]/members/[member] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| namespac e | Strin g | Path | Yes | default-namespace | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
|---|---|---|---|---|---|
| member | Strin g | Path | Yes | user:2424254101**** | The member name. Format: user:${uid}. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| data | String | { "member": "231366754****", "role": "editor" } | If the value of success is false, a null value is returned. If the value of success is true, the detailed information is returned. |
| errorCode | String | "" | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |
| errorMessage | String | "" | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
GET /gateway/v2/namespaces/[namespace]/members/[member] HTTP/1.1 &namespace=default-namespace &member=user:2424254101**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"{    \"member\": \"231366754****\",    \"role\": \"editor\"  }",
"success":true, "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****", "errorMessage":"", "errorCode":"", "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;member&quot;: &quot;231366754****&quot;,
    &quot;role&quot;: &quot;editor&quot;
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.13 GetLatestJobStartLog

Obtains the latest startup log of a job instance.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Syntax**

```
GET /api/v2/namespaces/[namespace]/deployments/[deploymentId]/latest_jobmanager_start_log H TTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| namespac e | Strin g | Path | Yes | default-namespace | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
|---|---|---|---|---|---|
| deploymen tId | Strin g | Path | Yes | d0b3abf0-4bfe-46b1- a324-5b7de**** | The deployment ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| reason | String | "" | The error cause. A null value is returned if the service runs normally. |
| eagleEyeTrace Id | String | 0ad40c441762830 708230897**** | The EagleEye ID. |
| asapiSuccess | Boolean | true | Indicates that the operation call is successful with expected results and no errors. |
| asapiRequestI d | String | CF3A87DE-268D- 4E4B-865F- CCC911E70B1F | The ASAPI request ID. |
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| data | String | seconds: [1800] end new OSSLogClient endTimeInMs: [1783059502] **** | If the value of success is false, a null value is returned. If the value of success is true, the detailed information is returned. |
| errorCode | String | "" | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |

| errorMessage | String | "" | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |
|---|---|---|---|
| httpCode | Integer | 200 | The HTTP status code. |
| message | String | "" | The additional information. |

**Examples**

Sample requests

```
GET /api/v2/namespaces/[namespace]/deployments/[deploymentId]/latest_jobmanager_start_log H TTP/1.1 &namespace=default-namespace &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7de**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "reason":"",
 "eagleEyeTraceId":"0ad40c441762830708230897****",
 "asapiSuccess":true,
 "asapiRequestId":"CF3A87DE-268D-4E4B-865F-CCC911E70B1F",
 "data":"seconds: [1800]\end new OSSLogClient endTimeInMs:[1783059502] ****\",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200,
 "message":""
```

`}` `XML` format

```xml
<reason /> <eagleEyeTraceId>0ad40c441762830708230897****</eagleEyeTraceId> <asapiSuccess>true</asapiSuccess> <asapiRequestId>CF3A87DE-268D-4E4B-865F-CCC911E70B1F</asapiRequestId> <data>seconds: [1800]end new OSSLogClient endTimeInMs:[1783059502] ****</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode> <message />
```

##### 3.1.3.14 GetJob

Get the details of a job instance.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Syntax**

```
GET /api/v2/namespaces/[namespace]/jobs/[jobId] HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the project. |
| jobId | Strin g | Path | Yes | 5af678c0-7db0-4650- 94c2-d2604f0a**** | The ID of the job instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The ID of the request. |
|   |   | { "artifact": { "kind": "SQLSCRIPT", "sqlArtifact": { "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ |   |

| Parameter | Type | (strname Example VARCHAR, lens | Description |
|---|---|---|---|
| data | String | BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ " } }, "creator": "208778482972*** ", "creatorName": "flinkadmin", "deploymentId": "f9d616ef-4422- 42b5-b95c- f691d****", "deploymentName ": "sqlJob", "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "flinkConf": { "table.exec.operat or-name.max- length": "10240", "env.java.opts.job manager": "- Xloggc:/opt/flink/lo g/jobmanager- gc.log - XX:+UseGCLogFile Rotation - XX:NumberOfGCLo gFiles=2 - XX:GCLogFileSize= 50M", "***":"***" }, "jobId": "fa1b89ca- 908b-4cd5-b5b1- bb0ac****", "logging": { "log4j2Configuratio nTemplate": " | If success is false, the system returns a null value. If success is true, the system returns detailed data. |
| errorCode | String | "" | If success is false, this value is not empty and indicates the business error code. If success is true, this value is empty. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorMessage | String | "" | If success is false, the system returns the business error message. If success is true, the system returns a null value. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
GET /api/v2/namespaces/[namespace]/jobs/[jobId] HTTP/1.1 &namespace=default-namespace &jobId=5af678c0-7db0-4650-94c2-d2604f0a**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"{    \"artifact\": {      \"kind\": \"SQLSCRIPT\",      \"sqlArtifact\": {
\"sqlScript\": \"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'c onnector' = 'datagen'\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\ );\\INSERT INTO kafka_table\SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ data hub_table;\\" } }, \"creator\": \"208778482972***\", \"creatorName\": \"fl inkadmin\", \"deploymentId\": \"f9d616ef-4422-42b5-b95c-f691d****\", \"deploymentName\": \"sqlJob\", \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMode\": \"STREAMING\", \"flinkConf\": { \"table.exec.operatorname.max-length\": \"10240\", \"env.java.opts.jobmanager\": \"- Xloggc:/opt/flink/log/jobmanager-gc.log -XX:+UseGCLogFileRotation - XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M\", \"***\":\"***\" }, \"jobId\": \"fa1b89ca-908b-4cd5-b5b1-bb0ac****\", \"logging\": { \"log4j2ConfigurationTemplate\": \"<?xml version=\\\"1.0\\\" ***\", \"log4jLoggers\": [ { \"loggerLevel\": \"INFO\", \"loggerName\": \"\" } ], \"logReservePolicy\": { \"expirationDays\": 7, \"openHistory\": true } }, \"modifier\": \"2087 7848297****5\", \"modifierName\": \"flinkadmin\", \"namespace\": \"flinkteam\", \"restoreStrategy\": { \"kind\": \"NONE\" }, \"startTime\": 1783051000, \"status\": { \"currentJobStatus\": \"STARTING\" }, \"streamingResourceSetting\": { \"basicResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \"taskmanagerResourceSettingSpec\": { \"cp u\": 1.0, \"memory\": \"4Gi\" } }, \"resourceSettingMode\": \" BASIC\" }, \"userFlinkConf\": { \"execution.checkpointing.interval\": \"180s\", \"table.exec.state.ttl\": \"36 h\", \"restart-strategy.fixeddelay.delay\": \"10 s\", \"restart-strategy\": \"fixed-delay\", \"restartstrategy.fixed-delay.attempts\": \"21474****\", \"execution.checkpointing.min-paus e\": \"180s\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;artifact&quot;: {
      &quot;kind&quot;: &quot;SQLSCRIPT&quot;,
      &quot;sqlArtifact&quot;: {
        &quot;sqlScript&quot;: &quot;CREATE TEMPORARY TABLE `datahub_table` (strname VA
RCHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27; );CREATE TEMPORARY TABLE ` kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;prin t&#x27; );INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (C HAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;
```

`}` `},`

```
    &quot;creator&quot;: &quot;208778482972***&quot;,
    &quot;creatorName&quot;: &quot;flinkadmin&quot;,
    &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f691d****&quot;,
```

`&` `t``d` `l` `tN` `&` `t` `&` `t`

```
lJb&
```

`t`

```
    &quot;deploymentName&quot;: &quot;sqlJob&quot;,
    &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
    &quot;executionMode&quot;: &quot;STREAMING&quot;,
    &quot;flinkConf&quot;: {
      &quot;table.exec.operator-name.max-length&quot;: &quot;10240&quot;,
      &quot;env.java.opts.jobmanager&quot;: &quot;-Xloggc:/opt/flink/log/jobmanager-gc.
log -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=2 -XX:GCLogFileSize=50M&quot;,
      &quot;***&quot;:&quot;***&quot;
```

`},`

```
    &quot;jobId&quot;: &quot;fa1b89ca-908b-4cd5-b5b1-bb0ac****&quot;,
    &quot;logging&quot;: {
      &quot;log4j2ConfigurationTemplate&quot;: &quot;&lt;?xml version=\&quot;1.0\&quot;
***&quot;,
      &quot;log4jLoggers&quot;: [
```

`{`

```
          &quot;loggerLevel&quot;: &quot;INFO&quot;,
          &quot;loggerName&quot;: &quot;&quot;
```

`}` `],`

```
      &quot;logReservePolicy&quot;: {
        &quot;expirationDays&quot;: 7,
        &quot;openHistory&quot;: true
```

`}` `},`

```
    &quot;modifier&quot;: &quot;20877848297****5&quot;,
    &quot;modifierName&quot;: &quot;flinkadmin&quot;,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;restoreStrategy&quot;: {
      &quot;kind&quot;: &quot;NONE&quot;
```

`},`

```
    &quot;startTime&quot;: 1783051000,
    &quot;status&quot;: {
      &quot;currentJobStatus&quot;: &quot;STARTING&quot;
```

`},`

```
    &quot;streamingResourceSetting&quot;: {
      &quot;basicResourceSetting&quot;: {
        &quot;jobmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
```

`},`

```
        &quot;parallelism&quot;: 1,
        &quot;taskmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
```

`}` `},`

```
      &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
```

`},`

```
    &quot;userFlinkConf&quot;: {
      &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
      &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
      &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;,
      &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
      &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;21474****&quot;,
&quot;executioncheckpointingmin-pause&quot;:&quot;180s&quot;
```

```
      &quot;execution.checkpointing.minpause&quot;: &quot;180s&quot;
```

`}`

```xml
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.15 GetGenerateResourcePlanResult

Obtain the results of asynchronous fine-grained resource generation based on the asynchronous ticket ID.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Syntax**

```
GET /api/v2/namespaces/[namespace]/deployments/tickets/[ticketId]/resourceplan:asyncGenerate HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the project. |
| ticketId | Strin g | Path | Yes | 88a8fc49-e090-430a- 85d8-3ee8c79c**** | The receipt ID. Call the GenerateResourcePlanW ithFlinkConfAsync API to obtain this ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request succeeded. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "plan": " {\"ssgProfiles\": [{\"name\":\"defaul t\",\"cpu\":0.2,\"hea p\":\"768 mb\",\"offHeap\":\" 32 mb\",\"managed\": {},\"extended\": {}}],\"nodes\": [{\"id\":1,\"type\":\" StreamExecTableS ourceScan\",\"desc\ ":\"Source: datahub table[5]\", _ \"profile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\": 32768,\"minParalle lism\":1}}, {\"id\":2,\"type\":\" StreamExecCalc\",\ "desc\":\"Calc[6]\",\ "profile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\": 32768,\"minParalle lism\":1}}, {\"id\":3,\"type\":\" StreamExecSink\",\ "desc\":\"Sink: kafka table[7]\",\"p _ rofile\": {\"group\":\"default \",\"parallelism\":1,\ "maxParallelism\": 32768,\"minParalle lism\":1}}],\"edges \": [{\"source\":1,\"tar get\":2,\"mode\":\" PIPELINED\",\"strat egy\":\"FORWARD\" }, {\"source\":2,\"targ et\":3,\"mode\":\"PI PELINED\",\"strateg y\":\"FORWARD\"}] ,\"vertices\": {\"717c7b8afebbfb 7137f6****\": [1,2,3]}}", "ticketStatus": "FINISHED" } | If success is false, the system returns a null value. If success is true, the system returns detailed data. |
| errorCode | String | "" | If success is false, this value is not empty and indicates the business error code. If success is true, this value is empty. |

| n E n | Realtime Compute k (Compute-Stor dition) Developer ager API | for Apache Fli age Separation Guide·AppMa |   | Realtime Comput | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorMessage | String | "" | If success is false, the system returns the business error message. If success is true, the system returns a null value. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
GET /api/v2/namespaces/[namespace]/deployments/tickets/[ticketId]/resourceplan:asyncGenerate HTTP/1.1 &namespace=default-namespace &ticketId=88a8fc49-e090-430a-85d8-3ee8c79c**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "data":"{    \"plan\": \"{\\\"ssgProfiles\\\":
[{\\\"name\\\":\\\"default\\\",\\\"cpu\\\":0.2,\\\"heap\\\":\\\"768 mb\\\",\\\"offHeap\\\":\\\"32 mb\\\",\\\"managed\\\":{},\\\"extended\\\": {}}],\\\"nodes\\\": [{\\\"id\\\":1,\\\"type\\\":\\\"StreamExecTableSourceScan\\\",\\\"desc\\\":\\\"Source: datahub_table[5]\\\",\\\"profile\\\": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"min rallelism\\\":1}}, {\\\"id\\\":2,\\\"type\\\":\\\"StreamExecCalc\\\",\\\"desc\\\":\\\"Calc[6]\\\",\\\"profil \\": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"min rallelism\\\":1}}, {\\\"id\\\":3,\\\"type\\\":\\\"StreamExecSink\\\",\\\"desc\\\":\\\"Sink: kafka_table[7]\\\",\\\"profile\\\": {\\\"group\\\":\\\"default\\\",\\\"parallelism\\\":1,\\\"maxParallelism\\\":32768,\\\"min rallelism\\\":1}}],\\\"edges\\\": [{\\\"source\\\":1,\\\"target\\\":2,\\\"mode\\\":\\\"PIPELINED\\\",\\\"strategy\\\":\\\"F WARD\\\"}, {\\\"source\\\":2,\\\"target\\\":3,\\\"mode\\\":\\\"PIPELINED\\\",\\\"strategy\\\":\\\"FO ARD\\\"}],\\\"vertices\\\":{\\\"717c7b8afebbfb7137f6****\\\":[1,2,3]}}\", \"ticketStatus\": \"FINISHED\" }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;plan&quot;: &quot;{\&quot;ssgProfiles\&quot;:
[{\&quot;name\&quot;:\&quot;default\&quot;,\&quot;cpu\&quot;:0.2,\&quot;heap\&quot;:\&quo 768 mb\&quot;,\&quot;offHeap\&quot;:\&quot;32 mb\&quot;,\&quot;managed\&quot;:{},\&quot ;extended\&quot;:{}}],\&quot;nodes\&quot;: [{\&quot;id\&quot;:1,\&quot;type\&quot;:\&quot;StreamExecTableSourceScan\&quot;,\&quot;de \&quot;:\&quot;Source: datahub_table[5]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParallel m\&quot;:32768,\&quot;minParallelism\&quot;:1}}, {\&quot;id\&quot;:2,\&quot;type\&quot;:\&quot;StreamExecCalc\&quot;,\&quot;desc\&quot;:\& ot;Calc[6]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParallel m\&quot;:32768,\&quot;minParallelism\&quot;:1}}, {\&quot;id\&quot;:3,\&quot;type\&quot;:\&quot;StreamExecSink\&quot;,\&quot;desc\&quot;:\& ot;Sink: kafka_table[7]\&quot;,\&quot;profile\&quot;: {\&quot;group\&quot;:\&quot;default\&quot;,\&quot;parallelism\&quot;:1,\&quot;maxParallel m\&quot;:32768,\&quot;minParallelism\&quot;:1}}],\&quot;edges\&quot;: [{\&quot;source\&quot;:1,\&quot;target\&quot;:2,\&quot;mode\&quot;:\&quot;PIPELINED\&quot \&quot;strategy\&quot;:\&quot;FORWARD\&quot;}, {\&quot;source\&quot;:2,\&quot;target\&quot;:3,\&quot;mode\&quot;:\&quot;PIPELINED\&quot; &quot;strategy\&quot;:\&quot;FORWARD\&quot;}],\&quot;vertices\&quot;: {\&quot;717c7b8afebbfb7137f6****\&quot;:[1,2,3]}}&quot;,
    &quot;ticketStatus&quot;: &quot;FINISHED&quot;
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.16 GetDeployment

Obtains the details of a deployed job.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Syntax**

```
GET /api/v2/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| deploymen tId | Strin g | Path | Yes | d0b3abf0-4bfe-46b1- a324-5b7d**** | The job ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
|   |   | { "artifact": { "kind": "SQLSCRIPT", "sqlArtifact": { "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT strname, |   |

|   |   | CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ " } }, "creator": "2087784829****", "creatorName": "flinkadmin", "deploymentHasCh anged": true, "deploymentId": |   |
|---|---|---|---|
| data | String | "f9d616ef-4422- 42b5-b95c- f691****", "deploymentTarget ": { "mode": "PER JOB", _ "name": "dt- flinkteam" }, "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "flinkConf": { "execution.checkp ointing.interval": "180s", "table.exec.state.ttl ": "36 h", "restart- strategy.fixed- delay.delay": "10 s", "restart- strategy": "fixed- delay", "restart- strategy.fixed- delay.attempts": "21474****", "execution.checkp ointing.min-pause": "180s" }, "jobSummary": { "cancelled": 0, "cancelling": 0, "failed": 0, "finished": 0, "running": 0, "starting": 0 }, "logging": { "log4jLoggers": [ { "loggerLevel": "INFO", "loggerName": "" } ], "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "modifier": "208778482****", "modifierName": "flinkadmin", | If the value of success is false, a null value is returned. If the value of success is true, the detailed information is returned. |

|   |   | "name": "sqlJob", "namespace": "flinkteam", "streamingResourc eSetting": { "basicResourceSett ing": { "jobmanagerResou rceSettingSpec": { "cpu": 1.0, "memory": "4Gi" }, "parallelism": 1, "taskmanagerReso urceSettingSpec": { "cpu": 1.0, "memory": "4Gi" } }, "resourceSettingM ode": "BASIC" } } |   |
|---|---|---|---|
| errorCode | String | "" | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |
| errorMessage | String | "" | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
GET /api/v2/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1 &namespace=default-namespace &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7d**** &Common Request Parameter
```

Sample success responses `JSON` format `{`

```json
 "data":"{    \"artifact\": {      \"kind\": \"SQLSCRIPT\",      \"sqlArtifact\": {
\"sqlScript\": \"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'c onnector' = 'datagen'\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\ );\\INSERT INTO kafka_table\SELECT strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\\" } }, \"creator\": \"2087784829****\", \"creatorName\": \"flinkadmin\", \"deploymentHasChanged\": true, \"deploymentId\": \"f9d616ef-4422-42b5-b95c-f691**** \", \"deploymentTarget\": { \"mode\": \"PER_JOB\", \"name\": \"dtflinkteam\" }, \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMode\": \"STREAMING\", \"flinkConf\": { \"execution.checkpointing.interval\": \"180s\", \"table.exec.state.ttl\": \"36 h\", \"restart-strategy.fixed-delay.delay\": \"10 s \", \"restart-strategy\": \"fixed-delay\", \"restart-strategy.fixeddelay.attempts\": \"21474****\", \"execution.checkpointing.min-pause\": \"180s\" }, \"jobSummary\": { \"cancelled\": 0, \"cancelling\": 0, \"failed\": 0, \"finished\": 0, \"running\": 0, \"starting\": 0 }, \"logging\": { \"log4jLoggers\": [ { \"loggerLevel\": \"INFO\", \"loggerName\": \"\" } ], \"logReservePolicy\": { \"expirationDays\": 7, \"openHistory\": true }, \"loggingProfile\": \"d efault\" }, \"modifier\": \"208778482****\", \"modifierName\": \"flinkadmin\", \"name\": \"sqlJob\", \"namespace\": \"flinkteam\", \"streamingResourceSetting\": { \"basicResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \ "taskmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" } }, \"resourceSettingMode\": \"BASIC\" } }", "success":true, "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****", "errorMessage":"", "errorCode":"", "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;artifact&quot;: {
      &quot;kind&quot;: &quot;SQLSCRIPT&quot;,
      &quot;sqlArtifact&quot;: {
        &quot;sqlScript&quot;: &quot;CREATE TEMPORARY TABLE `datahub_table` (strname VA
RCHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27; );CREATE TEMPORARY TABLE ` kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;prin t&#x27; );INSERT INTO kafka_tableSELECT strname, CAST (CHAR_LENGTH (strname) AS BIGINT ) AS lensFROM datahub_table;&quot;
```

`}` `},`

```
&quot;creator&quot;: &quot;2087784829****&quot;, &quot;creatorName&quot;: &quot;flinkadmin&quot;, &quot;deploymentHasChanged&quot;: true, &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f691****&quot;, &quot;deploymentTarget&quot;: { &quot;mode&quot;: &quot;PER_JOB&quot;, &quot;name&quot;: &quot;dt-flinkteam&quot;
```

`},` `&` `t` `i` `i` `&` `t` `&` `t`

```
807flik117&
```

`t`

|   | &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;, &quot;executionMode&quot;: &quot;STREAMING&quot;, &quot;flinkConf&quot;: { &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;, &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;, &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;, &quot;restart-strategy&quot;: &quot;fixed-delay&quot;, &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;21474****&quot;, &quot;execution.checkpointing.min-pause&quot;: &quot;180s&quot; }, &quot;jobSummary&quot;: { &quot;cancelled&quot;: 0, &quot;cancelling&quot;: 0, &quot;failed&quot;: 0, &quot;finished&quot;: 0, &quot;running&quot;: 0, &quot;starting&quot;: 0 }, &quot;logging&quot;: { &quot;log4jLoggers&quot;: [ { &quot;loggerLevel&quot;: &quot;INFO&quot;, &quot;loggerName&quot;: &quot;&quot; } ], &quot;logReservePolicy&quot;: { &quot;expirationDays&quot;: 7, &quot;openHistory&quot;: true }, &quot;loggingProfile&quot;: &quot;default&quot; }, &quot;modifier&quot;: &quot;208778482****&quot;, &quot;modifierName&quot;: &quot;flinkadmin&quot;, &quot;name&quot;: &quot;sqlJob&quot;, &quot;namespace&quot;: &quot;flinkteam&quot;, &quot;streamingResourceSetting&quot;: { &quot;basicResourceSetting&quot;: { &quot;jobmanagerResourceSettingSpec&quot;: { &quot;cpu&quot;: 1.0, &quot;memory&quot;: &quot;4Gi&quot; }, &quot;parallelism&quot;: 1, &quot;taskmanagerResourceSettingSpec&quot;: { &quot;cpu&quot;: 1.0, &quot;memory&quot;: &quot;4Gi&quot; } }, &quot;resourceSettingMode&quot;: &quot;BASIC&quot; } }</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode> |   |
|---|---|---|

```xml
<httpCode>200</httpCode>
```

##### 3.1.3.17 GenerateResourcePlanWithFlinkConfAsync

Submits a ticket to asynchronously generate a resource plan and returns an asynchronous ticket ID to query the ticket result.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Syntax**

```
POST /api/v2/namespaces/[namespace]/deployments/[deploymentId]/resourceplan:asyncGenerate HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the project. |
| deployme ntId | Strin g | Path | Yes | d0b3abf0-4bfe-46b1- a324-5**** | The unique ID of the deployment. |

| Parameter | Type | Position | Required | Example | Descriptio n |
|---|---|---|---|---|---|

|   | Parameter |   | Type |   | Position |   | Required |   | Example |   | Descriptio n |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   | {'executio |   |   |   |
|   |   |   |   |   |   |   |   |   |   | {'executio |   |   |
|   |   |   |   |   |   |   |   |   | n.checkpoint |   |   |   |
|   |   |   |   |   |   |   |   |   | ing.interval |   |   |   |
|   |   |   |   |   |   |   |   |   | ': '180s', |   |   |   |
|   |   |   |   |   |   |   |   |   | 'execution.c |   |   |   |
|   |   |   |   |   |   |   |   |   | heckpointing |   |   |   |
|   |   |   |   |   |   |   |   |   | .min- |   |   |   |
|   |   |   |   |   |   |   |   |   | pause': |   |   |   |
|   |   |   |   |   |   |   |   |   | '180s', |   |   |   |
|   |   |   |   |   |   |   |   |   | 'restart- |   |   |   |
|   |   |   |   |   |   |   |   |   | strategy': |   |   |   |
|   |   |   |   |   |   |   |   |   | 'fixed- |   | The Flink |   |
|   |   |   |   |   |   |   |   |   | delay', |   | configuration |   |
|   |   |   |   |   |   |   |   |   |   |   | for |   |
|   | body |   | String |   | Body |   | No |   | 'restart- |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | generating a |   |
|   |   |   |   |   |   |   |   |   | strategy.fix |   | resource |   |
|   |   |   |   |   |   |   |   |   | ed- |   | plan. |   |
|   |   |   |   |   |   |   |   |   | delay.attemp |   |   |   |
|   |   |   |   |   |   |   |   |   | ts': |   |   |   |
|   |   |   |   |   |   |   |   |   | '2147483647' |   |   |   |
|   |   |   |   |   |   |   |   |   | , 'restart- |   |   |   |
|   |   |   |   |   |   |   |   |   | strategy.fix |   |   |   |
|   |   |   |   |   |   |   |   |   | ed- |   |   |   |
|   |   |   |   |   |   |   |   |   | delay.delay' |   |   |   |
|   |   |   |   |   |   |   |   |   | : '10 s', |   |   |   |
|   |   |   |   |   |   |   |   |   | 'table.exec. |   |   |   |
|   |   |   |   |   |   |   |   |   | state.ttl': |   |   |   |
|   |   |   |   |   |   |   |   |   | '36 h'} |   |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The ID of the request. |
| data | String | { "ticketId": "fda9f510-a668- 4de1-9c0f-9fc****" } | If success is false, the system returns a null value. If success is true, the system returns detailed data. |
| errorCode | String | "" | If success is false, this value is not empty and indicates the business error code. If success is true, this value is empty. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorMessage | String | "" | If success is false, the system returns the business error message. If success is true, the system returns a null value. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Request example

```
POST /api/v2/namespaces/[namespace]/deployments/[deploymentId]/resourceplan:asyncGenerate HTTP/1.1
```

`{`

```json
"namespace":"default-namespace", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5****"
```

`}` Success response example `JSON` format `{`

```json
 "data":"{    \"ticketId\": \"fda9f510-a668-4de1-9c0f-9fc****\"  }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;ticketId&quot;: &quot;fda9f510-a668-4de1-9c0f-9fc****&quot;
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.18 DeleteVariable

Deletes a variable.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Syntax**

```
DELETE /api/v2/namespaces/[namespace]/variables/[name] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| name | Strin g | Path | Yes | variableName | The name of the variable to delete. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| errorCode | String | "" | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |

| errorMessage | String | "" | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |
|---|---|---|---|
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
DELETE /api/v2/namespaces/[namespace]/variables/[name] HTTP/1.1 &namespace=default-namespace &name=blinkteam &Common Request Parameter
```

Sample success responses `JSON` format `{`

```json
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode>
```

##### 3.1.3.19 DeleteSavepoint

Deletes a snapshot.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |
|---|---|---|---|---|---|

**Syntax**

```
DELETE /api/v2/namespaces/[namespace]/savepoints/[savepointId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| savepointI d | Strin g | Path | Yes | 907a8f0e-4f6c-412b- 8a5e-7d4a065b**** | The ID of the savepoint to delete. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| errorCode | String | "" | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |
| errorMessage | String | "" | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
DELETE /api/v2/namespaces/[namespace]/savepoints/[savepointId] HTTP/1.1 &namespace=default-namespace &savepointId=907a8f0e-4f6c-412b-8a5e-7d4a065b**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode>
```

##### 3.1.3.20 DeleteMember

Deletes the user permission information.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can the ListNamespaces operation to obtain it. |

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| namespac e | Strin g | Path | Yes | default-namespace | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
|---|---|---|---|---|---|
| member | Strin g | Path | Yes | user:223769*** | The member UID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| errorCode | String | "" | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |
| errorMessage | String | "" | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
DELETE /gateway/v2/namespaces/[namespace]/members/[member] HTTP/1.1 &namespace=default-namespace &member=user:223769*** &Common request parameter
```

Sample success responses `JSON` format `{`

```json
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode>
```

##### 3.1.3.21 DeleteJob

Deletes information of non-running job instances from a job.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Syntax**

```
DELETE /api/v2/namespaces/[namespace]/jobs/[jobId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |

| jobId | Strin g | Path | Yes | 5af678c0-7db0-4650- 94c2-d2604f0a**** | The ID of the job instance. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| errorCode | String | "" | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |
| errorMessage | String | "" | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |
| httpCode | Integer | 200 | The value was fixed to 200. |

**Examples**

Sample requests

```
DELETE /api/v2/namespaces/[namespace]/jobs/[jobId] HTTP/1.1 &namespace=default-namespace &jobId=5af678c0-7db0-4650-94c2-d2604f0a**** &Common Request Parameter
```

Sample success responses `JSON` format `{`

```json
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode>
```

##### 3.1.3.22 DeleteDeployment

Deletes a deployed job by its ID.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Syntax**

```
DELETE /api/v2/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| deploymen tId | Strin g | Path | Yes | 5737ef81-d2f1-49cf- 8752-30910809**** | The job ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |

| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
|---|---|---|---|
| errorCode | String | "" | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |
| errorMessage | String | "" | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
DELETE /api/v2/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1 &namespace=default-namespace &deploymentId=5737ef81-d2f1-49cf-8752-30910809**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode>
```

##### 3.1.3.23 CreateVariable

Creates a variable.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Syntax**

```
POST /api/v2/namespaces/[namespace]/variables HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the project. |

|   | Parameter |   |   | Type |   | Position |   |   | Required |   | Example |   | Descriptio n |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | body |   |   |   |   |   |   |   |   |   | {'descript |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | {'descript |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ion': |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 'Created by |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | VVP2 SDK', |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 'kind': |   | The data |   |
|   |   |   |   |   |   |   |   |   |   |   | 'Encrypted', |   | content of the |   |
|   |   | body |   | string |   | wholebody |   |   | Yes |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 'name': |   | variable to |   |
|   |   |   |   |   |   |   |   |   |   |   | 'sls access _ _ |   | create. |   |
|   |   |   |   |   |   |   |   |   |   |   | id', |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 'value': |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 'dBRPSRR8Lbb |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ylhdZ'} |   |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | { "description": "Created by VVP2 SDK", "kind": "Encrypted", "name": "sls access id", _ _ "value": "dBRPSRR8Lb****" } | If success is false, the system returns a null value. If success is true, the system returns detailed data. |
| errorCode | String | "" | If success is false, this value is not empty and indicates the business error code. If success is true, this value is empty. |
| errorMessage | String | "" | If success is false, the system returns the business error message. If success is true, the system returns a null value. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Request example

```
POST /api/v2/namespaces/[namespace]/variables HTTP/1.1
```

`{`

```json
"namespace":"default-namespace", "body":"{'description': 'Created by VVP2 SDK', 'kind': 'Encrypted', 'name': 'sls_access_id', 'value': 'dBRPSRR8LbbylhdZ'}"
```

`}` Successful response example `JSON` format `{`

```json
 "data":"{    \"description\": \"Created by VVP2 SDK\",    \"kind\": \"Encrypted\",
\"name\": \"sls_access_id\", \"value\": \"dBRPSRR8Lb****\" }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;description&quot;: &quot;Created by VVP2 SDK&quot;,
    &quot;kind&quot;: &quot;Encrypted&quot;,
    &quot;name&quot;: &quot;sls_access_id&quot;,
    &quot;value&quot;: &quot;dBRPSRR8Lb****&quot;
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.24 CreateSavepoint

Creates a savepoint.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| body | Strin g | Body | No | { 'deploymentId': 'ee56beb9-2a99-4d87- 8633-63c****2', 'description': '', 'nativeFormat': False } | The parameters for triggering a savepoint. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| success | Boolean | true | Indicates whether the request is successful. |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| data | String | { "createdAt": 178305****, "deploymentId": "f9d616ef-4422- 42b5-b95c- f69****", "description": "", "jobId": "fa1b89ca- 908b-4cd5-b5b1- bb0ac****", "modifiedAt": 1783051217, "namespace": "flinkteam", "nativeFormat": false, "savepointId": "f1702682-c180- 4799-954a- e321****", "savepointLocation ": "oss://flink- full****", "savepointOrigin": "USER REQUEST", _ "status": { "state": "STARTED" }, "stopWithDrainEna bled": false } | If the value of success is false, a null value is returned. If the value of success is true, the detailed information is returned. |
| errorCode | String | "" | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |
| errorMessage | String | "" | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample requests

```
POST /api/v2/namespaces/[namespace]/savepoints HTTP/1.1
```

`{`

```json
"namespace":"default-namespace"
```

`}` Sample success responses `JSON` format `{`

```json
 "data":"{    \"createdAt\": 178305****,    \"deploymentId\": \"f9d616ef-4422-42b5-b95c
-f69****\", \"description\": \"\", \"jobId\": \"fa1b89ca-908b-4cd5-b5b1bb0ac****\", \"modifiedAt\": 1783051217, \"namespace\": \"flinkteam\", \"nativeFormat\": false, \"savepointId\": \"f1702682-c180-4799-954a-e321****\", \ "savepointLocation\": \"oss://flink-full****\", \"savepointOrigin\": \"USER_REQUEST\", \"status\": { \"state\": \"STARTED\" }, \"stopWithDrainEnabled\": false }", "success":true, "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****", "errorMessage":"", "errorCode":"", "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;createdAt&quot;: 178305****,
    &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f69****&quot;,
    &quot;description&quot;: &quot;&quot;,
    &quot;jobId&quot;: &quot;fa1b89ca-908b-4cd5-b5b1-bb0ac****&quot;,
    &quot;modifiedAt&quot;: 1783051217,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;nativeFormat&quot;: false,
    &quot;savepointId&quot;: &quot;f1702682-c180-4799-954a-e321****&quot;,
    &quot;savepointLocation&quot;: &quot;oss://flink-full****&quot;,
    &quot;savepointOrigin&quot;: &quot;USER_REQUEST&quot;,
    &quot;status&quot;: {
      &quot;state&quot;: &quot;STARTED&quot;
```

`},`

```xml
    &quot;stopWithDrainEnabled&quot;: false
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.25 CreateMember

Add a user to a project and grant the corresponding permissions.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Syntax**

```
POST /gateway/v2/namespaces/[namespace]/members HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the project. |

| Parameter | Type |   | Position |   |   | Required |   | Example |   | Descriptio n |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| body | string |   | wholebody |   |   |   |   | {'member': |   |   |   |
|   |   |   |   |   |   |   |   |   | {'member': |   |   |
|   |   |   |   |   |   |   |   | '2313667542* |   | The mapping |   |
|   |   |   |   |   |   |   |   |   |   | between the |   |
|   |   |   |   |   | ody | No |   |   |   |   |   |
|   |   |   |   |   |   |   |   | ***5', |   | member |   |
|   |   |   |   |   |   |   |   | 'role': |   | acco perm |   |
|   |   |   |   |   |   |   |   | 'EDITOR'} |   |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| data | String | { "member": "2313667542****", "role": "editor" } | If success is false, this parameter returns a null value. If success is true, this parameter returns detailed data. |
| errorCode | String | "" | If success is false, this value is not empty and represents the business error code. If success is true, this value is empty. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorMessage | String | "" | If success is false, this parameter returns the business error message. If success is true, this parameter returns a null value. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Request example

```
POST /gateway/v2/namespaces/[namespace]/members HTTP/1.1
```

`{`

```json
"namespace":"default-namespace"
```

`}` Successful response example `JSON` format `{`

```json
 "data":"{    \"member\": \"2313667542****\",    \"role\": \"editor\"  }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;member&quot;: &quot;2313667542****&quot;,
    &quot;role&quot;: &quot;editor&quot;
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.26 CreateDeployment

Create a deployed job.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Syntax**

```
POST /api/v2/namespaces/[namespace]/deployments HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the project. |

|   | Parameter |   |   | Type |   | Position |   |   | Required |   |   |   |   |   |   | Example |   |   |   | Descriptio n |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | {"artifact |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | {"artifact |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ": |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | {"kind":"SQL |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | SCRIPT","sql |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Artifact": |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | {"sqlScript" |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | :"CREATE |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | TEMPORARY |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | TABLE |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | (st |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | _ rname |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | VARCHAR) |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | with ( |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ' = |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 'datagen' |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ); |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | TEMPORARY |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | TABLE |   |   |   |   |   |

|   | Parameter |   |   |   | Type |   |   |   | Position |   |   |   |   | Required |   |   |   |   |   |   | xample |   | Descriptio n |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | E |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | e |   | kafka tabl |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | _ (strname |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | VARCHAR, |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | lens |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | BIGINT) |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ' = |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 'print' |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ); |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | INTO |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | kafka table _ |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The content |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | strname, |   |   |   |   |   |
|   | body |   |   |   | String |   |   |   | wholebody |   |   |   |   | Yes |   |   |   |   |   |   |   |   | of the |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | CAST |   |   |   | deployment. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | (CHAR LENGTH _ |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | (strname) |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | AS BIGINT) |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | AS lens |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | FROM |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ble; |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ymentTarget" |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | : |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | {"mode":"PER |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | JOB","name" _ |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | :"dt- |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | flinkteam"}, |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | "engineVersi |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | on":"vvr- |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 8.0.7- |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | flink- |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 1.17","execu |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | tionMode":"S |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | TREAMING","n |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ame":"sqlJob |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | "} |   |   |   |   |   |

| Parameter | Type | Position | Required |   |   | xample | Descriptio n |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   | E |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request succeeded. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
|   |   | { "artifact": { "kind": "SQLSCRIPT", "sqlArtifact": { "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens |   |

| Parameter | Type | FROM Example datahub table; _ | Description |
|---|---|---|---|
|   |   | " } }, "creator": "20877848***", "creatorName": "flinkadmin", "deploymentHasCh anged": true, "deploymentId": "f9d616ef-4422- 42b5-b95c-f***", "deploymentTarget ": { "mode": "PER JOB", _ "name": "dt- flinkteam" }, "engineVersion": |   |
| data | String | "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "flinkConf": { "execution.checkp ointing.interval": "180s", "table.exec.state.ttl ": "36 h", "restart- strategy.fixed- delay.delay": "10 s", "restart- strategy": "fixed- delay", "restart- strategy.fixed- delay.attempts": "21474****", "execution.checkp ointing.min-pause": "180s" }, "jobSummary": { "cancelled": 0, "cancelling": 0, "failed": 0, "finished": 0, "running": 0, "starting": 0 }, "logging": { "log4jLoggers": [ { "loggerLevel": "INFO", "loggerName": "" } ], "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "modifier": "2087784829****", "modifierName": "flinkadmin", "name": "sqlJob", "namespace": "flinkteam", "streamingResourc eSetting": { | If success is false, the system returns a null value. If success is true, the system returns detailed data. |

| Parameter | Type | "basicResourceSett Example ing": { | Description |
|---|---|---|---|
|   |   | "jobmanagerResou rceSettingSpec": { "cpu": 1.0, "memory": "4Gi" }, "parallelism": 1, "taskmanagerReso urceSettingSpec": { "cpu": 1.0, "memory": "4Gi" } }, "resourceSettingM ode": "BASIC" } } |   |
| errorCode | String | "" | If success is false, this parameter is not empty and indicates the business error code. If success is true, this parameter is empty. |
| errorMessage | String | "" | If success is false, the system returns the business error message. If success is true, the system returns a null value. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Request example

```
POST /api/v2/namespaces/[namespace]/deployments HTTP/1.1
```

`{`

```json
"namespace":"default-namespace", "body":"{"artifact":{"kind":"SQLSCRIPT","sqlArtifact":{"sqlScript":"CREATE TEMPORARY TA BLE `datahub_table` (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMP ORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT) with ( 'connector' = 'pri nt' ); INSERT INTO kafka_table SELECT strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens FROM datahub_table; "}},"deploymentTarget": {"mode":"PER_JOB","name":"dt-flinkteam"},"engineVersion":"vvr-8.0.7-flink- 1.17","executionMode":"STREAMING","name":"sqlJob"}"
```

`}` Successful response example `JSON` format `{`

```json
 "data":"{    \"artifact\": {      \"kind\": \"SQLSCRIPT\",      \"sqlArtifact\": {
\"sqlScript\": \"CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR)\with (\ 'c onnector' = 'datagen'\ );\\CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\ );\\INSERT INTO kafka_table\SELECT strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FROM\ datahub_table;\\" } }, \"creator\": \"20877848***\", \"creatorName\": \"flinkadmin\", \"deploymentHasChanged\": true, \"deploymentId\": \"f9d616ef-4422-42b5-b95c-f***\", \"deploymentTarget\": { \"mode\": \"PER_JOB\", \"name\": \"dt-flinkteam\" } , \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionMode\": \"STREAMING\", \"flinkConf\": { \"execution.checkpointing.interval\": \"180s\", \"table.exec.state.ttl\": \"36 h\", \"restart-strategy.fixed-delay.delay\": \"10 s \", \"restart-strategy\": \"fixed-delay\", \"restart-strategy.fixeddelay.attempts\": \"21474****\", \"execution.checkpointing.min-pause\": \"180s\" }, \"jobSummary\": { \"cancelled\": 0, \"cancelling\": 0, \"failed\": 0, \"finished\": 0, \"running\": 0, \"starting\": 0 }, \"logging\": { \"log4jLoggers\": [ { \"loggerLevel\": \"INFO\", \"loggerName\": \"\" } ], \"logReservePolicy\": { \"expirationDays\": 7, \"openHistory\": true }, \"loggingProfile\": \"d efault\" }, \"modifier\": \"2087784829****\", \"modifierName\": \"flinkadmin\", \"name\": \"sqlJob\", \"namespace\": \"flinkteam\", \"streamingResourceSetting\": { \"basicResourceSetting\": { \"jobmanagerResourceSettingSpec\": { \"cpu\": 1.0, \"memory\": \"4Gi\" }, \"parallelism\": 1, \"taskmanagerResourceSettingSpec\": { \"cp u\": 1.0, \"memory\": \"4Gi\" } }, \"resourceSettingMode\": \" BASIC\" } }",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<data>{
    &quot;artifact&quot;: {
      &quot;kind&quot;: &quot;SQLSCRIPT&quot;,
      &quot;sqlArtifact&quot;: {
        &quot;sqlScript&quot;: &quot;CREATE TEMPORARY TABLE `datahub_table` (strname VA
RCHAR)with ( &#x27;connector&#x27; = &#x27;datagen&#x27; );CREATE TEMPORARY TABLE ` kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27;connector&#x27; = &#x27;prin t&#x27; );INSERT INTO kafka_tableSELECT strname, CAST (CHAR_LENGTH (strname) AS BIGINT ) AS lensFROM datahub_table;&quot;
```

`}` `},`

```
    &quot;creator&quot;: &quot;20877848***&quot;,
    &quot;creatorName&quot;: &quot;flinkadmin&quot;,
    &quot;deploymentHasChanged&quot;: true,
    &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f***&quot;,
    &quot;deploymentTarget&quot;: {
      &quot;mode&quot;: &quot;PER_JOB&quot;,
      &quot;name&quot;: &quot;dt-flinkteam&quot;
```

`}` `},`

```
    &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
    &quot;executionMode&quot;: &quot;STREAMING&quot;,
    &quot;flinkConf&quot;: {
      &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
      &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
      &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;,
      &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
      &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;21474****&quot;,
      &quot;execution.checkpointing.min-pause&quot;: &quot;180s&quot;
```

`},`

```
    &quot;jobSummary&quot;: {
      &quot;cancelled&quot;: 0,
      &quot;cancelling&quot;: 0,
      &quot;failed&quot;: 0,
      &quot;finished&quot;: 0,
      &quot;running&quot;: 0,
      &quot;starting&quot;: 0
```

`},`

```
    &quot;logging&quot;: {
      &quot;log4jLoggers&quot;: [
```

`{`

```
          &quot;loggerLevel&quot;: &quot;INFO&quot;,
          &quot;loggerName&quot;: &quot;&quot;
```

`}` `],`

```
      &quot;logReservePolicy&quot;: {
        &quot;expirationDays&quot;: 7,
        &quot;openHistory&quot;: true
```

`},`

```
      &quot;loggingProfile&quot;: &quot;default&quot;
```

`},`

```
    &quot;modifier&quot;: &quot;2087784829****&quot;,
    &quot;modifierName&quot;: &quot;flinkadmin&quot;,
    &quot;name&quot;: &quot;sqlJob&quot;,
    &quot;namespace&quot;: &quot;flinkteam&quot;,
    &quot;streamingResourceSetting&quot;: {
      &quot;basicResourceSetting&quot;: {
        &quot;jobmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
```

`},`

```
        &quot;parallelism&quot;: 1,
        &quot;taskmanagerResourceSettingSpec&quot;: {
          &quot;cpu&quot;: 1.0,
          &quot;memory&quot;: &quot;4Gi&quot;
```

`}` `},`

```
      &quot;resourceSettingMode&quot;: &quot;BASIC&quot;
```

`}`

```xml
  }</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
<errorCode
```

`/>`

```xml
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.27 FlinkApiProxy

You can call this API through the Flink REST API to obtain information about session clusters or running jobs. Note that this API only retrieves information and does not allow you to manage or perform operations on session clusters and jobs.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Syntax**

```
GET /flink-ui/v2/proxy HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Query | Yes | default-namespace | The name of the project workspace. |
| resourceT ype | Strin g | Query | Yes | jobs | The resource type. Valid values: jobs sessionclusters |
| resourceId | Strin g | Query | Yes | c6f157ac-60b9-4b38- 8bad-d43**** | If the resource type is jobs, use the job ID. If the resource type is sessionclusters, use the session name. |
| flinkApiPat h | Strin g | Query | Yes | /jobs/4df35f8e54554b23 bf7dcd38a151**** | The Flink REST API path. For example, you can use /jobs/jobid/config to obtain the configuration of the specified job. For more information, see the Flink community REST API documentation. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | This parameter indicates whether the request succeeds. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The ID of the request. |
|   |   | {"jid":"65eb3696d b7d4a589851cda2 ****4","name":"1d bd6e8c-d493- 41d0-aa0f- 45972****1","isSto ppable":false,"stat e":"RUNNING","star t- time":178****394," end-time":- 1,"duration":22108 ,"maxParallelism":- 1,"now":178****50 2,"timestamps": {"CANCELLING":0," RECONCILING":0,"I NITIALIZING":1783 0****394,"CREATE D":17830****3,"RE STARTING":0,"RUN NING":1783****2,"F AILING":0,"CANCEL ED":0,"FINISHED":0 ,"SUSPENDED":0,"F AILED":0},"vertices ": [{"id":"717c7b8afe bbfb713****","nam e":"Source: datahub table[23] _ -> Calc[24] -> Sink: kafka table[25]"," _ maxParallelism":32 768,"parallelism":1 ,"status":"CREATED ","start-time":- 1,"end-time":- 1,"duration":- 1,"tasks": {"CREATED":0,"CA NCELING":0,"SCHE DULED":1,"CANCEL ED":0,"FAILED":0," RECONCILING":0,"I NITIALIZING":0,"FIN ISHED":0,"DEPLOYI NG":0,"RUNNING":0 },"metrics":{"read- bytes":0,"read- bytes- complete":false,"w rite- bytes":0,"write- |   |

| Parameter | Type | bytes- Example complete":false,"re | DeIfs tchrei pvatliuoen of success is false, the |
|---|---|---|---|
| data | String | ad- records":0,"read- records- complete":false,"w rite- records":0,"write- records- complete":false,"ac cumulated- backpressured- time":0,"accumulat ed-idle- time":0,"accumulat ed-busy- time":0.0}}],"statu s-counts": {"CREATED":1,"CA NCELING":0,"SCHE DULED":0,"CANCEL ED":0,"FAILED":0," RECONCILING":0,"I NITIALIZING":0,"FIN ISHED":0,"DEPLOYI NG":0,"RUNNING":0 },"plan": {"jid":"65eb3696d b7d4a589851cda2 6f252924","name": "1dbd6e8c-d493- 41d0-aa0f- 4597224738b1","ty pe":"STREAMING"," nodes": [{"id":"717c7b8afe bbfb713****eb2a9 4","parallelism":1," operator":"","opera tor strategy":"","de _ | system returns a null value. If the value of success is true, the system returns detailed data. |
|   |   | scription":" [23]:TableSourceSc an(table=[[vvp, default, datahub table]], _ fields=[strname]) +- [24]:Calc(select= [SUBSTRING(strna me, 0, 10) AS strname, CAST(CHAR LENGT _ H(strname) AS BIGINT) AS lens]) +- [25]:Sink(table= [vvp.default.kafka _ table], fields= [strname, lens]) ","optimizer proper _ ties":{}}]}} |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | If the value of success is false, this parameter is not empty and indicates the business error code. If the value of success is true, this parameter is empty. |
| errorMessage | String | "" | If the value of success is false, the system returns the business error message. If the value of success is true, the system returns a null value. |
| httpCode | Integer | 200 | The HTTP status code. |

**Examples**

Sample request

```
GET /flink-ui/v2/proxy HTTP/1.1 &namespace=default-namespace &resourceType=jobs &resourceId=c6f157ac-60b9-4b38-8bad-d43**** &flinkApiPath=/jobs/4df35f8e54554b23bf7dcd38a151**** &Common request parameters
```

Sample success response `JSON` format `{`

```json
 "data":"{\\\"jid\\\":\\\"65eb3696db7d4a589851cda2****4\\\",\\\"name\\\":\\\"1dbd6e8c-d
493-41d0-aa0f- 45972****1\\\",\\\"isStoppable\\\":false,\\\"state\\\":\\\"RUNNING\\\",\\\"start-time\\ \":178****394,\\\"end-time\\\":-1,\\\"duration\\\":22108,\\\"maxParallelism\\\":-1,\\\" now\\\":178****502,\\\"timestamps\\\": {\\\"CANCELLING\\\":0,\\\"RECONCILING\\\":0,\\\"INITIALIZING\\\":17830****394,\\\"CREATED \":17830****3,\\\"RESTARTING\\\":0,\\\"RUNNING\\\":1783****2,\\\"FAILING\\\":0,\\\"CANCEL \\\":0,\\\"FINISHED\\\":0,\\\"SUSPENDED\\\":0,\\\"FAILED\\\":0},\\\"vertices\\\":[{\\\" id\\\":\\\"717c7b8afebbfb713****\\\",\\\"name\\\":\\\"Source: datahub_table[23] -> Calc [24] -> Sink: kafka_table[25]\\\",\\\"maxParallelism\\\":32768,\\\"parallelism\\\":1,\\\"status\\\":\\\ REATED\\\",\\\"start-time\\\":-1,\\\"end-time\\\":-1,\\\"duration\\\":-1,\\\"tasks\\\": {\\\"CREATED\\\":0,\\\"CANCELING\\\":0,\\\"SCHEDULED\\\":1,\\\"CANCELED\\\":0,\\\"FAILED\ ":0,\\\"RECONCILING\\\":0,\\\"INITIALIZING\\\":0,\\\"FINISHED\\\":0,\\\"DEPLOYING\\\":0,\ "RUNNING\\\":0},\\\"metrics\\\":{\\\"read-bytes\\\":0,\\\"read-bytescomplete\\\":false,\\\"write-bytes\\\":0,\\\"write-bytes-complete\\\":false,\\\"read-re cords\\\":0,\\\"read-records-complete\\\":false,\\\"write-records\\\":0,\\\"write-recor ds-complete\\\":false,\\\"accumulated-backpressured-time\\\":0,\\\"accumulated-idle-tim e\\\":0,\\\"accumulated-busy-time\\\":0.0}}],\\\"status-counts\\\": {\\\"CREATED\\\":1,\\\"CANCELING\\\":0,\\\"SCHEDULED\\\":0,\\\"CANCELED\\\":0,\\\"FAILED\ ":0,\\\"RECONCILING\\\":0,\\\"INITIALIZING\\\":0,\\\"FINISHED\\\":0,\\\"DEPLOYING\\\":0,\ "RUNNING\\\":0},\\\"plan\\\": {\\\"jid\\\":\\\"65eb3696db7d4a589851cda26f252924\\\",\\\"name\\\":\\\"1dbd6e8c-d493-41 d0-aa0f-4597224738b1\\\",\\\"type\\\":\\\"STREAMING\\\",\\\"nodes\\\": [{\\\"id\\\":\\\"717c7b8afebbfb713****eb2a94\\\",\\\"parallelism\\\":1,\\\"operator\\\":\ "\\\",\\\"operator_strategy\\\":\\\"\\\",\\\"description\\\":\\\" [23]:TableSourceScan(table=[[vvp, default, datahub_table]], fields=[strname])<br/>+- [2 4]:Calc(select=[SUBSTRING(strname, 0, 10) AS strname, CAST(CHAR_LENGTH(strname) AS BIGI NT) AS lens])<br/> +- [25]:Sink(table=[vvp.default.kafka_table], fields=[strname, len s])<br/>\\\",\\\"optimizer_properties\\\":{}}]}}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<data> {\&quot;jid\&quot;:\&quot;65eb3696db7d4a589851cda2****4\&quot;,\&quot;name\&quot;:\&quot; bd6e8c-d493-41d0-aa0f- 45972****1\&quot;,\&quot;isStoppable\&quot;:false,\&quot;state\&quot;:\&quot;RUNNING\&quo ,\&quot;start-time\&quot;:178****394,\&quot;end-time\&quot;:- 1,\&quot;duration\&quot;:22108,\&quot;maxParallelism\&quot;:- 1,\&quot;now\&quot;:178****502,\&quot;timestamps\&quot;: {\&quot;CANCELLING\&quot;:0,\&quot;RECONCILING\&quot;:0,\&quot;INITIALIZING\&quot;:17830* *394,\&quot;CREATED\&quot;:17830****3,\&quot;RESTARTING\&quot;:0,\&quot;RUNNING\&quot;:17
****2,\&quot;FAILING\&quot;:0,\&quot;CANCELED\&quot;:0,\&quot;FINISHED\&quot;:0,\&quot;SU
ENDED\&quot;:0,\&quot;FAILED\&quot;:0},\&quot;vertices\&quot;: [{\&quot;id\&quot;:\&quot;717c7b8afebbfb713****\&quot;,\&quot;name\&quot;:\&quot;Source: datahub_table[23] -&gt; Calc[24] -&gt; Sink: kafka_table[25]\&quot;,\&quot;maxParallelism\&quot;:32768,\&quot;parallelism\&quot;:1,\&q t;status\&quot;:\&quot;CREATED\&quot;,\&quot;start-time\&quot;:-1,\&quot;end-time\&quot ;:-1,\&quot;duration\&quot;:-1,\&quot;tasks\&quot;: {\&quot;CREATED\&quot;:0,\&quot;CANCELING\&quot;:0,\&quot;SCHEDULED\&quot;:1,\&quot;CANCE D\&quot;:0,\&quot;FAILED\&quot;:0,\&quot;RECONCILING\&quot;:0,\&quot;INITIALIZING\&quot;: \&quot;FINISHED\&quot;:0,\&quot;DEPLOYING\&quot;:0,\&quot;RUNNING\&quot;:0},\&quot;metric &quot;:{\&quot;read-bytes\&quot;:0,\&quot;read-bytescomplete\&quot;:false,\&quot;write-bytes\&quot;:0,\&quot;write-bytescomplete\&quot;:false,\&quot;read-records\&quot;:0,\&quot;read-recordscomplete\&quot;:false,\&quot;write-records\&quot;:0,\&quot;write-recordscomplete\&quot;:false,\&quot;accumulated-backpressuredtime\&quot;:0,\&quot;accumulated-idle-time\&quot;:0,\&quot;accumulated-busy-time\&quot; :0.0}}],\&quot;status-counts\&quot;: {\&quot;CREATED\&quot;:1,\&quot;CANCELING\&quot;:0,\&quot;SCHEDULED\&quot;:0,\&quot;CANCE D\&quot;:0,\&quot;FAILED\&quot;:0,\&quot;RECONCILING\&quot;:0,\&quot;INITIALIZING\&quot;: \&quot;FINISHED\&quot;:0,\&quot;DEPLOYING\&quot;:0,\&quot;RUNNING\&quot;:0},\&quot;plan\& ot;: {\&quot;jid\&quot;:\&quot;65eb3696db7d4a589851cda26f252924\&quot;,\&quot;name\&quot;:\&qu ;1dbd6e8c-d493-41d0-aa0f- 4597224738b1\&quot;,\&quot;type\&quot;:\&quot;STREAMING\&quot;,\&quot;nodes\&quot;:[{\& quot;id\&quot;:\&quot;717c7b8afebbfb713****eb2a94\&quot;,\&quot;parallelism\&quot;:1,\&qu ;operator\&quot;:\&quot;\&quot;,\&quot;operator_strategy\&quot;:\&quot;\&quot;,\&quot;des iption\&quot;:\&quot;[23]:TableSourceScan(table=[[vvp, default, datahub_table]], fields =[strname])&lt;br/&gt;+- [24]:Calc(select=[SUBSTRING(strname, 0, 10) AS strname, CAST(C HAR_LENGTH(strname) AS BIGINT) AS lens])&lt;br/&gt; +- [25]:Sink(table= [vvp.default.kafka_table], fields=[strname, lens])&lt;br/&gt;\&quot;,\&quot;optimizer_properties\&quot;:{}}]}}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <errorMessage /> <errorCode /> <httpCode>200</httpCode>
```

##### 3.1.3.28 ListDeployments

List resource information for all deployments.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Syntax**

```
GET /api/v2/namespaces/[namespace]/deployments HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the project. |
| pageSize | Integ er | Query | No | 10 | The pagination parameter that specifies the number of items per page. Valid values: 1 to 100. Default value: 10. |
| pageIndex | Integ er | Query | No | 1 | The pagination parameter that specifies the page number. Minimum value: 1. Default value: 1. |
| name | Strin g | Query | No | test | The name of the deployment. |
| execution Mode | Strin g | Query | No | STREAMING | The execution mode of the deployment. Valid values: BATCH (batch job) STREAMING (streaming job) |
| status | Strin g | Query | No | FINISHED | The latest job status of the deployment. Valid values: CANCELLED (CANCELLED) FAILED (FAILED) RUNNING (RUNNING) TRANSITIONING (TRANSITIONING) FINISHED (FINISHED) |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| creator | Strin g | Query | No | 17915******4216 | The UID of the creator. |
| modifier | Strin g | Query | No | 170906468757**** | The UID of the modifier. |
| labelKey | Strin g | Query | No | key1 | The tag name. |
| labelValue Array | Strin g | Query | No | value1,value2 | The tag values. Separate multiple values with semicolons. |

| Parameter | Type | Position | Required | Example | Descriptio n |
|---|---|---|---|---|---|
| sortName | String | Query | No | gmt create _ | The sorting method. The system returns data in descending order of creation time and modification time. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | [ { "artifact": { "kind": "SQLSCRIPT" }, "creator": "2087784829****", "creatorName": "flinkadmin", "deploymentHasCh anged": true, "deploymentId": "f9d616ef-4422- 42b5-b95c- f691d4****", "deploymentTarget ": { "mode": "PER JOB", _ "name": "dt- flinkteam" }, "engineVersion": "vvr-8.0.7-flink- 1.17", "executionMode": "STREAMING", "flinkConf": { "execution.checkp ointing.interval": "180s", "table.exec.state.ttl ": "36 h", "restart- strategy.fixed- delay.delay": "10 s", "restart- strategy": "fixed- delay", "restart- strategy.fixed- delay.attempts": "21474****7", "execution.checkp ointing.min-pause": "180s" }, "jobSummary": { "cancelled": 0, "cancelling": 0, "failed": 0, "finished": 0, "running": 0, "starting": 0 }, "modifier": "208778482****5", "modifierName": "flinkadmin", "name": "sqlJob", "namespace": "flinkteam" } ] | If success is false, the system returns a null value. If success is true, the system returns detailed data. |
| errorCode | String | "" | If success is false, this parameter is not empty and indicates the business error code. If success is true, this parameter is empty. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorMessage | String | "" | If success is false, the system returns the business error message. If success is true, the system returns a null value. |
| httpCode | Integer | 200 | The HTTP status code. |
| totalSize | Integer | 1 | The total number of entries. |

**Examples**

Sample requests

```
GET /api/v2/namespaces/[namespace]/deployments HTTP/1.1 &namespace=default-namespace &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "totalSize":1,
 "data":"[    {      \"artifact\": {        \"kind\": \"SQLSCRIPT\"      },
\"creator\": \"2087784829****\", \"creatorName\": \"flinkadmin\", \"deploymentHasChanged\": true, \"deploymentId\": \"f9d616ef-4422-42b5-b95c-f691d4
****\",      \"deploymentTarget\": {        \"mode\": \"PER_JOB\",        \"name\": \"dt
-flinkteam\" }, \"engineVersion\": \"vvr-8.0.7-flink-1.17\", \"executionM ode\": \"STREAMING\", \"flinkConf\": { \"execution.checkpointing.interval\": \"180s\", \"table.exec.state.ttl\": \"36 h \", \"restart-strategy.fixed-delay.delay\": \"10 s\", \"restart-strategy\" : \"fixed-delay\", \"restart-strategy.fixed-delay.attempts\": \"21474****7\", \"execution.checkpointing.min-pause\": \"180s\" }, \"jobSummary\": { \" cancelled\": 0, \"cancelling\": 0, \"failed\": 0, \"finished\": 0, \"running\": 0, \"starting\": 0 }, \"modifier\": \"208778482****5\", \"modifierName\": \"flinkadmin\", \"name\": \"sqlJob\", \"namespace\": \"flinkteam\" } ]",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "httpCode":200
```

`}` `XML` format

```xml
<totalSize>1</totalSize> <data>[
```

`{`

```
      &quot;artifact&quot;: {
        &quot;kind&quot;: &quot;SQLSCRIPT&quot;
```

`},`

```
      &quot;creator&quot;: &quot;2087784829****&quot;,
      &quot;creatorName&quot;: &quot;flinkadmin&quot;,
      &quot;deploymentHasChanged&quot;: true,
      &quot;deploymentId&quot;: &quot;f9d616ef-4422-42b5-b95c-f691d4****&quot;,
      &quot;deploymentTarget&quot;: {
        &quot;mode&quot;: &quot;PER_JOB&quot;,
        &quot;name&quot;: &quot;dt-flinkteam&quot;
```

`},`

```
      &quot;engineVersion&quot;: &quot;vvr-8.0.7-flink-1.17&quot;,
      &quot;executionMode&quot;: &quot;STREAMING&quot;,
      &quot;flinkConf&quot;: {
        &quot;execution.checkpointing.interval&quot;: &quot;180s&quot;,
        &quot;table.exec.state.ttl&quot;: &quot;36 h&quot;,
        &quot;restart-strategy.fixed-delay.delay&quot;: &quot;10 s&quot;,
        &quot;restart-strategy&quot;: &quot;fixed-delay&quot;,
        &quot;restart-strategy.fixed-delay.attempts&quot;: &quot;21474****7&quot;,
        &quot;execution.checkpointing.min-pause&quot;: &quot;180s&quot;
```

`},`

```
      &quot;jobSummary&quot;: {
        &quot;cancelled&quot;: 0,
        &quot;cancelling&quot;: 0,
        &quot;failed&quot;: 0,
        &quot;finished&quot;: 0,
        &quot;running&quot;: 0,
        &quot;starting&quot;: 0
```

`},`

```
      &quot;modifier&quot;: &quot;208778482****5&quot;,
      &quot;modifierName&quot;: &quot;flinkadmin&quot;,
      &quot;name&quot;: &quot;sqlJob&quot;,
      &quot;namespace&quot;: &quot;flinkteam&quot;
```

`}`

```xml
  ]</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.29 ListMembers

Views the mapping between user UIDs and authorization in a namespace.

**Request headers**

| > Document V | ersion: 2 | 026082 | 8 |   | 34 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| workspace | Strin g | Hea der | Yes | a14bd5d90a**** | The ID of the workspace where the job resides. You can call the ListNamespaces operation to obtain it. |

**Syntax**

```
GET /gateway/v2/namespaces/[namespace]/members HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the namespace where the job resides. You can call the ListNamespaces operation to obtain it. |
| pageIndex | Integ er | Quer y | No | 1 | The page number. Default value: 1. |
| pageSize | Integ er | Quer y | No | 10 | The number of entries per page. Maximum value: 100. Default value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |

| data | String | [ { "member": "19326829721009 78", "role": "owner" }, { "member": "20877848297216 2995", "role": "owner" } ] | If the value of success is false, a null value is returned. If the value of success is true, the detailed information is returned. |
|---|---|---|---|
| errorCode | String | "" | If the value of success is false, an error code is returned. If the value of success is true, a null value is returned. |
| errorMessage | String | "" | If the value of success is false, an error message is returned. If the value of success is true, a null value is returned. |
| httpCode | Integer | 200 | The HTTP status code. |
| totalSize | Integer | 1 | The total number of entries. |

**Examples**

Sample requests

```
GET /gateway/v2/namespaces/[namespace]/members HTTP/1.1 &namespace=default-namespace &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "totalSize":1,
 "data":"[    {      \"member\": \"1932682972100978\",      \"role\": \"owner\"    },
{ \"member\": \"208778482972162995\", \"role\": \"owner\" } ]", "success":true, "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****", "errorMessage":"", "errorCode":"", "httpCode":200
```

`}` `XML` format

```xml
<totalSize>1</totalSize> <data>[
```

`{`

```
      &quot;member&quot;: &quot;1932682972100978&quot;,
      &quot;role&quot;: &quot;owner&quot;
```

`},` `{`

```
      &quot;member&quot;: &quot;208778482972162995&quot;,
      &quot;role&quot;: &quot;owner&quot;
```

`}`

```xml
  ]</data>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <httpCode>200</httpCode>
```

##### 3.1.3.30 ListVariables

Get the variable list.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| workspac e | Strin g | Header | Yes | a14bd5d90a**** | The ID of the workspace. |

**Syntax**

```
GET /api/v2/namespaces/[namespace]/variables HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| namespac e | Strin g | Path | Yes | default-namespace | The name of the project. |
| pageSize | Integ er | Query | No | 10 | The pagination parameter that specifies the number of elements on the requested page. The maximum value is 100, the minimum value is 1, and the default value is 10. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | No | 1 | The pagination parameter for the page index that specifies the requested page number. The minimum value is 1, and the default value is 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | The request ID. |
| data | String | [ { "description": "Created by VVP2 SDK", "kind": "Encrypted", "name": "sls access id", _ _ "value": "******" } ] | If success is false, the system returns a null value. If success is true, the system returns detailed data. |
| errorCode | String | "" | If success is false, this value is not empty and indicates the business error code. If success is true, this value is empty. |
| errorMessage | String | "" | If success is false, the system returns the business error message. If success is true, the system returns a null value. |
| httpCode | Integer | 200 | The HTTP status code. |
| totalSize | Integer | 1 | The total number of entries. |
| pageIndex | Integer | 1 | The pagination parameter for the page index that specifies the requested page number. |
| pageSize | Integer | 10 | The pagination parameter that specifies the number of elements on the requested page. |

**Examples**

Sample requests

```
GET /api/v2/namespaces/[namespace]/variables HTTP/1.1 &namespace=default-namespace &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "totalSize":1,
 "data":"[    {      \"description\": \"Created by VVP2 SDK\",      \"kind\":
\"Encrypted\", \"name\": \"sls_access_id\", \"value\": \"******\" } ]",
 "pageIndex":1,
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "errorMessage":"",
 "errorCode":"",
 "pageSize":10,
 "httpCode":200
```

`}` `XML` format

```xml
<totalSize>1</totalSize> <data>[
```

`{`

```
      &quot;description&quot;: &quot;Created by VVP2 SDK&quot;,
      &quot;kind&quot;: &quot;Encrypted&quot;,
      &quot;name&quot;: &quot;sls_access_id&quot;,
      &quot;value&quot;: &quot;******&quot;
```

`}`

```xml
  ]</data>
 <pageIndex>1</pageIndex>
 <success>true</success>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <errorMessage  />
 <errorCode  />
 <pageSize>10</pageSize>
 <httpCode>200</httpCode>
```

### 3.2 API examples

#### 3.2.1 Examples

This topic describes API examples.

**Notes**

You must parse all interfaces that returns Resp by using a fixed method. All PUT and POST requests must include the content-type header and use the built-in JsonUtil for serialization.

**Sample code**

```java
package sample; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.http.FormatType; import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.profile.IClientProfile; import com.aliyuncs.ververica.model.v20200501.*; import com.fasterxml.jackson.core.JsonProcessingException; import com.fasterxml.jackson.core.type.TypeReference; import com.ververica.common.model.ResultModel; import com.ververica.common.model.deployment.Artifact; import com.ververica.common.model.deployment.Deployment; import com.ververica.common.model.deployment.DeploymentState; import com.ververica.common.model.namespace.Namespace; import com.ververica.common.params.*; import com.ververica.common.resp.*; import com.ververica.common.util.JsonUtil; import com.ververica.common.util.SdkUtil; import java.util.List; public class SdkSample {
    /**
     * Normal format:
     * {
     * "requestId":"202008030937-4TFJR5MK2R",
     * "success": true, # When this value is true, the result shows only requestId. Whe
n false, it throws reason and message.
     * "message": "",
     * "reason": "",
     * "data": Data content (Object)
     * }
```

`*/`

```
    public static void main(String[] args) throws JsonProcessingException,
ClientException {
        String regionId = "cn-hangzhou";
        DefaultProfile.addEndpoint(regionId, "ververica", "ververica-
share.aliyuncs.com");
        IClientProfile profile = DefaultProfile.getProfile(regionId, "**************",
"****************");
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
//namespace/deploymentIddependsonactualenvironmentjobconfiguration.
```

```java
        // namespace/deploymentId depends on actual environment job configuration.
        // Get list of namespaces.
        ListNamespacesRequest listNamespacesRequest = new ListNamespacesRequest();
        listNamespacesRequest.setSysVersion("2024-11-18");
        ResultModel<ListNamespacesResp> listNamespacesRespResultModel =
JsonUtil.toBean(SdkUtil.getHttpContentString(client,
                listNamespacesRequest), new
TypeReference<ResultModel<ListNamespacesResp>>() {
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
        ResultModel<GetDeploymentResp> getDeploymentRespResultModel =
JsonUtil.toBean(data, new TypeReference<ResultModel<GetDeploymentResp>>() {
        });
        Deployment deployment = getDeploymentRespResultModel.getData();
        deployment.getMetadata().getAnnotations().put("update-flag", "zdbox");
        deployment.getMetadata().getLabels().put("key2", "value2");
        deployment.getSpec().setState(DeploymentState.RUNNING);
        // Update deployment state.
        UpdateDeploymentDesiredStateParams updateDeploymentDesiredStateParams = new Upd
ateDeploymentDesiredStateParams();
        updateDeploymentDesiredStateParams.setState(DeploymentState.CANCELLED);
        UpdateDeploymentDesiredStateRequest
                updateDeploymentDesiredStateRequest = new
UpdateDeploymentDesiredStateRequest();
        updateDeploymentDesiredStateRequest.setWorkspace(workspaceName);
        updateDeploymentDesiredStateRequest.setNamespace(namespace);
        updateDeploymentDesiredStateRequest.setDeploymentId(deploymentId);
updateDeploymentDesiredStateRequest.setParamsJson(JsonUtil.toJson(updateDeploymentDesired ateParams));
        updateDeploymentDesiredStateRequest.setHttpContentType(FormatType.JSON);
        updateDeploymentDesiredStateRequest.setSysVersion("2024-11-18");
System.out.println(client.doAction(updateDeploymentDesiredStateRequest).getHttpContentStr g());
        ResultModel<UpdateDeploymentDesiredStateResp>
                updateDeploymentDesiredStateRespResultModel =
JsonUtil.toBean(client.doAction(updateDeploymentDesiredStateRequest).getHttpContentString
```

`,`

```java
                        new TypeReference<ResultModel<UpdateDeploymentDesiredStateResp>>
() {
                        });
System.out.println(JsonUtil.toJson(updateDeploymentDesiredStateRespResultModel));
        // Create savepoint: If data is empty, the trigger failed. Check the message.
        /**
         * Success includes data field with return data: {"data":{"metadata":
{"createdAt":"2020-08-18T07:04:40.379926Z","jobId":"d0d6720f-00ac-47cc-8d54- 7d88a4d7b446","modifiedAt":"2020-08-18T07:04:40.379926Z","deploymentId":"0cb796fc-2641- 488e-bde8- 52b2199c5747","origin":"USER_REQUEST","resourceVersion":1,"namespace":"test","annotations {"com.dataartisans.appmanager.controller.deployment.spec.version":"4"},"id":"c4e40dc9-6 9c7-4ba0-8add-5f862ecb00ef"},"apiVersion":"v1","kind":"Savepoint","spec": {"savepointLocation":"oss://qiqi-zp/vvp/flinksavepoints/namespaces/test/deployments/0cb796fc-2641-488e-bde8-52b2199c5747/c4e40dc9-69 c7-4ba0-8add-5f862ecb00ef"},"status":{"state":"STARTED"}},"requestId":"188B1FFC-2729-45 8E-A404-D3CD5D972DA0"}
         * Failure has no data field and includes a message: {"RequestId":"B545121D-ED4
C-4E71-9D76-CBD510A04E5B","HostId":"ververica-share.cnshanghai.aliyuncs.com","Code":"BadRequest","Message":"No active job for a deployment."}
```

`*/`

```java
        CreateSavepointRequest
                createSavepointRequest = new CreateSavepointRequest();
        createSavepointRequest.setWorkspace(workspaceName);
        createSavepointRequest.setNamespace(namespace);
        CreateSavepointParams createSavepointParams
                = new CreateSavepointParams();
        createSavepointParams.setDeploymentId(deploymentId);
        createSavepointRequest.setParamsJson(JsonUtil.toJson(createSavepointParams));
        createSavepointRequest.setHttpContentType(FormatType.JSON);
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
JsonUtil.toBean(client.doAction(listSavepointsRequest).getHttpContentString(), new Type Reference<ResultModel<ListSavepointsResp>>() {
```

```java
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
                JsonUtil.toBean(client.doAction(listJobsRequest).getHttpContentString(),
new TypeReference<ResultModel<ListJobsResp>>() {
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
'VALIDATION_RESULT_VALID_INSERT_QUERY' or 'VALIDATION_RESULT_VALID_DDL_STATEMENT'. Othe rwise, check errorDetails.
        ValidateSqlScriptRequest
                validateSqlScriptRequest = new ValidateSqlScriptRequest();
        validateSqlScriptRequest.setWorkspace(workspaceName);
        validateSqlScriptRequest.setNamespace(namespace);
        ValidateSqlScriptParams
                validateSqlScriptParams = new ValidateSqlScriptParams();
        validateSqlScriptParams.setStatement("CREATE TABLE RANDOM_TABLE(`name` STRING)
with ('connector'='random','type'='random')"); validateSqlScriptRequest.setParamsJson(JsonUtil.toJson(validateSqlScriptParams));
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
```

```java
        ExecuteSqlScriptRequest
                executeSqlScriptRequest = new ExecuteSqlScriptRequest();
        executeSqlScriptRequest.setWorkspace(workspaceName);
        executeSqlScriptRequest.setNamespace(namespace);
        ExecuteSqlScriptParams executeSqlScriptParams
                = new
                ExecuteSqlScriptParams();
        executeSqlScriptParams.setStatement("create table abaaaa (a varchar) with
('connector' = 'random', 'type' = 'random');");
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
System.out.println(client.doAction(getGlobalDeploymentDefaultsRequest).getHttpContentStri ());
        getGlobalDeploymentDefaultsRequest.setSysVersion("2024-11-18");
        ResultModel<GetGlobalDeploymentDefaultsResp> globalDefaults =
JsonUtil.toBean(client.doAction(getGlobalDeploymentDefaultsRequest).getHttpContentString(
                        new TypeReference<ResultModel<GetGlobalDeploymentDefaultsResp>>(
) {
                        });
        System.out.println(JsonUtil.toJson(globalDefaults.getData()));
        Deployment.DeploymentSpec spec =
                globalDefaults.getData().getSpec();
        spec.setState(DeploymentState.RUNNING);
        // SQL job.
        Artifact.SqlScriptArtifact
                sqlScriptArtifact = new
                Artifact.SqlScriptArtifact();
        sqlScriptArtifact.setSqlScript("INSERT INTO PRINT_TABLE SELECT /* comments */ U
PPER(name) FROM RANDOM_TABLE");
        spec.getTemplate().getSpec().setArtifact(sqlScriptArtifact);
        // To create a DataStream job, pass a different Artifact.
        Artifact.JarArtifact jarArtifact = new
                Artifact.JarArtifact();
        jarArtifact.setJarUri("oss://qiqi-zp/multioss/artifacts/namespaces/test/job-1.0
-SNAPSHOT2.jar"); //specgetTemplate()getSpec()setArtifact(jarArtifact)
```

```java
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
JsonUtil.toBean(client.doAction(listArtifactsRequest).getHttpContentString(), new TypeR eference<ResultModel<ListArtifactsResp>>() {
                });
        System.out.println(JsonUtil.toJson(artifacts));
        // Get artifact.
        GetArtifactMetadataRequest
                getArtifactMetadataRequest = new GetArtifactMetadataRequest();
        getArtifactMetadataRequest.setWorkspace(workspaceName);
        getArtifactMetadataRequest.setNamespace(namespace);
        getArtifactMetadataRequest.setFilename("flip-75-demo-1.0-SNAPSHOT-1.jar");
        getArtifactMetadataRequest.setSysVersion("2024-11-18");
System.out.println(client.doAction(getArtifactMetadataRequest).getHttpContentString());
        ResultModel<GetArtifactMetadataResp> artifact =
JsonUtil.toBean(client.doAction(getArtifactMetadataRequest).getHttpContentString(),
                        new TypeReference<ResultModel<GetArtifactMetadataResp>>() {
                        });
Systemoutprintln(JsonUtiltoJson(artifact));
```

```java
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
        // Delete deployment. Specify an existing DeploymentId whose state is
CANCELLED.
        DeleteDeploymentRequest
                deleteDeploymentRequest = new DeleteDeploymentRequest();
        deleteDeploymentRequest.setWorkspace(workspaceName);
        deleteDeploymentRequest.setNamespace(namespace);
        deleteDeploymentRequest.setDeploymentId(deploymentId);
        deleteDeploymentRequest.setSysVersion("2024-11-18");
        DeleteDeploymentResponse
                deleteDeploymentResponse =
client.getAcsResponse(deleteDeploymentRequest);
        System.out.println(JsonUtil.toJson(deleteDeploymentResponse));
```

`}` `}`

> **Note:** For detailed sample code, contact Alibaba Cloud technical support.

#### 3.2.2 pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?> <project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
<groupId>comaliyun</groupId>
```

```xml
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

If your business logic is complex and you need to write nested statements in DML statements, it can be difficult to locate problems. To simplify the development process, you can define a data view and write nested statements to the data view. QL reference

> **Note:** A data view displays a logical table that describes the computing logic without storing physical data.

**Syntax**

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

Realtime Compute performs window aggregation on data based on time attributes. In jobs that use window functions with Event Time, you must declare the Watermark method in the data source table. WATERMARK defines the event time attribute of a table. Its syntax is WATERMARK FOR rowtime_column_name AS watermark_strategy_expression. The rowtime_column_name parameter designates an existing column as the event time marker for the table. This column must be of the TIMESTAMP(3) type, reside at the top level of the schema, and may also be a computed column. QL reference The watermark_strategy_expression parameter defines the strategy for generating watermarks. It allows any non-query expression—including computed columns—to calculate the watermark. The return type of the expression must be TIMESTAMP(3), representing elapsed time since the Epoch. The system emits a watermark only if it is non-null and greater than the previously emitted local watermark (to ensure monotonic increase). The framework computes the watermark generation expression for every record. Periodically, the framework emits the largest watermark generated, provided it differs from the last emitted watermark, is not null, and exceeds the last emitted watermark. Watermarks emit at intervals configured by pipeline.auto-watermark-interval. If the interval is 0 ms, the system generates a watermark for every record and emits it when it is not null and greater than the last emitted watermark. When you use event time semantics, the table must include an event time attribute and a watermark strategy. Flink provides several common watermark strategies: Strictly ascending timestamps: WATERMARK FOR rowtime_column AS rowtime_column. The system emits a watermark equal to the maximum timestamp observed so far. Rows with timestamps greater than this maximum are not considered late. Ascending timestamps: WATERMARK FOR rowtime_column AS rowtime_column - INTERVAL '0.001' SECOND. The system emits a watermark equal to the maximum timestamp observed so far minus one millisecond. Rows with timestamps greater than or equal to this maximum are not considered late. Bounded-out-of-order timestamps: WATERMARK FOR rowtime_column AS rowtime_column - INTERVAL 'string' timeUnit. The system emits a watermark equal to the maximum timestamp observed so far minus a specified delay. For example, WATERMARK FOR rowtime_column AS rowtime_column - INTERVAL '5' SECOND implements a 5-second delay watermark strategy.

```
CREATE TABLE Orders (
 user BIGINT,
 product STRING,
 order_time TIMESTAMP(3),
 WATERMARK FOR order_time AS order_time -INTERVAL '5' SECOND
) WITH ( . . . );
```

**Summary of watermark usage**

A watermark means all events with timestamps `t'< t` have already occurred. If a

| k | t |   |
|---|---|---|
| t |   |   |
|   |   | ( |

watermark `t` takes effect, the system discards all subsequent records with Event Time less than `t` (currently, Realtime Compute discards these late-arriving data; future versions will support user configuration to allow updates from later data). For out-of-order streams, watermarks are critical. Even if some events arrive late, they do not excessively compromise the accuracy of window computations. QL reference In parallel data streams, when an operator has multiple input streams, the operator uses the minimum Event Time among all input streams as its Event Time.

#### 4.4.2 Computed column

A computed column uses data from other columns to calculate the value for its own column. If your source table does not contain a column of the TIMESTAMP type, you can use a computed column to convert data from fields of other types.

**Concept of computed columns**

A computed column is a virtual column and is not physically stored in a table. You can use expressions, built-in functions, or user-defined functions to calculate the value of a computed column based on data from other columns. In Flink SQL, you can use computed columns as ordinary fields.

**Use cases of computed columns**

Currently, the Event Time (also known as rowtime) column for Watermark supports only the TIMESTAMP type (supporting the LONG type in the future). You can define a watermark only in the DDL statement of a source table. If no column of the TIMESTAMP type exists in your source table, you can use a computed column to convert data from fields of other types.

**Syntax of computed columns**

```
column_name AS computed_column_expression
```

**Examples of computed columns**

The rowtime field for a watermark must be of the TIMESTAMP data type. Realtime Compute for Apache Flink currently supports the TIMESTAMP data type with millisecond precision, which corresponds to a 13-digit Unix timestamp. If the TIME field in DataHub is at microsecond precision (16-digit Unix timestamp), you can use a computed column to convert it into a 13-digit timestamp, as shown in the following example. QL reference

```
CREATE TABLE test_stream(
  a INT,
  b BIGINT,
  `TIME` BIGINT,
  ts AS TO_TIMESTAMP(TIME/1000), -- Use a computed column to convert a 16-digit timesta
mp into a 13-digit timestamp.
  WATERMARK FOR ts AS WITHOFFSET(ts, 1000)
) WITH (
  'connector' = 'datahub',
  ...
```

); In the preceding example, the `TIME` field in the source table contains time information and is of the BIGINT type. The system uses the computed column feature to convert the `TIME` field into the `ts` field of the TIMESTAMP type, and then uses the `ts` field as the rowtime field for the watermark.

#### 4.4.3 Time attribute

This topic introduces the Event Time and Processing Time data types that Flink SQL supports. Flink SQL supports two time types: Event Time and Processing Time. Event Time: The event time you provide (usually the original creation time of the data). Event Time must be data you provide in the schema. Processing Time: The local system time when the system processes the event. The following figure shows the positions of different time attributes in the real-time computing process. Based on the definitions in the preceding figure, Ingestion Time and Processing Time are time attributes that the system adds to streaming records. You cannot control them. Event Time is a time attribute carried by the streaming record itself. Due to data disorder, network jitter, or other reasons, a record with Event Time of t1 (corresponding to partition1) may be processed by Flink later than a record with Event Time of t2 (corresponding to partition2), where t2 > t1.

**Event Time**

Event Time is also called rowtime. You must declare the Event Time attribute in the DDL of the source table. You can declare a field in the source table as Event Time. Currently, only a field of the TIMESTAMP type (supporting LONG type in the future) can be declared as a rowtime field. If the field is not of the TIMESTAMP type, you must use a Computed column to construct a TIMESTAMP-type column based on an existing column. QL reference However, data may arrive out of sequence due to data disorder, network jitter or other reasons, so you must explicitly define a Watermark calculation method when defining a rowtime field. The following example shows how to use a window function to aggregate data based on Event Time.

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

The following example shows how to use a window function to aggregate data based on Processing Time. QL reference

```
CREATE TABLE mq_stream (
  a VARCHAR,
  b VARCHAR,
  c BIGINT,
  d AS PROCTIME()   ---Explicitly define a Processing Time column in the declaration of
the source table. ) WITH (
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

Currently, a time attribute field loses its time attribute after either of the following two operations: Non-window GROUP BY Join of two streams If you continue to use the time attribute field for window function operations after either of these operations, an error similar to `org.apache.flink.table.api.ValidationException:`

```
Window can only be defined over a time attribute column. occurs.
```

### 4.5 Subscription

The subscription billing method allows you to use resources only after you pay for the resources. You must make a payment based on the subscription duration when you purchase resources. This billing method is suitable for long-term stable business for which the resource usage cycle can be estimated. This topic describes the billing rules, billing cycles, and unit prices in different regions of the subscription billing method. QL reference

| Item | Description |
|---|---|
| Billing rule | For more information about the unit prices in different regions, seeU nit prices in different regions. Important The subscription duration in the formula is measured in months. You can view the fees on the buy page. The number of compute units (CUs) consumed for management is fixed to 2. For example, the unit prices of management resources and computing resources are both USD 45.94 per CU per month. If you want to create a workspace that uses 8 CUs as computing resources and set the subscription duration to three months, the fee for creating the workspace in the Intel X86 architecture is USD 1378.2, which is calculated by using the following formula: Fee for management resources + Fee for computing resources = 2 CUs × USD 45.94 per CU per month × 3 months + 8 CUs × USD 45.94 per CU per month × 3 months = USD 275.64 + USD 1102.56 = USD 1378.2. |
| Billing cycle | The billing cycle (based on UTC+8:00) of a subscription workspace is the subscription duration of the workspace. The billing cycle starts from the time (accurate to the second) when the subscription workspace is activated or renewed and ends at 00:00:00 the next day after the expiration date. |
| Resource changes for an expired subscription instance | The impact on your business varies based on the time period after the subscription workspace expires. For more information, see Resource availability for an expired subscription. |
| Renewal | If you want to continue using a subscription workspace after it expires, you can renew the workspace. For more information, see Renewals. Note If you do not renew your workspace at the earliest opportunity, your workspace is released after it expires. To ensure service continuity, we recommend that you renew your workspace at the earliest opportunity. For more information about the resource changes for an expired subscription workspace, see Resource availability for an expired subscription. If your account has overdue payments, your workspace cannot be automatically renewed. Top up your account and manually renew the workspace. |

QL reference

| Refund | You make a payment based on the subscription duration when you purchase a subscription workspace. If you no longer require the workspace due to changes in business requirements, you can submit a ticket to unsubscribe from the workspace and apply for a refund. For more information about the operations and rules, see Refund policy. |
|---|---|
| Resource scaling | After you create a subscription workspace, you can modify the resource configurations of your workspace to scale the workspace. For more information, see Reconfigure resources. |

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

Unit prices of computing resources of a namespace in the Intel X86 architecture QL reference

| Region | Unit price in a single zone (USD per CU per month) | Unit price across zones (USD per CU per month) |
|---|---|---|
| Singapore | 45.94 | Cross-zone high availability not supported |
| Japan (Tokyo) | 50.95 |   |
| Germany (Frankfurt) | 48.40 |   |
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

QL reference A subscription workspace has a validity period based on the subscription duration that you specify when you purchase the workspace. After the subscription duration of a subscription workspace ends, you can no longer use the workspace. If you do not renew the workspace within a specified period of time, the workspace is automatically released. The following figure shows the resource changes for an expired workspace and related operations. Manual renewal or autorenewal to extend the validity period of the The service cannot service be restored. You must reactivate the service. Service in Service More than 15 Resources Service Within 15 days days after after expiration use expired suspended released expiration Service

| Payment status |   | Suspension policy | Solution |
|---|---|---|---|
| Before the workspace expires |   | The system sends notifications to you by email or text message. | Renew the workspace. After the renewal is successful, you can continue using the workspace. For more information, see Renewals. |
| After the workspac e expires | Within 15 days after the workspace expires | You cannot access the workspace. The deployments that are running in the workspace stop running. | Renew the workspace. After the renewal is successful, you can continue using the workspace. For more information, see Renewals. |
|   | 15 days after the workspace expires | The workspace is automatically released. The deployment data of the workspace is deleted and cannot be restored. Note Resources such as the JAR packages that you upload are not deleted and are stored in your Object Storage Service (OSS) buckets. | You cannot restore the instance. |

**References**

QL reference For more information about how to change the billing method of a workspace from subscription to pay-as-you-go, see Switch from subscription to pay-as-you-go. For more information about how to create a workspace, see Activate Realtime Compute for Apache Flink.

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

); Result table

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

); Result table B QL reference

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

### 4.6 Query statements

This topic describes the query statements provided by Flink. For more information about the query statements provided by Apache Flink 1.11, visit Queries.

### 4.7 Window functions

This topic describes the window functions, time attributes, and window types supported by Flink SQL.

**Window functions**

Flink SQL supports aggregation over infinite windows. You do not need to explicitly define windows in SQL statements. Flink SQL also supports aggregation over a specific window. For example, if you want to count the number of users who clicked a URL in the previous minute, you can define a window to collect data about user clicks in the previous minute. Then, you can compute the data in the window to obtain the result. Flink SQL supports window aggregates and over aggregates. This topic describes window aggregates. Window aggregates support the windows that are defined based on the following time attributes: event time and processing time. The TUMBLE, HOP, and SESSION window functions are supported for each time attribute.

> **Warning:** The TUMBLE, HOP, and SESSION functions cannot be used with the LAST_VALUE, FIRST_VALUE, or TopN function. If you use these window functions with the LAST_VALUE, FIRST_VALUE, or TopN function, the data becomes out of order and is discarded. As a result, the output data is abnormal.

QL reference

**Time attributes**

Flink SQL supports two time attributes: event time and processing time. For more information about time attributes, see Time attributes. Flink aggregates data in windows based on the time attributes. The windowing method varies based on the time attributes. Event time: the event time that you provide in the data store. The system closes a window based on the watermark that is generated based on the event time of the data. A window ends only when the value of the watermark is later than the time when the window closes. The output data is generated when the window ends. The window generates output data only if the data that triggers the window to end flows into Flink. The watermark value for a single subtask increments. If multiple subtasks run or multiple source tables exist, the minimum watermark value is used.

> **Important:** If an out-of-order data record in which the time is later than the current time exists in a source table or no data exists in a subtask or a partition of a source table, the window may not be terminated and the output data may be abnormal. To avoid this issue, you must specify an offset based on the out-of-order data and make sure that data exists in all subtasks and all partitions of the source table. If no data exists in a subtask or a partition of the source table, the watermark cannot advance and the window cannot be terminated in a timely manner. In this case, you can add `table.exec.source.idle-timeout: 10s` to the Other Configuration field in the Parameters section of the Configuration tab on the Deployments page to trigger the termination of the window. For more information about this parameter, see Configuration.
> After data is processed by using GROUP BY, JOIN operations on two data streams, or OVER window nodes, the watermark property is lost and the event time can no longer be used for windowing.

Processing time: the local system time at which the system processes an event. The processing time is generated by Flink and does not exist in your raw data. Therefore, you must explicitly define a Processing Time column.

> **Note:** The processing time is affected by the speed at which events reach Flink and the order in which data is processed in Flink. Therefore, the results of each backtrack may be different.

**Cascading windows**

The event time attribute of the rowtime column no longer takes effect after a window

| ction such as | TUMBLE ROWTIME _ |   |
|---|---|---|
| max(rowtime) |   |   |
|   |   | of the rowtime |

operation is complete. You can use a helper function such as `TUMBLE_ROWTIME` , `HOP_ROWTIME` , or `SESSION_ROWTIME` to obtain `max(rowtime)` of the rowtime column in a window. You can use the obtained value as the rowtime of the time window. The value is `window_end - 1` and is of the TIMESTAMP data type. The TIMESTAMP value has the rowtime attribute. For example, if the time span of a window is `[00:00, 00:15)` , `00:14:59.999` is returned. In the following example, 1-hour tumbling windows are used to aggregate data based on the aggregation results of 1-minute tumbling windows. This helps you meet various window requirements. QL reference

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
  'connector'='datahub'        -- Simple Log Service allows you to export only VARCHAR-
type DDL statements. Therefore, DataHub is used to store data.
  ...
```

);

```
CREATE TEMPORARY VIEW one_minute_window_output AS SELECT
  TUMBLE_ROWTIME(ts, INTERVAL '1' MINUTE) as rowtime,  -- Use TUMBLE_ROWTIME as the agg
regation time of the level-two window.
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

QL reference

| GeminiStateBackend | Memory |
|---|---|
| HashMapStateBackend | Memory |
| RocksDBStateBackend | Memory |
| RocksDBStateBackend | File |

For more information about state storage backends, see GeminiStateBackend and HashMapStateBackend. Timers are mainly used to trigger expired windows. If the memory is sufficient, you can store the timers in the memory for better performance. If a large number of timers exist or memory resources are insufficient, you can use RocksDBStateBackend to store the timers in a RocksDB file.

#### 4.7.1 Overview

This topic describes the window functions, time attributes, and window types that Flink SQL supports.

**Window functions**

Flink SQL supports aggregation over infinite windows. Windows do not need to be explicitly defined in SQL statements. Flink SQL also supports aggregation over a specific window. For example, to count the number of users who clicked a URL in the last minute, you can define a window to collect data about user clicks for the previous minute. Then, you can compute the data in the window to obtain the result. Flink SQL supports window aggregates and over aggregates. This topic describes window aggregates. Window aggregates support the windows that are defined based on the following two time attributes: event time and processing time. For each time attribute, Flink SQL supports three window types: tumbling window, sliding window, and session window.

**Time attributes**

Flink SQL supports two time attributes: event time and processing time. Realtime Compute for Apache Flink aggregates data in windows based on these time attributes. The event time attribute specifies the time when each data entry is created. It is provided in the schema. The processing time attribute specifies the local system time at which the system processes an event.

> **Note:** For more information about the time attributes in Apache Flink, visit Time Attributes.

**Cascading windows**

The event time attribute of the rowtime column no longer takes effect after a window

|   | TUMBLE ROWTIME _ |
|---|---|
| max(rowtime) |   |

operation is complete. You can use a helper function such as `TUMBLE_ROWTIME` , `HOP_ROWTIME` , or `SESSION_ROWTIME` to obtain `max(rowtime)` of the rowtime column in a window. You can use the obtained value as the rowtime of the time window. The value is `window_end - 1` and is of the TIMESTAMP data type. The TIMESTAMP value has the rowtime attribute. For example, if the time span of a window is `[00:00, 00:15)` , `00:14:59.999` is returned. QL reference In the following example, 1-hour tumbling windows are used to aggregate data based on the aggregation results of 1-minute tumbling windows. This helps you meet various window requirements.

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
  'connector'='datahub'        -- Log Service allows you to export only VARCHAR-type DD
L statements. Therefore, DataHub is used for storage.
  ...
```

);

```
CREATE TEMPORARY VIEW one_minute_window_output AS SELECT
  TUMBLE_ROWTIME(ts, INTERVAL '1' MINUTE) as rowtime,  -- Use TUMBLE_ROWTIME as the agg
regation time of the level-two window.
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

This topic describes how to use the Flink rolling window function.

**Definition**

QL reference A tumbling window (TUMBLE) assigns each element to a window of a specified size. Typically, a tumbling window has a fixed size and windows do not overlap. For example, if you specify a 5-minute tumbling window, an infinite stream of data divides into windows such as `[0:00,` `0:05)` , `[0:05, 0:10)` , `[0:10, 0:15)` , and so on. The following figure shows a 30-second tumbling window.

**Syntax**

Use the TUMBLE function in the GROUP BY clause to define a tumbling window.

```xml
TUMBLE(<time-attr>, <size-interval>) <size-interval>: INTERVAL 'string' timeUnit
```

> **Note:** The `<time-attr>` parameter must be a valid time attribute field in the time stream, specified as either Processing Time or Event Time. For more information about how to define Time attributes, see Overview.

**Identifier functions**

Use an identifier function to select the start time or end time of a window. The time attribute of the window supports aggregation for downstream windows.

| Window identifier function | Return type | Description |
|---|---|---|

QL reference

| TUMBLE START(time- _ |   | TIMESTAMP | Returns the start time of the window (inclusive). For example, for the window [00:10, 00:15) , the function returns 00:10 . |
|---|---|---|---|
|   | TUMBLE START(time- _ |   |   |
| attr, size- |   |   |   |
| interval) |   |   |   |
| TUMBLE END(time- _ |   | TIMESTAMP | Returns the end time of the window (inclusive). For example, for the window [00:00, 00:15] , the function returns 00:15 . |
|   | TUMBLE END(time- _ |   |   |
| attr, size- |   |   |   |
| interval) |   |   |   |
| TUMBLE ROWTIME(tim _ |   |   | Returns the end time of the window (exclusive). For example, for the window [00:00, 00:15] , the function returns 00:14:59.999 . The return value is a rowtime attribute, which means you can perform time-based operations on this field, such as cascading windows. You can use this function only on Event Time-based windows. For more information, see Cascading windows. |
|   | TUMBLE ROWTIME(tim _ |   |   |
| e-attr, size- |   |   |   |
|   |   | T a |   |
| interval) |   |   |   |
| TUMBLE PROCTIME(ti |   |   | Returns the end time of the window (exclusive). For example, for the window [00:00, 00:15] , the function returns 00:14:59.999 . The return value is a proctime attribute, which meands you can perform time-based operations on this field, such as cascading windows. You can use this function only on Processing Time-based windows. For more information, see Cascading windows. |
|   | TUMBLE PROCTIME(ti |   |   |
| _ me-attr, size- | _ |   |   |
|   |   | TI att |   |
| interval) |   |   |   |

|   | [00:10, 00:15) |
|---|---|
| 00:10 |   |

|   | [00:00, 00:15] |
|---|---|
| 00:14:59.999 |   |

|   | [00:00, 00:15] |
|---|---|
| 00:14:59.999 |   |

**Example of using Event Time to count clicks per minute for**

**each user on a specified website**

Test data

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
  'connector'='datahub'          --SLS currently supports only VARCHAR-type DDL for o
utput, so use DataHub for storage.
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
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | Jar |   |
|   | 10:00:00.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:01:00.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 2 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | Jar |   |
|   | 10:01:00.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:02:00.0 |   |   |   |   |

QL reference

|   | 2017-10-10 |   |   |   |   |   |   | Timo | 1 |
|---|---|---|---|---|---|---|---|---|---|
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 |   |   |
|   | 10:02:00.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:03:00.0 |   |   |   |   |

**Example of using Processing Time to count clicks per minute**

**for each user on a specified website**

Test data

| username (VARCHAR) | click url (VARCHAR) _ |
|---|---|
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Timo | http://taobao.com/xxx |

Test statement QL reference

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
  'connector'='datahub'              -- Currently, SLS supports only VARCHAR-type DDL
for output, so use DataHub for storage.
  ...
```

);

```
INSERT INTO tumble_output SELECT TUMBLE_START(ts, INTERVAL '1' MINUTE), TUMBLE_END(ts, INTERVAL '1' MINUTE), username, COUNT(click_url) FROM window_test GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE), username;
```

Test results

|   | window start _ (TIMESTAMP) |   |   |   |   | window end _ (TIMESTAMP) |   |   |   | username (VARCHAR) | clicks (BIGINT) |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | 2019-04-11 |   |   |   |   |   |   |   |   | Jark | 5 |
|   |   | 2019-04-11 |   |   |   |   | 201 | 9-04-11 |   |   |   |
|   | 14:43:00.0 |   |   |   |   |   |   |   |   |   |   |
|   |   |   | 00 |   |   | 14:44:00.000 |   |   |   |   |   |
|   | 2019-04-11 |   |   |   |   |   |   |   |   | Timo | 1 |
|   |   | 2019-04-11 |   |   |   |   | 201 |   | 9-04-11 | Timo |   |
|   | 14:43:00.0 |   |   |   |   |   |   |   |   |   |   |
|   |   |   | 00 |   |   | 14:44:00.000 |   |   |   |   |   |

#### 4.7.3 Sliding window

This topic describes how to use the Flink sliding window function.

**Definition**

A sliding window (HOP) differs from a tumbling window in that its windows can overlap. A sliding window has two parameters: **slide** and **size**. The **slide** parameter defines the step size for each slide. The **size** parameter defines the window size. QL reference
**slide < size**: Windows overlap, and the system assigns each element to multiple windows.
**slide = size**: This setting is equivalent to a tumbling window (TUMBLE).
**slide > size**: This setting is equivalent to a hopping window. Windows do not overlap and
have gaps between them. In most cases, most elements fit into multiple window scenarios because windows overlap. Therefore, sliding windows are useful for calculating moving averages. For example, to calculate the average value of data from the past 5 minutes and update it every 10 seconds, set **slide** to 10 seconds and **size** to 5 minutes. The following figure shows a sliding window with a 30-second interval and a 1-minute window size.

**Function syntax**

Use the HOP function in the GROUP BY clause to define a sliding window.

```xml
HOP(<time-attr>, <slide-interval>,<size-interval>) <slide-interval>: INTERVAL 'string' timeUnit <size-interval>: INTERVAL 'string' timeUnit
```

> **Note:** The `<time-attr>` parameter must be a valid time attribute field in the stream, specified as either Processing Time or Event Time. For more information about how to define Time attributes, see Overview.

**Identifier functions**

Use a sliding window identifier function to select the start time or end time of a window. The time attribute of the window supports aggregation for downstream windows. QL reference

|   | Window identifier function |   | Return type | Description |   |
|---|---|---|---|---|---|
|   | HOP START(<time- _ |   |   | Returns the start time of the window (inclusive). For example, for the window [00:10, 00:15) , the function returns 00:10 . |   |
|   |   | HOP START(<time- _ |   | Returns the start |   |
|   | attr>, <slide- |   |   |   |   |
|   |   |   | TIMESTAMP |   |   |
|   |   |   | TIMEST |   |   |
|   | interval>, <size- |   |   |   |   |
|   | interval>) |   |   |   |   |
|   | HOP END(<time- _ |   |   | Returns the end time of the window (inclusive). For example, for the window [00:00, 00:15) , the function returns 00:15 . |   |
|   |   | HOP END(<time- _ |   | Returns the end |   |
|   | attr>, <slide- |   |   |   |   |
|   |   |   | TIMESTAMP |   |   |
|   |   |   | TIMEST |   |   |
|   | interval>, <size- |   |   |   |   |
|   | interval>) |   |   |   |   |
|   | HOP ROWTIME(<time- _ |   |   | Returns the end time of the window (exclusive). For example, for the window [00:00, 00:15) , the function returns 00:14:59.999 . The return value is a rowtime attribute, which means can perform time-based operations on this field, such as Cascading windows. You can use this function only on Event Time-based windows. |   |
|   |   |   |   | For example, for the |   |
|   | attr>, <slide- |   | TIMESTAMP (rowtime- |   | 00:14:59.999 |
|   | interval>, <size- |   | attr) |   |   |
|   | interval>) |   |   |   |   |
|   | HOP PROCTIME(<time _ |   |   | Returns the end time of the window (exclusive). For example, for the window [00:00, 00:15) , the function returns 00:14:59.999 . The return value is a proctime attribute, which meands you can perform time-based operations on this field, such as Cascading windows. You can use this function only on Processing Time-based windows. |   |
|   |   | HOP PROCTIME(<time _ | TIMESTAMP (rowtime- | the function returns |   |
|   | -attr>, <slide- |   |   |   |   |
|   |   |   | attr) |   |   |
|   | interval>, <size- |   |   |   |   |
|   | interval>) |   |   |   |   |

|   | [00:10, 00:15) |
|---|---|
| 00:10 |   |

|   | [00:00, 00:15) |
|---|---|
| 00:15 |   |

Count the number of clicks for each user over the past minute. Update the count every 30 seconds. This means the system uses a 1-minute window and slides it every 30 seconds. Test data

| username (VARCHAR) | click url (VARCHAR) _ | ts (TIMESTAMP) |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |

QL reference

| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
|---|---|---|
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
  'connector'='datahub'           --SLS currently supports only VARCHAR-type DDL for
output, so use DataHub for storage.
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

Test results

|   | window start _ (TIMESTAMP) |   |   |   | window end _ (TIMESTAMP) |   |   | username (VARCHAR) | clicks (BIGINT) |
|---|---|---|---|---|---|---|---|---|---|
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 2 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | Jar |   |
|   | 09:59:30.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:00:30.0 |   |   |   |   |

QL reference

|   | 2017-10-10 |   |   |   |   |   |   | Jark | 3 |
|---|---|---|---|---|---|---|---|---|---|
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | Jar |   |
|   | 10:00:00.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:01:00.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 2 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | Jar |   |
|   | 10:00:30.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:01:30.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 2 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | Jar |   |
|   | 10:01:00.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:02:00.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 1 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 |   |   |
|   | 10:01:30.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:02:30.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Timo | 1 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | Ti |   |
|   | 10:02:00.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:03:00.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Timo | 1 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | Ti |   |
|   | 10:02:30.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:03:30.0 |   |   |   |   |

The HOP window cannot read the time when data enters. The start time of the first window shifts backward. **Shift duration = Window duration - Step size** . See the following table for examples.

| Window duration (second s) | Step size (seconds) |   | Event Time |   |   |   | StartTime of the first window |   |   |   |   | EndTime of the first window |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 120 | 30 |   | 2019-07-31 |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   | 2019-07-31 |   |   |   | 201 | 9-07-31 |   |   |   | 201 | 9-07-31 |   |
|   |   |   | 10:00:0 |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 0.0 |   | 09:58:3 |   |   | 0.0 |   | 10:00:30.0 |   |   |   |
| 60 | 10 |   | 2019-07-31 |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   | 2019-07-31 |   |   |   | 201 | 9-07-31 |   |   |   | 201 | 9-07-31 |   |
|   |   |   | 10:00:0 |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 0.0 |   | 09:59:1 |   |   | 0.0 |   | 10:00:10.0 |   |   |   |

#### 4.7.4 Session window

This topic describes how to use the Flink session window function.

**Definition**

QL reference A session window (SESSIOIN) groups elements by SESSION activity. Unlike tumbling windows and sliding windows, a session window has no overlapping windows or fixed window size. Instead, the system closes the window when it no longer receives elements within a fixed time period, which indicates a session break. You can configure a session window with a gap interval which defines the length of the inactive period. For example, a data stream representing mouse click activity may have long idle periods interspersed with bursts of clicks. If data arrives after the specified gap interval, the system starts a new window. The following figure shows an example of session windows. Each key forms different windows due to different data distributions.

**Function syntax**

Use the SESSION function in the GROUP BY clause to define a session window.

```xml
SESSION(<time-attr>, <gap-interval>) <gap-interval>: INTERVAL 'string' timeUnit
```

> **Note:** `<time-attr>` must be a valid time attribute field in the data stream, specified as either Processing Time or Event Time. For more information about how to define Time attributes, see Overview.

**Identifier functions**

QL reference Use an identifier function to select the start time or end time of a window. The time attribute of the window supports aggregation for downstream windows.

| Window identifier function |   | Return type | Description |
|---|---|---|---|
| SESSION START(<tim _ |   |   | Returns the start time of the window (inclusive). For example, for a window [00:10,00:15) , the function returns 00:10 , which is the time of the first record in this session window. |
|   | SESSION START(<tim _ |   |   |
| e-attr>, <gap- |   |   |   |
|   |   | Tim |   |
| interval>) |   |   |   |
| SESSION END(<time- _ |   |   | Returns the end time of the window (inclusive). For example, for a window [00:00,00:15) , the function returns 00:15 , which is the time of the last record in this session window plus <gap-interval> . |
|   | SESSION END(<time- _ |   |   |
| attr>, <gap- |   | T |   |
| interval>) |   |   |   |
| SESSION ROWTIME(<t _ |   |   | Returns the end time of the window (exclusive). For example, for a window [00:00,00:15) , the function returns 00:14:59.999 . The return value is a rowtime attribute, which means you can perform time-based operations on this field, such as Cascading windows. You can use this function only on Event Time-based windows. |
|   | SESSION ROWTIME(<t _ |   | th |
| ime-attr>, <gap- |   |   |   |
|   |   | Times attr) |   |
| interval>) |   |   |   |
| SESSION PROCTIME(< _ |   |   | Returns the end time of the window (exclusive). For example, for a window [00:00,00:15) , the function returns 00:14:59.999 . The return value is a proctime attribute, which means you can perform time-based operations on this field, such as Cascading windows. You can use this function only on Processing Time-based windows. |
|   | SESSION PROCTIME(< _ |   | the |
| time-attr>, <gap- |   |   |   |
|   |   | Timest attr) |   |
| interval>) |   |   |   |

|   | [00:10,00:15) |
|---|---|
| 00:10 |   |

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

QL reference

| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

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
  'connector'='datahub'           --SLS currently supports only VARCHAR-type DDL for
output, so use DataHub for storage.
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
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | Jar |   |
|   | 10:00:00.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:00:40.0 |   |   |   |   |

QL reference

|   | 2017-10-10 |   |   |   |   |   |   | Jark | 2 |
|---|---|---|---|---|---|---|---|---|---|
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | Jar |   |
|   | 10:00:49.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:01:35.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Jark | 1 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | Jar |   |
|   | 10:01:58.0 |   |   |   |   |   |   |   |   |
|   |   |   |   |   | 10:02:28.0 |   |   |   |   |
|   | 2017-10-10 |   |   |   |   |   |   | Timo | 1 |
|   |   | 2017-10-10 |   |   |   |   | 2017-10-10 | Ti |   |
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

In Flink SQL, OVER windows are defined in compliance with standard SQL syntax. Traditional OVER windows are not classified into fine-grained window types. OVER windows are classified into the following two types based on how computed rows are determined: ROWS OVER windows: Each row of elements is treated as a new computed row. A new window is generated for each row. RANGE OVER windows: All rows of elements with the same timestamp are treated as one QL reference computed row and are assigned to the same window.

**Attributes**

| Orthogonal attribute | Description | proctime | eventtime |
|---|---|---|---|
| ROWS OVER Window | A window is determined based on the actual row of an element. | Supported | Supported |
| RANGE OVER Window | A window is determined based on the timestamp value of an element. | Supported | Supported |

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

value_expression: specifies the value expression used for partitioning. timeCol: specifies the time field used to sort elements. rowCount: specifies the number of rows that precede the current row. This example describes bounded ROWS OVER windows. Assume that an on-sale product table contains item IDs, item types, on-sale time, and prices. Calculate the highest price among the three products similar to the current product before the current product is on sale. QL reference Test data

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

|   |   | 2017-11-11 | 2 |
|---|---|---|---|
|   | 10:01:00 |   |   |

|   |   | 2017-11-11 | 5 |
|---|---|---|---|
|   | 10:02:00 |   |   |

|   |   | 2017-11-11 | 3 |
|---|---|---|---|
|   | 10:03:00 |   |   |

|   |   | 2017-11-11 | 6 |
|---|---|---|---|
|   | 10:03:00 |   |   |

|   |   | 2017-11-11 | 4 |
|---|---|---|---|
|   | 10:05:00 |   |   |

|   |   | 2017-11-11 | 2 |
|---|---|---|---|
|   | 10:06:00 |   |   |

|   |   | 2017-11-11 | 7 |
|---|---|---|---|
|   | 10:07:00 |   |   |

|   |   | 2017-11-11 | 2 |
|---|---|---|---|
|   | 10:08:00 |   |   |

Test statements

```
CREATE TEMPORARY TABLE tmall_item(
  itemID VARCHAR,
  itemType VARCHAR,
  eventtime varchar,
  onSellTime AS TO_TIMESTAMP(eventtime),
  price DOUBLE,
  WATERMARK FOR onSellTime AS onSellTime - INTERVAL '0' SECOND  -- Define a waterma
rk for the rowtime. ) WITH (
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

QL reference Test results

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
| tronic | 10:01:00 |   |

|   |   | 2017-11-11 |
|---|---|---|
| tronic | 10:02:00 |   |

|   |   | 2017-11-11 |
|---|---|---|
| tronic | 10:03:00 |   |

|   |   | 2017-11-11 |
|---|---|---|
| tronic | 10:03:00 |   |

|   |   | 2017-11-11 |
|---|---|---|
| tronic | 10:05:00 |   |

|   |   | 2017-11-11 |
|---|---|---|
| tronic | 10:06:00 |   |

|   |   | 2017-11-11 |
|---|---|---|
| tronic | 10:07:00 |   |

|   |   | 2017-11-11 |
|---|---|---|
| hes | 10:08:00 |   |

**RANGE OVER windows**

For a RANGE OVER window, all elements with the same timestamp are assigned to the same window. Syntax

```
SELECT
    agg1(col1) OVER(
     [PARTITION BY (value_expression1,..., value_expressionN)]
     ORDER BY timeCol
     RANGE
     BETWEEN (UNBOUNDED | timeInterval) PRECEDING AND CURRENT ROW) AS colName,
... FROM Tab1;
```

value_expression: specifies the value expression used for partitioning. timeCol: specifies the time field used to sort elements. timeInterval: specifies the time interval between the time of the current row and that of the element row to which it can be traced back. This example describes bounded RANGE OVER windows. Assume that an on-sale product table contains item IDs, item types, on-sale time, and prices. Calculate the highest price among similar products that are on sale 2 minutes earlier than the current product. QL reference Test data

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

|   |   | 2017-11-11 | 2 |
|---|---|---|---|
|   | 10:01:00 |   |   |

|   |   | 2017-11-11 | 5 |
|---|---|---|---|
|   | 10:02:00 |   |   |

|   |   | 2017-11-11 | 3 |
|---|---|---|---|
|   | 10:03:00 |   |   |

|   |   | 2017-11-11 | 6 |
|---|---|---|---|
|   | 10:03:00 |   |   |

|   |   | 2017-11-11 | 4 |
|---|---|---|---|
|   | 10:05:00 |   |   |

|   |   | 2017-11-11 | 2 |
|---|---|---|---|
|   | 10:06:00 |   |   |

|   |   | 2017-11-11 | 7 |
|---|---|---|---|
|   | 10:07:00 |   |   |

|   |   | 2017-11-11 | 2 |
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
  WATERMARK FOR onSellTime AS onSellTime - INTERVAL '0' SECOND  -- Define a waterma
rk for the rowtime. ) WITH (
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
| onic | 10:01:00 |   |   |

|   |   | 2017-11-11 | 50 |
|---|---|---|---|
| onic | 10:02:00 |   |   |

|   |   | 2017-11-11 | 30 |
|---|---|---|---|
| onic | 10:03:00 |   |   |

|   |   | 2017-11-11 | 60 |
|---|---|---|---|
| onic | 10:03:00 |   |   |

|   |   | 2017-11-11 | 40 |
|---|---|---|---|
| onic | 10:05:00 |   |   |

|   |   | 2017-11-11 | 20 |
|---|---|---|---|
| onic | 10:06:00 |   |   |

|   |   | 2017-11-11 | 70 |
|---|---|---|---|
| onic | 10:07:00 |   |   |

|   |   | 2017-11-11 | 20 |
|---|---|---|---|
| es | 10:08:00 |   |   |

QL reference

### 4.8 Built-in functions

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

Test statements QL reference

```
SELECT BITAND(a, b) as intt FROM T1;
```

Test result

**intt(INT)**

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

This topic describes how to use the BITOR function to perform a bitwise OR operation. QL reference

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
INT BITOR(INT number1, INT number2)
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

QL reference

| number2 | INT |
|---|---|

> **Note:** The input and output parameters are both of the INT type.

Test data

| a(INT) | b(INT) |
|---|---|
| 2 | 3 |

Test statements

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

QL reference

| TO BASE _ | INT | Positive valid values: [2, 36]. Negative valid values: [-36, - 2]. |
|---|---|---|

Test data

| id(INT) | x(BIGINT) | y (VARCHAR) |
|---|---|---|
| 1 | 12L | '12' |
| 2 | 10L | '10' |
| 3 | 0L | 'test' |
| 4 | NULL | NULL |

Test statements

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

QL reference

| enddate | TIMESTAMP or VARCHAR |
|---|---|

> **Note:** A date of the VARCHAR type is in the **yyyy-MM-dd** or **yyyy-MM-dd HH:mm:ss** format.
> If an input parameter is NULL or a parsing error occurs, NULL is returned.

Test data

| datetime1(VARCHAR) | datetime2(VARCHAR) | nullstr(VARCHAR) |
|---|---|---|
| 2017-10-15 00:00:00 | 2017-09-15 00:00:00 | NULL |

Test statements

```
SELECT DATEDIFF(datetime1, datetime2) as int1,
        DATEDIFF(TIMESTAMP '2017-10-15 23:00:00',datetime2) as int2,
        DATEDIFF(datetime2,TIMESTAMP '2017-10-15 23:00:00') as int3,
        DATEDIFF(datetime2,nullstr) as int4,
        DATEDIFF(nullstr,TIMESTAMP '2017-10-15 23:00:00') as int5,
        DATEDIFF(nullstr,datetime2) as int6,
        DATEDIFF(TIMESTAMP '2017-10-15 23:00:00',TIMESTAMP '2017-9-15 00:00:00')as in
```

`t7`

```
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

QL reference

| startdate | TIMESTAMP or VARCHAR Note A date of the VARCHAR type is in the yyyy-MM- dd or yyyy-MM-dd HH:mm:ss format. |
|---|---|
| time | TIMESTAMP |
| days | INT |

> **Note:** If an input parameter is NULL or a parsing error occurs, NULL is returned.

Test data

| datetime1(VATCHAR) | nullstr(VATCHAR) |
|---|---|
| 2017-09-15 00:00:00 | null |

Test statements

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

QL reference

| date | VARCHAR | The source string. The default format is yyyy- MM-dd HH:mm:ss. |
|---|---|---|
| from format _ | VARCHAR | The original format. This parameter is optional. The default format is yyyy-MM-dd hh:mm:ss. |
| to format _ | VARCHAR | The format of the output date. |

> **Note:** If an input parameter is NULL or a parsing error occurs, NULL is returned.

Test data

| date1(VARCHAR) | datetime1(VARCHAR) | nullstr(VARCHAR) |
|---|---|---|
| 0915-2017 | 2017-09-15 00:00:00 | NULL |

Test statements

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

QL reference

| format | VARCHAR | The format of the output date, for example, yyyy-MM-dd HH:mm:ss. |
|---|---|---|
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
| 1970-01-01 08:00:00 | 1970-01-01 08:00:00 |

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
| startdate | VARCHAR Note A date of the VARCHAR type is in the yyyy-MM- dd or yyyy-MM-dd HH:mm:ss format. |
| time | TIMESTAMP |
| days | INT |

QL reference

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

This topic describes how to use the FROM_UNIXTIME function. This function returns a date of the VARCHAR type.

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

QL reference

| 1505404800 | NULL |
|---|---|

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

Test result QL reference

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
| path | VARCHAR | The expression of the specified path. You must use single quotation marks (') in a custom path. Example: JSON VALUE(json,'$.passenger name') AS _ _ ABC The following symbols are supported in a path: $: indicates the root object. []: indicates the array subscript. *: indicates the array wildcard characters. .: indicates child elements. |

> **Note:** If the input parameters contain invalid JSON or NULL values, NULL is returned.

Test data Table 1. T1

| id(INT) | json(VARCHAR) | path1(VARCHAR) |
|---|---|---|
| 1 | [10, 20, [30, 40]] | $[2][*] |
| 2 | {"aaa":"bbb","ccc": {"ddd":"eee","fff":"ggg","hhh": ["h0","h1","h2"]},"iii":"jjj"} | $.ccc.hhh[*] |

QL reference

| 3 | {"aaa":"bbb","ccc": {"ddd":"eee","fff":"ggg",hhh": ["h0","h1","h2"]},"iii":"jjj"} | $.ccc.hhh[1] |
|---|---|---|
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
| 6 | NULL |

##### 4.8.2.14 KEYVALUE

This topic describes how to use the KEYVALUE function. This function splits a string into keyvalue pairs based on the split1 delimiter, and splits the key-value pairs based on the split2 delimiter. The value that corresponds to the key is returned.

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

QL reference

| split2 | VARCHAR | The split2 delimiter that splits the key-value pairs. |
|---|---|---|
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

Test result

**result(VARCHAR)**

v2 NULL NULL NULL NULL

##### 4.8.2.15 MURMUR_HASH

The topic describes how to use the MURMUR_HASH function. This function specifies the 32-bit hash value for a parameter by using the hash32x86 method.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

QL reference

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

740959099 NULL 271330425

**Example 2**

Test dataTable 2. T2

**str**

### 4.5 Subscription

NULL Test statements

```
SELECT MURMUR_HASH(CAST(str AS FLOAT)) as intt FROM T2;
```

Test result QL reference

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

This is a test String. NULL test Test statements

```
SELECT MURMUR_HASH_64(value) as big FROM T1;
```

Test result

**big(VARCHAR)**

2706826604463634835 NULL 5010266691562018262

**Example 2**

QL reference Test dataTable 2. T2

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
| urlStr | VARCHAR | The URL that you want to parse. Note If the value of urlStr is NULL, NULL is returned. |

QL reference

| partToExtract | VARCHAR | The part that you want to parse from the URL. Valid values: HOST PATH QUERY REF PROTOCOL FILE AUTHORITY USERINFO |
|---|---|---|
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

| var1( VAR CHA R) | var2( VAR CHA R) | var3 (VAR CHA R) | var4 (VAR CHA R) | var5 (VAR CHA R) | var6 (VAR CHA R) | var7 (VAR CHA R) | var8 (VAR CHA R) | var9 (VAR CHA R) | var1 0(VA RCH AR) | var1 1(VA RCH AR) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | query =1 | faceb ook.c om | /path /p1.p hp | NULL | http | /path /p1.p hp? query =1 | faceb ook.c om | NULL | NULL | NULL |

##### 4.8.2.18 REGEXP

This topic describes how to use the REGEXP function. This function searches a specified string by using a regular expression and returns a Boolean value based on the matching result. QL reference

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

true false false false false

##### 4.8.2.19 REGEXP_REPLACE

QL reference This topic describes how to use the REGEXP_REPLACE function. This function replaces the specified string with the desired string and returns a new string.

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

20140313 QL reference Empty string s2s0s1s4s-s0s3s-s1s3s null num-num

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

Test statements QL reference

```
SELECT SPLIT_INDEX(str, sep, index) as var1 FROM T1;
```

Test result

**var1(VARCHAR)**

Mary NULL NULL NULL

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

QL reference Test result

| var1(DATE) | var2(DATE) | var3(DATE) |
|---|---|---|
| 1970-04-11 | 2017-09-15 | 2017-09-15 |

##### 4.8.2.22 TO_TIMESTAMP_TZ

This topic describes how to use the TO_TIMESTAMP_TZ function. This function converts a date value of the VARCHAR type into the TIMESTAMP type based on the specified time zone.

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

This topic describes how to use the UNIX_TIMESTAMP function. This function converts a date value into a UNIX timestamp. QL reference

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
BIGINT UNIX_TIMESTAMP(VARCHAR date) BIGINT UNIX_TIMESTAMP(TIMESTAMP timestamp) BIGINT UNIX_TIMESTAMP(VARCHAR date, VARCHAR format)
```

**Input parameters**

| Parameter | Data type | Description |   |   |
|---|---|---|---|---|
| timestamp | TIMESTAMP | N/A. |   |   |
| date | VARCHAR | The default date format is yyyy-MM-dd HH:mm:ss . |   |   |
|   |   |   | yyyy-MM-dd |   |
| format | VARCHAR | The default date format is yyyy-MM-dd hh:mm:ss . |   |   |
|   |   |   | yyyy-MM-dd |   |

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

QL reference

```
GENERATE_SERIES(INT from, INT to)
```

**Input parameters**

| Parameter | Data type |
|---|---|
| from | The lower boundary of a series of values (including the lower boundary). This parameter is of the INT type. |
| to | The upper boundary of a series of values (excluding the upper boundary). This parameter is of the INT type. |

Test data Table 1. T1

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

QL reference

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| str | VARCHAR | The JSON string. |
| path1 to pathN | VARCHAR | A path string, which does not start with a dollar sign ( $ ). |

Test data Table 1. T1

| d(VARCHAR) | s(VARCHAR) |
|---|---|
| {"qwe":"asd","qwe2":"asd2","qwe3":"asd3"} | qwe3 |
| {"qwe":"asd4","qwe2":"asd5","qwe3":"asd3"} | qwe2 |

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

This topic describes how to use the MULTI_KEYVALUE function. This function splits a string into key-value pairs based on the key-value pair delimiter specified by split1, splits a keyvalue pair based on the delimiter specified by split2, and returns the values of key_name1 and key_name2.

> **Important:** This function is supported only in VVP 2.4.0 and VVR 3.0.0 and later.

**Syntax**

```
MULTI_KEYVALUE(VARCHAR str, VARCHAR split1, VARCHAR split2, VARCHAR key_name1, VARCHAR key_name2, ...)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|

QL reference

| str | VARCHAR | The string that you want to split. |
|---|---|---|
| split1 | VARCHAR | The key-value pair delimiter. If the value of split1 is NULL, spaces are used as key-value pair delimiters. If the length of split1 is greater than 1, split1 represents only a set of delimiters, in which each character represents a valid delimiter. |
| split2 | VARCHAR | The key-value delimiter. If the value of split2 is NULL, spaces are used as key-value delimiters. If the length of split2 is greater than 1, split2 represents only a set of delimiters, in which each character represents a valid delimiter. |
| key name1, _ key name2, ... _ | VARCHAR | The list of keys whose values you want to obtain. |

Test data Table 1. T1

| str(VARCHAR) | split1(VARCHA R) | split2(VARCHA R) | key1(VARCHAR ) | key2(VARCHAR ) |
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

QL reference

| NULL | NULL |
|---|---|
| v1 | NULL |
| NULL | NULL |
| NULL | NULL |
| v1 | NULL |
| v1 | v2 |
| v1 | v2 |
| v1 | v2 |
| v1 | v2 |

##### 4.8.3.4 STRING_SPLIT

This topic describes how to use the STRING_SPLIT function. This function splits a string into substrings based on the specified delimiter and returns a list of substrings.

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

Test data Table 1. T1 QL reference

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

This topic describes how to use the APPROX_COUNT_DISTINCT function to improve the performance of your jobs.

> **Important:** This topic applies only to Ververica Platform (VVP) 2.4.0, Ververica Runtime (VVR) 3.0.0, and later.

**Background information**

When you optimize the COUNT DISTINCT function, distinct key information must be saved in the state data of the aggregate node. If a large number of distinct keys exist, the read/write overhead of state data is high. This situation causes a bottleneck in job performance optimization. In many cases, accurate computation is not necessary. If you want to achieve high job performance at the expense of a small portion of accuracy, you can use the
**APPROX_COUNT_DISTINCT** function. **APPROX_COUNT_DISTINCT** supports miniBatch and
local-global optimization on the aggregate node. When you use this function, make sure that the following requirements are met: The input data does not contain retract messages. A large number of distinct keys, such as unique visitors (UVs), exist. The
**APPROX_COUNT_DISTINCT** function cannot bring obvious benefits if only a small number
of distinct keys exist.

**Syntax**

```
APPROX_COUNT_DISTINCT(col [, accuracy])
```

**Input parameters**

QL reference

| Parameter | Data type | Description |
|---|---|---|
| col | All data types | The name of the field. |
| accuracy | FLOAT | The computation accuracy. This parameter is optional. A larger value indicates a higher accuracy, which leads to a higher state overhead. A higher state overhead weakens the performance of the APPROX COUNT DISTINCT _ _ function. Valid values: (0.0, 1.0). Default value: 0.99. |

Test dataTable 1. T1

| a (VARCHAR) | c (BIGINT) |
|---|---|
| Hi | 1 |
| Hi | 2 |
| Hi | 3 |
| Hi | 4 |
| Hi | 5 |
| Hi | 6 |

Test statement

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

This topic describes how to use the FIRST_VALUE function. This function returns the first nonnull record of a data stream.

> **Important:** This topic applies only to Ververica Platform (VVP) 2.4.0, Ververica Runtime (VVR) 3.0.0, and later.

**Syntax**

QL reference

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
| 6 | 6 | Hello |
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

QL reference

| Hello | 1 |
|---|---|
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| NULL | 7 |
| Hello World | 7 |
| Hello World | 7 |
| Hello World | 7 |

##### 4.8.4.3 LAST_VALUE

This topic describes how to use the LAST_VALUE function. This function returns the last nonnull record of a data stream.

> **Important:** This topic applies only to Ververica Platform (VVP) 2.4.0, Ververica Runtime (VVR) 3.0.0, and later.

**Syntax**

```
T LAST_VALUE(T value) T LAST_VALUE(T value, BIGINT order)
```

**Input parameters**

| Parameter | Data type | Description |
|---|---|---|
| value | Any data type | A data stream. |
| order | BIGINT | The non-null record that has the largest order value is considered the last non-null record. |

> **Important:** All input parameters must be of the same data type.

Test data Table 1. T1

| a(BIGINT) | b(INT) | c(VARCHAR) |
|---|---|---|
| 1 | 1 | Hello |
| 2 | 2 | Hello |
| 3 | 3 | Hello |

QL reference

| 4 | 4 | Hello |
|---|---|---|
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
| Hello World | 8 |
| Hello World | 20 |

### 4.9 User-defined functions (JAR)

#### 4.9.1 Overview

This topic describes notes, classification, definition, and parameter-passing methods for developing Flink user-defined functions.

**Notes**

To avoid conflicts between JAR package dependencies, note the following guidelines when developing user-defined functions: QL reference Ensure that the Flink version you select on the draft development page matches the Flink version specified in your Pom dependencies. Set the scope of all Flink-related dependencies to provided, that is, add `<scope>provided</scope>` to each relevant dependency. Package all other third-party dependencies using the Shade method. For details about Shade packaging, see Apache Maven Shade Plugin.

**User-defined function classification**

Flink supports the following three types of user-defined functions.

| Classification | Description |
|---|---|
| UDF (user-defined scalar function) | A user-defined scalar function maps zero, one, or multiple scalar values to a new scalar value. The input and output have a one-to-one relationship, meaning the function reads one row of data and produces one output value. For more information, see User-defined scalar function (UDF). |
| UDAF (user-defined aggregation function) | A user-defined aggregation function aggregates multiple records into a single record. The input and output have a one-to-one relationship, meaning the function aggregates multiple input records into one output value. For more information, see User-defined aggregate function (UDAF). |
| UDTF (user-defined table-valued function) | A user-defined table-valued function accepts zero, one, or multiple scalar values as input parameters (which can be variable-length). Similar to custom-defined scalar functions but different in output, a table-valued function can return any number of rows, not just a single value. Each returned row may consist of one or more columns. A single function call can produce multiple rows or columns of data. For more information, see User-defined table-valued function (UDTF). |

**Pass parameters to user-defined functions**

If you need to modify certain parameter value in your user-defined function later, directly editing the UDF code becomes cumbersome. In this case, configure the parameter in the
**Additional Dependencies** configuration item of the fully managed Flink console, then
reference it within your UDF code. You can subsequently update the parameter value directly in the Flink console for rapid adjustments. User-defined functions provide an optional open(FunctionContext context) method. The FunctionContext object supports parameter passing, enabling the passing of custom configuration items through it. Follow these steps to pass parameters to user-defined functions:
1. Add the parameter and its value in **Additional Dependencies** of the **Configuration** panel
on the right side of the draft development page. Sample code:

```
maxJobCreationAttempts: value
```

2. Retrieve the user-defined function parameter in your UDF code using ConfigOptions.key().
Sample code: QL reference

```
String strValue = context.getJobParameter("key","default_value"); Integer intValue = Integer.parseInt(context.getJobParameter("key","default_value"));
```

If the function parameter is in key-value format, you must use the FunctionContext#getJobParameter method to obtain the value of the pipeline.global-jobparameters configuration item. When defining key-value pairs in pipeline.global-jobparameters, separate keys and values with a colon (:), and separate different key-value pairs with commas (,). If a key or value contains a colon or comma, enclose it with double quotation marks ("). If a key or value also contains double quotation marks, escape them by doubling the character (""). Sample code:

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
**Upload a file**: Click **Click to select** next to **Select a file**, then choose your target
user-defined function JAR file. If dependencies exist, click **Click to select** next to
**Dependencies** and select the files your user-defined function JAR depends on.
**External URL**: Enter the external URL address.

> **Note:** Your user-defined function JAR file is uploaded to the sql-artifacts directory in the OSS bucket you selected. Additionally, the Realtime Compute for Apache Flink development console parses the JAR file to detect classes implementing Flink UDF, UDAF, and UDTF interfaces, then automatically extracts class names and populates the Function Name field.
> For Java-based UDFs, dependencies can be packaged into the user-defined function JAR package or uploaded separately via the dependencies option.
> When the user-defined function file or its dependencies are large, we recommend uploading via an external URL. Note that if the external URL points to an OSS bucket, dependency files must reside in the sql- artifacts/namespaces/{namespace} directory.

v. Click **Confirm**. On the **SQL Editor** page, you can view all successfully registered UDFs in the **UDFs** list on the left. Job-level user-defined functions Global user-defined functions (catalog functions) default to parsing with the latest Flink version during registration. If you use a global user-defined function in a deployment while selecting a non-latest Flink version in advanced configuration, compatibility issues may arise. To resolve this, you may implement your UDF code according to the engine version required by your deployment and register it as a job-level user-defined function. Follow this process: i. Upload the user-defined function JAR package. In the left-side navigation pane, click **Artifacts** > **Upload Artifact** and upload the userdefined function JAR package. ii. Specify the job-level user-defined function in your deployment. QL reference In the **Additional Dependencies** configuration item of your deployment, specify the user-defined function JAR package. iii. Register the user-defined function. Use the `CREATE TEMPORARY FUNCTION` syntax to register a job-level user-defined function.

```
CREATE TEMPORARY FUNCTION MyScalarFunc AS 'com.test.MyScalarFunc';
```

#### 4.9.2 User-defined scalar function (UDF)

This topic describes how to develop, register, and use user-defined scalar functions (UDFs) in Flink.

**Definition**

A user-defined scalar function (UDF) maps zero, one, or multiple scalar values to a new scalar value. The input and output have a one-to-one relationship, meaning the function reads one row of data and writes one output value.

**Develop a UDF**

> **Note:** Flink provides Python UDX examples to help you quickly develop UDXs. These examples include implementations of Python UDFs, Python user-defined aggregate functions (UDAFs), and Python user-defined table-valued functions (UDTFs). They come with a pre- configured development environment for the corresponding version, so you do not need to set up the environment yourself.

1. Download and decompress the ASI_UDX_Demo example to your local machine.
After decompression, the system generates the **ASI_UDX-main** folder, containing the following items:
**pom.xml**: This is the project-level configuration file that primarily describes the Maven
coordinates, dependencies, rules that developers must follow, defect management systems, organizations, licenses, and other project-related factors.
**\ASI_UDX-main\src\main\java\ASI_UDF\ASI_UDF.java**: This is the Java code for the
UDF example.
2. In IntelliJ IDEA, click **File > Open** to open the decompressed **ASI_UDX-main** folder.
3. Double-click to open \ASI_UDX-main\src\main\java\ASI_UDF, then configure **ASI_UDF.java**
as needed. In this sample code, **ASI_UDF.java** already contains the code that retrieves characters from position begin to end in each row of data.

```java
package ASI_UDF; import org.apache.flink.table.functions.ScalarFunction; public class ASI_UDF extends ScalarFunction {
    public String eval(String s, Integer begin, Integer end) {
        return s.substring(begin, end);
```

`}` `}` QL reference
4. Double-click to open \ASI_UDX-main\, then configure **pom.xml**.
In this sample code, the **pom.xml** file already includes dependency information for the main JAR packages of Flink 1.11. If your business: Does not depend on other JAR packages: You do not need to configure the **pom.xml** file. Proceed with the next step. Depends on other JAR packages: Add the required JAR package dependency information to the **pom.xml** file. The main JAR package dependencies for Flink 1.11 are as follows.

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
1. Develop a Flink SQL draft. For more information, see the Develop a SQL draft section in Alib
aba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide. QL reference Retrieve characters from position 2 to 4 in field a of each row in the ASI_UDF_Source table. The sample code is as follows.

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

2. On the **Dewployments** page, click **Start** in the **Actions** column corresponding to the
target deployment. After starting the deployment, each row in the ASI_UDF_Sink table receives characters from position 2 to 4 in field a of each row in the ASI_UDF_Source table.

#### 4.9.3 User-defined aggregate function (UDAF)

**(UDAF)**

This topic describes how to develop, register, and use user-defined aggregate functions (UDAFs) in Flink.

**Definition**

A user-defined aggregate function (UDAF) aggregates multiple records into one record. The input and output have a one-to-one relationship, meaning the function aggregates multiple input records into one output value.

**Develop a UDAF**

> **Note:** Flink provides Python UDX examples to help you quickly develop UDXs. These examples include implementations of Python UDFs, Python user-defined aggregate functions (UDAFs), and Python user-defined table-valued functions (UDTFs). They come with a pre- configured development environment for the corresponding version, so you do not need to set up the environment yourself.

1. Download and decompress the ASI_UDX_Demo example to your local machine.
After decompression, the system generates the **ASI_UDX-main** folder, containing the following items: QL reference
**pom.xml**: This is the project-level configuration file that primarily describes Maven
coordinates, dependencies, rules that developers must follow, defect management systems, organizations, licenses, and all other project-related factors.
**\ASI_UDX-main\src\main\java\ASI_UDAF\ASI_UDAF.java**: This is the Java code for the
UDAF example.
2. In IntelliJ IDEA, click **file > open** to open the decompressed **ASI_UDX-main**.
3. Double-click to open \ASI_UDX-main\src\main\java\ASI_UDAF, then configure
**ASI_UDAF.java** as needed.
In this sample code, **ASI_UDAF.java** already contains the code that sums current and historical data. For instance, if the first data point is 1, the second is 2, and the third is 3, then the first result is 1, the second is 3, and the third is 6.

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
In this sample code, the **pom.xml** file already includes dependency information for the main JAR packages of Flink 1.11. If your business: Does not depend on other JAR packages: You do not need to configure the **pom.xml** file. Proceed with the next step. Depends on other JAR packages: Add the required JAR package dependency information to the **pom.xml** file. The main JAR package dependencies for Flink 1.11 are as follows. QL reference

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
1. Develop a Flink SQL draft. For more information, see the Develop a SQL draft section in Alib
aba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide. Obtain the sum of the current and historical data in field "a" of the ASI_UDAF_Source table. The sample code is as follows. QL reference

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

This topic describes how to develop, register, and use user-defined table-valued functions (UDTFs) in Flink.

**Definition**

A user-defined table-valued function (UDTF) accepts zero, one, or multiple scalar values as input parameters (which can be variable-length). Similar to custom-defined scalar functions but different in output, a table-valued function can return any number of rows, not just a single value. Each returned row may consist of one or more columns. A single function call can produce multiple rows or columns of data.

**Develop a UDTF**

> **Note:** Flink provides Python UDX examples to help you quickly develop UDXs. These examples include implementations of Python UDFs, Python user-defined aggregate functions (UDAFs), and Python user-defined table-valued functions (UDTFs). They come with a pre- configured development environment for the corresponding version, so you do not need to set up the environment yourself.

1. Download and decompress the ASI_UDX_Demo example to your local machine.
After decompression, the system generates the **ASI_UDX-main** folder, containing the following items:
**pom.xml**: This is the project-level configuration file that primarily describes the Maven
coordinates, dependencies, rules that developers must follow, defect management systems, organizations, licenses, and all other project-related factors.
**\ASI_UDX-main\src\main\java\ASI_UDF\ASI_UDTF.java**: This is the Java code for the
UDTF example. QL reference
2. In IntelliJ IDEA, click **file > open** to open the decompressed **ASI_UDX-main**.
3. Double-click to open \ASI_UDX-main\src\main\java\ASI_UDTF, then modify **ASI_UDTF.java**
file as needed. In this sample code, the **ASI_UDTF.java** already contains the code that splits a single string into multiple columns by using a pipe character (|).

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
In this sample code, the **pom.xml** file already includes dependency information for the main JAR packages of Flink 1.11. If your business: Does not depend on other JAR packages: You do not need to configure the **pom.xml** file. Proceed with the next step. Depends on other JAR packages: Add the required JAR package dependency information to the **pom.xml** file. The main JAR package dependencies for Flink 1.11 are as follows. QL reference

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

The JAR package named **ASI_UDX-1.0-SNAPSHOT.jar** appears in the \ASI_UDXmain\target\ directory, indicating that you have completed the UDTF development.

**Register a UDTF**

For the UDTF registration process, see the Managing UDFs section in Alibaba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide.

**Use a UDTF**

After registering a UDTF, you can use it to perform the following steps:
1. Develop a Flink SQL draft. For more information, see the Develop a SQL draft section in Alib
aba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide. Split each string in the message field of the ASI_UDTF_Source table into multiple columns by using a pipe character (|). The sample code is as follows: QL reference

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
| UDF (user-defined scalar function) | A user-defined scalar function maps zero, one, or multiple scalar values to a new scalar value. The input and output have a one- to-one relationship, meaning the function reads one row of data and produces one output value. For more information, see User- defined scalar function (UDF). |
| UDAF (user-defined aggregation function) | A user-defined aggregation function aggregates multiple records into one record. The input and output have a many-to-one relationship, meaning the function aggregates multiple input records into one output value. For more information, see User- defined aggregate function (UDAF). |

QL reference

| UDTF (user-defined table-valued function) | A user-defined table-valued function takes zero, one, or multiple scalar values as input parameters (which can be variable- length). Similar to custom-defined scalar functions but different in output, a table-valued function can return any number of rows, not just a single value. Each returned row can consist of one or more columns. A single function call can produce multiple rows or columns of data. For more information, see User-defined table-valued function (UDTF). |
|---|---|

**Dependency**

The Flink cluster pre-installs common Python packages such as Pandas, NumPy, and PyArrow. You can view the list of third-party Python packages installed in the Flink cluster on the
**Develop a draft** section in Alibaba Cloud Realtime Compute for Apache Flink (Compute-
Storage Separation Edition) Developer Guide. In addition, you can also use other types of third-party Python packages in Python userdefined functions. Note that if you use non-preinstalled third-party Python packages, you must upload them as dependency files when registering the Python UDF. For more information, see **Manage UDFs** and **Use Python dependencies** in Alibaba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide.

**Debugging**

You can output log information by using Logging in the code implementation of Python userdefined functions to facilitate issue diagnosis. The following example shows how to do this.

```python
@udf(result_type=DataTypes.BIGINT()) def add(i, j):
  logging.info("hello world")
  return i + j
```

After generating logs, you can view them in the TaskManager log files.

**Tuning**

Use the Pandas library In addition to standard Python user-defined functions, Flink also supports Pandas userdefined functions. For Pandas user-defined functions, the types of input data are data structures defined in Pandas, such as pandas.Series and pandas.DataFrame. You can use high-performance Python libraries like Pandas and NumPy within Pandas user-defined functions to develop high-performance user-defined functions. For more information, see Vectorized User-defined Functions. Configure the following parameters The performance of Python user-defined functions depends largely on their implementation. If you encounter performance issues, optimize the implementation of the Python user-defined functions as much as possible. In addition, the performance of Python user-defined functions is also affected by the values of the following parameters.

| Parameter | Description |
|---|---|

QL reference

| python.fn- execution.bundle.size | Python UDF computation is asynchronous. During execution, Java operators asynchronously send data to the Python process for processing. Before sending data to the Python process, Java operators cache the data and send it only after reaching a certain threshold. The python.fn-execution.bundle.size parameter controls the maximum number of data records that can be cached. The default value is 100,000, measured in number of records. |
|---|---|
| python.fn- execution.bundle.time | This parameter controls the maximum caching time for data. Computation of cached data triggers when either the number of cached records reaches the threshold defined by python.fn- execution.bundle.size or the caching time reaches the threshold defined by python.fn-execution.bundle.time. The default value is 1,000, measured in milliseconds. |
| python.fn- execution.arrow.batch.size | When you use Pandas UDFs, this parameter defines the maximum number of data records that a single Arrow batch can hold. The default value is 10,000. Note The value of python.fn-execution.arrow.batch.size cannot exceed that of python.fn-execution.bundle.size. |

> **Note:** Larger values for these three parameters are not always better. If you set these parameters too high, checkpoint operations may need to process excessive amount of data, leading to prolonged checkpoint durations or even checkpoint failures. For more details about these parameters, see Configuration.

#### 4.10.2 User-defined scalar function (UDF)

This topic describes the limits, development, registration, and usage of Python user-defined scalar functions (UDFs).

**Definition**

A user-defined scalar function (UDF) maps zero, one, or multiple scalar values to a new scalar value. The input and output have a one-to-one relationship, meaning the function reads one row of data and writes one output value.

**Limits**

Realtime Compute for Apache Flink is subject to deployment environments and network environments. Therefore, when you develop Python UDFs, note the following limits: Only open-source Flink V1.12 and later are supported. The Flink cluster pre-installs Python 3.7.9. Therefore, you must develop code in Python 3.7.9. Flink runs in JDK 1.8. If your Python deployment depends on third-party JAR packages, make sure that the JAR packages are compatible with JDK 1.8. QL reference Only open-source Scala V2.11 is supported. If your Python deployment depends on thirdparty JAR packages, make sure that you use JAR package dependencies corresponding to Scala V2.11.

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
1. Develop a Flink SQL draft. For more information, see the Develop a SQL draft section in Alib
aba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide. Obtain characters from position 2 to 4 in field a of each row in the ASI_UDF_Source table. Sample code: QL reference

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

2. On the **Deployments** page, click **Start** in the **Actions** column corresponding to the
deployment that you want to manage. After starting the deployment, each row in the ASI_UDF_Sink table receives characters from position 2 to 4 in field a of each row in the ASI_UDF_Source table.

#### 4.10.3 User-defined aggregate function (UDAF)

**(UDAF)**

This topic describes the limits, development, registration, and usage of Python user-defined aggregate functions (UDAFs).

**Definition**

A user-defined aggregate function (UDAF) aggregates multiple records into one record. The input and output have a many-to-one relationship, meaning the function aggregates multiple input records into one output value.

**Limits**

Realtime Compute for Apache Flink is subject to deployment environments and network environments. Therefore, when you develop Python UDFs, note the following limits: Only open-source Flink V1.12 and later are supported. The Flink cluster pre-installs Python 3.7.9. Therefore, you must develop code in Python 3.7.9. Flink runs in JDK 1.8. If your Python deployment depends on third-party JAR packages, make sure that the JAR packages are compatible with JDK 1.8. Only open-source Scala V2.11 is supported. If your Python deployment depends on thirdparty JAR packages, make sure that you use JAR package dependencies corresponding to Scala V2.11.

**Develop a UDAF**

QL reference

> **Note:** Flink provides Python UDX examples to help you quickly develop UDXs. These examples include implementations of Python ser-defined scalar functions (UDFs), Python UDAFs, and Python user-defined table-valued functions (UDTFs). This topic uses Windows as an example to describe how to develop a UDAF.

1. Download and decompress the python_demo-master example to your computer.
2. In PyCharm, click **file > open** to open the decompressed **python_demo-master**.
3. Double-click and open \python_demo-master\udx\udafs.py, then configure **udafs.py** as
needed. In this sample code, **weighted_avg** defines the code that calculates the weighted average of current and historical data.

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

A ZIP package named **python_demo.zip** appears in the \python_demo-master\ directory, indicating that you have completed the development of the Python UDAF. QL reference

**Register a UDAF**

For the UDFA registration process, see the Managing UDFs section in Alibaba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide.

**Use a UDAF**

After registering a UDAF, you can use the UDAF to perform the following steps:
1. Develop a Flink SQL draft. For more information, see the Develop a SQL draft section in Alib
aba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide. The following sample code obtains the weighted average of the current and historical data in field a of the ASI_UDAF_Source table, using field b as the weight.

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

This topic describes the limits, development, registration, and usage of Python user-defined table-valued functions (UDTFs).

**Definition**

A user-defined table-valued function (UDTF) accepts zero, one, or multiple scalar values as input parameters (which can be variable-length parameters). A table-valued function can return any number of rows as output, not just a single value. Each returned row can consist of one or more columns. One function call can produce multiple rows or columns of data. UDTFs are similar to user-defined scalar functions but differ in their output structure.

**Limits**

Realtime Compute for Apache Flink is subject to deployment environments and network environments. Therefore, when you develop Python UDFs, note the following limits: QL reference Only open-source Flink V1.12 and later are supported. The Flink cluster pre-installs Python 3.7.9. Therefore, you must develop code in Python 3.7.9. Flink runs in JDK 1.8. If your Python deployment depends on third-party JAR packages, make sure that the JAR packages are compatible with JDK 1.8. Only open-source Scala V2.11 is supported. If your Python deployment depends on thirdparty JAR packages, make sure that you use JAR package dependencies corresponding to Scala V2.11.

**Develop a UDTF**

> **Note:** Flink provides Python UDX examples to help you quickly develop UDXs. These examples include implementations of Python ser-defined scalar functions (UDFs), Python user- defined aggregate functions (UDAFs), and Python UDTFs. This topic uses Windows as an example to describe how to develop a UDTF.

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
1. Develop a Flink SQL draft. For more information, see the Develop a SQL draft section in Alib
aba Cloud Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide. The message field of each row in the ASI_UDTF_Source table is concatenated with the string "aa" with a pipe character (|), and then split into multiple column using a pipe character (|). The sample code is as follows: QL reference

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
INSERT INTO ASI_UDTF_Sink SELECT name,place FROM ASI_UDTF_Source,lateral table(split(concat_ws('|', `message`, 'aa'))) as T(name, place);
```

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

QL reference

**Input parameters**

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
LOAD MODULE `cluster-serving`; INSERT INTO ClusterServingOutput SELECT cluster_serving(uri, `data`) FROM ClusterSe rvingInput;
```

iii. Add the following configuration to the **Additional Configuration** section on the
**Advanced** tab of the job and to the **Additional Configuration** section on the Create
Session Cluster page, and then click **Save**.

```
pipeline.global-job-parameters: '"modelPath:""[Directory of your model file]"""'
```

QL reference modelPath indicates the OSS directory in which your model file is stored, such as oss://***/tf_auto/. iv. On the Deployments page, find the required job and click **Start** in the **Actions** column. Test results

| uri1 | data1 |
|---|---|
| 0.03932024,0.017788976,-2.2538425E- 4,0.021853039,0.030905273,0.052324444,0.053021688,0.08776 946,0.0625467,0.12149326,0.048770625,0.04533424,0.0927158 6,0.023119276,0.0037812046,0.052707616,0.029312208,0.0235 19568,0.07501668,0.037939064,0.06363185,0.04994791,0.0850 4477,0.06940596,0.052632406,0.028651983,0.02205597,0.0586 1686,0.040175162,0.04682718,0.05283319,0.01967535,0.11177 8766,0.03182444,0.04509241,0.09942829,0.009491239,0.03890 3005,0.11488753,0.019503327,0.0346709,0.060727723,0.03718 308,0.1295206,0.04292037,0.13272661,0.009957914,0.0503708 87,0.03016096,0.067269124,0.09981682,0.08606887,0.0851935 45,0.041775055,0.02956512,0.027142545,0.09836763,0.029330 501,0.040107135,0.0753366,0.068517864,0.020111244,0.08627 1614,0.04449262,0.107297346,0.07932708,0.036529146,0.0148 92701,0.08245985,0.04272034,0.076421194,0.035283472,0.028 554386,0.019374546,0.048012834,0.011391987,0.028220229,0. 054405782,0.037807927,0.085761145,0.07974813,0.04150249,- 0.017132144,0.08219319,0.019887058,0.034193676,0.0622105 1,0.07516215,0.0598385,0.09159884,0.038117558,0.05329266, 0.021038251,0.072046585,0.05561088,0.017538168,0.0256914 01,0.08580602,0.02225845,0.117060736,0.060743354,0.118408 88,0.065381594,0.08059649,0.045638822,0.06399781,0.011646 094,0.043574452,0.123603456,0.045708194,0.05672055,0.0840 2837,0.118181005,0.09657015,0.08259893,0.0010145458,0.031 954847,0.07388758,0.035380267,0.070080444,0.06764534,0.05 8731187,0.022044828,0.094359346,0.05559277,0.032255664,0. 07360537,0.11992536 | 128 |
