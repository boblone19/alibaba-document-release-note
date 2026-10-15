---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Virtual Private Cloud Developer Guide"
product_version: "V3.16.2"
doc_version: "20220916"
pdf_pages: 498
source_pdf: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Virtual Private Cloud Developer Guide 20220916.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.16.2_intl_en/%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97%2B%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20Virtual%20Private%20Cloud%20Developer%20Guide%2020220916.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 Virtual Private Cloud Developer Guide

## Getting started

### Usage notes on development

documentation This topic describes how to view the desired product development documentation when you use Apsara Stack API (ASAPI). Prerequisites The Apsara Stack version is obtained from an O&M personnel or operations administrator. Procedure You can go to the Apsara Stack documentation center and view the desired product documentation.
1. Go to the Apsara Stack Documentation Centerpage by using a browser.
2. Click the Ent erprise, Agilit y, or All-in-one tab based on the Apsara Stack version that you use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the name of the product that you want to view.
5. In the upper-right corner of the product documentation section, click View Det ails or Download PDF.

### Call API operations

Apsara Stack allows you to call API operations by using the Portable OpenAPI Proxy (POP) gateway or the Apsara Stack API (ASAPI) gateway. To ensure that Apsara Stack provides the same experience as the public cloud, API operations in Apsara Stack are called by using the POP gateway by default starting Apsara Stack Enterprise V3.16.0. This topic describes how to use POP Gateway to call Apsara Stack API operations. Not e You can still use the ASAPI gateway to call API operations. For more information, see Call API operations by using the ASAPI gateway, Obtain the endpoint of ASAPI, and Obtain ASAPI SDK. Procedure
1. Obtain an AccessKey pair.
Obtain the AccessKey pair that is required for the API call. For more information, see Obtain an AccessKey pair or Obtain an STS AccessKey pair assigned by STS. Not e We recommend that you use an AccessKey pair or an STS AccessKey 3-tuple of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services.
2. Obtain the region ID.
For more information, see Obtain the values of common header parameters.
3. Obtain the organization ID and resource set ID.
You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrgani zationList in Apsara Uni-manager Management Console Developer Guide. You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourc eGroup in Apsara Uni-manager Management Console Developer Guide. Not e When you call an API operation, set the `<x-acs-organizationid>` parameter to the organization ID that you obtained, and set the `<x-acs-resourcegroupid>` parameter to the resource set ID that you obtained. This way, you can query resources in the specified organization and resource set. If you do not set the `<x-acs-organizationid>` parameter, the organization to which the current user belongs is queried. If you do not set the `<x-acs-resourcegroupid>` parameter, this parameter is left empty by default. If you specify a resource set, you must also specify an organization ID.
4. View the developer guide of the cloud service that you want to use to learn how to make the API call.
For more information about how to view, use, and obtain the developer guide of a specific service, and understand the features and usage methods of operations, see Usage notes.
5. Obtain the endpoint of a cloud service.
6. Obtain the cloud service SDK and call an API operation.

## Preparations

### Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

### View the information about API

operations This topic describes how to view the information about API operations. The information includes service names, API operation names, and API versions. The information is required when you use an SDK to call API operations. Context The API operations on the API Directory page are only for reference. For information about how to call API operations, see developer guides of the corresponding cloud services. If the information on the API Directory page is inconsistent with that in the developer guide of the corresponding cloud service, the information in the developer guide prevails. Procedure
1. Go to the API Tool console. For more information, see Log on to the API Tool console.
2. In the left-side navigation pane, click API Direct ory.
3. On the API Direct ory page, select the service that you want to use from the drop-down list, enter a keyword of
an API operation name in the search box, and then click Search.
4. View and record the service name, API operation name, and API version of the API operation that you want to
call.

### Obtain an AccessKey pair

AccessKey credentials are provided by Resource Access Management (RAM) or Security Token Service (STS). You can use one type of AccessKey credentials for authentication when you call API operations. This topic describes how to obtain an AccessKey pair that is provided by RAM. Context An AccessKey ID and an AccessKey secret are used to implement symmetric encryption and verify the identity of request senders. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. You can use RAM or STS to assign AccessKey credentials: An AccessKey pair that is provided by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An AccessKey 3-tuple that is provided by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an STS AccessKey 3-tuple. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only operations administrators and the administrators of level-1 organizations can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur. Warning The AccessKey pair of a personal account is managed by the permission system of the Apsara Unimanager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region, for example, cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |

| Parameter | Description |
|---|---|
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, click the profile picture and then click User Inf ormat ion.
3. In the AccessKey Pair section, view the AccessKey pair of your account.
Not e An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Organizat ions.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you want to obtain.
5. Click Management Accesskey.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### Obtain an STS AccessKey 3-tuple

This topic describes how to use Security Token Service (STS) to call Apsara Stack API operations. Background information STS allows you to manage temporary credentials to your Apsara Stack resources. You can use STS to call Apsara Stack API operations. An STS AccessKey 3-tuple consists of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to call API operations, you must specify an STS AccessKey 3-tuple. For more information about STS, see What is STS. Procedure
1. Obtain the `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click User Inf ormat ion. iii. Click View Current Role Policy. In the View Policies of Current Role dialog box, view your `RAM role` .
2. Obtain the STS AccessKey 3-tuple.
Not e In the following sample code, replace the parameters with the actual information. Remove the angle brackets (<>) in the final code. The following list describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <yourRoleSessionName>: Replace the parameter with the name of the current session. <yourRoleArn>: Replace the parameter with your RAM role. "sts.aliyuns.com": Replace the parameter with the endpoint of STS.

```java
public static void main(String[] args) {
    // Create a DefaultAcsClient instance and initialize it.
    // Specify the region ID, AccessKey ID, and AccessKey secret.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<your
AccessKeySecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    String assumeRole = callAssumeRole(client);
    if (StringUtils.isEmpty(assumeRole)) return;
    JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
    JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
    // Obtain the STS AccessKey 3-tuple.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace "sts.aliyuns.com" with the endpoint of STS. The format of an STS endpoint is sts-vpc.
${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRoleSessionName>" with the name of the current session.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // Replace "<yourRoleArn>" with the RAM role ARN that is obtained in the previous step.
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

3. Use the STS AccessKey 3-tuple to call an API operation of a cloud service. The following sample code provides
an example on how to call the `DescribeVpcs` operation of Virtual Private Cloud (VPC). Not e In the following sample code, replace the parameters with the actual information. Remove the angle brackets (<>) in the final code. The following list describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourStsAccesskeyID>: Replace the parameter with your STS AccessKey ID. <yourStsAccessKeySecret>: Replace the parameter with your STS AccessKey secret. <yourStsToken>. Replace the parameter with your security token. <yourResourceGroupID>: Replace the parameter with the resource set ID. <yourRegionID>: Replace the parameter with the organization ID.

```
public static void main(String[] args) {
    // Replace "<yourRegionID>" with the region ID.
    // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessKey ID and Acces
sKey secret of the 3-tuple obtained in the previous step.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccesskey>", "<you
rStsAccessSecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    CommonRequest request = new CommonRequest();
    request.setSysDomain("vpc.aliyuns.com");
    request.setSysProduct("vpc");
    request.setSysAction("DescribeVpcs");
    request.setSysVersion("2016-04-28");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRegionID>" with the region ID.
    request.putHeaderParameter("x-acs-regionid", "<yourRegionID>");
    // Replace "<yourStsToken>" with the security token of the 3-tuple obtained in the previous step
```

`.`

```java
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
    // Optional. Replace the parameter with the resource set ID.
    // request.putHeaderParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
    // Required. Replace the parameter with the organization ID.
    request.putHeaderParameter("x-acs-organizationid", "<yourOrganizationID>");
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

### Obtain the values of common headers

You must provide multiple headers when you call Apsara Stack operations. This topic describes the headers and how to obtain the values of the headers. This topic also describes the return values of specific headers after you call Apsara Stack operations. Headers

| T ype | Descript ion |
|---|---|
| x-acs-regionid | The region ID. For more information,see Obtain a region ID. |
| x-acs-organizat ionid | The ID of the organization in the Apsara Uni-manager Management Console. For more information, seeObtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information, see Obtain the ID of a resource set. |
| x-acs-inst anceid | The ID of the instance that you want to manage. For more information, see Obtain an instance ID. |

Obtain a region ID
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Regions.
4. Click the name of the required organization.
5. View the region ID in the Regions window on the right.
Obtain an organization ID You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide. Obtain a resource set ID You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide. Obtain an instance ID You can obtain the ID of an instance in the cloud service console of the Apsara Uni-manager Management Console. For example, to obtain the ID of a virtual private cloud (VPC), perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud.
3. In the left-side navigation pane, click Virt ual Privat e Clouds.
4. View the VPC ID/name in the VPC list.
Response parameters The following additional response parameters are returned by default when you call operations to query the instances of cloud services.

| T ype | Descript ion |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

### Obtain the endpoint of VPC

This topic describes how to obtain the endpoint of Virtual Private Cloud (VPC). Background information To use (Portable OpenAPI Proxy) POP Gateway to call Apsara Stack API operations, you must use a service endpoint. You can obtain a service endpointfrom Apsara Stack onsite O&M engineers. You can also perform the following steps to obtain an endpoint. Procedure
1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose Product s > Plat f orms > Apsara Inf rast ruct ure Management Framework.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for `Registration Vars of Services` and click the report name.
4. On the Regist rat ion Vars of Services page, click the
icon next to Service and search for `VPC` .
5. Find `vpc-yaochi` . Right-click the value in the Service Regist rat ion column and select Show More.
On the Det ails page, view the value of vpc-int ernal.openapi.endpoint . The value indicates the `endpoint` of VPC.

### Obtain VPC SDK

When you call Apsara Stack API operations by using the Portable OpenAPI Proxy (POP) gateway, you must use an SDK of your cloud service. This topic describes how to obtain Virtual Private Cloud (VPC) SDK. Background information To use VPC features, you must install both the VPC SDK and the Alibaba Cloud core library. For example, to use VPC SDK for Java, you must download `aliyun-java-sdk-vpc` and `aliyun-java-sdk-core` . VPC SDK encapsulates the API released on April 28, 2016. The SDK identifies callers based on their AccessKey pairs and provides features such as automatic signing to allow you to create and manage resources by calling API operations. Alibaba Cloud SDK includes code and examples. You can create cloud applications by using an SDK in the programming language that you require. We recommend that you use the SDK core library that is provided on the Alibaba Cloud official website. The SDK core library is applicable to all cloud services and is compatible with Apsara Stack. Instructions Alibaba Cloud SDK supports Java, Python, and Go. You can select an SDK from Alibaba Cloud SDK based on your business requirements. Not e We recommend that you use an SDK for Java, Python, or Go. If you use SDKs in other programming languages, the SDKs may be incompatible with your system. SDK for Java

## Call examples for SDK for Java

### Quick start

This topic describes how to obtain and use Virtual Private Cloud (VPC) SDK for Java. Prerequisites You must have an Apsara Stack tenant account and an AccessKey pair (AccessKey ID and AccessKey secret) to use SDK for Java. For more information, see Obtain an AccessKey pair. Obtain the endpoint of VPC. For more information, see Obtain the endpoint of VPC. To install Alibaba Cloud SDK for Java,you must useJava Development Kit (JDK) 1.8 or later. Install VPC SDK for Java If you use Apache Maven to manage Java projects, you need to only add Maven commands to the pom.xml file of the projects. To use VPC SDK, you must install the SDK core library and VPC SDK. We recommend that you use the core library version 4.5.17 or later, and use the SDK version 3.2.0.

```xml
<dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.5.17</version>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-vpc</artifactId>
            <version>3.2.0</version>
        </dependency>
</dependencies>
```

Use VPC SDK for Java To use VPC SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exceptions.
SDK for Java Not e In the following sample code, replace the parameters with the actual information. Remove the angle brackets (<>) in the final code. The following list describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <Product>: Replace the parameter with the service name. <Endpoint>: Replace the parameter with the endpoint of the service. <readTimeout>: Replace the parameter with a read timeout period based on your business requirements. Unit: milliseconds. <connectionTimeout>: Replace the parameter with a connection timeout period based on your business requirements. Unit: milliseconds. <maxRequestsPerHost>: Replace the parameter with the maximum number of requests that are supported by each host. <maxRequests>: Replace the parameter with the maximum number of requests. <http://192.168.XX.XX:33XX>: Replace the parameter with the IP address and port of the proxy. SDK for Java

```java
import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.vpc.model.v20160428.*; import com.google.gson.Gson; public class Main {
     public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",          // Replace the parameter with the region ID.
            "<yourAccessKeyID>",      // Replace the parameter with your AccessKey ID.
            "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey secret.
        // Replace the parameter with the endpoint of the service.
        profile.addEndpoint("<yourRegionID>", "<Product>", "<Endpoint>");
        // Set the request configuration.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);// Ignore the certificate.
        clientConfig.setReadTimeoutMillis(<readTimeout>);// Optional. Set the read timeout period. U
nit: milliseconds.
        clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);// Optional. Set the connection
timeout period. Unit: milliseconds.
        clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);// Optional. Set the maximum number
of requests for each host.
        clientConfig.setMaxRequests(<maxRequests>);// Optional. Set the maximum number of requests.
        clientConfig.setProtocolType(ProtocolType.HTTP); // Optional. Set the request protocol. Defa
ult value: HTTP.
        /* Optional. Set the proxy IP address and port.
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`or`

```
        clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>");
```

`*/`

```java
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set the parameters.
        DescribeVpcsRequest request = new DescribeVpcsRequest();
        // Set service-related parameters.
        request.setPageSize(10);
        request.setPageNumber(1);
        // Specify the organization ID and resource set ID to query specified resources.
        request.putHeaderParameter("x-acs-organizationid", "1");
        request.putHeaderParameter("x-acs-resourcegroupid", "11");
        // Send the request and handle the response or exception.
        DescribeVpcsResponse response;
       try {
            DescribeVpcsResponse response = client.getAcsResponse(request);
            System.out.println(new Gson().toJson(response));
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

SDK for Java

### Use SDK

#### Install VPC SDK for Java

This topic describes how to install and use Virtual Private Cloud (VPC) SDK for Java. Alibaba Cloud SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Alibaba Cloud SDK for Java by adding Maven dependencies or downloading Alibaba Cloud SDK. To use VPC SDK, you must install the core library of Alibaba Cloud SDK for Java and VPC SDK for Java. We recommend that you use the core library version 4.5.17 or later, and use VPC SDK for Java 3.2.0. To use VPC SDK for Java, you must install the core library of Alibaba Cloud SDK for Java and add the following dependencies to the pom.xml file. For more information about the specific SDK version, see Alibaba Cloud SDK.

```xml
<dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.5.17</version>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-vpc</artifactId>
            <version>3.2.0</version>
        </dependency>
</dependencies>
```

#### Configure authentication credentials

When using Alibaba Cloud SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. SDK for Java supports authentication through an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Alibaba Cloud, you must configure the AccessKey pair as a credential when you initialize the client. Not e Do not disclose any code that may contain your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",          // Replace the parameter with the region ID.
    "<yourAccessKeyID>",      // Replace the parameter with your AccessKey ID.
    "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey secret.
```

Not e In the preceding sample code,replace the parameterswith the actual information. Remove the angle brackets (<>) in the final code.

#### Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. SDK for Java You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements. Not e You must use actual values to replace the variables in the following sample code. Do not retain the angle brackets (<>) in the final code. The following list describes the variables: <readTimeout>: Specify the read timeout period based on your business requirements. Unit: milliseconds. <connectionTimeout>: Specify the connection timeout period based on your business requirements. Unit: milliseconds. <maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER. <maxRequests>: Specify the maximum number of requests based on your business requirements. The supported data type is INTEGER. <http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy.

```
// Obtain the HttpClientConfig object. HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Specify whether to ignore certificates. clientConfig.setIgnoreSSLCerts(true); // (Optional) Specify the read timeout period. Unit: milliseconds. clientConfig.setReadTimeoutMillis(<readTimeout>); // (Optional) Specify the connection timeout period. Unit: milliseconds. clientConfig.setConnectionTimeoutMillis(<connectionTimeout>); // (Optional) Specify the maximum number of requests that are supported by each server. The supported da ta type is INTEGER. clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>); // (Optional) Specify the maximum number of requests. The supported data type is INTEGER. clientConfig.setMaxRequests(<maxRequests>); // (Optional) Specify the protocol type. clientConfig.setProtocolType(ProtocolType.HTTP); /** (Optional) Specify whether to configure the proxy based on your business requirements. The following code is available: clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
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

This topic describes how to use Virtual Private Cloud (VPC) SDK for Java to initiate a request. Procedure
1. Create an AcsClient instance.

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
Name the request in the following format: ${apiName}Request . Replace ${apiName} with the API name, for example, DescribeVpcs. SDK for Java When multiple service SDKs are used, different requests may have the same name. You can differentiate the requests based on package names.

```
DescribeVpcsRequest request = new DescribeVpcsRequest(); // Set service-related parameters. request.setPageSize(10); request.setPageNumber(1); // Specify the organization ID and resource set ID to query specified resources. request.putHeaderParameter("x-acs-organizationid", "1"); request.putHeaderParameter("x-acs-resourcegroupid", "");
```

3. Initiate the request and handle the response.

```java
DescribeVpcsResponse response; try {
  DescribeVpcsResponse response = client.getAcsResponse(request);
  System.out.println(new Gson().toJson(response));
} catch (ServerException e) {
    e.printStackTrace();
} catch (ClientException e) {
    e.printStackTrace();
```

In normal cases, all returned fields are deserialized into the response. You can directly use `response.getXXX()` to obtain the response fields.

```
instanceStatus := response.getStatus()
```

If an exception occurs or you need the original HTTP response, use `doAction()` to obtain the original response.

```
HttpResponse response = client.doAction(request);
```

#### Handle errors

If an error occurs on the server side or SDK side, the Apsara Stack Java SDK returns the corresponding exception message. An exception message contains the detailed error information, namely the error code and the error message. Generally, you are not required to handle the errors returned by the Apsara Stack Java SDK. You are only required to handle the errors on the server side according to the error message. `ServerException` is the error message on the server side. `ClientException` is the error message on the SDK side. For example, if the following error occurs, modify the ID of AccessKey according to the detailed error message.

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found
```

`.` To handle the errors returned by the Apsara Stack Java SDK, see the following code example for reference: SDK for Java

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handle the response.
    // ...
}catch (ServerException e){
    // Add your own error handling logic here.
    // For example, print the detailed error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If the problem is tricky, open a ticket and provide the RequestId for us.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // Add your own error handling logic here.
    // For example, print the detailed error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

#### Use CommonRequest to call API operations

If you want to call the API operations of a cloud service that does not provide SDKs, or you cannot use an SDK to call API operations whose requests and responses meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations. Characteristics of CommonRequest calling The CommonRequest calling method has the following characteristics: Light weight: You only need the core package to initiate the call, without downloading or installing the SDK of each product. Easy and convenient: You can call the latest API without updating the SDK. Fast iteration Use CommonRequest to call API operations If you want to send a CommonRequest request, you must obtain the values of the following parameters: You can obtain the values of these parameters from the API references. Domain: the endpoint of the service. Version: the version of the API in the YYYY-MM-DD format. You can obtain the API version from the sections about common parameters in the API references. Operation information: the name of the API operation that you want to call. You must obtain the value of the Action parameter and specify an API operation in `request.setSysAction("<Acti` `on>")` . For example, if you want to call the DescribeVpcs operation, you must use `request.setSysAction("DescribeVpcs"` `)` to specify the API operation when you initiate a CommonRequest request. Example: Call an RPC API operation The following code provides an example of how to call the `DescribeVpcs` operation to query virtual private clouds (VPCs). VPC API operations are RPC operations. SDK for Java Not e In the following sample code, replace the parameters with the actual information. Remove the angle brackets (<>) in the final code. The following list describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <yourSecurityToken>: Replace the parameter with your security token. <yourResourceGroupID>: Replace the parameter with the resource set ID. <yourOrganizationID>: Replace the parameter with the organization ID. <yourInstanceID>: Replace the parameter with the instance ID. <http://192.168.XX.XX:33XX>: Replace the parameter with the IP address and port of the proxy.

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionUD>",          // Replace the parameter with the region ID.
            "<yourAccessKeyID>",      // Replace the parameter with your AccessKey ID.
            "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey secret.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /**
        Optional. Configure the HTTP proxy based on your business requirements.
        Format:
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
        Specify the IP address and port of the proxy.
```

`*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set the parameters.
        CommonRequest request = new CommonRequest();
        // Specify the endpoint of the service.
        request.setSysDomain("vpc.aliyuncs.com");
        request.setSysProduct("Vpc");
        request.setSysVersion("2016-04-28");
        request.setSysAction("DescribeVpcs");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// Optional. Specify
the resource set ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// Required. Specify th
e organization ID.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// Optional. Specify the region ID.
If you use Apsara Stack Enterprise V3.15.0 or earlier versions, this parameter is required.
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// Optional Specify the inst
ance ID. This parameter is required when you want to delete, modify, or query an instance.
        /**
```

SDK for Java

```
        When you use STS AccessKey credentials to call an API operation, you must add the SecurityToken
field in the request parameters.
        Format:
        request.putQueryParameter("SecurityToken", "<yourSecurityToken>");
        Specify your security token.
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

SDK for Python

## Call examples for SDK for Python

### Quick start

This topic describes how to obtain and use Virtual Private Cloud (VPC) SDK for Python. Prerequisites You must have an Apsara Stack tenant account and an AccessKey pair (AccessKey ID and AccessKey secret) to use VPC SDK for Python. For more information, see Obtain AccessKey credentials. Obtain the endpoint of VPC. For more information, see Obtain the endpoint of VPC. Install VPC SDK for Python
1. Install the SDK core library.
If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-core-v3
```

2. Install VPC SDK for Python.
The following examples describe how to install VPC SDK for Python: If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-vpc
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-vpc
```

Use VPC SDK for Python To use VPC SDK for Python, perform the following steps:
1. Create a client instance. When you create a client, you must specify a region ID, an AccessKey ID, and an
AccessKey secret.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exceptions.
Not e In the following sample code, replace the parameters with the actual information. Remove the angle brackets (<>) in the final code. The following list describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <vpc.aliyuns.com>: Replace the parameter with the service endpoint. SDK for Python

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkvpc.request.v20160428 import DescribeVpcsRequest
# global config
region_id = '<yourRegionID>' # Specify the region ID. access_key = '<yourAccessKeyID>' # Specify the AccessKey ID. acces_secret = '<yourAccessKeySecret>' # Specify the AccessKey secret.
# product config
product_name = 'Vpc' # Specify the service name. endpoint = '<vpc.aliyuns.com>' # Specify the endpoint of the service.
# create client
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, acces_secret, region_id)
# setup request
request = DescribeVpcsRequest.DescribeVpcsRequest() request.set_accept_format('json') # Specify the response format.
# get response
response = clt.do_action_with_exception(request) print response # If you use Python 3.x, the default value is print (response).
```

### Use SDK

#### Install VPC SDK for Python

This topic describes how to install and use Virtual Private Cloud (VPC) SDK for Python. Apsara Stack SDK for Python supports Python 2.6.x, Python 2.7.x, and Python 3.x or later. You can install Apsara Stack SDK for Python by using pip. Not e To use the SDK of a cloud service, you must install the SDK core library for Python. For example, if you want to use VPC SDK for Python, you must install the SDK core library for Python and VPC SDK for Python. If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-core-v3
```

The following example describes how to install VPC SDK. If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-vpc
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-vpc
```

#### Configure authentication credentials

When using Alibaba Cloud SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. SDK for Python supports authentication through an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain AccessKey credentials. SDK for Python If you want to use your AccessKey pair to access Alibaba Cloud, you must configure the AccessKey pair as a credential when you initialize the client. Not ice Do not disclose any code that may contain your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

#### Set HTTPS requests

The Python SDK supports using HTTP and HTTPS to initiate API requests. When using the Python SDK, you can specify a protocol (HTTP or HTTPS) for a specific request to use, or set a global default protocol for all requests to use. Not e The default protocol (HTTP or HTTPS) of a product takes precedence over the global default protocol you set. Add OpenSSL dependency HTTPS of the Python SDK depends on the OpenSSL support in Python. To use Alibaba Cloud SDK to send HTTPS requests, you must add OpenSSL support in Python.

| Run the | python -c "import ssl" | co |
|---|---|---|
| ImportError: No module named ssl |   |   |

Run the `python -c "import ssl"` command to check if the Python environment supports OpenSSL. If the `ImportError: No module named ssl` error message does not appear, OpenSSL is supported in Python. If Python does not support OpenSSL, run the following command to install OpenSSL:

```
pip install pyopenssl
```

Set HTTP/HTTPS for a request See the following code example for reference to set the HTTPS call for an API:

```bash
request = CreateInstanceRequest.CreateInstanceRequest() request.set_protocol_type("https")
# Value: "https" or "http"
```

Set global default protocol for all requests See the following code example for reference to set the global default protocol for all requests:

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request.
```

#### Initiate a request

This topic describes how to use Virtual Private Cloud (VPC) SDK for Python to initiate a request. Procedure
1. Import the VPC SDK.

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkvpc.request.v20160428 import DescribeVpcsRequest
```

SDK for Python
2. Create an AcsClient instance.

```
client.region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, access_secret, region_id)
```

3. Create a request object.

```
request = DescribeVpcsRequest.DescribeVpcsRequest() request.set_accept_format('json')
```

4. Initiate the request and process the response.

```
response = clt.do_action_with_exception(request) print response # If you use Python 3.x, the default value is print (response).
```

#### Handle errors

If an error occurs on the server side or SDK side when you use the Python SDK, the Python SDK returns the corresponding exception message. An exception message contains the detailed error information, namely the error code and the error message. Generally, you are not required to handle the errors returned by the Python SDK. You are only required to handle the errors on the server side according to the error message. `ServerException` is the error message on the server side. `ClientException` is the error message on the SDK side. For example, if the following error occurs, modify the ID of AccessKey according to the detailed error message.

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFo und Specified access key is not found.
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

#### Use CommonRequest to call API operations

If you want to call the API operations of a cloud service that does not provide SDKs, or you cannot use an SDK to call API operations whose requests and responses meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations. Characteristics of CommonRequest calling The CommonRequest calling method has the following characteristics: Light weight: You only need the core package to initiate the call, without downloading or installing the SDK of each product. Easy and convenient: You can call the latest API without updating the SDK. Fast iteration Use CommonRequest to call API operations SDK for Python If you want to send a CommonRequest request, you must obtain the values of the following parameters: You can obtain the values of these parameters from the API references. Domain: the endpoint of the service. Version: the version of the API in the YYYY-MM-DD format. You can obtain the API version from the sections about common parameters in the API references. Operation information: the name of the API operation that you want to call. To call an RPC API operation: You must obtain the value of the Action parameter and use `request.set_action_name('Action')` to specify the API operation. For example, if you want to call the DescribeVpcs operation, you must use `request.set_action_name('DescribeVp` `cs')` to specify the API operation when you initiate a CommonRequest request. Example: Call an RPC API operation The following code provides an example of how to call the `DescribeVpcs` operation to query virtual private clouds (VPCs). VPC API operations are RPC operations. Not e In the following sample code, replace the parameters with the actual information. Remove the angle brackets (<>) in the final code. The following list describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <yourSecurityToken>: Replace the parameter with your security token. <yourResourceGroupID>: Replace the parameter with the resource set ID. <yourOrganizationID>: Replace the parameter with the organization ID. <yourInstanceID>: Replace the parameter with the instance ID. <vpc.aliyuncs.com>: Replace the parameter with the endpoint of the service. SDK for Python

```python
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
# Specify the AccessKey ID, the AccessKey secret, and the region ID.
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('Vpc') request.set_action_name('DescribeVpcs') request.set_version('2016-04-28') request.set_domain('<vpc.aliyuncs.com>') # Specify the endpoint of the service.
# or:
# request = = CommonRequest(product='Vpc', action_name='DescribeVpcs',version='2016-04-28',domain='vpc.a
liyuncs.com')
######
# Specify the request protocol. Valid values: https and http. Default value: http.
# You can specify HTTPS as the protocol in the following manner:
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30')
######
# When you use an STS AccessKey 3-tuple to call an API operation, you must add the SecurityToken field i
n the request parameters.
# Format:
# request.add_query_param("SecurityToken", "<yourSecurityToken>");
# Specify your security token.
######
# Optional. Specify the resource set ID.
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID>")
# Required. Specify the organization ID.
request.add_header("x-acs-caller-sdk-source","ApiTestDemo")
# Optional. Specify the region ID. This parameter is required if you use Apsara Stack Enterprise V3.15.0
or earlier. request.add_header("x-acs-regionid", "<yourRegionID>")
# Optional. Specify the instance ID. This parameter is required if you want to modify, delete, or query
an instance.
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
response = client.do_action_with_exception(request) print(str(response, encoding = 'utf-8'))
```

SDK for Go

## Call examples for SDK for Go

### Quick start

Alibaba Cloud SDK for Go allows you to access services without complex coding. This topic describes how to obtain and use Virtual Private Cloud (VPC) SDK for Go. Prerequisites You must have an Apsara Stack tenant account and an AccessKey pair (AccessKey ID and AccessKey secret) to use VPC SDK. For more information, see Obtain an AccessKey pair. Obtain the endpoint of VPC. For more information, see Obtain the endpoint of VPC. Install the core package of Alibaba Cloud SDK for Go Alibaba Cloud SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package: You can check whether the latest version of the core package is installed on the Alibaba Cloud SDK for Go page.

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

Usage The following sample code shows you how to use Alibaba Cloud SDK for Go:
1. Initialize a client instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exceptions.
Not e In the following sample code, replace the parameters with the actual information. Remove the angle brackets (<>) in the final code. The following list describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <Endpoint>: Replace the parameter with the endpoint. SDK for Go

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/vpc"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "fmt"
```

`)`

```
func main() {
    // Create a vpcClient instance.
    vpcClient, err := vpc.NewClientWithAccessKey(
        "<yourRegionID>",             // Replace the parameter with the region ID.
        "<yourAccessKeyID>",         // Replace the parameter with your AccessKey ID.
        "<yourAccessKeySecret>")        // Replace the parameter with your AccessKey secret.
    if err != nil {
        // Handle exceptions.
        panic(err)
    // Create a request and set the required parameters.
    request := vpc.CreateDescribeVpcsRequest()
    // Specify the endpoint of the service.
    request.Domain = "<Endpoint>"
    // Set request.PageSize to 10.
    request.PageSize = requests.NewInteger(10)
    // Initiate the request and handle exceptions.
    response, err := vpcClient.DescribeVpcs(request)
    if err != nil {
        // Handle exceptions.
        panic(err)
    fmt.Println(response)
```

4. Optional. Switch to HTTP or HTTPS.

```
request.Scheme = "HTTPS"
```

### Use SDK

#### Install Go SDK

This topic describes how to install the Go SDK. The Alibaba Cloud Go SDK supports Go 1.7 or later versions. Install the Go SDK manually.
1. Download the source code of the Go SDK from the official site of Apsara Stack.
2. Extract the package to the directory where the GO_PATH file of the current user resides.

#### Configure authentication credentials

When using Alibaba Cloud SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. SDK for Go supports authentication through an AccessKey pair. For more information, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as the credentials when you initialize the client. Not ice Do not disclose any code containing your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised. The following code provides an example to show how to initialize a vpcClient instance. SDK for Go

```
// Initialize a vpcClient instance. vpcClient, err := vpc.NewClientWithAccessKey(
        "<yourRegionID>",                 // Replace the parameter with the region ID.
        "<yourAccessKeyID>",             // Replace the parameter with your AccessKey ID.
        "<yourAccessKeySecret>")        // Replace the parameter with your AccessKey secret.
```

Not e In the preceding sample code, replace the parameters with the actual information. Delete the angle brackets (<>) in the final code.

#### Initiate a request

This topic describes how to use Virtual Private Cloud (VPC) SDK for Go to initiate a request. The following example shows how to use VPC SDK for Go to initiate a request.
1. Import VPC SDK for Go.

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/vpc
```

2. Create a VPC client. The client includes all APIs of the VPC.
Not e In the following sample code, replace the parameters with the actual information. Delete the angle brackets (<>) in the final code.

```
vpcClient,err := <vpc>.NewClientWithAccessKey( //Replace the parameter with the name of the service
```

`.`

```
    "<yourRegionID>",  // Replace the parameter with the region ID.
    "<yourAccessKeyID>",  // Replace the parameter with your AccessKey ID.
    "<yourAccessKeySecret>")  // Replace the parameter with your AccessKey secret.
vpcClient.Domain = "vpc.aliyuns.com" //Specify the endpoint of the service.
```

3. Use the `xxx.CreateXXXRequest` method to create a request.
Specify the name in ${service}.Create${apiName}Request format. ${service} specifies the service name in lowercase, such as vpc. ${apiName} is the API name, such as DescribeVpcs.

```
request := vpc.CreateDescribeVpcsRequest() request.InstanceId = ""
```

4. Initiate a request.

```
response, err := vpcClient.DescribeVpcs(request)
```

#### Troubleshooting

When you use Alibaba Cloud SDK for Go, a `ClientError` or a `ServerError` is returned when an error occurs on the server side or on the SDK side. Both error types are included in `sdk.errors` . The errors conform to the standard Go error interface, so they can be handled in a similar way as standard Go errors. Handle errors You can use the following code to handle errors: SDK for Go

```
response,err := vpcClient.DescribeVpcs(request) if err != nil {
    // Obtain the error information.
   err.Error()
```

ClientError When you send a request, if an error occurs in the SDK and cannot be automatically handled, the SDK returns a

```
 ClientError .
```

The following code shows how to determine and obtain the error message in a `ClientError` of Virtual Private Cloud (VPC) SDK for Go: Not ice When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-` `cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/vpc" // Replace vpc with the name of the servic
```

`e.`

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // The error package that you want to add.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

```
response, err := vpcClient.DescribeVpcs(request) if clientError, ok := err.(*errors.ClientError); ok{
    // Obtain the error code.
    clientError.ErrorCode()
    // Obtain the error message.
    clientError.Message()
    // Obtain the original error. The return value may be nil.
    clientError.OriginError()
```

ServerError When the server returns an error message, the SDK wraps the message into a `ServerError` and returns it to the client. In this case, you can still obtain the original HTTP response from the response. The following code shows how to determine and obtain the error message in a server error and response of VPC SDK for Go: SDK for Go Not ice When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-` `cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/vpc" // Replace vpc with the name of the servic
```

`e.`

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // The error package that you want to add.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

```
response, err := vpcClient.DescribeVpcs(request) if serverError, ok := err.(*errors.ServerError); ok{
    // Obtain the error code.
    serverError.ErrorCode()
    // Obtain the error message.
    serverError.Message()
    // Obtain the original HTTP response.
    response.GetOriginHttpResponse()
```

#### Use CommonRequest to call API operations

If you want to call the API operations of a cloud service that does not provide SDKs, or you cannot use an SDK to call API operations whose requests and responses meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations. Example: Call an RPC API operation The following code provides an example of how to call the `DescribeVpcs` operation to query virtual private clouds (VPCs). VPC API operations are RPC operations. Not e In the following code, replace the parameters with the actual information. Delete the angle brackets (<>) in the final code. The following section describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <vpc.aliyuncs.com>: Replace the parameter with the endpoint of the service. <yourSecurityToken>: Replace the parameter with your security token. <yourResourceGroupID>: Replace the parameter with the resource set ID. <yourOrganizationID>: Replace the parameter with the organization ID. <yourInstanceID>: Replace the parameter with the instance ID. SDK for Go

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
        "<yourRegionID>",        //Replace the parameter with the region ID.
        "<yourAccessKeyID>",     //Replace the parameter with the AccessKey ID.
        "<yourAccessKeySecret>") //Replace the parameter with your AccessKey secret.
    if err != nil {
        panic(err)
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<vpc.aliyuncs.com>" // Replace the parameter with the endpoint of the service.
    request.Product = "Vpc"
    request.Version = "2016-04-28"
    // This is an RPC API operation. Therefore, the APIName(Action) parameter must be specified.
    request.ApiName = "DescribeVpcs"
    // Configure service-related parameters.
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
```

`/*`

```
     When you use STS AccessKey credentials to call an RPC API operation, you must add the SecurityToken
field in the request parameters.
     Format:
     request.QueryParams["SecurityToken"]="<yourSecurityToken>"
     Specify your security token.
```

`*/`

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo" // Required. Specify the source of the ca
ll.
    request.Headers["x-acs-regionid"] = "<yourRegionID>" // Optional. Specify your region ID. This param
eter is required if you use Apsara Stack Enterprise V3.15.0 or earlier.
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // Optional. Specify the resource
set ID.
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // Required. Specify the organizati
on ID.
    // request.Headers["x-acs-instanceid"] = "<yourInstanceID>" // Optional. Specify the instance ID. Th
is parameter is required if you want to modify, delete, or query an instance.
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    fmt.Print(response.GetHttpContentString())
```

## API reference

### Overview

The following tables list the API operations available for use in Virtual Private Cloud (VPC). VPC management

| API | Description |
|---|---|
| CreateVpc | Creates a VPC. |
| DeleteVpc | Deletes a VPC. |
| ModifyVpcAttribute | Modifies the name and description of a VPC. |
| DescribeVpcs | Queries VPCs. |
| AssociateVpcCidrBlock | Adds a secondary IPv4 CIDR block to a VPC. |
| UnassociateVpcCidrBlock | Deletes a secondary IPv4 CIDR block from a VPC. |

vSwitch management

| API | Description |
|---|---|
| CreateVSwitch | Creates a vSwitch. |
| DeleteVSwitch | Deletes a vSwitch. |
| ModifyVSwitchAttribute | Modifies the name and description of a vSwitch. |
| DescribeVSwitches | Queries vSwitches. |

vRouter management

| API | Description |
|---|---|
| ModifyVRouterAttribute | Modifies the name and description of a vRouter. |
| DescribeVRouters | Queries vRouters in a specified region. |

Route table management

| API | Description |
|---|---|
| CreateRouteTable | Creates a custom route table. |
| CreateRouteEntry | Creates a custom route entry in the vRouter or virtual border router (VBR) of a VPC. |
| DeleteRouteEntry | Deletes a custom route entry. |
| DescribeRouteEntryList | Queries route entries. |
| ModifyRouteEntry | Modifies the name and description of a custom route entry. |

| Developer Guide·API reference | Virtual Private Clou |
|---|---|

| API | Description |
|---|---|
| AssociateRouteTable | Associates a custom route table with a vSwitch in the same VPC. |
| DeleteRouteTable | Deletes a custom route table. |
| DescribeRouteTableList | Queries route tables. |
| UnassociateRouteTable | Disassociates a route table from a vSwitch. |

Region management

| API | Description |
|---|---|
| DescribeRegions | Queries available regions. |
| DescribeZones | Queries zones in a specified region. |

Tag management

| API | Description |
|---|---|
| TagResources | Creates and adds tags to a specified resource. |
| ListTagResources | Queries tags that are added to instances. |
| UnTagResources | Removes tags from a specified resource. |

BGP API

| API | Description |
|---|---|
| DescribeBgpGroups | Queries Border Gateway Protocol (BGP) groups in a specified region. |
| ModifyBgpGroupAttribute | Modifies configurations of BGP groups. |
| DeleteBgpGroup | Deletes a specified BGP group. |
| DescribeBgpPeers | Queries BGP peers in a specified region. |
| DeleteBgpPeer | Deletes a specified BGP peer. |
| AddBgpNetwork | Advertises BGP networks. |
| DeleteBgpNetwork | Deletes advertised BGP networks. |
| DescribeBgpNetworks | Queries advertised BGP networks. |

VBR management

| API | Description |
|---|---|
| CreateVirtualBorderRouter | Creates a VBR. |
| DeleteVirtualBorderRouter | Deletes a VBR. |

| Virtual Private Cloud | Developer Guide·API referenc |
|---|---|

| API | Description |
|---|---|
| DescribeVirtualBorderRouters | Queries VBRs. |
| TerminateVirtualBorderRouter | Disables a VBR. |
| RecoverVirtualBorderRouter | Enables a disabled VBR. |
| UnassociatePhysicalConnectionFromVirtualBorderRouter | Disassociates a VBR from an Express Connect circuit. |

Express Connect management

| API | Description |
|---|---|
| CancelPhysicalConnection | Cancels an Express Connect circuit before it is enabled. After you perform this operation, the Express Connect circuit enters the Canceled state. |
| DescribePhysicalConnections | Queries Express Connect circuits in a specified region. |
| ModifyPhysicalConnectionAttribute | Modifies the configuration of an Express Connect circuit. |
| TerminatePhysicalConnection | Disables an Express Connect circuit after it is enabled. |
| EnablePhysicalConnection | Enables an Express Connect circuit that is in the Confirmed state. After you perform this operation, the Express Connect circuit enters the Enabled state. |
| DeletePhysicalConnection | Deletes an Express Connect circuit. |
| CreatePhysicalConnectionOccupancyOrder | Creates an order for resource occupation. |
| ApplyPhysicalConnectionLOA | Applies for a letter of authorization (LOA). |
| CreatePhysicalConnectionSetupOrder | Creates an order for initial installation. |
| CompletePhysicalConnectionLOA | Completes construction. |
| DescribePhysicalConnectionLOA | Queries LOA information about an Express Connect circuit. |

VPN Gateway management

| API | Description |
|---|---|
| CreateVpnGateway | Creates a VPN gateway. |
| DescribeVpnGateways | Queries VPN gateways. |
| DescribeVpnGateway | Queries detailed information about a specified VPN gateway. |
| DeleteVpnGateway | Deletes a specified VPN gateway. |
| ModifyVpnGatewayAttribute | Modifies the name and description of a VPN gateway. |
| CreateCustomerGateway | Creates a customer gateway. |
| DescribeCustomerGateways | Queries customer gateways. |
| DescribeCustomerGateway | Queries details about a customer gateway. |

| Developer Guide·API reference | Virtual Private Clou |
|---|---|

| API | Description |
|---|---|
| DeleteCustomerGateway | Deletes a specified customer gateway. |
| ModifyCustomerGatewayAttribute | Modifies the name and description of a customer gateway. |
| DeleteVpnPbrRouteEntry | Deletes a policy-based route entry of a VPN gateway. |
| DeleteVpnRouteEntry | Deletes a destination-based route entry of a VPN gateway. |
| DescribeVpnRouteEntries | Queries detailed information about destination-based route entries of a VPN gateway. |
| ModifyVpnRouteEntryWeight | Modifies the weight of a destination-based route entry of a VPN gateway. |
| CreateVpnRouteEntry | Creates a destination-based route entry for a VPN gateway. |
| ModifyVpnPbrRouteEntryWeight | Modifies the weight of a policy-based route entry of a VPN gateway. |
| DescribeVpnPbrRouteEntries | Queries detailed information about policy-based route entries of a VPN gateway. |
| PublishVpnRouteEntry | Advertises a route entry of a VPN gateway to a VPC. |
| CreateVpnPbrRouteEntry | Creates a policy-based route entry for a VPN gateway. |
| DescribeVpnConnection | Queries details about an IPsec-VPN connection. |
| DeleteVpnConnection | Deletes a specified IPsec-VPN connection. |
| DownloadVpnConnectionConfig | Queries configuration information about an IPsec-VPN connection. |
| CreateVpnConnection | Creates an IPsec-VPN connection. |
| DescribeVpnConnections | Queries IPsec-VPN connections in a specified region. |
| ModifyVpnConnectionAttribute | Modifies the configuration of an IPsec-VPN connection. |
| CreateSslVpnServer | Creates an SSL-VPN server. |
| DeleteSslVpnServer | Deletes an SSL-VPN server. |
| ModifySslVpnServer | Modifies the configuration of an SSL-VPN server. |
| DeleteSslVpnClientCert | Deletes an SSL-VPN client certificate. |
| ModifySslVpnClientCert | Modifies the name of an SSL-VPN client certificate. |
| CreateSslVpnClientCert | Creates an SSL-VPN client certificate. |
| DescribeSslVpnClientCerts | Queries SSL-VPN client certificates. |
| DescribeSslVpnClientCert | Queries details about an SSL-VPN client certificate. |
| DescribeSslVpnServers | Queries one or more SSL-VPN servers. |
| DescribeVpnSslServerLogs | Queries the logs of an SSL-VPN server. |

NAT Gateway management

| API | Description |
|---|---|
| CreateNatGateway | Creates a network address translation (NAT) gateway. |
| ModifyNatGatewayAttribute | Modifies the configuration of a NAT gateway. |
| ModifyNatGatewaySpec | Resizes a NAT gateway. |
| DeleteNatGateway | Deletes a specified NAT gateway. |
| DescribeNatGateways | Queries NAT gateways. |
| CreateForwardEntry | Adds DNAT entries to a DNAT table. |
| DescribeForwardTableEntries | Queries DNAT entries in a specified DNAT table. |
| ModifyForwardEntry | Modifies a specified DNAT entry. |
| DeleteForwardEntry | Deletes a specified DNAT entry. |
| CreateSnatEntry | Adds SNAT entries to an SNAT table. |
| DescribeSnatTableEntries | Queries SNAT entries. |
| ModifySnatEntry | Modifies a specified SNAT entry. |
| DeleteSnatEntry | Deletes a specified SNAT entry. |
| ModifyBandwidthPackageSpec | Modifies the bandwidth of a NAT service plan. |
| DeleteBandwidthPackage | Deletes a specified NAT service plan. |
| CreateBandwidthPackage | Creates a NAT service plan. |
| DescribeBandwidthPackages | Queries NAT service plans in a specified region. |
| ModifyBandwidthPackageAttribute | Modifies the name and description of a specified NAT service plan. |
| AddBandwidthPackageIps | Adds public IP addresses to a NAT service plan. |

EIP management

| API | Description |
|---|---|
| AllocateEipAddress | Applies for an elastic IP address (EIP). |
| AllocateEipAddressPro | Applies for a specified EIP. |
| AssociateEipAddress | Associates an EIP with a cloud service in the same region. |
| ModifyEipAddressAttribute | Modifies the name, description, and maximum bandwidth of an EIP. |
| UnassociateEipAddress | Disassociates an EIP from a cloud resource. |
| ReleaseEipAddress | Releases a specified EIP. |

| Developer Guide·API reference | Virtual Private Clou |
|---|---|

| API | Description |
|---|---|
| DescribeEipGatewayInfo | Queries information about the subnet mask and gateway of an EIP. |

HAVIP management

| API | Description |
|---|---|
| CreateHaVip | Creates a high-availability virtual IP address (HAVIP). |
| DescribeHaVips | Queries HAVIPs in a specified region. |
| ModifyHaVipAttribute | Modifies the description of an HAVIP. |
| AssociateHaVip | Associates an HAVIP with an Elastic Compute Service (ECS) instance. |
| UnassociateHaVip | Disassociates an HAVIP from an ECS instance. |
| DeleteHaVip | Deletes an HAVIP. |

Network ACL management

| API | Description |
|---|---|
| CreateNetworkAcl | Creates a network access control list (ACL). |
| AssociateNetworkAcl | Associates a network ACL with a vSwitch. |
| ModifyNetworkAclAttributes | Modifies the attributes of a network ACL. |
| UpdateNetworkAclEntries | Updates rules of a network ACL. |
| UnassociateNetworkAcl | Disassociates a network ACL from a vSwitch. |
| CopyNetworkAclEntries | Copies rules of a network ACL. |
| DeleteNetworkAcl | Deletes a network ACL. |
| DescribeNetworkAcls | Queries network ACLs. |
| DescribeNetworkAclAttributes | Queries details about a network ACL. |

IPv6 gateway management

| API | Description |
|---|---|
| CreateIpv6Gateway | Creates an IPv6 gateway. |
| DeleteIpv6Gateway | Deletes an IPv6 gateway. |
| DescribeIpv6Gateways | Queries IPv6 gateways. |
| ModifyIpv6GatewaySpec | Modifies the specification of an IPv6 gateway. |
| DescribeIpv6EgressOnlyRules | Queries egress-only rules. |
| CreateIpv6EgressOnlyRule | Adds an egress-only rule to an IPv6 address. |

| Virtual Private Cloud | Developer Guide·API reference |
|---|---|

| API | Description |
|---|---|
| DeleteIpv6EgressOnlyRule | Deletes an egress-only rule. |
| DeleteIpv6InternetBandwidth | Sets the Internet bandwidth value of an IPv6 address to zero. |
| DescribeIpv6GatewayAttribute | Queries detailed information about an IPV6 gateway. |
| DescribeIpv6Addresses | Queries IPv6 addresses. |
| ModifyIpv6InternetBandwidth | Modifies the Internet bandwidth value of an IPv6 address. |
| AllocateIpv6InternetBandwidth | Purchases Internet bandwidth resources for an IPv6 address. |
| ModifyIpv6AddressAttribute | Modifies the name and description of an IPv6 address. |
| ModifyIpv6GatewayAttribute | Modifies the information about an IPv6 gateway. |

### Call VPC APIs

#### Request syntax

To call a Virtual Private Cloud (VPC) API operation, you must send an HTTP GET request to the endpoint of the VPC API. You must add the request parameters that correspond to the API operation being called. After you call the API, the system returns a response. The request and response are encoded in UTF-8. VPC API operations use the RPC protocol. You can call VPC API operations by sending HTTP GET requests. The following example shows the syntax of a VPC API request:

```
http://Endpoint/?Action=xx&Parameters
```

where: Endpoint: the endpoint of the API. The endpoint of the VPC API is `vpc.`example`.com` . Not e `example.com` is a custom domain name. You can obtain the endpoint in the Apsara Uni-manager Operations Console. For more information, see Generate the ASAPI endpoint. Action: the operation that you want to perform. For example, to query VPCs, you must set the Action parameter to DescribeVpcs. Version: the version of the API that you want to call. The current VPC API version is 2016-04-28. Parameters: the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common request parameters and operation-specific parameters. Common parameters include the API version and authentication information. For more information about common parameters, see Common parameters. The following example describes how to call the DescribeVpcs operation. Not e The example in this topic is formatted to improve readability.

```
https://vpc.example.com/?Action=DescribeVpcs &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### API authorization

To ensure the security of your account, we recommend that you call VPC APIs as a RAM user. Before you can use a RAM account to call a VPC API, you must create a RAM account and assign corresponding permissions to it. For more information about VPC resources and APIs you can assign permissions on, see RAM authentication.

#### Request signatures

You must sign all API requests to ensure security. Virtual Private Cloud (VPC) uses the request signature to verify the identity of the API caller. VPC implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Alibaba Cloud accounts and RAM users that is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to create an AccessKey pair, see Obtain an AccessKey pair. You must add the signature to an RPC API request in the following format:

```
 https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-
```

SHA1`&Signature=`xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf Take DescribeVpcs as an example. Assume that the AccessKey ID is `testid` and the AccessKey secret is `testsecret` . The original request URL is formatted as the following example:

```
http://vpc.example.com/?Action=DescribeVpcs &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

Perform the following operations to calculate the signature:
1. Create a string-to-sign by using the request parameters:

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeVpcs&Format%3DXML&SignatureMethod%3DHMAC-SHA1&Signatur eNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&SignatureVersion%3D1.0&TimeStamp%3D2016-02-23T12%253A4 6%253A24Z&Version%3D2014-05-15
```

2. Calculate the HMAC value of the string-to-sign.
Add an ampersand (&) after the AccessKey secret as the key to calculate the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YGOjuE=
```

3. Add the signature string to the request as the Signature parameter:

```
http://vpc.example.com/?Action=DescribeVpcs &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### RAM authentication

Before calling a VPC API using a RAM user, you must use an Apsara Stack tenant account to create an authorization policy to assign permissions to the RAM user. In the authorization policy, an Alibaba Cloud Resource Name (ARN) is used as the unique identifier of the resource to authorize. VPC resources The following table lists the VPC resources that can be authorized and their corresponding ARN formats.

| Resource type | ARN format |
|---|---|
| Virtual Private Cloud (VPC) | acs:vpc:$regionid:$accountid:vpc/$vpcid |
|   | acs:vpc:$regionid:$accountid:vpc/* |
|   | acs:vpc:*:$accountid:vpc/* |
| VRouter | acs:vpc:$regionid:$accountid:vrouter/$vrouterid |
|   | acs:vpc:$regionid:$accountid:vrouter/* |
|   | acs:vpc:*:$accountid:vrouter/* |
| VSwitch | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |
|   | acs:vpc:$regionid:$accountid:vswitch/* |
|   | acs:vpc:*:$accountid:vswitch/* |
| Routing table | acs:vpc:$regionid:$accountid:routetable/$routetableid |
|   | acs:vpc:$regionid:$accountid:routetable/* |
|   | acs:vpc:*:$accountid:routetable/* |
| Elastic IP Address (EIP) | acs:vpc:$regionid:$accountid:eip/$allocationid |
|   | acs:vpc:$regionid:$accountid:eip/* |
|   | acs:vpc:*:$accountid:eip/* |
| NAT Gateway | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |
|   | acs:vpc:$regionid:$accountid:natgateway/* |
|   | acs:vpc*:$accountid:vpc/* |

| Developer Guide·API refe |   |
|---|---|
|   | rence Virtual Private Clou |
| Resource type | ARN format |
| NAT Gateway service plan | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/* |
|   | aacs:vpc:*:$accountid:vpc/* |
| Forwarding table | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |
|   | acs:vpc:$regionid:$accountid:forwardtable/* |
|   | acs:vpc:*:$accountid:vpc/* |
| SNAT table | acs:vpc:$regionid:$accountid:snattable/$snattableid |
|   | acs:vpc:$regionid:$accountid:snattable/* |
|   | acs:vpc:*:$accountid:vpc/* |
| General resource | acs:vpc:$regionid:$accountid:* |
|   | acs:vpc:*:$accountid:* |

$regionid`/`accoutid`/`vrouterid are IDs of the specific resources, `*` represents all resources. VPC API operations The following table lists the API operations that can be authorized and their corresponding ARN formats.

| Operation | ARN format |
|---|---|
| vpc:CreateVpc | acs:vpc:$regionid:$accountid:vpc/* |
| vpc:DeleteVpc | acs:vpc:$regionid:$accountid:vpc/$vpcid |
| vpc:DescribeVpcs | vpc:$regionid:$accountid:vpc/* |
| vpc:ModifyVpcAttribute | acs:vpc:$regionid:$accountid:vpc/$vpcid |
| vpc:DescribeVRouters | acs:vpc:$regionid:$accountid:vrouter/* |
|   | The VRouter ID is specified: "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |
|   | The VRouter ID is not specified: "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/*" |
| vpc:ModifyVRouterAttribute | acs:vpc:$regionid:$accountid:vrouter/$vrouterid |
| vpc:CreateVSwitch | acs:vpc:$regionid:$accountid:vswitch/* |
|   | acs:vpc:$regionid:$accountid:vpc/$vpcid |
| vpc:DeleteVSwitch | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |
| vpc:DescribeVSwitches | acs:vpc:$regionid:$accountid:vswitch/* |
|   | "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |

| Virtual Private Cloud | Developer Guide·API reference ARN format acs:vpc:$regionid:$accountid:vswitch/$vswitchid acs:vpc:$regionid:$accountid:routetable/$routetableid acs:vpc:$regionid:$accountid:routetable/$routetableid acs:vpc:$regionid:$accountid:routetable/* "vpc:VRouter":"acs:vpc$regionid:$accountid:vrouter/$vrouterid" acs:vpc:$regionid:$accountid:eip/* acs:vpc:$regionid:$accountid:eip/* Bind an ECS instance acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid acs:vpc:$regionid:$accountid:eip/* Bind an ECS instance acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid acs:vpc:$regionid:$accountid:eip/$allocationid acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid acs:vpc:$regionid:$accountid:natgateway/* acs:vpc:$regionid:$accountid:natgateway/$natgatewayid acs:vpc:$regionid:$accountid:natgateway/* acs:vpc:$regionid:$accountid:natgateway/$natgatewayid acs:vpc:$regionid:$accountid:natgateway/$natgatewayid acs:ecs:$regionid:$accountid:instance/$instanceid acs:vpc:$regionid:$accountid:natgateway/$natgatewayid acs:ecs:$regionid:$accountid:instance/$instanceid acs:vpc:$regionid:$accountid:bandwidthpackage/* acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackag eid acs:vpc:$regionid:$accountid:bandwidthpackage/* |   |   |
|---|---|---|---|
| Operation | ARN format |   |   |
| vpc:ModifyVSwitchAttribute | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |   |   |
| vpc:CreateRouteEntry | acs:vpc:$regionid:$accountid:routetable/$routetableid |   |   |
| vpc:DeleteRouteEntry | acs:vpc:$regionid:$accountid:routetable/$routetableid |   |   |
| vpc:DescribeRouteTables | acs:vpc:$regionid:$accountid:routetable/* |   |   |
|   | "vpc:VRouter":"acs:vpc$regionid:$accountid:vrouter/$vrouterid" |   |   |
|   |   | "vpc:VRouter":"acs:vpc$regionid:$accountid:vrouter/$vrouterid" |   |
| vpc:AllocateEipAddress | acs:vpc:$regionid:$accountid:eip/* |   |   |
| vpc:AssociateEipAddres | acs:vpc:$regionid:$accountid:eip/* |   |   |
|   | Bind an ECS instance acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:DescribeEipAddresses | acs:vpc:$regionid:$accountid:eip/* |   |   |
| vpc:UnassociateEipAddress | Bind an ECS instance acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:ReleaseEipAddress | acs:vpc:$regionid:$accountid:eip/$allocationid |   |   |
| vpc:DescribeEipMonitorData | acs:vpc:$regionid:$accountid:eip/$allocationid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:CreateNatGateway | acs:vpc:$regionid:$accountid:natgateway/* |   |   |
| vpc:DescribeNatGateways | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
|   | acs:vpc:$regionid:$accountid:natgateway/* |   |   |
| vpc:ModifyNatGatewaySpec | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
| vpc:ModifyNatGatewayAttribute | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:DeleteNatGateway | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:CreateBandwidthPackage | acs:vpc:$regionid:$accountid:bandwidthpackage/* |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackag eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackag |   |
|   | eid |   |   |
| vpc:DescribeBandwidthPackages |   |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/* |   |   |

| Developer Guide·API reference |   |   |   |
|---|---|---|---|
| Operation | ARN format |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackag eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackag |   |
| vpc:ModifyBandwidthPackageSpec | eid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackag eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackag |   |
| vpc:ModifyBandwidthPackageAttribute | eid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackag eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackag |   |
| vpc:AddBandwidthPackageIps | eid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackag eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackag |   |
| vpc:RemoveBandwidthPackageIps | eid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackag eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackag |   |
| vpc:DeleteBandwidthPackage | eid |   |   |
| vpc:CreateForwardEntry | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |   |
| vpc:DeleteForwardEntry | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |   |
| vpc:ModifyForwardEntry | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |   |
| vpc:DescribeForwardTableEntries | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |   |
| vpc:CreateSnatEntry | acs:vpc:$regionid:$accountid:snattable/* |   |   |
| vpc:ModifySnatEntry | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |
| vpc:DescribeSnatTableEntries | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |
| vpc:DeleteSnatEntry | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |

### Common parameters

Common request parameters Common request parameters are request parameters that you must use when you call each API. Common request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The format of the response. Valid values: JSON (default) \| XML |
| Version | String | Yes | The API version in the format of YYYY-MM-DD . Valid value: 2016-04-28 |
| AccessKeyId | String | Yes | The AccessKey ID that you use to call an API. |
| Signature | String | Yes | The signature result string. |
| SignatureMethod | String | Yes | The algorithm used to create the request signature. Valid value: HMAC-SHA1 |

| Virtual Private Clou | d |   | Developer Guide·API reference |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| Timestamp | String | Yes | The timestamp of the request. The timestamp uses UTC and it complies with the ISO 8601 standard. Its format is YYYY-MM-DDThh:mm:ssZ . For example, 20:00:00 on January 10, 2013 in China Standard Time (UTC +8) is written as 2013-01-10T12:00:00Z. |
| SignatureVersion | String | Yes | The version of the signature algorithm. Valid value: 1.0 |
| SignatureNonce | String | Yes | A unique random number that is used to prevent network replay attacks. You must use different random numbers for different requests. |

```
http://vpc.example.com/?Action=DescribeVpcs &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

Common response parameters API responses use a unified format. 2xx HTTP status codes indicate a successful invocation. 4xx or 5xx HTTP status codes indicate a failed invocation. The responses can be returned in JSON or XML format. The XML format is used by default. You can specify the format when calling an API. Each time you send a request to call an API, the system returns a unique identifier RequestId, regardless of whether the invocation is successful or not. XML format

```xml
<? xml version="1.0" encoding="utf-8"? >
      <!—Result root node-->
      <API name+Response>
      <!—Returned request tag-->
      <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
      <!—Returned results-->
      </API name+Response>
```

JSON format `{`

```json
      "RequestId":"4C467B38-3910-447D-87BC-AC049166F216",
      /*Returned results*/
```

### VPC

#### CreateVpc

Deletes a virtual private cloud (VPC). Descriptions When you call this operation, take note of the following rules: You can specify only one CIDR block for a VPC. The CIDR block must be 172.16.0.0/16, 192.168.0.0/16, or their subnets, and the subnet mask must be 8 to 24 bits in length. The default CIDR block is 192.168.0.0/16. After you create a VPC, you cannot modify its CIDR block. In each VPC, cloud services can use a maximum of 60,000 private IP addresses. You cannot increase the quota. After you create a VPC, a vRouter and a route table are automatically created. At most three customer-side CIDR blocks can be added to a VPC. If a user CIDR block includes another user CIDR block, the one with the shorter subnet mask takes effect. For example, if 192.168.0.0/16 and 192.168.0.0/24 are specified, only 192.168.0.0/16 takes effect. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpc | The operation that you want to perform. Set the value to Creat eVpc. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region to which the VPC belongs. You can call the DescribeRegions operation to query the most recent region list. |
| CidrBlock | String | No | 172.16.0.0/16 | The CIDR block of the VPC. You can use one of the following CIDR blocks or their subnets as the CIDR block of your VPC: 172.16.0.0/16. 192.168.0.0/16 (default). |
| Ipv6CidrBlock | String | No | 1007:XXXX:0:40::/5 6 | The IPv6 CIDR block of the VPC. |
| EnableIpv6 | Boolean | No | false | Specifies whether to enable the IPv6 CIDR block. Valid values: f alse (default): disables the IPv6 CIDR block. t rue: enables the IPv6 CIDR block. |
| VpcName | String | No | abc | The name of the VPC. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter and cannot start with http:// or https:// . |
| Description | String | No | This is my first Vpc. | The description of the VPC. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| ResourceGroupId | String | No | rg- acfmxazb4ph6aiy*** * | The ID of the resource group. |   |   |
| DryRun | Boolean | No | false | Specifies whether to precheck this request. Valid values: t rue: sends a check request without creating a VPC. The system checks the required parameters, request format and service limits. An error message is returned if the request fails the precheck. If the request passes the precheck, the DryRun Operation error code is returned. f alse: sends the request. This is the default value. If the request passes the precheck, a 2XX HTTP status code is returned and the a VPC is created. |   |   |
|   |   |   |   |   | DryRun |   |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. Client T oken can contain only ASCII characters and cannot exceed 64 characters in length. |   |   |
| UserCidr | String | No | 189.XX.XX.0/12 | The user CIDR block. Separate multiple CIDR blocks with commas (,). At most three CIDR blocks are supported. |   |   |

|   | Operation |
|---|---|

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpcId | String | vpc- bp15zckdt37pq72zv*** * | The ID of the created VPC. |
| VRouterId | String | vrt- bp1lhl0taikrteen8**** | The ID of the vRouter that is automatically created by the system after the VPC is created. |
| RouteTableId | String | vtb- bp145q7glnuzdv**** | The ID of the route table that is automatically created by the system after the VPC is created. |
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |
| ResourceGroupId | String | rg- acfmxazb4ph6aiy**** | The ID of the resource group to which the EIP belongs. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateVpc &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateVpcResponse>
      <ResourceGroupId>rg-acfmxazb4ph****</ResourceGroupId>
      <RequestId>8B2F5262-6B57-43F2-97C4-971425462DFE</RequestId>
      <RouteTableId>vtb-bp1krxxzp0c2****</RouteTableId>
      <VRouterId>vrt-bp1jcg5cmxjbl9xgc****</VRouterId>
      <VpcId>vpc-bp1qpo0kug3a20qqe****</VpcId>
</CreateVpcResponse>
```

`JSON` format `{`

```json
    "CreateVpcResponse": {
        "ResourceGroupId": "rg-acfmxazb4ph****",
        "RequestId": "8B2F5262-6B57-43F2-97C4-971425462DFE",
        "RouteTableId": "vtb-bp1krxxzp0c2****",
        "VRouterId": "vrt-bp1jcg5cmxjbl9xgc****",
        "VpcId": "vpc-bp1qpo0kug3a20qqe****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | Specified value of "regionId" is not supported. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |
| 400 | InvalidParameter | Specified CIDR block is not valid | The error message returned because the specified CIDR block is invalid. |
| 400 | ResourceNotAvailable | Resource you requested is not available in this region or zone. | The error message returned because you cannot create a vSwitch in the current region or zone. |
| 400 | InvalidVpcName.Malfor med | Specified VPC name is not valid. | The error message returned because the format of the VPC name is invalid. Enter a valid VPC name and try again. |
| 400 | InvalidVpcDiscription.Ma lformed | Specified VPC description is not valid. | The error message returned because the format of the VPC description is invalid. |
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the permissions and try again. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded.Vpc | VPC quota exceeded. | The error message returned because the number of VPCs that belong to the Apsara Stack tenant account has reached the upper limit. You can submit a ticket to request a quota increase. |
| 400 | ResourceNotAvailable.V pc | Resource you requested is not available in this region or zone. | The error message returned because the resource you requested is not available in this region or zone. |
| 400 | InvalidParameter | Specified UserCidr invalid format. | The error message returned because the format of the user CIDR block is invalid. |
| 400 | InvalidParameter | Specified UserCidr Subnet mask is not valid . | The error message returned because the subnet mask of the user CIDR block is invalid. |
| 400 | InvalidUserCidr.Quota | Specified UserCidr number is greater than 3. | The error message returned because the UserCidr value has reached the upper limit. |
| 400 | InvalidUserCidr.Malform ed | Specified UserCidr overlapping in of 100.64.0.0/10. | The error message returned because the UserCidr value overlaps with 100.64.0.0/10. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 400 | InvalidResourceGroupId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID is invalid. |
| 400 | OperationUnsupported. ResourceGroupId | ResourceGroup is not supported in this region. | The error message returned because the resource group feature is not enabled. |

#### DeleteVpc

Deletes a virtual private cloud (VPC). Descriptions When you call this operation, take note of the following limits: Before you delete a VPC, make sure that you have released or removed all resources deployed in the VPC, such as vSwitches, instances, and high-availability virtual IP addresses (HAVIPs). You can delete only a VPC that is in the Available state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpc | The operation that you want to perform. Set the value to Delet eVpc. |

| Developer Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpcId | String | Yes | vpc- bp1m7v25emi1h5mt c**** | The ID of the VPC that you want to delete. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the VPC is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVpc &VpcId=vpc-bp1m7v25emi1h5mtc**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVpcResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteVpcResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | OperationDenied | The operation is not supported in this status. | The error message returned because the state of the VPC is invalid and the operation cannot be performed. |
| 403 | OperationDenied | The snapshot creation for the specified disk is not finished yet. | The error message returned because the snapshot of the specified disk is being created. |
| 400 | IncorrectVpcStatus | Current VPC status does not support this operation. | The error message returned because the state of the VPC does not support this operation. |
| 400 | DependencyViolation.R outeEntry | Specified object has dependent resources | The error message returned because custom route entries exist in the VPC and the VPC cannot be deleted. |

|   | Virtual Private | Cloud |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | DependencyViolation.In stance | Specified object has dependent resources | The error message returned because the VPC is associated with a resource. |
| 400 | DependencyViolation.V Switch | Specified object has dependent resources | The error message returned because vSwitches exist in the VPC and the VPC cannot be deleted. Delete the vSwitches and try again. |
| 400 | DependencyViolation.Se curityGroup | Specified object has dependent resources | The error message returned because security groups exist in the VPC and the VPC cannot be deleted. Delete the security groups and try again. |
| 404 | InvalidVpcId.NotFound | Specified VPC does not exist. | The error message returned because the specified VPC does not exist. |
| 400 | DependencyViolation.R outeInterface | Specified object has dependent route interface . | The error message returned because the vSwitch is associated with a router interface and cannot be deleted. |
| 400 | DependencyViolation.T unnel | Specified object has dependent tunnel. | The error message returned because the VPC is associated with a tunnel. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 400 | DependencyViolation.N atGateway | Specified object has dependent resources NatGateway. | The error message returned because NAT gateways exist in the VPC and the VPC cannot be deleted. Delete the NAT gateways and try again. |
| 400 | DependencyViolation.R outerInterface | Specified object has dependent resources RouterInterface. | The error message returned because the VPC is associated with a router interface. |
| 400 | DependencyViolation.Se curityGroup | Specified object has dependent resources SecurityGroup. | The error message returned because security groups exist in the VPC and the VPC cannot be deleted. Delete the security groups and try again. |
| 400 | Forbidden.VpcNotFoun d | Specified VPC can not found. | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | Forbbiden | Active custom route in vpc. | The error message returned because you must add a custom route entry to the VPC. |
| 400 | DependencyViolation.D hcpOptionsSet | The VPC cannot be deleted when it is associated with dhcpOptionsSet. | The error message returned because DHCP options sets exist in the VPC and the VPC cannot be deleted. Delete the DHCP options sets and try again. |

#### ModifyVpcAttribute

Modifies the name and description of a virtual private cloud (VPC). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpcAttribute | The operation that you want to perform. Set the value to Modif yVpcAt t ribut e. |
| VpcId | String | Yes | vpc- bp1qtbach57ywecf* *** | The ID of the VPC that you want to modify. |
| Description | String | No | This is my VPC. | The description of the VPC. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| VpcName | String | No | Vpc-1 | The new name of the VPC. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter and cannot start with http:// or https:// . |
| CidrBlock | String | No | 192.XX.XX.0/24 | The IPv4 CIDR block of the VPC. The CIDR block can be 172.16.0.0/16, 192.168.0.0/16, and one of their subnets. The subnet mask must be 8 to 24 bits in length. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the VPC is deployed. You can call the DescribeRegions operation to the most recent region list. |
| EnableIPv6 | Boolean | No | true | Specifies whether to enable IPv6 CIDR blocks. Valid values: t rue: enables IPv6 CIDR blocks. f alse: disables IPv6 CIDR blocks. |
| Ipv6CidrBlock | String | No | 1007:XXXX:0:40::/6 1 | Specifies whether to enable IPv6 CIDR blocks. Valid values: t rue: enables IPv6 CIDR blocks. f alse: disables IPv6 CIDR blocks. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVpcAttribute &VpcId=vpc-bp1qtbach57ywecf**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVpcAttributeResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ModifyVpcAttributeResponse>
```

`JSON` format `{`

```json
    "ModifyVpcAttributeResponse": {
        "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVpcId.NotFound | Specified VPC does not exist. | The error message returned because the specified VPC does not exist. |
| 400 | InvalidVpcName.Malfor med | Specified VPC name is not valid. | The error message returned because the format of the VPC name is invalid. Enter a valid VPC name and try again. |
| 400 | InvalidVpcDiscription.Ma lformed | Specified VPC description is not valid. | The error message returned because the format of the VPC description is invalid. |
| 400 | InvalidParameter | Specified UserCidr invalid format. | The error message returned because the format of the user CIDR block is invalid. |
| 400 | InvalidParameter | Specified UserCidr Subnet mask is not valid . | The error message returned because the subnet mask of the user CIDR block is invalid. |
| 400 | InvalidUserCidr.Quota | Specified UserCidr number is greater than 3. | The error message returned because the UserCidr value has reached the upper limit. |
| 400 | InvalidUserCidr.Malform ed | Specified UserCidr overlapping in of 100.64.0.0/10. | The error message returned because the UserCidr value overlaps with 100.64.0.0/10. |
| 400 | IncorrectVpcStatus | Current VPC status does not support this operation. | The error message returned because the state of the VPC does not support this operation. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidCidrBlock.Malfor med | Specified CIDR block is not valid. | The error message returned because the format of the specified CIDR block is invalid. |

#### DescribeVpcAttribute

Queries the detailed information about a specified virtual private cloud (VPC). Request parameters

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| Action | String | Yes | DescribeVpcAttribut e | The operation that you want to perform. Set the value to DescribeVpcAt t ribut e. |   |   |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the VPC. You can call the DescribeRegions operation to query the most recent region list. |   |   |
| VpcId | String | Yes | vpc- bp18sth14qii3pnv*** * | The ID of the VPC that you want to query. |   |   |
| DryRun | Boolean | No | false | Specifies whether to precheck the request. t rue: prechecks the API request. Resources are not queried. The system checks whether your AccessKey pair is valid, whether the RAM user is authorized, and whether required parameters are set. If the request fails the precheck, the corresponding error message is returned. If the request passes the precheck, the D ryRunOperation error code is returned. f alse: sends the request. This is the default value. If the request passes the precheck, a 2xx HTTP status code is returned and resources are queried. |   |   |
|   |   |   |   |   | D |   |
| IsDefault | Boolean | No | false | Specifies whether the VPC is the default one. Valid values: f alse: no t rue (default): yes |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AssociatedCens | Array of AssociatedCen |   | The list of Cloud Enterprise Network (CEN) instances that are associated with the VPC. If the VPC is not associated with a CEN instance, the parameter is not returned. |
| AssociatedCen |   |   |   |
| CenId | String | cen- 7qthudw0ll6jmc**** | The ID of the CEN instance that is associated with the VPC. |
| CenOwnerId | Long | 111111111111 | The ID of the Apsara Stack tenant account to which the CEN instance belongs. |
| CenStatus | String | Attached | The status of the associated CEN instance. At t ached is returned only when the VPC is associated with a CEN instance. |
| CidrBlock | String | 192.168.0.0/16 | The IPv4 CIDR block of the VPC. |
| ClassicLinkEnabled | Boolean | false | Indicates whether the ClassicLink feature is enabled. Valid values: t rue: yes f alse: no |
| CloudResources | Array of CloudResourceSet Type |   | The list of resources deployed in the VPC. |
| CloudResourceSet Type |   |   |   |
| ResourceCount | Integer | 1 | The number of resources deployed in the VPC. |
| ResourceType | String | VSwitch | The type of resources deployed in the VPC. Valid values: VSwit ch: vSwitches VRout er: vRouters Rout eT able: route tables |
| CreationTime | String | 2018-10-16T07:31:09Z | The time when the VPC was created. |
| Description | String | VPC | The description of the VPC. |
| DhcpOptionsSetId | String | dopt- o6w0df4epg9zo8isy*** * | The ID of the DHCP options set. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|
| Parameter | Type | Example | Description |
| DhcpOptionsSetSt atus | String | Available | The status of the DHCP options set. Valid values: Available: The DHCP options set is available. InUse: The DHCP options set is being used. Delet ed: The DHCP options set is deleted. Pending: The DHCP options set is being configured. |
| Ipv6CidrBlock | String | 2408:XXXX:0:a600::/5 6 | The IPv6 CIDR block of the VPC. |
| IsDefault | Boolean | false | Indicates whether the VPC is the default one. Valid values: t rue: yes f alse: no |
| OwnerId | Long | 3253532535 | The ID of the owner. |
| RegionId | String | cn-qingdao-env17-d01 | The region ID of the VPC. You can call the DescribeRegions operation to query the most recent region list. |
| RequestId | String | 7486AE4A-129D-43DB- A714-2432C074BA04 | The ID of the request. |
| ResourceGroupId | String | rg- acfmxazbvgb4ph**** | The ID of the resource group to which the VPC belongs. |
| SecondaryCidrBloc ks | List | 192.168.20.0/24 | The secondary IPv4 CIDR block of the VPC. |
| Status | String | Available | The status of the VPC. Valid values: Available: available Pending: being configured |
| UserCidrs | List | 172.16.0.1/24 | The user CIDR block. Multiple CIDR blocks are separated by commas (,). At most three CIDR blocks are returned. |
| VRouterId | String | vrt- bp1jso6ng1at0ajsc**** | The ID of the vRouter that belongs to the VPC. |
| VSwitchIds | List | vsw- bp1nhbnpv2blyz8dl**** | The list of vSwitches deployed in the VPC. |
| VpcId | String | vpc- bp18sth14qii3pnvo**** | The ID of the VPC. |
| VpcName | String | doctest2 | The name of the VPC. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpcAttribute &RegionId=cn-qingdao-env17-d01 &VpcId=vpc-bp18sth14qii3pnv**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpcAttributeResponse>
      <VpcName>doctest2</VpcName>
      <Description></Description>
      <IsDefault>false</IsDefault>
      <ResourceGroupId>rg-acfmxazb4ph****</ResourceGroupId>
      <UserCidrs></UserCidrs>
      <ClassicLinkEnabled>false</ClassicLinkEnabled>
      <AssociatedCens>
            <AssociatedCen>
                  <CenStatus>Attached</CenStatus>
                  <CenOwnerId>12315790855****</CenOwnerId>
                  <CenId>cen-7qthudw0ll6jmc****</CenId>
            </AssociatedCen>
      </AssociatedCens>
      <VRouterId>vrt-bp1jso6ng1at0ajs****</VRouterId>
      <VpcId>vpc-bp18sth14qii3pnvo****</VpcId>
      <CreationTime>2018-10-16T07:31:09Z</CreationTime>
      <CidrBlock>192.168.0.0/16</CidrBlock>
      <Status>Available</Status>
      <VSwitchIds>
            <VSwitchId>vsw-bp14cagpfysr29fe****</VSwitchId>
      </VSwitchIds>
      <RequestId>7486AE4A-129D-43DB-A714-2432C074BA04</RequestId>
      <RegionId>cn-hangzhou</RegionId>
      <CloudResources>
            <CloudResourceSetType>
                  <ResourceType>VSwitch</ResourceType>
                  <ResourceCount>1</ResourceCount>
            </CloudResourceSetType>
            <CloudResourceSetType>
                  <ResourceType>VRouter</ResourceType>
                  <ResourceCount>1</ResourceCount>
            </CloudResourceSetType>
            <CloudResourceSetType>
                  <ResourceType>RouteTable</ResourceType>
                  <ResourceCount>1</ResourceCount>
            </CloudResourceSetType>
      </CloudResources>
</DescribeVpcAttributeResponse>
```

`JSON` format `{`

```json
    "DescribeVpcAttributeResponse": {
        "VpcName": "doctest2",
        "Description": "",
        "IsDefault": false,
        "ResourceGroupId": "rg-acfmxazb4ph****",
        "UserCidrs": "",
        "ClassicLinkEnabled": false,
        "AssociatedCens": {
            "AssociatedCen": {
                "CenStatus": "Attached",
                "CenOwnerId": "12315790855****",
                "CenId": "cen-7qthudw0ll6jmc****"
```

`},`

```json
        "VRouterId": "vrt-bp1jso6ng1at0ajs****",
        "VpcId": "vpc-bp18sth14qii3pnvo****",
        "CreationTime": "2018-10-16T07:31:09Z",
        "CidrBlock": "192.168.0.0/16",
        "Status": "Available",
        "VSwitchIds": {
            "VSwitchId": "vsw-bp14cagpfysr29fe****"
```

`},`

```json
        "RequestId": "7486AE4A-129D-43DB-A714-2432C074BA04",
        "RegionId": "cn-hangzhou",
        "CloudResources": {
            "CloudResourceSetType": [
```

`{`

```json
                    "ResourceType": "VSwitch",
                    "ResourceCount": 1
```

`},` `{`

```json
                    "ResourceType": "VRouter",
                    "ResourceCount": 1
```

`},` `{`

```json
                    "ResourceType": "RouteTable",
                    "ResourceCount": 1
```

`]` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 400 | IncorrectVpcStatus | Current VPC status does not support this operation. | The error message returned because this operation cannot be performed while the VPC is in the current state. |
| 404 | InvalidVpcId.NotFound | Specified VPC does not exist. | The error message returned because the specified VPC does not exist. |

#### AssociateVpcCidrBlock

Adds a secondary IPv4 CIDR block to a virtual private cloud (VPC). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociateVpcCidrBlo ck | The operation that you want to perform. Set the value to Associat eVpcCidrBlock. |
| RegionId | String | Yes | ch-qingdao-env17- d01 | The ID of the region where the VPC is deployed. You can call the DescribeRegions operation to the most recent region list. |
| VpcId | String | Yes | vpc- o6wrloqsdqc9io3m g**** | The ID of the VPC to which you want to add a secondary IPv4 CIDR block. |
| SecondaryCidrBlock | String | No | 192.168.0.0/16 | The secondary IPv4 CIDR block. You can specify one of the following standard IPv4 CIDR blocks or their subnets as the secondary IPv4 CIDR block: 192.168.0.0/16, 172.16.0.0/12, and 10.0.0.0/8. To use a public CIDR block as the secondary IPv4 CIDR block, submit a ticket. When you add a secondary IPv4 CIDR block, take note of the following rules: The CIDR block cannot start with 0. The subnet mask must be 8 to 24 bits in length. The secondary CIDR block cannot overlap with the primary CIDR block or an existing secondary CIDR block. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C1221A1F-2ACD-4592- 8F27-474E02883159 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AssociateVpcCidrBlock &RegionId=ch-qingdao-env17-d01 &VpcId=vpc-o6wrloqsdqc9io3mg**** &<Common request parameters>
```

Sample success response `XML` format

```xml
<AssociateVpcCidrBlockResponse>
         <RequestId>C1221A1F-2ACD-4592-8F27-474E02883159</RequestId>
</AssociateVpcCidrBlockResponse>
```

`JSON` format `{`

```json
 "RequestId":"C1221A1F-2ACD-4592-8F27-474E02883159"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidCidrBlock.Malfor med | Specified CIDR block is not valid. | The error message returned because the format of the specified CIDR block is invalid. |
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the permissions and try again. |
| 400 | MissingParam.Secondar yCidrBlockOrIpv6CidrBlo ck | Either SecondaryCidrBlock or Ipv6CidrBlock must be specified. | The error message returned because the secondary IPv4 CIDR block or the IPv6 CIDR block is not set. |
| 400 | MissingParam.VpcId | You must specify VpcId. | The error message returned because VpcId is not set. |

#### UnassociateVpcCidrBlock

Deletes a secondary IPv4 CIDR block from a virtual private cloud (VPC). Descriptions Before you delete a secondary IPv4 CIDR block from a VPC, delete the vSwitch which is created with the IPv4 CIDR block. For more information, see `DeleteVSwitch` . Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociateVpcCidr Block | The operation that you want to perform. Set the value to Unassociat eVpcCidrBlock. |
| RegionId | String | Yes | ch-qingdao-env17- d01 | The ID of the region to which the secondary IPv4 CIDR block to be deleted belongs. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- o6wrloqsdqc9io3m g**** | The ID of the VPC from which you want to delete a secondary IPv4 CIDR block. |

| Virtual Private Cloud |   |   |   | Developer Guide·API reference |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SecondaryCidrBlock | String | No | 192.XX.XX.0/16 | The secondary IPv4 CIDR block. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C1221A1F-2ACD-4592- 8F27-474E02883159 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UnassociateVpcCidrBlock &RegionId=ch-qingdao-env17-d01 &VpcId=vpc-o6wrloqsdqc9io3mg**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UnassociateVpcCidrBlockResponse>
         <RequestId>C1221A1F-2ACD-4592-8F27-474E02883159</RequestId>
</UnassociateVpcCidrBlockResponse>
```

`JSON` format `{`

```json
 "RequestId":"C1221A1F-2ACD-4592-8F27-474E02883159"
```

#### MoveResourceGroup

Moves a resource to a different resource group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | MoveResourceGroup | The operation that you want to perform. Set the value to MoveResourceGroup. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NewResourceGroupI d | String | Yes | rg- acfm3peow3k**** | The ID of the resource group to which the cloud resource is to be moved. Not e You can use resource groups to manage resources owned by your Apsara Stack account. Resource groups simplify the resource and permission management of your Apsara Stack account. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the cloud resource. You can call the DescribeRegions operation to query the most recent region list. |
| ResourceId | String | Yes | vpc- hp31psbg8ec3023s6 **** | The ID of the instance that you want to move. |
| ResourceType | String | Yes | vpc | The type of the cloud resource. Valid values: vpc: a virtual private cloud (VPC) eip: an elastic IP address (EIP) |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F84A05B3-7275-4C8B- 8AEE-9088C639C271 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=MoveResourceGroup &NewResourceGroupId=rg-acfm3peow3k**** &RegionId=cn-qingdao-env17-d01 &ResourceId=vpc-hp31psbg8ec3023s6**** &ResourceType=vpc &<Common request parameters>
```

Sample success responses `XML` format

```xml
<MoveResourceGroup>
  <RequestId>F84A05B3-7275-4C8B-8AEE-9088C639C271</RequestId>
</MoveResourceGroup>
```

`JSON` format `{`

```json
    "RequestId": "F84A05B3-7275-4C8B-8AEE-9088C639C271"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidResourceGroupId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID is invalid. |

### vSwitch

#### CreateVSwitch

Creates a vSwitch. Descriptions When you call this operation, take note of the following limits: You can create at most 24 vSwitches in a virtual private cloud (VPC). The first IP address and last three IP addresses of each vSwitch CIDR block are reserved. For example, if the CIDR block of a vSwitch is 192.168.1.0/24, the IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved. The number of instances in a vSwitch cannot exceed the remaining capacity of the VPC. The remaining capacity is the difference between 15,000 and the current number of instances. Each instance can belong to only one vSwitch. vSwitches do not support multicasting or broadcasting. After you create a vSwitch, you cannot modify its CIDR block. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVSwitch | The operation that you want to perform. Set the value to Creat eVSwit ch. |
| CidrBlock | String | Yes | 172.XX.XX.0/24 | The CIDR block of the vSwitch. Take note of the following limits: The subnet mask must be 16 to 29 bits in length. The CIDR block of the vSwitch must fall within the CIDR block of the VPC to which the vSwitch belongs. The CIDR block of a vSwitch cannot be the same as the destination CIDR block in a route entry of the VPC. However, it can be a subset of the destination CIDR block. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpcId | String | Yes | vpc- 257gqcdfvx6n**** | The ID of the VPC where you want to create the vSwitch. |
| ZoneId | String | Yes | cn-qingdao-env- amtest11001-a | The zone ID of the vSwitch. You can call the DescribeZones operation to query the most recent zone list. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the vSwitch. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6CidrBlock | Integer | No | 12 | The last eight bits of the IPv6 CIDR block of the vSwitch. Valid values: 0 to 255. |
| VSwitchName | String | No | VSwitch-1 | The name of the vSwitch. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter. It cannot start with http:// or https:// . |
| Description | String | No | This is my vswitch. | The description of the vSwitch. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The token used to ensure idempotence. You can use the client to generate a value, but you must make sure that it is unique among different requests. Client T oken can contain only ASCII characters and cannot exceed 64 characters in length. |
| IsCgw | Boolean | No | true | Specifies whether the gateway is a customer gateway. Valid values: t rue: yes f alse (default): no |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VSwitchId | String | vsw-25navfgbue4g**** | The ID of the vSwitch. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 861E6630-AEC0-4B2D- B214-6CB5E44B7F04 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateVSwitch &CidrBlock=172.XX.XX.0/24 &VpcId=vpc-257gqcdfvx6n**** &ZoneId=cn-qingdao-env-amtest11001-a &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateVSwitchResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
      <VSwitchId>vsw-25naue4cdvf****</VSwitchId>
</CreateVSwitchResponse>
```

`JSON` format `{`

```json
    "CreateVSwitchResponse": {
        "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0",
        "VSwitchId": "vsw-25naue4cdvf****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidZoneId.NotFound | Specified zone does not exist. | The error message returned because the zone ID is invalid. |
| 404 | InvalidVpcId.NotFound | Specified VPC does not exist. | The error message returned because the specified VPC does not exist. |
| 400 | InvalidVSwitchName.Ma lformed | Specified virtual switch name is not valid. | The error message returned because the format of the specified vSwitch name is invalid. Check whether the specified name is valid. |
| 400 | InvalidVSwitchDiscriptio n.Malformed | Specified virtual switch description is not valid. | The error message returned because the description of the vSwitch is invalid. |
| 400 | ResourceNotAvailable | Resource you requested is not available in this region or zone. | The error message returned because you cannot create a vSwitch in the current region or zone. |
| 400 | InvalidParameter | Specified CIDR block is not valid in VPC. | The error message returned because the vSwitch CIDR block does not fall within the VPC CIDR block. |

| Developer Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidCidrBlock.Overlap ped | Specified CIDR block overlapped with other subnets. | The error message returned because the vSwitch CIDR block overlaps with another vSwitch CIDR block or the destination CIDR block of a custom route entry. Make sure that the vSwitch CIDR block does not overlap with another vSwitch CIDR block or the destination CIDR block of a route entry. |
| 400 | InvalidCidrBlock.Overlap ped | Specified CIDR block overlapped with other entry. | The error message returned because the vSwitch CIDR block overlaps with another vSwitch CIDR block or the destination CIDR block of a custom route entry. Make sure that the vSwitch CIDR block does not overlap with another vSwitch CIDR block or the destination CIDR block of a route entry. |
| 400 | QuotaExceeded.VSwitc h | Virtual switch quota exceeded. | The error message returned because the number of vSwitches has reached the quota. Reduce the number of vSwitches and try again later. |
| 400 | IncorrectRouteEntryStat us | Some route entry status blocked this operation. | The error message returned because one or more route entries in the current route table are in the Pending or Modifying state. |
| 400 | IncorrectVSwitchStatus | Some virtual switch is modifying within the same VPC. | The error message returned because multiple vSwitches are in the Modifying state in the same VPC. Try again later. |
| 400 | InvalidCirdrBlock.MaskLe ngth | Specified CIDR block is not valid . | The error message returned because the format of the CIDR block is invalid. |
| 400 | IncorrectVpcStatus | Current VPC status does not support this operation. | The error message returned because this operation cannot be performed while the VPC is in the current state. |
| 400 | InvalidCidrBlock.Malfor med | Specified CIDR block is not valid. | The error message returned because the format of the specified CIDR block is invalid. |
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because the required parameters are not set. Try again. |
| 400 | IncorrectVSwitchStatus | VSwitch Creation simultaneously is not supported. | The error message returned because the system failed to create the vSwitch and one or more vSwitches that belong to the VPC are in the Creating state. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Forbidden.VpcNotFoun d | Specified VPC can not found. | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |

#### DeleteVSwitch

Deletes a vSwitch. Descriptions When you call this operation, take note of the following limits: Before you delete a vSwitch, delete all the resources that are deployed in the vSwitch first, including Elastic Compute Service (ECS) instances, Server Load Balancer (SLB) instances, and ApsaraDB RDS instances. If SNAT entries and high-availability virtual IP addresses (HAVIPs) are configured in the vSwitch, delete them before you delete the vSwitch. You can delete only vSwitches that are in the Available state. You cannot delete a vSwitch from a virtual private cloud (VPC) if a vSwitch is being created, a vSwitch is being deleted, or a route entry is being deleted in the VPC. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVSwitch | The operation that you want to perform. Set the value to Delet eVSwit ch. |
| VSwitchId | String | Yes | vsw- asdfjcdvflna**** | The ID of the vSwitch that you want to delete. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the vSwitch. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://vpc.aliyuncs.com/?Action=DeleteVSwitch &VSwitchId=vsw-asdfjcdvflna**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVSwitchResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteVSwitchResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorrectVSwitchStatus | The current virtual switch status does not support this operation. | The error message returned because the vSwitch is in the Pending state and cannot be deleted. |
| 400 | DependencyViolation | Specified object has dependent resources. | The error message returned because resources deployed in the vSwitch are not deleted and the vSwitch cannot be deleted. Delete the resources deployed in the VPC first before you delete the VPC. |
| 400 | DependencyViolation | Some route entry status blocked this operation. | The error message returned because one or more route entries in the current route table are in the Pending or Modifying state. |
| 400 | IncorrectRouteEntryStat us | Some route entry status blocked this operation. | The error message returned because one or more route entries in the current route table are in the Pending or Modifying state. |
| 400 | DependencyViolation.H aVip | VSwitch cannot be deleted when there are some HaVip dependent with it. | The error message returned because the vSwitch is associated with an HAVIP and the vSwitch cannot be deleted. |
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because one or more required parameters are not set. Check whether you have set all the required parameters before you call this operation. |
| 404 | InvalidVSwitchId.NotFou nd | VSwitch not exist. | The error message returned because the specified vSwitch does not exist. Check whether you specify a valid vSwitch. |
| 404 | IncorrectStatus | Vswtich status not stable. | The error message returned because the vSwitch is in the Pending or Modifying state. Try again later. |

#### ModifyVSwitchAttribute

Modifies the name and description of a vSwitch. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVSwitchAttrib ute | The operation that you want to perform. Set the value to Modif yVSwit chAt t ribut e. |
| VSwitchId | String | Yes | vsw- 25nacdfvue4**** | The ID of the vSwitch. |
| VSwitchName | String | No | VSwitch-1 | The new name for the vSwitch. The name must be 2 to 128 characters in length, and can contain, digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter The name cannot start with http:// or https:// . |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the vSwitch is deployed. You can call the DescribeRegions operation to the most recent region list. |
| Description | String | No | This is my vswitch. | The description of the vSwitch. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| Ipv6CidrBlock | Integer | No | 10 | The last eight bits of the IPv6 CIDR block of the vSwitch. Valid values: 0 to 255. You can set this parameter only when the VPC to which the vSwitch belongs has the IPv6 feature enabled. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVSwitchAttribute &VSwitchId=vsw-25nacdfvue4**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVSwitchAttributeResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ModifyVSwitchAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVSwitchId.NotFou nd | The specified virtual switch does not exists. | The error message returned because the specified vSwitch does not exist. Check whether the specified ID is valid. |
| 400 | InvalidVSwitchName.Ma lformed | Specified virtual switch name is not valid. | The error message returned because the format of the specified vSwitch name is invalid. Check whether the specified name is valid. |
| 400 | InvalidVSwitchDiscriptio n.Malformed | Specified virtual switch description is not valid. | The error message returned because the format of the specified vSwitch description is invalid. Check whether the specified description is valid. |
| 400 | InvalidVSwitchDiscriptio n.Malformed | Specified virtual switch description is not valid. | The error message returned because the specified description of the vSwitch is invalid. |

#### DescribeVSwitchAttributes

Queries detailed information about a vSwitch. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVSwitchAttr ibutes | The operation that you want to perform. Set the value to DescribeVSwit chAt t ribut es. |
| VSwitchId | String | Yes | vsw-25naue4g**** | The ID of the vSwitch that you want to query. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the vSwitch is deployed. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DryRun | Boolean | No | false | Specifies whether to precheck this request. Valid values: t rue: prechecks the API request. Resources are not queried. The system checks whether your AccessKey pair is valid, whether the RAM user is authorized, and whether required parameters are set. If the request fails the precheck, an error message is returned. If the request passes the precheck, the DryRunOperation error code is returned. f alse: sends the request. This is the default value. If the request passes the precheck, a 2XX HTTP status code is returned and the resource is queried. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AvailableIpAddres sCount | Long | 12 | The number of available IP addresses. |
| CidrBlock | String | 192.168.0.1/24 | The IPv4 CIDR block of the vSwitch. |
| CloudResources | Array of CloudResourceSet Type |   | The list of resources deployed in the VPC. |
| CloudResourceSet Type |   |   |   |
| ResourceCount | Integer | 1 | The number of resources deployed in the VPC. |
| ResourceType | String | VSwitch | The types of resources deployed in the VPC. Valid values: VSwit ch: vSwitches VRout er: vRouters Rout eT able: route tables |
| CreationTime | String | 2017-08-22T10:40:25Z | The time when the vSwitch was created. |
| Description | String | abc | The description of the vSwitch. |
| Ipv6CidrBlock | String | 2408:XXXX:0:2900::/6 4 | The IPv6 CIDR block of the vSwitch. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IsCgw | Boolean | false | Indicates whether the gateway is a customer gateway. Valid values: t rue: yes f alse (default): no |
| IsDefault | Boolean | false | Indicates whether the vSwitch is the default vSwitch. Valid values: t rue: yes f alse (default): no |
| NetworkAclId | String | nacl- 2zesich96aa37rl29**** | The ID of the network ACL that is associated with the vSwitch. |
| OwnerId | Long | 12345678 | The ID of the Alibaba Cloud account to which the vSwitch belongs. |
| RequestId | String | 7B48B4B9-1EAD-469F- B488-594DAB4B6A1A | The ID of the request. |
| ResourceGroupId | String | rg-acfmxazb4pbgfh**** | The ID of the resource group. |
| RouteTable | Struct |   | The information about the route table that is associated with the vSwitch. |
| RouteTableId | String | vtb- bp145q7glnuzdv**** | The ID of the route table that is associated with the vSwitch. |
| RouteTableType | String | System | The type of the route table. Syst em : a system route table Cust om: a custom route table |
| Status | String | Pending | The state of the vSwitch. Valid values: Pending: The vSwitch is being configured. Available: The vSwitch is available. |
| VSwitchId | String | vsw-25b7pcdfvv15t**** | The ID of the vSwitch. |
| VSwitchName | String | test | The name of the vSwitch. |
| VpcId | String | vpc-257gqcfv642n**** | The ID of the VPC to which the vSwitch belongs. |
| ZoneId | String | cn-qingdao-env17- amtest11001-a | The ID of the zone to which the vSwitch belongs. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVSwitchAttributes &VSwitchId=vsw-25naue4g**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVSwitchAttributesResponse>
  <IsDefault>false</IsDefault>
  <Status>Pending</Status>
  <Description>abc</Description>
  <NetworkAclId>nacl-2zesich96aa37rl29****</NetworkAclId>
  <ResourceGroupId>rg-acfmxazb4pbgfh****</ResourceGroupId>
  <ZoneId>cn-qingdao-env17-amtest11001-a</ZoneId>
  <RequestId>7B48B4B9-1EAD-469F-B488-594DAB4B6A1A</RequestId>
  <AvailableIpAddressCount>12</AvailableIpAddressCount>
  <VSwitchId>vsw-25b7pcdfvv15t****</VSwitchId>
  <CidrBlock>192.168.0.1/24</CidrBlock>
  <RouteTable>
        <RouteTableId>vtb-bp145q7glnuzdv****</RouteTableId>
        <RouteTableType>System</RouteTableType>
  </RouteTable>
  <IsCgw>false</IsCgw>
  <OwnerId>12345678</OwnerId>
  <VpcId>vpc-257gqcfv642n****</VpcId>
  <CreationTime>2017-08-22T10:40:25Z</CreationTime>
  <VSwitchName>test</VSwitchName>
  <Ipv6CidrBlock>2408:XXXX:0:2900::/64</Ipv6CidrBlock>
  <CloudResources>
        <ResourceCount>1</ResourceCount>
        <ResourceType>VSwitch</ResourceType>
  </CloudResources>
</DescribeVSwitchAttributesResponse>
```

`JSON` format `{`

```json
    "IsDefault": false,
    "Status": "Pending",
    "Description": "abc",
    "NetworkAclId": "nacl-2zesich96aa37rl29****",
    "ResourceGroupId": "rg-acfmxazb4pbgfh****",
    "ZoneId": "cn-qingdao-env17-amtest11001-a",
    "RequestId": "7B48B4B9-1EAD-469F-B488-594DAB4B6A1A",
    "AvailableIpAddressCount": 12,
    "VSwitchId": "vsw-25b7pcdfvv15t****",
    "CidrBlock": "192.168.0.1/24",
    "RouteTable": {
        "RouteTableId": "vtb-bp145q7glnuzdv****",
        "RouteTableType": "System"
```

`},`

```json
    "IsCgw": false,
    "OwnerId": 12345678,
    "VpcId": "vpc-257gqcfv642n****",
    "CreationTime": "2017-08-22T10:40:25Z",
    "VSwitchName": "test",
    "Ipv6CidrBlock": "2408:XXXX:0:2900::/64",
    "CloudResources": {
        "ResourceCount": 1,
        "ResourceType": "VSwitch"
```

### vRouter

#### ModifyVRouterAttribute

Modifies the name and description of a vRouter. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVRouterAttrib ute | The operation that you want to perform. Set the value to Modif yVRout erAt t ribut e. |
| VRouterId | String | Yes | vrt- bp1lhl0taikrteen8*** * | The ID of the vRouter. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the vRouter is deployed. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VRouterName | String | No | VRouter-1 | The name of the vRouter to be modified. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter but cannot start with http:// or https:// . |
| Description | String | No | My VRouter | The description of the vRouter to be modified. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=ModifyVRouterAttribute &VRouterId=vrt-bp1lhl0taikrteen8**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVRouterAttributeResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ModifyVRouterAttributeResponse>
```

`JSON` format `{`

```json
    "ModifyVRouterAttributeResponse": {
        "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVRouterId.NotFou nd | Specified virtual router does not exist. | The error message returned because the specified vRouter does not exist. Check whether the specified vRouter is valid. |
| 400 | InvalidVRouterName.Ma lformed | Specified virtual router name is not valid. | The error message returned because the name format of the specified vRouter is invalid. |
| 400 | InvalidVRouterDiscriptio n.Malformed | Specified virtual router description is not valid. | The error message returned because the description format of the specified vRouter is invalid. |
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because required parameters are not set. Check whether you have set all the required parameters before you call this operation. |

#### DescribeVRouters

Queries vRouters in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVRouters | The operation that you want to perform. Set the value to DescribeVRout ers. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the vRouter that you want to query. You can call the DescribeRegions operation to query the most recent region list. |
| VRouterId | String | No | vrt- bp1lhl0taikrteen**** | The ID of the vRouter. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VRouters | Array of VRouter |   | The details about the vRouters. |
| VRouter |   |   |   |

| Virtual Private Clou | d |   | Developer Guide·API reference |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreationTime | String | 2018-03-22T07:46:20Z | The time when the vRouter was created. |
| Description | String | abc | The description of the vRouter. |
| RegionId | String | cn-hangzhou | The region ID of the vRouter. |
| RouteTableIds | List | { "RouteTableId": [ "vtb- rj9ybe3y0u41mmjsp**** "] } | The ID of the route table in the vRouter. |
| VRouterId | String | vrt- rj98khsezfqpjrxmv**** | The ID of the vRouter. |
| VRouterName | String | doctest | The name of the vRouter. |
| VpcId | String | vpc- rj905wotv6y030t1**** | The ID of the virtual private cloud (VPC) to which the vRouter belongs. |
| TotalCount | Integer | 1 | The number of returned entries. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVRouters &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVRoutersResponse>
    <PageNumber>1</PageNumber>
    <TotalCount>2</TotalCount>
    <VRouters>
        <VRouter>
            <VRouterName></VRouterName>
            <RouteTableIds>
                <RouteTableId>vtb-bp1krxxzp0c29fmo****</RouteTableId>
            </RouteTableIds>
            <CreationTime>2018-12-06T06:11:55Z</CreationTime>
            <Description></Description>
            <RegionId>cn-hangzhou</RegionId>
            <VRouterId>vrt-bp1jcg5cmxjbl9xgc****</VRouterId>
            <VpcId>vpc-bp1qpo0kug3a20qqe****</VpcId>
        </VRouter>
        <VRouter>
            <VRouterName></VRouterName>
            <RouteTableIds>
                <RouteTableId>vtb-bp1blq1oh0ybfnpm****</RouteTableId>
            </RouteTableIds>
            <CreationTime>2018-11-08T08:54:03Z</CreationTime>
            <Description></Description>
            <RegionId>cn-hangzhou</RegionId>
            <VRouterId>vrt-bp149ve7yeyvio4nc****</VRouterId>
            <VpcId>vpc-bp1aevy8sofi8mh1q****</VpcId>
        </VRouter>
    </VRouters>
    <PageSize>10</PageSize>
    <RequestId>EE4C2417-9437-4333-BDEB-8493F7AA7258</RequestId>
</DescribeVRoutersResponse>
```

`JSON` format `{`

```json
    "PageNumber": 1,
    "TotalCount": 1,
    "VRouters": {
        "VRouter": [
```

`{`

```json
                "VRouterName": "",
                "RouteTableIds": {
                    "RouteTableId": [
                        "vtb-rj9ybe3y0u41mmjsp****"
```

`]` `},`

```json
                "CreationTime": "2018-03-22T07:46:20Z",
                "Description": "",
                "RegionId": "us-west-1",
                "VRouterId": "vrt-rj98khsezfqpjrxmv****",
                "VpcId": "vpc-rj905wotv6y030t1z****"
```

`]` `},`

```json
    "PageSize": 10,
    "RequestId": "CB2793A8-845F-444C-8E93-76F1BBDF9C78"
```

### Route table

#### CreateRouteTable

Creates a custom route table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRouteTable | The operation that you want to perform. Set the value to Creat eRout eT able. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the virtual private cloud (VPC) to which the custom route table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- bp1qpo0kug3a20qq e**** | The ID of the VPC to which the custom route table belongs. |
| RouteTableName | String | No | myRouteTable | The name of the route table. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | abc | The description of the route table. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 62172DD5-6BAC-45DF- 8D44-E11ED28DCAC0 | The ID of the request. |
| RouteTableId | String | vtb- bp145q7glnuzdvzu2*** * | The ID of the route table. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateRouteTable &RegionId=cn-qingdao-env17-d01 &VpcId=vpc-bp1qpo0kug3a20qqe**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateRouteTableResponse>
      <RequestId>62172DD5-6BAC-45DF-8D44-E11ED28DCAC0</RequestId>
      <RouteTableId>vtb-bp145q7glnuzdvzu2****</RouteTableId>
</CreateRouteTableResponse>
```

`JSON` format `{`

```json
    "RequestId": "62172DD5-6BAC-45DF-8D44-E11ED28DCAC0",
    "RouteTableId": "vtb-bp145q7glnuzdvzu2****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter.Descri ption.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |
| 404 | InvalidVpcId.NotFound | Specified VPC does not exist. | The error message returned because the specified VPC does not exist. |

#### CreateRouteEntry

Adds a custom route entry to the route table of a vRouter or a virtual border router (VBR). Descriptions When you call t his operat ion t o add a cust om rout e ent ry t o t he rout e t able of a vRout er, t ake not e of t he f ollowing limit s: The number of custom route entries in a route table cannot exceed 48. The destination CIDR block (Dest inat ionCidrBlock) of a custom route entry cannot be the same as or overlap with the CIDR block of a vSwitch in the virtual private cloud (VPC). The destination CIDR block (Dest inat ionCidrBlock) of a custom route entry cannot be 100.64.0.0/10 or a subset of it. The destination CIDR blocks (Dest inat ionCidrBlock) of route entries in the same route table must be unique. If you do not include the mask length when you specify the destination CIDR block (Dest inat ionCidrBlock), the destination CIDR block is considered a host IP address whose mask length is 32 bits. Multiple custom route entries can be destined for the same next hop (Next HopId). The next hop (Next HopId) of a custom route entry must belong to the same VPC as the route table. Equal-cost multi-path (ECMP) route entries can be configured by specifying the Next HopList parameter. If you want to add a non-ECMP route entry, you must specify Dest inat ionCidrBlock, Next HopT ype, and Next HopId, and you cannot specify Next HopList . If you want to add an ECMP route entry, you must specify Dest inat ionCidrBlock and Next HopList , and you cannot specify Next HopT ype or Next HopId. When you call t his operat ion t o add a cust om rout e ent ry t o t he rout e t able of a VBR, t ake not e of t he f ollowing limit s: The number of custom route entries in a route table cannot exceed 48. The Next HopList parameter is not supported. The destination CIDR block (Dest inat ionCidrBlock) of a custom route entry cannot be 100.64.0.0/10 or a subset of it. The destination CIDR blocks (Dest inat ionCidrBlock) of route entries in the same route table must be unique. If you do not include the mask length when you specify the destination CIDR block (Dest inat ionCidrBlock), the destination CIDR block is considered a host IP address whose mask length is 32 bits. Multiple custom route entries can be destined for the same next hop (Next HopId). The next hop (Next HopId) of a custom route entry must be a router interface associated with the VBR. You can add route entries only when the VBR is in the Act ive state, and the Express Connect circuit associated with the VBR is in the Enabled state. Only non-ECMP route entries are supported. When you add non-ECMP route entries, you must specify Dest inat ionCidrBlock, Next HopT ype, and Next HopId, and you cannot specify Next HopList . Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRouteEntry | The operation that you want to perform. Set the value to Creat eRout eEnt ry. |
| DestinationCidrBlock | String | Yes | 192.168.0.0/24 | The destination CIDR block of the custom route entry. Both IPv4 and IPv6 CIDR blocks are supported. Make sure that the destination CIDR block meets the following requirements: The destination CIDR block is not 100.64.0.0/10 or a subset of 100.64.0.0/10. The destination CIDR block of the custom route entry is different from the destination CIDR blocks of other route entries in the same route table. If the specified destination CIDR block is an IPv4 address, a 32-bit subnet mask is used. If the specified destination CIDR block is an IPv6 address, a 128-bit subnet mask is used. |
| RouteTableId | String | Yes | vtb- bp145q7glnuzd**** | The ID of the route table to which you want to add a custom route entry. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the route table. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NextHopId | String | No | ri-2zeo3xzyf38r4**** | The ID of the next hop. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate a value, but you must make sure that it is unique among different requests. Client T oken can contain only ASCII characters. It cannot exceed 64 characters in length. |
| RouteEntryName | String | No | test | The name of the custom route entry that you want to add. The name must be 2 to 128 characters in length and can contain digits, underscores ( ), and hyphens (-). The name must start _ with a letter. |
| Description | String | No | abc | The description of the custom route entry. |
| NextHopType | String | No | RouterInterface | The type of the next hop of the custom route entry. Valid values: Inst ance: an Elastic Compute Service (ECS) instance. This is the default value. HaVip: a high-availability virtual IP address (HAVIP). Rout erInt erf ace: a router interface. Net workInt erf ace: an elastic network interface (ENI). VpnGat eway: a VPN gateway. IPv6Gat eway: an IPv6 gateway. Nat Gat eway: a NAT gateway. |
| NextHopList.N.Next HopType | String | No | RouterInterface | The type of the next hop of the ECMP route entry. Set the value to Rout erInt erf ace (router interface). |
| NextHopList.N.Next HopId | String | No | ri- 2zeo3xzyf3cd8r4*** * | The ID of the next hop of the ECMP route entry. |
| NextHopList.N.Weig ht | Integer | No | 10 | The weight of the next hop of the ECMP route entry. Valid values: 0 to 100. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateRouteEntry &DestinationCidrBlock=192.168.0.0/24 &RouteTableId=vtb-bp145q7glnuzd**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateRouteEntryResponse> <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId> <CreateRouteEntryResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidInstanId.NotFoun d | Specified instance does not exist. | The error message returned because the specified instance does not exist. Check whether the instance ID is valid. |
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because one or more required parameters are not set. Check whether you have set all the required parameters before you call this operation. |
| 400 | InvalidCidrBlock.Malfor med | Specified CIDR block is not valid. | The error message returned because the format of the specified CIDR block is invalid. |
| 404 | InvalidNextHopId.NotFo und | Specified next hop does not exist. | The error message returned because the specified next hop does not exist. |
| 404 | InvalidRouteTableId.Not Found | Specified route table does not exist. | The error message returned because the specified route table does not exist. |
| 400 | InvalidCIDRBlock.Duplica te | Specified CIDR block is already exists. | The error message returned because the specified CIDR block already exists in the route table. |
| 400 | IncorrectVpcStatus | Current VPC status does not support this operation. | The error message returned because this operation cannot be performed while the VPC is in the current state. |
| 400 | IncorrectInstanceStatus | Current instance status does not support this operation. | The error message returned because this operation cannot be performed while the instance is in the current state. |

| Developer Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded | Route entry quota exceeded in this route table. | The error message returned because the number of route entries in the route table has reached the upper limit. |
| 400 | IncorrectRouteEntryStat us | Some route entry status blocked this operation. | The error message returned because one or more route entries in the current route table are in the Pending or Modifying state. |
| 400 | InvalidCidrBlock | Specified CIDR block is not valid. | The error message returned because: 1.You are unauthorized to use the 10.0.0.0/8 CIDR block. Check whether your account is included in the whitelist to use the CIDR block. 2.The destination CIDR block of the added custom route entry cannot be a subset of the CIDR blocks of the vSwitches in the VPC. 3.The CIDR block cannot be 100.64.0.0/10. |
| 400 | InvalidNextHopType | Specified parameter "NextHopType" is not valid | The error message returned because the specified next hop type is invalid. |
| 400 | InvalidNextHop.NotFou nd | Specified next hop does not exist. | The error message returned because the specified next hop does not exist. |
| 400 | InvalidVRouter.NotFoun d | vRouter not exists. | The error message returned because the specified vRouter does not exist. Check whether the specified vRouter is valid. |
| 400 | InvalidVPC.NotFound | vpc not exists. | The error message returned because the specified VPC does not exist. Check whether the specified VPC is valid. |
| 400 | InvalidNexthopTypeAnd List.BothNull | both nexthopType and nextHopList are null. | The error message returned because the NextHopType and NextHopList parameters are not specified. |
| 400 | InvalidNexthopTypeAnd List.BothNotNull | both nexthopType and nextHopList are not null. | The error message returned because you cannot leave both the NextHopType and the NextHopList parameters empty. |
| 400 | InvalidRouterInterface | invalid router interface. | The error message returned because the specified router interface does not exist. |
| 400 | InvalidOppositeRouterT ype | nexthop list cannot only contain router interface whose opposite router interface is on vbr. | The error message returned because the specified next hop is invalid. The peer router of the router interface that you specify as the next hop must be a VBR. |
| 400 | InvalidNexthopListSize | nexthop size is illegal. Must be between 2 and 4. | The error message returned because you must specify two to four router interfaces as next hops. |

| Virtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidEntryRuleQuota.N otFound | Route entry quota rule not exists. | The error message returned because the quota of route entries does not exist. |
| 400 | Forbidden.CheckEntryRu leQuota | Route entry quota rule check error. | The error message returned because an error occurred when the system was checking the quota of route entries. |
| 400 | InvalidVBRStatus | invalid virtual border router status. | The error message returned because the VBR is in an invalid state. |
| 400 | InvalidPhysicalConnectio nBusinessStatus | invalid physical connection business status. | The error message returned because the Express Connect circuit is in an invalid state. |
| 404 | InvalidHaVipId.NotFoun d | The specified HaVip does not exist in the specified VPC. | The error message returned because the specified HAVIP does not exist in the VPC. |
| 400 | IncorrectHaVipStatus | This operation is denied because satus of the specified HaVip is neither Available nor InUse. | The error message returned because you cannot perform the operation when the specified HAVIP is in the Available or InUse state. |
| 400 | CountLimitExceed.HaVip RouteEntry | There can be 5 route entry to HaVip at most in one route table. | The error message returned because the number of route entries that point to the HAVIP has reached the upper limit. |
| 400 | InvalidRouteEntry.Duplic ate | The route entry already exist. | The error message returned because the specified route entry already exists. |
| 403 | IncorrectInstanceStatus | The current status of the resource does not support this operation. | The error message returned because the specified resource is in a state that does not support the operation. |
| 400 | IncorrectRouteEntryStat us | Specified routeEntry status error. | The error message returned because one or more route entries in the current route table are in the Pending or Modifying state. |
| 400 | IncorrectRouteEntryStat us | VBR has NotStable route entry. | The error message returned because one or more route entries in the current VBR are in the Pending or Modifying state. |
| 400 | InvalidParam | The Ecmp routerEntry with router interfaces local vgw vip not match. | The error message returned because the route entry does not match the gateway IP address of the router interface. |
| 400 | INVALID WEIGHT PARAM _ _ | Specified value of weight invalid | The error message returned because the specified weight is invalid. |
| 400 | FORBIDDEN USE VPC AS _ _ _ INTERNET GATEWAY _ _ | The Specified CIDR must be in vpc CIDR. | The error message returned because the specified CIDR block must be a subset of the VPC CIDR block. |

| Developer Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | INVALID VPC ID _ _ | The Specified VpcId not match. | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidRouteEntrySize | The Specified routerEntry size not legal. | The error message returned because you must specify two to four router interfaces as next hops if you want to configure ECMP routing. |
| 400 | InvalidRouteEntry | Specified routeEntry not exist. | The error message returned because the specified route entry does not exist. |

#### DeleteRouteEntry

Deletes a custom route entry from a route table. Descriptions When you call this operation, take note of the following rules: You can delete only a custom route entry that is in the Available state. You cannot delete a custom route entry from a virtual private cloud (VPC) where a vSwitch is being created or deleted. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteRouteEntry | The operation that you want to perform. Set the value to Delet eRout eEnt ry. |
| DestinationCidrBlock | String | Yes | 10.0.0.0/16 | The destination CIDR block of the route entry. IPv4 and IPv6 CIDR blocks are supported. |
| RouteTableId | String | Yes | vtb- hp37isva36oj7839j** ** | The ID of the route table to which the route entry belongs. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the route table to which the route entry belongs. You can call the DescribeRegions operation to query the most recent region list. |
| RouteEntryId | String | No | rte- bp1mnnr2al0naomn **** | The ID of the route entry that you want to delete. |
| NextHopId | String | No | ngw- bp1vpo4l2vd7zef8o **** | The ID of the next hop. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NextHopList.N.Next HopType | String | No | RouterInterface | The type of the next hop of the ECMP route. Set the value to Rout erInt erf ace (router interface). |
| NextHopList.N.Next HopId | String | No | ri- 2zeo3xzyf38r43cd** ** | The ID of the next hop of the ECMP route. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteRouteEntry &DestinationCidrBlock=10.0.0.0/16 &RouteTableId=vtb-hp37isva36oj7839j**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteRouteEntryResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteRouteEntryResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | MissingParameter | Either nexthopId or nextHopList should be specified | The error message returned because nexthopId or nextHopList is not set. |
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because one or more required parameters are not set. Check whether you have set all the required parameters before you call this operation. |
| 400 | IncorrcetRouteEntryStat us | Some route entry status blocked this operation. | The error message returned because one or more route entries in the route table are in the Pending or Modifying state. |

|   | Developer Guid | e·API reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidCidrBlock.Malfor med | Specified CIDR block is not valid. | The error message returned because the format of the specified CIDR block is invalid. |
| 404 | InvalidRouteTableId.Not Found | Specified route table does not exist. | The error message returned because the specified route table does not exist. |
| 400 | OperationDenied | Specified operation is denied as route entry type is system. | The error message returned because the specified route entry is a system route entry. |
| 400 | InvalidRouteEntry.NotFo und | Route entry not exists. | The error message returned because the specified route entry does not exist. Check whether the specified route entry is valid. |
| 400 | InvalidVRouter.NotFoun d | vRouter not exists. | The error message returned because the specified vRouter does not exist. Check whether the specified vRouter is valid. |
| 400 | IncorrectRouteEntryStat us | Some route entry status blocked this operation. | The error message returned because one or more route entries in the current route table are in the Pending or Modifying state. |
| 400 | IncorrectRouteEntryStat us | VBR has NotStable route entry. | The error message returned because one or more route entries in the current virtual border router (VBR) are in the Pending or Modifying state. |
| 404 | InvalidVpcId.NotFound | Specified value of VpcId is not found in our record. | The error message returned because the specified VPC does not exist. Check whether the specified VPC is valid. |
| 400 | IncorrectRouteEntryStat us | Specified routeEntry status error. | The error message returned because one or more route entries in the current route table are in the Pending or Modifying state. |
| 400 | Forbbiden | Specified RouteEntry cannot allowed delete by openApi. | The error message returned because you cannot call this operation to delete the specified route entry. |
| 400 | InvalidNextHop | Specified nexthop and nexthop list cannot both null. | The error message returned because the next hop and next hop list cannot be empty at the same time. |
| 400 | InvalidRouteEntry | Specified routeEntry not exist. | The error message returned because the specified route entry does not exist. |
| 400 | IncorrectVpcStatus | Current VPC status does not support this operation. | The error message returned because this operation cannot be performed while the VPC is in the current state. |

#### DescribeRouteEntryList

Queries information about route entries in a route table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRouteEntryL ist | The operation that you want to perform. Set the value to DescribeRout eEnt ryList . |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the route table to which the route entries belong. You can call the DescribeRegions operation to query the most recent region list. |
| RouteTableId | String | Yes | vtb- bp1r9pvl4xen8s9ju** ** | The ID of the route table that you want to query. |
| RouteEntryId | String | No | rte- bp1mnnr2al0naomn p**** | The ID of the route entry that you want to query. |
| DestinationCidrBlock | String | No | 192.168.2.0/24 | The destination CIDR block of the route entry. IPv4 and IPv6 CIDR blocks are supported. Not e Only the Alibaba Cloud China site supports IPv6 CIDR blocks. |
| RouteEntryName | String | No | abc | The name of the route entry. |
| IpVersion | String | No | IPv4 | The IP version. Valid values: IPv4: IPv4 IPv6: IPv6 Not e Only the Alibaba Cloud China site supports IPv6. |
| RouteEntryType | String | No | System | The type of the route entry. Valid values: Cust om: a custom route entry Syst em: a system route entry |
| NextHopId | String | No | vpn- bp10zyaph5cc8b7c7 **** | The ID of the next hop. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NextHopType | String | No | Instance | The type of the next hop. Valid values: Inst ance: an Elastic Compute Service (ECS) instance HaVip: a high-availability virtual IP address (HAVIP) VpnGat eway: a VPN gateway Nat Gat eway: a NAT gateway Net workInt erf ace: a secondary elastic network interface (ENI) Rout erInt erf ace: a router interface IPv6Gat eway: an IPv6 gateway |
| MaxResult | Integer | No | 50 | The number of entries to return on each page. Valid values: 20 to 100. Default value: 50. |
| NextToken | String | No | caeba0bbb2be03f8 4eb48b699f0a4**** | The token used to start the next query. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NextToken | String | caeba0bbb2be03f84eb 48b699f0a4**** | The token used to start the next query. |
| RequestId | String | 14A07460-EBE7-47CA- 9757-12CC4761D47A | The ID of the request. |
| RouteEntrys | Array of RouteEntry |   | The information about the route entries. |
| RouteEntry |   |   |   |
| Description | String | RouteEntryDescription | The description of the route entry. |
| DestinationCidrBlo ck | String | 10.0.0.0/24 | The destination CIDR block of the route entry. |
| IpVersion | String | IPv4 | The IP version. Valid values: IPv4: IPv4 IPv6: IPv6 |
| NextHops | Array of NextHop |   | The information about the next hops. |
| NextHop |   |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Enabled | Integer | 0 | Indicates whether the route entry is available. Valid values: 0: unavailable 1: available |
| NextHopId | String | vpn- bp10zyaph5cc8b7c7*** * | The ID of the next hop. |
| NextHopRegionId | String | cn-qingdao-env17-d01 | The region ID of the next hop. |
| NextHopRelatedIn fo | Struct |   | The information about the instance associated with the next hop. |
| InstanceId | String | vpc- bp1t36rn9l53iwbsf**** | The ID of the instance associated with the next hop. |
| InstanceType | String | VPC | The type of the instance associated with the next hop. Valid values: VPC: a virtual private cloud (VPC) VBR: a virtual border router (VBR) |
| RegionId | String | ch-qingdao-env17-d01 | The region ID of the instance associated with the next hop. Valid values: |
| NextHopType | String | Instance | The type of the next hop. Valid values: Inst ance: an ECS instance HaVip: an HAVIP VpnGat eway: a VPN gateway Nat Gat eway: a NAT gateway Net workInt erf ace: a secondary ENI Rout erInt erf ace: a router interface IPv6Gat eway: an IPv6 gateway Not e Only the Alibaba Cloud China site supports IPv6 gateways as next hops. |
| Weight | Integer | 100 | The weight of the route entry. |
| RouteEntryId | String | rte- bp1mnnr2al0naomnp** ** | The ID of the route entry. |
| RouteEntryName | String | aaa | The name of the route entry. |

|   | Developer Guide·AP | I reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RouteTableId | String | vtb- bp15w5q90d2rk3bww* *** | The ID of the route table. |
| Status | String | Available | The status of the route entry. Valid values: Pending: being configured Available: available Modif ying: being modified |
| Type | String | Custom | The type of the route entry. Valid values: Cust om: a custom route entry Syst em: a system route entry |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRouteEntryList &RegionId=cn-qingdao-env17-d01 &RouteTableId=vtb-bp1r9pvl4xen8s9ju**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRouteEntryListResponse>
  <NextToken>caeba0bbb2be03f84eb48b699f0a4****</NextToken>
  <RequestId>14A07460-EBE7-47CA-9757-12CC4761D47A </RequestId>
  <RouteEntrys>
        <Status>Available</Status>
        <RouteEntryId>rte-bp1mnnr2al0naomnp****</RouteEntryId>
        <Type>Custom</Type>
        <Description>RouteEntryDescription</Description>
        <RouteTableId>vtb-bp15w5q90d2rk3bww****</RouteTableId>
        <IpVersion>IPv4</IpVersion>
        <RouteEntryName>aaa</RouteEntryName>
        <DestinationCidrBlock>10.0.0.0/24</DestinationCidrBlock>
        <NextHops>
              <NextHopRegionId>cn-qingdao-env17-d01</NextHopRegionId>
              <NextHopType>Instance</NextHopType>
              <NextHopId>vpn-bp10zyaph5cc8b7c7****</NextHopId>
              <Enabled>0</Enabled>
              <Weight>100</Weight>
              <NextHopRelatedInfo>
                    <InstanceId>vpc-bp1t36rn9l53iwbsf****</InstanceId>
                    <RegionId>ch-qingdao-env17-d01</RegionId>
                    <InstanceType>VPC</InstanceType>
              </NextHopRelatedInfo>
        </NextHops>
  </RouteEntrys>
</DescribeRouteEntryListResponse>
```

`JSON` format `{`

```json
    "NextToken": "caeba0bbb2be03f84eb48b699f0a4****",
    "RequestId": "14A07460-EBE7-47CA-9757-12CC4761D47A",
    "RouteEntrys": {
        "Status": "Available",
        "RouteEntryId": "rte-bp1mnnr2al0naomnp****",
        "Type": "Custom",
        "Description": "RouteEntryDescription",
        "RouteTableId": "vtb-bp15w5q90d2rk3bww****",
        "IpVersion": "IPv4",
        "RouteEntryName": "aaa",
        "DestinationCidrBlock": "10.0.0.0/24",
        "NextHops": {
            "NextHopRegionId": "cn-qingdao-env17-d01",
            "NextHopType": "Instance",
            "NextHopId": "vpn-bp10zyaph5cc8b7c7****",
            "Enabled": 0,
            "Weight": 100,
            "NextHopRelatedInfo": {
                "InstanceId": "vpc-bp1t36rn9l53iwbsf****",
                "RegionId": "ch-qingdao-env17-d01",
                "InstanceType": "VPC"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | OperationFailed.QueryC enEntry | Operation is denied because getting CEN route entry has failed. | The error message returned because the system cannot obtain the Cloud Enterprise Network (CEN) routes. |

#### ModifyRouteEntry

Modifies the name and description of a custom route entry. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyRouteEntry | The operation that you want to perform. Set the value to Modif yRout eEnt ry. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region to which the route entry belongs. You can call the DescribeRegions operation to query the most recent region list. |
| RouteEntryId | String | Yes | rte- acfvgfsghfdd**** | The ID of the custom route entry. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RouteEntryName | String | No | EntryName | The name of the route entry. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter but cannot start with http:// or https:// . |
| Description | String | No | EntryDescription | The description of the route entry. The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 861E6630-AEC0-4B2D- B214-6CB5E44B7F04 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyRouteEntry &RegionId=cn-qingdao-env17-d01 &RouteEntryId=rte-acfvgfsghfdd**** &<Common request parameters>
```

Sample success response `XML` format

```xml
<ModifyRouteEntryResponse>
    <RequestId>861E6630-AEC0-4B2D-B214-6CB5E44B7F04</RequestId>
</ModifyRouteEntryResponse>
```

`JSON` format `{`

```json
 "RequestId": "861E6630-AEC0-4B2D-B214-6CB5E44B7F04"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the permissions and try again. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidRouteEntryId.Not Found | The specified routeEntry does not exist. | The error message returned because the specified route entry does not exist. |

#### AssociateRouteTable

Associates a custom route table with a vSwitch in the same virtual private cloud (VPC). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociateRouteTabl e | The operation that you want to perform. Set the value to Associat eRout eT able. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the VPC to which the route table belongs. You can call the DescribeRegions operation to the most recent region list. |
| RouteTableId | String | Yes | vtb- bp145q7glnuzdvzu2 **** | The ID of the route table. |
| VSwitchId | String | Yes | vsw- 25ncdvfaue4**** | The ID of the vSwitch. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DC668356-BCB4-42FD- 9BC3-FA2B2E04B634 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AssociateRouteTable &RegionId=cn-qingdao-env17-d01 &RouteTableId=vtb-bp145q7glnuzdvzu2**** &VSwitchId=vsw-25ncdvfaue4**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AssociateRouteTableResponse>
  <RequestId>DC668356-BCB4-42FD-9BC3-FA2B2E04B634</RequestId>
</AssociateRouteTableResponse>
```

`JSON` format

```json
{"RequestId":"DC668356-BCB4-42FD-9BC3-FA2B2E04B634"}
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRouteTableId.Not Found | Specified route table does not exist. | The error message returned because the specified route table does not exist. |

#### DeleteRouteTable

Deletes a custom route table. Descriptions Before you delete a custom route table, disassociate the vSwitch that is associated with the custom route table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteRouteTable | The operation that you want to perform. Set the value to Delet eRout eT able. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the virtual private cloud (VPC) to which the route table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| RouteTableId | String | Yes | vtb- bp145q7glnuzdvzu2 **** | The ID of the route table to be deleted. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DC668356-BCB4-42FD- 9BC3-FA2B2E04B634 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteRouteTable &RegionId=cn-qingdao-env17-d01 &RouteTableId=vtb-bp145q7glnuzdvzu2**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteRouteTableResponse>
      <RequestId>DC668356-BCB4-42FD-9BC3-FA2B2E04B634</RequestId>
</DeleteRouteTableResponse>
```

`JSON` format `{`

```json
  "RequestId": "DC668356-BCB4-42FD-9BC3-FA2B2E04B634"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorrectVSwitchStatus | The current virtual switch status does not support this operation. | The error message returned because the vSwitch is in the Configuring state and cannot be deleted. |

#### DescribeRouteTableList

Queries route tables. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRouteTable List | The operation that you want to perform. Set the value to DescribeRout eT ableList . |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the virtual private cloud (VPC) to which the route table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| RouterType | String | No | VBR | The type of the router to which the route table belongs. Valid values: VRout er (default): a vRouter VBR: a virtual border router (VBR) |
| RouterId | String | No | vrt- bp1lhl0taikrteen8*** * | The ID of the router to which the route table belongs. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpcId | String | No | vpc- bp15zckdt37pq72** ** | The ID of the VPC to which the route table belongs. When this parameter is specified, the value of the Rout erT ype parameter is automatically set to VRout er. |
| RouteTableId | String | No | vtb- bp145q7glnuzdvzu2 **** | The ID of the route table that you want to query. |
| RouteTableName | String | No | doctest | The name of the route table that you want to query. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| ResourceGroupId | String | No | rg-acfmxazb4ph**** | The ID of the resource group to which the route table to be queried belongs. |
| Tag.N.Key | String | No | Key1 | The tag key. |
| Tag.N.Value | String | No | Value1 | The tag value. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. Not e The HTTP status code 200 indicates that the call was successful. |
| Message | String | successful | The returned message. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | DC668356-BCB4-42FD- 9BC3-FA2B2E04B634 | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RouterTableList | Array of RouterTableListTy pe |   | The list of route tables. |
| RouterTableListTy pe |   |   |   |
| CreationTime | String | 2017-08-22T10:40:25Z | The time when the route table was created. |
| Description | String | This is Route Table. | The description of the route table. |
| OwnerId | Long | 12345678 | The ID of the Apsara Stack tenant account to which the route table belongs. |
| ResourceGroupId | String | rg-acfmxazb4ph**** | The ID of the resource group to which the route table belongs. |
| RouteTableId | String | vtb- bp145q7glnuzdvzu2*** * | The ID of the route table. |
| RouteTableName | String | doctest | The name of the route table. |
| RouteTableType | String | System | The type of the route table. Cust om: a custom route table Syst em: a system route table |
| RouterId | String | vrt- bp1lhl0taikrteen8**** | The ID of the router to which the route table belongs. |
| RouterType | String | VBR | The type of the router to which the route table belongs. Valid values: VRout er: a vRouter VBR: a virtual border router (VBR) |
| Status | String | Available | The status of the route table. Pending: The route table is being configured. Available: The route table is available. |
| Tags | Array of Tag |   | The tags of the route table. |
| Tag |   |   |   |
| Key | String | type | The key of the tag that is added to the route table. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Value | String | ingress | The value of the tag that is added to the route table. |
| VSwitchIds | List | vsw- bp12mw1f8k3jgygk9*** * | The list of vSwitches deployed in the VPC. |
| VpcId | String | vpc- bp15zckdt37pq72**** | The ID of the VPC to which the route table belongs. |
| Success | Boolean | true | Indicates whether the call is successful. Valid values: t rue: yes f alse: no |
| TotalCount | Integer | 1 | The number of entries returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRouteTableList &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRouteTableListResponse>
  <TotalCount>1</TotalCount>
  <PageSize>10</PageSize>
  <Message>successful</Message>
  <RequestId>DC668356-BCB4-42FD-9BC3-FA2B2E04B634</RequestId>
  <PageNumber>1</PageNumber>
  <RouterTableList>
        <Status>Available</Status>
        <Description>This is Route Table.</Description>
        <RouteTableId>vtb-bp145q7glnuzdvzu2****</RouteTableId>
        <OwnerId>12345678</OwnerId>
        <ResourceGroupId>rg-acfmxazb4ph****</ResourceGroupId>
        <VpcId>vpc-bp15zckdt37pq72****</VpcId>
        <RouterType>VBR</RouterType>
        <CreationTime>2017-08-22T10:40:25Z</CreationTime>
        <RouterId>vrt-bp1lhl0taikrteen8****</RouterId>
        <RouteTableType>System</RouteTableType>
        <RouteTableName>doctest</RouteTableName>
        <Tags>
              <Value>ingress</Value>
              <Key>type</Key>
        </Tags>
        <VSwitchIds>vsw-bp12mw1f8k3jgygk9****</VSwitchIds>
  </RouterTableList>
  <Code>200</Code>
  <Success>true</Success>
</DescribeRouteTableListResponse>
```

`JSON` format `{`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "Message": "successful",
    "RequestId": "DC668356-BCB4-42FD-9BC3-FA2B2E04B634",
    "PageNumber": 1,
    "RouterTableList": {
        "Status": "Available",
        "Description": "This is Route Table.",
        "RouteTableId": "vtb-bp145q7glnuzdvzu2****",
        "OwnerId": 12345678,
        "ResourceGroupId": "rg-acfmxazb4ph****",
        "VpcId": "vpc-bp15zckdt37pq72****",
        "RouterType": "VBR",
        "CreationTime": "2017-08-22T10:40:25Z",
        "RouterId": "vrt-bp1lhl0taikrteen8****",
        "RouteTableType": "System",
        "RouteTableName": "doctest",
        "Tags": {
            "Value": "ingress",
            "Key": "type"
```

`},`

```json
        "VSwitchIds": "vsw-bp12mw1f8k3jgygk9****"
```

`},`

```json
    "Code": 200,
    "Success": true
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. Apply for the permissions and try again. |

#### UnassociateRouteTable

Disassociates a route table from a vSwitch. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociateRouteTa ble | The operation that you want to perform. Set the value to Unassociat eRout eT able. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the virtual private cloud (VPC) to which the route table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| RouteTableId | String | Yes | vtb- bp145q7glnuzdvzu2 **** | The ID of the route table. |
| VSwitchId | String | Yes | vsw- 25naucfvfbgte4**** | The ID of the vSwitch from which you want to disassociate the route table. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 62172DD5-6BAC-45DF- 8D44-62172DD5 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UnassociateRouteTable &RegionId=cn-qingdao-env17-d01 &RouteTableId=vtb-bp145q7glnuzdvzu2**** &VSwitchId=vsw-25naucfvfbgte4**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UnassociateRouteTableResponse>
      <RequestId>62172DD5-6BAC-45DF-8D44-62172DD5</RequestId>
</UnassociateRouteTableResponse>
```

`JSON` format `{`

```json
  "RequestId": "62172DD5-6BAC-45DF-8D44-62172DD5"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRouteTableId.Not Found | Specified route table does not exist. | The error message returned because the specified route table does not exist. |

### Region

#### DescribeRegions

Queries the most recent region list. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |
| ProductType | String | No | ECS | The type of the cloud service. |
| AcceptLanguage | String | No | zh-CN | The language of the response. Valid values: zh-CN: Chinese. This is the default value. en-US: English |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of Region |   | The list of regions. |
| Region |   |   |   |
| LocalName | String | China (Qingdao) | The name of the region. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RegionEndpoint | String | vpc.aliyuncs.com | The endpoint of the region. |
| RegionId | String | cn-qingdao-env17-d01 | The ID of the region. |
| RequestId | String | 611CB80C-B6A9-43DB- 9E38-0B0AC3D9B58F | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRegions &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRegionsResponse>
  <RequestId>611CB80C-B6A9-43DB-9E38-0B0AC3D9B58F</RequestId>
  <Regions>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <RegionEndpoint>vpc.aliyuncs.com</RegionEndpoint>
        <LocalName>China (Qingdao)</LocalName>
  </Regions>
</DescribeRegionsResponse>
```

`JSON` format `{`

```json
    "RequestId": "611CB80C-B6A9-43DB-9E38-0B0AC3D9B58F",
    "Regions": {
        "RegionId": "cn-qingdao-env17-d01",
        "RegionEndpoint": "vpc.aliyuncs.com",
        "LocalName": "China (Qingdao)"
```

#### DescribeZones

Queries zones in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeZones | The operation that you want to perform. Set the value to DescribeZones. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where zones are queried. You can call the DescribeRegions operation to the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Zones | Array of Zone |   | The zones that are returned. |
| Zone |   |   |   |
| LocalName | String | Hangzhou Zone | The name of the zone. |
| ZoneId | String | cn-cn-qingdao-env17- amtest11001-a | The ID of the zone. |
| RequestId | String | 6FEA0CF3-D3B9-43E5- A304-D217037876A8 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeZones &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeZonesResponse>
  <RequestId>6FEA0CF3-D3B9-43E5-A304-D217037876A8</RequestId>
  <Zones>
        <ZoneId>cn-cn-qingdao-env17-amtest11001-a</ZoneId>
        <LocalName>Hangzhou Zone B</LocalName>
  </Zones>
</DescribeZonesResponse>
```

`JSON` format `{`

```json
    "RequestId": "6FEA0CF3-D3B9-43E5-A304-D217037876A8",
    "Zones": {
        "ZoneId": "cn-cn-qingdao-env17-amtest11001-a",
        "LocalName": "Hangzhou Zone B"
```

### Tag

#### TagResources

Creates tags and adds the tags to resources at a time. Descriptions Tags are used to classify instances. Each tag consists of a key and a value. To use tags, make sure that the following requirements are met: The keys of tags that are added to the same instance must be unique. You cannot create tags without adding them to instances. All tags must be added to instances. Tag information is not shared across regions. Virtual private clouds (VPCs), route tables, vSwitches, and elastic IP addresses (EIPs) that belong to the same Apsara Stack tenant account and in the same region share tag information with each other. For example, if you have added a tag to a VPC, the tag is available to vSwitches, route tables, and EIPs that belong to the same account and in the same region where the VPC is created. You can select this tag from the editing page without the need to enter the tag again. You can modify the key and value of a tag or remove a tag from an instance. After you delete an instance, all tags that are added to the instance are deleted. You can add up to 20 tags to each instance. Before you add a tag to an instance, the system automatically checks the number of existing tags. An error message is returned if the maximum number of tags is reached. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TagResources | The operation that you want to perform. Set the value to T agResources. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the resource. |
| ResourceId.N | RepeatList | Yes | vpc- bp16qjewdsunr41m 1**** | The ID of the resource. Valid values of N: 1 to 20. |
| ResourceType | String | Yes | VPC | The type of the resource. Valid values: VPC: a virtual private cloud (VPC) VSWIT CH: a vSwitch ROUT ET ABLE: a route table EIP: an elastic IP address (EIP) |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tag.N.Key | String | No | FinanceDept | The key of the tag. Valid values of N: 1 to 20. The value of this parameter cannot be an empty string. The tag key cannot exceed 64 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). _ It must start with a letter but cannot start with aliyun or acs: . It cannot contain http:// or https:// . |
| Tag.N.Value | String | No | FinanceJoshua | The value of the tag that is attached to the resource. Valid values of N: 1 to 20. The value of this parameter cannot be an empty string. The tag value cannot exceed 128 characters in length, and must start with a letter. It can contain digits, periods (.), underscores ( ), and hyphens (-). It cannot _ start with aliyun or acs: . It cannot contain http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C46FF5A8-C5F0-4024- 8262-B16B639225A0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=TagResources &RegionId=cn-qingdao-env17-d01 &ResourceId.1=vpc-bp16qjewdsunr41m1**** &ResourceType=VPC &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TagResourcesResponse>
      <RequestId>C46FF5A8-C5F0-4024-8262-B16B639225A0</RequestId>
</TagResourcesResponse>
```

`JSON` format `{`

```json
 "RequestId":"C46FF5A8-C5F0-4024-8262-B16B639225A0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. Submit a ticket to obtain the required permissions. |

#### ListTagResources

Queries tags that are added to one or more instances. Descriptions Set ResourceId.N or T ag.N t hat consist s of T ag.N.Key and T ag.N.Value in the request to specify the object to be queried. T ag.N is a resource tag that consists of a key-value pair. If you set only T ag.N.Key, all tag values that are associated with the specified key are returned. If you set only T ag.N.Value, an error message is returned. If you set T ag.N and ResourceId.N to filter tags, ResourceId.N must match all specified key-value pairs. If you specify multiple key-value pairs, resources that contain these key-value pairs are returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListTagResources | The operation that you want to perform. Set the value to List T agResources. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the resource. |
| ResourceType | String | Yes | VPC | The type of the resource. Valid values: VPC: a virtual private cloud (VPC) VSWIT CH: a vSwitch ROUT ET ABLE: a route table EIP: an elastic IP address (EIP) |
| ResourceId.N | RepeatList | No | vpc- bp16qjewdsunr41m 1**** | The ID of the resource. Valid values of N: 1 to 20. |
| Tag.N.Key | String | No | FinanceDept | The key of the tag. Valid values of N: 1 to 20. The value of this parameter cannot be an empty string. The tag key cannot exceed 64 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). _ It must start with a letter but cannot start with aliyun or acs: . It cannot contain http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tag.N.Value | String | No | FinanceJoshua | The value of the tag. Valid values of N: 1 to 20. The value of this parameter cannot be an empty string. The tag value cannot exceed 128 characters in length, and must start with a letter. It can contain digits, periods (.), underscores ( ), and hyphens (-). It cannot _ start with aliyun or acs: . It cannot contain http:// or https:// . |
| NextToken | String | No | caeba0bbb2be03f8 4eb48b699f0a**** | The query token. Set this parameter to the value of the NextToken parameter that is returned in the last API call. If no subsequent queries are to be sent, you can leave the parameter empty. |
| MaxResults | Integer | No | 10 | The maximum number of entries to return. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NextToken | String | caeba0bbb2be03f84eb 48b699f0**** | The token that is required for the next query. If the Next T oken paramet er is empty, no subsequent request will be sent. |
| RequestId | String | DE65F6B7-7566-4802- 9007-96F2494AC512 | The ID of the request. |
| TagResources | Array of TagResource |   | The resources to which the tags are added. |
| TagResource |   |   |   |
| ResourcId | String | None | Ignore this parameter. |
| ResourceId | String | vpc- bp16qjewdsunr41m1*** * | The ID of the resource. |
| ResourceType | String | VPC | The type of the resource. |
| TagKey | String | FinanceDept | The tag key. |
| TagValue | String | FinanceJoshua | The tag value. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListTagResources &RegionId=cn-qingdao-env17-d01 &ResourceType=VPC &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListTagResourcesResponse>
  <NextToken>caeba0bbb2be03f84eb48b699f0****</NextToken>
  <RequestId>DE65F6B7-7566-4802-9007-96F2494AC512</RequestId>
  <TagResources>
        <ResourceId>2zebd226fxed6h4i****</ResourceId>
        <TagKey>FinanceDept</TagKey>
        <ResourceType>VPC</ResourceType>
        <ResourcId>vpc-bp16qjewdsunr41m1****</ResourcId>
        <TagValue>FinanceJoshua</TagValue>
  </TagResources>
</ListTagResourcesResponse>
```

`JSON` format `{`

```json
    "NextToken": "caeba0bbb2be03f84eb48b699f0****",
    "RequestId": "DE65F6B7-7566-4802-9007-96F2494AC512",
    "TagResources": {
        "ResourceId": "2zebd226fxed6h4i****",
        "TagKey": "FinanceDept",
        "ResourceType": "VPC",
        "ResourcId": "vpc-bp16qjewdsunr41m1****",
        "TagValue": "FinanceJoshua"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. Submit a ticket to obtain the required permissions. |

#### UnTagResources

Removes tags from specified resources. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnTagResources | The operation that you want to perform. Set the value to Unt agResources. |

| Virtual Private Cloud |   |   |   | Developer Guide·API reference |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region to which the resource belongs. |
| ResourceId.N | RepeatList | Supported | vpc- bp16qjewdsunr41m 1**** | The ID of the resource. Valid values of N: 1 to 20. |
| ResourceType | String | Yes | VPC | The type of the resource. Valid values: VPC: a virtual private cloud (VPC) VSWIT CH: a vSwitch ROUT ET ABLE: a route table EIP: an elastic IP address (EIP) |
| TagKey.N | RepeatList | No | FinanceDept | The key of the tag that you want to remove. Valid values of N: 1 to 20. The key can be an empty string. The key can be up to 64 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). _ It must start with a letter but cannot start with aliyun or acs: . It cannot contain http:// or https:// . |
| All | Boolean | No | false | Specifies whether to remove all tags from the resource. This parameter takes effect only when the T agKey.N parameter is not set in the request. Valid values: t rue: removes all tags from the resource. f alse(default): does not remove tags. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C46FF5A8-C5F0-4024- 8262-B16B639225A0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UnTagResources &RegionId=cn-qingdao-env17-d01 &ResourceId.1=vpc-bp16qjewdsunr41m1**** &ResourceType=VPC &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UntagResourcesResponse>
      <RequestId>C46FF5A8-C5F0-4024-8262-B16B639225A0</RequestId>
</UntagResourcesResponse>
```

`JSON` format `{`

```json
 "RequestId":"C46FF5A8-C5F0-4024-8262-B16B639225A0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. To obtain the required permissions, submit a ticket. |

### Physical connections

#### CreatePhysicalConnection

Applies for an Express Connect circuit. Descriptions After your application is approved, the Express Connect circuit changes to the Init ial state. You can contact the Internet service provider (ISP) to start construction. When you call this operation, take note of the following limits: If your Apsara Stack tenant account has more than five Express Connect circuits that are not in the Enabled state, you cannot apply for another Express Connect circuit. If your account has an Express Connect circuit with overdue payments, you cannot apply for another Express Connect circuit. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreatePhysicalConne ction | The operation that you want to perform. Set the value to Creat ePhysicalConnect ion. |
| AccessPointId | String | Yes | ap-cn-beijing-**** | The ID of the access point to which the Express Connect circuit belongs. |
| ClientToken | String | Yes | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LineOperator | String | Yes | CT | The ISP of the Express Connect circuit. Valid values: CT : China Telecom CU: China Unicom CM: China Mobile CO: other ISPs in mainland China Equinix: Equinix Ot her: other ISPs outside mainland China |
| PeerLocation | String | Yes | XX street | The geographical location of the data center. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
| Type | String | No | VPC | The type of the Express Connect circuit. Default value: VPC. |
| bandwidth | Integer | No | 10 | The bandwidth value of the bandwidth plan. Unit: Mbit/s. Valid values: 5 t o 5000. |
| PortType | String | No | 1000Base-T | The port type of the Express Connect circuit. Valid values: 100Base-T : a copper port that supports 100 Mbit/s of bandwidth 1000Base-T : a copper port that supports 1,000 Mbit/s of bandwidth 1000Base-LX: a single-mode fiber port that supports 1,000 Mbit/s of bandwidth (10 kilometers) 10GBase-T : a copper port that supports 10,000 Mbit/s of bandwidth 10GBase-LR: a single-mode fiber port that supports 10,000 Mbit/s of bandwidth (10 kilometers) |
| RedundantPhysicalC onnectionId | String | No | pc-119mfjzm7****** | The ID of the standby Express Connect circuit. The standby Express Connect circuit must be in the Allocat ed, Conf irmed, or Enabled state. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | Description | The description of the Express Connect circuit. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . |
| Name | String | No | test | The name of the Express Connect circuit. The name must be 2 to 128 characters in length and can contain digits, underscores ( ), and hyphens (-). It must start with a _ letter, but cannot start with http:// or https:// . |
| CircuitCode | String | No | longtel001 | The circuit code provided by the Internet service provider (ISP) of the Express Connect circuit. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PhysicalConnectio nId | String | pc-bp12mw****** | The ID of the Express Connect circuit. |
| RequestId | String | 8A6A5EC5-6F6C-4906- 9689-56ACE58A13E0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreatePhysicalConnection &AccessPointId=ap-cn-beijing-**** &ClientToken=123e4567-e89b-12d3-a456-426655440000 &LineOperator=CT &PeerLocation=XX street &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreatePhysicalConnectionResponse>
      <RequestId>8A6A5EC5-6F6C-4906-9689-56ACE58A13E0</RequestId>
      <PhysicalConnectionId>pc-bp12mw******</PhysicalConnectionId>
</CreatePhysicalConnectionResponse>
```

`JSON` format `{`

```json
    "CreatePhysicalConnectionResponse": {
        "RequestId": "8A6A5EC5-6F6C-4906-9689-56ACE58A13E0",
        "PhysicalConnectionId": "pc-bp12mw******"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidAccessPointId.No tEnabled | Invalid access point status. | The error message returned because the access point is unavailable. |
| 400 | InvalidType.Malformd | The Type provided was invalid. | The error message returned because Type is set to an invalid value. |
| 400 | InvalidPeerLocation.Mal formd | The PeerLocation provided was invalid. | The error message returned because PeerLocation is set to an invalid value. |
| 400 | InvalidLineOperator.Mal formd | The LineOperator provided was invalid. | The error message returned because LineOperator is set to an invalid value. |
| 400 | InvalidPortType.Malfor md | The PortType provided was invalid. | The error message returned because the specified port type is invalid. |
| 400 | InvalidDescription.Malfo rmed | The specifid ?Description? is not valid. | The error message returned because the format of the resource description is invalid. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| 400 | InvalidRedundantPhysic alConnectionId.NotFoun d | The RedundantPhysicalConnectionId does not found. | The error message returned because the specified standby Express Connect circuit does not exist. |
| 400 | InvalidName.Malformed | The specified ?Name? is not valid. | The error message returned because the format of the name is invalid. |
| 400 | QuotaExceeded.pConnP erAP | Physical connection count per ap quota exceed. | The error message returned because the number of Express Connect circuits that are associated with the specified access point has reached the upper limit. |
| 400 | InvalidBandwidth | invalid physical connection banwidth. | The error message returned because the specified bandwidth value of the Express Connect circuit is invalid. |
| 400 | InvalidRedundantPhysic alConnection | redundant physical connection doesn't belong to current user. | The error message returned because the specified standby Express Connect circuit does not belong to your Apsara Stack tenant account. |
| 400 | InvalidRedundantPhysic alConnectionStatus | invalid redundant physical connection status. | The error message returned because the standby Express Connect circuit is in an invalid state. |

|   | Developer Guid | e·API reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidCircuitCode.Malfo rmed | circuitCode is illegal. | The error message returned because CircuitCode is set to an invalid value. |
| 400 | QuotaExceeded.freePco nnPerAP | free physical connections count excceeded. | The error message returned because the quota on Express Connect circuits is reached. |

#### DescribeAccessPoints

Queries the access points of Express Connect circuits in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccessPoint s | The operation that you want to perform. Set the value to DescribeAccessPoint s. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the access point. You can call the DescribeRegions operation to query the most recent region list. |
| Filter.N.Key | String | No | name | Specifies filter conditions. You can specify at most five filter conditions. |
| Filter.N.Value.N | RepeatList | No | test | Specifies filter values based on keys. You can specify multiple filter values for one key. The logical operator between filter values is OR. If one filter value is matched, the filter condition is matched. |
| Type | String | No | VPC | The network type of the Express Connect circuit. Default value: VPC. |
| Name | String | No | Hangzhou-Yuhang-C | The name of the access point. |
| HostOperator | String | No | China Telecom | The Internet service provider (ISP) of the access point. Valid values: China Mobile China Unicom China T elecom Ot her ISPs in China ISPs out side China |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessPointSet | Array of AccessPointType |   | The information about the access points. |
| AccessPointType |   |   |   |
| AccessPointId | String | ap-cn-hangzhou-**** | The ID of the access point. |
| AttachedRegionN o | String | cn-qingdao-env66-d01 | The region ID of the access point. |
| Description | String | Access point description | The description of the access point. |
| HostOperator | String | China Telecom | The Internet service provider (ISP) of the access point. Valid values: China Mobile China Unicom China T elecom Ot her ISPs in China ISPs out side China |
| Location | String | Qingdao | The geographical location of the access point. |
| Name | String | Qingdao-Laoshan-A | The name of the access point. |
| Status | String | recommended | The status of the access point. Valid values: recommended: The access point is ready for use. hot : A large number of Express Connect circuits are connected to the access point. f ull: The number of Express Connect circuits connected to the access point has reached the upper limit. disabled: The access point is unavailable. |
| Type | String | VPC | The network type of the Express Connect circuit. |
| TotalCount | Integer | 5 | The number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. Default value: 1. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageSize | Integer | 10 | The number of entries returned on each page. Maximum value: 50. Default value: 10. |
| RequestId | String | 3E85D803-C7CF-4BCD- 9CFE-6DBA1DFFA027 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAccessPoints &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAccessPointsResponse>
      <AccessPointSet>
            <Status>recommended</Status>
            <Type>VPC</Type>
            <Description>ap-cn-hangzhou-dq-A-EU95</Description>
            <AttachedRegionNo>cn-qingdao-env66-d01</AttachedRegionNo>
            <HostOperator>China Telecom</HostOperator>
            <AccessPointId>ap-cn-hangzhou-xs-D</AccessPointId>
            <Name>Qingdao-Laoshan-A</Name>
            <Location>Qingdao</Location>
      </AccessPointSet>
      <TotalCount>5</TotalCount>
      <PageSize>10</PageSize>
      <RequestId>3E85D803-C7CF-4BCD-9CFE-6DBA1DFFA027</RequestId>
      <PageNumber>1</PageNumber>
</DescribeAccessPointsResponse>
```

`JSON` format `{`

```json
    "DescribeAccessPointsResponse": {
        "AccessPointSet": {
            "Status": "recommended",
            "Type": "VPC",
            "Description": "ap-cn-hangzhou-dq-A-EU95",
            "AttachedRegionNo": "cn-qingdao-env66-d01",
            "HostOperator": "China Telecom",
            "AccessPointId": "ap-cn-hangzhou-xs-D",
            "Name": "Qingdao-Laoshan-A",
            "Location": "Qingdao"
```

`},`

```json
        "TotalCount": 5,
        "PageSize": 10,
        "RequestId": "3E85D803-C7CF-4BCD-9CFE-6DBA1DFFA027",
        "PageNumber": 1
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotSup port | The RegionId provided does not support in our records. | The error message returned because the specified region ID is invalid. |

#### CancelPhysicalConnection

Cancels an Express Connect circuit before it is enabled. After you cancel an Express Connect circuit, it changes to the Canceled state. Limits You can cancel only an Express Connect circuit that is in the Init ial, Approved, Allocat ed, or Conf irmed state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CancelPhysicalConne ction | The operation that you want to perform. Set the value to CancelPhysicalConnect ion. |
| PhysicalConnectionId | String | Yes | pc-119mf**** | The ID of the Express Connect circuit. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CancelPhysicalConnection &PhysicalConnectionId=pc-119mf**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CancelPhysicalConnectionResponse>
      <RequestId>BE36E95A-F83E-4127-A29E-F2F35D4C999A</RequestId>
</CancelPhysicalConnectionResponse>
```

`JSON` format `{`

```json
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConnectio nId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the specified Express Connect circuit does not exist. |
| 400 | Forbidden.NotAllowedI nState | The request does not allow in this state. | The error message returned because the operation cannot be performed when the Express Connect circuit in the current state. |

#### DescribePhysicalConnections

Queries Express Connect circuits in a region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePhysicalCon nections | The operation that you want to perform. Set the value to DescribePhysicalConnect ions . |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
| PageNumber | Integer | No | 10 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 1 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Filter.N.Key | String | No | 1 | The filter condition. Valid values of N are 1 t o 5. The following filter conditions are supported: PhysicalConnect ionId: the ID of the Express Connect circuit AccessPoint Id: the ID of the access point T ype: the type of the Express Connect circuit LineOperat or: the Internet service provider (ISP) of the Express Connect circuit Spec: the specification of the Express Connect circuit St at us: the status of the Express Connect circuit Name: the name of the Express Connect circuit The logical relation between values in a filter condition is OR, which means that the filter condition is met if one of the values is met. The logical relation between filter conditions is AND. In this case, the result is returned only when all conditions are met. |
| Filter.N.Value.N | RepeatList | No | 1 | The value of the filter condition. Valid values of N are 1 t o 5. |
| IncludeReservationD ata | Boolean | No | false | Specifies whether to return the orders that have not taken effect. t rue: yes f alse (default): no |
| ClientToken | String | No | 23243242rggy**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PhysicalConnectio nSet | Array of PhysicalConnectio nType |   | The details about the Express Connect circuits. |
| PhysicalConnectio nType |   |   |   |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessPointId | String | eip- 2zeerraiwb7uj6i0******* | The ID of the access point. |
| AdLocation | String | Ax-x Bxx, Building xx, xxx Base, Binhai Boulevard, Nanshan District, Shenzhen, Guangdong | The geographical location of the access device. |
| Bandwidth | Long | 10 | The bandwidth of the Express Connect circuit. Unit: Mbit/s. |
| BusinessStatus | String | Normal | The payment status of the Express Connect circuit. Valid values: Normal: normal FinancialLocked: locked due to overdue payments Securit yLocked: locked for security reasons |
| ChargeType | String | Prepaid | The billing method. The value is set to Prepaid, which indicates the subscription billing method. |
| CircuitCode | String | longtel001 | The circuit code provided by the ISP for the Express Connect circuit. |
| CreationTime | String | 2017-06-08T12:20:55 | The time when the Express Connect circuit was created. |
| Description | String | The Express Connect circuit | The description of the Express Connect circuit. |
| EnabledTime | String | 2017-06-08T12:20:55 | The time when the Express Connect circuit was enabled. |
| EndTime | String | 2019-02-25T11:01:04Z | The time when the Express Connect circuit expires. |
| HasReservationDa ta | String | true | Indicates whether you have subscription messages. t rue: yes f alse: no |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LineOperator | String | CT | The ISP of the Express Connect circuit. Valid values: CT : China Telecom CU: China Unicom CM: China Mobile CO: other ISPs in China Equinix: Equinix Ot her: other ISPs outside China |
| LoaStatus | String | Available | The status of the letter of authorization (LOA). |
| Name | String | name | The name of the Express Connect circuit. |
| PeerLocation | String | Building XX, XX Avenue, XX District, Hangzhou, Zhejiang | The geographical location of the data center. |
| PhysicalConnectio nId | String | pc-119mfjzm***** | The ID of the Express Connect circuit. |
| PortNumber | String | 80 | The port number of the access device. |
| PortType | String | 1000Base-T | The port type of the Express Connect circuit. Valid values: 100Base-T : a copper port that supports 100 Mbit/s of bandwidth 1000Base-T : a copper port that supports 1,000 Mbit/s of bandwidth 1000Base-LX: a single-mode fiber port that supports 1,000 Mbit/s of bandwidth (10 kilometers) 10GBase-T : a copper port that supports 10,000 Mbit/s of bandwidth 10GBase-LR: a single-mode fiber port that supports 10,000 Mbit/s of bandwidth (10 kilometers) |
| RedundantPhysica lConnectionId | String | pc-119mfjzm******* | The ID of the standby Express Connect circuit. |
| ReservationActive Time | String | 2019-02-25T11:01:04Z | The time when the renewal takes effect. |
| ReservationInterne tChargeType | String | PayByBandwidth | The renewal type. |
| ReservationOrderT ype | String | RENEW | The type of the renewal order. |
| Spec | String | Large | The specification of the Express Connect circuit. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | Initial | The status of the Express Connect circuit. Valid values: Init ial: pending approval Approved: approved Allocat ing: allocating resources Allocat ed: under construction Conf irmed: waiting for user confirmation Enabled: enabled Reject ed: rejected Canceled: canceled Allocat ion Failed: resource allocation failed T erminat ed: disabled |
| Type | String | VPC | The type of the Express Connect circuit. Default value: VPC. |
| TotalCount | Integer | 10 | The total number of entries returned. |
| PageNumber | Integer | 10 | The number of the page returned. Default value: 1. |
| PageSize | Integer | 10 | The number of entries returned on each page. Maximum value: 50. Default value: 10. |
| RequestId | String | EEC8EAB1-F299-4F5C- 8E54-0A3129164C27 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribePhysicalConnections &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePhysicalConnectionsResponse>
      <PhysicalConnectionSet>
            <Status>Initial</Status>
            <Description>Express Connect circuit</Description>
            <EndTime>2019-02-25T11:01:04Z</EndTime>
            <LineOperator>CT</LineOperator>
            <CircuitCode>longtel001</CircuitCode>
            <PhysicalConnectionId>pc-119mfjzm*****</PhysicalConnectionId>
            <HasReservationData>true</HasReservationData>
            <RedundantPhysicalConnectionId>pc-119mfjzm*******</RedundantPhysicalConnectionId>
            <PeerLocation>Building XX, XX Avenue, XX District, Hangzhou, Zhejiang</PeerLocation>
            <BusinessStatus>Normal</BusinessStatus>
            <ReservationInternetChargeType>PayByBandwidth</ReservationInternetChargeType>
            <Name>name</Name>
            <ReservationOrderType>RENEW</ReservationOrderType>
            <LoaStatus>Available</LoaStatus>
            <Type>VPC</Type>
            <AdLocation>Ax-x Bxx, Building xx, xxx Base, Binhai Boulevard, Nanshan District, Shenzhen, G
uangdong</AdLocation>
            <ChargeType>Prepaid</ChargeType>
            <Bandwidth>10</Bandwidth>
            <CreationTime>2017-06-08T12:20:55</CreationTime>
            <AccessPointId>eip-2zeerraiwb7uj6i0*******</AccessPointId>
            <EnabledTime>2017-06-08T12:20:55</EnabledTime>
            <ReservationActiveTime>2019-02-25T11:01:04Z</ReservationActiveTime>
            <PortNumber>80</PortNumber>
            <Spec>Large</Spec>
            <PortType>1000Base-T</PortType>
      </PhysicalConnectionSet>
      <TotalCount>10</TotalCount>
      <PageSize>10</PageSize>
      <RequestId>EEC8EAB1-F299-4F5C-8E54-0A3129164C27</RequestId>
      <PageNumber>10</PageNumber>
</DescribePhysicalConnectionsResponse>
```

`JSON` format `{`

```json
    "PhysicalConnectionSet": {
        "Status": "Initial",
        "Description": "Express Connect circuit",
        "EndTime": "2019-02-25T11:01:04Z",
        "LineOperator": "CT",
        "CircuitCode": "longtel001",
        "PhysicalConnectionId": "pc-119mfjzm*****",
        "HasReservationData": true,
        "RedundantPhysicalConnectionId": "pc-119mfjzm*******",
        "PeerLocation": "Building XX, XX Avenue, XX District, Hangzhou, Zhejiang",
        "BusinessStatus": "Normal",
        "ReservationInternetChargeType": "PayByBandwidth",
        "Name": "name",
        "ReservationOrderType": "RENEW",
        "LoaStatus": "Available",
        "Type": "VPC",
        "AdLocation": "Ax-x Bxx, Building xx, xxx Base, Binhai Boulevard, Nanshan District, Shenzhen, Gu
angdong",
        "ChargeType": "Prepaid",
        "Bandwidth": 10,
        "CreationTime": "2017-06-08T12:20:55",
        "AccessPointId": "eip-2zeerraiwb7uj6i0*******",
        "EnabledTime": "2017-06-08T12:20:55",
        "ReservationActiveTime": "2019-02-25T11:01:04Z",
        "PortNumber": 80,
        "Spec": "Large",
        "PortType": "1000Base-T"
```

`},`

```json
    "TotalCount": 10,
    "PageSize": 10,
    "RequestId": "EEC8EAB1-F299-4F5C-8E54-0A3129164C27",
    "PageNumber": 10
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidFilterKey.ValueNo tSupported | Specified filter key is not supported: Filter.X.key | The error message returned because Filter.X.key is not supported. |

#### ModifyPhysicalConnectionAttribute

Modifies the configuration of a physical connection. When you call this operation, take note of the following limits: You can only modify the configuration of a physical connection that is in the Init ial, Enabled, or Reject ed state. You cannot modify the configurations of a physical connection that is in the Canceled, Allocat ing, Allocat ionFailed, or T erminat ed state. After you modify the configurations of a physical connection that is in the Reject ed state, its state becomes Init ial. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyPhysicalConn ectionAttribute | The operation that you want to perform. Set the value to Modif yPhysicalConnect ionAt t ribut e. |
| PhysicalConnectionId | String | Yes | pc-119mfjzm****** | The ID of the physical connection. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the physical connection is deployed. You can call the DescribeRegions operation to query region IDs. |
| LineOperator | String | No | CT | The Internet service provider (ISP). Valid values: CT: China Telecom CU: China Unicom CM: China Mobile CO: other ISPs in China Equinix: Equinix Other: other ISPs outside China |
| bandwidth | Integer | No | 5 | The bandwidth of the physical connection. Unit: Mbit/s. Valid values: 2 to 10240. |
| PeerLocation | String | No | Building XX, XX Avenue, XX District, Hangzhou, Zhejiang | The geographical location of the data center. |
| PortType | String | No | 1000Base-LX | The port type of the physical connection. Default value: 1000Base-T. Valid values: 100Base-T: a copper port that supports 100 Mbit/s. 1000Base-T: a copper port that supports 1,000 Mbit/s. 1000Base-LX: a single-mode fiber port that supports 1,000 Mbit/s (10 kilometers). 10GBase-T: a copper port that supports 10,000 Mbit/s. 10GBase-LR: a single-mode fiber port that supports 10,000 Mbit/s (10 kilometers). |
| RedundantPhysicalC onnectionId | String | No | pc-119mfjzm7 | The ID of the standby physical connection. The standby physical connection must be in the Allocat ed, Conf irmed, or Enabled state. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | The description of the physical connection | The description of the physical connection. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . |
| Name | String | No | The name of the physical connection | The name of the physical connection. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). The name _ cannot start with http:// or https:// . |
| ClientToken | String | No | efefe566754h | The client token that is used to guarantee the idempotency of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| CircuitCode | String | No | longtel001 | The circuit code provided by the ISP for the physical connection. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 013EE132-A109-4247- 91B0-099A8FF49AD7 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=ModifyPhysicalConnectionAttribute &PhysicalConnectionId=pc-119mfjzm****** &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyPhysicalConnectionAttributeResponse>
      <RequestId>8A6A5EC5-6F6C-4906-9689-56ACE58A13E0</RequestId>
</ModifyPhysicalConnectionAttributeResponse>
```

`JSON` format `{`

```json
  "RequestId": "8A6A5EC5-6F6C-4906-9689-56ACE58A13E0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConnectio nId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the physical connection does not exist. |
| 400 | InvalidLineOperator.Mal formd | The LineOperator provided was invalid. | The error message returned because the value of the LineOperator parameter is invalid. |
| 400 | InvalidPeerLocation.Mal formd | The PeerLocation provided was invalid. | The error message returned because the value of the PeerLocation parameter is invalid. |
| 400 | InvalidPortType.Malfor md | The PortType provided was invalid. | The error message returned because the type of the port is invalid. |
| 400 | InvalidDescription.Malfo rmed | The specifid ? Description? is not valid. | The error message returned because the format of the resource description is invalid. The value must be 2 to 256 characters in length and cannot start with http:// or https://. |
| 400 | InvalidName.Malformed | The specified ? Name? is not valid. | The error message returned because the format of the name is invalid. |
| 400 | InvalidStatus | invalid physical connection status. | The error message returned because the state of the specified physical connection is invalid. |
| 400 | InvalidBandwidth | invalid physical connection banwidth. | The error message returned because the maximum bandwidth of the physical connection is invalid. |
| 400 | InvalidRedundantPhysic alConnection | redundant physical connection doesn't belong to current user. | The error message returned because the backup connection does not belong to your Apsara Stack tenant account. |
| 400 | InvalidRedundantPhysic alConnectionStatus | invalid redundant physical connection status. | The error message returned because the state of the backup physical connection is invalid. |
| 400 | InvalidCircuitCode.Malfo rmed | circuitCode is illegal. | The error message returned because the value of the CircuitCode parameter is invalid. |

#### TerminatePhysicalConnection

Disables an Express Connect circuit after it is enabled. Descriptions After you call this operation, the specified Express Connect circuit changes to the T erminat ing state. After the Express Connect circuit is disabled, it changes to the T erminat ed state. When you call this operation, take note of the following limits: You can only terminate an Express Connect circuit that is in the Enabled state. Before you disable an Express Connect circuit, you must delete the virtual border routers (VBRs) associated with it. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TerminatePhysicalCo nnection | The operation that you want to perform. Set the value to T erminat ePhysicalConnect ion. |
| PhysicalConnectionId | String | Yes | pc-119mfjzm**** | The ID of the Express Connect circuit. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 513E0A50-4F2D-4CBE- BF35-40559DF65D79 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=TerminatePhysicalConnection &PhysicalConnectionId=pc-119mfjzm**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TerminatePhysicalConnectionResponse>
      <RequestId>513E0A50-4F2D-4CBE-BF35-40559DF65D79</RequestId>
</TerminatePhysicalConnectionResponse>
```

`JSON` format `{`

```json
    "TerminatePhysicalConnectionResponse": {
        "RequestId": "513E0A50-4F2D-4CBE-BF35-40559DF65D79"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConnectio nId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the specified Express Connect circuit does not exist. |
| 400 | Forbidden.NotAllowedI nState | The request does not allow in this state. | The error message returned because the operation cannot be performed when the Express Connect circuit in the current state. |

#### EnablePhysicalConnection

Enables an Express Connect circuit that is in the Conf irmed state. After you enable an Express Connect circuit, it changes to the Enabled state. Descriptions When you call this operation, take note of the following limits: You can enable only an Express Connect circuit that is in the Conf irmed state. After you enable an Express Connect circuit, it changes to the Enabled state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EnablePhysicalConne ction | The operation that you want to perform. Set the value to EnablePhysicalConnect ion. |
| PhysicalConnectionId | String | Yes | pc-119mfjz**** | The ID of the Express Connect circuit. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=EnablePhysicalConnection &PhysicalConnectionId=pc-119mfjz**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<EnablePhysicalConnectionResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</EnablePhysicalConnectionResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConnectio nId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the Express Connect circuit does not exist. |
| 400 | Forbidden.NotAllowedI nState | The request does not allow in this state. | The error message returned because the operation cannot be performed when the Express Connect circuit in the current state. |

#### DeletePhysicalConnection

Deletes an Express Connect circuit. Limits You can only delete an Express Connect circuit that is in the Reject ed, Canceled, Allocat ionFailed, or T erminat ed state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeletePhysicalConne ction | The operation that you want to perform. Set the value to Delet ePhysicalConnect ion. |
| PhysicalConnectionId | String | Yes | pc-119mfjzm7**** | The ID of the Express Connect circuit. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeletePhysicalConnection &PhysicalConnectionId=pc-119mfjzm7**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeletePhysicalConnectionResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeletePhysicalConnectionResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConnectio nId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the Express Connect circuit does not exist. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Forbidden.NotAllowedI nState | The request does not allow in this state. | The error message returned because the operation cannot be performed when the Express Connect circuit in the current state . |
| 400 | InvalidPhysicalConnectio nId.NotMatched | instance id not matched. | The error message returned because the instance ID does not match. |
| 400 | Forbidden.VBRExists | physical connection owner's vbr still exists. | The error message returned because the virtual border router (VBR) of the Express Connect circuit still exists. |
| 400 | Forbidden.VBRExists | vbr owner's vbr still exists. | The error message returned because the VBR still exists. |
| 400 | Forbidden.AssociateTo VBR | The physical connection still associate to VBR. | The error message returned because the Express Connect circuit is already associated with a VBR. |

#### CreatePhysicalConnectionOccupancyOrder

Creates an order for resource occupation of one or more physical connections. Not e You can perform this operation only for a physical connection that is in the Complet e state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreatePhysicalConne ctionOccupancyOrde r | The operation that you want to perform. Set the value to Creat ePhysicalConnect ionOccupancyOrd er. |
| PhysicalConnectionId | String | Yes | pc- bp1hp0wr072f6***** * | The ID of the physical connection. |
| RegionId | String | Yes | cn-hangzhou | The region where the physical connection is deployed. |
| Period | Integer | No | 1 | The subscription duration. |
| InstanceChargeType | String | No | PostPaid | The billing method of the physical connection. Valid values: PrePaid: subscription. If you select this billing method, make sure that your Apsara Stack tenant account supports balance payment or credit payment. Post Paid: pay-as-you-go. This is the default value. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AutoPay | Boolean | No | true | Specifies whether automatic payment is enabled. Valid values: t rue: enables automatic payment. This is the default value. Make sure that you have sufficient balance in your account. Otherwise, your order becomes invalid and must be canceled. f alse: An order is generated but no payment is made. |
| PricingCycle | String | No | Month | The unit of the subscription cycle. Year: by year. Mont h: by month. |
| ClientToken | String | No | CBCE910E-D396- 4944-8764- B4047838B2D1 | The client token that is used for authentication. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B9300FE-11E2-4E3B- 949C-BED3B44DD26D | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CreatePhysicalConnectionOccupancyOrder &PhysicalConnectionId=pc-bp1hp0wr072f6****** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreatePhysicalConnectionOccupancyOrder>
    <RequestId>9B9300FE-11E2-4E3B-949C-BED3B44DD26D</RequestId>
</CreatePhysicalConnectionOccupancyOrder>
```

`JSON` format `{`

```json
 "RequestId": "9B9300FE-11E2-4E3B-949C-BED3B44DD26D"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConnectio nId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the physical connection does not exist. |
| 400 | Forbidden.NotAllowedI nState | The request does not allow in this state. | The error message returned because the state is invalid. |

#### ApplyPhysicalConnectionLOA

Requests a letter of authorization (LOA) for a physical connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ApplyPhysicalConne ctionLOA | The operation that you want to perform. Set the value toApplyPhysicalConnect ionLOA. |
| CompanyName | String | Yes | company | The name of the customer company that requires the physical connection. |
| ConstructionTime | String | Yes | 2019-02- 28T16:00:00.000Z | The time when construction started. |
| InstanceId | String | Yes | pc- bp1qrb3044eqixxxxx xxx | The ID of the physical connection. |
| LineType | String | Yes | SDH | The type of the physical connection. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the physical connection is deployed. |
| Si | String | Yes | Alibaba | The construction company. |
| ClientToken | String | No | A47BD386-7FDE- 4xxx4-8D22- C62xxxxxxxx | Client authentication. |
| Bandwidth | Integer | No | 3 | The bandwidth of the physical connection. |
| PeerLocation | String | No | Hangzhou | The geographical location where the physical connection is deployed. |
| PMInfo.N.PMName | String | No | Tom | The name of the construction personnel. N is a natural number. Replace N with a value when you call this operation. |

| Virtual Private Cloud |   |   |   | Developer Guide·API reference |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PMInfo.N.PMContactI nfo | String | No | 1320000**** | The contact information about the construction personnel. N is a natural number. Replace N with a value when you call this operation. |
| PMInfo.N.PMCertifica teType | String | No | IDCard | The identity type of the construction personnel. N is a natural number. Replace N with a value when you call this operation. |
| PMInfo.N.PMCertifica teNo | String | No | 3210xxxxxxxxxxxxxx | The identity number of the construction personnel. N is a natural number. Replace N with a value when you call this operation. |
| PMInfo.N.PMGender | String | No | Male | The gender of the construction personnel. N is a natural number. Replace N with a value when you call this operation. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A47BD386-7FDE-42C4- 8D22-C6223D18AA1C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=ApplyPhysicalConnectionLOA &CompanyName=company &ConstructionTime=2019-02-28T16:00:00.000Z &InstanceId=pc-bp1qrb3044eqixxxxxxxx &LineType=SDH &RegionId=cn-hangzhou &Si=Alibaba &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ApplyPhysicalConnectionLOAResponse>
      <RequestId>A47BD386-7FDE-42C4-8D22-C6223D18AA1C</RequestId>
    </ApplyPhysicalConnectionLOAResponse>
```

`JSON` format `{`

```json
    "RequestId":"A47BD386-7FDE-42C4-8D22-C6223D18AA1C"
```

#### CreatePhysicalConnectionSetupOrder

Creates an order for initial installation of a physical connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreatePhysicalConne ctionSetupOrder | The operation that you want to perform. Set the value toCreat ePhysicalConnect ionSet upOrder. |
| AccessPointId | String | Yes | ap-cn-beijing-ft-A | The ID of the access point. |
| LineOperator | String | Yes | CT | The Internet service provider (ISP). Valid values: CT: China Telecom. CU: China Unicom. CM: China Mobile. CO: other ISPs in China. Equinix: Equinix. Other: other ISPs outside China. |
| RegionId | String | Yes | cn-shanghai | The region where the physical connection is deployed. |
| PortType | String | No | 100Base-T | The port type of the physical connection. Default value: 1000Base-T. Valid values: 100Base-T : a copper port that supports 100 Mbit/s. 1000Base-T : a copper port that supports 1,000 Mbit/s. 1000Base-LX: a single-mode fiber port that supports 1,000 Mbit/s (10 kilometers). 10GBase-T : a copper port that supports 10,000 Mbit/s. 10GBase-LR: a single-mode fiber port that supports 10,000 Mbit/s (10 kilometers). |
| RedundantPhysicalC onnectionId | String | No | pc- bp10zsv5ntp******** | The ID of the standby physical connection. The standby physical connection must be in the Allocat ed, Conf irmed, or Enabled state. |
| AutoPay | Boolean | No | true | Indicates whether automatic payment is enabled. Valid values:t rueandf alse. |

| Virtual Private Cloud |   |   |   | Developer Guide·API reference |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 318BB676-0A2B- 43A0-9AD8- F1D34E93750F | The client token that is used for authentication. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 202844382740728 | The ID of the order. |
| PhysicalConnectio nId | String | pc- 2zegmc02v7ss4****** | The ID of the physical connection. |
| RequestId | String | F7A6301A-64BA-41EC- 8284-8F4838C15D1F | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CreatePhysicalConnectionSetupOrder &AccessPointId=ap-cn-beijing-ft-A &LineOperator=CT &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreatePhysicalConnectionSetupOrderResponse>
     <OrderId>205226815210296</OrderId>
     <RequestId>76CCB7F1-C141-4BD1-8106-63987D12BEF4</RequestId>
     <PhysicalConnectionId>pc-2zegmc02v7ss4pin******</PhysicalConnectionId>
</CreatePhysicalConnectionSetupOrderResponse>
```

`JSON` format `{`

```json
    "OrderId": 205226815210296,
    "RequestId": "76CCB7F1-C141-4BD1-8106-63987D12BEF4",
    "PhysicalConnectionId": "pc-2zegmc02v7ss4******"
```

#### CompletePhysicalConnectionLOA

Generates a report for an installed physical connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CompletePhysicalCo nnectionLOA | The operation that you want to perform. Set the value to Complet ePhysicalConnect ionLOA. |
| InstanceId | String | Yes | pc- bp10tvlhnwkwxxxxx xxxxx | The ID of the physical connection. |
| LineCode | String | Yes | aaa111 | The circuit code provided by the Internet service provider (ISP). |
| LineLabel | String | Yes | bbb222 | The label of the cable in the data center. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the physical connection is deployed. |
| ClientToken | String | No | F8983C74-E068- 4509-B442- 89xxxxxC8F43B | The client token that is used for authentication. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F8983C74-E068-4509- B442-89BD82C8F43B | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CompletePhysicalConnectionLOA &InstanceId=pc-bp10tvlhnwkwxxxxxxxxxx &LineCode=aaa111 &LineLabel=bbb222 &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CompletePhysicalConnectionLOAResponse>
      <code>200</code>
   <message>successful</message>
   <requestId>5FA3B04E-AEA0-4F89-BF0D-3FD71ED69BF7</requestId>
   <success>true</success>
    </CompletePhysicalConnectionLOAResponse>
```

`JSON` format `{`

```json
    "code":"200",
    "message":"successful",
    "requestId":"5FA3B04E-AEA0-4F89-BF0D-3FD71ED69BF7",
    "success":true
```

#### DescribePhysicalConnectionLOA

Queries letter of authorization (LOA) information about an Express Connect circuit. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePhysicalCon nectionLOA | The operation that you want to perform. Set the value to DescribePhysicalConnect ionLOA. |
| InstanceId | String | Yes | pc- bp1ca4wca27ex***** * | The ID of the Express Connect circuit. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 318BB676-0A2B- 43A0-9AD8- F1D34E93750F | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PhysicalConnectio nLOAType | Struct |   | The LOA information about the Express Connect circuit. |
| CompanyLocalize dName | String | company | The name of the construction company. |
| CompanyName | String | AppCompany**** | The name of the organization that requires the Express Connect circuit. |
| ConstructionTime | String | 2019-02-26T08:00:00Z | The time when construction starts. |
| InstanceId | String | pc-bp1ca4wca27****** | The ID of the Express Connect circuit. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| LineCode | String | lincode**** | The circuit code provided by the Internet service provider (ISP). |
| LineLabel | String | linetest**** | The label of the cable in the data center. |
| LineType | String | MSTP | The type of the Express Connect circuit. Valid values: MST P Ot her SDH MPLSVPN FIBRE |
| LoaUrl | String | http://****** | The download URL of the LOA file. |
| PMInfo | Array of PMInfo |   | The information about the construction workers. |
| PMInfo |   |   |   |
| PMCertificateNo | String | engineer**** | The identity document number of the construction worker. |
| PMCertificateType | String | Other | The type of the identity document. Valid values: IDCard: identity card Ot her: other identity documents Passport : passport |
| PMContactInfo | String | 18910010****** | The phone number of the construction worker. |
| PMGender | String | Male | The gender of the construction worker. |
| PMName | String | name | The name of the construction worker. |
| SI | String | ctcu | The on-site construction company. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | Enabled | The status of the Express Connect circuit. Valid values: Init ial: pending approval Approved: approved Allocat ing: allocating resources Allocat ed: under construction Conf irmed: waiting for user confirmation Enabled: enabled Reject ed: rejected Canceled: canceled Allocat ion Failed: resource allocation failed T erminat ed: disabled |
| RequestId | String | 318BB676-0A2B-43A0- 9AD8-F1D34E93750F | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribePhysicalConnectionLOA &InstanceId=pc-bp1ca4wca27ex****** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePhysicalConnectionLOAResponse>
   <code>200</code>
   <data>
      <companyName>test1234</companyName>
      <constructionTime>2019-02-26T08:00:00Z</constructionTime>
      <instanceId>pc-bp1ca4wca27ert****</instanceId>
      <lineType>MSTP</lineType>
      <loaUrl>http://********</loaUrl>
      <pmInfo>
         <nextPMIndex>1</nextPMIndex>
         <pmCertificateNo>12345**</pmCertificateNo>
         <pmCertificateType>Other</pmCertificateType>
         <pmContactInfo>189100100**0</pmContactInfo>
         <pmGender>Male</pmGender>
         <pmName>test</pmName>
      </pmInfo>
      <si>ctcu</si>
      <status>Available</status>
   </data>
   <message>successful</message>
   <requestId>318BB676-0A2B-43A0-9AD8-F1D34E93750F</requestId>
   <success>true</success>
    </DescribePhysicalConnectionLOAResponse>
```

`JSON` format `{`

```json
    "code": "200",
    "data": {
        "companyName": "test1234",
        "constructionTime": "2019-02-26T08:00:00Z",
        "instanceId": "pc-bp1ca4wca27erts****",
        "lineType": "MSTP",
        "loaUrl":"http://*******",
        "pmInfo": [
```

`{`

```json
                "nextPMIndex": 1,
                "pmCertificateNo": "1234567",
                "pmCertificateType": "Other",
                "pmContactInfo": "18910010***",
                "pmGender": "Male",
                "pmName": "test"
```

`],`

```json
        "si": "ctcu",
        "status": "Available"
```

`},`

```json
    "message": "successful",
    "requestId": "318BB676-0A2B-43A0-9AD8-F1D34E93750F",
    "success": true
```

### VBR

#### CreateVirtualBorderRouter

Creates a virtual border router (VBR). Descriptions After you create a VBR for your Apsara Stack tenant account, the VBR is in the Act ive state. After you create a VBR for another Apsara Stack tenant account, the VBR is in the Unconf irmed state. The other Apsara Stack tenant account must confirm the VBR. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVirtualBorder Router | The operation that you want to perform. Set the value to Creat eVirt ualBorderRout er. |
| PhysicalConnectionId | String | Yes | pc-2zextbehcx**** | The ID of the Express Connect circuit. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VlanId | Integer | Yes | 0 | The VLAN ID of the VBR. Valid values: 0 t o 2999. Not e Only the owner of the Express Connect circuit can set this parameter. The VLAN IDs of two VBRs of the same Express Connect circuit must be different. |
| VbrOwnerId | Long | No | 1688111111111111 | The ID of the Apsara Stack tenant account to which the VBR belongs. By default, the ID of the current Apsara Stack tenant account or the account to which the Express Connect circuit belongs is used. |
| CircuitCode | String | No | longtel001 | The circuit code provided by the Internet service provider (ISP) for the Express Connect circuit. Not e Only the owner of the Express Connect circuit can set this parameter. |
| LocalGatewayIp | String | No | 192.168.XX.XX | The IP address of the VBR on the Apsara Stack side. |
| PeerGatewayIp | String | No | 192.168.XX.XX | The IP address of the VBR on the user side. Only the owner of the VBR can set this parameter. This parameter is required when you create a VBR for the owner of the Express Connect circuit. You can ignore this parameter when you create a VBR for another Apsara Stack tenant account. |
| PeeringSubnetMask | String | No | 255.255.255.252 | The subnet mask for the IP addresses of the VBR on the Apsara Stack side and on the user side. The two IP addresses must belong to the same subnet. |
| Description | String | No | Description | The description of the VBR. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Name | String | No | test | The name of the VBR. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter. It cannot start with http:// or https:// . |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| LocalIpv6GatewayIp | String | No | 2001:XXXX:3c4d:00 15:0000:0000:0000: 1a2b | The IPv6 address of the VBR on the Apsara Stack side. |
| PeerIpv6GatewayIp | String | No | 2001:XXXX:3c4d:00 15:0000:0000:0000: 1a2b | The IPv6 address of the VBR on the user side. Only the owner of the VBR can set this parameter. This parameter is required when you create a VBR for the owner of the Express Connect. You can ignore this parameter when you create a VBR for another Apsara Stack tenant account. |
| PeeringIpv6SubnetM ask | String | No | 2408:4004:cc:400:: /56 | The subnet mask for the IPv6 addresses of the VBR on the Apsara Stack side and on the user side. The two IPv6 addresses must fall within the same subnet. |
| EnableIpv6 | Boolean | No | false | Specifies whether to enable IPv6. Valid values: t rue: yes f alse (default): no |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VbrId | String | vbr- bp1jcg5cmxjbl9xgc**** | The ID of the VBR. |
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateVirtualBorderRouter &PhysicalConnectionId=pc-2zextbehcx**** &RegionId=cn-qingdao-env66-d01 &VlanId=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateRouterInterfaceResponse>
      <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
      <VbrId>vbr-bp1jcg5cmxjbl9xgc****</VbrId>
</CreateRouterInterfaceResponse>
```

`JSON` format `{`

```json
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
    "VbrId": "vbr-bp1jcg5cmxjbl9xgc****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId is not found. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |
| 400 | InvalidPhysicalConnectio nId.NotFound | The specified PhysicalConnectionId is not found. | The error message returned because the specified Express Connect circuit ID does not exist. |
| 400 | InvalidVlanId.Used | The specified VlanId has been used. | The error message returned because the VLAN ID is being used. |
| 400 | MissingParameter | The input parameter 'PhysicalConnectionId' that is mandatory for processing this request is not supplied. | The error message returned because PhysicalConnectionId is not set. |
| 400 | InvalidPhysicalConnectio nId.NotEnabled | The specified PhysicalConnectionId is not in Enabled state. | The error message returned because the status of the Express Connect circuit is invalid. Check the Express Connect circuit and try again. |
| 404 | InvalidVbrOwnerId.NotF ound | The specified VbrOwnerId is not valid. | The error message returned because VbrOwnerId is set to an invalid value. |
| 400 | InvalidVlanId.Malformed | The specified VlanId is not valid. | The error message returned because VlanId is set to an invalid value. |
| 400 | InvalidCircuitCode.Malfo rmed | The specified CircuitCode is not valid. | The error message returned because CircuitCode is set to an invalid value. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | MissingParameter | The input parameter 'LocalGatewayIp' that is mandatory for processing this request is not supplied. | The error message returned because LocalGatewayIp is not set. |
| 400 | InvalidLocalGatewayIp. Malformed | The specified LocalGatewayIp is not valid. | The error message returned because the IP address of the local gateway is invalid. |
| 400 | MissingParameter | The input parameter 'PeerGatewayIp' that is mandatory for processing this request is not supplied. | The error message returned because PeerGatewayIp is not set. |
| 400 | MissingParameter | The input parameter 'PeeringSubnetMask' that is mandatory for processing this request is not supplied. | The error message returned because PeeringSubnetMask is not set. |
| 400 | InvalidPeeringSubnetMa sk.Malformed | The specified PeeringSubnetMask is not valid. | The error message returned because PeeringSubnetMask is set to an invalid value. Check whether PeeringSubnetMask is set to a valid value. |
| 403 | Forbidden.LocalGatewa yIpNotAllowedByCaller | The caller is not allowed to specify the LocalGatewayIp parameter. | The error message returned because you are not allowed to set LocalGatewayIp. |
| 403 | Forbidden.PeerGateway IpNotAllowedByCaller | The caller is not allowed to specify the PeerGatewayIp parameter. | The error message returned because you are not allowed to set PeerGatewayIp. |
| 403 | Forbidden.PeeringSubn etMaskNotAllowedByCa ller | The caller is not allowed to specify the PeeringSubnetMask parameter. | The error message returned because you are not allowed to set PeeringSubnetMask. |
| 403 | Forbidden.NameNotAll owedByCaller | The caller is not allowed to specify the Name parameter. | The error message returned because you are not allowed to set Name. |
| 403 | Forbidden.DescriptionN otAllowedByCaller | The caller is not allowed to specify the Description parameter. | The error message returned because you are not allowed to set Description. |
| 400 | InvalidName.Malformed | The specified ?Name? is not valid. | The error message returned because the format of the name is invalid. |
| 400 | InvalidDescription.Malfo rmed | The specifid ?Description? is not valid. | The error message returned because the format of the resource description is invalid. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| 400 | QuotaExceeded.vbrPerp Conn | Virtual boarder router per PhysicalConnection quota exceed. | The error message returned because the number of VBRs of each Express Connect circuit has reached the upper limit. Reduce the number of VBRs and try again. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded.freevbr | Free virtual boarder router quota exceed. | The error message returned because the number of VBRs has reached the upper limit. |
| 400 | InvalidIp.NotSameSubn et | Local gateway ip and peer gateway ip are not in the same subnet. | The error message returned because the IP addresses of the local gateway and the peer gateway do not fall within the same subnet. |
| 404 | CROSS BID.FORBIDDEN _ | Create VBR across bid is illegal | The error message returned because you are not allowed to create a VBR for another Apsara Stack tenant account. |

#### DeleteVirtualBorderRouter

Deletes a virtual border router (VBR). When you call this operation, take note of the following rules: Before you delete a VBR, you must delete all router interfaces on the VBR. You can delete only a VBR that is in the Unconfirmed, Enabled, or Terminated state. If the owner of a physical connection wants to delete a VBR that belongs to another Apsara Stack tenant account, the VBR must be in the Unconfirmed state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVirtualBorder Router | The operation that you want to perform. Set the value to Delet eVirt ualBorderRout er. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the VBR is deployed. You can call the DescribeRegions operation to query region IDs. |
| VbrId | String | Yes | vbr- bp12mw1f8k3jgygk 9**** | The ID of the VBR. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F8BF7D24-F3EB-4E23- 9208-B77C6EB78E75 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DeleteVirtualBorderRouter &RegionId=cn-shanghai &VbrId=vbr-bp12mw1f8k3jgygk9**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVirtualBorderRouterResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteVirtualBorderRouterResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter does not exist in our records. | The error message returned because the specified vRouter does not exist. Check whether the ID of the VBR is valid. |
| 400 | InvalidOperation.RouterI nterfaceNotDeleted | The specified VirutalBorderRouter still has routerInterface. | The error message returned because the VBR is associated with router interfaces. |
| 400 | InvalidOperation.Operat ionNotAllowedInState | The specified VirutalBorderRouter is in invalid state. | The error message returned because the state of the VBR is invalid. Check the state of the VBR. |
| 403 | Forbidden.OperationNo tAllowedByUser | The caller is not allowed to delete the specified VirtualBorderRouter. | The error message returned because you are not allowed to delete the VBR. |
| 403 | Forbidden.MultiVlanRi | Multiple vlan router interfaces are found. | The error message returned because multiple VLAN router interfaces exist. |
| 403 | Forbidden.NoRiFound | No vlan router interfaces are found. | The error message returned because no VLAN router interface is available. |
| 400 | InvalidStatus.NotAllowe d | The virtual border has been associated by physicalConnection. | The error message returned because the VBR is associated with a physical connection. |

#### DescribeVirtualBorderRouters

Queries virtual border routers (VBRs) that you have created. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVirtualBord erRouters | The operation that you want to perform. Set the value toDescribeVirt ualBorderRout ers. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the VBR is deployed. You can call the DescribeRegions operation to query region IDs. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1 |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| Filter.N.Key | String | No | 1 | The key of filter condition N. Valid values of N:1 t o 5. Valid values of filter conditions: PhysicalConnect ionId: Filter by physical connection ID. VbrId: Filter by VBR ID. St at us: Filter by VBR status. Name: Filter by VBR name. AccessPoint Id: Filter by access point ID. t ype: Filter by physical connection type. |
| Filter.N.Value.N | RepeatList | No | 1 | The value of filter condition N. Valid values of N:1 t o 5. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VirtualBorderRout erSet | Array of VirtualBorderRout erType |   | The information about the queried VBR. |
| VirtualBorderRout erType |   |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessPointId | String | ap-cn-kojok1xxxxxxxx | The ID of the access point that is associated with the physical connection. |
| ActivationTime | String | 2017-06-08T12:20:55 | The first time when the VBR was activated. |
| AssociatedCens | Array of AssociatedCen |   | Cloud Enterprise Network (CEN). |
| AssociatedCen |   |   |   |
| CenId | String | cen-kojok19xxxxxxxx | The ID of the CEN instance. |
| CenOwnerId | Long | 1086496381294461 | The user ID (UID) of the Apsara Stack tenant account to which the CEN instance belongs. |
| CenStatus | String | Attached | The status of the CEN instance. |
| AssociatedPhysica lConnections | Array of AssociatedPhysica lConnection |   | The associated physical connection. |
| AssociatedPhysica lConnection |   |   |   |
| CircuitCode | String | 12 | The circuit code of the Internet service provider (ISP) that corresponds to the router interface of the VBR. |
| EnableIpv6 | Boolean | false |   |
| LocalGatewayIp | String | 116.62.xx.xx | The IP address of the on-premises router interface of the VBR. |
| LocalIpv6GatewayI p | String | 2408:****:cc:400::* |   |
| PeerGatewayIp | String | 116.62.xx.xx | The IP address of the peer router interface of the VBR. |
| PeerIpv6GatewayI p | String | 2408:****:cc:400::* |   |
| PeeringIpv6Subnet Mask | String | 2408:****:cc:400::/* |   |
| PeeringSubnetMas k | String | 255.255.255.252 | The subnet mask of the connection between the on-premises router interface and the peer router interface of the VBR. |

| Virtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PhysicalConnectio nBusinessStatus | String | Normal | The business status of the physical connection. |
| PhysicalConnectio nId | String | pc-119mfjzm7xxxxxxxx | The ID of the physical connection. |
| PhysicalConnectio nOwnerUid | String | qfrgrgs | The UID of the Apsara Stack tenant account to which the physical connection belongs. |
| PhysicalConnectio nStatus | String | Normal | The status of the physical connection. |
| Status | String | Active |   |
| VlanId | String | 0 | The VLAN ID of the VBR. |
| VlanInterfaceId | String | ri- kojok19x3j0q6kxxxxxxxx x | The ID of the router interface of the VBR. This ID can be used as the next hop of a route entry of the VBR. |
| CircuitCode | String | longtel001 | The circuit code provided by the ISP for the physical connection. |
| CreationTime | String | 2017-06-08T12:20:55 | The time when the VBR was created. |
| Description | String | VBR | The description of the VBR. |
| DetectMultiplier | Long | 3 | The multiple of the detection time. This value indicates the maximum number of dropped packets that is allowed by the receiver when the sender transmits packets. This value can be used to check whether the connection functions as expected. Valid values:3 t o 10. |
| EccId | String | ecc-h********* |   |
| EnableIpv6 | Boolean | false |   |
| LocalGatewayIp | String | 116.62.**. ** | The IP address configured on the Apsara Stack side. |
| LocalIpv6GatewayI p | String | 2408:****:cc:400::* |   |
| MinRxInterval | Long | 100 | The time interval to receive Bidirectional Forwarding Detection (BFD) packets. Valid values: 200 to 1000. Unit: milliseconds. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MinTxInterval | Long | 100 | The time interval to send BFD packets. Valid values: 200 to 1000. Unit: milliseconds. |
| Name | String | test | The name of the VBR. |
| PConnVbrExpireTi me | String | 2017-06-08T12:20:55 | The time when the VBR expires. |
| PeerGatewayIp | String | 116.62.**. ** | The IP address configured on the user side. |
| PeerIpv6GatewayI p | String | 2408:****:cc:400::* |   |
| PeeringIpv6Subnet Mask | String | 2408:****:cc:400::/* |   |
| PeeringSubnetMas k | String | 255.255.255.252 | The subnet mask of the connection between the Apsara Stack-side IP address and the user-side IP address. |
| PhysicalConnectio nBusinessStatus | String | Normal | The service status of the physical connection. |
| PhysicalConnectio nId | String | pc-119mfjzm7x****** | The ID of the physical connection to which the VBR connects. |
| PhysicalConnectio nOwnerUid | String | usdgbh123f****** | The UID of the Apsara Stack tenant account to which the physical connection belongs. |
| PhysicalConnectio nStatus | String | Normal | The status of the physical connection. |
| RecoveryTime | String | 2017-06-08T12:20:55 | The last time when the VBR was recovered from the Terminated state to the Active state. |
| RouteTableId | String | rtb-bp1nxxxxxxxx******* | The ID of the route table of the VBR. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | active | The status of the physical connection. Valid values: Init ial: Application is being reviewed. Approved: Application is approved. Allocat ing: Resources are being allocated. Allocat ed: The leased line is under construction. Conf irmed: waiting for user confirmation. Enabled: The physical connection is enabled. Reject ed: The application is rejected. Canceled: The application is canceled. Allocat ion Failed: The system failed to allocate resources. T erminat ed: The physical connection is terminated. |
| TerminationTime | String | 2017-06-08T12:20:55 | The last time when the VBR was terminated. |
| Type | String | ecc | The type of the physical connection. |
| VbrId | String | vbr-kojok19xx****** | The ID of the VBR. |
| VlanId | Integer | 10 | The VLAN ID of the VBR. |
| VlanInterfaceId | String | ri- 2zeo3xzyf38r4xx******* | The ID of the router interface of the VBR. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | DE77A7F3-3B74-41C0- A5BC-CAFD188C28B6 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeVirtualBorderRouters &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVirtualBorderRoutersResponse>
          <RequestId>AE65530E-8436-4FB1-8217-DCD35712AC89</RequestId>
          <PageNumber>1</PageNumber>
          <VirtualBorderRouterSet>
                <VirtualBorderRouterType>
                      <LocalGatewayIp>10.1.xx.xx</LocalGatewayIp>
                      <PeerGatewayIp>10.2.xx.xx</PeerGatewayIp>
                      <PhysicalConnectionOwnerUid>123157908XXXXXXXX</PhysicalConnectionOwnerUid>
                      <VlanId>10</VlanId>
                      <PhysicalConnectionStatus>Enabled</PhysicalConnectionStatus>
                      <PhysicalConnectionId>pc-2zeoaxkq3jotxxxxxxxx</PhysicalConnectionId>
                      <RouteTableId>vtb-2ze9hmd6yofwvxxxxxxxx</RouteTableId>
                      <PeeringSubnetMask>255.0.0.0</PeeringSubnetMask>
                      <CreationTime>2018-03-06T11:16:34Z</CreationTime>
                      <ActivationTime>2018-03-06T11:16:34Z</ActivationTime>
                      <Status>active</Status>
                      <PhysicalConnectionBusinessStatus>Normal</PhysicalConnectionBusinessStatus>
                      <VlanInterfaceId>ri-2zeum6rgu0586xxxxxxxx</VlanInterfaceId>
                      <AccessPointId>ap-cn-beijing-dx-A</AccessPointId>
                      <VbrId>vbr-2zecmmvg5gxxxxxxxx</VbrId>
                </VirtualBorderRouterType>
          </VirtualBorderRouterSet>
          <TotalCount>1</TotalCount>
          <PageSize>10</PageSize>
</DescribeVirtualBorderRoutersResponse>
```

`JSON` format `{`

```json
    "DescribeVirtualBorderRoutersResponse": {
        "RequestId": "AE65530E-8436-4FB1-8217-DCD35712AC89",
        "PageNumber": "1",
        "VirtualBorderRouterSet": {
            "VirtualBorderRouterType": {
                "LocalGatewayIp": "10.1.xx.xx",
                "PeerGatewayIp": "10.2.xx.xx",
                "PhysicalConnectionOwnerUid": "123157908XXXXXXXX",
                "VlanId": "10",
                "PhysicalConnectionStatus": "Enabled",
                "PhysicalConnectionId": "pc-2zeoaxkq3jotxxxxxxxx",
                "RouteTableId": "vtb-2ze9hmd6yofwvxxxxxxxx",
                "PeeringSubnetMask": "255.0.0.0",
                "CreationTime": "2018-03-06T11:16:34Z",
                "ActivationTime": "2018-03-06T11:16:34Z",
                "Status": "active",
                "PhysicalConnectionBusinessStatus": "Normal",
                "VlanInterfaceId": "ri-2zeum6rgu0586xxxxxxxx",
                "AccessPointId": "ap-cn-beijing-dx-A",
                "VbrId": "vbr-2zecmmvg5gxxxxxxxx"
```

`},`

```json
        "TotalCount": "1",
        "PageSize": "10"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidFilterKey.ValueNo tSupported | Specified filter key is not supported: Filter.X.key | The error message returned because Filter.X.key is not supported. |

6.12.4.

#### DescribeVirtualBorderRoutersForPhysicalConnection

Queries virtual border routers (VBRs) that are associated with an Express Connect circuit. The VBRs can be created by the owner of the Express Connect circuit and by other Apsara Stack tenant accounts. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVirtualBord erRoutersForPhysical Connection | The operation that you want to perform. Set the value to DescribeVirt ualBorderRout ersForPhysica lConnect ion. |
| PhysicalConnectionId | String | Yes | pc-119mfj**** | The ID of the Express Connect circuit. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the Express Connect circuit is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| Filter.N.Key | String | No | 1 | The key of the filter condition. Valid values of N: 1 to 5. Valid values of filter conditions: PhysicalConnect ionId: Filter by Express Connect circuit ID. VbrId: Filter by VBR ID. St at us: Filter by VBR status. Name: Filter by VBR name. AccessPoint Id: Filter by access point ID. eccId: Filter by Express Cloud Connect (ECC) instance ID. t ype: Filter by VBR type. |
| Filter.N.Value.N | RepeatList | No | 1 | The value of the filter condition. Valid values of N: 1 to 5. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |

| Developer Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VirtualBorderRout erForPhysicalConn ectionSet | Array of VirtualBorderRout erForPhysicalConn ectionType |   | The details of the VBR. |
| VirtualBorderRout erForPhysicalConn ectionType |   |   |   |
| ActivationTime | String | 2021-06-08T12:20:55 | The first time when the VBR was activated. |
| Bandwidth | String | 10 | The bandwidth of the VBR associated with the Express Connect circuit. Unit: Mbit/s. |
| CircuitCode | String | longtel001 | The circuit code of the Express Connect circuit. The circuit code is provided by the connectivity provider. |
| CreationTime | String | 2021-06-08T12:20:55 | The time when the VBR was created. |
| EccId | String | ecc-sjghe**** | The ID of the ECC instance. |
| EnableIpv6 | Boolean | false | Indicates whether IPv6 is enabled. Valid values: false: no true: yes |
| LocalGatewayIp | String | 10.0.XX.XX | The IPv4 address of the VBR. |
| LocalIpv6GatewayI p | String | 2001:XXXX:3c4d:0015: 0000:0000:0000:1a2b | The IPv6 address of the VBR. |
| PConnVbrBussines sStatus | String | Available | The status of the VBR. |
| PConnVbrChargeT ype | String | PrePaid | The billing method of the VBR. Valid values: PrePaid: subscription If you select subscription, make sure that your Apsara Stack tenant account supports balance payments or credit payments. PostPaid: pay-as-you-go |
| PConnVbrExpireTi me | String | 2021-06-22T12:20:55 | The time when the VBR expires. |

| Virtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PeerGatewayIp | String | 10.0.XX.XX | The IPv4 address of the gateway device on the user side. |
| PeerIpv6GatewayI p | String | 2001:XXXX:3c4d:0015: 0000:0000:0000:2a2b | The IPv6 address of the gateway device on the user side. |
| PeeringIpv6Subnet Mask | String | 2000:1234:0:a000::/55 | The subnet mask of the IPv6 addresses configured on the user side and Apsara Stack side. |
| PeeringSubnetMas k | String | 255.255.255.252 | The subnet mask of the IPv4 addresses configured on the user side and Apsara Stack side. |
| RecoveryTime | String | 2021-06-08T12:20:55 | The last time when the status of the VBR changed from T erminat ed to Act ive. |
| Status | String | Available | The status of the VBR. |
| TerminationTime | String | 2021-06-08T20:20:55 | The last time when the VBR was disabled. |
| Type | String | pconnVBR | The type of the VBR. |
| VbrId | String | vbr- bp16ksp61j7e0tk**** | The ID of the VBR. |
| VbrOwnerUid | Long | 253460731706911258 | The Apsara Stack tenant account ID of the VBR owner. If the VBR and Express Connect circuit belong to the same Apsara Stack tenant account, this value is empty. |
| VlanId | Integer | 1678 | The virtual LAN (VLAN) ID of the VBR. |
| TotalCount | Integer | 2 | The number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 7C5AE8B3-A2D8-428D- A2FF-93A225C0821E | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVirtualBorderRoutersForPhysicalConnection &PhysicalConnectionId=pc-119mfj**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVirtualBorderRoutersResponse>
  <TotalCount>2</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>7C5AE8B3-A2D8-428D-A2FF-93A225C0821E</RequestId>
  <PageNumber>1</PageNumber>
  <VirtualBorderRouterForPhysicalConnectionSet>
        <Status>Available</Status>
        <PeerGatewayIp>10.0.XX.XX</PeerGatewayIp>
        <ActivationTime>2021-06-08T12:20:55</ActivationTime>
        <VbrOwnerUid>253460731706911260</VbrOwnerUid>
        <CircuitCode>longtel001</CircuitCode>
        <PeerIpv6GatewayIp>2001:XXXX:3c4d:0015:0000:0000:0000:2a2b</PeerIpv6GatewayIp>
        <VbrId>vbr-bp16ksp61j7e0tk****</VbrId>
        <PConnVbrChargeType>PrePaid</PConnVbrChargeType>
        <PeeringSubnetMask>255.255.255.252</PeeringSubnetMask>
        <TerminationTime>2021-06-08T20:20:55</TerminationTime>
        <EnableIpv6>false</EnableIpv6>
        <PeeringIpv6SubnetMask>2000:1234:0:a000::/55</PeeringIpv6SubnetMask>
        <RecoveryTime>2021-06-08T12:20:55</RecoveryTime>
        <LocalGatewayIp>10.0.XX.XX</LocalGatewayIp>
        <Type>pconnVBR</Type>
        <Bandwidth>10</Bandwidth>
        <CreationTime>2021-06-08T12:20:55</CreationTime>
        <EccId>ecc-sjghe****</EccId>
        <PConnVbrExpireTime>2021-06-22T12:20:55</PConnVbrExpireTime>
        <LocalIpv6GatewayIp>2001:XXXX:3c4d:0015:0000:0000:0000:1a2b</LocalIpv6GatewayIp>
        <VlanId>1678</VlanId>
        <PConnVbrBussinessStatus>Available</PConnVbrBussinessStatus>
  </VirtualBorderRouterForPhysicalConnectionSet>
</DescribeVirtualBorderRoutersResponse>
```

`JSON` format `{`

```json
    "TotalCount": 2,
    "PageSize": 10,
    "RequestId": "7C5AE8B3-A2D8-428D-A2FF-93A225C0821E",
    "PageNumber": 1,
    "VirtualBorderRouterForPhysicalConnectionSet": {
        "Status": "Available",
        "PeerGatewayIp": "10.0.XX.XX",
        "ActivationTime": "2021-06-08T12:20:55",
        "VbrOwnerUid": 253460731706911260,
        "CircuitCode": "longtel001",
        "PeerIpv6GatewayIp": "2001:XXXX:3c4d:0015:0000:0000:0000:2a2b",
        "VbrId": "vbr-bp16ksp61j7e0tk****",
        "PConnVbrChargeType": "PrePaid",
        "PeeringSubnetMask": "255.255.255.252",
        "TerminationTime": "2021-06-08T20:20:55",
        "EnableIpv6": false,
        "PeeringIpv6SubnetMask": "2000:1234:0:a000::/55",
        "RecoveryTime": "2021-06-08T12:20:55",
        "LocalGatewayIp": "10.0.XX.XX",
        "Type": "pconnVBR",
        "Bandwidth": 10,
        "CreationTime": "2021-06-08T12:20:55",
        "EccId": "ecc-sjghe****",
        "PConnVbrExpireTime": "2021-06-22T12:20:55",
        "LocalIpv6GatewayIp": "2001:XXXX:3c4d:0015:0000:0000:0000:1a2b",
        "VlanId": 1678,
        "PConnVbrBussinessStatus": "Available"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConnectio nId.NotFound | The specified PhysicalConnectionId does not belong to user. | The error message returned because the specified Express Connect circuit does not belong to your Apsara Stack tenant account. |

#### TerminateVirtualBorderRouter

Disables a virtual border router (VBR). After you call this operation, the state of the VBR changes from Enabled to T erminat ing. After the VBR is disabled, its state changes to T erminat ed. Not e Only the owner of the physical connection to which the VBR connects can call this operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TerminateVirtualBor derRouter | The operation that you want to perform. Set the value to T erminat eVirt ualBorderRout er. |

| Developer Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-shanghai | The region where the VBR is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| VbrId | String | Yes | vbr- bp15zckdt37pq72** ** | The ID of the VBR that you want to disable. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-00**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=TerminateVirtualBorderRouter &RegionId=cn-shanghai &VbrId=vbr-bp15zckdt37pq72**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TerminateVirtualBorderRouterResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</TerminateVirtualBorderRouterResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter is not found. | The error message returned because the specified VBR does not exist. Check whether the specified VBR ID is valid. |

| Virtual Private | Cloud |   | Developer Guide·API reference |
|---|---|---|---|
| HttpCode | Error code | Error message | Description |
| 400 | InvalidOperation.Operat ionNotAllowedInState | The specified VirutalBorderRouter is in invalid state. | The error message returned because the state of the specified VBR is invalid. Check the state of the VBR. |
| 403 | Forbidden.OperationTer minateNotAllowedByUs er | The caller is not allowed to terminate the specified VirtualBorderRouter. | The error message returned because you are not authorized to disable the specified VBR. |

#### RecoverVirtualBorderRouter

Enables a disabled VBR. After you call the operation, the state of the VBR changes from T erminat ed to Recovering. When the VBR is enabled, its state changes to Enabled. When you call this operation, take note of the following items: Only the owner of the physical connection can call this operation. The physical connection to which the VBR belongs must be in the Enabled state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RecoverVirtualBorde rRouter | The operation that you want to perform. Set the value to RecoverVirt ualBorderRout er. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the VBR is deployed. You can call the DescribeRegions operation to query region IDs. |
| VbrId | String | Yes | vbr- bp1lhl0taikrte**** | The ID of the VBR. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=RecoverVirtualBorderRouter &RegionId=cn-shanghai &VbrId=vbr-bp1lhl0taikrte**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RecoverVirtualBorderRouterResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</RecoverVirtualBorderRouterResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter is not found. | The error message returned because the specified VBR does not exist. Check whether the parameter is set to a valid value. |
| 400 | InvalidOperation.Operat ionNotAllowedInState | The specified VirutalBorderRouter is in invalid state | The error message returned because the status of the VBR interface is invalid. |
| 400 | OperationFailed.VlanIdA lreadyInUse | The specifed vlanId has been used. | The error message returned because the VLAN interface is being used. |
| 403 | Forbidden.OperationRec overNotAllowedByUser | The caller is not allowed to recover the specified VirtualBorderRouter. | The error message returned because you do not have the permissions to recover the VBR. |

#### ModifyVirtualBorderRouterAttribute

Modifies the configuration of a virtual border router (VBR). Descriptions Only the owner of an Express Connect circuit can modify the VlanId parameter. One VLAN ID of an Express Connect circuit cannot be used by two VBRs at the same time. The VLAN ID of a VBR in the T erminat ed state is reserved for seven days and cannot be used by other VBRs. The VLAN ID can be used by other VBRs after 7 days. You cannot set LocalGat ewayIp, PeerGat ewayIp, or PeeringSubnet Mask for VBRs that do not belong to your Apsara Stack tenant account. Set PeeringSubnet Mask to a subnet mask with 24 to 30 bits in length (255.255.255.0～255.255.255.252). Set LocalGat ewayIp and PeerGat ewayIp to IP addresses that belong to the same CIDR block. For example, you can set LocalGatewayIp to 192.168.XX.XX, PeerGatewayIp to 192.168.XX.XX, and PeeringSubnetMask to 255.255.255.248. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVirtualBorder RouterAttribute | The operation that you want to perform. Set the value to Modif yVirt ualBorderRout erAt t ribut e. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the VBR. You can call the DescribeRegions operation to query the most recent region list. |
| VbrId | String | Yes | vbr- 2zehfr9ovv4b**** | The ID of the VBR. |
| VlanId | Integer | No | 0 | The VLAN ID of the VBR. Valid values: 0 t o 2999. Not e Only the owner of the Express Connect circuit can set this parameter. The VLAN IDs of two VBRs of the same Express Connect circuit must be different. |
| CircuitCode | String | No | longtel001 | The circuit code provided by the Internet service provider (ISP) for the Express Connect circuit. Not e Only the owner of the Express Connect circuit can set this parameter. |
| LocalGatewayIp | String | No | 192.168.XX.XX | The IP address of the VBR on the Apsara Stack side. |
| PeerGatewayIp | String | No | 192.168.XX.XX | The IP address of the VBR on the user side. Only the owner of the VBR can set this parameter. This parameter is required when you create a VBR for the owner of the Express Connect circuit. You can ignore this parameter when you create a VBR for another Apsara Stack tenant account. |
| PeeringSubnetMask | String | No | 255.255.255.252 | The subnet mask for the IP addresses of the VBR on the Apsara Stack side and on the user side. The two IP addresses must belong to the same subnet. |
| MinTxInterval | Long | No | 300 | The time interval to send BFD packets. Valid values: 200 t o 1000. Unit: milliseconds. |

| Developer Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| MinRxInterval | Long | No | 300 | The time interval to receive BFD packets. Valid values: 200 t o 1000. Unit: milliseconds. |
| DetectMultiplier | Long | No | 3 | The maximum number of dropped packets that is allowed by the receiver when the initiator transmits packets. This value can be used to check whether a connection works as expected. Valid values: 3 t o 10. |
| Description | String | No | desc | The description of the VBR. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| Name | String | No | VBR | The name of the VBR. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter. It cannot start with http:// or https:// . |
| AssociatedPhysicalC onnections | String | No | pc-kojok19****** | The ID of the Express Connect circuit. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 00xxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| LocalIpv6GatewayIp | String | No | 2001:XXXX:3c4d:00 15:0000:0000:0000: 1a2b | The IPv6 address of the VBR on the Apsara Stack side. |
| PeerIpv6GatewayIp | String | No | 2001:XXXX:3c4d:00 15:0000:0000:0000: 1a2b | The IPv6 address of the VBR on the user side. Only the owner of the VBR can set this parameter. This parameter is required when you create a VBR for the owner of the Express Connect. You can ignore this parameter when you create a VBR for another Apsara Stack tenant account. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PeeringIpv6SubnetM ask | String | No | 2408:4004:cc:400:: /56 | The subnet mask for the IPv6 addresses of the VBR on the Apsara Stack side and on the user side. The two IPv6 addresses must fall within the same subnet. |
| EnableIpv6 | Boolean | No | false | Specifies whether to enable IPv6. Valid values: t rue: yes f alse (default): no |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 980960B0-2969-40BF- 8542-EBB34FD358AB | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVirtualBorderRouterAttribute &RegionId=cn-qingdao-env66-d01 &VbrId=vbr-2zehfr9ovv4b**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVirtualBorderRouterAttributeResponse>
      <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId>
</ModifyVirtualBorderRouterAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId is not found. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |
| 400 | InvalidVbrId.NotFound | The specified VirutalBorderRouter is not found. | The error message returned because the specified VBR does not exist. Check whether the parameter is set to a valid value. |

| Developer Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|
| HttpCode | Error code | Error message | Description |
| 400 | InvalidVlanId.Used | The specified VlanId has been used. | The error message returned because the VLAN ID is being used. |
| 400 | InvalidCircuitCode.Malfo rmed | The specified CircuitCode is not valid. | The error message returned because CircuitCode is set to an invalid value. |
| 400 | InvalidVlanId.Malformed | The specified VlanId is not valid. | The error message returned because VlanId is set to an invalid value. |
| 400 | InvalidIp.Malformed | The specified ip address is not valid. | The error message returned because the specified private IP address is invalid. Check the private IP address. |
| 400 | InvalidPeeringSubnetMa sk.Malformed | The specified PeeringSubnetMask is not valid. | The error message returned because PeeringSubnetMask is set to an invalid value. Check whether PeeringSubnetMask is set to a valid value. |
| 403 | Forbidden.CircuitCodeN otAllowedByCaller | The caller is not allowed to modify. | The error message returned because you are not allowed to modify CircuitCode. |
| 403 | Forbidden.CircuitCodeN otAllowedByCaller | The caller is not allowed to specify the CircuitCode parameter. | The error message returned because you are not allowed to set CircuitCode. |
| 403 | Forbidden.LocalGatewa yIpNotAllowedByCaller | The caller is not allowed to specify the LocalGatewayIp parameter. | The error message returned because you are not allowed to set LocalGatewayIp. |
| 403 | Forbidden.PeerGateway IpNotAllowedByCaller | The caller is not allowed to specify the PeerGatewayIp parameter. | The error message returned because you are not allowed to set PeerGatewayIp. |
| 403 | Forbidden.PeeringSubn etMaskNotAllowedByCa ller | The caller is not allowed to specify the PeeringSubnetMask parameter. | The error message returned because you are not allowed to set PeeringSubnetMask. |
| 403 | Forbidden.VlanIdNotAll owedByCaller | The caller is not allowed to specify the VlanId. | The error message returned because you are not allowed to specify the VLAN ID. |
| 403 | Forbidden.NameNotAll owedByCaller | The caller is not allowed to specify the Name parameter. | The error message returned because you are not allowed to set Name. |
| 403 | Forbidden.DescriptionN otAllowedByCaller | The caller is not allowed to specify the Description parameter. | The error message returned because you are not allowed to set Description. |
| 400 | InvalidIp.NotSameSubn et | Local gateway ip and peer gateway ip are not in the same subnet. | The error message returned because the IP addresses of the local gateway and the peer gateway do not fall within the same subnet. |

6.12.8.

#### AssociatePhysicalConnectionToVirtualBorderRouter

Associates a virtual border router (VBR) with an Express Connect circuit. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociatePhysicalCo nnectionToVirtualBo rderRouter | The operation that you want to perform. Set the value to Associat ePhysicalConnect ionT oVirt ualB orderRout er. |
| PhysicalConnectionId | String | Yes | pc- bp1qrb3044eqixog* *** | The ID of the Express Connect circuit. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
| VbrId | String | Yes | vbr- bp186tnz6rijyhj**** | The ID of the VBR. |
| VlanId | String | Yes | 123 | The VLAN ID of the VBR. Valid values: 1 to 2999. Not e Only the owner of the Express Connect circuit can set this parameter. The VLAN IDs of two VBRs of the same the Express Connect circuit must be different. |
| CircuitCode | String | No | longtel001 | The circuit code of the Express Connect circuit. The circuit code is provided by the connectivity provider. Not e Only the owner of the Express Connect circuit can set this parameter. |
| LocalGatewayIp | String | No | 10.10.XX.XX | The IP address of the VBR on the Apsara Stack side. |
| PeerGatewayIp | String | No | 10.10.XX.XX | The IP address of the peer router interface of the VBR. Only the owner of the VBR can set or modify the value. If the VBR is in the Enabled state, you cannot leave this parameter empty. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PeeringSubnetMask | String | No | 255.255.255.0 | The subnet mask for the IP addresses of the VBR on the Apsara Stack side and on the user side. The two IP addresses must fall within the same subnet. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id of each API request may be different. |
| LocalIpv6GatewayIp | String | No | 2001:XXXX:3c4d:00 15:0000:0000:0000: 1a2b | The IPv6 address of the gateway device on the Apsara Stack side. |
| PeerIpv6GatewayIp | String | No | 2001:XXXX:3c4d:00 15:0000:0000:0000: 2a2b | The IPv6 address of the gateway device in the data center. |
| PeeringIpv6SubnetM ask | String | No | 2408:4004:cc:400:: /56 | The subnet mask for the IPv6 addresses of the gateway devices in the data center and the VBRs. The two IPv6 addresses must fall within the same subnet. |
| EnableIpv6 | String | No | true | Specifies whether to enable IPv6. Valid values: t rue: yes f alse: no |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 980960B0-2969-40BF- 8542-EBB34FD358AB | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AssociatePhysicalConnectionToVirtualBorderRouter &PhysicalConnectionId= pc-bp1qrb3044eqixog**** &RegionId=cn-qingdao-env66-d01 &VbrId=vbr-bp186tnz6rijyhj**** &VlanId=123 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AssociatePhysicalConnectionToVirtualBorderRouterResponse>
  <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId>
</AssociatePhysicalConnectionToVirtualBorderRouterResponse>
```

`JSON` format `{`

```json
    "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidInstanceId.NotFo und | The specified Instance does not exist in the specified region. | The error message returned because the instance does not exist in the specified region. |
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter does not exist in our records. | The error message returned because the specified VBR does not exist. Check whether the parameter is set to a valid value. |
| 400 | InvalidOperation.RouterI nterfaceNotDeleted | The specified VirutalBorderRouter still has routerInterface. | The error message returned because the VBR is associated with a router interface. |
| 400 | InvalidOperation.Operat ionNotAllowedInState | The specified VirutalBorderRouter is in invalid state. | The error message returned because the specified VBR is in an invalid state. Check the status of the VBR. |
| 403 | Forbidden.OperationNo tAllowedByUser | The caller is not allowed to delete the specified VirtualBorderRouter. | The error message returned because you are not allowed to delete the VBR. |
| 403 | Forbidden.MultiVlanRi | Multiple vlan router interfaces are found. | The error message returned because multiple VLAN router interfaces exist. |
| 403 | Forbidden.NoRiFound | No vlan router interfaces are found. | The error message returned because no VLAN router interface is available. |
| 400 | InvalidStatus.NotAllowe d | Invalid virtual border router status. | The error message returned because the status of the VBR does not support this operation. |
| 404 | InvalidRegionId.NotFoun d | The specified RegionId is not found. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |

| Developer Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|
| HttpCode | Error code | Error message | Description |
| 400 | InvalidPhysicalConnectio nId.NotFound | The specified PhysicalConnectionId is not found. | The error message returned because the specified Express Connect circuit ID does not exist. |
| 400 | InvalidVlanId.Used | The specified VlanId has been used. | The error message returned because the VLAN ID is being used. |
| 400 | MissingParameter | The input parameter 'PhysicalConnectionId' that is mandatory for processing this request is not supplied. | The error message returned because the PhysicalConnectionId parameter is not specified. |
| 400 | InvalidPhysicalConnectio nId.NotEnabled | The specified PhysicalConnectionId is not in Enabled state. | The error message returned because the Express Connect circuit is in an invalid state. Check the Express Connect circuit and try again. |
| 404 | InvalidVbrOwnerId.NotF ound | The specified VbrOwnerId is not valid. | The error message returned because VbrOwnerId is set to an invalid value. |
| 400 | MissingParameter | The input parameter 'VlanId' that is mandatory for processing this request is not supplied. | The error message returned because VlanId is not set. |
| 400 | InvalidVlanId.Malformed | The specified VlanId is not valid. | The error message returned because the value of VlanId is invalid. |
| 400 | InvalidCircuitCode.Malfo rmed | The specified CircuitCode is not valid. | The error message returned because CircuitCode is set to an invalid value. |
| 400 | MissingParameter | The input parameter 'LocalGatewayIp' that is mandatory for processing this request is not supplied. | The error message returned because LocalGatewayIp is not set. |
| 400 | InvalidLocalGatewayIp. Malformed | The specified LocalGatewayIp is not valid. | The error message returned because the IP address of the VBR is invalid. |
| 400 | MissingParameter | The input parameter 'PeerGatewayIp' that is mandatory for processing this request is not supplied. | The error message returned because PeerGatewayIp is not set. |
| 400 | InvalidPeerGatewayIp.M alformed | The specified PeerGatewayIp is not valid. | The error message returned because the value of PeerGatewayIp is invalid. |
| 400 | MissingParameter | The input parameter 'PeeringSubnetMask' that is mandatory for processing this request is not supplied. | The error message returned because PeeringSubnetMask is not set. |
| 400 | InvalidPeeringSubnetMa sk.Malformed | The specified PeeringSubnetMask is not valid. | The error message returned because PeeringSubnetMask is set to an invalid value. Check whether PeeringSubnetMask is set to a valid value. |
| 403 | Forbidden.LocalGatewa yIpNotAllowedByCaller | The caller is not allowed to specify the LocalGatewayIp parameter. | The error message returned because you are not allowed to set LocalGatewayIp. |

| Virtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbidden.PeerGateway IpNotAllowedByCaller | The caller is not allowed to specify the PeerGatewayIp parameter. | The error message returned because you are not allowed to set PeerGatewayIp. |
| 403 | Forbidden.PeeringSubn etMaskNotAllowedByCa ller | The caller is not allowed to specify the PeeringSubnetMask parameter. | The error message returned because you are not allowed to set PeeringSubnetMask. |
| 403 | Forbidden.NameNotAll owedByCaller | The caller is not allowed to specify the Name parameter. | The error message returned because you are not allowed to set Name. |
| 403 | Forbidden.DescriptionN otAllowedByCaller | The caller is not allowed to specify the Description parameter. | The error message returned because you are not allowed to set Description. |
| 400 | InvalidName.Malformed | The specified ?Name? is not valid. | The error message returned because the format of the name is invalid. |
| 400 | InvalidDescription.Malfo rmed | The specifid ?Description? is not valid. | The error message returned because the specified description is invalid. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| 400 | QuotaExceeded.vbrPerp Conn | Virtual boarder router per PhysicalConnection quota exceed. | The error message returned because the number of VBRs of each Express Connect circuit has reached the upper limit. Reduce the number of VBRs and try again. |
| 400 | EXCEED ASSOCIATE MA _ _ X NUM _ | assocaite virtual boarder num too many. | The error message returned because the number of associated VBRs has reached the upper limit. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidIp.NotSameSubn et | Local gateway ip and peer gateway ip are not in the same subnet. | The error message returned because the IP addresses of the local gateway and the peer gateway do not fall within the same subnet. |
| 400 | InvalidStatus.StatusNot Enabled | The physical connection status is invalid. | The error message returned because the status of the Express Connect circuit does not support this operation. Check the status of the Express Connect circuit. |
| 400 | PHYSICAL NOT ALLOW _ _ _ ASSOCIATE VBR _ | The specified operation not allow. | The error message returned because the Express Connect circuit is associated with a VBR and the operation cannot be performed. |

6.12.9.

#### UnassociatePhysicalConnectionFromVirtualBorderRouter

Disassociates a virtual border router (VBR) from a physical connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociatePhysical ConnectionFromVirt ualBorderRouter | The operation that you want to perform. Set the value toUnassociat ePhysicalConnect ionFromVi rt ualBorderRout er. |
| PhysicalConnectionId | String | Yes | pc- bp1qrb3044eqixog* *** | The ID of the physical connection. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the physical connection is deployed. |
| VbrId | String | Yes | vbr- bp16ksp61j7e0tkn** *** | The VLAN ID of the VBR. Valid values: 1 to 2999. Not e Only the owner of the physical connection can set this parameter. The VLAN IDs of two VBRs of the same physical connection must be different. |
| ClientToken | String | No | longtel001 | The circuit code provided by the Internet service provider (ISP) of the physical connection. Not e Only the owner of the physical connection can set this parameter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 980960B0-2969-40BF- 8542-EBB34FD358AB | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=UnassociatePhysicalConnectionFromVirtualBorderRouter &PhysicalConnectionId=pc-bp1qrb3044eqixog**** &RegionId=cn-hangzhou &VbrId=vbr-bp16ksp61j7e0tkn***** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UnassociatePhysicalConnectionFromVirtualBorderRouterResponse>
      <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId>
    </UnassociatePhysicalConnectionFromVirtualBorderRouterResponse>
```

`JSON` format `{`

```json
    "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter does not exist in our records. | The error message returned because the specified VBR does not exist. Check whether the parameter is set to a valid value. |
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter or PhysicalConnection does not exist in our records. | The error message returned because the VBR or physical connection does not exist. |
| 400 | PARAMETER MUST NOT _ _ NULL _ | The specified physical connection id or vbrId must not be null. | The error message returned because the VbrId and PhysicalConnectionId parameters are not set. |
| 400 | PHYSICAL NOT ASSOCIA _ _ TE TO VBR _ _ | The specified PhysicalConnection have not associate to the vbr. | The error message returned because no VBR is created for the physical connection. |
| 400 | ROUTER INTERFACE REF _ _ ERED BY ROUTEENTRY _ _ | The specified VlanInterface has been used by routeEntry. | The error message returned because the VLAN interface is being used by a route entry. |
| 400 | InvalidStatus.NotAllowe d | Invalid virtual border router status. | The error message returned because the status of the VBR is invalid. |
| 400 | PHYSICAL NOT ALLOW _ _ _ ASSOCIATE VBR _ | The specified operation not allow. | The error message returned because the physical connection is associated with a VBR and the operation cannot be performed. |

### BGP

#### CreateBgpGroup

Creates a Border Gateway Protocol (BGP) group for a specified virtual border router (VBR). BGP groups allow VBRs to communicate with data centers. Each BGP group is associated with a VBR. You can add a BGP peer that needs to communicate with a VBR to the corresponding BGP group and advertise the BGP network in the VBR. BGP groups are used to simplify BGP configurations. You can save time and effort by adding BGP peers that use the same configurations to one BGP group. You must use an autonomous system (AS) number to create a BGP group. When you call this operation, take note of the following limits: Only BGP4 is supported by the BGP groups. BGP groups support IPv4 BGP. IPv6 BGP is not supported. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBgpGroup | The operation that you want to perform. Set the value to Creat eBgpGroup. |
| PeerAsn | Long | Yes | 65515 | The AS number of the on-premises device. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region to which the BGP group belongs. You can call the DescribeRegions operation to query the most recent region list. |
| RouterId | String | Yes | vbr- m5eadkqe6budw4sj **** | The ID of the VBR that is associated with the BGP group. |
| Name | String | No | test | The name of the BGP group. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter. It cannot start with http:// or https:// . |
| Description | String | No | BGP | The description of the BGP group. The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with http:// or https:// . |
| LocalAsn | Long | No | 45104 | The AS number of the device on the Apsara Stack side. |
| AuthKey | String | No | !PWZ**** | The authentication key of the BGP group. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IsFakeAsn | Boolean | No | true | Specifies whether to use a fake ASN. Valid values: f alse (default): no t rue: yes Not e A running BGP router typically belongs to only one AS. If you want to replace the current AS with a new one (for example, the current AS needs to be migrated or merged with another one) and you cannot modify BGP configurations, you can specify a fake AS number to establish connections to the on-premises device. This ensures that your services are not interrupted. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id of each API request may be different. |
| IpVersion | String | No | ipv4 | The IP version. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BgpGroupId | String | bgpg- 2zendnzngq9lkjkhv**** | The ID of the BGP group. |
| RequestId | String | C1221A1F-2ACD-4592- 8F27-474E02883159 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateBgpGroup &PeerAsn=45103 &RegionId=cn-qingdao-env66-d01 &RouterId= vbr-m5eadkqe6budw4sj**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateBgpGroupResponse>
  <RequestId>C1221A1F-2ACD-4592-8F27-474E02883159</RequestId>
  <BgpGroupId>bgpg-2zendnzngq9lkjkhv****</BgpGroupId>
</CreateBgpGroupResponse>
```

`JSON` format `{`

```json
    "RequestId": "C1221A1F-2ACD-4592-8F27-474E02883159",
    "BgpGroupId": "bgpg-2zendnzngq9lkjkhv****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number has reached the upper limit. |
| 400 | QuotaExceeded.BgpNet work | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the upper limit. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple Express Connect circuits cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified VBR does not exist. Check whether the specified VBR is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Malfor med | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDescription.M alformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.Malf ormed | Specified Bgp Group authkey is not valid. | The error message returned because the authentication key of the BGP group is invalid. |
| 404 | InvalidRegionId.NotFoun d | The specified RegionId is not found. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malform ed | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as the AS number on the Apsara Stack side. |
| 400 | InvalidParams.NotFoun d | instance not found | The error message returned because the specified instance does not exist. |
| 400 | InvalidParams.NotFoun d | vpc instance not found | The error message returned because the specified virtual private cloud (VPC) does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.AlreadyEx ists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.CannotOp erate | invalid status cannot operate | The error message returned because you cannot perform the operation when the specified resource is in the current state. |
| 400 | QuotaExceeded.Bgp | bgp group count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the upper limit. |

#### DescribeBgpGroups

Queries Border Gateway Protocol (BGP) groups in a region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBgpGroups | The operation that you want to perform. Set the value to DescribeBgpGroups. |
| RegionId | String | Yes | cn-shanghai | The region to which the BGP group belongs. You can call the DescribeRegions operation to query region IDs. |
| RouterId | String | No | vrt-kojok19x3j0q6kx | The ID of the virtual border router (VBR) that is associated with the BGP group. |
| BgpGroupId | String | No | bgpg- wz9f62v4fbg2gxxxx xxxx | The ID of the BGP group. |
| IsDefault | Boolean | No | false | Specifies whether the specified BGP group is the default one. |

| Developer Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |

| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
|---|---|---|---|---|
| PageSize | Integer | No | 1 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| BgpGroups | Array of BgpGroup |   | The detailed information about the BGP group. |
| BgpGroup |   |   |   |
| AuthKey | String | ! PWZ2wsq | The key used by the BGP group. |
| BgpGroupId | String | bgp- wz977wcrmb69axxxxxx xx | The ID of the BGP group. |
| Description | String | The description of the BGP group. | The description of the BGP group |
| Hold | String | 30 | The hold time of the BGP connection. If no message is received within the hold time, the BGP peer is considered disconnected. |
| IpVersion | String | IPv4 |   |
| IsFake | String | true | Whether the autonomous system (AS) number is valid. |
| Keepalive | String | 10 | The keepalive time. |
| LocalAsn | String | 45104 | The local AS number. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | The name of the BGP group | The name of the BGP group. |
| PeerAsn | String | 1111 | The AS number of the BGP peer. |
| RegionId | String | cn-shanghai | The ID of the region to which the BGP group belongs. For more information about region IDs, see Regions and zones. |
| RouteLimit | String | 99 | Routing limits. |
| RouterId | String | vrt- bp1lhl0taikrteen***** | The ID of the VBR. |
| Status | String | active | The status of the BGP peer. |
| RequestId | String | 1D0971B2-A35A-42C1- A44C-E91360C36C0B | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeBgpGroups &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBgpGroupsResponse>
   <TotalCount>1</TotalCount>
   <PageSize>10</PageSize>
   <RequestId>09E2C0FD-37FF-4737-80DF-517AC36D43DB</RequestId>
   <BgpGroups>
      <BgpGroup>
         <BgpGroupId>bgpg-2zev8h2wo4******</BgpGroupId>
         <LocalAsn>45104</LocalAsn>
         <Hold>30</Hold>
         <Description></Description>
         <AuthKey></AuthKey>
         <IsFake>true</IsFake>
         <PeerAsn>234</PeerAsn>
         <Keepalive>10</Keepalive>
         <RouteLimit>99</RouteLimit>
         <Name>Group1</Name>
         <Status>Pending</Status>
         <RouterId>vbr-2zecmmvg5gvu8i4******</RouterId>
         <RegionId>cn-beijing</RegionId>
      </BgpGroup>
   </BgpGroups>
</DescribeBgpGroupsResponse>
```

`JSON` format `{`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "09E2C0FD-37FF-4737-80DF-517AC36D43DB",
    "BgpGroups": {
        "BgpGroup": [
```

`{`

```json
                "BgpGroupId": "bgpg-2zev8h2wo******",
                "LocalAsn": 45104,
                "Hold": 30,
                "Description": "",
                "AuthKey": "",
                "IsFake": true,
                "PeerAsn": 234,
                "Keepalive": 10,
                "RouteLimit": 99,
                "Name": "Group1",
                "Status": "Pending",
                "RouterId": "vbr-2zecmmvg5gvu8i4*****",
                "RegionId": "cn-beijing"
```

`]` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because unknown errors occur. |
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |

#### ModifyBgpGroupAttribute

Modifies the configuration of a Border Gateway Protocol (BGP) group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBgpGroupAttr ibute | The operation that you want to perform. Set the value to Modif yBgpGroupAt t ribut e. |
| BgpGroupId | String | Yes | bgpg- wz9f62v4fbg2g***** *** | The ID of the BGP group. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the BGP group is deployed. You can call the DescribeRegions operation to query region IDs. |

| Virtual Private Cloud |   |   |   | Developer Guide·API reference |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Name | String | No | test | The name of the BGP group. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter and cannot start with http:// or https:// . |
| Description | String | No | BGP | The description of the BGP group. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . |
| LocalAsn | Long | No | 23 | The autonomous system (AS) number of the device on the cloud side. |
| PeerAsn | Long | No | 1111 | The AS number of the local device. |
| AuthKey | String | No | ! PWZ2wsq | The authentication key of the BGP group. |
| IsFakeAsn | Boolean | No | true | A router that runs BGP typically belongs to only one AS. In some cases, for example, the AS needs to be migrated or is merged with another AS, a new AS number replaces of the original one. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001******* | The client token is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8C3C6D7C-A1CE-4FD8- BC57-DC493A55F76F | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=ModifyBgpGroupAttribute &BgpGroupId=bgpg-wz9f62v4fbg2g******** &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyBgpGroupAttributeResponse>
      <RequestId>C1221A1F-2ACD-4592-8F27-474E02883159</RequestId>
</ModifyBgpGroupAttributeResponse>
```

`JSON` format `{`

```json
  "RequestId": "C1221A1F-2ACD-4592-8F27-474E02883159"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | Specified value of "regionId" is not supported. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the virtual border router (VBR) has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number has exceeded the upper limit. |
| 400 | QuotaExceeded.BgpNet work | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the upper limit. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple physical connections cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified VBR does not exist. Check whether the specified VBR ID is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Malfor med | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription.Ma lformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.Malf ormed | Specified Bgp Group authkey is not valid. | The error message returned because the verification key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |

| Virtual Private | Cloud |   | Developer Guide·API reference |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidPeerAsn.Malform ed | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous system (AS) number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotFoun d | instance not found | The error message returned because the instance does not exist. |
| 400 | InvalidParams.NotFoun d | vpc instance not found | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.AlreadyEx ists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.CannotOp erate | invalid status cannot operate | The error message returned because the state is invalid and the operation cannot be performed. |

#### DeleteBgpGroup

Deletes a Border Gateway Protocol (BGP) group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBgpGroup | The operation that you want to perform. Set the value to Delet eBgpGroup. |
| BgpGroupId | String | Yes | bgpg- wz9f62v4fbg2gxxxx xxxx | The ID of the BGP group. |
| RegionId | String | Yes | cn-shanghai | The region to which the BGP group belongs. You can call the DescribeRegions operation to query region IDs. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 97E2E97F-968C-48AF- A310-AC4D068854DB | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=DeleteBgpGroup &BgpGroupId=bgpg-wz9f62v4fbg2gxxxxxxxx &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteBgpGroupResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteBgpGroupResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | Specified value of "regionId" is not supported. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the virtual border router (VBR) has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The Network Quality Analyzer (NQA) number has exceeded the quota of the VBR. |
| 400 | QuotaExceeded.BgpNet work | bgp network count per vbr quota exceed. | The number of BGP networks in the VBR has reached the upper limit. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The IP addresses of multiple physical connections cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified vRouter does not exist. Check whether the specified VBR is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Malfor med | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription.Ma lformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |

| Virtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidBgpAuthkey.Malf ormed | Specified Bgp Group authkey is not valid. | The error message returned because the verification key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malform ed | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous system (AS) number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotNull | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous system (AS) number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotFoun d | instance not found | The error message returned because the instance does not exist. |
| 400 | InvalidParams.NotFoun d | vpc instance not found | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.AlreadyEx ists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.CannotOp erate | invalid status cannot operate | The error message returned because the state is invalid and the operation cannot be performed. |

#### CreateBgpPeer

Adds a Border Gateway Protocol (BGP) peer to a BGP group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBgpPeer | The operation that you want to perform. Set the value to Creat eBgpPeer. |
| BgpGroupId | String | Yes | bgpg- wz9f62v4fbg**** | The ID of the BGP group to which you want to add a BGP peer. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region to which the BGP group belongs. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PeerIpAddress | String | No | 116.62.XX.XX | The IP address of the BGP peer. |
| EnableBfd | Boolean | No | true | Specifies whether to enable the Bidirectional Forwarding Detection (BFD) feature. Valid values: t rue: enables BFD. f alse: disables BFD. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id of each API request may be different. |
| IpVersion | String | No | ipv4 | The IP version. |
| BfdMultiHop | Integer | No | 3 | The multihop BFD feature. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BgpPeerId | String | bgp- m5eoyp2mwegk8ce9v* *** | The ID of the BGP peer. |
| RequestId | String | D4B7649A-61BB-4C64- A586-1DFF1EDA6A42 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateBgpPeer &BgpGroupId=bgpg-wz9f62v4fbg**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateBgpPeerResponse>
  <BgpPeerId>bgp-m5eoyp2mwegk8ce9v****</BgpPeerId>
  <RequestId>D4B7649A-61BB-4C64-A586-1DFF1EDA6A42</RequestId>
</CreateBgpPeerResponse>
```

`JSON` format `{`

```json
    "BgpPeerId": "bgp-m5eoyp2mwegk8ce9v****",
    "RequestId": "D4B7649A-61BB-4C64-A586-1DFF1EDA6A42"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | Specified value of "regionId" is not supported. | The error message returned because RegionId is set to an invalid value. Check whether the service is available in the specified region. |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the virtual border router (VBR) has reached the upper limit. |
| 400 | QuotaExceeded.Bgp | bgp group count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number has reached the upper limit. |
| 400 | QuotaExceeded.BgpNet work | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the upper limit. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple Express Connect circuits cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified VBR does not exist. Check whether the specified VBR is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Malfor med | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription.Ma lformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.Malf ormed | Specified Bgp Group authkey is not valid. | The error message returned because the authentication key of the BGP group is invalid. |

| Developer Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malform ed | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as the AS number on the Apsara Stack side. |
| 400 | InvalidParams.NotNull | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as the AS number on the Apsara Stack side. |
| 400 | InvalidParams.NotFoun d | instance not found | The error message returned because the specified instance does not exist. |
| 400 | InvalidParams.NotFoun d | vpc instance not found | The error message returned because the specified virtual private cloud (VPC) does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.AlreadyEx ists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.CannotOp erate | invalid status cannot operate | The error message returned because you cannot perform the operation when the specified resource is in the current state. |

#### DescribeBgpPeers

Queries BGP peers in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBgpPeers | The operation that you want to perform. Set the value to DescribeBgpPeers. |
| RegionId | String | Yes | cn-shanghai | The ID of the region to which the BGP group belongs. You can call the DescribeRegions operation to query region IDs. |
| RouterId | String | No | vbr- 2zecmmvg5gvu8i4t e**** | The ID of the router. |
| BgpPeerId | String | No | bgp- 2ze3un0ft1jd1xd**** * | The ID of the BGP peer. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BgpGroupId | String | No | bgpg- 2zev8h2wo414sfh** **** | The ID of the BGP group. |
| IsDefault | Boolean | No | false | Specifies whether the BGP group is the default one. t rue: yes f alse: no |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 1 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BgpPeers | Array of BgpPeer |   | The detailed information about the BGP peer. |
| BgpPeer |   |   |   |
| Name | String | test | The name of the BGP peer. |
| PeerIpAddress | String | 116.62.**. ** | The IP address of the BGP peer. |
| AuthKey | String | ! PWZ2wsq****** | The authentication key of the BGP group. |
| RouterId | String | vbr- 2zecmmvg5gvu8i4te*** *w | The ID of the router. |
| Status | String | active | The state of the BGP peer. Valid values: Pending: pending. Available: available. Modif ying: being modified. Delet ing: being deleted. Delet ed: deleted. |
| BfdMultiHop | Integer | 3 |   |
| BgpGroupId | String | bgp- wz977wcrmb69******* | The ID of the BGP group. |
| BgpPeerId | String | bgp- wz977wcrmb69agdb*** *** | The ID of the BGP peer. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| BgpStatus | String | deleted | The state of the BGP connection. Valid values: creat ing: being created. working: being used. modif ying: being modified. delet ing: being deleted. Delet ed: deleted. |
| Description | String | xxxxxxxxx | The description of the BGP group. |
| EnableBfd | Boolean | true | Indicates whether the Bidirectional Forwarding Detection (BFD) protocol is enabled. |
| Hold | String | 30 | The hold time of the BGP connection. |
| IpVersion | String | IPv4 |   |
| IsFake | String | true | Indicates whether a fake autonomous system (AS) number is used. |
| Keepalive | String | 10 | The hold time of the BGP connection. |
| LocalAsn | String | 45104 | The local AS number. |
| PeerAsn | String | active | The AS number of the BGP peer. |
| RegionId | String | cn-shanghai | The ID of the region to which the BGP group belongs. |
| RouteLimit | String | 99 | Routing limits. |
| TotalCount | Integer | 10 | The number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| RequestId | String | DE77A7F3-3B74-41C0- A5BC-CAFD188C28B6 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeBgpPeers &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBgpPeersResponse>
  <TotalCount>10</TotalCount>
  <BgpPeers>
        <Status>active</Status>
        <Description>xxxxxxxxx</Description>
        <IpVersion>IPv4</IpVersion>
        <PeerIpAddress>116.62. **. **</PeerIpAddress>
        <Keepalive>10</Keepalive>
        <RouterId>vbr-2zecmmvg5gvu8i4te****w</RouterId>
        <PeerAsn>active</PeerAsn>
        <Name>test</Name>
        <BgpPeerId>bgp-wz977wcrmb69agdb******</BgpPeerId>
        <LocalAsn>45104</LocalAsn>
        <BfdMultiHop>3</BfdMultiHop>
        <EnableBfd>true</EnableBfd>
        <BgpStatus>deleted</BgpStatus>
        <IsFake>true</IsFake>
        <AuthKey>! PWZ2wsq******</AuthKey>
        <RouteLimit>99</RouteLimit>
        <RegionId>cn-shanghai</RegionId>
        <Hold>30</Hold>
        <BgpGroupId>bgp-wz977wcrmb69*******</BgpGroupId>
  </BgpPeers>
  <PageSize>2</PageSize>
  <RequestId>DE77A7F3-3B74-41C0-A5BC-CAFD188C28B6</RequestId>
  <PageNumber>1</PageNumber>
</DescribeBgpPeersResponse>
```

`JSON` format `{`

```json
    "TotalCount": 10,
    "BgpPeers": {
        "Status": "active",
        "Description": "xxxxxxxxx",
        "IpVersion": "IPv4",
        "PeerIpAddress": "116.62. **. **",
        "Keepalive": 10,
        "RouterId": "vbr-2zecmmvg5gvu8i4te****w",
        "PeerAsn": "active",
        "Name": "test",
        "BgpPeerId": "bgp-wz977wcrmb69agdb******",
        "LocalAsn": 45104,
        "BfdMultiHop": 3,
        "EnableBfd": true,
        "BgpStatus": "deleted",
        "IsFake": true,
        "AuthKey": "! PWZ2wsq******",
        "RouteLimit": 99,
        "RegionId": "cn-shanghai",
        "Hold": 30,
        "BgpGroupId": "bgp-wz977wcrmb69*******"
```

`},`

```json
    "PageSize": 2,
    "RequestId": "DE77A7F3-3B74-41C0-A5BC-CAFD188C28B6",
    "PageNumber": 1
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because unknown errors occur. |
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |

#### ModifyBgpPeerAttribute

Modifies the configuration of a Border Gateway Protocol (BGP) peer. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBgpPeerAttri bute | The operation that you want to perform. Set the value to Modif yBgpPeerAt t ribut e. |
| BgpPeerId | String | Yes | Bgp- m5eoyp2mwegk8ce 9v**** | The ID of the BGP peer that you want to modify. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the BGP peer. You can call the DescribeRegions operation to query the most recent region list. |
| BgpGroupId | String | No | bgpg- wz9f62v4fbg**** | The ID of the BGP group. |
| PeerIpAddress | String | No | 116.62.XX.XX | The IP address of the BGP peer. |
| EnableBfd | Boolean | No | true | Specifies whether to enable the Bidirectional Forwarding Detection (BFD) feature. Valid values: t rue: enables BFD. f alse: disables BFD. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id of each API request may be different. |
| BfdMultiHop | Integer | No | 3 | The multihop BFD feature. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D4B7649A-61BB-4C64- A586-1DFF1EDA6A42 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyBgpPeerAttribute &BgpPeerId=Bgp-m5eoyp2mwegk8ce9v**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyBgpPeerAttributeResponse>
  <RequestId>D4B7649A-61BB-4C64-A586-1DFF1EDA6A42</RequestId>
</ModifyBgpPeerAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "D4B7649A-61BB-4C64-A586-1DFF1EDA6A42"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### DeleteBgpPeer

Deletes a specific Border Gateway Protocol (BGP) peer. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBgpPeer | The operation that you want to perform. Set the value to Delet eBgpPeer. |
| BgpPeerId | String | Yes | bgp- wz977wcrmb69a*** ***** | The ID of the BGP peer. |
| RegionId | String | Yes | cn-shanghai | The region to which the BGP group belongs. You can call the DescribeRegions operation to query region IDs. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001xxxxxxxx | The client token that is used to ensure the idempotence of the request. The value of this parameter is generated by a client. The value must be unique among different requests and must be 1 to 64 ASCII characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | AEBB1EB6-3C15-4A35- B4CE-03485200C143 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DeleteBgpPeer &BgpPeerId=bgp-wz977wcrmb69a******** &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteBgpPeerResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteBgpPeerResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | Specified value of "regionId" is not supported. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The Network Quality Analyzer (NQA) number exceeds the virtual border router (VBR) quota. |
| 400 | QuotaExceeded.BgpNet work | bgp network count per vbr quota exceed. | The number of BGP networks in the VBR has reached the quota. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The IP addresses of multiple physical connections cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified VBR does not exist. Check whether the parameter is set to a valid value. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Malfor med | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription.Ma lformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.Malf ormed | Specified Bgp Group authkey is not valid. | The error message returned because the verification key of the BGP group is invalid. |

|   | Developer Guid | e·API reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malform ed | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous system (AS) number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotNull | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotFoun d | instance not found | The error message returned because the instance does not exist. |
| 400 | InvalidParams.NotFoun d | vpc instance not found | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.AlreadyEx ists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.CannotOp erate | invalid status cannot operate | The error message returned because the state is invalid and the operation cannot be performed. |

#### AddBgpNetwork

Advertises a Border Gateway Protocol (BGP) network. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddBgpNetwork | The operation that you want to perform. Set the value to AddBgpNet work. |
| DstCidrBlock | String | Yes | 10.10.**. **/32 | The CIDR block of the virtual private cloud (VPC) or vSwitch that you want to connect to a data center. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the virtual border router (VBR) is deployed. You can call the DescribeRegions operation to query region IDs. |
| RouterId | String | Yes | vrt- 2zeo3xzyf38r4u***** * | The ID of the vRouter associated with the router interface. |
| VpcId | String | No | vpc- bp1qpo0kug3a2**** * | The ID of the VPC. |

| Virtual Private Cloud |   |   |   | Developer Guide·API reference |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |

| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
|---|---|---|---|---|

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9C7FA9D6-72E0-48A9- A9C3-2DA8569CD5EB | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=AddBgpNetwork &DstCidrBlock=10.10. **. **/32 &RegionId=cn-shanghai &RouterId=vrt-2zeo3xzyf38r4u****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddBgpNetworkResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</AddBgpNetworkResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the quota. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number exceeds the VBR quota. |

| Developer Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded.BgpNet work | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the quota. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple physical connections cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified vRouter does not exist. Check whether the ID of the VBR is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Malfor med | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription.Ma lformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.Malf ormed | Specified Bgp Group authkey is not valid. | The error message returned because the verification key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malform ed | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous system (AS) number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotNull | parameter must not null. | The error message returned because a required parameter is not set. |
| 400 | InvalidParams.NotFoun d | instance not found | The error message returned because the specified instance does not exist. |
| 400 | InvalidParams.NotFoun d | vpc instance not found | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.AlreadyEx ists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.CannotOp erate | invalid status cannot operate | The error message returned because the state is invalid and the operation cannot be performed. |
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded.Bgp | bgp group count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the quota. |

#### DeleteBgpNetwork

Deletes an advertised Border Gateway Protocol (BGP) network. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBgpNetwork | The operation that you want to perform. Set the value to Delet eBgpNet work. |
| DstCidrBlock | String | Yes | 10.110.192.12/32 | The CIDR block of the virtual private cloud (VPC) or vSwitch that you want to connect to a data center. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the BGP group is deployed. You can call the DescribeRegions operation to query region IDs. |
| RouterId | String | Yes | vrt- bp1lhl0taikrteen80o xx | The ID of the virtual border router (VBR). |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 22F4C006-D3BB-4F96- 9FF9-4C8335276D70 | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=DeleteBgpNetwork &DstCidrBlock=10.110.192.12/32 &RegionId=cn-hangzhou &RouterId=vrt-bp1lhl0taikrteen80oxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteBgpNetworkResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteBgpNetworkResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | Specified value of "regionId" is not supported. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number has exceeded the upper limit. |
| 400 | QuotaExceeded.BgpNet work | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the upper limit. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple physical connections cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified VBR does not exist. Check whether the specified VBR ID is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Malfor med | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription.Ma lformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.Malf ormed | Specified Bgp Group authkey is not valid. | The error message returned because the verification key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |

| Virtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidPeerAsn.Malform ed | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotNull | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotFoun d | instance not found | The error message returned because the instance does not exist. |
| 400 | InvalidParams.NotFoun d | vpc instance not found | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.AlreadyEx ists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.CannotOp erate | invalid status cannot operate | The error message returned because the state is invalid and the operation cannot be performed. |

#### DescribeBgpNetworks

Queries advertised Border Gateway Protocol (BGP) networks. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBgpNetwor ks | The operation that you want to perform. Set the value to DescribeBgpNet works. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the BGP group is deployed. You can call the DescribeRegions operation to query region IDs. |
| RouterId | String | No | vrt- 2zeazning6tb******* * | The ID of the vRouter to which the route table belongs. |
| PageNumber | Integer | No | 2 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BgpNetworks | Array of BgpNetwork |   | BGP networks. |
| BgpNetwork |   |   |   |
| DstCidrBlock | String | 10.1.**. **/24 | The advertised BGP network. |
| RouterId | String | vrt- bp1el837xkkak******** | The ID of the vRouter. |
| Status | String | Enabled | The state of the advertised BGP network. |
| VpcId | String | vpc- bp1qpo0kug3a******** | The ID of the virtual private cloud (VPC). |
| PageNumber | Integer | 2 | The page number of the returned page. |
| PageSize | Integer | 12 | The number of entries returned per page. |
| RequestId | String | 6F513A15-669F-419D- B511-08A85292059B | The ID of the request. |
| TotalCount | Integer | 2 | The total number of advertised BGP networks. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeBgpNetworks &RegionId=cn-hangzhou &RouterId=vrt-2zeazning6tb******** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBgpNetworksResponse>
      <BgpNetworks>
            <BgpNetwork>
                  <DstCidrBlock>192.168. **. **/24</DstCidrBlock>
                  <VpcId></VpcId>
            </BgpNetwork>
      </BgpNetworks>
      <RequestId>6F513A15-669F-419D-B511-08A85292059B</RequestId>
      <PageSize>10</PageSize>
      <TotalCount>1</TotalCount>
</DescribeBgpNetworksResponse>
```

`JSON` format `{`

```json
  "BgpNetworks": {
    "BgpNetwork": [
```

`{`

```json
        "DstCidrBlock": "192.168. **. **/24",
        "VpcId": ""
```

`]` `},`

```json
  "RequestId": "6F513A15-669F-419D-B511-08A85292059B",
  "PageSize": 10,
  "TotalCount": 1
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because unknown errors have occurred. |
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |

### Router interface

#### CreateRouterInterface

Creates a router interface. Usage notes When you call this operation, take note of the following limits: You can create only one pair of interfaces to be connected between two routers. You can create a maximum of five router interfaces for a router. Each destination CIDR block of route entries in the same route table must be unique. A virtual border router (VBR) can serve only as an initiator. The VBR must be in the Activated state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRouterInterfa ce | The operation that you want to perform. Set the value to Creat eRout erInt erf ace. |
| OppositeRegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the acceptor. |
| RegionId | String | Yes | cn-qingdao-env33- d01 | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Role | String | Yes | InitiatingSide | The role of the router interface. Valid values: Init iat ingSide: initiator Accept ingSide: acceptor |
| RouterId | String | Yes | vrt- n3619981j2qdfyhfc* *** | The ID of the router that is associated with the router interface. |
| RouterType | String | Yes | VRouter | The type of the router associated with the router interface. Valid values: VRout er: a vRouter VBR: a VBR |
| Spec | String | Yes | Mini.2 | The specification of the router interface. Valid values: Mini.2: 2 Mbit/s Mini.5: 5 Mbit/s Small.1: 10 Mbit/s Small.2: 20 Mbit/s Small.5: 50 Mbit/s Middle.1: 100 Mbit/s Middle.2: 200 Mbit/s Middle.5: 500 Mbit/s Large.1: 1,000 Mbit/s Large.2: 2,000 Mbit/s Large.5: 5,000 Mbit/s Xlarge.1: 10,000 Mbit/s Not e When Role is set to Accept ingSide (acceptor), Spec is set to Negat ive. |
| OppositeInterfaceId | String | No | ri- 2zeo3xzyf38r4urzd* *** | The ID of the peer router interface. |
| OppositeRouterId | String | No | vrt- bp1lhl0taikrteen8*** * | The ID of the peer router. |
| OppositeRouterType | String | No | VRouter | The type of the router associated with the peer router interface. Valid values: VRout er: a vRouter VBR: a VBR |
| OppositeInterfaceO wnerId | String | No | 2348**** | The ID of the account to which the peer router interface belongs. |

| Virtual Private Cloud |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckSourceIp | String | No | 116.62.XX.XX | The source IP address that is used to perform health checks. The source IP address must be an idle IP address of the local virtual private cloud (VPC). Not e You can set this parameter if an Express Connect circuit is used. |
| HealthCheckTargetIp | String | No | 116.12.XX.XX | The destination IP address that is used to perform health checks. Not e This parameter is required when the Healt hCheckSourceIp parameter is set. |
| AccessPointId | String | No | ap-cn-sha**** | The ID of the access point to which the VBR belongs. You can call the DescribeAccessPoints operation to query the most recent access point list. Not e This parameter is required when the VBR is connected to an Express Connect circuit. |
| OppositeAccessPoin tId | String | No | ap-cn-sha**** | The ID of the access point to which the peer belongs. Not e This parameter is required when the peer router interface is associated with a VBR. The specified value cannot be changed after the router interface is created. |
| Description | String | No | Description | The description of the router interface. The description must be 2 to 255 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| Name | String | No | Name | The name of the router interface. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). _ The name must start with a letter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Period | Integer | No | 3 | The subscription duration. Valid values: Valid values when the PricingCycle parameter is set to Month: 1 t o 9. Valid values when the PricingCycle parameter is set to Year: 1 t o 3. Not e This parameter is required when Inst anceChargeT ype is set to PrePaid. |
| InstanceChargeType | String | No | PrePaid | The billing method of the router interface. Valid values: PrePaid: subscription Post Paid (default): pay-as-you-go |
| AutoPay | Boolean | No | false | Specifies whether to enable auto-renewal for the instance. Valid values: f alse: disables automatic payment. After an order is generated, you must go to the Order Center to complete the payment. t rue: enables automatic payment. Payments are automatically completed. Not e This parameter is required when Inst anceChargeT ype is set to PrePaid. |
| PricingCycle | String | No | Month | The billing cycle of the subscription. Valid values: Mont h (default): monthly subscription Year: annual subscription Not e This parameter is required when Inst anceChargeT ype is set to PrePaid. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id of each API request may be different. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | Long | 202008594930117 | The order number. This parameter is returned when InstanceChargeType is set to PrePaid. |
| RequestId | String | 079874CD-AEC1-43E6- AC03-ADD96B6E4907 | The ID of the request. |
| RouterInterfaceId | String | ri-2ze7fbuohm**** | The ID of the router interface. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateRouterInterface &OppositeRegionId=cn-qingdao-env66-d01 &RegionId=cn-qingdao-env33-d01 &Role=InitiatingSide &RouterId=vrt-123**** &RouterType=VRouter &Spec=Mini.2 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateRouterInterfaceResponse>
  <RequestId>079874CD-AEC1-43E6-AC03-ADD96B6E4907</RequestId>
  <OrderId>202008594930117</OrderId>
  <RouterInterfaceId>ri-2ze7fbuohm****</RouterInterfaceId>
</CreateRouterInterfaceResponse>
```

`JSON` format `{`

```json
    "RequestId": "079874CD-AEC1-43E6-AC03-ADD96B6E4907",
    "OrderId": 202008594930117,
    "RouterInterfaceId": "ri-2ze7fbuohm****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The regionId provided does not exist in our records. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |
| 400 | InvalidRole.ValueNotSu pported | The specified Role is not valid. | The error message returned because Role is set to an invalid value. Check whether the specified value is valid. |
| 400 | InvalidSpec.ValudNotSu pported | The specified Spec is not supported. | The error message returned because the specification does not support this operation. Change the specification and try again. |
| 400 | InvalidRouterType.Value NotSupported | The specified RouterType is not valid. | The error message returned because the type of the router is invalid. |
| 404 | InvalidRouterId.NotFoun d | The specified RouterId does not exist in our recored. | The error message returned because the specified router ID does not exist. |
| 400 | InvalidName.Malformed | The specified "Name" is not valid. | The error message returned because the format of the name is invalid. |
| 400 | InvalidDescription.Malfo rmed | The specifid "Description" is not valid. | The error message returned because the specified description is invalid. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| 400 | Forbidden.BillsOutstand ing | You cannot create more RouterInterface because you have bills outstanding. | The error message returned because the router interface cannot be created when you have unsettled bills. |
| 400 | LimitationExceed.Interfa ceNumberOnRouter | Total number of RouterInterfaces on a Router exceeded. | The error message returned because the number of router interfaces reaches the quota. |
| 400 | Forbidden.NotInRouterI nterfaceCreateWhitelist | Not in router interface create whitelist. | The error message returned because you are not included in the whitelist to create router interfaces. |
| 400 | RI CREATE ONE LIMIT B _ _ _ _ Y SYNC _ | Create ri only one limit by sync. | The error message returned because you can create only one router interface at a time. |
| 400 | InvalidAccessPoint.Valu eNotAllowed | The non-vbr router interface cannot have access point configured. | The error message returned because you cannot configure access points for the router interface of a vRouter. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidAccessPoint.Valu eNotAllowed | The non-vbr opposite router interface cannot have opposite access point configured. | The error message returned because you cannot configure access points for the router interface of a vRouter. |
| 400 | InvalidAccessPoint.Not Match | The accessPoint id is not matched | The error message returned because the specified ID of the access point is invalid. |
| 400 | InvalidAccessPoint.NotE xist | The accessPoint not exit | The error message returned because the access point does not exist. |
| 400 | InvalidRouterType.Value NotSupported | The specified RouterType is not valid | The error message returned because the type of the router is invalid. |

#### ConnectRouterInterface

Initiates a connection from the initiator router interface to the acceptor. After you call this operation, the router interface enters the Connecting state. When the connection is established, it enters the Active state. When you call this operation, take note of the following: Only an initiator router interface in the Idle state can initiate a connection. You can interconnect only a single pair of router interfaces between two routers. You cannot initiate a connection if your account contains a router interface with overdue payments. Request parameters

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConnectRouterInterfac e | The operation that you want to perform. Set the value to ConnectRouterInterface. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterfaceId | String | Yes | ri-2ze7fbuohm**** | The ID of the initiator router interface. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 079874CD-AEC1-43E6- AC03-ADD96B6E4907 | The ID of the request. |

Examples Sample request s

```
https://vpc.example.com/?Action=ConnectRouterInterface &RegionId=cn-hangzhou &RouterInterfaceId=ri-2ze7fbuohm**** &<Common request parameters>
```

Sample responses XML format

```xml
<? xml version="1.0" encoding="UTF-8"? > <ConnectRouterInterfaceResponse>
     <RequestId>079874CD-AEC1-43E6-AC03-ADD96B6E4907</RequestId>
</ConnectRouterInterfaceResponse>
```

JSON format `{`

```json
   "RequestId": "079874CD-AEC1-43E6-AC03-ADD96B6E4907"
```

#### DeactivateRouterInterface

Deactivates a router interface. After you call this operation, the router interface enters the Deactivating state. When the router interface is deactivated, it enters the Inactive state. Not e You cannot deactivate a router interface that has overdue payments. Request parameters

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeactivateRouterInter face | The operation that you want to perform. Set the value to DeactivateRouterInterface. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterfaceId | String | Yes | ri- 2zeo3xzyf38r4urz**** | The ID of the router interface. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | BE7EB53A-99AB-4DA8- AEDE-75FA90D046A6 | The ID of the request. |

Examples Sample request s

```
https://vpc.example.com/?Action=DeactivateRouterInterface &RegionId=cn-hangzhou &RouterInterfaceId=ri-2zeo3xzyf38r4urz**** &<Common request parameters>
```

Sample responses XML format

```xml
<? xml version="1.0" encoding="UTF-8"? > <DeactivateRouterInterfaceResponse>
    <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeactivateRouterInterfaceResponse>
```

JSON format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### ModifyRouterInterfaceSpec

Modifies the specifications of a router interface. After you call this operation, the router interface enters the Activating state. When the router interface is activated, it enters the Active state. Not e You cannot modify the specifications of a router interface that has overdue payments. Request parameters

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyRouterInterface Spec | The operation that you want to perform. Set the value to ModifyRouterInterfaceSpec. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterfaceId | String | Yes | ri- 2zeo3xzyf38r4urzd*** * | The ID of the router interface. |
| Spec | String | Yes | Large | The specifications of the router interface. |
| ClientToken | String | No | 02fb3da4-130e-11e9- 8e44-0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |
| Spec | String | Small.1 | The specifications of the router interface. |

Examples Sample request s

```
https://vpc.example.com/?Action=ModifyRouterInterfaceSpec &RegionId=cn-hangzhou &Spec=Middle.2 &RouterInterfaceId=ri-2zeo3xzyf38r4urzd**** &<Common request parameters>
```

Sample responses XML format

```xml
<? xml version="1.0" encoding="UTF-8"? > <ModifyRouterInterfaceSpecResponse>
     <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
     <Spec>Middle.2</Spec>
</ModifyRouterInterfaceSpecResponse>
```

JSON format `{`

```json
     "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0",
     "Spec":"Middle.2"
```

#### DeleteRouterInterface

Deletes a router interface. When you call this operation, take note of the following: You can only delete a router interface that is in the Idle or Inactive state. Before you delete a router interface, you must delete all custom route entries destined for the router interface. Request parameters

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteRouterInterface | The operation that you want to perform. Set the value to DeleteRouterInterface. |
| RegionId | String | Yes | cn-shanghai | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |

| Virtual Private Clou | d |   |   | Developer Guide·API reference |
|---|---|---|---|---|
| Parameter | Type | Requir ed | Example | Description |
| RouterInterfaceId | String | Yes | ri- 2zeo3xzyf38r4urz**** | The ID of the router interface. |
| ClientToken | String | No | qwefcc12123333334f | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Examples Sample request s

```
https://vpc.example.com/?Action=DeleteRouterInterface &RegionId=cn-shanghai &RouterInterfaceId=ri-2zeo3xzyf38r4urz**** &<Common request parameters>
```

Sample responses XML format

```xml
<? xml version="1.0" encoding="UTF-8"? > <DeleteRouterInterfaceResponse>
     <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteRouterInterfaceResponse>
```

JSON format `{`

```json
   "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### DescribeRouterInterfaces

Queries router interfaces in a specified region. Request parameters

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRouterInterfa ces | The operation that you want to perform. Set the value to DescribeRouterInterfaces. |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the router interfaces that you want to query. You can call the DescribeRegions operation to query the most recent region list. |
| Filter.n.Key | String | No | Filter.1.status | Filter condition n. You can specify a maximum of five filter conditions. Valid values of n: 1 to 5. You can specify multiple values for each filter condition. The values are associated by the OR operator. If a router interface matches at least one of the values, it meets the filter condition. Multiple filter conditions are associated by the AND operator. A router interface is returned only if it meets all the filter conditions. The following filter conditions are available: RouterInterfaceId: the ID of the router interface. RouterId: the ID of the VRouter or VBR associated with the router interface. RouterType: the type of the router associated with the router interface. Valid values: VRouter and VBR. RouterInterfaceOwnerId: the account ID of the router interface. OppositeInterfaceId: the ID of the peer router interface. OppositeRouterType: the type of the router associated with the peer router interface. Valid values: VRouter and VBR. OppositeRouterId: the ID of the VRouter or VBR associated with the peer router interface. OppositeInterfaceOwnerId: the account ID of the peer router interface. Status: the status of the router interface. Name: the name of the router interface. |
| Filter.n.Value.m | String | No | Filter.1.Active | Value m of filter condition n. Valid values of m: 1 to 5. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C7F6FCBD-F9CC-4501- 8EF3-CDC9577CAE45 | The ID of the request. |
| TotalCount | String | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| RouterInterfaceSet | List |   | Details about the router interface. For more information, see the RouterInterfaceType list. |

RouterInterfaceType list

| Parameter | Type | Example | Description |
|---|---|---|---|
| RouterType | String | VRouter | The type of the router to which the route table belongs. Valid values: VRouter VBR |
| RouterInterfaceId | String | ri- 2zenfgfpyu3v93koa**** | The ID of the router interface. |
| RouterId | String | vrt- bp1d3bxtdv68tfd7g**** | The ID of the router to which the route table belongs. |
| Spec | String | Large | The specifications of the router interface. |
| Role | String | InitiatingSide | Indicates whether the router interface is the connection initiator or connection acceptor. |
| CreationTime | String | 2017-06-08T12:20:55 | The time when the router interface was created. |
| OppositeInterfaceO wnerId | String | 123157908552**** | The account ID of the owner of the peer router interface. |
| OppositeRouterTyp e | String | VRouter | The type of the router associated with the peer router interface. |
| OppositeRouterId | String | vrt- bp1d3bxtdv68tfd7g**** | The ID of the router associated with the peer router interface. |
| OppositeInterfaceI d | String | ri- bp12dxgw8gmoma1h*** * | The ID of the peer router interface. |
| VpcInstanceId | String | vpc- 2ze3tq4uxhysg717x**** | The ID of the local VPC for the peering connection. |
| Status | String | active | The status of the router interface. |

Examples Sample request s

```
https://vpc.example.com/?Action=DescribeRouterInterfaces &RegionId=cn-beijing &<Common request parameters>
```

Sample responses XML format

```xml
<? xml version="1.0" encoding="UTF-8" ? > <DescribeRouterInterfacesResponse>
    <PageNumber>1</PageNumber>
    <TotalCount>2</TotalCount>
    <PageSize>10</PageSize>
    <RequestId>FC2B35C9-15C5-4972-94B7-F529A1620AE0</RequestId>
    <RouterInterfaceSet>
        <RouterInterfaceType>
            <ChargeType>AfterPay</ChargeType>
            <OppositeInterfaceBusinessStatus>Normal</OppositeInterfaceBusinessStatus>
            <RouterInterfaceId>ri-2zepoga55p33dxxxxxxxx</RouterInterfaceId>
            <OppositeInterfaceStatus>Active</OppositeInterfaceStatus>
            <Spec>Small.1</Spec>
            <OppositeInterfaceOwnerId>12315790xxxxxxxx</OppositeInterfaceOwnerId>
            <OppositeInterfaceSpec>Negative</OppositeInterfaceSpec>
            <CreationTime>2018-04-19T07:35:00Z</CreationTime>
            <RouterType>VRouter</RouterType>
            <Status>Active</Status>
            <OppositeRouterType>VRouter</OppositeRouterType>
            <OppositeRouterId>vrt-m5ey5a8d65bmxxxxxxxx</OppositeRouterId>
            <OppositeInterfaceId>ri-m5eo6ht5pu2fxxxxxxxxx</OppositeInterfaceId>
            <VpcInstanceId>vpc-2zeugdd0wut2rhxxxxxxxx</VpcInstanceId>
            <RouterId>vrt-2zefso23vmu6xxxxxxxxx</RouterId>
            <ConnectedTime>2018-04-19T07:35:07Z</ConnectedTime>
            <OppositeRegionId>cn-qingdao</OppositeRegionId>
            <BusinessStatus>Normal</BusinessStatus>
            <Role>InitiatingSide</Role>
            <OppositeVpcInstanceId>vpc-m5ep989i7ocrtnxxxxxxxx</OppositeVpcInstanceId>
            <EndTime>2999-09-08T16:00:00Z</EndTime>
        </RouterInterfaceType>
        <RouterInterfaceType>
            <ChargeType>Prepaid</ChargeType>
            <OppositeInterfaceBusinessStatus>Normal</OppositeInterfaceBusinessStatus>
            <RouterInterfaceId>ri-2zegbp7nhj0mxxxxxxxx</RouterInterfaceId>
            <OppositeInterfaceStatus>Deleted</OppositeInterfaceStatus>
            <Spec>Small.1</Spec>
            <OppositeInterfaceOwnerId>1231579085529123</OppositeInterfaceOwnerId>
            <OppositeInterfaceSpec>Negative</OppositeInterfaceSpec>
            <CreationTime>2017-12-27T06:31:30Z</CreationTime>
            <RouterType>VRouter</RouterType>
            <Status>Inactive</Status>
            <OppositeRouterType>VRouter</OppositeRouterType>
            <OppositeRouterId>vrt-bp1d3bxtdv68txxxxxxxx</OppositeRouterId>
            <OppositeInterfaceId>ri-bp12dxgw8gmoxxxxxxxx</OppositeInterfaceId>
            <VpcInstanceId>vpc-2ze3tq4uxhysg7xxxxxxxx</VpcInstanceId>
            <RouterId>vrt-2zeazning6tbzkxxxxxxxx</RouterId>
            <ConnectedTime>2017-12-27T06:31:36Z</ConnectedTime>
            <OppositeRegionId>cn-hangzhou</OppositeRegionId>
            <BusinessStatus>Normal</BusinessStatus>
            <Role>InitiatingSide</Role>
            <OppositeVpcInstanceId>vpc-bp15k6sx6fhdzxxxxxxxx</OppositeVpcInstanceId>
            <EndTime>2018-07-27T16:00:00Z</EndTime>
        </RouterInterfaceType>
    </RouterInterfaceSet>
</DescribeRouterInterfacesResponse>
```

JSON format `{`

```json
    "PageNumber": 1,
    "TotalCount": 2,
    "PageSize": 10,
    "RequestId": "FC2B35C9-15C5-4972-94B7-F529A1620AE0",
    "RouterInterfaceSet": {
        "RouterInterfaceType": [
```

`{`

```json
                "ChargeType": "AfterPay",
                "OppositeInterfaceBusinessStatus": "Normal",
                "RouterInterfaceId": "ri-2zepoga55p33djxxxxxxxx",
                "OppositeInterfaceStatus": "Active",
                "Spec": "Small.1",
                "OppositeInterfaceOwnerId": "123157908xxxxxxxx",
                "OppositeInterfaceSpec": "Negative",
                "CreationTime": "2018-04-19T07:35:00Z",
                "RouterType": "VRouter",
                "Status": "Active",
                "OppositeRouterType": "VRouter",
                "OppositeRouterId": "vrt-m5ey5a8d65bmauxxxxxxxx",
                "OppositeInterfaceId": "ri-m5eo6ht5pu2fxxxxxxxxx",
                "VpcInstanceId": "vpc-2zeugdd0wut2rhxxxxxxxx",
                "RouterId": "vrt-2zefso23vmu6xi3xxxxxxxx",
                "ConnectedTime": "2018-04-19T07:35:07Z",
                "OppositeRegionId": "cn-qingdao",
                "BusinessStatus": "Normal",
                "Role": "InitiatingSide",
                "OppositeVpcInstanceId": "vpc-m5ep989i7ocrxxxxxxxx",
                "EndTime": "2999-09-08T16:00:00Z"
```

`},` `{`

```json
                "ChargeType": "Prepaid",
                "OppositeInterfaceBusinessStatus": "Normal",
                "RouterInterfaceId": "ri-2zegbp7nhj0mnxxxxxxxx",
                "OppositeInterfaceStatus": "Deleted",
                "Spec": "Small.1",
                "OppositeInterfaceOwnerId": "1231579085xxxxxxxx",
                "OppositeInterfaceSpec": "Negative",
                "CreationTime": "2017-12-27T06:31:30Z",
                "RouterType": "VRouter",
                "Status": "Inactive",
                "OppositeRouterType": "VRouter",
                "OppositeRouterId": "vrt-bp1d3bxtdv68xxxxxxxx",
                "OppositeInterfaceId": "ri-bp12dxgw8gmomxxxxxxxx",
                "VpcInstanceId": "vpc-2ze3tq4uxhysgxxxxxxxx",
                "RouterId": "vrt-2zeazning6tbzkxxxxxxxx",
                "ConnectedTime": "2017-12-27T06:31:36Z",
                "OppositeRegionId": "cn-hangzhou",
                "BusinessStatus": "Normal",
                "Role": "InitiatingSide",
                "OppositeVpcInstanceId": "vpc-bp15k6sx6fhdzxxxxxxxx",
                "EndTime": "2018-07-27T16:00:00Z"
```

`]`

#### ActivateRouterInterface

Activates a router interface that is in the Inactive state. After you call this operation, the router interface enters the Activating state. When the router interface is activated, it enters the Active state. Not e You cannot activate a router interface that has overdue payments. Request parameters

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ActivateRouterInterfac e | The operation that you want to perform. Set the value to ActivateRouterInterface. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterfaceId | String | Yes | ri- 2zeo3xzyf38r4urz**** | The ID of the router interface. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 079874CD-AEC1-43E6- AC03-ADD96B6E4907 | The ID of the request. |

Examples Sample request s

```
https://vpc.example.com/?Action=ActivateRouterInterface &RegionId=cn-hangzhou &RouterInterfaceId=ri-2zeo3xzyf38r4urz**** &<Common request parameters>
```

Sample responses XML format

```xml
<? xml version="1.0" encoding="UTF-8"? > <ActivateRouterInterfaceResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
 </ActivateRouterInterfaceResponse>
```

JSON format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### ModifyRouterInterfaceAttribute

Modifies the configuration of a router interface. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyRouterInterfa ceAttribute | The operation that you want to perform. Set the value to Modif yRout erInt erf aceAt t ribut e. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterfaceId | String | Yes | ri- 2zeo3xzyf38r4urz*** * | The ID of the router interface. |
| Name | String | No | test | The name of the router interface. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter. It cannot start with http:// or https:// . |
| Description | String | No | Router interface | The description of the router interface. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| OppositeInterfaceId | String | No | ri- 2zeo3xzyf38r4urz*** * | The ID of the peer router interface. |
| OppositeRouterId | String | No | vrt- bp1jcg5cmxjbl9xgc* *** | The ID of the peer router. |
| OppositeRouterType | String | No | VRouter | The type of the router to which the peer router interface belongs. VRout er VBR (default) |
| OppositeInterfaceO wnerId | Long | No | 10 | The ID of the Apsara Stack tenant account to which the peer router interface belongs. |
| HealthCheckSourceIp | String | No | 116.62.XX.XX | The source IP address that is used to perform health checks. The source IP address must be an idle IP address of the local VPC. Not e You can set this parameter when an Express Connect circuit is used. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckTargetIp | String | No | 116.62.XX.XX | The destination IP address that is used to perform health checks. Not e This parameter is required when the Healt hCheckSourceIp parameter is specified. |
| HcThreshold | Integer | No | 12 | The number of consecutive health check successes before a backend server is declared as healthy. |
| HcRate | Integer | No | 2 | The rate of heath checks. |
| DeleteHealthCheckIp | Boolean | No | true | Specifies whether to delete the IP addresses for health checks configured on the router interface. t rue: yes f alse (default): no |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyRouterInterfaceAttribute &RegionId=cn-qingdao-env66-d01 &RouterInterfaceId=ri-2zeo3xzyf38r4urz**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyRouterInterfaceAttributeResponse>
      <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
</ModifyRouterInterfaceAttributeResponse>
```

`JSON` format `{`

```json
    "ModifyRouterInterfaceAttributeResponse": {
        "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidRouterInterfaceId .NotFound | The specified RouterInterfaceId does not exist in our records. | The error message returned because the specified router interface does not exist. Check whether the specified router interface is valid. |
| 400 | Forbidden.FinancileLock ed | This RouterInterface is financiel locked because of bills outstanding. | The error message returned because the router interface is locked due to overdue payments. |
| 400 | InvalidName.Malformd | The attribute name is illeagl. | The error message returned because the format of the name is invalid. |
| 400 | InvalidOppositeRouterT ype.ValueNotSupporte d | The specified OppositeRouterType is not valid. | The error message returned because OppositeRouterType is set to an invalid value. |
| 400 | InvalidDescription.Malfo rmed | The Description is illeagl. | The error message returned because the format of the resource description is invalid. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| 400 | Forbbiden | The Router instance owener error | The error message returned because the specified router does not belong to your Apsara Stack tenant account. |
| 400 | LinkRole.NotSupport | This linkrole is not supported | The error message returned because this link is not supported. |
| 400 | InvalidParam.ModifyRou terInterface | Modify routerinterface param invalide | The error message returned because the value of the parameter that you set to modify the router interface is invalid. |

### VPN gateways

#### VPN gateway

##### CreateVpnGateway

Creates a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnGateway | The operation that you want to perform. Set the value to: Creat eVpnGat eway. |

| Virtual Private Cloud |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | Yes | 5 | The public bandwidth of the VPN gateway. Unit: Mbit/s. Valid values: 5, 10, 20, 50, and 100. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where you want to create the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- bp1ub1yt9cvakoelj** ** | The ID of the virtual private cloud (VPC) where the VPN gateway is deployed. |
| EnableIpsec | Boolean | No | true | Specifies whether to enable the IPsec-VPN feature. Valid values: t rue: enables the IPsec-VPN feature. f alse: disables the IPsec-VPN feature. This is the default value. |
| EnableSsl | Boolean | No | true | Specifies whether to enable the SSL-VPN feature. Valid values: t rue: enables the SSL-VPN feature. f alse: disables the SSL-VPN feature. This is the default value. |
| Name | String | No | MYVPN | The name of the VPN gateway. The default value is the ID of the VPN gateway. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter, and cannot start with http:// or https:// . |
| SslConnections | Integer | No | 5 | The maximum number of concurrent connections. Valid values: 5, 10, and 20. |
| VSwitchId | String | No | vsw- bp1j5miw2bae9s2vt **** | The ID of the vSwitch to which the VPN gateway belongs. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | myVpn | The name of the VPN gateway. |
| RequestId | String | 54B48E3D-DF70-471B- AA93-08E683A1B457 | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2ogj*** * | The ID of the VPN gateway. |

Examples Sample requests

```
http(s)://vpc.example.com/?Action=CreateVpnGateway &Bandwidth=5 &RegionId=cn-qingdao-env66-d01 &VpcId=vp c-bp1ub1yt9cvakoelj**** &
```

Sample success responses `XML` format

```xml
<CreateVpnGatewayResponse>
      <Name>myVpn</Name>
      <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
      <RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457</RequestId>
</CreateVpnGatewayResponse>
```

`JSON` format

```json
{ "CreateVpnGatewayResponse":{ "Name":"myVpn", "VpnGatewayId":"vpn-bp1q8bgx4xnkm2ogj****", "RequestId":" 54B48E3D-DF70-471B-AA93-08E683A1B457" } }
```

##### DescribeVpnGateways

Queries VPN gateways. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnGatewa ys | The operation that you want to perform. Set the value to DescribeVpnGat eways. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the VPN gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | No | vpc- bp1ub1yt9cvakoelj** ** | The ID of the virtual private cloud (VPC) to which the VPN gateway belongs. |
| VpnGatewayId | String | No | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Status | String | No | init | The status of the VPN gateway. Valid values: init : The VPN gateway is being initialized. provisioning : The VPN gateway is being prepared. act ive: The VPN gateway is running as expected. updat ing: The VPN gateway is being updated. Delet ing: The VPN gateway is being deleted. |
| BusinessStatus | String | No | Normal | The payment status of the VPN gateway. Valid values: Normal: The VPN gateway does not have overdue payments and is running as expected. FinancialLocked: The VPN gateway is locked due to overdue payments. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGateways | Array of VpnGateway |   | Detailed information about the VPN gateways. |
| VpnGateway |   |   |   |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2ogj*** * | The ID of the VPN gateway. |
| VpcId | String | vpc- bp1ub1yt9cvakoelj**** | The ID of the VPC to which the VPN gateway belongs. |
| VSwitchId | String | vsw- bp1y9ovl1cu9ou4tv**** | The ID of the vSwitch to which the VPN gateway belongs. |
| InternetIp | String | 116.XX.XX.69 | The public IP address of the VPN gateway. |
| CreateTime | Long | 1515383700000 | The timestamp generated when the VPN gateway was created. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| EndTime | Long | 1518105600000 | The timestamp to be generated when the VPN gateway expires. |
| Spec | String | 5 Mbps | The bandwidth limit of the VPN gateway. |
| Name | String | test | The name of the VPN gateway. |
| Description | String | test | The description of the VPN gateway. |
| Status | String | active | The status of the VPN gateway. |
| BusinessStatus | String | Normal | The payment status of the VPN gateway. |
| ChargeType | String | Prepay | The billing method of the VPN gateway. Valid value: Post payByFlow. |
| IpsecVpn | String | enable | Indicates whether the IPsec-VPN feature is enabled. Valid values: enable: enabled disable: disabled |
| SslMaxConnection s | Long | 5 | The maximum number of concurrent SSL-VPN connections. |
| SslVpn | String | enable | Indicates whether the SSL-VPN feature is enabled. Valid values: enable: enabled disable: disabled |
| Tag | String | 1 | The tag of the VPN gateway. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | DF11D6F6-E35A-41C3- 9B20-6FC8A901FE65 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpnGateways &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpnGatewaysResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <VpnGateways>
            <VpnGateway>
                  <Status>active</Status>
                  <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
                  <BusinessStatus>Normal</BusinessStatus>
                  <Spec>5M</Spec>
                  <CreateTime>1492753580000</CreateTime>
                  <InternetIp>116.XX.XX.69</InternetIp>
                  <EndTime>1495382400000</EndTime>
                  <VSwitchId>vsw-bp1y9ovl1cu9ou4tv****</VSwitchId>
                  <VpcId>vpc-bp1ub1yt9cvakoelj****</VpcId>
            </VpnGateway>
      </VpnGateways>
      <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId>
</DescribeVpnGatewaysResponse>
```

`JSON` format `{`

```json
    "PageNumber": 1,
    "TotalCount": 1,
    "VpnGateways": {
        "VpnGateway": [
```

`{`

```json
                "Status": "active",
                "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
                "BusinessStatus": "Normal",
                "Spec": "5M",
                "CreateTime": 1492753580000,
                "InternetIp": "116.XX.XX.69",
                "EndTime": 1495382400000,
                "VSwitchId": "vsw-bp1y9ovl1cu9ou4tv****",
                "VpcId": "vpc-bp1ub1yt9cvakoelj****"
```

`]` `},`

```json
    "PageSize": 10,
    "RequestId": "B2CD1315-CA2B-47B1-9DA5-8F1D69C48E82"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. Apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. To acquire the required permissions, submit a ticket. |

##### DescribeVpnGateway

Queries the details of a specified VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnGatewa y | The operation that you want to perform. Set the value to DescribeVpnGat eway. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the VPN gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2ogj*** * | The ID of the VPN gateway. |
| VpcId | String | vpc- bp1ub1yt9cvakoelj**** | The ID of the VPC for which the VPN gateway is created. |
| VSwitchId | String | vsw- bp1y9ovl1cu9ou4tv**** | The ID of the vSwitch to which the VPN gateway is attached. |
| InternetIp | String | 116.XX.XX.222 | The public IP address of the VPN gateway. |
| CreateTime | Long | 1495382400000 | The timestamp generated when the VPN gateway was created. |

| Virtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| EndTime | Long | 1495382400000 | The timestamp to be generated when the VPN gateway expires. |
| Spec | String | 5 M | The maximum bandwidth of the VPN gateway. Unit: Mbit/s. |
| Name | String | vpngatewayname | The name of the VPN gateway. |
| Description | String | vpngatewaydescription | The description of the VPN gateway. |
| Status | String | init | The status of the VPN gateway. init : The VPN gateway is being initialized. provisioning : The VPN gateway is being prepared. act ive: The VPN gateway is running as expected. updat ing: The VPN gateway is being updated. Delet ing: The VPN gateway is being deleted. |
| BusinessStatus | String | Normal | The payment status of the VPN gateway. Normal: The VPN gateway is running as expected. FinancialLocked: The VPN gateway is locked due to overdue payments. |
| ChargeType | String | PostpayByFlow | The billing method of the VPN gateway. Valid value: Post payByFlow. |
| IpsecVpn | String | enable | Indicates whether the IPsec-VPN feature is enabled. enable: IPsec-VPN is enabled. disable : IPsec-VPN is disabled. |
| RequestId | String | E98A9651-7098-40C7- 8F85-C818D1EBBA85 | The ID of the request. |
| SslMaxConnection s | Long | 5 | The maximum number of concurrent SSL-VPN connections. |
| SslVpn | String | enable | Indicates whether the SSL-VPN feature is enabled. enable: SSL-VPN is enabled. disable : SSL-VPN is disabled. |
| Tag | String | tag1 | The tag of the VPN gateway. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpnGateway &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpnGatewayResponse>
      <Status>active</Status>
      <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
      <Spec>5M</Spec>
      <BusinessStatus>Normal</BusinessStatus>
      <RequestId>E98A9651-7098-40C7-8F85-C818D1EBBA85</RequestId>
      <CreateTime>1492753580000</CreateTime>
      <InternetIp>116.XX.XX.222</InternetIp>
      <EndTime>1495382400000</EndTime>
      <VSwitchId>vsw-bp1y9ovl1cu9ou4tv****</VSwitchId>
      <VpcId>vpc-bp1ub1yt9cvakoelj****</VpcId>
</DescribeVpnGatewayResponse>
```

`JSON` format `{`

```json
    "Status": "active",
    "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
    "BusinessStatus": "Normal",
    "Spec": "5M",
    "CreateTime": 1492753580000,
    "RequestId": "E98A9651-7098-40C7-8F85-C818D1EBBA85",
    "InternetIp": "116.XX.XX.222",
    "EndTime": 1495382400000,
    "VSwitchId": "vsw-bp1y9ovl1cu9ou4tv****",
    "VpcId": "vpc-bp1ub1yt9cvakoelj****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidVpnGatewayInsta nceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |

##### DeleteVpnGateway

Deletes a specified VPN gateway. Not e You cannot delete a VPN gateway that is associated with an IPsec-VPN connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnGateway | The operation that you want to perform. Set the value to Delet eVpnGat eway. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the VPN gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVpnGateway &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteNatGatewayResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteNatGatewayResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidVpnGatewayInsta nceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |
| 403 | ForbiddenRelease | Forbidden to release a prepaid instance within validity period | The error message returned because you cannot release a subscription VPN gateway within the subscription duration. |
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.Configurin g | The specified VPN gateway is being configured. | The error message returned because the VPN gateway is being configured. |

##### ModifyVpnGatewayAttribute

Modifies the name and description of a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnGateway Attribute | The operation that you want to perform. Set the value to Modif yVpnGat ewayAt t ribut e. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the VPN gateway is created. You can call the DescribeRegions operation to query the most recent region list. |

|   | Virtual Private Cloud |   |   |   | Developer Guide·API reference |   |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | vpngateway | The description of the VPN gateway. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . |
| Name | String | No | myvpn | The name of the VPN gateway. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter, and cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2ogj*** * | The ID of the VPN gateway. |
| VpcId | String | vpc- bp1ub1yt9cvakoel**** | The ID of the virtual private cloud (VPC) to which the VPN gateway belongs. |
| VSwitchId | String | vsw- bp1y9ovl1cu9ou4tv**** | The ID of the vSwitch to which the VPN gateway belongs. |
| InternetIp | String | 116.XX.XX.69 | The public IP address of the VPN gateway. |
| CreateTime | Long | 1492753580000 | The timestamp generated when the VPN gateway was created. |
| EndTime | Long | 1495382400000 | The timestamp to be generated when the VPN gateway expires. |
| Spec | String | 5 Mbps | The specification of the VPN gateway. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | test | The name of the VPN gateway. |
| Description | String | test | The description of the VPN gateway. |
| Status | String | active | The status of the VPN gateway. |
| IntranetIp | String | 172.XX.XX.104 | The private IP address of the VPN gateway. |
| RequestId | String | 54B48E3D-DF70-471B- AA93-08E683A1B457 | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=ModifyVpnGatewayAttribute &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj****
```

`&<`公共请求参数`>` Sample success responses `XML` format

```xml
<ModifyVpnGatewayAttributeResponse>
      <Name>aaa</Name>
      <Status>active</Status>
      <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
      <Spec>5M</Spec>
      <CreateTime>1492753580000</CreateTime>
      <IntranetIp>172.XX.XX.104</IntranetIp>
      <RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457</RequestId>
      <InternetIp>116.XX.XX.69</InternetIp>
      <EndTime>1495382400000</EndTime>
      <VSwitchId>vsw-bp1y9ovl1cu9ou4tv****</VSwitchId>
      <VpcId>vpc-bp1ub1yt9cvakoelj****</VpcId>
</ModifyVpnGatewayAttributeResponse>
```

`JSON` format `{`

```json
 "Name":"aaa",
 "Status":"active",
 "VpnGatewayId":"vpn-bp1q8bgx4xnkm2ogj****",
 "Spec":"5M",
 "RequestId":"BA56EAF8-E3A9-4BE6-8511-8F03512153E2",
 "IntranetIp":"172.XX.XX.104",
 "CreateTime":1492753580000,
 "InternetIp":"116.XX.XX.69",
 "EndTime":1495382400000,
 "VSwitchId":"vsw-bp1y9ovl1cu9ou4tv****",
 "VpcId":"vpc-bp1ub1yt9cvakoelj****"
```

#### Customer gateway

##### CreateCustomerGateway

Creates a customer gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateCustomerGat eway | The operation that you want to perform. Set the value to Creat eCust omerGat eway. |
| IpAddress | String | Yes | 116.XX.XX.222 | The IP address of the customer gateway. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where you want to create the customer gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | Gateway | The name of the customer gateway. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter. However, the name cannot start with http:// or https:// . |
| Description | String | No | Gateway | The description of the customer gateway. The description must be 2 to 256 characters in length, and contain digits, hyphens (-), underscores ( ), full width periods (。), full _ width commas (，), and full width colons (：). The description cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGateway Id | String | cgw- bp1aw0a5nfff03xp1*** * | The ID of the customer gateway. |
| IpAddress | String | 100.XX.XX.1 | The IP address of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| CreateTime | Long | 1493363486000 | The timestamp generated when the customer gateway was created. |
| RequestId | String | cgw- bp1aw0a5nfff03xp1pc qc | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateCustomerGateway &IpAddress=116.XX.XX.222 &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateCustomerGatewayResponse>
      <CustomerGatewayId>cgw-bp1aw0a5nfff03xp****</CustomerGatewayId>
      <RequestId>185E81B1-3916-4667-B48F-C52409B33F2B</RequestId>
      <CreateTime>1493363486000</CreateTime>
      <IpAddress>100.XX.XX.1</IpAddress>
</CreateCustomerGatewayResponse>
```

`JSON` format `{`

```json
    "CustomerGatewayId": "cgw-bp1jrawp82av6bws9****",
    "CreateTime": 1493363599000,
    "RequestId": "D32B3C26-6C6C-4988-93E9-D2A6444CE6AE",
    "IpAddress": "100.XX.XX.1"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | InvalidIpAddress.Alread yExist | Specified IpAddress is already exist. | The error message returned because the specified IP address already exists. The IP addresses must be unique in the same region. |
| 400 | InvalidIpAddress.Wrong Format | Specified IpAddress is invalid. | The error message returned because the specified IP address is invalid. |
| 400 | InvalidName | The name is not valid | The error message returned because the specified name is in an invalid format. |
| 400 | InvalidDescription | The description is not valid | The error message returned because the description format of the specified parameter is invalid. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |

##### DescribeCustomerGateways

Queries customer gateways in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCustomerGa teways | The operation that you want to perform. Set the value to DescribeCust omerGat eways. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the customer gateway. You can call the DescribeRegions operation to query the most recent region list. |
| CustomerGatewayId | String | No | vpn- bp1q8bgx4xnkm2og j**** | The ID of the customer gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the returned page. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGateway s | Array of CustomerGateway |   | The details about the customer gateways. |
| CustomerGateway |   |   |   |
| CustomerGateway Id | String | cgw- bp1pvpl9r9adju6l5**** | The ID of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| IpAddress | String | 139.XX.XX.55 | The IP address of the customer gateway. |
| CreateTime | Long | 1492747187000 | The timestamp generated when the customer gateway was created. |
| TotalCount | Integer | 1 | The number of returned entries. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCustomerGateways &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeCustomerGatewaysResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
      <CustomerGateways>
            <CustomerGateway>
                  <Name>test</Name>
                  <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId>
                  <CreateTime>1492747187000</CreateTime>
                  <IpAddress>139.XX.XX.55</IpAddress>
            </CustomerGateway>
      </CustomerGateways>
</DescribeCustomerGatewaysResponse>
```

`JSON` format `{`

```json
    "PageNumber": 1,
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "E82612A9-CB90-4D7E-B394-1DB7F6509B29",
    "CustomerGateways": {
        "CustomerGateway": [
```

`{`

```json
                "Name": "test",
                "CustomerGatewayId": "cgw-bp1pvpl9r9adju6l5****",
                "CreateTime": 1492747187000,
                "IpAddress": "139.XX.XX.55"
```

`]` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are not authorized to perform this operation on the specified resource. Apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. Submit a ticket to obtain the required permissions. |

##### DescribeCustomerGateway

Queries details of a specified customer gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCustomerGa teway | The operation that you want to perform. Set the value to DescribeCust omerGat eway. |
| CustomerGatewayId | String | Yes | vpn- bp1q8bgx4xnkm2og j**** | The ID of the customer gateway. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the customer gateway is created. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGateway Id | String | cgw- bp1pvpl9r9adju6l5**** | The ID of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| IpAddress | String | 139.XX.XX.32 | The IP address of the customer gateway. |
| RequestId | String | 99506ECB-218F-45A5- AE8E-79518451F615 | The ID of the request. |
| CreateTime | Long | 1492747187000 | The timestamp generated when the customer gateway was created. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCustomerGateway &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeCustomerGatewayResponse>
      <Name>test</Name>
      <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId>
      <CreateTime>1492747187000</CreateTime>
      <RequestId>99506ECB-218F-45A5-AE8E-79518451F615</RequestId>
      <IpAddress>139.XX.XX.32</IpAddress>
</DescribeCustomerGatewayResponse>
```

`JSON` format `{`

```json
    "CustomerGatewayId": "cgw-bp1pvpl9r9adju6l5****",
    "Name": "test",
    "RequestId": "A0457BC9-6C0F-4437-AB9D-FB2EABC1D6A2",
    "CreateTime": 1492747187000,
    "IpAddress": "139.XX.XX.32"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidCustomerGatewa yInstanceId.NotFound | The specified customer gateway instance id does not exist. | The error message returned because the specified instance ID does not exist. |

##### DeleteCustomerGateway

Deletes a specified customer gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteCustomerGat eway | The operation that you want to perform. Set the value to Delet eCust omerGat eway. |
| CustomerGatewayId | String | Yes | cgw- 2zllmw9lqrcdis3bd* *** | The ID of the customer gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the customer gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D-48FE- 8316-ACA81BB230DA | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteCustomerGateway &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteCustomerGatewayResesponse>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteCustomerGatewayResesponse>
```

`JSON` format `{`

```json
  "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |

|   | Virtual Private | Cloud |   | Developer Guide·API reference |   |
|---|---|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidCustomerGatewa yInstanceId.NotFound | The specified customer gateway instance id does not exist. | The error message returned because the specified instance ID does not exist. |

##### ModifyCustomerGatewayAttribute

Modifies the name and description of a customer gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyCustomerGat ewayAttribute | The operation that you want to perform. Set the value to Modif yCust omerGat ewayAt t ribut e. |
| CustomerGatewayId | String | Yes | vpn- bp1q8bgx4xnkm2og j**** | The ID of the customer gateway. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the customer gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | test | The name of the customer gateway. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). _ The name must start with a letter. It cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | test | The description of the customer gateway. The description must be 2 to 256 characters in length and can contain digits, hyphens (-), underscores ( ), periods (.), commas (,), and _ colons (:). The description must start with a letter, and cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGateway Id | String | cgw- bp1pvpl9r9adju6l5**** | The ID of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| IpAddress | String | 139.XX.XX.55 | The IP address of the customer gateway. |
| CreateTime | Long | 1492747187000 | The timestamp generated when the customer gateway was created. |
| RequestId | String | E61293C8-AF07-4E87- A272-542680038F93 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyCustomerGatewayAttribute &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyCustomerGatewayAttributeResponse>
      <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId>
      <RequestId>E61293C8-AF07-4E87-A272-542680038F93</RequestId>
      <CreateTime>1492747187000</CreateTime>
      <IpAddress>139.XX.XX.55</IpAddress>
      <Description>modify</Description>
</ModifyCustomerGatewayAttributeResponse>
```

`JSON` format `{`

```json
    "CustomerGatewayId": "cgw-bp1pvpl9r9adju6l5****",
    "RequestId": "8AA5CE21-2E6A-4530-BDF5-F055849476E6",
    "CreateTime": 1492747187000,
    "IpAddress": "139.XX.XX.55",
    "Description": "modify"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. Apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidCustomerGatewa yInstanceId.NotFound | The specified customer gateway instance id does not exist. | The error message returned because the specified instance ID does not exist. |
| 400 | InvalidName | The name is not valid | The error message returned because the format of the name is invalid. |
| 400 | InvalidDescription | The description is not valid | The error message returned because the format of the description is invalid. |

#### Routes for VPN gateways

##### DeleteVpnPbrRouteEntry

Deletes a policy-based route from a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnPbrRouteE ntry | The operation that you want to perform. Set the value to Delet eVpnPbrRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66rmd **** | The next hop of the policy-based route. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the policy-based route is created. You can call the DescribeRegions operation to query the most recent region list. |

| Developer Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the policy- based route. |
| RouteSource | String | Yes | 192.168.1.0/24 | The source CIDR block of the policy-based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx*** * | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The weight of the policy-based route. Valid values: 0: specifies a low priority for the route. 100: specifies a high priority for the route entry. Not e If two policy-based route entries are configured with the same destination CIDR block, you cannot set the weights of both route entries to 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The overlay mode. Set the value to Ipsec (IPsec tunneling). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVpnPbrRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVpnPbrRouteEntryResponse>
      <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</DeleteVpnPbrRouteEntryResponse>
```

`JSON` format `{`

```json
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 404 | InvalidVpnGatewayInsta nceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.FinancialLo cked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

##### DeleteVpnRouteEntry

Deletes a destination-based route from a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnRouteEntr y | The operation that you want to perform. Set the value to Delet eVpnRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66rmd **** | The next hop of the destination-based route. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the destination- based route is created. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx*** * | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The weight of the destination-based route. Valid values: 0:: specifies a low priority for the route entry. 100: specifies a high priority for the route entry. Not e If two destination-based route entries are configured with the same destination CIDR block, you cannot set the weights of both route entries to 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The overlay mode. Set the value to Ipsec (IPsec tunneling). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVpnRouteEntryResponse>
        <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</DeleteVpnRouteEntryResponse>
```

`JSON` format `{`

```json
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 404 | InvalidVpnGatewayInsta nceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.FinancialLo cked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

##### DescribeVpnRouteEntries

Queries destination-based routes of a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnRouteEn tries | The operation that you want to perform. Set the value to DescribeVpnRout eEnt ries. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the destination- based routes are created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx*** * | The ID of the VPN gateway. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 10 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |
| TotalCount | Integer | 10 | The number of returned entries. |
| VpnRouteEntries | Array of VpnRouteEntry |   | The detailed information about the destination- based routes. |
| VpnRouteEntry |   |   |   |
| CreateTime | Long | 1492747187000 | The timestamp generated when the destination- based route was created. |
| NextHop | String | vco- bp15oes1py4i66rmd*** * | The next hop of the destination-based route. |

| Virtual Private Clou | d |   | Developer Guide·API reference |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the destination- based route. |
| State | String | published | The status of the destination-based route. published: The route is advertised. normal: The route is not advertised. |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m9** ** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the destination-based route. Valid values: 0: indicates that the priority of the route entry is low. 100: indicates that the priority of the route entry is high. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpnRouteEntries &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpnRouteEntriesResponse>
   <PageNumber>1</PageNumber>
   <TotalCount>1</TotalCount>
   <VpnRouteEntries>
      <VpnRouteEntry>
         <RouteDest>10.0.0.0/24</RouteDest>
         <VpnInstanceId>vpn-bp1cmw7jh1nfe43m9****</VpnInstanceId>
         <State>normal</State>
         <Weight>100</Weight>
         <CreateTime>1563874074000</CreateTime>
         <NextHop>vco-bp1tui07ob10fmuro****</NextHop>
      </VpnRouteEntry>
   </VpnRouteEntries>
   <PageSize>10</PageSize>
   <RequestId>BF3995A6-FA4F-4C74-B90F-89ECF4BFF4D5</RequestId>
</DescribeVpnRouteEntriesResponse>
```

`JSON` format `{`

```json
 "PageNumber": 1,
 "TotalCount": 1,
 "VpnRouteEntries": {
  "VpnRouteEntry": [
```

`{`

```json
    "RouteDest": "10.0.0.0/24",
    "VpnInstanceId": "vpn-bp1cmw7jh1nfe43m9****",
    "State": "normal",
    "Weight": 100,
    "CreateTime": 1563874074000,
    "NextHop": "vco-bp1tui07ob10fmuro****"
```

`]` `},`

```json
 "PageSize": 10,
 "RequestId": "BF3995A6-FA4F-4C74-B90F-89ECF4BFF4D5"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

##### ModifyVpnRouteEntryWeight

Modifies the weight of a destination-based route for a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnRouteEntr yWeight | The operation that you want to perform. Set the value to Modif yVpnRout eEnt ryWeight . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NewWeight | Integer | Yes | 100 | The new weight you want to set for the destination-based route. 0: specifies a low priority for the route entry. 100: specifies a high priority for the route entry. Not e If two destination-based route entries are configured with the same destination CIDR block, you cannot set the weights of both route entries to 100. |
| NextHop | String | Yes | vco- bp15oes1py4i66rmd **** | The next hop of the destination-based route. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the destination- based route is created. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx*** * | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The current weight of the destination-based route. Valid values: 0 and 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The overlay mode. Set the value to Ipsec (IPsec tunneling). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVpnRouteEntryWeight &NewWeight=100 &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVpnRouteEntryWeightResponse>
        <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</ModifyVpnRouteEntryWeightResponse>
```

`JSON` format `{`

```json
    "RequestId": "E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 404 | InvalidVpnGatewayInsta nceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.FinancialLo cked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

##### CreateVpnRouteEntry

Creates a destination-based route on a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnRouteEntr y | The operation that you want to perform. Set the value to Creat eVpnRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66rmd **** | The next hop of the destination-based route. |
| PublishVpc | Boolean | Yes | true | Specifies whether to advertise the destination-based route to the route table of the associated virtual private cloud (VPC). t rue: advertises the destination-based route to the route table of the associated VPC. f alse: does not advertise the destination- based route to the route table of the associated VPC. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the destination- based route is created. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx*** * | The ID of the VPN gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Weight | Integer | Yes | 0 | The weight of the destination-based route. Valid values: 0: specifies a low priority for the route. 100:specifies a high priority for the route. Not e If two destination-based route entries are configured with the same destination CIDR block, you cannot set the weights of both route entries to 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | mytest | The description of the destination-based route. |
| OverlayMode | String | No | Ipsec | The overlay mode. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | Long | 1492747187000 | The timestamp generated when the destination- based route was created. |
| Description | String | mytest | The description of the destination-based route. |
| NextHop | String | vco- bp15oes1py4i66rmd*** * | The next hop of the destination-based route. |
| OverlayMode | String | Ipsec | The overlay mode. |
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The ID of the request. |
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the destination- based route. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| State | String | published | The status of the destination-based route. published: The route is advertised. normal: The route is not advertised. |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m9** ** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the destination-based route. Valid values: 0 and 100. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateVpnRouteEntryResponse>
   <RouteDest>10.0.0.0/24</RouteDest>
   <VpnInstanceId>vpn-bp1cmw7jh1nfe43m9****</VpnInstanceId>
   <OverlayMode>Ipsec</OverlayMode>
   <State>published</State>
   <Weight>100</Weight>
   <CreateTime>1563873294331</CreateTime>
   <NextHop>vco-bp1tui07ob10fmuro****</NextHop>
      <RequestId>EE4C2417-9437-4333-BDEB-8493F7AA7258</RequestId>
</CreateVpnRouteEntryResponse>
```

`JSON` format `{`

```json
    "RouteDest": "10.0.0.0/24",
    "VpnInstanceId": "vpn-bp1cmw7jh1nfe43m9****",
    "OverlayMode": "Ipsec",
    "State": "published",
    "Weight": 100,
    "CreateTime": 1563873294331,
    "NextHop": "vco-bp1tui07ob10fmuro****",
    "RequestId":"CB2793A8-845F-444C-8E93-76F1BBDF9C78"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 404 | InvalidVpnGatewayInsta nceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.FinancialLo cked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

##### ModifyVpnPbrRouteEntryWeight

Modifies the weight of a policy-based route of a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnPbrRoute EntryWeight | The operation that you want to perform. Set the value to Modif yVpnPbrRout eEnt ryWeight . |
| NewWeight | Integer | Yes | 100 | The new weight you want to set for the policy-based route. 0: specifies a low priority for the route entry. 100: specifies a high priority for the route entry. Not e If two policy-based route entries are configured with the same destination CIDR block, you cannot set the weights of both route entries to 100. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NextHop | String | Yes | vco- bp15oes1py4i66rmd **** | The next hop of the policy-based route. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the policy-based route is created. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the policy- based route. |
| RouteSource | String | Yes | 192.168.1.0/24 | The source CIDR block of the policy-based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx*** * | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The original weight of the policy-based route. Valid values: 0 and 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The overlay mode. Set the value to Ipsec (IPsec tunneling). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVpnPbrRouteEntryWeight &NewWeight=100 &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVpnPbrRouteEntryWeightResponse>
        <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</ModifyVpnPbrRouteEntryWeightResponse>
```

`JSON` format `{`

```json
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 404 | InvalidVpnGatewayInsta nceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.FinancialLo cked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

##### DescribeVpnPbrRouteEntries

Queries policy-based routes of a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnPbrRout eEntries | The operation that you want to perform. Set the value to DescribeVpnPbrRout eEnt ries. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the policy-based routes are created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx*** * | The ID of the VPN gateway. |
| PageNumber | Integer | No | 10 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The ID of the request. |
| TotalCount | Integer | 12 | The number of returned entries. |
| VpnPbrRouteEntri es | Array of VpnPbrRouteEntry |   | The detailed information about the policy-based routes. |
| VpnPbrRouteEntry |   |   |   |
| CreateTime | Long | 1492747187000 | The timestamp generated when the policy-based route was created. |
| NextHop | String | vco- bp15oes1py4i66rmd*** * | The next hop of the policy-based route. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the policy-based route. |
| RouteSource | String | 192.xx.0.0/24 | The source CIDR block of the policy-based route. |
| State | String | published | The status of the policy-based route. Valid values: published: The route is advertised. normal: The route is not advertised. |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m9** ** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the policy-based route. Valid values: 0: indicates that the priority of the route entry is low. 100: indicates that the priority of the route entry is high. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpnPbrRouteEntries &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpnPbrRouteEntriesResponse>
   <PageNumber>1</PageNumber>
   <TotalCount>1</TotalCount>
   <RequestId>E5D94DC7-AEC7-4E73-A203-61B04D1F1160</RequestId>
   <PageSize>10</PageSize>
   <VpnPbrRouteEntries>
      <VpnPbrRouteEntry>
         <RouteDest>10.0.0.0/32</RouteDest>
         <VpnInstanceId>vpn-bp1cmw7jh1nfe43m9****</VpnInstanceId>
         <State>published</State>
         <Weight>100</Weight>
         <CreateTime>1563881012000</CreateTime>
         <NextHop>vco-bp1tui07ob10fmuro****</NextHop>
         <RouteSource>11.0.0.0/32</RouteSource>
      </VpnPbrRouteEntry>
   </VpnPbrRouteEntries>
</DescribeVpnPbrRouteEntriesResponse>
```

`JSON` format `{`

```json
    "PageNumber": 1,
    "TotalCount": 1,
    "RequestId": "E5D94DC7-AEC7-4E73-A203-61B04D1F1160",
    "PageSize": 10,
    "VpnPbrRouteEntries": {
        "VpnPbrRouteEntry": [
```

`{`

```json
                "RouteDest": "10.0.0.0/32",
                "VpnInstanceId": "vpn-bp1cmw7jh1nfe43m9****",
                "State": "published",
                "Weight": 100,
                "CreateTime": 1563881012000,
                "NextHop": "vco-bp1tui07ob10fmuro****",
                "RouteSource": "11.0.0.0/32"
```

`]` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

##### PublishVpnRouteEntry

Advertises a route of a VPN gateway to the route table of the associated virtual private cloud (VPC). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PublishVpnRouteEnt ry | The operation that you want to perform. Set the value to PublishVpnRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66rmd **** | The next hop of the route. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PublishVpc | Boolean | Yes | true | Specifies whether to advertise the route of the VPN gateway to the route table of the associated VPC. t rue: advertises the route to the route table of the associated VPC. f alse: does not advertise the route to the route table of the associated VPC. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the route of the VPN gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the route of the VPN gateway. |
| RouteType | String | Yes | pbr | The type of the route of the VPN gateway. Valid values: pbr: policy-based route. dbr: destination-based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx*** * | The ID of the VPN gateway. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=PublishVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &RouteType=pbr &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PublishVpnRouteEntryResponse>
      <RequestId>EE4C2417-9437-4333-BDEB-8493F7AA7258</RequestId>
</PublishVpnRouteEntryResponse>
```

`JSON` format `{`

```json
    "RequestId":"CB2793A8-845F-444C-8E93-76F1BBDF9C78"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 404 | InvalidVpnGatewayInsta nceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.FinancialLo cked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

##### CreateVpnPbrRouteEntry

Creates a policy-based route for a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnPbrRouteE ntry | The operation that you want to perform. Set the value to Creat eVpnPbrRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66rmd **** | The next hop of the policy-based route. |
| PublishVpc | Boolean | Yes | true | Specifies whether to advertise the policy- based route to the route table of the associated virtual private cloud (VPC). Valid values: t rue: advertises the policy-based route to the route table of the associated VPC . f alse: does not advertise the policy- based route to the route table of the associated VPC. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where you want to create the policy-based route for the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the policy- based route. |
| RouteSource | String | Yes | 192.168.1.0/24 | The source CIDR block of the policy-based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx*** * | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The weight of the policy-based route. Valid values: 0: specifies a low priority for the route entry. 100: specifies a high priority for the route entry. Not e If two policy-based route entries are configured with the same destination CIDR block, you cannot set the weights of both route entries to 100. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | vpnroute1 | The description of the policy-based route. |
| OverlayMode | String | No | Ipsec | The overlay mode. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | Long | 1492747187000 | The timestamp generated when the policy-based route was created. |
| Description | String | vpnroute1 | The description of the policy-based route. |
| NextHop | String | vco- bp15oes1py4i66rmd*** * | The next hop of the policy-based route. |
| OverlayMode | String | Ipsec | The overlay mode. |
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The ID of the request. |
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the policy-based route. |
| RouteSource | String | 192.168.1.0/24 | The source CIDR block of the policy-based route. |
| State | String | normal | The status of the policy-based route. Valid values: published: The route is advertised. normal: The route is not advertised. |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m9** ** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the policy-based route. Valid values: 0 and 100. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateVpnPbrRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateVpnPbrRouteEntryResponse>
   <RouteDest>10.0.0.0/24</RouteDest>
   <RouteSource>192.168.1.0/24</RouteSource>
   <VpnInstanceId>vpn-bp1cmw7jh1nfe43m9****</VpnInstanceId>
   <OverlayMode>Ipsec</OverlayMode>
   <State>published</State>
   <Weight>100</Weight>
   <CreateTime>1563873294331</CreateTime>
   <NextHop>vco-bp1tui07ob10fmuro****</NextHop>
</CreateVpnPbrRouteEntryResponse>
```

`JSON` format `{`

```json
    "RouteDest": "10.0.0.0/24",
    "RouteSource": "192.168.1.0/24",
    "VpnInstanceId": "vpn-bp1cmw7jh1nfe43m9****",
    "OverlayMode": "Ipsec",
    "State": "published",
    "Weight": 100,
    "CreateTime": 1563873294331,
    "NextHop": "vco-bp1tui07ob10fmuro****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVpnGatewayInsta nceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.FinancialLo cked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

#### IPsec-VPN

##### DescribeVpnConnection

Queries the details of an IPsec-VPN connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnConnect ion | The operation that you want to perform. Set the value to DescribeVpnConnect ion. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the IPsec-VPN connection is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80nck* *** | The ID of the IPsec-VPN connection. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnectionId | String | vco- bp1bbi27hojx80nck**** | The ID of the IPsec-VPN connection. |
| CustomerGateway Id | String | cgw- bp1mvj4g9kogwwcxk** ** | The ID of the customer gateway. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2ogj*** * | The ID of the VPN gateway. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | ipsec1 | The name of the IPsec-VPN connection. |
| LocalSubnet | String | 10.1.1.0/24,10.1.2.0/24 | The CIDR block of the VPC. |
| RemoteSubnet | String | 10.10.1.0/24,10.10.2.0/ 24 | The CIDR block of the data center. |
| CreateTime | Long | 1492753817000 | The time when the IPsec-VPN connection was created. |
| Status | String | ike sa not established _ _ _ | The status of the IPsec-VPN connection. Valid values: ike sa not est ablished: indicates that Phase _ _ _ 1 negotiations failed. ike sa est ablished: indicates that Phase 1 _ _ negotiations succeeded. ipsec sa not est ablished: indicates that _ _ _ Phase 2 negotiations failed. ipsec sa est ablished: indicates that Phase 2 _ _ negotiations succeeded. |
| EffectImmediately | Boolean | true | Indicates whether the IPsec-VPN connection immediately takes effect. Valid values: t rue: Negotiations are reinitiated when the configuration is changed. f alse: Negotiations are reinitiated when traffic is detected. When negotiations are reinitiated, transient connections may occur. |
| IkeConfig | Struct |   | The configuration of Phase 1 negotiations. |
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. |
| IkeMode | String | main | The IKE mode. Both main and aggressive modes are supported. The main mode provides higher security. If NAT traversal is enabled, we recommend that you select the aggressive mode. |
| IkePfs | String | group2 | The DH group. |
| IkeVersion | String | ikev1 | The IKE version. |

| Virtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| LocalId | String | 116.XX.XX.69 | The local ID. The default value is the IP address of the VPN gateway. Both fully qualified domain names (FQDNs) and IP addresses are supported. |
| Psk | String | pgw6dy7d1i8in7x5 | The pre-shared key. |
| RemoteId | String | 139.XX.XX.32 | The peer ID. The default value is the IP address of the customer gateway. Both FQDNs and IP addresses are supported. |
| IpsecConfig | Struct |   | The configuration of Phase 2 negotiations. |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm. |
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. |
| IpsecPfs | String | group2 | The DH group. |
| RequestId | String | F2310D45-BCF6-4E2E- 9082-B4503844BA4C | The ID of the request. |
| VcoHealthCheck | Struct |   | The information about health checks. |
| Dip | String | 10.XX.XX.1 | The destination IP address. |
| Enable | String | true | Indicates whether health checks are enabled. Valid values: f alse: Health checks are disabled. t rue: Health checks are enabled. |
| Interval | Integer | 3 | The interval between two consecutive health checks. Unit: seconds. |
| Retry | Integer | 3 | The maximum number of health check retries. |
| Sip | String | 192.XX.XX.2 | The source IP address for health checks. |
| Status | String | failed | The status of the health check. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpnConnection &RegionId=cn-qingdao-env66-d01 &VpnConnectionId=vco-bp1bbi27hojx80nck**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpnConnectionResponse>
      <PageNumber>1</PageNumber>
      <VpnConnections>
            <VpnConnection>
                  <Name>c2</Name>
                  <CustomerGatewayId>cgw-bp1wl8dtz3auwlav****</CustomerGatewayId>
                  <Status>ike_sa_not_established</Status>
                  <RemoteSubnet>192.168.0.0/16</RemoteSubnet>
                  <IpsecConfig>
                        <IpsecLifetime>86400</IpsecLifetime>
                        <IpsecAuthAlg>md5</IpsecAuthAlg>
                        <IpsecPfs>group2</IpsecPfs>
                        <IpsecEncAlg>aes</IpsecEncAlg>
                  </IpsecConfig>
                  <EffectImmediately>false</EffectImmediately>
                  <VpnGatewayId>vpn-bp1yfrjxn4d5t63tb****</VpnGatewayId>
                  <CreateTime>1519391420000</CreateTime>
                  <VpnConnectionId>vco-bp1w3m1p23iftycvs****</VpnConnectionId>
                  <LocalSubnet>172.16.0.0/12</LocalSubnet>
                  <IkeConfig>
                        <IkeEncAlg>aes</IkeEncAlg>
                        <RemoteId>47.XX.XX.176</RemoteId>
                        <IkePfs>group2</IkePfs>
                        <IkeAuthAlg>sha1</IkeAuthAlg>
                        <Psk>1234567</Psk>
                        <IkeMode>aggressive</IkeMode>
                        <IkeLifetime>86400</IkeLifetime>
                        <IkeVersion>ikev1</IkeVersion>
                        <LocalId>116.XX.XX.119</LocalId>
                  </IkeConfig>
            </VpnConnection>
      </VpnConnections>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <RequestId>7D598A10-26EF-44F2-9F47-E417842F3CEA</RequestId>
</DescribeVpnConnectionResponse>
```

`JSON` format `{`

```json
    "PageNumber": 1,
    "VpnConnections": {
        "VpnConnection": [
```

`{`

```json
                "Name": "c2",
                "CustomerGatewayId": "cgw-bp1wl8dtz3auwlavw****",
                "Status": "ike_sa_not_established",
                "RemoteSubnet": "192.168.0.0/16",
                "IpsecConfig": {
                    "IpsecLifetime": 86400,
                    "IpsecAuthAlg": "md5",
                    "IpsecPfs": "group2",
                    "IpsecEncAlg": "aes"
```

`},`

```json
                "EffectImmediately": false,
                "VpnGatewayId": "vpn-bp1yfrjxn4d5t63t****",
                "CreateTime": 1519391420000,
                "VpnConnectionId": "vco-bp1w3m1p23iftycv****",
                "LocalSubnet": "172.16.0.0/12",
                "IkeConfig": {
                    "IkeEncAlg": "aes",
                    "RemoteId": "47.XX.XX.176",
                    "IkePfs": "group2",
                    "IkeAuthAlg": "sha1",
                    "Psk": "1234567",
                    "IkeMode": "aggressive",
                    "IkeLifetime": 86400,
                    "IkeVersion": "ikev1",
                    "LocalId": "116.XX.XX.119"
```

`]` `},`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "7D598A10-26EF-44F2-9F47-E417842F3CEA"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidVpnConnectionIns tanceId.NotFound | The specified vpn connection instance id does not exist. | The error message returned because the specified IPsec-VPN connection does not exist. Check whether the ID of the IPsec-VPN connection is valid. |

##### DeleteVpnConnection

Deletes a specified IPsec-VPN connection. Not e After an IPsec-VPN connection between a virtual private cloud (VPC) and a data center is deleted, the communication between the VPC and data center is interrupted. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnConnectio n | The operation that you want to perform. Set the value to Delet eVpnConnect ion. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the IPsec-VPN connection is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80nck* *** | The ID of the IPsec-VPN connection. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D-48FE- 8316-ACA81BB230DA | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVpnConnection &RegionId=cn-qingdao-env66-d01 &VpnConnectionId=vco-bp1bbi27hojx80nck**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVpnConnectionResponse>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteVpnConnectionResponse>
```

`JSON` format `{`

```json
  "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidVpnConnectionIns tanceId.NotFound | The specified vpn connection instance id does not exist. | The error message returned because the specified IPsec-VPN connection does not exist. Check whether the ID of the IPsec-VPN connection is valid. |
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |

##### DownloadVpnConnectionConfig

Queries the configuration of an IPsec-VPN connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DownloadVpnConne ctionConfig | The operation that you want to perform. Set the value to DownloadVpnConnect ionConf ig. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the IPsec-VPN connection is created. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80nck* *** | The ID of the IPsec-VPN connection. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0C68048B-0F70-40DA- B8AE-1B79B5CF62E3 | The ID of the request. |
| VpnConnectionCo nfig | Struct |   | The configuration of the IPsec-VPN connection. |
| IkeConfig | Struct |   | The IKE configuration. |
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. Valid values: sha1 and md5. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. Unit: seconds. |
| IkeMode | String | main | The IKE mode. Valid values: main and aggressive. The main mode offers higher security. If NAT traversal is enabled, we recommend that you select the aggressive mode. |
| IkePfs | String | group2 | The DH group. |
| IkeVersion | String | ikev1 | The IKE version. |
| LocalId | String | 116.XX.XX.69 | The local ID. The default value is the IP address of the VPN gateway. Both fully qualified domain names (FQDNs) and IP addresses are supported. |
| Psk | String | pgw6dy7d1i8i**** | The pre-shared key. |
| RemoteId | String | 139.XX.XX.32 | The peer ID. The default value is the IP address of the customer gateway. Both FQDNs and IP addresses are supported. |
| IpsecConfig | Struct |   | The configuration of the IPsec-VPN connection. |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm. Valid values: sha1 and md5. |

| Virtual Private Clou | d |   | Developer Guide·API reference |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. Unit: seconds. |
| IpsecPfs | String | group2 | The DH group. |
| Local | String | 139.XX.XX.32 | The ID of the VPN gateway. |
| LocalSubnet | String | 10.1.1.0/24,10.1.2.0/24 | The CIDR block of the VPC. |
| Remote | String | 116.XX.XX.69 | The ID of the customer gateway. |
| RemoteSubnet | String | 10.10.1.0/24,10.10.2.0/ 24 | The CIDR block of the data center. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DownloadVpnConnectionConfig &RegionId=cn-qingdao-env66-d01 &VpnConnectionId=vco-bp1bbi27hojx80nck**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DownloadVpnConnectionConfigResponse>
      <RequestId>0C68048B-0F70-40DA-B8AE-1B79B5CF62E3</RequestId>
      <VpnConnectionConfig>
            <RemoteSubnet>10.10.1.0/24,10.10.2.0/24</RemoteSubnet>
            <Local>139.XX.XX.32</Local>
            <IpsecConfig>
                  <IpsecLifetime>86400</IpsecLifetime>
                  <IpsecAuthAlg>sha1</IpsecAuthAlg>
                  <IpsecPfs>group2</IpsecPfs>
                  <IpsecEncAlg>aes</IpsecEncAlg>
            </IpsecConfig>
            <Remote>116.XX.XX.69x</Remote>
            <LocalSubnet>172.16.2.0/24</LocalSubnet>
            <IkeConfig>
                  <IkeEncAlg>aes</IkeEncAlg>
                  <IkePfs>group2</IkePfs>
                  <RemoteId>116.XX.XX.69</RemoteId>
                  <IkeAuthAlg>sha1</IkeAuthAlg>
                  <Psk>pgw6dy7d1i8i****</Psk>
                  <IkeMode>main</IkeMode>
                  <IkeLifetime>86400</IkeLifetime>
                  <IkeVersion>ikev1</IkeVersion>
                  <LocalId>139.XX.XX.32</LocalId>
            </IkeConfig>
      </VpnConnectionConfig>
</DownloadVpnConnectionConfigResponse>
```

`JSON` format `{`

```json
    "RequestId": "0C68048B-0F70-40DA-B8AE-1B79B5CF62E3",
    "VpnConnectionConfig": {
        "RemoteSubnet": "10.10.1.0/24,10.10.2.0/24",
        "Local": "139.XX.XX.32",
        "IpsecConfig": {
            "IpsecLifetime": 86400,
            "IpsecAuthAlg": "sha1",
            "IpsecPfs": "group2",
            "IpsecEncAlg": "aes"
```

`},`

```json
        "Remote": "116.XX.XX.69",
        "LocalSubnet": "172.16.2.0/24",
        "IkeConfig": {
            "IkeEncAlg": "aes",
            "IkePfs": "group2",
            "RemoteId": "116.XX.XX.69",
            "IkeAuthAlg": "sha1",
            "Psk": "pgw6dy7d1i8i****",
            "IkeMode": "main",
            "IkeLifetime": 86400,
            "IkeVersion": "ikev1",
            "LocalId": "139.XX.XX.32"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidVpnConnectionIns tanceId.NotFound | The specified vpn connection instance id does not exist. | The error message returned because the specified IPsec-VPN connection does not exist. Check whether the ID of the IPsec-VPN connection is valid. |

##### CreateVpnConnection

Creates an IPsec-VPN connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnConnectio n | The operation that you want to perform. Set the value to Creat eVpnConnect ion. |
| CustomerGatewayId | String | Yes | vpn- bp1q8bgx4xnk**** | The ID of the customer gateway. |
| LocalSubnet | String | Yes | 10.1.1.0/24,10.1.2.0 /24 | The CIDR block of the virtual private cloud (VPC) that is used to connect with the data center. This CIDR block is used in Phase 2 negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.1.0/24,192.168.2.0/24. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the IPsec-VPN connection. You can call the DescribeRegions operation to query the most recent region list. |
| RemoteSubnet | String | Yes | 10.10.1.0/24,10.10.2 .0/24 | The CIDR block of the data center. The peer CIDR block is used in Phase 2 negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.3.0/24,192.168.4.0/24. |
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm**** | The ID of the VPN gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | IPsec | The name of the IPsec-VPN connection. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter and cannot start with http:// or https:// . |
| EffectImmediately | Boolean | No | false | Specifies whether to delete the current IPsec tunnel and reinitiate negotiations. Valid values: t rue: initiates negotiations after the configuration is completed. f alse: initiates negotiations when inbound traffic is detected. This is the default value. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IkeConfig | String | No | {"IkeVersion":"ikev1" ,"IkeMode":"main","I keEncAlg":"aes","Ike AuthAlg":"sha1","Ike Pfs":"group2","IkeLif etime":86400} | The configuration of Phase 1 negotiations: IkeConf ig.Psk: the pre-shared key that is used to authenticate the VPN gateway and the customer gateway. By default, a random value is generated. You can also specify a pre-shared key. The description cannot exceed 100 characters in length. IkeConf ig.IkeVersion: The version of the IKE protocol. Valid values: ikev1 and ikev2. Default value: ikev1. IkeConf ig.IkeMode: the negotiation mode of IKE V1. Valid values: main and aggressive. Default value: main. IkeConf ig.IkeEncAlg: The encryption algorithm used in Phase 1 negotiations. Valid values: aes, aes192, aes256, des, and 3des. Default value: aes. IkeConf ig.IkeAut hAlg: The authentication algorithm used in Phase 1 negotiations. Valid values: md5 and sha1. Default value: md5. IkeConf ig.IkePf s: The Diffie-Hellman key exchange algorithm used in Phase 1 negotiations. Valid values: group1, group2, group5, group14, and group24. Default value: group2. IkeConf ig.IkeLif et ime: the SA lifetime as a result of Phase 1 negotiations. Valid values: 0 t o 86400. Unit: seconds. Default value: 86400. IkeConf ig.LocalIdIPsec: the identifier of the VPN gateway. This parameter can contain up to 100 characters. The default value is the public IP address of the VPN gateway. IkeConf ig.Remot eId: the identifier of the customer gateway. This parameter can contain up to 100 characters. By default, it is the public IP address of the customer gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IpsecConfig | String | No | {"IpsecEncAlg":"aes" ,"IpsecAuthAlg":"sh a1","IpsecPfs":"grou p2","IpsecLifetime": 86400} | The configuration of Phase 2 negotiations: IpsecConf ig.IpsecEncAlg: The encryption algorithm used in Phase 2 negotiations. Valid values: aes, aes192, aes256, des, and 3des. Default value: aes. IpsecConf ig. IpsecAut hAlg: The authentication algorithm used in Phase 2 negotiations. Valid values: md5 and sha1. Default value: md5. IpsecConf ig. IpsecPf s: the Diffie- Hellman group for perfect forward secrecy (PFS). If you set this parameter, the system forwards packets of all protocols. The Diffie-Hellman key exchange algorithm used in Phase 2 negotiations. Valid values: group1, group2, group5, group14, and group24. Default value: group2. IpsecConf ig. IpsecLif et ime: the SA lifetime as a result of Phase 2 negotiations. Valid values: 0 t o 86400. Unit: seconds. Default value: 86400. |
| HealthCheckConfig | String | No | {"enable":"true","dip ":"192.168.xx.2","sip ":"192.168.xx.2","int erval":"3","retry":"3" } | The health check configuration: Healt hCheckConf ig.enable: specifies whether to enable health checks. Valid values: t rue and f alse. Default value: false. Healt hCheckConf ig.dip: the destination IP address configured for health checks. Healt hCheckConf ig.sip: the source IP address configured for health checks. Healt hCheckConf ig.int erval: the time interval of health check retries. Unit: seconds. Healt hCheckConf ig.ret ry: the maximum number of health check retries. |
| AutoConfigRoute | Boolean | No | true | Specifies whether to automatically configure routes. Valid values: t rue: enables automatic configuration. f alse: disables automatic configuration. This is the default value. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnectionId | String | vco-bp15oes1py4i6**** | The ID of the IPsec-VPN connection. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | Long | 1544666102000 | The timestamp generated when the IPsec-VPN connection was created. |
| Name | String | test | The name of the IPsec-VPN connection. |
| RequestId | String | 082AD562-B8DB-4BB2- 861F-DA1FCA01FD76 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateVpnConnection &CustomerGatewayId=vpn-bp1q8bgx4xnk**** &LocalSubnet=10.1.1.0/24,10.1.2.0/24 &RegionId=cn-qingdao-env66-d01 &RemoteSubnet=10.10.1.0/24,10.10.2.0/24 &VpnGatewayId=vpn-bp1q8bgx4xnkm**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateVpnConnectionResponse>
      <VpnConnectionId>vco-bp1bbi27hojx8****</VpnConnectionId>
      <CreateTime>1493363928000</CreateTime>
</CreateVpnConnectionResponse>
```

`JSON` format `{`

```json
    "CreateTime": 1544666102000,
    "VpnConnectionId": "vco-bp15oes1py4i6****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |

| Developer Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidCustomerGatewa yInstanceId.NotFound | The specified customer gateway instance id does not exist. | The error message returned because the specified instance ID does not exist. |
| 404 | InvalidVpnGatewayInsta nceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |
| 400 | InvalidVpnConnection.Al readyExists | Vpn connection already exists. | The error message returned because the IPsec-VPN connection already exists. |
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.FinancialLo cked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

##### DescribeVpnConnections

Queries one or more IPsec-VPN connections. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnConnect ions | The operation that you want to perform. Set the value to DescribeVpnConnect ions. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the IPsec-VPN connections are created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | No | vpn- bp1q8bgx4xnkx**** | The ID of the VPN gateway. |
| CustomerGatewayId | String | No | cgw- bp1mvj4g9kogw**** | The ID of the customer gateway. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpnConnectionId | String | No | vco- bp15oes1py4i6**** | The ID of the IPsec-VPN connection. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnections | Array of VpnConnection |   | The detailed information about the IPsec-VPN connections. |
| VpnConnection |   |   |   |
| IkeConfig | Struct |   | The configuration of Phase 1 negotiations. |
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. Valid values: sha1 and MD5. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. Unit: seconds. |
| IkeMode | String | main | The IKE mode. Valid values: main and aggressive . The main mode offers higher security. If NAT traversal is enabled, we recommend that you select the aggressive mode. |
| IkePfs | String | group2 | The DH group. Valid values: group1, group2, group5, group14, and group24. |
| IkeVersion | String | ikev1 | The IKE version. |
| LocalId | String | 116.XX.XX.64 | The local ID. The default value is the IP address of the VPN gateway. Both fully qualified domain names (FQDNs) and IP addresses are supported. |
| Psk | String | pgw6dy7d**** | The pre-shared key. |
| RemoteId | String | 139.XX.XX.167 | The peer ID. The default value is the IP address of the customer gateway. Both FQDNs and IP addresses are supported. |
| IpsecConfig | Struct |   | The configuration of Phase 2 negotiations. |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm.Valid values: sha1 and md5. |

|   | Developer Guide·AP | I reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. |
| IpsecPfs | String | group2 | The DH group. |
| VpnConnectionId | String | vco-bp10lz7aejumd**** | The ID of the IPsec-VPN connection. |
| CustomerGateway Id | String | cgw- bp1mvj4g9kogw**** | The ID of the customer gateway. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm**** | The ID of the VPN gateway. |
| Name | String | name | The name of the IPsec-VPN connection. |
| LocalSubnet | String | 10.1.1.0/24,10.1.2.0/24 | The CIDR block of the VPC. |
| RemoteSubnet | String | 10.10.1.0/24,10.10.2.0/ 24 | The CIDR block of the data center. |
| CreateTime | Long | 1492753817000 | The timestamp generated when the IPsec-VPN connection was created. |
| Status | String | ipsec sa established _ _ | The status of the IPsec-VPN connection. Valid values: ike sa not est ablished: indicates that Phase _ _ _ 1 negotiations failed. ike sa est ablished: indicates that Phase 1 _ _ negotiations succeeded. ipsec sa not est ablished: indicates that _ _ _ Phase 2 negotiations failed. ipsec sa est ablished: indicates that Phase 2 _ _ negotiations succeeded. |
| EffectImmediately | Boolean | true | Indicates whether IPsec-VPN negotiations are initiated immediately. Valid values: t rue: Negotiations are reinitiated when the configuration is changed. f alse: Negotiations are reinitiated when traffic is detected. When negotiations are reinitiated, transient connections may occur. |
| VcoHealthCheck | Struct |   | The configuration of health checks. |
| Dip | String | 8.XX.XX.8 | The destination IP address. |

| Virtual Private Clou | d |   | Developer Guide·API reference |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Enable | String | true | Indicates whether health checks are enabled. Valid values: t rue: Health checks are enabled. f alse: Health checks are disabled. |
| Interval | Integer | 2 | The interval between two consecutive health checks. Unit: seconds. |
| Retry | Integer | 1 | The maximum number of health check retries. |
| Sip | String | 192.XX.XX.66 | The source IP address that is used for health checks. |
| Status | String | failed | The status of the health check. Valid values: f ailed: The health check failed. success: The health check was successful. |
| TotalCount | Integer | 10 | The number of entries. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned on each page. |
| RequestId | String | 54A4B3D0-DF4D-4C54- B8DC-5DC8DD49C939 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpnConnections &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpnConnections>
   <PageNumber>1</PageNumber>
   <VpnConnections>
      <VpnConnection>
         <Name>VPN connection test</Name>
         <CustomerGatewayId>cgw-bp1pvpl9r9adjxxxxxxxx</CustomerGatewayId>
         <RemoteSubnet>172.16.2.0/24</RemoteSubnet>
         <IpsecConfig>
            <IpsecLifetime>86400</IpsecLifetime>
            <IpsecAuthAlg>sha1</IpsecAuthAlg>
            <IpsecPfs>group2</IpsecPfs>
            <IpsecEncAlg>aes</IpsecEncAlg>
         </IpsecConfig>
         <EffectImmediately>true</EffectImmediately>
         <VpnGatewayId>vpn-bp1q8bgx4xnkmxxxxxxxx</VpnGatewayId>
         <CreateTime>1492753817000</CreateTime>
         <VpnConnectionId>vco-bp10lz7aejumdxxxxxxxx</VpnConnectionId>
         <status>ipsec_sa_established</status>
         <LocalSubnet>10.1.1.0/24,10.1.2.0/24</LocalSubnet>
         <IkeConfig>
            <IkeEncAlg>aes</IkeEncAlg>
            <RemoteId>139.XX.XX.167</RemoteId>
            <IkePfs>group2</IkePfs>
            <IkeAuthAlg>sha1</IkeAuthAlg>
            <Psk>pgw6dy****</Psk>
            <IkeMode>main</IkeMode>
            <IkeLifetime>86400</IkeLifetime>
            <IkeVersion>ikev1</IkeVersion>
            <LocalId>116.XX.XX.64</LocalId>
         </IkeConfig>
      </VpnConnection>
   </VpnConnections>
   <TotalCount>1</TotalCount>
   <PageSize>10</PageSize>
   <RequestId>54A4B3D0-DF4D-4C54-B8DC-5DC8DD49C939</RequestId>
</DescribeVpnConnections>
```

`JSON` format `{`

```json
    "PageNumber": 1,
    "VpnConnections": {
        "VpnConnection": [
```

`{`

```json
                "Name": "vpn connection test",
                "CustomerGatewayId": "cgw-bp1pvpl9r9adjxxxxxxxx",
                "RemoteSubnet": "172.16.2.0/24",
                "IpsecConfig": {
                    "IpsecLifetime": 86400,
                    "IpsecAuthAlg": "sha1",
                    "IpsecPfs": "group2",
                    "IpsecEncAlg": "aes"
```

`},`

```json
                "EffectImmediately": true,
                "VpnGatewayId": "vpn-bp1q8bgx4xnkmxxxxxxxx",
                "CreateTime": 1492753817000,
                "VpnConnectionId": "vco-bp10lz7aejumdxxxxxxxx",
                "status": "ipsec_sa_established",
                "LocalSubnet": "10.1.1.0/24,10.1.2.0/24",
                "IkeConfig": {
                    "IkeEncAlg": "aes",
                    "RemoteId": "139.XX.XX.167",
                    "IkePfs": "group2",
                    "IkeAuthAlg": "sha1",
                    "Psk": "pgw6dy****",
                    "IkeMode": "main",
                    "IkeLifetime": 86400,
                    "IkeVersion": "ikev1",
                    "LocalId": "116.XX.XX.64"
```

`]` `},`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "54A4B3D0-DF4D-4C54-B8DC-5DC8DD49C939"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

##### ModifyVpnConnectionAttribute

Modifies the configuration of an IPsec-VPN connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnConnectio nAttribute | The operation that you want to perform. Set the value to Modif yVpnConnect ionAt t ribut e. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the IPsec-VPN connection is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80nck* *** | The ID of the IPsec-VPN connection. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | IPsec | The name of the IPsec-VPN connection. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter. However, the name cannot start with http:// or https:// . |
| LocalSubnet | String | No | 10.1.1.0/24,10.1.2.0 /24 | The CIDR block of the virtual private cloud (VPC) that is used to connect with the data center. This CIDR block is used in Phase 2 negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.1.0/24,192.168.2.0/24. |
| RemoteSubnet | String | No | 10.10.1.0/24,10.10.2 .0/24 | The CIDR block of the data center. This CIDR block is used in Phase 2 negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.3.0/24,192.168.4.0/24. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EffectImmediately | Boolean | No | false | Specifies whether to delete the current IPsec tunnel and reinitiate negotiations. Valid values: t rue: initiates negotiations after the configuration is completed. f alse: initiates negotiations when inbound traffic is detected. This is the default value. |
| IkeConfig | String | No | {"IkeVersion":"ikev1" ,"IkeMode":"main","I keEncAlg":"aes","Ike AuthAlg":"sha1","Ike Pfs":"group2","IkeLif etime":86400} | The configuration of Phase 1 negotiations: IkeConf ig.Psk: the pre-shared key that is used to authenticate the VPN gateway and the customer gateway. You can specify a key or use the default key that is randomly generated by the system. The key must be 1 to 100 characters in length. IkeConf ig.IkeVersion: the version of the IKE protocol. Valid values: ikev1 and ikev2. Default value: ikev1. IkeConf ig.IkeMode: the negotiation mode of IKE V1. Valid values: main and aggressive. Default value: main. IkeConf ig.IkeEncAlg: The encryption algorithm of Phase 1 negotiations. Valid values: aes, aes192, aes256, des, and 3des. Default value: aes. IkeConf ig.IkeAut hAlg: The authentication algorithm of Phase 1 negotiations. Valid values: md5 and sha1. Default value: sha1. IkeConfig.IkePfs: The Diffie-Hellman key exchange algorithm of Phase 1 negotiations. Valid values: group1, group2, group5, group14, and group24. Default value: group2. IkeConf ig.IkeLif et ime: the SA lifetime as a result of Phase 1 negotiations. Valid values: 0 to 86400. Unit: seconds. Default value: 86400. IkeConf ig.LocalIdIPsec: the identifier of the VPN gateway. This parameter can contain up to 100 characters. By default, it is the public IP address of the VPN gateway. IkeConf ig.Remot eId: the identifier of the customer gateway. This parameter can contain up to 100 characters. By default, it is the public IP address of the customer gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IpsecConfig | String | No | {"IpsecEncAlg":"aes" ,"IpsecAuthAlg":"sh a1","IpsecPfs":"grou p2","IpsecLifetime": 86400} | The configuration of Phase 2 negotiations: IpsecConf ig.IpsecEncAlg: The encryption algorithm of Phase 2 negotiations. Valid values: aes, aes192, aes256, des, and 3des. Default value: aes. IpsecConf ig. IpsecAut hAlg: The authentication algorithm of Phase 2 negotiations. Valid values: md5 and sha1. Default value: sha1. IpsecConf ig. IpsecPf s: the Diffie- Hellman group for perfect forward secrecy (PFS). If you set this parameter, the system forwards packets of all protocols. The Diffie-Hellman key exchange algorithm of Phase 2 negotiations. Valid values: group1, group2, group5, group14, and group24. Default value: group2. IpsecConf ig. IpsecLif et ime: the SA lifetime as a result of Phase 2 negotiations. Valid values: 0 to 86400. Unit: seconds. Default value: 86400. |
| HealthCheckConfig | String | No | {"enable":"true","dip ":"192.168.xx.2","sip ":"192.168.xx.2","int erval":"3","retry":"3" } | The health check configuration: Healt hCheckConf ig.enable: specifies whether to enable health checks. Valid values: t rue and f alse. Default value: false. Healt hCheckConf ig.dip: the destination IP address configured for the health check. Healt hCheckConf ig.sip: the source IP address configured for the health check. Healt hCheckConf ig.int erval: the time interval of health check retries. Unit: seconds. Healt hCheckConf ig.ret ry: the maximum number of health check retries. |
| AutoConfigRoute | Boolean | No | true | Specifies whether to automatically advertise routes. Valid values: t rue: enables automatic advertising. f alse: disables automatic advertising. This is the default value. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnectionId | String | vco- bp1bbi27hojx80nck**** | The ID of the IPsec-VPN connection. |

| Virtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGateway Id | String | vpn- bp1q8bgx4xnkm2ogj*** * | The ID of the customer gateway. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2ogj*** * | The ID of the VPN gateway. |
| Name | String | test | The name of the IPsec-VPN connection. |
| LocalSubnet | String | 10.1.1.0/24,10.1.2.0/24 | The CIDR block of the VPC. |
| RemoteSubnet | String | 10.10.1.0/24,10.10.2.0/ 24 | The CIDR block of the data center. |
| CreateTime | Long | 1492753817000 | The timestamp generated when the IPsec-VPN connection was created. |
| Description | String | description | The description of the IPsec-VPN connection. |
| EffectImmediately | Boolean | false | Indicates whether IPsec-VPN negotiations are initiated immediately. Valid values: t rue: initiates negotiations after the configuration is completed. f alse: initiates negotiations when inbound traffic is detected. |
| IkeConfig | Struct |   | The configuration of Phase 1 negotiations. |
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. |
| IkeMode | String | main | The IKE mode. |
| IkePfs | String | group2 | The DH group. |
| IkeVersion | String | ikev1 | The IKE version. |
| LocalId | String | 116.XX.XX.64 | The local ID. The default value is the IP address of the VPN gateway. Both fully qualified domain names (FQDNs) and IP addresses are supported. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Psk | String | pgw6dy7d1i8i**** | The pre-shared key. |
| RemoteId | String | 139.XX.XX.167 | The peer ID. The default value is the IP address of the customer gateway. Both FQDNs and IP addresses are supported. |
| IpsecConfig | Struct |   | The configuration of Phase 2 negotiations. |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm. |
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. |
| IpsecPfs | String | group2 | The DH group. |
| RequestId | String | 7DB79D0C-5F27-4AB5- 995B-79BE55102F90 | The ID of the request. |
| VcoHealthCheck | Struct |   | The health check configuration. |
| Dip | String | 1.XX.XX.1 | The destination IP address. |
| Enable | String | true | Indicates whether health checks are enabled. Valid values: t rue: Health checks are enabled. f alse: Health checks are disabled. |
| Interval | Integer | 3 | The interval between two consecutive health checks. Unit: seconds. |
| Retry | Integer | 1 | The maximum number of health check retries. |
| Sip | String | 2.XX.XX.2 | The source IP address. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVpnConnectionAttribute &RegionId=cn-qingdao-env66-d01 &VpnConnectionId=vco-bp1bbi27hojx80nck**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVpnConnectionAttributeResponse>
      <Name>vpn</Name>
      <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId>
      <RemoteSubnet>172.16.2.0/24</RemoteSubnet>
      <IpsecConfig>
            <IpsecLifetime>86400</IpsecLifetime>
            <IpsecAuthAlg>sha1</IpsecAuthAlg>
            <IpsecPfs>group2</IpsecPfs>
            <IpsecEncAlg>aes</IpsecEncAlg>
      </IpsecConfig>
      <EffectImmediately>false</EffectImmediately>
      <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
      <CreateTime>1492753817000</CreateTime>
      <VpnConnectionId>vco-bp10lz7aejumd2vxo****</VpnConnectionId>
      <RequestId>57070A3D-38F2-40A6-A1C9-DB14542EF54D</RequestId>
      <LocalSubnet>10.1.1.0/24,10.1.2.0/24</LocalSubnet>
      <IkeConfig>
            <IkeEncAlg>aes</IkeEncAlg>
            <RemoteId>139.XX.XX.32</RemoteId>
            <IkePfs>group2</IkePfs>
            <IkeAuthAlg>sha1</IkeAuthAlg>
            <Psk>pgw6dy7d1i8i****</Psk>
            <IkeMode>main</IkeMode>
            <IkeLifetime>86400</IkeLifetime>
            <IkeVersion>ikev1</IkeVersion>
            <LocalId>116.XX.XX.69</LocalId>
      </IkeConfig>
</ModifyVpnConnectionAttributeResponse>
```

`JSON` format `{`

```json
    "Name": "vpn",
    "CustomerGatewayId": "cgw-bp1pvpl9r9adju6l5****",
    "RemoteSubnet": "172.16.2.0/24",
    "IpsecConfig": {
        "IpsecLifetime": 86400,
        "IpsecAuthAlg": "sha1",
        "IpsecPfs": "group2",
        "IpsecEncAlg": "aes"
```

`},`

```json
    "EffectImmediately": false,
    "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
    "CreateTime": 1492753817000,
    "VpnConnectionId": "vco-bp10lz7aejumd2vxo****",
    "RequestId": "7DB79D0C-5F27-4AB5-995B-79BE55102F90",
    "LocalSubnet": "10.1.1.0/24,10.1.2.0/24",
    "IkeConfig": {
        "IkeEncAlg": "aes",
        "RemoteId": "139.XX.XX.32",
        "IkePfs": "group2",
        "IkeAuthAlg": "sha1",
        "Psk": "pgw6dy7d1i8i****",
        "IkeMode": "main",
        "IkeLifetime": 86400,
        "IkeVersion": "ikev1",
        "LocalId": "116.XX.XX.69"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidVpnConnectionIns tanceId.NotFound | The specified vpn connection instance id does not exist. | The error message returned because the specified IPsec-VPN connection does not exist. You can check whether the configuration of the connection is valid. |
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.FinancialLo cked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

| Virtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidName | The name is not valid | The error message returned because the specified name is in an invalid format. |

#### SSL-VPN

##### CreateSslVpnServer

Creates an SSL-VPN server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSslVpnServer | The operation that you want to perform. Set the value to Creat eSslVpnServer. |
| ClientIpPool | String | Yes | 192.168.1.0/24 | The CIDR block that is allocated to the virtual network interface of the client. It is not the CIDR block where the client resides. When the client accesses the server through an SSL-VPN connection, the VPN gateway selects an IP address from the specified CIDR block and assigns it to the client. This CIDR block must not conflict with the value of LocalSubnet . |
| LocalSubnet | String | Yes | 10.0.0.0/8 | The CIDR block to be accessed by the client through the SSL-VPN connection. You can set the value to the CIDR block of a VPC, a vSwitch, a data center that is connected to the VPC through an Express Connect circuit, or an Alibaba Cloud service, such as ApsaraDB RDS or OSS. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the VPN gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1hgim8by0kc9ng a**** | The ID of the VPN gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | sslvpnname | The name of the SSL-VPN server. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter, but cannot start with http:// or https:// . |
| Proto | String | No | UDP | The protocol that is used by the SSL-VPN server. Valid values: T CP: TCP. UDP : UDP. This is the default value. |
| Cipher | String | No | AES-128-CBC | The encryption algorithm that is used in the SSL-VPN connection. Valid values: AES-128-CBC: the AES-128-CBC algorithm. This is the default value. AES-192-CBC: the AES-192-CBC algorithm. AES-256-CBC: the AES-256-CBC algorithm. none: If the parameter is set to this value, no encryption algorithm is used. |
| Port | Integer | No | 1194 | The port that is used by the SSL-VPN server. Default value: 1194. The following ports cannot be used: 22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, and 4500. |
| Compress | Boolean | No | false | Specifies whether to enable data compression. Valid values: t rue: enables data compression. f alse: disables data compression. This is the default value. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | test | The name of the SSL-VPN server. |

| Virtual Private Clou | d |   | Developer Guide·API reference |
|---|---|---|---|
| Parameter | Type | Example | Description |

| RequestId | String | E98A9651-7098-40C7- 8F85-C818D1EBBA85 | The ID of the request. |
|---|---|---|---|
| SslVpnServerId | String | vss- bp18q7hzj6largv4v**** | The ID of the SSL-VPN server. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateSslVpnServer &ClientIpPool=192.168.1.0/24 &LocalSubnet=10.0.0.0/8 &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1hgim8by0kc9nga**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateSslVpnServerResponse>
      <RequestId>E98A9651-7098-40C7-8F85-C818D1EBBA85</RequestId>
      <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId>
      <Name>test</Name>
</CreateSslVpnServerResponse>
```

`JSON` format `{`

```json
    "RequestId": "E98A9651-7098-40C7-8F85-C818D1EBBA85",
    "SslVpnServerId": "vss-bp18q7hzj6largv4v****",
    "Name": "test"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |

| Developer Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidName | The name is not valid | The error message returned because the format of the specified name is invalid. |
| 404 | InvalidVpnGatewayInsta nceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.FinancialLo cked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

##### DeleteSslVpnServer

Deletes an SSL-VPN server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSslVpnServer | The operation that you want to perform. Set the value to Delet eSslVpnServer. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the SSL-VPN server is created. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | Yes | vss- bp18q7hzj6largv4v* *** | The ID of the SSL-VPN server. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D-48FE- 8316-ACA81BB230DA | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteSslVpnServer &RegionId=cn-qingdao-env66-d01 &SslVpnServerId=vss-bp18q7hzj6largv4v**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteSslVpnServerResponse>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteSslVpnServerResponse>
```

`JSON` format `{`

```json
  "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.FinancialLo cked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

##### ModifySslVpnServer

Modifies the configuration of an SSL-VPN server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySslVpnServer | The operation that you want to perform. Set the value to Modif ySslVpnServer. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the VPN gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | Yes | vss- bp18q7hzj6largv4v* *** | The ID of the SSL-VPN server. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | test | The name of the SSL-VPN server. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter, and cannot start with http:// or https:// . |
| ClientIpPool | String | No | 10.30.30.0/24 | The client IP address pool. |
| LocalSubnet | String | No | 10.20.20.0/24 | The CIDR block of the VPC. |
| Proto | String | No | UDP | The protocol that is used by the SSL-VPN server. Valid values: T CP: TCP UDP: UDP. This is the default value. |
| Cipher | String | No | AES-128-CBC | The encryption algorithm that is used in the SSL-VPN connection. Valid values: AES-128-CBC: the AES-128-CBC algorithm. This is the default value. AES-192-CBC: the AES-192-CBC algorithm. AES-256-CBC: the AES-256-CBC algorithm. none: If the parameter is set to this value, no encryption algorithm is used. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Port | Integer | No | 1194 | The port that is used by the SSL-VPN server. Default value: 1194. The following ports cannot be used: 22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, and 4500. |
| Compress | Boolean | No | false | Specifies whether to enable data compression. Valid values: t rue: enables data compression. f alse: disables data compression. This is the default value. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Cipher | String | AES-128-CBC | The encryption algorithm. |
| ClientIpPool | String | 10.30.30.0/24 | The client IP address pool. |
| Compress | Boolean | false | Indicates whether data compression is enabled. |
| Connections | Integer | 0 | The total number of current connections. |
| CreateTime | Long | 1492753580000 | The time when the SSL-VPN server was created. |
| InternetIp | String | 47.XX.XX.98 | The public IP address. |
| LocalSubnet | String | 10.20.20.0/24 | The CIDR block of the VPC. |
| MaxConnections | Integer | 5 | The maximum number of connections. |
| Name | String | test | The name of the SSL-VPN server. |
| Port | Integer | 1194 | The port that is used by the SSL-VPN server. |
| Proto | String | UDP | The protocol that is used by the SSL-VPN server. |
| RegionId | String | cn-qingdao-env66-d01 | The region ID of the SSL-VPN server. |
| RequestId | String | DF11D6F6-E35A-41C3- 9B20-6FC8A901FE65 | The ID of the request. |

|   | Developer Guide·AP | I reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| SslVpnServerId | String | vss- bp18q7hzj6largv4v**** | The ID of the SSL-VPN server. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2ogj*** * | The ID of the VPN gateway. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifySslVpnServer &RegionId=cn-qingdao-env66-d01 &SslVpnServerId=vss-bp18q7hzj6largv4v**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifySslVpnServerResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <SslVpnServers>
            <SslVpnServer>
                  <RegionId>cn-qingdao-env66-d01</RegionId>
                  <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId>
                  <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
                  <Name>test</Name>
                  <CLientIpPool>10.30.30.0/24</CLientIpPool>
                  <LocalSubnet>10.20.20.0/24</LocalSubnet>
                  <Proto>UDP</Proto>
                  <Port>1194</Port>
                  <Cipher>AES-128-CBC</Cipher>
                  <Compress>true</Compress>
                  <CreateTime>1492753580000</CreateTime>
                  <Connections>0</Connections>
                  <MaxConnections>5</MaxConnections>
                  <InternetIp>47.XX.XX.98</InternetIp>
            </SslVpnServer>
      </SslVpnServers>
      <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId>
</ModifySslVpnServerResponse>
```

`JSON` format `{`

```json
    "PageNumber": "1",
    "TotalCount": "1",
    "PageSize": "10",
    "SslVpnServers": {
        "SslVpnServer": {
            "RegionId": "cn-qingdao-env66-d01",
            "SslVpnServerId": "vss-bp18q7hzj6largv4v****",
            "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
            "Name": "test",
            "CLientIpPool": "10.30.30.0/24",
            "LocalSubnet": "10.20.20.0/24",
            "Proto": "UDP",
            "Port": "1194",
            "Cipher": "AES-128-CBC",
            "Compress": "true",
            "CreateTime": "1492753580000",
            "Connections": "0",
            "MaxConnections": "5",
            "InternetIp": "47.XX.XX.98"
```

`},`

```json
    "RequestId": "DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | InvalidName | The name is not valid | The error message returned because the specified name is in an invalid format. |
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.FinancialLo cked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

##### DeleteSslVpnClientCert

Deletes an SSL-VPN client certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSslVpnClientC ert | The operation that you want to perform. Set the value to Delet eSslVpnClient Cert . |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the SSL-VPN client certificate is created. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnClientCertId | String | Yes | vsc- bp1n8wcf134yl0osr* *** | The ID of the SSL-VPN client certificate. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D-48FE- 8316-ACA81BB230DA | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteSslVpnClientCert &RegionId=cn-qingdao-env66-d01 &SslVpnClientCertId=vsc-bp1n8wcf134yl0osr**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteSslVpnClientCertResponse>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteSslVpnClientCertResponse>
```

`JSON` format `{`

```json
  "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |

##### ModifySslVpnClientCert

Modifies the name of an SSL-VPN client certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySslVpnClientC ert | The operation that you want to perform. Set the value to Modif ySslVpnClient Cert . |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the SSL-VPN client certificate is created. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnClientCertId | String | Yes | vsc- bp1n8wcf134yl0osr c**** | The ID of the SSL-VPN client certificate. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Name | String | No | cert2 | The name of the SSL-VPN client certificate. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter. However, the name cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | cert2 | The name of the SSL-VPN client certificate. |
| RequestId | String | 606998F0-B94D-48FE- 8316-ACA81BB230DA | The ID of the request. |
| SslVpnClientCertId | String | vsc- bp1n8wcf134yl0osr**** | The ID of the SSL-VPN client certificate. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifySslVpnClientCert &RegionId=cn-qingdao-env66-d01 &SslVpnClientCertId=vsc-bp1n8wcf134yl0osrc**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifySslVpnClientCertResponse>
      <SslVpnClientCertId>vsc-bp1n8wcf134yl0osr****</SslVpnClientCertId>
      <Name>cert2</Name>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</ModifySslVpnClientCertResponse>
```

`JSON` format `{`

```json
    "SslVpnClientCertId": "vsc-bp1n8wcf134yl0osr****",
    "Name": "cert2",
    "RequestId": "606998F0-B94D-48FE-8316-ACA81BB230DA"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | InvalidName | The name is not valid | The error message returned because the specified name is in an invalid format. |

##### CreateSslVpnClientCert

Creates an SSL-VPN client certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSslVpnClientC ert | The operation that you want to perform. Set the value to Creat eSslVpnClient Cert . |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the VPN gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | Yes | vss- m5et0q3iy1qex328 w**** | The ID of the SSL-VPN server. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | SslVpnClientCert1 | The name of the SSL-VPN client certificate. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter, and cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | SslVpnClientCert | The name of the SSL-VPN client certificate. |
| RequestId | String | 079874CD-AEC1-43E6- AC03-ADD96B6E4907 | The ID of the request. |
| SslVpnClientCertId | String | vsc- m5euof6s5jy8vs5kd**** | The ID of the SSL-VPN client certificate. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateSslVpnClientCert &RegionId=cn-qingdao-env66-d01 &SslVpnServerId=vss-m5et0q3iy1qex328w**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateSslVpnClientCertResponse>
      <SslVpnClientCertId>vsc-bp1n8wcf134yl0osr****</SslVpnClientCertId>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</CreateSslVpnClientCertResponse>
```

`JSON` format `{`

```json
    "SslVpnClientCertId": "vsc-bp1n8wcf134yl0osr****",
    "RequestId": "606998F0-B94D-48FE-8316-ACA81BB230DA"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | VpnGateway.Configurin g | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.FinancialLo cked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |
| 400 | InvalidName | The name is not valid | The error message returned because the specified name is in an invalid format. |

##### DescribeSslVpnClientCerts

Queries one or more SSL-VPN client certificates. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSslVpnClien tCerts | The operation that you want to perform. Set the value to DescribeSslVpnClient Cert s. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the SSL-VPN client certificates to be queried. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | No | vss- bp18q7hzj6largv4v* *** | The ID of the SSL-VPN server. |
| SslVpnClientCertId | String | No | vsc- bp1n8wcf134yl0osr* *** | The ID of the SSL-VPN client certificate. |
| Name | String | No | cert1 | The name of the SSL-VPN client certificate. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The ID of the request. |
| SslVpnClientCertK eys | Array of SslVpnClientCertK ey |   | The detailed information about the queried SSL client certificates. |
| SslVpnClientCertK ey |   |   |   |
| CreateTime | Long | 1492747187000 | The timestamp generated when the SSL client certificate was created. |
| EndTime | Long | 1494966335000 | The time to be generated when the SSL client certificate expires. |
| Name | String | cert1 | The name of the SSL-VPN client certificate. |
| RegionId | String | cn-qingdao-env66-d01 | The region ID of the SSL-VPN client certificate. |
| SslVpnClientCertId | String | vsc- bp1n8wcf134yl0osr**** | The ID of the SSL-VPN client certificate. |
| SslVpnServerId | String | vss- bp18q7hzj6largv4v**** | The ID of the SSL-VPN server. |
| Status | String | normal | The status of the SSL-VPN client certificate. Valid values: expiring-soon: The SSL-VPN client certificate expires in one week. normal: The certificate is normal. expired: The certificate has expired. |
| TotalCount | Integer | 1 | The number of returned entries. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSslVpnClientCerts &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSslVpnServersResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <SslVpnServers>
            <SslVpnServer>
                  <RegionId>cn-qingdao-env66-d01</RegionId>
                  <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId>
                  <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
                  <Name>test</Name>
                  <CLientIpPool>10.10.20.0/24</CLientIpPool>
                  <LocalSubnet>10.10.10.0/24</LocalSubnet>
                  <Proto>UDP</Proto>
                  <Port>1194</Port>
                  <Cipher>AES-128-CBC</Cipher>
                  <Compress>true</Compress>
                  <CreateTime>1492753580000</CreateTime>
                  <Connections>0</Connections>
                  <MaxConnections>5</MaxConnections>
                  <InternetIp>47.XX.XX.98</InternetIp>
            </SslVpnServer>
      </SslVpnServers>
      <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId>
</DescribeSslVpnServersResponse>
```

`JSON` format `{`

```json
    "DescribeSslVpnServersResponse": {
        "PageNumber": "1",
        "TotalCount": "1",
        "PageSize": "10",
        "SslVpnServers": {
            "SslVpnServer": {
                "RegionId": "cn-qingdao-env66-d01",
                "SslVpnServerId": "vss-bp18q7hzj6largv4v****",
                "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
                "Name": "test",
                "CLientIpPool": "10.10.20.0/24",
                "LocalSubnet": "10.10.10.0/24",
                "Proto": "UDP",
                "Port": "1194",
                "Cipher": "AES-128-CBC",
                "Compress": "true",
                "CreateTime": "1492753580000",
                "Connections": "0",
                "MaxConnections": "5",
                "InternetIp": "47.XX.XX.98"
```

`},`

```json
        "RequestId": "DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

##### DescribeSslVpnClientCert

Queries a specified SSL-VPN client certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSslVpnClien tCert | The operation that you want to perform. Set the value to DescribeSslVpnClient Cert . |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the SSL-VPN client certificate that you want to query is created. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnClientCertId | String | Yes | vsc- bp17r58rjf5r1gjyr*** * | The ID of the SSL-VPN client certificate that you want to query. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CaCert | String | The CA certificate | The CA certificate. |
| ClientCert | String | The SSL-VPN client certificate | The SSL-VPN client certificate. |
| ClientConfig | String | The configuration of the client | The configuration of the client. |
| ClientKey | String | The key of the client | The key of the client. |
| CreateTime | Long | 1552550980000 | The timestamp generated when the SSL-VPN client certificate was created. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EndTime | Long | 1647158980000 | The timestamp to be generated when the SSL-VPN client certificate expires. |
| Name | String | abc | The name of the SSL-VPN client certificate. |
| RegionId | String | cn-qingdao-env66-d01 | The ID of the region where the SSL-VPN client certificate is created. |
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The ID of the request. |
| SslVpnClientCertId | String | vsc- bp13k5mp4tg8v3z9b** ** | The ID of the SSL-VPN client certificate. |
| SslVpnServerId | String | vss- bp155e9yclsg1xgq4**** | The ID of the SSL-VPN server. |
| Status | String | normal | The status of the SSL-VPN client certificate. Valid values: expiring-soon: The SSL-VPN client certificate expires in one week. normal: The certificate is normal. expired: The certificate has expired. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSslVpnClientCert &RegionId=cn-qingdao-env66-d01 &SslVpnClientCertId=vsc-bp17r58rjf5r1gjyr**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSslVpnServersResponse>
      <Name>df</Name>
      <Status>normal</Status>
      <ClientConfig>****</ClientConfig>
      <ClientCert>****</ClientCert>
      <CreateTime>1552550980000</CreateTime>
      <RegionId>cn-qingdao-env66-d01</RegionId>
      <RequestId>49D54005-6E0E-4132-B305-F3A24DEDDDC9</RequestId>
      <EndTime>1647158980000</EndTime>
      <SslVpnClientCertId>vsc-bp13k5mp4tg8v3z9b****</SslVpnClientCertId>
      <ClientKey>****</ClientKey>
      <CaCert>****</CaCert>
      <SslVpnServerId>vss-bp155e9yclsg1xgq4****</SslVpnServerId>
</DescribeSslVpnServersResponse>
```

`JSON` format `{`

```json
 "Name": "df",
 "Status": "normal",
 "ClientConfig": "****",
 "ClientCert": "****",
 "CreateTime": 1552550980000,
 "RegionId": "cn-qingdao-env66-d01",
 "RequestId": "49D54005-6E0E-4132-B305-F3A24DEDDDC9",
 "EndTime": 1647158980000,
 "SslVpnClientCertId": "vsc-bp13k5mp4tg8v3z9b****",
 "ClientKey": "****",
 "CaCert": "****",
 "SslVpnServerId": "vss-bp155e9yclsg1xgq4****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

##### DescribeSslVpnServers

Queries one or more SSL-VPN servers. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSslVpnServe rs | The operation that you want to perform. Set the value to DescribeSslVpnServers. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the SSL-VPN servers are created. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | No | vss- bp15j3du13gq1dgey **** | The ID of the SSL-VPN server. |

| Virtual Private Cloud |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpnGatewayId | String | No | vpn- bp1on0xae9d771ggi **** | The ID of the VPN gateway. |
| Name | String | No | test | The name of the SSL-VPN server. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned on each page. |
| RequestId | String | 085CA5EA-1E76-43A8- 981B-E0208DECA0CB | The ID of the request. |
| SslVpnServers | Array of SslVpnServer |   | The detailed information about the SSL-VPN servers. |
| SslVpnServer |   |   |   |
| Cipher | String | AES-128-CBC | The encryption algorithm. |
| ClientIpPool | String | 10.10.1.0/24 | The client IP address pool. |
| Compress | Boolean | false | Indicates whether the transmitted data is compressed. |
| Connections | Integer | 0 | The total number of current connections. |
| CreateTime | Long | 1544668844000 | The timestamp generated when the SSL-VPN server was created. |
| InternetIp | String | 47.XX.XX.167 | The public IP address. |
| LocalSubnet | String | 192.168.0.0/24 | The CIDR block of the client. |
| MaxConnections | Integer | 5 | The maximum number of connections. |

|   | Developer Guide·AP | I reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | test | The name of the SSL-VPN server. |
| Port | Integer | 1194 | The port that is used by the SSL-VPN server. |
| Proto | String | UDP | The protocol that is used by the SSL-VPN server. |
| RegionId | String | cn-qingdao-env66-d01 | The ID of the region where the SSL-VPN server is created. |
| SslVpnServerId | String | vss- bp15j3du13gq1dgey*** * | The ID of the SSL-VPN server. |
| VpnGatewayId | String | vpn- bp1on0xae9d771ggi*** * | The ID of the VPN gateway. |
| TotalCount | Integer | 1 | The total number of entries returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSslVpnServers &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSslVpnServersResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <SslVpnServers>
            <SslVpnServer>
                  <RegionId>cn-qingdao-env66-d01</RegionId>
                  <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId>
                  <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
                  <Name>test</Name>
                  <CLientIpPool>10.10.10.0/24</CLientIpPool>
                  <LocalSubnet>10.10.20.0/24</LocalSubnet>
                  <Proto>UDP</Proto>
                  <Port>1194</Port>
                  <Cipher>AES-128-CBC</Cipher>
                  <Compress>true</Compress>
                  <CreateTime>1492753580000</CreateTime>
                  <Connections>0</Connections>
                  <MaxConnections>5</MaxConnections>
                  <InternetIp>47.XX.XX.167</InternetIp>
            </SslVpnServer>
      </SslVpnServers>
      <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId>
</DescribeSslVpnServersResponse>
```

`JSON` format `{`

```json
    "PageNumber": "1",
    "TotalCount": "1",
    "PageSize": "10",
    "SslVpnServers": {
        "SslVpnServer": {
            "RegionId": "cn-qingdao-env66-d01",
            "SslVpnServerId": "vss-bp18q7hzj6largv4v****",
            "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
            "Name": "test",
            "CLientIpPool": "10.10.10.0/24",
            "LocalSubnet": "10.10.20.0/24",
            "Proto": "UDP",
            "Port": "1194",
            "Cipher": "AES-128-CBC",
            "Compress": "true",
            "CreateTime": "1492753580000",
            "Connections": "0",
            "MaxConnections": "5",
            "InternetIp": "47.XX.XX.167"
```

`},`

```json
    "RequestId": "DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

##### DescribeVpnSslServerLogs

Queries the logs of an SSL-VPN server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnSslServe rLogs | The operation that you want to perform. Set the value to DescribeVpnSslServerLogs. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the SSL-VPN server is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnSslServerId | String | Yes | vss- bp155e9yclsg1xgq4 **** | The name of the SSL-VPN server. |
| From | Integer | No | 2018020201 | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. If the From parameter is set, you must set the T o or Minut ePeriod parameter. |
| To | Integer | No | 2018020206 | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. If the From parameter is set, you must set the T o or Minut ePeriod parameter. |
| MinutePeriod | Integer | No | 10 | The cycle of the logs. If the From and T o parameters are not set, you must set the Minut ePeriod parameter. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |

| Virtual Private Cloud |   |   |   | Developer Guide·API reference |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The number of log entries. |
| Data | List | test | An array of log entries. Each item in the array indicates a log entry. |
| IsCompleted | Boolean | true | Indicates whether the log data is accurate. Valid values: t rue: accurate f alse: inaccurate |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 1 | The number of entries returned per page. |
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpnSslServerLogs &RegionId=cn-qingdao-env66-d01 &VpnSslServerId=vss-bp155e9yclsg1xgq4**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpnSslServerLogsResponse>
   <Data></Data>
   <PageNumber>1</PageNumber>
   <Count>0</Count>
   <PageSize>10</PageSize>
   <IsCompleted>true</IsCompleted>
   <RequestId>26641E42-66C7-4942-9FEC-F99213914F8F</RequestId>
</DescribeVpnSslServerLogsResponse>
```

`JSON` format `{`

```json
 "Data": {
  "Logs": []
```

`},`

```json
 "PageNumber": 1,
 "Count": 0,
 "PageSize": 10,
 "IsCompleted": true,
 "RequestId": "26641E42-66C7-4942-9FEC-F99213914F8F"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

### NAT gateways

#### CreateNatGateway

Creates a NAT gateway. Descriptions When you call this operation, take note of the following items: You cannot deploy a NAT gateway and a user-created SNAT gateway in the same virtual private cloud (VPC) if the SNAT gateway is an Elastic Compute Service (ECS) instance. After a NAT gateway is created, a route entry is automatically added to the route table of the VPC. The destination CIDR block of the route entry is 0.0.0.0/0 and the next hop of the route entry is the NAT gateway. The route entry ensures that traffic is routed to the NAT gateway. If the route table of the VPC already contains a route entry whose destination CIDR block is 0.0.0.0/0, delete the route entry. Otherwise, you cannot create a NAT gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateNatGateway | The operation that you want to perform. Set the value to Creat eNat Gat eway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- bp1di7uewzmtvfuq 8**** | The ID of the VPC. |
| Name | String | No | fortest | The name of the NAT gateway. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter and cannot start with http:// or https:// . If you do not specify this parameter, the ID of the NAT gateway is used by default. |
| Description | String | No | testnat | The description of the NAT gateway. The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . |
| ClientToken | String | No | shefffxxddjehfh**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Spec | String | No | Small | The size of the NAT gateway. Valid values: Small(default): small Middle: middle Large: large XLarge.1: super large |
| BandwidthPackage. N.IpCount | Integer | No | 5 | The number of public IP addresses in the NAT service plan. Valid values: 1 to 50. N indicates the sequence number of the NAT service plan. Valid values: 1 to 4. |
| BandwidthPackage. N.Bandwidth | Integer | No | 5 | The bandwidth limit of NAT service plan N. Unit: Mbit/s. Valid values: 5 to 5000. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BandwidthPackage. N.Zone | String | No | cn-neimeng-env133- d01 | The zone of NAT service plan N. If you do not set this parameter, the service plan is randomly allocated to a zone. Even if the IP addresses of the NAT service plan and the backend ECS instances belong to different zones, the ECS instances can still connect to the NAT gateway. However, you can reduce the network latency by allocating the NAT service plan to the zone where your ECS instances are deployed. |
| BandwidthPackage. N.ISP | String | No | BGP | By default, the type of Internet Service Provider (ISP) line of NAT service plan N is BGP (Multi-ISP). |
| BandwidthPackage. N.InternetChargeTyp e | String | No | 95 | Specifies the billing method of the NAT service plan. |
| InstanceChargeType | String | No | PostPaid | The billing method. Valid values: PrePaid: subscription Post Paid (default): pay-as-you-go |
| PricingCycle | String | No | Month | The billing cycle of a subscription NAT service plan. Valid values: Mont h (default): The NAT service plan is billed on a monthly basis. Year: The NAT service plan is billed on an annual basis. This parameter is required if Inst anceChargeT ype is set to PrePaid. This parameter is optional if Inst anceChargeT ype is set to Post Paid. |
| Duration | String | No | 1 | The subscription duration. If PricingCycle is set to Mont h, set Period to a value from 1 t o 9. If PricingCycle is set to Year, set Period to a value from 1 t o 3. This parameter is required when Inst anceChargeT ype is set to PrePaid. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AutoPay | Boolean | No | false | Specifies whether to enable automatic payment. Valid values: f alse: disables automatic payment. After an order is generated, you must go to the Order Center to make the payment. t rue: enables automatic payment. Payments are automatically made. This parameter is required when Inst anceChargeT ype is set to PrePaid. This parameter is optional when Inst anceChargeT ype is set to Post Paid. |
| VSwitchId | String | No | vsw- n2yf2tj1k2bfey5pq** ** | The ID of the vSwitch. |
| NatType | String | No | Normal | The type of the NAT gateway. |
| InternetChargeType | String | No | PayByLcu | The metering method of the NAT gateway. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NatGatewayId | String | ngw-112za33e4**** | The ID of the NAT gateway. The ID is a unique identifier that is automatically generated by the system. |
| ForwardTableIds | List | ftb-11tc6xgmv**** | The list of DNAT entries. |
| BandwidthPackag eIds | List | bwp-11odxu2k7**** | The list of NAT service plans. |
| RequestId | String | 2315DEB7-5E92-423A- 91F7-4C1EC9AD97C3 | The ID of the request. |
| SnatTableIds | List | stb-SnatTableIds**** | The list of SNAT entries. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=CreateNatGateway &RegionId=cn-hangzhou &VpcId= vpc-bp1di7uewzmtvfuq8**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateNatGatewayResponse>
    <BandwidthPackageIds>
  </BandwidthPackageIds>
    <RequestId>7C01CA72-73FD-4056-B16A-42E392D47625</RequestId>
    <SnatTableIds>
          <SnatTableId>stb-wz9aq9mec6f843j45****</SnatTableId>
    </SnatTableIds>
    <ForwardTableIds>
          <ForwardTableId>ftb-wz9sl3znmxhy605f8****</ForwardTableId>
    </ForwardTableIds>
    <NatGatewayId>ngw-wz95lh0c2wj9b6r1z****</NatGatewayId>
</CreateNatGatewayResponse>
```

`JSON` format `{`

```json
    "BandwidthPackageIds": {
        "BandwidthPackageId": []
```

`},`

```json
    "RequestId": "7C01CA72-73FD-4056-B16A-42E392D47625",
    "SnatTableIds": {
        "SnatTableId": [
            "stb-wz9aq9mec6f843j45****"
```

`]` `},`

```json
    "ForwardTableIds": {
        "ForwardTableId": [
            "ftb-wz9sl3znmxhy605f8****"
```

`]` `},`

```json
    "NatGatewayId": "ngw-wz95lh0c2wj9b6r1z****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidVPCStatus | vpc incorrect status. | The error message returned because the operation is not supported when the VPC is in the current state. Check whether the status of the VPC is valid. |
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | InvalidNatGatewayNam e.MalFormed | NatGateway name is not valid. | The error message returned because the specified gateway name is invalid. |
| 400 | InvalidNatGatewayDescr iption.MalFormed | NatGateway description is not valid. | The error message returned because the description of the specified gateway is invalid. |
| 400 | MissingParameter.Band widthPackage | only support one BandwidthPackage be created with NatGateway. | The error message returned because no NAT service plan is specified. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVpcId.NotFound | Specified value of VpcId is not found in our record. | The error message returned because the specified VPC does not exist. Check whether the specified VPC is valid. |
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because the required parameters are not set. Check whether you have set all the required parameters before you call this operation. |
| 404 | InvalidZoneId.NotFound | Specified value of ZoneId is not exists. | The error message returned because the specified zone does not exist. |
| 404 | InvalidZoneId.NotFound | Can not find ZoneId for allocated ip. | The error message returned because the zone of the specified IP address is invalid. |
| 400 | QuotaExceeded.Bandwi dthPackageIps | The specified ipCount exceeded quota. | The error message returned because the number of IP addresses has reached the upper limit. Go to the Quota Management page and request a quota increase. |
| 400 | InvalidParameter.Name. Malformed | The specified Name is not valid. | The error message returned because the specified name is invalid. Enter the name in the correct format. |
| 400 | InvalidParameter.Descri ption.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |
| 400 | ZONE NO AVAILABLE IP _ _ _ | The Zone have no available ip. | The error message returned because no IP addresses are available in the zone. |
| 400 | InvalidParameter.Bandw idthPackage.n.ISP.Value NotSupport | The specified ISP of BandwidthPackage is not valid. | The error message returned because the specified ISP of the NAT service plan is invalid. |
| 400 | InvalidNatGatewayId.No tFound | The NatGatewayId not exist. | The error message returned because the specified NAT gateway ID does not exist. Check whether the NAT gateway ID is valid. |
| 400 | VswitchStatusError | The VSwitch is creating . | The error message returned because the operation is not supported when the system is creating the vSwitch. |
| 400 | VpcStatusError | The Vpc is creating . | The error message returned because the operation is not supported when the system is creating the VPC. |
| 400 | InvalidParameter.Spec.V alueNotSupported | The specified Spec is not valid. | The error message returned because the specified gateway size is invalid. |
| 400 | Forbidden.CheckEntryRu leQuota | Route entry quota rule check error. | The error message returned because an error occurs when the system checks the quota of route entries. |

#### ModifyNatGatewayAttribute

Modifies the name and description of a NAT gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNatGatewayA ttribute | The operation that you want to perform. Set the value to Modif yNat Gat ewayAt t ribut e. |
| NatGatewayId | String | Yes | ngw- 2ze0dcn4mq31qx2jc **** | The ID of the NAT gateway that you want to modify. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | nat123 | The name of the NAT gateway that you want to modify. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter. The name cannot start with http:// or https:// . Not e You must specify at least one of the following parameters: Name and Descript ion. |
| Description | String | No | fortest | The description of the NAT gateway. The description must be 2 to 256 characters in length, and must start with a letter. It cannot start with http:// or https:// . Not e You must specify at least one of the following parameters: Name and Descript ion. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | AB5F62CF-2B60-4458- A756-42C9DFE108D1 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyNatGatewayAttribute &NatGatewayId=ngw-2ze0dcn4mq31qx2jc**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyNatGatewayAttributeResponse>
  <RequestId>AB5F62CF-2B60-4458-A756-42C9DFE108D1</RequestId>
</ModifyNatGatewayAttributeResponse>
```

`JSON` format

```json
{"RequestId":"AB5F62CF-2B60-4458-A756-42C9DFE108D1"}
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidNatGatewayId.No tFound | The specified NatGatewayId does not exist in our records. | The error message returned because the specified NAT gateway ID does not exist. Check whether the NAT gateway ID is valid. |
| 400 | InvalidParameter.Name. Malformed | The specified Name is not valid. | The error message returned because the specified name is invalid. |
| 400 | InvalidParameter.Descri ption.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |

#### ModifyNatGatewaySpec

Resizes a NAT gateway. NAT gateways are available in different sizes. The size of a NAT gateway determines the Source Network Address Translation (SNAT) performance of the gateway, such as the maximum number of connections and the number of new connections per second. However, the data throughput is not affected. The following table describes the correlations between different sizes of NAT gateways and SNAT performance metrics.

| Size | Maximum connection | Number of new connections per second |
|---|---|---|
| Small | 10,000 | 1,000 |
| Medium | 50,000 | 5,000 |

| Developer Guide·API reference |   | Virtual Private Clou |
|---|---|---|

| Size | Maximum connection | Number of new connections per second |
|---|---|---|
| Large | 200,000 | 10,000 |

Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNatGatewayS pec | The operation that you want to perform. Set the value to Modif yNat Gat ewaySpec. |
| NatGatewayId | String | Yes | ngw- bp1uewa15k4iy5770 **** | The ID of the NAT gateway. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the NAT gateway is deployed. |
| Spec | String | Yes | Small | The size of the NAT gateway. Valid values: Small: a small-sized NAT gateway Middle: a middle-sized NAT gateway Large: a large-sized NAT gateway |
| AutoPay | Boolean | No | false | Specifies whether to enable automatic payment. Valid values: t rue: enables automatic payment. f alse: disables automatic payment. This is the default value. |
| ClientToken | String | No | SHA234js121223**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters, and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DBD4E4A2-786E-4BD2- 8EB6-107FFC2B5B7D | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyNatGatewaySpec &NatGatewayId=ngw-bp1uewa15k4iy5770**** &RegionId=cn-qingdao-env17-d01 &Spec=Small &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyNatGatewaySpecResponse>
      <RequestId>DBD4E4A2-786E-4BD2-8EB6-107FFC2B5B7D</RequestId>
</ModifyNatGatewaySpecResponse>
```

`JSON` format `{`

```json
    "RequestId":"DBD4E4A2-786E-4BD2-8EB6-107FFC2B5B7D"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidNatGatewayId.No tFound | The specified NatGatewayId does not exist in our records. | The error message returned because the specified NAT gateway ID does not exist. Check whether the NAT gateway ID is valid. |
| 400 | NATGW MODIFY SPEC S _ _ _ AME | The specified Spec is same with now. | The error message returned because the specified gateway size is the same as the current one. |
| 400 | InvalidParameter.Spec.V alueNotSupported | The specified Spec is not valid. | The error message returned because the specified gateway size is invalid. |

#### DeleteNatGateway

Deletes a specified NAT gateway. Not e Before you delete a NAT gateway, you must disassociate NAT service plans from the NAT gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteNatGateway | The operation that you want to perform. Set the value to Delet eNat Gat eway. |
| NatGatewayId | String | Yes | ngw- bp1uewa15k4iy5770 **** | The ID of the NAT gateway. |

|   | Developer Guide·API r | eference |   |   | Virtual Private Clou | d |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| Force | Boolean | No | false | Specifies whether to forcibly delete the NAT gateway. Valid values: t rue: forcibly deletes the NAT gateway. f alse: does not forcibly delete the NAT gateway. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteNatGateway &NatGatewayId=ngw-bp1uewa15k4iy5770**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteNatGatewayResponse>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
</DeleteNatGatewayResponse>
```

`JSON` format `{`

```json
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidNatGatewayId.No tFound | The specified NatGatewayId does not exist in our records. | The error message returned because the specified NAT gateway ID does not exist. Check whether the NAT gateway ID is valid. |

|   | Virtual Private | Cloud |   | Developer Guide·API reference |   |
|---|---|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | DependencyViolation.Ba ndwidthPackages | There are BandwidthPackages on specified NatGateway not deleted. | The error message returned because one or more NAT service plans are associated with the NAT gateway. Disassociate all NAT service plans from the NAT gateway and try again. |

#### DescribeNatGateways

Queries NAT gateways. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeNatGatewa ys | The operation that you want to perform. Set the value to DescribeNat Gat eways. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the NAT gateways are deployed. You can call the DescribeRegions operation to query the most recent region list. |
| NatGatewayId | String | No | ngw- bp1uewa15k4iy5770 **** | The ID of the NAT gateway. |
| VpcId | String | No | vpc- bp15zckdt37pq72z* *** | The ID of the virtual private cloud (VPC). |
| Name | String | No | test | The name of the NAT gateway. |
| InstanceChargeType | String | No | PostPaid | The billing method of the NAT gateway. Valid values: Post Paid: pay-as-you-go PrePaid: subscription |
| Spec | String | No | Large | The size of the NAT gateway. Valid values: Small: small Middle: middle Large: large XLarge.1: super large |
| NatType | String | No | Normal | The type of the NAT gateway. Set the value to Normal, which specifies a standard NAT gateway. |
| ResourceGroupId | String | No | rg- bp67acfmxazb4ph** ** | The ID of the resource group to which the NAT gateway belongs. |

|   | Developer Guide·API r | eference |   |   | Virtual Private Clou | d |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNumber | Integer | No | 10 | The number of the page to return. |
| PageSize | Integer | No | 1 | The number of entries to return on each page. |
| DryRun | Boolean | No | true | Specifies whether to precheck the request only. Valid values: t rue: prechecks the request only. Resources are not queried. The system checks whether the AccessKey pair is valid, whether the Resource Access Management (RAM) user is authorized, and whether the required parameters are specified. If the request fails the precheck, the corresponding error message is returned. If the request passes the precheck, the DryRunOperation error code is returned. f alse: prechecks the request. This is the default value. After the request passes the precheck, a 2xx HTTP status code is returned and resources are queried. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NatGateways | Array of NatGateway |   | Detailed information about the NAT gateway. |
| NatGateway |   |   |   |
| AutoPay | Boolean | true | Indicates whether automatic payment is enabled. Valid values: f alse: automatic payment is disabled. After an order is generated, you must go to the Order Center to make the payment. t rue: automatic payment is enabled. Payments are automatically made. |
| BandwidthPackag eIds | List | bwp-s6lmotmkk**** | The ID of the service plan associated with the NAT gateway. |
| BusinessStatus | String | Normal | The status of the NAT gateway. Valid values: Normal: The NAT gateway works as expected. FinancialLocked: The NAT gateway is locked due to overdue payments. Securit yLocked: The NAT gateway is locked due to security reasons. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreationTime | String | 2017-06-08T12:20:55 | The time when the NAT gateway was created. The time follows the ISO 8601 standard in the YYYY- MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| DeletionProtectio n | Boolean | true | Indicates whether deletion protection is enabled. Valid values: t rue: enabled f alse: disabled |
| Description | String | NAT | The description of the NAT gateway. |
| EcsMetricEnabled | Boolean | true | Indicates whether the traffic monitoring feature is enabled. Valid values: t rue: enabled f alse: disabled |
| ExpiredTime | String | 2017-08-26T16:00Z | The time when the NAT gateway expires. |
| ForwardTableIds | List | ftb- uf6gj3mhsg94qsqst**** | The list of DNAT entries. |
| InstanceChargeTy pe | String | PostPaid | The billing method of the NAT gateway. Valid values: Post Paid: pay-as-you-go PrePaid: subscription |
| InternetChargeTyp e | String | PayBySpec | The metering method of the NAT gateway. Only PayBySpec is returned, which indicates the pay-by- specification metering method. |
| IpLists | Array of IpList |   | Detailed information about the elastic IP address (EIP) that is associated with the NAT gateway. |
| IpList |   |   |   |
| AllocationId | String | eip- n2y6nbm9z7t1l3xfz**** | The ID of the EIP that is associated with the NAT gateway. |
| ApAccessEnabled | Boolean | false | Indicates whether access points are configured. Valid values: t rue: access points are configured. f alse: access points are not configured. |
| IpAddress | String | 116.62.XX.XX | The EIP. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| SnatEntryEnabled | Boolean | false | Indicates whether the EIP is specified in an SNAT entry. |
| UsingStatus | String | UsedBySnatTable | The status of the EIP. |
| Name | String | abc | The name of the NAT gateway. |
| NatGatewayId | String | ngw- bp1047e2d4z7kf2ki**** | The ID of the NAT gateway. |
| NatGatewayPrivat eInfo | Struct |   | Private information about the NAT gateway. If Nat T ype is set to Normal, all parameters returned in this list are empty. |
| EniInstanceId | String | 10 | The instance ID of the elastic network interface (ENI). |
| IzNo | String | cn-hangzhou-b | The zone ID of the instance. |
| MaxBandwidth | Integer | 5120 | The bandwidth limit. Unit: Mbit/s. |
| PrivateIpAddress | String | 192.168.1.xx | The private IP address. |
| VswitchId | String | vsw- bp1s2laxhdf9ayjbo**** | The ID of the vSwitch. |
| NatType | String | Normal | The type of the NAT gateway. |
| RegionId | String | cn-qingdao-env17-d01 | The ID of the region where the NAT gateway is deployed. |
| ResourceGroupId | String | rg- bp67acfmxazb4ph**** | The ID of the resource group to which the NAT gateway belongs. |
| SnatTableIds | List | stb- uf6dalcdu0krz423p**** | The list of SNAT entries of the NAT gateway. |
| Spec | String | Small | The size of the NAT gateway. |
| Status | String | Initiating | The status of the NAT gateway. Valid values: Init iat ing: The NAT gateway is being initialized. Available: The NAT gateway is available. Pending: The NAT gateway is being configured. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpcId | String | vpc- bp15zckdt37pq72z**** | The ID of the VPC. |
| PageNumber | Integer | 10 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |
| TotalCount | Integer | 10 | The total number of returned entries. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeNatGateways &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeNatGatewaysResponse>
  <TotalCount>10</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF    </RequestId>
  <PageNumber>10</PageNumber>
  <NatGateways>
        <Status>Initiating</Status>
        <Description>NAT</Description>
        <ResourceGroupId>rg-bp67acfmxazb4ph****</ResourceGroupId>
        <InstanceChargeType>PostPaid</InstanceChargeType>
        <DeletionProtection>true</DeletionProtection>
        <AutoPay>true</AutoPay>
        <NatType>Normal</NatType>
        <BusinessStatus>Normal</BusinessStatus>
        <InternetChargeType>PayBySpec</InternetChargeType>
        <Name>abc</Name>
        <EcsMetricEnabled>true</EcsMetricEnabled>
        <VpcId>vpc-bp15zckdt37pq72z****</VpcId>
        <ExpiredTime>2017-08-26T16:00Z</ExpiredTime>
        <CreationTime>2017-06-08T12:20:55</CreationTime>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <Spec>Small</Spec>
        <NatGatewayId>ngw-bp1047e2d4z7kf2ki****</NatGatewayId>
        <IpLists>
              <UsingStatus>UsedBySnatTable</UsingStatus>
              <ApAccessEnabled>false</ApAccessEnabled>
              <SnatEntryEnabled>false</SnatEntryEnabled>
              <AllocationId>eip-n2y6nbm9z7t1l3xfz****</AllocationId>
              <IpAddress>116.62.XX.XX</IpAddress>
        </IpLists>
        <ForwardTableIds>ftb-uf6gj3mhsg94qsqst****</ForwardTableIds>
        <SnatTableIds>stb-uf6dalcdu0krz423p****</SnatTableIds>
        <BandwidthPackageIds>bwp-s6lmotmkk****</BandwidthPackageIds>
        <NatGatewayPrivateInfo>
              <IzNo>cn-hangzhou-b</IzNo>
              <PrivateIpAddress>192.168.1.xx</PrivateIpAddress>
              <MaxBandwidth>5120</MaxBandwidth>
              <EniInstanceId>10</EniInstanceId>
              <VswitchId>vsw-bp1s2laxhdf9ayjbo****</VswitchId>
        </NatGatewayPrivateInfo>
  </NatGateways>
</DescribeNatGatewaysResponse>
```

`JSON` format `{`

```json
    "TotalCount": 10,
    "PageSize": 10,
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
    "PageNumber": 10,
    "NatGateways": {
        "Status": "Initiating",
        "Description": "NAT",
        "ResourceGroupId": "rg-bp67acfmxazb4ph****",
        "InstanceChargeType": "PostPaid",
        "DeletionProtection": true,
        "AutoPay": true,
        "NatType": "Normal",
        "BusinessStatus": "Normal",
        "InternetChargeType": "PayBySpec",
        "Name": "abc",
        "EcsMetricEnabled": true,
        "VpcId": "vpc-bp15zckdt37pq72z****",
        "ExpiredTime": "2017-08-26T16:00Z",
        "CreationTime": "2017-06-08T12:20:55",
        "RegionId": "cn-qingdao-env17-d01",
        "Spec": "Small",
        "NatGatewayId": "ngw-bp1047e2d4z7kf2ki****",
        "IpLists": {
            "UsingStatus": "UsedBySnatTable",
            "ApAccessEnabled": false,
            "SnatEntryEnabled": false,
            "AllocationId": "eip-n2y6nbm9z7t1l3xfz****",
            "IpAddress": "116.62.XX.XX"
```

`},`

```json
        "ForwardTableIds": "ftb-uf6gj3mhsg94qsqst****",
        "SnatTableIds": "stb-uf6dalcdu0krz423p****",
        "BandwidthPackageIds": "bwp-s6lmotmkk****",
        "NatGatewayPrivateInfo": {
            "IzNo": "cn-hangzhou-b",
            "PrivateIpAddress": "192.168.1.xx",
            "MaxBandwidth": 5120,
            "EniInstanceId": 10,
            "VswitchId": "vsw-bp1s2laxhdf9ayjbo****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### CreateForwardEntry

Adds a DNAT entry to a DNAT table. Each DNAT entry consists of the following parameters: ExternalIp, ExternalPort, Protocol, InternalIp, and InternalPort. After you add a DNAT entry, the NAT gateway forwards packets of the specified protocol from [ExternalIp: ExternalPort] to [InternalIp: InternalPort] and sends responses back over the same route. When you call this operation, take note of the following limits: The combinations of ExternalIp, ExternalPort, and Protocol used in DNAT entries must be unique. Requests cannot be distributed to more than one Elastic Compute Service (ECS) instance if these requests are originated from the same source IP address, received on the same port, and use the same protocol. The combinations of Protocol, InternalIp, and InternalPort used in DNAT entries must be unique. If one or more DNAT entries in the DNAT table are in the Pending or Modifying state, you cannot add DNAT entries to the DNAT table. The public IP address (ExternalIp) in the DNAT entry, which is used to access the Internet, must meet the following requirements: If you have purchased a NAT service plan before November 3, 2017, the ExternalIp must be a public IP address in the NAT service plan. If you have not purchased a NAT service plan before November 3, 2017, the ExternalIp must be an elastic IP address (EIP) associated with the NAT service plan. You cannot specify the same EIP in both a DNAT entry and an SNAT entry. The private IP address (InternalIp) in the DNAT entry must meet the following requirements: The private IP address must belong to the CIDR block of the virtual private cloud (VPC) where the NAT gateway is deployed. The DNAT entry takes effect only when the private IP address is allocated to an ECS instance and the ECS instance is not assigned an EIP. If the private IP address is allocated to a resource other than an ECS instance, such as a high-availability virtual IP addresses (HAVIPs), Server Load Balancer (SLB) instance, or RDS instance, the DNAT entry does not take effect. Consequently, inbound traffic cannot be forwarded to the private IP address. You cannot specify the same EIP in both a DNAT entry and an SNAT entry. You can add up to 100 DNAT entries to a DNAT table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateForwardEntry | The operation that you want to perform. Set the value to Creat eForwardEnt ry. |
| ExternalIp | String | Yes | 116.XX.XX.28 | The public IP address of the NAT gateway. |
| ExternalPort | String | Yes | 8080 | The public port. Valid values: 1 t o 65535. |
| ForwardTableId | String | Yes | ftb- bp1mbjubq34hlcqp a**** | The ID of the DNAT table. |
| InternalIp | String | Yes | 192.XX.XX.1 | The destination private IP address. |
| InternalPort | String | Yes | 80 | The destination private port. Valid values: 1 t o 65535. |
| IpProtocol | String | Yes | TCP | The protocol that is used by the ports. Valid values: T CP: forwards TCP packets. UDP: forwards UDP packets. Any: forwards packets of all protocols. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env17- d0 | The ID of the region where the NAT gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| ForwardEntryName | String | No | ForwardEntry-1 | The name of the DNAT entry. The name must be 2 to 128 characters in length, and start with a letter. It cannot start with http:// or https:// . |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
| PortBreak | Boolean | No | false | Specifies whether to remove limits on the port range. Valid values: t rue: removes limits on the port range. f alse (default): sets limits on the port range. Not e When an SNAT entry and a DNAT entry use the same public IP address, and you want to specify a port number greater than 1024, set Port Break to t rue. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ForwardEntryId | String | fwd- 119smw5tkasdf**** | The ID of the DNAT entry. |
| RequestId | String | A4AEE536-A97A-40EB- 9EBE-53A6948A6928 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateForwardEntry &ExternalIp=116.XX.XX.28 &ExternalPort=8080 &ForwardTableId=ftb-bp1mbjubq34hlcqpa**** &InternalIp=192.XX.XX.1 &InternalPort=80 &IpProtocol=TCP &RegionId=cn-qingdao-env17-d0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateForwardEntryResponse>
  <RequestId>A4AEE536-A97A-40EB-9EBE-53A6948A6928</RequestId>
  <ForwardEntryId>fwd-119smw5tkasdf****</ForwardEntryId>
</CreateForwardEntryResponse>
```

`JSON` format `{`

```json
    "CreateForwardEntryResponse": {
        "RequestId": "A4AEE536-A97A-40EB-9EBE-53A6948A6928",
        "ForwardEntryId": "fwd-119smw5tkasdf****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | InvalidExternalIp.Malfor med | The specified ExternalIp is not a valid IP address. | The error message returned because the specified IP address is invalid. |
| 400 | InvalidInternalIp.Malfor med | The specified InternalIp is not a valid IP address. | The error message returned because the specified private IP address is invalid. |
| 400 | InvalidExternalPort.Malf ormed | The specified ExternalPort is not a valid port. | The error message returned because the specified public port is invalid. |
| 400 | InvalidInternalPort.Malf ormed | The specified InternalPort is not a valid port. | The error message returned because the specified private port is invalid. |
| 400 | Forbidden.DestnationIp OutOfVpcCIDR | The specified Internal Ip is Out of VPC CIDR. | The error message returned because the specified private IP address does not fall within the CIDR block of the VPC. Enter a private IP address that falls within the CIDR block of the VPC. |
| 400 | InvalidProtocal.ValueNo tSupported | The specified IpProtocol does not support. | The error message returned because the specified protocol is not supported. |
| 400 | IncorretForwardEntrySt atus | Some Forward entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. The error message returned because one or more DNAT entries in the DNAT table are in the Pending or Modifying state. |
| 404 | InvalidForwardTableId. NotFound | Specified forward table does not exist. | The error message returned because the specified DNAT table does not exist. Check the parameter value and try again. |

| Virtual Private | Cloud |   | Developer Guide·API reference |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidExternalIp.NotFou nd | Specified External Ip address does not found on the VRouter | The error message returned because the specified public IP address does not exist. |
| 400 | Forbidden.ExternalIp.Us edInSnatTable | The specified ExternalIp is already used in SnatTable | The error message returned because the specified public IP address is already used by an SNAT entry. Select a different IP address or delete the SNAT entry. |
| 400 | Forbindden | The specified Instance already bind eip | The error message returned because the ECS instance is associated with an EIP. Disassociate the EIP from the ECS instance before you create forwarding rules. |
| 400 | Forbidden.InternalIpOut OfVpcCIDR | The specified Internal Ip is Out of VPC CIDR. | The error message returned because the private IP address does not fall within the CIDR block of the VPC. |
| 400 | Invalid.natgwNotExist | The specified natgateway not exist. | The error message returned because the specified NAT gateway does not exist. |
| 400 | InvalidIp.NotInNatgw | The specified Ip not belong to natgateway. | The error message returned because the specified IP address is not associated with the NAT gateway. |
| 400 | MissingParameter | Missing mandatory parameter | The error message returned because one or more required parameters are not set. Check whether you have set all required parameters. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 400 | InvalidParameter.Name. Malformed | The specified Name is not valid. | The error message returned because the specified name is invalid. |

#### DescribeForwardTableEntries

Queries DNAT entries. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeForwardTab leEntries | The operation that you want to perform. Set the value to DescribeForwardT ableEnt ries. |
| ForwardTableId | String | Yes | ftb- bp1mbjubq34hlcqp a**** | The ID of the DNAT table. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the NAT gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| ForwardEntryId | String | No | fwd- 8vbn3bc8roygjp0gy* *** | The ID of the DNAT entry that is automatically assigned. |
| ExternalIp | String | No | 116.XX.XX.28 | The public IP address of the NAT gateway. |
| ExternalPort | String | No | 8080 | The public port. Valid values: 1 to 65535. |
| InternalIp | String | No | 192.XX.XX.1 | The destination private IP address. |
| InternalPort | String | No | 80 | The destination private port. Valid values: 1 to 65535. |
| IpProtocol | String | No | TCP | The protocol type. Valid values: T CP: forwards TCP packets. UDP: forwards UDP packets. Any: forwards packets of all protocols. |
| ForwardEntryName | String | No | ForwardEntry-1 | The name of the DNAT entry. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https:// . |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ForwardTableEntri es | Array of ForwardTableEntr y |   | The details of the DNAT entries. |
| ForwardTableEntr y |   |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ExternalIp | String | 116.XXX.XX.28 | The public IP address of the NAT gateway. |
| ExternalPort | String | 80 | The public port. |
| ForwardEntryId | String | fwd-119smw5tk**** | The ID of the DNAT entry. |
| ForwardEntryNam e | String | ForwardEntry-1 | The name of the DNAT entry. |
| ForwardTableId | String | ftb-11tc6xgmv**** | The ID of the DNAT table to which the DNAT entry belongs. |
| InternalIp | String | 192.XX.XX.1 | The private IP address. |
| InternalPort | String | 25 | The destination private port. Valid values: 1 to 65535. |
| IpProtocol | String | TCP | The protocol type. |
| Status | String | Available | The state of the DNAT entry. |
| TotalCount | Integer | 5 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | A6C4A8B1-7561-4509- 949C-20DEB40D71E6 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeForwardTableEntries &ForwardTableId=ftb-bp1mbjubq34hlcqpa**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeForwardTableEntriesResponse>
  <TotalCount>5</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>A6C4A8B1-7561-4509-949C-20DEB40D71E6</RequestId>
  <PageNumber>1</PageNumber>
  <ForwardTableEntries>
        <Status>Available</Status>
        <ExternalPort>80</ExternalPort>
        <ExternalIp>116.XXX.XX.28</ExternalIp>
        <ForwardEntryId>fwd-119smw5tk****</ForwardEntryId>
        <IpProtocol>TCP</IpProtocol>
        <InternalPort>25</InternalPort>
        <ForwardEntryName>ForwardEntry-1</ForwardEntryName>
        <InternalIp>192.XX.XX.1</InternalIp>
        <ForwardTableId>ftb-11tc6xgmv****</ForwardTableId>
  </ForwardTableEntries>
</DescribeForwardTableEntriesResponse>
```

`JSON` format `{`

```json
    "TotalCount": 5,
    "PageSize": 10,
    "RequestId": "A6C4A8B1-7561-4509-949C-20DEB40D71E6",
    "PageNumber": 1,
    "ForwardTableEntries": {
        "Status": "Available",
        "ExternalPort": 80,
        "ExternalIp": "116.XXX.XX.28",
        "ForwardEntryId": "fwd-119smw5tk****",
        "IpProtocol": "TCP",
        "InternalPort": 25,
        "ForwardEntryName": "ForwardEntry-1",
        "InternalIp": "192.XX.XX.1",
        "ForwardTableId": "ftb-11tc6xgmv****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | IncorretForwardEntrySt atus | Some Forward entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. One or more DNAT entries in the DNAT table are in the Pending or Modifying state. |
| 404 | InvalidForwardTableId. NotFound | Specified forwardTableId does not exist | The error message returned because the specified DNAT table does not exist. Check the parameter value and try again. |

#### ModifyForwardEntry

Modifies a DNAT entry. Not e You cannot modify DNAT entries if one or more DNAT entries in the DNAT table are in the Pending or Modif ying state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyForwardEntry | The operation that you want to perform. The operation that you want to perform. Set the value to Modif yForwardEnt ry. |
| ForwardEntryId | String | Yes | fwd- 8vbn3bc8roygjp0gy 3xk7 | The ID of the DNAT entry. |
| ForwardTableId | String | Yes | ftb- 8vbx8xu2lqj9qb334h 0ow | The ID of the DNAT table. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the NAT gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| ExternalIp | String | No | 116.XX.XX.28 | The public IP address of the NAT gateway. |
| ExternalPort | String | No | 80 | The public port. Valid values: 1 to 65535. |
| InternalIp | String | No | 10.XX.XX.78 | The destination private IP address. |
| InternalPort | String | No | 80 | The destination private port. Valid values: 1 to 65535. |
| IpProtocol | String | No | TCP | The protocol type. Valid values: T CP: forwards Transmission Control Protocol (TCP) packets. UDP: forwards User Datagram Protocol (UDP) packets. Any: forwards packets of all protocols. |
| ForwardEntryName | String | No | ForwardEntry-1 | The name of the DNAT entry. The description must be 2 to 128 characters in length, and start with a letter. It cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 24CC85DC-7700-4F09- 9624-99E988C7DD03 | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=ModifyForwardEntry &ForwardEntryId=fwd-8vbn3bc8roygjp0gy3xk7 &ForwardTableId=ftb-8vbx8xu2lqj9qb334h0ow &RegionId= cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
</ModifyForwardEntryResponse> <RequestId>24CC85DC-7700-4F09-9624-99E988C7DD03</RequestId> </ModifyForwardEntryResponse>
```

`JSON` format `{`

```json
    "RequestId": "24CC85DC-7700-4F09-9624-99E988C7DD03"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | InvalidExternalIp.Malfor med | The specified ExternalIp is not a valid IP address. | The error message returned because the specified IP address is invalid. |
| 400 | InvalidInternalIp.Malfor med | The specified InternalIp is not a valid IP address. | The error message returned because the specified private IP address is invalid. |
| 400 | InvalidExternalPort.Malf ormed | The specified ExternalPort is not a valid port. | The error message returned because the specified public port is invalid. |

|   | Virtual Private | Cloud |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidInternalPort.Malf ormed | The specified InternalPort is not a valid port. | The error message returned because the specified private port is invalid. |
| 400 | Forbidden.DestnationIp OutOfVpcCIDR | The specified Destination Ip is Out of VPC CIDR. | The error message returned because the specified private IP address does not fall within the CIDR block of the VPC. Enter a private IP address that falls within the CIDR block of the VPC. |
| 400 | InvalidProtocal.ValueNo tSupported | The specified IpProtocol does not support. | The error message returned because the specified protocol is not supported. |
| 400 | IncorretForwardEntrySt atus | Some Forward entry status blocked this operation.. | The error message returned because the operation cannot be performed. The error message returned because one or more DNAT entries in the DNAT table are in the Pending or Modifying state. |
| 400 | QuotaExceeded | Forward entry quota exceeded in this route table. | The error message returned because one route table cannot contain more than 48 custom routes to a route table. You can submit a ticket to increase the quota. |
| 404 | InvalidForwardEntryId.N otFound | Specified forward entry ID does not exist | The error message returned because the specified DNAT entry does not exist. |
| 404 | InvalidExternalIp.NotFou nd | Specified External Ip address does not found on the VRouter | The error message returned because the specified public IP address does not exist. |
| 404 | InvalidForwardTableId. NotFound | Specified forward table does not exist. | The error message returned because the specified DNAT table does not exist. Check the parameter value and try again. |
| 400 | Forbidden.ExternalIp.Us edInSnatTable | The specified ExternalIp is already used in SnatTable | The error message returned because the specified public IP address is already used by an SNAT entry. Select a different IP address or delete the SNAT entry. |
| 400 | Forbidden.Already.Boun ded | The specified instance already bounded | The error message returned because the specified instance is already associated with another DNAT entry. |
| 400 | InvalidParameter.Name. Malformed | The specified Name is not valid. | The error message returned because the format of the specified name is invalid. |

#### DeleteForwardEntry

Deletes a DNAT entry. Not e You cannot delete DNAT entries if one or more DNAT entries in the DNAT table are in the Pending or Modif ying state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteForwardEntry | The operation that you want to perform. Set the value to Delet eForwardEnt ry. |
| ForwardEntryId | String | Yes | fwd- 8vbn3bc8roygjp0g** ** | The ID of the DNAT entry. |
| ForwardTableId | String | Yes | ftb- 8vbx8xu2lqj9qb334* *** | The ID of the DNAT table. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteForwardEntry &ForwardEntryId=fwd-8vbn3bc8roygjp0g**** &ForwardTableId=ftb-8vbx8xu2lqj9qb334**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteForwardEntryResponse>
  <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteForwardEntryResponse>
```

`JSON` format

```json
{"RequestId":"0ED8D006-F706-4D23-88ED-E11ED28DCAC0"}
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | IncorretForwardEntrySt atus | Some Forward entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. The error message returned because one or more DNAT entries in the DNAT table are in the Pending or Modifying state. |
| 404 | InvalidForwardEntryId.N otFound | Specified forward entry ID does not exist | The error message returned because the specified DNAT entry does not exist. |
| 404 | InvalidForwardTableId. NotFound | Specified forward table does not exist. | The error message returned because the specified DNAT table does not exist. Check the parameter value and try again. |
| 400 | IncorretForwardEntrySt atus | The Specified forwardEntry is not exist | The error message returned because the specified DNAT entry does not exist. |
| 400 | MissingParameter | Missing mandatory parameter | The error message returned because one or more required parameters are not set. Check whether you have set all required parameters. |

#### CreateSnatEntry

Adds an SNAT entry to an SNAT table. When you call this operation, take note of the following limits: The vSwitch and the Elastic Compute Service (ECS) instance specified in the SNAT entry must belong to the virtual private cloud (VPC) where the NAT gateway is deployed. Each vSwitch or ECS instance can be specified in only one SNAT entry. If a high-availability virtual IP address (HAVIP) exists in the vSwitch, you cannot create SNAT entries. You cannot specify the same EIP in both a DNAT entry and an SNAT entry. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSnatEntry | The operation that you want to perform. Set the value to Creat eSnat Ent ry. |

|   | Developer Guide·API r | eference |   |   | Virtual Private Clou | d |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| SnatIp | String | Yes | 47.XX.XX.98 | The public IP addresses. Separate multiple IP addresses with commas (,). |
| SnatTableId | String | Yes | stb- bp190wu8io1vgev** ** | The ID of the SNAT table. |
| SourceVSwitchId | String | No | vsw- bp1nhx2s9ui5o**** | The ID of the vSwitch that requires to access the Internet. |
| SourceCIDR | String | No | 10.1.1.0/24 | The CIDR block of the vSwitch or the IP address of the ECS instance. vSwitch granularity: specifies the CIDR block of the vSwitch, for example, 192.168.1.0/24. When an ECS instance of a vSwitch requires to access the Internet, the NAT gateway provides the SNAT service for the ECS instance. If you specify only one public IP address in the Snat Ip parameter, the ECS instance uses the specified public IP address to access the Internet. If you specify multiple public IP addresses in the Snat Ip parameter, the ECS instance randomly selects a public IP address from Snat Ip to access the Internet. ECS granularity: specifies the IP address of the ECS instance, for example, 192.168.1.0/32. When the ECS instance requires to access the Internet, the NAT gateway provides the SNAT service for the ECS instance. If you specify only one public IP address in the Snat Ip parameter, the ECS instance uses the specified public IP address to access the Internet. If you specify multiple public IP addresses in the Snat Ip parameter, the ECS instance randomly selects a public IP address from Snat Ip to access the Internet. This parameter and the SourceVSwt ichId parameter cannot be set at the same time. If the SourceVSwit chId parameter is set, you cannot set the SourceCIDR parameter. If the SourceCIDR parameter is set, you cannot set the SourceVSwit chId parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SnatEntryName | String | No | SnatEntry-1 | The name of the SNAT entry. The name must be 2 to 128 characters in length, and must start with a letter. It cannot start with http:// or https:// . |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| SnatEntryId | String | snat-kmd6nv8fy**** | The ID of the SNAT entry. |
| RequestId | String | 2315DEB7-5E92-423A- 91F7-4C1EC9AD97C3 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateSnatEntry &RegionId=cn-qingdao-env17-d01 &SnatIp=47.XX.XX.98 &SnatTableId=stb-bp190wu8io1vgev**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateSnatEntryResponse>
      <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
      <SnatEntryId>snat-119smw5tkx****</SnatEntryId>
</CreateSnatEntryResponse>
```

`JSON` format `{`

```json
    "SnatEntryId": "snat-kmd6nv8fyx****",
    "RequestId": "2315DEB7-5E92-423A-91F7-4C1EC9AD97C3"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidSnatTableId.NotF ound | Specified SNAT table does not exist. | The error message returned because the specified SNAT table does not exist. Check whether the ID of the SNAT table is valid. |
| 400 | Forbidden.SourceVSwit chId.IncludeHaVip | There is some HaVips under specified VSwitch | The error message returned because the specified vSwitch is associated with HAVIPs. |
| 400 | InvalidSnatIp.Malforme d | The specified SnatIp is not a valid IP address. | The error message returned because the specified public IP address is invalid. |
| 400 | SNAT IP POOL COUNT _ _ _ _ TOO MANY _ | The Snat pool ip too many. | The error message returned because the number of IP addresses in the SNAT IP address pool has reached the upper limit. |
| 400 | Forbidden.SnatEntryCou ntLimited | SNAT entry in the specified SNAT table reach it?s limit. | The error message returned because the number of SNAT entries has reached the upper limit. |
| 400 | NOT ALLOW USE SOUR _ _ _ CECIDR | The User not in nat scope unlimited _ _ white list. Cannot use SourceCidr param. | The error message returned because the specified private IP address does not fall within the CIDR block of the VPC. |
| 404 | InvalidVSwitchId.NotFou nd | The specified virtual switch does not exists. | The error message returned because the specified vSwitch does not exist. Check whether the specified ID is valid. |
| 400 | INVALID PARAMETER _ | The parameter invalid. | The error message returned because the specified parameter is invalid. |
| 400 | Forbidden.SourceVSwit chId.Duplicated | The specified SourceCIDRis duplicated. | The error message returned because an SNAT entry is already created for the specified vSwitch. |
| 404 | InvalidSnatIp.NotFound | Specified SnatIp does not found on the NAT Gateway | The error message returned because the specified public IP address is not found on the NAT gateway. |
| 400 | Forbidden.IpUsedInForw ardTable | The specified SnatIp already used in forward table | The error message returned because the specified public IP address is already used by a DNAT entry. Select another public IP address or delete the DNAT entry. |
| 400 | Forbindden | The specified Instance already bind eip | The error message returned because the ECS instance is associated with an EIP. Disassociate the EIP from the ECS instance before you create forwarding rules. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | OperationUnsupported. CidrConflict | The specified CIDR block conflicts with an existing SNAT entry. | The error message returned because the specified CIDR block conflicts with those in existing SNAT entries. |
| 400 | InvalidParameter.Name. Malformed | The specified Name is not valid. | The error message returned because the specified name is invalid. |

#### DescribeSnatTableEntries

Queries SNAT entries. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSnatTableE ntries | The operation that you want to perform. Set the value to DescribeSnat T ableEnt ries. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| SnatTableId | String | Yes | stb- 8vbczigrhop8x5u3t* *** | The ID of the SNAT table. |
| SnatEntryId | String | No | snat- 8vbae8uqh7rjpk7d2* *** | The ID of the SNAT entry. |
| SourceVSwitchId | String | No | vsw-3xb**** | The ID of the vSwitch that can access the Internet through SNAT. |
| SourceCIDR | String | No | 116.XX.XX.0/28 | The source CIDR block of the SNAT entry. |
| SnatIp | String | No | 116.XX.XX.28 | The public IP address in the SNAT entry. |
| SnatEntryName | String | No | SnatEntry-1 | The name of the SNAT entry. The name must be 2 to 128 characters in length, and start with a letter. The name cannot start with http:// or https:// . |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| SnatTableEntries | Array of SnatTableEntry |   | The detailed information about the SNAT entries. |
| SnatTableEntry |   |   |   |
| SnatEntryId | String | snat- 8vbae8uqh7rjpk7d2**** | The ID of the SNAT entry. |
| SnatEntryName | String | SnatEntry-1 | The name of the SNAT entry. |
| SnatIp | String | 116.XX.XX.28 | The public IP address in the SNAT entry. |
| SnatTableId | String | stb- 8vbczigrhop8x5u3t**** | The ID of the SNAT table to which the SNAT entry belongs. |
| SourceCIDR | String | 116.XX.XX.0/28 | The source CIDR block of the SNAT entry. |
| SourceVSwitchId | String | vsw-3xb**** | The ID of the vSwitch that can access the Internet through SNAT. |
| Status | String | Pending | The state of the SNAT entry. |
| TotalCount | Integer | 1 | The number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned on each page. |
| RequestId | String | 6D7E89B1-1C5B-412B- 8585-4908E222EED5 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSnatTableEntries &RegionId=cn-qingdao-env17-d01 &SnatTableId=stb-8vbczigrhop8x5u3t**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSnatTableEntriesResponse>
  <TotalCount>1</TotalCount>
  <PageSize>5</PageSize>
  <RequestId>6D7E89B1-1C5B-412B-8585-4908E222EED5</RequestId>
  <PageNumber>1</PageNumber>
  <SnatTableEntries>
        <Status>Pending</Status>
        <SourceVSwitchId>vsw-3xb****</SourceVSwitchId>
        <SnatEntryName>SnatEntry-1</SnatEntryName>
        <SourceCIDR>116.XX.XX.0/28</SourceCIDR>
        <SnatEntryId>snat-8vbae8uqh7rjpk7d2****</SnatEntryId>
        <SnatIp>116.XX.XX.28</SnatIp>
        <SnatTableId>stb-8vbczigrhop8x5u3t****</SnatTableId>
  </SnatTableEntries>
</DescribeSnatTableEntriesResponse>
```

`JSON` format `{`

```json
    "TotalCount": 1,
    "PageSize": 5,
    "RequestId": "6D7E89B1-1C5B-412B-8585-4908E222EED5",
    "PageNumber": 1,
    "SnatTableEntries": {
        "Status": "Pending",
        "SourceVSwitchId": "vsw-3xb****",
        "SnatEntryName": "SnatEntry-1",
        "SourceCIDR": "116.XX.XX.0/28",
        "SnatEntryId": "snat-8vbae8uqh7rjpk7d2****",
        "SnatIp": "116.XX.XX.28",
        "SnatTableId": "stb-8vbczigrhop8x5u3t****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidSnatTableId.NotF ound | Specified SNAT table does not exist. | The error message returned because the specified SNAT table does not exist. Check whether the ID of the SNAT table is valid. |

#### ModifySnatEntry

Modifies a specified SNAT entry. Not e You cannot modify SNAT entries if one or more SNAT entries in the SNAT table are in the Pending or Modif ying state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySnatEntry | The operation that you want to perform. Set the value to Modif ySnat Ent ry. |
| RegionId | String | Yes | cn-qingdao-env17- d0 | The ID of the region where the NAT gateway is deployed. |
| SnatEntryId | String | Yes | snat- bp1vcgcf8tm0plqcg **** | The ID of the SNAT entry. |
| SnatTableId | String | Yes | stb- 8vbczigrhop8x5u3t* *** | The ID of the SNAT table to which the SNAT entry belongs. |
| SnatIp | String | Yes | 47.XX.XX.98 | The public IP address in the SNAT entry. If multiple IP addresses are specified, separate them with commas (,). |
| SnatEntryName | String | No | SnatEntry-1 | The name of the SNAT entry. The description must be 2 to 128 characters in length, and start with a letter. It cannot start with http:// or https:// . |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. Only ASCII characters are allowed. It can contain up to 64 ASCII characters. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2315DEB7-5E92-423A- 91F7-4C1EC9AD97C3 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifySnatEntry &RegionId=cn-qingdao-env17-d0 &SnatEntryId=snat-bp1vcgcf8tm0plqcg**** &SnatTableId=stb-8vbczigrhop8x5u3t**** &SnatIp=47.XX.XX.98 &<Common request parameters>
```

Successful response examples `XML` format

```xml
<ModifySnatEntryResponse>
      <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
</ModifySnatEntryResponse>
```

`JSON` format `{`

```json
  "RequestId": "2315DEB7-5E92-423A-91F7-4C1EC9AD97C3"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |
| 404 | InvalidSnatTableId.NotF ound | Specified SNAT table does not exist. | The error message returned because the specified SNAT table does not exist. Check whether the ID of the SNAT table is valid. |
| 400 | InvalidSnatIp.Malforme d | The specified SnatIp is not a valid IP address. | The error message returned because the specified public IP address is invalid. |
| 404 | InvalidSnatEntryId.NotF ound | Specified SNAT entry does not exist. | The error message returned because the specified SNAT entry does not exist. Check whether the SNAT entry is valid. |
| 400 | Forbidden.SourceVSwit chId.Duplicated | The specified SourceCIDRis duplicated. | The error message returned because an SNAT entry is already configured for the specified vSwitch. |
| 404 | InvalidSnatIp.NotFound | Specified SnatIp does not found on the NAT Gateway | The error message returned because the specified public IP address does not exist in the NAT gateway. |
| 400 | Forbidden.IpUsedInForw ardTable | The specified SnatIp already used in forward table | The error message returned because the specified public IP address is already used by a DNAT entry. Select another IP address or delete the DNAT rule that uses the public IP address. |
| 400 | InvalidParameter.Name. Malformed | The specified Name is not valid. | The error message returned because the specified name format is invalid. |

#### DeleteSnatEntry

Deletes a specified SNAT entry. Not e You cannot delete SNAT entries if one or more SNAT entries in the SNAT table are in the Pending or Modif ying state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSnatEntry | The operation that you want to perform. Set the value to Delet eSnat Ent ry. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| SnatEntryId | String | Yes | snat- bp1vcgcf8tm0plqc* *** | The ID of the SNAT entry. |
| SnatTableId | String | Yes | stb- bp190wu8io1vgev80 **** | The ID of the SNAT table. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 47B80B6A-759A-479C- A565-76D04BDA29F3 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteSnatEntry &RegionId=cn-qingdao-env17-d01 &SnatEntryId=snat-bp1vcgcf8tm0plqc**** &SnatTableId=stb-bp190wu8io1vgev80**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteSnatEntryResponse>
  <RequestId>47B80B6A-759A-479C-A565-76D04BDA29F3</RequestId>
</DeleteSnatEntryResponse>
```

`JSON` format

```json
{"RequestId":"47B80B6A-759A-479C-A565-76D04BDA29F3"}
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | IncorretSnatEntryStatus | Some Snat entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. The error message returned because one or more SNAT entries in the SNAT table are in the Pending or Modifying state. |
| 404 | InvalidSnatEntryId.NotF ound | Specified Snat entry ID does not exist | The error message returned because the specified SNAT entry does not exist. Check whether the SNAT entry is valid. |
| 404 | InvalidSnatTableId.NotF ound | Specified SNAT table does not exist. | The error message returned because the specified SNAT table does not exist. Check whether the ID of the SNAT table is valid. |
| 404 | InvalidSnatEntryId.NotF ound | Specified SNAT entry does not exist. | The error message returned because the specified SNAT entry does not exist. Check whether the SNAT entry is valid. |

#### ModifyBandwidthPackageSpec

Modifies the bandwidth value of a specified NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBandwidthPa ckageSpec | The operation that you want to perform. Set the value to Modif yBandwidt hPackageSpec. |
| Bandwidth | String | Yes | 5 | The maximum bandwidth of the NAT service plan. Valid values: 5 to 1000. |
| BandwidthPackageId | String | Yes | bwp-s6lmotmkk**** | The ID of the NAT service plan. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 079874CD-AEC1-43E6- AC03-ADD96B6E4907 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyBandwidthPackageSpec &Bandwidth=5 &BandwidthPackageId=bwp-s6lmotmkk**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyBandwidthPackageSpecResponse>
  <RequestId>079874CD-AEC1-43E6-AC03-ADD96B6E4907</RequestId>
</ModifyBandwidthPackageSpecResponse>
```

`JSON` format `{`

```json
    "RequestId": "079874CD-AEC1-43E6-AC03-ADD96B6E4907"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidBandwidth.Value NotSupported | The specified value of Bandwidth not supported. | The error message returned because the specified maximum bandwidth value is invalid. |
| 404 | BandwidthPackage.Fina ncialLocked | The specified BandwidthPackage has been Financail Lock. | The error message returned because the specified NAT service plan is locked due to overdue payments. |

#### DeleteBandwidthPackage

Deletes a specified NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBandwidthPac kage | The operation that you want to perform. Set the value to Delet eBandwidt hPackage. |

|   | Virtual Private Cloud |   |   |   | Developer Guide·API reference |   |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BandwidthPackageId | String | Yes | bwp- bp1arsrmca9kp**** | The ID of the NAT service plan. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| Force | Boolean | No | false | Specifies whether to forcibly delete the NAT service plan. f alse(default): no t rue: yes |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7D275A59-1EB0-4775- 8A20-2A47055EAC5C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteBandwidthPackage &BandwidthPackageId=bwp-bp1arsrmca9kp**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteBandwidthPackageResponse>
  <RequestId>7D275A59-1EB0-4775-8A20-2A47055EAC5C</RequestId>
</DeleteBandwidthPackageResponse>
```

`JSON` format `{`

```json
    "RequestId": "7D275A59-1EB0-4775-8A20-2A47055EAC5C"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | DependencyViolation.Fo rwardEntry | The specified BandwidthPackageId has dependent resource. | The error message returned because the NAT service plan contains SNAT or DNAT entries. Delete them and try again. |
| 400 | DependencyViolation.Sn atEntry | The specified BandwidthPackageId has dependent resource. | The error message returned because the NAT service plan contains SNAT or DNAT entries. Delete them and try again. |

#### CreateBandwidthPackage

Creates a NAT service plan. A NAT service plan consists of bandwidth resources and one or more public IP addresses. You can associate up to four NAT service plans with a NAT gateway. A NAT service plan includes: Bandwidth resources One or more public IP addresses Not e This operation can be performed by only Apsara Stack accounts that have purchased NAT service plans before November 3, 2017. If you have not purchased a NAT service plan before November 3, 2017, you can apply for public IP addresses by associating elastic IP addresses (EIPs). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBandwidthPac kage | The operation that you want to perform. Set the value to Creat eBandwidt hPackage. |
| Bandwidth | Integer | Yes | 5 | The maximum bandwidth of the NAT service plan. Valid values: 5 to 1000. Unit: Mbit/s. |
| IpCount | Integer | Yes | 2 | The number of public IP addresses in the NAT service plan. Valid values: 1 t o 50. |
| NatGatewayId | String | Yes | ngw-7mwb327j1**** | The ID of the NAT gateway. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Name | String | No | The name of the NAT service plan. | The name of the NAT service plan. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It must start with a _ letter. The name cannot start with http:// or https:// . |
| Description | String | No | The description of the NAT service plan. | The description of the NAT service plan. The name must be 2 to 256 characters in length, and start with a letter. It cannot start with http:// or https:// . |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| ISP | String | No | BGP | Only BGP is supported. |
| Zone | String | No | cn-qingdao-env17- amtest11001-a | The zone to which the NAT service plan belongs. If you do not set this parameter, the service plan is randomly allocated to a zone. Not e Connectivity is not affected when the IP addresses provided by the NAT service plan and the backend Elastic Compute Service (ECS) instances belong to different zones. However, when the IP addresses and ECS instances belong to the same zone, latency can be reduced. |
| InternetChargeType | String | No | PayByBandwidth | The metering method of the NAT service plan. Valid values: PayByT raf f ic: pay-by-data-transfer |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BandwidthPackag eId | String | bwp-s6lmotmkk**** | The ID of the NAT service plan. |
| RequestId | String | 54ED4074-3F89-4F11- B166-837DD3E20FE3 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateBandwidthPackage &Bandwidth=5 &IpCount=2 &NatGatewayId=ngw-7mwb327j1**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateBandwidthPackageResponse>
  <RequestId>54ED4074-3F89-4F11-B166-837DD3E20FE3</RequestId>
  <BandwidthPackageId>bwp-s6lmotmkk****</BandwidthPackageId>
</CreateBandwidthPackageResponse>
```

`JSON` format `{`

```json
    "RequestId": "54ED4074-3F89-4F11-B166-837DD3E20FE3",
    "BandwidthPackageId": "bwp-s6lmotmkk****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidVpcId.NotFound | Specified value of VpcId is not found in our record. | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because one or more required parameters are not set. Check whether you have set all the required parameters before you call this operation. |
| 404 | InvalidZoneId.NotFound | Specified value of ZoneId is not exists. | The error message returned because the specified zone does not exist. |
| 404 | InvalidZoneId.NotFound | Can not find ZoneId for allocated ip. | The error message returned because the zone of the specified IP address is invalid. |
| 400 | QuotaExceeded.Bandwi dthPackageIps | The specified ipCount exceeded quota. | The error message returned because the number of IP addresses has reached the upper limit. Submit a ticket to increase the quota. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded.Bandwi dthPackageCountOnNat Gateway | BandwidthPackage count limit on one NatGateway exceeded. | The error message returned because the number of NAT service plans has reached the upper limit. You can associate up to four NAT service plans with a NAT gateway. |
| 400 | InvalidParameter.Name. Malformed | The specified Name is not valid. | The error message returned because the specified name is invalid. |
| 400 | InvalidParameter.Descri ption.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |
| 400 | InvalidParameter.Bandw idthPackage.n.ISP.Value NotSupport | The specified ISP of BandwidthPackage is not valid. | The error message returned because the specified Internet service provider (ISP) of the EIP bandwidth plan is invalid. |
| 400 | ZONE NO AVAILABLE IP _ _ _ | The Zone have no available ip. | The error message returned because no IP address is available in the zone. |

#### DescribeBandwidthPackages

Queries NAT service plans in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBandwidthP ackages | The operation that you want to perform. Set the value to DescribeBandwidt hPackages. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| BandwidthPackageId | String | No | bwp- bp1xea10o8qxwdfs **** | The ID of the NAT service plan. |
| NatGatewayId | String | No | ngw- bp1uewa15k4iydfre* *** | The ID of the NAT gateway. |
| PageNumber | Integer | No | 10 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BandwidthPackag es | Array of BandwidthPackag e |   | The detailed description of the NAT service plan. |
| BandwidthPackag e |   |   |   |
| Bandwidth | String | 5 | The bandwidth value of the NAT service plan. Valid values: 5 to 5000. Unit: Mbit/s. |
| BandwidthPackag eId | String | bwp-xxoo123sfwr**** | The ID of the NAT service plan. |
| BusinessStatus | String | Normal | The state of the NAT service plan. Valid values: Normal: The NAT service plan working as expected. FinancialLocked: The NAT service plan is locked due to overdue payments. Securit yLocked: The NAT service plan is locked due to security reasons. |
| CreationTime | String | 2017-06-08T12:20:55 | The time when the NAT service plan was created. The time follows the ISO 8601 standard in YYYY-MM-DDThh:mmZ format. It must be in UTC. |
| Description | String | test123 | The description of the NAT service plan. The description must be 2 to 256 characters in length. The description is displayed in the console. This parameter is empty by default. It cannot start with http:// or https:// . |
| ISP | String | BGP | Only BGP is supported. |
| InstanceChargeTy pe | String | PostPaid | The billing method of the NAT service plan. Only Post Paid (pay-as-you-go) is supported. |
| InternetChargeTyp e | String | PayByBandwidth | The metering method of the NAT service plan. PayByT raf f ic: pay-by-data-transfer |
| IpCount | String | 1 | The number of public IP addresses in the NAT service plan. Valid values: 1 to 50. |
| Name | String | abc | The name of the NAT service plan. |
| NatGatewayId | String | ngw-xxoo123ggtf**** | The ID of the NAT gateway. |

|   | Virtual Private Clou | d |   | Developer Guide·API reference |   |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PublicIpAddresses | Array of PublicIpAddresse |   | The IP address in the NAT service plan. |
| PublicIpAddresse |   |   |   |
| AllocationId | String | eip- 2zeerraiwb7ujdeds**** | The ID that is allocated. |
| ApAccessEnabled | Boolean | true |   |
| IpAddress | String | 116.XX.XX.28 | The IP address. |
| UsingStatus | String | Available | The state of the NAT service plan. |
| RegionId | String | cn-qingdao-env17-d01 | The region ID of the NAT service plan. |
| Status | String | Available | The state of the bandwidth plan. |
| ZoneId | String | cn-qingdao-env17- amtest11001-a | The ID of the zone to which the NAT service plan belongs. |
| TotalCount | Integer | 10 | The number of entries returned. |
| PageNumber | Integer | 10 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF" | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeBandwidthPackages &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBandwidthPackagesResponse>
  <TotalCount>10</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF"</RequestId>
  <PageNumber>10</PageNumber>
  <BandwidthPackages>
        <Status>Available</Status>
        <IpCount>1</IpCount>
        <Description>test123</Description>
        <ZoneId>cn-qingdao-env17-amtest11001-a</ZoneId>
        <InstanceChargeType>PostPaid</InstanceChargeType>
        <ISP>BGP</ISP>
        <BusinessStatus>Normal</BusinessStatus>
        <InternetChargeType>PayByBandwidth</InternetChargeType>
        <Name>abc</Name>
        <Bandwidth>5</Bandwidth>
        <CreationTime>2017-06-08T12:20:55</CreationTime>
        <BandwidthPackageId>bwp-xxoo123sfwr****</BandwidthPackageId>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <NatGatewayId> ngw-xxoo123ggtf****</NatGatewayId>
        <PublicIpAddresses>
              <UsingStatus>Available</UsingStatus>
              <ApAccessEnabled>true</ApAccessEnabled>
              <AllocationId>eip-2zeerraiwb7ujdeds****</AllocationId>
              <IpAddress>116.XX.XX.28</IpAddress>
        </PublicIpAddresses>
  </BandwidthPackages>
</DescribeBandwidthPackagesResponse>
```

`JSON` format `{`

```json
    "TotalCount": 10,
    "PageSize": 10,
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF\"",
    "PageNumber": 10,
    "BandwidthPackages": {
        "Status": "Available",
        "IpCount": 1,
        "Description": "test123",
        "ZoneId": "cn-qingdao-env17-amtest11001-a",
        "InstanceChargeType": "PostPaid",
        "ISP": "BGP",
        "BusinessStatus": "Normal",
        "InternetChargeType": "PayByBandwidth",
        "Name": "abc",
        "Bandwidth": 5,
        "CreationTime": "2017-06-08T12:20:55",
        "BandwidthPackageId": "bwp-xxoo123sfwr****",
        "RegionId": "cn-qingdao-env17-d01",
        "NatGatewayId": "ngw-xxoo123ggtf****",
        "PublicIpAddresses": {
            "UsingStatus": "Available",
            "ApAccessEnabled": true,
            "AllocationId": "eip-2zeerraiwb7ujdeds****",
            "IpAddress": "116.XX.XX.28"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### ModifyBandwidthPackageAttribute

Modifies the name and description of a specified NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBandwidthPa ckageAttribute | The operation that you want to perform. Valid values: Modif yBandwidt hPackageAt t ribut e . |
| BandwidthPackageId | String | Yes | bwp-s6lmotmkk**** | The ID of the NAT service plan. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the NAT service plan. You can call the DescribeRegions interface to obtain the region ID. |
| Name | String | No | NATABC | The name of the NAT bandwidth plan. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). But not _ with http:// or https:// The beginning. |
| Description | String | No | This is NAT. | The description of the NAT bandwidth plan. The name must be 2 to 256 characters in length. It must start with a letter, but cannot start with http:// or https:// The beginning. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DFDDD35D-3F29-4E15- AA28-53F5341F9599 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyBandwidthPackageAttribute &BandwidthPackageId=bwp-s6lmotmkk**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyBandwidthPackageAttributeResponse>
  <RequestId>DFDDD35D-3F29-4E15-AA28-53F5341F9599</RequestId>
</ModifyBandwidthPackageAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "DFDDD35D-3F29-4E15-AA28-53F5341F9599"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidBandwidthPackag eId.NotFound | The specified bandwidthPackageId does not exist in our records. | The error message returned because the ID of the specified NAT service plan does not exist. |
| 400 | InvalidParameter.Name. Malformed | The specified Name is not valid. | The error message returned because the specified name is invalid. |
| 400 | InvalidParameter.Descri ption.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |

#### AddBandwidthPackageIps

Adds one or more public IP addresses to a NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| Action | String | Yes | AddBandwidthPacka geIps | The operation that you want to perform. Valid values: AddBandwidt hPackageIps . |   |   |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the NAT bandwidth plan resides. You can call DescribeRegions interface to obtain the region ID. |   |   |
| IpCount | String | Yes | 2 | The number of public IP addresses in the NAT bandwidth plan. Valid values: 1 ~ 50 . |   |   |
| BandwidthPackageId | String | Yes | bwp-s6lmotmkk**** | The ID of the NAT service plan. |   |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e0**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | EC0B5C51-7F40-44D6- A642-1DE764B547EC | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AddBandwidthPackageIps &RegionId=cn-qingdao-env17-d01 &IpCount=2 &BandwidthPackageId=bwp-s6lmotmkk**** &<Public request parameters>
```

Sample success responses `XML` format

```xml
<AddBandwidthPackageIpsResponse>
  <RequestId>EC0B5C51-7F40-44D6-A642-1DE764B547EC</RequestId>
</AddBandwidthPackageIpsResponse>
```

`JSON` format `{`

```json
  "RequestId": "EC0B5C51-7F40-44D6-A642-1DE764B547EC"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | InvalidIpCount.ValueNot Supported | The specified value of IpCount not supported. | The error message returned because the value of the IpCount parameter is invalid. |
| 400 | QuotaExceeded.Bandwi dthPackageIps | The specified ipCount exceeded quota. | The error message returned because the number of IP addresses has reached the upper limit. Submit a ticket to increase the quota. |

| Developer Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | BandwidthPackage.Fina ncialLocked | The specified BandwidthPackage has been Financail Lock. | The error message returned because the specified NAT service plan is locked due to overdue payments. |

### Elastic IP addresses

#### AllocateEipAddress

Applies for an elastic IP address (EIP). After you call this operation, the system randomly allocates an EIP that is in the Available state in the specified region. EIPs support only the ICMP, TCP, and UDP transport layer protocols. The IGMP and SCTP protocols are not supported. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateEipAddress | The operation that you want to perform. Set the value to Allocat eEipAddress. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where you want to apply for an EIP. You can call the DescribeRegions operation to query region IDs. |
| Bandwidth | String | No | 1 | The bandwidth limit of the EIP. Valid values: 1 to 200. Unit: Mbit/s. Default value: 1. |
| Period | Integer | No | 1 | The subscription duration of the EIP. When PricingCycle is set to Mont h, Period can be set from 1 t o 9. When PricingCycle is set to Year, Period can be set from 1 t o 3. This parameter is required when Inst anceChargeT ype is set to PrePaid. When Inst anceChargeT ype is set to Post Paid, ignore this parameter. Not e This parameter is unavailable for EIPs that are purchased on the Alibaba Cloud International site. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ISP | String | No | BGP | The line type. Default value: BGP. If your account is in the single-path BGP whitelist, you can set the parameter to ChinaT elecom, ChinaUnicom, or ChinaMobile. This parameter is required if your workloads are deployed in the China East 1 Finance region. In this case, set the value to BGP FinanceCloud. _ |
| ActivityId | Long | No | 111111 | The promotion code. You can leave this parameter empty. |
| Netmode | String | No | public | The type of network. Set the value to public (Internet). |
| AutoPay | Boolean | No | false | Specifies whether to enable automatic payment. Valid values: f alse: disables automatic payment. After an order is generated, you must go to the order center to complete the payment. t rue: enables automatic payment. After an order is generated, the system automatically deducts fees from your account balance to pay for the order. This parameter is required when Inst anceChargeT ype is set to PrePaid. When Inst anceChargeT ype is set to Post Paid, this parameter is not required. Not e This parameter is unavailable for EIPs that are purchased on the Alibaba Cloud International site. |
| PricingCycle | String | No | Month | The billing cycle of the subscription EIP. Valid values: Mont h: billed on a monthly basis. This is the default value. Year: billed on an annual basis. This parameter is required when Inst anceChargeT ype is set to PrePaid. When Inst anceChargeT ype is set to Post Paid, this parameter is not required. Not e This parameter is unavailable for EIPs that are purchased on the Alibaba Cloud International site. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceChargeType | String | No | PostPaid | The billing method of the EIP. Valid values: PrePaid: subscription. Post Paid: pay-as-you-go. This is the default value. When Inst anceChargeT ype is set to PrePaid, you must set Int ernet ChargeT ype to PayByBandwidt h. When Inst anceChargeT ype is set to Post Paid, you can set Int ernet ChargeT ype to PayByBandwidt h or PayByT raf f ic. Not e If you want to purchase an EIP from the Alibaba Cloud International site, you must set this parameter to Post Paid (pay-as-you-go). |
| InternetChargeType | String | No | PayByTraffic | The metering method of the EIP. Valid values: PayByBandwidt h: pay-by-bandwidth. This is the default value. PayByT raf f ic: pay-by-data-transfer. When Inst anceChargeT ype is set to PrePaid, Int ernet ChargeT ype must be set to PayByBandwidt h. When Inst anceChargeT ype is set to Post Paid, Int ernet ChargeT ype can be set to PayByBandwidt h or PayByT raf f ic. |
| ResourceGroupId | String | No | rg- acfmxazffggds**** | The ID of the enterprise resource group. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. Client T oken can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| EipAddress | String | 10.XX.XX.78 | The allocated EIP. |
| AllocationId | String | eip-25877c70gddh**** | The ID of the EIP. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | Long | 10 | The order number. This parameter is returned only when Inst anceChargeT ype is set to PrePaid. |
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |
| ResourceGroupId | String | rg-acfmxazfdgdg**** | The ID of the enterprise resource group. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AllocateEipAddress &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AllocateEipAddressrResponse>
  <ResourceGroupId>rg-acfmxazfdgdg****</ResourceGroupId>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
  <AllocationId>eip-25877c70gddh****</AllocationId>
  <EipAddress>10.XX.XX.78</EipAddress>
  <OrderId>10</OrderId>
</AllocateEipAddressrResponse>
```

`JSON` format `{`

```json
    "AllocateEipAddressrResponse": {
        "ResourceGroupId": "rg-acfmxazfdgdg****",
        "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
        "AllocationId": "eip-25877c70gddh****",
        "EipAddress": "10.XX.XX.78",
        "OrderId": 10
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. Apply for permissions and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded | The error message returned because the number of EIPs reaches the quota. You can submit a ticket to request a quota increase. We recommend that you use NAT gateways. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | Specified value of "InternetChargeType" is not valid | The error message returned because InternetChargeType is set to an invalid value. |
| 400 | InvalidParameter | Specified value of "Bandwidth" is not valid. | The error message returned because the specified bandwidth limit is invalid. |
| 400 | InsufficientBalance | Your account does not have enough balance. | The error message returned because the balance in your account is insufficient. Top up your account and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded. | The error message returned because the number of EIPs reaches the quota. You can submit a ticket to request a quota increase. We recommend that you use NAT gateways. |
| 400 | ReserveIpFail | Reserve eip failed. | The error message returned because the system failed to reserve the EIP. |
| 400 | InvalidRegion.NotSuppo rt | The specified region does not support. | The error message returned because the specified region does not support this operation. |
| 400 | InvalidResourceGroupId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID does not exist. |
| 409 | OperationConflict | Request was denied due to conflict with a previos request. | The error message returned because a request conflict occurs. Try again later or submit a ticket to report the problem. |

#### AllocateEipAddressPro

Applies for a specified EIP. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateEipAddressP ro | The operation that you want to perform. Set the value to Allocat eEipAddressPro. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the specified EIP for which you want to apply. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IpAddress | String | No | 12.XX.XX.23 | The IP address of the specified EIP. Specify IpAddress or Inst anceId. If you leave both parameters empty, the system randomly allocates an EIP. |
| InstanceId | String | No | eip- 25877c70gddh**** | The ID of the specified EIP. Specify IpAddress or Inst anceId. If you leave both parameters empty, the system randomly allocates an EIP. |
| Bandwidth | String | No | 5 | The bandwidth limit of the specified EIP. Unit: Mbit/s. Default value: 1. |
| Period | Integer | No | 1 | The subscription duration of the EIP. If PricingCycle is set to Mont h, set Period to a value from 1 to 9. If PricingCycle is set to Year, set Period to a value from 1 to 3. This parameter is required when Inst anceChargeT ype is set to PrePaid. Leave this parameter empty when Inst anceChargeT ype is set to Post Paid. |
| ISP | String | No | BGP | The line type. Default value: BGP. If your account is in the single-path BGP whitelist, you can set the parameter to ChinaT elecom, ChinaUnicom, or ChinaMobile. This parameter is required if your workloads are deployed in the China East 1 Finance region. In this case, set the value to BGP FinanceCloud. _ |
| Netmode | String | No | public | The type of network. Set the value to public (Internet). Default value: public (Internet). |
| Name | String | No | Test123 | The name of the EIP. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter. It cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | abc | The description of the EIP. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment. Valid values: f alse: disables automatic payment. After an order is generated, you must go to the Order Center to make the payment. t rue: enables automatic payment. Payments are automatically made. This parameter is required when Inst anceChargeT ype is set to PrePaid. Leave this parameter empty when Inst anceChargeT ype is set to Post Paid. |
| PricingCycle | String | No | Month | The billing cycle of the subscription EIP. Valid values: Mont h (default): The instance is billed on a monthly basis. Year: The instance is billed on an annual basis. This parameter is required if Inst anceChargeT ype is set to PrePaid. This parameter is optional if Inst anceChargeT ype is set to Post Paid. |
| InstanceChargeType | String | No | PostPaid | The billing method of the specified EIP. Valid values: PrePaid: subscription Post Paid (default): pay-as-you-go If Inst anceChargeT ype is set to PrePaid, you must set Int ernet ChargeT ype to PayByBandwidt h. If Inst anceChargeT ype is set to Post Paid, you can set Int ernet ChargeT ype to PayByBandwidt h or PayByT raf f ic. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InternetChargeType | String | No | PayByBandwidth | The metering method of the specified EIP. Valid values: PayByBandwidt h (default): pay-by- bandwidth PayByT raf f ic: pay-by-data-transfer If Inst anceChargeT ype is set to PrePaid, you must set Int ernet ChargeT ype to PayByBandwidt h. If Inst anceChargeT ype is set to Post Paid, you can set Int ernet ChargeT ype to PayByBandwidt h or PayByT raf f ic. |
| ResourceGroupId | String | No | rg- resourcegroup**** | The ID of the resource group to which the EIP belongs. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. Client T oken can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AllocationId | String | eip-25877c70gddh**** | The ID of the specified EIP. |
| EipAddress | String | 12.XX.XX.23 | The IP address of the specified EIP. |
| OrderId | Long | 20190000 | the ID of the order. |
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |
| ResourceGroupId | String | rg-resourcegroup**** | The ID of the resource group. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AllocateEipAddressPro &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AllocateEipAddressProResponse>
  <ResourceGroupId>rg-resourcegroup****</ResourceGroupId>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
  <AllocationId>eip-25877c70gddh****</AllocationId>
  <EipAddress>12.XX.XX.23</EipAddress>
  <OrderId>20190000</OrderId>
</AllocateEipAddressProResponse>
```

`JSON` format `{`

```json
    "ResourceGroupId": "rg-resourcegroup****",
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
    "AllocationId": "eip-25877c70gddh****",
    "EipAddress": "12.XX.XX.23",
    "OrderId": 20190000
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. Apply for permissions and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded | The error message returned because the number of EIPs reaches the quota. You can submit a ticket to request a quota increase. We recommend that you use NAT gateways. |
| 400 | InvalidParameter | Specified value of "InternetChargeType" is not valid | The error message returned because InternetChargeType is set to an invalid value. |
| 400 | InvalidParameter | Specified value of "Bandwidth" is not valid. | The error message returned because the specified bandwidth limit is invalid. |
| 400 | InsufficientBalance | Your account does not have enough balance. | The error message returned because the balance in your account is insufficient. Top up your account and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded. | The error message returned because the number of EIPs reaches the quota. You can submit a ticket to request a quota increase. We recommend that you use NAT gateways. |
| 400 | ReserveIpFail | Reserve eip failed. | The error message returned because the system failed to reserve the EIP. |
| 400 | InvalidRegion.NotSuppo rt | The specified region does not support. | The error message returned because the specified region does not support this operation. |

| Virtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidResourceGroupId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID does not exist. |

#### AssociateEipAddress

Associates an elastic IP address (EIP) with an instance in the same region. When you call the operation, take note of the following items: You can associate an EIP with an Elastic Compute Service (ECS) instance, a Server Load Balancer (SLB) instance, a secondary elastic network interface (ENI), or a NAT gateway that is deployed in a virtual private cloud (VPC). The EIP and the instance with which you want to associate the EIP must belong to the same region. To associate an EIP with a NAT gateway, make sure that no NAT service plan that was purchased before November 3, 2017 exists in your account. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociateEipAddress | The operation that you want to perform. Valid values: Associat eEipAddress . |
| AllocationId | String | Yes | eip- 2zeerraiwb7ujsxdc** ** | The ID of the EIP that you want to associate with an instance. |
| InstanceId | String | Yes | i- 2zebb08phyczzawe **** | The ID of the instance with which you want to associate the EIP. NAT gateways, SLB instances, ECS instances, secondary ENIs, and high-availability virtual IP addresses (HAVIPs) are supported. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region to which the EIP belongs. |
| InstanceType | String | No | EcsInstance | The type of instance with which you want to associate the EIP. Valid values: Nat : NAT Gateway. SlbInst ance : SLB SLB. EcsInst ance : ECS instances. Net workInt erf ace : auxiliary Elastic Network Interface. HaVip : High-availability virtual IP addresses. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceRegionId | String | No | cn-hangzhou | The ID of the region where the instance to be associated with the EIP is deployed. Not e This parameter is required only when the EIP is associated with a shared-bandwidth Global Accelerator (GA) instance. |
| PrivateIpAddress | String | No | 192.1.XX.XX | An IP address that belongs to the CIDR block of a vSwitch. If you do not set this parameter, the system allocates a private IP address based on the VPC ID and vSwitch ID. |
| Mode | String | No | NAT | The binding mode. Valid values: NAT : NAT mode (normal mode). MULT I BINDED : The multi-EIP network _ interface controller visible mode. BINDED : The visible mode of the EIP network interface controller. Only Inst anceT ype Configure as Net workInt erf ace this parameter is required. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001sdfg | Guaranteed request idempotence. You can use the client to generate the value, but you must ensure that it is unique among different requests. ClientToken Only ASCII characters are supported and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C0FD0EED-F90D-4479- 803D-DD62335357E5 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AssociateEipAddress &AllocationId=eip-2zeerraiwb7ujsxdc**** &InstanceId=i-2zebb08phyczzawe**** &<Public request parameters>
```

Sample success responses `XML` format

```xml
<AssociateEipAddressResponse>
  <RequestId>C0FD0EED-F90D-4479-803D-DD62335357E5</RequestId>
</AssociateEipAddressResponse>
```

`JSON` format `{`

```json
  "RequestId": "C0FD0EED-F90D-4479-803D-DD62335357E5"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidAssociation.Dupli cated | Specified instance already is associated. | The error message returned because an EIP or a GA instance is already associated with the specified instance. You must disassociate the EIP or GA instance from the specified instance before you can perform the operation. |
| 400 | OperationDenied | Specified instance is not in VPC. | The error message returned because the specified instance does not exist in the VPC. |
| 400 | InvalidParameter.Misma tch | Specified elastic IP address and ECS instance are not in the same region. | The error message returned because the specified EIP and ECS instance do not belong to the same region. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation | The error message returned because the state of the EIP does not support the operation. |
| 404 | InvalidInstanId.NotFoun d | Specified instance does not exist. | The error message returned because the specified instance does not exist. Check whether the ID is valid. |
| 400 | IncorrectInstanceStatus | Current instance status does not support this operation. | The error message returned because this operation cannot be performed while the instance is in the current state. |
| 400 | InvalidInstanceType.Val ueNotSupported | The specified value of InstanceType is not supported. | The error message returned because InstanceType is set to an invalid value. |
| 400 | IncorrectHaVipStatus | HaVip can be operated by this action only when it's status is Available or InUse. | The error message returned because the state of the HAVIP does not support the operation. You can perform the operation only when the HAVIP is in the Available or InUse state. |
| 400 | InvalidParameter | The specified parameter is not valid. | The error message returned because the specified value of the parameter is invalid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | OperationDenied | Eip of default vpc not allow this operation | The error message returned because the operation is not supported by EIPs in the default VPC. |
| 400 | Forbbiden | The eip instance owener error | The error message returned because you are unauthorized to perform the operation on the EIP. |
| 400 | InvalidBindingStatus | The eip binding status invalid. | The error message returned because the EIP is in an invalid state. |
| 400 | BIND INSTANCE HAVE P _ _ _ ORTMAP OR BIND EIP _ _ _ | The instance may have portMap or already bind eip. | The error message returned because a port forwarding rule is configured for the ECS instance. Delete the port forwarding rule and try again. |
| 400 | BIND INSTANCE OWENE _ _ R ERROR _ | Cannot operate the eip. | The error message returned because you are unauthorized to manage the specified EIP. |
| 404 | InvalidAllocationId.NotF ound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | InvalidParams.NotFoun d | instance not found | The error message returned because the specified instance does not exist. |
| 503 | ServiceUnavailable | The request has failed due to a temporary failure of the server. | The error message returned because the request failed due to a temporary malfunction of the server. |

#### ModifyEipAddressAttribute

Modifies the name, description, and bandwidth limit of a specified elastic IP address (EIP). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyEipAddressAt tribute | The operation that you want to perform. Set the value to Modif yEipAddressAt t ribut e. |
| AllocationId | String | Yes | eip- 2zeerraiwb7uj6i0d** ** | The ID of the EIP that you want to modify. |
| Bandwidth | String | No | 100 | The bandwidth limit of the EIP. Valid values: 1 to 200. Unit: Mbit/s. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region to which the EIP belongs. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Name | String | No | Test123 | The name of the EIP. The name must be 2 to 128 characters in length, and can contain, digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter. The name cannot start with http:// or https:// . |
| Description | String | No | abc | The description of the EIP. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyEipAddressAttribute &AllocationId=eip-2zeerraiwb7uj6i0d**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyEipAddressAttributeResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ModifyEipAddressAttributeResponse>
```

`JSON` format `{`

```json
    "ModifyEipAddressAttributeResponse": {
        "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InsufficientBalance.Eip | Your account does not have enough balance. | The error message returned because the balance in your account is insufficient. Top up your account and try again. |

| Developer Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidAllocationId.NotF ound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | InvalidParameter | Specified value of "Bandwidth" is not supported. | The error message returned because the specified bandwidth limit is invalid. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation. | The error message returned because the state of the EIP does not support this operation. |
| 404 | InvalidAllocationId.NotF ound | Specified allocation ID is not found.. | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | InvalidParameter | The parameter is invalid. | The error message returned because the parameter is set to an invalid value. |
| 404 | Forbidden.RegionNotFo und | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |

#### DescribeEipAddresses

Queries elastic IP addresses (EIPs) created in a specific region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEipAddresse s | The operation that you want to perform. Set the value to DescribeEipAddresses. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the EIP. You can call the DescribeRegions operation to query the most recent region list. |
| Tag.N.Key | String | No | TestKey | The key of tag N of the instance that you want to query. Valid values of N: 1 to 20. |
| Tag.N.Value | String | No | TestValue | The value of tag N of the instance that you want to query. Valid values of N: 1 to 20. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IncludeReservationD ata | Boolean | No | true | Specify whether to return data of orders that have not taken effect. Valid values: f alse: does not return data of orders that have not taken effect. This is the default value. t rue: returns data of orders that have not taken effect. |
| Status | String | No | Available | The status of the EIP. Valid values: Associat ing: The EIP is being associated with an instance. Unassociat ing: The EIP is being disassociated from an instance. InUse: The EIP is associated with an instance. Available: The EIP is available. |
| EipAddress | String | No | 116.xx.xx.28 | The IP address of the EIP that you want to query. You can enter up to 50 IP addresses of EIPs. Separate multiple IP addresses with commas (,). Not e If both the EipAddress and Allocat ionId parameters are set, you can enter up to 50 IP addresses of EIPs in EipAddress, and enter up to 50 IDs of EIPs in Allocat ionId. |
| AllocationId | String | No | eip- 2zeerraiwb7ujxscd** ** | The ID of the EIP that you want to query. You can enter up to 50 IDs of EIPs. Separate multiple IDs with commas (,). Not e If both the EipAddress and Allocat ionId parameters are set, you can enter up to 50 IDs of EIPs in Allocat ionId, and enter up to 50 IP addresses of EIPs in EipAddress. |
| SegmentInstanceId | String | No | eipsg- t4nr90yik5oy38xdy** ** | The IDs of contiguous EIPs. |
| ResourceGroupId | String | No | rg- acfmxazb4pcdvf**** | The ID of the resource group to which the EIPs belong. |
| PageNumber | Integer | No | 10 | The number of the page to return. Default value: 1. |

|   | Developer Guide·API r | eference |   |   | Virtual Private Clou | d |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 100. Default value: 10. |
| ISP | String | No | BGP | The Internet service provider (ISP). Set the value to BGP. |
| Filter.1.Key | String | No | CreationStartTime | The filter key used to query resources. Set the value to Creat ionSt art T ime, which indicates the time when the system started to create the resource. |
| Filter.2.Key | String | No | CreationEndTime | The filter key used to query resources. Set the value to Creat ionEndT ime, which indicates the time when the system completed creating the resource. |
| Filter.1.Value | String | No | 2018-01-22T09:12Z | The filter value used to query resources. Specify the time in the ISO 8601 standard in YYYY-MM-DDThh:mmZ format. The time must be in UTC. |
| Filter.2.Value | String | No | 2018-01-22T09:15Z | The filter value used to query resources. Specify the time in the ISO 8601 standard in YYYY-MM-DDThh:mmZ format. The time must be in UTC. |
| LockReason | String | No | financial | The reason why the EIP is locked. Valid values: f inancial: The EIP is locked due to overdue payments. securit y: The EIP is locked for security reasons. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AssociatedInstanceT ype | String | No | EcsInstance | The type of the cloud resource with which you want to associate the EIP. Valid values: EcsInst ance: an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC). This is the default value. SlbInst ance: a Server Load Balancer (SLB) instance in a VPC. Nat : a NAT gateway. HaVip: a high-availability virtual IP address (HAVIP). Net workInt erf ace: a secondary elastic network interface (ENI). You can associate only one EIP with each ECS instance, SLB instance, or HAVIP. You can associate multiple EIPs with each NAT gateway. The number of EIPs that can be associated with a secondary ENI depends on the EIP association mode. |
| AssociatedInstanceI d | String | No | i- 2zebb08phyccdvf*** * | The ID of the cloud resource with which the EIP is associated. |
| ChargeType | String | No | None | The billing method of the EIP. Valid values: Post Paid: pay-as-you-go PrePaid: subscription |
| DryRun | Boolean | No | false | Specifies whether to precheck only this request. Valid values: t rue: prechecks the request only. EIPs are not queried. The system checks the required parameters, request syntax, and service limits. If the request fails the precheck, the corresponding error message is returned. If the request passes the precheck, the DryRunOperation error code is returned. f alse: prechecks the request. This is the default value. After the request passes the check, a 2xx HTTP status code is returned and EIPs are queried. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| EipAddresses | Array of EipAddress |   | The details about the EIP. |
| EipAddress |   |   |   |
| AllocationId | String | eip- 2zeerraiwb7ujcdvf**** | The ID of the EIP. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |   |   |
|---|---|---|---|---|---|
| AllocationTime | String | 2019-04-23T01:37:38Z | The time when the EIP was created. |   |   |
| AvailableRegions | List | cn-east-hangzhou-01 | The ID of the region to which the EIP belongs. |   |   |
| Bandwidth | String | 5 | The bandwidth limit of the EIP. Unit: Mbit/s. |   |   |
| BandwidthPackag eBandwidth | String | 50 | The bandwidth of the EIP bandwidth plan. Unit: Mbit/s. |   |   |
| BandwidthPackag eId | String | cbwp- bp1ego3i4j07ccdvf**** | The ID of the EIP bandwidth plan. |   |   |
| BandwidthPackag eType | String | CommonBandwidthPac kage | The type of the bandwidth. Only CommonBandwidt hPackage (EIP Bandwidth Plan) is returned. |   |   |
| ChargeType | String | PostPaid | The billing method of the EIP. PrePaid: subscription Post Paid: pay-as-you-go |   |   |
| DeletionProtectio n | Boolean | true | Indicates whether deletion protection is enabled. Valid values: t rue: enabled f alse: disabled |   |   |
| Descritpion | String | abc | The description of the EIP. |   |   |
| EipBandwidth | String | 101 | The bandwidth limit of the EIP when it is not associated with an EIP bandwidth plan. |   |   |
| ExpiredTime | String | 2019-04-29T02:00Z | The expiration date. The time follows the ISO 8601 standard and is displayed in UTC. Format: YYYY- MM-ddTHH:mmZ . |   |   |
|   |   |   |   | YYYY- |   |
| HDMonitorStatus | String | false | Indicates whether fine-grained monitoring is enabled for the EIP. Valid values: f alse: disabled t rue: enabled |   |   |
| HasReservationDa ta | String | false | Indicates whether renewal data is included. This parameter returns t rue only when the IncludeReservat ionDat a parameter is set to t rue and some orders have not taken effect. |   |   |

|   | MM-ddTHH:mmZ |
|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ISP | String | BGP | The ISP. |
| InstanceId | String | i-bp15zckdt37cdvf**** | The ID of the instance with which the EIP is associated. |
| InstanceRegionId | String | cn-east-hangzhou-01 | The region ID of the associated resource. |
| InstanceType | String | EcsInstance | The type of the instance associated with the EIP. Valid values: EcsInst ance: an ECS instance in a VPC. SlbInst ance: an SLB instance in a VPC. Nat : a NAT gateway. HaVip: an HAVIP. Net workInt erf ace: a secondary ENI. |
| InternetChargeTyp e | String | PayByBandwidth | The metering method of the EIP. Valid values: PayByBandwidt h: pay-by-bandwidth PayByT raf f ic: pay-by-data-transfer |
| IpAddress | String | 101.xx.xx.36 | The IP address of the EIP. |
| Mode | String | NAT | The association mode. Valid values: NAT (default): the standard NAT mode MULT I BINDED: multi-EIP-to-ENI mode _ BINDED: cut-through mode This parameter is returned only when Inst anceT ype is set to Net workInt erf ace. |
| Name | String | test | The name of the EIP. |
| Netmode | String | public | The type of network. The value public (Internet) is returned. |
| OperationLocks | Array of LockReason |   | The details about the locked EIP. |
| LockReason |   |   |   |
| LockReason | String | financial | The reason why the EIP is locked. Valid values: f inancial: The EIP is locked due to overdue payments. securit y: The EIP is locked for security reasons. |
| PrivateIpAddress | String | 192.1.XX.XX | An IP address in the CIDR block of the vSwitch. |

|   | Developer Guide·AP | I reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RegionId | String | cn-east-hangzhou-01 | The ID of the region to which the EIP belongs. |
| ReservationActive Time | String | 2019-03-11T16:00:00Z | The time when the renewal takes effect. |
| ReservationBandw idth | String | 12 | The bandwidth after the renewal takes effect. |
| ReservationInterne tChargeType | String | PayByBandwidth | The metering method of the renewal. Valid values: PayByBandwidt h: pay-by-bandwidth PayByT raf f ic: pay-by-data-transfer |
| ReservationOrderT ype | String | RENEWCHANGE | The type of the renewal order. Valid values: RENEWCHANGE: upgrade or downgrade T EMP UPGRADE: temporary upgrade _ UPGRADE: upgrade |
| ResourceGroupId | String | rg-acfmxazcdxs**** | The ID of the resource group. |
| SecondLimited | Boolean | false | Indicates whether level-2 throttling is configured. Valid values: t rue: yes f alse: no |
| SegmentInstanceI d | String | eipsg- t4nr90yik5oy38xdyjth8 | The IDs of contiguous EIPs. This value is returned only when contiguous EIPs are specified. |
| Status | String | Associating | The status of the EIP. Valid values: Associat ing: The EIP is being associated with an instance. Unassociat ing: The EIP is being disassociated from an instance. InUse: The EIP is associated with an instance. Available: The EIP is available. |
| Tags | Array of Tag |   | The tags used to query resources. |
| Tag |   |   |   |
| Key | String | testX | The filter key used to query resources. |
| Value | String | testY | The filter value used to query resources. |
| TotalCount | Integer | 10 | The total number of entries returned. |

|   | Virtual Private Clou | d |   | Developer Guide·API reference |   |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 10 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEipAddresses &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeEipAddressesResponse>
  <TotalCount>10</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
  <EipAddresses>
        <HDMonitorStatus>false</HDMonitorStatus>
        <PrivateIpAddress>192.1.XX.XX</PrivateIpAddress>
        <ResourceGroupId>rg-acfmxazcdxs****</ResourceGroupId>
        <AllocationId>eip-2zeerraiwb7ujcdvf****</AllocationId>
        <SecondLimited>false</SecondLimited>
        <Name>test</Name>
        <SegmentInstanceId>eipsg-t4nr90yik5oy38xdyjth8</SegmentInstanceId>
        <ReservationOrderType>RENEWCHANGE</ReservationOrderType>
        <InstanceRegionId>cn-east-hangzhou-01</InstanceRegionId>
        <ExpiredTime>2019-04-29T02:00Z</ExpiredTime>
        <Bandwidth>5</Bandwidth>
        <BandwidthPackageId>cbwp-bp1ego3i4j07ccdvf****</BandwidthPackageId>
        <ReservationActiveTime>2019-03-11T16:00:00Z</ReservationActiveTime>
        <InstanceType>EcsInstance</InstanceType>
        <ReservationBandwidth>12</ReservationBandwidth>
        <Status>Associating</Status>
        <InstanceId>i-bp15zckdt37cdvf****</InstanceId>
        <Mode>NAT</Mode>
        <ISP>BGP</ISP>
        <HasReservationData>false</HasReservationData>
        <DeletionProtection>true</DeletionProtection>
        <BandwidthPackageType>CommonBandwidthPackage</BandwidthPackageType>
        <BandwidthPackageBandwidth>50</BandwidthPackageBandwidth>
        <ReservationInternetChargeType>PayByBandwidth</ReservationInternetChargeType>
        <InternetChargeType>PayByBandwidth</InternetChargeType>
        <AllocationTime>2019-04-23T01:37:38Z</AllocationTime>
        <Descritpion>abc</Descritpion>
        <EipBandwidth>101</EipBandwidth>
        <Netmode>public</Netmode>
        <ChargeType>PostPaid</ChargeType>
        <IpAddress>101.xx.xx.36</IpAddress>
        <RegionId>cn-east-hangzhou-01</RegionId>
        <OperationLocks>
              <LockReason>financial</LockReason>
        </OperationLocks>
        <Tags>
              <Value>testY</Value>
              <Key>testX</Key>
        </Tags>
        <AvailableRegions>cn-east-hangzhou-01</AvailableRegions>
  </EipAddresses>
  <PageNumber>10</PageNumber>
</DescribeEipAddressesResponse>
```

`JSON` format `{`

```json
    "TotalCount": 10,
    "PageSize": 10,
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
    "EipAddresses": {
        "HDMonitorStatus": false,
        "PrivateIpAddress": "192.1.XX.XX",
        "ResourceGroupId": "rg-acfmxazcdxs****",
        "AllocationId": "eip-2zeerraiwb7ujcdvf****",
        "SecondLimited": false,
        "Name": "test",
        "SegmentInstanceId": "eipsg-t4nr90yik5oy38xdyjth8",
        "ReservationOrderType": "RENEWCHANGE",
        "InstanceRegionId": "cn-east-hangzhou-01",
        "ExpiredTime": "2019-04-29T02:00Z",
        "Bandwidth": 5,
        "BandwidthPackageId": "cbwp-bp1ego3i4j07ccdvf****",
        "ReservationActiveTime": "2019-03-11T16:00:00Z",
        "InstanceType": "EcsInstance",
        "ReservationBandwidth": 12,
        "Status": "Associating",
        "InstanceId": "i-bp15zckdt37cdvf****",
        "Mode": "NAT",
        "ISP": "BGP",
        "HasReservationData": false,
        "DeletionProtection": true,
        "BandwidthPackageType": "CommonBandwidthPackage",
        "BandwidthPackageBandwidth": 50,
        "ReservationInternetChargeType": "PayByBandwidth",
        "InternetChargeType": "PayByBandwidth",
        "AllocationTime": "2019-04-23T01:37:38Z",
        "Descritpion": "abc",
        "EipBandwidth": 101,
        "Netmode": "public",
        "ChargeType": "PostPaid",
        "IpAddress": "101.xx.xx.36",
        "RegionId": "cn-east-hangzhou-01",
        "OperationLocks": {
            "LockReason": "financial"
```

`},`

```json
        "Tags": {
            "Value": "testY",
            "Key": "testX"
```

`},`

```json
        "AvailableRegions": "cn-east-hangzhou-01"
```

`},`

```json
    "PageNumber": 10
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | Forbidden.RegionNotFo und | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the region is valid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidLockReason.NotF ound | The specified LockReason is not found | The error message returned because the reason why the EIP is locked is unknown. |
| 400 | InvalidIAssociatedInstan ceType.ValueNotSuppo rted | The specified value of AssociatedInstanceType is not supported. | The error message returned because AssociatedInstanceType is set to an invalid value. Check whether the value is valid. |
| 400 | InvalidChargeType.Valu eNotSupported | The specified ChargeType is not supported. | The error message returned because the specified billing method is not supported. Set a supported billing method. |
| 400 | InvalidResourceGroupId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID does not exist. |
| 400 | OperationUnsupported. ResourceGroupId | ResourceGroup is not supported in this region. | The error message returned because the resource group feature is disabled. |

#### UnassociateEipAddress

Disassociates an elastic IP address (EIP) from an instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociateEipAddr ess | The operation that you want to perform. Set the value to Unassociat eEipAddress. |
| AllocationId | String | Yes | eip- 2zeerraiwb7uj6i0d** ** | The ID of the EIP that you want to disassociate. |
| InstanceId | String | Yes | i- hp3akk9irtd69jad*** * | The ID of the instance from which you want to disassociate the EIP. |
| Force | Boolean | No | false | Specifies whether to disassociate the EIP from a NAT gateway if a DNAT or SNAT entry is added to the NAT gateway. Valid values: f alse (default): does not disassociate the EIP from a NAT gateway if a DNAT or SNAT entry is added to the NAT gateway. t rue: disassociates the EIP from a NAT gateway if a DNAT or SNAT entry is added to the NAT gateway. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region to which the EIP belongs. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceType | String | No | EcsInstance | The type of instance from which you want to disassociate the EIP. Valid values: EcsInst ance (default): an Elastic Compute Service (ECS) instance that is deployed in a virtual private cloud (VPC) SlbInst ance: a Server Load Balancer (SLB) instance that is deployed in a VPC Net workInt erf ace: a secondary elastic network interface (ENI) that is deployed in a VPC Nat : a NAT gateway HaVip a high-availability virtual IP address (HAVIP) |
| PrivateIpAddress | String | No | 192.XX.XX.2 | The private IP address of the ECS instance or the secondary ENI from which you want to disassociate the EIP. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001*** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. ClientToken can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UnassociateEipAddress &AllocationId=eip-2zeerraiwb7uj6i0d**** &InstanceId=i-hp3akk9irtd69jad**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UnassociateEipAddressResponse>
   <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</UnassociateEipAddressResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidAllocationId.NotF ound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation. | The error message returned because the state of the EIP does not support this operation. |
| 400 | InvalidInstanceId.NotFo und | Specified instance does not exist. | The error message returned because the specified instance does not exist. Check whether the specified instance is valid. |
| 400 | IncorrectInstanceStatus | The current status of instance does not support this operation. | The error message returned because the state of the instance does not support the operation. |
| 400 | InvalidInstanceType.Val ueNotSupported | The specified value of InstanceType is not supported. | The error message returned because InstanceType is set to an invalid value. |
| 400 | IncorrectHaVipStatus | This operation is denied because satus of the specified HaVip is neither Available nor InUse. | The error message returned because you cannot perform the operation when the specified HAVIP is in the Available or InUse state. |
| 400 | OperationDenied | Eip of default vpc not allow this operation | The error message returned because EIPs in the default VPC do not support the operation. |
| 404 | Forbidden.RegionNotFo und | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |
| 400 | InvalidParameter | The specified parameter is not valid. | The error message returned because the parameter is set to an invalid value. |
| 400 | Forbbiden | The eip instance owener error | The error message returned because you are unauthorized to perform the operation on the EIP. |
| 400 | InvalidBindingStatus | The eip binding status invalid. | The error message returned because the binding mode of the EIP is invalid. |

#### ReleaseEipAddress

Releases a specified elastic IP address (EIP). Before you release an EIP, make sure that the EIP meets the following requirements: You can release only EIPs that are in the Available state. You can release only EIPs that are billed on a pay-as-you-go basis. You cannot release subscription EIPs. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleaseEipAddress | The operation that you want to perform. Set the value to ReleaseEipAddress. |
| AllocationId | String | Yes | eip- 2zeerraiwb7uj6i0d** ** | The ID of the EIP that you want to release. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region to which the EIP belongs. You can call the DescribeRegions operation to query region IDs. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 748C38F6-9A3D-482E- 83FB-DB6C39C68AEA | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ReleaseEipAddress &AllocationId=eip-2zeerraiwb7uj6i0d**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ReleaseEipAddressResponse>
      <RequestId>748C38F6-9A3D-482E-83FB-DB6C39C68AEA</RequestId>
</ReleaseEipAddressResponse>
```

`JSON` format `{`

```json
  "RequestId": "748C38F6-9A3D-482E-83FB-DB6C39C68AEA"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidAllocationId.NotF ound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation. | The error message returned because the state of the EIP does not support this operation. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 404 | Forbidden.RegionNotFo und | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |
| 400 | Forbidden.ChargeTypeIs Prepaid | It's forbidden to release a prepaid EIP | The error message returned because you cannot release subscription EIPs. |
| 400 | Forbbiden | The eip instance owener error | The error message returned because you are unauthorized to perform the operation on the EIP. |
| 400 | TaskConflict.AssociateG lobalAccelerationInstan ce | Operate too frequent. | The error message returned because the number of requests that you send exceeds the upper limit. |

#### DescribeEipGatewayInfo

Queries information about the gateway and subnet mask of an elastic IP address (EIP). You can query only EIPs that are associated with secondary elastic network interfaces (ENIs) in multi-EIP to ENI mode. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEipGatewayI nfo | The operation that you want to perform. Set the value to DescribeEipGat ewayInf o. |
| InstanceId | String | Yes | eni- bp1d66qjxb3qoin3** ** | The ID of the secondary ENI that is associated with the EIP. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region to which the EIP that you want to query belongs. You can call the DescribeRegions operation to query region IDs. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The status code of the operation. |
| EipInfos | Array of EipInfo |   | Detailed information about the EIP. |
| EipInfo |   |   |   |
| Ip | String | 47.XX.XX.236 | The IP address of the EIP. |
| IpGw | String | 47.XX.XX.1 | The IP address of the gateway that is associated with the EIP. |
| IpMask | String | 255.255.255.0 | The subnet mask of the EIP. |
| Message | String | successful | The result of the operation. |
| RequestId | String | C0FD0EED-F90D-4479- 803D-DD62335357E5 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEipGatewayInfo &InstanceId=eni-bp1d66qjxb3qoin3**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeEipGatewayInfoResponse>
  <Message>successful</Message>
  <RequestId>C0FD0EED-F90D-4479-803D-DD62335357E5    </RequestId>
  <Code>200</Code>
  <EipInfos>
        <IpMask>255.255.255.0</IpMask>
        <IpGw>47.XX.XX.1</IpGw>
        <Ip>47.XX.XX.236</Ip>
  </EipInfos>
</DescribeEipGatewayInfoResponse>
```

`JSON` format `{`

```json
    "Message": "successful",
    "RequestId": "C0FD0EED-F90D-4479-803D-DD62335357E5",
    "Code": 200,
    "EipInfos": {
        "IpMask": "255.255.255.0",
        "IpGw": "47.XX.XX.1",
        "Ip": "47.XX.XX.236"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. Apply for permissions and try again. |

#### DescribeHighDefinitionMonitorLogAttribute

Queries configurations about the fine-grained monitoring feature of an elastic IP address (EIP). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHighDefiniti onMonitorLogAttrib ute | The operation that you want to perform. Set the value to DescribeHighDef init ionMonit orLogAt t rib ut e. |
| InstanceId | String | Yes | eip- wz9fi6qboho9fwgx 7**** | The ID of the instance whose fine-grained monitoring configurations you want to query. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list. |
| InstanceType | String | No | EIP | The type of the instance. Set the value to EIP. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceId | String | eip- wz9fi6qboho9fwgx7*** * | The ID of the instance whose fine-grained monitoring configurations you want to query. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceType | String | EIP | The type of the monitoring instance that is queried. The value is set to EIP. |
| LogProject | String | hdmonitor-cn-qingdao- 165820696**** | The name of the project of Log Service. |
| LogStore | String | hdmonitor | The name of the Logstore of Log Service. |
| RequestId | String | 54B48E3D-DF70-471B- AA93-08E683A1B457 | The ID of the request. |
| Success | String | true | Indicates whether the operation is performed. Valid values: t rue: yes f alse: no |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeHighDefinitionMonitorLogAttribute &InstanceId=eip-wz9fi6qboho9fwgx7**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeHighDefinitionMonitorLogAttribute>
  <RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457</RequestId>
  <LogStore>hdmonitor</LogStore>
  <InstanceId>eip-wz9fi6qboho9fwgx7****</InstanceId>
  <InstanceType>EIP</InstanceType>
  <LogProject>hdmonitor-cn-qingdao-165820696****</LogProject>
  <Success>true</Success>
</DescribeHighDefinitionMonitorLogAttribute>
```

`JSON` format `{`

```json
    "DescribeHighDefinitionMonitorLogAttribute": {
        "RequestId": "54B48E3D-DF70-471B-AA93-08E683A1B457",
        "LogStore": "hdmonitor",
        "InstanceId": "eip-wz9fi6qboho9fwgx7****",
        "InstanceType": "EIP",
        "LogProject": "hdmonitor-cn-qingdao-165820696****",
        "Success": true
```

### HAVIPs

#### CreateHaVip

Creates a high-availability virtual IP address (HAVIP). Descriptions When you call this operation, take note of the following rules: You can create a maximum of five HAVIPs for a virtual private cloud (VPC). Before you delete a VPC, you must delete the HAVIPs that you have created for it. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateHaVip | The operation that you want to perform. Set the value to Creat eHaVip. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where you want to create an HAVIP. You can call the DescribeRegions operation to the most recent region list. |
| VSwitchId | String | Yes | vsw-asdfjlnau**** | The ID of the vSwitch to which the HAVIP belongs. |
| Name | String | No | test | The name of the HAVIP. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001s**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |
| IpAddress | String | No | 192.XX.XX.10 | The IP address of the HAVIP. If this parameter is not set, an idle IP address of the specified vSwitch is randomly allocated to the HAVIP. |
| Description | String | No | This is my HaVip. | The description of the HAVIP. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| HaVipId | String | havip- 2zeo05qre24nhrqp**** | The ID of the HAVIP. |
| IpAddress | String | 192.XX.XX.10 | The IP address of the HAVIP. |
| RequestId | String | C44F62BE-9CE7-4277- B117-69243F3988BF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateHaVip &RegionId=cn-qingdao-env17-d01 &VSwitchId=vsw-asdfjlnau**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateHaVipResponse>
  <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
  <IpAddress>192.XX.XX.10</IpAddress>
  <HaVipId>havip-2zeo05qre24nhrqp****</HaVipId>
</CreateHaVipResponse>
```

`JSON` format `{`

```json
    "RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF",
    "IpAddress": "192.XX.XX.10",
    "HaVipId": "havip-2zeo05qre24nhrqp****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | Specified value of "regionId" is not supported. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |
| 404 | InvalidVSwitchId.NotFou nd | The specified VSwitch does not exist in the specified region. | The error message returned because the specified vSwitch does not exist in the specified region. |
| 400 | InvalidDescription.Malfo rmed | The specified Description is wrongly formed. | The error message returned because the format of the specified description is invalid. The description must be 2 to 256 characters in length. It cannot start with http:// or https://. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | CountLimitExceed.HaVip InVpc | Specified Vpc exceeds the quota of max number of ha-vip count. | The error message returned because the number of HAVIPs in the VPC has reached the upper limit. |
| 403 | QuotaExceeded.HaVip | Living HaVip quota exceeded. | The error message returned because the number of active HAVIPs has reached the upper limit. |
| 400 | InvalidIPAddress.OutOfR ange | The specified IPAddress is out of VSwitch CIDR. | The error message returned because the specified IP address does not fall within the CIDR block of the vSwitch. |
| 400 | InvalidIPAddress.NotAva ilable | The specified IPAddress is not available because it is a system reserved IPAddress. | The error message returned because the specified IP address is reserved by the system and cannot be used. |
| 400 | InvalidIPAddress.Alread yUsed | The specified IPAddress is already used by other resource. | The error message returned because the specified IP address is already used by another resource. |

#### DescribeHaVips

Queries high-availability virtual IP addresses (HAVIPs) in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHaVips | The operation that you want to perform. Set the value to DescribeHaVips. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where you want to create an HAVIP. You can call the DescribeRegions operation to query the most recent region list. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Filter.N.Key | String | No | HaVipId.havip- bp149uyvut73dpldu **** | Specifies filter conditions. You can specify at most five filter conditions. Valid values of n: 1 t o 5. You can specify multiple values for each filter condition. The logical operator among multiple values is OR. If one value is matched, the filter condition is met. The logical operator among multiple filter conditions is AND, in which case all the filter conditions must be met for an HAVIP to be included in the result. The following filter conditions are available: VpcId: the ID of the virtual private cloud (VPC). VSwit chId: the ID of the vSwitch. St at us: the status of the HAVIP. HaVipId: the ID of the HAVIP. HaVipAddress: the IP address of the HAVIP. |
| Filter.N.Value.N | RepeatList | No | 1 | Specifies the value of the filter condition. Valid values of N: 1 t o 5. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| HaVips | Array of HaVip |   | The details about the HAVIP. |
| HaVip |   |   |   |
| AssociatedEipAdd resses | List | 121.XX.XX.1 | The list of elastic IP addresses (EIPs) that are associated with the HAVIP. |
| AssociatedInstanc eType | String | EcsInstance | The type of the instance that is associated with the HAVIP. |
| AssociatedInstanc es | List | i- bp145q7glnuzdvzu21** ** | The Elastic Compute Service (ECS) instances that are associated with the HAVIP. |
| ChargeType | String | none | The parameter is invalid. No value is returned. |
| CreateTime | String | 2018-07-03T14:25:26Z | The time when the HAVIP was created. |
| Description | String | My HaVip | The description of the HAVIP. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| HaVipId | String | havip- bp149uyvut73dpld**** | The ID of the HAVIP. |
| IpAddress | String | 192.XX.XX.27 | The private IP address of the HAVIP. |
| MasterInstanceId | String | i-bp145q7glnuzdvz**** | The ID of the instance that has obtained the private IP address of the HAVIP. |
| Name | String | test | The name of the HAVIP. |
| RegionId | String | cn-qingdao-env17-d01 | The ID of the region where the HAVIP is deployed. |
| Status | String | Available | The status of the HAVIP. |
| VSwitchId | String | vsw- bp1pkt1fba8e824ez**** | The ID of the vSwitch to which the HAVIP belongs. |
| VpcId | String | vpc- bp1kcm36tevkpms9**** | The ID of the VPC to which the HAVIP belongs. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 33E480C5-B46F-4CA5- B6FD-D77C746E86AB | The ID of the request. |
| TotalCount | Integer | 1 | The total number of entries returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeHaVips &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeHaVipsResponse>
  <TotalCount>1</TotalCount>
  <HaVips>
        <Status>Available</Status>
        <Description>My HaVip</Description>
        <VpcId>vpc-bp1kcm36tevkpms9****</VpcId>
        <MasterInstanceId>i-bp145q7glnuzdvz****</MasterInstanceId>
        <ChargeType>none</ChargeType>
        <CreateTime>2018-07-03T14:25:26Z</CreateTime>
        <VSwitchId>vsw-bp1pkt1fba8e824ez****</VSwitchId>
        <IpAddress>192.XX.XX.27</IpAddress>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <HaVipId>havip-bp149uyvut73dpld****</HaVipId>
        <AssociatedInstanceType>EcsInstance</AssociatedInstanceType>
        <Name>test</Name>
        <AssociatedInstances>i-bp145q7glnuzdvzu21****</AssociatedInstances>
        <AssociatedEipAddresses>121.XX.XX.1</AssociatedEipAddresses>
  </HaVips>
  <PageSize>10</PageSize>
  <RequestId>33E480C5-B46F-4CA5-B6FD-D77C746E86AB</RequestId>
  <PageNumber>1</PageNumber>
</DescribeHaVipsResponse>
```

`JSON` format `{`

```json
    "DescribeHaVipsResponse": {
        "TotalCount": 1,
        "HaVips": {
            "Status": "Available",
            "Description": "My HaVip",
            "VpcId": "vpc-bp1kcm36tevkpms9****",
            "MasterInstanceId": "i-bp145q7glnuzdvz****",
            "ChargeType": "none",
            "CreateTime": "2018-07-03T14:25:26Z",
            "VSwitchId": "vsw-bp1pkt1fba8e824ez****",
            "IpAddress": "192.XX.XX.27",
            "RegionId": "cn-qingdao-env17-d01",
            "HaVipId": "havip-bp149uyvut73dpld****",
            "AssociatedInstanceType": "EcsInstance",
            "Name": "test",
            "AssociatedInstances": "i-bp145q7glnuzdvzu21****",
            "AssociatedEipAddresses": "121.XX.XX.1"
```

`},`

```json
        "PageSize": 10,
        "RequestId": "33E480C5-B46F-4CA5-B6FD-D77C746E86AB",
        "PageNumber": 1
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidFilterKey.ValueNo tSupported | Specified filter key is not supported: Filter.X.key | The error message returned because Filter.X.key is not supported. |

#### ModifyHaVipAttribute

Modifies the description of a high-availability virtual IP address (HAVIP). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyHaVipAttribut e | The operation that you want to perform. Set the value to: Modif yHaVipAt t ribut e. |
| HaVipId | String | Yes | havip- 2zeo05qre24nhrqp* *** | The ID of the HAVIP that you want to modify. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region to which the HAVIP belongs. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e0**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | This is my HaVip. | The description of the HAVIP. |
| Name | String | No | test | The name of the HAVIP. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C44F62BE-9CE7-4277- B117-69243F3988BF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyHaVipAttribute &HaVipId=havip-2zeo05qre24nhrqp**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyHaVipAttributeResponse>
  <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
</ModifyHaVipAttributeResponse>
```

`JSON` format `{`

```json
"RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidHaVipId.NotFoun d | The specified HaVip does not exist in the specified region. | The error message returned because the HAVIP does not exist in the specified region. Specify another region ID and try again. |
| 400 | IncorrectStatus | HaVip can be deleted only when it's status is Available or InUse. | The error message returned because the HAVIP is unavailable and failed to be deleted. |
| 400 | InvalidDescription.Malfo rmed | The specified Description is wrongly formed. | The error message returned because the format of the specified description is invalid. The description must be 2 to 256 characters in length. It cannot start with http:// or https://. |

#### AssociateHaVip

Associates a high-availability virtual IP address (HAVIP) with an Elastic Compute Service (ECS) instance. Descriptions When you call this operation, take note of the following limits: The HAVIP takes effect immediately after it is associated with an ECS instance. You do not need to restart the ECS instance. However, you must associate the HAVIP with the elastic network interface (ENI) of the ECS instance. The HAVIP and ECS instance must belong to the same vSwitch. You can associate an HAVIP with at most two ECS instances. The ECS instance must be in the Running or Stopped state. The HAVIP must be in the Available or InUse state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociateHaVip | The operation that you want to perform. Set the value to Associat eHaVip. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HaVipId | String | Yes | havip- 2zeo05qre24nhrqpy f*** | The ID of the HAVIP. |
| InstanceId | String | Yes | i-faf344422ffsfa**** | The ID of the ECS instance with which you want to associate the HAVIP. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the HAVIP. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate a value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |
| InstanceType | String | No | ecs.g6.large | The type of the ECS instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C44F62BE-9CE7-4277- B117-69243F3988BF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AssociateHaVip &HaVipId=havip-2zeo05qre24nhrqpyf*** &InstanceId=i-faf344422ffsfa**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AssociateHaVipResponse>
  <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
</AssociateHaVipResponse>
```

`JSON` format `{`

```json
"RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidHaVipId.NotFoun d | The specified HaVip does not exist in the specified region. | The error message returned because the specified HAVIP does not exist in the specified region. Check the region. |
| 404 | InvalidInstanceId.NotFo und | The specified Instance does not exist in the specified region. | The error message returned because the instance does not exist in the specified region. |
| 400 | IncorrectHaVipStatus | HaVip can be operated by this action only when it's status is Available or InUse. | The error message returned because this operation can be performed only when the HAVIP is in the Available or InUse state. |
| 400 | CountLimitExceed.HaVip OnInstance | The amount of HaVip associated with the specified Instance reach its limits. | The error message returned because the number of HAVIPs has reached the upper limit. |
| 400 | CountLimitExceeded.Ha VipOnECSInstance | The amount of Instance associated with the specified HaVip reach its limits. | The error message returned because the number of ECS instances associated with the specified HAVIP has reached the upper limit. |
| 400 | InvalidNetworkInterface Id.NotFound | The network interface is not found. | The error message returned because the specified ENI does not exist. |

#### UnassociateHaVip

Disassociates a high-availability virtual IP address (HAVIP) from an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC). Descriptions When you call this operation, take note of the following limits: The ECS instance must be in the Running or Stopped state. The HAVIP must be in the Available or InUse state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociateHaVip | The operation that you want to perform. Set the value to Unassociat eHaVip. |
| HaVipId | String | Yes | havip- 2zeo05qre24nhrqpy f**** | The ID of the HAVIP. |
| InstanceId | String | Yes | i-faf344422ffsfa**** | The ID of the ECS instance that you want to disassociate. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the HAVIP. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |
| InstanceType | String | No | ecs.g5.large | The type of the ECS instance. |
| Force | String | No | True | Specifies whether to forcibly disassociate the HAVIP from the ECS instance. Valid values: T rue and False (default). Not e If you set this parameter to False, you cannot disassociate the HAVIP from a primary ECS instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C44F62BE-9CE7-4277- B117-69243F3988BF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UnassociateHaVip &HaVipId=havip-2zeo05qre24nhrqpyf**** &InstanceId=i-faf344422ffsfa**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UnassociateHaVipResponse>
  <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
</UnassociateHaVipResponse>
```

`JSON` format `{`

```json
"RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidHaVipId.NotFoun d | The specified HaVip does not exist in the specified region. | The error message returned because the specified HAVIP does not exist in the specified region. Check whether the region is correct. |
| 404 | InvalidInstanceId.NotFo und | The specified Instance does not exist in the specified region. | The error message returned because the instance does not exist in the specified region. |
| 400 | IncorrectHaVipStatus | HaVip can be operated by this action only when it's status is InUse. | The error message returned because the operation can be performed only when the HAVIP is in the InUse state. |
| 400 | IncorrectInstanceStatus | ECS instance can be operated by this action only when it's status is Running or Stopped. | The error message returned because the operation can be performed only when the ECS instance is in the Running or Stopped state. |
| 400 | ResourceNotAssociated | The HaVip and ECS instance are not associated. | The error message returned because the HAVIP is not associated with the ECS instance. |
| 400 | Forbidden.Unassociate Master | Unassociating a master instance is not allowed unless the parameter Force is True. | The error message returned because the Force parameter is set to False. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 400 | InvalidNetworkInterface Id.NotFound | The network interface is not found. | The error message returned because the specified elastic network interface (ENI) does not exist. |

#### DeleteHaVip

Deletes a high-availability virtual IP address (HAVIP). When you call this operation, take note of the following rules: You can delete only HAVIPs that are in the Available state. Make sure that no routes are destined for the HAVIP that you want to delete. Make sure that no elastic IP addresses (EIPs) are associated with the HAVIP that you want to delete. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteHaVip | The operation that you want to perform. Set the value to Delet eHaVip. |

| Developer Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HaVipId | String | Yes | havip- 2zeo05qre24nhrqpy f**** | The ID of the HAVIP that you want to delete. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where you want to create an HAVIP. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C44F62BE-9CE7-4277- B117-69243F3988BF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteHaVip &HaVipId=havip-2zeo05qre24nhrqpyf**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteHaVipResponse>
  <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
</DeleteHaVipResponse>
```

`JSON` format `{`

```json
"RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidHaVipId.NotFoun d | The specified HaVip does not exist in the specified region. | The error message returned because the specified HAVIP does not exist in the specified region. Check the region. |
| 400 | IncorrectStatus | HaVip can be deleted only when it is status is Available. | The error message returned because the HAVIP cannot be deleted. The error message returned because the HAVIP is not in the Available state. |
| 400 | DependencyViolation.H aVipReferedByRouteEnt ry | HaVip cannot be deleted when it is refered by a route table entry as next hop. | The error message returned because the HAVIP functions as the next hop of a route entry and cannot be deleted. You must delete the route entry before you can delete the HAVIP. |
| 400 | DependencyViolation.H aVipAssociatedWithEIP | HaVip cannot be deleted when it is associated with EIP. | The error message returned because the HAVIP is associated with an elastic IP address (EIP) and cannot be deleted. |

### ACLs

#### CreateNetworkAcl

Creates a network access control list (ACL). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateNetworkAcl | The operation that you want to perform. Set the value to Creat eNet workAcl. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region to which the network ACL belongs. You can call the DescribeRegions operation to the most recent region list. |
| VpcId | String | Yes | vpc- dsfd34356vdf**** | The ID of the virtual private cloud (VPC) to which you want to apply the network ACL. |
| NetworkAclName | String | No | acl-1 | The name of the network ACL. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter and cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | This is my NetworkAcl. | The description of the network ACL. The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkAclAttribu te | Struct |   | The attributes of the network ACL. |
| CreationTime | String | 2019-04-25 11:33:27 | The time when the network ACL was created. |
| Description | String | This is my NetworkAcl. | The description of the network ACL. |
| EgressAclEntries | Array of EgressAclEntry |   | The outbound rules. |
| EgressAclEntry |   |   |   |
| Description | String | This is EgressAclEntries. | The description of the outbound rule. |
| DestinationCidrIp | String | 10.0.0.0/24 | The destination CIDR block. |
| EntryType | String | custom | The type of the rule. Valid values: cust om: a custom rule. syst em: a system rule. |
| NetworkAclEntryId | String | nae- a2d447uw4tillxsdc**** | The ID of the outbound rule. |
| NetworkAclEntryN ame | String | acl-2 | The name of the outbound rule. |
| Policy | String | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Port | String | -1/-1 | The destination ports. |
| Protocol | String | all | The transport layer protocols. Valid values: icmp gre t cp udp all: all protocols supported |
| IngressAclEntries | Array of IngressAclEntry |   | The inbound rules. |
| IngressAclEntry |   |   |   |
| Description | String | This is IngressAclEntries. | The description of the inbound rule. |
| EntryType | String | custom | The type of the rule. Valid values: cust om: a custom rule. syst em: a system rule. |
| NetworkAclEntryId | String | nae- a2dk86arlydmexscd**** | The ID of the inbound rule. |
| NetworkAclEntryN ame | String | acl-3 | The name of the inbound rule. |
| Policy | String | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |
| Port | String | -1/-1 | The source ports. |
| Protocol | String | all | The transport layer protocols. Valid values: icmp gre t cp udp all: all protocols supported |
| SourceCidrIp | String | 10.0.0.0/24 | The source CIDR block. |
| NetworkAclId | String | nacl- a2do9e413e0spdefr**** | The description of the network ACL. |
| NetworkAclName | String | acl-1 | The name of the network ACL. |

|   | Developer Guide·AP | I reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RegionId | String | cn-qingdao-env17-d01 | The region where the network ACL is deployed. |
| Resources | Array of Resource |   | The resources that are associated with the network ACL. |
| Resource |   |   |   |
| ResourceId | String | vsw- bp1de348lntdwgthy*** * | The ID of the associated resource. |
| ResourceType | String | VSwitch | The type of the associated resource. |
| Status | String | BINDED | The state of the associated resource. Valid values: BINDED: The resource is associated with the network ACL. BINDING: The resource is being associated with the network ACL. UNBINDING: The resource is disassociated from the network ACL. |
| Status | String | Modifying | The state of the network ACL. Valid values: Available: The network ACL is available for use. Modif ying: The network ACL is being configured. |
| VpcId | String | vpc- a2d33rfpl72k5xsscd**** | The ID of the VPC to which the network ACL applies. |
| NetworkAclId | String | nacl- a2do9e413e0spzasx*** * | The description of the network ACL. |
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateNetworkAcl &RegionId=cn-qingdao-env17-d01 &VpcId=vpc-dsfd34356vdf**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateNetworkAclResponse>
  <NetworkAclId>nacl-a2do9e413e0spzasx****</NetworkAclId>
  <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
  <NetworkAclAttribute>
        <Status>Modifying</Status>
        <Description>This is my NetworkAcl.</Description>
        <VpcId>vpc-a2d33rfpl72k5xsscd****</VpcId>
        <NetworkAclId>nacl-a2do9e413e0spdefr****</NetworkAclId>
        <CreationTime>2019-04-25 11:33:27</CreationTime>
        <NetworkAclName>acl-1 </NetworkAclName>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <IngressAclEntries>
              <Policy>accept</Policy>
              <Description>This is IngressAclEntries. </Description>
              <EntryType>custom</EntryType>
              <Port>-1/-1 </Port>
              <SourceCidrIp>10.0.0.0/24 </SourceCidrIp>
              <NetworkAclEntryName>acl-3 </NetworkAclEntryName>
              <Protocol>all</Protocol>
              <NetworkAclEntryId>nae-a2dk86arlydmexscd****</NetworkAclEntryId>
        </IngressAclEntries>
        <EgressAclEntries>
              <Policy>accept</Policy>
              <Description>This is EgressAclEntries.</Description>
              <EntryType>custom</EntryType>
              <DestinationCidrIp>10.0.0.0/24</DestinationCidrIp>
              <Port>-1/-1 </Port>
              <NetworkAclEntryName>acl-2</NetworkAclEntryName>
              <Protocol>all</Protocol>
              <NetworkAclEntryId>nae-a2d447uw4tillxsdc****</NetworkAclEntryId>
        </EgressAclEntries>
        <Resources>
              <Status>BINDED</Status>
              <ResourceId>vsw-bp1de348lntdwgthy****</ResourceId>
              <ResourceType>VSwitch</ResourceType>
        </Resources>
  </NetworkAclAttribute>
</CreateNetworkAclResponse>
```

`JSON` format `{`

```json
    "NetworkAclId": "nacl-a2do9e413e0spzasx****",
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0",
    "NetworkAclAttribute": {
        "Status": "Modifying",
        "Description": "This is my NetworkAcl.",
        "VpcId": "vpc-a2d33rfpl72k5xsscd****",
        "NetworkAclId": "nacl-a2do9e413e0spdefr****",
        "CreationTime": "2019-04-25 11:33:27",
        "NetworkAclName": "acl-1",
        "RegionId": "cn-qingdao-env17-d01",
        "IngressAclEntries": {
            "Policy": "accept",
            "Description": "This is IngressAclEntries.",
            "EntryType": "custom",
            "Port": "-1/-1",
            "SourceCidrIp": "10.0.0.0/24",
            "NetworkAclEntryName": "acl-3",
            "Protocol": "all",
            "NetworkAclEntryId": "nae-a2dk86arlydmexscd****"
```

`},`

```json
        "EgressAclEntries": {
            "Policy": "accept",
            "Description": "This is EgressAclEntries.",
            "EntryType": "custom",
            "DestinationCidrIp": "10.0.0.0/24",
            "Port": "-1/-1",
            "NetworkAclEntryName": "acl-2",
            "Protocol": "all",
            "NetworkAclEntryId": "nae-a2d447uw4tillxsdc****"
```

`},`

```json
        "Resources": {
            "Status": "BINDED",
            "ResourceId": "vsw-bp1de348lntdwgthy****",
            "ResourceType": "VSwitch"
```

#### AssociateNetworkAcl

Associates a network access control list (ACL) with a vSwitch. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociateNetworkAc l | The operation that you want to perform. Set the value to Associat eNet workAcl. |
| NetworkAclId | String | Yes | nacl- a2do9e413e0spxscd **** | The ID of the network ACL. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region to which the network ACL belongs. You can call the DescribeRegions operation to query the most recent region list. |
| Resource.N.Resource Type | String | No | VSwitch | The type of the resource with which you want to associate the network ACL. Set the value to VSwit ch. |
| Resource.N.Resource Id | String | No | vsw- bp1de348lntdwbgn h**** | The ID of the resource with which you want to associate the network ACL. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4CF20CC7-D1FC-425B- A15B-DF7C8E2131A7 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AssociateNetworkAcl &NetworkAclId=nacl-a2do9e413e0spxscd**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AssociateNetworkAclResponse>
     <RequestId>4CF20CC7-D1FC-425B-A15B-DF7C8E2131A7</RequestId>
</AssociateNetworkAclResponse>
```

`JSON` format `{`

```json
    "RequestId":"4CF20CC7-D1FC-425B-A15B-DF7C8E2131A7"
```

#### ModifyNetworkAclAttributes

Modifies the attributes of a network access control list (ACL). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNetworkAclAt tributes | The operation that you want to perform. Set the value to Modif yNet workAclAt t ribut es. |
| NetworkAclId | String | Yes | acl-bp1lhl0taik**** | The ID of the network ACL. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region where to which the network ACL belongs. You can call the DescribeRegions operation to query the most recent region list. |
| NetworkAclName | String | No | acl-1 | The name of the network ACL. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter and cannot start with http:// or https:// . |
| Description | String | No | This is my NetworkAcl. | The description of the network ACL. The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It must be 1 to 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8F76C3E4-B39F-465D- B8B3-50BAF03CA833 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyNetworkAclAttributes &NetworkAclId=acl-bp1lhl0taik**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success response `XML` format

```xml
<ModifyNetworkAclAttributesResponse>
     <RequestId>8F76C3E4-B39F-465D-B8B3-50BAF03CA833</RequestId>
</ModifyNetworkAclAttributesResponse>
```

`JSON` format `{`

```json
    "RequestId": "8F76C3E4-B39F-465D-B8B3-50BAF03CA833"
```

#### UpdateNetworkAclEntries

Updates the rules of a network access control list (ACL). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateNetworkAclE ntries | The operation that you want to perform. Set the value to Updat eNet workAclEnt ries. |
| NetworkAclId | String | Yes | nacl- bp1lhl0taikrzxsc**** | The ID of the network ACL. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region to which the network ACL belongs. You can call the DescribeRegions operation to query the most recent region list. |
| IngressAclEntries.N. NetworkAclEntryNa me | String | No | acl-3 | The name of the inbound rule. |
| IngressAclEntries.N. NetworkAclEntryId | String | No | nae- 2zepn32de59j8m4** ** | The ID of the inbound rule. |
| IngressAclEntries.N.P olicy | String | No | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |
| IngressAclEntries.N.P rotocol | String | No | all | The transport layer protocols. Valid values: icmp: Internet Control Message Protocol (ICMP) gre: Generic Routing Encapsulation (GRE) t cp: TCP udp: UDP all: All protocols are supported. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IngressAclEntries.N.S ourceCidrIp | String | No | 10.0.0.0/24 | The source CIDR block. |
| IngressAclEntries.N.P ort | String | No | -1/-1 | The source ports. |
| IngressAclEntries.N.E ntryType | String | No | custom | The type of the rule. Valid values: cust om (default): a custom rule. syst em: a system rule. |
| IngressAclEntries.N.D escription | String | No | This is IngressAclEntries. | The description of the inbound rule. |
| EgressAclEntries.N.N etworkAclEntryNam e | String | No | acl-2 | The name of the outbound rule. |
| EgressAclEntries.N.N etworkAclEntryId | String | No | nae- 2zecs97e0brcge46** ** | The ID of the outbound rule. |
| EgressAclEntries.N.P olicy | String | No | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |
| EgressAclEntries.N.Pr otocol | String | No | all | The transport layer protocols. Valid values: icmp: ICMP gre: GRE t cp: TCP udp: UDP all: All protocols are supported. |
| EgressAclEntries.N.D estinationCidrIp | String | No | 10.0.0.0/24 | The destination CIDR block. |
| EgressAclEntries.N.P ort | String | No | -1/-1 | The destination ports. |
| EgressAclEntries.N.E ntryType | String | No | custom | The type of the rule. Valid values: cust om (default): a custom rule syst em: a system rule |
| EgressAclEntries.N.D escription | String | No | This is EgressAclEntries. | The description of the outbound rule. |
| UpdateIngressAclEnt ries | Boolean | No | false | Specifies whether to update the inbound rule. Valid rules: t rue: updates the inbound rule. f alse (default): does not update the inbound rule. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UpdateEgressAclEntr ies | Boolean | No | false | Specifies whether to update the outbound rule. Valid rules: t rue: updates the outbound rule. f alse (default): does not update the outbound rule. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to guarantee the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1170A5A0-E760-4331- 9133-A7D38D973215 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UpdateNetworkAclEntries &NetworkAclId=nacl-bp1lhl0taikrzxsc**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UpdateNetworkAclEntriesResponse>
     <RequestId>1170A5A0-E760-4331-9133-A7D38D973215</RequestId>
</UpdateNetworkAclEntriesResponse>
```

`JSON` format `{`

```json
    "RequestId": "1170A5A0-E760-4331-9133-A7D38D973215"
```

#### UnassociateNetworkAcl

Disassociates a network access control list (ACL) from a vSwitch. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociateNetwork Acl | The operation that you want to perform. Set the value to Unassociat eNet workAcl. |
| NetworkAclId | String | Yes | nacl- a2do9e413e0sp**** | The ID of the network ACL. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region where the network ACL is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| Resource.N.Resource Type | String | No | VSwitch | The type of the resource associated with the network ACL. |
| Resource.N.Resource Id | String | No | vsw- bp1de348lntdw**** | The ID of the associated resource. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | AD024BAA-2D91-48FD- 810B-8FB7489B6EE6 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UnassociateNetworkAcl &NetworkAclId=nacl-a2do9e413e0sp**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success response `XML` format

```xml
<UnassociateNetworkAclResponse>
     <RequestId>AD024BAA-2D91-48FD-810B-8FB7489B6EE6</RequestId>
</UnassociateNetworkAclResponse>
```

`JSON` format `{`

```json
    "RequestId": "AD024BAA-2D91-48FD-810B-8FB7489B6EE6"
```

#### CopyNetworkAclEntries

Copies rules of a network access control list (ACL). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CopyNetworkAclEntr ies | The operation that you want to perform. Set the value to CopyNet workAclEnt ries. |
| NetworkAclId | String | Yes | nacl- a2do9e413e0sp**** | The ID of the network ACL. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region to which the network ACL belongs. You can call the DescribeRegions operation to query the most recent region list. |
| SourceNetworkAclId | String | Yes | nacl- ghuo9ehg3e0sp**** | The ID of the network ACL whose rules you want to copy. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6608E72F-F276-440F- ABEF-419971CEC4D1 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CopyNetworkAclEntries &NetworkAclId=nacl-a2do9e413e0sp**** &RegionId=cn-qingdao-env17-d01 &SourceNetworkAclId=nacl-ghuo9ehg3e0sp**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CopyNetworkAclEntriesResponse>
     <RequestId>6608E72F-F276-440F-ABEF-419971CEC4D1</RequestId>
</CopyNetworkAclEntriesResponse>
```

`JSON` format `{`

```json
    "RequestId": "6608E72F-F276-440F-ABEF-419971CEC4D1"
```

#### DeleteNetworkAcl

Deletes a network access control list (ACL). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteNetworkAcl | The operation that you want to perform. Set the value to Delet eNet workAcl. |
| NetworkAclId | String | Yes | nacl- bp1q8bgx4xnkm**** | The ID of the network ACL. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The ID of the region to which the network ACL belongs. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 34F1206D-04B0-4A05- 9D8A-80521E288BD1 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteNetworkAcl &NetworkAclId=nacl-bp1q8bgx4xnkm**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteNetworkAclResponse>
     <RequestId>34F1206D-04B0-4A05-9D8A-80521E288BD1</RequestId>
</DeleteNetworkAclResponse>
```

`JSON` format `{`

```json
    "RequestId": "34F1206D-04B0-4A05-9D8A-80521E288BD1"
```

#### DescribeNetworkAcls

Queries network ACLs. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeNetworkAcl s | The operation that you want to perform. Set the value to DescribeNet workAcls. |
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region where the network ACL is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| NetworkAclId | String | No | nacl- bp1lhl0taikrbgnh**** | The description of the network ACL. |
| NetworkAclName | String | No | acl-1 | The name of the network ACL. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter and cannot start with http:// or https:// . |
| VpcId | String | No | vpc-1234**** | The ID of the VPC to which the network ACL applies. |
| ResourceType | String | No | VSwitch | The type of the associated instance. Set the value to VSwit ch. This parameter is valid only when ResourceType and ResourceId are both set. |
| ResourceId | String | No | vsw- bp1de348lntdwnhb g**** | The ID of the associated instance. This parameter is valid only when ResourceType and ResourceId are both set. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | The token used to ensure idempotence. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkAcls | Array of NetworkAcl |   | The details about the network ACL. |
| NetworkAcl |   |   |   |
| CreationTime | String | 2019-04-25 11:44:17 | The time when the network ACL was created. |
| Description | String | This is my NetworkAcl. | The description of the network ACL. |
| EgressAclEntries | Array of EgressAclEntry |   | The outbound rules. |
| EgressAclEntry |   |   |   |
| Description | String | This is EgressAclEntries. | The description of the outbound rule. |
| DestinationCidrIp | String | 10.0.0.0/24 | The destination CIDR block. |
| EntryType | String | custom | The type of the rule. Valid values: cust om: a custom rule syst em: a system rule |
| NetworkAclEntryId | String | nae- a2d447uw4tillfvgb**** | The ID of the outbound rule. |
| NetworkAclEntryN ame | String | acl-2 | The name of the outbound rule. |
| Policy | String | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |
| Port | String | -1/-1 | The destination ports. |

|   | Virtual Private Clou | d |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Protocol | String | all | The transport layer protocols. Valid values: icmp: Internet Control Message Protocol (ICMP) gre: Generic Routing Encapsulation (GRE) t cp: TCP udp: UDP all: All protocols are supported. |
| IngressAclEntries | Array of IngressAclEntry |   | Information about inbound rules. |
| IngressAclEntry |   |   |   |
| Description | String | This is IngressAclEntries. | The description of the inbound rule. |
| EntryType | String | custom | The type of the rule. Valid values: cust om: a custom rule syst em: a system rule |
| NetworkAclEntryId | String | nae- a2dk86arlydmezasw*** * | The ID of the inbound rule. |
| NetworkAclEntryN ame | String | acl-3 | The name of the inbound rule. |
| Policy | String | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |
| Port | String | -1/-1 | The source ports. |
| Protocol | String | all | The transport layer protocols. Valid values: icmp: ICMP gre: GRE t cp: TCP udp: UDP all: All protocols are supported. |
| SourceCidrIp | String | 10.0.0.0/24 | The source CIDR block. |
| NetworkAclId | String | nacl- a2do9e413e0spxscd*** * | The ID of the network ACL. |
| NetworkAclName | String | acl-8 | The name of the network ACL. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| OwnerId | Long | 12345678 | The ID of the Apsara Stack tenant account to which the network ACL belongs. |
| RegionId | String | cn-qingdao-env17-d01 | The ID of the region to which the network ACL belongs. |
| Resources | Array of Resource |   | The resources that are associated with the network ACL. |
| Resource |   |   |   |
| ResourceId | String | vsw- bp1de348lntdwcdf**** | The ID of the resource with which you want to associate the network ACL. |
| ResourceType | String | VSwitch | The type of the associated resource. |
| Status | String | BINDED | The status of the associated resource. Valid values: BINDED: The resource is associated with the network ACL. BINDING: The resource is being associated with the network ACL. UNBINDING: The resource is disassociated from the network ACL. |
| Status | String | Available | The status of the network ACL. Valid values: Available: The network ACL is available for use. Modif ying: The network ACL is being configured. |
| VpcId | String | vpc- a2d33rfpl72k5defr**** | The ID of the associated VPC. |
| PageNumber | String | 1 | The page number of the returned page. |
| PageSize | String | 10 | The number of entries on the current page. |
| RequestId | String | F7DDDC17-FA06-4AC2- 8F35-59D2470FCFC1 | The ID of the request. |
| TotalCount | String | 2 | The total number of entries returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeNetworkAcls &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeNetworkAclsResponse>
  <TotalCount>2</TotalCount>
  <NetworkAcls>
        <Status>Available</Status>
        <Description>This is my NetworkAcl.</Description>
        <OwnerId>12345678</OwnerId>
        <VpcId>vpc-a2d33rfpl72k5defr****</VpcId>
        <NetworkAclId>nacl-a2do9e413e0spxscd****</NetworkAclId>
        <CreationTime>2019-04-25 11:44:17</CreationTime>
        <NetworkAclName>acl-8</NetworkAclName>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <IngressAclEntries>
              <Policy>accept</Policy>
              <Description>This is IngressAclEntries. </Description>
              <EntryType>custom</EntryType>
              <Port>-1/-1 </Port>
              <SourceCidrIp>10.0.0.0/24 </SourceCidrIp>
              <NetworkAclEntryName>acl-3 </NetworkAclEntryName>
              <Protocol>all</Protocol>
              <NetworkAclEntryId>nae-a2dk86arlydmezasw****</NetworkAclEntryId>
        </IngressAclEntries>
        <EgressAclEntries>
              <Policy>accept</Policy>
              <Description>This is EgressAclEntries. </Description>
              <EntryType>custom</EntryType>
              <DestinationCidrIp>10.0.0.0/24 </DestinationCidrIp>
              <Port>-1/-1 </Port>
              <NetworkAclEntryName>acl-2 </NetworkAclEntryName>
              <Protocol>all</Protocol>
              <NetworkAclEntryId>nae-a2d447uw4tillfvgb****</NetworkAclEntryId>
        </EgressAclEntries>
        <Resources>
              <Status>BINDED</Status>
              <ResourceId>vsw-bp1de348lntdwcdf****</ResourceId>
              <ResourceType>VSwitch</ResourceType>
        </Resources>
  </NetworkAcls>
  <PageSize>10</PageSize>
  <RequestId>F7DDDC17-FA06-4AC2-8F35-59D2470FCFC1</RequestId>
  <PageNumber>1</PageNumber>
</DescribeNetworkAclsResponse>
```

`JSON` format `{`

```json
    "TotalCount": 2,
    "NetworkAcls": {
        "Status": "Available",
        "Description": "This is my NetworkAcl.",
        "OwnerId": 12345678,
        "VpcId": "vpc-a2d33rfpl72k5defr****",
        "NetworkAclId": "nacl-a2do9e413e0spxscd****",
        "CreationTime": "2019-04-25 11:44:17",
        "NetworkAclName": "acl-8",
        "RegionId": "cn-qingdao-env17-d01",
        "IngressAclEntries": {
            "Policy": "accept",
            "Description": "This is IngressAclEntries.",
            "EntryType": "custom",
            "Port": "-1/-1",
            "SourceCidrIp": "10.0.0.0/24",
            "NetworkAclEntryName": "acl-3",
            "Protocol": "all",
            "NetworkAclEntryId": "nae-a2dk86arlydmezasw****"
```

`},`

```json
        "EgressAclEntries": {
            "Policy": "accept",
            "Description": "This is EgressAclEntries.",
            "EntryType": "custom",
            "DestinationCidrIp": "10.0.0.0/24",
            "Port": "-1/-1",
            "NetworkAclEntryName": "acl-2",
            "Protocol": "all",
            "NetworkAclEntryId": "nae-a2d447uw4tillfvgb****"
```

`},`

```json
        "Resources": {
            "Status": "BINDED",
            "ResourceId": "vsw-bp1de348lntdwcdf****",
            "ResourceType": "VSwitch"
```

`},`

```json
    "PageSize": 10,
    "RequestId": "F7DDDC17-FA06-4AC2-8F35-59D2470FCFC1",
    "PageNumber": 1
```

#### DescribeNetworkAclAttributes

Queries details about a network access control list (ACL). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeNetworkAcl Attributes | The operation that you want to perform. Set the value to DescribeNet workAclAt t ribut es. |
| NetworkAclId | String | Yes | nacl- a2do9e413e0spzasx **** | The ID of the network ACL. |

|   | Virtual Private Cloud |   |   |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env17- d01 | The region ID of the network ACL. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkAclAttribu te | Struct |   | The details about the network ACL. |
| CreationTime | String | 2019-04-25 11:33:27 | The time when the network ACL was created. |
| Description | String | This is my NetworkAcl. | The description of the network ACL. |
| EgressAclEntries | Array of EgressAclEntry |   | The information about outbound rules of the network ACL. |
| EgressAclEntry |   |   |   |
| Description | String | This is EgressAclEntries. | The description of the outbound rule. |
| DestinationCidrIp | String | 10.0.0.0/24 | The destination CIDR block. |
| EntryType | String | custom | The type of the rule. Valid values: cust om: a custom rule syst em: a system rule |
| NetworkAclEntryId | String | nae- a2d447uw4tillxdcv**** | The ID of the outbound rule. |
| NetworkAclEntryN ame | String | acl-2 | The name of the outbound rule. |
| Policy | String | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Port | String | -1/-1 | The destination port range. |
| Protocol | String | all | The transport layer protocol. Valid values: icmp: Internet Control Message Protocol (ICMP) gre: Generic Routing Encapsulation (GRE) t cp: TCP udp: UDP all: all protocols |
| IngressAclEntries | Array of IngressAclEntry |   | The information about inbound rules of the network ACL. |
| IngressAclEntry |   |   |   |
| Description | String | This is IngressAclEntries. | The description of the inbound rule. |
| EntryType | String | custom | The type of the rule. Valid values: cust om: a custom rule syst em: a system rule |
| NetworkAclEntryId | String | nae- a2dk86arlydmevfbg**** | The ID of the inbound rule. |
| NetworkAclEntryN ame | String | acl-3 | The name of the inbound rule. |
| Policy | String | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |
| Port | String | -1/-1 | The source port range. |
| Protocol | String | all | The transport layer protocol. Valid values: icmp: ICMP gre: GRE t cp: TCP udp: UDP all: all protocols |
| SourceCidrIp | String | 10.0.0.0/24 | The CIDR block of the source address. |
| NetworkAclId | String | nacl- a2do9e413e0spnhmj*** * | The ID of the network ACL. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkAclName | String | acl-1 | The name of the network ACL. |
| OwnerId | Long | 12345678 | The ID of the Apsara Stack tenant account to which the network ACL belongs. |
| RegionId | String | cn-qingdao-env17-d01 | The region ID of the network ACL. |
| Resources | Array of Resource |   | The resources that are associated with the network ACL. |
| Resource |   |   |   |
| ResourceId | String | vsw- bp1de348lntdwxscd*** * | The ID of the associated resource. |
| ResourceType | String | VSwitch | The type of the associated resource. |
| Status | String | BINDED | The status of the associated resource. Valid values: BINDED: The resource is associated with the network ACL. BINDING: The resource is being associated with the network ACL. UNBINDING: The resource is disassociated from the network ACL. |
| Status | String | Available | The status of the associated resource. Valid values: Available: The resource is available. Modif ying: The resource is being configured. |
| VpcId | String | vpc- a2d33rfpl72k5defr**** | The ID of the virtual private cloud (VPC) to which the network ACL applies. |
| RequestId | String | F5905F9C-0161-4E72- 9CB1-1F3F3CF6268A | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeNetworkAclAttributes &NetworkAclId=nacl-a2do9e413e0spzasx**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeNetworkAclAttributesResponse>
  <RequestId>F5905F9C-0161-4E72-9CB1-1F3F3CF6268A</RequestId>
  <NetworkAclAttribute>
        <Status>Available</Status>
        <Description>This is my NetworkAcl.</Description>
        <OwnerId>12345678</OwnerId>
        <VpcId>vpc-a2d33rfpl72k5defr****</VpcId>
        <NetworkAclId>nacl-a2do9e413e0spnhmj****</NetworkAclId>
        <CreationTime>2019-04-25 11:33:27</CreationTime>
        <NetworkAclName>acl-1</NetworkAclName>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <IngressAclEntries>
              <Policy>accept</Policy>
              <Description>This is IngressAclEntries.</Description>
              <EntryType>custom</EntryType>
              <Port>-1/-1</Port>
              <SourceCidrIp>10.0.0.0/24</SourceCidrIp>
              <NetworkAclEntryName>acl-3</NetworkAclEntryName>
              <Protocol>all</Protocol>
              <NetworkAclEntryId>nae-a2dk86arlydmevfbg****</NetworkAclEntryId>
        </IngressAclEntries>
        <EgressAclEntries>
              <Policy>accept</Policy>
              <Description>This is EgressAclEntries.</Description>
              <EntryType>custom</EntryType>
              <DestinationCidrIp>10.0.0.0/24</DestinationCidrIp>
              <Port>-1/-1</Port>
              <NetworkAclEntryName>acl-2</NetworkAclEntryName>
              <Protocol>all</Protocol>
              <NetworkAclEntryId>nae-a2d447uw4tillxdcv****</NetworkAclEntryId>
        </EgressAclEntries>
        <Resources>
              <Status>BINDED</Status>
              <ResourceId>vsw-bp1de348lntdwxscd****</ResourceId>
              <ResourceType>VSwitch</ResourceType>
        </Resources>
  </NetworkAclAttribute>
</DescribeNetworkAclAttributesResponse>
```

`JSON` format `{`

```json
    "RequestId": "F5905F9C-0161-4E72-9CB1-1F3F3CF6268A",
    "NetworkAclAttribute": {
        "Status": "Available",
        "Description": "This is my NetworkAcl.",
        "OwnerId": 12345678,
        "VpcId": "vpc-a2d33rfpl72k5defr****",
        "NetworkAclId": "nacl-a2do9e413e0spnhmj****",
        "CreationTime": "2019-04-25 11:33:27",
        "NetworkAclName": "acl-1",
        "RegionId": "cn-qingdao-env17-d01",
        "IngressAclEntries": {
            "Policy": "accept",
            "Description": "This is IngressAclEntries.",
            "EntryType": "custom",
            "Port": "-1/-1",
            "SourceCidrIp": "10.0.0.0/24",
            "NetworkAclEntryName": "acl-3",
            "Protocol": "all",
            "NetworkAclEntryId": "nae-a2dk86arlydmevfbg****"
```

`},`

```json
        "EgressAclEntries": {
            "Policy": "accept",
            "Description": "This is EgressAclEntries.",
            "EntryType": "custom",
            "DestinationCidrIp": "10.0.0.0/24",
            "Port": "-1/-1",
            "NetworkAclEntryName": "acl-2",
            "Protocol": "all",
            "NetworkAclEntryId": "nae-a2d447uw4tillxdcv****"
```

`},`

```json
        "Resources": {
            "Status": "BINDED",
            "ResourceId": "vsw-bp1de348lntdwxscd****",
            "ResourceType": "VSwitch"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |

### IPv6 gateways

#### CreateIpv6Gateway

Creates an IPv6 gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateIpv6Gateway | The operation that you want to perform. Set the value to Creat eIpv6Gat eway. |
| RegionId | String | Yes | cn-neimeng-env133- d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- 123sedrfswd23**** | The ID of the virtual private cloud (VPC) for which you want to create the IPv6 gateway. |
| Spec | String | No | Small | The specification of the IPv6 gateway. Valid values: Small (default): Free Edition Medium: Enterprise Edition Large: Enhanced Enterprise Edition The forwarding capacity of an IPv6 gateway varies based on the specification. |
| Name | String | No | ipv6GW | The name of the IPv6 gateway. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | ipv6gatewayforVPC 1 | The description of the IPv6 gateway. The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6GatewayId | String | ipv6gw- hp3y0l3ln89j8cdvf**** | The ID of the IPv6 gateway. |
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateIpv6Gateway &RegionId=cn-neimeng-env133-d01 &VpcId=vpc-123sedrfswd23**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateIpv6GatewayResponse>
        <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
        <Ipv6GatewayId>ipv6gw-hp3y0l3ln89j8cdvf****</Ipv6GatewayId>
</CreateIpv6GatewayResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0",
    "Ipv6GatewayId": "ipv6gw-hp3y0l3ln89j8cdvf****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidVpcId.NotFound | Specified VPC does not exist. | The error message returned because the specified VPC does not exist. |

#### DeleteIpv6Gateway

Deletes an IPv6 gateway. Before you delete an Enterprise Edition or Enhanced Enterprise Edition IPv6 gateway, you must delete the egress-only rules configured on the IPv6 gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteIpv6Gateway | The operation that you want to perform. Set the value to Delet eIpv6Gat eway. |
| Ipv6GatewayId | String | Yes | ipv6gw- hp3y0l3ln89j8**** | The ID of the IPv6 gateway that you want to delete. |
| RegionId | String | Yes | cn-neimeng-env133- d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E9A8AABE-A84B-4AF2- A68A-8E2EA190E7AE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteIpv6Gateway &Ipv6GatewayId=ipv6gw-hp3y0l3ln89j8**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteIpv6GatewayResponse>
      <RequestId>E9A8AABE-A84B-4AF2-A68A-8E2EA190E7AE</RequestId>
</DeleteIpv6GatewayResponse>
```

`JSON` format `{`

```json
 "RequestId": "E9A8AABE-A84B-4AF2-A68A-8E2EA190E7AE"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### DescribeIpv6Gateways

Queries IPv6 gateways in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Gatewa ys | The operation that you want to perform. Set the value to DescribeIpv6Gat eWays. |
| RegionId | String | Yes | cn-neimeng-env133- d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6GatewayId | String | No | ipv6gw-123456**** | The ID of the IPv6 gateway. |

| Virtual Private Cloud |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpcId | String | No | vpc-123456**** | The ID of the virtual private cloud (VPC) to which the IPv6 gateway belongs. |
| Name | String | No | ipv6GW**** | The name of the IPv6 gateway. |
| PageNumber | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6Gateways | Array of Ipv6Gateway |   | The details about the IPv6 gateways. |
| Ipv6Gateway |   |   |   |
| BusinessStatus | String | Normal | The status of the IPv6 gateway. Valid values: Normal: normal FinancialLocked: locked due to overdue payments |
| CreationTime | String | 2020-12-20T14:51:23Z | The time when the IPv6 gateway was created. |
| Description | String | descriptionforIPv6GW | The description of the IPv6 gateway. |
| ExpiredTime | String | 2020-12-21T14:51:23Z | The time when the IPv6 gateway expires. |
| InstanceChargeTy pe | String | PostPaid | The metering method of the IPv6 gateway. |
| Ipv6GatewayId | String | ipv6gw- hp3rwmtmfhgis**** | The ID of the IPv6 gateway. |
| Name | String | name | The name of the IPv6 gateway. |
| RegionId | String | cn-neimeng-env133- d01 | The region ID of the IPv6 gateway. |
| Spec | String | Small | The specification of the IPv6 gateway. Small: Free Edition Medium: Enterprise Edition Large: Enhanced Enterprise Edition |
| Status | String | Available | The status of the IPv6 gateway. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|
| Parameter | Type | Example | Description |
| VpcId | String | vpc-123456**** | The ID of the VPC to which the IPv6 gateway belongs. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 19 | The number of entries returned per page. |
| RequestId | String | E3A06196-3E7C-490D- 8F39-CB4B5A0CE8AD | The ID of the request. |
| TotalCount | Integer | 2 | The total number of entries returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeIpv6Gateways &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeIpv6GatewaysResponse>
   <PageNumber>1</PageNumber>
   <Ipv6Gateways>
      <Ipv6Gateway>
         <Name></Name>
         <CreationTime>2018-12-20T14:51:23Z</CreationTime>
         <Status>Available</Status>
         <Description></Description>
         <BusinessStatus>Normal</BusinessStatus>
         <Spec>Medium</Spec>
         <RegionId>cn-huhehaote</RegionId>
         <InstanceChargeType>PostPaid</InstanceChargeType>
         <ExpiredTime></ExpiredTime>
         <VpcId>vpc-hp3ag7ydchedxxxxxxxxx</VpcId>
         <Ipv6GatewayId>ipv6gw-hp33of4uz4k4kxxxxxxxx</Ipv6GatewayId>
      </Ipv6Gateway>
      <Ipv6Gateway>
         <CreationTime>2018-12-05T09:21:35Z</CreationTime>
         <Name>IPv6 gateway</Name>
         <Status>Available</Status>
         <Description></Description>
         <BusinessStatus>Normal</BusinessStatus>
         <Spec>Medium</Spec>
         <RegionId>cn-huhehaote</RegionId>
         <InstanceChargeType>PostPaid</InstanceChargeType>
         <ExpiredTime></ExpiredTime>
         <VpcId>vpc-hp3kzilwd9yflxxxxxxxx</VpcId>
         <Ipv6GatewayId>ipv6gw-hp33p10bdbt77xxxxxxxx</Ipv6GatewayId>
      </Ipv6Gateway>
   </Ipv6Gateways>
   <TotalCount>2</TotalCount>
   <PageSize>10</PageSize>
   <RequestId>E3A06196-3E7C-490D-8F39-CB4B5A0CE8AD</RequestId>
</DescribeIpv6GatewaysResponse>
```

`JSON` format `{`

```json
    "PageNumber": 1,
    "Ipv6Gateways": {
        "Ipv6Gateway": [
```

`{`

```json
                "Name": "",
                "CreationTime": "2018-12-20T14:51:23Z",
                "Status": "Available",
                "Description": "",
                "BusinessStatus": "Normal",
                "Spec": "Medium",
                "RegionId": "cn-huhehaote",
                "InstanceChargeType": "PostPaid",
                "ExpiredTime": "",
                "VpcId": "vpc-hp3ag7ydchedxxxxxxxxx",
                "Ipv6GatewayId": "ipv6gw-hp33of4uz4k4kxxxxxxxx"
```

`},` `{`

```json
                "CreationTime": "2018-12-05T09:21:35Z",
                "Name": "IPv6 gateway",
                "Status": "Available",
                "Description": "",
                "BusinessStatus": "Normal",
                "Spec": "Medium",
                "RegionId": "cn-huhehaote",
                "InstanceChargeType": "PostPaid",
                "ExpiredTime": "",
                "VpcId": "vpc-hp3kzilwd9yflxxxxxxxx",
                "Ipv6GatewayId": "ipv6gw-hp33p10bdbt77xxxxxxxx"
```

`]` `},`

```json
    "TotalCount": 2,
    "PageSize": 10,
    "RequestId": "E3A06196-3E7C-490D-8F39-CB4B5A0CE8AD"
```

#### ModifyIpv6GatewaySpec

Changes the specification of an IPv6 gateway. The forwarding capacity and bandwidth of an IPv6 gateway vary based on the specification. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Gateway Spec | The operation that you want to perform. Set the value to Modif yIpv6Gat ewaySpec. |
| Ipv6GatewayId | String | Yes | ipv6gw-123456**** | The ID of the IPv6 gateway. |
| RegionId | String | Yes | cn-neimeng-env133- d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |

|   | Virtual Private Cloud |   |   |   | Developer Guide·API reference |   |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Spec | String | Yes | Small | The new specification that you want to set for the IPv6 gateway. Valid values: Small (default): Free Edition Middle: Enterprise Edition Large: Enhanced Enterprise Edition |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB-49E8- A2DC-CC114C67AF75 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyIpv6GatewaySpec &Ipv6GatewayId=ipv6gw-123456**** &RegionId=cn-neimeng-env133-d01 &Spec=Small &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyIpv6GatewaySpecResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</ModifyIpv6GatewaySpecResponse>
```

`JSON` format `{`

```json
 "RequestId": "9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### DescribeIpv6EgressOnlyRules

Queries egress-only rules. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6EgressO nlyRules | The operation that you want to perform. Set the value to DescribeIpv6EgressOnlyRules. |
| Ipv6GatewayId | String | Yes | ipv6gw-123456**** | The ID of the IPv6 gateway. |
| RegionId | String | Yes | cn-neimeng-env133- d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6EgressOnlyRuleI d | String | No | ipv6gwpy- 123456**** | The ID of the egress-only rule that you want to query. |
| Name | String | No | rulename | The name of the egress-only rule. |
| InstanceType | String | No | Ipv6Address | The type of the instance to which the egress-only rule applies. Set the value to: Ipv6Address, which specifies that the egress-only rule applies to an IPv6 address. |
| InstanceId | String | No | i-123456**** | The ID of the Elastic Compute Service (ECS) instance that is associated with the IPv6 address to which the egress-only rule applies. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6EgressOnlyRul es | Array of Ipv6EgressOnlyRul e |   | The details about the egress-only rules. |
| Ipv6EgressOnlyRul e |   |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | ruledescription | The description of the egress-only rule. |
| InstanceId | String | i-123456**** | The ID of the instance to which the egress-only rule applies. |
| InstanceType | String | Ipv6Address | The type of the instance to which the egress-only rule applies. |
| Ipv6EgressOnlyRul eId | String | ipv6gwpy-123456**** | The ID of the egress-only rule. |
| Name | String | rulename | The name of the egress-only rule. |
| Status | String | Available | The status of the egress-only rule. |
| PageNumber | Integer | 1 | The number of the returned page. Default value: 1. |
| PageSize | Integer | 10 | The number of entries returned on each page. Maximum value: 50. Default value: 10. |
| RequestId | String | E16671B7-DEA6-48E0- 8E9C-41913DAD44DD | The ID of the request. |
| TotalCount | Integer | 1 | The number of entries returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeIpv6EgressOnlyRules &Ipv6GatewayId=ipv6gw-123456**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeIpv6EgressOnlyRulesResponse>
  <TotalCount>1</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>E16671B7-DEA6-48E0-8E9C-41913DAD44DD</RequestId>
  <PageNumber>1</PageNumber>
  <Ipv6EgressOnlyRules>
        <Status>Available</Status>
        <Ipv6EgressOnlyRuleId>ipv6gwpy-123456****</Ipv6EgressOnlyRuleId>
        <Description>ruledescription</Description>
        <InstanceId>i-123456****</InstanceId>
        <InstanceType>Ipv6Address</InstanceType>
        <Name>rulename</Name>
  </Ipv6EgressOnlyRules>
</DescribeIpv6EgressOnlyRulesResponse>
```

`JSON` format `{`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "E16671B7-DEA6-48E0-8E9C-41913DAD44DD",
    "PageNumber": 1,
    "Ipv6EgressOnlyRules": {
        "Status": "Available",
        "Ipv6EgressOnlyRuleId": "ipv6gwpy-123456****",
        "Description": "ruledescription",
        "InstanceId": "i-123456****",
        "InstanceType": "Ipv6Address",
        "Name": "rulename"
```

#### CreateIpv6EgressOnlyRule

Creates an egress-only rule for an IPv6 address. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateIpv6EgressOnl yRule | The operation that you want to perform. Set the value to Creat eIpv6EgressOnlyRule. |
| InstanceId | String | Yes | ipv6- hp3nxjkfxn5pnhgl5** ** | The ID of the IPv6 address to which you want to apply the egress-only rule. |
| Ipv6GatewayId | String | Yes | ipv6gw- hp3c2paq0ywauasz a**** | The ID of the IPv6 gateway. |
| RegionId | String | Yes | cn-neimeng-env133- d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceType | String | No | IPv6Address | The type of the instance to which you want to apply the egress-only rule. Set the value to: Ipv6Address (default): an IPv6 address. |
| Name | String | No | rulename | The name of the egress-only rule. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | ruledescription | The description of the egress-only rule. The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6EgressRuleId | String | ipv6py- hp3w98rmlbqp01245** ** | The ID of the egress-only rule. |
| RequestId | String | 9DFEDBEE-E5AB-49E8- A2DC-CC114C67AF75 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateIpv6EgressOnlyRule &InstanceId=ipv6-hp3nxjkfxn5pnhgl5**** &Ipv6GatewayId=ipv6gw-hp3c2paq0ywauasza**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateIpv6EgressOnlyRuleResponse>
      <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
      <Ipv6EgressRuleId>ipv6py-hp3w98rmlbqp01245****</Ipv6EgressRuleId>
</CreateIpv6EgressOnlyRuleResponse>
```

`JSON` format `{`

```json
    "Ipv6EgressRuleId": "ipv6py-hp3w98rmlbqp01245****",
    "RequestId": "9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### DeleteIpv6EgressOnlyRule

Deletes an egress-only rule. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteIpv6EgressOnl yRule | The operation that you want to perform. Set the value to Delet eIpv6EgressOnlyRule. |
| Ipv6EgressOnlyRuleI d | String | Yes | ipv6py- hp3w98rmlbqp0**** | The ID of the egress-only rule that you want to delete. |
| RegionId | String | Yes | cn-neimeng-env133- d01 | The ID of the IPv6 gateway. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB-49E8- A2DC-CC114C67AF75 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteIpv6EgressOnlyRule &Ipv6EgressOnlyRuleId=ipv6py-hp3w98rmlbqp0**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteIpv6EgressOnlyRuleResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</DeleteIpv6EgressOnlyRuleResponse>
```

`JSON` format `{`

```json
 "RequestId": "4E40EAF1-783D-4C05-948D-DA0426C398C1"
```

#### DeleteIpv6InternetBandwidth

Sets the Internet bandwidth value of an IPv6 address to zero. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteIpv6InternetB andwidth | The operation that you want to perform. Set the value to Delet eIpv6Int ernet Bandwidt h. |
| RegionId | String | Yes | cn-neimeng-env133- d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6AddressId | String | No | ipv6-123456**** | The ID of the IPv6 address whose Internet bandwidth value you want to set to zero. |
| Ipv6InternetBandwid thId | String | No | 2 | The Internet bandwidth value of the IPv6 address. Unit: Mbit/s. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E07E0FE6-5C21-405F- AF82-7613AA81EF92 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteIpv6InternetBandwidth &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteIpv6InternetBandwidthResponse>
   <RequestId>6972A26E-99B1-4367-9890-FBDEBB0F5E7D</RequestId>
</DeleteIpv6InternetBandwidthResponse>
```

`JSON` format `{`

```json
 "RequestId": "E07E0FE6-5C21-405F-AF82-7613AA81EF92"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### DescribeIpv6GatewayAttribute

Queries detailed information about a specified IPv6 gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Gatewa yAttribute | The operation that you want to perform. Set the value to DescribeIpv6Gat ewayAt t ribut e. |
| Ipv6GatewayId | String | Yes | ipv6gw-123456**** | The ID of the IPv6 gateway that you want to query. |
| RegionId | String | Yes | cn-neimeng-env133- d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| BusinessStatus | String | Normal | The status of the IPv6 gateway. Valid values: Normal: normal FinacialLocked: locked due to overdue payments Securit yLocked: locked due to security reasons |
| CreationTime | String | 2020-12-05T09:21:35Z | The time when the IPv6 gateway was created. |
| Description | String | test | The description of the IPv6 gateway. |
| ExpiredTime | String | 2020-12-06T09:21:35Z | The time when the IPv6 gateway expires. |
| InstanceChargeTy pe | String | PostPaid | The metering method of the IPv6 gateway. |
| Ipv6GatewayId | String | ipv6gw-123456**** | The ID of the IPv6 gateway. |
| Name | String | test | The name of the IPv6 gateway. |
| RegionId | String | cn-neimeng-env133- d01 | The region ID of the IPv6 gateway. |
| RequestId | String | E3A06196-3E7C-490D- 8F39-CB4B5A0CE8AD | The ID of the request. |
| Spec | String | Small | The specification of the IPv6 gateway. Small: Free Edition Medium: Enterprise Edition Large: Enhanced Enterprise Edition |
| Status | String | Available | The status of the IPv6 gateway. |
| VpcId | String | vpc-123456**** | The ID of the virtual private cloud (VPC) to which the IPv6 gateway belongs. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeIpv6GatewayAttribute &Ipv6GatewayId=ipv6gw-123456**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeIpv6GatewayAttributeResponse>
  <Status>Available</Status>
  <Description>test</Description>
  <RequestId>E3A06196-3E7C-490D-8F39-CB4B5A0CE8AD</RequestId>
  <InstanceChargeType>PostPaid</InstanceChargeType>
  <Ipv6GatewayId>ipv6gw-123456****</Ipv6GatewayId>
  <BusinessStatus>Normal</BusinessStatus>
  <Name>test</Name>
  <VpcId>vpc-123456****</VpcId>
  <ExpiredTime>2020-12-06T09:21:35Z</ExpiredTime>
  <CreationTime>2020-12-05T09:21:35Z</CreationTime>
  <RegionId>cn-neimeng-env133-d01</RegionId>
  <Spec>Small</Spec>
</DescribeIpv6GatewayAttributeResponse>
```

`JSON` format `{`

```json
    "Status": "Available",
    "Description": "test",
    "RequestId": "E3A06196-3E7C-490D-8F39-CB4B5A0CE8AD",
    "InstanceChargeType": "PostPaid",
    "Ipv6GatewayId": "ipv6gw-123456****",
    "BusinessStatus": "Normal",
    "Name": "test",
    "VpcId": "vpc-123456****",
    "ExpiredTime": "2020-12-06T09:21:35Z",
    "CreationTime": "2020-12-05T09:21:35Z",
    "RegionId": "cn-neimeng-env133-d01",
    "Spec": "Small"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### DescribeIpv6Addresses

Queries the IPv6 addresses in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Address es | The operation that you want to perform. Set the value to DescribeIpv6Addresses. |
| RegionId | String | Yes | cn-neimeng-env133- d01 | The region ID of the IPv6 address. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Ipv6AddressId | String | No | ipv6- n2yrzmwjz2uj3s7j5** ** | The ID of the IPv6 address. You can specify up to 20 IDs in each call. Separate multiple IDs with commas (,). |
| Ipv6Address | String | No | 2408:XXXX:180:170 1:94c7:bc38:3bfa:d 2c | The IPv6 address that you want to query. |
| Name | String | No | test | The name of the IPv6 address. |
| AssociatedInstanceI d | String | No | i-123456**** | The ID of the instance that is assigned the IPv6 address. |
| AssociatedInstanceT ype | String | No | EcsInstance | The type of the instance that is assigned the IPv6 address. Set the value to EcsInst ance: an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC). This is the default value. |
| NetworkType | String | No | Public | The type of connection supported by the IPv6 address. Valid values: Privat e: communication within the private network Public: communication over the Internet |
| VpcId | String | No | vpc- hp325kt6307**** | The ID of the VPC to which the IPv6 address belongs. |
| VSwitchId | String | No | vsw-123456**** | The ID of the vSwitch to which the IPv6 address belongs. |
| Ipv6InternetBandwid thId | String | No | 1 | The Internet bandwidth value of the IPv6 address. Unit: Mbit/s. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6Addresses | Array of Ipv6Address |   | The details about the IPv6 addresses. |
| Ipv6Address |   |   |   |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AllocationTime | String | 2020-12-20T14:56:09Z | The time when the IPv6 address was created. |
| AssociatedInstanc eId | String | i-hp325kt6307**** | The ID of the instance that is assigned the IPv6 address. |
| AssociatedInstanc eType | String | EcsInstance | The type of the instance that is assigned the IPv6 address. Only EcsInst ance is returned, which indicates an ECS instance in a VPC. |
| Ipv6Address | String | 2408:XXXX:180:1701:9 4c7:bc38:3bfa:d2c | The IPv6 address. |
| Ipv6AddressId | String | ipv6- n2yrzmwjz2uj3s7j5**** | The ID of the IPv6 address. |
| Ipv6AddressName | String | test | The name of the IPv6 address. |
| Ipv6GatewayId | String | ipv6gw- hp38x2x0fz7**** | The ID of the IPv6 gateway to which the IPv6 address belongs. |
| Ipv6InternetBand width | Struct |   | The information about the Internet bandwidth of the IPv6 address. |
| Bandwidth | Integer | 2 | The exclusive Internet bandwidth of the IPv6 address. Unit: Mbit/s. |
| BusinessStatus | String | Normal | The status of the exclusive Internet bandwidth of the IPv6 address. Valid values: Normal: normal FinacialLocked: locked due to overdue payments Securit yLocked: locked due to security reasons |
| InstanceChargeTy pe | String | PostPaid | The billing method of the IPv6 gateway. Only Post Paid is returned, which indicates the pay- as-you-go billing method. |
| InternetChargeTyp e | String | PayByTraffic | The metering method of the IPv6 gateway. Valid values: PayByT raf f ic: pay-by-data-transfer PayByBandwidt h: pay-by-bandwidth |
| Ipv6InternetBand widthId | String | ipv6bw- hp3b35oq1fj50kb**** | The ID of the Internet bandwidth. |

| Virtual Private Clou | d |   | Developer Guide·API reference |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkType | String | Public | The type of connection supported by the IPv6 address. Valid values: Privat e: communication within the private network Public: communication over the Internet |
| RealBandwidth | Integer | 2 | The actual maximum bandwidth of the IPv6 address. Unit: Mbit/s. |
| Status | String | Available | The status of the IPv6 address. Valid values: Pending: The IPv6 address is being configured. Available: The IPv6 address is available. |
| VSwitchId | String | vsw-123456**** | The ID of the vSwitch to which the IPv6 address belongs. |
| VpcId | String | vpc-hp325kt6307**** | The ID of the VPC to which the IPv6 address belongs. |
| PageNumber | Integer | 1 | The number of the returned page. Default value: 1. |
| PageSize | Integer | 10 | The number of entries returned on each page. Maximum value: 50. Default value: 10. |
| RequestId | String | AA4486A8-B6AE-469E- AB09-820EF8ECFA2B | The ID of the request. |
| TotalCount | Integer | 2 | The number of entries returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeIpv6Addresses &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeIpv6AddressesResponse>
  <TotalCount>2</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>AA4486A8-B6AE-469E-AB09-820EF8ECFA2B</RequestId>
  <PageNumber>1</PageNumber>
  <Ipv6Addresses>
        <AllocationTime>2020-12-20T14:56:09Z</AllocationTime>
        <Status>Available</Status>
        <AssociatedInstanceId>i-hp325kt6307****</AssociatedInstanceId>
        <VpcId>vpc-hp325kt6307****</VpcId>
        <NetworkType>Public</NetworkType>
        <VSwitchId>vsw-123456****</VSwitchId>
        <Ipv6AddressId>ipv6-n2yrzmwjz2uj3s7j5****</Ipv6AddressId>
        <Ipv6GatewayId>ipv6gw-hp38x2x0fz7****</Ipv6GatewayId>
        <RealBandwidth>2</RealBandwidth>
        <AssociatedInstanceType>EcsInstance</AssociatedInstanceType>
        <Ipv6Address>2408:XXXX:180:1701:94c7:bc38:3bfa:d2c</Ipv6Address>
        <Ipv6AddressName>test</Ipv6AddressName>
        <Ipv6InternetBandwidth>
              <InstanceChargeType>PostPaid</InstanceChargeType>
              <Bandwidth>2</Bandwidth>
              <Ipv6InternetBandwidthId>ipv6bw-hp3b35oq1fj50kb****</Ipv6InternetBandwidthId>
              <BusinessStatus>Normal</BusinessStatus>
              <InternetChargeType>PayByTraffic</InternetChargeType>
        </Ipv6InternetBandwidth>
  </Ipv6Addresses>
</DescribeIpv6AddressesResponse>
```

`JSON` format `{`

```json
    "TotalCount": 2,
    "PageSize": 10,
    "RequestId": "AA4486A8-B6AE-469E-AB09-820EF8ECFA2B",
    "PageNumber": 1,
    "Ipv6Addresses": {
        "AllocationTime": "2020-12-20T14:56:09Z",
        "Status": "Available",
        "AssociatedInstanceId": "i-hp325kt6307****",
        "VpcId": "vpc-hp325kt6307****",
        "NetworkType": "Public",
        "VSwitchId": "vsw-123456****",
        "Ipv6AddressId": "ipv6-n2yrzmwjz2uj3s7j5****",
        "Ipv6GatewayId": "ipv6gw-hp38x2x0fz7****",
        "RealBandwidth": 2,
        "AssociatedInstanceType": "EcsInstance",
        "Ipv6Address": "2408:XXXX:180:1701:94c7:bc38:3bfa:d2c",
        "Ipv6AddressName": "test",
        "Ipv6InternetBandwidth": {
            "InstanceChargeType": "PostPaid",
            "Bandwidth": 2,
            "Ipv6InternetBandwidthId": "ipv6bw-hp3b35oq1fj50kb****",
            "BusinessStatus": "Normal",
            "InternetChargeType": "PayByTraffic"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### ModifyIpv6InternetBandwidth

Modifies the Internet bandwidth value of an IPv6 address. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6InternetB andwidth | The operation that you want to perform. Set the value to Modif yIpv6Int ernet Bandwidt h. |
| Bandwidth | Long | Yes | 4 | The new Internet bandwidth value that you want to set for the IPv6 address. Unit: Mbit/s. Valid values: 1 to 5000. If Int ernet ChargeT ype is set to PayByBandwidt h, valid values are 1 to 5000. If Int ernet ChargeT ype is set to PayByT raf f ic, valid values vary based on the specification of the IPv6 gateway. Small (default) specifies the Free Edition and the valid values are 1 to 500. Medium specifies the Enterprise Edition and the valid values are 1 to 1000. Large specifies the Enterprise Enhanced Edition and the valid values are 1 to 2000. |
| RegionId | String | Yes | cn-neimeng-env133- d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6AddressId | String | No | ipv6-1233456**** | The ID of the IPv6 address whose Internet bandwidth value you want to modify. |
| Ipv6InternetBandwid thId | String | No | 20 | The Internet bandwidth value before it is modified. Unit: Mbit/s. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D560AF68-4CE8-4A5C- B3FE-469F558094D0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyIpv6InternetBandwidth &Bandwidth=4 &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyIpv6InternetBandwidthResponse>
      <RequestId>D560AF68-4CE8-4A5C-B3FE-469F558094D0</RequestId>
</ModifyIpv6InternetBandwidthResponse>
```

`JSON` format `{`

```json
    "RequestId": "D560AF68-4CE8-4A5C-B3FE-469F558094D0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### AllocateIpv6InternetBandwidth

Purchases Internet bandwidth resources for an IPv6 address. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateIpv6Internet Bandwidth | The operation that you want to perform. Set the value to Allocat eIpv6Int ernet Bandwidt h. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | Yes | 2 | The Internet bandwidth resources that you want to purchase for the IPv6 address. Unit: Mbit/s. Valid values: 1 to 5000. If Int ernet ChargeT ype is set to PayByBandwidt h, valid values are 1 to 5000. If Int ernet ChargeT ype is set to PayByT raf f ic, valid values vary based on the specification of the IPv6 gateway. Small (default) specifies the Free Edition and the valid values are 1 to 500. Medium specifies the Enterprise Edition and the valid values are 1 to 1000. Large specifies the Enterprise Enhanced Edition and the valid values are 1 to 2000. |
| Ipv6AddressId | String | Yes | ipv6-123456**** | The ID of the IPv6 address for which the Internet bandwidth resources are purchased. |
| Ipv6GatewayId | String | Yes | ipv6gw-123456**** | The ID of the IPv6 gateway. |
| RegionId | String | Yes | cn-neimeng-env133- d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| InternetChargeType | String | No | PayByTraffic | The metering method of the Internet bandwidth resources of the IPv6 gateway. Valid values: PayByT raf f ic: pay-by-data-transfer PayByBandwidt h (default): pay-by- bandwidth |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| InternetBandwidth Id | String | 2 | The Internet bandwidth resources that you purchased. Unit: Mbit/s. |

|   | Developer Guide·AP | I reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6AddressId | String | ipv6-123456**** | The ID of the IPv6 address for which the Internet bandwidth resources were purchased. |
| RequestId | String | 6972A26E-99B1-4367- 9890-FBDEBB0F5E7D | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AllocateIpv6InternetBandwidth &Bandwidth=2 &Ipv6AddressId=ipv6-123456**** &Ipv6GatewayId=ipv6gw-123456**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AllocateIpv6InternetBandwidthResponse>
  <RequestId>6972A26E-99B1-4367-9890-FBDEBB0F5E7D</RequestId>
  <InternetBandwidthId>2</InternetBandwidthId>
  <Ipv6AddressId>ipv6-123456****</Ipv6AddressId>
</AllocateIpv6InternetBandwidthResponse>
```

`JSON` format `{`

```json
    "RequestId": "6972A26E-99B1-4367-9890-FBDEBB0F5E7D",
    "InternetBandwidthId": 2,
    "Ipv6AddressId": "ipv6-123456****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### ModifyIpv6AddressAttribute

Modifies the name and description of an IPv6 address. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6AddressA ttribute | The operation that you want to perform. Set the value to Modif yIpv6AddressAt t ribut e. |

| Virtual Private Cloud |   |   |   | Developer Guide·API reference |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Ipv6AddressId | String | Yes | ipv6- hp32vv2klzw4yerdf* *** | The ID of the IPv6 address that you want to modify. |
| RegionId | String | Yes | cn-neimeng-env133- d01 | The region ID of the IPv6 address. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | test | The new name of the IPv6 address. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter, but cannot start with http:// or https:// . |
| Description | String | No | test | The new description of the IPv6 address. The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D560AF68-4CE8-4A5C- B3FE-469F558094D0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyIpv6AddressAttribute &Ipv6AddressId=ipv6-hp32vv2klzw4yerdf**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyIpv6AddressAttributeResponse>
   <RequestId>D560AF68-4CE8-4A5C-B3FE-469F558094D0</RequestId>
</ModifyIpv6AddressAttributeResponse>
```

`JSON` format `{`

```json
 "RequestId": "D560AF68-4CE8-4A5C-B3FE-469F558094D0"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### ModifyIpv6GatewayAttribute

Modifies the name and description of an IPv6 gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Gateway Attribute | The operation that you want to perform. Set the value to Modif yIpv6Gat ewayAt t ribut e. |
| Ipv6GatewayId | String | Yes | ipv6gw- hp39kh1ya51yzp2lu* *** | The ID of the IPv6 gateway that you want to modify. |
| RegionId | String | Yes | cn-neimeng-env133- d01 | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | ipv6name | The new name of the IPv6 gateway. |
| Description | String | No | ipv6description | The new description of the IPv6 gateway. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB-49E8- A2DC-CC114C67AF75 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyIpv6GatewayAttribute &Ipv6GatewayId=ipv6gw-hp39kh1ya51yzp2lu**** &RegionId=cn-neimeng-env133-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyIpv6GatewayAttributeResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</ModifyIpv6GatewayAttributeResponse>
```

`JSON` format `{`

```json
 "RequestId": "9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

## Appendixes

### Use the ASAPI gateway to call API

operations You can use the Apsara Stack API (ASAPI) gateway to call API operations of most Apsara Stack services. This topic describes how to call API operations by using the ASAPI gateway and provides links to references. Procedure
1. Obtain the ASAPI SDK.
Before you use ASAPI to call an API operation, you must obtain the ASAPI SDK. For more information, see Obtain the ASAPI SDK.
2. Obtain the endpoint of ASAPI. For more information, see Obtain the endpoint of ASAPI.
3. Obtain an AccessKey pair.
Obtain the AccessKey pair that is required for calling an API operation. Not e We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services.
4. Obtain the region ID.
Obtain the region ID that is required for calling an API operation.
5. Obtain the organization ID and resource set ID.
You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrgani zationList in Apsara Uni-manager Management Console Developer Guide. You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourc eGroup in Apsara Uni-manager Management Console Developer Guide. Not e When you call an API operation, you can specify the organization ID and resource set ID by using the <x-acsorganizationid> and <x-acs-resourcegroupid> parameters. This allows you to query specified resources. If you do not set the <x-acs-organizationid> parameter, the organization to which the current user belongs is used by default. If you do not set the <x-acs-resourcegroupid> parameter, it is empty by default. If you specify a resource set ID, you must also specify an organization ID.
6. Refer to the API reference.
Obtain the developer guide of the Apsara Stack service that you want to use. You can learn the features of API operations and how to call the API operations. For more information, see Use developer guides.
7. Use ASAPI SDK to call API operations.
After you complete the preceding steps, you can use the ASAPI SDK to call API operations. For more information about how to use SDKs for different languages, see the relevant topics. The following example shows how to call the DescribeInstances operation of Elastic Compute Service (ECS) by using SDK for Java:

```java
public static void main(String[] args) {
    ASClient client = new ASClient();
    // Specify the caller. The caller is recorded in logs.
    client.setSdkSource("autoTest");
    // Set request parameters.
    Map<String, Object> parameters = new HashMap<String, Object>();;
    parameters.put("Product", "Ecs");// Specify the POP code, which is the same as the POP code in t
he corresponding API directory.
    parameters.put("Action", "DescribeInstances"); // Specify the name of the API operation. Use the
same letter case as the corresponding API directory.
    parameters.put("Version", "2014-05-26"); // Specify the API version.
    // Specify the region ID that you obtained.
    parameters.put("RegionId", "xxx");
    // Specify your AccessKey ID and AccessKey secret.
    parameters.put("AccessKeyId", "xxx");
    parameters.put("AccessKeySecret", "xxx");
    // Add the parameters based on the API reference. Take note that the parameters are case-sensiti
ve.
    parameters.put("PageNumber",1);
    parameters.put("PageSize",10);
    Map<String,String> headers=new HashMap<>();
    // Specify the organization ID in the Apsara Uni-manager Management Console.
    headers.put("x-acs-organizationid","3");
    // Specify the resource set ID in the Apsara Uni-manager Management Console.
    //headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>");
    // Specify the endpoint of ASAPI.
    String endpoint="https://public.asapi.xxx.xxx/asapi/v3";
    // Initiate the request.
    String result = client.doPost(endpoint,headers, parameters);
    // Display the results.
    System.out.println(JSONObject.toJSONString(JSONObject.parseObject(result), SerializerFeature.Pre
ttyFormat));
```

### Use the ASAPI gateway to make API

calls

#### Obtain an endpoint of ASAPI

This topic describes three methods that you can use to obtain an endpoint of Apsara Stack API (ASAPI) and how to verify the endpoint. Methods Method 1: Use Registration Vars of Services to obtain an endpoint
1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click Product s. iii. Choose Plat f orms > Apsara Inf rast ruct ure Management Framework.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for `Registration Vars of Services` and click the report name.
4. On the Regist rat ion Vars of Services page, click the
icon next to Service and search for `asapi` .
5. Find the asapi service, right-click in the Service Regist rat ion column, and then select Show More from the
shortcut menu. In the Det ails dialog box, obtain the value of asapi.public.endpoint .
6. Generate an endpoint of ASAPI based on the following format:

```
https://<asapi.public.endpoint>/asapi/v3
```

Method 2: Use cluster resources to generate an endpoint
1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click Product s. iii. Choose Plat f orms > Apsara Inf rast ruct ure Management Framework.
2. Go to the Clusters page.
i. In the left-side navigation pane, choose Operat ions > Clust er Operat ions. ii. In the Clust er search box, enter `ascm` . iii. Click Operat ions in the Act ions column.
3. Obtain the value of the domain parameter.
i. Click the Clust er Resources tab. ii. In the Name field, search for `asapi_dns_public` . iii. Click Det ails in the Applicat ion Paramet er column. In the Applicat ion Paramet er message, obtain the value of the domain parameter.
4. Generate an endpoint of ASAPI based on the following format:

```
https://<domain>/asapi/v3
```

Method 3: Concatenate strings to generate an endpoint You can also concatenate strings to generate an endpoint based on the following format:

```
https://public.asapi.<region>.<internet-domain>/asapi/v3
```

Not e
1. Replace <region> with the actual region ID.
2. Replace <internet-domain> with the root domain of your Apsara Stack service. To obtain the root domain,
contact Apsara Stack O&M personnel. Take note of this point: Use the internet-domain parameter instead of the intranet-domain parameter. If the region value is `cn-****-****-d01` and the int ernet -domain value is `inter.****.****.com` , the following endpoint is used:

```
https://public.asapi.cn-****-****-d01.inter.****.****.com/asapi/v3
```

Verify the endpoint Enter the following code. If you cannot access the endpoint, the endpoint is unavailable. You can use the historical endpoint.

```bash
 curl https://public.asapi.${global:region}.${global:internet-domain}/api/version -k
```

Not e ${global:region} and ${global:internet-domain} are variables. You must replace them with the actual values that you obtained. Available endpoint example: Unavailable endpoint example: Historical endpoint Only the HTTP protocol is supported. The historical endpoint is suffixed with `intranet-domain` and in the following format:

```
 http://server.asapi.${global:region}.${global:intranet-domain}/asapi/v3
```

Not e ${global:region} and ${global:intranet-domain} are variables. You must replace them with the actual values that you obtained. Procedure To obtain the actual values of the variables ${global:region}, ${global:internet-domain}, and ${global:intranetdomain}, perform the following operations:
1. In the address bar, enter the region-id.aso.intranet-domain-id.com URL and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password used to log on to the Apsara Uni-manager Operations Console from the deployment personnel or an administrator. When you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password is 10 to 20 characters in length.
3. Click Log On to log on to the Apsara Uni-manager Operat ions Console.
4. In the top navigation bar, choose Product s > Plat f orms > Apsara Inf rast ruct ure Management Framework
to go to Apsara Infrastructure Management.
5. In the left-side navigation pane, choose Operat ions > Clust er Operat ions.
6. On the Clust ers page, enter ascm-A in the Cluster search box to find the cluster. Click the cluster name.
7. On the Clust er Dashboard page, click Operat ions Menu > Conf igurat ion Files.
8. In the File List window on the left side of the Clust er Conf igurat ion page, click kv.conf , click the file content
in the right window, and then press Ctrl + F. Search for region, internet-domain, and intranet-domain. Replace ${global:region} with the obtained region value, ${global:internet-domain} with the obtained internet-domain value, and ${global:intranet-domain} with the obtained intranet-domain value. Not e ${global:} is not included in the endpoint of ASAPI that you can use.

#### Obtain Apsara Stack SDKs

Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. Public environment If you are using the public environment, you can go to the Apsara Stack documentation page and download the Apsara Stack SDKs in the Ot her Resources section at the lower part of the page. Private environment If you are using the private environment, you must switch to the public environment and then go to the Apsara Stack documentation page. At the lower part of the page, download the Apsara Stack SDKs in the Ot her Resources section. Apsara Stack SDK for Java

| greopId | artifactId | Version |
|---|---|---|
| com.alibaba | alicrypto-java-aliyun | 1.0.4 |
| com.alibaba | fastjson | 1.2.68 |
| org.bouncycastle | bcprov-jdk15to18 | 1.66 |
| org.bouncycastle | bcpkix-jdk15on | 1.65 |
| org.bouncycastle | bcprov-jdk15on | 1.65 |
| com.aliyun | gmsse | 1.1.0 |
| org.apache.commons | commons-lang3 | 3.0 |
| commons-codec | commons-codec | 1.11 |
| commons-logging | commons-logging | 1.2 |
| org.apache.httpcomponents | httpcore | 4.4.11 |
| org.apache.httpcomponents | httpclient | 4.5.7 |

Apsara Stack SDK for Python

| Package | Version |
|---|---|
| aliyun-python-sdk-core | 2.13.35 |
| certifi | 2021.5.30 |
| cffi | 1.14.6 |
| charset-normalizer | 2.0.4 |
| cryptography | 3.4.8 |

| Package | Version |
|---|---|
| idna | 3.2 |
| jmespath | 0.10.0 |
| pycparser | 2.20 |
| requests | 2.26.0 |
| urllib3 | 1.26.6 |

Not e You can use the version for each package listed in the preceding table or a later version.

### STS overview

#### What is STS?

Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and RAM roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed to access Apsara Stack resources by using an issued STS token. When the STS token is issued, you can specify a validity period and access permissions for the STS token. Use a RAM user to obtain an STS token An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and can use the STS token to access Apsara Stack resources. Benefits STS tokens help reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify the validity period for STS tokens. After STS tokens expire, they become invalid. Therefore, you do not need to rotate the STS tokens on a regular basis. You can attach custom policies to STS tokens for flexible and fine-grained authorization.

#### AssumeRole

Obtains a Security Token Service (STS) token that is used by a RAM user to assume a RAM role. In this example, an Apsara Stack tenant account is used as the trusted entity of the RAM role. Request parameters

| Paramet er | T ype | Requir ed | Example | Descript ion |
|---|---|---|---|---|
| Act ion | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::123456789 012****:role/adminro le | The Apsara Stack Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Apsara Stack tenant account. |

| Paramet er | T ype | Requir ed | Example | Descript ion |
|---|---|---|---|---|
| RoleSessionName | String | Yes | alice | The name of the role session. Set this parameter based on your business requirements. In most cases, you can set this parameter to the identity of the user who calls the operation. For example, specify a username. In ActionTrail logs, you can distinguish the users who assume the same RAM role to perform operations based on the value of the RoleSessionName parameter. This way, you can perform user-specific auditing. The name must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"} | The policy that specifies the permissions of the STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. The policy must be 1 to 1,024 characters in length. |

Responses

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| Request Id | String | 6894B13B-6D71-4EF5- 88FA-F32781734A7F | The ID of the request. |
| Credent ials | None | None | The access credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuKg5U1 **** | The AccessKey ID. |
| AccessKeySecret | String | ***************************************** | The AccessKey secret. |
| Securit yT oken | String | ******** | The security token. |
| Expirat ion | String | 2015-04-09T11:52:19Z | The time when the STS token expires. |
| AssumedRoleUser | None | None | The temporary identity that you use to assume the RAM role. |

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| Arn | String | acs:ram::123456789012 ****:role/adminrole/alic e | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495****:ali ce | The ID of the temporary identity that you use to assume the RAM role. |

Examples Add Project Object Model (POM) dependencies The Alibaba Cloud core library is required. Perform the following steps to add the Alibaba Cloud core library to POM:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

Call an API operation to obtain the STS AccessKey 3-tuple. In the following sample code, the `Sts::AssumeRole::2015-04-01` operation is used to obtain the 3-tuple.

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<your
AccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        // Replace "sts.aliyuns.com" with the actual endpoint of STS. In most cases, the endpoint is in
the following format: sts-vpc.${global:region}.${global:internet-domain}.
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        // Replace "<yourRoleSessionName>" with the alias that you specify for the current role session.
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
        // Replace "<yourRoleArn>" with the actual ARN that you obtained for the RAM role in the precedi
ng step.
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
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: " + stsToken);
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

Call examples In the following sample code, the `DescribeZones` operation in Elastic Compute Service (ECS) is used.

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
        // Replace "<yourRegionID>" with the actual region ID.
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the AccessKey ID and secret
in the 3-tuple that you obtained in the preceding step.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccessKey>", "<you
rStsAccessKeySecret>");
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
        // Replace "<yourStsToken>" with the STS token in the 3-tuple that you obtained in the preceding
step.
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

Error codes

| Ht t pCode | Error code | Error message | Descript ion |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleArn | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleSessio nName | The parameter RoleSessionName is wrongly formed. | The error message returned because the value of the RoleSessionName parameter is in an invalid format. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| 400 | InvalidParameter.DurationSe conds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the Durat ionSeconds parameter is invalid. The minimum value is 900, and the maximum value is equal to the value of the MaxSessionDurat ion parameter. |
| 400 | InvalidParameter.PolicyGram mar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the policy is invalid. |
| 400 | InvalidParameter.PolicySize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |

| Ht t pCode | Error code | Error message | Descript ion |
|---|---|---|---|
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error occurred. |
