---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Server Guard Advanced Edition Server Guard Advanced Edition Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 225
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Server Guard Advanced Edition Server Guard Advanced Edition Developer Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E5%AE%89%E5%85%A8%E4%B8%AD%E5%BF%83%EF%BC%88%E5%AE%89%E9%AA%91%E5%A3%AB%EF%BC%89%EF%BC%88%E4%B8%93%E6%9C%89%E4%BA%91%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Alibaba%20Cloud%20Security-Server%20Guard%20Advanced%20Edition%20Server%20Guard%20Advanced%20Edition%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Server Guard Advanced Edition Server Guard Advanced Edition Developer Guide 20260828

## Preparations

### Obtain API information and

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
7. Select an API operation and obtain the POP endpoint of the cloud service on the Parameter
tab.

### Obtain an AccessKey pair

Access credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You can use one type of access credential for authentication when you make an API request. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign an access credential for authentication. An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An access credential that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an AccessKey pair assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs to personal accounts and organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

**Warning**

The AccessKey pair of a personal account is managed and limited by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain an organization ID, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. Click the profile picture in the upper-right corner of the page and click **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of the personal account.

**Note**

The AccessKey pair provides full permissions on cloud resources within your Alibaba Cloud account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. On the right side of the page that appears, click **Management AccessKey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### Obtain the values of common

**request headers**

You must specify multiple request headers when you call Apsara Stack API operations. This topic describes the common request headers and how to obtain the values of the request headers. This topic also describes the return values of specific parameters after you call API operations.

**Common request headers**

| Header | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain region IDs, see Obtain a region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see Obtain a resource set ID. |
| x-acs-instanceid | The ID of the instance that you want to manage. For more information about how to obtain instance IDs, see Obtain an instance ID. |

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the required organization.
5. In the **Regions** section, view the region ID.

**Obtain an organization ID**

You must call an operation to obtain an organization ID. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You must call an operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide.

**Obtain an instance ID**

You can obtain the ID of an instance in a service console of the Apsara Uni-manager Management Console. This section uses the Elastic Compute Service (ECS) console as an example. Perform the following operations to obtain the ID of an ECS instance:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Elastic Computing** > **Elastic Compute**
**Service**.
3. In the left-side navigation pane, click **Instances**.
4. View the **instance ID** in the instance list.
The following table describes the additional response parameters that are returned by default when you call API operations to query the instances of cloud services.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

### Obtain an AccessKey pair

**assigned by STS**

This topic describes how to use Security Token Service (STS) to make API calls.

**Background information**

Alibaba Cloud STS allows you to manage temporary credentials to your Alibaba Cloud resources. You can use STS to make API calls. An AccessKey pair assigned by STS consists of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to make API calls, you must use an AccessKey pair assigned by STS.

**Procedure**

