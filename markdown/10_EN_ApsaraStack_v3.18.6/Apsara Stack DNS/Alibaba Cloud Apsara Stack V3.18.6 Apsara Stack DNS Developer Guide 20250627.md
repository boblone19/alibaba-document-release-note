---
title: "Apsara Stack DNS Developer Guide 20250627"
product_version: "V3.18.6"
pdf_pages: 239
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Apsara Stack DNS Developer Guide 20250627.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E8%A7%A3%E6%9E%90DNS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20Stack%20DNS%20Developer%20Guide%2020250627.pdf"
converter: line-classifier (PyMuPDF)
---

# Apsara Stack DNS Developer Guide 20250627

Apsara Stack DNS

## Preparations

### Obtain the information and

**the endpoint of an API operation**

To call an API operation of a cloud service, you must obtain the information about the operation, including the service code, operation name, and API version.

**Background information**

The API information on the debugging page of the Apsara Uni-manager Management Console is for reference only. For more information about how to call API operations, see the developer guides of cloud services. If the information on the debugging page is different from that in the developer guide of a cloud service, the information in the developer guide prevails.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI**
**Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top
navigation bar.
4. In the left-side navigation pane, select the cloud service that you want to manage.
5. Select an API version from the **Version** drop-down list.
6. In the API operation list, you can view all API operations of the current version.
7. Click the operation that you want to call. Obtain the endpoint from the Endpoint parameter
on the Parameter tab.

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID, such as cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. |

Apsara Stack DNS

### Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain an AccessKey pair. Only operations administrators and level-1 organization administrators can obtain the AccessKey pair of an organization.

**Background information**

We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services. When you use the AccessKey pair of a personal account, you must configure header parameters as described in the following table for access control.

**Warning**

The AccessKey pairs of personal accounts are under control of the Apsara Uni-manager Management Console permission system. AccessKey pairs of organization accounts have higher permissions. For security purposes, organization operations must be approved by administrators.

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
click **User Information**.
3. In the **Apsara Stack AccessKey Pair** section, view your AccessKey pair.

**Note**

The AccessKey pair consists of an AccessKey ID and an AccessKey secret. AccessKey pairs allow you to access Apsara Stack resources with full permissions for your account. You must keep your AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

Apsara Stack DNS To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the **Enterprise** page, click **Organizations**.
4. In the organization navigation tree, click an organization name.
5. In the Current Organization section, click **Obtain an accesskey**.
6. In the AccessKey message, view the AccessKey pair of the organization.

**Note**

An AccessKey pair is automatically allocated to each level-1 organization. Subordinate organizations use the same AccessKey pair of their level-1 organization.

### Obtain common header

**parameters**

When calling API operations, you must provide multiple header parameters. This topic describes how to obtain these parameters and explains some response parameters.

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resource Management** > **Regions**.
4. Click the name of the organization.
5. In the **Region List** section on the right, view the **Region Name**, which is the region ID.

**Obtain an organization ID**

You must call a specific API operation to obtain the organization ID. You can obtain the organization ID by using the online debugging feature in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. Click **Products** in the top navigation bar and select **Developer Tools** > **API & Tools** >
**Developer Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.
4. Click the
button and select **Cloud Platform** > **Unified Cloud Management**
**Platform**. For **Version**, select **2019-05-10**.
5. Enter `GetOrganizationList` in the text box for online debugging. Enter the name of the
target organization in the name parameter and call the operation. After the call is successful, view the **Call Result** section and find the **id** value, which is the organization ID. For more information, see the GetOrganizationList section in the Apsara Uni-manager Mana gement Console Developer Guide.

**Obtain a resource set ID**

You must call a specific API operation to obtain the resource set ID. You can obtain the resource set ID by using the online debugging feature in the Apsara Uni-manager Management Console.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The organization ID. |

Apsara Stack DNS
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. Click **Products** in the top navigation bar and select **Developer Tools** > **API & Tools** >
**Developer Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.
4. Click the
button and select **Cloud Platform** > **Unified Cloud Management**
**Platform**. For **Version**, select **2019-05-10**.
5. Enter `ListResourceGroup` in the text box for online debugging. After the call is successful,
view the **Call Result** section and find the **id** value, which is the resource set ID. For more information, see the ListResourceGroup section in the Apsara Uni-manager Management Co nsole Developer Guide.

**Obtain an instance ID**

You can obtain an instance ID from the cloud service instance list in the Apsara Uni-manager Management Console. This topic uses API Gateway as an example to describe how to obtain an instance ID:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Development And Tools** > **Development**
**And O&M** > **API Gateway**.
3. In the left-side navigation pane, click **Instances**.
4. View the **Instance ID** in the instance list.

**Response parameters**

The following response parameters are returned by default when you call operations to query the instances of cloud services.

### Obtain access credentials

**assigned by STS**

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

STS allows you to manage temporary access credentials for your Apsara Stack resources. You can use STS to call API operations.

|  | stsAK |
|---|---|
| RAM role |  |

Apsara Stack DNS

**Procedure**

1. Obtain the Apsara Stack Resource Name (ARN) of your `Resource Access Management (RAM)`
`role` . i. Log on to the Apsara Uni-manager Management Console. ii. In the upper-right corner of the homepage, click the profile picture and then click **User**
**Information**.
iii. On the page that appears, click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view the ARN of your `RAM role` . Apsara Stack DNS

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
} public static String AssumeRole(ASClient asClient, String roleArn) {
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
}
```

3. Use the access credentials assigned by STS to call an API operation of a cloud service. In
this example, the Elastic Compute Service (ECS) API is used. Apsara Stack DNS

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
        asClient.setSdkSource("test");
  // Call an API operation of ECS.
        String ecsRes = DescribeZones(asClient,<stsAK>,<stsSK>,<stsToken>);
} public static String DescribeZones(ASClient asClient, String stsAK, String stsSK, Str ing stsToken) {
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
    }
```

Apsara Stack DNS

## Use POP to make API calls

### Preparations

You can use the point of presence (POP) gateway to call API operations in Apsara Stack in the same way as in Alibaba Cloud public cloud. This topic describes the preparations before you use the POP gateway to call API operations.

**Background information**

To enable you to call API operations in the same way as that in Alibaba Cloud public cloud and have a more convenient and consistent experience, we recommend that you use the POP gateway to call API operations in Apsara Stack.

**Obtain service endpoints**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI**
**Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top
navigation bar.
4. In the left-side navigation pane, select the cloud service that you want to manage.
5. Select an API version from the **Version** drop-down list.
6. In the API operation list, you can view all API operations of the current version.
7. Click the operation that you want to call. Obtain the endpoint from the Endpoint parameter
on the Parameter tab.

**Obtain an endpoint in Apsara Infrastructure Management**

Apsara Stack DNS To use the POP gateway to call API operations in Apsara Stack, you must obtain the required service endpoints. You can obtain service endpoints from Apsara Stack onsite O&M engineers You can also obtain service endpoints by yourself. In this example, API Gateway is used.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Apsara Infrastructure**
**Management** > **O&M Tools**.
3. In the left-side navigation pane, choose **O&M Tools** > **Service Registration Variable**
**Dashboard**.
4. On the Service Registration Variable Dashboard page, click **Advanced Filter**.
5. Enter `apigateway` in the Service Registration field and click **Search**.
icon.
6. In the **Service Registration** column of the apigateway service, click the
7. Click the text information in the **Service Registration** column of the `apigateway` service.
In the **Registration Variables** message, obtain the endpoint from the value of apigateway.openapi.endpoint.

**Obtain common parameters**

You must obtain the parameters required when you use the POP gateway to call API operations, such as the organization ID, resource set ID, region ID, and instance ID. For more information, see Obtain the values of common request headers.

### SDK for Java

Before you use an SDK for Java to call the API of a cloud service over the point of presence (POP) gateway, you must check the style of the service API. A service API can be of the Remote Procedure Call (RPC) or Resource-Oriented Architecture (ROA) style.

**Usage notes**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample**
**Code** in the top navigation bar.

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues. Proceed with caution.

**Examples**

The following sample code provides an example on how to call RPC APIs. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException;
```

Apsara Stack DNS p y p p

```java
import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
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
```

Apsara Stack DNS

```java
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
        }
    }
}
```

The following sample code provides an example on how to call ROA APIs. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06- 07. Sample code:

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
//Specifytheserviceendpoint.
```

Apsara Stack DNS

```java
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
        }
    }
}
```

**Important**

By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be ignored in the test environment, you can specify the following setting: Apsara Stack DNS Java

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Disable certificate verification for the client. clientConfig.setIgnoreSSLCerts(true)
```

### SDK for Go

This topic describes how to use SDK for Go over the point of presence (POP) gateway.

**Usage notes**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample**
**Code** in the top navigation bar.

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues. Proceed with caution.

**Background information**

Remote Procedure Call (RPC) and Resource-Oriented Architecture (ROA) APIs are supported.

**Examples**

The following sample code provides an example on how to call RPC APIs. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code: Apsara Stack DNS

```java
package main import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

)

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
    }
    fmt.Print(response.GetHttpContentString())
}
```

The following sample code provides an example on how to call ROA APIs. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06- 07. Sample code: Apsara Stack DNS

```java
package main import (
 "fmt"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
 "os"
```

)

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
 }
 fmt.Print(response.GetHttpContentString())
}
```

**Proxy configuration**

You can configure proxies for API calls in one of the following ways: Configure proxies by using environment variables. Set the HTTP_PROXY, HTTPS_PROXY, or NO_PROXY environment variable. Sample code: Apsara Stack DNS

```java
import (
    "os"
```

)

```
func main(){
 os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // Set the HTTP_PROXY environment var
iable.
 os.Setenv("HTTPS_PROXY", "https://x.x.x.x:xxxx") // Set the HTTPS_PROXY environment
variable. }
```

Configure proxies on the client. Sample code:

```
// The proxies that are configured on the client take precedence over those that are configured by using environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Configure the HTTP proxy. client.GetHttpProxy() // Query the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Configure the HTTPS proxy. client.GetHttpsProxy() // Query the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Configure the proxy whitelist. client.GetNoProxy() // Query the proxy whitelist.
```

**SSL verification**

**Description**

You can configure SSL verification for requests. If you set the HTTPSInsecure parameter to `true` , certificate verification is disabled. To ensure connection security, we recommend that you enable certificate verification. If you set the HTTPSInsecure parameter to `false` , certificate verification is enabled. By default, certificate authority (CA) certificates on the operating systems are used.

**Default value**

```
 false
```

**Configuration methods**

**Important**

By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be ignored in the test environment, you can specify the following settings: Apsara Stack DNS

```
// If you configure the HTTPSInsecure parameter for a request, the setting takes effect only on the current request. request.SetHTTPSInsecure(true) // Set the HTTPSInsecure parame ter to true for the request. isInsecure := request.GetHTTPSInsecure() // Query the setting of the HTT PSInsecure parameter for the request.
```

If you do not configure the HTTPSInsecure parameter for a request, the setting for a client takes effect.

```
// If you configure the HTTPSInsecure parameter for the client, the setting takes effec t on all requests that are initiated by the client. client.SetHTTPSInsecure(true) // Set the HTTPSInsecure parameter to true for the client. isInsecure := client.GetHTTPSInsecure() // Query the setting of the HTTPSI nsecure parameter for the client.
```

### SDK for Python

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

Apsara Stack DNS

```python
    "<your-RegionID>",
    timeout=1000,  # Specify the timeout period.
    verify=False, # Disable SSL certificate verification. To enable SSL certificate ver
ification, specify verify='<The path of the certificate>'. );
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
    }
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

Apsara Stack DNS

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

)

```
request = DescribeInstancesRequest() request.set_protocol_type('https') # Set the protocol to HTTPS. client.do_action_with_exception(request)
```

**Disable certificate verification**

**Important**

By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be ignored in the test environment, you can set the `verify` parameter to false.

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # The region ID.
    verify=False  # Disable SSL certificate verification.
```

)

**Enable certificate verification**

Apsara Stack DNS

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # The region ID.
    verify='./cacert.pem'  # The path of the certificate authority (CA) certificate.
```

)

| API | Description |
|---|---|
| ObtainGlobalAuthZoneList | Obtains global authoritative zones |
| ObtainGlobalAuthRecordList | Obtains global authoritative RRSets |
| AddGlobalRrSet | Adds global RRSets |
| DeleteGlobalRrSet | Deletes global RRSets |
| UpdateGlobalRrSet | Updates global RRSets |
| RemarkGlobalRrSet | Configures descriptions for global RRSets |

Apsara Stack DNS

## API Reference

### Overview

#### Calling methods

You can use a pair of AccessKey ID and AccessKey Secret to call API operations. You can use SDKs of different languages, or create a client based on the signature description provided by the POP gateway.

#### Supported formats

AccessKey ID and AccessKey Secret of an Apsara Stack tenant account Temporary AccessKey ID and AccessKey Secret of an Apsara Stack tenant account AccessKey ID and AccessKey Secret of a RAM user account Temporary AccessKey ID and AccessKey Secret of a RAM user account

#### Instructions

The AccessKey ID is used to identify users. The AccessKey Secret is used to compute the request signature.

#### Time format

Unless otherwise specified, the time string is a UTC+0 time in the format of YYYY-MM- DDTHH:mm:ssZ. For example, 2018-01-16T09:00:01Z indicates 17:00:01 on January 16, 2018, in China Standard Time (UTC+8).

### List of operations by function

DNS V2.0 provides the following API operations.

### Prerequisites

#### Obtain an AccessKey pair

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID, such as cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. |

Apsara Stack DNS An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain an AccessKey pair. Only operations administrators and level-1 organization administrators can obtain the AccessKey pair of an organization.

**Background information**

We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services. When you use the AccessKey pair of a personal account, you must configure header parameters as described in the following table for access control.

**Warning**

The AccessKey pairs of personal accounts are under control of the Apsara Uni-manager Management Console permission system. AccessKey pairs of organization accounts have higher permissions. For security purposes, organization operations must be approved by administrators.

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
click **User Information**.
3. In the **Apsara Stack AccessKey Pair** section, view your AccessKey pair.

**Note**

The AccessKey pair consists of an AccessKey ID and an AccessKey secret. AccessKey pairs allow you to access Apsara Stack resources with full permissions for your account. You must keep your AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console as an administrator.

| sudo docker ps -l | command to obtain the ID of |
|---|---|
| sudo docker inspect ${container id} \|grep env |  |

Apsara Stack DNS
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the **Enterprise** page, click **Organizations**.
4. In the organization navigation tree, click an organization name.
5. In the Current Organization section, click **Obtain an accesskey**.
6. In the AccessKey message, view the AccessKey pair of the organization.

**Note**

An AccessKey pair is automatically allocated to each level-1 organization. Subordinate organizations use the same AccessKey pair of their level-1 organization.

#### Obtain an endpoint

**Procedure**

1. Log on to the Apsara Infrastructure Management Framework console as an administrator.
2. In the top navigation bar, choose **Operations > Cluster Operations**.
3. On the **Cluster Operations** page, select dnsProduct from the **Project** drop-down list.
4. In the Service Instances section, click **Details** in the Actions column corresponding to
dnsService.
5. In the Machine Information section, click **Terminal** in the Actions column corresponding to
a server to go to the console. Apsara Stack DNS endpoint of the current environment. The endpoint is the value corresponding to pop_out_endpoint (the string starting with "api.").

### SDK example

#### Create a client

You need to specify a region ID, AccessKey ID, and AccessKey Secret to create a client.

**Go SDK**

```
1.    if client, err := genesisdns.NewClientWithAccessKey(RegionId, AccessKey,
AccessSecret); err == nil {
2.      //Normal business logic
3.    } else {
4.      //Business logic to handle exceptions
5.    }
```

**Python SDK**

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

**Java SDK**

```
1.    public static void main(String[] args) {
2.         DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{se
cret}");
3.         IAcsClient client = new DefaultAcsClient(profile);
4.    }
```

#### Cloud API reference

##### TransferLeadership

Switches a secondary node to become the primary node.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 343778269185 | The node ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Id | String | 343778269185 | The ID of the node to become the primary node. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=TransferLeadership &Id=343778269185 &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"343778269185",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>343778269185</Id> <Code>error code </Code>
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | 1 | The ID of the probe node. |
| -Ip | String | 127.0.0.1 | The IP address of the probe node. |
| -Dimension | String | ["region","vpcId","z one"], | The probe dimensions. Valid values: region: The probe scope is defined by a specific region. vpcId: The probe scope is defined by a specific virtual private cloud (VPC). zone: The probe scope is defined by a specific zone. |
| - DimensionValu e | String | ["chengdu","az1","" ] | The values of the probe dimensions. |
| - AssignedTaskC ount | Integer | 0 | The default range, which is 0 to 1000. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |

Apsara Stack DNS

##### DescribeDnsGtmAgents

Queries a list of probe nodes for checking the health of addresses in address pools.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| psara Stack DNS |  |  | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | error code | The error code returned. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeDnsGtmAgents &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "DimensionValue":"[\"chengdu\",\"az1\",\"\"]",
  "Ip":"127.0.0.1",
  "AssignedTaskCount":0,
  "Id":"1",
  "Dimension":"[\"region\",\"vpcId\",\"zone\"],"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The ID of the tenant- specific default forwarding domain name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the tenant-specific default forwarding domain name. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <DimensionValue>[&quot;chengdu&quot;,&quot;az1&quot;,&quot;&quot;]</DimensionValue>
 <Ip>127.0.0.1</Ip>
 <AssignedTaskCount>0</AssignedTaskCount>
 <Id>1</Id>
 <Dimension>[&quot;region&quot;,&quot;vpcId&quot;,&quot;zone&quot;],</Dimension>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### DeletePrivateDefaultForwardZone

Deletes a tenant-specific default forwarding domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The DNS record ID. |
| ZoneId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the tenant- specific internal domain name. |
| Name | Strin g | Body | No | www | The name of the DNS record. |

Apsara Stack DNS Sample requests

```
http(s)://[Endpoint]/?Action=DeletePrivateDefaultForwardZone &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### UpdatePrivateZoneRecord

