---
title: "Cloud Security Management Center Developer Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 262
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Cloud Security Management Center Developer Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E5%AE%89%E5%85%A8%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Cloud%20Security%20Management%20Center%20Developer%20Guide%2020260701.pdf"
converter: line-classifier (PyMuPDF)
---

# Cloud Security Management Center Developer Guide 20260701

Cloud Security Management Cent

## Preparations

### Log on to OpenAPI Explorer

You can log on to OpenAPI Explorer from the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of a
browser and press the Enter key.
2. Enter your username and password.
Obtain the username and password from an operations administrator.

**Note**

The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click **Log on**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: The first time you log on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Re-enter the username and password as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**.

**Note**

For more information, see the **Bind a virtual MFA device to enable MFA** topic in
**Apsara Uni-manager Management Console User Guide** .
5. In the top navigation bar, choose **Products > Application Services > OpenAPI**
**Explorer**.
Cloud Security Management Cent

### View the information about an

**operation**

When you use a service SDK to call an operation of the service, you must obtain the service name, operation name, and API version. This topic describes how to view the information about an operation.

**Background information**

The operations on the API Directory page are for reference only. For information about how to call operations, see API references of the corresponding services. If the information on the API Directory page is inconsistent with that in the API reference of the corresponding service, the information in the API reference takes precedence.

**Procedure**

1. Log on to OpenAPI Explorer.
2. In the left-side navigation pane, click **API Directory**.
3. On the **API Directory** page, select the required service from the drop-down list, enter a
keyword of an operation name in the search box, and then click Search.
4. View and record the service name, operation name, and API version.

### Obtain an AccessKey pair

Access credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You can use one type of access credential for authentication when you make an API request. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign an access credential for authentication. An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An access credential that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an AccessKey pair assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs to personal accounts and organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain an organization ID, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

Cloud Security Management Cent The AccessKey pair of a personal account is managed and limited by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. Click the profile picture in the upper-right corner of the page and click **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of the personal account.
Cloud Security Management Cent

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
Cloud Security Management Cent

**Note**

You must use the actual values to replace the variables in the following sample code. The angle brackets <> are not retained in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourRoleSessionName>: Replace it with your current session name. In most cases, this variable is set to the identity of the user who make API calls. Example: Username. You can distinguish the users who assume the same RAM role to perform operations based on the value of the `RoleSessionName` variable. This way, you can perform user-specific auditing. The value of this variable must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (_). <yourRoleArn>: Replace it with the Alibaba Cloud Resource Name (ARN) of your RAM role. "sts.aliyuns.com": Replace it with the actual endpoint of STS. Cloud Security Management Cent

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
} private static String callAssumeRole(IAcsClient client) {
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
    }
    return null;
}
```

3. Use the AccessKey pair assigned by STS to call an operation of a cloud service. The
following sample code provides an example on how to use the AccessKey pair assigned by STS to call the `DescribeZones` operation of Elastic Compute Service (ECS): Cloud Security Management Cent

**Note**

You must use the actual values to replace the variables in the following sample code. The angle brackets <> are not retained in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with the actual region ID.Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourStsToken>: Replace it with the security token of the AccessKey pair assigned by STS. <yourResourceGroupID>: Replace it with the actual resource set ID. <yourResourceGroupID>: Replace it with the actual organization ID. Cloud Security Management Cent

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
    }
}
```

### Obtain an endpoint

This topic describes how to obtain the endpoint of an Apsara Stack Security service.

**Background information**

To use the POP gateway to call the API operations of a cloud service, you must specify the endpoint of the cloud service. You can obtain the endpoint from Apsara Stack onsite O&M engineers. You can also perform the following steps to obtain the endpoint.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Resources**.
Cloud Security Management Cent
3. In the left-side navigation pane, click **Product & Cluster O&M**.
4. Enter sas-securityoperationscentercluster in the **Product | Cluster** search box. Then, click
**Cluster Details** in the Actions column.
5. On the **Services** tab, click the name of the service.
6. Click the **yundun-soc** component in the **Components** section. Then, click the
**Registration Variables** tab and enter yundunsoc.pop.endpoint in the search box to obtain
the endpoint of the service.
7. The endpoint of a service is in the following format:

```
${EndpointPre}.${global:region}.${global:internet-domain}
```

Cloud Security Management Cent s

## Call examples

### Call examples for SDK for Java

#### Quick start

This topic describes how to obtain and use Apsara Stack SDK for Java.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained before you can use Apsara Stack SDK for Java. You can view and obtain your AccessKey pair in the Apsara Unimanager Management Console. For more information, see Obtain an AccessKey pair. The endpoint of a service is obtained. For more information, see Obtain an endpoint. Java Development Kit (JDK) 1.8 or later is installed.

**Installation**

If you use Apache Maven to manage a Java project, you need to only import the JAR file of Apsara Stack SDK for Java to the pom.xml file of the project. If you want to use Apsara Stack Security SDK for Java, you must install the core library of Apsara Stack SDK for Java. We recommend that you use V4.5.17 or later of the core library.

**Usage**

To use Apsara Stack SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.

**Note**

|In the following sample code, replace the variables with actual values based on your
business requirements and remove the angle brackets <> from the final code. The following list describes the variables: <your-region-id>: Replace this variable with the region ID. <your-access-key-id>: Replace this variable with your AccessKey ID. <your-access-key-secret>: Replace this variable with your AccessKey secret. <your-endpoint>: Replace this variable with the endpoint of the service. <API-version>: Replace this variable with the version of the API. <your-action>: Replace this variable with the name of the API operation. Cloud Security Management Cent s

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // The ID of the region.
            "<your-access-key-id>",      // The AccessKey ID.
            "<your-access-key-secret>"); // The AccessKey secret.
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the required parameters.
        CommonRequest request = new CommonRequest();
        request.setDomain("<your-endpooint>");// The endpoint of the service.
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
        }
    }
}
```

#### Use SDK

##### Install SDK for Java

This topic describes how to install and use Apsara Stack Security SDK for Java. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK. For more information, visit Alibaba Cloud SDKs. If you want to use Apsara Stack Security SDK for Java, you must install the core library of Apsara Stack SDK for Java. We recommend that you use V4.5.17 or later of the core library. When you install the core library, you must add the following dependency to the pom.xml file. For more information about the specific SDK version, visit Alibaba Cloud SDKs. Cloud Security Management Cent s

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

##### Use CommonRequest

**Note**

If you want to call the API operations of an Apsara Stack service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need to only download the core package. You do not need to download
and install SDKs of Apsara Stack services.
2. Easy to use: You can call the newly released API operations of an Apsara Stack service
without the need to update the SDK for the service.
3. Fast iteration.
Apsara Stack services provide remote procedure call (RPC) and RESTful APIs. The request method of CommonRequest varies based on the style of the API that you want to call. In most cases, an API uses the RPC style if the API operations include the Action parameter. An API uses the RESTful style if the API operations include the PathPattern parameter. All API operations of a service use the same API style. The API of each service supports only one style. If you pass an invalid identifier, another API operation may be called, or the `ApiNotFound` error is returned. If you want to send a CommonRequest request, you must obtain the values of the following parameters. For more information, see Common parameters. Endpoint: the endpoint of the service. Version: the version of the API. The version is in the YYYY-MM-DD format. Operation information: the name of the API operation that you want to call. The APIs of most Apsara Stack services, such as Threat Detection Service, are RPC APIs. If you want to call an RPC API operation, you must obtain the value of the Action parameter, and then specify the value in the `request.ApiName = "<Action>"` format. If you want to call a RESTful API operation of a service, such as Container Service for Kubernetes (ACK), you must obtain the value of the PathPattern parameter, and then specify the RESTful path in the `request.PathPattern = "<PathPattern>"` format.

**Example: Call an RPC API operation**

The following sample code shows how to use CommonRequest to call an API operation of Apsara Stack Security: Cloud Security Management Cent s

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // The ID of the region.
            "<YOUR-ACCESS-KEY-ID>",      // The AccessKey ID.
            "<YOUR-ACCESS-KEY-SECRET>"); // The AccessKey secret.
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the required parameters.
        CommonRequest request = new CommonRequest();
        request.setDomain("<YOUR-ENDPOINT>");// The endpoint of the service.
        request.setVersion("<API-version>");// The version of the API.
        request.setAction("<YOUR-ACTION>");// The name of the API operation.
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
        }
    }
}
```

### Call examples for SDK for

**Python**

#### Quick start

This topic describes how to obtain and use Apsara Stack SDK for Python.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained before you can use Apsara Stack SDK for Python. For more information, see Obtain an AccessKey pair. The endpoint of a service is obtained. For more information, see Obtain an endpoint.

**Installation**

Cloud Security Management Cent s If you use Python 2.x, run the following command to install the core library of Apsara Stack SDK for Python:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library of Apsara Stack SDK for Python:

```
pip3 install aliyun-python-sdk-core-v3
```

**Usage**

To use Apsara Stack SDK for Python, perform the following steps:
1. Create a client instance.
Before you create a client instance, you must obtain a region ID, an AccessKey ID, and an AccessKey secret.
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.

**Note**

|In the following sample code, replace the variables with actual values based on your
business requirements and remove the angle brackets <> from the final code. The following list describes the variables: <your_region_id>: Replace this variable with the region ID. <your_access_key_id>: Replace this variable with your AccessKey ID. <your_access_key_secret>: Replace this variable with your AccessKey secret. <your-endpoint>: Replace this variable with the endpoint of the service. <API-version>: Replace this variable with the version of the API. <your-action>: Replace this variable with the name of the API operation.

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('<your-endpoint>')// The endpoint of the service. request.set_version('<API-version>')// The version of the API. request.set_action_name('<your-action>')// The name of the API operation.
# or:
# request =
CommonRequest(domain='<your-endpoint>', version='<API-version>', action_name='<your-action>') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

Cloud Security Management Cent s

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

**Note**

If you want to call the API operations of an Apsara Stack service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need to only download the core package. You do not need to download
and install SDKs of Apsara Stack services.
2. Easy to use: You can call the newly released API operations of an Apsara Stack service
without the need to update the SDK for the service.
3. Fast iteration.
Apsara Stack services provide remote procedure call (RPC) and RESTful APIs. The request method of CommonRequest varies based on the style of the API that you want to call. In most cases, an API uses the RPC style if the API operations include the Action parameter. An API uses the RESTful style if the API operations include the PathPattern parameter. All API operations of a service use the same API style. The API of each service supports only one style. If you pass an invalid identifier, another API operation may be called, or the `ApiNotFound` error is returned. If you want to send a CommonRequest request, you must obtain the values of the following parameters. For more information, see Common parameters. Endpoint: the endpoint of the service. Version: the version of the API. The version is in the YYYY-MM-DD format. Operation information: the name of the API operation that you want to call. Cloud Security Management Cent s The APIs of most Apsara Stack services, such as Threat Detection Service, are RPC APIs. If you want to call an RPC API operation, you must obtain the value of the Action parameter, and then specify the value in the `request.ApiName = "<Action>"` format. If you want to call a RESTful API operation of a service, such as Container Service for Kubernetes (ACK), you must obtain the value of the PathPattern parameter, and then specify the RESTful path in the `request.PathPattern = "<PathPattern>"` format.

**Example: Call an RPC API operation**

The following sample code provides an example on how to use CommonRequest to call an API operation:

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('<YOUR-ENDPOINT>') //The endpoint of the service. request.set_version('<API-version>') //The version of the API. request.set_action_name('<YOUR-ACTION>')//The name of the API operation.
# or:
# request = CommonRequest(domain='<your-endpoint>', version='<API-version>',
action_name='your-action') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

### Call examples for SDK for Go

#### Quick start

Apsara Stack SDK for Go allows you to access services without complex coding. This topic describes how to obtain and use Apsara Stack SDK for Go.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained before you can use Apsara Stack SDK for Go. You can view and obtain your AccessKey pair in the Apsara Unimanager Management Console. For more information, see Obtain an AccessKey pair. The endpoint of a service is obtained. For more information, see Obtain an endpoint.

**Install the core package of Apsara Stack SDK for Go**

Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core library:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Use Apsara Stack SDK for Go**

To use Apsara Stack SDK for Go, perform the following steps:
1. Initialize a client instance.
Cloud Security Management Cent s
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.

**Note**

|In the following sample code, replace the variables with actual values based on your
business requirements and remove the angle brackets <> from the final code. The following list describes the variables: <your_region_id>: Replace this variable with the region ID. <your_access_key_id>: Replace this variable with your AccessKey ID. <your_access_key_secret>: Replace this variable with your AccessKey secret. <your-endpoint>: Replace this variable with the endpoint of the service. <API-version>: Replace this variable with the version of the API. <your-action>: Replace this variable with the name of the API operation.

```java
package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" "github.com/aliyun/alibaba-cloud-sdk-go/sdk" "fmt"
```

)

```
func main() { client, err := sdk.NewClientWithAccessKey("<your_region_id>", "{your_access_key_id}", "{your_access_key_secret}") if err != nil { panic(err)
 }
:= requests.NewCommonRequest() request.Domain = "<your-endpoint>"// The endpoint of the service. request.Version = "<API-version>"// The version of the API. request.ApiName = "<your-action>"// The name of the API operation. request.QueryParams["PageNumber"] = "1" request.QueryParams["PageSize"] = "30" response, err := client.ProcessCommonRequest(request) if err != nil { panic(err)
 }
fmt.Print(response.GetHttpContentString()) }
```

#### Use SDK

##### Install Go SDK

This topic describes how to install the Go SDK. The Alibaba Cloud Go SDK supports Go 1.7 or later versions. Install the Go SDK manually.
1. Download the source code of the Go SDK from the official site of Apsara Stack.
Cloud Security Management Cent s
2. Extract the package to the directory where the GO_PATH file of the current user resides.

##### Use CommonRequest

**Note**

If you want to call the API operations of an Apsara Stack service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need to only download the core package. You do not need to download
and install SDKs of Apsara Stack services.
2. Easy to use: You can call the newly released API operations of an Apsara Stack service
without the need to update the SDK for the service.
3. Fast iteration.
Apsara Stack services provide remote procedure call (RPC) and RESTful APIs. The request method of CommonRequest varies based on the style of the API that you want to call. In most cases, an API uses the RPC style if the API operations include the Action parameter. An API uses the RESTful style if the API operations include the PathPattern parameter. All API operations of a service use the same API style. The API of each service supports only one style. If you pass an invalid identifier, another API operation may be called, or the `ApiNotFound` error is returned. If you want to send a CommonRequest request, you must obtain the values of the following parameters. For more information, see Common parameters. Endpoint: the endpoint of the service. Version: the version of the API. The version is in the YYYY-MM-DD format. Operation information: the name of the API operation that you want to call. The APIs of most Apsara Stack services, such as Threat Detection Service, are RPC APIs. If you want to call an RPC API operation, you must obtain the value of the Action parameter, and then specify the value in the `request.ApiName = "<Action>"` format. If you want to call a RESTful API operation of a service, such as Container Service for Kubernetes (ACK), you must obtain the value of the PathPattern parameter, and then specify the RESTful path in the `request.PathPattern = "<PathPattern>"` format.

**Example: Call an RPC API operation**

The following sample code provides an example on how to use CommonRequest to call an API operation: Cloud Security Management Cent s

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "fmt"
```

)

```
func main() {
    client, err := sdk.NewClientWithAccessKey("cn-hangzhou", "{your_access_key_id}", "{
your_access_key_secret}")
    if err != nil {
        panic(err)
    }
    request := requests.NewCommonRequest()
    request.Domain = "<YOUR-ENDPOINT>"// The endpoint of the service.
    request.Version = "<API-version>"// The version of the API.
    request.ApiName = "<YOUR-ACTION>"// The name of the API operation.
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Format | Strin g | No | The type of the returned value. Set the value to JSON. |
| Version | Strin g | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Valid values: 2018-01-16: Auditprivate 2019-07-23: yundunnextsoc 2018-12-03: Sas 2016-11-11: aegis 2021-10-11: yundun-css 2019-08-05: secspy 2018-01-16: Ddosprivate 2018-06-30: hsm-private 2017-12-07: Cloudfw 2019-01-03: Sddp 2020-07-01: semawaf 2018-12-03: soar |
| AccessKeyId | Strin g | Yes | The AccessKey ID that is provided by Apsara Stack. |
| AccessKeySe cret | Strin g | Yes | The AccessKey secret that is provided by Apsara Stack. |
| RegionId | Strin g | Yes | The region ID of the service. |

Cloud Security Management Cent

## Common parameters

**Common request parameters**

Common request parameters must be included in all Apsara Stack Security API requests. Table 1. Common request parameters

| Product | Strin g | Yes | The name of the service to which the operation belongs. Valid values: Auditprivate: basic components of Apsara Stack Security yundunnextsoc: Security Operations Center (SOC) Sas: Threat Detection Service aegis: Server Guard yundun-css: Container Protection secspy: Network Detection and Response Ddosprivate: Anti-DDoS Service hsm-private: Data Encryption Service Cloudfw: Cloud Firewall Sddp: Sensitive Data Discovery and Protection (SDDP) semawaf: Web Application Firewall (WAF) soar: Security Orchestration and Automation Response (SOAR) |
|---|---|---|---|
| EndpointPre | Strin g | Yes | The prefix in the endpoint of the service to which the operation belongs. Valid values: auditprivate: the prefix in the endpoint of basic components of Apsara Stack Security yundunnextsoc-pop: the prefix in the endpoint of SOC tds: the prefix in the endpoint of Threat Detection Service aegis: the prefix in the endpoint of Server Guard yundun-css: the prefix in the endpoint of Container Protection secspy-share: the prefix in the endpoint of Network Detection and Response ddosprivate: the prefix in the endpoint of Anti-DDoS Service hsmprivate: the prefix in the endpoint of Data Encryption Service cloudfw: the prefix in the endpoint of Cloud Firewall sddp-api: the prefix in the endpoint of SDDP semawaf: the prefix in the endpoint of WAF soar: the prefix in the endpoint of SOAR |

Cloud Security Management Cent

**Common response parameters**

API responses use the HTTP response format: A 2xx status code indicates a successful call. A 4xx or 5xx status code indicates a failed call. Responses are returned in the JSON format. Every response returns a unique RequestID regardless of whether the call is successful.

| Parameter | Description |
|---|---|
| Endpoint | http://yundunnewsoc-pop.[RegionId].example.com/? |
| Operation-specific parameters | Action=GetEcsProtectCount |

Cloud Security Management Cent

## Security Operations Center

### Request method

#### Request syntax

**Description**

where: `endpoint` : the endpoint of the Security Operations Center (SOC) API is `yundunnewsoc-pop.`

```
[ RegionId].example.com .
```

**Note**

`Action` : the name of the operation being performed. For example, if `Action=GetEcsProtectCount` ,You can call this operation to query the number of ECS instances with an online Server Guard agent and the number of ECS instances with an offline agent.

#### Request signature

Alibaba Cloud Security authenticates every access request. You must include a signature in each request that you send over the HTTP or HTTPS protocol. To ensure the security of API calls, Alibaba Cloud authenticates each API request using a signature. If you manually send an API request, you must use your AccessKey secret to calculate a Hash-based Message Authentication Code (HMAC) for the signature. The calculation is based on the encoded and sorted request parameters, as defined in RFC 2104. This section uses the following request parameters as an example to demonstrate how to create an API signature:

| Common parameters except Signature | &Timestamp=2016-02-23T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2019-07-23 &SignatureVersion=1.0 |
|---|---|
| Access Key Secret | <yourAccessKeySecret> |

Cloud Security Management Cent
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

| Parameter | Type | Required | Description |  |  |
|---|---|---|---|---|---|
| Version | String | Yes | The version number of the API. The value is in the YYYY-MM-DD format. Set the value to 2019-07-23. |  |  |
| AccessKeyId | String | Yes | The AccessKey ID that is provided by Apsara Stack. |  |  |
| Signature | String | Yes | The signature string of the request. |  |  |
| SignatureMethod | String | Yes | The encryption algorithm of the signature string. Set the value to HMAC-SHA1. |  |  |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time must be in UTC. The value must be in the YYYY-MM- DDThh:mm:ssZ format. For example, use 2014-05- 26T12:00:00Z to indicate May 26, 2014, 12:00:00 (UTC+8). |  |  |
|  |  |  |  | YYYY-MM- |  |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |  |  |
| SignatureNonce | String | Yes | A unique random number that is used to prevent replay attacks. You must use different numbers for different requests. |  |  |
| ResourceOwnerA ccount | String | No | The Apsara Stack tenant account to which the resource you want to access belongs, which is the username. |  |  |

|  | DDThh:mm:ssZ |
|---|---|

Cloud Security Management Cent
5. Add the resulting signature value to the request parameters as the Signature parameter.
This completes the request signing process.

#### Common parameters

Common request parameters must be included in all Apsara Stack Security API requests, such as the API version number and authentication information.

| Format | String | No | The response format. Valid values: JSON and XML. Note Default value: XML. |
|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|

Cloud Security Management Cent

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
{ "RequestId": "4C467B38-3910-447D-87BC-AC049166F216", /* Returned data */ }
```

### Operations

#### DescribeAttacks

Queries attacks on the user side or the platform side based on specified conditions.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| Action | Strin g | Query | Yes | DescribeAttacks | The operation that you want to perform. Set the value to DescribeAttacks. |
| DataScop e | Integ er | Query | No | 1 | Specifies whether to query the attacks on the user side or the platform side. Valid values: 0: indicates the platform side. 1: indicates the user side. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |
| PageNo | Integ er | Query | No | 1 | The page number. |
| SourceFro m | Integ er | Query | No | 41 | The source of attack data. Valid values: 40:Web Application Firewall. 41: Cloud Firewall. 42: Anti-DDoS (aliguard). 44: Network Traffic Monitoring System (IDS). 46: Threat detection (brute-force attack protection) |
| UserId | Long | Query | No | 2956140888888888 | The ID of the organization. |
| AttackTyp e | Strin g | Query | No | Brute-force Attack | The type of the attack. Valid values: Brute- force Attack , Non- web Attack , and SQL Injection . |

Cloud Security Management Cent

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| ProcessSt ate | Integ er | Query | No | 1 | The handling status. Valid values: 2: The alert is sent. 1: Defended 3: cleaning. 4: The cleaning process ends. |
| StartTime | Long | Query | No | 1641398400000 | The beginning of the time range to query. Unit: milliseconds. |
| EndTime | Long | Query | No | 1643644800000 | The end of the time range to query. Unit: milliseconds. |
| Keyword | Strin g | Query | No | 192.168.XX.XX | The keyword to match. You can specify an attack name, an asset name, or the IP address of an asset. |
| Asset | Strin g | Query | No | ae3ef6ef-8888-4aee- 8bac-19879e68**** | The ID of the asset. |
| Lang | Strin g | Query | No | zh CN _ | The language of the content within the request and the response. Valid values: zh CN: Simplified _ Chinese zh TW: Traditional _ Chinese en US: English _ |
| AssetType | Strin g | Query | No | ECS | The type of the affected asset. Valid values include ECS , SLB , OSS , EIP , and RDS . |

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | The request ID. |

Cloud Security Management Cent

**Response parameters**

| C e r | loud Security Ma r Developer Guid ations Center | nagement Cent e·Security Ope |  |  |  |
|---|---|---|---|---|---|

| Parameter | Type | Examples | Description |
|---|---|---|---|
| Data | Struct |  | The data that is returned. |
| -Items | Array |  | The retrieved data. |
| --AttackerIp | String | 10.0.X.X | The IP address of the attacker. |
| --AttackType | Integer | 1 | The type of the attack. |
| --AttackId | Integer | 10154212 | The ID of the attack. |
| --ProcessState | Integer | 1 | The handling status. Valid values: 2: The alert is sent. 1: Defended 3: cleaning. 4: The cleaning process ends. |
| --AttackTrait | String | 1 | This parameter is deprecated. |
| --SourceFrom | String |  | The source of attack data. Valid values: 40:Web Application Firewall. 41: Cloud Firewall. 42: Anti-DDoS (aliguard). 44: Network Traffic Monitoring System (IDS). 46: Threat detection (brute-force attack protection) |
| --UserId | Long | 295614088888888 8 | The ID of the organization. |
| --UserName | String | Organization A | The name of the organization. |
| --RaisedTime | Long | 1641548505000 | The time of the attack. |
| --AssetType | Integer | 1 | The type of the affected asset. |
| --AttackName | String | zz 78**** _ | The name of the attack. |
| --Asset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the attacked asset. |

|  |  |  |  | Cloud Security Management Cen er Developer Guide·Security Op rations Cente | t e r |
|---|---|---|---|---|---|

| Parameter | Type | Examples | Description |
|---|---|---|---|
| -- SourceFromIp | String | 10.0.X.X | The source IP address of the attack. |
| --TargetIp | String | 10.0.X.X | The destination IP address of the attack. |
| --AssetName | String | SSH brute- force**** | The name of the attacked asset. |
| -- AssetPublicIps | String | 192.168.XX.XX | The public IP address of the affected asset. |
| -- AssetPrivateIp s | String | 192.168.XX.XX | The private IP address of the affected asset. |
| -Total | Integer | 20 | The total number of entries returned. |
| -PageNo | Integer | 1 | The page number. |
| -PageSize | Integer | 10 | The number of entries per page. |

Sample requests

```
http(s)://yundunnewsoc-pop.[RegionId].example.com/?Action=DescribeAttacks &DataScope=1 &PageSize=20 &PageNo=1 &<Common request parameters>
```

Sample success response `JSON` format

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data": {"PageSize":"10","Total":"20","PageNo":"1","Items":[{"UserName":"Organization A","Attac kTrait":"1","SourceFrom":"1","AttackType":"1" "AttackerIp":"10.0.X.X","AssetName":"SSH brute force****","SourceFromIp":"10.0.X.X","AssetPrivateIps":"192. XX.XX","ProcessState":"1","AssetType":"1","AttackId":"10154212","Attack_Name":":" "2956 140888888888","AssetPublicIps":"172.12.XX.XX","Asset":"ae3ef6 ef-8888-4aee-8bac-19879e6 8****","TargetIp":"10.0.X.X","RaisedTime":"1641548505000"}]}}
```

`XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlarms | The operation that you want to perform. Set the value to DescribeAlarms. |
| DataScope | Integer | No | 1 | Specifies whether to query the data on the user side or the platform side. Valid values: 0: platform 1: user |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| PageNo | Integer | No | 1 | The number of the page to return. |

Cloud Security Management Cent

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>
    <PageSize>10</PageSize>
    <Total>20</Total>
    <PageNo>1</PageNo>
    <Items>
        <UserName>Organization A</UserName>
        <AttackTrait>1</AttackTrait>
        <SourceFrom>1</SourceFrom>
        <AttackType>1</AttackType>
        <AttackerIp>10.0.X.X</AttackerIp>
        <AssetName>SSH brute-force****</AssetName>
        <SourceFromIp>10.0.X.X</SourceFromIp>
        <AssetPrivateIps>192.168.XX.XX</AssetPrivateIps>
        <ProcessState>1</ProcessState>
        <AssetType>1</AssetType>
        <AttackId>10154212</AttackId>
        <AttackName>zz_78****</AttackName>
        <UserId>2956140888888888</UserId>
        <AssetPublicIps>172.12.XX.XX</AssetPublicIps>
        <Asset>ae3ef6ef-8888-4aee-8bac-19879e68****</Asset>
        <TargetIp>10.0.X.X</TargetIp>
        <RaisedTime>1641548505000</RaisedTime>
    </Items>
</Data>
```

#### DescribeAlarms

Queries security alerts on the user side or the platform side based on specified conditions.

**Request parameters**

| StartTime | Long | No | 1609430400000 | The beginning of the time range to query. Unit: milliseconds. |
|---|---|---|---|---|
| EndTime | Long | No | 1645977600000 | The end of the time range to query. Unit: milliseconds. |
| ProcessState | Integer | No | 1 | The handling status. Valid values: 1: unhandled 2: handled 3: ignored |
| RiskLevels.N | RepeatL ist | No | 1 | The risk levels to query. Valid values: 0: reminder. 1: suspicious. 2: urgent. You can specify multiple values in an array. Separate the values with commas. |
| Keyword | String | No | 192.168.XX.XX | The keyword to match. You can specify an alert name, an asset name, or an IP address of an asset. |
| SourceFrom | Integer | No | 20 | The source of data. Valid values: 20: Threat Detection Service or Server Guard |
| UserId | Long | No | 2956140888888 888 | The ID of the organization. |
| AlarmType | String | No | Suspicious network connection | The type of the alert. Valid values include Other, Suspicious network connection, Webshell, Suspicious process, and Unusual logon. |
| Asset | String | No | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the asset. |
| Lang | String | No | zh CN _ | The language of the content within the request and response. Valid values: zh CN: Simplified Chinese _ zh TW: Traditional Chinese _ en US: English _ |
| AssetType | String | No | ECS | The type of the affected asset. Valid values include ECS, SLB, OSS, EIP, and RDS. |

Cloud Security Management Cent

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |  | The data that is returned. |
| Items | Array of Item |  | The list of the returned data. |
| AlarmId | Integer | 4008888 | The ID of the alert. |
| AlarmName | String | Reverse** | The name of the alert. |
| AlarmType | String | Suspicious process | The type of the alert. Valid values include Other, Suspicious network connection, Webshell, Suspicious process, and Unusual logon. |
| AlarmUniqueIn fo | String | eeee98dd0c4cd5cc 61c016b2bdcf**** | The unique identifier of the alert. |
| Asset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the affected asset. |
| AssetName | String | zzzz 88**** _ | The name of the affected asset. |
| AssetPrivateIp s | String | 192.168.XX.XX | The private IP address of the affected asset. |
| AssetPublicIps | String | 172.12.XX.XX | The public IP address of the affected asset. |
| AssetType | String | ECS | The type of the affected asset. Valid values include ECS, SLB, OSS, EIP, and RDS. |
| Detail | String | {"lastTime": 1641536460051,"a ssetsType": 0,"modifiedTime": "2022-01-07 14:21:00"} | The details. |
| LastTime | Integer | 1641537619 | The time when the alert was last generated. Unit: milliseconds. |

Cloud Security Management Cent

**Response parameters**

| ProcessState | Integer | 1 | The handling status. Valid values: 1: unhandled 2: handled 3: ignored |
|---|---|---|---|
| RaisedTime | Long | 1640931449000 | The time at which the alert was first generated. Unit: milliseconds. |
| RiskLevel | Integer | 2 | The risk level of the alert. Valid values: 0: reminder 1: suspicious 2: urgent |
| SourceFrom | Integer | 20 | The source of data. Valid values: 20: Threat Detection Service or Server Guard |
| UserId | Integer | 295614088 | The ID of the organization. |
| UserName | String | Organization A | The name of the organization. |
| PageNo | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| Total | Integer | 200 | The total number of entries returned. |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | The ID of the request. |

Cloud Security Management Cent Sample requests

```
http(s)://yundunnewsoc-pop.[RegionId].example.com/?Action=DescribeAlarms &RiskLevels=[0,1,2] &DataScope=1 &PageSize=20 &PageNo=1 &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVulFran gs | The operation that you want to perform. Set the value to DescribeVulFrangs. |

Cloud Security Management Cent

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>
    <PageSize>20</PageSize>
    <Total>200</Total>
    <PageNo>1</PageNo>
    <Items>
        <AlarmId>4008888</AlarmId>
        <UserName>Organization A</UserName>
        <AlarmType>Suspicious process</AlarmType>
        <SourceFrom>20</SourceFrom>
        <AssetName>zzzz_88****</AssetName>
        <AssetPrivateIps>192.168.XX.XX</AssetPrivateIps>
        <ProcessState>1</ProcessState>
        <AssetType>ECS</AssetType>
        <AlarmName>Reverse**</AlarmName>
        <UserId>295614088</UserId>
        <AlarmUniqueInfo>eeee98dd0c4cd5cc61c016b2bdcf****</AlarmUniqueInfo>
        <AssetPublicIps>172.12.XX.XX</AssetPublicIps>
        <Asset>ae3ef6ef-8888-4aee-8bac-19879e68****</Asset>
        <RaisedTime>1640931449000</RaisedTime>
        <RiskLevel>2</RiskLevel>
        <Detail>{"lastTime": 1641536460051,"assetsType": 0,"modifiedTime": "2022-01-07
14:21:00"}</Detail>
        <LastTime>1641537619</LastTime>
    </Items>
</Data>
```

`JSON` format

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data": {"PageSize":"20","Total":"200","PageNo":"1","Items": [{"AlarmId":"4008888","UserName":"Organization A","AlarmType":"Suspicious process","SourceFrom":"20","AssetName":"zzzz_88****","AssetPrivateIps":"192.168.XX.XX","P cessState":"1","AssetType":"ECS","AlarmName":"Reverse**","UserId":"295614088","AlarmUniqu nfo":"eeee98dd0c4cd5cc61c016b2bdcf****","AssetPublicIps":"172.12.XX.XX","Asset":"ae3ef6ef 8888-4aee-8bac-19879e68****","RaisedTime":"1640931449000","RiskLevel":"2","Detail":"{\" lastTime\": 1641536460051,\"assetsType\": 0,\"modifiedTime\": \"2022-01-07 14:21:00\"}","LastTime":"1641537619"}]}}
```

#### DescribeVulFrangs

Queries vulnerabilities based on specified conditions.

**Request parameters**

| RiskLevel | Integer | No | 1 | The severity of the vulnerability. Valid values: 0: low 1: medium 2: high |
|---|---|---|---|---|
| ProcessState | Integer | No | 1 | The handling status. Valid values: 1: unhandled 2: handled |
| VulType | String | No | cve | The type of the vulnerability. Valid values: cve, sys, sca, and emg. |
| PocFlag | Integer | No | 1 | Specifies whether to query data related to Proof of Concept (POC). Valid values: 0: no 1: yes |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| DataScope | Integer | No | 1 | Specifies whether to query the data on the user side or the platform side. Valid values: Valid values: 0: platform 1: user |
| UserId | Long | No | 2956140888888 888 | The ID of the organization. |
| UsageLevel | String | No | LOW | The exploitability of the vulnerability. Valid values include LOW, HIGH, MEDIUM, INSUFFICIENT INFO, and _ NONE. |
| StartTime | Long | No | 1641484800000 | The beginning of the time range to query. Unit: milliseconds. |
| EndTime | Long | No | 1643644800000 | The end of the time range to query. Unit: milliseconds. |
| Page | Integer | No | 1 | The number of the page to return. |
| NeedFix | String | No | necessity | The priority to fix the vulnerability. |

Cloud Security Management Cent

| Keyword | String | No | 192.168.XX.XX | The keyword to match. You can specify a vulnerability name, an asset name, or the IP address of an asset. |
|---|---|---|---|---|
| SourceFrom | Integer | No | 1 | The source of data. Valid values: 1: host vulnerabilities detected by Server Guard |
| Asset | String | No | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the asset affected by the vulnerability. |
| AssetType | String | No | ECS | The type of the asset affected by the vulnerability. Valid values include ECS, SLB, OSS, EIP, and RDS. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |  | The data that is returned. |
| Items | Array of Item |  | The list of the returned data. |
| Asset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the asset affected by the vulnerability. |
| AssetName | String | zzz 75**** _ | The name of the asset affected by the vulnerability. |
| AssetPrivateIp s | String | 192.168.XX.XX | The private IP address of the asset affected by the vulnerability. |
| AssetPublicIps | String | 172.12.XX.XX | The public IP address of the asset affected by the vulnerability. |
| AssetType | String | ECS | The type of the asset affected by the vulnerability. Valid values include ECS, SLB, OSS, EIP, and RDS. |
| Id | Long | 75489 | The ID of the data. |
| LastTime | String | 1642025151000 | The time when the vulnerability was last detected. Unit: milliseconds. |

Cloud Security Management Cent

**Response parameters**

| NeedFix | String | necessity | The priority to fix the vulnerability. |
|---|---|---|---|
| ProcessState | Integer | 1 | The handling status. Valid values: 1: unhandled 2: handled |
| RaisedTime | Integer | 2022 | The time of occurrence. The time follows the yyyy format. |
| RiskLevel | Integer | 1 | The severity of the vulnerability. Valid values: 0: low 1: medium 2: high |
| SourceFrom | Integer | 1 | The source of data. Valid values: 1: host vulnerabilities detected by Server Guard |
| SrcInnerName | String | oval:com.redhat.rh sa:def:2021**** | The name of the vulnerability. |
| UsageLevel | String | LOW | The exploitability of the vulnerability. Valid values include LOW, HIGH, MEDIUM, INSUFFICIENT INFO, and NONE. _ |
| UserName | String | Organization A | The name of the organization. |
| VulName | String | RHSA-2021:1180- Mode**** | The name of the vulnerability. |
| VulRelated | String | CVE-2017-100**** | The ID of the associated vulnerability. |
| VulType | String | cve | The type of the vulnerability. Valid values: cve, sys, sca, and emg. |
| PageNo | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| Total | Integer | 200 | The total number of entries returned. |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | The ID of the request. |

Cloud Security Management Cent Cloud Security Management Cent Sample requests

```
http(s)://yundunnewsoc-pop.[RegionId].example.com/?Action=DescribeVulFrangs &DataScope=1 &PageSize=20 &Page=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>
    <PageSize>10</PageSize>
    <Total>200</Total>
    <PageNo>1</PageNo>
    <Items>
        <NeedFix>necessity</NeedFix>
        <UserName>Organization A</UserName>
        <SourceFrom>1</SourceFrom>
        <VulName>RHSA-2021:1180-Mode****</VulName>
        <AssetName>zzz_75****</AssetName>
        <UsageLevel>LOW</UsageLevel>
        <AssetPrivateIps>192.168.XX.XX</AssetPrivateIps>
        <ProcessState>1</ProcessState>
        <AssetType>ECS</AssetType>
        <SrcInnerName>oval:com.redhat.rhsa:def:2021****</SrcInnerName>
        <VulRelated>CVE-2017-100****</VulRelated>
        <AssetPublicIps>172.12.XX.XX</AssetPublicIps>
        <Asset>ae3ef6ef-8888-4aee-8bac-19879e68****</Asset>
        <Id>75489</Id>
        <RaisedTime>2022</RaisedTime>
        <RiskLevel>1</RiskLevel>
        <LastTime>1642025151000</LastTime>
        <VulType>cve</VulType>
    </Items>