1. Obtain your `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click **User**
**Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view your `RAM role` .
2. Obtain the AccessKey pair assigned by STS.

**Note**

You must use the actual values to replace the variables in the following sample code. The angle brackets <> are not retained in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourRoleSessionName>: Replace it with your current session name. In most cases, this variable is set to the identity of the user who make API calls. Example: Username. You can distinguish the users who assume the same RAM role to perform operations based on the value of the `RoleSessionName` variable. This way, you can perform user-specific auditing. The value of this variable must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (_). <yourRoleArn>: Replace it with the Alibaba Cloud Resource Name (ARN) of your RAM role. "sts.aliyuns.com": Replace it with the endpoint of STS.

```java
public static void main(String[] args) {
    // Create a DefaultAcsClient instance and initialize it.
    // Replace <yourRegionID>, <yourAccessKeyID>, and <yourAccessKeySecret> with the
actual region ID, your AccessKey ID, and your AccessKey secret.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourAccessKeyID>", "<yourAccessKeySecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    String assumeRole = callAssumeRole(client);
    if (StringUtils.isEmpty(assumeRole)) return;
    JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
    JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
    // Obtain the AccessKey pair assigned by STS.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace "sts.aliyuns.com" with the actual endpoint of STS. The format of an ST
S endpoint is sts-vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRoleSessionName>" with the name of the current session.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // The ARN of your RAM role. Replace "<yourRoleArn>" with the ARN of your RAM rol
e that is obtained in the previous step.
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
    return null;
```

3. Use the AccessKey pair assigned by STS to call an operation of a cloud service. The
following sample code provides an example on how to use the AccessKey pair assigned by STS to call the `DescribeZones` operation of Elastic Compute Service (ECS):

**Note**

You must use the actual values to replace the variables in the following sample code. The angle brackets <> are not retained in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourStsAccesskeyID>: Replace it with your STS AccessKey ID. <yourStsAccessKeySecret>: Replace it with your STS AccessKey secret. <yourStsToken>: Replace it with the security token of the AccessKey pair assigned by STS. <yourResourceGroupID>: Replace it with the actual resource set ID. <yourOrganizationID>: Replace it with the actual organization ID.

```java
public static void main(String[] args) {
    // Replace "<yourRegionID>" with the actual region ID.
    // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessK
ey ID and AccessKey secret of the AccessKey pair assigned by STS. The AccessKey ID an d AccessKey secret are obtained in the previous step.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccesskey>", "<yourStsAccessSecret>");
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
    // Replace "<yourRegionID>" with the actual region ID.
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
    // Replace "<yourStsToken>" with the STS token of the AccessKey pair assigned by
STS. The STS token is obtained in the previous step.
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
    // Optional. Replace "<yourResourceGroupID>" with the actual resource set ID.
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
    // Optional. Replace "<yourOrganizationID>" with the actual organization ID.
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

## Call examples

### Call examples for SDK for Java

#### Use SDK

##### Install SDK for Java

This topic describes how to install and use Apsara Stack Security SDK for Java. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK. For more information, visit Alibaba Cloud SDKs. If you want to use Apsara Stack Security SDK for Java, you must install the core library of Apsara Stack SDK for Java. We recommend that you use V4.5.17 or later of the core library. When you install the core library, you must add the following dependency to the pom.xml file. For more information about the specific SDK version, visit Alibaba Cloud SDKs.

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

##### Use CommonRequest

Before you call the SDK for Java to access the endpoint of a cloud service by using the Point of Presence (POP) gateway, you must familiarize yourself with the call style of the cloud service. The following call styles are supported: remote procedure call (RPC) and resource-oriented architecture (ROA).

**Prerequisites**

We recommend that you use CommonRequest to call Apsara Stack API operations. To view the recommended SDK version and sample code, perform the following operations: Log in to the Apsara Uni-manager Management Console. In the top navigation bar, choose **Products** >
**Development Tools** > **API & SDK** > **OpenAPI Explorer**. In the top navigation bar of the
page that appears, choose **API Integration** > **API Debugging**.

**Important**

We recommend that you do not download SDKs fromSDK Centerand use them in Apsara Stack. SDKs for the Alibaba Cloud public cloud may not support Apsara Stack API operations and may have compatibility issues. Proceed with caution.

**Use CommonRequest to call API operations**

The following sample code provides an example on how to call RPC API operations. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");
        // Ignore SSL certificate verification.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the timeout period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and specify the request parameters.
        CommonRequest request = new CommonRequest();
        // Specify the request method.
        request.setSysMethod(MethodType.POST);
        // Specify the endpoint of the service.
        request.setSysDomain("<apigatewayEndpoint>");
        // Specify the API version.
        request.setSysVersion("2016-07-14");
        // Specify the name of the service that you want to access and the region where
the service resides.
        request.setSysLocationProduct("apigateway");
        // Specify the name of the API operation.
        request.setSysAction("DescribeApiGroups");
        // If you use access credentials assigned by Security Token Service (STS) to ca
ll RPC API operations, you must specify the SecurityToken parameter.
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");
        // Configure service-related parameters.
        request.putQueryParameter("PageSize", "10");
        request.putQueryParameter("PageNumber", "1");
        // Required. Specify the call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0
and earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. Specify the ID of the resource set.
```

```java
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. The instance ID. This parameter is required for the modify and del
ete operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
        try {
            // Initiate the request and handle the response or exception.
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

The following sample code provides an example on how to call ROA API operations. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06-07. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");
        // Ignore SSL certificate verification.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the timeout period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
//CreateanAPIrequestandspecifytherequestparameters
```

```java
        // Create an API request and specify the request parameters.
        CommonRequest request = new CommonRequest();
        // Specify the request protocol to HTTPS.
        request.setSysProtocol(ProtocolType.HTTP);
        // Specify the request method.
        request.setSysMethod(MethodType.GET);
        // Specify the endpoint of the service.
        request.setSysDomain("<crEndpoint>");
        // Specify the API version.
        request.setSysVersion("2016-06-07");
        // Specify the uriPattern parameter, which is required for ROA APIs.
        request.setSysUriPattern("/namespace");
        // Specify the name of the service that you want to access and the region where
the service resides.
        request.setSysLocationProduct("cr");
        // Specify the name of the API operation.
        request.setSysAction("GetNamespaceList");
        // Required. Specify the call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0
and earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. Specify the ID of the resource set.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. The instance ID. This parameter is required for the modify and del
ete operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
        // If you use access credentials assigned by STS to call ROA API operations, yo
u must add the x-acs-security-token field to the header.
        // request.putHeadParameter("x-acs-security-token", "<your-securitytoken>");
        try {
            // Initiate the request and handle the response or exception.
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

**Important**

By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be disabled in the test environment, you can specify the following setting: Java

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Disable server certificate verification. clientConfig.setIgnoreSSLCerts(true)
```

### Call examples for SDK for

**Python**

#### Use SDK

##### Install SDK for Python

This topic describes how to install and use SDK for Python. Apsara Stack SDK for Python supports Python 2.6.x, Python 2.7.x, and Python 3.x or later. You can install Apsara Stack SDK for Python by using pip.

**Note**

To use the SDK of an Apsara Stack service, you must install the core library of Apsara Stack SDK for Python. If you use Python 2.x, run the following command to install the core library:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library:

```
pip3 install aliyun-python-sdk-core-v3
```

##### Use CommonRequest

This topic describes how to use the POP Python software development kit (SDK) to call cloud product APIs.

**Prerequisites**

In Apsara Stack, use CommonRequest to make API calls. You can find the recommended SDK version and sample code in the Apsara Uni-manager Management Console. To do this, navigate to **Products** > **Development Tools** > **API And Tools** > **Developer Portal** and select **API Integration** > **API Debugging**.

**Important**

Do not download SDKs directly from the SDK Center for Apsara Stack scenarios. The SDKs for the public cloud may not support Apsara Stack APIs or have compatibility issues. Use them with caution.

**Background information**

Currently, you can call APIs only using the Remote Procedure Call (RPC) method.

**CommonRequest call example**

The following example shows how to call the DescribeInstances operation of ECS. The API version is 2014-05-26. The following is the sample code:

```java
from aliyunsdkcore.client import AcsClient import os from aliyunsdkcore.request import CommonRequest
# Create an AcsClient instance.
client = AcsClient(
    "<AccessKey ID>",
    "<AccessKey secret>",
    "<your-RegionID>",
    timeout=1000,  # Set the timeout period.
    verify=False, # Ignore the certificate or set verify='<certificate_path>'.
```

);

```python
# Use with HTTPS.
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def describe_api_groups():
    # Create a request and set its parameters.
    request = CommonRequest()
    # When you call an RPC API using an STS AccessKey pair, add the SecurityToken field
to the parameters.
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-
SecurityToken>"};
    params = {"PageSize":"10","PageNumber":"1"};
    request.set_query_params(params)
    headers = {
        # Required. A description of the call source.
        "x-acs-caller-sdk-source":"ApiTestDemo",
        # Optional. Required for versions earlier than Enterprise Edition V3.15.0.
        "x-acs-regionid":"<your-RegionID>",
        # Optional. The resource group ID.
        "x-acs-resourcegroupid":"<your-ResourceGroupID>",
        # Required. The organization ID.
        "x-acs-organizationid":"<your-OrganizationID>"
        # Optional. Required for modify and delete operations.
        # "x-acs-instanceid":"<your-InstanceID>"
```

```python
    request.set_headers(headers)
    request.set_version("2016-07-14")
    request.set_action_name("DescribeApiGroups")
    request.set_endpoint("<ApigatewayEndpoint>")   // Replace <ApigatewayEndpoint> with
the actual endpoint.
    request.set_product("apigateway")
    request.set_method("POST")
    # Initiate the API request and print the return value.
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    describe_api_groups()
```

**Set a proxy**

When you call an API, you may need to set the HTTP_PROXY and HTTPS_PROXY environment variables. The following is the sample code:

```bash
# HTTPS proxy
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# HTTP proxy
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

**HTTPS configuration**

This section describes how to access OpenAPI using the HTTPS protocol.

**Use the HTTPS protocol**

By default, the SDK uses the HTTPS protocol.

```
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Region ID
```

`)`

```
request = DescribeInstancesRequest() request.set_protocol_type('https') # Use HTTPS. client.do_action_with_exception(request)
```

**Ignore certificates**

**Important**

When you access OpenAPI using the HTTPS protocol, the SDK verifies the SSL/TLS certificate by default. If your code environment does not have a certificate, a certificate verification error is reported. To ensure secure communication in a production environment, keep this verification enabled. If you must ignore certificate verification in a test environment, set the `verify` parameter.

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Region ID
    verify=False  # Ignore SSL certificate verification.
```

`)`

**Specify a CA certificate file**

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Region ID
    verify='./cacert.pem'  # Certificate path
```

`)`

### Call examples for SDK for Go

#### Use SDK

##### Install the core package of SDK for Go

This topic describes how to install the core package of SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

##### Use CommonRequest

This topic describes how to use the POP Go software development kit (SDK) to make API calls.

**Prerequisites**

For Apsara Stack, use CommonRequest to make API calls. In the Apsara Uni-manager Management Console, go to **Products** > **Development Tools** > **API And Tools** >
**Developer Portal**. Then, choose **API Integration** > **API Debugging** to view the
recommended SDK versions and sample code.

**Important**

Do not download SDKs directly from the SDK Center for Apsara Stack environments. SDKs for the Alibaba Cloud public cloud might not support Apsara Stack APIs and can cause compatibility issues. Use them with caution.

**Background information**

You can call APIs using the Remote Procedure Call (RPC) or Resource-Oriented Architecture (ROA) style.

**CommonRequest call examples**

The API information for the RPC example is as follows: Product (apigateway), API operation (DescribeApiGroups), and Version (2016-07-14). The following code is an example:

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
cessKey secret>")
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<ApigatewayEndpoint>"
    request.Version = "2016-07-14"
    request.ApiName = "DescribeApiGroups"
    request.Product = "apigateway"
    // If you use an STS AccessKey pair to call an RPC API, add the SecurityToken param
eter.
    // request.QueryParams["SecurityToken"]="<your-SecurityToken>"
    // Required. Specify the source of the call.
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. Required for Apsara Stack Enterprise Edition V3.15.0 and earlier.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource group ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
    // Optional. Required for modify and delete operations.
    // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    fmt.Print(response.GetHttpContentString())
```

The API information for the ROA example is as follows: Product (CR), API operation (GetNamespaceList), and Version (2016-06-07). The following code is an example:

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
 // If you use an STS AccessKey pair to call a ROA API, add the x-acs-security-token fi
eld to the header.
 // request.Headers["x-acs-security-token"] = "<your-SecurityToken>"
 // Required. Specify the source of the call.
 request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. Required for Apsara Stack Enterprise Edition V3.15.0 and earlier.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource group ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
 // Optional. Required for modify and delete operations.
 // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
 response, err := client.ProcessCommonRequest(request)
 if err != nil {
  panic(err)
 fmt.Print(response.GetHttpContentString())
```

**Set a proxy**

You may need to set a proxy when you call an instance. You can set the proxy in one of the following two ways. Set the proxy using environment variables. Use the HTTP_PROXY, HTTPS_PROXY, or NO_PROXY environment variables. The following code is an example:

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

Set the proxy on the client. The following code is an example:

```
// Proxy settings on the client have a higher priority than environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Set the HTTP proxy. client.GetHttpProxy() // Get the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Set the HTTPS proxy. client.GetHttpsProxy() // Get the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Set the proxy whitelist. client.GetNoProxy() // Get the proxy whitelist.
```

**SSL verification**

**Summary**

This setting controls the SSL certificate verification behavior for requests. Set to `true` to disable certificate verification. This is an insecure practice. We recommend that you configure a certificate. Set to `false` to enable SSL certificate verification. By default, the operating system's CA certificates are used.

**Default value**

The default value is `false` .

**Settings**

**Important**

When you access OpenAPI over HTTPS, the SDK enables SSL certificate validation by default. If your code environment does not have a certificate, a validation error occurs. To ensure secure communication in a production environment, keep this validation enabled. To ignore certificate validation in a test environment, use the following settings.

```
// Set HTTPSInsecure for the request (affects only the current request). request.SetHTTPSInsecure(true) // Set HTTPSInsecure for the re quest to true. isInsecure := request.GetHTTPSInsecure() // Get the HTTPSInsecure settin g for the request.
```

The client-level setting takes effect only if the request-level setting is not set.

```
// Set HTTPSInsecure for the client (affects all requests sent by the client). client.SetHTTPSInsecure(true) // Set HTTPSInsecure for the clien t to true. isInsecure := client.GetHTTPSInsecure() // Get the HTTPSInsecure setting f or the client.
```

ters

## Common parameters

**Common request parameters**

Common request parameters must be included in all Apsara Stack API requests. Table 1. Common request parameters

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Format | Strin g | No | The type of the returned value. Set the value to JSON. |
| Version | Strin g | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Valid values: 2018-01-16: Auditprivate 2019-07-23: yundunnextsoc 2018-12-03: Sas 2016-11-11: aegis 2021-10-11: yundun-css 2019-08-05: secspy 2018-01-16: Ddosprivate 2018-06-30: hsm-private 2017-12-07: Cloudfw 2019-01-03: Sddp 2020-07-01: semawaf 2018-12-03: soar |
| AccessKeyId | Strin g | Yes | The AccessKey ID that is provided by Apsara Stack. |
| AccessKeySe cret | Strin g | Yes | The AccessKey secret that is provided by Apsara Stack. |
| RegionId | Strin g | Yes | The region ID of the service. |

ters

| Product | Strin g | Yes | The name of the service to which the operation belongs. Valid values: Auditprivate: basic components of Apsara Stack Security yundunnextsoc: Security Operations Center (SOC) Sas: Threat Detection Service aegis: Server Guard yundun-css: Container Protection secspy: Network Detection and Response Ddosprivate: Anti-DDoS Service hsm-private: Data Encryption Service Cloudfw: Cloud Firewall Sddp: Sensitive Data Discovery and Protection (SDDP) semawaf: Web Application Firewall (WAF) soar: Security Orchestration and Automation Response (SOAR) |
|---|---|---|---|
| EndpointPre | Strin g | Yes | The prefix in the endpoint of the service to which the operation belongs. Valid values: auditprivate: the prefix in the endpoint of basic components of Apsara Stack Security yundunnextsoc-pop: the prefix in the endpoint of SOC tds: the prefix in the endpoint of Threat Detection Service aegis: the prefix in the endpoint of Server Guard yundun-css: the prefix in the endpoint of Container Protection secspy-share: the prefix in the endpoint of Network Detection and Response ddosprivate: the prefix in the endpoint of Anti-DDoS Service hsmprivate: the prefix in the endpoint of Data Encryption Service cloudfw: the prefix in the endpoint of Cloud Firewall sddp-api: the prefix in the endpoint of SDDP semawaf: the prefix in the endpoint of WAF soar: the prefix in the endpoint of SOAR |

**Common response parameters**

API responses use the HTTP response format: A 2xx status code indicates a successful call. A 4xx or 5xx status code indicates a failed call. Responses are returned in the JSON format. Every response returns a unique RequestID regardless of whether the call is successful.

## API documentation

### Make API requests

#### Request structure

Apsara Stack Security API is based on Remote Procedure Call (RPC). This topic describes the structure of the API requests. You can send an HTTP request to call an API operation. The URL of the request must be in the following format:

```
http://endpoint/?Action=xx&parameters
```

Where:

| endpoint | : the endpoint used to call a clo |
|---|---|

`endpoint` : the endpoint used to call a cloud service. The endpoint for the Server Guard service is `aegis.[ RegionId].example.com` . `Action` : the operation that you want to perform. For example, you can set this parameter to DescribeFeatures to query the deployed Apsara Stack Security features. `parameters` : the request parameters. Request parameters include common request parameters and custom request parameters. Request parameters must be separated with ampersands (&). Common request parameters include information such as the API version and authentication information. For more information about the custom request parameters, see the corresponding operation description.

**Example**

Call the DescribeFeatures operation to query the deployed Apsara Stack Security features.

```
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=keytest&Format=JSON&SecureTransport=true&SignatureMethod=HMAC- SHA1&SignatureNonce=15215528852396&SignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018- 03-02Txxxxxxx&Version=2018-01-16&Signature=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures &Format=JSON &Version=2018-01-16 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### Signature mechanism

Alibaba Cloud Security authenticates every access request. You must include a signature in each request that you send over the HTTP or HTTPS protocol.

**API signature**

To ensure the security of API calls, Alibaba Cloud authenticates each API request using a signature. If you manually send an API request, you must use your AccessKey secret to calculate a Hash-based Message Authentication Code (HMAC) for the signature. The calculation is based on the encoded and sorted request parameters, as defined in RFC 2104. This section uses the following request parameters as an example to demonstrate how to create an API signature:

| Parameter | Content |
|---|---|
| Endpoint | http://yundunprivate.[RegionId].example.com/? |
| API-specific parameters | Action=DescribeFeatures |
| Common parameters (excluding Signature) | &Timestamp=2016-02-23T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2018-01-16 &SignatureVersion=1.0 |
| AccessKey secret | <yourAccessKeySecret> |

1. Construct a canonicalized query string from the request parameters.

**Note**

Request parameters consist of common request parameters (excluding the Signature parameter) and API-specific parameters. i. Sort the request parameters alphabetically by parameter name. Sort the request parameters alphabetically by name. ii. Parameter encoding URL-encode the names and values of the sorted parameters using the UTF-8 character set. The following rules apply to the encoding: Do not encode uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), hyphens (-), underscores (_), periods (.), or tildes (~). Encode other characters in the %XY format, where XY is the hexadecimal value of the character's ASCII code. For example, the double quotation mark (") is encoded as %22. Encode extended UTF-8 characters in the %XY%ZA… format. Note that a space must be encoded as %20, not as a plus sign (+). iii. Connect each encoded parameter name and its value with an equal sign (=). iv. Join the resulting parameter-value pairs with ampersands (&) in the alphabetical order that is specified in the sorting step. This process creates the canonicalized query string.
2. Construct the string-to-sign from the canonicalized query string using the following format:

```
StringToSign=HTTPMethod + “&” + percentEncode(“/”) + ”&” + percentEncode(CanonicalizedQueryString)
```

3. Calculate the HMAC value of the string-to-sign (StringToSign) as defined in RFC 2104.

**Note**

The key for the signature calculation is your AccessKey secret with an ampersand (&) character (ASCII code 38) appended. The hash algorithm is Secure Hash Algorithm 1 (SHA1).
4. Base64-encode the HMAC value to obtain the signature value (Signature).

```
LEW8N4y7Uasop******
```

5. Add the resulting signature value to the request parameters as the Signature parameter.
This completes the request signing process.

#### Common request parameters

The following table describes the common request parameters that are used to indicate information such as the API version and authentication information.

| Name | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The API version in the format of YYYY- MM-DD. Set the value to 2016-11-11. |
| AccessKeyId | String | Yes | The key ID that Alibaba Cloud assigns to a user for service access. |
| Signature | String | Yes | The signature string. |
| SignatureMethod | String | Yes | The signature method. Set the value to HMAC-SHA1. |

| Timestamp | String | Yes | The timestamp of the request. Follow the ISO 8601 standard to specify the date and use the offset from Coordinated Universal Time (UTC) to specify the time zone. The format is YYYY-MM- DDThh:mm:ssZ . For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014, Beijing time. |
|---|---|---|---|
| SignatureVersion | String | Yes | The signature algorithm version. Set the value to 1.0. |
| SignatureNonce | String | Yes | The unique random number used to prevent network replay attacks. You must use different random numbers for different requests. |
| ResourceOwnerA ccount | String | No | The owner account of the resource to be accessed through this API request, that is, the logon username. |
| Format | String | No | The format of the response. Set the value to JSON or XML. Note Default value: XML. |

|   |   | YYYY-MM- |
|---|---|---|
|   | DDThh:mm:ssZ |   |

#### Response structure

Apsara Stack Security API responses can be returned in either the XML or JSON format. Every response returns a unique ID (indicated by **RequestId**) regardless of whether the call is successful.

**Sample responses (XML format)**

```xml
<? xml version="1.0" encoding="UTF-8"? > <! --The root node of the result--> <Operation name+Response>
    <! --Returned request ID-->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! --Returned data-->
</Operation name+Response>
```

**Sample responses (JSON format)**

```json
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216", /* Returned data */
```

### Asset management

#### DescribeCloudCenterInstances

You can call the DescribeCloudCenterInstances operation to query for assets that meet specific search criteria, such as an instance name or a region. This operation supports both paged queries and the NextToken method. The NextToken method is recommended.

**Permissions**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- aegis:DescribeCloudCenterInsta nces | Read | acs:yundun-aegis:*: {#accountId}:* |

**Throttling**

Per user: 10 queries per second (QPS). Per API: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | Chinese | The language of the request and response. Default value: zh. zh: Chinese. en: English. |
| RegionId | Strin g | Query | No | cn-hangzhou | The ID of the region where the instance resides. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Criteria | Strin g | Query | No | [{"name":"riskStatus","v alue":"YES"}, {"name":"internetIp","va lue":"1.2.XX.XX"}] | The search conditions for assets. This parameter is a JSON string and is case- sensitive. Note: You can search for assets by instance ID, instance name, VPC ID, region, public IP address, and other conditions. You can call the DescribeCriteria operation to query for supported search conditions. |
| MachineT ypes | Strin g | Query | No | ecs | The type of asset to query. Valid values: ecs: server. cloud product: cloud _ product. |
| LogicalEx p | Strin g | Query | No | OR | The logical relationship between multiple search conditions. Default value: OR. Valid values: OR: The search conditions are combined with a logical OR. AND: The search conditions are combined with a logical AND. |
| NoPage | Boole an | Query | No | true | Specifies whether to enable paged queries. Default value: true. Valid values: true: Enables paged queries. false: Disables paged queries. |
| PageSize | Integ er | Query | No | 100 | The number of assets to display on each page in a paged query. Default value: 20. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| CurrentPa ge | Integ er | Query | No | 1 | The page number to start displaying results from. Default value: 1. |
| Importanc e | Integ er | Query | No | 2 | The importance level of the asset. Valid values: 2: Important. 1: General. 0: Test. |
| ResourceS etIds | Strin g | Query | No | 123,456 | A list of resource set IDs. Separate multiple IDs with a comma. |
| ResourceS tatus | Strin g | Query | No | NORMAL | The status of the resource. Valid values: NORMAL: Normal. DELETED: Locked. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Instances | Array |   | The details of the assets. |
| -InternetIp | String | 1.2.XX.XX | The public IP address of the instance. |
| -Os | String | Linux | The operating system of the instance. |
| -InstanceId | String | i-m5*** | The instance ID. |
| - InstanceName | String | yztest-l*** | The instance name. |
| -RegionName | String | China (Hangzhou) | The name of the region where the asset resides. |
| -Ip | String | 1.2.XX.XX | The public IP address of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -ClientStatus | String | online | The online status of the client on the instance. Valid values: online: The agent is running. offline: The agent is stopped. pause: The agent's protection is paused. |
| -Region | String | cn-hangzhou- cm***-*** | The ID of the region where the instance resides. |
| -Uuid | String | c9107c04-942f- 40c1-981a-f1c1*** | The UUID of the instance. |
| -IntranetIp | String | 1.2.XX.XX | The private IP address of the instance. |
| -AssetType | String | 0 | The type of the asset. Valid values: 0: Elastic Compute Service. 1: Server Load Balancer. 2: NAT Gateway. 3: RDS database. 4: MongoDB database. 5: Redis database. 6: container image. 7: container. |
| -Status | String | Running | The running status of the instance. Valid values: Running: The instance is running. notRunning: The instance is shut down. |
| -Tag | String | InternetIp,test | The tag name of the asset instance. |
| -VpcInstanceId | String | vpc- uf60agqq65bs98zo o**** | The ID of the VPC where the instance resides. |
| -OsName | String | - | The kernel version of the instance. |
| -Flag | Integer | 0 | Indicates whether the instance is an Alibaba Cloud asset. Valid values: 0: Alibaba Cloud asset. 1: Third-party asset. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -HcStatus | String | YES | Indicates whether baseline risks are detected on the instance. Valid values: YES: Baseline risks are detected. NO: No baseline risks are detected. |
| -VulStatus | String | YES | Indicates whether the instance has vulnerabilities. Valid values: YES: The instance has vulnerabilities. NO: The instance has no vulnerabilities. |
| -AlarmStatus | String | NO | Indicates whether security alerts are triggered for the asset. Valid values: YES: Security alerts are triggered. NO: No security alerts are triggered. |
| -RiskStatus | String | NO | Indicates whether the asset has security risks. Valid values: Exists NO: Non-existent |
| - WeakPassword Status | String | NO | Indicates whether a weak password exists. Valid values: NO: No weak password exists. YES: A weak password exists. |
| - HealthCheckC ount | Integer | 1 | The number of baseline risks on the instance. |
| -VulCount | Integer | 2 | The number of vulnerabilities on the instance. |
| - SafeEventCou nt | Integer | 5 | The number of security alerts for the asset. |
| -RegionId | String | cn-hanghzou | The ID of the region where the asset resides. |
| -GroupId | String | 4120080 | The ID of the group to which the instance belongs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Importance | Integer | 2 | The importance level of the asset. Valid values: 2: Important. 1: General. 0: Test. |
| -ClientVersion | String | 00 31 _ | The client version. |
| -RiskCount | String | { "account": 0, "appNum": 0, "asapVulCount": 0, "baselineHigh": 0, "baselineLow": 0, "baselineMedium": 0, "baselineNum": 0, "cmsNum": 0, "containerAsap": 0, "containerLater": 0, "containerNntf": 0, "containerRemind": 0, "containerSerious": 0, "containerSuspicio us": 0, "cveNum": 0, "emgNum": 0, "health": 0, "imageBaselineHig h": 0, "imageBaselineLow ": 0, "imageBaselineMe dium": 0, "imageBaselineNu m": 0, "imageMaliciousFil | The statistics of risks on the asset. This parameter is a JSON string that contains the following fields: account: The number of accounts with unusual logons or successful brute-force attacks. appNum: The number of scanner vulnerabilities. asapVulCount: The total number of important vulnerabilities. baselineHigh: The number of important baseline risks. baselineLow: The number of low- severity baseline risks. baselineMedium: The number of medium-severity baseline risks. baselineNum: The total number of cloud product configuration risks. cmsNum: The number of Web-CMS vulnerabilities. containerAsap: The number of important container vulnerabilities. containerLater: The number of medium- severity container vulnerabilities. containerNntf: The number of low- severity container vulnerabilities. containerRemind: The number of container reminder alerts. containerSerious: The number of container urgent alerts. containerSuspicious: The number of container suspicious alerts. cveNum: The number of Linux vulnerabilities. emgNum: The number of emergency vulnerabilities. health: The number of unhandled baseline alerts. imageBaselineHigh: The number of important baseline risks for the image. imageBaselineLow: The number of low- severity baseline risks for the image. imageBaselineMedium: The number of medium-severity baseline risks for the |

|   |   | imageMaliciousFil |   |
|---|---|---|---|
| Parameter | Type | eERxeamminpdl"e: 0, "imageMaliciousFil | image. Description imageBaselineNum: The total number of |
|   |   | eSerious": 0, "imageMaliciousFil eSuspicious": 0, "imageVulAsap": 0, "imageVulLater": 0, "imageVulNntf": 0, "laterVulCount": 0, "newSuspicious": 0, "nntfVulCount": 0, "remindNum": 0, "scaNum": 0, "seriousNum": 0, "suspNum": 0, "suspicious": 0, "sysNum": 0, "trojan": 0, "uuid": "inet-37316411- 37fe-4b72-b245- 346a2721****", "vul": 0, "weakPWNum": 0 } | baseline risks for the image. imageMaliciousFileRemind: The number of reminder alerts for malicious files in the image. imageMaliciousFileSerious: The number of urgent alerts for malicious files in the image. imageMaliciousFileSuspicious: The number of suspicious alerts for malicious files in the image. imageVulAsap: The number of important vulnerabilities in the image. imageVulLater: The number of medium- severity vulnerabilities in the image. imageVulNntf: The number of low- severity vulnerabilities in the image. laterVulCount: The number of medium- severity vulnerabilities. newSuspicious: The number of alerts. nntfVulCount: The number of low- severity vulnerabilities. remindNum: The number of reminder alerts. scaNum: The number of Software Component Analysis (SCA) vulnerabilities. seriousNum: The number of urgent alerts. suspNum: The number of suspicious alerts. |
|   |   |   | suspicious: The total number of alerts. sysNum: The number of Windows vulnerabilities. trojan: The number of trojans. uuid: The UUID of the asset. vul: The number of vulnerabilities. weakPWNum: The number of weak passwords. |
| -ClusterId | String | c690a0789419f428 4a4e0a29e12fe*** * | The cluster ID. |
| -ClusterName | String | cluster1 | The cluster name. |
| -CreatedTime | Long | 1607365213000 | The timestamp when the cluster was created. Unit: milliseconds. |
| -PodCount | Integer | 1 | The number of pods. |

| libaba Cloud Sec | urity-Server Gu |   | Server Guard Advanced Edition D |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - ExposedStatus | Integer | 0 | The exposure status of the asset. Valid values: 0: Not exposed. 1: Exposed. |
| - AutoSnapshots Level | Integer | 0 | The security status of the snapshot restoration. Valid values: 0: Unknown. 1: Secure. 2: Medium-risk. 3: High-risk. |
| - ExposedCount | Integer | 1 | The number of external exposures. |
| - WeakPassword Count | Integer | 2 | The number of weak passwords. |
| - FirstLoginTime | Long | 2023-12-11 12:41:51 | The time of the first logon. |
| - LastLoginTime | Long | 2024-01-04 22:58:22 | The time of the last logon. |
| - AssetsSyncTim e | Long | 2024-01-04 22:58:22 | The asset synchronization time. |
| -ProviderName | String | test | The name of the provider. |
| - ProviderRegio nName | String | region 1 _ | The name of the region under the provider. |
| - ProviderAzNa me | String | az1 | The name of the data center. |
| -ProviderId | Long | 34 | The provider ID. |
| - ProviderRegio nId | Long | 12 | The ID of the region under the provider. |
| -ProviderAzId | Long | 56 | The ID of the data center under the provider. |
| -OrgId | String | 9 | The organization ID. |

| erver Guard Adv veloper Guide·AP n | anced Edition D I documentati |   | Alibaba Cloud Security-Server G ard Advanced Editio |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -OrgFullId | String | \|1\|8\|9\| | The full organization ID. The separator is \|. |
| - ResourceSetId | String | 11 | The resource set ID. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. This is a unique identifier generated by Alibaba Cloud for the request. You can use this ID to troubleshoot issues. |
| Success | Boolean | true | The status of the API call. Valid values: true: The call was successful. false: The call failed. |
| PageInfo | Struct |   | The information is displayed on the page. |
| -Count | Integer | 10 | The number of assets displayed on the current page. |
| -PageSize | Integer | 20 | The number of assets to display on each page in a paged query. Default value: 20. |
| -TotalCount | Integer | 50 | The total number of assets found. |
| -CurrentPage | Integer | 1 | The page number of the current page in a paged query. |

Sample request

```json
https://[Endpoint]/?Action=DescribeCloudCenterInstances&RegionId=cnhangzhou&Lang=zh&Criteria=[{"name":"riskStatus","value":"YES"}, {"name":"internetIp","value":"1.2.XX.XX"}]&MachineTypes=ecs&LogicalExp=OR&NoPage=true&Pag ize=100&CurrentPage=1&Importance=2&Flags=1&ResourceSetIds=123,456&ResourceStatus=NORMAL
```

Sample response `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true,
    "PageInfo":{
"TtlC t"50
```

```json
        "TotalCount":50,
        "PageSize":20,
        "CurrentPage":1,
        "Count":10
```

`},`

```json
    "Instances":[
            "ProviderId":34,
            "CreatedTime":1607365213000,
            "Os":"Linux",
            "VulStatus":"YES",
            "ExposedCount":1,
            "IntranetIp":"1.2.XX.XX",
            "Importance":2,
            "AutoSnapshotsLevel":0,
            "InternetIp":"1.2.XX.XX",
            "RegionName":"China (Hangzhou)",
            "AssetsSyncTime":"2024-01-04 22:58:22",
            "Status":"Running",
            "ExposedStatus":0,
            "SafeEventCount":5,
            "InstanceId":"i-m5***",
            "HealthCheckCount":1,
            "Flag":0,
            "ProviderAzId":56,
            "VulCount":2,
            "InstanceName":"yztest-l***",
            "Region":"cn-hangzhou-cm***-***",
            "ProviderAzName":"az1",
            "Ip":"1.2.XX.XX",
            "ClientVersion":"00_31",
            "ProviderRegionName":"region_1",
            "RiskCount":"{<br/>                    \"account\": 0,<br/>
\"appNum\": 0,<br/> \"asapVulCount\": 0,<br/> \"bas elineHigh\": 0,<br/> \"baselineLow\": 0,<br/> \"bas elineMedium\": 0,<br/> \"baselineNum\": 0,<br/> \"c msNum\": 0,<br/> \"containerAsap\": 0,<br/> \"conta inerLater\": 0,<br/> \"containerNntf\": 0,<br/> \"c ontainerRemind\": 0,<br/> \"containerSerious\": 0,<br/> \"containerSuspicious\": 0,<br/> \"cveNum\": 0,<br/> \"emgNum\": 0,<br/> \"health\": 0,<br/> \"imageBase lineHigh\": 0,<br/> \"imageBaselineLow\": 0,<br/> \ "imageBaselineMedium\": 0,<br/> \"imageBaselineNum\": 0,<br/> \"imageMaliciousFileRemind\": 0,<br/> \"imageMaliciousFileSerious\": 0,<br/> \"imageMaliciousFileSuspicious\": 0,<br/> \ "imageVulAsap\": 0,<br/> \"imageVulLater\": 0,<br/> \"imageVulNntf\": 0,<br/> \"laterVulCount\": 0,<br/> \"newSuspicious\": 0,<br/> \"nntfVulCount\": 0,<br/> \"remindNum\": 0,<br/> \"scaNum\": 0,<br/> \"seriou sNum\": 0,<br/> \"suspNum\": 0,<br/> \"suspicious\" : 0,<br/> \"sysNum\": 0,<br/> \"trojan\": 0,<br/> \"uuid\": \"inet-37316411-37fe-4b72-b245-346a2721****\",<br/> \"vul\" : 0,<br/> \"weakPWNum\": 0<br/> }",
            "PodCount":1,
"ProviderRegionId":12
```

```json
            ProviderRegionId:12,
            "ClusterName":"cluster1",
            "ResourceSetId":"11",
            "FirstLoginTime":"2023-12-11 12:41:51",
            "ClientStatus":"online",
            "ClusterId":"c690a0789419f4284a4e0a29e12fe****",
            "WeakPasswordCount":2,
            "OsName":"-",
            "RiskStatus":"NO",
            "WeakPasswordStatus":"NO",
            "GroupId":"4120080",
            "LastLoginTime":"2024-01-04 22:58:22",
            "ProviderName":"test",
            "OrgId":"9",
            "AssetType":"0",
            "OrgFullId":"|1|8|9|",
            "Uuid":"c9107c04-942f-40c1-981a-f1c1***",
            "AlarmStatus":"NO",
            "VpcInstanceId":"vpc-uf60agqq65bs98zoo****",
            "Tag":"InternetIp,test",
            "RegionId":"cn-hanghzou",
            "HcStatus":"YES"
```

`]`

```
}<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>< br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br /><br/><br/><br/><br/><br/><br/>
```

`XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeCloudCenterInstancesResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Success>true</Success>
    <PageInfo>
        <Count>10</Count>
        <PageSize>20</PageSize>
        <TotalCount>50</TotalCount>
        <CurrentPage>1</CurrentPage>
    </PageInfo>
    <Instances>
        <InternetIp>1.2.XX.XX</InternetIp>
        <Os>Linux</Os>
        <InstanceId>i-m5***</InstanceId>
        <InstanceName>yztest-l***</InstanceName>
        <RegionName>China (Hangzhou)</RegionName>
        <Ip>1.2.XX.XX</Ip>
        <ClientStatus>online</ClientStatus>
        <Region>cn-hangzhou-cm***-***</Region>
        <Uuid>c9107c04-942f-40c1-981a-f1c1***</Uuid>
        <IntranetIp>1.2.XX.XX</IntranetIp>
        <AssetType>0</AssetType>
```

```json
        <Status>Running</Status>
        <Tag>InternetIp,test</Tag>
        <VpcInstanceId>vpc-uf60agqq65bs98zoo****</VpcInstanceId>
        <OsName>-</OsName>
        <Flag>0</Flag>
        <HcStatus>YES</HcStatus>
        <VulStatus>YES</VulStatus>
        <AlarmStatus>NO</AlarmStatus>
        <RiskStatus>NO</RiskStatus>
        <WeakPasswordStatus>NO</WeakPasswordStatus>
        <HealthCheckCount>1</HealthCheckCount>
        <VulCount>2</VulCount>
        <SafeEventCount>5</SafeEventCount>
        <RegionId>cn-hanghzou</RegionId>
        <GroupId>4120080</GroupId>
        <Importance>2</Importance>
        <ClientVersion>00_31</ClientVersion>
        <RiskCount>{ "account": 0, "appNum": 0, "asapVulCount": 0, "baselineHigh": 0,
"baselineLow": 0, "baselineMedium": 0, "baselineNum": 0, "cmsNum": 0, "containerAsap": 0, "containerLater": 0, "containerNntf": 0, "containerRemind": 0, "containerSerious": 0 , "containerSuspicious": 0, "cveNum": 0, "emgNum": 0, "health": 0, "imageBaselineHigh": 0, "imageBaselineLow": 0, "imageBaselineMedium": 0, "imageBaselineNum": 0, "imageMaliciousFileRemind": 0, "imageMaliciousFileSerious": 0, "imageMaliciousFileSuspicious": 0, "imageVulAsap": 0, "imageVulLater": 0, "imageVulNntf": 0, "laterVulCount": 0, "newSuspicious": 0, "nntfVulCount": 0, "remindNu m": 0, "scaNum": 0, "seriousNum": 0, "suspNum": 0, "suspicious": 0, "sysNum": 0, "trojan": 0, "uuid": "inet-37316411-37fe-4b72-b245-346a2721****", "vul": 0, "weakPWNum" : 0 }</RiskCount>
        <ClusterId>c690a0789419f4284a4e0a29e12fe****</ClusterId>
        <ClusterName>cluster1</ClusterName>
        <CreatedTime>1607365213000</CreatedTime>
        <PodCount>1</PodCount>
        <ExposedStatus>0</ExposedStatus>
        <AutoSnapshotsLevel>0</AutoSnapshotsLevel>
        <ExposedCount>1</ExposedCount>
        <WeakPasswordCount>2</WeakPasswordCount>
        <FirstLoginTime>2023-12-11 12:41:51</FirstLoginTime>
        <LastLoginTime>2024-01-04 22:58:22</LastLoginTime>
        <AssetsSyncTime>2024-01-04 22:58:22</AssetsSyncTime>
        <ProviderName>test</ProviderName>
        <ProviderRegionName>region_1</ProviderRegionName>
        <ProviderAzName>az1</ProviderAzName>
        <ProviderId>34</ProviderId>
        <ProviderRegionId>12</ProviderRegionId>
        <ProviderAzId>56</ProviderAzId>
        <OrgId>9</OrgId>
        <OrgFullId>|1|8|9|</OrgFullId>
        <ResourceSetId>11</ResourceSetId>
    </Instances>
</DescribeCloudCenterInstancesResponse>
```

#### DescribePropertyScaDetail

Queries the details of middleware on the Asset Fingerprints page.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- aegis:DescribePropertyScaDeta il | Read | acs:yundun-aegis:*: {#accountId}:* |

**Traffic shaping**

The request rate for a single user is limited to 10 queries per second (QPS). The request rate for this API is limited to 100 QPS.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language of the request and response. Default value: zh. zh: Chinese. en: English. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SearchIte m | Strin g | Query | No | type | The type of the search condition. Valid values: name : the name of the middleware, database, or web service type : the type of the middleware, database, or web service. Note: The SearchItem and SearchInfo parameters are used together. Set both parameters to view all data for asset fingerprints of a specific name or type. Setting only one parameter has no effect. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SearchInf o | Strin g | Query | No | system service _ | The content to query. The value you enter for this parameter depends on the value of the SearchItem parameter: SearchItem to name , enter the name of the asset fingerprint. SearchItem to type , select the type of the asset fingerprint. Valid values: system service : _ System service software librar _ y docker compone _ nt : The component for the container. Database : The name of the database. web container : _ The web container. jar : Java Archive (JAR) package web framework _ : Web framework Note The SearchItem and SearchInfo parameters are used together. Set both parameters to view all data for asset fingerprints of a specific name or type. Setting only one parameter has no effect. |
| ScaName | Strin g | Query | No | openssl | The name of the asset fingerprint to query. |

| A a | libaba Cloud rd Advanced | Security- Edition | Server Gu |   | Serve evelo | r Guard Advanced Edition D per Guide·API documentat o | i n |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| BizType | Strin g | Query | No | system service _ | The type of the middleware, database, or web service to query. Valid values: system service : _ System service software library _ docker componen _ t : Specifies the container component. database web container : A _ container for running web applications. jar : A Java Archive (JAR) package web framework : _ Specifies the web framework. |
| SearchIte mSub | Strin g | Query | No | version | The type of the subquery condition. Valid values: port : The port number. pid : The process ID. version user |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SearchInf oSub | Strin g | Query | No | 1.0.2k | The content of the subquery condition. The value you enter for this parameter depends on the value of the SearchItemSub parameter: SearchItemSub to port , enter the port number. SearchItemSub to pid , enter the process ID. SearchItemSub to version , enter the version of the middleware, database, or web service. SearchItemSub to user , enter the username. Note : The subquery condition helps you search for specific data of middleware, databases, or web services. |
| Remark | Strin g | Query | No | 192.168 | The search condition, which can be a server name or an IP address. Note : Fuzzy search is supported. |
| Port | Strin g | Query | No | 68 | The listening port of the process. |
| Pid | Strin g | Query | No | 756 | The process ID. |
| ScaVersio n | Strin g | Query | No | 1.0.2k | The version of the middleware, database, or web service. |

| libaba Cloud rd Advanced | Security- Edition | Server Gu |   | Serve evelo | r Guard Advanced Edition D per Guide·API documentat o |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | Description |
| User | Strin g | Query | No | root | The user that runs the service. |
| Name | Long | Query | No | 1 | The name of the middleware, database, or web service. Note : This parameter is deprecated. You do not need to specify it. |
| Uuid | Strin g | Query | No | uuid-02ebabe7-1c19- ab**** | The UUID of the server where the middleware, database, or web service is located. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number to return. Default value: 1. |
| PageSize | Integ er | Query | No | 10 | The number of entries to return on each page. Default value: 10. Note: Do not leave this parameter empty. |
| SelectTyp e | Strin g | Query | No | equals | The query type. Default value: like. Valid values: equals : term query like : fuzzy query |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Propertys | Array |   | The details of the asset fingerprints. |
| InstanceName | String | Test01 | The name of the server where the middleware, database, or web service is located. |
| -Ip | String | 47.42.XX.XX | The public IP address of the server where the middleware, database, or web service is located. |

| erver Guard Adv veloper Guide·AP | anced Edition D I documentati |   | Alibaba Cloud Security-Server G ard Advanced Editio |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Create | String | 1597987834000 | The timestamp of the last scan. This is the time when Server Guard last collected information about the middleware, database, or web service. Unit: milliseconds. |
| CreateTimesta mp | Long | 1597987834000 | The timestamp of the last scan. This is the time when Server Guard last collected information about the middleware, database, or web service. Unit: milliseconds. |
| -UUID | String | uuid-02ebabe7- 1c19-a**** | The UUID of the server where the middleware, database, or web service is located. |
| InstanceId | String | i-2zeclqj7ti**** | The instance ID of the server where the middleware, database, or web service is located. |
| IntranetIp | String | 192.210.XX.XX | The private IP address of the server where the middleware, database, or web service is located. |
| InternetIp | String | 47.42.XX.XX | The public IP address of the server where the middleware, database, or web service is located. |
| Name | String | openssl | The name of the middleware, database, or web service. |
| Type | String | library | The type of the middleware, database, or web service. |
| Version | String | 1.0.2k | The version of the middleware, database, or web service. |
| Pid | String | 756 | The process ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BizType | String | software library _ | The type of the middleware, database, or web service. Valid values: system service : System service _ software library : Software library _ docker component _ database : database web container : Specifies the web _ container jar web framework : Specifies the web _ framework. |
| BizTypeDispal y | String | Software Library | The display name of the middleware, database, or web service type. Valid values: System Service Software Library Container Component Database Web Container JAR Package Web Framework |
| Port | String | 68 | The port of the middleware, database, or web service. |
| ContainerNam e | String | 5-rce web 1 _ _ | The container name. |
| Path | String | /usr/lib64/libssl.so. 1.0.2k | The path of the middleware, database, or web service. |
| -Ppid | String | 1 | The parent process ID. |
| ProcessUser | String | root | The username that runs the process. |
| ListenIp | String | 0.0.XX.XX | The listening IP address of the process. |
| ListenStatus | String | NONE | The listening status of the process. Valid values: NONE : not listening LISTEN : listening |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenProtocol | String | UDP | The listening protocol of the process. Valid values: UDP TCP |
| ProcessStarted | Long | 1596539788 | The timestamp when the process started. Unit: milliseconds. |
| Cmdline | String | /sbin/dhclient -H iz2zeflhhbtk8gtxzt0 87az -1 -q -lf /var/lib/dhclient/dh client--eth0.lease - pf /var/run/dhclient- eth0.pid eth0 | The command line of the process. |
| -ConfigPath | String | /etc/my.cnf | The path of the configuration file. |
| WebPath | String | /usr/share/nginx/ht ml | The web directory. |
| Proof | String | /usr/lib64/libssl.so. 1.0.2k | The version validation information for the middleware, database, or web service. |
| ImageName | String | registry-vpc.cn- beijing.aliyuncs.co m/acs/aliyun- ingress- controller**** | The image name. |
| OrgId | String | 12 | The organization ID. |
| ResourceSetId | String | 12 | The resource set ID. |
| OrgName | String | test | The organization name. |
| ResourceSetN ame | String | test | The resource set name. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. This is a unique identifier that Alibaba Cloud generates for the request. You can use this ID to troubleshoot issues. |
| PageInfo | Struct |   | The paging information. |

| libaba Cloud Sec rd Advanced Edit | urity-Server Gu ion |   | eveloper Guide·API documentat o |
|---|---|---|---|
| Parameter | Type | Example | Description |
| Count | Integer | 2 | The number of entries returned on the current page. |
| -PageSize | Integer | 20 | The number of entries returned on each page. Default value: 10. |
| TotalCount | Integer | 2 | The total number of asset fingerprints found. |
| CurrentPage | Integer | 1 | The number of the current page. |

Request example

```
https://[Endpoint]/?Action=DescribePropertyScaDetail&RegionId=cnhangzhou&Lang=zh&SearchItem=type&SearchInfo=system_service&ScaName=openssl&BizType=system ervice&SearchItemSub=version&SearchInfoSub=1.0.2k&Remark=192.168&Port=68&Pid=756&ScaVersi =1.0.2k&User=root&Name=1&Uuid=uuid-02ebabe7-1c19ab****&CurrentPage=1&PageSize=10&SelectType=equals
```

Response example `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Propertys":[
            "BizTypeDisplay":"Software Library",
            "ProcessUser":"root",
            "ResourceSetName":"test",
            "Ip":"47.42.XX.XX",
            "Port":"68",
            "OrgName":"test",
            "IntranetIp":"192.210.XX.XX",
            "Name":"openssl",
            "ProcessStarted":1596539788,
            "InternetIp":"47.42.XX.XX",
            "Version":"1.0.2k",
            "ContainerName":"5-rce_web_1",
            "ListenProtocol":"UDP",
            "Create":"1597987834000",
            "WebPath":"/usr/share/nginx/html",
            "ResourceSetId":"12",
            "CreateTimestamp":1597987834000,
            "Ppid":"1",
            "Path":"/usr/lib64/libssl.so.1.0.2k",
            "InstanceId":"i-2zeclqj7ti****",
            "Pid":"756",
            "BizType":"software_library",
            "InstanceName":"Test01",
            "ImageName":"registry-vpc.cn-beijing.aliyuncs.com/acs/aliyun-ingress-
controller****",
            "OrgId":"12",
            "Type":"library",
            "Uuid":"uuid-02ebabe7-1c19-a****",
            "ListenStatus":"NONE",
            "ConfigPath":"/etc/my.cnf",
            "Proof":"/usr/lib64/libssl.so.1.0.2k",
            "ListenIp":"0.0.XX.XX",
            "Cmdline":"/sbin/dhclient -H iz2zeflhhbtk8gtxzt087az -1 -q -lf /var/lib/dhcl
ient/dhclient--eth0.lease -pf /var/run/dhclient-eth0.pid eth0"
```

`],`

```json
    "PageInfo":{
        "TotalCount":2,
        "PageSize":20,
        "CurrentPage":1,
        "Count":2
```

`XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribePropertyScaDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <Propertys>
        <InstanceName>Test01</InstanceName>
        <Ip>47.42.XX.XX</Ip>
        <Create>1597987834000</Create>
        <CreateTimestamp>1597987834000</CreateTimestamp>
        <Uuid>uuid-02ebabe7-1c19-a****</Uuid>
        <InstanceId>i-2zeclqj7ti****</InstanceId>
        <IntranetIp>192.210.XX.XX</IntranetIp>
        <InternetIp>47.42.XX.XX</InternetIp>
        <Name>openssl</Name>
        <Type>library</Type>
        <Version>1.0.2k</Version>
        <Pid>756</Pid>
        <BizType>software_library</BizType>
        <BizTypeDisplay>Software Library</BizTypeDisplay>
        <Port>68</Port>
        <ContainerName>5-rce_web_1</ContainerName>
        <Path>/usr/lib64/libssl.so.1.0.2k</Path>
        <Ppid>1</Ppid>
        <ProcessUser>root</ProcessUser>
        <ListenIp>0.0.XX.XX</ListenIp>
        <ListenStatus>NONE</ListenStatus>
        <ListenProtocol>UDP</ListenProtocol>
        <ProcessStarted>1596539788</ProcessStarted>
        <Cmdline>/sbin/dhclient -H iz2zeflhhbtk8gtxzt087az -1 -q -lf
/var/lib/dhclient/dhclient--eth0.lease -pf /var/run/dhclient-eth0.pid eth0</Cmdline>
        <ConfigPath>/etc/my.cnf</ConfigPath>
        <WebPath>/usr/share/nginx/html</WebPath>
        <Proof>/usr/lib64/libssl.so.1.0.2k</Proof>
        <ImageName>registry-vpc.cn-beijing.aliyuncs.com/acs/aliyun-ingress-
controller****</ImageName>
        <OrgId>12</OrgId>
        <ResourceSetId>12</ResourceSetId>
        <OrgName>test</OrgName>
        <ResourceSetName>test</ResourceSetName>
    </Propertys>
    <PageInfo>
        <Count>2</Count>
        <PageSize>20</PageSize>
        <TotalCount>2</TotalCount>
        <CurrentPage>1</CurrentPage>
    </PageInfo>
</DescribePropertyScaDetailResponse>
```

#### DescribeAssetDetailByUuid

You can call the DescribeAssetDetailByUuid operation to query the details and extended information of a server asset by its UUID.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- aegis:DescribeAssetDetailByUui d | Read | acs:yundun-aegis:*: {#accountId}:* |

**Traffic shaping**

The rate limit for an individual user is 10 queries per second (QPS). The rate limit for this operation is 100 QPS.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SourceIp | Strin g | Quer y | No | 219.133.XX.XX | The source IP address. |
| Uuid | Strin g | Quer y | Yes | 9e6cad93-a379-46fd- a701-9bbf02f4**** | The UUID of the asset to query. Note: Call the DescribeCloudCenterInsta nces operation to obtain this parameter. |
| Lang | Strin g | Quer y | No | zh | The language of the content in the request and response. Default value: zh. Valid values: zh: Chinese, en: English. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The call request ID is a unique identifier generated by Alibaba Cloud and is used to troubleshoot and locate issues. |

| AssetDetail | Struct |   | The details of the asset. |
|---|---|---|---|
| -IpList | Normal | ["192.168.XX.XX"," 192.168.XX.XX"] | A list of IP addresses. |
| -MacList | Normal | ["00:16:3*:1*:9*:cf "] | MAC address. |
| -DiskInfoList | Normal |   | The disk information. The following list describes the disk-related parameters: * diskName: The name of the disk. * totalSize: The total disk capacity in GB. * useSize: The used disk capacity in GB. |
| -InternetIp | String | 192.168.XX.XX | The public IP address of the server. |
| -IntranetIp | String | 192.168.XX.XX | The private IP address of the server. |
| - InstanceName | String | i- fasdfasdfadfafa**** | The name of the server. |
| -InstanceId | String | i- uf6h7p2fgk6rkk0g* *** | The ID of the server. |
| -Ip | String | 192.168.XX.XX | The IP address assigned by ECS. |
| -Uuid | String | 9e6cad93-a379- 46fd-a701- 9bbf02f4**** | The UUID of the server. |
| -AssetType | String | 6 | The asset type. Valid values: * 0: ECS. * 1: Server Load Balancer (SLB). * 2: NAT Gateway. * 3: ApsaraDB RDS database. * 4: MongoDB database. * 5: Redis database. * 6: Container image. * 7: Container. |
| -Os | String | linux | The operating system type of the server. |
| -ClientStatus | String | online | The status of the Server Guard agent. Valid values: * pause: Protection is paused. * online: The server is protected. * offline: The server is not protected. |

| -Region | String | cn-hangzhou-dg- a01 | The region where the server resides. |
|---|---|---|---|
| -RegionId | String | cn-hanghzou | The region ID of the asset. |
| -RegionName | String | China (Hohhot) | The name of the region where the server resides. |
| -Tag | String | InternetIp | The tag of the server. |
| -GroupTrace | String | default | The group to which the server belongs. Servers that are not assigned to a group belong to the default group. |
| -Cpu | Integer | 2 | The number of CPU cores. |
| -CpuInfo | String | Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz | The details of the CPU. |
| -Kernel | String | 4.18.0- 80.11.2.el8 0.x86 _ _ 64 | The kernel version of the operating system. |
| -OsDetail | String | Linux 64bit | The architecture of the server's operating system. |
| -Mem | Integer | 32 | The memory size in GB. |
| -SysInfo | String | CentOS Linux 8.0.1905 | The operating system information of the server. |
| -HostName | String | qewrqwerqs**** | The hostname. |
| -OsName | String | - | The name of the server's operating system. |
| -VpcInstanceId | String | vpc- bp1fs3bwonlfq503 w**** | The ID of the VPC that the server belongs to. |
| -CreateTime | Long | 1603863599000 | The timestamp when Server Guard recorded the current asset information. Unit: milliseconds. |

| -Flag | Integer | 0 | Indicates whether the asset is an Alibaba Cloud asset. Valid values: * 0: Alibaba Cloud asset. * 1: Third-party asset. |
|---|---|---|---|
| -OrgId | String | 12 | The organization ID. |
| - ResourceSetId | String | 12 | The resource set ID. |
| - FirstLoginTime | Long | 1603863599000 | The time of the first logon. |

Request example

```
https://[Endpoint]/?Action=DescribeAssetDetailByUuid&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&Uuid=9e6cad93-a379-46fd-a701-9bbf02f4****&Lang=zh
```

Sample response `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "AssetDetail":{
        "GroupTrace":"default",
        "Os":"linux",
        "Ip":"192.168.XX.XX",
        "Cpu":2,
        "IntranetIp":"192.168.XX.XX",
        "OsDetail":"Linux 64bit",
        "InternetIp":"192.168.XX.XX",
        "RegionName":"China (Hohhot)",
        "InstanceStatus":"",
        "ResourceSetId":"12",
        "Kernel":"4.18.0-80.11.2.el8_0.x86_64",
        "HostName":"qewrqwerqs****",
        "FirstLoginTime":"",
        "ClientStatus":"online",
        "InstanceId":"i-uf6h7p2fgk6rkk0g****",
        "CpuInfo":"Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz",
        "IpList":[
            "192.168.XX.XX",
            "192.168.XX.XX"
```

`],`

```json
        "OsName":"-",
        "CreateTime":1603863599000,
        "SysInfo":"CentOS Linux 8.0.1905",
        "Flag":0,
        "InstanceName":"i-fasdfasdfadfafa****",
        "MacList":[
            "00:16:3*:1*:9*:cf"
```

`],`

```json
        "OrgId":"12",
        "AssetType":"6",
        "Uuid":"9e6cad93-a379-46fd-a701-9bbf02f4****",
        "Mem":32,
        "Region":"cn-hangzhou-dg-a01",
        "VpcInstanceId":"vpc-bp1fs3bwonlfq503w****",
        "RegionId":"cn-hanghzou",
        "Tag":"InternetIp"
```

`XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <DescribeAssetDetailByUuidResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <AssetDetail>
        <InternetIp>192.168.XX.XX</InternetIp>
        <IntranetIp>192.168.XX.XX</IntranetIp>
        <InstanceName>i-fasdfasdfadfafa****</InstanceName>
        <InstanceId>i-uf6h7p2fgk6rkk0g****</InstanceId>
        <Ip>192.168.XX.XX</Ip>
        <Uuid>9e6cad93-a379-46fd-a701-9bbf02f4****</Uuid>
        <AssetType>6</AssetType>
        <Os>linux</Os>
        <ClientStatus>online</ClientStatus>
        <Region>cn-hangzhou-dg-a01</Region>
        <RegionId>cn-hanghzou</RegionId>
        <RegionName>China (Hohhot)</RegionName>
        <Tag>InternetIp</Tag>
        <GroupTrace>default</GroupTrace>
        <Cpu>2</Cpu>
        <CpuInfo>Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz</CpuInfo>
        <Kernel>4.18.0-80.11.2.el8_0.x86_64</Kernel>
        <OsDetail>Linux 64bit</OsDetail>
        <Mem>32</Mem>
        <SysInfo>CentOS Linux 8.0.1905</SysInfo>
        <HostName>qewrqwerqs****</HostName>
        <OsName>-</OsName>
        <IpList>
            <Ip>["192.168.XX.XX","192.168.XX.XX"]</Ip>
        </IpList>
        <MacList>
            <Mac>["00:16:3*:1*:9*:cf"]</Mac>
        </MacList>
        <DiskInfoList>
            <DiskInfo></DiskInfo>
        </DiskInfoList>
        <VpcInstanceId>vpc-bp1fs3bwonlfq503w****</VpcInstanceId>
        <InstanceStatus></InstanceStatus>
        <CreateTime>1603863599000</CreateTime>
        <Flag>0</Flag>
        <OrgId>12</OrgId>
        <ResourceSetId>12</ResourceSetId>
        <FirstLoginTime></FirstLoginTime>
    </AssetDetail>
</DescribeAssetDetailByUuidResponse>
```

#### DescribeGroupSummary

You can call this operation to obtain a list of asset groups.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeGroupSummary. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The number of asset groups. |
| Groups | List | The information about asset groups. For more information, see the following parameter descriptions. |
| GroupId | Long | The asset group ID. |
| GroupIndex | Integer | The sequence number of the asset group. |
| GroupLevel | Integer | The level of the asset group. |
| GroupName | String | The name of the asset group. |
| GroupFather | Integer | The ID of the parent asset group. |
| GroupFlag | Integer | The type of the asset group. Valid values: 1: indicates a non-leaf node group that contains child asset groups. 0: indicates a leaf node group. |
| MachineNum | Integer | The number of ECS instances contained in the group. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeGroupSummary &<Common request parameters>
```

Sample responses (JSON format)

```json
 "Groups":[
   "GroupFlag":1,
   "GroupName":"Test group 21",
   "GroupIndex":1,
   "MachineNum":0,
   "GroupId":346
```

`},`

```json
   "GroupFlag":1,
   "GroupName":"Test group 1",
   "GroupIndex":2,
   "MachineNum":0,
   "GroupId":343
```

`},`

```json
   "GroupFlag":1,
   "GroupName":"Test group 2",
   "GroupIndex":3,
   "MachineNum":0,
   "GroupId":345
```

`},`

```json
   "GroupFlag":0,
   "GroupName":"Not grouped",
   "GroupIndex":100,
   "MachineNum":1,
   "GroupId":336
```

`],`

```json
 "Count":4,
 "RequestId":"B9FB5483-3CA6-4520-9F89-068ED6AAC6EE"
```

#### DescribeGroupStruct

You can call this operation to query the asset group structure.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeGroupStruct. |
| Mark | String | No | The IP address or instance name of the server. |

| TagIdList | String | No | The server tag ID. |
|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| GroupFather | Integer | The ID of the parent asset group. |
| GroupId | Long | The ID of the asset group. |
| Groups | List | The asset groups. For more information, see the following descriptions. |
| GroupId | Long | The ID of the asset group. |
| GroupIndex | Integer | The sequence number of the asset group. |
| GroupLevel | Integer | The level of the asset group. |
| GroupName | String | The name of the asset group. |
| GroupFather | Integer | The ID of the parent asset group. |
| GroupFlag | Integer | The type of the asset group. Valid values: 1: indicates a non-leaf node group that contains child asset groups. 0: indicates a leaf node group. |
| ChildGroups | List | The child asset groups. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeGroupStruct &remark=x.x.x.x &tagIdList=123 &<Common request parameters>
```

Sample response (JSON format)

```json
    "Groups":[
            "groupIndex":2,
            "groupFather":0,
            "groupId":343,
            "groupName":"****",
            "groupLevel":1,
            "groupFlag":1,
            "childGroups":[]
```

`},`

```json
            "groupIndex":3,
            "groupFather":0,
            "groupId":345,
            "groupName":"****",
            "groupLevel":1,
            "groupFlag":1,
            "childGroups":[
                    "groupIndex":1,
                    "groupFather":345,
                    "groupId":346,
                    "groupName":"****",
                    "groupLevel":2,
                    "groupFlag":1,
                    "childGroups":[]
```

`]` `},`

```json
            "groupIndex":100,
            "groupFather":0,
            "groupId":336,
            "groupName":"****",
            "groupFlag":0,
            "childGroups":[]
```

`],`

```json
    "RequestId":"C4490A16-DDE4-4351-A366-57F9FCDC188F",
    "GroupFather":0,
    "GroupId":0
```

#### DescribeAllEntity

You can call this operation to query information about all servers.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeAllEntity. |
| GroupId | Long | No | The ID of the asset group. |
| Os | String | No | The operating system of the server. Valid values: win: indicates the Windows operating system. linux: indicates the Linux operating system. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Count | Integer | The number of returned records. |
| EntityList | Array | The servers. For more information, see the following descriptions. |
| GroupId | Integer | The ID of the asset group. |
| Uuid | String | The universally unique identifier (UUID) of the server. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeAllEntity &GroupId=123 &Os=win &<Common request parameters>
```

Sample response (JSON format)

```json
    "Count":2,
    "RequestId":"09D7C349-5306-4335-849A-10916F89E769",
    "EntityList":[
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "Ip":"x.x.x.x",
            "GroupId":336,
            "InstanceName":"****"
```

`},`

```
        ......
```

`]`

#### DescribeEntityList

You can call this operation to query servers of a specified type. For example, you can query servers by security event type.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeEntityList. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| RegionNo | String | No | The ID of the region. |
| GroupId | Long | No | The ID of the asset group. |
| Os | String | No | The operating system of the server. Valid values: win: indicates the Windows operating system. linux: indicates the Linux operating system. |
| Account | String | No | Queries servers with unusual logons detected. Set this parameter to remoteLogin. |

| Health | String | No | Queries servers with baseline check issues detected. Set this parameter to exception. |
|---|---|---|---|
| Patch | String | No | Queries servers with vulnerabilities detected. Set this parameter to vul. |
| Suspicious | String | No | Queries servers with unusual events detected. Set this parameter to exception. |
| Trojan | String | No | Queries servers with webshells detected. Valid values: webshell: indicates trojan files. process: indicates trojan processes. |
| Status | String | No | The status of the Server Guard Agent. Valid values: offline: indicates that the Server Guard Agent is offline. pause: indicates that the Server Guard Agent is disabled. |
| TagIdList | String | No | The server tag ID. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| TotalCount | Integer | The number of returned records. |
| EntityList | Array | The servers. For more information, see the following descriptions. |
| AegisOnline | Boolean | Indicates whether the Server Guard Agent is online. |
| AegisVersion | String | The version of the Server Guard Agent. |
| BuyVersion | String | The version of the Server Guard package. |
| GroupId | Integer | The ID of the asset group. |
| ClientStatus | Boolean | Indicates whether the server is protected. A value of false indicates that the protection for the server is paused. |

| Flag | Integer | The type of the server. Valid values: 0: indicates an Alibaba Cloud ECS instance. 1: indicates an external server. |
|---|---|---|
| Uuid | String | The universally unique identifier (UUID) of the server. |
| InstanceName | String | The instance name of the server. |
| Os | String | The type of the operating system. |
| Region | String | The ID of the region. |
| Ip | String | The IP address of the server. Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeEntityList &Account=remoteLogin &CurrentPage=1 &GroupId=1 &Health=exception &Os=windows &PageSize=20 &Patch=vul &RegionNo=**** &Remark=x.x.x.x &Status=offline &Suspicious=exception &TagIdList=1,2,3 &Trojan=webshell &<Common request parameters>
```

Sample response (JSON format)

```json
    "TotalCount":1,
    "PageSize":1,
    "RequestId":"8BFB5273-6582-446A-9E0B-BAC0A1A468EA",
    "CurrentPage":1,
    "EntityList":[
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "Os":"linux",
            "ClientStatus":false,
            "Ip":"x.x.x.x",
            "Region":"****",
            "Flag":0,
            "BuyVersion":"4",
            "GroupId":336,
            "InstanceName":"****"
```

`]`

#### DescribeMachines

You can call this operation to query servers that match the specified criteria. For example, you can query all servers in an asset group.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeMachines. |
| GroupId | Long | No | The ID of the asset group. |
| TagIdList | String | No | The server tag ID. |
| Mark | String | No | The IP address or instance name of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| Count | Integer | The number of returned records. |
| Machines | Array | The servers. For more information, see the following descriptions. |

| GroupId | Integer | The ID of the asset group. |
|---|---|---|
| InstanceName | String | The instance name of the server. |
| Os | String | The type of the operating system. |
| Ip | String | The IP address of the server. Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |
| Uuid | String | The universally unique identifier (UUID) of the server. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeMachines &GroupId=123 &<Common request parameters>
```

Sample response (JSON format)

```json
    "Count":1,
    "Machines":[
            "groupId":336,
            "os":"linux",
            "instanceName":"****",
            "uuid":"inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
            "ip":"192.168.x.x"
```

`],`

```json
    "RequestId":"C984123D-C8E0-4974-9CEE-ADD0596C46DB"
```

#### DescribeMachineDetail

You can call this operation to query the detailed information about a specified server.

| Parameter | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeMachineDetail. |
|---|---|---|---|
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| MachineDetail | Array | The detailed information about the server. For more information, see the following descriptions. |
| AegisOnline | Boolean | Indicates whether the Server Guard Agent is online. |
| AegisVersion | String | The version of the Server Guard Agent. |
| BuyVersion | String | The version of the Server Guard package. |
| GroupId | Integer | The ID of the asset group. |
| ClientStatus | Boolean | Indicates whether the server is protected. A value of false indicates that the protection for the server is paused. |
| Flag | Integer | The type of the server. Valid values: 0: indicates an Alibaba Cloud ECS instance. 1: indicates an external server. |
| GroupId | Long | The ID of the asset group. |
| GroupTrace | String | The full path of the asset group. |
| InstanceId | String | The instance ID of the server. |
| InstanceName | String | The instance name of the server. |
| Os | String | The type of the operating system. |
| Region | String | The ID of the region. |
| Ip | String | The IP address of the server. Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |
| IntranetIp | String | The private IP address of the server. |
| Uuid | String | The UUID of the server. |

| Tag | String | The server tag ID. |
|---|---|---|

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeMachineDetail &Uuid=6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac &<Common request parameters>
```

Sample response (JSON format)

```json
    "RequestId":"5D5D6F8F-6986-4996-9321-8EEA9FC048D1",
    "MachineDetail":{
        "Uuid":"inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
        "Ip":"192.168.x.x",
        "GroupTrace":"Not grouped",
        "Os":"linux",
        "ClientStatus":true,
        "Region":"outside-of-aliyun",
        "Tag":"",
        "AegisOnline":false,
        "InstanceName":"****"
```

#### DescribePropertyStatistic

You can call this operation to query the server statistics.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertyStatistic. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|

| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
|---|---|---|
| PropertyStatistics | Array | The list of server statistics. For more information, see the following parameter descriptions. |
| PortCount | String | The number of enabled ports. |
| PortGetDate | String | The port information update time. |
| ProcCount | String | The number of running processes. |
| ProcGetDate | String | The process information update time. |
| RootUserCount | String | The number of user accounts with root permission. |
| UserCount | String | The total number of user accounts. |
| UserGetDate | String | The user account information update time. |
| Uuid | String | The UUID of the server. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyStatistic &Uuids=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818 &<Common request parameters>
```

Sample responses (JSON format)

```json
 "PropertyStatistics":[
   "UserGetDate":1514373155000,
   "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
   "RootUserCount":1,
   "UserCount":33,
   "ProcCount":89,
   "PortGetDate":1514115614000,
   "PortCount":6,
   "ProcGetDate":1514373133000
```

`],`

```json
 "RequestId":"C1CACE7E-E868-4E44-A52E-4CB1463B62BB"
```

#### DescribePropertyPortItem

You can call this operation to obtain a list of listener ports on hosts.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertyPortItem. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Port | String | No | The port number. |
| ProcName | String | No | The process name. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertyPortItems | Array | The list of listener ports on hosts. For more information, see the following parameter descriptions. |
| Count | Integer | The number of hosts that have enabled the specified port. |
| Port | String | The port number. |
| Proto | String | The network protocol, such as TCP or UDP. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyPortItem &Port=22 &<Common request parameters>
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PageSize":20,
 "RequestId":"9D38986A-F145-4FA8-AE1C-1DB1C2BDF4C0",
 "CurrentPage":1,
 "PropertyPortItems":[
   "Proto":"tcp",
   "Port":"22",
   "Count":2
```

`],`

```json
 "Count":1
```

#### DescribePropertyPortDetail

You can call this operation to query detailed information about a listening port.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertyPortDetail. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| GroupId | Long | No | The ID of the asset group. |
| Ip | String | No | The IP address of the server. |
| Port | String | No | The port number. |

| Extend | String | No | Indicates whether fuzzy match is enabled to search for port numbers. Valid values: 1: indicates that fuzzy match is enabled. 0: indicates that fuzzy match is disabled. |
|---|---|---|---|
| ProcName | String | No | The name of the process. |
| Mark | String | No | The IP address or instance name of the server. Note Fuzzy match is supported. |
| TagIdListString | String | No | The server tag ID. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyPorts | Array | The information about the listening port. For more information, see the following descriptions. |
| BindIp | String | The IP address bound to the port. |
| Create | String | The time when the port was enabled. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| Port | String | The port number. |
| ProcName | String | The name of the process. |
| Proto | String | The network protocol, such as TCP and UDP. |
| Uuid | String | The UUID of the server. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyPortDetail &Uuid=inet-f6ac9a93-0818-4052-90e2-d24f18ee198b &<Common request parameters>
```

Sample response (JSON format)

```json
    "TotalCount":1,
    "PageSize":20,
    "RequestId":"D85484BB-4DC2-44EC-AD67-0B3765EC9213",
    "CurrentPage":1,
    "PropertyPorts":[
            "InstanceName":"****",
            "Uuid":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
            "Proto":"tcp",
            "Create":1514373168000,
            "Ip":"x.x.x.x",
            "Port":"22",
            "ProcName":"sshd",
            "BindIp":"0.0.0.0"
```

`],`

```json
    "Count":1
```

#### DescribePropertyProcItem

You can call this operation to obtain a list of server processes.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertyProcItem. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |

| CurrentPage | Integer | No | The current page number. Default value: 1. |
|---|---|---|---|
| Name | String | No | The process name. |
| User | String | No | The user who started the process. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertyProcItems | Array | The list of server processes. For more information, see the following parameter descriptions. |
| Count | Integer | The number of servers on which the process is running. |
| Name | String | The process name. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyProcItem &Name=init &<Common request parameters>
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PropertyProcItems":[
   "Count":2,
   "Name":"init"
```

`],`

```json
 "PageSize":20,
 "RequestId":"8BE95FB1-66B7-4509-AF82-3AA67368A5D8",
 "CurrentPage":1,
 "Count":1
```

#### DescribePropertyProcDetail

You can call this operation to query server process details.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertyProcDetail. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| GroupId | Long | No | The ID of the asset group. |
| Ip | String | No | The IP address of the server. |
| Name | String | No | The name of the process. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for process names. Valid values: 1: indicates that fuzzy match is enabled. 0: indicates that fuzzy match is disabled. |
| User | String | No | The user who started the process. |

| Mark | String | No | The IP address or instance name of the server. Note Fuzzy match is supported. |
|---|---|---|---|
| Cmdline | String | No | The process parameter. |
| TagIdListString | String | No | The server tag ID. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyProcs | Array | The details of the server process. For more information, see the following descriptions. |
| Cmdline | String | The process parameter. |
| Create | String | The time when the information was reported. |
| EuidName | String | The permissions that the process has to access resources and files. |
| InstanceName | String | The instance name of the server. |
| Md5 | String | The MD5 value of the executable file. |
| Name | String | The name of the process. |
| Path | String | The path of the process. |
| Pid | String | The ID of the process. |
| ProcName | String | The name of the process. |
| Pname | String | The name of the parent process. |
| StartTime | String | The time when the process was started. |
| User | String | The user who started the process. |

| Uuid | String | The UUID of the server. |
|---|---|---|

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyProcDetail &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818 &<Common request parameters>
```

Sample response (JSON format)

```json
    "PropertyProcs":[
            "InstanceName":"****",
            "Path":"/sbin/init",
            "Pname":"N/A",
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "User":"root",
            "Create":1514373133000,
            "StartTime":"2017-12-26 22:34:45",
            "Pid":"1",
            "EuidName":"root",
            "Cmdline":"/sbin/init",
            "Name":"init",
            "Md5":"70023aaf3f480d198d3b078d8c39****"
```

`],`

```json
    "TotalCount":1,
    "PageSize":20,
    "RequestId":"AB20A6D4-43EB-44E2-AD64-E03EAC1C14D9",
    "CurrentPage":1,
    "Count":1
```

#### DescribePropertySoftwareItem

You can call this operation to query servers that have been installed with the specified application.

| Name | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertySoftwareItem. |
|---|---|---|---|
| PageSize | Integer | No | The maximum number of records displayed on a page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Name | String | No | The name of the application. |
| Path | String | No | The application installation path. |
| SoftwareVersion | String | No | The version of the application. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertySoftwareItems | Array | A list of servers that have been installed with the application. For more information, see the following parameter descriptions. |
| Count | Integer | The number of servers that have been installed with the application. |
| Name | String | The name of the application. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertySoftwareItem &Name=spice-vdagent &<Common request parameters>
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PropertySoftwareItems":[
   "count":2,
   "Name":"spice-vdagent"
```

`],`

```json
 "PageSize":20,
 "RequestId":"0F2A3DEA-A5B3-4C2A-8BFC-4724A205E28B",
 "CurrentPage":1,
 "count": 1,
```

#### DescribePropertySoftwareDetail

You can call this operation to query the details of software installed on a server.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertySoftwareDetail. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| Ip | String | No | The IP address of the server. |
| Name | String | No | The name of the software. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for software names.. Valid values: 1: indicates that fuzzy match is enabled. 0: indicates that fuzzy match is disabled. |
| Path | String | No | The installation path of the software. |

| Remark | String | No | The IP address or instance name of the server. Note Fuzzy match is supported. |
|---|---|---|---|
| SoftwareVersion | String | No | The version of the software. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertySoftwares | Array | The details of software installed on the server. For more information, see the following descriptions. |
| Create | String | The time when the information was reported. |
| InstallTime | String | The time when the software was installed. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| Path | String | The installation path of the software. |
| Version | String | The version of the software. |
| Uuid | String | The UUID of the server. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertySoftwareDetail &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818 &<Common request parameters>
```

Sample response (JSON format)

```json
    "TotalCount":1,
    "PropertySoftwares":[
            "InstanceName":"****",
            "Path":"/usr/libexec/gvfs-gphoto2-volume-monitor",
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "InstallTime":"2016-06-29 06:55:22",
            "Version":"1.4.3",
            "Create":1514172615000,
            "Ip":"x.x.x.x"
```

`],`

```json
    "PageSize":20,
    "RequestId":"31409246-AB88-4B36-A2B8-16D21BA9E170",
    "CurrentPage":1,
    "Count":1
```

#### DescribePropertyUserItem

You can call this operation to query user account information.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribePropertyUserItem. |
| PageSize | Integer | No | The maximum number of records displayed on a page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| User | String | No | The username of the account. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |

| Count | Integer | The number of records on the current page. |
|---|---|---|
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertyUserItems | Array | The returned user account information. For more information, see the following parameter descriptions. |
| Count | Integer | The number of servers under the account. |
| Name | String | The username of the account. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyUserItem &<Common request parameters>
```

Sample responses (JSON format)

```json
 "TotalCount":2,
 "PropertyUserItems":[
   "User":"abrt",
   "Count": 2
```

`},`

```json
   "User":"adm",
   "Count": 2
```

`],`

```json
 "PageSize":20,
 "RequestId":"E80981C2-AD12-4C60-9976-6927C1FE449B",
 "CurrentPage":1,
 "Count": 2
```

#### DescribePropertyUserDetail

You can call this operation to query user account details.

| Parameter | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribePropertyUserDetail. |
|---|---|---|---|
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| GroupId | Long | No | The ID of the asset group. |
| Ip | String | No | The IP address of the server. |
| IsRoot | String | No | Indicates whether the user account is a root account. Valid values: 1: indicates yes. 0: indicates no. |
| User | String | No | The name of the user account. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for user accounts. Valid values: 1: indicates that fuzzy match is enabled. 0: indicates that fuzzy match is disabled. |
| Mark | String | No | The IP address or instance name of the server. Note Fuzzy match is supported. |
| TagIdListString | String | No | The server tag ID. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |

| PageSize | Integer | The number of records returned on each page. |
|---|---|---|
| PropertyUsers | Array | The details of the user account. For more information, see the following descriptions. |
| AccountsExpirationDat e | String | The time when the user account expires. |
| Create | String | The time when the information was reported. |
| GroupName | String | The information about the user group. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| IsRoot | String | Indicates whether the user account is a root account. |
| LastLoginIp | String | The last IP address that is used by the user account to log on to the server. |
| LastLoginTime | String | The last logon time of the user account. |
| PasswordExpirationDat e | String | The time when the password of the user account expires. |
| User | String | The name of the user account. |
| Uuid | String | The UUID of the server. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribePropertyUserDetail &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818 &<Common request parameters>
```

Sample response (JSON format)

```json
    "TotalCount":66,
    "PageSize":2,
    "RequestId":"2EEAE2A6-1662-471C-A5E5-8A6190B01AFF",
    "CurrentPage":1,
    "Count":1,
    "PropertyUsers":[
            "GroupName":[
                "root"
```

`],`

```json
            "InstanceName":"****",
            "IsRoot":"1",
            "LastLoginTime":"2017-12-27 10:22:25",
            "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "User":"root",
            "LastLoginIp":"192.168.x.x",
            "Create":1514373155000,
            "Ip":"x.x.x.x",
            "AccountsExpirationDate":"never",
            "PasswordExpirationDate":"never"
```

`]`

#### DescribeTopRiskyAssets

You can call this operation to query top N vulnerable servers.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeTopRiskyAssets. |
| PageSize | Integer | No | The number of records to return, that is, the top N vulnerable servers. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |

| TopRiskyAssets | Array | The top N vulnerable servers. For more information, see the following descriptions. |
|---|---|---|
| HcCount | String | The number of at-risk items detected in the baseline check. |
| Ip | String | The IP address of the server. |
| Uuid | String | The universally unique identifier (UUID) of the server. |
| VulCount | String | The number of detected vulnerabilities. |
| WarningCount | String | The number of detected security events. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeTopRiskyAssets &PageSize=1 &<Common request parameters>
```

Sample response (JSON format)

```json
    "TotalCount": 1,
    "RequestId": "5D8D4058-2EE3-4599-9951-BDAA3340AD4D",
    "TopRiskyAssets": [
            "Ip": "192.168.x.x",
            "Uuid": "inet-dsljaoe-jjdsklaj****",
            "VulCount": 2,
            "HcCount": 1,
            "WarningCount": 2
```

`]`

#### CreateAssetGroup

API for user login

**Request headers**

This operation uses common request headers and does not have any special request headers. For more information, see Common request parameters.

| Parame ter name | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupNa me | Strin g | Query | No | Ungrouped | The name of the group. |
| GroupId | Strin g | Query | No | 1 | The ID of the group. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| GroupId | String | 12345 | The ID of the server group. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateAssetGroup &Common request parameters
```

Sample success response `JSON` format

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "GroupId":"12345"
```

#### DescribePropertyUserChangeItem

Queries the records of property changes for users in Security Center.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Uuid | Strin g | Query | No | 00f2-xxx-xxx | The unique ID of the server. |

| libaba Cloud rd Advanced | Security- Edition | Server Gu |   | Serve evelo | r Guard Advanced Edition D per Guide·API documentat o |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| User | Strin g | Query | No | root | The username. |
| UserId | Strin g | Query | No | 123 | The user ID. |
| IsRoot | Strin g | Query | No | 1 | Specifies whether the user has root permissions. Valid values: 0 : No 1 : Yes |
| ChangeTi meStart | Long | Query | No | 1649066826000 | The start time of the change. |
| ChangeTi meEnd | Long | Query | No | 1649066826000 | The end time of the change. |
| CurrentPa ge | Integ er | Query | No | 4 | The number of the page to return. |
| PageSize | Integ er | Query | No | 20 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PropertyUserC hangeItemList | Array | - | The unique identifier of a record of a user property change. |
| -UserId | Long | 123 | The user ID. |
| -UserName | String | test | The username. |
| -Count | Integer | 1 | The number of items displayed on the current page for a paged query. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| PageInfo | Struct | - | The pagination information. |

| S e o | erver Guard Adv veloper Guide·AP n | anced Edition D I documentati |   | Alibaba Cloud Security-Server G ard Advanced Editio | u n |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Count | Integer | 1 | The number of entries returned on the current page. |
| -PageSize | Integer | 10 | The number of entries per page. |
| -TotalCount | Integer | 10 | The total number of entries. |
| -CurrentPage | Integer | 1 | The page number of the returned page. |

Request example

```
http(s)://[Endpoint]/?Action=DescribePropertyUserChangeItem &<Common request parameters>
```

Response example `JSON` format

```json
 "PageInfo":{
  "TotalCount":10,
  "PageSize":10,
  "CurrentPage":1,
  "Count":1
```

`},`

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PropertyUserChangeItemList":[
   "UserName":"test",
   "UserId":123,
   "Count":1
```

`]`

### Vulnerability management

#### DescribeTarget

You can call this operation to query the servers that are checked for the specified type of risks in vulnerability management.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeTarget. |
| Type | String | No | The type of the risks. For example, vul represents vulnerabilities. |
| Config | String | No | The type of the vulnerabilities in JSON format. For example, {"vulType":"cve"} represents Linux software vulnerabilities. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| Targets | Array | A list of servers that are checked for the specified type of risks. For more information, see the following parameter descriptions. |
| TargetType | String | Valid values: groupId: indicates the ID of an asset group. uuid: indicates the UUID of a server. |
| Target | String | The asset group ID or server UUID. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeTarget &Config={"vulType":"cve"} &Type=vul &<Common request parameters>
```

Sample responses (JSON format)

```json
    "TotalCount":2,
    "RequestId":"1FF54D56-47ED-47FB-B4DB-2BDF3857D526",
    "Targets":[
            "Target":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
            "TargetType":"uuid"
```

`},`

```json
            "Target":"336",
            "TargetType":"groupId"
```

`]`

#### DescribeVulTargetStatistics

You can call this operation to query the information about target hosts for which vulnerability detection is enabled in the vulnerability management configuration.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulTargetStatistics. |
| Type | String | No | The vulnerability type. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of returned records. |
| TargetStats | Array | The list of target hosts for which vulnerability detection is enabled. For more information, see the following parameter descriptions. |
| VulType | String | The vulnerability type. |

| Targets | Array | The information about target hosts. For more information, see the following parameter descriptions. |
|---|---|---|
| Flag | String | Indicates whether vulnerability detection is enabled. |
| TargetType | String | The type of the Target parameter value. Valid values: groupId: indicates an asset group ID. uuid: indicates a host asset UUID. |
| Target | String | The asset group ID or host asset UUID. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulTargetStatistics &Type=cve &<Common request parameters>
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "TargetStats":[
   "VulType":"cve","Targets":[]
```

