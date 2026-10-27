---
title: "Alibaba Cloud Apsara Stack Enterprise V3.18.1 Cloud Security Network Detection and Response Developer 20231213"
product_version: "V3.18.1"
doc_version: "20231213"
pdf_pages: 121
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.18.1 Cloud Security Network Detection and Response Developer 20231213.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3.18.1%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%BE%E7%BD%91%E7%BB%9C%E6%A3%80%E6%B5%8B%E4%B8%8E%E5%93%8D%E5%BA%94/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.18.1%20Cloud%20Security%20Network%20Detection%20and%20Response%20Developer%2020231213.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.18.1 Cloud Security Network Detection and Response Developer 20231213

## Table of Contents

- 1 Preparations
  - 1.1 Log on to the API Tool console
  - 1.2 View the information about an operation
  - 1.3 Obtain an AccessKey pair
  - 1.4 Obtain an AccessKey pair assigned by STS
  - 1.5 Obtain an endpoint
- 2 Call examples
  - 2.1 Call examples for SDK for Java
    - 2.1.1 Use SDK
      - 2.1.1.1 Install SDK for Java
      - 2.1.1.2 Use CommonRequest to call API operations
  - 2.2 Call examples for SDK for Python
    - 2.2.1 Use SDK
      - 2.2.1.1 Install SDK for Python
      - 2.2.1.2 Use CommonRequest to call API operations
  - 2.3 Call examples for SDK for Go
    - 2.3.1 Use SDK
      - 2.3.1.1 Install the core package of SDK for Go
      - 2.3.1.2 Use CommonRequest to call API operations
- 3 Common parameters
- 4 Network Traffic Monitoring System
  - 4.1 Make API requests
    - 4.1.1 Request structure
    - 4.1.2 Request signatures
    - 4.1.3 Common parameters
    - 4.1.4 Response structure
  - 4.2 API documentation
    - 4.2.1 API Reference (2023-04-03 )
      - 4.2.1.1 DescribePlaybook
      - 4.2.1.2 DescribeSoarRecords
      - 4.2.1.3 PublishPlaybook
      - 4.2.1.4 TriggerPlaybook
    - 4.2.2 DescribeSoarRecordActions
    - 4.2.3 GetPlaybookTriggerResult
    - 4.2.4 TriggerPlaybookAndWait
    - 4.2.5 CreateEventByAlert
    - 4.2.6 SyncBanRecord
    - 4.2.7 DescribeManualTaskInfo
    - 4.2.8 DescribePlaybook
    - 4.2.9 DescribeSoarRecords
    - 4.2.10 StopOneAction
    - 4.2.11 PublishPlaybook
    - 4.2.12 TriggerPlaybook
    - 4.2.13 ModifyPlaybook
    - 4.2.14 AddToBlackList
    - 4.2.15 AddToWhiteList
    - 4.2.16 DelFromBlackList
    - 4.2.17 DelFromWhiteList
    - 4.2.18 DescribeBlackList
    - 4.2.19 DescribeWhiteList
    - 4.2.20 DescribeL7Rule
    - 4.2.21 SwitchL7RuleStatus
    - 4.2.22 AddL7Rule
    - 4.2.23 DelL7Rule
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

### 1.2 View the information about an operation

**operation**

When you use a service SDK to call an operation of the service, you must obtain the service name, operation name, and API version. This topic describes how to view the information about an operation.

**Background information**

The operations on the API Directory page are for reference only. For information about how to call operations, see API references of the corresponding services. If the information on the API Directory page is inconsistent with that in the API reference of the corresponding service, the information in the API reference takes precedence.

**Procedure**

1. Log on to the API Tool console.
2. In the left-side navigation pane, click **API Directory**.
3. On the **API Directory** page, select the required service from the drop-down list, enter a
keyword of an operation name in the search box, and then click Search.
4. View and record the service name, operation name, and API version.

### 1.3 Obtain an AccessKey pair

AccessKey pairs are classified into AccessKey pairs assigned by Resource Access Management (RAM) and AccessKey pairs assigned by Security Token Service (STS). You can use either type of AccessKey pair for authentication when you call operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of request senders. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign an AccessKey pair for authentication. Use RAM to assign an AccessKey ID and an AccessKey secret to a third party. Use STS to assign an AccessKey ID, an AccessKey secret, and a security token to a third party. For more information, see Obtain an STS AccessKey pair. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts or organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, you must add the following parameters in request headers for access control. If you do not add the parameters, an error may occur. The error indicates that permissions are insufficient.

> **Warning:** The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. The AccessKey pair of an organization has more permissions than the AccessKey pair of a personal account. If you want to obtain the AccessKey pair of an organization, make sure that you are authorized by an administrator. This helps ensure security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |

| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
|---|---|
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

### 1.4 Obtain an AccessKey pair assigned by STS

**assigned by STS**

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

Apsara Stack STS allows you to manage temporary credentials for your Apsara Stack resources. You can use STS to call API operations in Apsara Stack. An AccessKey pair assigned by STS consists of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to call API operations, you must use an AccessKey pair assigned by STS.

**Procedure**

1. Obtain the Alibaba Cloud Resource Name (ARN) of your `Resource Access Management (RAM)`
`role` . i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click **User**
**Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view the ARN of your `RAM role` .
2. Obtain the AccessKey pair assigned by STS.

> **Note:** You must replace the variables in the following code with actual values. Delete the angle brackets (<>) before you submit the code.
> Variables:
> <yourRegionID>: Replace it with the actual region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <yourRoleSessionName>: Replace it with your current session name.
> In most cases, this variable is set to the identity of the user who makes API calls. Example: username. You can identify the users who assume the same RAM role to perform operations based on the value of the `RoleSessionName` variable. This way, you can perform user-specific auditing. The value is 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (_).
> <yourRoleArn>: Replace it with the ARN of your RAM role.
> "sts.aliyuns.com": Replace it with the actual endpoint of STS.

```xml
public static void main(String[] args) {
    // Create a DefaultAcsClient instance and initialize the instance.
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
```

`}`

```java
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace "sts.aliyuns.com" with the endpoint of STS. The format of an STS endpo
int is sts-vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRoleSessionName>" with the actual session name.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // The ARN of your RAM role. Replace "<yourRoleArn>" with the ARN of your RAM rol
e that is obtained in the preceding step.
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
```

`}`

```
    return null;
```

`}`
3. Use the AccessKey pair assigned by STS to call an operation of a cloud service. The
following sample code provides an example on how to use the AccessKey pair assigned by STS to call the `DescribeZones` operation of Elastic Compute Service (ECS):

> **Note:** You must replace the variables in the following code with actual values. Delete the angle brackets (<>) before you submit the code.
> Variables:
> <yourRegionID>: Replace it with the actual region ID.
> <yourStsAccesskeyID>: Replace it with your AccessKey ID.
> <yourStsAccessKeySecret>: Replace it with your AccessKey secret.
> <yourStsToken>: Replace it with the security token of the AccessKey pair assigned by STS.
> <yourResourceGroupID>: Replace it with the actual resource set ID.
> <yourOrganizationID>: Replace it with the actual organization ID.

```java
public static void main(String[] args) {
    // Replace "<yourRegionID>" with the actual region ID.
    // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessK
ey ID and AccessKey secret of the AccessKey pair assigned by STS. The AccessKey ID an d AccessKey secret are obtained in the preceding step.
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
STS. The STS token is obtained in the preceding step.
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

`}` `}`

### 1.5 Obtain an endpoint

This topic describes how to obtain the endpoint of an Apsara Stack Security service.

**Background information**

If you want to call API operations in Apsara Stack by using the POP gateway, you must specify the endpoint of the corresponding cloud service. You can obtain an endpoint from onsite Apsara Stack O&M engineers. This topic describes how to obtain an endpoint.

**Procedure**

1. Log on to the Apsara Infrastructure Management console.
2. In the left-side navigation pane, click **Product & Cluster O&M**.
3. In the **Product | Cluster** search box, enter **yundun-advance**. Find the cluster whose
name contains **BasicThinCluster** and click **Cluster Details** in the Actions column.
4. On the **Desired State Configuration** tab, search for the **kv.conf** file and open the file. In
the file, find the **region** and **internet-domain** parameters.
5. Obtain the value of the **EndpointPre** parameter. For more information, see Common
parameters.
6. Obtain the endpoint based on the **region**, **internet-domain**, and **EndpointPre**
parameters. The endpoint of a cloud service is in the following format:

```
${EndpointPre}.${global:region}.${global:internet-domain}
```

**What to do next**

If you want to call the API operations of Apsara Stack Security services from the service domain or O&M domain, you must configure the hosts file on your computer.
1. Obtain the virtual IP address (VIP) of the POP.
i. Click **Back to Old Version** to switch to Apsara Infrastructure Management of the previous version. In the top navigation bar, choose **Operations > Cluster Operations**. ii. Enter **webappAll** in the **Project** search box and **StandardCloudCluster** in the **Cluster** search box. Click the name of the first **StandardCloudCluster** cluster. iii. In the **Cluster Resource** section, find the O&M domain, management domain, and service domain. Click the icon to the right of **Type**, select **Contains** from the dropdown list, and then enter `vip` in the Filter field.

> **Note:** The following list describes the cluster resources of the preceding domains:
> O&M domain: The value of the **Name** parameter of the cluster resource is **pop-vip-ops**.
> Management domain: The value of the **Name** parameter of the cluster resource is **pop-vip-mgmt**.
> Service domain: The value of the **Name** parameter of the cluster resource is **pop-vip-biz**.

iv. Right-click the value of the **Result** parameter of the O&M domain, management domain, or service domain. Click **Show More** and view the value of the **vip_ip** parameter in the Details dialog box.
2. Configure the following hosts file on your computer.

```xml
<vip_ip> <Endpoint of the API that you want to request>
```

## 2 Call examples

### 2.1 Call examples for SDK for Java

#### 2.1.1 Use SDK

##### 2.1.1.1 Install SDK for Java

This topic describes how to install and use Apsara Stack Security SDK for Java. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK. For more information, visit Alibaba Cloud SDKs. If you want to use Apsara Stack Security SDK for Java, you must install the core library of Apsara Stack SDK for Java. We recommend that you use V4.5.17 or later of the core library. When you install the core library, you must add the following dependency to the pom.xml file. For more information about the specific SDK version, visit Alibaba Cloud SDKs.

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

##### 2.1.1.2 Use CommonRequest to call API operations

> **Note:** If you want to call the API operations of a service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need to only download the core package. You do not need to download
and install SDKs of services.
2. Easy to use: You can call the newly released API operations of a service without the need to
update the SDK for the service.
3. Fast iteration.

**Use CommonRequest to call an API operation**

Apsara Stack services provide RPC and RESTful APIs. The request method of CommonRequest varies based on the style of the API that you want to call. In most cases, an API uses the RPC style if the API operations include the Action parameter. An API uses the RESTful style if the API operations include the PathPattern parameter. All API operations of a service use the same API style. The API of each service supports only one style. If you pass an invalid identifier, another API operation may be called, or the `ApiNotFound` error is returned. If you want to send a CommonRequest request, you must obtain the values of the following parameters. For more information about the values of these parameters, see the API reference in DocumentationDocumentation. You can also visit OpenAPI Explorer to obtain the parameter values of API operations for some services. Endpoint: the endpoint of a service. Version: the version of the API. The version is in the YYYY-MM-DD format. Operation information: the name of the API operation that you want to call. The APIs of most Apsara Stack services, such as Threat Detection Service, are RPC APIs. If you want to call an RPC API operation, you must obtain the value of the Action parameter, and then specify the value in the `request.ApiName = "<Action>"` format. If you want to call a RESTful API operation of a service, such as Container Service for Kubernetes (ACK), you must obtain the value of the PathPattern parameter, and then specify the RESTful path in the `request.PathPattern = "<PathPattern>"` format.

**Example: Call an RPC API operation**

The following sample code shows how to use CommonRequest to call an API operation of Apsara Stack Security:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // The ID of the region.
            "<your-access-key-id>",      // The AccessKey ID.
            "<your-access-key-secret>"); // The AccessKey secret.
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and specify parameters.
        CommonRequest request = new CommonRequest();
        request.setDomain("<your-endpoint>");// The endpoint of the service.
        request.setVersion("<API-version>");// The version of the API.
        request.setAction("<your-action>");// The name of the API operation.
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClientException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
```

`}` `}` `}`

### 2.2 Call examples for SDK for Python

**Python**

#### 2.2.1 Use SDK

##### 2.2.1.1 Install SDK for Python

This topic describes how to install and use SDK for Python. Apsara Stack SDK for Python supports Python 2.6.x, Python 2.7.x, and Python 3.x or later. You can install Apsara Stack SDK for Python by using pip.

> **Note:** To use the SDK of an Apsara Stack service, you must install the core library of Apsara Stack SDK for Python.

If you use Python 2.x, run the following command to install the core library:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library:

```
pip3 install aliyun-python-sdk-core-v3
```

##### 2.2.1.2 Use CommonRequest to call API operations

> **Note:** If you want to call the API operations of an Apsara Stack service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need only to download the core package. You do not need to download
and install SDKs of Apsara Stack services.
2. Easy to use: You can call the newly released API operations of an Apsara Stack service
without the need to update the SDK for the service.
3. Fast iteration.

**Use CommonRequest to call an API operation**

Apsara Stack services provide RPC and RESTful APIs. The request method of CommonRequest varies based on the style of the API that you want to call. In most cases, an API uses the RPC style if the API operations include the Action parameter. An API uses the RESTful style if the API operations include the PathPattern parameter. All API operations of a service use the same API style. The API of each service supports only one style. If you pass an invalid identifier, another API operation may be called, or the `ApiNotFound` error is returned. If you want to send a CommonRequest request, you must obtain the values of the following parameters. For more information about the values of these parameters, see the API reference in DocumentationDocumentation. You can also visit OpenAPI Explorer to obtain the parameter values of API operations for some services. Endpoint: the endpoint of a service. Version: the version of the API. The version is in the YYYY-MM-DD format. Operation information: the name of the API operation that you want to call. The APIs of most Apsara Stack services, such as Threat Detection Service, are RPC APIs. If you want to call an RPC API operation, you must obtain the value of the Action parameter, and then specify the value in the `request.ApiName = "<Action>"` format. If you want to call a RESTful API operation of a service, such as Container Service for Kubernetes (ACK), you must obtain the value of the PathPattern parameter, and then specify the RESTful path in the `request.PathPattern = "<PathPattern>"` format.

