---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Alibaba Cloud DNS Developer Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 56
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Alibaba Cloud DNS Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Alibaba%20Cloud%20DNS%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Alibaba Cloud DNS Developer Guide 20220928

## Table of Contents

- 1 ASAPI Developer Guide
  - 1.1 Preparations
    - 1.1.1 Log on to the API Tool console
    - 1.1.2 View information about API operations
    - 1.1.3 Obtain an AccessKey pair
    - 1.1.4 Obtain common header parameters
    - 1.1.5 Obtain an STS AccessKey pair
  - 1.2 Use POP to make API calls
    - 1.2.1 Preparations
    - 1.2.2 SDK for Java
    - 1.2.3 SDK for Go
    - 1.2.4 SDK for Python
  - 1.3 Use ASAPI to make API calls
    - 1.3.1 ASAPI overview
    - 1.3.2 Generate an endpoint for ASAPI
    - 1.3.3 Obtain Apsara Stack SDKs
    - 1.3.4 Common request parameters
    - 1.3.5 SDK description
      - 1.3.5.1 SDK for Java
      - 1.3.5.2 SDK for Python
      - 1.3.5.3 SDK for Node.js
    - 1.3.6 HTTP requests
      - 1.3.6.1 Overview
      - 1.3.6.2 Request structure
      - 1.3.6.3 Request signatures
      - 1.3.6.4 Responses
- 2 API Reference
  - 2.1 Overview
    - 2.1.1 Calling methods
    - 2.1.2 Supported formats
    - 2.1.3 Instructions
    - 2.1.4 Time format
  - 2.2 List of operations by function
  - 2.3 Prerequisites
    - 2.3.1 Obtain an AccessKey pair
    - 2.3.2 Obtain an endpoint
  - 2.4 SDK example
    - 2.4.1 Create a client
    - 2.4.2 Obtain global authoritative zones
    - 2.4.3 Obtain global authoritative RRSets
    - 2.4.4 Add global RRSets
    - 2.4.5 Delete global RRSets
    - 2.4.6 Update global RRSets
    - 2.4.7 Configure descriptions for global RRSets

## 1 ASAPI Developer Guide

### 1.1 Preparations

#### 1.1.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click Log On.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding operations
in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator: a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click Log On. c. Enter a six-digit MFA verification code and click Aut hent icat e. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click Aut hent icat e.

> Not e For more information, see the Bind a virtual MFA device to enable MFA topic in A psara Uni-manager Management Console User Guide.

5. In the top navigation bar, choose Product s > Ot hers > API T ool.

#### 1.1.2 View information about API operations

This topic describes how to view information about API operations. Before you use SDKs, obtain service names, API operation names, and API operation versions. Context The API operations on the API Directory page are only for reference. For information about how to call API operations, see developer guides of the corresponding cloud services. If the information on the API Directory page is inconsistent with that in the developer guide of the corresponding cloud service, the information in the developer guide prevails. Procedure
1. Go to the API Tool console. For more information, see Log on to the API Tool console.
2. In the left-side navigation pane, click API Direct ory.
3. On the API Direct ory page, select the desired service from the drop-down list, enter a keyword of
an API operation name in the search box, and then click the search icon.
4. Then, you can view the service name, API operation name, and API operation version.

#### 1.1.3 Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. AccessKey pairs are used to implement symmetric encryption to verify the identity of requesters. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. This topic describes how to obtain an AccessKey pair. Prerequisites An account that assumes the operations administrator or level-1 organization administrator role is obtained. Only an operations administrator or a level-1 organization administrator can obtain an AccessKey pair of the organization. Context AccessKey supports the following authorization methods: Use RAM to authorize the AccessKey ID and AccessKey secret to third-party requesters. Use STS to authorize the AccessKey ID, AccessKey secret, and security token to third-party requesters. This topic describes how to obtain an AccessKey pair authorized by RAM. For more information about how to obtain an AccessKey pair authorized by STS, see Obtain an STS AccessKey pair. We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions can occur.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region, such as cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For information about how to obtain an organization ID, see the "GetOrganizationList" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance on which to perform operations. For example, you can query the ID of an Elastic Compute Service (ECS) instance from the ECS instance list. |

> **Warning:** The AccessKey pair of a personal account is managed and controlled by the permission system of the Apsara Uni-manage Management Console. If you need to obtain the AccessKey pair of an account that has permissions on an organization, make sure that your operation is allowed by an administrator. This ensures security. The account that has permissions on an organization is a privileged account.

Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and choose
User Inf ormat ion from the shortcut menu.
3. In the Apsara St ack AccessKey Pair section, obtain the AccessKey pair.

> Not e The AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide you with full permissions on Apsara Stack resources. You must keep the AccessKey pair confidential.

Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Organizat ions.
4. In the organization navigation tree, click the name of the level-1 organization for which you want
to obtain AccessKey pairs.
5. Click Management AccessKey on the right side of the page.
6. In the AccessKey message, view the AccessKey pair of the organization.

#### 1.1.4 Obtain common header parameters

You must provide multiple header parameters when you call API operations. This topic describes how to obtain common header parameters. Some response parameters are also explained. Query a region ID
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Regions.
4. Click the name of the organization that you want to view.
5. View the region ID in the Regions window on the right.
Obtain an organization ID You can call the API operation to obtain the organization ID. For more information about how to obtain the organization ID, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide. Obtain a resource set ID You can call the API operation to obtain the resource set. For more information about how to obtain the resource set ID, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide. Obtain an instance ID You can obtain the ID of an instance in the cloud service console of the Apsara Uni-manager Management Console. This topic illustrates how to obtain the ID of an ECS instance. Perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Product s > Elast ic Comput ing > Elast ic Comput e Service.
3. In the left-side navigation pane, choose Inst ances & Images > Inst ances.
4. View the inst ance ID in the instance list.
Response parameters The following response parameter are returned by default when you call list-type API operations for cloud product resource instances.

| Paramet er | Descript ion |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

#### 1.1.5 Obtain an STS AccessKey pair

This topic describes how to use STS to make API calls. Background information Alibaba Cloud Security Token Service (STS) allows you to manage temporary credentials to your Alibaba Cloud resources. You can use STS to make API calls. Procedure
1. Obtain the `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Move the pointer over the profile picture in the upper-right corner of the page and click Personal Inf ormat ion. iii. Click View Current Role Policy. In the View Policies of Current Role dialog box, view your `RAM role` .
2. Use the following code to obtain `stsAK` , `stsSK` , and `stsToken` by using your `RAM role` .

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
     // The call source.
        asClient.setSdkSource("asapi_test");
     // Pass in the ARN.
        String assumeRole = AssumeRole(asClient, "<RAM Role>");
        JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
        JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
        // Obtain the STS triplet.
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
     // Your AccessKey ID.
        reqParams.put("AccessKeyId", <Your AccessKey ID>);
     // Your AccessKey secret.
        reqParams.put("AccessKeySecret", <Your AccessKey secret>);
        reqParams.put("roleSessionName", "AsapiStsUser");
        reqParams.put("roleArn", roleArn);
        return asClient.doRequest(endpoint, headers, reqParams);
```

`}`
3. You can use STS to make API calls. The following sample code demonstrates how to call ECS API
operations.

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
        asClient.setSdkSource("asapi_test");
  // Call ECS API operations.
        String ecsRes = DescribeZones(asClient,<stsAK>,<stsSK>,<stsToken>);