Modifies a DNS record for a tenant-specific internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Type | Strin g | Body | Yes | A | The type of the DNS record. Valid values: A: maps a domain name to an IPv4 address. AAAA: maps a domain name to an IPv6 address. CNAME: maps a domain name to another domain name. MX: maps a domain name to a mail server address. TXT: serves as a Sender Policy Framework (SPF) record to prevent email spam. The text can be up to 255 characters in length. PTR: maps an IP address to a domain name. SRV: specifies the servers that host specific services. NAPTR: records the Naming Authority Pointer (NAPTR) and is typically used for ENUM. CAA: specifies authorized certificate authorities (CAs) for a domain name. NS: maps a domain name to the specified DNS servers. |
| Ttl | Integ er | Body | Yes | 300 | The time-to-live (TTL) of the DNS record. |

Apsara Stack DNS

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| LbaStrate gy | Strin g | Body | Yes | ALL RR _ | The load balancing policy. Valid values: ALL RR: returns all _ addresses without applying a weight. RATIO: returns addresses by weight. |
| RDatas | Repe atList | Body | Yes |  | The list of record values. |
| -Value | Strin g |  | Yes | 1.1.1.1 | The value. |
| - LbaWeigh t | Integ er |  | No | 100 | The load balancing weight. You do not need to specify this parameter if LbaStrategy is set to ALL RR. _ |
| LineIds | Strin g | Body | Yes | ["default"] | The line IDs. |
| Remark | Strin g | Body | No | remark | The description of the DNS record. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The DNS record ID. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdatePrivateZoneRecord &Common request parameters
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | name | The name of the line. |
| Priority | Integ er | Body | Yes | 1 | The priority of the line. A value of 1 indicates the highest priority. A larger value indicates a lower priority. |
| V4Addres ses | Strin g | Body | No | ["1.1.1.1","2.2.2.2"] | The IPv4 addresses. You must specify at least one of V4Addresses and V6Addresses. |
| V6Addres ses | Strin g | Body | No | ["2400:3200::7777"] | The IPv6 addresses. You must specify at least one of V4Addresses and V6Addresses. |

Apsara Stack DNS Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code</Code>
```

##### AddGlobalLine

Creates a global line.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The line ID. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
&Name=name &Priority=1 &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### UpdateGlobalZoneRecord

Modifies a DNS record for a global internal domain name.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The DNS record ID. |
| ZoneId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the global internal domain name. |
| Name | Strin g | Body | No | www | The name of the DNS record. |

Apsara Stack DNS This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Type | Strin g | Body | Yes | A | The type of the DNS record. Valid values: A: maps a domain name to an IPv4 address. AAAA: maps a domain name to an IPv6 address. CNAME: maps a domain name to another domain name. MX: maps a domain name to a mail server address. TXT: serves as a Sender Policy Framework (SPF) record to prevent email spam. The text can be up to 255 characters in length. PTR: maps an IP address to a domain name. SRV: specifies the servers that host specific services. NAPTR: records the Naming Authority Pointer (NAPTR) and is typically used for ENUM. CAA: specifies authorized certificate authorities (CAs) for a domain name. NS: maps a domain name to the specified DNS servers. |
| Ttl | Integ er | Body | Yes | 300 | The time-to-live (TTL) of the DNS record. |

Apsara Stack DNS

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| LbaStrate gy | Strin g | Body | Yes | ALL RR _ | The load balancing policy. Valid values: ALL RR: returns all _ addresses without applying a weight. RATIO: returns addresses by weight. |
| RDatas | Repe atList | Body | Yes |  | The list of record values. |
| -Value | Strin g |  | Yes | 1.1.1.1 | The value. |
| - LbaWeigh t | Integ er |  | No | 100 | The load balancing weight. You do not need to specify this parameter if LbaStrategy is set to ALL RR. _ |
| LineIds | Strin g | Body | Yes | ["default"] | The line IDs. |
| Remark | Strin g | Body | No | remark | The description of the DNS record. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The DNS record ID. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateGlobalZoneRecord &Common request parameters
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |
| Name | Strin g | Body | No | com. | The queried domain name. Partial match is supported. |
| RegionId | Strin g | Body | Yes | cn-region-env1-d01 | The region ID. |

Apsara Stack DNS Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### DescribePrivateForwardZones

Queries a list of tenant-specific forwarding configurations.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -Forwarders | String | ["1.1.1.1"] | The IP addresses of the DNS servers used for forwarding. |
| - RegionAndVpc s | Array |  | The information about the associated virtual private clouds (VPCs) and region ID. |
| --Vpcs | Array |  | The VPCs with which the tenant-specific forwarding configuration is associated. |
| ---Id | String | vpc- 9gd80vqxu8zq5j5s t90yx | The VPC ID. |
| ---Name | String | vpc-name | The name of the VPC. |
| --RegionId | String | cn-region-env1- d01 | The region ID of the VPC. |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the forwarding domain name. |
| -Name | String | com. | The name of the forwarding domain name. |
| -CallerUid | String | 126760529569940 0 | The caller ID. This is a system parameter. |
| -VpcCount | Integer | 1 | The number of associated VPCs. |
| -Remark | String | remark | The description of the tenant-specific forwarding configuration. |
| -ForwardMode | String | FORWARD ONLY _ | The forwarding mode. Valid values: FORWARD ONLY (recommended): _ forwards all requests without recursion. FORWARD FIRST: falls back to recursive _ queries of public DNS servers if forwarding fails. |
| - CreateTimesta mp | Long | 1702460677 | The time when the tenant-specific forwarding configuration was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |

Apsara Stack DNS

| Parameter | Type | Example | Description |
|---|---|---|---|
| - UpdateTimest amp | Long | 1702460677 | The time when the tenant-specific forwarding configuration was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePrivateForwardZones &Common request parameters
```

Sample success responses `JSON` format Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "VpcCount":1,
  "ForwardMode":"FORWARD_ONLY",
  "Forwarders":"[\"1.1.1.1\"]",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "CallerUid":"1267605295699400",
  "-RegionAndVpcs":{
   "--Vpcs":{
    "Id":"vpc-9gd80vqxu8zq5j5st90yx",
    "Name":"vpc-name"
   },
   "RegionId":""
  },
  "Name":"com.",
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The ID of the recursive ACL configuration. |

| Parameter | Type | Example | Description |
|---|---|---|---|

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <VpcCount>1</VpcCount>
 <ForwardMode>FORWARD_ONLY</ForwardMode>
 <Forwarders>[&quot;1.1.1.1&quot;]</Forwarders>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <CallerUid>1267605295699400
 </CallerUid>
 <-RegionAndVpcs>
  <--Vpcs>
   <Id>vpc-9gd80vqxu8zq5j5st90yx
   </Id>
   <Name>vpc-name</Name>
  </--Vpcs>
  <RegionId  />
 </-RegionAndVpcs>
 <Name>com.</Name>
 <Remark>remark</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### DeleteRecursorAcl

Deletes a recursive access control list (ACL) configuration.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the recursive ACL configuration. |

Apsara Stack DNS

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### DeleteZoneVpc

Disassociates one or more virtual private clouds (VPCs) from a tenant-specific internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Vpcs | Repe atList | Body | Yes |  | The VPCs to be disassociated. |
| -Id | Strin g |  | Yes | vpc- 9gd80vqxu8zq5j5st90yx | The VPC ID. |
| -Name | Strin g |  | No | vpc-name | The name of the VPC. |
| RegionId | Strin g | Body | Yes | cn-region-env1-d01 | The region ID of the VPC. |
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the tenant- specific internal domain name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -AnycastAddr | String | 10.1.0.12,10.1.0.13 | The anycast IP addresses. |
| -Id | String | 343778269185 | The node ID. |
| -LocalAddr | String | 10.1.24.1 | The IP address of the node. |
| -RegionId | String | cn-region-env1- d01 | The region ID. |
| -Description | String | description | The description of the node. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Code>error code</Code>
```

##### DescribeNodes

Queries a list of nodes.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Role | String | leader | The role of the node. Valid values: leader: The node is a leader node and participates in election. follower: The node is a follower node and participates in election. learner: The node is a learner node and does not participate in election. candidate: The node is a candidate node in an abnormal state. |
| -Index | Integer | 1 | The ID of the last synchronized log. |
| -IsOnline | Boolean | true | The operational status of the node. Valid values: true: normal. false: offline. |
| - IsInEmergency | Boolean | false | Indicates whether the node is added to an emergency group. Valid values: true false |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Total | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses Apsara Stack DNS `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "PageSize":10,
 "Message":"error message",
 "PageNumber":1,
 "Total":10,
 "Data":{
  "Role":"leader",
  "Description":"description",
  "AnycastAddr":"10.1.0.12,10.1.0.13",
  "IsInEmergency":false,
  "Index":1,
  "Id":"343778269185",
  "RegionId":"cn-region-env1-d01",
  "LocalAddr":"10.1.24.1",
  "IsOnline":true
 },
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <PageSize>10</PageSize> <Message>error message </Message> <PageNumber>1</PageNumber> <Total>10</Total> <Data>
 <Role>leader</Role>
 <Description>description</Description>
 <AnycastAddr>10.1.0.12,10.1.0.13
 </AnycastAddr>
 <IsInEmergency>false</IsInEmergency>
 <Index>1</Index>
 <Id>343778269185
 </Id>
 <RegionId>cn-region-env1-d01
 </RegionId>
 <LocalAddr>10.1.24.1</LocalAddr>
 <IsOnline>true</IsOnline>
</Data> <Code>error code </Code>
```

##### AddPrivateDefaultForwardZone

Creates a tenant-specific default forwarding configuration.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ForwardM ode | Strin g | Body | Yes | FORWARD ONLY _ | The forwarding mode. Valid values: FORWARD ONLY _ (recommended): forwards all requests without recursion. FORWARD FIRST: falls _ back to recursive queries of public DNS servers if forwarding fails. |
| Forwarder s | Strin g | Body | Yes | ["1.1.1.1","1.1.1.2"] | The IP addresses of the DNS servers used for forwarding. |
| RegionId | Strin g | Body | Yes | cn-region-env1-d01 | The region ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the tenant-specific default forwarding configuration. |

Apsara Stack DNS

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddPrivateDefaultForwardZone &Common request parameters
```

Sample success responses

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | com. | The domain name for cache clearing. |
| IncludeSu bDomain | Boole an | Body | Yes | true | The domain name matching mode. Valid values: true: suffix match. false: exact match. |
| MemberId | Long | Body | Yes | 343778263564 | The node ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|

Apsara Stack DNS `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### FlushCache

Clears the DNS cache.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

Apsara Stack DNS

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Code>error code </Code>
```

##### DescribeDnsGtmAddressPools

Queries a list of address pools.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Ip | Strin g | Body | No | 1.1.1.1 | The IP address in the address pool. Fuzzy search is supported. |
| Id | Strin g | Body | No | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The address pool ID. |
| Name | Strin g | Body | No | name | The name of the address pool. Fuzzy search is supported. |
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -Addrs | Array |  |  |
| --Value | String | 1.1.1.1 | The address value. |
| --Mode | String | SMART | The health check mode of the address. Valid values: SMART: returns the address only if it is healthy. ONLINE: always returns the address. OFFLINE: never returns the address. |
| --LbaWeight | Integer | 100 | The load balancing weight. You do not need to specify this parameter if LbaStrategy is set to ALL RR. _ |
| --Available | Boolean | true | Indicates whether the address is available. Valid values: true false |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The address pool ID. |

Apsara Stack DNS

**Response parameters**

| A | psara Stack DNS |  |  | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Name | String | name | The name of the address pool. |
| -Type | String | A | The type of the address pool. Valid values: A: indicates a pool of IPv4 addresses. AAAA: indicates a pool of IPv6 addresses. CNAME: indicates a pool of domain names. |
| -LbaStrategy | String | ALL RR _ | The load balancing policy. Valid values: ALL RR: returns all addresses without _ applying a weight. RATIO: returns addresses by weight. |
| - CreateTimesta mp | Long | 1702460677 | The time when the address pool was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| - UpdateTimest amp | Long | 1702460677 | The time when the address pool was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| MonitoredAddr essCount | Integer | 1 | The number of health check tasks. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

**Examples**

Sample requests Apsara Stack DNS