**Example: Call an RPC API operation**

The following sample code shows how to use the CommonRequest method to call the API operation:

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('<your-endpoint>') //The endpoint of the service. request.set_version('<API-version>') //The version of the API. request.set_action_name('<your-action>')//The name of the API operation.
# or:
# request = CommonRequest(domain='<your-endpoint>', version='<API-version>',
action_name='your-action') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

### 2.3 Call examples for SDK for Go

#### 2.3.1 Use SDK

##### 2.3.1.1 Install the core package of SDK for Go

This topic describes how to install the core package of SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

##### 2.3.1.2 Use CommonRequest to call API operations

> **Note:** If you want to call the API operations of an Apsara Stack service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need only to download the core package. You do not need to download
and install SDKs of Apsara Stack services.
2. Easy to use: You can call the newly released API operations of an Apsara Stack service
without the need to update the SDK for the service.
3. Fast iteration.

**Use CommonRequest to call an API operation**

Apsara Stack services provide RPC and RESTful APIs. The request method of CommonRequest varies based on the style of the API that you want to call. In most cases, an API uses the RPC style if the API operations include the Action parameter. An API uses the RESTful style if the API operations include the PathPattern parameter. All API operations of a service use the same API style. The API of each service supports only one style. If you pass an invalid identifier, another API operation may be called, or the `ApiNotFound` error is returned. If you want to send a CommonRequest request, you must obtain the values of the following parameters. For more information about the values of these parameters, see the API reference in DocumentationDocumentation. You can also visit OpenAPI Explorer to obtain the parameter values of API operations for some services. Endpoint: the endpoint of a service. Version: the version of the API. The version is in the YYYY-MM-DD format. Operation information: the name of the API operation that you want to call. The APIs of most Apsara Stack services, such as Threat Detection Service, are RPC APIs. If you want to call an RPC API operation, you must obtain the value of the Action parameter, and then specify the value in the `request.ApiName = "<Action>"` format. If you want to call a RESTful API operation of a service, such as Container Service for Kubernetes (ACK), you must obtain the value of the PathPattern parameter, and then specify the RESTful path in the `request.PathPattern = "<PathPattern>"` format.

**Example: Call an RPC API operation**

The following sample code shows how to use the CommonRequest method to call the API operation:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "fmt"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey("cn-hangzhou", "{your_access_key_id}", "{
your_access_key_secret}")
    if err != nil {
        panic(err)
```

`}`

```
    request := requests.NewCommonRequest()
    request.Domain = "<your-endpoint>"// The endpoint of the service.
    request.Version = "<API-version>"// The version of the API.
    request.ApiName = "<your-action>"// The name of the API operation.
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}`

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

| Product | Strin g | Yes | The name of the service to which the API operation belongs. Valid values: Auditprivate: basic components of Apsara Stack Security yundunnextsoc: Security Operations Center (SOC) Sas: Threat Detection Service aegis: Server Guard yundun-css: Container Production secspy: Network Detection and Response Ddosprivate: Anti-DDoS Service hsm-private: Data Encryption Service Cloudfw: Cloud Firewall Sddp: Sensitive Data Discovery and Protection (SDDP) semawaf: Web Application Firewall (WAF) soar: Security Orchestration and Automation Response (SOAR) |
|---|---|---|---|
| EndpointPre | Strin g | Yes | The prefix in the endpoint of the service to which the API operation belongs. Valid values: auditprivate: the prefix in the endpoint of basic components of Apsara Stack Security yundunnextsoc-pop: the prefix in the endpoint of SOC tds: the prefix in the endpoint of Threat Detection Service aegis: the prefix in the endpoint of Server Guard yundun-css: the prefix in the endpoint of Container Protection secspy-share: the prefix in the endpoint of Network Detection and Response ddosprivate: the prefix in the endpoint of Anti-DDoS Service hsmprivate: the prefix in the endpoint of Data Encryption Service cloudfw: the prefix in the endpoint of Cloud Firewall sddp-api: the prefix in the endpoint of SDDP semawaf: the prefix in the endpoint of WAF soar: the prefix in the endpoint of SOAR |

**Common response parameters**

API responses use the HTTP response format: A 2xx status code indicates a successful call. A 4xx or 5xx status code indicates a failed call. Responses are returned in the JSON format. Every response returns a unique RequestID regardless of whether the call is successful.

## 4 Network Traffic Monitoring System

**System**

### 4.1 Make API requests

#### 4.1.1 Request structure

Apsara Stack Security API operations use the RPC protocol. This topic describes the structure of API requests.

**Description**

You can call Apsara Stack Security API operations by sending HTTP requests. The request structure is as follows:

```
http://endpoint/?Action=xx&parameters
```

where:

|   | Endpoint |   | : The endpoin |
|---|---|---|---|
| [RegionId].example.com |   |   |   |
|   | Action | : the name of t |   |

`Endpoint` : The endpoint of the Network Traffic Monitoring System API is `secspy.` `Action` : the name of the operation being performed. For example, to query the Apsara Stack Security features that are deployed, you must set the Action parameter to DescribeFeatures. `Parameters` : the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operationspecific parameters. Common parameters include information such as the API version number and authentication information. For more information about operation-specific parameters, see the corresponding operation description.

**Example**

The following example demonstrates how to call the DescribeFeatures operation to query the Apsara Stack Security features that are deployed:

```
https://secspy.[RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-test&For mat=JSON&SecureTransport=true&SignatureMethod=HMAC- SHA1&SignatureNonce=15215528852396&SignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2019- 12-02Txxxxxxx&Version=2019-08-05&Signature=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```
https://secspy.[RegionId].example.com/?Action=DescribeFeatures &Format=JSON &Version=2019-08-05 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2019-12-02T12:00:00Z
```

#### 4.1.2 Request signatures

Apsara Stack Security authenticates each access request. Therefore, a request must contain signature information regardless of whether it is sent over HTTP or HTTPS.

**Authorization**

To ensure the security of your account, we recommend that you use a Resource Access Management (RAM) user to call API operations. Before you use a RAM user to call an API operation, you must grant the RAM user the required permissions by creating a policy and attaching the policy to the RAM user.

**Signature**

You must sign all API requests to ensure security. Alibaba Cloud uses the request signature to verify the identity of the API caller. When you manually make an API request, you must use the AccessKey secret to calculate an HMAC value based on the encoded and sorted request string. The HMAC value is the signature. For more information, see the definition in RFC 2104. This section uses the raw access parameters in the following table to describe how to create an operation signature.

| Parameter | Description |
|---|---|
| Endpoint | http://secspy.[RegionId].example.com/? |
| Operation-specific parameters | Action=DescribeFeatures |
| Common parameters except Signature | &Timestamp=2019-12-01T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2019-08-05 &SignatureVersion=1.0 |
| AccessKey secret | <yourAccessKeySecret> |

1. Create a canonicalized query string by arranging the request parameters.

> **Important:** The request parameters include operation-specific parameters and all common request parameters except Signature.

i. Sort the request parameters. Sort the request parameters (including all common and operation-specific parameters except **Signature**) in alphabetical order.

> **Note:** If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?).

ii. Encode the parameters. Encode the canonicalized query string in UTF-8 based on the following rules: Uppercase letters, lowercase letters, digits, and some special characters such as hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded. Other characters must be percent encoded in the %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22. Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20. Do not encode spaces as plus signs (+). iii. Connect the encoded parameter names and their values with equal signs (=). iv. Sort the parameters in the order specified in the Sort parameters step and connect them with ampersands (&) to produce a canonicalized query string.
2. Create a string-to-sign from the encoded canonicalized query string.

```
StringToSign=HTTPMethod + "&" + percentEncode("/") + "&" + percentEncode(CanonicalizedQueryString)
```

3. Calculate the HMAC value of the string-to-sign based on RFC 2104.

> **Note:** Use the SHA1 algorithm to calculate the HMAC value of the string-to-sign. The AccessKey secret to which an ampersand (&) (ASCII:38) is appended is used as the key for HMAC calculation.

4. Encode the HMAC value in Base64 to obtain the signature string.

```
LEW8N4y7Uasop******
```

5. Add the signature string to the request as the Signature parameter.

#### 4.1.3 Common parameters

Common request parameters must be included in all Apsara Stack Security API requests, such as the API version number and authentication information.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The version number of the API. The value is in the format of YYYY-MM-DD. Set the value to 2019-08-05. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. |

| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |
|---|---|---|---|
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. For example, use 2019-12- 01T12:00:00Z to indicate 12:00:00, December 1, 2019 in UTC+8. |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |
| SignatureNonce | String | Yes | A unique random number used to prevent replay attacks. You must use different numbers for different requests. |
| ResourceOwnerA ccount | String | No | The Alibaba Cloud account to which the resource you want to access belongs. |
| Format | String | No | The response format. Valid values: JSON or XML. Note Default value: XML. |

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

### 4.2 API documentation

This is the API reference content

#### 4.2.1 API Reference (2023-04-03 )

##### 4.2.1.1 DescribePlaybook

Queries script information.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| PlaybookI d | Strin g | Query | No | 1 | Script id (script id, script name, script uuid must be specified). |
| PlaybookU uid | Strin g | Query | No | bdeaa8bc-a003-4a9a- b37c-249d64a41ba2 | The script UUID (script id, script name, and script UUID must be specified). |
| PlaybookN ame | Strin g | Query | No | Test script | The script name (script id, script name, script uuid must be specified). |
| TaskflowM d5 | Strin g | Query | No | 58638e2be58a4185f510 6298fb3e5157 | Md5 information of the script's configuration file. |

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| DebugFla g | Integ er | Query | No | 1 | 0 indicates a playbook request in the publish state. 1 indicates that the script in the edit state is requested. 2 indicates that the script of the historical version is requested (taskFlowMd5 must have a value). |
| TaskTena ntId | Strin g | Query | No | -999999 | The information about the tenant. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RequestId | String | 65C02B7B-C23D- 4929-A378- 11EB59813141 | The request ID. |
| Playbook | Struct |   | The details of the playbook. |
| -Active | Boolean | true | The status of the playbook. Valid values: true: enabled. false: disabled. |
| - Compiledresul t | String |   | The compilation result of the playbook. |
| -Creator | String | sys | The user who created the playbook. |
| -Description | String |   | The description of the playbook. |
| -DomainId | String | ids-group | The tenant information of the playbook. |
| -GmtCreate | Long | 1642066923992 | The time at which the playbook was created. The value is a 13-byte timestamp. Unit: milliseconds. |
| -GmtModified | Long | 1642066923992 | The time at which the playbook was last modified. The value is a 13-byte timestamp. Unit: milliseconds. |

| loud Security Net and Response | work Detectio |   | Developer·Network Traffic Moni oring System |
|---|---|---|---|

| Parameter | Type | Examples | Description |
|---|---|---|---|
| -Id | Long | 582 | The ID of the script. |
| -Inputtype | String | event | The input type. |
| -InputParams | String | [{"name":"compon ent name","dataTy _ pe":"String","descri ption":"Component name","required":f alse,"stanchDefault Value":""}, {"name":"version", "dataType":"String ","description":"Co mponent version","required" :false,"stanchDefau ltValue":""}] | The input parameters of the playbook. |
| -Modifier | String | yundunluck | The person who modified the configurations. |
| -Name | String | test1 | The name of the flow. |
| -DisplayName | String | Test script | The display name of the playbook. |
| -OnlineActive | Boolean | true | The status of the playbook. Valid values: true: enabled. false: disabled. |
| - OnlineCompile dresult | String |   | The compilation result of the playbook in the production environment. |
| -OnlineOss | String | ophon-gen/****- ba81cd3cc999- 1641814492160- beaver linkage att _ _ ack ban v62 test.j _ _ _ ar | the oss address of the online editing result. |
| -Oss | String | ophon-gen/****- ba81cd3cc999- 1641814492160- beaver linkage att _ _ ack ban v62 test.j _ _ _ ar | The OSS address. |
| -Cron | String | 0 0 9 * * ? | The scheduling configurations for the playbook. |

| Developer·Networ ring System | k Traffic Monit |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|

| Parameter | Type | Examples | Description |
|---|---|---|---|
| -TriggerInfo | String | {"Query start time":"2022-01-05 10:10:10","Query end time":"2022- 01-05 10:10:10"} | The information that is used to manually run the playbook. |
| -OperateType | String | general | The operation type of the playbook. |
| -OwnType | String | user | The ownership type of the playbook. Valid values: user: user-defined. sys: built-in. |
| -Owner | String | sys | The owner of the playbook. |
| -Taskconfig | String | {\"apps\": [{\"actions\": [{\"customInput\":t rue,\"description\":\ "Call an API operation\",\"id\":0, \"name\":\"execute API\" | The configuration file of the playbook. |
| -Taskflow | String |   | The information about the component on which the playbook depends. |
| -TenantId | String | -99999 | The information about the tenant to which the flow belongs. |
| -ExecuteMode | String | one | The execution method of the playbook. Valid values: one: manual triggering. mul: timing trigger. strema: streaming trigger. |
| - OnlineExecute Mode | String | one | The trigger mode of the online process: one: manual triggering. mul: timing trigger. strema: streaming trigger. |
| - OutputParams | String | {"ip":"***"} | The output information of the process. |
| -RightLevel | String |   |   |
| -PlaybookUuid | String | bdeaa8bc-a003- 4a9a-b37c- 249d64a41ba2 | The unique ID of the flow. |

| Cloud Security Ne and Response | twork Detectio |   | Developer·Network Traffic Moni oring System |
|---|---|---|---|

| Parameter | Type | Examples | Description |
|---|---|---|---|
| - PlaybookStatu s | Integer | 1 | Whether the process has been published before: 1: posted. 0: has not been published. |

**Examples**

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "Playbook":{
  "Owner":"sys",
  "Description":"",
  "GmtModified":1642066923992,
  "Creator":"sys",
  "OnlineExecuteMode":"one",
  "Cron":"0 0 9 * * ?",
  "Name":"test1",
  "Taskconfig":"{\\\"apps\\\":[{\\" actions\\\":[{\\\"customInput\\\":true ,\\" descrip
tion\\\":\\" Execute an openAPI call \\\\ ",\\\",\\\" id \\\:\":0 ,\\ "e \\"
  "Compiledresult":"",
  "InputParams":"[{" name ":" component_name "," dataType ":" String "," description ":
" Component name "," required ":false," stanchDefaultValue ":"},{"name":"version", "dat aType" "String", "description":"Component version", "required":false, "stanchDefaultValue":"}] ",
  "OwnType":"user",
  "OnlineActive":true,
  "DisplayName":"Test script",
  "PlaybookStatus":1,
  "Inputtype":"event",
  "ExecuteMode":"one",
  "OutputParams":"{\"ip\":\"***\"}",
  "Modifier":"yundunluck",
  "OperateType":"general",
  "RightLevel":"",
  "Taskflow":"<?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\"?><bpmn:definitions xmlns
:xsi=\\\"http://www.w3.org/2001/XMLSchema-instance\\",
  "TriggerInfo":"{\" Query start time \":\"2022-01-05 10:10:10\",\" Query end time \":\
"2022-01-05 10:10:10\"} ",
  "Oss":"ophon-gen/****-ba81cd3cc999-1641814492160-
beaver_linkage_attack_ban_v62_test.jar",
  "PlaybookUuid":"bdeaa8bc-a003-4a9a-b37c-249d64a41ba2",
  "Active":true,
  "GmtCreate":1642066923992,
  "TenantId":"-99999",
  "DomainId":"ids-group\t",
  "OnlineOss":"ophon-gen/****-ba81cd3cc999-1641814492160-
beaver_linkage_attack_ban_v62_test.jar",
  "OnlineCompiledresult":"",
  "Id":582
```