```

`}`

```
public static String DescribeZones(ASClient asClient, String stsAK, String stsSK, Strin g stsToken) {
        Map<String, String> headers = new HashMap<>();
        Map<String, Object> reqParams = new HashMap<>();
        reqParams.put("action", "DescribeZones");
        reqParams.put("Product", "Ecs");
        reqParams.put("Version", "2014-05-26");
        reqParams.put("regionId", "<your-RegionID>");
        // The STS triplet of AccessKey ID, AccessKey secret, and security token.
        reqParams.put("AccessKeyId", <stsAK>);
        reqParams.put("AccessKeySecret", <stsSK>);
        reqParams.put("SecurityToken", <stsToken>);
        return asClient.doRequest(endpoint, headers, reqParams, HttpMethod.GET);
```

`}`

### 1.2 Use POP to make API calls

#### 1.2.1 Preparations

Like in the public cloud, you can use the POP gateway to call API operations in Apsara Stack. This topic describes the preparations before you use the POP gateway to call API operations. Background information In Apsara Stack, you can use both ASAPI and POP gateways to call API operations. To use the same method and produce the same user experience as in the public cloud, we recommend that you use the POP gateway to call API operations in Apsara Stack. Obtain service endpoints To use the POP gateway to call API operations, you must use the service endpoints. You can obtain the service endpoints from Alibaba Cloud onsite O&M engineers. You can also obtain the service endpoints by yourself. The following example describes how to obtain the ECS endpoints.
1. Log on to Apsara Infrastructure Management Framework.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click O&M. iii. In the left-side navigation pane, choose Product Management > Product s. iv. In the Apsara Stack O&M section, click Apsara Inf rast ruct ure Management Framework.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for `Registration Vars of Services` and click the report name.
4. On the Regist rat ion Vars of Services page, click the
icon next to Service and search for `ECS` .
5. Find the `ecs-yaochi` service, right-click the Service Regist rat ion column, and then select Show
More from the shortcut menu. On the Det ails page, view the int ernal.openapi.endpoint value, which is the `endpoint` . Obtain common parameters You must obtain the parameters required when you use the POP gateway to call API operations, such as the organization ID, resource set ID, region ID, and instance ID. For more information, see Obtain common header parameters.

#### 1.2.2 SDK for Java

Before you use POP SDK for Java to make API calls, you must first understand the RPC and ROA styles. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. SSL certificate validation is ignored for requests over HTTPS. Call examples The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeInstances {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "<yourAccessK
eyId>", "<yourAccessSecret>");
        // Ignore SSL certificate validation.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Configure the time-out period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Set the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the parameters.
        CommonRequest request = new CommonRequest();
        // Specify the request method.
        request.setSysMethod(MethodType.POST);
        // Set the service endpoint.
        request.setSysDomain("<ecsEndpoint>");
        // Specify the version of the API operation.
        request.setSysVersion("2014-05-26");
        // Specify the name of the service that you want to access and the region where the
service resides.
        request.setSysLocationProduct("Ecs");
        // Specify the name of the API operation.
        request.setSysAction("DescribeInstances");
        // When you use the STS AccessKey ID to call RPC API operations, you must add the S
ecurityToken parameter to the header.
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");
        // Configure operation-specific parameters.
        request.putBodyParameter("PageSize", "10");
        request.putBodyParameter("PageNumber", "1");
        // Required. The call source.
```

`//`

```java
equ ed. eca souce.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. For the historical versions before Enterprise Edition V3.15.0.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. For the modify and delete operations.
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

`}` `}` `}` The following sample code provides an example on how to use the ROA style to make an API call. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016- 06-07. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "<yourAccessK
eyId>", "<yourAccessSecret>");
        // Ignore SSL certificate validation.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Configure the time-out period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Set the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
```

`g`

```java
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the parameters.
        CommonRequest request = new CommonRequest();
        // Set the request protocol to HTTPS.
        request.setSysProtocol(ProtocolType.HTTP);
        // Specify the request method.
        request.setSysMethod(MethodType.GET);
        // Set the service endpoint.
        request.setSysDomain("<crEndpoint>");
        // Specify the version of the API operation.
        request.setSysVersion("2016-06-07");
        // Configure the uriPattern parameter, which is required for the ROA style.
        request.setSysUriPattern("/namespace");
        // Specify the name of the service that you want to access and the region where the
service resides.
        request.setSysLocationProduct("cr");
        // Specify the name of the API operation.
        request.setSysAction("GetNamespaceList");
        // Required. The call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. For the historical versions before Enterprise Edition V3.15.0.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. For the modify and delete operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
        // When you use the STS AccessKey ID to call ROA API operations, you must add the x
-acs-security-token parameter to the header.
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

> Not ice
> If you send a request over HTTPS, you must enable the request to ignore SSL certificate validation.

#### 1.2.3 SDK for Go

This topic describes how to use POP SDK for Go. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Both RPC and ROA styles are supported for API calls. Call examples The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

```java
package main import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-RegionID>", "<AccessKey ID>", "<Access
Key Secret>")
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<ECSEndpoint>"
    request.Version = "2014-05-26"
    request.ApiName = "DescribeInstances"
    request.Product = "Ecs"
    // When you use the STS AccessKey ID to call RPC API operations, you must add the Secur