```
http(s)://[Endpoint]/?Action=DescribeDnsGtmAddressPools &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "MonitoredAddressCount":1,
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "Type":"A",
  "LbaStrategy":"ALL_RR",
  "-Addrs":{
   "LbaWeight":100,
   "Mode":"SMART",
   "Value":"1.1.1.1",
   "Available":true
  },
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "Name":"name"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The address pool ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

```xml
<MonitoredAddressCount>1</MonitoredAddressCount> <RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <Type>A</Type>
 <LbaStrategy>ALL_RR</LbaStrategy>
 <-Addrs>
  <LbaWeight>100</LbaWeight>
  <Mode>SMART</Mode>
  <Value>1.1.1.1</Value>
  <Available>true</Available>
 </-Addrs>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>name</Name>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### DeleteDnsGtmAddressPool

Deletes an address pool.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Developer Guide·A | PI Reference |  | Apsara Stack DN |
|---|---|---|---|
| Parameter | Type | Example | Description |

| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The address pool ID. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteDnsGtmAddressPool &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

**3.4.2.15.**

##### UpdatePrivateDefaultForwardZoneRemark

Modifies the description of a tenant-specific default forwarding configuration.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The ID of the tenant- specific default forwarding configuration. |
| Remark | Strin g | Body | No | remark | The description of the tenant-specific default forwarding configuration. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the tenant-specific default forwarding configuration. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdatePrivateDefaultForwardZoneRemark &Id=e8605e05-4320-4ef5-983d-c5dd48d05b49 &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ZoneId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the global internal domain name. |
| Name | Strin g | Body | No | www | The name of the DNS record. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### AddGlobalZoneRecord

Creates a DNS record for a global internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Type | Strin g | Body | Yes | A | The type of the DNS record. Valid values: A: maps a domain name to an IPv4 address. AAAA: maps a domain name to an IPv6 address. CNAME: maps a domain name to another domain name. MX: maps a domain name to a mail server address. TXT: serves as a Sender Policy Framework (SPF) record to prevent email spam. The text can be up to 255 characters in length. PTR: maps an IP address to a domain name. SRV: specifies the servers that host specific services. NAPTR: records the Naming Authority Pointer (NAPTR) and is typically used for ENUM. CAA: specifies authorized certificate authorities (CAs) for a domain name. NS: maps a domain name to the specified DNS servers. |
| Ttl | Integ er | Body | Yes | 300 | The time-to-live (TTL) of the DNS record. |
| LbaStrate gy | Strin g | Body | Yes | ALL RR _ | The load balancing policy. Valid values: ALL RR: returns all _ addresses without applying a weight. RATIO: returns addresses by weight. |

Apsara Stack DNS

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Remark | Strin g | Body | No | Description | The description of the DNS record. |
| RDatas | Repe atList | Body | Yes |  | The list of record values. |
| -Value | Strin g |  | Yes | 1.1.1.1 | The value. |
| - LbaWeigh t | Integ er |  | No | 100 | The load balancing weight. You do not need to specify this parameter if LbaStrategy is set to ALL RR. _ |
| LineIds | Strin g | Body | Yes | ["default"] | The line IDs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The DNS record ID. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```json
http(s)://[Endpoint]/?Action=AddGlobalZoneRecord? ZoneId=aaa&Name=www&Type=A&Ttl=300&LbaStrategy=RATIO&Remark=remark&LineIds= ["default"]&RDatas.1.Value=1.1.1.1&RDatas.1.LbaWeight=100 &Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The ID of the tenant- specific forwarding domain name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the tenant-specific forwarding domain name. |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### DeletePrivateForwardZone

Deletes a tenant-specific forwarding domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |
| Name | Strin g | Body | No | com. | The queried domain name. Partial match is supported. |

Apsara Stack DNS

```
http(s)://[Endpoint]/?Action=DeletePrivateForwardZone &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### DescribeGlobalForwardZones

Queries a list of global forwarding domain names.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -Forwarders | String | ["1.1.1.1"] | The IP addresses of the DNS servers used for forwarding. |
| - RegionAndVpc s | Array |  | The information about the associated virtual private clouds (VPCs) and region ID. |
| --Vpcs | Array |  | The VPCs with which the global forwarding domain name is associated. |
| ---Id | String | vpc- 9gd80vqxu8zq5j5s t90yx | The VPC ID. |
| ---Name | String | vpc-name | The name of the VPC. |
| --RegionId | String | cn-region-env1- d01 | The region ID of the VPC. |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the forwarding domain name. |
| -Name | String | com. | The name of the forwarding domain name. |
| -CallerUid | String | 126760529569940 0 | The caller ID. This is a system parameter. |
| -VpcCount | Integer | 1 | The number of associated VPCs. |
| -Remark | String | remark | The description of the global forwarding domain name. |
| -ForwardMode | String | FORWARD ONLY _ | The forwarding mode. Valid values: FORWARD ONLY (recommended): _ forwards all requests without recursion. FORWARD FIRST: falls back to recursive _ queries of public DNS servers if forwarding fails. |
| - CreateTimesta mp | Long | 1702460677 | The time when the global forwarding domain name was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |

Apsara Stack DNS

| Parameter | Type | Example | Description |
|---|---|---|---|
| - UpdateTimest amp | Long | 1702460677 | The time when the global forwarding domain name was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGlobalForwardZones &Common request parameters
```

Sample success responses `JSON` format Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "VpcCount":1,
  "ForwardMode":"FORWARD_ONLY",
  "Forwarders":"[\"1.1.1.1\"]",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "CallerUid":"1267605295699400",
  "-RegionAndVpcs":{
   "--Vpcs":{
    "Id":"vpc-9gd80vqxu8zq5j5st90yx",
    "Name":"vpc-name"
   },
   "RegionId":"cn-region-env1-d01"
  },
  "Name":"com.",
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <VpcCount>1</VpcCount>
 <ForwardMode>FORWARD_ONLY</ForwardMode>
 <Forwarders>[&quot;1.1.1.1&quot;]</Forwarders>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <CallerUid>1267605295699400</CallerUid>
 <-RegionAndVpcs>
  <--Vpcs>
   <Id>vpc-9gd80vqxu8zq5j5st90yx
   </Id>
   <Name>vpc-name</Name>
  </--Vpcs>
  <RegionId>cn-region-env1-d01
  </RegionId>
 </-RegionAndVpcs>
 <Name>com.</Name>
 <Remark>remark</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### DescribeResolveConf

Queries the global recursion configuration.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Enable | Boolean | true | Specifies whether to enable recursion. Valid values: true false |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeResolveConf
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "UpdateTime":"1702460677",
 "Enable":true,
 "UpdateTimestamp":1702460677,
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <UpdateTime>1702460677</UpdateTime> <Enable>true</Enable> <UpdateTimestamp>1702460677</UpdateTimestamp> <Code>error code </Code>
```

##### DescribePrivateLines

Queries a list of a private lines.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Ip | Strin g | Body | No | 1.1.1.1 | The queried IP address. Fuzzy search is supported for IPv4 addresses, and only exact search is supported for IPv6 addresses. |
| Name | Strin g | Body | No | name | The name of the line. Partial match is supported. |
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |
| RegionId | Strin g | Body | No | cn-region-env1-d01 | The region ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -V4Addresses | String | ["1.1.1.1"] | The list of IPv4 addresses. |
| -V6Addresses | String | ["2400:3200::7777 "] | The list of IPv6 addresses. |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The address pool ID. |
| -Name | String | name | The name of the line. |
| -Priority | Integer | 1 | The priority of the line. A value of 1 indicates the highest priority. A larger value indicates a lower priority. |
| - CreateTimesta mp | Long | 1702460677 | The time when the private line was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |

Apsara Stack DNS

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| - UpdateTimest amp | Long | 1702460677 | The time when the private line was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePrivateLines &Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "V4Addresses":"[\"1.1.1.1\"]",
  "V6Addresses":"[\"2400:3200::7777\"]",
  "Priority":1,
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "Name":"name"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <V4Addresses>[&quot;1.1.1.1&quot;]</V4Addresses>
 <V6Addresses>[&quot;2400:3200::7777&quot;]</V6Addresses>
 <Priority>1</Priority>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>name</Name>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### UpdatePrivateLine

Modifies a private line.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The line ID. |
| Name | Strin g | Body | Yes | name | The name of the line. |
| Priority | Integ er | Body | Yes | 1 | The priority of the line. A value of 1 indicates the highest priority. A larger value indicates a lower priority. |
| V4Addres ses | Strin g | Body | No | ["1.1.1.1","2.2.2.2"] | The IPv4 addresses. You must specify at least one of V4Addresses and V6Addresses. |
| V6Addres ses | Strin g | Body | No | ["2400:3200::7777"] | The IPv6 addresses. You must specify at least one of V4Addresses and V6Addresses. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The line ID. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | No | com. | The domain name. Partial match is supported. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The domain ID. |
| -Name | String | com. | The domain name. |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### DescribeConflictPrivateZones

Queries the domain names that conflict with a private domain name in a virtual private cloud (VPC).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| -IsForward | Boolean | true | Indicates whether the domain name is a forwarding domain name. Valid values: true false |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| TotalItems | Integer | 10 | The total number of entries. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeConflictPrivateZones &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Data":{
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "IsForward":true,
  "Name":"com."
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The ID of the health check configuration. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the health check configuration. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Data>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <IsForward>true</IsForward>
 <Name>com.
 </Name>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### DeleteDnsGtmMonitor

Deletes a health check configuration for address pools.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The domain ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |

Apsara Stack DNS

```
http(s)://[Endpoint]/?Action=DeleteDnsGtmMonitor &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### DeletePrivateZone

Deletes a tenant-specific internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Developer Guide·A | PI Reference |  | Apsara Stack DN |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the tenant-specific internal domain name. |

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### DescribeDnsGtmMonitor

Queries health check configurations for address pools.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| GtmAddre ssPoolId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The address pool ID. |
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -AgentIds | String | ["agent- id1","agent-id1"] | The list of probe node IDs. |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the health check configuration. |
| -ProtocolType | String | HTTP | The health check protocol. Valid values: ICMP TCP UDP HTTP HTTPS |
| -Enable | String | true | Specifies whether to enable probe. Valid values: true false |
| - MonitorExtend Info | String | {"code":200,"path" :"index.htm","host" :"aliyun.com"} | The extended information. The required parameters vary based on the health check protocol. Parameters required for HTTP or HTTPS: port: the port used for the health check. host: the value of the Host header in the request. path: the URL path for the request. code: the threshold status code. The health check fails if the returned status code is greater than or equal to this value. Parameter required for TCP or UDP: port: the port used for the health check. Parameters required for ICMP: None. |

Apsara Stack DNS

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Interval | Integer | 15 | The health check interval. Unit: seconds. |
| -Timeout | Integer | 3 | The timeout. Unit: seconds. |
| - EvaluationCou nt | Integer | 5 | The number of retries. |
| - CreateTimesta mp | Long | 1702460677 | The time when the health check configuration was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| - UpdateTimest amp | Long | 1702460677 | The time when the health check configuration was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeDnsGtmMonitor &Common request parameters
```

Sample success responses `JSON` format Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "ProtocolType":"HTTP",
  "Timeout":3,
  "AgentIds":"[\"agent-id1\",\"agent-id1\"]",
  "Enable":"true",
  "EvaluationCount":5,
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "MonitorExtendInfo":"{\"code\":200,\"path\":\"index.htm\",\"host\":\"aliyun.com\"}",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "Interval":15
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <ProtocolType>HTTP</ProtocolType>
 <Timeout>3</Timeout>
 <AgentIds>[&quot;agent-id1&quot;,&quot;agent-id1&quot;]
 </AgentIds>
 <Enable>true</Enable>
 <EvaluationCount>5</EvaluationCount>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <MonitorExtendInfo>
{&quot;code&quot;:200,&quot;path&quot;:&quot;index.htm&quot;,&quot;host&quot;:&quot;aliyu com&quot;}</MonitorExtendInfo>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Interval>15</Interval>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### AddPrivateLine

Creates a private line.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | name | The name of the line. |
| Priority | Integ er | Body | Yes | 1 | The priority of the line. A value of 1 indicates the highest priority. A larger value indicates a lower priority. |
| V4Addres ses | Strin g | Body | No | ["1.1.1.1","2.2.2.2"] | The IPv4 addresses. You must specify at least one of V4Addresses and V6Addresses. |
| V6Addres ses | Strin g | Body | No | ["2400:3200::7777"] | The IPv6 addresses. You must specify at least one of V4Addresses and V6Addresses. |
| RegionId | Strin g | Body | Yes | cn-region-env1-d01 | The region ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The line ID. |

Apsara Stack DNS This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| GtmInstan ceId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the Global Traffic Manager (GTM) instance. |
| Name | Strin g | Body | No | name | The name of the access policy. Partial match is supported. |

Apsara Stack DNS

