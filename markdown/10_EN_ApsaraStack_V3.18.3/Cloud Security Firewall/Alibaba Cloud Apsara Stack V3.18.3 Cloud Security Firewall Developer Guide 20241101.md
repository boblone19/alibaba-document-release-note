---
title: "Alibaba Cloud Apsara Stack V3.18.3 Cloud Security Firewall Developer Guide 20241101"
product_version: "V3.18.3"
doc_version: "20241101"
pdf_pages: 108
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Cloud Security Firewall Developer Guide 20241101.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E7%9B%BE%E4%BA%91%E9%98%B2%E7%81%AB%E5%A2%99/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Cloud%20Security%20Firewall%20Developer%20Guide%2020241101.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Cloud Security Firewall Developer Guide 20241101

## Table of Contents

- 1 Preparations
  - 1.1 Log on to the API Tool console
  - 1.2 Obtain an AccessKey pair
- 2 Use POP to make API calls
  - 2.1 Preparations
  - 2.2 SDK for Java
  - 2.3 SDK for Go
  - 2.4 SDK for Python
- 3 Common parameters
- 4 Cloud Firewall
  - 4.1 Make API requests
    - 4.1.1 Request structure
    - 4.1.2 Request signatures
    - 4.1.3 Common parameters
    - 4.1.4 Response structure
  - 4.2 Firewall switch
    - 4.2.1 PutEnableFwSwitch
    - 4.2.2 PutDisableFwSwitch
    - 4.2.3 PutEnableAllFwSwitch
    - 4.2.4 PutDisableAllFwSwitch
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

### 1.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press Enter.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Management Console from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Log On**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable** **MFA** topic in **Apsara Uni-manager Management Console User Guide** .

5. In the top navigation bar, choose **Products > Others > API Tool**.

### 1.2 Obtain an AccessKey pair

AccessKey pairs are classified into AccessKey pairs assigned by Resource Access Management (RAM) and AccessKey pairs assigned by Security Token Service (STS). You can use either type of AccessKey pair for authentication when you call operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of request senders. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign an AccessKey pair for authentication. Use RAM to assign an AccessKey ID and an AccessKey secret to a third party. Use STS to assign an AccessKey ID, an AccessKey secret, and a security token to a third party. For more information, see Obtain an STS AccessKey pair. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts or organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, you must add the following parameters in request headers for access control. If you do not add the parameters, an error may occur. The error indicates that permissions are insufficient.

> **Warning:** The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. The AccessKey pair of an organization has more permissions than the AccessKey pair of a personal account. If you want to obtain the AccessKey pair of an organization, make sure that you are authorized by an administrator. This helps ensure security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. For example, you can obtain the ID of an Elastic Compute Service (ECS) instance from the ECS instance list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
click **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of your account.

> **Note:** An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. Click **Management Accesskey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.
e API calls

## 2 Use POP to make API calls

### 2.1 Preparations

Like in the public cloud, you can use the POP gateway to call API operations in Apsara Stack. This topic describes the preparations before you use the POP gateway to call API operations.

**Background information**

In Apsara Stack, you can use both ASAPI and POP gateways to call API operations. To use the same method and produce the same user experience as in the public cloud, we recommend that you use the POP gateway to call API operations in Apsara Stack.

**Obtain service endpoints**

To use the POP gateway to call API operations, you must use the service endpoints. You can obtain the service endpoints from Alibaba Cloud onsite O&M engineers. You can also obtain the service endpoints by yourself. The following example describes how to obtain the ECS endpoints.
1. Log on to Apsara Infrastructure Management Framework.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click **O&M**. iii. In the left-side navigation pane, choose **Product Management** > **Products**. iv. In the Apsara Stack O&M section, click **Apsara Infrastructure Management**
**Framework**.
2. In the left-side navigation pane, click **Reports**.
3. On the **All Reports** page, search for `Registration Vars of Services` and click the report
name.
4. On the **Registration Vars of Services** page, click the
icon next to **Service** and search for `ECS` .
5. Find the `ecs-yaochi` service, right-click the **Service Registration** column, and then
select **Show More** from the shortcut menu. e API calls On the **Details** page, view the **internal.openapi.endpoint** value, which is the

```
 endpoint .
```

**Obtain common parameters**

You must obtain the parameters required when you use the POP gateway to call API operations, such as the organization ID, resource set ID, region ID, and instance ID. For more information, see Obtain common header parameters.

### 2.2 SDK for Java

Before you use Apsara Stack API (ASAPI) SDK for POP for Java to access ASAPI, you must know the remote procedure call (RPC) and resource-oriented architecture (ROA) styles that are supported for API calls. ASAPI is compatible with both styles. Their difference lies in the ASAPI endpoints that are used for API calls.

**Prerequisites**

An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. SSL certificate validation is ignored for requests over HTTPS.

**Background information**

ASAPI supports only the HTTPS request protocol.

**Difference between two styles**

When you use the RPC or ROA style to make API calls, take note that the two styles use different ASAPI endpoints.

```bash
# ASAPI endpoint for the RPC style:
public.asapi.<global:region>.<global:internet-domain>/asapi/v3
# ASAPI endpoint for the ROA style:
public.asapi.<global:region>.<global:internet-domain>/asapi/v3/roa
```

**Call examples**

The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

```java
package com.aliyuns.client.pop.ecs; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.ecs.model.v20140526.DescribeInstancesRequest; import com.aliyuncs.ecs.model.v20140526.DescribeInstancesResponse; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import java.util.List; public class DescribeInstancesTest {
    public static void main(String[] args) {
        // Specify the endpoint of ASAPI.
```

e API calls