`},`

```json
 "PageSize":10,
 "RequestId":"89DD84B4-B592-476C-A6C0-51D56B3E8EAC",
 "CurrentPage":1
```

#### DescribeTargetConfig

You can call this operation to query the vulnerability scanning configuration information of a specified server.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeTargetConfig. |
| Type | String | No | The type of the vulnerability. |

| Uuid | String | No | The UUID of the server. |
|---|---|---|---|

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of the returned records. |
| TargetConfigs | Array | The list of vulnerability scanning configuration information. For more information, see the following parameter descriptions. |
| Type | String | The type of the vulnerability. |
| Config | String | Whether vulnerability scanning is enabled. Valid values: on and off. |
| OverAllConfig | String | Whether global vulnerability scanning is enabled. Valid values: on and off. Note The global vulnerability scanning configuration overrides the vulnerability scanning configuration for a single server. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeTargetConfig &Type=cve &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818 &<Common request parameters>
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "RequestId":"092094BF-910F-4CE6-BE93-C3989B607977",
 "TargetConfigs":[
   "Config":"off",
   "Type":"cve",
   "OverAllConfig":"off"
```

`]`

#### DescribeVulConfig

You can call this operation to query the global scanning configuration for each vulnerability type.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulConfig. |
| Type | String | No | The type of the vulnerability. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| TargetConfigs | Array | The list of global vulnerability scanning configurations. For more information, see the following parameter descriptions. |
| Type | String | The type of the vulnerability. |
| Config | String | The global scanning configuration for the vulnerability type. Valid values: on and off. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulConfig &Type=cve &<Common request parameters>
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "RequestId":"A8E09216-31DF-45B6-A76B-E3F053752C07",
 "TargetConfigs":[
   "Config":"off",
   "Type":"cve"
```

