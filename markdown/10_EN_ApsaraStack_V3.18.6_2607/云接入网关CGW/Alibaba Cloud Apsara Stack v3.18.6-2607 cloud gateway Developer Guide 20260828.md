---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 cloud gateway Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 71
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 cloud gateway Developer Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E6%8E%A5%E5%85%A5%E7%BD%91%E5%85%B3CGW/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20cloud%20gateway%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 cloud gateway Developer Guide 20260828

## Quick Start

### Developer document

**instructions**

This topic describes how to find the required documentation when calling an API operation of an Apsara Stack service.

**Usage process**

You can follow the procedure in the figure below to access the development documentation you need.

**Prerequisites**

You need to obtain the Apsara Stack version from Operations and Maintenance (O&M) personnel or an operations administrator.

**Procedure**

You can visit the Apsara Stack documentation center to view the required documentation.
1. Open the Apsara Stack documentation center in your browser.
2. Click the **Enterprise Edition**, **Agility Edition**, or **Appliance** tab based on your Apsara
Stack version.
3. Select the corresponding Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the Apsara Stack service whose documentation you
want to view.
5. Click **View details** or **Download PDF** in the target document area.

### Procedure for API calls

Apsara Stack allows you to call API operations using either the Portable OpenAPI Proxy (POP) gateway or the Apsara Stack API (ASAPI) gateway. To provide the same experience as the public cloud, API operations in Apsara Stack are called using the POP gateway by default starting from Apsara Stack Enterprise V3.16.0. This topic describes how to use the POP gateway to call Apsara Stack API operations. The method of using the ASAPI gateway to call Apsara Stack API operations in earlier versions is still valid. For more information, see ASAPI gateway call procedure, Generate an endpoint for ASAPI, and Obtain the SDK package for ASAPI.

**Flowchart**

**Procedure**

1. Obtain an AccessKey pair.
Obtain the AccessKey parameter required for the call. For more information, see Obtain an AccessKey pair or Obtain STS AccessKey credentials. We recommend that you use the AccessKey pair of a personal account or STS AccessKey credentials to call the API operations of the Apsara Uni-manager Management Console and cloud services.
2. Obtain a region ID.
Obtain the RegionID parameter required for the call. For more information, see Obtain common header parameters.
3. Obtain the organization ID and resource set ID.
You need to obtain the organization ID through an API. For more information about how to obtain the organization ID, see the GetOrganizationList chapter in the Apsara Uni-manager Management Console Developer Guide. You need to obtain the resource set ID through an API. For more information about how to obtain the resource set ID, see the ListResourceGroup chapter in the Apsara Uni-manager Management Console Developer Guide. When you call an API operation, add the organization ID `<x-acs-organizationid>` and resource set ID `<x-acs-resourcegroupid>` to the header parameters to specify the organization and resource set to which the resources belong. This enables you to query resources in isolation. If you do not specify the organization ID `<x-acs-organizationid>` , the system obtains the organization to which the current user belongs by default. If you do not specify the resource set ID `<x-acs-resourcegroupid>` , it is empty by default. If you want to specify a resource set, you must also specify the organization ID.
4. Obtain the API references.
You need to review the developer guide of the target cloud service to understand the functions and usage of the API operations. For more information about the process and method to obtain the developer guide, see Instructions for using developer documentation.
5. Obtain the endpoint of the cloud service.
6. Obtain the SDK of the cloud service and call an API operation.

## Preparations

### Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, you must obtain the endpoint of the console from the deployment personnel. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. In the address bar of your browser, enter the endpoint of the Apsara Uni-manager
Management Console and press Enter.
2. Enter the correct username and password.
Obtain the username and password from an operations administrator. The first time you log on to the Apsara Uni-manager Management Console, you must follow the on-screen instructions to change the password of your account. For security purposes, your password must be 10 to 32 characters in length and must contain at least two of the following types of characters: Uppercase or lowercase letters (A to Z, a to z) Digits (0 to 9) Special characters (such as exclamation point (!), at sign (@), number sign (#), dollar sign ($), and percent sign (%))
3. Click **Account Logon**.
4. If Multi-Factor Authentication (MFA) is enabled for your account, perform the following
operations based on your scenario: The first time you log on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator: a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Re-enter your username and password as described in Step 2, and click **Account**
**Logon**.
c. Enter the 6-digit MFA code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter the 6-digit MFA code and click **Authenticate**.
5. In the menu bar at the top of the page, choose **Products > Others > API Tools**.

### View API information

When using a service SDK, you need to obtain the service name, API operation name, and API version. This topic describes how to view API information.

**Background information**

The API operations in API Audit are for reference only. For information about how to use specific API operations, see the API documentation of each cloud service. If there are inconsistencies, the API support information takes precedence.

**Procedure**

1. Log on to the API & Tools console.
2. In the left-side navigation pane, select **API Audit**.
3. On the **API Audit** page, enter keywords such as **API name** to search.
4. View and record the corresponding service name, API operation name, and call status.

### Obtain an AccessKey pair

AccessKey pairs are assigned by Resource Access Management (RAM) or Security Token Service (STS). You can use one type of AccessKey pairs for authentication when you call API operations. This topic describes how to obtain an AccessKey pair assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender based on symmetric encryption. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. AccessKey pairs can be assigned by RAM or STS: RAM: assigns an AccessKey pair that consists of an AccessKey ID and an AccessKey secret. STS: assigns an access credential that consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an STS AccessKey pair. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only operations administrators and the administrators of level-1 organizations can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the headers for access control. Otherwise, an error that indicates insufficient permissions may occur. The following table describes the headers.

**Warning**

The AccessKey pair of a personal account is managed and limited by the permission system of the Apsara Uni-manager Management Console. If you want to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The region, such as cn-hangzhou-*. |

| x-acs-organizationid | The organization ID in the Apsara Uni-manager Management Console. For more information about how to obtain the organization ID, see the GetOrganizationList topic in Apsara Uni- manager Management Console Developer Guide. |
|---|---|
| x-acs-resourcegroupid | The resource set ID in the Apsara Uni-manager Management Console. For more information about how to obtain the resource set ID, see the ListResourceGroup topic in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

**Obtain an AccessKey pair for personal accounts**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the page, click the profile picture and then click **Personal**
**Information**.
3. In the **Alibaba Cloud AccessKey** section, you can view the AccessKey information of your
personal account. The AccessKey pair provides full permissions on cloud resources within your Apsara Stack tenant account. You must keep the AccessKey pair confidential.

**Obtain an AccessKey pair for organizations**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resource Management > Organization**
**Management**.
4. In the organization chart, click the name of the target level-1 organization.
5. Click **Manage AccessKey**.
6. In the dialog box that appears, view the AccessKey information of the organization.

### Obtain an STS AccessKey

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

Apsara Stack Security Token Service (STS) allows you to manage temporary credentials for your Apsara Stack resources. You can use STS credentials to call Apsara Stack API operations. When you use STS to call API operations, you must specify an AccessKey ID, an AccessKey secret, and a security token, which together form an STS AccessKey 3-tuple. For more information, see What is STS.

**Procedure**

1. Obtain the `RAM Role` of the user.
i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page, and click **Personal**
**information**.
iii. Click **View current role policy**. In the **Current selected role policy** dialog box, view the `RAM Role` .
2. Obtain the STS AccessKey 3-tuple.
In the following sample code, replace the parameters with the actual information. Delete the angle brackets (<>) in the final code. The following list describes the parameters: <yourRegionID>: Replace it with your region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourRoleSessionName>: Replace it with the name of the current session. <yourRoleArn>: Replace it with your RAM role. <sts.aliyuns.com>: Replace it with the STS endpoint.

```
public static void main(String[] args) {
    // Create a DefaultAcsClient instance and initialize the instance.
    // Replace with your region ID, AccessKey ID, AccessKey secret
    DefaultProfile profile = DefaultProfile.getProfile("", "", "");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    String assumeRole = callAssumeRole(client);
    if (StringUtils.isEmpty(assumeRole)) return;
    JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
    JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
    // Obtain the STS triplet
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
```

`}`

```java
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    //  Replace with the actual STS Endpoint, generally in the format of sts-vpc.${gl
obal:region}.${global:internet-domain}
    request.setSysDomain("");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Business parameter, set the alias for this session call, replace  with the act
ual value
    request.putQueryParameter("RoleSessionName", "");
    // The ARN of the role to assume, replace  with the actual Ram Role ARN obtained
in the previous step
    request.putQueryParameter("RoleArn", "");
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
3. Call cloud service API operations by using the STS AccessKey 3-tuple. The following code
uses the `DescribeZones` operation of ECS as an example. In the following sample code, replace the parameters with the actual information. Delete the angle brackets (<>) in the final code. The following list describes the parameters: <yourRegionID>: Replace it with your region ID. <yourStsAccesskeyID>: Replace it with your STS AccessKey ID. <yourStsAccessKeySecret>: Replace it with your STS AccessKey secret. <yourStsToken>: Replace it with the security token of the STS AccessKey 3tuple. <yourResourceGroupID>: Replace it with your resource set ID. <yourOrganizationID>: Replace it with your organization ID.

```java
public static void main(String[] args) {
    //  Replace with your actual region ID
    // ,  Replace with the AccessKeyID and AccessKeySecret from the STS triplet obtai
ned in the previous step
    DefaultProfile profile = DefaultProfile.getProfile("", "", "");
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
    // Replace with your actual region ID
    request.putHeadParameter("x-acs-regionid", "");
    //  Replace with the SecurityToken from the STS triplet obtained in the previous
step
    request.putQueryParameter("SecurityToken", "");
    // Optional. Replace with your actual resource set ID
    // request.putHeadParameter("x-acs-resourcegroupid", "");
    // Required. Replace with your organization ID
    request.putHeadParameter("x-acs-organizationid", "");
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

### Obtain the values of common

**request headers**

When calling Apsara Stack API operations, you must provide multiple header parameters. This topic describes these header parameters and how to obtain their values. It also describes the values of some response parameters returned after you call API operations.

**Common request headers**

| Name | Description |
|---|---|
| x-acs-regionid | The region ID of the environment. For more information about how to obtain a region ID, see Obtain a region ID. |
| x-acs-organizationid | The organization ID in the Apsara Uni-manager Management Console. For more information about how to obtain an organization ID, see Obtain an organization ID. |
| x-acs-resourcegroupid | The resource set ID in the Apsara Uni-manager Management Console. For more information about how to obtain a resource set ID, see Obtain a resource set ID. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. For more information about how to obtain an instance ID, see Obtain an instance ID. |

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resource Management** > **Regions**.
4. Click the name of the required organization.
5. View the region ID in the **Region List** on the right.

**Obtain an organization ID**

You need to obtain the organization ID through an API. For more information about how to obtain an organization ID, see the GetOrganizationList chapter in the Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You need to obtain the resource set ID through an API. For more information about how to obtain a resource set ID, see the ListResourceGroup chapter in the Apsara Uni-manager Management Console Developer Guide.

**Obtain an instance ID**

Each cloud service should modify and replace the product name and the process of obtaining an instance ID You can obtain the ID of an instance in a service console of the Apsara Uni-manager Management Console. This section uses the Elastic Compute Service (ECS) console as an example. Perform the following operations to obtain the ID of an ECS instance:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top menu bar, choose **Products** > **Elastic Computing** > **Elastic Compute Service**
**ECS**.
3. In the left-side navigation pane, click **Instances**.
4. View the **Instance ID** in the instance list.

**Response parameters**

The following response parameters are returned by default when you call operations to query the instances of cloud services.

| Name | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

### Obtain the product name

**endpoint**

This topic describes how to obtain the product name endpoint.Replace the product name in the title and short description with your cloud product name

**Background information**

To use the Portable OpenAPI Proxy (POP) gateway to call API operations in Apsara Stack, you must obtain the service endpoint. You can obtain service endpoints from Alibaba Cloud onsite O&M engineers. You can also follow these steps to obtain an endpoint.

**Procedure**

**Warning**

1. 2. 3. 4. Java

## Use the SDK for Java

### Getting started

This section describes how to obtain Product Name SDK for Java and start using it. Replace Product Name with your actual product name.

**Prepare the runtime environment**

Before using Apsara Stack SDK for Java, you must obtain an Apsara Stack tenant account with the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret. For more information, see Obtain an AccessKey pair to view your AccessKey pair in the Apsara Uni-manager Management Console. Obtain the endpoint of Product Name. For more information, see Obtain the endpoint of Product Name. Replace Product Name and the link with your actual product information. Java Development Kit (JDK) 1.8 or later must be installed before you can use Apsara Stack SDK for Java.

**Install Apsara Stack SDK for Java**

If you use Apache Maven to manage a Java project, you need only to import the JAR file to the pom.xml file of the project. To use the SDK for Product Name, you must install the SDK core library and the SDK for the product. We recommend that you use SDK core library version 4.5.17 or later. The SDK version is X.X.X. Replace Product Name with your actual product name and X.X.X with the actual SDK version of your product.

**Use Auto Scaling SDK for Java**

To use Apsara Stack SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and specify the required parameters.
3. Initiate the API request and handle the response or exception.
Replace with your product-specific example Java In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets <> from the final code. The following list describes the variables: <yourRegionID>: Replace the variable with the actual region ID. <yourAccessKeyID>: Replace the variable parameter with your AccessKey ID. <yourAccessKeySecret>: Replace <yourAccessKeySecret> with your AccessKey secret. <Product>: Replace the parameter with the name of the current service. <Endpoint>: Replace the variable parameter with the endpoint of your service. <readTimeout>: Replace the variable parameter with a read timeout period based on your business requirements. Unit: milliseconds. <connectionTimeout>: Replace the variable parameter with a connection timeout period based on your business requirements. Unit: milliseconds. <maxRequestsPerHost>: Replace the variable parameter with the maximum number of requests that are supported by each host. <maxRequests>: Replace the variable parameter with the maximum number of requests. <http://192.168.XX:33XX>: Replace the variable with the IP address and port of the proxy that you use.

```java
 import com.aliyuncs.profile.DefaultProfile;
 import com.aliyuncs.DefaultAcsClient;
 import com.aliyuncs.IAcsClient;
 import com.aliyuncs.exceptions.ClientException;
 import com.aliyuncs.exceptions.ServerException;
 import com.aliyuncs.ecs.model.v20140526.*;
 public class Main {
     public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",          // Enter the region ID.
            "<yourAccessKeyID>",      // Replace the field with the AccessKey ID of th
e current user.
            "<yourAccessKeySecret>"); // Replace <yourAccessKeySecret> with your
AccessKey secret.
        // Specify the endpoint of the current service. Replace the variable with the
actual endpoint.
        profile.addEndpoint("<yourRegionID>", "<Product>", "<Endpoint>");
        // Set the request configuration.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);// Ignore the certificate.
        clientConfig.setReadTimeoutMillis(<readTimeout>);// Optional. Specify the rea
d timeout period. Unit: milliseconds.
        clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);// Optional. Spe
cify the connection timeout period. Unit: milliseconds.
        clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);// Optional. Specify
the maximum number of requests per host.
        clientConfig.setMaxRequests(<maxRequests>);// Optional. Specify the maximum n
```

Java `g` `q` `(` `q`

```
);//
```

`p` `p` `y`

```
umber of requests.
        clientConfig.setProtocolType(ProtocolType.HTTP); // Optional. Set the request
protocol. Default value: HTTP.
        /* Optional. Set the proxy IP address and port.
        clientConfig.setHttpProxy("<http://192.168.XX:33XX>");
```

`or`

```
        clientConfig.setHttpsProxy("<https://192.168.XX:33XX>");
```

`*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure parameters.
        DescribeInstancesRequest request = new DescribeInstancesRequest();
        // Set service-related parameters.
        request.setPageSize(10);
        request.setPageNumber(1);
        // Special header parameters. Specify the organization ID and resource set ID
. Resources are isolated.
        request.putHeadParameter("x-acs-organizationid", "1");
        request.putHeadParameter("x-acs-resourcegroupid", "11");
        // Send the API request and handle the response or exception.
        DescribeInstancesResponse response;
        try {
            response = client.getAcsResponse(request);
            for (DescribeInstancesResponse.Instance instance:response.getInstances())
```

`{`

```java
                System.out.println(instance.getPublicIpAddress());
```

`}`

```
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            e.printStackTrace();
```

`}` `}` `}`

### User guide

#### Install Java SDK

This topic describes how to install and call Product Name SDK for Java. Replace Product Name with your actual product name. Apsara Stack SDK for Java supports JDK 1.8 and later versions. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the Alibaba Cloud SDK. To use the SDK for Product Name, you must install the core library of Alibaba Cloud SDK for Java and the SDK for Java for Product Name. We recommend that you use V4.5.17 or later of the core library, and the X.X.X version of SDK for Java for the actual service. Replace Product Name with your actual product name; Replace X.X.X with your product's SDK version. For example, to use ECS SDK for Java, you must install the core library of Alibaba Cloud SDK for Java and ECS SDK for Java, and add the following dependencies to the pom.xml file. For the exact SDK version number, see Alibaba Cloud SDK. Each cloud product should replace this with their own example Java

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency> <!-- ecs java sdk --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-ecs</artifactId>
    <version>4.23.2</version>
</dependency>
```

#### Configure identity verification

**credentials**

When using Apsara Stack SDK to access Apsara Stack services, you must provide an authorized account for authentication. This topic describes how to configure identity verification credentials. Currently, Java SDK supports authentication through AccessKey. For more information, see Obtain an AccessKey. To access Apsara Stack using your AccessKey pair, you must specify the AccessKey pair as credentials when initializing the client. Do not disclose code that contains your AccessKey pair. For example, do not commit the code to publicly accessible GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",          // Replace with your actual region ID
    "<yourAccessKeyID>",      // Replace with your actual AccessKey ID
    "<yourAccessKeySecret>"); // Replace with your actual AccessKey Secret
```

In the preceding sample code, replace the variable parameters with your actual information. Remove the angle brackets (<>) in the final code.

#### Request connection configuration

This topic describes how to configure HttpClientConfig. You can use the following code to configure HttpClientConfig. Select and configure parameters based on your business requirements. Java In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets (<>) from the final code. The following list describes the variables: <readTimeout>: Specify the read timeout period based on your business requirements. Unit: milliseconds. <connectionTimeout>: Specify the connection timeout period based on your business requirements. Unit: milliseconds. <maxRequestsPerHost>: Specify the maximum number of requests for each server based on your business requirements. The value is in the INT format. <maxRequests>: Specify the maximum number of requests based on your business requirements. The value is in the INT format. <http://192.168.XX.XX:33XX>: Replace it with the IP address and port of the proxy.

```
// Get the HttpClientConfig object HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Specify whether to ignore the certificate clientConfig.setIgnoreSSLCerts(true); // Optional. Specify the read timeout period. Unit: milliseconds clientConfig.setReadTimeoutMillis(<readTimeout>); // Optional. Specify the connection timeout period. Unit: milliseconds clientConfig.setConnectionTimeoutMillis(<connectionTimeout>); // Optional. Specify the maximum number of requests for each server. The value is in th e INT format clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>); // Optional. Specify the maximum number of requests. The value is in the INT format clientConfig.setMaxRequests(<maxRequests>); // Optional. Specify the protocol type clientConfig.setProtocolType(ProtocolType.HTTP); /** (Optional) Specify whether to configure the proxy based on your business requirements. The following code is available: clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`or`

```
clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>"); Replace with the IP address and port of the proxy
```

`*/`

```
profile.setHttpClientConfig(clientConfig);
```

#### Send a request

This topic describes how to send a request by using SDK for Java of a service.

**Procedure**

1. Create an AcsClient.

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
Java The naming convention for request classes is ${apiName}Request , where **${apiName}** is the API name, such as DescribeInstances. When the SDKs of multiple services are used, different requests may have the same name. You can differentiate the requests by SDK package.

```
DescribeInstancesRequest request = new DescribeInstancesRequest(); // Set service-specific parameters request.setPageSize(10); request.setPageNumber(1); // Set the organization ID and resource set ID for special header parameters. Resourc es are isolated. request.putHeadParameter("x-acs-organizationid", "1"); request.putHeadParameter("x-acs-resourcegroupid", "");
```

3. Send a request and handle the response.

```java
DescribeInstancesResponse response; try {
    response = client.getAcsResponse(request);
    for (DescribeInstancesResponse.Instance instance:response.getInstances()) {
        System.out.println(instance.getPublicIpAddress());
```

`}`

```
} catch (ServerException e) {
    e.printStackTrace();
} catch (ClientException e) {
    e.printStackTrace();
```

`}` Under normal circumstances, all fields in the response are deserialized to the response object. You can directly call `response.getXXX()` to obtain fields from the response.

```
instanceStatus := response.getStatus()
```

If an exception occurs or you need the original HTTP response, you can use `doAction()` to obtain the original response.

```
HttpResponse response = client.doAction(request);
```

#### Handle errors

When you use the SDK for Java, the server or SDK might encounter an error and return an error response. The error response contains specific information including error codes and error messages. Generally, you do not need to handle errors returned by the Java SDK. You only need to handle server errors based on error messages generated on the server side. `ServerException` indicates a server error. `ClientException` indicates an SDK error. For example, if the following error occurs, you can modify the AccessKey ID based on the error message:

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

Java If you want to handle the SDK errors, you can refer to the following example to write your code:

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handle the response.
}catch (ServerException e){
    // You can add your error handling logic here.
    // For example, print the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If you are unable to fix the error, submit a ticket and provide RequestId to Ali
baba Cloud technical support personnel.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // You can add your error handling logic here.
    // For example, print the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

`}`

#### Use CommonRequest to call API

**operations**

If you want to call API operations of a cloud service that does not provide an SDK, or you cannot use an SDK to call API operations whose requests and responses meet your business requirements, you can use CommonRequest. CommonRequest allows you to call all available API operations.

**Characteristics of CommonRequest calling**

The CommonRequest calling method has the following characteristics: Light weight: You only need the core package to initiate the call, without downloading or installing the SDK of each product. Easy and convenient: You can call the latest API without updating the SDK. Fast iteration

**Use CommonRequest**

To send a CommonRequest request, you must obtain the values of the following parameters. You can obtain these values from the API references of cloud services. Domain: specifies the service endpoint. Version: the version number of the API, in the YYYY-MM-DD format. You can obtain the API version from the common parameters in the API documents. Operation information: the name of the API operation that you want to call. You need to obtain the **Action** parameter and use `request.setSysAction("")` to specify the API name. For example, for the RunInstances operation, you need to use `request.setSysAction("RunInstances")` to specify the API name when you send a CommonRequest request. Java You need to obtain the **PathPattern** parameter and use `request.setSysUriPattern("")` to specify the RESTful path. For example, the **PathPattern** of the API operation that is used to view all cluster instances

| is | /api/v1/clusters | . When you send a Commo |
|---|---|---|
| request.setSysUriPattern("/api/v1/clusters") |   |   |

**Example: Call an RPC API operation**

The following code provides an example of how to call the API operation that queries the status list of instances (ECS uses the RPC style). In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets <> from the final code. The following list describes the variables: <yourRegionID>: Replace it with your region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourSecurityToken>: Replace it with your security token. <yourResourceGroupID>: Replace it with your resource set ID. <yourOrganizationID>: Replace it with your organization ID. <yourInstanceID>: Replace it with your instance ID. <http://192.168.XX.XX:33XX>: Replace it with the IP address and port of the proxy.

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize it.
        DefaultProfile profile = DefaultProfile.getProfile(
            "",          // Replace it with your region ID.
            "",      // Replace it with your AccessKey ID.
            ""); // Replace it with your AccessKey secret.
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /**
        You can configure HTTP proxy based on your business requirements.
        To configure HTTP proxy, perform the following steps:
        clientConfig.setHttpProxy("");
        Specify the IP address and port of the proxy.
```

`*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure parameters.
        CommonRequest request = new CommonRequest();
        // Replace the parameter with the service domain name.
        request.setDomain("ecs.aliyuncs.com");
        request.setSysProduct("Ecs");
requestsetVersion("20140526");
```

Java

```
        request.setVersion("2014-05-26");
        request.setAction("DescribeInstanceStatus");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        request.putHeadParameter("x-acs-resourcegroupid", "");// Optional. Specify the
resource set ID.
        request.putHeadParameter("x-acs-organizationid", "");// Required. Specify the o
rganization ID.
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// Required.
Specify the source of the call.
        request.putHeadParameter("x-acs-regionid", "");// Optional. Specify the region
ID. This parameter is required if you use Apsara Stack Enterprise V3.15.0 or earlier.
        // request.putHeadParameter("x-acs-instanceid", "");// Optional. Specify the in
stance ID. This parameter is required when you want to delete, modify, or query an inst ance.
        /**
        When you use STS AccessKey credentials to call an API operation, you must add t
he SecurityToken field in the request parameters.
        Use the following method:
        request.putQueryParameter("SecurityToken", "");
        Replace  with your security token.
```

`*/`

```java
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

**Example: Call a RESTful API operation**

You must pass parameters in two methods depending on the request method and ContentType value: If the request method is `GET` or `DELETE` , or the ContentType value is `application/x-` `www-form-urlencoded` , use the following method to pass parameters: Place the request parameters in the Query section, for example,

```
 request.putQueryParameter("page_number", "1"); .
```

If the request method is `POST` or `PUT` , and the ContentType value is `application/json` , use the following method to pass parameters: Place the request parameters in the Body section, for example:

```
String requestBody = "{\"page_number\":\"1\",\"page_size\":\"5\",\"SecurityToken\", \ "\"}"; request.setHttpContent(requestBody.getBytes(), "utf-8", FormatType.JSON);
```

The following code provides an example of how to call the API operation that queries the cluster list (CS uses the RESTful style). Java In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets <> from the final code. The following list describes the variables: <yourRegionID>: Replace it with your region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourResourceGroupID>: Replace it with your resource set ID. <yourOrganizationID>: Replace it with your organization ID. <yourInstanceID>: Replace it with your instance ID. <http://192.168.XX.XX:33XX>: Replace it with the IP address and port of the proxy. <yourSecurityToken>: Replace it with your security token.

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    /**
     * DemoAPI: DescribeClusterV1
```

`*/`

```
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize it.
        DefaultProfile profile = DefaultProfile.getProfile(
            "",          // Replace it with your region ID.
            "",      // Replace it with your AccessKey ID.
            ""); // Replace it with your AccessKey secret.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /**
        Specify whether to configure HTTP proxy based on your requirements.
        To configure HTTP proxy, perform the following steps:
        clientConfig.setHttpProxy("");
        Replace it with the actual IP address and port of the proxy.
```

`*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the request parameters.
        CommonRequest request = new CommonRequest();
        // Actual request method of the API operation. For more information, see the AP
I reference.
        request.setMethod(MethodType.GET);
        request.setDomain("cs.aliyuncs.com");
        request.setSysProduct("CS");
        request.setSysVersion("2015-12-15");
        request.setSysUriPattern("/api/v1/clusters");
        request.putHeadParameter("Content-Type", "application/json");
requestputHeadParameter("x-acs-resourcegroupid" "");//Optional Specifythe
```

Java

```
        request.putHeadParameter(xacsresourcegroupid,
);// Optional. Specify the resource set ID.
        request.putHeadParameter("x-acs-organizationid", "");// Required. Specify the o
rganization ID.
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// Required.
Specify the source of the call.
        request.putHeadParameter("x-acs-regionid", "");// Optional. Specify the region
ID. If you use Apsara Stack Enterprise V3.15.0 or earlier versions, this parameter is r equired.
        // request.putHeadParameter("x-acs-instanceid", "");// Optional. Specify the in
stance ID. This parameter is required when you want to delete, modify, or query the det ailed information about an instance.
        // Business parameters. If the request method is GET or DELETE, or the
ContentType value is application/x-www-form-urlencoded, use the following method to pas s parameters.
        request.putQueryParameter("page_number", "1");
        request.putQueryParameter("page_size", "5");
        String requestBody = "{}";
        /**
        When you use STS AccessKey credentials to call an API operation, you must add t
he SecurityToken field in the request parameters.
        Use the following method:
        String requestBody = "{\"SecurityToken\": \"\"}";
        Replace  with your security token.
```

`*/`

```
        /**
        If the request method is POST or PUT, and the ContentType value is
application/json, use the following method to pass data:
        String requestBody = "
{\"page_number\":\"1\",\"page_size\":\"5\",\"SecurityToken\", \"\"}";
        request.setHttpContent(requestBody.getBytes(), "utf-8", FormatType.JSON);
```

`*/`

```java
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

`}` `}` `}` Python

## Use the SDK for Python

### Getting started

This topic describes how to obtain and use SDK for Python.

**Prepare the runtime environment**

You need an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) before using SDK for Python. For more information, see Obtain an AccessKey. You need to obtain the endpoint. For more information, see Obtain the endpoint of ECS.

**Install SDK for Python**

1. Install the core library.
If you are using Python 2.x, run the following command to install the Alibaba Cloud SDK core library:

```
pip install aliyun-python-sdk-core
```

If you are using Python 3.x, run the following command to install the Alibaba Cloud SDK core library:

```
pip3 install aliyun-python-sdk-core-v3
```

2. Install the SDK.
The following sample code shows how to install ECS SDK for Python: If you are using Python 2.x, run the following command to install ECS SDK for Python:

```
pip install aliyun-python-sdk-ecs
```

If you are using Python 3.x, run the following command to install ECS SDK for Python:

```
pip3 install aliyun-python-sdk-ecs
```

**Use SDK for Python**

To use ECS SDK for Python, perform the following steps:
1. Create a client instance. When creating a client instance, you must obtain a region ID,
AccessKey ID, and AccessKey secret.
2. Create an API request and specify the required parameters.
3. Initiate the API request and handle the response or exception.
In the following sample code, replace the parameters with actual values. Delete the angle brackets (<>) in the final code. The following list describes the variables: <yourRegionID>: Replace the variable with the actual region ID. <yourAccessKeyID>: Replace the variable with your AccessKey ID. <yourAccessKeySecret>: Replace the variable with your AccessKey secret. <ecs.aliyuns.com>: Replace the variable with the endpoint of the service. Python

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
# global config
region_id = '' # Specify your region ID. access_key = '' # Specify your AccessKey ID. acces_secret = '' # Specify your AccessKey secret.
# product config
product_name = 'ECS' # Specify the service name. endpoint = '' # Specify the endpoint of the service.
# create client
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, acces_secret, region_id)
# setup request
request = DescribeInstancesRequest.DescribeInstancesRequest() request.set_accept_format('json') # Specify the response format.
# get response
response = clt.do_action_with_exception(request) print response
```