```java
        String endpoint = "public.asapi.<global:region>.<global:internet-
domain>/asapi/v3";
        // Specify the region where the ECS service resides.
        String region = "<global:region>";
        // Specify the name of the service that you want to access.
        String product = "ECS";
        // Specify your AccessKey pair.
        String ak = "<accessKeyId>";
        String sk = "<accessKeySecret>";
        try {
            DefaultProfile clientProfile = DefaultProfile.getProfile(region, ak, sk);
            // Ignore SSL certificate validation.
            HttpClientConfig clientConfig = HttpClientConfig.getDefault();
            clientConfig.setIgnoreSSLCerts(true);
            // Set the connection timeout period.
            clientConfig.setConnectionTimeoutMillis(3000L);
            // Set the read timeout period.
            clientConfig.setReadTimeoutMillis(10000L);
            clientProfile.setHttpClientConfig(clientConfig);
            // Create a connection.
            DefaultAcsClient acsClient = new DefaultAcsClient(clientProfile);
            // Create a request.
            DescribeInstancesRequest request = new DescribeInstancesRequest();
            // Specify the endpoint of ASAPI.
            request.setSysEndpoint(endpoint);
            // Specify the name of the service that you want to access and the region w
here the service resides.
            request.setSysLocationProduct(product);
            request.setSysRegionId(region);
            // Set the request protocol to HTTPS.
            request.setSysProtocol(ProtocolType.HTTPS);
            DescribeInstancesResponse result =  acsClient.getAcsResponse(request);
            List<DescribeInstancesResponse.Instance> instances = result.getInstances();
            for (DescribeInstancesResponse.Instance instance: instances) {
                System.out.println(instance.getInstanceId());
                System.out.println(instance.getInstanceName());
```

`}`

```
        } catch (Exception e) {
            e.printStackTrace();
```

`}` `}` `}` The following sample code provides an example on how to use the ROA style to make an API call. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06-07. Sample code:

```java
package com.aliyuns.client.pop.cr; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient;
```

e API calls `p` `y`

```java
import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceListTest {
    public static void main(String[] args) {
        // Specify the endpoint of ASAPI.
        String endpoint = "public.asapi.<global:region>.<global:internet-
domain>/asapi/v3/roa";
        // Specify the region where the Container Registry service resides.
        String region = "<global:region>";
        // Specify the name of the service that you want to access.
        String product = "cr";
        // Specify your AccessKey pair.
        String ak = "<accessKeyId>";
        String sk = "<accessKeySecret>";
        DefaultProfile profile = DefaultProfile.getProfile(region, ak, sk);
        // Ignore SSL certificate validation.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        // Set the connection timeout period.
        clientConfig.setConnectionTimeoutMillis(3000L);
        // Set the read timeout period.
        clientConfig.setReadTimeoutMillis(10000L);
        profile.setHttpClientConfig(clientConfig);
        // Create a connection for the client.
        IAcsClient client = new DefaultAcsClient(profile);
        // Create a request.
        CommonRequest request = new CommonRequest();
        // Set the request protocol to HTTPS.
        request.setSysProtocol(ProtocolType.HTTPS);
        // Specify the request method.
        request.setSysMethod(MethodType.GET);
        // Specify the endpoint of ASAPI.
        request.setSysDomain(endpoint);
        // Specify the version of the API.
        request.setSysVersion("2016-06-07");
        // Specify the pattern of the uniform resource identifier (URI).
        request.setSysUriPattern("/namespace");
        // Specify the name of the service that you want to access and the region where
the service resides.
        request.setSysLocationProduct(product);
        request.putHeadParameter("Content-Type", "application/json");
        String requestBody = "" +
                "{}";
        request.setHttpContent(requestBody.getBytes(), "utf-8", FormatType.JSON);
        try {
            CommonResponse response = client.getCommonResponse(request);
```

e API calls

```java
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            e.printStackTrace();
```

`}` `}` `}`

> **Important:** If you send a request over HTTPS, you must enable the request to ignore SSL certificate validation.

### 2.3 SDK for Go

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Go.

**Prerequisites**

An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed.

**Background information**

Only the remote procedure call (RPC) style is supported for API calls.

**Call examples**

The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

```java
package main import (
 "fmt"
 "time"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/responses"
```

`)`

```
func getSdkConfig() *sdk.Config {
 return sdk.NewConfig().
  WithTimeout(time.Duration(30) * time.Second).
  WithEnableAsync(true).
  WithGoRoutinePoolSize(100).
  WithMaxTaskQueueSize(10000).
  WithDebug(false).
  WithScheme("HTTP")
```

`}` e API calls `}`

```
func main(){
 ak := "<The AccessKey ID of your Apsara Stack tenant account.>"
 sk := "<The AccessKey secret of your Apsara Stack tenant account.>"
 regionId := "<The region where the ECS service resides.>"
 endpoint := "<The endpoint of ASAPI.>" // No network protocol.
 request := requests.NewCommonRequest()
  request.SetReadTimeout(10 * time.Second) // Set the read timeout period of the reques
t to 10 seconds.
  request.SetConnectTimeout(5 * time.Second)  // Set the connection timeout period of t
he request to 5 seconds.
 request.Method = requests.GET
 request.Domain = endpoint         // Location Service will not be enabled if the host
is specified. For example, the service with a certification type-bearer token must be s pecified.
 request.Version = "2014-05-26"            // Specify the version of the API.
 request.Scheme = "https"                // Specify the request protocol. Default value:
http.
 request.ApiName = "DescribeInstances"
 request.QueryParams["Product"] = "Ecs"  // Specify the name of the service that you wa
nt to access.
 request.TransToAcsRequest()
 client, err :=
sdk.NewClientWithOptions(regionId,getSdkConfig(),credentials.NewAccessKeyCredential(ak,sk
 // If relevant parameters are not set for the request, the client settings are used.
  //client.SetReadTimeout(10 * time.Second)              // Set the read timeout period
of the client to 10 seconds.
 //client.SetConnectTimeout(5 * time.Second)            // Set the connection timeout
period of the client to 5 seconds.
  resp := responses.BaseResponse{}
  err = client.DoAction(request, &resp)
    if err != nil {
        panic(err)
```

`}`

```
 fmt.Print(endpoint)
```

`}`

**Configure proxies**

You can configure proxies in one of the following ways: Configure proxies by using environment variables. Set the HTTP_PROXY and HTTPS_PROXY environment variables, or set the NO_PROXY environment variable. Sample code: e API calls

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

### 2.4 SDK for Python

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Python.