`},`

```json
 "RequestId":"65C02B7B-C23D-4929-A378-11EB59813141\t"
```

`}` `XML` format

```xml
<Playbook>
 <Owner>sys</Owner>
 <Description  />
 <GmtModified>1642066923992</GmtModified>
```

`<C` `t` `>`

```
</C
```

`t` `>`

```xml
 <Creator>sys</Creator>
 <OnlineExecuteMode>one</OnlineExecuteMode>
 <Cron>0 0 9 * * ?
 </Cron>
 <Name>test1</Name>
 <Taskconfig>{\&quot;apps\&quot;:[{\&quot;actions\&quot;:
[{\&quot;customInput\&quot;:true,\&quot;description\&quot;: Execute an openAPI call \&q uot;&quot;,\&quot;id \API \quot;&quot;&quot; 0:
 </Taskconfig>
 <Compiledresult  />
 <InputParams>[&
{quot;name&quot;:&quot;component_name&quot;,&quot;dataType&quot;:&quot;description&quot;& ot;&quot;component name&quot;&quot;&quot;required&quot;&quot;:&quot;stanchDefaultValue dataType&quot;:&quot;String&quot;,&quot;description&quot;:&quot; Component Version&quot;,&quot;required&quot;:false,&quot;&quot;stanchDefaultValue&quot;:&quot;&quot quot;&quot;&quot;}]
 </InputParams>
 <OwnType>user</OwnType>
 <OnlineActive>true</OnlineActive>
 <DisplayName> Test script </DisplayName>
 <PlaybookStatus>1</PlaybookStatus>
 <Inputtype>event</Inputtype>
 <ExecuteMode>one</ExecuteMode>
 <OutputParams>{&quot;ip&quot;:&quot;***&quot;}
 </OutputParams>
 <Modifier>yundunluck</Modifier>
 <OperateType>general</OperateType>
 <RightLevel  />
 <Taskflow>&lt;?xml version=\&quot;1.0\&quot; encoding=\&quot;UTF-8\&quot;?
&gt;&lt;bpmn:definitions xmlns:xsi=\&quot;http://www.w3.org/2001/XMLSchema-instance\
 </Taskflow>
 <TriggerInfo>{&quot; Query start time&quot;&quot;2022-01-05 10:10:10&quot;&quot; Query
end time&quot;:&quot;2022-01-05 10:10:10&quot;&quot;}
 </TriggerInfo>
 <Oss>ophon-gen/****-ba81cd3cc999-1641814492160-beaver_linkage_attack_ban_v62_test.jar
 </Oss>
 <PlaybookUuid>bdeaa8bc-a003-4a9a-b37c-249d64a41ba2
 </PlaybookUuid>
 <Active>true</Active>
 <GmtCreate>1642066923992</GmtCreate>
 <TenantId>-99999</TenantId>
 <DomainId>ids-group
 </DomainId>
 <OnlineOss>ophon-gen/****-ba81cd3cc999-1641814492160-
beaver_linkage_attack_ban_v62_test.jar
 </OnlineOss>
 <OnlineCompiledresult  />
 <Id>582</Id>
</Playbook> <RequestId>65C02B7B-C23D-4929-A378-11EB59813141 </RequestId>
```

##### 4.2.1.2 DescribeSoarRecords

Queries the execution history of a playbook.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Query | Yes | 1 | The page number of the returned page. |
| PageSize | Integ er | Query | Yes | 10 | The number of entries per page. |
| QueryCon dition | Strin g | Query | No | {\"type\":\"complex\",\"c ondition\":\" {\\\"condition\\\":\\\"AND\ \\",\\\"rules\\\": [{\\\"field\\\":\\\"taskNam e\\\",\\\"match\\\":\\\"is\\\ ",\\\"type\\\":\\\"string\\\", \\\"value\\\": [\\\"test rtap\\\"]}]}\"} _ | The query conditions. The value of this parameter includes the following fields: field: indicates the field to be matched. The value: represents the value to match. type: represent the type of match, as follows: match: means equal to. contains: means contains. A complex: indicates a subquery that can be nested. The subquery follows the preceding rules. |

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| TaskUuid | Strin g | Query | No | 73b14357-e011-4993- a769-bfb779ab3638 | The UUID of the task that is generated when the playbook is run. You can obtain the UUID from TriggerUuid by calling the TriggerPlaybook operation. If you specify TriggerUuid , the value of QueryCondition does not take effect. |
| PlaybookN ame | Strin g | Query | No | Test script | The ID of the playbook. |
| TriggerUs er | Strin g | Query | No | user | The name of the user who triggered the script. |
| TaskStatu s | Strin g | Query | No | success | Script running status: success: success. failed: failed inprogress: is running. |
| PlaybookU uid | Strin g | Query | No | 77dd60ec-a788-4cc9- a930-bedcfca4ce5f | The unique ID of the script run. |
| TaskflowM d5 | Strin g | Query | No | 58638e2be58a4185f510 6298fb3e5157 | The Md5 information of the configuration file of the process. |
| TaskType | Strin g | Query | No | general | The type of the sub- task. |
| StartMillis | Strin g | Query | No | 1695107717298 | The start time node of the query. |
| EndMillis | Strin g | Query | No | 1695194117298 | The end time of the query. |

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| RequestU uid | Strin g | Query | No | bdeaa8bc-a003-4a9a- b37c-249d64a41ba2 | The UUID of the task that is generated when the playbook is run. |
| TriggerTy pe | Strin g | Query | No | stream | Trigger type: stream: streaming. manual: labor. schedule: timing scheduling. trace: war room. |
| EventId | Strin g | Query | No | 1 | The ID of the event. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| SoarExecuteR ecords | Array | [] | An array that consists of details of the execution history. |
| -Id | Long | 1 | The ID of the query record. |
| -RequestUuid | String | a5a60946-3ad4- 4e0d-92db- 500da9619793 | The UUID of the task that is generated when the playbook is run. |
| - PlaybookName | String | Test | The ID of the playbook. |
| -TriggerType | String | manual | The type of the trigger. |
| -TriggerUser | String | 12385**452 | The user who triggers the playbook. The value is the ID of the account that is used for logon and API calls. |
| -TenantId | String | -999999 | The tenant information. |
| -TaskTenantId | String | -1 | The information about the tenant that triggered the task. |
| -ResultStatus | String | success | The status of the script execution. |
| -TaskStatus | String | TaskStatus | The state of the task. |

| loud Security Ne and Response | twork Detectio |   | Developer·Network Traffic Moni oring System |
|---|---|---|---|
| Parameter | Type | Examples | Description |
| -TaskflowMd5 | String | 58638e2be58a418 5f5106298fb3e515 7 | The Md5 information of the configuration file of the process. |
| -PlaybookUuid | String | bdeaa8bc-a003- 4a9a-b37c- 249d64a41ba2 | The unique key ID of the script. |
| -EndTime | Long | 1695179134000 | The end time of the task execution. |
| -StartTime | Long | 1695179131000 | The start time of the task execution. |
| -FlowTag | Integer | 1 | Whether the executed task is an officially released script 0: no. 1: yes. |
| RequestId | String | 1C982EAB-D314- 4583-B108- 62F20DE02CD5 | The UUID of the task that is generated when the playbook is run. |
| PageSize | Integer | 1 | Paging information, page number. |
| PageNumber | Integer | 10 | The amount of data returned on each page. |
| TotalCount | Integer | 50 | The total amount of data. |

**Examples**

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "TotalCount":50,
 "RequestId":"1C982EAB-D314-4583-B108-62F20DE02CD5",
 "PageSize":1,
 "PageNumber":10,
 "SoarExecuteRecords":{
  "TriggerType":"manual",
  "EndTime":1695179134000,
  "ResultStatus":"success",
  "TaskTenantId":"-1",
  "StartTime":1695179131000,
  "PlaybookName":"Test",
  "TaskStatus":"TaskStatus",
  "TriggerUser":"\t12385**452\t",
  "PlaybookUuid":"bdeaa8bc-a003-4a9a-b37c-249d64a41ba2",
  "TenantId":"-999999",
  "Id":1,
  "RequestUuid":"a5a60946-3ad4-4e0d-92db-500da9619793\t",
  "TaskflowMd5":"58638e2be58a4185f5106298fb3e5157",
  "FlowTag":1
```

`}` `}` `XML` format

```xml
<TotalCount>50</TotalCount> <RequestId>1C982EAB-D314-4583-B108-62F20DE02CD5</RequestId> <PageSize>1</PageSize> <PageNumber>10</PageNumber> <SoarExecuteRecords>
 <TriggerType>manual</TriggerType>
 <EndTime>1695179134000</EndTime>
 <ResultStatus>success</ResultStatus>
 <TaskTenantId>-1</TaskTenantId>
 <StartTime>1695179131000</StartTime>
 <PlaybookName> Test </PlaybookName>
 <TaskStatus>TaskStatus</TaskStatus>
 <TriggerUser>
12385**452 </TriggerUser>
  <PlaybookUuid>bdeaa8bc-a003-4a9a-b37c-249d64a41ba2</PlaybookUuid>
  <TenantId>-999999</TenantId>
  <Id>1</Id>
  <RequestUuid>a5a60946-3ad4-4e0d-92db-500da9619793
  </RequestUuid>
  <TaskflowMd5>58638e2be58a4185f5106298fb3e5157</TaskflowMd5>
  <FlowTag>1</FlowTag>
 </SoarExecuteRecords>
```

##### 4.2.1.3 PublishPlaybook

Publish the script interface.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| PlaybookU uid | Strin g | Query | No | bdeaa8bc-a003-4a9a- b37c-249d64a41ba2 | The unique key ID of the script. |
| Descriptio n | Strin g | Query | No | Release Script | The release description of the script. |
| State | Boole an | Query | Yes | false | The status of the playbook. Valid values: true: the publishing process. false: disable the process. |
| Restart | Boole an | Query | Yes | false | Specifies whether to restart the playbook. Valid values: true: stop first, then publish. false: posted directly. |
| PicUrl | Strin g | Query | No | http://sophon-gen/-4a86- aa76-8705e4fc6988.jpg | The URL of the process image. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RequestId | String | 913BE26B-F9CC- 4A84-8CEC- 190E4BADD246 | The ID of the call. |

**Examples**

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"913BE26B-F9CC-4A84-8CEC-190E4BADD246"
```

`}` `XML` format

```xml
<RequestId>913BE26B-F9CC-4A84-8CEC-190E4BADD246 </RequestId>
```

##### 4.2.1.4 TriggerPlaybook

Runs a playbook.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| PlaybookU uid | Strin g | Query | No | bdeaa8bc-a003-4a9a- b37c-249d64a41ba2 | The unique key ID of the script. |
| PlaybookN ame | Strin g | Query | No | Test script | The ID of the playbook. |
| InputPara m | Strin g | Query | Yes | {"name":"test","ip":"10. 123.xx.xx"} | The parameters that are used to run the playbook. Specify the custom input parameters of the playbook. |
| TriggerTy pe | Strin g | Query | No | manual | Trigger type: one: manual triggering. mul: timing trigger. strema: streaming trigger. |
| TaskTena ntId | Strin g | Query | No | -999999 | Triggers a script to add script tenant information. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RequestId | String | 0E402C78-34DC- 4B2B-BB15- 73BB914172C1 | The request ID. |
| RequestUuid | String | a5a60946-3ad4- 4e0d-92db- 500da9619793 | The UUID of the task that is generated when the playbook is run. You can stop the task or query the result of the task by using the UUID. |

**Examples**

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"0E402C78-34DC-4B2B-BB15-73BB914172C1",
 "RequestUuid":"a5a60946-3ad4-4e0d-92db-500da9619793"