### Use the SDK

#### Install Python SDK

This topic describes how to install and use Apsara Stack SDK for Python. Apsara Stack SDK for Python supports Python 2.6.x, Python 2.7.x, and Python 3.x or later. You can install Apsara Stack SDK for Python using pip. To use the SDK of a cloud service, you must install the core library of Apsara Stack SDK for Python. For example, if you want to use ECS SDK for Python, you must install the core library of Apsara Stack SDK for Python and ECS SDK for Python. If you are using Python 2.x, run the following command to install the core library of Apsara Stack SDK:

```
pip install aliyun-python-sdk-core
```

If you are using Python 3.x, run the following command to install the core library of Apsara Stack SDK:

```
pip3 install aliyun-python-sdk-core-v3
```

The following examples show how to install ECS SDK for Python: If you are using Python 2.x, run the following command to install ECS SDK:

```
pip install aliyun-python-sdk-ecs
```

If you are using Python 3.x, run the following command to install ECS SDK:

```
pip3 install aliyun-python-sdk-ecs
```

Python

#### Configure identity verification

**credentials**

When using Alibaba Cloud SDK to access Apsara Stack services, you must provide an authorized account for authentication. Currently, Python SDK supports authentication through AccessKey. For more information, see Obtain an AccessKey. To access Apsara Stack using your AccessKey pair, you must specify the AccessKey pair as the credentials when initializing the client.

