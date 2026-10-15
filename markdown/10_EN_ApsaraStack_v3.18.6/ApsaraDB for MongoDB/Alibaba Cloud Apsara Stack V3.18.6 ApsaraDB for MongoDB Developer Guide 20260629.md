---
title: "ApsaraDB for MongoDB Developer Guide 20260629"
product_version: "V3.18.6"
pdf_pages: 223
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 ApsaraDB for MongoDB Developer Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E6%95%B0%E6%8D%AE%E5%BA%93%20MongoDB%20%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20ApsaraDB%20for%20MongoDB%20Developer%20Guide%2020260629.pdf"
converter: line-classifier (PyMuPDF)
---

# ApsaraDB for MongoDB Developer Guide 20260629

## Getting started

### Apsara Stack documentation

This topic describes how to find the required documentation when you call an API operation of an Apsara Stack service.

**Flowchart**

You can follow the procedure described in the following figure to view the specific documentation.

**Prerequisites**

The Apsara Stack version is obtained from an O&M personnel or operations administrator. You can go to the Apsara Stack documentation center to view the desired documentation.
1. Go to the Apsara Stack documentation center.
2. Click the **Enterprise**, **Agility&XStack**, or **All-in-one** tab based on the Apsara Stack
version that you use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the Apsara Stack service whose documentation you
want to view.
5. In the product documentation section, click **View Details** or **Download PDF**.

### Procedure for API calls

By default, Apsara Stack Enterprise Edition V3.16.0 and later versions use the point of presence (POP) gateway to deliver the same user experience as in the Alibaba Cloud public cloud. This topic describes how to use the POP gateway to call Apsara Stack API operations.

**Flowchart**

1. Obtain an AccessKey pair.
For more information, see Obtain an AccessKey pair.

**Note**

We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and Apsara Stack services.
2. Obtain a region ID.
For more information, see Obtain common header parameters.
3. Obtain an organization ID and a resource set ID.
Obtain an organization ID by calling the GetOrganizationList operation. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Develop er Guide. Obtain a resource set ID by calling the ListResourceGroup operation. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide.

**Note**

When you call an API operation, set the `<x-acs-organizationid>` header to the organization ID that you queried, and set the `<x-acs-resourcegroupid>` header to the resource set ID that you queried. This way, you can query resources in the specified organization and resource set. If you do not specify the `<x-acs-organizationid>` parameter, the organization to which the current user belongs is used. If you do not specify the `<x-acs-resourcegroupid>` parameter, this parameter is left empty. If you specify a resource set ID, you must also specify an organization ID.
4. View the developer guide of the cloud service that you want to use to learn how to make
the API call. Obtain the developer guide of the cloud service that you want to use. This way, you can learn the features of API operations and the calling of the API operations. For more information, see Apsara Stack documentation.
5. Obtain the endpoint of ApsaraDB for MongoDB.
6. Obtain the SDK of ApsaraDB for MongoDB and make an API call.

## Preparations

### Obtain the information and

**the endpoint of an API operation**

To call an API operation of a cloud service, you must obtain the information about the operation, including the service code, operation name, and API version.

**Background information**

The API information on the debugging page of the Apsara Uni-manager Management Console is for reference only. For more information about how to call API operations, see the developer guides of cloud services. If the information on the debugging page is different from that in the developer guide of a cloud service, the information in the developer guide prevails.
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
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

### Obtain an AccessKey pair

AccessKey pairs are classified into AccessKey pairs assigned by Resource Access Management (RAM) and those assigned by Security Token Service (STS). You can use either type of AccessKey pair for authentication when you call operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign an AccessKey pair for authentication. An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An access credential that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

**Warning**

The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, click the profile picture and then click **User**
**Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of your account.

**Note**

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. Click **Management Accesskey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### Obtain common header

**parameters**

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
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top
navigation bar.
4. Move the pointer over the
icon and choose **Platform** > **Apsara Uni-manager**. Select
**2019-05-10** from the **Version** drop-down list.
5. Search for the `ListResourceGroup` operation and debug the operation online. Obtain the
resource set ID from the **id** parameter on the **Call Result** tab. For more information about this operation, see the ListResourceGroup topic in Apsara Uni-manager Operations Console Developer Guide.

**Obtain an instance ID**

You can obtain an instance ID from the instance list page of the Apsara Uni-manager Management Console. For example, you can perform the following steps to obtain the ID of an ApsaraDB for MongoDB instance:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Database Services** > **ApsaraDB for**
**MongoDB**.
3. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances** based on the instance type.
4. In the instance list that appears, find the instance whose ID you want to obtain and obtain
its ID in the **Instance ID/Name** column.

**Response parameters**

The following table describes the additional response parameters that are returned by default when you call API operations to query the instances of cloud services.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of a resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of an organization. |

## Call examples for SDK for

**Java**

### Getting started

This topic describes how to obtain and use Apsara Stack SDK for Java. You can obtain an authorized Apsara Stack tenant account and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret before you can use Apsara Stack SDK for Java. You can obtain your AccessKey pair in the Apsara Uni-manager Management Console. For more information, see Obtain an AccessKey pair. Obtain the endpoint of ApsaraDB for MongoDB. For more information, see Obtain the information about an API operation. Apsara Stack SDK for Java V1.8 or later is installed. If you use Apache Maven to manage Java projects, import JAR files to the pom.xml file of the projects. To use an Apsara Stack SDK, you must install the SDK core library and the Apsara Stack SDK. We recommend that you use V4.5.17 or later for the SDK core library. In this example, the SDK V3.6.3 is used. To use Apsara Stack SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.

**Note**

Replace the variables in the following sample code with actual values. Do not retain the angle brackets (<>) in the final code. The following section describes the variables. <yourRegionID>: Replace this variable with your region ID. <yourAccessKeyID>: Replace this variable with your AccessKey ID. <yourAccessKeySecret>: Replace this variable with your AccessKey secret. <yourDBInstanceId>: Replace this variable with your ApsaraDB for MongoDB instance ID.

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.google.gson.Gson; import java.util.*; import com.aliyuncs.dds.model.v20151201.*;
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourAccessKeyID>", "<yourAccessKeySecret>");
        IAcsClient client = new DefaultAcsClient(profile);
        DescribeAccountsRequest request = new DescribeAccountsRequest();
        request.setDBInstanceId("<yourDBInstanceId>");
        try {
            DescribeAccountsResponse response = client.getAcsResponse(request);
            System.out.println(new Gson().toJson(response));
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

### Use SDK

#### Install ApsaraDB for MongoDB SDK for

**Java**

This topic describes how to install and use ApsaraDB for MongoDB SDK for Java. Apsara Stack SDK for Java V1.8 or later is supported. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK package. To use ApsaraDB for MongoDB SDK for Java, you must install the core library of Apsara Stack SDK for Java and ApsaraDB for MongoDB SDK for Java. We recommend that you use V4.5.17 or later for the core library of Apsara Stack SDK for Java. In this example, ApsaraDB for MongoDB SDK for Java uses V3.6.3. For example, to use ApsaraDB for MongoDB SDK for Java, you must install the core library of Apsara Stack SDK for Java and ApsaraDB for MongoDB SDK for Java, and then add the following dependencies to the pom.xml file. For more information, see SDK Center.

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency> <!-- dds java sdk --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-dds</artifactId>
    <version>3.6.3</version>
</dependency>
```

#### Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you can use an AccessKey pair for identity verification. Apsara Stack SDK for Java supports identity verification based on AccessKey pairs. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you use an AccessKey pair to access Apsara Stack, you must configure your credential when initializing the client.

**Note**

Do not disclose any code that may contain your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack account may be compromised.

```xml
DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", " <yourAccessKeyID>", "<yourAccessKeySecret>")
```

**Note**

You must use actual values to replace the variables in the preceding sample code. Do not retain the angle brackets (<>) in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret.

#### Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements.

**Note**

You must use actual values to replace the variables in the following sample code. Do not retain the angle brackets (<>) in the final code. The following list describes the variables: <readTimeout>: Specify the read timeout period based on your business requirements. Unit: milliseconds. <connectionTimeout>: Specify the connection timeout period based on your business requirements. Unit: milliseconds. <maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER. <maxRequests>: Specify the maximum number of requests based on your business requirements. The supported data type is INTEGER. <http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy.

```
// Obtain the HttpClientConfig object. HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Specify whether to ignore certificates. clientConfig.setIgnoreSSLCerts(true); // (Optional) Specify the read timeout period. Unit: milliseconds. clientConfig.setReadTimeoutMillis(<readTimeout>); // (Optional) Specify the connection timeout period. Unit: milliseconds. clientConfig.setConnectionTimeoutMillis(<connectionTimeout>); // (Optional) Specify the maximum number of requests that are supported by each server. The supported data type is INTEGER. clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>); // (Optional) Specify the maximum number of requests. The supported data type is INTEGE
```

`R.`

```
clientConfig.setMaxRequests(<maxRequests>); // (Optional) Specify the protocol type. clientConfig.setProtocolType(ProtocolType.HTTP); /** (Optional) Specify whether to configure the proxy based on your business requirements. The following code is available: clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`Or`

```
clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>"); Replace https://192.168.XX.XX:33XX with the actual IP address and port of the proxy.
```

`*/`

```
profile.setHttpClientConfig(clientConfig);
```

#### Initiate a request

This topic describes how to use ApsaraDB for MongoDB SDK for Java to initiate a request.
1. Create an ACS client.

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
The naming convention for requests is ${apiName}Request , where **${apiName}** indicates the API name, such as DescribeAccounts. When you use the SDKs of multiple services, different requests may share the same name. Make sure to differentiate different requests by their SDK.

```
DescribeAccountsRequest request = new DescribeAccountsRequest();
      request.setDBInstanceId("dds-********");
      request.setAccountName("root");
```

3. Initiate the request and handle the response.

```
DescribeAccountsResponse response = client.getAcsResponse(request);
```

In normal cases, all returned fields are deserialized into the response. You can directly call `response.getXXX()` to obtain the response fields.

```
AccountData := response.getData()
```

If an exception occurs or you need the original HTTP response, use `doAction()` to obtain the original response.

```
HttpResponse response = client.doAction(request);
```

#### Troubleshooting

If the server or SDK encounters an error when you use SDK for Java, it returns an error response. The error response contains an error code and an error message. In most cases, you do not need to handle the errors returned by SDK for Java. You need to only handle the errors returned by the server based on error messages. `ServerException` indicates a server error. `ClientException` indicates an SDK error. For example, when the following error occurs, you can modify the AccessKey ID based on the error message to solve the problem:

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

If you want to handle SDK errors, refer to the following example to write your code:

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handle the response.
    // ...
}catch (ServerException e){
    // You can add your logic to handle errors.
    // For example, print the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If the error persists, you can submit a ticket with the request ID included.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // You can add your logic to handle errors.
    // For example, print the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
}
```

## Call examples for SDK for

**Python**

### Getting started

This topic describes how to obtain and use ApsaraDB for MongoDB SDK for Python. You can obtain an Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret before you can use Apsara Stack SDK for Python. For more information, see Obtain an AccessKey pair. You can obtain the endpoint of ApsaraDB for MongoDB. For more information, see Obtain the information about an API operation.
1. Install the SDK core library.
If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library of Apsara Stack SDK for Python:

```
pip3 install aliyun-python-sdk-core-v3
```

2. Install ApsaraDB for MongoDB SDK for Python.
The following example shows how to install the ApsaraDB for MongoDB SDK for Python. If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-dds
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-dds
```

To use ApsaraDB for MongoDB SDK for Python, perform the following steps:
1. Create a client instance. Before you create a client instance, you must obtain a region ID,
an AccessKey ID, and an AccessKey secret.
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.

**Note**

Replace the variables in the following sample code with actual values. Do not retain the angle brackets (<>) in the final code. The following section describes the variables. <yourRegionID>: Replace this variable with your region ID. <yourAccessKeyID>: Replace this variable with your AccessKey ID. <yourAccessKeySecret>: Replace this variable with your AccessKey secret. <yourDBInstanceId>: Replace this variable with your ApsaraDB for MongoDB instance ID.

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential from aliyunsdkdds.request.v20151201.DescribeAccountsRequest import credentials = AccessKeyCredential('<yourAccessKeyID>', '<yourAccessKeySecret>') client = AcsClient(region_id='<yourRegionID>', credential=credentials) request.set_accept_format('json') request.set_DBInstanceId("<yourDBInstanceId>") response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

### Use SDK

#### Install ApsaraDB for MongoDB SDK for

**Python**

This topic describes how to install the core library of Apsara Stack SDK for Python and ApsaraDB for MongoDB SDK for Python.

**Background information**

To use a service SDK, you must install the core library of Apsara Stack SDK for Python. To use ApsaraDB for MongoDB SDK for Python, you must install the core library of Apsara Stack SDK for Python and ApsaraDB for MongoDB SDK for Python.

**Install the core library of Apsara Stack SDK for Python**

Apsara Stack SDK for Python supports Python 2.6.x, 2.7.x, as well as 3.x and later. You can use the pip command to install Apsara Stack SDK for Python. If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-core-v3
```

If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-dds
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-dds
```

#### Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you can use an AccessKey pair for identity verification. Apsara Stack SDK for Python supports identity verification based on AccessKey pairs. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you use an AccessKey pair to access Apsara Stack, you must configure your credential when initializing the client.

**Important**

Do not disclose any code that may contain your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack account may be compromised.

```
clt = client.AcsClient(<yourRegionID>, <yourAccessKeyID>, <yourAccessKeySecret>)
```

**Note**

In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret.

#### Set HTTPS requests

Apsara Stack SDK for Python allows you to initiate API requests over HTTP and HTTPS. You can specify the HTTP or HTTPS protocol for a specific request, or set a global default protocol.

**Note**

The default HTTP or HTTPS protocol of a service takes precedence over the global default protocol.

**Add OpenSSL support**

The HTTPS protocol support of Apsara Stack SDK for Python is based on the OpenSSL support in Python. To use Apsara Stack SDK for Python to send HTTPS requests, you must add OpenSSL support in Python. OpenSSL supports TLS 1.2 and later. Run the `python -c "import ssl"` command to check whether your Python environment supports OpenSSL. If the error message `ImportError: No module named ssl` is not returned, OpenSSL is already supported. Otherwise, run the following command to install it:

```
pip install pyopenssl
```

**Set the protocol to HTTP or HTTPS for a single request**

The following sample code provides an example on how to set HTTPS as the protocol for a request:

```bash
request = DescribeInstancesRequest() request.set_protocol_type("https")
# Set the value to https or http.
```

**Set a global default protocol**

The following sample code provides an example on how to set a global default protocol:

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request.
```

#### Initiate a request

This topic describes how to use ApsaraDB for MongoDB SDK for Python to initiate a request. The DescribeAccounts operation is used in the example.
1. Import ApsaraDB for MongoDB SDK for Python.

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential from aliyunsdkdds.request.v20151201.DescribeAccountsRequest import
```

2. Create an ACS client.

**Note**

The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret.

```
credentials = AccessKeyCredential('<yourAccessKeyID>', '<yourAccessKeySecret>') client = AcsClient(region_id='<yourRegionID>', credential=credentials)
```

3. Create a request object.

**Note**

<yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID.

```
request.set_accept_format('json') request.set_DBInstanceId("<yourDBInstanceId>")
```

4. Initiate the request and process the response.

```python
response = client.do_action_with_exception(request)
# python2:  print response
print(str(response, encoding='utf-8'))
```

#### Handle errors

If an error occurs on the server side or SDK side when you use the Python SDK, the Python SDK returns the corresponding exception message. An exception message contains the detailed error information, namely the error code and the error message. Generally, you are not required to handle the errors returned by the Python SDK. You are only required to handle the errors on the server side according to the error message. `ServerException` is the error message on the server side. `ClientException` is the error message on the SDK side. For example, if the following error occurs, modify the ID of AccessKey according to the detailed error message.

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

To handle the errors returned by the Python SDK, see the following code example for reference:

```bash
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
    # Add your own error handling logic here.
    # For example, print the detailed error message.
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

## Call examples for SDK for

**Go**

### Getting started

This topic describes how to obtain and use ApsaraDB for MongoDB SDK for Go.

**Environment requirements**

An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret.

**Install the core library of Apsara Stack SDK for Go.**

Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core library of Apsara Stack SDK for Go:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

The following code provides an example on how to use ApsaraDB for MongoDB SDK for Go.
1. Initialize a client instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exceptions.

**Note**

In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID.

```java
package main import (
    "fmt"
      dds "github.com/aliyun/alibaba-cloud-sdk-go/services/dds"
```

)

```
func main() {
    client, err := dds.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>",
"<yourAccessKeySecret>")
    request.Scheme = "https"
    request.DBInstanceId = "<yourDBInstanceId>"
    response, err := client.DescribeAccounts(request)
    if err != nil {
        fmt.Print(err.Error())
    }
    fmt.Printf("response is %#v\n", response)
}
```

4. (Optional) Switch to HTTP or HTTPS.

```
request.Scheme = "HTTPS"
```

### Use SDK

#### Install the core package of SDK for Go

This topic describes how to install the core package of SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you can use an AccessKey pair for identity verification. Apsara Stack SDK for Go supports identity verification based on AccessKey pairs. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you use an AccessKey pair to access Apsara Stack, you must configure your credential when initializing the client.

**Important**

Do not disclose any code that may contain your AccessKey pair. For example, your AccessKey pair may become disclosed if you commit your code to a public GitHub project, which could compromise your Alibaba Cloud account.

```
client, err := dds.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<your AccessKeySecret>")
```

**Note**

In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret.

#### Initiate a request

This topic describes how to use ApsaraDB for MongoDB SDK for Go to initiate a request. Use ApsaraDB for MongoDB SDK for Go to initiate a request.
1. Import ApsaraDB for MongoDB SDK for Go.

```java
package main import (
    "fmt"
      dds "github.com/aliyun/alibaba-cloud-sdk-go/services/dds"
```

)
2. Create a service client that contains all API operations of the service.

**Note**

You must use actual values to replace the variables in the following sample code. The angle brackets <> are not retained in the final code. The following list describes the variables: <yourRegionID>: Replace it with the actual region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID.

```
client, err := dds.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<yo urAccessKeySecret>")
```

3. Use the `xxx.CreateXXXRequest` method to create a request.
The naming convention for this method is ${service}.Create${apiName}Request . The **${service}** part specifies a service name. Service names must use lowercase letters. Example: dds. This value indicates ApsaraDB for MongoDB. The **${apiName}** part specifies an API name. Example: DescribeRegions.

**Note**

<yourDBInstanceId>: Replace it with your ApsaraDB for MongoDB instance ID.

```
    request.Scheme = "https"
    request.DBInstanceId = "<yourDBInstanceId>"
```

4. Initiate the request.

```
response, err := client.DescribeAccounts(request)
```

#### Handle errors

When you use Alibaba Cloud SDK for Go, a `ClientError` or a `ServerError` is returned when an error occurs on the server or SDK side. Both error types are included in `sdk.errors` . The errors conform to the standard Go error interface, so they can be handled in a similar way as standard Go errors. You can use the following code to handle the errors:

```
response, err := client.DescribeAccounts(request) if err != nil {
    fmt.Print(err.Error())
}
```

**ClientError**

If an error occurs in the SDK when you send a request and cannot be automatically handled, the SDK returns a `ClientError` . The following code provides an example on how to determine and obtain the error message in the `ClientError` :

**Important**

When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/dds" // In the package, dds in
dicates ApsaraDB for MongoDB.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Error package that is added.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

)

```
response, err := Client.DescribeAccounts(request) if clientError, ok := err.(*errors.ClientError); ok{
    // Obtain the error code.
    clientError.ErrorCode()
    // Obtain the error message.
    clientError.Message()
    // Obtain the original error. The return value may be nil.
    clientError.OriginError()
}
```

**ServerError**

When the server returns an error message, the SDK wraps the message into a `ServerError` and returns it to the client. In this case, you can still obtain the original HTTP response from the response. The following code provides an example on how to determine and obtain the error message in ServerError and Response:

**Important**

When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/dds" // In the package, dds in
dicates ApsaraDB for MongoDB.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Error package that is added.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

)

```
response, err := Client.DescribeAccounts(request) if serverError, ok := err.(*errors.ServerError); ok{
    // Obtain the error code.
    serverError.ErrorCode()
    // Obtain the error message.
    serverError.Message()
    // Obtain the original HTTP response.
    response.GetOriginHttpResponse()
}
```

## Use POP to make API calls

### Preparations

You can use the point of presence (POP) gateway to call API operations in Apsara Stack in the same way as in Alibaba Cloud public cloud. This topic describes the preparations before you use the POP gateway to call API operations.

**Background information**

To enable you to use the API call method in Apsara Stack as in Alibaba Cloud public cloud and have a more convenient and consistent experience, we recommend that you use the POP gateway to call Apsara Stack API operations.

**Obtain an endpoint**

**Obtain an endpoint in OpenAPI Explorer**

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

To use the POP gateway to call API operations in Apsara Stack, you must obtain the required service endpoints. You can obtain service endpoints from Apsara Stack onsite O&M engineers. You can also obtain service endpoints by yourself. In this example, API Gateway is used to show how to obtain the endpoints of a cloud service.
1. Go to the Apsara Uni-manager Operations Console.
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

You must obtain the parameters required when you use the POP gateway to call API operations in Apsara Stack, such as the organization ID, resource set ID, region ID, and instance ID. For more information, see Obtain common header parameters.

### SDK for Java

Before you use an SDK for Java to call the API of a cloud service over the point of presence (POP) gateway, you must check the style of the service API. A service API can be of the Remote Procedure Call (RPC) or Resource-Oriented Architecture (ROA) style.

**Usage notes**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample**
**Code** in the top navigation bar.

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues. Proceed with caution. The following sample code provides an example on how to call RPC APIs. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException;
```

```java
import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
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
```

q y

```
(
```

`yp`

```java
);
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

By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be ignored in the test environment, you can specify the following setting: Java

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

Remote Procedure Call (RPC) and Resource-Oriented Architecture (ROA) APIs are supported. The following sample code provides an example on how to call RPC APIs. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code:

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

The following sample code provides an example on how to call ROA APIs. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06- 07. Sample code:

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

You can configure proxies for API calls in one of the following ways: Configure proxies by using environment variables. Set the HTTP_PROXY, HTTPS_PROXY, or NO_PROXY environment variable. Sample code:

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

You can configure SSL verification for requests. If you set the HTTPSInsecure parameter to `true` , certificate verification is disabled. To ensure connection security, we recommend that you enable certificate verification. If you set the HTTPSInsecure parameter to `false` , certificate verification is enabled. By default, certificate authority (CA) certificates on the operating systems are used.

**Default value**

```
 false
```

**Configuration methods**

**Important**

By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be ignored in the test environment, you can specify the following settings:

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

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # The region ID.
    verify='./cacert.pem'  # The path of the certificate authority (CA) certificate.
```

)

| Operation | Description |
|---|---|
| CreateDBInstance | Creates or clones an ApsaraDB for MongoDB replica set instance. |
| ModifyDBInstanceSpec | Modifies the specifications or storage capacity of an ApsaraDB for MongoDB standalone or replica set instance. |
| DeleteDBInstance | Releases an ApsaraDB for MongoDB instance. |
| CreateShardingDBInstance | Creates or clones an ApsaraDB for MongoDB sharded cluster instance. |
| CreateNode | Creates a shard or mongos node for an ApsaraDB for MongoDB sharded cluster instance. |
| DeleteNode | Deletes a shard or mongos node from an ApsaraDB for MongoDB sharded cluster instance. |
| ModifyNodeSpec | Changes the specifications or storage capacity of nodes in an ApsaraDB for MongoDB sharded cluster instance. |

| Operation | Description |
|---|---|
| MigrateToOtherZone | Migrates an ApsaraDB for MongoDB instance to another zone. |
| DescribeRegions | Queries the regions and zones in which an ApsaraDB for MongoDB instance can be created. |
| MigrateAvailableZone | Changes the zone of an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| DescribeAvailableResource | Queries the ApsaraDB for MongoDB instances that can be created in a specified zone. |

| Operation | Description |
|---|---|
| AllocatePublicNetworkAddress | Applies for a public endpoint for an ApsaraDB for MongoDB instance. |
| ReleasePublicNetworkAddress | Releases the public endpoint of an ApsaraDB for MongoDB instance. |

## List of operations by

**function**

The following tables list the API operations available for use in ApsaraDB for MongoDB.

| ModifyInstanceVpcAuthMode | Enables or disables password-free access to an ApsaraDB for MongoDB instance over a virtual private cloud (VPC). |
|---|---|
| DescribeShardingNetworkAddre ss | Queries the connection information of an ApsaraDB for MongoDB sharded cluster instance. |
| ModifyDBInstanceConnectionSt ring | Modifies the endpoint of an ApsaraDB for MongoDB instance. |
| ReleaseNodePrivateNetworkAd dress | Releases the internal endpoint of a shard or Configserver node in an ApsaraDB for MongoDB sharded cluster instance. |

| Operation | Description |
|---|---|
| DescribeReplicaSetRole | Queries the role and connection information of an ApsaraDB for MongoDB instance. |
| DescribeKernelReleaseNotes | Queries the release notes of the minor database engine versions of an ApsaraDB for MongoDB instance. |
| DescribeAvailableEngineVersio n | Queries the database engine versions to which an ApsaraDB for MongoDB instance can be upgraded. |
| DescribeDBInstances | Queries a list of ApsaraDB for MongoDB instances. |
| DescribeDBInstanceAttribute | Queries the details of an ApsaraDB for MongoDB instance. |
| DescribeRoleZoneInfo | Queries the roles and zones of nodes in an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| RestartDBInstance | Restarts an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceMaintainTime | Modifies the maintenance window of an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceDescription | Modifies the name of an ApsaraDB for MongoDB instance. |
| SwitchDBInstanceHA | Switches between the primary and secondary nodes in an ApsaraDB for MongoDB instance. |
| UpgradeDBInstanceEngineVersi on | Upgrades the database engine version of an ApsaraDB for MongoDB instance. |
| UpgradeDBInstanceKernelVersi on | Updates the minor database engine version of an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceNetExpireTim e | Extends the retention period of the classic network endpoint of an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|

