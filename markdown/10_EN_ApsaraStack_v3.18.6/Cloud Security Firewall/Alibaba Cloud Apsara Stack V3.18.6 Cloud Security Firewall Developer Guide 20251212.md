---
title: "Cloud Security Firewall Developer Guide 20251212"
product_version: "V3.18.6"
pdf_pages: 114
source_pdf: "7703c5b6813f39c3_Alibaba Cloud Apsara Stack V3.18.6 Cloud Security Firewall Developer Guide 20251212.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%BE-%E4%BA%91%E9%98%B2%E7%81%AB%E5%A2%99/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Cloud%20Security%20Firewall%20Developer%20Guide%2020251212.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Cloud Security Firewall Developer Guide 20251212

## Table of Contents

- 1 Preparations
  - 1.1 Log on to the Developer Portal console
  - 1.2 Obtain an AccessKey pair
- 2 Use POP to make API calls
  - 2.1 Preparations
  - 2.2 SDK for Java
  - 2.3 SDK for Go
  - 2.4 Python version
- 3 API common parameters
- 4 Cloud Firewall
  - 4.1 Invocation method
    - 4.1.1 Request structure
    - 4.1.2 Request signatures
    - 4.1.3 Common parameters
    - 4.1.4 Response structure
  - 4.2 Firewall switch
    - 4.2.1 PutEnableFwSwitch
    - 4.2.2 PutDisableFwSwitch
    - 4.2.3 PutEnableAllFwSwitch
    - 4.2.4 PutDisableAllFwSwitch
    - 4.2.5 UpdateResourceDetails
    - 4.2.6 PutEnableAllResourceFwSwitch
    - 4.2.7 PutDisableAllResourceFwSwitch
  - 4.3 VPC firewalls
    - 4.3.1 CreateVpcFirewallControlPolicy
    - 4.3.2 DescribeVpcFirewallControlPolicy
    - 4.3.3 ModifyVpcFirewallControlPolicy
    - 4.3.4 ModifyVpcFirewallControlPolicyPosition
    - 4.3.5 DeleteVpcFirewallControlPolicy
    - 4.3.6 DescribeVpcFirewallPolicyPriorUsed
    - 4.3.7 DescribeVpcFirewallAclGroupList
    - 4.3.8 ResetVpcFirewallRuleHitCount
  - 4.4 Access control
    - 4.4.1 DescribePolicyPriorUsed
    - 4.4.2 ModifyControlPolicyPosition
    - 4.4.3 DescribeControlPolicy
    - 4.4.4 AddControlPolicy
    - 4.4.5 DeleteControlPolicy
    - 4.4.6 ModifyControlPolicy
  - 4.5 Address books
    - 4.5.1 AddAddressBook
    - 4.5.2 DeleteAddressBook
    - 4.5.3 ModifyAddressBook
    - 4.5.4 DescribeAddressBook
- 5 Error codes

## 1 Preparations

### 1.1 Log on to the Developer Portal console

**console**

You can log on to the Developer Portal console through the Apsara Uni-manager Management Console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, you must obtain the endpoint of the console from the deployment personnel. We recommend that you use the Chrome browser.

**Procedure**