**Important**

Do not disclose code that contains your AccessKey pair. For example, do not commit the code to publicly accessible GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

#### Set HTTPS requests

SDK for Python enables you to send API requests using HTTP and HTTPS. You can specify a protocol (HTTP or HTTPS) for a specific request, or configure a global default protocol. The default protocol of a service (HTTP/HTTPS) takes precedence over the global default protocol.

**Add OpenSSL dependency**

The HTTPS protocol support in SDK for Python is based on the OpenSSL support in Python. To use Alibaba Cloud SDK to send requests over HTTPS, you need to add OpenSSL support in Python. OpenSSL supports TLS 1.2 and later versions. Run `python -c "import ssl"` to check whether your Python environment supports OpenSSL. If the error message `ImportError: No module named ssl` does not appear, OpenSSL is supported. If OpenSSL is not available, you can install it by running the following command:

```
pip install pyopenssl
```

**Set the protocol to HTTP or HTTPS for a single request**

The following code example shows how to set HTTPS for an API call:

```bash
request = DescribeInstancesRequest() request.set_protocol_type("https")
# Value: "https" or "http"
```

**Configure a global default protocol**

The following code example shows how to configure a global default protocol: Python

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request
```

#### Send a request

This topic describes how to use SDK for Python to send a request.

**Procedure**

1. Import the SDK of the related product.

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
```

2. Create an AcsClient instance.

```
client.region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, access_secret, region_id)
```

3. Create a Request object.

```
request = DescribeInstancesRequest.DescribeInstancesRequest() request.set_accept_format('json')
```

4. Send the request and process the response.

```
response = clt.do_action_with_exception(request) print response
```

#### Handle errors

If the server or SDK encounters an error when you use the SDK for Python, the SDK returns an error response. The error response contains an error code and an error message. Among the errors returned by the SDK for Python, you do not need to handle the SDK errors, but must solve the server errors. `ServerException` indicates a server error. `ClientException` indicates an SDK error. For example, if the following error occurs, you can modify the AccessKey ID based on the error message:

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

If you want to handle the SDK errors returned by the SDK, refer to the following example to write your code: Python

```bash
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
    # You can add your error handling logic here.
    # For example, display the error message.
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

#### Use CommonRequest to call API

**operations**

If you want to call API operations of a cloud service that does not provide an SDK, or you cannot use an SDK to call API operations whose requests and responses meet your business requirements, you can use CommonRequest to call API operations. CommonRequest supports all API operations.

**Characteristics of CommonRequest calling**

The CommonRequest calling method has the following characteristics: Light weight: You only need the core package to initiate the call, without downloading or installing the SDK of each product. Easy and convenient: You can call the latest API without updating the SDK. Fast iteration

**Use CommonRequest**

To send a CommonRequest request, you must obtain the values of the following parameters. You can obtain these values from the API references of cloud services. Domain: specifies the service endpoint. Version: the version number of the API, in the YYYY-MM-DD format. You can obtain the API version from the common parameters chapter in the API document. Operation information: the name of the API operation that you want to call. To call an RPC API operation: You need to obtain the **Action** parameter and use `request.set_action_name('Action')` to specify the API operation name. For example, to call the RunInstances operation, you must use `request.set_action_name('RunInstances')` to specify the API operation name. To call a RESTful API operation: You need to obtain the **PathPattern** parameter and use `request.set_uri_pattern('Pattern')` to specify the RESTful path. For example, the **PathPattern** of the API operation that is used to view all cluster

| ances is | /api/v1/clusters | . When you send a C |
|---|---|---|
| request.set uri pattern('/api/v1/clusters') _ _ |   |   |

**Example: Call an RPC API operation**

The following code provides an example of how to call the DescribeInstanceStatus operation of Elastic Compute Service (ECS) to obtain the status list of instances: Python In the following sample code, replace the parameters with the actual information. Delete the angle brackets (<>) in the final code. The following list describes the parameters: <yourRegionID>: Replace it with your region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourSecurityToken>: Replace it with your security token. <yourResourceGroupID>: Replace it with your resource set ID. <yourOrganizationID>: Replace it with your organization ID. <yourInstanceID>: Replace it with your instance ID. <ecs.aliyuncs.com>: Replace it with the endpoint of the service. Python

```python
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
# Specify the AccessKey ID, AccessKey secret, and region ID.
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('Ecs') request.set_action_name('DescribeInstanceStatus') request.set_version('2014-05-26') request.set_domain('<ecs.aliyuncs.com>') # Specify the endpoint of the service.
# or:
# request = = CommonRequest(product='Ecs',
action_name='DescribeInstanceStatus',version='2014-05-26',domain='ecs.aliyuncs.com')
######
# Set the request protocol type. HTTP and HTTPS are supported. The default protocol is
HTTP.
# You can specify HTTPS as the protocol:
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30')
######
# When you use STS AccessKey credentials to call an API operation, you must add the Sec
urityToken field in the request parameters.
# Example:
# request.add_query_param("SecurityToken", "<yourSecurityToken>");
# Specify your security token.
######
# Optional. Specify the resource set ID.
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID>")
# Required. Specify the organization ID.
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
# Required. Specify the source of the API call.
request.add_header("x-acs-caller-sdk-source","ApiTestDemo")
# Optional. Specify the region ID. This parameter is required if you use Apsara Stack E
nterprise V3.15.0 or earlier. request.add_header("x-acs-regionid", "<yourRegionID>")
# Optional. Specify the instance ID. This parameter is required if you want to modify,
delete, or query an instance.
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
response = client.do_action_with_exception(request) print(str(response, encoding = 'utf-8'))
```

**Example: Call a RESTful API operation**

You must pass parameters in two methods depending on the request method and ContentType value. If the request method is `GET` or `DELETE` , or the ContentType value is `application/x-` `www-form-urlencoded` , use the following method to pass parameters: Python Add the request parameters to the Query section. For example,

```
 request.add_query_param("page_number", "1") .
```

If the request method is `POST` or `PUT` , and the ContentType value is `application/json` , use the following method to pass parameters: Add the request parameters to the Body section. For example:

```
body = '{"page_number":"1",page_size"5":"SecurityToken","":"<yourSecurityToken>"}' request.set_content(body.encode('utf-8'))
```

The following code provides an example of how to call the DescribeClusterV1 operation of Container Service (CS) to obtain the cluster list: In the following sample code, replace the parameters with actual values. Delete the angle brackets (<>) before you submit the code. The following list describes the variables: <yourRegionID>: Replace it with your region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourSecurityToken>: Replace it with your security token. <yourResourceGroupID>: Replace it with your resource set ID. <yourOrganizationID>: Replace it with your organization ID. <yourInstanceID>: Replace it with your instance ID. <cs.aliyuncs.com>: Replace it with the endpoint of the service.

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
######
# API:CS-DescribeClusterV1
######
# Specify the AccessKey ID, AccessKey secret, and region ID.
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('CS') request.set_version('2015-12-15') request.set_uri_pattern('/api/v1/clusters') # Pattern request.set_domain('<cs.aliyuncs.com>') # Specify the endpoint of the service.
# or:
# request = CommonRequest(product='CS', version='2015-12-15',
uri_pattern='/api/v1/clusters', domain='cs.aliyuns.com')
######
# Set the request protocol type. HTTP and HTTPS are supported. The default protocol is
HTTP.
# You can specify HTTPS in the following manner:
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('GET') request.add_header('Content-Type', 'application/json')
# Optional. Specify the resource set ID.
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID")
```

