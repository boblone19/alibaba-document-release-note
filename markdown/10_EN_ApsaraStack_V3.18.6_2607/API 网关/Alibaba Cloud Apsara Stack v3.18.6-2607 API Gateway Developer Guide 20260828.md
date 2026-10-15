---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 API Gateway Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 367
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 API Gateway Developer Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/API%20%E7%BD%91%E5%85%B3/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20API%20Gateway%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 API Gateway Developer Guide 20260828

## Preparations

### Obtain API information and

**endpoints**

Obtain information about a product's open API operations, including the product name (code), API operation name, and API version.

**Background information**

The API information in the API directory of the Apsara Uni-manager Management Console is for reference only. For instructions on how to use a specific API, see the developer guide for the corresponding cloud product. If any inconsistencies exist, the information in the developer guide prevails.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top menu bar, choose **Products** > **Developer Tools** > **API & Tools** > **Developer**
**Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.
4. In the navigation pane on the left, select the target cloud product.
5. From the **Version** drop-down list, select the target API version.
6. In the API list, review the API operations for the current version.
7. Select the desired API operation. Obtain the POP Endpoint information for the cloud product,
which is displayed under the parameter name.

### Obtain an AccessKey

An AccessKey supports two authorization patterns: Resource Access Management (RAM) and Security Token Service (STS). You can use an AccessKey from either pattern to initiate a call. This topic describes how to obtain an AccessKey that uses RAM authorization.

**Background information**

An AccessKey uses an AccessKey ID and an AccessKey secret for symmetric encryption to authenticate the identity of a request sender. The AccessKey ID identifies the user, and the AccessKey secret is a string used to create an encrypted signature. The two authorization patterns for an AccessKey are: RAM authorization, which grants an AccessKey ID and an AccessKey secret to a third-party requester. STS authorization, which grants an AccessKey ID, an AccessKey secret, and a security token to a third-party requester. For more information, see Obtain an STS AccessKey. The Apsara Uni-manager Management Console provides individual AccessKeys and organization AccessKeys. Only operations administrators and primary organization administrators can obtain organization AccessKeys. You can use an individual account AccessKey to call the APIs of the Apsara Uni-manager Management Console and related cloud products. If you use an individual account AccessKey, you must add the following restrictive parameters to the header. Otherwise, a permission error may occur:

**Warning**

An individual account AccessKey is a restricted AccessKey managed by the permission system of the Apsara Uni-manager Management Console, whereas an organization AccessKey has broader permissions. Therefore, administrators must confirm the security of operations that use an organization AccessKey.

| Parameter | Description |
|---|---|
| x-acs-regionid | The region, such as cn-hangzhou-*. |
| x-acs-organizationid | The ID of the corresponding organization in the Apsara Uni-manager Management Console. For more information, see the GetOrganizationList topic in the Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the corresponding resource set in the Apsara Uni-manager Management Console. For more information, see the ListResourceGroup topic in the Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance on which you want to perform an operation. For example, you can find the instance ID of an ECS instance in the ECS instance list. |

**Obtain an individual account AccessKey**

To obtain an AccessKey for an individual account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the page, click your profile picture, and then click **Personal**
**Information**.
3. In the **AccessKey** section, view the AccessKey information for your individual account.

**Note**

The AccessKey ID and AccessKey secret are the keys to access your cloud resources and grant full permissions to your account. Keep them confidential.

**Obtain an organization AccessKey**

To obtain an organization AccessKey, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top menu bar, click **Enterprise**.
3. In the navigation pane on the left, choose **Resource Management > Organization**
**Management**.
4. In the organization chart, click the name of the target primary organization.
5. Click **Manage AccessKey**.
6. In the dialog box that appears, view the organization AccessKey information.

### Get common header

**parameters**

API calls require several header parameters. This topic describes how to obtain these parameters and explains the return values.

**Get the Region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top menu bar, click **Enterprise**.
3. In the navigation pane on the left, choose **Resource Management** > **Region**
**Management**.
4. Click the name of the target organization.
5. In the **Region List** on the right, find the **Region Name**. This value is the Region ID.

**Get the organization ID**

You can obtain the organization ID by calling an API. You can use the online API debugging feature in the Apsara Uni-manager Management Console to quickly obtain the organization ID.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top menu bar, click **Products**, and then choose **Developer Tools** > **APIs And**
**Tools** > **Developer Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.
4. Click the
button, choose **Cloud Platform** > **Unified Cloud Management Platform**, and set **Version** to **2019-05-10**.
5. In the text box, enter `GetOrganizationList` to start online debugging. For the name
parameter, enter the target organization name and make the call. If the call is successful, find the value of **id** in the **Call Result**. This value is the organization ID. For more information, see the GetOrganizationList chapter in the Apsara Uni-manager Management C onsole Development Guide.

**Get the resource group ID**

You can obtain the resource group ID by calling an API. You can use the online API debugging feature in the Apsara Uni-manager Management Console to quickly obtain the resource group ID.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top menu bar, click **Products**, and then choose **Developer Tools** > **APIs And**
**Tools** > **Developer Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.
4. Click the
button, choose **Cloud Platform** > **Unified Cloud Management Platform**, and set **Version** to **2019-05-10**.
5. In the text box, enter `ListResourceGroup` to start online debugging. If the call is
successful, find the value of **id** in the **Call Result**. This value is the resource group ID. For more information, see the ListResourceGroup chapter in the Apsara Uni-manager Managem ent Console Development Guide.

**Get the instance ID**

You can obtain the instance ID from the instance list of a cloud product in the Apsara Unimanager Management Console. This topic uses API Gateway as an example.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top menu bar, choose **Products** > **Middleware** > **Application Integration** > **API**
**Gateway**.
3. In the navigation pane on the left, click **Instance List**.
4. In the instance list, find the **Instance ID**.

**Return parameters**

When you call an API to list resource instances of a cloud product, the following parameters are returned by default.

| Name | Description |
|---|---|
| ResourceGroupName | The name of the resource group. |
| ResourceGroup | The ID of the resource group. |
| DepartmentName | The name of the organization. |

| Department | The ID of the organization. |
|---|---|

### Obtain an STS AccessKey

This topic describes how to use Security Token Service (STS) to call product APIs in Apsara Stack.

**Background information**

Alibaba Cloud Security Token Service (STS) is a service that provides temporary access permissions. You can use STS to call Apsara Stack product APIs.

**Procedure**

1. Obtain the `RAM Role` of the user role.
i. Log on to the Apsara Uni-manager Management Console. ii. In the upper-right corner of the page, click the profile picture and select **Personal**
**Information**.
iii. Click **View Current Role Policy**. In the **Current Role Policy** dialog box, you can view the `RAM Role` .
2. Use the following code and the `RAM Role` to obtain the `stsAK` , `stsSK` , and

```
 stsToken .
```

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
     // Specify the call source.
        asClient.setSdkSource("test");
     // Pass the ARN.
        String assumeRole = AssumeRole(asClient, "<RAM Role>");
        JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
        JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
        // Obtain the STS trituple.
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
        reqParams.put("AccessKeyId", <your_access_key_id>);
     // The AccessKey secret of the current user.
        reqParams.put("AccessKeySecret", <your_access_key_secret>);
        reqParams.put("roleSessionName", "StsUser");
        reqParams.put("roleArn", roleArn);
        return asClient.doRequest(endpoint, headers, reqParams);
```

`}`
3. Use the STS credentials to call product APIs, as shown in the following example.

```java
import com.aliyun.credentials.Client; import com.aliyun.credentials.models.Config; // The following example shows how to use an STS token to initialize the credential c lient. This example does not include the procedure for obtaining the STS token. public class DemoStsTest {
    public static void main(String[] args) {
        Config credentialConfig = new Config();
        credentialConfig.setType("sts");
        // Replace this with the AccessKeyId from the STS trituple obtained in the pr
evious step.
        credentialConfig.setAccessKeyId("your_AccessKeyId");
        // Replace this with the AccessKeySecret from the STS trituple obtained in th
e previous step.
        credentialConfig.setAccessKeySecret("your__AccessKeySecret");
        // Replace this with the SecurityToken from the STS trituple obtained in the
previous step.
        credentialConfig.setSecurityToken("your__SecurityToken");
        Client credentialClient = new Client(credentialConfig);
        // Continue to call the API. For more information, see the complete API docum
entation.
```

`}` `}`

### Obtain user and role

**information**

This topic describes how to obtain user and role information.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. Create a user.
i. In the top navigation bar, select **Enterprise**. ii. In the left-side navigation pane, select **User Management > User Management**. iii. On the **System Users** tab, click **Create User.** iv. In the **Create User** dialog box, configure the user information and click **OK**. For more information about configuration, see the **Apsara Uni-manager Management**
**Console User Guide > Create a user** section.
3. Create a role.
i. In the left-side navigation pane, select **Role-Based Access Control****> Role**
**Authorization**.
ii. Above the role list, click **Create Custom Role**. iii. Set **Basic Configurations** and click **Next**.
**Management scope**: Select **Resource set**.
iv. Set **Management Permission**. In the permission list, select the permissions for **View**
**RAM Service Roles** and **Create RAM Service Roles**, and then click **Next**.
v. Set **Application Permissions**. In the permission list, select **API Gateway** with **Read-**
**Only** and **Read and write permissions**, and then click **Next**.
vi. Set **Menu Permissions**. In the list, select **API Gateway** and click **Next** or **Create**.
4. Assign the role to the user.
i. In the left-side navigation pane, select **User Management > User Management**. ii. On the **System Users** tab, find the newly created user, click in the **Actions** column, and then select **Role Authorization**. iii. In the **Role Authorization** dialog box, add the newly created user role and click **OK**.
5. Add the user to a resource set.
i. On the **System Users** tab, find the newly created user and click the username. ii. On the **Resource Sets** tab, click **Join Resource Set** above the list. iii. In the **Join Resource Set** dialog box, select the user role from the **Select Role Type** drop-down list, select the resource sets to join in the **Select Resource Set** list, and then click **OK**.

### Obtain the region ID and

**organization ID**

This topic describes how to obtain the region ID and organization ID.

**Obtain the region ID**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Enterprise**.
3. **Resource Management > Region Management**.
4. In the left-side organizational structure, click the target organization. On the right side, find
the **Region List** and obtain the Region ID.

**Obtain the organization ID**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Product > Middleware > Application Integration >**
**API Gateway**.
3. In the left-side navigation pane, select **API Gateway > Instance list** or **AI Gateway**.
4. On the **Gateway Instance** page, open the developer tools, click the Network tab, and then
refresh the page.
5. In the search box, enter **ListResourceGroupByOrgId**. Click the API operation name. On
the Preview tab on the right, obtain the organization ID.

## Calling Apsara Stack APIs

**through a POP gateway**

### Java version

**Environment requirements**

Supports JDK 8 to JDK 19. The platform supports Linux, Mac, and Windows.

**Installation code**

Use the Maven dependency configuration:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <!-- Note: Use the version number specified in the developer documentation for your
Apsara Stack environment. -->
    <version>4.6.0</version>
</dependency> <dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.53</version>
</dependency>
```

**Installation documentation**

**Configuration instructions**

| Parameter | Description |
|---|---|
| regionId | The ID of the region. See Obtain the region ID and organization ID. |
| AccessKeyId | The AccessKey ID of the user. See Obtain an AccessKey. |
| AccessKeySecret | The AccessKey secret of the user. See Obtain an AccessKey. |
| endpoint | The endpoint for API access. See Obtain API information and endpoints. |

| organizationId | The ID of the organization. See Obtain the region ID and organization ID. |
|---|---|
| httpProxy | The proxy endpoint (optional). Contact Alibaba Cloud on-site personnel to obtain this information. |

**Code example**

The following example shows how to call an API Gateway console interface by using a common request:

```java
package com.aliyun.apsarastack; import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONArray; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.AcsResponse; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.HttpResponse; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; /**
 * Example of calling an API Gateway console interface by using a common request
```

`*/`

```java
public class Sample {
    private static IAcsClient client;
    // Define the API path.
    private static final String LIST_ROUTES = "/route/listRoutes";
    public static void main(String[] args) throws ClientException {
        listRoutes();
```

`}`

```
    /**
     * Example of querying a route list
```

`*/`

```java
    private static void listRoutes() throws ClientException {
        Map<String, Object> request = new HashMap<>();
        request.put("current", 1);
```

```java
        request.put("size", 10);
        request.put("gwInstanceId", "your_instance_id");
        CommonResponse response = getCommonResponse(request, LIST_ROUTES,
MethodType.POST);
        HttpResponse httpResponse = response.getHttpResponse();
        if (httpResponse.getStatus() == 200) {
            JSONObject jsonObject =
JSON.parseObject(httpResponse.getHttpContentString());
            if (Integer.parseInt(jsonObject.get("code").toString()) == 200) {
                Object data = jsonObject.get("data");
                if (data instanceof JSONObject) {
                    JSONObject dataObj = (JSONObject) data;
                    JSONArray records = (JSONArray) dataObj.get("records");
                    records.forEach(record -> {
                        System.out.println(JSON.toJSONString(record));
                    });
```

`}` `}`

```java
            System.out.println(jsonObject);
```

`}` `}`

```
    /**
     * Common request method
```

`*`

```
     * @param param Request parameters
     * @param path API path
     * @param methodType HTTP method type
     * @return Response result
     * @throws ClientException Client exception
```

`*/`

```
    public static CommonResponse getCommonResponse(Object param, String path, MethodTyp
e methodType) throws ClientException {
        CommonRequest request = new CommonRequest();
        request.setSysUriPattern(path);
        request.setHttpContent(JSONObject.toJSONBytes(param), "UTF-8",
FormatType.JSON);
        initDefaultHeader(request, methodType);
        return client.getCommonResponse(request);
```

`}`

```
    static {
        // Create a DefaultAcsClient instance and initialize it.
        DefaultProfile profile = DefaultProfile.getProfile(
                "<your-regionId>",      // The region ID.
                "<AccessKey ID>",        // The AccessKey ID.
                "<AccessKey Secret>");   // The AccessKey secret.
        // Optional: Configure a proxy.
        HttpClientConfig httpClientConfig = HttpClientConfig.getDefault();
        httpClientConfig.setHttpProxy("http://127.0.0.1:9898");
        profile.setHttpClientConfig(httpClientConfig);
```

```
        client = new DefaultAcsClient(profile);
```

`}`

```
    /**
     * Configure request headers.
```

`*`

```
     * @param request Request object
     * @param methodType HTTP method type
     * @param <T> Response type
```

`*/`

```java
    private static <T extends AcsResponse> void initDefaultHeader(CommonRequest request
, MethodType methodType) {
        // Required: Specify the caller. Typically, use the unique identifier of the ca
lling application.
        request.putHeadParameter("x-acs-caller-sdk-source", "your-app-name");
        // Required: Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional: Specify the resource group ID.
        // request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Optional: Specify the role ID.
        // request.putHeadParameter("x-acs-roleId", "<your-roleId>");
        // Set the request method.
        request.setSysMethod(methodType);
        // Set the cloud service endpoint.
        request.setSysDomain("<your-endpoint>");
        // Set LocationProduct.
        request.setSysProduct("csb-cop");
        // Set the API version.
        request.setSysVersion("2023-02-06");
```

`}` `}`

**Step examples**

1. . Initialize the client**
Create `DefaultProfile` and configure information such as the AccessKey ID, AccessKey secret, and endpoint:

```
DefaultProfile profile = DefaultProfile.getProfile(
        "<your-regionId>",      // The region ID.
        "<AccessKey ID>",        // The AccessKey ID.
        "<AccessKey Secret>");   // The AccessKey secret.
// Optional: Configure a proxy. HttpClientConfig httpClientConfig = HttpClientConfig.getDefault(); httpClientConfig.setHttpProxy("http://127.0.0.1:9898"); profile.setHttpClientConfig(httpClientConfig); IAcsClient client = new DefaultAcsClient(profile);
```

2. . Build request parameters**
Build a request parameter map based on the requirements of the specific API:

```
Map<String, Object> request = new HashMap<>(); request.put("current", 1); request.put("size", 10); request.put("gwInstanceId", "your_instance_id");
```

3. . Create a CommonRequest**
Set the request path, request body, and request method:

```
CommonRequest request = new CommonRequest(); request.setSysUriPattern("/route/listRoutes"); request.setHttpContent(JSONObject.toJSONBytes(param), "UTF-8", FormatType.JSON);
```

4. . Set request headers**
Set required header information:

```
request.putHeadParameter("x-acs-caller-sdk-source", "your-app-name"); request.putHeadParameter("x-acs-organizationid", "<your-organizationid>"); request.setSysMethod(MethodType.POST); request.setSysDomain("<your-endpoint>"); request.setSysProduct("csb-cop"); request.setSysVersion("2023-02-06");
```

5. . Send the request and process the response**

```java
CommonResponse response = client.getCommonResponse(request); HttpResponse httpResponse = response.getHttpResponse(); if (httpResponse.getStatus() == 200) {
    JSONObject jsonObject = JSON.parseObject(httpResponse.getHttpContentString());
    if (Integer.parseInt(jsonObject.get("code").toString()) == 200) {
        Object data = jsonObject.get("data");
        // Process the returned data.
        System.out.println(JSON.toJSONString(data));
```

`}` `}`
6. . Handle exceptions**

```java
try {
    CommonResponse response = client.getCommonRequest(request);
    // Process the response.
} catch (ClientException e) {
    // Handle client exceptions.
    System.out.println("ErrorCode: " + e.getErrCode());
    System.out.println("ErrorMessage: " + e.getErrMsg());
```

`}`

**Call method for self-managed ACK environments**

In a self-managed ACK environment, you do not need information such as the AccessKey pair or proxy. You can make calls directly through the endpoint of the console service.

**Obtain the console endpoint**

```bash
kubectl get svc -n <namespace where the console service resides>
```

Find the IP address of `cop-gateway-admin-svc` and use it as the endpoint.

**Code example**

```
static {
    // Create a DefaultAcsClient instance and initialize it.
    DefaultProfile profile = DefaultProfile.getProfile(
            "-",  // The region ID is not required.
            "-",  // The AccessKey ID is not required.
            "-"); // The AccessKey secret is not required.
    client = new DefaultAcsClient(profile);
```

`}`

```java
private static <T extends AcsResponse> void initDefaultHeader(CommonRequest request, Me thodType methodType) {
    // The authentication header specific to self-managed ACK environments.
    request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
    request.putHeadParameter("X-CSB-OPENAPI", "true");
    request.setSysMethod(methodType);
    request.setSysDomain("<IP address of the console service>");
    request.setSysProduct("csb-cop");
    request.setSysVersion("2023-02-06");
```

`}`

**Common API paths**

| Feature | API path |
|---|---|
| Query the instance list | /gatewayInstance/listInstances |
| Create a service | /microservice/createService |
| Query the route list | /route/listRoutes |
| Create a route | /route/createRoute |
| Query the domain name list | /domain/listDomains |

### Common API call methods

**Overview**

This document describes the common API call methods for the API Gateway console, including request format, response format, and authentication method. These methods apply to all interfaces of API Gateway (SCG) and AI Gateway (Higress).

**Basic interface information**

| Item | Description |
|---|---|
| Protocol | HTTP/HTTPS |
| Request method | POST (primary), GET |
| Data format | JSON |
| Character encoding | UTF-8 |
| Interface prefix | / |

**Unified request format**

**Request headers**

| Parameter | Required | Description |
|---|---|---|
| Content-Type | Yes | application/json . |
| Authorization | Yes | The user authentication token. |
| x-acs-request-id | No | The request trace ID for log tracing. |

**Request body**

All APIs use a JSON-formatted request body. The basic structure is as follows: `{`

```json
  "gwInstanceId": "xxx",
  ... // Other business parameters
```

`}`

**Note**

Most APIs require the gwInstanceId parameter to specify the gateway instance for the operation.

**Unified response format**

**Response structure**

| Parameter | Type | Description |
|---|---|---|
| requestId | String | The request trace ID. |
| code | Integer | The response status code. |
| msg | String | The response message. The system returns an error message if an error occurs. |
| data | Object | The response data, which is the business data. |

**Status code description**

| Status code | Description |
|---|---|
| 200 | The request succeeded. |
| 500 | The request failed due to a business exception. |
| 400 | The request parameters are invalid. |
| 401 | Unauthorized or authentication failed. |

**Successful response example**

`{`

```json
  "requestId": "abc****456",
  "code": 200,
  "msg": null,
  "data": {
    "routeId": "route-001",
    "routeName": "test-route"
```

`}` `}`

**Failed response example**

`{`

```json
  "requestId": "ab****f456",
  "code": 500,
  "msg": "Route not found",
  "data": null
```

`}`

**Paged response example**

`{`

```json
  "requestId": "ab****456",
  "code": 200,
  "msg": null,
  "data": {
    "size": 10,
    "current": 1,
    "total": 100,
    "records": [
      { "id": "1", "name": "item-1" },
      { "id": "2", "name": "item-2" }
```

`]` `}` `}`

**Authentication method**

**User authentication**

Pass the authentication token through the `Authorization` request header:

```
Authorization: Bearer <token>
```

Or use cookie-based authentication (for the web console).

**Consumer authentication (API call)**

When calling a gateway API, the consumer passes the API key in one of the following ways:

| Method | Description |
|---|---|
| Request header | Authorization: Bearer <api-key> or x- api-key: <api-key> . |
| Query parameter | ?api key=<api-key> . _ |

|   |   | Authorization: Bearer <api-key> |
|---|---|---|
|   | api-key: <api-key> |   |

The specific authentication method depends on the authentication configuration of the gateway instance.

**General parameter description**

**Gateway instance ID (gwInstanceId)**

Most APIs require the gateway instance ID to identify the target instance for the operation. The system automatically identifies the gateway type based on the instance ID and executes the corresponding processing logic.

**Pagination parameters**

List query APIs support the following pagination parameters:

| Parameter | Type | Default value | Description |
|---|---|---|---|
| current | Integer | 1 | The current page number. |
| size | Integer | 10 | The number of entries per page. |

**Search parameters**

List query APIs support the following search parameters:

| Parameter | Type | Description |
|---|---|---|
| searchName | String | The search keyword. The system performs a fuzzy match by name. |

**API overview**

**API Gateway APIs**

| Module | API path | Description |
|---|---|---|
| Route management | /route | Manage route configurations. |
| Service management | /service | Manage service registration. |
| Domain name management | /domain | Manage domain name bindings. |
| Consumer management | /app | Manage consumers and API keys. |
| Certificate management | /certificate | Manage SSL certificates. |

| Origin management | /source | Manage service origins. |
|---|---|---|
| Policy management | /strategy | Configure routing policies. |
| Policy configuration | /strategyConfig | Manage policy instances. |
| Instance management | /gatewayInstance | Manage gateway instances. |
| Cluster management | /k8sCluster | Manage Kubernetes clusters. |

**Error handling**

**Business exceptions**

When a business logic exception occurs, the system returns: `{`

```json
  "code": 500,
  "msg": "<error message>",
  "data": null
```

`}` Common business exceptions:

| Error message | Description |
|---|---|
| Route not found | The route does not exist. |
| Service not found | The service does not exist. |
| Permission denied | Insufficient permissions. |
| Instance not found | The gateway instance does not exist. |

**Parameter validation exceptions**

When request parameter validation fails, the system returns: `{`

```json
  "code": 500,
  "msg": "<field> <error message>",
  "data": null
```

`}` Example: `{`

```json
  "code": 500,
  "msg": "gwInstanceId must not be blank",
  "data": null
```

`}`

**Request examples**

**cURL example**

```json
# Create a route
curl -X POST 'http://localhost:8080/route/createRoute' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <token>' \
  -d '{
    "gwInstanceId": "instance-001",
    "routeName": "test-route",
    "path": "/api/test",
    "serviceId": "service-001"
```

`}'`

**HTTP request example**

```
POST /route/createRoute HTTP/1.1 Host: localhost:8080 Content-Type: application/json Authorization: Bearer <token>
```

`{`

```json
  "gwInstanceId": "instance-001",
  "routeName": "test-route",
  "path": "/api/test",
  "serviceId": "service-001"
```

`}`

**Best practice**

1. . Request tracing**
Always include a unique `x-acs-request-id` in the request header. The response returns the same requestId to facilitate log tracing and troubleshooting.
2. . Error handling**
Check the `code` field in the response to determine whether the request succeeded. `code=200` indicates success. Other values indicate failure. Obtain error messages from the `msg` field.
3. . Paged queries**
Use pagination parameters for list operations to avoid excessive data volume. Obtain the total number of records from the `total` field. Obtain the data for the current page from the `records` field.
4. . Instance differentiation**
Confirm the gateway type that corresponds to `gwInstanceId` before you perform an operation. Call `/gatewayInstance/getInstance` to query instance details and confirm the type.

#### API call - Cluster management

**Overview**

The cluster management module provides features to import, query, and update Kubernetes clusters. A cluster provides the deployment environment for gateway instances. The system supports two cluster types: self-managed Kubernetes clusters and ACK clusters.
**Applicable engines**: SCG / Higress
**API path prefix**: `/k8s`

**Authentication method**

**Self-managed ACK environment**: Add `X-CSB-TOKEN: csb@2022` and `X-CSB-OPENAPI:`
`true` to the request header.
**Enterprise Edition environment**: Add `x-acs-organizationid` and `x-acs-caller-sdk-`
`source` to the request header and use a valid AccessKey pair.

**Import a cluster**

**API description**

Import a Kubernetes cluster to the gateway console.

**Request information**

| Item | Content |
|---|---|
| URL | /k8s/importCluster |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ImportK8sClusterRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|

| k8sClusterName | String | Yes | The name of the cluster. The name must contain 2 to 128 characters and start with a letter. |
|---|---|---|---|
| k8sClusterType | String | No | The cluster type: self-built: Self- managed Kubernetes cluster container-service: ACK cluster |
| configContent | String | Conditional | The configuration content of the KubeConfig file. Note You must specify this parameter for self-managed clusters. |
| k8sClusterAttribute | Object | Conditional | The extended attributes of the cluster. Note You must specify this parameter for ACK clusters. |

**k8sClusterAttribute structure**

| Parameter | Type | Required |   | Description |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
| csClusterId | String | Conditional |   | The ID of the ACK cluster. Note You must specify this parameter when the type is container- service . |   |   |   |   |
|   |   |   |   |   |   | container- |   |   |
|   |   |   |   |   | service |   |   |   |

**Query the cluster list**

**API description**

Query the Kubernetes cluster list by page.

**Request information**

| Item | Content |
|---|---|
| URL | /k8s/listClusters |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ListK8sClusterRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| current | Integer | Yes | The current page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |

| clusterName | String | No | The name of the cluster. This parameter supports fuzzy search. |
|---|---|---|---|

**Query all clusters**

**API description**

Query the list of all Kubernetes clusters without pagination.

**Request information**

| Item | Content |
|---|---|
| URL | /k8s/getClusterList |
| Method | POST |
| Content-Type | application/json |

This API requires no request parameters.

**Update a cluster**

**API description**

Update the information of a Kubernetes cluster.

**Request information**

| Item | Content |
|---|---|
| URL | /k8s/updateCluster |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on UpdateK8sClusterRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| clusterCode | String | Yes | The cluster code. |
| k8sClusterAttribute | String | Yes | The extended attributes of the cluster (JSON string). |

**Cancel cluster import**

**API description**

Cancel the import of a Kubernetes cluster.

**Request information**

| Item | Content |
|---|---|
| URL | /k8s/cancelImportCluster |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on**

**CancelImportK8sClusterRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| k8sClusterCode | String | Yes | The cluster code. |

**Test the cluster connection**

**API description**

Test whether the Kubernetes cluster connection is normal.

**Request information**

| Item | Content |
|---|---|
| URL | /k8s/checkConnectCluster |

| Method | POST |
|---|---|
| Content-Type | application/json |

