---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 ApsaraDB for Redis Developer Guide"
product_version: "V3.16.2"
doc_version: "20220915"
pdf_pages: 114
source_pdf: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 ApsaraDB for Redis Developer Guide 20220915.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.16.2_intl_en/%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97%2B%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20ApsaraDB%20for%20Redis%20Developer%20Guide%2020220915.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 ApsaraDB for Redis Developer Guide

## ASAPI Developer Guide

### Preparations

#### Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press Enter.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Log On.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding operations
in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click Log On. c. Enter a six-digit MFA verification code and click Aut hent icat e. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click Aut hent icat e. Not e For more information, see the Bind a virtual MFA device to enable MFA topic in A psara Uni-manager Management Console User Guide.
5. In the top navigation bar, choose Product s > Ot hers > API T ool.

#### View information about API operations

This topic describes how to view information about API operations. Before you use SDKs, obtain service names, API operation names, and API operation versions. Context The API operations on the API Directory page are only for reference. For information about how to call API operations, see developer guides of the corresponding cloud services. If the information on the API Directory page is inconsistent with that in the developer guide of the corresponding cloud service, the information in the developer guide prevails. Procedure
1. Go to the API Tool console. For more information, see Log on to the API Tool console.
2. In the left-side navigation pane, click API Direct ory.
3. On the API Direct ory page, select the desired service from the drop-down list, enter a keyword of
an API operation name in the search box, and then click the search icon.
4. Then, you can view the service name, API operation name, and API operation version.

#### Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. AccessKey pairs are used to implement symmetric encryption to verify the identity of requesters. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. This topic describes how to obtain an AccessKey pair. Prerequisites An account that assumes the operations administrator or level-1 organization administrator role is obtained. Only an operations administrator or a level-1 organization administrator can obtain an AccessKey pair of the organization. Context AccessKey supports the following authorization methods: Use RAM to authorize the AccessKey ID and AccessKey secret to third-party requesters. Use STS to authorize the AccessKey ID, AccessKey secret, and security token to third-party requesters. This topic describes how to obtain an AccessKey pair authorized by RAM. For more information about how to obtain an AccessKey pair authorized by STS, see Obtain an STS AccessKey pair. We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions can occur.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region, such as cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For information about how to obtain an organization ID, see the "GetOrganizationList" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance on which to perform operations. For example, you can query the ID of an Elastic Compute Service (ECS) instance from the ECS instance list. |

Warning The AccessKey pair of a personal account is managed and controlled by the permission system of the Apsara Uni-manage Management Console. If you need to obtain the AccessKey pair of an account that has permissions on an organization, make sure that your operation is allowed by an administrator. This ensures security. The account that has permissions on an organization is a privileged account. Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and choose
User Inf ormat ion from the shortcut menu.
3. In the Apsara St ack AccessKey Pair section, obtain the AccessKey pair.
Not e The AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide you with full permissions on Apsara Stack resources. You must keep the AccessKey pair confidential. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Organizat ions.
4. In the organization navigation tree, click the name of the level-1 organization for which you want
to obtain AccessKey pairs.
5. Click Management AccessKey on the right side of the page.
6. In the AccessKey message, view the AccessKey pair of the organization.

#### Obtain common header parameters

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

#### Obtain an STS AccessKey pair

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

3. You can use STS to make API calls. The following sample code demonstrates how to call ECS API
operations.

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
        asClient.setSdkSource("asapi_test");
  // Call ECS API operations.
        String ecsRes = DescribeZones(asClient,<stsAK>,<stsSK>,<stsToken>);
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

### Use POP to make API calls

#### Preparations

Like in the public cloud, you can use the POP gateway to call API operations in Apsara Stack. This topic describes the preparations before you use the POP gateway to call API operations. Background information In Apsara Stack, you can use both ASAPI and POP gateways to call API operations. To use the same method and produce the same user experience as in the public cloud, we recommend that you use the POP gateway to call API operations in Apsara Stack. Obtain service endpoints To use the POP gateway to call API operations, you must use the service endpoints. You can obtain the service endpoints from Alibaba Cloud onsite O&M engineers. You can also obtain the service endpoints by yourself. The following example describes how to obtain the ECS endpoints.
1. Log on to Apsara Infrastructure Management Framework.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click O&M. iii. In the left-side navigation pane, choose Product Management > Product s. iv. In the Apsara Stack O&M section, click Apsara Inf rast ruct ure Management Framework.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for `Registration Vars of Services` and click the report name.
4. On the Regist rat ion Vars of Services page, click the
icon next to Service and search for `ECS` .
5. Find the `ecs-yaochi` service, right-click the Service Regist rat ion column, and then select Show
More from the shortcut menu. On the Det ails page, view the int ernal.openapi.endpoint value, which is the `endpoint` . Obtain common parameters You must obtain the parameters required when you use the POP gateway to call API operations, such as the organization ID, resource set ID, region ID, and instance ID. For more information, see Obtain common header parameters.

#### SDK for Java

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

The following sample code provides an example on how to use the ROA style to make an API call. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016- 06-07. Sample code:

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

Not ice If you send a request over HTTPS, you must enable the request to ignore SSL certificate validation.

#### SDK for Go

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
    fmt.Print(response.GetHttpContentString())
```

The following sample code provides an example on how to use the ROA style to make an API call. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016- 06-07. The following sample code shows how to call API operations:

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
 fmt.Print(response.GetHttpContentString())
```

Configure proxies You can configure proxies in one of the following ways when you call API operations: Configure proxies as environment variables. Set the HTTP_PROXY and HTTPS_PROXY environment variables, or set the NO_PROXY environment variable. Sample code:

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

Configure proxies on the client. Sample code:

```
// The proxies that are configured on the client take precedence over those that are conf igured by using environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Configure the HTTP proxy. client.GetHttpProxy() // Query the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Configure the HTTPS proxy. client.GetHttpsProxy() // Query the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Configure the proxy whitelist. client.GetNoProxy() // Query the proxy whitelist.
```

#### SDK for Python

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

### Use ASAPI to make API calls

#### ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage organizations, users, roles, resource sets, and logon policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Uni-manager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Uni-manager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide. Not e If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

#### Generate an endpoint for ASAPI

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

Not e
1. Replace <region> with your actual region ID. For information about how to query a region ID,
see Query a region ID.
2. Replace <internet-domain> with the root domain of your Apsara Stack service. To obtain the
root domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internetdomain parameter instead of the intranet-domain parameter. If the region value is `cn-****-****-d01` and the int ernet -domain value is `inter.****.****.com` , the following endpoint can be generated: An example of a complete endpoint:

```
https://public.asapi.cn-****-****-d01.inter.****.****.com/asapi/v3
```

#### Obtain Apsara Stack SDKs

Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use the ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. You can go to Apsara Stack documentation and download the Apsara Stack SDKs in the Ot her Resources section at the lower part of the page.

#### Common request parameters

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

Not e

```
The Signature , SignatureMethod , SignatureVersion , SignatureNonce , Timestamp ,
```

and `Format` parameters are encapsulated into Apsara Stack SDK. You do not need to configure these parameters.

#### SDK description

##### SDK for Java

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

Not e Replace `1.0.6.4-RELEASE` with the actual version of Apsara Stack SDK for Java.
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

##### SDK for Python

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

Not e Replace `2.4.7` with the actual version of Apsara Stack SDK for Python. Sample requests You can use the GET or POST method to call API operations provided by ASAPI.

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

##### SDK for Node.js

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
value of the operation-specific parameter>" // 5. Configure request headers. // When you use the STS AccessKey ID to call ROA API operations, you must add the x-acs-sec urity-token parameter to the header. // AsapiClient.addHeader("x-acs-security-token", "<your-securitytoken>") AsapiClient.addHeader('x-acs-caller-sdk-source', '<The identifier of the requester>') AsapiClient.addHeader('x-acs-roleid', '<The ID of the role>') AsapiClient.addHeader('x-acs-userid', '<The ID of the user>') AsapiClient.addHeader('x-acs-organizationid', '<your-organizationid>') AsapiClient.addHeadert("x-acs-regionid", "<your-regionid>"); AsapiClient.addHeader("x-acs-resourcegroupid", "<your-resourcegroupid>"); AsapiClient.addHeader("x-acs-instanceid", "<your-instanceid>"); // 6. Make an API call and obtain the response. try {
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

Disable certificate validation The following sample code shows how to disable certificate validation:

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

#### HTTP requests

##### Overview

This topic describes how to make API requests and is intended for users who use API URLs to initiate HTTP GET requests. If you are using an SDK to initiate requests, you can skip this topic. The request URL consists of different parameters and has a fixed syntax. The URL contains common request parameters, your signature, and operation-specific parameters. Sample request URLs are provided for each API operation. These URLs are not encoded to make them easy to read. Before you make a request, you must encode the request URL. After the authentication process is complete based on your signature, the results are returned to you. Response parameters are returned if the call is successful, whereas an error message is returned if the call fails. You can troubleshoot issues based on the error message.

##### Request structure

You can use API URLs to initiate HTTP GET requests. Each URL must include request parameters. This topic describes the syntax of HTTP GET requests and provides the endpoint of ASAPI. Sample request GetOrganizationList is used in the following unencoded URL request:

```
https://public.asapi.aliyuns.com/asapi/v3?Action=GetOrganizationList&Product=ascm&Version=2 019-05-10&Id=<Organization ID>&<Common parameters>
```

`https` : the protocol used to transmit the request. `public.asapi.aliyuns.com/asapi/v3` : the endpoint of ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` : the API operation. `Id` : the ID of the organization. `<Common request parameters>` : common parameters specified in the system. Protocols ASAPI supports only the HTTP request protocol. Endpoints For more information about how to obtain the endpoint of ASAPI, see Generate an endpoint for ASAPI. You must use the `Action, Product, and Version` parameters to specify an API operation. For example, you can set `Action to GetOrganizationList, Product to ascm, and Version to 2019-05-10` . You must also specify other operation-specific request parameters and common request parameters. For more information, see Common request parameters.

##### Request signatures

This topic describes how to sign HTTP API requests. ASAPI uses the request signature to verify the identity of the request sender. ASAPI implements symmetric encryption by using an AccessKey pair to verify the identity of the request sender. Not e An AccessKey pair consists of an AccessKey ID and an AccessKey secret, which are issued to each user or organization in the Apsara Uni-manager Management Console. The AccessKey ID is used to verify identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must keep your AccessKey secret confidential. ASAPI provides SDKs for Node.js, Python, and Java to facilitate complex signature calculation. For more information, see Obtain the core package for ASAPI. Step 1: Create a canonicalized query string
1. Arrange the request parameters in alphabetical order, including all common and operation-specific
parameters except the `Signature` parameter. Not e If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?).
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

Not e When you calculate the signature, the key value specified by RFC 2104 is your `AccessKey secret` plus an ampersand (&), which has an ASCII value of 38. For more information, see Obtain an AccessKey pair.
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

2. Predefine the time format for the `Timestamp` parameter. Specify the `Timestamp` parameter in
the ISO 8601 format. The time must be in UTC+0.

```java
private static final String ISO8601_DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ss'Z'"; private static String formatIso8601Date(Date date) {
    SimpleDateFormat df = new SimpleDateFormat(ISO8601_DATE_FORMAT);
    df.setTimeZone(new SimpleTimeZone(0, "GMT"));
    return df.format(date);
```

3. Create a request string.

```
final String HTTP_METHOD = "GET"; Map parameters = new HashMap(); // Specify request parameters. parameters.put("Product", "ascm"); parameters.put("Action", "GetOrganizationList"); parameters.put("Version", "2019-05-10"); parameters.put("AccessKeyId", "testid"); parameters.put("RegionId", "cn-region-test"); parameters.put("Timestamp", formatIso8601Date(new Date())); parameters.put("SignatureMethod", "HMAC-SHA1"); parameters.put("SignatureVersion", "1.0"); parameters.put("SignatureNonce", UUID.randomUUID().toString()); parameters.put("Format", "JSON"); parameters.put("Id", "1"); // Arrange request parameters. String[] sortedKeys = parameters.keySet().toArray(new String[]{}); Arrays.sort(sortedKeys); final String SEPARATOR = "&"; // Create a string-to-sign. StringBuilder stringToSign = new StringBuilder(); stringToSign.append(HTTP_METHOD).append(SEPARATOR); stringToSign.append(percentEncode("/")).append(SEPARATOR); StringBuilder canonicalizedQueryString = new StringBuilder(); for(String key : sortedKeys) {
    // Encode the key and the value.
    canonicalizedQueryString.append("&")
    .append(percentEncode(key)).append("=")
    .append(percentEncode(parameters.get(key)));
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