```

`}` `XML` format

```xml
<RequestId>0E402C78-34DC-4B2B-BB15-73BB914172C1 </RequestId> <RequestUuid>a5a60946-3ad4-4e0d-92db-500da9619793 </RequestUuid>
```

#### 4.2.2 DescribeSoarRecordActions

Queries the records of an action node.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Query | Yes | 1 | The page number. |
| PageSize | Integ er | Query | Yes | 10 | The number of entries returned on each page. |

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| RequestU uid | Strin g | Query | No | 73b14357-e011-4993- a769-bfb779ab3638 | The UUID of the task that is generated when the playbook is run. |
| QueryCon dition | Strin g | Query | Yes | {\"type\":\"complex\",\"c ondition\":\" {\\\"condition\\\":\\\"AND\ \\",\\\"rules\\\": [{\\\"field\\\":\\\"taskNam e\\\",\\\"match\\\":\\\"is\\\ ",\\\"type\\\":\\\"string\\\", \\\"value\\\": [\\\"test rtap\\\"]}]}\"} _ | The query conditions. The value of this parameter includes the following fields: field: indicates the field to be matched. The value: represents the value to match. type: represent the type of match, as follows: match: means equal to. contains: means contains. A complex: indicates a subquery that can be nested. The subquery follows the preceding rules. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RecordActions | Array |   | A record of the action. |
| -Action | String | SubTaskFlow | The node name. |
| -ActionUuid | String | 7ab8a0c7-5ba7- 45b3-9086- 82bcc5182073-186 | The UUID of the node. |
| -AssetName | String |   | The name of the asset. |
| -Component | String | dataTranform | The component name. |
| - DataSourceNa me | String |   | The name of the data source. |
| -EndTime | String | 1695345688134 | The time when the sub-task ends. |

| loud Security Net and Response | work Detectio |   | Developer·Network Traffic Moni oring System |
|---|---|---|---|
| Parameter | Type | Examples | Description |
| -EventId | String | 1 | The ID of the event. |
| -NodeName | String | Parameter processing | The name of the node. |
| -TaskName | String | beaver waf applic _ _ ation ban v62 _ _ | The name of the flow. |
| -RequestUuid | String | 3e4796fb-83e0- 4810-99a4- de22598066a5 | The UUID of the node. |
| -StartTime | Long | 1695345688133 | The start time of the node. |
| -endTime | Long | 1695345688134 | The end time of the node. |
| -Status | String | success | The status of the node. |
| -TaskUuid | String | 86252583-0f66- 4ab2-b0c5- 2036449b80e0 | The UUID of the flow. |
| -TriggerDataId | String |   | The ID of the scheduled task. This parameter is included when the script is scheduled. |
| -TriggerType | String |   | The type of the timed script trigger (included when the script is scheduled for execution). |
| -TenantId | String | -999999 | The information about the script tenant. |
| -TaskTenantId | String | -2 | The information about the tenant that triggered the task. |
| -TaskType | String | general | The type of the task. Valid values: general: the script. standard: standard action. |
| RequestId | String | BA548717-9E9A- 463B-AE72- 7B1CB6E866F7 | The UUID of the port. |
| PageSize | Integer | 1 | The page number. |

| Parameter | Type | Examples | Description |
|---|---|---|---|
| PageNumber | Integer | 10 | The number of entries returned on each page. |
| TotalCount | Integer | 50 | The total amount of data. |

**Examples**

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "TotalCount":50,
 "RecordActions":{
  "Status":"success",
  "TriggerType":"",
  "Action":"SubTaskFlow",
  "ActionUuid":"7ab8a0c7-5ba7-45b3-9086-82bcc5182073-186",
  "EndTime":"1695345688134",
  "NodeName":"Parameter processing",
  "StartTime":1695345688133,
  "TaskUuid":"86252583-0f66-4ab2-b0c5-2036449b80e0",
  "TaskTenantId":"-2",
  "AssetName":"",
  "TriggerDataId":"",
  "TenantId":"-999999",
  "DataSourceName":"",
  "TaskName":"beaver_waf_application_ban_v62",
  "TaskType":"general",
  "EventId":"1",
  "endTime":1695345688134,
  "Component":"dataTranform",
  "RequestUuid":"3e4796fb-83e0-4810-99a4-de22598066a5"
```

`},`

```json
 "RequestId":"BA548717-9E9A-463B-AE72-7B1CB6E866F7",
 "PageSize":1,
 "PageNumber":10
```

`}` `XML` format

```xml
<TotalCount>50</TotalCount> <RecordActions>
 <Status>success</Status>
 <TriggerType  />
 <Action>SubTaskFlow</Action>
 <ActionUuid>7ab8a0c7-5ba7-45b3-9086-82bcc5182073-186</ActionUuid>
 <EndTime>1695345688134</EndTime>
 <NodeName> Parameter processing </NodeName>
 <StartTime>1695345688133</StartTime>
 <TaskUuid>86252583-0f66-4ab2-b0c5-2036449b80e0</TaskUuid>
 <TaskTenantId>-2</TaskTenantId>
 <AssetName  />
 <TriggerDataId  />
 <TenantId>-999999</TenantId>
 <DataSourceName  />
 <TaskName>beaver_waf_application_ban_v62</TaskName>
 <TaskType>general</TaskType>
 <EventId>1</EventId>
 <endTime>1695345688134</endTime>
 <Component>dataTranform</Component>
 <RequestUuid>3e4796fb-83e0-4810-99a4-de22598066a5</RequestUuid>
</RecordActions> <RequestId>BA548717-9E9A-463B-AE72-7B1CB6E866F7</RequestId> <PageSize>1</PageSize> <PageNumber>10</PageNumber>
```

#### 4.2.3 GetPlaybookTriggerResult

Query script returns results.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| RequestU uid | Strin g | Query | Yes | 318D7C63-6035-4D2D- 95A9-0F8DE90970C4 | The ID of the trigger script request. |
| NodeNam e | Strin g | Query | No | action | The node name. |
| PageNum ber | Integ er | Query | Yes | 1 | Indicates the page number of the returned page. |

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | Yes | 10 | The number of entries returned on each page. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| SaoExecuteDe tailInfoList | Array |   | Detailed results. |
| -Content | String | {} | The content. |
| -NodeName | String | test | The name of the node. |
| -ActionUuid | String | 7c0c9f-7793-4g67- uu35- h7af44324849 | The UUID of the action. |
| RequestId | String | 6998644F-A6DE- 4988-AEB6- 4B043B8BD1B0 | The ID of the interface. |
| RequestUuid | String | 7b8d0f5b-8818- 4f57-acc6- c3ac44482339 | The request ID. |
| PlaybookUuid | String | 318D7C63-6035- 4D2D-95A9- 0F8DE90970C4 | The UUID of the script. |
| ResultStatus | String | success | Result status: inprogress: processing. success: success. failed: failed. |
| ErrorMsg | String | Error message | If the status is Error, the error message is included. |
| PageSize | Integer | 1 | Indicates the page number of the returned page. |
| PageNumber | Integer | 10 | The number of entries returned on each page. |
| TotalCount | Integer | 50 | The total amount of data. |

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "PlaybookUuid":"318D7C63-6035-4D2D-95A9-0F8DE90970C4",
 "TotalCount":50,
 "RequestId":"6998644F-A6DE-4988-AEB6-4B043B8BD1B0",
 "PageSize":1,
 "ResultStatus":"success",
 "PageNumber":10,
 "ErrorMsg":"Error message",
 "RequestUuid":"7b8d0f5b-8818-4f57-acc6-c3ac44482339",
 "SaoExecuteDetailInfoList":{
  "ActionUuid":"7c0c9f-7793-4g67-uu35-h7af44324849",
  "NodeName":"test",
  "Content":"{}"
```

`}` `}` `XML` format

```xml
<PlaybookUuid>318D7C63-6035-4D2D-95A9-0F8DE90970C4 </PlaybookUuid> <TotalCount>50</TotalCount> <RequestId>6998644F-A6DE-4988-AEB6-4B043B8BD1B0 </RequestId> <PageSize>1</PageSize> <ResultStatus>success</ResultStatus> <PageNumber>10</PageNumber> <ErrorMsg> Error message </ErrorMsg> <RequestUuid>7b8d0f5b-8818-4f57-acc6-c3ac44482339</RequestUuid> <SaoExecuteDetailInfoList>
 <ActionUuid>7c0c9f-7793-4g67-uu35-h7af44324849
 </ActionUuid>
 <NodeName>test</NodeName>
 <Content>{}</Content>
</SaoExecuteDetailInfoList>
```

#### 4.2.4 TriggerPlaybookAndWait

Triggers a script without returning a result.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| PlaybookU uid | Strin g | Query | No | 318D7C63-6035-4D2D- 95A9-0F8DE90970C4 | Script UUID (script UUID and script name must be passed). |
| PlaybookN ame | Strin g | Query | No | Test script | Script name (script UUID and script name must be passed). |
| InputPara m | Strin g | Query | Yes | { "input":"12312" } | The input parameter of the script, which can be used as an event. |
| TaskTena ntId | Strin g | Query | No | -999999 | The tenant information. |
| MaxWaitS econds | Integ er | Query | Yes | 5 | The maximum wait time. Unit: seconds. The maximum wait time is 25 seconds. |
| PageNum ber | Integ er | Query | Yes | 1 | Indicates the page number of the returned page. |
| PageSize | Integ er | Query | Yes | 10 | The number of entries returned on each page. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| SaoExecuteDe tailInfoList | Array |   | Detailed results. |
| -Content | String | {} | The content information. |
| -NodeName | String | action | The name of the node. |
| -ActionUuid | String | b266e528-d360- 42f0-8ae2- 955ac82d1692 | The UUID of the action node. |
| RequestId | String | 6998644F-A6DE- 4988-AEB6- 4B043B8BD1B0 | The UUID of the port. |

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RequestUuid | String | 7b8d0f5b-8818- 4f57-acc6- c3ac44482339 | The ID of the request. |
| PlaybookUuid | String | 318D7C63-6035- 4D2D-95A9- 0F8DE90970C4 | The UUID of the script. |
| ResultStatus | String | success | Task execution result: inprogress: processing. success: success. failed: failed. |
| ErrorMsg | String | msg | If the status is Error, the error message is included. |
| PageSize | Integer | 10 | The number of entries returned on each page. |
| PageNumber | Integer | 1 | Indicates the page number of the returned page. |
| TotalCount | Integer | 50 | The total amount of data. |

**Examples**

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "PlaybookUuid":"318D7C63-6035-4D2D-95A9-0F8DE90970C4",
 "TotalCount":50,
 "RequestId":"6998644F-A6DE-4988-AEB6-4B043B8BD1B0",
 "PageSize":10,
 "ResultStatus":"success",
 "PageNumber":1,
 "ErrorMsg":"msg",
 "RequestUuid":"7b8d0f5b-8818-4f57-acc6-c3ac44482339",
 "SaoExecuteDetailInfoList":{
  "ActionUuid":"b266e528-d360-42f0-8ae2-955ac82d1692",
  "NodeName":"action",
  "Content":"{}"
```

`}` `}` `XML` format

```xml
<PlaybookUuid>318D7C63-6035-4D2D-95A9-0F8DE90970C4</PlaybookUuid> <TotalCount>50</TotalCount> <RequestId>6998644F-A6DE-4988-AEB6-4B043B8BD1B0</RequestId> <PageSize>10</PageSize> <ResultStatus>success</ResultStatus> <PageNumber>1</PageNumber> <ErrorMsg>msg</ErrorMsg> <RequestUuid>7b8d0f5b-8818-4f57-acc6-c3ac44482339</RequestUuid> <SaoExecuteDetailInfoList>
 <ActionUuid>b266e528-d360-42f0-8ae2-955ac82d1692</ActionUuid>
 <NodeName>action</NodeName>
 <Content>{}</Content>
</SaoExecuteDetailInfoList>
```

#### 4.2.5 CreateEventByAlert

Creates a case based on a threat event that is reported by Security Operations Center (SOC).

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| DocId | Strin g | Query | No | 1 | The docId of the threat event data in an Elasticsearch index. |
| BatchCod e | Strin g | Query | No | 20212045 | The batch code of the threat event data. You can use the code to associate the threat event with raw error logs. |
| EsIndex | Strin g | Query | No | soc-alarms | The name of the Elasticsearch index to which the threat event belongs. |
| Name | Strin g | Query | No | SOAR-Webshell event | The name of the case. |

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| Severity | Strin g | Query | No | information | The level of the threat event. Valid values: information : Information. suspicious general : General. serious urgent : urgent. |
| Type | Strin g | Query | No | networkScanning | The type of the threat. Valid values: networkScanning : Network scanning. exploitVulnerabilit y : Exploit. maliciousSoftwar e : Malware. networkAttack : cyber attacks. riskConnection : Risk Connection. abnormalBehavio r : Abnormal behavior. illegalAccount : illegal rights. |
| SourceIps | Strin g | Query | No | [{"ip":"12.12.XX.XX","po rt":1XX3,"location":"Chin a"}] | The list of source IP addresses. |
| DestIps | Strin g | Query | No | [{"ip":"12.12.XX.XX","po rt":1XX4,"location":"Chin a"}] | The list of destination IP addresses. |
| StartTime | Long | Query | No | 1641540484251 | The start time of the case. The value is a 13- byte timestamp. Unit: milliseconds. |
| ThreatTim e | Long | Query | No | 1641540484251 | The beginning of the time range for the threat event. The value is a 13-byte timestamp. Unit: milliseconds. |

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| EndTime | Long | Query | No | 1641540484251 | The end time of the case. The value is a 13- byte timestamp. Unit: milliseconds. |
| AttCks | Strin g | Query | No | attack | The attack tag. |
| Suggestio ns | Strin g | Query | No | Handling suggestion | The suggestions to handle the threat event. |
| Descriptio n | Strin g | Query | No | Threat description | The description of the threat event. |
| AlertAliuid | Long | Query | No | 109898459283 | The Alibaba Cloud user ID of the person who executed the event. |
| Aliuid | Long | Query | No | 109898459283 | The Alibaba Cloud user ID of the tenant. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RequestId | String | 3BB85AD2-E1D2- 45C5-B22B- 949CBC9BD98B | The request ID. |
| Id | Long | 2 | The ID of the case. |

**Examples**

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"3BB85AD2-E1D2-45C5-B22B-949CBC9BD98B\t",
 "Id":2