| DescribeAccounts | Queries the information of database accounts of an ApsaraDB for MongoDB instance. |
|---|---|
| ResetAccountPassword | Resets the password of the root account of an ApsaraDB for MongoDB instance. |
| ModifyAccountDescription | Modifies the description of the root account of an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| DescribeSecurityGroupConfigur ation | Queries the Elastic Compute Service (ECS) security groups associated with an ApsaraDB for MongoDB instance. |
| ModifySecurityGroupConfigurati on | Modifies the ECS security groups associated with an ApsaraDB for MongoDB instance. |
| DescribeSecurityIps | Queries the IP address whitelists of an ApsaraDB for MongoDB instance. |
| ModifySecurityIps | Modifies the IP address whitelists of an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| DescribeDBInstanceTDEInfo | Queries whether transparent data encryption (TDE) is enabled for an ApsaraDB for MongoDB instance. |
| ModifyDBInstanceTDE | Modifies the TDE status of an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| ModifyDBInstanceSSL | Modifies the Secure Sockets Layer (SSL) settings of an ApsaraDB for MongoDB instance. |
| DescribeDBInstanceSSL | Queries the SSL settings of an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| DescribeAuditRecords | Queries the audit log entries of an ApsaraDB for MongoDB instance. |
| DescribeAuditFiles | Queries the audit log files of an ApsaraDB for MongoDB instance. |
| DescribeAuditPolicy | Queries whether the audit log feature is enabled for an ApsaraDB for MongoDB instance. |
| ModifyAuditLogFilter | Modifies the type of audit logs that you want to collect from an ApsaraDB for MongoDB instance. |

| DescribeAuditLogFilter | Queries the types of audit logs that you want to collect from an ApsaraDB for MongoDB instance. |
|---|---|
| ModifyAuditPolicy | Enables or disables the audit log feature or specifies the log retention period for an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| DescribeSlowLogRecords | Queries the slow query log entries of an ApsaraDB for MongoDB instance. |
| DescribeErrorLogRecords | Queries the error log entries of an ApsaraDB for MongoDB instance. |
| DescribeRunningLogRecords | Queries the operational log entries of an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| DescribeDBInstancePerformanc e | Queries the performance data of an ApsaraDB for MongoDB instance. |
| DescribeDBInstanceMonitor | Queries the internal at which the performance monitoring data is collected from an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| DescribeParameterModification History | Queries the parameter modification records of an ApsaraDB for MongoDB instance. |
| DescribeParameters | Queries the parameter settings of an ApsaraDB for MongoDB instance. |
| ModifyParameters | Modifies the parameters of an ApsaraDB for MongoDB instance. |

| Operation | Description |
|---|---|
| DescribeBackupPolicy | Queries the backup policy of an ApsaraDB for MongoDB instance. |
| ModifyBackupPolicy | Modifies the backup policy of an ApsaraDB for MongoDB instance. |
| CreateBackup | Backs up an ApsaraDB for MongoDB instance. |
| DescribeBackups | Queries the backups of an ApsaraDB for MongoDB instance. |
| RestoreDBInstance | Restores data to the current ApsaraDB for MongoDB instance. |
| DescribeBackupDBs | Queries the databases that are backed up at a specified point in time or the databases in a specified backup set before you restore a database for an ApsaraDB for MongoDB instance. |

**Backup and restoration**

| Developer Guide·List of operatio s by function | ApsaraDB for MongoDB |
|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | Quer y | Yes | CreateDBInstance | The operation that you want to perform. Set the value to CreateDBInstance. |
| RegionId | Strin g | Dom ain | Yes | cn-hangzhou | The region where the instance is deployed. |
| ClientToke n | Strin g | Quer y | Yes | ETnLKlblzczshOTUbOCzxx xxxxxxxx | The token that ensures the idempotence of the request and prevents duplicate submissions. The client generates this parameter. You must ensure that its value is unique across different requests. The maximum length is 64 ASCII characters, and it cannot contain non-ASCII characters. |
| ZoneId | Strin g | Quer y | No | cn-hangzhou-b | The ID of the zone. |
| Engine | Strin g | Quer y | Yes | MongoDB | The database engine. Set the value to MongoDB. |
| EngineVer sion | Strin g | Quer y | Yes | 4.0 | The version of the database. |

## API Reference

### Lifecycle management

#### CreateDBInstance

Call CreateDBInstance to create or clone a MongoDB replica set instance.

**Request headers**

This operation uses common request headers and does not have specific request headers. For more information, see Common request parameters.

**Request parameters**

| DBInstanc eClass | Strin g | Quer y | Yes | dds.mongo.standard | The instance type. |
|---|---|---|---|---|---|
| DBInstanc eStorage | Integ er | Quer y | Yes | 10 | The storage capacity of the instance. Valid values: 10 to 3000. Unit: GB. The value must be a multiple of 10. |
| DBInstanc eDescripti on | Strin g | Quer y | No | Test database 1 | The name of the instance. The name must be 2 to 256 characters in length. It must start with a letter and can contain digits, letters, underscores ( ), _ and hyphens (-). |
| SecurityIPL ist | Strin g | Quer y | No | 10.23.12.24/24 | The IP allowlist of the instance. Separate multiple IP addresses with commas. Duplicate entries are not allowed. You can specify up to 1,000 IP addresses. Supported formats: %, 0.0.0.0/0, 10.23.12.24 (IP address), or 10.23.12.24/24 (CIDR format. /24 indicates the prefix length. Valid values: 1 to 32). The % and 0.0.0.0/0 settings allow access from any IP address to the instance databases. These are high-risk configurations. Exercise caution when you use them. |

| AccountPa ssword | Strin g | Quer y | No | Alitest!159 | The password of the root account. The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include !#$%^&*() +- _ =. The password must be 8 to 32 characters in length. |
|---|---|---|---|---|---|
| ChargeTyp e | Strin g | Quer y | No | PrePaid | The billing method of the instance. Valid values: PostPaid: pay-as-you- go PrePaid: subscription The default billing method is pay-as-you-go. If you set this parameter to PrePaid, you must also specify the Period parameter. |
| Period | Integ er | Quer y | No | 1 | The subscription duration of the instance. Unit: months. Valid values: 1 to 9, 12, 24, and 36. This parameter is available and required only if ChargeType is set to PrePaid. |
| NetworkTy pe | Strin g | Quer y | No | VPC | The network type of the instance. Valid values: classic: classic network vpc: virtual private cloud The default network type is classic network. If you set this parameter to vpc, you must also specify the VpcId and VSwitchId parameters. |

| VpcId | Strin g | Quer y | No | vpc-bpxxxxxxxx | The ID of the VPC. This parameter is available only if NetworkType is set to VPC. |
|---|---|---|---|---|---|
| VSwitchId | Strin g | Quer y | No | vsw-bpxxxxxxxx | The ID of the vSwitch. This parameter is available only if NetworkType is set to VPC. |
| SrcDBInsta nceId | Strin g | Quer y | No | dds-bpxxxxxxxx | The ID of the source instance. You can specify this parameter only when you call this operation to clone an instance. You must also specify either BackupId or RestoreTime. |
| BackupId | Strin g | Quer y | No | 32994xxxx | The ID of the specific backup set. You can specify this parameter only when you call this operation to clone an instance. You must also specify SrcDBInstanceId. |
| RestoreTi me | Strin g | Quer y | No | 2019-03-13T12:11:14Z | The point in time to which you want to restore the cloned instance. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. You can specify this parameter only when you call this operation to clone an instance. You must also specify SrcDBInstanceId and BackupId. You can select any point in time within the last seven days for cloning. |
| BusinessIn fo | Strin g | Quer y | No | {“ActivityId":"000000000 "} | Additional parameters for business information. |

| AutoRene w | Strin g | Quer y | No | true | Specifies whether to enable auto-renewal for the instance. Valid values: true: enables auto- renewal. false: disables auto- renewal. In this case, you must manually renew the instance. By default, manual renewal is used. This parameter is available only if ChargeType is set to PrePaid. |
|---|---|---|---|---|---|
| DatabaseN ames | Strin g | Quer y | No | mongodbtest | The name of the database. When you call this operation to clone an instance, you can specify this parameter to clone specific databases. If you do not specify this parameter, all databases of the instance are cloned. |
| StorageEn gine | Strin g | Quer y | No | WiredTiger | Only WiredTiger is supported. If you do not specify this parameter, WiredTiger is used by default. |
| Replication Factor | Strin g | Quer y | No | 3 | The number of nodes in the replica set. Valid values: 3, 5, and 7. Default value: 3 |
| ReadonlyR eplicas | Strin g | Quer y | No | 1 | The number of read-only nodes to create. Valid values: 1 to 5. If you do not specify this parameter, no read-only nodes are created by default. |
| ResourceG roupId | Strin g | Quer y | No | rg-axxxxxxxx | The ID of the resource group. |
| CpuType | Strin g | Quer y | No | intel | The CPU chip type. Valid values: intel, arm, and others. |

| IPVersionS electedTyp e | Strin g | Quer y | No | IPv4 | The IP version supported by the instance. Default value: IPv4. Valid values: IPv4 IPv4v6 |
|---|---|---|---|---|---|
| SecurityIPv 6List | Strin g | Quer y | No | 2001:db8::1,2001:db8::ff, 2001:db8:1::/64 | The IPv6 addresses in the allowlist. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D8F1D721-6439- 4257-A89C- F1E8E9C9624D | The ID of the request. |
| OrderId | String | 2033xxxxxxxxxxxx | The ID of the order. |
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |

**Response parameters**

Sample requests

```
&RegionId=cn-hangzhou &ClientToken=ETnLKlblzczshOTUbOCzxxxxxxxxxx &Engine=MongoDB &EngineVersion=4.0 &DBInstanceClass=dds.mongo.standard &DBInstanceStorage=10 &Common request parameters
```

Sample success responses `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"D8F1D721-6439-4257-A89C-F1E8E9C9624D",
 "DBInstanceId":"dds-bpxxxxxxxx",
 "OrderId":"2033xxxxxxxxxxxx"
}
```

`XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eSpec | The operation that you want to perform. Set the value to ModifyDBInstanceSpec. |
| DBInstanceId | String | Yes | dds- d1n4eab47879* *** | The ID of the instance. |
| RegionId | String | No | cn-qd- agility14**** | The region ID of the instance. Note You can call the DescribeDBInstanceAttribute operation to query the region ID of the instance. |
| DBInstanceClass | String | No | dds.mongo.stan dard | The instance type. Note For more information, see Instance types in Aps araDB for MongoDB Prod uct Introduction. You must specify either this parameter or the DBInstanceStorage parameter. |

```xml
<RequestId>D8F1D721-6439-4257-A89C-F1E8E9C9624D</RequestId> <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId> <OrderId>2033xxxxxxxxxxxx</OrderId>
```

#### ModifyDBInstanceSpec

Modifies the specifications or storage capacity of an ApsaraDB for MongoDB replica set instance. This operation is applicable to replica set instances. You can call the **ModifyNodeSpec**,
**CreateNode**, or **DeleteNode** operation to change the configurations of a sharded cluster
instance. When you call this operation, you must configure the `x-acs-organizationid` , `x-acs-` `resourcegroupid` , and `x-acs-instanceid` header parameters to specify the organization ID, resource group ID, and instance ID. Otherwise, the call is directed to the root resource set and organization. For more information about the code, see SDK description in ApsaraD B for MongoDB Developer Guide.

**Request parameters**

| DBInstanceStora ge | String | No | 50 | The storage space of the instance. Valid values: 10 to 3000. The value must be a multiple of 10. Unit: GB. Note The values that can be specified for this parameter are subject to the instance types. For more information, see In stance types in ApsaraD B for MongoDB Product I ntroduction. You must specify either this parameter or the DBInstanceClass parameter. Storage capacity can be scaled down only on subscription replica set instances. The new storage capacity you specify must be greater than the used storage space. |
|---|---|---|---|---|
| OrderType | String | No | UPGRADE | The type of the change. Valid values: UPGRADE: upgrades the configurations of an instance. DOWNGRADE: downgrades the configurations of an instance. Default value: DOWNGRADE. Note This parameter is required when the ChargeType parameter is set to PostPaid. |
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment. Valid values: true: enables automatic payment. Make sure that you have sufficient balance within your account. false: disables automatic payment. Default value: true. |
| BusinessInfo | String | No | {“ActivityId":"00 0000000"} | The business information. |
| ReplicationFacto r | String | No | 3 | The number of nodes in the instance. Valid values for replica set instances: 3, 5, and 7. Valid values for standalone instances: 1. |

| ReadonlyReplica s | String | No | 1 | The number of read-only nodes. Valid values: 1 to 5. |
|---|---|---|---|---|
| CouponNo | String | No | youhuiquan pro _ motion option i _ _ d for blank _ _ | The coupon code. Default value: youhuiquan promotion option id _ _ _ for blank. _ _ |
| EffectiveTime | String | No | Immediately | The time when the new configurations take effect. Valid values: Immediately: The new configurations immediately take effect. MaintainTime: The new configurations take effect during the maintenance window of the instance. Default value: Immediately. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 20331066**** | The order ID of the instance. |
| RequestId | String | C5662998-62BE- 4C7F-961D- 7DFE775D**** | The ID of the request. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/?Action=ModifyDBInstanceSpec &DBInstanceId=dds-d1n4eab47879**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
  <RequestId>C5662998-62BE-4C7F-961D-7DFE775D****</RequestId>
  <OrderId>20331066****</OrderId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDBInstanc e | The operation that you want to perform. Set the value toDeleteDBInstance. |
| DBInstanceId | String | Yes | dds- d1n4eab47879* *** | The ID of the instance. |
| ClientToken | String | No | ETnLKlblzczshOT UbOCz**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|

```json
{
  "RequestId": "C5662998-62BE-4C7F-961D-7DFE775D****",
  "OrderId": "20331066****"
}
```

#### DeleteDBInstance

Releases an ApsaraDB for MongoDB instance. The instance must be in the Running state when you call this operation. After an instance is released, all the data in the instance is deleted and cannot be restored. Proceed with caution. When you call this operation, you must configure the `x-acs-organizationid` , `x-acs-` `resourcegroupid` , and `x-acs-instanceid` header parameters to specify the organization ID, resource group ID, and instance ID. Otherwise, the call is directed to the root resource group and organization. For more information about the code, see SDK Description in Apsar aDB for MongoDB Developer Guide.

**Request parameters**

**Response parameters**

| RequestId | String | 72651AF9-7897- 41A7-8B67- 6C15C7F2**** | The ID of the request. |
|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | Quer y | Yes | CreateShardingDBInstanc e | The operation that you want to perform. Set the value to CreateShardingDBInstanc e. |
| RegionId | Strin g | Host | Yes | cn-qd-agility14**** | The ID of the region where the instance resides. |

Sample requests

```
http(s)://mongodb.example.com/?Action=DeleteDBInstance &DBInstanceId=dds-d1n4eab47879**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
  <RequestId>72651AF9-7897-41A7-8B67-6C15C7F2****</RequestId>
```

`JSON` format

```json
{
  "RequestId": "72651AF9-7897-41A7-8B67-6C15C7F2****"
}
```

#### CreateShardingDBInstance

Call the CreateShardingDBInstance operation to create or clone a MongoDB sharded cluster instance.

**Request headers**

This operation uses common request headers and does not have specific request headers. For more information, see Common request parameters.

**Request parameters**

| ZoneId | Strin g | Quer y | No | cn-qd-agility14- amtest110**** | The ID of the zone where the instance resides. |
|---|---|---|---|---|---|
| Engine | Strin g | Quer y | Yes | MongoDB | The database engine. Set the value to MongoDB. |
| EngineVer sion | Strin g | Quer y | Yes | 4.0 | The version of the database. |
| Mongos | Repe atLis t | Quer y | No | - | The structure of Mongos. |
| -Class | Strin g |  | No | dds.cs.mid | The specification of ConfigServer. |
| ReplicaSet | Repe atLis t | Quer y | No | - | The structure of ReplicaSet. |
| -Class | Strin g |  | No | dds.cs.mid | The specification of ConfigServer. |
| -Storage | Integ er |  | No | 20 | The storage capacity of ConfigServer. |
| ConfigServ er | Repe atLis t | Quer y | No | - | The structure of ConfigServer. |
| -Class | Strin g |  | No | dds.cs.mid | The specification of ConfigServer. |
| -Storage | Integ er |  | No | 20 | The storage capacity of ConfigServer. |

| DBInstanc eDescripti on | Strin g | Quer y | No | Test Database 1 | The name of the instance. The naming rules are as follows: The name must start with a letter. It can contain digits, letters, underscores ( ), and _ hyphens (-). The name must be 2 to 256 characters in length. |
|---|---|---|---|---|---|
| SecurityIPL ist | Strin g | Quer y | No | 10.23.12.24/24 | The IP allowlist of the instance. Separate multiple IP addresses with commas (,). Do not duplicate IP addresses. You can specify up to 1,000 IP addresses. Supported formats include %, 0.0.0.0/0, 10.23.12.24 (IP address), or 10.23.12.24/24 (CIDR format, Classless Inter- Domain Routing, where /24 indicates the length of the address prefix, ranging from 1 to 32). % and 0.0.0.0/0 indicate that any IP address can access the database of the instance. This is a high-risk setting. Proceed with caution. |
| AccountPa ssword | Strin g | Quer y | No | Alitest**** | The password for the root account. The password must meet the following requirements: The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include: !#$%^&*() +-= _ The password must be 8 to 32 characters in length. |

| ChargeTyp e | Strin g | Quer y | No | PrePaid | The billing method of the instance. Valid values: PostPaid: pay-as-you- go PrePaid: subscription. Default value: PostPaid. When you set this parameter to PrePaid, you must also configure the Period parameter. |
|---|---|---|---|---|---|
| Period | Integ er | Quer y | No | 1 | The subscription duration of the instance. Unit: months. Valid values: 1 to 9, 12, 24, and 36. You must configure this parameter when you set ChargeType to PrePaid. |
| NetworkTy pe | Strin g | Quer y | No | Classic | The network type of the instance. Valid values: Classic: classic network VPC: virtual private cloud Default value: Classic. When you set this parameter to VPC, you must also configure the VpcId and VSwitchId parameters. |
| VpcId | Strin g | Quer y | No | vpc- bp1q2qqm4vxo6e6zl**** | The ID of the VPC. You must configure this parameter when you set NetworkType to VPC. |
| VSwitchId | Strin g | Quer y | No | vsw- bp1buy0h9myt5i9e7**** | The ID of the vSwitch. You must configure this parameter when you set NetworkType to VPC. |

| SrcDBInsta nceId | Strin g | Quer y | No | dds-bp1b47357f21**** | The ID of the source instance. You must configure this parameter when you call this operation to clone an instance. You must also configure the RestoreTime parameter together with this parameter. |
|---|---|---|---|---|---|
| RestoreTi me | Strin g | Quer y | No | 2019-03-08T02:30:25Z | The point in time to which you want to restore data when you clone an instance. Specify the time in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. You must configure this parameter when you call this operation to clone an instance. You must also configure the SrcDBInstanceId parameter together with this parameter. You can select any point in time within the last seven days for cloning. |
| ClientToke n | Strin g | Quer y | No | ETnLKlblzczshOTUbOCz** ** | The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. The client generates this parameter value. It must be unique across different requests. The value can be up to 64 ASCII characters in length and cannot contain non-ASCII characters. |
| StorageEn gine | Strin g | Quer y | No | WiredTiger | The storage engine of the database. Only WiredTiger is supported. |

| AutoRene w | Strin g | Quer y | No | false | Specifies whether to enable auto-renewal for the instance. Valid values: true: enables auto- renewal. false: disables auto- renewal. In this case, you must manually renew the instance. Default value: false. You must configure this parameter when you set ChargeType to PrePaid. |
|---|---|---|---|---|---|
| ResourceG roupId | Strin g | Quer y | No | rg-acfm22cdcgc**** | The ID of the resource group. |
| IPVersionS electedTyp e | Strin g | Quer y | No | IPv4 | The network type supported by the instance. Default value: IPv4. Valid values: IPv4 IPv4v6 |
| SecurityIPv 6List | Strin g | Quer y | No | 2001:db8::1,2001:db8::ff, 2001:db8:1::/64 | The IPv6 addresses in the allowlist. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D8F1D721-6439- 4257-A89C- F1E8E9C9**** | The ID of the request. |
| OrderId | String | 20331066**** | The ID of the resource. |
| DBInstanceId | String | dds- bp14ed961586**** | The ID of the instance. |

**Response parameters**

Sample requests

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateNode | The operation that you want to perform. Set the value to CreateNode. |
| NodeClass | String | Yes | dds.shard.mid | The instance type of the shard or mongos node. |
| NodeType | String | Yes | shard | The type of the node. Valid values: shard mongos |
| DBInstanceId | String | Yes | dds- bp11501cd7b5* *** | The ID of the sharded cluster instance. |

```
http(s)://[Endpoint]/?Action=CreateShardingDBInstance &RegionId=cn-qd-agility14**** &Engine=MongoDB &EngineVersion=4.0 &Common request parameters
```

Sample success responses `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"D8F1D721-6439-4257-A89C-F1E8E9C9****",
 "DBInstanceId":"dds-bp14ed961586****",
 "OrderId":"20331066****"
}
```

`XML` format

```xml
<RequestId>D8F1D721-6439-4257-A89C-F1E8E9C9****</RequestId> <DBInstanceId>dds-bp14ed961586****</DBInstanceId> <OrderId>20331066****</OrderId>
```

#### CreateNode

Creates a shard or mongos node for an ApsaraDB for MongoDB sharded cluster instance. This operation is applicable only to sharded cluster instances.

**Request parameters**

| NodeStorage | Integer | No | 10 | The disk storage capacity of the node. This parameter is required if you set the NodeType parameter to shard. Valid values: 10 to 2000. Unit: GB. The value of this parameter must be a multiple of 10. |
|---|---|---|---|---|
| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| FromApp | String | No | OpenApi | The source of the request. Valid values: OpenApi: the ApsaraDB for MongoDB API. mongo buy: the ApsaraDB for _ MongoDB console. |
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment for the instance. Valid values: true: enables automatic payment. Make sure that you have sufficient balance within your Alibaba Cloud account. false: disables automatic payment. You must pay for the instance in the ApsaraDB for MongoDB console. Default value: true. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NodeId | String | d- bp1b7bb3bbe1**** | The node ID. |
| OrderId | String | 2034**** | The order ID. |
| RequestId | String | 7D48FB19-20CA- 4725-A870- 3D8F5CE69F14 | The request ID. |

**Response parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteNode | The operation that you want to perform. Set the value to DeleteNode. |
| DBInstanceId | String | Yes | dds- bp11501cd7b5* *** | The instance ID. |
| NodeId | String | Yes | s- bp1713dece57* *** | The ID of the shard or mongos node that you want to delete. You can call the DescribeDBInstanceAttribute operation to query the node ID. |

Sample requests

```
&NodeClass=dds.shard.mid &NodeType=shard &DBInstanceId=dds-bp11501cd7b5**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7D48FB19-20CA-4725-A870-3D8F5CE69F14</RequestId> <NodeId>d-bp1b7bb3bbe1****</NodeId> <OrderId>2034****</OrderId>
```

`JSON` format

```json
{
    "RequestId": "7D48FB19-20CA-4725-A870-3D8F5CE69F14",
    "NodeId": "d-bp1b7bb3bbe1****",
    "OrderId": "2034****"
}
```

#### DeleteNode

Deletes a shard or mongos node from an ApsaraDB for MongoDB sharded cluster instance. Before you call this API operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements: The instance is in the running state. The instance is a sharded cluster instance. The number of shard or mongos nodes in the instance is greater than 2.

**Request parameters**

| ClientToken | String | No | ETnLKlblzczshOT UbOCz**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 2033**** | The order ID. |
| RequestId | String | 9F9BDE64-BF30- 41F3-BD29- C19CE4AB3404 | The request ID. |
| TaskId | Integer | 111111111 | The task ID. |

**Response parameters**

Sample requests

```
&DBInstanceId=dds-bp11501cd7b5**** &NodeId=s-bp1713dece57**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TaskId>111111111</TaskId> <RequestId>9F9BDE64-BF30-41F3-BD29-C19CE4AB3404</RequestId> <OrderId>2033****</OrderId>
```

`JSON` format

```json
{
    "TaskId": 111111111,
    "RequestId": "9F9BDE64-BF30-41F3-BD29-C19CE4AB3404",
    "OrderId": "2033****"
}
```

#### ModifyNodeSpec

You can call this operation to modify the specifications and storage capacity of the nodes in an ApsaraDB for MongoDB sharded cluster instance.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNodeSpec | The operation that you want to perform. Set the value to ModifyNodeSpec. |
| NodeId | String | Yes | d-bpxxxxxxxx | The ID of the shard or mongos node in the sharded cluster instance. You can call the DescribeDBInstanceAttribute operation to view the ID. Note If you set this parameter to the ID of a shard, you must also specify the NodeStorage parameter. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeClass | String | No | dds.shard.stand ard | The specifications of the mongos node. For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. Note You must specify this parameter or the NodeStorage parameter. |
| NodeStorage | Integer | No | 20 | The storage capacity for the shard node. Valid values: 10 to 2000. Unit: GB. The value must be a multiple of 10 GB. Note You must specify this parameter or the NodeClass parameter. This parameter is valid only if you set the NodeId parameter to the ID of a shard. |

This operation is applicable only to sharded cluster instances.

**Request parameters**

| ClientToken | String | No | ETnLKlblzczshOT UbOCzxxxxxxxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
|---|---|---|---|---|
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment for the instance. Valid values: true: enables automatic payment. Make sure that your account has sufficient balance. false: disables automatic payment. You must perform the following operations to pay for the instance: Log on to the ApsaraDB for MongoDB console. In the top navigation bar, click Expenses. The Billing Management page appears. In the left-side navigation pane, click Bills. On the Unpaid tab, click Make a Payment in the Actions column for the bill that you want to pay. Default value: true. |
| EffectiveTime | String | No | Immediately | The time when the new settings take effect. Valid values: Immediately: The settings take effect immediately. MaintainTime: The settings take effect during the maintenance period of the instance. Default value: Immediately. |
| FromApp | String | No | OpenApi | The source of the request. Valid values: OpenApi: the ApsaraDB for MongoDB API mongo buy: the ApsaraDB for _ MongoDB console |
| OrderType | String | No | UPGRADE | The type of the order. Valid values: UPGRADE DOWNGRADE |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 2033xxxxxxxxx | The ID of the order. |
| RequestId | String | EFFC5788-8BB5- 41B5-9F15- 9CFC5A0E8FCC | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

Sample requests

```
http(s)://mongodb.aliyuncs.com/? Action=ModifyNodeSpec &NodeId=d-bpxxxxxxxx &DBInstanceId=dds-bpxxxxxxxx &NodeClass=dds.shard.standard &NodeStorage=20 &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <OrderId>2033xxxxxxxxx</OrderId>
   <RequestId>EFFC5788-8BB5-41B5-9F15-9CFC5A0E8FCC</RequestId>