```
&Name=name &Priority=1 &RegionId=cn-region-env1-d01 &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### DescribeDnsGtmAccessStrategies

Queries a list of access policies.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Developer Gui | de·API R | eference |  |  | Apsara Stack DN |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | Description |
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -LineIds | String | ["default"] | The line IDs. |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the access policy. |
| -Name | String | name | The name of the access policy. |
| - GtmInstanceId | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the GTM instance. |
| - DefaultGtmAd dressPoolType | String | IPV4 | The type of the primary address pool. Valid values: DOMAIN: indicates a pool of domain names. IPv6: indicates a pool of IPv6 addresses. IPv4: indicates a pool of IPv4 addresses. |
| - DefaultGtmAd dressPoolId | String | b42155a3-029f- 4d56-bfcb- 0c82657dc7c7 | The ID of the primary address pool. |
| - DefaultGtmAd dressPoolNam e | String | address-pool- name1 | The name of the primary address pool. |
| - DefaultMinAva ilableAddrNum | Integer | 1 | The minimum number of available addresses in the primary address pool. |
| - DefaultAvailab leAddrNum | Integer | 2 | The number of available addresses in the primary address pool. |
| - FailoverGtmAd dressPoolId | String | 90b574f8-6978- 46e4-be85- 159232b981a7 | The ID of the secondary address pool. |

**Response parameters**

| psara Stack DNS |  |  | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - FailoverGtmAd dressPoolNam e | String | address-pool- name2 | The name of the secondary address pool. |
| - FailoverGtmAd dressPoolType | String | IPV4 | The type of the secondary address pool. Valid values: DOMAIN: indicates a pool of domain names. IPv6: indicates a pool of IPv6 addresses. IPv4: indicates a pool of IPv4 addresses. |
| - FailoverMinAv ailableAddrNu m | Integer | 1 | The minimum number of available addresses in the secondary address pool. |
| - FailoverAvaila bleAddrNum | Integer | 2 | The number of available addresses in the secondary address pool. |
| - SpecifiedGtmA ddressPool | String | DEFAULT | The active address pool that you manually specify. Valid values: DEFAULT: the primary address pool. FAILOVER: the secondary address pool. |
| -SwitchMode | String | BY PROBE RESULT _ _ | The policy that determines which address pool (primary or secondary) is active. Valid values: BY HAND: manually determines which _ address pool is active. BY PROBE RESULT: automatically _ _ determines which address pool is active. |
| - InUseGtmAddr essPoolId | String | b42155a3-029f- 4d56-bfcb- 0c82657dc7c7 | The ID of the address pool in use. |
| - InUseGtmAddr essPoolName | String | address-pool- name1 | The name of the address pool in use. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

| Developer Guide·A | PI Reference |  | Apsara Stack DN |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeDnsGtmAccessStrategies &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "FailoverMinAvailableAddrNum":1,
  "DefaultGtmAddressPoolName":"address-pool-name1",
  "FailoverGtmAddressPoolType":"IPV4",
  "LineIds":"[\"default\"]",
  "DefaultAvailableAddrNum":2,
  "SpecifiedGtmAddressPool":"DEFAULT",
  "DefaultGtmAddressPoolId":"b42155a3-029f-4d56-bfcb-0c82657dc7c7",
  "SwitchMode":"BY_PROBE_RESULT",
  "FailoverAvailableAddrNum":2,
  "Name":"name",
  "DefaultMinAvailableAddrNum":1,
  "FailoverGtmAddressPoolId":"90b574f8-6978-46e4-be85-159232b981a7",
  "DefaultGtmAddressPoolType":"IPV4",
  "FailoverGtmAddressPoolName":"address-pool-name2",
  "InUseGtmAddressPoolName":"address-pool-name1",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "GtmInstanceId":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "InUseGtmAddressPoolId":"b42155a3-029f-4d56-bfcb-0c82657dc7c7"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the tenant- specific forwarding domain name. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <FailoverMinAvailableAddrNum>1</FailoverMinAvailableAddrNum>
 <DefaultGtmAddressPoolName>address-pool-name1</DefaultGtmAddressPoolName>
 <FailoverGtmAddressPoolType>IPV4</FailoverGtmAddressPoolType>
 <LineIds>[&quot;default&quot;]</LineIds>
 <DefaultAvailableAddrNum>2</DefaultAvailableAddrNum>
 <SpecifiedGtmAddressPool>DEFAULT</SpecifiedGtmAddressPool>
 <DefaultGtmAddressPoolId>b42155a3-029f-4d56-bfcb-0c82657dc7c7
 </DefaultGtmAddressPoolId>
 <SwitchMode>BY_PROBE_RESULT</SwitchMode>
 <FailoverAvailableAddrNum>2</FailoverAvailableAddrNum>
 <Name>name</Name>
 <DefaultMinAvailableAddrNum>1</DefaultMinAvailableAddrNum>
 <FailoverGtmAddressPoolId>90b574f8-6978-46e4-be85-159232b981a7
 </FailoverGtmAddressPoolId>
 <DefaultGtmAddressPoolType>IPV4</DefaultGtmAddressPoolType>
 <FailoverGtmAddressPoolName>address-pool-name2</FailoverGtmAddressPoolName>
 <InUseGtmAddressPoolName>address-pool-name1</InUseGtmAddressPoolName>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id>
 <GtmInstanceId>56bab908-04e0-44ee-b126-1cbdbcd24507</GtmInstanceId>
 <InUseGtmAddressPoolId>b42155a3-029f-4d56-bfcb-0c82657dc7c7
 </InUseGtmAddressPoolId>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### UpdatePrivateForwardZone

Modifies a tenant-specific forwarding domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | com. | The name of the tenant- specific forwarding domain name. |
| ForwardM ode | Strin g | Body | Yes | FORWARD ONLY _ | The forwarding mode. Valid values: FORWARD ONLY _ (recommended): forwards all requests without recursion. FORWARD FIRST: falls _ back to recursive queries of public DNS servers if forwarding fails. |
| Forwarder s | Strin g | Body | Yes | ["1.1.1.1","1.1.1.2"] | The IP addresses of the DNS servers used for forwarding. |
| Remark | Strin g | Body | No | remark | The description of the tenant-specific forwarding domain name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the tenant-specific forwarding domain name. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdatePrivateForwardZone &Common request parameters
```

Sample success responses

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | com. | The name of the forwarding domain name. |
| ForwardM ode | Strin g | Body | Yes | FORWARD ONLY _ | The forwarding mode. Valid values: FORWARD ONLY _ (recommended): forwards all requests without recursion. FORWARD FIRST: falls _ back to recursive queries of public DNS servers if forwarding fails. |
| Forwarder s | Strin g | Body | Yes | ["1.1.1.1"] | The IP addresses of the DNS servers used for forwarding. |

Apsara Stack DNS `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### AddGlobalForwardZone

Creates a global forwarding domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the forwarding domain name. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddGlobalForwardZone &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### DescribeConflictGlobalZones

Queries domain names that conflict with a global domain name on Apsara Stack.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | No | com. | The domain name. Partial match is supported. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The domain ID. |
| -Name | String | com. | The domain name. |
| -IsForward | Boolean |  | Indicates whether the domain name is a forwarding domain name. Valid values: true false |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| TotalItems | Integer | 10 | The total number of entries. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeConflictGlobalZones &Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The DNS record ID. |
| Remark | Strin g | Body | No | remark | The description of the DNS record. |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Data":{
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "IsForward":"",
  "Name":"com."
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Data>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <IsForward  />
 <Name>com.</Name>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### UpdatePrivateZoneRecordRemark

Modifies the description of a DNS record for a tenant-specific internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The description of the DNS record. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdatePrivateZoneRecordRemark &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### UpdateDnsGtmInstance

Modifies the information about a Global Traffic Manager (GTM) instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The ID of the GTM instance. |
| Name | Strin g | Body | Yes | name | The name of the GTM instance. |
| ZoneId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the scheduling domain. |
| Ttl | Integ er | Body | Yes | 300 | The time-to-live (TTL) of the cached record. |
| Prefix | Strin g | Body | Yes | www | The name of the scheduling domain. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the GTM instance. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateDnsGtmInstance &Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| GtmInstan ceId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the Global Traffic Manager (GTM) instance. |
| Name | Strin g | Body | Yes | name | The name of the access policy. |
| LineIds | Strin g | Body | Yes | ["default"] | The line IDs. |
| DefaultGt mAddress PoolType | Strin g | Body | Yes | IPV4 | The type of the primary address pool. Valid values: DOMAIN: indicates a pool of domain names. IPv6: indicates a pool of IPv6 addresses. IPv4: indicates a pool of IPv4 addresses. |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code</Code>
```

##### AddDnsGtmAccessStrategy

Creates an access policy.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DefaultGt mAddress PoolId | Strin g | Body | Yes | b42155a3-029f-4d56- bfcb-0c82657dc7c7 | The ID of the primary address pool. |
| DefaultMi nAvailable AddrNum | Integ er | Body | Yes | 1 | The minimum number of available addresses in the primary address pool. |
| FailoverGt mAddress PoolId | Strin g | Body | No | 90b574f8-6978-46e4- be85-159232b981a7 | The ID of the secondary address pool. |
| FailoverGt mAddress PoolType | Strin g | Body | No | IPV4 | The type of the secondary address pool. Valid values: DOMAIN: indicates a pool of domain names. IPv6: indicates a pool of IPv6 addresses. IPv4: indicates a pool of IPv4 addresses. |
| FailoverMi nAvailable AddrNum | Integ er | Body | No | 1 | The minimum number of available addresses in the secondary address pool. |
| Specified GtmAddre ssPool | Strin g | Body | No | DEFAULT | The active address pool that you manually specify. Valid values: DEFAULT: the primary address pool. FAILOVER: the secondary address pool. |
| SwitchMo de | Strin g | Body | Yes | BY HAND _ | The policy that determines which address pool (primary or secondary) is active. Valid values: BY HAND: manually _ determines which address pool is active. BY PROBE RESULT: _ _ automatically determines which address pool is active. |

Apsara Stack DNS

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the access policy. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddDnsGtmAccessStrategy &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### UpdateDnsGtmInstanceRemark

Modifies the description of a Global Traffic Manager (GTM) instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The ID of the GTM instance. |
| Remark | Strin g | Body | No | remark | The description of the GTM instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the GTM instance. |

Apsara Stack DNS

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateDnsGtmInstanceRemark &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Enable | Boole an | Body | No | true | Specifies whether to enable recursion. Valid values: true false |
| ForwardM ode | Strin g | Body | No | FORWARD ONLY _ | The forwarding mode. Valid values: FORWARD ONLY _ (recommended): forwards all requests without recursion. FORWARD FIRST: falls _ back to recursive queries of public DNS servers if forwarding fails. |
| Forwarder s | Strin g | Body | No | ["2.2.2.2","3.3.3.3"] | The IP addresses of the DNS servers used for forwarding. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### SetGlobalDefaultForward

Specifies a global default forwarding configuration.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

|  | Developer Guide·A | PI Reference |  | Apsara Stack DN | S |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | error code | The error code returned. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |
| RegionId | Strin g | Body | Yes | cn-region-env1-d01 | The region ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SetGlobalDefaultForward &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Code>error code </Code>
```

##### DescribePrivateDefaultForwardZones

Queries tenant-specific default forwarding configurations.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -Forwarders | String | ["1.1.11.1"] | The IP addresses of the DNS servers used for forwarding. |
| - RegionAndVpc s | Array |  | The information about the associated virtual private clouds (VPCs) and region ID. |
| --Vpcs | Array |  | The VPCs with which the tenant-specific default forwarding configuration is associated. |
| ---Id | String | vpc- 9gd80vqxu8zq5j5s t90yx | The VPC ID. |
| ---Name | String | vpc-name | The name of the VPC. |
| --RegionId | String | cn-region-env1- d01 | The region ID of the VPC. |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the tenant-specific default forwarding configuration. |
| -CallerUid | String | 126760529569940 0 | The caller ID. This is a system parameter. |
| -VpcCount | Integer | 1 | The number of associated VPCs. |
| -Remark | String | remark | The description of the tenant-specific default forwarding configuration. |
| -ForwardMode | String | FORWARD ONLY _ | The forwarding mode. Valid values: FORWARD ONLY (recommended): _ forwards all requests without recursion. FORWARD FIRST: falls back to recursive _ queries of public DNS servers if forwarding fails. |
| - CreateTimesta mp | Long | 1702460677 | The time when the tenant-specific default forwarding configuration was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |

Apsara Stack DNS

| Parameter | Type | Example | Description |
|---|---|---|---|
| - UpdateTimest amp | Long | 1702460677 | The time when the tenant-specific default forwarding configuration was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePrivateDefaultForwardZones &Common request parameters
```

Sample success responses `JSON` format Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "VpcCount":1,
  "ForwardMode":"FORWARD_ONLY",
  "Forwarders":"[\"1.1.11.1\"]",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "CallerUid":"1267605295699400",
  "-RegionAndVpcs":{
   "--Vpcs":{
    "Id":"vpc-9gd80vqxu8zq5j5st90yx",
    "Name":"vpc-name"
   },
   "RegionId":"cn-region-env1-d01"
  },
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <VpcCount>1</VpcCount>
 <ForwardMode>FORWARD_ONLY</ForwardMode>
 <Forwarders>[&quot;1.1.11.1&quot;]</Forwarders>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <CallerUid>1267605295699400</CallerUid>
 <-RegionAndVpcs>
  <--Vpcs>
   <Id>vpc-9gd80vqxu8zq5j5st90yx
   </Id>
   <Name>vpc-name
   </Name>
  </--Vpcs>
  <RegionId>cn-region-env1-d01
  </RegionId>
 </-RegionAndVpcs>
 <Remark>remark</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### DescribeGlobalZones

Queries a list of global internal domain names.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | No | com. | The queried domain name. Partial match is supported. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -Masters | String | ["1.1.1.1:53","2.2.2. 2:53"] | The DNS server address of the primary domain name. |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The domain ID. |
| -Name | String | com. | The domain name. |
| -KeyName | String | my-tsig | The name of the Transaction Signature (TSIG) key. KeyName, KeyAlgorithm, and KeySecret must all be provided or all omitted. |
| -KeyAlgorithm | String | HMAC-SHA512 | The algorithm used for the TSIG key. KeyName, KeyAlgorithm, and KeySecret must all be provided or all omitted. |
| -KeySecret | String | Ok1qR5IW1ajVka5 cHPEJQIXfLyx5V3P SkFBROAzOn21Jum Dq6nIpoj6H8rfj5Uo +Ok55ZWQ0Wgrf3 02fDscHLw== | The value of the TSIG key. KeyName, KeyAlgorithm, and KeySecret must all be provided or all omitted. |
| -RecordCount | Integer | 1 | The total number of DNS records. |
| - GtmInstanceC ount | Integer | 0 | The total number of Global Traffic Manager (GTM) instances created. |
| -Remark | String | remark | The description of the global internal domain name. |

Apsara Stack DNS

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| - CreateTimesta mp | Long | 1702460677 | The time when the global internal domain name was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| - UpdateTimest amp | Long | 1702460677 | The time when the global internal domain name was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGlobalZones &Common request parameters
```

Sample success responses `JSON` format Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "PageSize":10,
 "Message":"error message",
 "PageNumber":1,
 "Data":{
  "KeyName":"my-tsig",
  "Masters":"[\"1.1.1.1:53\",\"2.2.2.2:53\"]",
  "GtmInstanceCount":"",
"KeySecret":"Ok1qR5IW1ajVka5cHPEJQIXfLyx5V3PSkFBROAzOn21JumDq6nIpoj6H8rfj5Uo+Ok55ZWQ0Wgrf 2fDscHLw==",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "RecordCount":1,
  "CreateTimestamp":1702460677,
  "Name":"com.",
  "KeyAlgorithm":"HMAC-SHA512",
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <PageSize>10</PageSize> <Message>error message</Message> <PageNumber>1</PageNumber> <Data>
 <KeyName>my-tsig</KeyName>
 <Masters>[&quot;1.1.1.1:53&quot;,&quot;2.2.2.2:53&quot;]</Masters>
 <GtmInstanceCount  />
<KeySecret>Ok1qR5IW1ajVka5cHPEJQIXfLyx5V3PSkFBROAzOn21JumDq6nIpoj6H8rfj5Uo+Ok55ZWQ0Wgrf30 DscHLw==</KeySecret>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <RecordCount>1</RecordCount>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>com.</Name>
 <KeyAlgorithm>HMAC-SHA512</KeyAlgorithm>
 <Remark>remark</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### DescribeGlobalZoneRecords

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ZoneId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The domain ID. |
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |
| Name | Strin g | Body | No | name | The queried domain name. Partial match is supported. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -LineIds | String | ["default"] | The global line IDs. |
| -RDatas | Array |  |  |
| --Value | String | 1.1.1.1 | The value. |
| --LbaWeight | String | 100 | The load balancing weight. You do not need to specify this parameter if LbaStrategy is set to ALL RR. _ |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The DNS record ID. |
| -Name | String | www | The name of the DNS record. |
| -ZoneId | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The domain ID. |
| -ZoneName | String | com. | The domain name. |

Apsara Stack DNS Queries DNS records for a global internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| psara Stack DNS |  |  | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Type | String | A | The type of the DNS record. Valid values: A: maps a domain name to an IPv4 address. AAAA: maps a domain name to an IPv6 address. CNAME: maps a domain name to another domain name. MX: maps a domain name to a mail server address. TXT: serves as a Sender Policy Framework (SPF) record to prevent email spam. The text can be up to 255 characters in length. PTR: maps an IP address to a domain name. SRV: specifies the servers that host specific services. NAPTR: records the Naming Authority Pointer (NAPTR) and is typically used for ENUM. CAA: specifies authorized certificate authorities (CAs) for a domain name. NS: maps a domain name to the specified DNS servers. |
| -Ttl | Integer | 300 | The time-to-live (TTL) of the DNS record. Unit: seconds. |
| -LbaStrategy | String | ALL RR _ | The load balancing policy. Valid values: ALL RR: returns all addresses without _ applying a weight. RATIO: returns addresses by weight. |
| -Remark | String | remark | The description of the DNS record. |
| - CreateTimesta mp | Long | 1702460677 | The time when the DNS record was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| - UpdateTimest amp | Long | 1702460677 | The time when the DNS record was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |

| Developer Guide·A | PI Reference |  | Apsara Stack DN |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGlobalZoneRecords &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "ZoneName":"com.",
  "Type":"A",
  "ZoneId":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "LbaStrategy":"ALL_RR",
  "-RDatas":{
   "LbaWeight":"100",
   "Value":"1.1.1.1"
  },
  "LineIds":"[\"default\"]",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "Ttl":300,
  "CreateTimestamp":1702460677,
  "Name":"www",
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The line ID. |
| Name | Strin g | Body | Yes | name | The name of the line. |
| Priority | Integ er | Body | Yes | 1 | The priority of the line. A value of 1 indicates the highest priority. A larger value indicates a lower priority. |

Apsara Stack DNS `XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <ZoneName>com.</ZoneName>
 <Type>A</Type>
 <ZoneId>56bab908-04e0-44ee-b126-1cbdbcd24507
 </ZoneId>
 <LbaStrategy>ALL_RR</LbaStrategy>
 <-RDatas>
  <LbaWeight>100</LbaWeight>
  <Value>1.1.1.1</Value>
 </-RDatas>
 <LineIds>[&quot;default&quot;]</LineIds>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <Ttl>300</Ttl>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>www</Name>
 <Remark>remark</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### UpdateGlobalLine