**Prerequisites**

An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed.

**Background information**

Only the remote procedure call (RPC) style is supported for API calls.

**Call examples**

The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code: e API calls

```java
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest import os
# Create an AcsClient instance.
client = AcsClient(
   "<your-access-key-id>",
   "<your-access-key-secret>",
   "<your-region-id>",
   timeout=1000,  # Set the timeout period.
    verify=False, # Ignore certificate validation. or verify='<The location where the c
ertificate is stored.>'
```

);

```python
# Set the following parameters for the HTTPS request protocol:
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def hello_ecs_instance():
    # Create a request and set the parameters.
    request = DescribeInstancesRequest.DescribeInstancesRequest()
    params = {"PageNumber":"1", "Product":"Ecs","Version": "2014-05-26","Action": "Desc
ribeInstances"};
    request.set_body_params(params)
    # The endpoint that contains no network protocol is in the following format: ASAPI
domain name/asapi/v3.
    request.set_endpoint('<The endpoint of ASAPI.>')
    # Set the following parameter if the endpoint contains no network protocol:
    request.set_protocol_type("https")
    request.set_PageSize(10)
    # Initiate the API request and obtain the response.
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    hello_ecs_instance()
```

**Configure proxies**

Set the HTTP_PROXY and HTTPS_PROXY environment variables. Sample code: e API calls

```bash
# Configure the HTTPS proxy.
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# Configure the HTTP proxy.
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

eters

## 3 Common parameters

**Common request parameters**

Common request parameters must be included in all Apsara Stack Security API requests. Table 1. Table of common request parameters

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Format | Strin g | No | The format in which to return the response. Set the value to JSON. |
| Version | Strin g | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Valid values: If you call the API operations of the cloud service whose service code is Auditprivate, set the value to 2018-01-16. If you call the API operations of the cloud service whose service code is yundunnextsoc, set the value to 2019-07-23. If you call the API operations of the cloud service whose service code is Sas, set the value to 2018-12-03. If you call the API operations of the cloud service whose service code is aegis, set the value to 2016-11-11. If you call the API operations of the cloud service whose service code is yundun-css, set the value to 2021-10-11. If you call the API operations of the cloud service whose service code is secspy, set the value to 2019-08-05. If you call the API operations of the cloud service whose service code is Ddosprivate, set the value to 2018-01-16. If you call the API operations of the cloud service whose service code is hsm-private, set the value to 2018-06-30. If you call the API operations of the cloud service whose service code is Cloudfw, set the value to 2017-12-07. If you call the API operations of the cloud service whose service code is Sddp, set the value to 2019-01-03. If you call the API operations of the cloud service whose service code is semawaf, set the value to 2020-07-01. If you call the API operations of the cloud service whose service code is soar, set the value to 2018-12-03. |
| AccessKeyId | Strin g | Yes | The AccessKey ID provided to you by Apsara Stack. |
| AccessKeySe cret | Strin g | Yes | The AccessKey secret provided to you by Apsara Stack. |
| RegionId | Strin g | Yes | The region ID of the service. |

eters

| Product | Strin g | Yes | The name of the service to which the API operation belongs. Valid values: Auditprivate: basic components of Apsara Stack Security yundunnextsoc: Security Operations Center (SOC) Sas: Threat Detection Service aegis: Server Guard yundun-css: Container Production secspy: Network Detection and Response Ddosprivate: Anti-DDoS Service hsm-private: Data Encryption Service Cloudfw: Cloud Firewall Sddp: Sensitive Data Discovery and Protection (SDDP) semawaf: Web Application Firewall (WAF) soar: Security Orchestration and Automation Response (SOAR) |
|---|---|---|---|
| EndpointPre | Strin g | Yes | The prefix in the endpoint of the service to which the API operation belongs. Valid values: auditprivate: the prefix in the endpoint of basic components of Apsara Stack Security yundunnextsoc-pop: the prefix in the endpoint of SOC tds: the prefix in the endpoint of Threat Detection Service aegis: the prefix in the endpoint of Server Guard yundun-css: the prefix in the endpoint of Container Protection secspy-share: the prefix in the endpoint of Network Detection and Response ddosprivate: the prefix in the endpoint of Anti-DDoS Service hsmprivate: the prefix in the endpoint of Data Encryption Service cloudfw: the prefix in the endpoint of Cloud Firewall sddp-api: the prefix in the endpoint of SDDP semawaf: the prefix in the endpoint of WAF soar: the prefix in the endpoint of SOAR |

**Common response parameters**

API responses use the HTTP response format: A 2xx status code indicates a successful call. A 4xx or 5xx status code indicates a failed call. Responses are returned in the JSON format. Every response returns a unique RequestID regardless of whether the call is successful.

## 4 Cloud Firewall

### 4.1 Make API requests

#### 4.1.1 Request structure

Apsara Stack Security API operations use the RPC protocol. This topic describes the structure of API requests.

**Description**

You can call Apsara Stack Security API operations by sending HTTP requests. The request syntax is as follows:

```
http://endpoint/?Action=xx&parameters
```

where:

|   | endpoint |   | : The endpoin |
|---|---|---|---|
| [RegionId].example.com |   |   |   |
|   | Action | : the name of t |   |

`endpoint` : The endpoint of the Web Application Firewall (WAF) API is `semawaf.` `Action` : the name of the operation being performed. For example, to query the Apsara Stack Security features that are deployed, you must set the Action parameter to DescribeFeatures. `parameters` : the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operationspecific parameters. Common parameters include information such as the API version number and authentication information. For more information about operation-specific parameters, see the corresponding operation description.

**Example**

The following example demonstrates how to call the DescribeFeatures operation to query the Apsara Stack Security features that are deployed:

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

> **Note:** The request parameters include operation-specific parameters and all common request parameters except Signature.

i. Sort the request parameters. Sort the request parameters in alphabetical order. ii. Encode the parameters. Encode the canonicalized query string in UTF-8 based on the following rules: Uppercase letters, lowercase letters, digits, and some special characters such as hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded. Other characters must be percent encoded in the %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22. Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20. Do not encode spaces as plus signs (+). iii. Connect the encoded parameter names and values by using equal signs (=). iv. Sort the pairs of parameter names and values that are connected by using equal signs (=) in alphabetical order. Connect the pairs with ampersands (&) to create a canonicalized query string.
2. Create a string-to-sign from the encoded canonicalized query string based on the following
rule:

```
StringToSign=HTTPMethod + "&" + percentEncode("/") + "&" + percentEncode(CanonicalizedQueryString)
```

3. Calculate the HMAC value of the string-to-sign based on the HMAC definition in RFC 2104.

> **Note:** Your AccessKey secret in combination with an ampersand (&) (ASCII:38) is used as the key for the HMAC calculation. The SHA1 algorithm is used to calculate the HMAC value of the string-to-sign.

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

Turns on a firewall switch.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutEnableFwSwi tch | The operation that you want to perform. Set the value to PutEnableFwSwitch. |

| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
|---|---|---|---|---|
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| IpaddrList.N | RepeatL ist | No | ["1.2.3.4","5.6.7. 8"] | The list of IP addresses. |
| RegionList.N | RepeatL ist | No | ["cn- hangzhou","cn- shanghai"] | The list of regions. |
| ResourceTypeL ist.N | RepeatL ist | No | ["EcsPublicIp","N atEip"] | The list of asset types. Valid values: BastionHostIP: the IP address of a bastion host EcsEIP: the EIP of an ECS instance EcsPublicIP: the public IP address of an ECS instance EIP EniEIP: the EIP of an ENI NatEIP: the EIP of a NAT gateway SlbEIP: the EIP of an SLB instance SlbPublicIP: the public IP address of an SLB instance NatPublicIP: the public IP address of a NAT gateway HAVIP: the HA VIP |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B2841452-CB8D- 4F7D-B247- 38E1CF7334F8 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutEnableFwSwitch&IpaddrList=["1.2.3.4","5.6.7.8"] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
```