ityToken parameter to the header.
    // request.QueryParams["SecurityToken"]="<your-SecurityToken>"
    // Required. The call source.
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. For the historical versions before Enterprise Edition V3.15.0.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource set ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
    // Optional. For the modify and delete operations.
    // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}` The following sample code provides an example on how to use the ROA style to make an API call. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016- 06-07. The following sample code shows how to call API operations:

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
    client, err := sdk.NewClientWithAccessKey("<your-regionid>", "<yourAccessKeyId>", "<you
rAccessSecret>")
 request := requests.NewCommonRequest()
 request.Method = "GET"
 request.Domain = "<crEndpoint>"
 request.Version = "2016-06-07"
 request.ApiName = "GetNamespaceList"
 request.Product = "cr"
 request.PathPattern = "/namespace"
 // When you use the STS AccessKey ID to call ROA API operations, you must add the x-acs-se
curity-token parameter to the header.
 // request.Headers["x-acs-security-token"] = "<your-SecurityToken>"
 // Required. The call source.
 request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. For the historical versions before Enterprise Edition V3.15.0.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource set ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
 // Optional. For the modify and delete operations.
 // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
 response, err := client.ProcessCommonRequest(request)
 if err != nil {
  panic(err)
```

`}`

```
 fmt.Print(response.GetHttpContentString())
```

`}` Configure proxies You can configure proxies in one of the following ways when you call API operations: Configure proxies as environment variables. Set the HTTP_PROXY and HTTPS_PROXY environment variables, or set the NO_PROXY environment variable. Sample code:

```java
import (
    "os"
```

`)`

```
func main(){
 os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // Configure the HTTP_PROXY environment v
ariable.
 os.Setenv("HTTPS_PROXY", "https://x.x.x.x:xxxx") // Configure the HTTPS_PROXY environmen
t variable.
```

`}` Configure proxies on the client. Sample code:

```
// The proxies that are configured on the client take precedence over those that are conf igured by using environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Configure the HTTP proxy. client.GetHttpProxy() // Query the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Configure the HTTPS proxy. client.GetHttpsProxy() // Query the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Configure the proxy whitelist. client.GetNoProxy() // Query the proxy whitelist.
```

#### 1.2.4 SDK for Python

This topic describes how to use POP SDK for Python. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. Sample code:

```java
from aliyunsdkcore.client import AcsClient import os from aliyunsdkcore.request import CommonRequest
# Create an AcsClient object.
client = AcsClient(
    "<AccessKey ID>",
    "<AccessKey Secret>",
    "<your-RegionID>",
timeot1000
#Setthetimeotperiod
```

```
    timeout=1000,  # Set the timeout period.
    verify=False, # Ignore certificate validation. or verify='<The location where the certi
ficate is stored.>'
```

);

```python
# Set the following parameters for the HTTPS request protocol:
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def hello_ecs_instance():
    # Create a request and set the parameters.
    request = CommonRequest()
    # When you use the STS AccessKey ID to call RPC API operations, you must add the Securi
tyToken parameter to the header.
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-SecurityToken>"};
    params = {"PageSize":"10","PageNumber":"1"};
    request.set_body_params(params)
    headers = {
        # Required. The call source.
        "x-acs-caller-sdk-source":"ApiTestDemo",
        # Optional. For the historical versions before Enterprise Edition V3.15.0.
        "x-acs-regionid":"<your-RegionID>",
        # Optional. The resource set ID.
        "x-acs-resourcegroupid":"<your-ResourceGroupID>",
        # Required. The organization ID.
        "x-acs-organizationid":"<your-OrganizationID>"
        # Optional. For the modify and delete operations.
        # "x-acs-instanceid":"<your-InstanceID>"
```

`}`

```python
    request.set_headers(headers)
    request.set_version("2014-05-26")
    request.set_action_name("DescribeInstances")
    request.set_endpoint("<ecsEndpoint>") // Replace ecsEndpoint with the real endpoint.
    request.set_product("Ecs")
    request.set_method("POST")
    # Initiate the API request and obtain the response.
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    hello_ecs_instance()
```

Configure proxies You can configure HTTP_PROXY and HTTPS_PROXY environment variables when you call API operations. Sample code:

```bash
# Configure the HTTPS proxy.
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# Configure the HTTP proxy.
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

### 1.3 Use ASAPI to make API calls

#### 1.3.1 ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage organizations, users, roles, resource sets, and logon policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Uni-manager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Uni-manager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide.

> Not e If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

#### 1.3.2 Generate an endpoint for ASAPI

This topic describes three methods used to generate an endpoint for Apsara Stack API (ASAPI). Method 1: Use Registration Vars of Services to generate an endpoint
1. Log on to Apsara Infrastructure Management Framework.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click O&M. iii. In the left-side navigation pane, choose Product Management > Product s. iv. In the Apsara Stack O&M section, click Apsara Inf rast ruct ure Management Framework.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for `Registration Vars of Services` and click the report name.
4. On the Regist rat ion Vars of Services page, click the
icon next to Service and search for `asapi` .
5. Find the asapi service, right-click in the Service Regist rat ion column, and then select Show More
from the shortcut menu. In the Det ails dialog box, obtain the value of asapi.public.endpoint .
6. Generate an endpoint for ASAPI based on the following format:

```
https://<asapi.public.endpoint>/asapi/v3
```

Method 2: Use cluster resources to generate an endpoint
1. Log on to Apsara Infrastructure Management Framework.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click O&M. iii. In the left-side navigation pane, choose Product Management > Product s. iv. In the Apsara Stack O&M section, click Apsara Inf rast ruct ure Management Framework.
2. Go to the cluster operations page.
i. In the left-side navigation pane, choose Operations > Cluster Operations. ii. In the Clust er search box, enter `ascm` . iii. Find the cluster that you want to manage and click Operat ions in the Act ions column.
3. Obtain the value of the domain parameter.
i. Click the Cluster Resources tab. ii. In the Name field, search for `asapi_dns_public` . iii. Click Det ails in the Applicat ion Paramet er column. In the Applicat ion Paramet er message, obtain the value of the domain parameter.
4. Generate an endpoint for ASAPI based on the following format:

```
https://<domain>/asapi/v3
```

Method 3: Concatenate strings to generate an endpoint You can also concatenate strings to generate an endpoint based on the following format:

```
https://public.asapi.<region>.<internet-domain>/asapi/v3
```

> Not e

1. Replace <region> with your actual region ID. For information about how to query a region ID,
see Query a region ID.
2. Replace <internet-domain> with the root domain of your Apsara Stack service. To obtain the
root domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internetdomain parameter instead of the intranet-domain parameter. If the region value is `cn-****-****-d01` and the int ernet -domain value is `inter.****.****.com` , the following endpoint can be generated: An example of a complete endpoint:

```
https://public.asapi.cn-****-****-d01.inter.****.****.com/asapi/v3
```

#### 1.3.3 Obtain Apsara Stack SDKs

Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use the ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. You can go to Apsara Stack documentation and download the Apsara Stack SDKs in the Ot her Resources section at the lower part of the page.

#### 1.3.4 Common request parameters

Common request parameters must be included in all API requests. Sample common parameters The following table describes the common parameters that are used when you call API operations supported by Apsara Stack API (ASAPI).

| Paramet er | T ype | Required | Descript ion |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. For more information, see View the information about API operations. |
| Product | String | Yes | The name of the service. |
| Version | String | Yes | The version of the API operation. For more information, see View information about API operations. |
| RegionId | String | Yes | The ID of the region. For more informatio, see Query a region ID. |
| AccessKeyId | String | Yes | The AccessKey ID used to connect to the service. For more information, see Obtain an AccessKey pair. |
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Valid values: HMAC- SHA1 and HMAC- SHA256. |

| Paramet er | T ype | Required | Descript ion |
|---|---|---|---|
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Valid values: 1.0 and 2.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2018-01-01T12:00:00Z. |
| Format | String | Yes | The format in which to return the response. Set the value to JSON. |

> Not e

```
The Signature , SignatureMethod , SignatureVersion , SignatureNonce , Timestamp ,
```

> and `Format` parameters are encapsulated into Apsara Stack SDK. You do not need to configure
> these parameters.

#### 1.3.5 SDK description

##### 1.3.5.1 SDK for Java

This topic describes how to obtain and use Apsara Stack SDK for Java to call API operations. Prerequisites An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. You can obtain and view your AccessKey pair in the Apsara Uni-manager Management Console. For more information, see Obtain an AccessKey pair. The endpoint of the ASAPI is obtained. For more information, see Generate an endpoint for ASAPI. Apsara Stack SDK for Java 1.8 or later is installed. Background information The help center of Apsara Stack provides Maven dependencies and JAR files for Apsara Stack SDK for Java. You can write code to use Apsara Stack SDK for Java to call API operations. In this example, the Windows 10 64-bit OS and IntelliJ IDEA are used. Procedure
1. Use one of the following methods to configure Maven in IntelliJ IDEA. Maven is a tool used for
project management. Use Maven that is integrated in IntelliJ IDEA. Download Maven based on the OS that you are using from the official website and configure Maven. For more information, see Download Maven.
2. Obtain the Maven dependencies for Apsara Stack SDK for Java from the official website.
3. Use one of the following methods to create a Maven project:
Method 1: Create a Maven project in IntelliJ IDEA. Method 2: Convert an existing project to a Maven project. a. Right-click the project that you want to convert and select Add Framework Support .... b. Select Maven and click OK.
4. Create a folder named libs in the root directory of the project. Then, add the JAR file of Apsara
Stack SDK for Java to the libs folder, as shown in the following figure.
5. Add the dependencies of Apsara Stack SDK for Java to the pom.xml file in the project directory.

```xml
<dependencies>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>asapi</artifactId>
        <version>1.0.6.4-RELEASE</version>
        <scope>system</scope>
        <systemPath>${project.basedir}/libs/asapi-1.0.6.4-RELEASE.jar</systemPath>
    </dependency>
  <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>alicrypto-java-aliyun</artifactId>
    <version>1.0.4</version>
    <systemPath>${project.basedir}/libs/alicrypto-java-aliyun-1.0.4.jar</systemPath>
  </dependency>
  <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>gmsse</artifactId>
    <version>1.1.0</version>
    <systemPath>${project.basedir}/libs/gmsse-1.1.0.jar</systemPath>
  </dependency>
    <dependency>
    <groupId>org.apache.httpcomponents</groupId>
    <artifactId>httpclient</artifactId>
    <version>4.5.7</version>
    <systemPath>${project.basedir}/libs/httpclient-4.5.7.jar</systemPath>
  </dependency>
</dependencies>
```

> Not e Replace `1.0.6.4-RELEASE` with the actual version of Apsara Stack SDK for Java.

6. On the right side of IntelliJ IDEA, view information in the Maven section.
If the information in the following figure appears, the dependencies are added. Use Apsara Stack SDK for Java You can use the GET or POST method to call API operations provided by ASAPI. The following sample code shows how to call API operations:

```java
// 1. Create a connection to an ASClient object. ASClient client = new ASClient(); // 2. Configure the identifier of the requester. This parameter is required and used only f or identification. You can set this parameter to a random value. client.setSdkSource("<The identifier of the requester>"); Map<String, Object> parameters = new HashMap<String, Object>(); // 3. Configure the parameters for authorization. The parameter values vary based on your e nvironment. // The AccessKey ID of your Apsara Stack tenant account. parameters.put("AccessKeyId","<AccessKey ID>"); // The AccessKey secret of your Apsara Stack tenant account. parameters.put("AccessKeySecret", "<AccessKey Secret>"); // The ID of the region. parameters.put("RegionId", "<your RegionID>"); // 4. Configure parameters for an API call. In this example, the Product, Action, and Versi on parameters are configured. parameters.put("Product", "<The name of the service>"); parameters.put("Action", "<The name of the API operation>"); parameters.put("Version", "<The version of the API operation>"); // When you use the STS AccessKey ID to call RPC API operations, you must add the SecurityT oken parameter to the header. // parameters.put("SecurityToken", "<your-securitytoken>"); // When you use the STS AccessKey ID to call ROA API operations, you must add the x-acs-sec urity-token parameter to the header. // headers.put("x-acs-security-token", "<your-securitytoken>"); // 5. Configure operation-specific parameters. parameters.put("<The name of the operation-specific parameter>", "<The value of the operati on-specific parameter>"); // 6. Configure request headers and the encryption method for the signature string. Valid v alues of the SignatureMethod parameter: HMAC-SHA1 and HMAC-SHA256. By default, HMAC-SHA256 is used. Map<String, String> headers = new HashMap<String, String>(); //headers.put("SignatureMethod", "HMAC-SHA1"); headers.put("x-acs-regionid", "<your-regionid>"); headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>"); headers.put("x-acs-organizationid", "<your-organizationid>"); headers.put("x-acs-instanceid", "<your-instanceid>"); // 7. Make an API call. We recommend that you use the doPost() method. // Configure the time-out period for a connection. //client.setConnectTimeout(10000); // Configure the time-out period for a request. // client.setSocketTimeout(10000); String result = client.doPost(endpoint, headers, parameters); System.out.println(result);
```

Configure proxies If you need to use a proxy to make API calls, use the following sample code to configure the proxy:

```
Cloud cloud = new Cloud(); // Configure the IP address of the proxy. cloud.setConfig("proxy_host", "<IP>"); // Configure the port used by the proxy. cloud.setConfig("proxy_port", "<Port>"); Create a connection to an ASClient object. ASClient client = new ASClient(cloud);
```

Header parameters

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Query a region ID. |
| x-acs-organizat ionid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-inst anceid | The ID of the instance to which you make API calls. |

##### 1.3.5.2 SDK for Python

This topic describes how to obtain and use Apsara Stack SDK for Python to call API operations. Preparations An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. The endpoint of ASAPI is obtained. For more information, see Generate an endpoint for ASAPI. Install Apsara Stack SDK for Python
1. Download the required version of Apsara Stack SDK for Python. For more information, see Obtain
Apsara Stack SDKs.
2. Upload the compressed file of Apsara Stack SDK for Python to the host from which you want to
send API requests and extract the file. Then, run the following code in the directory of the extracted files to install Apsara Stack SDK for Python:

```bash
# Install Apsara Stack SDK for Python 2.x.
pip install aliyun-python2-sdk-asapi-2.4.7.tar.gz
# Install Apsara Stack SDK for Python 3.x.
pip3 install aliyun-python3-sdk-asapi-2.4.7.tar.gz
```

> Not e
> Replace `2.4.7` with the actual version of Apsara Stack SDK for Python.

Sample requests You can use the GET or POST method to call API operations provided by ASAPI.

```python
# 1. Import dependencies.
   from aliyunsdkasapi.ASClient import ASClient
   from aliyunsdkasapi.AsapiRequest import AsapiRequest
   if __name__ == '__main__':
    # 2. Create a request. The Product parameter specifies the name of the service. The Ver
sion parameter specifies the version of the API operation. The Action parameter specifies t he operation that you want to perform. The asapi-endpoint parameter specifies the endpoint of ASAPI.
    req = AsapiRequest("<Product>", "<Version>", "<Action>", "<asapi-endpoint>")
    # 3. Configure operation-specific parameters.
    req.add_body_params("<key>", "<value>")
 # When you use the STS AccessKey ID to call RPC API operations, you must add the SecurityT
oken parameter to the header.
 # req.add_body_params("SecurityToken", "<your-securitytoken>");
 # When you use the STS AccessKey ID to call ROA API operations, you must add the x-acs-sec
urity-token parameter to the header.
 # req.add_header("x-acs-security-token", "<your-securitytoken>");
    # 4. Configure request headers.
    req.add_header("x-acs-resourcegroupid", "<your-resourcegroupid>");
    req.add_header("x-acs-organizationid", "<your-organizationid>");
    req.add_header("x-acs-regionid", "<your-regionid>");
    req.add_header("x-acs-instanceid", "<your-instanceid>");
    # 5. Configure a request method.
    req.set_method("POST")
    # 6. Configure initialization parameters for an ASClient object. The parameter values v
ary based on your environment. The timeout parameter specifies the time-out period for a re quest. The cert_file parameter specifies the certificate. The verify parameter specifies wh ether to verify the certificate.
    as_client = ASClient("<accesskeyid>", "<accesskeysecret>", "<regionid>",timeout=1000,
            cert_file=None,
            verify=False)
    # Configure the identifier of the requester. This parameter is required and used only f
or identification. You can set this parameter to a random value.
    as_client.setSdkSource("<The identifier of the requester>")
    response = as_client.do_request(req)
    print(response)
```

Header paramet ers

| Paramet er | Descript ion |
|---|---|
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Query a region ID. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. |

Configure proxies Perform the following steps to configure a proxy:
1. Import OS dependencies.

```java
import os
```

2. Configure one or more proxies.

```bash
# Before you make an API call, configure one or more proxies.
os.environ['http_proxy'] = "http://x.x.x.x:xxxx" os.environ['https_proxy'] = "https://x.x.x.x:xxxx"
```

##### 1.3.5.3 SDK for Node.js

This topic describes how to obtain and use Apsara Stack SDK for Node.js to call API operations. Preparations An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. The endpoint of Apsara Stack API (ASAPI) is obtained. For more information, see Generate an endpoint for the ASAPI. For more information about how to obtain the region ID, see Obtain the endpoint of ASAPI. Add dependencies Run the following command to install Apsara Stack SDK for Node.js:

```
 tnpm i @ali/asapi-nodejs-sdk@0.0.33 --save
```

Use Apsara Stack SDK for Node.js The following sample code shows how to use Apsara Stack SDK for Node.js to make API calls:

```
// 1. Import the dependencies of Apsara Stack SDK for Node.js. const Controller = require('egg').Controller; const ASAPIClient = require('@ali/asapi-nodejs-sdk'); // 2. Configure the parameters. const cnofig = {
    API_GATEWAY: '<The endpoint of ASAPI>',
    regionId: '<The ID of the region in which the Apsara Stack service is deployed>',
    accessKeyId: '<The AccessKey ID of your Apsara Stack tenant account>',
    accessKeySecret: '<The AccessKey secret of your Apsara Stack tenant account>'
```

};