```

`}` `XML` format

```xml
<RequestId>3BB85AD2-E1D2-45C5-B22B-949CBC9BD98B </RequestId> <Id>2</Id>
```

#### 4.2.6 SyncBanRecord

Synchronizes blocking records.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| Entity | Strin g | Query | Yes | 12.12.XX.XX | The value of the blocked threat indicator. |
| EntityTyp e | Strin g | Query | Yes | IP | The type of the indicator, such as IP,file hash . _ |
| BanType | Strin g | Query | Yes | ban-whole | The type of the blocking operation. You can specify this parameter based on your business requirements. The type of the blocking operation is returned when you unblock a threat indicator. |
| TaskName | Strin g | Query | No | Test blocking record | The name of the sub- task. |
| RuleConfi g | Strin g | Query | Yes |   | The custom configurations of the blocking rule. |
| PolicyId | Strin g | Query | Yes | 23 | The ID of the blocking rule that triggers the blocking operation. The ID is specified in the system that performs the blocking operation. |
| EventUuid | Strin g | Query | No | 3BB85AD2-E1D2-45C5- B22B-949CBC9BD98B | The UUID of the case. |

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| StartTime | Long | Query | Yes | 1640169543000 | The beginning of the time range during which a threat indicator is blocked. The value is a 13-byte timestamp. Unit: milliseconds. |
| EndTime | Long | Query | Yes | 1640169543000 | The end time of the blocking period. The value is a 13-digit timestamp. Unit: milliseconds. If the blocking period is permanent, set to -1. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RequestId | String | 3BB85AD2-E1D2- 45C5-B22B- 949CBC9BD98B | The request ID. |
| Id | Long | 10 | The ID of the blocking result. |

**Examples**

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"3BB85AD2-E1D2-45C5-B22B-949CBC9BD98B\t",
 "Id":10
```

`}` `XML` format

```xml
<RequestId>3BB85AD2-E1D2-45C5-B22B-949CBC9BD98B </RequestId> <Id>10</Id>
```

#### 4.2.7 DescribeManualTaskInfo

Queries the execution results.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| Id | Long | Query | No | 1 | The ID of the task. You must set one of the task ID and TaskUUID. |
| NodeNam e | Strin g | Query | No | test | The node name. |
| TaskUuid | Strin g | Query | No | 13123233 | The UUID of the task. You must set one of the task ID and TaskUUID. |
| NeedDataI nfo | Boole an | Query | Yes | true | Specifies whether to return details. Valid values: true : enables the broadcasting feature. false |
| PageNum ber | Integ er | Query | Yes | 1 | The page number of the returned page. |
| PageSize | Integ er | Query | Yes | 10 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| ManualTaskRe cords | Array |   | The details of the job. |
| - AssignedUserI d | String | test | The user ID. |
| - AssignedUser Group | String | test | The user groups. |
| -GmtCreate | Long | 1641803299000 | The time when the UDF was created. |

| Parameter | Type | Examples | Description |
|---|---|---|---|
| -GmtModified | Long | 1641803299000 | The time when the patch baseline was updated. |
| -Id | Long | 1231 | The node ID. |
| -PlaybookId | Long | 123 | The ID of the script. |
| - PlaybookName | String | Test script | The ID of the playbook. |
| -NodeName | String | test | The name of the node. |
| -Status | Integer | 0 | The status of the task. If this parameter is not specified, all tasks are queried. Valid values: -1 : handling not required 0 : unhandled 1 : handled 2 : unhandled after the deadline |
| -TaskUuid | String | AF2B656D-C2C1- 4E47-85FD- 1596C83C6B86 | The sub-task ID. |
| -ActionUuid | String | AF2B656D-C2C1- 4E47-85FD- 1596C83C6B86 | The UUID of the action. |
| - ActualDealerId | String | 1 | The ID of the user who handled the task. |
| - ActualDealedT ime | Long | 1641803299000 | The time at which the task is handled. |
| -PageConfigId | Long | 1 | The ID of the page configuration. |
| - DisplayAction Uuid | String | AF2B656D-C2C1- 4E47-85FD- 1596C83C6B86 | The display UUID of the action. |
| -AkkaActorInfo | String | test | The information about the action node. |
| -DeadlineTime | Long | 1641803299000 | The deadline for handling the task. |
| -TenantId | String | -1 | The tenant ID. |

| C n | loud Security Net and Response | work Detectio |   | Developer·Network Traffic Moni oring System | t |
|---|---|---|---|---|---|

| Parameter | Type | Examples | Description |
|---|---|---|---|
| -Content | String | Data information | The content information. |
| -Url | String |   | The URL. |
| -TaskType | Integer |   | The type of the sub-task. |
| -DataUrl | String | http://xxxxxx | The data URL. |
| -DataInfo | String | {"k":"value"} | The data information. |
| -DownloadUrl | String | http://xxxxxx | The download URL of the data. |
| -NeedDataInfo | Boolean | true | Indicates whether the node information needs to be displayed. |
| -PlaybookType | String |   | The type of the script. |
| -TaskTenantId | String | -2 | The ID of the tenant that executes the task. |
| RequestId | String | AF2B656D-C2C1- 4E47-85FD- 1596C83C6B86 | The request ID. |
| PageNumber | Long | 1 | The page number of the returned page. |
| PageSize | Long | 10 | The number of entries per page. |
| TotalCount | Long | 100 | The total number of namespaces returned. |

**Examples**

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "TotalCount":100,
 "RequestId":"AF2B656D-C2C1-4E47-85FD-1596C83C6B86",
 "PageSize":10,
 "ManualTaskRecords":{
  "ActualDealedTime":1641803299000,
  "ActionUuid":"AF2B656D-C2C1-4E47-85FD-1596C83C6B86\t",
  "AssignedUserId":"test",
  "NodeName":"test",
  "NeedDataInfo":true,
  "GmtModified":1641803299000,
  "AkkaActorInfo":"test",
  "PlaybookName":"Test script",
  "Url":"",
  "TaskType":"",
  "ActualDealerId":"1",
  "DownloadUrl":"http://xxxxxx\t",
  "Status":0,
  "DataInfo":"{\"k\":\"value\"}\t",
  "AssignedUserGroup":"test",
  "TaskUuid":"AF2B656D-C2C1-4E47-85FD-1596C83C6B86\t",
  "TaskTenantId":"-2",
  "PageConfigId":1,
  "GmtCreate":1641803299000,
  "TenantId":"-1",
  "DeadlineTime":1641803299000,
  "Content":"Data information \t ",
  "DataUrl":"http://xxxxxx\t",
  "PlaybookId":123,
  "Id":1231,
  "DisplayActionUuid":"AF2B656D-C2C1-4E47-85FD-1596C83C6B86\t",
  "PlaybookType":""
```

`},`

```json
 "PageNumber":1
```

`}` `XML` format

```xml
<TotalCount>100</TotalCount> <RequestId>AF2B656D-C2C1-4E47-85FD-1596C83C6B86</RequestId> <PageSize>10</PageSize> <ManualTaskRecords>
 <ActualDealedTime>1641803299000</ActualDealedTime>
 <ActionUuid>AF2B656D-C2C1-4E47-85FD-1596C83C6B86
 </ActionUuid>
 <AssignedUserId>test</AssignedUserId>
 <NodeName>test</NodeName>
 <NeedDataInfo>true</NeedDataInfo>
 <GmtModified>1641803299000</GmtModified>
 <AkkaActorInfo>test</AkkaActorInfo>
 <PlaybookName> Test script </PlaybookName>
 <Url  />
 <TaskType  />
 <ActualDealerId>1</ActualDealerId>
 <DownloadUrl>http://xxxxxx
 </DownloadUrl>
 <Status>0</Status>
 <DataInfo>{&quot;k&quot;:&quot;value&quot;}
 </DataInfo>
 <AssignedUserGroup>test</AssignedUserGroup>
 <TaskUuid>AF2B656D-C2C1-4E47-85FD-1596C83C6B86
 </TaskUuid>
 <TaskTenantId>-2</TaskTenantId>
 <PageConfigId>1</PageConfigId>
 <GmtCreate>1641803299000</GmtCreate>
 <TenantId>-1</TenantId>
 <DeadlineTime>1641803299000</DeadlineTime>
 <Content> data information
 </Content>
 <DataUrl>http://xxxxxx
 </DataUrl>
 <PlaybookId>123</PlaybookId>
 <Id>1231</Id>
 <DisplayActionUuid>AF2B656D-C2C1-4E47-85FD-1596C83C6B86
 </DisplayActionUuid>
 <PlaybookType  />
</ManualTaskRecords> <PageNumber>1</PageNumber>
```

#### 4.2.8 DescribePlaybook

Queries the details of a playbook.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| PlaybookI d | Integ er | Query | No | 1 | The script id (script id and script name must be one). |
| PlaybookN ame | Strin g | Query | No | Test script | The name of the script (one of the script id and the script name must be specified). |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RequestId | String | 65C02B7B-C23D- 4929-A378- 11EB59813141 | The request ID. |
| Playbook | Struct |   | The details of the playbook. |
| -Active | Boolean | true | The status of the playbook. Valid values: true: enabled. false: disabled. |
| - Compiledresul t | String |   | The compilation result of the playbook. |
| -Creator | String | sys | The user who created the playbook. |
| -Description | String |   | The description of the playbook. |
| -DomainId | String | ids-group | The tenant information of the playbook. |
| -GmtCreate | Long | 1642066923992 | The time at which the playbook was created. The value is a 13-byte timestamp. Unit: milliseconds. |
| -GmtModified | Long | 1642066923992 | The time at which the playbook was last modified. The value is a 13-byte timestamp. Unit: milliseconds. |
| -Id | Long | 582 | The ID of the script. |
| -Inputtype | String | event | The input type. |

| C n | loud Security Ne and Response | twork Detectio |   | Developer·Network Traffic Moni oring System | t |
|---|---|---|---|---|---|

| Parameter | Type | Examples | Description |
|---|---|---|---|
| -InputParams | String | [{"name":"compon ent name","dataTy _ pe":"String","descri ption":"Component name","required":f alse,"stanchDefault Value":""}, {"name":"version", "dataType":"String ","description":"Co mponent version","required" :false,"stanchDefau ltValue":""}] | The input parameters of the playbook. |
| -Modifier | String | yundunluck | The person who modified the configurations. |
| -Name | String | test1 | The name of the playbook. |
| -DisplayName | String | Test 1 | The display name of the playbook. |
| -OnlineActive | Boolean | true | The status of the playbook. Valid values: true: enabled. false: disabled. |
| - OnlineCompile dresult | String |   | The compilation result of the playbook in the production environment. |
| -OnlineOss | String | ophon-gen/****- ba81cd3cc999- 1641814492160- beaver linkage att _ _ ack ban v62 test.j _ _ _ ar | the oss address of the online editing result. |
| -Oss | String | sophon- gen/2****6-accb- ba81cd3cc999- 1641814492160- beaver linkage att _ _ ack ban v62 test.j _ _ _ ar | the oss address of the online editing result. |
| -Cron | String | 0 0 9 * * ? | The scheduling configurations for the playbook. |
| -TriggerInfo | String | {"Query start time":"2022-01-05 10:10:10","Query end time":"2022- 01-05 10:10:10"} | The information that is used to manually run the playbook. |

| Developer·Networ ring System | k Traffic Monit |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|

| Parameter | Type | Examples | Description |
|---|---|---|---|
| -OperateType | String | general | The operation type of the playbook. |
| -OwnType | String | user | The ownership type of the playbook. Valid values: user: user-defined. sys: built-in. |
| -Owner | String | sys | The owner of the playbook. |
| -Taskconfig | String | {\"apps\": [{\"actions\": [{\"customInput\":t rue,\"description\":\ "Call an API operation\",\"id\":0, \"name\":\"execute API\" | The configuration file of the playbook. |
| -Taskflow | String |   | The information about the component on which the playbook depends. |
| -TenantId | String | -2 | The tenant information. |
| -ExecuteMode | String | one | The execution method of the playbook. Valid values: one: manual triggering. mul: timing trigger. strema: streaming trigger. |
| - OnlineExecute Mode | String | one | Online process trigger mode: one: manual triggering. mul: timing trigger. strema: streaming trigger. |
| - OutputParams | String | {"ip":"***"} | The output data of the process. |
| -RightLevel | String |   |   |

**Examples**

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "Playbook":{
  "Owner":"sys",
  "Description":"",
  "GmtModified":1642066923992,
  "Creator":"sys",
  "OnlineExecuteMode":"one",
  "Cron":"0 0 9 * * ?",
  "Name":"test1",
  "Taskconfig":"{\\\"apps\\\":[{\\" actions\\\":[{\\\"customInput\\\":true ,\\" descrip
tion\\\":\\" Execute an openAPI call \\\\ ",\\\",\\\"id \\\:\":0 ,\\ "e \\"
  "Compiledresult":"",
  "InputParams":"[{" name ":" component_name "," dataType ":" String "," description ":
" Component name "," required ":false," stanchDefaultValue ":"},{"name":"version", "dat aType"\"String\",\"description\":\"Component version\",\"required\":false,\"stanchDefaultValue\":\"\"}]",
  "OwnType":"user",
  "OnlineActive":true,
  "DisplayName":"Test 1",
  "Inputtype":"event",
  "ExecuteMode":"one",
  "OutputParams":"{\"ip\":\"***\"}",
  "Modifier":"yundunluck",
  "OperateType":"general",
  "RightLevel":"",
  "Taskflow":"<?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\"?><bpmn:definitions xmlns
:xsi=\\\"http://www.w3.org/2001/XMLSchema-instance\\",
  "TriggerInfo":"{\" Query start time \":\"2022-01-05 10:10:10\",\" Query end time \":\
"2022-01-05 10:10:10\"}",
  "Oss":"sophon-gen/2****6-accb-ba81cd3cc999-1641814492160-
beaver_linkage_attack_ban_v62_test.jar",
  "Active":true,
  "GmtCreate":1642066923992,
  "TenantId":"-2",
  "DomainId":"ids-group\t",
  "OnlineOss":"ophon-gen/****-ba81cd3cc999-1641814492160-
beaver_linkage_attack_ban_v62_test.jar",
  "OnlineCompiledresult":"",
  "Id":582
```

`},`

```json
 "RequestId":"65C02B7B-C23D-4929-A378-11EB59813141\t"
```

`}` `XML` format