`JSON` format `{`

```json
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.2 PutDisableFwSwitch

Turns off a firewall switch.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutDisableFwSwi tch | The operation that you want to perform. Set the value to PutDisableFwSwitch. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| IpaddrList.N | RepeatL ist | No | ["1.2.3.4","5.6.7. 8"] | The list of IP addresses. |
| RegionList.N | RepeatL ist | No | ["cn- hangzhou","cn- shanghai"] | The list of regions. |

| ResourceTypeL ist.N | RepeatL ist | No | ["EcsPublicIp","N atEip"] | The list of asset types. Valid values: BastionHostIP: the IP address of a bastion host EcsEIP: the EIP of an ECS instance EcsPublicIP: the public IP address of an ECS instance EIP EniEIP: the EIP of an ENI NatEIP: the EIP of a NAT gateway SlbEIP: the EIP of an SLB instance SlbPublicIP: the public IP address of an SLB instance NatPublicIP: the public IP address of a NAT gateway HAVIP: the HA VIP |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B2841452-CB8D- 4F7D-B247- 38E1CF7334F8 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutDisableFwSwitch&IpaddrList=["1.2.3.4","5.6.7.8"] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
```

`JSON` format `{`

```json
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.3 PutEnableAllFwSwitch

Turns on all firewall switches.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutEnableAllFwS witch | The operation that you want to perform. Set the value to PutEnableAllFwSwitch. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B2841452-CB8D- 4F7D-B247- 38E1CF7334F8 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutEnableAllFwSwitch &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
```

`JSON` format `{`

```json
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.4 PutDisableAllFwSwitch

Turns off all firewall switches.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutDisableAllFw Switch | The operation that you want to perform. Set the value to PutDisableAllFwSwitch. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B2841452-CB8D- 4F7D-B247- 38E1CF7334F8 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutDisableAllFwSwitch &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
```

`JSON` format `{`

```json
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

### 4.3 VPC firewalls

#### 4.3.1 CreateVpcFirewallControlPolicy

Creates an access control policy to a specific policy group for a VPC firewall.

> **Note:** The VPC firewall instances that are used to protect each Cloud Enterprise Network (CEN) instance and each Express Connect use different access control policies.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpcFirew allControlPolicy | The operation that you want to perform. Set the value to CreateVpcFirewallControlPolicy. |
| AclAction | String | Yes | accept | The action that the VPC firewall performs on the traffic. Valid values: accept: allows the traffic. drop: denies the traffic. log: monitors the traffic. |
| ApplicationNa me | String | Yes | HTTP | The type of the application to which the access control policy applies. Valid values: FTP HTTP HTTPS MySQL SMTP SMTPS RDP VNC SSH Redis MQTT MongoDB Memcache SSL ANY, which indicates all types of applications |
| Description | String | Yes | test | The description of the access control policy. |

| Destination | String | Yes | 80 | The destination port in the access control policy. Note If the DestPortType parameter is set to port, you must specify this parameter. |
|---|---|---|---|---|
| DestinationTy pe | String | Yes | net | The type of the destination address in the access control policy. net: CIDR block group: destination address book domain: destination domain name |
| NewOrder | String | Yes | -1 | The priority of the access control policy. The priority value starts from 1. A smaller value indicates a higher priority. Note The value -1 indicates the lowest priority. |
| Proto | String | Yes | TCP | The type of the security protocol in the access control policy. If you are not sure about the protocol type, you can set this parameter to ANY. TCP UDP ICMP |
| Source | String | Yes | 10.2.3.0/24 | The source address in the access control policy. If the SourceType parameter is set to net , the value of this parameter is the source CIDR block. Example: 10.2.3.0/24. If the SourceType parameter is set to group , the value of this parameter is the name of the source address book. Example: db group. _ |

| SourceType | String | Yes | net | The type of the source address in the access control policy. Valid values: net: source CIDR block group: source address book |
|---|---|---|---|---|
| VpcFirewallId | String | Yes | vfw- a42bbb7b88714 8c9**** | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID. Valid values: If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used. Example: cen- ervw5jbw1234*****. If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used. Example: vfw- a42bbb748c91234*****. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| DestPort | String | No | 80 | The destination port in the access control policy. Note If the DestPortType parameter is set to port , you must specify this parameter. |
| DestPortType | String | No | net | The type of the destination port in the access control policy. port group: port address book |
| DestPortGroup | String | No | my port group _ _ | The name of the destination port address book in the access control policy. Note If the DestPortType parameter is set to group , you must specify this parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclUuid | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |
| RequestId | String | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. |

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

> **Note:** The VPC firewall instances that are used to protect each Cloud Enterprise Network (CEN) instance and each Express Connect use different access control policies.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpcFire wallControlPolic y | The operation that you want to perform. Set the value to DescribeVpcFirewallControlPolic y. |
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

> **Note:** The VPC firewall instances that are used to protect each Cloud Enterprise Network (CEN) instance and each Express Connect use different access control policies.

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

> **Note:** The VPC firewall instances that are used to protect each Cloud Enterprise Network (CEN) instance and each Express Connect use different access control policies.

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
| Direction | String | Yes | in | The traffic direction to which the access control policy applies. Valid values: in: inbound traffic out: outbound traffic |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| End | Integer | 150 | The lowest priority of the access control policy. |
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |
| Start | Integer | 1 | The highest priority of the access control policy. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePolicyPriorUsed &Direction=in &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePolicyPriorUsedResponse>
      <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
      <Start>1</Start>
      <End>150</End>
</DescribePolicyPriorUsedResponse>
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

#### 4.4.2 ModifyControlPolicyPosition

Modifies the priority of an access control policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyControlPol icyPosition | The operation that you want to perform. Set the value to ModifyControlPolicyPosition. |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out: outbound traffic |
| NewOrder | String | Yes | 1 | The new priority of the access control policy. |
| OldOrder | String | Yes | 5 | The original priority of the access control policy. |

| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
|---|---|---|---|---|
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 850A84D6-0DE4- 4797-A1E8- 00090125EEB1 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyControlPolicyPosition &Direction=in &NewOrder=1 &OldOrder=5 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyControlPolicyPosition>
   <RequestId>850A84D6-0DE4-4797-A1E8-00090125EEB1</RequestId>
</ModifyControlPolicyPosition>
```

