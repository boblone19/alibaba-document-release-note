---
title: "ApsaraDB for RDS Developer Guide 20260313"
product_version: "V3.18.6"
pdf_pages: 397
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 ApsaraDB for RDS Developer Guide 20260313.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E6%95%B0%E6%8D%AE%E5%BA%93RDS%20/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20ApsaraDB%20for%20RDS%20Developer%20Guide%2020260313.pdf"
converter: line-classifier (PyMuPDF)
---

# ApsaraDB for RDS Developer Guide 20260313

ApsaraDB for RDS

## Use ASAPI to call Apsara

**Stack SDKs**

### Preparations

#### Go to OpenAPI Explorer

You can go to OpenAPI Explorer from the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of your
browser and press the Enter key.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

The first time you log on to the Apsara Uni-manager Management Console, you must follow instructions to change the password of your account. For security purposes, your password must be 10 to 32 characters in length and must contain at least two of the following character types: Letters Digits Special characters, including ! @ # $ %
3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform operations based
on your logon scenarios: Scenario 1: The first time you log on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind an MFA device. b. Re-enter the username and password as described in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. Scenario 2: You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**. ApsaraDB for RDS

**Note**

For more information, see the **Bind a virtual MFA device to enable MFA** topic in
**Apsara Uni-manager Management Console User Guide** .
5. In the top navigation bar, choose **Products > Application Services > OpenAPI**
**Explorer**.

#### Obtain the information and the

**endpoint of an API operation**

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
| x-acs-regionid | The ID of the region, such as cn-hangzhou-*. |

ApsaraDB for RDS

#### Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. AccessKey pairs are used to implement symmetric encryption to verify the identity of requesters. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. This topic describes how to obtain an AccessKey pair.

**Prerequisites**

An account that assumes the operations administrator or level-1 organization administrator role is obtained. Only an operations administrator or a level-1 organization administrator can obtain an AccessKey pair of the organization.

**Background information**

AccessKey supports the following authorization methods: Use RAM to authorize the AccessKey ID and AccessKey secret to third-party requesters. Use STS to authorize the AccessKey ID, AccessKey secret, and security token to third-party requesters. This topic describes how to obtain an AccessKey pair authorized by RAM. We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions can occur.

| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For information about how to obtain an organization ID, see the "GetOrganizationList" section in Apsara Uni- manager Management Console Developer Guide. |
|---|---|
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance on which to perform operations. For example, you can query the ID of an Elastic Compute Service (ECS) instance from the ECS instance list. |

ApsaraDB for RDS

**Warning**

The AccessKey pair of a personal account is managed and controlled by the permission system of the Apsara Uni-manage Management Console. If you need to obtain the AccessKey pair of an account that has permissions on an organization, make sure that your operation is allowed by an administrator. This ensures security. The account that has permissions on an organization is a privileged account.

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
choose **User Information** from the shortcut menu.
3. In the **Apsara Stack AccessKey Pair** section, obtain the AccessKey pair.

**Note**

The AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide you with full permissions on Apsara Stack resources. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
ApsaraDB for RDS
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization navigation tree, click the name of the level-1 organization for which you
want to obtain AccessKey pairs.
5. Click **Management AccessKey** on the right side of the page.
6. In the AccessKey message, view the AccessKey pair of the organization.

#### Obtain the values of common request

**headers**

You must provide multiple request headers when you call API operations in Apsara Stack. This topic describes how to obtain the values of common request headers. This topic also explains the response parameters that are returned after you call API operations.

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the desired organization.
5. In the **Regions** list, obtain the region ID from the **Region Name** column.

**Obtain an organization ID**

You must call a specific API operation to obtain an organization ID. You can obtain an organization ID by using the online debugging feature in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI**
**Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top
navigation bar.
4. Move the pointer over the
icon and choose **Platform** > **Apsara Uni-manager**. Select
**2019-05-10** from the **Version** drop-down list.
5. Search for the `GetOrganizationList` operation and debug the operation online. Set the
name parameter to the name of the organization that you want to query and click Initiate Call. Obtain the organization ID from the **id** parameter on the **Call Result** tab. For more information about this operation, see the GetOrganizationList topic in Apsara Uni-manager Operations Console Developer Guide.

**Obtain a resource set ID**

You must call a specific API operation to obtain a resource set ID. You can obtain a resource set ID by using the online debugging feature in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI**
**Explorer**.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of a resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of an organization. |

ApsaraDB for RDS
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top
navigation bar.
4. Move the pointer over the
icon and choose **Platform** > **Apsara Uni-manager**. Select
**2019-05-10** from the **Version** drop-down list.
5. Search for the `ListResourceGroup` operation and debug the operation online. Obtain the
resource set ID from the **id** parameter on the **Call Result** tab. For more information about this operation, see the ListResourceGroup topic in Apsara Uni-manager Operations Console Developer Guide.

**Obtain an instance ID**

You can obtain the ID of an instance in the cloud service console of the Apsara Uni-manager Management Console. For example, to obtain the ID of an API gateway, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > Application Services > API Gateway.
3. In the left-side navigation pane, click **Instances**.
4. View the **instance ID** in the instance list.

**Response parameters**

The following table describes the additional response parameters that are returned by default when you call API operations to query the instances of cloud services.

#### Obtain access credentials assigned by

**STS**

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

STS allows you to manage temporary access credentials for your Apsara Stack resources. You can use STS to call API operations.

**Procedure**

|  | stsAK |
|---|---|
| RAM role |  |

ApsaraDB for RDS
1. Obtain the Apsara Stack Resource Name (ARN) of your `Resource Access Management (RAM)`
`role` . i. Log on to the Apsara Uni-manager Management Console. ii. In the upper-right corner of the homepage, click the profile picture and then click **User**
**Information**.
iii. On the page that appears, click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view the ARN of your `RAM role` . ApsaraDB for RDS

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
this example, the Elastic Compute Service (ECS) API is used. ApsaraDB for RDS

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

### Use POP to make API calls

#### Preparations

You can use the point of presence (POP) gateway to call API operations in Apsara Stack in the same way as in Alibaba Cloud public cloud. This topic describes the preparations before you use the POP gateway to call API operations.

**Background information**

To enable you to call API operations in the same way as that in Alibaba Cloud public cloud and have a more convenient and consistent experience, we recommend that you use the POP gateway to call API operations in Apsara Stack.

**Obtain service endpoints**

**Obtain an endpoint in OpenAPI Explorer**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI**
**Explorer**.
ApsaraDB for RDS
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top
navigation bar.
4. In the left-side navigation pane, select the cloud service that you want to manage.
5. Select an API version from the **Version** drop-down list.
6. In the API operation list, you can view all API operations of the current version.
7. Click the operation that you want to call. Obtain the endpoint from the Endpoint parameter
on the Parameter tab.

**Obtain an endpoint in Apsara Infrastructure Management**

To use the POP gateway to call API operations in Apsara Stack, you must obtain the required service endpoints. You can obtain service endpoints from Apsara Stack onsite O&M engineers You can also obtain service endpoints by yourself. In this example, API Gateway is used.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Apsara Infrastructure**
**Management** > **O&M Tools**.
3. In the left-side navigation pane, choose **O&M Tools** > **Service Registration Variable**
**Dashboard**.
4. On the Service Registration Variable Dashboard page, click **Advanced Filter**.
5. Enter `apigateway` in the Service Registration field and click **Search**.
icon.
6. In the **Service Registration** column of the `apigateway` service, click the
7. Click the text information in the **Service Registration** column of the `apigateway` service.
In the **Registration Variables** message, obtain the endpoint from the value of apigateway.openapi.endpoint.

**Obtain common parameters**

ApsaraDB for RDS You must obtain the parameters required when you use the POP gateway to call API operations, such as the organization ID, resource set ID, region ID, and instance ID. For more information, see Obtain the values of common request headers.

#### SDK for Java

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
IAcsClientclient=newDefaultAcsClient(profile);
```

ApsaraDB for RDS

```java
        IAcsClient client  new DefaultAcsClient(profile);
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
        }
    }
}
```

The following sample code provides an example on how to call ROA APIs. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06- 07. Sample code: ApsaraDB for RDS

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

ApsaraDB for RDS

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
        }
    }
}
```

**Important**

By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be ignored in the test environment, you can specify the following setting: Java

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Disable certificate verification for the client. clientConfig.setIgnoreSSLCerts(true)
```

#### SDK for Go

This topic describes how to use SDK for Go over the point of presence (POP) gateway.

**Usage notes**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample**
**Code** in the top navigation bar.
ApsaraDB for RDS

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues. Proceed with caution.

**Background information**

Remote Procedure Call (RPC) and Resource-Oriented Architecture (ROA) APIs are supported.

**Examples**

The following sample code provides an example on how to call RPC APIs. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code: ApsaraDB for RDS

```java
package main
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

The following sample code provides an example on how to call ROA APIs. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06- 07. Sample code: ApsaraDB for RDS

```java
package main
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

You can configure proxies for API calls in one of the following ways: Configure proxies by using environment variables. Set the HTTP_PROXY, HTTPS_PROXY, or NO_PROXY environment variable. Sample code: ApsaraDB for RDS

```
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

You can configure SSL verification for requests. If you set the HTTPSInsecure parameter to `true` , certificate verification is disabled. To ensure connection security, we recommend that you enable certificate verification. If you set the HTTPSInsecure parameter to `false` , certificate verification is enabled. By default, certificate authority (CA) certificates on the operating systems are used.

**Default value**

```
 false
```

**Configuration methods**

**Important**

By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be ignored in the test environment, you can specify the following settings: ApsaraDB for RDS

```
// If you configure the HTTPSInsecure parameter for a request, the setting takes effect only on the current request. request.SetHTTPSInsecure(true) // Set the HTTPSInsecure parame ter to true for the request. isInsecure := request.GetHTTPSInsecure() // Query the setting of the HTT PSInsecure parameter for the request.
```

If you do not configure the HTTPSInsecure parameter for a request, the setting for a client takes effect.

```
// If you configure the HTTPSInsecure parameter for the client, the setting takes effec t on all requests that are initiated by the client. client.SetHTTPSInsecure(true) // Set the HTTPSInsecure parameter to true for the client. isInsecure := client.GetHTTPSInsecure() // Query the setting of the HTTPSI nsecure parameter for the client.
```

#### SDK for Python

This topic describes how to use SDK for Python over the point of presence (POP) gateway.

**Usage notes**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample**
**Code** in the top navigation bar.

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues.Proceed with caution.

**Background information**

Only remote procedure call (RPC) APIs are supported.

**Example**

The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

```java
from aliyunsdkcore.client import AcsClient import os from aliyunsdkcore.request import CommonRequest
# Create an AcsClient instance.
client = AcsClient(
    "<AccessKey ID>",
    "<AccessKey Secret>",
```

ApsaraDB for RDS

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

ApsaraDB for RDS You can configure a proxy for API calls by setting the HTTP_PROXY or HTTPS_PROXY environment variable. Sample code:

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

ApsaraDB for RDS

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # The region ID.
    verify='./cacert.pem'  # The path of the certificate authority (CA) certificate.
```

)

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDBInstanc e | The operation that you want to perform. Set the value to CreateDBInstance. |
| DBInstanceClass | String | Yes | rds.mysql.s1.sm all | The instance type of the instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
| DBInstanceNetT ype | String | Yes | Internet | The network connection type of the instance. Valid values: Internet: Internet Intranet: internal network |
| DBInstanceStora ge | Integer | Yes | 20 | The storage capacity of the instance. Unit: GB. The storage capacity increases in increments of 5 GB. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
| Engine | String | Yes | MySQL | The database engine of the instance. Valid values: MySQL SQLServer PostgreSQL POLARDB |

ApsaraDB for RDS

## API reference

### Instance management

#### CreateDBInstance

Creates an ApsaraDB RDS instance. For more information about the instance types of ApsaraDB RDS instances, see **Instance**
**types** in **ApsaraDB RDS****Product Introduction**.

**Request parameters**

| EngineVersion | String | Yes | 5.6 | The version of the database engine. Valid values when Engine is set to MySQL: 5.5, 5.6, 5.7, and 8.0 Valid values when Engine is set to SQL Server: 2008r2, 08r2 ent ha, 2012, _ _ 2012 ent ha, 2012 std ha, _ _ _ _ 2012 web, 2014 std ha, _ _ _ 2016 ent ha, 2016 std ha, _ _ _ _ 2016 web, 2017 std ha, _ _ _ 2017 ent, 2019 std ha, and _ _ _ 2019 ent _ Valid values when Engine is set to PostgreSQL: 9.4, 10.0, 11.0, 12.0, and 13.0 Set the value to 11 when Engine is set to POLARDB. |
|---|---|---|---|---|
| PayType | String | Yes | Postpaid | The billing method of the instance. Set the value to Postpaid. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region. You can call the DescribeRegions operation to query the most recent region list. |
| SecurityIPList | String | Yes | 10.23.12.27/24 | The IP address whitelist of the instance. If the IP address whitelist contains more than one entry, separate the entries with commas (,). Each entry must be unique. The IP address whitelist can contain up to 1,000 entries. The entries in the IP address whitelist must be in one of the following formats: IP address. Example: 10.23.12.24. CIDR block. Example: 10.23.12.24/24. In this example, 24 indicates that the prefix of the CIDR block is 24 bits in length. You can replace 24 with a value within the range of 1 to 32. |
| DBInstanceStora geType | String | No | cloud ssd _ | The storage type of the instance. Valid values: local ssd: local SSD. This is the _ recommended storage type. cloud ssd: standard SSD. _ |
| SystemDBChars et | String | No | gbk | An invalid parameter. |

ApsaraDB for RDS

| DBInstanceDesc ription | String | No | Test database | The name of the instance. The name must be 2 to 255 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). _ Note The name cannot start with http:// or https://. |
|---|---|---|---|---|
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| ZoneId | String | No | cn-hangzhou-b | The zone ID of the primary instance. Note If you specify a virtual private cloud (VPC) and a vSwitch, you must specify the ZoneId parameter. If you specify the RDS High-availability Edition, you must also specify the ZoneIdSlave1 parameter, which specifies whether to use the single-zone deployment method or the multi-zone deployment method. If you specify the RDS Enterprise Edition, you must also specify the ZoneIdSlave1 and ZoneIdSlave2 parameters, which specify whether to use the single-zone deployment method or the multi-zone deployment method. |
| InstanceNetwork Type | String | No | Classic | The network type of the instance. Default value: Classic. Valid values: VPC Classic |

ApsaraDB for RDS

| ConnectionMode | String | No | Standard | The connection mode of the instance. Valid values: Standard: standard mode Safe: database proxy mode Note SQL Server 2012, SQL Server 2016, and SQL Server 2017 support only the standard mode. |
|---|---|---|---|---|
| VPCId | String | No | vpc- xxxxxxxxxxxx | The ID of the VPC. Note If you set the InstanceNetworkType parameter to VPC, you must specify the VPCId parameter. |
| VSwitchId | String | No | vsw- xxxxxxxxxxx | The ID of the vSwitch. If you specify more than one vSwitch ID, separate the vSwitch IDs with commas (,). Note If you set the InstanceNetworkType parameter to VPC, you must specify the VSwitchId parameter. |
| PrivateIpAddress | String | No | 172.16.201.69 | The internal IP address of the instance. The internal IP address must be within the CIDR block that is supported by the specified vSwitch. The system automatically assigns an internal IP address to the instance based on the VPCId and VSwitchId values. |
| UsedTime | String | No | None | An invalid parameter. |
| Period | String | No | None | An invalid parameter. |
| ResourceGroupI d | String | No | rg- acfmyxxxxxxxxx x | The ID of the resource group. |
| TunnelId | String | No | None | An invalid parameter. |

ApsaraDB for RDS

| Category | String | No | HighAvailability | The RDS edition of the instance. Valid values: Basic: Basic Edition HighAvailability: High- availability Edition AlwaysOn: Cluster Edition Finance: Enterprise Edition |
|---|---|---|---|---|
| ZoneIdSlave1 | String | No | cn-hangzhou-c | The zone ID of the secondary instance. If you set the ZoneIdSlave1 parameter to the same value as the ZoneId parameter, the single-zone deployment method is used. If you set the ZoneIdSlave1 parameter to a different value from the ZoneId parameter, the multi-zone deployment method is used. |
| ZoneIdSlave2 | String | No | cn-hangzhou-d | The zone ID of the logger instance. If you set the ZoneIdSlave2 parameter to the same value as the ZoneId parameter, the single-zone deployment method is used. If you set the ZoneIdSlave2 parameter to a different value from the ZoneId parameter, the multi-zone deployment method is used. |
| EncryptionKey | String | No | 0d24xxxx-da7b- 4786-b981- 9a164dxxxxxx | The ID of the key that is used to encrypt data on standard SSDs in the region of the instance. You can obtain the ID of the key from the Key Management Service (KMS) console. You can also create a key. Note If you specify the EncryptionKey parameter, disk encryption is automatically enabled. In this case, you must also specify the RoleARN parameter. Disk encryption cannot be disabled after it is enabled. |
| RoleARN | String | No | acs:ram::1406xx xxxx:role/aliyunr dsinstanceencry ptiondefaultrole | The Alibaba Cloud Resource Name (ARN) that is provided by your Alibaba Cloud account for Resource Access Management (RAM) users. RAM users can use the ARN to connect from ApsaraDB RDS to KMS. |
| DedicatedHostG roupId | String | No | None | An invalid parameter. |

ApsaraDB for RDS

| TargetDedicated HostIdForMaster | String | No | None | An invalid parameter. |
|---|---|---|---|---|
| TargetDedicated HostIdForSlave | String | No | None | An invalid parameter. |
| TargetDedicated HostIdForLog | String | No | None | An invalid parameter. |
| MultiAVZExPara m | String | No | None | An invalid parameter. |
| License mode _ | String | No | None | An invalid parameter. |
| BucketUrlImage | String | No | None | An invalid parameter. |
| BucketUrlPsuPat ch | String | No | None | An invalid parameter. |
| BucketUrlOpatch Tool | String | No | None | An invalid parameter. |
| DBName | String | No | None | An invalid parameter. |
| Port | String | No | None | An invalid parameter. |
| CharacterSetNa me | String | No | None | An invalid parameter. |
| DBNationalChar acterSet | String | No | None | An invalid parameter. |
| BackupRetentio nPeriod | String | No | None | An invalid parameter. |
| SwitchMode | String | No | None | An invalid parameter. |
| SyncMode | String | No | None | An invalid parameter. |
| TdeStatus | Integer | No | 0 | An invalid parameter. |

ApsaraDB for RDS

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm- uf6wjk5xxxxxxxxxx | The ID of the instance. |
| OrderId | String | 1007893702xxxxx | The ID of the order. |
| ConnectionStri ng | String | rm- uf6wjk5xxxxxxx.my sql.rds.aliyuncs.co m | The endpoint of the instance. Note The DBInstanceNetType parameter indicates whether the endpoint is an internal endpoint or a public endpoint. |
| Port | String | 3306 | The port that is used to connect to the instance. Note The DBInstanceNetType parameter indicates whether the port is an internal port or a public port. |
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | The ID of the request. |

ApsaraDB for RDS

**Note**

In the new version of SDK, the default timeout period on the client side is different from the default timeout period on the instance. If you use the new version of SDK to call this operation, a timeout error may be reported even if the operation is successfully called. To prevent this issue, you can set the ReadTimeout parameter to 20000 before you call this operation.

**Examples**

Sample requests

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidZoneId.NotS upported | The Specified vpc Zone not supported. | The error message returned because the specified zone does not allow you to create an instance in a VPC. Specify a different zone and try again. |

ApsaraDB for RDS

```
http(s)://rds.example.com/?Action=CreateDBInstance &RegionId=cn-hangzhou &Engine=MySQL &EngineVersion=5.6 &DBInstanceClass=rds.mysql.s1.small &DBInstanceStorage=20 &DBInstanceNetType=Internet &PayType=Postpaid &SecurityIPList=10.23.12.27/24 &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <OrderId>1007893702xxxxx</OrderId>
      <ConnectionString>rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com</ConnectionString>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <Port>3306</Port>
      <RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId>
```

`JSON` format

```json
{
    "OrderId": "1007893702xxxxx",
    "ConnectionString": "rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com",
    "DBInstanceId": "rm-uf6wjk5xxxxxxx",
    "Port": "3306",
    "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC"
}
```

| 400 | InvalidZone.NotSup ported | The Specified Zone not supported. | The error message returned because the specified region is invalid. |
|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDBInstanc e | The operation that you want to perform. Set the value to DeleteDBInstance. |
| DBInstanceId | String | Yes | rm- uf6wjk5********* * | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCz********** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

ApsaraDB for RDS

#### DeleteDBInstance

Releases an ApsaraDB RDS instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The read/write splitting feature is disabled for the instance. The instance is a primary, read-only, disaster recovery, or temporary instance.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DeleteDBInstance &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RestartDBInstan ce | The operation that you want to perform. Set the value to RestartDBInstance. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|

ApsaraDB for RDS `XML` format

```xml
  <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
  <RegionId>ap-southeast-1</RegionId>
```

`JSON` format

```json
{
  "RequestId":"65BDA532-28AF-4122-AA39-B382721EEE64",
  "RegionId":"ap-southeast-1"
}
```

#### RestartDBInstance

Restarts an ApsaraDB RDS instance. If a large number of transactions need to be submitted or rolled back, the restart process may be delayed for a minute. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance does not have ongoing backup tasks.

**Request parameters**

**Response parameters**

| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |
|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceAttribute | The operation that you want to perform. Set the value to DescribeDBInstanceAttribute. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx xxx | The ID of the instance. You can specify up to 30 instance IDs in a single request. Separate multiple instance IDs with commas (,). |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=RestartDBInstance &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
```

`JSON` format

```json
{
    "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

#### DescribeDBInstanceAttribute

Queries the details of one or more ApsaraDB RDS instances.

**Request parameters**

| Expired | String | No | False | Specifies whether the instance has expired. Valid values: True: The instances are expired. False: The instances are not expired. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of DBInstanceAtt ribute |  | Details of the attributes of the instances returned. |
| DBInstanceAtt ribute |  |  |  |
| DBInstanceId | String | rm- uf6wjk5xxxxxxxxxx | The ID of the instance. |
| PayType | String | Postpaid | The billing method of the instance. Valid values: Postpaid: pay-as-you-go Prepaid: subscription |
| DBInstanceTy pe | String | Primary | The role of the instance. Valid values: Primary: primary instance Readonly: read-only instance Guard: disaster recovery instance Temp: temporary instance |
| Category | String | Basic | The RDS edition of the instance. Valid values: Basic: Basic Edition HighAvailability: High-availability Edition AlwaysOn: Cluster Edition Finance: Enterprise Edition |
| InstanceNetwo rkType | String | Classic | The network type of the instance. Valid values: Classic VPC |
| RegionId | String | cn-hangzhou | The ID of the region. |
| ZoneId | String | cn-hangzhou-a | The ID of the zone. |

ApsaraDB for RDS

**Response parameters**

| ConnectionStri ng | String | rm- uf6wjk5xxxxxxxxxx .mysql.rds.aliyuncs .com | The internal endpoint of the instance. |
|---|---|---|---|
| Port | String | 3306 | The internal port that is used to connect to the instance. |
| Engine | String | MySQL | The database engine of the instance. |
| EngineVersion | String | 5.5 | The version of the database engine. |
| DBInstanceCla ssType | String | s | The instance family of the instance. Valid values: s: shared instance family x: general-purpose instance family d: dedicated instance family h: dedicated host instance family |
| DBInstanceCla ss | String | rds.mys2.small | The instance type of the instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
| DBInstanceMe mory | Long | 4096 | The memory capacity of the instance. Unit: MB. |
| DBInstanceSto rage | Integer | 10 | The storage capacity of the instance. Unit: GB. |
| DBInstanceNet Type | String | Internet | The network connection type of the instance. Valid values: Internet: Internet Intranet: internal network |
| DBInstanceSta tus | String | Running | The state of the instance. For more information, see Instance states. |
| DBInstanceDe scription | String | Test database | The description of the instance. |

ApsaraDB for RDS

| LockMode | String | Unlock | The lock state of the instance. Valid values: Unlock: The instance is not locked. ManualLock: The instance is manually locked. LockByExpiration: The instance is automatically locked after it expires. LockByRestoration: The instance is automatically locked before it is rolled back. LockByDiskQuota: The instance is automatically locked after the storage space is exhausted. LockReadInstanceByDiskQuota: The instance is a read-only instance that is automatically locked after the storage space is exhausted. |
|---|---|---|---|
| LockReason | String | instance expired _ | The reason why the instance is locked. |
| DBMaxQuantit y | Integer | 200 | The maximum number of databases that can be created on an instance. |
| AccountMaxQ uantity | Integer | 50 | The maximum number of accounts that can be created on an instance. |
| CreationTime | String | 2011-05- 30T12:11:04Z | The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| ExpireTime | String | 2019-03- 27T16:00:00Z | The expiration time of the instance. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Note Pay-as-you-go instances never expire. |
| MaintainTime | String | 00:00Z-02:00Z | The maintenance window of the instance. The time is displayed in UTC. In the ApsaraDB RDS console, the maintenance window is displayed in UTC+8. |
| AvailabilityVal ue | String | 100.0% | The availability of the instance. Unit: %. |
| MaxIOPS | Integer | 150 | The maximum number of I/O requests processed by the instance per second. |

ApsaraDB for RDS

| MaxConnectio ns | Integer | 60 | The maximum number of concurrent connections allowed by the instance. |
|---|---|---|---|
| MasterInstanc eId | String | rm- uf6wjk5xxxxxxxxxx | The ID of the primary instance. If this parameter is not returned, the instance is a primary instance. |
| IncrementSour ceDBInstanceI d | String | rm- uf6wjk5xxxxxxxxxx | The ID of the instance from which incremental data comes. The incremental data of a disaster recovery instance or read-only instance comes from its primary instance. If this parameter is not returned, the instance is a primary instance. |
| GuardDBInsta nceId | String | rm- uf64zsuxxxxxxxxxx | The ID of the disaster recovery instance attached to the primary instance. |
| TempDBInstan ceId | String | rm- uf64zsuxxxxxxxxxx | The ID of the temporary instance attached to the primary instance. |
| ReadOnlyDBIn stanceIds | Array of ReadOnlyDBIn stanceId |  | The IDs of the read-only instances attached to the primary instance. |
| ReadOnlyDBIn stanceId |  |  |  |
| DBInstanceId | String | rm-bpxxxxxxxxx | The ID of the read-only instance. |
| AdvancedFeat ures | String | LinkedServer | The advanced features that are separated by commas (,). This parameter is applicable only to instances that run SQL Server. Valid values: LinkedServer DistributeTransaction |
| AutoUpgradeM inorVersion | String | Auto | The method that is used to update the minor engine version of the instance. Valid values: Auto: automatic update. Manual: manual update. ApsaraDB RDS automatically updates the current minor engine version of the instance only when the current minor engine version is phased out. |
| Collation | String | Chinese PRC CI AS _ _ _ | The character set collation of the instance. |

ApsaraDB for RDS

| Developer Guide·A | PI reference |  | ApsaraDB for RD |
|---|---|---|---|

| ConnectionMo de | String | Standard | The connection mode of the instance. Valid values: Standard: standard mode Safe: database proxy mode |
|---|---|---|---|
| ConsoleVersio n | String | 2 | The type of the proxy that is enabled on the instance. Valid values: 1: shared proxy 2: dedicated proxy Note We recommend that you do not use this parameter. Use the ProxyType parameter instead. |
| CurrentKernel Version | String | rds 20181010 _ | The minor engine version of the instance. |
| DBInstanceSto rageType | String | local ssd _ | The storage type of the instance. Valid values: local ssd/ephemeral ssd: local SSD _ _ cloud ssd: standard SSD _ |
| DispenseMode | String | None | An invalid parameter. |
| EncryptionKey | String | None | An invalid parameter. |
| EncryptionKey | String | None | An invalid parameter. |
| Extra | Struct |  | An invalid parameter. |
| ActiveReplicaD BInstanceID | String | None | An invalid parameter. |
| DBInstanceId | List | None | An invalid parameter. |
| ReplicaGroupI D | String | None | An invalid parameter. |
| ReplicaGroupS tatus | String | None | An invalid parameter. |
| LatestKernelV ersion | String | rds 20201031 _ | The latest minor engine version that is supported by the instance. |

| MasterZone | String | 5454284 | The ID of the primary zone. |
|---|---|---|---|
| ProxyType | Integer | 1 | The type of the proxy that is supported by the instance. Valid values: 0: The instance does not support database proxies. 1: The instance supports shared proxies, which are known as the multi- tenant mode. 2: The instance supports dedicated proxies, which are known as the single- tenant mode. |
| ReadonlyInsta nceSQLDelaye dTime | String | 30 | The latency of data replication to the read- only instances. The read-only instances replicate data from the primary instance at the latency that is specified by the ReadonlyInstanceSQLDelayedTime parameter. Unit: seconds. |
| ResourceGrou pId | String | rg- acfmyxxxxxxxxxx | The ID of the resource group. |
| SecurityIPMod e | String | normal | The whitelist mode of the instance. Valid values: normal: standard whitelist mode safety: enhanced whitelist mode |
| SlaveConnecti onString | String | None | An invalid parameter. |
| SlaveZones | Array of SlaveZone |  | Details of secondary zones. |
| SlaveZone |  |  |  |
| ZoneId | String | cn-hangzhou-a | The zone ID of the instance. |
| TimeZone | String | Central Standard Time | The time zone of the instance. |
| VSwitchId | String | vsw-xxxxxx | The ID of the vSwitch. |
| VpcCloudInsta nceId | String | vpc- 23rsxdfxxxxxxx | The ID of the instance. This parameter is returned only when the instance resides in a virtual private cloud (VPC). |
| VpcId | String | vpc-xxxxxxxxx | The ID of the VPC. |

ApsaraDB for RDS

| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |
|---|---|---|---|

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceAttribute &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
  <RequestId>BD3A30D8-32E7-40CF-AAEA-6BFD4E3DC55E</RequestId>
  <Items>
        <DBInstanceAttribute>
              <DBInstanceMemory>8192</DBInstanceMemory>
              <ResourceGroupId>rg-acfmyxxxxxxxxxx</ResourceGroupId>
              <Port>3306</Port>
              <MasterZone>cn-hangzhou-h</MasterZone>
              <LatestKernelVersion>rds_20201031</LatestKernelVersion>
              <DBInstanceType>Primary</DBInstanceType>
              <ConsoleVersion>2</ConsoleVersion>
              <InstanceNetworkType>VPC</InstanceNetworkType>
              <DBInstanceClassType>x</DBInstanceClassType>
              <DBInstanceId>rm-uf6wjk5xxxxxxxxxx</DBInstanceId>
              <AutoUpgradeMinorVersion>Auto</AutoUpgradeMinorVersion>
              <DBInstanceStorage>150</DBInstanceStorage>
              <AvailabilityValue>100.0%</AvailabilityValue>
              <Engine>MySQL</Engine>
              <DBInstanceDescription>test1</DBInstanceDescription>
              <IPType>IPv4</IPType>
              <EngineVersion>8.0</EngineVersion>
              <DBInstanceStatus>Running</DBInstanceStatus>
              <MaxConnections>2000</MaxConnections>
              <DBInstanceClass>rds.mysql.s3.large</DBInstanceClass>
              <AccountMaxQuantity>99999</AccountMaxQuantity>
              <VSwitchId>vsw-xxxxxx</VSwitchId>
              <PayType>Prepaid</PayType>
              <LockMode>Unlock</LockMode>
              <GuardDBInstanceId>rm-uf64zsuxxxxxxxxxx</GuardDBInstanceId>
              <SupportCreateSuperAccount>No</SupportCreateSuperAccount>
              <InsId>1</InsId>
              <VpcId>vpc-xxxxxxxxx</VpcId>
              <CurrentKernelVersion>rds_20200831</CurrentKernelVersion>
              <TempUpgradeTimeStart>2021-01-10 00:00:00</TempUpgradeTimeStart>
              <TempUpgradeTimeEnd>2021-06-18 00:00:00</TempUpgradeTimeEnd>
              <CreationTime>2020-06-17T09:03:57Z</CreationTime>
              <ConnectionMode>Standard</ConnectionMode>
              <VpcCloudInstanceId>vpc-23rsxdfxxxxxxx</VpcCloudInstanceId>
<ProxyType>2</ProxyType>
```

ApsaraDB for RDS

```
oyype
```

/

```xml
oyype
              <ConnectionString>rm-
uf6wjk5xxxxxxxxxx.mysql.rds.aliyuncs.com</ConnectionString>
              <ExpireTime>2021-06-17T16:00:00Z</ExpireTime>
              <DBMaxQuantity>99999</DBMaxQuantity>
              <Category>HighAvailability</Category>
              <DBInstanceNetType>Intranet</DBInstanceNetType>
              <SuperPermissionMode></SuperPermissionMode>
              <DedicatedHostGroupId></DedicatedHostGroupId>
              <DBInstanceCPU>4</DBInstanceCPU>
              <GuardDBInstanceName>rm-m5xxxxx</GuardDBInstanceName>
              <SecurityIPList>42.xx.xx.xx</SecurityIPList>
              <OriginConfiguration></OriginConfiguration>
              <ReadOnlyDBInstanceIds>
        </ReadOnlyDBInstanceIds>
              <SecurityIPMode>normal</SecurityIPMode>
              <MaintainTime>23:00Z-00:00Z</MaintainTime>
              <DispenseMode>MultiAVZDispenseMode</DispenseMode>
              <ZoneId>cn-hangzhou-h</ZoneId>
              <DBInstanceStorageType>local_ssd</DBInstanceStorageType>
              <AccountType>Mix</AccountType>
              <MaxIOPS>5000</MaxIOPS>
              <SupportUpgradeAccountType>No</SupportUpgradeAccountType>
              <SlaveZones>
                    <SlaveZone>
                          <ZoneId>cn-hangzhou-h</ZoneId>
                    </SlaveZone>
              </SlaveZones>
              <Extra>
                    <DBInstanceIds>
            </DBInstanceIds>
              </Extra>
              <CanTempUpgrade>true</CanTempUpgrade>
              <RegionId>cn-hangzhou</RegionId>
        </DBInstanceAttribute>
  </Items>
```

`JSON` format

```json
{
    "RequestId": "BD3A30D8-32E7-40CF-AAEA-6BFD4E3DC55E",
    "Items": {
        "DBInstanceAttribute": [
            {
                "DBInstanceMemory": 8192,
                "ResourceGroupId": "rg-acfmyxxxxxxxxxx",
                "Port": "3306",
                "MasterZone": "cn-hangzhou-h",
                "LatestKernelVersion": "rds_20201031",
                "DBInstanceType": "Primary",
                "ConsoleVersion": "2",
                "InstanceNetworkType": "VPC",
                "DBInstanceClassType": "x",
"DBInstanceId" "rm f6jk5
```

" ApsaraDB for RDS

```json
                "DBInstanceId": "rm-uf6wjk5xxxxxxxxxx",
                "AutoUpgradeMinorVersion": "Auto",
                "DBInstanceStorage": 150,
                "AvailabilityValue": "100.0%",
                "Engine": "MySQL",
                "DBInstanceDescription": "test1",
                "IPType": "IPv4",
                "EngineVersion": "8.0",
                "DBInstanceStatus": "Running",
                "MaxConnections": 2000,
                "DBInstanceClass": "rds.mysql.s3.large",
                "AccountMaxQuantity": 99999,
                "VSwitchId": "vsw-xxxxxx",
                "PayType": "Prepaid",
                "LockMode": "Unlock",
                "GuardDBInstanceId": "rm-uf64zsuxxxxxxxxxx",
                "SupportCreateSuperAccount": "No",
                "InsId": 1,
                "VpcId": "vpc-xxxxxxxxx",
                "CurrentKernelVersion": "rds_20200831",
                "TempUpgradeTimeStart": "2021-01-10 00:00:00",
                "TempUpgradeTimeEnd": "2021-06-18 00:00:00",
                "CreationTime": "2020-06-17T09:03:57Z",
                "ConnectionMode": "Standard",
                "VpcCloudInstanceId": "vpc-23rsxdfxxxxxxx",
                "ProxyType": 2,
                "ConnectionString": "rm-uf6wjk5xxxxxxxxxx.mysql.rds.aliyuncs.com",
                "ExpireTime": "2021-06-17T16:00:00Z",
                "DBMaxQuantity": 99999,
                "Category": "HighAvailability",
                "DBInstanceNetType": "Intranet",
                "SuperPermissionMode": "",
                "DedicatedHostGroupId": "",
                "DBInstanceCPU": "4",
                "GuardDBInstanceName": "rm-m5xxxxx",
                "SecurityIPList": "42.xx.xx.xx",
                "OriginConfiguration": "",
                "ReadOnlyDBInstanceIds": {
                    "ReadOnlyDBInstanceId": []
                },
                "SecurityIPMode": "normal",
                "MaintainTime": "23:00Z-00:00Z",
                "DispenseMode": "MultiAVZDispenseMode",
                "ZoneId": "cn-hangzhou-h",
                "DBInstanceStorageType": "local_ssd",
                "AccountType": "Mix",
                "MaxIOPS": 5000,
                "SupportUpgradeAccountType": "No",
                "SlaveZones": {
                    "SlaveZone": [
                        {
                            "ZoneId": "cn-hangzhou-h"
                        }
```

]

```
},
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nces | The operation that you want to perform. Set the value to DescribeDBInstances. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| proxyId | String | No | API | The ID of the proxy mode. |

ApsaraDB for RDS

```json
                },
                "Extra": {
                    "DBInstanceIds": {
                        "DBInstanceId": []
                    }
                },
                "CanTempUpgrade": true,
                "RegionId": "cn-hangzhou"
            }
```

]

```
    }
}
```

#### DescribeDBInstances

Queries one or more ApsaraDB RDS instances that meet the specified conditions.

**Request parameters**

| Engine | String | No | MySQL | The database engine of the instance. Valid values: MySQL SQLServer PostgreSQL PolarDB By default, this operation returns the instances that run any of the supported database engines. |
|---|---|---|---|---|
| ZoneId | String | No | cn-hangzhou-a | The ID of the zone. |
| ResourceGroupI d | String | No | rg-acfmyxxxxx | The ID of the resource group. |
| DBInstanceStatu s | String | No | Running | The state of the instance. For more information, see Instance states. |
| Expired | String | No | True | Specifies whether to query the instances that have expired. Valid values: True: The instances are expired. False: The instances are not expired. |
| SearchKey | String | No | rm-uf6w | The keywords that are parts of the IDs or descriptions of the instances. |
| DBInstanceId | String | No | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| DBInstanceType | String | No | Primary | The role of the instance. Valid values: Primary: primary instance Readonly: read-only instance Guard: disaster recovery instance Temp: temporary instance By default, this operation returns the instances that assume any of the supported roles. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 1 to 100. Default value: 30. |

ApsaraDB for RDS

| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |
|---|---|---|---|---|
| InstanceNetwork Type | String | No | Classic | The network type of the instance. Valid values: VPC Classic By default, this operation returns the instances that reside in the classic network and virtual private clouds (VPCs). |
| VpcId | String | No | vpc- uf6f7l4fg90xxxx xxxxxx | The ID of the VPC. |
| VSwitchId | String | No | vsw- uf6adz52c2pxxx xxxxxxx | The ID of the vSwitch. |
| DBInstanceClass | String | No | rds.mys2.small | The instance type of the instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
| EngineVersion | String | No | 5.7 | The version of the database engine. |
| PayType | String | No | Postpaid | The billing method of the instance. Valid values: Postpaid: pay-as-you-go Prepaid: subscription |
| ConnectionMode | String | No | Standard | The connection mode of the instance. Valid values: Standard: standard mode Safe: database proxy mode By default, this operation returns the instances that are connected in standard mode and database proxy mode. |
| Tag.1.key | String | No | testkey1 | The first tag key. |
| Tag.2.key | String | No | testkey2 | The second tag key. |
| Tag.3.key | String | No | testkey3 | The third tag key. |

ApsaraDB for RDS

| Tag.4.key | String | No | testkey4 | The fourth tag key. |
|---|---|---|---|---|
| Tag.5.key | String | No | testkey5 | The fifth tag key. |
| Tag.1.value | String | No | testvalue1 | The value of the first tag key. |
| Tag.2.value | String | No | testvalue2 | The value of the second tag key. |
| Tag.3.value | String | No | testvalue3 | The value of the third tag key. |
| Tag.4.value | String | No | testvalue4 | The value of the fourth tag key. |
| Tag.5.value | String | No | testvalue5 | The value of the fifth tag key. |
| Tags | String | No | {"key1":"value1 "} | The tags that are added to the instance. Each tag is a key-value pair that consists of two parts: TagKey and TagValue. You can specify a maximum of five tags in the following format for each request: {"key1":"value1","key2":"value2"...}. |
| DedicatedHostG roupId | String | No | dhg- 7a9xxxxxxxx | The ID of the dedicated cluster to which the instance belongs. |
| DedicatedHostId | String | No | i-bpxxxxxxx | The ID of the host to which the instance belongs in the specified dedicated cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageRecordCo unt | Integer | 10 | The number of instances returned on the current page. |
| TotalRecordCo unt | Integer | 100 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| Items | Array of DBInstance |  | Details of the instances. |
| DBInstance |  |  |  |

ApsaraDB for RDS

**Response parameters**

| DBInstanceId | String | rm- uf6wjk5xxxxxxxxxx | The ID of the instance. |
|---|---|---|---|
| DBInstanceDe scription | String | Test database | The description of the instance. |
| PayType | String | Postpaid | The billing method of the instance. Valid value: Postpaid. |
| DBInstanceTy pe | String | Primary | The role of the instance. Valid values: Primary: primary instance ReadOnly: read-only instance Guard: disaster recovery instance Temp: temporary instance |
| InstanceNetwo rkType | String | Classic | The network type of the instance. Valid values: Classic VPC |
| ConnectionMo de | String | Performance | The connection mode of the instance. Valid values: Standard: standard mode Safe: database proxy mode |
| RegionId | String | cn-hangzhou | The ID of the region. |
| ExpireTime | String | 2019-02- 27T16:00:00Z | The expiration time of the instance. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Note Pay-as-you-go instances never expire. |
| DBInstanceSta tus | String | Running | The state of the instance. For more information, see Instance states. |
| Engine | String | MySQL | The database engine of the instance. |
| DBInstanceNet Type | String | Internet | The type of network connection to the instance. Valid values: Internet: Internet Intranet: internal network |

ApsaraDB for RDS

| LockMode | String | Unlock | The lock status of the instance. Valid values: Unlock: The instance is not locked. ManualLock: The instance is manually locked. LockByExpiration: The instance is automatically locked after it expires. LockByRestoration: The instance is automatically locked before it is rolled back. LockByDiskQuota: The instance is automatically locked after the storage space is exhausted. Released: The instance is released. After an instance is released, the instance cannot be unlocked. You can only restore the backup data of the instance to a new instance. This process requires a long period of time. |
|---|---|---|---|
| LockReason | String | instance expired _ | The reason why the instance is locked. |
| MasterInstanc eId | String | rm- uf6wjk5xxxxxxxxxx | The ID of the primary instance. If the value of this parameter is null, the instance is a primary instance. |
| GuardDBInsta nceId | String | rm- uf64zsuxxxxxxxxxx | The ID of the disaster recovery instance. This parameter is returned only when the instance is a primary instance and has a disaster recovery instance attached. |
| TempDBInstan ceId | String | rm- uf64zsuxxxxxxxxxx | The ID of the temporary instance. This parameter is returned only when the instance is a primary instance and has a temporary instance attached. |
| Category | String | Basic | The RDS edition of the instance. Valid values: Basic: Basic Edition HighAvailability: High-availability Edition Finance: Enterprise Edition |
| CreateTime | String | 2018-11- 05T11:26:02Z | The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |

ApsaraDB for RDS

| DBInstanceCla ss | String | rds.mys2.small | The instance type of the instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
|---|---|---|---|
| DBInstanceSto rageType | String | ModuleList.4.Modul eCode | The storage type of the instance. |
| DestroyTime | String | 2018-11- 05T11:26:02Z | The time when the instance was destroyed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DispenseMode | String | None | The deployment method of the instance. |
| EngineVersion | String | 5.7 | The version of the database engine. |
| InsId | Integer | 0 | An invalid parameter. |
| MasterZone | String | None | An invalid parameter. |
| MutriORsignle | Boolean | true | Indicates whether the multi-zone deployment method is used for the instance. Valid values: true and false. |
| ReadOnlyDBIn stanceIds | Array of ReadOnlyDBIn stanceId |  | The IDs of read-only instances if the primary instance has read-only instances attached. |
| ReadOnlyDBIn stanceId |  |  |  |
| DBInstanceId | String | rr-uf6wjk5xxxxxxx | The ID of the read-only instance. |
| ReplicateId | String | None | An invalid parameter. |
| ResourceGrou pId | String | rg-acfmyxxxxxxx | The ID of the resource group. |
| SlaveZones | Array of SlaveZone |  | The IDs of zones where the secondary instances reside. |
| SlaveZone |  |  |  |
| ZoneId | String | cn-hangzhou-h | The ID of the zone where the secondary instance resides. |

ApsaraDB for RDS

| VSwitchId | String | vsw- uf6adz52c2pxxxxx xx | The ID of the vSwitch. |
|---|---|---|---|
| VpcCloudInsta nceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. This parameter is returned only when the instance resides in a VPC. |
| VpcId | String | vpc- uf6f7l4fg90xxxxxx x | The ID of the VPC. |
| ZoneId | String | cn-hangzhou-a | The ID of the zone. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstances &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format ApsaraDB for RDS

```xml
  <TotalRecordCount>1</TotalRecordCount>
  <PageRecordCount>1</PageRecordCount>
  <RequestId>B4309486-26EF-47B3-ADDE-6140B4C1109D</RequestId>
  <PageNumber>1</PageNumber>
  <Items>
        <DBInstance>
              <ResourceGroupId>rg-acxxxxx</ResourceGroupId>
              <DBInstanceNetType>Intranet</DBInstanceNetType>
              <DBInstanceType>Primary</DBInstanceType>
              <MutriORsignle>false</MutriORsignle>
              <InstanceNetworkType>VPC</InstanceNetworkType>
              <DBInstanceId>rm-bpxxxxx</DBInstanceId>
              <ReadOnlyDBInstanceIds>
        </ReadOnlyDBInstanceIds>
              <LockReason></LockReason>
              <DBInstanceDescription>test</DBInstanceDescription>
              <Engine>MySQL</Engine>
              <EngineVersion>8.0</EngineVersion>
              <DBInstanceStatus>Running</DBInstanceStatus>
              <ZoneId>cn-hangzhou-h</ZoneId>
              <DBInstanceClass>rds.mysql.s3.large</DBInstanceClass>
              <CreateTime>2020-06-17T09:03:57Z</CreateTime>
              <VSwitchId>vsw-bpxxxxx</VSwitchId>
              <PayType>Prepaid</PayType>
              <LockMode>Unlock</LockMode>
              <GuardDBInstanceId>rm-m5xxxxx</GuardDBInstanceId>
              <InsId>1</InsId>
              <VpcId>vpc-bpxxxxx</VpcId>
              <VpcName>test-huadong</VpcName>
              <ConnectionMode>Standard</ConnectionMode>
              <VpcCloudInstanceId>rm-bpxxxxx-1</VpcCloudInstanceId>
              <RegionId>cn-hangzhou</RegionId>
              <ExpireTime>2021-06-17T16:00:00Z</ExpireTime>
        </DBInstance>
  </Items>
```

`JSON` format

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidDBInstanceT ype.ValueNotSuppo rt | The specified parameter"DBInstanceType" is not valid. | The error message returned because the specified instance type is invalid. Specify a valid instance type. |

ApsaraDB for RDS

```json
{
    "TotalRecordCount": 1,
    "PageRecordCount": 1,
    "RequestId": "B4309486-26EF-47B3-ADDE-6140B4C1109D",
    "PageNumber": 1,
    "Items": {
        "DBInstance": [
            {
                "ResourceGroupId": "rg-acxxxxx",
                "DBInstanceNetType": "Intranet",
                "DBInstanceType": "Primary",
                "MutriORsignle": false,
                "InstanceNetworkType": "VPC",
                "DBInstanceId": "rm-bpxxxxx",
                "ReadOnlyDBInstanceIds": {
                    "ReadOnlyDBInstanceId": []
                },
                "LockReason": "",
                "DBInstanceDescription": "test",
                "Engine": "MySQL",
                "EngineVersion": "8.0",
                "DBInstanceStatus": "Running",
                "ZoneId": "cn-hangzhou-h",
                "DBInstanceClass": "rds.mysql.s3.large",
                "CreateTime": "2020-06-17T09:03:57Z",
                "VSwitchId": "vsw-bpxxxxx",
                "PayType": "Prepaid",
                "LockMode": "Unlock",
                "GuardDBInstanceId": "rm-m5xxxxx",
                "InsId": 1,
                "VpcId": "vpc-bpxxxxx",
                "VpcName": "test-huadong",
                "ConnectionMode": "Standard",
                "VpcCloudInstanceId": "rm-bpxxxxx-1",
                "RegionId": "cn-hangzhou",
                "ExpireTime": "2021-06-17T16:00:00Z"
            }
```

]

```
    }
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eSpec | The operation that you want to perform. Set the value to ModifyDBInstanceSpec. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| PayType | String | Yes | Postpaid | The billing method of the instance. Set the value to Postpaid. |
| DBInstanceClass | String | No | rds.mys2.small | The instance type of the instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. You can call the DescribeAvailableClasses operation to query the instance types that are available in a region. Note You must specify at least one of the DBInstanceClass and DBInstanceStorage parameters. |

ApsaraDB for RDS

#### ModifyDBInstanceSpec

Changes the instance type or storage capacity of an ApsaraDB RDS instance. This operation is supported for primary and read-only instances. This operation is not supported for disaster recovery or temporary instances. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance does not have ongoing backup tasks. At least one of the DBInstanceClass and DBInstanceStorage parameters is specified in the request. If you want to decrease the storage capacity, the specified storage capacity is greater than or equal to 1.1 times the used storage capacity. The instance is a primary or read-only instance.

**Note**

If you want to upgrade the RDS edition of the instance, for example, from the Basic Edition to the High-availability Edition, you need only to select a proper instance type.

**Request parameters**

| DBInstanceStora ge | Integer | No | 20 | The storage capacity of the instance. Unit: GB. The storage capacity increases in increments of 5 GB. For more information, see Instance types in ApsaraDB RDS Product Introduction. You can also call the DescribeAvailableClasses operation to query the storage capacity range that is available for a specific instance type in a region. Note You must specify at least one of the DBInstanceStorage and DBInstanceClass parameters. If the instance runs MySQL on RDS High- availability Edition with local SSDs, you can decrease the storage capacity in decrements of 5 GB. |
|---|---|---|---|---|
| EffectiveTime | String | No | MaintainTime | The time when you want the specified settings to take effect. Valid values: Immediate: The settings take effect immediately. MaintainTime: The settings take effect during the maintenance window of the instance. Default value: Immediate. |
| SourceBiz | String | No | None | An invalid parameter. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

ApsaraDB for RDS

| Category | String | No | HighAvailability | The RDS edition of the instance. Valid values: Basic: Basic Edition HighAvailability: High- availability Edition Finance: Enterprise Edition |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3C5CFDEE-F774- 4DED-89A2- 1D76EC63C575 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceSpec &DBInstanceId=rm-uf6wjk5xxxxxxx &PayType=Postpaid &DBInstanceClass=rds.mys2.small &<Common request parameters>
```

Sample success responses `XML` format

```xml
  <RequestId>3C5CFDEE-F774-4DED-89A2-1D76EC63C575</RequestId>
  <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
  <OrderId>207938506080728</OrderId>
```

`JSON` format

```json
{
    "RequestId": "3C5CFDEE-F774-4DED-89A2-1D76EC63C575",
    "DBInstanceId": "rm-uf6wjk5xxxxxxx",
    "OrderId": 207938506080728
}
```

#### DescribeRegions

Queries the details of the regions that are available to ApsaraDB RDS. Before you call the CreateDBInstance operation to create an instance, you can call the DescribeRegions operation to query the available regions and zones.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of RDSRegion |  | Details of the available regions and zones. |
| RDSRegion |  |  |  |
| RegionId | String | cn-hangzhou | The ID of the region. |
| ZoneId | String | cn-hangzhou-b | The ID of the zone. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

ApsaraDB for RDS

**Note**

If a zone supports the multi-zone deployment method, the value of the ZoneId parameter for the zone contains an MAZ part. Examples: cn-hangzhou-MAZ6(b,f) and cn-hangzhou-MAZ5(b,e,f).

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
https://rds.example.com/?Action=DescribeRegions &<Common request parameters>
```

Sample success responses `XML` format ApsaraDB for RDS

```xml
  <RequestId>1CE1DC20-7EFC-464F-9583-0AB8915C5697</RequestId>
  <Regions>
        <RDSRegion>
              <ZoneId>cn-hangzhou-h</ZoneId>
              <RegionId>cn-hangzhou</RegionId>
              <LocalName>China (Hangzhou)</LocalName>
              <RegionEndpoint>rds.aliyuncs.com</RegionEndpoint>
        </RDSRegion>
        <RDSRegion>
              <ZoneId>cn-hangzhou-MAZ10(h,i)</ZoneId>
              <RegionId>cn-hangzhou</RegionId>
              <LocalName>China (Hangzhou)</LocalName>
              <RegionEndpoint>rds.aliyuncs.com</RegionEndpoint>
        </RDSRegion>
        <RDSRegion>
              <ZoneId>cn-hangzhou-MAZ8(f,g)</ZoneId>
              <RegionId>cn-hangzhou</RegionId>
              <LocalName>China (Hangzhou)</LocalName>
              <RegionEndpoint>rds.aliyuncs.com</RegionEndpoint>
        </RDSRegion>
  </Regions>
```

`JSON` format

```json
{
  "RequestId": "1CE1DC20-7EFC-464F-9583-0AB8915C5697",
  "Regions": {
    "RDSRegion": [
      {
        "ZoneId": "cn-hangzhou-h",
        "RegionId": "cn-hangzhou",
        "LocalName": "China (Hangzhou)",
        "RegionEndpoint": "rds.aliyuncs.com"
      },
      {
        "ZoneId": "cn-hangzhou-MAZ10(h,i)",
        "RegionId": "cn-hangzhou",
        "LocalName": "China (Hangzhou)",
        "RegionEndpoint": "rds.aliyuncs.com"
      },
      {
        "ZoneId": "cn-hangzhou-MAZ8(f,g)",
        "RegionId": "cn-hangzhou",
        "LocalName": "China (Hangzhou)",
        "RegionEndpoint": "rds.aliyuncs.com"
      }
```

]

```
  }
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | MigrateToOther Zone | The operation that you want to perform. Set the value to MigrateToOtherZone. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx xxx | The ID of the instance. |
| ZoneId | String | Yes | cn-hangzhou-b | The ID of the destination zone. You can call the DescribeRegions operation to query the most recent region list. |
| EffectiveTime | String | No | Immediate | The time when you want the change to take effect. Valid values: Immediate: The change takes effect immediately. MaintainTime: The change takes effect during the maintenance window of the instance. Default value: Immediate. |
| VSwitchId | String | No | vsw- uf6adz52c2pxxx xxxx | The ID of the vSwitch. Note This parameter must be specified when the instance resides in a virtual private cloud (VPC). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

ApsaraDB for RDS

#### MigrateToOtherZone

Migrates an ApsaraDB RDS instance across zones within the same region. For example, if an instance is located in Hangzhou Zone A, you can call this operation to migrate the instance to Hangzhou Zone B.

**Note**

You can migrate the instance between zones only within the same region. For example, you cannot migrate the instance from a zone in the China (Hangzhou) region to a zone in the China (Qingdao) region.

**Request parameters**

**Response parameters**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorrectDBInstanc eLockMode.ValueN otSupported | The Current DB instance lock mode does not support this operation. | The error message returned because the lock mode of the instance does not support this operation. |
| 403 | OperationDenied.O utofUsage | The resource is out of usage. | The error message returned because the specified zone does not provide sufficient resources. Select another zone and try again. |
| 404 | InvalidVPCId.NotFo und | Specified virtual vpc is not found. | The error message returned because the specified VPC ID does not exist. Check whether the VPC ID is correct. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=MigrateToOtherZone &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &ZoneId=cn-hangzhou-b &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
```

`JSON` format

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

#### ModifyDBInstanceDescription

Modifies the name of an ApsaraDB RDS instance.

**Request parameters**

| Action | String | Yes | ModifyDBInstanc eDescription | The operation that you want to perform. Set the value to ModifyDBInstanceDescription. |
|---|---|---|---|---|
| DBInstanceDesc ription | String | Yes | Instance in Alibaba Cloud test environment | The name of the instance. Note The name must be 2 to 64 characters in length. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx xxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 17F57FEE-EA4F- 4337-8D2E- 9C23CAA63D74 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceDescription &DBInstanceDescription=Instance in Alibaba Cloud test environment &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
           <RequestId>17F57FEE-EA4F-4337-8D2E-9C23CAA63D74</RequestId>
```

`JSON` format

```json
{
    "RequestId": " 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74"
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eMaintainTime | The operation that you want to perform. Set the value to ModifyDBInstanceMaintainTime. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| MaintainTime | String | Yes | 22:00Z-02:00Z | The maintenance window of the instance. Specify the time in the HH:mmZ-HH:mmZ format. The time must be in UTC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

ApsaraDB for RDS

#### ModifyDBInstanceMaintainTime

Modifies the maintenance window of an ApsaraDB RDS instance. You can set the maintenance window to a period of time during off-peak hours. Apsara Stack performs routine maintenance within the maintenance window to minimize impacts on your business.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceMaintainTime &DBInstanceId=rm-uf6wjk5xxxxxxx &MaintainTime=22:00Z-02:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
           <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCharact erSetName | The operation that you want to perform. Set the value to DescribeCharacterSetName. |
| Engine | String | Yes | mysql | The database engine of the instance. Valid values: mysql mssql PostgreSQL MariaDB |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CharacterSetN ameItems | List | ["gbk","utf8","euckr ","ascii"] | Details of the character sets that are supported for the instance. |
| Engine | String | mysql | The database engine of the instance. |
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | The ID of the request. |

ApsaraDB for RDS

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

#### DescribeCharacterSetName

Queries the character sets that are supported for an ApsaraDB RDS instance.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://example/?Action=DescribeCharacterSetName &Engine=mysql &RegionId=cn-hangzhou &<Common request parameters>
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceIpHostname | The operation that you want to perform. Set the value to DescribeDBInstanceIpHostname. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the ApsaraDB RDS instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the ApsaraDB RDS instance. |

ApsaraDB for RDS Sample success responses `XML` format

```xml
<RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId> <CharacterSetNameItems>
    <CharacterSetName>["gbk","utf8","euckr","ascii"]</CharacterSetName>
</CharacterSetNameItems> <Engine>mysql</Engine>
```

`JSON` format

```json
{
    "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC",
    "CharacterSetNameItems": {
        "CharacterSetName": "[\"gbk\",\"utf8\",\"euckr\",\"ascii\"]"
    },
    "Engine": "mysql"
}
```

#### DescribeDBInstanceIpHostname

Queries the hostname of the Elastic Compute Service (ECS) instance where an ApsaraDB RDS instance resides. ApsaraDB RDS instances are deployed based on ECS instances. This operation is used to query the hostname of the ECS instance where an ApsaraDB RDS instance resides. The hostname is required when you configure a distributed transaction whitelist. This operation is applicable only to ApsaraDB RDS High-availability Edition instances that run one of the following SQL Server versions: 2012 SE, 2012 EE, 2014 SE, 2016 SE, 2016 EE, and 2017 SE.

**Request parameters**

**Response parameters**

| IpHostnameInf os | String | 172.16.xx.xx,sdxxx xxxxxB;172.16.xx.x x,sdxxxxxxxxA | The internal IP addresses and hostnames of the ECS instances where the primary and secondary ApsaraDB RDS instances reside. Format: IP address 1,Hostname 1;IP address 2,Hostname 2. |
|---|---|---|---|
| RequestId | String | 67CD4719-51E3- 4A76-A38C- 02F45FAE7E36 | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyResource Group | The operation that you want to perform. Set the value to ModifyResourceGroup. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceIpHostname &DBInstanceId=rm-uf6wjk5xxxxxxx &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
  <IpHostnameInfos>172.16.xx.xx,sdxxxxxxxxB;172.16.xx.xxx,sdxxxxxxxxA</IpHostnameInfos>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <RequestId>67CD4719-51E3-4A76-A38C-02F45FAE7E36</RequestId>
```

`JSON` format

```json
{
    "IpHostnameInfos": "172.16.xx.xx,sdxxxxxxxxB;172.16.xx.xx,sdxxxxxxxxA",
    "DBInstanceId": "rm-uf6wjk5xxxxxxx",
    "RequestId": "67CD4719-51E3-4A76-A38C-02F45FAE7E36"
}
```

#### ModifyResourceGroup

Migrates an ApsaraDB RDS instance to a specified resource group. Resource Management enables you to build an organizational structure for resources based on your business needs. You can use a resource directory, folders, accounts, and resource groups to hierarchically organize and manage resources.

**Request parameters**

| DBInstanceId | String | Yes | rm-bpxxxxx | The ID of the instance. |
|---|---|---|---|---|
| ResourceGroupI d | String | Yes | rg-acxxxxx | The ID of the resource group. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyResourceGroup &DBInstanceId=rm-bpxxxxx &ResourceGroupId=rg-acxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
  <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
```

`JSON` format

```json
{
    "RequestId": "65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

| 400 | ResourceGroupId.In Valid | The Specified resource group id is not found. | The error message returned because the specified resource group ID does not exist. Check whether the ID is correct. |
|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateReadOnly DBInstance | The operation that you want to perform. Set the value to CreateReadOnlyDBInstance. |

ApsaraDB for RDS

### Read-only instances

#### CreateReadOnlyDBInstance

Creates a read-only instance for a primary ApsaraDB RDS instance.

**Before you call this operation, make sure that the following requirements are met:**

The primary instance cannot belong to a dedicated cluster and must run one of the following database engine versions and RDS editions: MySQL 8.0 on RDS High-availability Edition or Enterprise Edition MySQL 5.7 on RDS High-availability Edition or Enterprise Edition MySQL 5.6 SQL Server 2017 EE PostgreSQL 10, 11, or 12 on RDS High-availability Edition (If the primary instance runs PostgreSQL 10, it must be equipped with local SSDs.) If the primary instance runs MySQL, the number of read-only instances that are created cannot reach the upper limit. If the memory capacity of the primary instance is greater than or equal to 64 GB, up to 10 read-only instances can be created. If the memory capacity of the primary instance is less than 64 GB, up to five read-only instances can be created. If the primary instance runs SQL Server, up to seven read-only instances can be created. If the primary instance runs PostgreSQL with local SSDs, up to five read-only instances can be created. If the primary instance runs PostgreSQL with standard SSDs, up to 32 read-only instances can be created.

**Request parameters**

| DBInstanceClass | String | Yes | rds.mys2.small | The instance type of the read-only instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. We recommend that you specify an instance type higher than or equal to that of the primary instance. If the instance type of the read-only instance is lower than that of the primary instance, the read-only instance may encounter issues such as high latency or heavy load. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the primary instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| DBInstanceStora ge | Integer | Yes | 20 | The storage capacity of the read-only instance. Valid values: 5 to 3000. Unit: GB. The storage capacity increases in increments of 5 GB. Note The supported storage capacity range varies based on the RDS edition that is used. For more information, see the buy page of read-only instances. |
| EngineVersion | String | Yes | 5.6 | The major engine version of the read-only instance. The read-only instance must run the same major engine version as the primary instance. If the read-only instance runs MySQL, set this parameter to 5.6, 5.7, or 8.0. If the read-only instance runs SQL Server, set this parameter to 2017 ent or 2019 ent. _ _ If the read-only instance runs PostgreSQL, set this parameter to 10.0, 11.0, or 12.0. |
| PayType | String | Yes | Postpaid | The billing method of the read-only instance. Set the value to Postpaid. |

ApsaraDB for RDS

| RegionId | String | Yes | cn-hangzhou | The ID of the region. The read-only instance and the primary instance must reside in the same region. You can call the DescribeRegions operation to query the most recent region list. |
|---|---|---|---|---|
| ZoneId | String | Yes | cn-hangzhou-b | The ID of the zone. You can call the DescribeRegions operation to query the most recent zone list. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| DBInstanceStora geType | String | No | local ssd _ | The storage type of the read-only instance. Valid values: local ssd: local SSD _ cloud ssd: standard SSD _ Note ApsaraDB RDS for MySQL supports only local SSDs. ApsaraDB RDS for SQL Server supports only standard SSDs. |
| DBInstanceDesc ription | String | No | Test read-only instance | The description of the read-only instance. The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). The description _ must start with a letter. Note The description cannot start with http:// or https://. |

ApsaraDB for RDS

| InstanceNetwork Type | String | No | Classic | The network type of the read-only instance. Valid values: VPC Classic Default value: VPC. If you set this parameter to VPC, you must also specify the VPCId and VSwitchId parameters. Note The network type of the read-only instance can be different from that of the primary instance. |
|---|---|---|---|---|
| VPCId | String | No | vpc- uf6f7l4fg90xxxx xxxxxx | The virtual private cloud (VPC) ID of the read-only instance. If you leave the InstanceNetworkType parameter empty or set this parameter to VPC, you must specify the VPCId parameter. Note If local SSDs are used for the primary instance, the read-only instance can belong to a VPC different from that of the primary instance. If standard SSDs are used for the primary instance, the read-only instance must belong to the same VPC as the primary instance. |
| VSwitchId | String | No | vsw- uf6adz52c2pxxx xxxxxxx | The ID of the vSwitch of the read- only instance. If you leave the InstanceNetworkType parameter empty or set this parameter to VPC, you must specify the VSwitchId parameter. |

ApsaraDB for RDS

| PrivateIpAddress | String | No | 172.16.201.69 | The internal IP address of the read- only instance. The internal IP address must be within the CIDR block that is supported by the specified vSwitch. The system automatically assigns an internal IP address to the instance based on the VPCId and VSwitchId values. |
|---|---|---|---|---|
| ResourceGroupI d | String | No | rg- acfmyxxxxxxxxx x | The ID of the resource group. |
| Category | String | No | HighAvailability | The RDS edition of the read-only instance. Valid values: Basic: Basic Edition HighAvailability: High- availability Edition Note If the read-only instance runs PostgreSQL with standard SSDs, you must set this parameter to Basic. |
| DedicatedHostG roupId | String | No | None | An invalid parameter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rr-uf6wjk5xxxxxxx | The ID of the read-only instance. |
| OrderId | String | 10078937xxxxx | The ID of the order. |
| ConnectionStri ng | String | rr- xxxxx.mysql.rds.ali yuncs.com | The internal endpoint of the read-only instance. |
| Port | String | 3306 | The internal port number of the read-only instance. |
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidEngineVersio n.Malformed | The specified parameter "EngineVersion" is not valid. | The error message returned because the specified engine version is invalid. |
| 400 | InvalidSecurityIPLis t.Malformed | The specified parameter "SecurityIPList" is not valid. | The error message returned because the IP address whitelist of the instance is invalid. |

ApsaraDB for RDS

```
http(s)://rds.example.com/?Action=CreateReadOnlyDBInstance &RegionId=cn-hangzhou &ZoneId=cn-hangzhou-b &DBInstanceId=rm-uf6wjk5xxxxxxx &DBInstanceClass=rds.mys2.small &DBInstanceStorage=20 &EngineVersion=5.6 &PayType=Postpaid &VPCId=vpc-uf6f7l4fg90xxxxxxxxxx &VSwitchId=vsw-uf6adz52c2pxxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <OrderId>10078937xxxxx</OrderId>
      <ConnectionString>rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com</ConnectionString>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <Port>3306</Port>
      <RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId>
```

`JSON` format

```json
{
        "OrderId": "10078937xxxxx",
        "ConnectionString": "rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com",
        "DBInstanceId": "rm-uf6wjk5xxxxxxx",
        "Port": 3306,
        "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC"
    }
}
```

| 400 | InvalidSecurityIPLis t.Duplicate | The Security IP address is not in the available range or occupied. | The error message returned because the specified IP address is in use or is not within the valid range. Specify a valid IP address. |
|---|---|---|---|
| 400 | InvalidParameter | The specified parameter "dbInstanceId" is not valid. | The error message returned because the specified instance ID is invalid. Specify a valid instance ID. |
| 403 | OperationDenied.Pr imaryDBInstanceSt atus | The operation is not permitted due to status of primary instance. | The error message returned because the instance belongs to a dedicated cluster and is not in the running state. |
| 400 | OperationDenied | VPC IP is in use, please check. | The error message returned because the specified IP address in the VPC is already in use. |
| 404 | IncorrectDBInstanc eConnType | Current DB instance conn type does not support this operation. | The error message returned because the network connection type of the instance does not support this operation. |
| 400 | InvalidZoneId.NotS upported | The Specified vpc Zone not supported. | The error message returned because the specified zone does not allow you to create an instance in a VPC. Specify a different zone and try again. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeReadDB InstanceDelay | The operation that you want to perform. Set the value to DescribeReadDBInstanceDelay. |
| DBInstanceId | String | Yes | rm-bpxxxxxxx | The ID of the primary instance. |
| ReadInstanceId | String | Yes | rr-bpxxxxxxx | The ID of the read-only instance. |

ApsaraDB for RDS

#### DescribeReadDBInstanceDelay

Queries the latency of data replication between a primary ApsaraDB RDS instance and its read-only instance. Before you call this operation, make sure that the following requirements are met: The instance runs MySQL, PostgreSQL, or PolarDB. The primary instance has a read-only instance attached.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-bpxxxxxxx | The ID of the primary instance. |
| DelayTime | Integer | 0 | The latency of data replication between the primary instance and the read-only instance. |
| Items | Array of Items |  | Details of the latency information. |
| Items |  |  |  |
| DBInstanceId | String | rm-bpxxxxxxx | The ID of the primary instance. |
| ReadDBInstan ceNames | List | "ReadDBInstanceN ame": ["rr- bpxxxxx"] | The name of the read-only instance. Note This parameter is returned only when the primary instance runs the MySQL database engine. |
| ReadDelayTim es | List | "ReadDelayTime": ["0"] | The latency of data replication. Note This parameter is returned only when the primary instance runs the MySQL database engine. |
| ReadonlyInsta nceDelay | Array of ReadonlyInsta nceDelay |  | Details of the write-ahead log (WAL) latency. Note This parameter is returned only when the primary instance runs the PostgreSQL or PPAS database engine. |
| ReadonlyInsta nceDelay |  |  |  |
| FlushLag | String | 0 | The duration that is allowed for the latency in the persistence of WAL data. Unit: seconds. |
| FlushLatency | String | 0 | The data size that is allowed for the latency in the persistence of WAL data. Unit: MB. |

ApsaraDB for RDS

**Response parameters**

| ReadDBInstan ceName | String | rr-bpxxxxxxx | The name of the read-only instance. |
|---|---|---|---|
| ReplayLag | String | 0 | The duration that is allowed for the latency in the playback of WAL data. Unit: seconds. |
| ReplayLatency | String | 0 | The data size that is allowed for the latency in the playback of WAL data. Unit: MB. |
| SendLatency | String | 0 | The data size that is allowed for the latency in the sending of WAL data. Unit: MB. |
| WriteLag | String | 0 | The duration that is allowed for the latency in the write-back of WAL data. Unit: seconds. |
| WriteLatency | String | 0 | The data size that is allowed for the latency in the write-back of WAL data. Unit: MB. |
| ReadDBInstan ceId | String | rr-bpxxxxxxx | The ID of the read-only instance. |
| RequestId | String | F1BDDEA8-452D- 450B-AB10- CD5C5BAFC5DF | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeReadDBInstanceDelay &RegionId=cn-hangzhou &DBInstanceId=rm-bpxxxxxxx &ReadInstanceId=rr-bpxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format ApsaraDB for RDS

```xml
  <RequestId>11152741-D854-4E18-920E-64E75D484D57</RequestId>
  <DBInstanceId>rm-bpxxxxx</DBInstanceId>
  <Items>
        <Items>
              <ReadDBInstanceNames>
                    <ReadDBInstanceName>rr-bpxxxxx</ReadDBInstanceName>
              </ReadDBInstanceNames>
              <ReadDelayTimes>
                    <ReadDelayTime>0</ReadDelayTime>
              </ReadDelayTimes>
              <DBInstanceId>rm-bpxxxxx</DBInstanceId>
              <ReadonlyInstanceDelay>
        </ReadonlyInstanceDelay>
        </Items>
  </Items>
  <DelayTime>0</DelayTime>
```

`JSON` format

```json
{
    "RequestId": "11152741-D854-4E18-920E-64E75D484D57",
    "DBInstanceId": "rm-bpxxxxx",
    "Items": {
        "Items": [
            {
                "ReadDBInstanceNames": {
                    "ReadDBInstanceName": [
                        "rr-bpxxxxx"
```

]

```json
                },
                "ReadDelayTimes": {
                    "ReadDelayTime": [
                        "0"
```

]

```json
                },
                "DBInstanceId": "rm-bpxxxxx",
                "ReadonlyInstanceDelay": {
                    "ReadonlyInstanceDelay": []
                }
            }
```

]

```json
    },
    "DelayTime": "0"
}
```

### Version upgrade

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eAutoUpgradeMi norVersion | The operation that you want to perform. Set this value to ModifyDBInstanceAutoUpgradeM inorVersion. |
| AutoUpgradeMin orVersion | String | Yes | Auto | The method that is used to update the minor engine version of the instance. Valid values: Auto: automatic update. Manual: manual update. ApsaraDB RDS automatically updates the current minor engine version of the instance only when the current minor engine version is phased out. |
| DBInstanceId | String | Yes | rm-uf6wjk5xxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A31818D5-0550- 4A81-8D13- B45948D7193F | The ID of the request. |

ApsaraDB for RDS

**2.3.1.**

#### ModifyDBInstanceAutoUpgradeMinorVersion

Changes the method used to update the minor engine version of an ApsaraDB RDS instance. This operation is supported only for instances that run MySQL.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpgradeDBInsta nceKernelVersio n | The operation that you want to perform. Set the value to UpgradeDBInstanceKernelVersio n. |

ApsaraDB for RDS

```
http(s)://rds.example.com/?Action=ModifyDBInstanceAutoUpgradeMinorVersion &DBInstanceId=rm-uf6wjk5xxx &AutoUpgradeMinorVersion=Auto &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceAutoUpgradeMinorVersionResponse>
    <RequestId>A31818D5-0550-4A81-8D13-B45948D7193F</RequestId>
</ModifyDBInstanceAutoUpgradeMinorVersionResponse>
```

`JSON` format

```json
{
    "RequestId": "A31818D5-0550-4A81-8D13-B45948D7193F"
}
```

#### UpgradeDBInstanceKernelVersion

Updates the minor engine version of an ApsaraDB RDS instance. An update to the minor engine version enhances performance, introduces new features, and fixes known bugs. For more information, see Update the minor engine version of an ApsaraDB RDS for MySQL instance, Update the minor engine version of an ApsaraDB RDS for SQL Server instance, and Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance.

**Note**

This operation is supported only for instances that run the MySQL, SQL Server, or PostgreSQL database engine.

**Request parameters**

| DBInstanceId | String | Yes | rm-bpxxxxx | The ID of the instance. This operation is supported only for instances that run the MySQL, SQL Server, or PostgreSQL database engine. Note If your instance runs PostgreSQL, you must make sure that the instance is equipped with standard SSDs. If your instance is equipped with local SSDs, you can call the RestartDBInstance operation to restart the instance. In this case, your instance can automatically update to the latest minor engine version. If your instance runs SQL Server, you must make sure that the instance runs SQL Server 2019. |
|---|---|---|---|---|
| SwitchTime | String | No | 2020-01- 15T00:00:00Z | The specific point in time when you want to perform the update. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Note This parameter takes effect only when you set the UpgradeTime parameter to SpecifyTime. |
| SwitchTimeMode | String | No | Immediately | The method that is used to update the minor engine version. Valid values: Immediately: immediately updates the minor engine version. MaintainTime: updates the minor engine version during the maintenance window of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceNa me | String | rm-bpxxxxx | The ID of the instance. |

ApsaraDB for RDS

**Response parameters**

| RequestId | String | DA2ECBA0-4745- 4491-9166- 799FF8984AC9 | The ID of the request. |
|---|---|---|---|
| TargetMinorVe rsion | String | xcluster80 202103 _ 05 | The new minor engine version of the instance. |
| TaskId | String | 226917711 | The ID of the task. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=UpgradeDBInstanceKernelVersion &DBInstanceId=rm-bpxxxxx &UpgradeTime=SpecifyTime &SwitchTime=2020-01-15T00:00:00Z &TargetMinorVersion=xcluster80_20210305 &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <TaskId>226917711</TaskId>
      <RequestId>DA2ECBA0-4745-4491-9166-799FF8984AC9</RequestId>
      <TargetMinorVersion>xcluster80_20210305</TargetMinorVersion>
      <DBInstanceName>rm-bpxxxxx</DBInstanceName>
```

`JSON` format

```json
{
 "TaskId": "226917711",
 "RequestId": "DA2ECBA0-4745-4491-9166-799FF8984AC9",
 "TargetMinorVersion": "xcluster80_20210305",
 "DBInstanceName": "rm-bpxxxxx"
}
```

### Network and endpoint

**management**

#### AllocateInstancePublicConnection

Applies for a public endpoint for an ApsaraDB for RDS instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateInstance PublicConnectio n | The operation that you want to perform. Set the value to AllocateInstancePublicConnectio n. |
| ConnectionStrin gPrefix | String | Yes | test1234 | The prefix of the public endpoint. A complete public endpoint must be in the following format: <Prefix>. <Database engine name>.rds.aliyuncs.com. Example: test1234.mysql.rds.aliyuncs.com. Note The prefix must be 5 to 40 characters in length and can contain letters, digits, and hyphens (-).It cannot contain the following special characters: ~ ! # % ^ & * = + \| { } ; : ' " , < > / ? |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| Port | String | Yes | 3306 | The public port of the instance. Valid values: 1000 to 5999. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=AllocateInstancePublicConnection &ConnectionStringPrefix=test1234 &DBInstanceId=rm-uf6wjk5xxxxxxx &Port=3306 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AllocateInstancePublicConnectionResponse>
         <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</AllocateInstancePublicConnectionResponse>
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleaseInstance PublicConnectio n | The operation that you want to perform. Set the value to ReleaseInstancePublicConnection . |
| CurrentConnecti onString | String | Yes | rm- uf6wjk5xxxx.my sql.rds.aliyuncs. com | The public endpoint. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

ApsaraDB for RDS `JSON` format

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

#### ReleaseInstancePublicConnection

Releases the public endpoint of an ApsaraDB RDS instance. When you do not need to connect to an instance over the Internet, you can release its public endpoint to ensure data security.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ReleaseInstancePublicConnection &DBInstanceId=rm-uf6wjk5xxxxxxx &CurrentConnectionString=rm-uf6wjk5xxxx.mysql.rds.aliyuncs.com &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SwitchDBInstanc eNetType | The operation that you want to perform. Set the value to SwitchDBInstanceNetType. |
| ConnectionStrin gPrefix | String | Yes | test1234 | The prefix of the endpoint. The prefix must be 8 to 64 characters in length and can contain letters and digits. It must start with a lowercase letter. A complete endpoint must be in the following format: <Prefix>. <Database engine name>.rds.aliyuncs.com. Example: test1234.mysql.rds.aliyuncs.com. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

ApsaraDB for RDS

```xml
<ReleaseInstancePublicConnectionResponse>
         <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</ReleaseInstancePublicConnectionResponse>
```

`JSON` format

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

#### SwitchDBInstanceNetType

Switches an ApsaraDB RDS instance between its internal and public endpoints. To save endpoint resources, you can call this operation to switch an instance between its internal and public endpoints. After the endpoint that is used to connect to the instance is changed, you must update the endpoint information in the code of your application and restart the application. Before you call this operation, make sure that the following requirements are met: The instance is connected by using its internal or public endpoint. The instance is in the running state. The number of times that you have switched the instance between its internal and public endpoints within the last 24 hours does not reach 20. The instance resides in the classic network.

**Request parameters**

| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
|---|---|---|---|---|
| Port | String | No | 3306 | The number of the port that is used to connect to the instance. Valid values: 3001 to 3999. |
| ConnectionStrin gType | String | No | Normal | The type of the endpoint. Valid values: Normal ReadWriteSplitting If this parameter is not specified, the system returns both types of endpoints. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=SwitchDBInstanceNetType &DBInstanceId=rm-uf6wjk5xxxxxxx &ConnectionStringPrefix=rm-xxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceNetInfo | The operation that you want to perform. Set the value to DescribeDBInstanceNetInfo. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Flag | String | No | N/A | The hidden parameter. |
| DBInstanceNetR WSplitType | String | No | Normal | The type of the endpoint. Valid values: Normal ReadWriteSplitting Note By default, the system returns both types of endpoints. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceNet Infos | Array of DBInstanceNet Info |  | Details of the instance connection information. |
| DBInstanceNet Info |  |  |  |

ApsaraDB for RDS

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

#### DescribeDBInstanceNetInfo

Queries the connection information of an ApsaraDB RDS instance.

**Request parameters**

**Response parameters**

| ConnectionStri ng | String | rm- uf6wxxxxx.mysql.r ds.aliyuncs.com | The endpoint of the instance. |
|---|---|---|---|
| IPAddress | String | 192.168.12.84 | The IP address of the instance. |
| IPType | String | Public | The network type of the instance. Valid values when the instance resides in the classic network: Inner: internal network Public: Internet Valid values when the instance resides in a virtual private cloud (VPC): Private: internal network Public: Internet |
| Port | String | 3306 | The port that is used to connect to the instance. |
| VPCId | String | vpc- uf6f7l4fg90xxxxxx xxxx | The ID of the VPC. |
| VSwitchId | String | vsw- uf6adz52c2pxxxxx xxxxx | The ID of the vSwitch. |
| ConnectionStri ngType | String | Normal | The type of the endpoint. Valid values: Normal ReadWriteSplitting |
| MaxDelayTime | String | 12 | The latency threshold. This parameter is returned only for a read/write splitting endpoint. Unit: seconds. Note If the latency on a read- only instance exceeds the specified threshold, ApsaraDB RDS no longer routes read requests to the read-only instance. |
| DistributionTy pe | String | Standard | The policy that is used to allocate read weights. This parameter is returned only for a read/write splitting endpoint. Valid values: Standard: ApsaraDB RDS allocates a read weight to each instance based on the instance specifications. Custom: You must manually assign a read weight to each instance. |

ApsaraDB for RDS

| DBInstanceWe ights | Array of DBInstanceWe ight |  | Details of the weight. This parameter is returned only when the read/write splitting feature is enabled for the instance. |
|---|---|---|---|
| DBInstanceWe ight |  |  |  |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| DBInstanceTy pe | String | Master | The role of the instance. Valid values: Master: primary instance Readonly: read-only instance |
| Weight | String | 100 | The weight of the instance. |
| Availability | String | Unavailable | The availability of the instance. Valid values: Unavailable Available |
| ExpiredTime | String | 1209534 | The remaining time of the classic network in hybrid access mode. Unit: seconds. |
| SecurityIPGrou ps | Array of securityIPGrou p |  | Details of the IP address whitelist. |
| securityIPGrou p |  |  |  |
| SecurityIPGrou pName | String | Default | The name of the IP address whitelist. |
| SecurityIPs | String | 127.0.0.1 | The IP addresses contained in the IP address whitelist. |
| Upgradeable | String | Disabled | Indicates whether the IP version can be updated. Valid values: Enable and Disabled. Note The IP version can be updated from IPv4 to IPv6. |
| InstanceNetwo rkType | String | VPC | The network type. Valid values: Classic VPC |

ApsaraDB for RDS

| RequestId | String | 777C4593-8053- 427B-99E2- 105593277CAB | The ID of the request. |
|---|---|---|---|
| SecurityIPMod e | String | safety | The whitelist mode of the instance. Valid values: normal: standard whitelist mode safety: enhanced whitelist mode |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceNetInfo &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <dBInstanceNetInfos>
            <connectionString>rm-
uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com</connectionString>
            <connectionStringType>Normal</connectionStringType>
            <iPAddress>192.168.xx.xx</iPAddress>
            <iPType>Public</iPType>
            <port>3306</port>
            <upgradeable>Disabled</upgradeable>
            <vPCId></vPCId>
      </dBInstanceNetInfos>
      <instanceNetworkType>Classic</instanceNetworkType>
      <requestId>777C4593-8053-427B-99E2-105593277CAB</requestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eConnectionStri ng | The operation that you want to perform. Set the value to ModifyDBInstanceConnectionStri ng. |
| ConnectionStrin gPrefix | String | Yes | rm-xxxxxx | The prefix of the endpoint. Only the prefix of the CurrentConnectionString parameter value can be modified. Note The prefix must be 8 to 64 characters in length and can contain letters, digits, and hyphens (-).It cannot contain the following special characters: ~ ! # % ^ & * = + \ \| { } ; : ' " , < > / ? |

ApsaraDB for RDS

```json
{
    "dBInstanceNetInfos": [
        {
            "connectionString": "rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com",
            "connectionStringType": "Normal",
            "dBInstanceWeights": [],
            "iPAddress": "192.168.xx.xx",
            "iPType": "Public",
            "port": "3306",
            "securityIPGroups": [],
            "upgradeable": "Disabled",
            "vPCId": ""
        }
```

`],`

```json
    "instanceNetworkType": "Classic",
    "requestId": "777C4593-8053-427B-99E2-105593277CAB"
}
```

#### ModifyDBInstanceConnectionString

Modifies the endpoint and port number of an ApsaraDB RDS instance. ApsaraDB RDS provides the internal and public endpoints. It allows hybrid access by using both a Virtual Private Cloud (VPC) endpoint and a classic network endpoint.

**Note**

You can modify only the prefix of an endpoint. The read/write splitting endpoint cannot be modified.

**Request parameters**

| CurrentConnecti onString | String | Yes | rm- uf6wjk5xxxxxxx. mysql.rds.aliyun cs.com | The endpoint of the instance. It can be an internal endpoint, a public endpoint, or a classic network endpoint in hybrid access mode. Note The read/write splitting endpoint cannot be modified. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| Port | String | Yes | 3306 | The new port number of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceConnectionString &DBInstanceId=rm-uf6wjk5xxxxxxx &CurrentConnectionString=rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com &ConnectionStringPrefix=rm-xxxxxx &Port=3306 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceConnectionStringResponse>
         <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</ModifyDBInstanceConnectionStringResponse>
```

`JSON` format

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

Releases the endpoint of an ApsaraDB RDS instance.

#### ReleaseInstanceConnection

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleaseInstance Connection | The operation that you want to perform. Set the value to ReleaseInstanceConnection. |
| CurrentConnecti onString | String | Yes | rm- uf6wjk5xxxx.my sql.rds.aliyuncs. com | The public endpoint of the instance. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| InstanceNetwork Type | String | Yes | Classic | The network type of the instance. Valid values: VPC Classic |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

ApsaraDB for RDS

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ReleaseInstanceConnection &CurrentConnectionString=rm-uf6wjk5xxxx.mysql.rds.aliyuncs.com &DBInstanceId=rm-uf6wjk5xxxxxxx &InstanceNetworkType=Classic &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eNetworkType | The operation that you want to perform. Set the value to ModifyDBInstanceNetworkType. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| InstanceNetwork Type | String | Yes | Classic | The new network type of the instance. Valid values: VPC Classic |
| RetainClassic | String | No | True | Specifies whether to retain the classic network endpoint. Valid values: True: retains the classic network endpoint. False: does not retain the classic network endpoint. Default value: False. Note This parameter is valid when the network type is changed from classic network to VPC. |

ApsaraDB for RDS

```json
{
    "RequestId":"65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

#### ModifyDBInstanceNetworkType

Changes the network type of an ApsaraDB RDS instance. This operation is used to switch the network type of an instance between Virtual Private Cloud (VPC) and classic network.

**Request parameters**

| ClassicExpiredD ays | String | No | 7 | The number of days for which you want to retain the classic network endpoint. Valid values: 1 to 120. Default value: 7. Note This parameter is required if RetainClassic is set to True. |
|---|---|---|---|---|
| ReadWriteSplitti ngClassicExpired Days | Integer | No | 7 | The number of days for which you want to retain the read/write splitting endpoint of the classic network type. Valid values: 1 to 120. Default value: 7. Note This parameter is valid when a read/write splitting endpoint of the classic network type exists and when RetainClassic is set to True. |
| VPCId | String | No | vpc- uf6f7l4fg90xxxx xx | The ID of the VPC. |
| VSwitchId | String | No | vsw- uf6adz52c2pxxx xx | The ID of the vSwitch. This parameter is required if the VPCId parameter is specified. |
| PrivateIpAddress | String | No | 172.10.40.25 | The internal IP address of the instance, which must be within the CIDR block supported by the specified vSwitch. The system automatically assigns an internal IP address to the instance based on the VPCId and VSwitchId values. |

ApsaraDB for RDS

| ReadWriteSplitti ngPrivateIpAddr ess | String | No | 192.168.0.22 | The internal IP address corresponding to the read/write splitting endpoint of the instance, which must be within the CIDR block supported by the specified vSwitch. The system automatically assigns an internal IP address to the instance based on the VPCId and VSwitchId values. Note This parameter is valid when a read/write splitting endpoint of the classic network type exists. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |
| TaskId | String | 1025486523574 | The ID of the task. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceNetworkType &DBInstanceId=rm-uf6wjk5xxxxxxx &InstanceNetworkType=Classic &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
```

`JSON` format

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | NetTypeExists | Specified network type already exists. | The error message returned because the specified network type is the same as the original network type of the specified instance. |
| 403 | OperationDenied.D BInstanceConnTyp e | The current DB instance connection type does not support this operation. | The error message returned because the current network connection type does not support this operation. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SwitchDBInstanc eVpc | The operation that you want to perform. Set the value to SwitchDBInstanceVpc. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. Note The instance must run PostgreSQL with standard SSDs or run MySQL. The instance must be in the running state. The instance must reside in a VPC. The instance cannot be a temporary instance or a shared instance. |

ApsaraDB for RDS

#### SwitchDBInstanceVpc

Changes the virtual private cloud (VPC) or vSwitch of an ApsaraDB RDS instance. This operation is supported only for ApsaraDB RDS for PostgreSQL instances that use standard SSDs or ApsaraDB RDS for MySQL instances.

**Request parameters**

| VPCId | String | No | vpc- uf6f7l4fg90xxxx xxxxxx | The ID of the VPC. Note The VPC must belong to the same region as the instance. You can change the VPC of the instance only when the instance runs MySQL with local SSDs. |
|---|---|---|---|---|
| VSwitchId | String | No | vsw- uf6adz52c2pxxx xxxxxxx | The ID of the vSwitch. Note The vSwitch must belong to the same zone as the instance. |
| PrivateIpAddress | String | No | 10.23.xx.xx | The internal IP address of the instance, which must be within the CIDR block supported by the vSwitch specified by the VSwitchId parameter. Note You can call the DescribeVSwitches operation to query available vSwitches. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 777C4593-8053- 427B-99E2- 10xxxxxxxxxx | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=SwitchDBInstanceVpc &DBInstanceId=rm-uf6wjk5xxxxxxx &VPCId=vpc-uf6f7l4fg90xxxxxxxxxx &VSwitchId=vsw-uf6adz52c2pxxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>777C4593-8053-427B-99E2-10xxxxxxxxxx </RequestId>
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eNetworkExpire Time | The operation that you want to perform. Set the value to ModifyDBInstanceNetworkExpire Time. |
| ConnectionStrin g | String | Yes | rm- uf6wjk5xxxxx.m ysql.rds.aliyuncs .com | The classic network endpoint whose expiration time you want to extend. Valid values: Internal endpoint of the classic network Read/write splitting endpoint of the classic network |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| ClassicExpiredD ays | Integer | No | 7 | The number of days for which you want to extend the expiration time of the classic network endpoint. Valid values: 1 to 120. |
| RdsClassicexpire d | String | No | None | An invalid parameter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4C467B38-3910- 447D-87BC- AC049166F216 | The ID of the request. |

ApsaraDB for RDS `JSON` format

```json
{
    "RequestId": "777C4593-8053-427B-99E2-10xxxxxxxxxx"
}
```

#### ModifyDBInstanceNetworkExpireTime

Changes the expiration time of an endpoint for an ApsaraDB RDS instance. When an ApsaraDB RDS instance runs in hybrid access mode and provides both a VPC endpoint and a classic network endpoint, this operation is used to extend the expiration time of the retained classic network endpoint.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDatabase | The operation that you want to perform. Set the value to CreateDatabase. |

ApsaraDB for RDS

```
http(s)://rds.example.com/?Action=ModifyDBInstanceNetworkExpireTime &DBInstanceId=rm-uf6wjk5xxxxxxx &ConnectionString=rm-uf6wjk5xxxxx.mysql.rds.aliyuncs.com &ClassicExpiredDays=7 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceNetworkExpireTimeResponse>
      <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    </ModifyDBInstanceNetworkExpireTimeResponse>
```

`JSON` format

```json
{
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216"
}
```

### Database management

#### CreateDatabase

Creates a database on an ApsaraDB RDS instance. If you want to perform data management tasks such as data change and schema design, use Data Management System (DMS). Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The maximum number of databases in the instance is not reached. You can call the DescribeDBInstanceAttribute operation to query the maximum number of databases. The instance is not a read-only instance.

**Note**

This operation is not supported for instances that run PostgreSQL with local SSDs or SQL Server 2017 EE. You can execute the CREATE DATABASE statement to create a database.

**Request parameters**

| CharacterSetNa me | String | Yes | gbk | The character set. Valid values for MySQL databases: utf8, gbk, latin1, and utf8mb4 Valid values for SQL Server databases: Chinese PRC CI AS, _ _ _ Chinese PRC CS AS, _ _ _ SQL Latin1 General CP1 CI AS _ _ _ _ _ , SQL Latin1 General CP1 CS A _ _ _ _ _ S, and Chinese PRC BIN _ _ Valid values for PostgreSQL databases: KOI8U, UTF8, WIN866, WIN874, WIN1250, WIN1251, WIN1252, WIN1253, WIN1254, WIN1255, WIN1256, WIN1257, WIN1258, EUC CN, _ EUC KR, EUC TW, EUC JP, _ _ _ EUC JIS 2004, KOI8R, _ _ MULE INTERNAL, LATIN1, _ LATIN2, LATIN3, LATIN4, LATIN5, LATIN6, LATIN7, LATIN8, LATIN9, LATIN10, ISO 8859 5, ISO 8859 6, _ _ _ _ ISO 8859 7, ISO 8859 8, and _ _ _ _ SQL ASCII _ |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx xxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| DBName | String | Yes | rds mysql _ | The name of the database. Note The name must be 2 to 64 characters in length. The name must start with a lowercase letter and end with a lowercase letter or a digit. The name can contain lowercase letters, digits, underscores ( ), and _ hyphens (-). The name must be unique within the instance. For information about invalid characters, see Forbidden keywords. |

ApsaraDB for RDS

| DBDescription | String | No | Test database | The description of the database. It must be 2 to 256 characters in length. It must start with a letter and can contain letters, digits, underscores ( ), and hyphens (-). _ Note The description cannot start with http:// or https:// . |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5A77D650-27A1- 4E08-AD9E- 59008EDB6927 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
&DBInstanceId=rm-uf6wjk5xxxxxxxxxx &DBName=rds_mysql &CharacterSetName=gbk &<Common request parameters>
```

Sample success responses `XML` format

```xml
    <RequestId>5A77D650-27A1-4E08-AD9E-59008EDB6927</RequestId>
```

`JSON` format

```json
{
    "RequestID":"5A77D650-27A1-4E08-AD9E-59008EDB6927"
  }
```

#### DeleteDatabase

Deletes a database from an ApsaraDB RDS instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is a primary instance. The instance runs the MySQL or SQL Server database engine.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDatabase | The operation that you want to perform. Set the value to DeleteDatabase. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| DBName | String | Yes | testdb01 | The name of the database. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 07F6177E-6DE4- 408A-BB4F- 0723301340F3 | The ID of the request. |

ApsaraDB for RDS

**Note**

This operation is not supported for instances that run PostgreSQL. You can execute the DROP DATABASE statement to delete a database.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
&DBInstanceId=rm-uf6wjk5xxxxxxx &DBName=testdb01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>07F6177E-6DE4-408A-BB4F-0723301340F3</RequestId>
```

`JSON` format

```json
{
    "RequestId":"07F6177E-6DE4-408A-BB4F-0723301340F3"
}
```

Queries the details of databases on an ApsaraDB RDS instance.

#### DescribeDatabases

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDataba ses | The operation that you want to perform. Set the value to DescribeDatabases. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| DBName | String | No | testDB01 | The name of the database. |
| DBStatus | String | No | Creating | The state of the database. Valid values: Creating Running Deleting |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 50 100 Default value: 30 |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Databases | Array of Database |  | Details of the databases. |
| Database |  |  |  |
| DBName | String | testDB01 | The name of the database. |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance to which the database belongs. |

ApsaraDB for RDS

**Note**

If the request parameters are incorrectly specified, the response is null.

**Request parameters**

**Response parameters**

| Engine | String | MySQL | The database engine of the instance to which the database belongs. |
|---|---|---|---|
| DBStatus | String | Creating | The state of the database. Valid values: Creating Running Deleting |
| CharacterSetN ame | String | utf8 | The name of the character set. |
| DBDescription | String | Test database | The description of the database. |
| Accounts | Array of AccountPrivile geInfo |  | Details of the account that has specific permissions on the database. |
| AccountPrivile geInfo |  |  |  |
| Account | String | test | The name of the account. |
| AccountPrivile ge | String | DMLOnly | The permissions that the account has on the database. Valid values: ReadWrite: read and write permissions ReadOnly: read-only permissions DMLOnly: DML-only permissions DDLOnly: DDL-only permissions |
| RequestId | String | 2603CA96-B17D- 4903-BC04- 61A2C829CD94 | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDatabases &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format ApsaraDB for RDS

```xml
      <RequestId>2603CA96-B17D-4903-BC04-61A2C829CD94</RequestId>
      <Databases>
            <Database>
                  <Engine>MySQL</Engine>
                  <CharacterSetName>utf8</CharacterSetName>
                  <DBStatus>Creating</DBStatus>
                  <DBDescription></DBDescription>
                  <DBInstanceId>rdsaiiabnaiiabn</DBInstanceId>
                  <Accounts></Accounts>
                  <DBName>testdb</DBName>
            </Database>
            <Database>
                  <Engine>MySQL</Engine>
                  <CharacterSetName>gbk</CharacterSetName>
                  <DBStatus>Creating</DBStatus>
                  <DBDescription></DBDescription>
                  <DBInstanceId>rdsaiiabnaiiabn</DBInstanceId>
                  <Accounts></Accounts>
                  <DBName>testdb2</DBName>
            </Database>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBDescri ption | The operation that you want to perform. Set the value to ModifyDBDescription. |
| DBDescription | String | Yes | Test database A | The description of the database. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

ApsaraDB for RDS

```json
{
    "RequestId": "2603CA96-B17D-4903-BC04-61A2C829CD94",
    "Databases": {
        "Database": [
            {
                "Engine": "MySQL",
                "CharacterSetName": "utf8",
                "DBStatus": "Creating",
                "DBDescription": "",
                "DBInstanceId": "rdsaiiabnaiiabn",
                "Accounts": {
                    " AccountPrivilegeInfo": []
                },
                "DBName": "testdb"
            },
            {
                "Engine": "MySQL",
                "CharacterSetName": "gbk",
                "DBStatus": "Creating",
                "DBDescription": "",
                "DBInstanceId": "rdsaiiabnaiiabn",
                "Accounts": {
                    " AccountPrivilegeInfo": []
                },
                "DBName": "testdb2"
            }
```

]

```
    }
}
```

#### ModifyDBDescription

Modifies the description of a database.

**Note**

This operation is not supported for instances that run PostgreSQL or PolarDB.

**Request parameters**

| DBName | String | Yes | testDB01 | The name of the database. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 17F57FEE-EA4F- 4337-8D2E- 9C23CAA63D74 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBDescription &DBDescription=Test database A &DBInstanceId=rm-uf6wjk5xxxxxxx &DBName=testDB01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId> 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74</RequestId>
```

`JSON` format

```json
{
  "RequestId": " 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74"
}
```

#### CopyDatabaseBetweenInstances

Copies databases across ApsaraDB RDS instances. This operation can also be used to restore specific databases to an existing instance by point in time or backup set. Before you call this operation, make sure that the following requirements are met: The source and destination instances belong to the same Apsara Stack tenant account. The source and destination instances run the same version of database engine. The source and destination instances reside in the same region and use the same network type. Their zones can be different. The destination instance does not have databases whose names are the same as those of the databases that you want to copy. The available storage capacity of the destination instance is larger than the size of the databases that you want to copy from the source instance.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CopyDatabaseB etweenInstances | The operation that you want to perform. Set the value to CopyDatabaseBetweenInstances. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the source instance. |
| DbNames | String | Yes | {"test1":"test2"} | The names of the databases to be copied. Format: {"Source instance database name":"Destination instance database name"}. |
| TargetDBInstanc eId | String | Yes | rm- ut5ajk3xxxxxxx | The ID of the destination instance, which must differ from the ID of the source instance. |
| BackupId | String | No | 1065238746521 | The ID of the backup set by which you want to restore databases of the source instance. You can call the DescribeBackups operation to obtain the IDs of backup sets. Note You can specify one of BackupId and RestoreTime. |
| RestoreTime | String | No | 2011-06- 11T16:00:00Z | The point in time to which you want to restore databases of the source instance. You can select a point in time within the backup retention period. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. Note You can specify one of BackupId and RestoreTime. |

| Parameter | Type | Example | Description |
|---|---|---|---|

ApsaraDB for RDS

**Note**

This operation is applicable only to ApsaraDB RDS for SQL Server 2012 or 2016. You can restore specific databases or tables of an ApsaraDB RDS for MySQL instance to the original instance or a new instance.

**Request parameters**

**Response parameters**

| DBInstanceId | String | rm- uf6wjk5xxxxxxxxxx | The ID of the destination instance. |
|---|---|---|---|
| RequestId | String | 803D11AF-C370- 465B-AB46- CB3A642DC303 | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=CopyDatabaseBetweenInstances &DBInstanceId=rm-uf6wjk5xxxxxxx &TargetDBInstanceId=rm-ut5ajk3xxxxxxx &DbNames={"test1":"test2"} &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>803D11AF-C370-465B-AB46-CB3A642DC303</RequestId>
```

`JSON` format

```json
{
    "RequestId": "803D11AF-C370-465B-AB46-CB3A642DC303"
}
```

### Account management

#### CreateAccount

Creates an account that is used to manage databases on an ApsaraDB RDS instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. The number of accounts that are created on the instance does not exceed the maximum number of accounts that are allowed for each instance.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateAccount | The operation that you want to perform. Set the value to CreateAccount. |
|  |  |  |  | The name of the account. |

ApsaraDB for RDS

**Note**

This operation is supported only for instances that run MySQL, PostgreSQL, or SQL Server. This operation is not supported for instances that run SQL Server 2017 EE or SQL Server 2019 EE. You can create multiple privileged accounts and multiple standard accounts for each ApsaraDB RDS instance that runs PostgreSQL with standard SSDs. You can create only a single privileged account for each ApsaraDB RDS instance that runs PostgreSQL 9.4 or PostgreSQL 10.0 with local SSDs.

**Request parameters**

| AccountName | String | Yes | test1 | Note The name must be unique. The name must start with a letter and end with a letter or a digit. The name can contain lowercase letters, digits, and underscores ( ). _ The length of the name must meet the following requirements: If the instance runs MySQL 5.6, the name must be 2 to 16 characters in length. If the instance runs MySQL 5.7 or MySQL 8.0, the name must be 2 to 32 characters in length. |
|---|---|---|---|---|
|  |  |  |  | If the instance runs SQL Server, the name must be 2 to 64 characters in length. If the instance runs PostgreSQL with standard SSDs, the name must be 2 to 63 characters in length. If the instance runs PostgreSQL with local SSDs, the name must be 2 to 16 characters in length. For information about invalid characters, see Forbidden keywords. |

ApsaraDB for RDS

| AccountPasswor d | String | Yes | Test123456 | The password of the account. Note The password must be 8 to 32 characters in length. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password can contain the following special characters: ! @ # $ % ^ & * ( ) + - = _ |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| AccountDescripti on | String | No | Test account A | The description of the account. The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and _ hyphens (-). The description must start with a letter. Note The description cannot start with http:// or https://. |
| AccountType | String | No | Normal | The type of the account. Valid values: Normal: standard account Super: privileged account Default value: Normal. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D4D4BE8A-DD46- 440A-BFCD- EE31DA81C9DD | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAccount | The operation that you want to perform. Set the value to DeleteAccount. |
| AccountName | String | Yes | test1 | The name of the account. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

ApsaraDB for RDS

```
&DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1 &AccountPassword=Test123456 &<Common request parameters>
```

Sample success responses `XML` format

```xml
         <RequestId>D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD</RequestId>
```

`JSON` format

```json
{
    "RequestId":"D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD"
}
```

#### DeleteAccount

Deletes an account from an ApsaraDB for RDS instance. Before you call this operation, make sure that the instance is in the running state.

**Note**

This operation is not supported for instances that run SQL Server 2017 EE or PostgreSQL with local SSDs. If the instance runs PostgreSQL with standard SSDs and the account to be deleted has permissions on databases, tables, or other objects, this operation only locks the account. To delete the account, you must revoke the permissions.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 91E855E5-7E80- 4955-929B- C74EE1D38C66 | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CheckAccountN ameAvailable | The operation that you want to perform. Set the value to CheckAccountNameAvailable. |
| AccountName | String | Yes | DatabaseTest | The name of the account that you want to create. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxx | The ID of the instance. |

ApsaraDB for RDS

**Examples**

Sample requests

```
&DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestID>91E855E5-7E80-4955-929B-C74EE1D38C66</RequestID>
```

`JSON` format

```json
{
    "RequestID":"91E855E5-7E80-4955-929B-C74EE1D38C66"
}
```

#### CheckAccountNameAvailable

Queries whether the name of the account that you want to create on an ApsaraDB RDS instance is available.

**Request parameters**

| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5E4AA101-1EE5- 41C0-AE6D- 0F066331AC1C | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=CheckAccountNameAvailable &AccountName=DatabaseTest &DBInstanceId=rm-uf6wjk5xxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>5E4AA101-1EE5-41C0-AE6D-0F066331AC1C</RequestId>
```

`JSON` format

```json
{
    "RequestId":"5E4AA101-1EE5-41C0-AE6D-0F066331AC1C"
}
```

#### CheckDBNameAvailable

Checks whether a database name is unique and conforms to the naming conventions on an ApsaraDB RDS instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CheckDBNameA vailable | The operation that you want to perform. Set the value to CheckDBNameAvailable. |
| DBInstanceId | String | Yes | rm-t4n3axxxxx | The ID of the instance. |
| DBName | String | Yes | test1 | The database name to check. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6EF82B07-28D2- 48D1-B5D6- 7E78FED277C7 | The ID of the request. Note If this operation returns only the ID of the request, the database name can be used. Otherwise, an error message is returned to indicate that the database name is duplicate or does not conform to the naming conventions. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=CheckDBNameAvailable &DBInstanceId=rm-t4n3axxxxx &DBName=test1 &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccount s | The operation that you want to perform. Set the value to DescribeAccounts. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| AccountName | String | No | test1 | The name of the account. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Accounts | Array of DBInstanceAcc ount |  | Details of the accounts. |
| DBInstanceAcc ount |  |  |  |

ApsaraDB for RDS

```xml
  <RequestId>6EF82B07-28D2-48D1-B5D6-7E78FED277C7</RequestId>
```

`JSON` format

```json
{"RequestId":"6EF82B07-28D2-48D1-B5D6-7E78FED277C7"}
```

#### DescribeAccounts

Queries information of the accounts that are created on an ApsaraDB RDS instance.

**Note**

This operation is not supported for instances that run SQL Server 2017 EE or PostgreSQL.

**Request parameters**

**Response parameters**

| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance to which the account belongs. |
|---|---|---|---|
| AccountName | String | test1 | The name of the account. |
| AccountStatus | String | Available | The status of the account. Valid values: Unavailable Available |
| AccountDescri ption | String | Test account | The description of the account. |
| DatabasePrivil eges | Array of DatabasePrivil ege |  | Details of the permissions that are granted to the account. |
| DatabasePrivil ege |  |  |  |
| DBName | String | test1 | The name of the database. |
| AccountPrivile ge | String | ReadWrite | The type of permissions that are granted to the account. Valid values: ReadWrite: read and write permissions ReadOnly: read-only permissions DDLOnly: DDL-only permissions DMLOnly: DML-only permissions Custom: custom permissions (which can be modified by using SQL commands) |
| AccountPrivile geDetail | String | SELECT,INSERT | The permissions that are granted to the account. For more information, see Create an account in ApsaraDB RDS for MySQL User Guide. |
| AccountType | String | Normal | The type of the account. Valid values: Normal: standard account Super: privileged account Sysadmin: superuser account that has the system administrator permissions |
| PrivExceeded | String | 0 | Indicates whether the number of databases that are managed by the account exceeds the specified limit. Valid values: 1: yes 0: no |

ApsaraDB for RDS

| RequestId | String | A2E94301-D07F- 4457-9B49- 6AA2BB388C85 | The ID of the request. |
|---|---|---|---|
| SystemAdmin AccountFirstAc tivationTime | String | 2020-02- 06T11:00:00Z | The first time when superuser accounts were enabled. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| SystemAdmin AccountStatus | String | True | Indicates whether superuser accounts are enabled. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeAccounts &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <Accounts>
            <DBInstanceAccount>
                  <DatabasePrivileges>
                        <DatabasePrivilege>
                              <AccountPrivilege>ReadWrite</AccountPrivilege>
<AccountPrivilegeDetail>SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,REFERENCES,INDEX,ALTER,CR TE TEMPORARY TABLES,LOCK TABLES,CREATE VIEW,SHOW VIEW,CREATE ROUTINE,ALTER ROUTINE,EXECUTE,EVENT,TRIGGER</AccountPrivilegeDetail>
                              <DBName>testdb</DBName>
                        </DatabasePrivilege>
                  </DatabasePrivileges>
                  <AccountStatus>Available</AccountStatus>
                  <AccountDescription></AccountDescription>
                  <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
                  <AccountName>testacc02</AccountName>
                  <PrivExceeded>0</PrivExceeded>
                  <AccountType>Normal</AccountType>
            </DBInstanceAccount>
      </Accounts>
      <RequestId>A2E94301-D07F-4457-9B49-6AA2BB388C85</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GrantAccountPri vilege | The operation that you want to perform. Set the value to GrantAccountPrivilege. |
| AccountName | String | Yes | test1 | The name of the account. |

ApsaraDB for RDS

```json
{
    "Accounts": {
        "DBInstanceAccount": [
            {
                "DatabasePrivileges": {
                    "DatabasePrivilege": [
                        {
                            "AccountPrivilege": "ReadWrite",
                            "AccountPrivilegeDetail":
"SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,REFERENCES,INDEX,ALTER,CREATE TEMPORARY TABLES ,LOCK TABLES,CREATE VIEW,SHOW VIEW,CREATE ROUTINE,ALTER ROUTINE,EXECUTE,EVENT,TRIGGER",
                            "DBName": "testdb"
                        }
```

]

```json
                },
                "AccountStatus": "Available",
                "AccountDescription": "",
                "DBInstanceId": "rm-uf6wjk5xxxxxxx",
                "AccountName": "testacc02",
                "PrivExceeded": "0",
                "AccountType": "Normal"
            }
```

]

```json
    },
    "RequestId": "A2E94301-D07F-4457-9B49-6AA2BB388C85"
}
```

#### GrantAccountPrivilege

Grants an account the permissions on a database of an ApsaraDB for RDS instance. Each account can be granted permissions on one or more databases. Before you call this operation, make sure that the instance is in the running state.

**Note**

This operation is not supported for instances that run PostgreSQL with local SSDs, SQL Server 2017 EE, or PolarDB.

**Request parameters**

| AccountPrivilege | String | Yes | ReadWrite | The permissions of the account. Default value: ReadWrite: read and write permissions ReadOnly: read-only permissions DDLOnly: DDL-only permissions DMLOnly: DML-only permissions DBOwner: database owner permissions Note If the instance runs MySQL, you can set this parameter to ReadWrite, ReadOnly, DDLOnly, or DMLOnly. If the instance runs SQL Server, you can set this parameter to ReadWrite, ReadOnly, or DBOwner. If the instance runs PostgreSQL with standard SSDs, you can set this parameter to DBOwner. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx xxx | The ID of the instance. |
| DBName | String | Yes | testDB | The name of the database on which you want to grant permissions. |
| KillConnection | String | No | None | An invalid parameter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 81BC9559-7B22- 4B7F-B705- 5F56DEECDEA7 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RevokeAccountP rivilege | The operation that you want to perform. Set the value to RevokeAccountPrivilege. |
| AccountName | String | Yes | test1 | The name of the account. |

ApsaraDB for RDS

```
http(s)://rds.example.com/?Action=GrantAccountPrivilege &DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1 &DBName=test &AccountPrivilege=ReadWrite &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>81BC9559-7B22-4B7F-B705-5F56DEECDEA7</RequestId>
```

`JSON` format

```json
{
       "RequestId":"81BC9559-7B22-4B7F-B705-5F56DEECDEA7"
}
```

#### RevokeAccountPrivilege

Revokes database access permissions of an account. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state.

**Note**

The permissions that can be revoked include SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, and TRIGGER. This operation is not supported for instances that run PostgreSQL, SQL Server 2017 EE, or PolarDB.

**Request parameters**

| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
|---|---|---|---|---|
| DBName | String | Yes | testDB | The name of the database. You can revoke all permissions of the account on this database. Separate multiple databases with commas (,). |
| KillConnection | String | No | None | An invalid parameter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E22099CA-A61E- 4992-A0B7- CE82DC175626 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=RevokeAccountPrivilege &DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1 &DBName=testDB &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>E22099CA-A61E-4992-A0B7-CE82DC175626</RequestId>
```

`JSON` format

```json
{
       "RequestId":"E22099CA-A61E-4992-A0B7-CE82DC175626"
}
```

#### ModifyAccountDescription

Modifies the description of a database account.

**Note**

This operation is not supported for instances that run PostgreSQL, SQL Server 2017 EE, or PolarDB.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAccountD escription | The operation that you want to perform. Set the value to ModifyAccountDescription. |
| AccountDescripti on | String | Yes | Test account A | The description of the account. The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and _ hyphens (-). The description must start with a letter. Note The description cannot start with http:// or https://. |
| AccountName | String | Yes | test1 | The name of the account. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 17F57FEE-EA4F- 4337-8D2E- 9C23CAA63D74 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyAccountDescription &AccountDescription=Test account A &AccountName=test1 &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId> 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetAccountPa ssword | The operation that you want to perform. Set the value to ResetAccountPassword. |
| AccountName | String | Yes | test1 | The name of the account. |
| AccountPasswor d | String | Yes | Test123456 | The new password for the account. Note The password must be 8 to 32 characters in length. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password can contain the following special characters: ! @ # $ & % ^ * ( ) + - = _ |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

ApsaraDB for RDS

```json
{
  "RequestId": " 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74"
}
```

#### ResetAccountPassword

Resets the password of an account on an ApsaraDB RDS instance. Before you call this operation, make sure that the instance is in the running state.

**Note**

This operation is not supported for accounts that are created by using SQL statements on instances that run PostgreSQL, SQL Server 2017 EE, or PolarDB.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D4D4BE8A-DD46- 440A-BFCD- EE31DA81C9DD | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetAccount | The operation that you want to perform. Set the value to ResetAccount. |
| AccountName | String | Yes | test1 | The name of the privileged account. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ResetAccountPassword &DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1 &AccountPassword=Test123456 &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD</RequestId>
```

`JSON` format

```json
{
       "RequestId":"D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD"
}
```

#### ResetAccount

Resets permissions of the privileged account.

**Note**

This operation is not supported for instances that run SQL Server 2008 R2 because they do not have privileged accounts.

**Request parameters**

| AccountPasswor d | String | Yes | Test123456 | The new password of the privileged account. Note The password must be 8 to 32 characters in length. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password can contain the following special characters: ! @ # $ & % ^ * ( ) + - = _ |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 81BC9559-7B22- 4B7F-B705- 5F56DEECDEA7 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
&AccountName=test1 &AccountPassword=Test123456 &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>81BC9559-7B22-4B7F-B705-5F56DEECDEA7</RequestId>
```

`JSON` format

```json
{
       "RequestId":"81BC9559-7B22-4B7F-B705-5F56DEECDEA7"
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GrantOperatorP ermission | The operation that you want to perform. Set the value to GrantOperatorPermission. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| ExpiredTime | String | Yes | 2019-03- 27T16:00:00Z | The expiration time of the permissions. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| Privileges | String | Yes | Control | The permissions that you want to grant to the service account. Valid values: Control: the configuration permissions, which allow you to view and modify configurations of the instance. Data: the data permissions, which allow you to view schemas, indexes, and SQL statements of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 842B73C8-5776- 4BD9-9872- 69C8C46DD7D3 | The ID of the request. |

ApsaraDB for RDS

#### GrantOperatorPermission

Grants permissions to the service account of an ApsaraDB RDS instance. When you seek help from Alibaba Cloud technical support to troubleshoot instance exceptions, you must grant permissions to the service account of your instance. The service account is used by Alibaba Cloud technical support to perform operations on the databases of your instance. This operation is available only when your instance runs one of the following database engines: MySQL PostgreSQL

**Request parameters**

**Response parameters**

**Examples**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | LockAccount | The operation that you want to perform. Set the value to LockAccount. |
| AccountName | String | Yes | testaccount | The account that you want to lock. You can lock only a single account at a time. |
| DBInstanceId | String | Yes | pgm-bpxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1B291C4B-DDCD- 4D0A-8F6D- 7F3241DE9228 | The ID of the request. |

ApsaraDB for RDS Sample requests

```
http(s)://rds.example.com/?Action=GrantOperatorPermission &DBInstanceId=rm-uf6wjk5xxxxxxx &ExpiredTime=2019-03-27T16:00:00Z &Privileges=Control &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>842B73C8-5776-4BD9-9872-69C8C46DD7D3</RequestId>
```

`JSON` format

```json
{
    "RequestId":"842B73C8-5776-4BD9-9872-69C8C46DD7D3"
}
```

#### LockAccount

Locks an account of an ApsaraDB RDS for PostgreSQL instance. ApsaraDB RDS for PostgreSQL instances that use standard SSDs allow you to lock accounts. Locked accounts cannot be used to log on to an instance.

**Request parameters**

**Response parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RevokeOperator Permission | The operation that you want to perform. Set the value to RevokeOperatorPermission. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

| Parameter | Type | Example | Description |
|---|---|---|---|

ApsaraDB for RDS

**Examples**

Sample requests

```
&AccountName=testaccount &DBInstanceId=pgm-bpxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
    <RequestId>1B291C4B-DDCD-4D0A-8F6D-7F3241DE9228</RequestId>
```

`JSON` format

```json
{
    "RequestId": "1B291C4B-DDCD-4D0A-8F6D-7F3241DE9228"
}
```

#### RevokeOperatorPermission

Revokes permissions from the service account of an ApsaraDB RDS instance. After Alibaba Cloud technical support resolves the issues on your instance, you can revoke permissions from the service account of your instance. This operation is available only when your instance runs one of the following database engines: MySQL PostgreSQL

**Request parameters**

**Response parameters**

| RequestId | String | 842B73C8-5776- 4BD9-9872- 69C8C46DD7D3 | The ID of the request. |
|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnlockAccount | The operation that you want to perform. Set the value to UnlockAccount. |
| AccountName | String | Yes | testaccount | The account that you want to unlock. You can unlock only a single account at a time. |
| DBInstanceId | String | Yes | pgm-bpxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=RevokeOperatorPermission &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>842B73C8-5776-4BD9-9872-69C8C46DD7D3</RequestId>
```

`JSON` format

```json
{
    "RequestId":"842B73C8-5776-4BD9-9872-69C8C46DD7D3"
}
```

#### UnlockAccount

Unlocks an account of an ApsaraDB RDS for PostgreSQL instance. You cannot use a locked account to log on to the corresponding ApsaraDB RDS for PostgreSQL instance that uses standard SSDs. You must first unlock the account.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | AA65190D-852A- 4C9B-88DA- E92698CAA350 | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBackup | The operation that you want to perform. Set the value to CreateBackup. |

ApsaraDB for RDS

**Examples**

Sample requests

```
&AccountName=testaccount &DBInstanceId=pgm-bpxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
  <RequestId>AA65190D-852A-4C9B-88DA-E92698CAA350</RequestId>
```

`JSON` format

```json
{
    "RequestId": "AA65190D-852A-4C9B-88DA-E92698CAA350"
}
```

### Backup and restoration

#### CreateBackup

Creates a backup set for an ApsaraDB RDS instance. This operation uses the backup feature of ApsaraDB RDS to create a backup set. You can also use an operation of Database Backup (DBS) to create a backup schedule. For more information, see **List of operations by function** in **Database Backup****Developer Guide**. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance does not have ongoing backup tasks. The number of backup sets that are created per day for an instance cannot exceed 20.

**Request parameters**

| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
|---|---|---|---|---|
| DBName | String | No | rds mysql _ | The name of the database whose data you want to back up. Separate multiple database names with commas (,). Note You can specify this parameter when you perform a logical backup on individual databases of an ApsaraDB RDS for MySQL instance. You can also specify this parameter when you perform a full physical backup on individual databases of an ApsaraDB RDS for SQL Server instance. |
| BackupStrategy | String | No | db | The backup policy of the instance. Valid values: db: database backup instance: instance backup Note You can specify this parameter when you perform a logical backup on an ApsaraDB RDS for MySQL instance. You can also specify this parameter when you perform a full physical backup on an ApsaraDB RDS for SQL Server instance. |

ApsaraDB for RDS

| BackupMethod | String | No | Physical | The backup type of the instance. Valid values: Logical: logical backup Physical: physical backup Snapshot: snapshot backup Default value: Physical. Note You can perform a logical backup only when databases are created on the instance. For more information about backup types supported by instances that run different database engines, see User Guide of the corresponding database engines. When you perform a snapshot backup on an ApsaraDB RDS for SQL Server instance that uses standard SSDs, you must set this parameter to Snapshot. |
|---|---|---|---|---|
| BackupType | String | No | Auto | The backup method of the instance. Valid values: Auto: full or incremental backup that is automatically selected FullBackup: full backup Default value: Auto. Note You must set this parameter only when the instance runs the SQL Server database engine. This parameter is valid only when the BackupMethod parameter is set to Physical. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupJobId | String | 5073731 | The ID of the backup task. |

ApsaraDB for RDS

**Response parameters**

| RequestId | String | 2C125605-266F- 41CA-8AC5- 3A643D4F42C5 | The ID of the request. |
|---|---|---|---|

ApsaraDB for RDS

**Examples**

Sample requests

```
&DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>2C125605-266F-41CA-8AC5-3A643D4F42C5</RequestId>
      <BackupJobId>5073731</BackupJobId>
```

`JSON` format

```json
{
    "RequestId": "2C125605-266F-41CA-8AC5-3A643D4F42C5",
    "BackupJobId": "5073731"
}
```

#### CloneDBInstance

Restores the data of an ApsaraDB RDS instance to a new instance. The new instance is also called a cloned instance. Before you call this operation, make sure that the following requirements are met: The original instance is in the running state. The original instance does not have ongoing migration tasks. The log backup feature is enabled for the original instance to support point-in-time restoration. The primary instance has at least one completed backup set before you clone the instance by backup set.

**Note**

RAM users can be used to create cloned instances. Make sure that your RAM users have been granted permissions to clone instances. Take note of the following information: The new instance has the same IP address whitelist, SQL Explorer (SQL Audit), alert threshold, backup, and parameter settings as the original instance. The data and account information of the new instance is the same as that indicated by the backup set or point in time used for restoration of the original instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CloneDBInstanc e | The operation that you want to perform. Set the value to CloneDBInstance. |
| PayType | String | Yes | Postpaid | The billing method of the new instance. Set the value to Postpaid. |
| DBInstanceClass | String | No | mysql.n1.micro. 1 | The instance type of the new instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. Note The default value is the instance type of the original instance. |
| DBInstanceStora ge | Integer | No | 1000 | The storage capacity of the new instance. Unit: GB. The storage capacity must be in 5 GB increments. For more information, see Instance types in ApsaraDB RDS Product Introduction. Note The default value is the storage capacity of the original instance. |
| InstanceNetwork Type | String | No | VPC | The network type of the new instance. Valid values: VPC Classic Note The default value is the network type of the original instance. |
| DBInstanceId | String | No | rm- uf6wjk5xxxxxxx xxx | The ID of the original instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

ApsaraDB for RDS

| BackupId | String | No | 9026262 | The ID of the backup set by which you want to restore the original instance. You can call the DescribeBackups operation to query the backup set list. Note You must specify at least one of BackupId and RestoreTime. |
|---|---|---|---|---|
| RestoreTime | String | No | 2011-06- 11T16:00:00Z | The point in time to which you want to restore the original instance. You can select a point in time within the backup retention period. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Note You must specify at least one of BackupId and RestoreTime. |
| VPCId | String | No | vpc- uf6f7l4fg90xxxx xxxxxx | The ID of the virtual private cloud (VPC). Note The VPC must belong to the specified region. |
| VSwitchId | String | No | vsw- uf6adz52c2pxxx xxxxxxx | The ID of the vSwitch. Note The vSwitch must belong to the specified VPC and region. |
| PrivateIpAddress | String | No | 172.16.201.69 | The internal IP address of the new instance, which must be within the CIDR block supported by the specified vSwitch. The system automatically assigns an internal IP address to the instance based on the VPCId and VSwitchId values. |
| UsedTime | String | No | None | An invalid parameter. |
| Period | String | No | None | An invalid parameter. |

ApsaraDB for RDS

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the new instance. |
| OrderId | String | 100789370xxxxx | The ID of the order. |
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=CloneDBInstance &PayType=Postpaid &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &DBInstanceStorageType=cloud_essd &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <OrderId>100789370xxxxx</OrderId>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId>
```

`JSON` format

```json
{
    "OrderId": "100789370xxxxx",
    "DBInstanceId": "rm-uf6wjk5xxxxxxx",
    "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC"
}
```

#### DescribeBackups

Queries the backup sets of an ApsaraDB RDS instance.

**Note**

A backup set can be used to restore data only when its **BackupStatus** value is **Success**.

**Request parameters**

| Action | String | Yes | DescribeBackup s | The operation that you want to perform. Set the value to DescribeBackups. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| BackupId | String | No | 327329803 | The ID of the backup set. |
| BackupStatus | String | No | Success | The status of the backup set. Valid values: Success Failed |
| BackupMode | String | No | Automated | The backup mode. Valid values: Automated Manual |
| StartTime | String | No | 2011-06- 01T16:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | No | 2011-06- 15T16:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 50 100 Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|

ApsaraDB for RDS

**Response parameters**

| TotalRecordCo unt | String | 100 | The total number of entries returned. |
|---|---|---|---|
| PageNumber | String | 1 | The page number of the returned page. |
| PageRecordCo unt | String | 30 | The number of backup sets on the page. |
| Items | Array of Backup |  | Details of the backup sets. |
| Backup |  |  |  |
| BackupId | String | 321020562 | The ID of the backup set. |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| HostInstanceI D | String | 5882781 | The No. of the instance that generates the backup set. This parameter is used to indicate whether the instance that generates the backup set is a primary instance or a secondary instance. |
| BackupStatus | String | Success | The status of the backup set. |
| BackupStartTi me | String | 2019-02- 03T12:20:00Z | The start time of the backup. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mmZ format. The time is displayed in UTC. |
| BackupEndTim e | String | 2019-02- 13T12:20:00Z | The end time of the backup. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mmZ format. The time is displayed in UTC. |
| BackupType | String | FullBackup | The backup type. Valid values: FullBackup IncrementalBackup |
| BackupMode | String | Automated | The backup mode. Valid values: Automated Manual |
| BackupMethod | String | Physical | The backup method. Valid values: Logical Physical Snapshot |

ApsaraDB for RDS

| BackupDownlo adURL | String | http://rdsbak-hz- v3.oss-cn- hangzhou.aliyuncs. com/xxxxx | The URL that is used to download the backup file over the Internet. If the backup file cannot be downloaded over the Internet, null is returned. Note For example, if the instance runs SQL Server and the BackupMethod parameter is set to Snapshot, null is returned. |
|---|---|---|---|
| BackupIntrane tDownloadURL | String | http://rdsbak-hz- v3.oss-cn- hangzhou- internal.aliyuncs.co m/xxxxx | The URL that is used to download the backup file over an internal network. If the backup file cannot be downloaded over the Internet, null is returned. Note For example, if the instance runs SQL Server and the BackupMethod parameter is set to Snapshot, null is returned. |
| BackupSize | Long | 2167808 | The size of the backup set. Unit: byte. |
| StoreStatus | String | Disabled | Indicates whether the backup set can be deleted. Valid values: Enabled: The backup set can be deleted. Disabled: The backup set cannot be deleted. |
| MetaStatus | String | OK | The status of the backup set that is used to restore individual databases or tables. Valid values: OK: The backup set is normal. LARGE: The backup set contains an abnormally large number of tables. It cannot be used to restore individual databases or tables. EMPTY: The backup set is generated from a failed backup task. Note If an empty string is returned, the backup set cannot be used to restore individual databases or tables. |
| SlaveStatus | String | None | An invalid parameter. |
| RequestId | String | 1A6D328C-84B8- 40DC-BF49- 6C73984D7494 | The ID of the request. |

ApsaraDB for RDS

**Examples**

ApsaraDB for RDS Sample requests

```
http(s)://rds.example.com/?Action=DescribeBackups &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <TotalRecordCount>100</TotalRecordCount>
      <TotalEcsSnapshotSize>0</TotalEcsSnapshotSize>
      <PageRecordCount>30</PageRecordCount>
      <RequestId>1A6D328C-84B8-40DC-BF49-6C73984D7494</RequestId>
      <PageNumber>1</PageNumber>
      <Items>
            <Backup>
                  <BackupMethod>Physical</BackupMethod>
                  <BackupInitiator>System</BackupInitiator>
                  <StorageClass>0</StorageClass>
                  <BackupIntranetDownloadURL>http://rdsbak-hz-v3.oss-cn-hangzhou-interna
l.aliyuncs.com/xxxxx</BackupIntranetDownloadURL>
                  <BackupSize>2167808</BackupSize>
                  <BackupMode>Automated</BackupMode>
                  <BackupId>321020562</BackupId>
                  <IsAvail>1</IsAvail>
                  <Encryption>{}</Encryption>
                  <HostInstanceID>5882781</HostInstanceID>
                  <StoreStatus>Disabled</StoreStatus>
                  <BackupDownloadURL>http://rdsbak-hz-v3.oss-cn-
hangzhou.aliyuncs.com/xxxxx</BackupDownloadURL>
                  <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
                  <CopyOnlyBackup>0</CopyOnlyBackup>
                  <BackupEndTime>2019-02-13T12:20:00Z</BackupEndTime>
                  <ConsistentTime>1576506856</ConsistentTime>
                  <BackupStartTime>2019-02-03T12:20:00Z</BackupStartTime>
                  <MetaStatus>OK</MetaStatus>
                  <BackupType>FullBackup</BackupType>
                  <BackupStatus>Success</BackupStatus>
                  <BackupDownloadLinkByDB>
                        <BackupDownloadLinkByDB>
                              <DownloadLink>https://cn-
hangzhou.bak.rds.aliyuncs.com/custins53664665/hins18676859_2021072909473127987849.zip?E xpires=*****&amp;dbList=tb1</DownloadLink>
                              <IntranetDownloadLink>https://cn-hangzhou-
internal.bak.rds.aliyuncs.com/custins53664665/hins18676859_2021072909473127987849.zip?E xpires=*****&amp;dbList=tb1</IntranetDownloadLink>
                              <DataBase>dbs</DataBase>
                        </BackupDownloadLinkByDB>
                  </BackupDownloadLinkByDB>
            </Backup>
      </Items>
```

ApsaraDB for RDS `JSON` format

```json
{
        "TotalRecordCount": 100,
        "TotalEcsSnapshotSize": 0,
        "PageRecordCount": 30,
        "RequestId": "1A6D328C-84B8-40DC-BF49-6C73984D7494",
        "PageNumber": 1,
        "Items": {
            "Backup": {
                "BackupMethod": "Physical",
                "BackupInitiator": "System",
                "StorageClass": 0,
                "BackupIntranetDownloadURL": "http://rdsbak-hz-v3.oss-cn-hangzhou-intern
al.aliyuncs.com/xxxxx",
                "BackupSize": 2167808,
                "BackupMode": "Automated",
                "BackupId": 321020562,
                "IsAvail": 1,
                "Encryption": "{}",
                "HostInstanceID": 5882781,
                "StoreStatus": "Disabled",
                "BackupDownloadURL": "http://rdsbak-hz-v3.oss-cn-
hangzhou.aliyuncs.com/xxxxx",
                "DBInstanceId": "rm-uf6wjk5xxxxxxx",
                "CopyOnlyBackup": 0,
                "BackupEndTime": "2019-02-13T12:20:00Z",
                "ConsistentTime": 1576506856,
                "BackupStartTime": "2019-02-03T12:20:00Z",
                "MetaStatus": "OK",
                "BackupType": "FullBackup",
                "BackupStatus": "Success",
                "BackupDownloadLinkByDB": {
                    "BackupDownloadLinkByDB": {
                        "DownloadLink": "https://cn-
hangzhou.bak.rds.aliyuncs.com/custins53664665/hins18676859_2021072909473127987849.zip?E xpires=*****&amp;dbList=tb1",
                        "IntranetDownloadLink": "https://cn-hangzhou-
internal.bak.rds.aliyuncs.com/custins53664665/hins18676859_2021072909473127987849.zip?E xpires=*****&amp;dbList=tb1",
                        "DataBase": "dbs"
                    }
                }
            }
        }
    }
}
```

Queries the backup settings of an ApsaraDB RDS instance.

#### DescribeBackupPolicy

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackup Policy | The operation that you want to perform. Set the value to DescribeBackupPolicy. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| BackupPolicyMo de | String | No | DataBackupPolic y | The backup type. Valid values: DataBackupPolicy: data backup LogBackupPolicy: log backup |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupRetenti onPeriod | Integer | 7 | The number of days for which data backup files are retained. |
| PreferredBack upTime | String | 15:00Z-16:00Z | The time when a data backup is performed. The time follows the ISO 8601 standard in the HH:mmZ-HH:mmZ format. The time is displayed in UTC. |
| PreferredBack upPeriod | String | Monday,Wednesda y,Friday,Sunday | The cycle based on which data backups are performed. If more than one day of the week is specified, the days of the week are separated by commas (,). Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |
| BackupLog | String | Enable | Indicates whether the log backup feature is enabled. Value values: Enable and Disabled. |
| LogBackupRet entionPeriod | Integer | 7 | The number of days for which log backup files are retained. |

ApsaraDB for RDS

**Request parameters**

**Response parameters**

| EnableBackup Log | String | 1 | Indicates whether the log backup feature can be enabled. Valid values: 1: enables the feature. 0: disables the feature. |
|---|---|---|---|
| HighSpaceUsa geProtection | String | Enable | Indicates whether the log backup deletion feature is enabled. If the disk usage exceeds 80% or the remaining disk space is less than 5 GB on the instance, this feature deletes log backup files. Valid values: Disable Enable |
| LocalLogReten tionHours | Integer | 0 | The number of hours for which log backup files are retained on the instance. |
| LocalLogReten tionSpace | String | 30 | The maximum disk usage that is allowed for log backup files on the instance. |
| LogBackupFre quency | String | LogInterval | The frequency at which log backups are performed. Valid values: LogInterval: Log backups are performed every 30 minutes. Default value: same as the value of the PreferredBackupPeriod parameter. Note The LogBackupFrequency parameter is supported only when the instance runs SQL Server. |
| PreferredNext BackupTime | String | 2018-01- 19T15:15Z | The time when the next backup is performed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| RequestId | String | B87E2AB3-B7C9- 4394-9160- 7F639F732031 | The ID of the request. |
| ArchiveBackup KeepCount | String | 1 | The number of archived backup files that are retained. |
| ArchiveBackup KeepPolicy | String | ByMonth | The cycle based on which archived backup files are retained. |
| ArchiveBackup RetentionPerio d | String | 365 | The number of days for which archived backup files are retained. |

ApsaraDB for RDS

| CompressType | Integer | 1 | The format that is used to compress backup data. Valid values: 0: Backup data is not compressed. 1: Backup data is compressed by using zlib. 2: Backup data is compressed by using zlib that invokes more than one thread in parallel for each backup. 4: Backup data is compressed by using QuickLZ and can be used to restore individual databases or tables. 8: Backup data is compressed by using QuickLZ but cannot be used to restore individual databases or tables. This value is available only when the instance runs MySQL 8.0. |
|---|---|---|---|
| Duplication | String | None | An invalid parameter. |
| DuplicationCo ntent | String | None | An invalid parameter. |
| DuplicationLoc ation | Struct |  | An invalid parameter. |
| Location | Struct |  | An invalid parameter. |
| Bucket | String | None | An invalid parameter. |
| Endpoint | String | None | An invalid parameter. |
| Sotrage | String | None | An invalid parameter. |
| LogBackupLoc alRetentionNu mber | Integer | 60 | The number of log backup files that are retained on the instance. |
| ReleasedKeep Policy | String | None | The policy that is used to retain archived backup files if the instance is released. Valid values: None: No archived backup files are retained. Lastest: Only the last archived backup file is retained. All: All archived backup files are retained. |

ApsaraDB for RDS

**Examples**

Sample requests ApsaraDB for RDS

```
http(s)://rds.example.com/?Action=DescribeBackupPolicy &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
  <Category>Standard</Category>
  <ArchiveBackupRetentionPeriod>0</ArchiveBackupRetentionPeriod>
  <RequestId>292884FE-D689-47A2-9829-C05E63366201</RequestId>
  <Duplication></Duplication>
  <ReleasedKeepPolicy>None</ReleasedKeepPolicy>
  <ArchiveBackupKeepPolicy>ByMonth</ArchiveBackupKeepPolicy>
  <PreferredBackupTime>00:00Z-01:00Z</PreferredBackupTime>
  <LocalLogRetentionHours>18</LocalLogRetentionHours>
  <PreferredNextBackupTime>2021-01-07T00:40Z</PreferredNextBackupTime>
  <DuplicationLocation>
        <Sotrage>OSS</Sotrage>
        <Location>
              <Endpoint></Endpoint>
              <Bucket></Bucket>
        </Location>
  </DuplicationLocation>
  <HighSpaceUsageProtection>Enable</HighSpaceUsageProtection>
  <CompressType>1</CompressType>
  <LogBackupFrequency>LogInterval</LogBackupFrequency>
  <PreferredBackupPeriod>Tuesday,Thursday,Saturday</PreferredBackupPeriod>
  <ArchiveBackupKeepCount>1</ArchiveBackupKeepCount>
  <LogBackupRetentionPeriod>7</LogBackupRetentionPeriod>
  <LogBackupLocalRetentionNumber>60</LogBackupLocalRetentionNumber>
  <BackupLog>Enable</BackupLog>
  <EnableBackupLog>1</EnableBackupLog>
  <SupportReleasedKeep>0</SupportReleasedKeep>
  <SupportVolumeShadowCopy>1</SupportVolumeShadowCopy>
  <LocalLogRetentionSpace>30</LocalLogRetentionSpace>
  <BackupRetentionPeriod>10</BackupRetentionPeriod>
  <DuplicationContent></DuplicationContent>
  <BackupInterval>30</BackupInterval>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBackupPo licy | The operation that you want to perform. Set the value to ModifyBackupPolicy. |

ApsaraDB for RDS

```json
{
    "Category": "Standard",
    "ArchiveBackupRetentionPeriod": 0,
    "RequestId": "292884FE-D689-47A2-9829-C05E63366201",
    "Duplication": "",
    "ReleasedKeepPolicy": "None",
    "ArchiveBackupKeepPolicy": "ByMonth",
    "PreferredBackupTime": "00:00Z-01:00Z",
    "LocalLogRetentionHours": "18",
    "PreferredNextBackupTime": "2021-01-07T00:40Z",
    "DuplicationLocation": {
        "Sotrage": "OSS",
        "Location": {
            "Endpoint": "",
            "Bucket": ""
        }
    },
    "HighSpaceUsageProtection": "Enable",
    "CompressType": "1",
    "LogBackupFrequency": "LogInterval",
    "PreferredBackupPeriod": "Tuesday,Thursday,Saturday",
    "ArchiveBackupKeepCount": 1,
    "LogBackupRetentionPeriod": "7",
    "LogBackupLocalRetentionNumber": 60,
    "BackupLog": "Enable",
    "EnableBackupLog": "1",
    "SupportReleasedKeep": 0,
    "SupportVolumeShadowCopy": 1,
    "LocalLogRetentionSpace": "30",
    "BackupRetentionPeriod": 10,
    "DuplicationContent": "",
    "BackupInterval": "30"
}
```

#### ModifyBackupPolicy

Modifies the backup settings of an ApsaraDB RDS instance. Before you call this operation, make sure that the following requirements are met: The instance is not a read-only instance. The instance is in the running state.

**Request parameters**

| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
|---|---|---|---|---|
| BackupPolicyMo de | String | No | DataBackupPolic y | The type of backup that you want to perform for the instance. Valid values: DataBackupPolicy: data backup LogBackupPolicy: log backup |
| PreferredBackup Time | String | No | 00:00Z-01:00Z | The time to execute the backup task. Specify the time in the ISO 8601 standard in the HH:mmZ-HH:mmZ format. The time must be in UTC. Note This parameter is required when you set the BackupPolicyMode parameter to DataBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to DataBackupPolicy. |

ApsaraDB for RDS

| PreferredBackup Period | String | No | Monday | The cycle based on which you want to perform backups. Specify at least two days of the week and separate these days with commas (,). Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday Note A backup policy is specified by this parameter and the BackupInterval parameter. For example, if you set this parameter to Saturday,Sunday and the BackupInterval parameter to 30, a backup is performed once every 30 minutes on every Saturday and Sunday. This parameter is required when you set the BackupPolicyMode parameter to DataBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to DataBackupPolicy. |
|---|---|---|---|---|

ApsaraDB for RDS

| BackupRetentio nPeriod | String | No | 7 | The number of days for which you want to retain data backup files. Valid values: 7 to 730. Note This parameter is required when you set the BackupPolicyMode parameter to DataBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to DataBackupPolicy. |
|---|---|---|---|---|
| BackupLog | String | No | Enable | Specifies whether to enable log backup. Valid values: Enable Disabled Note This parameter is required when you set the BackupPolicyMode parameter to DataBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to DataBackupPolicy. |

ApsaraDB for RDS

| LogBackupReten tionPeriod | String | No | 7 | The number of days for which you want to retain log backup files. Valid values: 7 to 730. The log backup retention period cannot be longer than the data backup retention period. Note If you enable the log backup feature, you can specify the log backup retention period. This applies only when the instance runs MySQL or PostgreSQL. This parameter is valid when you set the BackupPolicyMode parameter to DataBackupPolicy or LogBackupPolicy. |
|---|---|---|---|---|
| EnableBackupLo g | String | No | 1 | Specifies whether to enable log backup. Valid values: True or 1: enables log backup. False or 0: disables log backup. Note This parameter is required when you set the BackupPolicyMode parameter to LogBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to LogBackupPolicy. |

ApsaraDB for RDS

| LocalLogRetenti onHours | String | No | 18 | The number of hours for which you want to retain log backup files on the instance. Valid values: 0 to 7 × 24. The value 0 specifies not to retain log backup files on the instance. Note This parameter is required when you set the BackupPolicyMode parameter to LogBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to LogBackupPolicy. |
|---|---|---|---|---|
| LocalLogRetenti onSpace | String | No | 30 | The maximum storage usage that is allowed for log backup files on the instance. If the storage usage for log backup files exceeds the value of this parameter, ApsaraDB RDS deletes earlier log backup files until the storage usage falls below the value of this parameter. Valid values: 0 to 50. You can retain the default value. Note This parameter is required when you set the BackupPolicyMode parameter to LogBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to LogBackupPolicy. |

ApsaraDB for RDS

| HighSpaceUsage Protection | String | No | Enable | Specifies whether to forcibly delete log backup files when the storage usage of the instance exceeds 80% or the remaining storage space is less than 5 GB. Valid values: Enable and Disable. You can retain the default value. Note This parameter is required when you set the BackupPolicyMode parameter to LogBackupPolicy. This parameter is valid only when you set the BackupPolicyMode parameter to LogBackupPolicy. |
|---|---|---|---|---|
| Duplication | String | No | None | An invalid parameter. |
| DuplicationCont ent | String | No | None | An invalid parameter. |
| DuplicationLocat ion | String | No | None | An invalid parameter. |
| LogBackupFrequ ency | String | No | LogInterval | The frequency at which you want to perform log backups. Valid values: LogInterval: performs log backups every 30 minutes. Default value: same as the data backup frequency. Note The value LogInterval is supported only when the instance runs SQL Server. This parameter is valid only when you set the BackupPolicyMode parameter to DataBackupPolicy. |

ApsaraDB for RDS

| CompressType | String | No | 4 | The format that is used to compress backups. Valid values: 1: The zlib tool is used to compress backups into .tar.gz files. 4: The QuickLZ tool is used to compress data into .xb.gz files. This compression format is supported only when the instance runs MySQL 5.6 or 5.7. Backup files in this compression format can be used to restore individual databases or tables. 8: The QuickLZ tool is used to compress data into .xb.gz files. This compression format is supported only when the instance runs MySQL 8.0. This compression format cannot be used to restore individual databases or tables. Note This parameter is valid only when you set the BackupPolicyMode parameter to DataBackupPolicy. |
|---|---|---|---|---|
| ReleasedKeepPo licy | String | No | None | The policy that is used to retain archived backup files if the instance is released. Default value: None. Valid values: None: No archived backup files are retained. Lastest: Only the last archived backup file is retained. All:: All archived backup files are retained. Note This parameter is valid only when you set the BackupPolicyMode parameter to DataBackupPolicy. |
| LogBackupLocal RetentionNumbe r | Integer | No | 60 | The number of log backup files that you want to retain on the instance. Default value: 60. Valid values: 6 to 100. Note This parameter is valid only when you set the BackupPolicyMode parameter to LogBackupPolicy. |

| Parameter | Type | Example | Description |
|---|---|---|---|

ApsaraDB for RDS

**Response parameters**

| CompressType | String | 4 | The format that is used to compress backups. Valid values: 0: Backups are not compressed. 1: Backups are compressed by using the zlib tool. 2: Backups are compressed in parallel by using the zlib tool. 4: Backups are compressed by using the QuickLZ tool and can be used to restore individual databases or tables. 8: Backups are compressed by using the QuickLZ tool but cannot be used to restore individual databases or tables. This value is supported only when the instance runs MySQL 8.0. |
|---|---|---|---|
| DBInstanceID | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| EnableBackup Log | String | 1 | Indicates whether log backup is enabled. Valid values: 1: Log backup is enabled. 0: Log backup is disabled. |
| HighSpaceUsa geProtection | String | Disable | Indicates whether log backup files are forcibly deleted when the storage usage of the instance exceeds 80% or the remaining storage space is less than 5 GB. |
| LocalLogReten tionHours | Integer | 18 | The number of hours for which log backup files are retained on the instance. |
| LocalLogReten tionSpace | String | 30 | The maximum storage usage for log backup files on the instance. |
| LogBackupLoc alRetentionNu mber | Integer | 60 | The number of log backup files that are retained on the instance. |
| RequestId | String | DA147739-AEAD- 4417-9089- 65E9B1D8240D | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyBackupPolicy &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBackup | The operation that you want to perform. Set the value to DeleteBackup. |

ApsaraDB for RDS `XML` format

```xml
        <HighSpaceUsageProtection>Disable</HighSpaceUsageProtection>
      <DBInstanceID>rm-bp1z3xxxxx</DBInstanceID>
      <RequestId>E4BF5598-ED12-4406-AAA4-F375428BE741</RequestId>
      <LocalLogRetentionHours>18</LocalLogRetentionHours>
      <EnableBackupLog>1</EnableBackupLog>
      <LocalLogRetentionSpace>30</LocalLogRetentionSpace>
      <LogBackupLocalRetentionNumber>60</LogBackupLocalRetentionNumber>
```

`JSON` format

```json
{
    "HighSpaceUsageProtection": "Disable",
    "DBInstanceID": "rm-bp1z3xxxxx",
    "RequestId": "E4BF5598-ED12-4406-AAA4-F375428BE741",
    "LocalLogRetentionHours": "18",
    "EnableBackupLog": "1",
    "LocalLogRetentionSpace": "30",
    "LogBackupLocalRetentionNumber": 60
}
```

#### DeleteBackup

Deletes backup sets of an ApsaraDB RDS instance. Backup sets of only the instance itself are deleted. Backup sets of the associated instances such as read-only, disaster recovery, and cloned instances are not deleted. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance is of the High-availability Edition and runs MySQL or PostgreSQL. If the log backup feature is disabled, ApsaraDB RDS instances cannot be restored by point in time. You can delete data backup sets that are retained for more than seven days. If the log backup feature is enabled and the retention period of log backups is shorter than the retention period of data backups, the data backup sets that are retained for longer than the retention period of log backups can be deleted.

**Request parameters**

| BackupId | String | Yes | 324909958 | The ID of the backup set. You can call the DescribeBackups operation to query the IDs of backup sets. Up to 100 IDs can be specified in a single request. Separate multiple IDs with commas (,). Note Only the backup sets whose StoreStatus is Enabled when you call the DescribeBackups operation can be deleted. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 37441409-FFD1- 40AA-8EC5- 9ECF5E2F7C29 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
&DBInstanceId=rm-uf6wjk5xxxxxxx &BackupId=324909958 &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>37441409-FFD1-40AA-8EC5-9ECF5E2F7C29</RequestId>
```

`JSON` format

```json
{
    "RequestId": "37441409-FFD1-40AA-8EC5-9ECF5E2F7C29"
}
```

#### DeleteBackupFile

Deletes backup sets of an ApsaraDB RDS for SQL Server instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBackupFil e | The operation that you want to perform. Set the value to DeleteBackupFile. |
| DBInstanceId | String | Yes | rm- bp6wjk5xxxxxx | The ID of the instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. Note You can call the DescribeRegions operation to query the most recent region list. |
| BackupId | String | No | 293044600 | The ID of the backup set. You can specify up to 100 backup set IDs. Separate multiple backup set IDs with commas (,). Note For ApsaraDB RDS for SQL Server instances, you can specify backup set IDs only for individual databases. You can call the DescribeBackups operation to query the IDs of backup sets. |
| DBName | String | No | testdb | The name of the database. |
| BackupTime | String | No | 2011-06- 11T16:00:00Z | The point in time before which the backup sets that you want to delete are created. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DeletedBakset Ids | Integer | 293044600 | The IDs of the deleted backup sets. |
| RequestId | String | C7B3A91C-0ACD- 4948-ACAE- xxxxxxxD4069 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackup Tasks | The operation that you want to perform. Set the value to DescribeBackupTasks. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Flag | String | No | None | A hidden parameter. |
| BackupJobId | String | No | 4762614 | The ID of the backup task. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DeleteBackupFile &DBInstanceId=rm-bp6wjk5xxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>C7B3A91C-0ACD-4948-ACAE-xxxxxxxD4069</RequestId> <DeletedBaksetIds>
    <DeletedBaksetIds>1111</DeletedBaksetIds>
</DeletedBaksetIds>
```

`JSON` format

```json
{"RequestId":"C7B3A91C-0ACD-4948-ACAE-xxxxxxxD4069","DeletedBaksetIds": {"DeletedBaksetIds":"1111"}}
```

#### DescribeBackupTasks

Queries the backup tasks of an ApsaraDB RDS instance.

**Request parameters**

| BackupMode | String | No | Automated | The backup mode. Valid values: Automated Manual |
|---|---|---|---|---|
| BackupJobStatus | String | No | NoStart | The state of the backup task. Valid values: NoStart Progressing By default, this operation returns backup tasks in both states. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of BackupJob |  | Details of the backup tasks. |
| BackupJob |  |  |  |
| BackupId | String | 346650271 | The ID of the backup set that is generated by the backup task. Note You can obtain the ID of the backup set only if you specify the BackupJobId parameter after the value of Finished is returned for the BackupStatus parameter. |
| BackupJobId | String | 4762614 | The ID of the backup task. |
| BackupProgres sStatus | String | NoStart | The state of the backup program. Valid values: NoStart Preparing Waiting Uploading Checking Finished |

ApsaraDB for RDS

**Response parameters**

| BackupStatus | String | NoStart | The state of the backup task. Valid values: NoStart Checking Preparing Waiting Uploading Finished Failed Note This parameter is returned only when a backup task is executed. |
|---|---|---|---|
| JobMode | String | Automated | The backup mode. Valid values: Automated Manual |
| Process | String | 25 | The progress of the backup task in percentage. |
| TaskAction | String | NormalBackupTask | The type of the backup task. Valid values: TempBackupTask: temporary backup task NormalBackupTask: regular backup task |
| RequestId | String | 90496720-2319- 42A8-87CD- FCE4DF95EBED | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeBackupTasks &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLogBac kupFiles | The operation that you want to perform. Set the value to DescribeLogBackupFiles. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| EndTime | String | Yes | 2018-10- 31T08:40Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |

ApsaraDB for RDS

```xml
      <Items>
            <BackupJob>
                  <JobMode>Automated</JobMode>
                  <BackupProgressStatus>NoStart</BackupProgressStatus>
                  <TaskAction>NormalBackupTask</TaskAction>
                  <BackupStatus>NoStart</BackupStatus>
                  <BackupJobId>4762614</BackupJobId>
            </BackupJob>
      </Items>
      <RequestId>90496720-2319-42A8-87CD-FCE4DF95EBED</RequestId>
```

`JSON` format

```json
{
    "Items": {
        "BackupJob": [
            {
                "JobMode": "Automated",
                "BackupProgressStatus": "NoStart",
                "TaskAction": "NormalBackupTask",
                "BackupStatus": "NoStart",
                "BackupJobId": 4762614
            }
```

]

```json
    },
    "RequestId": "90496720-2319-42A8-87CD-FCE4DF95EBED"
}
```

#### DescribeLogBackupFiles

Queries the log backup files of an ApsaraDB RDS instance.

**Request parameters**

| StartTime | String | Yes | 2018-10- 01T08:40Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
|---|---|---|---|---|
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 to 1000. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of BinLogFile |  | The log backup files. |
| BinLogFile |  |  |  |
| DownloadLink | String | http://rdsbak-hz- v3.oss-cn- hangzhou.aliyuncs. com/xxxxx | The HTTP download URL. If the backup file cannot be downloaded, an empty string is returned. |
| FileSize | Long | 788480 | The size of the log backup file. Unit: byte. |
| IntranetDownl oadLink | String | http://rdsbak-hz- v3.oss-cn- hangzhou.aliyuncs. com/xxxxx | The URL that is used to download the log backup file over an internal network. If the backup file cannot be downloaded, an empty string is returned. This URL is valid for 1 hour. |
| LinkExpiredTi me | String | 2019-03- 01T15:04:13Z | The expiration time of the URL. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| LogBeginTime | String | 2018-10- 31T08:40Z | The start time of the log backup file. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |

ApsaraDB for RDS

**Response parameters**

| LogEndTime | String | 2018-10- 31T08:40Z | The end time of the log backup file. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 100 | The number of log backup files on the current page. |
| RequestId | String | F8EC669C-FC85- 43D7-AF06- C3641626B37E | The ID of the request. |
| TotalFileSize | Long | 2300 | The total size of log backup files. Unit: byte. |
| TotalRecordCo unt | Integer | 17 | The total number of log backup files. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeLogBackupFiles &DBInstanceId=rm-uf6wjk5xxxxxxx &StartTime=2018-10-01T08:40Z &EndTime=2018-10-31T08:40Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <Items></Items>
      <PageNumber>1</PageNumber>
      <TotalRecordCount>0</TotalRecordCount>
      <RequestId>F8EC669C-FC85-43D7-AF06-C3641626B37E</RequestId>
      <PageRecordCount>0</PageRecordCount>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetaLis t | The operation that you want to perform. Set the value to DescribeMetaList. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

ApsaraDB for RDS

```json
{
    "Items": {
        "BinLogFile": [ ]
    },
    "PageNumber": 1,
    "TotalRecordCount": 0,
    "RequestId": "F8EC669C-FC85-43D7-AF06-C3641626B37E",
    "PageRecordCount": 0
}
```

#### DescribeMetaList

Queries the information of the restorable databases and tables in a specific backup set. Before you call the RestoreTable operation to restore individual databases or tables of an ApsaraDB RDS for MySQL instance, you can call this operation to query the information of the restorable databases and tables.

**Note**

This operation is supported only for instances that run MySQL 8.0, MySQL 5.7, or MySQL 5.6 on RDS High-availability Edition with local SSDs.

**Request parameters**

| RestoreType | String | No | BackupSetID | The method that is used to restore data. Valid values: BackupSetID: Data is restored from a backup set. If you use this value, you must also specify the BackupSetID parameter. RestoreTime: Data is restored to a specific point in time. If you use this value, you must also specify the RestoreTime parameter. Default value: BackupSetID. |
|---|---|---|---|---|
| BackupSetID | String | No | 14358 | The ID of the backup set from which you want to restore data. You can call the DescribeBackups operation to query the IDs of backup sets. Note This parameter is required when you set the RestoreType parameter to BackupSetID. |
| RestoreTime | String | No | 2019-05- 30T03:29:10Z | The point in time to which you want to restore data. The specified point in time must be earlier than the current time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. You can call the DescribeBackups operation to query the restorable time range. Note This parameter is required when you set the RestoreType parameter to RestoreTime. |
| GetDbName | String | No | testdb1 | The name of the database to query. ApsaraDB RDS implements exact match based on the value of this parameter and returns the name of the matched database and the names of all tables contained in the database. Note If you leave this parameter unspecified, ApsaraDB RDS returns all databases that are created on the instance. |

ApsaraDB for RDS

| Pattern | String | No | test | The keyword in the name of the database to query. ApsaraDB RDS implements fuzzy match based on the value of this parameter and returns only the names of the matched databases. Note For example, if you set the value to test , ApsaraDB RDS returns testdb1 and testdb2 . Then, you can specify the GetDbName parameter to query tables in the required database. |
|---|---|---|---|---|
| PageSize | String | No | 1 | The number of entries to return on each page. Default value: 1. Note This parameter is valid only when you specify the PageIndex parameter. |
| PageIndex | String | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. Note This parameter is valid only when you specify the PageSize parameter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceNa me | String | rm-uf6wjk5xxxxxxx | The name of the instance. |
| Items | Array of Meta |  | The information of the databases and tables contained in the backup set. |
| Meta |  |  |  |
| Database | String | testdb1 | The name of the database. |
| Size | String | 64 | The size of the tables. Unit: KB. |
| Tables | String | test1 | The names of the tables. |

ApsaraDB for RDS

**Response parameters**

| PageNumber | Integer | 1 | The page number of the returned page. |
|---|---|---|---|
| PageRecordCo unt | Integer | 1 | The number of entries returned on the current page. |
| RequestId | String | 60F9A12A-16B8- 4728-B099- 4CA38D32C31C | The ID of the request. |
| TotalPageCou nt | Integer | 1 | The total number of pages returned. |
| TotalRecordCo unt | Integer | 1 | The total number of entries returned. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeMetaList &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <TotalPageCount>1</TotalPageCount>
      <TotalRecordCount>1</TotalRecordCount>
      <PageRecordCount>1</PageRecordCount>
      <RequestId>60F9A12A-16B8-4728-B099-4CA38D32C31C</RequestId>
      <PageNumber>1</PageNumber>
      <Items>
            <Meta>
                  <Size>64</Size>
                  <Database>testdb1</Database>
                  <Tables>test1</Tables>
            </Meta>
      </Items>
      <DBInstanceName>rm-uf6wjk5xxxxxxx</DBInstanceName>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RestoreTable | The operation that you want to perform. Set the value to RestoreTable. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx xxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

ApsaraDB for RDS

```json
{
    "TotalPageCount": "1",
    "TotalRecordCount": "1",
    "PageRecordCount": "1",
    "RequestId": "60F9A12A-16B8-4728-B099-4CA38D32C31C",
    "PageNumber": "1",
    "Items": {
        "Meta": [{
            "Size": "64",
            "Database": "testdb1",
            "Tables": "test1"
        }]
    },
    "DBInstanceName": "rm-uf6wjk5xxxxxxx"
}
```

#### RestoreTable

Restores individual databases or tables for an ApsaraDB RDS instance. ApsaraDB RDS for MySQL allows you to restore individual databases or tables. If one or more databases or tables of an ApsaraDB RDS instance are accidentally deleted, you can use a backup set to restore the databases or tables. For more information, see Restore individual databases and tables for an ApsaraDB RDS for MySQL instance. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The instance does not have ongoing migration tasks. If you want to restore data to a specific point in time, the log backup feature is enabled for the instance. The restoration of individual databases or tables is enabled, and new backups are created. The instance does not contain tables that have the same names as the new tables.

**Note**

This operation is supported only for instances that run MySQL.

**Request parameters**

| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
|---|---|---|---|---|
| BackupId | String | No | 9026262 | The ID of the backup set. You can call the DescribeBackups operation to obtain the IDs of backup sets. Note You must specify at least one of BackupId and RestoreTime. |
| RestoreTime | String | No | 2011-06- 11T16:00:00Z | The point in time to which you want to restore databases within the backup retention period. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Note You must specify at least one of BackupId and RestoreTime. The log backup feature must be enabled. |
|  |  |  |  | The databases and tables that you want to restore. Format: |

ApsaraDB for RDS

|  |  |  |  | [{"type":"db","name":"<The name of Database 1 on the source instance>","newname":"<The name of Database 1 on the destination instance>","tables": [{"type":"table","name":" |
|---|---|---|---|---|
| TableMeta | String | No | [{"type":"db","n ame":"testdb1"," newname":"test db1 new","table _ s": [{"type":"table", "name":"testdb1 table1","newna me":"testdb1tab le1 new"}]}] _ | <The name of Table 1 in Database 1 on the source instance>","newname":"<The name of Table 1 in Database 1 on the destination instance>"}, {"type":"table","name":"<The name of Table 2 in Database 1 on the source instance>","newname":"<The name of Table 2 in Database 1 on the destination instance>"}]}, {"type":"db","name":"<The name of Database 2 on the source instance>","newname":"<The name of Database 2 on the destination instance>","tables": [{"type":"table","name":" <The name of Table 3 in Database 2 on the source instance>","newname":"<The name of Table 3 in Database 2 on the destination instance>"}, {"type":"table","name":"<The name of Table 4 in Database 2 on the source instance>","newname":"<The name of Table 4 in Database 2 on the destination instance>"}]}] |

ApsaraDB for RDS

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | EA2D4F34-01A7- 46EB-A339- D80882135206 | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDetach edBackups | The operation that you want to perform. Set the value to DescribeDetachedBackups. |
| Region | String | Yes | cn-hangzhou | The region ID of the instance. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```json
&DBInstanceId=rm-uf6wjk5xxxxxxxxxx &RestoreTime=2019-08-20T16:00:00Z &TableMeta=[{"type":"db","name":"dtstestdata","newname":"dtstestdata","tables":[{"type" :"table","name":"customer_old","newname":"customer_old123"}, {"type":"table","name":"order","newname":"order123"}]}] &<Common request parameters>
```

Sample success responses `XML` format

```xml
  <RequestId>EA2D4F34-01A7-46EB-A339-D80882135206</RequestId>
```

`JSON` format

```json
{
    "RequestId": "EA2D4F34-01A7-46EB-A339-D80882135206"
}
```

#### DescribeDetachedBackups

Queries the backup sets of an ApsaraDB RDS instance that is deleted. This operation is supported for instances that run MySQL with local SSDs.

**Request parameters**

| DBInstanceId | String | No | rm- uf6wjk5xxxxxxx | The ID of the instance. |
|---|---|---|---|---|
| BackupId | String | No | 327xxxxx3 | The ID of the backup set. |
| BackupLocation | String | No | cn-hangzhou | The region where the backup set resides. |
| BackupStatus | String | No | Success | The state of the backup set. Valid values: Success Failed |
| BackupMode | String | No | Automated | The backup mode. Valid values: Automated Manual |
| StartTime | String | No | 2021-03- 01T16:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | No | 2021-03- 15T16:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Default value: 30. Valid values: 30 50 100 |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|

ApsaraDB for RDS

**Response parameters**

| Items | Array of Items |  | Details of backup sets. |
|---|---|---|---|
| Items |  |  |  |
| BackupDBNam es | String | testdb | The names of databases. |
| BackupDownlo adURL | String | http://rdsbak-hz- v3.oss-cn- hangzhou.aliyuncs. com/xxxxx | The URL that is used to download the log backup file over the Internet. If the backup set cannot be downloaded, an empty string is returned. |
| BackupEndTim e | String | 2019-02- 13T12:20:00Z | The end time of the backup task. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| BackupExtract ionStatus | String | None | The state of all backup sets. |
| BackupId | String | 327xxxxx3 | The ID of the backup set. |
| BackupIntrane tDownloadURL | String | http://rdsbak-hz- v3.oss-cn- hangzhou- internal.aliyuncs.co m/xxxxx | The URL that is used to download the log backup file over an internal network. If the backup set cannot be downloaded, an empty string is returned. |
| BackupLocatio n | String | cn-hangzhou | The region where the backup set resides. |
| BackupMethod | String | Physical | The method that is used to generate the backup set. Valid values: Logical: logical backup Physical: physical backup |
| BackupMode | String | Automated | The backup mode. Valid values: Automated Manual |
| BackupScale | String | None | The scalability of the backup set. |
| BackupSize | Long | 2167808 | The size of the backup set. Unit: byte. |
| BackupStartTi me | String | 2019-02- 03T12:20:00Z | The start time of the backup task. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |

ApsaraDB for RDS

| BackupStatus | String | Success | The state of the backup set. |
|---|---|---|---|
| BackupType | String | FullBackup | The backup type. Valid values: FullBackup IncrementalBackup |
| ConsistentTim e | Long | 1576506856 | The point in time at which the data in the backup set is consistent. The value of this parameter is a timestamp. Note This parameter is supported only for instances that run MySQL 5.6. If the instance does not run MySQL 5.6, the value 0 is returned. |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| HostInstanceId | String | 5882781 | The No. of the instance that generates the backup set. This parameter is used to indicate whether the instance that generates the backup set is a primary instance or a secondary instance. |
| MetaStatus | String | OK | The state of the backup set that is used to restore individual databases or tables. Valid values: OK: The backup set is normal. LARGE: The backup set contains an abnormally large number of tables. It cannot be used to restore individual databases or tables. EMPTY: The backup set is generated from a failed backup task. |
| SlaveStatus | String | None | The state of the secondary instance. |
| StoreStatus | String | Disabled | Indicates whether the backup set can be deleted. Valid values: Enabled: The backup set can be deleted. Disabled: The backup set cannot be deleted. |
| TotalBackupSi ze | Long | 2167808 | The size of all files in the backup set. Unit: byte. |
| PageNumber | String | 1 | The page number of the returned page. |

ApsaraDB for RDS

| PageRecordCo unt | String | 30 | The number of backup sets on the current page. |
|---|---|---|---|
| RequestId | String | 1A6D328C-84B8- 40DC-BF49- 6C73984D7494 | The ID of the request. |
| TotalBackupSi ze | Long | 2167808 | The size of all files in all backup sets. Unit: byte. |
| TotalRecordCo unt | String | 100 | The total number of entries returned. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDetachedBackups &Region=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format ApsaraDB for RDS

```xml
    <TotalRecordCount>1</TotalRecordCount>
    <PageRecordCount>1</PageRecordCount>
    <RequestId>B0BBC25A-6B3E-4BFD-A052-48664294E20D</RequestId>
    <PageNumber>1</PageNumber>
    <Items>
            <Backup>
                    <BackupMethod>Snapshot</BackupMethod>
                    <BackupInitiator>System</BackupInitiator>
                    <StorageClass>0</StorageClass>
                    <BackupMode>Automated</BackupMode>
                    <BackupSize>161061273600</BackupSize>
                    <BackupId>677987116</BackupId>
                    <IsAvail>1</IsAvail>
                    <HostInstanceID>9232003</HostInstanceID>
                    <BackupDBNames></BackupDBNames>
                    <StoreStatus>Disabled</StoreStatus>
                    <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
                    <BackupDownloadURL></BackupDownloadURL>
                    <BackupEndTime>2020-07-11T05:07:33Z</BackupEndTime>
                    <BackupStartTime>2020-07-11T05:07:33Z</BackupStartTime>
                    <ConsistentTime>0</ConsistentTime>
                    <BackupType>FullBackup</BackupType>
                    <MetaStatus></MetaStatus>
                    <BackupScale>DBInstance</BackupScale>
                    <BackupStatus>Success</BackupStatus>
                    <BackupLocation>OSS</BackupLocation>
            </Backup>
    </Items>
    <TotalBackupSize>161061273600</TotalBackupSize>
```

`JSON` format ApsaraDB for RDS

```json
{
    "TotalRecordCount": 1,
    "PageRecordCount": 1,
    "RequestId": "B0BBC25A-6B3E-4BFD-A052-48664294E20D",
    "PageNumber": 1,
    "Items": {
        "Backup": [
            {
          "BackupMethod":"Physical",
                    "BackupIntranetDownloadURL":"http://...",
                    "BackupMode":"Automated",
                    "BackupSize":9405440,
                    "BackupId":509538643,
                    "IsAvail":1,
                    "HostInstanceID":100453678,
                    "BackupDBNames":"",
                    "StoreStatus":"Enabled",
                    "DBInstanceId":"rm-uf6wjk5xxxxxxx",
                    "BackupDownloadURL":"https://...",
                    "BackupEndTime":"2020-09-04T02:55:36Z",
                    "BackupStartTime":"2020-09-04T02:54:04Z",
                    "ConsistentTime":"1599188049",
                    "BackupType":"FullBackup",
                    "MetaStatus":"OK",
                    "BackupScale":"DBInstance",
                    "BackupStatus":"Success",
                    "BackupLocation":"OSS"
            }
```

]

```json
    },
    "TotalBackupSize": "161061273600"
}
```

### Database proxy

#### CalculateDBInstanceWeight

Queries the read weights of a primary ApsaraDB RDS instance and its read-only instances. When the read/write splitting feature is enabled, this operation is used to calculate systemassigned read weights. For more information about custom read weights, see DescribeDBInstanceNetInfo. Before you call this operation, make sure that the following requirements are met: The shared proxy feature is enabled for the primary instance. The primary instance runs one of the following database engine versions and RDS editions: MySQL 5.7 on RDS High-availability Edition (with local SSDs) MySQL 5.6 SQL Server 2017 EE

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CalculateDBInst anceWeight | The operation that you want to perform. Set the value to CalculateDBInstanceWeight. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the primary instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of DBInstanceWe ight |  | Details of the system-assigned read weights. |
| DBInstanceWe ight |  |  |  |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| DBInstanceTy pe | String | Master | The role of the instances. Valid values: Master: primary instance Readonly: read-only instance |
| Weight | String | 100 | The read weight that ApsaraDB RDS calculates in real time for the instance. |
| ReadonlyInsta nceSQLDelaye dTime | String | 30 | The latency of data replication to the read- only instances that are attached to the primary instance. The read-only instances replicate data from the primary instance at the latency that is specified by the ReadonlyInstanceSQLDelayedTime parameter. Unit: seconds. |
| RequestId | String | C816A4BF-A6EC- 4722-95F9- 2055859CCFD2 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

ApsaraDB for RDS

```
http(s)://rds.example.com/?Action=CalculateDBInstanceWeight &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <items>
            <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
            <DBInstanceType>Master</DBInstanceType>
            <Weight></Weight>
            <Availability></Availability>
      </items>
      <requestId>C816A4BF-A6EC-4722-95F9-2055859CCFD2</requestId>
```

`JSON` format

```json
{
    "items": [
        {
            "DBInstanceId": "rm-uf6wjk5xxxxxxx",
            "DBInstanceType": "Master",
            "Weight": "",
            "Availability": ""
        }
```

`],`

```json
    "requestId": "C816A4BF-A6EC-4722-95F9-2055859CCFD2"
}
```

#### DescribeDBInstanceProxyConfiguration

Queries the shared proxy settings on an ApsaraDB RDS instance. This operation is used to query the original shared proxy settings rather than the latest dedicated proxy settings. For more information about how to query the dedicated proxy settings, see DescribeDBProxy. Before you call this operation, make sure that the following requirements are met: The shared proxy feature is enabled for the instance. The read/write splitting feature is enabled for the instance.

**Request parameters**

| Action | String | Yes | DescribeDBInsta nceProxyConfigu ration | The operation that you want to perform. Set the value to DescribeDBInstanceProxyConfigu ration. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx xxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AttacksProtect ionConfigurati on | String | {\"check interval s _ _ econds\":\"0\",\"ma x failed login atte _ _ _ mpts\":\"0\",\"block ing seconds\":\"0\", _ \"status\":\"Disable \"} | Indicates whether the mechanism that is used to prevent brute-force attacks is enabled. Valid values: Enable Disable The return value is a JSON string. Example: {"status":"Disable", "check interval seconds": 60, _ _ "max failed login attempts": 60, _ _ _ "blocking seconds": 600} _ Description: Each client allows {max failed login attempts} logon _ _ _ attempts that fail due to incorrect passwords within {check interval seconds} seconds. If _ _ one more such attempt is conducted, the client must wait {blocking seconds} seconds before you _ can try again. Valid values: check interval seconds: 30 to 600. _ _ Unit: seconds. max failed login attempts: 10 to _ _ _ 5000. blocking seconds: 30 to 3600. Unit: _ seconds. |
| PersistentCon nectionsConfig uration | String | {\"status\":\"Disabl e\"} | Indicates whether the short-lived connection optimization feature is enabled. Valid values: Enable Disable The return value is a JSON string. Example: {"status":"Disable"}. |

ApsaraDB for RDS

**Response parameters**

| TransparentSw itchConfigurati on | String | {\"status\":\"Enabl e\"} | Indicates whether the transparent switchover feature is enabled. Valid values: Enable Disable The return value is a JSON string. Example: {"status":"Enable"}. |
|---|---|---|---|
| RequestId | String | E9DD55F4-1A5F- 48CA-BA57- DFB3CA8C4C34 | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?DBInstanceId=rm-uf6wjk5xxxxxxxxxx &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```json
<DescribeDBInstanceProxyConfigurationResponse>
      <PersistentConnectionsConfiguration>{"status":"Disable"}
</PersistentConnectionsConfiguration>
      <TransparentSwitchConfiguration>{"status":"Enable"}
</TransparentSwitchConfiguration>
      <AttacksProtectionConfiguration>
{"check_interval_seconds":"0","max_failed_login_attempts":"0","blocking_seconds":"0","sta s":"Disable"}</AttacksProtectionConfiguration>
      <RequestId>E9DD55F4-1A5F-48CA-BA57-DFB3CA8C4C34</RequestId>
</DescribeDBInstanceProxyConfigurationResponse>
```

`JSON` format

```json
{
    "PersistentConnectionsConfiguration": "{\"status\":\"Disable\"}",
    "TransparentSwitchConfiguration": "{\"status\":\"Enable\"}",
    "AttacksProtectionConfiguration": "
{\"check_interval_seconds\":\"0\",\"max_failed_login_attempts\":\"0\",\"blocking_seconds\ \"0\",\"status\":\"Disable\"}",
    "RequestId": "E9DD55F4-1A5F-48CA-BA57-DFB3CA8C4C34"
}
```

Queries the details of the dedicated proxy of an ApsaraDB RDS instance.

#### DescribeDBProxy

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBProx y | The operation that you want to perform. Set the value to DescribeDBProxy. |
| DBInstanceId | String | Yes | rm- bp1ja4f56s7us** ** | The ID of the instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBProxyConne ctStringItems | Array of DBProxyConne ctStringItems |  | Details of the configured proxy endpoints. |
| DBProxyConne ctStringItems |  |  |  |
| DBProxyConne ctString | String | gos787jog2wk0ye1 ****- rw4rm.rwlb.rds.aliy uncs.com | The endpoint of the proxy terminal. |
| DBProxyConne ctStringNetTyp e | String | InnerString | The network type of the proxy endpoint. Valid values: InnerString: internal network OuterString: Internet |

ApsaraDB for RDS ApsaraDB RDS provides the dedicated proxy feature to deliver capabilities such as read/write splitting and short-lived connection optimization. Before you call this operation, make sure that the instance runs one of the following database engine versions and RDS editions: MySQL 8.0 on RDS Enterprise Edition (minor version of 20191204 or later) MySQL 8.0 on RDS High-availability Edition (minor version of 20190915 or later) MySQL 5.7 on RDS Enterprise Edition (minor version of 20191128 or later) MySQL 5.7 on RDS High-availability Edition (minor version of 20190925 or later) MySQL 5.6 on RDS High-availability Edition (minor version of 20200229 or later)

**Request parameters**

**Response parameters**

| DBProxyConne ctStringNetWo rkType | String | 1 | The network type of the proxy endpoint. Valid values: 0: Internet 1: classic network 2: VPC |
|---|---|---|---|
| DBProxyConne ctStringPort | String | 3306 | The port that is used to connect to the proxy endpoint. |
| DBProxyEndpo intId | String | 20**** | The ID of the proxy terminal to which the proxy endpoint belongs. |
| DBProxyEndpo intName | String | gos787jog2wk0ye1 **** | The name of the proxy terminal to which the proxy endpoint belongs. |
| DBProxyVpcIn stanceId | String | rm- bp145737x5****13 1161274792**** | The ID of the proxy instance. |
| DBProxyInstan ceCurrentMino rVersion | String | 1.13.11 | The dedicated proxy version that is running on the instance. |
| DBProxyInstan ceLatestMinor Version | String | 1.13.12 | The latest dedicated proxy version that is available to the instance. |
| DBProxyInstan ceNum | Integer | 1 | The number of proxy instances that are enabled on the instance. |
| DBProxyInstan ceStatus | String | Running | The state of the proxy instance. Valid values: CREATING: The proxy instance is being created. ACTIVATION: The proxy instance is running. DELETING: The proxy instance is being deleted. RESTARTING: The proxy instance is restarting. CLASS CHANGING: The specifications _ of the proxy instance are being changed. TRANSING: The proxy instance is being migrated. MINOR VERSION UPGRADING: The _ _ minor version of the proxy instance is being updated. |

ApsaraDB for RDS

| DBProxyInstan ceType | String | 2 | The type of the proxy enabled on the instance. Valid values: 1: shared proxy 2: dedicated proxy |
|---|---|---|---|
| DBProxyServic eStatus | String | Startup | The state of the dedicated proxy feature. Startup: enabled Shutdown: disabled |
| RequestId | String | 909A69EE-71C8- 4417-A0B9- FF085407E1E3 | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBProxy &DBInstanceId=rm-bp1ja4f56s7us**** &<Common request parameters>
```

Sample success responses `XML` format ApsaraDB for RDS

```xml
      <DBProxyInstanceName>gos787jog2wk0ye1****</DBProxyInstanceName>
      <DBProxyInstanceCurrentMinorVersion>1.13.11</DBProxyInstanceCurrentMinorVersion>
      <DBProxyServiceStatus>Startup</DBProxyServiceStatus>
      <DBProxyInstanceNum>1</DBProxyInstanceNum>
      <DBProxyInstanceLatestMinorVersion>1.13.12</DBProxyInstanceLatestMinorVersion>
      <RequestId>909A69EE-71C8-4417-A0B9-FF085407E1E3</RequestId>
      <DbProxyEndpointItems>
            <DbProxyEndpointItems>
                  <DbProxyEndpointName>gos787jog2wk0ye1****</DbProxyEndpointName>
                  <DbProxyEndpointAliases>proxy-test</DbProxyEndpointAliases>
                  <DbProxyEndpointType>RWSplit</DbProxyEndpointType>
                  <DbProxyReadWriteMode>ReadWrite</DbProxyReadWriteMode>
            </DbProxyEndpointItems>
      </DbProxyEndpointItems>
      <DBProxyConnectStringItems>
            <DBProxyConnectStringItems>
                  <DBProxyConnectString>gos787jog2wk0ye1****-
rw4rm.rwlb.rds.aliyuncs.com</DBProxyConnectString>
                  <DBProxyEndpointId>209090</DBProxyEndpointId>
                  <DBProxyEndpointName>gos787jog2wk0ye1****</DBProxyEndpointName>
                  <DBProxyConnectStringNetWorkType>2</DBProxyConnectStringNetWorkType>
                  <DBProxyConnectStringNetType>InnerString</DBProxyConnectStringNetType>
                  <DBProxyConnectStringPort>3306</DBProxyConnectStringPort>
                  <DBProxyVpcInstanceId>rm-bp145737x5****131161274792****</DBProxyVpcIns
tanceId>
            </DBProxyConnectStringItems>
      </DBProxyConnectStringItems>
      <DBProxyInstanceStatus>Running</DBProxyInstanceStatus>
      <DBProxyInstanceType>2</DBProxyInstanceType>
```

`JSON` format ApsaraDB for RDS

```json
{
    "DBProxyInstanceName": "gos787jog2wk0ye1****",
    "DBProxyInstanceCurrentMinorVersion": "1.13.11",
    "DBProxyServiceStatus": "Startup",
    "DBProxyInstanceNum": 1,
    "DBProxyInstanceLatestMinorVersion": "1.13.12",
    "RequestId": "909A69EE-71C8-4417-A0B9-FF085407E1E3",
    "DbProxyEndpointItems": {
        "DbProxyEndpointItems": [
            {
                "DbProxyEndpointName": "gos787jog2wk0ye1****",
                "DbProxyEndpointAliases": "proxy-test",
                "DbProxyEndpointType": "RWSplit",
                "DbProxyReadWriteMode": "ReadWrite"
            }
```

]

```json
    },
    "DBProxyConnectStringItems": {
        "DBProxyConnectStringItems": [
            {
                "DBProxyConnectString": "gos787jog2wk0ye1****-
rw4rm.rwlb.rds.aliyuncs.com",
                "DBProxyEndpointId": 209090,
                "DBProxyEndpointName": "gos787jog2wk0ye1****",
                "DBProxyConnectStringNetWorkType": 2,
                "DBProxyConnectStringNetType": "InnerString",
                "DBProxyConnectStringPort": "3306",
                "DBProxyVpcInstanceId": "rm-bp145737x5****131161274792****"
            }
```

]

```json
    },
    "DBProxyInstanceStatus": "Running",
    "DBProxyInstanceType": "2"
}
```

#### DescribeDBProxyEndpoint

Queries the dedicated proxy endpoint of an ApsaraDB RDS instance. ApsaraDB RDS provides the dedicated proxy feature to deliver capabilities such as read/write splitting and short-lived connection optimization. Before you call this operation, make sure that the instance runs one of the following database engine versions and RDS editions: MySQL 8.0 on RDS Enterprise Edition (minor version of 20191204 or later) MySQL 8.0 on RDS High-availability Edition (minor version of 20190915 or later) MySQL 5.7 on RDS Enterprise Edition (minor version of 20191128 or later) MySQL 5.7 on RDS High-availability Edition (minor version of 20190925 or later) MySQL 5.6 on RDS High-availability Edition (minor version of 20200229 or later)

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBProx yEndpoint | The operation that you want to perform. Set the value to DescribeDBProxyEndpoint. |
| DBInstanceId | String | Yes | rm- bp1ja4f56s7us** ** | The ID of the instance. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |
| DBProxyEndpoin tId | String | No | keaxncrjluwu0g ue**** | The name of the proxy terminal. |
| DBProxyConnect String | String | No | testproxy****.rw lb.rds.aliyuncs.c om | The proxy endpoint to query. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBProxyConne ctString | String | testproxy****.rwlb. rds.aliyuncs.com | The proxy endpoint queried. |
| DBProxyConne ctStringNetTyp e | String | InnerString | The network type of the proxy endpoint. Valid values: InnerString: internal network OuterString: Internet |
| DBProxyConne ctStringPort | String | 3306 | The port that is used to connect to the proxy endpoint. |
| DBProxyEndpo intId | String | keaxncrjluwu0gue* *** | The ID of the proxy endpoint. You can call this operation to query the ID of a proxy endpoint. |

ApsaraDB for RDS

**Response parameters**

| DBProxyFeatur es | String | TransactionReadSq lRouteOptimizeStat us:1;ConnectionPer sist:0;ReadWriteSpl iting:1 | The configuration of the proxy terminal. The configuration is in the JSON format and contains the following parameters: TransactionReadSqlRouteOptimize Status: the status of the transaction splitting feature. Valid values: 0 and 1. The value 0 indicates that this feature is disabled. The value 1 indicates that this feature is enabled. ConnectionPersist: the status of the connection pool feature. Valid values: 0, 1, and 2. The value 0 indicates that this feature is disabled. The value 1 indicates that the session connection pool feature is enabled. The value 2 indicates that the transaction connection pool feature is enabled. ReadWriteSpliting: the status of the read/write splitting feature. Valid values: 0 and 1. The value 0 indicates that this feature is disabled. The value 1 indicates that this feature is enabled. |
|---|---|---|---|
| ReadOnlyInsta nceDistributio nType | String | Standard | The policy that is used to assign read weights. Valid values: Standard: ApsaraDB RDS automatically assigns read weights to the primary and read-only instances based on the specifications of these instances. Custom: You must manually assign read weights to the primary and read- only instances. |
| ReadOnlyInsta nceMaxDelayT ime | String | 30 | The latency threshold that is allowed for read/write splitting. If the latency on a read-only instance exceeds the specified threshold, ApsaraDB RDS no longer routes read requests to the read-only instance. |

ApsaraDB for RDS

| ReadOnlyInsta nceWeight | String | [{\"Availability\":\" Available\",\"DBInst anceId\":\"rr- bp176984qewd8** **\",\"DBInstanceTy pe\":\"ReadOnly\",\ "Weight\":400}, {\"Availability\":\"A vailable\",\"DBInsta nceId\":\"rm- bp1ja4f56s7us****\ ",\"DBInstanceType \":\"Master\",\"Weig ht\":0}] | The read weights of the primary and read- only instances. The value of this parameter is in the JSON format and contains the following parameters: DBInstanceId: the ID of the instance. DBInstanceType: the role of the instance. Valid values: Master and ReadOnly. Weight: the read weight of the instance. The read weight must increase in increments of 100 and cannot exceed 10000. Note If the primary instance is not attached with read-only instances, this operation returns null for this parameter. |
|---|---|---|---|
| RequestId | String | 847BA085-B377- 4BFA-8267- F82345ECE1D2 | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBProxyEndpoint &DBInstanceId=rm-bp1ja4f56s7us**** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format ApsaraDB for RDS

```json
      <DbProxyEndpointReadWriteMode>ReadWrite</DbProxyEndpointReadWriteMode>
      <ReadOnlyInstanceDistributionType>Standard</ReadOnlyInstanceDistributionType>
      <DBProxyConnectString>testproxy****.rwlb.rds.aliyuncs.com</DBProxyConnectString>
      <RequestId>336E33D5-8C02-4265-9627-704BF9F3954B</RequestId>
      <DBProxyEndpointId>keaxncrjluwu0guehzae</DBProxyEndpointId>
      <DbProxyEndpointAliases>proxyterminal-test</DbProxyEndpointAliases>
<DBProxyFeatures>TransactionReadSqlRouteOptimizeStatus:1;ConnectionPersist:0;ReadWriteSpl ing:1;PinPreparedStmt:0</DBProxyFeatures>
      <ReadOnlyInstanceWeight>[{"Availability":"Available","DBInstanceId":"rr-
bp176984qewd8****","DBInstanceType":"ReadOnly","Weight":400}, {"Availability":"Available","DBInstanceId":"rmbp1ja4f56s7us****","DBInstanceType":"Master","Weight":0}]</ReadOnlyInstanceWeight>
      <ReadOnlyInstanceMaxDelayTime>30</ReadOnlyInstanceMaxDelayTime>
      <DBProxyConnectStringNetType>InnerString</DBProxyConnectStringNetType>
      <EndpointConnectItems>
            <EndpointConnectItems>
                  <DbProxyEndpointNetType>2</DbProxyEndpointNetType>
                  <DbProxyEndpointPort>3306</DbProxyEndpointPort>
<DbProxyEndpointConnectString>testproxy****.rwlb.rds.aliyuncs.com</DbProxyEndpointConnect ring>
            </EndpointConnectItems>
            <EndpointConnectItems>
                  <DbProxyEndpointNetType>0</DbProxyEndpointNetType>
                  <DbProxyEndpointPort>3306</DbProxyEndpointPort>
<DbProxyEndpointConnectString>test****.rwlb.rds.aliyuncs.com</DbProxyEndpointConnectStrin
            </EndpointConnectItems>
      </EndpointConnectItems>
      <DBProxyConnectStringPort>3306</DBProxyConnectStringPort>
```

`JSON` format

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | Endpoint.NotFound | Specified endpoint is not found. | The error message returned because the port used to connect to the dedicated proxy endpoint is not found. |

ApsaraDB for RDS

```json
{
    "DbProxyEndpointReadWriteMode": "ReadWrite",
    "ReadOnlyInstanceDistributionType": "Standard",
    "DBProxyConnectString": "testproxy****.rwlb.rds.aliyuncs.com",
    "RequestId": "336E33D5-8C02-4265-9627-704BF9F3954B",
    "DBProxyEndpointId": "keaxncrjluwu0guehzae",
    "DbProxyEndpointAliases": "proxyterminal-test",
    "DBProxyFeatures":
"TransactionReadSqlRouteOptimizeStatus:1;ConnectionPersist:0;ReadWriteSpliting:1;PinPrepa dStmt:0",
    "ReadOnlyInstanceWeight": "[{\"Availability\":\"Available\",\"DBInstanceId\":\"rr-b
p176984qewd8****\",\"DBInstanceType\":\"ReadOnly\",\"Weight\":400}, {\"Availability\":\"Available\",\"DBInstanceId\":\"rmbp1ja4f56s7us****\",\"DBInstanceType\":\"Master\",\"Weight\":0}]",
    "ReadOnlyInstanceMaxDelayTime": "30",
    "DBProxyConnectStringNetType": "InnerString",
    "EndpointConnectItems": {
        "EndpointConnectItems": [
            {
                "DbProxyEndpointNetType": "2",
                "DbProxyEndpointPort": "3306",
                "DbProxyEndpointConnectString": "testproxy****.rwlb.rds.aliyuncs.com"
            },
            {
                "DbProxyEndpointNetType": "0",
                "DbProxyEndpointPort": "3306",
                "DbProxyEndpointConnectString": "test****.rwlb.rds.aliyuncs.com"
            }
```

]

```json
    },
    "DBProxyConnectStringPort": "3306"
}
```

#### DescribeDBProxyPerformance

Queries the performance data of the dedicated proxy for an ApsaraDB RDS instance. ApsaraDB RDS provides the dedicated proxy feature to deliver capabilities such as read/write splitting and short-lived connection optimization. Before you call this operation, make sure that the following requirements are met: The dedicated proxy feature is enabled on the instance.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBProx yPerformance | The operation that you want to perform. Set the value to DescribeDBProxyPerformance. |
| DBInstanceId | String | Yes | rm-t4n3axxxxx | The ID of the instance. |
| EndTime | String | Yes | 2019-09- 21T18:00:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| MetricsName | String | Yes | Maxscale CpuUs _ age | The performance metrics to query. These performance metrics are determined by the DBProxyInstanceType parameter. If you set the DBProxyInstanceType parameter to DedicatedProxy, you can query only the Maxscale CpuUsage _ performance metric, which indicates CPU utilization. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |
| StartTime | String | Yes | 2019-09- 19T01:00:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| DBProxyInstance Type | String | No | DedicatedProxy | The type of the proxy enabled on the instance. Set the value to DedicatedProxy. |

ApsaraDB for RDS The instance runs one of the following database engine versions and RDS editions: MySQL 8.0 on RDS Enterprise Edition (minor version of 20191204 or later) MySQL 8.0 on RDS High-availability Edition (minor version of 20190915 or later) MySQL 5.7 on RDS Enterprise Edition (minor version of 20191128 or later) MySQL 5.7 on RDS High-availability Edition (minor version of 20190925 or later) MySQL 5.6 on RDS High-availability Edition (minor version of 20200229 or later)

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | lsmexxxxxxx | The ID of the instance. |
| EndTime | String | 2019-09- 21T18:00:00Z | The end time of the query. |
| PerformanceK eys | Array of PerformanceK ey |  | Details of the performance data. |
| PerformanceK ey |  |  |  |
| Key | String | cpu ratio _ | The name of the performance metric. |
| ValueFormat | String | docker container c _ _ pu | The format that the value of the performance metric follows. |
| Values | Array of PerformanceV alue |  | An array that consists of performance metric values in the following format: {value1, value2, ...}. |
| PerformanceV alue |  |  |  |
| Date | String | 2019-10- 10T09:00:00Z | The time when the performance metric value is recorded. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Value | String | 2.83 | The value of the performance metric. |
| RequestId | String | DD31056F-A0CE- 41D7-AD39- 689B6ABAE982 | The ID of the request. |
| StartTime | String | 2019-09- 19T01:00:00Z | The start time of the query. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBProxyPerformance &RegionId=cn-hangzhou &DBInstanceId=rm-t4n3axxxxx &MetricsName=Maxscale_CpuUsage &StartTime=2019-09-19T01:00:00Z &EndTime=2019-09-21T18:00:00Z &<Common request parameters>
```

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|

ApsaraDB for RDS Sample success responses `XML` format

```xml
  <DBInstanceId>lsmexxxxxxx</DBInstanceId>
  <RequestId>DD31056F-A0CE-41D7-AD39-689B6ABAE982</RequestId>
  <PerformanceKeys>
        <PerformanceKey>
              <Values>
                    <PerformanceValue>
                          <Value>2.83</Value>
                          <Date>2019-10-10T09:00:00Z</Date>
                    </PerformanceValue>
              </Values>
              <Key>cpu_ratio</Key>
              <ValueFormat>docker_container_cpu</ValueFormat>
        </PerformanceKey>
  </PerformanceKeys>
  <EndTime>2019-10-10T09:39:28Z</EndTime>
  <StartTime>2019-10-01T09:39:28Z</StartTime>
```

`JSON` format

```json
{
    "DBInstanceId": "lsmexxxxxxx",
    "RequestId": "DD31056F-A0CE-41D7-AD39-689B6ABAE982",
    "PerformanceKeys": {
        "PerformanceKey": [
            {
                "Values": {
                    "PerformanceValue": [
                        {
                            "Value": "2.83",
                            "Date": "2019-10-10T09:00:00Z"
                        }
```

]

```json
                },
                "Key": "cpu_ratio",
                "ValueFormat": "docker_container_cpu"
            }
```

]

```json
    },
    "EndTime": "2019-10-10T09:39:28Z",
    "StartTime": "2019-10-01T09:39:28Z"
}
```

| 404 | Endpoint.NotFound | Specified endpoint is not found. | The error message returned because the port used to connect to the dedicated proxy endpoint is not found. |
|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBProxy | The operation that you want to perform. Set the value to ModifyDBProxy. |
| ConfigDBProxyS ervice | String | Yes | Startup | Specifies whether to enable or disable the dedicated proxy feature. Valid values: Startup: enables the dedicated proxy feature. Shutdown: disables the dedicated proxy feature. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| DBProxyInstance Num | String | No | 1 | The number of enabled proxy instances. Valid values: 1 to 60. Default value: 1. Note The capability to process requests increases in proportion with the number of enabled proxy instances. You can specify an appropriate number of proxy instances based on the monitoring information of database loads. |

ApsaraDB for RDS

#### ModifyDBProxy

Enables or disables the dedicated proxy feature for an ApsaraDB RDS instance. ApsaraDB RDS provides the dedicated proxy feature to deliver capabilities such as read/write splitting and short-lived connection optimization. Before you call this operation, make sure that the instance runs one of the following database engine versions and RDS editions: MySQL 8.0 on RDS Enterprise Edition (minor version of 20191204 or later) MySQL 8.0 on RDS High-availability Edition (minor version of 20190915 or later) MySQL 5.7 on RDS Enterprise Edition (minor version of 20191128 or later) MySQL 5.7 on RDS High-availability Edition (minor version of 20190925 or later) MySQL 5.6 on RDS High-availability Edition (minor version of 20200229 or later)

**Request parameters**

| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |
|---|---|---|---|---|
| InstanceNetwork Type | String | No | VPC | The network type of the instance. Set the value to VPC. |
| VPCId | String | No | vpc- xxxxxxxxxxxx | The ID of the VPC in which the instance resides. |
| VSwitchId | String | No | CloudInstanceId | The ID of the vSwitch to which the instance is connected. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FC452BB1-EED8- 4278-95C7- 0324B3710DF1 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
&DBInstanceId=rm-uf6wjk5xxxxxxx &ConfigDBProxyService=Startup &<Common request parameters>
```

Sample success responses `XML` format

```xml
    <RequestId>FC452BB1-EED8-4278-95C7-0324B3710DF1</RequestId>
```

`JSON` format

```json
{
    "RequestId": "FC452BB1-EED8-4278-95C7-0324B3710DF1"
}
```

#### ModifyDBProxyEndpoint

Modifies the proxy terminal settings of an ApsaraDB RDS instance. ApsaraDB RDS provides the dedicated proxy feature to deliver capabilities such as read/write splitting and connection pooling.

| Parameter | Type | Requir ed |  | Example | Description |  |  |
|---|---|---|---|---|---|---|---|
| Action | String | Yes |  | ModifyDBProxyE ndpoint | The operation that you want to perform. Set the value to ModifyDBProxyEndpoint. |  |  |
| DBInstanceId | String | Yes |  | rm- bp145737x5bi6* *** | The ID of the instance. |  |  |
| DBProxyEndpoin tId | String | Yes |  | gos787jog2wk0y **** | The ID of the proxy endpoint. You can call the DescribeDBProxyEndpoint operation to query the proxy endpoints of a proxy terminal. Note This parameter is required if you set the DbEndpointOperator parameter to Delete or Modify. |  |  |
| ConfigDBProxyF eatures | String | No |  |  | The features that you want to enable for the proxy endpoint. If you specify more than one feature, separate them with semicolons (;). Format: Feature 1:Status;Feature 2:Status;... Valid feature values: ReadWriteSpliting: read/write splitting ConnectionPersist: connection pooling TransactionReadSqlRouteOpti mizeStatus: transaction splitting Valid status values: 1: enabled 0: disabled |  |  |
|  |  |  |  |  |  | Feature 1:Status;Feature |  |
|  |  |  |  |  | 2:Status;... |  |  |
|  |  |  |  | ReadWriteSplitin g:1;ConnectionP ersist:0; |  |  |  |

ApsaraDB for RDS Before you call this operation, make sure that the following requirements are met: The dedicated proxy feature is enabled on the instance. The instance runs one of the following database engine versions and RDS editions: MySQL 8.0 on RDS Enterprise Edition (minor version of 20191204 or later) MySQL 8.0 on RDS High-availability Edition (minor version of 20190915 or later) MySQL 5.7 on RDS Enterprise Edition (minor version of 20191128 or later) MySQL 5.7 on RDS High-availability Edition (minor version of 20190925 or later) MySQL 5.6 on RDS High-availability Edition (minor version of 20200229 or later)

**Request parameters**

| RegionId |  | String | No |  | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |  |  |
|---|---|---|---|---|---|---|---|---|
| ReadOnlyInstanc eMaxDelayTime |  | String | No |  | 30 | The latency threshold that is allowed for read/write splitting. If the latency on a read-only instance exceeds the specified threshold, ApsaraDB RDS no longer routes read requests to the read-only instance. If you do not specify this parameter, the original value of this parameter is retained. Valid values: 30 to 3600. Default value: 30. Note You must specify this parameter only when the read/write splitting feature is enabled. |  |  |
| ReadOnlyInstanc eDistributionTyp e |  | String | No |  | Standard | The policy that is used to assign read weights. Valid values: Standard: ApsaraDB RDS automatically assigns read weights to the primary and read-only instances based on the specifications of these instances. Custom: You must manually assign read weights to the primary and read-only instances. Note You must specify this parameter only when the read/write splitting feature is enabled. |  |  |
| ReadOnlyInstanc eWeight |  | String | No |  | {"rm- | The read weights assigned to the primary instance and its read-only instances. Read weights increase in increments of 100 and the maximum read weight is 10000. Format: {"Instance ID 1":"Read |  |  |
|  |  |  |  |  |  |  | {"Instance ID 1":"Read |  |
|  |  |  |  |  | uf6wjk5xxxx":"5 00","rr- | weight","Instance ID 2":"Read |  |  |
|  | Weight |  |  |  |  |  |  |  |
|  |  |  |  |  | tfhfgk5xxx":"200 | weight"...} |  |  |
|  |  |  |  |  | "...} |  |  |  |

| Parameter | Type | Example | Description |
|---|---|---|---|

ApsaraDB for RDS

**Response parameters**

| RequestId | String | 6B50D92C-1960- 4D4F-A290- AFADD6B1A5C8 | The ID of the request. |
|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBProxyEndpoint &DBInstanceId=rm-bp145737x5bi6**** &DBProxyEndpointId=gos787jog2wk0y**** &ConfigDBProxyFeatures=ReadWriteSpliting:1;ConnectionPersist:1; &ReadOnlyInstanceMaxDelayTime=30 &ReadOnlyInstanceDistributionType=Standard &<Common request parameters>
```

Sample success responses `XML` format

```xml
    <RequestId>6B50D92C-1960-4D4F-A290-AFADD6B1A5C8</RequestId>
```

`JSON` format

```json
{
    "RequestId": "6B50D92C-1960-4D4F-A290-AFADD6B1A5C8"
}
```

#### ModifyDBProxyInstance

Modifies the dedicated proxy settings of an ApsaraDB RDS instance. ApsaraDB RDS provides the dedicated proxy feature to deliver capabilities such as read/write splitting and short-lived connection optimization. Before you call this operation, make sure that the following requirements are met: The dedicated proxy feature is enabled on the instance. The instance runs one of the following database engine versions and RDS editions: MySQL 8.0 on RDS Enterprise Edition (minor version of 20191204 or later) MySQL 8.0 on RDS High-availability Edition (minor version of 20190915 or later) MySQL 5.7 on RDS Enterprise Edition (minor version of 20191128 or later) MySQL 5.7 on RDS High-availability Edition (minor version of 20190925 or later) MySQL 5.6 on RDS High-availability Edition (minor version of 20200229 or later)

**Request parameters**

| Action | String | Yes | ModifyDBProxyI nstance | The operation that you want to perform. Set the value to ModifyDBProxyInstance. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm-t4n3axxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| DBProxyInstance Num | String | Yes | 2 | The number of proxy instances. A value of 0 indicates that the dedicated proxy feature is disabled for the instance. Valid values: 0 to 60. Note The capability to process requests increases in proportion with the number of enabled proxy instances. You can specify an appropriate number of proxy instances based on the monitoring information of database loads. |
| DBProxyInstance Type | String | Yes | DedicatedProxy | The type of the proxy enabled on the instance. Set the value to DedicatedProxy. |
| EffectiveTime | String | No | MaintainTime | The time when you want the new settings to take effect. Valid values: Immediate: The new settings take effect immediately. MaintainTime: The new settings take effect within the maintenance window. SpecificTime: The new settings take effect at the specified point in time. Default value: MaintainTime. |
| EffectiveSpecific Time | String | No | 2019-07- 10T13:15:12Z | The point in time when the new settings take effect. Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. Note This parameter is required when the EffectiveTime parameter is set to SpecificTime. |

ApsaraDB for RDS

| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65C55572-530E- 4A53-BE03- 1D08CAF0F046 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBProxyInstance &DBInstanceId=rm-t4n3axxxxx &DBProxyInstanceType=DedicatedProxy &DBProxyInstanceNum=2 &EffectiveTime=Immediate &<Common request parameters>
```

Sample success responses `XML` format

```xml
    <RequestId>65C55572-530E-4A53-BE03-1D08CAF0F046</RequestId>
```

`JSON` format

```json
{
    "RequestId": "65C55572-530E-4A53-BE03-1D08CAF0F046"
}
```

#### ModifyReadWriteSplittingConnection

Modifies the latency threshold that is allowed for read/write splitting and the read weights of a primary ApsaraDB RDS instance and its read-only instances. Before you call this operation, make sure that the following requirements are met: The shared proxy feature is enabled for the primary instance. The read/write splitting feature is enabled for the primary instance. The primary instance runs one of the following database engine versions and RDS editions: MySQL 5.7 on RDS High-availability Edition (with local SSDs) MySQL 5.6 SQL Server 2017 EE

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyReadWrit eSplittingConne ction | The operation that you want to perform. Set the value to ModifyReadWriteSplittingConnec tion. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the primary instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| ConnectionStrin gPrefix | String | No | rm- m5xxxxxxxxrw. mysql.rds.aliyun cs.com | The prefix of the read/write splitting endpoint. The prefix must be unique. It can be up to 30 characters in length and can contain lowercase letters and hyphens (-). It must start with a lowercase letter. Note The default prefix consists of the name of the primary instance followed by rw. |
| Port | String | No | 3306 | The port that is connected to the read/write splitting endpoint. |
| MaxDelayTime | String | No | 12 | The latency threshold that is allowed for read/write splitting. Unit: seconds. If the latency on a read- only instance exceeds the specified threshold, ApsaraDB RDS no longer routes read requests to the read-only instance. If you do not specify this parameter, the default latency threshold is used. Note The MaxDelayTime parameter is not supported for instances that run SQL Server 2017 on RDS Cluster Edition. You must specify at least one of MaxDelayTime and DistributionType. |

ApsaraDB for RDS

**Request parameters**

| DistributionType | String | No | Standard | The method that is used to assign read weights. Valid values: Standard: ApsaraDB RDS automatically assigns read weights to the primary and read-only instances based on the specifications of these instances. Custom: You must manually assign read weights to the primary and read-only instances. Note You must specify at least one of MaxDelayTime and DistributionType. |
|---|---|---|---|---|
| Weight | String | No | null | The read weights of the primary instance and its read-only instances. A read weight must be a multiple of 100 and cannot exceed 10000. Format: {"Instanceid1":"Weight","Instanceid2 ":"Weight"...}. Note This parameter is required if you set the DistributionType parameter to Custom. This parameter is invalid if you set the DistributionType parameter to Standard. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5A77D650-27A1- 4E08-AD9E- 59008EDB6927 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyReadWriteSplittingConnection &DistributionType=Standard &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleaseReadWri teSplittingConne ction | The operation that you want to perform. Set the value to ReleaseReadWriteSplittingConne ction. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the primary instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5A77D650-27A1- 4E08-AD9E- 59008EDB6927 | The ID of the request. |

ApsaraDB for RDS

```xml
<ModifyReadWriteSplittingConnectionResponse>
      <RequestID>5A77D650-27A1-4E08-AD9E-59008EDB6927</RequestID>
</ModifyReadWriteSplittingConnectionResponse>
```

`JSON` format

```json
{
    "RequestID":"5A77D650-27A1-4E08-AD9E-59008EDB6927"
  }
```

#### ReleaseReadWriteSplittingConnection

Releases the read/write splitting endpoint of a primary ApsaraDB RDS instance. Before you call this operation, make sure that the following requirements are met: The shared proxy feature is enabled for the primary instance. The read/write splitting feature is enabled for the primary instance. The primary instance runs one of the following database engine versions and RDS editions: MySQL 5.7 on RDS High-availability Edition (with local SSDs) MySQL 5.6 SQL Server 2017 EE

**Request parameters**

**Response parameters**

**Examples**

Sample requests

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceHAConfig | The operation that you want to perform. Set the value to DescribeDBInstanceHAConfig. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxx | The ID of the instance. |

ApsaraDB for RDS

```
http(s)://rds.example.com/?Action=ReleaseReadWriteSplittingConnection &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ReleaseReadWriteSplittingConnectionResponse>
      <RequestID>5A77D650-27A1-4E08-AD9E-59008EDB6927</RequestID>
</ReleaseReadWriteSplittingConnectionResponse>
```

`JSON` format

```json
{
    "RequestID":"5A77D650-27A1-4E08-AD9E-59008EDB6927"
  }
```

### Primary/secondary high

**availability and data replication**

#### DescribeDBInstanceHAConfig

Queries the high availability mode and data replication mode of an ApsaraDB RDS instance.

**Request parameters**

**Response parameters**

| HAMode | String | RPO | The high availability mode of the instance. Valid values: RPO: Data consistency is preferred. The instance ensures data reliability to minimize data loss. If you have high requirements on data consistency, select this mode. RTO: Service availability is preferred. The instance restores the database service at the earliest opportunity to ensure service availability. If you have high requirements on service availability, select this mode. Note This parameter is returned only for instances that run MySQL. |
|---|---|---|---|
| SyncMode | String | Sync | The data replication mode of the instance. Valid values: Sync Semi-sync Async Note This parameter is returned only for instances that run MySQL. |
| HostInstanceIn fos | Array of NodeInfo |  | Details of the primary and secondary instances. |
| NodeInfo |  |  |  |
| NodeId | String | 3397027 | The ID of the instance. |
| NodeType | String | Master | The role of the instance. Valid values: Master: primary instance Slave: secondary instance |
| RegionId | String | cn-hangzhou | The region ID of the instance. |
| ZoneId | String | cn-hangzhou-b | The zone ID of the instance. |

ApsaraDB for RDS

| SyncStatus | String | NotAvailable | The synchronization status of the instance. Valid values: NotAvailable: The synchronization fails. This means that faults occur. Syncing: The synchronization is in process. In this case, a primary/secondary switchover may cause data loss. Synchronized: The synchronization is complete. NotSupport: The database engine or version does not involve the synchronization between the primary and secondary instances. |
|---|---|---|---|
| LogSyncTime | String | 2018-05- 05T15:15:00Z | The time when the secondary instance received logs from the primary instance. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DataSyncTime | String | 2018-05- 05T15:15:00Z | The time when the data synchronization between the primary and secondary instances was complete. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |
| SwitchMode | String | None | An invalid parameter. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceHAConfig &DBInstanceId=rm-uf6wjk5xxxxxx &<Common request parameters>
```

Sample success responses `XML` format ApsaraDB for RDS

```xml
  <RequestId>103D4ACC-F2F9-4A7E-9ACC-14B0A25613E0</RequestId>
  <DBInstanceId>rm-uf6wjk5xxxxxx</DBInstanceId>
  <HAMode>RPO</HAMode>
  <HostInstanceInfos>
        <NodeInfo>
              <DataSyncTime></DataSyncTime>
              <ZoneId>cn-hangzhou-h</ZoneId>
              <LogSyncTime></LogSyncTime>
              <NodeType>Slave</NodeType>
              <NodeId>13567431</NodeId>
              <SyncStatus>NotSupport</SyncStatus>
              <RegionId>cn-hangzhou</RegionId>
        </NodeInfo>
        <NodeInfo>
              <DataSyncTime></DataSyncTime>
              <ZoneId>cn-hangzhou-h</ZoneId>
              <LogSyncTime></LogSyncTime>
              <NodeType>Master</NodeType>
              <NodeId>14565107</NodeId>
              <SyncStatus>NotSupport</SyncStatus>
              <RegionId>cn-hangzhou</RegionId>
        </NodeInfo>
  </HostInstanceInfos>
  <SyncMode>Semi-sync</SyncMode>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eHAConfig | The operation that you want to perform. Set the value to ModifyDBInstanceHAConfig. |
| DbInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

ApsaraDB for RDS

```json
{
    "RequestId": "103D4ACC-F2F9-4A7E-9ACC-14B0A25613E0",
    "DBInstanceId": "rm-uf6wjk5xxxxxx",
    "HAMode": "RPO",
    "HostInstanceInfos": {
        "NodeInfo": [
            {
                "DataSyncTime": "",
                "ZoneId": "cn-hangzhou-h",
                "LogSyncTime": "",
                "NodeType": "Slave",
                "NodeId": "13567431",
                "SyncStatus": "NotSupport",
                "RegionId": "cn-hangzhou"
            },
            {
                "DataSyncTime": "",
                "ZoneId": "cn-hangzhou-h",
                "LogSyncTime": "",
                "NodeType": "Master",
                "NodeId": "14565107",
                "SyncStatus": "NotSupport",
                "RegionId": "cn-hangzhou"
            }
```

]

```json
    },
    "SyncMode": "Semi-sync"
}
```

#### ModifyDBInstanceHAConfig

Changes the high availability mode and data replication mode of an ApsaraDB RDS instance.

**Request parameters**

| SyncMode | String | No | Sync | The data replication mode of the instance. Valid values: Sync Semi-sync Async Note This parameter is not supported for instances that run SQL Server 2017 EE. |
|---|---|---|---|---|
| HAMode | String | No | RPO | The high availability mode of the instance. Valid values: RPO: Data consistency is preferred. The instance ensures data reliability to minimize data loss. If you have high requirements on data consistency, select this mode. RTO: Service availability is preferred. The instance restores the database service at the earliest opportunity to ensure service availability. If you have high requirements on service availability, select this mode. |
| SwitchMode | String | No | 0 | The time when primary/secondary switchovers are performed. Valid values: 0: Primary/secondary switchovers are performed immediately. 1: Primary/secondary switchovers are performed within the maintenance window. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D4D4BE8A-DD46- 440A-BFCD- EE31DA81C9DD | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceHAConfig &DbInstanceId=rm-uf6wjk5xxxxxxx &HAMode=RPO &SyncMode=Sync &<Common request parameters>
```

Sample success responses

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceSwitchLog | The operation that you want to perform. Set the value to DescribeDBInstanceSwitchLog. |
| EndTime | String | Yes | 2018-06- 11T15:00Z | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. Example: 2011- 06-11T16:00Z. The end time must be later than the start time. |
| StartTime | String | Yes | 2014-06- 11T15:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. Example: 2011- 06-11T15:00Z. |
| DBInstanceId | String | No | rdsaiiabnaiiabn | The ID of the instance. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. Valid values: 1 to 30. Default value: 1. |

ApsaraDB for RDS `XML` format

```xml
      <RequestId>D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD</RequestId>
```

`JSON` format

```json
{
    "RequestId":"D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD"
}
```

#### DescribeDBInstanceSwitchLog

Queries the primary/secondary switchover logs of an ApsaraDB RDS instance. This operation is supported for instances that run MySQL, SQL Server, PostgreSQL, or PolarDB.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceNa me | String | rdsaiiabnaiiabn | The name of the instance. |
| Items | Array of Item |  | Details of primary/secondary switchover logs. |
| Item |  |  |  |
| AffectedSessio ns | String | None | The number of affected sessions during the switchover. |
| HAStatus | String | None | None |
| SwitchCauseC ode | String | None | The cause for the switchover. |
| SwitchFinishTi me | String | None | The end time of the switchover. |
| SwitchId | String | None | The ID of the switchover task. |
| SwitchStartTi me | String | None | The start time of the switchover. |
| TotalSessions | String | None | The total number of sessions during the switchover. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 60 | The number of entries returned per page. |
| RequestId | String | D1CA494F-CC13- 4EB6-8C4D- 5352EE4045BD | The ID of the request. |
| TotalRecordCo unt | Integer | 5 | The total number of entries returned. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceSwitchLog &EndTime=2018-06-11T15:00Z &StartTime=2014-06-11T15:00Z &<Common request parameters>
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHASwit chConfig | The operation that you want to perform. Set the value to DescribeHASwitchConfig. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx xxx | The ID of the instance. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |

ApsaraDB for RDS Sample success responses `XML` format

```xml
      <Items></Items>
      <PageNumber>1</PageNumber>
      <TotalRecordCount>5</TotalRecordCount>
      <RequestId>D1CA494F-CC13-4EB6-8C4D-5352EE4045BD</RequestId>
      <PageRecordCount>60</PageRecordCount>
      <DBInstanceName>rm-m5el220b25im05g7g</DBInstanceName>
```

`JSON` format

```json
{
    "Items": {},
    "PageNumber": 1,
    "TotalRecordCount": 5,
    "RequestId": "D1CA494F-CC13-4EB6-8C4D-5352EE4045BD",
    "PageRecordCount": 60,
    "DBInstanceName": "rm-m5el220b25im05g7g"
}
```

#### DescribeHASwitchConfig

Queries the automatic primary/secondary switchover settings of an ApsaraDB RDS instance. After the switchover, the original primary instance becomes the secondary instance. This operation is supported only for instances that run the High-availability Edition, Enterprise Edition, or Cluster Edition.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| HAConfig | String | Manual | The primary/secondary switchover mode of the instance. Valid values: Auto: The automatic primary/secondary switchover feature is enabled. The system automatically switches over workloads from the primary to secondary instances in the event of a fault. Manual: You must manually perform a primary/secondary switchover in the event of a fault. |
| ManualHATim e | String | 2019-08- 29T15:00:00Z | The time when the automatic primary/secondary switchover feature is disabled. |
| RequestId | String | 4FDF4B79-2741- 4C5F-8C76- 4B953FC5C2B1 | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeHASwitchConfig &RegionId=cn-hangzhou &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <ManualHATime>2019-08-29T15:00:00Z</ManualHATime>
   <RequestId>4FDF4B79-2741-4C5F-8C76-4B953FC5C2B1</RequestId>
   <HAConfig>Manual</HAConfig>
```

`JSON` format

```json
{
    "ManualHATime": "2019-08-29T15:00:00Z",
    "RequestId": "4FDF4B79-2741-4C5F-8C76-4B953FC5C2B1",
    "HAConfig": "Manual"
}
```

Switches workloads between a primary ApsaraDB RDS instance and its secondary instance.

#### SwitchDBInstanceHA

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SwitchDBInstanc eHA | The operation that you want to perform. Set the value to SwitchDBInstanceHA. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx xxx | The ID of the primary instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| NodeId | String | Yes | 349054 | The unique identifier of the secondary instance. You can call the DescribeDBInstanceHAConfig operation to query the No. of the secondary instance. |
| Operation | String | No | None | An invalid parameter. |
| Force | String | No | No | Specifies whether to enable forced switchover. Valid values: Yes No Default value: No. |
| EffectiveTime | String | No | Immediate | The time when you want the switchover to take effect. Valid values: Immediate: The switchover takes effect immediately. MaintainTime: The switchover takes effect within the maintenance window. Default value: Immediate. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | The ID of the request. |

ApsaraDB for RDS This operation switches workloads between the primary and secondary ApsaraDB RDS instances that do not run the Basic Edition. After the switchover, the secondary instance takes over as the primary instance.

**Request parameters**

**Response parameters**

**Examples**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyHASwitch Config | The operation that you want to perform. Set the value to ModifyHASwitchConfig. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx xxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |

ApsaraDB for RDS Sample requests

```
http(s)://rds.example.com/?Action=SwitchDBInstanceHA &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &NodeId=349054 &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId>
```

`JSON` format

```json
{
    "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC"
  }
```

#### ModifyHASwitchConfig

Enables or disables the automatic primary/secondary switchover feature for an ApsaraDB RDS instance. After the switchover, the original primary instance becomes the secondary instance.

**Note**

This operation is supported only for instances that run MySQL on RDS Highavailability Edition.

**Request parameters**

| HAConfig | String | No | Manual | The primary/secondary switchover mode of the instance. Valid values: Auto: The automatic primary/secondary switchover feature is enabled. The system automatically switches over workloads from the primary to secondary instances in the event of a fault. Manual: You must manually perform a primary/secondary switchover in the event of a fault. Default value: Auto. Note If you set this parameter to Manual, you must specify the ManualHATime parameter. |
|---|---|---|---|---|
| ManualHATime | String | No | 2019-08- 29T15:00:00Z | The time to disable the automatic primary/secondary switchover feature. The time can range from the current time to 23:59:59 seven days later. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. Note This parameter is valid only when the HAConfig parameter is set to Manual. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B6AE1448-D846- 4831-B1C7- CFF3E99D5470 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyHASwitchConfig &RegionId=cn-hangzhou &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &HAConfig=Manual &ManualHATime=2019-08-28T15:00:00 &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceIPArrayList | The operation that you want to perform. Set the value to DescribeDBInstanceIPArrayList. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| WhitelistNetwork Type | String | No | VPC | The network type of the IP address whitelist. Valid values: Classic: classic network in enhanced whitelist mode VPC: virtual private cloud (VPC) in enhanced whitelist mode MIX: standard whitelist mode By default, this operation returns IP address whitelists of all network types. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of DBInstanceIPA rray |  | Details of the IP address whitelist. |
| DBInstanceIPA rray |  |  |  |

ApsaraDB for RDS

```xml
   <RequestId>B6AE1448-D846-4831-B1C7-CFF3E99D5470</RequestId>
```

`JSON` format

```json
{
    "RequestId": "B6AE1448-D846-4831-B1C7-CFF3E99D5470"
}
```

### Security and encryption

#### DescribeDBInstanceIPArrayList

Queries the IP address whitelists of an ApsaraDB RDS instance.

**Request parameters**

**Response parameters**

| DBInstanceIPA rrayName | String | rds default _ | The name of the IP address whitelist. |
|---|---|---|---|
| DBInstanceIPA rrayAttribute | String | hidden | The attribute of the IP address whitelist. By default, this parameter is empty. Note The IP address whitelists that have the hidden attribute are not displayed in the ApsaraDB RDS console. These IP address whitelists are used to access Alibaba Cloud services such as Data Transmission Service (DTS). |
| SecurityIPList | String | 192.168.1.0/24 | The IP addresses in the IP address whitelist. |
| SecurityIPType | String | IPv4 | The type of the IP address. Valid values: IPv4 IPv6 |
| RequestId | String | E2B6AF71-DC32- 4055-B477- 43B348798D10 | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceIPArrayList &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <Items>
            <DBInstanceIPArray>
                  <DBInstanceIPArrayName>rds_default</DBInstanceIPArrayName>
                  <DBInstanceIPArrayAttribute></DBInstanceIPArrayAttribute>
                  <WhitelistNetworkType>VPC</WhitelistNetworkType>
                  <SecurityIPList>192.168.1.0/24</SecurityIPList>
                  <SecurityIPType>IPv4</SecurityIPType>
            </DBInstanceIPArray>
      </Items>
      <RequestId>E2B6AF71-DC32-4055-B477-43B348798D10</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySecurityIp s | The operation that you want to perform. Set the value to ModifySecurityIps. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

ApsaraDB for RDS

```json
{
    "Items": {
        "DBInstanceIPArray": [
            {
                "DBInstanceIPArrayName": "rds_default",
                "DBInstanceIPArrayAttribute": "",
                "WhitelistNetworkType": "VPC",
                "SecurityIPList": "192.168.1.0/24",
                "SecurityIPType": "IPv4"
            }
```

]

```json
    },
    "RequestId": "E2B6AF71-DC32-4055-B477-43B348798D10"
}
```

#### ModifySecurityIps

Modifies an IP address whitelist of an ApsaraDB RDS instance. This operation allows you to add more IP addresses to a whitelist to allow their access to the instance.

**Note**

Before you call this operation, make sure that the instance is in the running state.

**Request parameters**

| SecurityIps | String | Yes | 10.23.12.24 | The IP addresses that you want to add to the IP address whitelist. Separate multiple IP addresses with commas (,). Each IP address in the IP address whitelist must be unique. Both IPv4 and IPv6 IP addresses are allowed. They support the following formats: IP addresses, such as 10.23.12.24. Classless Inter-Domain Routing (CIDR) blocks, such as 10.23.12.0/24. In this case, /24 indicates that the prefix of each IP address is 24-bit long. You can replace 24 with a value within the range of 1 to 32. Note A maximum of 1,000 IP addresses and CIDR blocks can be configured for each instance. If you want to add a large number of IP addresses, we recommend that you merge them into CIDR blocks, such as 10.23.12.0/24. |
|---|---|---|---|---|
| DBInstanceIPArr ayName | String | No | test | The name of the IP address whitelist that you want to modify. Default value: Default. Note A maximum of 200 IP address whitelists can be configured for each instance. |
| DBInstanceIPArr ayAttribute | String | No | hidden | The attribute of the IP address whitelist. By default, this parameter is empty. Note The IP address whitelists that have the hidden attribute are not displayed in the ApsaraDB RDS console. These IP address whitelists are used to access Alibaba Cloud services such as Data Transmission Service (DTS). |
| SecurityIPType | String | No | IPv4 | The type of the IP address. |
| SecurityGroupId | String | No | sg-xxxxxxx | The ID of the security group. |

ApsaraDB for RDS

| ModifyMode | String | No | Cover | The method that is used to modify the IP address whitelist. Valid values: Cover: uses the SecurityIps value to overwrite the existing entries in the IP address whitelist. Append: adds the IP addresses and CIDR blocks that are specified in the SecurityIps parameter to the IP address whitelist. Delete: deletes IP addresses and CIDR blocks that are specified in the SecurityIps parameter from the IP address whitelist. You must retain at least one IP address or CIDR block. Default value: Cover. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |
| TaskId | String | 115855279 | The ID of the task. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifySecurityIps &DBInstanceId=rm-uf6wjk5xxxxxxx &SecurityIps=10.23.12.24 &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId> 1AD222E9-E606-4A42-BF6D-8A4442913CEF</RequestId>
      <TaskId>115855279</TaskId>
```

`JSON` format

```json
{
    "RequestId": " 1AD222E9-E606-4A42-BF6D-8A4442913CEF",
    "TaskId": 115855279
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceEncryptionKe y | The operation that you want to perform. Set the value to DescribeDBInstanceEncryptionKe y. |
| DBInstanceId | String | No | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| EncryptionKey | String | No | 749c1df7-xxxx- xxxx-xxxx- xxxxxxxxxxxx | The ID of the custom key that is used for disk encryption. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Creator | String | 1443*****9604 | The creator of the key. |
| DeleteDate | String | 2022-05- 08T08:14:16Z | The scheduled time at which the key is deleted. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Description | String | Description of the key | The description of the key. |
| EncryptionKey | String | 5306d1b6-7fd3- 42d9-9511- xxxxxxx | The ID of the key. |
| EncryptionKey Status | String | Enabled | The status of the key. Valid values: Enabled Disabled |
| KeyUsage | String | ENCRYPT/DECRYPT | The purpose of the key. |

ApsaraDB for RDS

#### DescribeDBInstanceEncryptionKey

Queries the status of disk encryption and the details of keys on an ApsaraDB RDS instance. This operation is supported for instances that run MySQL, SQL Server, or PostgreSQL.

**Request parameters**

**Response parameters**

| MaterialExpire Time | String | 2021-10- 18T08:14:16Z | The time at which the key expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
|---|---|---|---|
| Origin | String | Aliyun KMS _ | The source of the key. |
| RequestId | String | 3BC2768E-DEDA- 40FC-BBE9- 6B884F3626AF | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceEncryptionKey &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceEncryptionKeyResponse>
      <Origin>Aliyun_KMS</Origin>
      <Description>Description of the key</Description>
      <EncryptionKeyStatus>Enabled</EncryptionKeyStatus>
      <RequestId>3BC2768E-DEDA-40FC-BBE9-6B884F3626AF</RequestId>
      <MaterialExpireTime>2021-10-18T08:14:16Z</MaterialExpireTime>
      <KeyUsage>ENCRYPT/DECRYPT</KeyUsage>
      <EncryptionKey>5306d1b6-7fd3-42d9-9511-xxxxxxx</EncryptionKey>
      <Creator>1443*****9604</Creator>
      <DeleteDate>2022-05-08T08:14:16Z</DeleteDate>
</DescribeDBInstanceEncryptionKeyResponse>
```

`JSON` format

```json
{
    "Origin": "Aliyun_KMS",
    "Description": "Description of the key",
    "EncryptionKeyStatus": "Enabled",
    "RequestId": "3BC2768E-DEDA-40FC-BBE9-6B884F3626AF",
    "MaterialExpireTime": "2021-10-18T08:14:16Z",
    "KeyUsage": "ENCRYPT/DECRYPT",
    "EncryptionKey": "5306d1b6-7fd3-42d9-9511-xxxxxxx",
    "Creator": "1443*****9604",
    "DeleteDate": "2022-05-08T08:14:16Z"
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDTCSecur ityIpHostsForSQ LServer | The operation that you want to perform. Set the value to ModifyDTCSecurityIpHostsForSQ LServer. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the ApsaraDB RDS instance. |
| SecurityIpHosts | String | Yes | 192.168.1.100,k 3ecstest | The IP address of the ECS instance and the hostname of the Windows computer. Format: IP address,Hostname. Separates multiple values with semicolons (;). |
| WhiteListGroupN ame | String | Yes | test1 | The name of the IP address whitelist. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the ApsaraDB RDS instance. |
| DTCSetResult | String | Success | The result of the IP address whitelist configuration. Valid values: Success Fail |
| RequestId | String | 671B6D32-B907- 4EFF-A3B7- 94D2EAD5E3A3 | The ID of the request. |
| TaskId | String | 178968983 | The ID of the task. |

ApsaraDB for RDS

**2.10.4.**

#### ModifyDTCSecurityIpHostsForSQLServer

Configures a distributed transaction whitelist for an ApsaraDB RDS instance. Distributed transaction whitelists allow for distributed transactions between an Elastic Compute Service (ECS) instance and an ApsaraDB RDS instance. This operation is applicable only to ApsaraDB RDS High-availability Edition instances that run one of the following SQL Server versions: 2012 SE, 2012 EE, 2014 SE, 2016 SE, 2016 EE, and 2017 SE.

**Request parameters**

**Response parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDTCSec urityIpHostsForS QLServer | The operation that you want to perform. Set the value to DescribeDTCSecurityIpHostsForS QLServer. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyDTCSecurityIpHostsForSQLServer &DBInstanceId=rm-uf6wjk5xxxxxxx &RegionId=cn-hangzhou &SecurityIpHosts=192.168.1.100,k3ecstest &WhiteListGroupName=test1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDTCSecurityIpHostsForSQLServerResponse>
  <RequestId>671B6D32-B907-4EFF-A3B7-94D2EAD5E3A3</RequestId>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <DTCSetResult>Success</DTCSetResult>
      <TaskId>178968983</TaskId>
</ModifyDTCSecurityIpHostsForSQLServerResponse>
```

`JSON` format

```json
{
    "RequestId": "671B6D32-B907-4EFF-A3B7-94D2EAD5E3A3",
    "DBInstanceId": "rm-uf6wjk5xxxxxxx",
    "DTCSetResult": "Success",
    "TaskId": 178968983
}
```

**2.10.5.**

#### DescribeDTCSecurityIpHostsForSQLServer

Queries the distributed transaction whitelists of an ApsaraDB RDS instance. This operation is supported only for ApsaraDB RDS High-availability Edition instances that run one of the following SQL Server versions: 2012 SE, 2012 EE, 2014 SE, 2016 SE, 2016 EE, and 2017 SE.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| IpHostPairNum | String | 1 | The number of distributed transaction whitelists. |
| Items | Array of WhiteListGrou ps |  | Details of distributed transaction whitelists. |
| WhiteListGrou ps |  |  |  |
| SecurityIpHost s | String | 192.168.1.100,k3e cstest | The IP address of the Elastic Compute Service (ECS) instance and the hostname of the Windows computer. Format: IP address,Hostname. Separates multiple values with semicolons (;). |
| WhitelistGroup Name | String | test1 | The name of the distributed transaction whitelist. |
| RequestId | String | 2CA62A70-2203- 45C6-8E90- 8971D5ACC0C2 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDTCSecurityIpHostsForSQLServer &DBInstanceId=rm-uf6wjk5xxxxxxx &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDTCSecurityIpHostsForSQLServerResponse>
  <Items>
            <WhiteListGroups>
                  <WhitelistGroupName>test1</WhitelistGroupName>
                  <SecurityIpHosts>192.168.1.100,k3ecstest</SecurityIpHosts>
            </WhiteListGroups>
      </Items>
      <IpHostPairNum>1</IpHostPairNum>
      <RequestId>2CA62A70-2203-45C6-8E90-8971D5ACC0C2</RequestId>
</DescribeDTCSecurityIpHostsForSQLServerResponse>
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceSSL | The operation that you want to perform. Set the value to DescribeDBInstanceSSL. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConnectionStri ng | String | rm- uf6wjk5xxxxxx.mys ql.rds.aliyuncs.com | The endpoint that is protected by SSL encryption. |
| SSLExpireTime | String | 2022-05- 08T08:14:16Z | The time when the server certificate expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |

ApsaraDB for RDS `JSON` format

```json
{
    "Items": {
        "WhiteListGroups": [
            {
                "WhitelistGroupName": "test1",
                "SecurityIpHosts": "192.168.1.100,k3ecstest"
            }
```

]

```json
    },
    "IpHostPairNum": 1,
    "RequestId": "2CA62A70-2203-45C6-8E90-8971D5ACC0C2"
}
```

#### DescribeDBInstanceSSL

Queries Secure Sockets Layer (SSL) settings of an ApsaraDB RDS instance.

**Note**

This operation is supported only for instances that run MySQL 5.6, MySQL 5.7 on RDS High-availability Edition with local SSDs, MySQL 8.0 on RDS High-availability Edition with local SSDs, SQL Server, or PostgreSQL with standard SSDs.

**Request parameters**

**Response parameters**

| RequireUpdate | String | Yes | Indicates whether the server certificate needs to be updated. Valid values for ApsaraDB RDS for MySQL or ApsaraDB RDS for SQL Server: No Yes Valid values for ApsaraDB RDS for PostgreSQL: 0: no 1: yes |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |
| RequireUpdate Reason | String | - | The reason why the server certificate needs to be updated. This parameter is supported only when the instance runs PostgreSQL with standard SSDs. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceSSL &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format ApsaraDB for RDS

```xml
<ClientCertRevocationList>-----BEGIN X509 CRL-----MIIB****19mg==-----END X509 CRL-----</ ClientCertRevocationList> <RequestId>1AD222E9-E606-4A42-BF6D-8A4442913CEF</RequestId> <RequireUpdateItem>-</RequireUpdateItem> <CAType>aliyun</CAType> <LastModifyStatus>setting</LastModifyStatus> <ACL>cert</ACL> <RequireUpdate>Yes</RequireUpdate> <ModifyStatusReason>Modify DB Instance SSL Config.</ModifyStatusReason> <ClientCACertExpireTime>-</ClientCACertExpireTime> <ServerKey>-----BEGIN PRIVATE KEY-----MIIE****ihfg==-----END PRIVATE KEY-----</ServerKey
```

>

```xml
<SSLExpireTime>2022-05-08T08:14:16Z</SSLExpireTime> <SSLCreateTime>-</SSLCreateTime> <ServerCert>-----BEGIN CERTIFICATE-----MIID*****QqEP-----END CERTIFICATE-----</ServerCer
```

`t>`

```xml
<SSLEnabled>on</SSLEnabled> <ClientCACert>-----BEGIN CERTIFICATE-----MIID*****viXk=-----END CERTIFICATE-----</Client CACert> <ReplicationACL>cert</ReplicationACL> <RequireUpdateReason>-</RequireUpdateReason> <ConnectionString>rm-uf6wjk5xxxxxx.mysql.rds.aliyuncs.com</ConnectionString> <ServerCAUrl>-</ServerCAUrl>
```

`JSON` format

```json
{
    "ClientCertRevocationList": "-----BEGIN X509 CRL-----MIIB****19mg==-----END X509 CRL
-----",
    "RequestId": "1AD222E9-E606-4A42-BF6D-8A4442913CEF",
    "RequireUpdateItem": "-",
    "CAType": "aliyun",
    "LastModifyStatus": "setting",
    "ACL": "cert",
    "RequireUpdate": "Yes",
    "ModifyStatusReason": "Modify DB Instance SSL Config.",
    "ClientCACertExpireTime": "-",
    "ServerKey": "-----BEGIN PRIVATE KEY-----MIIE****ihfg==-----END PRIVATE KEY-----",
    "SSLExpireTime": "2022-05-08T08:14:16Z",
    "SSLCreateTime": "-",
    "ServerCert": "-----BEGIN CERTIFICATE-----MIID*****QqEP-----END CERTIFICATE-----",
    "SSLEnabled": "on",
    "ClientCACert": "-----BEGIN CERTIFICATE-----MIID*****viXk=-----END CERTIFICATE-----"
```

,

```json
    "ReplicationACL": "cert",
    "RequireUpdateReason": "-",
    "ConnectionString": "rm-uf6wjk5xxxxxx.mysql.rds.aliyuncs.com",
    "ServerCAUrl": "-"
}
```

#### ModifyDBInstanceSSL

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eSSL | The operation that you want to perform. Set the value to ModifyDBInstanceSSL. |
| ConnectionStrin g | String | Yes | rm- uf6wjk5xxxxx.m ysql.rds.aliyuncs .com | The internal or public endpoint for which the server certificate needs to be created or updated. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| SSLEnabled | Integer | No | 1 | Specifies whether to enable or disable SSL encryption. Valid values: 1: enables SSL encryption. 0: disables SSL encryption. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 777C4593-8053- 427B-99E2- 105593277CAB | The ID of the request. |

ApsaraDB for RDS Modifies the SSL encryption settings of an ApsaraDB RDS instance. This operation is used to configure SSL encryption for an instance.

**Note**

This operation is supported only for instances that run MySQL 5.6, MySQL 5.7 on RDS High-availability Edition with local SSDs, MySQL 8.0 on RDS High-availability Edition with local SSDs, SQL Server, or PostgreSQL with standard SSDs. SSL encryption is not supported for connections to read/write splitting endpoints.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceSSL &ConnectionString=rm-uf6wjk5xxxxx.mysql.rds.aliyuncs.com &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eTDE | The operation that you want to perform. Set the value to ModifyDBInstanceTDE. |
| DBInstanceId | String | Yes | rm-uf6wjk5**** | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| TDEStatus | String | Yes | Enabled | Specifies whether to enable TDE. Valid values: Enabled Disabled |

ApsaraDB for RDS

```xml
<RequestId>777C4593-8053-427B-99E2-105593277CAB</RequestId>
```

`JSON` format

```json
{
    "RequestId": "777C4593-8053-427B-99E2-105593277CAB"
}
```

#### ModifyDBInstanceTDE

Enables the Transparent Data Encryption (TDE) feature for an ApsaraDB RDS instance. TDE performs real-time I/O encryption and decryption on data files. Data is encrypted before it is written to a disk. Data is also decrypted when it is read from a disk and written to the memory. Before you call this operation, make sure that the following requirements are met: Key Management Service (KMS) is activated. If KMS is not activated, you can activate it when you enable TDE. The instance runs one of the following database engines and RDS editions: MySQL 5.6 MySQL 5.7 on RDS High-availability Edition with local SSDs SQL Server 2019 SE or an Enterprise Edition of SQL Server

**Request parameters**

| DBName | String | No | testDB | The name of the database for which you want to enable TDE. You can specify up to 50 names in a single request. Separate multiple names with commas (,). Note This parameter is available and required only when the instance runs SQL Server 2019 SE or an Enterprise Edition of SQL Server. |
|---|---|---|---|---|
| EncryptionKey | String | No | 749c1df7-****- ****-****-**** | The ID of the custom key. Note This parameter can be specified only for instances that run MySQL. |
| RoleArn | String | No | acs:ram::14069 26****:role/aliyu nrdsinstanceenc ryptiondefaultrol e | The Alibaba Cloud Resource Name (ARN) of the role. An ARN is the global resource identifier of a role. Note This parameter can be specified only for instances that run MySQL. |
| EncryptAlgorith m | String | No | SM4 | The encryption method for TDE. Valid values: SM4 AES 256 CBC _ _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 777C4593-8053- 427B-99E2- 105593277CAB | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceTDE &DBInstanceId=rm-uf6wjk5**** &TDEStatus=Enabled &<Common request parameters>
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceTDE | The operation that you want to perform. Set the value to DescribeDBInstanceTDE. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TDEStatus | String | Enabled | The TDE status at the instance level. Valid value: Enabled and Disabled |

ApsaraDB for RDS Sample success responses `XML` format

```xml
      <RequestId>777C4593-8053-427B-99E2-105593277CAB</RequestId>
```

`JSON` format

```json
{
        "RequestId": "777C4593-8053-427B-99E2-105593277CAB"
    }
}
```

#### DescribeDBInstanceTDE

Queries the data encryption status of an ApsaraDB RDS instance. This operation is used to view the Transparent Data Encryption (TDE) configuration of an instance.

**Note**

This operation is supported only for instances that run MySQL 5.6, SQL Server 2019 SE, or SQL Server EE.

**Request parameters**

**Response parameters**

| Databases | Array of Database |  | Details of the TDE status at the database level. Note For the instances that run SQL Server 2019 SE or SQL Server EE, you can specify whether to enable TDE at the database level when you enable TDE at the instance level. |
|---|---|---|---|
| Database |  |  |  |
| DBName | String | test02 | The name of the database. |
| TDEStatus | String | Enabled | The TDE status at the database level. Valid value: Enabled and Disabled |
| EncryptAlgorit hm | String | AES 256 CBC _ _ | The encryption method of the TDE. Valid values: SM4 AES 256 CBC _ _ |
| RequestId | String | C816A4BF-A6EC- 4722-95F9- 2055859CCFD2 | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceTDE &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <TDEStatus>Enabled</TDEStatus>
      <Databases>
            <DBName>test02</DBName>
            <TDEStatus>Enabled</TDEStatus>
      </Databases>
      <requestId>C816A4BF-A6EC-4722-95F9-2055859CCFD2</requestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeResourc eUsage | The operation that you want to perform. Set the value to DescribeResourceUsage. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| Engine | String | MySQL | The database engine of the instance. |

ApsaraDB for RDS

```json
{
    "TDEStatus": "Enabled",
    "Databases": [
        {
            "DBName": "test02",
            "TDEStatus": "Enabled"
        }
```

`],`

```json
    "requestId": "C816A4BF-A6EC-4722-95F9-2055859CCFD2"
}
```

### Monitoring management

#### DescribeResourceUsage

Queries the storage usage of an ApsaraDB RDS instance.

**Request parameters**

**Response parameters**

| DiskUsed | Long | 2337275904 | The storage space occupied by both data files and log files. Unit: byte. A value of -1 indicates that no data files or log files are stored on the instance. |
|---|---|---|---|
| DataSize | Long | 1292094741 | The storage space occupied by data files. Unit: byte. A value of -1 indicates that no data files are stored on the instance. |
| LogSize | Long | 1045181163 | The storage space occupied by log files. Unit: byte. A value of -1 indicates that no log files are stored on the instance. |
| BackupSize | Long | 53002759 | The storage space occupied by backup data. Unit: byte. A value of -1 indicates that no backup data is stored on the instance. |
| ColdBackupSiz e | Long | 2337275904 | The storage space occupied by cold backup files. Unit: byte. A value of -1 indicates that no cold backup files are stored on the instance. |
| SQLSize | Long | 315052751 | The storage space occupied by SQL data. Unit: byte. A value of -1 indicates that no SQL data is stored on the instance. |
| BackupOssDat aSize | Long | 8821760 | The size of data backup files that are stored in Object Storage Service (OSS) buckets. Unit: byte. A value of 0 indicates that no data backup files are stored in OSS buckets. |
| BackupOssLog Size | Long | 44180999 | The size of log backup files that are stored in OSS buckets. Unit: byte. A value of 0 indicates that no log backup files are stored in OSS buckets. |
| RequestId | String | F937E173-559C- 4498-8D90- 38D32342B9E4 | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeResourceUsage &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses ApsaraDB for RDS `XML` format

```xml
  <PaidBackupSize>0</PaidBackupSize>
  <RequestId>28E73580-103C-4925-A48D-9A7E25F24297</RequestId>
  <BackupSize>51305057407</BackupSize>
  <ArchiveBackupSize>0</ArchiveBackupSize>
  <ColdBackupSize>-1</ColdBackupSize>
  <LogSize>2097152</LogSize>
  <BackupOssLogSize>48565375</BackupOssLogSize>
  <DBInstanceId> rm-uf6wjk5xxxxxxx</DBInstanceId>
  <BackupDataSize>51256492032</BackupDataSize>
  <DataSize>3198156800</DataSize>
  <BackupLogSize>48565375</BackupLogSize>
  <BackupOssDataSize>0</BackupOssDataSize>
  <SQLSize>446228522</SQLSize>
  <DiskUsed>3200253952</DiskUsed>
  <Engine>MySQL</Engine>
```

`JSON` format

```json
{
    "PaidBackupSize": 0,
    "RequestId": "28E73580-103C-4925-A48D-9A7E25F24297",
    "BackupSize": 51305057407,
    "ArchiveBackupSize": 0,
    "ColdBackupSize": -1,
    "LogSize": 2097152,
    "BackupOssLogSize": "48565375",
    "DBInstanceId": " rm-uf6wjk5xxxxxxx",
    "BackupDataSize": 51256492032,
    "DataSize": 3198156800,
    "BackupLogSize": 48565375,
    "BackupOssDataSize": "0",
    "SQLSize": 446228522,
    "DiskUsed": 3200253952,
    "Engine": "MySQL"
}
```

#### DescribeDBInstancePerformance

Queries the performance metrics of an ApsaraDB RDS instance. You can query the performance of an instance over a specific time range based on its performance metrics. Performance metrics are generated by using one of the following methods based on the database engine and version, RDS edition, monitoring frequency (ModifyDBInstanceMonitor), and query time range: Instances that run MySQL:

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

ApsaraDB for RDS 5-second monitoring frequency If the query time range is greater than seven days, performance metrics are collected at 1-day intervals. If the query time range is greater than one day but less than or equal to seven days, performance metrics are collected at 1-hour intervals. If the query time range is greater than or equal to an hour but less than or equal to one day, performance metrics are collected at 1-minute intervals. If the query time range is less than an hour, performance metrics are collected at 5second intervals. 60-second monitoring frequency If the query time range is greater than 30 days, performance metrics are collected at 1day intervals. If the query time range is greater than seven days but less than or equal to 30 days, performance metrics are collected at 1-hour intervals. If the query time range is less than or equal to seven days, performance metrics are collected at 1-minute intervals. 300-second monitoring frequency If the query time range is greater than 30 days, performance metrics are collected at 1day intervals. If the query time range is greater than seven days but less than or equal to 30 days, performance metrics are collected at 1-hour intervals. If the query time range is less than or equal to seven days, performance metrics are collected at 5-minute intervals. Instances that run PostgreSQL with local SSDs or standard SSDs: If the query time range is less than or equal to an hour, performance metrics are collected at 5-second intervals. If the query time range is less than or equal to 2 hours, performance metrics are collected at 10-second intervals. If the query time range is less than or equal to 6 hours, performance metrics are collected at 30-second intervals. If the query time range is less than or equal to 12 hours, performance metrics are collected at 1-minute intervals. If the query time range is less than or equal to one day, performance metrics are collected at 2-minute intervals. If the query time range is less than or equal to five days, performance metrics are collected at 10-minute intervals. If the query time range is less than or equal to 15 days, performance metrics are collected at 30-minute intervals. If the query time range is less than or equal to 30 days, performance metrics are collected at 1-hour intervals. If the query time range is greater than 30 days, performance metrics are collected at 1day intervals.

**Request parameters**

| Action | String | Yes | DescribeDBInsta ncePerformance | The operation that you want to perform. Set the value to DescribeDBInstancePerformance. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| Key | String | Yes | MySQL Sessions _ | The performance metrics that you want to query. Separate multiple performance metrics with commas (,). For more information, see Performance parameters. Note If you set the Key parameter to MySQL SpaceUsage or _ SQLServer SpaceUsage, you _ can query the performance metric only over one day. |
| StartTime | String | Yes | 2012-06- 08T15:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. Note The time span between the beginning time and the end time must be longer than the monitoring frequency. Otherwise, this operation may return an empty parameter. |
| EndTime | String | Yes | 2012-06- 18T15:00Z | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. Note The time span between the beginning time and the end time must be longer than the monitoring frequency. Otherwise, this operation may return an empty parameter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm- uf6wjk5xxxxxxxxxx | The ID of the instance. |

ApsaraDB for RDS

**Response parameters**

| Engine | String | MySQL | The database engine of the instance. |
|---|---|---|---|
| StartTime | String | 2012-06- 10T15:00Z | The start time of the query. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mmZ format. The time is displayed in UTC. |
| EndTime | String | 2012-06- 19T15:00Z | The end time of the query. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mmZ format. The time is displayed in UTC. |
| PerformanceK eys | Array of PerformanceK ey |  | Details of the performance metrics. |
| PerformanceK ey |  |  |  |
| Key | String | MySQL Sessions _ | The name of the performance metric. |
| Unit | String | KB | The unit of the performance metric. |
| ValueFormat | String | recv k&sent k _ _ | The format that the value of the performance metric follows. Multiple values of the performance metric are separated by the &amp; string. Example: com delete&amp;com insert&amp;com in _ _ _ sert select&amp;com replace. _ _ |
| Values | Array of PerformanceV alue |  | An array that consists of values of the performance metric in the following format: {value1, value2, ...}. |
| PerformanceV alue |  |  |  |
| Value | String | 0.0&13.6 | The value of the performance metric. |
| Date | String | 2011-05- 30T03:29:00Z | The date and time when the value of the performance metric was recorded. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| RequestId | String | A5409D02-D661- 4BF3-8F3D- 0A814D0574E7 | The ID of the request. |

ApsaraDB for RDS

**Example**

Sample requests ApsaraDB for RDS

```
http(s)://rds.example.com/?Action=DescribeDBInstancePerformance &DBInstanceId= rm-uf6wjk5xxxxxxx &Key=MySQL_Sessions &StartTime=2012-06-08T15:00Z &EndTime=2012-06-18T15:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>A5409D02-D661-4BF3-8F3D-0A814D0574E7</RequestId>
      <DBInstanceID> rm-uf6wjk5xxxxxxx</DBInstanceID>
      <StartTime>2012-06-11T15:00Z</StartTime>
      <EndTime>2013-10-17T15:00Z</EndTime>
      <Engine>MySQL</Engine>
      <PerformanceKeys>
            <PerformanceKey>
                  <Key>MySQL_NetworkTraffic</Key>
                  <Unit>KB</Unit>
                  <ValueFormat>recv_k&amp;sent_k</ValueFormat>
                  <Values></Values>
            </PerformanceKey>
      </PerformanceKeys>
```

`JSON` format

```json
{
    "RequestId": "A5409D02-D661-4BF3-8F3D-0A814D0574E7",
    "DBInstanceID": " rm-uf6wjk5xxxxxxx",
    "StartTime": "2012-06-11T15:00Z",
    "EndTime": "2013-10-17T15:00Z",
    "Engine": "MySQL",
    "PerformanceKeys": {
        "PerformanceKey": [
            {
                "Key": "MySQL_NetworkTraffic",
                "Unit": "KB",
                "ValueFormat": "recv_k&sent_k",
                "Values": {
                    "PerformanceValue": []
                }
            }
```

]

```
    }
}
```

Queries the monitoring frequency of an ApsaraDB RDS instance.

#### DescribeDBInstanceMonitor

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceMonitor | The operation that you want to perform. Set the value to DescribeDBInstanceMonitor. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Period | String | 60 | The monitoring frequency. Unit: seconds. |
| RequestId | String | 30829FD4-1A84- 4C2A-A625- 2EADECB95CA3 | The ID of the request. |

ApsaraDB for RDS

**Note**

This operation is not supported for instances that run PostgreSQL. The query granularity of these instances is self-adaptive based on the query time range.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDBInstanceMonitor &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <period>60</period>
      <requestId>30829FD4-1A84-4C2A-A625-2EADECB95CA3</requestId>
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eMonitor | The operation that you want to perform. Set the value to ModifyDBInstanceMonitor. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| Period | String | Yes | 60 | The new monitoring frequency. Valid values: 5 10 60 300 Unit: seconds. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

ApsaraDB for RDS `JSON` format

```json
{
    "period": "60",
    "requestId": "30829FD4-1A84-4C2A-A625-2EADECB95CA3"
}
```

#### ModifyDBInstanceMonitor

Modifies the monitoring frequency of an ApsaraDB RDS instance. ApsaraDB RDS provides different monitoring frequency settings for different instances. For more information, see **Set a monitoring frequency** in **ApsaraDB RDS****User Guide**.

**Note**

This operation is not supported for instances that run PostgreSQL. The query granularity of these instances is self-adaptive based on the query time range.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 52B9805C-432C- 4ED1-83FD- 2F916B6D2733 | The ID of the request. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidDBInstanceI d.NotFound | The DBInstanceId provided does not exist in our records. | The error message returned because the specified instance does not exist. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyDBInstanceMonitor &DBInstanceId=rm-uf6wjk5xxxxxxx &Period=60 &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <requestId>52B9805C-432C-4ED1-83FD-2F916B6D2733</requestId>
```

`JSON` format

```json
{
    "requestId": "52B9805C-432C-4ED1-83FD-2F916B6D2733"
}
```

### Parameter management

#### DescribeParameters

Queries the parameter configurations of an ApsaraDB RDS instance. Before you call this operation, make sure that the instance runs one of the following database engines: MySQL PostgreSQL

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeParame ters | The operation that you want to perform. Set the value to DescribeParameters. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MySQL | The database engine of the instance. |
| EngineVersion | String | 5.7 | The database engine version of the instance. |
| RunningParam eters | Array of DBInstancePar ameter |  | The running parameters of the instance. |
| DBInstancePar ameter |  |  |  |
| ParameterNa me | String | fill factor | The name of the parameter. |
| ParameterValu e | String | 0 | The value of the parameter. |
| ParameterDes cription | String | This option sets the default fill factor value within the server scope. A fill factor is provided to optimize index data storage and performance. | The description of the parameter. |

ApsaraDB for RDS PolarDB

**Request parameters**

**Response parameters**

| ConfigParamet ers | Array of DBInstancePar ameter |  | The parameters that are being synchronized. After you modify and submit parameters, you must wait for the parameters to be synchronized to the instance. After the synchronization is complete, these parameters are removed from the list. |
|---|---|---|---|
| DBInstancePar ameter |  |  |  |
| ParameterNa me | String | fill factor | The name of the parameter. |
| ParameterValu e | String | 50 | The value of the parameter. |
| ParameterDes cription | String | This option sets the default fill factor value within the server scope. A fill factor is provided to optimize index data storage and performance. | The description of the parameter. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeParameters &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format ApsaraDB for RDS

```xml
      <ConfigParameters>
            <DBInstanceParameter>
                  <ParameterDescription> This option sets the default fill factor value
within the server scope. A fill factor is provided to optimize index data storage and p erformance. </ParameterDescription>
                  <ParameterName>fill factor</ParameterName>
                  <ParameterValue>50</ParameterValue>
            </DBInstanceParameter>
      </ConfigParameters>
      <Engine>mssql</Engine>
      <EngineVersion>2008r2</EngineVersion>
      <RunningParameters>
            <DBInstanceParameter>
                  <ParameterDescription> This option sets the default fill factor value
within the server scope. A fill factor is provided to optimize index data storage and p erformance. </ParameterDescription>
                  <ParameterName>fill factor</ParameterName>
                  <ParameterValue>0</ParameterValue>
            </DBInstanceParameter>
      </RunningParameters>
      <RequestId>2A748162-8040-4D6B-813E-6910C8C033F1</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyParamete r | The operation that you want to perform. Set the value to ModifyParameter. |

ApsaraDB for RDS

```json
{
  "ConfigParameters": {
      "DBInstanceParameter": [
          {
              "ParameterDescription": "This parameter sets the default fill factor value
within the server scope. A fill factor is provided to optimize index data storage and p erformance.",
              "ParameterName": "fill factor",
              "ParameterValue": "50"
          }
```

]

```json
  },
  "Engine": "mysql",
  "EngineVersion": "5.7",
  "RunningParameters": {
      "DBInstanceParameter": [
          {
              "ParameterDescription": "This parameter sets the default fill factor value
within the server scope. A fill factor is provided to optimize index data storage and p erformance.",
              "ParameterName": "fill factor",
              "ParameterValue": "0"
          }
```

]

```json
  },
  "RequestId": "2A748162-8040-4D6B-813E-6910C8C033F1"
}
```

#### ModifyParameter

Modifies the parameters of an ApsaraDB RDS instance. You can modify the parameters directly or by using a parameter template. After you submit the parameter modification request, ApsaraDB RDS starts a task to apply the new parameter values to the instance. If a new parameter value takes effect only after the instance restarts, ApsaraDB RDS restarts the instance.

**Note**

Before you execute a parameter modification task, ApsaraDB RDS checks whether the parameters exist, whether they are editable, and whether the new parameter values are valid.

**Request parameters**

| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
|---|---|---|---|---|
| Parameters | String | No | {"delayed insert _ timeout":"600", _ "max length for _ _ sort data":"204 _ _ 8"} | The JSON strings of parameters and their values. All the parameter values are of the string type. Format: {"Parameter name 1":"Parameter value 1","Parameter name 2":"Parameter value 2"...} Note If you specify this parameter, you do not need to specify the ParameterGroupId parameter. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Forcerestart | Boolean | No | false | Specifies whether to restart the instance for a new parameter value to take effect. Valid values: true: The system forcibly restarts the instance. If a new parameter value takes effect only after the instance starts, you must set this parameter to true. Otherwise, the new parameter value cannot take effect. false: The system does not forcibly restart the instance. Default value: false. |

ApsaraDB for RDS

| ParameterGroup Id | String | No | rpg-xxxxxxxxx | The ID of the parameter template. Note If you specify this parameter, you do not need to specify the Parameters parameter. If the parameter template applies only after you restart the instance, you must specify the Forcerestart parameter. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 542BB8D6-4268- 45CC-A557- B03EFD7AB30A | The ID of the request. |

| > Document Versio | n: 20260313 |  |  | 26 |
|---|---|---|---|---|

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyParameter &DBInstanceId=rm-uf6wjk5xxxxxxx &Parameters={"delayed_insert_timeout":"600","max_length_for_sort_data":"2048"} &<Common request parameters>
```

Sample success responses `XML` format

```xml
         <RequestId>542BB8D6-4268-45CC-A557-B03EFD7AB30A</RequestId>
```

`JSON` format

```json
{
       "RequestId":"542BB8D6-4268-45CC-A557-B03EFD7AB30A"
}
```

#### DescribeModifyParameterLog

Queries the parameter modification logs of an ApsaraDB RDS instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeModifyP arameterLog | The operation that you want to perform. Set the value to DescribeModifyParameterLog. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxx | The ID of the instance. |
| StartTime | String | Yes | 2020-03- 01T00:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2020-03- 01T10:00Z | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 50 100 Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxx | The ID of the instance. |
| Engine | String | mysql | The database engine of the instance. |
| EngineVersion | String | 5.6 | The database engine version of the instance. |
| Items | Array of ParameterCha ngeLog |  | Details of parameter modification log entries. |

ApsaraDB for RDS

**Response parameters**

| ParameterCha ngeLog |  |  |  |
|---|---|---|---|
| ModifyTime | String | 1584076066000 | The time when the parameter was modified. This value is a UNIX timestamp. Unit: milliseconds. |
| NewParameter Value | String | 3 | The new value of the parameter. |
| OldParameter Value | String | 8 | The original value of the parameter. |
| ParameterNa me | String | innodb stats samp _ _ le pages _ | The name of the parameter. |
| Status | String | Syncing | The status of the new value specified for the parameter. Valid values: Applied: The new value has taken effect. Syncing: The new value is being applied and has not taken effect. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 1 | The number of entries returned per page. |
| RequestId | String | C8E88DED-533F- 4B3C-9207- 731FBF394CCA | The ID of the request. |
| TotalRecordCo unt | Integer | 1 | The total number of entries returned. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeModifyParameterLog &DBInstanceId=rm-uf6wjk5xxxxx &StartTime=2020-03-01T00:00Z &EndTime=2020-03-01T10:00Z &<Common request parameters>
```

Sample success responses `XML` format ApsaraDB for RDS

```xml
  <EngineVersion>5.6</EngineVersion>
  <Engine>mysql</Engine>
  <RequestId>C8E88DED-533F-4B3C-9207-731FBF394CCA</RequestId>
  <DBInstanceId>rm-uf6wjk5xxxxx</DBInstanceId>
  <PageNumber>1</PageNumber>
  <PageRecordCount>1</PageRecordCount>
  <TotalRecordCount>1</TotalRecordCount>
  <Items>
        <ParameterChangeLog>
              <Status>Syncing</Status>
              <ModifyTime>1584076066000</ModifyTime>
              <NewParameterValue>3</NewParameterValue>
              <OldParameterValue>8</OldParameterValue>
              <ParameterName>innodb_stats_sample_pages</ParameterName>
        </ParameterChangeLog>
  </Items>
```

`JSON` format

```json
{"EngineVersion":"5.6",
   "Engine":"mysql",
   "RequestId":"C8E88DED-533F-4B3C-9207-731FBF394CCA",
   "DBInstanceId":"rm-uf6wjk5xxxxx",
   "PageNumber":"1",
   "PageRecordCount":"1",
   "TotalRecordCount":"1",
   "Items":
    {"ParameterChangeLog":
      [{"Status":"Syncing",
        "ModifyTime":"1584076066000",
        "NewParameterValue":"3",
        "OldParameterValue":"8",
        "ParameterName":"innodb_stats_sample_pages"}]}
   }
```

### Log management

#### DescribeSlowLogs

You can call the DescribeSlowLogs operation to query the summary of the slow query logs of an instance.

**Usage notes**

This operation is supported only by ApsaraDB RDS instances that run MySQL. This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeSlowLogs | The operation that you want to perform. Set the value to DescribeSlowLogs. |
| DBInstanc eId | Strin g | Query | Yes | REDLINE LOG STATISTIC _ _ S-rm-uf6wjk5**** | The instance ID. You can call the DescribeDBInstances operation to query the instance ID. |
| StartTime | Strin g | Query | Yes | 2025-05-17T16:00:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| EndTime | Strin g | Query | Yes | 2025-05-18T16:00:00Z | The end of the time range to query. The end time must be later than the start time. The time span between the start time and the end time must be less than 15 days. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| DBName | Strin g | Query | No | testDB | The name of the destination database. |
| Engine | Strin g | Query | No | MySQL | The type of the database. This parameter is required and supports only MySQL. |

ApsaraDB for RDS

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SortKey | Strin g | Query | No | TotalExecutionCounts | The dimension based on which ApsaraDB RDS sorts the entries to return. Valid values: TotalExecutionCoun ts : The system sorts the entries to return based on the number of times that SQL statements are executed. TotalQueryTimes : The system sorts the entries to return based on the total execution duration. TotalLogicalRead s : The system sorts the entries to return based on the total number of logical reads. TotalPhysicalRead s : The system sorts the entries to return based on the total number of physical reads. |
| PageSize | Integ er | Query | No | 30 | The number of entries per page. Valid values: 30 to 100 . Default value: 30 . |
| PageNum ber | Integ er | Query | No | 1 | The page number. Pages start from page 1. Default value: 1 . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array | { "ONLINE": 1, "OFFLINE": 9 } | Details about the slow query logs. |
| -SlowLogId | Long | 26584213 | The ID of the slow query log summary. |
| -SQLId | Long | 1111 | The ID of the SQL statement. |

ApsaraDB for RDS

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| -SQLHASH | String | U2FsdGVk**** | The unique ID of the SQL statement in the slow query log details. |
| -SQLIdStr | String | None | The ID of the SQL statement in the statistical template of slow query logs. This parameter is replaced by the SQLHASH parameter. |
| -DBName | String | testDB | The database name. |
| -SQLText | String | select sleep(2) | The details of the SQL statement. |
| - MySQLTotalEx ecutionCounts | Long | 1 | The total number of SQL statements that were executed in the query. This parameter is returned only for instances that run MySQL. |
| - MySQLTotalEx ecutionTimes | Long | 1 | The total execution duration of all SQL statements in the query. This parameter is returned only for instances that run MySQL. Unit: seconds. |
| - TotalLockTime s | Long | 0 | The total lock duration that was caused by all SQL statements in the query. Unit: seconds. |
| -MaxLockTime | Long | 0 | The longest lock duration that was caused by a specific SQL statement in the query. Unit: seconds. |
| - ParseTotalRow Counts | Long | 1 | The total number of rows that were parsed by all SQL statements in the query. |
| - ParseMaxRow Count | Long | 1 | The largest number of rows that were parsed by a specific SQL statement in the query. |
| - ReturnTotalRo wCounts | Long | 1 | The total number of rows that were returned by all SQL statements in the query. |
| - ReturnMaxRo wCount | Long | 1 | The largest number of rows that were returned by a specific SQL statement in the query. |

ApsaraDB for RDS

| Developer Guide·A | PI reference |  | ApsaraDB for RD |
|---|---|---|---|
| Parameter | Type | Example | Description |
| -CreateTime | String | 2025-05- 18T12:11:04Z | The date when the data was generated. |
| - TotalLogicalRe adCounts | Long | 1 | The total number of logical reads that were performed by all SQL statements in the query. |
| - TotalPhysicalR eadCounts | Long | 1 | The total number of physical reads that were performed by all SQL statements in the query. |
| -ReportTime | String | 2025-05- 17T16:00:00Z | The time when the report was generated. |
| - MaxExecution Time | Long | 60 | The longest execution duration of a specific SQL statement in the query. Unit: seconds. |
| - AvgExecutionT ime | Long | 1 | The average execution duration per SQL statement in the query. Unit: seconds. |
| RequestId | String | 08A3B71B-FE08- 4B03-974F- CC7EA6DB1828 | The request ID. |
| DBInstanceId | String | REDLINE LOG STA _ _ TISTICS-rm- uf6wjk5**** | The instance ID. |
| Engine | String | MySQL | The database engine of the instance. |
| StartTime | String | 2025-05- 17T16:00:00Z | The start time of the query. |
| EndTime | String | 2025-05- 18T16:00:00Z | The end time of the query. |
| TotalRecordCo unt | Integer | 3 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number. |
| PageRecordCo unt | Integer | 30 | The number of entries on the current page. |

**Examples**

Sample requests ApsaraDB for RDS

```
http(s)://rds.example.com/?Action=DescribeSlowLogs &DBInstanceId=REDLINE_LOG_STATISTICS-rm-uf6wjk5**** &StartTime=2025-05-17T16:00Z &EndTime=2025-05-18T16:00Z &<Common request parameters>
```

Sample success responses `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalRecordCount":3,
 "PageRecordCount":30,
 "RequestId":"08A3B71B-FE08-4B03-974F-CC7EA6DB1828",
 "EndTime":"2025-05-18T16:00:00Z",
 "DBInstanceId":"REDLINE_LOG_STATISTICS-rm-uf6wjk5****",
 "PageNumber":1,
 "StartTime":"2025-05-17T16:00:00Z",
 "Items":[
  {
   "MaxLockTime":0,
   "CreateTime":"2025-05-18T12:11:04Z",
   "SlowLogId":26584213,
   "TotalPhysicalReadCounts":1,
   "TotalLogicalReadCounts":1,
   "TotalLockTimes":0,
   "ReturnMaxRowCount":1,
   "AvgExecutionTime":1,
   "SQLText":"select sleep(2)",
   "ParseMaxRowCount":1,
   "MaxExecutionTime":60,
   "ReportTime":"2025-05-17T16:00:00Z",
   "SQLHASH":"U2FsdGVk****",
   "SQLIdStr":"None",
   "ReturnTotalRowCounts":1,
   "MySQLTotalExecutionCounts":1,
   "ParseTotalRowCounts":1,
   "DBName":"testDB",
   "SQLId":1111,
   "MySQLTotalExecutionTimes":1
  }
```

`],`

```json
 "Engine":"MySQL"
}
```

`XML` format

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | CallEcsApi.Failure | CallEcsApi.Failure | call ecs api failure. |
| 404 | InvalidDB.NotFoun d | InvalidDB.NotFound | Specified db does not exist or DB status does not support this operation. |
| 404 | InvalidEngine.NotF ound | InvalidEngine.NotFound | Specified engine does not exist or engine version does not support this operation. |
| 400 | InvalidTask.NotFou nd | InvalidTaskId.NotFound | The "ImportId" is not found. |
| 403 | IncorrectTaskStatu s | OperationDenied.IncorrectTask Status | The operation is not permitted due to status of import. |
| 403 | IncorrectMigrationS tatus | OperationDenied.IncorrectMigr ationStatus | Migration status does not support this operation. |

ApsaraDB for RDS

```xml
<TotalRecordCount>3</TotalRecordCount> <PageRecordCount>30</PageRecordCount> <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828</RequestId> <EndTime>2025-05-18T16:00:00Z</EndTime> <DBInstanceId>REDLINE_LOG_STATISTICS-rm-uf6wjk5****</DBInstanceId> <PageNumber>1</PageNumber> <StartTime>2025-05-17T16:00:00Z</StartTime> <Items>
 <MaxLockTime>0</MaxLockTime>
 <CreateTime>2025-05-18T12:11:04Z</CreateTime>
 <SlowLogId>26584213</SlowLogId>
 <TotalPhysicalReadCounts>1</TotalPhysicalReadCounts>
 <TotalLogicalReadCounts>1</TotalLogicalReadCounts>
 <TotalLockTimes>0</TotalLockTimes>
 <ReturnMaxRowCount>1</ReturnMaxRowCount>
 <AvgExecutionTime>1</AvgExecutionTime>
 <SQLText>select sleep(2)</SQLText>
 <ParseMaxRowCount>1</ParseMaxRowCount>
 <MaxExecutionTime>60</MaxExecutionTime>
 <ReportTime>2025-05-17T16:00:00Z</ReportTime>
 <SQLHASH>U2FsdGVk****</SQLHASH>
 <SQLIdStr>None</SQLIdStr>
 <ReturnTotalRowCounts>1</ReturnTotalRowCounts>
 <MySQLTotalExecutionCounts>1</MySQLTotalExecutionCounts>
 <ParseTotalRowCounts>1</ParseTotalRowCounts>
 <DBName>testDB</DBName>
 <SQLId>1111</SQLId>
 <MySQLTotalExecutionTimes>1</MySQLTotalExecutionTimes>
</Items> <Engine>MySQL</Engine>
```

| psaraDB for | RDS |  | Developer Guide·API referenc |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidMigrationID. NotFound | InvalidMigrationID.NotFound | The specified migration record does not exist. |
| 403 | OperationDenied.P ayType | OperationDenied.PayType | The operation is not permitted due to pay type of instance. |
| 403 | GetvSwitch.Failure | OperationDenied.VSwitchNotA ccess | No availble vSwitch. |
| 403 | GetCluster.Failure | OperationDenied.ClusterNotAc cess | No availble cluster. |
| 403 | IncorrectSQLLogAct iveStatus | OperationDenied.SQLLogActiv eStatus | The operation is not permitted due to SQLLogActive status. |
| 403 | InvalidClassicNetw ork.ValueNotSuppo rted | OperationDenied.ClassicNetwo rkNotSupported | The operation is not permitted due to create classicNetwork instance. |
| 403 | InvalidDBInstanceS yncMode | OperationDenied.DBInstanceS yncMode | The operation is not permitted due to instance sync mode. |
| 403 | OperationDenied.R esource | OperationDenied.Resource | The resource is out of usage. |
| 403 | Forbidden.BidInvali d | OperationDenied.BidInvalid | The operation is not permitted due to ownerId or resourceOwnerId. |
| 403 | Forbidden.Account NoFound | OperationDenied.AccountNoFo und | The specified ownerId or resourceOwnerId is not found. |
| 403 | InvalidInstanceUse Type.NotSupport | OperationDenied.DBInstanceU seTypeNotSupport | The specified dbinstance use type is not found. |
| 400 | TIME RANGE OVER _ _ LIMIT _ | TIME RANGE OVER LIMIT _ _ _ | search time range cannot be longer than three days. |
| 400 | TIME RANGE OVER _ _ LIMIT.AUDIT _ | TIME RANGE OVER LIMIT.AUDI _ _ _ T | search time range cannot be longer than 7 days. |
| 400 | TIME RANGE OVER _ _ LIMIT.AUDIT DOW _ _ NLOAD | TIME RANGE OVER LIMIT.AUDI _ _ _ T DOWNLOAD _ | search time range cannot be longer than 7 days for exporting files. |
| 400 | TIME RANGE OVER _ _ LIMIT.SLOW LOG _ _ | TIME RANGE OVER LIMIT.SLO _ _ _ W LOG _ | search time range cannot be longer than 7 days. |
| 400 | TIME RANGE OVER _ _ LIMIT.ERROR LOG _ _ | TIME RANGE OVER LIMIT.ERR _ _ _ OR LOG _ | search time range cannot be longer than 7 days. |
| 400 | TOO MANY DOWN _ _ LOAD REQUEST T _ _ O OSS _ | TOO MANY DOWNLOAD REQU _ _ _ EST TO OSS _ _ | too many download request is made in 30 minutes, please wait pre request complete. |
| 400 | IGNITE LOG CLUST _ _ ER DEACTIVATED _ | IGNITE LOG CLUSTER DEACTI _ _ _ VATED | backend app is upgrading, please try again later. |

| Developer Gu | ide·API reference |  | ApsaraDB for RD |
|---|---|---|---|
| HTTP status code | Error code | Error message | Description |
| 400 | IdempotenceParam NotMatch | IdempotenceParamNotMatch | The specified parameter not match. |
| 400 | DefaultVpc.NotSup port | DefaultVpc.NotSupport | The default VPC create is not supported. |
| 400 | Forbidden.RegionN otFound | Forbidden.RegionNotFound | The provided RegionId does not exist. |
| 400 | ClassicNetworkTyp e.NotSupport | ClassicNetworkType.NotSuppo rt | The Classic instance network create is not supported. |
| 400 | InvalidVpcIdOrVswi tchId.NotSupported | InvalidVpcIdOrVswitchId.NotSu pported | The specified vpcId or vSwitchId is not supported. |
| 400 | InvalidVpcIdRegion .NotSupported | InvalidVpcId.NotSupported | The specified vpcId or vSwitchId is not supported. |
| 400 | InvalidVSwitchId.N otSupported | InvalidVSwitchId.NotSupported | The specified VPC zone is not supported. |
| 400 | InvalidVSwitchId.N otSupported | InvalidVSwitchId.NotSupported | The specified VPC zone is not supported. |
| 400 | InvalidQuantity.Mal formed | InvalidQuantity.NotSupported | The specified instance quantity is not supported. |
| 400 | TargetSubnet.NotCl oudInstanceIp | InvalidCloudInstanceIp.NotFou nd | The specified cloud instance ip is not exist. |
| 400 | InvalidRetainInstan ce.Format | InvalidRestoreTime.Malformed | The specified retain instance is not valid. |
| 400 | InvalidRestoreTime .Format | InvalidRestoreTime.Malformed | The specified parameter "RestoreTime" is not valid. |
| 404 | InvalidBackupSetID .NotFound | InvalidBackupId.NotFound | The BackupId provided does not exist. |
| 403 | InvalidBackup.NotF ound | OperationDenied.NotFoundBac kup | The operation is not permitted due to no backup. |
| 403 | InvalidBackupSetId OrRestoreTime.Not Found | OperationDenied.NotFoundBac kupSetIdOrRestoreTime | The operation is not permitted due to no backupSetId or restoreTime. |
| 403 | IncorrectBackupSet Method | OperationDenied.BackupMetho d | The operation is not permitted method of backup. |
| 403 | InvalidBackupLogSt atus | OperationDenied.BackupLogSt atus | The Current backup log enable status does not support this operation. |
| 403 | SecurityIPList.Dupli cate | OperationDenied.SecurityIPList Duplicate | The Specified same security IP already exists. |

| psaraDB for | RDS |  | Developer Guide·API referenc |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | BackupSetDeleteN otSupport | OperationDenied.BackupSetDe leteNotSupport | The Specified backup does not support this operation. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 25659 | InvalidRegion.ValueNotSupport ed | The specified parameter "Region" is not valid. |
| 403 | ReadDBInstanceEx ceeded | QuotaExceeded.ReadonlyDBIn stanceCount | The quota of primary instance mounted read only instance. |
| 403 | LX RORDS BIZ MAI _ _ _ NRDS QUOTA ERR _ _ OR | QuotaExceeded.ReadonlyDBIn stanceCount | The quota of primary instance mounted read only instance. |
| 403 | LX RORDS BIZ MAI _ _ _ NRDS TYPE ERROR _ _ | OperationDenied.PrimaryDBIns tanceType | The operation is not permitted due to type of primary instance. |
| 403 | LX RDS BIZ QUER _ _ _ Y INSTANCE ERRO _ _ R | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | IZ INVALID _ | InvalidZoneId.NotFound | The provided ZoneId does not exist. |
| 404 | Abs.InvalidDBInsta nceId.Malformed | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | InvalidLogRetentio n | InvalidLogRetention.NotSuppor t | The specified log retention is not valid,The current instance type does not support this operation. |
| 403 | UploadLimitExceed ed | QuotaExceeded.Upload | The quota of file exceeds. |
| 403 | -113 | ChargeTypeViolation | The operation is not permitted due to charge type of the instance. |
| 403 | LX SYSTEM _ | System.Error | The operation is error for current isntance. |
| 403 | InvalidStartTime.M alformed | InvalidStartTime.Format | The specified parameter "StartTime" is not valid. |
| 403 | InvalidEndTime.Mal formed | InvalidEndTime.Format | The specified parameter "EndTime" is not valid. |
| 400 | Abs.Engine.Malfor med | InvalidEngine.Malformed | The specified parameter "Engine" is not valid. |
| 400 | InvalidAction | InvalidAction | Specified action is not valid. |
| 400 | Abs.InvalidDBinsta nceNetType.ValueN otSupported | InvalidDBinstanceNetType.Val ueNotSupport | The specified parameter "DBinstanceNetType" is not valid. |

| Developer Gu | ide·API reference |  | ApsaraDB for RD |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | Abs.InstanceUsedT ype.ValueNotSuppo rted | InvalidDBInstanceType.ValueN otSupport | The specified parameter"DBInstanceType" is not valid. |
| 400 | InvalidPageSize | InvalidPageSize | Specified parameter pageSize is not valid. |
| 400 | InvalidPageSize.Ma lformed | InvalidPageSize.Malformed | The specified parameter "PageSize" is not valid. |
| 400 | InvalidExpirePeriod .Malformed | InvalidExpirePeriod.Malformed | The specified parameter "ExpirePeriod" is not valid. |
| 400 | InvalidEngineVersio n.Malformed | InvalidEngineVersion.ValueNot Support | The specified parameter "EngineVersion" is not valid. |
| 400 | InvalidEngine.Malfo rmed | InvalidEngine.ValueNotSupport | The specified parameter "Engine" is not valid. |
| 400 | InvalidLogBackupR etentionPeriod.Malf ormed | InvalidLogBackupRetentionPeri od.Malformed | The Specified LogBackupRetentionPeriod is not valid. |
| 400 | OperationDenied.D BInstanceType | IncorrectDBInstanceType.Child DBInstanceNotSupport | The operation is not permitted due to instance type. |
| 403 | IncorrectBackupSet State | OperationDenied.BackupStatu s | The operation is not permitted due to status of instancebackup. |
| 404 | InvalidOASBackupS etID.NotFound | InvalidBackupID.NotFound | The BackupID provided does not exist. |
| 404 | OASBackupSetExtr actFinished | QuotaExceeded.BackupExtract Finished | The Specified OAS backup set had extracted finish. |
| 400 | OASExtractTimesE xceeded | QuotaExceeded.OASExtractTi mesExceeded | The Current DB Instance backup set had extracted too many times from OAS today. |
| 403 | DBSizeExceeded | QuotaExceeded.DBInstanceSto rage | The quota of instance storage exceeds. |
| 400 | InvalidDBInfo.Form at | InvalidDBInfo.Malformed | The specified parameter "DBInfo" is not valid or db not exist. |
| 403 | NotValidRegion. | OperationDenied.Region | The operation is not permitted due to different region. |
| 403 | InvalidTargetDBInst anceName.Format | OperationDenied.DBInstanceId | The operation is not permitted due to DBInstanceId and SourceDBInstanceId is same. |
| 400 | InvalidFileName.Fo rmat | InvalidFileName.Malformed | The specified parameter "FileName" is not valid. |

| A | psaraDB for | RDS |  | Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidFileName.No tFound | InvalidFileName.NotFound | The FileName provided does not exist. |
| 400 | FileNotCompleted | InvalidFileName.NotCompleted | The specified "FileName" is not completed . |
| 400 | FileNotUploaded | InvalidFileName.NotCompleted | The specified "FileName" is not completed . |
| 400 | FileNotAvailable | InvalidFileName.NotAvailable | The specified "FileName" is not Available . |
| 403 | FileSizeExceeded | QuotaExceeded.FileSize | The quota of file size exceeds. |
| 403 | Abs.IsLockTable.Ma lformed | InvalidIsLockTable.Malformed | The specified parameter "IsLockTable" is not valid. |
| 400 | InvalidDBInstanceN ame.Format | InvalidDBInstanceId.MalForme d | The specified parameter "DBInstanceId" is not valid. |
| 400 | ParameterLeastAss ociate | ParameterLeastAssociate | Must input at least one optional parameter. |
| 400 | Abs.InvalidMaintain Time | InvalidMaintainTime.MalForme d | The specified parameter "MaintainTime" is not valid. |
| 400 | InvalidPeriod.Malfo rmed | InvalidPeriod.Malformed | The Specified parameter "Period" is not valid. |
| 400 | PARAMETER MUST _ NOT NULL _ _ | PARAMETER MUST NOT NULL _ _ _ | The parameter must not be null. |
| 400 | PARAMETER ERRO _ R | PARAMETER ERROR _ | The parameter must not be null. |
| 404 | IntranetNetTypeNo tExists | IntranetNetTypeNotExists | Current DB instance network type does not support this operation. |
| 400 | InvalidVSwitchId.Mi smatch | InvalidVSwitchId.Mismatch | Specified instance and vSwitch are not in the same zone. |
| 404 | InvalidVPCId.NotFo und | InvalidVPCId.NotFound | Specified VPC ID is not found. |
| 400 | InvalidVSwitchId.N otFound | InvalidVSwitchId.NotFound | Specified vSwitch is not found in specified VPC. |
| 400 | VpcIzNoNotEqualsR dsMultIzNo | VpcIzNoNotEqualsRdsMultIzNo | Specified VPC IzNo does not equal to RDS IzNo. |
| 403 | VPC SYSTEM ERRO _ _ R | OperationDenied | VPC system error, please check params. |
| 400 | VPC CLOUD INSTA _ _ NCEIP USED _ | InvalidPrivateIpAddress.Duplic ated | Specified private IP address is duplicated. |

|  | Developer Gu | ide·API reference |  | ApsaraDB for RD | S |
|---|---|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | Invalid.TargetCloud InstanceIp | InvalidPrivateIpAddress.Misma tch | Specified private IP address is not in the CIDR block of virtual switch. |
| 400 | IncorrecttVpcId | IncorrectVpcId.Mismatch | The specified parameter "VpcId " is not valid. |
| 400 | IncorrectInstanceN etworkType | InvalidInstanceNetworkType.V alueNotSupported | The specified parameter "InstanceNetworkType" is not valid. |
| 403 | InvalidCloudInstanc eId.Duplicated | OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. |
| 400 | InvalidIzNo.NotSup ported | InvalidIzNo.NotSupported | Specified VCP zone is not supported. |
| 403 | OperationDenied.S witchToVPC | OperationDenied.Switch | Specified instance cannot be switched to VPC. |
| 404 | InvalidCloudInstanc e.ID | InvalidDBInstanceName.NotFo und | The DBInstanceId provided does not exist. |
| 403 | SlaveLagExceeded | Exceeded.SlaveLag | The slave lag exceeds. |
| 403 | LockTimeout | LockTimeout | The request processing has failed due to lock timeout. |
| 403 | BackupTimesExcee ded | Exceeded.BackupTimes | The backup times exceeds. |
| 404 | Abs.dbInstanceId.N otFound | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | INST NOT BELONG _ _ TO USER _ _ | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26915 | InvalidDBInstanceStorage.Valu eNotSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | MissingParameter | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | LX RDS BIZ INSTA _ _ _ NCE UPGRADE ER _ _ ROR | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | Abs.dbInstanceClas sOrdbInstanceStor age.MissParameter | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | LX BARDS BIZ UP _ _ _ GRADE INSTANCE _ _ ERROR | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 400 | Abs.InstanceUsedT ype.ValueNotSuppo rted | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | LX BARDS BIZ UP _ _ _ GRADE STORAG _ | OperationDenied.DBInstanceSt orageReduce | The operation is not permitted due to reduce storage. |
| 403 | LX BARDS BIZ UP _ _ _ GRADE STORAGE _ _ ERROR | OperationDenied.DBInstanceSt orageReduce | The operation is not permitted due to reduce storage. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26914 | InvaildDBInstanceClassInRegio n.NotAvailable | The DBInstanceClass in the Region is not available. |
| 403 | LX RDS BIZ STATU _ _ _ S ERROR _ | OperationDenied.DBInstanceSt atus | The operation is not permitted due to instance status. |
| 400 | ILLEGAL ARGUMEN _ T | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | InvalidSourceDatab aseUserName.Malf ormed | InvalidDBInfo.Format | The specified parameter "SourceDatabaseUserName" is not valid. |
| 400 | InvalidQueryTime.F ormat | InvalidQueryTime.Format | he specified parameter "QueryTime" is not valid. |
| 400 | Abs.SourceDatabas ePort.Malformed | InvalidSourceDatabasePort.Mal formed | The specified parameter 'SourceDatabasePort' is not valid. |
| 400 | Abs.ImportDataTyp e.Malformed | InvalidImportDataType.Malfor med | The specified parameter 'ImportDataType' is not valid. |
| 400 | ClusterDRCNotSup oort | OperationDenied.DBInstnceInR egion | The operation is not permitted due to DBInstance in the region. |
| 404 | InvalidOrderCharge .NotSupport | InvalidOrderCharge.NotSuppor t | The specified order charge does not support in RDS. |
| 404 | IncorrectInstanceU seType | InvalidDBInstanceIdUseType | InvalidDBInstanceIdUseType. |
| 403 | IncorrectMigrationI D | InvalidImportId.ImportIdvalue | The operation is not permitted due to ImportId value. |
| 403 | InvalidSwitchType | InvalidSwitchType.Malformed | The specified parameter InvalidSwitchType is not valid. |

ApsaraDB for RDS

| Developer Gu | ide·API reference |  | ApsaraDB for RD |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | HaStatusNotSuppor t | OperationDenied.HaStatus | The operation is not permitted due to hastatus no supported. |
| 404 | QuotaExceeded.Ta gOnDBInstance | QuotaExceeded.TagOnDBInsta nce | The quota of tag on DBInstance exceeds. |
| 400 | Tag.Mismatch | Tag.Mismatch | Tag-Key and InvalidDBInstanceName.NotFo undag-Value is mismatch. |
| 400 | InvalidTag.1.key.M alformed | InvalidTag.1.key.Malformed | The specified parameter 'Tag.1.key' is not valid. |
| 400 | InvalidTag.2.key.M alformed | InvalidTag.2.key.Malformed | The specified parameter 'Tag.2.key' is not valid. |
| 400 | InvalidTag.3.key.M alformed | InvalidTag.3.key.Malformed | The specified parameter 'Tag.3.key' is not valid. |
| 400 | InvalidTag.4.key.M alformed | InvalidTag.4.key.Malformed | The specified parameter 'Tag.4.key' is not valid. |
| 400 | InvalidTag.5.key.M alformed | InvalidTag.5.key.Malformed | The specified parameter 'Tag.5.key' is not valid. |
| 400 | InvalidTag.1.value. Malformed | InvalidTag.1.value.Malformed | The specified parameter 'Tag.1.value' is not valid. |
| 400 | InvalidTag.2.value. Malformed | InvalidTag.2.value.Malformed | The specified parameter 'Tag.2.value' is not valid. |
| 400 | InvalidTag.3.value. Malformed | InvalidTag.3.value.Malformed | The specified parameter 'Tag.3.value' is not valid. |
| 400 | InvalidTag.4.value. Malformed | InvalidTag.4.value.Malformed | The specified parameter 'Tag.4.value' is not valid. |
| 400 | InvalidTag.5.value. Malformed | InvalidTag.5.value.Malformed | The specified parameter 'Tag.5.value' is not valid. |
| 400 | TAG KEY ILLEGAL _ _ | Tag.Malformed | The specified parameter Tag is not valid. |
| 400 | TAG VALUE ILLEGA _ _ L | Tag.Malformed | The specified parameter Value is not valid. |
| 400 | Tag.NoRegionIdExi st | Tag.NoRegionIdExist | the region Id can not be blank. |
| 400 | Tag.NoTagInfoExist | Tag.NoTagInfoExist | all the tags and tagN parameters is null. |
| 400 | Tag.TagKeyCanNot BeAll | Tag.TagKeyCanNotBeAll | tag key can not be all. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | Tag.TagKeyDuplex | Tag.TagKeyDuplex | tag key must be sole in one operation. |
| 400 | Tag.NoDBInstanceI dExist | Tag.NoDBInstanceIdExist | the dbinstance Id can not be blank. |
| 400 | Tag.TooManyDBIns tanceIds | Tag.TooManyDBInstanceIds | the dbinstance Ids is more than 30. |
| 400 | Tag.TooManyTagsF orOneInstance | Tag.TooManyTagsForOneInsta nce | total 10 tags can be added to one resource. |
| 400 | Tag.SetTagInfoAtT woParamters | Tag.SetTagInfoAtTwoParamter s | only tags or tagN parameter could be setted. |
| 400 | Tag.Allow5TagInfos | Tag.Allow5TagInfos | only 5 tags allowed in one operation. |
| 400 | Tag.TagKeyIsBlank | Tag.TagKeyIsBlank | tag key can not be blank. |
| 400 | Tag.TagKeyStartWi th.aliyun | Tag.TagKeyStartWith.aliyun | tag key and value can not be started with aliyun. |
| 400 | Tag.TagKeyTooLon g | Tag.TagKeyTooLong | the max tag key's length is 64. |
| 400 | Tag.TagValueTooLo ng | Tag.TagValueTooLong | the max tag value's length is 128. |
| 400 | Tag.InvalidTagsPar amter | Tag.InvalidTagsParamter | tags paramter is invalid. |
| 400 | Abs.InvalidTimePeri od | OperationDenied.TimePeriod | The specified parameter "TimePeriod" is not valid. |
| 400 | Abs.InvalidStartTim e | InvalidStartTime.Malformed | The specified parameter "StartTime" is not valid. |
| 400 | Abs.InvalidEndTime | InvalidEndTime.Malformed | The specified parameter "EndTime" is not valid. |
| 403 | EnabledSSLNotSup port | OperationDenied.EnabledSSLN otSupport | The specified parameter "EnabledSSL" is not valid. |
| 403 | InvalidRequest.Not Finished | OperationDenied.RequestNotFi nished | The specified request not finished. |
| 403 | InvalidRequest.Exis ts | OperationDenied.RequestExist s | The specified request already exists. |
| 400 | Abs.instanceNames .Malformed | InvalidDBInstanceId.QuotaExc eeded | The quota of instance ID exceeded. |
| 400 | InvalidOrderTask.N otSupport | InvalidOrderTask.NotSupport | The Current InstanceId exist Order Task in RDS. |

ApsaraDB for RDS

| Developer Gu | ide·API reference |  | ApsaraDB for RD |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | RenewChange.Exis t | RenewChange.Exist | The Current InstanceId exist renewChange order in RDS. |
| 400 | INVITATION CODE _ _ BIZ FAIL _ | InvalidEActionCode.CodeBizNo tSupported | The specified action code biz is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26080 | InvalidEngine.VauleNotSupport ed | The specified parameter "Engine" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26063 | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26035 | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26036 | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | InvalidEngineVersio n.ValueNotSupport ed | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26062 | InvalidDBInstanceClass.ValueN otSupported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | Abs.dbInstanceClas s.NotFound | InvalidDBInstanceClass.ValueN otSupported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ MissingParameter | InvalidDBInstanceClass.ValueN otSupported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26037 | InvalidDBInstanceStorage.Valu eNotSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | InvalidDBInstanceS torage.ValueNotSu pported | InvalidDBInstanceStorage.Valu eNotSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | Abs.dbInstanceNet Type.ValueNotSupp orted | InvalidDBInstanceNetType.Val ueNotSupported | The specified parameter "InvalidDBInstanceNetType" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ | FUWU BIZ COMMODITY VERIF _ _ _ Y FAIL _ | Oops, unable to complete your payment. The reason for this error may be due to one of the following: 1. Your bank account funds are insufficient. 2. Your account is not yet verified. 3. You have already exceeded the maximum limit of RDS instances. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | QUERY PRICE RES _ _ PONSE ERROR _ | QueryPriceResonse.Failed | query price response error. |
| 400 | LX CREATE ORDER _ _ FAILED _ | CreateOrder.Failed | Create order failed. |
| 404 | InvalidRegion.NotF ound | InvalidRegionId.NotFound | The provided RegionId does not exist. |
| 404 | INQUERY ORDER F _ _ EE FAILED _ | QueryPrice.Failed | QueryPrice Failed. |
| 404 | InvalidRegionId.Not Found | InvalidRegionId.NotFound | The provided RegionId is not found. |
| 404 | InvalidRegion Zone _ NotFound _ | InvalidRegionId.NotFound | The provided RegionId is not found. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26038 | InvalidRegionId.NotFound | The RegionId provided does not exist. |
| 400 | Abs.dbInstanceDes cription.Malformed | InvalidDBInstanceDescription. Malformed | The specified parameter "DBInstanceDescription" is not valid. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26044 | InvalidEngineVersionInRegion. NotAvailable | The EngineVersion in the Region is not available. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26045 | InvalidEngineVersionInRegion. NotAvailable | The EngineVersion in the Region is not available. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26175 | InvaildEngineInRegion.NotAvail able | The engine type in this region is not available. |
| 403 | InvalidUserRegionP rivilege.Malformed | RegionUnauthorized | There is no authority to create instance in the specified region. |
| 403 | LX USER BUY COM _ _ _ MODITY COUNT EX _ _ CEEDED LIMIT _ | QuotaExceeded.CreateInstanc e | The quota of create instance exceeds. |
| 403 | INST HAS UNPAID _ _ _ ORDER | INST HAS UNPAID ORDER _ _ _ | The instanceId has unpaid order. |
| 403 | GET COMMODITY F _ _ AILED | COMMODITY.FAILED | The commodity is error. |
| 403 | MONEY LESSTHAN _ _ 100 | MoneyLessThan100 | The Account Monet less Than 100. |
| 403 | InvalidOrderCharge .NotPay | InvalidOrderCharge.NotPay | The specified parameter OrderCharge is not pay. |

ApsaraDB for RDS

| Developer Gu | ide·API reference |  | ApsaraDB for RD |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | Abs.MissingOwnerI dOrOwnerAccount | MissingParameter | The input parameter "OwnerId" or "OwnerAccount" that is mandatory for processing this request is not supplied. |
| 400 | UnsupportedParam eter | UnsupportedParameter | Unsupported parameter. |
| 400 | InvalidDBInstanceC onnType.Format | InvalidDBInstanceConnType.Fo rmat | The specified instance connection type is not valid. |
| 400 | InvalidSecurityIPLis t.Format | InvalidSecurityIps.MalFormed | The specified parameter "SecurityIps" is not valid. |
| 400 | InvalidBackupSetLo cation | InvalidBackupLocation.Malform ed | The specified parameter "BackupLocation" is not valid. |
| 400 | InvalidParameters. Format | InvalidParameters.Malformed | The specified parameter "Parameters" is not valid. |
| 400 | InvalidConfigValue | InvalidSQLCollectorStatus.Valu eNotSupported | The specified SQLCollectorStatus value not support. |
| 400 | InvalidSqlLog.Malfo rmed | InvalidSQLCollectorStatus.Malf ormed | The specified parameter "SQLCollectorStatus" is not valid. |
| 400 | QuotaExceeded.Sta rtDiagnose | QuotaExceeded.StartDiagnose | The quota of start diagnose exceeds now,try again later. |
| 400 | TaskExists | TaskExists | Specified task have existed. |
| 400 | InvalidDBInstanceD escription.Format | InvalidDBInstanceDescription. Malformed | The specified parameter "DBInstanceDescription" is not valid. |
| 400 | InvalidConnectionS tring.Format | InvalidConnectionString.Malfor med | The specified parameter "ConnectionStringPrefix" is not valid. |
| 400 | InvalidGroupName. Format | InvalidGroupName.Malformed | The specified parameter "DBInstanceIPArrayName" is not valid. |
| 400 | Abs.backupSetStat us.ValueNotSuppor ted | InvalidBackupStatus.ValueNot Support | The specified parameter "BackupStatus" is not valid. |
| 400 | Abs.jobMode.Value NotSupported | InvalidBackupMode.ValueNotS upport | The specified parameter "BackupMode" is not valid. |
| 400 | Abs.InvalidDescript ion.Malformed | InvalidDBDescription.Malforme d | The specified parameter "DBDescription" is not valid. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | Abs.backupTime.Va lueNotSupported | InvalidPreferredBackupTime.M alformed | The specified parameter "PreferredBackupTime" is not valid. |
| 400 | Abs.backupPeriod. Malformed | InvalidPreferredBackupPeriod. Malformed | The specified parameter "PreferredBackupPeriod" is not valid. |
| 400 | InvalidAccountNam e.Format | InvalidAccountName.Malforme d | The specified parameter "AccountName" is not valid. |
| 400 | InvalidAccountNam e.Forbid | InvalidAccountName.keyword | The specified parameter "AccountName" is a keyword. |
| 400 | InvalidAccountNam e.Duplicate | InvalidAccountName.Duplicate | Invalid "AccountName" specified, duplicated. |
| 400 | InvalidAccountPass word.Format | InvalidAccountPassword.Malfor med | The specified parameter "AccountPassword" is not valid. |
| 400 | AccountLimitExcee ded | QuotaExceeded.AccountName | Account limit exceeded. |
| 400 | SwitchTimesLimitE xceeded | QuotaExceeded.SwitchTime | SwitchTimes limit exceeded. |
| 400 | InvalidTDEstatus.F ormat | InvalidTDEstatus.Format | The specified TDEStatus is not valid. |
| 400 | InvalidConnectionM ode | InvalidConnectionMode.ValueN otSupported | The specified parameter "ConnectionMode" is not valid. |
| 400 | InvalidAccountPrivil ege.Malformed | InvalidAccountPrivilege.ValueN otSupport | The specified "AccountPrivilege" is not valid. |
| 400 | IncorrectEngineVer sion | InvaildEngineInRegion.ValueNo tSupported | The engine is not supported in the region. |
| 400 | InvalidDBName.For mat | InvalidDBName.Malformed | The specified parameter "DBName" is not valid. |
| 400 | DBLimitExceeded | QuotaExceeded.DBName | The database operation execeed. |
| 400 | InvalidDBName.Du plicate | InvalidDBName.Duplicate | The Security db Name is not in the available range or occupied. |
| 400 | InvalidCharacterSe tName.Format | InvalidCharsetName.ValueNotS upport | The specified parameter "CharsetName" is not valid. |
| 400 | InvalidDBDescriptio n.Format | InvalidDBDescription.Malforme d | The specified parameter "DBDescription" is not valid. |
| 400 | InvalidDBName.For bid | InvalidParameter.Keyword | The specified parameter "DBName" is keyword. |

| Developer Gu | ide·API reference |  | ApsaraDB for RD |
|---|---|---|---|
| HTTP status code | Error code | Error message | Description |
| 400 | InvalidUserType.No tSupport | InvalidUserType.NotSupport | The operation is not permitted due to type of account. |
| 400 | InvalidExpiredTime .Format | InvalidExpiredTime.Malformed | The specified "ExpiredTime" is not valid. |
| 400 | InvalidBackupMeth od.Format | InvalidBackupMethod.ValueNot Support | The specified parameter "BackupMethod" is not valid. |
| 400 | InvalidBackupLog. Malformed | InvalidBackupLog.Malformed | The specified parameter "backupPeriod" is not valid. |
| 400 | InvalidStartTime.Fo rmat | InvalidStartTime.Malformed | The specified parameter "StartTime" is not valid. |
| 400 | InvalidEndTime.For mat | InvalidEndTime.Malformed | The specified parameter "EndTime" is not valid. |
| 400 | InvalidMaxRecords PerPage.Malformed | InvalidPageSize.Malformed | The specified parameter "PageSize" is not valid. |
| 400 | InvalidSortKey.Malf ormed | InvalidSortKey.Malformed | The specified parameter "SortKey" is not valid. |
| 400 | InvalidSortMethod. Malformed | InvalidSortMethod.Malformed | The specified parameter "SortMethod" is not valid. |
| 400 | InvalidParameter | InvalidParameter | Invalid parameter. |
| 400 | InvalidPort.Malform ed | InvalidPort.Malformed | The specified parameter "Port" is not valid. |
| 400 | InvalidKey.Malform ed | InvalidPerformanceKey.Malfor med | The specified parameter "Key" is not valid. |
| 400 | InvalidQueryKeywo rd.NotSupport | InvalidQueryKeyword.Malform ed | the query key contains exception character. |
| 400 | InvalidParameterCo mbination | InvalidStartTimeAndEndTime. Malformed | The end time must be greater than the start time. |
| 400 | InvalidParameter.R esourceOwnerAcco unt | InvalidParameter.ResourceOw nerAccount | The specified parameter "resourceOwnerAccount" is not valid. |
| 400 | InvalidStorage.For mat | InvalidStorage.Format | The specified "storage" is not valid. |
| 403 | Abs.ApiForbiddenB ySubBid | ActionUnauthorized | The specified action is not available for you. |
| 403 | Forbidden | Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | RAM.ApiNotSupport ed | Forbidden.NotSupportRAM | This action does not support accessed by RAM mode. |
| 403 | RISK CONTROL RE _ _ SULT FAIL _ | Forbidden.RiskControl | This operation is forbidden by aliyun risk control system. |
| 403 | InvalidRegion.NotS upport | OperationDenied.NotSupport | the specified instance region does not support this operation. |
| 403 | IncorrectDBInstanc eLockMode | OperationDenied.LockMode | The operation is not permitted due to instance being locked. |
| 403 | IncorrectDBInstanc eState | OperationDenied.DBInstanceSt atus | The operation is not permitted due to status of instance. |
| 403 | IncorrectDBInstanc eType | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | ChildDBInstanceNo tSupport | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | GuardDBInstanceN otSupport | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | ReadDBInstanceNo tSupport | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | IncorrectDBInstanc eEngine | OperationDenied.DBInstanceE ngine | The operation is not permitted due to engine of instance. |
| 403 | IncorrectDBInstanc eNetType | OperationDenied.DBInstanceN etType | The operation is not permitted due to network type of the instance. |
| 403 | IncorrectDBInstanc eConnType | OperationDenied.PublicConnec tionExists | The specified public connection already existed. |
| 403 | InsufficientResourc eCapacity | OperationDenied | The resource is out of usage. |
| 403 | ClusterNotSupport | OperationDenied.ClusterNotSu pport | The instance cluster does not support this operation. |
| 403 | IncorrectDBInstanc e | OperationDenied.DBInstance | The operation is not permitted due to type of the instance. |
| 403 | IncorrectGuardDBI nstanceVersion | OperationDenied.GuardDBInst anceLower | The operation is not permitted due to higher guard instance version. |
| 403 | IncorrectMasterDBI nstanceState | OperationDenied.MasterDBInst anceState | The operation is not permitted due to status of master instance. |
| 403 | IncorrectAccountSt atus | OperationDenied.AccountStatu s | The operation is not permitted due to status of account. |

ApsaraDB for RDS

| Developer Gu | ide·API reference |  | ApsaraDB for RD |
|---|---|---|---|
| HTTP status code | Error code | Error message | Description |
| 403 | IncorrectAccountTy pe | OperationDenied.AccountType | The operation is not permitted due to type of account. |
| 403 | ConcurrentTaskExc eeded | OperationDenied.TaskExceede d | The concurrent tasks exceeded allowed amount. |
| 403 | IncorrectDBInstanc eAccountMode | OperationDenied.AccountMode | The operation is not permitted due to account mode of instance. |
| 403 | DBNameAndAccou ntPrivilegeCount | OperationDenied.DBNameAnd AccountPrivilegeCount | The operation is not permitted due to count of database or account privilege. |
| 403 | OldPasswordWrong | OperationDenied.PasswordWro ng | The operation is not permitted due to wrong of password. |
| 403 | IncorrectDBType | OperationDenied.DBType | The operation is not permitted due to type of the database. |
| 403 | IncorrectDBState | OperationDenied.DBStatus | The operation is not permitted due to status of the database. |
| 403 | BackupJobExists | OperationDenied.BackupJobExi sts | The operation is not permitted due to backup job exist. |
| 400 | Abs.backupMethod. ValueNotSupported | InvalidBackupMethod.ValueNot Support | The specified parameter "BackupMethod" is not valid. |
| 400 | Abs.backupType.Va lueNotSupported | InvalidBackupType.ValueNotSu pport | The specified parameter "BackupType" is not valid. |
| 404 | INSUFFICIENT BAL _ ANCE | InsufficientBalance | Your account does not have enough balance. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL I _ _ _ NSUFFICIENT BALA _ NCE | InsufficientBalance | Your account does not have enough balance. |
| 400 | INSTANCE PRODUC _ E FAILED _ | CreateOrder.Failed | The instance order is error. |
| 404 | InvalidDBInstanceN ame.NotFound | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | InvalidInstanceId | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | InvalidDB.NotFoun d | InvalidDB.NotFound | The Specified db does not exist or DB status does not support. |
| 404 | InvalidDBInstance. NotFound | InvalidDBInstanceId.NotFound | The specified instance is not found. |

| psaraDB for | RDS |  | Developer Guide·API referenc |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | RAM.InstanceNotFo und | Forbidden.InstanceNotFound | The specified instance is not found. |
| 404 | InvalidConnectionS tring.Duplicate | InvalidConnectionStringPrefix. Duplicated | Specified connection string needs to be same as current network type. |
| 404 | AtLeastOneNetTyp eExists | AtLeastOneNetTypeExists | The specified network type at least one. |
| 404 | NetTypeExists | NetTypeExists | The specified public network type already exists. |
| 404 | InvalidConnectionS tringOrPort.Duplica te | InvalidConnectionString.Duplic ate | Specified connection string or port needs to be same as current network type. |
| 404 | InvalidConnectionS tring.NotFound | InvalidConnectionString.NotFo und | The specified connection string or network type is not found. |
| 404 | ConnectionStringLe ngthExceeded | ConnectionStringLengthExcee ded | The specified connection string is too long. |
| 404 | InvalidSecurityIPLis t.QuotaExceeded | InvalidSecurityIPListLength.Mal formed | The security IP address is not in the available range or occupied. |
| 404 | InvalidSecurityIPLis t.NotFound | InvalidSecurityIPs.NotFound | The specified security ip list has no matching value or at least one security IP is needed. |
| 404 | InvalidSecurityIPLis t.Duplicate | InvalidInstanceIp.Duplicate | Invalid security IP list specified, duplicated. |
| 404 | InvalidDBInstanceN etType.NotFound | InvalidDBInstanceNetType.Not Found | The specified instance network type is not found. |
| 403 | ChildDBInstanceExi sts | OperationDenied.ChildDBInsta nceExists | The specified instance had child instance. |
| 404 | GuardInstance.Exis t | InvalidGuardInstanceId.Exist | The guard instance has exist. |
| 404 | InvalidDBInstanceC lass.NotFound | InvalidDBInstanceClass.NotFou nd | The specified instance class is not found. |
| 404 | InvalidUser.NotFou nd | InvalidUser.NotFound | The specified user does not exist. |
| 404 | InvalidOperatorPer mission.NotFound | InvalidOperatorPermission.Not Found | The permission provided does not exist. |
| 404 | InvalidDBName.Not Found | InvalidDBName.NotFound | The specified database is not found. |
| 404 | ParamNotFound | Param.NotFound | The specified params is not found. |

| Developer Gu | ide·API reference |  | ApsaraDB for RD |
|---|---|---|---|
| HTTP status code | Error code | Error message | Description |
| 404 | InvalidAccountNam e.NotFound | InvalidAccountName.NotFound | The specified account is not found. |
| 500 | Invalid.Request | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | Unkown.Exception | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | Unknown.Exception | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -101 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -130 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -100 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -40 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 200 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 400 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 403 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 503 | ServiceUnavailable | ServiceUnavailable | The request has failed due to a temporary failure of the server. |
| 500 |  | InternalError | The request processing has failed due to some unknown error, exception or failure. |

#### DescribeSlowLogRecords

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DBInstanc eId | Strin g | Query | Yes | rm-uf6wjk5**** | The instance ID. You can call the DescribeDBInstances operation to query the instance ID. |
| StartTime | Strin g | Query | Yes | 2025-05-17T16:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| EndTime | Strin g | Query | Yes | 2025-05-18T16:00Z | The end of the time range to query. The end time must be later than the start time. The time span between the start time and the end time must be less than 15 days. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array | { "ONLINE": 1, "OFFLINE": 9 } | Details about the slow query logs. |
| -HostAddress | String | rm-uf6wjk5**** [****] @ [100.14.XX.XX] | The name and IP address of the client that is connected to the database. |

ApsaraDB for RDS You can call the DescribeSlowLogRecords operation to query the details of the slow query logs of an instance.

**Usage notes**

You can query a maximum of 1,000 logs. This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Developer Guide·A | PI reference |  | ApsaraDB for RD |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -DBName | String | testDB | The database name. |
| -SQLText | String | select sleep(2) | The details of the SQL statement. |
| -QueryTimes | Long | 2 | The execution duration. Unit: seconds. |
| -QueryTimeMS | Long | 2001 | The execution duration. Unit: milliseconds. |
| -LockTimes | Long | 0 | The lock duration. Unit: seconds. |
| - ParseRowCoun ts | Long | 1 | The number of rows parsed by the SQL statement. |
| - ReturnRowCou nts | Long | 1 | The number of entries returned. |
| - ExecutionStart Time | String | 2025-05- 18T01:40:44Z | The start time of the query. |
| RequestId | String | 08A3B71B-FE08- 4B03-974F- CC7EA6DB1828 | The request ID. |
| DBInstanceId | String | rm-uf6wjk5**** | The instance ID. |
| Engine | String | MySQL | The database engine of the instance. |
| TotalRecordCo unt | Integer | 3 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number. |
| PageRecordCo unt | Integer | 1 | The number of entries on the current page. |

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeSlowLogRecords &DBInstanceId=rm-uf6wjk5**** &StartTime=2025-05-17T16:00Z &EndTime=2025-05-18T16:00Z &<Common request parameters>
```

ApsaraDB for RDS Sample success responses `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalRecordCount":3,
 "PageRecordCount":1,
 "RequestId":"08A3B71B-FE08-4B03-974F-CC7EA6DB1828",
 "DBInstanceId":"rm-uf6wjk5****",
 "PageNumber":1,
 "Items":[
  {
   "QueryTimes":2,
   "ExecutionStartTime":"2025-05-18T01:40:44Z",
   "ReturnRowCounts":1,
   "LockTimes":0,
   "DBName":"testDB",
   "ParseRowCounts":1,
   "HostAddress":"rm-uf6wjk5****[****] @  [100.14.XX.XX]",
   "QueryTimeMS":2001,
   "SQLText":"select sleep(2)"
  }
```

`],`

```json
 "Engine":"MySQL"
}
```

`XML` format

```xml
<TotalRecordCount>3</TotalRecordCount> <PageRecordCount>1</PageRecordCount> <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828</RequestId> <DBInstanceId>rm-uf6wjk5****</DBInstanceId> <PageNumber>1</PageNumber> <Items>
 <QueryTimes>2</QueryTimes>
 <ExecutionStartTime>2025-05-18T01:40:44Z</ExecutionStartTime>
 <ReturnRowCounts>1</ReturnRowCounts>
 <LockTimes>0</LockTimes>
 <DBName>testDB</DBName>
 <ParseRowCounts>1</ParseRowCounts>
 <HostAddress>rm-uf6wjk5****[****] @  [100.14.XX.XX]</HostAddress>
 <QueryTimeMS>2001</QueryTimeMS>
 <SQLText>select sleep(2)</SQLText>
</Items> <Engine>MySQL</Engine>
```

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | CallEcsApi.Failure | CallEcsApi.Failure | call ecs api failure. |
| 404 | InvalidDB.NotFoun d | InvalidDB.NotFound | Specified db does not exist or DB status does not support this operation. |
| 404 | InvalidEngine.NotF ound | InvalidEngine.NotFound | Specified engine does not exist or engine version does not support this operation. |
| 400 | InvalidTask.NotFou nd | InvalidTaskId.NotFound | The "ImportId" is not found. |
| 403 | IncorrectTaskStatu s | OperationDenied.IncorrectTask Status | The operation is not permitted due to status of import. |
| 403 | IncorrectMigrationS tatus | OperationDenied.IncorrectMigr ationStatus | Migration status does not support this operation. |
| 404 | InvalidMigrationID. NotFound | InvalidMigrationID.NotFound | The specified migration record does not exist. |
| 403 | OperationDenied.P ayType | OperationDenied.PayType | The operation is not permitted due to pay type of instance. |
| 403 | GetvSwitch.Failure | OperationDenied.VSwitchNotA ccess | No availble vSwitch. |
| 403 | GetCluster.Failure | OperationDenied.ClusterNotAc cess | No availble cluster. |
| 403 | IncorrectSQLLogAct iveStatus | OperationDenied.SQLLogActiv eStatus | The operation is not permitted due to SQLLogActive status. |
| 403 | InvalidClassicNetw ork.ValueNotSuppo rted | OperationDenied.ClassicNetwo rkNotSupported | The operation is not permitted due to create classicNetwork instance. |
| 403 | InvalidDBInstanceS yncMode | OperationDenied.DBInstanceS yncMode | The operation is not permitted due to instance sync mode. |
| 403 | OperationDenied.R esource | OperationDenied.Resource | The resource is out of usage. |
| 403 | Forbidden.BidInvali d | OperationDenied.BidInvalid | The operation is not permitted due to ownerId or resourceOwnerId. |
| 403 | Forbidden.Account NoFound | OperationDenied.AccountNoFo und | The specified ownerId or resourceOwnerId is not found. |
| 403 | InvalidInstanceUse Type.NotSupport | OperationDenied.DBInstanceU seTypeNotSupport | The specified dbinstance use type is not found. |
| 400 | TIME RANGE OVER _ _ LIMIT _ | TIME RANGE OVER LIMIT _ _ _ | search time range cannot be longer than three days. |

ApsaraDB for RDS

| A | psaraDB for | RDS |  | Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | TIME RANGE OVER _ _ LIMIT.AUDIT _ | TIME RANGE OVER LIMIT.AUDI _ _ _ T | search time range cannot be longer than 7 days. |
| 400 | TIME RANGE OVER _ _ LIMIT.AUDIT DOW _ _ NLOAD | TIME RANGE OVER LIMIT.AUDI _ _ _ T DOWNLOAD _ | search time range cannot be longer than 7 days for exporting files. |
| 400 | TIME RANGE OVER _ _ LIMIT.SLOW LOG _ _ | TIME RANGE OVER LIMIT.SLO _ _ _ W LOG _ | search time range cannot be longer than 7 days. |
| 400 | TIME RANGE OVER _ _ LIMIT.ERROR LOG _ _ | TIME RANGE OVER LIMIT.ERR _ _ _ OR LOG _ | search time range cannot be longer than 7 days. |
| 400 | TOO MANY DOWN _ _ LOAD REQUEST T _ _ O OSS _ | TOO MANY DOWNLOAD REQU _ _ _ EST TO OSS _ _ | too many download request is made in 30 minutes, please wait pre request complete. |
| 400 | IGNITE LOG CLUST _ _ ER DEACTIVATED _ | IGNITE LOG CLUSTER DEACTI _ _ _ VATED | backend app is upgrading, please try again later. |
| 400 | IdempotenceParam NotMatch | IdempotenceParamNotMatch | The specified parameter not match. |
| 400 | DefaultVpc.NotSup port | DefaultVpc.NotSupport | The default VPC create is not supported. |
| 400 | Forbidden.RegionN otFound | Forbidden.RegionNotFound | The provided RegionId does not exist. |
| 400 | ClassicNetworkTyp e.NotSupport | ClassicNetworkType.NotSuppo rt | The Classic instance network create is not supported. |
| 400 | InvalidVpcIdOrVswi tchId.NotSupported | InvalidVpcIdOrVswitchId.NotSu pported | The specified vpcId or vSwitchId is not supported. |
| 400 | InvalidVpcIdRegion .NotSupported | InvalidVpcId.NotSupported | The specified vpcId or vSwitchId is not supported. |
| 400 | InvalidVSwitchId.N otSupported | InvalidVSwitchId.NotSupported | The specified VPC zone is not supported. |
| 400 | InvalidVSwitchId.N otSupported | InvalidVSwitchId.NotSupported | The specified VPC zone is not supported. |
| 400 | InvalidQuantity.Mal formed | InvalidQuantity.NotSupported | The specified instance quantity is not supported. |
| 400 | TargetSubnet.NotCl oudInstanceIp | InvalidCloudInstanceIp.NotFou nd | The specified cloud instance ip is not exist. |
| 400 | InvalidRetainInstan ce.Format | InvalidRestoreTime.Malformed | The specified retain instance is not valid. |
| 400 | InvalidRestoreTime .Format | InvalidRestoreTime.Malformed | The specified parameter "RestoreTime" is not valid. |

| Developer Gu | ide·API reference |  | ApsaraDB for RD |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidBackupSetID .NotFound | InvalidBackupId.NotFound | The BackupId provided does not exist. |
| 403 | InvalidBackup.NotF ound | OperationDenied.NotFoundBac kup | The operation is not permitted due to no backup. |
| 403 | InvalidBackupSetId OrRestoreTime.Not Found | OperationDenied.NotFoundBac kupSetIdOrRestoreTime | The operation is not permitted due to no backupSetId or restoreTime. |
| 403 | IncorrectBackupSet Method | OperationDenied.BackupMetho d | The operation is not permitted method of backup. |
| 403 | InvalidBackupLogSt atus | OperationDenied.BackupLogSt atus | The Current backup log enable status does not support this operation. |
| 403 | SecurityIPList.Dupli cate | OperationDenied.SecurityIPList Duplicate | The Specified same security IP already exists. |
| 403 | BackupSetDeleteN otSupport | OperationDenied.BackupSetDe leteNotSupport | The Specified backup does not support this operation. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 25659 | InvalidRegion.ValueNotSupport ed | The specified parameter "Region" is not valid. |
| 403 | ReadDBInstanceEx ceeded | QuotaExceeded.ReadonlyDBIn stanceCount | The quota of primary instance mounted read only instance. |
| 403 | LX RORDS BIZ MAI _ _ _ NRDS QUOTA ERR _ _ OR | QuotaExceeded.ReadonlyDBIn stanceCount | The quota of primary instance mounted read only instance. |
| 403 | LX RORDS BIZ MAI _ _ _ NRDS TYPE ERROR _ _ | OperationDenied.PrimaryDBIns tanceType | The operation is not permitted due to type of primary instance. |
| 403 | LX RDS BIZ QUER _ _ _ Y INSTANCE ERRO _ _ R | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | IZ INVALID _ | InvalidZoneId.NotFound | The provided ZoneId does not exist. |
| 404 | Abs.InvalidDBInsta nceId.Malformed | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | InvalidLogRetentio n | InvalidLogRetention.NotSuppor t | The specified log retention is not valid,The current instance type does not support this operation. |
| 403 | UploadLimitExceed ed | QuotaExceeded.Upload | The quota of file exceeds. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | -113 | ChargeTypeViolation | The operation is not permitted due to charge type of the instance. |
| 403 | LX SYSTEM _ | System.Error | The operation is error for current isntance. |
| 403 | InvalidStartTime.M alformed | InvalidStartTime.Format | The specified parameter "StartTime" is not valid. |
| 403 | InvalidEndTime.Mal formed | InvalidEndTime.Format | The specified parameter "EndTime" is not valid. |
| 400 | Abs.Engine.Malfor med | InvalidEngine.Malformed | The specified parameter "Engine" is not valid. |
| 400 | InvalidAction | InvalidAction | Specified action is not valid. |
| 400 | Abs.InvalidDBinsta nceNetType.ValueN otSupported | InvalidDBinstanceNetType.Val ueNotSupport | The specified parameter "DBinstanceNetType" is not valid. |
| 400 | Abs.InstanceUsedT ype.ValueNotSuppo rted | InvalidDBInstanceType.ValueN otSupport | The specified parameter"DBInstanceType" is not valid. |
| 400 | InvalidPageSize | InvalidPageSize | Specified parameter pageSize is not valid. |
| 400 | InvalidPageSize.Ma lformed | InvalidPageSize.Malformed | The specified parameter "PageSize" is not valid. |
| 400 | InvalidExpirePeriod .Malformed | InvalidExpirePeriod.Malformed | The specified parameter "ExpirePeriod" is not valid. |
| 400 | InvalidEngineVersio n.Malformed | InvalidEngineVersion.ValueNot Support | The specified parameter "EngineVersion" is not valid. |
| 400 | InvalidEngine.Malfo rmed | InvalidEngine.ValueNotSupport | The specified parameter "Engine" is not valid. |
| 400 | InvalidLogBackupR etentionPeriod.Malf ormed | InvalidLogBackupRetentionPeri od.Malformed | The Specified LogBackupRetentionPeriod is not valid. |
| 400 | OperationDenied.D BInstanceType | IncorrectDBInstanceType.Child DBInstanceNotSupport | The operation is not permitted due to instance type. |
| 403 | IncorrectBackupSet State | OperationDenied.BackupStatu s | The operation is not permitted due to status of instancebackup. |
| 404 | InvalidOASBackupS etID.NotFound | InvalidBackupID.NotFound | The BackupID provided does not exist. |
| 404 | OASBackupSetExtr actFinished | QuotaExceeded.BackupExtract Finished | The Specified OAS backup set had extracted finish. |

| Developer Gu | ide·API reference |  | ApsaraDB for RD |
|---|---|---|---|
| HTTP status code | Error code | Error message | Description |
| 400 | OASExtractTimesE xceeded | QuotaExceeded.OASExtractTi mesExceeded | The Current DB Instance backup set had extracted too many times from OAS today. |
| 403 | DBSizeExceeded | QuotaExceeded.DBInstanceSto rage | The quota of instance storage exceeds. |
| 400 | InvalidDBInfo.Form at | InvalidDBInfo.Malformed | The specified parameter "DBInfo" is not valid or db not exist. |
| 403 | NotValidRegion. | OperationDenied.Region | The operation is not permitted due to different region. |
| 403 | InvalidTargetDBInst anceName.Format | OperationDenied.DBInstanceId | The operation is not permitted due to DBInstanceId and SourceDBInstanceId is same. |
| 400 | InvalidFileName.Fo rmat | InvalidFileName.Malformed | The specified parameter "FileName" is not valid. |
| 404 | InvalidFileName.No tFound | InvalidFileName.NotFound | The FileName provided does not exist. |
| 400 | FileNotCompleted | InvalidFileName.NotCompleted | The specified "FileName" is not completed . |
| 400 | FileNotUploaded | InvalidFileName.NotCompleted | The specified "FileName" is not completed . |
| 400 | FileNotAvailable | InvalidFileName.NotAvailable | The specified "FileName" is not Available . |
| 403 | FileSizeExceeded | QuotaExceeded.FileSize | The quota of file size exceeds. |
| 403 | Abs.IsLockTable.Ma lformed | InvalidIsLockTable.Malformed | The specified parameter "IsLockTable" is not valid. |
| 400 | InvalidDBInstanceN ame.Format | InvalidDBInstanceId.MalForme d | The specified parameter "DBInstanceId" is not valid. |
| 400 | ParameterLeastAss ociate | ParameterLeastAssociate | Must input at least one optional parameter. |
| 400 | Abs.InvalidMaintain Time | InvalidMaintainTime.MalForme d | The specified parameter "MaintainTime" is not valid. |
| 400 | InvalidPeriod.Malfo rmed | InvalidPeriod.Malformed | The Specified parameter "Period" is not valid. |
| 400 | PARAMETER MUST _ NOT NULL _ _ | PARAMETER MUST NOT NULL _ _ _ | The parameter must not be null. |
| 400 | PARAMETER ERRO _ R | PARAMETER ERROR _ | The parameter must not be null. |

| psaraDB for | RDS |  | Developer Guide·API referenc |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | IntranetNetTypeNo tExists | IntranetNetTypeNotExists | Current DB instance network type does not support this operation. |
| 400 | InvalidVSwitchId.Mi smatch | InvalidVSwitchId.Mismatch | Specified instance and vSwitch are not in the same zone. |
| 404 | InvalidVPCId.NotFo und | InvalidVPCId.NotFound | Specified VPC ID is not found. |
| 400 | InvalidVSwitchId.N otFound | InvalidVSwitchId.NotFound | Specified vSwitch is not found in specified VPC. |
| 400 | VpcIzNoNotEqualsR dsMultIzNo | VpcIzNoNotEqualsRdsMultIzNo | Specified VPC IzNo does not equal to RDS IzNo. |
| 403 | VPC SYSTEM ERRO _ _ R | OperationDenied | VPC system error, please check params. |
| 400 | VPC CLOUD INSTA _ _ NCEIP USED _ | InvalidPrivateIpAddress.Duplic ated | Specified private IP address is duplicated. |
| 400 | Invalid.TargetCloud InstanceIp | InvalidPrivateIpAddress.Misma tch | Specified private IP address is not in the CIDR block of virtual switch. |
| 400 | IncorrecttVpcId | IncorrectVpcId.Mismatch | The specified parameter "VpcId " is not valid. |
| 400 | IncorrectInstanceN etworkType | InvalidInstanceNetworkType.V alueNotSupported | The specified parameter "InstanceNetworkType" is not valid. |
| 403 | InvalidCloudInstanc eId.Duplicated | OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. |
| 400 | InvalidIzNo.NotSup ported | InvalidIzNo.NotSupported | Specified VCP zone is not supported. |
| 403 | OperationDenied.S witchToVPC | OperationDenied.Switch | Specified instance cannot be switched to VPC. |
| 404 | InvalidCloudInstanc e.ID | InvalidDBInstanceName.NotFo und | The DBInstanceId provided does not exist. |
| 403 | SlaveLagExceeded | Exceeded.SlaveLag | The slave lag exceeds. |
| 403 | LockTimeout | LockTimeout | The request processing has failed due to lock timeout. |
| 403 | BackupTimesExcee ded | Exceeded.BackupTimes | The backup times exceeds. |
| 404 | Abs.dbInstanceId.N otFound | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |

| Developer Gu | ide·API reference |  | ApsaraDB for RD |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | INST NOT BELONG _ _ TO USER _ _ | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26915 | InvalidDBInstanceStorage.Valu eNotSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | MissingParameter | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | LX RDS BIZ INSTA _ _ _ NCE UPGRADE ER _ _ ROR | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | Abs.dbInstanceClas sOrdbInstanceStor age.MissParameter | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | LX BARDS BIZ UP _ _ _ GRADE INSTANCE _ _ ERROR | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 400 | Abs.InstanceUsedT ype.ValueNotSuppo rted | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | LX BARDS BIZ UP _ _ _ GRADE STORAG _ | OperationDenied.DBInstanceSt orageReduce | The operation is not permitted due to reduce storage. |
| 403 | LX BARDS BIZ UP _ _ _ GRADE STORAGE _ _ ERROR | OperationDenied.DBInstanceSt orageReduce | The operation is not permitted due to reduce storage. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26914 | InvaildDBInstanceClassInRegio n.NotAvailable | The DBInstanceClass in the Region is not available. |
| 403 | LX RDS BIZ STATU _ _ _ S ERROR _ | OperationDenied.DBInstanceSt atus | The operation is not permitted due to instance status. |
| 400 | ILLEGAL ARGUMEN _ T | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | InvalidSourceDatab aseUserName.Malf ormed | InvalidDBInfo.Format | The specified parameter "SourceDatabaseUserName" is not valid. |
| 400 | InvalidQueryTime.F ormat | InvalidQueryTime.Format | he specified parameter "QueryTime" is not valid. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | Abs.SourceDatabas ePort.Malformed | InvalidSourceDatabasePort.Mal formed | The specified parameter 'SourceDatabasePort' is not valid. |
| 400 | Abs.ImportDataTyp e.Malformed | InvalidImportDataType.Malfor med | The specified parameter 'ImportDataType' is not valid. |
| 400 | ClusterDRCNotSup oort | OperationDenied.DBInstnceInR egion | The operation is not permitted due to DBInstance in the region. |
| 404 | InvalidOrderCharge .NotSupport | InvalidOrderCharge.NotSuppor t | The specified order charge does not support in RDS. |
| 404 | IncorrectInstanceU seType | InvalidDBInstanceIdUseType | InvalidDBInstanceIdUseType. |
| 403 | IncorrectMigrationI D | InvalidImportId.ImportIdvalue | The operation is not permitted due to ImportId value. |
| 403 | InvalidSwitchType | InvalidSwitchType.Malformed | The specified parameter InvalidSwitchType is not valid. |
| 403 | HaStatusNotSuppor t | OperationDenied.HaStatus | The operation is not permitted due to hastatus no supported. |
| 404 | QuotaExceeded.Ta gOnDBInstance | QuotaExceeded.TagOnDBInsta nce | The quota of tag on DBInstance exceeds. |
| 400 | Tag.Mismatch | Tag.Mismatch | Tag-Key and InvalidDBInstanceName.NotFo undag-Value is mismatch. |
| 400 | InvalidTag.1.key.M alformed | InvalidTag.1.key.Malformed | The specified parameter 'Tag.1.key' is not valid. |
| 400 | InvalidTag.2.key.M alformed | InvalidTag.2.key.Malformed | The specified parameter 'Tag.2.key' is not valid. |
| 400 | InvalidTag.3.key.M alformed | InvalidTag.3.key.Malformed | The specified parameter 'Tag.3.key' is not valid. |
| 400 | InvalidTag.4.key.M alformed | InvalidTag.4.key.Malformed | The specified parameter 'Tag.4.key' is not valid. |
| 400 | InvalidTag.5.key.M alformed | InvalidTag.5.key.Malformed | The specified parameter 'Tag.5.key' is not valid. |
| 400 | InvalidTag.1.value. Malformed | InvalidTag.1.value.Malformed | The specified parameter 'Tag.1.value' is not valid. |
| 400 | InvalidTag.2.value. Malformed | InvalidTag.2.value.Malformed | The specified parameter 'Tag.2.value' is not valid. |
| 400 | InvalidTag.3.value. Malformed | InvalidTag.3.value.Malformed | The specified parameter 'Tag.3.value' is not valid. |

ApsaraDB for RDS

|  | Developer Gu | ide·API reference |  | ApsaraDB for RD | S |
|---|---|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidTag.4.value. Malformed | InvalidTag.4.value.Malformed | The specified parameter 'Tag.4.value' is not valid. |
| 400 | InvalidTag.5.value. Malformed | InvalidTag.5.value.Malformed | The specified parameter 'Tag.5.value' is not valid. |
| 400 | TAG KEY ILLEGAL _ _ | Tag.Malformed | The specified parameter Tag is not valid. |
| 400 | TAG VALUE ILLEGA _ _ L | Tag.Malformed | The specified parameter Value is not valid. |
| 400 | Tag.NoRegionIdExi st | Tag.NoRegionIdExist | the region Id can not be blank. |
| 400 | Tag.NoTagInfoExist | Tag.NoTagInfoExist | all the tags and tagN parameters is null. |
| 400 | Tag.TagKeyCanNot BeAll | Tag.TagKeyCanNotBeAll | tag key can not be all. |
| 400 | Tag.TagKeyDuplex | Tag.TagKeyDuplex | tag key must be sole in one operation. |
| 400 | Tag.NoDBInstanceI dExist | Tag.NoDBInstanceIdExist | the dbinstance Id can not be blank. |
| 400 | Tag.TooManyDBIns tanceIds | Tag.TooManyDBInstanceIds | the dbinstance Ids is more than 30. |
| 400 | Tag.TooManyTagsF orOneInstance | Tag.TooManyTagsForOneInsta nce | total 10 tags can be added to one resource. |
| 400 | Tag.SetTagInfoAtT woParamters | Tag.SetTagInfoAtTwoParamter s | only tags or tagN parameter could be setted. |
| 400 | Tag.Allow5TagInfos | Tag.Allow5TagInfos | only 5 tags allowed in one operation. |
| 400 | Tag.TagKeyIsBlank | Tag.TagKeyIsBlank | tag key can not be blank. |
| 400 | Tag.TagKeyStartWi th.aliyun | Tag.TagKeyStartWith.aliyun | tag key and value can not be started with aliyun. |
| 400 | Tag.TagKeyTooLon g | Tag.TagKeyTooLong | the max tag key's length is 64. |
| 400 | Tag.TagValueTooLo ng | Tag.TagValueTooLong | the max tag value's length is 128. |
| 400 | Tag.InvalidTagsPar amter | Tag.InvalidTagsParamter | tags paramter is invalid. |
| 400 | Abs.InvalidTimePeri od | OperationDenied.TimePeriod | The specified parameter "TimePeriod" is not valid. |

| psaraDB for | RDS |  | Developer Guide·API referenc |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | Abs.InvalidStartTim e | InvalidStartTime.Malformed | The specified parameter "StartTime" is not valid. |
| 400 | Abs.InvalidEndTime | InvalidEndTime.Malformed | The specified parameter "EndTime" is not valid. |
| 403 | EnabledSSLNotSup port | OperationDenied.EnabledSSLN otSupport | The specified parameter "EnabledSSL" is not valid. |
| 403 | InvalidRequest.Not Finished | OperationDenied.RequestNotFi nished | The specified request not finished. |
| 403 | InvalidRequest.Exis ts | OperationDenied.RequestExist s | The specified request already exists. |
| 400 | Abs.instanceNames .Malformed | InvalidDBInstanceId.QuotaExc eeded | The quota of instance ID exceeded. |
| 400 | InvalidOrderTask.N otSupport | InvalidOrderTask.NotSupport | The Current InstanceId exist Order Task in RDS. |
| 400 | RenewChange.Exis t | RenewChange.Exist | The Current InstanceId exist renewChange order in RDS. |
| 400 | INVITATION CODE _ _ BIZ FAIL _ | InvalidEActionCode.CodeBizNo tSupported | The specified action code biz is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26080 | InvalidEngine.VauleNotSupport ed | The specified parameter "Engine" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26063 | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26035 | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26036 | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | InvalidEngineVersio n.ValueNotSupport ed | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26062 | InvalidDBInstanceClass.ValueN otSupported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | Abs.dbInstanceClas s.NotFound | InvalidDBInstanceClass.ValueN otSupported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ MissingParameter | InvalidDBInstanceClass.ValueN otSupported | The specified parameter "DBInstanceClass" is not valid. |

| Developer Gu | ide·API reference |  | ApsaraDB for RD |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26037 | InvalidDBInstanceStorage.Valu eNotSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | InvalidDBInstanceS torage.ValueNotSu pported | InvalidDBInstanceStorage.Valu eNotSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | Abs.dbInstanceNet Type.ValueNotSupp orted | InvalidDBInstanceNetType.Val ueNotSupported | The specified parameter "InvalidDBInstanceNetType" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ | FUWU BIZ COMMODITY VERIF _ _ _ Y FAIL _ | Oops, unable to complete your payment. The reason for this error may be due to one of the following: 1. Your bank account funds are insufficient. 2. Your account is not yet verified. 3. You have already exceeded the maximum limit of RDS instances. |
| 400 | QUERY PRICE RES _ _ PONSE ERROR _ | QueryPriceResonse.Failed | query price response error. |
| 400 | LX CREATE ORDER _ _ FAILED _ | CreateOrder.Failed | Create order failed. |
| 404 | InvalidRegion.NotF ound | InvalidRegionId.NotFound | The provided RegionId does not exist. |
| 404 | INQUERY ORDER F _ _ EE FAILED _ | QueryPrice.Failed | QueryPrice Failed. |
| 404 | InvalidRegionId.Not Found | InvalidRegionId.NotFound | The provided RegionId is not found. |
| 404 | InvalidRegion Zone _ NotFound _ | InvalidRegionId.NotFound | The provided RegionId is not found. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26038 | InvalidRegionId.NotFound | The RegionId provided does not exist. |
| 400 | Abs.dbInstanceDes cription.Malformed | InvalidDBInstanceDescription. Malformed | The specified parameter "DBInstanceDescription" is not valid. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26044 | InvalidEngineVersionInRegion. NotAvailable | The EngineVersion in the Region is not available. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26045 | InvalidEngineVersionInRegion. NotAvailable | The EngineVersion in the Region is not available. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26175 | InvaildEngineInRegion.NotAvail able | The engine type in this region is not available. |
| 403 | InvalidUserRegionP rivilege.Malformed | RegionUnauthorized | There is no authority to create instance in the specified region. |
| 403 | LX USER BUY COM _ _ _ MODITY COUNT EX _ _ CEEDED LIMIT _ | QuotaExceeded.CreateInstanc e | The quota of create instance exceeds. |
| 403 | INST HAS UNPAID _ _ _ ORDER | INST HAS UNPAID ORDER _ _ _ | The instanceId has unpaid order. |
| 403 | GET COMMODITY F _ _ AILED | COMMODITY.FAILED | The commodity is error. |
| 403 | MONEY LESSTHAN _ _ 100 | MoneyLessThan100 | The Account Monet less Than 100. |
| 403 | InvalidOrderCharge .NotPay | InvalidOrderCharge.NotPay | The specified parameter OrderCharge is not pay. |
| 400 | Abs.MissingOwnerI dOrOwnerAccount | MissingParameter | The input parameter "OwnerId" or "OwnerAccount" that is mandatory for processing this request is not supplied. |
| 400 | UnsupportedParam eter | UnsupportedParameter | Unsupported parameter. |
| 400 | InvalidDBInstanceC onnType.Format | InvalidDBInstanceConnType.Fo rmat | The specified instance connection type is not valid. |
| 400 | InvalidSecurityIPLis t.Format | InvalidSecurityIps.MalFormed | The specified parameter "SecurityIps" is not valid. |
| 400 | InvalidBackupSetLo cation | InvalidBackupLocation.Malform ed | The specified parameter "BackupLocation" is not valid. |
| 400 | InvalidParameters. Format | InvalidParameters.Malformed | The specified parameter "Parameters" is not valid. |
| 400 | InvalidConfigValue | InvalidSQLCollectorStatus.Valu eNotSupported | The specified SQLCollectorStatus value not support. |
| 400 | InvalidSqlLog.Malfo rmed | InvalidSQLCollectorStatus.Malf ormed | The specified parameter "SQLCollectorStatus" is not valid. |
| 400 | QuotaExceeded.Sta rtDiagnose | QuotaExceeded.StartDiagnose | The quota of start diagnose exceeds now,try again later. |
| 400 | TaskExists | TaskExists | Specified task have existed. |

ApsaraDB for RDS

| Developer Gu | ide·API reference |  | ApsaraDB for RD |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidDBInstanceD escription.Format | InvalidDBInstanceDescription. Malformed | The specified parameter "DBInstanceDescription" is not valid. |
| 400 | InvalidConnectionS tring.Format | InvalidConnectionString.Malfor med | The specified parameter "ConnectionStringPrefix" is not valid. |
| 400 | InvalidGroupName. Format | InvalidGroupName.Malformed | The specified parameter "DBInstanceIPArrayName" is not valid. |
| 400 | Abs.backupSetStat us.ValueNotSuppor ted | InvalidBackupStatus.ValueNot Support | The specified parameter "BackupStatus" is not valid. |
| 400 | Abs.jobMode.Value NotSupported | InvalidBackupMode.ValueNotS upport | The specified parameter "BackupMode" is not valid. |
| 400 | Abs.InvalidDescript ion.Malformed | InvalidDBDescription.Malforme d | The specified parameter "DBDescription" is not valid. |
| 400 | Abs.backupTime.Va lueNotSupported | InvalidPreferredBackupTime.M alformed | The specified parameter "PreferredBackupTime" is not valid. |
| 400 | Abs.backupPeriod. Malformed | InvalidPreferredBackupPeriod. Malformed | The specified parameter "PreferredBackupPeriod" is not valid. |
| 400 | InvalidAccountNam e.Format | InvalidAccountName.Malforme d | The specified parameter "AccountName" is not valid. |
| 400 | InvalidAccountNam e.Forbid | InvalidAccountName.keyword | The specified parameter "AccountName" is a keyword. |
| 400 | InvalidAccountNam e.Duplicate | InvalidAccountName.Duplicate | Invalid "AccountName" specified, duplicated. |
| 400 | InvalidAccountPass word.Format | InvalidAccountPassword.Malfor med | The specified parameter "AccountPassword" is not valid. |
| 400 | AccountLimitExcee ded | QuotaExceeded.AccountName | Account limit exceeded. |
| 400 | SwitchTimesLimitE xceeded | QuotaExceeded.SwitchTime | SwitchTimes limit exceeded. |
| 400 | InvalidTDEstatus.F ormat | InvalidTDEstatus.Format | The specified TDEStatus is not valid. |
| 400 | InvalidConnectionM ode | InvalidConnectionMode.ValueN otSupported | The specified parameter "ConnectionMode" is not valid. |
| 400 | InvalidAccountPrivil ege.Malformed | InvalidAccountPrivilege.ValueN otSupport | The specified "AccountPrivilege" is not valid. |

| psaraDB for | RDS |  | Developer Guide·API referenc |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorrectEngineVer sion | InvaildEngineInRegion.ValueNo tSupported | The engine is not supported in the region. |
| 400 | InvalidDBName.For mat | InvalidDBName.Malformed | The specified parameter "DBName" is not valid. |
| 400 | DBLimitExceeded | QuotaExceeded.DBName | The database operation execeed. |
| 400 | InvalidDBName.Du plicate | InvalidDBName.Duplicate | The Security db Name is not in the available range or occupied. |
| 400 | InvalidCharacterSe tName.Format | InvalidCharsetName.ValueNotS upport | The specified parameter "CharsetName" is not valid. |
| 400 | InvalidDBDescriptio n.Format | InvalidDBDescription.Malforme d | The specified parameter "DBDescription" is not valid. |
| 400 | InvalidDBName.For bid | InvalidParameter.Keyword | The specified parameter "DBName" is keyword. |
| 400 | InvalidUserType.No tSupport | InvalidUserType.NotSupport | The operation is not permitted due to type of account. |
| 400 | InvalidExpiredTime .Format | InvalidExpiredTime.Malformed | The specified "ExpiredTime" is not valid. |
| 400 | InvalidBackupMeth od.Format | InvalidBackupMethod.ValueNot Support | The specified parameter "BackupMethod" is not valid. |
| 400 | InvalidBackupLog. Malformed | InvalidBackupLog.Malformed | The specified parameter "backupPeriod" is not valid. |
| 400 | InvalidStartTime.Fo rmat | InvalidStartTime.Malformed | The specified parameter "StartTime" is not valid. |
| 400 | InvalidEndTime.For mat | InvalidEndTime.Malformed | The specified parameter "EndTime" is not valid. |
| 400 | InvalidMaxRecords PerPage.Malformed | InvalidPageSize.Malformed | The specified parameter "PageSize" is not valid. |
| 400 | InvalidSortKey.Malf ormed | InvalidSortKey.Malformed | The specified parameter "SortKey" is not valid. |
| 400 | InvalidSortMethod. Malformed | InvalidSortMethod.Malformed | The specified parameter "SortMethod" is not valid. |
| 400 | InvalidParameter | InvalidParameter | Invalid parameter. |
| 400 | InvalidPort.Malform ed | InvalidPort.Malformed | The specified parameter "Port" is not valid. |
| 400 | InvalidKey.Malform ed | InvalidPerformanceKey.Malfor med | The specified parameter "Key" is not valid. |

|  | Developer Gu | ide·API reference |  | ApsaraDB for RD | S |
|---|---|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidQueryKeywo rd.NotSupport | InvalidQueryKeyword.Malform ed | the query key contains exception character. |
| 400 | InvalidParameterCo mbination | InvalidStartTimeAndEndTime. Malformed | The end time must be greater than the start time. |
| 400 | InvalidParameter.R esourceOwnerAcco unt | InvalidParameter.ResourceOw nerAccount | The specified parameter "resourceOwnerAccount" is not valid. |
| 400 | InvalidStorage.For mat | InvalidStorage.Format | The specified "storage" is not valid. |
| 403 | Abs.ApiForbiddenB ySubBid | ActionUnauthorized | The specified action is not available for you. |
| 403 | Forbidden | Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. |
| 403 | RAM.ApiNotSupport ed | Forbidden.NotSupportRAM | This action does not support accessed by RAM mode. |
| 403 | RISK CONTROL RE _ _ SULT FAIL _ | Forbidden.RiskControl | This operation is forbidden by aliyun risk control system. |
| 403 | InvalidRegion.NotS upport | OperationDenied.NotSupport | the specified instance region does not support this operation. |
| 403 | IncorrectDBInstanc eLockMode | OperationDenied.LockMode | The operation is not permitted due to instance being locked. |
| 403 | IncorrectDBInstanc eState | OperationDenied.DBInstanceSt atus | The operation is not permitted due to status of instance. |
| 403 | IncorrectDBInstanc eType | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | ChildDBInstanceNo tSupport | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | GuardDBInstanceN otSupport | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | ReadDBInstanceNo tSupport | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | IncorrectDBInstanc eEngine | OperationDenied.DBInstanceE ngine | The operation is not permitted due to engine of instance. |
| 403 | IncorrectDBInstanc eNetType | OperationDenied.DBInstanceN etType | The operation is not permitted due to network type of the instance. |
| 403 | IncorrectDBInstanc eConnType | OperationDenied.PublicConnec tionExists | The specified public connection already existed. |

| psaraDB for | RDS |  | Developer Guide·API referenc |
|---|---|---|---|
| HTTP status code | Error code | Error message | Description |
| 403 | InsufficientResourc eCapacity | OperationDenied | The resource is out of usage. |
| 403 | ClusterNotSupport | OperationDenied.ClusterNotSu pport | The instance cluster does not support this operation. |
| 403 | IncorrectDBInstanc e | OperationDenied.DBInstance | The operation is not permitted due to type of the instance. |
| 403 | IncorrectGuardDBI nstanceVersion | OperationDenied.GuardDBInst anceLower | The operation is not permitted due to higher guard instance version. |
| 403 | IncorrectMasterDBI nstanceState | OperationDenied.MasterDBInst anceState | The operation is not permitted due to status of master instance. |
| 403 | IncorrectAccountSt atus | OperationDenied.AccountStatu s | The operation is not permitted due to status of account. |
| 403 | IncorrectAccountTy pe | OperationDenied.AccountType | The operation is not permitted due to type of account. |
| 403 | ConcurrentTaskExc eeded | OperationDenied.TaskExceede d | The concurrent tasks exceeded allowed amount. |
| 403 | IncorrectDBInstanc eAccountMode | OperationDenied.AccountMode | The operation is not permitted due to account mode of instance. |
| 403 | DBNameAndAccou ntPrivilegeCount | OperationDenied.DBNameAnd AccountPrivilegeCount | The operation is not permitted due to count of database or account privilege. |
| 403 | OldPasswordWrong | OperationDenied.PasswordWro ng | The operation is not permitted due to wrong of password. |
| 403 | IncorrectDBType | OperationDenied.DBType | The operation is not permitted due to type of the database. |
| 403 | IncorrectDBState | OperationDenied.DBStatus | The operation is not permitted due to status of the database. |
| 403 | BackupJobExists | OperationDenied.BackupJobExi sts | The operation is not permitted due to backup job exist. |
| 400 | Abs.backupMethod. ValueNotSupported | InvalidBackupMethod.ValueNot Support | The specified parameter "BackupMethod" is not valid. |
| 400 | Abs.backupType.Va lueNotSupported | InvalidBackupType.ValueNotSu pport | The specified parameter "BackupType" is not valid. |
| 404 | INSUFFICIENT BAL _ ANCE | InsufficientBalance | Your account does not have enough balance. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL I _ _ _ NSUFFICIENT BALA _ NCE | InsufficientBalance | Your account does not have enough balance. |
| 400 | INSTANCE PRODUC _ E FAILED _ | CreateOrder.Failed | The instance order is error. |
| 404 | InvalidDBInstanceN ame.NotFound | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | InvalidInstanceId | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | InvalidDB.NotFoun d | InvalidDB.NotFound | The Specified db does not exist or DB status does not support. |
| 404 | InvalidDBInstance. NotFound | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | RAM.InstanceNotFo und | Forbidden.InstanceNotFound | The specified instance is not found. |
| 404 | InvalidConnectionS tring.Duplicate | InvalidConnectionStringPrefix. Duplicated | Specified connection string needs to be same as current network type. |
| 404 | AtLeastOneNetTyp eExists | AtLeastOneNetTypeExists | The specified network type at least one. |
| 404 | NetTypeExists | NetTypeExists | The specified public network type already exists. |
| 404 | InvalidConnectionS tringOrPort.Duplica te | InvalidConnectionString.Duplic ate | Specified connection string or port needs to be same as current network type. |
| 404 | InvalidConnectionS tring.NotFound | InvalidConnectionString.NotFo und | The specified connection string or network type is not found. |
| 404 | ConnectionStringLe ngthExceeded | ConnectionStringLengthExcee ded | The specified connection string is too long. |
| 404 | InvalidSecurityIPLis t.QuotaExceeded | InvalidSecurityIPListLength.Mal formed | The security IP address is not in the available range or occupied. |
| 404 | InvalidSecurityIPLis t.NotFound | InvalidSecurityIPs.NotFound | The specified security ip list has no matching value or at least one security IP is needed. |
| 404 | InvalidSecurityIPLis t.Duplicate | InvalidInstanceIp.Duplicate | Invalid security IP list specified, duplicated. |
| 404 | InvalidDBInstanceN etType.NotFound | InvalidDBInstanceNetType.Not Found | The specified instance network type is not found. |

ApsaraDB for RDS

| psaraDB for | RDS |  | Developer Guide·API referenc |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | ChildDBInstanceExi sts | OperationDenied.ChildDBInsta nceExists | The specified instance had child instance. |
| 404 | GuardInstance.Exis t | InvalidGuardInstanceId.Exist | The guard instance has exist. |
| 404 | InvalidDBInstanceC lass.NotFound | InvalidDBInstanceClass.NotFou nd | The specified instance class is not found. |
| 404 | InvalidUser.NotFou nd | InvalidUser.NotFound | The specified user does not exist. |
| 404 | InvalidOperatorPer mission.NotFound | InvalidOperatorPermission.Not Found | The permission provided does not exist. |
| 404 | InvalidDBName.Not Found | InvalidDBName.NotFound | The specified database is not found. |
| 404 | ParamNotFound | Param.NotFound | The specified params is not found. |
| 404 | InvalidAccountNam e.NotFound | InvalidAccountName.NotFound | The specified account is not found. |
| 500 | Invalid.Request | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | Unkown.Exception | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | Unknown.Exception | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -101 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -130 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -100 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -40 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 200 | InternalError | The request processing has failed due to some unknown error, exception or failure. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 400 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 403 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 503 | ServiceUnavailable | ServiceUnavailable | The request has failed due to a temporary failure of the server. |
| 500 |  | InternalError | The request processing has failed due to some unknown error, exception or failure. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeErrorLo gs | The operation that you want to perform. Set the value to DescribeErrorLogs. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| EndTime | String | Yes | 2011-05- 30T20:10Z | The end of the time range to query. The end time must be later than the start time. The time span between the start time and the end time must be less than 31 days. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| StartTime | String | Yes | 2011-05- 01T20:10Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |

#### DescribeErrorLogs

Queries the error logs of an ApsaraDB RDS instance within a specific time range. Error logs contain the time when they were generated and the error messages.

**Request parameters**

| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid value: 30 to 100. Default value: 30. |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalRecordCo unt | Integer | 100 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 30 | The number of error logs on the current page. |
| Items | Array of ErrorLog |  | Details of error logs. |
| ErrorLog |  |  |  |
| ErrorInfo | String | spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an informational message only; no user action is required | The error message. |
| CreateTime | String | 2011-05- 30T12:11:04Z | The time when the error log was generated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| RequestId | String | 98504E07-BB0E- 40FC-B152- E4882615812C | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeErrorLogs &DBInstanceId=rm-uf6wjk5xxxxxxx &StartTime=2011-05-01T20:10Z &EndTime=2011-05-30T20:10Z &<Common request parameters>
```

ApsaraDB for RDS Sample success responses `XML` format

```xml
      <RequestId>98504E07-BB0E-40FC-B152-E4882615812C</RequestId>
      <PageNumber>1</PageNumber>
      <TotalRecordCount>1</TotalRecordCount>
      <PageRecordCount>1</PageRecordCount>
      <Items>
            <ErrorLog>
                  <ErrorInfo>spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This
is an informational message only; no user action is required</ErrorInfo>
                  <CreateTime>2013-06-04T15:00:00</CreateTime>
            </ErrorLog>
      </Items>
```

`JSON` format

```json
{ "RequestId":"98504E07-BB0E-40FC-B152-E4882615812C", "PageNumber":1, "TotalRecordCount":1, "PageRecordCount":1, "Items": {"ErrorLog":
```

[

```json
{ "ErrorInfo":"spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an informat ional message only; no user action is required", "CreateTime":"2013-06-04T15:00:00" }
```

]

```
} }
```

#### DescribeBinlogFiles

Queries the log backup files of an ApsaraDB RDS instance. If the **DownloadLink** value is null, ApsaraDB RDS does not provide a download URL. If the **DownloadLink** value is not null, ApsaraDB RDS provides a download URL for a log backup file. The expiration time of the URL is specified by the **LinkExpiredTime** parameter. You must download the log backup file before the expiration time. This operation returns SQL log entries that are generated over a specific time range. The beginning of the time range must be earlier than or equal to the time that is specified by the LogEndTime parameter. In addition, the end of the time range must be later than or equal to the time that is specified by the LogBeginTime parameter.

**Note**

This operation is not supported for instances that run SQL Server.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBinlogFi les | The operation that you want to perform. Set the value to DescribeBinlogFiles. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| EndTime | String | Yes | 2011-06- 20T15:00:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| StartTime | String | Yes | 2011-06- 01T15:00:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid value: 30 to 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalRecordCo unt | Integer | 100 | The total number of log backup files returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 30 | The number of log backup files returned on the current page. |
| Items | Array of BinLogFile |  | Details of log backup files. |
| BinLogFile |  |  |  |

ApsaraDB for RDS

**Request parameters**

**Response parameters**

| FileSize | Long | 2269410 | The size of the log backup file. Unit: byte. |
|---|---|---|---|
| LogBeginTime | String | 2019-02- 09T17:45:21Z | The start time of the log data recorded in the log backup file. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| LogEndTime | String | 2019-02- 15T13:10:28Z | The end time of the log data recorded in the log backup file. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DownloadLink | String | http://rdsxxxxx.oss. aliyuncs.com/xxxx xx | The HTTP download URL. If this parameter is set to null, no download link is available. |
| HostInstanceI D | String | 5841973 | The number of the instance to which the log backup file belongs. This parameter is used to indicate whether the log backup file is generated on a primary instance or a secondary instance. |
| LinkExpiredTi me | String | 2013-06- 09T18:00:00Z | The expiration time of the URL. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Checksum | String | 183583043934687 01857 | The checksum. |
| IntranetDownl oadLink | String | http://rdslog-hz- v3.oss-cn- hangzhou- internal.aliyuncs.co m/xxxxxx | The download URL that is used over an internal network. |
| LogFileName | String | 000000040000000 000000019 | The name of the log backup file. |
| RequestId | String | ED169A3E-1657- 4104-82AB- 24EA8CD0DB75 | The ID of the request. |
| TotalFileSize | Long | 2269410 | The total size of the log backup files returned. |

ApsaraDB for RDS

**Examples**

Sample requests

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSQLColl ectorPolicy | The operation that you want to perform. Set the value to DescribeSQLCollectorPolicy. |

ApsaraDB for RDS

```
http(s)://rds.example.com/?Action=DescribeBinlogFiles &DBInstanceId=rm-uf6wjk5xxxxxxx &StartTime=2011-06-01T15:00:00Z &EndTime=2011-06-20T15:00:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <Items></Items>
      <PageNumber>1</PageNumber>
      <TotalRecordCount>0</TotalRecordCount>
      <TotalFileSize>0</TotalFileSize>
      <RequestId>ED169A3E-1657-4104-82AB-24EA8CD0DB75</RequestId>
      <PageRecordCount>0</PageRecordCount>
```

`JSON` format

```json
{
    "Items": {
        "BinLogFile": []
    },
    "PageNumber": 1,
    "TotalRecordCount": 0,
    "TotalFileSize": "0",
    "RequestId": "ED169A3E-1657-4104-82AB-24EA8CD0DB75",
    "PageRecordCount": 0
}
```

#### DescribeSQLCollectorPolicy

Queries the status of the SQL Explorer (SQL Audit) feature on an ApsaraDB RDS instance. Before you call this operation, make sure that the ApsaraDB RDS instance runs one of the following database engines: MySQL PostgreSQL PolarDB

**Request parameters**

| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
|---|---|---|---|---|
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| SQLCollectorSt atus | String | Enable | The status of the SQL Explorer (SQL Audit) feature. Valid values: Enable Disabled |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |
| StoragePeriod | Integer | 0 | None |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeSQLCollectorPolicy &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <requestId>C3565F9F-76E9-4F7E-A662-D1B2488EC2FC</requestId>
      <SQLCollectorStatus>Enable</SQLCollectorStatus>
```

`JSON` format

```json
{
    "requestId": "C3565F9F-76E9-4F7E-A662-D1B2488EC2FC",
    "SQLCollectorStatus": "Enable"
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySQLCollec torPolicy | The operation that you want to perform. Set the value to ModifySQLCollectorPolicy. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| SQLCollectorStat us | String | Yes | Enable | Specifies whether to enable or disable the SQL Explorer (SQL Audit) feature. Valid values: Enable and Disabled. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| StoragePeriod | Integer | No | 0 | An invalid parameter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

ApsaraDB for RDS

#### ModifySQLCollectorPolicy

Enables or disables the SQL Explorer (SQL Audit) feature for an ApsaraDB RDS instance. Before you call this operation, make sure that the ApsaraDB RDS instance runs one of the following database engines: MySQL PostgreSQL PolarDB

**Request parameters**

**Response parameters**

**Examples**

Sample requests

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSQLLog Records | The operation that you want to perform. Set the value to DescribeSQLLogRecords. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| EndTime | String | Yes | 2011-06- 11T15:00:00Z | The end of the time range to query. The end time must be later than the start time. The time span between the start time and the end time must be less than 31 days. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. |

ApsaraDB for RDS

```
http(s)://rds.example.com/?Action=ModifySQLCollectorPolicy &DBInstanceId=rm-uf6wjk5xxxxxxx &SQLCollectorStatus=Enable &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <requestId>C3565F9F-76E9-4F7E-A662-D1B2488EC2FC</requestId>
```

`JSON` format

```json
{
    "requestId": "C3565F9F-76E9-4F7E-A662-D1B2488EC2FC",
}
```

#### DescribeSQLLogRecords

Queries the logs that are generated by the SQL Explorer (SQL Audit) feature on an ApsaraDB RDS instance. Before you call this operation, make sure that the ApsaraDB RDS instance runs one of the following database engines: MySQL PostgreSQL PolarDB

**Request parameters**

| StartTime | String | Yes | 2011-06- 01T15:00:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
|---|---|---|---|---|
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| SQLId | Long | No | 25623548 | The unique ID of the SQL statement. |
| QueryKeywords | String | No | rds | The keywords that are used for the query. Separate multiple keywords with spaces. A maximum of 10 keywords are allowed. |
| Database | String | No | Database | The name of the database. If you specify this parameter, this operation returns only the log entries that are generated for the specified database. If you do not specify this parameter, this operation returns the log entries that are generated for all databases on the instance. |
| User | String | No | user | The name of the database account to query. If you specify this parameter, this operation returns only the log entries that are generated for the specified database account. If you do not specify this parameter, this operation returns the log entries that are generated for all database accounts on the instance. |
| Form | String | No | Stream | Specifies whether to generate SQL audit log files or return SQL audit log entries. Default value: Stream. Valid values: File: generates audit log files. If you set this parameter to File, only common response parameters are returned. You must call the DescribeSQLLogFiles operation to obtain the download URL of audit log files. Stream: returns SQL audit log entries. |

ApsaraDB for RDS

| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid value: 30 to 100. Default value: 30. |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalRecordCo unt | Integer | 100 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 30 | The number of SQL audit logs on the current page. |
| Items | Array of SQLRecord |  | Details of SQL audit logs. |
| SQLRecord |  |  |  |
| DBName | String | testDB | The name of the database. |
| AccountName | String | accounttest | The name of the account that was used to execute the SQL statement. |
| HostAddress | String | 192.168.0.121 | The IP address of the client that was connected to the database. |
| SQLText | String | update test.zxb set id=0 limit 1 | The SQL statement returned. |
| TotalExecution Times | Long | 600 | The execution duration of the SQL statement. Unit: microseconds. |
| ReturnRowCou nts | Long | 30 | The number of entries returned. |
| ThreadID | String | 1025865428 | The thread ID. |

ApsaraDB for RDS

**Response parameters**

| ExecuteTime | String | 2011-06- 11T15:00:23Z | The time when the SQL statement was executed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
|---|---|---|---|
| RequestId | String | 08A3B71B-FE08- 4B03-974F- CC7EA6DB1828 | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeSQLLogRecords &DBInstanceId=rm-uf6wjk5xxxxxx &StartTime=2011-06-01T15:00:00Z &EndTime=2011-06-11T15:00:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <PageNumber>1</PageNumber>
      <TotalRecordCounts>1</TotalRecordCounts>
      <ItemsCounts>1</ItemsCounts>
      <SQLItems>
            <SQLItem>
                  <DBName>test</DBName>
                  <AccountName>accounttest</AccountName>
                  <HostAddress>192.168.0.121</HostAddress>
                  <SQLText>update test.zxb set id=0 limit 1</SQLText>
                  <TotalExecutionTimes>12</TotalExecutionTimes>
                  <ReturnRowCounts>34</ReturnRowCounts>
                  <ExecuteTime>2011-06-11T15:00:23Z</ExecuteTime>
            </SQLItem>
      </SQLItems>
      <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSQLLog Files | The operation that you want to perform. Set the value to DescribeSQLLogFiles. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxx | The ID of the instance. |
| FileName | String | No | custinsxxxxx.csv | The name of the audit log file. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Valid value: 30 to 200. Default value: 30. |

ApsaraDB for RDS

```json
{ "PageNumber":1, "TotalRecordCounts":1, "ItemsCounts":1, "SQLItems": {"SQLItem":
```

[

```json
{ "DBName":"test", "AccountName":"accounttest", "HostAddress":"192.168.0.121", "SQLText":"update test.zxb set id=0 limit 1", "TotalExecutionTimes":12, "ReturnRowCounts":34, "ExecuteTime":"2011-06-11T15:00:23Z" }
```

]

```json
}, "RequestId": "08A3B71B-FE08-4B03-974F-CC7EA6DB1828" }
```

#### DescribeSQLLogFiles

Queries the audit log files that the SQL Explorer (SQL Audit) feature generates for an ApsaraDB RDS instance. Before you call this operation, make sure that the ApsaraDB RDS instance runs one of the following database engines: MySQL SQL Server 2008 R2 PostgreSQL PolarDB

**Request parameters**

| PageNumber | Integer | No | 1 | The number of the page to return. Valid values: 1 to 100000. Default value: 1. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalRecordCo unt | Integer | 10 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 10 | The number of entries returned on the current page. |
| Items | Array of LogFile |  | Details of audit log files. |
| LogFile |  |  |  |
| FileID | String | custinsxxxxx.csv | The name of the audit log file. |
| LogStatus | String | Success | The state of the audit log file. Valid values: Success Failed Generating |
| LogStartTime | String | 2015-05- 23T07:00:00Z | The beginning of the time range within which audit logs were recorded. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| LogEndTime | String | 2015-05- 24T07:00:00Z | The end of the time range within which audit logs were recorded. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| LogDownloadU RL | String | http://rdslog-hz- v3.oss-cn- hangzhou.aliyuncs. com/xxxxx | The download URL. If audit log files cannot be downloaded, this parameter is empty. |
| LogSize | String | 3000 | The size of the audit log file. Unit: byte. |

ApsaraDB for RDS

**Response parameters**

| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |
|---|---|---|---|

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeSQLLogFiles &DBInstanceId=rm-uf6wjk5xxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <items>
            <FileID>ZUBaS964T3OYtxxxxxxxx</FileID>
            <LogStatus>Success</LogStatus>
            <LogStartTime>2015-05-23T07:00:00Z</LogStartTime>
            <LogEndTime>2015-05-23T07:00:00Z</LogEndTime>
            <LogDownloadURL>xxxxxx.cn-hangzhou.oss.aliyun-
inc.com/xxxxx</LogDownloadURL>
            <LogSize>257</LogSize>
      </items>
      <pageRecordCount>1</pageRecordCount>
      <requestId> 1AD222E9-E606-4A42-BF6D-8A4442913CEF</requestId>
      <totalRecordCount>1</totalRecordCount>
```

`JSON` format

```json
{
    "items": [
        {
            "FileID": "ZUBaS964T3OYtxxxxxxxx",
            "LogStatus": "Success",
            "LogStartTime": "2015-05-23T07:00:00Z",
            "LogEndTime": "2015-05-23T07:00:00Z",
            "LogDownloadURL": "xxxxxx.cn-hangzhou.oss.aliyun-inc.com/xxxxx",
            "LogSize": "257"
        }
```

`],`

```json
    "pageRecordCount": 1,
    "requestId": " 1AD222E9-E606-4A42-BF6D-8A4442913CEF",
    "totalRecordCount": 1
}
```

Queries the SQL log reports of an ApsaraDB RDS instance.

#### DescribeSQLLogReportList

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSQLLog ReportList | The operation that you want to perform. Set the value to DescribeSQLLogReportList. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| EndTime | String | Yes | 2021-03- 18T16:00:00Z | The end of the time range to query. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. Note The end time must be later than the start time. |
| StartTime | String | Yes | 2021-03- 13T16:00:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 50 100 Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer greater than 0. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of Item |  | Details of SQL log reports. |
| Item |  |  |  |
| LatencyTopNIt ems | Array of LatencyTopNIt em |  | Details of the SQL statements executed with the highest latency. |

ApsaraDB for RDS

**Request parameters**

**Response parameters**

| LatencyTopNIt em |  |  |  |
|---|---|---|---|
| AvgLatency | Long | 500 | The average amount of time that is required to execute the SQL statement. Unit: milliseconds. |
| SQLExecuteTi mes | Long | 5 | The number of SQL statement executions. |
| SQLText | String | SELECT * FROM table name; _ | The SQL statement returned. Note Only the first 128 characters of the SQL statement are returned. In addition, only the SQL statements that take longer than 100 milliseconds to execute are returned. |
| QPSTopNItems | Array of QPSTopNItem |  | Details of the SQL statements executed the most frequently. |
| QPSTopNItem |  |  |  |
| SQLExecuteTi mes | Long | 5 | The number of SQL statement executions. |
| SQLText | String | SELECT * FROM table name; _ | The SQL statement returned. Note Only the first 128 characters of the SQL statement are returned. In addition, only the SQL statements that take longer than 5 milliseconds to execute are returned. |
| ReportTime | String | 2019-03- 27T16:00:00Z | The time when the report was generated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 30 | The number of SQL log reports on the current page. |
| RequestId | String | 08A3B71B-FE08- 4B03-974F- CC7EA6DB1828 | The ID of the request. |

ApsaraDB for RDS

| TotalRecordCo unt | Integer | 60 | The total number of entries returned. |
|---|---|---|---|

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeSQLLogReportList &DBInstanceId=rm-uf6wjk5xxxxxxx &EndTime=2021-03-18T16:00:00Z &StartTime=2021-03-13T16:00:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <TotalRecordCount>60</TotalRecordCount>
      <PageRecordCount>30</PageRecordCount>
      <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828    </RequestId>
      <PageNumber>1</PageNumber>
      <Items>
            <Item>
                  <ReportTime>2019-03-27T16:00:00Z</ReportTime>
                  <LatencyTopNItems>
                        <LatencyTopNItem>
                              <AvgLatency>500</AvgLatency>
                              <SQLExecuteTimes>5</SQLExecuteTimes>
                              <SQLText>SELECT * FROM table_name;</SQLText>
                        </LatencyTopNItem>
                  </LatencyTopNItems>
                  <QPSTopNItems>
                        <QPSTopNItem>
                              <SQLExecuteTimes>5</SQLExecuteTimes>
                              <SQLText>SELECT * FROM table_name;</SQLText>
                        </QPSTopNItem>
                  </QPSTopNItems>
            </Item>
      </Items>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

ApsaraDB for RDS

```json
{
    "TotalRecordCount": "60",
    "PageRecordCount": "30",
    "RequestId": "08A3B71B-FE08-4B03-974F-CC7EA6DB1828\t",
    "PageNumber": "1",
    "Items": {
        "Item": [{
            "ReportTime": "2019-03-27T16:00:00Z",
            "LatencyTopNItems": {
                "LatencyTopNItem": [{
                    "AvgLatency": "500",
                    "SQLExecuteTimes": "5",
                    "SQLText": "SELECT * FROM table_name;"
                }]
            },
            "QPSTopNItems": {
                "QPSTopNItem": [{
                    "SQLExecuteTimes": "5",
                    "SQLText": "SELECT * FROM table_name;"
                }]
            }
        }]
    }
}
```

#### PurgeDBInstanceLog

Deletes log backup files from an ApsaraDB RDS instance. ApsaraDB RDS allows an instance to automatically upload log backup files to Object Storage Service (OSS) buckets. If the remaining storage space of an instance is insufficient, you can also manually upload the log backup files of the instance to OSS buckets. After the log backup files of an instance are uploaded, ApsaraDB RDS deletes these files from the instance to release storage space. When this operation is called, log backup files are uploaded from an instance to OSS buckets, and then are deleted from the instance. If the instance runs SQL Server, transaction log backup files are compressed before they are uploaded.

**Note**

This operation is supported only for instances that run MySQL or SQL Server. When you upload log backup files, the data restoration feature is not affected. This operation is called to release storage space. The backup storage usage is not reduced. The OSS buckets to which log backup files are uploaded are provided by ApsaraDB RDS. You do not need to purchase these OSS buckets. In addition, you cannot access these OSS buckets.

**Request parameters**

| Action | String | Yes | PurgeDBInstanc eLog | The operation that you want to perform. Set the value to PurgeDBInstanceLog. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=PurgeDBInstanceLog &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
```

`JSON` format

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

### Event history management

#### DescribeActionEventPolicy

Queries the status of the event history feature for an ApsaraDB RDS instance.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeActionE ventPolicy | The operation that you want to perform. Set the value to DescribeActionEventPolicy. |
| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EnableEventLo g | String | True | Indicates whether the event history feature was enabled for the region. |
| RegionId | String | cn-hangzhou | The ID of the region. |
| RequestId | String | CCECD3CD-AB2D- 4F6D-BEDE- 47BC90A398D2 | The ID of the request. |

ApsaraDB for RDS The event history feature enables you to view the events that occurred within a region over a specific time range. Such historical events include instance creation and parameter modification.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeActionEventPolicy &Region=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
  <RequestId>CCECD3CD-AB2D-4F6D-BEDE-47BC90A398D2</RequestId>
      <RegionId>cn-hangzhou</RegionId>
      <EnableEventLog>True</EnableEventLog>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEvents | The operation that you want to perform. Set the value to DescribeEvents. |
| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to query the most recent region list. |
| ResourceType | String | No | instance | The type of the resource associated with an event. Set the value to instance. |
| ResourceName | String | No | rm- bp1z306******** ** | The name of the resource associated with an event. Set the value to an instance ID. |
| StartTime | String | No | 2019-06- 11T15:00:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| EndTime | String | No | 2019-06- 12T15:00:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |

ApsaraDB for RDS

```json
{
    "RequestId": "CCECD3CD-AB2D-4F6D-BEDE-47BC90A398D2",
    "RegionId": "cn-hangzhou",
    "EnableEventLog": "True"
}
```

#### DescribeEvents

Queries the events of ApsaraDB RDS instances within a region. The event history feature enables you to view the events that occurred within a region over a specific time range. Such historical events include instance creation and parameter modification. Before you call this operation, make sure that the event history feature is enabled.

**Request parameters**

| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 50 100 Default value: 30. |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EventItems | Array of EventItems |  | Details of the events. |
| EventItems |  |  |  |
| EventId | Integer | 11000053 | The ID of the event. |
| EventName | String | ModifySecurityIPLis t | The name of the event. |
| EventPayload | String | {\"Domain\": \"rds- inc- share.aliyuncs.com \", \"Api\": \"ReleaseInstanceP ublicConnection\"} | The request or context parameters of the event. |
| EventReason | String | FROM USER _ | The source of the event. |
| EventRecordTi me | String | 2019-08- 20T01:12:49Z | The time when the event was recorded. The time is slightly later than the time when the event occurred. |
| EventTime | String | 2019-08- 20T01:08:22Z | The time when the event occurred. |
| EventType | String | NetworkManageme nt | The type of the event. |
| EventUserTyp e | String | SYSTEM | The type of the user who executed the event. |
| RegionId | String | cn-hangzhou | The ID of the region. |

ApsaraDB for RDS

**Response parameters**

| ResourceNam e | String | rm- bp1z3065m9976ix 8a | The name of the resource associated with the event. Only an instance ID is supported. |
|---|---|---|---|
| ResourceType | String | instance | The type of the resource associated with the event. Only instances are supported for this parameter. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 30 | The number of entries returned per page. |
| RequestId | String | A103039D-B1B2- 4C57-B989- 7D7C0DA95426 | The ID of the request. |
| TotalRecordCo unt | Integer | 40 | The total number of entries returned. |

ApsaraDB for RDS

**Examples**

Sample requests

```
&Region=cn-hangzhou &StartTime=2019-08-20T01:30:00Z &EndTime=2019-08-20T01:35:00Z &<Common request parameters>
```

Sample success responses `XML` format ApsaraDB for RDS

```xml
  <EventItems>
            <EventItems>
                  <EventName>ModifySecurityIPList</EventName>
                  <EventUserType>SYSTEM</EventUserType>
                  <ResourceType>instance</ResourceType>
                  <EventPayload></EventPayload>
                  <EventTime>2019-08-20T01:33:43Z</EventTime>
                  <RegionId>cn-hangzhou</RegionId>
                  <EventRecordTime>2019-08-20T01:33:57Z</EventRecordTime>
                  <EventReason>FROM_SYSTEM</EventReason>
                  <EventId>11000048</EventId>
                  <ResourceName>rm-bpxxxxxxx</ResourceName>
                  <EventType>SecurityManagement</EventType>
            </EventItems>
            <EventItems>
                  <EventName>ModifySecurityIPList</EventName>
                  <EventUserType>SYSTEM</EventUserType>
                  <ResourceType>instance</ResourceType>
                  <EventPayload></EventPayload>
                  <EventTime>2019-08-20T01:33:43Z</EventTime>
                  <RegionId>cn-hangzhou</RegionId>
                  <EventRecordTime>2019-08-20T01:33:57Z</EventRecordTime>
                  <EventReason>FROM_SYSTEM</EventReason>
                  <EventId>11000047</EventId>
                  <ResourceName>rm-bpxxxxxxx</ResourceName>
                  <EventType>SecurityManagement</EventType>
            </EventItems>
      </EventItems>
      <TotalRecordCount>2</TotalRecordCount>
      <PageNumber>1</PageNumber>
      <PageSize>2</PageSize>
      <RequestId>B5FF9EE6-830E-4DBE-8498-9890A62D2875</RequestId>
```

`JSON` format

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidStartTime.Fo rmat | Specified start time is not valid. | The error message returned because the specified start time is invalid. |

ApsaraDB for RDS

```json
{
    "EventItems": {
        "EventItems": [
            {
                "EventName": "ModifySecurityIPList",
                "EventUserType": "SYSTEM",
                "ResourceType": "instance",
                "EventPayload": "",
                "EventTime": "2019-08-20T01:33:43Z",
                "RegionId": "cn-hangzhou",
                "EventRecordTime": "2019-08-20T01:33:57Z",
                "EventReason": "FROM_SYSTEM",
                "EventId": 11000048,
                "ResourceName": "rm-bpxxxxxxx",
                "EventType": "SecurityManagement"
            },
            {
                "EventName": "ModifySecurityIPList",
                "EventUserType": "SYSTEM",
                "ResourceType": "instance",
                "EventPayload": "",
                "EventTime": "2019-08-20T01:33:43Z",
                "RegionId": "cn-hangzhou",
                "EventRecordTime": "2019-08-20T01:33:57Z",
                "EventReason": "FROM_SYSTEM",
                "EventId": 11000047,
                "ResourceName": "rm-bpxxxxxxx",
                "EventType": "SecurityManagement"
            }
```

]

```json
    },
    "TotalRecordCount": 2,
    "PageNumber": 1,
    "PageSize": 2,
    "RequestId": "B5FF9EE6-830E-4DBE-8498-9890A62D2875"
}
```

Enables or disables the event history feature for an ApsaraDB RDS instance.

#### ModifyActionEventPolicy

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyActionEve ntPolicy | The operation that you want to perform. Set the value to ModifyActionEventPolicy. |
| EnableEventLog | String | Yes | True | Specifies whether to enable the event history feature. Valid values: True and False. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region for which you want to enable the event history feature. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EnableEventLo g | String | True | Indicates whether the event history feature was enabled for the region. |
| RegionId | String | cn-hangzhou | The ID of the region. |
| RequestId | String | BAC0952C-0EB3- 4DE7-A567- B83269BFE43F | The ID of the request. |

ApsaraDB for RDS The event history feature enables you to view the events that occurred within a region over a specific time range. Such historical events include instance creation and parameter modification.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=ModifyActionEventPolicy &Region=cn-hangzhou &EnableEventLog=True &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDiagnosti cReport | The operation that you want to perform. Set the value to CreateDiagnosticReport. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxx | The ID of the instance. |
| StartTime | String | Yes | 2018-06- 11T15:00Z | The start time of the monitoring data that is included in the generated diagnostic report. Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2018-06- 12T15:00Z | The end time of the monitoring data that is included in the generated diagnostic report. Specify the time in the ISO 8610 standard in the yyyy- MM-ddTHH:mmZ format. The time must be in UTC. |

ApsaraDB for RDS

```xml
   <RequestId>BAC0952C-0EB3-4DE7-A567-B83269BFE43F</RequestId>
   <RegionId>cn-hangzhou</RegionId>
   <EnableEventLog>True</EnableEventLog>
```

`JSON` format

```json
{
    "RequestId": "BAC0952C-0EB3-4DE7-A567-B83269BFE43F",
    "RegionId": "cn-hangzhou",
    "EnableEventLog": "True"
}
```

### Performance optimization

**and diagnostics (CloudDBA)**

#### CreateDiagnosticReport

Creates a diagnostic report for an ApsaraDB RDS instance.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ReportId | String | 10166270 | The ID of the diagnostic report. |
| RequestId | String | 8DA8956A-53DA- 423E-9540- 387428ED37FF- 5711 | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=CreateDiagnosticReport &DBInstanceId=rm-uf6wjk5xxxxxx &StartTime=2018-06-11T15:00Z &EndTime=2018-06-12T15:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <reportId>10166270</reportId>
   <requestId>8DA8956A-53DA-423E-9540-387428ED37FF-5711</requestId>
```

`JSON` format

```json
{
    "reportId": "10166270",
    "requestId": "8DA8956A-53DA-423E-9540-387428ED37FF-5711"
}
```

#### DescribeDiagnosticReportList

Queries diagnostic reports of an ApsaraDB RDS instance. This operation returns the details of diagnostic reports such as the time range of monitoring data, report generation time, and download URL. The diagnostic reports are retained for 15 days.

**Note**

This operation is not supported for instances that run SQL Server 2017 EE.

**Request parameters**

| Action | String | Yes | DescribeDiagnos ticReportList | The operation that you want to perform. Set the value to DescribeDiagnosticReportList. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B7E9A79C-DE1B- 4398-845F- D654FC0958BD | The ID of the request. |
| ReportList | Array of Report |  | Details of the diagnostic reports. |
| DiagnosticTim e | String | 2018-01- 17T12:46:09Z | The time when the diagnostic report was generated. |
| DownloadURL | String | http://rdsreport-hz- v3.oss-cn- hangzhou.aliyuncs. com/xxxxx | The public download URL. If the diagnostic report cannot be downloaded, this parameter returns an empty string. |
| EndTime | String | 2018-01- 10T15:31:00Z | The end time of the monitoring data. |
| Score | Integer | 100 | The diagnostic score. |
| StartTime | String | 2018-01- 10T15:30:00Z | The start time of the monitoring data. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeDiagnosticReportList &DBInstanceId=rm-uf6wjk5xxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

ApsaraDB for RDS

```xml
      <reportList>
            <diagnosticTime>2018-01-17T12:46:09Z</diagnosticTime>
            <downloadURL>http://rdsreport-hzi-v2.oss-cn-hangzhou-
i.aliyuncs.com/xxxxx</downloadURL>
            <endTime>2018-01-10T15:31:00Z</endTime>
            <score>100</score>
            <startTime>2018-01-10T15:30:00Z</startTime>
      </reportList>
      <requestId>B7E9A79C-DE1B-4398-845F-D654FC0958BD</requestId>
```

`JSON` format

```json
{
    "reportList": [
        {
            "diagnosticTime": "2018-01-17T12:46:09Z",
            "downloadURL": "http://rdsreport-hzi-v2.oss-cn-hangzhou-
i.aliyuncs.com/xxxxx",
            "endTime": "2018-01-10T15:31:00Z",
            "score": 100,
            "startTime": "2018-01-10T15:30:00Z"
        }
```

`],`

```json
    "requestId": "B7E9A79C-DE1B-4398-845F-D654FC0958BD"
}
```

### Data migration

#### CreateUploadPathForSQLServer

Obtains the information used to upload files.

**Note**

This operation is supported only for instances that run SQL Server. You can call this operation to create a username and password to log on to the file server, and a path to upload files. This information can be used to upload data files. After the upload is complete, you can migrate external data. Before you call this operation, make sure that the following requirements are met: The instance is in the running state. The database is in the running state. Up to 20 files can be created for a single database per day. A 24-hour period is considered a single day. For example, if the last creation time was 2012-03-15 18:30:12, the next creation time must be later than 2012-03-16 18:30:12.

**Request parameters**

| Action | String | Yes | CreateUploadPat hForSQLServer | The operation that you want to perform. Set the value to CreateUploadPathForSQLServer. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- bp1********** | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| DBName | String | Yes | test | The name of the database. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| InternetFtpSer ver | String | 10.230.239.1 | The IP address of the file server on the Internet. |
| InternetPort | Integer | 3021 | The port of the file server on the Internet. |
| UserName | String | test | The username used to log on to the file server. |
| Password | String | test12345 | The password used to log on to the file server. |
| FileName | String | testdb01 1370572 _ 475975.bak | The name of the data file with the extension. |
| IntranetFtpser ver | String | None | The IP address of the file server on the internal network. |
| Intranetport | Integer | 0 | The port of the file server on the internal network. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=CreateUploadPathForSQLServer &DBInstanceId=rdsaiiabnaiiabn &DBName=RDS_MySQL &<Common request parameters>
```

Sample success responses

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | FTPServiceUnavaila ble | The request has failed due to a temporary failure of the FTP server. | The error message returned because an FTP server error occurred. |
| 403 | OperationDenied.D BStatus | The operation is not permitted due to status of database. | The error message returned because this operation is not supported when the instance or database is in the read-only state. Before you call this operation on an ApsaraDB RDS for SQL Server instance of the dedicated instance family, make sure that the following requirements are met: 1. The instance is in the running state. 2. The instance does not have temporary backup tasks. 3. The instance does not have migration tasks. 4. The instance does not have restoration tasks. 5. Files have been uploaded and are valid. |

ApsaraDB for RDS `XML` format

```xml
         <RequestId>66816822-CEC1-4C8D-AB26-2530A7D4DCA5</RequestId>
         <InternetFtpServer>10.230.239.1</InternetFtpServer>
         <InternetPort>3021</InternetPort>
         <IntranetFtpServer></IntranetFtpServer>
         <IntranetPort></IntranetPort>
         <UserName>test</UserName>
         <Password>test12345</Password>
         <FileName>testdb01_1370572475975.bak</FileName>
```

`JSON` format

```json
{
        "RequestId": "66816822-CEC1-4C8D-AB26-2530A7D4DCA5",
        "InternetFtpServer": "10.230.239.1",
        "InternetPort": "3021",
        "UserName": "test",
        "Password": "test12345",
        "FileName": "testdb01_1370572475975.bak"
    }
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeFilesFor SQLServer | The operation that you want to perform. Set the value to DescribeFilesForSQLServer. |
| DBInstanceId | String | Yes | rm- bp1842vmucoa5 w874 | The ID of the instance. |
| StartTime | String | Yes | 2011-06- 11T16:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| EndTime | String | Yes | 2011-06- 11T16:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 5 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rdsaiiabnaiiabn | The ID of the instance. |

ApsaraDB for RDS

#### DescribeFilesForSQLServer

Queries the details of data files for an ApsaraDB RDS instance. This operation returns the username used to log on to the file server. After data files are uploaded, their states are updated. This operation also returns the states of data files. If data files are available, you can migrate the data files and view their migration progress information.

**Note**

This operation is supported only for instances that run SQL Server.

**Request parameters**

**Response parameters**

| TotalRecordCo unt | Integer | 1 | The total number of entries returned. |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 1 | The number of SQL statements on the current page. |
| Items | Array of SQLServerUplo adFile |  | Details of the data files. |
| SQLServerUplo adFile |  |  |  |
| DBName | String | testdb01 | The name of the database. |
| FileName | String | testdb01 1370572 _ 475975.bak | The name of the data file with the extension. |
| FileSize | Long | 1243435 | The size of the data file. Unit: byte. |
| InternetFtpSer ver | String | 10.230.239.1 | The IP address of the file server on the Internet. |
| InternetPort | Integer | 3021 | The port of the file server on the Internet. |
| IntranetFtpser ver | String | Empty | The IP address of the file server on the internal network. |
| Intranetport | Integer | 0 | The port of the file server on the internal network. |
| UserName | String | MKEakJbyG | The username used to log on to the file server. |
| Password | String | aT2Y XN1GGnOLz _ m | The password used to log on to the file server. |

ApsaraDB for RDS

| FileStatus | String | Success | The state of the data file. Valid values: Unavailable Available NotStarted Uploading UploadFailed Virus Deleted Success |
|---|---|---|---|
| CreationTime | String | 2014-06- 11T15:02:40Z | The time when the FTP file was generated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Description | String | 2 | The description of the file status. Valid values: 0: The file upload is not started. 1: The file is being uploaded. 2: The file is uploaded and can be migrated. 3: The file failed to be uploaded because the upload is canceled or a network error occurred. You can upload the file again. 4: The file is uploaded but a virus is detected. 5: The file is deleted. |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
https://rds.example.com/?Action=DescribeFilesForSQLServer &DBInstanceId=rm-bp1842vmucoa5w874 &EndTime=2011-06-11T16:00Z &StartTime=2011-06-11T16:00Z &<Common request parameters>
```

Sample success responses `XML` format ApsaraDB for RDS

```xml
      <PageNumber>1</PageNumber>
      <TotalRecordCount>1</TotalRecordCount>
      <PageRecordCount>1</PageRecordCount>
      <Items>
            <SQLServerUploadFile>
                  <DBName>testdb01</DBName>
                  <FileName>testdb01_1370572475975.bak</FileName>
                  <FileSize>1243435</FileSize>
                  <InternetFtpServer>10.230.239.1</InternetFtpServer>
                  <InternetPort>3021</InternetPort>
                  <IntranetFtpServer></IntranetFtpServer>
                  <IntranetPort></IntranetPort>
                  <UserName>MKEakJbyG</UserName>
                  <Password>aT2Y_XN1GGnOLzm</Password>
                  <FileStatus>Success </FileStatus>
                  <CreationTime>2014-06-11T15:02:40Z</CreationTime>
            </SQLServerUploadFile>
      </Items>
      <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828</RequestId>
```

`JSON` format

```json
{
    "PageNumber":1,
    "TotalRecordCount":1,
    "PageRecordCount":1,
    "Items":{
        "SQLServerUploadFile":[
            {
                "DBName":"testdb01",
                "FileName":"testdb01_1370572475975.bak",
                "FileSize ":"1243435",
                "InternetFtpServer ":"10.230.239.1",
                "InternetPort":3021,
                "IntranetFtpServer":"",
                "IntranetPort":"",
                "UserName":"MKEakJbyG",
                "Password":"aT2Y_XN1GGnOLzm",
                "FileStatus":"Success ",
                "CreationTime":"2014-06-11T15:02:40Z"
            }
```

]

```json
    },
    "RequestId":"08A3B71B-FE08-4B03-974F-CC7EA6DB1828"
}
```

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | FTPServiceUnavaila ble | The request has failed due to a temporary failure of the FTP server. | The error message returned because an FTP server error occurred. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ImportDatabase BetweenInstanc es | The operation that you want to perform. Set the value to ImportDatabaseBetweenInstance s. |

ApsaraDB for RDS

#### ImportDatabaseBetweenInstances

Migrates data across ApsaraDB RDS instances. We recommend that you use Data Transmission Service (DTS). DTS provides data migration, subscription, and synchronization features to help you establish stable and secure transmission links. During migration, the source instance changes to the **Migrating** state and the destination instance changes to the **Importing Data** state. Before you call this operation, make sure that the following requirements are met: The source and destination instances run SQL Server and belong to the dedicated or dedicated host instance family. For more information about instance types, see **Instance**
**types** in **ApsaraDB RDS****Product Introduction**.
The source and destination instances are created by using the same user credentials. The source and destination instances are in the running state. The source and destination databases are in the running state. The remaining storage space of the destination instance is greater than the storage space occupied by the source database.

**Note**

This operation is not supported for instances that run SQL Server 2017 EE. You can migrate the data of multiple databases at a time.

**Request parameters**

| DBInfo | String | Yes | {"DBNames": ["mydb","mydb2 "]} | The names of the source and destination databases. The value of this parameter is a JSON string. Note For the source and destination instances that run SQL Server, the value of this parameter consists of one or more key-value pairs. In each key-value pair, the key specifies the name of the source database, and the value specifies the name of the destination database. A source database can have a different name from its destination database. Example: {"DBNames": {"srcdb":"destdb","srcdb2 ":"destmydb2"}} In the preceding example, the data of the source database srcdb is migrated to the destination database destdb, and the data of the source database srcdb2 is migrated to the destination database destmydb2. The name of each source or destination database must be unique. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the destination instance. |
| SourceDBInstan ceId | String | Yes | rm- g4a1jk8xxxxxxx | The ID of the source instance. The source and destination instances cannot have the same ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ImportId | String | 85265475235 | The ID of the migration task. |
| RequestId | String | 5A77D650-27A1- 4E08-AD9E- 59008EDB6927 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CancelImport | The operation that you want to perform. Set the value to CancelImport. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

ApsaraDB for RDS

```
http(s)://rds.example.com/?Action=ImportDatabaseBetweenInstances &DBInstanceId=rm-uf6wjk5xxxxxxx &SourceDBInstanceId=rm-g4a1jk8xxxxxxx &DBInfo={"DBNames":["mydb","mydb2"]} &<Common request parameters>
```

Sample success responses `XML` format

```xml
           <ImportId>2122321</ImportId>
         <RequestId>5A77D650-27A1-4E08-AD9E-59008EDB6927</RequestId>
```

`JSON` format

```json
{
       "ImportId":2122321,
       "RequestId":"5A77D650-27A1-4E08-AD9E-59008EDB6927"
}
```

#### CancelImport

Cancels a migration task of an ApsaraDB RDS instance. This operation is supported for instances that run SQL Server and belong to the dedicated or dedicated host instance family. For information about how to initiate a migration task, see ImportDatabaseBetweenInstances.

**Note**

This operation is not supported for instances that run SQL Server 2017 EE.

**Request parameters**

| ImportId | Integer | Yes | 8562584 | The ID of the migration task. Note This parameter is returned when the migration task is initiated. For more information, see ImportDatabaseBetweenInstanc es. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 17F57FEE-EA4F- 4337-8D2E- 9C23CAA63D74 | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
&DBInstanceId=rm-uf6wjk5xxxxxxx &ImportId=8562584 &<Common request parameters>
```

Sample success responses `XML` format

```xml
         <RequestId>17F57FEE-EA4F-4337-8D2E-9C23CAA63D74</RequestId>
```

`JSON` format

```json
{
  "RequestId": " 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74"
}
```

#### CreateMigrateTask

Creates a backup data migration task from Object Storage Service (OSS) to ApsaraDB RDS for SQL Server.

**Request parameters**

| Action | String | Yes | CreateMigrateTa sk | The operation that you want to perform. Set the value to CreateMigrateTask. |
|---|---|---|---|---|
| BackupMode | String | Yes | FULL | The type of the backup data migration task. Valid values: FULL: The backup data migration task migrates full backup files. UPDF: The backup data migration task migrates incremental or log backup files. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |
| DBName | String | Yes | testDB | The name of the destination database. |
| IsOnlineDB | String | Yes | True | Specifies whether to make the restored database data available for user access. Valid values: True False Note Set the value to True for instances that run SQL Server 2008 R2. |
| CheckDBMode | String | No | AsyncExecuteDB Check | The consistency check method for the database. Valid values: SyncExecuteDBCheck: synchronous database check AsyncExecuteDBCheck: asynchronous database check Default value: AsyncExecuteDBCheck (compatible with SQL Server 2008 R2). Note This parameter is valid when IsOnlineDB is set to True. |

ApsaraDB for RDS

| OssObjectPositio ns | String | No | oss-ap- southeast- 1.aliyuncs.com:r dsmssqlsingapor e:autotest 2008 _ R2 TestMigratio _ n FULL.bak _ | The location of the backup file in the OSS bucket. The parameter consists of the following parts that are separated by colons (:): The endpoint of the OSS bucket: oss-ap-southeast-1.aliyuncs.com. The name of the OSS bucket: rdsmssqlsingapore. The key of the backup file in the OSS bucket: autotest 2008R2 TestMigration F _ _ _ ULL.bak. Note This parameter is optional for instances that run SQL Server 2008 R2. This parameter is required for instances that run a database engine later than SQL Server 2008 R2. |
|---|---|---|---|---|
| OSSUrls | String | No | check cdn oss.s _ _ h www.xxxxxx.mo bi | The shared URL of the backup file in the OSS bucket. The URL must be encoded. If you specify multiple URLs, separate them with vertical bars (\|) and then encode them. Note This parameter is required for instances that run SQL Server 2008 R2. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupMode | String | FULL | The type of the backup data migration task. Valid values: FULL: The backup data migration task migrates full backup files. UPDF: The backup data migration task migrates incremental or log backup files. |
| DBInstanceId | String | rm-uf6wjk5xxxxx | The ID of the instance. |

ApsaraDB for RDS

**Response parameters**

| DBName | String | test02 | The name of the database. |
|---|---|---|---|
| MigrateTaskId | String | 564563256 | The ID of the backup data migration task. |
| RequestId | String | 866F5EB8-4650- 4061-87F0- 379F6F968BCE | The ID of the request. |
| TaskId | String | 5451225 | The ID of the task. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=CreateMigrateTask &DBInstanceId=rm-uf6wjk5xxxxxxx &DBName=testDB &BackupMode=FULL &IsOnlineDB=True &OssObjectPositions=oss-ap-southeast- 1.aliyuncs.com:rdsmssqlsingapore:autotest_2008R2_TestMigration_FULL.bak &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <MigrateTaskId>135847</MigrateTaskId>
      <DBInstanceId>rm-bp178grbxxxxxxx</DBInstanceId>
      <RequestId>5F2B3757-BD56-40B3-B5F2-FCDD9FA0E2E2</RequestId>
      <BackupMode>UPDF</BackupMode>
      <TaskId>128301751</TaskId>
      <DBName>test02</DBName>
```

`JSON` format

```json
{
    "MigrateTaskId": "135847",
    "DBInstanceId": "rm-bp178grbxxxxxxx",
    "RequestId": "5F2B3757-BD56-40B3-B5F2-FCDD9FA0E2E2",
    "BackupMode": "UPDF",
    "TaskId": "128301751",
    "DBName": "test02"
}
```

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidDBName | The instance does not have the specified DB name. | The error message returned because the specified destination database does not exist. Check the name and state of the destination database or specify another database. |
| 400 | InvalidOSSURL | The Specified OSS URL is not valid | The error message returned because the specified OSS URL is invalid. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescibeImportsF romDatabase | The operation that you want to perform. Set the value to DescibeImportsFromDatabase. |
| DBInstanceId | String | Yes | rm-bpxxxxx | The ID of the instance. |
| EndTime | String | Yes | 2011-06- 11T16:00Z | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| Engine | String | Yes | MySQL | The database engine of the instance. Valid values: MySQL SQLServer |
| StartTime | String | Yes | 2011-06- 11T15:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |

ApsaraDB for RDS

#### DescibeImportsFromDatabase

Queries the details of migration tasks for an ApsaraDB RDS instance. This operation is supported only for instances that run MySQL or SQL Server. For information about how to initiate a migration task, see ImportDatabaseBetweenInstances.

**Request parameters**

| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
|---|---|---|---|---|
| ImportId | Integer | No | 123 | The ID of the migration task. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 50 100 Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of ImportResultFr omDB |  | Details of the migration tasks. |
| ImportResultFr omDB |  |  |  |

ApsaraDB for RDS

**Response parameters**

| ImportDataSta tus | String | NotStart | The state of the migration task. Valid values: NotStart: The migration task is not started. FullExporting: The migration task is exporting full data. FullImporting: The migration task is importing full data. Success: The migration task is successful. Failed: The migration task failed. Canceled: The migration task has been canceled. Canceling: The migration task is being canceled. IncrementalWaiting: The migration task is waiting to synchronize incremental data. IncrementalImporting: The migration task is synchronizing incremental data. StopSyncing: The migration task has stopped synchronizing data. |
|---|---|---|---|
| ImportDataSta tusDescription | String | Description | The description of the migration task. |
| ImportDataTy pe | String | Full | The type of the migration task. Valid values: Full: The migration task migrates full data. Incremental: The migration task migrates incremental data. |
| ImportId | Integer | 123 | The ID of the migration task. |
| IncrementalIm portingTime | String | 2011-06- 11T15:00Z | The time when the migration task synchronized incremental data. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 1 | The number of entries returned per page. |
| RequestId | String | B000AA91-393D- 46F9-8D9B- 098E28931A3A | The ID of the request. |
| TotalRecordCo unt | Integer | 1 | The total number of entries returned. |

ApsaraDB for RDS ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescibeImportsFromDatabase &DBInstanceId=rm-bpxxxxx &EndTime=2011-06-11T16:00Z &Engine=MySQL &StartTime=2011-06-11T15:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
  <TotalRecordCount>0</TotalRecordCount>
  <PageRecordCount>30</PageRecordCount>
  <RequestId>B000AA91-393D-46F9-8D9B-098E28931A3A</RequestId>
  <PageNumber>1</PageNumber>
  <Items>
        <ImportResultFromDB>
              <ImportId>123</ImportId>
              <ImportDataType>Full</ImportDataType>
              <ImportDataStatus>NotStart</ImportDataStatus>
              <ImportDataStatusDescription>Description</ImportDataStatusDescription>
              <IncrementalImportingTime></IncrementalImportingTime>
        </ImportResultFromDB>
  </Items>
```

`JSON` format

```json
{
  "TotalRecordCount": 0,
  "PageRecordCount": 30,
  "RequestId": "B000AA91-393D-46F9-8D9B-098E28931A3A",
  "PageNumber": 1,
  "Items": {
    "ImportResultFromDB": [
      {
        "ImportId":"123",
        "ImportDataType":"Full",
        "ImportDataStatus":"NotStart",
        "ImportDataStatusDescription":"Description",
        "IncrementalImportingTime":""
      }
```

]

```
  }
}
```

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 403 | OperationDenied.D BInstanceType | The operation is not permitted due to type of instance. | The error message returned because this operation is not supported when the instance is not a primary instance. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMigrate TaskById | The operation that you want to perform. Set the value to DescribeMigrateTaskById. |
| DBInstanceId | String | Yes | rm- bp11e1tzgxxxx4 ox | The ID of the instance. |
| MigrateTaskId | String | Yes | 235943 | The ID of the backup data migration task. You can call the DescribeMigrateTasks operation to query the IDs of migration tasks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupMode | String | FULL | The type of the backup data migration task. Valid values: FULL: The backup data migration task migrates full backup files. UPDF: The backup data migration task migrates incremental or log backup files. |
| CreateTime | String | 2020-05- 30T12:11:04Z | The time when the backup data migration task was created. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DBInstanceNa me | String | rm- uf6wjk5xxxxxxxxxx | The ID of the instance. |

ApsaraDB for RDS

#### DescribeMigrateTaskById

Queries a backup data migration task for an ApsaraDB RDS for SQL Server instance.

**Request parameters**

**Response parameters**

| DBName | String | mytestdb | The name of the database. |
|---|---|---|---|
| Description | String | Success to DBCC checkdb asynchronously | The description of the backup data migration task. |
| EndTime | String | 2021-05- 30T12:11:04Z | The time when the backup data migration task was complete. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| IsDBReplaced | String | False | Indicates whether the imported data overwrites the existing data. Valid values: False True |
| MigrateTaskId | String | 235943 | The ID of the backup data migration task. |
| RequestId | String | 6ED3635A-01F9- 47BD-B9C8- CB3FD70A336E | The ID of the request. |
| Status | String | Success | The state of the backup data migration task. Valid values: NoStart: The backup data migration task is not started. Running: The backup data migration task is running. Success: The backup data migration task is successful. Failed: The migration task failed. Waiting: The backup data migration task is waiting for an incremental backup file to be imported. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeMigrateTaskById &DBInstanceId=rm-bp11e1tzgxxxx4ox &MigrateTaskId=235943 &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMigrate Tasks | The operation that you want to perform. Set the value to DescribeMigrateTasks. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. |

ApsaraDB for RDS

```xml
    <Status>Success</Status>
    <Description>Success to DBCC checkdb asynchronously</Description>
    <RequestId>B994DF29-44A1-43FD-A693-917930DFEBCE</RequestId>
    <EndTime>2021-03-04T13:50:23Z</EndTime>
    <MigrateTaskId>235943</MigrateTaskId>
    <CreateTime>2021-03-04T13:47:17Z</CreateTime>
    <BackupMode>FULL</BackupMode>
    <DBName>mytestdb</DBName>
    <DBInstanceName>rm-bp11e1tzgxxxxx4ox</DBInstanceName>
```

`JSON` format

```json
{
  "Status": "Success",
  "Description": "Success",
  "RequestId": "6ED3635A-01F9-47BD-B9C8-CB3FD70A336E",
  "EndTime": "2021-03-04T13:47:58Z",
  "MigrateTaskId": "235943",
  "CreateTime": "2021-03-04T13:47:17Z",
  "BackupMode": "FULL",
  "DBName": "mytestdb",
  "DBInstanceName": "rm-bp11e1tzgxxxxx4ox"
}
```

#### DescribeMigrateTasks

Queries backup data migration tasks for an ApsaraDB RDS for SQL Server instance. This operation allows you to query the backup data migration tasks that are created for an instance within the last week.

**Note**

This operation is supported only for full backup files. This operation is not supported for instances that run SQL Server 2017 EE.

**Request parameters**

| EndTime | String | Yes | 2017-10- 25T01:00Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
|---|---|---|---|---|
| StartTime | String | Yes | 2017-10- 20T01:00Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid value: 30 to 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| Items | Array of MigrateTask |  | The backup data migration tasks. |
| MigrateTask |  |  |  |
| BackupMode | String | FULL | The type of the backup data migration task. Valid values: FULL: The backup data migration task migrates full backup files. UPDF: The backup data migration task migrates incremental or log backup files. |
| CreateTime | String | 2017-05- 30T12:11:04Z | The time when the backup data migration task was created. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| DBName | String | testDB | The name of the database. |

ApsaraDB for RDS

**Response parameters**

| Description | String | Api description | The description of the backup data migration task. |
|---|---|---|---|
| EndTime | String | 2017-05- 30T13:11:04Z | The time when the backup data migration task was complete. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| IsDBReplaced | String | True | Indicates whether the imported data overwrites the existing data. |
| MigrateTaskId | String | 564522545 | The ID of the backup data migration task. |
| Status | String | Success | The state of the backup data migration task. Valid values: NoStart: The backup data migration task is not started. Running: The backup data migration task is running. Success: The backup data migration task is successful. Failed: The migration task failed. Waiting: The backup data migration task is waiting for an incremental backup file to be imported. |
| PageRecordCo unt | Integer | 10 | The number of entries returned per page. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| RequestId | String | 4E356DDF-6B83- 45DB-99D5- 4B1E8A0D286B | The ID of the request. |
| TotalRecordCo unt | Integer | 30 | The total number of entries returned. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeMigrateTasks &DBInstanceId=rm-uf6wjk5xxxxxxx &StartTime=2017-10-20T01:00Z &EndTime=2017-10-25T01:00Z &<Common request parameters>
```

Sample success responses

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

ApsaraDB for RDS `XML` format

```xml
      <RequestId>A5409D02-D661-4BF3-8F3D-0A814D0574E7</RequestId>
      <PageRecordCount>1</PageRecordCount>
      <PageNumber>1</PageNumber>
      <TotalRecordCount>10</TotalRecordCount>
      <Items>
            <MigrateTaskId>rm-bp1842vxxxxx</MigrateTaskId>
            <DBName>test02</DBName>
            <CreateTime>2017-05-30 T12:11:4Z</CreateTime>
            <EndTime>2017-05-30 T12:11:4Z</EndTime>
            <IsDBReplaced>True</IsDBReplaced>
            <Status>Success</Status>
            <BackupMode>FULL</BackupMode>
            <Description>Api description</Description>
      </Items>
```

`JSON` format

```json
{
    "RequestId": "A5409D02-D661-4BF3-8F3D-0A814D0574E7",
    "PageRecordCount": 1,
    "PageNumber": 1,
    "TotalRecordCount": 10,
    "Items": {
        "MigrateTaskId": "rm-bp1842vxxxxx",
        "DBName": "test02",
        "CreateTime": "2017-05-30 T12:11:4Z",
        "EndTime": "2017-05-30 T12:11:4Z",
        "IsDBReplaced": "True",
        "Status": "Success",
        "BackupMode": "FULL",
        "Description": "Api description"
    }
}
```

#### DescribeOssDownloads

Queries the backup file details of a backup data migration task for an ApsaraDB RDS for SQL Server instance.

**Note**

This operation is not supported for instances that run SQL Server 2017 EE or SQL Server 2019 EE.

**Request parameters**

| Action | String | Yes | DescribeOssDow nloads | The operation that you want to perform. Set the value to DescribeOssDownloads. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. You can call the DescribeDBInstances operation to query the IDs of instances. |
| MigrateTaskId | String | Yes | 5625458541 | The ID of the backup data migration task. You can call the DescribeMigrateTasks operation to query the IDs of migration tasks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| Items | Array of OssDownload |  | Details of the backup files. |
| OssDownload |  |  |  |
| BackupMode | String | Database | The backup type. Valid values: Database: full backup files Differential Database: incremental _ backup files Transaction Log: log backup files _ |
| CreateTime | String | 2017-08- 17T12:45:15Z | The time when the backup file was created in the download list. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Description | String | App description | The description of the backup file. |
| FileName | String | test | The name of the backup file stored in Object Storage Service (OSS). |
| FileSize | String | 2 | The size of the backup file. Unit: MB |
| IsAvailable | String | True | Indicates whether the backup file is available. Valid values: True and False. |

ApsaraDB for RDS

**Response parameters**

| Status | String | Finished | The state of the backup file. Valid values: NoStart Downloading Finished DownloadFailed VerifyFailed Deleted DeleteFailed CheckSuccess CheckFailed Restoring Restored RestoredFailed |
|---|---|---|---|
| MigrateTaskId | String | 562154852 | The ID of the backup data migration task. |
| RequestId | String | A5409D02-D661- 4BF3-8F3D- 0A814D0574E7 | The ID of the request. |

ApsaraDB for RDS

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=DescribeOssDownloads &DBInstanceId=rm-uf6wjk5xxxxxxx &MigrateTaskId=5625458541 &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>A5409D02-D661-4BF3-8F3D-0A814D0574E7</RequestId>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <MigrateTaskId>562154852</MigrateTaskId>
      <Items>
            <OssDownload>
                  <Status>Finished</Status>
                  <Description>App description</Description>
                  <EndTime>2017-08-27T12:45:15Z</EndTime>
                  <IsAvailable>True</IsAvailable>
                  <BackupMode>Database</BackupMode>
                  <CreateTime>2017-08-17T12:45:15Z</CreateTime>
                  <FileName>test</FileName>
                  <FileSize>2</FileSize>
            </OssDownload>
      </Items>
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TagResources | The operation that you want to perform. Set the value to TagResources. |

ApsaraDB for RDS `JSON` format

```json
{
        "RequestId": "A5409D02-D661-4BF3-8F3D-0A814D0574E7",
        "DBInstanceId": "rm-uf6wjk5xxxxxxx",
        "MigrateTaskId": 562154852,
        "Items": {
            "OssDownload": {
                "Status": "Finished",
                "Description": "App description",
                "EndTime": "2017-08-27T12:45:15Z",
                "IsAvailable": "True",
                "BackupMode": "Database",
                "CreateTime": "2017-08-17T12:45:15Z",
                "FileName": "test",
                "FileSize": 2
            }
        }
    }
}
```

### Tag management

#### TagResources

Creates and adds tags to ApsaraDB RDS instances. If you have a large number of instances, you can create multiple tags and add these tags to the instances. Then, you can filter the instances by tag. A tag consists of a key and a value. Each key must be unique within a region for an Apsara Stack account. Different keys can be mapped to the same value. If the tag that you specify does not exist, this tag is automatically created and added to the specified instance. If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag. You can add up to 20 tags to each instance. You can add tags to up to 50 instances at a time.

**Request parameters**

| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to query the most recent region list. |
|---|---|---|---|---|
| ResourceId.N | RepeatL ist | Yes | rm- uf6wjk5xxxxxxx | The ID of Instance N. You can add tags to N instances at a time. Valid values of N: 1 to 50. |
| ResourceType | String | Yes | INSTANCE | The type of the resource. Set the value to INSTANCE. |
| Tag.N.Key | String | No | testkey1 | The key of Tag N. You can create N tag keys at a time. Valid values of N: 1 to 20. This parameter cannot be an empty string. |
| Tag.N.Value | String | No | testvalue1 | The value of Tag N. You can create N tag values at a time. Valid values of N: 1 to 20. This parameter can be an empty string. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 224DB9F7-3100- 4899-AB9C- C938BCCB43E7 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
&RegionId=cn-hangzhou &ResourceType=INSTANCE &ResourceId.1=rm-uf6wjk5xxxxxxx &Tag.1.Key=testkey1 &Tag.1.Value=testvalue1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
  <RequestId>224DB9F7-3100-4899-AB9C-C938BCCB43E7</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddTagsToReso urce | The operation that you want to perform. Set the value to AddTagsToResource. |
| RegionId | String | Yes | cn-hagnzhou | The region ID. You can call the DescribeRegions operation to query the most recent region list. |
| DBInstanceId | String | Yes | rm- uf6wjk5xxxxxxx | The ID of the instance. Note You can specify up to 30 instance IDs in a single request. Separate multiple instance IDs with commas (,). |
| Tags | String | No | {"key1":"value1 ","key2":""} | The tags that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. Format: {"key1":"value1","key2":"value2"...}. Note The tag key is required, and the tag value is optional. |

ApsaraDB for RDS

```json
{
    "RequestId":"224DB9F7-3100-4899-AB9C-C938BCCB43E7"
}
```

#### AddTagsToResource

Adds existing or new tags to an ApsaraDB RDS instance. This operation has the following limits: Each tag consists of a tag key and a tag value. The tag key is required, and the tag value is optional. Tag keys and tag values cannot start with aliyun. Tag keys and tag values are not case-sensitive. Each tag key can be up to 64 characters in length, and each tag value can be up to 128 characters in length. Up to 10 tags can be added to each instance. The tag keys of these tags must be unique. If you add two tags that have the same tag value to an instance, the new tag overwrites the existing tag.

**Request parameters**

| Tag.1.key | String | No | key1 | The key of the first tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
|---|---|---|---|---|
| Tag.2.key | String | No | key2 | The key of the second tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| Tag.3.key | String | No | key3 | The key of the third tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| Tag.4.key | String | No | key4 | The key of the fourth tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| Tag.5.key | String | No | key5 | The key of the fifth tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| Tag.1.value | String | No | value1 | The value of the first tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| Tag.2.value | String | No | value2 | The value of the second tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |

ApsaraDB for RDS

| Tag.3.value | String | No | value3 | The value of the third tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
|---|---|---|---|---|
| Tag.4.value | String | No | value4 | The value of the fourth tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| Tag.5.value | String | No | value5 | The value of the fifth tag that you want to add. Each tag consists of a tag key and a tag value. You can specify up to five tags in a single request. The tag key is required, and the tag value is optional. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| proxyId | String | No | API | The ID of the proxy mode. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 224DB9F7-3100- 4899-AB9C- C938BCCB43E7 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
http(s)://rds.example.com/?Action=AddTagsToResource &RegionId=cn-hagnzhou &DBInstanceId=rm-uf6wjk5xxxxxxx &Tags=%7B%22test%22%3A%221%22%7D &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListTagResource s | The operation that you want to perform. Set the value to ListTagResources. |
| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to query the most recent region list. |
| ResourceId.N | RepeatL ist | Yes | rm- uf6wjk5xxxxxxx | The ID of Instance N. You can query the tags that are added to N instances at a time. Valid values of N: 1 to 50. Note You must specify at least one of the ResourceId.N and Tag.N.Key parameters. |
| ResourceType | String | Yes | INSTANCE | The type of the resource. Set the value to INSTANCE. |
| NextToken | String | No | 212db86sca438 4811e0b5e8707 ec21345 | The token required to obtain more results. This parameter is not required in the first query. If a query does not return all results, in the next query, you can specify the token returned from the previous query to obtain more results. |

ApsaraDB for RDS

```xml
      <requestId>224DB9F7-3100-4899-AB9C-C938BCCB43E7</requestId>
```

`JSON` format

```json
{
    "requestId": "224DB9F7-3100-4899-AB9C-C938BCCB43E7"
}
```

#### ListTagResources

Queries the tags that are added to ApsaraDB RDS instances.

**Request parameters**

| Tag.N.Key | String | No | testkey1 | The key of Tag N. You can query N tag keys at a time. Valid values of N: 1 to 20. This parameter cannot be an empty string. Note You must specify at least one of the ResourceId.N and Tag.N.Key parameters. |
|---|---|---|---|---|
| Tag.N.Value | String | No | testvalue1 | The value of Tag N. You can specify N tag values at a time. Valid values of N: 1 to 20. This parameter can be an empty string. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NextToken | String | 212db86sca43848 11e0b5e8707ec21 345 | The token required to obtain more results. If this query does not return all results, in the next query, you can specify the token returned from this query to obtain more results. |
| RequestId | String | 47A514A1-4B77- 4E30-B4C5- 2A880650B3FD | The ID of the request. |
| TagResources | Array of TagResource |  | Details of the tags. |
| TagResource |  |  |  |
| ResourceId | String | rm-uf6wjk5xxxxxxx | The ID of the instance. |
| ResourceType | String | ALIYUN::RDS::INST ANCE | The resource type. The value ALIYUN::RDS::INSTANCE indicates ApsaraDB RDS instances. |
| TagKey | String | testkey1 | The key of the tag. |
| TagValue | String | testvalue1 | The value of the tag. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests ApsaraDB for RDS

```
http(s)://rds.example.com/?Action=ListTagResources &RegionId=cn-hangzhou &ResourceType=INSTANCE &ResourceId.1=rm-uf6wjk5xxxxxxx &Tag.1.Key=testkey1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
        <TagResource>
              <ResourceType>ALIYUN::RDS::INSTANCE</ResourceType>
              <TagValue>testvalue1</TagValue>
              <ResourceId>rm-uf6wjk5xxxxxxx</ResourceId>
              <TagKey>testkey1</TagKey>
        </TagResource>
  <RequestId>47A514A1-4B77-4E30-B4C5-2A880650B3FD</RequestId>
```

`JSON` format

```json
{
        "TagResource":[
            {
                "ResourceType":"ALIYUN::RDS::INSTANCE",
                "TagValue":"testvalue1",
                "ResourceId":"rm-uf6wjk5xxxxxxx",
                "TagKey":"testkey1"
            }
```

]

```json
    },
    "RequestId":"47A514A1-4B77-4E30-B4C5-2A880650B3FD"
}
```

#### UntagResources

Removes tags from ApsaraDB RDS instances.

**Note**

Up to 20 tags can be removed at a time. If a tag is removed from an instance and is not added to other instances, the tag is deleted.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UntagResources | The operation that you want to perform. Set the value to UntagResources. |
| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to query the most recent region list. |
| ResourceId.N | RepeatL ist | Yes | rm- uf6wjk5xxxxxxx | The ID of Instance N. You can remove tags from N instances at a time. Valid values of N: 1 to 50. |
| ResourceType | String | Yes | INSTANCE | The type of the resource. Set the value to INSTANCE. |
| TagKey.N | RepeatL ist | No | testkey1 | The key of Tag N. You can remove N tag keys at a time. Valid values of N: 1 to 20. This parameter cannot be an empty string. |
| All | Boolean | No | false | Specifies whether to remove all tags from the instance. Valid values: true false Default value: false. Note This parameter is valid when TagKey.N is not specified. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 601B6F25-21E7- 4484-99D5- 3EF2625C0088 | The ID of the request. |

ApsaraDB for RDS

**Response parameters**

**Examples**

Sample requests

```
&RegionId=cn-hangzhou &ResourceType=INSTANCE &ResourceId.1=rm-uf6wjk5xxxxxxx &TagKey.1=testkey1 &<Common request parameters>
```

| Resource | Resource description in authorization policy |
|---|---|
| Instance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid acs:rds:$regionid:$accountid:dbinstance/ acs:rds:::dbinstance/ |

| Operation 1 | Operation 2 |
|---|---|
| CreateDBInstance | ModifyDBInstanceSpec |
| DeleteDBInstance | CreateReadonlyDBInstance |
| DescribeDBInstances | DescribeDBInstanceAttribute |

ApsaraDB for RDS Sample success responses `XML` format

```xml
        <RequestId>601B6F25-21E7-4484-99D5-3EF2625C0088</RequestId>
```

`JSON` format

```json
{
    "RequestId":"601B6F25-21E7-4484-99D5-3EF2625C0088"
}
```

### RAM authorization

**Use RAM for RDS resource authorization**

All RDS instances created through an Apsara Stack tenant account are resources owned by that account. By default, you have full operation permissions on the resources under your account. Resource Access Management (RAM) allows you to grant RAM users the access and management permissions on RDS resources owned by an Apsara Stack tenant account. If you do not need to use RAM, ignore this topic.

**Resource types in RAM**

The only type of RDS resources that can be authorized through RAM is dbinstance. The following table lists the resource description method when the resources are authorized through RAM. The $regionid field must be the ID of a region or an asterisk (*). The $instanceid field must be the ID of an instance or an asterisk (*). Similarly, $account-id is the numerical ID of your Apsara Stack tenant account, which can be replaced by an asterisk (*).

**Authorization operations in RAM**

In RAM, the following operations can be authorized to an RDS resource.

| SwitchDBInstanceNetType | RestartDBInstance |
|---|---|
| ModifyDBInstanceDescription | ModifySecurityIps |
| ModifyDBInstanceMaintainTime | UpgradeDBInstanceEngineVersion |
| PurgeDBInstanceLog | CreateDatabase |
| DeleteDatabase | DescribeDatabases |
| ModifyDBDescription | ModifyeParameter |
| DescribeParameters | DescribeOptimizeAdviceByDBA |
| DescribeOptimizeAdviceOnMissIndex | ImportDataBaseBetweenInstances |
| CancelImport | CreateAccount |
| ResetAccountPassword | GrantAccountPrivilege |
| RevokeAccountPrivilege | DescribeAccounts |
| DeleteAccount | ModifyAccountDescription |
| CreateBackup | DescribeBackups |
| CreateTempDBInstance | DescribeBackupPolicy |
| ModifyBackupPolicy | DescribeResourceUsage |
| DescribeDBInstancePerformance | DescribeSlowLogs |
| DescribeSlowLogRecords | DescribeErrorLogs |
| DescribeBinlogFiles | DescribeSQLLogReports |
| DescribeSQLLogRecords | DescribeOptimizeAdviceOnStorage |
| DescribeOptimizeAdviceOnMissPK | DescribeOptimizeAdviceOnExcessIndex |

| Operation | Authentication rule |
|---|---|
| CreateDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DeleteDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDBInstances | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |

ApsaraDB for RDS

**Note**

All operations except DescribeRegions and DescribeParameterTemplates can be authorized.

**RAM authentication rules of API operations**

When you call API operations to access resources as a RAM user, the RDS backend checks whether the RAM user is granted the required permissions by querying RAM. The permissions to be checked are determined by the resources used by the API operation. The following table lists the authentication rules for each API operation.

| SwitchDBInstanceNetType | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
|---|---|
| ModifyDBInstanceDescription | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyDBInstanceMaintainTime | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| PurgeDBInstanceLog | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DeleteDatabase | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyDBDescription | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CancelImport | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ResetAccountPassword | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| RevokeAccountPrivilege | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DeleteAccount | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateBackup | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateTempDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyBackupPolicy | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDBInstancePerformance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSlowLogRecords | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeBinlogFiles | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSQLLogRecords | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnMissPK | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnMissIndex | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeParameters | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreatePrepaidDBInstanceForChannel | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyPrepaidDBInstanceSpec | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreatePostpaidDBInstanceForChannel | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyPostpaidDBInstanceSpec | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDBInstanceAttribute | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| RestartDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifySecurityIps | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| UpgradeDBInstanceEngineVersion | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateDatabase | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |

ApsaraDB for RDS

| DescribeDatabases | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
|---|---|
| ImportDataBaseBetweenInstances | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateAccount | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| GrantAccountPrivilege | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeAccounts | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyAccountDescription | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeBackups | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeBackupPolicy | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeResourceUsage | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSlowLogs | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeErrorLogs | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSQLLogReports | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnStorage | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnExcessIndex | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceByDBA | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyeParameter | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |

| Error code | Error message | HTTP status code |
|---|---|---|
| MissingParameter | The input parameter "parameter name" that is mandatory for processing this request is not supplied. | 400 |
| InvalidParameter | The specified parameter "Action or Version" is not valid. | 400 |
| InvalidAccessKeyId.NotFo und | The Access Key ID provided does not exist in our records. | 404 |
| IncompleteSignature | The request signature does not conform to Aliyun standards. | 400 |
| IllegalTimestamp | The input parameter "Timestamp" that is mandatory for processing this request is not supplied. | 400 |

ApsaraDB for RDS

### Appendix

#### Error codes on the client

##### Common errors

| InvalidOwnerId | The specified OwnerId is not valid. | 400 |
|---|---|---|
| InvalidOwnerAccount | The specified OwnerAccount is not valid. | 400 |
| InvalidOwner | OwnerId and OwnerAccount can't be used at one API access. | 400 |
| Throttling | Request was denied due to request throttling. | 400 |
| InvalidAction | The specified action is not valid. | 403 |
| ActionUnauthorized | The specified action is not available for you | 403 |
| UnsupportedHTTPMethod | This http method not supported. | 403 |
| UnsupportedParameter | The parameter "<parameter name>" is not supported. | 400 |
| Forbidden.InstanceNotFo und | The specified Instance is not found. | 404 |
| Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. | 403 |
| Forbedden.NotSupportRA M | This action does not support accessed by RAM mode. | 403 |
| Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 403 |
| InsufficientBalance | Your account does not have enough balance. | 400 |
| Forbidden.Authentication | This operation is forbidden by Aliyun Realname Authentication system. | 403 |
| Invalid<parameter name>.ValueNotSupport ed | The specified parameter “parameter name” is not valid. | 400 |
| Invalid<parameter name>.Malformed | The specified parameter "parameter name n" is not valid. | 400 |
| InvalidParameter | The specified parameter " parameter name n " is not valid. | 400 |

| Error code | Error message | HTTP status code |
|---|---|---|
| InvalidRegionId.NotFound | The DBInstanceId provided does not exist in our records. | 404 |
| InvalidSecurityIPList.Duplicate | The Security IP address is not in the available range or occupied. | 400 |
| InvalidSecurityIPListLength.Malform ed | The quota of security ip exceeds. | 400 |

ApsaraDB for RDS

##### Specific errors

| InvalidEngineVersionInRegion.NotAv ailable | The EngineVersion in the Region is not available. | 403 |
|---|---|---|
| InvaildEngineInRegion.NotAvailable | The Engine in the Region is not available. | 403 |
| InvaildDBInstanceClassInRegion.Not Available | The DBInstanceClass in the Region is not available. | 403 |
| OperationDenied | The resource is out of usage. | 403 |
| RegionUnauthorized | There is no authority to create instance in the specified region. | 403 |
| QuotaExceeded.CreateInstance | The quota of create instance exceeds. | 403 |
| InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist in our records. | 404 |
| MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. | 400 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 400 |
| OperationDenied.DBInstanceStorag eReduce | The operation is not permitted due to reduce storage. | 403 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to instance status. | 403 |
| DependencyViolation | The operation is not permitted due to instance mount read only or guard instance. | 403 |
| InvalidConnectionStringPrefix.Dupli cate | The connection string is not in the available range or occupied. | 400 |
| QuotaExceeded.SwitchTime | The quota of switch time exceed. | 400 |
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| InvalidSecurityIps.Duplicate | The quota of security ip exceeds. | 400 |
| OperationDenied.CurrentEngineVer sion | The operation is not permitted due to specified current version. | 400 |
| OperationDenied.ReadOnlyDBInstan ceLower | The operation is not permitted due to higher read only instance version. | 403 |
| OperationDenied.GuardDBInstanceL ower | The operation is not permitted due to higher guard instance version. | 403 |
| OperationDenied.MasterDBInstance State | The operation is not permitted due to status of master instance. | 403 |
| QuotaExceeded.DBName | The quota of db exceeds. | 400 |
| InvalidDBName.Duplicate | The Security db Name is not in the available range or occupied. | 400 |

ApsaraDB for RDS

| InvalidParameter.Keyword | The specified parameter "DBName" is keyword | 400 |
|---|---|---|
| OperationDenied.DBStatus | The operation is not permitted due to status of database. | 403 |
| OperationDenied.DBInstanceEngine | The operation is not permitted due to engine of instance. | 403 |
| FTPServiceUnavailable | The request has failed due to a temporary failure of the FTP server. | 403 |
| QuotaExceeded.Upload | The quota of file exceeds. | 403 |
| InvalidFileName.NotCompleted | The specified "FileName" is not completed. | 404 |
| InvalidFileName.NotAvailable | The specified "FileName" is not Available. | 404 |
| QuotaExceeded.FileSize | The quota of file size exceeds. | 403 |
| QuotaExceeded.DBInstanceStorage | The quota of instance storage exceeds. | 403 |
| InvalidDBInfo.Malformed | The specified parameter "DBInfo" is not valid or db not exist. | 400 |
| OperationDenied.Region | The operation is not permitted due to different region. | 403 |
| OperationDenied.Engine | The operation is not permitted due to different engine. | 403 |
| OperationDenied.DBInstanceId | The operation is not permitted due to DBInstanceId and SourceDBInstanceId is same. | 403 |
| InvalidTaskId.NotFound | The ImportId provided does not exist in our records. | 400 |
| OperationDenied.IncorrectTaskStat us | The operation is not permitted due to status of import. | 403 |
| InvalidAccountName.keyword | The specified parameter "AccountName" is a keyword. | 400 |
| InvalidAccountName.Duplicate | The Security db Name is not in the available range or occupied. | 400 |
| QuotaExceeded.AccountName | The quota of account exceeds. | 403 |
| OperationDenied.AccountStatus | The operation is not permitted due to status of account. | 403 |
| InvalidDBName.NotFound | The DBName provided does not exist in our records. | 404 |
| OperationDenied.AccountType | The operation is not permitted due to type of account. | 403 |
| OperationDenied.BackupJobExists | The operation is not permitted due to backup job exist. | 403 |

ApsaraDB for RDS

| OperationDenied.NoDatabase | The operation is not permitted due to no database. | 403 |
|---|---|---|
| InvalidStartTimeAndEndTime.Malfor med | The end time must be greater than the start time | 400 |
| OperationDenied.BackupJobExists | The operation is not permitted due to backup job exist. | 403 |
| InvalidBackupId.NotFound | The BackupId provided does not exist in our records. | 404 |
| OperationDenied.NotFoundBackup | The operation is not permitted due to no backup. | 403 |
| OperationDenied.BackupStatus | The operation is not permitted due to type of backup. | 403 |
| OperationDenied.BackupMethod | The operation is not permitted method of backup. | 403 |
| OperationDenied.TempDBInstanceE xists | The operation is not permitted due to temp instance exist. | 403 |
| Forbidden.Authentication | The operation is forbidden by Aliyun Realname Authentication System. | 403 |
| IncorrectDBInstanceConnType | Current DB instance conn type does not support this operation. | 404 |
| IncorrecttVpcId.Mismatch | The specified parameter "VpcId" is not valid. | 400 |
| IntranetNetTypeNotExists | Current DB instance net type does not support this operation. | 404 |
| InvalidDBInstanceName.NotFound | The DBInstanceId provided does not exist in our records. | 403 |
| InvalidConnectionMode.ValueNotSu pported | The specified parameter "ConnectionMode" is not valid. | 400 |
| InvalidConnectionString.Duplicate Specified | connection string already exists in the Aliyun RDS. | 403 |
| InvalidConnectionString.Duplicate Specified | connection string or port want to be modified is the same with current net type. | 400 |
| InvalidConnectionStringPrefix.Dupli cated | Specified connection string already exists in the Aliyun RDS. | 403 |
| InvalidCurrentConnectionString.Not Found | Specified current connection string doesn't exist. | 400 |
| InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist in our records. | 400 |
| InvalidDBInstanceId.QuotaExceeded | The quota of instance id exceeds. | 400 |
| InvalidDBInstanceNetType.NotFoun d | The Specified DB instance net type is not found. | 404 |

ApsaraDB for RDS

| InvalidDBinstanceNetType.ValueNot Support | The specified parameter "DBinstanceNetType" is not valid. | 400 |
|---|---|---|
| InvalidDBInstanceType.ValueNotSu pport | The specified parameter "DBInstanceType" is not valid. | 400 |
| InvalidEngineVersion.Malformed | The specified parameter "EngineVersion" is not valid. | 400 |
| InvalidInstanceNetworkType.ValueN otSupported | The specified parameter "InstanceNetworkType" is not valid. | 400 |
| InvalidParameter | The specified parameter "dbInstanceId" is not valid. | 400 |
| InvalidPort.Malformed | Specified port is not valid. | 400 |
| InvalidPrivateIpAddress.Duplicated | Specified private IP address is duplicated. | 400 |
| InvalidPrivateIpAddress.Mismatch | Specified private IP address is not in the CIDR block of virtual switch. | 400 |
| InvalidVPCId.NotFound | Specified virtual vpc is not found. | 400 |
| InvalidVSwitchId.Mismatch | Specified instance and virtual switch are not in the same zone. | 400 |
| InvalidVSwitchId.NotFound | Specified virtual switch is not found in specified VPC. | 400 |
| NetTypeExists | Specified net type already existed. | 400 |
| NetTypeExists | Specified public net type already existed. | 403 |
| OperationDenied.DBInstanceNetTyp e | The operation is not permitted due to net type of instance. | 403 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to status of instance. | 403 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 403 |
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| OperationDenied.Switch | Specified instance cannot be switched. | 400 |
| OperationDenied.Switch | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied | The resource is out of usage. | 403 |
| OperationDenied | The vpc cloudinstanceIp is use, please check params. | 406 |
| OperationDenied | The vpc service is error, please check params. | 400 |
| PARAMETER ERROR _ | The vpc request parameter may not be null. | 406 |

ApsaraDB for RDS

| PARAMETER MUST NOT NULL _ _ _ | The parameter must not be null. | 406 |
|---|---|---|
| PublicConnectionExists | PublicConnection exists. | 403 |
| bpcIzNoNotEqualsRdsMultIzNo | Specified vpc IzNo not equal rds IzNo. | 400 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to status of instance. | 403 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 403 |
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| OperationDenied.Switch | Specified instance cannot be switched. | 400 |
| OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied | The resource is out of usage. | 403 |
| OperationDenied | The vpc cloudinstanceIp is use, please check params. | 406 |
| OperationDenied | The vpc service is error, please check params. | 400 |
| PARAMETER ERROR _ | The vpc request parameter may not be null. | 406 |
| PARAMETER MUST NOT NULL _ _ _ | The parameter must not be null. | 406 |
| PublicConnectionExists | PublicConnection exists. | 403 |
| bpcIzNoNotEqualsRdsMultIzNo | Specified vpc IzNo not equal rds IzNo. | 400 |

| Error code | Error message | HTTP status code |
|---|---|---|
| ServiceUnavailabl e | The request has failed due to a temporary failure of the server. | 503 |
| InternalError | The request processing has failed due to some unknown error, exception or failure. | 500 |

| State | Description |
|---|---|
| Creating | An instance is being created. |
| Running | An instance is in the running state. |
| Deleting | An instance is being deleted. |

ApsaraDB for RDS

#### Error codes on the server

#### Instance states

| Rebooting | An instance is being restarted. |
|---|---|
| DBInstanceClassChanging | An instance is being upgraded or downgraded. |
| TRANSING | Data is being migrated. |
| EngineVersionUpgrading | Engine version is being upgraded. |
| TransingToOthers | Data is being migrated to other RDS instances. |
| GuardDBInstanceCreating | A disaster recovery instance is being created. |
| Restoring | A backup is being restored. |
| Importing | Data is being imported. |
| ImportingFromOthers | Data is being imported from other RDS instances. |
| DBInstanceNetTypeChanging | The network type is being switched between Intranet and Internet. |
| GuardSwitching | The instance is undergoing disaster recover failover. |
| INS CLONING _ | The instance is being cloned. |

| API parameter | Description |
|---|---|
| MySQL NetworkTraffic _ | The average inbound traffic to a MySQL instance per second and average outbound traffic from a MySQL instance per second. Unit: KB. |
| MySQL QPSTPS _ | The average number of SQL statements executed per second and average number of transactions per second. |
| MySQL Sessions _ | The number of active connections and total number of current connections. |
| MySQL InnoDBBufferRatio _ | The read hit rate of the InnoDB buffer pool, utilization of the InnoDB buffer pool, and percentage of dirty data blocks in the InnoDB buffer pool. |
| MySQL InnoDBDataReadW _ riten | The average volume of data that InnoDB reads per second and average volume of data that InnoDB writes per second. Unit: KB. |
| MySQL InnoDBLogRequest _ s | The average number of reads from the InnoDB buffer pool per second and average number of writes to the InnoDB buffer pool per second. |
| MySQL InnoDBLogWrites _ | The average number of log write requests per second, average number of physical writes performed on log files per second, and average number of fsync() writes to log files per second. |
| MySQL TempDiskTableCre _ ates | The number of temporary tables automatically created in the hard disk when MySQL statements are executed. |

ApsaraDB for RDS

#### Performance parameters

**ApsaraDB RDS for MySQL**

| MySQL MyISAMKeyBufferR _ atio | The average key buffer utilization of MyISAM per second, average key buffer read hit rate of MyISAM per second, and average key buffer write hit rate of MyISAM per second. |
|---|---|
| MySQL MyISAMKeyReadWr _ ites | The average number of data reads from the buffer pool by MyISAM per second, average number of data writes to the buffer pool by MyISAM per second, average number of data reads from the hard disk by MyISAM per second, and average number of data writes to the hard disk by MyISAM per second. |
| MySQL COMDML _ | The average number of DELETE statements executed per second, average number of INSERT statements executed per second, average number of INSERT SELECT statements executed per second, average _ number of REPLACE statements executed per second, and average number of REPLACE SELECT statements executed per second, average _ number of SELECT statements executed per second, and average number of UPDATE statements executed per second. |
| MySQL RowDML _ | The average number of rows read from the InnoDB table per second, average number of rows updated in the InnoDB table per second, average number of rows deleted from the InnoDB table per second, average number of rows inserted into the InnoDB table per second, and average number of physical writes to log files per second. |
| MySQL MemCpuUsage _ | The CPU utilization and memory usage of a MySQL instance within the entire operating system. |
| MySQL IOPS _ | The IOPS of a MySQL instance. |
| MySQL DetailedSpaceUsag _ e | The disk space occupied by a MySQL instance, including ins size (total _ space), data size (data space), log size (log space), tmp size _ _ _ (temporary space), and other size (system space). _ |
| slavestat | The latency of read-only instances. |

| API parameter | Description |
|---|---|
| SQLServer Transactions _ | The average number of transactions per second. |
| SQLServer Sessions _ | The total number of current connections. |
| SQLServer BufferHit _ | The buffer hit rate. |
| SQLServer FullScans _ | The average number of full table scans per second. |
| SQLServer SQLCompilations _ | The number of SQL compilations per second. |
| SQLServer CheckPoint _ | The number of checkpoints written to pages per second. |
| SQLServer Logins _ | The number of logons per second. |
| SQLServer LockTimeout _ | The number of lock timeouts per second. |
| SQLServer Deadlock _ | The number of deadlocks per second. |
| SQLServer LockWaits _ | The number of lock waits per second. |

ApsaraDB for RDS

**ApsaraDB RDS for SQL Server**

| SQLServer NetworkTraffic _ | The average inbound/outbound traffic to/from an SQL Server instance per second. Unit: KB. |
|---|---|
| SQLServer QPS _ | The average number of SQL statements executed per second. |
| SQLServer InstanceCPUUsage _ | The CPU utilization of an SQL Server instance within the entire operating system. |
| SQLServer IOPS _ | The IOPS of an SQL server instance. |
| SQLServer SpaceUsage _ | The space usage of an SQL Server instance within the entire operating system. |

| Parameter field | Keyword description |
|---|---|
| DBName/ AccountName | admin, aurora, replicator, xtrabak, root(MySQL5.5/5.6), mysql, test, eagleye, information schema, guest, add, analyze, asc, between, blob, call, c _ hange,check,condition,continue,cross,current timestamp,database,day micros _ _ econd,dec,default,desc,distinct,double,e ach,enclosed,exit,fetch,float8,foreign,goto,having,hour minute,ignore,infile,inse _ nsitive,int1,int4,interval,iterate,keys,lea ding,like,lines,localtimestamp,longblob,low priority,mediumint,minute microse _ _ cond,modifies,no write to binlog,on, _ _ _ optionally,out,precision,purge,read,references,rename,require,revoke,schema,s elect,set,spatial,sqlexception,sql big re _ _ sult,ssl,table,tinyblob,to,true,unique,update,using,utc timestamp,varchar,when, _ with,xor,all,and,asensitive,bigint,both,c ascade,char,collate,connection,convert,current date,current user,databases,da _ _ y minute,decimal,delayed,describe,dis _ tinctrow,drop,else,escaped,explain,float,for,from,grant,high priority,hour secon _ _ d,in,inner,insert,int2,int8,into,join,kill,le ave,limit,load,lock,longtext,match,mediumtext,minute second,natural,null,opti _ mize,or,outer,primary,raid0,reads,regex p,repeat,restrict,right,schemas,sensitive,show,specific,sqlstate,sql calc found r _ _ _ ows,starting,terminated,tinyint,trailing, undo,unlock,usage,utc date,values,varcharacter,where,write,year month,alter, _ _ as,before,binary,by,case,character,colu mn,constraint,create,current time,cursor,day hour,day second,declare,delete, _ _ _ deterministic,div,dual,elseif,exists,false, float4,force,fulltext,group,hour microsecond,if,index,inout,int,int3,integer,is,key _ ,label,left,linear,localtime,long,loop,me diumblob,middleint,mod,not,numeric,option,order,outfile,procedure,range,real,r elease,replace,return,rlike,second mi _ crosecond,separator,smallint,sql,sqlwarning,sql small result,straight join,then,t _ _ _ inytext,trigger,union,unsigned,use,utc _ time,varbinary,varying,while,x509,zerofill,galaxy |

ApsaraDB for RDS

#### Forbidden keywords

**ApsaraDB RDS for MySQL**

| Parameter field | Keyword description |
|---|---|
| DBName/ AccountName | root,admin,eagleye,master,aurora,sa,sysadmin,administrator,mssqld,public,security admin,serveradmin,setupadmin,pr ocessadmin,diskadmin,dbcreator,bulkadmin,tempdb,msdb,model,distribution,mssqls ystemresource,guest,add,except, percent,all,exec,plan,alter,execute,precision,and,exists,primary,any,exit,print,as,fetc h,proc,asc,file,procedure,authorizati on,fillfactor,public,backup,for,raiserror,begin,foreign,read,between,freetext,readtext, break,freetexttable,reconfigure,br owse,from,references,bulk,full,replication,by,function,restore,cascade,goto,restrict,c ase,grant,return,check,group,rev oke,checkpoint,having,right,close,holdlock,rollback,clustered,identity,rowcount,coale sce,identity insert,rowguidcol,coll _ ate,identitycol,rule,column,if,save,commit,in,schema,compute,index,select,constrain t,inner,session user,contains,insert, _ set,containstable,intersect,setuser,continue,into,shutdown,convert,is,some,create,jo in,statistics,cross,key,system user, _ current,kill,table,current date,left,textsize,current time,like,then,current timestamp, _ _ _ lineno,to,current user,load,top,cur _ sor,national,tran,database,nocheck,transaction,dbcc,nonclustered,trigger,deallocate ,not,truncate,declare,null,tsequal, default,nullif,union,delete,of,unique,deny,off,update,desc,offsets,updatetext,disk,on, use,distinct,open,user,distributed, opendatasource,values,double,openquery,varying,drop,openrowset,view,dummy,op enxml,waitfor,dump,option,when, else,or,where,end,order,while,errlvl,outer,with,escape,over,writetext,galaxy |

| RDS edition | Instanc e family | Instance type | CPU and memory | Maxi mum conn ectio ns | Maxi mum IOPS | Storage capacity | Zone- disaste r recove ry deploy ment |
|---|---|---|---|---|---|---|---|

ApsaraDB for RDS

**ApsaraDB RDS for SQL Server**

#### Instance specifications

Instances of different editions, versions, and instance types each perform differently from one another. Table 1. ApsaraDB RDS for MySQL instance specifications

| High- availabil ity Edition | Dedicat ed (X8) | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysql.x8.medium .2 | 2 cores, 16 GB | 2,500 | 4,500 | 50 GB to 1,000 GB (in 5 GB increments ) | Single- data center deploy ment and dual- data center deploy ment |
|---|---|---|---|---|---|---|---|
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysql.x8.large.2 | 4 cores, 32 GB | 5,000 | 9,000 | 50 GB to 1,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysql.x8.xlarge.2 | 8 cores, 64 GB | 10,00 0 | 18,00 0 | 500 GB to 3,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysql.x8.2xlarge. 2 | 16 cores, 128 GB | 20,00 0 | 36,00 0 | 500 GB to 3,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysql.x8.4xlarge. 2 | 32 cores, 256 GB | 40,00 0 | 72,00 0 | 1,000 GB to 6,000 GB |  |
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysql.x8.8xlarge. 2 | 64 cores, 512 GB | 80,00 0 | 144,0 00 |  |  |
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysql.x4.large.2 | 4 cores, 16 GB | 2,500 | 4,500 | 50 GB to 1,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysql.x4.xlarge.2 | 8 cores, 32 GB | 5,000 | 9,000 | 500 GB to 3,000 GB (in 5 GB increments ) |  |

ApsaraDB for RDS

|  | Dedicat |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysql.x4.2xlarge. 2 | 16 cores, 64 GB | 10,00 0 | 18,00 0 | 500 GB to 3,000 GB (in 5 GB increments ) |  |
|  | ed (X4) |  |  |  |  |  |  |
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysql.x4.4xlarge. 2 | 32 cores, 128 GB | 20,00 0 | 36,00 0 | 500 GB to 3,000 GB (in 5 GB increments ) |  |
|  | Dedicat ed host | MySQL 5.6, MySQL 5.7, and MySQL 8.0 rds.mysql.st.v52 | 90 cores, 720 GB | 150,0 00 | 140,0 00 | 1,000 GB to 6,000 GB |  |
|  |  | MySQL 5.6 and MySQL 5.7 rds.mysql.st.h43 | 60 cores, 470 GB | 150,0 00 | 120,0 00 |  |  |
|  | Dedicat ed (with a large number of cores) | MySQL 5.7 mysql.x4.large.25 | 4 cores, 16 GB | 2,500 | 4,500 | 50 GB to 1,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.7 mysql.x4.xlarge.2 5 | 8 cores, 32 GB | 5,000 | 9,000 | 500 GB to 3,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.7 mysql.x4.2xlarge. 25 | 16 cores, 64 GB | 10,00 0 | 18,00 0 | 500 GB to 3,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.7 mysql.x4.4xlarge. 25 | 32 cores, 128 GB | 20,00 0 | 36,00 0 | 1000 GB to 3,000 GB (in 5 GB increments ) |  |

ApsaraDB for RDS

| RDS Enterpri se Edition |  |  |  |  |  |  | Single- data center Enterpri se Edition deploy ment |
|---|---|---|---|---|---|---|---|
|  | Dedicat ed (with a large memory capacit y) | MySQL 5.7 mysql.x8.medium .25 | 2 cores, 16 GB | 2,500 | 4,500 | 50 GB to 1,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.7 mysql.x8.xlarge.2 5 | 4 cores, 32 GB | 5,000 | 9,000 | 50 GB to 1,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.7 mysql.x8.xlarge.2 5 | 8 cores, 64 GB | 10,00 0 | 18,00 0 | 500 GB to 3,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.7 mysql.x8.2xlarge. 25 | 16 cores, 128 GB | 20,00 0 | 36,00 0 |  |  |
|  |  | MySQL 5.7 mysql.x8.4xlarge. 25 | 32 cores, 256 GB | 40,00 0 | 72,00 0 | 1000 GB to 3,000 GB (in 5 GB increments ) |  |
|  | Dedicat ed host | MySQL 5.7 mysql.st.8xlarge.2 5 | 60 cores, 470 GB | 100,0 00 | 120,0 00 | 1,000 GB to 6,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.7 mysql.st.12xlarge. 25 | 90 cores, 720 GB | 150,0 00 | 140,0 00 | 1,000 GB to 6,000 GB (in 5 GB increments ) |  |

ApsaraDB for RDS

| Read- only instanc e | Dedicat ed (X8) | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysqlro.x8.mediu m.1 | 2 cores, 16 GB | 2,500 | 4,500 | 50 GB to 1,000 GB (in 5 GB increments ) | Single- data center deploy ment and dual- data center deploy ment |
|---|---|---|---|---|---|---|---|
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysqlro.x8.large. 1 | 4 cores, 32 GB | 5,000 | 9,000 | 50 GB to 1,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysqlro.x8.xlarge .1 | 8 cores, 64 GB | 10,00 0 | 18,00 0 | 500 GB to 3,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysqlro.x8.2xlarg e.1 | 16 cores, 128 GB | 20,00 0 | 36,00 0 | 500 GB to 3,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysqlro.x8.4xlarg e.1 | 32 cores, 256 GB | 40,00 0 | 72,00 0 | 1,000 GB to 6,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysqlro.x8.8xlarg e.1 | 64 cores, 512 GB | 80,00 0 | 14,40 0 | 1,000 GB to 6,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysqlro.x4.large. 1 | 4 cores, 16 GB | 2,500 | 4,500 | 50 GB to 1,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysqlro.x4.xlarge .1 | 8 cores, 32 GB | 5,000 | 9,000 | 50 GB to 1,000 GB (in 5 GB increments ) |  |

ApsaraDB for RDS

|  | Dedicat |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysqlro.x4.2xlarg e.1 | 16 cores, 64 GB | 10,00 0 | 18,00 0 | 500 GB to 3,000 GB (in 5 GB increments ) |  |
|  | ed (X4) |  |  |  |  |  |  |
|  |  | MySQL 5.6, MySQL 5.7, and MySQL 8.0 mysqlro.x4.4xlarg e.1 | 32 cores, 128 GB | 20,00 0 | 36,00 0 | 500 GB to 3,000 GB (in 5 GB increments ) |  |
|  | Dedicat ed host | MySQL 5.6, MySQL 5.7, and MySQL 8.0 rds.mysql.st.v52 | 90 cores, 720 GB | 150,0 00 | 140,0 00 | 1,000 GB to 6,000 GB (in 5 GB increments ) |  |
|  |  | MySQL 5.6 and MySQL 5.7 rds.mysql.st.h43 | 60 cores, 470 GB | 100,0 00 | 120,0 00 |  |  |

| RDS editio n | Data base engi ne versi on | Instan ce family | Instance type | CPU and memor y | Maxi mu m con nect ions | Maxi mu m IOPS | Storage capacity | Zone- disast er recov ery deplo yment |
|---|---|---|---|---|---|---|---|---|

ApsaraDB for RDS Table 2. ApsaraDB RDS for SQL Server instance specifications

|  | SQL Serv er 2008 R2 | Dedica ted | mssql.x8.mediu m.2 | 2 cores, 16 GB | 2,50 0 | 4,50 0 | 250 GB | Single- data center deploy ment and dual- data center deploy ment. This instan ce type is not availa ble in new data center s, and does not suppor t V5 server s. |
|---|---|---|---|---|---|---|---|---|
|  |  |  | mssql.x8.large.2 | 4 cores, 32 GB | 5,00 0 | 9,00 0 | 500 GB |  |
|  |  |  | mssql.x8.xlarge. 2 | 8 cores, 64 GB | 10,0 00 | 18,0 00 | 1,000 GB |  |
|  |  |  | mssql.x8.2xlarg e.2 | 16 cores, 128 GB | 20,0 00 | 36,0 00 | 2,000 GB |  |
|  |  | Dedica ted host | rds.mssql.st.d13 | 30 cores, 220 GB | 64,0 00 | 20,0 00 | 2 TB |  |
|  |  |  | mssql.x4.mediu m.e2 | 2 cores, 8 GB |  |  |  |  |
|  |  |  | mssql.x8.mediu m.e2 | 2 cores, 16 GB |  |  |  |  |
|  |  |  | mssql.x4.large.e 2 | 4 cores, 16 GB |  |  |  |  |
|  |  |  | mssql.x8.large.e 2 | 4 cores, 32 GB |  |  |  |  |
|  |  |  | mssql.x4.xlarge. e2 | 8 cores, 32 GB |  |  |  |  |
|  |  |  | mssql.x8.xlarge. e2 | 8 cores, 64 GB |  |  |  |  |
|  |  |  | mssql.x4.2xlarg e.e2 | 16 cores, 64 GB |  |  |  |  |

ApsaraDB for RDS

| High- availab ility Edition | SQL Serv er 2012 EE: 2012 ent _ _ ha SQL Serv er 2016 EE: 2016 ent _ _ ha | Dedica ted |  |  |  | Depe nden |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  | mssql.x8.2xlarg e.e2 | 16 cores, 128 GB |  |  |  |  |
|  |  |  | mssql.x4.3xlarg e.e2 | 24 cores, 96 GB |  |  |  |  |
|  |  |  | mssql.x4.4xlarg e.e2 | 32 cores, 128 GB |  |  |  |  |
|  |  |  | mssql.x8.4xlarg e.e2 | 32 cores, 256 GB |  |  |  |  |
|  |  |  |  |  | Unli mite d | t on the perfo rman ce of clou d disks | 20 GB to 4,000 GB | Single- data center deploy ment |
|  |  |  | mssql.x8.7xlarg e.e2 | 56 cores, 480 GB |  |  |  |  |
|  |  |  | mssql.x4.8xlarg e.e2 | 64 cores, 256 GB |  |  |  |  |
|  |  |  | mssql.x8.8xlarg e.e2 | 64 cores, 512 GB |  |  |  |  |
|  | SQL Serv er 2012 SE: 2012 std _ _ ha | Dedica ted | mssql.x4.mediu m.s2 | 2 cores, 8 GB |  |  |  |  |
|  |  |  | mssql.x8.mediu m.s2 | 2 cores, 16 GB |  |  |  |  |
|  |  |  | mssql.x4.large.s 2 | 4 cores, 16 GB |  |  |  |  |
|  |  |  | mssql.x8.large.s 2 | 4 cores, 32 GB |  |  |  |  |
|  |  |  | mssql.x4.xlarge. s2 | 8 cores, 32 GB |  |  |  |  |
|  |  |  | mssql.x8.xlarge. s2 | 8 cores, 64 GB |  |  |  |  |

ApsaraDB for RDS

|  | SQL Serv er 2016 SE: 2016 std _ _ ha |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  | mssql.x4.2xlarg e.s2 | 16 cores, 64 GB |  |  |  |  |
|  |  |  | mssql.x8.2xlarg e.s2 | 16 cores, 128 GB |  |  |  |  |
|  |  |  | mssql.x4.3xlarg e.s2 | 24 cores, 96 GB |  |  |  |  |

| RDS edition | Databa se engine versio n | Instanc e family | Instanc e type | CPU and memor y | Maxim um connec tions | Maxim um IOPS | Storag e capacit y | Zone- disaste r recove ry deploy ment |
|---|---|---|---|---|---|---|---|---|
| High- availabi lity Edition | PolarDB 11 | Dedicat ed | polardb .x4.sma ll.2 | 1 core, 4 GB | 200 | 5,000 | 250 GB | Single- data center deploy ment and dual- data center deploy ment |
|  |  |  | polardb .x4.med ium.2 | 2 cores, 8 GB | 400 | 10,000 |  |  |
|  |  |  | polardb .x8.med ium.2 | 2 cores, 16 GB | 2,500 | 15,000 |  |  |
|  |  |  | polardb .x4.larg e.2 | 4 cores, 16 GB | 2,500 | 20,000 | 250 GB to 500 GB (in 5 GB increme nts) |  |
|  |  |  | polardb .x8.larg e.2 | 4 cores, 32 GB | 5,000 | 30,000 |  |  |
|  |  |  | polardb .x4.xlar ge.2 | 8 cores, 32 GB | 5,000 | 40,000 | 500 GB to 1,000 GB (in 5 GB increme nts) |  |
|  |  |  | polardb .x8.xlar ge.2 | 8 cores, 64 GB | 10,000 | 60,000 |  |  |

ApsaraDB for RDS

|  |  |  | polardb .x4.2xla rge.2 | 16 cores, 64 GB | 10,000 | 80,000 | 1,000 GB to 2,000 GB (in 5 GB increme nts) |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  | polardb .x8.2xla rge.2 | 16 cores, 128 GB | 12,000 | 120,00 0 |  |  |
|  |  |  | polardb .x4.4xla rge.2 | 32 cores, 128 GB | 12,000 | 160,00 0 | 2,000 GB to 3,000 GB (in 5 GB increme nts) |  |
|  |  |  | polardb .x8.4xla rge.2 | 32 cores, 256 GB | 12,000 | 240,00 0 |  |  |
|  |  |  | rds.pola rdb.st.h 43 | 60 cores, 470 GB | 12,000 | 450,00 0 | 6,000 GB |  |
|  |  | Dedicat ed host |  |  |  |  |  |  |

| RDS edition | Databa se engine versio n | Instanc e family | Instanc e type | CPU and memor y | Maxim um connec tions | Maxim um IOPS | Storag e capacit y | Zone- disaste r recove ry deploy ment |
|---|---|---|---|---|---|---|---|---|
|  |  | Dedicat ed (with a large memor y capacit y) | pg.x8.m edium.2 | 2 cores, 16 GB | 2,500 | 4,500 | 20 GB to 6,000 GB |  |
|  |  |  | pg.x8.la rge.2 | 4 cores, 32 GB | 5,000 | 9,000 |  |  |
|  |  |  | pg.x8.xl arge.2 | 8 cores, 64 GB | 10,000 | 18,000 |  |  |
|  |  |  | pg.x8.2 xlarge.2 | 16 cores, 128 GB | 12,000 | 36,000 |  |  |

ApsaraDB for RDS Table 4. ApsaraDB RDS for PostgreSQL instance specifications

| High- availabi lity Edition or read- only instanc e | Postgre SQL 9.4 and Postgre SQL 10 |  |  |  |  |  | (in 5 GB increme nts) | Single- data center deploy ment and dual- data center deploy ment |
|---|---|---|---|---|---|---|---|---|
|  |  | Dedicat ed (with a large number of cores) | pg.x4.la rge.2 | 4 cores, 16 GB | 2,500 | 4,500 |  |  |
|  |  |  | pg.x4.xl arge.2 | 8 cores, 32 GB | 5,000 | 9,000 |  |  |
|  |  |  | pg.x4.2 xlarge.2 | 16 cores, 64 GB | 10,000 | 18,000 |  |  |
|  |  |  | pg.x4.4 xlarge.2 | 32 cores, 128 GB | 12,000 | 36,000 |  |  |
|  |  | Dedicat ed host | rds.pg.s t.h43 | 60 cores, 470 GB | 4,000 | 50,000 |  |  |

ApsaraDB for RDS