</Data>
```

`JSON` format

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data": {"PageSize":"10","Total":"200","PageNo":"1","Items": [{"NeedFix":"necessity","UserName":"Organization A","SourceFrom":"1","VulName":"RHSA-20 21:1180- Mode****","AssetName":"zzz_75****","UsageLevel":"LOW","AssetPrivateIps":"192.168.XX.XX"," ocessState":"1","AssetType":"ECS","SrcInnerName":"oval:com.redhat.rhsa:def:2021****","Vul lated":"CVE-2017-100****","AssetPublicIps":"172.12.XX.XX","Asset":"ae3ef6ef-8888-4aee-8 bac- 19879e68****","Id":"75489","RaisedTime":"2022","RiskLevel":"1","LastTime":"1642025151000" VulType":"cve"}]}}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHcFran gs | The operation that you want to perform. Set the value to DescribeHcFrangs. |
| RiskLevel | Integer | No | 1 | The level of the risk. Valid values: 0: low 1: medium 2: high |
| ProcessState | Integer | No | 1 | The handling status. Valid values: 1: unhandled 2: handled |
| HcType | String | No | Alibaba Cloud Standard - Windows 2016/2019 Security Baseline | The type of the risk in host configurations. Valid values: Alibaba Cloud Standard - Windows 2016/2019 Security Baseline, Alibaba Cloud Standard - Apache Tomcat Security Baseline, and Alibaba Cloud Standard - CentOS Linux 7/8 Security Baseline Check. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| StartTime | Long | No | 1641484800000 | The beginning of the time range to query. Unit: milliseconds. |
| EndTime | Long | No | 1643731200000 | The end of the time range to query. Unit: milliseconds. |
| Page | Integer | No | 1 | The number of the page to return. |

Cloud Security Management Cent

#### DescribeHcFrangs

Queries the risks in the host configurations on the user side.

**Request parameters**

| Keyword | String | No | 192.168.XX.XX | The keyword to match. You can specify an asset name or the IP address of an asset. |
|---|---|---|---|---|
| DataScope | Integer | No | 1 | Specifies whether to query the data on the user side or the platform side. Valid values: 0: platform 1: user |
| UserId | Long | No | 2956140888888 888 | The ID of the organization. |
| SourceFrom | Integer | No | 2 | The source of data. Valid values: 2: host configuration check |
| Asset | String | No | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the asset. |
| AssetType | String | No | ECS | The type of the asset. Valid values include ECS, SLB, OSS, EIP, and RDS. |
| Lang | String | No | zh CN _ | The language of the content within the request and response. Valid values: zh CN: Simplified Chinese _ zh TW: Traditional Chinese _ en US: English _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |  | The data that is returned. |
| Items | Array of Item |  | The list of the returned data. |
| Asset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the asset that is affected by the risk. |
| AssetName | String | zz 78**** _ | The name of the asset that is affected by the risk. |
| AssetPrivateIp s | String | 192.168.XX.XX | The private IP address of the asset that is affected by the risk. |

Cloud Security Management Cent

**Response parameters**

| AssetPublicIps | String | 172.12.XX.XX | The public IP address of the asset that is affected by the risk. |
|---|---|---|---|
| AssetType | String | ECS | The type of the asset that is affected by the risk. Valid values include ECS, SLB, OSS, EIP, and RDS. |
| HcAsset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the asset. |
| HcName | String | CIS Standard*** | The name of the host configuration risk. |
| HcType | String | Alibaba Cloud Standard - Windows 2016/2019 Security Baseline | The type of the risk in host configurations. Valid values: Alibaba Cloud Standard - Windows 2016/2019 Security Baseline, Alibaba Cloud Standard - Apache Tomcat Security Baseline, and Alibaba Cloud Standard - CentOS Linux 7/8 Security Baseline Check. |
| Id | Long | 65357 | The ID of the record. |
| LastFoundTim e | String | 1642042910000 | The time when the risk was last detected. Unit: milliseconds. |
| ProcessState | Integer | 2 | The handling status of the risk. Valid values: 1: handled 2: unhandled |
| RiskLevel | Integer | 1 | The level of the risk. Valid values: 0: low 1: medium 2: high |
| SourceFrom | String | 2 | The source of data. Valid values: 2: host configuration check |
| UserId | Long | 295614088888888 8 | The ID of the organization. |

Cloud Security Management Cent

| UserName | String | Organization A | The name of the organization. |
|---|---|---|---|
| PageNo | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| Total | Integer | 200 | The total number of entries returned. |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | The ID of the request. |

Cloud Security Management Cent Sample requests

```
http(s)://yundunnewsoc-pop.[RegionId].example.com/?Action=DescribeVulFrangs &DataScope=1 &PageSize=20 &Page=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>
    <PageSize>10</PageSize>
    <Total>200</Total>
    <PageNo>1</PageNo>
    <Items>
        <UserName>Organization A</UserName>
        <SourceFrom>2</SourceFrom>
        <HcType>Alibaba Cloud Standard - Windows 2016/2019 Security Baseline</HcType>
        <AssetName>zz_78****</AssetName>
        <HcAsset>ae3ef6ef-8888-4aee-8bac-19879e68****</HcAsset>
        <AssetPrivateIps>192.168.XX.XX</AssetPrivateIps>
        <ProcessState>2</ProcessState>
        <LastFoundTime>1642042910000</LastFoundTime>
        <AssetType>ECS</AssetType>
        <HcName>CIS standard***</HcName>
        <UserId>2956140888888888</UserId>
        <AssetPublicIps>172.12.XX.XX</AssetPublicIps>
        <Asset>ae3ef6ef-8888-4aee-8bac-19879e68****</Asset>
        <Id>65357</Id>
        <RiskLevel>1</RiskLevel>
    </Items>
</Data>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryThreats | The operation that you want to perform. Set the value to QueryThreats. |
| FromTime | Long | No | 1640944798076 | The beginning of the time range to query. Unit: milliseconds. |
| ToTime | Long | No | 1641549603697 | The end of the time range to query. Unit: milliseconds. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| Index | String | No | threat | The data index. Set the value to threat. |
| UserIds | String | No | - 1,29561408888 8**** | The ID of the department. You can specify -1 or the ID of a tenant organization. The value -1 specifies that data on the platform side is queried. Separate multiple values with commas (,). |
| Aliuid | Long | No | 1 | This parameter is deprecated. |

Cloud Security Management Cent

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data": {"PageSize":"10","Total":"200","PageNo":"1","Items":[{"UserName":"Organization A","Sour ceFrom":"2","HcType":"Alibaba Cloud Standard - Windows 2016/2019 Security Baseline","AssetName":"zz_78****","HcAsset":"ae3ef6ef-8888-4aee-8bac- 19879e68****","AssetPrivateIps":"192.168.XX.XX","ProcessState":"2","LastFoundTime":"16420 910000","AssetType":"ECS","HcName":"CIS standard***","UserId":"2956140888888888","AssetPublicIps":"172.12.XX.XX","Asset":"ae3ef6e 8888-4aee-8bac-19879e68****","Id":"65357","RiskLevel":"1"}]}}
```

### Operations Center

#### QueryThreats

Queries attack data in the Operations Center dashboard.

**Request parameters**

| Query | String | No | 192.168.XX.XX | The keyword to match. You can specify the IP address of an alerting asset or the IP address in an attack. |
|---|---|---|---|---|
| ProcessStatus | String | No | 1 | The handling status. Valid values: 1: unhandled 2: handled |
| ThreatLevel | String | No | 1 | The risk level of the attack. Valid values: 1: low 2: medium 3: high |
| SrcFrom | String | No | 20,40 | The source of data. Separate multiple values with commas (,). Valid values: 20: Server Guard 40: Web Application Firewall (WAF) 41: Cloud Firewall 44: Network Detection and Response (NDR) |
| ThreatType | String | No | Suspicious process | The type of the alert that is generated for the attack. Valid values include Non-web attack, Precise defense, Web attack, Other, and Suspicious process. |
| ThreatName | String | No | Suspicious encoded command | The name of the attack. |
| ProcessWay | String | No | 1 | The handling method. Valid values: 0: allow 1: intercept 2: ignore 3: manually handle 4: batch block 5: automatically handle 6: alert 7: discard 8: block |

Cloud Security Management Cent

| ThreatInoutside | String | No | 1 | The source of the attack. Valid values: 1: internal attack 2: external attack |
|---|---|---|---|---|
| ThreatResult | String | No | Success | The result of the attack. Valid values include Attempt, Success, and Failure. |
| Lang | String | No | zh CN _ | The language of the content within the request and response. Valid values: zh CN: Simplified Chinese _ zh TW: Traditional Chinese _ en US: English _ |
| Tag | String | No | 121 | The tag. |
| DestinationIp | String | No | 192.168.XX.XX | The attacked IP address. |
| ThreatSourceIp | String | No | 172.12.XX.XX | The source IP address of the attack. |
| UrlHost | String | No | www.ecs****.co m | The website. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| Datas | List | {"lastTime":16415 49724000," logTi __ me":16415497242 87,"process way":" _ "} | The list of data records that are queried from Elasticsearch. Each array in the list represents a data record. |
| FromTime | Long | 1641484800000 | The start time of the attack. Unit: milliseconds. |
| HistogramInter val | Long | 0 | The interval of the histogram. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | The ID of the request. |

Cloud Security Management Cent

**Response parameters**

| ToTime | Long | 1641550177290 | The end time of the attack. Unit: milliseconds. |
|---|---|---|---|
| Total | Integer | 200 | The total number of entries returned. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryThreatCha rtData | The operation that you want to perform. Set the value to QueryThreatChartData. |

Cloud Security Management Cent Sample requests

```
&CurrentPage=1 &PageSize=10 &FromTime=1641484800000 &ToTime=1641550177290 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ToTime>1641550177290</ToTime> <PageSize>10</PageSize> <RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <HistogramInterval>0</HistogramInterval> <CurrentPage>1</CurrentPage> <Datas>{"lastTime":1641549724000,"__logTime":1641549724287,"process_way":""}</Datas> <Total>200</Total> <FromTime>1641484800000</FromTime>
```

`JSON` format

```json
{"ToTime":"1641550177290","PageSize":"10","RequestId":"8010791A-3154-4154-ACB2-866E56A6
****","HistogramInterval":"0","CurrentPage":"1","Datas":"
{\"lastTime\":1641549724000,\"__logTime\":1641549724287,\"process_way\":\"\"}","Total":"2 ","FromTime":"1641484800000"}
```

#### QueryThreatChartData

Queries the data in a chart of the Operations Center dashboard.

**Request parameters**

| FromTime | Long | No | 1640944798076 | The beginning of the time range to query. Unit: milliseconds. |
|---|---|---|---|---|
| ToTime | Long | No | 1641549603697 | The end of the time range to query. Unit: milliseconds. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| Index | String | No | threat | The data index. Set the value to threat. |
| Aliuid | Long | No | 1 | This parameter is deprecated. |
| UserIds | String | No | - 1,29561408888 8**** | The ID of the department. You can specify -1 or the ID of a tenant organization. The value -1 specifies that data on the platform side is queried. Separate multiple values with commas (,). |
| Query | String | No | 192.168.XX.XX | The keyword to match. You can specify the IP address of an alerting asset or the IP address in an attack. |
| ProcessStatus | String | No | 1 | The handling status. Valid values: 1: unhandled 2: handled |
| ThreatLevel | String | No | 1 | The risk level of the attack. Valid values: 1: low 2: medium 3: high |

Cloud Security Management Cent

| SrcFrom | String | No | 20,40 | The source of data. Separate multiple values with commas (,). Valid values: 20: Server Guard 40: Web Application Firewall (WAF) 41: Cloud Firewall 44: Network Detection and Response (NDR) |
|---|---|---|---|---|
| ThreatType | String | No | Suspicious process | The type of the alert that is generated for the attack. Valid values include Non-web attack, Precise defense, Web attack, Other, and Suspicious process. |
| ThreatName | String | No | Suspicious encoded command | The name of the attack. |
| ProcessWay | String | No | 1 | The handling method. Valid values: 0: allow 1: intercept 2: ignore 3: manually handle 4: batch block 5: automatically handle 6: alert 7: discard 8: block |
| ThreatInoutside | String | No | 1 | The source of the attack. Valid values: 1: internal attack 2: external attack |
| ThreatResult | String | No | Success | The result of the attack. Valid values include Attempt, Success, and Failure. |
| Properties | String | No | {"x type":"term" _ ,"y config 1":"sr _ _ c from,count"} _ | The settings that are used to query the chart. Specify the value in the following JSON format: {"x type":"term"(X- _ axis),"y config 1":"src from(Y- _ _ _ axis),count(Count)"}. |

Cloud Security Management Cent

| ChartType | String | No | pie | The type of the chart. Valid values include histogram, bar, line, pie, table, and value. |
|---|---|---|---|---|
| Lang | String | No | zh CN _ | The language of the content within the request and response. Valid values: zh CN: Simplified Chinese _ zh TW: Traditional Chinese _ en US: English _ |
| Tag | String | No | tem | The tag. |
| Size | String | No | 10 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | List | {"20": {"src from,count":" _ 23507"}} | The list of data records that are queried from Elasticsearch. Each array in the list represents a data record. |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | The ID of the request. |

Cloud Security Management Cent

**Response parameters**

Sample requests

```
http(s)://[Endpoint]/?Action=QueryThreatChartData &CurrentPage=1 &PageSize=10 &FromTime=1641484800000 &ToTime=1641550177290 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>{"20":{"src_from,count":"23507"}}</Data>
```

`JSON` format

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data":"{\"20\": {\"src_from,count\":\"23507\"}}"}
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | CreateEventType | The operation that you want to perform. Set the value to CreateEventType . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| LogType | Integ er | Query | Yes | 5 | The code of the log type. |
| SourceId | Long | Query | Yes | 10000 | The ID of the log source. |
| Name | Strin g | Query | Yes | High-risk query | The name of the audit event type. |
| Remark | Strin g | Query | Yes | High-risk database query | The description of the audit event type. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |
| EventType | Struct | - | The audit event type that is created. |
| -LogType | Integer | 1 | The code of the log type. |

Cloud Security Management Cent

## APIs

### CreateEventType

Creates an audit event type.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

|  |  |  | Cloud Security Management Cen |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -SourceId | Long | 1000 | The ID of the log source. |
| -CreateTime | Long | 1639236844747 | The creation time. |
| -Reserved | Boolean | true | Indicates whether the event type is reserved in the system. |
| -Name | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | The name of the audit event type. |
| -Remark | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | The description of the audit event type. |
| -Id | Integer | 10135 | The ID of the audit event type. |
| -SourceName | String | rds-ss12222 | The name of the log source. |

Sample requests

```
&LogType=5 &Name=High-risk query &Remark=High-risk database query &SourceId=10000 &<Common request parameters>
```

Sample success responses

```json
 JSON format
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "EventType":{
  "SourceId":1000,
  "CreateTime":1639236844747,
  "LogType":1,
  "SourceName":"rds-ss12222",
  "Id":10135,
  "Reserved":true,
  "Name":"EVENT_TYPE_NAME__host__account_create",
  "Remark":"EVENT_TYPE_NAME__host__account_create"
 }
}
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeEventType | The operation that you want to perform. Set the value to DescribeEventType . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| SourceId | Long | Query | No | 1000 | The ID of the log source. |
| LogType | Integ er | Query | No | 1 | The type of the log. |
| PageSize | Integ er | Query | No | 20 | The number of entries per page. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EventTypeList | Array | - | The audit event types. |
| -LogType | Integer | 1 | The type of the log. |
| -SourceId | Long | 1000 | The ID of the log source. |
| -CreateTime | Long | 1639236844747 | The creation time. |
| -Reserved | Boolean | true | Indicates whether the event type is reserved in the system. |

Cloud Security Management Cent

### DescribeEventType

Queries audit event types.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

|  |  |  |  | Cloud Security Management Cen er Developer Guide·API | t s |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Name | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | The name of the audit event type. |
| -Remark | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | The description of the audit event type. |
| -Code | String | account create _ | The code of the audit event type. |
| -Id | Integer | 10135 | The ID of the audit event type. |
| -SourceName | String | rds-ss12222 | The name of the log source. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |
| CurrentPage | Integer | 1 | The page number. |
| PageSize | Integer | 20 | The number of entries per page. |
| TotalCount | Integer | 100 | The total number of entries returned. |

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DeleteEventType | The operation that you want to perform. Set the value to DeleteEventType . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| Id | Integ er | Query | Yes | 10135 | The ID of the audit event type. |

| Parameter | Type | Example | Description |
|---|---|---|---|

Cloud Security Management Cent

```json
{
 "TotalCount":100,
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "CurrentPage":1,
 "EventTypeList":[
  {
   "SourceId":1000,
   "CreateTime":1639236844747,
   "LogType":1,
   "SourceName":"rds-ss12222",
   "Id":10135,
   "Code":"account_create",
   "Reserved":true,
   "Name":"EVENT_TYPE_NAME__host__account_create",
   "Remark":"EVENT_TYPE_NAME__host__account_create"
  }
```

]

```
}
```

### DeleteEventType

Deletes an audit event type.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | CreateLogFilter | The operation that you want to perform. Set the value to CreateLogFilter . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| Type | Integ er | Query | Yes | 1 | The type of the filter condition. Valid values: 1 and 2. The value 1 indicates a filter condition for logs, and the value 2 indicates a filter condition for audit events. |

Cloud Security Management Cent Sample requests

```
&Id=10135 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### CreateLogFilter

Creates a filter condition to query audit logs.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| LogType | Integ er | Query | Yes | 1 | The type of the log. |
| SourceId | Long | Query | No | 1000 | The ID of the log source. |
| Name | Strin g | Query | Yes | RDS-scscsc | The name of the filter condition. |
| Defaultabl e | Boole an | Query | No | true | Specifies whether to use the filter condition as the default filter condition. Valid values: true and false. |
| EventRisk Level | Integ er | Query | No | 1 | The risk level. |
| EventType | Integ er | Query | No | 1 | The type of the audit event. |
| Alertable | Boole an | Query | No | true | Specifies whether an alert is triggered. Valid values: true and false. |
| Query | Strin g | Query | No | Get | The keyword for the query. |
| StartTime | Long | Query | No | 1519813584985 | The beginning of the time range to query. This value is a timestamp. |
| EndTime | Long | Query | No | 1519813584985 | The end of the time range to query. This value is a timestamp. |
| LogInitiati or | Strin g | Query | No | EQ:Initiator | The initiator. |
| LogTarget | Strin g | Query | No | EQ:target | The target. |
| LogAction | Strin g | Query | No | EQ:cmd | The operation. |
| LogOutco me | Strin g | Query | No | EQ:result | The result. |

Cloud Security Management Cent

|  |  |  |  | Cloud | Security Management Cen er Developer Guide·API |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| LogReaso n | Strin g | Query | No | EQ:reason | The reason. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |
| LogFilter | Struct | - | The filter condition that is created. For more information, see the following parameter descriptions. |
| -LogType | Integer | 1 | The type of the log. |
| -SourceId | Long | 1000 | The ID of the log source. |
| -Defaultable | Boolean | true | Indicates whether the filter condition is used as the default filter condition. Valid values: true and false. |
| -CreateTime | Long | 1639236844747 | The creation time. |
| -Name | String | RDS-scscsc | The name of the filter condition. |
| -Id | Integer | 1000 | The ID of the filter condition. |
| -Type | Integer | 1 | The type of the filter condition. Valid values: 1 and 2. The value 1 indicates a filter condition for logs, and the value 2 indicates a filter condition for audit events. |
| -UserId | String | 1000 | The ID of the creator. |
| -EventType | Integer | 1 | The type of the audit event. |

**Response parameters**

Sample requests

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RequestId | Strin g | System | Yes | DescribeLogFilter | The operation that you want to perform. Set the value to DescribeLogFilter . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| LogType | Strin g | Query | No | 1 | The type of the log. |
| SourceId | Long | Query | No | 1001 | The ID of the log source. |

Cloud Security Management Cent

```
&LogType=1 &Name=RDS-scscsc &Type=1 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "LogFilter":{
  "Type":1,
  "EventType":1,
  "UserId":"1000",
  "SourceId":1000,
  "CreateTime":1639236844747,
  "LogType":1,
  "Id":1000,
  "Defaultable":true,
  "Name":"RDS-scscsc"
 }
}
```

### DescribeLogFilter

Queries filter conditions for audit logs.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

|  |  |  |  | Cloud | Security Management Cen er Developer Guide·API |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Count | Integ er | Query | No | 1001 | The number of entries to return. |
| Type | Strin g | Query | No | 1 | The type of the filter condition. Valid values: 1 and 2. The value 1 specifies a filter condition for logs, and the value 2 specifies a filter condition for audit events. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogFilterList | Array | - | The filter conditions. |
| -LogType | Integer | 1 | The type of the log. |
| -SourceId | Long | 1000 | The ID of the log source. |
| -Defaultable | Boolean | true | Indicates whether the filter condition is used as the default filter condition. Valid values: True and False. |
| -CreateTime | Long | 1639236844747 | The creation time. |
| -Name | String | RDS-scscsc | The name of the filter condition. |
| -Id | Integer | 1000 | The ID of the filter condition. |
| -Type | Integer | 1 | The type of the filter condition. Valid values: 1 and 2. The value 1 indicates a filter condition for logs, and the value 2 indicates a filter condition for audit events. |
| -UserId | String | 100000 | The ID of the creator. |
| - EventRiskLeve l | Integer | 1 | The risk level. |

**Response parameters**

| loud Security Ma | nagement Cent |  |  |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -EventType | Integer | 1 | The type of the audit event. |
| -Alertable | Boolean | true | Indicates whether an alert is triggered. |
| -StartTime | Long | 1519813584985 | The start time of the query. This value is a timestamp. |
| -EndTime | Long | 1519813584985 | The end time of the query. This value is a timestamp. |
| -Query | String | Get | The keyword for the query. |
| -LogTarget | String | EQ:target | The target. |
| -LogAction | String | EQ:cmd | The operation. |
| -LogOutcome | String | EQ:result | The result. |
| -LogInitiatior | String | EQ:Initiator | The initiator. |
| -LogReason | String | EQ:reason | The reason. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DeleteLogFilter | The operation that you want to perform. Set the value to DeleteLogFilter . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| Id | Integ er | Query | Yes | 1000 | The ID of the filter condition. |

Cloud Security Management Cent

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "LogFilterList":[
  {
   "EndTime":1519813584985,
   "Query":"Get",
   "EventType":1,
   "SourceId":1000,
   "CreateTime":1639236844747,
   "LogType":1,
   "StartTime":1519813584985,
   "EventRiskLevel":1,
   "LogTarget":"EQ:target",
   "Name":"RDS-scscsc",
   "Type":1,
   "LogAction":"EQ:cmd",
   "LogInitiatior":"EQ:Initiator",
   "UserId":"100000",
   "LogReason":"EQ:reason",
   "LogOutcome":"EQ:result",
   "Id":1000,
   "Alertable":true,
   "Defaultable":true
  }
```

]

```
}
```

### DeleteLogFilter

Deletes a filter condition for audit logs.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | CreateReceiver | The operation that you want to perform. Set the value to CreateReceiver . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| LogType | Integ er | Query | No | 1 | The type of the log. |
| SourceId | Long | Query | No | 1000 | The ID of the log source. |

Cloud Security Management Cent

**Response parameters**

Sample requests

```
&Id=1000 &<Common request parameters>
```

Sample success responses