##### Responses

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

`],`

```json
  "requestId":"xxxxxxxxxxxxxx",
  "success":true,
  "message":"success"
```

Sample error responses If a request fails, the following information is returned. For more information, see the developer guide of the corresponding Apsara Stack service. `{`

```json
    "code": "asapi.server.api.notfound",// The error code.
    "eagleEyeTraceId": "xxx-xxx-xxx-xxx", // The trace ID provided by EagleEye.
    "asapiSuccess": false, // Indicates whether the request is successful.
    "hostId": "xxxx", // The ID of the host.
    "message": "Failed to ....", // The message returned.
    "asapiErrorMessage": "Failed to ....", // The error message provided by ASAPI.
    "asapiErrorCode": "asapi.server.api.notfound" // The error code provided by ASAPI.
```

## API reference

### API overview

Instance lifecycle management API operations

| Operation | Description |
|---|---|
| CreateInstance | Creates an instance. |
| DeleteInstance | Releases an instance. |
| ModifyInstanceSpec | Changes the specifications of a specified instance. |

Instance management API operations

| Operation | Description |
|---|---|
| DescribeInstanceAttribute | Queries detailed information about instances. |
| DescribeInstances | Queries basic information about instances. |
| DescribeRegions | Queries available regions. |
| DescribeSecurityIps | Queries the IP whitelist that allows connections to a specified instance from specified IP addresses or CIDR blocks. |
| FlushInstance | Clears an instance. |
| ModifyInstanceAttribute | Sets the attribute for a specified instance. |
| ModifyInstanceMaintainTime | Changes maintenance time for a specified instance. |
| ModifySecurityIps | Changes the whitelist for a specified instance. |
| ModifyInstanceNetExpireTime | Changes the period for retaining a domain name of a specified classic network. |
| SwitchNetwork | Changes the type of a network. |

Backup and recovery API operations

| Operation | Description |
|---|---|
| CreateBackup | Creates a backup. |
| ModifyBackupPolicy | Changes a backup policy. |
| DescribeBackupPolicy | Queries backup policies. |

|   | Developer Guide·API reference | ApsaraDB for Redi | s |
|---|---|---|---|

| Operation | Description |
|---|---|
| DescribeBackups | Queries available backups. |
| RestoreInstance | Restore a specified instance based on a specified backup set. |

Monitoring management API operations

| Operation | Description |
|---|---|
| DescribeMonitorItems | Queries available monitoring metrics. |
| DescribeHistoryMonitorValues | Queries historical monitoring data. |

Parameter management API operations

| Operation | Description |
|---|---|
| DescribeInstanceConfig | Queries parameters of a specified instance. |
| ModifyInstanceConfig | Changes parameters of a specified instance. |

### Request structures

Endpoint The endpoint of the KVStore for Redis API is `r-kvstore.`example.com. For more information about how to obtain an endpoint, see Generate the endpoint of ASAPI. Not e example.com is a domain name that is customized for a project. You can obtain the domain name from the administrator. Protocols You can send requests over HTTP or HTTPS. To enhance data security, we recommend that you send API requests by using HTTPS. Methods You can send requests by using the HTTP GET method. This method requires that you specify request parameters in the request URL. Request parameters You must specify the Action parameter for each request. For example, you can specify CreateInstance. You must also specify common request parameters and specific request parameters that are required by each operation. Encoding Requests and responses are both encoded in UTF-8.

### Common parameters

Common request parameters must be included in all API requests. Common request parameters Common request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Format | String | Yes | The type of the returned value. Valid values: JSON and XML. Default value: XML |
| Version | String | Yes | The version of the API. Specify the version in the YYYY- MM-DD format. The current version is 2015-01-01. |
| AccessKeyId | String | Yes | The AccessKey ID provided by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMetho d | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. For example, you can set the parameter to 2016-01-01T12:00:00Z. This specifies 20:00:00, January 1, 2016, UTC+08:00. |
| SignatureVersio n | String | Yes | The version of the signature algorithm. The current version is 1.0. |
| SignatureNonce | String | Yes | The unique random number that is used to prevent replay attacks. You must use different random numbers for different requests. |

```
https:// r-kvstore.example.com/ ? Format=json &Version=2015-01-01 &Signature=Pc5xxxxxxxxxxxxxxxxxx &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2016-01-01T12:00:00Z
```

Common response parameters Each time you call an API operation, the system returns a globally unique ID (RequestId). This is regardless of whether the request is successful.

```xml
<? xml version="1.0" encoding="utf-8"? > <!-The root of the response--> <Operation name+Response> <!—The returned request tag--> <RequestId>4C4fdsf38-3910-447D-87AD-AC078932216</RequestId> <!—The returned result--> </Operation name+Response>
```

### Responses

After you call an API operation, KVStore for Redis returns data in the same format. In the response, an HTTP status code in the `2xx` format indicates that the call is successful. An HTTP status code in the `4xx` or `5xx` format indicates that the call failed. The system returns responses for successful calls in XML or JSON format. You can specify the response format in request parameters. The system uses the XML format by default. Not e The response examples in this topic have been formatted with line breaks or indents to provide a clear view. The responses in your actual running environments are not properly formatted as these examples. Sample success response The response in XML format includes a message that indicates whether the call is successful and the specific service data. An example is as follows:

```xml
<? xml version="1.0" encoding="utf-8"? > <!—The root node of the response--> <Operation name+Response> <!—The request ID returned--> <RequestId>4C4fdsf38-3910-447D-87AD-AC078932216</RequestId> <!—The result data returned--> </Operation name+Response>
```

JSON format `{`

```json
"RequestId": "4C4fdsf38-3910-447D-87AD-AC078932216", /* The result data returned */
```

Sample error response When an error occurs during an API call, no result data is returned. You can locate the cause of the error by referencing the attached list of error codes. If an error occurs when you call an operation over HTTP, an HTTP status code in the `4xx` or `5xx` format is returned. The returned message body includes the specific error code and error message. The message body also contains a globally unique request ID called RequestId and a target site ID called HostId. If you cannot locate the cause, request Apsara Stack customer service, and provide the HostId and RequestId for troubleshooting.

```xml
<? xml version="1.0" encoding="UTF-8"? > <Error> <RequestId>8906582E-6722-409A-A6C4-0E7863B733A5</RequestId> <HostId> r-kvstore.example.com</HostId> <Code>UnsupportedOperation</Code> <Message>The specified action is not supported. </Message> </Error>
```

JSON format `{`

```json
"RequestId": "7463B73D-35CC-4D19-A010-6B8D65D242EF", "HostId": " r-kvstore.example.com", "Code": "UnsupportedOperation", "Message": "The specified action is not supported."
```

### Request signatures