```json
// 3. Initialize a client for API calls. const AsapiClient = new ASAPIClient(cnofig, this.ctx); // 4. Configure request parameters. const params = {
    "Action": "<The name of the API operation>",
    "Product": "<The name of the service that provides the API operation>",
    "Version": "<The version of the API operation>",
    "regionId": '<The ID of the region in which the Apsara Stack service is deployed>',
    // When you use the STS AccessKey ID to call RPC API operations, you must add the Secur
ityToken parameter to the header.
    // "SecurityToken": "<your-securitytoken>",
      "<The name of the operation-specific parameter required by the API operation>": "<The
value of the operation-specific parameter>"
```

`}`

```
// 5. Configure request headers. // When you use the STS AccessKey ID to call ROA API operations, you must add the x-acs-sec urity-token parameter to the header. // AsapiClient.addHeader("x-acs-security-token", "<your-securitytoken>") AsapiClient.addHeader('x-acs-caller-sdk-source', '<The identifier of the requester>') AsapiClient.addHeader('x-acs-roleid', '<The ID of the role>') AsapiClient.addHeader('x-acs-userid', '<The ID of the user>') AsapiClient.addHeader('x-acs-organizationid', '<your-organizationid>') AsapiClient.addHeadert("x-acs-regionid", "<your-regionid>"); AsapiClient.addHeader("x-acs-resourcegroupid", "<your-resourcegroupid>"); AsapiClient.addHeader("x-acs-instanceid", "<your-instanceid>"); // 6. Make an API call and obtain the response. try {
  const res = await AsapiClient.doRequest(cnofig.API_GATEWAY, params, {
    method: 'POST', // The request method.
    formatParams: false, // Specifies whether to format parameters and capitalize the first
letter of each parameter.
    enableProxy: true, // Specifies whether to configure a proxy.
    proxy: 'http://x.x.x.x:xxxx',
    timeout: 10000, // The time-out period.
  // ca: , // The certificate issued by a certificate authority (CA). For more information,
visit https://nodejs.org/api/https.html#https_https_request_options_callback.
```

`})`

```
  console.log(res)
} catch (e) {
  console.log(e)
```

`}` Disable certificate validation The following sample code shows how to disable certificate validation:

```
Configure the environment variable. NODE_TLS_REJECT_UNAUTHORIZED=0
```