Python

```python
# Required. Specify the organization ID.
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
# Required. Specify the source of the API call.
request.add_header("x-acs-caller-sdk-source","ApiTestDemo")
# Optional. Specify the region ID. This parameter is required if you use Apsara Stack E
nterprise V3.15.0 or earlier. request.add_header("x-acs-regionid", "<yourRegionID>")
# Optional. Specify the instance ID. This parameter is required if you want to modify,
delete, or query an instance.
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
# Business parameters. If the request method is GET or DELETE, or the ContentType value
is application/x-www-form-urlencoded, use the following method to pass data. request.add_query_param("page_number", "1") request.add_query_param("page_size", "5")
######
# When you use STS credentials to call an API operation, you must add the SecurityToken
field in the request parameters.
# Example:
# body = '''{\"SecurityToken\", \"<yourSecurityToken>\"}'''
# Specify your security token.
######
######
# If the request method is POST or PUT, and the ContentType value is application/json,
use the following method to pass data.
# body = '{"page_number":"1",page_size"5":"SecurityToken","":"<your-SecurityToken>"}'
# request.set_content(body.encode('utf-8'))
######
response = client.do_action_with_exception(request) print(str(response, encoding = 'utf-8'))
```

or SDK for Go

## Call examples for SDK for

**Go**

### Getting started

Apsara Stack SDK for Go enables you to access services without complex coding. This topic describes how to obtain and use Apsara Stack SDK for Go.

**Preparations**

An authorized Apsara Stack tenant account and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are required before you can use Apsara Stack SDK for Python. For more information, see Obtain an AccessKey to obtain and view your AccessKey in the Apsara Uni-manager Management Console. The endpoint is obtained. For more information, see Obtain the endpoint of the product.

**Install the core package of Apsara Stack SDK for Go**

Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Use SDK for Go**

The following sample code shows how to use Apsara Stack SDK for Go:
1. Initialize a client instance.
2. Create an API request and configure the required parameters.
3. Initiate the API request and handle the response or exception.
In the following sample code, replace the parameters with actual values based on your business requirements and remove the angle brackets <> from the final code. The following list describes the variables: <yourRegionID>: Replace the variable with the actual region ID. <yourAccessKeyID>: Replace the variable parameter with your AccessKey ID. <yourAccessKeySecret>: Replace <yourAccessKeySecret> with your AccessKey secret. <Endpoint>: Replace the variable parameter with your endpoint. or SDK for Go

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "fmt"
```

`)`

```
func main() {
    // Create an ecsClient instance
    ecsClient, err := ecs.NewClientWithAccessKey(
        "<yourRegionID>",             // Replace with your actual region ID
        "<yourAccessKeyID>",         // Replace with your actual AccessKey ID
        "<yourAccessKeySecret>")        // Replace with your actual AccessKey Secret
    if err != nil {
        // Handle errors
        panic(err)
```

`}`

```
    // Create an API request and configure parameters
    request := ecs.CreateDescribeInstancesRequest()
    // Specify the endpoint of the product
    request.Domain = "<Endpoint>"
    // Set the request.PageSize parameter to 10
    request.PageSize = requests.NewInteger(10)
    // Send the request and handle exceptions
    response, err := ecsClient.DescribeInstances(request)
    if err != nil {
        // Handle exceptions
        panic(err)
```

`}`

```
    fmt.Println(response)
```

`}`
4. (Optional) Switch to HTTP or HTTPS.

```
request.Scheme = "HTTPS"
```

### Use the SDK

#### Install the core package of SDK for Go

This topic describes how to install the core package of SDK for Go. Alibaba Cloud SDK for Go supports Go 1.10.x and later versions. You can install the core package of SDK for Go by executing the following command.

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### Configure identity verification

**credentials**

When using Apsara Stack SDK to access Apsara Stack services, you must provide an authorized account for authentication. or SDK for Go Currently, Go SDK supports authentication through AccessKey. For more information, see Obtain an AccessKey. To use your AccessKey pair to access Apsara Stack, you must specify the AccessKey pair when initializing the client.

**Important**

Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Alibaba Cloud account may be compromised. The following code demonstrates how to initialize an ecsClient instance using ECS as an example.

```
// Initialize an ecsClient instance ecsClient, err := ecs.NewClientWithAccessKey(
        "<yourRegionID>",                 // Replace with your actual region ID
        "<yourAccessKeyID>",             // Replace with your actual AccessKey ID
        "<yourAccessKeySecret>")        // Replace with your actual AccessKey Secret
```

In the preceding sample code, replace the variable parameters with your actual information. Remove the angle brackets (<>) in the final code.

#### Initiate a call

This topic describes how to use Alibaba Cloud product SDK for Go to initiate a call. The following example demonstrates how to use ECS SDK for Go to initiate a request.
1. Import the cloud product SDK.

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/ecs
```

2. Create a client that includes all of the API operations for the product.
In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets (<>) from the final code.

```
ecsClient,err := <ecs>.NewClientWithAccessKey( //Replace with your actual product na
```

`me`

```
    "<yourRegionID>",  // Replace with your actual RegionID
    "<yourAccessKeyID>",  // Replace with your actual AccessKey ID
    "<yourAccessKeySecret>")  // Replace with your actual AccessKey Secret
ecsClient.Domain = "ecs.aliyuns.com" //Set the request domain address. This is an exa mple value. Replace it with the actual request address.
```

3. Use the `xxx.CreateXXXRequest` method to create a request.
The naming convention for this method is ${service}.Create${apiName}Request , where:
**${service}** is the product name (lowercase). For example, ecs.
**${apiName}** is the API name, such as DescribeInstances.

```
request := ecs.CreateDescribeInstanceAttributeRequest() request.InstanceId = ""
```

4. Initiate the call.
or SDK for Go

```
response, err := ecsClient.DescribeInstanceAttribute(request)
```

#### Error handling

When an error occurs on the server side or SDK side, Alibaba Cloud Go SDK returns the corresponding error information through the `ClientError` and `ServerError` types in the `sdk.errors` package. These errors conform to the standard Go error interface and can be handled similarly to standard Go errors.

**Error handling**

You can use the following code to handle errors:

```
response,err := ecsClient.DescribeInstances(request) if err != nil {
    // Obtain error information
   err.Error()
```

`}`

**ClientError**

When any internal SDK call encounters an error that cannot be automatically handled, the SDK returns a `ClientError` . The following example uses ECS to demonstrate how you can identify and obtain error information from a `ClientError` :

**Important**

To use specific error structures, you need to import the error structure package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` . For more information, see:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" // Replace ecs with the n
ame of the actual service.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Error package that is added.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

```
response, err := ecsClient.DescribeInstances(request) if clientError, ok := err.(*errors.ClientError); ok{
    // Obtain the error code
    clientError.ErrorCode()
    // Obtain the error information
    clientError.Message()
    // Obtain the original error. The returned value may be nil.
    clientError.OriginError()
```

`}`

**ServerError**

or SDK for Go When the server returns an error response, the SDK encapsulates this response into a `ServerError` . In this case, you can still obtain the original HTTP response from Response. The following example uses ECS to demonstrate how you can identify and obtain ServerError and error information from Response:

**Important**

To use specific error structures, you need to import the error structure package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` . For more information, see:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" // Replace ecs with the n
ame of the actual service.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Error package that is added.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

```
response, err := ecsClient.DescribeInstances(request) if serverError, ok := err.(*errors.ServerError); ok{
    // Obtain the error code
    serverError.ErrorCode()
    // Obtain the error information
    serverError.Message()
    // Obtain the original HTTP response
    response.GetOriginHttpResponse()
```

`}`

#### Use CommonRequest to call APIs

If you need to call API operations of a cloud service that doesn't provide an SDK, or you cannot use an SDK to call API operations that meet your business requirements, you can use CommonRequest. CommonRequest supports all API operations.

**Example: Call an RPC API operation**

The following code demonstrates how to use CommonRequest to call the DescribeInstanceStatus operation of Elastic Compute Service (ECS) to obtain a list of instance statuses (ECS uses the RPC style): or SDK for Go In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets (<>) from the final code. The following list describes the variables: <yourRegionID>: Replace it with your region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <ecs.aliyuncs.com>: Replace it with the endpoint of the service. <yourSecurityToken>: Replace it with your security token. <yourResourceGroupID>: Replace it with your resource set ID. <yourOrganizationID>: Replace it with your organization ID. <yourInstanceID>: Replace it with your instance ID. or SDK for Go

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "fmt"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey(
        "<yourRegionID>",        //Replace it with your region ID
        "<yourAccessKeyID>",     //Replace it with your AccessKey ID
        "<yourAccessKeySecret>") //Replace it with your AccessKey secret
    if err != nil {
        panic(err)
```

`}`

```
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<ecs.aliyuncs.com>" // Replace it with the endpoint of the servic
```

`e`

```
    request.Product = "Ecs"
    request.Version = "2014-05-26"
    // This is an RPC API operation. Therefore, the ApiName(Action) parameter must be s