1. In the address bar of your browser, enter the endpoint of the Apsara Uni-manager
Management Console and press Enter.
2. Enter the correct username and password.
You can obtain the username and password to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. For security purposes, your password must be 10 to 32 characters in length and must contain at least two of the following types of characters: Uppercase or lowercase letters (A to Z, a to z) Digits (0 to 9) Special characters (such as exclamation mark (!), at sign (@), number sign (#), dollar sign ($), and percent sign (%))
3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the following
operations based on your scenario: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator: a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Re-enter your username and password as described in Step 2, and click **Log On**. c. Enter the 6-digit MFA code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter the 6-digit MFA code and click **Authenticate**.

**Note**

For more information about how to bind and enable an MFA device, see the **Bind and**
**Enable a Virtual MFA Device** section in the **Apsara Uni-manager Management**
**Console User Guide**.
5. In the top menu bar, choose **Products > Application Services > Developer Portal**.

### 1.2 Obtain an AccessKey pair

AccessKey credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You can use one type of AccessKey credentials for authentication when you call API operations. This topic describes how to obtain an AccessKey pair assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender based on symmetric encryption. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID identifies a user. The AccessKey secret is a string used to encrypt signatures. AccessKey credentials can be assigned by RAM or STS: RAM: assigns an AccessKey pair that consists of an AccessKey ID and an AccessKey secret. STS: assigns an access credential that consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an STS AccessKey pair. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only operations administrators and administrators of level-1 organizations can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the following request headers for access control. Otherwise, an error indicating insufficient permissions may occur.

**Warning**

The AccessKey pair of a personal account is managed and controlled by the permission system of the Apsara Uni-manager Management Console. To obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The region, such as cn-hangzhou-*. |
| x-acs-organizationid | The organization ID in the Apsara Uni-manager Management Console. For more information about how to obtain the organization ID, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide. |

| x-acs-resourcegroupid | The resource set ID in the Apsara Uni-manager Management Console. For more information about how to obtain the resource set ID, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide. |
|---|---|
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

**Obtain an AccessKey pair for personal accounts**

To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the page, click your profile picture and select **Personal**
**Information**.
3. In the **Alibaba Cloud AccessKey** section, you can view the AccessKey information of your
personal account.

**Note**

The AccessKey pair provides full permissions on cloud resources within your Alibaba Cloud account. You must keep the AccessKey pair confidential.

**Obtain an AccessKey pair for organizations**

To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the navigation pane on the left, choose **Resource Management > Organization**
**Management**.
4. In the organization chart, click the name of the target level-1 organization.
5. Click **Manage AccessKey**.
6. In the dialog box that appears, view the AccessKey information of the organization.
e API calls

## 2 Use POP to make API calls

### 2.1 Preparations

You can use the POP gateway to call API operations in Apsara Stack in the same way as in Alibaba Cloud public cloud. This topic describes the preparations required before calling API operations.

**Background information**

To enable you to use the API call method in Apsara Stack as in Alibaba Cloud public cloud and provide a more convenient and consistent experience, we recommend that you use the POP gateway to call Apsara Stack API operations.

**Obtain an endpoint**

**Obtain an endpoint from the Developer Portal**

1. Go to the Apsara Uni-manager Management Console.
2. In the top menu bar, choose **Products** > **Development Tools** > **API & SDK** > **OpenAPI**
**Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging**.
4. In the left-side navigation pane, select the cloud service that you want to manage.
5. From the **Version** drop-down list, select the API version that you want to use.
6. In the API list, you can view all API operations of the current version.
7. Select the corresponding API operation and obtain the POP Endpoint information under the
parameter name.

**Obtain an endpoint from Apsara Infrastructure Management**

e API calls To use the POP gateway to call Apsara Stack API operations, you must use the service endpoint. You can obtain an endpoint from onsite Alibaba Cloud O&M engineers. You can also obtain service endpoints by yourself. In this example, API Gateway is used to demonstrate how to obtain the endpoints of a cloud service.
1. Go to the Apsara Uni-manager Operations Console.
2. In the top menu bar, choose **Platform Operation**> **Apsara Infrastructure**
**Management** > **O&M Tools**.
3. In the left navigation bar, select **O&M Tools** > **Service Registration Variable**
**Dashboard**.
4. On the Service Registration Variable Dashboard page, click **Advanced Filter**.
5. In the Service Registration text box, enter `apigateway` , and click **Search**.
6. In the Service Registration column of the `apigateway` service, click the **Service**

**Registration**

icon.
7. Click the text information in the **Service Registration** column of the `apigateway` service.
In the **Registration Variable** dialog box that appears, view the apigateway.openapi.endpoint value, which is the `Endpoint` .

**Obtain common parameters**

For information about how to obtain parameters such as organization ID, resource set ID, region ID, and instance ID that are used when you call Apsara Stack API operations through the POP gateway, see the **Obtain common header parameters** section under
**Preparations** in this guide.

### 2.2 SDK for Java

Before you use point of presence (POP) SDK for Java to make API calls, you must first understand the remote procedure call (RPC) and resource-oriented architecture (ROA) styles.

**Prerequisites**

We recommend that you use CommonRequest to make API calls in Apsara Stack. You can go to the Apsara Uni-manager Management Console and choose **Products** > **Development**
**Tools** > **API & SDK** > **OpenAPI Explorer,** and then select **API Integration** > **SDK**
**Examples** to view the recommended SDK versions and sample code.

**Important**

We do not recommend that you download SDKs from the SDK Center for use in Apsara Stack scenarios. The SDKs for Alibaba Cloud public cloud may not support the APIs of Apsara Stack. Compatibility issues may occur. Use these SDKs with caution!

**Examples**

RPC call example with the following API information: product (apigateway), operation (DescribeApiGroups), and version (2016-07-14). Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; importcomaliyuncsexceptionsClientException;
```

e API calls

```java
import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize it.
        DefaultProfile profile = DefaultProfile.getProfile("", "", "");
        // Ignore SSL certificate verification.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the timeout period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set the parameters.
        CommonRequest request = new CommonRequest();
        // Specify the request method
        request.setSysMethod(MethodType.POST);
        // Specify the endpoint of the service.
        request.setSysDomain("");
        // Specify the API version.
        request.setSysVersion("2016-07-14");
        // Specify the service name.
        request.setSysLocationProduct("apigateway");
        // Specify the name of the API operation.
        request.setSysAction("DescribeApiGroups");
        // If you use the Security Token Service (STS) AccessKey pair to call RPC API o
perations, you must specify the SecurityToken parameter.
        // request.putBodyParameter("SecurityToken", "");
        // Set service-related parameters.
        request.putQueryParameter("PageSize", "10");
        request.putQueryParameter("PageNumber", "1");
        // (Required) Specify the call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // (Optional) You must specify this parameter for Apsara Stack V3.15.0 or
earlier.
        request.putHeadParameter("x-acs-regionid", "");
        // (Optional) Specify the ID of the resource set.
        request.putHeadParameter("x-acs-resourcegroupid", "");
        // (Required) Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "");
        // (Optional) You must specify this parameter when you modify or delete
resources.
        // request.putHeadParameter("x-acs-instanceid", "");
```

e API calls

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
```

`}` `}` `}` ROA call example with the following API information: product (CR), operation (GetNamespaceList), and version (2016-06-07). Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize it.
        DefaultProfile profile = DefaultProfile.getProfile("", "", "");
        // Ignore SSL certificate verification.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the timeout period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set the parameters.
        CommonRequest request = new CommonRequest();
        // Configure HTTPS access
        request.setSysProtocol(ProtocolType.HTTP);
        // Specify the request method
        request.setSysMethod(MethodType.GET);
        // Specify the endpoint of the service
        request.setSysDomain("");
//S
```

`if` `th`

```
API
```

`i` e API calls

```java
        // Specify the API version
        request.setSysVersion("2016-06-07");
        // Set the URI pattern (required only for ROA calls)
        request.setSysUriPattern("/namespace");
        // Specify the service name
        request.setSysLocationProduct("cr");
        // Specify the name of the API operation
        request.setSysAction("GetNamespaceList");
        // (Required) Specify the call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // (Optional) You must specify this parameter for Apsara Stack V3.15.0 or
earlier.
        request.putHeadParameter("x-acs-regionid", "");
        // Optional. Specify the ID of the resource set.
        request.putHeadParameter("x-acs-resourcegroupid", "");
        // Required. Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "");
        // (Optional) You must specify this parameter when you modify or delete
resources.
        // request.putHeadParameter("x-acs-instanceid", "");
        // When you use an STS AccessKey pair to call ROA API operations, you must add
the x-acs-security-token field to the header
        // request.putHeadParameter("x-acs-security-token", "");
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

**Important**

By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be disabled in the test environment, you can configure the following setting: Java e API calls

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Disable server certificate verification. clientConfig.setIgnoreSSLCerts(true)
```

### 2.3 SDK for Go

This topic describes how to work with the POP SDK for Go.

**Prerequisites**

For Apsara Stack, we recommend that you use CommonRequest to call API operations. You can view the recommended SDK versions and sample code in the Apsara Uni-manager Management Console by choosing **Products** > **Development Tools** > **API & SDK** >
**OpenAPI Explorer**, and then selecting **API Integration** > **SDK Examples**.

**Important**

We do not recommend that you download SDKs from the SDK center for use in Apsara Stack environments. The SDKs for Alibaba Cloud public cloud may not support the API operations of Apsara Stack and may have compatibility issues. Use them with caution!

**Background information**

Remote procedure call (RPC) and resource-oriented architecture (ROA) styles are supported for API calls.

**Examples**

RPC example API information: product (apigateway), API operation (DescribeApiGroups), and version (2016-07-14). The following sample code provides an example: e API calls

```java
package main import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey("", "", "")
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = ""
    request.Version = "2016-07-14"
    request.ApiName = "DescribeApiGroups"
    request.Product = "apigateway"
    // If you use the Security Token Service (STS) to AccessKey pair to call RPC API op
erations, you must specify the SecurityToken parameter.
    // request.QueryParams["SecurityToken"]=""
    // Required. Specify the call source.
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. You must specify this parameter for Apsara Stack V3.15.0 or earlier.
    request.Headers["x-acs-regionid"] = ""
    // Optional. Specify the ID of the resource set.
    request.Headers["x-acs-resourcegroupid"] = ""
    // Required. Specify the organization ID.
    request.Headers["x-acs-organizationid"] = ""
    // Optional. You must specify this parameter when you modify or delete resources.
    // request.Headers["x-acs-instanceid"] = ""
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}` ROA example API information: product (CR), API operation (GetNamespaceList), and version (2016-06-07). Sample code: e API calls

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
    client, err := sdk.NewClientWithAccessKey("", "", "")
 request := requests.NewCommonRequest()
 request.Method = "GET"
 request.Domain = ""
 request.Version = "2016-06-07"
 request.ApiName = "GetNamespaceList"
 request.Product = "cr"
 request.PathPattern = "/namespace"
 // If you use the STS AccessKey pair to call ROA API operations, you must add the x-
acs-security-token field to the header
 // request.Headers["x-acs-security-token"] = ""
 // Required. Specify the call source.
 request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. You must specify this parameter for Apsara Stack V3.15.0 or earlier.
    request.Headers["x-acs-regionid"] = ""
    // Optional. Specify the ID of the resource set.
    request.Headers["x-acs-resourcegroupid"] = ""
    // Required. Specify the organization ID.
    request.Headers["x-acs-organizationid"] = ""
 // Optional. You must specify this parameter when you modify or delete resources.
 // request.Headers["x-acs-instanceid"] = ""
 response, err := client.ProcessCommonRequest(request)
 if err != nil {
  panic(err)
```

`}`

```
 fmt.Print(response.GetHttpContentString())
```

`}`

**Proxy settings**

You can configure a proxy in one of the following ways when you call API operations: Method 1: Configure a proxy by using environment variables. Specify the HTTP_PROXY and HTTPS_PROXY environment variables, or specify the NO_PROXY environment variable. Sample code: e API calls

```java
import (
    "os"
```

`)`

```
func main(){
 os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // Specify the HTTP_PROXY environment
variable.
 os.Setenv("HTTPS_PROXY", "https://x.x.x.x:xxxx") // Specify the HTTPS_PROXY environm
ent variable.
```

`}` Method 2: Configure a proxy on the client. Sample code:

```
// The proxy settings on the client take precedence over the environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Configure the HTTP proxy. client.GetHttpProxy() // Query the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Configure the HTTPS proxy. client.GetHttpsProxy() // Query the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Configure the proxy whitelist. client.GetNoProxy() // Query the proxy whitelist.
```

**SSL verification**

**Summary**

You can configure SSL certificate verification for requests. If you set this parameter to `true` , certificate verification is disabled. This is not secure. We recommend that you configure certificates. If you set this parameter to `false` , SSL certificate verification is enabled. By default, the CA certificates provided by the operating system are used.

**Default value**

The default value is `false` .

**Settings**

**Important**

By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be disabled in the test environment, you can specify the following settings:

```
// Configure HTTPSInsecure for the request (affects only the current request) request.SetHTTPSInsecure(true) // Set HTTPSInsecure to true fo r the request. isInsecure := request.GetHTTPSInsecure() // Query the HTTPSInsecure sett ing for the request.
```

e API calls The HTTPSInsecure setting takes effect for the client only when you do not specify the HTTPSInsecure parameter for the request.

```
// Configure HTTPSInsecure for the client (affects all requests sent by the client). client.SetHTTPSInsecure(true) // Set HTTPSInsecure to true for t he client. isInsecure := client.GetHTTPSInsecure() // Query the HTTPSInsecure setting for the client.
```

### 2.4 Python version

This topic describes how to use POP Python SDK to call cloud product APIs.

**Prerequisites**

We recommend using CommonRequest for API calls in Apsara Stack. You can view the recommended SDK version and sample code in the Apsara Uni-manager Management Console by navigating to **Products** > **Development Tools** > **API & SDK** > **OpenAPI**
**Explorer**, and selecting **API Integration** > **SDK Examples**.

**Important**

We do not recommend downloading SDKs directly from the SDK Center for use in Apsara Stack scenarios. The public cloud SDKs may not support Apsara Stack APIs and may have compatibility issues. Please use with caution!

**Background information**

Currently, only the RPC method is supported for API calls.

**CommonRequest call example**

Example interface information: Product (ECS), Interface (DescribeInstances), Version (2014- 05-26). Sample code is as follows:

```java
from aliyunsdkcore.client import AcsClient import os from aliyunsdkcore.request import CommonRequest
# Create AcsClient instance
client = AcsClient(
    "<AccessKey ID>",
    "<AccessKey Secret>",
    "<your-RegionID>",
    timeout=1000,  # Set timeout
    verify=False, # Ignore certificate or verify='<certificate location>'
```

);

```python
# Use with https
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def describe_api_groups():
    # Create request and set parameters
```

e API calls

```bash
    request = CommonRequest()
    # When using sts ak to call rpc interface, you need to add SecurityToken field in p
arameters
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-
SecurityToken>"};
    params = {"PageSize":"10","PageNumber":"1"};
    request.set_query_params(params)
    headers = {
        # Required, call source description
        "x-acs-caller-sdk-source":"ApiTestDemo",
        # Optional, required for historical versions before Enterprise Edition V3.15.0
        "x-acs-regionid":"<your-RegionID>",
        # Optional, resource set ID
        "x-acs-resourcegroupid":"<your-ResourceGroupID>",
        # Required, organization ID
        "x-acs-organizationid":"<your-OrganizationID>"
        # Optional, required for modify & delete operations
        # "x-acs-instanceid":"<your-InstanceID>"
```

`}`

```python
    request.set_headers(headers)
    request.set_version("2016-07-14")
    request.set_action_name("DescribeApiGroups")
    request.set_endpoint("<ApigatewayEndpoint>")   //Please replace Endpoint with the r
eal address
    request.set_product("apigateway")
    request.set_method("POST")
    # Initiate API request and display return value
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    describe_api_groups()
```

**Set proxy**

When calling APIs, you may need to set HTTP_PROXY and HTTPS_PROXY through environment variables. Sample code is as follows:

```bash
# https proxy
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# http proxy
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

**HTTPS configuration**

e API calls The following describes how to access OpenAPI using HTTPS protocol.

**Using HTTPS protocol**

SDK uses HTTPS protocol by default.

```
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Region ID
```

`)`

```
request = DescribeInstancesRequest() request.set_protocol_type('https') # Use https client.do_action_with_exception(request)
```

**Ignore certificate**

**Important**

When accessing OpenAPI using HTTPS protocol, the SDK will verify SSL/TLS certificate validity by default. If your code environment does not have a certificate environment, it will report a certificate verification failure error. To ensure communication security in production environments, we recommend keeping verification enabled. If you must ignore certificate verification in a test environment, you can set it through the `verify` parameter.

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Region ID
    verify=False  # Ignore SSL certificate verification
```

`)`

**Specify CA certificate file**

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Region ID
    verify='./cacert.pem'  # Certification path