Request headers

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Query a region ID. |
| x-acs-organizat ionid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-inst anceid | The ID of the instance on which you want to perform operations. |
| x-acs-caller-sdk-source | The custom name of the requester or the system. This parameter is used to identify the source of the API request. |
| x-acs-roleid | The ID of the role. |
| x-acs-userid | The ID of the user. |

#### 1.3.6 HTTP requests

##### 1.3.6.1 Overview

This topic describes how to make API requests and is intended for users who use API URLs to initiate HTTP GET requests. If you are using an SDK to initiate requests, you can skip this topic. The request URL consists of different parameters and has a fixed syntax. The URL contains common request parameters, your signature, and operation-specific parameters. Sample request URLs are provided for each API operation. These URLs are not encoded to make them easy to read. Before you make a request, you must encode the request URL. After the authentication process is complete based on your signature, the results are returned to you. Response parameters are returned if the call is successful, whereas an error message is returned if the call fails. You can troubleshoot issues based on the error message.

##### 1.3.6.2 Request structure

You can use API URLs to initiate HTTP GET requests. Each URL must include request parameters. This topic describes the syntax of HTTP GET requests and provides the endpoint of ASAPI. Sample request GetOrganizationList is used in the following unencoded URL request:

```
https://public.asapi.aliyuns.com/asapi/v3?Action=GetOrganizationList&Product=ascm&Version=2 019-05-10&Id=<Organization ID>&<Common parameters>
```

`https` : the protocol used to transmit the request. `public.asapi.aliyuns.com/asapi/v3` : the endpoint of ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` : the API operation. `Id` : the ID of the organization. `<Common request parameters>` : common parameters specified in the system. Protocols ASAPI supports only the HTTP request protocol. Endpoints For more information about how to obtain the endpoint of ASAPI, see Generate an endpoint for ASAPI. You must use the `Action, Product, and Version` parameters to specify an API operation. For example, you can set `Action to GetOrganizationList, Product to ascm, and Version to 2019-05-10` . You must also specify other operation-specific request parameters and common request parameters. For more information, see Common request parameters.

##### 1.3.6.3 Request signatures

This topic describes how to sign HTTP API requests. ASAPI uses the request signature to verify the identity of the request sender. ASAPI implements symmetric encryption by using an AccessKey pair to verify the identity of the request sender.

> Not e
> An AccessKey pair consists of an AccessKey ID and an AccessKey secret, which are issued to each user or organization in the Apsara Uni-manager Management Console.
> The AccessKey ID is used to verify identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must keep your AccessKey secret confidential.
> ASAPI provides SDKs for Node.js, Python, and Java to facilitate complex signature calculation. For more information, see Obtain the core package for ASAPI.

Step 1: Create a canonicalized query string
1. Arrange the request parameters in alphabetical order, including all common and operation-specific
parameters except the `Signature` parameter.

> Not e
> If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?).

2. Encode the request parameters and their values in UTF-8 based on RFC 3986. The following rules
apply in the encoding process: Letters, digits, and special characters such as hyphens ( `-` ), underscores ( `_` ), and periods ( `.` ) do not need to be encoded. Other characters must be percent encoded in the %XY format. `XY` represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks ( `"` ) are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20 . Do not encode spaces as plus signs ( `+` ). This encoding method is similar to but different from the `application/x-www-form-urlencoded` MIME encoding algorithm. If you use `java.net.URLEncoder` from the Java standard library, use `percentEncode` to encode request parameters and their values. In the encoded query string, replace the plus signs ( `+` ) with %20 , asterisks ( `*` ) with %2A , and %7E with tildes ( ~ ). This way, you can obtain an encoded string that matches the preceding encoding rules.

```java
private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException
```

`{`

```
    return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").rep
lace("*", "%2A").replace("%7E", "~") : null;
```

`}`
3. Use equal signs ( `=` ) to connect the encoded request parameters and their values.
4. Use ampersands ( `&` ) to connect the encoded request parameters. These parameters must be
arranged in the same order as those in Step 1. Then, a canonicalized query string that follows the request structure is obtained. For more information, see Request structure. Step 2: Create a string-to-sign
1. Create a `string-to-sign` . You can also use `percentEncode` to encode the canonicalized query
string created in Step 1 based on the following rules:

```
StringToSign=
    HTTPMethod + "&" + //HTTPMethod: the HTTP method that is used to send a request, su
ch as GET.
    percentEncode("/") + "&" + //percentEncode("/"): Encode the forward slash (/) in UT
F-8 as %2F.
    percentEncode(CanonicalizedQueryString) // Encode the canonicalized query string cr
eated in Step 1.
```

2. Calculate the RFC 2104-compliant HMAC-SHA1 or HMAC-256 value of `StringToSign` . In the
following example, Java Base64 is used:

```
String signature = Base64.getEncoder().encodeToString(signData);
```

> Not e
> When you calculate the signature, the key value specified by RFC 2104 is your
> `AccessKey secret` plus an ampersand (&), which has an ASCII value of 38. For more

information, see Obtain an AccessKey pair.
3. Encode the `Signature` parameter based on RFC 3986 and add it to the canonicalized query
string. Example 1: Concat enat e paramet ers `GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid and `AccessKeySecret` is set to testsecret. Perform the following operations:
1. Construct a canonicalized query string.

```
https://public.asapi.aliyuns.com/asapi/v3/?AccessKeyId=testid&Action=GetOrganizationLis t&Format=JSON&Id=1&Product=ascm&RegionId=cn-region-test&SignatureMethod=HMAC-SHA1&Signa tureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f39d2&SignatureVersion=1.0&Timestamp=2020-09-1 5T08%3A50%3A40Z&Version=2019-05-10
```

2. Create a `string-to-sign` .

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DGetOrganizationList%26Format%3DJSON%26Id%3D1%26 Product%3Dascm%26RegionId%3Dcn-region-test%26SignatureMethod%3DHMAC-SHA1%26SignatureNon ce%3D43967c6e-e3ad-44fa-b06b-fcf3db5f39d2%26SignatureVersion%3D1.0%26Timestamp%3D2020-0 9-15T08%253A50%253A40Z%26Version%3D2019-05-10
```

3. Calculate the signature.
Calculate the signature. The key value used for calculation is `testsecret&` because `AccessKeySecret` is set to testsecret. The calculated signature is `OLeaidS1JvxuMvnyHOwuJ+uX5qY=` . Java Base64 is used in the following sample code:

```
 String signature = Base64.getEncoder().encodeToString(signData);  Encode
```

`Signature=hvqv9Ll5RE6kQ4YsQXFAf9VuRIY=` based on RFC 3986 and add it to the canonicalized query string.

```
https://public.asapi.aliyuns.com/asapi/v3/?AccessKeyId=testid&Action=GetOrganizationLis t&Format=JSON&Id=1&Product=ascm&RegionId=cn-region-test&SignatureMethod=HMAC-SHA1&Signa tureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f39d2&SignatureVersion=1.0&Timestamp=2020-09-1 5T08%3A50%3A40Z&Version=2019-05-10
```

You can use browsers or tools such as cURL and Wget to initiate an HTTP request for calling the `DescribeRegions` operation to query the Alibaba Cloud region list. Example 2: Use t he st andard library of t he programming language `GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid, `AccessKeySecret` is set to testsecret, and all request parameters are stored in a Java `Map<String, String>` object.
1. Predefine an encoding method.

```java
private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException {
        return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").r
eplace("*", "%2A").replace("%7E", "~") : null;
```

`}`
2. Predefine the time format for the `Timestamp` parameter. Specify the `Timestamp` parameter in
the ISO 8601 format. The time must be in UTC+0.

```java
private static final String ISO8601_DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ss'Z'"; private static String formatIso8601Date(Date date) {
    SimpleDateFormat df = new SimpleDateFormat(ISO8601_DATE_FORMAT);
    df.setTimeZone(new SimpleTimeZone(0, "GMT"));
    return df.format(date);