pecified
    request.ApiName = "DescribeInstanceStatus"
    // Configure service-related parameters
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
```

`/*`

```
     When you use STS AccessKey credentials to call an RPC API operation, you must add
the SecurityToken field in the request parameters
     Example:
     request.QueryParams["SecurityToken"]="<yourSecurityToken>"
     Replace it with your security token
```

`*/`

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo" // Required. Specify the
call source
    request.Headers["x-acs-regionid"] = "<yourRegionID>" // Optional. Specify your regi
on ID. This parameter is required if you use Apsara Stack Enterprise V3.15.0 or earlier
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // Optional. Spe
cify the resource set ID
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // Required. Speci
fy the organization ID
    // request.Headers["x-acs-instanceid"] = "<yourInstanceID>" // Optional. Specify th
e instance ID. This parameter is required if you want to modify, delete, or query the d etailed information about an instance
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}`

**Example: Call a RESTful API operation**

or SDK for Go You must pass parameters using two methods depending on the request method and ContentType value: If the request method is `GET` or `DELETE` , or the ContentType is `application/x-www-` `form-urlencoded` , use the following method: Place the request parameters in the Query, such as `request.QueryParams["page_number"] =` `"1"` . If the request method is `POST` or `PUT` , and the ContentType is `application/json` , use the following method: Place the request parameters in the Body, for example:

```
body := "{\"page_number\":\"1\",page_size:\"5\"}" request.SetContent([]byte(body)) request.SetContentType("application/json")
```

The following code demonstrates how to use CommonRequest to call the DescribeClusterV1 operation of CS to obtain a list of clusters (CS uses the RESTful style): In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets (<>) from the final code. The following list describes the variables: <yourRegionID>: Replace it with your region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <cs.aliyuncs.com>: Replace it with the endpoint of the service. <yourSecurityToken>: Replace it with your security token. <yourResourceGroupID>: Replace it with your resource set ID. <yourOrganizationID>: Replace it with your organization ID. <yourInstanceID>: Replace it with your instance ID. or SDK for Go

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "fmt"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey(
        "<yourRegionID>",         //Replace it with your region ID
        "<yourAccessKeyID>",      //Replace it with your AccessKey ID
        "<yourAccessKeySecret>")  //Replace it with your AccessKey secret
    if err != nil {
        panic(err)
```

`}`

```
    request := requests.NewCommonRequest()
    request.Method = "GET"
    request.Domain = "cs.aliyuncs.com" // Replace it with the endpoint of the service
    request.Product = "CS"
    request.Version = "2015-12-15"
    // This is a RESTful API. Therefore, the PathPattern field must be specified
    request.PathPattern = "/api/v1/clusters"
    // When you use STS AccessKey credentials to call a ROA API operation, you need to
add the x-acs-security-token field in the header
    // request.Headers["x-acs-security-token"] = "<yourSecurityToken>"
    // Required. Specify the call source
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. Required for Apsara Stack Enterprise V3.15.0 or earlier
    request.Headers["x-acs-regionid"] = "<yourRegionID>"
    // Optional. Replace it with your resource set ID
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>"
    // Required. Replace it with your organization ID
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>"
    // Optional. Required when you want to modify, delete, or view details of a single
instance. Replace it with your instance ID
    // request.Headers["x-acs-instanceid"] = "<yourInstanceID>"
    // Service parameters. When the request method is GET or DELETE, or the ContentType
is application/x-www-form-urlencoded, use the following method to pass data
    // request.QueryParams["page_number"] =  "1"
    // request.QueryParams["page_size"] = "5"
    // When the request method is POST or PUT and the ContentType is application/json,
use the following method to pass data
    // body := "{\"page_number\":\"1\",page_size:\"5\"}"
    // request.SetContent([]byte(body))
    // request.SetContentType("application/json")
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}`

## API reference

### API overview

The following tables list the API operations available for use in Virtual Private Cloud (VPC).

**Dynamic VIP management APIs**

| API | Description |
|---|---|
| ListDynamicVIPs | Obtains dynamic VIP resources. |
| GetDynamicVIP | Obtains details of a dynamic VIP resource. |
| UpdateDynamicVIP | Modifies the status code of a dynamic VIP. |
| DeleteDynamicVIP | Disassociates an EIP from an instance. |
| ListCloudNames | Obtains a list of cloud names. |
| ListCloudRegions | Obtains a list of regions. |
| ListProducts | Obtains a list of products. |
| ListClusters | Obtains a list of clusters. |
| ListServices | Obtains a list of services. |
| ListServerRoles | Obtains a list of service roles. |
| ListApplications | Obtains a list of applications. |
| ListTempVipByNames | Obtains the names of VIPs registered by an application. |
| GetTmplVipDetailByName | Obtains details of VIPs registered by an application. |
| ListSupportIPTypes | Supported types. |

| ListSupportTunnelTypes | Obtains supported tunnel types. |
|---|---|
| CreateDynamicVIP | Creates a dynamic VIP. |
| ListDynamicVipParams | Obtains dynamic VIP parameters. |
| UpdateDynamicVipParams | Updates dynamic VIP parameters. |
| DeleteDynamicVipParams | Deletes dynamic VIP parameters. |
| GetDynamicVipParam | Obtains details of dynamic VIP parameters. |

**Dynamic DNS management APIs**

| API | Description |
|---|---|
| CreateDynamicDns | Creates a dynamic DNS resource. |
| DeleteDynamicDns | Deletes a dynamic DNS resource. |
| UpdateDynamicDns | Updates a dynamic DNS resource (only supports DNS product). |
| ListDynamicDnses | Obtains dynamic DNS resources. |

### Call API operations

#### Request syntax

To send a Virtual Private Cloud (VPC) API request, you must send an HTTP GET request to the VPC endpoint. You must add the request parameters that correspond to the API operation being called. After you call the API, the system returns a response. Requests and responses are encoded in UTF-8. VPC API operations use the RPC protocol. You can call VPC API operations by sending HTTP GET requests. The request syntax is as follows:

```
http://Endpoint/?Action=xx&Parameters
```

In the request,
**Endpoint**: The endpoint of the VPC API is `vpc.example.com` .
`example.com` is a custom domain name. You can obtain the endpoint in the Apsara Stack Operations console. For more information, see Obtain the endpoint of Asapi.
**Action**: the name of the operation being performed. For example, to query created VPC
instances, you must set the Action parameter to DescribeVpcs.
**Version**: the version of the API that you want to use. The current VPC API version is 2016-
04-28.
**Parameters**: the request parameters for the operation. Separate multiple parameters with
ampersands (&). Request parameters include both common parameters and operation-specific parameters. Common parameters are used for all VPC API calls regardless of the operation. For more information, see Common parameters. The following example demonstrates how to call the DescribeVpcs operation. The examples in this topic have been formatted for ease of reading.

```
https://vpc.example.com/?Action=DescribeVpcs &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### API authorization

To ensure the security of your account, we recommend that you call VPC APIs as a RAM user. Before you can use a RAM account to call a VPC API, you must create a RAM account and assign corresponding permissions to it. For more information about VPC resources and APIs you can assign permissions on, see RAM authentication.

#### Signature method

You must sign all API requests to ensure security. Apsara Stack uses the request signature to verify the identity of the API caller. VPC implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Apsara Stack tenant accounts and RAM users that is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to create an AccessKey pair, see Obtain an AccessKey pair. To call an RPC API operation, you must add the signature to the API request in the following format: https://endpoint/?SignatureVersion=1.0 &SignatureMethod=HMAC- SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf Take DescribeVpcs as an example. Assume that the AccessKey ID is `testid` and the AccessKey secret is `testsecret` . The original request URL is as follows:

```
http://vpc.example.com/?Action=DescribeVpcs &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

To calculate the signature, perform the following operations:
1. Use the request parameters to create a query string for signature.

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeVpcs&Format%3DXML&SignatureMethod%3DHMAC- SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f- 4e0ad82fd6cf&SignatureVersion%3D1.0&TimeStamp%3D2016-02- 23T12%253A46%253A24Z&Version%3D2014-05-15
```

2. Calculate the HMAC value of the string you want to sign.
Add an ampersand (&) after the AccessKey secret as the key to calculate the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YGOjuE=
```

3. Add the signature to the request parameters:

```
http://vpc.example.com/?Action=DescribeVpcs &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### RAM authentication

Before calling a VPC API using a RAM user, you must use an Apsara Stack tenant account to create an authorization policy to assign permissions to the RAM user. In the authorization policy, an Alibaba Cloud Resource Name (ARN) is used as the unique identifier of the resource to authorize.

**VPC resources**

The following table lists the VPC resources that can be authorized and their corresponding ARN formats.

| Resource type | ARN format |
|---|---|
| Virtual Private Cloud | acs:vpc:$regionid:$accountid:vpc/$vpcid |
| 0 | > Document Version: 2026082 |

