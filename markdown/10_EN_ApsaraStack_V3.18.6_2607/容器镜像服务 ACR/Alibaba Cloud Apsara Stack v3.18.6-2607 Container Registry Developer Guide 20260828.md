---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Container Registry Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 147
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Container Registry Developer Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%AE%B9%E5%99%A8%E9%95%9C%E5%83%8F%E6%9C%8D%E5%8A%A1%20ACR/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Container%20Registry%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Container Registry Developer Guide 20260828

## SDK reference

### Getting started

#### Usage notes on development

**documentation**

This topic describes how to view the desired product development documentation when you use Apsara Stack API (ASAPI).

**Procedure**

You can follow the procedure described in the following figure to view the desired development documentation.

**Prerequisites**

The Apsara Stack version is obtained from an O&M personnel or operations administrator.

**Procedure**

You can go to the Apsara Stack documentation center and view the desired product documentation.
1. Go to the Apsara Stack Documentation Centerpage by using a browser.
2. Click the **Enterprise**, **Agility**, or **All-in-one** tab based on the Apsara Stack version that you
use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the name of the product that you want to view.
5. In the upper-right corner of the product documentation section, click **View Details** or
**Download PDF**.

#### Procedure for API calls

Apsara Stack allows you to call API operations by using the point of presence (POP) gateway. To ensure that Apsara Stack provides the same experience as Alibaba Cloud public cloud, API operations in Apsara Stack Enterprise V3.16.0 and later are called by using the POP gateway by default. This topic describes how to use the POP gateway to call Apsara Stack API operations.

**Flowchart**

**Procedure**

1. Obtain AccessKey credentials.
Obtain the AccessKey credentials that are required when you call an API operation. For more information, see Obtain an AccessKey pair or Obtain an STS AccessKey 3-tuple.

**Note**

We recommend that you use the AccessKey pair of a personal account assigned by Resource Access Management (RAM) or an access credential assigned by Security Token Service (STS) to call the API operations of the Apsara Uni-manager Management Console and cloud services.
2. Obtain the region ID.
For more information, see Obtain the values of common header parameters.
3. Obtain an organization ID and a resource set ID.
Call an API operation to obtain the organization ID. For more information about how to obtain organization IDs, see GetOrganizationList in Apsara Uni-manager Management Cons ole Developer Guide. Call an API operation to obtain the resource set ID. For more information about how to obtain resource set IDs, see ListResourceGroup in Apsara Uni-manager Management Consol e Developer Guide.

|   | Note When you call an API operation, you can specify the organization ID by using <x-acs- organizationid> and the resource set ID by using <x-acs-resourcegroupid> to query only resources that belong to the specified resource set and organization. If you do not specify the <x-acs-organizationid> parameter, the organization to which the current user belongs is used. If you do not specify the <x-acs-resourcegroupid> parameter, this parameter is left empty. If you specify a resource set, you must also specify an organization ID. |   |   |   |
|---|---|---|---|---|
|   |   |   | <x-acs- |   |
|   | organizationid> | <x-acs-resourcegroupid> |   |   |

4. Obtain the API references.
For more information about how to view, use, and obtain the developer guide of a specific service, and understand the features and usage methods of operations, see Usage notes.
5. Obtain the endpoint of a cloud service.
6. Obtain the service SDK and use the SDK to call an operation of the service.

### Preparations

#### Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. On the login page, enter your username and password.
You can obtain the username and password that are used to log in to the Apsara Unimanager Management Console from the operations administrator.

**Note**

**First login**

The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %

**Forgotten password**

If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.
3. Click **Log In**.
4. In the top navigation bar, choose **Products > Others > API Tool**.

#### Obtain API information and the

**endpoint of an API operation**

To use the API of a cloud service, you must be aware of the information of the API, including the service name (code), API operation, and API version.

**Background information**

The information on the API directory page of the Apsara Uni-manager Management Console is for reference only. For more information about how to call API operations, see the developer guides of cloud services. If the information on the API Directory page is different from the information in the developer guide of a cloud service, the information in the developer guide takes precedence.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Development Tools** > **Developer**
**Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging**.
4. In the left-side navigation pane, select the cloud service.
5. Select an API version from the **Version** drop-down list.
6. In the API list, you can view all API operations of the current version.
7. Select an API operation and obtain the POP endpoint of the cloud service on the Parameter
tab.

#### Obtain an AccessKey pair

AccessKey pairs are classified into AccessKey pairs assigned by Resource Access Management (RAM) and AccessKey pairs assigned by Security Token Service (STS). You can use either type of AccessKey pair for authentication when you call operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of request senders. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign an AccessKey pair for authentication. Use RAM to assign an AccessKey ID and an AccessKey secret to a third party. Use STS to assign an AccessKey ID, an AccessKey secret, and a security token to a third party. For more information, see Obtain an AccessKey pair assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts or organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, you must add the following parameters in request headers for access control. If you do not add the parameters, an error may occur. The error indicates that permissions are insufficient.

**Warning**

The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. The AccessKey pair of an organization has more permissions than the AccessKey pair of a personal account. If you want to obtain the AccessKey pair of an organization, make sure that you are authorized by an administrator. This helps ensure security.

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

**Note**

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. Click **Management Accesskey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

#### Obtain an AccessKey pair assigned by

**STS**

This topic describes how to use Security Token Service (STS) to make API calls.

**Background information**

Alibaba Cloud STS allows you to manage temporary credentials to your Alibaba Cloud resources. You can use STS to make API calls. An AccessKey pair assigned by STS consists of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to make API calls, you must use an AccessKey pair assigned by STS. For more information about STS, see What is STS?

**Procedure**