```

`)` rameters

## 3 API common parameters

**Common request parameters**

You must include common request parameters in all API requests. Table 1. Common request parameters

| Name | Type | Requi red | Description |
|---|---|---|---|
| Format | Strin g | No | The type of the returned value. Valid value: JSON. |
| Version | Strin g | Yes | The API version number in YYYY-MM-DD format. Valid values: Auditprivate: 2018-01-16. yundunnextsoc: 2019-07-23. Sas: 2018-12-03. aegis: 2016-11-11. yundun-css: 2021-10-11. secspy: 2019-08-05. Ddosprivate: 2018-01-16. hsm-private: 2018-06-30. Cloudfw: 2017-12-07. Sddp: 2019-01-03. semawaf: 2020-07-01. soar: 2018-12-03. |
| AccessKeyId | Strin g | Yes | The AccessKey ID that is used to access the service. |
| AccessKeySe cret | Strin g | Yes | The AccessKey secret that is used to access the service. |
| RegionId | Strin g | Yes | The region ID of the service. |
| Product | Strin g | Yes | The name of the service to which the operation belongs. Valid values: Auditprivate: Alibaba Cloud Security basic component. yundunnextsoc: Security Operations Center (SOC). Sas: Threat Detection Service. aegis: Server Guard. yundun-css: Container Protection. secspy: Network Traffic Detection and Response. Ddosprivate: DDoS traffic scrubbing. hsm-private: Cloud Hardware Security Module (CloudHSM). Cloudfw: Cloud Firewall. Sddp: Sensitive Data Protection. semawaf: Web Application Firewall. soar: Security Operations Center (SOC)-Orchestration and Response. |

rameters

| EndpointPre | Strin g | Yes | The prefix in the endpoint of the service to which the operation belongs. Valid values: auditprivate: Alibaba Cloud Security basic component. yundunnextsoc-pop: Security Operations Center (SOC). tds: Threat Detection Service. aegis: Server Guard. yundun-css: Container Protection. secspy-share: Network Traffic Detection and Response. ddosprivate: DDoS traffic scrubbing. hsmprivate: Cloud Hardware Security Module (CloudHSM). cloudfw: Cloud Firewall. sddp-api: Sensitive Data Protection. semawaf: Web Application Firewall. soar: Security Operations Center (SOC)-Orchestration and Response. |
|---|---|---|---|

**Common response parameters**

Responses are returned in the HTTP response format: A 2xx HTTP status code indicates a successful call. A 4xx or 5xx HTTP status code indicates a failed call. Responses are returned in the JSON format. Every response returns a unique RequestId regardless of whether the call is successful.

## 4 Cloud Firewall

### 4.1 Invocation method

#### 4.1.1 Request structure

Apsara Stack Security API operations use the RPC protocol. This topic describes the structure of API requests. You can call Apsara Stack Security API operations by sending HTTP requests. The request syntax is as follows:

```
http://endpoint/?Action=xx&parameters
```

where:

|   | endpoint |   | : The endpoin |
|---|---|---|---|
| [RegionId].example.com |   |   |   |
|   | Action | : the name of t |   |

`endpoint` : The endpoint of the Web Application Firewall (WAF) API is `semawaf.` `Action` : the name of the operation being performed. For example, to query the Apsara Stack Security features that are deployed, you must set the Action parameter to DescribeFeatures. `parameters` : the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operationspecific parameters. Common parameters include information such as the API version number and authentication information. For more information about operation-specific parameters, see the corresponding operation description. The following example demonstrates how to call the DescribeFeatures operation to query the Apsara Stack Security features that are deployed:

```
https://yundunprivate.[RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-t est&Format=JSON&SecureTransport=true&SignatureMethod=HMAC- SHA1&SignatureNonce=15215528852396&SignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018- 03-02Txxxxxxx&Version=2018-01-16&Signature=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```
https://yundunprivate.[RegionId].example.com/?Action=DescribeFeatures &Format=JSON &Version=2020-07-01 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 4.1.2 Request signatures

Apsara Stack Security authenticates each access request. Therefore, a request must contain signature information regardless of whether it is sent over HTTP or HTTPS.

**Authorization**

To ensure the security of your account, we recommend that you use a RAM user to call API operations. Before you use a RAM user to call an API operation, you must grant the RAM user the required permissions by creating an policy and attaching the policy to the RAM user.

**Signature**

You must sign all API requests to ensure security. Alibaba Cloud uses the request signature to verify the identity of the API caller. When you manually make an API request, you must use the AccessKey secret to calculate an HMAC value based on the encoded and sorted request string. The HMAC value is the signature. For more information, see the definition in RFC 2104. The following parameters are used in the following procedure to describe how to calculate a signature.

| Parameter | Description |
|---|---|
| Endpoint | http://tds.[RegionId].example.com/? |
| Operation-specific parameters | Action=DescribeFeatures |
| Common parameters except Signature | &Timestamp=2018-12-24T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2018-12-03 &SignatureVersion=1.0 |
| Access Key Secret | <yourAccessKeySecret> |

1. Create a canonicalized query string by arranging the request parameters.

**Note**

The request parameters include operation-specific parameters and all common request parameters except Signature. i. Sort the request parameters. Sort the request parameters in alphabetical order. ii. Encode the parameters. Encode the canonicalized query string in UTF-8 based on the following rules: Uppercase letters, lowercase letters, digits, and some special characters such as hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded. Other characters must be percent encoded in the %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22. Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20. Do not encode spaces as plus signs (+). iii. Connect the encoded parameter names and values by using equal signs (=). iv. Sort the pairs of parameter names and values that are connected by using equal signs (=) in alphabetical order. Connect the pairs with ampersands (&) to create a canonicalized query string.
2. Create a string-to-sign from the encoded canonicalized query string based on the following
rule:

```
StringToSign=HTTPMethod + "&" + percentEncode("/") + "&" + percentEncode(CanonicalizedQueryString)
```

3. Calculate the HMAC value of the string-to-sign based on the HMAC definition in RFC 2104.

**Note**

Your AccessKey secret in combination with an ampersand (&) (ASCII:38) is used as the key for the HMAC calculation. The SHA1 algorithm is used to calculate the HMAC value of the string-to-sign.
4. Encode the HMAC value in Base64 to obtain the signature string.

```
LEW8N4y7Uasop******
```

5. Add the signature string to the request as the Signature parameter. The result is the signed
API request.

#### 4.1.3 Common parameters

Common request parameters must be included in all Apsara Stack Security API requests, such as the API version number and authentication information.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The version number of the API. The value is in the format of YYYY-MM-DD. Set the value to 2018-01-16. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014 (UTC+8). |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |

| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
|---|---|---|---|
| ResourceOwnerA ccount | String | No | The owner account (the logon username) of the resource you want to access by using this API request. |
| Format | String | No | The format of the response. Valid values: JSON and XML. Default value: XML. |

#### 4.1.4 Response structure

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

`{`

```json
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216", /* Returned data */
```

`}`

### 4.2 Firewall switch

#### 4.2.1 PutEnableFwSwitch

Enables a firewall for specific assets.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutEnableFwSwi tch | The operation that you want to perform. Set the value to PutEnableFwSwitch |

| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
|---|---|---|---|---|
| Lang | String | No | zh | The language of the content in the request and response messages. zh: Chinese en: English |
| IpaddrList.N | RepeatL ist | No | ["1.2.3.4","5.6.7. 8"] | The list of IP addresses. |
| RegionList.N | RepeatL ist | No | ["cn- hangzhou","cn- shanghai"] | The list of regions. |
| ResourceTypeLis t.N | RepeatL ist | No | ["EcsPublicIp","N atEip"] | The list of asset types. Valid values: BastionHostIP (Bastionhost) EcsEIP (ECS EIP) EcsPublicIP (public IP addresses of Elastic Compute Service (ECS) instances) EIP EniEIP (EIP of elastic network interfaces (ENIs)) NatEIP (NAT EIP) SlbEIP (SLB EIP) SlbPublicIP (SLB public IP) NatPublicIP (NAT public IP) HAVIP (HA VIP) |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B2841452-CB8D- 4F7D-B247- 38E1CF73**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutEnableFwSwitch&IpaddrList=["1.2.3.4","5.6.7.8"] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF73****</RequestId>
```

`JSON` format

```json
{"RequestId":"B2841452-CB8D-4F7D-B247-38E1CF73****"}
```

#### 4.2.2 PutDisableFwSwitch

Turns off a firewall switch.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutDisableFwSwi tch | The operation that you want to perform. Set the value to PutDisableFwSwitch |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The language of the content in the request and response messages. zh: Chinese en: English |
| IpaddrList.N | RepeatL ist | No | ["1.2.3.4","5.6.7. 8"] | The list of IP addresses. |
| RegionList.N | RepeatL ist | No | ["cn- hangzhou","cn- shanghai"] | The list of regions. |
| ResourceTypeLis t.N | RepeatL ist | No | ["EcsPublicIp","N atEip"] | The list of asset types. Valid values: BastionHostIP (Bastionhost) EcsEIP (ECS EIP) EcsPublicIP (public IP addresses of Elastic Compute Service (ECS) instances) EIP EniEIP (EIP of elastic network interfaces (ENIs)) NatEIP (NAT EIP) SlbEIP (SLB EIP) SlbPublicIP (SLB public IP) NatPublicIP (NAT public IP) HAVIP (HA VIP) |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | B2841452-CB8D- 4F7D-B247- 38E1CF73**** | The ID of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutDisableFwSwitch&IpaddrList=["1.2.3.4","5.6.7.8"] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF73****</RequestId>
```

`JSON` format

```json
{"RequestId":"B2841452-CB8D-4F7D-B247-38E1CF73****"}
```

#### 4.2.3 PutEnableAllFwSwitch

Enables all firewall switches.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutEnableAllFwS witch | The operation that you want to perform. Set the value to PutEnableAllFwSwitch |
| SourceIp | String | No | 1.XX.XX.4 | The source IP address of the request. |
| Lang | String | No | zh | The language of the content in the request and response messages. zh: Chinese en: English |
| InstanceId | String | No | i-**** | The ID of the ECS instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B2841452-CB8D- 4F7D-B247- 38E1CF73**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutEnableAllFwSwitch &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF73****</RequestId>
```

`JSON` format

```json
{"RequestId":"B2841452-CB8D-4F7D-B247-38E1CF73****"}
```

#### 4.2.4 PutDisableAllFwSwitch

Turns off all firewall switches.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutDisableAllFw Switch | The operation that you want to perform. Set the value to PutDisableAllFwSwitch. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The language of the content in the request and response messages. zh: Chinese en: English |
| InstanceId | String | No | i-**** | The ID of the ECS instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B2841452-CB8D- 4F7D-B247- 38E1CF73**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutDisableAllFwSwitch &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF73****</RequestId>
```