```

`JSON` format

```json
{
    "OrderId": "2033xxxxxxxx",
    "RequestId": "EFFC5788-8BB5-41B5-9F15-9CFC5A0E8FCC"
}
```

### Region management

#### MigrateToOtherZone

You can call this operation to migrate an ApsaraDB for MongoDB instance to another zone. This operation is applicable only to replica set instances, but not to sharded cluster instances.

**Note**

If you have applied for a public endpoint of the instance, you must first call the **ReleasePublicNetworkAddress** operation to release the public endpoint.

**Request parameters**

| Action | String | Yes | MigrateToOther Zone | The operation that you want to perform. Set the value to MigrateToOtherZone. |
|---|---|---|---|---|
| InstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note You must specify the Vswitch parameter if the network type of the instance is VPC. |
| ZoneId | String | Yes | cn-hangzhou-b | The ID of the destination zone to which you want to migrate the MongoDB instance. Note The destination and source zones are in the same region. You can call the DescribeRegions operation to query the zone IDs. |
| EffectiveTime | String | No | Immediately | The time when the instance is migrated to the destination zone. Valid values: Immediately MaintainTime: The instance will be migrated during the maintenance period of the instance. Default value: Immediately. |
| VSwitchId | String | No | vsw-bpxxxxxxxx | The ID of the vSwitch in the destination zone. Note This parameter can be used only when the network type of the instance is VPC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252- 4A4A-ADDA- 5CB1BF63873D | The ID of the request. |

**Response parameters**

Sample requests

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of DdsRegion |  | The information of the regions. |
| DdsRegion |  |  |  |
| RegionId | String | cn-qingdao | The region ID. |
| Zones | Array of Zone |  | The information of the zones in the region. |
| Zone |  |  |  |

```
http(s)://mongodb.example.com/? Action=MigrateToOtherZone &DBInstanceId=dds-bpxxxxxxxx &ZoneId=cn-hangzhou-b &EffectiveTime=Immediately &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>0FDDC511-7252-4A4A-ADDA-5CB1BF63873D</RequestId>
```

`JSON` format

```json
{
 "RequestId": "0FDDC511-7252-4A4A-ADDA-5CB1BF63873D"
}
```

#### DescribeRegions

Queries the available regions and zones of an ApsaraDB for MongoDB instance. Before you call the CreateDBInstance or CreateShardingDBInstance operation to create an instance, you must call the DescribeRegions operation to query the available regions and zones of the instance.

**Request parameters**

**Response parameters**

| VpcEnabled | Boolean | true | Indicates whether Virtual Private Cloud (VPC) is supported. Valid values: true false |
|---|---|---|---|
| ZoneId | String | cn-hangzhou-b | The zone ID. |
| RequestId | String | 4E46C22C-D3B7- 4DB8-9C76- 63851BE68E20 | The request ID. |

Sample requests

```
http(s)://mongodb.example.com/?Action=DescribeRegions &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>4E46C22C-D3B7-4DB8-9C76-63851BE68E20</RequestId>
   <Regions>
      <DdsRegion>
         <RegionId>cn-hangzhou</RegionId>
         <Zones>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-i</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-b</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-d</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-f</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-MAZ5(b,e,f)</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-g</ZoneId>
            </Zone>
         </Zones>
      </DdsRegion>
   </Regions>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

```json
{
 "RequestId": "4E46C22C-D3B7-4DB8-9C76-63851BE68E20",
 "Regions": {
  "DdsRegion": [
   {
    "RegionId": "cn-hangzhou",
    "Zones": {
     "Zone": [
      {
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-i"
      },
      {
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-b"
      },
      {
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-d"
      },
      {
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-f"
      },
      {
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-MAZ5(b,e,f)"
      },
      {
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-g"
      }
```

]

```
    }
   }
```

]

```
 }
}
```

#### MigrateAvailableZone

You can call this operation to change the zone of an ApsaraDB for MongoDB instance. This operation is applicable only to replica set instances, but not to sharded cluster instances.

**Note**

If you have applied for a public endpoint of the instance, you must first call
**ReleasePublicNetworkAddress** to release the public endpoint.

**Request parameters**

| Action | String | Yes | MigrateAvailable Zone | The operation that you want to perform. Set the value to MigrateAvailableZone. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note You must specify the Vswitch parameter if the network type of the instance is VPC. |
| ZoneId | String | Yes | cn-hangzhou-b | The ID of the destination zone to which you want to migrate the ApsaraDB for MongoDB instance. Note The destination zone must be in the same region as the current zone of the instance. You can call the DescribeRegions operation to view the zone IDs. |
| Vswitch | String | No | vsw-bpxxxxxxxx | The ID of the vSwitch in the destination zone. Note This parameter can be used only when the network type of the instance is VPC. |
| EffectiveTime | String | No | Immediately | The time when the instance is migrated to the destination zone. Valid values: Immediately: The instance will be migrated immediately. MaintainTime: The instance will be migrated during the maintenance period of the instance. Default value: Immediately. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252- 4A4A-ADDA- 5CB1BF63873D | The ID of the request. |

**Response parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAvailabl eResource | The operation that you want to perform. Set the value to DescribeAvailableResource. |
| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to view the region IDs. |
| ZoneId | String | No | cn-hangzhou-h | The zone ID of the instance. You can call the DescribeRegions operation to view the zone IDs. |

Sample requests

```
http(s)://mongodb.example.com/? Action=MigrateAvailableZone &DBInstanceId=dds-bpxxxxxxxx &ZoneId=cn-hangzhou-b &EffectiveTime=Immediately &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>0FDDC511-7252-4A4A-ADDA-5CB1BF63873D</RequestId>
```

`JSON` format

```json
{
 "RequestId": "0FDDC511-7252-4A4A-ADDA-5CB1BF63873D"
}
```

### Resource management

#### DescribeAvailableResource

You can call this operation to view the ApsaraDB for MongoDB instances that can be created in a specified zone.

**Request parameters**

| InstanceChargeT ype | String | No | PrePaid | The billing method. Valid values: PrePaid: subscription. PostPaid: pay-as-you-go. Note Default value: PrePaid. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 344EE51D-8850- 4935-B68B- 58A8F4DCE3BD | The ID of the request. |
| SupportedDBT ypes | Array of SupportedDBT ype |  | The database type supported. |
| SupportedDBT ype |  |  |  |
| AvailableZone s | Array of AvailableZone |  | The zone ID of the instance. |
| AvailableZone |  |  |  |
| RegionId | String | cn-hangzhou | The region ID of the instance. |
| SupportedEngi neVersions | Array of SupportedEngi neVersion |  | The versions of the storage engine. |
| SupportedEngi neVersion |  |  |  |
| SupportedEngi nes | Array of SupportedEngi ne |  | The storage engine supported. |
| SupportedEngi ne |  |  |  |
| Engine | String | WiredTiger | The storage engine of the instance. |
| SupportedNod eTypes | Array of SupportedNod eType |  | The instance types supported. |
| SupportedNod eType |  |  |  |
| AvailableReso urces | Array of AvailableReso urce |  | The details of available resources. |

**Response parameters**

| AvailableReso urce |  |  |  |
|---|---|---|---|
| InstanceClass | String | dds.mongo.2xlarge | The category of the instance. |
| InstanceClass Remark | String | 8 vCPUs, 32 GiB (maximum connections: 8000 IOPS: 14000) | The instance type. |
| NetworkTypes | String | VPC | The network type of the instance. |
| NodeType | String | 3 | The number of nodes in the instance. |
| Version | String | 4.0 | The database engine version of the instance. |
| ZoneId | String | cn-hangzhou-h | The zone ID of the instance. |
| DbType | String | sharding | The database engine of the instance. |

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAvailableResource &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>344EE51D-8850-4935-B68B-58A8F4DCE3BD</RequestId> <SupportedDBTypes>
    <DbType>sharding</DbType>
</SupportedDBTypes> <SupportedDBTypes>
    <AvailableZones>
        <ZoneId>cn-hangzhou-h</ZoneId>
        <RegionId>cn-hangzhou</RegionId>
    </AvailableZones>
    <AvailableZones>
        <SupportedEngineVersions>
            <Version>4.0</Version>
        </SupportedEngineVersions>
        <SupportedEngineVersions>
            <SupportedEngines>
                <Engine>WiredTiger</Engine>
            </SupportedEngines>
            <SupportedEngines>
                <SupportedNodeTypes>
                    <NetworkTypes>VPC</NetworkTypes>
                    <NodeType>3</NodeType>
                </SupportedNodeTypes>
                <SupportedNodeTypes>
                    <AvailableResources>
                        <InstanceClassRemark>8 vCPUs, 32 GiB (maximum connections: 8000
IOPS: 14000)</InstanceClassRemark>
                        <InstanceClass>dds.mongo.2xlarge</InstanceClass>
                    </AvailableResources>
                </SupportedNodeTypes>
            </SupportedEngines>
        </SupportedEngineVersions>
    </AvailableZones>