`JSON` format `{`

```json
 "RequestId":"850A84D6-0DE4-4797-A1E8-00090125EEB1"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.4.3 DescribeControlPolicy

Queries information about all the access control policies.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeControl Policy | The operation that you want to perform. Set the value to DescribeControlPolicy. |
|---|---|---|---|---|
| CurrentPage | String | Yes | 1 | The page number of the current page. Default value: 1. |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out: outbound traffic |
| PageSize | String | Yes | 10 | The number of entries to return on each page. Maximum value: 50. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| Source | String | No | 1.2.3.5 | The source address in the access control policy. Fuzzy match is supported. Valid values: If the SourceType parameter is set to net , the value of this parameter is the source CIDR block. Example: 10.0.1.0/24. If the SourceType parameter is set to group , the value of this parameter is the name of the source address book. Example: db group. _ If the SourceType parameter is set to location , the value of this parameter is the source location. Example: beijing. If this parameter is left empty, all source addresses are queried. Note The valid values of this parameter depend on the value of the SourceType parameter. |
|---|---|---|---|---|

| Destination | String | No | 1.2.3.0 | The destination address in the access control policy. Fuzzy match is supported. Valid values: If the DestinationType parameter is set to net , the value of this parameter is the destination CIDR block. Example: 10.0.3.0/24. If the DestinationType parameter is set to domain , the value of this parameter is the destination domain name. Example: aliyun. If the DestinationType parameter is set to group , the value of this parameter is the name of the destination address book. Example: db group. _ If the DestinationType parameter is set to location , the value of this parameter is the destination location. Example: beijing. If this parameter is left empty, all destination addresses are queried. Note The valid values of this parameter depend on the value of the DestinationType parameter. |
|---|---|---|---|---|
| Description | String | No | test | The description of the access control policy. Fuzzy match is supported. Note If this parameter is left empty, the descriptions of all access control policies are queried. |
| Proto | String | No | TCP | The type of protocol in the access control policy. Valid values: TCP. UDP. ICMP. ANY, which indicates all types of protocols. If this parameter is left empty, all types of protocols are queried. |

| AclAction | String | No | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept: allows the traffic. drop: denies the traffic. log: monitors the traffic. If this parameter is left empty, access control policies that specify the preceding actions are queried. |
|---|---|---|---|---|
| Release | String | No | true | Specifies whether the access control policy is enabled. By default, an access control policy is enabled after it is created. Valid values: true: The access control policy is enabled. false: The access control policy is disabled. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNo | String | 1 | The page number of the current page. |
| PageSize | String | 10 | The number of entries returned per page. |
| Policys | Array |   | The information about the access control policy. |
| AclAction | String | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept: allows the traffic. drop: denies the traffic. log: monitors the traffic. |
| AclUuid | String | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. |
| ApplicationId | String | 10*** | The application ID in the access control policy. |

| ApplicationNa me | String | HTTP | The type of the application that the access control policy supports. Valid values: FTP HTTP HTTPS Memcache MongoDB MQTT MySQL RDP Redis SMTP SMTPS SSH SSL VNC ANY, which indicates all types of applications |
|---|---|---|---|
| Description | String | test | The description of the access control policy. |
| DestPort | String | 80 | The destination port in the access control policy. |
| DestPortGroup | String | my port group _ _ | The name of the destination port address book in the access control policy. |
| DestPortGroup Ports | List | [80,443] | The ports in the destination port address book. |
| DestPortType | String | port | The type of the destination port in the access control policy. Valid values: port group: port address book |

| Destination | String | 1.2.3.4/24 | The destination address in the access control policy. Valid values: If the DestinationType parameter is set to net, the value of this parameter is the destination IP address or CIDR block. Example: 10.0.3.0/24. If the DestinationType parameter is set to domain, the value of this parameter is the destination domain name. Example: aliyuncs.com. If the DestinationType parameter is set to group, the value of this parameter is the name of the destination address book. Example: db group. _ If the DestinationType parameter is set to location, the value of this parameter is the destination location. For more information about location codes, see AddControlPolicy. Example: ["BJ11", "ZB"]. Note The valid values of this parameter depend on the value of the DestinationType parameter. |
|---|---|---|---|
| DestinationGro upCidrs | List | ["1.2.3.0/24", "1.2.3.1/32"] | The CIDR blocks in the destination address book. |
| DestinationGro upType | String | ip | The type of the destination address book in the access control policy. Valid values: ip: an address book that includes one or more IP addresses tag: an address book that includes one or more IP addresses with ECS tags domain: an address book that includes one or more domain names threat: an address book that includes one or more malicious IP addresses or domain names backsrc: an address book that includes one or more back-to-origin addresses of Anti-DDoS Pro or Anti-DDoS Premium instances or Web Application Firewall (WAF) instances |

| DestinationTy pe | String | net | The type of the destination address in the access control policy. Valid values: net: destination CIDR block group: destination address book domain: destination domain name location: destination location |
|---|---|---|---|
| Direction | String | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out: outbound traffic |
| DnsResult | String | 1.1.1.1,2.2.2.2 | The DNS resolution result. |
| DnsResultTime | Long | 1579261141 | The timestamp of the DNS resolution result. |
| HitTimes | Integer | 100 | The number of hits for the access control policy. |
| Order | Integer | 1 | The priority of the access control policy. The priority value starts from 1. A smaller value indicates a higher priority. Note The value -1 indicates the lowest priority. |
| Proto | String | TCP | The type of the security protocol in the access control policy. Valid values: ANY TCP UDP ICMP |

| Release | String | true | Indicates whether the access control policy is enabled. By default, an access control policy is enabled after it is created. Valid values: true: The access control policy is enabled. false: The access control policy is disabled. |
|---|---|---|---|
| Source | String | 1.2.3.0/24 | The source address in the access control policy. Valid values: If the SourceType parameter is set to net , the value of this parameter is the source CIDR block. Example: 10.0.1.0/24. If the SourceType parameter is set to group , the value of this parameter is the name of the source address book. Example: db group. _ If the SourceType parameter is set to location, the value of this parameter is the source location. For more information about location codes, see AddControlPolicy. Example: ["BJ11", "ZB"]. |
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

**Error codes**

For a list of error codes, see Error codes.

#### 4.4.4 AddControlPolicy

Creates an access control policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| AclAction | String | Yes | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept: allows the traffic. drop: denies the traffic. log: monitors the traffic. |
|---|---|---|---|---|
| Action | String | Yes | AddControlPolic y | The operation that you want to perform. Set the value to AddControlPolicy. |
| ApplicationNa me | String | Yes | HTTP | The type of applications to which the policy is applied. Valid values: ANY HTTP HTTPS MySQL SMTP SMTPS RDP VNC SSH Redis MQTT MongoDB Memcache SSL Note ANY, which indicates all types of applications |
| Description | String | Yes | test | The description of the access control policy. |

| Destination | String | Yes | 1.2.3.4/24 | The destination address in the access control policy. If the DestinationType parameter is set to net, the value of this parameter is the destination CIDR block. Example: 1.2.3.4/24. If the DestinationType parameter is set to group, the value of this parameter is the name of the destination address book. Example: db group. _ If the DestinationType parameter is set to domain, the value of this parameter is the destination domain name. Example: *.aliyuncs.com. If the DestinationType parameter is set to location, the value of this parameter is the destination location. For more information about the location codes, see the following section. Example: ["BJ11", "ZB"]. |
|---|---|---|---|---|
| DestinationTy pe | String | Yes | net | The type of the destination address in the access control policy. net: CIDR block group: destination address book domain: destination domain name location: destination location |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out: outbound traffic |
| NewOrder | String | Yes | -1 | The priority of the access control policy. The priority value starts from 1. A smaller value indicates a higher priority. Note The value -1 indicates the lowest priority. |
| Proto | String | Yes | TCP | The type of the security protocol in the access control policy. If you are not sure about the protocol type, you can set this parameter to ANY. ANY TCP UDP ICMP |

| Source | String | Yes | 1.2.3.0/24 | The source address in the access control policy. If the SourceType parameter is set to net, the value of this parameter is the source CIDR block. Example: 1.2.3.0/24. If the SourceType parameter is set to group, the value of this parameter is the name of the source address book. Example: db group. _ If the SourceType parameter is set to location, the value of this parameter is the source location. For more information about the location codes, see the following section. Example: ["BJ11", "ZB"]. |
|---|---|---|---|---|
| SourceType | String | Yes | net | The type of the source address in the access control policy. Valid values: net: source CIDR block group: source address book location: source location |
| DestPort | String | No | 80 | The destination port in the access control policy. Note If the DestPortType parameter is set to port, you must specify this parameter. |
| DestPortGroup | String | No | my port group _ _ | The name of the destination port address book in the access control policy. Note If the DestPortType parameter is set to group, you must specify this parameter. |
| DestPortType | String | No | port | The type of the destination port in the access control policy. Valid values: port group: port address book |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |

| SourceIp | String | No | 1.2.3.5 | The source IP address of the request. |
|---|---|---|---|---|

The following section lists the location codes. China: ZD Beijing: BJ11 Tianjin: TJ12 Hebei: HB13 Shanxi: SX14 Liaoning: LN21 Jilin Province: JL22 Shanghai: SH31 Jiangsu: JS32 Zhejiang: ZJ33 Anhui: AH34 Fujian: FJ35 Jiangxi: JX36 Shandong: SD37 Henan: HN41 Hubei: HB42 Hunan: HN43 Guangdong: GD44 Hainan: HN46 Chongqing: CQ50 Sichuan: SC51 Guizhou: GZ52 Yunnan: YN53 Shaanxi: SX61 Gansu: GS62 Qinghai: QH63 Heilongjiang: HLJ23 Xizang: XZ54 Guangxi: GX45 Nei Mongol: NMG15 Ningxia: NX64 Xinjiang: XJ65 Taiwan: TW Hong Kong S.A.R: HK Macao S.A.R: MO Areas outside China: ZB Asia (excluding China): ZC Europe: EU Africa: AF North America: NA South America: LA Oceania: OA Antarctica: AQ

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclUuid | String | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. |
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddControlPolicy &AclAction=accept &ApplicationName=ANY &Description=demo_rule_1 &Destination=1.2.3.4/24 &DestinationType=net &Direction=in &NewOrder=-1 &Proto=TCP &Source=1.2.3.0/24 &SourceType=net &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddControlPolicy>
   <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
   <AclUuid>00281255-d220-4db1-8f4f-c4df221ad84c</AclUuid>
</AddControlPolicy>
```