Modifies a global line.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Developer Gui | de·API R | eference |  |  | Apsara Stack DN |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| V4Addres ses | Strin g | Body | No | ["1.1.1.1","2.2.2.2"] | The IPv4 addresses. You must specify at least one of V4Addresses and V6Addresses. |
| V6Addres ses | Strin g | Body | No | ["2400:3200::7777"] | The IPv6 addresses. You must specify at least one of V4Addresses and V6Addresses. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The line ID. |

**Response parameters**

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Enable | Boole an | Body | Yes | true | Specifies whether to enable recursion. Valid values: true false |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

```xml
<RequestId /> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### EnableRecursor

Specifies whether to enable recursion.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
&Enable=true &Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Ip | Strin g | Body | No | 1.1.1.1 | The queried IP address. Fuzzy search is supported for IPv4 addresses, and only exact search is supported for IPv6 addresses. |
| Name | Strin g | Body | No | name | The name of the line. Partial match is supported. |
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -V4Addresses | String | ["1.1.1.1"] | The list of IPv4 addresses. |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Code>error code </Code>
```

##### DescribeGlobalLines

Queries a list of global lines.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| psara Stack DNS |  |  | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -V6Addresses | String | ["2400:3200::7777 "] | The list of IPv6 addresses. |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The line ID. |
| -Name | String | name | The name of the line. |
| -Priority | Integer | 1 | The priority of the line. A value of 1 indicates the highest priority. A larger value indicates a lower priority. |
| - CreateTimesta mp | Long | 1702460677 | The time when the line was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| - UpdateTimest amp | Long | 1702460677 | The time when the line was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGlobalLines &Common request parameters
```

Sample success responses `JSON` format Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "V4Addresses":"[\"1.1.1.1\"]",
  "V6Addresses":"[\"2400:3200::7777\"]",
  "Priority":1,
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "Name":"name"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <V4Addresses>[&quot;1.1.1.1&quot;]</V4Addresses>
 <V6Addresses>[&quot;2400:3200::7777&quot;]</V6Addresses>
 <Priority>1</Priority>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>name</Name>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### DescribeMetrics

Queries the queries per second (QPS) data.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | 343778269185 | The node ID. |
| -CmdAddr | String | 10.200.2.12:80 | The IP address and port number of the resolution node. |
| -QPS | String | 1 | The QPS data. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Total | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

**Examples**

Sample requests Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Body | Yes | cn-region-env1-d01 | The region ID. |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "PageSize":10,
 "Message":"error message",
 "PageNumber":1,
 "Total":10,
 "Data":{
  "QPS":"1",
  "CmdAddr":"10.200.2.12:80",
  "Id":"343778269185"
 },
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <PageSize>10</PageSize> <Message>error message </Message> <PageNumber>1</PageNumber> <Total>10</Total> <Data>
 <QPS>1</QPS>
 <CmdAddr>10.200.2.12:80</CmdAddr>
 <Id>343778269185</Id>
</Data> <Code>error code </Code>
```

##### DescribeDNSServerAddrs

Queries a list of anycast IP addresses of the DNS service.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Addrs | String | ["10.200.0.12", "10.200.0.13"] | The anycast IP addresses. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeDNSServerAddrs &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "Addrs":"[\"10.200.0.12\", \"10.200.0.13\"]",
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` format

```xml
<Addrs> [&quot;10.200.0.12&quot;, &quot;10.200.0.13&quot;]</Addrs>
 <RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0
 </RequestId>
 <Message>error message
 </Message>
 <Code>error code
 </Code>
```

##### UpdateGlobalZoneRemark

Modifies the description of a global internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The domain ID. |
| Remark | Strin g | Body | No | remark | The description of the global internal domain name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The domain ID. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateGlobalZoneRemark &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

| Parameter | Type | Example | Description |
|---|---|---|---|
| Forwarders | String | ["2.2.2.2","3.3.3.3"] | The IP addresses of the DNS servers used for forwarding. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Code | String | error code | The error code returned. |
| UpdateTimest amp | Long | 1702460677 | The time when the global default forwarding configuration was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| Enable | Boolean | true | Indicates whether forwarding is enabled. Valid values: true false |
| ForwardMode | String |  | The forwarding mode. Valid values: FORWARD ONLY (recommended): _ forwards all requests without recursion. FORWARD FIRST: falls back to recursive _ queries of public DNS servers if forwarding fails. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### DescribeGlobalDefaultForward

Queries the global default forwarding configuration.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Response parameters**

**Examples**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | com. | The domain name, which must end with a period (.). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |

Apsara Stack DNS Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGlobalDefaultForward
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "ForwardMode":"",
 "Forwarders":"[\"2.2.2.2\",\"3.3.3.3\"]",
 "Enable":true,
 "UpdateTimestamp":1702460677,
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <ForwardMode /> <Forwarders>[&quot;2.2.2.2&quot;,&quot;3.3.3.3&quot;]</Forwarders> <Enable>true</Enable> <UpdateTimestamp>1702460677</UpdateTimestamp> <Code>error code </Code>
```

##### AddGlobalZone

Creates a global internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| psara Stack DNS |  |  | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the global internal domain name. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeletePrivateDefaultForwardZone &Name=com. &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### UpdatePrivateZoneRemark

Modifies the description of a tenant-specific internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The ID of the tenant- specific internal domain name. |
| Remark | Strin g | Body | No | remark | The description of the tenant-specific internal domain name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the tenant-specific internal domain name. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdatePrivateZoneRemark &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProtocolTy pe | Strin g | Body | Yes | HTTP | The health check protocol. Valid values: ICMP TCP UDP HTTP HTTPS |
| GtmAddre ssPoolId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The address pool ID. |
| Enable | Boole an | Body | Yes | true | Specifies whether to enable probe. Valid values: true false |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### AddDnsGtmMonitor

Creates a health check configuration for address pools.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| MonitorEx tendInfo | Json | Body | No | {"code":200,"path":"ind ex.htm","host":"aliyun.c om"} | The extended information. The required parameters vary based on the health check protocol. Parameters required for HTTP or HTTPS: port: the port used for the health check. host: the value of the Host header in the request. path: the URL path for the request. code: the threshold status code. The health check fails if the returned status code is greater than or equal to this value. Parameter required for TCP or UDP: port: the port used for the health check. Parameters required for ICMP: None. |
| Interval | Integ er | Body | Yes | 15 | The health check interval. Unit: seconds. |
| Timeout | Integ er | Body | Yes | 3 | The timeout. Unit: seconds. |
| Evaluation Count | Integ er | Body | Yes | 5 | The number of retries. |
| AgentIds | Strin g | Body | Yes | ["agent-id1","agent-id1"] | The list of probe node IDs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

**Response parameters**

| Apsara Stack DNS |  |  | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The address pool ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The address pool ID. |

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### UpdateDnsGtmAddressPool

Modifies an address pool.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | name | The name of the address pool. |
| Type | Strin g | Body | Yes | A | The type of the address pool. Valid values: A: indicates a pool of IPv4 addresses. AAAA: indicates a pool of IPv6 addresses. CNAME: indicates a pool of domain names. |
| LbaStrate gy | Strin g | Body | Yes | ALL RR _ | The load balancing policy. Valid values: ALL RR: returns all _ addresses without applying a weight. RATIO: returns addresses by weight. |
| Addr | Repe atList | Body | Yes |  |  |
| -Value | Strin g |  | Yes | 1.1.1.1 | The address value. |
| -Mode | Strin g |  | Yes | SMART | The health check mode of the address. Valid values: SMART: returns the address only if it is healthy. ONLINE: always returns the address. OFFLINE: never returns the address. |
| - LbaWeigh t | Integ er |  | No | 100 | The load balancing weight. You do not need to specify this parameter if LbaStrategy is set to ALL RR. _ |

Apsara Stack DNS

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The address pool ID. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateDnsGtmAddressPool &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### UpdatePrivateLinePriority

Modifies the priority of a private line.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The line ID. |
| Priority | Integ er | Body | Yes | 1 | The priority of the line. A value of 1 indicates the highest priority. A larger value indicates a lower priority. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The line ID. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdatePrivateLinePriority &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The ID of the GTM instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the GTM instance. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### DeleteDnsGtmInstance

Deletes a Global Traffic Manager (GTM) instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteDnsGtmInstance &Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The line ID. |
| Priority | Integ er | Body | Yes | 1 | The priority of the line. A value of 1 indicates the highest priority. A larger value indicates a lower priority. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### UpdateGlobalLinePriority

Modifies the priority of a global line.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The line ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateGlobalLinePriority &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### AddDnsGtmInstance

Creates a Global Traffic Manager (GTM) instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | name | The name of the GTM instance. |
| ZoneId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the scheduling domain. |
| Ttl | Integ er | Body | Yes | 300 | The time-to-live (TTL) of the cached record. |
| Prefix | Strin g | Body | Yes | www | The name of the scheduling domain. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the GTM instance. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | No | com. | The cached domain name. Partial match is supported. |

Apsara Stack DNS

##### DescribeCache

Queries the cached DNS records.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Type | Strin g | Body | No | A | The type of the cached record. Valid values: A: maps a domain name to an IPv4 address. AAAA: maps a domain name to an IPv6 address. CNAME: maps a domain name to another domain name. MX: maps a domain name to a mail server address. TXT: serves as a Sender Policy Framework (SPF) record to prevent email spam. The text can be up to 255 characters in length. PTR: maps an IP address to a domain name. SRV: specifies the servers that host specific services. NAPTR: records the Naming Authority Pointer (NAPTR) and is typically used for ENUM. CAA: specifies authorized certificate authorities (CAs) for a domain name. NS: maps a domain name to the specified DNS servers. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -RRset | Array |  |  |
| --Rdatas | String | ["10.200.0.4"] | The list of resolved IP addresses. |
| --Name | String | com. | The cached domain name. |

Apsara Stack DNS

**Response parameters**

| psara Stack DNS |  |  | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --Type | String | A | The type of the cached record. Valid values: A: maps a domain name to an IPv4 address. AAAA: maps a domain name to an IPv6 address. CNAME: maps a domain name to another domain name. MX: maps a domain name to a mail server address. TXT: serves as an SPF record to prevent email spam. The text can be up to 255 characters in length. PTR: maps an IP address to a domain name. SRV: specifies the servers that host specific services. NAPTR: records the NAPTR and is typically used for ENUM. CAA: specifies authorized CAs for a domain name. NS: maps a domain name to the specified DNS servers. |
| --Ttl | String | 300 | The time-to-live (TTL) of the cached record. |
| -Id | String | 343778269185 | The node ID. |
| -CmdAddr | String | 10.200.2.12:80 | The IP address of the service instance. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

Apsara Stack DNS `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Data":{
  "-RRset":{
   "Type":"A",
   "Rdatas":"[\"10.200.0.4\"]",
   "Ttl":"300",
   "Name":"com."
  },
  "CmdAddr":"10.200.2.12:80",
  "Id":"343778269185"
 },
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Data>
 <-RRset>
  <Type>A</Type>
  <Rdatas>[&quot;10.200.0.4&quot;]</Rdatas>
  <Ttl>300</Ttl>
  <Name>com.</Name>
 </-RRset>
 <CmdAddr>10.200.2.12:80</CmdAddr>
 <Id>343778269185</Id>
</Data> <Code>error code</Code>
```

##### DescribeDnsGtmInstances

Queries a list of Global Traffic Manager (GTM) instances.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | No | name | The name of the GTM instance. Partial match is supported. |
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the GTM instance. |
| -Name | String | name | The name of the GTM instance. |
| -ZoneId | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the scheduling domain. |
| -ZoneName | String | com. | The domain name. |
| -Prefix | String | www | The name of the scheduling domain. |
| -Ttl | Integer | 300 | The global time-to-live (TTL). |
| - CreateTimesta mp | Long | 1702460677 | The time when the GTM instance was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| - UpdateTimest amp | Long | 1702460677 | The time when the GTM instance was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |

Apsara Stack DNS

**Response parameters**

|  | Developer Guide·A | PI Reference |  | Apsara Stack DN | S |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeDnsGtmInstances &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "ZoneName":"com.",
  "ZoneId":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "VpcId":"",
  "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "Prefix":"www",
  "UpdateTimestamp":1702460677,
  "Ttl":300,
  "CreateTimestamp":1702460677,
  "Name":"name"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Ids | Strin g | Body | Yes | "1343778269181,34377 8269182,343778269183 " | The IDs of the nodes used for creating a cluster. Separate multiple IDs with commas (,). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <ZoneName>com.</ZoneName>
 <ZoneId>e8605e05-4320-4ef5-983d-c5dd48d05b49</ZoneId>
 <VpcId  />
 <Id>56bab908-04e0-44ee-b126-1cbdbcd24507
 </Id>
 <Prefix>www</Prefix>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <Ttl>300</Ttl>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>name</Name>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### EnableEmergencyGroup

Enables an emergency group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Developer Guide·A | PI Reference |  | Apsara Stack DN |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | error code | The error code returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableEmergencyGroup &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Code>error code </Code>
```

##### DisableEmergencyGroup

Disables an emergency group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Response parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | com. | The domain name, which must end with a period (.). |
| Masters | Strin g | Body | No | ["1.1.1.1:53","2.2.2.2:53" ] | The DNS server address of the primary domain name. |
| KeyName | Strin g | Body | No | my-tsig | The name of the Transaction Signature (TSIG) key. KeyName, KeyAlgorithm, and KeySecret must all be provided or all omitted. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DisableEmergencyGroup
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <Code>error code</Code>
```

##### AddGlobalZone