**Request parameters (based on**

**CheckK8sClusterConnectRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| clusterCode | String | Yes | The cluster code. |

**Query the cluster name**

**API description**

Query the cluster name by cluster code.

**Request information**

| Item | Content |
|---|---|
| URL | /k8s/getK8sClusterName |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on GetK8sClusterNameRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| clusterCode | String | Yes | The cluster code. |

**Query cluster information associated with an instance**

**API description**

Query the associated Kubernetes cluster information by instance ID.

**Request information**

| Item | Content |
|---|---|

| URL | /k8s/getK8sClusterInfoByGwInstanceId |
|---|---|
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on GetK8sClusterInfoRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common Request call examples**

The following examples show how to call the cluster management API by using the Common Request method. A self-managed ACK environment and an Enterprise Edition environment differ only in the authentication parameter settings.

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; public class ClusterApiDemo {
    // ========== Environment configuration (modify based on the actual environment) ==
========
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
        // ========== Import a self-managed Kubernetes cluster ==========
        String clusterCode = importSelfBuiltCluster(client);
```

```
        // ========== Import an ACK cluster ==========
        // String csClusterCode = importContainerServiceCluster(client);
        // ========== Test cluster connectivity ==========
        checkConnect(client, clusterCode);
        // ========== Query the cluster list ==========
        listClusters(client);
        // ========== Query all clusters ==========
        getClusterList(client);
        // ========== Query the cluster name ==========
        getK8sClusterName(client, clusterCode);
        // ========== Cancel cluster import ==========
        // cancelImportCluster(client, clusterCode);
```

`}`

```java
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
```

`}` `}`

```java
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
```

`}`

```java
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
```

`}` `}`

```java
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
```

`}`

```
    /**
     * Import a self-managed Kubernetes cluster (based on ImportK8sClusterRequest)
```

`*/`

```java
    private static String importSelfBuiltCluster(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("k8sClusterName", "my-self-built-cluster");         // [Required] Cl
uster name
        request.put("k8sClusterType", "self-built");                    // [Optional] Cl
uster type: self-built
        request.put("configContent", "your-kubeconfig-content");        // [Required] Ku
beConfig configuration
        CommonRequest commonRequest = createBaseRequest("/k8s/importCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String clusterCode = result.getString("data");
            System.out.println("importSelfBuiltCluster success, clusterCode: " +
clusterCode);
            return clusterCode;
        } else {
            System.out.println("importSelfBuiltCluster failed: " +
result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * Import an ACK cluster (based on ImportK8sClusterRequest)
```

`*/`

```java
    private static String importContainerServiceCluster(IAcsClient client) throws Excep
tion {
        Map<String, Object> attribute = new HashMap<>();
        attribute.put("csClusterId", "ce********b5587f5ec1c");  // [Required] ACK
cluster ID
        Map<String, Object> request = new HashMap<>();
        request.put("k8sClusterName", "my-cs-cluster");                  // [Required] C
luster name
        request.put("k8sClusterType", "container-service");              // [Required] C
luster type: container-service
        request.put("k8sClusterAttribute", attribute);                   // [Required] C
luster extended attributes
        CommonRequest commonRequest = createBaseRequest("/k8s/importCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
```

```java
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String clusterCode = result.getString("data");
            System.out.println("importContainerServiceCluster success, clusterCode: " +
clusterCode);
            return clusterCode;
        } else {
            System.out.println("importContainerServiceCluster failed: " +
result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * Query the cluster list (based on ListK8sClusterRequest)
```

`*/`

```java
    private static void listClusters(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("current", 1);                                       // [Required] Cu
rrent page number
        request.put("size", 10);                                         // [Required] Nu
mber of entries per page
        // request.put("clusterName", "");                                  // [Optional]
Cluster name (fuzzy search)
        CommonRequest commonRequest = createBaseRequest("/k8s/listClusters");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listClusters: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Query all clusters
```

`*/`

```java
    private static void getClusterList(IAcsClient client) throws Exception {
        CommonRequest commonRequest = createBaseRequest("/k8s/getClusterList");
        commonRequest.setHttpContent(new byte[0], "UTF-8", FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getClusterList: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Test cluster connectivity (based on CheckK8sClusterConnectRequest)
```

`*/`

```java
    private static void checkConnect(IAcsClient client, String clusterCode) throws Exce
ption{
```

```java
ption {
        Map<String, Object> request = new HashMap<>();
        request.put("clusterCode", clusterCode);                         // [Required]
Cluster code
        CommonRequest commonRequest = createBaseRequest("/k8s/checkConnectCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("checkConnectCluster: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Query the cluster name (based on GetK8sClusterNameRequest)
```

`*/`

```java
    private static void getK8sClusterName(IAcsClient client, String clusterCode) throws
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("clusterCode", clusterCode);                         // [Required]
Cluster code
        CommonRequest commonRequest = createBaseRequest("/k8s/getK8sClusterName");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getK8sClusterName: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Query the cluster information associated with an instance (based on
GetK8sClusterInfoRequest)
```

`*/`

```java
    private static void getK8sClusterInfoByGwInstanceId(IAcsClient client, String gwIns
tanceId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // [Required] G
ateway instance ID
        CommonRequest commonRequest =
createBaseRequest("/k8s/getK8sClusterInfoByGwInstanceId");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getK8sClusterInfoByGwInstanceId: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Update a cluster (based on UpdateK8sClusterRequest)
```

`*/` `/`

```java
    private static void updateCluster(IAcsClient client, String clusterCode) throws Exc
eption {
        Map<String, Object> request = new HashMap<>();
        request.put("clusterCode", clusterCode);                         // [Required]
Cluster code
        request.put("k8sClusterAttribute", "{\"key\":\"value\"}");       // [Required]
Cluster extended attributes in JSON format
        CommonRequest commonRequest = createBaseRequest("/k8s/updateCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("updateCluster: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Cancel cluster import (based on CancelImportK8sClusterRequest)
```

`*/`

```java
    private static void cancelImportCluster(IAcsClient client, String clusterCode) thro
ws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("k8sClusterCode", clusterCode);                      // [Required] C
luster code
        CommonRequest commonRequest = createBaseRequest("/k8s/cancelImportCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("cancelImportCluster: " +
response.getHttpResponse().getHttpContentString());
```

`}` `}`

**Cluster type description**

| k8sClusterType | Description |
|---|---|
| self-built | Self-managed Kubernetes cluster. You must provide the KubeConfig. |
| container-service | ACK cluster. You must provide the cluster ID. |

**Response code description**

| 3 | > Document Version: 2026082 |
|---|---|

| Code | Description |
|---|---|
| 200 | The request succeeded. |
| 400 | The request contains invalid parameters. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

#### API call - Origin management

**Overview**

The origin management module provides functions to create, delete, modify, and query service registration centers. Origins are used for service discovery. SCG supports four origin types: Nacos, microservice namespace (EDAS), Eureka, and Database.
**Applicable engine**: SCG (API Gateway)
**API path prefix**: `/source`

**Authentication method**

**Self-managed ACK environment**: Add `X-CSB-TOKEN: csb@2022` and `X-CSB-OPENAPI:`
`true` to the request header.
**Enterprise Edition environment**: Add `x-acs-organizationid` and `x-acs-caller-sdk-`
`source` to the request header, and use a valid AK/SK pair.

**Create an origin**

**API description**

Create an origin for a service registry.

**Request information**

| Item | Content |
|---|---|
| URL | /source/createSource |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| sourceName | String | Yes | The name of the origin. |
| sourceType | Integer | Yes | The type of the origin: 1: Nacos 2: Microservice space (EDAS) 3: Eureka 5: Database |
| description | String | No | The description of the origin. |
| sourceStruct | Object | Yes | The configuration structure of the origin. Note The configuration structure varies depending on the origin type. |

**sourceStruct configurations for different origin types**

**Nacos (sourceType=1):**

| Parameter | Type | Required | Description |
|---|---|---|---|
| nacosRegistry | String | Yes | The endpoint of the Nacos registry. |
| nacosNamespaceId | String | Yes | The ID of the Nacos namespace. |
| nacosGroupName | String | No | The name of the Nacos group. Default value: DEFAULT GROUP. _ |

| nacosAccessKey | String | No | The AccessKey for Nacos authentication. |
|---|---|---|---|
| nacosSecretKey | String | No | The SecretKey for Nacos authentication. |
| checkType | Integer | No | The validation type: 0: No validation 1: Validate connection |

**Microservice namespace/EDAS (sourceType=2):**

| Parameter | Type | Required | Description |
|---|---|---|---|
| edasNameSpaceId | String | Yes | The ID of the EDAS namespace. |
| type | Integer | Yes | The type: 0: Nacos (DNCS) 1: ConfigServer (DNCS) |
| edasEndPoint | String | Conditional | The endpoint of EDAS. Note This parameter is required in address server mode. |
| edasServerAddr | String | Conditional | The server address of EDAS. Note This parameter is required in direct connection mode. |
| edasAccessKey | String | Yes | The AccessKey of EDAS. |
| edasSecretKey | String | Yes | The SecretKey of EDAS. |

**Eureka (sourceType=3):**

| Parameter | Type | Required | Description |
|---|---|---|---|
| eurekaRegistry | String | Yes | The endpoint of the Eureka registration center. |
| checkType | Integer | No | The verification type: 0: No verification 1: Verify connection |

**Database (sourceType=5):**

| Parameter | Type | Required | Description |
|---|---|---|---|
| databaseType | Integer | Yes | The type of the database: 0: MySQL 1: PostgreSQL |
| jdbcUrl | String | Yes | The JDBC connection string. |
| username | String | Yes | The username for the database. |
| password | String | Yes | The password for the database. |
| maxConnection | Integer | No | The maximum number of connections. |
| maxIdleConnection | Integer | No | The maximum number of idle connections. |
| connectionIdleTime | Integer | No | The idle time of a connection, in seconds. |

**Query the origin list**

**API description**

Query origins by page.

**Request information**

| Item | Content |
|---|---|
| URL | /source/listSources |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The current page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |
| sourceName | String | No | The name of the origin. Fuzzy search is supported. |
| sourceType | Integer | No | The filter condition for the origin type. |

**Query origin details**

**API description**

Query detailed information by origin ID.

**Request information**

| Item | Content |
|---|---|
| URL | /source/getSource |
| Method | POST |

| Content-Type | application/json |
|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| sourceId | String | Yes | The ID of the origin. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify origin**

**API description**

Modify an existing origin configuration.

**Request information**

| Item | Content |
|---|---|
| URL | /source/modifySource |
| Method | POST |
| Content-Type | application/json |

Same as the parameters for creating an origin. You must also specify `sourceId` .

**Delete origin**

**API description**

Delete the specified origin.

**Request information**

| Item | Content |
|---|---|
| URL | /source/deleteSource |
| Method | POST |

| Content-Type | application/json |
|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| sourceId | String | Yes | The ID of the origin. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common Request call examples**

The following examples show how to call the Origin Management API by using the Common Request method. The difference between a self-managed ACK environment and an Enterprise Edition environment lies only in the authentication settings.

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; public class SourceApiDemo {
    // ========== Environment configuration (modify according to actual environment) ==
========
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
        // ========== Create Nacos origin ==========
        String nacosSourceId = createNacosSource(client);
```

```
        // ========== Create EDAS namespace origin ==========
        // String edasSourceId = createEdasSource(client);
        // ========== Create Eureka origin ==========
        // String eurekaSourceId = createEurekaSource(client);
        // ========== Create Database origin ==========
        // String dbSourceId = createDatabaseSource(client);
        // ========== List origins ==========
        listSources(client);
        // ========== Get origin details ==========
        getSource(client, nacosSourceId);
        // ========== Modify origin ==========
        modifySource(client, nacosSourceId);
        // ========== Delete origin ==========
        deleteSource(client, nacosSourceId);
```

`}`

```java
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
```

`}` `}`

```java
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
```

`}`

```java
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
```

`}` `}`

```java
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
```

```
        setAuthHeaders(request);
        return request;
```

`}`

```
    /**
     * Create Nacos origin
```

`*/`

```java
    private static String createNacosSource(IAcsClient client) throws Exception {
        // Nacos configuration structure
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("nacosRegistry", "http://nacos-server:8848");       // 【Requir
ed】Nacos registration center address
        sourceStruct.put("nacosNamespaceId", "public");                      // 【Require
d】Nacos namespace ID
        sourceStruct.put("nacosGroupName", "DEFAULT_GROUP");                 //
【Optional】Nacos group name
        // sourceStruct.put("nacosAccessKey", "");                             // 【Optio
nal】Nacos authentication AccessKey
        // sourceStruct.put("nacosSecretKey", "");                             // 【Optio
nal】Nacos authentication SecretKey
        sourceStruct.put("checkType", 0);                                    //
【Optional】Validation type: 0-no validation
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("sourceName", "my-nacos-source");                       // 【Required
】Origin name
        request.put("sourceType", 1);                                       // 【Required
】Origin type: 1-NACOS
        request.put("sourceStruct", sourceStruct);                          // 【Required
】Origin configuration structure
        request.put("description", "Nacos service registry");               //
【Optional】Origin description
        CommonRequest commonRequest = createBaseRequest("/source/createSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String sourceId = result.getString("data");
            System.out.println("createNacosSource success, sourceId: " + sourceId);
            return sourceId;
        } else {
            System.out.println("createNacosSource failed: " + result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
```

```
     * Create EDAS namespace origin
```

`*/`

```java
    private static String createEdasSource(IAcsClient client) throws Exception {
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("edasNameSpaceId", "edas-ns-xxx");                  //
【Required】EDAS namespace ID
        sourceStruct.put("type", 0);                                         //
【Required】Type: 0-Nacos(DNCS), 1-ConfigServer(DNCS)
        sourceStruct.put("edasEndPoint", "edas-endpoint.aliyuncs.com");      // 【Condit
ionally required】EDAS Endpoint
        sourceStruct.put("edasServerAddr", "edas-server_addr");              //
【Conditionally required】EDAS server address
        sourceStruct.put("edasAccessKey", "your-edas-ak");                   //
【Required】EDAS AccessKey
        sourceStruct.put("edasSecretKey", "your-edas-sk");                   //
【Required】EDAS SecretKey
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("sourceName", "my-edas-source");
        request.put("sourceType", 2);                                       // 【Required
】Origin type: 2-EDAS namespace
        request.put("sourceStruct", sourceStruct);
        CommonRequest commonRequest = createBaseRequest("/source/createSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String sourceId = result.getString("data");
            System.out.println("createEdasSource success, sourceId: " + sourceId);
            return sourceId;
        } else {
            System.out.println("createEdasSource failed: " + result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * Create Eureka origin
```

`*/`

```java
    private static String createEurekaSource(IAcsClient client) throws Exception {
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("eurekaRegistry", "http://eureka-server:8761/eureka/");  // 【R
equired】Eureka registration center address
        sourceStruct.put("checkType", 0);                                    //
【Optional】Validation type
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
reqestpt("sorceName"
```

`"m`

```
erekasorce")
```

```java
        request.put("sourceName", "my-eureka-source");
        request.put("sourceType", 3);                                       // 【Required
】Origin type: 3-Eureka
        request.put("sourceStruct", sourceStruct);
        CommonRequest commonRequest = createBaseRequest("/source/createSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String sourceId = result.getString("data");
            System.out.println("createEurekaSource success, sourceId: " + sourceId);
            return sourceId;
        } else {
            System.out.println("createEurekaSource failed: " +
result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * Create Database origin
```

`*/`

```java
    private static String createDatabaseSource(IAcsClient client) throws Exception {
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("databaseType", 0);                                 // 【Require
d】Database type: 0-MySQL, 1-PostgreSQL
        sourceStruct.put("jdbcUrl", "jdbc:mysql://mysql-server:3306/mydb");  // 【Requir
ed】JDBC connection URL
        sourceStruct.put("username", "db_user");                             // 【Require
d】Database username
        sourceStruct.put("password", "db_password");                         // 【Require
d】Database password
        // sourceStruct.put("maxConnection", 100);                             // 【Optio
nal】Maximum connections
        // sourceStruct.put("maxIdleConnection", 20);                          // 【Optio
nal】Maximum idle connections
        // sourceStruct.put("connectionIdleTime", 300);                        // 【Optio
nal】Connection idle time (seconds)
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("sourceName", "my-database-source");
        request.put("sourceType", 5);                                       // 【Required
】Origin type: 5-Database
        request.put("sourceStruct", sourceStruct);
        CommonRequest commonRequest = createBaseRequest("/source/createSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
```

```java
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String sourceId = result.getString("data");
            System.out.println("createDatabaseSource success, sourceId: " + sourceId);
            return sourceId;
        } else {
            System.out.println("createDatabaseSource failed: " +
result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * List origins
```

`*/`

```java
    private static void listSources(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("current", 1);                                          // 【Required
】Current page number
        request.put("size", 10);                                            // 【Required
】Number of items per page
        // request.put("sourceName", "");                                     //
【Optional】Origin name (fuzzy search)
        // request.put("sourceType", 1);                                      //
【Optional】Origin type filter
        CommonRequest commonRequest = createBaseRequest("/source/listSources");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listSources: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Get origin details
```

`*/`

```java
    private static void getSource(IAcsClient client, String sourceId) throws Exception
```

`{`

```
        Map<String, Object> request = new HashMap<>();
        request.put("sourceId", sourceId);                                  // 【Required
】Origin ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/source/getSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
```

`yp`

```java
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getSource: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Modify origin
```

`*/`

```java
    private static void modifySource(IAcsClient client, String sourceId) throws Excepti
on {
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("nacosRegistry", "http://nacos-server:8848");
        sourceStruct.put("nacosNamespaceId", "public");
        sourceStruct.put("checkType", 0);
        Map<String, Object> request = new HashMap<>();
        request.put("sourceId", sourceId);                                  // 【Required
】Origin ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("sourceName", "my-nacos-source-modified");              //
【Required】Origin name
        request.put("sourceType", 1);                                       // 【Required
】Origin type
        request.put("sourceStruct", sourceStruct);                          // 【Required
】Origin configuration structure
        CommonRequest commonRequest = createBaseRequest("/source/modifySource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifySource: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Delete origin
```

`*/`

```java
    private static void deleteSource(IAcsClient client, String sourceId) throws Excepti
on {
        Map<String, Object> request = new HashMap<>();
        request.put("sourceId", sourceId);                                  // 【Required
】Origin ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/source/deleteSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteSource: " +
```

```
response.getHttpResponse().getHttpContentString());
```

`}` `}`

**Origin type description (SCG)**

| sourceType | Type name | Description |
|---|---|---|
| 1 | Nacos | The Nacos registration center. |
| 2 | EDAS namespace | The EDAS microservice namespace. |
| 3 | Eureka | The Eureka registration center. |
| 5 | Database | The database origin (MySQL/PostgreSQL). |

**Database type description**

| databaseType | Type name | Description |
|---|---|---|
| 0 | MySQL | The MySQL database. |
| 1 | PostgreSQL | The PostgreSQL database. |

**Response code description**

| code | Description |
|---|---|
| 200 | The operation succeeded. |
| 400 | A parameter error occurred. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

#### API call - Service management

**Overview**

The service management module provides features to create, delete, modify, and query backend services. A service is the target of route forwarding. It can be a static node, a discovered service, or an imported service.
**Applicable engine**: SCG / Higress (The API is engine-agnostic and works universally.)
**API path prefix**: `/microservice/**`

**Authentication method**

**Self-managed ACK environment**: Add `X-CSB-TOKEN: csb@2022` and `X-CSB-OPENAPI:`
`true` to the request header.
**Enterprise Edition environment**: Add `x-acs-organizationid` and `x-acs-caller-sdk-`
`source` to the request header, and use a valid AccessKey pair.

**Create a service**

**API description**

Create a new backend service.

**Request information**

| Item | Content |
|---|---|
| URL | /microservice/createService |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on CreateMicroserviceRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| name | String | Yes | The name of the service (identifier in the gateway). |
| upstreamType | Integer | Yes | The upstream type: 1: Static node 2: Service discovery 3: Service import |

| loadBalanceType | Integer | Yes | The load balancing type (see description below). |
|---|---|---|---|
| protocol | String | Yes | The protocol: HTTP GRPC Webservice Dubbo HSF |
| serviceStruct | Object | Yes | The service structure configuration (see detailed description below). |
| serviceType | Integer | No | The service type: 0: RPC service 1: Database Note Default value is 0. |
| description | String | No | The description of the service. |
| serviceName | String | Conditional | The name of the service registered in the registration center. Note Use this parameter for service discovery. |
| serviceSourceType | Integer | Conditional | The source type. Note Use this parameter for service discovery. |
| isOpenHealthCheck | Boolean | No | Specifies whether to enable health check. |

| healthCheckStruct | HealthCheckStruct | No | The health check configuration (SCG). |
|---|---|---|---|
| activeHealthCheckStru ct | ActiveHealthCheckStru ct | No | The active health check configuration (Higress). |
| proxyServerName | String | No | The name of the proxy server. |
| isDisasterRecovery | Boolean | No | Specifies whether the service is for disaster recovery. Default value is false. |

**Load balancing type description (based on**

**LoadBalanceTypeEnum)**

| Value | Type name | Description | Applicable scenario |
|---|---|---|---|
| 1 | WEIGHT ROUND ROBI _ _ N | Weighted round-robin. | Static nodes only |
| 2 | WEIGHT RANDOM _ | Weighted random. | Static nodes only |
| 3 | ROUND ROBIN _ | Round robin. | General-purpose |
| 4 | RANDOM | Random. | General-purpose |
| 5 | LEAST REQUEST _ | Least requests. | Higress Nacos |
| 6 | CONSISTENT HASH _ | Consistent hash. | Higress Nacos |
| 7 | LEAST CONN _ | Least connections. | Higress Nacos |

**serviceStruct configuration description**

**Static node (upstreamType=1):**

`{`

```json
    "nodes": [
```

`{`

```json
            "ip": "192***.*.100",     // Required. The IP address of the node.
            "port": 8080,              // Required. The port.
            "weight": 100,             // Optional. The weight. Default value is 100.
            "enable": true             // Optional. Specifies whether to enable the node
. Default value is true.
```

`}` `]` `}`

**Nacos service discovery (upstreamType=2):**

`{`

```json
    "nacosNamespaceId": "public",      // Required. The ID of the Nacos namespace.
    "nacosGroupName": "DEFAULT_GROUP"  // Optional. The name of the Nacos group.
```

`}`

**HealthCheckStruct structure (SCG health check)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| type | int | Yes | The type of the health check. |
| healthPath | String | Yes | The path for the health check. |
| httpStatuses | String | Yes | The HTTP status codes indicating health, such as "200, 301". |
| timeout | int | Yes | The request timeout in seconds. |
| healthInterval | int | Yes | The interval between health checks in seconds. |
| unHealthInterval | int | Yes | The interval between unhealthy checks in seconds. |
| httpSuccesses | int | Yes | The success threshold. |
| httpFailures | int | Yes | The failure threshold. |

**ActiveHealthCheckStruct structure (Higress active health**

**check)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| enable | Boolean | Yes | Specifies whether to enable the feature. |
| protocol | String | Yes | The protocol. Valid values: http tcp |
| timeout | Integer | Yes | The timeout period in seconds. |
| interval | Integer | Yes | The interval between health checks in seconds. |
| healthyThreshold | Integer | Yes | The healthy threshold. |
| unhealthyThreshold | Integer | Yes | The unhealthy threshold. |
| httpPath | String | Conditional | The HTTP health check path. Note Configure this parameter when protocol=http . |
| httpHost | String | No | The host for the HTTP health check. |
| expectedStatuses | List | Conditional | The expected status codes, such as ["200", "301"]. |

|   |   |   | protocol=http |
|---|---|---|---|

**Query the list of services**

**API description**

Query the list of services by page.

**Request information**

| Item | Content |
|---|---|
| URL | /microservice/listServices |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on**

**GatewayServiceListByPageRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The current page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |
| serviceName | String | No | The service name. Fuzzy search is supported. |
| serviceId | String | No | The service ID. Exact match is required. |
| sourceName | String | No | The name of the source. |
| isDisasterRecovery | Boolean | No | Specifies whether to filter disaster recovery services. |
| sourceTypeList | List | No | The list of source types. |
| provider | String | No | The provider of the AI gateway. |

**Query service details**

**API description**

Query the detailed information of a service by its service ID.

**Request information**

| Item | Content |
|---|---|
| URL | /microservice/getService |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| serviceId | String | Yes | The ID of the service. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify a service**

**API description**

Modify an existing service configuration.

**Request information**

| Item | Content |
|---|---|
| URL | /microservice/modifyService |
| Method | POST |
| Content-Type | application/json |

The parameters are the same as those for creating a service. You must also specify

```
 serviceId .
```

**Modify service nodes**

**API description**

Modify the node configuration of a service individually.

**Request information**

| Item | Content |
|---|---|
| URL | /microservice/modifyNode |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on UpdateNodeRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| serviceId | String | Yes | The ID of the service. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| nodes | List | Yes | The list of nodes. |

**Delete a service**

**API description**

Delete a specified service.

**Request information**

| Item | Content |
|---|---|
| URL | /microservice/deleteService |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| serviceId | String | Yes | The ID of the service. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Delete services in batches**

**API description**

Delete multiple services in batches.

**Request information**

| Item | Content |
|---|---|
| URL | /microservice/batchDeleteService |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| serviceIds | List | Yes | The list of service IDs. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**List all services**

**API description**

List all services under the gateway instance (without pagination).

**Request information**

| Item | Content |
|---|---|
| URL | /microservice/listAllServices |

| Method | POST |
|---|---|
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| serviceType | Integer | No | The filter for service type. |

**Common Request call examples**

The following examples show how to call the service management API by using the Common Request method. The difference between a self-managed ACK environment and an Enterprise Edition environment lies only in the authentication parameter settings.

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.ArrayList; import java.util.Arrays; import java.util.HashMap; import java.util.List; import java.util.Map; public class ServiceApiDemo {
    // ========== Environment configuration (modify according to actual environment) ==
========
    // Self-managed ACK environment configuration
    private static final boolean IS_SELF_HOSTED = true;                     // Whether i
t is a self-managed ACK environment
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";    // Self-man
aged ACK console address
    // Enterprise Edition environment configuration (used when IS_SELF_HOSTED = false)
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
```

`i` `i` `fi` `l``S` `i`

```
CCSS
```

`"` `k`

```
id"
```

```java
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
    // Gateway instance ID
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
        // ========== Create fixed-node service ==========
        String serviceId = createFixedNodeService(client);
        // ========== Create Nacos service discovery service ==========
        // String nacosServiceId = createNacosService(client);
        // ========== List services ==========
        listServices(client);
        // ========== Get service details ==========
        getService(client, serviceId);
        // ========== Modify service ==========
        modifyService(client, serviceId);
        // ========== Delete service ==========
        deleteService(client, serviceId);
```

`}`

```
    /**
     * Create client (common for self-managed ACK and Enterprise Edition)
```

`*/`

```java
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
```

`}` `}`

```java
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
```

`}`

```java
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
```

`}` `}` `}`

```java
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
```

`}`

```
    /**
     * Create fixed-node service
```

`*/`

```java
    private static String createFixedNodeService(IAcsClient client) throws Exception {
        // Node configuration (based on Node structure)
        Map<String, Object> node = new HashMap<>();
        node.put("ip", "192.***.*.100");                                    // [Required]
Node IP address
        node.put("port", 8080);                                             // [Required]
Port
        node.put("weight", 100);                                            // [Optional]
Weight, default is 100
        node.put("enable", true);                                           // [Optional]
Whether enabled, default is true
        // Service structure configuration
        Map<String, Object> serviceStruct = new HashMap<>();
        serviceStruct.put("nodes", Arrays.asList(node));
        // Create request (based on CreateMicroserviceRequest)
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        request.put("name", "service-demo-01");                             // [Required]
Service name (identifier in gateway)
        request.put("upstreamType", 1);                                     // [Required]
Upstream type: 1 - fixed node
        request.put("loadBalanceType", 3);                                  // [Required]
Load balancing type: 3 - round robin
        request.put("protocol", "HTTP");                                    // [Required]
Protocol
        request.put("serviceStruct", serviceStruct);                        //
[Required] Service structure configuration
        request.put("serviceType", 0);                                      // [Optional]
Service type: 0 - RPC service
        request.put("description", "demo backend service");                 //
[Optional] Service description
        request.put("isOpenHealthCheck", false);                            // [Optional]
Whether health check is enabled
        CommonRequest commonRequest = createBaseRequest("/microservice/createService");
```

`Co` `o`

```
equestco
```

`o`

```java
equest ceateBaseequest(/ cose ce/ceateSe ce);
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String serviceId = result.getString("data");
            System.out.println("createFixedNodeService success, serviceId: " +
serviceId);
            return serviceId;
        } else {
            System.out.println("createFixedNodeService failed: " +
result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * Create Nacos service discovery service
```

`*/`

```java
    private static String createNacosService(IAcsClient client) throws Exception {
        // Nacos service structure configuration
        Map<String, Object> serviceStruct = new HashMap<>();
        serviceStruct.put("nacosNamespaceId", "public");                    //
[Required] Nacos namespace ID
        serviceStruct.put("nacosGroupName", "DEFAULT_GROUP");               // [Optional
] Nacos group name
        // Create request
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        request.put("name", "service-nacos-demo");                          //
[Required] Service name
        request.put("upstreamType", 2);                                     // [Required]
Upstream type: 2 - service discovery
        request.put("loadBalanceType", 3);                                  // [Required]
Load balancing type
        request.put("protocol", "HTTP");                                    // [Required]
Protocol
        request.put("serviceName", "user-service");                         //
[Required] Service name in registry
        request.put("serviceSourceType", 1);                                // [Required]
Source type: 1 - NACOS
        request.put("sourceId", "nacos-source-id");                         //
[Required] Source ID
        request.put("serviceStruct", serviceStruct);                        //
[Required] Service structure configuration
        CommonRequest commonRequest = createBaseRequest("/microservice/createService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
```

```java
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String serviceId = result.getString("data");
            System.out.println("createNacosService success, serviceId: " + serviceId);
            return serviceId;
        } else {
            System.out.println("createNacosService failed: " +
result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * Create service with health check
```

`*/`

```java
    private static String createServiceWithHealthCheck(IAcsClient client) throws Except
ion {
        // Node configuration
        Map<String, Object> node = new HashMap<>();
        node.put("ip", "192.168.1.100");
        node.put("port", 8080);
        node.put("weight", 100);
        node.put("enable", true);
        Map<String, Object> serviceStruct = new HashMap<>();
        serviceStruct.put("nodes", Arrays.asList(node));
        // SCG health check configuration (based on HealthCheckStruct)
        Map<String, Object> healthCheckStruct = new HashMap<>();
        healthCheckStruct.put("type", 0);                                   // [Required]
Check type
        healthCheckStruct.put("healthPath", "/health");                     //
[Required] Check path
        healthCheckStruct.put("httpStatuses", "200,301");                   //
[Required] Healthy status codes
        healthCheckStruct.put("timeout", 5);                                // [Required]
Request timeout (seconds)
        healthCheckStruct.put("healthInterval", 30);                        //
[Required] Health check interval (seconds)
        healthCheckStruct.put("unHealthInterval", 60);                      //
[Required] Unhealthy check interval (seconds)
        healthCheckStruct.put("httpSuccesses", 3);                          //
[Required] Success threshold
        healthCheckStruct.put("httpFailures", 3);                           //
[Required] Failure threshold
        // Higress active health check configuration (based on ActiveHealthCheckStruct)
        // Map<String, Object> activeHealthCheckStruct = new HashMap<>();
        // activeHealthCheckStruct.put("enable", true);                       //
[Required] Whether enabled
```

```java
        // activeHealthCheckStruct.put("protocol", "http");                   // [Requir
ed] Protocol
        // activeHealthCheckStruct.put("timeout", 5);                         //
[Required] Timeout (seconds)
        // activeHealthCheckStruct.put("interval", 30);                       //
[Required] Check interval (seconds)
        // activeHealthCheckStruct.put("healthyThreshold", 3);                // [Requir
ed] Healthy threshold
        // activeHealthCheckStruct.put("unhealthyThreshold", 3);              // [Requir
ed] Unhealthy threshold
        // activeHealthCheckStruct.put("httpPath", "/health");                // [Requir
ed] HTTP check path
        // activeHealthCheckStruct.put("expectedStatuses", Arrays.asList("200",
"301")); // [Required] Expected status codes
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("name", "service-health-check");
        request.put("upstreamType", 1);
        request.put("loadBalanceType", 3);
        request.put("protocol", "HTTP");
        request.put("serviceStruct", serviceStruct);
        request.put("isOpenHealthCheck", true);                             // [Required]
Enable health check
        request.put("healthCheckStruct", healthCheckStruct);                // [Required
] Health check configuration
        CommonRequest commonRequest = createBaseRequest("/microservice/createService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String serviceId = result.getString("data");
            System.out.println("createServiceWithHealthCheck success, serviceId: " +
serviceId);
            return serviceId;
        } else {
            System.out.println("createServiceWithHealthCheck failed: " +
result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * List services (based on GatewayServiceListByPageRequest)
```

`*/`

```java
    private static void listServices(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
```

`//`

```java
        request.put("current", 1);                                          // [Required]
Current page number
        request.put("size", 10);                                            // [Required]
Number of entries per page
        // request.put("serviceName", "");                                    // [Optiona
l] Service name (fuzzy search)
        // request.put("serviceId", "");                                      // [Optiona
l] Service ID (exact search)
        // request.put("isDisasterRecovery", false);                          //
[Optional] Filter by whether it is a disaster recovery service
        CommonRequest commonRequest = createBaseRequest("/microservice/listServices");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listServices: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Get service details
```

`*/`

```java
    private static void getService(IAcsClient client, String serviceId) throws Exceptio
n {
        Map<String, Object> request = new HashMap<>();
        request.put("serviceId", serviceId);                                // [Required]
Service ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/microservice/getService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getService: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Modify service
```

`*/`

```java
    private static void modifyService(IAcsClient client, String serviceId) throws Excep
tion {
        Map<String, Object> node = new HashMap<>();
        node.put("ip", "192.***.*.101");
        node.put("port", 8081);
        node.put("weight", 100);
        node.put("enable", true);
        Map<String, Object> serviceStruct = new HashMap<>();
        serviceStruct.put("nodes", Arrays.asList(node));
Map<String Object>request=newHashMap<>();
```

```java
        Map<String, Object> request = new HashMap<>();
        request.put("serviceId", serviceId);                                // [Required]
ID of the service to modify
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        request.put("name", "service-demo-modified");                       //
[Required] Service name
        request.put("upstreamType", 1);                                     // [Required]
Upstream type
        request.put("loadBalanceType", 1);                                  // [Required]
Load balancing type
        request.put("protocol", "HTTP");                                    // [Required]
Protocol
        request.put("serviceStruct", serviceStruct);                        //
[Required] Service structure configuration
        CommonRequest commonRequest = createBaseRequest("/microservice/modifyService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyService: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Delete service
```

`*/`

```java
    private static void deleteService(IAcsClient client, String serviceId) throws Excep
tion {
        Map<String, Object> request = new HashMap<>();
        request.put("serviceId", serviceId);                                // [Required]
Service ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/microservice/deleteService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteService: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Batch delete services
```

`*/`

```java
    private static void batchDeleteServices(IAcsClient client, List<String> serviceIds)
throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("serviceIds", serviceIds);                              // [Required]
List of service IDs
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required]GatewayinstanceID
```

```java
[Required] Gateway instance ID
        CommonRequest commonRequest =
createBaseRequest("/microservice/batchDeleteService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("batchDeleteService: " +
response.getHttpResponse().getHttpContentString());
```

`}` `}`

**Upstream type description**

| upstreamType | Description | Configuration method |
|---|---|---|
| 1 | Static node | Configure the IP address, port, and weight in serviceStruct.nodes . |
| 2 | Service discovery | Specify the service name in the registration center by using serviceName . You must configure sourceId . |
| 3 | Service import | Import a service from an existing source. |

**Protocol type description**

| protocol | Description |
|---|---|
| HTTP | The HTTP or HTTPS protocol. |
| GRPC | The gRPC protocol. |
| Webservice | The WebService protocol. |
| Dubbo | The Dubbo RPC protocol. |
| HSF | The HSF RPC protocol. |

**Response code description**

| code | Description |
|---|---|
| 200 | The operation succeeded. |
| 400 | A parameter error occurred. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

#### API call - Instance management

**Overview**

The instance management module manages gateway instances. An instance is a running entity of the gateway. You can deploy it on a Kubernetes cluster. The instance supports two engine types: SCG and Higress.
**Applicable engines**: SCG / Higress
**API path prefix**: `/gatewayInstance`

**Authentication method**

**Self-managed ACK environment**: Add `X-CSB-TOKEN: csb@2022` and `X-CSB-OPENAPI:`
`true` to the request header.
**Enterprise Edition environment**: Add `x-acs-organizationid` and `x-acs-caller-sdk-`
`source` to the request header. Use a valid AccessKey pair.

**Create an instance**

**API description**

Create a new gateway instance.

**Request information**

| Item | Content |
|---|---|
| URL | /gatewayInstance/createInstance |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on CreateGwInstanceRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceName | String | Yes | The instance name. It must be 2 to 128 characters in length and start with a letter. |
| clusterCode | String | Yes | The cluster code. |
| namespace | String | Yes | The Kubernetes namespace. |
| brokerEngineType | String | No | The engine type: SCG HIGRESS SHARED SCG _ CLOUD NATIVE GAT _ _ EWAY |
| deployMode | String | No | The deployment mode: adp, edas, tiangong, custom, k8s, and so on. |
| instanceClass | String | No | The instance specification. |
| instanceNumber | String | No | The number of instance nodes. |
| vpcId | String | No | The VPC ID. |
| vswId | String | No | The vSwitch ID. |
| ingressName | String | No | The Ingress name. |
| deployConfigContent | String | No | The custom deployment configuration. |
| accessModeConfigCon tent | String | No | The access mode configuration. |

**Query the list of instances**

**API description**

Query gateway instances by page.

**Request information**

| Item | Content |
|---|---|
| URL | /gatewayInstance/listInstances |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ListGwInstancesRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| current | Integer | Yes | The page number. Start from 1. |
| size | Integer | Yes | The number of entries per page. |
| name | String | No | The instance name for fuzzy search. |
| gwInstanceId | String | No | Filter by instance ID. |
| deployMode | String | No | Filter by deployment mode. |
| status | Integer | No | Filter by instance status. |
| brokerEngineType | String | No | Filter by engine type. |

**List all instances**

**API description**

List all gateway instances without pagination.

**Request information**

| Item | Value |
|---|---|
| URL | /gatewayInstance/listAllInstances |
| Method | POST |
| Content-Type | application/json |

No request parameters are required.

**Query instance details**

**API description**

Query detailed information by instance ID.

**Request information**

| Item | Value |
|---|---|
| URL | /gatewayInstance/getInstanceInfo |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on GetInstanceInfoRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the instance. |

**Modify an instance**

**API description**

Modify the name of the instance.

**Request information**

| Item | Content |
|---|---|

| URL | /gatewayInstance/modifyInstance |
|---|---|
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ModifyInstanceRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the instance. |
| instanceName | String | Yes | The new name of the instance. |

**Delete an instance**

**API description**

Delete the specified gateway instance.

**Request information**

| Item | Content |
|---|---|
| URL | /gatewayInstance/deleteInstance |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on DeleteGwInstanceRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the instance. |

**Restart an instance**

**API description**

Restart the specified gateway instance.

**Request information**

| Item | Content |
|---|---|
| URL | /gatewayInstance/restartInstance |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on RestartGwInstanceRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the instance. |

**Stop instance**

**API description**

Stop the specified gateway instance.

**Request information**

| Item | Content |
|---|---|
| URL | /gatewayInstance/stopInstance |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on StopInstanceRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the instance. |

**Upgrade instance**

**API description**

Upgrade the instance to the latest version.

**Request information**

| Item | Content |
|---|---|
| URL | /gatewayInstance/upgradeInstance |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on UpgradeGwInstanceRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the instance. |

**Modify instance resources**

**API description**

Scale the instance up or down by modifying its specification and node count.

**Request information**

| Item | Content |
|---|---|
| URL | /gatewayInstance/modifyResource |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on**

**ModifyInstanceResourceRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the instance. |
| instanceClass | String | No | The specification of the instance. |

| instanceNumber | Integer | No | The number of instance nodes. |
|---|---|---|---|
| specificationTemplate | Integer | No | The specification template. |

**Query instance resources**

**API description**

Query the specification and node information of an instance.

**Request information**

| Item | Content |
|---|---|
| URL | /gatewayInstance/getResource |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on GetInstanceResourceRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the instance. |

**Common request call examples**

The following examples show how to call the instance management API by using Common Request. The only difference between a self-managed ACK environment and an Enterprise Edition environment lies in the authentication settings.

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; public class InstanceApiDemo {
```

```java
    // ========== Environment configuration (modify according to the actual
environment) ==========
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
        // ========== Create an instance ==========
        String instanceId = createInstance(client);
        // ========== Query the instance list ==========
        listInstances(client);
        // ========== Query instance details ==========
        getInstanceInfo(client, instanceId);
        // ========== Modify the instance name ==========
        modifyInstance(client, instanceId);
        // ========== Query instance resources ==========
        getResource(client, instanceId);
        // ========== Delete the instance ==========
        // deleteInstance(client, instanceId);
```

`}`

```java
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
```

`}` `}`

```java
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
```

`}`

```java
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
```

`d` `("` `i` `i`

```
id"
```

`O``G` `O` `)`

```
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
```

`}` `}`

```java
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
```

`}`

```
    /**
     * Create an instance (based on CreateGwInstanceRequest)
```

`*/`

```java
    private static String createInstance(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceName", "my-gateway-instance");            //
【Required】Instance name
        request.put("clusterCode", "cluster-code-xxx");                  // 【Required】C
luster code
        request.put("namespace", "default");                             //
【Required】Kubernetes namespace
        request.put("brokerEngineType", "SCG");                          //
【Optional】Engine type: SCG/HIGRESS
        // request.put("deployMode", "adp");                                // 【Optional
】Deployment mode
        // request.put("instanceClass", "standard");                        // 【Optional
】Instance specification
        // request.put("instanceNumber", "2");                              // 【Optional
】Number of nodes
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/createInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String instanceId = result.getString("data");
            System.out.println("createInstance success, instanceId: " + instanceId);
            return instanceId;
        } else {
            System.out.println("createInstance failed: " + result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * Query the instance list (based on ListGwInstancesRequest)
```

`*/`

```java
    private static void listInstances(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("current", 1);                                       // 【Required】Cu
rrent page number
        request.put("size", 10);                                         // 【Required】Nu
mber of entries per page
        // request.put("name", "");                                         // 【Optional
】Instance name (fuzzy search)
        // request.put("brokerEngineType", "SCG");                          // 【Optional
】Engine type filter
        // request.put("status", 2);                                        // 【Optional
】Status filter: 2-running
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/listInstances");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listInstances: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Query instance details (based on GetInstanceInfoRequest)
```

`*/`

```java
    private static void getInstanceInfo(IAcsClient client, String gwInstanceId) throws
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【Required】I
nstance ID
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/getInstanceInfo");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getInstanceInfo: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Modify the instance name (based on ModifyInstanceRequest)
```

`*/`

```java
    private static void modifyInstance(IAcsClient client, String gwInstanceId) throws E
xception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【Required】I
nstance ID
        request.put("instanceName", "modified-instance-name");           //
```

```
equest.put( staceae,
```

`od` `ed`

```
stace ae);
```

`//`

```java
【Required】New instance name
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/modifyInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyInstance: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Query instance resources (based on GetInstanceResourceRequest)
```

`*/`

```java
    private static void getResource(IAcsClient client, String gwInstanceId) throws Exce
ption {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【Required】I
nstance ID
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/getResource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getResource: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Modify instance resources (based on ModifyInstanceResourceRequest)
```

`*/`

```java
    private static void modifyResource(IAcsClient client, String gwInstanceId) throws E
xception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【Required】I
nstance ID
        request.put("instanceClass", "large");                           //
【Optional】Instance specification
        request.put("instanceNumber", 3);                                //
【Optional】Number of nodes
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/modifyResource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyResource: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Restart the instance (based on RestartGwInstanceRequest)
```

`*/`

```java
    private static void restartInstance(IAcsClient client, String gwInstanceId) throws
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【Required】I
nstance ID
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/restartInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("restartInstance: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Stop the instance (based on StopInstanceRequest)
```

`*/`

```java
    private static void stopInstance(IAcsClient client, String gwInstanceId) throws Exc
eption {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【Required】I
nstance ID
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/stopInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("stopInstance: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Delete the instance (based on DeleteGwInstanceRequest)
```

`*/`

```java
    private static void deleteInstance(IAcsClient client, String gwInstanceId) throws E
xception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【Required】I
nstance ID
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/deleteInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteInstance: " +
```

```
response.getHttpResponse().getHttpContentString());
```

`}` `}`

**Instance status description**

| status | Status name | Description |
|---|---|---|
| 0 | starting | The instance is starting. |
| 1 | error | The instance is in an error state. |
| 2 | running | The instance is running. |
| 3 | unknown | The status is unknown. |
| 4 | stopped | The instance has stopped. |
| 5 | wait deploy _ | The system is waiting for deployment. |
| 6 | updating | The system is updating (upgrading or scaling). |
| 7 | stopping | The instance is stopping. |

**Engine type description**

| brokerEngineType | Description |
|---|---|
| SCG | Spring Cloud Gateway (API gateway). |
| HIGRESS | Higress (AI gateway). |
| SHARED SCG _ | Shared Spring Cloud Gateway. |
| CLOUD NATIVE GATEWAY _ _ | Cloud-native gateway. |

**Response code description**

| code | Description |
|---|---|
| 200 | The request succeeded. |
| 400 | The parameters are invalid. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

#### API call - Group management

**Overview**

The group management module lets you create, delete, modify, and query route groups. Groups logically classify routes. You can configure a base path and a default domain name for each group.
**Applicable engines**: SCG / Higress (The API is engine-agnostic and works universally.)
**API path prefix**: `/group`

**Authentication method**

**Self-managed ACK environment**: Add `X-CSB-TOKEN: csb@2022` and `X-CSB-OPENAPI:`
`true` to the request header.
**Enterprise Edition environment**: Add `x-acs-organizationid` and `x-acs-caller-sdk-`
`source` to the request header. Use a valid AccessKey pair.

**Create a group**

**API description**

Create a new route group.

**Request information**

| Item | Content |
|---|---|
| URL | /group/createGroup |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on CreateGroupRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| name | String | Yes | The name of the group. |
| basePath | String | Yes | The base path of the group, such as /api/v1 . |
| groupId | String | No | The ID of the group. This parameter is optional and the system generates it automatically. |
| description | String | No | The description of the group. |
| needDefaultDomain | boolean | No | Specifies whether to use the default domain name. Default value: false. |
| defaultDomainForRout e | Boolean | No | Specifies whether to generate a default domain name for routes. Default value: false. |
| domainIds | List | No | The list of associated domain IDs. |
| isDisasterRecovery | Boolean | No | Specifies whether the group is for disaster recovery. Default value: false. |

**List groups**

**API description**

Query the list of route groups by page.

**Request information**

| Item | Content |
|---|---|
| URL | /group/listGroups |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ListGroupsRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |
| groupId | String | No | Filter by group ID. |
| groupIdList | List | No | Filter by a list of group IDs. |
| name | String | No | Perform fuzzy search by group name. |
| defaultDomainIsNull | Boolean | No | Filter by whether the default domain name is empty. |
| editable | Boolean | No | Filter by whether the group is editable. |
| isDisasterRecovery | Boolean | No | Filter by whether the group is for disaster recovery. |

**Query group details**

**API description**

Query detailed information by group ID.

**Request information**

| Item | Content |
|---|---|
| URL | /group/getGroup |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on GetGroupRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| groupId | String | Yes | The ID of the group. |

**Modify a group**

**API description**

Modify the configuration of an existing group.

**Request information**

| Item | Content |
|---|---|
| URL | /group/modifyGroup |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ModifyGroupRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|

| gwInstanceId | String | Yes | The ID of the gateway instance. |
|---|---|---|---|
| groupId | String | Yes | The ID of the group. |
| name | String | No | The name of the group. |
| basePath | String | No | The base path of the group. |
| description | String | No | The description of the group. |
| domainIds | List | No | The list of associated domain IDs. |
| defaultDomainForRout e | Boolean | No | Specifies whether to generate a default domain name for the route. |

**Delete a group**

**API description**

Delete the specified group.

**Request information**

| Item | Content |
|---|---|
| URL | /group/deleteGroup |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |

| groupId | String | Yes | The ID of the group. |
|---|---|---|---|

**Add a domain name for a group**

**API description**

Add an associated domain name for a group.

**Request information**

| Item | Content |
|---|---|
| URL | /group/addGroupDomain |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on AddGroupDomainRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| groupId | String | Yes | The ID of the group. |
| domainIds | List | Yes | The list of domain IDs to add. |

**Delete group domain**

**API description**

Delete the domain name associated with the group.

**Request information**

| Item | Content |
|---|---|
| URL | /group/deleteGroupDomain |
| Method | POST |

| Content-Type | application/json |
|---|---|

**Request parameters (based on DeleteGroupDomainRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| groupId | String | Yes | The ID of the group. |
| domainId | String | Yes | The ID of the domain name to delete. |

**Query all groups**

**API description**

Query all groups under the gateway instance without pagination.

**Request information**

| Item | Content |
|---|---|
| URL | /group/getAllGroups |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common request call example**

The following example shows how to call the group management API by using the common request method. The difference between a self-managed ACK environment and an enterprise edition environment lies only in the authentication setting.

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; importcomali ncsCommonReqest
```

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.Arrays; import java.util.HashMap; import java.util.List; import java.util.Map; public class GroupApiDemo {
    // ========== Environment configuration (modify according to actual environment) ==
========
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
        // ========== Create group ==========
        String groupId = createGroup(client);
        // ========== List groups ==========
        listGroups(client);
        // ========== Get group details ==========
        getGroup(client, groupId);
        // ========== Modify group ==========
        modifyGroup(client, groupId);
        // ========== Add group domain ==========
        addGroupDomain(client, groupId, Arrays.asList("domain-id-xxx"));
        // ========== Delete group domain ==========
        deleteGroupDomain(client, groupId, "domain-id-xxx");
        // ========== Delete group ==========
        deleteGroup(client, groupId);
```

`}`

```java
    private static IAcsClient createClient() {
if(ISSELFHOSTED){
```

```
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
```

`}` `}`

```java
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
```

`}`

```java
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
```

`}` `}`

```java
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
```

`}`

```
    /**
     * Create group (based on CreateGroupRequest)
```

`*/`

```java
    private static String createGroup(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("name", "api-group-demo");                              // 【Required
】Group name
        request.put("basePath", "/api/v1");                                 // 【Required
】Group base path
        request.put("description", "API demo group");                       //
【Optional】Group description
        // request.put("groupId", "");                                         //
【Optional】Group ID (system-generated)
        // request.put("needDefaultDomain", false);                            // 【Optio
nal】Whether to require a default domain
        // request.put("defaultDomainForRoute", false);                        // 【Optio
nal】Whether to generate a default domain for routing
        // request.put("domainIds", Arrays.asList("domain-id-xxx"));           // 【Opti
```

`q` `p` `,` `p`

```java
onal】List of associated domain IDs
        // request.put("isDisasterRecovery", false);                           // 【Optio
nal】Whether this is a disaster recovery group
        CommonRequest commonRequest = createBaseRequest("/group/createGroup");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String groupId = result.getString("data");
            System.out.println("createGroup success, groupId: " + groupId);
            return groupId;
        } else {
            System.out.println("createGroup failed: " + result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * List groups (based on ListGroupsRequest)
```

`*/`

```java
    private static void listGroups(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("current", 1);                                          // 【Required
】Current page number
        request.put("size", 10);                                            // 【Required
】Number of entries per page
        // request.put("name", "");                                            // 【Option
al】Group name (fuzzy search)
        // request.put("editable", true);                                      //
【Optional】Filter by editable status
        // request.put("isDisasterRecovery", false);                           // 【Optio
nal】Filter by disaster recovery status
        CommonRequest commonRequest = createBaseRequest("/group/listGroups");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listGroups: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Get group details (based on GetGroupRequest)
```

`*/`

```java
    private static void getGroup(IAcsClient client, String groupId) throws Exception {
        Map<String, Object> request = new HashMap<>();
```

```java
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("groupId", groupId);                                    // 【Required
】Group ID
        CommonRequest commonRequest = createBaseRequest("/group/getGroup");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getGroup: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Modify group (based on ModifyGroupRequest)
```

`*/`

```java
    private static void modifyGroup(IAcsClient client, String groupId) throws Exception
```

`{`

```java
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("groupId", groupId);                                    // 【Required
】Group ID
        request.put("name", "api-group-modified");                          // 【Optional
】Group name
        request.put("basePath", "/api/v2");                                 // 【Optional
】Group base path
        request.put("description", "Modified group description");           // 【Optiona
l】Group description
        CommonRequest commonRequest = createBaseRequest("/group/modifyGroup");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyGroup: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Add group domain (based on AddGroupDomainRequest)
```

`*/`

```java
    private static void addGroupDomain(IAcsClient client, String groupId, List<String>
domainIds) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("groupId", groupId);                                    // 【Required
】Group ID
        request.put("domainIds", domainIds);                                // 【Required
】List of domain IDs to add
        CommonRequest commonRequest = createBaseRequest("/group/addGroupDomain");
```

```java
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("addGroupDomain: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Delete group domain (based on DeleteGroupDomainRequest)
```

`*/`

```java
    private static void deleteGroupDomain(IAcsClient client, String groupId, String dom
ainId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("groupId", groupId);                                    // 【Required
】Group ID
        request.put("domainId", domainId);                                  // 【Required
】Domain ID to delete
        CommonRequest commonRequest = createBaseRequest("/group/deleteGroupDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteGroupDomain: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Delete group
```

`*/`

```java
    private static void deleteGroup(IAcsClient client, String groupId) throws Exception
```

`{`

```java
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("groupId", groupId);                                    // 【Required
】Group ID
        CommonRequest commonRequest = createBaseRequest("/group/deleteGroup");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteGroup: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Get all groups
```

`*/`

```java
    private static void getAllGroups(IAcsClient client) throws Exception {
```

`M`

```
<Sti Obj
```

`t>` `t` `H` `hM`

```
<>()
```

```java
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/group/getAllGroups");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getAllGroups: " +
response.getHttpResponse().getHttpContentString());
```

`}` `}`

**Group attribute description**

| Attribute | Description |
|---|---|
| groupId | The unique identifier of the group. |
| name | The name of the group. |
| basePath | The base path of the group. All routes under this group inherit this path prefix. |
| description | The description of the group. |
| defaultDomain | The default domain name of the group. |
| editable | Whether the group is editable: true: The group is editable. false: The group is not editable (such as the DEFAULT group). |
| isDisasterRecovery | Whether the group is a disaster recovery group. |

**Response code description**

| code | Description |
|---|---|
| 200 | The request succeeded. |
| 400 | The parameters are invalid. |

| 403 | You do not have sufficient permissions. |
|---|---|
| 500 | An internal server error occurred. |

#### API call - Route management

**Overview**

The route management module provides functions to create, delete, modify, and query routes. A route defines how a request forwards from the gateway to the backend service.
**Applicable engine**: SCG / Higress (the API is engine-agnostic and universally applicable)
**API path prefix**: `/route`

**Authentication method**

**Self-managed ACK environment**: Add `X-CSB-TOKEN: csb@2022` and `X-CSB-OPENAPI:`
`true` to the request header.
**Enterprise Edition environment**: Add `x-acs-organizationid` and `x-acs-caller-sdk-`
`source` to the request header, and use a valid AccessKey pair.

**Validate parameters before creating a route**

**API description**

Validate parameters before you create a route. The system checks whether the route name is duplicate.

**Request information**

| Item | Content |
|---|---|
| URL | /route/checkCreateRoute |
| Method | POST |
| Content-Type | application/json |

**Create a route**

**API description**

Create a new routing rule.

**Request information**

| Item | Content |
|---|---|

| URL | /route/createRoute |
|---|---|
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on RouteCreateRequest +**

**AbstractRouteRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| routeName | String | Yes | The name of the route. This is a unique identifier. |
| groupId | String | Yes | The ID of the group. The default group is "DEFAULT". |
| routePath | List | Yes | The list of paths. Supports Ant-style wildcards. |
| serviceType | String | Yes | The type of service: SINGLE: Single service WEIGHTED: Weighted |
| serviceId | String | Conditional | The ID of the backend service. Note This parameter is required in single- service mode. |

| serviceIds | List | Conditional | The list of services and their weights. Note This parameter is required in weighted mode. |
|---|---|---|---|
| path | RoutePath | No | The new path matching configuration. It has higher priority than routePath . |
| order | int | No | The priority of the route. A smaller number indicates a higher priority. The default value is 0. |
| enableStatus | Boolean | No | The enabled status. The default value is true. |
| openStripPrefix | boolean | No | Specifies whether to enable path prefix stripping. The default value is false. |
| stripPrefix | int | No | The number of prefix layers to strip. Use this parameter together with openStripPrefix. |
| methods | List | No | The HTTP methods that are allowed, such as ["GET","POST"] . |
| header | List | No | The list of header matching conditions. |
| cookie | List | No | The list of cookie matching conditions. |
| queryParam | List | No | The list of query parameter matching conditions. |

| domainIds | List | No | The list of associated domain IDs. |
|---|---|---|---|
| requestTimeout | Integer | No | The request timeout period, in milliseconds. |
| isDisasterRecovery | Boolean | No | Specifies whether the route is for disaster recovery. |
| disasterRecoveryServi ceId | String | No | The ID of the disaster recovery service. |
| disasterRecoveryServi ceIds | List | No | The list of disaster recovery service IDs and their weights. |
| hsfMethodMappingCon fig | HsfMethodMappingCon fig | No | The HSF method mapping configuration. This applies only to HSF protocol configurations. |

**RoutePath structure**

| Parameter | Type | Required | Description |
|---|---|---|---|
| matchType | String | Yes | The match type: PRE: Prefix EXACT: Exact REGEX: Regex |
| matchValue | String | No | The match value. |
| caseSensitive | Boolean | No | Specifies whether the match is case- sensitive. |

**KvPair structure**

| Parameter | Type | Required | Description |
|---|---|---|---|
| key | String | Yes | The key name. |

| tack APIs through a POP | gatewa |   | API Gatewa |
|---|---|---|---|

| value | String | Yes | The key value. |
|---|---|---|---|

**ServiceAndWeight structure**

| Parameter | Type | Required | Description |
|---|---|---|---|
| serviceId | String | Yes | The ID of the service. |
| weight | Integer | Yes | The weight. Valid values: 0 to 100. |

**List routes**

**API description**

Query routes by page.

**Request information**

| Item | Content |
|---|---|
| URL | /route/listRoutes |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on RouteListRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |

| routeName | String | No | The name of the route. Fuzzy search is supported. |
|---|---|---|---|
| serviceName | String | No | The name of the service. Fuzzy search is supported. |
| exactServiceId | String | No | The ID of the service. Exact match is supported. |
| enableStatus | Boolean | No | The filter for the enabled status. |
| routeId | String | No | The ID of the route. |
| groupName | String | No | The name of the group. |
| domainName | String | No | The domain name. |
| routePath | String | No | The path of the route. Fuzzy search is supported. |
| isDisasterRecovery | Boolean | No | Indicates whether the route is for disaster recovery. |

**Query route details**

**API description**

Query the detailed information of a route by its ID.

**Request information**

| Item | Content |
|---|---|
| URL | /route/getRoute |
| Method | POST |

| Content-Type | application/json |
|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| routeId | String | Yes | The ID of the route. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify a route**

**API description**

Modify an existing route configuration.

**Request information**

| Item | Content |
|---|---|
| URL | /route/modifyRoute |
| Method | POST |
| Content-Type | application/json |

The request parameters are the same as those for creating a route. You must also specify

```
 routeId .
```

**Delete a route**

**API description**

Delete the specified route.

**Request information**

| Item | Content |
|---|---|
| URL | /route/deleteRoute |
| Method | POST |

| Content-Type | application/json |
|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| routeId | String | Yes | The ID of the route. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify the enabled status of a route**

**API description**

Enable or disable a route.

**Note**

This API applies only to the SCG engine. The Higress engine does not support this API.

**Request information**

| Item | Content |
|---|---|
| URL | /route/changeRouteStatus |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| routeId | String | Yes | The ID of the route. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

| enableStatus | Boolean | Yes | true: Enable the route. false: Disable the route. |
|---|---|---|---|

**Delete routes in batches**

**API description**

Delete multiple routes in batches.

**Request information**

| Item | Content |
|---|---|
| URL | /route/batchDeleteRoute |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| routeIds | List | Yes | The list of route IDs. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common request call examples**

The following examples show how to call the route management API by using the common request method. The difference between a self-managed ACK environment and an enterprise edition environment lies only in the authentication parameter settings.

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.ArrayList;
```

```java
import java.util.Arrays; import java.util.HashMap; import java.util.List; import java.util.Map; public class RouteApiDemo {
    // ========== Environment configuration (modify according to actual environment) ==
========
    // Self-managed ACK environment configuration
    private static final boolean IS_SELF_HOSTED = true;                     // Whether i
t is a self-managed ACK environment
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";    // Self-man
aged ACK console address
    // Enterprise edition environment configuration (used when IS_SELF_HOSTED = false)
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
    // Gateway instance ID and backend service ID
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    private static final String SERVICE_ID = "your-service-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
        // ========== Validate before creating route ==========
        checkCreateRoute(client);
        // ========== Create route ==========
        String routeId = createRoute(client);
        // ========== List routes ==========
        listRoutes(client);
        // ========== Get route details ==========
        getRoute(client, routeId);
        // ========== Modify route ==========
        modifyRoute(client, routeId);
        // ========== Change route status ==========
        changeRouteStatus(client, routeId, false);
        // ========== Delete route ==========
        deleteRoute(client, routeId);
```

`}`

```
    /**
     * Create client (common for self-managed ACK and enterprise edition)
```

`*/`

```java
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
```

`}` `}`

```java
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
```

`}`

```java
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
```

`}` `}`

```java
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
```

`}`

```
    /**
     * Validate before creating route
```

`*/`

```java
    private static void checkCreateRoute(IAcsClient client) throws Exception {
        Map<String, Object> request = buildRouteRequest();
        CommonRequest commonRequest = createBaseRequest("/route/checkCreateRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("checkCreateRoute: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Create route
```

`*/`

```java
    private static String createRoute(IAcsClient client) throws Exception {
Map<String Object>request=buildRouteRequest();
```

```java
        Map<String, Object> request = buildRouteRequest();
        CommonRequest commonRequest = createBaseRequest("/route/createRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonRequest(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String routeId = result.getString("data");
            System.out.println("createRoute success, routeId: " + routeId);
            return routeId;
        } else {
            System.out.println("createRoute failed: " + result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * Build route request parameters
```

`*/`

```java
    private static Map<String, Object> buildRouteRequest() {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        request.put("routeName", "route-demo-01");                          //
[Required] Route name
        request.put("groupId", "DEFAULT");                                  // [Required]
Group ID
        request.put("routePath", Arrays.asList("/api-demo/**"));            // [Required
] Path list
        request.put("serviceType", "SINGLE");                               // [Required]
Service type: SINGLE/WEIGHTED
        request.put("serviceId", SERVICE_ID);                               // [Required]
Backend service ID (SINGLE mode)
        request.put("enableStatus", true);                                  // [Optional]
Enable status
        request.put("order", 100);                                          // [Optional]
Route priority
        // request.put("openStripPrefix", false);                             // [Optiona
l] Whether to enable path prefix stripping
        // request.put("stripPrefix", 1);                                     // [Optiona
l] Number of prefix levels to strip
        // request.put("methods", Arrays.asList("GET", "POST"));              // [Option
al] HTTP method restriction
        // request.put("domainIds", new ArrayList<>());                        //
[Optional] Associated domain ID list
        // New path matching configuration (takes precedence over routePath)
        // Map<String, Object> path = new HashMap<>();
        // path.put("matchType", "PRE");                                      // PRE/EXAC
T/REGEX
        // path.put("matchValue", "");                                        // Match va
lue
```

```
lue
        // path.put("caseSensitive", false);                                  // Whether
case-sensitive
        // request.put("path", path);
        // Weighted mode service list (WEIGHTED mode)
        // List<Map<String, Object>> serviceIds = new ArrayList<>();
        // Map<String, Object> service1 = new HashMap<>();
        // service1.put("serviceId", "service-id-1");
        // service1.put("weight", 80);
        // Map<String, Object> service2 = new HashMap<>();
        // service2.put("serviceId", "service-id-2");
        // service2.put("weight", 20);
        // serviceIds.add(service1);
        // serviceIds.add(service2);
        // request.put("serviceIds", serviceIds);
        // Header match conditions
        // List<Map<String, Object>> header = new ArrayList<>();
        // Map<String, Object> headerCondition = new HashMap<>();
        // headerCondition.put("key", "X-Version");
        // headerCondition.put("value", "v1");
        // header.add(headerCondition);
        // request.put("header", header);
        // Cookie match conditions
        // List<Map<String, Object>> cookie = new ArrayList<>();
        // Map<String, Object> cookieCondition = new HashMap<>();
        // cookieCondition.put("key", "sessionId");
        // cookieCondition.put("value", "session-*");
        // cookie.add(cookieCondition);
        // request.put("cookie", cookie);
        // Query parameter match conditions
        // List<Map<String, Object>> queryParam = new ArrayList<>();
        // Map<String, Object> queryCondition = new HashMap<>();
        // queryCondition.put("key", "version");
        // queryCondition.put("value", "1.0");
        // queryParam.add(queryCondition);
        // request.put("queryParam", queryParam);
        // Disaster recovery route configuration
        // request.put("isDisasterRecovery", true);                           //
[Optional] Whether it is a disaster recovery route
        // request.put("disasterRecoveryServiceId", "disaster-service-id");   //
[Optional] Disaster recovery service ID
        return request;
```

`}`

```
    /**
     * List routes
```

`*/`

```java
    private static void listRoutes(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
```

```java
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        request.put("current", 1);                                          // [Required]
Current page number
        request.put("size", 10);                                            // [Required]
Number of entries per page
        // request.put("routeName", "");                                      // [Optiona
l] Route name (fuzzy search)
        // request.put("serviceName", "");                                    // [Optiona
l] Service name (fuzzy search)
        // request.put("enableStatus", true);                                 // [Optiona
l] Enable status filter
        CommonRequest commonRequest = createBaseRequest("/route/listRoutes");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listRoutes: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Get route details
```

`*/`

```java
    private static void getRoute(IAcsClient client, String routeId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("routeId", routeId);                                    // [Required]
Route ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/route/getRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getRoute: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Modify route
```

`*/`

```java
    private static void modifyRoute(IAcsClient client, String routeId) throws Exception
```

`{`

```
        Map<String, Object> request = buildRouteRequest();
        request.put("routeId", routeId);                                    // [Required]
Route ID to modify
        request.put("routeName", "route-demo-01-modified");                 //
[Optional] Modify route name
        request.put("order", 200);                                          // [Optional]
Modify priority
```

```java
        CommonRequest commonRequest = createBaseRequest("/route/modifyRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyRoute: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Change route status
```

`*/`

```java
    private static void changeRouteStatus(IAcsClient client, String routeId, boolean en
ableStatus) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("routeId", routeId);                                    // [Required]
Route ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        request.put("enableStatus", enableStatus);                          //
[Required] Enable status
        CommonRequest commonRequest = createBaseRequest("/route/changeRouteStatus");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("changeRouteStatus: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Delete route
```

`*/`

```java
    private static void deleteRoute(IAcsClient client, String routeId) throws Exception
```

`{`

```java
        Map<String, Object> request = new HashMap<>();
        request.put("routeId", routeId);                                    // [Required]
Route ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/route/deleteRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteRoute: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Batch delete routes
```

`*/`

```java
    private static void batchDeleteRoutes(IAcsClient client, List<String> routeIds) thr
ows Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("routeIds", routeIds);                                  // [Required]
Route ID list
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/route/batchDeleteRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("batchDeleteRoute: " +
response.getHttpResponse().getHttpContentString());
```

`}` `}`

**Path matching type description**

| matchType | Description | Example |
|---|---|---|
| PRE | Prefix match. | /api/** matches all paths that start with /api/ . |
| EXACT | Exact match. | /api/user matches only /api/user . |
| REGEX | Regex match. | Use a regular expression to match the path. |

**Service type description**

| serviceType | Description | Usage |
|---|---|---|
| SINGLE | Single service | Use serviceId to specify one backend service. |
| WEIGHTED | Weighted service | Use serviceIds to specify multiple services and their weights. |

**Response code descriptions**

| code | Description |
|---|---|
| 200 | The request succeeded. |
| 400 | The parameter is invalid. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

#### API call - Policy configuration

**management**

**Overview**

The policy configuration management module manages policies. You can create, delete, modify, and query policies. A policy configures behaviors for routes, services, and consumers, such as throttling, circuit breaking, retry, and CORS.
**Applicable engine**: SCG / Higress (The API is engine-agnostic and works universally.)
**API path prefix**: `/strategyConfig/**`

**Authentication method**

**Self-managed ACK environment**: Add `X-CSB-TOKEN: csb@2022` and `X-CSB-OPENAPI:`
`true` to the request header.
**Enterprise Edition environment**: Add `x-acs-organizationid` and `x-acs-caller-sdk-`
`source` to the request header and use a valid AccessKey pair.

**Create a policy configuration**

**API description**

Create a new policy configuration. The structure of the `config` field varies by policy type. For more information, see the policy configuration examples below.

**Request information**

| Item | Content |
|---|---|
| URL | /strategyConfig/createStrategyConfig |
| Method | POST |

| Content-Type | application/json |
|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| strategyName | String | Yes | The English name of the policy type. |
| strategyConfigName | String | No | The name of the policy configuration. |
| config | Object | No | The policy configuration parameters in map format. |
| rawConfig | String | No | The policy configuration parameters in YAML format. |
| routeIds | List | No | The list of associated route IDs. |
| serviceIds | List | No | The list of associated service IDs. |
| appIds | List | No | The list of associated consumer IDs. |
| domainIds | List | No | The list of associated domain IDs. |

**Query the list of policy configurations**

**API description**

Query the list of policy configurations by page.

**Request information**

| Item | Content |
|---|---|

| URL | /strategyConfig/listStrategyConfigs |
|---|---|
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |
| strategyName | String | No | The name of the policy type used for filtering. |
| routeId | String | No | The ID of the associated route used for filtering. |
| serviceId | String | No | The ID of the associated service used for filtering. |
| appId | String | No | The ID of the associated consumer used for filtering. |

**Query policy configuration details**

**API description**

Query detailed information by policy configuration ID.

**Request information**

| Item | Content |
|---|---|

| URL | /strategyConfig/getStrategyConfig |
|---|---|
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| strategyConfigId | String | Yes | The ID of the policy configuration. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify policy configuration**

**API call description**

Modify an existing policy configuration.

**Request information**

| Item | Content |
|---|---|
| URL | /strategyConfig/modifyStrategyConfig |
| Method | POST |
| Content-Type | application/json |

Use the same parameters as those for creating a policy configuration. Additionally, specify

```
 strategyConfigId .
```

**Modify policy configuration status**

**API call description**

Enable or disable a policy configuration.

**Request information**

| Item |   | Content |   |   |
|---|---|---|---|---|
| URL |   | /strategyConfig/modifyStrategyConfigStatus |   |   |
|   |   |   | /strategyConfig/modifyStrategyConfigStatus |   |
|   | RL |   |   |   |
| Method |   | POST |   |   |
| Content-Type |   | application/json |   |   |

| Parameter | Type | Required | Description |
|---|---|---|---|
| strategyConfigId | String | Yes | The ID of the policy configuration. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| isOpen | Boolean | Yes | true: Enable the policy false: Disable the policy |

**Delete a policy configuration**

**API description**

Delete a specified policy configuration.

**Request information**

| Item | Content |
|---|---|
| URL | /strategyConfig/deleteStrategyConfig |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| strategyConfigId | String | Yes | The ID of the policy configuration. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common Request call examples**

The following examples show how to call the policy configuration management API by using the Common Request method. The difference between a self-managed ACK environment and an Enterprise Edition environment lies only in the authentication parameter settings.

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.ArrayList; import java.util.Arrays; import java.util.HashMap; import java.util.List; import java.util.Map; public class StrategyConfigApiDemo {
    // ========== Environment configuration (modify according to actual environment) ==
========
    // Self-managed ACK environment configuration
    private static final boolean IS_SELF_HOSTED = true;                     // Whether i
t is a self-managed ACK environment
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";    // Self-man
aged ACK console address
    // Enterprise Edition environment configuration (used when IS_SELF_HOSTED = false)
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";  // E
nterprise Edition Endpoint
    private static final String ACCESS_KEY_ID = "your-access-key-id";                //
AccessKey ID
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";        //
AccessKey Secret
    private static final String ORGANIZATION_ID = "your-org-id";                     //
Enterprise organization ID
    // Gateway instance ID
```

```java
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    public static void main(String[] args) throws Exception {
        // Initialize client
        IAcsClient client = createClient();
        // ========== Example: Create different types of policy configurations
==========
        // 1. Flow control policy
        String flowControlStrategyId = createFlowControlStrategy(client);
        // 2. Timeout policy
        String timeoutStrategyId = createTimeoutStrategy(client);
        // 3. Circuit breaker policy
        String circuitBreakerStrategyId = createCircuitBreakerStrategy(client);
        // 4. Cross-domain policy
        String corsStrategyId = createCorsStrategy(client);
        // 5. Caching policy
        String cacheStrategyId = createCacheStrategy(client);
        // 6. IP allowlist and blocklist policy
        String ipBlockStrategyId = createIpBlockStrategy(client);
        // 7. ACL permission control policy
        String aclStrategyId = createAclStrategy(client);
        // 8. Mock policy
        String mockStrategyId = createMockStrategy(client);
        // 9. Request tracing policy
        String tracingStrategyId = createTracingStrategy(client);
        // 10. Request body size limit policy
        String requestSizeStrategyId = createRequestSizeStrategy(client);
        // ========== Query policy configuration list ==========
        listStrategyConfigs(client);
        // ========== Query policy configuration details ==========
        getStrategyConfig(client, flowControlStrategyId);
        // ========== Modify policy configuration status ==========
        modifyStrategyConfigStatus(client, flowControlStrategyId, false);
        // ========== Delete policy configuration ==========
        deleteStrategyConfig(client, flowControlStrategyId);
```

`}`

```
    /**
     * Create client (common for self-managed ACK and Enterprise Edition)
```

`*/` `*/`

```java
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            // Self-managed ACK environment: AK/SK do not need to be filled in
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            // Enterprise Edition environment: Requires valid AK/SK
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
```

`}` `}`

```
    /**
     * Get endpoint
```

`*/`

```java
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
```

`}`

```
    /**
     * Set authentication headers (common for self-managed ACK and Enterprise Edition)
```

`*/`

```java
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            // Self-managed ACK environment authentication
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            // Enterprise Edition environment authentication
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
```

`}` `}`

```
    /**
     * Create base request object
```

`*/`

```java
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
```

`}`

```
    // ========== Policy configuration creation examples ==========
    /**
     * 1. Flow control policy (Flow Control Policy)
*configstructure:CacheGatewayFlowRule
```

```
      config structure: CacheGatewayFlowRule
```

`*/`

```java
    private static String createFlowControlStrategy(IAcsClient client) throws Exception
```

`{`

```
        // Flow control rule configuration
        Map<String, Object> flowRule = new HashMap<>();
        flowRule.put("resource", "route-id-xxx");                           // 【Required
】Resource name (route ID)
        flowRule.put("resourceMode", 0);                                    // 【Required
】Resource mode: 0-route ID, 1-API group
        flowRule.put("grade", 1);                                           // 【Required
】Throttling threshold type: 1-QPS
        flowRule.put("count", 100.0);                                       // 【Required
】Throttling threshold (QPS quantity)
        flowRule.put("controlBehavior", 0);                                 // 【Optional
】Flow control effect: 0-fast failure, 2-uniform queuing
        flowRule.put("intervalSec", 1L);                                    // 【Optional
】Statistical time window (seconds)
        flowRule.put("burst", 20);                                          // 【Optional
】Burst capacity
        flowRule.put("maxQueueingTimeoutMs", 500);                          // 【Optional
】Maximum queue waiting time (milliseconds)
        flowRule.put("enable", true);                                       // 【Optional
】Whether to enable
        // Optional: Parameter throttling configuration
        // Map<String, Object> paramItem = new HashMap<>();
        // paramItem.put("parseStrategy", 0);                                // Parameter
extraction strategy: 0-client IP, 1-Host, 2-Header, 3-URL parameter
        // paramItem.put("fieldName", "X-User-Id");                          //
Parameter field name
        // paramItem.put("pattern", "user-*");                               // Matching
pattern
        // paramItem.put("matchStrategy", 0);                                // Matching
strategy: 0-exact, 1-regex
        // flowRule.put("paramItem", paramItem);
        List<Map<String, Object>> gatewayFlowRules = new ArrayList<>();
        gatewayFlowRules.add(flowRule);
        Map<String, Object> config = new HashMap<>();
        config.put("isOpenTrafficControl", true);                           // 【Required
】Whether to enable flow control
        config.put("gatewayFlowRules", gatewayFlowRules);                   //
【Required】Flow control rule list
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Flow Control Policy");
        request.put("strategyConfigName", "route-flow-control");
        request.put("config", config);
        return executeCreate(client, request, "Flow Control Policy");
```

`}`

```
    /**
     * 2. Timeout policy (Timeout Policy)
     * config structure: RequestTimeoutConfig
```

`*/`

```java
    private static String createTimeoutStrategy(IAcsClient client) throws Exception {
        Map<String, Object> config = new HashMap<>();
        config.put("timeout", 30000);                                       // 【Required
】Timeout duration (milliseconds)
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Timeout Policy");
        request.put("strategyConfigName", "route-timeout");
        request.put("config", config);
        return executeCreate(client, request, "Timeout Policy");
```

`}`

```
    /**
     * 3. Circuit breaker policy (Circuit Breaker Policy)
     * config structure: CacheRouteFuse
```

`*/`

```java
    private static String createCircuitBreakerStrategy(IAcsClient client) throws Except
ion {
        // Circuit breaker condition configuration
        Map<String, Object> fuseCondition = new HashMap<>();
        fuseCondition.put("type", 2);                                       // 【Required
】Rule type: 1-average response time, 2-error count, 3-backend timeout
        fuseCondition.put("operator", "in");                                // 【Required
】Comparator: gt(greater than), in(includes), notIn(excludes)
        fuseCondition.put("judgValue", "500,502,503");                      // 【Required
】Judgment value (error code list or response time)
        fuseCondition.put("errorCount", 5.0);                               // 【Optional
】Error count threshold
        fuseCondition.put("statInterval", 30);                              // 【Optional
】Judgment time window (seconds)
        fuseCondition.put("timeWindow", 20);                                // 【Optional
】Circuit breaker duration (seconds)
        fuseCondition.put("minRequestAmount", 10);                          // 【Optional
】Minimum request count
        List<Map<String, Object>> routeFusesCondition = new ArrayList<>();
        routeFusesCondition.add(fuseCondition);
        // Degradation Mock configuration (used when degradeStrategy=1)
        Map<String, Object> fuseMock = new HashMap<>();
        fuseMock.put("isOpen", 1);                                          // 0-
disabled, 1-enabled
        fuseMock.put("responseCode", 200);                                  // 【Optional
】Response status code
        fuseMock.put("responseBody", "{\"code\":0,\"msg\":\"service degraded\"}");  //
【Optional】Response body
        fuseMock.put("responseHeader", Arrays.asList("Content-Type:application/json"));
// 【Optional】Response header list
```

```
        Map<String, Object> config = new HashMap<>();
        config.put("isOpenFuse", true);                                     // 【Required
】Whether to enable circuit breaking
        config.put("combinedCondition", "any");                             // 【Optional
】Combination condition: all(all satisfied), any(any satisfied)
        config.put("routeFusesCondition", routeFusesCondition);             //
【Required】Circuit breaker condition list
        config.put("degradeStrategy", 1);                                   // 【Optional
】Degradation strategy: 1-Mock response
        config.put("fuseMock", fuseMock);                                   // 【Optional
】Degradation Mock configuration
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Circuit Breaker Policy");
        request.put("strategyConfigName", "route-circuit-breaker");
        request.put("config", config);
        return executeCreate(client, request, "Circuit Breaker Policy");
```

`}`

```
    /**
     * 4. Cross-domain policy (Cross-domain Policy)
     * config structure: RouteCross
```

`*/`

```java
    private static String createCorsStrategy(IAcsClient client) throws Exception {
        Map<String, Object> config = new HashMap<>();
        config.put("isOpenCross", true);                                    // 【Required
】Whether to enable cross-domain
        config.put("crossType", "cors");                                    // 【Optional
】Cross-domain type: cors, jsonp
        config.put("allowedOrigins", "*");                                  // 【Required
】Allowed origins (* means all)
        config.put("allowedMethods", Arrays.asList("GET", "POST", "PUT", "DELETE",
"OPTIONS")); // 【Required】Allowed methods
        config.put("allowedHeaders", "*");                                  // 【Optional
】Allowed request headers
        config.put("exposedHeaders", "X-Custom-Header");                    //
【Optional】Exposed response headers
        config.put("allowedCredentials", true);                             // 【Optional
】Whether to allow credentials
        config.put("maxAge", 3600L);                                        // 【Optional
】Preflight request cache time (seconds)
        config.put("callbackFunc", "callback");                             // 【Optional
】JSONP callback function name
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Cross-domain Policy");
        request.put("strategyConfigName", "route-cors");
        request.put("config", config);
        return executeCreate(client, request, "Cross-domain Policy");
```

`}`

```
    /**
     * 5. Caching policy (Caching Policy)
     * config structure: ResponseCache
```

`*/`

```java
    private static String createCacheStrategy(IAcsClient client) throws Exception {
        // Cache interface configuration
        Map<String, Object> cacheRequest = new HashMap<>();
        cacheRequest.put("routeId", "route-id-xxx");                        // 【Required
】Route ID
        cacheRequest.put("cacheKey", "query:userId");                       // 【Optional
】Cache key rule
        List<Map<String, Object>> routeInterfaceList = new ArrayList<>();
        routeInterfaceList.add(cacheRequest);
        Map<String, Object> config = new HashMap<>();
        config.put("isOpenResponseCache", true);                            // 【Required
】Whether to enable caching
        config.put("routeInterfaceList", routeInterfaceList);               //
【Optional】Cache interface list
        config.put("isOpenCacheControl", true);                             // 【Optional
】Whether to enable browser cache control
        config.put("maxAge", 300L);                                         // 【Optional
】Browser cache time (seconds)
        config.put("allowedStatusCodes", Arrays.asList(200, 301, 302));     // 【Optiona
l】Allowed cacheable status codes
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Caching Policy");
        request.put("strategyConfigName", "route-cache");
        request.put("config", config);
        return executeCreate(client, request, "Caching Policy");
```

`}`

```
    /**
     * 6. IP allowlist and blocklist policy (IP Blacklist and Whitelist Policy)
     * config structure: RouteIpBlockConfig
```

`*/`

```java
    private static String createIpBlockStrategy(IAcsClient client) throws Exception {
        // IP rule configuration
        Map<String, Object> allowRule = new HashMap<>();
        allowRule.put("ip", "192.168.1.100");                               // 【Required
】IP address (supports CIDR format)
        allowRule.put("policy", "allow");                                   // 【Required
】Policy: allow-allowlist, deny-blocklist
        Map<String, Object> denyRule = new HashMap<>();
        denyRule.put("ip", "10.0.0.0/8");                                   // 【Required
】IP address (CIDR format)
        denyRule.put("policy", "deny");                                     // 【Required
```

】`Polic`

```
】Policy
        List<Map<String, Object>> ipBlockRules = new ArrayList<>();
        ipBlockRules.add(allowRule);
        ipBlockRules.add(denyRule);
        Map<String, Object> config = new HashMap<>();
        config.put("isOpenIpBlock", true);                                  // 【Required
】Whether to enable IP allowlist/blocklist
        config.put("ipBlockRules", ipBlockRules);                           // 【Required
】IP rule list
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "IP Allowlist and Blocklist Policy");
        request.put("strategyConfigName", "route-ip-block");
        request.put("config", config);
        return executeCreate(client, request, "IP Allowlist and Blocklist Policy");
```

`}`

```
    /**
     * 7. ACL permission control policy (ACL Permission Control Policy)
     * config structure: RouteACLConfig
```

`*/`

```java
    private static String createAclStrategy(IAcsClient client) throws Exception {
        // ACL rule configuration
        Map<String, Object> allowRule = new HashMap<>();
        allowRule.put("group", "consumer-group-allow");                     // 【Required
】Consumer group/ID
        allowRule.put("policy", "allow");                                   // 【Required
】Policy: allow-allow, deny-deny
        Map<String, Object> denyRule = new HashMap<>();
        denyRule.put("group", "consumer-group-deny");                       // 【Required
】Consumer group/ID
        denyRule.put("policy", "deny");                                     // 【Required
】Policy
        List<Map<String, Object>> aclRules = new ArrayList<>();
        aclRules.add(allowRule);
        aclRules.add(denyRule);
        Map<String, Object> config = new HashMap<>();
        config.put("isEnableACL", true);                                    // 【Required
】Whether to enable ACL permission control
        config.put("aclRules", aclRules);                                   // 【Required
】ACL rule list
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "ACL Permission Control Policy");
        request.put("strategyConfigName", "route-acl");
        request.put("config", config);
```

```
        return executeCreate(client, request, "ACL Permission Control Policy");
```

`}`

```
    /**
     * 8. Mock policy (MOCK Policy)
     * config structure: CacheMockConfig
```

`*/`

```java
    private static String createMockStrategy(IAcsClient client) throws Exception {
        Map<String, Object> config = new HashMap<>();
        config.put("isOpenMock", true);                                     // 【Required
】Whether to enable Mock
        config.put("responseCode", 200);                                    // 【Optional
】Response status code
        config.put("responseBody", "{\"code\":0,\"data\":{\"id\":1}}");     // 【Optiona
l】Response body
        config.put("responseHeader", Arrays.asList(                         // 【Optional
】Response header list
            "Content-Type:application/json",
            "X-Mock:true"
        ));
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "MOCK Policy");
        request.put("strategyConfigName", "route-mock");
        request.put("config", config);
        return executeCreate(client, request, "MOCK Policy");