#### DescribeAutoDelConfig

You can call this operation to query the number of days that an invalid vulnerability is kept for before it is automatically deleted in the vulnerability management settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeAutoDelConfig. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Days | Integer | The number of days that an invalid vulnerability is kept for. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeAutoDelConfig &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053",
 "Days":7
```

#### DescribeVulLevel

You can call this operation to query the vulnerability severities that require attention.

| Name | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulLevel. |
|---|---|---|---|

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| ConcernLevels | List | The list of vulnerability severities that require attention. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulLevel &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"7935CB7A-D1B7-4EE6-93D0-FF3D040CF19B",
 "ConcernLevels":["high","medium"]
```

#### DescribeVulWhitelist

You can call this operation to obtain the whitelist of vulnerabilities.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulWhitelist. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of returned records. |
| VulWhitelists | Array | The vulnerability whitelist. For more information, see the following parameter descriptions. |
| AliasName | String | The alias of the vulnerability. |
| Name | String | The name of the vulnerability. |
| Reason | String | The reason for adding the vulnerability to the whitelist. |
| Type | String | The vulnerability type. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulWhitelist &CurrentPage=1 &PageSize=20 &<Common request parameters>
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "VulWhitelists":[
   "Name":"oval:com.redhat.rhsa:def:20173263",
   "AliasName":"RHSA-2017:3263: curl security update",
   "Type":"cve",
   "Reason":"Not fixed at present"
```

`],`

```json
 "PageSize":3,
 "RequestId":"74F97EF7-B543-43FD-A4E9-18456731F9C5",
 "CurrentPage":1
```

#### DescribeGroupedVul

You can call this operation to query information about the specified vulnerability group. The vulnerability management feature can display detected vulnerability records by group. A vulnerability group contains all servers with a specific vulnerability detected by Server Guard.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeGroupedVul. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Dealed | String | No | Indicates whether the vulnerability has been handled. Valid values: Y: indicates that the vulnerability has been handled. N: indicates that the vulnerability has not been handled. |
| Direction | String | No | The sorting mode of vulnerabilities in the vulnerability group. Valid values: asc: indicates sorting in ascending order. desc: indicates sorting in descending order. |
| LastTsEnd | Long | No | The end time of the last detection of the vulnerability. |
| LastTsStart | Long | No | The start time of the last detection of the vulnerability. |
| Level | String | No | The severity of the vulnerability. Valid values: serious: critical high: important medium: moderate low: low |
| Name | String | No | The name of the vulnerability. |

| Necessity | String | No | The necessity for fixing the vulnerability. Valid values: asap: indicates that the vulnerability must be fixed as soon as possible. later: indicates that the vulnerability can be fixed later. nntf: indicates that the vulnerability can be ignored. |
|---|---|---|---|
| OrderBy | String | No | The field based on which the vulnerabilities in the vulnerability group are sorted. You can specify other request parameters for sorting order. |
| PatchId | Long | No | The ID of the patch used to fix the vulnerability. |
| Product | String | No | The product where the vulnerability exists. |

| StatusList | String | No | The status of the vulnerability. Valid values: 1: indicates that the vulnerability has not been fixed. 2: indicates that the vulnerability fix failed. 3: indicates that the server has failed to be rolled back to the version before the vulnerability fix. 4: indicates that the vulnerability is being fixed. 5: indicates that the server is being rolled back to the version before the vulnerability fix. 6: indicates that the vulnerability fix is being verified. 7: indicates that the vulnerability has been fixed successfully. 8: indicates that the vulnerability has been fixed successfully, and that the server is waiting for restart. 9: indicates that the server has been rolled back to the version before the vulnerability fix. 10: indicates that the vulnerability has been ignored. 11: indicates that the server has been rolled back to the version before the vulnerability fix, and that the server is waiting for restart. 12: indicates that the vulnerability does not exist. 20: indicates that the vulnerability is invalid. Note The statuses are specified in a single parameter, separated with commas (,). |
|---|---|---|---|
| Type | String | No | The type of the vulnerability. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |

| PageSize | Integer | The maximum number of records displayed on a page. |
|---|---|---|
| TotalCount | Integer | The total number of returned records. |
| GroupedVulItems | Array | The information about the vulnerability group. For more information, see the following parameter descriptions. |
| AliasName | String | The alias of the vulnerability. |
| AsapCount | Integer | The number of assets to be fixed as soon as possible. |
| Count | Integer | The total number of vulnerabilities. |
| GmtLast | Long | The last time when the vulnerability was detected. |
| HandledCount | Integer | The total number of vulnerabilities handled. |
| Level | String | The severity of the vulnerability. |
| Name | String | The name of the vulnerability. |
| PendingCount | Integer | The number of vulnerabilities that have not been handled. |
| Product | String | The product affected by the vulnerability. |
| Status | Integer | The status of the vulnerability. |
| TotalCount | Integer | The total number of vulnerabilities. |
| Type | String | The type of the vulnerability. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeGroupedVul &CurrentPage=1 &Dealed=y &Direction=asc &LastTsEnd=1517414400000 &LastTsStart=1517414500000 &Level=high &Name=oval:com.redhat.rhsa:def:20170817 &Necessity=asap &OrderBy=name &PageSize=20 &PatchId=27001 &Product=redhat &SourceIp= &StatusList=1,2 &Type=cve &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c,b688bf9f-1fd9-42c8-bb34-28697f562dc5 &<Common request parameters>
```

Sample responses (JSON format)

```json
 "GroupedVulItems":[
   "Name":"oval:com.redhat.rhsa:def:20170817",
   "Status":7,
   "Count":0,
   "TotalCount":1,
   "PendingCount":0,
   "AliasName":"RHSA-2017:0817: kernel security, bug fix, and enhancement update",
   "AsapCount":0,
   "Type":"cve",
   "GmtLast":1513695612000,
   "Level":"high",
   "HandledCount":1
```

`},` `],`

```json
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"6FCF95BE-7A78-4AD8-811C-BF12FC34AC34",
 "CurrentPage":1
```

#### DescribeVulList

You can call this operation to obtain the vulnerability list of the specified host asset.

| Name | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulList. |
|---|---|---|---|
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Dealed | String | No | Indicates whether the vulnerability has been handled. Valid values: Y: indicates that the vulnerability has been handled. N: indicates that the vulnerability has not been handled. |
| Level | String | No | The severity of the vulnerability. Valid values: serious: critical high: important medium: moderate low: low |
| Name | String | No | The name of the vulnerability. |
| Necessity | String | No | The necessity for fixing the vulnerability. Valid values: asap: indicates that the vulnerability must be fixed as soon as possible. later: indicates that the vulnerability can be fixed later. nntf: indicates that the vulnerability can be ignored. |
| Type | String | No | The type of the vulnerability. |

| StatusList | String | No | The status of the vulnerability. Valid values: 1: indicates that the vulnerability has not been fixed. 2: indicates that the vulnerability fix failed. 3: indicates that the host has failed to be rolled back to the version before the vulnerability fix. 4: indicates that the vulnerability is being fixed. 5: indicates that the host is being rolled back to the version before the vulnerability fix. 6: indicates that the vulnerability fix is being verified. 7: indicates that the vulnerability has been fixed successfully. 8: indicates that the vulnerability has been fixed successfully, and that the host is waiting for restart. 9: indicates that the host has been rolled back to the version before the vulnerability fix. 10: indicates that the vulnerability has been ignored. 11: indicates that the host has been rolled back to the version before the vulnerability fix, and that the host is waiting for restart. 12: indicates that the vulnerability does not exist. 20: indicates that the vulnerability is invalid. Note Note: The statuses are specified in a single parameter, separated with commas (,). |
|---|---|---|---|
| Uuids | String | No | The UUID of the host asset. Separate multiple host asset UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |

| TotalCount | Integer | The total number of records returned from the query. |
|---|---|---|
| VulRecords | Array | The list of vulnerabilities. For more information, see the following parameter descriptions. |
| AliasName | String | The alias of the vulnerability. |
| ExtendContent | String | The extended information of the vulnerability. |
| ExtendContentJson | String | The extended information of the vulnerability (JSON format). |
| FirstTs | Long | The first time when the vulnerability was detected. |
| ModifyTs | Long | The last time when the vulnerability was updated. |
| LastTs | Long | The last time when the vulnerability was detected. |
| Level | String | The severity of the vulnerability. |
| Name | String | The name of the vulnerability. |
| Necessity | String | The necessity for fixing the vulnerability. Valid values: asap: indicates that the vulnerability must be fixed as soon as possible. later: indicates that the vulnerability can be fixed later. nntf: indicates that the vulnerability can be ignored. |
| PrimaryId | Long | The ID of the primary key. |
| Product | String | The product affected by the vulnerability. |
| RecordId | Long | The ID of the vulnerability record. |
| Related | String | The CVE ID of the vulnerability. |
| RepairTs | Long | The time when the vulnerability was fixed. |
| ResultCode | String | The code of the vulnerability handling result. |
| ResultMessage | String | The message of the vulnerability handling result. |
| RiskDesc | String | The risk description of the vulnerability. |
| RiskLevel | Integer | The risk level of the vulnerability. |