Creates a global internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| KeyAlgorit hm | Strin g | Body | No | HMAC-SHA512 | The algorithm used for the TSIG key. KeyName, KeyAlgorithm, and KeySecret must all be provided or all omitted. |
| KeySecret | Strin g | Body | No | Ok1qR5IW1ajVka5cHPEJ QIXfLyx5V3PSkFBROAzO n21JumDq6nIpoj6H8rfj5 Uo+Ok55ZWQ0Wgrf302 fDscHLw== | The value of the TSIG key. KeyName, KeyAlgorithm, and KeySecret must all be provided or all omitted. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The domain ID. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"\terror code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the ACL policy. |
| Remark | Strin g | Body | No | remark | The description of the ACL policy. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the ACL policy. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code> error code</Code>
```

##### UpdateRecursorAclRemark

Modifies the description of a recursive access control list (ACL) policy.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateRecursorAclRemark &Common request parameters
```

Sample success responses

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the forwarding domain name. |
| Name | Strin g | Body | Yes | com. | The forwarding domain name, which must end with a period (.). |
| ForwardM ode | Strin g | Body | Yes | FORWARD ONLY _ | The forwarding mode. Valid values: FORWARD ONLY _ (recommended): forwards all requests without recursion. FORWARD FIRST: falls _ back to recursive queries of public DNS servers if forwarding fails. |

Apsara Stack DNS `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message </Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507 </Id> <Code>error code </Code>
```

##### UpdateGlobalForwardZone

Modifies a global forwarding domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Forwarder s | Strin g | Body | Yes | ["1.1.1.1","1.1.1.2"] | The IP addresses of the DNS servers used for forwarding. |
| Remark | Strin g | Body | No | remark | The description of the global forwarding domain name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the forwarding domain name. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateGlobalForwardZone &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | com. | The domain name, which must end with a period (.). |
| RegionId | Strin g | Body | Yes | cn-region-env1-d01 | The region ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The domain ID. |

Apsara Stack DNS

##### AddPrivateZone

Creates a tenant-specific internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
&Name=com. &RegionId=cn-region-env1-d01 &Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | com. | The domain name, which must end with a period (.). |
| ForwardM ode | Strin g | Body | Yes | FORWARD ONLY _ | The forwarding mode. Valid values: FORWARD ONLY _ (recommended): forwards all requests without recursion. FORWARD FIRST: falls _ back to recursive queries of public DNS servers if forwarding fails. |
| Forwarder s | Strin g | Body | Yes | ["1.1.1.1","1.1.1.2"] | The IP addresses of the DNS servers used for forwarding. |
| RegionId | Strin g | Body | Yes | cn-region-env1-d01 | The region ID. |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### AddPrivateForwardZone

Creates a tenant-specific forwarding domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the forwarding domain name. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddPrivateForwardZone &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### UpdateDnsGtmAccessStrategy

Modifies an access policy.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | No | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The ID of the access policy. |
| GtmInstan ceId | Strin g | Body | No | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the Global Traffic Manager (GTM) instance. |
| Name | Strin g | Body | No | name | The name of the access policy. |
| LineIds | Strin g | Body | No | ["default"] | The line IDs. |
| DefaultGt mAddress PoolType | Strin g | Body | No | IPV4 | The type of the primary address pool. Valid values: DOMAIN: indicates a pool of domain names. IPv6: indicates a pool of IPv6 addresses. IPv4: indicates a pool of IPv4 addresses. |
| DefaultGt mAddress PoolId | Strin g | Body | No | b42155a3-029f-4d56- bfcb-0c82657dc7c7 | The ID of the primary address pool. |
| DefaultMi nAvailable AddrNum | Integ er | Body | No | 1 | The minimum number of available addresses in the primary address pool. |
| FailoverGt mAddress PoolId | Strin g | Body | No | 90b574f8-6978-46e4- be85-159232b981a7 | The ID of the secondary address pool. |
| FailoverGt mAddress PoolType | Strin g | Body | No | IPV4 | The type of the secondary address pool. Valid values: DOMAIN: indicates a pool of domain names. IPv6: indicates a pool of IPv6 addresses. IPv4: indicates a pool of IPv4 addresses. |

Apsara Stack DNS

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| FailoverMi nAvailable AddrNum | Integ er | Body | No | 1 | The minimum number of available addresses in the secondary address pool. |
| Specified GtmAddre ssPool | Strin g | Body | No | DEFAULT | The active address pool that you manually specify. Valid values: DEFAULT: the primary address pool. FAILOVER: the secondary address pool. |
| SwitchMo de | Strin g | Body | No | BY PROBE RESULT _ _ | The policy that determines which address pool (primary or secondary) is active. Valid values: BY HAND: manually _ determines which address pool is active. BY PROBE RESULT: _ _ automatically determines which address pool is active. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the access policy. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateDnsGtmAccessStrategy &Common request parameters
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the global forwarding domain name. |
| Remark | Strin g | Body | No | remark | The description of the global forwarding domain name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id> <Code>error code</Code>
```

##### UpdateGlobalForwardZoneRemark

Modifies the description of a global forwarding domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

|  | Developer Guide·A | PI Reference |  | Apsara Stack DN | S |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the global forwarding domain name. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The private line ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateGlobalForwardZoneRemark &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### DeletePrivateLine

Deletes a private line.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The private line ID. |

Apsara Stack DNS

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### BindZoneVpc

Associates a tenant-specific internal domain name with a virtual private cloud (VPC).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Vpcs | Repe atList | Body | Yes |  | The VPCs with which the tenant-specific internal domain name is associated. |
| -Id | Strin g |  | Yes | vpc- 9gd80vqxu8zq5j5st90yx | The VPC ID. |
| -Name | Strin g |  | No | vpc-name | The name of the VPC. |
| RegionId | Strin g | Body | Yes | cn-region-env1-d01 | The region ID of the VPC. |
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the tenant- specific internal domain name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the GTM instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the GTM instance. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Code>error code</Code>
```

##### DeleteDnsGtmAccessStrategy

Deletes an access policy.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteDnsGtmAccessStrategy &Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The domain ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The domain ID. |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### DeleteGlobalForwardZone

Deletes a global forwarding domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The domain ID. |
| Name | Strin g | Body | Yes | com. | The domain name, which must end with a period (.). |
| Masters | Strin g | Body | No | ["1.1.1.1:53","2.2.2.2:53" ] | The DNS server address of the primary domain name. |

Apsara Stack DNS

```
http(s)://[Endpoint]/?Action=DeleteGlobalForwardZone &Id=56bab908-04e0-44ee-b126-1cbdbcd24507 &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### UpdateGlobalZone

Modifies a global internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| KeyName | Strin g | Body | No | my-tsig | The name of the Transaction Signature (TSIG) key. KeyName, KeyAlgorithm, and KeySecret must all be provided or all omitted. |
| KeyAlgorit hm | Strin g | Body | No | HMAC-SHA512 | The algorithm used for the TSIG key. KeyName, KeyAlgorithm, and KeySecret must all be provided or all omitted. |
| KeySecret | Strin g | Body | No | Ok1qR5IW1ajVka5cHPEJ QIXfLyx5V3PSkFBROAzO n21JumDq6nIpoj6H8rfj5 Uo+Ok55ZWQ0Wgrf302 fDscHLw== | The value of the TSIG key. KeyName, KeyAlgorithm, and KeySecret must all be provided or all omitted. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The domain ID. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
&Id=56bab908-04e0-44ee-b126-1cbdbcd24507 &Name=com. &Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The ID of the ACL policy. |
| Name | Strin g | Body | Yes | Policy name | The name of the ACL policy. |
| Policy | Strin g | Body | Yes | true | Specifies whether to enable recursion. Valid values: true false |
| LineIds | Strin g | Body | Yes | ["default"] | The line IDs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### UpdateRecursorAcl

Modifies a recursive access control list (ACL) policy.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the ACL policy. |

**Examples**

Sample requests

```
&Id=e8605e05-4320-4ef5-983d-c5dd48d05b49 &Name=Policy name &Policy=true &LineIds=["default"] &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### UpdateGlobalZoneRecordRemark

Modifies the description of a DNS record for a global internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The DNS record ID. |
| Remark | Strin g | Body | No | remark | The description of the DNS record. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The DNS record ID. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateGlobalZoneRecordRemark &Id=56bab908-04e0-44ee-b126-1cbdbcd24507 &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | No | Policy name | The name of the policy. Partial match is supported. |
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -LineIds | String | ["default"] | The line IDs. |
| -Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the ACL policy. |
| -Name | String | name | The name of the ACL policy. |
| -Policy | String | true | Specifies whether to enable recursion. Valid values: true false |
| -Remark | String | remark | The description of the ACL policy. |
| - CreateTimesta mp | Long | 1702460677 | The time when the ACL policy was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |

Apsara Stack DNS

##### DescribeRecursorAcls

Queries a list of recursive access control list (ACL) policies.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| - UpdateTimest amp | Long | 1702460677 | The time when the ACL policy was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error messga | The error message returned. |
| Code | String | error code | The error code returned. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRecursorAcls &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error messga",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "Policy":"true",
  "LineIds":"[\"default\"]",
  "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "Name":"name",
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |
| Id | Strin g | Body | No | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The domain ID. |
| Name | Strin g | Body | No | com | The domain name. Partial match is supported. |
| RegionId | Strin g | Body | Yes | cn-region-env1-d01 | The region ID. |

Apsara Stack DNS `XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error messga</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <Policy>true</Policy>
 <LineIds>[&quot;default&quot;]</LineIds>
 <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>name</Name>
 <Remark>remark</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### DescribePrivateZones

Queries a list of tenant-specific internal domain names.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| - RegionAndVpc s | Array |  | The information about the associated virtual private clouds (VPCs) and region ID. |
| --Vpcs | Array |  | The VPCs with which the tenant-specific internal domain name is associated. |
| ---Id | String | vpc- 9gd80vqxu8zq5j5s t90yx | The VPC ID. |
| ---Name | String | vpc-name | The name of the VPC. |
| --RegionId | String | cn-region-env1- d01 | The region ID of the VPC. |
| -Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The domain ID. |
| -Name | String | com. | The domain name. |
| -CallerUid | String | 126760529569940 0 | The caller ID. This is a system parameter. |
| -VpcCount | Integer | 1 | The number of associated VPCs. |
| -RecordCount | Integer | 1 | The total number of DNS records. |
| - GtmInstanceC ount | Integer | 0 | The total number of Global Traffic Manager (GTM) instances created. |
| -Remark | String | remark | The description of the tenant-specific internal domain name. |
| - CreateTimesta mp | Long | 1702460677 | The time when the tenant-specific internal domain name was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |

Apsara Stack DNS

| Parameter | Type | Example | Description |
|---|---|---|---|
| - UpdateTimest amp | Long | 1702460677 | The time when the tenant-specific internal domain name was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePrivateZones &Common request parameters
```