```

`}`

```
    /**
     * 9. Request tracing policy (Request Tracing Policy)
     * config structure: RouteTracingConfig
```

`*/`

```java
    private static String createTracingStrategy(IAcsClient client) throws Exception {
        Map<String, Object> config = new HashMap<>();
        config.put("isEnableTracing", true);                                // 【Required
】Whether to enable tracing
        config.put("traceHeader", "X-Trace-Id");                            // 【Required
】Tracing header name
        config.put("isEnableDownstream", true);                             // 【Optional
】Whether to pass to downstream services
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Request Tracing Policy");
        request.put("strategyConfigName", "route-tracing");
        request.put("config", config);
        return executeCreate(client, request, "Request Tracing Policy");
```

`}`

```
    /**
     * 10. Request body size limit policy (Request Size Limit Policy)
```

`q` `p` `q`

```
     * config structure: DataSize
```

`*/`

```java
    private static String createRequestSizeStrategy(IAcsClient client) throws Exception
```

`{`

```
        Map<String, Object> config = new HashMap<>();
        config.put("dataSize", "10MB");                                     // 【Required
】Maximum request body size (supports KB/MB/GB units)
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Request Size Limit Policy");
        request.put("strategyConfigName", "route-request-size");
        request.put("config", config);
        return executeCreate(client, request, "Request Size Limit Policy");
```

`}`

```
    // ========== Common operation methods ==========
    /**
     * Execute creation of policy configuration
```

`*/`

```java
    private static String executeCreate(IAcsClient client, Map<String, Object> request,
String strategyName) throws Exception {
        CommonRequest commonRequest =
createBaseRequest("/strategyConfig/createStrategyConfig");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String strategyId = result.getString("data");
            System.out.println("create " + strategyName + " success, strategyId: " + st
rategyId);
            return strategyId;
        } else {
            System.out.println("create " + strategyName + " failed: " +
result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * Query policy configuration list
```

`*/`

```java
    private static void listStrategyConfigs(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("current", 1);
        request.put("size", 10);
```

```java
        CommonRequest commonRequest =
createBaseRequest("/strategyConfig/listStrategyConfigs");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listStrategyConfigs: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Query policy configuration details
```

`*/`

```java
    private static void getStrategyConfig(IAcsClient client, String strategyConfigId) t
hrows Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("strategyConfigId", strategyConfigId);
        request.put("gwInstanceId", GW_INSTANCE_ID);
        CommonRequest commonRequest =
createBaseRequest("/strategyConfig/getStrategyConfig");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getStrategyConfig: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Modify policy configuration status
```

`*/`

```java
    private static void modifyStrategyConfigStatus(IAcsClient client, String
strategyConfigId, boolean isOpen) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("strategyConfigId", strategyConfigId);
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("isOpen", isOpen);
        CommonRequest commonRequest =
createBaseRequest("/strategyConfig/modifyStrategyConfigStatus");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyStrategyConfigStatus: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Delete policy configuration
```

`*/`

```java
    private static void deleteStrategyConfig(IAcsClient client, String
strategyConfigId) throws Exception {
```

```java
        Map<String, Object> request = new HashMap<>();
        request.put("strategyConfigId", strategyConfigId);
        request.put("gwInstanceId", GW_INSTANCE_ID);
        CommonRequest commonRequest =
createBaseRequest("/strategyConfig/deleteStrategyConfig");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteStrategyConfig: " +
response.getHttpResponse().getHttpContentString());
```

`}` `}`

**Policy type description (strategyName)**

The policy type uses the English identifier `strategyName` . Different engines support different policy types.

**SCG policy (for SCG engine)**

| strategyName | Category | Description |
|---|---|---|
| Authentication Policy | Authentication | The system supports authentication methods such as JWT, BASIC, and APIKEY, as well as custom authentication to protect application security. |
| Flow Control Policy | Traffic | The system limits the request rate to prevent a sudden surge of data from overwhelming the network. |
| Timeout Policy | Traffic | The system limits the maximum timeout duration for gateway- forwarded requests. |
| Circuit Breaker Policy | Traffic | The gateway blocks calls to service providers to protect application services. |
| MOCK Policy | Transformation | Set filtering rules and return values to handle data objects that are difficult to construct or obtain. |
| Signature Policy | Security | The system generates signatures for requests passing through the gateway. |

| Cross-domain Policy | Transformation | Documents or scripts from one domain can request resources from another domain through the gateway. |
|---|---|---|
| Caching Policy | Traffic | The system caches responses to avoid repeatedly requesting the same resources from backend services. |
| IP Blacklist and Whitelist Policy | Security | The system restricts source IP addresses of requests to enhance backend service security. |
| Request Tracing Policy | Observability | The system adds request tracing headers to track request chains for requests passing through this gateway. |
| ACL Permission Control Policy | Authentication | The system controls which consumers can access services. |
| Request Size Limit Policy | Traffic | The system limits the maximum size of the request body. |
| HSF Protocol Mapping Policy | Transformation | The system controls the specific HSF method targeted by routing and sets HTTP-to- HSF parameter format mappings. |

|   | IP Blacklist and | Securit |
|---|---|---|
| Whitelist Policy |   |   |

|   | ACL Permission Control | Au |
|---|---|---|
| Policy |   |   |

|   | Request Size Limit |
|---|---|
| Policy |   |

|   | HSF Protocol Mapping |   |
|---|---|---|
| Policy |   |   |

**Higress policies (for Higress engine)**

**Authentication policies**

| strategyName | Description |
|---|---|
| basic-auth | Authenticate and authorize based on the HTTP Basic Auth standard. |
| hmac-auth | Generate signatures based on the HMAC algorithm to authenticate and authorize identities. |

| jwt-auth | Authenticate and authorize based on JSON Web Token. |
|---|---|
| key-auth | Authenticate and authorize identities based on API keys. |
| oauth | Authenticate and authorize based on OAuth2. |
| oidc | Verify user identity based on the OpenID Connect standard. |
| ext-auth | Send authorization requests to external authorization services to check client request permissions. |

**Security policies**

| strategyName | Description |
|---|---|
| bot-detect | Identify and block internet crawlers from scraping site resources. |
| ip-restriction | Restrict access by adding IP addresses to an allowlist or blocklist. |
| request-block | Block HTTP requests based on characteristics such as URI and request headers. |
| request-validation | Validate the body and header data of forwarded requests. |
| waf | Configure WAF rules based on OWASP ModSecurity CRS. |

**Traffic policies**

| strategyName | Description |
|---|---|
| key-rate-limit | Limit traffic based on specific key values. |
| cluster-key-rate-limit | Limit traffic at the cluster level based on specific key values. |

| cache-control | Add Expires and Cache-Control headers to responses. |
|---|---|
| cors | Enable CORS on the server to return HTTP response headers. |

**Transformation policies**

| strategyName | Description |
|---|---|
| custom-response | Configure custom HTTP response status codes, headers, and body. |
| de-graphql | Convert RESTful APIs into GraphQL requests. |
| transformer | Transform request/response headers, query parameters, and body parameters. |
| geo-ip | Query geographic location information based on IP address and pass it to subsequent plugins. |
| frontend-gray | Implement frontend user grayscale functionality for business A/B testing. |
| model-mapper | Map model parameter values in LLM protocols according to specified rules. |
| model-router | Route requests based on the model parameter in LLM protocols. |

**Observability policies**

| strategyName | Description |
|---|---|
| traffic-tag | Tag traffic by adding request headers based on weight or request content. |
| log-request-response | Record request and response information for debugging and monitoring. |

**Other policies**

| strategyName | Description |
|---|---|
| opa | Implement OPA policy control. |

**Policy scope description (scope)**

You can apply policies to different scopes. The priority is: **route > domain > service >**

**consumer > instance.**

| scope | bitMask | Description |
|---|---|---|
| INSTANCE | 1 | Apply the policy to the entire gateway instance. |
| ROUTE | 2 | Apply the policy to a specific route. |
| SERVICE | 4 | Apply the policy to a specific service. |
| CONSUMER | 8 | Apply the policy to a specific consumer. |
| DOMAIN | 16 | Apply the policy to a specific domain. |

**Composite scope**: You can apply a policy to multiple scopes simultaneously. For example,
`scope=3` means applying the policy to both instance and route (INSTANCE + ROUTE = 1 + 2 = 3).

**Response code description**

| code | Description |
|---|---|
| 200 | The operation succeeded. |
| 400 | A parameter error occurred. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

#### API call - Consumer management

**Overview**

The consumer management module lets you create, delete, modify, and query consumers. Consumers handle API authentication and authorization and can bind to routes for access control.
**Applicable engine**: SCG / Higress (engine-agnostic, interface is universal)
**Path prefix**: `/application`

**Authentication method**

**Self-built ACK environment**: Add `X-CSB-TOKEN: csb@2022` and `X-CSB-OPENAPI: true`
to the request header.
**Enterprise Edition environment**: Add `x-acs-organizationid` and `x-acs-caller-sdk-`
`source` to the request header and use a valid AccessKey pair.

**Create a consumer**

**API description**

Create a new consumer (application).

**Request information**

| Item | Content |
|---|---|
| URL | /application/createApp |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| appName | String | Yes | The name of the consumer. |

| authType | Integer | Yes | The authentication type: 1: BASIC 2: OAuth2 3: JWT 4: CUSTOM 5: API KEY _ 6: API GATEWAY _ 7: CSB AUTH _ |
|---|---|---|---|
| key | String | Yes | The authentication key (API key or username). |
| password | String | Conditional | The password. Note Use this parameter for BASIC authentication. |
| description | String | No | The description of the consumer. |
| expireTime | Long | No | The expiration timestamp in milliseconds. A value of null indicates that the key never expires. |

**List consumers**

**API description**

List consumers by page.

**Request information**

| Item | Content |
|---|---|
| URL | /application/listApps |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on AppRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The page number. Start from 1. |
| size | Integer | Yes | The number of entries per page. |
| appName | String | No | The name of the consumer. The system performs a fuzzy search. |
| authType | String | No | The authentication type for filtering. |
| appType | Integer | No | The application category: 0: Backend application 1: Portal application |
| isDisasterRecovery | Boolean | No | Specifies whether to filter disaster recovery consumers. |

**Query consumer details**

**API description**

Query the detailed information based on the consumer ID.

**Request information**

| Item | Content |
|---|---|
| URL | /application/getApp |
| Method | POST |

| Content-Type | application/json |
|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| appId | String | Yes | The ID of the consumer. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify a consumer**

**API description**

Modify the configuration of an existing consumer.

**Request information**

| Item | Content |
|---|---|
| URL | /application/modifyApp |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| appId | String | Yes | The ID of the consumer. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| appName | String | Yes | The name of the consumer. |

| description | String | No | The description of the consumer. |
|---|---|---|---|

**Delete a consumer**

**API description**

Delete the specified consumer.

**Request information**

| Item | Content |
|---|---|
| URL | /application/deleteApp |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| appId | String | Yes | The ID of the consumer. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Delete consumers in batches**

**API description**

Delete multiple consumers in batches.

**Request information**

| Item | Content |
|---|---|
| URL | /application/batchDeleteApp |
| Method | POST |

| Content-Type | application/json |
|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| appIds | List | Yes | The list of consumer IDs. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Refresh token**

**API description**

Refresh the token (authentication credential) of the consumer.

**Request information**

| Item | Content |
|---|---|
| URL | /application/refreshToken |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| appId | String | Yes | The ID of the consumer. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Query all consumers**

**API description**

Query all consumers under the gateway instance without pagination.

**Request information**

| Item | Content |
|---|---|
| URL | /application/listAppsByGwInstanceId |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common Request call examples**

The following examples show how to call the Consumer management API by using the Common Request method. The difference between a self-managed ACK environment and an Enterprise Edition environment lies only in the authentication setting.

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.Arrays; import java.util.HashMap; import java.util.List; import java.util.Map; public class ConsumerApiDemo {
    // ========== Environment configuration (modify according to actual environment) ==
========
    // Self-managed ACK environment configuration
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";
    // Enterprise Edition environment configuration (used when IS_SELF_HOSTED = false)
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
```

```java
    private static final String ORGANIZATION_ID = "your-org-id";
    // Gateway instance ID
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
        // ========== Create consumer (BASIC authentication) ==========
        String appId = createBasicConsumer(client);
        // ========== Create consumer (API Key authentication) ==========
        // String apiKeyAppId = createApiKeyConsumer(client);
        // ========== List consumers ==========
        listApps(client);
        // ========== Get consumer details ==========
        getApp(client, appId);
        // ========== Modify consumer ==========
        modifyApp(client, appId);
        // ========== Delete consumer ==========
        deleteApp(client, appId);
```

`}`

```java
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
```

`}` `}`

```java
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
```

`}`

```java
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
```

`}` `}`

```java
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
```

`t` `tS` `D` `i``(`

```
tEd it())
```

```
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
```

`}`

```
    /**
     * Create BASIC authentication consumer
```

`*/`

```java
    private static String createBasicConsumer(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("appName", "consumer-demo-01");                         // 【Required
】Consumer name
        request.put("authType", 1);                                         // 【Required
】Authentication type: 1-BASIC
        request.put("key", "user-001");                                     // 【Required
】Username
        request.put("password", "secret-password");                         // 【Required
】Password (for BASIC authentication)
        request.put("description", "API consumer application");             // 【Optiona
l】Consumer description
        // request.put("expireTime", 315360000000L);                         // 【Optiona
l】Expiration timestamp (in milliseconds)
        CommonRequest commonRequest = createBaseRequest("/application/createApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String appId = result.getString("data");
            System.out.println("createBasicConsumer success, appId: " + appId);
            return appId;
        } else {
            System.out.println("createBasicConsumer failed: " +
result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * Create API Key authentication consumer
```

`*/`

```java
    private static String createApiKeyConsumer(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】GatewayinstanceID
```

```java
】Gateway instance ID
        request.put("appName", "consumer-apikey-demo");                     //
【Required】Consumer name
        request.put("authType", 5);                                         // 【Required
】Authentication type: 5-API_KEY
        request.put("key", "api-key-xxx");                                  // 【Required
】API Key value
        CommonRequest commonRequest = createBaseRequest("/application/createApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String appId = result.getString("data");
            System.out.println("createApiKeyConsumer success, appId: " + appId);
            return appId;
        } else {
            System.out.println("createApiKeyConsumer failed: " +
result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * List consumers
```

`*/`

```java
    private static void listApps(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("current", 1);                                          // 【Required
】Current page number
        request.put("size", 10);                                            // 【Required
】Number of entries per page
        // request.put("appName", "");                                        //
【Optional】Consumer name (fuzzy search)
        // request.put("authType", "1");                                      //
【Optional】Filter by authentication type
        // request.put("appType", 0);                                         //
【Optional】Application category: 0-backend, 1-portal
        CommonRequest commonRequest = createBaseRequest("/application/listApps");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listApps: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
```

`/`

```
     * Get consumer details
```

`*/`

```java
    private static void getApp(IAcsClient client, String appId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("appId", appId);                                        // 【Required
】Consumer ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/application/getApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getApp: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Modify consumer
```

`*/`

```java
    private static void modifyApp(IAcsClient client, String appId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("appId", appId);                                        // 【Required
】Consumer ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("appName", "consumer-demo-modified");                   //
【Required】Consumer name
        request.put("description", "Updated description");                  //
【Optional】Consumer description
        CommonRequest commonRequest = createBaseRequest("/application/modifyApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyApp: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Delete consumer
```

`*/`

```java
    private static void deleteApp(IAcsClient client, String appId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("appId", appId);                                        // 【Required
】Consumer ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/application/deleteApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
```

```java
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteApp: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Batch delete consumers
```

`*/`

```java
    private static void batchDeleteApps(IAcsClient client, List<String> appIds) throws
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("appIds", appIds);                                      // 【Required
】List of consumer IDs
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/application/batchDeleteApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("batchDeleteApp: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Refresh token
```

`*/`

```java
    private static void refreshToken(IAcsClient client, String appId) throws Exception
```

`{`

```java
        Map<String, Object> request = new HashMap<>();
        request.put("appId", appId);                                        // 【Required
】Consumer ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/application/refreshToken");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("refreshToken: " +
response.getHttpResponse().getHttpContentString());
```

`}` `}`

**Authentication type description**

| authType | Type name | Description |
|---|---|---|

| 1 | BASIC | HTTP Basic authentication with username and password. |
|---|---|---|
| 2 | OAuth2.0 | OAuth2 authentication. |
| 3 | JWT | JWT authentication. |
| 4 | CUSTOM | Custom authentication. |
| 5 | API KEY _ | API Key authentication. |
| 6 | API GATEWAY _ | API gateway authentication. |
| 7 | CSB AUTH _ | CSB authentication. |

**Response code description**

| code | Description |
|---|---|
| 200 | The request succeeded. |
| 400 | The parameters are invalid. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

#### API call - Domain name management

**Overview**

The Domain Name management module lets you create, delete, modify, and query domain names. A domain name configures the access domain name for a gateway to provide external services and supports the HTTP and HTTPS protocols.
**Applicable engine**: SCG / Higress (The API is universal and does not distinguish between
engines.)
**API path prefix**: `/domain`

**Authentication method**

**Self-managed ACK environment**: Add `X-CSB-TOKEN: csb@2022` and `X-CSB-OPENAPI:`
`true` to the request header.
**Enterprise Edition environment**: Add `x-acs-organizationid` and `x-acs-caller-sdk-`
`source` to the request header and use a valid AccessKey pair.

**Create a domain name**

**API description**

Create a new domain name configuration.

**Request information**

| Item | Content |
|---|---|
| URL | /domain/createDomain |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on**

**CreateOrUpdateDomainRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| domain | String | Yes | The domain name, such as api.example.com . |
| protocol | String | Yes | The protocol type: HTTP or HTTPS. |
| certificateId | String | Conditional | The ID of the certificate. Note This parameter is required when you use the HTTPS protocol. |

| caCertificateId | String | No | The ID of the CA certificate. Use this parameter for mutual authentication. |
|---|---|---|---|
| clientAuth | Integer | No | The client authentication type: 0: None 1: Enabled |
| subjectDn | String | No | The header that contains information about the owner of the client certificate. |
| issuerDn | String | No | The header that contains information about the issuer of the client certificate. |

**List domains**

**API description**

List domains by page.

**Request information**

| Item | Content |
|---|---|
| URL | /domain/listDomains |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on ListDomainsRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The page number. The value starts from 1. |

| size | Integer | Yes | The number of entries per page. |
|---|---|---|---|
| domain | String | No | The domain name for fuzzy search. |
| protocol | String | No | The protocol type for filtering. |

**Query domain name details**

**API description**

Query the detailed information of a domain name by its ID.

**Request information**

| Item | Content |
|---|---|
| URL | /domain/getDomain |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on GetDomainRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| domainId | String | Yes | The ID of the domain name. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify a domain name**

**API description**

Modify an existing domain name configuration.

**Request information**

| Item | Content |
|---|---|

| URL | /domain/modifyDomain |
|---|---|
| Method | POST |
| Content-Type | application/json |

Use the same parameters as those for creating a domain name. Additionally, you must specify `domainId` .

**Delete a domain name**

**API description**

Delete the specified domain name.

**Request information**

| Item | Content |
|---|---|
| URL | /domain/deleteDomain |
| Method | POST |
| Content-Type | application/json |

**Request parameters (based on DeleteDomainRequest)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| domainId | String | Yes | The ID of the domain name. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**List all domain names**

**API description**

List all domain names under the gateway instance (without pagination).

**Request information**

| Item | Content |
|---|---|
| URL | /domain/listAllDomains |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common Request call examples**

The following examples show how to use the Common Request method to call the Domain Name management API. The difference between a self-built ACK environment and an Enterprise Edition environment lies only in the Authentication Setting.

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; public class DomainApiDemo {
    // ========== Environment configuration (modify according to actual environment) ==
========
    // Self-hosted ACK environment configuration
    private static final boolean IS_SELF_HOSTED = true;                     // Whether i
t is a self-hosted ACK environment
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";    // Self-hos
ted ACK console address
    // Enterprise Edition environment configuration (used when IS_SELF_HOSTED = false)
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
```

```java
    private static final String ORGANIZATION_ID = "your-org-id";
    // Gateway instance ID
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
        // ========== Create an HTTP Domain Name ==========
        String httpDomainId = createHttpDomain(client);
        // ========== Create an HTTPS Domain Name (with certificate) ==========
        // String httpsDomainId = createHttpsDomain(client);
        // ========== List Domain Names ==========
        listDomains(client);
        // ========== Get Domain Name details ==========
        getDomain(client, httpDomainId);
        // ========== Modify Domain Name ==========
        modifyDomain(client, httpDomainId);
        // ========== Delete Domain Name ==========
        deleteDomain(client, httpDomainId);
```

`}`

```
    /**
     * Create client (common for self-hosted ACK and Enterprise Edition)
```

`*/`

```java
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
```

`}` `}`

```java
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
```

`}`

```java
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
```

`}` `}`

```java
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
```

`}`

```
    /**
     * Create an HTTP Domain Name (based on CreateOrUpdateDomainRequest)
```

`*/`

```java
    private static String createHttpDomain(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        request.put("domain", "api.example.com");                           //
[Required] Domain Name
        request.put("protocol", "HTTP");                                    // [Required]
Protocol type: HTTP
        CommonRequest commonRequest = createBaseRequest("/domain/createDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String domainId = result.getString("data");
            System.out.println("createHttpDomain success, domainId: " + domainId);
            return domainId;
        } else {
            System.out.println("createHttpDomain failed: " + result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * Create an HTTPS Domain Name (with certificate)
```

`*/`

```java
    private static String createHttpsDomain(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        request.put("domain", "secure.example.com");                        //
[Required] Domain Name
        request.put("protocol", "HTTPS");                                   // [Required]
Protocol type: HTTPS
        request.put("certificateId", "cert-id-xxx");                        //
[Required]CertificateID(requiredforHTTPS)
```

```java
[Required] Certificate ID (required for HTTPS)
        // request.put("caCertificateId", "ca-cert-id");                     //
[Optional] CA certificate ID (used for mutual authentication)
        // request.put("clientAuth", 1);                                     // [Optional
] Client Authentication type: 0-none, 1-enabled
        // request.put("subjectDn", "CN=client");                            // [Optional
] Client certificate owner information header
        // request.put("issuerDn", "CN=issuer");                             // [Optional
] Client certificate issuer information header
        CommonRequest commonRequest = createBaseRequest("/domain/createDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String domainId = result.getString("data");
            System.out.println("createHttpsDomain success, domainId: " + domainId);
            return domainId;
        } else {
            System.out.println("createHttpsDomain failed: " + result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * List Domain Names (based on ListDomainsRequest)
```

`*/`

```java
    private static void listDomains(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        request.put("current", 1);                                          // [Required]
Current page number
        request.put("size", 10);                                            // [Required]
Number of entries per page
        // request.put("domain", "example");                                 // [Optional
] Domain Name (fuzzy search)
        // request.put("protocol", "HTTP");                                  // [Optional
] Protocol type filter
        CommonRequest commonRequest = createBaseRequest("/domain/listDomains");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listDomains: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Get Domain Name details (based on GetDomainRequest)
```

```
Get
```

`o``a`

```
aedeta s(basedo Getoa equest)
```

`*/`

```java
    private static void getDomain(IAcsClient client, String domainId) throws Exception
```

`{`

```java
        Map<String, Object> request = new HashMap<>();
        request.put("domainId", domainId);                                  // [Required]
Domain Name ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/domain/getDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getDomain: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Modify Domain Name
```

`*/`

```java
    private static void modifyDomain(IAcsClient client, String domainId) throws Excepti
on {
        Map<String, Object> request = new HashMap<>();
        request.put("domainId", domainId);                                  // [Required]
Domain Name ID to modify
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        request.put("domain", "api-new.example.com");                       //
[Required] Domain Name
        request.put("protocol", "HTTP");                                    // [Required]
Protocol type
        CommonRequest commonRequest = createBaseRequest("/domain/modifyDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonRequest(commonRequest);
        System.out.println("modifyDomain: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Delete Domain Name (based on DeleteDomainRequest)
```

`*/`

```java
    private static void deleteDomain(IAcsClient client, String domainId) throws Excepti
on {
        Map<String, Object> request = new HashMap<>();
        request.put("domainId", domainId);                                  // [Required]
Domain Name ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/domain/deleteDomain");
```

```java
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteDomain: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * List all Domain Names
```

`*/`

```java
    private static void listAllDomains(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/domain/listAllDomains");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listAllDomains: " +
response.getHttpResponse().getHttpContentString());
```

`}` `}`

**Protocol type description**

| protocol | Description |
|---|---|
| HTTP | The HTTP protocol does not require a certificate. |
| HTTPS | The HTTPS protocol requires binding an SSL certificate. |

**Client authentication type description**

| clientAuth | Description |
|---|---|
| 0 | No client authentication. |
| 1 | Enable mutual authentication. |

**Response code description**

| code | Description |
|---|---|
| 200 | The operation succeeded. |
| 400 | The parameter is invalid. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

#### API call - Route plugin management

**Overview**

The route plugin management module provides plugin configuration at the route level. Plugins add extra features to routes, such as request/response processing, authentication, and logging.
**Applicable engine**: SCG only (The Higress engine does not support this API. Use the policy
configuration module instead.)
**API path prefix**: `/route`

**Authentication method**

**Self-managed ACK environment**: Add `X-CSB-TOKEN: csb@2022` and `X-CSB-OPENAPI:`
`true` to the request header.
**Enterprise Edition environment**: Add `x-acs-organizationid` and `x-acs-caller-sdk-`
`source` to the request header, and use a valid AccessKey pair.

**Create a route plugin**

**API call description**

Create a plugin configuration for a route.

**Important**

This applies only to the SCG engine.

**Request information**

| Item | Content |
|---|---|
| URL | /route/createRoutePlugin |
| Method | POST |

| Content-Type | application/json |
|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| routeId | String | Yes | The ID of the route. |
| pluginId | String | Yes | The ID of the plugin. You must query the plugin list first. |
| pluginName | String | Yes | The name of the plugin. |
| pluginConfig | Object | Yes | The configuration of the plugin in JSON format. |
| isOpen | Boolean | No | Specifies whether to enable the plugin. Default value: true. |

**Query the plugin list for a route**

**API call description**

Query the list of plugins under a route.

**Important**

This API call applies only to the SCG engine.

**Request information**

| Item | Content |
|---|---|
| URL | /route/listRoutePlugins |
| Method | POST |

| Content-Type | application/json |
|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| routeId | String | Yes | The ID of the route. |
| current | Integer | Yes | The current page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |

**Modify route plugin**

**API description**

Modify the plugin configuration of a route.

**Important**

This applies only to the SCG engine.

**Request information**

| Item | Content |
|---|---|
| URL | /route/modifyRoutePlugin |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|

| gwInstanceId | String | Yes | The ID of the gateway instance. |
|---|---|---|---|
| routeId | String | Yes | The ID of the route. |
| routePluginId | String | Yes | The ID of the route plugin. |
| pluginConfig | Object | Yes | The new plugin configuration. |

**Modify route plugin status**

**API description**

Enable or disable the route plugin.

**Important**

This feature applies only to the SCG engine.

**Request information**

| Item | Content |
|---|---|
| URL | /route/modifyRoutePluginStatus |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| routeId | String | Yes | The ID of the route. |
| routePluginId | String | Yes | The ID of the route plugin. |

| isOpen | Boolean | Yes | true: Enable the plugin. false: Disable the plugin. |
|---|---|---|---|

**Delete route plugin**

**API description**

Delete the plugin configuration of a route.

**Important**

This feature applies only to the SCG engine.

**Request information**

| Item | Content |
|---|---|
| URL | /route/deleteRoutePlugin |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| routeId | String | Yes | The ID of the route. |
| routePluginId | String | Yes | The ID of the route plugin. |

**Common request call example**

The following example shows how to use the Common Request method to call the route Plugin management API. The difference between a self-hosted ACK environment and an Enterprise Edition environment lies only in the authentication parameter settings.

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse;
```

`p` `p`

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; public class RoutePluginApiDemo {
    // ========== Environment configuration (modify according to actual environment) ==
========
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-h****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    private static final String ROUTE_ID = "your-route-id";
    private static final String PLUGIN_ID = "your-plugin-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
        // ========== Create route Plugin ==========
        String routePluginId = createRoutePlugin(client);
        // ========== List route Plugins ==========
        listRoutePlugins(client);
        // ========== Modify route Plugin ==========
        modifyRoutePlugin(client, routePluginId);
        // ========== Modify route Plugin status ==========
        modifyRoutePluginStatus(client, routePluginId, false);
        // ========== Delete route Plugin ==========
        deleteRoutePlugin(client, routePluginId);
```

`}`

```java
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
```

`}` `}`

```java
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
```

`}`

```java
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
```

`}` `}`

```java
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
```

`}`

```
    /**
     * Create route Plugin
```

`*/`

```java
    private static String createRoutePlugin(IAcsClient client) throws Exception {
        // Plugin configuration example (Header modification Plugin)
        Map<String, Object> pluginConfig = new HashMap<>();
        Map<String, Object> addHeaders = new HashMap<>();
        addHeaders.put("X-Custom-Header", "custom-value");
        pluginConfig.put("addHeaders", addHeaders);
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("routeId", ROUTE_ID);                                   // 【Required
】Route ID
        request.put("pluginId", PLUGIN_ID);                                 // 【Required
】Plugin ID
        request.put("pluginName", "request-header-modifier");               //
【Required】Plugin name
        request.put("pluginConfig", pluginConfig);                          // 【Required
】Plugin configuration
        request.put("isOpen", true);                                        // 【Optional
】Whether to enable
        CommonRequest commonRequest = createBaseRequest("/route/createRoutePlugin");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
```

```java
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String routePluginId = result.getString("data");
            System.out.println("createRoutePlugin success, routePluginId: " +
routePluginId);
            return routePluginId;
        } else {
            System.out.println("createRoutePlugin failed: " + result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * List route Plugins
```

`*/`

```java
    private static void listRoutePlugins(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("routeId", ROUTE_ID);                                   // 【Required
】Route ID
        request.put("current", 1);                                          // 【Required
】Current page number
        request.put("size", 10);                                            // 【Required
】Number of entries per page
        CommonRequest commonRequest = createBaseRequest("/route/listRoutePlugins");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listRoutePlugins: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Modify route Plugin
```

`*/`

```java
    private static void modifyRoutePlugin(IAcsClient client, String routePluginId) thro
ws Exception {
        Map<String, Object> pluginConfig = new HashMap<>();
        Map<String, Object> addHeaders = new HashMap<>();
        addHeaders.put("X-Custom-Header", "new-value");
        pluginConfig.put("addHeaders", addHeaders);
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("routeId", ROUTE_ID);                                   // 【Required
】Route ID
```

`//`【`R` `t`

```
t(" tPl iId" tPl iId)
```

`i` `d`

```java
        request.put("routePluginId", routePluginId);                        // 【Required
】Route Plugin ID
        request.put("pluginConfig", pluginConfig);                          // 【Required
】New Plugin configuration
        CommonRequest commonRequest = createBaseRequest("/route/modifyRoutePlugin");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyRoutePlugin: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Modify route Plugin status
```

`*/`

```java
    private static void modifyRoutePluginStatus(IAcsClient client, String
routePluginId, boolean isOpen) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("routeId", ROUTE_ID);                                   // 【Required
】Route ID
        request.put("routePluginId", routePluginId);                        // 【Required
】Route Plugin ID
        request.put("isOpen", isOpen);                                      // 【Required
】true to enable, false to disable
        CommonRequest commonRequest =
createBaseRequest("/route/modifyRoutePluginStatus");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyRoutePluginStatus: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Delete route Plugin
```

`*/`

```java
    private static void deleteRoutePlugin(IAcsClient client, String routePluginId) thro
ws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【Required
】Gateway instance ID
        request.put("routeId", ROUTE_ID);                                   // 【Required
】Route ID
        request.put("routePluginId", routePluginId);                        // 【Required
】Route Plugin ID
        CommonRequest commonRequest = createBaseRequest("/route/deleteRoutePlugin");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatTypeJSON);
```

```java
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteRoutePlugin: " +
response.getHttpResponse().getHttpContentString());
```

`}` `}`

**Notes**

The route Plugin applies only to the SCG engine. Use the policy configuration module for the Higress engine. Query the Plugin list to obtain a valid `pluginId` before you create a route Plugin. The Plugin configuration format varies depending on the Plugin type.

**Response code description**

| code | Description |
|---|---|
| 200 | The operation succeeded. |
| 400 | A parameter error occurred. |
| 403 | You do not have sufficient permissions. |
| 500 | An internal server error occurred. |

#### API call - Certificate management

**Overview**

The certificate management module manages SSL/TLS certificates. You can create, delete, modify, and query certificates. Use certificates to configure HTTPS domains. The module supports server certificates and CA certificates.
**Applicable engine**: SCG / Higress (engines are not distinguished; the API is universal)
**API path prefix**: `/certificate`

**Authentication method**

**Self-managed ACK environment**: Add `X-CSB-TOKEN: csb@2022` and `X-CSB-OPENAPI:`
`true` to the request header.
**Enterprise Edition environment**: Add `x-acs-organizationid` and `x-acs-caller-sdk-`
`source` to the request header. Also, use a valid AccessKey pair.

**Create a certificate**

**API call description**

Create an SSL/TLS certificate.

**Request information**

| Item | Content |
|---|---|
| URL | /certificate/createCertificate |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| name | String | Yes | The name of the certificate. |
| certType | Integer | Yes | The type of the certificate: 0: Server certificate 1: CA certificate |
| cert | String | Yes | The content of the certificate in PEM format. |
| key | String | Conditional | The content of the private key. Note This parameter is required for server certificates. |

**Query the certificate list**

**API call description**

Query certificates by page.

**Request information**

| Item | Content |
|---|---|
| URL | /certificate/listCertificates |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| gwInstanceId | String | Yes | The ID of the gateway instance. |
| current | Integer | Yes | The page number. The value starts from 1. |
| size | Integer | Yes | The number of entries per page. |
| name | String | No | The certificate name for fuzzy search. |
| certType | Integer | No | The filter for certificate type. |

**Query certificate details**

**API call description**

Query detailed information by certificate ID.

**Request information**

| Item | Content |
|---|---|

| URL | /certificate/getCertificate |
|---|---|
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| certificateId | String | Yes | The ID of the certificate. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Modify a certificate**

**API call description**

Modify an existing certificate configuration.

**Request information**

| Item | Content |
|---|---|
| URL | /certificate/modifyCertificate |
| Method | POST |
| Content-Type | application/json |

These parameters are the same as those for creating a certificate. You must also specify

```
 certificateId .
```

**Delete a certificate**

**API call description**

Delete the specified certificate.

**Request information**

| Item | Content |
|---|---|
| URL | /certificate/deleteCertificate |
| Method | POST |
| Content-Type | application/json |

| Parameter | Type | Required | Description |
|---|---|---|---|
| certificateId | String | Yes | The ID of the certificate. |
| gwInstanceId | String | Yes | The ID of the gateway instance. |

**Common Request call examples**

The following examples show how to call the Certificate API by using the Common Request method. The difference between a self-managed ACK environment and an Enterprise Edition environment lies only in the authentication setting.

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; public class CertificateApiDemo {
    // ========== Environment configuration (modify according to your actual
environment) ==========
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
privatestaticfinalStringORGANIZATIONID="your-org-id";
```

```java
    private static final String ORGANIZATION_ID = yourorgid;
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
        // ========== Create a server certificate ==========
        String certId = createServerCertificate(client);
        // ========== Create a CA certificate ==========
        // String caCertId = createCACertificate(client);
        // ========== List certificates ==========
        listCertificates(client);
        // ========== Get certificate details ==========
        getCertificate(client, certId);
        // ========== Delete a certificate ==========
        deleteCertificate(client, certId);
```

`}`

```java
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
```

`}` `}`

```java
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
```

`}`

```java
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
```

`}` `}`

```java
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
```

`q` `(` );

```
        setAuthHeaders(request);
        return request;
```

`}`

```
    /**
     * Create a server certificate
```

`*/`

```java
    private static String createServerCertificate(IAcsClient client) throws Exception {
        // Certificate content in PEM format (replace with real certificate content in
practice)
        String certContent = "-----BEGIN CERTIFICATE-----\n" +
                "**********************" +
                "-----END CERTIFICATE-----";
        String keyContent = "-----BEGIN PRIVATE KEY-----\n" +
                "**********************\n" +
                "-----END PRIVATE KEY-----";
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        request.put("name", "my-server-cert");                              // [Required]
Certificate name
        request.put("certType", 0);                                         // [Required]