`JSON` format `{`

```json
 "RequestId":"CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D",
 "AclUuid":"00281255-d220-4db1-8f4f-c4df221ad84c"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.4.5 DeleteControlPolicy

Deletes an access control policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteControlPol icy | The operation that you want to perform. Set the value to DeleteControlPolicy. |
| AclUuid | String | Yes | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. To delete an access control policy, you must specify the ID of the policy. You can call the DescribeControlPolicy operation to obtain the ID. |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out: outbound traffic |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the traffic. |
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

**Error codes**

For a list of error codes, see Error codes.

#### 4.4.6 ModifyControlPolicy

Modifies the configurations of an access control policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| AclAction | String | Yes | accept | The action that Cloud Firewall performs on the traffic. Valid values: accept: allows the traffic. drop: denies the traffic. log: monitors the traffic. |
| AclUuid | String | Yes | 00281255-d220- 4db1-8f4f- c4df221ad84c | The ID of the access control policy. To modify the access control policy, you must specify the ID of the policy. You can call the DescribeControlPolicy operation to obtain the ID. |
| Action | String | Yes | ModifyControlPol icy | The operation that you want to perform. Set the value to ModifyControlPolicy. |

| ApplicationNa me | String | Yes | HTTP | The type of the application that the access control policy supports. Valid values: ANY HTTP HTTPS MySQL SMTP SMTPS RDP VNC SSH Redis MQTT MongoDB Memcache SSL Note The value ANY indicates all types of applications. |
|---|---|---|---|---|
| Description | String | Yes | test | The description of the access control policy. |
| Destination | String | Yes | 1.2.3.4/24 | The destination address in the access control policy. If the DestinationType parameter is set to net, the value of this parameter is the destination CIDR block. Example: 1.2.3.4/24. If the DestinationType parameter is set to group, the value of this parameter is the name of the destination address book. Example: db group. _ If the DestinationType parameter is set to domain, the value of this parameter is the destination domain name. Example: *.aliyuncs.com. If the DestinationType parameter is set to location, the value of this parameter is the destination location. For more information about location codes, see AddControlPolicy. Example: ["BJ11", "ZB"]. |

| DestinationTy pe | String | Yes | net | The type of the destination address in the access control policy. Valid values: net: CIDR block group: destination address book domain: destination domain name location: destination location |
|---|---|---|---|---|
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values: in: inbound traffic out: outbound traffic |
| Proto | String | Yes | TCP | The type of the security protocol in the access control policy. If you are not sure about the protocol type, you can set this parameter to ANY. ANY TCP UDP ICMP |
| Source | String | Yes | 1.2.3.0/24 | The source address in the access control policy. If the SourceType parameter is set to net, the value of this parameter is the source CIDR block. Example: 1.2.3.0/24. If the SourceType parameter is set to group, the value of this parameter is the name of the source address book. Example: db group. _ If the SourceType parameter is set to location, the value of this parameter is the source location. For more information about location codes, see AddControlPolicy. Example: ["BJ11", "ZB"]. |
| SourceType | String | Yes | net | The type of the source address in the access control policy. Valid values: net: source CIDR block group: source address book location: source location |
| DestPort | String | No | 80 | The destination port in the access control policy. |

| DestPortGroup | String | No | my port group _ _ | The name of the destination port address book in the access control policy. |
|---|---|---|---|---|
| DestPortType | String | No | port | The type of the destination port in the access control policy. Valid values: port group: port address book |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.5 | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

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

Creates an address book for access control. Supported address book types are IP address books, Elastic Compute Service (ECS) tag address books, port address books, and domain address books.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddAddressBook | The operation that you want to perform. Set the value to AddAddressBook. |
| Description | String | Yes | DEMO address book | The description of the address book. |
| GroupName | String | Yes | demo address b _ _ ook | The name of the address book. |
| GroupType | String | Yes | ip | The type of the address book. Valid values: ip: IP address book domain: domain address book port: port address book tag: ECS tag address book |

| AddressList | String | No | 1.2.3.4/32, 1.2.3.0/24 | The addresses you want to add to the address book. Separate multiple addresses with commas (,). Note If the GroupType parameter is set to ip, port or domain, this parameter is required. If the GroupType parameter is set to ip, the value of this parameter is the IP addresses. Example: 1.2.3.4/32,1.2.3.0/24. If the GroupType parameter is set to port, the value of this parameter is the ports or port ranges. Example: 80,100/200. If the GroupType parameter is set to domain, the value of this parameter is the domain names. Example: demo1.aliyun.com,demo2.aliyun.c om. |
|---|---|---|---|---|
| AutoAddTagEc s | String | No | 1 | Specifies whether to automatically add public IP addresses of ECS instances to the address book if they match the specific tags. Valid values: 1: yes 0: no |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| TagList.N.Tag Key | String | No | key1 | The key of ECS tag N you want to match. |
| TagList.N.Tag Value | String | No | value1 | The value of ECS tag N you want to match. |

| TagRelation | String | No | and | The logical relation among ECS tags you want to mach. Valid values: and: Only the public IP addresses of ECS instances that match all the specific tags can be added to the address book. or: The public IP addresses of ECS instances that match any of the specific tags can be added to the address book. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| GroupUuid | String | f04ac7ce-628b- 4cb7-be61- 310222b718e8 | The ID of the returned address book |
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddAddressBook &Description=DEMO address book &GroupName=demo_address_book &GroupType=ip &AddressList=1.2.3.4/32,1.2.3.0/24 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddAddressBook>
      <RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
      <GroupUuid>0580bbd0-24cd-47ae-9e5a-f5a099251e32</GroupUuid>
    </AddAddressBook>
```