`JSON` format

```json
{"RequestId":"B2841452-CB8D-4F7D-B247-38E1CF73****"}
```

#### 4.2.5 UpdateResourceDetails

Updates the details of a resource in Cloud Firewall.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | No | 192.0.x.x | The source IP address of the access request. |
| Lang | Strin g | Query | No | zh | The language of the response message. Valid values: zh (default): Chinese. en: English. |
| Desc | Strin g | Query | No | Description of the traffic redirection configuration | The business description. |
| IpaddrList | Repe atList | Query | No | ["192.0.X.X","192.0.X.X"] | The list of IP addresses. IpaddrList, RegionList, and ResourceTypeList cannot all be empty. Specify a value for at least one of these parameters. |
| RegionList | Repe atList | Query | No | ['cn-wulan-env182- amtest182001-a'] | The list of regions. |

|   | Cloud Security | Firewall |   |   | Dev | eloper Guide·Cloud Firewal | l |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ResourceT ypeList | Repe atList | Query | No | [eip] | The list of resource types. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2C29FE9D-14D8- 4DF8-A3CC- 6B62B4F0DECF | The ID of the request. |

**Examples**

Request example

```
http(s)://[Endpoint]/?Action=UpdateResourceDetails &Common request parameters
```

Response example `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"2C29FE9D-14D8-4DF8-A3CC-6B62B4F0DECF"
```

`}`

#### 4.2.6 PutEnableAllResourceFwSwitch

Enables or disables all resource switches for Cloud Firewall.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | No | 192.0.x.x | The source IP address of the request. |

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Lang | Strin g | Query | No | zh | The language of the response message. Valid values: `zh` (Chinese) and `en` (English). Default value: `zh`. |
| InstanceId | Strin g | Query | No | **** | The instance ID. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2C29FE9D-14D8- 4DF8-A3CC- 6B62B4F0DECF | The ID of the request. |

**Examples**

Request example

```
http(s)://[Endpoint]/?Action=PutEnableAllResourceFwSwitch &<Common request parameters>
```

Response example `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"2C29FE9D-14D8-4DF8-A3CC-6B62B4F0DECF"
```

`}`

#### 4.2.7 PutDisableAllResourceFwSwitch

Disables protection for all resources in Cloud Firewall.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | No | 192.0.x.x | The source IP address of the request. |
| Lang | Strin g | Query | No | zh | The language of the response message. Valid values: zh (Chinese) and en (English). The default value is zh. |
| InstanceId | Strin g | Query | No | **** | The instance ID. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2C29FE9D-14D8- 4DF8-A3CC- 6B62B4F0DECF | The ID of the request. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=PutDisableAllResourceFwSwitch &Common request parameters
```

Sample response `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"2C29FE9D-14D8-4DF8-A3CC-6B62B4F0DECF"
```

`}`

### 4.3 VPC firewalls

#### 4.3.1 CreateVpcFirewallControlPolicy

Creates an access control policy to a specific policy group for a VPC firewall.

**Note**

The VPC firewall instances that are used to protect each Cloud Enterprise Network (CEN) instance and each Express Connect use different access control policies.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpcFirew allControlPolicy | The operation that you want to perform. Set the value to CreateVpcFirewallControlPolicy. |
| AclAction | String | Yes | accept | The action that the VPC firewall performs on the traffic. Valid values: accept: allows the traffic. drop: denies the traffic. log: monitors the traffic. |
| ApplicationNa me | String | Yes | HTTP | The type of the application to which the access control policy applies. Valid values: FTP HTTP HTTPS MySQL SMTP SMTPS RDP VNC SSH Redis MQTT MongoDB Memcache SSL ANY, which indicates all types of applications |
| Description | String | Yes | test | The description of the access control policy. |
| Destination | String | Yes | 80 | The destination port in the access control policy. Note If the DestPortType parameter is set to port, you must specify this parameter. |

| DestinationTy pe | String | Yes | net | The type of the destination address in the access control policy. net: CIDR block group: destination address book domain: destination domain name |
|---|---|---|---|---|
| NewOrder | String | Yes | -1 | The priority of the access control policy. The priority value starts from 1. A smaller value indicates a higher priority. Note The value -1 indicates the lowest priority. |
| Proto | String | Yes | TCP | The type of the security protocol in the access control policy. If you are not sure about the protocol type, you can set this parameter to ANY. TCP UDP ICMP |
| Source | String | Yes | 10.2.3.0/24 | The source address in the access control policy. If the SourceType parameter is set to net , the value of this parameter is the source CIDR block. Example: 10.2.3.0/24. If the SourceType parameter is set to group , the value of this parameter is the name of the source address book. Example: db group. _ |
| SourceType | String | Yes | net | The type of the source address in the access control policy. Valid values: net: source CIDR block group: source address book |

| VpcFirewallId | String | Yes | vfw- a42bbb7b88714 8c9**** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. Valid values: If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used. Example: cen- ervw5jbw1234*****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw- a42bbb748c91234*****. |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| DestPort | String | No | 80 | The destination port in the access control policy. Note If the DestPortType parameter is set to port , you must specify this parameter. |
| DestPortType | String | No | net | The type of the destination port in the access control policy. port group: port address book |
| DestPortGroup | String | No | my port group _ _ | The name of the destination port address book in the access control policy. Note If the DestPortType parameter is set to group , you must specify this parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclUuid | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

| RequestId | String | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateVpcFirewallControlPolicy &VpcFirewallId=vfw-a42bbb7b887148c9**** &AclAction=accept &ApplicationName=ANY &Description=demo_rule_1 &Destination=10.2.3.0/24 &DestinationType=net &NewOrder=-1 &Proto=TCP &Source=10.2.3.0/24 &SourceType=net &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateVpcFirewallControlPolicyResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
  <AclUuid>00281255-d220-4db1-8f4f-c4d*********</AclUuid>
</CreateVpcFirewallControlPolicyResponse>
```

`JSON` format `{`

```json
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D",
    "AclUuid": "00281255-d220-4db1-8f4f-c4d*********"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.2 DescribeVpcFirewallControlPolicy

Queries the information of the access control policies for a specific VPC firewall.

**Note**

The VPC firewall instances that are used to protect each Cloud Enterprise Network (CEN) instance and each Express Connect use different access control policies.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeVpcFire wallControlPolic y | The operation that you want to perform. Set the value to DescribeVpcFirewallControlPolic y. |
|---|---|---|---|---|
| CurrentPage | String | Yes | 1 | The page number of the current page. Default value: 1. |
| PageSize | String | Yes | 10 | The number of entries to return on each page. Maximum value: 50. |
| VpcFirewallId | String | Yes | vfw- a42bbb7b88714 8c9**** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. Valid values: If the VPC firewall is used to protect a CEN instance, the ID of the CEN instance is used. Example: cen-ervw0g12b5jbw****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw- a42bbb7b887148c9****. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Source | String | No | 10.0.1.0/24 | The source address in the access control policy. Fuzzy match is supported. Valid values: If the SourceType parameter is set to net , the value of this parameter is the source CIDR block. Example: 10.0.1.0/24. If the SourceType parameter is set to group , the value of this parameter is the name of the source address book. Example: db group. _ If the SourceType parameter is not specified, all sources are queried. Note The valid values of this parameter depend on the value of the SourceType parameter. |
|---|---|---|---|---|

| Destination | String | No | 10.0.3.0 | The destination address in the access control policy. Fuzzy match is supported. Valid values: If the DestinationType parameter is set to net , the value of this parameter is the destination CIDR block. Example: 10.0.3.0/24. If the DestinationType is set to domain , the value of this parameter is the destination domain name. Example: aliyun.com. If the DestinationType parameter is set to group , the value of this parameter is the name of the destination address book. Example: db group. _ If the DestinationType parameter is not specified, all destination addresses are queried. Note The valid values of this parameter depend on the value of the DestinationType parameter. |
|---|---|---|---|---|
| Description | String | No | test | The description of the access control policy. Fuzzy match is supported. Note If this parameter is not specified, the descriptions of all access control policies are queried. |
| Proto | String | No | TCP | The type of the protocol in the access control policy. Valid values: TCP UDP ICMP ANY, which indicates all types of protocols |

| AclAction | String | No | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept: allows the traffic. drop: denies the traffic. log: monitors the traffic. If this parameter is not specified, access control policies that specify all the preceding actions are queried. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Policys | Array |   | The information of the access control policy. |
| AclAction | String | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept: allows the traffic. drop: denies the traffic. log: monitors the traffic. |
| AclUuid | String | 00281255-d220- 4db1-8f4f- c4df221a**** | The ID of the access control policy. |
| ApplicationId | String | 10** | The application ID in the access control policy. |

| ApplicationNa me | String | HTTP | The type of the application that the access control policy supports. Valid values: HTTP HTTPS MySQL SMTP SMTPS RDP VNC SSH Redis MQTT MongoDB Memcache SSL ANY, which indicates all types of applications |
|---|---|---|---|
| Description | String | test | The description of the access control policy. |
| DestPort | String | 80 | The destination port in the access control policy. |
| DestPortGroup | String | my port group _ _ | The name of the destination port address book in the access control policy. |
| DestPortGroup Ports | List | [80,443] | The ports in the destination port address book. |
| DestPortType | String | port | The type of the destination port in the access control policy. Valid values: port group: port address book |

| Destination | String | 10.0.3.0/24 | The destination address in the access control policy. Valid values: If the DestinationType parameter is set to net , the value of this parameter is the destination CIDR block. Example: 10.0.3.0/24. If the DestinationType parameter is set to domain , the value of this parameter is the destination domain name. Example: aliyuncs.com. If the DestinationType parameter is set to group , the value of this parameter is the name of the destination address book. Example: db group. _ Note The valid values of this parameter depend on the value of the DestinationType parameter. |
|---|---|---|---|
| DestinationGro upCidrs | List | ["10.0.4.0/24", "10.0.0.1/32"] | The CIDR blocks in the destination address book. |
| DestinationTy pe | String | net | The type of the destination address in the access control policy. Valid values: net: destination CIDR block group: destination address book domain: destination domain name |
| Direction | String | in | The direction of traffic to which the access control policy applies. Valid values: in: inbound traffic out: outbound traffic |
| HitTimes | Integer | 100 | The number of hits for the access control policy. |

| Order | Integer | 1 | The priority of the access control policy. The priority value starts from 1. A smaller value indicates a higher priority. The value -1 indicates the lowest priority. |
|---|---|---|---|
| Proto | String | TCP | The type of the protocol in the access control policy. Valid values: TCP UDP ICMP ANY, which indicates all types of protocols |
| Source | String | 10.0.6.0/24 | The source address in the access control policy. Valid values: If the SourceType parameter is set to net , the value of this parameter is the source CIDR block. Example: 10.0.6.0/24. If the SourceType parameter is set to group , the value of this parameter is the name of the source address book. Example: db group. _ Note The valid values of this parameter depend on the value of the SourceType parameter. |
| SourceGroupCi drs | List | ["10.0.6.0/24", "10.0.0.2/32"] | The CIDR blocks in the source address book of the access control policy. |
| SourceType | String | net | The type of the source address in the access control policy. Valid values: net: source CIDR block group: source address book |
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |
| TotalCount | String | 20 | The total number of the access control policies. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpcFirewallControlPolicy &VpcFirewallId=vfw-a42bbb7b887148c9**** &CurrentPage=1 &PageSize=10 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpcFirewallControlPolicyResponse>
  <TotalCount>1</TotalCount>
  <PageNo>1</PageNo>
  <PageSize>10</PageSize>
  <RequestId>A08BC58F-A83D-43EB-BC31-2F0D723929CC</RequestId>
  <Policys>
        <ApplicationName>HTTP</ApplicationName>
        <Description>11</Description>
        <HitTimes>0</HitTimes>
        <DestinationType>net</DestinationType>
        <SourceType>net</SourceType>
        <Proto>TCP</Proto>
        <Order>5</Order>
        <ApplicationId>27</ApplicationId>
        <DestPortType>port</DestPortType>
        <Source>10.1.1.1/32</Source>
        <DestPort>80/80</DestPort>
        <AclAction>accept</AclAction>
        <AclUuid>53d82f0e-9bf1-4761-ab3b-a070b4811234</AclUuid>
        <Destination>10.2.1.1/32</Destination>
  </Policys>
</DescribeVpcFirewallControlPolicyResponse>
```