```xml
<Playbook>
 <Owner>sys</Owner>
 <Description  />
 <GmtModified>1642066923992</GmtModified>
 <Creator>sys</Creator>
 <OnlineExecuteMode>one</OnlineExecuteMode>
 <Cron>0 0 9 * * ?</Cron>
 <Name>test1</Name>
 <Taskconfig>{\&quot;apps\&quot;:[{\&quot;actions\&quot;:
[{\&quot;customInput\&quot;:true,\&quot;description\&quot;: Execute an openAPI call \&q uot;&quot;&quot;,\&quot;id \config \&quot;&quot;&quot;name \quot;&quot;&quot;&quot;&quot; quot;
 <Compiledresult  />
 <InputParams>[&
{quot;name&quot;:&quot;component_name&quot;,&quot;dataType&quot;:&quot;description&quot;& ot;&quot;component name&quot;&quot;&quot;required&quot;&quot;:&quot;stanchDefaultValue dataType&quot;:&quot;String&quot;,&quot;description&quot;:&quot; Widget Version&quot;,&quot;required&quot;:false,&quot;&quot;stanchDefaultValue&quot;:&quot;&quot quot;}]</InputParams>
 <OwnType>user</OwnType>
 <OnlineActive>true</OnlineActive>
 <DisplayName>Test 1</DisplayName>
 <Inputtype>event</Inputtype>
 <ExecuteMode>one</ExecuteMode>
 <OutputParams>{&quot;ip&quot;:&quot;***&quot;}</OutputParams>
 <Modifier>yundunluck</Modifier>
 <OperateType>general</OperateType>
 <RightLevel  />
 <Taskflow>&lt;?xml version=\&quot;1.0\&quot; encoding=\&quot;UTF-8\&quot;?
&gt;&lt;bpmn:definitions xmlns:xsi=\&quot;http://www.w3.org/2001/XMLSchema-instance\</T askflow>
 <TriggerInfo>{&quot; Query start time&quot;:&quot;2022-01-05 10:10:10&quot;&quot; Quer
y end time&quot;:&quot;2022-01-05 10:10:10&quot;}</TriggerInfo>
 <Oss>sophon-gen/2****6-accb-ba81cd3cc999-1641814492160-
beaver_linkage_attack_ban_v62_test.jar</Oss>
 <Active>true</Active>
 <GmtCreate>1642066923992</GmtCreate>
 <TenantId>-2</TenantId>
 <DomainId>ids-group
 </DomainId>
 <OnlineOss>ophon-gen/****-ba81cd3cc999-1641814492160-
beaver_linkage_attack_ban_v62_test.jar</OnlineOss>
 <OnlineCompiledresult  />
 <Id>582</Id>
</Playbook> <RequestId>65C02B7B-C23D-4929-A378-11EB59813141 </RequestId>
```

#### 4.2.9 DescribeSoarRecords

Queries the execution history of a playbook.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Query | Yes | 1 | The page number of the returned page. |
| PageSize | Integ er | Query | Yes | 10 | The number of entries per page. |
| QueryCon dition | Strin g | Query | Yes | {\"type\":\"complex\",\"c ondition\":\" {\\\"condition\\\":\\\"AND\ \\",\\\"rules\\\": [{\\\"field\\\":\\\"taskNam e\\\",\\\"match\\\":\\\"is\\\ ",\\\"type\\\":\\\"string\\\", \\\"value\\\": [\\\"test rtap\\\"]}]}\"} _ | The query conditions. The value of this parameter includes the following fields: field: indicates the field to be matched. The value: represents the value to match. type: represent the type of match, as follows: match: means equal to. contains: means contains. A complex: indicates a subquery that can be nested. The subquery follows the preceding rules. |

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| TaskUuid | Strin g | Query | No | 73b14357-e011-4993- a769-bfb779ab3638 | The UUID of the task that is generated when the playbook is run. You can obtain the UUID from TriggerUuid by calling the TriggerPlaybook operation. If you specify TriggerUuid , the value of QueryCondition does not take effect. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| SoarExecuteR ecords | Array | [] | An array that consists of details of the execution history. |
| -All | Integer | 1 | The number of times that the SQL statement was executed. |
| - DataSourceNa me | String | TEST | The name of the data source that triggers the playbook. |
| -EndTime | Long | 1641460993364 | The time at which the playbook stops running. The value is a 13-byte timestamp. Unit: milliseconds. |
| -EventId | String | 1641460993340 | The ID of the event that triggers the playbook. |
| -RequestUuid | String | a5a60946-3ad4- 4e0d-92db- 500da9619793 | The UUID of the task that is generated when the playbook is run. |
| -Sao | String | test rtap _ | The name of the playbook. |
| -SaoId | Long | 531 | The ID of the flow. |

| loud Security Ne | twork Detectio |   | Developer·Network Traffic Moni |
|---|---|---|---|

| Parameter | Type | Examples | Description |
|---|---|---|---|
| -StartTime | Long | 1641460993348 | The time at which the playbook starts to run. The value is a 13-byte timestamp. Unit: milliseconds. |
| -Status | String | success | The execution result. Valid values: success: success. failed: failed. The inprogresss: is being executed. |
| -Success | Integer | 1 | The number of successful executions. |
| -TaskName | String | test rtap _ | The name of the task. |
| -TaskUuid | String | cfa5cc68-9279- 45fa-88a0- c79cca020efe | The UUID of the task. |
| -TriggerDataId | String | 1641460993340 | The ID of the data source that triggers the playbook. |
| -TriggerType | String | manual | Type of trigger: one: manual triggering. mul: timing trigger. strema: streaming trigger. |
| -TriggerUser | String | 12385**452 | The user who triggers the playbook. The value is the ID of the account that is used for logon and API calls. |
| -RawEventReq | String | {\"ac\":\"c60dcd*** dc82d73d3b\",\"dat aSourceName\":\"4 357\",\"domainId\": \"ids- group\",\"eventId\": \"1641460993340\ ",\"eventStr\": {},\"taskList\": [\"test rtap\"],\"tas _ kTriggerList\": [],\"tenantId\":\"ba ba\",\"triggerType\" :\"manual\",\"trigge rUser\":\"sys\",\"ts\" :\"1641460993340\ "}" | The detailed raw data about how the playbook is triggered. |
| -SrcIp | String | 10.10.XX.XX | The IP address of the server on which the playbook is run. |

| Developer·Networ ring System | k Traffic Monit |   | Cloud Security Network Detecti n and Respons |
|---|---|---|---|

| Parameter | Type | Examples | Description |
|---|---|---|---|
| -ResultLevel | String | DEBUG | The log level of the execution result for the playbook. Valid values: Call information DEBUG: debugging. INFO: general call information. Information ERROR: a serious error. |
| - ResultMessage | String | "" | The message of the execution result for the playbook. |
| -ErrorMsg | String | error msg | The cause of the error. |
| -RouterPath | String | " {\"actorPath\":\"/us er/sysActorMgr/eve ntMatchRouter/$d/l oad21.08833\",\"po rt\":12153,\"ip\":\"1 0.xx.xx.24\"}", | The execution path of the action. |
| - ResultDetailInf o | String | [] | The data returned. |
| - ActionLogNum | String | 1 | The number of actions. |
| -TenantId | String | -999999 | The tenant information. |
| -TaskTenantId | String | -2 | The information about the tenant on which the task is executed. |
| -TaskType | String | general | Task type: general: the script. standard: standard action. |
| RequestId | String | B57576EA-1F92- 4810-8CC7- B27FEE6CD9DE | The ID of the request. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| PageNumber | Integer | 1 | The page number. |
| TotalCount | Integer | 20 | The total number of entries returned. |

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "TotalCount":20,
 "RequestId":"B57576EA-1F92-4810-8CC7-B27FEE6CD9DE\t",
 "PageSize":20,
 "PageNumber":1,
 "SoarExecuteRecords":{
  "All":1,
  "Sao":"test_rtap\t",
  "SaoId":531,
  "EndTime":1641460993364,
  "SrcIp":"10.10.XX.XX\t",
  "Success":1,
  "TriggerUser":"12385**452\t",
  "ResultLevel":"DEBUG",
  "ResultDetailInfo":"\"\"",
  "TaskType":"general",
  "EventId":"1641460993340",
  "RouterPath":"path",
  "RawEventReq":"
{\\\"ac\\\":\\\"c60dcd***dc82d73d3b\\\",\\\"dataSourceName\\\":\\\"4357\\\",\\\"domainId\ ":\\\"ids-group\\\",\\\"eventId\\\":\\\"1641460993340\\\",\\\"eventStr\\\": {},\\\"taskList\\\":[\\\"test_rtap\\\"],\\\"taskTriggerList\\\": [],\\\"tenantId\\\":\\\"baba\\\",\\\"triggerType\\\":\\\"manual\\\",\\\"triggerUser\\\":\ "sys\\\",\\\"ts\\\":\\\"1641460993340\\\"}\"",
  "Status":"success",
  "TriggerType":"manual",
  "StartTime":1641460993348,
  "TaskUuid":"cfa5cc68-9279-45fa-88a0-c79cca020efe\t",
  "ErrorMsg":"error msg",
  "TaskTenantId":"-2",
  "ActionLogNum":"1",
  "ResultMessage":"\"\"",
  "TriggerDataId":"1641460993340",
  "TenantId":"-999999",
  "DataSourceName":"TEST",
  "TaskName":"test_rtap",
  "RequestUuid":"a5a60946-3ad4-4e0d-92db-500da9619793\t"
```

`}` `}` `XML` format

```xml
<TotalCount>20</TotalCount> <RequestId>B57576EA-1F92-4810-8CC7-B27FEE6CD9DE </RequestId> <PageSize>20</PageSize> <PageNumber>1</PageNumber> <SoarExecuteRecords>
 <All>1</All>
 <Sao>test_rtap
 </Sao>
 <SaoId>531</SaoId>
 <EndTime>1641460993364</EndTime>
 <SrcIp>10.10.XX.XX
 </SrcIp>
 <Success>1</Success>
 <TriggerUser>12385**452
 </TriggerUser>
 <ResultLevel>DEBUG</ResultLevel>
 <ResultDetailInfo>&quot;&quot;</ResultDetailInfo>
 <TaskType>general</TaskType>
 <EventId>1641460993340</EventId>
 <RouterPath>path</RouterPath>
 <RawEventReq>
{\&quot;ac\&quot;:\&quot;c60dcd***dc82d73d3b\&quot;,\&quot;dataSourceName\&quot;:\&quot;4 7\&quot;,\&quot;domainId\&quot;:\&quot;idsgroup\&quot;,\&quot;eventId\&quot;:\&quot;1641460993340\&quot;,\&quot;eventStr\&quot;:{ },\&quot;taskList\&quot;:[\&quot;test_rtap\&quot;],\&quot;taskTriggerList\&quot;:[],\&q uot;tenantId\&quot;:\&quot;baba\&quot;,\&quot;triggerType\&quot;:\&quot;manual\&quot;,\&q t;triggerUser\&quot;:\&quot;sys\&quot;,\&quot;ts\&quot;:\&quot;1641460993340\&quot;}&quot </RawEventReq>
 <Status>success</Status>
 <TriggerType>manual</TriggerType>
 <StartTime>1641460993348</StartTime>
 <TaskUuid>cfa5cc68-9279-45fa-88a0-c79cca020efe
 </TaskUuid>
 <ErrorMsg>error msg</ErrorMsg>
 <TaskTenantId>-2</TaskTenantId>
 <ActionLogNum>1</ActionLogNum>
 <ResultMessage>&quot;&quot;</ResultMessage>
 <TriggerDataId>1641460993340</TriggerDataId>
 <TenantId>-999999</TenantId>
 <DataSourceName>TEST</DataSourceName>
 <TaskName>test_rtap</TaskName>
 <RequestUuid>a5a60946-3ad4-4e0d-92db-500da9619793
 </RequestUuid>
</SoarExecuteRecords>
```

#### 4.2.10 StopOneAction

Stops a calling process.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| RequestU uid | Strin g | Query | Yes | 73b14357-e011-4993- a769-bfb779ab3638 | The UUID of the task that you want to stop. You can obtain the UUID from TriggerUuid by calling the TriggerPlaybook operation. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RequestId | String | C8242F6C-F6E9- 491C-AA00- D619224268ED | The request ID. |

**Examples**

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"C8242F6C-F6E9-491C-AA00-D619224268ED"
```

`}` `XML` format

```xml
<RequestId>C8242F6C-F6E9-491C-AA00-D619224268ED</RequestId>
```

#### 4.2.11 PublishPlaybook

Publish the script interface.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| PlaybookI d | Integ er | Query | Yes | 1 | The ID of the playbook. An ID is generated for each playbook that you create. You can manage playbooks by ID. |
| Descriptio n | Strin g | Query | No | Release Script | The release description of the script. |
| State | Boole an | Query | Yes | false | The status of the playbook. Valid values: true: the publishing process. false: disable the process. |
| Restart | Boole an | Query | Yes | false | Specifies whether to restart the playbook. Valid values: true: stop first, then publish. false: posted directly. |
| PicUrl | Strin g | Query | No | http://sophon-gen/-4a86- aa76-8705e4fc6988.jpg | The URL of the process image. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RequestId | String | 913BE26B-F9CC- 4A84-8CEC- 190E4BADD246 | The ID of the call. |

**Examples**

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"913BE26B-F9CC-4A84-8CEC-190E4BADD246"
```

`}` `XML` format

```xml
<RequestId>913BE26B-F9CC-4A84-8CEC-190E4BADD246</RequestId>
```

#### 4.2.12 TriggerPlaybook

Runs a playbook.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| PlaybookI d | Integ er | Query | No | 1 | The ID of the playbook that you want to run. |
| PlaybookN ame | Strin g | Query | Yes | Test script | The name of the playbook that you want to run. |
| InputPara m | Strin g | Query | Yes | {"name":"test","ip":"10. 123.XX.XX"} | The parameters that are used to run the playbook. Specify the custom input parameters of the playbook. |
| TriggerTy pe | Strin g | Query | No | manual | Trigger type: one: manual triggering. mul: timing trigger. strema: streaming trigger. |
| TaskTena ntId | Strin g | Query | No | -999999 | Triggers a script to add script tenant information. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RequestId | String | 0E402C78-34DC- 4B2B-BB15- 73BB914172C1 | The request ID. |

| Parameter | Type | Examples | Description |
|---|---|---|---|
| TriggerUuid | String | a5a60946-3ad4- 4e0d-92db- 500da9619793 | The UUID of the task that is generated when the playbook is run. You can stop the task or query the result of the task by using the UUID. |

**Examples**

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "TriggerUuid":"a5a60946-3ad4-4e0d-92db-500da9619793",
 "RequestId":"0E402C78-34DC-4B2B-BB15-73BB914172C1"
```