```

`}`
3. Create a request string.

```
final String HTTP_METHOD = "GET"; Map parameters = new HashMap(); // Specify request parameters. parameters.put("Product", "ascm"); parameters.put("Action", "GetOrganizationList"); parameters.put("Version", "2019-05-10"); parameters.put("AccessKeyId", "testid"); parameters.put("RegionId", "cn-region-test"); parameters.put("Timestamp", formatIso8601Date(new Date())); parameters.put("SignatureMethod", "HMAC-SHA1"); parameters.put("SignatureVersion", "1.0"); parameters.put("SignatureNonce", UUID.randomUUID().toString()); parameters.put("Format", "JSON"); parameters.put("Id", "1"); // Arrange request parameters. String[] sortedKeys = parameters.keySet().toArray(new String[]{}); Arrays.sort(sortedKeys); final String SEPARATOR = "&"; // Create a string-to-sign. StringBuilder stringToSign = new StringBuilder(); stringToSign.append(HTTP_METHOD).append(SEPARATOR); stringToSign.append(percentEncode("/")).append(SEPARATOR); StringBuilder canonicalizedQueryString = new StringBuilder(); for(String key : sortedKeys) {
    // Encode the key and the value.
    canonicalizedQueryString.append("&")
    .append(percentEncode(key)).append("=")
    .append(percentEncode(parameters.get(key)));
```

`}`

```
//Encode the canonicalized query string. stringToSign.append(percentEncode( canonicalizedQueryString.toString().substring(1)));
```

4. The signature. The key value used for calculation is `testsecret&` because `AccessKeySecret` is
set to testsecret. The calculated signature is OLeaidS1JvxuMvnyHOwuJ%2BuX5qY%3D .

```
// The following sample code shows how to calculate the signature: final String ALGORITHM = "HmacSHA1"; final String ENCODING = "UTF-8"; key = "testsecret&"; Mac mac = Mac.getInstance(ALGORITHM); mac.init(new SecretKeySpec(key.getBytes(ENCODING), ALGORITHM)); byte[] signData = mac.doFinal(stringToSign.getBytes(ENCODING)); String signature = Base64.getEncoder().encodeToString(signData);
```

Encode the Signature parameter based on RFC 3986 and add it to the canonicalized query string. The following URL is obtained:

```
https://public.asapi.aliyuns.com/asapi/v3/?AccessKeyId=testid&Action=GetOrganizationLis t&Format=JSON&Id=1&Product=ascm&RegionId=cn-region-test&SignatureMethod=HMAC-SHA1&Signa tureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f39d2&SignatureVersion=1.0&Timestamp=2020-09-1 5T08%3A50%3A40Z&Version=2019-05-10
```

5. Use browsers or tools such as cURL and Wget to initiate an HTTP request.

##### 1.3.6.4 Responses

Responses are returned only in the JSON format. If a return code is greater than or equal to 200 and less than 300, a success response is returned. Otherwise, an error response is returned. Sample success responses If a request is successful, the request ID and operation-specific parameter values are returned. For more information, see the developer guide of the corresponding Apsara Stack service.

```json
   "successResponse":true,
  "eagleEyeTraceId":"xxxxxxxxxxxxxx",
  "asapiSuccess":true,
  "code":"200",
  "cost":12,
  "asapiRequestId":"xxxxxxxxxxxxxx",
  "data":[
```

`{`

```json
      "muserId":"aliyuntest",
      "internal":false,
      "level":"0",
      "supportRegions":"cn-*",
      "personNum":100,
      "mtime":1553247962000,
      "uuid":"1",
      "parentId":0,
      "supportRegionList":[
        "cn-*"
```

`],`

```json
      "name":"root",
      "alias":"root",
      "ctime":1553247962000,
      "id":1,
      "resourceGroupNum":100,
      "cuserId":"aliyuntest"
```

`}` `],`

```json
  "requestId":"xxxxxxxxxxxxxx",
  "success":true,
  "message":"success"