</SupportedDBTypes>
```

`JSON` format

```json
{
    "RequestId":"344EE51D-8850-4935-B68B-58A8F4DCE3BD",
    "SupportedDBTypes":[
        {
            "DbType":"sharding"
        },
        {
            "AvailableZones":[
                {
                    "ZoneId":"cn-hangzhou-h",
                    "RegionId":"cn-hangzhou"
                },
                {
                    "SupportedEngineVersions":[
                        {
                            "Version":"4.0"
                        },
                        {
                            "SupportedEngines":[
                                {
                                    "Engine":"WiredTiger"
                                },
                                {
                                    "SupportedNodeTypes":[
                                        {
                                            "NetworkTypes":"VPC",
                                            "NodeType":"3"
                                        },
                                        {
                                            "AvailableResources":[
                                                {
                                                    "InstanceClassRemark":"8 vCPUs, 32 Gi
B (maximum connections: 8000 IOPS: 14000)",
                                                    "InstanceClass":"dds.mongo.2xlarge"
                                                }
```

]

```
                                        }
```

]

```
                                }
```

]

```
                        }
```

]

```
                }
```

]

```
        }
```

]

```
}
```

### Connection management

#### AllocatePublicNetworkAddress

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocatePublicNe tworkAddress | The operation that you want to perform. Set the value to AllocatePublicNetworkAddress. |
| DBInstanceId | String | Yes | dds- bp11501cd7b5* *** | The ID of the instance. Note If you specify the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | s- bp1713dece57* *** | The ID of the mongos node, shard node, or ConfigServer node in the sharded cluster instance. Note This parameter is available only when you specify the ID of a sharded cluster instance for DBInstanceId. You can call the DescribeDBInstanceAttrib ute operation to query the IDs of mongos nodes, shard nodes, and ConfigServer nodes. |
| IPVersionSelecte dType | String | No | IPv6 | The IP version. Default value: IPv4. Valid values: IPv4 IPv6 IPv4v6 |

| Parameter | Type | Example | Description |
|---|---|---|---|

Call the AllocatePublicNetworkAddress operation to apply for a public endpoint for a MongoDB instance.

**Request parameters**

**Response parameters**

| RequestId | String | B6D17591-B48B- 4D31-9CD6- 9B9796B2270A | The ID of the request. |
|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateNodePri vateNetworkAdd ress | The operation that you want to perform. Set the value to AllocateNodePrivateNetworkAdd ress. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the sharded cluster instance. |
| NodeId | String | Yes | d-bpxxxxxxxx | The ID of the node. Shard node ConfigServer node Mongos node |

Sample requests

```
http(s)://mongodb.aliyuncs.com/?Action=AllocatePublicNetworkAddress &DBInstanceId=dds-bp11501cd7b5**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B6D17591-B48B-4D31-9CD6-9B9796B2270A</RequestId>
```

`JSON` format

```json
{
    "RequestId": "B6D17591-B48B-4D31-9CD6-9B9796B2270A"
}
```

#### AllocateNodePrivateNetworkAddress

Call the AllocateNodePrivateNetworkAddress operation to request an intranet endpoint for a shard node or ConfigServer node of a sharded cluster instance, or to request only an IPv6 intranet endpoint for a mongos node.

**Request parameters**

| ZoneId | String | No | cn-hangzhou-b | The ID of the zone where the instance resides. |
|---|---|---|---|---|
| AccountName | String | No | shardcsaccount | The account name. Note The account name must start with a lowercase letter and contain 4 to 16 characters in length. It can contain lowercase letters, digits, and underscores ( ). _ You must specify an account name and password only when you apply for endpoints for shard, ConfigServer, or mongos nodes for the first time. All shard nodes and ConfigServer nodes use the same account and password that you specified during the first application. The account has only read-only permissions. |
| AccountPasswor d | String | No | Test123456 | The password of the account. The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Valid special characters include !#$%^&amp;*() +-= _ The password must be 8 to 32 characters in length. |
| IPVersionSelecte dType | String | No | IPv6 | The IP version. Valid values: IPv4 IPv6 IPv4v6 |

| Parameter | Type | Example | Description |
|---|---|---|---|

**Response parameters**

| RequestId | String | EFD65226-08CC- 4C4D-B6A4- CB3C382F67B0 | The ID of the request. |
|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| DBInstanc eId | Strin g | Quer y | Yes | dds-bpxxxxxxxx | The ID of the instance. If you specify the ID of a sharded cluster instance for this parameter, you must also specify the NodeId parameter. |

Sample requests

```
http(s)://mongodb.example.com/?Action=AllocateNodePrivateNetworkAddress &DBInstanceId=dds-bpxxxxxxxx &NodeId=d-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AllocateNodePrivateNetworkAddressResponse>
   <RequestId>EFD65226-08CC-4C4D-B6A4-CB3C382F67B0</RequestId>
</AllocateNodePrivateNetworkAddressResponse>
```

`JSON` format

```json
{
 "RequestId":"0FDDC511-7252-4A4A-ADDA-5CB1BF63873D"
}
```

#### ReleasePublicNetworkAddress

Call the ReleasePublicNetworkAddress operation to release the public endpoint of a MongoDB instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| NodeId | Strin g | Quer y | No | s-bpxxxxxxxx | The ID of the mongos node, shard node, or ConfigServer node in the sharded cluster instance. This parameter is available only when you specify the ID of a sharded cluster instance for the DBInstanceId parameter. |
|---|---|---|---|---|---|
| IPVersionS electedTyp e | Strin g | Quer y | No | IPv4 | The type of IP address. Valid values: IPv4 IPv6 IPv4v6 The private network of mongos nodes in a sharded cluster supports only IPv6 addresses. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1D6AFE36-1AF5- 4DE4-A954- 672159D4CC69 | The ID of the request. |

**Response parameters**

Sample requests

```
http(s)://[Endpoint]/?Action=ReleasePublicNetworkAddress &DBInstanceId=dds-bpxxxxxxxx &Common request parameters
```

Sample success responses `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"1D6AFE36-1AF5-4DE4-A954-672159D4CC69"
}
```

`XML` format

```xml
<RequestId>1D6AFE36-1AF5-4DE4-A954-672159D4CC69</RequestId>
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyInstanceV pcAuthMode | The operation that you want to perform. Set the value to ModifyInstanceVpcAuthMode. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeDBInstanceAttribute operation to view the region ID of the instance. |
| NodeId | String | No | s-bpxxxxxxxx | The ID of the mongos node in the sharded cluster instance. Note This parameter is valid only if you select a sharded cluster instance. |
| VpcAuthMode | String | No | Open | Specifies whether to enable password-free access within the VPC. Valid values: Open: enables password-free access within the VPC. Close: disables password-free access within the VPC. |

| Parameter | Type | Example | Description |
|---|---|---|---|

#### ModifyInstanceVpcAuthMode

You can call this operation to enable or disable password-free access from the same VPC as an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: A replica set or sharded cluster instance is used. The database engine version of the instance is MongoDB 4.0 or 4.2. You can call the
**DescribeDBInstanceAttribute** operation to view the database engine version of the
instance. If necessary, you can call the **UpgradeDBInstanceEngineVersion** operation to upgrade the database engine. The network type of the instance must be VPC.

**Request parameters**

**Response parameters**

| RequestId | String | BA51E9D9-B14A- 4542-B6E6- 7DE00BECCB8C | The ID of the request. |
|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeShardin gNetworkAddres s | The operation that you want to perform. Set the value to DescribeShardingNetworkAddres s. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyInstanceVpcAuthMode &DBInstanceId=dds-bpxxxxxxxx &VpcAuthMode=Open &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>BA51E9D9-B14A-4542-B6E6-7DE00BECCB8C</RequestId>
```

`JSON` format

```json
{
    "RequestId": "BA51E9D9-B14A-4542-B6E6-7DE00BECCB8C"
}
```

#### DescribeShardingNetworkAddress

Call the DescribeShardingNetworkAddress operation to query connection information for a MongoDB sharded cluster instance. This operation supports sharded cluster instances only.

**Request parameters**

| NodeId | String | No | d-bpxxxxxxxx | The ID of a mongos node, shard node, or ConfigServer node in the sharded cluster instance. Note You can call the DescribeDBInstanceAttribute operation to query the IDs of mongos, shard, and ConfigServer nodes. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CompatibleCo nnections | Array of CompatibleCo nnection |  | The list of endpoint information for instances that use the DynamoDB protocol. |
| CompatibleCo nnection |  |  |  |
| ExpiredTime | String | 2591963 | The remaining validity period of the classic network endpoint. Unit: seconds. |
| IPAddress | String | 10.140.xxx.xx | The IP address. |
| NetworkAddre ss | String | dds- bpxxxxxxxxxxxxxx. mongodb.rds.aliyu ncs.com | The endpoint. |
| NetworkType | String | VPC | The network type. Valid values: VPC: virtual private cloud Classic: classic network Public: Internet |
| Port | String | 3717 | The port number. |
| VPCId | String | vpc-bpxxxxxxxx | The ID of the VPC. Note This parameter is returned only when the network type is VPC. |

**Response parameters**

| VswitchId | String | vsw-bpxxxxxxxx | The ID of the vSwitch in the VPC. Note This parameter is returned only when the network type is VPC. |
|---|---|---|---|
| NetworkAddre sses | Array of NetworkAddre ss |  | The list of endpoint information for instances that use the MongoDB protocol. |
| NetworkAddre ss |  |  |  |
| ExpiredTime | String | 2591963 | The remaining validity period of the classic network endpoint. Unit: seconds. |
| IPAddress | String | 10.140.xxx.xx | The IP address. |
| NetworkAddre ss | String | s- bpxxxxxxxx.mongo db.rds.aliyuncs.co m | The endpoint (string). |
| NetworkType | String | VPC | The network type. VPC: virtual private cloud. Classic: classic network Public: Internet |
| NodeId | String | s-bpxxxxxxxx | The ID of the mongos node. |
| NodeType | String | mongos | The type of the node. Valid values: mongos: the mongos node shard: the shard node configserver: the configserver node |
| Port | String | 3717 | The port number. |
| Role | String | Primary | The role of the node. Valid values: Primary: the primary node Secondary: the secondary node |

| VPCId | String | vpc-bpxxxxxxxx | The ID of the VPC. Note This parameter is returned only when the network type is VPC. |
|---|---|---|---|
| VswitchId | String | vsw-bpxxxxxxxx | The ID of the vSwitch in the VPC. Note This parameter is returned only when the network type is VPC. |
| IpVersion | String | ipv4 | The IP version. Valid values: ipv4 ipv4v6 |
| IPAddress | String | 192.168.1.xxx | The IPv4 address. |
| IPAddressV6 | String | 2001:0db8:85a3:0 000:0000:8a2e:03 70:xxxx | The IPv6 address. |
| RequestId | String | 18D8AAFD-6BEB- 420F-8164- 810CB0C0AA39 | The request ID. |

Sample requests

```
http(s)://mongodb.example.com/?Action=DescribeShardingNetworkAddress &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeDBInstanceNetInfoResponse>
    <RequestId>18D8AAFD-6BEB-420F-8164-810CB0C0AA39</RequestId>
    <!-- Connection list for instances compatible with the DynamoDB protocol -->
    <CompatibleConnections>
        <CompatibleConnection>
            <IPAddress>10.140.23.45</IPAddress>
            <NetworkAddress>dds-
bp1a2b3c4d5e6f7g.mongodb.rds.aliyuncs.com</NetworkAddress>
            <NetworkType>VPC</NetworkType>
            <Port>3717</Port>
            <ExpiredTime>2591963</ExpiredTime>
            <VPCId>vpc-bp1a2b3c4d5e6f7g</VPCId>
            <VswitchId>vsw-bp1a2b3c4d5e6f7g</VswitchId>
        </CompatibleConnection>
    </CompatibleConnections>
    <!-- Connection list for instances compatible with the MongoDB protocol -->
    <NetworkAddresses>
        <NetworkAddress>
            <NodeId>s-bp1x9y8z7w6v5u4t</NodeId>
            <NodeType>mongos</NodeType>
            <Role>Primary</Role>
            <NetworkAddress>s-
bp1x9y8z7w6v5u4t.mongodb.rds.aliyuncs.com</NetworkAddress>
            <IPAddress>192.168.1.100</IPAddress>
            <IPAddressV6>2001:0db8:85a3:0000:0000:8a2e:0370:1234</IPAddressV6>
            <IpVersion>ipv4v6</IpVersion>
            <Port>3717</Port>
            <NetworkType>VPC</NetworkType>
            <ExpiredTime>2591963</ExpiredTime>
            <VPCId>vpc-bp1x9y8z7w6v5u4t</VPCId>
            <VswitchId>vsw-bp1x9y8z7w6v5u4t</VswitchId>
        </NetworkAddress>
        <NetworkAddress>
            <NodeId>d-bp1shard12345678</NodeId>
            <NodeType>shard</NodeType>
            <Role>Secondary</Role>
            <NetworkAddress>d-
bp1shard12345678.mongodb.rds.aliyuncs.com</NetworkAddress>
            <IPAddress>192.168.1.101</IPAddress>
            <IPAddressV6></IPAddressV6>
            <IpVersion>ipv4</IpVersion>
            <Port>3717</Port>
            <NetworkType>Classic</NetworkType>
            <ExpiredTime>0</ExpiredTime>
        </NetworkAddress>
    </NetworkAddresses>
</DescribeDBInstanceNetInfoResponse>
```

`JSON` format

```json
{
    "RequestId": "18D8AAFD-6BEB-420F-8164-810CB0C0AA39",
    "CompatibleConnections": {
        "CompatibleConnection": [
            {
                "IPAddress": "10.140.23.45",
                "NetworkAddress": "dds-bp1a2b3c4d5e6f7g.mongodb.rds.aliyuncs.com",
                "NetworkType": "VPC",
                "Port": "3717",
                "ExpiredTime": "2591963",
                "VPCId": "vpc-bp1a2b3c4d5e6f7g",
                "VswitchId": "vsw-bp1a2b3c4d5e6f7g"
            }
```

]

```json
    },
    "NetworkAddresses": {
        "NetworkAddress": [
            {
                "NodeId": "s-bp1x9y8z7w6v5u4t",
                "NodeType": "mongos",
                "Role": "Primary",
                "NetworkAddress": "s-bp1x9y8z7w6v5u4t.mongodb.rds.aliyuncs.com",
                "IPAddress": "192.168.1.100",
                "IPAddressV6": "2001:0db8:85a3:0000:0000:8a2e:0370:1234",
                "IpVersion": "ipv4v6",
                "Port": "3717",
                "NetworkType": "VPC",
                "ExpiredTime": "2591963",
                "VPCId": "vpc-bp1x9y8z7w6v5u4t",
                "VswitchId": "vsw-bp1x9y8z7w6v5u4t"
            },
            {
                "NodeId": "d-bp1shard12345678",
                "NodeType": "shard",
                "Role": "Secondary",
                "NetworkAddress": "d-bp1shard12345678.mongodb.rds.aliyuncs.com",
                "IPAddress": "192.168.1.101",
                "IPAddressV6": "",
                "IpVersion": "ipv4",
                "Port": "3717",
                "NetworkType": "Classic",
                "ExpiredTime": "0"
            }
```

]

```
    }
}
```

#### ModifyDBInstanceConnectionString

You can call this operation to modify the connection string of an ApsaraDB for MongoDB instance.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eConnectionStri ng | The operation that you want to perform. Set the value to ModifyDBInstanceConnectionStri ng. |
| CurrentConnecti onString | String | Yes | s- bpxxxxxxxx.mon godb.rds.aliyunc s.com | The current connection string, which is to be modified. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NewConnectionS tring | String | Yes | aliyuntest111 | The new connection string. It must be 8 to 64 characters in length and can contain letters and digits. It must start with a lowercase letter. Note You only need to specify the prefix of the connection string. The content other than the prefix cannot be modified. |
| NodeId | String | No | s-bpxxxxxxxx | The ID of the mongos node in the sharded cluster instance. Only one mongos ID can be specified in each call. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FF36A84C-0694- 42D0-861D- C383E8E4FAAF | The ID of the request. |

**Request parameters**

**Response parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| DBInstanc eId | Strin g | Quer y | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeId | Strin g | Quer y | No | s-bpxxxxxxxx | The ID of the replica set instance. |
| IPVersionS electedTyp e | Strin g | Quer y | No | IPv6 | The IP version. Set the value to IPv6. |

Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceConnectionString &CurrentConnectionString=s-bpxxxxxxxx.mongodb.rds.aliyuncs.com &NewConnectionString=aliyuntest111 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyDBInstanceConnectionStringResponse>
   <RequestId>FF36A84C-0694-42D0-861D-C383E8E4FAAF</RequestId>
</ModifyDBInstanceConnectionStringResponse>
```

`JSON` format

```json
{
 "RequestId": "FF36A84C-0694-42D0-861D-C383E8E4FAAF"
}
```

#### ReleasePrivateNetworkAddress

Call the ReleasePrivateNetworkAddress operation to release the IPv6 private network address of a MongoDB replica set instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F8CA8312-530A- 413A-9129- F2BB32A8D404 | The ID of the request. |

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| DBInstanc eId | Strin g | Quer y | Yes | dds-bp1a7009eb24**** | The ID of the sharded cluster instance. |

Sample requests

```
http(s)://[Endpoint]/?Action=ReleasePrivateNetworkAddress &DBInstanceId=dds-bpxxxxxxxx &Common request parameters
```

Sample success responses `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"F8CA8312-530A-413A-9129-F2BB32A8D404"
}
```

`XML` format

```xml
<RequestId>F8CA8312-530A-413A-9129-F2BB32A8D404</RequestId>
```

#### ReleaseNodePrivateNetworkAddress

Call the ReleaseNodePrivateNetworkAddress operation to release the internal endpoint of a shard or ConfigServer node in an ApsaraDB for MongoDB sharded cluster instance, or to release only the IPv6 internal endpoint of a mongos node.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| NodeId | Strin g | Quer y | Yes | d-bp128a003436**** | The ID of the node. Shard node ConfigServer node Mongos node |
|---|---|---|---|---|---|
| NetworkTy pe | Strin g | Quer y | Yes | VPC | The network type to which the internal endpoint of the node belongs. Valid values: VPC: virtual private cloud Classic: classic network |
| IPVersionS electedTyp e | Strin g | Quer y | No | IPv4 | The IP version. Default value: IPv4. Valid values: IPv4 IPv6 IPv4v6 Only IPv6 is supported for the private endpoint of mongos in a sharded cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252- 4A4A-ADDA- 5CB1BF63873D | The ID of the request. |

**Response parameters**

Sample requests

```
http(s)://[Endpoint]/?Action=ReleaseNodePrivateNetworkAddress &DBInstanceId=dds-bp1a7009eb24**** &NodeId=d-bp128a003436**** &Common request parameters
```

Sample success responses `JSON` format

```json
{
    "RequestId":"0FDDC511-7252-4A4A-ADDA-5CB1BF63873D"
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeReplica SetRole | The operation that you want to perform. Set the value to DescribeReplicaSetRole. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DB4A0595-FCA9- 437F-B2BB- 25DBFC009D3E | The ID of the request. |
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |
| ReplicaSets | Array of ReplicaSet |  | The list of replica set role information. |
| ReplicaSet |  |  |  |
| ConnectionDo main | String | dds- bpxxxxxxxx.mongo db.rds.aliyuncs.co m | The connection endpoint of the node. |

`XML` format

```xml
<ReleaseNodePrivateNetworkAddressResponse>
      <RequestId>EFD65226-08CC-4C4D-B6A4-CB3C382F67B0</RequestId>
</ReleaseNodePrivateNetworkAddressResponse>
```

### Instance information query

#### DescribeReplicaSetRole

Call the DescribeReplicaSetRole operation to query role information and connection information for a MongoDB instance. This operation applies to replica set instances. It does not apply to sharded cluster instances.

**Request parameters**

**Response parameters**

| ConnectionPor t | String | 3717 | The connection port of the node. |
|---|---|---|---|
| ExpiredTime | String | 1209582 | The remaining duration of the classic network endpoint. Unit: seconds. |
| NetworkType | String | VPC | The network type. VPC: virtual private cloud Classic: classic network. Public: Internet |
| ReplicaSetRole | String | Primary | The role of the node in the replica set. Primary: primary node Secondary: secondary node |
| RoleId | String | 651xxxxx | The role ID of the node. |
| NodeType | String | mongos | The type of the node. mongos: mongos node shard: shard node configserver: ConfigServer node |
| IpVersion | String | ipv4 | The IP version. Valid values: ipv4 ipv4v6 |
| IpAddress | String | 192.168.1.xxx | The IPv4 address. |
| IpAddressV6 | String | 2001:0db8:85a3:0 000:0000:8a2e:03 70:xxxx | The IPv6 address. |

Sample requests

```
http(s)://mongodb.example.com/?Action=DescribeReplicaSetRole &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
    <RequestId>7762D0FF-F34D-4DAF-9D06-6C1C28CC98CD</RequestId>
    <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId>
    <ReplicaSets>
        <ReplicaSet>
            <NetworkType>Classic</NetworkType>
            <ConnectionPort>3717</ConnectionPort>
            <ReplicaSetRole>Primary</ReplicaSetRole>
            <ConnectionDomain>dds-
bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
            <ExpiredTime>12xxxxx</ExpiredTime>
            <RoleId>55xxxxx</RoleId>
            <IpVersion>ipv4</IpVersion>
            <IpAddress>192.168.1.105</IpAddress>
            <IpAddressV6></IpAddressV6>
        </ReplicaSet>
        <ReplicaSet>
            <NetworkType>Classic</NetworkType>
            <ConnectionPort>3717</ConnectionPort>
            <ReplicaSetRole>Secondary</ReplicaSetRole>
            <ConnectionDomain>dds-
bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
            <ExpiredTime>12xxxxx</ExpiredTime>
            <RoleId>55xxxxx</RoleId>
            <IpVersion>ipv4</IpVersion>
            <IpAddress>192.168.1.106</IpAddress>
            <IpAddressV6></IpAddressV6>
        </ReplicaSet>
        <ReplicaSet>
            <NetworkType>VPC</NetworkType>
            <ConnectionPort>3717</ConnectionPort>
            <ReplicaSetRole>Primary</ReplicaSetRole>
            <ConnectionDomain>dds-
bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
            <RoleId>55xxxxx</RoleId>
            <IpVersion>ipv4v6</IpVersion>
            <IpAddress>10.0.0.50</IpAddress>
            <IpAddressV6>2001:0db8:85a3:0000:0000:8a2e:0370:7334</IpAddressV6>
        </ReplicaSet>
        <ReplicaSet>
            <NetworkType>VPC</NetworkType>
            <ConnectionPort>3717</ConnectionPort>
            <ReplicaSetRole>Secondary</ReplicaSetRole>
            <ConnectionDomain>dds-
bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
            <RoleId>55xxxxx</RoleId>
            <IpVersion>ipv4v6</IpVersion>
            <IpAddress>10.0.0.51</IpAddress>
            <IpAddressV6>2001:0db8:85a3:0000:0000:8a2e:0370:7335</IpAddressV6>
        </ReplicaSet>
    </ReplicaSets>
```

`JSON` format

```json
{
    "RequestId": "7762D0FF-F34D-4DAF-9D06-6C1C28CC98CD",
    "DBInstanceId": "dds-bpxxxxxxxx",
    "ReplicaSets": {
        "ReplicaSet": [
            {
                "NetworkType": "Classic",
                "ConnectionPort": "3717",
                "ReplicaSetRole": "Primary",
                "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
                "ExpiredTime": "12xxxxx",
                "RoleId": "55xxxxx",
                "IpVersion": "ipv4",
                "IpAddress": "192.168.1.105",
                "IpAddressV6": ""
            },
            {
                "NetworkType": "Classic",
                "ConnectionPort": "3717",
                "ReplicaSetRole": "Secondary",
                "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
                "ExpiredTime": "12xxxxx",
                "RoleId": "55xxxxx",
                "IpVersion": "ipv4",
                "IpAddress": "192.168.1.106",
                "IpAddressV6": ""
            },
            {
                "NetworkType": "VPC",
                "ConnectionPort": "3717",
                "ReplicaSetRole": "Primary",
                "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
                "RoleId": "55xxxxx",
                "IpVersion": "ipv4v6",
                "IpAddress": "10.0.0.50",
                "IpAddressV6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
            },
            {
                "NetworkType": "VPC",
                "ConnectionPort": "3717",
                "ReplicaSetRole": "Secondary",
                "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
                "RoleId": "55xxxxx",
                "IpVersion": "ipv4v6",
                "IpAddress": "10.0.0.51",
                "IpAddressV6": "2001:0db8:85a3:0000:0000:8a2e:0370:7335"
            }
```

]

```
    }
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeKernelR eleaseNotes | The operation that you want to perform. Set the value to DescribeKernelReleaseNotes. |
| KernelVersion | String | No | mongodb 20180 _ 522 0.4.8 _ | The minor version of the database. Example: mongodb 20180522 0.4.8. _ _ If you specify this parameter, a list of versions later than the version specified is returned. If you do not specify this parameter, a list of all versions is returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ReleaseNotes | Array of ReleaseNote |  | An array that consists of the information of version release notes. |
| ReleaseNote |  |  |  |
| KernelVersion | String | mongodb 2018061 _ 9 0.4.9 _ | The version of the database. |
| ReleaseNote | String | Released the balancer switch limit for a sharded set | The release notes. |
| RequestId | String | F01D4DDA-CB72- 4083-B399- AF4642294FE6 | The ID of the request. |

#### DescribeKernelReleaseNotes

You can call this operation to view the release notes of the minor database versions of an ApsaraDB for MongoDB instance.

**Request parameters**

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeKernelReleaseNotes &<Common request parameters>
```

Sample success responses

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAvailabl eEngineVersion | The operation that you want to perform. Set the value to DescribeAvailableEngineVersion. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 52507B6B-003B- 47A3-A0A3- 9FE992C7A243 | The ID of the request. |

`XML` format

```xml
<RequestId>F01D4DDA-CB72-4083-B399-AF4642294FE6</RequestId> <ReleaseNotes>
    <ReleaseNote>
        <KernelVersion>mongodb_20180619_0.4.9</KernelVersion>
        <ReleaseNote>Released the balancer switch limit for a sharded set</ReleaseNote>
    </ReleaseNote>
</ReleaseNotes>
```

`JSON` format

```json
{
    "RequestId":"F01D4DDA-CB72-4083-B399-AF4642294FE6",
    "ReleaseNotes":
    {
        "ReleaseNote":[
            {
                "KernelVersion":"mongodb_20180619_0.4.9",
                "ReleaseNote":"Released the balancer limit for a sharded set"
            }
```

]

```
    }
}
```

#### DescribeAvailableEngineVersion

You can call this operation to view the database engine versions that an ApsaraDB for MongoDB instance can be upgraded to.

**Request parameters**

**Response parameters**

| EngineVersion s | List | {"EngineVersion": ["4.0" ]} | The databse engine versions that the ApsaraDB for MongoDB instance can be upgraded to. Note An empty string is returned if the latest version is being used. |
|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAvailableEngineVersion &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <EngineVersions>
      <EngineVersion>4.0</EngineVersion>
   </EngineVersions>
   <RequestId>52507B6B-003B-47A3-A0A3-9FE992C7A243</RequestId>
```

`JSON` format

```json
{
 "EngineVersions": {
  "EngineVersion": [
   "4.0"
```

]

```json
 },
 "RequestId": "52507B6B-003B-47A3-A0A3-9FE992C7A243"
}
```

#### DescribeDBInstances

Queries the list of ApsaraDB for MongoDB instances. When you call this operation, you must configure the `x-acs-organizationid` , `x-acs-` `resourcegroupid` , and `x-acs-instanceid` header parameters to specify the organization ID, resource group ID, and instance ID. Otherwise, the call is directed to the root resource group and organization. For more information about the code, see SDK Description in ApsaraDB for MongoDB Developer Guide.

**Request parameters**

| Action | String | Yes | DescribeDBInsta nces | The operation that you want to perform. Set the value to DescribeDBInstances. |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be an integer that is greater than 0. Default value: 1. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| DBInstanceId | String | No | dds- d1n4eab47879* *** | The ID of the instance. |
| ReplicationFacto r | String | No | 3 | The number of nodes in the replica set instance. Valid values: 3, 5, and 7. |
| DBInstanceDesc ription | String | No | test | The description of the instance. |
| ExpireTime | String | No | 2019-12- 26T16:00Z | The time when the instance expires. |
| DBInstanceStatu s | String | No | ACTIVATION | The status of the instance. For more information, see Instance states in ApsaraDB for MongoDB Developer Guide. |
| DBInstanceType | String | No | replicate | The architecture of the instance. Valid values: sharding: sharded cluster instance replicate: replica set instance or standalone instance Default value: replicate. |
| DBInstanceClass | String | No | dds.mongo.mid | The instance type. Note For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. |
| Engine | String | No | MongoDB | The database engine of the instance. Set the value to MongoDB. |

| EngineVersion | String | No | 4.2 | The database engine version of the instance. Valid values: 3.0, 3.4, 4.0, and 4.2. |
|---|---|---|---|---|
| NetworkType | String | No | Classic | The network type of the instance. Valid values: Classic VPC Set the value to Classic. |
| VpcId | String | No | vpc- bp1q2qqm4vxo 6e6zl**** | The ID of the virtual private cloud (VPC). |
| VSwitchId | String | No | vsw- bp1buy0h9myt5 i9e7**** | The ID of the vSwitch in the VPC. |
| ChargeType | String | No | PostPaid | The billing method of the instance. Valid values: PrePaid: subscription PostPaid: pay-as-you-go |
| ZoneId | String | No | cn-qd-agility14- amtest110**** | The zone ID of the instance. Note You can call the DescribeRegions operation to query available zones. |
| Expired | String | No | true | Specifies whether the instance has expired. Valid values: true: The instance has expired. false: The instance has not expired. |
| ResourceGroupI d | String | No | rg- acfm22cdcgc*** * | The ID of the resource group. |

| Tag.N.Key | String | No | testdatabase | The key of tag N. Note Valid values of N: 1 to 20. The tag key cannot exceed 64 characters in length. The tag key cannot start with aliyun , acs: , http:// , or https:// . The tag key cannot be an empty string. |
|---|---|---|---|---|
| Tag.N.Value | String | No | apitest | The value of tag N. Note Valid values of N: 1 to 20. The tag value cannot exceed 128 characters in length. The tag value cannot start with aliyun , acs: , http:// , or https:// . The tag value can be an empty string. |

|  | aliyun |  |  |
|---|---|---|---|
| acs: |  |  |  |
|  |  | , |  |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstances | Array of DBInstance |  | Details about the instances. |
| DBInstance |  |  |  |
| ChargeType | String | PostPaid | The billing method of the instance. PrePaid: subscription PostPaid: pay-as-you-go |

**Response parameters**

| CreationTime | String | 2021-05- 31T12:00:52Z | The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
|---|---|---|---|
| DBInstanceCla ss | String | dds.mongo.mid | The instance type. Note For more information, see Instance types in ApsaraDB for MongoDB Product Introduction. |
| DBInstanceDe scription | String | Test database | The description of the instance. |
| DBInstanceId | String | dds- d1n4eab47879**** | The ID of the instance. |
| DBInstanceSta tus | String | Running | The status of the instance. |
| DBInstanceSto rage | Integer | 50 | The storage space of the instance. |
| DBInstanceTy pe | String | replicate | The architecture of the instance. Valid values: sharding: sharded cluster instance replicate: replica set instance |
| DestroyTime | String | 2021-12- 31T16:00:00Z | The time when the instance data was destroyed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. Note Subscription instances are released seven days after expiration. After an instance is released, its data is deleted and cannot be restored. Pay-as-you-go instances are locked after the payment has been overdue for longer than 24 hours. Pay-as-you-go instances are released after the payment has been overdue for longer than seven days. The data of released instances is deleted and cannot be restored. |
| Engine | String | MongoDB | The database engine of the instance. |

| EngineVersion | String | 3.0 | The database engine version of the instance. |
|---|---|---|---|
| ExpireTime | String | 2019-11- 25T16:00Z | The time when the instance expires. The time follows the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| KindCode | String | 1 | The kind code of the instance. Valid values: 0: physical machine 1: Elastic Compute Service (ECS) instance 2: Docker cluster 18: Kubernetes cluster |
| LastDowngrad eTime | String | 20210708 | The time when the instance was last downgraded. |
| LockMode | String | unlock | Indicates whether the instance is locked. Valid values: Unlock: The instance is not locked. ManualLock: The instance is manually locked. LockByExpiration: The instance is automatically locked after it expires. LockByRestoration: The instance is automatically locked before it is rolled back. LockByDiskQuota: The instance is automatically locked after the storage space is exhausted. Released: The instance is released. You cannot unlock an instance that is released. After an instance is released, you can only use a backup to restore the data of the instance to a new instance. This process requires a long period of time. |
| MongosList | Array of MongosAttribu te |  | Details about the mongos nodes. Note This parameter is returned if the instance is a sharded cluster instance. |
| MongosAttribu te |  |  |  |
| NodeClass | String | dds.mongos.mid | The type of the mongos node. |

| NodeDescripti on | String | Test mongos node | The description of the mongos node. |
|---|---|---|---|
| NodeId | String | s- d1n849c1788f**** | The ID of the mongos node. |
| NetworkType | String | Classic | The network type of the instance. The value is fixed at Classic. |
| RegionId | String | cn-qd-agility14**** | The region ID of the instance. |
| ReplicationFac tor | String | 3 | The number of nodes in the instance. Note This parameter is returned if the instance is a replica set instance. |
| ResourceGrou pId | String | rg- acfm22cdcgc**** | The ID of the resource group. |
| ShardList | Array of ShardAttribute |  | Details about the shard nodes. Note This parameter is returned if the instance is a sharded cluster instance. |
| ShardAttribute |  |  |  |
| NodeClass | String | dds.shard.mid | The type of the shard node. |
| NodeDescripti on | String | Test shard node | The description of the shard node. |
| NodeId | String | d- d1n753c91603**** | The ID of the shard node. |
| NodeStorage | Integer | 20 | The storage space of the shard node. Unit: GB. |
| Tags | Array of Tag |  | Details about the resource tags. |
| Tag |  |  |  |
| Key | String | test | The tag key of the resource. |
| Value | String | api | The tag value of the resource. |

| VpcAuthMode | String | Close | Indicates whether password-free access within the VPC is enabled. Valid values: Open: Password-free access is enabled. Close: Password-free access is disabled. |
|---|---|---|---|
| ZoneId | String | cn-qd-agility14- amtest110**** | The zone ID of the instance. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 30 | The number of entries returned per page. |
| RequestId | String | A10B8ECB-0BA0- 4EC6-93A5- C65FDEDA**** | The ID of the request. |
| TotalCount | Integer | 1 | The number of instances in the query results. |

Sample requests

```
http(s)://mongodb.example.com/?Action=DescribeDBInstances &<Common request parameters>
```

Sample success responses `XML` format

```xml
  <TotalCount>1</TotalCount>
  <PageSize>30</PageSize>
  <RequestId>A10B8ECB-0BA0-4EC6-93A5-C65FDEDA****</RequestId>
  <PageNumber>1</PageNumber>
  <DBInstances>
        <EngineVersion>3.0</EngineVersion>
        <ReplicationFactor>3</ReplicationFactor>
        <DBInstanceStatus>Running</DBInstanceStatus>
        <ZoneId>cn-qd-agility14-amtest110****</ZoneId>
        <ResourceGroupId>rg-acfm22cdcgc****</ResourceGroupId>
        <DBInstanceClass>dds.mongo.mid</DBInstanceClass>
        <DestroyTime>2021-12-31T16:00:00Z</DestroyTime>
        <DBInstanceType>replicate</DBInstanceType>
        <LockMode>unlock</LockMode>
        <DBInstanceId>dds-d1n4eab47879****</DBInstanceId>
        <VpcAuthMode>Close</VpcAuthMode>
        <NetworkType>Classic</NetworkType>
        <ChargeType>PostPaid</ChargeType>
        <LastDowngradeTime>20210708</LastDowngradeTime>
        <DBInstanceStorage>50</DBInstanceStorage>
        <CreationTime>2021-05-31T12:00:52Z</CreationTime>
        <RegionId>cn-qd-agility14****</RegionId>
        <ExpireTime>2019-11-25T16:00Z</ExpireTime>
        <KindCode>1</KindCode>
        <Engine>MongoDB</Engine>
        <DBInstanceDescription>Test database</DBInstanceDescription>
        <ShardList>
              <NodeClass>dds.shard.mid</NodeClass>
              <NodeDescription>Test shard node</NodeDescription>
              <NodeStorage>20</NodeStorage>
              <NodeId>d-d1n753c91603****</NodeId>
        </ShardList>
        <MongosList>
              <NodeClass>dds.mongos.mid</NodeClass>
              <NodeDescription>Test mongos node</NodeDescription>
              <NodeId>s-d1n849c1788f****</NodeId>
        </MongosList>
        <Tags>
              <Value>api</Value>
              <Key>test</Key>
        </Tags>
  </DBInstances>
```

`JSON` format

```json
{
  "TotalCount": "1",
  "PageSize": "30",
  "RequestId": "A10B8ECB-0BA0-4EC6-93A5-C65FDEDA****",
  "PageNumber": "1",
  "DBInstances": [
    {
      "EngineVersion": "3.0",
      "ReplicationFactor": "3",
      "DBInstanceStatus": "Running",
      "ZoneId": "cn-qd-agility14-amtest110****",
      "ResourceGroupId": "rg-acfm22cdcgc****",
      "DBInstanceClass": "dds.mongo.mid",
      "DestroyTime": "2021-12-31T16:00:00Z",
      "DBInstanceType": "replicate",
      "LockMode": "unlock",
      "DBInstanceId": "dds-d1n4eab47879****",
      "VpcAuthMode": "Close",
      "NetworkType": "Classic",
      "ChargeType": "PostPaid",
      "LastDowngradeTime": "20210708",
      "DBInstanceStorage": "50",
      "CreationTime": "2021-05-31T12:00:52Z",
      "RegionId": "cn-qd-agility14****",
      "ExpireTime": "2019-11-25T16:00Z",
      "KindCode": "1",
      "Engine": "MongoDB",
      "DBInstanceDescription": "Test database",
      "ShardList": [
        {
          "NodeClass": "dds.shard.mid",
          "NodeDescription": "Test shard node",
          "NodeStorage": "20",
          "NodeId": "d-d1n753c91603****"
        }
```

`],`

```json
      "MongosList": [
        {
          "NodeClass": "dds.mongos.mid",
          "NodeDescription": "Test mongos node",
          "NodeId": "s-d1n849c1788f****"
        }
```

`],`

```json
      "Tags": [
        {
          "Value": "api",
          "Key": "test"
        }
```

]

```
    }
```

]

```
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceAttribute | The operation that you want to perform. Set the value to DescribeDBInstanceAttribute. |
| DBInstanceId | String | Yes | dds- bp11483712c1* *** | The ID of the instance. |
| Engine | String | No | MongoDB | The database engine. The value is fixed to MongoDB. |
| ResourceGroupI d | String | No | rg- acfmyiu4ekp**** | The ID of the resource group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C373EED9-5125- 4DD9-89DB- FB1ECD2C2B4F | The request ID. |
| DBInstances | Array of DBInstan ce |  | The list of instance information. |
| DBInstance |  |  |  |
| CpuType | String | intel | The CPU type. |
| ChargeType | String | PostPaid | The billing method of the instance. Valid values: PostPaid: pay-as-you-go |

#### DescribeDBInstanceAttribute

Call the DescribeDBInstanceAttribute operation to query information about ApsaraDB for MongoDB instances.

**Request parameters**

**Response parameters**

| Configserver List | Array of Configser verAttrib ute |  | The list of Configserver node information. Note This parameter is returned only when the instance type is a sharded cluster instance. |
|---|---|---|---|
| Configserver Attribute |  |  |  |
| ConnectStri ng | String | mongodb://root:** **@dds- bp11483712c1*** *-cs1730- pub.mongodb.rds .aliyuncs.com:371 7 | The connection address of the Configserver node. |
| MaxConnect ions | Integer | 8000 | The maximum number of connections for the Configserver node. |
| MaxIOPS | Integer | 8000 | The maximum IOPS for the Configserver node. |
| NodeClass | String | dds.cs.mid | The specification of the Configserver node. |
| NodeDescrip tion | String | testConfigserver | The name of the Configserver node. |
| NodeId | String | dds- bp11483712c1*** *-cs | The ID of the Configserver node. |
| NodeStorag e | Integer | 20 | The storage capacity of the Configserver node. Unit: GB. |
| Port | Integer | 3717 | The port of the Configserver node. |
| CreationTim e | String | 2022-08- 21T05:10:00Z | The time when the instance was created. The time follows the yyyy-MM-ddTHH:mm:ssZ format in UTC. |
| CurrentKern elVersion | String | mongodb 201809 _ 14 1.1.5 _ | The kernel version of the current database instance. |
| DBInstanceC lass | String | dds.mongo.mid | The specification of the instance. |

| DBInstance Description | String | ceshi | The instance name. |
|---|---|---|---|
| DBInstanceI d | String | dds- bp11483712c1*** * | The instance ID. |
| DBInstanceR eleaseProtec tion | Boolean | false | Indicates whether release protection is enabled for the instance. Valid values: true: enabled false: (default) not enabled |
| DBInstanceS tatus | String | Running | The status of the instance. Valid values: Creating: creating Running: running DBInstanceClassChanging: upgrading or downgrading DBInstanceNetTypeChanging: switching between internal and public networks Deleting: deleting EngineVersionUpgrading: migrating the version GuardSwitching: performing the disaster recovery failover HASwitching: performing the primary/secondary switchover ImportingFromOthers: importing from databases LinkSwitching: switching the link EngineVersionUpgrading: performing the major version upgrade MinorVersionUpgrading: performing the minor version upgrade NET CREATING: creating a network connection _ NET DELETING: deleting a network connection _ NodeCreating: creating an instance node NodeDeleting: deleting an instance node Rebooting: rebooting Restoring: restoring from backup SSLModifying: modifying SSL settings TempDBInstanceCreating: creating a temporary instance Transing: migrating an instance TransingToOthers: migrating to another database |

| DBInstanceS torage | Integer | 10 | The storage capacity of the instance. Unit: GB. |
|---|---|---|---|
| DBInstanceT ype | String | replicate | The type of the instance. Valid values: replicate: replica set instance sharding: sharded cluster instance |
| Engine | String | MongoDB | The database engine. |
| EngineVersi on | String | 3.4 | The database version. Valid values: 4.2 4.0 3.4 3.0 Note Only replica set instances support version 3.0. |
| ExpireTime | String | None | Not applicable. |
| KindCode | String | 0 | The specification type of the instance. Valid values: 0: physical machine |
| LastDowngr adeTime | String | 2022-08-28 | The most recent downgrade time of the instance. Format: yyyy-MM-dd (UTC). |
| LockMode | String | Unlock | The lock status of the instance. Valid values: Unlock: normal, not locked. ManualLock: Manually trigger the lock. LockByExpiration: Automatically locked due to instance expiration. LockByRestoration: Automatically locked before instance rollback. LockByDiskQuota: Automatically locked because the instance storage is full. Released: The instance has been released. You cannot unlock the instance. You can only recreate a new instance from backup data. Recreation takes a long time. Please wait patiently. |

| MaintainEnd Time | String | 03:00Z | The end time of the maintenance window for the instance. Format: HH:mmZ (UTC). |
|---|---|---|---|
| MaintainStar tTime | String | 02:00Z | The start time of the maintenance window for the instance. Format: HH:mmZ (UTC). |
| MaxConnect ions | Integer | 500 | The maximum number of connections for the instance. |
| MaxIOPS | Integer | 1000 | The maximum IOPS for the instance. |
| MongosList | Array of MongosAt tribute |  | The list of mongos node information. Note This parameter is returned when the instance type is a sharded cluster instance. |
| MongosAttri bute |  |  |  |
| ConnectStin g | String | s- bp1d8c262a158* ***.mongodb.rds. aliyuncs.com | The endpoint of the mongos node. |
| MaxConnect ions | Integer | 1000 | The maximum number of connections for the mongos node. |
| MaxIOPS | Integer | 800 | The maximum IOPS for the mongos node. |
| NodeClass | String | dds.mongos.mid | The specification code of the mongos node. |
| NodeDescrip tion | String | mongos1 | The name of the mongos node. |
| NodeId | String | s- bp1d8c262a158* *** | The ID of the mongos node. |
| Port | Integer | 3717 | The connection port of the mongos node. |

| VPCId | String | vpc- bp1n3i15v90el48 nx**** | The ID of the virtual private cloud (VPC) for the mongos node. |
|---|---|---|---|
| VSwitchId | String | vsw- bp1n3i15v90el48 nx**** | The ID of the vSwitch for the mongos node. |
| VpcCloudIns tanceId | String | s- bp1d8c262a158* *** | The VPC ID of the mongos node. |
| NetworkTyp e | String | VPC | The network type of the instance. Valid values: Classic: classic network VPC: virtual private cloud |
| ProtocolTyp e | String | mongodb | The access protocol type of the instance. Valid values: mongodb: MongoDB protocol |
| ReadonlyRe plicas | String | 0 | The number of read-only nodes for the instance. Currently, read-only nodes are not supported. The value is 0. |
| RegionId | String | cn-qingdao- env17-d01 | The region ID of the instance. |
| ReplacateId | String | bls-mgs**** | The ID of the BLS channel. |
| ReplicaSetN ame | String | test | The name of the replica set for the instance. Note This parameter is returned when the instance type is a replica set instance. |
| ReplicaSets | Array of ReplicaSe t |  | The information about the replica set instance. Note This parameter is returned when the instance type is a replica set instance. |

| ReplicaSet |  |  |  |
|---|---|---|---|
| IPVersion | String | IPv4 | The IP version. Valid values: IPv4 IPv4v6 |
| IPAddress | String | 192.168.1.xxx | The IPv4 address. |
| IPAddressV6 | String | 2001:0db8:85a3: 0000:0000:8a2e: 0370:xxxx | The IPv6 address. |
| ConnectionD omain | String | dds- bp11483712c1*** *.mongodb.rds.ali yuncs.com | The endpoint of the node. |
| ConnectionP ort | String | 3717 | The connection port of the node. |
| NetworkTyp e | String | VPC | The network type of the node. Valid values: Classic: classic network VPC: virtual private cloud |
| ReplicaSetR ole | String | Primary | The role of the node. Valid values: Primary: primary node Secondary: secondary node |
| VPCCloudIns tanceId | String | vpc- bp1jk5vwkcri27q me**** | The ID of the VPC-connected instance. |
| VPCId | String | vpc- bp1jk5vwkcri27q me**** | The ID of the virtual private cloud. |
| VSwitchId | String | vsw- bp1jk5vwkcri27q me**** | The ID of the vSwitch in the virtual private cloud. |
| ReplicationF actor | String | 3 | The number of nodes for the instance. |

| ResourceGro upId | String | rg-a7qme**** | The ID of the resource group to which the instance belongs. |
|---|---|---|---|
| ShardList | Array of ShardAttr ibute |  | The list of shard node information. Note This parameter is returned when the instance type is a sharded cluster instance. |
| ShardAttribu te |  |  |  |
| ConnectStri ng | String | d- bp1af0680a9c6d 3****.mongodb.rd s.aliyuncs.com | The endpoint of the shard node. |
| MaxConnect ions | Integer | 8000 | The maximum number of connections for the shard node. |
| MaxIOPS | Integer | 8000 | The maximum IOPS for the shard node. |
| NodeClass | String | dds.shard.mid | The specification of the shard node. |
| NodeDescrip tion | String | testshard | The name of the shard node. |
| NodeId | String | d- bp16e09d9c5d*** * | The ID of the shard node. |
| NodeStorag e | Integer | 10 | The storage capacity of the shard node. Unit: GB. |
| Port | Integer | 3717 | The port of the shard node. |
| StorageEngi ne | String | WiredTiger | The storage engine type of the instance. |
| Tags | Array of Tag |  | The list of tag information for the instance. |
| Tag |  |  |  |

| Key | String | test | The tag key of the instance. |
|---|---|---|---|
| Value | String | api | The tag value of the instance. |
| VPCId | String | vpc- bp1jk5vwkcri27q me**** | The ID of the virtual private cloud. |
| VSwitchId | String | vsw- bp1oo2a7isyrb8ig f**** | The ID of the vSwitch in the virtual private cloud. |
| VpcAuthMod e | String | NotSupport | The password-free access mode over the internal network. Valid values: Open: Password-free access over the internal network is enabled. Close: Password-free access over the internal network is disabled. You must use a password to access the instance. NotSupport: This feature is not supported. |
| ZoneId | String | cn-qingdao- ft154e- amtest154001-a | The ID of the zone to which the instance belongs. |

Sample requests

```
http(s)://mongodb.example.com/?Action=DescribeDBInstanceAttribute &DBInstanceId=dds-bp11483712c1**** &<Common Request Parameter>
```

Sample success responses `XML` format

```xml
    <RequestId>C373EED9-5125-4DD9-89DB-FB1ECD2C2B4F</RequestId>
    <DBInstances>
        <DBInstance>
            <!-- Basic information -->
            <DBInstanceId>dds-bp11483712c1****</DBInstanceId>
            <DBInstanceDescription>ceshi</DBInstanceDescription>
            <DBInstanceClass>dds.mongo.mid</DBInstanceClass>
            <DBInstanceStorage>10</DBInstanceStorage>
            <DBInstanceType>sharding</DBInstanceType>
            <Engine>MongoDB</Engine>
            <EngineVersion>4.4</EngineVersion>
            <ChargeType>PostPaid</ChargeType>
<DBInstanceStatus>Running</DBInstanceStatus>
```

```xml
            <DBInstanceStatus>Running</DBInstanceStatus>
            <CreationTime>2022-08-21T05:10:00Z</CreationTime>
            <ExpireTime></ExpireTime>
            <RegionId>cn-qingdao-env17-d01</RegionId>
            <ZoneId>cn-qingdao-ft154e-amtest154001-a</ZoneId>
            <NetworkType>VPC</NetworkType>
            <VPCId>vpc-bp1n3i15v90el48nx****</VPCId>
            <VSwitchId>vsw-bp1n3i15v90el48nx****</VSwitchId>
            <VPCCloudInstanceIds>s-bp1d8c262a158****</VPCCloudInstanceIds>
            <MaxConnections>500</MaxConnections>
            <MaxIOPS>1000</MaxIOPS>
            <MaintainStartTime>02:00Z</MaintainStartTime>
            <MaintainEndTime>03:00Z</MaintainEndTime>
            <LockMode>Unlock</LockMode>
            <DBInstanceReleaseProtection>false</DBInstanceReleaseProtection>
            <CurrentKernelVersion>mongodb_20180914_1.1.5</CurrentKernelVersion>
            <StorageEngine>WiredTiger</StorageEngine>
            <ProtocolType>mongodb</ProtocolType>
            <ReadonlyReplicas>0</ReadonlyReplicas>
            <ReplicationFactor>3</ReplicationFactor>
            <ResourceGroupId>rg-a7qme****</ResourceGroupId>
            <KindCode>0</KindCode>
            <LastDowngradeTime>2022-08-28</LastDowngradeTime>
            <ReplacateId>bls-mgs****</ReplacateId>
            <VpcAuthMode>Close</VpcAuthMode>
            <!-- New parameters -->
            <CpuType>intel</CpuType>
            <!-- Sharded cluster specific: Mongos node list -->
            <MongosList>
                <MongosAttribute>
                    <NodeId>s-bp1d8c262a158****</NodeId>
                    <NodeDescription>mongos1</NodeDescription>
                    <NodeClass>dds.mongos.mid</NodeClass>
                    <ConnectSting>s-
bp1d8c262a158****.mongodb.rds.aliyuncs.com</ConnectSting>
                    <Port>3717</Port>
                    <MaxConnections>1000</MaxConnections>
                    <MaxIOPS>800</MaxIOPS>
                    <VPCId>vpc-bp1n3i15v90el48nx****</VPCId>
                    <VSwitchId>vsw-bp1n3i15v90el48nx****</VSwitchId>
                    <VpcCloudInstanceId>s-bp1d8c262a158****</VpcCloudInstanceId>
                </MongosAttribute>
            </MongosList>
            <!-- Sharded cluster specific: Shard node list -->
            <ShardList>
                <ShardAttribute>
                    <NodeId>d-bp16e09d9c5d****</NodeId>
                    <NodeDescription>testshard</NodeDescription>
                    <NodeClass>dds.shard.mid</NodeClass>
                    <ConnectString>d-
bp1af0680a9c6d3****.mongodb.rds.aliyuncs.com</ConnectString>
                    <Port>3717</Port>
                    <NodeStorage>10</NodeStorage>
```

g g

```xml
                    <MaxConnections>8000</MaxConnections>
                    <MaxIOPS>8000</MaxIOPS>
                </ShardAttribute>
            </ShardList>
            <!-- Sharded cluster specific: ConfigServer node list -->
            <ConfigserverList>
                <ConfigserverAttribute>
                    <NodeId>dds-bp11483712c1****-cs</NodeId>
                    <NodeDescription>testConfigserver</NodeDescription>
                    <NodeClass>dds.cs.mid</NodeClass>
                    <ConnectString>mongodb://root:****@dds-bp11483712c1****-cs1730-pub.m
ongodb.rds.aliyuncs.com:3717</ConnectString>
                    <Port>3717</Port>
                    <NodeStorage>20</NodeStorage>
                    <MaxConnections>8000</MaxConnections>
                    <MaxIOPS>8000</MaxIOPS>
                </ConfigserverAttribute>
            </ConfigserverList>
            <!-- Tag list -->
            <Tags>
                <Tag>
                    <Key>test</Key>
                    <Value>api</Value>
                </Tag>
            </Tags>
        </DBInstance>
        <!-- Example: Replica set instance structure (simplified to show differences) -
```

`->`

```xml
        <DBInstance>
            <DBInstanceId>dds-replicate-id****</DBInstanceId>
            <DBInstanceType>replicate</DBInstanceType>
            <ReplicaSetName>test</ReplicaSetName>
            <CpuType>intel</CpuType>
            <!-- Replica set specific: ReplicaSets list -->
            <ReplicaSets>
                <ReplicaSet>
                    <ReplicaSetRole>Primary</ReplicaSetRole>
                    <ConnectionDomain>dds-replicate-
id****.mongodb.rds.aliyuncs.com</ConnectionDomain>
                    <ConnectionPort>3717</ConnectionPort>
                    <IPAddress>192.168.1.xxx</IPAddress>
                    <IPAddressV6>2001:0db8:85a3:0000:0000:8a2e:0370:xxxx</IPAddressV6>
                    <IPVersion>IPv4v6</IPVersion>
                    <NetworkType>VPC</NetworkType>
                    <VPCId>vpc-bp1jk5vwkcri27qme****</VPCId>
                    <VSwitchId>vsw-bp1oo2a7isyrb8igf****</VSwitchId>
                    <VPCCloudInstanceId>vpc-bp1jk5vwkcri27qme****</VPCCloudInstanceId>
                </ReplicaSet>
            </ReplicaSets>
        </DBInstance>
    </DBInstances>
```

`JSON` format

```json
{
    "RequestId": "C373EED9-5125-4DD9-89DB-FB1ECD2C2B4F",
    "DBInstances": {
        "DBInstance": [
            {
                "DBInstanceId": "dds-bp11483712c1****",
                "DBInstanceDescription": "ceshi",
                "DBInstanceClass": "dds.mongo.mid",
                "DBInstanceStorage": 10,
                "DBInstanceType": "sharding",
                "Engine": "MongoDB",
                "EngineVersion": "4.4",
                "ChargeType": "PostPaid",
                "DBInstanceStatus": "Running",
                "CreationTime": "2022-08-21T05:10:00Z",
                "ExpireTime": "",
                "RegionId": "cn-qingdao-env17-d01",
                "ZoneId": "cn-qingdao-ft154e-amtest154001-a",
                "NetworkType": "VPC",
                "VPCId": "vpc-bp1n3i15v90el48nx****",
                "VSwitchId": "vsw-bp1n3i15v90el48nx****",
                "VPCCloudInstanceIds": "s-bp1d8c262a158****",
                "MaxConnections": 500,
                "MaxIOPS": 1000,
                "MaintainStartTime": "02:00Z",
                "MaintainEndTime": "03:00Z",
                "LockMode": "Unlock",
                "DBInstanceReleaseProtection": false,
                "CurrentKernelVersion": "mongodb_20180914_1.1.5",
                "StorageEngine": "WiredTiger",
                "ProtocolType": "mongodb",
                "ReadonlyReplicas": "0",
                "ReplicationFactor": "3",
                "ResourceGroupId": "rg-a7qme****",
                "KindCode": "0",
                "LastDowngradeTime": "2022-08-28",
                "ReplacateId": "bls-mgs****",
                "VpcAuthMode": "Close",
                "CpuType": "intel",
                "MongosList": {
                    "MongosAttribute": [
                        {
                            "NodeId": "s-bp1d8c262a158****",
                            "NodeDescription": "mongos1",
                            "NodeClass": "dds.mongos.mid",
                            "ConnectSting": "s-
bp1d8c262a158****.mongodb.rds.aliyuncs.com",
                            "Port": 3717,
                            "MaxConnections": 1000,
                            "MaxIOPS": 800,
```

a

```json
OS:800,
                            "VPCId": "vpc-bp1n3i15v90el48nx****",
                            "VSwitchId": "vsw-bp1n3i15v90el48nx****",
                            "VpcCloudInstanceId": "s-bp1d8c262a158****"
                        }
```

]

```json
                },
                "ShardList": {
                    "ShardAttribute": [
                        {
                            "NodeId": "d-bp16e09d9c5d****",
                            "NodeDescription": "testshard",
                            "NodeClass": "dds.shard.mid",
                            "ConnectString": "d-
bp1af0680a9c6d3****.mongodb.rds.aliyuncs.com",
                            "Port": 3717,
                            "NodeStorage": 10,
                            "MaxConnections": 8000,
                            "MaxIOPS": 8000
                        }
```

]

```json
                },
                "ConfigserverList": {
                    "ConfigserverAttribute": [
                        {
                            "NodeId": "dds-bp11483712c1****-cs",
                            "NodeDescription": "testConfigserver",
                            "NodeClass": "dds.cs.mid",
                            "ConnectString": "mongodb://root:****@dds-bp11483712c1****-c
s1730-pub.mongodb.rds.aliyuncs.com:3717",
                            "Port": 3717,
                            "NodeStorage": 20,
                            "MaxConnections": 8000,
                            "MaxIOPS": 8000
                        }
```

]

```json
                },
                "Tags": {
                    "Tag": [
                        {
                            "Key": "test",
                            "Value": "api"
                        }
```

]

```json
                }
            },
            {
                "DBInstanceId": "dds-replicate-id****",
                "DBInstanceType": "replicate",
                "ReplicaSetName": "test",
                "CpuType": "intel",
                "ReplicaSets": {
                    "ReplicaSet": [
                        {
                            "ReplicaSetRole": "Primary",
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRoleZo neInfo | The operation that you want to perform. Set the value to DescribeRoleZoneInfo. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 728B9A96-E262- 4AE5-915E- 3A51CCE2FDA9 | The ID of the request. |
| ZoneInfos | Array of ZoneInfo |  | An array that consists of information of nodes in the zone. |
| ZoneInfo |  |  |  |
| InsName | String | dds-bpxxxxxxxx | The ID of the node. |

```json
                            "ConnectionDomain": "dds-replicate-
id****.mongodb.rds.aliyuncs.com",
                            "ConnectionPort": "3717",
                            "IPAddress": "192.168.1.xxx",
                            "IPAddressV6": "2001:0db8:85a3:0000:0000:8a2e:0370:xxxx",
                            "IPVersion": "IPv4v6",
                            "NetworkType": "VPC",
                            "VPCId": "vpc-bp1jk5vwkcri27qme****",
                            "VSwitchId": "vsw-bp1oo2a7isyrb8igf****",
                            "VPCCloudInstanceId": "vpc-bp1jk5vwkcri27qme****"
                        }
```

]

```
                }
            }
```

]

```
    }
}
```

#### DescribeRoleZoneInfo

You can call this operation to view the roles and zones of nodes in an ApsaraDB for MongoDB instance.

**Request parameters**

**Response parameters**

| NodeType | String | normal | The type of the node. Valid values: normal configServer shard mongos Note Valid value for replica set instances: normal. Valid values for sharded cluster instances: configServer, shard, and mongos. |
|---|---|---|---|
| RoleId | String | 83xxxxx | The ID of the role. |
| RoleType | String | Primary | The role of the node. Valid values: Primary Secondary Hidden |
| ZoneId | String | cn-hangzhou-e | The zone ID. |

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeRoleZoneInfo &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <ZoneInfos>
      <ZoneInfo>
         <RoleType>Primary</RoleType>
         <NodeType>normal</NodeType>
         <InsName>dds-bpxxxxxxxx</InsName>
         <ZoneId>cn-hangzhou-e</ZoneId>
         <RoleId>83xxxxx</RoleId>
      </ZoneInfo>
      <ZoneInfo>
         <RoleType>Secondary</RoleType>
         <NodeType>normal</NodeType>
         <InsName>dds-bpxxxxxxxx</InsName>
         <ZoneId>cn-hangzhou-f</ZoneId>
         <RoleId>83xxxxx</RoleId>
      </ZoneInfo>
      <ZoneInfo>
         <RoleType>Hidden</RoleType>
         <NodeType>normal</NodeType>
         <InsName>dds-bpxxxxxxxx</InsName>
         <ZoneId>cn-hangzhou-b</ZoneId>
         <RoleId>83xxxxx</RoleId>
      </ZoneInfo>
   </ZoneInfos>
   <RequestId>728B9A96-E262-4AE5-915E-3A51CCE2FDA9</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RestartDBInstan ce | The operation that you want to perform. Set the value to RestartDBInstance. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

```json
{
 "ZoneInfos": {
  "ZoneInfo": [
   {
    "RoleType": "Primary",
    "NodeType": "normal",
    "InsName": "dds-bpxxxxxxxx",
    "ZoneId": "cn-hangzhou-e",
    "RoleId": "83xxxxx"
   },
   {
    "RoleType": "Secondary",
    "NodeType": "normal",
    "InsName": "dds-bpxxxxxxxx",
    "ZoneId": "cn-hangzhou-f",
    "RoleId": "83xxxxx"
   },
   {
    "RoleType": "Hidden",
    "NodeType": "normal",
    "InsName": "dds-bpxxxxxxxx",
    "ZoneId": "cn-hangzhou-b",
    "RoleId": "83xxxxx"
   }
```

]

```json
 },
 "RequestId": "728B9A96-E262-4AE5-915E-3A51CCE2FDA9"
}
```

### Instance management

#### RestartDBInstance

You can call this operation to restart an ApsaraDB for MongoDB instance. This operation can also be used to restart a shard or mongos node in a replica set instance.

**Request parameters**

| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard or mongos node in the sharded cluster instance. Note The sharded cluster instance will be restarted if this parameter is not specified. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 149C517D-B586- 47BE-A107- 8673E0ED77C6 | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eMaintainTime | The operation that you want to perform. Set the value to ModifyDBInstanceMaintainTime. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=RestartDBInstance &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>149C517D-B586-47BE-A107-8673E0ED77C6</RequestId>
```

`JSON` format

```json
{
 "RequestId": "149C517D-B586-47BE-A107-8673E0ED77C6"
}
```

#### ModifyDBInstanceMaintainTime

You can call this operation to modify the maintenance window of an ApsaraDB for MongoDB instance.

**Request parameters**

| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
|---|---|---|---|---|
| MaintainEndTim e | String | Yes | 02:00Z | The end time of the maintenance window. Specify the time in the HH:mmZ format. The time must be in UTC. Note The difference between the start time and end time must be one hour. For example, if MaintainStartTime is 01:00Z, MaintainEndTime must be 02:00Z. |
| MaintainStartTi me | String | Yes | 01:00Z | The start time of the maintenance window. Specify the time in the HH:mmZ format. The time must be in UTC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A9310426-C763- 42A2-A3AD- 70A8DA204531 | The ID of the request. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceMaintainTime &MaintainStartTime=01:00Z &MaintainEndTime=02:00Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>A9310426-C763-42A2-A3AD-70A8DA204531</RequestId>
```

`JSON` format

```json
{
 "RequestId": "A9310426-C763-42A2-A3AD-70A8DA204531"
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eDescription | The operation that you want to perform. Set the value to ModifyDBInstanceDescription. |
| DBInstanceDesc ription | String | Yes | testdata | The name of the instance. Note The name cannot start with http:// or https://. The name must start with a letter. It can contain letters, underscores ( ), hyphens _ (-), and digits. It must be 2 to 256 characters in length. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you want to modify the name of a shard or mongos node in a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard or mongos node in the sharded cluster instance. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 06F8F642-4009- 4FFC-80C4- 9D67DBF7B74E | The ID of the request. |

#### ModifyDBInstanceDescription

You can call this operation to change the name of an ApsaraDB for MongoDB instance.

**Request parameters**

**Response parameters**

Sample requests

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SwitchDBInstanc eHA | The operation that you want to perform. Set the value to SwitchDBInstanceHA. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard node in the sharded cluster instance. Note If you set the DBInstanceId parameter to the ID of a sharded cluster instance, you must specify this parameter. |

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceDescription &DBInstanceDescription=testdata &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>06F8F642-4009-4FFC-80C4-9D67DBF7B74E</RequestId>
```

`JSON` format

```json
{
 "RequestId": "06F8F642-4009-4FFC-80C4-9D67DBF7B74E"
}
```

#### SwitchDBInstanceHA

You can call this operation to switch between the primary and secondary nodes in an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation.

**Note**

On replica set instances, the switch is performed between primary and secondary instances. On sharded cluster instances, the switch is performed between primary and secondary shard nodes.

**Request parameters**

| RoleIds | String | No | 972xxxx,972xxx x | The IDs of the roles that you want to switch. You can call the DescribeRoleZoneInfo operation to view the IDs and information of roles of nodes. Note Separate role IDs with commas (,). If this parameter is not specified, the primary and secondary nodes are switched. If you set the DBInstanceId parameter to the ID of a sharded cluster instance, the roles to be switched must belong to one shard node. |
|---|---|---|---|---|
| SwitchMode | Integer | No | 0 | The time when roles of the primary and secondary nodes are switched. Valid values: 0: The roles are switched immediately. 1: The roles are switched during the maintenance period. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 26BD4E5F-BDB4- 47BA-B232- 413AA78CFA8F | The ID of the request. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=SwitchDBInstanceHA &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>26BD4E5F-BDB4-47BA-B232-413AA78CFA8F</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpgradeDBInsta nceEngineVersio n | The operation that you want to perform. Set the value to UpgradeDBInstanceEngineVersio n. |
| EngineVersion | String | Yes | 4.2 | The new database engine version of the instance. Valid values: 3.4, 4.0, and 4.2. Note The new database engine version must be later than the current version. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C4907B00-A208- 4E0C-A636- AA85140E406C | The ID of the request. |

```json
{
 "RequestId": "26BD4E5F-BDB4-47BA-B232-413AA78CFA8F"
}
```

#### UpgradeDBInstanceEngineVersion

You can call this operation to upgrade the database version of an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation.

**Note**

The available database versions are subject to the storage engine used by the instance. You can call the **DescribeAvailableEngineVersion** operation to view the available database versions. The database version cannot be downgraded after it is upgraded. The instance is automatically restarted for two to three times during the upgrade process. Make sure that you upgrade the instance during off-peak hours.

**Request parameters**

**Response parameters**

Sample requests

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpgradeDBInsta nceKernelVersio n | The operation that you want to perform. Set the value to UpgradeDBInstanceKernelVersio n. |
| DBInstanceId | String | No | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 27B9A130-7C4B- 40D9-84E8- 2FC081097AAC | The ID of the request. |

```
http(s)://mongodb.example.com/? Action=UpgradeDBInstanceEngineVersion &EngineVersion=4.0 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>C4907B00-A208-4E0C-A636-AA85140E406C</RequestId>
```

`JSON` format

```json
{
 "RequestId": "C4907B00-A208-4E0C-A636-AA85140E406C"
}
```

#### UpgradeDBInstanceKernelVersion

You can call this operation to upgrade the minor database version of an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation.

**Note**

The instance will be restarted once during the upgrade. Perform this operation during off-peak hours.

**Request parameters**

**Response parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eNetExpireTime | The operation that you want to perform. Set the value to ModifyDBInstanceNetExpireTime. |
| ClassicExpendEx piredDays | Integer | Yes | 30 | The retention period of the original classic network address. Valid values: 14, 30, 60, and 120. Unit: day. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| ConnectionStrin g | String | No | dds- bpxxxxxxxx.mon godb.rds.aliyunc s.com | The connection address of the instance |

Sample requests

```
http(s)://mongodb.example.com/? Action=UpgradeDBInstanceKernelVersion &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>27B9A130-7C4B-40D9-84E8-2FC081097AAC</RequestId>
```

`JSON` format

```json
{
 "RequestId": "27B9A130-7C4B-40D9-84E8-2FC081097AAC"
}
```

#### ModifyDBInstanceNetExpireTime

You can call this operation to extend the retention period of the classic network of an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: The instance must be running. The network of the instance is in hybrid access mode.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 459E7D5C-38DA- 4E14-9C82- 5B5AF693DBAB | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccount s | The operation that you want to perform. Set the value to DescribeAccounts. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceNetExpireTime &ClassicExpendExpiredDays=30 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>459E7D5C-38DA-4E14-9C82-5B5AF693DBAB</RequestId>
```

`JSON` format

```json
{
 "RequestId": "459E7D5C-38DA-4E14-9C82-5B5AF693DBAB"
}
```

### Account management

#### DescribeAccounts

You can call this operation to view the information of the database account of an ApsaraDB for MongoDB instance.

**Note**

This operation can display only the information of the root account.

**Request parameters**

| AccountName | String | No | root | The name of the account. Set the value to root. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Accounts | Array of Account |  | An array that consists of the information of accounts. |
| Account |  |  |  |
| AccountDescri ption | String | Administrator | The description of the account. |
| AccountName | String | root | The name of the account. |
| AccountStatus | String | Available | The status of the account. Unavailable Available |
| CharacterType | String | normal | The role of the account. Valid values: db: the shard node cs: the Configserver node mongos: the mongos node logic: the sharded cluster instance normal: the replica set instance |
| DBInstanceId | String | dds-bpxxxxxxxx | The name of the instance to which the account belongs. |
| RequestId | String | B562A65B-39AB- 4EE8-8635- 5A222054FB35 | The ID of the request. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAccounts &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetAccountPa ssword | The operation that you want to perform. Set the value to ResetAccountPassword. |
| AccountName | String | Yes | root | The account for which you want to reset the password. Set the value to root. |

```xml
   <Accounts>
      <Account>
         <AccountStatus>Available</AccountStatus>
         <AccountDescription>Administrator</AccountDescription>
         <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId>
         <AccountName>root</AccountName>
      </Account>
   </Accounts>
   <RequestId>A806B0FC-CFCC-48D8-8AEC-34C892806B40</RequestId>
```

`JSON` format

```json
{
    "Accounts": {
        "Account": [
            {
                "AccountStatus": "Available",
                "AccountDescription": "Administrator",
                "DBInstanceId": "dds-bpxxxxxxxx",
                "AccountName": "root"
            }
```

]

```json
    },
    "RequestId": "A806B0FC-CFCC-48D8-8AEC-34C892806B40"
}
```

#### ResetAccountPassword

You can call this operation to reset the password of the root account of an ApsaraDB for MongoDB instance.

**Note**

This operation can reset only the password of the root account of an instance.

**Request parameters**

| AccountPasswor d | String | Yes | Ali! 123456 | The new password. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! # $ % ^ & * ( ) + - = #$%^&*() +-= _ _ The password must be 8 to 32 characters in length. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

|  |  | ! # $ % ^ & |
|---|---|---|
|  | * ( ) + - = #$%^&*() +-= _ _ |  |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 06CBD06E-ABC9- 4121-AB93- 3C3820B3E7E6 | The ID of the request. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=ResetAccountPassword &AccountName=root &AccountPassword=Ali! 123456 &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>06CBD06E-ABC9-4121-AB93-3C3820B3E7E6</RequestId>
```

`JSON` format

```json
{
 "RequestId": "06CBD06E-ABC9-4121-AB93-3C3820B3E7E6"
}
```

#### ModifyAccountDescription

You can call this operation to modify the description of the root account of an ApsaraDB for MongoDB instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAccountD escription | The operation that you want to perform. Set the value to ModifyAccountDescription. |
| AccountDescripti on | String | Yes | superadmin | The description of the account. It cannot start with http:// or https://. The description must start with a letter. It must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and _ hyphens (-). |
| AccountName | String | Yes | root | The name of the account for which you want to modify the description. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 59DE9FC2-7B40- 45CF-9011- 7327A8A771A2 | The ID of the request. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyAccountDescription &AccountName=root &AccountDescription=superadmin &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>59DE9FC2-7B40-45CF-9011-7327A8A771A2</RequestId>
```

`JSON` format

| Parame ter Name | Typ e | Locati on | Require d | Example | Limit |
|---|---|---|---|---|---|
| Action | Strin g | Query | Yes | CreateAccount | The operation that you want to do. Set the value to CreateAccount. |
| DBInstanc eId | Strin g | Query | Yes | dds-ir4c9c4cfe26a894 | The ID of the instance. |
| AccountN ame | Strin g | Query | Yes | testxxx | The name of the account. |
| AccountPa ssword | Strin g | Query | Yes | Pw123xxxx | The password of the account. |
| AccountD escription | Strin g | Query | No. | test account | The description of the account. |
| Database Name | Strin g | Query | No. | db1 | The database name. |

| Parameter Name | Type | Examples | Description |
|---|---|---|---|
| RequestId | String | F8CA8312-530A- 413A-9129- F2BB32A8xxxx | The ID of the request. |

```json
{
 "RequestId": "59DE9FC2-7B40-45CF-9011-7327A8A771A2"
}
```

#### CreateAccount

Creates a database account for an ApsaraDB for MongoDB instance.

**Request header**

This interface uses common request headers without special request headers. See the public request parameters documentation.

**Response parameters**

Sample requests

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidAccountNam e.Malformed | InvalidAccountName.Malforme d | Specified parameter AccountName is not valid. |
| 400 | InvalidAccountPass word.Malformed | InvalidAccountPassword.Malfor med | Specified parameter AccountPassword is not valid. |
| 400 | InvalidAccountDesc ription.Malformed | InvalidAccountDescription.Malf ormed | Specified parameter AccountDescription is not valid. |
| 400 | InvalidAccountNam e.Format | InvalidAccountName.Malforme d | Specified parameter AccountName is not valid. |
| 404 | AccountLimitExcee ded | AccountLimitExceeded | AccountQuotaExceeded: Exceeding the allowed amount of account. |
| 400 | InvalidParameters. Format | InvalidParameters.Format | Specified parameter AccountName or AccountPassword not exist. |
| 403 | IncorrectAccountTy pe | IncorrectAccountType | Current account type does not support this operation. |
| 403 | InvalidDBName | InvalidDBName | The specified database name is not allowed. |
| 400 | InvalidAccountNam e.Duplicate | InvalidAccountName.Duplicate | Specified account name already exists in this instance. |

```
&DBInstanceId=dds-ir4c9c4cfe26a894 &AccountName=testxxx &AccountPassword= &Public request parameters
```

Sample success responses `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"F8CA8312-530A-413A-9129-F2BB32A8xxxx"
}
```

`XML` format

```xml
<RequestId>F8CA8312-530A-413A-9129-F2BB32A8xxxx</RequestId>
```

**Error code**

| psaraDB for | MongoDB |  | Developer Guide·API Referenc |
|---|---|---|---|

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidAccountNam e.Forbid | InvalidAccountName.Forbid | Specified Account Name is a keyword in DDS |
| 400 | InvalidParameters. Format | InvalidParameters.Format | The specified database does not exist. |
| 403 | IncorrectDBInstanc eCharacterType | IncorrectDBInstanceCharacter Type | Current DB Instance character type does not _ support this operation. |
| 403 | IncorrectDBInstanc eState | IncorrectDBInstanceState | Current DB instance state does not support this operation. |
| 403 | IncorrectDBInstanc eLockMode | IncorrectDBInstanceLockMode | Current DB instance lock mode does not support this operation. |
| 400 | InvalidAccountPass word.Malformed | IncorrectDBInstanceLockMode | Specified parameter AccountPassword is not valid. |
| 400 | InvalidAccountNam e.Malformed | InvalidAccountName.Malforme d | Specified parameter AccountName is not valid. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurit yGroupConfigur ation | The operation that you want to perform. Set the value to DescribeSecurityGroupConfigura tion. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|

### IP whitelists and security

**groups**

#### DescribeSecurityGroupConfiguration

You can call this operation to view ECS security groups to which an ApsaraDB for MongoDB instance is added.

**Request parameters**

**Response parameters**

| Items | Array of RdsEcsSecurit yGroupRel |  | The information list of the ECS security group. |
|---|---|---|---|
| RdsEcsSecurit yGroupRel |  |  |  |
| NetType | String | vpc | The network type of the ECS security group. Valid values: vpc classic |
| RegionId | String | cn-hangzhou | The region ID of the ECS security group. |
| SecurityGroupI d | String | sg-bpxxxxxxxx | The ID of the ECS security group. |
| RequestId | String | 3C4A2494-85C4- 45C5-93CF- 548DB3375193 | The ID of the request. |

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeSecurityGroupConfiguration &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Items>
    <RdsEcsSecurityGroupRel>
        <SecurityGroupId>sg-bpxxxxxxxx</SecurityGroupId>
        <RegionId>cn-hangzhou</RegionId>
        <NetType>classic</NetType>
    </RdsEcsSecurityGroupRel>
</Items> <RequestId>D18F5B88-ACA6-470E-9493-384412EDD902</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurit yIps | The operation that you want to perform. Set the value to DescribeSecurityIps. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| SecurityIpGrou ps | Array of SecurityIpGrou p |  | The list of IP allowlist groups. |
| SecurityIpGrou p |  |  |  |
| SecurityIpGrou pAttribute | String | hidden | The attribute of the IP allowlist group. The default value is empty. |
| SecurityIpGrou pName | String | default | The name of the group. |

```json
{
 "Items": {
  "RdsEcsSecurityGroupRel": [
   {
    "SecurityGroupId": "sg-bpxxxxxxxx",
    "RegionId": "cn-hangzhou",
    "NetType": "classic"
   }
```

]

```json
 },
 "RequestId": "D18F5B88-ACA6-470E-9493-384412EDD902"
}
```

#### DescribeSecurityIps

Call the DescribeSecurityIps operation to query the IP whitelist of a MongoDB instance.

**Request parameters**

**Response parameters**

| SecurityIpList | String | 47.xxx.xxx.xx,100.x xx.xxx.0/24 | The IP allowlist contained in the group. |
|---|---|---|---|
| SecurityIps | String | 47.xxx.xxx.xx,100.x xx.xxx.0/24 | The IP allowlist contained in the default group. |
| RequestId | String | FC724D23-2962- 479E-ABB1- 606C935AE7FD | The ID of the request. |
| SecurityIPType | String | ipv4 | The type of IP address. IPv4 address IPv6 address |
| WhitelistNetTy pe | String | mix | The network type of the allowlist. |
| CreateTime | String | "2026-05- 06T02:49:06Z" | The time when the allowlist was created. |

Sample requests

```
http(s)://mongodb.example.com/?Action=DescribeSecurityIps &DBInstanceId=dds-bpxxxxxxxx &<Common Request Parameter>
```

Sample success responses `XML` format

```xml
<Response>
    <eagleEyeTraceId>0ab07e0817791996299386818e002d</eagleEyeTraceId>
    <SecurityIps>::1</SecurityIps>
    <asapiSuccess>true</asapiSuccess>
    <asapiRequestId>24F37C1B-6D50-4541-8E62-777A8FCFBA16</asapiRequestId>
    <RequestId>24F37C1B-6D50-4541-8E62-777A8FCFBA16</RequestId>
    <SecurityIpGroups>
        <SecurityIpGroup>
            <SecurityIpGroupAttribute></SecurityIpGroupAttribute>
            <SecurityIPType>ipv4</SecurityIPType>
            <SecurityIpList>127.0.0.1/0</SecurityIpList>
            <CreateTime>2026-05-18T06:45:48Z</CreateTime>
            <WhitelistNetType>mix</WhitelistNetType>
            <SecurityIpGroupName>default</SecurityIpGroupName>
        </SecurityIpGroup>
        <SecurityIpGroup>
            <SecurityIpGroupAttribute></SecurityIpGroupAttribute>
            <SecurityIPType>ipv6</SecurityIPType>
            <SecurityIpList>::1</SecurityIpList>
            <CreateTime>2026-05-18T06:45:48Z</CreateTime>
            <WhitelistNetType>mix</WhitelistNetType>
            <SecurityIpGroupName>default</SecurityIpGroupName>
        </SecurityIpGroup>
    </SecurityIpGroups>
</Response>
```

`JSON` format

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | Quer y | Yes | ModifySecurityIps | The operation that you want to perform. Set the value to ModifySecurityIps. |
| DBInstanc eId | Strin g | Quer y | Yes | dds-bpxxxxxxxx | The ID of the instance. |

```json
{
  "eagleEyeTraceId": "0ab07e0817791996299386818e002d",
  "SecurityIps": "::1",
  "asapiSuccess": true,
  "asapiRequestId": "24F37C1B-6D50-4541-8E62-777A8FCFBA16",
  "RequestId": "24F37C1B-6D50-4541-8E62-777A8FCFBA16",
  "SecurityIpGroups": {
    "SecurityIpGroup": [
      {
        "SecurityIpGroupAttribute": "",
        "SecurityIPType": "ipv4",
        "SecurityIpList": "127.0.0.1/0",
        "CreateTime": "2026-05-18T06:45:48Z",
        "WhitelistNetType": "mix",
        "SecurityIpGroupName": "default"
      },
      {
        "SecurityIpGroupAttribute": "",
        "SecurityIPType": "ipv6",
        "SecurityIpList": "::1",
        "CreateTime": "2026-05-18T06:45:48Z",
        "WhitelistNetType": "mix",
        "SecurityIpGroupName": "default"
      }
```

]

```
  }
}
```

#### ModifySecurityIps

Call the ModifySecurityIps operation to modify the IP whitelist of a MongoDB instance.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| SecurityIps | Strin g | Quer y | Yes | 10.23.12.24/24,10.22.22. 22 | The IP addresses in the IP whitelist group. Separate multiple IP addresses with commas (,). You can specify up to 1,000 unique IP addresses. The following formats are supported: IP address, such as 10.23.12.24 CIDR block, such as 10.23.12.24/24, where /24 indicates the prefix length. The prefix length ranges from 1 to 32. |
|---|---|---|---|---|---|
| ModifyMod e | Strin g | Quer y | No | Append | The modification mode. Valid values: Cover: Overwrites the original whitelist. Append: Appends entries to the whitelist. Delete: Deletes the whitelist. Default value: Cover. |
| SecurityIp GroupNam e | Strin g | Quer y | No | allowserver | The name of the IP whitelist group to be modified. Default value: default. |
| SecurityIp GroupAttri bute | Strin g | Quer y | No | test | The attribute of the whitelist group. The value can contain uppercase letters, lowercase letters, and digits. The maximum length is 120 characters. Default value: empty string |
| SecurityIP Type | Strin g | Quer y | No | ipv4 | The IP version. Default value: ipv4. Valid values: ipv4 ipv6 |

| Parameter | Type | Example | Description |
|---|---|---|---|

**Response parameters**

| RequestId | String | 61B05CCF-EBAB- 4BF3-BA67- D77256A721E2 | The ID of the request. |
|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceTDEInfo | The operation that you want to perform. Set the value to DescribeDBInstanceTDEInfo. |

Sample requests

```
&DBInstanceId=dds-bpxxxxxxxx &SecurityIps=10.23.12.24/24,10.22.22.22 &Common request parameters
```

Sample success responses `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"61B05CCF-EBAB-4BF3-BA67-D77256A721E2"
}
```

`XML` format

```xml
<RequestId>61B05CCF-EBAB-4BF3-BA67-D77256A721E2</RequestId>
```

### Key management

#### DescribeDBInstanceTDEInfo

You can call this operation to view whether TDE is enabled for an ApsaraDB for MongoDB instance. Before you call this operation, make sure that the following requirements are met: A replica set or sharded cluster instance is used. The storage engine of the instance is WiredTiger. The database engine version of the instance is 4.0 or 4.2. If the database engine version of your instance is earlier than 4.0, you can call the **UpgradeDBInstanceEngineVersion** operation to upgrade the database engine.

**Request parameters**

| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F4DD0E29-361B- 42F2-9301- B0048CCCE5D6 | The ID of the request. |
| TDEStatus | String | enabled | The TDE status. Valid values: enabled disabled |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeDBInstanceTDEInfo &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TDEStatus>enabled</TDEStatus> <RequestId>F4DD0E29-361B-42F2-9301-B0048CCCE5D6</RequestId>
```

`JSON` format

```json
{
    "TDEStatus":"enabled",
    "RequestId":"F4DD0E29-361B-42F2-9301-B0048CCCE5D6"
}
```

#### ModifyDBInstanceTDE

You can call this operation to modify the transparent data encryption (TDE) status of an ApsaraDB for MongoDB instance. Before data files are written to disks, transparent data encryption (TDE) encrypts the data files. When data files are loaded from disks to the memory, TDE decrypts the data files.

**Note**

After TDE is enabled, it cannot be disabled. Before you call this operation, make sure that the following requirements are met: A replica set or sharded cluster instance is used. The storage engine of the instance is WiredTiger. The database engine version of the instance is 4.0 or 4.2. If the database engine version is

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eTDE | The operation that you want to perform. Set the value to ModifyDBInstanceTDE. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| TDEStatus | String | Yes | enabled | The TDE status. Set the value to Enabled. Note After TDE is enabled, it cannot be disabled. Proceed with caution. |
| EncryptorName | String | No | aes-256-cbc | The encryption method. Set the value to aes-256-cbc. Note This parameter is valid only when you set the TEDStatus parameter to enabled. |
| EncryptionKey | String | No | 749c1df7-xxxx- xxxx-xxxx- xxxxxxxxxxxx | The custom key. |

earlier than 4.0, you can call the **UpgradeDBInstanceEngineVersion** operation to upgrade the database engine.

**Request parameters**

| RoleARN | String |  |  |  | The ARN of the role. It is in the format of acs:ram::$accountID:role/$roleN ame . Note $accountID : indicates the ID of the Alibaba Cloud account that owns the RAM role. To view the account ID, log on to the Alibaba Cloud Management Console, move your pointer over your profile picture in the upper-right corner, and then click Security Settings. $roleName : indicates the name of the RAM role. To view the RAM role name, perform the following steps: Log on to the RAM console. In the left-side navigation pane, click RAM Roles. In the RAM Role Name column on the page that appears, you can view the name of the RAM role. |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | acs:ram::$accountID:role/$roleN |  |
|  |  |  |  |  | ame |  |  |
|  |  |  | No | acs:ram::12345 6789012****:rol e/adminrole |  |  |  |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 434D7127-6229- 4355-BA50- 7A3685A725DF | The ID of the request. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyDBInstanceTDE &DBInstanceId=dds-bpxxxxxxxx &TDEStatus=enabled &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>434D7127-6229-4355-BA50-7A3685A725DF</RequestId>
```

`JSON` format

```json
{
 "RequestId": "434D7127-6229-4355-BA50-7A3685A725DF"
}
```

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectDBInstanc eState | Current DB instance state does not support this operation. | The error message returned because the operation is not supported while the instance is in its current state. Check whether the specified parameters are correct. |
| 403 | IncorrectDBInstanc eLockMode | Current DB instance lock mode does not support this operation. | The error message returned because the instance is locked. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDBInstanc eSSL | The operation that you want to perform. Set the value to ModifyDBInstanceSSL. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

**Error codes**

### SSL encryption

#### ModifyDBInstanceSSL

Call the ModifyDBInstanceSSL operation to modify the Secure Sockets Layer (SSL) configuration of a MongoDB instance. When you call this operation, the instance must meet the following conditions: The instance is in the running state. The instance type is a replica set instance. The database version of the instance is 3.4, 4.0, or 4.2.

**Note**

The instance restarts once during the process of enabling, updating, or disabling SSL. We recommend that you perform these operations during off-peak hours.

**Request parameters**

| SSLAction | String | Yes | Open | The operation to perform on SSL encryption. Valid values: Open: Enable SSL encryption. Close: Disable SSL encryption. Update: Update the SSL certificate. |
|---|---|---|---|---|
| ConfigMode | String | No | free | The configuration mode. Valid values: simple: simplified mode advanced: advanced mode Note This parameter is supported only for MongoDB 7.0 and later. |
| CertSource | String | Yes | cloud | The source of the certificate. This parameter identifies the certificate authority or type of source for the current SSL certificate. Default value: cloud. Valid values: cloud and custom. The custom mode is not supported currently. |
| ConnectionStrin g | String | Yes | "pc- xxxxx.redis.rds.a liyuncs.com:637 9" | The protected connection string. Note This parameter is supported only for MongoDB 7.0 and later. |
| TLSMode | String | No | required | The Transport Layer Security (TLS) encryption mode. This parameter defines the server's policy for requiring encrypted client connections. prefer: prefer encryption. Clients can choose whether to encrypt. If the client supports encryption, the system enforces it; otherwise, plaintext connections are allowed. required: enforce encryption. The system rejects all unencrypted connection requests. Clients must provide a valid certificate. Note This parameter is supported only for MongoDB 7.0 and later. |

| MinTLSVersion | String | No | TLSv1.2 | The minimum TLS version that the instance supports. This parameter specifies the minimum TLS protocol version allowed for establishing secure connections. Valid values: TLSv1.0, TLSv1.1, TLSv1.2, and TLSv1.3. Note This parameter is supported only for MongoDB 7.0 and later. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6D806B11-078F- 4154-BF9F- 844F56D08964 | The ID of the request. |

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/?Action=ModifyDBInstanceSSL &DBInstanceId=dds-bpxxxxxxxx &SSLAction=Open &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>6D806B11-078F-4154-BF9F-844F56D08964</RequestId>
```

`JSON` format

```json
{
 "RequestId": "6D806B11-078F-4154-BF9F-844F56D08964"
}
```

**Error codes**

| 403 | IncorrectDBInstanc eState | Current DB instance state does not support this operation. | The instance state does not support this operation. Check whether the input parameters are correct. |
|---|---|---|---|
| 403 | IncorrectDBInstanc eLockMode | Current DB instance lock mode does not support this operation. | The instance is locked. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta nceSSL | The operation that you want to perform. Set the value to DescribeDBInstanceSSL. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| SSLExpiredTim e | String | 2020-03- 11T02:28:25Z | The expiration time of the SSL certificate. The time follows the yyyy-MM- ddTHH:mm:ssZ format (UTC). |
| RequestId | String | 36BB1BC2-789C- 4BBA-A519- C5B388E4B0D4 | The ID of the request. |
| SSLStatus | String | Open | The status of the SSL feature. Open: The SSL feature is enabled. Closed: The SSL feature is disabled. |

#### DescribeDBInstanceSSL

Call the DescribeDBInstanceSSL operation to query the Secure Sockets Layer (SSL) settings of an ApsaraDB for MongoDB instance. When you call this operation, the instance must meet the following conditions: The instance is in the running state. The instance type is a replica set instance.

**Request parameters**

**Response parameters**

| CertCommonN ame | String | dds- bpxxxxxxxx.mongo db.rds.example.co m | The name of the SSL certificate. |
|---|---|---|---|
| ConnectionStri ng | String | pc- xxxxx.redis.rds.aliy uncs.com:6379 | The protected connection string: the database endpoint after SSL/Transport Layer Security (TLS) encryption is enabled. Clients must use this address and configure a valid certificate to establish a secure connection. |
| SSLEnabled | Boolean | true | The TLS encryption status: indicates whether SSL encryption is currently enabled for the instance. true: enabled false: disabled |
| TLSMode | String | required | The TLS encryption mode: defines the server's policy for requiring encrypted client connections. prefer: Prefer encryption. Allows clients to choose whether to encrypt. If the client supports encryption, the server enforces it; otherwise, plaintext connections are allowed. required: Require encryption. Rejects all unencrypted connection requests. Clients must present a valid certificate. Note This parameter returns a value only if you set a value for it and your instance runs MongoDB 7 or later. |

| MinTLSVersion | String | TLSv1.2 | The minimum supported TLS version: the minimum TLS protocol version that the instance allows for establishing connections, ensuring security. Common values: TLSv1.0, TLSv1.1, TLSv1.2, and TLSv1.3. Note This parameter returns a value only if you set a value for it and your instance runs MongoDB 7 or later. |
|---|---|---|---|
| CertSource | String | cloud | The source of the certificate: identifies the issuing authority or type of the current SSL certificate. Valid values: cloud and custom Note This parameter returns a value only if you set a value for it and your instance runs MongoDB 7 or later. |

Sample requests

```
http(s)://mongodb.example.com/?Action=DescribeDBInstanceSSL &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
    <RequestId>36BB1BC2-789C-4BBA-A519-C5B388E4B0D4</RequestId>
    <SSLStatus>Open</SSLStatus>
    <SSLEnabled>true</SSLEnabled>
    <SSLExpiredTime>2020-03-11T02:28:25Z</SSLExpiredTime>
    <CertCommonName>dds-bpxxxxxxxx.mongodb.rds.example.com</CertCommonName>
    <ConnectionString>pc-xxxxx.redis.rds.aliyuncs.com:6379</ConnectionString>
    <TLSMode>required</TLSMode>
    <MinTLSVersion>TLSv1.2</MinTLSVersion>
    <CertSource>aliyun</CertSource>
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditRe cords | The operation that you want to perform. Set the value to DescribeAuditRecords. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| EndTime | String | Yes | 2019-03- 13T13:11:14Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. |
| StartTime | String | Yes | 2019-03- 13T12:11:14Z | The beginning of the time range to query. Specify the time in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. |

`JSON` format

```json
{
    "RequestId": "36BB1BC2-789C-4BBA-A519-C5B388E4B0D4",
    "SSLStatus": "Open",
    "SSLEnabled": true,
    "SSLExpiredTime": "2020-03-11T02:28:25Z",
    "CertCommonName": "dds-bpxxxxxxxx.mongodb.rds.example.com",
    "ConnectionString": "pc-xxxxx.redis.rds.aliyuncs.com:6379",
    "TLSMode": "required",
    "MinTLSVersion": "TLSv1.2",
    "CertSource": "aliyun"
}
```

### Audit logs

#### DescribeAuditRecords

You can call this operation to view the audit logs of ApsaraDB for MongoDB instances. When you call this operation, ensure that the audit log feature of the instance is enabled. Otherwise, the operation returns an empty audit log.

**Request parameters**

| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the sharded cluster instance. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
|---|---|---|---|---|
| Database | String | No | testdatabase | The name of the database. If you do not specify this parameter, this operation returns audit logs of all databases. |
| User | String | No | root | The account of the database. If you do not specify this parameter, this operation returns audit logs of all accounts. |
| Form | String | No | Stream | The form of the audit log entry returend. Valid values: File: returns a log file. If this parameter is set to File, only common parameters are returned. In this case, you must call the DescribeAuditFiles operation to view the download URL of the log file. Stream: returns data streams. Default value: Stream. |
| QueryKeywords | String | No | slow | The keywords used for a query. Separate multiple keywords with spaces. You can specify a maximum of 10 keywords. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| OrderType | String | No | asc | The order of time in which the log entries to return are sorted. Valid values: asc: The log entries are sorted by time in ascending order. desc: The log entries are sorted by time in descending order. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Items | Array of SQLRecord |  | An array that consists of the information of the audit log entries. |
| SQLRecord |  |  |  |
| AccountName | String | root | The account of the database. |
| DBName | String | test123 | The name of the database. |
| ExecuteTime | String | 2019-03- 11T03:30:27Z | The time when the statement was executed. The time is in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| HostAddress | String | 11.xxx.xxx.xxx | The IP address of the client. |
| ReturnRowCou nts | Long | 2 | The number of entries returned. |
| Syntax | String | { \"atype\" : \"createCollection\" , \"param\" : { \"ns\" : \"123.test1\" }, \"result\": \"OK\" } | The statement that was executed. |
| TableName | String | C1 | The name of the collection. |
| ThreadID | String | 140682188297984 | The ID of the thread. |
| TotalExecution Times | Long | 700 | The duration of the statement execution. Unit: microseconds. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 30 | The maximum number of records on the current page. |
| RequestId | String | 3278BEB8-503B- 4E46-8F7E- D26E040C9769 | The ID of the request. |
| TotalRecordCo unt | Integer | 40 | The total number of entries. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAuditRecords &StartTime=2019-03-13T12:11:14Z &EndTime=2019-03-13T13:11:14Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalRecordCount>40</TotalRecordCount> <PageRecordCount>30</PageRecordCount> <RequestId>3278BEB8-503B-4E46-8F7E-D26E040C9769</RequestId> <PageNumber>1</PageNumber> <Items>
    <TableName>C1</TableName>
    <ThreadID>140682188297984</ThreadID>
    <ExecuteTime>2019-03-11T03:30:27Z</ExecuteTime>
    <ReturnRowCounts>2</ReturnRowCounts>
    <DBName>test123</DBName>
    <TotalExecutionTimes>700</TotalExecutionTimes>
    <Syntax>{ \"atype\" : \"createCollection\", \"param\" : { \"ns\" : \"123.test1\" },
\"result\": \"OK\" }</Syntax>
    <HostAddress>11.xxx.xxx.xxx</HostAddress>
    <AccountName>root</AccountName>
</Items>
```

`JSON` format

```json
{
    "TotalRecordCount":"40",
    "PageRecordCount":"30",
    "RequestId":"3278BEB8-503B-4E46-8F7E-D26E040C9769",
    "PageNumber":"1",
    "Items":[
        {
            "TableName":"C1",
            "ThreadID":"140682188297984",
            "ExecuteTime":"2019-03-11T03:30:27Z",
            "ReturnRowCounts":"2",
            "DBName":"test123",
            "TotalExecutionTimes":"700",
            "Syntax":"{ \\\"atype\\\" : \\\"createCollection\\\", \\\"param\\\" : { \\\"
ns\\\" : \\\"123.test1\\\" }, \\\"result\\\": \\\"OK\\\" }",
            "HostAddress":"11.xxx.xxx.xxx",
            "AccountName":"root"
        }
```

]

```
}
```

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidEndTime.For mat | Specified end time is not valid. | The error message returned when the end time is invalid. Check the format of the specified time. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditFil es | The operation that you want to perform. Set the value to DescribeAuditFiles. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the specified cluster instance. Note If you do not specify this parameter, the audit logs of all mongos and shard nodes will be returned. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the instance. |
| Items | Array of LogFile |  | An array that consists of the information of audit log files. |

**Error codes**

#### DescribeAuditFiles

You can call this operation to view the audit log files of an ApsaraDB for MongoDB instance.

**Request parameters**

**Response parameters**

| LogFile |  |  |  |
|---|---|---|---|
| FileID | Integer | 406505 | The ID of the file. |
| LogDownloadU RL | String | http://xxxxxxxx.oss -cn- hangzhou.aliyuncs. com/custinsxxxxxx /custinsxxxxxx xxx _ xxx.csv | The download URL for audit log files. Note If the download URL is unavailable, this parameter is empty. |
| LogEndTime | String | 2019-03- 12T09:23:15Z | The end of the time range for the audit log files displayed. The time is in the yyyy- MM-ddTHH:mmZ format. The time is displayed in UTC. |
| LogSize | Long | 98 | The size of the audit log file. Unit: bytes. |
| LogStartTime | String | 2019-03- 11T08:19:29Z | The beginning of the time range for the audit log files displayed. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| LogStatus | String | Success | The status of the audit log file. Success: The audit log file is archived. Failed: The audit log file failed to be archived. Generating: The audit log file is being archived. Initializing: Archiving is not started. |
| PageNumber | Integer | 1 | The page number of the page returned. |
| PageRecordCo unt | Integer | 1 | The number of entries on the current page. |
| RequestId | String | F8CA8312-530A- 413A-9129- F2BB32A8D404 | The ID of the request. |
| TotalRecordCo unt | Integer | 1 | The total number of entries. |

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAuditFiles &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidDBInstanceC lass.NotFound | Specified DB instance class is not found. | The error message returned because the specified instance type does not exist. Verify the specified instance type. |

Sample success responses `XML` format

```xml
   <Items>
      <LogFile>
         <LogStartTime>2019-03-11T08:19:29Z</LogStartTime>
         <LogEndTime>2019-03-12T09:23:15Z</LogEndTime>
         <LogStatus>Success</LogStatus>
         <FileID>406505</FileID>
         <LogDownloadURL>http://xxxxxxxx.oss-cn-
hangzhou.aliyuncs.com/custinsxxxxxx/custinsxxxxxx_xxxxxx.csv</LogDownloadURL>
         <LogSize>98</LogSize>
      </LogFile>
   </Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>1</TotalRecordCount>
   <RequestId>F8CA8312-530A-413A-9129-F2BB32A8D404</RequestId>
   <PageRecordCount>1</PageRecordCount>
```

`JSON` format

```json
{
 "Items": {
  "LogFile": [
   {
    "LogStartTime": "2019-03-11T08:19:29Z",
    "LogEndTime": "2019-03-12T09:23:15Z",
    "LogStatus": "Success",
    "FileID": 406505,
    "LogDownloadURL": "http://xxxxxxxx.oss-cn-
hangzhou.aliyuncs.com/custinsxxxxxx/custinsxxxxxx_xxxxxx.csv",
    "LogSize": 98
   }
```

]

```json
 },
 "PageNumber": 1,
 "TotalRecordCount": 1,
 "RequestId": "F8CA8312-530A-413A-9129-F2BB32A8D404",
 "PageRecordCount": 1
}
```

**Error codes**

| 403 | IncorrectDBInstanc eType | Current DB instance type does not support this operation. | The error message returned because the operation is not supported by the current instance type. |
|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditPo licy | The operation that you want to perform. Set the value to DescribeAuditPolicy. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogAuditStatu s | String | Enable | The status of the log audit feature. Valid values: Enable Disabled Default value: Disabled. |
| RequestId | String | 111E7B16-0A87- 4CBA-B271- F34AD61E099F | The ID of the request. |

#### DescribeAuditPolicy

You can call this operation to view whether the log audit feature is enabled for an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation.

**Request parameters**

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeAuditPolicy &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAuditLogF ilter | The operation that you want to perform. Set the value to ModifyAuditLogFilter. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| Filter | String | Yes | insert,query,upd ate,delete | The type of the audit log entries to be collected. Valid values: admin: O&M and management operations slow: slow queries query: query operations insert: insert operations update: update operations delete: delete operations command: protocol commands such as the aggregate method |
| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary |

```xml
   <LogAuditStatus>Enable</LogAuditStatus>
   <RequestId>111E7B16-0A87-4CBA-B271-F34AD61E099F</RequestId>
```

`JSON` format

```json
{
 "LogAuditStatus": "Enable",
 "RequestId": "111E7B16-0A87-4CBA-B271-F34AD61E099F"
}
```

#### ModifyAuditLogFilter

You can call this operation to modify the type of audit logs to be collected from ApsaraDB for MongoDB instances. The instance must be in the running state when you call this operation. This operation is applicable only to replica set instances, but not to sharded cluster instances.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E209BE2B-F264- 4B9D-81F6- A5A5FB1FBF28 | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAuditLo gFilter | The operation that you want to perform. Set the value to DescribeAuditLogFilter. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyAuditLogFilter &Filter=insert,query,update,delete &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>E209BE2B-F264-4B9D-81F6-A5A5FB1FBF28</RequestId>
```

`JSON` format

```json
{
 "RequestId": "E209BE2B-F264-4B9D-81F6-A5A5FB1FBF28"
}
```

#### DescribeAuditLogFilter

You can call this operation to view the types of audit logs collected from ApsaraDB for MongoDB instances. The instance must be in the running state when you call this operation.

**Note**

This operation is applicable only to replica set instances, but not to sharded cluster instances.

**Request parameters**

| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Filter | String | admin,slow,insert,q uery,update,delete ,command | The type of the audit log entries. Valid values: admin: O&M and management operations slow: slow queries query: query operations insert: insert operations update: update operations delete: delete operations command: protocol commands such as the aggregate method |
| RequestId | String | D7C8BA0C-9350- 487D-9B70- D69AF27FB1EB | The ID of the request. |
| RoleType | String | primary | The role of the node. |

**Response parameters**

Sample requests

```
http(s)://mongodb.aliyuncs.com/? Action=DescribeAuditLogFilter &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <Filter>admin,slow,insert,query,update,delete,command</Filter>
   <RoleType></RoleType>
   <RequestId>D7C8BA0C-9350-487D-9B70-D69AF27FB1EB</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAuditPolic y | The operation that you want to perform. Set the value to ModifyAuditPolicy. |
| AuditStatus | String | Yes | enable | The status of the audit log feature. Valid values: enable disabled |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| StoragePeriod | Integer | No | 30 | The retention period of audit logs. Unit: day. Valid values: 1 to 30. Default value: 30. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DC04D812-F18D- 4568-9B88- F260D9590116 | The ID of the request. |

```json
{
 "Filter": "admin,slow,insert,query,update,delete,command",
 "RoleType": "",
 "RequestId": "D7C8BA0C-9350-487D-9B70-D69AF27FB1EB"
}
```

#### ModifyAuditPolicy

You can call this operation to enable or disable the audit log feature or set the retention period of audit logs for an ApsaraDB for MongoDB instance.

**Request parameters**

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyAuditPolicy &AuditStatus=enable &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

| Paramete r | Type | Requ ired | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSlowLo gRecords | The operation that you want to perform. Set the value to DescribeSlowLogRecords. |
| StartTime | String | Yes | 2022-09- 05T12:10Z | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm.ssZ format. The time must be in UTC. Note This parameter specifies the time when the slow query is executed, rather than the time when the slow query is logged. |
| EndTime | String | Yes | 2022-09- 06T12:10Z | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm.ssZ format. The time must be in UTC. Note The end time must be later than the start time. The end time must be within 24 hours from the start time. Otherwise, the query fails. |

```xml
   <RequestId>DC04D812-F18D-4568-9B88-F260D9590116</RequestId>
```

`JSON` format

```json
{
 "RequestId": "DC04D812-F18D-4568-9B88-F260D9590116"
}
```

### Log management

#### DescribeSlowLogRecords

Queries the slow query logs of an ApsaraDB for MongoDB instance within a specific period of time.

**Request parameters**

| DBInstanc eId | String | Yes | dds- bp1366caac83* *** | The instance ID. Note You can call the DescribeDBInstanceAttribute operation to query the instance ID. If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
|---|---|---|---|---|
| NodeId | String | No | d- bp18b06ebc21* *** | The ID of the shard node. Note You can call the DescribeDBInstanceAttribute operation to query the ID of the shard node. This parameter is available only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
| DBName | String | No | admin | The name of the database. Note If you do not specify this parameter, the slow query logs of all databases are queried. |
| PageSize | Integer | No | 30 | The number of entries per page. Valid values: 30 to 100. Default value: 30. |
| PageNumb er | Integer | No | 1 | The page number. Pages start from page 1. Default value: 1. |
| OrderType | String | No | asc | The order of time in which the log entries to return are sorted. Valid values: asc: The log entries are sorted by time in ascending order. desc (default): The log entries are sorted by time in descending order. |
| ResourceG roupId | String | No | rg- acfmyiu4ekp*** * | The ID of the resource group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MongoDB | The database engine. |
| Items | Array of LogRecords |  | The details of the slow query logs. |

**Response parameters**

| LogRecords |  |  |  |
|---|---|---|---|
| AccountName | String | root | The account of the database. |
| DBName | String | admin | The name of the database. |
| DocsExamined | Long | 1000000 | The number of documents scanned during the execution of the slow query. |
| ExecutionStart Time | String | 2022-09- 06T01:41:28Z | The beginning of the queried time range. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| HostAddress | String | 192.168.XX.XX | The IP address of the client that connects to the database. |
| KeysExamined | Long | 0 | The data entries that are scanned during indexing. |
| QueryTimes | String | 600 | The execution duration of the query. Unit: milliseconds. |
| ReturnRowCou nts | Long | 0 | The number of rows returned as the result of the slow query. |
| SQLText | String | {\"op\":\"query\",\" ns\":\"mongodbtest .customer\",\"query \": {\"find\":\"custome r\",\"filter\": {\"name\":\"jack\"} }} | The SQL statement that is executed as part of the slow query. |
| TableName | String | C1 | The name of the collection. |
| PageNumber | Integer | 1 | The page number. |
| PageRecordCo unt | Integer | 1 | The number of slow query logs on the page. |
| RequestId | String | 414A4E5-4C36- 4461-95FC- 23757A20B5F8 | The request ID. |
| TotalRecordCo unt | Integer | 1 | The total number of entries. |

Sample requests

```
http(s)://mongodb.example.com/?Action=DescribeSlowLogRecords &StartTime=2022-09-05T12:10Z &EndTime=2022-09-06T12:10Z &DBInstanceId=dds-bp1366caac83**** &NodeId=d-bp18b06ebc21**** &DBName=admin &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalRecordCount>1</TotalRecordCount> <PageRecordCount>1</PageRecordCount> <RequestId>414A4E5-4C36-4461-95FC-23757A20B5F8</RequestId> <PageNumber>1</PageNumber> <Items>
    <LogRecords>
        <TableName>C1</TableName>
        <QueryTimes>600</QueryTimes>
        <ExecutionStartTime>2022-09-06T01:41:28Z</ExecutionStartTime>
        <ReturnRowCounts>0</ReturnRowCounts>
        <KeysExamined>0</KeysExamined>
        <DBName>mongodbtest</DBName>
        <DocsExamined>1000000</DocsExamined>
        <HostAddress>192.168.XX.XX</HostAddress>
        <AccountName>root</AccountName>
        <SQLText>{\"op\":\"query\",\"ns\":\"mongodbtest.customer\",\"query\":
{\"find\":\"customer\",\"filter\":{\"name\":\"jack\"}}}</SQLText>
    </LogRecords>
</Items> <Engine>MongoDB</Engine>
```

`JSON` format

```json
{
    "TotalRecordCount": "1",
    "PageRecordCount": "1",
    "RequestId": "414A4E5-4C36-4461-95FC-23757A20B5F8",
    "PageNumber": "1",
    "Items": {
        "LogRecords": [{
            "TableName": "C1",
            "QueryTimes": "600",
            "ExecutionStartTime": "2022-09-06T01:41:28Z",
            "ReturnRowCounts": "0",
            "KeysExamined": "0",
            "DBName": "mongodbtest",
            "DocsExamined": "1000000",
            "HostAddress": "192.168.XX.XX",
            "AccountName": "root",
            "SQLText": "
{\\\"op\\\":\\\"query\\\",\\\"ns\\\":\\\"mongodbtest.customer\\\",\\\"query\\\":{\\\"fi nd\\\":\\\"customer\\\",\\\"filter\\\":{\\\"name\\\":\\\"jack\\\"}}}"
        }]
    },
    "Engine": "MongoDB"
}
```

#### DescribeErrorLogRecords

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeErrorLo gRecords | The operation that you want to perform. Set the value to DescribeErrorLogRecords. |
| StartTime | String | Yes | 2019-01- 01T12:10Z | The beginning of the time range to query. Specify the time in the yyyy- MM-ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-01- 02T12:10Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you specify this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the sharded cluster instance. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary Note If you set NodeId to the ID of a mongos node, the value of this parameter must be primary. |
| DBName | String | No | mongodbtest | The name of the database. |

You can call this operation to view the error logs of an ApsaraDB for MongoDB instance.

**Request parameters**

| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 to 100 |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| ResourceGroupI d | String | No | rg-axxxxxxxx | The ID of the resource group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MongoDB | The database engine. |
| Items | Array of LogRecords |  | An array that consists of the information of log entries. |
| LogRecords |  |  |  |
| Category | String | NETWORK | The category of the log entry. |
| ConnInfo | String | conn18xxxxxx | The log connection information. |
| Content | String | xxxxxxxx | The content of the log entry. |
| CreateTime | String | 2019-02- 26T12:09:34Z | The time when the log entry was generated. The time is in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Id | Integer | 1111111111 | The ID of the log entry. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageRecordCo unt | Integer | 1 | The number of entries returned on each page. |
| RequestId | String | 68BCBEC2-1E66- 471F-A1A8- E3C60C0A80B0 | The ID of the request. |
| TotalRecordCo unt | Integer | 1 | The total number of entries. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeErrorLogRecords &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <Items>
      <LogRecords>
         <Category>NETWORK</Category>
         <CreateTime>2019-02-26T12:09:34Z</CreateTime>
         <ConnInfo>conn18xxxxxx</ConnInfo>
         <Content>xxxxxxxx</Content>
      </LogRecords>
   </Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>2</TotalRecordCount>
   <RequestId>68BCBEC2-1E66-471F-A1A8-E3C60C0A80B0</RequestId>
```

`JSON` format

```json
{
    "TotalRecordCount":"1",
    "PageRecordCount":"1",
    "RequestId":"68BCBEC2-1E66-471F-A1A8-E3C60C0A80B0",
    "PageNumber":"1",
    "Items":{
        "LogRecords":[
            {
                "ConnInfo":"conn18xxxxxx",
                "Category":"NETWORK",
                "Id":"1111111111",
                "Content":"xxxxxxxx",
                "CreateTime":"2019-02-26T12:09:34Z"
            }
```

]

```
    },"Engine":"MongoDB"
}
```

#### DescribeRunningLogRecords

You can call this operation to view the operational logs of an ApsaraDB for MongoDB instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRunnin gLogRecords | The operation that you want to perform. Set the value to DescribeRunningLogRecords. |
| StartTime | String | Yes | 2019-01- 01T12:10Z | The beginning of the time range to query. Specify the time in the yyyy- MM-ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-01- 02T12:10Z | The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the sharded cluster instance. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
| DBName | String | No | mongodbtest | The name of the database. |
| RoleType | String | No | primary | The role of the node in the instance. Valid values: primary secondary Note If you set NodeId to the ID of a mongos node, the value of RoleType must be primary. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30 to 100 |

| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
|---|---|---|---|---|
| OrderType | String | No | asc | The order of time in which the log entries to return are sorted. Valid values: asc: The log entries are sorted by time in ascending order. desc: The log entries are sorted by time in descending order. |
| ResourceGroupI d | String | No | rg-axxxxxxx | The ID of the resource group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | MongoDB | The database engine. |
| Items | Array of LogRecords |  | An array that consists of the information of log entries. |
| LogRecords |  |  |  |
| Category | String | NETWORK | The category of the log entry. |
| ConnInfo | String | conn18xxxxxx | The log connection information. |
| Content | String | end connection 11.xxx.xxx.xx:3xxx x (0 connections now open)\n | The content of the log entry. |
| CreateTime | String | 2019-02- 26T12:09:34Z | The time when the log entry was generated. The time is in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Id | Integer | 1111111111 | The ID of the log entry. |
| PageNumber | Integer | 1 | The page number of the page returned. |
| PageRecordCo unt | Integer | 30 | The number of entries returned on each page. |

**Response parameters**

| RequestId | String | 45D2B592-DEBA- 4347-BBF3- 47FF6C97DBBC | The ID of the request. |
|---|---|---|---|
| TotalRecordCo unt | Integer | 2 | The total number of entries. |

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeRunningLogRecords &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <Items>
      <LogRecords>
         <Category>-</Category>
         <CreateTime>2019-02-26T12:09:34Z</CreateTime>
         <ConnInfo>conn18xxxxxx</ConnInfo>
         <Content>
    end connection 11.xxx.xxx.xx:3xxxx (0 connections now open)
   </Content>
      </LogRecords>
      <LogRecords>
         <Category>NETWORK</Category>
         <CreateTime>2019-02-26T12:09:34Z</CreateTime>
         <ConnInfo>thread1</ConnInfo>
         <Content>connection accepted from 11.xxx.xxx.xx:3xxxx #1862051 (11 connections
now open)</Content>
      </LogRecords>
   </Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>2</TotalRecordCount>
   <RequestId>45D2B592-DEBA-4347-BBF3-47FF6C97DBBC</RequestId>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDBInsta ncePerformance | The operation that you want to perform. Set the value to DescribeDBInstancePerformance. |

```json
{
    "Items": {
        "LogRecords": [
            {
                "Category": "-",
                "CreateTime": "2019-02-26T12:09:34Z",
                "ConnInfo": "conn18xxxxxx",
                "Content": "end connection 11.xxx.xxx.xx:3xxxx (0 connections now open)\
```

`n"`

```json
            },
            {
                "Category": "NETWORK",
                "CreateTime": "2019-02-26T12:09:34Z",
                "ConnInfo": "thread1",
                "Content": "connection accepted from 11.xxx.xxx.xx:3xxxx #1862051 (11
connections now open)"
            }
```

]

```json
    },
    "PageNumber": 1,
    "TotalRecordCount": 2,
    "RequestId": "45D2B592-DEBA-4347-BBF3-47FF6C97DBBC"
}
```

### Performance monitoring

**management**

#### DescribeDBInstancePerformance

You can call this operation to view the performance data of an ApsaraDB for MongoDB instance.

**Request parameters**

| Key | String | Yes | MongoDB Detail _ edSpaceUsage | The performance metric. Valid values: CpuUsage: the CPU utilization percentage MemoryUsage: the memory usage percentage MongoDB IOPS: the IOPS usage _ IOPSUsage: the IOPS usage percentage. MongoDB DetailedSpaceUsage _ : the disk usage. DiskUsage : the disk usage percentage MongoDB Opcounters : the _ operation QPS MongoDB Connections : the _ number of connections MongoDB Cursors : the number _ of cursors MongoDB Network : the network _ traffic MongoDB Global Lock Current _ _ _ Queue : the global lock waiting _ queues MongoDB Wt Cache : the _ _ WiredTiger storage Note Separate multiple metrics with commas (,). |
|---|---|---|---|---|
| StartTime | String | Yes | 2019-03- 11T12:30Z | The beginning of the time range to query. Specify the time in the yyyy- MM-ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-03- 11T12:30Z | The end of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |

| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in a sharded cluster instance. You can specify this parameter to view the performance of a single node. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
|---|---|---|---|---|
| ReplicaSetRole | String | No | Primary | The role of the node. Valid values: Primary Secondary Note If you set the DBInstanceId parameter to the ID of a standalone instance, the value of this parameter can only be Primary. |
| RoleId | String | No | 60xxxxx | The role ID of a node in a instance. You can call the DescribeReplicaSetRole operation to view role IDs. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 267F98DC-367D- 4F20-B137- 8B5B664D1C5D | The ID of the request. |
| StartTime | String | 2019-03- 11T12:20Z | The beginning of the time range to query. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| EndTime | String | 2019-03- 11T12:30Z | The beginning of the time range to query. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| PerformanceK eys | Array of PerformanceK ey |  | An array that consists of the information of performance metrics. |
| PerformanceK ey |  |  |  |

**Response parameters**

| Key | String | MongoDB Detailed _ SpaceUsage | Performance metric. |
|---|---|---|---|
| PerformanceV alues | Array of PerformanceV alue |  | An array that consists of the values of performance metrics. |
| PerformanceV alue |  |  |  |
| Date | String | 2019-03- 11T12:21:51Z | The date and time when the value is generated. |
| Value | String | 0.6 | The value of a performance metric. |
| Unit | String | MB | The unit of the performance metric. |
| ValueFormat | String | cpu usage _ | The format of the performance metric value. If the performance metric contains multiple fields, the fields are separated with ampersands (&). For example, if you query disk usage, the returned ValueFormat is ins size&amp;data size&amp;log size _ _ _ . |
| DBInstanceId | String | dds-bpxxxxxxxx | The ID of the request. |
| Engine | String | MongoDB | The database engine. It is fixed to MongoDB. |

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeDBInstancePerformance &Key=MongoDB_DetailedSpaceUsage &StartTime=2019-03-11T12:30Z &EndTime=2019-03-11T12:30Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

```xml
<PerformanceKeys>
    <ValueFormat>cpu_usage</ValueFormat>
    <Unit>MB</Unit>
    <Key>MongoDB_DetailedSpaceUsage</Key>
</PerformanceKeys> <PerformanceKeys>
    <PerformanceValues>
        <Value>0.6</Value>
        <Date>2019-03-11T12:21:51Z</Date>
    </PerformanceValues>
</PerformanceKeys> <EndTime>2019-03-11T12:30Z</EndTime> <RequestId>267F98DC-367D-4F20-B137-8B5B664D1C5D</RequestId> <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId> <StartTime>2019-03-11T12:20Z</StartTime> <Engine>MongoDB</Engine>
```

`JSON` format

```json
{
    "PerformanceKeys":[
        {
            "ValueFormat":"cpu_usage",
            "Unit":"MB",
            "Key":"MongoDB_DetailedSpaceUsage"
        },
        {
            "PerformanceValues":[
                {
                    "Value":"0.6",
                    "Date":"2019-03-11T12:21:51Z"
                }
```

]

```
        }
```

`],`

```json
    "EndTime":"2019-03-11T12:30Z",
    "RequestId":"267F98DC-367D-4F20-B137-8B5B664D1C5D",
    "DBInstanceId":"dds-bpxxxxxxxx",
    "StartTime":"2019-03-11T12:20Z",
    "Engine":"MongoDB"
}
```

#### DescribeDBInstanceMonitor

You can call this operation to set the collection frequency of monitoring data for an ApsaraDB for MongoDB instance.

**Request parameters**

| Action | String | Yes | DescribeDBInsta nceMonitor | The operation that you want to perform. Set the value to DescribeDBInstanceMonitor. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Granularity | String | 300 | The collection frequency of monitoring data. The value is fixed to 300 . Unit: seconds. |
| RequestId | String | EFD65226-08CC- 4C4D-B6A4- CB3C382F67B0 | The ID of the request. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeDBInstanceMonitor &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Granularity>300</Granularity> <RequestId>EFD65226-08CC-4C4D-B6A4-CB3C382F67B0</RequestId>
```

`JSON` format

```json
{
 "Granularity": 300,
 "RequestId": "EFD65226-08CC-4C4D-B6A4-CB3C382F67B0"
}
```

### Parameter management

**8.14.1.**

#### DescribeParameterModificationHistory

You can call this operation to view the parameter modification records of an ApsaraDB for MongoDB instance.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeParame terModificationH istory | The operation that you want to perform. Set the value to DescribeParameterModificationH istroy. |
| StartTime | String | Yes | 2019-01- 01T12:10Z | The beginning of the time range to query. Specify the time in the yyyy- MM-ddTHH:mmZ format. The time must be in UTC. |
| EndTime | String | Yes | 2019-01- 02T12:10Z | The end of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| CharacterType | String | Yes | db | The role of the instance. Valid values: db: the shard node cs: the Configserver node mongos: the mongos node logic: the sharded cluster instance |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard in the specified sharded cluster instance. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |

| RegionId | String | No | cn-hangzhou | The region ID of the instance. You can call the DescribeDBInstanceAttribute operation to query the region ID of the instance. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| HistoricalPara meters | Array of HistoricalPara meter |  | An array that consists of the information of parameter modification records. |
| HistoricalPara meter |  |  |  |
| ModifyTime | String | 2019-03- 12T07:58:24Z | The time when the parameter was modified. The time is in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |
| NewParameter Value | String | 200 | The parameter value after modification. |
| OldParameter Value | String | 100 | The parameter value before modification. |
| ParameterNa me | String | operationProfiling.s lowOpThresholdMs | The name of the modified parameter. |
| RequestId | String | B1BB6E0E-B4EF- 4145-81FA- A07719860248 | The ID of the request. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeParameterModificationHistory &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeParame ters | The operation that you want to perform. Set the value toDescribeParameters. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |

```xml
<DescribeParameterModificationHistoryResponse>
   <HistoricalParameters>
      <HistoricalParameter>
         <OldParameterValue>100</OldParameterValue>
         <ModifyTime>2019-03-12T07:58:24Z</ModifyTime>
         <NewParameterValue>200</NewParameterValue>
         <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName>
      </HistoricalParameter>
   </HistoricalParameters>
   <RequestId>B1BB6E0E-B4EF-4145-81FA-A07719860248</RequestId>
</DescribeParameterModificationHistoryResponse>
```

`JSON` format

```json
{
 "HistoricalParameters": {
  "HistoricalParameter": [
   {
    "OldParameterValue": "100",
    "ModifyTime": "2019-03-12T07:58:24Z",
    "NewParameterValue": "200",
    "ParameterName": "operationProfiling.slowOpThresholdMs"
   }
```

]

```json
 },
 "RequestId": "B1BB6E0E-B4EF-4145-81FA-A07719860248"
}
```

#### DescribeParameters

You can call this operation to view parameter configurations of an ApsaraDB for MongoDB instance.

**Request parameters**

| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard in the specified sharded cluster instance. Note This parameter is only valid when you set theDBInstanceIdparameter to the ID of a sharded cluster instance. |
|---|---|---|---|---|
| CharacterType | String | No | mongos | The type of the database account. Valid values: mongos: The account that can be used to log on to a mongos node shard: The account that can be used to log on to a shard node |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConfigParamet ers | Array of Parameter |  | An array that consists of the information of configured parameters. |
| Parameter |  |  |  |
| CheckingCode | String | [0-65536] | The valid values of the parameter. |
| ForceRestart | Boolean | true | Indicates whether a restart is required for parameter modifications to take effect. false: A restart is not required. Modifications take effect immediately after they are made. true: A restart is required for modifications to take effect. |
| ModifiableStat us | Boolean | true | Indicates whether the parameter is modifiable. false true |
| ParameterDes cription | String | The threshold in milliseconds at which the database profiler considers a query slow, default is 100. | The description of the parameter. |
| ParameterNa me | String | operationProfiling.s lowOpThresholdMs | The name of the parameter. |
| ParameterValu e | String | 200 | The value of the parameter. |

**Response parameters**

| Developer Guide·A | PI Reference |  | ApsaraDB for MongoDB |
|---|---|---|---|

| RequestId | String | 3ADD0C7D-2D2A- 4F15-88FF- E7AC9B9FDCC8 | The ID of the request. |
|---|---|---|---|
| RunningParam eters | Array of Parameter |  | An array that consists of the information of instance parameters that have taken effect. |
| Parameter |  |  |  |
| CheckingCode | String | [33554432- 268435456] | The valid values of the parameter. |
| ForceRestart | String | false | Indicates whether a restart is required for parameter modifications to take effect. false: A restart is not required. Modifications take effect immediately after they are made. true: A restart is required for modifications to take effect. |
| ModifiableStat us | String | true | Indicates whether the parameter is modifiable. false true |
| ParameterDes cription | String | The maximum memory bytes that sort stage may use, default is 33554432(i.e. 32MB) | The description of the parameter. |
| ParameterNa me | String | setParameter.inter nalQueryExecMaxB lockingSortBytes | The name of the parameter. |
| ParameterValu e | String | 33554432 | The value of the parameter. |
| EngineVersion | String | 4.0 | The engine version of the instance. |
| Engine | String | mongodb | The database engine of the instance. Default value: mongodb. |

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeParameters &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <ConfigParameters>
            <Parameter>
                  <ParameterDescription>The threshold in milliseconds at which the datab
ase profiler considers a query slow, default is 100. </ParameterDescription>
                  <ParameterValue>200</ParameterValue>
                  <CheckingCode>[0-65536]</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName>
            </Parameter>
      </ConfigParameters>
      <RequestId>3ADD0C7D-2D2A-4F15-88FF-E7AC9B9FDCC8</RequestId>
      <RunningParameters>
            <Parameter>
                  <ParameterDescription></ParameterDescription>
                  <ParameterValue>zlib</ParameterValue>
                  <CheckingCode>snappy|zlib|disabled</CheckingCode>
                  <ForceRestart>true</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>net.compression.compressors</ParameterName>
            </Parameter>
            <Parameter>
                  <ParameterDescription>The level of database profiling, which inserts i
nformation about operation performance into the system.profile collection. 'off' for no profiling, 'slowOp' for only includes slow operations, 'all' for includes all operation s, default is 'slowOp'. </ParameterDescription>
                  <ParameterValue>slowOp</ParameterValue>
                  <CheckingCode>off|slowOp|all</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>operationProfiling.mode</ParameterName>
            </Parameter>
            <Parameter>
                  <ParameterDescription>The threshold in milliseconds at which the datab
ase profiler considers a query slow, default is 100. </ParameterDescription>
                  <ParameterValue>220</ParameterValue>
                  <CheckingCode>[0-65536]</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName>
            </Parameter>
            <Parameter>
                  <ParameterDescription>The expiration threshold in milliseconds for idl
e cursors before MongoDB removes them; i.e. MongoDB removes cursors that have been idle for the specified cursorTimeoutMillis. default is 600000(i.e. 10 minutes)
```

```xml
</ParameterDescription>
                  <ParameterValue>600000</ParameterValue>
                  <CheckingCode>[1-2147483647]</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
                  <ParameterName>setParameter.cursorTimeoutMillis</ParameterName>
            </Parameter>
            <Parameter>
                  <ParameterDescription>The maximum memory bytes that sort stage may use
, default is 33554432(i.e. 32MB)</ParameterDescription>
                  <ParameterValue>33554432</ParameterValue>
                  <CheckingCode>[33554432-268435456]</CheckingCode>
                  <ForceRestart>false</ForceRestart>
                  <ModifiableStatus>true</ModifiableStatus>
<ParameterName>setParameter.internalQueryExecMaxBlockingSortBytes</ParameterName>
            </Parameter>
      </RunningParameters>
      <EngineVersion>4.0</EngineVersion>
      <Engine>mongodb</Engine>
```

`JSON` format

```json
{
    "ConfigParameters": {
        "Parameter": [
            {
                "ParameterDescription": "The threshold in milliseconds at which the data
base profiler considers a query slow, default is 100.",
                "ParameterValue": "200",
                "CheckingCode": "[0-65536]",
                "ForceRestart": false,
                "ModifiableStatus": true,
                "ParameterName": "operationProfiling.slowOpThresholdMs"
            }
```

]

```json
    },
    "RequestId": "3ADD0C7D-2D2A-4F15-88FF-E7AC9B9FDCC8",
    "RunningParameters": {
        "Parameter": [
            {
                "ParameterDescription": "",
                "ParameterValue": "zlib",
                "CheckingCode": "snappy|zlib|disabled",
                "ForceRestart": "true",
                "ModifiableStatus": "true",
                "ParameterName": "net.compression.compressors"
            },
            {
                "ParameterDescription": "The level of database profiling, which inserts
information about operation performance into the system.profile collection. 'off' for n o profiling, 'slowOp' for only includes slow operations, 'all' for includes all operati ons,defaultis'slowOp'.",
```

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidDBInstanceC lass.NotFound | Specified DB instance class is not found. | The error message returned when the specified instance type does not exists. Verify the specified instance type. |
| 403 | IncorrectDBInstanc eType | Current DB instance type does not support this operation. | The error message returned when the current operation is not supported by the instance type of the specified instance. |

```
os,deaut
```

s

```json
sowOp.,
                "ParameterValue": "slowOp",
                "CheckingCode": "off|slowOp|all",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "operationProfiling.mode"
            },
            {
                "ParameterDescription": "The threshold in milliseconds at which the data
base profiler considers a query slow, default is 100.",
                "ParameterValue": "220",
                "CheckingCode": "[0-65536]",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "operationProfiling.slowOpThresholdMs"
            },
            {
                "ParameterDescription": "The expiration threshold in milliseconds for id
le cursors before MongoDB removes them; i.e. MongoDB removes cursors that have been idl e for the specified cursorTimeoutMillis. default is 600000(i.e. 10 minutes)",
                "ParameterValue": "600000",
                "CheckingCode": "[1-2147483647]",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "setParameter.cursorTimeoutMillis"
            },
            {
                "ParameterDescription": "The maximum memory bytes that sort stage may us
e, default is 33554432(i.e. 32MB)",
                "ParameterValue": "33554432",
                "CheckingCode": "[33554432-268435456]",
                "ForceRestart": "false",
                "ModifiableStatus": "true",
                "ParameterName": "setParameter.internalQueryExecMaxBlockingSortBytes"
            }
```

]

```json
    },
    "EngineVersion": "4.0",
    "Engine": "mongodb"
}
```

**Error codes**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyParamete rs | The operation that you want to perform. Set the value toModifyParameters. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| Parameters | String | Yes | {"operationProfil ing.slowOpThres holdMs":"300"} | The parameters to be modified and their new values. Set this parameter to a JSON string. For example, set the parameter in the {"name":"value","name":"value2"} format. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the mongos or shard node in the specified sharded cluster instance. Note This parameter is only valid when you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
| CharacterType | String | No | db | The role of the instance. Valid values: db: the shard node cs: the Configserver node mongos: the mongos node logic: the sharded cluster instance |

#### ModifyParameters

You can call this operation to modify the parameters of an AsparaDB for MongoDB instance. The instance must be in the running state when you call this operation.

**Note**

If some of the modified parameters take effect only after the instance is restarted, the instance is automatically restarted after the operation is complete. You can call the **DescribeParameterTemplates** operation to query the parameters that take effect only after the instance is restarted.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 36923CC2-DDAB- 4B48-A144- DA92C1E19537 | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackup Policy | The operation that you want to perform. Set the value to DescribeBackupPolicy. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=ModifyParameters &DBInstanceId=dds-bpxxxxxxxx &Parameters={"operationProfiling.slowOpThresholdMs":"300"} &<Common request parameters>
```

Sample success responses `XML` format

```xml
      <RequestId>36923CC2-DDAB-4B48-A144-DA92C1E19537</RequestId>
```

`JSON` format

```json
{
    "RequestId": "36923CC2-DDAB-4B48-A144-DA92C1E19537"
}
```

### Backup and recovery

#### DescribeBackupPolicy

You can call this operation to view the backup policy of an ApsaraDB for MongoDB instance.

**Request parameters**

**Response parameters**

| BackupRetenti onPeriod | String | 7 | The backup retention period. Unit: days. |
|---|---|---|---|
| PreferredBack upPeriod | String | Monday,Wednesda y,Friday,Sunday | The period of backup. Valid values: Monday Tuesday Thursday Friday Saturday Sunday |
| PreferredBack upTime | String | 20:00Z-21:00Z | The time when the data was backed up. The time is in the HH:mmZ-HH:mmZ format. The time is displayed in UTC. |
| PreferredNext BackupTime | String | 2020-05- 13T22:56Z | The next backup time. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. |
| RequestId | String | C2C283A1-1CC4- 4DD9-B985- 3811E0244A45 | The ID of the request. |

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeBackupPolicy DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PreferredBackupPeriod>Monday,Wednesday,Friday,Sunday</PreferredBackupPeriod> <RequestId>C2C283A1-1CC4-4DD9-B985-3811E0244A45</RequestId> <PreferredBackupTime>20:00Z-21:00Z</PreferredBackupTime> <PreferredNextBackupTime>2020-05-13T22:56Z</PreferredNextBackupTime> <BackupRetentionPeriod>7</BackupRetentionPeriod>
```

`JSON` format

```json
{
    "PreferredBackupPeriod":"Monday,Wednesday,Friday,Sunday",
    "RequestId":"C2C283A1-1CC4-4DD9-B985-3811E0244A45",
    "PreferredBackupTime":"20:00Z-21:00Z",
    "PreferredNextBackupTime":"2020-05-13T22:56Z",
    "BackupRetentionPeriod":"7"
}
```

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBackupPo licy | The operation that you want to perform. Set the value to ModifyBackupPolicy. |
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. |
| PreferredBackup Period | String | Yes | Monday,Wednes day,Friday,Sund ay | The backup cycle. Valid values: Monday: Monday Tuesday: Tuesday Wednesday: Wednesday Thursday: Thursday Friday: Friday Saturday: Saturday Sunday: Sunday Note To specify multiple values, separate them with commas (,). |
| PreferredBackup Time | String | Yes | 03:00Z-04:00Z | The time range during which to perform backups. Specify the time in the HH:mmZ-HH:mmZ format. The time must be in UTC. Note The time range must be one hour. |
| BackupRetentio nPeriod | String | Yes | 7 | The retention period of backup files. Valid values: 7 to 730. |

| Parameter | Type | Example | Description |
|---|---|---|---|

#### ModifyBackupPolicy

Call the ModifyBackupPolicy operation to modify the backup policy for a MongoDB instance.

**Request parameters**

**Response parameters**

| RequestId | String | 644A359C-B871- 4DD3-97B5- ED91EF5809C2 | The ID of the request. |
|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBackup | The operation that you want to perform. Set the value to CreateBackup. |
| DBInstanceId | String | Yes | d-bpxxxxxxxx | The ID of the instance. |
| BackupMethod | String | No | Logical | The backup method of the instance. Default value: Physical. Valid values: Logical Physical |

Sample requests

```
http(s)://mongodb.example.com/?Action=ModifyBackupPolicy &DBInstanceId=dds-bpxxxxxxxx &PreferredBackupPeriod=Monday,Wednesday,Friday,Sunday &PreferredBackupTime=03:00Z-04:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>644A359C-B871-4DD3-97B5-ED91EF5809C2</RequestId>
```

`JSON` format

```json
{
 "RequestId": "644A359C-B871-4DD3-97B5-ED91EF5809C2"
}
```

#### CreateBackup

You can call this operation to manually back up an ApsaraDB for MongoDB instance. The instance must be in the running state when you call this operation.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupId | String | 5664xxxx | The ID of the backup set. |
| RequestId | String | 7016B12F-7F64- 40A4-BAFF- 013F02AC82FC | The ID of the request. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackup s | The operation that you want to perform. Set the value to DescribeBackups. |
| StartTime | String | Yes | 2019-03- 12T12:00Z | The beginning of the time range to query. Specify the time in the yyyy- MM-ddTHH:mmZ format. The time must be in UTC. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=CreateBackup DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>7016B12F-7F64-40A4-BAFF-013F02AC82FC</RequestId>
   <BackupId>5664xxxx</BackupId>
```

`JSON` format

```json
{
    "RequestId": "7016B12F-7F64-40A4-BAFF-013F02AC82FC",
    "BackupId": "5664xxxx"
}
```

#### DescribeBackups

You can call this operation to view the backups of an ApsaraDB for MongoDB instance.

**Request parameters**

| EndTime | String | Yes | 2019-03- 13T12:00Z | The end of the time range to query. Specify the time in the yyyy-MM- ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds-bpxxxxxxxx | The ID of the instance. Note If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter. |
| NodeId | String | No | d-bpxxxxxxxx | The ID of the shard node in the sharded cluster instance. Note This parameter is valid only if you set the DBInstanceId parameter to the ID of a sharded cluster instance. |
| BackupId | String | No | 12345678 | The ID of the backup set. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 30 | The number of entries returned per page. |
| RequestId | String | 8925E66F-1971- 4C8C-90A7- F93BF1867E25 | The ID of the request. |
| TotalCount | Integer | 1 | The total number of backup sets. |
| Backups | Array of Backup |  | An array that consists of the information of backup sets. |

**Response parameters**

| Backup |  |  |  |
|---|---|---|---|
| BackupDBNam es | String | mongodbtest,new,t est | The name of the database that has been backed up. |
| BackupDownlo adURL | String | http://xxxxx.oss- cn- hangzhou.aliyuncs. com/xxxxx/hinsxxx xx data xxxxx.tar. _ _ gz | The Internet download URL of the backup file. If the download URL is unavailable, this parameter is an empty string. |
| BackupEndTim e | String | 2019-03- 13T04:34:57Z | The end of the backup time range. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| BackupId | Integer | 11111111 | The ID of the backup set. |
| BackupIntrane tDownloadURL | String | http://xxxxx.oss- cn-hangzhou- internal.example.c om/xxxxx/xxxxx.tar .gz | The internal download URL of the backup file. Note You can download the backup file by using this URL on the Elastic Compute Service (ECS) instance that is connected to the ApsaraDB for MongoDB instance. The ECS instance and ApsaraDB for MongoDB instance must be in the classic network of the same region or in the same virtual private cloud (VPC). |
| BackupMethod | String | Physical | The backup method. Valid values: Snapshot Physical Logical |
| BackupMode | String | Automated | The backup mode. Valid values: Automated Manual |
| BackupSize | Long | 335520510 | The size of the backup file. Unit: bytes. |
| BackupStartTi me | String | 2019-03- 13T04:32:42Z | The beginning of the backup time range. The time is in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. |

| BackupStatus | String | Success | The status of the backup. Valid values: Success: The backup task is successful. Failed: The backup task failed. |
|---|---|---|---|
| BackupType | String | FullBackup | The backup type. Valid values: FullBackup: full backup. IncrementalBackup: incremental backup. |

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeBackups &StartTime=2019-03-12T12:00Z &EndTime=2019-03-13T12:00Z &DBInstanceId=dds-bpxxxxxxxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>1</TotalCount> <PageSize>30</PageSize> <RequestId>8925E66F-1971-4C8C-90A7-F93BF1867E25</RequestId> <PageNumber>1</PageNumber> <Backups>
    <BackupMethod>Physical</BackupMethod>
    <BackupDownloadURL>http://xxxxx.oss-cn-
hangzhou.aliyuncs.com/xxxxx/hinsxxxxx_data_xxxxx.tar.gz</BackupDownloadURL>
    <BackupIntranetDownloadURL>http://xxxxx.oss-cn-hangzhou-
internal.example.com/xxxxx/xxxxx.tar.gz</BackupIntranetDownloadURL>
    <BackupSize>335520510</BackupSize>
    <BackupMode>Automated</BackupMode>
    <BackupEndTime>2019-03-13T04:34:57Z</BackupEndTime>
    <BackupStartTime>2019-03-13T04:32:42Z</BackupStartTime>
    <BackupType>FullBackup</BackupType>
    <BackupId>11111111</BackupId>
    <BackupDBNames>mongodbtest,new,test</BackupDBNames>
    <BackupStatus>Success</BackupStatus>
</Backups>
```

`JSON` format

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RestoreDBInstan ce | The operation that you want to perform. Set the value to RestoreDBInstance. |

```json
{
    "TotalCount":"1",
    "PageSize":"30",
    "RequestId":"8925E66F-1971-4C8C-90A7-F93BF1867E25",
    "PageNumber":"1",
    "Backups":[
        {
            "BackupMethod":"Physical",
            "BackupDownloadURL":"http://xxxxx.oss-cn-
hangzhou.aliyuncs.com/xxxxx/hinsxxxxx_data_xxxxx.tar.gz",
            "BackupIntranetDownloadURL":"http://xxxxx.oss-cn-hangzhou-
internal.example.com/xxxxx/xxxxx.tar.gz",
            "BackupSize":"335520510",
            "BackupMode":"Automated",
            "BackupEndTime":"2019-03-13T04:34:57Z",
            "BackupStartTime":"2019-03-13T04:32:42Z",
            "BackupType":"FullBackup",
            "BackupId":"11111111",
            "BackupDBNames":"mongodbtest,new,test",
            "BackupStatus":"Success"
        }
```

]

```
}
```

#### RestoreDBInstance

Restores data to the current ApsaraDB for MongoDB instance. This operation is applicable only to replica set instances. Standalone instances and sharded cluster instances are not supported. You can clone a standalone instance by creating an instance from a backup set. You can clone a sharded cluster instance by calling the CreateShardingDBInstance operation.

**Note**

This operation overwrites the data of the current instance, and the data cannot be restored. Proceed with caution.

**Request parameters**

| BackupId | Integer | Yes | 11111111 | The ID of the backup set. Note You can call the DescribeBackups operation to query the backup set ID. |
|---|---|---|---|---|
| DBInstanceId | String | Yes | dds- bp11501cd7b5* *** | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 973DCB8F-56B3- 4102-8777- 3A90495927F7 | The request ID. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/?Action=RestoreDBInstance &BackupId=11111111 &DBInstanceId=dds-bp11501cd7b5**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
   <RequestId>973DCB8F-56B3-4102-8777-3A90495927F7</RequestId>
```

`JSON` format

```json
{
 "RequestId": "973DCB8F-56B3-4102-8777-3A90495927F7"
}
```

#### DescribeBackupDBs

You can call this operation to view the databases at a specified time or the databases in a specified backup set before you restore a database for an ApsaraDB for MongoDB instance.

**Note**

You can call the **CreateDBInstance** operation to restore a database for an ApsaraDB for MongoDB instance.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackup DBs | The operation that you want to perform. Set the value to DescribeBackupDBs. |
| SourceDBInstan ce | String | Yes | dds-bpxxxxxxxx | The ID of the source instance. |
| PageNumber | Integer | No | 1 | The number of the page to return. The value must be a positive integer. Default value: 1. |
| PageSize | Integer | No | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. Default value: 30. |
| RestoreTime | String | No | 2019-08- 22T12:00:00Z | The point in time at which the instance will be restored. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Note It can be any time within the past seven days. The time must be earlier than the current time, but later than the time when the database was created. You must specify either this parameter or the BackupId parameter. |
| BackupId | String | No | 5664xxxx | The ID of the backup set. Note You can call the DescribeBackups operation to view the backup ID. You must specify this parameter or the RestoreTime parameter. |

Before you call this operation, make sure that the following requirements are met: A replica set instance is used. The database engine version of the instance must be **3.0**, **3.4**, **4.0**, or **4.2**.

**Request parameters**

| ResourceGroupI d | String | No | rg-axxxxxxxx | The ID of the resource group. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Databases | Array of Database |  | An array that consists of inforamtion of databases. |
| Database |  |  |  |
| DBName | String | mongodbtest | The name of the database. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| TotalCount | Integer | 5 | The number of databases. |
| PageSize | Integer | 30 | The number of entries returned on each page. |
| RequestId | String | 1AF0AD89-ED4F- 44AD-B65F- BFC1D5CD9455 | The ID of the request. |

**Response parameters**

Sample requests

```
http(s)://mongodb.example.com/? Action=DescribeBackupDBs &SourceDBInstance=dds-bpxxxxxxxx &RestoreTime=2019-08-22T12:00:00Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>5</TotalCount> <Databases>
    <DBName>mongodbtest</DBName>
</Databases> <PageSize>30</PageSize> <RequestId>1AF0AD89-ED4F-44AD-B65F-BFC1D5CD9455</RequestId> <PageNumber>1</PageNumber>
```

`JSON` format

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectDBInstanc eType | Current DB instance type does not support this operation. | The error message returned when the current operation is not supported by the instance type of the specified instance. |

| State | Description |
|---|---|
| Creating | The instance is being created. |
| DBInstanceClassChanging | The instance specifications are being changed. |
| DBInstanceNetTypeChanging | The network type of the instance is being changed. |
| Deleting | The instance is being deleted. |
| EngineVersionUpgrading | The database engine version of the instance is being upgraded. |
| GuardSwitching | The instance is undergoing a disaster-triggered failover. |
| HASwitching | The instance is undergoing a primary/secondary switching. |
| Importing | Data is being imported into the instance. |
| ImportingFromOthers | A database is being imported into the instance. |
| LinkSwitching | The instance is undergoing a link switching. |
| MinorVersionUpgrading | The minor version of the instance is being upgraded. |

```json
{
    "TotalCount":"5",
    "Databases":[
        {
            "DBName":"mongodbtest"
        }
```

`],`

```json
    "PageSize":"30",
    "RequestId":"1AF0AD89-ED4F-44AD-B65F-BFC1D5CD9455",
    "PageNumber":"1"
}
```

**Error codes**

### Instance states

This topic descries the instance states of ApsaraDB for MongoDB instances.

| NET CREATING _ | A network connection to the instance is being created. |
|---|---|
| NET DELETING _ | A network connection to the instance is being deleted. |
| NodeCreating | A node is being created in the instance. |
| NodeDeleting | A node is being deleted in the instance. |
| Rebooting | The instance is being restarted. |
| Restoring | The cluster is being restored from the backup. |
| Running | The cluster is running. |
| SSLModifying | The SSL status of the instance is changing. |
| TempDBInstanceCreating | A node is being deleted in the instance. |
| Transing | The instance is being migrated. |
| TransingToOthers | A database in the instance is being migrated. |

| Parameter | Type | Requ ired | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::123456 789012****:role/ adminrole | The Apsara Stack Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Apsara Stack tenant account. |

## Appendixes

### STS overview

#### What is STS?

Apsara Stack Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed for Apsara Stack resource access only by using an STS token. When an STS token is issued, you can specify a validity period and access permissions for the STS token.

**Use an STS token to assume a RAM role**

An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and use the STS token to access Apsara Stack resources.

**Benefits**

STS tokens reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify a validity period for an STS token. The token automatically becomes invalid when it expires. You do not need to rotate STS tokens on a regular basis. You can attach custom policies to STS tokens for flexible and fine-grained authorization.

#### AssumeRole

Obtains a Security Token Service (STS) token that is used by a RAM user to assume a RAM role. In this example, an Apsara Stack tenant account is used as the trusted entity of the RAM role.

**Request parameters**

| Parameter | Type | Requ ired | Example | Description |
|---|---|---|---|---|
| RoleSessionNa me | String | Yes | alice | The name of the role session. Set this parameter based on your business requirements. In most cases, you can set this parameter to the identity of the user who calls the operation. For example, specify a username. In ActionTrail logs, you can distinguish the users who assume the same RAM role to perform operations based on the value of the RoleSessionName parameter. This way, you can perform user-specific auditing. The name must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resourc e": ["*"]}],"Version":" 1"} | The policy that specifies the permissions of the STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. The policy must be 1 to 1,024 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | The ID of the request. |
| Credentials | None | None | The access credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuK g5U1**** | The AccessKey ID. |
| AccessKeySecret | String | ****************************************** | The AccessKey secret. |
| SecurityToken | String | ******** | The security token. |

**Responses**

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
        }
    }
}
```

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
        }
    }
}
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