| Status | Integer | The status of the vulnerability. Valid values: 1: indicates that the vulnerability is to be handled. 2: indicates that the vulnerability has been ignored. 3: indicates that the vulnerability has been confirmed. 8: indicates that the vulnerability has been marked as a false positive. 16: indicates that the vulnerability is being handled. 32: indicates that the vulnerability has been handled. |
|---|---|---|
| Tag | String | The tag of the vulnerability. |
| Type | String | The type of the vulnerability. |
| Uuid | String | The UUID of the host asset. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulList &CurrentPage=1 &Dealed=n &Level=serious &Name=RHSA-2017:1100: nss and nss-util security update &Necessity=asap &PageSize=20 &StatusList=1 &Type=cve &Uuids=f293ade2-e5b1-4cc0-99a6-cc993a4158cc &<Common request parameters>
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PageSize":20,
 "RequestId":"2E35F7F7-DA6D-46A5-BA9D-8751BDAE7710",
 "CurrentPage":1,
 "VulRecords":[
   "Uuid":"b688bf9f-1fd9-42c8-bb34-28697f562dc5",
   "Necessity":"nntf",
   "ModifyTs":1512949391000,
   "Type":"cve",
   "FirstTs":1499321694000,
   "Related":"CVE-2016-1248",
   "ExtendContentJson":{"Necessity":
{"Cvss_factor":"6.8","Total_score":"6.799999965526585","Status":"normal","Enviroment_fa or":"1.0","Time_factor":"0.9999999949303802","Assets_factor":"1","Gmt_create":"20171210 "Is_calc":"1"},"Os":"centos","cveList":["CVE-2016-1248"],"RpmEntityList": [{"Name":"vim-minimal","Version":"7.4.160","FullVersion":"7.4.160- 1.el7","MatchDetail":"vim-minimal version less than 2:7.4.160- 1.el7_3.1","UpdateCmd":"yum update vimminimal","Path":"/etc/virc"}],"OsRelease":"7"},
   "Name":"oval:com.redhat.rhsa:def:20162972",
   "Status":1,
   "LastTs":1512949391000,
   "AliasName":"RHSA-2016:2972: vim security update (Moderate)",
   "Tag":"oval",
   "PrimaryId":281156,
   "Level":"high"
```

`]`

#### DescribeVulDetails

You can call this operation to query detailed information about a vulnerability.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulDetails. |
| Type | Integer | Yes | The type of the vulnerability. |
| Name | String | Yes | The name of the vulnerability. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Cves | Array | The vulnerability details. For more information, see the following parameter descriptions. |
| Classify | String | The vulnerability type code. |
| Classifys | Array | The detailed vulnerability information. For more information, see the following parameter descriptions. |
| Classify | String | The vulnerability type code. |
| Description | String | The description of the vulnerability type. |
| DemoVideoUrl | String | The URL of the vulnerability video demo. |
| CnvdId | String | The CNVD ID. |
| Complexity | String | The complexity. |
| Content | String | The vulnerability details. |
| ExtendContentJson | String | The additional information about the vulnerability (JSON format). |
| CveId | String | The CVE ID. |
| CvssScore | String | The CVSS score. |
| CvssVector | String | The CVSS score string. |
| OtherId | String | The ID of the vulnerability. |
| Poc | String | The proof of concept (POC) method. |
| PocCreateTime | Long | The time when the POC method was created. |
| PocDisclosureTime | Long | The time when the POC method was revealed. |
| Service | String | The products that are affected by the vulnerability. |
| Reference | String | The corresponding reference. |
| ReleaseTime | Long | The time when the vulnerability was revealed. |
| Solution | String | The solution for fixing the vulnerability. |
| Summary | String | The vulnerability summary. |
| Title | String | The title of the vulnerability. |
| Vendor | String | The vendors that are affected by the vulnerability. |

| VulLevel | String | The severity level of the vulnerability. |
|---|---|---|

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulDetails &Name=oval:com.redhat.rhsa:def:20170036 &Type=cve &<Common request parameters>
```

Sample responses (JSON format)

```json
 "Cves": [{
  "CvssVector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
  "OtherId": "CVE-2016-7117",
  "Classifys": [],
  "Vendor": "Linux",
  "CvssScore": "10.0",
  "CnvdId": "CNVD-2016-09362",
  "Reference": "http://www.securityfocus.com/bid/93304",
  "Solution": "<p>The vendor has released a patch to fix this vulnerability. Download
the patch from: \n<br />https://bugzilla.redhat.com/show_bug.cgi?id=1382268</p>\n",
  "CveId": "CVE-2016-7117",
  "ReleaseTime": 1476028800000,
  "VulLevel": "serious",
  "Title": "The use-after-free vulnerability in __sys_recvmmsg function in the Linux
kernel",
  "Summary": "The Linux kernel is released by the Linux Foundation of the United Stat
es for Linux operating systems. The use-after-free vulnerability is found in the net/ socket.c file in \n\nLinux kernel 4.5.2 and earlier versions. It allows remote attack ers to execute arbitrary code."
 }],
 "RequestId": "70DEE6B7-A167-4B5D-ADAA-3631443D5190"
```

#### DescribeVulNumStatistics

You can call this operation to query vulnerability statistics.

| Name | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulNumStatistics. |
|---|---|---|---|
| StartTs | Long | No | The start time for statistics collection. |
| EndTs | Long | No | The end time for statistics collection. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CmsDealedTotalNum | Integer | The number of CMS vulnerabilities handled. |
| CmsNum | Integer | The number of CMS vulnerabilities. |
| CveNum | Integer | The number of CVE vulnerabilities. |
| EmgNum | Integer | The number of other vulnerabilities. |
| SysNum | Integer | The number of Windows OS vulnerabilities. |
| VulAsapSum | Integer | The number of vulnerabilities that need to be handled as soon as possible. |
| VulDealedTotalNum | Integer | The total number of vulnerabilities handled. |
| VulSeriousTotal | Integer | The total number of critical vulnerabilities. |
| VulHighTotal | Integer | The total number of important vulnerabilities. |
| VulMediumTotal | Integer | The total number of moderate vulnerabilities. |
| VulLowTotal | Integer | The total number of low vulnerabilities. |
| VulLaterSum | Integer | The number of vulnerabilities that can be handled later. |
| VulNntfSum | Integer | The number of vulnerabilities that do not need to be fixed temporarily. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulNumStatistics &EndTs=1514736000000 &StartTs=1514736000000 &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c &<Common request parameters>
```

Sample responses (JSON format)

```json
    "VulHighTotal":0,
    "CveNum":1,
    "VulMediumTotal":0,
    "EmgNum":0,
    "VulLowTotal":0,
    "VulNntfSum":1,
    "VulAsapSum":0,
    "SysNum":0,
    "VulDealedTotalNum":1,
    "RequestId":"093C121C-2981-4E69-8309-CD1BDD8C872A",
    "CmsNum":0,
    "VulSeriousTotal":0,
    "CmsDealedTotalNum":0,
    "VulLaterSum":0
```

#### DescribeVulLevelStatistics

You can call this operation to obtain the statistics on vulnerabilities by vulnerability severity.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulLevelStatistics. |
| StartTs | Long | No | The start time of the time frame specified for query. |
| EndTs | Long | No | The end time of the time frame specified for query. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|

| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
|---|---|---|
| TotalCount | Integer | The total number of returned records. |
| LevelStatistics | Array | The vulnerability statistics. For more information, see the following parameter descriptions. |
| CmsDealedTotalNum | Integer | The number of handled CMS vulnerabilities. |
| CmsNum | Integer | The number of CMS vulnerabilities. |
| CveNum | Integer | The number of CVE vulnerabilities. |
| EmgNum | Integer | The number of other vulnerabilities. |
| Level | String | The severity of the vulnerability. |
| SysNum | Integer | The number of Windows vulnerabilities. |
| VulAsapSum | Integer | The number of high-priority vulnerabilities. |
| VulDealedTotalNum | Integer | The total number of handled vulnerabilities. |
| VulSeriousTotal | Integer | The total number of critical-risk vulnerabilities. |
| VulHighTotal | Integer | The total number of important-risk vulnerabilities. |
| VulMediumTotal | Integer | The total number of moderate-risk vulnerabilities. |
| VulLowTotal | Integer | The total number of low-risk vulnerabilities. |
| VulLaterSum | Integer | The number of medium-priority vulnerabilities. |
| VulNntfSum | Integer | The number of low-priority vulnerabilities. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulLevelStatistics &EndTs=1514736000000 &StartTs=1514736000000 &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c,b688bf9f-1fd9-42c8-bb34-28697f562dc5 &<Common request parameters>
```

Sample responses (JSON format)

```json
 "TotalCount":0,
 "LevelStatistics":[
   "VulHighTotal":0,
   "CveNum":0,
   "VulMediumTotal":0,
   "EmgNum":0,
   "VulLowTotal":0,
   "VulNntfSum":0,
   "VulAsapSum":0,
   "SysNum":0,
   "VulDealedTotalNum":0,
   "CmsNum":0,
   "Level":"high",
   "VulSeriousTotal":0,
   "CmsDealedTotalNum":0,
   "VulLaterSum":0
```

`},`

```json
   "VulHighTotal":0,
   "CveNum":0,
   "VulMediumTotal":0,
   "EmgNum":0,
   "VulLowTotal":0,
   "VulNntfSum":0,
   "VulAsapSum":0,
   "SysNum":0,
   "VulDealedTotalNum":0,
   "CmsNum":0,
   "Level":"low",
   "VulSeriousTotal":0,
   "CmsDealedTotalNum":0,
   "VulLaterSum":0
```

`],`

```json
 "RequestId":"9B062D3F-AD5A-4D3E-9A7A-45CAC2713FC0"
```

#### DescribeVulMachineList

You can call this operation to query the vulnerability statistics of a specified server.

| Name | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVulMachineList. |
|---|---|---|---|
| StartTs | Long | No | The start time of the time frame during which the statistics were collected. |
| EndTs | Long | No | The end time of the time frame during which the statistics were collected. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of the returned records. |
| MachineStatistics | Array | The vulnerability statistics. For more information, see the following parameter descriptions. |
| CmsDealedTotalNum | Integer | The number of CMS vulnerabilities that have been handled. |
| CmsNum | Integer | The number of CMS vulnerabilities. |
| CveNum | Integer | The number of CVE vulnerabilities. |
| EmgNum | Integer | The number of other vulnerabilities. |
| SysNum | Integer | The number of Windows vulnerabilities. |
| VulAsapSum | Integer | The number of high-priority vulnerabilities. |
| VulDealedTotalNum | Integer | The total number of vulnerabilities that have been handled. |
| VulSeriousTotal | Integer | The total number of critical-risk vulnerabilities. |
| VulHighTotal | Integer | The total number of important-risk vulnerabilities. |
| VulMediumTotal | Integer | The total number of moderate-risk vulnerabilities. |
| VulLowTotal | Integer | The total number of low-risk vulnerabilities. |
| VulLaterSum | Integer | The number of medium-priority vulnerabilities. |
| VulNntfSum | Integer | The number of low-priority vulnerabilities. |
| Uuid | String | The UUID of the server. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeVulMachineList &EndTs=1514736000000 &StartTs=1514736000000 &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c &<Common request parameters>
```

Sample responses (JSON format)

```json
 "TotalCount":0,
 "MachineStatistics":[
   "Uuid":"577f9886-bf66-4c3c-88ac-28c938cb527b",
   "VulHighTotal":0,
   "CveNum":1,
   "VulMediumTotal":0,
   "EmgNum":0,
   "VulLowTotal":0,
   "VulNntfSum":0,
   "VulAsapSum":0,
   "SysNum":0,
   "VulDealedTotalNum":0,
   "CmsNum":0,
   "VulSeriousTotal":0,
   "CmsDealedTotalNum":0,
   "VulLaterSum":0
```

`],`

```json
 "RequestId":"A3F8BE63-9BA1-450D-BB5D-CE9205E6645D"
```

### Baseline check

#### DescribeStratetyDetail

You can call this operation to query the details of a specified baseline check policy.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeStratetyDetail. |

| Id | String | No | The ID of the baseline check policy. |
|---|---|---|---|

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Strategy | Array | The details of the baseline check policy. For more information, see the following parameter descriptions. |
| CycleDays | Integer | The cycle of policy execution. |
| CycleStartTime | Integer | The start time of policy execution. Valid values: 0: indicates the period from 00:00 to 06:00. 6: indicates the period from 06:00 to 12:00. 12: indicates the period from 12:00 to 18:00. 18: indicates the period from 18:00 to 24:00. |
| Id | Integer | The ID of the policy. |
| Name | String | The name of the policy. |
| Type | Integer | The type of the policy. Valid values: 1: indicates a system default policy. 2: indicates a custom policy. |
| RiskTypeWhiteListQue ryResultList | Array | The risk information contained in the policy. For more information, see the following parameter descriptions. |
| Alias | String | The name of the risk category. |
| On | Boolean | Indicates whether to check for risks of the specified category. |
| TypeName | String | The code of the risk category. |
| SubTypes | Array | The list of risk subcategories. For more information, see the following parameter descriptions. |
| Alias | String | The name of the risk subcategory. |
| TypeName | String | The code of the risk subcategory. |
| On | Boolean | Indicates whether to check for risks of the specified subcategory. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeStratetyDetail &Id=1 &<Common request parameters>
```

Sample responses (JSON format)

```json
     "RequestId": "99F17C4B-2E23-4B41-BBEB-C03963B06EB4",
     "Strategy": {
  "Name": "Yunwu testing",
             "CycleDays": 1,
             "CycleStartTime": 18,
             "Type": 2,
             "Id": 12,
             "RiskTypeWhiteListQueryResultList": [
                     "On": false,
                     "Alias": "Compliance with Security Standards",
                     "TypeName": "cis",
                     "SubTypes": [
                              "On": true,
                              "Alias": "Memcached",
                              "TypeName": "memcached-check"
```

`},`

```json
                              "On": true,
                              "Alias": "CentOS 7",
                              "TypeName": "centos7"
```

`},`

```json
                              "On": false,
                              "Alias": "Tomcat 7",
                              "TypeName": "tomcat7"
```

`},`

```json
                              "On": false,
                              "Alias": "MongoDB",
                              "TypeName": "mongodb-check"
```

`]` `]`

#### DescribeStrategyTarget

You can call this operation to query the information about asset groups to which a specified baseline check policy applies.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeStrategyTarget. |
| Config | String | No | The policy configuration information. The baseline check policy ID is specified in JSON format, for example, {"strategyId":15161} . |
| Type | String | No | The configuration type. Set the value to hc strategy. _ |
| Target | String | No | The ID of the asset group to which the baseline check policy applies. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| StrategyTargets | Array | The information about asset groups to which the policy applies. For more information, see the following parameter descriptions. |
| Flag | String | Indicates whether the policy applies to the specified asset group. Valid values: add: indicates the whitelist mode, that is, the policy applies to the asset group. del: indicates the blacklist mode, that is, the policy does not apply to the asset group. Note Generally, the blacklist mode is used for system default policies, and the whitelist mode is used for custom policies. |
| TargetType | String | The return value is fixed to groupId, indicating that the value of the Target parameter is the ID of the asset group. |
| Target | String | The asset group ID. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeStrategyTarget &Config={"strategyId":15161} &Type=hc_strategy &<Common request parameters>
```

Sample responses (JSON format)

```json
        "Count": 1,
        "StrategyTargets":[
                "Flag": "del",
                "Target": "281801",
                "TargetType": "groupId"
```

`]`

```json
 "requestId": "B44F545D-15CF-4A57-B8BF-4340D15D0507"
```

#### DescribeUuidConfig

You can call this operation to check whether baseline check is enabled for a specified server.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeUuidConfig. |
| Uuid | String | No | The UUID of the server. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Data | Struct | The baseline check configuration. For more information, see the following parameter descriptions. |
| Flag | String | Indicates whether baseline check is enabled. Valid values: add: indicates enabled. del: indicates disabled. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeUuidConfig &uuid=4bc19998-e100-4b04-ab11-1e677418d311 &<Common request parameters>
```

Sample responses (JSON format)

```json
    "Data": {
        "Flag": "del"
```

`},`

```json
    "RequestId": "A89978FE-BC35-427E-A4B1-7AEEAE741CC2",
```

#### DescribeUserSetting

You can call this operation to query the number of days an invalid risk is kept for before it is automatically deleted in baseline check.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeUserSetting. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| InvalidWarningKeepDa ys | Integer | The number of days that an invalid risk is kept for. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeUserSetting &<Common request parameters>
```

Sample responses (JSON format)

```json
 "InvalidWarningKeepDays":90,
 "RequestId":"0A079FE2-0D1B-4A4D-A4EF-D02B5DDE12A7"
```

#### DescribeRiskWhiteList

You can call this operation to obtain the whitelist of risk items that are exempt from the baseline check.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRiskWhiteList. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| RiskName | String | No | The name of the risk item. This parameter supports fuzzy match. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| WhiteLists | Array | The risk item whitelist. For more information, see the following parameter descriptions. |
| Reason | String | The reason for adding the risk item to the whitelist. |
| RiskId | Long | The ID of the risk item. |

| RiskName | String | The name of the risk item. |
|---|---|---|

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeRiskWhiteList &RiskName=SSH logon baseline check &<Common request parameters>
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PageSize":20,
 "RequestId":"B452E97A-7DFA-44FC-915D-5D590A702846",
 "CurrentPage":1,
 "WhiteLists":[
   "RiskName":"SSH logon baseline check",
   "RiskId":1
```

`],`

```json
 "Count":1
```

#### DescribeStratety

You can call this operation to query the execution details of a specified baseline check policy.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeStratety. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Strategies | Array | The list of baseline check policies. For more information, see the following parameter descriptions. |

| CycleDays | Integer | The execution cycle of the policy. |
|---|---|---|
| CycleStartTime | Integer | The start time of policy execution. |
| EcsCount | Integer | The number of hosts to which the policy applies. |
| ExecStatus | Integer | The current execution status of the policy. Valid values: 1: indicates that the policy has been executed. 2: indicates that the policy is being executed. |
| Id | Integer | The ID of the policy. |
| Name | String | The name of the policy. |
| ProcessRate | Integer | The progress of policy execution. Unit: percentage. |
| RiskCount | Integer | The number of risk items contained in the policy. |
| ConfigTargets | Array | The asset group to which the policy applies. For more information, see the following parameter descriptions. |
| Flag | String | Indicates whether the policy applies to the specified asset group. Valid values: add: indicates the whitelist mode, that is, the policy applies to the asset group. del: indicates the blacklist mode, that is, the policy does not apply to the asset group. Note Generally, the blacklist mode is used for system default policies, and the whitelist mode is used for custom policies. |
| TargetType | String | The return value is fixed to groupId, indicating that the value of the Target parameter is the ID of the asset group. |
| Target | String | The asset group ID. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeStratety &<Common request parameters>
```

Sample responses (JSON format)

```json
        "requestId": "751BEDD8-A16F-49CE-A3C4-605849645D79",
    "Strategies": [
                "Name": "Threat Detection Service No. 12345",
                "RiskCount": 4,
                "CycleDays": 1,
                "CycleStartTime": 6,
                "Type": 2,
                "ProcessRate": 0,
                "ConfigTargets": [
                        "Flag": "add",
                        "Target": "5078483",
                        "TargetType": "groupId"
```

`],`

```json
                "Id": 36071,
                "ExecStatus": 1,
                "EcsCount": 2
```

`]`

#### DescribeStrategyExecDetail

You can call this operation to query the execution details of a baseline check policy.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeStrategyExecDetail. |
| StrategyId | Integer | No | The ID of the baseline check policy. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| EndTime | String | The time when the baseline check was complete. |
| FailCount | Integer | The number of servers that failed to pass the check. |

| FailedEcsList | Array | A list of servers that failed to pass the check. For more information, see the following parameter descriptions. |
|---|---|---|
| Ip | String | The IP address of the server. |
| InstanceName | String | The instance name of the server. |
| IntranetIp | String | The private IP address of the server. |
| Reason | String | The reason that causes the baseline check failure. |
| InProcessCount | Integer | The number of servers that are being checked. |
| percent | String | The baseline check progress in percentage. |
| Source | String | The baseline check mode: automatic or manual. |
| StartTime | String | The time when the baseline check started. |
| SuccessCount | Integer | The number of servers that have passed the check. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeStrategyExecDetail &StrategyId=1 &<Common request parameters>
```

Sample responses (JSON format)

```json
     "requestId": "751BEDD8-A16F-49CE-A3C4-605849645D79",
       "Source": "Schedule",
       "InProcessCount": 0,
       "SuccessCount": 1,
       "Percent": 100,
       "EndTime": "2018-04-08 12:15:20",
       "FailedEcsList": [],
       "StartTime": "2018-04-08 12:15:10",
       "FailCount": 0,
```

#### DescribeRiskType

You can call this operation to query all types of risks detected in baseline check and view the number of risks that have been detected by a baseline check policy or on the specified servers for a specific risk type.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeRiskType. |
| StrategyId | Long | No | The ID of the baseline check policy. |
| Uuids | String | No | The UUID of the server. Multiple UUIDs are separated with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The number of risk types. |
| RiskTypes | Array | A list of risk types. For more information, see the following parameter descriptions. |
| Alias | String | The name of the risk type. |
| TypeName | String | The code of the risk type. |
| WarnCount | String | The number of risks that have been detected. |
| SubTypes | Array | A list of sub-risk types. For more information, see the following parameter descriptions. |
| Alias | String | The name of the sub-risk type. |
| TypeName | String | The code of the sub-risk type. |
| WarnCount | String | The number of risks that have been detected. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeRiskType &StrategyId=10 &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"11D3993A-02B8-4FD9-9116-922BCDE53A80",
 "RiskTypes":[
   "TypeName":"system",
   "SubTypes":[
     "TypeName":"group_policy",
     "Alias":"Group policy",
     "WarnCount":0
```

`},`

```json
     "TypeName":"baseline",
     "Alias":"Baseline policy",
     "WarnCount":0
```

`},`

```json
     "TypeName":"register",
     "Alias":"Registry",
     "WarnCount":0
```

`],`

```json
   "Alias":"System",
   "WarnCount":0
```

`],`

```json
 "count": 1,
```

#### Describesummary

You can call this operation to query the risks detected in baseline check by risk type.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to Describesummary. |
| PageSize | Integer | No | The number of records displayed on a page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |

| Dealed | String | No | Indicates whether the risk has been handled. Valid values: Y: indicates that the risk has been handled. N: indicates that the risk has not been handled. |
|---|---|---|---|
| RiskLevels | String | No | The risk level. Separate multiple risk levels with commas (,). |
| RiskName | String | No | The name of the risk. Note Fuzzy match is supported. |
| StatusList | String | No | The status of the risk. Valid values: 1: indicates that the risk is pending. 2: indicates that the risk has been ignored. 3: indicates that the risk has been confirmed. 8: indicates that the risk has been marked as a false positive. 16: indicates that the risk is being handled. 32: indicates that the risk has been handled. You can specify multiple statuses and separate them with commas (,). |
| StrategyId | Long | No | The ID of the baseline check policy. |
| TypeNames | String | No | The type of the risk. Separate multiple risk types with commas (,). |
| SubTypeNames | String | No | The type of the sub-risk. Separate multiple sub-risk types with commas (,). |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of returned risk records. |
| CurrentPage | Integer | The current page number. |

| PageSize | Integer | The maximum number of records displayed on a page. |
|---|---|---|
| WarningSummarys | Array | A list of risks. For more information, see the following parameter descriptions. |
| LastFoundTime | String | The latest time when the risk was detected. |
| Level | String | The risk level. |
| PendingCount | Integer | The number of pending risks. |
| RiskDetail | String | The risk details. |
| RiskId | Long | The ID of the risk. |
| RiskName | String | The name of the risk. |
| TypeAlias | String | The type of the risk. |
| SubTypeAlias | String | The type of the sub-risk. |
| TotalCount | Integer | The total number of risks. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=Describesummary &CurrentPage=20 &Dealed=Y &PageSize=10 &StrategyId=1 &Uuid=2738e842-7d46-42f7-acb4-e6796b051ddc &<Common request parameters>
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "PageSize":20,
 "RequestId":"38AAFEEE-F52F-4B2E-9F28-FC4A35F8D432",
 "CurrentPage":1,
 "count": 1,
 "WarningSummarys":[
   "RiskId":1,
   "LastFoundTime":"2018-04-08 16:51:26",
   "RiskDetail":"The SSH logon security policy checks the following configurations: \
n1. Checks whether the logon port is the default port 22\n2 and whether the root acco unt is allowed\n3. Checks whether the SSH V1 protocol is used\n4. Checks whether the RSH protocol is used\n5. Checks whether authentication-based logon is performed\n Sol ution: \n Edit /etc/ssh/sshd_config\n1. Port (not 22)\n2. PermitRootLogin (no)\n3. Pr otocol (2)\n4. IgnoreRhosts (yes)\n5. e) HostbasedAuthentication (no)
   "Level":"low",
   "TypeAlias":"System",
   "SubTypeAlias":"Baseline check policy",
   "RiskName":"SSH logon baseline check"
```

`]`

#### ListBaselineCheckWhiteRecord

Retrieves the details of baseline check whitelist records.

**Request headers**

This operation uses common request headers and does not have special request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | No | 219.133.XX.XX | The source IP address. |
| Lang | Strin g | Query | No | en | The language of the request and response. The default value is zh. Valid values: zh: Chinese. en: English. |
| Source | Strin g | Query | No | console batch _ | The source from which the task was added. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| CheckIte mFuzzy | Strin g | Query | No | redis | A fuzzy match for the name of the check item. |
| CheckIds | Array | Query | No | 21313 | The ID of the check item. Note To obtain the check item ID, call the DescribeRiskType operation. |
| RecordIds | Array | Query | No | ["rec1001", "rec1002", "rec1003"] | A list of IDs of whitelist records. |
| CurrentPa ge | Integ er | Query | No | 4 | The number of the page to return for a paged query. |
| PageSize | Integ er | Query | No | 10 | The number of entries to return on each page for a paged query. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | Array | - | A list of server information. |
| -RecordId | Long | 20201105144514 | The record ID. |
| -CheckId | Long | 696 | The ID of the check item. |
| -TargetType | String | RD-Account | The mode used to select the assets on which the rule takes effect. Valid values: uuid: selects individual assets. groupId: The ID of the server group for adding servers. global: selects all assets. |
| -Target | String | foo2,foo3 | The ID of the target. This is currently the group ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Reason | String | Started | The reason for adding the item to the whitelist. |
| -Source | String | Local | The data source. Valid values: API: API detection. OSS: OSS detection. |
| -Lang | String | zh | The language. |
| -CheckItem | String | CHECK CONN SRC _ _ | The check item. |
| -CheckType | String | code scan _ | The type of the check item. Valid values: hc.check.type.identity auth: Identity _ authentication hc.check.type.access control: Access _ control hc.check.type.network service: Network _ service. hc.check.type.service conf: Service _ configuration check. hc.check.type.file rights: Checks file _ permissions. hc.check.type.security audit: Security _ audit. hc.check.type.attack defense: Attack _ and defense. hc.check.type.others: Other types. |
| - CheckTypeDis Name | String | Data Integrity | The display name of the check item type. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| PageInfo | Struct | - | The pagination information. |
| -CurrentPage | Integer | 1 | The number of the returned page. |
| -PageSize | Integer | 10 | The maximum number of entries returned on each page. |
| -TotalCount | Integer | 10 | The total number of entries. |

| erver Guard Adv veloper Guide·AP | anced Edition D I documentati |   | Alibaba Cloud Security-Server G ard Advanced Editio |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Count | Integer | 1 | The number of entries returned on the current page. |

The following is a sample response in `JSON` format.

```json
 "PageInfo":{
  "TotalCount":10,
  "PageSize":10,
  "CurrentPage":1,
  "Count":1
```

`},`

```json
 "RequestId":"",
 "List":[
   "Target":"foo2,foo3",
   "CheckId":696,
   "CheckItem":"CHECK_CONN_SRC",
   "CheckTypeDisName":"Data Integrity",
   "CheckType":"code_scan",
   "TargetType":"RD-Account",
   "Lang":"zh",
   "RecordId":20201105144514,
   "Reason":"Started",
   "Source":"Local"
```

`]`

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | ServerError | ServerError | ServerError |
| 403 | NoPermission | NoPermission | The caller does not have the required permissions. |

### Unusual logon detection

#### DescribeBaseConfigs

You can call this operation to query the logon security settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBaseConfigs. |
| Type | String | Yes | The type of the logon security configuration record. Valid values: login common location: indicates _ _ an approved logon location. login common ip: indicates an _ _ approved logon IP address. login common time: indicates an _ _ approved logon time period. login common account: indicates _ _ an approved logon account. |
| Target | String | No | The specified server. Note You must specify this parameter to query the logon security settings of a specified server. For more information about the format, see the sample request. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of the returned records. |
| BaseConfigs | Array | The logon security settings. For more information, see the following parameter descriptions. |
| Account | String | The approved logon account. |

| EndTime | String | The end time of the approved logon time period. |
|---|---|---|
| Ip | String | The approved logon IP address. |
| Location | String | The approved logon location. |
| StartTime | String | The start time of the approved logon time period. |
| TotalCount | Integer | The total number of servers. |
| UuidCount | Integer | The number of servers to which the specified configuration record applies. |
| TargetList | Array | The information about servers to which the specified configuration record applies. For more information, see the following parameter descriptions. |
| TargetType | String | The type of the Target parameter value. Valid values: groupId: indicates an asset group ID. uuid: indicates a server UUID. |
| Target | String | The asset group ID or server UUID. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeBaseConfigs &CurrentPage=1 &PageSize=20 &Target=[{"targetType":"uuid","target":"6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac"}] &Type=login_common_location &<Common request parameters>
```

Sample responses (JSON format)

```json
 "BaseConfigs": [{
  "totalCount": 9,
  "location": "United States",
  "uuidCount": 1,
  "targetList": [{
   "target": "6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac",
   "targetType": "uuid"
```

`}]`

```json
 }],
 "TotalCount": 1,
 "PageSize": 5,
 "RequestId": "485ABE58-4E27-4416-997C-F8F3B8748EB6",
 "CurrentPage": 1
```

#### DescribeSwitchConfigs

You can call this operation to query the logon security configuration records in the logon security settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSwitchConfigs. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| ConfigList | Array | The statuses of the logon security configuration items. For more information, see the following parameter descriptions. |

| Item | String | The logon security configuration items. Valid values: login common location: indicates an approved _ _ logon location. login common ip: indicates an approved logon _ _ IP address. login common time: indicates an approved _ _ logon time range. login common account: indicates an approved _ _ logon account. |
|---|---|---|
| Status | Integer | The status of the configuration item. Valid values: 1: indicates enabled. 0: indicates disabled. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeSwitchConfigs &<Common request parameters>
```

Sample responses (JSON format)

```json
 "Count":3,
 "RequestId":"3F2C126D-870B-4AE4-8604-58BDECF873F4",
 "ConfigList":[
   "Status":1,
   "Item":"login_common_ip"
```

`},`

```json
   "Status":0,
   "Item":"login_common_account"
```

`},`

```json
   "Status":0,"Item":"login_common_time"
```

`]`

#### DescribeConfigTarget