`JSON` format `{`

```json
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8",
    "GroupUuid":"0580bbd0-24cd-47ae-9e5a-f5a099251e32"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.5.2 DeleteAddressBook

Deletes an address book for access control.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAddressB ook | The operation that you want to perform. Set the value to DeleteAddressBook. |
| GroupUuid | String | Yes | 0657ab9d-fe8b- 4174-b2a6- 6baf358ea4ad | The ID of the address book. To delete the address book, you must specify the ID of the address book. You can call the DescribeAddressBook operation to obtain the ID. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteAddressBook &GroupUuid=0657ab9d-fe8b-4174-b2a6-6baf358ea4ad &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteAddressBook>
   <RequestId>850A84D6-0DE4-4797-A1E8-00090125EEB1</RequestId>
</DeleteAddressBook>
```

`JSON` format `{`

```json
 "RequestId":"850A84D6-0DE4-4797-A1E8-00090125EEB1"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.5.3 ModifyAddressBook

Modifies an address book for the access control.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAddressB ook | The operation that you want to perform. Set the value to ModifyAddressBook. |
| Description | String | Yes | DEMO address book | The description of the address book. |
| GroupName | String | Yes | demo address b _ _ ook | The name of the address book. |
| GroupUuid | String | Yes | 0657ab9d-fe8b- 4174-b2a6- 6baf358ea4ad | The ID of the address book. To modify the address book, you must specify the ID of the address book. You can call the DescribeAddressBook operation to obtain the ID. |

| AddressList | String | No | 1.1.1.1/32, 2.2.2.0/24 | The addresses you want to add to the address book. Separate multiple addresses with commas (,). Note If the GroupType parameter is set to ip, port, or domain, this parameter is required. If the GroupType parameter is set to ip, the value of this parameter is the IP addresses. Example: 1.2.3.4/32,1.2.3.0/24. If the GroupType parameter is set to port, the value of this parameter is the ports or port ranges. Example: 80,100/200. If the GroupType parameter is set to domain, the value of this parameter is the domain names. Example: demo1.aliyun.com,demo2.aliyun.c om. |
|---|---|---|---|---|
| AutoAddTagEc s | String | No | 1 | Specifies whether to automatically add the public IP addresses of ECS instances to the address book if they match the specific tags. Valid values: 1: yes 0: no |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| TagList.N.Tag Key | String | No | key1 | The key of ECS tag N you want to match. |
| TagList.N.Tag Value | String | No | value1 | The value of ECS tag N you want to match. |

| TagRelation | String | No | and | The logical relation among ECS tags. Valid values: and: Only the public IP addresses of ECS instances that match all the specific tags can be added to the address book. or: The public IP addresses of ECS instances that match any of the specific tags can be added to the address book. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CBF1E9B7-D6A0- 4E9E-AD3E- 2B47E6C2837D | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyAddressBook &GroupUuid=0657ab9d-fe8b-4174-b2a6-6baf358ea4ad &Description=DEMO address book &GroupName=demo_address_book &GroupType=ip &AddressList=1.1.1.1/32,2.2.2.0/24 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyAddressBook>
      <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</ModifyAddressBook>
```