```json
 JSON format
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### CreateReceiver

Creates an alert recipient for audit events.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| EventRisk Level | Integ er | Query | Yes | 1 | The risk level. |
| Contact | Strin g | Query | Yes | *****@aliyun.com | The contact information about the alert recipient. |
| Name | Strin g | Query | Yes | Jack | The name of the alert recipient. |
| Type | Integ er | Query | Yes | 1 | The alert receiving method. Set the value to 1. The value 1 specifies that alerts are sent through emails. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |
| Receiver | Struct | - | The created alert recipient. For more information, see the following parameter descriptions. |
| -LogType | Integer | 1 | The type of the log. |
| -SourceId | Long | 1000 | The ID of the log source. |
| - EventRiskLeve l | Integer | 1 | The risk level. |
| -CreateTime | Long | 1639236844747 | The creation time. |
| -Contact | String | *****@aliyun.com | The contact information about the alert recipient. |
| -Name | String | Jack | The name of the alert recipient. |
| -Id | Integer | 10001 | The ID of the alert recipient. |

**Response parameters**

| Cloud Security Ma | nagement Cent |  |  |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -SourceName | String | rds-ss12222 | The name of the log source. |
| -Type | Integer | 1 | The alert receiving method. The value is fixed as 1. The value 1 indicates that alerts are sent through emails. |

Sample requests

```
&Contact=*****@aliyun.com &EventRiskLevel=1 &Name=Jack &Type=1 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "Receiver":{
  "Type":1,
  "SourceId":1000,
  "CreateTime":1639236844747,
  "LogType":1,
  "SourceName":"rds-ss12222",
  "Id":10001,
  "EventRiskLevel":1,
  "Contact":"*****@aliyun.com",
  "Name":"Jack"
 }
}
```

### DescribeReceiver

Queries information about alert recipients.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeReceiver | The operation that you want to perform. Set the value to DescribeReceiver . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| LogType | Strin g | Query | No | 1 | The type of the log. |
| SourceId | Long | Query | No | 1000 | The ID of the log source. |
| EventRisk Level | Strin g | Query | No | 1 | The risk level. |
| Contact | Strin g | Query | No | 123@qq.com | The contact information about the alert recipient. |
| Name | Strin g | Query | No | Jack | The name of the alert recipient. |
| SourceNa me | Strin g | Query | No | rds-ss12222 | The name of the log source. |
| PageSize | Integ er | Query | No | 20 | The number of entries per page. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ReceiverList | Array | - | The information about the alert recipient. |
| -LogType | Integer | 1 | The type of the log. |
| -SourceId | Long | 1000 | The ID of the log source. |
| - EventRiskLeve l | Integer | 1 | The risk level. |

Cloud Security Management Cent

**Response parameters**

| Cloud Security Ma r Developer Guid | nagement Cent e·APIs |  |  |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -CreateTime | Long | 1639236844747 | The creation time. |
| -Contact | String | *****@aliyun.com | The contact information about the alert recipient. |
| -Name | String | Jack | The name of the alert recipient. |
| -Id | Integer | 10001 | The ID of the alert recipient. |
| -SourceName | String | rds-ss12222 | The name of the log source. |
| -Type | Integer | 1 | The alert receiving method. The value is fixed as 1. The value 1 indicates that alerts are sent through emails. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |
| CurrentPage | Integer | 1 | The page number. |
| PageSize | Integer | 20 | The number of entries per page. |
| TotalCount | Integer | 100 | The total number of entries returned. |

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DeleteReceiver | The operation that you want to perform. Set the value to DeleteReceiver . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| Id | Integ er | Query | Yes | 1000 | The ID of the alert recipient. |

| Parameter | Type | Example | Description |
|---|---|---|---|

Cloud Security Management Cent

```json
{
 "TotalCount":100,
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "CurrentPage":1,
 "ReceiverList":[
  {
   "Type":1,
   "SourceId":1000,
   "CreateTime":1639236844747,
   "LogType":1,
   "SourceName":"rds-ss12222",
   "Id":10001,
   "EventRiskLevel":1,
   "Contact":"*****@aliyun.com",
   "Name":"Jack"
  }
```

]

```
}
```

### DeleteReceiver

Deletes an alert recipient for audit events.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | CreateRule | The operation that you want to perform. Set the value to CreateRule . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| LogType | Integ er | Query | Yes | 1 | The code of the log type. |
| SourceId | Long | Query | No | 1000 | The ID of the log source. |

Cloud Security Management Cent Sample requests

```
&Id=1000 &<Common request parameters>
```

Sample success responses

```json
 JSON format
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### CreateRule

Creates an audit rule.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Expressio n | Strin g | Query | No | action INCLUDE "Delete instance" OR action INCLUDE "Delete cluster" OR action INCLUDE "Delete host" | The expression in the audit rule. |
| EventRisk Level | Integ er | Query | Yes | 1 | The risk level. |
| Remark | Strin g | Query | No | remark | The remarks. |
| Alertable | Boole an | Query | Yes | true | Specifies whether an alert is triggered. |
| EventType Id | Integ er | Query | Yes | 10001 | The type of the audit event. |
| OperatorT ype | Integ er | Query | No |  |  |
| RuleName | Strin g | Query | Yes | High-risk deletion operation | The name of the audit rule. |
| StartTime | Strin g | Query | No | 1640442436125 | The start time. This value is a timestamp. |
| EndTime | Strin g | Query | No | 1640442436125 | The end time. This value is a timestamp. |
| AlertActio nList | Strin g | Query | No | 1 | The alert recipient in the rule. Separate multiple alert recipients with commas (,). |
| LogInitiati or | Strin g | Query | No | EQ:Initiator | The initiator. |
| LogTarget | Strin g | Query | No | EQ:target | The destination. |
| LogAction | Strin g | Query | No | EQ:cmd | The audit object. |
| LogOutco me | Strin g | Query | No | EQ:result | The result. |
| LogReaso n | Strin g | Query | No | EQ:reason | The reason. |

Cloud Security Management Cent

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |
| Rule | Struct | - | The created audit rule. For more information, see the following parameter descriptions. |
| -LogType | Integer | 1 | The code of the log type. |
| -SourceId | Long | 1000 | The ID of the log source. |
| - EventRiskLeve l | Integer | 1 | The risk level. |
| -Alertable | Boolean | true | Indicates whether an alert is triggered. |
| -Enabled | Boolean | true | Indicates whether the rule is enabled. |
| -EventTypeId | Integer | 10001 | The type of the audit event. |
| -CreateTime | Long | 1639236844747 | The creation time. |
| -Reserved | Boolean | false | Indicates whether the audit rule is reserved. |
| -Name | String | High-risk deletion operation | The name of the audit rule. |
| - EventTypeNa me | String | Resource Management event | The name of the event type. |
| -Id | Integer | 1000 | The ID of the audit rule. |
| -SourceName | String | rds-ss12222 | The name of the log source. |
| -AlertActions | String | 1 | The alert recipient in the rule. |

Cloud Security Management Cent

**Response parameters**

Sample requests

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeRule | The operation that you want to perform. Set the value to DescribeRule . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |

Cloud Security Management Cent

```
&Alertable=true &EventRiskLevel=1 &EventTypeId=10001 &LogType=1 &RuleName=High-risk deletion operation &<Common request parameters>
```

Sample success responses

```json
 JSON format
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "Rule":{
  "SourceId":1000,
  "CreateTime":1639236844747,
  "LogType":1,
  "Enabled":true,
  "EventTypeId":10001,
  "SourceName":"rds-ss12222",
  "AlertActions":"1",
  "EventRiskLevel":1,
  "Name":"High-risk deletion operation",
  "EventTypeName":"Resource Management event",
  "Alertable":true,
  "Id":1000,
  "Reserved":false
 }
}
```

### DescribeRule

Queries audit rules.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| loud Security r Developer | Manage Guide·API | ment Cent s |  |  |  |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | Description |
| LogType | Integ er | Query | No | 1 | The code of the log type. |
| SourceId | Long | Query | No | 1000 | The ID of the log source. |
| EventType Id | Long | Query | No | 10001 | The type of the audit event. |
| Expressio n | Strin g | Query | No | action INCLUDE "Delete instance" OR action INCLUDE "Delete cluster" OR action INCLUDE "Delete host" | The expression in the audit rule. |
| EventRisk Level | Integ er | Query | No | 1 | The risk level. |
| Alertable | Boole an | Query | No | true | Specifies whether an alert is triggered. |
| Enabled | Boole an | Query | No | true | Specifies whether the rule is enabled. |
| PageSize | Integ er | Query | No | 20 | The number of entries per page. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RuleList | Array | - | The audit rules. |
| -LogType | Integer | 1 | The code of the log type. |
| -EventTypeId | Integer | 10001 | The type of the audit event. |
| -Expression | String | action INCLUDE "Delete instance" OR action INCLUDE "Delete cluster" OR action INCLUDE "Delete host" | The expression in the audit rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| - EventRiskLeve l | Integer | 1 | The risk level. |
| -CreateTime | Long | 1639236844747 | The creation time. |
| -Reserved | Boolean | true | Indicates whether the audit rule is reserved. |
| -Name | String | High-risk deletion operation | The name of the audit rule. |
| - EventTypeNa me | String | Resource Management event | The name of the event type. |
| -Id | Integer | 1000 | The ID of the audit rule. |
| -Alertable | Boolean | true | Indicates whether an alert is triggered. |
| -Enabled | Boolean | true | Indicates whether the rule is enabled. |
| -AlertActions | String | 1 | The alert recipient in the rule. |
| -SourceName | String | rds-ss12222 | The name of the log source. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |
| CurrentPage | Integer | 1 | The page number. |
| PageSize | Integer | 20 | The number of entries per page. |
| TotalCount | Integer | 100 | The total number of entries returned. |

Cloud Security Management Cent Sample requests

```
&<Common request parameters>
```

Sample success responses

```
 JSON format
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | EnableRule | The operation that you want to perform. Set the value to EnableRule . |
| SourceIp | Strin g | Query | No | 192.168.x.x | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|

Cloud Security Management Cent

```json
{
 "RuleList":[
  {
   "CreateTime":1639236844747,
   "LogType":1,
   "EventTypeId":10001,
   "Enabled":true,
   "SourceName":"rds-ss12222",
   "AlertActions":"1",
   "EventRiskLevel":1,
   "Name":"High-risk deletion operation",
   "Expression":"action INCLUDE \"Delete instance\" OR action INCLUDE \"Delete cluster\
" OR action INCLUDE \"Delete host\"",
   "EventTypeName":"Resource Management event",
   "Id":1000,
   "Alertable":true,
   "Reserved":true
  }
```

`],`

```json
 "TotalCount":100,
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "CurrentPage":1
}
```

### EnableRule

Enables an audit rule.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DisableRule | The operation that you want to perform. Set the value to DisableRule . |
| SourceIp | Strin g | Query | No | 192.168.x.x | The source IP address of the request. |
| Id | Integ er | Query | No | 1 | The ID of the audit rule. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

Cloud Security Management Cent Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DisableRule

Disables an audit rule.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DeleteRule | The operation that you want to perform. Set the value to DeleteRule . |
| SourceIp | Strin g | Query | No | 192.168.x.x | The source IP address of the request. |
| Id | Integ er | Query | Yes | 1000 | The ID of the audit rule. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

Cloud Security Management Cent `JSON` format

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DeleteRule

Deletes an audit rule.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

Sample requests

```
&Id=1000 &<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | CreateTask | The operation that you want to perform. Set the value to CreateTask . |
| SourceIp | Strin g | Query | No | 192.168.x.x | The source IP address of the request. |
| Param | Strin g | Query | Yes | {"id":421711} | The query parameters in the JSON format. |
| Type | Integ er | Query | Yes | 1 | The type of the export task. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |
| Task | Struct | - | The created export task. For more information, see the following parameter descriptions. |
| -Result | String | {"url":"https://yund un-auditlog- archive.oss- ***.aliyun.com/OPS /20211224151432 914- e902e5b4/EVENT/O PS-******.zip?} | The result of the export task. |

Cloud Security Management Cent

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### CreateTask

Creates an export task.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| -CreateTime | Long | 1639236844747 | The creation time. |
| -Param | String | {"id":421711} | The query parameters in the JSON format. |
| -Id | Integer | 1000 | The ID of the export task. |
| -Type | Integer | 1 | The type of the export task. |
| -Status | Integer | 3 | The status of the task. Valid values: 1, 2, 3, and 4. The value 1 indicates that the task is being prepared. The value 2 indicates that the task is in progress. The value 3 indicates that the task is successful. The value 4 indicates that the task failed. |

Cloud Security Management Cent Sample requests

```
&Param={"id":421711} &Type=1 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "Task":{
  "Status":3,
  "Type":1,
  "CreateTime":1639236844747,
  "Param":"{\"id\":421711}",
  "Id":1000,
  "Result":"{\"url\":\"https://yundun-auditlog-archive.oss-
***.aliyun.com/OPS/20211224151432914-e902e5b4/EVENT/OPS-******.zip?}"
 },
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeTask

Queries export tasks.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeTask | The operation that you want to perform. Set the value to DescribeTask . |
| SourceIp | Strin g | Query | No | 192.168.x.x | The source IP address of the request. |
| Type | Integ er | Query | No | 1 | The type of the export task. |
| Status | Integ er | Query | No | 1 | The status of the task. Valid values: 1, 2, 3, and 4. The value 1 indicates that the task is being prepared. The value 2 indicates that the task is in progress. The value 3 indicates that the task is successful. The value 4 indicates that the task failed. |
| PageSize | Integ er | Query | No | 20 | The number of entries per page. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TaskList | Array | - | The export tasks. |

Cloud Security Management Cent This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Result | String | {"url":"https://yund un-auditlog- archive.oss-cn- neimeng-env30- d01- a.intra.env30.shug uang.com/OPS/202 11224151432914- e902e5b4/EVENT/O PS- 20211224151432.z ip?} | The result of the export task. |
| -CreateTime | Long | 1639236844747 | The creation time. |
| -Param | String | {"id":421711} | The query parameters in the JSON format. |
| -StartTime | Long | 1639236844747 | The start time. This value is a timestamp. |
| -Id | Integer | 1000 | The ID of the export task. |
| -EndTime | Long | 1639236844747 | The end time. This value is a timestamp. |
| -Type | Integer | 1 | The type of the export task. |
| -Status | Integer | 1 | The status of the task. Valid values: 1, 2, 3, and 4. The value 1 indicates that the task is being prepared. The value 2 indicates that the task is in progress. The value 3 indicates that the task is successful. The value 4 indicates that the task failed. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |
| CurrentPage | Integer | 1 | The page number. |
| PageSize | Integer | 20 | The number of entries per page. |
| TotalCount | Integer | 100 | The total number of entries returned. |

Cloud Security Management Cent Sample requests

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeSetting | The operation that you want to perform. Set the value to DescribeSetting . |
| SourceIp | Strin g | Query | No | 192.168.x.x | The source IP address of the request. |

Cloud Security Management Cent

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "TotalCount":100,
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "CurrentPage":1,
 "TaskList":[
  {
   "Status":1,
   "Type":1,
   "EndTime":1639236844747,
   "CreateTime":1639236844747,
   "Param":"{\"id\":421711}",
   "StartTime":1639236844747,
   "Id":1000,
   "Result":"{\"url\":\"https://yundun-auditlog-archive.oss-cn-neimeng-env30-d01-a.intr
a.env30.shuguang.com/OPS/20211224151432914-e902e5b4/EVENT/OPS-20211224151432.zip?}"
  }
```

]

```
}
```

### DescribeSetting

Queries the system parameter settings of security audit.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| SettingList | Array | - | The system parameter settings. |
| -Name | String | max day alert nu _ _ _ mber | The name of the system parameter. |
| -UpdateTime | Long | 1639236844747 | The last update time. |
| -Remark | String | Maximum number of alerts sent per day | The description of the system parameter. |
| -Id | Integer | 1 | The ID of the system parameter. |
| -Type | Integer | 2 | The data type. |
| -Value | String | -1 | The value of the system parameter. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

Cloud Security Management Cent Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "SettingList":[
  {
   "Type":2,
   "UpdateTime":1639236844747,
   "Value":"-1",
   "Id":1,
   "Name":"max_day_alert_number",
   "Remark":"Maximum number of alerts sent per day"
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### ModifySetting

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | ModifySetting | The operation that you want to perform. Set the value to ModifySetting . |
| SourceIp | Strin g | Query | No | 192.168.x.x | The source IP address of the request. |
| Name | Strin g | Query | Yes | max day alert number _ _ _ | The name of the system parameter. |
| Value | Strin g | Query | Yes | -1 | The value of the system parameter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

Cloud Security Management Cent Modifies the system parameter settings of security audit.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

Queries log types.

### DescribeLogType

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeLogType | The operation that you want to perform. Set the value to DescribeLogType . |
| SourceIp | Strin g | Query | No | 192.168.x.x | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogTypeList | Array | - | The log types. |
| -Remark | String | Platform database | The name of the log type. |
| -Type | Integer | 1 | The code of the log type. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

Cloud Security Management Cent

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeLogSource | The operation that you want to perform. Set the value to DescribeLogSource . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| LogType | Integ er | Query | No | 1 | The code of the log type. |
| Enabled | Boole an | Query | No | true | Specifies whether the log source is enabled. |
| PageSize | Integ er | Query | No | 20 | The number of entries per page. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogSourceList | Array | - | The log sources. |

Cloud Security Management Cent

```json
{
 "LogTypeList":[
  {
   "Type":1,
   "Remark":"Platform database"
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeLogSource

Queries log sources.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| loud Security Ma r Developer Guid | nagement Cent e·APIs |  |  |
|---|---|---|---|
| Parameter | Type | Example | Description |
| -LogType | Integer | 1 | The code of the log type. |
| -Code | String | RDS-scscsc | The code of the log source. |
| -CreateTime | Long | 1639236844747 | The creation time. |
| -Name | String | RDS-scscsc | The name of the log source. |
| -Id | Integer | 1000 | The ID of the log source. |
| -Alertable | Boolean | true | Indicates whether an alert is triggered. |
| -Enabled | Boolean | true | Indicates whether the log source is enabled. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |
| CurrentPage | Integer | 1 | The page number. |
| PageSize | Integer | 20 | The number of entries per page. |
| TotalCount | Integer | 1000 | The total number of entries returned. |

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeLogCountStat | The operation that you want to perform. Set the value to DescribeLogCountSta t . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| StartTime | Strin g | Query | No | 1639725751259 | The beginning of the time range to query. This value is a timestamp. |
| LogTypeLi st | Strin g | Query | No | 1,2,3,4,5 | The code of the log type. Separate multiple codes of log types with commas (,). |

Cloud Security Management Cent

```json
{
 "LogSourceList":[
  {
   "CreateTime":1639236844747,
   "LogType":1,
   "Enabled":true,
   "Id":1000,
   "Alertable":true,
   "Code":"RDS-scscsc",
   "Name":"RDS-scscsc"
  }
```

`],`

```json
 "TotalCount":1000,
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "CurrentPage":1
}
```

### DescribeLogCountStat

Queries raw log statistics.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| EndTime | Strin g | Query | No | 1639725751259 | The end of the time range to query. This value is a timestamp. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StatList | Array | - | The raw log statistics. |
| -StatItemList | Array | - | The raw log data. |
| --Count | Long | 1000 | The number of raw logs. |
| --Time | Long | 1640244151259 | The time at which the statistics were collected. This value is a timestamp. |
| --Capacity | Float | 1000.0 | The storage usage. |
| -LogType | Integer | 1 | The code of the log type. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

Cloud Security Management Cent

**Response parameters**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLogCountStat &<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeLog | The operation that you want to perform. Set the value to DescribeLog . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| LogType | Integ er | Query | No | 1 | The code of the log type. |
| SourceId | Long | Query | No | 1001 | The ID of the log source. |
| Query | Strin g | Query | No | Get | The keyword for the query. |
| StartTime | Long | Query | No | 1639236844747 | The start time. This value is a timestamp. |

Cloud Security Management Cent

```json
{
 "StatList":[
  {
   "LogType":1,
   "StatItemList":[
    {
     "Capacity":1000.0,
     "Time":1640244151259,
     "Count":1000
    }
```

]

```
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeLog

Queries raw logs.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| loud Security r Developer | Manage Guide·API | ment Cent s |  |  |  |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| EndTime | Long | Query | No | 1639236844747 | The end time. This value is a timestamp. |
| PageSize | Integ er | Query | No | 20 | The number of entries per page. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| HistogramList | Array | - | The chart information about the number of raw logs. |
| -Count | Integer | 1000 | The number of raw logs. |
| -StartTime | Long | 1639236844747 | The start time. This value is a timestamp. |
| -EndTime | Long | 1639236844747 | The end time. This value is a timestamp. |
| -Completed | Boolean | true | Indicates whether all raw logs that are generated within the specified time range are returned. If not, the Count parameter shows an estimated value. |
| LogList | Array | - | The raw logs. |
| -ColumnList | Array | - | The log details. |
| --TokenList | Array | - | The tokens. |
| ---Delimit | Boolean | false | Indicates whether the token is a delimiter token. |
| ---Word | String | 012 | The fixed value of the token. |
| --Value | String | 012 | The value of the column. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| --Key | String | value | The name of the column. |
| -Source | String | 1 | The name of the log source. |
| -LogTime | Long | 1640244151259 | The time when the log was generated. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |
| PageSize | Integer | 20 | The number of entries per page. |
| TotalCount | Long | 100 | The total number of entries returned. |
| CurrentPage | Integer | 1 | The page number. |

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeEventRisk | The operation that you want to perform. Set the value to DescribeEventRisk . |

Cloud Security Management Cent

```json
{
 "LogList":[
  {
   "ColumnList":[
    {
     "Value":"012",
     "TokenList":[
      {
       "Word":"012",
       "Delimit":false
      }
```

`],`

```json
     "Key":"value"
    }
```

`],`

```json
   "LogTime":1640244151259,
   "Source":"1"
  }
```

`],`

```json
 "HistogramList":[
  {
   "EndTime":1639236844747,
   "StartTime":1639236844747,
   "Completed":true,
   "Count":1000
  }
```

`],`

```json
 "TotalCount":100,
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "CurrentPage":1
}
```

### DescribeEventRisk

Queries the risk level information about audit events.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EventRiskList | Array | - | The risk levels. |
| -Level | Integer | 0 | The code of the risk level. |
| -Name | String | Global risk | The name of the risk level. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

Cloud Security Management Cent

**Response parameters**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "EventRiskList":[
  {
   "Level":0,
   "Name":"Global risk"
  }
```

]

```
}
```

### DescribeEventRiskStat

Queries audit event statistics by risk level.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeEventRiskStat | The operation that you want to perform. Set the value to DescribeEventRiskSta t . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| StartTime | Strin g | Query | No | 1639725751259 | The start time. This value is a timestamp. |
| LogTypeLi st | Strin g | Query | No | 1,2,3 | The code of the log type. Separate multiple codes of log types with commas (,). |
| EndTime | Strin g | Query | No | 1640244151259 | The end time. This value is a timestamp. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StatList | Array | - | The audit event statistics. |
| -StatItemList | Array | - | The statistical details. |
| -- EventRiskLeve l | Integer | 1 | The risk level. |
| --Count | Integer | 1 | The number of audit events. |
| --Capacity | Integer | 44 | The storage usage. |
| -LogType | Integer | 1 | The code of the log type. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

Cloud Security Management Cent

**Request parameters**

**Response parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RequestId | Strin g | System | Yes | DescribeEventTypeStat | The operation that you want to perform. Set the value to DescribeEventTypeSt at . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| StartTime | Strin g | Query | No | 1639725751259 | The beginning of the time range to query. This value is a timestamp. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEventRiskStat &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "StatList":[
  {
   "LogType":1,
   "StatItemList":[
    {
     "Capacity":44,
     "Count":1,
     "EventRiskLevel":1
    }
```

]

```
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeEventTypeStat

Queries audit event statistics by event type.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Cloud Security r Developer | Manage Guide·API | ment Cent s |  |  |  |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| LogTypeLi st | Strin g | Query | No | 1,2,3,4,5 | The code of the log type. Separate multiple codes of log types with commas (,). |
| EndTime | Strin g | Query | No | 1640244151259 | The end of the time range to query. This value is a timestamp. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StatList | Array | - | The statistics. |
| -Count | Integer | 10001 | The number of audit events. |
| -Name | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | The name of the audit event type. |
| -Reserved | Boolean | true | Indicates whether the event type is reserved in the system. |
| -Id | Integer | 10135 | The ID of the audit event type. |
| -Capacity | Float | 8991.659133 | The storage usage. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

**Response parameters**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEventTypeStat &<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeEventCountStat | The operation that you want to perform. Set the value to DescribeEventCountS tat . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| StartTime | Strin g | Query | No | 1639725751259 | The start time. This value is a timestamp. |
| LogTypeLi st | Strin g | Query | No | 1,2,3 | The code of the log type. Separate multiple codes of log types with commas (,). |
| EndTime | Strin g | Query | No | 1640244151259 | The end time. This value is a timestamp. |

Cloud Security Management Cent

```json
{
 "StatList":[
  {
   "Capacity":8991.659,
   "Count":10001,
   "Id":10135,
   "Name":"EVENT_TYPE_NAME__host__account_create",
   "Reserved":true
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeEventCountStat

Queries audit event statistics.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| StatList | Array | - | The audit event statistics. For more information, see the following parameter description. |
| -StatItemList | Array | - | The audit event statistics. |
| --Count | Integer | 10001 | The number of audit events. |
| --Time | Long | 1639929600000 | The time when the log was generated. |
| --Capacity | Integer | 8991 | The storage usage. |
| -LogType | Integer | 1 | The code of the log type. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEventCountStat &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "StatList":[
  {
   "LogType":1,
   "StatItemList":[
    {
     "Capacity":8991,
     "Time":1639929600000,
     "Count":10001
    }
```

]

```
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeEvent

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeEvent | The operation that you want to perform. Set the value to DescribeEvent . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| lang | Strin g | Query | No | zh | The language of the content within the request and response. Valid values: Valid values: zh and en. The value zh indicates Chinese, and the value en indicates English. |
| LogType | Integ er | Query | No | 1 | The code of the log type. |
| SourceId | Long | Query | No | 1000 | The ID of the log source. |
| EventRisk Level | Integ er | Query | No | 1 | The code of the risk level. |
| Alertable | Boole an | Query | No | true | Specifies whether an alert is triggered. |
| EventType Id | Long | Query | No | 10001 | The ID of the audit event type. |
| StartTime | Long | Query | No | 1639236844747 | The beginning of the time range to query. This value is a timestamp. |

Cloud Security Management Cent Queries audit event details.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| EndTime | Long | Query | No | 1639236844747 | The end of the time range to query. This value is a timestamp. |
| Keyword | Strin g | Query | No | Describe | The keyword for the query. |
| RuleId | Long | Query | No | 1000 | The ID of the audit rule. |
| LogInitiati or | Strin g | Query | No | EQ:Initiator | The initiator. |
| LogTarget | Strin g | Query | No | EQ:Target | The target. |
| LogAction | Strin g | Query | No | EQ:cmd | The operation. |
| LogOutco me | Strin g | Query | No | EQ:result | The result. |
| LogReaso n | Strin g | Query | No | EQ:reason | The reason. |
| PageSize | Integ er | Query | No | 20 | The number of entries per page. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| HistogramList | Array | - | The chart information about the number of audit events. |
| -Count | Integer | 1001 | The number of audit events. |
| -StartTime | Long | 1639236844747 | The beginning of the time range. This value is a timestamp. |
| -EndTime | Long | 1639236844747 | The end of the time range. This value is a timestamp. |

Cloud Security Management Cent

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Completed | Boolean | true | Indicates whether all of the audit events that occurred within the specified time range have been collected. If not, the Count parameter shows an estimated value. |
| EventList | Array | - | The audit events. |
| -LogSha256 | String | 929724b41deb5ad c78764976f0a3971 09f2602ba5c7dcce d2cb26b8d37a97b 5d | The SHA-256 value of the log file. |
| -SourceId | Long | 1000 | The ID of the log source. |
| -LogType | Integer | 1 | The type of the log. |
| - EventRiskLeve l | Integer | 1 | The risk level. |
| -LogContent | String | 929724b41deb5ad c78764976f0a3971 09f2602ba5c7dcce d2cb26b8d37a97b 5d | The log content. |
| -LogMd5 | String | 36c22c2020d4738 81f8b8bbf1c3eaf0 8 | The MD5 hash value of the log file. |
| -LogTime | Long | 1639929600000 | The time at which the log was generated. |
| -EventTypeId | Integer | 1001 | The ID of the audit event type. |
| -CreateTime | Long | 1639236844747 | The creation time. |
| -Receivers | String | 123.qq.com | The alert recipient. |
| - EventTypeNa me | String | Resource Management event | The name of the audit event type. |
| -Id | Long | 1000 | The ID of the audit event. |
| -SourceName | String | rds-ss12222 | The name of the log source. |

Cloud Security Management Cent

| C e | loud Security Ma r Developer Guid | nagement Cent e·APIs |  |  |  |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - EventTypeRes erved | Boolean | true | Indicates whether the event type is reserved in the system. |
| -RuleId | Integer | 1000 | The ID of the audit rule. |
| -LogInitiatior | String | EQ:Initiator | The initiator. |
| -LogTarget | String | EQ:target | The target. |
| -LogAction | String | EQ:cmd | The operation. |
| -LogOutcome | String | EQ:result | The result. |
| -LogReason | String | EQ:reason | The reason. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| CurrentPage | Integer | 1 | The page number. |
| PageSize | Integer | 20 | The number of entries per page. |

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format Cloud Security Management Cent

```json
{
 "HistogramList":[
  {
   "EndTime":1639236844747,
   "StartTime":1639236844747,
   "Completed":true,
   "Count":1001
  }
```

`],`

```json
 "TotalCount":100,
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "EventList":[
  {
   "LogMd5":"36c22c2020d473881f8b8bbf1c3eaf08",
   "SourceId":1000,
   "LogTime":1639929600000,
   "RuleId":1000,
   "EventTypeId":1001,
   "LogAction":"EQ:cmd",
   "LogOutcome":"EQ:result",
   "EventTypeReserved":true,
   "CreateTime":1639236844747,
   "Receivers":"123.qq.com",
   "LogType":1,
   "SourceName":"rds-ss12222",
   "EventRiskLevel":1,
   "LogTarget":"EQ:target",
   "LogInitiatior":"EQ:Initiator",
   "LogSha256":"929724b41deb5adc78764976f0a397109f2602ba5c7dcced2cb26b8d37a97b5d",
   "LogContent":"929724b41deb5adc78764976f0a397109f2602ba5c7dcced2cb26b8d37a97b5d",
   "LogReason":"EQ:reason",
   "EventTypeName":"Resource Management event",
   "Id":1000
  }
```

`],`

```json
 "CurrentPage":1
}
```

### DescribeArchiveCountStat

Queries archived statistics about logs and events.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeArchiveCountSt at | The operation that you want to perform. Set the value to DescribeArchiveCoun tStat . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| StartTime | Strin g | Query | No | 1639725751259 | The start time. This value is a timestamp. |
| LogTypeLi st | Strin g | Query | No | 1,2,3 | The type of the log. Separate multiple log types with commas (,). |
| EndTime | Strin g | Query | No | 1640244151259 | The end time. This value is a timestamp. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StatList | Array | - | The archived statistics. For more information, see the following parameter description. |
| -StatItemList | Array | - | The archiving information. For more information, see the following parameter description. |
| --Count | Integer | 3 | The number of the archives. |
| --Time | Long | 1639929600000 | The time at which the statistics were collected. This value is a timestamp. |
| --Capacity | Float | 6.6 | The storage used for the archives. |
| -LogType | Integer | 1 | The type of the log. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

Cloud Security Management Cent

**Response parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DeleteTask | The operation that you want to perform. Set the value to DeleteTask . |
| SourceIp | Strin g | Query | No | 192.168.x.x | The source IP address of the request. |
| Id | Integ er | Query | Yes | 1000 | The ID of the export task. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeArchiveCountStat &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "StatList":[
  {
   "LogType":1,
   "StatItemList":[
    {
     "Capacity":6.6,
     "Time":1639929600000,
     "Count":3
    }
```

]

```
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DeleteTask

Deletes an export task.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | System | Yes | DescribeArchive | The operation that you want to perform. Set the value to DescribeArchive . |
| SourceIp | Strin g | Query | No | 192.168.XX.XX | The source IP address of the request. |
| LogType | Integ er | Query | No | 1 | The type of the log. |
| StartTime | Strin g | Query | No | 1639725751259 | The beginning of the time range to query. This value is a timestamp. |

Cloud Security Management Cent Sample requests

```
&Id=1000 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"
}
```

### DescribeArchive

Queries the details of archived logs and events.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| EndTime | Strin g | Query | No | 1640244151259 | The end of the time range to query. This value is a timestamp. |
| Type | Integ er | Query | No | 1 | The type of the archive. |
| PageSize | Integ er | Query | No | 20 | The number of entries per page. |
| CurrentPa ge | Integ er | Query | No | 1 | The page number. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ArchiveList | Array | - | The archived data. For more information, see the following parameter description. |
| -LogType | Integer | 1 | The type of the log. |
| -CompactAlg | Integer | 1 | The compression algorithm. |
| -Sha256 | String | 929724b41deb5ad c78764976f0a3971 09f2602ba5c7dcce d2cb26b8d37a97b 5d | The SHA-256 value of the archive file. |
| -CreateTime | Long | 1639236844747 | The creation time. |
| -Count | Integer | 3 | The number of the archives. |
| -Name | String | NETWORK/202112 24153332996- 44a9fc6e/EVENT/N ETWORK- 20211224153332.z ip | The name of the archive file. |
| -Id | Integer | 1000 | The archive ID. |
| -Type | Integer | 1 | The type of the archive. |

Cloud Security Management Cent

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Md5 | String | 36c22c2020d4738 81f8b8bbf1c3eaf0 8 | The MD5 hash value of the archive file. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The request ID. |
| CurrentPage | Integer | 1 | The page number. |
| PageSize | Integer | 20 | The number of entries per page. |
| TotalCount | Integer | 100 | The total number of entries returned. |

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "TotalCount":100,
 "ArchiveList":[
  {
   "Type":1,
   "CompactAlg":1,
   "CreateTime":1639236844747,
   "LogType":1,
   "Count":3,
   "Id":1000,
   "Sha256":"929724b41deb5adc78764976f0a397109f2602ba5c7dcced2cb26b8d37a97b5d",
   "Name":"NETWORK/20211224153332996-44a9fc6e/EVENT/NETWORK-20211224153332.zip",
   "Md5":"36c22c2020d473881f8b8bbf1c3eaf08"
  }
```

`],`

```json
 "RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****",
 "PageSize":20,
 "CurrentPage":1
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeFieldSta tistics | The operation that you want to perform. Set the value to DescribeFieldStatistics. |
| RegionId | String | No | cn-hangzhou | The region ID of the asset. |
| MachineTypes | String | No | ecs | The types of the assets that you want to query. Separate multiple types with commas (,). If no asset types are specified, all types of assets are returned. Valid values: 0: Elastic Compute Service (ECS) instance 1: Server Load Balancer (SLB) instance 2: NAT gateway 3: ApsaraDB RDS database 4: ApsaraDB for MongoDB database 6: container image 7: container |

| Parameter | Type | Example | Description |
|---|---|---|---|
| GroupedFields | Struct |  | The asset information. |
| AliYunInstance Count | Integer | 10 | The number of instances that are provided by Alibaba Cloud. |

Cloud Security Management Cent

## Threat Detection Service

**(TDS)**

### Asset management

#### DescribeFieldStatistics

Queries assets.

**Request parameters**

**Response parameters**

| ExposedInstan ceCount | Integer | 10 | The number of instances that are exposed on the Internet. |
|---|---|---|---|
| GeneralAssetC ount | Integer | 10 | The number of general instances. |
| GroupCount | Integer | 10 | The number of groups. |
| IdcInstanceCo unt | Integer | 10 | The number of servers outside the cloud. |
| ImportantAsse tCount | Integer | 10 | The number of important instances. |
| InstanceCount | Integer | 10 | The number of instances. |
| InstanceSyncT askCount | Integer | 10 | The number of synchronization tasks. |
| NewInstanceC ount | Integer | 10 | The number of new instances. |
| NotRunningSta tusCount | Integer | 10 | The number of servers that are not running. |
| OfflineInstanc eCount | Integer | 10 | The number of offline instances. |
| ProviderCount | Integer | 10 | The number of service providers. |
| RegionCount | Integer | 10 | The number of regions. |
| RiskInstanceC ount | Integer | 10 | The number of vulnerable instances. |
| TencentInstan ceCount | Integer | 10 | The number of instances that are provided by Tencent Cloud. |
| TestAssetCoun t | Integer | 10 | The number of test instances. |
| UnprotectedIn stanceCount | Integer | 10 | The number of unprotected instances. |
| VpcCount | Integer | 10 | The number of virtual private clouds (VPCs). |
| RequestId | String | 7E06****9-D5EF- 4220-9471- ***5E92719F | The ID of the request. |

Cloud Security Management Cent Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeFieldStatistics &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7E06****9-D5EF-4220-9471-***5E92719F</RequestId> <GroupedFields>
    <ProviderCount>10</ProviderCount>
    <ExposedInstanceCount>10</ExposedInstanceCount>
    <GroupCount>10</GroupCount>
    <InstanceSyncTaskCount>10</InstanceSyncTaskCount>
    <TencentInstanceCount>10</TencentInstanceCount>
    <RiskInstanceCount>10</RiskInstanceCount>
    <ImportantAssetCount>10</ImportantAssetCount>
    <IdcInstanceCount>10</IdcInstanceCount>
    <GeneralAssetCount>10</GeneralAssetCount>
    <TestAssetCount>10</TestAssetCount>
    <UnprotectedInstanceCount>10</UnprotectedInstanceCount>
    <InstanceCount>10</InstanceCount>
    <OfflineInstanceCount>10</OfflineInstanceCount>
    <VpcCount>10</VpcCount>
    <AliYunInstanceCount>10</AliYunInstanceCount>
    <RegionCount>10</RegionCount>
    <NotRunningStatusCount>10</NotRunningStatusCount>
    <NewInstanceCount>10</NewInstanceCount>
</GroupedFields>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeGroupe dTags | The operation that you want to perform. Set the value to DescribeGroupedTags. |
| MachineTypes | String | No | 0 | The types of the assets whose tags you want to query. Separate multiple types with commas (,). Valid values: 0: Elastic Compute Service (ECS) instance 1: Server Load Balancer (SLB) instance 2: NAT gateway 3: ApsaraDB RDS database 4: ApsaraDB for MongoDB database 6: container image 7: container |

Cloud Security Management Cent

```json
{
    "RequestId": "7E06****9-D5EF-4220-9471-***5E92719F",
    "GroupedFields": {
        "ProviderCount": 10,
        "ExposedInstanceCount": 10,
        "GroupCount": 10,
        "InstanceSyncTaskCount": 10,
        "TencentInstanceCount": 10,
        "RiskInstanceCount": 10,
        "ImportantAssetCount": 10,
        "IdcInstanceCount": 10,
        "GeneralAssetCount": 10,
        "TestAssetCount": 10,
        "UnprotectedInstanceCount": 10,
        "InstanceCount": 10,
        "OfflineInstanceCount": 10,
        "VpcCount": 10,
        "AliYunInstanceCount": 10,
        "RegionCount": 10,
        "NotRunningStatusCount": 10,
        "NewInstanceCount": 10
    }
}
```

#### DescribeGroupedTags

Queries the statistics of asset tags.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 2 | The number of entries returned on the current page. |
| GroupedFileds | Array of GroupedFiled |  | An array that consists of the statistics of the asset tags. |
| Count | String | 2 | The number of assets to which a tag is attached. |
| Name | String | test | The name of the tag. |
| TagId | Integer | 5 | The ID of the tag. |
| HttpStatusCod e | Integer | 1 | This parameter is deprecated. |
| RequestId | String | 7E0618A9-D5EF- ***-9471- C42B5E92719F | The ID of the request. |
| Success | Boolean | true | This parameter is deprecated. |

Cloud Security Management Cent

**Response parameters**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGroupedTags &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7E0618A9-D5EF-***-9471-C42B5E92719F</RequestId> <HttpStatusCode>1</HttpStatusCode> <GroupedFileds>
    <TagId>5</TagId>
    <Count>2</Count>
    <Name>test</Name>
</GroupedFileds> <Count>2</Count> <Success>true</Success>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAllGrou ps | The operation that you want to perform. Set the value to DescribeAllGroups. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 1 | The number of entries returned on the current page. |
| Groups | Array of Group |  | An array that consists of the information about server groups. |
| GroupFlag | Integer | 1 | The flag of the server group. Valid values: 0: default group 1: other groups |
| GroupId | Integer | 3 | The ID of the server group. |

Cloud Security Management Cent

```json
{
    "RequestId": "7E0618A9-D5EF-***-9471-C42B5E92719F",
    "HttpStatusCode": 1,
    "GroupedFileds": {
        "TagId": 5,
        "Count": 2,
        "Name": "test"
    },
    "Count": 2,
    "Success": true
}
```

#### DescribeAllGroups

Queries the information about server groups.

**Request parameters**

**Response parameters**

| GroupName | String | Group name | The name of the server group. |
|---|---|---|---|
| RequestId | String | 7E0618A9-****- 4220-9471- C42B5E92719F | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeInstanc eStatistics | The operation that you want to perform. Set the value to DescribeInstanceStatistics. |

Cloud Security Management Cent Sample requests

```
&<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7E0618A9-****-4220-9471-C42B5E92719F</RequestId> <Groups>
    <GroupName>Group name</GroupName>
    <GroupFlag>1</GroupFlag>
    <GroupId>3</GroupId>
</Groups> <Count>1</Count>
```

`JSON` format

```json
{
    "RequestId": "7E0618A9-****-4220-9471-C42B5E92719F",
    "Groups": {
        "GroupName": "Group name",
        "GroupFlag": 1,
        "GroupId": 3
    },
    "Count": 1
}
```

#### DescribeInstanceStatistics

Queries the risk information about assets.

**Request parameters**

| From | String | Yes | sas | The source of data. Set the value to sas. |
|---|---|---|---|---|
| Uuid | String | Yes | a51cec37-ed73- 4c53-b467-*** | The UUIDs of the assets. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array of Data |  | An array that consists of the risk information about assets. |
| Account | Integer | 1 | The number of logon accounts. |
| AppNum | Integer | 0 | The number of application vulnerabilities. |
| CmsNum | Integer | 2 | The number of Web-CMS vulnerabilities. |
| CveNum | Integer | 1 | The number of Linux software vulnerabilities. |
| EmgNum | Integer | 0 | The number of urgent vulnerabilities. |
| ExposedCount | Integer | 1 | This parameter is deprecated. |
| Health | Integer | 1 | The number of risk items. |
| ScaNum | Integer | 5 | The number of vulnerabilities that are detected based on software component analysis. |
| Suspicious | Integer | 2 | The number of alerts. |

Cloud Security Management Cent

**Response parameters**

| SysNum | Integer | 1 | The number of Windows system vulnerabilities. |
|---|---|---|---|
| Trojan | Integer | 1 | The number of trojans. |
| Uuid | String | us1233****** | The UUID of the asset. |
| Vul | Integer | 4 | The total number of vulnerabilities. Note Total number of vulnerabilities = CveNum + EmgNum + SysNum + CmsNum + AppNum. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeInstanceStatistics &From=sas &Uuid=a51cec37-ed73-4c53-b467-*** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</RequestId> <Data>
    <Account>1</Account>
    <Uuid>us1233******</Uuid>
    <Suspicious>2</Suspicious>
    <Health>1</Health>
    <CveNum>1</CveNum>
    <ExposedCount>1</ExposedCount>
    <ScaNum>5</ScaNum>
    <CmsNum>2</CmsNum>
    <Trojan>1</Trojan>
    <SysNum>1</SysNum>
    <EmgNum>0</EmgNum>
    <AppNum>0</AppNum>
    <Vul>4</Vul>
</Data>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCloudPr oductFieldStatist ics | The operation that you want to perform. Set the value to DescribeCloudProductFieldStatis tics. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| GroupedFields | Struct |  | The statistics of cloud services. |
| CategoryCount | String | [{"MachineType":1 ,"Count":11}] | The statistics on the numbers of assets of different types. MachineType indicates the type of the assets. Count indicates the number of assets that belong to the type. Valid values of MachineType: 1: Server Load Balancer (SLB) instance 2: NAT gateway 3: ApsaraDB RDS database 4: ApsaraDB for MongoDB instance |

Cloud Security Management Cent

```json
{
    "RequestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
    "Data": {
        "Account": 1,
        "Uuid": "us1233******",
        "Suspicious": 2,
        "Health": 1,
        "CveNum": 1,
        "ExposedCount": 1,
        "ScaNum": 5,
        "CmsNum": 2,
        "Trojan": 1,
        "SysNum": 1,
        "EmgNum": 0,
        "AppNum": 0,
        "Vul": 4
    }
}
```

#### DescribeCloudProductFieldStatistics

Queries the statistics of cloud services.

**Request parameters**

**Response parameters**

| InstanceCount | Integer | 100 | The number of instances. |
|---|---|---|---|
| RiskInstanceC ount | Integer | 90 | The number of vulnerable instances. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCloudC enterInstances | The operation that you want to perform. Set the value to DescribeCloudCenterInstances. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCloudProductFieldStatistics &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</RequestId> <GroupedFields>
    <InstanceCount>100</InstanceCount>
    <CategoryCount>[{"MachineType":1,"Count":11}]</CategoryCount>
    <RiskInstanceCount>90</RiskInstanceCount>
</GroupedFields>
```

`JSON` format

```json
{
    "RequestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
    "GroupedFields": {
        "InstanceCount": 100,
        "CategoryCount": "[{\"MachineType\":1,\"Count\":11}]",
        "RiskInstanceCount": 90
    }
}
```

#### DescribeCloudCenterInstances

Queries the asset information on the Assets page, such as the name and region of an asset.

**Request parameters**

| RegionId | String | No | cn-demo-***-*** | The ID of the region. |
|---|---|---|---|---|
| Criteria | String | No | [{\"name\":\"risk Status\",\"value\ ":\"YES\"}, {\"name\":\"inte rnetIp\",\"value\" :\"1.2.3.4\"}] | The search conditions. Note Supported search conditions include the instance ID, instance name, virtual private cloud (VPC) ID, region, and public IP address. You can call the DescribeCriteria operation to query the supported search conditions. Set the value in the following format: [{\"name\":\"Name of condition 1\",\"value\":\"Value of condition 1\"}, {\"name\":\"Name of condition 2\",\"value\":\"Value of condition 2\"},{},...] |
| MachineTypes | String | No | 0 | The type of the asset that you want to query. Valid values: 0: Elastic Compute Service (ECS) instance 1: Server Load Balancer (SLB) instance 2: NAT gateway 3: ApsaraDB RDS database 4: ApsaraDB for MongoDB database 6: container image 7: container |
| LogicalExp | String | No | OR | The logical relationship among multiple search conditions. Valid values: OR: The logical relationship among multiple search conditions is OR. AND: The logical relationship among multiple search conditions is AND. |

Cloud Security Management Cent

| NoPage | Boolean | No | true | Specifies whether to enable paged query. Valid values: true: yes false: no |
|---|---|---|---|---|
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| Importance | Integer | No | 1 | This parameter is deprecated. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Instances | Array of Instance |  | An array that consists of the details of the asset. |
| AlarmStatus | String | NO | Indicates whether alerts are triggered for the asset. Valid values: YES NO |
| AssetType | String | ecs | The type of the asset. |
| AutoSnapshots Level | Integer | 1 | This parameter is deprecated. |
| ClientStatus | String | online | Indicates whether the asset is protected by the agent. Valid values: online: The asset is protected by the agent. offline: The asset is not protected by the agent. pause: The agent suspends protection for the asset. |
| ClientVersion | String | 11 11 _ | The version of the agent. |
| ClusterId | String | 16392368***** | The ID of the cluster. |
| ClusterName | String | demo-cluster | The name of the cluster. |

Cloud Security Management Cent

**Response parameters**

| CreatedTime | Long | 1609988137000 | The time when the asset was created. The value is a UNIX timestamp. Unit: milliseconds. |
|---|---|---|---|
| ExposedCount | Integer | 5 | The number of vulnerabilities that are detected on the asset. |
| ExposedStatus | Integer | 0 | Indicates whether the asset is exposed on the Internet. Valid values: 0: no 1: yes |
| Flag | Integer | 1 | This parameter is deprecated. |
| GroupId | String | 3 | The ID of the group. |
| HcStatus | String | NO | Indicates whether baseline risks are detected on the asset. Valid values: YES NO |
| HealthCheckC ount | Integer | 0 | The number of risk items. |
| Importance | Integer | 1 | This parameter is deprecated. |
| InstanceId | String | i-m5*** | The ID of the instance. |
| InstanceName | String | yztest-l*** | The name of the instance. |
| InternetIp | String | 47.100.XX.XX | The public IP address. |
| IntranetIp | String | 192.168.XX.XX | The private IP address. |
| Ip | String | 192.168.XX.XX | The IP address that is displayed for the asset. If the asset has a public IP address, the public IP address is returned. Otherwise, the private IP address is returned. |
| Os | String | Linux | The operating system. |
| OsName | String | CentOS 7.6 64-bit | The name of the operating system. |

Cloud Security Management Cent

| PodCount | Integer | 1 | The number of pods. |
|---|---|---|---|
| ProviderAzId | Long | 1 | This parameter is deprecated. |
| ProviderAzNa me | String | None | This parameter is deprecated. |
| ProviderId | Long | 1 | This parameter is deprecated. |
| ProviderName | String | None | This parameter is deprecated. |
| ProviderRegio nId | Long | 1 | This parameter is deprecated. |
| ProviderRegio nName | String | None | This parameter is deprecated. |
| Region | String | cn-demo-***-*** | The region. |
| RegionId | String | cn-demo-***-*** | The ID of the region. |
| RegionName | String | China (Hangzhou) | The name of the region. |
| RiskCount | String | {} | The details of risks. |
| RiskStatus | String | NO | Indicates whether risks are detected on the asset. Valid values: YES NO |
| SafeEventCou nt | Integer | 5 | The number of alerts that are generated for the asset. |
| Status | String | Running | The status of the asset. Valid values: Running: The asset is running. notRunning: The asset is stopped. |
| Tag | String | InternetIp | The tag that is added to the asset. |
| Uuid | String | c9107c04-942f- 40c1-981a-f1c1*** | The UUID of the asset. |
| VpcInstanceId | String | classic | The ID of the VPC to which the asset belongs. |

Cloud Security Management Cent

| VulCount | Integer | 2 | The number of vulnerabilities that are detected on the asset. |
|---|---|---|---|
| VulStatus | String | YES | Indicates whether the asset is exposed to vulnerabilities. Valid values: YES NO |
| WeakPassword Count | Integer | 2 | The number of weak passwords. |
| WeakPassword Status | String | YES | Indicates whether weak passwords are detected on the asset. Valid values: YES NO |
| PageInfo | Struct |  | The pagination information. |
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 50 | The total number of entries returned. |
| RequestId | String | 32A73759-4C0F- 4801-****- 901223ACEE9A | The ID of the request. |
| Success | Boolean | true | Indicates whether the request is successful. Valid values: true: yes false: no |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCloudCenterInstances &<Common request parameters>
```

Sample success responses `XML` format Cloud Security Management Cent

```xml
<Instances>
    <ProviderId>1</ProviderId>
    <ProviderAzName>None</ProviderAzName>
    <CreatedTime>1609988137000</CreatedTime>
    <Os>Linux</Os>
    <VulStatus>YES</VulStatus>
    <ExposedCount>5</ExposedCount>
    <Ip>192.168.XX.XX</Ip>
    <ProviderRegionName>None</ProviderRegionName>
    <ClientVersion>11_11</ClientVersion>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <RiskCount>{}</RiskCount>
    <PodCount>1</PodCount>
    <Importance>1</Importance>
    <AutoSnapshotsLevel>1</AutoSnapshotsLevel>
    <ProviderRegionId>1</ProviderRegionId>
    <InternetIp>47.100.XX.XX</InternetIp>
    <RegionName>China (Hangzhou)</RegionName>
    <ClusterName>demo-cluster</ClusterName>
    <ExposedStatus>0</ExposedStatus>
    <Status>Running</Status>
    <ClientStatus>online</ClientStatus>
    <SafeEventCount>5</SafeEventCount>
    <ClusterId>16392368*****</ClusterId>
    <InstanceId>i-m5***</InstanceId>
    <WeakPasswordCount>2</WeakPasswordCount>
    <OsName>CentOS 7.6 64-bit</OsName>
    <HealthCheckCount>0</HealthCheckCount>
    <ProviderAzId>1</ProviderAzId>
    <WeakPasswordStatus>YES</WeakPasswordStatus>
    <RiskStatus>NO</RiskStatus>
    <Flag>0</Flag>
    <GroupId>3</GroupId>
    <VulCount>2</VulCount>
    <InstanceName>yztest-l***</InstanceName>
    <ProviderName>None</ProviderName>
    <AssetType>ecs</AssetType>
    <Uuid>c9107c04-942f-40c1-981a-f1c1***</Uuid>
    <AlarmStatus>NO</AlarmStatus>
    <Region>cn-demo-***-***</Region>
    <VpcInstanceId>classic</VpcInstanceId>
    <RegionId>cn-demo-***-***</RegionId>
    <Tag>InternetIp</Tag>
    <HcStatus>NO</HcStatus>
</Instances> <PageInfo>
    <TotalCount>50</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>10</Count>
</PageInfo> <RequestId>32A73759-4C0F-4801-****-901223ACEE9A</RequestId> <Success>true</Success>
```

Cloud Security Management Cent `JSON` format

```json
{
    "Instances": {
        "ProviderId": 1,
        "ProviderAzName": "None",
        "CreatedTime": 1609988137000,
        "Os": "Linux",
        "VulStatus": "YES",
        "ExposedCount": 5,
        "Ip": "192.168.XX.XX",
        "ProviderRegionName": "None",
        "ClientVersion": "11_11",
        "IntranetIp": "192.168.XX.XX",
        "RiskCount": "{}",
        "PodCount": 1,
        "Importance": 1,
        "AutoSnapshotsLevel": 1,
        "ProviderRegionId": 1,
        "InternetIp": "47.100.XX.XX",
        "RegionName": "China (Hangzhou)",
        "ClusterName": "demo-cluster",
        "ExposedStatus": 0,
        "Status": "Running",
        "ClientStatus": "online",
        "SafeEventCount": 5,
        "ClusterId": "16392368*****",
        "InstanceId": "i-m5***",
        "WeakPasswordCount": 2,
        "OsName": "CentOS 7.6 64bit",
        "HealthCheckCount": 0,
        "ProviderAzId": 1,
        "WeakPasswordStatus": "YES",
        "RiskStatus": "NO",
        "Flag": 0,
        "GroupId": 3,
        "VulCount": 2,
        "InstanceName": "yztest-l***",
        "ProviderName": "None",
        "AssetType": "ecs",
        "Uuid": "c9107c04-942f-40c1-981a-f1c1***",
        "AlarmStatus": "NO",
        "Region": "cn-demo-***-***",
        "VpcInstanceId": "classic",
        "RegionId": "cn-demo-***-***",
        "Tag": "InternetIp",
        "HcStatus": "NO"
    },
    "PageInfo": {
        "TotalCount": 50,
        "PageSize": 20,
        "CurrentPage": 1,
        "Count": 10
    },
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSumma ryInfo | The operation that you want to perform. Set the value to DescribeSummaryInfo. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| ResourceDirecto ryAccountId | String | No | None | This parameter is deprecated. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AegisClientOffl ineCount | Integer | 12 | The number of unprotected assets. |
| AegisClientOnl ineCount | Integer | 127 | The number of protected assets. |
| RequestId | String | D40198E1-6EA8- 482E-****- D9573D75C0CA | The ID of the request. |

Cloud Security Management Cent

```json
    "RequestId": "32A73759-4C0F-4801-****-901223ACEE9A",
    "Success": true
}
```

#### DescribeSummaryInfo

Queries the security information about assets, such as the security score of your assets, the number of protected assets, and the number of unprotected assets.

**Request parameters**

**Response parameters**

| SecurityScore | Integer | 44 | The security score of your assets. Valid values: 95 to 100: The assets are secure. 85 to 94: The assets are exposed to a few security risks. We recommend that you reinforce your security system at the earliest opportunity. 70 to 84: The assets are exposed to a number of security risks. We recommend that you reinforce your security system at the earliest opportunity. 69 or lower: The current security system is unable to protect the asset against attacker intrusions. We recommend that you reinforce your security system at the earliest opportunity. |
|---|---|---|---|
| Success | Boolean | true | This parameter is deprecated. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSummaryInfo &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AegisClientOnlineCount>127</AegisClientOnlineCount> <RequestId>D40198E1-6EA8-482E-****-D9573D75C0CA</RequestId> <AegisClientOfflineCount>12</AegisClientOfflineCount> <SecurityScore>44</SecurityScore> <Success>true</Success>
```

`JSON` format

```json
{
    "AegisClientOnlineCount": 127,
    "RequestId": "D40198E1-6EA8-482E-****-D9573D75C0CA",
    "AegisClientOfflineCount": 12,
    "SecurityScore": 44,
    "Success": true
}
```

### Secure score

#### DescribeSecureSuggestion

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecure Suggestion | The operation that you want to perform. Set the value to DescribeSecureSuggestion. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F35F45B0-5D6B- ****-BE02- A62D0760E840 | The ID of the request. |
| Suggestions | Array of Suggestion |  | An array that consists of the suggestions. |
| Detail | Array of Detail |  | An array that consists of the details about the suggestions. |
| Description | String | You have four ApsaraDB RDS instances at risk. | The description of the suggestion. |
| SubType | String | CLOUD HC RDS _ _ | The sub-type of the unhandled risk. |
| Title | String | The check on security policies of ApsaraDB RDS instances has failed. The instances are at risk | The name of the unhandled risk. |
| Points | Integer | 40 | The penalty point of each item. |

Cloud Security Management Cent Queries suggestions on how to handle the security risks that affect the security score.

**Request parameters**

**Response parameters**

| SuggestType | String | SS ALARM _ | The type of the unhandled risk. Valid values: SS REINFORCE: Key features, such as _ the antivirus feature, are not configured. SS ALARM: unhandled alerts. _ SS VUL: unfixed vulnerabilities. _ SS HC: baseline risks. _ SS AK: AccessKey pair leaks. _ SS CLOUD HC: configuration risks in _ _ Alibaba Cloud services. OTHER: other risks. |
|---|---|---|---|
| TotalCount | Integer | 15 | The total number of entries returned. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSecureSuggestion &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Suggestions>
    <Points>40</Points>
    <SuggestType>SS_ALARM</SuggestType>
    <Detail>
        <SubType>CLOUD_HC_RDS</SubType>
        <Description>You have four ApsaraDB RDS instances at risk.</Description>
        <Title>The check on security policies of ApsaraDB RDS instances has failed. The
instances are at risk</Title>
    </Detail>
</Suggestions> <TotalCount>15</TotalCount> <RequestId>F35F45B0-5D6B-****-BE02-A62D0760E840</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlarmE ventList | The operation that you want to perform. Set the value to DescribeAlarmEventList. |
| CurrentPage | Integer | Yes | 1 | The number of the page to return. |
| From | String | Yes | sas | The ID of the request source. Set the value to sas. |
| PageSize | String | Yes | 20 | The number of entries to return on each page. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

Cloud Security Management Cent

```json
{
    "Suggestions": {
        "Points": 40,
        "SuggestType": "SS_ALARM",
        "Detail": {
            "SubType": "CLOUD_HC_RDS",
            "Description": "You have four ApsaraDB RDS instances at risk.",
            "Title": "The check on security policies of ApsaraDB RDS instances has fail
ed. The instances are at risk"
        }
    },
    "TotalCount": 15,
    "RequestId": "F35F45B0-5D6B-****-BE02-A62D0760E840"
}
```

### Security alerts

#### DescribeAlarmEventList

Queries alert events on the Alerts page. An alert event consists of an alert and exceptions. Each alert event is associated with multiple exceptions.

**Request parameters**

| Dealed | String | No | Y | The status of the alert event. Valid values: N: unhandled Y: handled |
|---|---|---|---|---|
| Levels | String | No | serious | The severities of the alert events. Separate multiple severities with commas (,). Valid values: serious suspicious remind |
| Remark | String | No | database server _ | The name of the alert, or the asset information. |
| GroupId | String | No | tst*** | The group ID of the affected asset. |
| AlarmEventNam e | String | No | DDoS trojan | The name of the alert event. |
| AlarmEventType | String | No | Malicious process | The type of the alert event. |
| UniqueInfo | String | No | asdasjhdk**** | The unique identifier of the alert event. |

Cloud Security Management Cent

| OperateErrorCod eList.N | RepeatL ist | No | ignore. Success | The handling result code of the alert event. Set the value in the following format: Operation type.Operation result code. Operation types include: Common: performs common operations. deal: handles the alert. ignore: ignores the alert. offline handled: marks the alert _ as handled. mark mis info: adds the alerts to _ _ the whitelist. rm mark mis info: removes the _ _ _ alerts from the whitelist. quara: quarantines the source file of the malicious process. kill and quara: terminates the _ _ malicious process and quarantines the source file. kill virus: deletes the source file _ of the malicious process. block ip: blocks the source file of _ the malicious process. manual handled: manually _ handles the alert. Operation result codes include: Success: The operation is successful. Failure: The operation fails. AgentOffline: The agent is offline. |
|---|---|---|---|---|
| ClusterId | String | No | dasdaS****** | The ID of the cluster. |
| ContainerFieldN ame | String | No | containerId | The key that is used to query the container. |
| ContainerFieldV alue | String | No | sadskdjhaskjdha sd***** | The value that is used to query the container. |
| TargetType | String | No | containerId | The container that matches both the value of ContainerFieldName and the value of ContainerFieldValue. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |  | The pagination information. |

Cloud Security Management Cent

**Response parameters**

| Count | Integer | 1 | The total number of returned pages. |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| RequestId | String | 28267723-D857- 4DD8-****- 013100000000 | The ID of the request. |
| SuspEvents | Array of SuspEvents |  | An array that consists of the information about the alert event. |
| AlarmEventNa me | String | Execution of malicious commands | The name of the alert event. |
| AlarmEventNa meOriginal | String | Precise defense against malicious commands | The original parent name of the alert event. |
| AlarmEventTy pe | String | Suspicious process | The type of the alert event. |
| AlarmUniqueIn fo | String | 8df9******f4211fbf 756ef***** | The ID of the alert event. |
| AppName | String | app1 | The name of the application. |
| CanBeDealOnL ine | Boolean | true | Indicates whether the online processing of the alert event is supported, such as quarantining the source file of the malicious process, adding the alert event to the whitelist, and ignoring the alert event. Valid values: true: yes false: no |
| CanCancelFaul t | Boolean | false | Indicates whether you can cancel marking the alert as a false positive. Valid values: true: yes false: no |

Cloud Security Management Cent

| ContainHwMod e | Boolean | false | Indicates whether network protection is enabled. Valid values: true: yes false: no |
|---|---|---|---|
| ContainerId | String | sadjadash*** | The ID of the container. |
| ContainerImag eId | String | cri-asdaks***** | The ID of the image to which the container belongs. |
| ContainerImag eName | String | centos1 | The name of the image to which the container belongs. |
| DataSource | String | aegis *** _ | The source of data. |
| Dealed | Boolean | false | Indicates whether the alert is handled. Valid values: true: yes false: no |
| Description | String | After an attacker accesses a server, the attacker may import malicious shell scripts into scheduled tasks to keep malicious programs running. The scheduled tasks include crontab and systemd. | The description of the alert event. |
| EndTime | Long | 1543740301000 | The end time of the alert event. The value is a UNIX timestamp. Unit: milliseconds. |
| GmtModified | Long | 1569235879000 | The time when the alert was last triggered. The value is a UNIX timestamp. Unit: milliseconds. |
| HasTraceInfo | Boolean | true | Indicates whether the alert has tracing information. Valid values: true: yes false: no |
| InstanceId | String | i-e*** | The ID of the affected asset. |
| InstanceName | String | Test server | The name of the affected asset. |

Cloud Security Management Cent

| InternetIp | String | 47.100.XX.XX | The public IP address of the affected asset. |
|---|---|---|---|
| IntranetIp | String | 192.168.XX.XX | The private IP address of the affected asset. |
| K8sClusterId | String | cb9218d50728c47 0fb7dfbc16***** | The ID of the Kubernetes cluster. |
| K8sClusterNa me | String | cqqtesttest | The name of the Kubernetes cluster. |
| K8sNamespac e | String | kube-system | The namespace of the Kubernetes cluster. |
| K8sNodeId | String | i-km100o6qy****** | The ID of the node in the Kubernetes cluster. |
| K8sNodeName | String | node1 | The name of the node in the Kubernetes cluster. |
| K8sPodName | String | podname1 | The pod name of the Kubernetes cluster. |
| Level | String | serious | The severity of the alert event. Valid values: serious suspicious remind |
| OperateErrorC ode | String | kill and quara.Suc _ _ cess | The handling result code of the alert event. |
| OperateTime | Long | 1234567890123 | The time when the operation is performed. The value is a UNIX timestamp. Unit: milliseconds. |
| SaleVersion | String | 1 | The edition in which alert event detection can be enabled. Valid values: 0: the Basic edition 1: the Enterprise edition |
| SecurityEventI ds | String | 1 | The IDs of associated exceptions. |

Cloud Security Management Cent

| Solution | String | Check the malicious URLs that are listed in the alert. Check the directory for malicious files. Terminate malicious processes. If you manually run the processes, you can mark them as false positives in the console. | The solution to the alert event. |
|---|---|---|---|
| Stages | String | ["attack entrance"] _ | The phase of the alert event. |
| StartTime | Long | 1543740301000 | The start time of the alert event. The value is a UNIX timestamp. Unit: milliseconds. |
| SuspiciousEve ntCount | Integer | 1 | The number of associated exceptions. |
| Uuid | String | 47900178-885d- 4fa4-9d77-*** | The ID of the associated instance. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlarmEventList &CurrentPage=1 &From=sas &PageSize=20 &<Common request parameters>
```

Sample success responses `XML` format Cloud Security Management Cent

```xml
<PageInfo>
    <TotalCount>1</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>1</Count>
</PageInfo> <RequestId>28267723-D857-4DD8-****-013100000000</RequestId> <SuspEvents>
    <K8sNodeId>i-km100o6qy******</K8sNodeId>
    <Description>After an attacker accesses a server, the attacker may import malicious
shell scripts into scheduled tasks to keep malicious programs running. The scheduled ta sks include crontab and systemd. </Description>
    <K8sNodeName>node1</K8sNodeName>
    <ContainHwMode>false</ContainHwMode>
    <EndTime>1543740301000</EndTime>
    <OperateErrorCode>kill_and_quara.Success</OperateErrorCode>
    <AlarmEventName>Execution of malicious commands</AlarmEventName>
    <SecurityEventIds>1</SecurityEventIds>
    <GmtModified>1569235879000</GmtModified>
    <HasTraceInfo>true</HasTraceInfo>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <K8sClusterId>cb9218d50728c470fb7dfbc16*****</K8sClusterId>
    <AppName>app1</AppName>
    <K8sNamespace>kube-system</K8sNamespace>
    <InternetIp>47.100.XX.XX</InternetIp>
    <ContainerId>sadjadash***</ContainerId>
    <AlarmEventType>Suspicious process</AlarmEventType>
    <Solution>Check the malicious URLs that are listed in the alert. Check the director
y for malicious files. Terminate malicious processes. If you manually run the processes , you can mark them as false positives in the console. </Solution>
    <CanCancelFault>false</CanCancelFault>
    <AlarmEventNameOriginal>Precise defense against malicious
commands</AlarmEventNameOriginal>
    <InstanceId>i-e***</InstanceId>
    <Stages>["attack_entrance"]</Stages>
    <StartTime>1543740301000</StartTime>
    <K8sPodName>podname1</K8sPodName>
    <SaleVersion>1</SaleVersion>
    <Dealed>false</Dealed>
    <ContainerImageId>cri-asdaks*****</ContainerImageId>
    <DataSource>aegis_***</DataSource>
    <InstanceName>Test server</InstanceName>
    <OperateTime>1234567890123</OperateTime>
    <CanBeDealOnLine>true</CanBeDealOnLine>
    <K8sClusterName>cqqtesttest</K8sClusterName>
    <Uuid>47900178-885d-4fa4-9d77-***</Uuid>
    <ContainerImageName>centos1</ContainerImageName>
    <SuspiciousEventCount>1</SuspiciousEventCount>
    <AlarmUniqueInfo>8df9******f4211fbf756ef*****</AlarmUniqueInfo>
    <Level>serious</Level>
</SuspEvents>
```

`JSON` format

| { "PageInfo": { "TotalCount": 1, "PageSize": 20, "CurrentPage": 1, "Count": 1 }, "RequestId": "28267723-D857-4DD8-****-013100000000", "SuspEvents": { "K8sNodeId": "i-km100o6qy******", "Description": "After an attacker accesses a server, the attacker may import ma licious shell scripts into scheduled tasks to keep malicious programs running. The sche duled tasks include crontab and systemd.", "K8sNodeName": "node1", "ContainHwMode": false, "EndTime": 1543740301000, "OperateErrorCode": "kill and quara.Success", _ _ "AlarmEventName": "Execution of malicious commands", "SecurityEventIds": 1, "GmtModified": 1569235879000, "HasTraceInfo": true, "IntranetIp": "192.168.XX.XX", "K8sClusterId": "cb9218d50728c470fb7dfbc16*****", "AppName": "app1", "K8sNamespace": "kube-system", "InternetIp": "47.100.XX.XX", "ContainerId": "sadjadash***", "AlarmEventType": "Suspicious process", "Solution": "Check the malicious URLs that are listed in the alert. Check the d irectory for malicious files. Terminate malicious processes. If you manually run the pr ocesses, you can mark them as false positives in the console.", "CanCancelFault": false, "AlarmEventNameOriginal": "Precise defense against malicious commands", "InstanceId": "i-e***", "Stages": "[\"attack entrance\"]", _ "StartTime": 1543740301000, "K8sPodName": "podname1", "SaleVersion": 1, "Dealed": false, "ContainerImageId": "cri-asdaks*****", "DataSource": "aegis ***", _ "InstanceName": "Test server", "OperateTime": 1234567890123, "CanBeDealOnLine": true, "K8sClusterName": "cqqtesttest", "Uuid": "47900178-885d-4fa4-9d77-***", "ContainerImageName": "centos1", "SuspiciousEventCount": 1, "AlarmUniqueInfo": "8df9******f4211fbf756ef*****", "Level": "serious" } } |  |
|---|---|

Cloud Security Management Cent

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlarmE ventDetail | The operation that you want to perform. Set the value to DescribeAlarmEventDetail. |
| AlarmUniqueInfo | String | Yes | 8df************* *********** | The ID of the alert event. Note To query the details of an alert event, you must specify the ID of the alert event. You can call the DescribeAlarmEventList operation to obtain the ID of the alert event. |
| From | String | Yes | sas | The ID of the request source. Set the value to sas. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |  | The details of the alert event. |
| AlarmEventAli asName | String | Webshell - Webshell file | The alias of the alert type. |

Cloud Security Management Cent

#### DescribeAlarmEventDetail

Queries the details of an alert event. An alert event consists of an alert and exceptions. Each alert event is associated with multiple exceptions.

**Request parameters**

**Response parameters**

| AlarmEventDe sc | String | After an attacker accesses a server, the attacker may import malicious shell scripts into scheduled tasks to keep malicious programs running. The scheduled tasks include crontab and systemd. | The description of the alert event. |
|---|---|---|---|
| AlarmUniqueIn fo | String | asds************ | The ID of the alert event. |
| AppName | String | demo-name | The name of the Kubernetes application. |
| CanBeDealOnL ine | Boolean | false | Indicates whether the online processing of alert events is supported, such as blocking an alert, adding an alert to the whitelist, and ignoring an alert. Valid values: true: yes false: no |
| CanCancelFaul t | Boolean | false | Indicates whether you can cancel marking the alert event as a false positive. Valid values: true: yes false: no |
| CauseDetails | Array of CauseDetail |  | An array that consists of the cause of the alert event, which can be used to trace the alert. |
| Key | String | item | The key of the field that displays the tracing information. |
| Value | Array of Value |  | An array that consists of the value of the field that displays the tracing information. |
| Name | String | Solutions | The name of the field that displays the tracing information. |
| Type | String | html | The format of the field that displays the tracing information. Valid values: html text |

Cloud Security Management Cent

| Value | String | Check for the exploited pages of your web services and vulnerabilities in parameter configuration, and resolve these issues. | The value of the field that displays the tracing information. |
|---|---|---|---|
| ContainHwMod e | Boolean | false | Indicates whether network protection is enabled. Valid values: true: yes false: no |
| ContainerId | String | B4*****-3***-4***- B***-9F******** | The ID of the container. |
| ContainerImag eId | String | docker- pullable://registry.a cs.demo.com/acs/a liyun-demo- controller:demo | The ID of the image to which the container belongs. |
| ContainerImag eName | String | registry.acs.demo. com/acs/aliyun- demo- controller:demo | The name of the image to which the container belongs. |
| DataSource | String | demo *** _ | The source of data. |
| EndTime | Long | 1542366542000 | The end time of the alert event. The value is a UNIX timestamp. Unit: milliseconds. |
| InstanceName | String | worker-k8s-for-cs- cb9****** | The name of the instance. |
| InternetIp | String | 47.100.XX.XX | The public IP address. |
| IntranetIp | String | 192.168.XX.XX | The internal IP address. |
| K8sClusterId | String | cb9218*********** | The ID of the Kubernetes cluster. |
| K8sClusterNa me | String | demo******* | The name of the Kubernetes cluster. |
| K8sNamespac e | String | kube-system | The namespace of the Kubernetes cluster. |
| K8sNodeId | String | i-km10********** | The ID of the node in the Kubernetes cluster. |

Cloud Security Management Cent

| K8sNodeName | String | cn-wulan-env116- d01.i- km10*********** | The name of the node in the Kubernetes cluster. |
|---|---|---|---|
| K8sPodName | String | nginx-ingress- controller-5b******- l4*** | The pod name of the Kubernetes cluster. |
| Level | String | serious | The severity of the alert event. Valid values: serious suspicious remind |
| Solution | String | Check the malicious URLs that are listed in the alert. Check the directory for malicious file downloads. Stop the malicious processes that are running. If you trust the processes, mark the alert as a false positive in the console, and submit a ticket to security engineers. | The solution to the alert event. |
| StartTime | Long | 1542378601000 | The start time of the alert event. The value is a UNIX timestamp. Unit: milliseconds. |
| Type | String | Suspicious network connection | The type of the alert event. |
| Uuid | String | B41******-3***- 4***-B***- 9********* | The UUID of the server. |
| RequestId | String | B41******-3***- 4***-B***- 9********* | The ID of the request. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlarmEventDetail &AlarmUniqueInfo=8df914418f4211fbf756efe7a6f40cbc &From=sas &<Common request parameters>
```

Sample success responses Cloud Security Management Cent `XML` format

```xml
<RequestId>B41******-3***-4***-B***-9*********</RequestId> <Data>
    <K8sNodeId>i-km10**********</K8sNodeId>
    <K8sNodeName>cn-wulan-env116-d01.i-km10***********</K8sNodeName>
    <ContainHwMode>false</ContainHwMode>
    <EndTime>1542366542000</EndTime>
    <IntranetIp>192.168.0.100</IntranetIp>
    <K8sClusterId>cb9218***********</K8sClusterId>
    <AppName>demo-name</AppName>
    <K8sNamespace>kube-system</K8sNamespace>
    <InternetIp>123.123.123.123</InternetIp>
    <ContainerId>B4*****-3***-4***-B***-9F********</ContainerId>
    <AlarmEventDesc>After an attacker accesses a server, the attacker may import malici
ous shell scripts into scheduled tasks to keep malicious programs running. The schedule d tasks include crontab and systemd. </AlarmEventDesc>
    <Solution>Check the malicious URLs that are listed in the alert. Check the director
y for malicious file downloads. Stop the malicious processes that are running. If you t rust the processes, mark the alert as a false positive in the console, and submit a tic ket to security engineers. </Solution>
    <CanCancelFault>false</CanCancelFault>
    <StartTime>1542378601000</StartTime>
    <K8sPodName>nginx-ingress-controller-5b******-l4***</K8sPodName>
    <ContainerImageId>docker-pullable://registry.acs.demo.com/acs/aliyun-demo-
controller:demo</ContainerImageId>
    <DataSource>demo_***</DataSource>
    <InstanceName>worker-k8s-for-cs-cb9******</InstanceName>
    <CanBeDealOnLine>false</CanBeDealOnLine>
    <Type>Suspicious network connection</Type>
    <K8sClusterName>demo*******</K8sClusterName>
    <Uuid>B41******-3***-4***-B***-9*********</Uuid>
    <ContainerImageName>registry.acs.demo.com/acs/aliyun-demo-
controller:demo</ContainerImageName>
    <AlarmUniqueInfo>asds************</AlarmUniqueInfo>
    <AlarmEventAliasName>Webshell - Webshell file</AlarmEventAliasName>
    <Level>serious</Level>
    <CauseDetails>
        <Key>item</Key>
        <Value>
            <Type>html</Type>
            <Value>Check for the exploited pages of your web services and
vulnerabilities in parameter configuration, and resolve these issues. </Value>
            <Name>Solutions</Name>
        </Value>
    </CauseDetails>
</Data>
```

`JSON` format Cloud Security Management Cent

```json
{
    "RequestId": "B41******-3***-4***-B***-9*********",
    "Data": {
        "K8sNodeId": "i-km10**********",
        "K8sNodeName": "cn-wulan-env116-d01.i-km10***********",
        "ContainHwMode": false,
        "EndTime": 1542366542000,
        "IntranetIp": "192.168.0.100",
        "K8sClusterId": "cb9218***********",
        "AppName": "demo-name",
        "K8sNamespace": "kube-system",
        "InternetIp": "123.123.123.123",
        "ContainerId": "B4*****-3***-4***-B***-9F********",
        "AlarmEventDesc": "After an attacker accesses a server, the attacker may import
malicious shell scripts into scheduled tasks to keep malicious programs running. The sc heduled tasks include crontab and systemd.",
        "Solution": "Check the malicious URLs that are listed in the alert. Check the d
irectory for malicious file downloads. Stop the malicious processes that are running. I f you trust the processes, mark the alert as a false positive in the console, and submi t a ticket to security engineers.",
        "CanCancelFault": false,
        "StartTime": 1542378601000,
        "K8sPodName": "nginx-ingress-controller-5b******-l4***",
        "ContainerImageId": "docker-pullable://registry.acs.demo.com/acs/aliyun-demo-co
ntroller:demo",
        "DataSource": "demo_***",
        "InstanceName": "worker-k8s-for-cs-cb9******",
        "CanBeDealOnLine": false,
        "Type": "Suspicious network connection",
        "K8sClusterName": "demo*******",
        "Uuid": "B41******-3***-4***-B***-9*********",
        "ContainerImageName": "registry.acs.demo.com/acs/aliyun-demo-controller:demo",
        "AlarmUniqueInfo": "asds************",
        "AlarmEventAliasName": "Webshell - Webshell file",
        "Level": "serious",
        "CauseDetails": {
            "Key": "item",
            "Value": {
                "Type": "html",
                "Value": "Check for the exploited pages of your web services and
vulnerabilities in parameter configuration, and resolve these issues.",
                "Name": "Solutions"
            }
        }
    }
}
```

#### DescribeSuspEvents

Queries the information about an exception. An alert event consists of an alert and exceptions. Each alert event is associated with multiple exceptions.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSuspEv ents | The operation that you want to perform. Set the value to DescribeSuspEvents. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Dealed | String | No | N | The status of the exception. Valid values: N: unhandled Y: handled |
| Name | String | No | ecs-xxx | The name of the exception or the affected server. Fuzzy match is supported. |
| Levels | String | No | serious | The severity of the exception. Separate multiple severities with commas (,). The following severities are listed in descending order: serious suspicious remind |

Cloud Security Management Cent

**Request parameters**

| ParentEventTyp es | String | No | Webshell | The type of the alert event. Valid values: Suspicious process Webshell Unusual logon Exception Sensitive file tampering Malicious process (cloud threat detection) Suspicious network connection Other Abnormal account Application intrusion event Cloud threat detection Precise defense Application whitelist Persistent webshell Web application threat detection Malicious script Threat intelligence Malicious network activity |
|---|---|---|---|---|
| Remark | String | No | Test server | The IP address or name of the server. |
| Status | String | No | None | This parameter is deprecated. |
| PageSize | String | No | 20 | The number of entries to return on each page. |
| CurrentPage | String | No | 1 | The number of the page to return. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

Cloud Security Management Cent

| AlarmUniqueInfo | String | No | 8df914418f4211 fbf*** | The ID of the alert event to which the exception is related. Note To query the details about the exceptions of an alert event, you must specify the ID of the alert event. You can call the DescribeAlarmEventList operation to query the IDs of alert events. |
|---|---|---|---|---|
| UniqueInfo | String | No | a0************** ******* | The unique information that identifies the exception. |
| From | String | No | sas | The data source of the exception. Set the value to sas. |
| Source | String | No | 47.100.XX.XX | The source IP address of the request. |
| GroupId | Long | No | 1 | The ID of the group. |
| Uuids | String | No | xxxx-xx-xxxx- xxxx-xxxx | The UUIDs of servers. Separate multiple UUIDs with commas (,). |
| OperateErrorCod eList.N | RepeatL ist | No | None | This parameter is deprecated. |
| ClusterId | String | No | 1 | The ID of the cluster. |
| ContainerFieldN ame | String | No | appName1 | The key that is used to query the container. |
| ContainerFieldV alue | String | No | nginx-***- controller | The value that is used to query the container. |
| TargetType | String | No | containerId | The container that matches both the value of ContainerFieldName and the value of ContainerFieldValue. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 1 | The total number of returned pages. |
| CurrentPage | Integer | 1 | The page number of the returned page. |

Cloud Security Management Cent

**Response parameters**

| PageSize | Integer | 20 | The number of entries returned per page. |
|---|---|---|---|
| RequestId | String | 43F670F3-AB40- 4E91-****- C57400000000 | The ID of the request. |
| SuspEvents | Array of WarningSumm ary |  | An array that consists of the information about the exception. |
| Advanced | Boolean | false | Indicates whether the Advanced edition is purchased. Valid values: true: yes false: no |
| AlarmEventNa me | String | DDoS trojan | The name of the alert event. |
| AlarmEventNa meDisplay | String | None | This parameter is deprecated. |
| AlarmEventTy pe | String | Malicious process (cloud threat detection) | The type of the alert event. |
| AlarmEventTy peDisplay | String | None | This parameter is deprecated. |
| AlarmUniqueIn fo | String | 8df914418f*** | The ID of the alert event. |
| AppName | String | demo-name | The name of the Kubernetes application. |
| AutoBreaking | Boolean | false | Indicates whether the exception is automatically blocked. Valid values: true: yes false: no |
| CanBeDealOnL ine | Boolean | true | Indicates whether the online processing of the exception is supported, such as quarantining a file. Valid values: true: yes false: no |
| CanCancelFaul t | Boolean | false | Indicates whether you can cancel marking the alert event as a false positive. Valid values: true: yes false: no |

Cloud Security Management Cent

| ContainHwMod e | Boolean | false | Indicates whether network protection is enabled. Valid values: true: yes false: no |
|---|---|---|---|
| ContainerId | String | B4*****-3***-4***- B***-9F******** | The ID of the container. |
| ContainerImag eId | String | docker- pullable://registry.a cs.***.com/acs/aliy un-**- controller:demo | The ID of the image to which the container belongs. |
| ContainerImag eName | String | registry.acs.demo. com/acs/aliyun-**- controller:demo | The name of the image to which the container belongs. |
| DataSource | String | aegis suspicious * _ _ ** | The source of data. |
| Desc | String | XOR DDoS trojan | The description of the exception. |
| Details | Array of QuaraFile |  | An array that consists of the exception details. |
| InfoType | String | download url _ | The type of the icon. |
| Name | String | Alert description | The name in the exception details. |
| NameDisplay | String | None | This parameter is deprecated. |
| Type | String | html | The format of the exception details. Valid values: text html |
| Value | String | Description | The content in the exception details. |
| ValueDisplay | String | None | This parameter is deprecated. |
| EventNotes | Array of EventNote |  | An array that consists of the remarks. |
| Note | String | Remarks | The content of the remarks. |
| NoteId | Long | 1 | The ID of the remarks. |

Cloud Security Management Cent

| NoteTime | String | 2018-12-12 12:00:00 | The time when the remarks were created. The time is in the yyyy-MM-dd HH:mm:ss format. |
|---|---|---|---|
| EventStatus | Integer | 1 | The status of the exception. Valid values: 1: unhandled 2: ignored 4: confirmed 8: marked as a false positive 16: handling 32: handled 64: expired |
| EventSubType | String | XOR DDoS trojan | The name of the exception. |
| HasTraceInfo | Boolean | false | This parameter is deprecated. |
| Id | Long | 1000 | The ID of the exception. |
| InstanceId | String | i-km10********* | The ID of the instance. |
| InstanceName | String | nginx | The name of the associated instance. |
| InternetIp | String | 47.100.XX.XX | The public IP address of the associated instance. |
| IntranetIp | String | 192.168.XX.XX | The private IP address of the associated instance. |
| K8sClusterId | String | cb9218*********** | The ID of the Kubernetes cluster. |
| K8sClusterNa me | String | demo******* | The name of the Kubernetes cluster. |
| K8sNamespac e | String | kube-**** | The namespace of the Kubernetes cluster. |
| K8sNodeId | String | i-km10********** | The ID of the node in the Kubernetes cluster. |
| K8sNodeName | String | cn-wulan-env116- d01.i- km10*********** | The node name of the Kubernetes cluster. |

Cloud Security Management Cent

| K8sPodName | String | nginx-ingress- controller-5b******- l4*** | The pod name of the Kubernetes cluster. |
|---|---|---|---|
| LastTime | String | 2018-09-26 01:51:01 | The time when the exception was last detected. The time is in the yyyy-MM-dd HH:mm:ss format. |
| LastTimeStam p | Long | 1639236844747 | The time when the exception was last detected. The value is a UNIX timestamp. Unit: milliseconds. |
| Level | String | serious | The severity of the exception. Valid values: serious suspicious remind |
| MarkMisRules | String | ***Trojan file path*****Contain** ** | The advanced whitelist rule. |
| Name | String | Malicious process (cloud threat detection) - XOR DDoS trojan | The complete name of the exception. |
| OccurrenceTi me | String | 2018-09-26 01:51:01 | The time when the exception first occurred. The time is in the yyyy-MM-dd HH:mm:ss format. |
| OccurrenceTi meStamp | Long | 1639236844747 | The time when the exception was first detected. The value is a UNIX timestamp. Unit: milliseconds. |
| OperateErrorC ode | String | quara.Succes | The handling result of the exception. |
| OperateMsg | String | success | The remarks of the exception operation. |
| OperateTime | Long | 1639236844747 | The time when the operation is performed. The value is a UNIX timestamp. Unit: milliseconds. |
| SaleVersion | String | 1 | The edition in which exception detection can be enabled. Valid values: 0: the Basic edition 1: the Enterprise edition |
| SecurityEventI ds | String | None | This parameter is deprecated. |

Cloud Security Management Cent

| Stages | String | [] | The phase of the exception. |
|---|---|---|---|
| UniqueInfo | String | e17e*** | The ID of the exception. |
| Uuid | String | bf6b30d3-eea8- 4924-9f0a-*** | The ID of the associated instance. |
| TotalCount | Integer | 100 | The total number of entries returned. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSuspEvents &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>100</TotalCount> <PageSize>20</PageSize> <RequestId>43F670F3-AB40-4E91-****-C57400000000</RequestId> <CurrentPage>1</CurrentPage> <Count>1</Count> <SuspEvents>
    <K8sNodeId>i-km10**********</K8sNodeId>
    <Advanced>false</Advanced>
    <K8sNodeName>cn-wulan-env116-d01.i-km10***********</K8sNodeName>
    <ContainHwMode>false</ContainHwMode>
    <OperateErrorCode>quara.Succes</OperateErrorCode>
    <AlarmEventName>DDoS trojan</AlarmEventName>
    <SecurityEventIds>None</SecurityEventIds>
    <EventStatus>1</EventStatus>
    <HasTraceInfo>false</HasTraceInfo>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <K8sClusterId>cb9218***********</K8sClusterId>
    <EventSubType>XOR DDoS trojan</EventSubType>
    <AppName>demo-name</AppName>
    <Name>Malicious process (cloud threat detection) - XOR DDoS trojan</Name>
    <K8sNamespace>kube-****</K8sNamespace>
    <Desc>XOR DDoS trojan</Desc>
    <LastTimeStamp>1639236844747</LastTimeStamp>
    <InternetIp>47.100.XX.XX</InternetIp>
    <ContainerId>B4*****-3***-4***-B***-9F********</ContainerId>
    <AlarmEventType>Malicious processes (cloud threat detection)</AlarmEventType>
    <AlarmEventNameDisplay>None</AlarmEventNameDisplay>
    <UniqueInfo>e17e***</UniqueInfo>
    <CanCancelFault>false</CanCancelFault>
    <AlarmEventTypeDisplay>None</AlarmEventTypeDisplay>
    <InstanceId>i-km10*********</InstanceId>
    <Stages>[]</Stages>
```

Cloud Security Management Cent

```xml
    <MarkMisRules>***Trojan file path*****Contain****</MarkMisRules>
    <K8sPodName>nginx-ingress-controller-5b******-l4***</K8sPodName>
    <SaleVersion>1</SaleVersion>
    <ContainerImageId>docker-pullable://registry.acs.***.com/acs/aliyun-**-
controller:demo</ContainerImageId>
    <DataSource>aegis_suspicious_***</DataSource>
    <InstanceName>nginx</InstanceName>
    <OccurrenceTime>2018-09-26 01:51:01</OccurrenceTime>
    <OperateTime>1639236844747</OperateTime>
    <CanBeDealOnLine>true</CanBeDealOnLine>
    <OperateMsg>success</OperateMsg>
    <K8sClusterName>demo*******</K8sClusterName>
    <Uuid>bf6b30d3-eea8-4924-9f0a-***</Uuid>
    <ContainerImageName>registry.acs.demo.com/acs/aliyun-**-
controller:demo</ContainerImageName>
    <AlarmUniqueInfo>8df914418f***</AlarmUniqueInfo>
    <AutoBreaking>false</AutoBreaking>
    <OccurrenceTimeStamp>1639236844747</OccurrenceTimeStamp>
    <Level>serious</Level>
    <Id>1000</Id>
    <LastTime>2018-09-26 01:51:01</LastTime>
    <Details>
        <Type>html</Type>
        <Value>Description</Value>
        <ValueDisplay>None</ValueDisplay>
        <InfoType>download_url</InfoType>
        <NameDisplay>None</NameDisplay>
        <Name>Alert description</Name>
    </Details>
    <EventNotes>
        <NoteId>1</NoteId>
        <Note>Remarks</Note>
        <NoteTime>2018-12-12 12:00:00</NoteTime>
    </EventNotes>
</SuspEvents>
```

`JSON` format

```json
{
    "TotalCount": 100,
    "PageSize": 20,
    "RequestId": "43F670F3-AB40-4E91-****-C57400000000",
    "CurrentPage": 1,
    "Count": 1,
    "SuspEvents": {
        "K8sNodeId": "i-km10**********",
        "Advanced": false,
        "K8sNodeName": "cn-wulan-env116-d01.i-km10***********",
        "ContainHwMode": false,
        "OperateErrorCode": "quara.Succes",
        "AlarmEventName": "DDoS trojan",
        "SecurityEventIds": "None",
        "EventStatus": 1,
        "HasTraceInfo": false,
```

Cloud Security Management Cent ,

```json
        "IntranetIp": "192.168.XX.XX",
        "K8sClusterId": "cb9218***********",
        "EventSubType": "XOR DDoS trojan",
        "AppName": "demo-name",
        "Name": "Malicious process (cloud threat detection) - XOR DDoS trojan",
        "K8sNamespace": "kube-****",
        "Desc": "XOR DDoS trojan",
        "LastTimeStamp": 1639236844747,
        "InternetIp": "47.100.XX.XX",
        "ContainerId": "B4*****-3***-4***-B***-9F********",
        "AlarmEventType": "Malicious process (cloud threat detection)",
        "AlarmEventNameDisplay": "None",
        "UniqueInfo": "e17e***",
        "CanCancelFault": false,
        "AlarmEventTypeDisplay": "None",
        "InstanceId": "i-km10*********",
        "Stages": "[]",
        "MarkMisRules": "***Trojan file path*****Contain****",
        "K8sPodName": "nginx-ingress-controller-5b******-l4***",
        "SaleVersion": 1,
        "ContainerImageId": "docker-pullable://registry.acs.***.com/acs/aliyun-**-contr
oller:demo",
        "DataSource": "aegis_suspicious_***",
        "InstanceName": "nginx",
        "OccurrenceTime": "2018-09-26 01:51:01",
        "OperateTime": 1639236844747,
        "CanBeDealOnLine": true,
        "OperateMsg": "success",
        "K8sClusterName": "demo*******",
        "Uuid": "bf6b30d3-eea8-4924-9f0a-***",
        "ContainerImageName": "registry.acs.demo.com/acs/aliyun-**-controller:demo",
        "AlarmUniqueInfo": "8df914418f***",
        "AutoBreaking": false,
        "OccurrenceTimeStamp": 1639236844747,
        "Level": "serious",
        "Id": 1000,
        "LastTime": "2018-09-26 01:51:01",
        "Details": {
            "Type": "html",
            "Value": "Description",
            "ValueDisplay": "None",
            "InfoType": "download_url",
            "NameDisplay": "None",
            "Name": "Alert description"
        },
        "EventNotes": {
            "NoteId": 1,
            "Note": "Remarks",
            "NoteTime": "2018-12-12 12:00:00"
        }
    }
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSuspEv entDetail | The operation that you want to perform. Set the value to DescribeSuspEventDetail. |
| From | String | Yes | sas | The data source of the exception. Set the value to sas. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| SuspiciousEventI d | Integer | No | 1 | The ID of the exception. Note To query the details of an exception, you must specify the ID of the exception. You can call the DescribeSuspEvents operation to query the IDs of exceptions. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CanBeDealOnL ine | Boolean | true | Indicates whether the online processing of exceptions is supported. Valid values: true: yes false: no |
| DataSource | String | aegis suspicious * _ _ ** | The data source of the exception. |

Cloud Security Management Cent

#### DescribeSuspEventDetail

Queries the details of an exception. An alert event consists of an alert and exceptions. Each alert event is associated with multiple exceptions.

**Request parameters**

**Response parameters**

| Details | Array of QuaraFile |  | An array that consists of the details about the exception. |
|---|---|---|---|
| InfoType | String | download url _ | The type of the icon. |
| Name | String | Alert description | The title in the exception details. |
| Type | String | html | The format of the exception details. Valid values: text html |
| Value | String | Description | The content in the exception details. |
| EventDesc | String | This file may have been uploaded by an attacker who has intruded into your website. Check the validity of this file. | The description of the exception. |
| EventName | String | WEBSHELL | The name of the exception. |
| EventStatus | String | 32 | The status of the exception. Valid values: 1: pending handling 2: ignored 4: confirmed 8: marked as false positive 16: handling 32: handled 64: expired |
| EventTypeDes c | String | Webshell - Webshell file | The type of the exception. |
| Id | Integer | 1 | The ID of the alert event. |
| InstanceName | String | worker-k8s-for-cs- cb9****** | The name of the instance. |
| InternetIp | String | 47.100.XX.XX | The public IP address. |
| IntranetIp | String | 192.168.XX.XX | The private IP address. |

Cloud Security Management Cent

| LastTime | String | 2018-10-30 11:43:46 | The time when the exception last occurred. The time is in the yyyy-MM-dd HH:mm:ss format. |
|---|---|---|---|
| Level | String | serious | The severity of the exception. Valid values: serious suspicious remind |
| OperateErrorC ode | String | quara.Succes | The handling result of the exception. |
| OperateMsg | String | success | The message that describes the handling result of the exception. |
| RequestId | String | 1 | The ID of the request. |
| SaleVersion | String | None | This parameter is deprecated. |
| SasId | String | None | This parameter is deprecated. |
| Uuid | String | B41******-3***- 4***-B***- 9********* | The UUID of the server. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSuspEventDetail &From=sas &<Common request parameters>
```

Sample success responses `XML` format Cloud Security Management Cent

```xml
<EventDesc>This file may have been uploaded by an attacker who has intruded into your w ebsite. Check the validity of this file.</EventDesc> <EventTypeDesc>Webshell - Webshell file</EventTypeDesc> <RequestId>1</RequestId> <OperateErrorCode>quara.Succes</OperateErrorCode> <EventStatus>32</EventStatus> <EventName>WEBSHELL</EventName> <SaleVersion>None</SaleVersion> <IntranetIp>192.168.XX.XX</IntranetIp> <DataSource>aegis_suspicious_***</DataSource> <InstanceName>worker-k8s-for-cs-cb9******</InstanceName> <CanBeDealOnLine>true</CanBeDealOnLine> <OperateMsg>success</OperateMsg> <Uuid>B41******-3***-4***-B***-9*********</Uuid> <Details>
    <Type>html</Type>
    <Value>Description</Value>
    <InfoType>download_url</InfoType>
    <Name>Alert description</Name>
</Details> <InternetIp>47.100.XX.XX</InternetIp> <Level>serious</Level> <Id>1</Id> <LastTime> 2018-10-30 11:43:46 </LastTime> <SasId>None</SasId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRiskIte mType | The operation that you want to perform. Set the value to DescribeRiskItemType. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |

Cloud Security Management Cent

```json
{
    "EventDesc": "This file may have been uploaded by an attacker who has intruded into
your website. Check the validity of this file.",
    "EventTypeDesc": "Webshell - Webshell file",
    "RequestId": 1,
    "OperateErrorCode": "quara.Succes",
    "EventStatus": 32,
    "EventName": "WEBSHELL",
    "SaleVersion": "None",
    "IntranetIp": "192.168.XX.XX",
    "DataSource": "aegis_suspicious_***",
    "InstanceName": "worker-k8s-for-cs-cb9******",
    "CanBeDealOnLine": true,
    "OperateMsg": "success",
    "Uuid": "B41******-3***-4***-B***-9*********",
    "Details": {
        "Type": "html",
        "Value": "Description",
        "InfoType": "download_url",
        "Name": "Alert description"
    },
    "InternetIp": "47.100.XX.XX",
    "Level": "serious",
    "Id": 1,
    "LastTime": "2018-10-30 11:43:46",
    "SasId": "None"
}
```

### Configuration assessment

#### DescribeRiskItemType

Queries the types of check items in configuration assessment. Each check item is categorized into a type. The types of check items include identity authentication and permissions, network access control, log audit, data security, monitoring and alerting, and basic security protection.

**Request parameters**

| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | Array of ItemType |  | An array that consists of the types of check items. |
| Id | Long | 1 | The ID of the check item. |
| Title | String | Identity authentication and permissions | The type of the check item. |
| RequestId | String | 3B3F3A90-46A5- ***-A2D8- D68B14262F96 | The ID of the request. |

Cloud Security Management Cent

**Response parameters**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRiskItemType &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>3B3F3A90-46A5-***-A2D8-D68B14262F96</RequestId> <List>
    <Title>Identity authentication and permissions</Title>
    <Id>1</Id>
</List>
```

`JSON` format

```json
{
    "RequestId": "3B3F3A90-46A5-***-A2D8-D68B14262F96",
    "List": {
        "Title": "Identity authentication and permissions",
        "Id": 1
    }
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartBaselineSe curityCheck | The operation that you want to perform. Set the value to StartBaselineSecurityCheck. |
| Type | String | Yes | check | The type of the check task. Valid values: check verify |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| ItemIds.N | RepeatL ist | No | 1 | The ID of the check item. Note To perform a check task on cloud service configurations, you must specify the ID of the check item. You can call the DescribeRiskItemType operation to obtain the IDs of check items. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 48D2E9A9-A1B0- 4295-***- 0995757C47E9 | The ID of the request. |

Cloud Security Management Cent

#### StartBaselineSecurityCheck

Checks cloud service configurations. You can check all items or a specific item and verify whether an item is checked.

**Request parameters**

**Response parameters**

Sample requests

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRiskChe ckSummary | The operation that you want to perform. Set the value to DescribeRiskCheckSummary. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| ResourceDirecto ryAccountId | String | No | None | This parameter is deprecated. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 291B49F9-1685- 4005-****- 606B6F78740F | The ID of the request. |

Cloud Security Management Cent

```
http(s)://[Endpoint]/?Action=StartBaselineSecurityCheck &Type=check &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>48D2E9A9-A1B0-4295-***-0995757C47E9</RequestId>
```

`JSON` format

```json
{
    "RequestId": "48D2E9A9-A1B0-4295-***-0995757C47E9"
}
```

#### DescribeRiskCheckSummary

Queries the summary information about the check results of cloud service configurations. The operation returns the following information: the number of risk items, the risk rate, the number of affected assets, the last check time, and the statistics of each type of check items.

**Request parameters**

**Response parameters**

| RiskCheckSum mary | Struct |  | The summary information about the check results of cloud service configurations. |
|---|---|---|---|
| AffectedAsset Count | Integer | 0 | The number of affected assets. |
| DisabledRiskC ount | Integer | 0 | The number of the check items that fail the check. |
| EnabledRiskCo unt | Integer | 3 | The number of the check items that pass the check. |
| Groups | Array of group |  | An array that consists of the statistics of each type of check item. |
| CountByStatus | Array of statusCount |  | An array that consists of the statistics of check items. |
| Count | Integer | 2 | The number of detected risk items. |
| Status | String | pass | The status of a check item after the check is finished. Valid values: pass: The check item passes the check, which indicates that the check item is normal. failed: The check item fails the check, which indicates that risks are detected for the check item. |
| Id | Long | 1 | The type ID of the check item. |
| RemainingTim e | Integer | 0 | The time when the next check will be performed. |
| Sort | Integer | 1 | The sequence number of the check item type in the All Types drop-down list in the console. |
| Status | String | finish | The status of the check. Valid values: finish: The check is finished. running: The check is in process. waiting: The check is pending. notStart: The check is not started. |
| Title | String | Identity authentication and permissions | The type of the check items. |

Cloud Security Management Cent

| ItemCount | Integer | 4 | The number of check items. |
|---|---|---|---|
| PreviousCount | Integer | 0 | The number of detected risk items in the last check. |
| PreviousTime | Long | 1545012926000 | The time when the last check was performed. The value is a UNIX timestamp. Unit: milliseconds. |
| RiskCount | Integer | 1 | The number of detected risk items. |
| RiskLevelCoun t | Array of levelCount |  | The number of check items at each risk level. Valid values: high medium low |
| Count | Integer | 1 | The number of risk items of the risk level. |
| Key | String | medium | The risk level of a check item. |
| RiskRate | Float | 0.25 | The proportion of risk items to all check items. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRiskCheckSummary &<Common request parameters>
```

Sample success responses `XML` format Cloud Security Management Cent

```xml
<RequestId>291B49F9-1685-4005-****-606B6F78740F</RequestId> <RiskCheckSummary>
    <DisabledRiskCount>0</DisabledRiskCount>
    <PreviousTime>1545012926000</PreviousTime>
    <RiskRate>0.25</RiskRate>
    <ItemCount>4</ItemCount>
    <PreviousCount>0</PreviousCount>
    <EnabledRiskCount>3</EnabledRiskCount>
    <AffectedAssetCount>0</AffectedAssetCount>
    <RiskCount>1</RiskCount>
    <Groups>
        <Status>finish</Status>
        <RemainingTime>0</RemainingTime>
        <Sort>1</Sort>
        <Title>Identity authentication and permissions</Title>
        <Id>1</Id>
        <CountByStatus>
            <Status>pass</Status>
            <Count>2</Count>
        </CountByStatus>
    </Groups>
    <RiskLevelCount>
        <Count>1</Count>
        <Key>medium</Key>
    </RiskLevelCount>
</RiskCheckSummary>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRiskChe ckResult | The operation that you want to perform. Set the value to DescribeRiskCheckResult. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

Cloud Security Management Cent

```json
{
    "RequestId": "291B49F9-1685-4005-****-606B6F78740F",
    "RiskCheckSummary": {
        "DisabledRiskCount": 0,
        "PreviousTime": 1545012926000,
        "RiskRate": 0.25,
        "ItemCount": 4,
        "PreviousCount": 0,
        "EnabledRiskCount": 3,
        "AffectedAssetCount": 0,
        "RiskCount": 1,
        "Groups": {
            "Status": "finish",
            "RemainingTime": 0,
            "Sort": 1,
            "Title": "Identity authentication and permissions",
            "Id": 1,
            "CountByStatus": {
                "Status": "pass",
                "Count": 2
            }
        },
        "RiskLevelCount": {
            "Count": 1,
            "Key": "medium"
        }
    }
}
```

#### DescribeRiskCheckResult

Queries the check results of cloud service configurations by check item type or name.

**Request parameters**

| GroupId | Long | No | 21000 | The type ID of the check item. |
|---|---|---|---|---|
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| RiskLevel | String | No | high | The risk level of the check item. Valid values: high medium low |
| Status | String | No | pass | The status of the check result. Valid values: pass failed running waiting ignored falsePositive |
| ItemIds.N | RepeatL ist | No | sde*** | The ID of the check item. |
| AssetType | String | No | RDS | The type of the cloud service. Valid values: RDS: ApsaraDB RDS ECS: Elastic Compute Service (ECS) OSS: Object Storage Service (OSS) MongoDB: ApsaraDB for MongoDB Redis: KVStore for Redis |
| Name | String | No | Cloud platform - MFA configuration of Apsara Stack tenant accounts | The name of the check item. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| QueryFlag | String | No | None | This parameter is deprecated. |
| regionId | String | No | hangzhou** | The ID of the region. |

Cloud Security Management Cent

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The total number of returned pages. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| List | Array of RiskCheckRes ultForDisplay |  | An array that consists of the information about the check item. |
| AffectedCount | Integer | 0 | The number of affected assets. |
| CheckTime | Long | 1543991525000 | The time when the last check was performed. The value is a UNIX timestamp. Unit: milliseconds. |
| ItemId | Long | 1 | The ID of the check item. |
| RemainingTim e | Integer | 0 | This parameter is deprecated. |
| RepairStatus | String | disabled | Indicates whether the risk of the check item can be fixed. Valid values: enabled: yes disabled: no |
| RiskAssertTyp e | String | ECS | The type of the affected asset. |
| RiskItemResou rces | Array of RiskItemResou rce |  | An array that consists of the details about the check item. |
| ContentResour ce | Json | { "type": "link", "value": "Risk: MFA is disabled\n", "url": "https://***.aliyun.c om/#/secure\n" } | The content in the check item details. |
| ResourceNam e | String | bestPractice | The title in the check item details. Valid values: bestPractice: description influence: risk suggestion: solution helpResource: reference |

Cloud Security Management Cent

| RiskLevel | String | high | The risk level of the check item. Valid values: high medium low |
|---|---|---|---|
| Sort | Integer | 1 | The sequence number of the check result. |
| StartStatus | String | enabled | Indicates whether the check item is supported. Valid values: enabled: yes disable: no |
| Status | String | pass | The status of the check result. Valid values: pass failed running waiting ignored falsePositive |
| TaskId | Long | 7 | The ID of the check task. |
| Title | String | Cloud platform - MFA configuration of Apsara Stack tenant accounts | The title of the check item. |
| Type | String | Identity authentication and permissions | The type of the check item. |
| PageCount | Integer | 20 | The total number of pages returned. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | AD271C07-4ACE- ***-AA9B- F14FD3B7717F | The ID of the request. |
| TotalCount | Integer | 12 | The total number of entries returned. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRiskCheckResult &<Common request parameters>
```

Cloud Security Management Cent Sample success responses `XML` format

```json
<TotalCount>12</TotalCount> <PageSize>10</PageSize> <PageCount>20</PageCount> <RequestId>AD271C07-4ACE-***-AA9B-F14FD3B7717F</RequestId> <CurrentPage>1</CurrentPage> <List>
    <RiskAssertType>ECS</RiskAssertType>
    <Status>pass</Status>
    <CheckTime>1543991525000</CheckTime>
    <StartStatus>enabled</StartStatus>
    <Type>Identity authentication and permissions</Type>
    <TaskId>7</TaskId>
    <RemainingTime>0</RemainingTime>
    <AffectedCount>0</AffectedCount>
    <Sort>1</Sort>
    <Title>Cloud platform - MFA configuration of Apsara Stack tenant accounts</Title>
    <RepairStatus>disabled</RepairStatus>
    <RiskLevel>high</RiskLevel>
    <ItemId>1</ItemId>
    <RiskItemResources>
        <ContentResource>{   "type": "link",   "value": "Risk: MFA is disabled\n",
"url": "https://***.aliyun.com/#/secure\n" }</ContentResource>
        <ResourceName>bestPractice</ResourceName>
    </RiskItemResources>
</List> <Count>10</Count>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurit yCheckSchedule Config | The operation that you want to perform. Set the value to DescribeSecurityCheckScheduleC onfig. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

Cloud Security Management Cent

```json
{
    "TotalCount": 12,
    "PageSize": 10,
    "PageCount": 20,
    "RequestId": "AD271C07-4ACE-***-AA9B-F14FD3B7717F",
    "CurrentPage": 1,
    "List": {
        "RiskAssertType": "ECS",
        "Status": "pass",
        "CheckTime": 1543991525000,
        "StartStatus": "enabled",
        "Type": "Identity authentication and permissions",
        "TaskId": 7,
        "RemainingTime": 0,
        "AffectedCount": 0,
        "Sort": 1,
        "Title": "Cloud platform - MFA configuration of Apsara Stack tenant accounts",
        "RepairStatus": "disabled",
        "RiskLevel": "high",
        "ItemId": 1,
        "RiskItemResources": {
            "ContentResource": "{   \"type\": \"link\",   \"value\": \"Risk: MFA is disa
bled\\n\", \"url\": \"https://***.aliyun.com/#/secure\\n\" }",
            "ResourceName": "bestPractice"
        }
    },
    "Count": 10
}
```

#### DescribeSecurityCheckScheduleConfig

Queries the custom check cycle and time period.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 48D2E9A9-A1B0- 4295-****- 0995757C47E9 | The ID of the request. |
| RiskCheckJobC onfig | Struct |  | The settings of scheduled check tasks. |
| DaysOfWeek | String | 1,2,3 | The day of the week when the check tasks are performed. You can specify multiple days. Separate multiple values with commas (,). Valid values: 1: Monday 2: Tuesday 3: Wednesday 4: Thursday 5: Friday 6: Saturday 7: Sunday |
| EndTime | Integer | 12 | The time range during which the check tasks end. Valid values: 6: 00:00 to 06:00 12: 06:00 to 12:00 18: 12:00 to 18:00 24: 18:00 to 24:00 |
| StartTime | Integer | 6 | The time range during which the check tasks start. Valid values: 6: 00:00 to 06:00 12: 06:00 to 12:00 18: 12:00 to 18:00 24: 18:00 to 24:00 |

Cloud Security Management Cent

**Response parameters**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSecurityCheckScheduleConfig &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVulList | The operation that you want to perform. Set the value to DescribeVulList. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| Remark | String | No | 47.200.XX.XX | The tag to query, which can be the internal IP address, public IP address, or name of the asset. |
| GroupId | String | No | 9207613 | The ID of the asset group. |

Cloud Security Management Cent

```xml
<RiskCheckJobConfig>
    <DaysOfWeek>1,2,3</DaysOfWeek>
    <EndTime>12</EndTime>
    <StartTime>6</StartTime>
</RiskCheckJobConfig> <RequestId>48D2E9A9-A1B0-4295-****-0995757C47E9</RequestId>
```

`JSON` format

```json
{
    "RiskCheckJobConfig": {
        "DaysOfWeek": "1,2,3",
        "EndTime": 12,
        "StartTime": 6
    },
    "RequestId": "48D2E9A9-A1B0-4295-****-0995757C47E9"
}
```

### Vulnerability management

#### DescribeVulList

Queries vulnerabilities by type.

**Request parameters**

| Type | String | No | cve | The type of the vulnerability. Valid values: cve: Linux software vulnerabilities sys: Windows system vulnerabilities cms: Web-CMS vulnerabilities app: application vulnerabilities emg: urgent vulnerabilities |
|---|---|---|---|---|
| Uuids | String | No | 1587bedb-fdb4- 48c4-9330- ************ | The UUIDs of assets. Separate multiple UUIDs with commas (,). |
| AliasName | String | No | RHSA-2019:***- Important: polkit security update | The alias of the vulnerability. |
| Level | String | No | serious | The severity of the vulnerability. Valid values: serious high medium low |
| Necessity | String | No | asap,later,nntf | The priority to fix the vulnerabilities. Separate multiple priorities with commas (,). Valid values: asap: high later: medium nntf: low |
| Dealed | String | No | n | Specifies whether the vulnerability is handled. Valid values: y: yes n: no |
| BatchName | String | No | Test | The name that identifies the group of vulnerabilities. |
| Resource | String | No | vulnerability | The source of the group of vulnerabilities. Valid values: vulnerability and host. |
| CreateTsStart | Long | No | 1512949391000 | The beginning of the creation time. The value is a UNIX timestamp. Unit: milliseconds. |

Cloud Security Management Cent

| CreateTsEnd | Long | No | 1512949392000 | The end of the creation time. The value is a UNIX timestamp. Unit: milliseconds. |
|---|---|---|---|---|
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| ModifyTsStart | Long | No | 1512949391000 | The beginning of the time range during which the vulnerability is modified. The value is a UNIX timestamp. Unit: milliseconds. |
| ModifyTsEnd | Long | No | 1512949392000 | The end of the time range during which the vulnerability is modified. The value is a UNIX timestamp. Unit: milliseconds. |
| AttachTypes | String | No | sca | The additional type of vulnerability. You can specify this parameter when you query application vulnerabilities. If Type is set to app, you must specify this parameter. Set the value to sca. |
| ContainerFieldN ame | String | No | None | This parameter is deprecated. |
| ContainerFieldV alue | String | No | None | This parameter is deprecated. |
| TargetType | String | No | groupId | The type of the asset to query. Valid values: groupId: the ID of an asset group. uuid: the UUID of an asset. |
| ClusterId | String | No | Test cluster 1 | The ID of the cluster. |
| MinScore | Integer | No | 100 | The minimum score. |
| VpcInstanceIds | String | No | vpc-xxx | The ID of the virtual private cloud (VPC). |

| Parameter | Type | Example | Description |
|---|---|---|---|

Cloud Security Management Cent

**Response parameters**

| RequestId | String | ECDE6715-6286- 40E6-A32D- 3094051FD74D | The ID of the request. |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 2 | The total number of entries returned. |
| VulRecords | Array of VulRecord |  | An array that consists of the information about the vulnerability. |
| AliasName | String | RHSA-2017:0574: gnutls security, bug fix, and enhancement update | The alias of the vulnerability. |
| ContainerId | String | None | This parameter is deprecated. |
| ContainerImag eId | String | None | This parameter is deprecated. |
| ContainerImag eName | String | None | This parameter is deprecated. |
| ContainerInner Path | String | None | This parameter is deprecated. |
| ContainerNam e | String | None | This parameter is deprecated. |
| ExtendContent Json | Struct |  | The extended information. |
| AbsolutePath | String | /roo/www/web | The absolute path. |
| AliasName | String | RHSA-2017:0574: gnutls security, bug fix, and enhancement update | The alias of the vulnerability. |
| Ip | String | 47.200.XX.XX | The IP address of the asset that is associated with the vulnerability. By default, the public IP address is displayed. If the public IP address does not exist, the private IP address is displayed. |
| LastTs | Long | 1554189334000 | The timestamp when the vulnerability is last detected. Unit: milliseconds. |

Cloud Security Management Cent

| Necessity | Struct |  | The priority to fix the vulnerability. |
|---|---|---|---|
| Assets factor _ | String | 1 | The asset score. |
| Cvss factor _ | String | 7.8 | The Common Vulnerability Scoring System (CVSS) score. |
| Enviroment fa _ ctor | String | 1.0 | The environmental score. |
| Is calc _ | String | 1 | Indicates whether the vulnerability severity score is calculated. Valid values: 0: no 1: yes |
| Status | String | normal | The status of the vulnerability severity score. Valid values: none: No score is generated. pending: The score is pending calculation. miss: The score failed to be calculated. normal: The calculation is normal. |
| Time factor _ | String | 1.0 | The temporal score. |
| Total score _ | String | 7.8 | The total vulnerability severity score. |
| Os | String | centos | The operating system. |
| OsRelease | String | 7 | The version of the operating system. |
| PrimaryId | Long | 111 | The ID of the vulnerability. |
| RpmEntityList | Array of RpmEntity |  | An array that consists of the information about RPM Package Manager (RPM) packages. |
| FullVersion | String | 3.10.0-693.2.2.el7 | The complete version number. |
| MatchDetail | String | python-perf version less than 0:3.10.0- 693.21.1.el7 | The matching details. |

Cloud Security Management Cent

| Name | String | python-perf | The name of the RPM package. |
|---|---|---|---|
| Path | String | /usr/lib64/python2. 7/site-packages | The path. |
| UpdateCmd | String | *** update python- perf | The command that is used to fix the vulnerability. |
| Version | String | 3.10.0 | The version number. |
| Status | String | 1 | The status of the vulnerability. Valid values: 1: unfixed 2: fix failed 3: rollback failed 4: fixing 5: rolling back 6: verifying 7: fixed 8: fixed and to be restarted 9: rolled back 10: ignored 11: rolled back and to be restarted 12: not found 20: expired |
| Tag | String | oval | The tag that is added to the vulnerability. |
| cveList | List | ["CVE-2016-8610", "CVE-2017-5335" ] | The Common Vulnerabilities and Exposures (CVE) list. |
| FirstTs | Long | 1554189334000 | The time when the vulnerability was first detected. The value is a UNIX timestamp. Unit: milliseconds. |
| GroupId | Integer | 281801 | The ID of the asset group. |
| InstanceId | String | i-bp18t*** | The ID of the asset. |
| InstanceName | String | Test ECS instance | The name of the asset. |
| InternetIp | String | 47.200.XX.XX | The public IP address of the asset. |
| IntranetIp | String | 192.168.XX.XX | The internal IP address of the asset. |

Cloud Security Management Cent

| r Developer Guid ion Service (TDS) | e·Threat Detec |  |  |
|---|---|---|---|

| K8sClusterId | String | None | This parameter is deprecated. |
|---|---|---|---|
| K8sNamespac e | String | None | This parameter is deprecated. |
| K8sNodeId | String | None | This parameter is deprecated. |
| K8sNodeName | String | None | This parameter is deprecated. |
| K8sPodName | String | None | This parameter is deprecated. |
| LastTs | Long | 1541207563000 | The timestamp when the vulnerability was last detected. Unit: milliseconds. |
| ModifyTs | Long | 1541207563000 | The timestamp when the vulnerability was modified. Unit: milliseconds. |
| Name | String | oval:com.redhat.rh sa:def:20170574 | The name of the vulnerability. |
| Necessity | String | asap | The priority to fix the vulnerability. Valid values: asap: high later: medium nntf: low |
| Online | Boolean | true | Indicates whether the asset is online. Valid values: true: yes false: no |
| OsVersion | String | linux | The version of the operating system. |
| PrimaryId | Long | 101162078 | The ID of the vulnerability. |
| Related | String | CVE-2017- 7518,CVE-2017- 12188 | The list of CVEs related to the vulnerability. Multiple CVEs are separated by commas (,). |
| RepairTs | Long | 1541207563000 | The timestamp when the vulnerability was fixed. Unit: milliseconds. |

Cloud Security Management Cent

| ResultCode | String | 0 | The code returned after the vulnerability is fixed. |
|---|---|---|---|
| ResultMessage | String | timeout | The message returned after the vulnerability is fixed. |
| Status | Integer | 1 | The status of the vulnerability. Valid values: 1: unfixed 2: fix failed 3: rollback failed 4: fixing 5: rolling back 6: verifying 7: fixed 8: fixed and to be restarted 9: rolled back 10: ignored 11: rolled back and to be restarted 12: not found 20: expired |
| Tag | String | oval | The tag that is added to the vulnerability. |
| Type | String | cve | The type of the vulnerability. Valid values: cve: Linux software vulnerabilities sys: Windows system vulnerabilities cms: Web-CMS vulnerabilities emg: urgent vulnerabilities app: application vulnerabilities |
| Uuid | String | 04c56617-23fc- 43a5-ab9b- ************ | The UUID of the asset. |

Cloud Security Management Cent Sample requests

```
&<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>2</TotalCount> <PageSize>20</PageSize> <RequestId>ECDE6715-6286-40E6-A32D-3094051FD74D</RequestId> <VulRecords>
```

Cloud Security Management Cent

```xml
    <K8sNodeId>None</K8sNodeId>
    <K8sNodeName>None</K8sNodeName>
    <OsVersion>linux</OsVersion>
    <ContainerInnerPath>None</ContainerInnerPath>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <K8sClusterId>None</K8sClusterId>
    <Name>oval:com.redhat.rhsa:def:20170574</Name>
    <K8sNamespace>None</K8sNamespace>
    <RepairTs>1541207563000</RepairTs>
    <ModifyTs>1541207563000</ModifyTs>
    <InternetIp>47.200.XX.XX</InternetIp>
    <ContainerId>None</ContainerId>
    <ContainerName>None</ContainerName>
    <AliasName>RHSA-2017:0574: gnutls security, bug fix, and enhancement
update</AliasName>
    <Status>1</Status>
    <InstanceId>i-bp18t***</InstanceId>
    <Necessity>asap</Necessity>
    <LastTs>1541207563000</LastTs>
    <K8sPodName>None</K8sPodName>
    <ResultMessage>timeout</ResultMessage>
    <ContainerImageId>None</ContainerImageId>
    <GroupId>281801</GroupId>
    <InstanceName>Test ECS instance</InstanceName>
    <FirstTs>1554189334000</FirstTs>
    <Type>cve</Type>
    <Related>CVE-2017-7518,CVE-2017-12188</Related>
    <Uuid>04c56617-23fc-43a5-ab9b-************</Uuid>
    <ContainerImageName>None</ContainerImageName>
    <Tag>oval</Tag>
    <Online>true</Online>
    <ResultCode>0</ResultCode>
    <PrimaryId>101162078</PrimaryId>
    <ExtendContentJson>
        <Status>1</Status>
        <Os>centos</Os>
        <Ip>47.200.XX.XX</Ip>
        <AliasName>RHSA-2017:0574: gnutls security, bug fix, and enhancement
update</AliasName>
        <LastTs>1554189334000</LastTs>
        <Tag>oval</Tag>
        <AbsolutePath>/roo/www/web</AbsolutePath>
        <OsRelease>7</OsRelease>
        <PrimaryId>111</PrimaryId>
        <RpmEntityList>
            <Path>/usr/lib64/python2.7/site-packages</Path>
            <UpdateCmd>*** update python-perf</UpdateCmd>
            <Version>3.10.0</Version>
            <FullVersion>3.10.0-693.2.2.el7</FullVersion>
            <MatchDetail>python-perf version less than 0:3.10.0-
693.21.1.el7</MatchDetail>
            <Name>python-perf</Name>
        </RpmEntityList>
        <cveList>["CVE-2016-8610", "CVE-2017-5335" ]</cveList>
```

Cloud Security Management Cent

```xml
        <Necessity>
            <Total_score>7.8</Total_score>
            <Status>normal</Status>
            <Time_factor>1.0</Time_factor>
            <Cvss_factor>7.8</Cvss_factor>
            <Is_calc>1</Is_calc>
            <Enviroment_factor>1.0</Enviroment_factor>
            <Assets_factor>1</Assets_factor>
        </Necessity>
    </ExtendContentJson>
</VulRecords> <CurrentPage>1</CurrentPage>
```

`JSON` format

```json
{
    "TotalCount": 2,
    "PageSize": 20,
    "RequestId": "ECDE6715-6286-40E6-A32D-3094051FD74D",
    "VulRecords": {
        "K8sNodeId": "None",
        "K8sNodeName": "None",
        "OsVersion": "linux",
        "ContainerInnerPath": "None",
        "IntranetIp": "192.168.XX.XX",
        "K8sClusterId": "None",
        "Name": "oval:com.redhat.rhsa:def:20170574",
        "K8sNamespace": "None",
        "RepairTs": 1541207563000,
        "ModifyTs": 1541207563000,
        "InternetIp": "47.200.XX.XX",
        "ContainerId": "None",
        "ContainerName": "None",
        "AliasName": "RHSA-2017:0574: gnutls security, bug fix, and enhancement update"
```

,

```json
        "Status": 1,
        "InstanceId": "i-bp18t***",
        "Necessity": "asap",
        "LastTs": 1541207563000,
        "K8sPodName": "None",
        "ResultMessage": "timeout",
        "ContainerImageId": "None",
        "GroupId": 281801,
        "InstanceName": "Test ECS instance",
        "FirstTs": 1554189334000,
        "Type": "cve",
        "Related": "CVE-2017-7518,CVE-2017-12188",
        "Uuid": "04c56617-23fc-43a5-ab9b-************",
        "ContainerImageName": "None",
        "Tag": "oval",
        "Online": true,
        "ResultCode": 0,
        "PrimaryId": 101162078,
"ExtendContentJson":{
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVulWhit elist | The operation that you want to perform. Set the value to DescribeVulWhitelist. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

Cloud Security Management Cent

```json
        ExtendContentJson: {
            "Status": 1,
            "Os": "centos",
            "Ip": "47.200.XX.XX",
            "AliasName": "RHSA-2017:0574: gnutls security, bug fix, and enhancement upd
ate",
            "LastTs": 1554189334000,
            "Tag": "oval",
            "AbsolutePath": "/roo/www/web",
            "OsRelease": 7,
            "PrimaryId": 111,
            "RpmEntityList": {
                "Path": "/usr/lib64/python2.7/site-packages",
                "UpdateCmd": "*** update python-perf",
                "Version": "3.10.0",
                "FullVersion": "3.10.0-693.2.2.el7",
                "MatchDetail": "python-perf version less than 0:3.10.0-693.21.1.el7",
                "Name": "python-perf"
            },
            "cveList": "[\"CVE-2016-8610\", \"CVE-2017-5335\" ]",
            "Necessity": {
                "Total_score": 7.8,
                "Status": "normal",
                "Time_factor": 1,
                "Cvss_factor": 7.8,
                "Is_calc": 1,
                "Enviroment_factor": 1,
                "Assets_factor": 1
            }
        }
    },
    "CurrentPage": 1
}
```

#### DescribeVulWhitelist

Queries the whitelist of vulnerabilities by page.

**Request parameters**

| PageSize | Integer | No | 10 | The number of entries to return on each page. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 74F97EF7-B543- 43FD-XXXX- 18456731F9C5 | The ID of the request. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| VulWhitelists | Array of VulWhitelist |  | An array that consists of the information about the vulnerability whitelist. |
| AliasName | String | RHSA-xxxx | The alias of the vulnerability. |
| Name | String | oval:com.redh.xxx xx | The name of the vulnerability. |
| Reason | String | Not urgent | The reason why you add the vulnerability to the whitelist. |
| Type | String | cve | The type of the vulnerability. |

Cloud Security Management Cent

**Response parameters**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVulWhitelist &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeConcer nNecessity | The operation that you want to perform. Set the value to DescribeConcernNecessity. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|

Cloud Security Management Cent

```xml
<TotalCount>1</TotalCount> <PageSize>10</PageSize> <RequestId>74F97EF7-B543-43FD-XXXX-18456731F9C5</RequestId> <VulWhitelists>
    <Type>cve</Type>
    <AliasName>RHSA-xxxx</AliasName>
    <Reason>Not urgent</Reason>
    <Name>oval:com.redh.xxxxx</Name>
</VulWhitelists> <CurrentPage>1</CurrentPage>
```

`JSON` format

```json
{
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "74F97EF7-B543-43FD-XXXX-18456731F9C5",
    "VulWhitelists": {
        "Type": "cve",
        "AliasName": "RHSA-xxxx",
        "Reason": "Not urgent",
        "Name": "oval:com.redh.xxxxx"
    },
    "CurrentPage": 1
}
```

#### DescribeConcernNecessity

Queries the priorities to fix vulnerabilities.

**Request parameters**

**Response parameters**

| ConcernNeces sity | List | [ "asap", "later", "nntf"] | The priorities to fix the vulnerabilities. Valid values: asap: high later: medium nntf: low |
|---|---|---|---|
| RequestId | String | 9139DAF6-5CE0- 49A0-XXXX- 07243A290F70 | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeGroupe dVul | The operation that you want to perform. Set the value to DescribeGroupedVul. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeConcernNecessity &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>9139DAF6-5CE0-49A0-XXXX-07243A290F70</RequestId> <ConcernNecessity>[ "asap", "later", "nntf"]</ConcernNecessity>
```

`JSON` format

```json
{
    "RequestId": "9139DAF6-5CE0-49A0-XXXX-07243A290F70",
    "ConcernNecessity": "[ \"asap\", \"later\", \"nntf\"]"
}
```

#### DescribeGroupedVul

Queries information about vulnerabilities by group.

**Request parameters**

| Type | String | No | cve | The type of the vulnerability. Valid values: cve: Linux software vulnerabilities sys: Windows system vulnerabilities cms: Web-CMS vulnerabilities app: application vulnerabilities emg: urgent vulnerabilities |
|---|---|---|---|---|
| Uuids | String | No | d42f938c-d962- 48a0-90f9- 05e4ea****** | The UUIDs of assets. Separate multiple UUIDs with commas (,). |
| AliasName | String | No | RHSA-2019:***- Important: polkit security update | The alias of the vulnerability. |
| Necessity | String | No | asap,later,nntf | The priority to fix the vulnerability. Separate multiple priorities with commas (,). Valid values: asap: high later: medium nntf: low |
| Dealed | String | No | n | Specifies whether the vulnerability is handled. Valid values: y: yes n: no |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| GroupId | String | No | weds**** | The ID of the asset group. |
| ContainerFieldN ame | String | No | XXX | The name of the container filed. |
| ContainerFieldV alue | String | No | XXX | The value of the container filed. |
| TargetType | String | No | groupId | The type of the asset to query. Valid values: groupId: the ID of an asset group. uuid: the UUID of an asset. |
| ClusterId | String | No | Test 1 | The ID of the cluster. |

Cloud Security Management Cent

| MinScore | Integer | No | 100 | The minimum score. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | 0DFCADBA-7065- 42DA-XXXX- 6868B9C2A8CF | The ID of the request. |
| TotalCount | Integer | 2 | The total number of entries returned. |
| GroupedVulIte ms | Array of GroupedVulIte m |  | An array that consists of the information about vulnerabilities by group. |
| AliasName | String | RHSA-2019:***- Important: polkit security update | The alias of the vulnerability. |
| AsapCount | Integer | 0 | The number of vulnerabilities that have the high priority. |
| GmtLast | Long | 1554185744000 | The time when the vulnerability was last detected. The value is a UNIX timestamp. Unit: milliseconds. |
| HandledCount | Integer | 0 | The number of handled vulnerabilities. |
| LaterCount | Integer | 0 | The number of vulnerabilities that have the medium priority. |
| Name | String | ***glibc security and bug fixes | The name of the vulnerability. |
| NntfCount | Integer | 59 | The number of vulnerabilities that have the low priority. |
| Tags | String | Restart required | The tag that is added to the vulnerability. |
| TotalFixCount | Long | 0 | The total number of fixed vulnerabilities. |

Cloud Security Management Cent

**Response parameters**

| Type | String | cve | The type of the vulnerability. Valid values: cve: Linux software vulnerabilities sys: Windows system vulnerabilities cms: Web-CMS vulnerabilities app: application vulnerabilities emg: urgent vulnerabilities |
|---|---|---|---|

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGroupedVul &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>2</TotalCount> <PageSize>20</PageSize> <RequestId>0DFCADBA-7065-42DA-XXXX-6868B9C2A8CF</RequestId> <CurrentPage>1</CurrentPage> <GroupedVulItems>
    <Type>cve</Type>
    <LaterCount>0</LaterCount>
    <GmtLast>1554185744000</GmtLast>
    <HandledCount>0</HandledCount>
    <AliasName>RHSA-2019:***-Important: polkit security update</AliasName>
    <AsapCount>0</AsapCount>
    <TotalFixCount>0</TotalFixCount>
    <NntfCount>59</NntfCount>
    <Tags>Restart required</Tags>
    <Name>***glibc security and bug fixes</Name>
</GroupedVulItems>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAutoDel Config | The operation that you want to perform. Set the value to DescribeAutoDelConfig. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Days | Integer | 7 | The number of days that a detected vulnerability is retained. Unit: days. |
| RequestId | String | 43186B14-5A39- 44E0-XXXX- 8B24D1EF82CC | The ID of the request. |

Cloud Security Management Cent

```json
{
    "TotalCount": 2,
    "PageSize": 20,
    "RequestId": "0DFCADBA-7065-42DA-XXXX-6868B9C2A8CF",
    "CurrentPage": 1,
    "GroupedVulItems": {
        "Type": "cve",
        "LaterCount": 0,
        "GmtLast": 1554185744000,
        "HandledCount": 0,
        "AliasName": "RHSA-2019:***-Important: polkit security update",
        "AsapCount": 0,
        "TotalFixCount": 0,
        "NntfCount": 59,
        "Tags": "Restart required",
        "Name": "***glibc security and bug fixes"
    }
}
```

#### DescribeAutoDelConfig

Queries the configurations for automatic vulnerability deletion.

**Request parameters**

**Response parameters**

Sample requests

```
&<Common request parameters>
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCheckW arningSummary | Set the value to DescribeCheckWarningSummary. |
| SourceIp | String | No | 1.2.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| TypeName | String | No | database | The type of check items. |
| Status | String | No | 1 | The status of the check item. Valid values: 1: failed 2: verifying 3: passed 5: expired 6: ignored |

Cloud Security Management Cent Sample success responses `XML` format

```xml
<RequestId>43186B14-5A39-44E0-XXXX-8B24D1EF82CC</RequestId> <Days>7</Days>
```

`JSON` format

```json
{
    "RequestId": "43186B14-5A39-44E0-XXXX-8B24D1EF82CC",
    "Days": 7
}
```

### Baseline check

#### DescribeCheckWarningSummary

Queries the statistical information about baseline check results. The information includes the number of servers on which a baseline check is performed, the number of baseline check items, and the pass rate of check items in the last baseline check.

**Request parameters**

| RiskStatus | Integer | No | 1 | The status of the check item. Valid values: 1: failed 3: passed |
|---|---|---|---|---|
| RiskName | String | No | Redis security baseline check | The name of the risk item. |
| StrategyId | Long | No | 1 | The ID of the baseline check policy. |
| Uuids | String | No | f03259d8-1e81- 4fae-bcbb- 275fb5****** | The ID of the server on which the baseline check is performed. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 00BD7CE2-284A- 4534-BD09-*** | The ID of the request. |
| TotalCount | Integer | 100 | The total number of baseline check items. |
| WarningSumm arys | Array of WarningSumm ary |  | The statistics of check items. |
| CheckCount | Integer | 10 | The number of check items. |
| HighWarningC ount | Integer | 1 | The number of high-risk items. |
| LastFoundTim e | String | 2019-01-01 12:23:00 | The time when the last baseline check was performed. |

Cloud Security Management Cent

**Response parameters**

| Level | String | high | The severity of the risk item. Valid values: high medium low |
|---|---|---|---|
| LowWarningCo unt | Integer | 3 | The number of low-risk items. |
| MediumWarni ngCount | Integer | 2 | The number of medium-risk items. |
| RiskId | Long | 1 | The ID of the risk item. |
| RiskName | String | Redis password | The name of the risk item. |
| SubTypeAlias | String | Redis | The sub-type type of the risk item. |
| TypeAlias | String | Database | The type of the check item. Valid values: database, system, weak password, and middleware. |
| WarningMachi neCount | Integer | 11 | The number of assets on which risk items are detected. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCheckWarningSummary &Lang=zh &TypeName=database &Status=1 &RiskStatus=1 &StrategyId=1 &Uuids=f03259d8-1e81-4fae-bcbb-275fb5****** &CurrentPage=1 &PageSize=20 &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <TotalCount>25</TotalCount>
   <PageSize>20</PageSize>
   <RequestId>DFA6CDC5-E826-4D18-A499-BEF9DA31F1AD</RequestId>
   <CurrentPage>1</CurrentPage>
   <Count>20</Count>
```

W i S Cloud Security Management Cent

```xml
   <WarningSummarys>
      <RiskId>43</RiskId>
      <LastFoundTime>2019-04-10 00:33:00</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>3</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>8</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>
                              </SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>
                              </RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>47</RiskId>
      <LastFoundTime>2019-04-10 00:58:11</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>2</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>7</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 7 security standard compliance (Level-3 classified sec
urity protection)</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 7 security standard compliance (Level-3 classified
security protection)</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>48</RiskId>
      <LastFoundTime>2019-04-10 00:58:11</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>2</WarningMachineCount>
      <CheckCount>12</CheckCount>
      <HighWarningCount>6</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 7 security standard compliance (Level-2 classified sec
urity protection)</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 7 security standard compliance (Level-2 classified
security protection)</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>3</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
<CheckCount>1</CheckCount>
```

Cloud Security Management Cent

```xml
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Database</TypeAlias>
      <SubTypeAlias>Redis security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Redis security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>19</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Linux weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>12</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Anonymous FTP logon</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Anonymous FTP logon</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>13</RiskId>
      <LastFoundTime>2019-04-10 06:58:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Windows weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Windows weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>23</RiskId>
      <LastFoundTime>2019-04-10 14:00:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>8</CheckCount>
      <HighWarningCount>0</HighWarningCount>
<Level>medium</Level>
```

Cloud Security Management Cent ee

```xml
edu /ee
      <TypeAlias>Middleware</TypeAlias>
      <SubTypeAlias>Apache Tomcat security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Apache Tomcat security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>2</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>PostgreSQL weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>PostgreSQL weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>11</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>MySQL weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>MySQL weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>20</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>FTP weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>FTP weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>17</RiskId>
      <LastFoundTime>2019-04-10 06:58:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Microsoft SQL Server weak password</SubTypeAlias>
```

Cloud Security Management Cent

```xml
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Microsoft SQL Server weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>24</RiskId>
      <LastFoundTime>2019-04-10 06:52:05</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>2</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>Database</TypeAlias>
      <SubTypeAlias>Memcached security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Memcached security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>42</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 6 security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6 security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>49</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>12</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 6 security standard compliance (Level-2 classified sec
urity protection)</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6 security standard compliance (Level-2 classified
security protection)</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>50</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 6 security standard compliance (Level-3 classified sec
```

Cloud Security Management Cent

```xml
urity protection)</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6 security standard compliance (Level-3 classified
security protection)</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>55</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>14</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Linux Ubuntu security standard compliance (Level-2 classified secur
ity protection)</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux Ubuntu security standard compliance (Level-2 classified security
protection)</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>56</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Linux Ubuntu security standard compliance (Level-3 classified secur
ity protection)</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux Ubuntu security standard compliance (Level-3 classified security
protection)</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>54</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Linux Ubuntu security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux Ubuntu security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>51</RiskId>
      <LastFoundTime>2019-02-19 12:44:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>12</CheckCount>
```

/ Cloud Security Management Cent

```xml
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Windows 2012 R2 security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Windows 2012 R2 security baseline check</RiskName>
   </WarningSummarys>
```

`JSON` format

```json
{
 "TotalCount":25,
 "PageSize":20,
 "RequestId":"DFA6CDC5-E826-4D18-A499-BEF9DA31F1AD",
 "CurrentPage":1,
 "Count":20,
 "WarningSummarys":[
  {
   "RiskId":43,
   "LastFoundTime":"2019-04-10 00:33:00",
   "MediumWarningCount":0,
   "WarningMachineCount":3,
   "CheckCount":16,
   "HighWarningCount":8,
   "Level":"high",
   "TypeAlias":"System",
   "SubTypeAlias":"CentOS Linux 7 security baseline check\n
\n ",
   "LowWarningCount":0,
   "RiskName":"CentOS Linux 7 security baseline check\n
\n "
  },
  {
   "RiskId":47,
   "LastFoundTime":"2019-04-10 00:58:11",
   "MediumWarningCount":0,
   "WarningMachineCount":2,
   "CheckCount":15,
   "HighWarningCount":7,
   "Level":"medium",
   "TypeAlias":"System",
   "SubTypeAlias":"CentOS Linux 7 security standard compliance - MLPS level-3",
   "LowWarningCount":0,
   "RiskName":"CentOS Linux 7 security standard compliance (Level-3 classified security
protection)"
  },
  {
   "RiskId":48,
   "LastFoundTime":"2019-04-10 00:58:11",
   "MediumWarningCount":0,
   "WarningMachineCount":2,
   "CheckCount":12,
   "HighWarningCount":6,
```

Cloud Security Management Cent

```json
   "Level":"medium",
   "TypeAlias":"System",
   "SubTypeAlias":"CentOS Linux 7 security standard compliance - MLPS level-2",
   "LowWarningCount":0,
   "RiskName":"CentOS Linux 7 security standard compliance (Level-2 classified security
protection)"
  },
  {
   "RiskId":3,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":1,
   "CheckCount":1,
   "HighWarningCount":1,
   "Level":"high",
   "TypeAlias":"Database",
   "SubTypeAlias":"Redis security baseline check",
   "LowWarningCount":0,
   "RiskName":"Redis security baseline check",
  },
  {
   "RiskId":19,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":1,
   "CheckCount":1,
   "HighWarningCount":1,
   "Level":"high",
   "TypeAlias":"Weak password",
   "SubTypeAlias":"Linux weak password",
   "LowWarningCount":0,
   "RiskName":"Linux weak password"
  },
  {
   "RiskId":12,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":1,
   "CheckCount":1,
   "HighWarningCount":1,
   "Level":"high",
   "TypeAlias":"Weak password",
   "SubTypeAlias":"Anonymous FTP logon",
   "LowWarningCount":0,
   "RiskName":"Anonymous FTP logon"
  },
  {
   "RiskId":13,
   "LastFoundTime":"2019-04-10 06:58:58",
   "MediumWarningCount":0,
   "WarningMachineCount":1,
   "CheckCount":1,
   "HighWarningCount":1,
   "Level":"high",
```

Cloud Security Management Cent

```json
   "TypeAlias":"Weak password",
   "SubTypeAlias":"Windows weak password",
   "LowWarningCount":0,
   "RiskName":"Windows weak password"
  },
  {
   "RiskId":23,
   "LastFoundTime":"2019-04-10 14:00:17",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":8,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"Middleware",
   "SubTypeAlias":"Apache Tomcat security baseline check",
   "LowWarningCount":0,
   "RiskName":"Apache Tomcat security baseline check"
  },
  {
   "RiskId":2,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":1,
   "HighWarningCount":0,
   "Level":"high",
   "TypeAlias":"Weak password",
   "SubTypeAlias":"PostgreSQL weak password",
   "LowWarningCount":0,
   "RiskName":"PostgreSQL weak password"
  },
  {
   "RiskId":11,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":1,
   "HighWarningCount":0,
   "Level":"high",
   "TypeAlias":"Weak password",
   "SubTypeAlias":"MySQL weak password",
   "LowWarningCount":0,
   "RiskName":"MySQL weak password"
  },
  {
   "RiskId":20,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":1,
   "HighWarningCount":0,
   "Level":"high",
   "TypeAlias":"Weak password",
   "SubTypeAlias":"FTP weak password",
```

`"L` W i

```
t"0
```

Cloud Security Management Cent

```json
   "LowWarningCount":0,
   "RiskName":"FTP weak password"
  },
  {
   "RiskId":17,
   "LastFoundTime":"2019-04-10 06:58:58",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":1,
   "HighWarningCount":0,
   "Level":"high",
   "TypeAlias":"Weak password",
   "SubTypeAlias":"Microsoft SQL Server weak password",
   "LowWarningCount":0,
   "RiskName":"Microsoft SQL Server weak password"
  },
  {
   "RiskId":24,
   "LastFoundTime":"2019-04-10 06:52:05",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":2,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"Database",
   "SubTypeAlias":"Memcached security baseline check",
   "LowWarningCount":0,
   "RiskName":"Memcached security baseline check"
  },
  {
   "RiskId":42,
   "LastFoundTime":"2019-02-19 14:59:17",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":16,
   "HighWarningCount":0,
   "Level":"high",
   "TypeAlias":"System",
   "SubTypeAlias":"CentOS Linux 6 security baseline check",
   "LowWarningCount":0,
   "RiskName":"CentOS Linux 6 security baseline check"
  },
  {
   "RiskId":49,
   "LastFoundTime":"2019-02-19 14:59:17",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":12,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"System",
   "SubTypeAlias":"CentOS Linux 6 security standard compliance (Level-2 classified secu
rity protection)",
   "LowWarningCount":0,
"RiskName":"CentOSLinux6securitystandardcompliance(Level-2classifiedsecurity
```

Cloud Security Management Cent

```json
   RiskName:CentOS Linux 6 security standard compliance (Level2 classified security
protection)"
  },
  {
   "RiskId":50,
   "LastFoundTime":"2019-02-19 14:59:17",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":15,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"System",
   "SubTypeAlias":"CentOS Linux 6 security standard compliance (Level-3 classified secu
rity protection)",
   "LowWarningCount":0,
   "RiskName":"CentOS Linux 6 security standard compliance (Level-3 classified security
protection)"
  },
  {
   "RiskId":55,
   "LastFoundTime":"2019-02-19 12:57:23",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":14,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"System",
   "SubTypeAlias":"Linux Ubuntu security standard compliance (Level-2 classified securi
ty protection)",
   "LowWarningCount":0,
   "RiskName":"Linux Ubuntu security standard compliance (Level-2 classified security p
rotection)"
  },
  {
   "RiskId":56,
   "LastFoundTime":"2019-02-19 12:57:23",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":15,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"System",
   "SubTypeAlias":"Linux Ubuntu security standard compliance (Level-3 classified securi
ty protection)",
   "LowWarningCount":0,
   "RiskName":"Linux Ubuntu security standard compliance (Level-3 classified security p
rotection)"
  },
  {
   "RiskId":54,
   "LastFoundTime":"2019-02-19 12:57:23",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":16,
   "HighWarningCount":0,
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeStratety | The operation that you want to perform. Set the value to DescribeStratety. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| StrategyIds | String | No | test1,test2,test3 | The IDs of the baseline check policies. Separate multiple IDs with commas (,). |

| Parameter | Type | Example | Description |
|---|---|---|---|

Cloud Security Management Cent g g ,

```json
   "Level":"high",
   "TypeAlias":"System",
   "SubTypeAlias":"Linux Ubuntu security baseline check",
   "LowWarningCount":0,
   "RiskName":"Linux Ubuntu security baseline check"
  },
  {
   "RiskId":51,
   "LastFoundTime":"2019-02-19 12:44:58",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":12,
   "HighWarningCount":0,
   "Level":"high",
   "TypeAlias":"System",
   "SubTypeAlias":"Windows 2012 R2 security baseline check",
   "LowWarningCount":0,
   "RiskName":"Windows 2012 R2 security baseline check"
  }
```

]

```
}
```

#### DescribeStratety

Queries the configurations of baseline check policies.

**Request parameters**

**Response parameters**

| RequestId | String | 16B9826C-B99F- 4F8A-8048- EA81D6D3DE8B | The ID of the request. |
|---|---|---|---|
| Strategies | Array |  | The information about the baseline check policy. |
| ConfigTargets | Array |  | The information about the group associated with the baseline check policy. |
| Flag | String | add | The related ID. |
| Target | String | 3259405 | The ID of the related group. |
| TargetType | String | groupId | The type of the related group. |
| CycleDays | Integer | 1 | The cycle of the baseline check. 1: every second day 3: every fourth day 7: every eighth day 30: every 31st day |
| CycleStartTim e | Integer | 6 | The time when the baseline check starts. Valid values: 0, 6, 12, and 18. |
| EcsCount | Integer | 5 | The number of servers on which baseline checks were performed based on the specified baseline check policy. |
| ExecStatus | Integer | 1 | The execution status of the baseline check. Valid values: 1: The baseline check is not running. 2: The baseline check is running. |
| Id | Integer | 212635 | The ID of the policy. |
| Name | String | test | The name of the policy. |
| PassRate | Integer | 80 | The pass rate of the latest baseline check. |
| ProcessRate | Integer | 80 | The progress of the baseline check. |
| RiskCount | Integer | 5 | The number of selected check items. |

Cloud Security Management Cent

| Type | Integer | 1 | The type of the baseline check policy. Valid values: 1: default policy 2: custom policy |
|---|---|---|---|

Cloud Security Management Cent Sample requests

```
? Lang=zh &SourceIp=127.0.0.1 &StrategyIds=1,2,3 &<Common request parameters>
```

Sample success responses `XML` format Cloud Security Management Cent

```xml
   <RequestId>ACAFE09B-3346-433B-BDA8-369AB3D9B4F9</RequestId>
   <Strategies>
      <CycleStartTime>6</CycleStartTime>
      <EcsCount>0</EcsCount>
      <Type>2</Type>
      <ExecStatus>1</ExecStatus>
      <ProcessRate>0</ProcessRate>
      <CycleDays>3</CycleDays>
      <Id>15161</Id>
      <ConfigTargets>
         <Target>4361221</Target>
         <TargetType>groupId</TargetType>
         <Flag>add</Flag>
      </ConfigTargets>
      <RiskCount>1</RiskCount>
      <Name>test</Name>
   </Strategies>
   <Strategies>
      <CycleStartTime>0</CycleStartTime>
      <EcsCount>17</EcsCount>
      <PassRate>81</PassRate>
      <Type>1</Type>
      <ExecStatus>1</ExecStatus>
      <ProcessRate>0</ProcessRate>
      <CycleDays>1</CycleDays>
      <Id>20</Id>
      <ConfigTargets>
         <Target>281801</Target>
         <TargetType>groupId</TargetType>
         <Flag>del</Flag>
      </ConfigTargets>
      <ConfigTargets>
         <Target>4790960</Target>
         <TargetType>groupId</TargetType>
         <Flag>del</Flag>
      </ConfigTargets>
      <RiskCount>13</RiskCount>
      <Name>Default policy</Name>
   </Strategies>
```

`JSON` format Cloud Security Management Cent

```json
{
 "RequestId":"ACAFE09B-3346-433B-BDA8-369AB3D9B4F9",
 "Strategies":[
  {
   "Name":"test",
   "RiskCount":1,
   "CycleDays":3,
   "Type":2,
   "CycleStartTime":6,
   "ConfigTargets":[
    {
     "Flag":"add",
     "Target":"4361221",
     "TargetType":"groupId"
    }
```

`],`

```json
   "ProcessRate":0,
   "Id":15161,
   "ExecStatus":1,
   "EcsCount":0
  },
  {
   "Name":"Default policy",
   "RiskCount":13,
   "PassRate":81,
   "CycleDays":1,
   "Type":1,
   "CycleStartTime":0,
   "ConfigTargets":[
    {
     "Flag":"del",
     "Target":"281801",
     "TargetType":"groupId"
    },
    {
     "Flag":"del",
     "Target":"4790960",
     "TargetType":"groupId"
    }
```

`],`

```json
   "ProcessRate":0,
   "Id":20,
   "ExecStatus":1,
   "EcsCount":17
  }
```

]

```
}
```

**Error codes**

For a list of error codes, see Error codes.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeStrateg yExecDetail | Set the value to DescribeStrategyExecDetail. |
| StrategyId | Integer | Yes | 1 | The ID of the baseline check policy. Note To query the results of a baseline check that uses a baseline check policy, you must specify the ID of the policy. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EndTime | String | 2019-01-08 20:11:20 | The time when the baseline check ends. The time is in the yyyy-MM-dd HH:mm:ss format. |
| FailCount | Integer | 94 | The number of check items that failed to pass the baseline check. This type of check item is considered risk items. |
| FailedEcsList | Array of FailedEcs |  | An array consisting of the servers on which risk items were detected. |
| IP | String | 192.168.XX.XX | The IP address of the server on which the baseline check was performed. |
| InstanceName | String | Test-20180703 | The name of the server. |
| IntranetIp | String | 192.168.XX.XX | The internal IP address. |

Cloud Security Management Cent

#### DescribeStrategyExecDetail

Queries the details of the last baseline check by using a baseline check policy. The details include the time when the check was performed, the number of risk items, and the details of baseline risks.

**Request parameters**

**Response parameters**

| Reason | String | Detect timeout | The failure cause for the check item. |
|---|---|---|---|
| InProcessCoun t | Integer | 0 | The number of baseline checks that are running. |
| Percent | String | 100% | The progress of the baseline check. |
| RequestId | String | 09322632-4668- 4AD9-****- 32757DEFBBA6 | The ID of the request. |
| Source | String | Manual | The type of the baseline check. Valid values: Schedule: automatic check that periodically runs Manual: intermediate check that is manually performed |
| StartTime | String | 2019-01-08 19:41:12 | The time when the baseline check starts. The time is in the yyyy-MM-dd HH:mm:ss format. |
| SuccessCount | Integer | 81 | The number of check items that passed the baseline check. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeStrategyExecDetail &StrategyId=1 &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCheckW arnings | Set the value to DescribeCheckWarnings. |

Cloud Security Management Cent

```xml
<EndTime>2019-01-08 20:11:20</EndTime> <RequestId>09322632-4668-4AD9-BD0D-32757DEFBBA6</RequestId> <Percent>100%</Percent> <FailCount>94</FailCount> <StartTime>2019-01-08 19:41:12</StartTime> <SuccessCount>81</SuccessCount> <Source>Manual</Source> <FailedEcsList>
    <InstanceName>Test-20180703</InstanceName>
    <IP>192.168.XX.XX</IP>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <Reason>Detect timeout</Reason>
</FailedEcsList> <InProcessCount>0</InProcessCount>
```

`JSON` format

```json
{
    "EndTime": "2019-01-08 20:11:20",
    "RequestId": "09322632-4668-4AD9-BD0D-32757DEFBBA6",
    "Percent": "100%",
    "FailCount": 94,
    "StartTime": "2019-01-08 19:41:12",
    "SuccessCount": 81,
    "Source": "Manual",
    "FailedEcsList": {
        "InstanceName": "Test-20180703",
        "IP": "192.168.XX.XX",
        "IntranetIp": "192.168.XX.XX",
        "Reason": "Detect timeout"
    },
    "InProcessCount": 0
}
```

#### DescribeCheckWarnings

Queries specified risk items and check items of a specified server.

**Request parameters**

| RiskId | Long | Yes | 1 | The ID of the risk item. Note To query specified risk items and check items of a specified server, you must specify the IDs of the risk items. |
|---|---|---|---|---|
| Uuid | String | Yes | d42f938c-d962- 48a0-90f9- 05********** | The ID of the server on which a baseline check is performed. The ID of the risk item. Note To query specified risk items and check items of a specified server, you must specify the ID of the server on which the baseline check is performed. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Default value: 20. |
| CurrentPage | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CheckWarning s | Array of CheckWarning |  | An array that consists of the information about the check item. |
| CheckId | Long | 1 | The ID of the check item. |
| CheckWarning Id | Long | 10 | The ID of the alert. |

Cloud Security Management Cent

**Response parameters**

| Item | String | Password expiration alert | The name of the check item. |
|---|---|---|---|
| Level | String | high | The severity of the risk item. Valid values: high medium low |
| Status | Integer | 1 | The status of the check item. Valid values: 1: failed 2: verifying 3: passed 5: expired 6: ignored |
| Type | String | Identity authentication | The type of the check item. |
| Uuid | String | d42f938c-d962- 48a0-90f9- *********** | The ID of the server on which the baseline check was performed. |
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | 0DFCADBA-7065- 42DA-AF17- 6868B9C2A8CF | The ID of the request. |
| TotalCount | Integer | 100 | The total number of entries returned. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCheckWarnings &RiskId=1 &Uuid=d42f938c-d962-48a0-90f9-05********** &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCheckW arningDetail | Set the value to DescribeCheckWarningDetail. |

Cloud Security Management Cent

```xml
<TotalCount>100</TotalCount> <CheckWarnings>
    <Status>1</Status>
    <Item>Password expiration alert</Item>
    <Type>Identity authentication</Type>
    <Uuid>d42f938c-d962-48a0-90f9-***********</Uuid>
    <CheckId>1</CheckId>
    <CheckWarningId>10</CheckWarningId>
    <Level>high</Level>
</CheckWarnings> <PageSize>20</PageSize> <RequestId>0DFCADBA-7065-42DA-AF17-6868B9C2A8CF</RequestId> <CurrentPage>1</CurrentPage> <Count>10</Count>
```

`JSON` format

```json
{
    "TotalCount": 100,
    "CheckWarnings": {
        "Status": 1,
        "Item": "Password expiration alert",
        "Type": "Identity authentication",
        "Uuid": "d42f938c-d962-48a0-90f9-***********",
        "CheckId": 1,
        "CheckWarningId": 10,
        "Level": "high"
    },
    "PageSize": 20,
    "RequestId": "0DFCADBA-7065-42DA-AF17-6868B9C2A8CF",
    "CurrentPage": 1,
    "Count": 10
}
```

#### DescribeCheckWarningDetail

Queries the details of a specified check item.

**Request parameters**

| CheckWarningId | Long | Yes | 1 | The ID of the alert triggered by the check item. Note To query the details of a check item, you must specify the ID of the alert triggered by the check item. |
|---|---|---|---|---|
| SourceIp | String | No | 192.168.x.x | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Advice | String | Fix now | The suggestion for the management of the risk item. |
| CheckId | Long | 1 | The ID of the check item. |
| Description | String | Password expiring | The additional details of the risk item. |
| Item | String | Password expiration alert | The name of the check item. |
| Level | String | high | The severity of the risk item. Valid values: high: The item is a high-risk one and highlighted in red. medium: The item is a medium-risk one and highlighted in orange. low: The item is a low-risk one and highlighted in gray. |
| Prompt | String | Password expiration alert | The prompt for the risk item. |
| RequestId | String | 09969D2C-4FAD- 429E-BFBF- 9A60DEF8BF6F | The ID of the request. |
| Type | String | Identity authentication | The type of the check item. |

Cloud Security Management Cent

**Response parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeWarnin gMachines | Set the value to DescribeWarningMachines. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCheckWarningDetail &CheckWarningId=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Item>Password expiration alert</Item> <Type>Identity authentication</Type> <Description>Password expiring</Description> <CheckId>1</CheckId> <RequestId>09969D2C-4FAD-429E-BFBF-9A60DEF8BF6F</RequestId> <Prompt>Password expiration alert</Prompt> <Level>high</Level> <Advice>Fix now</Advice>
```

`JSON` format

```json
{
    "Item": "Password expiration alert",
    "Type": "Identity authentication",
    "Description": "Password expiring",
    "CheckId": 1,
    "RequestId": "09969D2C-4FAD-429E-BFBF-9A60DEF8BF6F",
    "Prompt": "Password expiration alert",
    "Level": "high",
    "Advice": "Fix now"
}
```

#### DescribeWarningMachines

Queries information about servers on which a baseline check is performed. The information includes the statistics of a risk item, the status of the risk item, the IDs of the servers, and the names of the servers.

**Request parameters**

| RiskId | Long | Yes | 1 | The ID of the risk item. Note To query information about servers on which a baseline check is performed, you must specify the ID of a risk item that is detected in the baseline check. You can call the DescribeCheckWarningSumm ary operation to query the ID of the risk item. |
|---|---|---|---|---|
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| MachineName | String | No | Baseline check server | The name of the server on which the baseline check is performed. |
| Uuids | String | No | xxx-aaa-bbb-ccc | The ID of the server on which the baseline check is performed. Separate multiple IDs with commas (,). |
| StrategyId | Long | No | 1 | The ID of the baseline check policy. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The total number of returned pages. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |

Cloud Security Management Cent

**Response parameters**

| RequestId | String | 00BD7CE2-284A- 4534-BD09- FB69836DD750 | The ID of the request. |
|---|---|---|---|
| TotalCount | Integer | 100 | The total number of entries returned. |
| WarningMachi nes | Array of WarningMachi ne |  | An array that consists of the information about the servers on which alerts are generated. |
| HighWarningC ount | Integer | 10 | The number of high-risk items. |
| InstanceId | String | i- m5ee8b9nr3h30m hb**** | The ID of the server. |
| InstanceName | String | aaawebtest | The name of the server. |
| InternetIp | String | 47.100.XX.XX | The public IP address of the server. |
| IntranetIp | String | 192.168.XX.XX | The internal IP address of the server. |
| LowWarningCo unt | Integer | 3 | The number of low-risk items. |
| MediumWarni ngCount | Integer | 2 | The number of medium-risk items. |
| PassCount | Integer | 10 | The number of the check items that have passed the baseline check. |
| RegionId | String | cn-qingdao** | The ID of the region in which the server is deployed. |
| Status | Integer | 1 | The verification status of the risk item that is fixed. Valid values: 1: complete 2: verifying |
| Uuid | String | xxx-aaa-bbb-ccc | The ID of the server on which the baseline check is performed. |

Cloud Security Management Cent Sample requests Cloud Security Management Cent

```
http(s)://[Endpoint]/?Action=DescribeWarningMachines &RiskId=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>100</TotalCount> <PageSize>10</PageSize> <RequestId>00BD7CE2-284A-4534-BD09-FB69836DD750</RequestId> <CurrentPage>1</CurrentPage> <WarningMachines>
    <Status>1</Status>
    <InstanceName>aaawebtest</InstanceName>
    <MediumWarningCount>2</MediumWarningCount>
    <Uuid>xxx-aaa-bbb-ccc</Uuid>
    <InternetIp>47.100.XX.XX</InternetIp>
    <InstanceId>i-m5ee8b9nr3h30mhb****</InstanceId>
    <HighWarningCount>10</HighWarningCount>
    <RegionId>cn-qingdao</RegionId>
    <PassCount>10</PassCount>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <LowWarningCount>3</LowWarningCount>
</WarningMachines> <Count>10</Count>
```

`JSON` format

```json
{
    "TotalCount": 100,
    "PageSize": 10,
    "RequestId": "00BD7CE2-284A-4534-BD09-FB69836DD750",
    "CurrentPage": 1,
    "WarningMachines": {
        "Status": 1,
        "InstanceName": "aaawebtest",
        "MediumWarningCount": 2,
        "Uuid": "xxx-aaa-bbb-ccc",
        "InternetIp": "47.100.XX.XX",
        "InstanceId": "i-m5ee8b9nr3h30mhb****",
        "HighWarningCount": 10,
        "RegionId": "cn-qingdao",
        "PassCount": 10,
        "IntranetIp": "192.168.XX.XX",
        "LowWarningCount": 3
    },
    "Count": 10
}
```

### Asset fingerprints

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yCount | The operation that you want to perform. Set the value to DescribePropertyCount. |
| Type | String | No | port | The type of the asset fingerprint. Valid values: user: accounts software: software assets process: processes port: ports cron: scheduled tasks Note If you do not specify a type, all types of asset fingerprints are queried. |
| UuidList | String | No | [c4678332- ef3**,c46***] | The UUIDs of the assets. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Autorun | Integer | 123 | The number of startup items. |
| Cron | Integer | 261 | The number of scheduled tasks. |
| Port | Integer | 163 | The number of listening ports. |
| Process | Integer | 367 | The number of running processes. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
| Sca | Integer | 125 | The number of middleware assets. |
| Software | Integer | 5073 | The number of software assets. |

Cloud Security Management Cent

#### DescribePropertyCount

Queries the statistics of asset fingerprints, including the numbers of processes, ports, software assets, accounts, and scheduled tasks.

**Request parameters**

**Response parameters**

| User | Integer | 114 | The number of accounts. |
|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yPortDetail | The operation that you want to perform. Set the value to DescribePropertyPortDetail. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyCount &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Sca>125</Sca> <User>114</User> <RequestId>7E0618A9-D5EF-4220-9471-C42B5E92****</RequestId> <Port>163</Port> <Software>5073</Software> <Process>367</Process> <Autorun>123</Autorun> <Cron>261</Cron>
```

`JSON` format

```json
{
    "Sca": 125,
    "User": 114,
    "RequestId": "7E0618A9-D5EF-4220-9471-C42B5E92****",
    "Port": 163,
    "Software": 5073,
    "Process": 367,
    "Autorun": 123,
    "Cron": 261
}
```

#### DescribePropertyPortDetail

Queries the details of a port.

**Request parameters**

| Remark | String | No | 47.100.XX.XX | The name or IP address of the server. |
|---|---|---|---|---|
| Port | String | No | 22 | The number of the port. |
| ProcName | String | No | sshd | The name of the process. |
| Uuid | String | No | 50d213b4-3a35- 427a-b8a5-*** | The UUID of the asset. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 6 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |  | The pagination information. |
| Count | Integer | 5 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 762 | The total number of entries returned. |
| Propertys | Array of PropertyPort |  | An array that consists of the details of the port. |
| BindIp | String | 47.100.XX.XX | The IP addresses that are bound to the port. |
| Create | String | 2019-05- 13T10:39Z | The time when the data was last collected. |
| CreateTimesta mp | Long | 1557715141000 | The timestamp when the data was last collected. Unit: milliseconds. |
| InstanceId | String | 50d213b4-3a35- 427a-b8a5- 04b0c7e1fxxx | The ID of the asset that is associated with the port. |

Cloud Security Management Cent

**Response parameters**

| InstanceName | String | test-*** | The name of the asset that is associated with the port. |
|---|---|---|---|
| InternetIp | String | 42.2.X.X | The public IP address of the asset. |
| IntranetIp | String | 192.168.X.X | The private IP address of the asset. |
| Ip | String | 42.2.X.X | The public IP address of the asset. |
| Port | String | 22 | The port number. |
| ProcName | String | sshd | The name of the process that uses the port. |
| Proto | String | tcp | The network protocol of the port. |
| Uuid | String | 50d213b4-3a35- 427a-b8a5- 04b0c7e1fXX | The UUID of the asset that is associated with the port. |
| pid | String | 1 | The ID of the parent process. |
| RequestId | String | FAA793EF-5B14- 4CDD-B3E0- B14D4342C422 | The ID of the request. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyPortDetail &<Common request parameters>
```

Sample success responses `XML` format Cloud Security Management Cent

```xml
<Propertys>
    <InstanceName>test-***</InstanceName>
    <Uuid>50d213b4-3a35-427a-b8a5-04b0c7e1fXX</Uuid>
    <InternetIp>42.2.X.X</InternetIp>
    <Proto>tcp</Proto>
    <InstanceId>50d213b4-3a35-427a-b8a5-04b0c7e1fxxx</InstanceId>
    <Create>2019-05-13T10:39Z</Create>
    <ProcName>sshd</ProcName>
    <Ip>42.2.X.X</Ip>
    <Port>22</Port>
    <pid>1</pid>
    <IntranetIp>192.168.X.X</IntranetIp>
    <CreateTimestamp>1557715141000</CreateTimestamp>
    <BindIp>47.100.XX.XX</BindIp>
</Propertys> <PageInfo>
    <TotalCount>762</TotalCount>
    <PageSize>5</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>5</Count>
</PageInfo> <RequestId> FAA793EF-5B14-4CDD-B3E0-B14D4342C422</RequestId>
```

`JSON` format

```json
{
    "Propertys": {
        "InstanceName": "test-***",
        "Uuid": "50d213b4-3a35-427a-b8a5-04b0c7e1fXX",
        "InternetIp": "42.2.X.X",
        "Proto": "tcp",
        "InstanceId": "50d213b4-3a35-427a-b8a5-04b0c7e1fxxx",
        "Create": "2019-05-13T10:39Z",
        "ProcName": "sshd",
        "Ip": "42.2.X.X",
        "Port": 22,
        "pid": 1,
        "IntranetIp": "192.168.X.X",
        "CreateTimestamp": 1557715141000,
        "BindIp": "47.100.XX.XX"
    },
    "PageInfo": {
        "TotalCount": 762,
        "PageSize": 5,
        "CurrentPage": 1,
        "Count": 5
    },
    "RequestId": "FAA793EF-5B14-4CDD-B3E0-B14D4342C422"
}
```

#### DescribePropertyProcDetail

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yProcDetail | The operation that you want to perform. Set the value to DescribePropertyProcDetail. |
| Remark | String | No | 47.100.XX.XX | The name or IP address of the server. |
| Name | String | No | 8888 | The name of the process. |
| User | String | No | root | The user who runs the process. |
| Cmdline | String | No | ./8888 | The startup parameter of the process. |
| Uuid | String | No | c4678332-ef35- 4ad4-*** | The UUID of the asset that is associated with the process. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |  | The pagination information. |
| Count | Integer | 1 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 1 | The total number of entries returned. |

Cloud Security Management Cent Queries the details of a process.

**Request parameters**

**Response parameters**

| Propertys | Array of PropertyProc |  | An array that consists of the information about the process. |
|---|---|---|---|
| Cmdline | String | ./8888 | The startup parameter of the process. |
| Create | String | 2019-05- 15T11:08Z | The time when the data was last collected. |
| CreateTimesta mp | Long | 1565686951000 | The timestamp when the data was last collected. Unit: milliseconds. |
| EuidName | String | root | The permissions required to run the process. |
| InstanceId | String | c4678332-ef35- 4ad4-8358-*** | The ID of the asset that is associated with the process. |
| InstanceName | String | test-*** | The name of the asset that is associated with the process. |
| InternetIp | String | 40.2.x.x | The public IP address of the asset. |
| IntranetIp | String | 192.168.x.x | The private IP address of the asset. |
| Md5 | String | N/A | The MD5 hash value of the process file. |
| Name | String | 8888 | The name of the process. |
| Path | String | /root/Oracle/Middle ware/***/8888 | The path of the process. |
| Pid | String | 12826 | The ID of the process. |
| Pname | String | start***.s | The name of the parent process to which the process belongs. |
| StartTime | String | 2019-08-07 10:09:05 | The time when the process was started. The time is in the yyyy-MM-dd HH:mm:ss format. |
| User | String | root | The user who runs the process. |

Cloud Security Management Cent

| Uuid | String | c4678332-ef35- 4ad4-8358-6*** | The UUID of the asset that is associated with the process. |
|---|---|---|---|
| RequestId | String | 64388374-A309- 4191-8606- 3346CCA364B0 | The ID of the request. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyProcDetail &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Propertys>
    <Path>/root/Oracle/Middleware/***/8888</Path>
    <Pname>start***.s</Pname>
    <User>root</User>
    <InstanceId>c4678332-ef35-4ad4-8358-***</InstanceId>
    <StartTime>2019-08-07 10:09:05</StartTime>
    <Pid>12826</Pid>
    <EuidName>root</EuidName>
    <IntranetIp>192.168.x.x</IntranetIp>
    <Name>8888</Name>
    <InstanceName>test-***</InstanceName>
    <Uuid>c4678332-ef35-4ad4-8358-6***</Uuid>
    <InternetIp>40.2.x.x</InternetIp>
    <Create>2019-05-15T11:08Z</Create>
    <Cmdline>./8888</Cmdline>
    <CreateTimestamp>1565686951000</CreateTimestamp>
    <Md5>N/A</Md5>
</Propertys> <PageInfo>
    <TotalCount>1</TotalCount>
    <PageSize>5</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>1</Count>
</PageInfo> <RequestId>64388374-A309-4191-8606-3346CCA364B0</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yPortItem | The operation that you want to perform. Set the value to DescribePropertyPortItem. |
| ForceFlush | Boolean | No | true | Specifies whether to forcefully refresh the data that you want to query. |
| Port | String | No | 22 | The port number. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

Cloud Security Management Cent

```json
{
    "Propertys": {
        "Path": "/root/Oracle/Middleware/***/8888",
        "Pname": "start***.s",
        "User": "root",
        "InstanceId": "c4678332-ef35-4ad4-8358-***",
        "StartTime": "2019-08-07 10:09:05",
        "Pid": 12826,
        "EuidName": "root",
        "IntranetIp": "192.168.x.x",
        "Name": 8888,
        "InstanceName": "test-***",
        "Uuid": "c4678332-ef35-4ad4-8358-6***",
        "InternetIp": "40.2.x.x",
        "Create": "2019-05-15T11:08Z",
        "Cmdline": "./8888",
        "CreateTimestamp": 1565686951000,
        "Md5": "N/A"
    },
    "PageInfo": {
        "TotalCount": 1,
        "PageSize": 5,
        "CurrentPage": 1,
        "Count": 1
    },
    "RequestId": "64388374-A309-4191-8606-3346CCA364B0"
}
```

#### DescribePropertyPortItem

Queries information about all ports.

**Request parameters**

| PageSize | Integer | No | 5 | The number of entries to return on each page. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |  | The pagination information. |
| Count | Integer | 5 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 163 | The total number of entries returned. |
| PropertyItems | Array of PropertyItem |  | An array that consists of the information about the port. |
| Count | Integer | 495 | The number of servers that use the port. |
| Port | String | 22 | The number of the listening port. |
| Proto | String | tcp | The network protocol of the port. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

Cloud Security Management Cent

**Response parameters**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyPortItem &<Common request parameters>
```

Sample success responses `XML` format Cloud Security Management Cent

```xml
        <RequestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</RequestId>
        <PropertyItems>
       <Port>22</Port>
       <Proto>tcp</Proto>
       <Count>495</Count>
     </PropertyItems>
     <PropertyItems>
       <Port>111</Port>
       <Proto>tcp</Proto>
       <Count>43</Count>
     </PropertyItems>
     <PropertyItems>
       <Port>6000</Port>
       <Proto>tcp</Proto>
       <Count>2</Count>
     </PropertyItems>
     <PropertyItems>
       <Port>53</Port>
       <Proto>tcp</Proto>
       <Count>1</Count>
     </PropertyItems>
     <PropertyItems>
       <Port>80</Port>
       <Proto>tcp</Proto>
       <Count>38</Count>
     </PropertyItems>
        <PageInfo>
       <Count>5</Count>
       <PageSize>5</PageSize>
       <TotalCount>163</TotalCount>
       <CurrentPage>1</CurrentPage>
     </PageInfo>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yProcItem | The operation that you want to perform. Set the value to DescribePropertyProcItem. |

Cloud Security Management Cent

```json
{
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
  "PropertyItems": [
      {
        "Port": "22",
        "Proto": "tcp",
        "Count": 495
      },
      {
        "Port": "111",
        "Proto": "tcp",
        "Count": 43
      },
      {
        "Port": "6000",
        "Proto": "tcp",
        "Count": 2
      },
      {
        "Port": "53",
        "Proto": "tcp",
        "Count": 1
      },
      {
        "Port": "80",
        "Proto": "tcp",
        "Count": 38
      }
```

`],`

```json
  "PageInfo": {
      "Count": 5,
      "PageSize": 5,
      "TotalCount": 163,
      "CurrentPage": 1
    }
}
```

#### DescribePropertyProcItem

Queries information about all processes.

**Request parameters**

| ForceFlush | Boolean | No | true | Specifies whether to forcefully refresh the data that you want to query. |
|---|---|---|---|---|
| Name | String | No | test | The name of the process. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |  | The pagination information. |
| Count | Integer | 5 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 372 | The total number of entries returned. |
| PropertyItems | Array of PropertyProcIt em |  | An array that consists of the information about the process. |
| Count | Integer | 8888 | The number of servers on which the process runs. |
| Name | String | .ss | The name of the process. |
| RequestId | String | BD8AD4C6-A169- 4FA3-BA1F- ED40ED52973B | The ID of the request. |

Cloud Security Management Cent

**Response parameters**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyProcItem &<Common request parameters>
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

Cloud Security Management Cent Sample success responses `XML` format

```xml
  <PropertyItems>
        <Name>(sd-**)</Name>
        <Count>7</Count>
  </PropertyItems>
  <PropertyItems>
        <Name>6Cm***</Name>
        <Count>1</Count>
  </PropertyItems>
  <RequestId>BD8AD4C6-A169-4FA3-BA1F-ED40ED52973B</RequestId>
  <PageInfo>
        <Count>2</Count>
        <TotalCount>395</TotalCount>
        <PageSize>2</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
```

`JSON` format

```json
{
 "PropertyItems": [
  {
   "Name": "(sd-**)",
   "Count": 7
  },
  {
   "Name": "6Cm***",
   "Count": 1
  }
```

`],`

```json
 "RequestId": "BD8AD4C6-A169-4FA3-BA1F-ED40ED52973B",
 "PageInfo": {
  "Count": 2,
  "TotalCount": 395,
  "PageSize": 2,
  "CurrentPage": 1
 }
}
```

#### DescribePropertySoftwareDetail

Queries the details of a software asset.

**Request parameters**

| Action | String | Yes | DescribePropert ySoftwareDetail | The operation that you want to perform. Set the value to DescribePropertySoftwareDetail. |
|---|---|---|---|---|
| Remark | String | No | 47.100.XX.XX | The name or IP address of the server. |
| Name | String | No | tes*** | The name of the software. |
| Path | String | No | /etc/test | The directory in which the software is installed. |
| SoftwareVersion | String | No | 11 | The version of the software. |
| Uuid | String | No | 50d213b4-3a35- 427a-b8a5-*** | The ID of the instance on which the software is installed. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |  | The pagination information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 23 | The total number of entries returned. |
| Propertys | Array of PropertySoftw are |  | An array that consists of the details about the software. |
| Create | Long | 1565539587000 | The time when the data was last collected. Unit: milliseconds. |

Cloud Security Management Cent

**Response parameters**

| CreateTimesta mp | Long | 1565539587000 | The timestamp when the data was last collected. Unit: milliseconds. |
|---|---|---|---|
| InstallTime | String | 2017-09-07 10:54:49 | The time when the software was installed. The time is in the yyyy-MM-dd HH:mm:ss format. |
| InstallTimeSta mp | Long | 1565539587000 | The timestamp when the software was installed. Unit: milliseconds. |
| InstanceId | String | i-uf*** | The ID of the asset. |
| InstanceName | String | test | The name of the asset. |
| InternetIp | String | 47.100.XX.XX | The public IP address of the asset. |
| IntranetIp | String | 192.168.0.1 | The private IP address of the asset. |
| Ip | String | 47.100.XX.XX | The IP address that is displayed for the asset. Note If the asset has a public IP address, the public IP address is returned. Otherwise, the private IP address is returned. |
| Name | String | aaa base _ | The name of the software. |
| Path | String | /etc/test | The directory in which the software is installed. |
| Uuid | String | 4ef1115b-e423- 4b4b-b930-*** | The UUID of the asset. |
| Version | String | 11 | The version of the software. |
| RequestId | String | 9C5AE850-7140- 4DE6-B892- 055EB0D9F28A | The ID of the request. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertySoftwareDetail &<Common request parameters>
```

Cloud Security Management Cent Sample success responses `XML` format

```xml
<Propertys>
    <InstanceName>test</InstanceName>
    <Path>/etc/test</Path>
    <Uuid>4ef1115b-e423-4b4b-b930-***</Uuid>
    <InternetIp>47.100.XX.XX</InternetIp>
    <InstallTimeStamp>1565539587000</InstallTimeStamp>
    <InstanceId>i-uf***</InstanceId>
    <Version>11</Version>
    <InstallTime>2017-09-07 10:54:49</InstallTime>
    <Create>1565539587000</Create>
    <Ip>47.100.XX.XX</Ip>
    <IntranetIp>192.168.0.1</IntranetIp>
    <CreateTimestamp>1565539587000</CreateTimestamp>
    <Name>aaa_base</Name>
</Propertys> <PageInfo>
    <TotalCount>23</TotalCount>
    <PageSize>2</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>2</Count>
</PageInfo> <RequestId>9C5AE850-7140-4DE6-B892-055EB0D9F28A</RequestId>
```

`JSON` format

```json
{
    "Propertys": {
        "InstanceName": "test",
        "Path": "/etc/test",
        "Uuid": "4ef1115b-e423-4b4b-b930-***",
        "InternetIp": "47.100.XX.XX",
        "InstallTimeStamp": 1565539587000,
        "InstanceId": "i-uf***",
        "Version": 11,
        "InstallTime": "2017-09-07 10:54:49",
        "Create": 1565539587000,
        "Ip": "47.100.XX.XX",
        "IntranetIp": "192.168.0.1",
        "CreateTimestamp": 1565539587000,
        "Name": "aaa_base"
    },
    "PageInfo": {
        "TotalCount": 23,
        "PageSize": 2,
        "CurrentPage": 1,
        "Count": 2
    },
    "RequestId": "9C5AE850-7140-4DE6-B892-055EB0D9F28A"
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert ySoftwareItem | The operation that you want to perform. Set the value to DescribePropertySoftwareItem. |
| ForceFlush | Boolean | No | true | Specifies whether to forcefully refresh the data that you want to query. |
| Name | String | No | test | The name of the software that you want to query. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |  | The pagination information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 5037 | The total number of entries returned. |
| PropertyItems | Array of PropertySoftw areItem |  | An array that consists of the returned software assets. |

Cloud Security Management Cent

#### DescribePropertySoftwareItem

Queries information about all software assets.

**Request parameters**

**Response parameters**

| Count | Integer | 23 | The number of servers on which the software is installed. |
|---|---|---|---|
| Name | String | aaa base _ | The name of the returned software. |
| RequestId | String | 3A85CFCF-05C8- 451A-9E41- C0D5E96BA407 | The ID of the request. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertySoftwareItem &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <PageInfo>
       <Count>2</Count>
       <PageSize>2</PageSize>
       <TotalCount>5037</TotalCount>
       <CurrentPage>1</CurrentPage>
   </PageInfo>
   <PropertyItems>
       <Name>a11y-profile-manager-indicator</Name>
       <Count>1</Count>
   </PropertyItems>
   <PropertyItems>
       <Name>aaa_base</Name>
       <Count>23</Count>
   </PropertyItems>
   <requestId>3A85CFCF-05C8-451A-9E41-C0D5E96BA407</requestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yUserDetail | The operation that you want to perform. Set the value to DescribePropertyUserDetail. |
| Remark | String | No | 47.100.XX.XX | The name or IP address of the server. |
| User | String | No | tes*** | The name of the account that you want to query. |
| IsRoot | String | No | 0 | Specifies whether the account has root permissions. Valid values: 0: no 1: yes |
| Uuid | String | No | 50d213b4-*****- 427a-b8a5- 04b0c7****** | The UUID of the asset that you want to query. |

Cloud Security Management Cent

```json
{
  "PageInfo": {
      "Count": 2,
      "PageSize": 2,
      "TotalCount": 5037,
      "CurrentPage": 1
    },
    "PropertyItems": [
      {
        "Name": "a11y-profile-manager-indicator",
        "Count": 1
      },
      {
        "Name": "aaa_base",
        "Count": 23
      }
```

`],`

```json
     "requestId": "3A85CFCF-05C8-451A-9E41-C0D5E96BA407"
}
```

#### DescribePropertyUserDetail

Queries the details of a specified account.

**Request parameters**

| CurrentPage | Integer | No | 1 | The number of the page to return. |
|---|---|---|---|---|
| PageSize | Integer | No | 2 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |  | The pagination information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 384 | The total number of entries returned. |
| Propertys | Array of PropertyUser |  | An array that consists of the details of the account. |
| AccountsExpir ationDate | String | None | This parameter is deprecated. |
| Create | String | 2022-01- 03T06:43Z | The time when the data was last collected. The time is in the yyyy-MM-dd HH:mm:ss format. |
| CreateTimesta mp | Long | 1565644643000 | The timestamp when the data was collected. Unit: milliseconds. |
| GroupNames | List | adm | The name of the user group. |
| InstanceId | String | 02c4a5dc-****- 483a-9015- f972b****** | The ID of the asset. |
| InstanceName | String | e21g06001.cloud.g 06.xxx | The name of the asset. |
| InternetIp | String | 47.100.XX.XX | The public IP address of the asset. |

Cloud Security Management Cent

**Response parameters**

| IntranetIp | String | 192.168.0.1 | The private IP address of the asset. |
|---|---|---|---|
| Ip | String | 47.100.XX.XX | The IP address of the asset. |
| IsRoot | String | 0 | Indicates whether the account has the root permissions. Valid values: 0: no 1: yes |
| LastLoginIp | String | 47.100.XX.XX | The source IP address of the last logon. |
| LastLoginTime | String | 2022-01-03 06:33:33 | The time of the last logon. The time is in the yyyy-MM-dd HH:mm:ss format. |
| LastLoginTime stamp | Long | 1565644643000 | The timestamp of the last logon. Unit: milliseconds. |
| PasswordExpir ationDate | String | None | This parameter is deprecated. |
| Status | String | 0 | The logon status of the account. Valid values: 0: The account cannot be used for logon. 1: The account can be used for logon. |
| User | String | adm | The name of the account. |
| Uuid | String | 02c4a5dc-c2d2- 483a-9015- f972b4****** | The UUID of the asset. |
| RequestId | String | FAA793EF-5B14- 4CDD-B3E0- B14D4342C422 | The ID of the request. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyUserDetail &<Common request parameters>
```

Sample success responses `XML` format Cloud Security Management Cent

```xml
<Propertys>
    <Status>0</Status>
    <IsRoot>0</IsRoot>
    <User>adm</User>
    <InstanceId>02c4a5dc-****-483a-9015-f972b******</InstanceId>
    <LastLoginIp>47.100.XX.XX</LastLoginIp>
    <Ip>47.100.XX.XX</Ip>
    <IntranetIp>192.168.0.1</IntranetIp>
    <AccountsExpirationDate>None</AccountsExpirationDate>
    <InstanceName>e21g06001.cloud.g06.xxx</InstanceName>
    <LastLoginTime>2022-01-03 06:33:33</LastLoginTime>
    <Uuid>02c4a5dc-c2d2-483a-9015-f972b4******</Uuid>
    <InternetIp>47.100.XX.XX</InternetIp>
    <LastLoginTimestamp>1565644643000</LastLoginTimestamp>
    <Create>2022-01-03T06:43Z</Create>
    <CreateTimestamp>1565644643000</CreateTimestamp>
    <PasswordExpirationDate>None</PasswordExpirationDate>
    <GroupNames>adm</GroupNames>
</Propertys> <PageInfo>
    <TotalCount>384</TotalCount>
    <PageSize>2</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>2</Count>
</PageInfo> <RequestId>FAA793EF-5B14-4CDD-B3E0-B14D4342C422</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yUserItem | The operation that you want to perform. Set the value to DescribePropertyUserItem. |
| ForceFlush | Boolean | No | true | Specifies whether to forcefully refresh the data that you want to query. |
| User | String | No | adm | The account information about the asset fingerprint. |

Cloud Security Management Cent

```json
{
    "Propertys": {
        "Status": 0,
        "IsRoot": 0,
        "User": "adm",
        "InstanceId": "02c4a5dc-****-483a-9015-f972b******",
        "LastLoginIp": "47.100.XX.XX",
        "Ip": "47.100.XX.XX",
        "IntranetIp": "192.168.0.1",
        "AccountsExpirationDate": "None",
        "InstanceName": "e21g06001.cloud.g06.xxx",
        "LastLoginTime": "2022-01-03 06:33:33",
        "Uuid": "02c4a5dc-c2d2-483a-9015-f972b4******",
        "InternetIp": "47.100.XX.XX",
        "LastLoginTimestamp": 1565644643000,
        "Create": "2022-01-03T06:43Z",
        "CreateTimestamp": 1565644643000,
        "PasswordExpirationDate": "None",
        "GroupNames": "adm"
    },
    "PageInfo": {
        "TotalCount": 384,
        "PageSize": 2,
        "CurrentPage": 1,
        "Count": 2
    },
    "RequestId": "FAA793EF-5B14-4CDD-B3E0-B14D4342C422"
}
```

#### DescribePropertyUserItem

Queries the account information about an asset.

**Request parameters**

| CurrentPage | Integer | No | 1 | The number of the page to return. |
|---|---|---|---|---|
| PageSize | Integer | No | 2 | The number of entries to return on each page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |  | The pagination information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 114 | The total number of entries returned. |
| PropertyItems | Array of PropertyUserIt em |  | An array that consists of the account information. |
| Count | Integer | 384 | The number of servers that belong to the account. |
| User | String | adm | The name of the account. |
| RequestId | String | 76068BE2-F9C4- 4EDD-967B- F503B8CCXXXX | The ID of the request. |

Cloud Security Management Cent

**Response parameters**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyUserItem &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeModule Config | The operation that you want to perform. Set the value to DescribeModuleConfig. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

Cloud Security Management Cent

```xml
<PageInfo>
    <TotalCount>114</TotalCount>
    <PageSize>2</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>2</Count>
</PageInfo> <RequestId>76068BE2-F9C4-4EDD-967B-F503B8CCXXXX</RequestId> <PropertyItems>
    <User>adm</User>
    <Count>384</Count>
</PropertyItems>
```

`JSON` format

```json
{
    "PageInfo": {
        "TotalCount": 114,
        "PageSize": 2,
        "CurrentPage": 1,
        "Count": 2
    },
    "RequestId": "76068BE2-F9C4-4EDD-967B-F503B8CCXXXX",
    "PropertyItems": {
        "User": "adm",
        "Count": 384
    }
}
```

#### DescribeModuleConfig

Queries the configurations of asset fingerprint modules.

**Request parameters**

**Response parameters**

| Success | Boolean | true | Indicates whether the request is successful. |
|---|---|---|---|
| Count | Integer | 2 | The number of module configurations. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| ModuleConfigL ist | Array |  | The list of module configurations. |
| ConfigName | String | timescan | The name of the configuration. |
| ModuleName | String | alihids | The name of the template. |
| Items | Array |  | The list of configuration items. |
| InstanceId | String | lb-xxx | The ID of the instance. |
| InstanceName | String | ssxxxxxxxx | The name of the instance. |
| GroupId | Integer | 173 | The ID of the group. |
| Ip | String | 2.2.2.2 | The IP address of the instance. |
| Region | String | outside-of-aliyun | The region where the instance is deployed. |
| Uuid | String | lb-xxxx-xxxx-xxxx- xxxx | The UUID of the server. |

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeModuleConfig &<Common request parameters>
```

Sample success responses `XML` format Cloud Security Management Cent

```xml
<code>200</code> <data>
    <Count>2</Count>
    <ModuleConfigList>
        <ConfigName>timescan</ConfigName>
        <ModuleName>alihids</ModuleName>
        <Items>
            <InstanceName>ssxxxxxxxx</InstanceName>
            <Uuid>lb-xxxx-xxxx-xxxx-xxxx</Uuid>
            <InstanceId>lb-xxx</InstanceId>
            <Ip>2.2.2.2</Ip>
            <Region>cn-qingdao</Region>
            <GroupId>173</GroupId>
        </Items>
        <Items>
            <InstanceName>3a04702ca5a0</InstanceName>
            <Uuid>inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6</Uuid>
            <Ip>192.1.2.3</Ip>
            <Region>outside-of-aliyun</Region>
            <GroupId>343</GroupId>
        </Items>
    </ModuleConfigList>
    <ModuleConfigList>
        <ConfigName>sysvulfix</ConfigName>
        <ModuleName>alihids</ModuleName>
        <Items>
            <InstanceName>xx</InstanceName>
            <Uuid>lb-xxx</Uuid>
            <InstanceId>lb-xxx</InstanceId>
            <Ip>2.2.2.2</Ip>
            <Region>cn-qingdao</Region>
            <GroupId>173</GroupId>
        </Items>
        <Items>
            <InstanceName>3a04702ca5a0</InstanceName>
            <Uuid>inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6</Uuid>
            <Ip>192.168.5.3</Ip>
            <Region>outside-of-aliyun</Region>
            <GroupId>343</GroupId>
        </Items>
    </ModuleConfigList>
</data> <requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId> <success>true</success>
```

`JSON` format Cloud Security Management Cent

```json
{
  "code": 200,
  "data": {
    "Count": 2,
    "ModuleConfigList": [{
        "ConfigName": "timescan",
        "ModuleName": "alihids",
        "Items": [{
            "InstanceName": "ssxxxxxxxx",
            "Uuid": "lb-xxxx-xxxx-xxxx-xxxx",
            "InstanceId": "lb-xxx",
            "Ip": "2.2.2.2",
            "Region": "cn-qingdao",
            "GroupId": 173
          },
          {
            "InstanceName": "3a04702ca5a0",
            "Uuid": "inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
            "Ip": "192.1.2.3",
            "Region": "outside-of-aliyun",
            "GroupId": 343
          }
```

]

```json
      },
      {
        "ConfigName": "sysvulfix",
        "ModuleName": "alihids",
        "Items": [{
            "InstanceName": "xx",
            "Uuid": "lb-xxx",
            "InstanceId": "lb-xxx",
            "Ip": "2.2.2.2",
            "Region": "cn-qingdao",
            "GroupId": 173
          },
          {
            "InstanceName": "3a04702ca5a0",
            "Uuid": "inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
            "Ip": "192.168.5.3",
            "Region": "outside-of-aliyun",
            "GroupId": 343
          }
```

]

```
      }
```

]

```json
  },
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
  "success": true
}
```

**Error codes**

For a list of error codes, see Error codes.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeExpose dInstanceList | The operation that you want to perform. Set the value to DescribeExposedInstanceList. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| GroupId | Long | No | 9469268 | The ID of the server group. |
| VulStatus | Boolean | No | true | Specifies whether the server has vulnerabilities. Valid values: true: yes false: no |
| HealthStatus | Boolean | No | true | Specifies whether baseline risks exist in the server. |
| ExposureCompo nent | String | No | openssl | The server component that is exposed on the Internet. |
| ExposurePort | String | No | 22 | The port that is exposed on the Internet. |
| ExposureIp | String | No | 116.12.XX.XX | The public IP address of the server. |
| InstanceId | String | No | i- bp1g6wxdwps7s 9dz**** | The ID of the server. |
| InstanceName | String | No | abc centos7.2 0 _ _ 05 | The name of the server. |

Cloud Security Management Cent

### Asset exposure

#### DescribeExposedInstanceList

Queries the assets that are exposed.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ExposedInstan ces | Array of ExposedInstan ce |  | An array that consists of the details of the exposed asset. |
| AsapVulCount | Integer | 0 | The number of high-risk vulnerabilities that are exposed on the Internet and can be exploited by attackers. |
| ExploitHealthC ount | Integer | 0 | The number of baseline risks that can be exploited. |
| ExposureCom ponent | String | openssl,openssh | The server component that is exposed on the Internet. |
| ExposureIp | String | 116.12.XX.XX | The public IP address that is exposed on the Internet. |
| ExposurePort | String | 22 | The port that is exposed on the Internet. |
| ExposureType | String | INTERNET IP _ | The resource from which the asset is exposed. Valid values: INTERNET IP: the IP address of the _ Elastic Compute Service (ECS) instance SLB: the public IP address of the Server Load Balancer (SLB) instance EIP: the elastic IP address (EIP) DNAT: the NAT gateway that connects to the Internet by using the DNAT feature |
| ExposureTypeI d | String | i-ew11313a**** | The ID of the instance from which the asset is exposed. The value of this parameter varies based on the value of the ExposureType parameter. If the value of the ExposureType parameter is INTERNET IP, the value _ of this parameter is an empty string. If the value of the ExposureType parameter is SLB, the value of this parameter is the ID of the Internet- facing SLB instance. If the value of the ExposureType parameter is EIP, the value of this parameter is the ID of the EIP. If the value of the ExposureType parameter is DNAT, the value of this parameter is the ID of the NAT gateway. |

Cloud Security Management Cent

| GroupId | Long | 9469268 | The ID of the server group. |
|---|---|---|---|
| GroupName | String | Ungrouped | The name of the server group. |
| InstanceId | String | i- bp1g6wxdwps7s9d z**** | The ID of the server. |
| InstanceName | String | abc centos7.2 005 _ _ | The name of the server. |
| InternetIp | String | 116.12.XX.XX | The public IP address of the server. |
| IntranetIp | String | 192.168.XX.XX | The private IP address of the server. |
| LaterVulCount | Integer | 0 | The number of medium-risk vulnerabilities that are exposed on the Internet and can be exploited by attackers. |
| NntfVulCount | Integer | 0 | The number of low-risk vulnerabilities that are exposed on the Internet and can be exploited by attackers. |
| RegionId | String | cn-hangzhou | The ID of the region where the server resides. |
| TotalVulCount | Integer | 0 | The total number of vulnerabilities that are exposed on the Internet and can be exploited by attackers. |
| Uuid | String | dd803d9e-a337- 4add-9c5b- 7d503e08**** | The UUID of the server. |
| PageInfo | Struct |  | The pagination information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 2 | The total number of entries returned. |

Cloud Security Management Cent

| RequestId | String | 598A4A61-ABA7- 456B-8725- 7378258276D9 | The ID of the request. |
|---|---|---|---|

Cloud Security Management Cent Sample requests

```
http(s)://[Endpoint]/?Action=DescribeExposedInstanceList &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PageInfo>
    <TotalCount>2</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>2</Count>
</PageInfo> <RequestId>598A4A61-ABA7-456B-8725-7378258276D9</RequestId> <ExposedInstances>
    <GroupName>Ungrouped</GroupName>
    <TotalVulCount>0</TotalVulCount>
    <ExposureType>INTERNET_IP</ExposureType>
    <InstanceId>i-bp1g6wxdwps7s9dz****</InstanceId>
    <ExposureComponent>openssl,openssh</ExposureComponent>
    <ExposurePort>22</ExposurePort>
    <NntfVulCount>0</NntfVulCount>
    <AsapVulCount>0</AsapVulCount>
    <ExploitHealthCount>0</ExploitHealthCount>
    <IntranetIp>192.168.XX.XX </IntranetIp>
    <GroupId>9469268</GroupId>
    <InstanceName>abc_centos7.2_005 </InstanceName>
    <Uuid>dd803d9e-a337-4add-9c5b-7d503e08****</Uuid>
    <ExposureIp>116.12.XX.XX </ExposureIp>
    <ExposureTypeId>i-ew11313a****</ExposureTypeId>
    <InternetIp>116.12.XX.XX</InternetIp>
    <LaterVulCount>0</LaterVulCount>
    <RegionId>cn-hangzhou</RegionId>
</ExposedInstances>
```

`JSON` format Cloud Security Management Cent

```json
{"PageInfo": {"TotalCount":"2","PageSize":"20","CurrentPage":"1","Count":"2"},"RequestId":"598A4A61- ABA7-456B-8725-7378258276D9","ExposedInstances": [{"GroupName":"Ungrouped","TotalVulCount":"0","ExposureType":"INTERNET_IP","InstanceId":" bp1g6wxdwps7s9dz****","ExposureComponent":"openssl,openssh","ExposurePort":"22","NntfVulC nt":"0","AsapVulCount":"0","ExploitHealthCount":"0","IntranetIp":"192.168.XX.XX\t","Group ":"9469268","InstanceName":"abc_centos7.2_005\t","Uuid":"dd803d9e-a337-4add-9c5b-7d503e 08****","ExposureIp":"116.12.XX.XX\t","ExposureTypeId":"iew11313a****","InternetIp":"116.12.XX.XX","LaterVulCount":"0","RegionId":"cn-hangzhou"} ]}
```