You can call this operation to query the information about servers to which a specified logon security configuration record applies.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeConfigTarget. |
| Type | String | Yes | The logon security configuration record used to identify a valid logon to a server. Valid values: login common location: indicates _ _ an approved logon location. login common ip: indicates an _ _ approved logon IP address. login common time: indicates an _ _ approved logon time range. login common account: indicates _ _ an approved logon account. |
| Target | String | No | The specified server. Note You need to specify this parameter to query the logon security configuration records of a specified server. For more information about the format, see the sample request. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| TargetList | Array | The information about server to which the specified configuration record applies. For more information, see the following parameter descriptions. |
| TargetType | String | The type of the Target parameter value. Valid values: groupId: indicates an asset group ID. uuid: indicates a server UUID. |
| Target | String | The asset group ID or server UUID. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeConfigTarget &Config={"uuidCount":1,"location":"Ganzhou"} &Target=[{"targetType":"uuid","target":"6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac"}] &Type=login_common_location &<Common request parameters>
```

Sample responses (JSON format)

```json
  "TargetList": [{
   "Target": "inet-e53455ec-a134-4d46-9ff5-c4f3a5fe0f02",
   "TargetType": "uuid"
  }, {
   "Target": "inet-25f4ef74-29c7-49fd-85cc-b4543a2489a8",
   "TargetType": "uuid"
 "Count": 2,
 "RequestId": "B8064EA4-9472-4D03-B7D1-6684DB5CD0BE",
```

#### ModifyBaseConfig

You can call this operation to modify logon security settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyBaseConfig. |
| Type | String | Yes | The type of the logon security settings. Valid values: login common location: indicates _ _ approved logon locations. login common ip: indicates _ _ approved logon IP addresses. login common time: indicates _ _ approved logon time periods. login common account: indicates _ _ approved logon accounts. |
| Target | String | No | The target server. Note You must set this parameter when you need to query the logon security settings for a server. For more information about the format, see the following sample request. |

| Config | String |   | No | The logon security settings. The formats for all the settings are as follows: Approved logon locations: {"location":"Ganzhou City"} Approved logon IP addresses: {"ip":"x.x.x.x"} Approved logon time periods: {"startTime":"16:18","endTime" :"16:18"} Approved logon accounts: {"account":"dbaadmin"} |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   |   | {"startTime":"16:18","endTime" |   |
|   |   |   |   | :"16:18"} |   |   |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyBaseConfig &Config={"startTime":"16:18","endTime":"16:18"} &Target=[{"targetType":"uuid","target":"0c797eb1-e6b9-4b5a-8917a7e6cbbb4b2e","flag":"add"},{"targetType":"uuid","target":"1759b0ea-6dd7-438b-b60d-c9 0179bd9ebc","flag":"del"}] &Type=login_common_location &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"BB8F5902-BD50-49AB-B124-18E9CA92BB99"
```

#### DeleteBaseConfig

You can call this operation to delete a logon security setting, such as an approved logon location or IP address.

| Parameter | Type | Required | Description |
|---|---|---|---|

| Action | String |   | Yes | The operation that you want to perform. Set this parameter to DeleteBaseConfig. |   |   |
|---|---|---|---|---|---|---|
| Config | String |   | Yes | The logon security setting. The formats of the logon security settings and examples are as follows: Approved logon location: {"location":"Ganzhou City"} Approved logon IP address: {"ip":" x.x.x.x"} Approved logon time range: {"startTime":"16:18","endTime" :"16:18"} Approved logon account: {"account":"dbaa****"} |   |   |
|   |   |   |   |   | {"startTime":"16:18","endTime" |   |
|   |   |   |   | :"16:18"} |   |   |
| Type | String |   | Yes | The type of the logon security setting. Valid values: login common location: indicates _ _ an approved logon location. login common ip: indicates an _ _ approved logon IP address. login common time: indicates an _ _ approved logon time range. login common account: indicates _ _ an approved logon account. |   |   |
| Target | String |   | No | The target server. Note You must set this parameter if you want to delete a logon security setting for a server. For more information about the format, see the following sample request. |   |   |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DeleteBaseConfig &Config={"location":"Ganzhou City"} &Target=[{"targetType":"uuid","target":"6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac"}] &Type=login_common_location &<Common request parameters>
```

Sample response (JSON format)

```json
    "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
```

#### ModifySwitchConfig

You can call this operation to modify the setting about whether to enable a logon security configuration record to identify a valid logon to a server in the logon security settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifySwitchConfig. |
| Item | String | Yes | The logon security configuration items. Valid values: login common location: indicates _ _ an approved logon location. login common ip: indicates an _ _ approved logon IP address. login common time: indicates an _ _ approved logon time range. login common account: indicates _ _ an approved logon account. |
| Status | Integer | Yes | The status of the logon security configuration switch. Valid values: 1: indicates enabled. 0: indicates disabled. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |

| ConfigList | Array | The status of the logon security configuration switch. For more information, see the following parameter descriptions. |
|---|---|---|
| Item | String | The logon security configuration items. Valid values: login common location: indicates an approved _ _ logon location. login common ip: indicates an approved logon _ _ IP address. login common time: indicates an approved _ _ logon time range. login common account: indicates an approved _ _ logon account. |
| Status | Integer | The status of the logon security configuration switch. Valid values: 1: indicates enabled. 0: indicates disabled. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifySwitchConfig &Item=login_common_location &Status=1 &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"3F2C126D-870B-4AE4-8604-58BDECF873F4"
```

### Webshell detection

#### DescribeCategoryCount

You can call this operation to query the number of webshells detected by Server Guard.

| Name | Type | Required | Description |
|---|---|---|---|

| Action | String | Yes | The operation that you want to perform. Set the value to DescribeCategoryCount. |
|---|---|---|---|

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Webshell | Integer | The number of webshells. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeCategoryCount &<Common request parameters>
```

Sample responses (JSON format)

```json
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
    "Webshell": 2
```

#### DescribeWebshell

You can call this operation to query records of webshell files that have been detected by Server Guard, including the detection time and webshell file path.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeWebshell. |
| GroupId | Integer | No | The ID of the asset group. |
| Mark | String | No | The IP address or instance name of the server. |
| Tag | Integer | No | The server tag ID. |

| Dealed | String | No | The status of the webshell event. Valid values: n: indicates that the event is pending. y: indicates that the event has been handled. |
|---|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| WebshellList | Array | The webshell events. For more information, see the following descriptions. |
| Os | String | The operating system of the server. |
| InstanceName | String | The instance name of the server. |
| GroupId | Long | The ID of the asset group. |
| Ip | String | The IP address of the server. Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |
| Uuid | String | The universally unique identifier (UUID) of the server. |
| FoundTime | String | The time when the webshell file was detected. |
| InstanceId | String | The instance ID of the server. |
| TrojanType | String | The type of the webshell file. |
| FirstFoundTime | String | The time when the webshell file was detected for the first time. |
| TrojanSize | Long | The size of the webshell file. |
| Domain | String | The domain name associated with the server. |
| TrojanPath | String | The path of the webshell file. |
| Region | String | The region where the server resides. |

| Status | Integer | The status of the webshell event. Valid values: 1: indicates that the event is pending. 2: indicates that the event has been ignored. 3: indicates that the event has been confirmed. 8: indicates that the event has been labeled as a false positive. 16: indicates that the event is being handled. 32: indicates that the event has been handled. |
|---|---|---|

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeWebshell &Dealed=n &GroupId=1 &Remark=xx.xx.xx.xx &Tag=11 &<Common request parameters>
```

Sample response (JSON format)

```json
    "WebshellList": [{
        "Uuid": "aa46dbe9-d35d-4b77-a4d9-10bc6b1b****",
        "FoundTime": "2018-02-27 03:23:18",
        "Ip": "xx.xx.xx.xx",
        "FirstFoundTime": "2017-12-24 03:36:03",
        "Domain": "",
        "TrojanType": "Webshell",
        "InstanceId": "i-bp15xtqydmbujgep****",
        "TrojanPath": "c:/zhb/wamp/wamp/www/My.php",
        "GroupId": 3259405,
        "Os": "windows",
        "Status": 1,
        "Region": "cn-hangzhou-dg-a01",
        "TrojanSize": 0,
        "InstanceName": "win08****"
    }, {
        "Uuid": "aa46dbe9-d35d-4b77-a4d9-10bc6b1bb610",
        "FoundTime": "2017-12-25 03:53:22",
        "Ip": "x.x.x.x",
        "FirstFoundTime": "2017-12-24 03:36:01",
        "Domain": "",
        "TrojanType": "Webshell",
        "InstanceId": "i-bp15xtqydmbujgepdbev",
        "TrojanPath": "c:/zhb/wamp/../wamp/wamp/www/abc/My.php",
        "GroupId": 3259405,
        "Os": "windows",
        "Status": 9,
        "Region": "cn-hangzhou-dg-a01",
        "TrojanSize": 0,
        "InstanceName": "win08-zhb"
    }],
    "RequestId": "E4B254AE-5CB1-4810-8B51-A08DF5697F25"
```

#### DescribeQuaraFile

You can call this operation to obtain the list of quarantined files.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeQuaraFile. |

| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query result. Default value: 20. |
|---|---|---|---|
| CurrentPage | Integer | No | The current page number. Default value: 1. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| QuaraFiles | Array | The list of quarantined files. For more information, see the following parameter descriptions. |
| EventName | String | The name of the unusual event. |
| EventType | String | The type of the unusual event. |
| FileStatus | String | The status of the quarantined file. Valid values: quaraFailed("0"): indicates that the file failed to be quarantined. rollbackFailed("1"): indicates that the file failed to be rolled back to a previous version. quaraDone("2"): indicates that the file has been quarantined. rollbackDone("3"): indicates that the file has been rolled back to a previous version. quaraing("4"): indicates that the file is being quarantined. rollbacking("5"): indicates that the file is being rolled back to a previous version. |
| Md5 | String | The MD5 value of the file. |
| Online | Boolean | Indicates whether the Server Guard agent on the server is online. |
| Path | String | The file path. |
| Tag | String | The unique identifier of the unusual event. |
| Uuid | String | The UUID of the server. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeQuaraFile &<Common request parameters>
```

Sample responses (JSON format)

```json
    "TotalCount":1,
    "PageSize":20,
    "RequestId":"0C7FAD74-83FA-4671-9250-A5F2A64F437A",
    "CurrentPage":1,
    "QuaraFiles":[
            "Path":"/bin/ping",
            "Uuid":"9b0c4d55-2f1f-4766-a90a-2c9d8a0b7642",
            "FileStatus":"quaraDone",
            "EventType":"Parent class of cloud scanning events (test ping)",
            "EventName":"Sub-class of cloud scanning events (test ping)",
            "Tag":"1d791175ad0bffd973b039248d6086e0",
            "Online":false,
            "Md5":"1421d9ad2b0031483f396154d48161f1"
```

`]`

#### RollbackQuaraFile

You can call this operation to restore a specified quarantined file.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to RollbackQuaraFile. |
| EventName | String | No | The name of the unusual event. |
| EventType | String | No | The type of the unusual event. |
| Tag | String | No | The GUID of the unusual event. |
| Uuid | String | No | The UUID of the server. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=RollbackQuaraFile &EventName=DDoS trojan &EventType=Malicious process &Tag=a50f96f958fbd59f68e4bca4d90679d6 &Uuid=00f11fcb-1a9a-4fd5-a48a-e0e5bd12a6a4 &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"0C7FAD74-83FA-4671-9250-A5F2A64F437A",
```

#### DescribeWebPath

You can call this operation to query the Web directories defined in webshell settings.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeWebPath. |
| PageSize | Integer | No | The number of records to return on each page. Default value: 20. |
| CurrentPage | Integer | No | The number of the page to return. Default value: 1. |
| Type | String | No | The type of the settings. Set this parameter to web path to _ specify the Web directory settings. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| Count | Integer | The number of Web directories. |
| ConfigList | Array | The Web directories. For more information, see the following descriptions. |
| WebPath | String | The path of the Web directory. |
| TargetList | Array | The servers that the Web directory has been applied to. For more information, see the following descriptions. |
| TargetType | String | This parameter always returns a value of uuid, which means that the Target parameter returns the universally unique identifier (UUID) of the server. |
| Target | String | The UUID of the server. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeWebPath &<Common request parameters>
```

Sample response (JSON format)

```json
 "TotalCount":1,
 "PageSize":5,
 "RequestId":"7B6AD7C9-0F8D-4126-B8AA-6DC308B0B534",
 "CurrentPage":1,
 "Count":1,
 "ConfigList":[
   "TargetList":[
     "Target":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
     "TargetType":"uuid"
```

`],`

```json
   "WebPath":"/usr/local/tomcat/webroot18"
```

`]`

#### ModifyWebPath

You can call this operation to modify the Web directory in webshell settings.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyWebPath. |
| Type | String | No | The configuration type. Set the value to web path, indicating _ the web directory configuration. |
| Config | String | No | The Web directory configuration, in JSON format. For more information, see the sample request. |
| Target | String | No | The list of target servers to which the Web directory configuration applies, in JSON format. For more information, see the sample request. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=ModifyWebPath &Type=web_path &Config={"webPath":"/test"} &Target={"targetType":"uuid","target":"0c797eb1-e6b9-4b5a-8917a7e6cbbb4b2e","flag":"add"} &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"7B6AD7C9-0F8D-4126-B8AA-6DC308B0B534"
```

#### OperateTrojan

You can call this operation to handle detected webshells.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to OperateTrojan. |
| Info | String | No | The webshell information, in JSON format. For more information, see the sample request. |
| OperateType | String | No | The type of the operation. Valid values: isolate: indicates an operation to quarantine the file. trust: indicates an operation to trust the file. untrust: indicates an operation to cancel trusting the file. restore: indicates an operation to restore the file. |
| Type | Integer | No | The type of the trojan. Set the value to 1. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| FailedCount | Integer | The number of failed operations. |
| SuccessCount | Integer | The number of successful operations. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=OperateTrojan &Info=[{"uuid":"97988c2b-de9d-4159-90ab- 7cc73561c64c","filePath":"/home/test/Z02.php","webshellId":""}] &OperateType=trust &Type=1 &<Common request parameters>
```

Sample responses (JSON format)

```json
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
    "FailedCount": 0,
    "SuccessCount": 1
```

### Exception detection on hosts

#### DescribeSuspEventTypes

You can call this operation to query the unusual event types.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSuspEventTypes. |

| Name | Type | Description |
|---|---|---|

| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
|---|---|---|
| TotalCount | Integer | The total number of returned records. |
| EventTypes | Array | The list of unusual event types. For more information, see the following parameter descriptions. |
| AliseEventType | String | The name of the unusual event type. |
| EventType | String | The identifier of the unusual event type. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeSuspEventTypes &<Common request parameters>
```

Sample responses (JSON format)

```json
 "TotalCount":1,
 "RequestId":"66BE7091-BC00-4943-8A0D-B3DCE90AD7B5",
 "EventTypes":[
   "EventType":"Suspicious process",
   "AliseEventType":"Suspicious process"
```

`]`

#### DescribeSuspTrendStatistics

You can call this operation to query the chart data on different types of unusual server events on each day.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeSuspTrendStatistics. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Interval | Integer | The time length of the the time frame specified for query. |
| StartTime | Integer | The start time of the time frame specified for query. |
| SuspiciousItems | List | The statistics on numbers of different types of suspicious events. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeSuspTrendStatistics &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"66BE7091-BC00-4943-8A0D-B3DCE90AD7B5",
 "Start":-28800000,
 "Interval":86400000,
 "SuspiciousItems":[ ]
```

#### DescribeSuspiciousExportInfo

You can call this operation to query an unusual event export task.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeSuspiciousExportInfo. |
| ExportId | Long | No | The ID of the export task. |

| Parameter | Type | Description |
|---|---|---|
| RequestId | String | The ID of the request. |

| CurrentCount | Integer | The number of records that have been exported. |
|---|---|---|
| ExportStatus | String | The status of the export task. Valid values: init: indicates that the export task is being initialized. pending: indicates that the export task is pending. exporting: indicates that the export task is being executed. success: indicates that the export task has been completed. fail: indicates that the export task has failed. |
| Message | String | The status description or failure information of the export task. |
| FileName | String | The name of the exported file. |
| Id | Integer | The ID of the export task. |
| GmtCreate | Long | The time when the export task was created. |
| Link | String | The download link of the exported file. |
| Progress | Integer | The export progress. |
| TotalCount | Integer | The total number of records that have been exported. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample request

```
https://aegis.[ RegionId].example.com/?Action=DescribeSuspiciousExportInfo &ExportId=1 &<Common request parameters>
```

Sample response (JSON format)

```json
 "TotalCount":30,
 "GmtCreate":1518071546000,
 "Progress":100,
 "Message":"success",
 "RequestId":"654A6FD8-B55D-4D6B-AAFF-4122503D108B",
 "FileName":"suspicious_20180208",
 "ExportStatus":"success",
 "CurrentCount":30,
 "Id":11,
 "Link":"http://suspicious-export.oss-cn-
shanghai.example.com/export/suspicious_20180208_1518071576098.zip? Expires=1518075176&OSSAccessKeyId=<yourAccessKeyId>&Signature=xxxx%xxxx%3D"
```

#### OperateSuspiciousEvent

You can call this operation to handle detected unusual events.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to OperateSuspiciousEvent. |
| Data | String | No | The unusual event to be handled, in JSON format. For more information, see the sample request. |
| OperateType | String | No | The type of the operation. Valid values: deal: indicates an operation to handle the unusual event. confirm: indicates an operation to mark the unusual event as handled. mark misinformation: indicates an _ operation to mark the unusual event as false positive. unmark misinformation: indicates _ an operation to remove the false positive mark of the unusual event. ignore: indicates an operation to ignore the unusual event. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=OperateSuspiciousEvent &OperateType=ignore &Data={"uuid":"97988c2b-de9d-4159-90ab- 7cc73561c64c","tag":"f87eb0ee5934f6f65343ec601ce71c2f","eventType":"Malicious process es (malware checking)","eventName":"DDoS Trojan},{"uuid":"97988c2b-de9d-4159-90ab-7cc 73561c64c","tag":"95347a77b8c0d6dae99a23ab69aa90f4","eventType":"Malicious processes (malware checking)","eventName":"GateDDoS Trojan"} &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"654A6FD8-B55D-4D6B-AAFF-4122503D108B"
```

#### OperateLoginLog

You can call this operation to label a detected unusual logon event as handled.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to OperateLoginLog. |
| Ids | String | Yes | The ID of the unusual logon log. Separate multiple log IDs with commas (,). |
| OperateType | String | Yes | The type of the operation. Set the value to confirm, indicating that the event has been handled. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=OperateLoginLog &Ids=2006434 &OperateType=confirm &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"BE391ABB-6B7C-4C41-9F6C-862C1DEE3905"
```

#### DescribeVirusInfo

You can call this operation to upload the MD5 values of files and use Alibaba Cloud Antivirus to determine whether the files are malicious programs.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeVirusInfo. |
| Md5 | String | Yes | The MD5 value of the file. |
| Lang | String | No | The language attribute of the file, such as zh. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Data | Boolean | Indicates whether the file is malicious. Valid values: True: Indicates that the file is malicious. False: Indicates that the file is not malicious. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].aliyuncs.com/?Action= DescribeVirusInfo &Md5=6f6628d923f9018b28acc5f905e03244 &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId": "A2423F39-3272-4491-804E-D0EBDE3E894D",
 "Data": true
```

#### CreateSuspiciousExport

You can call this operation to export the information about unusual events on servers based on search conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateSuspiciousExport. |
| Dealed | String | No | Indicates whether the unusual event has been handled. Valid values: Y: indicates that the event has been handled. N: indicates that the event has not been handled. |
| EventNameRema rk | String | No | The name of the event. Fuzzy matching is supported. |
| EventType | String | No | The name of the event type. Valid values: Unusual logon Suspicious process Suspicious account Sensitive file tampering Suspicious network connection Unusual event Suspicious file Malicious process |
| GroupId | String | No | The ID of the asset group. |

| Level | String | No | The risk level of the event. Valid values: Critical: indicates a critical-risk event. Important: indicates an important- risk event. Moderate: indicates a moderate-risk event. low: indicates a low-risk event. You can specify multiple event levels and separate them with commas (,). |
|---|---|---|---|
| Remark | String | No | The name or IP address of the server. Fuzzy matching is supported. |
| StatusList | String | No | The handling status of the event. Valid values: 1: indicates that the event is to be handled. 2: indicates that the event has been ignored. 3: indicates that the event has been confirmed. 8: indicates that the event has been labeled as a false positive. 16: indicates that the event is being handled. 32: indicates that the event has been handled. You can specify multiple statuses and separate them with commas (,). |
| Tag | String | No | The tag of the server. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| FileName | String | The name of the exported file. |
| Id | Long | The ID of the export task. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=CreateSuspiciousExport &Remark=23 &EventType=Suspicious process &Level=serious,high,medium,low &Dealed=n &<Common request parameters>
```

Sample responses (JSON format)

```json
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
    "FileName": "suspicious_20180408",
    "Id": 387
```

#### CreateFileProtectRule

User logon

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | No | 219.133.XX.XX | The source IP address of the request. |
| Lang | Strin g | Query | No | en | The language of the content in the request and response. Default value: zh. zh: Chinese. en: English. |
| Id | Long | Query | No | 245 | The ID of the baseline policy. |
| RuleName | Strin g | Query | Yes | Rule**** | The name of the system rule. |
| ProcPaths | Repe atList | Query | Yes | D:\Games\Launcher.exe | A list of process paths to monitor. Wildcards are supported. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| FilePaths | Repe atList | Query | Yes | /static/test.png | A list of file paths to monitor. Wildcards are supported. |
| FileOps | Repe atList | Query | Yes | EXISTS | The list of file operations. |
| RuleActio n | Strin g | Query | Yes | 1 | The action of the rule. Valid values: close, alert, and drop. |
| AlertLevel | Integ er | Query | No | 0 | The alert notification level. Valid values: 0: No alert 1: Notice 2: Suspicious 3: Important |
| SwitchId | Strin g | Query | No | vs-abcdef**** | The ID of the switch that corresponds to the rule. |
| Status | Integ er | Query | No | 1 | The status of the quarantined file to query. Valid values: quaraFailed: Fencing failed quaraDone: Fencing successful Quarantining: The process of isolation. rollbackFailed: Revoking fencing failed rollbackDone: Revoking fencing successful rollbacking: Revoking fencing in progress. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

| erver Guard Adv veloper Guide·AP n | anced Edition D I documentati |   | Alibaba Cloud Security-Server G ard Advanced Editio |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RuleId | Long | 123 | The ID of the rule. |

Request example

```
http(s)://[Endpoint]/?Action=CreateFileProtectRule &RuleName=Rule**** &ProcPaths=D:\Games\Launcher.exe &FilePaths=/static/test.png &FileOps=EXISTS &RuleAction=1 &<Common request parameters>
```

Response example `JSON` format

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "RuleId":123
```

#### UpdateFileProtectRule

Modifies a core file protection rule.

**Authorization**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- aegis:UpdateFileProtectRule | Write | acs:yundun-aegis:*: {#accountId}:* |

**Traffic shaping**

The request frequency for a single user is limited to 10 queries per second (QPS). The request frequency for this API is limited to 100 QPS.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | No | 219.133.XX.XX | The source IP address of the request. |

| libaba Cloud rd Advanced | Security- Edition | Server Gu |   | Serve evelo | r Guard Advanced Edition D per Guide·API documentat o |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | Description |
| Lang | Strin g | Query | No | zh | The language of the request and response. The default value is zh. zh: Chinese en: English |
| Id | Long | Query | No | 1062 | The ID of the rule. |
| RuleName | Strin g | Query | Yes | test-rule-1 | The name of the rule. |
| ProcPaths | Repe atList | Query | Yes | ["/usr/local/*","/tmp/*"] | The paths of the processes to monitor. |
| FilePaths | Repe atList | Query | Yes | ["/usr/local/*","/tmp/*"] | The file paths to monitor. Wildcards are supported. |
| FileOps | Repe atList | Query | Yes | ["WRITE"] | The file operations to monitor. Valid values: READ: read WRITE: write EXECUTE: execute RENAME: rename CHMOD: modify permissions |
| RuleActio n | Strin g | Query | No | pass | The action of the rule on the client. Valid values: pass: The request is allowed. alert: An alert is generated. |
| SwitchId | Strin g | Query | No | None | This parameter is deprecated. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AlertLevel | Integ er | Query | No | 0 | The level of the alert notification. Valid values: 0: No alert 1: Informational 2: Suspicious 3: Important |
| Status | Integ er | Query | No | 0 | You can set the rule status. 0: disabled 1: enabled |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. Alibaba Cloud generates a unique ID for each request. You can use this ID to troubleshoot issues. |

Request example

```
https://[Endpoint]/?Action=UpdateFileProtectRule&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&Lang=en&Id=1062&RuleName=test-rule- 1&ProcPaths.1=/usr/local/*&FilePaths.1=/usr/local/*&FileOps.1=WRITE&RuleAction=pass&Switc d=RISK-COMMAND-AUDIT-RULE-SWITCH-TYPE_200****&AlertLevel=0&Status=
```

Sample success response `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

`XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <UpdateFileProtectRuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
</UpdateFileProtectRuleResponse>
```

#### ListFileProtectEventExport

Call the ListFileProtectEventExport operation to query alert events for core file monitoring.

**Authorization information**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- aegis:ListFileProtectEventExpor t | Read | acs:yundun-aegis:*: {#accountId}:* |

**Traffic shaping**

Call frequency for a single user: 10 QPS. Call frequency for this API operation: 100 QPS.

**Request header**

This operation uses only common request headers. For more information, see the common request parameters document.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | No | 219.133.XX.XX | The source IP address. The default value is 196.0.0.0. |
| Lang | Strin g | Query | No | zh | The language of the request and response. The default value is zh. Valid values: zh: Chinese. en: English. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| EventDTOList | Array | [ { "LatestTimeStr":"1 694576692000", "Status":"0,1,2", "FilePath":"/etc/pa m.d/su", "FirstTime":169457 6692000, "ResourceSetName ":"test", "GmtModified":"16 7118088****", "CmdLine":" [\"touch\",\"/test/aa aa\"]", "OrgName":"test", "Operation":"READ ", "IntranetIp":"192.1 68.176.75", "Remark":"test", "InstanceName":"c a cpm ****", _ _ "OrgId":"12", "ProcPermission":"r wxr-xr-x", "Uuid":"c9107c04- 942f-40c1-981a- f1c1***", "InternetIp":"43.11 6.5.5", "LatestTime":1694 576692000, "FirstTimeStr":"169 4576692000", "AlertLevel":1, "ProcessId":"52636 ", "ProcPath":" /usr/bin/sshpass", "ResourceSetId":"1 2", "HandleTime":1694 576692000, "RuleName":"test- rule-1" } ] | The list of alerts. |
| -AlertLevel | Integer | 1 | The alert notification level. Valid values: 0: No alert 1: Reminder 2: Suspicious 3: Important |
| -Uuid | String | c9107c04-942f- 40c1-981a-f1c1*** | The UUID of the instance. |
| -RuleName | String | test-rule-1 | The name of the rule. |

| libaba Cloud Sec | urity-Server Gu |   | Server Guard Advanced Edition D eveloper Guide·API documentat |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -FirstTime | Long | 1694576692000 | The time when the event first occurred. |
| -FirstTimeStr | String | 1694576692000 | The time when the event first occurred. |
| -LatestTime | Long | 1694576692000 | The time when the event last occurred. |
| -LatestTimeStr | String | 1694576692000 | The time when the event last occurred. |
| -Status | Integer | 0,1,2 | The status of the event. Valid values: 0: Unhandled 1: Handled 2: Whitelisted 3: Ignored |
| -ProcPath | String | /usr/bin/sshpass | The path of the process. |
| -FilePath | String | /etc/pam.d/su | The path of the file that the process accessed. |
| -CmdLine | String | ["touch","/test/aaa a"] | The command line of the event. |
| - ProcPermissio n | String | rwxr-xr-x | The permissions of the process. |
| -Operation | String | READ | The type of operation on the file. Valid values: DELETE: Deletes the file. WRITE: Writes to the file. READ: Reads the file. RENAME: Renames the file. CHOWN: Sets the owner and group of the file. |
| - InstanceName | String | ca cpm **** _ _ | The name of the server. |
| -IntranetIp | String | 192.168.176.75 | The internal IP address. |
| -InternetIp | String | 43.116.5.5 | The public IP address. |
| -GmtModified | Long | 167118088**** | The time of the last modification. |

| S e o | erver Guard Adv veloper Guide·AP n | anced Edition D I documentati |   | Alibaba Cloud Security-Server G ard Advanced Editio | u n |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Remark | String | test | The remarks. |
| -HandleTime | Long | 1694576692000 | The time when the event was handled. |
| -ProcessId | String | 52636 | The ID of the process that is associated with the event. |
| -OrgId | String | 12 | The ID of the organization. |
| - ResourceSetId | String | 12 | The ID of the resource set. |
| -OrgName | String | test | The name of the organization. |
| - ResourceSetN ame | String | test | The name of the resource set. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The unique ID of the request. This ID is used to troubleshoot issues. |
| PageInfo | Struct | { "TotalCount":2, "PageSize":20, "CurrentPage":1, "Count":2 } | The paging information. |
| -Count | Integer | 2 | The number of entries returned on the current page. |
| -PageSize | Integer | 20 | The number of entries to return on each page. |
| -TotalCount | Integer | 2 | Total data record count on servers exposed to the Internet |
| -CurrentPage | Integer | 1 | The page number of the returned page. |

Sample request

```
https://[Endpoint]/?Action=ListFileProtectEventExport&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&Lang=zh
```

Sample response `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "EventDTOList":[
            "LatestTimeStr":"1694576692000",
            "Status":"0,1,2",
            "FilePath":"/etc/pam.d/su",
            "FirstTime":1694576692000,
            "ResourceSetName":"test",
            "GmtModified":"167118088****",
            "CmdLine":"[\"touch\",\"/test/aaaa\"]",
            "OrgName":"test",
            "Operation":"READ",
            "IntranetIp":"192.168.176.75",
            "Remark":"test",
            "InstanceName":"ca_cpm_****",
            "OrgId":"12",
            "ProcPermission":"rwxr-xr-x",
            "Uuid":"c9107c04-942f-40c1-981a-f1c1***",
            "InternetIp":"43.116.5.5",
            "LatestTime":1694576692000,
            "FirstTimeStr":"1694576692000",
            "AlertLevel":1,
            "ProcessId":"52636",
            "ProcPath":" /usr/bin/sshpass",
            "ResourceSetId":"12",
            "HandleTime":1694576692000,
            "RuleName":"test-rule-1"
```

`],`

```json
    "PageInfo":{
        "TotalCount":2,
        "PageSize":20,
        "CurrentPage":1,
        "Count":2
```

`XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ListFileProtectEventExportResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <EventDTOList>
        <AlertLevel>1</AlertLevel>
        <Uuid>c9107c04-942f-40c1-981a-f1c1***</Uuid>
        <RuleName>test-rule-1</RuleName>
        <FirstTime>1694576692000</FirstTime>
        <FirstTimeStr>1694576692000</FirstTimeStr>
        <LatestTime>1694576692000</LatestTime>
        <LatestTimeStr>1694576692000</LatestTimeStr>
        <Status>0,1,2</Status>
        <ProcPath>/usr/bin/sshpass</ProcPath>
        <FilePath>/etc/pam.d/su</FilePath>
        <CmdLine>["touch","/test/aaaa"]</CmdLine>
        <ProcPermission>rwxr-xr-x</ProcPermission>
        <Operation>READ</Operation>
        <InstanceName>ca_cpm_****</InstanceName>
        <IntranetIp>192.168.176.75</IntranetIp>
        <InternetIp>43.116.5.5</InternetIp>
        <GmtModified>167118088****</GmtModified>
        <Remark>test</Remark>
        <HandleTime>1694576692000</HandleTime>
        <ProcessId>52636</ProcessId>
        <OrgId>12</OrgId>
        <ResourceSetId>12</ResourceSetId>
        <OrgName>test</OrgName>
        <ResourceSetName>test</ResourceSetName>
    </EventDTOList>
    <PageInfo>
        <Count>2</Count>
        <PageSize>20</PageSize>
        <TotalCount>2</TotalCount>
        <CurrentPage>1</CurrentPage>
    </PageInfo>
</ListFileProtectEventExportResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | -2000 | DefenceAtLeastOneConfig | At least one protection directory is needed. |
| 500 | -100 | InternalError | The request processing has failed due to some unknown error. |

### Retrieval of host logs

#### DescribeFilterFields

You can call this operation to query the filter fields of a specified server log search condition.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeFilterFields. |
| Query | String | No | The log search condition. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Total | String | The total number of search conditions. |
| LogFilterList | Array | The filter field information. For more information, see the following parameter descriptions. |
| Fields | String | The filter fields. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeFilterFields &Query=aegis-log-login@warn_port:22 &<Common request parameters>
```

Sample responses (JSON format)

```json
 "LogFilterList":[
   "Fields":"IP;IP address,UUID;Client ID","fieldsName":"default"
```

`],`

```json
 "Total":"20",
 "RequestID":"883e1e3d-4443-4206-871c-6c0625c01332"
```

#### DescribeHistogram

You can call this operation to obtain the statistics on server logs generated within a specified time frame.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeHistogram. |
| Query | String | Yes | The log query conditions. |
| EndTime | String | Yes | The end time of the time frame specified for query. |
| StartTime | String | Yes | The start time of the time frame specified for query. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Categories | String | The timeline information. |
| Items | Array | The log quantity statistics. For more information, see the following parameter descriptions. |
| Data | List | The number of logs. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeHistogram &EndTime=2018-03-03 17:41:03 &Query=aegis-log-login@warn_port:22 &StartTime=2018-03-02 17:41:03 &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"82D245FB-7A5D-4155-B59F-5B084CE93B6B",
 "Categories":[
  "1519983663000,1519984800000",
  "1519984800000,1519986600000",
  "1519986600000,1519988400000",
  "1519988400000,1519990200000",
  "1519990200000,1519992000000",
  "1519992000000,1519993800000",
  "1519993800000,1519995600000"
```

`],`

```json
 "Items":[
   "Data":[
```

`0,` `0,` `0,` `0,` `0,` `0,` `]` `]`

#### DescribeLogInfo

You can call this operation to query the server log fields based on specified query conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeLogInfo. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query result. Default value: 20. |

| CurrentPage | Integer | No | The current page number. Default value: 1. |
|---|---|---|---|
| Query | String | Yes | The log query conditions. |
| EndTime | String | Yes | The end time of the query. |
| StartTime | String | Yes | The start time of the query. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| LogInfoItems | Array | The information about server log fields. For more information, see the following parameter descriptions. |
| Id | String | The ID of the log source. |
| Name | String | The name of the log source. |
| Fields | Array | The list of server log fields. For more information, see the following parameter descriptions. |
| Name | String | The ID of the log field. |
| Desc | String | The name of the log field. |
| Type | String | The type of the log field. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeLogInfo &CurrentPage=1 &EndTime=2018-03-03 17:41:03 &PageSize=20 &Query=aegis-log-login@warn_port:22 &StartTime=2018-03-02 17:41:03 &<Common request parameters>
```

Sample responses (JSON format)

```json
    "TotalCount":1,
    "RequestId":"3A7CFB73-C24C-4711-B7D9-2BE74EBFFE78",
    "LogInfoItems":[
            "Fields":[
                    "Desc":"IP address",
                    "Type":"string",
                    "Name":"ip"
```

`},`

```json
                    "Desc":"Client number",
                    "Type":"string",
                    "Name":"uuid"
```

`},`

```json
                    "Desc":"Logon source IP address",
                    "Type":"string",
                    "Name":"warn_ip"
```

`},`

```json
                    "Desc":"Logon port",
                    "Type":"string",
                    "Name":"warn_port"
```

`},`

```json
                    "Desc":"Logon username",
                    "Type":"string",
                    "Name":"warn_user"
```

`},`

```json
                    "Desc":"Logon type",
                    "Type":"string",
                    "Name":"warn_type"
```

`},`

```json
                    "Desc":"Logon count",
                    "Type":"string",
                    "Name":"warn_count"