| loud gateway | Developer Guide·API reference |   |
|---|---|---|
| Virtual Private Cloud (VPC) | acs:vpc:$regionid:$accountid:vpc/* acs:vpc:*:$accountid:vpc/* acs:vpc:$regionid:$accountid:vrouter/$vrouterid acs:vpc:$regionid:$accountid:vrouter/* acs:vpc:*:$accountid:vrouter/* acs:vpc:$regionid:$accountid:vswitch/$vswitchid acs:vpc:$regionid:$accountid:vswitch/* acs:vpc:*:$accountid:vswitch/* acs:vpc:$regionid:$accountid:routetable/$routetableid acs:vpc:$regionid:$accountid:routetable/* acs:vpc:*:$accountid:routetable/* acs:vpc:$regionid:$accountid:eip/$allocationid acs:vpc:$regionid:$accountid:eip/* acs:vpc:*:$accountid:eip/* acs:vpc:$regionid:$accountid:natgateway/$natgatewayid acs:vpc:$regionid:$accountid:natgateway/* acs:vpc*:$accountid:vpc/* acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid acs:vpc:$regionid:$accountid:bandwidthpackage/* aacs:vpc:*:$accountid:vpc/* acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid acs:vpc:$regionid:$accountid:forwardtable/* acs:vpc:*:$accountid:vpc/* acs:vpc:$regionid:$accountid:snattable/$snattableid acs:vpc:$regionid:$accountid:snattable/* acs:vpc:*:$accountid:vpc/* |   |
|   | acs:vpc:$regionid:$accountid:vpc/* |   |
|   | acs:vpc:*:$accountid:vpc/* |   |
| VRouter | acs:vpc:$regionid:$accountid:vrouter/$vrouterid |   |
|   | acs:vpc:$regionid:$accountid:vrouter/* |   |
|   | acs:vpc:*:$accountid:vrouter/* |   |
| VSwitch | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |   |
|   | acs:vpc:$regionid:$accountid:vswitch/* |   |
|   | acs:vpc:*:$accountid:vswitch/* |   |
| Routing table | acs:vpc:$regionid:$accountid:routetable/$routetableid |   |
|   | acs:vpc:$regionid:$accountid:routetable/* |   |
|   | acs:vpc:*:$accountid:routetable/* |   |
| Elastic IP Address (EIP) | acs:vpc:$regionid:$accountid:eip/$allocationid |   |
|   | acs:vpc:$regionid:$accountid:eip/* |   |
|   | acs:vpc:*:$accountid:eip/* |   |
| NAT Gateway | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |
|   | acs:vpc:$regionid:$accountid:natgateway/* |   |
|   | acs:vpc*:$accountid:vpc/* |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
| NAT Gateway service plan |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/* |   |
|   | aacs:vpc:*:$accountid:vpc/* |   |
| Forwarding table | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/* |   |
|   | acs:vpc:*:$accountid:vpc/* |   |
| SNAT table | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |
|   | acs:vpc:$regionid:$accountid:snattable/* |   |
|   | acs:vpc:*:$accountid:vpc/* |   |

| General resource | acs:vpc:$regionid:$accountid:* |
|---|---|
|   | acs:vpc:*:$accountid:* |

$regionid/accoutid/vrouterid are IDs of the specific resources, `*` represents all resources.

**VPC API operations**

The following table lists the API operations that can be authorized and their corresponding ARN formats.

| Operation | ARN format |   |   |
|---|---|---|---|
| vpc:CreateVpc | acs:vpc:$regionid:$accountid:vpc/* |   |   |
| vpc:DeleteVpc | acs:vpc:$regionid:$accountid:vpc/$vpcid |   |   |
| vpc:DescribeVpcs | vpc:$regionid:$accountid:vpc/* |   |   |
| vpc:ModifyVpcAttribute | acs:vpc:$regionid:$accountid:vpc/$vpcid |   |   |
|   | acs:vpc:$regionid:$accountid:vrouter/* |   |   |
|   | The VRouter ID is specified: "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |   |   |
|   |   | "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |   |
| vpc:DescribeVRouters |   |   |   |
|   | The VRouter ID is not specified: "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/*" |   |   |
| vpc:ModifyVRouterAttribute | acs:vpc:$regionid:$accountid:vrouter/$vrouterid |   |   |
| vpc:CreateVSwitch | acs:vpc:$regionid:$accountid:vswitch/* |   |   |
|   | acs:vpc:$regionid:$accountid:vpc/$vpcid |   |   |
| vpc:DeleteVSwitch | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |   |   |
| vpc:DescribeVSwitches | acs:vpc:$regionid:$accountid:vswitch/* |   |   |
|   | "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |   |   |
|   |   | "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |   |
| vpc:ModifyVSwitchAttribute | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |   |   |
|   | acs:vpc:$regionid:$accountid:routetable/$routetableid |   |   |
|   |   | acs:vpc:$regionid:$accountid:routetable/$routetableid |   |
| vpc:CreateRouteEntry |   |   |   |
|   | acs:vpc:$regionid:$accountid:routetable/$routetableid |   |   |
|   |   | acs:vpc:$regionid:$accountid:routetable/$routetableid |   |
| vpc:DeleteRouteEntry |   |   |   |
| vpc:DescribeRouteTables | acs:vpc:$regionid:$accountid:routetable/* |   |   |
| 2 | > Document Version: 2026082 |   |   |

| loud gateway | Developer Guide·API referenc |   |   |
|---|---|---|---|
| vpc:DescribeRouteTables |   |   |   |
|   | "vpc:VRouter":"acs:vpc$regionid:$accountid:vrouter/$vr outerid" |   |   |
|   |   | "vpc:VRouter":"acs:vpc$regionid:$accountid:vrouter/$vr |   |
|   | outerid" |   |   |
| vpc:AllocateEipAddress | acs:vpc:$regionid:$accountid:eip/* |   |   |
| vpc:AssociateEipAddres | acs:vpc:$regionid:$accountid:eip/* |   |   |
|   | Bind an ECS instance acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:DescribeEipAddresses | acs:vpc:$regionid:$accountid:eip/* |   |   |
| vpc:UnassociateEipAddress | Bind an ECS instance acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:ReleaseEipAddress | acs:vpc:$regionid:$accountid:eip/$allocationid |   |   |
| vpc:DescribeEipMonitorData | acs:vpc:$regionid:$accountid:eip/$allocationid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:CreateNatGateway | acs:vpc:$regionid:$accountid:natgateway/* |   |   |
|   | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
|   |   | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |
| vpc:DescribeNatGateways |   |   |   |
|   | acs:vpc:$regionid:$accountid:natgateway/* |   |   |
|   | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
|   |   | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |
| vpc:ModifyNatGatewaySpec |   |   |   |
|   | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
|   |   | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |
| vpc:ModifyNatGatewayAttribute |   |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
|   |   | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |
| vpc:DeleteNatGateway |   |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:CreateBandwidthPackage | acs:vpc:$regionid:$accountid:bandwidthpackage/* |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
|   | thpackageid |   |   |
| vpc:DescribeBandwidthPackages |   |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/* |   |   |
| > Document Version: 20260828 | 5 |   |   |

| Developer Guide·API reference |   |   |   |
|---|---|---|---|
|   | cloud gatewa |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| vpc:ModifyBandwidthPackageSpec | thpackageid |   |   |
| vpc:ModifyBandwidthPackageAttrib | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| ute | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| vpc:AddBandwidthPackageIps | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| vpc:RemoveBandwidthPackageIps | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| vpc:DeleteBandwidthPackage | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |   |
| vpc:CreateForwardEntry | eid |   |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |   |
| vpc:DeleteForwardEntry | eid |   |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |   |
| vpc:ModifyForwardEntry | eid |   |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |   |
| vpc:DescribeForwardTableEntries | eid |   |   |
| vpc:CreateSnatEntry | acs:vpc:$regionid:$accountid:snattable/* |   |   |
|   | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |
|   |   | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |
| vpc:ModifySnatEntry |   |   |   |
|   | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |
|   |   | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |
| vpc:DescribeSnatTableEntries |   |   |   |
|   | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |
|   |   | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |
| vpc:DeleteSnatEntry |   |   |   |

### Common parameters

**Common request parameters**

Common request parameters must be included in all API requests. Table 1. Common request parameters

| Name | Type | Requi red | Description |
|---|---|---|---|
| Format | Strin g | No | The type of the return value. Valid value: JSON. |
| Version | Strin g | Yes | The version number of the API. The value is in the YYYY-MM-DD format. Set the value to 2019-05-10. |

| loud gateway |   |   | Developer Guide·API referenc |
|---|---|---|---|

| AccessKeyId | Strin g | Yes | The AccessKey ID that is used to access the service. |
|---|---|---|---|
| AccessKeySe cret | Strin g | Yes | The AccessKey secret that is used to access the service. |
| RegionId | Strin g | Yes | The region ID that is used to access the service. |
| Product | Strin g | Yes | The name of the service to which the operation belongs. |

You can also obtain the `Product` and `Version` parameters required for the API from the Apsara Uni-manager Management Console. To do this, perform the following steps.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Others > API & Tools**.
3. In the left-side navigation pane, click **API Directory**.
4. In the **API Name** text box, enter the operation name to query the operation information.

**Common header parameters**

| Name | Description |
|---|---|
| x-acs-organizationid | The organization ID in the Apsara Uni-manager Management Console. For more information, see Obtain an organization ID. |
| x-acs-resourcegroupid | The resource set ID in the Apsara Uni-manager Management Console. For more information, see Obtain a resource set ID. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. For more information, see Obtain an instance ID. |

When you call API operations of cloud services, you need to add the actual values of the **x-acs-organizationid**, **x-acs-resourcegroupid**, and **x-acs-instanceid** parameters to the request header in your code. These parameters specify the instance ID (the instance ID does not exist when you create an instance or query instance lists), and the organization and resource set to which the instance belongs. If you do not specify the headers when you call an API operation, the system uses the organization and resource set at the root level by default.

**Common response parameters**

API responses use the HTTP response format: A 2xx HTTP status code indicates a successful call. A 4xx or 5xx HTTP status code indicates that the call failed. Responses are returned in the JSON format. Every response returns a unique RequestId regardless of whether the call is successful.

### Dynamic VIP

#### ListDynamicVIPs

Call the ListDynamicVIPs operation to retrieve dynamic VIP resources.

**API description**

When you call this operation, note the following: If you do not specify the Filter parameter, all resources are returned. You can use the filter parameter in JSON to query specific fields. For more information, see the request examples. Paged query is enabled by default.

**Request parameters**

| Name | Type | Requ ired | Example | Description |
|---|---|---|---|---|
| Info | Json | Yes | {key,valu e} | See the description of request parameters below |

**Description of request parameters**

| Name | Type | Req uire d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListDynamicVIPs | The operation that you want to execute. Value: ListDynamicVIPs. |
| PageSize | Integ er | No | 1 | The number of rows per page in a paged query. Maximum value: 50. Default value: 10. |
| PageNumbe r | Integ er | No | 10 | The page number of the list. Default value: 1. |
| Filter | Array | No | [] | See the Filter details below |

**Filter parameters**

| Name | Type | Req uire d | Example | Description |
|---|---|---|---|---|
| Key | String | No | DynVipIp |   |
| Value | Array | No | [ "100.231.244.247 ", "198.146.15.31" ] |   |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 861E6630-AEC0- 4B2D-B214- 6CB5E44B7F04 | The ID of the request. |
| VSwitchId | String | vsw- 25nsdf2aue4g**** | The ID of the vSwitch. |

#### GetDynamicVIP

You can call the GetDynamicVIP operation to obtain dynamic VIP resources.

**Usage notes**

When you call this operation, note the following: You can query dynamic VIP resource instances using the VIP address as a parameter.

**Request parameters**

| Name | Type | Req uire d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetDynamicVIP | The operation that you want to perform. Set the value to GetDynamicVIP. |
| VIP | String | Yes | 172.16.1.2 | The filter conditions. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |
| Application | String | resource init _ | The application. |
| ClusterName | String | Oss2L54Cluster | The name of the cluster. |
| DynVipLbId | String | 171ed137b50-cn- qingdao-env17- d01 825176289 - _ _ 1320843925 | The dynamic VIP LoadBalancer ID. |
| DynVipIp | String | 172.16.1.2 | The VIP. |

| DynVipResour ceId | String | 7b87d5f0b3248d00 7cb8b3c3f32d086a | The VIP resource ID. A dynamic VIP resource has a unique ID that is locally generated by MD5 based on a combination of other fields. |
|---|---|---|---|
| DynVipTunnel Type | String | classic to any tunn _ _ _ el | The tunnel type. Valid values: ['none', 'single tunnel', 'classic to any tunnel', _ _ _ _ 'xregion any tunnel']. _ _ |
| DynVipType | String | internet | The type of the SLB instance. Valid values: internet and intranet. internet: The SLB instance provides only a public IP address. The SLB service can be accessed over the Internet. intranet: The SLB instance provides only a private IP address (or an address in a VPC). The SLB service can be accessed only over the internal network. |
| RegionId | String | cn-hangzhou | The region of the dynamic VIP. |
| RelatedTempl ateResId | String | 047004a37bbc9e9e bf628e2b2a170ab2 6cea65d3 | The res.id of the VIP template. It is a unique value used to distinguish templates. |
| ServerRole | String | TEngine2# | The server role. |
| ServiceName | String | oss-server | The name of the service. |
| VipTemplateN ame | String | oss cluster _ | The name of the VIP template. |
| IntranetDoma in | String | intra.env17e.shugua ng.com | Used to construct the Apsara Infrastructure Management URL. |
| ProductName | String | opsapi | The name of the product. |
| ListenerId | Json | {"80": "8a91b49b7443987 9017447aac23d001 4"} | Used for adaptation layer SDK, modify, and delete interfaces. |
| ServerGroupI d | String | 8a91b49b74439879 017447aac4ae0015 | Used for adaptation layer SDK, modify, and delete interfaces. |
| DynVipStatus | String | 8000 | The status code. |

#### UpdateDynamicVIP

Calls the UpdateDynamicVIP operation to modify the status code of a dynamic virtual IP address (VIP).

**Request parameters**

| Name | Type | Req uire d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateDynamicVI P | The operation that you want to execute. Value: UpdateDynamicVIP. |
| VIP | String | Yes | 172.16.1.2 | The VIP to be modified. |
| DynVipStat us | String | Yes | 8000 | The dynamic VIP status. 8000 indicates normal. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

#### DeleteDynamicVIP

You can call the DeleteDynamicVIP operation to delete a dynamic virtual IP address (VIP) resource.

**Request parameters**

| Name | Type | Req uire d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDynamicVI P | The operation that you want to execute. Value: DeleteDynamicVIP. |
| VIP | String | Yes | 172.16.1.2 | The VIP that you want to delete. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9A572171-4E27- 40D1-BD36- D26C9E71E29E | The ID of the request. |

#### CreateDynamicVIP

You can call the CreateDynamicVIP operation to create a dynamic virtual IP address (VIP) resource.

**After selecting the required parameters, call the**

**CreateDynamicVIP operation. The backend flow:**

1. Obtains template details by calling the Apsara Infrastructure Management.
2. If duplicate fields exist in the frontend data, the frontend data overwrites the Apsara
Infrastructure Management data.
3. Calls the adaptation layer SDK and retrieves the created VIP upon success.
4. Stores the VIP information in the local dynamic_vip_info database.
5. Stores the parameter information associated with the VIP in the local
dynamic_vip_template_parameter database. The dynamic VIP is created successfully.

**Request parameters**

| Name | Type | Req uire d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDynamicVI P | The operation that you want to perform. Set the value to CreateDynamicVIP. |
| ProductNam e | String | Yes | opsapi | The product name. |
| ClusterNam e | String | Yes | Oss2L54Cluster | The cluster name. |
| ServiceNam e | String | Yes | opsapi | The service name. |
| ServiceRole | String | Yes | ApiServer# | The SR name. |
| Application | String | Yes | api-server | The application name. |
| Name | String | Yes | opsapiserver | The template VIP name. |
| Region | String | Yes | cn-qingdao- env17-d01 | The ID of the region. |
| IntranetDo main | String | Yes | http://intra.env17 e.shuguang.com/ | The domain. |

| Ipprotocol | String | Yes | ipv4 | The VIP resource type: ipv4 or ipv6. |
|---|---|---|---|---|
| DynVipType | String | Yes | internet | The type of the SLB instance. Valid values: internet and intranet. internet: The SLB instance provides only a public IP address. The SLB service can be accessed over the Internet. intranet: The SLB instance provides only a private IP address (or an address in the VPC). The SLB service can be accessed only over the internal network. |
| DynVipTunn elType | String | Yes | classic to any tu _ _ _ nnel | The tunnel type. Valid values: none, single tunnel, classic to any tunnel, and _ _ _ _ xregion any tunnel. _ _ |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9A572171-4E27- 40D1-BD36- D26C9E71E29E | The ID of the request. |
| VIP | String | 66.248.51.171 | The created VIP. |

### Dynamic DNS

#### CreateDynamicDns

You can call the CreateDynamicDns operation to create a dynamic DNS resource.

**API description**

You can call the CreateDynamicDns operation to create a dynamic DNS resource.

**Request parameters**

| Name | Type | Req uire d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDynamicDn s | The operation that you want to perform. Set the value to: CreateDynamicDns |
| Region | String | Yes | hangzhou | The region on which your application is deployed. |
| LocalCloudI d | String | Yes |   | The local cloud ID. |

| RemoteClou dId | String | Yes |   | The remote cloud ID. |
|---|---|---|---|---|
| DnsType | String | No | dns product | The DNS type. Valid values: dns product: tenant DNS. ops dns: OPS DNS. |
| DnsRecordT ype | String | Yes | Forward-Zone | The record type. Valid values: [Forward- Zone, A]. OPS DNS corresponds to A record. DNS product corresponds to forward zone. |
| DnsZone | String | No | domain1.com,do main2.com | Fill in when the DNS type is dns product: Multiple zones can be separated by commas, for example: domain1.com,domain2.com. |
| DnsDomain | String | No | asd.inter.env17e. shuguang.com | Fill in when the DNS type is OPS DNS: Enter one DNS domain record, for example: asd.inter.env17e.shuguang.com. Note that the DomainName must be a domain that is already registered in the environment. |
| DnsRecord | String | Yes | 10.0.0.1,10.0.0.2 | Forwarders/Records. Multiple records are separated by commas. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | pc- bp1qrb3044eqixog0 **** | The ID of the request. |
| DnsRecordId | Array | [120,121] | The IDs of the successfully created DNS records. |

#### DeleteDynamicDns

You can call the DeleteDynamicDns operation to delete dynamic DNS resources.

**API description**

Tenant DNS and OPS DNS share the same interface for deletion, distinguished by the DNS type [DnsType] field: DNS product: tenant DNS, ops dns: OPS DNS To delete tenant DNS, the required parameter is DnsRecordId To delete OPS DNS, the required parameters are DnsDomain and DnsRecord

**Request parameters**

| Name | Type | Req uire d | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DeleteDynamicDn s | The operation that you want to execute. Value: DeleteDynamicDns |
|---|---|---|---|---|
| DnsType | String | Yes | dns product | The DNS type. Valid values: dns product: tenant DNS, ops dns: OPS DNS. |
| DnsRecordI d | String | No | 4819 | Required when DnsType is dns product: The DNS record ID. |
| DnsDomain | String | No | domain1.com | Required when DnsType is OPS DNS: The DNS domain. |
| DnsRecord | String | No | 10.0.0.1 | Required when DnsType is OPS DNS: The Forwarders/Records record |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |

#### UpdateDynamicDns

You can call the UpdateDynamicDns operation to modify dynamic DNS resources.

**API description**

This operation supports modifying tenant DNS (DNS product). OPS DNS does not support modification, only addition and deletion.

**Request parameters**

| Name | Type | Req uire d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateDynamicD ns | The operation that you want to perform. Value: UpdateDynamicDns. |
| DnsRecordI d | String | Yes | 4819 | The ID of the DNS record to be modified. |
| RemoteClou dId | String | No | AliDevCloud2 | The remote cloud ID. |
| DnsRecord | String | Yes | 10.0.0.1,10.0.0.2 | Forwarders/Records, multiple records are separated by commas. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2B3670CD-670E- 4540-8C13- 6DE929AEDD3B | The ID of the request. |

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
| AccessKeySecret | String | ****************************************** | The AccessKey secret. |
| SecurityToken | String | ******** | The security token. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Expiration | String | 2015-04- 09T11:52:19Z | The time when the STS token expires. |
| AssumedRoleUser | None | None | The temporary identity that you use to assume the RAM role. |
| Arn | String | acs:ram::12345678 9012****:role/admi nrole/alice | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495** **:alice | The ID of the temporary identity that you use to assume the RAM role. |

**Examples**

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

`}` `}` `}`

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

`}` `}` `}`

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