1. Obtain your `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Move the pointer over the profile picture in the upper-right corner of the page and click
**Personal Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view your `RAM role` .
2. Obtain the AccessKey pair assigned by STS.

**Note**

You must use the actual values to replace the variables in the following sample code. The angle brackets <> are not retained in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourRoleSessionName>: Replace it with your current session name. <yourRoleArn>: Replace it with the Alibaba Cloud Resource Name (ARN) of your RAM role. <sts.aliyuns.com>: Replace it with your actual STS endpoint.

```java
public static void main(String[] args) {
    // Create a DefaultAcsClient instance and initialize it.
    Replace <yourRegionID>, <yourAccessKeyID>, and <yourAccessKeySecret> with the act
ual region ID, your AccessKey ID, and your AccessKey secret.
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
    // Replace "sts.aliyuns.com" with the endpoint of STS. The format of an STS endpo
int is sts-vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // The business parameter that is used to specify an alias for the current sessio
n. Replace "<yourRoleSessionName>" with the actual session name.
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

3. Use the AccessKey pair assigned by STS to call API operations of cloud services. In the
following code, the `CreateNamespace` API operation of Container Registry Advanced Edition is called.

**Note**

You must use the actual values to replace the variables in the following sample code. The angle brackets <> are not retained in the final code. The following list describes the variables: <accesskeyId>: Replace it with your actual AccessKey ID. <accessKeySecret>: Replace it with your actual AccessKey secret. <securityToken>: Replace it with your actual security token.

```java
// This file is auto-generated, don't edit it. Thanks. package com.aliyun.sample; import com.aliyun.tea.*; import com.aliyun.cr20181201.*; import com.aliyun.cr20181201.models.*; import com.aliyun.teaopenapi.*; import com.aliyun.teaopenapi.models.*; public class Sample {
    /**
     * Use your AccessKey ID and AccessKey secret to initialize the client.
     * @param accessKeyId
     * @param accessKeySecret
     * @return Client
     * @throws Exception
```

`*/`

```
    public static com.aliyun.cr20181201.Client createClient(String accessKeyId, Strin
g accessKeySecret, String securityToken) throws Exception {
       // accessKeyId, accessKeySecret, and securityToken: Replace them with the Acce
ssKey ID, AccessKey secret, and security token that you obtained in the previous step
```

`.`

```
        Config config = new Config()
                // Your AccessKey ID.
                .setAccessKeyId(accessKeyId)
                // Your AccessKey secret.
                .setAccessKeySecret(accessKeySecret)
                // Your security token.
                .setSecurityToken(securityToken);
        // The endpoint.
        config.endpoint = "cr.cn-shanghai.aliyuncs.com";
        return new com.aliyun.cr20181201.Client(config);
    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.cr20181201.Client client = Sample.createClient("accessKeyId", "acc
essKeySecret", "securityToken");
        CreateNamespaceRequest createNamespaceRequest = new CreateNamespaceRequest();
        // Obtain the return value of the API operation after the sample code is run.
        client.createNamespace(createNamespaceRequest);
```

#### Obtain the values of common headers

You must provide multiple headers when you call Apsara Stack operations. This topic describes the headers and how to obtain the values of the headers. This topic also describes the return values of some headers after you call Apsara Stack operations.

**Headers**

| Header | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain region IDs, see Obtain a region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see Obtain a resource set ID. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. For more information about how to obtain instance IDs, see Obtain an instance ID. |

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the required organization.
5. View the region ID in the **Regions** section.

**Obtain an organization ID**

You must call an operation to obtain an organization ID. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You must call an operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide.

**Obtain an instance ID**

You can obtain the ID of an instance in the cloud service console of the Apsara Uni-manager Management Console. Perform the following operations to obtain an instance ID:
1. Log on to the Apsara Uni-manager Management Console.d
2. In the top navigation bar, choose **Products** > **Elastic Computing** > **Container Registry**.
3. On the Instances page, click the name of an Apsara Stack Advanced Edition instance.
4. On the **Overview** page, view the **Instance ID** in the Instance section.

**Response parameters**

The following response parameters are returned by default when you call operations to query the instances of cloud services.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

#### Obtain the Container Registry SDK

To use points of presence (POPs) to call Apsara Stack API operations, you must use the Container Registry SDK. This topic describes how to obtain Alibaba Cloud SDKs. An SDK includes code and examples. You can create cloud applications by using an SDK in the programming language that you require. The SDKs for Java, Python, and Go are provided. You can select the SDKs from Alibaba Cloud SDKs based on your business requirements.

**Note**

We recommend that you use an SDK for Java, Python, or Go. If you use SDKs in other programming languages, the SDKs may be incompatible with your system. We recommend that you use the SDK core library that is provided on the Alibaba Cloud official website. The SDK core library is shared by all cloud services and is compatible with Apsara Stack.

### Standard SDK

#### SDK for Java

##### Install Java

This topic describes how to install Java.

**Environment requirements**

You must use Java 6 or later. To install the core library of Alibaba Cloud SDK for Java, you can add the following dependency to the POM file:

**Note**

In the following example, the core library of SDK V4.5.21 is installed.

```xml
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-sdk-core</artifactId>
  <version>4.5.21</version>
</dependency>
```

**Install Container Registry SDK.**

To install Container Registry SDK for Java by using Apache Maven, add the following dependency to the project file:

**Note**

In the following example, SDK V4.1.2 is installed.

```xml
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-sdk-cr</artifactId>
  <version>4.1.2</version>
</dependency>
```

##### Call SDK for Java

This topic describes how to call SDK for Java.

**Sample code**

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile;
```

`/*`

```xml
pom.xml <dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-sdk-core</artifactId>
  <version>4.5.16</version>
</dependency>
```

`*/`

```java
public class GetNamespace {
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("cn-wl-e****", "<your-
access-key-id>", "<your-access-key-secret>");
        /** use STS Token
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",           // The region ID
            "<your-access-key-id>",       // The AccessKey ID of the RAM account
            "<your-access-key-secret>",   // The AccessKey Secret of the RAM account
            "<your-sts-token>");          // STS Token
        **/
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        //request.setProtocol(ProtocolType.HTTPS);
        request.setMethod(MethodType.GET);
        request.setDomain("cr.registry.inter.e****.shuguang.com");
        request.setVersion("2016-06-07");
        request.setUriPattern("/namespace/fc-example");
        request.putHeadParameter("Content-Type", "application/json");
        String requestBody = "" +
                "{}";
        request.setHttpContent(requestBody.getBytes(), "utf-8", FormatType.JSON);
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            e.printStackTrace();
```

#### SDK for Python

##### Installation

This topic describes how to install SDK for Python.

**Environment requirements**

Python 3 Install Alibaba Cloud SDK for Python by using the pip tool:

```
pip install aliyun-python-sdk-core
```

**Install the Container Registry SDK.**

PyPI PIP

```
pip install aliyun-python-sdk-cr==4.1.2
```

PyPI Anaconda

```
conde install aliyun-python-sdk-cr=4.1.2
```

##### Usage

This topic describes how to use SDK for Python.

**Sample code**

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential credentials = AccessKeyCredential('<your-access-key-id>', '<your-access-key-secret>')
# use STS Token
# credentials = StsTokenCredential('<your-access-key-id>', '<your-access-key-secret>',
'<your-sts-token>') client = AcsClient(region_id='cn-wl-e****', credential=credentials) request = CommonRequest() request.set_accept_format('json') request.set_method('GET') request.set_protocol_type('https') # https | http request.set_domain('cr.registry.inter.e****.shuguang.com') request.set_version('2016-06-07') request.add_header('Content-Type', 'application/json') request.set_uri_pattern('/namespace/fc-example') body = '''{}''' request.set_content(body.encode('utf-8')) response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding = 'utf-8'))
```

### Container Registry Advanced

**Edition SDKs**

#### SDK for Java

##### Installation

This topic describes how to install SDK for Java.

**Environment requirements**

You must use Java 8 or later. To install OpenAPI Portal SDK for Java, you can add the following dependency to the POM file:

**Note**

In this topic, a dependency of version 0.0.19 is used.

```xml
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>tea-openapi</artifactId>
  <version>0.0.19</version>
</dependency>
```

**Install the Container Registry SDK.**

To install the Container Registry SDK for Java by using Apache Maven, add the following dependency to the project file:

**Note**

In this topic, a dependency of version 1.0.1 is used.

```xml
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>cr20181201</artifactId>
  <version>1.0.1</version>
</dependency>
```

##### Usage

This topic describes how to use the SDK for Java.

**Procedure**

1. Initialize the com.aliyun.teaopenapi.models.Config object.
The Config object contains the `access_key_id` , `access_key_secret` , and `endpoint` configurations.

```
Config config = new Config()
    // Your AccessKey ID.
    .setAccessKeyId(accessKeyId)
    // Your AccessKey secret.
    . setAccessKeySecret(accessKeySecret);// The endpoint.
config.endpoint = "cr-ee.cn-qingdao***.shuguang.com";
```

2. Instantiate a client object from the com.aliyun.cr20181201.Client class.
Request and Response parameters for subsequent API calls are obtained from com.aliyun.cr20181201.models.

```
Client client = new Client(config);
```

3. Create a request based on the required API operation.
The class is named after the API operation, followed by Request.

```
GetArtifactBuildTaskRequest request = new GetArtifactBuildTaskRequest();
```

4. Configure request parameters.
You must set the required properties for the request class.

```
request.InstanceId = "test"; // Specify the parameter based on your needs. request.BuildTaskId = "test"; // Specify the parameter based on your needs.
```

5. Obtain a response by using the client object.

```java
GetArtifactBuildTaskResponse response = client.getArtifactBuildTask(request); System.out.println(new Gson().toJson(response.Body));
```

6. Obtain a response parameter by calling the corresponding property.
In this example, the `requestId` response is obtained.

```
String requestId = response.Body.requestId;
```

7. Use the catch() syntax to handle errors.

```
catch (Exception e) {
    e.printStackTrace();
```

**Sample code**

```java
// This file is auto-generated, don't edit it. Thanks. package com.aliyun.sample; import com.aliyun.tea.*; import com.aliyun.cr20181201.*; import com.aliyun.cr20181201.models.*; import com.aliyun.teaopenapi.*; import com.aliyun.teaopenapi.models.*; public class Sample {
    /**
     * Use your AccessKey ID and AccessKey secret to initialize the client.
     * @param accessKeyId
     * @param accessKeySecret
     * @return Client
     * @throws Exception
```

`*/`

```
    public static com.aliyun.cr20181201.Client createClient<String accessKeyId, String
accessKeySecret> throws Exception {
        Config config = new Config()
                // Your AccessKey ID.
                .setAccessKeyId<accessKeyId>
                // Your AccessKey secret.
                .setAccessKeySecret<accessKeySecret>;
        // The endpoint.
        config.endpoint = "cr-ee.registry.cn-wl-en****.inter.en****.shuguang.com";
        return new com.aliyun.cr20181201.Client(config);
    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.cr20181201.Client client = Sample.createClient<"accessKeyId",
"accessKeySecret">;
        GetNamespaceRequest getNamespaceRequest = new GetNamespaceRequest()
                .setInstanceId("cri-pri****")
                .setNamespaceName("test12");
        // After you copy and run the sample code, use the following object to query th
e response data of the request:
        client.getNamespace(getNamespaceRequest);
```

#### SDK for Python

##### Installation

This topic describes how to install SDK for Python.

**Environment requirements**

Python 3 Install Alibaba Cloud SDK for Python by using the pip tool:

```
pip install alibabacloud_tea_openapi>
```

**Install the Container Registry SDK.**

PyPI PIP

```
pip install alibabacloud_cr20181201==1.0.3
```

PyPI Anaconda

```
conde install alibabacloud_cr20181201=1.0.3
```

##### Usage

This topic describes how to use SDK for Python.

**Procedure**

1. Initialize the alibabacloud_tea_openapi.Config object.
The Config object contains the `access_key_id` , `access_key_secret` , and `endpoint` configurations.

```python
from alibabacloud_tea_openapi import models as open_api_models config = open_api_models.Config(
    # Your AccessKey ID.
    access_key_id=access_key_id,
    # Your AccessKey secret.
    access_key_secret=access_key_secret
```

`)`

```bash
# The endpoint.
config.endpoint = 'cr.cn-hangzhou.aliyuncs.com'
```

2. Instantiate a client object from the com.aliyun.cr20181201.Client class.
Request and Response parameters for subsequent API calls are obtained from com.aliyun.cr20181201.models.

```python
from alibabacloud_cr20181201.client import Client as Client from alibabacloud_cr20181201 import models as models client = Client(config)
```

3. Create a request based on the required API operation.
The method is in the Create<%- api %>Request() format.

```
request = models.CreateGetArtifactBuildTask()
```

4. Configure request parameters.
You must set the required properties for the request class.

```
// Set parameters based on your needs. request.InstanceId = "test"; // Set parameters based on your needs. request.BuildTaskId = "test";
```

5. Obtain a response by using the client object.

```python
requestId = response.body.requestId print(requestId)
```

6. Obtain a response parameter by calling the corresponding property.
In this example, the `requestId` response is obtained.

```
String requestId = response.Body.requestId;
```

7. Use the try...except... syntax to handle errors.

```python
from Tea.exceptions import UnretryableException try:
    response = client.describe_images(request)
except UnretryableException as e:
    # Server Error
    print(e.inner_exception.code)
    print(e.inner_exception.message)
except Exception as e:
    print(e)
```

**Sample code**

```java
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys from typing import List from alibabacloud_cr20181201.client import Client as cr20181201Client from alibabacloud_tea_openapi import models as open_api_models from alibabacloud_cr20181201 import models as cr_20181201_models class Sample:
    def __init__(self):
        pass
    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> cr20181201Client:
        """
        Use your AccessKey ID and AccessKey secret to initialize the client.
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # Your AccessKey ID.
            access_key_id=access_key_id,
            # Your AccessKey secret.
            access_key_secret=access_key_secret
```

`)`

```python
        # The endpoint.
        config.endpoint = 'cr-ee.registry.cn-wl-en****.inter.en****.shuguang.com'
        return cr20181201Client(config)
    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        get_namespace_request = cr_20181201_models.GetNamespaceRequest(
            instance_id='cri-pri****',
            namespace_name='test12'
```

`)`

```bash
        # After you copy and run the sample code, use the following object to query the
response data of the request:
        client.get_namespace(get_namespace_request)
    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        get_namespace_request = cr_20181201_models.GetNamespaceRequest(
            instance_id='cri-pri****',
            namespace_name='test12'
```

`)`

```bash
        # After you copy and run the sample code, use the following object to query the
response data of the request:
        await client.get_namespace_async(get_namespace_request)
if __name__ == '__main__':
    Sample.main(sys.argv[1:])
```

#### SDK for Go

##### Installation

This topic describes how to install SDK for Go.

**Environment requirements**

The Go version must be 1.10.x or later. Alibaba Cloud SDK for Go is installed.

```
go get github.com/alibabacloud-go/darabonba-openapi/client
```

**Install the Container Registry SDK.**

To install Container Registry SDK for Go, we recommend that you run the following command:

```
go get github.com/alibabacloud-go/cr-20181201
```

##### Usage

This topic describes how to use SDK for Go.

**Procedure**

1. Add the following dependencies:

```java
import (
  cr "github.com/alibabacloud-go/cr-20181201/client"
  openapi "github.com/alibabacloud-go/darabonba-openapi/client"
```

`)`
2. Initialize the &openapi.Config object.
The Config object contains the `access_key_id` , `access_key_secret` , and `endpoint` configurations.

```
config := &openapi.Config{
  // Your AccessKey ID.
  AccessKeyId: accessKeyId,
  // Your AccessKey secret.
  AccessKeySecret: accessKeySecret,
// The endpoint. config.Endpoint = tea.String("cr.cn-hangzhou.aliyuncs.com")
```

3. Instantiate a client object from the &cr.Client class.

```
client, _ := cr.NewClient(config)
```

4. Create a request based on the required API operation.
The method is named after the API operation, followed by Request.

```
request := &cr.GetArtifactBuildTaskRequest{}
```

5. Configure request parameters.
You must set the required properties for the request class.

```
// Set parameters based on your needs. request.SetInstanceId("test") // Set parameters based on your needs. request.SetBuildTaskId("test")
```

6. Obtain a response by using the client object.

```
response, err := client.GetArtifactBuildTask(request) fmt.Println(response)
```

7. Use the err syntax to handle errors.

```
if err != nil {
  fmt.Println(err)
  return
```

8. Obtain a response parameter by calling the corresponding property.
In this example, the `requestId` response is obtained.

```
fmt.Println(tea.StringValue(response.Body.ImageId))
```

**Sample code**

```java
// This file is auto-generated, don't edit it. Thanks. package main import (
  "os"
  cr20181201  "github.com/alibabacloud-go/cr-20181201/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
```

`)`

```
/**
 * Use your AccessKey ID and AccessKey secret to initialize the client.
 * @param accessKeyId
 * @param accessKeySecret
 * @return Client
 * @throws Exception
```

`*/`

```
func CreateClient (accessKeyId *string, accessKeySecret *string) (_result *cr20181201.C lient, _err error) {
  config := &openapi.Config{
    // Your AccessKey ID.
    AccessKeyId: accessKeyId,
    // Your AccessKey secret.
    AccessKeySecret: accessKeySecret,
  // The endpoint.
  config.Endpoint = tea.String("cr-ee.registry.cn-wl-en****.inter.en****.shuguang.com")
  _result = &cr20181201.Client{}
  _result, _err = cr20181201.NewClient(config)
  return _result, _err
func _main (args []*string) (_err error) {
  client, _err := CreateClient(tea.String("accessKeyId"),
tea.String("accessKeySecret"))
  if _err != nil {
    return _err
  getNamespaceRequest := &cr20181201.GetNamespaceRequest{
    InstanceId: tea.String("cri-pri****"),
    NamespaceName: tea.String("test12"),
  // After you copy and run the sample code, use the following object to query the resp
onse data of the request:
  _, _err = client.GetNamespace(getNamespaceRequest)
  if _err != nil {
    return _err
```

```
  return _err
func main() {
  err := _main(tea.StringSlice(os.Args[1:]))
  if err != nil {
    panic(err)
```

## API references for

**Container Registry Standard**

**Edition**

### Make API requests

#### Common request parameters

This topic provides the common request parameters and common responses of Container Registry API operations.

**Common request parameters**

Common request parameters must be included in all API requests.

| Parameter | Description | Required |
|---|---|---|
| Authorization | The authentication information used to check the authenticity of a request. Format: AccessKeyId:Signature . | Yes |
| Content-Length | The length of the HTTP request content. This length is specified in RFC 2616. | Yes |
| Content-Type | The type of HTTP request content. This type must follow the format that is specified in RFC 2616. | Yes |
| Content-MD5 | The 128-bit MD5 hash value of the HTTP message body. The hash value is encoded in the Base64 format. We recommend that you set this parameter for all requests to prevent parameter tampering. | Yes |
| Date | The time when a request is created. The time must be in GMT. If the deviation between the time when the request was sent and the time when the request was received exceeds 15 minutes, the request is considered invalid. | Yes |
| Host | The URL of the host to which the request is sent. Example: cr.cn- hangzhou.aliyuncs.com . | Yes |

|   |   | cr.cn- |   |
|---|---|---|---|
|   | hangzhou.aliyuncs.com |   |   |

| Accept | The type of response that is required by the client. Valid values: application/json and application/xml. | Yes |
|---|---|---|
| x-acs-version | The version of the API. | Yes |
| x-acs-region-id | The region where the container image is located. | Yes |
| x-acs-signature-nonce | A unique random number that is used to prevent replay attacks. A different random number is required for each request. | Yes |
| x-acs-signature-method | The encryption method of the signature string. Set the value to HMAC-SHA1. | Yes |

```
GET /namespaces HTTP/1.1 Authorization: acs ACSbW2iBbyX1Pk9N:mp/6Wdr18V3qAc5gbgsqMe/iB0c Content-Length: 0 Content-Type: application/json;charset=utf-8 Date: Wed, 23 May 2018 12:00:01 GMT Host: cr.cn-hangzhou.aliyuncs.com Accept: application/json x-acs-version: 2016-06-07 x-acs-region-id: cn-hangzhou x-acs-signature-nonce: f63659d4-10ac-483b-99da-ea8fde61eae3 x-acs-signature-version: 1.0 x-acs-signature-method: HMAC-SHA1 User-Agent: cr-sdk-python/3.0.0 (Darwin/15.2.0/x86_64;2.7.10)
```

**Common responses**

Every response returns a unique request ID regardless of whether the call is successful. XML format:

```xml
<?xml version="1.0" encoding="UTF-8"?> <API operation name + Response>
  <!--Returned request tag-->
  <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
  <!--Returned data-->
</API operation name+Response>
```

JSON format:

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216"
    /* Returned data */
```

#### Request syntax

This topic describes the syntax that you must follow when you make Container Registry API requests.

**Protocols**

You can send API requests over HTTP or HTTPS. We recommend that you use HTTPS to ensure higher security.

**Request methods**

The following HTTP methods are supported: PUT, POST, GET, and DELETE.

**Request parameters**

Each request must contain Common request parameters and operation-specific request parameters.

**Encoding**

All requests and responses are encoded in `UTF-8` .

#### Request signatures

You must sign all API requests to ensure security. Alibaba Cloud uses the request signature to verify the identity of the API caller.

**Signature**

A signature consists of two parts: common request header and CanonicalizedResource. The request body is not included in the signature. The common request header contains HTTP header parameters and Alibaba Cloud protocol header parameters. AccessKey pairs are issued by Alibaba Cloud. You can visit the official Alibaba Cloud website to apply for and manage an AccessKey pair. An AccessKey pair consists of an `AccessKey ID`

| AccessKey secret |   | . T |
|---|---|---|
| e |   |   |

and an `AccessKey secret` . The `AccessKey ID` is used to verify the identity of the user, while the `AccessKey secret` is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. Container Registry verifies each access request it receives. Therefore, all requests sent to Container Registry must contain signature information. Container Registry implements symmetric encryption with an AccessKey pair that consists of an `AccessKey ID` and an `AccessKey secret` to verify the identity of the request sender. If the calculated verification code is the same as the one provided, the request is considered valid. Otherwise, Container Registry rejects the request and returns the HTTP error code 403. You must add the signature to the HTTP header in the following format: `Authorization: acs`

```
[Access Key Id]:[Signature] .
```

**Signature calculation method**

The following code shows how to calculate the signature:

```
Signature = base64(hmac-sha1(VERB + "\n"
            + ACCEPT + "\n"
            + Content-MD5 + "\n"
            + Content-Type + "\n"
            + Date + "\n"
            + CanonicalizedHeaders + "\n"
            + CanonicalizedResource))
```

| VERB | in |
|---|---|
| Accept |   |

`VERB` indicates the HTTP method. Example: PUT. `Accept` indicates the response type required by the client. Valid values: application/json and application/xml.

| Content-MD5 |   | i |
|---|---|---|
| Content-Type |   |   |
| Date | indicate |   |

`Content-MD5` indicates the MD5 hash value of the request content. `Content-Type` indicates the type of request content. `Date` indicates the time when the request was sent. This parameter is required. The time must be in GMT. If the deviation between the time when a request was sent and the time when the request was received exceeds 15 minutes, the system determines that the request is invalid and returns the error code 400. Example: `Thu, 17 Mar 2018 18:00:00` `GMT` . `CanonicalizedHeaders` indicates the header fields that are prefixed with `x-acs-` in the request.

| CanonicalizedResource |   |
|---|---|
| /namespaces | . |

`CanonicalizedResource` indicates the URI of the requested resource. Example:

**CanonicalizedHeaders**

CanonicalizedHeaders (headers that start with `x-acs-` ) must comply with the following specifications before the signature is verified:

| x-acs- |   | to lowercase letters |
|---|---|---|
| to |   |   |

1. Convert the names of all HTTP request headers prefixed with `x-acs-` to lowercase letters.
For example, you must convert `X-ACS-Meta-Name: TaoBao` into `x-acs-meta-name:` `TaoBao` . Header field names are case-insensitive. We recommend that you use lowercase letters.
2. If a header field value is too long, replace specific delimiters with spaces. The delimiters
include \t , \n , \r , and \f .
3. Sort all HTTP request headers that are obtained from the preceding step in alphabetical
order.
4. Delete all spaces on each side of the delimiter between each header and head value. For

| x-acs-meta-name: TaoBao,Alipay | in |
|---|---|
| ers and content with delimiters ( \n |   |

headers.

**CanonicalizedResource**

CanonicalizedResource represents the specification description of the resource that you want to access. Arrange sub-resources and query parameters in alphabetical order. Then, separate the parameters with ampersands (&) to generate a sub-resource string. The sub-resource string consists of all parameters that follow the question mark (?) .

```
http://cr.cn-hangzhou.aliyuncs.com/repository?name=repository1&namespace=namespace1
```

The value of CanonicalizedResource must be the following string:

```
/repository?name=repository1&namespace=namespace1
```

### Manage namespaces

#### CreateNamespace

Creates a namespace.

**Request information**

**Request line**

```
PUT /namespace HTTP/1.1
```

**Request line parameters**

None.

**Operation-specific request headers**

None.

**Request body**

Request Body:

```json
    "Namespace": {
        "Namespace": "String",
```

**Request body parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Namespace | String | Yes | The name of the namespace. The name must be 2 to 30 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It _ cannot start with a hyphen (-) or an underscore ( ). _ |

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data":{
        "namespaceId":Long
```

`},`

```json
    "requestId":"String"
```

**Sample requests**

```json
PUT /namespace HTTP/1.1 <Common request headers>
    "Namespace": {
        "Namespace": "aliyun",
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "data": {},
    "requestId": "589EA3A1-9A67-4B82-95E5-11B1740178D1"
```

#### DeleteNamespace

Deletes an existing namespace. After you delete a namespace, all repositories in the namespace and all images in the repositories are deleted.

**Request information**

**Request line**

```
DELETE /namespace/[Namespace] HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|

| Namespace | String | Yes | The name of the namespace. The name must be 2 to 30 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It _ cannot start with a hyphen (-) or an underscore ( ). _ |
|---|---|---|---|

**Operation-specific request headers**

None.

**Request body**

None.

**Request body parameters**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data":{},
    "requestId":"string"
```

**Sample requests**

```
DELETE /namespace/[Namespace] HTTP/1.1 <Common request headers>
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "data": {},
    "requestId": "CBC151B2-C9B6-4393-9A7F-712C920F1DC7"
```

#### UpdateNamespace

Updates the basic information about a namespace.

**Request information**

**Request line**

```
POST /namespace/[Namespace] HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Namespace | String | Yes | The name of the namespace. |

**Operation-specific request headers**

None.

**Request body**

```json
    "Namespace": {
        "AutoCreate": Boolean,
        "DefaultVisibility": String
```

**Request body parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| AutoCreate | Boolean | Yes | Specifies whether to automatically create a repository. |
| DefaultVisibility | String | Yes | The default visibility of repositories that are created in the namespace. |

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data": {},
    "requestId": "string"
```

**Sample requests**

```json
POST /namespace/[Namespace] HTTP/1.1 <Common request headers>
    "Namespace": {
        "AutoCreate": false,
        "DefaultVisibility": "PUBLIC"
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
  "data": {},
    "requestId": "AL103117-2140-4A69-AC1A-BE69N040D01A"
```

#### GetNamespace

Queries the detailed information about a specified namespace.

**Request information**

**Request line**

```
GET /namespace/[Namespace] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Namespace | String | Yes | The name of the namespace. The name must be 2 to 30 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It _ cannot start with a hyphen (-) or an underscore ( ). _ |

**Operation-specific request headers**

None.

**Request body**

None.

**Request body parameters**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data": {
        "namespace": {
            "namespace": "String",
            "authorizeType": "String",
            "defaultVisibility": "String",
            "autoCreate": "Boolean",
            "namespaceStatus": "String"
```

`},`

```json
    "requestId": "String"
```

**Response parameters**

| Parameter | Type | Description |
|---|---|---|
| namespace | String | The name of the namespace. |
| authorizeType | String | The permissions that the current account has on the namespace. You can acquire the permissions only in the Container Registry console. |
| defaultVisibility | String | The default visibility of repositories that are created in the namespace. |
| autoCreate | String | Indicates whether to automatically create a repository when an image is pushed. If the feature is disabled, you must create a repository before you push an image. |

| namespaceStatus | String | The state of the namespace. Valid values: NORMAL and DELETING. |
|---|---|---|

**Sample requests**

```
GET /namespace/[Namespace] HTTP/1.1 <Common request headers>
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "data": {
        "namespace": {
            "namespace": "aliyun",
            "authorizeType": "ADMIN",
            "defaultVisibility": "PRIVATE",
            "autoCreate": true,
            "namespaceStatus": "NORMAL"
```

`},`

```json
    "requestId": "19228CE5-4905-4A24-A2C1-E774F32CCC31"
```

#### GetNamespaceList

Queries namespaces.

**Request information**

**Request line**

```
GET /namespace HTTP/1.1
```

**Request line parameters**

None.

**Operation-specific request headers**

None.

**Request body**

None.

**Request body parameters**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data": {
        "namespace": [
                "namespace": "String",
                "authorizeType": "String",
                "namespaceStatus": "String"
```

`]` `},`

```json
    "requestId": "string"
```

**Response body parameters**

| Parameter | Type | Description |
|---|---|---|
| namespace | String | The name of the namespace. |
| authorizeType | String | The permissions that the current account has on the namespace. You can acquire the permissions only in the Container Registry console. |
| namespaceStatus | String | The state of the namespace. Valid values: NORMAL and DELETING. |

**Sample requests**

```
GET /namespace HTTP/1.1 <Common request headers>
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "data": {
        "namespaces": [
                "namespace": "aliyun",
                "authorizeType": "ADMIN",
                "namespaceStatus": "NORMAL"
```

`},`

```json
                "namespace": "alibaba",
                "authorizeType": "ADMIN",
                "namespaceStatus": "NORMAL"
```

`]` `},`

```json
    "requestId": "AB034FC3-27E8-4E34-958B-0944E369270B"
```

### Image repository management

#### CreateRepo

Creates a repository.

**Request information**

**Request line**

```
PUT /repos HTTP/1.1
```

**Request line parameters**

None.

**Operation-specific request headers**

None.

**Request body**

Request Body:

```json
       "Repo": {
           "RepoNamespace": "String" //This parameter is required. The value must be 2
to 30 characters in length.
           "RepoName": "String" //This parameter is required. The value must be 2 to 30
characters in length.
           "Summary": "String" //This parameter is required. The value must be 1 to 100
characters in length.
           "Detail": "String" //This parameter is optional. The value of the parameter
cannot exceed 2,000 characters in length. The Markdown syntax is supported.
           "RepoType": "String" //This parameter is required. Valid values: PRIVATE and
PUBLIC.
```

**Request body parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| RepoNamespace | String | Yes | The namespace to which the image repository belongs. The name of the namespace must be 2 to 30 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It cannot start with _ a hyphen (-) or an underscore ( ). _ |
| RepoName | String | Yes | The name of the image repository. The name must be 1 to 64 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It _ cannot start with a hyphen (-) or an underscore ( ). _ |
| Summary | String | Yes | The summary of the repository. The summary must be 1 to 100 characters in length. |
| Detail | String | No | The detailed information about the repository. The Markdown syntax is supported. The value of this parameter cannot exceed 2,000 characters in length. |

| RepoType | String | Yes | The type of the repository. Valid values: PRIVATE and PUBLIC. Public repositories support anonymous downloads. To download images from a private repository, you must log on to the Container Registry console. |
|---|---|---|---|

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data": {},
    "requestId": "String"
```

**Sample requests**

```json
PUT /repos HTTP/1.1 <Common request headers>
    "repo": {
        "RepoNamespace": "aliyun",
        "RepoName": "Tengine",
        "Summary": "This is Aliyun Nginx",
        "RepoType": "PUBLIC"
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "data": {},
    "requestId": "80705201-FE46-4C08-AE30-FD50F5930993"
```

#### DeleteRepo

Deletes an existing repository. After you delete a repository, all images in the repository are deleted.

**Request information**

**Request line**

```
DELETE /repos/[RepoNamespace]/[RepoName] HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| RepoNamespace | String | Yes | The name of the namespace to which the repository belongs. The name of the namespace must be 2 to 30 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It cannot start with _ a hyphen (-) or an underscore ( ). _ |
| RepoName | String | Yes | The name of the repository. The name must be 1 to 64 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It _ cannot start with a hyphen (-) or an underscore ( ). _ |

**Operation-specific request headers**

None.

**Request body**

None.

**Request body parameters**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data":{},
    "requestId":"string"
```

**Sample requests**

```
DELETE /repos/[RepoNamespace]/[RepoName] HTTP/1.1 <Common request headers>
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "data": {},
    "requestId": "7BF6D761-E7F8-454C-A235-983E5D183B4E"
```

#### UpdateRepo

Updates the basic information about an image repository, including the repository type, summary, and description.

**Request information**

**Request line**

```
POST /repos/[RepoNamespace]/[RepoName] HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| RepoNamespace | String | Yes | The name of the namespace to which the repository belongs. |
| RepoName | String | Yes | The name of the repository. |

**Operation-specific request headers**

None.

**Request body**

```json
    "Repo": {
        "Summary": "String",
        "Detail": "String",
        "RepoType": "String"
```

**Request body parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Summary | String | Yes | The summary of the repository. |
| Detail | String | No | The detailed information about the repository. The Markdown syntax is supported. |
| RepoType | String | Yes | The type of the repository. Valid values: PRIVATE and PUBLIC. |

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data": {},
    "requestId": "String"
```

**Sample requests**

```json
POST /repos/[RepoNamespace]/[RepoName] HTTP/1.1 <Common request headers>
    "Repo": {
        "Summary": "Test repository",
        "Detail": "This is a test repository",
        "RepoType": "PRIVATE"
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "data": {},
    "requestId": "F3103017-5928-4A69-AC1A-BE69A840D01A"
```

#### GetRepoTag

Queries the information about an image.

**Request information**

**Request line**

```
GET /repos/[RepoNamespace]/[RepoName]/tag/[Tag] HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| RepoNamespace | String | Yes | The name of the namespace to which the repository belongs. |
| RepoName | String | Yes | The name of the repository. |
| Tag | String | Yes | The tag of the image. |

**Operation-specific request headers**

None.

**Request body**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Response body**

```json
    "imageUpdate": 1578625336000,
    "imageId": "6f08feb0be92c8ed2cc5b3e563313d2c08e468c1aa40d06908634884f236****",
    "requestId": "9AFB10K1-2301-4B00-A817-93249204****",
    "digest": "110acd135b0b71c38f10a6db02b0318d6ec731ec318cbfc5dadc4cc182b54052",
    "tag": 1,
    "imageSize": 558063443,
    "imageCreate": 1577445220000,
    "status": "NORMAL"
```

**Response body parameters**

| Parameter | Type | Description |
|---|---|---|
| imageUpdate | Long | The time when the image was last updated. |
| imageCreate | Long | The time when the image was created. |
| imageId | String | The ID of the image. |
| imageSize | String | The size of the image. |
| requestId | String | The ID of the request. |
| digest | String | The SHA-256 hash function of the image. |
| tag | String | The tag of the image. |
| status | String | The status of the image. |

**Sample requests**

```json
GET /repos/RepoNamespace/RepoName/tags/Tag HTTP/1.1 Common request header { "RepoName": "test", "RepoNamespace": "test", "Tag": "1.0" }
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "imageUpdate": 1578625336000,
    "imageId": "6f08feb0be92c8ed2cc5b3e563313d2c08e468c1aa40d06908634884f236****",
    "requestId": "",
    "digest": "110acd135b0b71c38f10a6db02b0318d6ec731ec318cbfc5dadc4cc182b54052",
    "tag": 1,
    "imageSize": 558063443,
    "imageCreate": 1577445220000,
    "status": "NORMAL"
```

#### GetRepo

Queries the detailed information about a repository.

**Request information**

**Request line**

```
GET /repos/[RepoNamespace]/[RepoName] HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| RepoNamespace | String | Yes | The name of the namespace to which the repository belongs. |
| RepoName | String | Yes | The name of the repository. |

**Operation-specific request headers**

None.

**Request body**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
"data":{
    "repo": {
        "summary": String,
        "repoId": Long,
        "gmtCreate": Long,
        "gmtModified": Long,
        "repoNamespace": String,
        "repoName": String,
        "repoBuildType": String,
        "repoType": String,
        "repoDomainList": {
            "public": String,
            "vpc": String
```

`},`

```json
        "regionId": String,
        "repoStatus": String,
        "detail": String,
        "repoAuthorizeType": String
```

`},`

```json
"requestId": string
```

**Response body parameters**

| Parameter | Type | Description |
|---|---|---|
| summary | String | The summary of the repository. |
| gmtCreate | Long | The time when the repository was created. |
| gmtModified | Long | The time when the repository was last modified. |
| repoNamespace | String | The name of the namespace to which the repository belongs. |
| repoName | String | The name of the repository. |
| repoBuildType | String | Indicates how the repository was created. |
| repoType | String | The type of the repository. |
| repoDomainList | Array | The domain names of the repository. |
| regionId | String | The ID of the region. |
| repoStatus | String | The status of the repository. |
| detail | String | The detailed information about the repository. |

| repoAuthorizeType | String | The permission type of the repository. |
|---|---|---|

**Sample requests**

```
GET /repos/[RepoNamespace]/[RepoName] HTTP/1.1 <Common request headers>
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
 "data":{
     "repo": {
       "summary": "test",
       "gmtCreate": 1524663834000,
       "gmtModified": 1524663871000,
       "repoNamespace": "test",
       "repoName": "test",
       "repoBuildType": "AUTO_BUILD",
       "repoType": "PUBLIC",
       "repoDomainList": {
         "public": "registry.cn-hangzhou.aliyuncs.com",
         "vpc": "registry-vpc.cn-hangzhou.aliyuncs.com"
```

`},`

```json
       "regionId": "cn-hangzhou",
       "repoStatus": "NORMAL",
       "detail": "",
       "repoAuthorizeType": "ADMIN"
```

`},`

```json
 "requestId": "B21BE190-08BA-41B6-B8B5-CA4029F1CC58"
```

#### GetRepoList

Queries information about repositories.

**Request information**

**Request line**

```
GET /repos HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|

| Status | String | Yes | The status of the repository. |
|---|---|---|---|
| RepoNamePrefix | String | Yes | The prefix of the repository name. |
| Page | Integer | No | The number of the page to return. |
| PageSize | Integer | No | The number of entries to return on each page. |

**Operation-specific request headers**

None.

**Request body**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
"data": {
    "total": Integer,
    "repos": [{
        "summary": String,
        "repoId": Long,
        "gmtCreate": Long,
        "gmtModified": Long,
        "repoNamespace": String,
        "repoName": String,
        "repoBuildType": String,
        "repoType": String,
        "repoDomainList": {
            "public": String,
            "vpc": String
```

`},`

```json
        "regionId": String,
        "repoStatus": String,
        "repoAuthorizeType": String
    }, {
        "summary": String,
        "repoId": Long,
        "gmtCreate": Long,
        "gmtModified": Long,
        "repoNamespace": String,
        "repoName": String,
        "repoBuildType": String,
        "repoType": String,
        "repoDomainList": {
            "public": String,
            "vpc": String
```

`},`

```json
        "regionId": String,
        "repoStatus": String,
        "repoAuthorizeType": String
    }],
    "pageSize": Integer,
    "page": Integer
```

`},`

```json
"requestId": String
```

**Response body parameters**

| Parameter | Type | Description |
|---|---|---|
| summary | String | The summary of the repository. |
| repoId | Long | The unique ID of the repository. |
| gmtCreate | Long | The time when the repository was created. |

| gmtModified | Long | The time when the repository was last modified. |
|---|---|---|
| repoNamespace | String | The name of the namespace to which the repository belongs. |
| repoName | String | The name of the repository. |
| repoBuildType | String | Indicates how the repository was created. |
| repoType | String | The type of the repository. |
| repoDomainList | Array | The domain names of the repository. |
| regionId | String | The ID of the region. |
| repoStatus | String | The status of the repository. |
| repoAuthorizeType | String | The permission type of the repository. |
| page | Integer | The page number of the returned page. |
| pageSize | Integer | The number of entries returned per page. |
| total | Integer | The total number of entries. |

**Sample requests**

```
GET /repos HTTP/1.1 <Common request headers>
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers> "data": {
    "total": 2,
    "repos": [{
        "summary": "Test1",
        "repoId": 00001,
        "gmtModified": 1524663871000,
        "repoNamespace": "test1",
        "repoName": "test_repo_1",
        "gmtCreate": 1524663834000,
        "repoBuildType": "AUTO_BUILD",
        "repoType": "PUBLIC",
        "repoDomainList": {
            "public": "registry.cn-hangzhou.aliyuncs.com",
            "vpc": "registry-vpc.cn-hangzhou.aliyuncs.com"
```

`},`

```json
        "regionId": "cn-hangzhou",
        "repoStatus": "NORMAL",
        "repoAuthorizeType": "ADMIN"
    }, {
        "summary": "Test2",
        "repoId": 00002,
        "gmtModified": 1487319003000,
        "repoNamespace": "test2",
        "repoName": "Test2",
        "gmtCreate": 1487319003000,
        "repoBuildType": "AUTO_BUILD",
        "repoType": "PRIVATE",
        "repoDomainList": {
            "public": "registry.cn-hangzhou.aliyuncs.com",
            "vpc": "registry-vpc.cn-hangzhou.aliyuncs.com"
```

`},`

```json
        "regionId": "cn-hangzhou",
        "repoStatus": "NORMAL",
        "repoAuthorizeType": "ADMIN"
    }],
    "pageSize": 20,
    "page": 1
```

`},`

```json
"requestId": "F11E3C4C-LO9Q-4D11-B7C5-5EFCA8E7CA2E"
```

#### GetRepoListByNamespace

Queries information about repositories.

**Request information**

**Request line**

```
GET /repos/[RepoNamespace] HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Status | String | Yes | The status of the repository. |
| RepoNamespace | String | Yes | The namespace to which the repository belongs. |
| RepoNamePrefix | String | Yes | The prefix of the repository name. |
| Page | Integer | No | The number of the page to return. |
| PageSize | Integer | No | The number of entries to return on each page. |

**Operation-specific request headers**

None.

**Request body**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
"data": {
    "total": Integer,
    "repos": [{
        "summary": String,
        "repoId": Long,
    "gmtCreate": Long,
        "gmtModified": Long,
        "repoNamespace": String,
        "repoName": String,
        "repoBuildType": String,
        "repoType": String,
        "repoDomainList": {
            "public": String,
            "vpc": String
```

`},`

```json
        "regionId": String,
        "repoStatus": String,
        "repoAuthorizeType": String
    }, {
    "summary": String,
        "repoId": Long,
    "gmtCreate": Long,
        "gmtModified": Long,
        "repoNamespace": String,
        "repoName": String,
        "repoBuildType": String,
        "repoType": String,
        "repoDomainList": {
            "public": String,
            "vpc": String
```

`},`

```json
        "regionId": String,
        "repoStatus": String,
        "repoAuthorizeType": String
    }],
    "pageSize": Integer,
    "page": Integer
```

`},`

```json
"requestId": "F11E3C4C-LO9Q-4D11-B7C5-5EFCA8E7CA2E"
```

**Response body parameters**

| Parameter | Type | Description |
|---|---|---|
| summary | String | The summary of the repository. |
| repoId | Long | The unique ID of the repository. |
| gmtCreate | Long | The time when the repository was created. |

| gmtModified | Long | The time when the repository was last modified. |
|---|---|---|
| repoNamespace | String | The name of the namespace to which the repository belongs. |
| repoName | String | The name of the repository. |
| repoBuildType | String | Indicates how the repository was created. |
| repoType | String | The type of the repository. |
| repoDomainList | Array | The domain names of the repository. |
| downloads | Long | The number of image downloads from the repository. |
| regionId | String | The ID of the region. |
| logo | String | The icon of the repository. |
| repoStatus | String | The status of the repository. |
| repoAuthorizeType | String | The permission type of the repository. |
| Page | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| total | Integer | The total number of entries. |

**Sample requests**

```
GET /repos/[RepoNamespace] HTTP/1.1 <Common request headers>
```

**Sample responses**

```json
HTTP/1.1 200 OK <Common response headers> "data": {
    "total": 2,
    "repos": [{
        "summary": "Test1",
        "repoId": 00001,
        "gmtModified": 1524663871000,
        "repoNamespace": "test",
        "repoName": "test_repo_1",
        "gmtCreate": 1524663834000,
        "repoBuildType": "AUTO_BUILD",
        "repoType": "PUBLIC",
        "repoDomainList": {
            "public": "registry.cn-hangzhou.aliyuncs.com",
            "vpc": "registry-vpc.cn-hangzhou.aliyuncs.com"
```

`},`

```json
        "regionId": "cn-hangzhou",
        "repoStatus": "NORMAL",
        "repoAuthorizeType": "ADMIN"
    }, {
        "summary": "Test2",
        "repoId": 00002,
        "gmtModified": 1487319003000,
        "repoNamespace": "test",
        "repoName": "test_repo_2",
        "gmtCreate": 1487319003000,
        "repoBuildType": "AUTO_BUILD",
        "repoType": "PRIVATE",
        "repoDomainList": {
            "public": "registry.cn-hangzhou.aliyuncs.com",
            "vpc": "registry-vpc.cn-hangzhou.aliyuncs.com"
```

`},`

```json
        "regionId": "cn-hangzhou",
        "repoStatus": "NORMAL",
        "repoAuthorizeType": "ADMIN"
    }],
    "pageSize": 20,
    "page": 1
```

`},`

```json
"requestId": "F11E3C4C-LO9Q-4D11-B7C5-5EFCA8E7CA2E"
```

#### GetRepoTags

Queries the information about images in a repository.

**Request information**

**Request line**

```
GET /repos/[RepoNamespace]/[RepoName]/tags HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| RepoNamespace | String | Yes | The name of the namespace to which the repository belongs. |
| RepoName | String | Yes | The name of the repository. |
| Page | Integer | No | The number of the page to return. |
| PageSize | Integer | No | The number of entries to return on each page. |

**Operation-specific request headers**

None.

**Request body**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
"data": {
 "total": Integer,
 "pageSize": Integer,
 "page": Integer,
 "tags": [{
   "imageUpdate": Long,
    "imageCreate": Long,
   "imageId": String,
   "digest": String,
   "imageSize": Long,
   "tag": String,
   "status": String
 }, {
   "imageUpdate": Long,
   "imageCreate": Long,
   "imageId": String,
   "digest": String,
   "imageSize": Long,
   "tag": String,
   "status": String
```

`}]` `},`

```json
"requestId": "9AFB10K1-2301-4B00-A817-932492040126"
```

**Response body parameters**

| Parameter | Type | Description |
|---|---|---|
| imageUpdate | Long | The time when the image was last updated. |
| imageCreate | Long | The time when the image was created. |
| imageId | String | The ID of the image. |
| digest | String | The SHA-256 hash function of the image. |
| imageSize | Long | The size of the image. |
| tag | String | The tag of the image. |
| status | String | The status of the image. |
| page | Integer | The page number of the returned page. |
| pageSize | Integer | The number of entries returned per page. |
| total | Integer | The total number of entries. |

**Sample requests**

```
GET /repos/[RepoNamespace]/[RepoName]/tags HTTP/1.1 <Common request headers>
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
   "total": 2,
   "pageSize": 30,
   "page": 1,
   "tags": [{
     "imageUpdate": 1514432549000,
     "imageId": "2842876c9b98f8c7607c1123ks18ff040b76a1d932c6d60c96aa3c283bd221cd",
     "digest": "83414d2c3b04e0lo1q7693e31aeca95b82c61949ea8de858579bf16bd92490c6",
     "imageSize": 715764,
     "tag": "new",
     "imageCreate": 1514432549000,
     "status": "NORMAL"
   }, {
     "imageUpdate": 1514372113000,
     "imageId": "414e6daa772a8cd5dfloqpe503e6e313c372d2e15958ab649709daf9b1065479",
     "digest": "fcf39ed78ef0fa27bcc74713b85259alop1b12e6a201e3083af50fd8eda1cbe1",
     "imageSize": 715653,
     "tag": "asdf",
     "imageCreate": 1514372044000,
     "status": "NORMAL"
```

`}]` `},`

```json
 "requestId": "9AFB52D3-6631-4B00-A857-932492097726"
```

### Image management

#### DeleteImage

Deletes an image tag. After an image tag is deleted, it cannot be recovered.

**Request information**

**Request line**

```
DELETE /repos/[RepoNamespace]/[RepoName]/tags/[Tag] HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|

| RepoNamespace | String | Yes | The name of the namespace. |
|---|---|---|---|
| RepoName | String | Yes | The name of the repository. |
| Tag | String | Yes | The tag of the image. |

**Operation-specific request headers**

None.

**Request body**

None.

**Request body parameters**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data":{},
    "requestId":"string"
```

**Sample requests**

```
DELETE /repos/[RepoNamespace]/[RepoName]/tags/[Tag] HTTP/1.1 <Common request headers>
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "data": {},
    "requestId": "7BF6D761-E7F8-454C-A235-983E5D183B4E"
```

#### GetImageManifest

Queries the manifest information about an image.

**Request information**

**Request line**

```
GET /repos/[RepoNamespace]/[RepoName]/tags/[Tag]/manifest HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| RepoNamespace | String | Yes | The name of the namespace. |
| RepoName | String | Yes | The name of the repository. |
| Tag | String | Yes | The tag of the image. |

**Operation-specific request headers**

None.

**Request body**

None.

**Request body parameters**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
  "data": {
    "manifest": {
      "name": "String",
      "fsLayers": "Array",
      "history": "Array",
      "signatures": "Array",
      "architecture": "String",
      "tag": "String",
      "schemaVersion": "Integer"
```

`},`

```json
  "requestId": "String"
```

**Response body parameters**

| Parameter | Type | Description |
|---|---|---|
| name | String | The name of the image, namespace, or repository. |
| fsLayers | String | The SHA-256 hash function of each layer of the image. |
| history | Array | Unstructured historical data that complies with schema v1. |
| signatures | Array | The signature of the image. |
| architecture | String | The architecture of the image. |
| tag | String | The tag of the image. |
| schemaVersion | Integer | The schema version. A value of 1 indicates manifest v2 and schema 1. A value of 2 indicates manifest v2 and schema 2. |

**Sample requests**

```
GET /repos/[RepoNamespace]/[RepoName]/tags/[Tag]/manifest HTTP/1.1 <Common request headers>
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
  "data": {
    "manifest": {
      "name": "testNamespace/testRepo",
      "fsLayers": [{
        "blobSum": "sha256:a"
      }],
      "history": [{
        "v1Compatibility": {
          "parent": "b",
          "os": "linux",
          "created": "2018-01-01T00:00:00.000000001Z",
          "container_config": {},
          "id": "c",
          "config": {},
          "docker_version": "17.12.0-ce",
          "architecture": "amd64"
      }],
      "signatures": [{
        "signature": "e",
        "header": {
          "alg": "ES256",
          "jwk": {}
```

`},`

```json
        "protected": "f"
      }],
      "architecture": "amd64",
      "tag": "tag1",
      "schemaVersion": 1
```

`},`

```json
  "requestId": "8DBD3292-A232-44F6-93DC-B30D70AF54E9"
```

#### GetImageLayer

Queries the layer information about an image.

**Request information**

**Request line**

```
GET /repos/[RepoNamespace]/[RepoName]/tags/[Tag]/layers HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|

| RepoNamespace | String | Yes | The name of the namespace. |
|---|---|---|---|
| RepoName | String | Yes | The name of the repository. |
| Tag | String | Yes | The tag of the image. |

**Operation-specific request headers**

None.

**Request body**

None.

**Request body parameters**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data": {
      "image": {
        "repoNamespace": "String",
        "repoName": "String",
        "layers": "Array",
        "tag": "String",
        "region": "String"
```

`},`

```json
    "requestId": "String"
```

**Response body parameters**

| Parameter | Type | Description |
|---|---|---|
| repoNamespace | String | The name of the namespace. |
| repoName | String | The name of the image repository. |
| layers | Array | The layer information of the image. |
| tag | String | The tag of the image. |

| region | String | The region where the image repository is deployed. |
|---|---|---|

**Sample requests**

```
GET /repos/[RepoNamespace]/[RepoName]/tags/[Tag]/layers HTTP/1.1 <Common request headers>
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "data": {
      "image": {
        "repoNamespace": "testNamespace",
        "repoName": "testRepo",
        "layers": [{
          "layerCMD": "file:a in /TEMP",
          "blobDigest": "sha256:b",
          "blobSize": 1000,
          "layerInstruction": "COPY",
          "layerIndex": 2
        }, {
          "layerCMD": "[\"bash\"]",
          "blobDigest": "sha256:c",
          "blobSize": 32,
          "layerInstruction": "CMD",
          "layerIndex": 1
        }, {
          "layerCMD": "file:e in /",
          "blobDigest": "sha256:f",
          "blobSize": 52608285,
          "layerInstruction": "ADD",
          "layerIndex": 0
        }],
        "tag": "latest",
        "region": "cn-hangzhou"
```

`},`

```json
    "requestId": "8DBD3292-A232-44F6-93DC-B30D70AF54E9"
```

### Trigger management

#### CreateRepoWebhook

Creates a trigger for an image repository.

**Request information**

**Request line**

```
PUT /repos/[RepoNamespace]/[RepoName]/webhooks HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| RepoNamespace | String | Yes | The namespace to which the repository belongs. |
| RepoName | String | Yes | The name of the repository. |

**Operation-specific request headers**

None.

**Request body**

```json
Request Body:
    "Webhook": {
        "WebhookName": "String" This parameter is required.
        "WebhookUrl": "String" This parameter is required.
        "TriggerType": "String" This parameter is required. Valid values: ALL,
TAG_REG_EXP, and TAG_LIST.
```

**Request body parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| WebhookName | String | Yes | The name of the trigger. |
| WebhookUrl | String | Yes | The URL of the trigger when an image is pushed to the repository. |
| TriggerType | String | Yes | The type of trigger. Valid values: ALL, TAG REG EXP, and _ _ TAG LIST. The trigger _ type determines that the trigger is invoked by the tag (TAG LIST), _ regular expression (TAG REG EXP), or _ _ both (ALL), of the image that is pushed to the repository. |

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data": {
        "webhookId": "String"
```

`},`

```json
    "requestId": "String"
```

**Sample requests**

```json
PUT /repos/[RepoNamespace]/[RepoName]/webhooks HTTP/1.1 <Common request headers>
    "Webhook": {
        "WebhookName": "MyTrigger",
        "WebhookUrl": "https://www.****.com",
        "TriggerType": "ALL"
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "data": {
        "webhookId": "39762"
```

`},`

```json
    "requestId": "3666F8EA-1468-4BEA-883B-FC60A651A609"
```

#### DeleteRepoWebhook

Deletes a trigger of a repository.

**Request information**

**Request line**

```
DELETE /repos/[RepoNamespace]/[RepoName]/webhooks/[WebhookId] HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| RepoNamespace | String | Yes | The namespace to which the repository belongs. You must select a created namespace. |
| RepoName | String | Yes | The name of the image repository. |
| WebhookId | Long | Yes | The ID of the trigger. |

**Operation-specific request headers**

None.

**Request body**

None.

**Request body parameters**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data": {},
    "requestId": "String"
```

**Sample requests**

```
DELETE /repos/[RepoNamespace]/[RepoName]/webhooks/[WebhookId] HTTP/1.1 <Common request headers>
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "data": {},
    "requestId": "639F1195-56D9-49B7-BC47-B3BFCC9ED1C9"
```

#### GetRepoWebhook

Queries triggers for an image repository.

**Request information**

**Request line**

```
GET /repos/[RepoNamespace]/[RepoName]/webhooks HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| RepoNamespace | String | Yes | The name of the namespace to which the repository belongs. |
| RepoName | String | Yes | The name of the repository. |

**Operation-specific request headers**

None.

**Request body**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data": {
        "webhooks":[
                "webhookId": Long,
                "triggerTag": String,
                "webhookName": String,
                "triggerType": String,
                "webhookUrl": String
```

`]` `},`

```json
    "requestId": String
```

**Response body parameters**

| Parameter | Type | Description |
|---|---|---|
| webhookId | Long | The ID of the webhook. |
| triggerTag | String | The trigger that is invoked by tags. |
| webhookName | String | The name of the webhook. |
| triggerType | String | The trigger mode |
| webhookUrl | String | The URL of the trigger. |
| syncTaskId | String | The ID of the synchronization task. |
| RequestId | String | The unique ID of the request. |

**Sample requests**

```
GET /repos/[RepoNamespace]/[RepoName]/webhooks HTTP/1.1 <Common request headers>
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "data": {
        "webhooks":[
                "webhookId": 39726,
                "triggerTag": "",
                "webhookName": "justForTest",
                "triggerType": "ALL",
                "webhookUrl": "https://www.****.com"
```

`]` `},`

```json
    "requestId": "A86AB63A-758B-4FD9-9CB1-1421083A2EF5"
```

#### UpdateRepoWebhook

Updates a trigger for an image repository.

**Request information**

**Request line**

```
POST /repos/[RepoNamespace]/[RepoName]/webhooks/[WebhookId] HTTP/1.1
```

**Request line parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| RepoNamespace | String | Yes | The name of the namespace to which the repository belongs. |
| RepoName | String | Yes | The name of the repository. |
| WebhookId | String | Yes | The ID of the trigger. |

**Operation-specific request headers**

None.

**Request body**

```json
   "Webhook": {
      "WebhookName": "String",
      "WebhookUrl": "String",
      "TriggerName": "String",
      "TriggerUrl": "String",
      "TriggerType": "String"
```

**Request body parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| WebhookName | String | Yes | The name of the trigger. The name must be 2 to 30 characters in length, and can contain lowercase letters, digits, and underscores ( ). It _ cannot start with an underscore ( ). _ |
| WebhookUrl | String | Yes | The URL of the trigger. The URL must be 1 to 1,024 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It cannot start with _ a hyphen (-) or an underscore ( ). _ |

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data": {
```

`},`

```json
    "requestId": "String"
```

**Response body parameters**

None.

**Sample requests**

```json
POST /repos/[RepoNamespace]/[RepoName]/webhooks/[WebhookId] HTTP/1.1 <Common request headers>
   "Webhook": {
      "WebhookName": "justForTest",
      "WebhookUrl": "https://www.****.com",
      "TriggerName": "justForTest",
      "TriggerUrl": "https://www.****.com",
      "TriggerType": "ALL"
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "data": {
```

`},`

```json
    "requestId": "8DBD3292-A232-44F6-93DC-B30D70AF54E9"
```

### Access credential

**management**

#### GetAuthorizationToken

Returns the temporary account and token that you use to log on to the registry. The token is valid for 1 hour. If you send a Security Token Service (STS) request, the token is valid within the request period of the STS token.

**Permissions**

| Invocation method | Permissions |
|---|---|
| Apsara Stack tenant account | Logon to the registry with the token and logon to the registry with the username and password of the Apsara Stack tenant account allow you to have the same permissions. |
| RAM user | Logon to the registry with the token and logon to the registry with the username and password of the RAM user allow you to have the same permissions. |
| STS | If you log on to the registry with the token, the permissions of your account are determined by the permission policies attached to the role. |

**Request information**

**Request line**

```
Get /tokens HTTP/1.1
```

**Request line parameters**

None.

**Operation-specific request headers**

None.

**Request body**

None.

**Response information**

**Response line**

```
HTTP/1.1 200 OK
```

**Operation-specific response headers**

None.

**Response body**

```json
    "data": {
        "authorizationToken": "String",
        "tempUserName": "String",
        "expireDate": Long
```

`},`

```json
    "requestId": "String"
```

**Response body parameters**

| Parameter | Type | Description |
|---|---|---|
| authorizationToken | String | The token that you use to log on to the registry. |
| tempUserName | String | The username that you use to log on to the registry. |
| expireDate | Long | The timestamp when the token expires. Unit: milliseconds. |

**Sample requests**

```
Get /tokens HTTP/1.1 <Common request headers>
```

**Sample success responses**

```json
HTTP/1.1 200 OK <Common response headers>
    "data": {
        "authorizationToken": "eyJ0aW1lIjoiMTUyNjU0OTc5:0705733****",
        "tempUserName": "cr_temp_user",
        "expireDate": 1526549792000
```

`},`

```json
    "requestId": "94E89857-B994-44B6-9C4F-DBD200E9E272"
```

## API references for

**Container Registry Advanced**

**Edition**

### Namespace management

#### CreateNamespace

Creates a namespace.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateNamespa ce | The operation that you want to perform. Set the value to CreateNamespace. |
| RegionId | String | Yes | cn-wl-env**** | The region ID of the namespace. |
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| NamespaceNam e | String | Yes | namespace1 | The name of the namespace. |
| AutoCreateRepo | Boolean | No | true | Specifies whether to automatically create an image repository. |
| DefaultRepoTyp e | String | No | PUBLIC | The default type of the repository that is automatically created. Valid values: PUBLIC PRIVATE |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. |

| RequestId | String | BC648259-91A7- 4502-BED3- EDF64361FA83 | The ID of the request. |
|---|---|---|---|

Sample requests

```
http(s)://[Endpoint]/?Action=CreateNamespace &InstanceId=cri-pri**** &NamespaceName=namespace1 &RegionId=cn-wl-env**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <IsSuccess>true</IsSuccess> <RequestId>BC648259-91A7-4502-BED3-EDF64361FA83</RequestId> <Code>success</Code>
```

`JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json
  "IsSuccess" : true,
  "RequestId" : "BC648259-91A7-4502-BED3-EDF64361FA83",
  "Code" : "success"
```

#### DeleteNamespace

Deletes a namespace.

**Note**

After you delete a namespace, all repositories in the namespace and all images in these repositories are deleted as well.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteNamespa ce | The operation that you want to perform. Set the value to DeleteNamespace. |

| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
|---|---|---|---|---|
| NamespaceNam e | String | Yes | ns3 | The name of the namespace. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the namespace. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| RequestId | String | BA08C185-8F76- 48D7-ACB3- BA11BF2778F9 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteNamespace &InstanceId=cri-pri**** &NamespaceName=ns3 &RegionId=cn-wl-en**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>BA08C185-8F76-48D7-ACB3-BA11BF2778F9</RequestId> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess":true,
    "RequestId":"BA08C185-8F76-48D7-ACB3-BA11BF2778F9",
    "Code":"success"
```

#### UpdateNamespace

Updates a namespace.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateNamespa ce | The operation that you want to perform. Set the value to UpdateNamespace. |
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| NamespaceNam e | String | Yes | test | The name of the namespace. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the namespace. |
| AutoCreateRepo | Boolean | No | true | Specifies whether to automatically create a repository when an image is pushed to the namespace. |
| DefaultRepoTyp e | String | No | PRIVATE | The default type of the repository. Valid values: PUBLIC : The repository is a public repository. PRIVATE : The repository is a private repository. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| RequestId | String | 90B8475C-C066- 4B92-946E- 4D0DECB514E8 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateNamespace &InstanceId=cri-pri**** &NamespaceName=test &RegionId=cn-wl-en**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>90B8475C-C066-4B92-946E-4D0DECB514E8</RequestId> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess":true,
    "RequestId":"90B8475C-C066-4B92-946E-4D0DECB514E8",
    "Code":"success"
```

#### GetNamespace

Queries details about a namespace.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetNamespace | The operation that you want to perform. Set the value to GetNamespace. |
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| NamespaceNam e | String | No | test | The name of the namespace. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the namespace. |
| NamespaceId | String | No | crn- tiw8t3f8i5lta**** | The ID of the namespace. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| AutoCreateRe po | Boolean | true | Indicates whether a repository is automatically created when an image is pushed to the namespace. |
|---|---|---|---|
| Code | String | success | The return value. |
| DefaultRepoTy pe | String | PUBLIC | The default type of the repository. Valid values: PUBLIC: The repository is a public repository. PRIVATE: The repository is a private repository. |
| InstanceId | String | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| NamespaceId | String | crn-tiw8t3f8i5lt**** | The ID of the namespace. |
| NamespaceNa me | String | test | The name of the namespace. |
| NamespaceSta tus | String | NORMAL | The status of the namespace. |
| RequestId | String | E4BC9E21-8AA5- 4582-83C1- C1209AB8196F | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=GetNamespace &InstanceId=cri-pri**** &NamespaceName=test &RegionId=cn-wl-en**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AutoCreateRepo>true</AutoCreateRepo> <Code>success</Code> <DefaultRepoType>PUBLIC</DefaultRepoType> <InstanceId>cri-pri****</InstanceId> <IsSuccess>true</IsSuccess> <NamespaceName>test</NamespaceName> <NamespaceId>crn-tiw8t3f8i5lta4uv</NamespaceId> <NamespaceStatus>NORMAL</NamespaceStatus> <RequestId>E4BC9E21-8AA5-4582-83C1-C1209AB8196F</RequestId>
```

`JSON` format

```json
    "AutoCreateRepo": "true",
    "Code": "success",
    "DefaultRepoType": "PUBLIC",
    "InstanceId": "cri-pri****",
    "IsSuccess": "true",
    "NamespaceName": "test",
    "NamespaceId": "crn-tiw8t3f8i5lta4uv",
    "NamespaceStatus": "NORMAL",
    "RequestId": "E4BC9E21-8AA5-4582-83C1-C1209AB8196F"
```

**Error codes**

访问错误中心查看更多错误码。 For a list of error codes, visit the API Error Center.

#### ListNamespace

Queries the namespaces.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListNamespace | The operation that you want to perform. Set the value to ListNamespace. |
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the namespace. |

| NamespaceStat us | String | No | NORMAL | The status of the namespace. Valid values: NORMAL : The namespace is normal. DELETING : The namespace is being deleted. |
|---|---|---|---|---|
| NamespaceNam e | String | No | test-namespace | The name of the namespace. |
| PageNo | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| Namespaces | Array of Namespaces |   | The information about namespaces. |
| AutoCreateRe po | Boolean | true | Indicates whether a repository is automatically created when an image is pushed to the namespace. |
| DefaultRepoTy pe | String | PUBLIC | The default type of the repository. Valid values: PUBLIC : The repository is a public repository. PRIVATE : The repository is a private repository. |
| InstanceId | String | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| NamespaceId | String | crn-tiw8t3f8i5lt**** | The ID of the namespace. |

| NamespaceNa me | String | test | The names of the queried namespaces. |
|---|---|---|---|
| NamespaceSta tus | String | NORMAL | The status of the namespace. Valid values: NORMAL : The namespace is normal. DELETING : The namespace is being deleted. |
| PageNo | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 30 | The number of entries returned per page. |
| RequestId | String | B7E5FCA5-55ED- 451C-9649- 0BB2B93387D0 | The ID of the request. |
| TotalCount | String | 1 | The total number of returned entries. |

Sample requests

```
http(s)://[Endpoint]/?Action=ListNamespace &InstanceId=cri-pri**** &RegionId=cn-wl-en**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <Namespaces>
    <NamespaceStatus>NORMAL</NamespaceStatus>
    <NamespaceName>test</NamespaceName>
    <DefaultRepoType>PUBLIC</DefaultRepoType>
    <InstanceId>cri-pri****</InstanceId>
    <AutoCreateRepo>true</AutoCreateRepo>
    <NamespaceId>crn-tiw8t3f8i5lt****</NamespaceId>
</Namespaces> <TotalCount>1</TotalCount> <PageSize>30</PageSize> <RequestId>B7E5FCA5-55ED-451C-9649-0BB2B93387D0</RequestId> <PageNo>1</PageNo> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess": true,
    "Namespaces": {
        "NamespaceStatus": "NORMAL",
        "NamespaceName": "test",
        "DefaultRepoType": "PUBLIC",
        "InstanceId": "cri-pri****",
        "AutoCreateRepo": true,
        "NamespaceId": "crn-tiw8t3f8i5lt****"
```

`},`

```json
    "TotalCount": 1,
    "PageSize": 30,
    "RequestId": "B7E5FCA5-55ED-451C-9649-0BB2B93387D0",
    "PageNo": 1,
    "Code": "success"
```

### Image repository management

#### CreateRepository

Creates an image repository.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRepositor y | The operation that you want to perform. Set the value to CreateRepository. |
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the namespace. |
| RepoName | String | Yes | repo1 | The name of the image repository. |
| RepoNamespace Name | String | Yes | namespace01 | The name of the namespace to which the image repository belongs. |
| RepoType | String | Yes | PRIVATE | The type of the repository. Valid values: PUBLIC : The repository is a public repository. PRIVATE : The repository is a private repository. |

| Summary | String | Yes | repo1 | The summary of the repository. |
|---|---|---|---|---|
| Detail | String | No | repo1 | The description of the repository. |
| TagImmutability | Boolean | No | true | Specifies whether to enable the feature of image tag immutability. Valid values: true : enables the feature of image tag immutability. false : disables the feature of image tag immutability. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| RepoId | String | crr- xwvi3osiy4ff**** | The ID of the image repository. |
| RequestId | String | 886FB272-15C3- 44FC-AA54- F4ABD5B93A28 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=CreateRepository &InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoName=repo1 &RepoNamespaceName=namespace01 &RepoType=PRIVATE &Summary=repo1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>886FB272-15C3-44FC-AA54-F4ABD5B93A28</RequestId> <RepoId>crr-xwvi3osiy4ff****</RepoId> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess": true,
    "RequestId": "886FB272-15C3-44FC-AA54-F4ABD5B93A28",
    "RepoId": "crr-xwvi3osiy4ff****",
    "Code": "success"
```

#### DeleteRepository

Deletes an image repository.

**Important**

If you delete a repository, all images in the repository are deleted as well.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteRepositor y | The operation that you want to perform. Set the value to DeleteRepository. |
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the instance. |
| RepoId | String | Yes | crr- l4933wbcmun2* *** | The ID of the image repository. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |

| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
|---|---|---|---|
| RequestId | String | 47DD9D56-09A0- 4C52-B520- C3805DBAB96B | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteRepository &InstanceId=cn-wl-en**** &RegionId=cri-pri**** &RepoId=crr-l4933wbcmun2**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>47DD9D56-09A0-4C52-B520-C3805DBAB96B</RequestId> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess": true,
    "RequestId": "47DD9D56-09A0-4C52-B520-C3805DBAB96B",
    "Code": "success"
```

#### UpdateRepository

Updates an image repository.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateRepositor y | The operation that you want to perform. Set the value to UpdateRepository. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the repository. |

| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
|---|---|---|---|---|
| RepoId | String | Yes | crr- tquyps22md8p* *** | The ID of the image repository. |
| RepoType | String | Yes | PUBLIC | The type of the repository. Valid values: PUBLIC : The repository is a public repository. PRIVATE : The repository is a private repository. |
| Summary | String | Yes | test repo | The summary of the repository. |
| Detail | String | No | repo-for-test | The description of the repository. |
| TagImmutability | Boolean | No | true | Specifies whether to enable the feature of image tag immutability. Valid values: true : enables the feature of image tag immutability. false : disables the feature of image tag immutability. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| RequestId | String | CC43EC6B-0DD4- 40AE-8811- B0519617051A | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateRepository &InstanceId=cri-pri**** &RepoId=crr-tquyps22md8p**** &RepoType=PUBLIC &Summary=test repo &Detail=repo-for-test &TagImmutability=true &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <UpdateRepositoryResponse>
    <Code>success</Code>
    <IsSuccess>true</IsSuccess>
    <RequestId>CC43EC6B-0DD4-40AE-8811-B0519617051A</RequestId>
</UpdateRepositoryResponse>
```

`JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json
  "Code" : "success",
  "IsSuccess" : true,
  "RequestId" : "CC43EC6B-0DD4-40AE-8811-B0519617051A"
```

#### ListRepository

Queries image repositories.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListRepository | The operation that you want to perform. Set the value to ListRepository. |
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the instance. |

| RepoStatus | String | No | NORMAL | The status of the repository. Valid values: NORMAL : The repository is normal. DELETING : The repository is being deleted. DELETED : The repository was deleted. |
|---|---|---|---|---|
| RepoName | String | No | repo-test | The name of the repository. |
| RepoNamespace Name | String | No | repo- namespace-test | The name of the namespace to which the repositories belong. |
| PageNo | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| PageNo | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 30 | The number of entries returned per page. |
| Repositories | Array of Repositories |   | The information about the repositories. |
| CreateTime | Long | 1564153576000 | The time when the repository was created. |
| InstanceId | String | cn-wl-en**** | The ID of the Container Registry Enterprise Edition instance. |
| ModifiedTime | Long | 1564153576000 | The time when the repository was last modified. |

| RepoBuildType | String | MANUAL | Indicates how the repository was created. Valid values: AUTO : The repository was automatically created. MANUAL : The repository was manually created. |
|---|---|---|---|
| RepoId | String | crr- 03cuozrsqhkw**** | The ID of the repository. |
| RepoName | String | test | The name of the repository. |
| RepoNamespa ceName | String | test | The name of the namespace to which the repositories belong. |
| RepoStatus | String | NORMAL | The status of the repository. |
| RepoType | String | PRIVATE | The type of the repository. Valid values: PUBLIC : The repository is a public repository. PRIVATE : The repository is a private repository. |
| Summary | String | test OK | The summary of the repository. |
| TagImmutabili ty | Boolean | true | Indicates whether the feature of image tag immutability is enabled. |
| RequestId | String | 5241C090-DA69- 4B0F-8E3F- 2F24FDE1110E | The ID of the request. |
| TotalCount | String | 1 | The total number of returned entries. |

Sample requests

```
http(s)://[Endpoint]/?Action=ListRepository &InstanceId=cri-pri**** &RegionId=cn-wl-en**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Repositories>
    <RepoNamespaceName>test</RepoNamespaceName>
    <TagImmutability>true</TagImmutability>
    <RepoBuildType>MANUAL</RepoBuildType>
    <ModifiedTime>1564153576000</ModifiedTime>
    <RepoType>PRIVATE</RepoType>
    <RepoStatus>NORMAL</RepoStatus>
    <InstanceId>cri-pri****</InstanceId>
    <CreateTime>1564153576000</CreateTime>
    <RepoName>test</RepoName>
    <Summary>test OK</Summary>
    <RepoId>crr-03cuozrsqhkw****</RepoId>
</Repositories> <IsSuccess>true</IsSuccess> <TotalCount>1</TotalCount> <PageSize>30</PageSize> <RequestId>5241C090-DA69-4B0F-8E3F-2F24FDE1110E</RequestId> <PageNo>1</PageNo> <Code>success</Code>
```

`JSON` format

```json
    "Repositories": {
        "RepoNamespaceName": "test",
        "TagImmutability": true,
        "RepoBuildType": "MANUAL",
        "ModifiedTime": 1564153576000,
        "RepoType": "PRIVATE",
        "RepoStatus": "NORMAL",
        "InstanceId": "cri-pri****",
        "CreateTime": 1564153576000,
        "RepoName": "test",
        "Summary": "test OK",
        "RepoId": "crr-03cuozrsqhkw****"
```

`},`

```json
    "IsSuccess": true,
    "TotalCount": 1,
    "PageSize": 30,
    "RequestId": "5241C090-DA69-4B0F-8E3F-2F24FDE1110E",
    "PageNo": 1,
    "Code": "success"
```

#### GetRepository

Queries details about an image repository.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| ontainer Registry |   |   |   | or Container Registry Advanced ditio |
|---|---|---|---|---|

| Action | String | Yes | GetRepository | The operation that you want to perform. Set the value to GetRepository. |
|---|---|---|---|---|
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the instance. |
| RepoId | String | No | crr- l5eoubonp0l**** | The ID of the repository. |
| RepoNamespace Name | String | No | test | The name of the namespace to which the repository belongs. |
| RepoName | String | No | test | The name of the repository. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| CreateTime | Long | 1570759546000 | The time when the repository was created. |
| Detail | String | test | The description of the repository. |
| InstanceId | String | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| ModifiedTime | Long | 1570759546100 | The time when the repository was last modified. |

| RepoBuildType | String | MANUAL | Indicates how the repository was created. Valid values: MANUAL : The repository was manually created. AUTO : The repository was automatically created. |
|---|---|---|---|
| RepoId | String | crr- l5eoubonp0l**** | The ID of the repository. |
| RepoName | String | test | The name of the repository. |
| RepoNamespa ceName | String | test | The name of the namespace to which the repository belongs. |
| RepoStatus | String | NORMAL | The status of the repository. |
| RepoType | String | PRIVATE | The type of the repository. Valid values: PUBLIC : The repository is a public repository. PRIVATE : The repository is a private repository. |
| RequestId | String | 915E6734-3E50- 4640-8DBA- 126D2D94DE29 | The ID of the request. |
| Summary | String | Automatically created repository | The summary of the repository. |
| TagImmutabili ty | Boolean | true | Indicates whether the feature of image tag immutability is enabled. Valid values: true : The feature of image tag immutability is enabled. false : The feature of image tag immutability is disabled. |

Sample requests

```
http(s)://[Endpoint]/?Action=GetRepository &InstanceId=cri-pri**** &RegionId=cn-wl-en**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RepoNamespaceName>test</RepoNamespaceName> <IsSuccess>true</IsSuccess> <RequestId>915E6734-3E50-4640-8DBA-126D2D94DE29</RequestId> <InstanceId>cri-pri****</InstanceId> <CreateTime>1570759546000</CreateTime> <RepoName>test</RepoName> <Code>success</Code> <TagImmutability>true</TagImmutability> <RepoBuildType>MANUAL</RepoBuildType> <ModifiedTime>1570759546100</ModifiedTime> <RepoType>PRIVATE</RepoType> <RepoStatus>NORMAL</RepoStatus> <Summary>Automatically created repository</Summary> <RepoId>crr-l5eoubonp0l****</RepoId> <Detail>test</Detail>
```

`JSON` format

```json
    "RepoNamespaceName": "test",
    "IsSuccess": true,
    "RequestId": "915E6734-3E50-4640-8DBA-126D2D94DE29",
    "InstanceId": "cri-pri****",
    "CreateTime": 1570759546000,
    "RepoName": "test",
    "Code": "success",
    "TagImmutability": true,
    "RepoBuildType": "MANUAL",
    "ModifiedTime": 1570759546100,
    "RepoType": "PRIVATE",
    "RepoStatus": "NORMAL",
    "Summary": "Automatically created repository",
    "RepoId": "crr-l5eoubonp0l****",
    "Detail": "test"
```

**Error codes**

访问错误中心查看更多错误码。 For a list of error codes, visit the API Error Center.

### Image management

#### ListRepoTag

Queries images in a repository.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | ListRepoTag | The operation that you want to perform. Set the value to ListRepoTag. |
|---|---|---|---|---|
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the instance. |
| RepoId | String | Yes | crr- tquyps22md8p* *** | The ID of the repository. |
| PageNo | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| Images | Array of Images |   | The images. |
| Digest | String | 67bfbcc12b67936e c7f867927817cbb0 71832b873dbcaed 312a1930ba5f1*** * | The digest of the image. |
| ImageCreate | String | 1572839125000 | The time when the image was created. |
| ImageId | String | 45023655bf39c382 e26a8607d057c27 871dee163c1ecf48 cc1ebf2a1**** | The ID of the image. |
| ImageSize | Long | 27107966 | The size of the image. |
| ImageUpdate | String | 1572875608000 | The time when the image was last updated. |
| Status | String | NORMAL | Status |
| Tag | String | v0.1 | The tag of the image. |

| Container Registry |   |   | or Container Registry Advanced ditio |
|---|---|---|---|

| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
|---|---|---|---|
| PageNo | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 30 | The number of entries returned per page. |
| RequestId | String | 031572FA-7D8F- 4C05-B790- 1071E0E05DE6 | The ID of the request. |
| TotalCount | String | 1 | The total number of returned entries. |

Sample requests

```
http(s)://[Endpoint]/?Action=ListRepoTag &InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-tquyps22md8p**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <TotalCount>1</TotalCount> <PageSize>30</PageSize> <RequestId>031572FA-7D8F-4C05-B790-1071E0E05DE6</RequestId> <Images>
    <Status>NORMAL</Status>
    <ImageCreate>1572839125000</ImageCreate>
    <ImageSize>27107966</ImageSize>
    <Digest>67bfbcc12b67936ec7f867927817cbb071832b873dbcaed312a1930ba5f1****</Digest>
    <ImageId>45023655bf39c382e26a8607d057c27871dee163c1ecf48cc1ebf2a1****</ImageId>
    <ImageUpdate>1572875608000</ImageUpdate>
    <Tag>v0.1</Tag>
</Images> <PageNo>1</PageNo> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess": true,
    "TotalCount": 1,
    "PageSize": 30,
    "RequestId": "031572FA-7D8F-4C05-B790-1071E0E05DE6",
    "Images": {
        "Status": "NORMAL",
        "ImageCreate": 1572839125000,
        "ImageSize": 27107966,
        "Digest": "67bfbcc12b67936ec7f867927817cbb071832b873dbcaed312a1930ba5f1****",
        "ImageId": "45023655bf39c382e26a8607d057c27871dee163c1ecf48cc1ebf2a1****",
        "ImageUpdate": 1572875608000,
        "Tag": "v0.1"
```

`},`

```json
    "PageNo": 1,
    "Code": "success"
```

#### DeleteRepoTag

Deletes an image from a repository.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteRepoTag | The operation that you want to perform. Set the value to DeleteRepoTag. |
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the instance. |
| RepoId | String | Yes | crr- xwvi3osiy4ff**** | The ID of the image repository. |
| Tag | String | Yes | 1.24 | The tag of the image. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |

| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
|---|---|---|---|
| RequestId | String | 96E66B3A-C81A- 48BE-ACD6- C0AB1F9313C0 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteRepoTag &InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-xwvi3osiy4ff**** &Tag=1.24 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>96E66B3A-C81A-48BE-ACD6-C0AB1F9313C0</RequestId> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess": true,
    "RequestId": "96E66B3A-C81A-48BE-ACD6-C0AB1F9313C0",
    "Code": "success"
```

#### GetRepoTag

Queries the tag information about a single image.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetRepoTag | The operation that you want to perform. Set the value to GetRepoTag. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the image. |

| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
|---|---|---|---|---|
| RepoId | String | Yes | crr- tquyps22md8p* *** | The ID of the repository. |
| Tag | String | Yes | 1.0 | The tag of the repository. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | NORMAL | The status of the image. Valid values: NORMAL : The image is normal. DELETING : The image is being deleted. |
| ImageCreate | Long | 1572839125000 | The time when the image was created. |
| ImageSize | Long | 27107966 | The size of the image. |
| RequestId | String | 031572FA-7D8F- 4C05-B790- 1071E0E05DE6 | The ID of the request. |
| Digest | String | 67bfbcc12b67936e c7f867927817cbb0 71832b873dbcaed 312a1930ba5f1*** * | The digest of the image. |
| Code | String | success | The return value. |
| ImageUpdate | Long | 1572875608000 | The time when the image was last updated. |
| Tag | String | 1.0 | The tag of the image. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| ImageId | String | 45023655bf39c382 e26a8607d057c27 871dee163c1ecf48 cc1ebf2a1**** | The ID of the image. |

Sample requests

```
http(s)://[Endpoint]/?Action=GetRepoTag &InstanceId=cri-pri**** &RepoId=crr-tquyps22md8p**** &Tag=1.0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <GetRepoTagResponse>
    <Status>NORMAL</Status>
    <ImageCreate>1572839125000</ImageCreate>
    <ImageSize>27107966</ImageSize>
    <RequestId>031572FA-7D8F-4C05-B790-1071E0E05DE6</RequestId>
    <Digest>67bfbcc12b67936ec7f867927817cbb071832b873dbcaed312a1930ba5f1****</Digest>
    <Code>success</Code>
    <ImageUpdate>1572875608000</ImageUpdate>
    <Tag>1.0</Tag>
    <IsSuccess>true</IsSuccess>
    <ImageId>45023655bf39c382e26a8607d057c27871dee163c1ecf48cc1ebf2a1****</ImageId>
</GetRepoTagResponse>
```

`JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json
  "Status" : "NORMAL",
  "ImageCreate" : 1572839125000,
  "ImageSize" : 27107966,
  "RequestId" : "031572FA-7D8F-4C05-B790-1071E0E05DE6",
  "Digest" : "67bfbcc12b67936ec7f867927817cbb071832b873dbcaed312a1930ba5f1****",
  "Code" : "success",
  "ImageUpdate" : 1572875608000,
  "Tag" : 1,
  "IsSuccess" : true,
  "ImageId" : "45023655bf39c382e26a8607d057c27871dee163c1ecf48cc1ebf2a1****"
```

#### GetRepoTagLayers

Queries the information about image layers of an image that is corresponding to a tag.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetRepoTagLay ers | The operation that you want to perform. Set the value to GetRepoTagLayers. |
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the instance. |
| RepoId | String | Yes | crr- kwgb20p8wwmh **** | The ID of the repository. |
| Tag | String | Yes | master | The tag of the image. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| Layers | Array of Layers |   | The information about image layers. |
| BlobDigest | String | sha256:36fb85fcb5 e919cb60e782397 a6be04201868fe7 b38ef7669fc01cae c1c8fc4e | The digest of the blob. |
| BlobSize | Long | 23655489 | The size of the blob. |
| LayerCMD | String | /usr/bin/virtual- kubelet /usr/bin/virtual- kubelet # buildkit | The command used to create the image layer. |
| LayerIndex | Integer | 0 | The index of the image layer. |
| LayerInstructio n | String | COPY | The instruction used to create the image layer. |

| RequestId | String | D39D7151-0299- 47E3-B948- E49E1EA8D406 | The ID of the request. |
|---|---|---|---|

Sample requests

```
http(s)://[Endpoint]/?Action=GetRepoTagLayers &InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-kwgb20p8wwmh**** &Tag=master &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>D39D7151-0299-47E3-B948-E49E1EA8D406</RequestId> <Layers> <BlobDigest>sha256:36fb85fcb5e919cb60e782397a6be04201868fe7b38ef7669fc01caec1c8fc4e</Blob gest>
    <LayerInstruction>COPY</LayerInstruction>
    <BlobSize>23655489</BlobSize>
    <LayerCMD>/usr/bin/virtual-kubelet /usr/bin/virtual-kubelet # buildkit</LayerCMD>
    <LayerIndex>0</LayerIndex>
</Layers> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess":true,
    "RequestId":"D39D7151-0299-47E3-B948-E49E1EA8D406",
    "Layers":[
"BlobDigest":"sha256:36fb85fcb5e919cb60e782397a6be04201868fe7b38ef7669fc01caec1c8fc4e",
            "LayerInstruction":"COPY",
            "BlobSize":23655489,
            "LayerCMD":"/usr/bin/virtual-kubelet /usr/bin/virtual-kubelet # buildkit",
            "LayerIndex":0
```

`],`

```json
    "Code":"success"
```

#### GetRepoTagManifest

Queries the manifest information of an image tag.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetRepoTagMan ifest | The operation that you want to perform. Set the value to GetRepoTagManifest. |
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the instance. |
| RepoId | String | Yes | crr- kwgb20p8wwmh **** | The ID of the repository. |
| Tag | String | Yes | master | The tag of the image. |
| SchemaVersion | Integer | No | 2 | The schema version of the manifest. Valid values: 1 and 2. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| Manifest | Struct |   | The information about the image manifest. |
| Architecture | String | null | The architecture of the image manifest. |
| Config | Struct |   | The configuration information. |
| Digest | String | sha256:b5b2b2c50 7a0944348e03031 14d8d93aaaa0817 32b86451d9bce1f4 32a537bc7 | The digest of the image. |

| MediaType | String | application/vnd.doc ker.container.imag e.v1+json | The MIME type of the configuration file. |
|---|---|---|---|
| Size | Long | 7023 | Size. |
| FsLayers | Array of FsLayers |   | A list of filesystem layer blob sums contained in this image. |
| BlobSum | String | null | The digest of the referenced filesystem image layer. |
| History | Array of History |   | A list of unstructured historical data for V1 compatibility. |
| V1Compatibilit y | Map | null | The raw V1 compatibility information. |
| Layers | Array of Layers |   | The information about image layers. |
| Digest | String | sha256:e692418e4 cbaf90ca69d05a66 403747baa33ee08 806650b51fab815 ad7fc331f | The digest of the image. |
| MediaType | String | application/vnd.doc ker.image.rootfs.di ff.tar.gzip | The MIME type of the configuration file. |
| Size | Long | 32654 | Size. |
| MediaType | String | application/vnd.doc ker.distribution.ma nifest.v2+json | The MIME type of the configuration file. |
| Name | String | null | Name. |
| SchemaVersio n | Integer | 2 | The schema version of the manifest. |
| Signatures | Array of Signatures |   | The information about signatures. |
| Header | Map | null | The header information of the signature. |
| Protected | String | null | The signed protected header. |
| Signature | String | null | The signature for the image manifest. |

| Tag | String | master | The tag of the image. |
|---|---|---|---|
| RequestId | String | D39D7151-0299- 47E3-B948- E49E1EA8D406 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=GetRepoTagManifest &InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-kwgb20p8wwmh**** &Tag=master &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>D39D7151-0299-47E3-B948-E49E1EA8D406</RequestId> <Manifest>
    <Architecture>null</Architecture>
    <SchemaVersion>2</SchemaVersion>
    <MediaType>application/vnd.docker.distribution.manifest.v2+json</MediaType>
    <Tag>master</Tag>
    <Name>null</Name>
    <FsLayers>
        <BlobSum>null</BlobSum>
    </FsLayers>
    <History>
        <V1Compatibility>null</V1Compatibility>
    </History>
    <Signatures>
        <Protected>null</Protected>
        <Header>null</Header>
        <Signature>null</Signature>
    </Signatures>
    <Layers>
<Digest>sha256:e692418e4cbaf90ca69d05a66403747baa33ee08806650b51fab815ad7fc331f</Digest>
        <Size>32654</Size>
        <MediaType>application/vnd.docker.image.rootfs.diff.tar.gzip</MediaType>
    </Layers>
    <Config>
<Digest>sha256:b5b2b2c507a0944348e0303114d8d93aaaa081732b86451d9bce1f432a537bc7</Digest>
        <Size>7023</Size>
        <MediaType>application/vnd.docker.container.image.v1+json</MediaType>
    </Config>
</Manifest> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess": true,
    "RequestId": "D39D7151-0299-47E3-B948-E49E1EA8D406",
    "Manifest": {
        "Architecture": "null",
        "SchemaVersion": 2,
        "MediaType": "application/vnd.docker.distribution.manifest.v2+json",
        "Tag": "master",
        "Name": "null",
        "FsLayers": {
            "BlobSum": "null"
```

`},`

```json
        "History": {
            "V1Compatibility": "null"
```

`},`

```json
        "Signatures": {
            "Protected": "null",
            "Header": "null",
            "Signature": "null"
```

`},`

```json
        "Layers": {
            "Digest":
"sha256:e692418e4cbaf90ca69d05a66403747baa33ee08806650b51fab815ad7fc331f",
            "Size": 32654,
            "MediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip"
```

`},`

```json
        "Config": {
            "Digest":
"sha256:b5b2b2c507a0944348e0303114d8d93aaaa081732b86451d9bce1f432a537bc7",
            "Size": 7023,
            "MediaType": "application/vnd.docker.container.image.v1+json"
```

`},`

```json
    "Code": "success"
```

#### CreateRepoTag

Creates an image tag based on an existing image tag in an image repository.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRepoTag | The operation that you want to perform. Set the value to CreateRepoTag. |
| FromTag | String | Yes | v1 | The source image tag. |

| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
|---|---|---|---|---|
| NamespaceNam e | String | Yes | ns | The name of the namespace. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the instance. |
| RepoName | String | Yes | repo1 | The name of the image repository. |
| ToTag | String | Yes | v2 | The image tag that you want to create. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The response code. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| RequestId | String | C4C7DD0C-C9D6- 437A-A7EE- 8BY***** | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=CreateRepoTag &FromTag=v1 &InstanceId=cri-pri**** &NamespaceName=ns &RegionId=cn-wl-en**** &RepoName=repo1 &ToTag=v2 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>C4C7DD0C-C9D6-437A-A7EE-8BY*****</RequestId> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess": true,
    "RequestId": "C4C7DD0C-C9D6-437A-A7EE-8BY*****",
    "Code": "success"
```

### Trigger management

#### UpdateRepoTrigger

Updates a trigger for a repository.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateRepoTrig ger | The operation that you want to perform. Set the value to UpdateRepoTrigger. |
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the instance. |
| RepoId | String | Yes | crr- tquyps22md8p* *** | The ID of the image repository. |
| TriggerId | String | Yes | crw- k7bdx4kt52ty*** * | The ID of the trigger. |
| TriggerName | String | No | test trigger _ | The name of the trigger. |
| TriggerUrl | String | No | https://www.test. com | The URL of the trigger. |

| TriggerType | String | No | TAG LIST _ | The type of the trigger. Valid values: ALL : a trigger that supports both tags and regular expressions. The system triggers image pulls if an image is built successfully. TAG LISTTAG : a tag-based _ trigger. The system triggers image pulls only if images with one of the specified tags are built successfully. TAG REG EXP : a regular _ _ expression-based trigger. Tags of newly-built images are filtered based on a regular expression. The system triggers image pulls only if images whose tags meet the regular expression are built successfully. |
|---|---|---|---|---|
| TriggerTag | String | No | master | The image tag based on which the trigger is set. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| RequestId | String | 32535049-ED91- 4589-98C0- 7C88766EDF1F | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateRepoTrigger &InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-tquyps22md8p**** &TriggerId=crw-k7bdx4kt52ty**** &TriggerName=test_trigger &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>32535049-ED91-4589-98C0-7C88766EDF1F</RequestId> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess":true,
    "RequestId":"32535049-ED91-4589-98C0-7C88766EDF1F",
    "Code":"success"
```

#### ListRepoTrigger

Queries the triggers of a repository.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListRepoTrigger | The operation that you want to perform. Set the value to ListRepoTrigger. |
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the instance. |
| RepoId | String | Yes | crr- tquyps22md8p* *** | The ID of the image repository. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| RequestId | String | 2CA76D52-A8F0- 4D0B-854E- FBD9F6C99049 | The ID of the request. |

| Triggers | Array of Triggers |   | The triggers of the repository. |
|---|---|---|---|
| RepoEvent | String | BUILD SUCCESS _ | The type of the event that activates the trigger. Valid values: BUILD SUCCESS : The trigger is _ activated when the build is successful. BUILD Fail : The trigger is activated _ when the build fails. |
| TriggerId | String | crw- vriyql9eq7ep**** | The ID of the trigger. |
| TriggerName | String | test | The name of the trigger. |
| TriggerTag | String | * | The image tag based on which the trigger is set. |
| TriggerType | String | ALL | The type of the trigger. Valid values: ALL : a trigger that supports both tags and regular expressions. TAG LISTTAG : a tag-based trigger. _ TAG REG EXP : a regular expression- _ _ based trigger. |
| TriggerUrl | String | https://www.test.co m | The URL of the trigger. |

Sample requests

```
http(s)://[Endpoint]/?Action=ListRepoTrigger &InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-tquyps22md8p**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>2CA76D52-A8F0-4D0B-854E-FBD9F6C99049</RequestId> <Triggers>
    <TriggerUrl>https://www.test.com</TriggerUrl>
    <TriggerType>ALL</TriggerType>
    <RepoEvent>BUILD_SUCCESS</RepoEvent>
    <TriggerName>test</TriggerName>
    <TriggerTag>*</TriggerTag>
    <TriggerId>crw-vriyql9eq7ep****</TriggerId>
</Triggers> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess": true,
    "RequestId": "2CA76D52-A8F0-4D0B-854E-FBD9F6C99049",
    "Triggers": {
        "TriggerUrl": "https://www.test.com",
        "TriggerType": "ALL",
        "RepoEvent": "BUILD_SUCCESS",
        "TriggerName": "test",
        "TriggerTag": "*",
        "TriggerId": "crw-vriyql9eq7ep****"
```

`},`

```json
    "Code": "success"
```

#### CreateRepoTrigger

Creates a trigger for a repository.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRepoTrigg er | The operation that you want to perform. Set the value to CreateRepoTrigger . |
| InstanceId | String | Yes | cri-pri**** | The ID of the Container Registry Enterprise Edition instance. |
| RegionId | String | Yes | cn-wl-en**** | The region ID of the instance. |
| RepoId | String | Yes | crr- xwvi3osiy4ff**** | The ID of the image repository. |

| TriggerName | String | Yes | trigger1 | The name of the trigger. |
|---|---|---|---|---|
| TriggerTag | String | Yes | [1] | The image tag based on which the trigger is set. Note If TriggerType is set to ALL , TriggerTag can be set to a string or an array, for example, * . If TriggerType is set to TAG LIST , _ TriggerTag must be set to an array, for example, [1] . If TriggerType is set to TAG REG EXP , _ _ TriggerTag must be set to a string, for example, * . |
| TriggerType | String | Yes | ALL | The type of the trigger. Valid values: ALL : a trigger that supports both tags and regular expressions. TAG LIST : a tag-based trigger. _ TAG REG EXP : a regular _ _ expression-based trigger. |
| TriggerUrl | String | Yes | http://www.mysit e.com | The URL of the trigger. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : The request is successful. false : The request fails. |
| RequestId | String | B79F5E0E-8770- 407D-BCB6- ECF4BA9C**** | The ID of the request. |

| TriggerId | String | crw- 0z4pf81pgz35**** | The ID of the trigger. |
|---|---|---|---|

Sample requests

```
http(s)://[Endpoint]/?Action=CreateRepoTrigger &InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-xwvi3osiy4ff**** &TriggerName=trigger1 &TriggerTag=[1] &TriggerType=ALL &TriggerUrl=http://www.mysite.com &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>B79F5E0E-8770-407D-BCB6-ECF4BA9C****</RequestId> <TriggerId>crw-0z4pf81pgz35****</TriggerId> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess": true,
    "RequestId": "B79F5E0E-8770-407D-BCB6-ECF4BA9C****",
    "TriggerId": "crw-0z4pf81pgz35****",
    "Code": "success"
```

#### DeleteRepoTrigger

Deletes a trigger of an image repository.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteRepoTrigg er | The operation that you want to perform. Set the value to DeleteRepoTrigger. |
| InstanceId | String | Yes | cri-pri**** | The ID of the instance. |

| RegionId | String | Yes | cn-wl-en**** | The ID of the region. |
|---|---|---|---|---|
| RepoId | String | Yes | crr- xwvi3osiy4ff**** | The ID of the image repository. |
| TriggerId | String | Yes | crw- 0z4pf81pgz35** ** | The ID of the trigger that you want to delete. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : successful false : failed |
| RequestId | String | 85180AE4-9A57- 48F8-9EF9- 68ECCE54B552 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteRepoTrigger &InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-xwvi3osiy4ff**** &TriggerId=crw-0z4pf81pgz35**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>85180AE4-9A57-48F8-9EF9-68ECCE54B552</RequestId> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess":true,
    "RequestId":"85180AE4-9A57-48F8-9EF9-68ECCE54B552",
    "Code":"success"
```

### Access credential

**management**

#### GetAuthorizationToken

Obtains the temporary account and token that you use to log on to a Container Registry instance. The returned token is valid for one hour. If you request for the token by using Security Token Service (STS), the returned token is valid within the validity period of the STS token. Take note of the following items when you log on to Container Registry instances by using an STS token: If the STS token belongs to an Alibaba Cloud account, you can use the STS token to log on to all Container Registry instances that belong to the Alibaba Cloud account. If the STS token belongs to a RAM user, you can use the STS token to log on to all Container Registry instances that belong to the RAM user. You can use an STS token to access only Container Registry instances to which the STS token is scoped.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetAuthorizatio nToken | The operation that you want to perform. Set the value to GetAuthorizationToken. |
| InstanceId | String | Yes | cri-pri**** | The ID of the instance. |
| RegionId | String | Yes | cn-wl-en**** | The ID of the region. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AuthorizationT oken | String | shaunadadakks:uu czxnjcyeyhdjadkkaj sjd**** | The token that is returned. |
| Code | String | success | The return value. |
| ExpireTime | Long | 1571242083000 | The timestamp when the token expires. Unit: milliseconds. |

| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : successful false : failed |
|---|---|---|---|
| RequestId | String | E069EB86-E6AD- 4A98-ADDE- 0E993390239A | The ID of the request. |
| TempUsernam e | String | temp user cr _ _ | The username that is used to log on to the instance. |

Sample requests

```
http(s)://[Endpoint]/?Action=GetAuthorizationToken &InstanceId=cri-pri**** &RegionId=cn-wl-en**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <AuthorizationToken>shaunadadakks:uuczxnjcyeyhdjadkkajsjd****</AuthorizationToken> <TempUsername>temp_user_cr</TempUsername> <RequestId>E069EB86-E6AD-4A98-ADDE-0E993390239A</RequestId> <ExpireTime>1571242083000</ExpireTime> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess": true,
    "AuthorizationToken": "shaunadadakks:uuczxnjcyeyhdjadkkajsjd****",
    "TempUsername": "temp_user_cr",
    "RequestId": "E069EB86-E6AD-4A98-ADDE-0E993390239A",
    "ExpireTime": 1571242083000,
    "Code": "success"
```

#### ResetLoginPassword

Resets the logon password of a Container Registry instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | ResetLoginPass word | The operation that you want to perform. Set the value to ResetLoginPassword. |
|---|---|---|---|---|
| InstanceId | String | Yes | cri-pri**** | The ID of the instance. |
| Password | String | Yes | test | The new logon password. |
| RegionId | String | Yes | cn-wl-en**** | The ID of the region. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return value. |
| IsSuccess | Boolean | true | Indicates whether the API call is successful. Valid values: true : successful false : failed |
| RequestId | String | EB9C5722-51E2- 4497-A573- 575B0CA5CE0C | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=ResetLoginPassword &InstanceId=cri-pri**** &Password=test &RegionId=cn-wl-en**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<IsSuccess>true</IsSuccess> <RequestId>EB9C5722-51E2-4497-A573-575B0CA5CE0C</RequestId> <Code>success</Code>
```

`JSON` format

```json
    "IsSuccess":true,
    "RequestId":"EB9C5722-51E2-4497-A573-575B0CA5CE0C",
    "Code":"success"
```

### Artifact build

#### CreateArtifactBuildTask

Creates an artifact build task in Container Registry.

**Request headers**

This operation uses common request headers and does not have any special request headers. For more information, see Common parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wl-en**** |   | The region ID. |   |   |
| InstanceId | Strin g | Quer y | Yes | cri-pri**** |   | The instance ID. |   |   |
| ArtifactBuil dType | Strin g | Quer y | Yes | IMAGE TO ACCELERATED _ _ IMAGE _ |   | The type of artifact to build. The following value is supported: IMAGE TO ACCELERATE _ _ D IMAGE : Creates an _ accelerated image that is optimized for ACK scenarios. |   |   |
|   |   |   |   |   |   |   | IMAGE TO ACCELERATE _ _ |   |
|   |   |   |   |   |   | D IMAGE _ |   |   |
| SourceArtif act | Json | Quer y | Yes | { \"repoId\" : \"crr- 1rgqu9n2e****\", \"version\": \"test\", \"artifactType\": \"IMAGE\" } |   | The source artifact. |   |   |

| TargetArtif act | Json | Quer y | Yes | { \"repoId\" : \"crr- 1rgqu9n2e****\", \"version\": \"test accelerated\", _ \"artifactType\": \"ACCELERATED IMAGE\" _ } | The target artifact. |
|---|---|---|---|---|---|
| Instruction s | Repe atLis t | Quer y | No | [] | Additional build instructions. |
| Parameter s | Map | Quer y | No | {} | Additional parameters. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return code. |
| IsSuccess | Boolean | true | Indicates whether the request was successful. |
| RequestId | String | RQ1234567890abc def | 1234567890 |
| BuildTaskId | String | i2ai-1yu**** | The ID of the artifact build task. |

Request example

```
http(s)://[Endpoint]/?Action=CreateArtifactBuildTask &RegionId=cn-wl-en**** &InstanceId=cri-pri**** &ArtifactBuildType=IMAGE_TO_ACCELERATED_IMAGE &SourceArtifact={<br/> \"repoId\" : \"crr-1rgqu9n2e****\",<br/> \"version\": \"test\",<br/> \"artifactType\": \"IMAGE\"<br/>} &TargetArtifact={<br/> \"repoId\" : \"crr-1rgqu9n2e****\",<br/> \"version\": \"test_accelerated\",<br/> \"artifactType\": \"ACCELERATED_IMAGE\"<br/>} &<Common request parameters> <br/><br/><br/><br/><br/><br/><br/><br/>
```

Successful response example `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json
 "IsSuccess":true,
 "RequestId":"RQ1234567890abcdef",
 "BuildTaskId":"i2a-1yu****",
 "Code":"0"
```

#### CreateArtifactBuildRule

Creates an accelerated image build rule for an image repository.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wl-en**** | The region ID. |
| InstanceId | Strin g | Query | Yes | cri-pri**** | The instance ID. |
| ScopeTyp e | Strin g | Query | Yes | REPOSITORY | The scope of the rule. Valid value: REPOSITORY : The rule applies to a repository. |
| ScopeId | Strin g | Query | Yes | crr-pmajihou6cg0**** | The ID of the scope. Valid value: ScopeId to the ID of the image repository. |
| ArtifactTy pe | Strin g | Query | Yes | ACCELERATED IMAGE _ | The type of the accelerated image. Valid value: ACCELERATED IMAGE _ : Generates an accelerated image. |
| Parameter s | Map | Query | No | {} | Additional parameters. |

|   |   | ACCELERATED IMAGE _ |
|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return code. |
| IsSuccess | Boolean | true | Indicates whether the request was successful. |
| RequestId | String | RQ1234567890abc def | 1234567890 |
| BuildRuleId | String | crabr- ly77w5i3t31f**** | The build rule ID. |

Request example

```
http(s)://[Endpoint]/?Action=CreateArtifactBuildRule &RegionId=cn-wl-en**** &InstanceId=cri-pri**** &ScopeType=REPOSITORY &ScopeId=crr-pmajihou6cg0**** &ArtifactType=ACCELERATED_IMAGE &<Common request parameters>
```

Response example `JSON` format

```json
 "IsSuccess":true,
 "BuildRuleId":"crbr-ly77w5i3t31f****",
 "RequestId":"RQ1234567890abcdef",
 "Code":"0"
```

#### GetArtifactBuildTask

Retrieves the details of an artifact build task in Container Registry.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|

| RegionId | Strin g | Host | Yes | cn-wl-en**** | The region ID. |
|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | Yes | cri-pri**** | The instance ID. |
| BuildTaskI d | Strin g | Quer y | Yes | i2ai-1yu**** | The artifact build task ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Instructions | String | [] | Additional build instructions. |
| EndTime | Integer | 2019-11- 30T05:40:00Z | The time when the task ended. |
| StartTime | Integer | 2019-11- 30T04:00:00Z | The time when the task started. |
| EstimateTime | Integer | 5000 | The estimated time to complete the task. Unit: milliseconds. |
| ArtifactBuildTy pe | String | IMAGE TO ACCELE _ _ RATED IMAGE _ | The type of the artifact build. The following value is supported: IMAGE TO ACCELERATED IMAGE : _ _ _ Creates an accelerated image for ACK. |
| RequestId | String | RQ1234567890abc def | The request ID. |
| TaskStatus | String | PENDING | The status of the task. PENDING indicates that the task is waiting to be executed. RUNNING indicates that the task is in progress. COMPLETED indicates that the task is complete. FAILED indicates that the task failed. |
| BuildTaskId | String | i2a-1yu**** | The artifact build task ID. |
| Code | String | success | The return code. |

| IsSuccess | Boolean | true | Indicates whether the request was successful. |
|---|---|---|---|
| SourceArtifact | Struct | exampleValue | The source artifact. |
| -RepoId | String | 1234567890 | The repository ID. |
| -Version | String | 1 | The version number. |
| -ArtifactType | String | EcsImage | The artifact type. |
| TargetArtifact | Struct | example.jar | The destination artifact. |
| -RepoId | String | 1234567890 | The repository ID. |
| -Version | String | 1 | The version number. |
| -ArtifactType | String | EcsImage | The artifact type. |

Sample request

```
http(s)://[Endpoint]/?Action=GetArtifactBuildTask &RegionId=cn-wl-en**** &InstanceId=cri-pri**** &BuildTaskId=i2a-1yu**** &<Common request parameters>
```

Sample response `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json
 "TargetArtifact":{
  "Version":"1",
  "ArtifactType":"EcsImage",
  "RepoId":"1234567890"
```

`},`

```json
 "ArtifactBuildType":"IMAGE_TO_ACCELERATED_IMAGE",
 "IsSuccess":true,
 "EndTime":2022,
 "RequestId":"RQ1234567890abcdef",
 "BuildTaskId":"i2a-1yu****",
 "StartTime":2022,
 "EstimateTime":5000,
 "Instructions":"",
 "TaskStatus":"PENDING",
 "Code":"0",
 "SourceArtifact":{
  "Version":"1",
  "ArtifactType":"EcsImage",
  "RepoId":"1234567890"
```

#### ListArtifactBuildTask

Retrieves a list of artifact build tasks.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wl-en**** | The region ID. |
| InstanceId | Strin g | Quer y | Yes | cri-pri**** | The instance ID. |
| PageNo | Integ er | Quer y | No | 1 | The page number. |

| PageSize | Integ er | Quer y | No | 10 | The number of entries to return on each page. The maximum value is 100. If you specify a value greater than 100, the system reports a parameter error or returns a maximum of 100 entries. |
|---|---|---|---|---|---|
| ArtifactBuil dType | Strin g | Quer y | No | ACCELERATED IMAGE _ | The type of the accelerated image. Valid value: ACCELERATED IMAGE _ : generates an accelerated image. |
| SourceArtif actRepoId | Strin g | Quer y | No | crr-1rgqu9n2e**** | The ID of the source artifact repository. |
| DestArtifac tRepoId | Strin g | Quer y | No | crr-1rgqu9n2e**** | The ID of the destination artifact repository. |

|   |   | ACCELERATED IMAGE _ |
|---|---|---|
| TED IMAGE _ |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ArtifactBuildTa sk | Array | [] | The list of artifact build tasks. |
| -Instructions | String | [] | The additional build instructions. |
| -SourceArtifact | Array | [] | The source artifact. |
| --RepoId | String | crr- gzsrlevmvoaq**** | The repository ID. |
| --Version | String | 1 | The version number. |
| --ArtifactType | String | IMAGE | The artifact type. |
| -EndTime | Integer | 2209702074010 | The time when the task ended. |

| -StartTime | Integer | 2209702074000 | The time when the task started. |
|---|---|---|---|
| -EstimateTime | Integer | 5000 | The estimated duration of the build task. |
| - ArtifactBuildTy pe | String | IMAGE TO ACCELE _ _ RATED IMAGE _ | The type of the artifact build. Valid value: IMAGE TO ACCELERATED IMAGE : _ _ _ creates an accelerated image that is optimized for ACK. |
| -TaskStatus | String | SUCCESS | The status of the task. For example, `PENDING` means the task is waiting to be executed, `RUNNING` means the task is in progress, `COMPLETED` means the task is finished, and `FAILED` means the task failed. |
| -BuildTaskId | String | i2ai--1yu**** | The ID of the artifact build task. |
| -TargetArtifact | Struct | {} | Target Artifact |
| --RepoId | String | crr- gzsrlevmvoaq**** | The repository ID. |
| --Version | String | 1 accelerated _ | The version number. |
| --ArtifactType | String | ACCELERATED IMA _ GE | The artifact type. |
| Code | String | success | The return code. |
| IsSuccess | Boolean | true | Indicates whether the API call was successful. Valid values: true : The API call was successful. false : The API call failed. |
| RequestId | String | C4C7DD0C-C9D6- 437A-A7EE- 121EFD70D002 | The request ID. |
| TotalCount | Integer | 200 | The total number of entries. |
| PageNo | Integer | 1 | The page number. |

| PageSize | Integer | 10 | The number of entries returned per page. |
|---|---|---|---|

#### GetArtifactBuildRule

Retrieves a build rule for accelerated images in an image repository.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wl-en**** | The region ID. |
| InstanceId | Strin g | Quer y | Yes | cri-pri**** | The instance ID. |
| ScopeType | Strin g | Quer y | No | REPOSITORY | The scope of the rule. Valid value: REPOSITORY : The rule applies to a specific repository. |
| ScopeId | Strin g | Quer y | No | crr-pmajihou6cg0**** | The ID of the object to which the rule applies. Valid value: ScopeId to the ID of the image repository. |
| ArtifactTyp e | Strin g | Quer y | No | ACCELERATED IMAGE _ | The type of artifact. Valid value: ACCELERATED IMAGE _ : An accelerated image. |
| BuildRuleI d | Strin g | Quer y | No | crabr-ly77w5i3t31f**** | The build rule ID. |

|   |   | ACCELERATED IMAGE _ |
|---|---|---|
| _ |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | RQ1234567890abc def | The request ID. |
| ScopeId | String | crr- nyrh2oko32xb**** | The ID of the object to which the rule applies. |
| BuildRuleId | String | crabr- ly77w5i3t31f**** | The build rule ID. |
| ArtifactType | String | ACCELERATED IMA _ GE | The artifact type. |
| ScopeType | String | REPOSITORY | The scope of the rule. |
| Code | String | success | The return code. |
| IsSuccess | Boolean | true | Indicates whether the request was successful. |
| Parameters | Struct | { "Status": { "Description": " (Required) The status of the Ecs instance.", "Type": "String" } } | The parameter information. |
| - ImageIndexOn ly | Boolean | false | Indicates that image data is accessed only by index and does not include other metadata or processing logic. |

Request example

```
http(s)://[Endpoint]/?Action=GetArtifactBuildRule &RegionId=cn-wl-en**** &InstanceId=cri-pri**** &<Common request parameters>
```

Response example `JSON` format

```json
HTTP/1.1 200 OK Content-Type: application/json
 "ScopeType":"REPOSITORY",
 "IsSuccess":true,
 "BuildRuleId":"crbr-ly77w5i3t31f****",
 "Parameters":{
  "ImageIndexOnly":""
```

`},`

```json
 "RequestId":"RQ1234567890abcdef",
 "ArtifactType":"EcsImage",
 "ScopeId":"crr-nyrh2oko32xb****",
 "Code":"0"
```

#### DeleteArtifactBuildRule

Deletes a build rule for accelerated images in an image repository.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | Yes | cn-wl-en**** | The region ID. |
| InstanceId | Strin g | Quer y | Yes | cri-pri**** | The instance ID. |
| BuildRuleI d | Strin g | Quer y | No | crabr-ly77w5i3t31f**** | The build rule ID. |
| ScopeType | Strin g | Quer y | No | REPOSITORY | The scope of the rule. Valid value: REPOSITORY : The rule applies at the repository level. |

| ScopeId | Strin g | Quer y | No | crr-pmajihou6cg0**** | The ID of the scope to which the rule applies. Valid value: ScopeId to the ID of an image repository. |
|---|---|---|---|---|---|
| ArtifactTyp e | Strin g | Quer y | No | ACCELERATED IMAGE _ | The type of the artifact. Valid value: ACCELERATED IMAGE _ : an accelerated image. |

|   |   | ACCELERATED IMAGE _ |
|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | success | The return code. |
| IsSuccess | Boolean | true | Indicates whether the request was successful. |
| RequestId | String | RQ1234567890abc def | The request ID. |

Sample request

```
http(s)://[Endpoint]/?Action=DeleteArtifactBuildRule &RegionId=cn-wl-en**** &InstanceId=cri-pri**** &Common request parameters
```

Sample success response `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json
 "IsSuccess":true,
 "RequestId":"RQ1234567890abcdef",
 "Code":"0"
```

## Appendixes

### STS overview

#### What is STS?

Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and RAM roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed to access Apsara Stack resources by using an issued STS token. When the STS token is issued, you can specify a validity period and access permissions for the STS token.

**Use a RAM user to obtain an STS token**

An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and can use the STS token to access Apsara Stack resources.

**Benefits**

STS tokens help reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify the validity period for STS tokens. After STS tokens expire, they become invalid. Therefore, you do not need to rotate the STS tokens on a regular basis. You can attach custom policies to STS tokens for flexible and fine-grained authorization.

#### AssumeRole

Obtains a Security Token Service (STS) token that is used by a RAM user to assume a RAM role. In this example, an Apsara Stack tenant account is used as the trusted entity of the RAM role.

**Request parameters**

| Parameter | Type | Requ ired | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::123456 789012****:role/ adminrole | The Apsara Stack Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Apsara Stack tenant account. |

| Parameter | Type | Requ ired | Example | Description |
|---|---|---|---|---|
| RoleSessionNa me | String | Yes | alice | The name of the role session. Set this parameter based on your business requirements. In most cases, you can set this parameter to the identity of the user who calls the operation. For example, specify a username. In ActionTrail logs, you can distinguish the users who assume the same RAM role to perform operations based on the value of the RoleSessionName parameter. This way, you can perform user-specific auditing. The name must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resourc e": ["*"]}],"Version":" 1"} | The policy that specifies the permissions of the STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. The policy must be 1 to 1,024 characters in length. |

**Responses**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | The ID of the request. |
| Credentials | None | None | The access credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuK g5U1**** | The AccessKey ID. |
| AccessKeySecret | String | wyLTSmsyPGP1ohv vw8xYgB29dlGI8KM iH2pK**** | The AccessKey secret. |
| SecurityToken | String | ******** | The security token. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Expiration | String | 2015-04- 09T11:52:19Z | The time when the STS token expires. |
| AssumedRoleUser | None | None | The temporary identity that you use to assume the RAM role. |
| Arn | String | acs:ram::12345678 9012****:role/admi nrole/alice | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495** **:alice | The ID of the temporary identity that you use to assume the RAM role. |

**Add Project Object Model (POM) dependencies**

The Alibaba Cloud core library is required. Perform the following steps to add the Alibaba Cloud core library to POM:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

**Call an API operation to obtain the STS AccessKey 3-tuple.**

In the following sample code, the `Sts::AssumeRole::2015-04-01` operation is used to obtain the 3-tuple.

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
    public static void main(String[] args) {
//CreateandinitialieaDefaltAcsClientinstance
```

```java
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourAccessKeyID>", "<yourAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        // Replace "sts.aliyuns.com" with the actual endpoint of STS. In most cases, th
e endpoint is in the following format: sts-vpc.${global:region}.${global:internet-domai n}.
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        // Replace "<yourRoleSessionName>" with the alias that you specify for the curr
ent role session.
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
        // Replace "<yourRoleArn>" with the actual ARN that you obtained for the RAM ro
le in the preceding step.
        request.putQueryParameter("RoleArn", "<yourRoleArn>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            String assumeRole = response.getData();
            if (StringUtils.isEmpty(assumeRole)) return;
            JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
            JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
            // Obtain the STS AccessKey 3-tuple.
            String stsAK = credentials.getString("AccessKeyId");
            String stsSK = credentials.getString("AccessKeySecret");
            String stsToken = credentials.getString("SecurityToken");
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: "
+ stsToken);
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

**Call examples**

In the following sample code, the `DescribeZones` operation in Elastic Compute Service (ECS) is used.

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; importcomaliyuncsCommonResponse;
```

```java
import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
        // Replace "<yourRegionID>" with the actual region ID.
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the
AccessKey ID and secret in the 3-tuple that you obtained in the preceding step.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccessKey>", "<yourStsAccessKeySecret>");
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
        //Replace "<yourRegionID>" with the actual region ID.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
        // Replace "<yourStsToken>" with the STS token in the 3-tuple that you obtained
in the preceding step.
        request.putQueryParameter("SecurityToken", "<yourStsToken>");
        // Optional. Specify the resource set ID.
        // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
        // Required. Specify the organization ID.
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

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.Role Arn | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.Role SessionName | The parameter RoleSessionName is wrongly formed. | The error message returned because the value of the RoleSessionName parameter is in an invalid format. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| 400 | InvalidParameter.Dura tionSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the DurationSeconds parameter is invalid. The minimum value is 900, and the maximum value is equal to the value of the MaxSessionDuration parameter. |
| 400 | InvalidParameter.Polic yGrammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the policy is invalid. |
| 400 | InvalidParameter.Polic ySize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error occurred. |