```

`],`

```json
            "Id":"aegis-log-login",
            "Name":"Logon serial number"
```

`},` `]`

#### DescribeLogItems

You can call this operation to query the server log details that are returned by a query.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeLogItems. |
| PageSize | Integer | No | The number of records displayed on a page. Default value: 20. |
| CurrentPage | Integer | No | The current page number. Default value: 1. |
| Query | String | No | The log query criterion. |
| AccountSnapshot Offset | Integer | No | The offset of the account snapshot log. |
| CrackOffset | Integer | No | The offset of the brute force password cracking log. |
| LoginOffset | Integer | No | The offset of the logon log. |
| NetworkOffset | Integer | No | The offset of the network connection log. |
| PortSnapshotOffs et | Integer | No | The offset of the listening port snapshot log. |
| ProcessOffset | Integer | No | The offset of the process startup log. |
| ProcessSnapshot Offset | Integer | No | The offset of the process snapshot log. |
| EndTime | String | Yes | The end time of the time frame specified for query. |
| StartTime | String | Yes | The start time of the time frame specified for query. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The current page number. |

| SetPageSize | Integer | The maximum number of records displayed on a page. |
|---|---|---|
| AccountSnapshotOffse t | Integer | The offset of the account snapshot log. |
| AccountSnapshotTotal Count | Integer | The total number of account snapshot log entries. |
| CrackOffset | Integer | The offset of the brute force password cracking log. |
| CrackTotalCount | Integer | The total number of brute force password cracking log entries. |
| LoginTotalCount | Integer | The total number of logon log entries. |
| NetworkOffset | Integer | The offset of the network connection log. |
| NetworkTotalCount | Integer | The total number of network connection log entries. |
| PortSnapshotOffset | Integer | The offset of the listening port snapshot log. |
| PortSnapshotTotalCou nt | Integer | The total number of listening port snapshot log entries. |
| ProcessOffset | Integer | The offset of the process startup log. |
| ProcessTotalCount | Integer | The total number of process startup log entries. |
| ProcessSnapshotOffset | Integer | The offset of the process snapshot log. |
| ProcessSnapshotTotal Count | Integer | The total number of process snapshot log entries. |
| LogsList | Array | A list of host log details. For more information, see the following parameter descriptions. |
| LogSourceID | String | The ID of the log source. |
| LogSource | String | The name of the log source. |
| MLogTime | String | The time when the log entry was created. |
| MContents | Array | A list of host log entries. For more information, see the following parameter descriptions. |
| MKey | String | The log entry. |
| MValue | String | The value of the log entry. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeLogItems &CurrentPage=1 &PageSize=100 &AccountSnapshotOffset=1000 &CrackOffset=1000 &EndTime=2018-03-05 11:46:07 &LoginOffset=1000 &NetworkOffset=1000 &PortSnapshotOffset=1000 &ProcessOffset=1000 &ProcessSnapshotOffset=1000 &Query=aegis-log-login@warn_port:22 &StartTime=2018-03-02 17:41:03 &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"BE391ABB-6B7C-4C41-9F6C-862C1DEE3905",
 "PageSize":100,
 "AccountSnapshotTotalCount":0,
 "LogsList":[],
 "CrackOffset":0,
 "ProcessOffset":0,
 "NetworkOffset":0,
 "ProcessSnapshotOffset":0,
 "LoginTotalCount":0,
 "CurrentPage":1,
 "PortSnapshotOffset":0,
 "NetworkTotalCount":0,
 "AccountSnapshotOffset":0,
 "CrackTotalCount":0,
 "PortSnapshotTotalCount":0,
 "ProcessSnapshotTotalCount":0,
 "ProcessTotalCount":0
```

#### CreateLogQuery

You can call this operation to create or save server log search conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to CreateLogQuery. |
| Conditions | String | No | The log search condition. |

| QueryDetail | String | No | The log search sub-conditions. |
|---|---|---|---|
| QueryName | String | No | The saved search name. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```json
https://aegis.[ RegionId].example.com/?Action=CreateLogQuery &Conditions=aegis-log-login@warn_port:22 &QueryDetail=[[{"itemForm":{},"d":{"name":"Logons","id":"aegis-log-login","fields":[{ "name":"ip","type":"string","desc":"IP address","text":"IP(IP address)"}]] &QueryName=test &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
```

#### DescribeLogQuery

You can call this operation to query the saved server log search conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeLogQuery. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| ListTotal | Integer | The total number of returned records. |

| QueryItems | Array | The details of log search conditions. For more information, see the following parameter descriptions. |
|---|---|---|
| Conditions | String | The log search conditions. |
| QueryDetail | String | The log search sub-conditions. |
| QueryName | String | The name of the log search task. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DescribeLogQuery &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"65802B9B-4D30-40F0-8691-F126652DBEBE",
 "ListTotal":1,
 "QueryItems":[
   "QueryDetail":"[[{\"itemForm\":{},\"d\":{\"name\":\"Account
snapshot\",\"id\":\"aegis-snapshot-host\",\"fields\": [{\"name\":\"ip\",\"type\":\"string\",\"desc\":\"IP address\"}, {\"name\":\"uuid\",\"type\":\"string\",\"desc\":\"Client ID\"}, {\"name\":\"perm\",\"type\":\"string\",\"desc\":\"Root permission availability\"},{\" name\":\"home_dir\",\"type\":\"string\",\"desc\":\"Home directory\"}, {\"name\":\"warn_time\",\"type\":\"string\",\"desc\":\"Password expiration reminder t ime\"},{\"name\":\"groups\",\"type\":\"array\",\"desc\":\"User group\"}, {\"name\":\"login_ip\",\"type\":\"string\",\"desc\":\"Last logon IP\"}, {\"name\":\"last_chg\",\"type\":\"string\",\"desc\":\"Last password change time\"},{\ "name\":\"shell\",\"type\":\"string\",\"desc\":\"Linux shell command\"}, {\"name\":\"domain\",\"type\":\"string\",\"desc\":\"Windows domain\"}, {\"name\":\"tty\",\"type\":\"string\",\"desc\":\"Logon terminal\"}, {\"name\":\"account_expire\",\"type\":\"string\",\"desc\":\"Account expiration time\" },{\"name\":\"passwd_expire\",\"type\":\"string\",\"desc\":\"Password expiration time \"},{\"name\":\"last_logon\",\"type\":\"string\",\"desc\":\"Last logon time\"},{\"nam e\":\"user\",\"type\":\"string\",\"desc\":\"User\"}, {\"name\":\"status\",\"type\":\"string\",\"desc\":\"User status: 0-disabled, 1-enable d\"}]},\"searchFields\":[{\"name\":\"ip\",\"type\":\"string\",\"desc\":\"IP address\" },{\"name\":\"uuid\",\"type\":\"string\",\"desc\":\"Client ID\"}, {\"name\":\"perm\",\"type\":\"string\",\"desc\":\"Root permission availability\"},{\" name\":\"home_dir\",\"type\":\"string\",\"desc\":\"Home directory\"}, {\"name\":\"warn_time\",\"type\":\"string\",\"desc\":\"Password expiration reminder t ime\"},{\"name\":\"groups\",\"type\":\"array\",\"desc\":\"User group\"}, {\"name\":\"login_ip\",\"type\":\"string\",\"desc\":\"Last logon IP\"}, {\"name\":\"last_chg\",\"type\":\"string\",\"desc\":\"Last password change time\"},{\ "name\":\"shell\",\"type\":\"string\",\"desc\":\"Linux shell command\"}, {\"name\":\"domain\",\"type\":\"string\",\"desc\":\"Windows domain\"}, {\"name\":\"tty\",\"type\":\"string\",\"desc\":\"Logon terminal\"}, {\"name\":\"account_expire\",\"type\":\"string\",\"desc\":\"Account expiration time\" },{\"name\":\"passwd_expire\",\"type\":\"string\",\"desc\":\"Password expiration time \"},{\"name\":\"last_logon\",\"type\":\"string\",\"desc\":\"Last logon time\"},{\"nam e\":\"user\",\"type\":\"string\",\"desc\":\"User\"}, {\"name\":\"status\",\"type\":\"string\",\"desc\":\"User status: 0-disabled, 1-enable d\"}],\"f\":{\"name\":\"ip\",\"type\":\"string\",\"desc\":\"IP address\"},\"searchLimit\": [{\"name\":\"Including\",\"value\":\":\"}],\"l\":\":\",\"kw\":\"string\"}]]",
   "Conditions":"aegis-snapshot-host@ip:string",
   "QueryName":"aa"
```

`]`

#### DeleteLogQuery

You can call this operation to delete the saved server log search conditions.

| Name | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set the value to DeleteLogQuery. |
| QueryName | String | No | The name of the saved search. |

| Name | Type | Description |
|---|---|---|
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

**Error codes**

For more information about the error codes that this operation can return, see Error codes. Sample requests

```
https://aegis.[ RegionId].example.com/?Action=DeleteLogQuery &QueryName=test &<Common request parameters>
```

Sample responses (JSON format)

```json
 "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
```

### APIs for host rule settings

#### CreateAntiBruteForceRule

Creates a brute-force attacks protection rule.

**Request headers**

This operation requires only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | No | 219.133.XX.XX | The source IP address of the request. |
| Resource OwnerId | Long | Query | No | 1000000**** | A system parameter for authentication. Do not set this parameter. |
| Name | Strin g | Query | No | Rule**** | Vulnerability Name |
| Span | Integ er | Query | No | 1 | The period in which logon failures are counted. Unit: minutes. Valid values: 1 : 1 minute 2 : 2 minutes 5 : 5 minutes 10 : 10 minutes 15 : 15 minutes The Span, FailCount, and ForbiddenTime parameters define a brute-force attacks protection rule. The rule means that if an account fails to log on more than FailCount times within a Span minute period, the account is locked for ForbiddenTime minutes. |
| FailCount | Integ er | Query | No | 2 | The maximum number of logon failures allowed. Unit: times. Valid values: 2, 3, 4, 5, 10, 50, 80, and 100. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Forbidden Time | Integ er | Query | No | 5 | The duration for which the account is locked. Unit: minutes. Valid values: 5 : 5 minutes 15 : 15 minutes 30 : 30 minutes 60 : 1 hour 120 : 2 hours 360 : 6 hours 720 : 12 hours 1440 : 24 hours 10080 : 7 days 52560000 : permanent (100 years) |
| UuidList | Repe atList | Query | No | a9a95aad-2b60-4812- b22d- ***********,a9a95aad- 2b60-4812-b22d- *********** | The UUIDs of the servers to which the rule applies. Separate multiple UUIDs with a comma (,). Note: You can call the DescribeCloudCent erInstances operation to query server UUIDs. If you do not specify this parameter, the rule applies to all servers. |
| DefaultRul e | Boole an | Query | No | true | The default forwarding rule forwards traffic to a specified application and port based on the IP address. The parameters are described as follows: appId : The ID of the application. containerPort : The port of the application instance. All requests that do not match the forwarding Rules go to the specified application. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| CreateAntiBrut eForceRule | Struct | {"ruleName": "block after 5 atte _ _ _ mpts", "maxAttempts": 5, "lockoutTime": 300} | The information about the created brute- force attacks protection rule. |
| -RuleId | Long | 123 | The ID of the rule. |

Request example

```
http(s)://[Endpoint]/?Action=CreateAntiBruteForceRule &<Common request parameters>
```

Response example `JSON` format

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "CreateAntiBruteForceRule":{
  "RuleId":123
```

#### ModifyAntiBruteForceRule

Call the ModifyAntiBruteForceRule operation to modify a brute-force attacks protection rule.