Sample success responses `JSON` format Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "PageSize":10,
 "Message":"error message",
 "PageNumber":1,
 "Data":{
  "GtmInstanceCount":"",
  "VpcCount":1,
  "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "UpdateTimestamp":1702460677,
  "RecordCount":1,
  "CreateTimestamp":1702460677,
  "CallerUid":"",
  "-RegionAndVpcs":{
   "--Vpcs":{
    "Id":"vpc-9gd80vqxu8zq5j5st90yx",
    "Name":"vpc-name"
   },
   "RegionId":"cn-region-env1-d01"
  },
  "Name":"com.",
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | Policy name | The name of the ACL policy. |
| Policy | Strin g | Body | Yes | true | Specifies whether to enable recursion. Valid values: true false |
| LineIds | Strin g | Body | Yes | ["default"] | The line IDs. |

Apsara Stack DNS

```xml
<RequestId> 101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId>
 <PageSize>10</PageSize>
 <Message>error message</Message>
 <PageNumber>1</PageNumber>
 <Data>
  <GtmInstanceCount  />
  <VpcCount>1</VpcCount>
  <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id>
  <UpdateTimestamp>1702460677</UpdateTimestamp>
  <RecordCount>1</RecordCount>
  <CreateTimestamp>1702460677</CreateTimestamp>
  <CallerUid  />
  <-RegionAndVpcs>
   <--Vpcs>
    <Id>vpc-9gd80vqxu8zq5j5st90yx</Id>
    <Name>vpc-name</Name>
   </--Vpcs>
   <RegionId>cn-region-env1-d01</RegionId>
  </-RegionAndVpcs>
  <Name>com.</Name>
  <Remark>remark</Remark>
 </Data>
 <TotalItems>10</TotalItems>
 <Code>error code</Code>
```

##### AddRecursorAcl

Creates a recursive access control list (ACL) policy.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| psara Stack | DNS |  |  | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Remark | Strin g | Body | No | remark | The description of the ACL policy. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the ACL policy. |

**Response parameters**

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id> <Code>error code</Code>
```

##### UpdateDnsGtmMonitor

Modifies a health check configuration for address pools.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the health check configuration. |
| ProtocolTy pe | Strin g | Body | Yes | HTTP | The health check protocol. Valid values: ICMP TCP UDP HTTP HTTPS |
| GtmAddre ssPoolId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The address pool ID. |
| Enable | Boole an | Body | Yes | true | Specifies whether to enable probe. Valid values: true false |
| MonitorEx tendInfo | Json | Body | No | {"code":200,"path":"ind ex.htm","host":"aliyun.c om"} | The extended information. The required parameters vary based on the health check protocol. Parameters required for HTTP or HTTPS: port: the port used for the health check. host: the value of the Host header in the request. path: the URL path for the request. code: the threshold status code. The health check fails if the returned status code is greater than or equal to this value. Parameter required for TCP or UDP: port: the port used for the health check. Parameters required for ICMP: None. |

Apsara Stack DNS

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Interval | Integ er | Body | Yes | 15 | The health check interval. Unit: seconds. |
| Timeout | Integ er | Body | Yes | 3 | The timeout. Unit: seconds. |
| Evaluation Count | Integ er | Body | Yes | 5 | The number of retries. |
| AgentIds | Strin g | Body | Yes | ["agent-id1","agent-id1"] | The list of probe node IDs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the health check configuration. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateDnsGtmMonitor &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ZoneId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the tenant- specific internal domain name. |
| Name | Strin g | Body | No | www | The name of the DNS record. Partial match is supported. |
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -LineIds | String | ["default"] | The private line IDs. |
| -RDatas | Array |  |  |
| --Value | String | 1.1.1.1 | The value. |
| --LbaWeight | Integer | 100 | The load balancing weight. |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The DNS record ID. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### DescribePrivateZoneRecords

Queries a list of DNS records for a tenant-specific internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| psara Stack DNS |  |  | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Name | String | www | The name of the DNS record. |
| -CallerUid | String | 126760529569940 0 | The caller ID. This is a system parameter. |
| -ZoneId | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the tenant-specific internal domain name. |
| -ZoneName | String | com. | The name of the tenant-specific internal domain name. |
| -Type | String | A | The type of the DNS record. Valid values: A: maps a domain name to an IPv4 address. AAAA: maps a domain name to an IPv6 address. CNAME: maps a domain name to another domain name. MX: maps a domain name to a mail server address. TXT: serves as a Sender Policy Framework (SPF) record to prevent email spam. The text can be up to 255 characters in length. PTR: maps an IP address to a domain name. SRV: specifies the servers that host specific services. NAPTR: records the Naming Authority Pointer (NAPTR) and is typically used for ENUM. CAA: specifies authorized certificate authorities (CAs) for a domain name. NS: maps a domain name to the specified DNS servers. |
| -Ttl | Integer | 300 | The time-to-live (TTL) of the DNS record. |
| -LbaStrategy | String | ALL RR _ | The load balancing policy. Valid values: ALL RR: returns all addresses without _ applying a weight. RATIO: returns addresses by weight. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - CreateTimesta mp | Long | 1702460677 | The time when the DNS record was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| - UpdateTimest amp | Long | 1702460677 | The time when the DNS record was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -Remark | String | remark | The description of the DNS record. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePrivateZoneRecords &ZoneId=56bab908-04e0-44ee-b126-1cbdbcd24507 &Common request parameters
```

Sample success responses `JSON` format Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "ZoneId":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "LbaStrategy":"ALL_RR",
  "LineIds":"[\"default\"]",
  "Ttl":300,
  "CallerUid":"1267605295699400",
  "Name":"www",
  "Remark":"remark",
  "ZoneName":"com.",
  "Type":"A",
  "-RDatas":{
   "LbaWeight":100,
   "Value":"1.1.1.1"
  },
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |
| Name | Strin g | Body | No | com | The domain name. Partial match is supported. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <ZoneId>56bab908-04e0-44ee-b126-1cbdbcd24507</ZoneId>
 <LbaStrategy>ALL_RR</LbaStrategy>
 <LineIds>[&quot;default&quot;]</LineIds>
 <Ttl>300</Ttl>
 <CallerUid>1267605295699400
 </CallerUid>
 <Name>www</Name>
 <Remark>remark</Remark>
 <ZoneName>com.</ZoneName>
 <Type>A</Type>
 <-RDatas>
  <LbaWeight>100</LbaWeight>
  <Value>1.1.1.1</Value>
 </-RDatas>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### DescribeGlobalZones

Queries a list of global internal domain names.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The domain ID. |
| -Name | String | com. | The domain name. |
| -RecordCount | Integer | 1 | The total number of DNS records. |
| - GtmInstanceC ount | Integer | 0 | The total number of Global Traffic Manager (GTM) instances created. |
| -Remark | String | remark | The description of the global internal domain name. |
| - CreateTimesta mp | Long | 1702460677 | The time when the global internal domain name was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| - UpdateTimest amp | Long | 1702460677 | The time when the global internal domain name was last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

**Examples**

Sample requests Apsara Stack DNS

```
http(s)://[Endpoint]/?Action=DescribeGlobalZones &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "PageSize":10,
 "Message":"error message",
 "PageNumber":1,
 "Data":{
  "GtmInstanceCount":0,
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "RecordCount":1,
  "CreateTimestamp":1702460677,
  "Name":"com.",
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <PageSize>10</PageSize> <Message>error message</Message> <PageNumber>1</PageNumber> <Data>
 <GtmInstanceCount>0</GtmInstanceCount>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <RecordCount>1</RecordCount>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>com.</Name>
 <Remark>remark</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### DescribeDnsGtmLogs

Queries logs.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Keyword | Strin g | Body | No | keyword | The keyword that is used for the query. |
| EventType | Strin g | Body | No |  | The type of event by which you want to filter the logs. Valid values: addresspool-switch: An address pool switchover occurs. addresspool-became- unavailable: An address pool becomes unavailable. addresspool-became- available: An address pool becomes available again. address-became- unavailable: An address becomes unavailable. address-became- available: An address becomes available again. |
| StartTime stamp | Long | Body | No | 1707363894 | The beginning of the time range to query. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| EndTimest amp | Long | Body | No | 1707363894 | The end of the time range to query. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |

Apsara Stack DNS

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The log ID. |
| -Target | String | Destination DNS instance | The destination DNS instance. |
| - CreateTimesta mp | Long | 1707363894 | The time when the log was created. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -EventType | String |  | The type of event by which you filter the logs. Valid values: addresspool-switch: An address pool switchover occurs. addresspool-became-unavailable: An address pool becomes unavailable. addresspool-became-available: An address pool becomes available again. address-became-unavailable: An address becomes unavailable. address-became-available: An address becomes available again. |
| -Detail | String | detail | The details. |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests Apsara Stack DNS

```
http(s)://[Endpoint]/?Action=DescribeDnsGtmLogs &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "Target":"Destination DNS instance",
  "EventType":"",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "CreateTimestamp":1707363894,
  "Detail":"detail"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <Target>Destination DNS instance</Target>
 <EventType  />
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id>
 <CreateTimestamp>1707363894</CreateTimestamp>
 <Detail>detail</Detail>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### DeleteGlobalZone

Deletes a global internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the global internal domain name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the global internal domain name. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507 </Id> <Code>error code </Code>
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 343778269185 | The node ID. |
| Descriptio n | Strin g | Body | No | description | The description of the node. |
| AnycastAd drs | Strin g | Body | No | 10.1.0.12,10.1.0.13 | The anycast IP addresses. |
| RegionId | Strin g | Body | Yes | cn-region-env1-d01 | The region ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Id | String | 343778269185 | The node ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

##### UpdateNode

Modifies the information about a node.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ZoneId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the tenant- specific internal domain name. |
| Name | Strin g | Body | No | www | The name of the DNS record. |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"343778269185",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <Id>343778269185</Id> <Code>error code </Code>
```

##### AddPrivateZoneRecord

Creates a DNS record for a tenant-specific internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Type | Strin g | Body | Yes | A | The type of the DNS record. Valid values: A: maps a domain name to an IPv4 address. AAAA: maps a domain name to an IPv6 address. CNAME: maps a domain name to another domain name. MX: maps a domain name to a mail server address. TXT: serves as an SPF record to prevent email spam. The text can be up to 255 characters in length. PTR: maps an IP address to a domain name. SRV: specifies the servers that host specific services. NAPTR: records the NAPTR and is typically used for ENUM. CAA: specifies authorized CAs for a domain name. NS: maps a domain name to the specified DNS servers. |
| Ttl | Integ er | Body | Yes | 300 | The time-to-live (TTL) of the DNS record. |
| LbaStrate gy | Strin g | Body | Yes | ALL RR _ | The load balancing policy. Valid values: ALL RR: returns all _ addresses without applying a weight. RATIO: returns addresses by weight. |
| RDatas | Repe atList | Body | Yes |  |  |

Apsara Stack DNS

| Developer Gui | de·API R | eference |  |  | Apsara Stack DN |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| -Value | Strin g |  | Yes | 1.1.1.1 | The value. |
| - LbaWeigh t | Integ er |  | No | 100 | The load balancing weight. You do not need to specify this parameter if LbaStrategy is set to ALL RR. _ |
| LineIds | Strin g | Body | Yes | ["default"] | The line IDs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The DNS record ID. |

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddPrivateZoneRecord &ZoneId= &Type=A &Ttl=300 &LbaStrategy=ALL_RR &RDatas= &LineIds=["default"] &Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | name | The name of the address pool. |
| Type | Strin g | Body | Yes | A | The type of the address pool. Valid values: A: indicates a pool of IPv4 addresses. AAAA: indicates a pool of IPv6 addresses. CNAME: indicates a pool of domain names. |
| LbaStrate gy | Strin g | Body | Yes | ALL RR _ | The load balancing policy. Valid values: ALL RR: returns all _ addresses without applying a weight. RATIO: returns addresses by weight. |
| Addr | Repe atList | Body | Yes |  |  |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### AddDnsGtmAddressPool

Creates an address pool.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Developer Gui | de·API R | eference |  |  | Apsara Stack DN |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | Description |
| -Value | Strin g |  | Yes | 1.1.1.1 | The address value. |
| -Mode | Strin g |  | Yes | SMART | The health check mode of the address. Valid values: SMART: returns the address only if it is healthy. ONLINE: always returns the address. OFFLINE: never returns the address. |
| - LbaWeigh t | Integ er |  | No | 100 | The load balancing weight. You do not need to specify this parameter if LbaStrategy is set to ALL RR. _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The address pool ID. |

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddDnsGtmAddressPool &Name=name &Type=A &LbaStrategy=ALL_RR &Addr= &Common request parameters
```

Sample success responses

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the tenant- specific forwarding configuration. |
| Remark | Strin g | Body | No | remark | The description of the tenant-specific forwarding configuration. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### UpdatePrivateForwardZoneRemark

Modifies the description of a tenant-specific forwarding configuration.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Developer Guide·A | PI Reference |  | Apsara Stack DN |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the tenant-specific forwarding configuration. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdatePrivateForwardZoneRemark &Id=56bab908-04e0-44ee-b126-1cbdbcd24507 &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507 </Id> <Code>error code </Code>
```

##### BindForwardZoneVpc

Associates a tenant-specific forwarding domain name with one or more virtual private clouds (VPCs).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Vpcs | Repe atList | Body | Yes |  | The VPCs with which the tenant-specific forwarding domain name is associated. |
| -Id | Strin g |  | Yes | vpc- 9gd80vqxu8zq5j5st90yx | The VPC ID. |
| -Name | Strin g |  | No | vpc-name | The name of the VPC. |
| RegionId | Strin g | Body | Yes | cn-region-env1-d01 | The region ID. |
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the tenant- specific forwarding configuration. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=BindForwardZoneVpc &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Vpcs | Repe atList | Body | Yes |  |  |
| -Id | Strin g |  | Yes | vpc- 9gd80vqxu8zq5j5st90yx | The VPC ID. |
| -Name | Strin g |  | No | vpc-name | The name of the VPC. |
| RegionId | Strin g | Body | Yes | cn-region-env1-d01 | The region ID of the VPC. |
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the tenant- specific forwarding configuration. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Code>error code</Code>
```

##### DeleteForwardZoneVpc

Disassociates one or more virtual private clouds (VPCs) from a tenant-specific forwarding configuration.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the tenant- specific default forwarding configuration. |
| ForwardM ode | Strin g | Body | Yes | FORWARD ONLY _ | The forwarding mode. Valid values: FORWARD ONLY _ (recommended): forwards all requests without recursion. FORWARD FIRST: falls _ back to recursive queries of public DNS servers if forwarding fails. |

Apsara Stack DNS

```
http(s)://[Endpoint]/?Action=DeleteForwardZoneVpc &Vpcs= &RegionId=cn-region-env1-d01 &Id=56bab908-04e0-44ee-b126-1cbdbcd24507 &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Code>error code</Code>
```

##### UpdatePrivateDefaultForwardZone

Modifies a tenant-specific default forwarding configuration.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Forwarder s | Strin g | Body | Yes | ["1.1.1.1","1.1.1.2"] | The IP addresses of the DNS servers used for forwarding. |
| Remark | Strin g | Body | No | Remark | The description of the tenant-specific default forwarding configuration. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the tenant-specific default forwarding configuration. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdatePrivateDefaultForwardZone &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the global line. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the global line. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### DeleteGlobalLine

Deletes a global line.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The DNS record ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The DNS record ID. |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### DeleteGlobalZoneRecord

Deletes a DNS record for a global internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The DNS record ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The error message returned. |
| Code | String | error code | The error code returned. |

Apsara Stack DNS

```
http(s)://[Endpoint]/?Action=DeleteGlobalZoneRecord&Id=56bab908-04e0-44ee-b126-1cbdbcd2 &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### DeletePrivateZoneRecord

Delete a DNS record for a tenant-specific internal domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The DNS record ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeletePrivateZoneRecord &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

#### Cross-cloud API reference

##### Query node management list:

##### DescribeNodes

You can call the DescribeNodes operation to query the node management list.

**Request headers**

The DescribeNodes operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -AnycastAddr | String | 10.1.0.12,10.1.0.13 | The anycast service endpoint. |
| -Id | String | 343778269185 | The node ID. |
| -LocalAddr | String | 10.1.24.1 | The IP address of the node. |
| -RegionId | String | cn-region-env1- d01 | The region ID. |
| -Description | String | description | The description. |
| -Role | String | leader | The role type of the node. Valid values: leader: leader node (election node). follower: follower node (election node). learner: learner node (non-election node). candidate: abnormal status node. |
| -Index | Integer | 1 | The latest synchronized log ID. |
| -IsOnline | Boolean | true | The working status. Valid values: true: The node is working properly. false: The node is offline. |
| - IsInEmergency | Boolean | false | Indicates whether the node is in emergency group status. Valid values: true: The node is in emergency group status. false: The node is not in emergency group status. |

Apsara Stack DNS

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Total | Integer | 10 | The total number. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |

Apsara Stack DNS

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "PageSize":10,
 "Message":"error message",
 "PageNumber":1,
 "Total":10,
 "Data":{
  "Role":"leader",
  "Description":"description",
  "AnycastAddr":"10.1.0.12,10.1.0.13",
  "RaftServicePort":"",
  "IsInEmergency":false,
  "Index":1,
  "Id":"343778269185",
  "RegionId":"cn-region-env1-d01",
  "CmdServicePort":"",
  "LocalAddr":"10.1.24.1",
  "IsOnline":true
 },
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The line ID. |
| Priority | Integ er | Body | Yes | 1 | The line priority. The value 1 indicates the highest priority. A larger value indicates a lower priority. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <PageSize>10</PageSize> <Message>error message </Message> <PageNumber>1</PageNumber> <Total>10</Total> <Data>
 <Role>leader</Role>
 <Description>description</Description>
 <AnycastAddr>10.1.0.12,10.1.0.13
 </AnycastAddr>
 <RaftServicePort  />
 <IsInEmergency>false</IsInEmergency>
 <Index>1</Index>
 <Id>343778269185
 </Id>
 <RegionId>cn-region-env1-d01
 </RegionId>
 <CmdServicePort  />
 <LocalAddr>10.1.24.1</LocalAddr>
 <IsOnline>true</IsOnline>
</Data> <Code>error code </Code>
```

##### Modify the priority of a UniversalLine

**cross-cloud DNS line: UpdateUniversalLinePriority**

You can call the UpdateUniversalLinePriority operation to modify the priority of a cross-cloud DNS line.

**Request headers**

The UpdateUniversalLinePriority operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The line ID. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateUniversalLinePriority &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### Enable emergency group:

##### EnableEmergencyGroup

You can call the EnableEmergencyGroup operation to enable an emergency group.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Ids | Strin g | Body | Yes | "1343778269181,34377 8269182,343778269183 " | The IDs of the nodes that are used to create a new cluster (separated by commas). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The ID of the request. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |

Apsara Stack DNS The EnableEmergencyGroup operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

**Request parameters**

**Response parameters**

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=EnableEmergencyGroup &Common request parameters
```

Sample success response `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"",
 "Code":"error code"
}
```

`XML` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | com. | The name of the cross- cloud shared domain name (must end with a period "."). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The domain ID. |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id /> <Code>error code </Code>
```

##### Add UniversalZone global shared domain

**name: AddUniversalZone**

Call the AddUniversalZone operation to add a cross-cloud shared domain name.

**Request headers**

The AddUniversalZone operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddUniversalZone &Common request parameters
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The ID of the DNS record. |
| Remark | Strin g | Body | No | remark | The remark. |

Apsara Stack DNS Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### Modify the remark of a cross-cloud shared

**domain DNS record:**

**UpdateUniversalZoneRecordRemark**

You can call the UpdateUniversalZoneRecordRemark operation to modify the remark of a DNS record for a cross-cloud shared domain.

**Request headers**

The UpdateUniversalZoneRecordRemark operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The ID of the request. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the DNS record. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateUniversalZoneRecordRemark &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### Disable emergency group:

##### DisableEmergencyGroup