`JSON` format `{`

```json
    "TotalCount":1,
    "PageNo":1,
    "PageSize":10,
    "RequestId":"A08BC58F-A83D-43EB-BC31-2F0D723929CC",
    "Policys":[
```

`{`

```json
            "DestinationGroupCidrs":[
```

`],`

```json
            "SourceGroupCidrs":[
```

`],`

```json
            "ApplicationName":"HTTP",
            "Description":"11",
            "HitTimes":0,
            "DestinationType":"net",
            "SourceType":"net",
            "Proto":"TCP",
            "Order":5,
            "ApplicationId":"27",
            "DestPortType":"port",
            "Source":"10.1.1.1/32",
            "DestPort":"80/80",
            "AclAction":"accept",
            "DestPortGroupPorts":[
```

`],`

```json
            "AclUuid":"53d82f0e-9bf1-4761-ab3b-a070b4811234",
            "Destination":"10.2.1.1/32"
```

`}` `]` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.3 ModifyVpcFirewallControlPolicy

Modifies the configuration of an access control policy in a specific policy group for a VPC firewall.

**Note**

The VPC firewall instances that are used to protect each Cloud Enterprise Network (CEN) instance and each Express Connect use different access control policies.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | ModifyVpcFirew allControlPolicy | The operation that you want to perform. Set the value to ModifyVpcFirewallControlPolicy. |
|---|---|---|---|---|
| AclAction | String | Yes | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept: allows the traffic. drop: denies the traffic. log: monitors the traffic. |
| AclUuid | String | Yes | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. To modify the configuration of an access control policy, you must provide the ID of the policy. You can call the DescribeVpcFirewallControlPolicy operation to obtain the ID. |
| ApplicationNa me | String | Yes | HTTP | The type of applications to which the access control policy applies. Valid values: ANY FTP HTTP HTTPS MySQL SMTP SMTPS RDP VNC SSH Redis MQTT MongoDB Memcache SSL ANY, which indicates all types of applications |
| Description | String | Yes | test | The description of the access control policy. |

| Destination | String | Yes | 10.2.3.0/24 | The destination address in the access control policy. If the DestinationType parameter is set to net , the value of this parameter is the destination CIDR block. Example: 10.2.3.0/24. If the DestinationType parameter is set to group , the value of this parameter is the name of the destination address book. Example: db group. _ If the DestinationType parameter is set to domain , the value of this parameter is the destination domain name. Example: *.aliyuncs.com. |
|---|---|---|---|---|
| DestinationTy pe | String | Yes | net | The type of the destination address in the access control policy. Valid values: net: CIDR block group: destination address book domain: destination domain name |
| Proto | String | Yes | TCP | The type of the security protocol in the access control policy. Valid values: ANY, which indicates all types of protocols TCP UDP ICMP |

| Source | String | Yes | 10.2.4.0/24 | The source address in the access control policy. Valid values: If the SourceType parameter is set to net , the value of this parameter is the source CIDR block. Example: 10.2.4.0/24 If the SourceType parameter is set to group , the value of this parameter is the name of the source address book. Example: db group _ |
|---|---|---|---|---|
| SourceType | String | Yes | net | The type of the source address in the access control policy. Valid values: net: source CIDR block. group: source address book |
| VpcFirewallId | String | Yes | vfw- a42bbb7b88714 8c9**** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used. Example: cen-ervw0g12b5jbw****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw- a42bbb7b887148c9****. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| DestPort | String | No | 80 | The destination port in the access control policy. |