```

`}` Sample error responses If a request fails, the following information is returned. For more information, see the developer guide of the corresponding Apsara Stack service. `{`

```json
    "code": "asapi.server.api.notfound",// The error code.
    "eagleEyeTraceId": "xxx-xxx-xxx-xxx", // The trace ID provided by EagleEye.
    "asapiSuccess": false, // Indicates whether the request is successful.
    "hostId": "xxxx", // The ID of the host.
    "message": "Failed to ....", // The message returned.
    "asapiErrorMessage": "Failed to ....", // The error message provided by ASAPI.
    "asapiErrorCode": "asapi.server.api.notfound" // The error code provided by ASAPI.
```

`}`

## 2 API Reference

### 2.1 Overview

#### 2.1.1 Calling methods

You can use a pair of AccessKey ID and AccessKey Secret to call API operations. You can use SDKs of different languages, or create a client based on the signature description provided by the POP gateway.

#### 2.1.2 Supported formats

AccessKey ID and AccessKey Secret of an Apsara Stack tenant account Temporary AccessKey ID and AccessKey Secret of an Apsara Stack tenant account AccessKey ID and AccessKey Secret of a RAM user account Temporary AccessKey ID and AccessKey Secret of a RAM user account

#### 2.1.3 Instructions

The AccessKey ID is used to identify users. The AccessKey Secret is used to compute the request signature.

#### 2.1.4 Time format

Unless otherwise specified, the time string is a UTC+0 time in the format of YYYY-MM-DDTHH:mm:ssZ. For example, 2018-01-16T09:00:01Z indicates 17:00:01 on January 16, 2018, in China Standard Time (UTC+8).

### 2.2 List of operations by function

DNS V2.0 provides the following API operations.

| API | Description |
|---|---|
| ObtainGlobalAuthZoneList | Obtains global authoritative zones |
| ObtainGlobalAuthRecordList | Obtains global authoritative RRSets |
| AddGlobalRrSet | Adds global RRSets |
| DeleteGlobalRrSet | Deletes global RRSets |
| UpdateGlobalRrSet | Updates global RRSets |
| RemarkGlobalRrSet | Configures descriptions for global RRSets |

### 2.3 Prerequisites

#### 2.3.1 Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain an AccessKey pair. Prerequisites Only operations administrators and level-1 organization administrators can obtain the AccessKey pair of an organization. Context We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services. When you use the AccessKey pair of a personal account, you must configure header parameters as described in the following table for access control.

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID, such as cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. |

> **Warning:** The AccessKey pairs of personal accounts are under control of the Apsara Uni- manager Management Console permission system. AccessKey pairs of organization accounts have higher permissions. For security purposes, organization operations must be approved by administrators.

Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, view your AccessKey pair.

> Not e The AccessKey pair consists of an AccessKey ID and an AccessKey secret. AccessKey pairs allow you to access Apsara Stack resources with full permissions for your account. You must keep your AccessKey pair confidential.

Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the organization navigation tree, click an organization name.
5. In the Current Organization section, click Obt ain an accesskey.
6. In the AccessKey message, view the AccessKey pair of the organization.

> Not e An AccessKey pair is automatically allocated to each level-1 organization. Subordinate organizations use the same AccessKey pair of their level-1 organization.

#### 2.3.2 Obtain an endpoint

Procedure
1. Log on to the Apsara Infrastructure Management Framework console as an administrator.
2. In the top navigation bar, choose Operat ions > Clust er Operat ions.
3. On the Clust er Operat ions page, select dnsProduct from the Project drop-down list.
4. In the Service Instances section, click Det ails in the Actions column corresponding to dnsService.
5. In the Machine Information section, click T erminal in the Actions column corresponding to a server
to go to the console.
6. Run the `sudo docker ps -l` command to obtain the ID of the current container.
7. Run the sudo docker inspect ${container id} |grep env command to obtain the endpoint of
the current environment. The endpoint is the value corresponding to pop_out_endpoint (the string starting with "api.").

### 2.4 SDK example

#### 2.4.1 Create a client

You need to specify a region ID, AccessKey ID, and AccessKey Secret to create a client. Go SDK

```
1.    if client, err := genesisdns.NewClientWithAccessKey(RegionId, AccessKey, AccessSecret
); err == nil {
2.      //Normal business logic
3.    } else {
4.      //Business logic to handle exceptions
5.    }
```

Python SDK

```
1.    from aliyunsdkcore.client import AcsClient
2.    from aliyunsdkcore.acs_exception.exceptions import ClientException
3.    from aliyunsdkcore.acs_exception.exceptions import ServerException
```

`4.` `5.`

```
6.    client = AcsClient("<access-key-id>",
7.       "<access-key-secret>",
8.       "<region-id>");
```

Java SDK

```
1.    public static void main(String[] args) {
2.         DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{secret
}");
3.         IAcsClient client = new DefaultAcsClient(profile);
4.    }
```

#### 2.4.2 Obtain global authoritative zones

Go SDK

```
1. if client, err := genesisdns.NewClientWithAccessKey("{regionid}","{ak}", "{secret}"); er
r == nil {
2.     request := genesisdns.CreateObtainGlobalAuthZoneListRequest()
3.     request.SetDomain("{endpoint}")
4.     if response, err := client.ObtainGlobalAuthZoneList(request); err == nil {
5.         fmt.Println(response.ZoneList)
6.     }
7. }
```

Python SDK

```
1. client = AcsClient("{ak}", "{secret}", "{regionid}");
```

`2.`

```
3. request = ObtainGlobalAuthZoneListRequest.ObtainGlobalAuthZoneListRequest()
4. request.set_PageSize(10)
5. region_provider.modify_point("GenesisDns", "{regionid}","{endpoint}")
6. try:
7.     response = client.do_action_with_exception(request)
8.     print(response)
9. except ServerException as e:
10.     print(e)
11. except ClientException as e:
12.     print(e)
```

Java SDK

```
1. public static void main(String[] args) {
2.     DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{secret}");
3.     IAcsClient client = new DefaultAcsClient(profile);
4.     ObtainGlobalAuthZoneListRequest request = new ObtainGlobalAuthZoneListRequest();
5.     try {
6.         request.setEndpoint("{endpoint}");
7.         request.setConnectTimeout(1000);
8.         request.setReadTimeout(1000);
9.         request.setPageSize(10);
10.         ObtainGlobalAuthZoneListResponse response = client.getAcsResponse(request);
11.         System.out.println(JSON.toJSONString(response.getZoneList()));
12.     } catch (Exception ex) {
13.         System.out.println(ex.getMessage());
14.     }
15. }
```

#### 2.4.3 Obtain global authoritative RRSets

Go SDK

```
1. if client, err := genesisdns.NewClientWithAccessKey("{regionid}","{ak}", "{secret}")); e
rr == nil {
2.     request := genesisdns.CreateObtainGlobalAuthRecordListRequest()
3.     request.SetDomain("{endpoint}")
4.     request.Id = requests.Integer("{zone id}")
5.     if response, err := client.ObtainGlobalAuthRecordList(request); err == nil {
6.         fmt.Println(response.Records)
7.     }
8. }
```

Python SDK

```
1. from aliyunsdkcore.client import AcsClient
2. from aliyunsdkcore.profile import region_provider
3. from aliyunsdkcore.acs_exception.exceptions import ClientException
4. from aliyunsdkcore.acs_exception.exceptions import ServerException
5. from aliyunsdkgenesisdns.request.v20180925 import ObtainGlobalAuthRecordListRequest
```

`6.`

```
7. client = AcsClient("{ak}", "{secret}", "{regionid}")
```

`8.`

```
9. request = ObtainGlobalAuthRecordListRequest.ObtainGlobalAuthRecordListRequest()
10. request.set_PageSize(10)
11. request.set_Id({zone id})
12. region_provider.modify_point("GenesisDns", "{regionid}", "{endpoint}")
13. try:
14.     response = client.do_action_with_exception(request)
15.     print(response)
16. except ServerException as e:
17.     print(e)
18. except ClientException as e:
19.     print(e)
```

Java SDK

```
1. public static void main(String[] args) {
2.     DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{secret}");
3.     IAcsClient client = new DefaultAcsClient(profile);
4.     ObtainGlobalAuthRecordListRequest request = new ObtainGlobalAuthRecordListRequest();
5.     try {
6.         request.setEndpoint("{endpoint}");
7.         request.setConnectTimeout(1000);
8.         request.setReadTimeout(1000);
9.         request.setPageSize(10);
10.         request.setId(Long.parseLong("{zone id}"));
11.         ObtainGlobalAuthRecordListResponse response = client.getAcsResponse(request);
12.         System.out.println(JSON.toJSONString(response.getRecords()));
13.     } catch (Exception ex) {
14.         System.out.println(ex.getMessage());
15.     }
16. }
```

#### 2.4.4 Add global RRSets

The following examples describe how a Resource Record Set (RRSet) is defined.

```
1.         request.RrSet = "[\"2001:0:0:0:0:0:0:1\"]" //A RRSet with an AAAA record
2.         request.RrSet = "[\"2001:0:0:0:0:0:0:1\", \"2001::2\"]" //A RRSet with two AAAA
records
3.         request.RrSet = "[\"2001:0:0:0:0:0:0:1 10\", \"2001::2 10\"]" //A RRSet with two
weighted AAAA records
4.         request.Type = "AAAA"
```

`5.`

```
6.         request.RrSet = "[\"www.aliyun.com. \"]" //A RRSet with a CNAME record
7.         request.RrSet = "[\"www.aliyun.com. 10\",\"www.taobao.com 30\"]" //A RRSet with
two weighted CNAME records
8.         request.Type = "CNAME"
```

`9.`

```
10.         request.RrSet = "[\"10 mailserver1.example.com. \"]" //A RRSet with an MX recor
```

`d`

```
11.         request.Type = "MX"
12.
13.         request.RrSet = "[\"10 mailserver1.example.com.\",\"20 mailserver2.example.com.
\"]" //A RRSet with two MX records
14.         request.RrSet = "[\"v=spf1 ip4:192.168.0.1/16 ip6:2001::1/96 ~all\"]" //A RRSet
with a TXT record
15.         request.Type = "TXT"
16.
17.         request.RrSet = "[\"1 10 8080 www1.example.com.\", \"2 20 8081 www2.example.com
. \"]" //A RRSet with two SRV records
18.         request.Type = "SRV"
19.
20.         request.RrSet = "[\"100 50 \\\"S\\\" \\\"Z3950+I2L+I2C\\\" \\\"\\\" _z3950._tcp
.example.com. \"]" //A RRSet with a NAPTR record
21.         request.Type = "NAPTR"
22.
23.         request.RrSet = "[\"0 issue \\\"caa.example.com\\\"\",\"0 issuewild \\\";\\\"\"
]" //A RRSet with a CAA record
24.         request.Type = "CAA"
25.
26.         request.RrSet = "[\"inner-ns1.example01.com. hostmaster.example01.com. 1 7200 9
00 1209600 86400\"]" //A RRSet with an SOA record
27.         request.Type = "SOA"
28.
29.         request.RrSet = "[\"ns1.example.com.\",\"ns2.example.com. \"]" //A RRSet with t
wo NS records
30.         request.Type = "NS"
```

Go SDK

```
1. func main()  {
2.     if client, err := genesisdns.NewClientWithAccessKey("{regionid}","{ak}", "{secret}")
; err == nil {
3.         request := genesisdns.CreateAddGlobalRrSetRequest()
4.         request.SetDomain("{endpoint}")
5.         request.ZoneId = requests.Integer("{zone id}")
6.         request.Ttl = requests.Integer("300")
7.         request.Type = "A"
8.         request.RrSet = "[\"1.1.1.1\"]"
9.         request.Rr = "sdka"
10.
11.         if response, err := client.AddGlobalRrSet(request); err == nil {
12.             fmt.Println(response.RequestId, response.Id)
13.         }
14.     }
15. }
```

Python SDK

```
1. from aliyunsdkcore.client import AcsClient
2. from aliyunsdkcore.profile import region_provider
3. from aliyunsdkcore.acs_exception.exceptions import ClientException
4. from aliyunsdkcore.acs_exception.exceptions import ServerException
5. from aliyunsdkgenesisdns.request.v20180925 import AddGlobalRrSetRequest
```

`6.`

```
7. client = AcsClient("{ak}", "{secret}", "{regionid}")
```

`8.`

```
9. request = AddGlobalRrSetRequest.AddGlobalRrSetRequest()
10. request.set_ZoneId(93)
11. request.set_Rr("sdk_python_a")
12. request.set_RrSet("[\"3.3.3.3\"]")
13. request.set_Ttl(300)
14. request.set_Type("A")
15.
16. region_provider.modify_point("GenesisDns", "{regionid}", "{endpoint}")
17. try:
18.     response = client.do_action_with_exception(request)
19.     print(response)
20. except ServerException as e:
21.     print(e)
22. except ClientException as e:
23.     print(e)
```

Java SDK

```
1. public static void main(String[] args) {
2.     DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{secret}");
3.     IAcsClient client = new DefaultAcsClient(profile);
4.     AddGlobalRrSetRequest request = new AddGlobalRrSetRequest();
5.     try {
6.         request.setEndpoint("{endpoint}");
7.         request.setConnectTimeout(1000);
8.         request.setReadTimeout(1000);
9.         request.setZoneId(Long.parseLong("93"));
10.         request.setRr("sdk_java_a");
11.         request.setTtl(300);
12.         request.setType("A");
13.         request.setRrSet("[\"1.1.1.1\", \"2.2.2.2\"]");
14.         AddGlobalRrSetResponse response = client.getAcsResponse(request);
15.         System.out.println(JSON.toJSONString(response));
16.     } catch (Exception ex) {
17.         System.out.println(ex.getMessage());
18.     }
19. }
```

#### 2.4.5 Delete global RRSets

Go SDK

```
1.    package main
```

`2.`

```
3.    import (
4.        "fmt"
5.        "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
6.        "github.com/aliyun/alibaba-cloud-sdk-go/services/genesisdns"
7.    )
```

`8.`

```
9.    func main()  {
10.        if client, err := genesisdns.NewClientWithAccessKey("{regionid}","{ak}", "{secre
t}"); err == nil {
11.            request := genesisdns.CreateDeleteGlobalRrSetRequest()
12.            request.SetDomain("{endpoint}")
13.            request.Id = requests.Integer("{rrSet id")
14.
15.            if response, err := client.DeleteGlobalRrSet(request); err == nil {
16.                fmt.Println(response.RequestId)
17.            }
18.        }
19.    }
```

Python SDK

```
1.    from aliyunsdkcore.client import AcsClient
2.    from aliyunsdkcore.profile import region_provider
3.    from aliyunsdkcore.acs_exception.exceptions import ClientException
4.    from aliyunsdkcore.acs_exception.exceptions import ServerException
5.    from aliyunsdkgenesisdns.request.v20180925 import DeleteGlobalRrSetRequest
```

`6.`

```
7.    client = AcsClient("{ak}", "{secret}", "{regionid}")
```

`8.`

```
9.    request = DeleteGlobalRrSetRequest.DeleteGlobalRrSetRequest()
10.    request.set_Id(170)
11.
12.    region_provider.modify_point("GenesisDns", "{regionid}", "{endpoint}")
13.    try:
14.        response = client.do_action_with_exception(request)
15.        print(response)
16.    except ServerException as e:
17.        print(e)
18.    except ClientException as e:
19.        print(e)
```

Java SDK

```
1.    public static void main(String[] args) {
2.        DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{secret}
");
3.        IAcsClient client = new DefaultAcsClient(profile);
4.        DeleteGlobalRrSetRequest request = new DeleteGlobalRrSetRequest();
5.        try {
6.            request.setEndpoint("{endpoint}");
7.            request.setConnectTimeout(1000);
8.            request.setReadTimeout(1000);
9.            request.setId(Long.parseLong("{RrSet id}"));
10.            DeleteGlobalRrSetResponse response = client.getAcsResponse(request);
11.            System.out.println(JSON.toJSONString(response));
12.        } catch (Exception ex) {
13.            System.out.println(ex.getMessage());
14.        }
```

#### 2.4.6 Update global RRSets

Go SDK

```
1.    package main
```

`2.`

```
3.    import (
4.        "fmt"
5.        "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
6.        "github.com/aliyun/alibaba-cloud-sdk-go/services/genesisdns"
7.    )
```

`8.`

```
9.    func main()  {
10.        if client, err := genesisdns.NewClientWithAccessKey("{regionid}","{ak}", "{secre
t}"); err == nil {
11.            request := genesisdns.CreateUpdateGlobalRrSetRequest()
12.            request.SetDomain("{endpoint}")
13.            request.RrsetId = requests.Integer("{RrSet id}")
14.            request.Rr = "go_sdk_a"
15.            request.RrSet = "[\"8.8.8.8\"]"
16.            request.Ttl = requests.Integer("300")
17.            request.Type = "A"
18. 19.
20.            if response, err := client.UpdateGlobalRrSet(request); err == nil {
21.                fmt.Println(response.RequestId)
22.            }
23.        }
24.    }
```

Python SDK

```
1.    from aliyunsdkcore.client import AcsClient
2.    from aliyunsdkcore.profile import region_provider
3.    from aliyunsdkcore.acs_exception.exceptions import ClientException
4.    from aliyunsdkcore.acs_exception.exceptions import ServerException
5.    from aliyunsdkgenesisdns.request.v20180925 import UpdateGlobalRrSetRequest
```

`6.`

```
7.    client = AcsClient("{ak}", "{secret}", "{regionid}")
```

`8.`

```
9.    request = UpdateGlobalRrSetRequest.UpdateGlobalRrSetRequest()
10.    request.set_RrsetId(165)
11.    request.set_Type("A")
12.    request.set_Rr("sdk_python_a")
13.    request.set_RrSet("[\"3.3.3.3\"]")
14.    request.set_Ttl(300)
15.
16.    region_provider.modify_point("GenesisDns", "{regionid}", "{endpoint}")
17.    try:
18.        response = client.do_action_with_exception(request)
19.        print(response)
20.    except ServerException as e:
21.        print(e)
22.    except ClientException as e:
23.        print(e)
```

Java SDK

```
1.    public static void main(String[] args) {
2.        DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{secret}
");
3.        IAcsClient client = new DefaultAcsClient(profile);
4.        UpdateGlobalRrSetRequest request = new UpdateGlobalRrSetRequest();
5.        try {
6.            request.setEndpoint("{endpoint}");
7.            request.setConnectTimeout(1000);
8.            request.setReadTimeout(1000);
9.            request.setRrsetId(Long.parseLong("165"));
10.            request.setRr("sdk_java_a");
11.            request.setRrSet("[\"4.4.4.4\"]");
12.            request.setTtl(300);
13.            request.setType("A");
14.
15.            UpdateGlobalRrSetResponse response = client.getAcsResponse(request);
16.            System.out.println(JSON.toJSONString(response));
17.        } catch (Exception ex) {
18.            System.out.println(ex.getMessage());
19.        }
20.    }
```

#### 2.4.7 Configure descriptions for global RRSets

Go SDK

```
1. package main
```

`2.`

```
3. import (
4.     "fmt"
5.     "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
6.     "github.com/aliyun/alibaba-cloud-sdk-go/services/genesisdns"
7. )
```

`8.`

```
9. func main()  {
10.     if client, err := genesisdns.NewClientWithAccessKey(""{regionid}","{ak}", "{secret}
"); err == nil {
11.         request := genesisdns.CreateRemarkGlobalRrSetRequest()
12.         request.SetDomain("{endpoint}")
13.         request.Id = requests.Integer("165")
14.         request.Remark = "go remark"
15. 16.
17.         if response, err := client.RemarkGlobalRrSet(request); err == nil {
18.             fmt.Println(response.RequestId)
19.         }
20.     }
21. }
```

Python SDK

```
1. from aliyunsdkcore.client import AcsClient
2. from aliyunsdkcore.profile import region_provider
3. from aliyunsdkcore.acs_exception.exceptions import ClientException
4. from aliyunsdkcore.acs_exception.exceptions import ServerException
5. from aliyunsdkgenesisdns.request.v20180925 import RemarkGlobalRrSetRequest
```

`6.`

```
7. client = AcsClient("{ak}", "{secret}", "{regionid}")
```

`8.`

```
9. request = RemarkGlobalRrSetRequest.RemarkGlobalRrSetRequest()
10. request.set_Id(165)
11. request.set_Remark("test remark python")
12. region_provider.modify_point("GenesisDns", "{regionid}", "{endpoint}")
13. try:
14.     response = client.do_action_with_exception(request)
15.     print(response)
16. except ServerException as e:
17.     print(e)
18. except ClientException as e:
19.     print(e)
```

Java SDK

```
1. public static void main(String[] args) {
2.     DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{secret}");
3.     IAcsClient client = new DefaultAcsClient(profile);
4.     RemarkGlobalRrSetRequest request = new RemarkGlobalRrSetRequest();
5.     try {
6.         request.setEndpoint("{endpoint}");
7.         request.setConnectTimeout(1000);
8.         request.setReadTimeout(1000);
9.         request.setId(Long.parseLong("165"));
10.         request.setRemark("test java remark");
11.
12.         RemarkGlobalRrSetResponse response = client.getAcsResponse(request);
13.         System.out.println(JSON.toJSONString(response));
14.     } catch (Exception ex) {
15.         System.out.println(ex.getMessage());
16.     }
17. }
```