Certificate type: 0 - Server certificate
        request.put("cert", certContent);                                   // [Required]
Certificate content (PEM format)
        request.put("key", keyContent);                                     // [Required]
Private key content (required for server certificate)
        CommonRequest commonRequest =
createBaseRequest("/certificate/createCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String certId = result.getString("data");
            System.out.println("createServerCertificate success, certId: " + certId);
            return certId;
        } else {
            System.out.println("createServerCertificate failed: " +
result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * Create a CA certificate
```

`*/`

```java
    private static String createCACertificate(IAcsClient client) throws Exception {
```

```java
        String caCertContent = "-----BEGIN CERTIFICATE-----\n" +
                "MIIBkTCB+wIJAKHHCgVZUffVMA0GCSqGSIb3DQEBCwUAMBExDzANBglghkgBZQME\n" +
                "-----END CERTIFICATE-----";
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        request.put("name", "my-ca-cert");                                  // [Required]
Certificate name
        request.put("certType", 1);                                         // [Required]
Certificate type: 1 - CA certificate
        request.put("cert", caCertContent);                                 // [Required]
Certificate content (PEM format)
        CommonRequest commonRequest =
createBaseRequest("/certificate/createCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String certId = result.getString("data");
            System.out.println("createCACertificate success, certId: " + certId);
            return certId;
        } else {
            System.out.println("createCACertificate failed: " +
result.getString("msg"));
            return null;
```

`}` `}`

```
    /**
     * List certificates
```

`*/`

```java
    private static void listCertificates(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        request.put("current", 1);                                          // [Required]
Current page number
        request.put("size", 10);                                            // [Required]
Number of entries per page
        // request.put("name", "");                                            //
[Optional] Certificate name (fuzzy search)
        // request.put("certType", 1);                                         //
[Optional] Filter by certificate type
        CommonRequest commonRequest =
createBaseRequest("/certificate/listCertificates");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
```

```java
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listCertificates: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Get certificate details
```

`*/`

```java
    private static void getCertificate(IAcsClient client, String certificateId) throws
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("certificateId", certificateId);                        //
[Required] Certificate ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        CommonRequest commonRequest = createBaseRequest("/certificate/getCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getCertificate: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Modify a certificate
```

`*/`

```java
    private static void modifyCertificate(IAcsClient client, String certificateId) thro
ws Exception {
        String certContent = "-----BEGIN CERTIFICATE-----\n...new certificate content...
\n-----END CERTIFICATE-----";
        String keyContent = "-----BEGIN PRIVATE KEY-----\n...new private key content...\
n-----END PRIVATE KEY-----";
        Map<String, Object> request = new HashMap<>();
        request.put("certificateId", certificateId);                        //
[Required] Certificate ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        request.put("name", "my-server-cert-modified");                     //
[Required] Certificate name
        request.put("certType", 1);                                         // [Required]
Certificate type
        request.put("cert", certContent);                                   // [Required]
Certificate content
        request.put("key", keyContent);                                     // [Required]
Private key content
        CommonRequest commonRequest =
createBaseRequest("/certificate/modifyCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
```

```java
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyCertificate: " +
response.getHttpResponse().getHttpContentString());
```

`}`

```
    /**
     * Delete a certificate
```

`*/`

```java
    private static void deleteCertificate(IAcsClient client, String certificateId) thro
ws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("certificateId", certificateId);                        //
[Required] Certificate ID
        request.put("gwInstanceId", GW_INSTANCE_ID);                        //
[Required] Gateway instance ID
        CommonRequest commonRequest =
createBaseRequest("/certificate/deleteCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteCertificate: " +
response.getHttpResponse().getHttpContentString());
```

`}` `}`

**Certificate type description**

| certType | Type name | Description |
|---|---|---|
| 0 | Server Certificate | Use this certificate for HTTPS domains. You must provide both the certificate and the private key. |
| 1 | CA Certificate | Use this certificate for mutual TLS authentication. |

**Response code description**

| code | Description |
|---|---|
| 200 | The request succeeded. |
| 400 | A parameter error occurred. |

| 403 | You do not have sufficient permissions. |
|---|---|
| 500 | An internal server error occurred. |

## API Gateway

### Cluster management

#### ListClusters

Queries a list of clusters.

**Request headers**

This operation has no special request headers. For more information about common request headers, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| current | Integ er | Body | No | 1 | The current page number. |
| size | Integ er | Body | No | 100 | The size |
| clusterNa me | Strin g | Body | No | my-cluster | The name of the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -records | Array | [] | The list of records. |
| -- k8sClusterCod e | String | k8s-cluster-001 | The code of the Kubernetes cluster. |

| -- k8sClusterNa me | String | production-cluster | The name of the Kubernetes cluster. |
|---|---|---|---|
| --masterUrl | String | https://k8s- master.example.co m:6443 | The URL of the master node. |
| -- k8sClusterStat us | Integer | 1 | The status of the Kubernetes cluster. |
| -- k8sClusterStat usDesc | String | running | The description of the Kubernetes cluster status. |
| -- k8sClusterImp ortDateTime | String | 2024-10-14 10:00:00 | The time when the Kubernetes cluster was imported. |
| -- k8sClusterTyp e | String | ACK | The type of the Kubernetes cluster. |
| -- k8sClusterAttri bute | Struct | {} | The properties of the Kubernetes cluster. |
| ---csClusterId | String | c-123456abcdef | The ID of the container service cluster. |
| --- csClusterNam e | String | prod-k8s-cluster | The name of the container service cluster. |
| ---slbType | String | alb | The type of the Server Load Balancer. |
| ---vpcId | String | vpc-bp1234567890 | The ID of the VPC. |
| ---mappingIP | String | 10.0.0.1 | The mapped IP address. |
| ---mappingPort | Integer | 8080 | The mapped port. |
| ---tunnelName | String | vpn-tunnel-001 | The name of the channel. |

| -total | Integer | 1000 | The total number of entries. |
|---|---|---|---|
| -current | Integer | 1 | The current page number. |
| -size | Integer | 100 | The size. |

#### GetK8sClusterInfoByGwInstanceId

Queries Kubernetes cluster information based on a gateway instance ID.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |
| data | Struct | {} | The data. |
| - k8sClusterCod e | String | k8s-cluster-001 | The code of the Kubernetes cluster. |
| - k8sClusterNa me | String | production-cluster | The name of the Kubernetes cluster. |
| -masterUrl | String | https://k8s- master.example.co m:6443 | The URL of the master node. |

| - k8sClusterStat us | Integer | 1 | The status of the Kubernetes cluster. |
|---|---|---|---|
| - k8sClusterStat usDesc | String | Running | The description of the Kubernetes cluster status. |
| - k8sClusterImp ortDateTime | String | 2024-10-14 10:00:00 | The time when the Kubernetes cluster was imported. |

#### GetK8sClusterName

Queries the name of a Kubernetes cluster.

**Request headers**

This operation has no special request headers. For more information about common request headers, see Common request parameters.

| Parameter name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message |
| data | String | {} | The returned data. |

#### ImportCluster

Imports a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| configCont ent | Strin g | Body | No | key=value | The configuration content. |
| k8sCluster Name | Strin g | Body | No | production-cluster | The name of the Kubernetes cluster. |
| k8sCluster Type | Strin g | Body | No | ACK | The type of the Kubernetes cluster. |
| k8sCluster Attribute | Json | Body | No | {} | The properties of the Kubernetes cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | String | {} | The data |

#### UpdateCluster

Updates a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| clusterCod e | Strin g | Body | No | cluster-001 | The cluster code. |
|---|---|---|---|---|---|
| k8sCluster Attribute | Strin g | Body | No | {} | The properties of the Kubernetes cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### CancelImportCluster

Cancels the import of a cluster.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| k8sCluster Code | Strin g | Body | No | k8s-cluster-001 | The code of the Kubernetes cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Map | {} | The data |

| Developer Guide·A | PI Gateway |   | API Gatewa |
|---|---|---|---|

#### CheckConnectCluster

Checks the connection status of a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| configCont ent | Strin g | Body | No | key=value | The configuration content. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message |
| data | Struct | {} | The data |
| -connectStatus | Integer | 1 | The connection status. |
| - connectStatus Desc | String | Connected | The description of the connection status. |

#### ListK8sAllNamespaces

Queries all namespaces in the Kubernetes.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| clusterCod e | Strin g | Body | No | cluster-001 | The cluster code. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Map | {} | The returned data. |

#### ListAllNamespaces

Lists all namespaces.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| sourceId | Strin g | Body | No | src-123456 | The source ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array | {} | The data. |
| -namespaceId | String | ns-abc123 | The namespace ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - namespaceNa me | String | Production environment | The namespace name. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |

### Instance Management

#### ListInstances

Queries a list of instances.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| current | Integ er | Body | No | 1 | The current page number. |
| size | Integ er | Body | No | 100 | The size. |
| name | Strin g | Body | No | my-resource | The name of the resource. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| deployMod e | Strin g | Body | No | rolling | The deployment mode. |
| status | Integ er | Body | No | 1 | The status. |
| brokerEngi neType | Strin g | Body | No | RocketMQ | The type of the message engine. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Struct | {} | The data |
| -records | Array | [] | The list of records. |
| --accessMode | Array | [] | The list of access modes. |
| ---ips | String | [] | The list of IP addresses. |
| ---ports | String | [] | The list of ports. |
| ---externalIps | String | [] | The list of external IP addresses. |
| ---clusterIp | String | [] | The list of cluster IP addresses. |
| --- accessModeTy pe | String | public | The type of the access mode. |
| --- loadBalancerN etworkType | String | public | The network type of the Server Load Balancer (SLB) instance. |
| --- loadBalancerA ddressType | String | internet | The address type of the SLB instance. |
| --- serviceName | String | user-service | The name of the service. |
| --edasAppInfos | Array | [] | The list of EDAS application information. |
| ---appId | String | 12345678 | The ID of the application. |

| --- edasNamespa ceId | String | edas-ns-001 | The ID of the EDAS namespace. |
|---|---|---|---|
| ---k8sClusterId | String | c-abc123def456 | The ID of the Kubernetes cluster. |
| --- k8sNamespac e | String | default | The Kubernetes namespace. |
| --status | Integer | 1 | The status. |
| --gwInstanceId | String | i- c0a81bb16a1524a 17 | The ID of the gateway instance. |
| --name | String | my-resource | The name. |
| -- instanceName | String | instance-001 | The name of the instance. |
| -- deployCluster Namespace | String | production | The namespace of the deployment cluster. |
| -- deployCluster Code | String | deploy-cluster-001 | The code of the deployment cluster. |
| -- deployCluster Name | String | Production cluster | The name of the deployment cluster. |
| -- k8sServiceNa me | String | my-service | The name of the Kubernetes service. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --modifyTime | String | 2024-10-14 12:30:00 | The update time. |
| --tid | String | t-123456789 | The ID of the task. |

| --vpcId | String | vpc-bp1234567890 | The ID of the VPC. |
|---|---|---|---|
| --regionId | String | cn-hangzhou | The ID of the region. |
| --zoneId | String | cn-hangzhou-b | The ID of the zone. |
| --deployMode | String | rolling | The deployment mode. |
| --edasAppId | String | edas-app-123456 | The ID of the EDAS application. |
| -- edasNamespa ceId | String | edas-ns-001 | The ID of the EDAS namespace. |
| --k8sClusterId | String | c-abc123def456 | The ID of the Kubernetes cluster. |
| -- k8sNamespac e | String | default | The Kubernetes namespace. |
| -- instanceClass | String | ecs.g6.large | The instance type. |
| --department | String | Technology department | The department. |
| -- resourceGroup | String | rg-default | The resource group. |
| -- ingressClassN ame | String | nginx | The class name of the Ingress. |
| -- brokerEngineT ype | String | RocketMQ | The type of the message engine. |
| -- brokerEngineV ersion | String | 5.0 | The version of the message engine. |
| -- brokerLatestE ngineVersion | String | 5.1.0 | The latest version of the message engine. |

| -- deployCluster Attribute | String | {"zone":"cn- hangzhou-a"} | The attributes of the deployment cluster. |
|---|---|---|---|
| --nodeNumber | Integer | 5 | The number of nodes. |
| -- sharedInstanc e | Boolean | false | Indicates whether the instance is a shared instance. |
| -- sharedInstanc eSource | String | aliyun | The source of the shared instance. |
| --vSwitchId | String | vsw- bp1234567890 | The ID of the vSwitch. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The number of the current page. |
| -size | Integer | 100 | The size. |

#### ListAllInstances

Queries a list of all instances.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array | {} | The data. |
| -accessMode | Array | [] | A list of access modes. |
| --ips | String | [] | A list of IP addresses. |
| --ports | String | [] | A list of ports. |

| --externalIps | String | [] | A list of external IP addresses. |
|---|---|---|---|
| --clusterIp | String | [] | A list of cluster IP addresses. |
| -- accessModeTy pe | String | public | The access mode type. |
| -- loadBalancerN etworkType | String | public | The network type of the Server Load Balancer instance. |
| -- loadBalancerA ddressType | String | internet | The address type of the Server Load Balancer instance. |
| --serviceName | String | user-service | The service name. |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | The gateway instance ID. |
| -name | String | my-resource | The name. |
| -status | Integer | 1 | The status. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

#### ListInstancesByServiceId

This operation queries a list of instances.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| serviceId | Strin g | Body | No | service-123456 | The service ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -serviceStruct | Map | {} | The service structure. |
| -instanceList | Map | {} | The list of instances. |

#### GetInstanceInfo

Queries information about an instance.

**Request headers**

This operation uses only common request headers. For more information, see the Common Request Parameters document.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |

| msg | String | Operation successful | The message. |
|---|---|---|---|
| data | Struct | {} | The data. |
| -accessMode | Array | [] | The list of access modes. |
| --ips | String | [] | The list of IP addresses. |
| --ports | String | [] | The list of ports. |
| --externalIps | String | [] | The list of external IP addresses. |
| --clusterIp | String | [] | The list of cluster IP addresses. |
| -- accessModeTy pe | String | public | The access mode type. |
| -- loadBalancerN etworkType | String | public | The network type of the Server Load Balancer (SLB) instance. |
| -- loadBalancerA ddressType | String | internet | The address type of the SLB instance. |
| --serviceName | String | user-service | The service name. |
| -edasAppInfos | Array | [] | The list of EDAS application information. |
| --appId | String | 12345678 | The application ID. |
| -- edasNamespa ceId | String | edas-ns-001 | The ID of the EDAS namespace. |
| --k8sClusterId | String | c-abc123def456 | The ID of the Kubernetes cluster. |
| -- k8sNamespac e | String | default | The Kubernetes namespace. |

| -status | Integer | 1 | The status. |
|---|---|---|---|
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | The gateway instance ID. |
| -name | String | my-resource | The name. |
| - instanceName | String | instance-001 | The instance name. |
| - deployCluster Namespace | String | production | The namespace of the deployment cluster. |
| - deployCluster Code | String | deploy-cluster-001 | The code of the deployment cluster. |
| - deployCluster Name | String | Production Cluster | The name of the deployment cluster. |
| - k8sServiceNa me | String | my-service | The name of the Kubernetes service. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -modifyTime | String | 2024-10-14 12:30:00 | The modification time. |
| -tid | String | t-123456789 | The task ID. |
| -vpcId | String | vpc-bp1234567890 | The ID of the VPC. |
| -regionId | String | cn-hangzhou | The region ID. |
| -zoneId | String | cn-hangzhou-b | The zone ID. |
| -deployMode | String | rolling | The deployment mode. |

| -edasAppId | String | edas-app-123456 | The ID of the EDAS application. |
|---|---|---|---|
| - edasNamespa ceId | String | edas-ns-001 | The ID of the EDAS namespace. |
| -k8sClusterId | String | c-abc123def456 | The ID of the Kubernetes cluster. |
| - k8sNamespac e | String | default | The Kubernetes namespace. |
| -instanceClass | String | ecs.g6.large | The instance type. |
| -department | String | Technical Department | The department. |
| - resourceGroup | String | rg-default | The resource group. |
| - ingressClassN ame | String | nginx | The Ingress class name. |
| - brokerEngineT ype | String | RocketMQ | The message engine type. |
| - brokerEngineV ersion | String | 5.0 | The message engine version. |
| - brokerLatestE ngineVersion | String | 5.1.0 | The latest version of the message engine. |
| - deployCluster Attribute | String | {"zone":"cn- hangzhou-a"} | The properties of the deployment cluster. |
| -nodeNumber | Integer | 5 | The number of nodes. |
| - sharedInstanc e | Boolean | false | Indicates whether the instance is a shared instance. |

| - sharedInstanc eSource | String | Alibaba Cloud | The source of the shared instance. |
|---|---|---|---|
| -vSwitchId | String | vsw- bp1234567890 | The ID of the virtual switch. |

#### CreateInstance

Creates an instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eName | Strin g | Body | No | Production Gateway Instance | The name of the gateway instance. |
| clusterCod e | Strin g | Body | No | cluster-001 | The code of the cluster. |
| deployCon figContent | Strin g | Body | No | replicas: 3 image: nginx:latest | The content of the deployment configuration. |
| accessMod eConfigCo ntent | Strin g | Body | No | mode: public enabled: true | The content of the access mode configuration. |
| namespac e | Strin g | Body | No | prod-ns | The namespace |
| vpcId | Strin g | Body | No | vpc-bp1234567890 | The ID of the VPC. |
| vswId | Strin g | Body | No | vsw-1234567890 | The ID of the vSwitch. |
| ingressNa me | Strin g | Body | No | my-ingress | The name of the Ingress. |

| brokerEngi neType | Strin g | Body | No | RocketMQ | The type of the message engine. |
|---|---|---|---|---|---|
| instanceCl ass | Strin g | Body | No | ecs.g6.large | The instance type. |
| instanceN umber | Strin g | Body | No | INS20240101001 | The instance number. |
| o11y | Json | Body | No | {"enabled":true,"metrics" :"prometheus"} | The observability configuration. |
| deployMod e | Strin g | Body | No | rolling | The deployment mode. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### AscmCreateInstance

Creates an instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eName | Strin g | Body | No | production-gateway- instance | The gateway instance name. |
| clusterCod e | Strin g | Body | No | cluster-001 | Cluster code. |

| instanceN umber | Strin g | Body | No | INS20240101001 | Instance number. |
|---|---|---|---|---|---|
| instanceCl ass | Strin g | Body | No | ecs.g6.large | Instance type. |
| vpcId | Strin g | Body | No | vpc-bp1234567890 | VPC ID. |
| backupZon eId | Strin g | Body | No | cn-hangzhou-h | Backup zone ID. |
| backupVS witchId | Strin g | Body | No | vsw-bp1234567890 | Backup vSwitch ID. |
| thirdZoneI d | Strin g | Body | No | cn-hangzhou-c | Third zone ID. |
| thirdVSwit chId | Strin g | Body | No | vsw-third-001 | Third zone vSwitch ID. |
| zoneType | Strin g | Body | No | primary | Zone type. |
| uid | Strin g | Body | No | user-1234567890 | User ID. |
| deployMod e | Strin g | Body | No | rolling | Deployment mode. |
| edasName spaceId | Strin g | Body | No | edas-ns-001 | EDAS namespace ID. |
| k8sClusterI d | Strin g | Body | No | c-abc123def456 | Kubernetes cluster ID. |
| k8sNames pace | Strin g | Body | No | default | Kubernetes namespace. |
| edasAppIn fos | Repe atLis t | Body | No | [] | A list of EDAS application information. |

| -appId | Strin g | Body | No | 12345678 | Application ID. |
|---|---|---|---|---|---|
| - edasName spaceId | Strin g | Body | No | edas-ns-001 | EDAS namespace ID. |
| - k8sClusterI d | Strin g | Body | No | c-abc123def456 | Kubernetes cluster ID. |
| - k8sNames pace | Strin g | Body | No | default | Kubernetes namespace. |
| deployCon figContent | Strin g | Body | No | replicas: 3 image: nginx:latest | Deployment configuration content. |
| accessMod eConfigCo ntent | Strin g | Body | No | mode: public enabled: true | Access mode configuration content. |
| namespac e | Strin g | Body | No | prod-ns | Namespace. |
| brokerEngi neType | Strin g | Body | No | RocketMQ | Message engine type. |
| ingressCla ssName | Strin g | Body | No | nginx | Ingress class name. |
| o11y | Json | Body | No | {"enabled":true,"metrics" :"prometheus"} | Observability configuration. |
| Departme nt | Strin g | Body | No | 1 | Department ID. |
| ResourceG roup | Strin g | Body | No | rg-acfmxazb4ph6aiy | Resource group. |
| RegionId | Strin g | Body | No | cn-hangzhou | Region ID. |
| ZoneId | Strin g | Body | No | cn-hangzhou-a | Zone ID. |

| vSwitchId | Strin g | Body | No | vsw-bp1234567890 | vSwitch ID. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | String | {} | The data. |

#### ModifyInstance

Modifies an instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| instanceNa me | Strin g | Body | No | instance-001 | The name of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Boolean | {} | The data. |

| PI Gateway |   |   | Developer Guide·API Gatewa |
|---|---|---|---|

#### ModifyInstanceImageUrl

Modifies the image URL of an instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| imageUrl | Strin g | Body | No | https://example.com/logo .png | The URL of the image. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Boolean | {} | The data. |

#### UpgradeInstance

Upgrades an instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the Common Request Parameters document.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Map | {} | The data. |

#### DeleteInstance

Deletes an instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| forcedDele te | Bool ean | Body | No | false | Specifies whether to force delete the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Map | {} | The data. |

| PI Gateway |   |   | Developer Guide·API Gatewa |
|---|---|---|---|

#### RestartInstance

Restarts an instance.

**Request headers**

This operation includes only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Map | {} | The data. |

#### StopInstance

Stops an instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Boolean | {} | The data. |

#### RefreshInstance

Refreshes an instance.

**Request headers**

This operation uses only common request headers. For more information about these headers, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eCode | Strin g | Body | No | gw-instance-001 | The code of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The status code. |
| msg | String | Operation successful | The message |
| data | Struct | {} | The returned data. |
| -accessMode | Array | [] | The list of access modes. |
| --ips | String | [] | The list of IP addresses. |

| --ports | String | [] | The list of ports. |
|---|---|---|---|
| --externalIps | String | [] | The list of external IP addresses. |
| --clusterIp | String | [] | The list of cluster IP addresses. |
| -- accessModeTy pe | String | public | The type of the access mode. |
| -status | Integer | 1 | The status. |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | The ID of the gateway instance. |
| -name | String | my-resource | The name. |
| - deployCluster Namespace | String | production | The namespace of the deployment cluster. |
| - deployCluster Code | String | deploy-cluster-001 | The code of the deployment cluster. |
| - deployCluster Name | String | Production Cluster | The name of the deployment cluster. |
| - k8sServiceNa me | String | my-service | The name of the Kubernetes service. |
| -createTime | String | 2024-10-14 08:00:00 | TThe creation time. |
| -modifyTime | String | 2024-10-14 12:30:00 | The update time. |
| -tid | String | t-123456789 | The task ID. |

#### CreateInstanceDeployConfig

Creates an instance deployment configuration.

**Request headers**

This operation uses common request headers. Special request headers are not required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| cpuReques t | Strin g | Body | No | 1000m | The CPU request. |
| cpuLimit | Strin g | Body | No | 2000m | The CPU limit. |
| memoryRe quest | Strin g | Body | No | 512Mi | The memory request. |
| memoryLi mit | Strin g | Body | No | 1Gi | The memory limit. |
| replicas | Integ er | Body | No | 3 | The number of replicas. |
| jvmArgs | Strin g | Body | No | -Xms512m -Xmx1024m | The JVM parameters. |
| gwInstanc eName | Strin g | Body | No | Production Gateway Instance | The name of the gateway instance. |
| accessMod eType | Strin g | Body | No | public | The access mode type. |
| ports | Repe atLis t | Body | No | [] | The list of ports. |
| -port | Integ er | Body | No | 8080 | The port number. |
| -targetPort | Strin g | Body | No | 8080 | The target port. |

| -nodePort | Integ er | Body | No | 30080 | The node port. |
|---|---|---|---|---|---|
| -name | Strin g | Body | No | my-resource | The name. |
| -protocol | Strin g | Body | No | HTTP | The protocol. |
| namespac e | Strin g | Body | No | prod-ns | The namespace. |
| externalTr afficPolicy | Strin g | Body | No | Local | The external traffic policy. |
| ipType | Strin g | Body | No | IPv4 | The IP type. |
| vpcId | Strin g | Body | No | vpc-bp1234567890 | The ID of the VPC. |
| vswId | Strin g | Body | No | vsw-1234567890 | The ID of the vSwitch. |
| uid | Strin g | Body | No | user-1234567890 | The user ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| - deployConfigY amlStr | String | apiVersion: apps/v1 kind: Deployment | The deployment configuration as a YAML string. |

| - accessModeCo nfigYamlStr | String | mode: public enabled: true | The access mode configuration as a YAML string. |
|---|---|---|---|

#### GetInstanceDeployDeployConfig

Queries the deployment configuration of an instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | String | {} | The data |

#### GetInstanceDeployMsg

Queries the deployment message of an instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Struct | {} | The data |
| - accessModeLis t | Array | [] | The list of access modes. |
| -- intranetUrlStrL ist | String | [] | The list of internal network URLs. |
| -- networkUrlStrL ist | String | [] | The list of network URLs. |
| --name | String | my-resource | The name. |
| --type | String | 1 | The type. |
| -podInfoList | Array | [] | The list of pod information. |
| --ipList | Array | [] | The list of IP addresses. |
| ---ip | String | 192.168.1.100 | The IP address. |
| ---ipType | String | IPv4 | The IP address type. |
| --name | String | my-resource | The name. |
| --isReady | Boolean | true | Whether it is ready. |

| - deploymentNa me | String | app-deployment | The deployment name. |
|---|---|---|---|
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | The gateway instance ID. |
| - instanceName | String | instance-001 | The instance name. |
| - engineSpecific ation | String | MSE GTW 16 32 2 _ _ _ _ 00 c _ | The engine specifications. |
| -vpcId | String | vpc-bp1234567890 | The VPC ID. |
| -regionId | String | cn-hangzhou | The region ID. |
| -zoneId | String | cn-hangzhou-b | The zone ID. |
| -vSwitchId | String | vsw- bp1234567890 | The virtual switch ID. |
| -resConfig | Struct | {} | Response Configuration |
| --cpuRequest | String | 1000m | The requested CPU resources. |
| -- memoryReque st | String | 512Mi | The requested memory resources. |
| --cpuLimit | String | 2000m | The CPU limit. |
| --memoryLimit | String | 1Gi | The memory limit. |
| --replicas | Integer | 3 | The number of replicas. |
| --jvmArgs | String | -Xms512m - Xmx1024m | The JVM parameters. |
| -clusterConfig | Struct | {} | The cluster configuration. |

| --clusterName | String | my-cluster | The cluster name. |
|---|---|---|---|
| --namespace | String | prod-ns | The namespace. |
| --clusterCode | String | cluster-001 | The cluster code. |

#### GetCustomDeployConfig

Queries a custom deployment configuration.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Struct | {} | The data |
| - deploymentYa mlStr | String | apiVersion: apps/v1 kind: Deployment | The deployment YAML string. |
| - serviceYamlStr | String | apiVersion: v1 kind: Service | The service YAML string. |
| -jarStr | String | my-service.jar | The JAR file name. |

| -wgetStr | String | wget https://example.co m/file | The Wget command string. |
|---|---|---|---|

#### GetInstanceAccessModeConfig

Retrieves the access mode configuration of an instance.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The response message. |
| data | Map | {} | The data |

#### GetResource

Queries the resources of an instance.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -replicas | Integer | 3 | The number of replicas. |
| -jvmArgs | String | -Xms512m - Xmx1024m | The JVM parameters. |
| - instanceName | String | instance-001 | The instance name. |
| - engineSpecific ation | String | MSE GTW 16 32 2 _ _ _ _ 00 c _ | The engine specifications. |
| -vpcId | String | vpc-bp1234567890 | The ID of the VPC. |
| -regionId | String | cn-hangzhou | The region ID. |
| -zoneId | String | cn-hangzhou-b | The zone ID. |
| -backupZoneId | String | cn-hangzhou-h | The ID of the backup zone. |
| - backupVSwitc hId | String | vsw- bp1234567890 | The ID of the backup vSwitch. |
| -thirdZoneId | String | cn-hangzhou-c | The ID of the third zone. |

| - thirdVSwitchId | String | vsw-third-001 | The ID of the vSwitch in the third zone. |
|---|---|---|---|
| -zoneType | String | primary | The type of the zone. |
| -vSwitchId | String | vsw- bp1234567890 | The vSwitch ID. |
| -cpuRequest | Struct | 1000m | The requested CPU resources. |
| --amount | String | 100.00 | The amount. |
| --unit | String | requests/second | The unit. |
| - memoryReque st | Struct | 512Mi | Memory Request |
| --amount | String | 100.00 | The amount. |
| --unit | String | requests/second | The unit. |
| -cpuLimit | Struct | 2000m | The CPU limit. |
| --amount | String | 100.00 | The amount. |
| --unit | String | requests/second | The unit. |
| -memoryLimit | Struct | 1Gi | The memory limit. |
| --amount | String | 100.00 | The amount. |
| --unit | String | requests/second | The unit. |

#### ModifyResource

Modifies the resources of an instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| replicas | Integ er | Body | No | 3 | The number of replicas. |
| specificati onTemplat e | Integ er | Body | No | 1 | The specification template. |
| source | Strin g | Body | No | manual | The source. |
| instanceCl ass | Strin g | Body | No | ecs.g6.large | The instance type. |
| backupZon eId | Strin g | Body | No | cn-hangzhou-h | The ID of the backup zone. |
| backupVS witchId | Strin g | Body | No | vsw-bp1234567890 | The ID of the backup vSwitch. |
| thirdZoneI d | Strin g | Body | No | cn-hangzhou-c | The ID of the third zone. |
| thirdVSwit chId | Strin g | Body | No | vsw-third-001 | The ID of the vSwitch in the third zone. |
| zoneType | Strin g | Body | No | primary | The type of the zone. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

| data | String | {} | The data. |
|---|---|---|---|

### Group Management

#### ModifyGroup

This operation modifies a group.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| groupId | Strin g | Body | No | group-123456 | The group ID. |
| name | Strin g | Body | No | my-resource | The name. |
| basePath | Strin g | Body | No | /api/v1 | The base path. |
| description | Strin g | Body | No | This is a sample service. | The description. |
| domainIds | Repe atLis t | Body | No | [] | A list of domain name IDs. |

**Response parameters**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |

| msg | String | The operation was successful. | The message. |
|---|---|---|---|
| data | String | {} | The data. |

#### CreateGroup

Creates a group.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter Name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| name | Strin g | Body | No | my-resource | The name. |
| basePath | Strin g | Body | No | /api/v1 | The base path. |
| needDefau ltDomain | Bool ean | Body | No | true | Specifies whether a default domain name is required. |
| description | Strin g | Body | No | This is an example service | The description. |
| domainIds | Repe atLis t | Body | No | [] | The list of domain name IDs. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |

| msg | String | The operation was successful. | The message. |
|---|---|---|---|
| data | String | {} | The data. |

#### ListGroups

Retrieves a list of groups.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| current | Integ er | Body | No | 1 | The current page number. |
| size | Integ er | Body | No | 100 | The size. |
| groupId | Strin g | Body | No | group-123456 | The group ID. |
| name | Strin g | Body | No | my-resource | The name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |

| -records | Array | [] | The list of records. |
|---|---|---|---|
| --domains | Array | [] | The list of domain names. |
| ---domainId | String | domain-123456 | The domain ID. |
| ---domain | String | api.example.com | The domain name. |
| ---protocol | String | HTTP | The protocol. |
| ---createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --groupId | String | group-123456 | The group ID. |
| --gwInstanceId | String | i- c0a81bb16a1524a 17 | The ID of the gateway instance. |
| --name | String | my-resource | The group name. |
| --basePath | String | /api/v1 | The base path. |
| --description | String | This is a sample service. | The description. |
| -- defaultDomain | String | api.example.com | The default domain name. |
| --editable | Boolean | true | Indicates whether the group is editable. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

| -size | Integer | 100 | The size. |
|---|---|---|---|

#### GetAllGroups

Retrieves a list of all groups.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| serviceTyp e | Integ er | Body | No | REST | The type of the service. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array | {} | The data. |
| -domains | Array | [] | A list of domain names. |
| --domainId | String | domain-123456 | The ID of the domain name. |
| --domain | String | api.example.com | The domain name. |
| --protocol | String | HTTP | The protocol. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -groupId | String | group-123456 | The ID of the group. |

| -gwInstanceId | String | i- c0a81bb16a1524a 17 | The ID of the gateway instance. |
|---|---|---|---|
| -name | String | my-resource | The name |
| -basePath | String | /api/v1 | The base path. |
| -description | String | This is an example service. | Description. |
| - defaultDomain | String | api.example.com | The default domain name. |
| -editable | Boolean | true | Indicates whether the group is editable. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -updateTime | String | 2024-10-14 15:00:00 | The update time. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

#### GetGroup

Queries the details of a group.

**Request headers**

This operation uses common request headers and does not use special request headers. For more information about common request headers, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

| groupId | Strin g | Body | No | group-123456 | The group ID. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Struct | {} | The data |
| -domains | Array | [] | The list of domain names. |
| --domainId | String | domain-123456 | The domain ID. |
| --domain | String | api.example.com | The domain name. |
| --protocol | String | HTTP | The protocol. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -groupId | String | group-123456 | The group ID. |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | The gateway instance ID. |
| -name | String | my-resource | The name. |
| -basePath | String | /api/v1 | The base path. |
| -description | String | This is an example service. | The description. |
| - defaultDomain | String | api.example.com | The default domain name. |

| -editable | Boolean | true | Indicates whether the group is editable. |
|---|---|---|---|
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -updateTime | String | 2024-10-14 15:00:00 | The update time. |

#### DeleteGroup

Deletes a group.

**Request headers**

This operation has no special request headers. For more information about common request headers, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| groupId | Strin g | Body | No | group-123456 | The ID of the group. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | String | {} | The data. |

#### AddGroupDomain

Adds a domain name to a group.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | gw-cn-wwo36s5y001 | The gateway instance ID. |
| groupId | Strin g | Body | No | 16782 | The API group ID. |
| domainIds | Repe atLis t | Body | No | ["3412", "3413"] | The IDs of the domain names to attach. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The return code. A value of 200 indicates success. Other values indicate an error. |
| msg | String | success | The returned message. If the request is successful, 'success' is returned. If the request fails, an error message is returned. |
| data | String | true | The returned data. If the operation is successful, the string 'true' is returned. |

**Examples**

Request example `{`

```json
  "gwInstanceId": "gw-cn-wwo36s5y001",
  "groupId": "16782",
  "domainIds": [
    "3412",
    "3413"
```

`]` `}` Successful response example `JSON` format `{`

```json
  "code": 200,
  "msg": "success",
  "data": "true"
```

`}`

#### DeleteGroupDomain

Deletes a domain name from a group.

**Request headers**

This operation does not have special request headers. For more information about common request headers, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| groupId | Strin g | Body | No | group-123456 | The group ID. |
| domainId | Strin g | Body | No | domain-123456 | The domain ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | String | {} | The data |

### Ingress management

#### CreateRoute

Creates a route.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

`{`

```json
  "gwInstanceId": "string",
  "groupId": "string",
  "serviceId": "string",
  "routeName": "string",
  "routePath": [
    "string"
```

`],`

```json
  "path": {
    "matchType": "string",
    "matchValue": "string",
    "caseSensitive": true
```

`},`

```json
  "openStripPrefix": true,
  "serviceType": "string",
  "serviceIds": [
```

`{`

```json
      "serviceId": "string",
      "weight": 0
```

`}` `],`

```json
  "enableStatus": true,
  "stripPrefix": 0,
  "order": 0,
  "methods": [
    "string"
```

`],`

```json
  "header": [
```

`{`

```json
      "key": "string",
      "value": "string"
```

`}` `],`

```json
  "cookie": [
```

`{`

```json
      "key": "string",
      "value": "string"
```

`}` `],`

```json
  "queryParam": [
```

`{`

```json
      "key": "string",
      "value": "string"
```

`}` `],`

```json
  "domainIds": [
    "string"
```

`],`

```json
  "routeId": "string",
  "hsfMethodMappingConfig": {
    "hsfMethod": "string",
    "parameterMappingList": [
```

`{`

```json
        "name": "string",
        "schema": {
          "type": "string",
          "items": "string",
          "array": true,
          "primitive": true,
          "generic": true
```

`},`

```json
        "location": "string",
        "required": true,
        "order": 0
```

`}` `]` `}` `}`

| Parameter Name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| order | Integ er | Body | No | 100 | The sort number. |
| filters | Strin g | Body | No | path=/api/** | The filter. |
| routeId | Strin g | Body | No | route-123456 | The route ID. |
| routeNam e | Strin g | Body | No | user-service-route | The route name. |
| serviceId | Strin g | Body | No | service-123456 | The service ID. |
| serviceTyp e | Strin g | Body | No | REST | The service type. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

| methods | Repe atLis t | Body | No | [] | A list of request methods. |
|---|---|---|---|---|---|
| header | Repe atLis t | Body | No | [] | A list of request headers. |
| -key | Strin g | Body | No | api-key-001 | The key. |
| -value | Strin g | Body | No | example-value | The value. |
| cookie | Repe at list | Body | No | [] | A list of cookies. |
| -key | Strin g | Body | No | api-key-001 | The key. |
| -value | Strin g | Body | No | example-value | The value. |
| queryPara m | Repe atLis t | Body | No | [] | A list of query parameters. |
| -key | Strin g | Body | No | api-key-001 | The key. |
| -value | Strin g | Body | No | example-value | The value. |
| domainIds | Repe atLis t | Body | No | [] | A list of domain name IDs. |
| routePath | Repe atLis t | Body | No | /api/v1/users | The route path. |
| stripPrefix | Integ er | Body | No | 1 | The number of prefix levels to strip. |

| requestTi meout | Integ er | Body | No | 30000 | The request timeout period, in milliseconds. |
|---|---|---|---|---|---|
| openStripP refix | Bool ean | Body | No | true | Specifies whether to strip the prefix. |
| enableForc eNonceCh eck | Bool ean | Body | No | false | Specifies whether to enforce a random number check. |
| path | JSON | Body | No | /api/v1/resource | The path. |
| serviceIds | Repe atLis t | Body | No | [] | A list of service IDs. |
| -serviceId | Strin g | Body | No | service-123456 | The service ID. |
| -weight | Integ er | Body | No | 100 | The weight. |
| groupId | Strin g | Body | No | group-123456 | The group ID. |
| enableStat us | Bool ean | Body | No | true | The enabled status. |
| hsfMethod MappingCo nfig | JSON | Body | No | {"method":"invoke","para ms":[]} | The HSF method mapping configuration. |

**Response parameters**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### BatchDeleteRoute

Deletes multiple routes at once.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the document on common request parameters.

| Parameter Name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | Gateway instance ID. |
| routeIds | Repe atLis t | Body | No | [] | List of route IDs. |

**Response parameters**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation succeeded | The message. |
| data | Struct | {} | The data. |
| -successIds | String | [] | List of successful IDs. |
| -failedIds | String | [] | List of failed IDs. |

#### ListRoutes

Queries a list of routes.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /route/listRoutes HTTP/1.1
```

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| size | Integ er | Body | No | 10 | The number of rows per page in a paged query. |
| current | Integ er | Body | No | 1 | Set the page on which the returned results are displayed. The default value is 1, indicating that the display starts on page 1. |
| routeNam e | Strin g | Body | No | demo-route | The name of the route. |
| serviceNa me | Strin g | Body | No | demo-service | The name of the service. |
| exactServi ceId | Strin g | Body | No | 1001 | The specified exact service ID is 1001, which uniquely identifies a specific service instance. |
| enableStat us | Bool ean | Body | No | true | The enabling status. |
| gwInstanc eId | Strin g | Body | No | i-demo | The ID of the gateway instance. |
| routeId | Strin g | Body | No | xxx-xxx-xxx-xxx | The ID of the route. |
| groupNam e | Strin g | Body | No | test | The name of the group. |
| domainNa me | Strin g | Body | No | example.com | The domain name. |

**Response parameters**

| > Document Versi | on: 20260828 |   | 23 |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The Request is not authorization. | The error message. |
| data | Struct | {} | The returned data. |
| -records | Array | [] | The list of returned data records. |
| --routePath | String | /reviews/v1 | The path of the route. |
| --domains | String | ["example.com", "www.example.co m"] | The list of domain names. |
| --routeId | String | RouteId 1 _ | The ID of the route. |
| --routeName | String | http-route | The name of the route. |
| --enableStatus | Boolean | true | Whether to enable it.disable: disabled enable: enable. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --serviceId | String | service-123456 | The ID of the service. |
| --serviceName | String | user-service | The name of the service. |
| --groupId | String | group-123456 | The ID of the group. |
| --groupName | String | Default group | The name of the group. |
| --path | Struct | /api/v1/resource | The path. |
| ---matchType | String | prefix | The match type. |

| ---matchValue | String | /v1/users | The match value. |
|---|---|---|---|
| --- caseSensitive | Boolean | false | Indicates whether the match is case- sensitive. |
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

**Examples**

Request example

```
POST /route/listRoutes HTTP/1.1
```

`{` `}` Response example `JSON` format `{`

```json
 "msg":"",
 "code":"",
 "data":{
  "total":"",
  "current":"",
  "size":"",
  "records":[
```

`{`

```json
    "routePath":"",
    "groupName":"",
    "routeId":"",
    "createTime":"",
    "groupId":"",
    "domains":"",
    "serviceId":"",
    "serviceName":"",
    "enableStatus":"",
    "path":[
```

`{`

```json
      "matchType":"",
      "caseSensitive":"",
      "matchValue":""
```

`}` `],`

```json
    "routeName":""
```

`}` `]` `}` `}`

#### ListRoutesByAppId

Queries a list of routes.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| size | Integ er | Body | No | 100 | The size. |
| current | Integ er | Body | No | 1 | The current page number. |

| total | Integ er | Body | No | 1000 | The total number of entries. |
|---|---|---|---|---|---|
| routeNam e | Strin g | Body | No | user-service-route | The route name. |
| routeId | Strin g | Body | No | route-123456 | The route ID. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -records | Array | [] | The list of records. |
| --routeId | String | route-123456 | The route ID. |
| --routeName | String | user-service-route | The route name. |
| --routePath | String | /api/v1/users | The route path. |
| --serviceId | String | service-123456 | The service ID. |
| --serviceName | String | user-service | The service name. |
| -- serviceProtoco l | String | HTTP | The service protocol. |

| --authId | String | auth 123456 _ | The authentication ID. |
|---|---|---|---|
| --authStatus | Integer | 1 | The authentication status. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

#### ListRoutesByGwInstanceId

Queries a list of routes.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| serviceTyp e | Integ er | Body | No | REST | The service type. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array | {} | The data. |
| -routeId | String | route-123456 | The route ID. |

| -routeName | String | user-service-route | The route name. |
|---|---|---|---|
| -routePath | String | /api/v1/users | The route path. |
| -serviceId | String | service-123456 | The service ID. |
| -serviceName | String | user-service | The service name. |
| - serviceProtoco l | String | HTTP | The service protocol. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

#### GetAllRoutePath

Retrieves all routing paths.

**Request headers**

No special request headers are required for this operation. For more information about common request headers, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| body | Strin g | Body | No | {"key":"value"} | The content of the request body. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The response code. |
| Msg | String | The operation was successful. | The message |

| Data | Struct | {} | The data |
|---|---|---|---|
| -RoutePaths | String | [] | The list of routing paths. |

#### GetRoute

Queries the details of a specified route.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | Struct | {} | The data. |
| -routePath | String | /api/v1/users | The path of the route. |
| -methods | String | [] | The list of request methods. |
| -header | Array | [] | The list of request headers. |
| --key | String | api-key-001 | The key. |

| --value | String | example-value | The value. |
|---|---|---|---|
| -cookie | Array | [] | The list of cookies. |
| --key | String | api-key-001 | The key. |
| --value | String | example-value | The value. |
| -queryParam | Array | [] | The list of query parameters. |
| --key | String | api-key-001 | The key. |
| --value | String | example-value | The value. |
| -plugins | Array | [] | The list of plugins. |
| --key | String | api-key-001 | The key. |
| --value | String | example-value | The value. |
| - sigSchemeDT OList | Array | [] | The list of signature schemes. |
| -- sigSchemeStat us | Integer | 1 | The status of the signature scheme. |
| -- sigSchemeNa me | String | HMAC-SHA256 | The name of the signature scheme. |
| --sigSchemeId | String | sig-scheme-001 | The ID of the signature scheme. |
| --sigAlg | String | SHA256withRSA | The signature algorithm. |
| --secretKey | String | sk 1234567890abc _ def | The secret key. |
| -domainVO | Array | [] | The list of domain name view objects. |

| --domainId | String | domain-123456 | The domain name ID. |
|---|---|---|---|
| --domain | String | api.example.com | The domain name. |
| --protocol | String | HTTP | The protocol. |
| --createTime | String | 2024-10-14 08:00:00 | The time when it was created. |
| - groupDomainV O | Array | [] | The list of group domain name view objects. |
| --domainId | String | domain-123456 | The domain name ID. |
| --domain | String | api.example.com | The domain name. |
| --protocol | String | HTTP | The protocol. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| - strategyConfig s | Array | [] | The list of policy configurations. |
| --scopes | String | [] | The list of authorization scopes. |
| -- strategyConfig Id | String | strategy-config- 001 | The ID of the policy configuration. |
| -- strategyConfig Name | String | Default Policy | The name of the policy configuration. |
| -- strategyName | String | Throttling Policy | The policy name. |
| --status | Boolean | 1 | The status. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |

| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
|---|---|---|---|
| --scope | Struct | openid profile | The authorization scope. |
| ---scopes | String | [] | The list of authorization scopes. |
| ---routeInfos | Array | [] | The list of route information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---serviceInfos | Array | [] | The list of service information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---appInfos | Array | [] | The list of application information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---domainInfos | Array | [] | The list of domain name information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | ID |
| --- mcpServerInfo s | Array | [] | The list of MCP server information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |

| -serviceIds | Array | [] | The list of service IDs. |
|---|---|---|---|
| -routeId | String | route-123456 | The ID of the route. |
| -routeName | String | user-service-route | The name of the route. |
| -enableStatus | Boolean | true | The enabled status. |
| - openStripPrefi x | Boolean | true | Indicates whether to strip the prefix. |
| -stripPrefix | Integer | 1 | The number of prefix levels to strip. |
| -order | Integer | 100 | The sorting number. |
| - routeCreateTi me | String | 2024-10-14 09:00:00 | The time when the route was created. |
| -groupId | String | group-123456 | The group ID. |
| -groupName | String | Default Group | The group name. |
| -basePath | String | /api/v1 | The base path. |
| -serviceName | String | user-service | The service name. |
| -serviceId | String | service-123456 | The service ID. |
| - serviceDescrip tion | String | User Management Service | The service description. |
| - upstreamType | Integer | 1 | The upstream type. |
| - upstreamType Name | String | HTTP Service | The name of the upstream type. |

| - loadBalanceTy pe | Integer | 1 | The load balancing type. |
|---|---|---|---|
| - loadBalanceTy peName | String | Polling | The name of the load balancing type. |
| - serviceCreateT ime | String | 2024-10-14 08:00:00 | The time when the service was created. |
| - isOpenFreeCer t | Boolean | false | Indicates whether to enable the free certificate. |
| -isOpenTraffic | Boolean | true | Indicates whether to enable traffic shaping. |
| -isOpenMock | Boolean | false | Indicates whether to enable mocking. |
| - isOpenTimeOu t | Boolean | true | Indicates whether to enable timeout. |
| - requestTimeo ut | Integer | 30000 | The request timeout period, in milliseconds. |
| -isOpenPlugin | Boolean | true | Indicates whether to enable plugins. |
| -isOpenFuse | Boolean | true | Indicates whether to enable circuit breaking. |
| -isOpenSig | Boolean | true | Indicates whether to enable signing. |
| -isRewrite | Boolean | true | Indicates whether to enable rewriting. |
| -isOpenCross | Boolean | true | Indicates whether to enable cross-domain requests. |
| - isOpenRespon seCache | Boolean | true | Indicates whether to enable response caching. |

| -serviceType | String | REST | The service type. |
|---|---|---|---|
| -path | Struct | /api/v1/resource | The path. |
| --matchType | String | prefix | The match type. |
| --matchValue | String | /v1/users | The match value. |
| -- caseSensitive | Boolean | false | Indicates whether the matching is case- sensitive. |
| -trafficControl | Struct | {} | The traffic shaping configuration. |
| --id | Integer | 123456 | The ID. |
| --userId | String | uid-123456 | The user ID. |
| --namespace | String | prod-ns | The namespace. |
| --routeId | String | route-123456 | The ID of the route. |
| -- resourceMode | Integer | 1 | The resource mode. |
| -- thresholdType | Integer | 1 | The threshold type. |
| --count | Float | 10.5 | The number. |
| -- controlBehavio r | Integer | 1 | The throttling behavior. |
| --intervalSec | Integer | 30 | The time interval, in seconds. |
| --burst | Integer | 100 | The maximum burst traffic. |
| -- maxQueueing TimeoutMs | Integer | 5000 | The maximum queuing timeout period, in milliseconds. |

| --isRequestAttr | Boolean | false | Indicates whether it is a request property. |
|---|---|---|---|
| --enable | Boolean | true | Indicates whether it is enabled. |
| --gwInstanceId | String | i- c0a81bb16a1524a 17 | The ID of the gateway instance. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| --attrStr | Struct | {} | The property structure. |
| ---paramAttr | Integer | 1 | The parameter property. |
| --- paramAttrDeta il | String | query | The details of the parameter property. |
| --- isOpenMatch | Integer | 1 | Indicates whether to enable matching. |
| ---matchMode | Integer | 1 | The match mode. |
| ---matchString | String | /api/* | The match string. |
| -- thresholdByQp s | Struct | {} | The configuration for the QPS threshold. |
| --- qpsThreshold | Integer | 1000 | The QPS threshold. |
| ---timeInterval | Integer | 300 | The time interval, in seconds. |
| ---timeUnit | Integer | 1 | The time unit. |
| --- flowControlMe thod | Integer | 1 | The throttling method. |

| --- flowControlInf o | Integer | 1 | The throttling information. |
|---|---|---|---|
| -- thresholdByTh readVo | Struct | {} | The configuration for the thread count threshold. |
| ---threadNum | Integer | 10 | The number of threads. |
| - routeMockCon figVo | Struct | {} | The route mock configuration. |
| -- responseHead er | String | [] | The list of response headers. |
| --isOpen | Integer | true | Indicates whether it is enabled. |
| -- responseBody | String | {"code":200,"data" :{}} | The response body. |
| -- responseCode | Integer | 200 | The response code. |
| - routeFusesCon figVo | Struct | {} | The route circuit breaking configuration. |
| -- routeFusesCon dition | Array | [] | The list of route circuit breaking conditions. |
| ---id | Integer | 123456 | The ID. |
| ---type | Integer | 1 | The type. |
| ---operator | String | admin | The operator. |
| ---judgValue | String | 100 | The judgment value. |
| ---errorCount | Float | 5.0 | The number of errors. |

| ---statInterval | Integer | 60 | The statistics interval, in seconds. |
|---|---|---|---|
| ---timeWindow | Integer | 60 | The time window, in seconds. |
| --- minRequestA mount | Integer | 10 | The minimum number of requests. |
| --- halfOpenBase AmountPerSte p | Integer | 5 | The base number of requests per step in the half-open state. |
| --- halfOpenReco veryStepNum | Integer | 3 | The number of recovery steps in the half- open state. |
| --resourceId | String | res-abc123 | The resource ID. |
| -- combinedCond ition | String | A AND B | The combined conditional expression. |
| -- degradeStrate gy | Integer | 1 | The degradation policy. |
| --fuseMock | Struct | {} | The circuit breaking mock configuration. |
| --- responseHead er | String | [] | The list of response headers. |
| ---isOpen | Integer | true | Indicates whether it is enabled. |
| --- responseBody | String | {"code":200,"data" :{}} | The response body. |
| --- responseCode | Integer | 200 | The response code. |
| -routeAuthVO | Struct | {} | The route authentication configuration. |

| -- requestHeader | String | Content-Type | The request header. |
|---|---|---|---|
| --authType | Integer | jwt | The authentication type. |
| -- appCodeAuthT ype | String | oauth2 | The application code authentication type. |
| --customAuth | Struct | {} | The custom authentication configuration. |
| --- authRequestH eader | String | [] | The list of authentication request headers. |
| --- authResponse Header | String | [] | The list of authentication response headers. |
| --- authServerHos t | String | auth.example.com | The authentication server host. |
| --- authServerUri | String | /oauth/token | The authentication server URI. |
| ---authTimeout | Integer | 30000 | The authentication timeout period, in milliseconds. |
| ---keepAlive | Integer | 60 | The keep-alive duration, in seconds. |
| --- tokenExpiratio n | Integer | 7200 | The token expiration time, in seconds. |
| --- authAssertTyp e | String | header | The authentication assertion type. |
| --- authAssertVal ue | String | Bearer token | The authentication assertion value. |
| --- openLoosePatt ern | Boolean | false | Indicates whether to enable loose mode. |

| --- cachedClient | Map | {} | The cached client information. |
|---|---|---|---|
| --apiKey | Struct | {} | The API key configuration. |
| --- enableInHead er | Boolean | true | Indicates whether to enable the API key in the request header. |
| --- enableInQuery | Boolean | true | Indicates whether to enable the API key in query parameters. |
| ---apiKeyName | String | my-api-key | The API key name. |
| --- enableRmPara m | Boolean | false | Indicates whether to remove the parameter. |
| --- enableOptions FreeAuth | Boolean | true | Indicates whether to exempt OPTIONS requests from authentication. |
| -crossConfig | Struct | {} | The cross-domain configuration. |
| -- allowedMetho ds | String | [] | The list of allowed request methods. |
| --isOpenCross | Boolean | true | Indicates whether to enable cross-domain requests. |
| --crossType | String | CORS | The cross-domain type. |
| -- allowedOrigins | String | * | The allowed origin domain names. |
| -- exposedHeade rs | String | X-Custom- Header,X-Request- Id | The exposed response headers. |
| -- allowedHeader s | String | Content- Type,Authorization | The allowed request headers. |

| -- allowedCreden tials | Boolean | true | Indicates whether to allow credentials. |
|---|---|---|---|
| --maxAge | Integer | 3600 | The maximum cache duration, in seconds. |
| --callbackFunc | String | handleCallback | The name of the callback function. |
| - responseCach eConfig | Struct | {} | The response cache configuration. |
| -- routeInterface List | Array | [] | The list of route interfaces. |
| ---method | String | GET | The request method. |
| ---headers | String | Content-Type: application/json | The request headers. |
| ---path | String | /api/v1/resource | The path. |
| --- queryParams | String | page=1&size=10 | The query parameter string. |
| --maxAge | Integer | 3600 | The maximum cache duration, in seconds. |
| -- isOpenCacheC ontrol | Boolean | true | Indicates whether to enable cache control. |
| -- allowedStatus Code | String | 200,201,204 | The allowed status codes. |
| -- isOpenRespon seCache | Boolean | true | Indicates whether to enable response caching. |
| - routeIpBlockC onfigVO | Struct | {} | The route IP address blocking configuration. |

| --ipBlockRules | Array | [] | The list of IP address blocking rules. |
|---|---|---|---|
| ---ip | String | 192.168.1.100 | The IP address. |
| ---policy | String | allow | The policy. |
| -- isOpenIpBlock | Boolean | false | Indicates whether to enable IP address blocking. |
| - routeACLConfi g | Struct | {} | The route access control configuration. |
| --aclRules | Array | [] | The list of access control rules. |
| ---group | String | default-group | The group. |
| ---policy | String | allow | The policy. |
| --isEnableACL | Boolean | true | Indicates whether to enable access control. |
| - routeTracingC onfig | Struct | {} | The route tracing configuration. |
| --traceHeader | String | X-Trace-Id | The tracing request header. |
| -- isEnableDown stream | Boolean | true | Indicates whether to enable downstream tracing. |
| -- isEnableTracin g | Boolean | true | Indicates whether to enable tracing. |

#### GetProtocolByRoute

Queries the protocol of a route.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |
| type | Integ er | Body | No | 1 | The type. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | String | {} | The data |

#### ModifyRoute

Modifies a route.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| order | Integ er | Body | No | 100 | The priority of the route. A smaller value indicates a higher priority. This parameter is used in scenarios where multiple routes may match the same request. |
| filters | Strin g | Body | No | [{"name":"jwtAuthFilter" }, {"name":"rateLimitFilter "}] | The filter chain associated with the route. This is typically a JSON string that defines various plugins in the request processing flow, such as authentication and rate limiting. |
| routeId | Strin g | Body | No | rt-a1b2c3d4e5f6 | The unique ID of the route to modify. |
| routeNam e | Strin g | Body | No | User Service V2 Ingress | A human-readable name for the route. This makes the route easy to identify and manage. |
| serviceId | Strin g | Body | No | service-123456 | The service ID. |
| serviceTy pe | Strin g | Body | No | HTTP | The type of the backend service, such as HTTP or GRPC. |
| gwInstanc eId | Strin g | Body | No | gw-prod-cluster-01 | The ID of the gateway instance to which the route belongs. |
| methods | Repe atList | Body | No | ["GET", "POST"] | A list of HTTP methods that the route matches, such as GET and POST. |
| header | Repe atList | Body | No | [{"key":"X-Version", "value":"v2"}] | A list of request header conditions for the route to match. This is used to implement header- based routing. |
| -key | Strin g | Body | No | api-key-001 | The key. |

|   | Developer Gui | de·API G | ateway |   |   | API Gatewa | y |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| -value | Strin g | Body | No | example-value | The value. |
| cookie | Repe atList | Body | No | [{"key":"user-group", "value":"canary"}] | A list of cookie conditions for the route to match. |
| -key | Strin g | Body | No | api-key-001 | The key. |
| -value | Strin g | Body | No | example-value | The value. |
| queryPara m | Repe atList | Body | No | [{"key":"env", "value":"test"}] | A list of URL query parameter conditions for the route to match. |
| -key | Strin g | Body | No | api-key-001 | The key. |
| -value | Strin g | Body | No | example-value | The value. |
| domainIds | Repe atList | Body | No | ["dm-api-example-com"] | A list of domain name IDs for the route to match. The Host header of the request must match one of these IDs. |
| routePath | Repe atList | Body | No | ["/api/v2/users/*"] | A list of URL path patterns for the route to match. The asterisk (*) wildcard character is supported. |
| stripPrefix | Integ er | Body | No | 2 | If openStripPrefix is set to true, this parameter specifies the number of path levels to strip before forwarding the request to the backend service. For example, if the path is /api/v2/users and stripPrefix is 2, the backend service receives /users. |
| requestTi meout | Integ er | Body | No | 5000 | The timeout period for the gateway to request the backend service. Unit: milliseconds. |

| A | PI Gateway |   |   |   | De | veloper Guide·API Gatewa | y |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| openStrip Prefix | Boole an | Body | No | true | Specifies whether to enable the path prefix stripping feature. |
| enableFor ceNonceC heck | Boole an | Body | No | false | Specifies whether to enforce Nonce verification to prevent signature replay attacks. |
| path | Json | Body | No | /api/v1/resource | The path. |
| serviceIds | Repe atList | Body | No | [{"serviceId":"svc-user- v2-stable", "weight":80}, {"serviceId":"svc-user- v2-canary", "weight":20}] | (Multi-service/Phased release mode) A list of target services and their weights for routing. The sum of the weights for all services must be 100. |
| -serviceId | Strin g | Body | No | service-123456 | The service ID. |
| -weight | Integ er | Body | No | 100 | The weight. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The business return code. A value of 200 indicates that the operation is successful. Other values indicate that the operation failed. |
| msg | String | success | The returned message. If the operation is successful, success is typically returned. |
| data | String | rt-a1b2c3d4e5f6 | The returned data. If the operation is successful, the ID of the modified route is typically returned. |

#### DeleteRoute

Deletes a route.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### ChangeRouteStatus

Changes the status of a route.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |

| enableStat us | Bool ean | Body | No | true | The enabled status of the route. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Map | {} | The data. |

### Source Management

#### ListSources

Queries a list of sources.

**Request headers**

This operation uses common request headers. No special request headers are used. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| size | Integ er | Body | No | 100 | The size. |
| current | Integ er | Body | No | 1 | The current page number. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| sourceId | Strin g | Body | No | src-123456 | The source ID. |
| sourceNa me | Strin g | Body | No | Internal System | The source name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |
| data | Struct | {} | The data. |
| -records | Array | [] | The list of records. |
| --sourceId | String | src-123456 | The source ID. |
| --sourceName | String | Internal System | The source name. |
| --sourceType | Integer | 1 | The source type. |
| -- sourceTypeNa me | String | Kubernetes | The name of the source type. |
| --description | String | This is an example service. | The description. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

#### ListAllSources

Queries a list of all sources.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

| Name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| serviceTyp e | Integ er | Body | No | REST | The service type. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| data | Array | {} | The data. |
| -sourceId | String | src-123456 | The ID of the source. |
| -sourceName | String | Internal system | The name of the source. |
| -sourceType | Integer | 1 | The type of the source. |
| - sourceTypeNa me | String | Kubernetes | The name of the source type. |
| -sourceStruct | Map | {} | The structure of the source. |
| code | Integer | 200 | The response code. |
| msg | String | The operation is successful. | The message. |

#### GetSource

Queries a source.

**Request headers**

This operation uses common request headers and does not have special request headers. For more information, see the document on common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| sourceId | Strin g | Body | No | src-123456 | The ID of the source. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -sourceId | String | src-123456 | The ID of the source. |
| -sourceName | String | Internal System | The name of the source. |
| -sourceType | Integer | 1 | The type of the source. |
| - sourceTypeNa me | String | Kubernetes | The name of the source type. |
| -sourceStruct | Map | {} | The structure of the source. |
| -description | String | This is a sample service. | The description. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |

| -updateTime | String | 2024-10-14 15:00:00 | The update time. |
|---|---|---|---|

#### CreateSource

Creates a source.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| sourceId | Strin g | Body | No | src-123456 | The ID of the source. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| sourceNa me | Strin g | Body | No | Internal System | The name of the source. |
| host | Strin g | Body | No | api.example.com | The host address. |
| port | Integ er | Body | No | 8080 | The port number. |
| username | Strin g | Body | No | zhangsan | The username. |
| password | Strin g | Body | No | ******** | The password. |
| description | Strin g | Body | No | This is an example service. | The description. |
| sourceTyp e | Integ er | Body | No | 1 | The type of the source. |
| sourceStru ct | Json | Body | No | {} | The structure of the source. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### ModifySource

Modifies a source.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| sourceId | Strin g | Body | No | src-123456 | The source ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| sourceNa me | Strin g | Body | No | Internal System | The source name. |
| sourceStru ct | Json | Body | No | {} | The source structure. |
| description | Strin g | Body | No | This is a sample service. | The description. |
| sourceTyp e | Integ er | Body | No | 1 | The source type. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### DeleteSource

Deletes a source.

**Request headers**

This operation has no special request headers. For more information about common request headers, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| sourceId | Strin g | Body | No | src-123456 | The ID of the source. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### BatchDeleteSource

Deletes sources in batches.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter Name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| sourceIds | Repe atLis t | Body | No | [] | A list of resource IDs. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Struct | {} | The data. |
| -successIds | String | [] | The successful IDs. |
| -failedIds | String | [] | A list of IDs of the sources that failed to be deleted. |

### Service Management

#### ListServices

Queries a list of services.

**Request headers**

This operation uses common request headers and does not require any special request headers. For more information, see the Common Parameters document.

| 69 |   |   |   | > D | ocument Version: 2026082 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| size | Integ er | Body | No | 100 | The size. |
| current | Integ er | Body | No | 1 | The current page number. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| serviceNa me | Strin g | Body | No | user-service | The service name. |
| serviceId | Strin g | Body | No | service-123456 | The service ID. |
| sourceNa me | Strin g | Body | No | Internal System | The source name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The response message. |
| data | Struct | {} | The data. |
| -records | Array | [] | The list of records. |
| --nodes | Array | [] | The list of nodes. |
| ---ip | String | 192.168.1.100 | The IP address. |
| ---port | Integer | 8080 | The port number. |
| ---weight | Integer | 100 | The weight. |

| Developer Guide·A | PI Gateway |   | API Gatewa |
|---|---|---|---|

| ---enable | Boolean | true | Indicates whether the node is enabled. |
|---|---|---|---|
| --serviceId | String | service-123456 | The service ID. |
| --name | String | my-resource | The name. |
| -- upstreamType | Integer | 1 | The upstream type. |
| --serviceType | Integer | REST | The service type. |
| -- upstreamType Name | String | HTTP Service | The name of the upstream type. |
| -- serviceProtoco l | String | HTTP | The service protocol. |
| --sourceId | String | src-123456 | The source ID. |
| --sourceName | String | Internal System | The source name. |
| --sourceType | Integer | 1 | The source type. |
| -- sourceTypeNa me | String | Kubernetes | The name of the source type. |
| --createTime | String | 2024-10-14 08:00:00 | The time when the service was created. |
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The number of the returned page. |

#### ListAllServices

Queries the list of all services.

**Request header**

This operation uses common request headers and does not require special request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| serviceTyp e | Integ er | Body | No | REST | The type of the service. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| data | Array | {} | The data. |
| -serviceId | String | service-123456 | The ID of the service. |
| -serviceName | String | user-service | The name of the service. |
| -protocol | String | HTTP | The protocol. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

#### GetService

Retrieves the details of a service.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a1700 | The ID of the gateway instance. |
| serviceId | Strin g | Body | No | bailian | The service ID. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -zones | String | [] | The list of zones. |
| -routeList | Array | [] | The list of routes. |
| --routePath | String | /api/v1/users | The route path. |
| --routeId | String | route-123456 | The route ID. |
| --routeName | String | user-service-route | The route name. |
| - strategyConfig s | Array | [] | The list of policy configurations. |
| --scopes | String | [] | The list of authorization scopes. |
| -- strategyConfig Id | String | strategy-config- 001 | The policy configuration ID. |

| -- strategyConfig Name | String | Default Policy | The policy configuration name. |
|---|---|---|---|
| -- strategyName | String | Throttling Policy | The policy name. |
| --status | Boolean | 1 | The status. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| --scope | Struct | openid profile | The authorization scope. |
| ---scopes | String | [] | The list of authorization scopes. |
| ---routeInfos | Array | [] | The list of route information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---serviceInfos | Array | [] | The list of service information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---appInfos | Array | [] | The list of application information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---domainInfos | Array | [] | The list of domain name information. |
| ----name | String | my-resource | The name. |

| ----id | String | 123456 | The ID. |
|---|---|---|---|
| --- mcpServerInfo s | Array | [] | The list of MCP server information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| -serviceId | String | service-123456 | The service ID. |
| -name | String | my-resource | The name. |
| -serviceName | String | user-service | The service name. |
| -description | String | This is a sample service. | The description. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -protocol | String | HTTP | The protocol. |
| -serviceType | Integer | REST | The service type. |
| - upstreamType | Integer | 1 | The upstream type. |
| - upstreamType Name | String | HTTP service | The name of the upstream type. |
| - loadBalanceTy pe | Integer | 1 | The load balancing type. |
| - loadBalanceTy peName | String | Polling | The name of the load balancing type. |
| -sourceType | Integer | 1 | The source type. |

| - serviceSource Type | Integer | 1 | The service source type. |
|---|---|---|---|
| -serviceStruct | Map | {} | The service structure. |
| - isOpenHealthC heck | Boolean | true | Indicates whether health checks are enabled. |
| - healthCheckSt ruct | Struct | {} | The health check configuration. |
| --type | Integer | 1 | The type. |
| --healthPath | String | /health | The health check path. |
| --httpStatuses | String | 200,201,204 | The HTTP status codes. |
| --timeout | Integer | 30000 | The timeout period. Unit: milliseconds. |
| -- healthInterval | Integer | 30 | The health check interval. Unit: seconds. |
| -- unHealthInterv al | Integer | 10 | The unhealthy check interval. Unit: seconds. |
| -- httpSuccesses | Integer | 3 | The number of consecutive successful HTTP checks. |
| --httpFailures | Integer | 5 | The number of consecutive failed HTTP checks. |

#### CreateService

Creates a service.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| description | Strin g | Body | No | This is an example service. | The description of the service. |
| serviceTyp e | Integ er | Body | No | REST | The type of the service. |
| name | Strin g | Body | No | my-resource | The name. |
| upstreamT ype | Integ er | Body | No | 1 | The type of the upstream service. |
| serviceSou rceType | Integ er | Body | No | 1 | The source type of the service. |
| serviceNa me | Strin g | Body | No | user-service | The service name. |
| loadBalanc eType | Integ er | Body | No | 1 | The type of load balancing. |
| serviceStr uct | Json | Body | No | {} | The structure of the service. |
| isOpenHea lthCheck | Bool ean | Body | No | true | Specifies whether to enable health checks. |
| healthChe ckStruct | Json | Body | No | {} | The health check configuration. |
| protocol | Strin g | Body | No | HTTP | The protocol. |
| serviceId | Strin g | Body | No | service-123456 | The ID of the service. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### ModifyService

This operation modifies a service.

**Request headers**

This operation requires only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| serviceId | Strin g | Body | No | service-123456 | The service ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| name | Strin g | Body | No | my-resource | The name. |
| serviceNa me | Strin g | Body | No | user-service | The service name. |
| description | Strin g | Body | No | This is a sample service. | The description. |
| upstreamT ype | Integ er | Body | No | 1 | The upstream type. |
| serviceSou rceType | Integ er | Body | No | 1 | The service source type. |

| serviceTyp e | Integ er | Body | No | REST | The service type. |
|---|---|---|---|---|---|
| loadBalanc eType | Integ er | Body | No | 1 | The load balancing type. |
| serviceStr uct | Json | Body | No | {} | The service structure. |
| isOpenHea lthCheck | Bool ean | Body | No | true | Specifies whether to enable health checks. |
| healthChe ckStruct | Json | Body | No | {} | The health check configuration. |
| protocol | Strin g | Body | No | HTTP | The protocol. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### ModifyNode

Modifies a service node.

**Request headers**

This operation uses only common request headers. For more information, see the document about common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
|---|---|---|---|---|---|
| serviceId | Strin g | Body | No | service-123456 | The service ID. |
| serviceSou rceType | Integ er | Body | No | 1 | The source type of the service. |
| serviceStr uct | Json | Body | No | {} | The service structure. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### DeleteService

Deletes a service.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request syntax**

```
POST /microservice/deleteService HTTP/1.1
```

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | test-service | The instance ID. |

| serviceId | Strin g | Body | No | service-123456 | The service ID. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data |

**Examples**

Sample request

```
POST /microservice/deleteService HTTP/1.1
```

`{` `}` Sample successful response `JSON` format `{`

```json
 "msg":"",
 "code":"",
 "data":""
```

`}`

#### BatchDeleteService

Deletes multiple services at a time.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|

| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
|---|---|---|---|---|---|
| serviceIds | Repe atLis t | Body | No | [] | A list of service IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |
| data | Struct | {} | The Data. |
| -successIds | String | [] | List of success IDs. |
| -failedIds | String | [] | List of failed IDs. |

#### ImportServices

This operation imports services.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter Name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| description | Strin g | Body | No | This is a sample service | The description. |
| loadBalanc eType | Integ er | Body | No | 1 | The load balancing type. |

| serviceTyp e | Integ er | Body | No | REST | The service type. |
|---|---|---|---|---|---|
| sourceId | Strin g | Body | No | src-123456 | The source ID. |
| sourceNa mespaceId | Strin g | Body | No | ns-source-001 | The ID of the source namespace. |
| groupNam e | Strin g | Body | No | Default Group | The group name. |
| port | Integ er | Body | No | 8080 | The port number. |
| serviceList | Repe atLis t | Body | No | [] | The list of services. |
| protocol | Strin g | Body | No | HTTP | The protocol. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| data | String | {} | The data. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The messages |

### Consumer management

#### ListApps

Queries a list of consumers.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| size | Integ er | Body | No | 100 | The size. |
| current | Integ er | Body | No | 1 | The current page number. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| appName | Strin g | Body | No | Sample Application | The application name. |
| appTags | Strin g | Body | No | [] | The list of application tags. |
| authType | Strin g | Body | No | jwt | The authentication type. |
| userId | Strin g | Body | No | uid-123456 | The user ID. |
| userName | Strin g | Body | No | Zhang San | The username. |
| email | Strin g | Body | No | admin@example.com | The email address. |
| status | Integ er | Body | No | 1 | The status. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| appType | Integ er | Body | No | 1 | The application type. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | Integer | 200 | The response code. |
|---|---|---|---|
| msg | String | Operation successful | The message. |
| data | Struct | {} | The data. |
| -records | Array | [] | The list of records. |
| --ipWhiteList | String | [] | The IP address whitelist. |
| --groups | String | [] | The list of groups. |
| --appTags | Array | [] | The list of application tags. |
| --appId | String | 12345678 | The application ID. |
| --appName | String | Sample Application | The application name. |
| --appAddress | String | https://example.co m | The application address. |
| --useAuth | Boolean | true | Indicates whether authentication is used. |
| --authType | Integer | jwt | The authentication type. |
| -- authTypeNam e | String | JWT | The name of the authentication type. |
| --useWhiteList | Boolean | true | Indicates whether a whitelist is used. |
| --description | String | This is a sample service. | The description. |
| -- chargePerson Name | String | Zhang San | The name of the owner. |
| --createBy | Integer | 1001 | The ID of the user who created the application. |

| --createTime | String | 2024-10-14 08:00:00 | The time when the application was created. |
|---|---|---|---|
| --updateBy | Integer | 1001 | The modifier ID. |
| --updateTime | String | 2024-10-14 15:00:00 | The time when the application was last updated. |
| --userId | String | uid-123456 | The user ID. |
| --userName | String | Zhang San | The username. |
| --delFlag | String | 0 | The deletion flag. |
| --isDisable | Boolean | false | Indicates whether the application is disabled. |
| --enable | Boolean | true | Indicates whether the application is enabled. |
| --timeOut | Boolean | false | Indicates whether the request timed out. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |
| -size | Integer | 100 | The size. |

#### ListAppsByGwInstanceId

Queries a list of applications by gateway instance ID.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
|---|---|---|---|---|---|
| serviceTyp e | Integ er | Body | No | REST | The service type. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array | {} | The data. |
| -groups | String | [] | The list of groups. |
| -appTags | Array | [] | The list of application tags. |
| - strategyConfig s | Array | [] | The list of policy configurations. |
| --scopes | String | [] | The list of authorization scopes. |
| -- strategyConfig Id | String | strategy-config- 001 | The policy configuration ID. |
| -- strategyConfig Name | String | Default Policy | The policy configuration name. |
| -- strategyName | String | Throttling Policy | The policy name. |
| --status | Boolean | 1 | The status. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -appId | String | 12345678 | The application ID. |

| -appName | String | Sample Application | The application name. |
|---|---|---|---|
| -useAuth | Boolean | true | Indicates whether authentication is used. |
| -authType | Integer | jwt | The authentication type. |
| - requestHeader | String | Content-Type | The request header. |
| - authTypeNam e | String | JWT | The name of the authentication type. |
| -ipWhiteList | String | [] | The IP whitelist. |
| -useWhiteList | Boolean | true | Indicates whether the whitelist is used. |
| -description | String | This is a sample service. | The description. |
| -token | String | eyJhbGciOiJIUzI1NiI sInR5cCI6IkpXVCJ9. .. | The token. |
| -appSecret | String | as abcdefghijklmn _ op | The application ciphertext. |
| -isDisable | Boolean | false | is disabled |
| -enable | Boolean | true | Indicates whether the application is enabled. |
| -key | String | api-key-001 | The key. |
| -password | String | ******** | The password. |
| -expireTime | Integer | 2025-10-14 23:59:59 | The expiration time. |
| -appCode | String | APP20240101 | The application code. |

| -accessKey | String | LTAI5tFhqxxxxxxx | The AccessKey ID. |
|---|---|---|---|
| -secretKey | String | sk 1234567890abc _ def | The secret key. |
| -payload | Struct | {} | The request payload. |
| --subject | String | CN=example.com | The certificate subject. |
| --issuer | String | https://auth.examp le.com | The issuer. |
| - oauth2Payload | Struct | {} | The OAuth2 payload. |
| --scopes | String | [] | The list of authorization scopes. |
| -- authorizationC ode | Boolean | true | Indicates whether the authorization code grant is enabled. |
| -- clientCredenti als | Boolean | true | Indicates whether the client credentials grant is enabled. |
| --implicitGrant | Boolean | false | Indicates whether the implicit grant is enabled. |
| -- passwordGran t | Boolean | true | Indicates whether the password grant is enabled. |
| -- tokenExpiratio n | Integer | 7200 | The token expiration time, in seconds. |
| -- refreshTokenE xpiration | Integer | 86400 | The refresh token expiration time, in seconds. |
| --clientId | String | client 123456 _ | The client ID. |

| --clientSecret | String | secret abc123 _ | The client secret. |
|---|---|---|---|
| --redirectUris | String | https://example.co m/callback | The redirection URI. |
| --pkce | Boolean | true | Indicates whether PKCE is enabled. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

#### GetApp

Queries a consumer.

**Request headers**

This operation uses only common request headers. For more information, see the Common parameters document.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| appId | Strin g | Body | No | 12345678 | The ID of the application. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -groups | String | [] | The list of groups. |

| -appTags | Array | [] | The list of application tags. |
|---|---|---|---|
| - strategyConfig s | Array | [] | The list of policy configurations. |
| --scopes | String | [] | The list of authorization scopes. |
| -- strategyConfig Id | String | strategy-config- 001 | The ID of the policy configuration. |
| -- strategyConfig Name | String | Default Policy | The name of the policy configuration. |
| -- strategyName | String | Throttling Policy | The name of the policy. |
| --status | Boolean | 1 | The status. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| --scope | Struct | openid profile | The authorization scope. |
| ---scopes | String | [] | The list of authorization scopes. |
| ---routeInfos | Array | [] | The list of routing information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---serviceInfos | Array | [] | The list of service information. |
| ----name | String | my-resource | The name. |

| ----id | String | 123456 | The ID. |
|---|---|---|---|
| ---appInfos | Array | [] | The list of application information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---domainInfos | Array | [] | The list of domain name information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| --- mcpServerInfo s | Array | [] | The list of MCP server information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| -appId | String | 12345678 | The ID of the application. |
| -appName | String | Sample Application | The name of the application. |
| -useAuth | Boolean | true | Indicates whether authentication is enabled. |
| -authType | Integer | jwt | The authentication type. |
| - requestHeader | String | Content-Type | The request header. |
| - authTypeNam e | String | JWT | The name of the authentication type. |
| -ipWhiteList | String | [] | The IP whitelist. |

| -useWhiteList | Boolean | true | Indicates whether the whitelist is enabled. |
|---|---|---|---|
| -description | String | This is a sample service. | The description. |
| -token | String | eyJhbGciOiJIUzI1NiI sInR5cCI6IkpXVCJ9. .. | The token. |
| -appSecret | String | as abcdefghijklmn _ op | The application secret. |
| -isDisable | Boolean | false | Indicates whether the application is disabled. |
| -enable | Boolean | true | Indicates whether the application is enabled. |
| -key | String | api-key-001 | The key. |
| -password | String | ******** | The password. |
| -expireTime | Integer | 2025-10-14 23:59:59 | The expiration time. |
| -appCode | String | APP20240101 | The application code. |
| -accessKey | String | LTAI5tFhqxxxxxxx | The AccessKey ID. |
| -secretKey | String | sk 1234567890abc _ def | The AccessKey secret. |
| -payload | Struct | {} | The request payload. |
| --subject | String | CN=example.com | The subject of the certificate. |
| --issuer | String | https://auth.examp le.com | The issuer of the certificate. |
| - oauth2Payload | Struct | {} | The OAuth 2.0 payload. |

| --scopes | String | [] | The list of authorization scopes. |
|---|---|---|---|
| -- authorizationC ode | Boolean | true | Indicates whether the authorization code grant is enabled. |
| -- clientCredenti als | Boolean | true | Indicates whether the client credentials grant is enabled. |
| --implicitGrant | Boolean | false | Indicates whether the implicit grant is enabled. |
| -- passwordGran t | Boolean | true | Indicates whether the password grant is enabled. |
| -- tokenExpiratio n | Integer | 7200 | The validity period of the token, in seconds. |
| -- refreshTokenE xpiration | Integer | 86400 | The validity period of the refresh token, in seconds. |
| --clientId | String | client 123456 _ | The client ID. |
| --clientSecret | String | secret abc123 _ | The client secret. |
| --redirectUris | String | https://example.co m/callback | The redirection URI. |
| --pkce | Boolean | true | Indicates whether Proof Key for Code Exchange (PKCE) is enabled. |

#### CreateApp

Creates a consumer.

**Request headers**

This operation uses common request headers and does not require special request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| key | Strin g | Body | No | api-key-001 | The key. |
| payload | Json | Body | No | {} | The request payload. |
| oauth2Payl oad | Json | Body | No | {} | The OAuth2 payload. |
| password | Strin g | Body | No | ******** | The password. |
| expireTim e | Integ er | Body | No | 2025-10-14 23:59:59 | The expiration time. |
| appSecret | Strin g | Body | No | as abcdefghijklmnop _ | The application ciphertext. |
| requestHe ader | Strin g | Body | No | Content-Type | The request header. |
| token | Strin g | Body | No | eyJhbGciOiJIUzI1NiIsInR5c CI6IkpXVCJ9... | The token. |
| useAuth | Bool ean | Body | No | true | Specifies whether to use authentication. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| authType | Integ er | Body | No | jwt | The authentication type. |
| useWhiteLi st | Bool ean | Body | No | true | Specifies whether to use a whitelist. |
| ipWhiteList | Strin g | Body | No | [] | The IP whitelist. |
| appName | Strin g | Body | No | SampleApp | The application name. |

| description | Strin g | Body | No | This is a sample service. | The description. |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| userId | Strin g | Body | No | uid-123456 | The user ID. |
| userName | Strin g | Body | No | ZhangSan | The username. |
| appKey | Strin g | Body | No | ak 1234567890abcdef _ | The application key. |
| groups | Repe atLis t | Body | No | [] | The list of groups. |
| appCode | Strin g | Body | No | APP20240101 | The application code. |
| accessKey | Strin g | Body | No | LTAI5tFhqxxxxxxx | The AccessKey ID. |
| secretKey | Strin g | Body | No | sk 1234567890abcdef _ | The secret key. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### ModifyApp

Modifies a consumer.

**Request header**

This operation uses common request headers. For more information, see the topic on common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| key | Strin g | Body | No | api-key-001 | The key. |
| payload | Json | Body | No | {} | The request payload. |
| oauth2Payl oad | Json | Body | No | {} | The OAuth2 payload. |
| password | Strin g | Body | No | ******** | The password. |
| expireTim e | Integ er | Body | No | 2025-10-14 23:59:59 | The expiration time. |
| appSecret | Strin g | Body | No | as abcdefghijklmnop _ | The application ciphertext. |
| requestHe ader | Strin g | Body | No | Content-Type | The request header. |
| token | Strin g | Body | No | eyJhbGciOiJIUzI1NiIsInR5c CI6IkpXVCJ9... | The token. |
| useAuth | Bool ean | Body | No | true | Specifies whether to use authentication. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| authType | Integ er | Body | No | jwt | The authentication type. |
| useWhiteLi st | Bool ean | Body | No | true | Specifies whether to use a whitelist. |
| ipWhiteList | Strin g | Body | No | [] | The IP address whitelist. |

| appName | Strin g | Body | No | ExampleApp | The application name. |
|---|---|---|---|---|---|
| description | Strin g | Body | No | This is an example service. | The description. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| userId | Strin g | Body | No | uid-123456 | The user ID. |
| userName | Strin g | Body | No | Zhang San | The username. |
| appKey | Strin g | Body | No | ak 1234567890abcdef _ | The application key. |
| groups | Repe atLis t | Body | No | [] | The list of groups. |
| appCode | Strin g | Body | No | APP20240101 | The application code. |
| accessKey | Strin g | Body | No | LTAI5tFhqxxxxxxx | The AccessKey ID. |
| secretKey | Strin g | Body | No | sk 1234567890abcdef _ | The AccessKey secret. |
| appAddres s | Strin g | Body | No | https://example.com | The application address. |
| appTagsSt r | Strin g | Body | No | tag1,tag2,tag3 | A string of application tags. |
| chargePers onName | Strin g | Body | No | Zhang San | The name of the owner. |
| openCross | Bool ean | Body | No | true | Specifies whether to enable cross-domain requests. |

| allowedOri gins | Strin g | Body | No | * | The allowed source domain names. |
|---|---|---|---|---|---|
| allowedHe aders | Strin g | Body | No | Content- Type,Authorization | The allowed request headers. |
| allowedMe thods | Strin g | Body | No | [] | The list of allowed request methods. |
| isDisable | Bool ean | Body | No | false | Specifies whether to disable the application. |
| appType | Integ er | Body | No | 1 | The application type. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The returned message. |
| data | String | {} | The data |

#### DeleteApp

Deletes a consumer.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| appId | Strin g | Body | No | 12345678 | The application ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### ModifyAppOpenStatus

Enables or disables a consumer application.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| appId | Strin g | Body | No | 12345678 | The ID of the application. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| enable | Bool ean | Body | No | true | Specifies whether to enable the application. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Map | {} | The data. |

| Developer Guide·A | PI Gateway |   | API Gatewa |
|---|---|---|---|

#### ModifyAppWhiteListStatus

Modifies the status of a consumer whitelist.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| isOpen | Bool ean | Body | No | true | Specifies whether to enable the whitelist. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | String | {} | The data |

#### GetAppAuth

Queries the authorization for a consumer.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| authId | Strin g | Body | No | auth 123456 _ | The authentication ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -authId | Integer | auth 123456 _ | The authentication ID. |
| -appId | String | 12345678 | The application ID. |
| -routeId | String | route-123456 | The route ID. |
| -routePath | String | /api/v1/users | The route path. |
| -serviceId | Integer | service-123456 | The service ID. |
| -serviceName | String | user-service | The service name. |
| - serviceProtoco l | String | HTTP | The service protocol. |
| -authStatus | Integer | 1 | The authentication status. |

#### CreateAppAuth

Creates a consumer authorization.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| body | Strin g | Body | No | {"key":"value"} | The request body. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The response code. |
| Msg | String | Operation successful | The response message. |
| Data | String | {} | The data. |

#### BatchCreateAppAuthByRoute

Grants batch authorization to consumers.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| appId | Strin g | Body | No | 12345678 | The ID of the application. |
| routeId | Repe atLis t | Body | No | route-123456 | The ID of the route. |

| authStatus | Integ er | Body | No | 1 | The authentication status. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data |

#### ModifyAppAuthStatus

Modifies the authorization status of a consumer.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| authId | Strin g | Body | No | auth 123456 _ | The authorization ID. |
| authStatus | Integ er | Body | No | 1 | The authorization status. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |

| msg | String | The operation was successful. | The message. |
|---|---|---|---|
| data | Struct | {} | The data. |
| -id | Integer | 123456 | The ID. |
| -createBy | Integer | 1001 | The ID of the user who created the resource. |
| -updateBy | Integer | 1001 | The ID of the user who last updated the resource. |
| -appId | String | 12345678 | The application ID. |
| -authId | String | auth 123456 _ | The authorization ID. |
| -routeId | String | route-123456 | The routing ID. |
| -authStatus | Integer | 1 | The authorization status. |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | The gateway instance ID. |

#### DeleteAppAuth

Deletes a consumer authorization.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| authId | Strin g | Body | No | auth 123456 _ | The authorization ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | String | {} | The data. |

#### RefreshToken

Refreshes a token.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| key | Strin g | Body | No | api-key-001 | The key. |
| payload | Json | Body | No | {} | The request payload. |
| oauth2Payl oad | Json | Body | No | {} | The OAuth2 payload. |
| password | Strin g | Body | No | ******** | The password. |
| expireTim e | Integ er | Body | No | 2025-10-14 23:59:59 | The expiration time. |
| appSecret | Strin g | Body | No | as abcdefghijklmnop _ | The application ciphertext. |
| requestHe ader | Strin g | Body | No | Content-Type | The request header. |

| token | Strin g | Body | No | eyJhbGciOiJIUzI1NiIsInR5c CI6IkpXVCJ9... | The token. |
|---|---|---|---|---|---|
| useAuth | Bool ean | Body | No | true | Specifies whether to use authentication. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| authType | Integ er | Body | No | jwt | The authentication type. |
| useWhiteLi st | Bool ean | Body | No | true | Specifies whether to use a whitelist. |
| ipWhiteList | Strin g | Body | No | [] | The IP whitelist. |
| appName | Strin g | Body | No | Sample Application | The application name. |
| description | Strin g | Body | No | This is a sample service. | The description. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| userId | Strin g | Body | No | uid-123456 | The user ID. |
| userName | Strin g | Body | No | Zhang San | The username. |
| appKey | Strin g | Body | No | ak 1234567890abcdef _ | The application key. |
| groups | Repe atLis t | Body | No | [] | The list of groups. |
| appCode | Strin g | Body | No | APP20240101 | The application code. |

| accessKey | Strin g | Body | No | LTAI5tFhqxxxxxxx | The AccessKey ID. |
|---|---|---|---|---|---|
| secretKey | Strin g | Body | No | sk 1234567890abcdef _ | The secret key. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Map | {} | The data. |

#### ResetSecretKey

Resets a secret key.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| appId | Strin g | Body | No | 12345678 | The ID of the application. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |

| msg | String | The operation was successful. | The message |
|---|---|---|---|
| data | Boolean | {} | The data |

#### HandlerConsumerAuth

Queries the authentication information for a consumer.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| isOpen | Bool ean | Body | No | true | Specifies whether the feature is enabled. |
| name | Strin g | Body | No | my-resource | The name. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| strategyCo nfigId | Strin g | Body | No | strategy-config-001 | The ID of the policy configuration. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | String | {} | The data. |

#### CreateAppAuthByRoute

Create a consumer authorization.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| appId | Strin g | Body | No | 12345678 | The ID of the application. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |
| authStatus | Integ er | Body | No | 1 | The authorization status. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation is successful. | The message. |
| data | String | {} | The data. |

#### BatchDeleteApp

Deletes consumers in a batch.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| > Document V | ersion: 2 | 026082 | 8 |   | 31 |
|---|---|---|---|---|---|

| Parameter Name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| appIds | Repe atLis t | Body | No | [] | A list of application IDs. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -successIds | String | [] | Successful IDs |
| -failedIds | String | [] | Failed IDs |

### Plugin Management

#### ListPlugins

Queries a list of plugins.

**Request header**

This operation has no special request headers. For more information about common request headers, see the common request parameters document.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| current | Integ er | Body | No | 1 | The current page number. |

| size | Integ er | Body | No | 100 | The size. |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| searchNa me | Strin g | Body | No | search keyword | The name to search for. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |
| data | Struct | {} | The data. |
| -records | Array | [] | The list of records. |
| --config | Array | [] | The list of configurations. |
| ---name | String | my-resource | The name. |
| ---required | Boolean | true | Indicates whether the parameter is required. |
| --pluginId | String | plugin-123456 | The plugin ID. |
| --gwInstanceId | String | i- c0a81bb16a1524a 17 | The ID of the gateway instance. |
| --pluginName | String | rate-limiter | The plugin name. |
| --description | String | This is an example service. | The description. |
| --downloadURL | String | https://example.co m/download/file.zip | The download URL. |

| --type | Integer | 1 | The type. |
|---|---|---|---|
| --used | Boolean | false | Indicates whether the plugin is used. |
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

#### ListOpenPlugins

Lists the open plugins.

**Request headers**

This operation uses only the common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| current | Integ er | Body | No | 1 | The current page number. |
| size | Integ er | Body | No | 100 | The size. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| searchNa me | Strin g | Body | No | Search keyword | The search keyword. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array | {} | The data. |
| -config | Array | [] | The list of configurations. |

| --name | String | my-resource | The name. |
|---|---|---|---|
| --required | Boolean | true | Indicates whether the parameter is required. |
| -pluginId | String | plugin-123456 | The plugin ID. |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | The gateway instance ID. |
| -pluginName | String | rate-limiter | The plugin name. |
| -description | String | This is a sample service. | The description. |
| -downloadURL | String | https://example.co m/download/file.zip | The download URL. |
| -type | Integer | 1 | The type. |
| -used | Boolean | false | Indicates whether the plugin is used. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

#### ListGlobalPlugins

Retrieves a list of global plugins.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| current | Integ er | Body | No | 1 | The current page number. |

| size | Integ er | Body | No | 100 | The size. |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| searchNa me | Strin g | Body | No | A search keyword | Search by name. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |
| data | Struct | {} | The data. |
| -records | Array | [] | The list of records. |
| --gwInstanceId | String | i- c0a81bb16a1524a 17 | The ID of the gateway instance. |
| --pluginId | String | plugin-123456 | The ID of the plugin. |
| --routePluginId | String | plugin-route-001 | The ID of the routing plugin. |
| --pluginName | String | rate-limiter | The name of the plugin. |
| --config | String | [] | The list of configurations. |
| --status | Boolean | 1 | The status. |
| --createTime | String | 2024-10-14 08:00:00 | The time when the plugin was created. |
| --updateTime | String | 2024-10-14 15:00:00 | The time when the plugin was last updated. |

| --order | Integer | 100 | The sort number. |
|---|---|---|---|
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

#### ListRoutePlugins

Queries a list of routing plugins.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter Name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| current | Integ er | Body | No | 1 | The current page number. |
| size | Integ er | Body | No | 100 | Size |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| routeId | Strin g | Body | No | route-123456 | The routing ID. |
| searchNa me | Strin g | Body | No | Search keyword | Search by name |

**Response parameters**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |

| msg | String | Operation successful. | The message. |
|---|---|---|---|
| data | Struct | {} | The data. |
| -records | Array | [] | The list of records. |
| --gwInstanceId | String | i- c0a81bb16a1524a 17 | The gateway instance ID. |
| --routeId | String | route-123456 | The routing ID. |
| --pluginId | String | plugin-123456 | The plugin ID. |
| --routePluginId | String | plugin-route-001 | The routing plugin ID. |
| --pluginName | String | rate-limiter | The plugin name. |
| --config | String | [] | The list of configurations. |
| --status | Boolean | 1 | The status. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| --order | Integer | 100 | The sort number. |
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

#### GetPlugin

Retrieves a plugin.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| pluginId | Strin g | Body | No | plugin-123456 | The plugin ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Struct | {} | The data |
| -config | Array | [] | The list of configurations. |
| --name | String | my-resource | The name. |
| --required | Boolean | true | Indicates whether the parameter is required. |
| -pluginId | String | plugin-123456 | The plugin ID. |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | The gateway instance ID. |
| -pluginName | String | rate-limiter | The plugin name. |
| -description | String | This is a sample service. | Description. |

| -downloadURL | String | https://example.co m/download/file.zip | The download URL. |
|---|---|---|---|
| -type | Integer | 1 | The type. |
| -used | Boolean | false | Indicates whether the plugin is used. |

#### CreatePlugin

Creates a plugin.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| pluginNam e | Strin g | Body | No | rate-limiter | The plugin name. |
| description | Strin g | Body | No | This is an example service. | The description. |
| downloadU RL | Strin g | Body | No | https://example.com/dow nload/file.zip | The download URL. |
| config | Repe atLis t | Body | No | [] | The configuration list. |
| -name | Strin g | Body | No | my-resource | The name. |
| -required | Bool ean | Body | No | true | Specifies whether the configuration is required. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message. |
| data | String | {} | The data. |

#### CreateGlobalPlugin

Creates a global plugin.

**Request headers**

This operation uses only common request headers. For more information, see the common request parameters document.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| pluginId | Strin g | Body | No | plugin-123456 | The ID of the plugin. |
| order | Integ er | Body | No | 100 | The sorting number. |
| status | Bool ean | Body | No | 1 | The status. |
| config | Strin g | Body | No | [] | The list of configurations. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |

| msg | String | The operation was successful. | The message. |
|---|---|---|---|
| data | String | {} | The data. |

#### CreateRoutePlugin

Creates a routing plugin.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |
| pluginId | Strin g | Body | No | plugin-123456 | The ID of the plugin. |
| order | Integ er | Body | No | 100 | The order number. |
| status | Bool ean | Body | No | 1 | The status. |
| config | Strin g | Body | No | [] | The list of configurations. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

| data | String | {} | The data. |
|---|---|---|---|

#### ModifyPlugin

Modifies a plugin.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| pluginId | Strin g | Body | No | plugin-123456 | The ID of the plugin. |
| description | Strin g | Body | No | This is a sample service. | The description. |
| downloadU RL | Strin g | Body | No | https://example.com/dow nload/file.zip | The download URL. |
| config | Repe atLis t | Body | No | [] | A list of configurations. |
| -name | Strin g | Body | No | my-resource | The name. |
| -required | Bool ean | Body | No | true | Specifies whether the configuration is required. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |

| msg | String | The operation was successful. | The message. |
|---|---|---|---|
| data | String | {} | The data. |

#### ModifyGlobalPlugin

Modifies a global plugin.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| routePlugi nId | Strin g | Body | No | plugin-route-001 | The routing plugin ID. |
| order | Integ er | Body | No | 100 | The order number. |
| config | Strin g | Body | No | [] | The configuration list. |
| status | Bool ean | Body | No | 1 | The status. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |
| data | String | {} | The data. |

| PI Gateway |   |   | Developer Guide·API Gatewa |
|---|---|---|---|

#### ModifyRoutePlugin

Modifies a routing plugin.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |
| routePlugi nId | Strin g | Body | No | plugin-route-001 | The ID of the routing plugin. |
| order | Integ er | Body | No | 100 | The order number. |
| config | Strin g | Body | No | [] | The configuration list. |
| status | Bool ean | Body | No | 1 | The status. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### DeletePlugin

Deletes a plugin.

**Request headers**

This operation requires only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| pluginId | Strin g | Body | No | plugin-123456 | The plugin ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | String | {} | The data |

#### DeleteGlobalPlugin

Deletes a global plugin.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

| routePlugi nId | Strin g | Body | No | plugin-route-001 | The ID of the routing plugin. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### DeleteRoutePlugin

Deletes a route plugin.

**Request headers**

This operation uses only common request headers. For more information, see the Common request parameters document.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |
| routePlugi nId | Strin g | Body | No | plugin-route-001 | The ID of the route plugin. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |

| msg | String | The operation was successful. | The message |
|---|---|---|---|
| data | String | {} | The data |

#### ModifyGlobalPluginStatus

Modifies the status of a global plugin.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| routePlugi nId | Strin g | Body | No | plugin-route-001 | The routing plugin ID. |
| order | Integ er | Body | No | 100 | The sort number. |
| config | Strin g | Body | No | [] | The configuration list. |
| status | Bool ean | Body | No | 1 | The status. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message. |
| data | String | {} | The data. |

| PI Gateway |   |   | Developer Guide·API Gatewa |
|---|---|---|---|

#### ModifyRoutePluginStatus

Modifies the status of a route plugin.

**Request headers**

This operation uses common request headers. No special request headers are used. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| routeId | Strin g | Body | No | route-123456 | The route ID. |
| routePlugi nId | Strin g | Body | No | plugin-route-001 | The route plugin ID. |
| order | Integ er | Body | No | 100 | The sort number. |
| config | Strin g | Body | No | [] | The configuration list. |
| status | Bool ean | Body | No | 1 | The status. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### ListPluginUsage

Queries the usage of plugins.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| current | Integ er | Body | No | 1 | The current page number. |
| size | Integ er | Body | No | 100 | The size |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| pluginId | Strin g | Body | No | plugin-123456 | The plugin ID. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -records | Array | [] | The list of records. |
| --routeId | String | route-123456 | The route ID. |
| --routeName | String | user-service-route | The route name. |

| --status | Boolean | 1 | The status. |
|---|---|---|---|
| -size | Integer | 100 | The size. |
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

### Policy Management

#### ModifyStrategyConfig

Modifies a policy configuration.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter Name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| strategyCo nfigName | Strin g | Body | No | DefaultPolicy | The name of the policy configuration. |
| strategyCo nfigId | Strin g | Body | No | strategy-config-001 | The ID of the policy configuration. |
| strategyNa me | Strin g | Body | No | ThrottlingPolicy | The policy name. |
| config | Json | Body | No | [] | The list of configurations. |
| rawConfig | Strin g | Body | No | {"timeout":30} | Original configuration. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| routeId | Strin g | Body | No | route-123456 | The routing ID. |

| serviceId | Strin g | Body | No | service-123456 | The service ID. |
|---|---|---|---|---|---|
| appId | Strin g | Body | No | 12345678 | The application ID. |
| domainId | Strin g | Body | No | domain-123456 | The domain ID. |
| routeIds | Repe atLis t | Body | No | [] | The list of routing IDs. |
| serviceIds | Repe atLis t | Body | No | [] | The list of service IDs. |
| appIds | Repe atLis t | Body | No | [] | The list of application IDs. |
| domainIds | Repe atLis t | Body | No | [] | The list of domain IDs. |
| mcpIds | Repe atLis t | Body | No | [] | The list of MCP IDs. |
| status | Bool ean | Body | No | 1 | The status. |

**Response parameters**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message. |
| data | String | {} | The data. |

#### CreateStrategyConfig

Creates a strategy configuration.

**Request header**

This operation uses common request headers and requires no special request headers. For more information, see Common request parameters.

| Parameter Name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| strategyCo nfigName | Strin g | Body | No | Default Policy | The name of the strategy configuration. |
| strategyNa me | Strin g | Body | No | default | The name of the policy. |
| config | Json | Body | No | [] | The list of configurations. |
| rawConfig | Strin g | Body | No | {"timeout":30} | The raw configuration. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The route ID. |
| serviceId | Strin g | Body | No | service-123456 | The service ID. |
| appId | Strin g | Body | No | 12345678 | The application ID. |
| mcpServer Id | Strin g | Body | No | mcp-server-001 | The ID of the MCP server. |
| domainId | Strin g | Body | No | domain-123456 | The domain ID. |
| routeIds | Repe atLis t | Body | No | [] | A list of route IDs. |

| serviceIds | Repe atLis t | Body | No | [] | A list of service IDs. |
|---|---|---|---|---|---|
| appIds | Repe atLis t | Body | No | [] | A list of application IDs. |
| domainIds | Repe atLis t | Body | No | [] | A list of domain IDs. |
| mcpIds | Repe atLis t | Body | No | [] | A list of MCP IDs. |
| strategyCo nfigId | Strin g | Body | No | strategy-config-001 | The ID of the strategy configuration. |

**Response parameters**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message |
| data | String | {} | The data. |

#### ListStrategies

Queries a list of policies.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| size | Integ er | Body | No | 100 | The size |
|---|---|---|---|---|---|
| current | Integ er | Body | No | 1 | The current page number. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| scope | Strin g | Body | No | openid profile | The authorization scope. |
| strategyNa me | Strin g | Body | No | throttling policy | The policy name. |
| brokerEngi neType | Strin g | Body | No | RocketMQ | The type of the message engine. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array | {} | The data. |
| -strategies | Array | [] | The list of policies. |
| --scopes | String | [] | The list of authorization scopes. |
| --uiStyles | String | [] | The list of UI styles. |
| -- strategyName | String | throttling policy | The policy name. |
| --strategyTitle | String | Advanced Throttling | The policy title. |
| --description | String | This is an example service. | The description. |
| -- supportCascad e | Integer | 1 | Indicates whether cascading is supported. |

| -- rawConfigExa mple | String | {"enabled":true} | An example of the raw configuration. |
|---|---|---|---|
| --order | Integer | 100 | The order number. |
| --document | String | API operation document | The document. |
| -category | Struct | {} | The category information. |
| --name | String | my-resource | The name. |
| --title | String | API operation title | The title. |
| --order | Integer | 100 | The order number. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

#### ListStrategyConfigs

Queries a list of policy configurations.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| size | Integ er | Body | No | 100 | The size. |
| current | Integ er | Body | No | 1 | The current page number. |
| strategyCo nfigName | Strin g | Body | No | Default Policy | The name of the policy configuration. |

| strategyCo nfigId | Strin g | Body | No | strategy-config-001 | The ID of the policy configuration. |
|---|---|---|---|---|---|
| strategyNa me | Strin g | Body | No | throttling policy | The name of the policy. |
| scope | Json | Body | No | openid profile | The authorization scope. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message |
| data | Struct | {} | The data |
| -records | Array | [] | The list of records. |
| --scopes | String | [] | The list of authorization scopes. |
| -- strategyConfig Id | String | strategy-config- 001 | The ID of the policy configuration. |
| -- strategyConfig Name | String | Default Policy | The name of the policy configuration. |
| -- strategyName | String | throttling policy | The name of the policy. |
| --status | Boolean | 1 | The status. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |

| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
|---|---|---|---|
| --scope | Struct | openid profile | The authorization scope. |
| ---scopes | String | [] | The list of authorization scopes. |
| ---routeInfos | Array | [] | The list of routing information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---serviceInfos | Array | [] | The list of service information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---appInfos | Array | [] | The list of application information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| ---domainInfos | Array | [] | The list of domain name information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |
| --- mcpServerInfo s | Array | [] | The list of MCP server information. |
| ----name | String | my-resource | The name. |
| ----id | String | 123456 | The ID. |

| -total | Integer | 1000 | The total number of entries. |
|---|---|---|---|
| -current | Integer | 1 | The current page number. |
| -size | Integer | 100 | The size. |

#### GetStrategy

Queries a policy.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| strategyNa me | Strin g | Body | No | throttling policy | The name of the policy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -scopes | String | [] | The list of authorization scopes. |
| -uiStyles | String | [] | The list of UI styles. |
| -strategyName | String | throttling policy | The name of the policy. |

| -strategyTitle | String | Advanced Throttling | The title of the policy. |
|---|---|---|---|
| -description | String | This is an example service. | The description. |
| - supportCascad e | Integer | 1 | Indicates whether cascading is supported. |
| - rawConfigExa mple | String | {"enabled":true} | An example of the raw configuration. |
| -order | Integer | 100 | The sort number. |
| -document | String | API operation document | The document. |

#### GetStrategyConfig

Queries a policy configuration.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| strategyCo nfigId | Strin g | Body | No | strategy-config-001 | The ID of the policy configuration. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |

| msg | String | The operation was successful. | The message. |
|---|---|---|---|
| data | Struct | {} | The data. |
| -scopes | String | [] | A list of authorization scopes. |
| - strategyConfig Name | String | Default Policy | The name of the policy configuration. |
| - strategyConfig Id | String | strategy-config- 001 | The ID of the policy configuration. |
| -strategyName | String | Throttling Policy | The name of the policy. |
| -routeId | String | route-123456 | The ID of the route. |
| -routeName | String | user-service-route | The name of the route. |
| -serviceId | String | service-123456 | The ID of the service. |
| -serviceName | String | user-service | The name of the service. |
| -appId | String | 12345678 | The ID of the application. |
| -appName | String | Sample Application | The name of the application. |
| -domainId | String | domain-123456 | The ID of the domain name. |
| -domainName | String | example.com | The domain name. |
| -status | Boolean | 1 | The status. |
| -config | Map | [] | A list of configurations. |
| -rawConfig | String | {"timeout":30} | The raw configuration. |

| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
|---|---|---|---|
| -updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -scope | Struct | openid profile | The authorization scope. |
| --scopes | String | [] | A list of authorization scopes. |
| --routeInfos | Array | [] | A list of route information. |
| ---name | String | my-resource | The name. |
| ---id | String | 123456 | The ID. |
| --serviceInfos | Array | [] | A list of service information. |
| ---name | String | my-resource | The name. |
| ---id | String | 123456 | The ID. |
| --appInfos | Array | [] | A list of application information. |
| ---name | String | my-resource | The name. |
| ---id | String | 123456 | The ID. |
| --domainInfos | Array | [] | A list of domain name information. |
| ---name | String | my-resource | The name. |
| ---id | String | 123456 | The ID. |
| -- mcpServerInfo s | Array | [] | A list of MCP server information. |
| ---name | String | my-resource | The name. |

| ---id | String | 123456 | The ID. |
|---|---|---|---|

#### GetRoutePolicies

Queries routing policies.

**Request headers**

This operation uses common request headers. For more information, see Common parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| routeId | Strin g | Body | No | route-123456 | The ID of the route. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | Struct | {} | The data. |
| -rewrite | Struct | {} | The rewrite configuration. |
| --enabled | Boolean | true | Indicates whether the feature is enabled. |
| --path | String | /api/v1/resource | The path. |
| --host | String | api.example.com | The host address. |
| -headerControl | Struct | {} | The request header control configuration. |

| --enabled | Boolean | true | Indicates whether the feature is enabled. |
|---|---|---|---|
| --request | Struct | {} | The request structure. |
| ---remove | String | [] | The list of items to remove. |
| ---add | Array | [] | The list of items to add. |
| ----key | String | api-key-001 | The key. |
| ----value | String | example-value | The value. |
| ---set | Array | [] | The list of items to set. |
| ----key | String | api-key-001 | The key. |
| ----value | String | example-value | The value. |
| --response | Struct | {} | The response structure. |
| ---remove | String | [] | The list of items to remove. |
| ---add | Array | [] | Add a list |
| ----key | String | api-key-001 | The key. |
| ----value | String | example-value | The value. |
| ---set | Array | [] | The list of items to set. |
| ----key | String | api-key-001 | The key. |
| ----value | String | example-value | The value. |
| -timeoutConfig | Struct | {} | The timeout configuration. |
| --enabled | Boolean | true | Indicates whether the feature is enabled. |

| --timeout | Integer | 30000 | The timeout period in milliseconds. |
|---|---|---|---|
| -fallbackConfig | Struct | {} | The fallback configuration. |
| -- responseCode s | String | [] | The list of response codes. |
| --services | Array | [] | The list of services. |
| ---name | String | my-resource | The name. |
| ---port | Integer | 8080 | The port number. |
| ---version | String | 1.0.0 | The version number. |
| ---weight | Integer | 100 | The weight. |
| --enabled | Boolean | true | Indicates whether the feature is enabled. |
| -- fallbackStrate gy | String | default | The fallback strategy. |

#### ModifyRoutePolicy

Modifies a routing policy.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| configType | Strin g | Body | No | yaml | The configuration type. |
| configData | Json | Body | No | {} | The configuration data. |

| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
|---|---|---|---|---|---|
| routeId | Strin g | Body | No | route-123456 | The route ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### DeleteStrategyConfig

Deletes a policy configuration.

**Request headers**

This operation uses common request headers and requires no special request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |
| strategyCo nfigId | Strin g | Body | No | strategy-config-001 | The ID of the policy configuration. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |

| msg | String | The operation was successful. | The message |
|---|---|---|---|
| data | String | {} | The data. |

#### ModifyStrategyConfigStatus

Modifies the status of a policy configuration.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| isOpen | Bool ean | Body | No | true | Specifies whether to enable the policy configuration. |
| strategyCo nfigId | Strin g | Body | No | strategy-config-001 | The ID of the policy configuration. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The ID of the gateway instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The response message. |
| data | String | {} | The data |

### Domain name management

#### ListDomains

Queries a list of domain names.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| size | Integ er | Body | No | 10 | The number of entries to return on each page for a paged query. |
| current | Integ er | Body | No | 1 | Set the page on which the returned results are displayed. The default value is 1, indicating that the display starts on page 1. |
| domain | Strin g | Body | No | www.aliyun.com | The domain name. |
| gwInstanc eId | Strin g | Body | No | i-xxxxxxx | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The interface status or POP error code. |
| Msg | String | success | The status description. If `Code` is `200`, `Msg` is usually empty. |
| Data | Struct | {} | The response data. |
| -Records | Array | [] | The record that returns the data result. |
| --DomainId | String | 00efd71a-770e- 4255-b54e- 6fe5659baffe | The domain name ID. |
| --CertificateId | String | 12345678-1234- 1234-1234- 12345678**** | The certificate ID. |

| -- CertificateNam e | String | myCertificate | The name of the SSL certificate. |
|---|---|---|---|
| --Domain | String | www.aliyun.com | The domain name. |
| --Protocol | String | HTTP | The protocol type. |
| --CreateTime | String | 2024-03- 15T01:46Z | The creation time. |
| --UpdateTime | String | 2024-03- 15T01:46Z | The update time. |
| --ClientAuth | Integer | 0 | Indicates whether mutual authentication is enabled. 0: disabled. 1: enabled. |
| -- CaCertificateId | String | 00efd71a-770e- 4255-b54e- 6fe5659baffe | The CA certificate ID. |
| -- CaCertificateN ame | String | test | The name of the CA certificate. |
| -Size | Long | 20 | The number of entries on each page. |
| -Total | Long | 1 | The total number of entries. |
| -Current | Long | 1 | The current page number. |

**Examples**

Sample response in `JSON` format `{`

```json
 "Msg":"success",
 "Data":{
  "Records":[
```

`{`

```json
    "DomainId":"00efd71a-770e-4255-b54e-6fe5659baffe",
    "CertificateId":"12345678-1234-1234-1234-12345678****",
    "CreateTime":"2024-03-15T01:46Z",
    "UpdateTime":"2024-03-15T01:46Z",
    "CertificateName":"myCertificate",
    "Domain":"www.aliyun.com",
    "Protocol":"HTTP",
    "ClientAuth":0,
    "CaCertificateName":"test",
    "CaCertificateId":"00efd71a-770e-4255-b54e-6fe5659baffe"
```

`}` `],`

```json
  "Size":20,
  "Total":1,
  "Current":1
```

`},`

```json
 "Code":200
```

`}`

#### ListAllDomains

Queries a list of all domain names.

**Request headers**

This operation requires only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| serviceTyp e | Integ er | Body | No | REST | The service type. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| data | Array | {} | The data |
|---|---|---|---|
| -domainId | String | domain-123456 | The domain name ID. |
| -certificateId | String | cert-987654 | The certificate ID. |
| - certificateNam e | String | MyCert | The certificate name. |
| -domain | String | api.example.com | The domain name. |
| -protocol | String | HTTP | The protocol. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -clientAuth | Integer | 1 | The client authentication method. |
| - caCertificateId | String | cert-123456 | The CA certificate ID. |
| - caCertificateN ame | String | MyCA | The name of the CA certificate. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

#### GetDomain

Queries the details of a domain name.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| domainId | Strin g | Body | No | domain-123456 | The domain name ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message |
| data | Struct | {} | The data |
| -routeInfos | Array | [] | The list of routing information. |
| --routeId | String | route-123456 | The routing ID. |
| --routeName | String | user-service-route | The routing name. |
| --serviceId | String | service-123456 | The service ID. |
| --serviceName | String | user-service | The service name. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -domainId | String | domain-123456 | The domain name ID. |
| -domain | String | api.example.com | The domain name. |
| -protocol | String | HTTP | The protocol. |

| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
|---|---|---|---|
| -updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -certificateId | String | cert-987654 | The certificate ID. |
| -clientAuth | Integer | 1 | The client authentication method. |
| - caCertificateId | String | cert-123456 | The CA certificate ID. |
| -subjectDn | String | CN=example.com, O=Example,C=CN | The subject distinguished name (DN) of the certificate. |
| -issuerDn | String | CN=Example CA, O=Example Inc, C=CN | The issuer DN. |

#### CreateDomain

Creates a domain name.

**Request headers**

This operation uses common request headers and does not use special request headers. For more information, see Common request parameters.

| Parameter name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| domainId | Strin g | Body | No | domain-123456 | The domain name ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| protocol | Strin g | Body | No | HTTP | The protocol. |

| certificateI d | Strin g | Body | No | cert-987654 | The certificate ID. |
|---|---|---|---|---|---|
| domain | Strin g | Body | No | api.example.com | The domain name. |
| clientAuth | Integ er | Body | No | 1 | The client authentication method. |
| caCertifica teId | Strin g | Body | No | cert-123456 | The CA certificate ID. |
| subjectDn | Strin g | Body | No | CN=example.com,O=Exa mple,C=CN | The subject distinguished name (DN) of the certificate. |
| issuerDn | Strin g | Body | No | CN=Example CA, O=Example Inc, C=CN | The issuer DN. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### ModifyDomain

Modifies a domain name.

**Request headers**

This operation uses common request headers and does not have any special request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|

| domainId | Strin g | Body | No | domain-123456 | The domain name ID. |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| protocol | Strin g | Body | No | HTTP | The protocol. |
| certificateI d | Strin g | Body | No | cert-987654 | The certificate ID. |
| domain | Strin g | Body | No | api.example.com | The domain name. |
| clientAuth | Integ er | Body | No | 1 | The client authentication method. |
| caCertifica teId | Strin g | Body | No | cert-123456 | The CA certificate ID. |
| subjectDn | Strin g | Body | No | CN=example.com,O=Exa mple,C=CN | The subject DN of the certificate. |
| issuerDn | Strin g | Body | No | CN=Example CA, O=Example Inc, C=CN | The issuer DN. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### DeleteDomain

Deletes a domain name.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| domainId | Strin g | Body | No | domain-123456 | The domain name ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message. |
| data | String | {} | The data. |

### Certificate Management

#### ListCertificates

Retrieves a list of certificates.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| size | Integ er | Body | No | 100 | The size |
| current | Integ er | Body | No | 1 | The current page number. |

| sni | Strin g | Body | No | example.com | The Server Name Indication (SNI) domain name. |
|---|---|---|---|---|---|
| certType | Integ er | Body | No | 1 | The certificate type. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | Struct | {} | The data. |
| -records | Array | [] | The record list. |
| --snis | String | [] | The list of SNI domain names. |
| --expireTime | String | 2025-10-14 23:59:59 | The expiration time. |
| --updateTime | String | 2024-10-14 15:00:00 | The update time. |
| --createTime | String | 2024-10-14 08:00:00 | The creation time. |
| -- certificateNam e | String | MyCert | The certificate name. |
| --certificateId | String | cert-987654 | The certificate ID. |
| --certType | Integer | 1 | The certificate type. |

| -size | Integer | 100 | The size |
|---|---|---|---|
| -total | Integer | 1000 | The total number of entries. |
| -current | Integer | 1 | The current page number. |

#### ListAllServerCertificates

Queries the list of all server certificates.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| serviceTyp e | Integ er | Body | No | REST | The service type. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | Map | {} | The data |

#### ListAllCACertificates

Retrieves the list of all CA certificates.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| serviceTyp e | Integ er | Body | No | REST | The service type. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array | {} | The Data. |
| -snis | String | [] | The list of SNI domain names. |
| -expireTime | String | 2025-10-14 23:59:59 | The expiration time. |
| -updateTime | String | 2024-10-14 15:00:00 | The update time. |
| -createTime | String | 2024-10-14 08:00:00 | The creation time. |
| - certificateNam e | String | MyCert | The certificate name. |
| -certificateId | String | cert-987654 | The certificate ID. |
| -certType | Integer | 1 | The certificate type. |
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |

#### GetCertificate

Queries a certificate.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| certificateI d | Strin g | Body | No | cert-987654 | The certificate ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | Struct | {} | The data. |
| -snis | String | [] | The list of SNI domain names. |
| -signTime | String | 2024-10-14 10:30:00 | The time when the certificate was signed. |
| -expireTime | String | 2025-10-14 23:59:59 | The expiration time. |
| -algorithm | String | sha256 | The type of the algorithm. |
| - privateKeyLen | Integer | 2048 | The length of the private key. |
| -fingerPrint | String | a1b2c3d4e5f6 | Fingerprint. |

| -signerCN | String | Example Corp | The common name (CN) of the signer. |
|---|---|---|---|
| -signerOU | String | IT Department | The organizational unit (OU) of the signer. |
| - certificateNam e | String | MyCert | The certificate name. |
| -certificateId | String | cert-987654 | The certificate ID. |
| -domainId | String | domain-123456 | The domain name ID. |
| -certType | Integer | 1 | The certificate type. |
| -SN | String | SN12345678 | The serial number. |

#### CreateCertificate

Creates a certificate.

**Request headers**

This operation uses common request headers and no special request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| certificateI d | Strin g | Body | No | cert-987654 | The certificate ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| certificates | Strin g | Body | No | cert1,cert2 | The list of certificates. |
| privateKey | Strin g | Body | No | -----BEGIN PRIVATE KEY---- - | The private key. |
| certificate Name | Strin g | Body | No | MyCert | The certificate name. |

| certType | Integ er | Body | No | 1 | The certificate type. |
|---|---|---|---|---|---|
| isImport | Bool ean | Body | No | false | Specifies whether to import the certificate. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | String | {} | The data. |

#### ModifyCertificate

Modifies a certificate.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| certificateI d | Strin g | Body | No | cert-987654 | The certificate ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |
| certificates | Strin g | Body | No | cert1,cert2 | The list of certificates. |
| privateKey | Strin g | Body | No | -----BEGIN PRIVATE KEY---- - | The private key. |

| certificate Name | Strin g | Body | No | MyCert | The certificate name. |
|---|---|---|---|---|---|
| certType | Integ er | Body | No | 1 | The certificate type. |
| isImport | Bool ean | Body | No | false | Specifies whether to import the certificate. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data. |

#### DeleteCertificate

Deletes a certificate.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| certificateI d | Strin g | Body | No | cert-987654 | The certificate ID. |
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | Integer | 200 | The response code. |
|---|---|---|---|
| msg | String | The operation was successful. | The message. |
| data | String | {} | The data |

### Other

#### GetTotalityInfo

This operation queries summary information.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | No | i-c0a81bb16a1524a17 | The gateway instance ID. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful | The message. |
| data | Struct | {} | The data. |
| -routeTotal | Integer | 150 | The number of routes. |
| -serverCount | Integer | 5 | The number of servers. |

| - interfaceCount | Integer | 50 | The number of interfaces. |
|---|---|---|---|
| - todayRequest Count | Integer | 15000 | The number of requests today. |
| - portalAppTotal | Integer | 50 | The total number of portal applications. |
| -backAppTotal | Integer | 10 | The total number of backend applications. |
| - mcpServerCou nt | Integer | 3 | The number of MCP servers. |
| -strategyCount | Integer | 5 | The number of policies. |

#### GetSettings

Queries system settings.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| brokerEngi neType | Strin g | Body | No | RocketMQ | The type of the message engine. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| msg | String | Operation successful. | The message |
| data | Struct | {} | The data |

| Developer Guide·A | PI Gateway |   | API Gatewa |
|---|---|---|---|

| - supportDeploy Modes | String | [] | A list of supported deployment modes. |
|---|---|---|---|
| -licenseInfoList | Array | [] | A list of license information. |
| --region | String | cn-hangzhou | The region. |
| --vcpuCount | Integer | 4 | The number of virtual CPU cores. |
| --upLimitNum | Integer | 10000 | The upper limit. |
| --routeCount | Integer | 25 | The number of routes. |
| --aiProxyCount | Integer | 10 | The number of AI proxies. |
| --percentage | Float | 85.5 | The percentage. |
| --warn | Boolean | false | Indicates whether a warning is reported. |
| --error | Boolean | false | Indicates whether an error is reported. |
| - capacityPlatfor mEnable | Boolean | true | Indicates whether the capacity platform is enabled. |
| -licenseEnable | Boolean | true | Indicates whether the license is enabled. |
| - customPluginE nable | Boolean | true | Indicates whether custom plugins are enabled. |

#### GetSlsStatistics

Queries statistics information from Simple Log Service (SLS).

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| body | Strin g | Body | No | {"key":"value"} | The request body. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The response code. |
| Msg | String | Operation successful | The message |
| Data | Struct | {} | The data |
| -Records | Array | [] | The record list. |
| --ServiceId | String | service-123456 | The service ID. |
| -- ServiceGroupI d | String | group-001 | The service group ID. |
| --ConsumerId | String | consumer-123 | The consumer ID. |
| --Time | String | 2024-10-14 14:00:00 | The time. |
| --InputToken | Long | 1024 | The number of input tokens. |
| --OutputToken | Long | 2048 | The number of output tokens. |
| -- TotalRequestC ount | Long | 500000 | The total number of requests. |
| -- FailedRequest Count | Long | 150 | The number of failed requests. |

| -Total | Long | 1000 | The total number of entries. |
|---|---|---|---|
| -Current | Long | 1 | The current page number. |
| -Size | Long | 100 | The size |