`}` `XML` format

```xml
<TriggerUuid>a5a60946-3ad4-4e0d-92db-500da9619793</TriggerUuid> <RequestId>0E402C78-34DC-4B2B-BB15-73BB914172C1</RequestId>
```

#### 4.2.13 ModifyPlaybook

Modify the script information.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| PlaybookI d | Integ er | Query | Yes | 1 | The ID of the playbook. |
| DisplayNa me | Strin g | Query | Yes | Test script name | The display name of the playbook. |
| Taskflow | Strin g | Query | No | XXX | The configuration file of the playbook. |
| Descriptio n | Strin g | Query | No | Demo playbook | The description of the playbook. |

| Cloud Security | Network | Detectio |   | Deve | loper·Network Traffic Moni |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| InputType | Strin g | Query | No | event | The input type. Set the value to event . |
| OperateTy pe | Strin g | Query | No | general | The operation type of the playbook. Set the value to general . |
| OwnType | Strin g | Query | No | user | The ownership type of the playbook. Valid values: user: user-defined. sys: built-in. |
| ExecuteM ode | Strin g | Query | No | one | The execution method of the playbook in the production environment. Valid values: one: manual triggering. mul: timing trigger. stream: streaming trigger. |
| Cron | Strin g | Query | No | 0 0 9 * * ? | The scheduling configurations for the playbook. |
| ProductCo de | Strin g | Query | No | code | The standard action field. |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RequestId | String | 8277EDCA-9E03- 4102-867E- E346E280865C | The request ID. |

**Examples**

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"8277EDCA-9E03-4102-867E-E346E280865C"
```

`}` `XML` format

```xml
<RequestId>8277EDCA-9E03-4102-867E-E346E280865C</RequestId>
```

#### 4.2.14 AddToBlackList

Adds the source IP address of an attack to the blacklist.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddToBlackLi st | The operation that you want to perform. Set the value to AddToBlackList. |
| SrcIp | String | Yes | 183.100.XX.X X | The source IP address of an attack. |
| DstIp | String | No | 120.223.XX.X X | The destination IP address of an attack. |
| DstPort | String | Yes | 8080 | The start of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| DstPortEnd | String | No | 8081 | The end of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| LiveTime | String | Yes | 5 | The validity period of the blacklist. Unit: minutes. Valid values: 1 to 10080. If you leave this parameter unspecified, the default value 5 is used. |

| Filter | String | No | inbound | The direction of the attack traffic that can be blocked by the blacklist. This parameter is available only for the blacklist. Valid values: inbound: blocks traffic destined for data centers in which Apsara Stack is deployed. This is the default value. outbound: blocks traffic sent from data centers in which Apsara Stack is deployed. |
|---|---|---|---|---|
| AliUid | String | No | 123456**** | The Apsara Stack tenant account. |
| IpType | String | No | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses. This is the default value. 6: IPv6 addresses. |
| Note | String | No | Add the IP address to the blacklist. | The additional description. |

All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see Common parameters. For more information about sample requests, see the "Examples" section of this topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The status code returned for the request. |
| success | String | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddToBlackList &SrcIp=183.100.XX.XX &DstIp=120.223.XX.XX &DstPort=8080 &LiveTime=5 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <success>true</requestId>
```

`JSON` format `{`

```json
  "code": 200,
  "success": "true"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.15 AddToWhiteList

Adds the source IP address of an attack to the whitelist.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddToWhiteLi st | The operation that you want to perform. Set the value to AddToWhiteList. |
| SrcIp | String | No | 183.100.XX.X X | The source IP address of an attack. |
| DstIp | String | Yes | 120.223.XX.X X | The destination IP address of an attack. |
| DstPort | String | No | 8080 | The start of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| DstPortEnd | String | No | 8081 | The end of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| LiveTime | String | No | 5 | The validity period of the whitelist. Unit: minutes. Valid values: 1 to 10080. If you leave this parameter unspecified, the default value 5 is used. |
| AliUid | String | Yes | 123456**** | The Apsara Stack tenant account. |

| IpType | String | Yes | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses. This is the default value. 6: IPv6 addresses. |
|---|---|---|---|---|
| Note | String | Yes | Add the IP address to the whitelist. | The additional description. |

All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see Common parameters. For more information about sample requests, see the "Examples" section of this topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The status code returned for the request. |
| success | String | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddToWhiteList &SrcIp=183.100.XX.XX &DstIp=120.223.XX.XX &AliUid=123456**** &IpType=4 &Note=Add the IP address to the whitelist. &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <success>true</requestId>
```

`JSON` format `{`

```json
  "code": 200,
  "success": "true"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.16 DelFromBlackList

Removes the source IP address of an attack from the blacklist.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DelFromBlack List | The operation that you want to perform. Set the value to DelFromBlackList. |
| SrcIp | String | Yes | 183.100.XX.X X | The source IP address of an attack. |
| DstIp | String | No | 120.223.XX.X X | The destination IP address of an attack. |
| DstPort | String | No | 8080 | The start of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| DstPortEnd | String | No | 8081 | The end of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| LiveTime | String | No | 5 | The validity period of the blacklist. Unit: minutes. Valid values: 1 to 10080. If you leave this parameter unspecified, the default value 5 is used. |
| Filter | String | No | outbound | The direction of the attack traffic that can be blocked by the blacklist. This parameter is available only for the blacklist. Valid values: inbound: blocks traffic destined for data centers in which Apsara Stack is deployed. This is the default value. outbound: blocks traffic sent from data centers in which Apsara Stack is deployed. |
| AliUid | String | Yes | 123456**** | The Apsara Stack tenant account. |

| IpType | String | No | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses. This is the default value. 6: IPv6 addresses. |
|---|---|---|---|---|

All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see Common parameters. For more information about sample requests, see the "Examples" section of this topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The status code returned for the request. |
| success | String | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DelFromBlackList &SrcIp=183.100.XX.XX &DstIp=120.223.XX.XX &AliUid=123456**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <success>true</requestId>
```

`JSON` format `{`

```json
  "code": 200,
  "success": "true"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.17 DelFromWhiteList

Removes the source IP address of an attack from the whitelist.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DelFromWhit eList | The operation that you want to perform. Set the value to DelFromWhiteList. |
| SrcIp | String | No | 183.100.XX.X X | The source IP address of an attack. |
| DstIp | String | Yes | 120.223.XX.X X | The destination IP address of an attack. |
| DstPort | String | No | 8080 | The start of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| DstPortEnd | String | No | 8081 | The end of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| LiveTime | String | No | 5 | The validity period of the whitelist. Unit: minutes. Valid values: 1 to 10080. If you leave this parameter unspecified, the default value 5 is used. |
| AliUid | String | Yes | 123456**** | The Apsara Stack tenant account. |
| IpType | String | No | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses. This is the default value. 6: IPv6 addresses. |

All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see Common parameters. For more information about sample requests, see the "Examples" section of this topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The status code returned for the request. |

| success | String | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DelFromWhiteList &SrcIp=183.100.XX.XX &DstIp=120.223.XX.XX &AliUid=123456**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <success>true</requestId>
```

`JSON` format `{`

```json
  "code": 200,
  "success": "true"
```

`}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.18 DescribeBlackList

Queries the details of the blacklist.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBlack List | The operation that you want to perform. Set the value to DescribeBlackList. |
| SrcIp | String | No | 183.100.XX.X X | The source IP address of an attack. |
| DstIp | String | No | 120.223.XX.X X | The destination IP address of an attack. |

| DstPort | String | No | 8080 | The start of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
|---|---|---|---|---|
| StartTime | Number | No | 16309962310 00 | The beginning of the time range when the blacklist is valid. Unit: milliseconds. |
| EndTime | Number | No | 16309964110 00 | The end of the time range when the blacklist expires. Unit: milliseconds. |
| AliUid | String | Yes | 123456**** | The Apsara Stack tenant account. |
| IpType | String | No | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses. This is the default value. 6: IPv6 addresses. |

All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see Common parameters. For more information about sample requests, see the "Examples" section of this topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The status code returned for the request. |
| success | String | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |
| data | Object |   | The returned data. |
| └DataList | Array |   | The details of the entry returned. |
| └└SrcIp | String | 183.100.XX.XX | The source IP address of an attack. |
| └└DstIp | String | 120.223.XX.XX | The destination IP address of an attack. |
| └└DstPort | Number | 8080 | The start of the destination port range of an attack. |
| └└DstPortEnd | Number | 8081 | The end of the destination port range of an attack. |
| └└LiveTime | String | 5 | The validity period of the blacklist. Default value: 5. Unit: minutes. |

| └└HitTimes | String | 10000 | The number of attacks. |
|---|---|---|---|
| └└Filter | String | inbound | The direction of the attack traffic that can be blocked by the blacklist. Valid values: inbound: blocks traffic destined for data centers in which Apsara Stack is deployed. This is the default value. outbound: blocks traffic sent from data centers in which Apsara Stack is deployed. |
| └└Note | String | Query the details of the blacklist. | The additional description. |
| └└StartTime | String | 1630996231000 | The beginning of the time range when the blacklist is valid. Unit: milliseconds. |
| └└EndTime | String | 1630996411000 | The end of the time range when the blacklist expires. Unit: milliseconds. |
| └└IpType | String | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses. This is the default value. 6: IPv6 addresses. |
| └Count | Number | 5 | The number of entries returned. |
| └Module | String | dispatch rule _ | The name of the process for this request. Default value: dispatch rule. _ |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeBlackList &AliUid=123456**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <success>true</success> <data>
    <DataList>
        <SrcIp>183.100.XX.XX</SrcIp>
        <DstIp>120.223.XX.XX</DstIp>
        <DstPort>8080</DstPort>
        <DstPortEnd>8081</DstPortEnd>
        <LiveTime>5</LiveTime>
        <HitTimes>10000</HitTimes>
        <Filter></Filter>
        <Note></Note>
        <StartTime>1630996231000</StartTime>
        <EndTime>1630996411000</EndTime>
        <IpType>4</IpType>
    </DataList>
    <Count>1</Count>
    <Module>dispatch_rule</Module>
</data>
```

`JSON` format `{`

```json
  "code": "200",
  "success": "true",
  "data": {
    "DataList": [
```

`{`

```json
        "SrcIp": "183.100.XX.XX",
        "DstIp": "120.223.XX.XX",
        "DstPort": 8080,
        "DstPortEnd": 8081,
        "LiveTime": "5",
        "HitTimes": "10000",
        "Filter": "",
        "Note": "",
        "StartTime": "1630996231000",
        "EndTime": "1630996411000",
        "IpType": "4"
```

`}` `],`

```json
    "Count": 1,
    "Module": "dispatch_rule"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.19 DescribeWhiteList

Queries the details of the whitelist.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeWhit eList | The operation that you want to perform. Set the value to DescribeWhiteList. |
| SrcIp | String | No | 183.100.XX.X X | The source IP address of an attack. |
| DstIp | String | No | 120.223.XX.X X | The destination IP address of an attack. |
| DstPort | String | No | 8080 | The start of the destination port range of an attack. Valid values: 0 to 65535. If you set this parameter to 0, all ports are specified. |
| StartTime | Number | No | 16309962310 00 | The beginning of the time range when the whitelist is valid. Unit: milliseconds. |
| EndTime | Number | No | 16309964110 00 | The end of the time range when the whitelist is valid. Unit: milliseconds. |
| AliUid | String | Yes | 123456**** | The Apsara Stack tenant account. |
| IpType | String | No | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses. This is the default value. 6: IPv6 addresses. |

All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see Common parameters. For more information about sample requests, see the "Examples" section of this topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The status code returned for the request. |
| success | String | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |
| data | Object |   | The returned data. |

| └DataList | Array |   | The details of the entry returned. |
|---|---|---|---|
| └└SrcIp | String | 183.100.XX.XX | The source IP address of an attack. |
| └└DstIp | String | 120.223.XX.XX | The destination IP address of an attack. |
| └└DstPort | Number | 8080 | The start of the destination port range of an attack. |
| └└DstPortEnd | Number | 8081 | The end of the destination port range of an attack. |
| └└LiveTime | String | 5 | The validity of the whitelist. Default value: 5. Unit: minutes. |
| └└HitTimes | String | 10000 | The number of attacks. |
| └└Filter | String | inbound | The direction of the traffic that is allowed by the whitelist. Valid values: inbound: allows traffic destined for data centers in which Apsara Stack is deployed. This is the default value. outbound: allows traffic sent from data centers in which Apsara Stack is deployed. |
| └└Note | String | Query the details of the whitelist. | The additional description. |
| └└StartTime | String | 1630996231000 | The beginning of the time range when the whitelist is valid. Unit: milliseconds. |
| └└EndTime | String | 1630996411000 | The end of the time range when the whitelist is valid. Unit: milliseconds. |
| └└IpType | String | 4 | The type of the IP addresses. Valid values: 4: IPv4 addresses 6: IPv6 addresses |
| └Count | Number | 5 | The number of entries returned. |
| └Module | String | dispatch rule _ | The name of the process for this request. Default value: dispatch rule. _ |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeWhiteList &AliUid=123456**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <success>true</success> <data>
    <DataList>
        <SrcIp>183.100.XX.XX</SrcIp>
        <DstIp>120.223.XX.XX</DstIp>
        <DstPort>8080</DstPort>
        <DstPortEnd>8081</DstPortEnd>
        <LiveTime>5</LiveTime>
        <HitTimes>10000</HitTimes>
        <Filter></Filter>
        <Note></Note>
        <StartTime>1630996231000</StartTime>
        <EndTime>1630996411000</EndTime>
        <IpType>4</IpType>
    </DataList>
    <Count>1</Count>
    <Module>dispatch_rule</Module>
</data>
```