Call the DisableEmergencyGroup operation to disable an emergency group.

**Request headers**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The ID of the request. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |

Apsara Stack DNS The DisableEmergencyGroup operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

**Return data**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DisableEmergencyGroup
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id /> <Code>error code </Code>
```

##### Modify the remark of a UniversalZone

**cross-cloud shared domain name:**

**UpdateUniversalZoneRemark**

You can call the UpdateUniversalZoneRemark operation to modify the remark of a cross-cloud shared domain name.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The domain ID. |
| Remark | Strin g | Body | No | remark | The remark. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The domain ID. |

Apsara Stack DNS

**Request headers**

The UpdateUniversalZoneRemark operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateUniversalZoneRemark &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The line ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The line ID. |

Apsara Stack DNS

##### Delete UniversalLine cross-cloud DNS line:

**DeleteUniversalLine**

You can call the DeleteUniversalLine operation to delete a cross-cloud DNS line.

**Request headers**

The DeleteUniversalLine operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteUniversalLine &Id=e8605e05-4320-4ef5-983d-c5dd48d05b49 &Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The line ID. |
| Name | Strin g | Body | Yes | name | The line name. |
| Priority | Integ er | Body | Yes | 1 | The line priority. 1 indicates the highest priority. The larger the value, the lower the priority. |
| V4Addres ses | Strin g | Body | No | ["1.1.1.1","2.2.2.2"] | The IPv4 address list (at least one of IPv4 and IPv6 must be specified). |
| V6Addres ses | Strin g | Body | No | ["2400:3200::7777"] | The IPv6 address list (at least one of IPv4 and IPv6 must be specified). |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id> <Code>error code</Code>
```

##### Modify UniversalLine cross-cloud

**resolution line: UpdateUniversalLine**

You can call the UpdateUniversalLine operation to modify a cross-cloud resolution line.

**Request headers**

This operation uses common request headers without special request headers. For more information, see the common request parameters document.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The line ID. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateUniversalLine &Id=e8605e05-4320-4ef5-983d-c5dd48d05b49 &Name=name &Priority=1 &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### Modify DNS records of cross-cloud shared

**domain names: UpdateUniversalZoneRecord**

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The ID of the DNS record. |
| ZoneId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The ID of the cross-cloud shared domain name. |
| Name | Strin g | Body | No | www | The name of the DNS record. |

Apsara Stack DNS You can call the UpdateUniversalZoneRecord operation to modify DNS records of cross-cloud shared domain names.

**Request headers**

The UpdateUniversalZoneRecord operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

**Request parameters**

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Type | Strin g | Body | Yes | A | The type of the record. Valid values: A: Maps a domain name to an IPv4 address. AAAA: Maps a domain name to an IPv6 address. CNAME: Maps a domain name to another domain name. MX: Maps a domain name to a mail server address. TXT: Text with a length limit of 255 characters, typically used for SPF records (anti-spam). PTR: Records the domain name for reverse DNS lookup of an IP address. SRV: Records servers that provide specific services. NAPRT: Records domain name authority pointers, typically used for ENUM. CAA: Sets certificate authority authorization information for a domain name. NS: Points a domain name to specified DNS servers for resolution. |
| Ttl | Integ er | Body | Yes | 300 | The cache time of the record. |

Apsara Stack DNS

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| LbaStrate gy | Strin g | Body | Yes | ALL RR _ | The load balancing policy. Valid values: ALL RR: Returns all _ addresses (non- weighted). RATIO: Returns addresses based on weight (weighted). |
| RDatas | Repe atList | Body | Yes |  | The collection of record values. |
| -Value | Strin g |  | Yes | 1.1.1.1 | The value. |
| - LbaWeigh t | Integ er |  | No | 100 | The weight. This parameter is not required for non- weighted types. |
| LineIds | Strin g | Body | Yes | ["default"] | The list of lines. |
| Remark | Strin g | Body | No | remark | The remarks. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the DNS record. |

Apsara Stack DNS

**Returned data**

**Examples**

Sample requests

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 343778269185 | The node ID. |
| Descriptio n | Strin g | Body | No | description | The remarks. |
| AnycastAd drs | Strin g | Body | No | 10.1.0.12,10.1.0.13 | The anycast service address. |
| RegionId | Strin g | Body | Yes | cn-region-env1-d01 | The region ID. |

Apsara Stack DNS

```
http(s)://[Endpoint]/?Action=UpdateUniversalZoneRecord &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### Modify a node: UpdateNode

You can call the UpdateNode operation to modify a node.

**Request headers**

The UpdateNode operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Id | String | 343778269185 | The node ID. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |

Apsara Stack DNS

**Examples**

Sample requests

```
&Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"343778269185",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <Id>343778269185</Id> <Code>error code </Code>
```

##### Delete a cross-cloud shared domain

**name: DeleteUniversalZone**

You can call the DeleteUniversalZone operation to delete a cross-cloud shared domain name.

**Request headers**

The DeleteUniversalZone operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The domain ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The domain ID. |

Apsara Stack DNS

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteUniversalZone &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | 343778269185 | The node ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Id | String | 343778269185 | The ID of the node that is switched to the primary node. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |

Apsara Stack DNS

##### Switch a secondary node to the primary

**node: TransferLeadership**

You can call the TransferLeadership operation to switch a secondary node to the primary node.

**Request headers**

The TransferLeadership operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=TransferLeadership &Id=343778269185 &Common request parameters
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Ip | Strin g | Body | No | 1.1.1.1 | The IP address to query. IPv4 addresses support fuzzy query. IPv6 addresses support only term query. |
| Name | Strin g | Body | No | name | The name of the address pool (matched by inclusion). |
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |

Apsara Stack DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"343778269185",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>343778269185</Id> <Code>error code </Code>
```

##### Query UniversalLine cross-cloud DNS line

**list: DescribeUniversalLines**

You can call the DescribeUniversalLines operation to query the cross-cloud DNS line list.

**Request headers**

The DescribeUniversalLines operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -V4Addresses | String | ["1.1.1.1"] | The list of IPv4 addresses. |
| -V6Addresses | String | ["2400:3200::7777 "] | The list of IPv6 addresses. |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the line. |
| -Name | String | name | The name of the line. |
| -Priority | Integer | 1 | The priority of the line. The value 1 indicates the highest priority. A larger value indicates a lower priority. |
| - CreateTimesta mp | Long | 1702460677 | The timestamp when the line was created (in seconds). |
| - UpdateTimest amp | Long | 1702460677 | The timestamp when the line was modified (in seconds). |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeUniversalLines &Common request parameters
```

Sample success responses Apsara Stack DNS `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "V4Addresses":"[\"1.1.1.1\"]",
  "V6Addresses":"[\"2400:3200::7777\"]",
  "Priority":1,
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "Name":"name"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <V4Addresses>[&quot;1.1.1.1&quot;]</V4Addresses>
 <V6Addresses>[&quot;2400:3200::7777&quot;]</V6Addresses>
 <Priority>1</Priority>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>name</Name>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### Add UniversalLine cross-cloud DNS line:

**AddUniversalLine**

You can call the AddUniversalLine operation to add a cross-cloud DNS line.

**Request headers**

The AddUniversalLine operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Body | Yes | name | The name of the line. |
| Priority | Integ er | Body | Yes | 1 | The priority of the line. The value 1 indicates the highest priority. A larger value indicates a lower priority. |
| V4Addres ses | Strin g | Body | No | ["1.1.1.1","2.2.2.2"] | The list of IPv4 addresses. You must specify at least one of the V4Addresses and V6Addresses parameters. |
| V6Addres ses | Strin g | Body | No | ["2400:3200::7777"] | The list of IPv6 addresses. You must specify at least one of the V4Addresses and V6Addresses parameters. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The ID of the request. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the line. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Id | Strin g | Body | Yes | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | The ID of the record. |

Apsara Stack DNS

```
http(s)://[Endpoint]/?Action=AddUniversalLine &Name=name &Priority=1 &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### Delete a UniversalZone DNS record:

**DeleteUniversalZoneRecord**

You can call the DeleteUniversalZoneRecord operation to delete a DNS configuration record of a cross-cloud shared domain name.

**Request headers**

The DeleteUniversalZoneRecord operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" topic.

**Request parameters**

**Returned data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The ID of the request. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the record. |

Apsara Stack DNS

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteUniversalZoneRecord&Id=e8605e05-4320-4ef5-983d-c5dd4 8d05b49 &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### Get UniversalZone record list:

**DescribeUniversalZoneRecords**

You can call the DescribeUniversalZoneRecords operation to query the resolution configuration list of a cross-cloud shared domain name.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ZoneId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The domain ID. |
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |
| Name | Strin g | Body | No | www | The DNS record name (matched by inclusion). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -LineIds | String | ["default"] | The DNS line. |
| -RDatas | Array |  |  |
| --Value | String | 1.1.1.1 | The value. |
| --LbaWeight | String | 100 | The weight. |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | The ID of the record. |
| -Name | String | www | The record name. |
| -ZoneId | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The domain ID. |
| -ZoneName | String | com. | The domain name. |

Apsara Stack DNS The DescribeUniversalZoneRecords operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Type | String | A | The record type. Valid values: A: Maps a domain name to an IPv4 address. AAAA: Maps a domain name to an IPv6 address. CNAME: Maps a domain name to another domain name. MX: Maps a domain name to a mail server address. TXT: The text length is limited to 255 characters. This type is typically used for SPF records (anti-spam). PTR: Records the domain name for reverse DNS lookup of an IP address. SRV: Records servers that provide specific services. NAPRT: Records domain name authority pointers, typically used for ENUM. CAA: Sets certificate authority authorization information for a domain name. NS: Points a domain name to specified DNS servers for resolution. |
| -Ttl | Integer | 300 | The cache time of the record. |
| -LbaStrategy | String | ALL RR _ | The load balancing policy. Valid values: ALL RR: Returns all addresses (non- _ weighted). RATIO: Returns addresses based on weight (weighted). |
| -Remark | String | Remarks | The remarks. |
| - CreateTimesta mp | Long | 1702460677 | The creation timestamp (in seconds). |
| - UpdateTimest amp | Long | 1702460677 | The modification timestamp (in seconds). |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The message of the abnormal request. |

Apsara Stack DNS

| A | psara Stack DNS |  |  | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | error code | The code of the abnormal request. |
| TotalItems | Integer | 10 | The total number. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeUniversalZoneRecords?ZoneId=56bab908-04e0-44ee-b12 6-1cbdbcd24507&PageNumber=1&PageSize=10 &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "ZoneName":"com.",
  "Type":"A",
  "ZoneId":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "LbaStrategy":"ALL_RR",
  "-RDatas":{
   "LbaWeight":"100",
   "Value":"1.1.1.1"
  },
  "LineIds":"[\"default\"]",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "Ttl":300,
  "CreateTimestamp":1702460677,
  "Name":"www",
  "Remark":"Remarks"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | No | 1 | The page number. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. |
| Name | Strin g | Body | No | www | The domain name (matched by inclusion). |

Apsara Stack DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <ZoneName>com.</ZoneName>
 <Type>A</Type>
 <ZoneId>56bab908-04e0-44ee-b126-1cbdbcd24507</ZoneId>
 <LbaStrategy>ALL_RR</LbaStrategy>
 <-RDatas>
  <LbaWeight>100</LbaWeight>
  <Value>1.1.1.1</Value>
 </-RDatas>
 <LineIds>[&quot;default&quot;]</LineIds>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <Ttl>300</Ttl>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>www</Name>
 <Remark>Remarks</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### Get UniversalZone list:

**DescribeUniversalZones**

You can call the DescribeUniversalZones operation to query the list of cross-cloud shared domain names.

**Request headers**

The DescribeUniversalZones operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

**Request parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The domain ID. |
| -Name | String | com. | The domain name. |
| -RecordCount | Integer | 1 | The total number of DNS records. |
| - GtmInstanceC ount | Integer |  | Invalid field. |
| -Remark | String | Remarks | The remarks. |
| - CreateTimesta mp | Long | 1702460677 | The creation timestamp (in seconds). |
| - UpdateTimest amp | Long | 1702460677 | The modification timestamp (in seconds). |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| TotalItems | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |

Apsara Stack DNS

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeUniversalZones?PageNumber=1&PageSize=10 &Common request parameters
```

Apsara Stack DNS Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "PageSize":10,
 "Message":"error message",
 "PageNumber":1,
 "Data":{
  "GtmInstanceCount":"",
  "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "UpdateTimestamp":1702460677,
  "RecordCount":1,
  "CreateTimestamp":1702460677,
  "Name":"com.",
  "Remark":"Remarks"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <PageSize>10</PageSize> <Message>error message</Message> <PageNumber>1</PageNumber> <Data>
 <GtmInstanceCount  />
 <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <RecordCount>1</RecordCount>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>com.</Name>
 <Remark>Remarks</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### Add a UniversalZone DNS record:

**AddUniversalZoneRecord**

You can call the AddUniversalZoneRecord operation to add a DNS record for a cross-cloud shared domain name.

**Request headers**

The AddUniversalZoneRecord operation does not have operation-specific request headers and uses only common request headers. For more information, see the Common request parameters topic.

**Request parameters**

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ZoneId | Strin g | Body | Yes | 56bab908-04e0-44ee- b126-1cbdbcd24507 | The domain ID. |
| Name | Strin g | Body | No | www | The record name. |
| Type | Strin g | Body | Yes | A | The record type. Valid values: A: Maps a domain name to an IPv4 address. AAAA: Maps a domain name to an IPv6 address. CNAME: Maps a domain name to another domain name. MX: Maps a domain name to a mail server address. TXT: Text with a length limit of 255 characters, typically used for SPF records (anti-spam). PTR: Records the domain name for reverse DNS lookup of an IP address. SRV: Records servers that provide specific services. NAPRT: Records domain name authority pointers, typically used for ENUM. CAA: Sets certificate authority authorization information for a domain name. NS: Points a domain name to specified DNS servers for resolution. |
| Ttl | Integ er | Body | Yes | 300 | The cache time of the record. |

Apsara Stack DNS

| Developer Gui | de·API R | eference |  |  | Apsara Stack DN |
|---|---|---|---|---|---|

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| LbaStrate gy | Strin g | Body | Yes | ALL RR _ | The load balancing policy. Valid values: ALL RR: Returns all _ addresses (non- weighted). RATIO: Returns addresses based on weight (weighted). |
| Remark | Strin g | Body | No | Remark | The remark. |
| RDatas | Repe atList | Body | Yes |  | The collection of record values. |
| -Value | Strin g |  | Yes | 1.1.1.1 | The value. |
| - LbaWeigh t | Integ er |  | No | 100 | The weight. |
| LineIds | Strin g | Body | Yes | ["default"] | The DNS line. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | The request ID. |
| Message | String | error message | The message of the abnormal request. |
| Code | String | error code | The code of the abnormal request. |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | The ID of the DNS record. |

**Response parameters**

**Examples**

Sample requests Apsara Stack DNS

```json
http(s)://[Endpoint]/?Action=AddUniversalZoneRecord? ZoneId=aaa&Name=www&Type=A&Ttl=300&LbaStrategy=RATIO&Remark=remark&LineIds= ["default"]&RDatas.1.Value=1.1.1.1&RDatas.1.LbaWeight=100 &Common request parameters
```

Sample success responses `JSON` format

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` format

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```