`JSON` format `{`

```json
    "RequestId":"CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.5.4 DescribeAddressBook

Queries the details of an address book for the access control.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAddress Book | The operation that you want to perform. Set the value to DescribeAddressBook. |
| ContainPort | String | No | 80 | Details about the address book that contains ports.This parameter only takes effect when the GroupType parameter is set to port. |
| CurrentPage | String | No | 1 | The number of the page to return. Default value: 1. |
| GroupType | String | No | ip | The type of the address book. Valid values: ip: IP address book domain: domain address book port: port address book tag: ECS tag address book |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| PageSize | String | No | 50 | The number of entries to return on each page. Maximum value: 50. |
| Query | String | No | 1.2.3.0 | The query condition that specifies the address book. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Acls | Array |   | The information about the address book. |
| AddressList | List | [ "1.2.3.4/32", "0.0.0.0/0" ] | The addresses in the address book. |
| AddressListCo unt | Integer | 2 | The number of addresses in the address book. |

| AutoAddTagEc s | Integer | 1 | Indicates whether to automatically add the public IP addresses of ECS instances to the address book if they match the specific tags. Valid values: 1: yes 0: no |
|---|---|---|---|
| Description | String | DEMO address book | The description of the address book. |
| Global | Integer | 0 | Indicates whether the address book is global. Valid values: 1: yes 0: no |
| GroupName | String | demo address boo _ _ k | The name of the address book. |
| GroupType | String | ip | The type of the address book. Valid values: ip: IP address book domain: domain address book port: port address book tag: ECS tag address book |
| GroupUuid | String | f04ac7ce-628b- 4cb7-be61- 310222b718e8 | The ID of the address book. |
| ReferenceCou nt | Integer | 3 | The number of times the address book is referenced. |
| TagList | Array |   | Details about the ECS tags that can be automatically added to the address book. |
| TagKey | String | key1 | The key of ECS tag N you want to match. |
| TagValue | String | value1 | The value of ECS tag N you want to match. |
| TagRelation | String | and | The logical relation among ECS tags. Valid values: and: Only the public IP addresses of ECS instances that match all the specific tags can be added to the address book. or: The public IP addresses of ECS instances that match any of the specific tags can be added to the address book. |

| PageNo | String | 1 | The number of the current page. |
|---|---|---|---|
| PageSize | String | 10 | The number of entries returned per page. |
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
 "PageSize":1,
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
   "TagList":[],
   "ReferenceCount":0,
   "TagKey":"",
   "AddressListCount":2,
   "GroupUuid":"a3c5e-018e-4c08-bea8-eafc95d1a54e",
   "Global":0
```

`}` `],`

```json
 "PageSiNo":1
```

`}`

**Error codes**

For a list of error codes, see Error codes.

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