`JSON` format `{`

```json
  "code": "200",
  "success": "true",
  "data": {
    "DataList": [
```

`{`

```json
        "SrcIp": "183.100.XX.XX",
        "DstIp": "120.223.XX.XX",
        "DstPort": 8080,
        "DstPortEnd": 8081,
        "LiveTime": "5",
        "HitTimes": "10000",
        "Filter": "",
        "Note": "",
        "StartTime": "1630996231000",
        "EndTime": "1630996411000",
        "IpType": "4"
```

`}` `],`

```json
    "Count": 1,
    "Module": "dispatch_rule"
```

`}` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 4.2.20 DescribeL7Rule

Queries the details of the application-layer rules that are used to block traffic.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeL7Rule | The operation that you want to perform. Set the value to DescribeL7Rule. |
| Lang | String | No | zh | The language of the content within the request and response. zh: Chinese en: English |
| RuleStatus | String | No | online | The status of the rules. %: all states init: initializing online: in effect offline: expired |
| AliUid | Long | No | 1234567890 | The Apsara Stack tenant account. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| ActionType | String | No | drop | The action of the rules. pass: allows traffic. alert: only records traffic in logs. drop: blocks traffic. |
| Direction | String | No | in | The direction of traffic. in: inbound traffic out: outbound traffic |
| Query | String | No | % | The query string. %: a wildcard character in SQL statements. You can use a percent sign (%) to match all characters in rules that are used to monitor HTTP requests. |

| QueryTimeType | Integer | No | 1 | The time condition of the rules to query. 1: queries rules that are created before the specified time condition 2: queries rules that are created at the specified time condition 3: queries rules that are created after the specified time condition 4: queries rules that are created within the specified time condition 5: queries rules that expire before the specified time condition 6: queries rules that expire at the specified time condition 7: queries rules that expire after the specified time condition 8: queries rules that expire within the specified time condition |
|---|---|---|---|---|
| QueryStartTime | Long | No | 1934325423 | The beginning of the time range to query. Unit: seconds. |
| QueryEndTime | Long | No | 1934325428 | The end of the time range to query. Unit: seconds. |
| WhiteRuleID | Long | No | 13285 | The ID of the whitelist or the rule that allows traffic. |
| BlackRuleID | Long | No | 13285 | The ID of the blacklist or the rule that blocks traffic. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| DataList | Array of Data |   | The list of the returned data. |
| ActionType | String | drop | The action of the rules. pass: indicates that the rules are used to allow traffic. alert: indicates that the rules are used to only record traffic in logs. drop: indicates that the rules are used to block traffic. |
| AliUid | Long | 1234567890 | The Apsara Stack tenant account. |

| CreateTime | String | 2018-05-14 14:50:54 | The time when the rule was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. |
|---|---|---|---|
| Direction | String | in | The direction of traffic. in: inbound traffic out: outbound traffic |
| EndTime | Long | 1642747110 | The end of the time range that is queried. The value is a UNIX timestamp. Unit: seconds. |
| ExpiredTime | String | 2018-05-14 14:50:54 | The expected expiration time of the rule. This parameter takes effect only for rules in the online state. |
| HitTimes | Integer | 10 | The number of times the rule is matched. |
| MatchsDesc | String | [ "The URL contains a.com", "The host address contains 1.1.1.1" ] | The matching item in the rule that is used to monitor HTTP requests. |
| MatchsDescEn | String | [ "The URL contains a.com", "The host address contains 1.1.1.1" ] | The matching item in the rule that is used to monitor HTTP requests. This parameter is intended for users outside the Chinese mainland. |
| ModifiedTime | String | 2018-05-14 14:50:54 | The time when the rule is updated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. |
| Modifier | String | administrator | The user who modified the rule for the last time. |
| OfflineTime | String | 2018-05-14 14:50:54 | The time when the rule expires. The time follows the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. |
| OnlineTime | String | 2018-05-14 14:50:54 | The time when the rule takes effect. This parameter takes effect only for the rule in the online state. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. |
| RuleDescriptio n | String | test | The description of the rule. |
| RuleId | Integer | 13285 | The ID of the rule. |

| RuleName | String | bot scanner block _ _ | The name of the rule. |
|---|---|---|---|
| RuleUuid | String | cfa13285-5330- 402e-980c- 5075c12c6aa8 | The UUID of the rule. |
| StartTime | Long | 1642747110 | The beginning of the time range that is queried. The value is a UNIX timestamp. Unit: milliseconds. |
| SwitchStatus | String | online | The status of the rule. init: indicates that the rule is being initialized. online: indicates that the rule is in effect. offline: indicates that the rule expired. |
| matchs | Array of Matchs |   | An array that consists of match conditions. |
| Content | String | 8.8.8.8 | The value of the HTTP header. |
| HeaderName | String | x-forward-for | The name of the HTTP header. This value is case-insensitive. Valid values: method, x-forward-for, host, url, cookie, and custom values. |
| MatchType | String | strict | The matching logic. strict: exact match. fuzzy: fuzzy match. notexist: The HTTP header does not exist. |
| NoCase | Integer | 1 | Indicates whether the rule is case- sensitive. 1: case-insensitive 0: case-sensitive |
| TcpOptionKind | Integer | 28 | The decimal value of the TCP Options field. |

| XPosition | Integer | -1 | The position from which the originating IP address is obtained in the HTTP header, such as X-Forwarded-For. The value of this parameter starts from 1. If 2 is returned, 9.9.9.9 is the originating IP address that is obtained from x-forward- for:8.8.8.8,9.9.9.9.7.7.7.7. If -1 or an integer that is smaller than 0 is returned, the originating IP address may be in any position of the HTTP header. |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | The status code of the request. 200: The request is successful. |
| Module | String | dispatch rule _ | The module name of the request. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | CFE6DXXX-XXX- XXXX-XXXX- 99XX99XX99XX | The ID of the request. |
| Success | Boolean | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |
| TotalCount | Integer | 10 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeL7Rule &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DataList>
    <RuleDescription>test</RuleDescription>
    <MatchsDescEn>[   "The URL contains a.com",   "The host address contains 1.1.1.1" ]
</MatchsDescEn>
    <OfflineTime>2018-05-14 14:50:54</OfflineTime>
    <ActionType>drop</ActionType>
    <EndTime>1642747110</EndTime>
    <CreateTime>2018-05-14 14:50:54</CreateTime>
    <RuleId>13285</RuleId>
    <StartTime>1642747110</StartTime>
    <OnlineTime>2018-05-14 14:50:54</OnlineTime>
    <RuleUuid>cfa13285-5330-402e-980c-5075c12c6aa8</RuleUuid>
    <Direction>in</Direction>
    <ModifiedTime>2018-05-14 14:50:54</ModifiedTime>
    <HitTimes>10</HitTimes>
    <ExpiredTime>2018-05-14 14:50:54</ExpiredTime>
    <MatchsDesc>[   "The URL contains a.com",   "The host address contains 1.1.1.1" ]</
MatchsDesc>
    <Modifier>administrator</Modifier>
    <SwitchStatus>online</SwitchStatus>
    <RuleName>bot_scanner_block</RuleName>
    <AliUid>1234567890</AliUid>
    <matchs>
        <XPosition>-1</XPosition>
        <MatchType>strict</MatchType>
        <HeaderName>x-forward-for</HeaderName>
        <TcpOptionKind>28</TcpOptionKind>
        <Content>8.8.8.8</Content>
        <NoCase>1</NoCase>
    </matchs>
</DataList> <TotalCount>10</TotalCount> <PageSize>10</PageSize> <RequestId>CFE6DXXX-XXX-XXXX-XXXX-99XX99XX99XX</RequestId> <CurrentPage>1</CurrentPage> <HttpStatusCode>200</HttpStatusCode> <Module>dispatch_rule</Module> <Success>true</Success>
```

`JSON` format `{`

```json
    "DataList": {
        "RuleDescription": "test",
        "MatchsDescEn": "[   \"The URL contains a.com\",   \"The host address contains
1.1.1.1\" ]",
        "OfflineTime": "2018-05-14 14:50:54",
        "ActionType": "drop",
        "EndTime": 1642747110,
        "CreateTime": "2018-05-14 14:50:54",
        "RuleId": 13285,
        "StartTime": 1642747110,
        "OnlineTime": "2018-05-14 14:50:54",
        "RuleUuid": "cfa13285-5330-402e-980c-5075c12c6aa8",
        "Direction": "in",
        "ModifiedTime": "2018-05-14 14:50:54",
        "HitTimes": 10,
        "ExpiredTime": "2018-05-14 14:50:54",
        "MatchsDesc": "[   \"The URL contains a.com\",   \"The host address contains
1.1.1.1\" ]",
        "Modifier": "administrator",
        "SwitchStatus": "online",
        "RuleName": "bot_scanner_block",
        "AliUid": 1234567890,
        "matchs": {
            "XPosition": -1,
            "MatchType": "strict",
            "HeaderName": "x-forward-for",
            "TcpOptionKind": 28,
            "Content": "8.8.8.8",
            "NoCase": 1
```

`}` `},`

```json
    "TotalCount": 10,
    "PageSize": 10,
    "RequestId": "CFE6DXXX-XXX-XXXX-XXXX-99XX99XX99XX",
    "CurrentPage": 1,
    "HttpStatusCode": 200,
    "Module": "dispatch_rule",
    "Success": true
```

`}`

#### 4.2.21 SwitchL7RuleStatus

Changes the status of application-layer rules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | SwitchL7RuleSta tus | The operation that you want to perform. Set the value to SwitchL7RuleStatus. |
|---|---|---|---|---|
| Lang | String | No | zh | The language of the content within the request and response. zh: Chinese en: English |
| AliUid | Long | No | 1234567890 | The Apsara Stack tenant account. |
| RuleUuidList | String | No | cfa13285-5330- 402e-980c- 5075c12c6aa8, cfa13285-5330- 402e-980c- 5075c12c6aa8 | The UUIDs of the rules. Separate multiple UUIDs with commas (,). |
| SwitchStatus | String | No | online | The status of the rules. online: in effect offline: expired |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | The status code of the request. 200: The request is successful. |
| Module | String | dispatch rule _ | The module name of the request. |
| RequestId | String | CFE6DXXX-XXX- XXXX-XXXX- 99XX99XX99XX | The ID of the request. |
| Success | Boolean | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SwitchL7RuleStatus &<Common request parameters>
```

Sample success responses `XML` format

|   | <RequestId>CFE6DXXX-XXX-XXXX-XXXX-99XX99XX99XX</RequestId> <HttpStatusCode>200</HttpStatusCode> <Module>dispatch rule</Module> _ <Success>true</Success> |   |
|---|---|---|

`JSON` format `{`

```json
    "RequestId": "CFE6DXXX-XXX-XXXX-XXXX-99XX99XX99XX",
    "HttpStatusCode": 200,
    "Module": "dispatch_rule",
    "Success": true
```

`}`

#### 4.2.22 AddL7Rule

Creates an HTTP rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddL7Rule | The operation that you want to perform. Set the value to AddL7Rule. |
| Lang | String | No | zh | The language of the content within the request and response. zh: Chinese en: English |
| AliUid | Long | No | 1397349584302 1 | The Apsara Stack tenant account. |
| RuleName | String | No | bot scanner blo _ _ ck | The name of the rule. |
| RuleDescription | String | No | test | The description of the rule. |
| Direction | String | No | in | The direction of traffic. in: inbound traffic out: outbound traffic |
| ActionType | String | No | drop | The action of the rule. pass: allows traffic. alert: only records traffic in logs. drop: blocks traffic. |

| SwitchStatus | String | No | online | The status of the rule. init: The rule is being initialized. online: The rule is in effect. offline: The rule expired. |
|---|---|---|---|---|
| StartTime | Long | No | 1642664320 | The time when the rule takes effect. The value is a UNIX timestamp. Unit: milliseconds. |
| EndTime | Long | No | 1642664320 | The time when the rule expires. If you set this parameter to 9999999999, the rule never expires. The value is a UNIX timestamp. Unit: milliseconds. |
| Matchs | String | No | None | The content of the rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | The status code of the request. 200: The request is successful. |
| Module | String | dispatch rule _ | The module name of the request. |
| RequestId | String | CFE6DXXX-XXX- XXXX-XXXX- 99XX99XX99XX | The ID of the request. |
| Success | Boolean | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddL7Rule &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>CFE6DXXX-XXX-XXXX-XXXX-99XX99XX99XX</RequestId> <HttpStatusCode>200</HttpStatusCode> <Module>dispatch_rule</Module> <Success>true</Success>
```

`JSON` format `{`

```json
    "RequestId": "CFE6DXXX-XXX-XXXX-XXXX-99XX99XX99XX",
    "HttpStatusCode": 200,
    "Module": "dispatch_rule",
    "Success": true
```

`}`

#### 4.2.23 DelL7Rule

Deletes application-layer rules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DelL7Rule | The operation that you want to perform. Set the value to DelL7Rule. |
| Lang | String | No | zh | The language of the content within the request and response. zh: Chinese en: English |
| AliUid | Long | No | 1397349584302 1 | The Apsara Stack tenant account. |
| RuleUuidList | String | No | cfa13285-5330- 402e-980c- 5075c12c6aa8 | The UUIDs of the rules. Separate multiple UUIDs with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | The status code of the request. 200: The request is successful. |
| Module | String | dispatch rule _ | The module name of the request. |

| RequestId | String | CFE6DXXX-XXX- XXXX-XXXX- 99XX99XX99XX | The ID of the request. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request is successful. Valid values: true: The request is successful. false: The request failed. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DelL7Rule &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>CFE6DXXX-XXX-XXXX-XXXX-99XX99XX99XX</RequestId> <HttpStatusCode>200</HttpStatusCode> <Module>dispatch_rule</Module> <Success>true</Success>
```

`JSON` format `{`

```json
    "RequestId": "CFE6DXXX-XXX-XXXX-XXXX-99XX99XX99XX",
    "HttpStatusCode": 200,
    "Module": "dispatch_rule",
    "Success": true
```

`}`

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