KVStore for Redis authenticates each access request. You need to include a signature when you submit an HTTP or HTTPS request. KVStore for Redis authenticates the request sender identity by using symmetric encryption based on an AccessKey pair that consists of an AccessKey ID and an AccessKey secret. An AccessKey ID and an AccessKey secret are issued to you by Alibaba Cloud. You can apply for and manage them on the Alibaba Cloud website. The AccessKey ID is used to verify the identity of the user. The AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to obtain the AccessKey pair, see Obtain an AccessKey pair. Sign a request Perform the following steps to sign an API request:
1. Create a canonicalized query string by using request parameters.
i. To construct a canonicalized query string, sort all request parameters by name in alphabetic order. These parameters include common request parameters and customized API request parameters. However, this does not include the Signature parameter. Not e When you use the GET method to submit requests, you specify these parameters in the request URI that follow the question mark (?) and are connected with the ampersand (&). ii. Encode the name and value of each request parameter. Perform URL encoding on the names and values by using the UTF-8 character set. The following section shows the URL encoding rules: Uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), hyphens (-), underscores (_), periods (.), and tildes (~) are not encoded. Encode other characters in the %XY format, where `XY` specifies the ASCII code of the characters in the hexadecimal format. For example, double quotation marks (") are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA format. Spaces must be encoded as %20 . Do not encode spaces as plus signs (+).

| Not e Libraries that support URL encoding, such as java.net.URLEncoder, follow the Multipurpose Internet Mail Extensions (MIME) encoding rules of application/x-www-form-u rlencoded . If this encoding method is used, replace the plus signs (+) in the encoded strings with %20 , the asterisks (*) with %2A , and %7E with a tilde (~) to conform to the encoding rules. |   |   |
|---|---|---|
|   | application/x-www-form-u |   |

| rlencoded |   |
|---|---|
|   | %20 |

iii. Connect the encoded parameter name and value with an equal sign (=). iv. Sort the key-value pairs connected by equal signs (=) in alphabetical order and separate them with ampersands (&).
2. Create a string-to-sign from the encoded canonicalized query string that is obtained in the
preceding step based on the following rules:

```
 StringToSign=
 HTTPMethod + "&" +
 percentEncode("/") + "&" +
 percentEncode(CanonicalizedQueryString)
```

In this example, `HTTPMethod` specifies the HTTP method that is used to submit the request, such as GET. `percentEncode("/")` is the value ( %2F ) as the result of encoding the slash sign (/) based on the URL encoding rule described in Step 1.b. `percentEncode(CanonicalizedQueryString)` is the string that results from encoding the canonicalized query string described in Step 1 based on the URL encoding rules described in Step 1.b.
3. As defined in RFC 2104, use the preceding signature string to calculate the signature into an HMAC
value. Not e The key that is used for calculating the signature is your AccessKey secret followed by an ampersand (&) (ASCII:38). The SHA1 algorithm is used for the calculation.
4. Encode the HMAC value in Base64 to obtain the signature string.
5. Add the signature string to the request as the Signature parameter.
Not e When you submit the signature string to the KVStore for Redis instance as the final request parameter value, perform URL encoding on this parameter based on RFC 3986 rules. This is the same method that is used to process other parameters. DescribeDrdsInstances is used in this example. The following section shows the canonicalized query string:

```
http://r-kvstore.example.com/?Timestamp=2013-06-01T10:33:56Z&Format=XML&AccessKeyId=testid& Action=DescribeInstances&SignatureMethod=HMAC-SHA1&RegionId=region1&SignatureNonce=NwDAxvLU 6tFE0DVb&Version=2015-01-01&SignatureVersion=1.0
```

The following section shows the calculated StringToSign:

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeInstances&Format%3DXML&RegionId%3Dregion1&Sig natureMethod%3DHMAC-SHA1&SignatureNonce%3DNwDAxvLU6tFE0DVb&SignatureVersion%3D1.0&Timestamp %3D2013-06-01T10%253A33%253A56Z&Version%3D2015-01-01
```

| In this example, if the AccessKey ID is testid used for HMAC calculation is testsecret& . T BIxxxxxxxxxxxxxxxxxxxxxx= . | testid |
|---|---|
| BIxxxxxxxxxxxxxxxxxxxxxx= |   |

In this example, if the AccessKey ID is `testid` and the AccessKey secret is `testsecret` , the key The following section shows the signed request URL that includes the Signature parameter:

```
http://r-kvstore.example.com/?Timestamp=2013-06-01T10%3A33%3A56Z&Format=XML&AccessKeyId=tes tid&Action=DescribeInstances&SignatureMethod=HMAC-SHA1&RegionId=region1&SignatureNonce=NwDA xvLU6tFE0DVb&SignatureVersion=1.0&Version=2015-01-01&Signature=BIPOMlxxxxxxxxxxxxxxxxxxu8LX BeZtLQkJTw6iFvw1E%3D
```

### RAM-based authorization

#### Grant resource permissions to a RAM user

The instances that you create by using your Alibaba Cloud account are the resources owned by the account. An account has the full operation permissions on the resources under this account by default. Alibaba Cloud Resource Access Management (RAM) allows you to grant the access and management permissions on resources under a cloud account to RAM users. Not e Ignore this topic if you do not use Resource Access Management (RAM).

#### Authorized resource types in RAM

KVStore for Redis only supports RAM authorization for Redis instances. The following table lists the description of resources when you use RAM to authorize access permissions to these resources.

| Resource | Resource description in authorization policy |
|---|---|
| Instance | acs:kvstore:$regionid:$accountid:instance/$instanc eid acs:kvstore:$regionid:$accountid:instance/ acs:kvstore:::instance/ |

All $regionids must be the ID of a region or an asterisk ( `*` ). All $instanceids must be the ID of an instance or an asterisk ( `*` ). Similarly, $account-id is the numerical ID of your Apsara Stack tenant account, which can be replaced by an asterisk ( `*` ).

#### Operation permissions granted to a RAM

user You are authorized to call the following API operations to manage the specified resource as a Resource Access Management (RAM) user: CreateInstance DeleteInstance ModifyInstanceSpec RenewInstance RenewMultiInstance TransformToPrePaid ModifyInstanceAttribute FlushInstance DescribeInstances DescribeInstanceAttribute ModifyInstanceMaintainTime ModifySecurityIps SwitchNetwork ModifyInstanceNetExpireTime CreateBackup ModifyBackupPolicy DescribeBackupPolicy DescribeBackups RestoreInstance DescribeHistoryMonitorValues DescribeInstanceConfig ModifyInstanceConfig

#### API authentication rules

When you use API operations to access resources as a Resource Access Management (RAM) user, the system queries the RAM service and checks whether the RAM user is granted the required permissions. Each API operation determines the resources for permission check according to the involved resources and the semantics of the API operation. The following table lists the authentication rules corresponding to different API operations. Authentication rules

| Operation | Authentication rule |
|---|---|
| CreateDBInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DeleteInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceSpec | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| RenewInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| RenewMultiInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| TransformToPrePaid | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceAttribute | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| FlushInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeInstances | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeInstanceAttribute | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceMaintainTime | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifySecurityIps | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| SwitchNetwork | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceNetExpireTime | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| CreateBackup | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyBackupPolicy | acs:kvstore:$regionid:$accountid:instance/$instanc eid |

| eveloper Guide·API reference | ApsaraDB for Redi |
|---|---|
| Operation | Authentication rule |
| DescribeBackupPolicy | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeBackups | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| RestoreInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeHistoryMonitorValues | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeInstanceConfig | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceConfig | acs:kvstore:$regionid:$accountid:instance/$instanc eid |

### Manage the lifecycle

#### CreateInstance

Creates a KVStore for Redis instance. Request parameters

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |   |   |
| Action | String | Yes | CreateInstance | The operation that you want to perform. Set this parameter to CreateInstance. |   |   |
| InstanceName | String | No | apitest | The name of the instance. The name must be 2 to 128 characters in length. The name must start with a letter. It cannot contain spaces or the following special characters: @ / : = " < > { [ ] } |   |   |
|   |   |   |   |   | @ / : = " < > { [ |   |
|   |   |   |   | ] } |   |   |

| Parameter | Type | Required |   | Example | Description |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| Password | String | No |   | Pass!123456 | The password that is used to connect to the instance. The password must be 8 to 30 characters in length and must contain uppercase letters, lowercase letters, and digits. Not e Special characters are not supported, such as ! < > ( ) [ ] { } , ` ~ . - @ # $ % ^ & * _ |   |   |   |   |   |
|   |   |   |   |   |   |   | Not e Special characters are not supported, such as ! |   |   |   |
|   |   |   |   |   |   |   |   | ! |   |   |
|   |   |   |   |   |   |   | < > ( ) [ ] { } , ` ~ . - |   |   |   |
|   |   |   |   |   |   |   | @ # $ % ^ & * _ |   |   |   |
| InstanceClass | String | Yes |   | redis.master.s mall.default | The type of the KVStore for Redis instance. For more information, see Instance types. |   |   |   |   |   |
| RegionId | String | Yes |   | cn-hangzhou | The region ID of the instance. You can query available regions by calling the DescribeRegions operation. |   |   |   |   |   |
| ZoneId | String | No |   | cn-hangzhou-e | The zone ID of the instance. You can query available zones by calling the DescribeRegions operation. |   |   |   |   |   |
| Token | String | No |   | ChargeType | The client token that is used to ensure the idempotence of requests. The value of this parameter is generated by the client and must be unique among different requests. The value is case-sensitive and can be up to 64 ASCII characters in length. |   |   |   |   |   |
| NetworkType | String | No |   | VPC | The type of the network. Default value: Classic. Valid values: Classic VPC |   |   |   |   |   |
| VpcId | String | No |   | vpc- bp1nme44gek3 4slfc**** | The ID of the VPC to which the instance belongs. |   |   |   |   |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VSwitchId | String | No | vsw- bp1e7clcw529l 773d**** | The ID of the vSwitch to which the instance belongs. Not e This parameter is required if the VpcId parameter is specified. |
| PrivateIp | String | No | 172.16.0.*** | The private IP address of the instance. |
| SrcDBInstanceId | String | No | r- bp1zxszhcgatn x**** | If an instance created based on a backup set generated by another instance is valid, specifies the ID of the instance that generates the backup set. |
| BackupId | String | No | 111111111 | If an instance created based on a backup set generated by another instance is valid, specifies the ID of the generated backup set. You can query backup set IDs by calling the DescribeBackups operation. |
| InstanceType | String | No | Redis | The category of the instance. Valid values: Redis and Memcache. Default value: Redis. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| InstanceId | String | r-bp1zxszhcgatnx**** | The globally unique identifier (GUID) of the KVStore for Redis instance. |
| InstanceName | String | apitest | The name of the instance. |

Not e Due to the compatibility with earlier versions, this topic does not describe some returned fields such as Config and Region for the operation. Alibaba Cloud will delete these fields as needed in the future. Sample requests

```
https://r-kvstore.example.com ?<Common request parameters> &Action=CreateInstance &RegionId=cn-hangzhou &Password=Pass!123456 &InstanceClass=redis.master.small.default
```

Sample responses XML format

```xml
<CreateInstanceResponse>
    <InstanceId>r-n8r8c5119d2e****</InstanceId>
    <InstanceName>testdb</InstanceName>
</CreateInstanceResponse>
```

JSON format `{`

```json
"InstanceId":"r-n8r8c5119d2e****", "InstanceName":"testdb"
```

#### DeleteInstance

Deletes a specified instance. The instance must be in the running state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DeleteInstance | The operation that you want to perform. Set the value to DeleteInstance. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The globally unique identifier (GUID) of the KVStore for Redis instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

Sample requests

```
https://r-kvstore.example.com &Action=DeleteInstance &InstanceId=r-n8r8c5119d2e**** &Common request parameters
```

Sample responses XML format

```xml
<DeleteInstanceResponse>
      <RequestId>5D622714-AEDD-4609-9167-F5DDD3D190D2</RequestId>
</DeleteInstanceResponse>
```

JSON format `{`

```json
    "RequestId": "5D622714-AEDD-4609-9167-F5DDD3D190D2"
```

#### ModifyInstanceSpec

Changes the specifications of a KVStore for Redis instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | ModifyInstan ceSpec | The operation that you want to perform. Set this parameter to ModifyInstanceSpec. |
| InstanceId | String | Yes | r- bp1zxszhcga tnx**** | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceClass | String | Yes | redis.logic.sh arding.drredi ssdb1g.1db. 0rodb.4proxy .default | The type of the KVStore for Redis instance. For more information, see Instance types. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common request parameters> | N/A | N/A | For more information, see Common parameters. |
| OrderId | String | 20722623431**** | The ID of the order. |

Sample requests

```
https://r-kvstore.example.com &Action=ModifyInstanceSpec &InstanceId=r-n8r8c5119d2e**** &InstanceClass= redis.master.mid.default &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyInstanceSpecResponse>
      <RequestId>A4828C10-AF0A-4CD7-8FBE-737C6CC1193E</RequestId>
      <OrderId>20722623431****</OrderId>
</ModifyInstanceSpecResponse>
```

JSON format `{`

```json
    "RequestId": "A4828C10-AF0A-4CD7-8FBE-737C6CC1193E",
    "OrderId": "20722623431****"
```

### Manage instances

#### DescribeInstanceAttribute

Queries detailed information about a KVStore for Redis instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DescribeInstanceA ttribute | The operation that you want to perform. Set this parameter to DescribeInstanceA ttribute. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Instances | List | N/A | An array that consists of the DBInstanceAttribute values. |

Parameters of DBInstanceAttribute

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceId | String | r-bp1d72gwl41z7f**** | The ID of the instance. |
| InstanceName | String | apitest | The name of the instance. |
| Capacity | Long | 1024 | The capacity of the instance. Unit: MB. |
| InstanceClass | String | redis.logic.sharding.drre dissdb1g.1db.0rodb.4pr oxy.default | The type of the instance. |
| Bandwidth | Long | 10 | The bandwidth threshold of the instance. Unit: Mbit/s. |
| Connections | Long | 10000 | The maximum connections allowed to the instance. |

| Parameter | Type | Example |   | Description |   |   |
|---|---|---|---|---|---|---|
| ConnectionDomain | String | r- bp1d72gwl41z7f****.re dis.rds.aliyuncs.com |   | The endpoint of the instance. This endpoint only supports connections over an internal network. |   |   |
| Port | Int | 6379 |   | The port of the instance. |   |   |
| RegionId | String | cn-hangzhou |   | The region ID of the instance. For more information, see DescribeRegions. |   |   |
| ZoneId | String | cn-hangzhou-b |   | The zone ID of the instance. For more information, see DescribeRegions. |   |   |
| InstanceStatus | String | Normal |   | The status of the instance. Valid values: Normal Creating Changing Inactive |   |   |
| CreateTime | String | 2019-03-06T10:42:03Z |   | The time when the instance was created. The time follows the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. The time is displayed in UTC. |   |   |
| EndTime | String | 2019-04-06T10:42:03Z |   | The time when the subscription instance expires. The time follows the ISO 8601 standard in the YYYY- MM-DDThh:mm:ssZ format. The time is displayed in UTC. |   |   |
|   |   |   |   |   | YYYY- |   |
|   |   |   |   | MM-DDThh:mm:ssZ |   |   |
| NetworkType | String | VPC |   | The network type of the instance. Valid values: Classic and VPC. |   |   |

|   |   | YYYY-MM- |   |
|---|---|---|---|
|   | DDThh:mm:ssZ |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpcId | String | vpc- bp1nme44gek34slfc**** | The ID of the VPC to which the instance belongs. |
| VSwitchId | String | vsw- bp1e7clcw529l773d**** | The ID of the vSwitch to which the instance belongs. |
| MaintainStartTime | String | 18:00Z | The start time of the maintenance window. |
| MaintainEndTime | String | 22:00Z | The end time of the maintenance window. |
| SecurityIPList | String | 127.0.0.1 | The IP whitelist. |
| AvailabilityValue | String | 100% | The availability metric of the current month. |

Not e Due to the compatibility with earlier versions, this topic does not describe some returned fields such as Config and Region for the operation. Alibaba Cloud will delete these fields in the future. Sample requests

```
https://r-kvstore.aliyuncs.com/?Action=DescribeInstanceAttribute &InstanceId=r-bp1zxszhcgatnx**** &Common request parameters
```

Sample responses XML format

```xml
<DescribeInstanceAttributeResponse>
      <Instances>
            <DBInstanceAttribute>
                  <Connections>10000</Connections>
                  <ResourceGroupId>rg-acfmyiu4ekp****</ResourceGroupId>
                  <Config>{"EvictionPolicy":"volatile-lru","hash-max-ziplist-entries":512,"
zset-max-ziplist-entries":128,"list-max-ziplist-entries":512,"list-max-ziplist-value":64,"z set-max-ziplist-value":64,"set-max-intset-entries":512,"hash-max-ziplist-value":64}</Config
```

`>`

```xml
                  <Port>6379</Port>
                  <HasRenewChangeOrder>false</HasRenewChangeOrder>
                  <ZoneType>singlezone</ZoneType>
                  <ConnectionDomain>r-bp1wcw2rlw76acc5k****.redis.rds.aliyuncs.com</Connect
ionDomain>
                  <MaintainEndTime>22:00Z</MaintainEndTime>
                  <Capacity>1024</Capacity>
                  <QPS>100000</QPS>
```

```xml
                  <PrivateIp>172.16.49.***</PrivateIp>
                  <SecurityIPList>127.0.0.1</SecurityIPList>
                  <InstanceStatus>Normal</InstanceStatus>
                  <NetworkType>VPC</NetworkType>
                  <Bandwidth>10</Bandwidth>
                  <PackageType>standard</PackageType>
                  <InstanceReleaseProtection>false</InstanceReleaseProtection>
                  <InstanceType>Redis</InstanceType>
                  <AvailabilityValue>100.0%</AvailabilityValue>
                  <Engine>Redis</Engine>
                  <MaintainStartTime>18:00Z</MaintainStartTime>
                  <Tags>
                        <Tag>
                              <Value>Community Edition</Value>
                              <Key>Type</Key>
                        </Tag>
                  </Tags>
                  <ArchitectureType>standard</ArchitectureType>
                  <EngineVersion>5.0</EngineVersion>
                  <ZoneId>cn-hangzhou-f</ZoneId>
                  <InstanceId>r-bp1wcw2rlw76ac****</InstanceId>
                  <VSwitchId>vsw-bp1w9ouei2nm66qlz****</VSwitchId>
                  <CreateTime>2020-03-31T14:56:22Z</CreateTime>
                  <InstanceClass>redis.logic.sharding.drredissdb1g.1db.0rodb.4proxy.default
</InstanceClass>
                  <AuditLogRetention>7</AuditLogRetention>
                  <IsRds>true</IsRds>
                  <ReplicationMode>master-slave</ReplicationMode>
                  <InstanceName>CommunityEditionMasterReplica50</InstanceName>
                  <VpcId>vpc-bp1opxu1zkhn00gzv****</VpcId>
                  <ChargeType>PostPaid</ChargeType>
                  <VpcAuthMode>Open</VpcAuthMode>
                  <NodeType>double</NodeType>
                  <VpcCloudInstanceId>r-bp1wcw2rlw76ac****</VpcCloudInstanceId>
                  <RegionId>cn-hangzhou</RegionId>
            </DBInstanceAttribute>
      </Instances>
      <RequestId>D67A69DF-C1FC-4B01-B239-B17888CCFD2A</RequestId>
</DescribeInstanceAttributeResponse>
```

JSON format `{`

```json
 "Instances": {
  "DBInstanceAttribute": [
```

`{`

```json
    "Connections": 10000,
    "ResourceGroupId": "rg-acfmyiu4ekp****",
    "Config": "{\"EvictionPolicy\":\"volatile-lru\",\"hash-max-ziplist-entries\":512,\"zset
-max-ziplist-entries\":128,\"list-max-ziplist-entries\":512,\"list-max-ziplist-value\":64,\ "zset-max-ziplist-value\":64,\"set-max-intset-entries\":512,\"hash-max-ziplist-value\":64}"
```

`,`

```json
    "Port": 6379,
    "HasRenewChangeOrder": "false",
```

```json
                "ZoneType":"singlezone",
    "ConnectionDomain": "r-bp1wcw2rlw76acc5k****.redis.rds.aliyuncs.com",
    "MaintainEndTime": "22:00Z",
    "Capacity": 1024,
    "QPS": 100000,
    "PrivateIp": "172.16.49.***",
    "SecurityIPList": "127.0.0.1",
    "InstanceStatus": "Normal",
    "NetworkType": "VPC",
    "Bandwidth": 10,
    "PackageType": "standard",
    "InstanceReleaseProtection": false,
    "InstanceType": "Redis",
    "AvailabilityValue": "100.0%",
    "Engine": "Redis",
    "MaintainStartTime": "18:00Z",
    "Tags": {
     "Tag": [
```

`{`

```json
       "Value": "Community Edition",
       "Key": "Type"
```

`]` `},`

```json
    "ArchitectureType": "standard",
    "EngineVersion": "5.0",
    "ZoneId": "cn-hangzhou-f",
    "InstanceId": "r-bp1wcw2rlw76ac****",
    "VSwitchId": "vsw-bp1w9ouei2nm66qlz****",
    "CreateTime": "2020-03-31T14:56:22Z",
    "InstanceClass": "redis.logic.sharding.drredissdb1g.1db.0rodb.4proxy.default",
    "AuditLogRetention": "7",
    "IsRds": true,
    "ReplicationMode": "master-slave",
    "InstanceName": "CommunityEditionMasterReplica50",
    "VpcId": "vpc-bp1opxu1zkhn00gzv****",
    "ChargeType": "PostPaid",
    "VpcAuthMode": "Open",
    "NodeType": "double",
    "VpcCloudInstanceId": "r-bp1wcw2rlw76ac****",
    "RegionId": "cn-hangzhou"
```

`]` `},`

```json
 "RequestId": "D67A69DF-C1FC-4B01-B239-B17888CCFD2A"
```

#### DescribeInstances

Queries information about one or more KVStore for Redis instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DescribeInst ances | The operation that you want to perform. Set this parameter to DescribeInstances. |
| InstanceIds | String | No | r- n8r8c5119d2 e**** | The globally unique identifier (GUID) of the KVStore for Redis instance. Not e If you specify multiple instance IDs, separate the instance IDs with commas (,). If the parameter value is left blank, all instances that belong to the specified account are displayed by default. |
| InstanceStat us | String | No | Normal | Specifies the status of the instances to be returned. Valid values: Normal Creating Changing Inactive |
| RegionId | String | Yes | cn- hangzhou | The region ID of the instance. You can call DescribeRegions to query the latest region list. |
| InstanceTyp e | String | No | Redis | Specifies the engine type of the instances to be returned. Valid values: Memcache Redis |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Valid values: 1 to 50. Default value: 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NetworkTyp e | String | No | VPC | Specifies the network type of the instances to be returned. Valid values: Classic VPC |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| Instances | List | N/A | Details about instances. For more information, see Parameters of an instance. |
| TotalCount | Integer | 1 | The total number of instances. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries per page. |

Parameters of an instance

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceId | String | r- n8r8c5119d2e** ** | The globally unique identifier (GUID) of the KVStore for Redis instance. |
| InstanceName | String | testdb | The name of the instance. |
| Capacity | Long | 512 | The capacity of the instance. Unit: MB. |
| InstanceClass | String | redis.master.mi d.default | The type of the instance. |
| Bandwidth | Long | 128 | The bandwidth threshold of the instance. Unit: Mbit/s. |
| Connections | Long | 300 | The maximum connections allowed to the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConnectionDom ain | String | de5d88e34d00* ***.m.cnhzalicm 10pub001.r- kvstore.exampl e.com | The endpoint of the instance. This endpoint only supports connections over an internal network. |
| Port | Int | 11211 | The port of the instance. |
| UserName | String | testuser | The account for the instance. |
| RegionId | String | cn-qingdao | The region ID of the instance. |
| ZoneId | String | cn-qingdao-b | The zone ID of the instance. |
| InstanceStatus | String | Normal | The status of the instance. Valid values: Normal Creating Changing Inactive Transforming BackupRecovering MinorVersionUpgrading |
| ChargeType | String | PostPaid | The billing method of the instance. Valid values: PrePaid and PostPaid. |
| CreateTime | String | 2019-03- 06T10:42:03Z | The time when the instance was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| EndTime | String | 2019-04- 06T10:42:03Z | The time when the subscription instance expires. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| NetworkType | String | VPC | The network type of the instance. Valid values: Classic and VPC. |
| VpcId | String | vpc- bp1nme44gek3 4slfc**** | The ID of the VPC to which the instance belongs. |
| VSwitchId | String | vsw- bp1e7clcw529l 773d**** | The ID of the vSwitch to which the instance belongs. |
| PrivateIpAddr | String | 172.16.**.*** | The private IP address of the instance. |

Not e Due to the compatibility with earlier versions, this topic does not describe some returned fields such as Config for the operation. Alibaba Cloud will delete these fields in the future. Sample requests

```
https://r-kvstore.example.com ?<Common request parameters> &Action=DescribeInstances &PageNumber=1 &PageSize=10 &InstanceId=r-n8r8c5119d2e****
```

Sample responses XML format

```xml
<DescribeInstancesResponse>
    <Instances>
        <Instance>
            <Bandwidth>128</Bandwidth>
            <Capacity>512</Capacity>
            <ConnectionDomain>de5d88e34d00****.m.cnhzalicm10pub001.r-kvstore.example.com</C
onnectionDomain>
            <Connections>300</Connections>
            <ZoneId>cn-qingdao-b</ZoneId>
            <InstanceId>r-n8r8c5119d2e****</InstanceId>
            <InstanceName>testdb</InstanceName>
            <InstanceStatus>Available</InstanceStatus>
            <InstanceClass>redis.master.mid.default</InstanceClass>
            <Port>11211</Port>
            <RegionId>cn-qingdao</RegionId>
            <UserName>testuser</UserName>
            <NetworkType>CLASSSIC</NetworkType>
            <ChargeType> PostPaid</ChargeType>
        </Instance>
    </Instances>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TotalCount>1</TotalCount>
    <RequestId>969D0A1D-C91A-4837-9F70-49785DF9BDCE</RequestId>
</DescribeInstancesResponse>
```

JSON format `{`

```json
    "Instances" : {
        "Instance" : [{
                "Bandwidth" : 128,
                "Capacity" : 512,
                "ConnectionDomain" : "de5d88e34d00****.m.cnhzalicm10pub001.r-kvstore.exampl
e.com",
                "Connections" : 300,
                "ZoneId" : "cn-qingdao-b",
                "InstanceId" : "r-n8r8c5119d2e****",
                "InstanceName" : "testdb",
                "InstanceStatus" : "Available",
                 "InstanceClass" : "redis.master.mid.default",
                "Port" : 11211,
                "RegionId" : "cn-qingdao",
                "UserName" : "testuser"
                "NetworkType":"CLASSSIC"
"ChargeType":" PostPaid"
```

`]` `},`

```json
    "PageNumber" : 1,
    "PageSize" : 10,
    "TotalCount" : 1,
    "RequestId" : "969D0A1D-C91A-4837-9F70-49785DF9BDCE"
```

#### DescribeRegions

Queries the regions where KVStore for Redis instances can be created. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set this parameter to DescribeRegions. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| RegionIds | List | N/A | The list in which each element contains RegionId and ZoneIds. The value of the ZoneIds parameter is a string in which multiple ZoneIds are separated by commas (,). |

Sample requests

```
https://r-kvstore.aliyuncs.com?Action=DescribeRegions &Common request parameters
```

Sample responses XML format

```xml
<DescribeRegionsResponse>
      <RegionIds>
            <KVStoreRegion>
              <RegionId>cn-hangzhou</RegionId>
              <ZoneIdList>
                    <ZoneId>cn-hangzhou-h</ZoneId>
                    <ZoneId>cn-hangzhou-MAZ10(h,i)</ZoneId>
                    <ZoneId>cn-hangzhou-MAZ9(g,h)</ZoneId>
                    <ZoneId>cn-hangzhou-b</ZoneId>
                    <ZoneId>cn-hangzhou-d</ZoneId>
                    <ZoneId>cn-hangzhou-e</ZoneId>
                    <ZoneId>cn-hangzhou-MAZ6(b,f)</ZoneId>
                    <ZoneId>cn-hangzhou-f</ZoneId>
                    <ZoneId>cn-hangzhou-g</ZoneId>
              </ZoneIdList>
              <RegionEndpoint>r-kvstore.aliyuncs.com</RegionEndpoint>
              <ZoneIds>cn-hangzhou-h,cn-hangzhou-MAZ10(h,i),cn-hangzhou-MAZ9(g,h),cn-hangzh
ou-b,cn-hangzhou-d,cn-hangzhou-e,cn-hangzhou-MAZ6(b,f),cn-hangzhou-f,cn-hangzhou-g</ZoneIds
```

`>`

```xml
              <LocalName>China (Hangzhou)</LocalName>
            </KVStoreRegion>
      </RegionIds>
      <RequestId>AD425AD3-CC7B-4EE2-A5CB-2F61BA73****</RequestId>
</DescribeRegionsResponse>
```

JSON format `{`

```json
    "RegionIds": {
        "KVStoreRegion": [{
                "RegionId": "cn-hangzhou",
                "ZoneIdList": {
                    "ZoneId": [
                        "cn-hangzhou-h",
                        "cn-hangzhou-MAZ10(h,i)",
                        "cn-hangzhou-MAZ9(g,h)",
                        "cn-hangzhou-b",
                        "cn-hangzhou-d",
                        "cn-hangzhou-e",
                        "cn-hangzhou-MAZ6(b,f)",
                        "cn-hangzhou-f",
                        "cn-hangzhou-g"
```

`]` `},`

```json
                "RegionEndpoint": "r-kvstore.aliyuncs.com",
                "ZoneIds": "cn-hangzhou-h,cn-hangzhou-MAZ10(h,i),cn-hangzhou-MAZ9(g,h),cn-h
angzhou-b,cn-hangzhou-d,cn-hangzhou-e,cn-hangzhou-MAZ6(b,f),cn-hangzhou-f,cn-hangzhou-g",
                "LocalName": "China (Hangzhou)"
```

`]` `},`

```json
    "RequestId": "AD425AD3-CC7B-4EE2-A5CB-2F61BA73****"
```

#### DescribeSecurityIps

Queries IP whitelists of a KVStore for Redis instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DescribeSecurityIp s | The operation that you want to perform. Set this parameter to DescribeSecurityIp s. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| SecurityIpGroups | List | N/A | Details about IP whitelists. |

Parameters of SecurityIpGroups

| Parameter | Type | Example |   | Description |   |   |
|---|---|---|---|---|---|---|
| SecurityIpGroupName | String | default |   | The name of the IP whitelist. |   |   |
| SecurityIpList | String | 100.100.202.***/24,10.1 0.10.*** |   | The IP addresses in the IP whitelist. A maximum of 1,000 IP addresses or CIDR blocks are allowed. IP addresses are separated with commas (,). Supported formats are IP addresses such as 0.0.0.0/0 and 10.23.12.24 , or CIDR blocks such as 10.23.12.24/24 . /24 indicates the length of the IP address prefix. The IP address prefix can consist of 1 to 32 bits. |   |   |
|   |   |   |   |   | 0.0.0.0/0 and |   |
|   |   |   |   | 10.23.12.24 |   |   |

Sample requests

```
https://r-kvstore.aliyuncs.com/?Action=DescribeSecurityIps &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeSecurityIpsResponse>
      <SecurityIpGroups>
            <SecurityIpGroup>
                  <SecurityIpList>127.0.0.1</SecurityIpList>
                  <SecurityIpGroupAttribute></SecurityIpGroupAttribute>
                  <SecurityIpGroupName>default</SecurityIpGroupName>
            </SecurityIpGroup>
            <SecurityIpGroup>
                  <SecurityIpList>100.100.202.***/24,10.10.10.***</SecurityIpList>
                  <SecurityIpGroupAttribute>hidden</SecurityIpGroupAttribute>
                  <SecurityIpGroupName>rds_replica_group</SecurityIpGroupName>
            </SecurityIpGroup>
      </SecurityIpGroups>
      <RequestId>EFC9161F-15E3-4A6E-8A99-C09916D1****</RequestId>
</DescribeSecurityIpsResponse>
```

JSON format `{`

```json
    "SecurityIpGroups": {
        "SecurityIpGroup": [
```

`{`

```json
                "SecurityIpList": "127.0.0.1",
                "SecurityIpGroupAttribute": "",
                "SecurityIpGroupName": "default"
```

`},` `{`

```json
                "SecurityIpList": "100.100.202.***/24,10.10.10.***",
                "SecurityIpGroupAttribute": "hidden",
                "SecurityIpGroupName": "rds_replica_group"
```

`]` `},`

```json
    "RequestId": "EFC9161F-15E3-4A6E-8A99-C09916D1****"
```

#### FlushInstance

Deletes the data of a KVStore for Redis instance. Deleted data cannot be recovered. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | FlushInstance | The operation that you want to perform. Set this parameter to FlushInstance. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The globally unique identifier (GUID) of the KVStore for Redis instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

Sample requests

```
https://r-kvstore.aliyuncs.com/?Action=FlushInstance &InstanceId=r-bp1zxszhcgatnx**** &Common request parameters
```

Sample responses XML format

```xml
<FlushInstanceResponse>
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B3E76</RequestId>
</FlushInstanceResponse>
```

JSON format `{`

```json
  "RequestId":"8D0C0AFC-E9CD-47A4-8395-5C31BF9B3E7"
```

#### ModifyInstanceAttribute

Modifies the attributes of a KVStore for Redis instance such as the name or password. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | ModifyInstanc eAttribute | The operation that you want to perform. Set this parameter to ModifyInstanceAttribute. |
| InstanceId | String | Yes | r- bp1zxszhcgat nx**** | The globally unique identifier (GUID) of the KVStore for Redis instance. |
| InstanceName | String | No | TestInstance | The new name of the instance. The name must be 2 to 128 characters in length. The name must start with a letter. It cannot contain spaces or the following special characters: @ / : = " < > { [ ] } |
| NewPassword | String | No | Qa12345678 | The new password of the instance. The password must be 8 to 30 characters in length and must contain uppercase letters, lowercase letters, and digits. Not e Special characters are not supported, such as ! < > ( ) [ ] { } , ` ~ . - @ # $ % ^ & * _ |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

Sample requests

```
https://r-kvstore.example.com &Action=ModifyInstanceAttribute &InstanceId=r-bp1zxszhcgatnx**** &NewPassword=Qa12345678 &InstanceName=TestInstance &Common request parameters
```

Sample responses XML format

```xml
<ModifyInstanceAttributeResponse>
    <RequestId>E3B35BEA-9EB0-402C-88CF-C46CCCC1EE59</RequestId>
</ModifyInstanceAttributeResponse>
```

JSON format `{`

```json
"RequestId" : "E3B35BEA-9EB0-402C-88CF-C46CCCC1EE59"
```

#### ModifyInstanceMaintainTime

Modifies the maintenance window of a KVStore for Redis instance. Alibaba Cloud maintains the KVStore for Redis instance in the specified maintenance window. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | ModifyInstanceMai ntainTime | The operation that you want to perform. Set this parameter to ModifyInstanceMai ntainTime. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The ID of the instance. |
| MaintainStartTime | String | Yes | 03:00Z | The start time of the maintenance window. |
| MaintainEndTime | String | Yes | 04:00Z | The end time of the maintenance window. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

Sample requests

```
https://r-kvstore.aliyuncs.com/?Action=ModifyInstanceMaintainTime &InstanceId=r-bp1zxszhcgatnx**** &MaintainStartTime=17:00Z &MaintainEndTime=18:00Z &Common request parameters
```

Sample responses XML format

```xml
<ModifyInstanceMaintainTimeResponse>
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B3E76</RequestId>
</ModifyInstanceMaintainTimeResponse>
```

JSON format `{`

```json
    "RequestId": "8D0C0AFC-E9CD-47A4-8395-5C31BF9B3E76"
```

#### ModifyInstanceNetExpireTime

Extends the retention period of the classic network endpoint of a KVStore for Redis instance. You can call this operation after you change the network type of the KVStore for Redis instance from classic network to VPC with the classic network endpoint retained. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | ModifyInstanceNet ExpireTime | The operation that you want to perform. Set this parameter to ModifyInstanceNet ExpireTime. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The ID of the instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ConnectionString | String | Yes | r- bp1zxszhcgatnx** **.redis.rds.aliyunc s.com | The endpoint of the classic network. |
| ClassicExpiredDays | String | Yes | 14 | The number of the days when the classic network IP is retained. Valid values: 14, 30, 60, and 120. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

Sample requests

```
https://r-kvstore.aliyuncs.com/?Action=ModifyInstanceNetExpireTime &ClassicExpiredDays=14 &ConnectionString=r-bp1zxszhcgatnx****.redis.rds.aliyuncs.com &InstanceId=r-bp1zxszhcgatnx**** &Common request parameters
```

Sample responses XML format

```xml
<ModifyInstanceNetExpireTimeResponse>
      <RequestId>9C4AF387-1EA3-4C84-8013-3F6B973EDDF5</RequestId>
</ModifyInstanceNetExpireTimeResponse>
```

JSON format `{`

```json
    "RequestId": "9C4AF387-1EA3-4C84-8013-3F6B973EDDF5",
```

#### ModifySecurityIps

Modifies the IP addresses in a whitelist of a KVStore for Redis instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | ModifySecurityIps | The operation that you want to perform. Set this parameter to ModifySecurityIps. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The globally unique identifier (GUID) of the KVStore for Redis instance. |
| SecurityIps | String | Yes | 100.64.***.0/24,10 .101.11.*** | The IP addresses to be modified. |
| SecurityIpGroupNa me | String | Yes | default | The name of the IP whitelist. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

Sample requests

```
https://r-kvstore.aliyuncs.com/?Action=ModifySecurityIps &InstanceId=r-bp1zxszhcgatnx**** &SecurityIps=100.64.***.0/24,10.101.11.*** &<Common request parameters>
```

Sample responses XML format

```xml
<ModifySecurityIpsResponse>
      <RequestId>AAAF99B1-69ED-4E80-8CD5-272C09E4****</RequestId>
</ModifySecurityIpsResponse>
```

JSON format `{`

```json
    "RequestId" : "AAAF99B1-69ED-4E80-8CD5-272C09E4****"
```

#### SwitchNetwork

Changes the network type of a KVStore for Redis instance from classic network to VPC. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | SwitchNetwork | The operation that you want to perform. Set this parameter to SwitchNetwork. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The ID of the instance. |
| TargetNetworkTy pe | String | Yes | VPC | The type of the network that you want to switch to. VPC Classic You can only switch from classic network to VPC. In this case, this parameter must be set to VPC. |
| VpcId | String | No | vpc- bp1nme44gek34sl fc**** | The ID of the VPC that you want to switch to. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VSwitchId | String | No | vsw- bp1e7clcw529l773 d**** | The ID of the vSwitch in the VPC that you want to switch to. This parameter is required if the ID of the VPC is specified. |
| RetainClassic | String | No | True | Specifies whether to retain the classic network IP address. Default value: False. Valid values: True: The classic network IP address is retained. False: The classic network IP address is not retained. |
| ClassicExpiredDays | String | No | 30 | The number of the days when the classic network IP is retained. Unit: days. Valid values: 14, 30, 60, and 120. If you set the RetainClassic parameter to true, you must also specify this parameter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

Sample requests

```
https://r-kvstore.aliyuncs.com?Action=SwitchNetwork &InstanceId=r-bp1zxszhcgatnx**** &TargetNetworkType=VPC &VpcId=vpc-bp1nme44gek34slfc**** &VSwitchId=vsw-bp1e7clcw529l773d**** &RetainClassic=True &ClassicExpiredDays=30 &<Common request parameters>
```

Sample responses XML format

```xml
<SwitchNetworkResponse>
      <TaskId>578678678</TaskId>
      <requestId>F0997EE8-F4C2-4503-9168-85177ED78C70</requestId>
</SwitchNetworkResponse>
```

JSON format `{`

```json
    "TaskId":"578678678",
    "requestId": "F0997EE8-F4C2-4503-9168-85177ED78C70"
```

### Backup and recovery

#### CreateBackup

Backs up a KVStore for Redis instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | CreateBackup | The operation that you want to perform. Set this parameter to CreateBackup. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

Sample requests

```
https://r-kvstore.aliyuncs.com/?Action=CreateBackup &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

Sample responses XML format

```xml
<CreateBackupResponse>
      <RequestId>2FF6158E-3394-4A90-B634-79C49184****</RequestId>
      <BackupJobID>1162****</BackupJobID>
</CreateBackupResponse>
```

JSON format `{`

```json
    "RequestId": "2FF6158E-3394-4A90-B634-79C49184****",
    "BackupJobID": "1162****"
```

#### ModifyBackupPolicy

Modifies the backup policy of a KVStore for Redis instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | ModifyBackupPolic y | The operation that you want to perform. Set this parameter to ModifyBackupPolic y. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The ID of the instance. |

| Developer Guide·API re | ference |   |   |   | ApsaraDB for Redi |   | s |
|---|---|---|---|---|---|---|---|
| Parameter | Type | Required | Example |   | Description |   |   |
| PreferredBackupTi me | String | Yes | 00:00Z-04:00Z |   | The time to execute backup. Specify the time in the HH:mmZ- HH:mmZ format. |   |   |
|   |   |   |   |   |   | HH:mmZ- |   |
|   |   |   |   |   | HH:mmZ |   |   |
| PreferredBackupPe riod | String | Yes | Tuesday |   | The days of the week to execute backup. Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

Sample requests

```
https://r-kvstore.aliyuncs.com/?Action=ModifyBackupPolicy &InstanceId=r-bp1zxszhcgatnx**** &PreferredBackupTime=00:00Z-04:00Z &PreferredBackupPeriod=Tuesday &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyBackupPolicyResponse>
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B****</RequestId>
</ModifyBackupPolicyResponse>
```

JSON format `{`

```json
    "RequestId":"8D0C0AFC-E9CD-47A4-8395-5C31BF9B****"
```

#### DescribeBackupPolicy

Queries the backup policy of a KVStore for Redis instance. The backup policy includes information such as the backup cycle and the backup time. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DescribeBackupPol icy | The operation that you want to perform. Set this parameter to DescribeBackupPol icy. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| BackupRetentionPeriod | String | 7 | The backup retention period. Unit: days. |
| PreferredBackupTime | String | 05:00Z-06:00Z | The time to execute backup. The time is in the HH:mmZ-HH:mmZ format. |
| PreferredBackupPeriod | String | Monday,Tuesday,Wedne sday,Thursday,Friday,Sa turday,Sunday | The days of the week to execute backup. Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PreferredNextBackupTi me | String | 2019-03-14T05:28Z | The scheduled time for the next backup. |

Sample requests

```
https://r-kvstore.aliyuncs.com/?Action=DescribeBackupPolicy &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeBackupPolicyResponse>
      <PreferredBackupPeriod>Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday</Pref
erredBackupPeriod>
      <RequestId>90B82DB7-FB28-4CC2-ADBF-1F8659F3****</RequestId>
      <PreferredNextBackupTime>2018-10-26T19:05Z</PreferredNextBackupTime>
      <PreferredBackupTime>19:00Z-20:00Z</PreferredBackupTime>
      <BackupRetentionPeriod>7</BackupRetentionPeriod>
</DescribeBackupPolicyResponse>
```

JSON format `{`

```json
 "PreferredBackupPeriod": "Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday",
 "RequestId": "90B82DB7-FB28-4CC2-ADBF-1F8659F3****",
 "PreferredNextBackupTime": "2018-10-26T19:05Z",
 "PreferredBackupTime": "19:00Z-20:00Z",
 "BackupRetentionPeriod": "7"
```

#### DescribeBackups

Queries the backup files of a KVStore for Redis instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackups | The operation that you want to perform. Set this parameter to DescribeBackups. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The ID of the instance. |
| BackupId | String | No | 11611111 | The ID of the backup set. |
| PageSize | String | Yes | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. |
| PageNumber | String | Yes | 1 | The number of the page to return. The value must be an integer that is greater than 0. |
| StartTime | String | Yes | 2019-03- 11T10:00Z | The beginning of the time range to query. |
| EndTime | String | Yes | 2019-03- 14T18:00Z | The end of the time range to query. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| Backups | List | N/A | Details about of backup files. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| TotalCount | Integer | 5 | The total number of backup files that were returned. |

| eveloper Guide·API refere | nce |   | ApsaraDB for Redi |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageSize | Integer | 30 | The number of entries returned per page. |

Parameters of a backup file

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupId | String | 111111111 | The ID of the backup set. |
| BackupDBNames | String | all | The name of the database that was backed up. |
| BackupStatus | String | Success | The status of the backup set. Success Failed |
| BackupStartTime | String | 2019-03-14T05:28:50Z | The time when the backup started. |
| BackupEndTime | String | 2019-03-14T05:31:13Z | The time when the backup ended. |
| BackupType | String | FullBackup | The type of the backup. Valid values: FullBackup IncrementalBackup |
| BackupMode | String | Automated | The mode in which data was backed up. Valid values: Automated Manual |
| BackupMethod | String | Physical | The method of the backup. Valid values: Logical Physical |
| BackupDownloadURL | String | https://rdsbak-hk45- v2.oss-cn- hongkong.aliyuncs.com /******** | The download URL of the backup file. |
| BackupSize | String | 1024 | The size of the backup set. |

Sample requests

```
https://r-kvstore.aliyuncs.com/?Action=DescribeBackups &InstanceId=r-bp1zxszhcgatnx**** &StartTime=2019-03-11T10:00Z &EndTime=2019-03-14T18:00Z &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeBackupsResponse>
      <TotalCount>1</TotalCount>
      <RequestId>721E2D39-351D-40E2-BF7C-B5075B0A****</RequestId>
      <PageSize>30</PageSize>
      <PageNumber>1</PageNumber>
      <Backups>
            <Backup>
                  <BackupMethod>Physical</BackupMethod>
                  <EngineVersion>4.0</EngineVersion>
                  <BackupIntranetDownloadURL>http://rdsbak-hz-v3.oss-cn-hangzhou-internal.a
liyuncs.com/********</BackupIntranetDownloadURL>
                  <BackupMode>Automated</BackupMode>
                  <BackupSize>2263040</BackupSize>
                  <BackupId>775661111</BackupId>
                  <NodeInstanceId>r-bp12fdcf4dea****</NodeInstanceId>
                  <BackupDBNames>all</BackupDBNames>
                  <BackupDownloadURL>http://rdsbak-hz-v3.oss-cn-hangzhou.aliyuncs.com/*****
***</BackupDownloadURL>
                  <BackupEndTime>2020-10-30T17:31:26Z</BackupEndTime>
                  <BackupStartTime>2020-10-30T17:28:28Z</BackupStartTime>
                  <BackupType>FullBackup</BackupType>
                  <BackupStatus>Success</BackupStatus>
            </Backup>
      </Backups>
</DescribeBackupsResponse>
```

JSON format `{`

```json
    "TotalCount": 1,
    "RequestId": "721E2D39-351D-40E2-BF7C-B5075B0A****",
    "PageSize": 30,
    "PageNumber": 1,
    "Backups": {
        "Backup": [
```

`{`

```json
                "BackupMethod": "Physical",
                "EngineVersion": "4.0",
                "BackupIntranetDownloadURL": "http://rdsbak-hz-v3.oss-cn-hangzhou-internal.
aliyuncs.com/********",
                "BackupMode": "Automated",
                "BackupSize": 2263040,
                "BackupId": 775661111,
                "NodeInstanceId": "r-bp12fdcf4dea****",
                "BackupDBNames": "all",
                "BackupDownloadURL": "http://rdsbak-hz-v3.oss-cn-hangzhou.aliyuncs.com/****
****",
                "BackupEndTime": "2020-10-30T17:31:26Z",
                "BackupStartTime": "2020-10-30T17:28:28Z",
                "BackupType": "FullBackup",
                "BackupStatus": "Success"
```

`]`

#### RestoreInstance

Restores the data of a KVStore for Redis instance from a backup file to the instance. If you use the operation together with the data flashback feature, you can restore data of a specified key to a specified point in time that is accurate to the second. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | RestoreInstance | The operation that you want to perform. Set this parameter to RestoreInstance. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The ID of the instance. |

| psaraDB for Redis |   |   | Develop | er Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BackupId | String | Yes | 78241**** | The ID of the backup set. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

Sample requests

```
http(s)://r-kvstore.aliyuncs.com/?Action=RestoreInstance &InstanceId=r-bp1zxszhcgatnx**** &RestoreType=1 &RestoreTime=2021-07-06T07:25:57Z &FilterKey=key:00000007198* &Common request parameters
```

Sample responses XML format

```xml
<RestoreInstanceResponse>
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B****</RequestId>
</RestoreInstanceResponse>
```

JSON format `{`

```json
    "RequestId": "8D0C0AFC-E9CD-47A4-8395-5C31BF9B****"
```

### Manage monitoring

#### DescribeMonitorItems

Queries the metrics of a KVStore for Redis instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DescribeMonitorIte ms | The operation that you want to perform. Set the value to DescribeMonitorIte ms. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| MonitorItems | List | N/A | Details about metrics. |

Sample requests

```
https://r-kvstore.aliyuncs.com/?Action=DescribeMonitorItems &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeMonitorItemsResponse>
    <MonitorItems>
        <MonitorItem>
            <MonitorKey>GetQ</MonitorKey>
            <Unit>Counts/s</Unit>
        </MonitorItem>
        <MonitorItem>
            <MonitorKey>Flush</MonitorKey>
            <Unit>Counts/s</Unit>
        </MonitorItem>
        <MonitorItem>
            <MonitorKey>UsedMemCache</MonitorKey>
            <Unit>Bytes</Unit>
        </MonitorItem>
        <MonitorItem>
            <MonitorKey>ReplaceQ</MonitorKey>
            <Unit>Counts/s</Unit>
        </MonitorItem>
    </MonitorItems>
    <RequestId>B906A893-58A3-4644-AC2D-A2C9B08706C1</RequestId>
</DescribeMonitorItemsResponse>
```

JSON format `{`

```json
    "MonitorItems" : {
        "MonitorItem" : [{
                "MonitorKey" : "GetQ",
                "Unit" : "Counts/s"
            }, {
                "MonitorKey" : "Flush",
                "Unit" : "Counts/s"
            }, {
                "MonitorKey" : "UsedMemCache",
                "Unit" : "Bytes"
            }, {
                "MonitorKey" : "ReplaceQ",
                "Unit" : "Counts/s"
```

`]` `},`

```json
    "RequestId" : "B906A893-58A3-4644-AC2D-A2C9B08706C1"
```

#### DescribeHistoryMonitorValues

Queries the monitoring history of a KVStore for Redis instance. Request parameters

| Parameter | Type | Required | Example |   | Description |   |   |
|---|---|---|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A |   | For more information, see Common parameters. |   |   |
| Action | String | Yes | DescribeHistoryMo nitorValues |   | The operation that you want to perform. Set this parameter to DescribeHistoryMo nitorValues. |   |   |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** |   | The ID of the instance. |   |   |
| StartTime | String | Yes | 2018-10- 18T12:00:00Z |   | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. |   |   |
|   |   |   |   |   |   | YYYY-MM- |   |
|   |   |   |   |   | DDThh:mm:ssZ |   |   |
| EndTime | String | Yes | 2018-10- 19T12:00:00Z |   | The end of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. The end of the time range must be later than or equal to the beginning of the time range. |   |   |
|   |   |   |   |   |   | YYYY-MM- |   |
|   |   |   |   | 0Z | DDThh:mm:ssZ |   |   |
| IntervalForHistory | String | Yes | 01m |   | The sampling interval of the monitoring data. Valid values: 01, 05, 15, and 60. Unit: minutes. The sampling points are collected every N minutes. |   |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| MonitorKeys | String | No | CpuUsage | The keys of the metrics. You can query the value of the parameter by calling the DescribeMonitorIte ms operation. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| MonitorHistory | String | {\"2020-11- 18T00:00:00Z\": {\"CpuUsage\":\"0.30\"} ,\"2020-11- 18T00:02:00Z\": {\"CpuUsage\":\"0.60\"} ,\"2020-11- 18T00:03:00Z\": {\"CpuUsage\":\"0.60\"} } | The metrics returned in the JSON format. For more information, see DescribeMonitorItems. Not e To improve the data transmission efficiency, only metrics whose values are not 0 are returned. Metrics not displayed are all set to the default value 0. |

Sample requests

```
https://r-kvstore.aliyuncs.com/?Action=DescribeHistoryMonitorValues &InstanceId=r-bp1zxszhcgatnx**** &StartTime=2018-10-18T12:00:00Z &EndTime=2018-10-18T12:03:00Z &IntervalForHistory=01m &MonitorKeys=CpuUsage &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeHistoryMonitorValuesResponse>
      <MonitorHistory>{"2020-11-18T00:00:00Z":{"CpuUsage":"0.30"},"2020-11-18T00:02:00Z":{"
CpuUsage":"0.60"},"2020-11-18T00:03:00Z":{"CpuUsage":"0.60"}}</MonitorHistory>
      <RequestId>689E8093-3094-4DC2-A2A2-30D40097****</RequestId>
</DescribeHistoryMonitorValuesResponse>
```

JSON format `{`

```json
    "MonitorHistory": "{\"2020-11-18T00:00:00Z\":{\"CpuUsage\":\"0.30\"},\"2020-11-18T00:02
:00Z\":{\"CpuUsage\":\"0.60\"},\"2020-11-18T00:03:00Z\":{\"CpuUsage\":\"0.60\"}}",
    "RequestId": "689E8093-3094-4DC2-A2A2-30D40097****"
```

### Manage parameters

#### DescribeInstanceConfig

Queries the configuration parameters of a KVStore for Redis instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DescribeInstanceC onfig | The operation that you want to perform. Set this parameter to DescribeInstanceC onfig. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The ID of the instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Config | String | {"#no loose statistics- _ _ cmds":"SET,GET","Evicti onPolicy":"volatile- lru","hash-max-ziplist- entries":512,"slowlog- log-slower- than":"1000","notify- keyspace- events":"$","zset-max- ziplist- entries":128,"list-max- ziplist- entries":512,"list-max- ziplist-value":64,"zset- max-ziplist- value":64,"set-max- intset- entries":512,"hash-max- ziplist- value":64,"#no loose d _ _ isabled- commands":"flushall"} | The configuration parameters of the instance. For more information, see Instance configurations. |

Sample requests

```
https://r-kvstore.aliyuncs.com/?Action=DescribeInstanceConfig &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

Sample responses XML format

```xml
<DescribeInstanceConfigResponse>
      <RequestId>4E2C08F6-2D11-4ECD-9A4C-27EF2D3D****</RequestId>
      <Config>{"#no_loose_statistics-cmds":"SET,GET","EvictionPolicy":"volatile-lru","hash-
max-ziplist-entries":512,"slowlog-log-slower-than":"1000","notify-keyspace-events":"$","zse t-max-ziplist-entries":128,"list-max-ziplist-entries":512,"list-max-ziplist-value":64,"zset -max-ziplist-value":64,"set-max-intset-entries":512,"hash-max-ziplist-value":64,"#no_loose_ disabled-commands":"flushall"}</Config> </DescribeInstanceConfigResponse>
```

JSON format `{`

```json
    "RequestId": "4E2C08F6-2D11-4ECD-9A4C-27EF2D3D****",
    "Config": "{\"#no_loose_statistics-cmds\":\"SET,GET\",\"EvictionPolicy\":\"volatile-lru
\",\"hash-max-ziplist-entries\":512,\"slowlog-log-slower-than\":\"1000\",\"notify-keyspaceevents\":\"$\",\"zset-max-ziplist-entries\":128,\"list-max-ziplist-entries\":512,\"list-max -ziplist-value\":64,\"zset-max-ziplist-value\":64,\"set-max-intset-entries\":512,\"hash-max -ziplist-value\":64,\"#no_loose_disabled-commands\":\"flushall\"}"
```

#### ModifyInstanceConfig

Modifies configuration parameters of a KVStore for Redis instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | ModifyInstanceCo nfig | The operation that you want to perform. Set this parameter to ModifyInstanceCo nfig. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx** ** | The ID of the instance. |
| Config | String | Yes | {"EvictionPolicy":"v olatile-lru","list- max-ziplist- entries":512,"zset -max-ziplist- entries":128,"hash -max-ziplist- entries":512,"hash -max-ziplist- value":64,"list- max-ziplist- value":64,"set- max-intset- entries":512,"zset -max-ziplist- value":64} | The configuration parameters of the instance (JSON string). For more information, see Instance configurations. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

Sample requests

```
https://r-kvstore.aliyuncs.com/?Action=ModifyInstanceConfig &InstanceId=r-bp1zxszhcgatnx**** &Config={"EvictionPolicy":"volatile-lru","list-max-ziplist-entries":512,"zset-max-ziplist-e ntries":128,"hash-max-ziplist-entries":512,"hash-max-ziplist-value":64,"list-max-ziplist-va lue":64,"set-max-intset-entries":512,"zset-max-ziplist-value":64} &<Common request parameters>
```

Sample responses XML format

```xml
<ModifyInstanceConfigResponse>
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B****</RequestId>
</ModifyInstanceConfigResponse>
```

JSON format `{`

```json
  "requestId":"8D0C0AFC-E9CD-47A4-8395-5C31BF9B****"
```

### Appendixes

#### Instance types

KVStore for Redis provides instances of Community Edition and performance-enhanced instances of Enhanced Edition. Performance-enhanced instances of Enhanced Edition support the standard, cluster, and read/write splitting architectures. Instances of Community Edition support the standard and cluster architectures. This topic describes the specifications of different instance types, such as memory capacity, maximum number of connections, and maximum bandwidth value. Calculation rules for bandwidth If network resources are sufficient, bandwidth is unlimited. However, if network resources are insufficient, the bandwidth is limited. The upper limit of the total bandwidth for a cluster instance is 2,048 MB/s. After the upper limit is reached, the bandwidth cannot be increased even if the number of shards is increased. The bandwidth value applies to the upstream and downstream bandwidths. For example, if the bandwidth of an instance is 10 MB/s, the upstream and downstream bandwidths of the instance are both 10 MB/s. The bandwidth in the tables is the internal bandwidth of the KVStore for Redis instance. The Internet bandwidth is determined by the internal bandwidth and is limited by the bandwidth of the connection between the KVStore for Redis instance and the client. We recommend that you connect to the instance over an internal network to maximize performance. Performance-enhanced instances of KVStore for Redis Enhanced Edition Standard master-replica instances

| Specification | InstanceClass (used in API operations) | I/O threads | Connectio ns per second | Maximum connectio ns | Total bandwidt h (MB/s) |
|---|---|---|---|---|---|
| 1 GB master- replica performance- enhanced instance | redis.amber.master.small.mul tithread | 6 | 10000 | 30000 | 96 |
| 2 GB master- replica performance- enhanced instance | redis.amber.master.mid.multit hread | 6 | 10000 | 30000 | 96 |
| 4 GB master- replica performance- enhanced instance | redis.amber.master.stand.mul tithread | 6 | 10000 | 30000 | 96 |
| 8 GB master- replica performance- enhanced instance | redis.amber.master.large.mult ithread | 6 | 10000 | 30000 | 96 |
| 16 GB master- replica performance- enhanced instance | redis.amber.master.2xlarge.m ultithread | 6 | 10000 | 30000 | 96 |
| 32 GB master- replica performance- enhanced instance | redis.amber.master.4xlarge.m ultithread | 6 | 10000 | 30000 | 96 |
| 64 GB master- replica performance- enhanced instance | redis.amber.master.8xlarge.m ultithread | 6 | 10000 | 30000 | 96 |

Cluster instances

| Specification | InstanceClass (used in API operations) | I/O thre ads | Shar ds | Prox y serv ers | Con nect ions per seco nd | Maxi mu m con nect ions | Maxi mu m ban dwi dth valu e per shar d | Tot al ban dwi dth (MB/ s) |
|---|---|---|---|---|---|---|---|---|
| 2 GB cluster performance- enhanced instance (2 shards) | redis.amber.logic.shar ding.1g.2db.0rodb.6p roxy.multithread | 6 | 2 | 4 | 500 00 | 600 00 | 96 | 192 |
| 4 GB cluster performance- enhanced instance (2 shards) | redis.amber.logic.shar ding.2g.2db.0rodb.6p roxy.multithread | 6 | 2 | 4 | 500 00 | 500 00 | 96 | 192 |
| 8 GB cluster performance- enhanced instance (4 shards) | redis.amber.logic.shar ding.2g.4db.0rodb.12 proxy.multithread | 6 | 4 | 4 | 500 00 | 120 000 | 96 | 384 |
| 16 GB cluster performance- enhanced instance (8 shards) | redis.amber.logic.shar ding.2g.8db.0rodb.24 proxy.multithread | 6 | 8 | 8 | 500 00 | 240 000 | 96 | 768 |
| 32 GB cluster performance- enhanced instance (8 shards) | redis.amber.logic.shar ding.4g.8db.0rodb.24 proxy.multithread | 6 | 8 | 8 | 500 00 | 240 000 | 96 | 768 |
| 64 GB cluster performance- enhanced instance (8 shards) | redis.amber.logic.shar ding.8g.8db.0rodb.24 proxy.multithread | 6 | 8 | 8 | 500 00 | 240 000 | 96 | 768 |
| 32 GB cluster performance- enhanced instance (16 shards) | redis.amber.logic.shar ding.2g.16db.0rodb.4 8proxy.multithread | 6 | 16 | 16 | 500 00 | 480 000 | 96 | 153 6 |
| 64 GB cluster performance- enhanced (16 shards) | redis.amber.logic.shar ding.4g.16db.0rodb.4 8proxy.multithread | 6 | 16 | 16 | 500 00 | 480 000 | 96 | 153 6 |
| 128 GB cluster performance- enhanced instance (16 shards) | redis.amber.logic.shar ding.8g.16db.0rodb.4 8proxy.multithread | 6 | 16 | 16 | 500 00 | 480 000 | 96 | 153 6 |

| Developer Guide·API refer | ence |   |   |   |   | A | psaraDB | for Redi |
|---|---|---|---|---|---|---|---|---|

| Specification | InstanceClass (used in API operations) | I/O thre ads | Shar ds | Prox y serv ers | Con nect ions per seco nd | Maxi mu m con nect ions | Maxi mu m ban dwi dth valu e per shar d | Tot al ban dwi dth (MB/ s) |
|---|---|---|---|---|---|---|---|---|
| 256 GB cluster performance- enhanced instance (16 shards) | redis.amber.logic.shar ding.16g.16db.0rodb. 48proxy.multithread | 6 | 16 | 16 | 500 00 | 480 000 | 96 | 153 6 |
| 512 GB cluster performance- enhanced instance (32 shards) | redis.amber.logic.shar ding.16g.32db.0rodb. 96proxy.multithread | 6 | 32 | 32 | 500 00 | 500 000 | 96 | 204 8 |
| 1,024 GB cluster performance- enhanced instance (64 shards) | redis.amber.logic.shar ding.16g.64db.0rodb. 192proxy.multithread | 6 | 64 | 64 | 500 00 | 500 000 | 96 | 204 8 |
| 2,048 GB cluster performance- enhanced instance (128 shards) | redis.amber.logic.shar ding.16g.128db.0rodb .384proxy.multithread | 6 | 128 | 128 | 500 00 | 500 000 | 96 | 204 8 |
| 4,096 GB cluster performance- enhanced instance (256 shards) | redis.amber.logic.shar ding.16g.256db.0rodb .768proxy.multithread | 6 | 256 | 256 | 500 00 | 500 000 | 96 | 204 8 |
| 8,192 GB cluster performance- enhanced instance (256 shards) | redis.amber.logic.shar ding.32g.256db.0rodb .768proxy.multithread | 6 | 256 | 256 | 500 00 | 500 000 | 96 | 204 8 |

Community Edition instances Standard master-replica instances

| Specification | InstanceClass (used in API operations) | Maximum connections | Total bandwidth (MB/s) | CPU |
|---|---|---|---|---|
| 1GB master- replica instance | redis.master.small.default | 10000 | 10 | 1 core |

| Specification | InstanceClass (used in API operations) | Maximum connections | Total bandwidth (MB/s) | CPU |
|---|---|---|---|---|
| 2 GB master- replica instance | redis.master.mid.default | 10000 | 16 | 1 core |
| 4 GB master- replica instance | redis.master.stand.default | 10000 | 24 | 1 core |
| 8 GB master- replica instance | redis.master.large.default | 10000 | 24 | 1 core |
| 16 GB master- replica instance | redis.master.2xlarge.defaul t | 10000 | 32 | 1 core |
| 32 GB master- replica instance | redis.master.4xlarge.defaul t | 10000 | 32 | 1 core |
| 64 GB master- replica instance | redis.master.8xlarge.defaul t | 10000 | 48 | 1 core |

Cluster instances

| Specification | InstanceClass (used in API operations) | Shard s | Maximu m connecti ons | Total bandwid th (MB/s) | CPU |
|---|---|---|---|---|---|
| 16 GB cluster instance | redis.logic.sharding.2g.8db.0rodb.8prox y.default | 8 | 80000 | 768 | 8 cores |
| 32 GB cluster instance | redis.logic.sharding.4g.8db.0rodb.8prox y.default | 8 | 80000 | 768 | 8 cores |
| 64 GB cluster instance | redis.logic.sharding.8g.8db.0rodb.8prox y.default | 8 | 80000 | 768 | 8 cores |
| 128 GB cluster instance | redis.logic.sharding.8g.16db.0rodb.16pr oxy.default | 16 | 160000 | 1536 | 16 cores |
| 256 GB cluster instance | redis.logic.sharding.16g.16db.0rodb.16 proxy.default | 16 | 160000 | 1536 | 16 cores |
| 512 GB cluster instance | redis.logic.sharding.16g.32db.0rodb.32 proxy.default | 32 | 320000 | 2048 | 32 cores |
| 1 TB cluster instance | redis.logic.sharding.16g.64db.0rodb.64 proxy.default | 64 | 500000 | 2048 | 64 cores |
| 2 TB cluster instance | redis.logic.sharding.16g.128db.0rodb.12 8proxy.default | 128 | 500000 | 2048 | 128 cores |

| Specification | InstanceClass (used in API operations) | Shard s | Maximu m connecti ons | Total bandwid th (MB/s) | CPU |
|---|---|---|---|---|---|
| 4 TB cluster instance | redis.logic.sharding.16g.256db.0rodb.25 6proxy.default | 256 | 500000 | 2048 | 256 cores |

Read/write splitting instances

| Specification | InstanceClass (used in API operations) | Read replic as | Connecti ons per second | Maximu m connecti ons | Total band width (MB/s ) | QPS |
|---|---|---|---|---|---|---|
| 1 GB read/write splitting instance (1 shard, 1 read replica) | redis.logic.splitrw.sm all.1db.1rodb.4proxy. default | 1 | 20000 | 20000 | 96 | 200000 |
| 1 GB read/write splitting instance (1 shard, 3 read replicas) | redis.logic.splitrw.sm all.1db.3rodb.4proxy. default | 3 | 40000 | 40000 | 192 | 400000 |
| 2 GB read/write splitting instance (1 shard, 1 read replica) | redis.logic.splitrw.mid .1db.1rodb.4proxy.de fault | 1 | 20000 | 20000 | 192 | 200000 |
| 2 GB read/write splitting instance (1 shard, 3 read replicas) | redis.logic.splitrw.mid .1db.3rodb.4proxy.de fault | 3 | 40000 | 40000 | 384 | 400000 |
| 4 GB read/write splitting instance (1 shard, 1 read replica) | redis.logic.splitrw.sta nd.1db.1rodb.4proxy. default | 1 | 20000 | 20000 | 192 | 200000 |
| 4 GB read/write splitting instance (1 shard, 3 read replicas) | redis.logic.splitrw.sta nd.1db.3rodb.4proxy. default | 3 | 40000 | 40000 | 384 | 400000 |
| 8 GB read/write splitting instance (1 shard, 1 read replica) | redis.logic.splitrw.lar ge.1db.1rodb.4proxy. default | 1 | 20000 | 20000 | 192 | 200000 |
| 8 GB read/write splitting instance (1 shard, 3 read replicas) | redis.logic.splitrw.lar ge.1db.3rodb.4proxy. default | 3 | 40000 | 40000 | 384 | 400000 |
| 16 GB read/write splitting instance (1 shard, 1 read replica) | redis.logic.splitrw.2xl arge.1db.1rodb.4prox y.default | 1 | 20000 | 20000 | 192 | 200000 |

| Specification | InstanceClass (used in API operations) | Read replic as | Connecti ons per second | Maximu m connecti ons | Total band width (MB/s ) | QPS |
|---|---|---|---|---|---|---|
| 16 GB read/write splitting instance (1 shard, 3 read replicas) | redis.logic.splitrw.2xl arge.1db.3rodb.4prox y.default | 3 | 40000 | 40000 | 384 | 400000 |
| 32 GB read/write splitting instance (1 shard, 1 read replica) | redis.logic.splitrw.4xl arge.1db.1rodb.4prox y.default | 1 | 20000 | 20000 | 192 | 200000 |
| 32 GB read/write splitting instance (1 shard, 3 read replicas) | redis.logic.splitrw.4xl arge.1db.3rodb.4prox y.default | 3 | 40000 | 40000 | 384 | 400000 |
| 64 GB read/write splitting instance (1 shard, 1 read replica) | redis.logic.splitrw.8xl arge.1db.1rodb.4prox y.default | 1 | 20000 | 20000 | 192 | 200000 |
| 64 GB read/write splitting instance (1 shard, 3 read replicas) | redis.logic.splitrw.8xl arge.1db.3rodb.4prox y.default | 3 | 40000 | 40000 | 384 | 400000 |

#### Error codes

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because RAM users are not authorized to call the API operation. | Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. | 403 |
| The error message returned because the operation is unavailable for RAM users. | Forbedden.NotSupport RAM | This action does not support accessed by RAM mode. | 403 |
| The error message returned because an exception or error occurs on the server. | ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 |
| The error message returned because the instance status that you specified does not exist. | InvalidStatus.NotFound | The Status provided does not exist in our records. | 404 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified value of the parameter is invalid. | InvalidParameter | The specified parameter InstanceName is not valid. | 400 |
| The error message returned because you are not authorized to call the administrator- specific API operations. | Forbbiden.NotAdminUse r | User not authorized to operate on the specified API as you are not the | 403 |
| The error message returned because the parameter is missing. | MissingParameter | Specified parameter is missing. | 400 |
| The error message returned because neither InstanceName nor NewPassword is specified. | MissingParameter | InstanceName/NewPass word at least one is mandatory for this action. | 400 |
| The error message returned because OwnerId is not specified for this operation. | MissingParameter | The input parameter OwnerId, OwnerAccount that is mandatory for processing this request | 403 |
| The error message returned because the specified Token parameter is invalid. | InvalidToken.Malformed | The Specified parameter "Token" is not valid. | 400 |
| The error message returned because the specified InstanceName parameter is invalid. | InvalidInstanceName.Ma lformed | The Specified parameter "InstanceName" is not valid. | 400 |
| The error message returned because the specified Password parameter is invalid. | InvalidPassword.Malfor med | The Specified parameter "Password" is not valid." | 400 |
| The error message returned because the specified Instances parameter is invalid. | InvalidInstances.Malfor med | The Specified parameter "Instances" is not valid. | 400 |
| The error message returned because the specified StartTime parameter is invalid. | InvalidStartTime.Malfor med | The Specified parameter "StartTime" is not valid. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified EndTime parameter is invalid. | InvalidEndTime.Malform ed | The Specified parameter "EndTime" is not valid. | 400 |
| The error message returned because the specified InstanceIds parameter is invalid. | InvalidInstanceIds.Malfo rmed | The Specified parameter "InstanceIds" is not valid. | 400 |
| The error message returned because your balance is insufficient to perform the current operation. | InsufficientBalance | Your account does not have enough balance. | 400 |
| The error message returned because your account fails to pass the real-name authentication. | RealNameAuthenticatio nError | Your account has not passed the real-name authentication yet. | 403 |
| The error message returned because your instance quota has been exhausted. | QuotaExcee | Living afterpay instances quota exceeded. | 400 |
| The error message returned because the capacity configuration is invalid. | InvalidCapacity.NotFoun d | The Capacity provided does not exist in our records. | 400 |
| The error message returned because the ClientToken parameter used for this request has already been used for a different request. | IdempotentParameterMi smatch | Request uses a client token in a previous request but is not identical to that request. | 400 |
| The error message returned because the inventory of instances in the specified zone is insufficient. | QuotaNotEnough | Quota not enough in this zone. | 400 |
| The error message returned because you are not authorized to call the order-class API operations. | Forbbiden.SubUser | The specified action is not available for you. | 403 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the Apsara Stack risk control system denies this access request. | Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 403 |
| The error message returned because the specified region does not exist. | InvalidRegion.NotFound | The RegionId or ZoneId provided does not exist in our records. | 404 |
| The error message returned because the specified ZoneId parameter is invalid. | InvalidZoneId.NotFound | The ZoneId provided is invalid. | 400 |
| The error message returned because the ID of the instance does not exist. | InvalidInstanceId.NotFou nd | The InstanceId provided does not exist in our records. | 404 |
| The error message returned because the password is incorrect. | IncorrectPassword | The Password provided is not correct. | 400 |
| The error message returned because the service is unavailable. | ServiceNotSupported | The specified service is not supported. | 400 |
| The error message returned because a renewal and configuration change order has not taken effect. | HasRenewChangeOrder | This instance has a renewChange order. | 400 |
| The error message returned because an internal error occured. | InternalError | The request processing has failed due to some unknown error. | 500 |
| The error message returned because the specified backup time is invalid. | InvalidPreferredBackupT ime | Specified preferred backup time is not valid. | 400 |
| The error message returned because the specified backup type is invalid. | InvalidBackupType.Form at | Specified backup type is not valid. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified backup method is invalid. | InvalidBackupMethod.Fo rmat | Specified backup method is not valid. | 400 |
| The error message returned because the backup task already exists. | BackupJobExists | A backup job already exists in the specified DB instance. | 400 |
| The error message returned because the maximum number of daily backup operations has been reached. | BackupTimesExceeded | Exceeding the daily backup times of this DB instance. | 400 |
| The error message returned because no parameters are specified. | ParameterLeastAssociat e | Must input at least one optional parameter. | 400 |
| The error message returned because the specified backup period is invalid. | InvalidBackupRetentionP eriod.Malformed | Specified backup retention period is not valid. | 400 |
| The error message returned because the specified next backup time is invalid. | InvalidPreferredBackupT ime.Format | Specified preferred backup time is not valid. | 400 |
| The error message returned because the specified backup period is invalid. | InvalidPreferredBackupP eriod.Malformed | Specified backup period is not valid. | 400 |
| The error message returned because the operation is not supported by the current instance type. | IncorrectDBInstanceTyp e | Current DB instance type does not support this operation | 400 |
| The error message returned because the specified key is invalid. | InvalidKey.Malformed | Specified key is not valid. | 400 |
| The error message returned because the nonce signature is used and cannot be used again. | SignatureNonceUsed | Specified signature nonce was used already. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because no virtual IP address can be assigned. | AllocateVpcIp.NotEnoug h | Ip resource is not enough | 400 |
| The error message returned because instances of the specified type cannot be created in the zone. | Zone.NotSupport | Specified zone does not support creating with instance class. | 400 |
| The error message returned because the code for the instance type is invalid. | MissingClassCode | Capacity or InstanceClass is mandatory for this action. | 400 |
| The error message returned because the specified instance type is not supported. | InvalidDBInstanceClass.N otFound | Specified DB instance class is not found. | 404 |
| The error message returned because the instance is locked. | IncorrectDBInstanceLock Mode | Current DB instance lock mode does not support this operation. | 400 |
| The error message returned because the ID of the backup set does not exist. | InvalidBackupSetID.NotF ound | Specified backup set ID does not exist. | 400 |
| The error message returned because the operation is not supported while the instance is in the current state. | IncorrectDBInstanceStat e | Current DB instance state does not support this operation. | 400 |
| The error message returned when the available resource capacity in the specified instance is insufficient. | InsufficientResourceCap acity | There is insufficient capacity available for the requested instance. | 400 |
| The error message returned because the specified end time is invalid. | InvalidEndTime.Format | Specified end time is not valid. | 400 |
| The error message returned because the specified duration for reserving a classic IP address is invalid. | InvalidClassicExpiredDay s.Format | The specified classicExpiredDays format is not valid. | 400 |

| psaraDB for Redis |   | De | veloper Guide·API referenc |
|---|---|---|---|

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the operation is not supported while the backup set is in the current state. | IncorrectBackupSetStat e | Current backup set state does not support operations. | 400 |
| The error message returned when the specified whitelist is not correct in format. | InvalidSecurityIPList.For mat | Specified security IP list format is not valid. | 400 |

#### Instance configurations

KVStore for Redis instance configurations

| Parameter | Description | Value |
|---|---|---|
| maxmemory-policy | The eviction policy that a KVStore for Redis instance uses to evict data when the memory exceeds the threshold. KVStore for Redis supports six data eviction policies. | VolatileLRU: only evicts original data that has Time To Live (TTL) configured based on the Least Recently Used (LRU) algorithm. VolatileTTL: only evicts data that has TTL configured based on the TTL values in ascending order. AllKeysLRU: evicts original data based on the LRU algorithm. VolatileRandom: only evicts original data that has TTL configured randomly. AllKeysRandom: evicts original data randomly. NoEviction: evicts no data, but returns an error message when you write new data to the instance. |

| Parameter | Description | Value |
|---|---|---|
| hash-max-ziplist-entries | A hash object uses ziplist encoding only if the hash object meets both of the following conditions: The number of key-value pairs stored in the hash object is smaller than or equal to the value of list-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the hash object are smaller than or equal to the value of list-max-ziplist-value. | Default value: 512. |
| hash-max-ziplist-value | A hash object uses ziplist encoding only if the hash object meets both of the following conditions: The number of key-value pairs stored in the hash object is smaller than or equal to the value of list-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the hash object are smaller than or equal to the value of list-max-ziplist-value. | Default value: 64. |
| list-max-ziplist-entries | A list object uses ziplist encoding only if the list object meets both of the following conditions: The number of key-value pairs stored in the list object is smaller than or equal to the value of list-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the list object are smaller than or equal to the value of list-max-ziplist-value. | Default value: 512. |

| Parameter | Description | Value |
|---|---|---|
| list-max-ziplist-value | A list object uses ziplist encoding only if the list object meets both of the following conditions: The number of key-value pairs stored in the list object is smaller than or equal to the value of list-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the list object are smaller than or equal to the value of list-max-ziplist-value. | Default value: 64. |
| set-max-intset-entries | A set object uses intset encoding only if: the number of entries is smaller than or equal to the value of set-max-intset-entries and all entries are decimal integers. | Default value: 512. |
| zset-max-ziplist-entries | A zset object uses ziplist encoding only if the zset object meets both of the following conditions: The number of key-value pairs stored in the zset object is smaller than or equal to the value of zset-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the zset object are smaller than or equal to the value of zset-max-ziplist- value. | Default value: 128. |

| Parameter | Description | Value |
|---|---|---|
| zset-max-ziplist-value | A zset object uses ziplist encoding only if the zset object meets both of the following conditions: The number of key-value pairs stored in the zset object is smaller than or equal to the value of zset-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the zset object are smaller than or equal to the value of zset-max-ziplist- value. | Default value: 64. |
| notify-keyspace-events | The keyspace notifications allow clients to subscribe to channels or modes to receive events where Redis datasets were modified in some way. | K: the keyspace notifications. All notifications are prefixed with \ keyspace\@ \ . __ _ _ E: the keyevent notifications. All notifications are prefixed with keyevent@ . __ __ g: the notifications about general commands that are non-type specific, such as DEL, EXPIRE, and RENAME. $: the string command notifications. l: the list command notifications. s: the set command notifications. h: the hash command notifications. z: the sorted set command notifications. x: the expiration events. The system sends an expiration event after the system deletes an expired key. e: the eviction events. The system sends an eviction event after the system evicts a key according to the maxmemory policy. A: the alias for g$lshzxe. |