**Authorization**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- aegis:ModifyAntiBruteForceRule | Write | acs:yundun-aegis:*: {#accountId}:* |

**Traffic Shaping**

Call frequency for a single user: 10 queries per second (QPS). Total call frequency for this operation: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | No | 219.133.XX.XX | The source IP address of the request. |
| Id | Long | Query | No | 65778 | The ID of the brute-force attacks protection rule. |
| Name | Strin g | Query | No | TestRule | The name of the brute- force attacks protection rule. |
| Span | Integ er | Query | No | 1 | The time interval for failed logons. Unit: minutes. Valid values: 1: 1 minute 2: 2 minutes 5: 5 minutes 10: 10 minutes 15: 15 minutes |
| FailCount | Integ er | Query | No | 10 | The threshold for the number of failed logons. Valid values: 2: 2 times 3: 3 times 4: 4 times 5: 5 times 10: 10 times 50: 50 times 80: 80 times 100: 100 times |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Forbidden Time | Integ er | Query | No | 5 | The duration to block logons. Unit: minutes. Valid values: 5: 5 minutes 15: 15 minutes 30: 30 minutes 60: 1 hour 120: 2 hours 360: 6 hours 720: 12 hours 1440: 24 hours 10080: 7 days 52560000: permanent (100 years) |
| UuidList | Repe atList | Query | No | [ { "uuid": "a9a95aad- 2b60-4812-b22d- ***********" }, { "uuid": "a9a95aad-2b60-4812- b22d-***********" } ] | The list of servers on which the brute-force attacks protection rule takes effect. |
| DefaultRul e | Boole an | Query | No | true | Specifies whether to set the brute-force attacks protection rule as the default policy. Valid values: true: Sets the rule as the default policy. false: Does not set the rule as the default policy. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. Alibaba Cloud generates a unique ID for each request. You can use the request ID to troubleshoot issues. |

Request example

```
https://[Endpoint]/?Action=ModifyAntiBruteForceRule&RegionId=cnhangzhou&SourceIp=219.133.XX.XX&ResourceOwnerId=&Id=65778&Name=TestRule&Span=1&FailCount= &ForbiddenTime=5&UuidList.1={"uuid":"a9a95aad-2b60-4812-b22d-
***********"}&DefaultRule=true
```

Response example `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

`XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <ModifyAntiBruteForceRuleResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
</ModifyAntiBruteForceRuleResponse>
```

**Additional information**

"PageInfo":{ "TotalCount":10, "PageSize":10, "CurrentPage":1, "Count":1 }, "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Rules":[ "Uuid":"49e25e0f-bb51-4a5a-a1b3-13a4ddaa****", "Id":1, "Name":"test" ]

#### DescribeAntiBruteForceRules

This operation queries the brute-force attacks protection rules that you have created.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | No | 1000000**** | The source IP address. |
| Resource OwnerId | Long | Query | No | 1000000**** | You do not need to specify this parameter. |
| Id | Long | Query | No | 245 | The ID of the baseline policy. |
| CurrentPa ge | Integ er | Query | No | 4 | The number of the page to return. |
| PageSize | Strin g | Query | No | N/A | The number of entries to return on each page. |
| Name | Strin g | Query | No | Rule**** | Vulnerability name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Rules | Array | - | The following is a list of rules that the check item supports. |
| -UuidList | List | ["3bb30859-b3b5- 4f28-868f- b0892c98****"] | Specify the UUID of the asset to query. You can separate multiple UUIDs with a comma. |
| -Id | Long | 1 | The ID of the rule. |
| -DefaultRule | Boolean | true | Indicates whether the rule is the default rule. Valid values: true : The rule is the default rule. false : The rule is not the default rule. A brute-force attacks protection rule that is set as the default rule applies to all servers for which no other rules are configured. |
| -Name | String | test | Name of the vulnerability |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Span | Integer | 10 | The period of time during which logon failures are measured. Unit: minutes. For example, if span is 10 and the number of logon failures exceeds the specified threshold within 10 minutes, the brute- force attack protection rule takes effect and blocks logons for a specified period. |
| -FailCount | Integer | 0 | The number of failed logons. |
| - ForbiddenTime | Integer | 360 | The duration for which to block the IP address of an attacker after the rule is triggered. Unit: minutes. |
| - EnableSmartR ule | Boolean | false | This parameter is deprecated. You can ignore it. |
| -MachineCount | Integer | 1 | The number of servers for which security alerts are generated. |
| - CreateTimesta mp | Long | 1527690629357 | Last scan time. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| PageInfo | Struct | - | The pagination information. |
| -Count | Integer | 1 | The number of entries returned on the current page. |
| -PageSize | Integer | 10 | The number of entries returned per page. |
| -TotalCount | Integer | 10 | The total number of entries. |
| -CurrentPage | Integer | 1 | The page number of the returned page. |

Request example

```
http(s)://[Endpoint]/?Action=DescribeAntiBruteForceRules &<Common request parameters>
```

Response example `JSON` format

```json
 "PageInfo":{
  "TotalCount":10,
  "PageSize":10,
  "CurrentPage":1,
  "Count":1
```

`},`

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Rules":[
   "DefaultRule":true,
   "ForbiddenTime":360,
   "UuidList":[
                                                   "3bb30859-b3b5-4f28-868f-b0892c98****"
```

`],`

```json
   "FailCount":0,
   "EnableSmartRule":false,
   "MachineCount":1,
   "Id":1,
   "Span":10,
   "CreateTimestamp":1527690629357,
   "Name":"test"
```

`]` `XML` format

#### DescribeInstanceAntiBruteForceRules

Retrieves a list of servers that have active brute-force attack defense rules.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | No | 219.133.XX.XX | The source IP address of the request. |
| Resource OwnerId | Long | Query | No | 1000000**** | A system parameter for authentication. Do not specify this parameter. |

| erver Guard veloper Guid n | Advanced e·API doc | Edition D umentati |   | Alibab | a Cloud Security-Server G ard Advanced Editio |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| UuidList | Repe atList | Query | No | a9a95aad-2b60-4812- b22d- ***********,a9a95aad- 2b60-4812-b22d- *********** | The UUIDs of the servers that you want to query. Separate multiple UUIDs with a comma (,). Note: You can call the DescribeCloudCent erInstances operation to query the UUIDs of asset instances associated with a specific asset tag. If this parameter is left empty, the tags specified by the TagList parameter are removed from all asset instances. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Rules | Array | dubbo | The check item supports the following rules. |
| -Id | Long | 1 | The policy ID. |
| -Name | String | test | Vulnerability name. |
| -Uuid | String | 49e25e0f-bb51- 4a5a-a1b3- 13a4ddaa**** | The UUID of the server. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| PageInfo | Struct | - | The pagination information. |
| -Count | Integer | 1 | The number of entries returned on the current page. |
| -PageSize | Integer | 10 | The number of entries to return on each page. |

| libaba Cloud Sec rd Advanced Edit | urity-Server Gu ion |   | Server Guard Advanced Edition D eveloper Guide·API documentat |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -TotalCount | Integer | 10 | The total number of entries returned. |
| -CurrentPage | Integer | 1 | The page number of the returned page. |

Request example

```
http(s)://[Endpoint]/?Action=DescribeInstanceAntiBruteForceRules &Common request parameters
```

Response example `JSON` format

```json
 "PageInfo":{
  "TotalCount":10,
  "PageSize":10,
  "CurrentPage":1,
  "Count":1
```

`},`

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Rules":[
   "Uuid":"49e25e0f-bb51-4a5a-a1b3-13a4ddaa****",
   "Id":1,
   "Name":"test"
```

`]`

## Error codes

This topic describes the error codes returned for operations in Apsara Stack Security. Table 1. Common errors

| Error code | Error message | Description |
|---|---|---|
| yd.error.all.10001 | Authorization required. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.all.10002 | A system error occurred. Try again later. | The error message returned because a system error occurred. Try again later. |
| yd.error.all.10003 | The parameter is invalid. | The error message returned because the specified parameter is invalid. Check the request parameter and try again. |
| yd.error.all.other | A system exception occurred. | The error message returned because a system error occurred. Try again later. |
| yd.error.all.ConsoleSystemError 1001 _ | An unknown error occurred. | The error message returned because an unknown error occurred. Try again later. |
| yd.error.all.ConsoleSystemError 1007 _ | The specified API operation is unpublished. | The error message returned because the specified API operation is unpublished. Contact Alibaba Cloud technical support. |
| yd.error.all.ConsoleSystemError 1008 _ | An error occurred while verifying postOnly. | The error message returned because the verification failed. Check the common request parameters and try again. |
| yd.error.all.ConsoleSystemError 1009 _ | The csrfToken field is not specified. | The error message returned because the csrfToken field is empty. Check the common request parameters and try again. |
| yd.error.all.ConsoleSystemError 1010 _ | An error occurred while verifying csrfToken. | The error message returned because the verification failed. Check the common request parameters and try again. |
| yd.error.all.ConsoleSystemError 1011 _ | The regionId parameter is not specified. | The error message returned because the RegionId parameter is not specified. Check the parameter. |
| yd.error.all.ConsoleSystemError 1012 _ | The format of the specified regionId parameter is invalid. | The error message returned because the format of the specified RegionId parameter is invalid. Check the parameter. |

| yd.error.all.ConsoleSystemError 1013 _ | The parameter is not specified. | The error message returned because the parameter is not specified. Check the parameter and try again. |
|---|---|---|
| yd.error.all.ConsoleSystemError 1014 _ | The format of the specified parameter is invalid. | The error message returned because the format of the specified parameter is invalid. Check the parameter and try again. |
| yd.error.all.ConsoleNeedLogin | You are not logged on. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.all.InvalidApi | An operation exception occurred. | The error message returned because an operation exception occurred. Try again later. |
| yd.error.all.InvalidParameter | The parameter is invalid. | The error message returned because the specified parameter is invalid. Check the request parameter and try again. |
| yd.error.all.InvalidResult | The return value is invalid. | The error message returned because the return value is invalid. Try again later. |
| yd.error.all.PropertyConvertFail ed | An error occurred during conversion. | The error message returned because property conversion failed. Try again later. |
| yd.error.all.NoPermission | Authorization required. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.all.ServerError | A server error occurred. | The error message returned because a server error occurred. Try again later or contact Alibaba Cloud technical support. |
| yd.error.all.UnkownError | An unknown error occurred. | The error message returned because an unknown error occurred. Try again later or contact Alibaba Cloud technical support. |

Table 2. Error codes specific to Threat Detection Service

| Error code | Error message | Description |
|---|---|---|
| yd.error.sas.1 | The specified field does not exist in the metadata. | The error message returned because the field you queried does not exist in the metadata. Check the request and try again. |

| yd.error.sas.2 | An error occurred while invoking the task engine. Try again. | The error message returned because the system failed to invoke the task engine. Try again later. |
|---|---|---|
| yd.error.sas.3 | An error occurred while starting the task. Try again. | The error message returned because the system failed to start the task. Try again later. |
| yd.error.sas.4 | An error occurred while stopping the task. Try again. | The error message returned because the system failed to stop the task. Try again later. |
| yd.error.sas.5 | An error occurred while restarting the task. Try again. | The error message returned because the system failed to restart the task. Try again later. |
| yd.error.sas.6 | An error occurred while obtaining the task status. Try again. | The error message returned because the system failed to obtain the task status. Try again later. |
| yd.error.sas.7 | An error occurred while deleting the task. Try again. | The error message returned because the system failed to delete the task. Try again later. |
| yd.error.sas.8 | The specified table does not contain metadata. | The error message returned because the table you queried does not contain metadata. Check the request and try again. |
| yd.error.sas.100 | Request failed. Refresh the page and try again. | The error message returned because the request failed. Try again later. |
| yd.error.sas.101 | The parameter is invalid. | The error message returned because the parameter is invalid. Check the parameter and try again. |
| yd.error.sas.103 | Request failed. | The error message returned because the request failed. Check the request and try again later. |
| yd.error.sas.400 | The asset is under protection. Uninstall the Server Guard agent and try again. | The error message returned because the asset that you want to delete is protected by the Server Guard agent. Uninstall the Server Guard agent from the server and try again. |
| yd.error.sas.500 | A system error occurred. | The error message returned because a system error occurred. Contact Alibaba Cloud technical support. |
| yd.error.sas.501 | The feature is not available in the current version. | The error message returned because the version you used does not support this feature. |

| yd.error.sas.502 | You are not authorized to access the server. | The error message returned because you are not authorized to manage the server. |
|---|---|---|

Table 3. Error codes specific to Anti-DDoS Service

| Error code | Error message | Description |
|---|---|---|
| yd.error.ddos.400 | An error occurred while accessing the server. Try again. | The error message returned because the system failed to access the server. Try again later. |
| yd.error.ddos.500 | An error occurred on the server. Contact technical support. | The error message returned because an error occurred on the server. Contact Alibaba Cloud technical support. |
| yd.error.ddos.UNKNOWN EXCE _ PTION | An unknown error occurred. | The error message returned because an unknown error occurred. Contact Alibaba Cloud technical support. |
| yd.error.ddos.REQUEST TIMEO _ UT | The request timed out. | The error message returned because the request timed out. Try again later. |
| yd.error.ddos.SERVER FAILED _ | The operation failed. | The error message returned because the operation failed. Contact Alibaba Cloud technical support. |
| yd.error.ddos.NOT AUTHORIZE _ D | Authorization required. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.ddos.PARAMETER INVA _ LID | The parameter is invalid or is not specified. | The error message returned because the specified request parameter is invalid. Check the parameter and try again. |
| yd.error.ddos.IP SEGMENT INV _ _ ALID | The specified CIDR block is invalid. Check the parameter and enter another value. | The error message returned because the specified CIDR block is invalid. Check the CIDR block specified in the request parameter. |
| yd.error.ddos.IP SEGMENT REP _ _ EAT | One CIDR block cannot be used in different regions. Enter another CIDR block. | The error message returned because the specified CIDR block is invalid. Check the CIDR block specified in the request parameter. |
| yd.error.ddos.IP SEGMENT ALR _ _ EADY | The specified CIDR block already exists. | The error message returned because the specified CIDR block is in use. Check the CIDR block specified in the request parameter. |

| yd.error.ddos.IP SEGMENT MAS _ _ K LENGTH ERR _ _ | The mask can contain a maximum of 24 bits. | The error message returned because the mask contains more than 24 bits. Check the mask of the CIDR block specified in the request parameter. |
|---|---|---|
| yd.error.ddos.QUERY REGION L _ _ IST ERR _ | An error occurred while obtaining the region list. | The error message returned because the system failed to obtain the region list. Try again later. |
| yd.error.ddos.IP SEGMENT OPE _ _ RATION ERR _ | An error occurred while processing the CIDR block. | The error message returned because the system failed to process the CIDR block. Try again later. |
| yd.error.ddos.QUERY IP SEGME _ _ NT ERR _ | An error occurred while obtaining the CIDR block. | The error message returned because the system failed to obtain the CIDR block. Try again later. |
| yd.error.ddos.MODIFY IP SEGM _ _ ENT ERR _ | An error occurred while modifying the CIDR block. | The error message returned because the system failed to modify the CIDR block. Try again later. |
| yd.error.ddos.IP SEGMENT TYP _ _ E ERR _ | Check whether the type of the CIDR block (internal or external) is specified. | The error message returned because the CIDR block type is not specified. Check the CIDR block type and try again. |
| yd.error.ddos.CANCEL FLOW C _ _ LEAN ERR _ | An error occurred while canceling traffic scrubbing. Check whether the network connection to Network Detection and Response is normal. | The error message returned because the system failed to cancel traffic scrubbing. Check the network connection to Network Detection and Response and try again. |
| yd.error.ddos.QUERY FLOW AN _ _ ALYSIS ERR _ | An error occurred while obtaining the traffic analysis result. Check whether the network connection to Network Detection and Response is normal. | The error message returned because the system failed to obtain the traffic analysis result. Check the network connection to Network Detection and Response and try again. |
| yd.error.ddos.QUERY BEAVER _ _ URL ERR _ | An error occurred while obtaining the URL of Network Detection and Response. | The error message returned because the system failed to obtain the URL of Network Detection and Response. Check the network connection to Network Detection and Response and try again. |
| yd.error.ddos.SET VALVE INVA _ _ LID | The threshold validation failed. Check the thresholds and enter correct values. | The error message returned because the threshold verification failed. Check the thresholds and try again. |

| yd.error.ddos.VALVE DEFAULT _ _ ALREADY | The specified request is invalid. You cannot add the default threshold. | The error message returned because the system failed to add the default threshold. The default threshold can only be modified. |
|---|---|---|
| yd.error.ddos.NOT BELONG BE _ _ AVER IP SEGMENT _ _ | Check whether the specified CIDR block belongs to the internal network of Network Detection and Response. | The error message returned because the CIDR block you entered does not belong to the internal network of Network Detection and Response. Check the CIDR block. |
| yd.error.ddos.VALVE DELETE E _ _ RR | The default threshold or the threshold configured for 128.0.XX.XX/XX cannot be deleted. | The error message returned because the system failed to delete the default threshold or the threshold configured for 128.0.XX.XX/XX. |
| yd.error.ddos.QUERY CODE ER _ _ R | An error occurred while obtaining the product configuration. | The error message returned because the system failed to obtain the product configuration. Try again later. |
| yd.error.ddos.IS OPENED _ | Enabled. | The error message returned because the specified switch has been turned on. |
| yd.error.ddos.IS CLOSED _ | Disabled. | The error message returned because the specified switch has been turned off. |

Table 4. Error codes specific to Server Guard

| Error code | Error message | Description |
|---|---|---|
| yd.error.aqs.REQUEST FAILED _ | Request failed. Try again later. | The error message returned because the request failed. Try again later. |

Table 7. Error codes specific to Cloud Firewall

| Error code | Error message |
|---|---|
| yd.error.code.200 | The request is successful. |
| yd.error.code.-360100 | The request method is invalid. |
| yd.error.code.-360101 | Authentication failed. |
| yd.error.code.-360102 | Invocation failed. |
| yd.error.code.-360103 | The parameter is invalid. Try again. |
| yd.error.code.-360104 | The specified application is invalid. Try again. |
| yd.error.code.-360105 | An error occurred while obtaining the logs. |
| yd.error.code.-360106 | An error occurred while obtaining the logs. |

| yd.error.code.-360107 | The specified UID is invalid.Try again. |
|---|---|
| yd.error.code.-360108 | An error occurred while paging. |
| yd.error.code.-360109 | The service is not supported. |
| yd.error.code.-360110 | The format of the specified IP address is invalid. Enter another value. |
| yd.error.code.-360111 | The specified time is invalid. Enter another value. |
| yd.error.code.-360112 | A parsing error occurred. |
| yd.error.code.-360113 | The name of the firewall is invalid. Enter another value. |
| yd.error.code.-360114 | The specified network instance is invalid. Enter another value. |
| yd.error.code.-360115 | The specified VPC is invalid. Enter another value. |
| yd.error.code.-360116 | The specified region is invalid. Enter another value. |
| yd.error.code.-360117 | The specified destination CIDR block is invalid. Enter another value. |
| yd.error.code.-360118 | The specified VPC firewall does not exist. Enter another value. |
| yd.error.code.-360119 | The firewall is configured and cannot be repeatedly created. |
| yd.error.code.-360120 | Authorized required. You must grant permissions to the firewall. |
| yd.error.code.-360121 | The specified security group is invalid. |
| yd.error.code.-360122 | The specified security group is invalid. |
| yd.error.code.-360123 | An error occurred while calling the ECS operation. |
| yd.error.code.-360124 | An error occurred while calling the VPC operation. |
| yd.error.code.-360125 | The format of the specified CIDR block is invalid. Enter another value. |
| yd.error.code.-360126 | An error occurred while creating a vSwitch. |
| yd.error.code.-360127 | An error occurred while creating an endpoint. |
| yd.error.code.-360128 | An error occurred while deleting an endpoint. |
| yd.error.code.-360129 | Authorization required. Try again. |
| yd.error.code.-360130 | The specified ECS instance is unavailable. |
| yd.error.code.-360131 | An unknown error occurred. |

| yd.error.code.-360132 | An error occurred while searching the route table. |
|---|---|
| yd.error.code.-360133 | The ID of the firewall is invalid. |
| yd.error.code.-360134 | The status of the firewall is invalid. Try again later. |
| yd.error.code.-360135 | The specified switch of the firewall is invalid. Enter another value. |
| yd.error.code.-360136 | The specified status of the firewall is invalid. Enter another value. |
| yd.error.code.-360137 | Unknown user. Try again. |
| yd.error.code.-360138 | The specified VPC for the firewall is invalid. Enter another value. |
| yd.error.code.-360139 | The specified VPC for the firewall is invalid. Enter another value. |
| yd.error.code.-360140 | The specified firewall does not exist. Enter another value. |
| yd.error.code.-360141 | The firewall is not configured. Configure the firewall. |
| yd.error.code.-360142 | The firewall is enabled. |
| yd.error.code.-360143 | The firewall is disabled. |
| yd.error.code.-360144 | The firewall cannot be enabled because the status of the firewall is invalid. Try again later. |
| yd.error.code.-360145 | The firewall cannot be disabled because the status of the firewall is invalid. Try again later. |
| yd.error.code.-360146 | The NIC of the firewall is invalid. Check the parameter. |
| yd.error.code.-360147 | The destination CIDR block is invalid. Specify another value. |
| yd.error.code.-360148 | The same CIDR block cannot be repeatedly configured. Specify another CIDR block. |
| yd.error.code.-360149 | The number of destination CIDR blocks exceeds the upper limit. Reduce the number of CIDR blocks. |
| yd.error.code.-360150 | The ID of the firewall is invalid. |
| yd.error.code.-360151 | The status of the endpoint is invalid. |
| yd.error.code.-360152 | The endpoint is invalid. |
| yd.error.code.-360153 | The endpoint is invalid. |
| yd.error.code.-360154 | A timeout error occurred while creating the endpoint. |

| yd.error.code.-360155 | A timeout error occurred while deleting the endpoint. |
|---|---|
| yd.error.code.-360156 | Permissions required. Try again. |
| yd.error.code.-360157 | The specified route table does not exist. |
| yd.error.code.-360158 | The route entry is invalid. |
| yd.error.code.-360159 | An error occurred while creating the route. |
| yd.error.code.-360160 | An error occurred while deleting the route. |
| yd.error.code.-360161 | A timeout error occurred while creating a route. |
| yd.error.code.-360162 | A timeout error occurred while deleting a route. |
| yd.error.code.-360163 | The route is invalid. |
| yd.error.code.-360164 | The task status is invalid. |
| yd.error.code.-360165 | An error occurred while enabling the firewall. Try again. |
| yd.error.code.-360166 | An error occurred while disabling the firewall. Try again. |
| yd.error.code.-360167 | The parameter is invalid. Try again. |
| yd.error.code.-360168 | The parameter is invalid. Try again. |
| yd.error.code.-360169 | The parameter is invalid. Try again. |
| yd.error.code.-360170 | The parameter is invalid. Try again. |
| yd.error.code.-360171 | The value of the Region parameter is invalid. |
| yd.error.code.-360172 | The system is busy. |
| yd.error.code.-360173 | The number of configured VPC firewalls reaches the upper limit. Increase the VPC firewall quota. |
| yd.error.code.-360174 | The number of configured VPC firewalls reaches the upper limit. Increase the VPC firewall quota. |
| yd.error.code.-360175 | The parameter is invalid. Try again. |
| yd.error.code.-360176 | The parameter is invalid. Try again. |
| yd.error.code.-360177 | The parameter is invalid. Try again. |
| yd.error.code.-360178 | An unknown error occurred. |
| yd.error.code.-360179 | An error occurred while calling the operation. |
| yd.error.code.-360180 | The number of VPCs that are attached to the CEN instance is insufficient. |

| yd.error.code.-360181 | The firewall of the CEN instance is overwritten. You do not need to create a firewall. |
|---|---|
| yd.error.code.-360182 | The security group does not exist. |
| yd.error.code.-360183 | The security group cannot be deleted. |
| yd.error.code.-360184 | An unknown error occurred. |
| yd.error.code.-360185 | An error occurred while updating the firewall route. |
| yd.error.code.-360186 | You cannot configure the firewall because the status of the firewall is invalid. |
| yd.error.code.-360187 | The number of VPCs in the region is insufficient. The VPC firewall cannot be enabled. |
| yd.error.code.-360188 | The quota is insufficient. You cannot configure the VPC firewall. Increase the quota. |
| yd.error.code.-360189 | The ECS instance does not exist. |
| yd.error.code.-360190 | An error occurred while calling the operation. |
| yd.error.code.-360191 | The parameter is invalid. Try again. |
| yd.error.code.-360192 | The account is invalid. Enter another value. |
| yd.error.code.-360193 | The account does not have the required permissions, and Cloud Firewall is not purchased. |
| yd.error.code.-360194 | An error occurred while configuring IPS. |
| yd.error.code.-360195 | The number of VPCs that are attached to the CEN instance is insufficient. The VPC firewall cannot be enabled. |
| yd.error.code.-360196 | VPC firewalls can be created only in the same region. |
| yd.error.code.-360197 | A conflict occurred. |
| yd.error.code.-360198 | The destination CIDR block is not specified. The firewall cannot be created. |
| yd.error.code.-360199 | A timeout error occurred while attaching Cloud Firewall to the CEN instance. |
| yd.error.code.-360200 | A timeout error occurred while creating the vSwitch. |
| yd.error.code.-360201 | A timeout error occurred while deleting the vSwitch. |
| yd.error.code.-360202 | The specified network instance ID is invalid. |
| yd.error.code.-360203 | The specified VPC does not exist. |
| yd.error.code.-360204 | A timeout error occurred while creating a VPC. |

| yd.error.code.-360205 | A timeout error occurred while creating a VPC. |
|---|---|
| yd.error.code.-360206 | The specified ECS instance does not exist. |
| yd.error.code.-360207 | An error occurred while disabling the ECS instance. Try again. |
| yd.error.code.-360208 | An error occurred while obtaining the backup ECS instance. |
| yd.error.code.-360209 | You are not allowed to create a firewall for a HUB VPC. |
| yd.error.code.-360210 | The specified CEN instance ID is invalid. |
| yd.error.code.-360211 | The parameter is invalid. Try again. |
| yd.error.code.-360212 | The number of VPCs that are attached to the CEN instance is insufficient. The VPC firewall cannot be enabled. |
| yd.error.code.-360213 | The CEN instance does not exist. |
| yd.error.code.-360214 | The request timed out. Try again. |
| yd.error.code.-360215 | The parameter is invalid. Try again. |
| yd.error.code.-360216 | The Express Connect circuit for the data center is invalid. |
| yd.error.code.-360217 | The specified firewall mode is invalid. |
| yd.error.code.-360218 | An error occurred while calling the operation of Apsara Stack Network Operations Platform (NET). |
| yd.error.code.-360300 | A backend error occurred. |
| yd.error.code.-360301 | A backend error occurred. |
| yd.error.code.-360302 | A backend error occurred. |
| yd.error.code.-360303 | A backend error occurred. |
| yd.error.code.-360304 | A backend error occurred. |
| yd.error.code.-360305 | A backend error occurred. |
| yd.error.code.-360306 | A backend error occurred. |
| yd.error.code.-360307 | A backend error occurred. |
| yd.error.code.-360308 | An error occurred while querying the cluster ID. |
| yd.error.code.-360309 | An error occurred while updating the information about the cluster. |
| yd.error.code.-360310 | An error occurred while updating the Express Connect circuit. |

| yd.error.code.-360311 | An error occurred while inserting the VLAN. |
|---|---|
| yd.error.code.-360312 | An error occurred while querying the IP address pool. |
| yd.error.code.-360313 | An error occurred while updating the IP address pool. |
| yd.error.code.-360314 | An error occurred while updating the information about the VPC route. |
| yd.error.code.-360315 | An error occurred while updating the status of the VPC. |
| yd.error.code.-360316 | An error occurred while inserting the firewall ns. |
| yd.error.code.-360317 | An error occurred while updating the VLAN. |
| yd.error.code.-360318 | An error occurred while updating the endpoint information about the firewall. |
| yd.error.code.-360319 | An error occurred while updating the network information about the firewall. |
| yd.error.code.-360320 | An error occurred while updating the health check configurations. |
| yd.error.code.-360321 | An error occurred while updating the route table. |
| yd.error.code.-360322 | An error occurred while updating the information about the Express Connect circuit for the data center. |
| yd.error.code.-360323 | An error occurred while updating the information about the route of the data center. |
| yd.error.code.-360400 | An unknown error occurred. |
| yd.error.code.-360401 | No VLAN is available. |
| yd.error.code.-360402 | An error occurred while calling the VPC operation. |
| yd.error.code.-360403 | An error occurred while creating the virtual firewall. |
| yd.error.code.-360404 | An error occurred while creating the Express Connect circuit. |
| yd.error.code.-360405 | An error occurred while enabling the Express Connect circuit. |
| yd.error.code.-360406 | An error occurred while creating the VBR. |
| yd.error.code.-360407 | An error occurred while updating the attributes of the VBR. |
| yd.error.code.-360408 | An error occurred while querying the VBR. |
| yd.error.code.-360409 | An error occurred while creating the RI. |

| yd.error.code.-360410 | An error occurred while updating the attributes of the RI. |
|---|---|
| yd.error.code.-360411 | An error occurred while connecting the RI. |
| yd.error.code.-360412 | An error occurred while creating an Express Connect circuit for the data center. |
| yd.error.code.-360413 | An error occurred while enabling an Express Connect circuit for the data center. |
| yd.error.code.-360414 | An error occurred while querying an RI. |
| yd.error.code.-360415 | An error occurred while querying the monitored IP addresses that are used for communications between VPCs. |
| yd.error.code.-360416 | An error occurred while querying the monitored IP addresses that are used for communications between a data center and a VPC. |
| yd.error.code.-360417 | The VPC monitoring mode is abnormal. |
| yd.error.code.-360418 | The status of the instance is invalid. |
| yd.error.code.-193000 | An unknown error occurred. |
| yd.error.code.-193001 | The specified HTTP request method is invalid. |
| yd.error.code.-193002 | An error occurred while calling the operation by using HTTP. |
| yd.error.code.-193003 | Permissions required. |
| yd.error.code.-193004 | Unsupported operation. |
| yd.error.code.-193005 | Authentication failed. |
| yd.error.code.-193006 | An error occurred while accessing the database. |
| yd.error.code.-193007 | Accessed native method. |
| yd.error.code.-193101 | An error occurred while encoding JSON data. |
| yd.error.code.-193102 | An error occurred while parsing JSON data. |
| yd.error.code.-193103 | An error occurred while parsing INT data. |
| yd.error.code.-193104 | An error occurred while parsing BOOL data. |
| yd.error.code.-193105 | An error occurred while parsing the body of the HTTP request. |
| yd.error.code.-193201 | The specified parameters are insufficient. |
| yd.error.code.-193202 | The specified parameter value is invalid. |
| yd.error.code.-193203 | The specified time is invalid. |

| yd.error.code.-193204 | The parameter is invalid. |
|---|---|
| yd.error.code.-193205 | The IP address is not in the value of traffic forwarding configuration. |
| yd.error.code.-193301 | The CIDR block already exists. |
| yd.error.code.-193302 | The firewall UUID is invalid. |
| yd.error.code.-193303 | The mode of the firewall is being switched. |
| yd.error.code.-193304 | The mode of the firewall is invalid. |
| yd.error.code.-193305 | The switch of the firewall mode in unauthorized. |
| yd.error.code.-193306 | The mode of the device is being switched. |
| yd.error.code.-193307 | An error occurred during the instance health check. The instance cannot be switched to the normal mode. |
| yd.error.code.-193308 | All devices are bypassed, and the instance mode cannot be switched. |
| yd.error.code.-193309 | The working mode of the instance takes precedence over the working mode of the device. |
| yd.error.code.-193310 | The specified page number is invalid. |
| yd.error.code.-193311 | The route type is invalid. |
| yd.error.code.-193312 | An error occurred while deleting the route. |
| yd.error.code.-193313 | An error occurred while deleting the route. |
| yd.error.code.-193314 | An error occurred while creating the route. |
| yd.error.code.-193315 | An error occurred while creating the route. |
| yd.error.code.-193316 | The ID of the Cloud Firewall instance is invalid. |
| yd.error.code.-193317 | The Cloud Firewall instance must be specified. |
| yd.error.code.-200100 | The request method is invalid. |
| yd.error.code.-200101 | Authentication failed. |
| yd.error.code.-200102 | Invocation failed. |
| yd.error.code.-200103 | The parameter is invalid. Try again. |
| yd.error.code.-200104 | The specified UID is invalid.Try again. |
| yd.error.code.-200105 | An error occurred while paging. |
| yd.error.code.-200106 | The IP address in the address book is invalid. Check the parameter and enter another value. |
| yd.error.code.-200107 | The address book already exists. |

| yd.error.code.-200108 | An error occurred. Try again. |
|---|---|
| yd.error.code.-200109 | The address book is in use and cannot be deleted. |
| yd.error.code.-200110 | The specified parameter is invalid. |
| yd.error.code.-200111 | The specified parameter is invalid. |
| yd.error.code.-200112 | The specified parameter is invalid. |
| yd.error.code.-200113 | The specified parameter is invalid. |
| yd.error.code.-200114 | The specified parameter is invalid. |
| yd.error.code.-200115 | The specified parameter is invalid. |
| yd.error.code.-200116 | The specified parameter is invalid. |
| yd.error.code.-200117 | The security group rule does not exist. |
| yd.error.code.-200118 | The specified priority is invalid, or the number of rules reaches the upper limit. |
| yd.error.code.-200119 | The specified priority is invalid, or the number of rules reaches the upper limit. |
| yd.error.code.-200120 | An error occurred. Try again. |
| yd.error.code.-200121 | The domain name is invalid. Check the parameter and enter another value. |
| yd.error.code.-200122 | The number of addresses in the address book exceeds the upper limit. |
| yd.error.code.-200123 | The specified parameter is invalid. |
| yd.error.code.-200124 | The specified parameter is invalid. |
| yd.error.code.-200125 | The specified parameter is invalid. |
| yd.error.code.-200126 | The specified parameter is invalid. |
| yd.error.code.-200127 | The number of ports in the address book exceeds the upper limit. |
| yd.error.code.-200128 | The port in the address book is invalid. Check the parameter and enter another value. |
| yd.error.code.-200129 | The number of address books exceeds the upper limit. |
| yd.error.code.-200130 | The number of address books exceeds the upper limit. |
| yd.error.code.-200200 | A backend error occurred. |
| yd.error.code.-200201 | A backend error occurred. |

| yd.error.code.-200202 | A backend error occurred. |
|---|---|
| yd.error.code.-200203 | A backend error occurred. |
| yd.error.code.-200300 | A backend error occurred. |
| yd.error.code.-200301 | A backend error occurred. |
| yd.error.code.-200302 | A backend error occurred. |
| yd.error.code.-200400 | An unknown error occurred. |
| yd.error.code.-200500 | An error occurred while calling the operation. |
| yd.error.code.200 | The request is successful. |
| yd.error.code.-210100 | The request method is invalid. |
| yd.error.code.-210101 | Authentication failed. |
| yd.error.code.-210102 | Invocation failed. |
| yd.error.code.-210103 | The parameter is invalid. Try again. |
| yd.error.code.-210104 | The specified UID is invalid.Try again. |
| yd.error.code.-210105 | An error occurred while paging. Try again. |
| yd.error.code.-210106 | The parameter is invalid. Try again. |
| yd.error.code.-210107 | The parameter is invalid. Try again. |
| yd.error.code.-210108 | The parameter is invalid. Try again. |
| yd.error.code.-210109 | The parameter is invalid. Try again. |
| yd.error.code.-210110 | The parameter is invalid. Try again. |
| yd.error.code.-210111 | The parameter is invalid. Try again. |
| yd.error.code.-210200 | A backend error occurred. |
| yd.error.code.-210201 | A backend error occurred. |
| yd.error.code.-210202 | A backend error occurred. |
| yd.error.code.-210203 | A backend error occurred. |
| yd.error.code.-210300 | A backend error occurred. |
| yd.error.code.-210301 | A backend error occurred. |
| yd.error.code.-210302 | An error occurred. Try again. |
| yd.error.code.-210400 | An error occurred. Try again. |
| yd.error.code.200 | Success |

| yd.error.code.-230100 | The request method is invalid. |
|---|---|
| yd.error.code.-230101 | Authentication failed. |
| yd.error.code.-230102 | An error occurred while sending the request to the local server. |
| yd.error.code.-230103 | The operation failed authentication. |
| yd.error.code.-230104 | The parameter is invalid. |
| yd.error.code.-230105 | The policy template already exists. |
| yd.error.code.-230106 | The policy template does not exist. |
| yd.error.code.-230107 | The user ID is invalid. |
| yd.error.code.-230108 | The security group ID is invalid. |
| yd.error.code.-230109 | The security group ID is invalid. |
| yd.error.code.-230110 | The direction of the rule is invalid. |
| yd.error.code.-230111 | An IP protocol error occurred. |
| yd.error.code.-230112 | The rule policy is invalid. |
| yd.error.code.-230113 | The priority of the policy is invalid. Enter another value. |
| yd.error.code.-230114 | The port in the policy is invalid. Enter another value. |
| yd.error.code.-230115 | The CIDR block is invalid. Enter another value. |
| yd.error.code.-230116 | The description is invalid. Enter another value. |
| yd.error.code.-230117 | The policy already exists. |
| yd.error.code.-230118 | The policy does not exist. |
| yd.error.code.-230119 | The rule ID is invalid. |
| yd.error.code.-230120 | The number of policies exceeds the limit. We recommend that you delete policies that you no longer use. |
| yd.error.code.-230121 | An error occurred while paging. |
| yd.error.code.-230122 | The rule is being published. Try again. |
| yd.error.code.-230123 | The submission status is invalid. |
| yd.error.code.-230124 | The policy group is rolled back. |
| yd.error.code.-230125 | The submitted information is invalid. |
| yd.error.code.-230126 | The rule is not changed. You do not need to publish the rule. |

| yd.error.code.-230127 | The security group ID is invalid. |
|---|---|
| yd.error.code.-230128 | The IP address in the rule is invalid. |
| yd.error.code.-230129 | The network type of the rule is invalid. Select another value. |
| yd.error.code.-230130 | An error occurred while managing the rule. |
| yd.error.code.-230131 | The policy cannot be submitted. |
| yd.error.code.-230150 | The policy group does not exist. Specify another value. |
| yd.error.code.-230151 | The number of policy groups exceeds the limit. |
| yd.error.code.-230152 | The policy group cannot be modified. |
| yd.error.code.-230153 | The policy group is prestarted. |
| yd.error.code.-230154 | The rule ID is invalid. |
| yd.error.code.-230200 | A backend error occurred. |
| yd.error.code.-230300 | A backend error occurred. |
| yd.error.code.-230301 | A backend error occurred. |
| yd.error.code.-230302 | A backend error occurred. |
| yd.error.code.-230400 | An unknown error occurred. |

**Error codes specific to Network Detection and Response**

| Error code | Error message | Description |
|---|---|---|
| ErrorNeedLogin.-210204 | need login (You are not logged on.) | The error message returned because you are not logged on. Log on first. |
| ErrorAuthentication.-210101 | authentication error (An authentication error occurred.) | The error message returned because an authentication error occurred. Use a RAM role that has the required permissions. |
| ErrorParametersAliUid.-210902 | invalid AliUid (The value of the AliUid parameter is invalid.) | The error message returned because the value of the AliUid parameter is invalid. Specify a valid value. |
| ErrorParametersIpType.-210920 | invalid para ip type (The value of the ipType parameter is invalid.) | The error message returned because the value of the ipType parameter is invalid. Specify a valid value. |

| ErrorParametersSrcIP.-210919 | invalid para src ip (The value of the SrcIP parameter is invalid.) | The error message returned because the value of the SrcIP parameter is invalid. Specify a valid value. |
|---|---|---|
| ErrorParametersDstIP.-210921 | invalid para dst ip (The value of the dstIP parameter is invalid.) | The error message returned because the value of the dstIP parameter is invalid. Specify a valid value. |
| ErrorParametersPort.-210208 | invalid port, must 0~65535 (The specified port number is invalid. The port number must range from 0 to 65535.) | The error message returned because the specified port number is invalid. Specify a port number ranging from 0 to 65535. |
| ErrorParametersLiveTime.- 210922 | invalid para live time (The value of the liveTime parameter is invalid.) | The error message returned because the value of the liveTime parameter is invalid. Specify a valid value. |
| ErrorDBInsert.-210122 | internal error: sql insert (An internal error occurred while executing the INSERT statement.) | The error message returned because an internal error occurred while executing the INSERT statement. |
| ErrorInnerUuid.-210606 | internal error: uuid list is 0 (The internal error of empty UUID list occurred.) | The error message returned because the UUID list is empty. |
| ErrorDBSelect.-210124 | internal error: sql select (An internal error occurred while executing the SELECT statement.) | The error message returned because an internal error occurred while executing the SELECT statement. |
| ErrorParasAddressCidrFeild.- 210915 | paras addressCidrList filed (Failed to reset the addressCidrList rule.) | The error message returned because the system failed to reset the addressCidrList rule. |
| ErrorPortAddressGroup.-210303 | get port in address group failed (Failed to obtain port information from the address group.) | The error message returned because the system failed to obtain port information from the address group. |
| ErrorPortAddressGroup.-210303 | get port in address group failed (Failed to obtain port information from the address group.) | The error message returned because the system failed to obtain port information from the address group. |
| ErrorSourceAddressGroup.- 210304 | get source address in address group failed (Failed to obtain source addresses from the address group.) | The error message returned because the system failed to obtain source addresses from the address group. |
| ErrorSourceAddressRange.- 210306 | source address range error, must be like \"192.168.XX.XX/192.168.XX.X X\" (The source address range is invalid. Example: \"192.168.XX.XX/192.168.XX.X X\") | The error message returned because the source address range is invalid. Specify the value in the \"192.168.XX.XX/192.168.XX.X X\" format. |

| ErrorDestAddressGroup.- 210305 | get dest address in address group failed (Failed to obtain destination addresses from the address group.) | The error message returned because the system failed to obtain destination addresses from the address group. |
|---|---|---|
| ErrorNoBeaverRules.-210226 | no beaver rules for online (The specified Network Detection and Response rule does not exist.) | The error message returned because the specified Network Detection and Response rule does not exist. |
| ErrorDBUpdate.-210121 | internal error: sql update (An internal error occurred while executing the UPDATE statement.) | The error message returned because an internal error occurred while executing the UPDATE statement. |
| ErrorDBDelete.-210123 | internal error: sql delete (An internal error occurred while executing the DELETE statement.) | The error message returned because an internal error occurred while executing the DELETE statement. |
| ErrorMarshalJSON.-210125 | internal error: marshal json (An internal error occurred while marshaling JSON data.) | The error message returned because an internal error occurred while marshaling JSON data. |