| DestPortType | String | No | port | The type of the destination port in the access control policy. port group: port address book |
|---|---|---|---|---|
| DestPortGroup | String | No | my port group _ _ | The name of the destination port address book in the access control policy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVpcFirewallControlPolicy &VpcFirewallId=vfw-a42bbb7b887148c9**** &AclAction=accept &AclUuid=00281255-d220-4db1-8f4f-c4df221ad84c &ApplicationName=ANY &Description=demo_rule_1 &Destination=10.2.3.0/24 &DestinationType=net &Proto=TCP &Source=10.2.4.0/24 &SourceType=net &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVpcFirewallControlPolicyResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</ModifyVpcFirewallControlPolicyResponse>
```

`JSON` format `{`

```json
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.4 ModifyVpcFirewallControlPolicyPosition

Modifies the priority of an access control policy in a specific policy group for a VPC firewall.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpcFirew allControlPolicyP osition | The operation that you want to perform. Set the value to ModifyVpcFirewallControlPolicyP osition. |
| NewOrder | String | Yes | 1 | The new priority of the access control policy. |
| OldOrder | String | Yes | 5 | The original priority of the access control policy. |
| VpcFirewallId | String | Yes | vfw- a42bbb7b88714 8c9**** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. Valid values: If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used. Example: cen-ervw0g12b5jbw****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw- a42bbb7b887148c9****. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 850A84D6-0DE4- 4797-A1E8- 00090125EEB1 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVpcFirewallControlPolicyPosition &VpcFirewallId=vfw-a42bbb7b887148c9**** &NewOrder=1 &OldOrder=5 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVpcFirewallControlPolicyPositionResponse>
  <RequestId>850A84D6-0DE4-4797-A1E8-00090125EEB1</RequestId>
</ModifyVpcFirewallControlPolicyPositionResponse>
```

`JSON` format `{`

```json
    "RequestId": "850A84D6-0DE4-4797-A1E8-00090125EEB1"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.5 DeleteVpcFirewallControlPolicy

Deletes an access control policy from a specific policy group for a VPC firewall.

**Note**

The VPC firewall instances that are used to protect each Cloud Enterprise Network (CEN) instance and each Express Connect use different access control policies.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpcFirewa llControlPolicy | The operation that you want to perform. Set the value to DeleteVpcFirewallControlPolicy. |
| AclUuid | String | Yes | 00281255-d220- 4db1-8f4f- c4df2214**** | The ID of the access control policy. To delete an access control policy, you must specify the ID of the policy. You can call the DescribeVpcFirewallControlPolic y operation to obtain the ID. |

| VpcFirewallId | String | Yes | vfw- a42bbb7b88714 8c91**** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. Valid values: If the VPC firewall is used to protect a CEN instance, the ID of the CEN instance is used. Example: cen-ervw0g12b5jbw****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw- a42bbb7b887148c9****. |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVpcFirewallControlPolicy &VpcFirewallId=vfw-a42bbb7b887148c9**** &AclUuid=00281255-d220-4db1-8f4f-c4df221ad84c &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVpcFirewallControlPolicyResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</DeleteVpcFirewallControlPolicyResponse>
```

`JSON` format `{`

```json
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.6 DescribeVpcFirewallPolicyPriorUsed

Queries the priority range of the access control policies in a specific policy group for a VPC firewall.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpcFire wallPolicyPriorUs ed | The operation that you want to perform. Set the value to DescribeVpcFirewallPolicyPriorU sed. |
| VpcFirewallId | String | Yes | vfw- a42bbb7b88714 8c9**** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. Valid values: If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used. Example: cen-ervw0g12b5jbw****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw- a42bbb7b887148c9****. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| End | Integer | 150 | The lowest priority for the access control policy. |

| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |
|---|---|---|---|
| Start | Integer | 1 | The highest priority for the access control policy. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpcFirewallPolicyPriorUsed &VpcFirewallId=vfw-a42bbb7b887148c9**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpcFirewallPolicyPriorUsedResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
  <Start>1</Start>
  <End>150</End>
</DescribeVpcFirewallPolicyPriorUsedResponse>
```

`JSON` format `{`

```json
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D",
    "Start": 1,
    "End": 150
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.7 DescribeVpcFirewallAclGroupList

Queries information about all access control policy groups for a VPC firewall.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpcFire wallAclGroupList | The operation that you want to perform. Set the value to DescribeVpcFirewallAclGroupList . |

| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
|---|---|---|---|---|
| FirewallConfig ureStatus | String | No | configured | Specifies whether VPC firewalls are configured. notconfigured: VPC firewalls are not configured. configured: VPC firewalls are configured. If you do not specify this parameter, all access control policy groups are queried. |
| CurrentPage | String | No | 1 | The page number of the current page. Default value: 1 |
| PageSize | String | No | 10 | The number of entries to return on each page. Maximum value: 50. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclGroupList | Array |   | The information about the access control policy group. |
| AclGroupId | String | vfw- a42bbb7b887148c 9**** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. Valid values: If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used. Example: cen-ervw0g12b5jbw****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw-a42bbb7b887148c9****. |

| AclGroupName | String | group test _ | The name of the access control policy group. If the VPC firewall is used to protect a CEN instance, the name of the CEN instance is used. If the VPC firewall is used to protect an Express Connect, the name of the VPC firewall is used. |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |
| TotalCount | Integer | 1 | The total number of access control policy groups. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpcFirewallAclGroupList &FirewallConfigureStatus=configured &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpcFirewallAclGroupListResponse>
  <TotalCount>1</TotalCount>
  <AclGroupList>
        <AclGroupId>vfw-a42bbb7b887148c9****</AclGroupId>
        <AclGroupName>group_test</AclGroupName>
  </AclGroupList>
</DescribeVpcFirewallAclGroupListResponse>
```

`JSON` format

```json
{"TotalCount":1,"AclGroupList":[{"AclGroupId":"vfwa42bbb7b887148c9****","AclGroupName":"group_test"}]}
```

**Error codes**

For a list of error codes, see Error codes.

#### 4.3.8 ResetVpcFirewallRuleHitCount

Resets the count on hits of an access control policy in a specific policy group for a VPC firewall.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetVpcFirewal lRuleHitCount | The operation that you want to perform. Set the value to ResetVpcFirewallRuleHitCount. |
| AclUuid | String | Yes | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. To delete an access control policy, you must specify the ID of the policy. You can call the DescribeVpcFirewallControlPolicy operation to obtain the ID. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ResetVpcFirewallRuleHitCount &AclUuid=00281255-d220-4db1-8f4f-c4df221a1234 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ResetVpcFirewallRuleHitCountResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</ResetVpcFirewallRuleHitCountResponse>
```

`JSON` format `{`

```json
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

### 4.4 Access control

#### 4.4.1 DescribePolicyPriorUsed

Queries the priority range of access control policies that match specific query conditions.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePolicyPr iorUsed | The operation that you want to perform. Set the value to DescribePolicyPriorUsed. |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic. out: outbound traffic. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The language of the content in the request and response messages. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| End | Integer | 150 | The lowest priority of existing access control policies. Note -1 indicates the lowest priority. |
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2**** | The ID of the request. |

| Start | Integer | 1 | The highest priority of existing access control policies. Note 0 indicates the highest priority. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePolicyPriorUsed &Direction=in &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2****</RequestId> <Start>1</Start> <End>150</End>
```

`JSON` format

```json
{"RequestId":"CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2****","Start":"1","End":"150"}
```

#### 4.4.2 ModifyControlPolicyPosition

Modifies the priority of an access control policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyControlPol icyPosition | The operation that you want to perform. Set the value to ModifyControlPolicyPosition. |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. in: inbound traffic out: outbound traffic |
| NewOrder | String | Yes | 1 | The new priority of the access control policy. |
| OldOrder | String | Yes | 5 | The original priority of the access control policy. |

| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
|---|---|---|---|---|
| Lang | String | No | zh | The language of the content in the request and response messages. zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 850A84D6-0DE4- 4797-A1E8- 00090125**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyControlPolicyPosition &Direction=in &NewOrder=1 &OldOrder=5 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>850A84D6-0DE4-4797-A1E8-00090125****</RequestId>
```

`JSON` format

```json
{"RequestId":"850A84D6-0DE4-4797-A1E8-00090125****"}
```

#### 4.4.3 DescribeControlPolicy

Queries information about all access control policies.

**Request parameters**

| Name | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeControl Policy | The operation that you want to perform. Set the value to DescribeControlPolicy. |

| CurrentPage | String | Yes | 1 | The page number of the current page. Default value: 1. |
|---|---|---|---|---|
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out: outbound traffic |
| PageSize | String | Yes | 10 | The number of entries to return on each page. Maximum value: 50. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The language of the content in the request and response messages. Valid values: zh: Chinese en: English |
| Source | String | No | 1.2.3.5 | The source address in the access control policy. Fuzzy match is supported. Valid values: Source CIDR block (when SourceType is set to net ) Example: 10.0.1.0/24 Source address book name (when SourceType is set to group ) Example: db group _ Source location (when SourceType is set to location ) Example: beijing (You can use Chinese or English for the query) Empty (indicates that all access control sources are queried) Note The valid values of this parameter depend on the value of the SourceType parameter. |

| Destination | String | No | 1.2.3.0 | The destination address in the access control policy. Fuzzy match is supported. Valid values: Destination CIDR block (when DestinationType is set to net ) Example: 10.0.3.0/24 Destination domain name (when DestinationType is set to domain ) Example: aliyun Destination address book name (when DestinationType is set to group ) For example: db group is empty _ (this queries the destination addresses of all access control policies). Destination location (when DestinationType is set to location ) Example: beijing (You can use Chinese or English for the query) Empty (indicates that all destination addresses in access control policies are queried) Note The valid values of this parameter depend on the value of the DestinationType parameter. |
|---|---|---|---|---|
| Description | String | No | test | The description of the access control policy. Fuzzy match is supported. Note If this parameter is left empty, the descriptions of all access control policies are queried. |

| Proto | String | No | TCP | The type of protocol in the access control policy. Valid values: TCP UDP ICMP ANY (indicates all types of protocols) Empty (indicates all types of protocols) |
|---|---|---|---|---|
| AclAction | String | No | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept: allows the traffic drop: deny log: observation Empty: all action types |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| PageNo | String | 1 | The page number of the current page. |
| PageSize | String | 10 | The number of entries returned per page. |
| Policys | Array of DataItem |   | The information about the access control policy. |
| AclAction | String | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept: allows the traffic drop: denies the traffic log: observation |
| AclUuid | String | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. |
| ApplicationId | String | 10*** | The application ID in the access control policy. |

| ApplicationNa me | String | HTTP | The type of the application that the access control policy supports. Valid values: FTP HTTP HTTPS Memcache MongoDB MQTT MySQL RDP Redis SMTP SMTPS SSH SSL VNC ANY (indicates all types of applications) |
|---|---|---|---|
| Description | String | test | The description of the access control policy. |
| DestPort | String | 80 | The destination port in the access control policy. |
| DestPortGroup | String | my port group _ _ | The name of the destination port address book in the access control policy. |
| DestPortGroup Ports | List | [80,443] | The ports in the destination port address book. |
| DestPortType | String | port | The type of the destination port in the access control policy. Valid values: port: port group: port address book |

| Destination | String | 1.2.3.4/24 | The destination address in the access control policy. Valid values: Destination IP address or CIDR block (when DestinationType is set to net) Example: 10.0.3.0/24 Destination domain name (when DestinationType is set to domain) Example: aliyuncs.com Destination address book name (when DestinationType is set to group) Example: db group _ Destination location name (when DestinationType is set to location; for more information about location codes, see AddControlPolicy) Example: ["BJ11", "ZB"] Note The valid values of this parameter depend on the value of the DestinationType parameter. |
|---|---|---|---|
| DestinationGro upCidrs | List | ["1.2.3.0/24", "1.2.3.1/32"] | The CIDR blocks in the destination address book. |
| DestinationGro upType | String | ip | The type of the destination address book in the access control policy. Valid values: ip: an address book that includes one or more IP addresses tag: an address book that includes one or more IP addresses with ECS tags domain: an address book that includes one or more domain names threat: an address book that includes one or more malicious IP addresses or domain names backsrc: an address book that includes one or more back-to-origin addresses of Anti-DDoS Pro or Anti-DDoS Premium instances or WAF instances |

| DestinationTy pe | String | net | The type of the destination address in the access control policy. Valid values: net: destination CIDR block group: destination address book domain: destination domain name location: destination location |
|---|---|---|---|
| Direction | String | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out: outbound traffic |
| DnsResult | String | 1.1.1.1,2.2.2.2 | The DNS resolution result. |
| DnsResultTime | Long | 1579261141 | The timestamp of the DNS resolution result. |
| HitTimes | Integer | 100 | The number of hits for the access control policy. |
| Order | Integer | 1 | The priority of the access control policy. The priority value starts from 1. A smaller priority value indicates a higher priority. Note －1 indicates the lowest priority. |
| Proto | String | TCP | The type of the protocol in the access control policy. Valid values: ANY TCP UDP ICMP |

| Release | String | true | Indicates whether the access control policy is enabled. By default, an access control policy is enabled after it is created. Valid values: true: The access control policy is enabled. false: The access control policy is disabled. |
|---|---|---|---|
| Source | String | 1.2.3.0/24 | The source address in the access control policy. Valid values: Source CIDR block (when SourceType is set to net ) Example: 10.0.1.0/24 Source address book name (when SourceType is set to group ) Example: db group _ Source location (when SourceType is set to location; for more information about location codes, see AddControlPolicy) |
| SourceGroupCi drs | List | ["10.0.0.0/24", "10.0.0.1/32"] | The CIDR blocks in the source address book. |
| SourceGroupT ype | String | ip | The type of the source address book in the access control policy. Valid values: ip: an address book that includes one or more IP addresses tag: an address book that includes one or more IP addresses with ECS tags domain: an address book that includes one or more domain names threat: an address book that includes one or more malicious IP addresses or domain names backsrc: an address book that includes one or more back-to-origin addresses of Anti-DDoS Pro or Anti-DDoS Premium instances or WAF instances |

| SourceType | String | net | The type of the source address in the access control policy. Valid values: net: source CIDR block group: source address book location: source location |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |
| TotalCount | String | 100 | The total number of the returned access control policies. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeControlPolicy &CurrentPage=1 &Direction=in &PageSize=10 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeControlPolicyResponse>
  <TotalCount>58</TotalCount>
  <PageNo>1</PageNo>
  <PageSize>10</PageSize>
  <RequestId>A08BC58F-A83D-43EB-BC31-2F0D723929CC</RequestId>
  <Policys>
        <ApplicationName>RDP</ApplicationName>
        <Description>11</Description>
        <HitTimes>0</HitTimes>
        <DestinationType>net</DestinationType>
        <SourceType>net</SourceType>
        <Proto>TCP</Proto>
        <Order>5</Order>
        <ApplicationId>27</ApplicationId>
        <Direction>in</Direction>
        <DestPortType>port</DestPortType>
        <Source>1.1.1.1/32</Source>
        <DestPort>1/1</DestPort>
        <AclAction>accept</AclAction>
        <AclUuid>53d82f0e-9bf1-4761-ab3b-a070b4811234</AclUuid>
        <Destination>1.1.1.1/32</Destination>
        <DnsResult>1.1.1.1,2.2.2.2</DnsResult>
        <DnsResultTime>1579261141</DnsResultTime>
  </Policys>
</DescribeControlPolicyResponse>
```

`JSON` format `{`

```json
    "TotalCount":58,
    "PageNo":1,
    "PageSize":10,
    "RequestId":"A08BC58F-A83D-43EB-BC31-2F0D723929CC",
    "Policys":[
```

`{`

```json
            "DestinationGroupCidrs":[
```

`],`

```json
            "SourceGroupCidrs":[
```

`],`

```json
            "ApplicationName":"RDP",
            "Description":"11",
            "HitTimes":0,
            "DestinationType":"net",
            "SourceType":"net",
            "Proto":"TCP",
            "Order":5,
            "ApplicationId":"27",
            "Direction":"in",
            "DestPortType":"port",
            "Source":"1.1.1.1/32",
            "DestPort":"1/1",
            "AclAction":"accept",
            "DestPortGroupPorts":[
```

`],`

```json
            "AclUuid":"53d82f0e-9bf1-4761-ab3b-a070b4811234",
            "Destination":"1.1.1.1/32",
            "DnsResult": "1.1.1.1,2.2.2.2",
            "DnsResultTime": 1579261141
```

`}` `]` `}`

#### 4.4.4 AddControlPolicy

Creates an access control policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddControlPolic y | The operation that you want to perform. Set the value to AddControlPolicy. |

| AclAction | String | Yes | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept: allows the traffic drop: denies the traffic log: monitors the traffic |
|---|---|---|---|---|
| ApplicationName | String | Yes | HTTP | The type of applications to which the access control policy applies. Valid values: FTP HTTP HTTPS Memcache MongoDB MQTT MySQL RDP Redis SMTP SMTPS SSH SSL VNC ANY (indicates all types of applications) |
| Description | String | Yes | test | The description of the access control policy. |

| Destination | String | Yes | 1.2.3.4/24 | The destination address in the access control policy. Valid values: If the DestinationType parameter is set to net , the value of this parameter is the destination CIDR block. Example: 1.2.3.4/24 If the DestinationType parameter is set to group , the value of this parameter is the name of the destination address book. Example: db group _ If the DestinationType parameter is set to domain , the value of this parameter is the destination domain name. Example: *.aliyuncs.com If the DestinationType parameter is set to location , the value of this parameter is the destination location. For more information about the location codes, see the following section. Example: ["BJ11", "ZB"] |
|---|---|---|---|---|
| DestinationType | String | Yes | net | The type of the destination address in the access control policy. Valid values: net: destination CIDR block group: destination address book domain: destination domain name location: destination location |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out: outbound traffic |

| NewOrder | String | Yes | -1 | The priority of the access control policy. The priority value starts from 1. A smaller priority value indicates a higher priority. Note －1 indicates the lowest priority. |
|---|---|---|---|---|
| Proto | String | Yes | TCP | The protocol type in the access control policy. Valid values: ANY Note If you are not sure about the protocol type, you can set this parameter to ANY. TCP UDP ICMP |
| Source | String | Yes | 1.2.3.0/24 | The source address in the access control policy. Valid values: If the SourceType parameter is set to net , the value of this parameter is the source CIDR block. Example: 1.2.3.0/24 If the SourceType parameter is set to group , the value of this parameter is the name of the source address book. Example: db group _ If the SourceType parameter is set to location , the value of this parameter is the source location. For more information about the location codes, see the following section. Example: ["BJ11", "ZB"] |

| SourceType | String | Yes | net | The type of the source address in the access control policy. Valid values: net: source CIDR block group: source address book location: source location |
|---|---|---|---|---|
| SourceIp | String | No | 1.2.3.5 | The source IP address of the request. |
| Lang | String | No | zh | The language of the content in the request and response. Valid values: zh: Chinese en: English |

| DestPort | String | No | 80 | The destination port in the access control policy. Valid values: If the protocol type is ICMP , the value of the DestPort parameter is empty. Note If the protocol type is ICMP , access control based on destination ports is not supported. If the protocol type is TCP , UDP , or ANY , and the destination port type (DestPortType) is group , the value of the DestPort parameter is empty. Note If you set the destination port type to group (destination port address book) in the access control policy, you do not need to specify a destination port number. All ports that the access control policy controls are included in the destination port address book. If the protocol type is TCP , UDP , or ANY , and the destination port type (DestPortType) is port , the value of the DestPort parameter is the destination port number. |
|---|---|---|---|---|
| DestPortType | String | No | port | The type of the destination port in the access control policy. Valid values: port: port group: port address book |

| DestPortGroup | String | No | my port group _ _ | The name of the destination port address book in the access control policy. Note If the DestPortType parameter is set to group , you must specify the name of the destination port address book. |
|---|---|---|---|---|
| Release | String | No | true | Specifies whether to enable the access control policy. By default, an access control policy is enabled after it is created. Valid values: true: enables the access control policy false: does not enable the access control policy |

The following section lists the location codes: China: ZD Beijing: BJ11 Tianjin: TJ12 Hebei: HB13 Shanxi: SX14 Liaoning: LN21 Jilin: JL22 Shanghai: SH31 Jiangsu: JS32 Zhejiang: ZJ33 Anhui: AH34 Fujian: FJ35 Jiangxi: JX36 Shandong: SD37 Henan: HN41 Hubei: HB42 Hunan: HN43 Guangdong: GD44 Hainan: HN46 Chongqing: CQ50 Sichuan: SC51 Guizhou: GZ52 Yunnan: YN53 Shaanxi: SX61 Gansu: GS62 Qinghai: QH63 Heilongjiang: HLJ23 Xizang: XZ54 Guangxi: GX45 Nei Mongol: NMG15 Ningxia: NX64 Xinjiang: XJ65 Taiwan: TW Hong Kong S.A.R: HK Macao S.A.R: MO Locations outside China: ZB Asia (excluding China): ZC Europe: EU Africa: AF North America: NA South America: LA Oceania: OA Antarctica: AQ

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclUuid | String | 00281255-d220- 4db1-8f4f- c4df221a**** | The ID of the access control policy that is created on the Internet firewall. |
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddControlPolicy &AclAction=accept &ApplicationName=ANY &Description=demo_rule_1 &Destination=1.2.3.4/24 &DestinationType=net &Direction=in &NewOrder=-1 &Proto=TCP &Source=1.2.3.0/24 &SourceType=net &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2****</RequestId> <AclUuid>00281255-d220-4db1-8f4f-c4df221a****</AclUuid>
```

`JSON` format

```json
{"RequestId":"CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2****","AclUuid":"00281255-d220-4db1-8f4fc4df221a****"}
```

#### 4.4.5 DeleteControlPolicy

Deletes an access control policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteControlPol icy | The operation that you want to perform. Set the value to DeleteControlPolicy. |
| AclUuid | String | Yes | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. To delete an access control policy, you must provide the ID of the policy. You can call the DescribeControlPolicy operation to obtain the ID. |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out: outbound traffic |

| SourceIp | String | No | 1.2.3.4 | The source IP address of the traffic. |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteControlPolicy &AclUuid=00281255-d220-4db1-8f4f-c4df221ad84c &Direction=in &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteControlPolicyResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</DeleteControlPolicyResponse>
```

`JSON` format `{`

```json
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
```

`}`

#### 4.4.6 ModifyControlPolicy

Modifies the configurations of an access control policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| AclAction | String | Yes | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept: allows the traffic. drop: denies the traffic. log: monitors the traffic. |
|---|---|---|---|---|
| AclUuid | String | Yes | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. To modify the access control policy, you must specify the ID of the policy. You can call the DescribeControlPolicy operation to obtain the ID. |
| Action | String | Yes | ModifyControlPol icy | The operation that you want to perform. Set the value to ModifyControlPolicy. |
| ApplicationNa me | String | Yes | HTTP | The type of the application that the access control policy supports. Valid values: ANY HTTP HTTPS MySQL SMTP SMTPS RDP VNC SSH Redis MQTT MongoDB Memcache SSL Note The value ANY indicates all types of applications. |
| Description | String | Yes | test | The description of the access control policy. |

| Destination | String | Yes | 1.2.3.4/24 | The destination address in the access control policy. If the DestinationType parameter is set to net, the value of this parameter is the destination CIDR block. Example: 1.2.3.4/24. If the DestinationType parameter is set to group, the value of this parameter is the name of the destination address book. Example: db group. _ If the DestinationType parameter is set to domain, the value of this parameter is the destination domain name. Example: *.aliyuncs.com. If the DestinationType parameter is set to location, the value of this parameter is the destination location. For more information about location codes, see AddControlPolicy. Example: ["BJ11", "ZB"]. |
|---|---|---|---|---|
| DestinationTy pe | String | Yes | net | The type of the destination address in the access control policy. Valid values: net: CIDR block group: destination address book domain: destination domain name location: destination location |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out: outbound traffic |
| Proto | String | Yes | TCP | The type of the security protocol in the access control policy. If you are not sure about the protocol type, you can set this parameter to ANY. ANY TCP UDP ICMP |

| Source | String | Yes | 1.2.3.0/24 | The source address in the access control policy. If the SourceType parameter is set to net, the value of this parameter is the source CIDR block. Example: 1.2.3.0/24. If the SourceType parameter is set to group, the value of this parameter is the name of the source address book. Example: db group. _ If the SourceType parameter is set to location, the value of this parameter is the source location. For more information about location codes, see AddControlPolicy. Example: ["BJ11", "ZB"]. |
|---|---|---|---|---|
| SourceType | String | Yes | net | The type of the source address in the access control policy. Valid values: net: source CIDR block group: source address book location: source location |
| DestPort | String | No | 80 | The destination port in the access control policy. |
| DestPortGroup | String | No | my port group _ _ | The name of the destination port address book in the access control policy. |
| DestPortType | String | No | port | The type of the destination port in the access control policy. Valid values: port group: port address book |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.5 | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyControlPolicy &AclAction=accept &AclUuid=00281255-d220-4db1-8f4f-c4df221ad84c &ApplicationName=ANY &Description=demo_rule_1 &Destination=1.2.3.4/24 &DestinationType=net &Direction=in &Proto=TCP &Source=1.2.3.0/24 &SourceType=net &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyControlPolicy>
   <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</ModifyControlPolicy>
```

`JSON` format `{`

```json
 "RequestId":"CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

### 4.5 Address books

#### 4.5.1 AddAddressBook

Creates an address book for access control. Supported address book types include IP address books, ECS tag-based address books, port address books, and domain name address books.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | AddAddressBook | The operation that you want to perform. Set the value to AddAddressBook. |
|---|---|---|---|---|
| Description | String | Yes | DEMO address book | The description of the address book. |
| GroupName | String | Yes | demo address b _ _ ook | The name of the address book. |
| GroupType | String | Yes | ip | The type of the address book. Valid values: ip: IP address book domain: domain name address book port: port address book tag: ECS tag-based address book |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The language of the content in the request and response messages. zh: Chinese en: English |
| AddressList | String | No | 1.2.3.4/32, 1.2.3.0/24 | The addresses that you want to add to the address book. Separate multiple addresses with commas (,). This parameter is required when GroupType is set to ip, port, or domain. When GroupType is set to ip, specify IP addresses in the address list. Example: 1.2.3.4/32, 1.2.3.0/24 When GroupType is set to port, specify ports or port ranges in the address list. Example: 80, 100/200 When GroupType is set to domain, specify domain names in the address list. Example: demo1.aliyun.com, demo2.aliyun.com |
| AutoAddTagEcs | String | No | 1 | Specifies whether to automatically add public IP addresses of ECS instances to the address book if the instances match the specified tags. 1: automatically add 0: do not automatically add |

| TagRelation | String | No | and | The logical relation among the ECS tags that you want to match. and: The tags have an AND relationship. Only the public IP addresses of ECS instances that match all specified tags are added to the address book. or: The tags have an OR relationship. The public IP addresses of ECS instances that match any of the specified tags are added to the address book. |
|---|---|---|---|---|
| TagList.N.TagKe y | String | No | key1 | The key of ECS tag N that you want to match. |
| TagList.N.TagVal ue | String | No | value1 | The value of ECS tag N that you want to match. |

**Returned data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| GroupUuid | String | f04ac7ce-628b- 4cb7-be61- 310222b7**** | The UUID of the returned address book. |
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddAddressBook &Description=DEMO address book &GroupName=demo_address_book &GroupType=ip &AddressList=1.2.3.4/32,1.2.3.0/24 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GroupUuid>f04ac7ce-628b-4cb7-be61-310222b7****</GroupUuid> <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2****</RequestId>
```

`JSON` format

```json
{"GroupUuid":"f04ac7ce-628b-4cb7-be61-310222b7****","RequestId":"CBF1E9B7-D6A0-4E9E-AD3 E-2B47E6C2****"}
```

#### 4.5.2 DeleteAddressBook

Deletes an address book for access control.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAddressB ook | The operation that you want to perform. Set the value to DeleteAddressBook. |
| GroupUuid | String | Yes | 0657ab9d-fe8b- 4174-b2a6- 6baf358ea4ad | The ID of the address book. To delete the address book, you must specify the ID of the address book. You can call the DescribeAddressBook operation to obtain the ID. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The language of the content in the request and response messages. zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteAddressBook &GroupUuid=0657ab9d-fe8b-4174-b2a6-6baf358ea4ad &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2****</RequestId>
```

`JSON` format

```json
{"RequestId":"CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2****"}
```

#### 4.5.3 ModifyAddressBook

Modifies an address book for access control.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAddressB ook | The operation that you want to perform. Set the value to ModifyAddressBook. |
| Description | String | Yes | DEMO address book | The description of the address book. |
| GroupName | String | Yes | demo address b _ _ ook | The name of the address book. |
| GroupUuid | String | Yes | 0657ab9d-fe8b- 4174-b2a6- 6baf358ea4ad | The unique ID of the address book. To modify the address book for access control, you must provide the unique ID of the address book. You can call the DescribeAddressBook operation to obtain the ID. |
| SourceIp | String | No | 1.XX.XX.4 | The source IP address of the request. |
| Lang | String | No | zh | The language of the content in the request and response messages. zh: Chinese en: English |
| AddressList | String | No | 1.1.1.1/32, 2.2.2.0/24 | The addresses in the address book. Separate multiple addresses with commas (,). This parameter is required when GroupType is set to ip, port, or domain. If GroupType is set to ip, specify IP addresses. Example: 1.2.3.4/32, 1.2.3.0/24 If GroupType is set to port, specify ports or port ranges. Example: 80, 100/200 If GroupType is set to domain, specify domain names. Example: demo1.aliyun.com, demo2.aliyun.com |

| AutoAddTagEcs | String | No | 1 | Specifies whether to automatically add public IP addresses of ECS instances to the address book if the instances match the specified tags. 1: yes 0: no |
|---|---|---|---|---|
| TagRelation | String | No | and | The logical relation among ECS tags. and: The public IP addresses of ECS instances are added to the address book only when the instances match all specified tags. or: The public IP addresses of ECS instances are added to the address book when the instances match any of the specified tags. |
| TagList.N.TagKe y | String | No | key1 | The key of ECS tag N that you want to match. |
| TagList.N.TagVal ue | String | No | value1 | The value of ECS tag N that you want to match. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyAddressBook &GroupUuid=0657ab9d-fe8b-4174-b2a6-6baf358ea4ad &Description=DEMO address book &GroupName=demo_address_book &GroupType=ip &AddressList=1.1.1.1/32,2.2.2.0/24 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2****</RequestId>
```

`JSON` format

```json
{"RequestId":"CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2****"}
```

#### 4.5.4 DescribeAddressBook

Queries the details of an address book for access control.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAddress Book | The operation that you want to perform. Set the value to DescribeAddressBook. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The language of the content in the request and response messages. zh: Chinese en: English |
| CurrentPage | String | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | String | No | 50 | The number of entries to return on each page. Maximum value: 50. |
| Query | String | No | 1.2.3.0 | The query condition that is used to search for the address book. |
| GroupType | String | No | ip | The type of the address book. Valid values: ip: IP address book domain: domain name address book port: port address book tag: ECS tag-based address book |
| ContainPort | String | No | 80 | Details about the address book that contains ports. This parameter only takes effect when the GroupType parameter is set to port. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Acls | Array of Acl |   | The information about the address book. |

| AddressList | List | [ "1.2.3.4/32", "0.0.0.0/0" ] | The addresses in the address book. |
|---|---|---|---|
| AddressListCo unt | Integer | 2 | The number of addresses in the address book. |
| AutoAddTagEc s | Integer | 1 | Specifies whether to automatically add public IP addresses of ECS instances to the address book if the instances match the specified tags. 1: yes 0: no |
| Description | String | DEMO address book | The description of the address book. |
| Global | Integer | 0 | Indicates whether the address book is global. Valid values: 1: yes 0: no |
| GroupName | String | demo address boo _ _ k | The name of the address book. |
| GroupType | String | ip | The type of the address book. Valid values: ip: IP address book domain: domain name address book port: port address book tag: ECS tag-based address book |
| GroupUuid | String | f04ac7ce-628b- 4cb7-be61- 310222b718e8 | The ID of the address book. |
| ReferenceCou nt | Integer | 3 | The number of times the address book is referenced. |
| TagList | Array of TagListItem |   | Details about the ECS tags that can be automatically added to the address book. |
| TagKey | String | key1 | The key of the ECS tag. |
| TagValue | String | value1 | The value of the ECS tag. |

| TagRelation | String | and | The logical relationship among ECS tags. and: Only the public IP addresses of ECS instances that match all the specific tags can be added to the address book. or: The public IP addresses of ECS instances that match any of the specific tags can be added to the address book. |
|---|---|---|---|
| PageNo | String | 1 | The page number of the returned page. |
| PageSize | String | 10 | The number of entries per page. |
| RequestId | String | B36F150A-1E27- 43AA-B72C- D2AC712F09DA | The ID of the request. |
| TotalCount | String | 100 | The number of address books. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAddressBook &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAddressBook>
   <TotalCount>123</TotalCount>
   <PageSiNo>1</PageSiNo>
   <PageSize>1</PageSize>
   <RequestId>B36F150A-1E27-43AA-B72C-D2AC712F09DA</RequestId>
   <Acls>
      <Description>9-3 IP address book</Description>
      <GroupType>ip</GroupType>
      <AddressList>1.2.3.4/32</AddressList>
      <AddressList>0.0.0.0/0</AddressList>
      <GroupName>9-3 IP address book</GroupName>
      <AutoAddTagEcs>0</AutoAddTagEcs>
      <TagValue></TagValue>
      <TagRelation></TagRelation>
      <ReferenceCount>0</ReferenceCount>
      <TagKey></TagKey>
      <AddressListCount>2</AddressListCount>
      <GroupUuid>a3c5e-018e-4c08-bea8-eafc95d1a54e</GroupUuid>
      <Global>0</Global>
   </Acls>
</DescribeAddressBook>
```

`JSON` format `{`

```json
    "TotalCount":123,
    "PageSiNo": 1,
    "PageSize": 1,
    "RequestId":"B36F150A-1E27-43AA-B72C-D2AC712F09DA",
    "Acls":[
```

`{`

```json
            "Description":"9-3 IP address book",
            "GroupType":"ip",
            "AddressList":[
                "1.2.3.4/32",
                "0.0.0.0/0"
```

`],`

```json
            "GroupName":"9-3 IP address book",
            "AutoAddTagEcs":0,
            "TagValue":"",
            "TagRelation":"",
            "TagList":[
```

`],`

```json
            "ReferenceCount":0,
            "TagKey":"",
            "AddressListCount":2,
            "GroupUuid":"a3c5e-018e-4c08-bea8-eafc95d1a54e",
            "Global":0
```

`}` `]` `}`

## 5 Error codes

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
