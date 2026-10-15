---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Resource Orchestration Service Developer Guide"
product_version: "V3.16.2"
doc_version: "20220915"
pdf_pages: 189
source_pdf: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Resource Orchestration Service Developer Guide 20220915.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.16.2_intl_en/%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97%2B%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20Resource%20Orchestration%20Service%20Developer%20Guide%2020220915.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 Resource Orchestration Service Developer Guide

## Getting started

### Usage notes on development

documentation This topic describes how to view the desired product development documentation when you use Apsara Stack API (ASAPI). Prerequisites The Apsara Stack version is obtained from an O&M personnel or operations administrator. Procedure You can go to the Apsara Stack documentation center and view the desired product documentation.
1. Go to the Apsara Stack Documentation Center page by using a browser.
2. Click the Ent erprise, Agilit y, or All-in-one tab based on the Apsara Stack version that you use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the name of the product that you want to view.
5. In the upper-right corner of the product documentation section, click View Det ails or Download
PDF.

### Call an API operation

Apsara Stack allows you to call API operations by using the point of presence (POP) gateway or the Apsara Stack API (ASAPI) gateway. To ensure that Apsara Stack provides the same experience as the public cloud, API operations in Apsara Stack are called by using the POP gateway by default starting Apsara Stack Enterprise V3.16.0. This topic describes how to call API operations in Apsara Stack by using the POP gateway. Not e You can still call API operations by using the ASAPI gateway if you are using an earlier version of Apsara Stack Enterprise. For more information, see Call API operations by using the ASAPI gateway, Generate an endpoint for ASAPI, and Obtain Apsara Stack SDKs. Flowchart Procedure
1. Obtain AccessKey credentials.
Obtain the AccessKey credentials that are required when you call an API operation. For more information, see Obtain an AccessKey pair or Obtain an STS AccessKey 3-tuple. Not e We recommend that you use the AccessKey pair of a personal account or a Security Token Service (STS) AccessKey 3-tuple to call the API operations of the Apsara Uni-manager Management Console and cloud services.
2. Obtain a region ID.
Obtain a region ID that is required when you call an API operation. For more information, see Obtain the values of common header parameters.
3. Obtain an organization ID and a resource set ID.
You must call an API operation to obtain an organization ID. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management C onsole Developer Guide. You must call an API operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Con sole Developer Guide. Not e When you call an API operation, set the `<x-acs-organizationid>` parameter to the organization ID that you obtained and the `<x-acs-resourcegroupid>` parameter to the resource set ID that you obtained. This way, you can query resources in the specified organization and resource set. If you do not set the `<x-acs-organizationid>` parameter, the organization to which the current user belongs is used by default. If you do not set the `<x-acs-resourcegroupid>` parameter, this parameter is empty by default. If you specify a resource set ID, you must also specify an organization ID.
4. Obtain the API references.
Obtain the developer guide of the cloud service that you want to use. You can learn the features of API operations and how to call the API operations. For more information, see Use developer guides.
5. Obtain the endpoint of the cloud service.
6. Obtain an SDK of the cloud service and call an API operation.

## Preparations

### Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

### View the information about API

operations You must obtain a service name, API operation name, and API version. All the information is required when you use SDKs. Procedure
1. Log on to the API Tool console.
2. In the left-side navigation pane, click API f old.
3. On the API Direct ory page, select the target service from the drop-down list, enter the API
operation name in the search box, and then click the search icon.
4. View and remember the service name, API operation name, and API version.

### Obtain an AccessKey pair

An AccessKey credential can be assigned by Resource Access Management (RAM) or STS. You can use one of the services to obtain an AccessKey credential for authentication when you call API operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM. Context The AccessKey ID and AccessKey secret contained in an AccessKey credential are used to implement symmetric encryption and verify the identity of request senders. The AccessKey ID is used to identify a user. The AccessKey secret is a string that is used to encrypt the signature. An AccessKey credential can be assigned by RAM or STS: An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An AccessKey 3-tuple that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an STS AccessKey 3-tuple. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, set the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur. Warning The AccessKey pair of a personal account is managed and controlled by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |

| Parameter | Description |
|---|---|
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni- manager Management Console Developer Guide. |

Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. Click the profile picture in the upper-right corner of the page and click User Inf ormat ion.
3. In the AccessKey Pair section, view the AccessKey pair of your account.
Not e An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Organizat ions.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you want
to obtain.
5. Click Management AccessKey on the right side of the page.
6. In the Management AccessKey dialog box, view the AccessKey pair of the organization.

### Obtain an STS AccessKey 3-tuple

This topic describes how to use STS to call API operations in Apsara Stack. Background information STS allows you to manage temporary credentials to your Apsara Stack resources. You can use STS to call API operations in Apsara Stack. An STS AccessKey 3-tuple consists of an AccessKey ID, an AccessKey secret, and a security token. All the three elements are required when you use STS to call API operations in Apsara Stack. For more information, see What is STS? Procedure
1. Obtain the Alibaba Cloud Resource Name (ARN) of the RAM role that is assumed by the
organization that you want to use. i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click User Inf ormat ion. iii. Click View Current Role Policy. iv. In the View Policies of Current Role dialog box, select an organization and view the RAM Role.
2. Obtain an STS AccessKey 3-tuple
Not e In the following code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code. The following section describes the variable parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <yourRoleSessionName>: Replace the parameter with the name of the current session. <yourRoleArn>: Replace the parameter with the obtained ARN of the RAM role. <sts.aliyuns.com>: Replace the parameter with the STS endpoint.

```
public static void main(String[] args) {
    // Create and initialize a DefaultAcsClient instance.
    // Specify the region ID, AccessKey ID, and AccessKey secret.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKe
yID>", "<yourAccessKeySecret>");
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
```

`}`

```java
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace <sts.aliyuns.com> with the STS endpoint in the sts-vpc.${global:region}.
${global:internet-domain} format.
    request.setSysDomain("<sts.aliyuncs.com>");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace <yourRoleSessionName> with the name of the current session.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // Replace <yourRoleArn> with the ARN of the RAM role that is obtained in the previ
ous step.
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
3. Use the AccessKey 3-tuple assigned by STS to call an operation of a service. The following sample
code provides an example on how to use the AccessKey 3-tuple assigned by STS to call the DescribeRegions operation of Resource Orchestration Service (ROS): Not e In the following code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code. The following section describes the variable parameters: <yourRegionID>: Replace the parameter with the region ID. <yourStsAccesskeyID>: Replace the parameter with your STS AccessKey ID. <yourStsAccessKeySecret>: Replace the parameter with your STS AccessKey secret. <yourStsToken>: Replace the parameter with your security token. <yourResourceGroupID>: Replace the parameter with the resource set ID. <yourOrganizationID>: Replace the parameter with the organization ID.

```java
public static void main(String[] args) {
    // Replace <yourRegionID> with the region ID.
    // Replace <yourStsAccessKeyID> and <yourStsAccessKeySecret> with the AccessKey ID
and AccessKey secret obtained in the previous step.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAcces
skey>", "<yourStsAccessSecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    CommonRequest request = new CommonRequest();
    request.setSysDomain("ros.aliyuncs.com");
    request.setSysProduct("ROS");
    request.setSysAction("DescribeRegions");
    request.setSysVersion("2019-09-10");
    request.setSysMethod(MethodType.GET);
    request.setHttpContentType(FormatType.FORM);
    // Replace <yourRegionID> with the region ID.
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
    // Replace <yourStsToken> with the security token obtained in the previous step.
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
    // Optional. Replace the parameter with the resource set ID.
    //request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
    // Required. Replace the parameter with the organization ID.
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

### Obtain the values of common

header parameters You must set header parameters when you call API operations in Apsara Stack. This topic describes the header parameters and how to obtain the values of the parameters. This topic also describes the return values of some parameters after you call API operations. Header parameters

| Paramet er | Descript ion |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain region IDs, see Obtain a region ID. |
| x-acs-organizat ionid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see Obtain a resource set ID. |

Obtain a region ID
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Regions.
4. Click the name of the organization that you want to use.
5. In the Regions section, view the region ID.
Obtain an organization ID You must call an API operation to obtain an organization ID. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. Obtain a resource set ID You must call an API operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide. Response parameters The following table describes the response parameters that are returned by default when you call operations to query the instances of cloud services.

| Paramet er | Descript ion |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |

| esource Orchestration Service | Developer Guide·Preparation |
|---|---|

| Paramet er | Descript ion |
|---|---|
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

### Obtain the endpoint of ROS

This topic describes how to obtain the endpoint of ROS. Background information To use the POP gateway to call API operations in Apsara Stack, you must specify the endpoint of the corresponding cloud service. You can contact an Alibaba Cloud on-site O&M engineer to obtain the endpoint. You can also perform the following steps to obtain the endpoint. Procedure
1. Log on to Apsara Infrastructure Management.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose Product s > Base/Cloud Plat f orm > Apsara Inf rast ruct ure Management Framework. Not e The following steps describe how to obtain the endpoint in the new version of Apsara Infrastructure Management Framework.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for Regist rat ion Vars of Services and click the report name.
4. On the Regist rat ion Vars of Services page, move the pointer over Service, click the
icon, and then search for ROS.
5. Find `ros-service` . Right-click the value in the Service Regist rat ion column and select Show
More.
6. In the Det ails dialog box, view the value of ros-openapi.endpoint. The value indicates the
endpoint of ROS.

### Obtain an ROS SDK

To call API operations of ROS in Apsara Stack by using the POP gateway, you must use an ROS SDK. The following table provides links for you to download Alibaba Cloud SDKs and ROS SDKs.

| Alibaba Cloud SDK | ROS SDK |
|---|---|
| Alibaba Cloud SDK for Java | ROS SDK for Java |
| Alibaba Cloud SDK for Python | ROS SDK for Python |
| Alibaba Cloud SDK for Go | ROS SDK for Go |

va

## Use ROS SDK for Java

### Get started with ROS SDK for Java

This topic describes how to get started with ROS SDK for Java. Prerequisites An Apsara Stack tenant account and an AccessKey pair, which consists of an AccessKey ID and an AccessKey secret, are obtained. For more information, see Obtain an AccessKey pair. The endpoint of ROS is obtained. For more information, see Obtain the endpoint of ROS. Java Development Kit (JDK)1.8or later is installed. Install the SDK If you use Apache Maven to manage a Java project, you need to only import the JAR file to the pom.xml file of the project. To use ROS SDK for Java, you must install the core library of Alibaba Cloud SDK for Java and ROS SDK for Java. We recommend that you use the SDK core library of V4.5.17 or later and ROS SDK for Java of V1.0.1 or later. Use ROS SDK for Java
1. Create and initialize a com.aliyun.ros20190910.Client instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exception.
Not e In the following code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code. The following section describes the variable parameters: <yourRegionId>: Replace the parameter with the region ID. <yourAccessKeyId>: Replace the parameter with your AccessKey ID. <yourAccessKeySecrect>: Replace the parameter with your AccessKey secret. <Endpoint>: Replace the parameter with the endpoint of ROS.

```java
package com.aliyun.sample; import com.aliyun.ros20190910.Client; import com.aliyun.tea.*; import com.aliyun.ros20190910.*; import com.aliyun.ros20190910.models.*; import com.aliyun.teaopenapi.*; import com.aliyun.teaopenapi.models.*; public class Sample {
```

va

```
    /**
     * Use your AccessKey ID and AccessKey secret to initialize the client instance.
```

`*`

```
     * @param accessKeyId
     * @param accessKeySecret
     * @return Client
     * @throws Exception
```

`*/`

```java
    private static String ACCESSKEYID = "<yourAccessKeyId>";
    private static String SECRET = "<yourAccessKeySecrect>";
    private static String REGIONID = "<yourRegionId>";
    public static com.aliyun.ros20190910.Client createClient() throws Exception {
        Config config = new Config()
                // Your AccessKey ID.
                .setAccessKeyId(ACCESSKEYID)
                // Your AccessKey secret.
                .setAccessKeySecret(SECRET);
        // The endpoint of ROS.
        config.endpoint = "<Endpoint>";
        return new com.aliyun.ros20190910.Client(config);
```

`}`

```
    public static void describeRegions(Client client) throws Exception {
        DescribeRegionsRequest describeRegionsRequest = new DescribeRegionsRequest();
        // Run the following code to obtain the response of the API request.
        DescribeRegionsResponse resp = client.describeRegions(describeRegionsRequest);
```

`}`

```
    public static void getStack(Client client, String stackId, String regionId) throws
Exception {
        GetStackRequest getStackRequest = new GetStackRequest()
                .setStackId(stackId)
                .setRegionId(regionId);
        // Run the following code to obtain the response of the API request.
        GetStackResponse resp = client.getStack(getStackRequest);
        com.aliyun.teaconsole.Client.log(com.aliyun.teautil.Common.toJSONString(TeaMode
l.buildMap(resp)));
```

`}`

```
    public static void deleteStack(Client client, String stackId, String regionId) thro
ws Exception {
        DeleteStackRequest deleteStackRequest = new DeleteStackRequest()
                .setStackId(stackId)
                .setRegionId(regionId);
        // Run the following code to obtain the response of the API request.
        DeleteStackResponse resp = client.deleteStack(deleteStackRequest);
        com.aliyun.teaconsole.Client.log(com.aliyun.teautil.Common.toJSONString(TeaMode
l.buildMap(resp)));
```

`}`

```
    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
```

va

```
        com.aliyun.ros20190910.Client client = Sample.createClient();
        CreateStackRequest.CreateStackRequestParameters parameters0 = new CreateStackRe
quest.CreateStackRequestParameters()
                .setParameterKey("VpcName")
                .setParameterValue("TestVpc");
        CreateStackRequest.CreateStackRequestParameters parameters1 = new CreateStackRe
quest.CreateStackRequestParameters()
                .setParameterKey("CidrBlock")
                .setParameterValue("192.168.0.0/16");
        CreateStackRequest createStackRequest = new CreateStackRequest()
                .setTemplateBody("{\n" +
                        "  \"ROSTemplateFormatVersion\": \"2015-09-01\",\n" +
                        "  \"Parameters\": {\n" +
                        "    \"VpcName\": {\n" +
                        "      \"Type\": \"String\",\n" +
                        "      \"Description\": \"Vpc Name\",\n" +
                        "      \"Label\": \"Vpc Name\"\n" +
                        "    },\n" +
                        "    \"CidrBlock\": {\n" +
                        "      \"Type\": \"String\",\n" +
                        "      \"Description\": \"Vpc CidrBlock\",\n" +
                        "      \"Label\": \"Vpc CidrBlock\"\n" +
                        "    }\n" +
                        "  },\n" +
                        "  \"Resources\": {\n" +
                        "    \"Vpc\": {\n" +
                        "      \"Type\": \"ALIYUN::ECS::VPC\",\n" +
                        "      \"Properties\": {\n" +
                        "        \"CidrBlock\": {\n" +
                        "          \"Ref\": \"CidrBlock\"\n" +
                        "        },\n" +
                        "        \"VpcName\": {\n" +
                        "          \"Ref\": \"VpcName\"\n" +
                        "        }\n" +
                        "      }\n" +
                        "    }\n" +
                        "  }\n" +
                        "}")
                .setStackName("stackName")
                .setRegionId("cn-hangzhou")
                .setTimeoutInMinutes(40L)
                .setParameters(java.util.Arrays.asList(
                        parameters0,
                        parameters1
                ));
        // Run the following code to obtain the response of the API request.
        client.createStack(createStackRequest);
        Sample.describeRegions(client);
        Sample.getStack(client, "yourStackId", REGIONID);
        Sample.deleteStack(client, "yourStackId", REGIONID);
```

`}` `}` va

### Use SDK

#### Install ROS SDK for Java

This topic describes the two steps that are required to install ROS SDK for Java: obtain ROS SDK for Java and add Maven dependencies. Step 1: Obtain ROS SDK for Java A JDK of 1.8 or later is required for Alibaba Cloud SDK for Java. To use ROS SDK for Java, you must install the core library of Alibaba Cloud SDK for Java and ROS SDK for Java. The version of the SDK core library must be V4.5.17 or later. The version of ROS SDK for Java must be V1.0.1 or later. For more information, see ROS SDK for Java. Step 2: Add Maven dependencies When you install ROS SDK for Java, you must add the following dependencies to the pom.xml file:

```xml
<dependencies>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>tea-openapi</artifactId>
        <version>0.0.19</version>
    </dependency>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>ros20190910</artifactId>
        <version>1.0.1</version>
    </dependency>
</dependencies>
```

#### Configure authentication credentials

When you use Alibaba Cloud SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. ROS SDK for Java allows you to complete the authentication process by using an AccessKey pair. For more information, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access ROS, you must configure the AccessKey pair as the credentials when you initialize a client instance. Warning Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack account may be compromised. va

```java
private static String ACCESSKEYID = "<yourAccessKeyId>"; // Specify your AccessKey ID. private static String SECRET = "<yourAccessKeySecrect>"; // Specify your AccessKey secre
```

`t.`

```java
private static String REGIONID = "<yourRegionId>"; // Specify the region ID.
```

Not e In the preceding code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code.

#### Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements. Not e You must use actual values to replace the variables in the following sample code. Do not retain the angle brackets (<>) in the final code. The following list describes the variables: <readTimeout>: Specify the read timeout period based on your business requirements. Unit: milliseconds. <connectionTimeout>: Specify the connection timeout period based on your business requirements. Unit: milliseconds. <maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER. <maxRequests>: Specify the maximum number of requests based on your business requirements. The supported data type is INTEGER. <http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy. va

```
// Obtain the HttpClientConfig object. HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Specify whether to ignore certificates. clientConfig.setIgnoreSSLCerts(true); // (Optional) Specify the read timeout period. Unit: milliseconds. clientConfig.setReadTimeoutMillis(<readTimeout>); // (Optional) Specify the connection timeout period. Unit: milliseconds. clientConfig.setConnectionTimeoutMillis(<connectionTimeout>); // (Optional) Specify the maximum number of requests that are supported by each server. The supported data type is INTEGER. clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>); // (Optional) Specify the maximum number of requests. The supported data type is INTEGER. clientConfig.setMaxRequests(<maxRequests>); // (Optional) Specify the protocol type. clientConfig.setProtocolType(ProtocolType.HTTP); /** (Optional) Specify whether to configure the proxy based on your business requirements. The following code is available: clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`Or`

```
clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>"); Replace https://192.168.XX.XX:33XX with the actual IP address and port of the proxy.
```

`*/`

```
profile.setHttpClientConfig(clientConfig);
```

#### Use ROS SDK for Java

This topic describes how to use ROS SDK for Java. Procedure
1. Create an AcsClient instance.

```
new com.aliyun.ros20190910.Client(config)
```

2. Create a request.
Name the request in the ${apiName}Request format. ${apiName} indicates the name of the API operation that you want to call. Example: GetStack. If multiple client instances are used, different requests may have the same name. You can differentiate the requests based on package names.

```
GetStackRequest getStackRequest = new GetStackRequest()
                .setStackId(stackId)
                .setRegionId(regionId);
```

3. Initiate the request and process the response.

```
GetStackResponse resp = client.getStack(getStackRequest); com.aliyun.teaconsole.Client.log(com.aliyun.teautil.Common.toJSONString(TeaModel.buildM ap(resp)));
```

#### Handle errors

va When you use ROS SDK for Java, errors may occur. If an error occurs on the ROS server, the SDK returns a `ServerException` error response. If an error occurs on a client instance, the SDK returns a `ClientException` error response. An error response is composed of an error code and an error message. In general, you do not need to handle client instance errors. You need to only handle server errors. If you want to handle client instance errors, you can use the following sample code:

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handle the response.
}catch (ServerException e){
    // Specify your error handling logic.
    // For example, you can display the details of the error.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If the error is tricky, you can submit a ticket and provide the request ID.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // Specify your error handling logic.
    // For example, you can display the details of the error.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

`}` thon

## Use ROS SDK for Python

### Get started with ROS SDK for

Python This topic describes how to get started with ROS SDK for Python. Prerequisites An Apsara Stack tenant account and an AccessKey pair, which consists of an AccessKey ID and an AccessKey secret, are obtained. For more information, see Obtain an AccessKey pair. The endpoint of ROS is obtained. For more information, see Obtain the endpoint of ROS. Step 1: Install ROS SDK for Python
1. Install the core library of Alibaba Cloud SDK for Python.
If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-core-v3
```

2. Install ROS SDK for Python.
If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-ros
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-ros
```

Step 2: Use ROS SDK for Python
1. Create a client instance. When you create a client instance, you must specify a region ID, an
AccessKey ID, and an AccessKey secret.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exception.
Not e In the following code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code. The following section describes the variable parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <ros.aliyuncs.com>: Replace the parameter with the endpoint of ROS. thon

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkros.request.v20190910.ListResourceTypesRequest import ListResourceTypesRe quest
# global config
region_id = '<yourRegionID>' # Specify the region ID. access_key = '<yourAccessKeyID>' # Specify your AccessKey ID. acces_secret = '<yourAccessKeySecret>' # Specify your AccessKey secret. endpoint = '<ros.aliyuncs.com>' # Specify the endpoint of ROS.
# create client
clt = client.AcsClient(access_key, acces_secret, region_id, endpoint=endpoint)
# setup request
request = ListResourceTypesRequest() request.set_accept_format('json') # Specify the response format.
# get response
response = clt.do_action_with_exception(request) print response
```

### Use SDK

#### Install ROS SDK for Python

This topic describes how to install ROS SDK for Python. Alibaba Cloud SDK for Python supports Python 2.6.x, 2.7.x, 3.x, and later. You can install Alibaba Cloud SDK for Python by using pip.
1. Install the core library of Alibaba Cloud SDK for Python.
If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-core-v3
```

2. Install ROS SDK for Python.
If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-ros
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-ros
```

#### Configure authentication credentials

When you use Alibaba Cloud SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. ROS SDK for Python allows you to complete the authentication process by using an AccessKey pair. For more information, see Obtain an AccessKey pair. thon If you want to use your AccessKey pair to access ROS, you must configure the AccessKey pair as the credentials when you initialize a client instance. Warning Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```python
from aliyunsdkcore import client clt = client.AcsClient(secret_id, secret_key, region_id, endpoint=endpoint)
```

#### Set HTTPS requests

The Python SDK supports using HTTP and HTTPS to initiate API requests. When using the Python SDK, you can specify a protocol (HTTP or HTTPS) for a specific request to use, or set a global default protocol for all requests to use. Not e The default protocol (HTTP or HTTPS) of a product takes precedence over the global default protocol you set. Add OpenSSL dependency HTTPS of the Python SDK depends on the OpenSSL support in Python. To use Alibaba Cloud SDK to send HTTPS requests, you must add OpenSSL support in Python.

| the | python -c "import ssl" | comm |
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

thon

#### Use ROS SDK for Python

This topic describes how to use ROS SDK for Python. Procedure
1. Import ROS SDK for Python.

```python
from aliyunsdkcore import client from aliyunsdkros.request.v20190910.ListResourceTypesRequest import ListResourceTypesRe quest
```

2. Create an AcsClient instance.

```
clt = client.AcsClient(access_key, access_secret, region_id, endpoint=endpoint)
```

3. Create a request object.

```
request = ListResourceTypesRequest() request.set_accept_format('json')
```

4. Initiate the request and process the response.

```
response = clt.do_action_with_exception(request) print response
```

#### Handle errors

When you use ROS SDK for Python, errors may occur. If an error occurs on the ROS server, the SDK returns

| a | ServerException |   |
|---|---|---|
| ClientException |   | e |

a `ServerException` error response. If an error occurs on a client instance, the SDK returns a `ClientException` error response. An error response is composed of an error code and an error message. In general, you do not need to handle client instance errors. You need to only handle server errors. If you want to handle client instance errors, you can use the following sample code:

```bash
#coding=utf-8
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
    # Specify your error handling logic.
    # For example, you can display the details of the error.
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

o

## Use ROS SDK for Go

### Get started with ROS SDK for Go

Alibaba Cloud SDK for Go allows you to access services without complex coding. This topic describes how to use ROS SDK for Go. Prerequisites An Apsara Stack tenant account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information, see Obtain an AccessKey pair. An endpoint of ROS is obtained. For more information, see Obtain the endpoint of ROS. Step 1: Install the core package of Alibaba Cloud SDK for Go Alibaba Cloud SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

Step 2: Use ROS SDK for Go
1. Initialize a client instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exception.
Not e In the following sample code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code. The following section describes the variable parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <Endpoint>: Replace the parameter with your ROS endpoint. o

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "fmt"
```

`)`

```
func main() {
    // Create a client instance.
    client, err := sdk.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<
yourAccessKeySecret>")
    if err != nil {
        // Handle the exception.
        panic(err)
```

`}`

```
    // Create an API request and set the required parameters.
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Scheme = "https" // https | http
    request.Domain = "ros.aliyuncs.com"
    request.Version = "2019-09-10"
    request.ApiName = "GetStack"
    request.QueryParams["RegionId"] = "<yourRegionID>"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}`
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

When you use Alibaba Cloud SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. ROS SDK for Go allows you to complete the authentication process by using an AccessKey pair. For more information, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access ROS, you must configure the AccessKey pair as the credentials when you initialize a client instance. o Warning Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```
// Initialize a client instance. client, err := sdk.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<yourAcce ssKeySecret>")
```

Not e In the preceding sample code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code.

#### Handle errors

When you use ROS SDK for Go, errors may occur. If an error occurs on the ROS server, the SDK returns a `ServerError` error response. If an error occurs on a client instance, the SDK returns a `ClientError` error response. Both error types are included in `sdk.errors` . The errors conform to the standard Go error interface and can be handled in a similar way as standard Go errors. Handle errors You can use the following code to handle errors:

```
response,err := ecsClient.DescribeInstances(request) if err != nil {
    // Obtain the error response.
   err.Error()
```

`}` ClientError When you send a request, if an error occurs on the client instance and cannot be automatically handled, the SDK returns a `ClientError` error response. The following sample code provides an example on how to determine and obtain the error message in the `ClientError` error response:

```
client, err := sdk.NewClientWithAccessKey("cn-hangzhou-ste4-d01", "<accessKeyId>", "<access Secret>") if clientError, ok := err.(*errors.ClientError); ok{
    // Obtain the error code.
    clientError.ErrorCode()
    // Obtain the error message.
    clientError.Message()
    // Obtain the original error.
    clientError.OriginError()
```

`}` o Not e When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Add an error package.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)` ServerError When the server returns an error message, the SDK wraps the message into a `ServerError` error response and returns it to the client instance. In this case, you can still obtain the original HTTP response from the error response. The following sample code provides an example on how to determine and obtain the error message in ServerError and Response:

```
response, err := client.ProcessCommonRequest(request) if serverError, ok := err.(*errors.ServerError); ok{
    // Obtain the error code.
    serverError.ErrorCode()
    // Obtain the error message.
    serverError.Message()
    // Obtain the original HTTP response.
    response.GetOriginHttpResponse()
```

`}` Not e When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Add an error package.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

#### Use CommonRequest to call API operations

o If you want to call the API operations of an Apsara Stack service that does not provide SDKs, or the requests and responses of the API operations that you call by using an SDK do not meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations. The following sample code provides an example on how to query details of a stack by calling the GetStack operation of ROS. Not e In the following sample code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code. The following section describes the variable parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <ros.aliyuncs.com>: Replace the parameter with the endpoint of the service. <yourSecurityToken>: Replace the parameter with your security token. <yourResourceGroupID>: Replace the parameter with the resource set ID. <yourOrganizationID>: Replace the parameter with the organization ID. o

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
        "<yourAccessKeyID>",     //Replace the parameter with your AccessKey ID.
        "<yourAccessKeySecret>") //Replace the parameter with your AccessKey secret.
    if err != nil {
        panic(err)
```

`}`

```
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<ros.aliyuncs.com>" // The endpoint of the service. Replace the sampl
e value with the actual endpoint of the service.
    request.Version = "2019-09-10"
    // The name of the API operation. This parameter is required because the operation is t
o be called by using the Remote Procedure Call (RPC) style.
    request.ApiName = "GetStack"
    // The business parameters.
    request.QueryParams["RegionId"] = "<yourRegionID>"
```

`/*`

```
     When you use STS AccessKey credentials to call an RPC API operation, you must add the
SecurityToken field in the request parameters.
     You can use the following syntax to specify this field:
     request.QueryParams["SecurityToken"]="<yourSecurityToken>"
     Replace the field value with your security token.
```

`*/`

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo" // Required. The source of t
he call.
    request.Headers["x-acs-regionid"] = "<yourRegionID>" // Optional. Specify the region ID
```

`.`

```
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // Optional. Specify
the resource set ID.
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // Required. Specify t
he organization ID.
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}`

## API Reference

### List of operations by function

The following tables list API operations available for use in Resource Orchestration Service (ROS). Stack operations

| Operation | Description |
|---|---|
| CreateStack | Creates a stack. |
| ContinueCreateStack | Creates a new stack based on the template of the previous stack that fails to be created. |
| UpdateStack | Updates a stack. |
| CancelUpdateStack | Cancels the update of a stack. |
| GetStack | Queries information about stacks. |
| DeleteStack | Deletes a stack. |
| ListStacks | Queries the list of stacks. |
| PreviewStack | Previews the stack to be created by using a specified template. |
| ListStackEvents | Queries stacks and their resource events. |

Resource operations

| Operation | Description |
|---|---|
| GetResourceTypeTemplate | Queries the template of a resource by resource type. |
| ListStackResources | Queries the resource list of a specific stack. |
| GetStackResource | Queries information about a resource in a specific stack. |
| GetResourceType | Queries detailed information about a resource type. |
| ListResourceTypes | Queries the list of supported resource types. |

Template operations

| Operation | Description |
|---|---|
| GetTemplateEstimateCost | Queries estimated prices of resources to be created based on a template. |
| ValidateTemplate | Validates the template that is used to create stacks. |

| esource Orchestration Service | Developer Guide·API Referenc |
|---|---|

| Operation | Description |
|---|---|
| GetTemplate | Queries detailed information about a template, including stacks and change sets associated with the template. |
| DeleteTemplate | Deletes a template. |
| ListTemplates | Queries the list of templates. |
| CreateTemplate | Creates a template. |
| UpdateTemplate | Updates a template. |
| GetTemplateSummary | Queries information about a new or existing template. |

Stack policy operations

| Operation | Description |
|---|---|
| SetStackPolicy | Configures a stack policy. |
| GetStackPolicy | Queries information about a stack policy. |

Other operations

| Operation | Description |
|---|---|
| DescribeRegions | Queries available regions. |
| SignalResource | Sends signals. |
| SetDeletionProtection | Configures deletion protection on a stack. |
| ListStackOperationRisks | Detects the resources that may face high risks caused by a stack deletion operation, and queries the reason for each risk. |

### Make API calls

To call the ROS API, you must send HTTP GET requests to the endpoint of the ROS API. You must add the request parameters that correspond to the API operation being called. After you call the API operation, the system returns a response. The request and response are both encoded in UTF-8. Request syntax ROS API operations use the RPC protocol. You can call ROS API operations by sending HTTP GET requests. The following example describes the request syntax of a ROS API request:

```
http://Endpoint/?Action=xx&Parameters
```

The following table describes the parameters in the request syntax.

| Parameter | Description |
|---|---|
| Endpoint | The endpoint of the ROS API. Set the value to ros.aliyuncs.com. |
| Action | The name of the operation being performed. For example, to query the list of stacks, set the value to ListStacks. |
| Parameters | The request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operation-specific parameters. Common parameters include information such as the API version number and authentication information. For more information, see Common parameters. |

Sample requests The following example demonstrates how to call the ListStacks operation to query the list of stacks: Not e The sample requests in this topic are formatted for better readability.

```
http(s)://ros.aliyuncs.com/? Action=ListStacks &RegionId=cn-hangzhou &Format=JSON &Version=2019-09-10 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=1521552885**** &SignatureVersion=1.0 &AccessKeyId=LTAI4GK3D6YtNkNZfjDV**** &TimeStamp=2020-05-01T12:00:00Z
```

…

### Request signatures

You must sign all API requests to ensure security. Alibaba Cloud uses the request signature to verify the identity of the API caller. Each API request must contain the signature, regardless of whether the request is sent over HTTP or HTTPS. Overview You must add the signature to the ROS API request in the following format:

```
https://Endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-SHA1&Signature=CT9X0VtwR86fNWSn sc6v8YGOjuE%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf
```

A signature contains the following parameters: SignatureMethod: the encryption method of the signature string. Set the value to HMAC-SHA1. SignatureVersion: the version of the signature encryption algorithm. Set the value to 1.0. SignatureNonce: a unique, random number used to prevent replay attacks. You must use different random numbers for different requests. We recommend that you use universally unique identifiers (UUIDs). Signature: the signature generated after the request has been symmetrically encrypted by using the AccessKey secret. The signature encryption algorithm complies with RFC 2104 HMAC-SHA1 specifications. The AccessKey secret is used to calculate the hash-based message authentication code (HMAC) value of the encoded and sorted query string, and the HMAC value is used as the signature string. Request signatures include operation-specific parameters. Therefore, the signature of a request varies based on the request parameters. To calculate a signature, follow the steps in this topic.

```
Signature = Base64( HMAC-SHA1( AccessKey Secret, UTF-8-Encoding-Of(StringToSign)) )
```

Step 1: Compose and encode a string-to-sign
1. Create a canonicalized query string by using the request parameters.
i. Create a canonicalized query string by arranging the request parameters (including all common and operation-specific parameters except Signature) in alphabetical order. Not e If you use the GET method to submit the request, these parameters are the part located after the question mark (?) and connected by the ampersands (&) in the request uniform resource identifier (URI). ii. Encode the names and values of the arranged request parameters in the request URL by using the unicode transformation format (UTF)-8 character set. The following table describes the encoding rules.

| Character | Encoding rule |
|---|---|
| Uppercase letters, lowercase letters, digits, hyphens (-), underscores ( ), periods (.), _ and tildes (~) | These characters do not need to be encoded. |
| Other characters | These characters must be percent encoded in %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22 . |
| Extended ASCII characters (UTF-8) | These characters are encoded in %XY%ZA... format. |
| Spaces | Spaces must be encoded as %20 . Do not encode spaces as plus signs (+). This encoding method is different from the application/x-ww w-form-urlencoded MIME encoding algorithm (such as the j ava.net.URLEncoder class provided by the Java standard library). However, you can apply the encoding algorithm and replace the plus sign (+) in the encoded string with %20 , the asterisk (*) with %2A , and the tilde (~) with %7E . You can use the following percentEncode method to implement this algorithm: private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException { return value ! = null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").replace("*", "%2A").replace("%7E", "~") : null; } |

|   |   | w-form-urlencoded |
|---|---|---|

|   | %20 |
|---|---|
| %7E |   |

iii. Connect the encoded parameter names and their values by using equal signs (=). iv. Sort the connected parameter name and value pairs in the order specified in step i and connect the pairs by using ampersands (&) to obtain the canonicalized query string.
2. Create a string-to-sign from the encoded canonicalized query string in the following way:

```
StringToSign=
      HTTPMethod + "&" +
      percentEncode("/") + "&" +
       percentEncode(CanonicalizedQueryString)
```

A string-to-sign contains the following parameters: HTTPMethod: the HTTP method used to submit a request, such as GET. percentEncode("/"): specifies the encoded value (%2F) of a forward slash (/). The encoding follows the URL encoding rules. percentEncode(CanonicalizedQueryString): specifies the encoded canonicalized query string based on the URL encoding rules. Step 2: Calculate the signature string
1. Calculate the HMAC value of the string-to-sign based on RFC 2104.
Not e Use the SHA1 algorithm to calculate the HMAC value of the string-to-sign. The combination of your AccessKey secret and an ampersand (&) (ASCII code 38) that follows the secret is used as the key for the HMAC calculation.
2. Encode the HMAC value in Base64 to obtain the signature string.
3. Add the signature string to the request as the Signature parameter.
Not e When the obtained signature value is submitted as the final request parameter value, the value must be URL-encoded that is similar to other parameters based on rules defined in RFC 3986.

| DescribeRegions |   |   |
|---|---|---|
| n | AccessKeyID | is |

The `DescribeRegions` operation is used in this example. This example shows the signature process when `AccessKeyID` is set to testid and `AccessKeySecret` is set to testsecret:
1. Create a canonicalized query string.

```
http://ros.aliyuncs.com/?Timestamp=2019-08-23T12%3A46%3A24Z&Format=XML&AccessKeyId=test id&Action=DescribeRegions&SignatureMethod=HMAC-SHA1&SignatureNonce=3ee8c1b8-83d3-44af-a 94f-4e0ad82fd6cf&Version=2019-09-10&SignatureVersion=1.0
```

2. Create a string-to-sign.

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DDescribeRegions%26Format%3DXML%26SignatureMetho d%3DHMAC-SHA1%26SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf%26SignatureVersio n%3D1.0%26Timestamp%3D2019-08-23T12%253A46%253A24Z%26Version%3D2019-09-10
```

3. Calculate the signature. Because `AccessKeySecret` is set to testsecret, the key value used for
calculation is `testsecret&` . The calculated signature is `OLeaidS1JvxuMvnyHOwuJ+uX5qY=` . The Java Base64 encoding method is used in this example.

```
Signature = Base64( HMAC-SHA1( AccessSecret, UTF-8-Encoding-Of(StringToSign) ) )
```

4. Add the Signature=OLeaidS1JvxuMvnyHOwuJ%2BuX5qY%3D string that has been encoded based on
RFC 3986 to the URL in Step 1.

```
http://ros.aliyuncs.com/?SignatureVersion=1.0&Action=DescribeRegions&Format=XML&Signatu reNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&Version=2019-09-10&AccessKeyId=testid&Sign ature=OLeaidS1JvxuMvnyHOwuJ%2BuX5qY%3D&SignatureMethod=HMAC-SHA1&Timestamp=2019-08-23T1 2%253A46%253A24Z
```

You can use browsers or tools such as cURL and Wget to initiate an HTTP request by using the new URL. The HTTP request calls the `DescribeRegions` operation to query the Alibaba Cloud region list.

### Common parameters

This topic describes the common request and response parameters. Common request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The format in which to return the response. Default value: JSON. Valid values: JSON XML |
| Version | String | Yes | The API version of the service. Specify the version number in the YYYY-MM-DD format. Set the value to 2019- 09-10. |
| AccessKeyId | String | Yes | The AccessKey ID used to connect to the service. The AccessKey ID is provided by Alibaba Cloud for authentication. |
| Signature | String | Yes | The signature string of the request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC- SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY- MM-DDThh:mm:ssZ format. The time must be in UTC. Example: 2020-01- 10T12:00:00Z. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |

Sample requests

```
http(s)://ros.aliyuncs.com/? Action=XXXXXX &Format=xml &Version=2019-09-10 &Signature=Pc5WB8gokVn0xfeu%2FZV%2BiNM1dgI%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=1521552885**** &SignatureVersion=1.0 &AccessKeyId=LTAI4GK3D6YtNkNZfjDV**** &TimeStamp=2020-05-01T12:00:00Z
```

Common response parameters Responses can be returned in the JSON or XML format. You can specify the response format in the request. The default response format is JSON. Every response returns a unique RequestId value regardless of whether the call is successful. A `2xx` HTTP status code indicates a successful call. A `4xx` or `5xx` HTTP status code indicates a failed call. Sample responses XML format

```xml
<? xml version="1.0" encoding="utf-8"? >
    <!—Result Root Node-->
    <Interface Name+Response>
        <!—Return Request Tag-->
        <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
        <!—Return Result Data-->
    </Interface Name+Response>
```

JSON format `{`

```json
    "RequestId":"4C467B38-3910-447D-87BC-AC049166F216"
    /*Return Result Data*/
```

`}`

### Common error codes

This topic describes the common client and server error codes. Client error codes

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| UnknownError | The request processing has failed due to some unknown error. | 400 | The error message returned because an unknown error that is not caused by a server-side issue has occurred on the client. |
| MissingParameter | The input parameter {name} should be specified. | 400 | The error message returned because the input parameter is missing. name indicates the parameter name. |
|   | One of the input parameters {names} should be specified. | 400 | The error message returned because the input parameter is missing. You must specify one of the input parameters. names indicates the names of all the related parameters. |
|   | The input parameter {name} should be specified, {reason}. | 400 | The error message returned because the input parameter is missing. name indicates the parameter name, and reason indicates the specific reason. |
| InvalidParameter | The specified parameter {name} is invalid. | 400 | The error message returned because the specified parameter is invalid. name indicates the parameter name. |
|   | The specified parameter {name} is invalid, {reason}. | 400 | The error message returned because the specified parameter is invalid. name indicates the parameter name, and reason indicates the specific reason. |
| MultipleParameter | Only one of the input parameters {names} can be specified. | 400 | The error message returned because the number of specified parameters exceeds the limit. You can specify only one of the parameters. names indicates the names of all the related parameters. |

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InvalidIdempotenceP arameter | The specified parameters are different from before. | 400 | The error message returned because the idempotent token is the same, but the specified parameters are different from before. |
| LastTokenProcessin g | The last token request is processing. | 400 | The error message returned because the previous token request is being processed. Try again later. |
| Invalid | Data supplied was not valid: {reason}. | 400 | The error message returned because the value is invalid. reason indicates the specific reason. |
| InvalidValue | {reason}. | 400 | The error message returned because the value is invalid. reason indicates the specific reason. |
| RequestLimitExceed ed | Request limit exceeded: {reason}. | 400 | The error message returned because the request contains content that exceeds the limit. reason indicates the specific reason. You can change the part of content that exceeds the limit by adjusting the quota. |
| NotSupported | {feature} is not supported. | 400 | The error message returned because a specified feature is not supported. feature indicates the specific feature or operation. |
| MismatchNextToken | {name} mismatches next token. | 400 | The error message returned because the specified parameter does not match the next token. name indicates the parameter name. |
| AssumeRoleFailure | Fail to assume role {name}: {reason} | 400 | The error message returned because ROS has failed to obtain a temporary identity to assume the specified RAM role. name indicates the RAM role name, and reason indicates the specific reason for the failure. |

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| Forbidden | You are not authorized to complete this action. | 403 | The error message returned because you are not authorized to complete this action. |
|   | A required authorization for the specified action {api} is not supplied. Code: {code} RequestId: {request id} _ | 403 | The error message returned because you have not authorized ROS to call the operation. api indicates the name of the operation. code indicates the error code. request id indicates the ID of _ the request. |
| AccountTypeNotSup ported | Account type not supported. | 403 | The error message returned because the specified account type is not supported. |
| NotFound | {reason}. | 404 | The error message returned because the request contains content that does not exist. reason indicates the specific reason. |

Server error codes

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InternalError | Server error. | 500 | The error message returned because an internal error has occurred. |
| ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 | The error message returned because a server error has occurred. Try again later. If the problem persists, submit a ticket. |

### Stack operations

#### CreateStack

You can call this operation to create a stack. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateStack | The operation that you want to perform. Set the value to CreateStack. |
| Parameters.N.Par ameterKey | String | Yes | InstanceId | The key of parameter N. If the key and value of the parameter are not specified, the key and value in the template are used. Maximum value of N: 200. Not e Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.ParameterKe y and Parameters.N.ParameterVa lue. |
| Parameters.N.Par ameterValue | String | Yes | i-xxxxxx | The value of parameter N. Maximum value of N: 200. Not e Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.ParameterKe y and Parameters.N.ParameterVa lue. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackName | String | Yes | MyStack | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a digit or letter. _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| DisableRollback | Boolean | No | false | Specifies whether to disable rollback on stack creation failure. Default value: false. Valid values: true: disables rollback on stack creation failure. false: enables rollback on stack creation failure. |
| TemplateBody | String | No | { "ROSTemplateFor matVersion": "2015-09-01" } | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| StackPolicyURL | String | No | oss://ros-stack- policy/demo | The URL of the file that contains the stack policy. The URL must point to a policy located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/stack- policy/demo and oss://ros/stack- policy/demo?RegionId=cn-hangzhou. The policy can be up to 16,384 bytes in length and the URL can be up to 1,350 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |
| TimeoutInMinutes | Long | No | 10 | The timeout period that is specified for the stack creation request. Default value: 60. Unit: minutes. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StackPolicyBody | String | No | {"Statement": [{"Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*"}]} | The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |
| TemplateURL | String | No | oss://ros- template/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template must be 1 to 524,288 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

|   | Parameter | Type | Required | Example | Description |   |
|---|---|---|---|---|---|---|
|   | NotificationURLs. N | RepeatLi st | No | http://my- site.com/ros- event | The callback URL for receiving stack event N. Only HTTP POST is supported. Maximum value of N: 5. Each URL can be up to 1,024 bytes in length. ROS sends a notification to the specified URL when the stack state changes. If rollback is enabled on the stack, notifications are sent if the stack is in the CREATE ROLLBACK or ROLLBACK _ state, but are not sent when the stack is in the CREATE FAILED or _ UPDATE FAILED state. _ Not e ROS does not send notifications when the stack is in the IN PROGRESS state. _ Notifications are sent regardless of whether the Outputs parameter is specified. The following code is an example of a notification: { "Outputs": [ { "Description": "No description given", "OutputKey": "InstanceId", "OutputValue": "i-xxx" } ], "StackId": "80bd6b6c- e888-4573-ae3b-93d29113****", "StackName": "test- notification-url", "Status": "CREATE COMPLETE" _ } |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RamRoleName | String | No | test-role | The name of the RAM role. ROS assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permission to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS uses the role previously associated with the stack. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |
| DeletionProtectio n | String | No | Enabled | Specifies whether to enable deletion protection on the stack. Default value: Disabled. Valid values: Enabled: enables deletion protection on the stack. Disabled: disables deletion protection on the stack. You can release the stack by using the ROS console or by calling the DeleteStack operation. Not e The deletion protection property of a nested stack is the same as that of its root stack. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CreateOption | String | No | KeepStackOnCrea tionComplete | Specifies whether to delete the stack after it is created. Default value: KeepStackOnCreationComplete. Valid values: KeepStackOnCreationComplete: retains the stack and all its resources after the stack is created. AbandonStackOnCreationComplete: deletes the stack but retains all its resources after the stack is created. This helps you ensure that the maximum number of stacks allowed to be created is not reached. If the stack fails to be created, the stack is retained. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=CreateStack &RegionId=cn-hangzhou &StackName=MyStack &Parameters.1.ParameterKey=InstanceId &Parameters.1.ParameterValue=i-xxxxxx &TimeoutInMinutes=10 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateStackResponse>
          <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
          <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</CreateStackResponse>
```

`JSON` format `{`

```json
    "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****",
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| CircularDependency | Circular Dependency Found: {reason}. | 400 | The error message returned because the template contains a circular reference. reason indicates the specific reason. |
| InvalidSchema | {reason}. | 400 | The error message returned because the specified template format is incorrect. reason indicates the specific reason. |
| InvalidTemplateAttribut e | The Referenced Attribute ({resource} {name}) is incorrect. | 400 | The error message returned because the resource attribute referenced in the template is incorrect. resource indicates the resource name, and name indicates the attribute name. |
| InvalidTemplatePropert yType | The specified value type of ({resource} {section}) is incorrect. | 400 | The error message returned because the type of the specified resource section defined in the template is invalid. resource indicates the resource name, and section indicates the section name. |

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InvalidTemplateReferen ce | The specified reference "{name}" (in {referencer}) is incorrect. | 400 | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| InvalidTemplateSection | The template section is invalid: {section}. | 400 | The error message returned because the template contains an invalid section. section indicates the section name. |
| InvalidTemplateVersion | The template version is invalid: {reason}. | 400 | The error message returned because the template version is incorrect. reason indicates the specific reason. |
| StackValidationFailed | {reason}. | 400 | The error message returned because the stack validation failed. reason indicates the specific reason. |
| UnknownUserParameter | The Parameter ({name}) was not defined in template. | 400 | The error message returned because the specified parameter is not defined in the template. name indicates the parameter key. |
| UserParameterMissing | The Parameter {name} was not provided. | 400 | The error message returned because no value is passed into the specified parameter defined in the template. name indicates the parameter key. |

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| ActionInProgress | Stack {name} already has an action ({action}) in progress. | 409 | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |
| StackExists | The Stack ({name}) already exists. | 409 | The error message returned because a stack with the same name already exists. name indicates the stack name. |

#### ContinueCreateStack

You can call this operation to create a stack based on the template of the previous stack that fails to be created. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ContinueCreateSt ack | The operation that you want to perform. Set the value to ContinueCreateStack. |
| Parameters.N.Par ameterKey | String | Yes | Amount | The key of the template parameter N to be overridden. If the key and value of the parameter are not specified, the key and value are set to those in the template of the stack that fails to be created. Maximum value of N: 200. Not e This parameter takes effect only when the Mode parameter is set to Recreate. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Parameters.N.Par ameterValue | String | Yes | 12 | The value of the template parameter N to be overridden. Maximum value of N: 200. This parameter takes effect only when the Mode parameter is set to Recreate. Take note of the following limits on the template parameter to be overridden: This parameter cannot change values in the Conditions section of the template from true to false or from false to true. This parameter can only be referenced by resources that are recreated. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| RecreatingResour ces.N | RepeatLi st | No | WebServer | The resource N to be recreated upon creation failure. ROS recreates the resources you list in this parameter and all resources that depend on the resources. |
| RamRoleName | String | No | test-role | The name of the RAM role. ROS assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permission to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS uses the role previously associated with the stack. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Mode | String | No | Recreate | The stack recreation mode. Default value: Recreate. Valid values: Recreate Only the following types of resources are recreated: Resources that fail to be created. Resources specified in the RecreatingResources.N parameter. Resources that depend on the resources specified in the RecreatingResources.N parameter. Resources for which creation operations are not initiated. The RecreatingResources.N, TemplateBody, TemplateURL, and Parameters parameters take effect only when the Mode parameter is set to Recreate. Ignore: ROS ignores and discards all resources that fail to be recreated and the resources for which creation operations are not initiated. Then, the stack creation operation is marked as successful. Content of the template is changed. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateBody | String | No | { "ROSTemplateFor matVersion": "2015-09-01" } | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. This parameter takes effect only when the Mode parameter is set to Recreate. Take note of the following limits on the template: Only the Description, Metadata, Resources, and Outputs sections in the template can be modified. No sections can be added to or removed from the outermost layer of the template. Take note of the following limits on the Resources section of the template: The resources not to be recreated cannot be deleted, and their template content cannot be modified. The resources to be recreated can be deleted, and their template content can be modified. New resources can be added. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateURL | String | No | oss://ros- template/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. This parameter takes effect only when the Mode parameter is set to Recreate. For the limits on the template specified in this parameter, see the description of the TemplateBody parameter. |
| DryRun | Boolean | No | false | Specifies whether to check the validity of the request without actually making the request. Default value: false. Valid values: true: checks the validity of the request without actually making the request. false: makes the request to recreate the stack. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ContinueCreateStack &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ContinueCreateStackResponse>
       <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
       <StackId type="string">0a7c379a-566f-4bc0-b3fb-a301df51****</StackId>
</ContinueCreateStackResponse>
```

`JSON` format `{`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "StackId": "0a7c379a-566f-4bc0-b3fb-a301df51****"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | CircularDependency | Circular Dependency Found: {reason}. | The error message returned because the template contains a circular reference. reason indicates the specific reason. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidSchema | {reason}. | The error message returned because the specified template format is invalid. reason indicates the specific reason. |
| 400 | InvalidTemplateAttribut e | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is invalid. resource indicates the resource name, and name indicates the attribute name. |
| 400 | InvalidTemplatePropert yType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is invalid. resource indicates the resource name, and section indicates the section name. |
| 400 | InvalidTemplateReferen ce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| 400 | InvalidTemplateSection | The template section is invalid: {section}. | The error message returned because the template contains an invalid section. section indicates the section name. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidTemplateVersion | The template version is invalid: {reason}. | The error message returned because the template version is invalid. reason indicates the specific reason. |
| 400 | StackValidationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |
| 400 | UnknownUserParameter | The Parameter ({name}) was not defined in template. | The error message returned because the specified parameter is not defined in the template. name indicates the parameter key. |
| 400 | UserParameterMissing | The Parameter {name} was not provided. | The error message returned because no value is passed into the specified parameter defined in the template. name indicates the parameter key. |
| 400 | ContinueCreateStackVali dationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |
| 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | The error message returned because the specified resource does not exist in the specified stack. name indicates the resource name, and stack indicates the stack name or ID. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |

#### UpdateStack

You can call this operation to update a stack. The values of Parameters and UsePreviousParameters in the request are related. If parameters defined in the template are not specified by Parameters, take note of the following items: When UsePreviousParameters is set to false, if the parameter has a default value in the template, the default value is used. If the parameter does not have a default value in the template, you must specify the parameter in the Parameters section. When UsePreviousParameters is set to true, if the parameter is specified when the stack is created, the specified value is used. If the parameter is not specified and it has a default value in the template, the default value is used. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateStack | The operation that you want to perform. Set the value to UpdateStack. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Parameters.N.Par ameterKey | String | Yes | Amount | The key of parameter N. If the key and value of the parameter are not specified, the key and value in the template are used. Maximum value of N: 200. Not e Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.ParameterKe y and Parameters.N.ParameterVa lue. |
| Parameters.N.Par ameterValue | String | Yes | 12 | The value of parameter N. Maximum value of N: 200. Not e Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.ParameterKe y and Parameters.N.ParameterVa lue. |
| RegionId | String | Yes | cn-beijing | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |
| StackPolicyDuring UpdateBody | String | No | {"Statement": [{"Effect": "Allow", "Action": "Update:*", "Principal": "*", "Resource": "*"}]} | The structure that contains the body of the temporary overriding stack policy. The stack policy body must be 1 to 16,384 bytes in length. To update protected resources, specify a temporary overriding stack policy during the update. If you do not specify a stack policy, the current policy that is associated with the stack is used. This parameter takes effect only when the ChangeSetType parameter is set to UPDATE. You can specify only one of the following parameters: StackPolicyBody StackPolicyURL StackPolicyDuringUpdateBody StackPolicyDuringUpdateURL |
| TimeoutInMinutes | Long | No | 10 | The timeout period that is specified for the stack update request. Default value: 60. Unit: minutes. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateBody | String | No | {"ROSTemplateFo rmatVersion": "2015-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| StackPolicyURL | String | No | oss://ros-stack- policy/demo | The URL of the file that contains the stack policy. The URL must point to a policy located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/stack- policy/demo and oss://ros/stack- policy/demo?RegionId=cn-hangzhou. The policy can be up to 16,384 bytes in length and the URL can be up to 1,350 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StackPolicyDuring UpdateURL | String | No | oss://ros-stack- policy/demo | The URL of the file that contains the temporary overriding stack policy. The URL must point to a policy located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/stack-policy/demo and oss://ros/stack-policy/demo? RegionId=cn-hangzhou. The policy can be up to 16,384 bytes in length and the URL can be up to 1,350 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. To update protected resources, specify a temporary overriding stack policy during the update. If you do not specify a stack policy, the current policy that is associated with the stack is used. This parameter takes effect only when the ChangeSetType parameter is set to UPDATE. You can specify only one of the following parameters: StackPolicyBody StackPolicyURL StackPolicyDuringUpdateBody StackPolicyDuringUpdateURL |
| StackPolicyBody | String | No | {"Statement": [{"Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*"}]} | The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UsePreviousPara meters | Boolean | No | true | Specifies whether to use the values that were passed last time for the parameters that you do not specify in the current request. Valid values: true false |
| DisableRollback | Boolean | No | false | This parameter cannot take effect when the stack is being updated. If the update fails, a rollback is performed regardless of the value of this parameter. |
| TemplateURL | String | No | oss://ros- template/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template must be 1 to 524,288 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RamRoleName | String | No | test-role | The name of the RAM role. ROS assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permission to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS uses the role previously associated with the stack. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |
| ReplacementOpti on | String | No | Disabled | Specifies whether to enable replacement update after a resource attribute that does not support modification update is changed. Modification update keeps the physical ID of the resource unchanged. However, the resource is deleted and then recreated, and its physical ID is changed if replacement update is enabled. Default value: Disabled. Valid values: Enable: enables replacement update. Disabled: disables replacement update. Not e Modification update takes precedence over replacement update. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

|   | Developer Guide·AP | I Reference |   | Resource Orchestration Servic | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=UpdateStack &RegionId=cn-beijing &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &Parameters.1.ParameterKey=Amount &Parameters.1.ParameterValue=12 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UpdateStackResponse>
      <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
      <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</UpdateStackResponse>
```

`JSON` format `{`

```json
    "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****",
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | CircularDependency | Circular Dependency Found: {reason}. | The error message returned because the template contains a circular dependency. reason indicates the specific reason. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidSchema | {reason}. | The error message returned because the specified template format is incorrect. reason indicates the specific reason. |
| 400 | InvalidTemplateAttribut e | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is incorrect. resource indicates the resource name, and name indicates the attribute name. |
| 400 | InvalidTemplatePropert yType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is incorrect. resource indicates the resource name, and section indicates the section name. |
| 400 | InvalidTemplateReferen ce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| 400 | InvalidTemplateSection | The template section is invalid: {section}. | The error message returned because the template contains an invalid section. section indicates the section name. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidTemplateVersion | The template version is invalid: {reason}. | The error message returned because the template version is incorrect. reason indicates the specific reason. |
| 400 | StackPolicyValidationFai led | Action denied by stack policy: {reason}. | The error message returned because the stack policy validation failed. reason indicates the specific reason. |
| 400 | StackValidationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |
| 400 | UnknownUserParameter | The Parameter ({name}) was not defined in template. | The error message returned because the specified parameter is not defined in the template. name indicates the parameter key. |
| 400 | UserParameterMissing | The Parameter {name} was not provided. | The error message returned because no value is passed into the specified parameter defined in the template. name indicates the parameter key. |
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |

#### CancelUpdateStack

You can call this operation to cancel the update of a stack. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CancelUpdateSta ck | The operation that you want to perform. Set the value to CancelUpdateStack. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| CancelType | String | No | Safe | The method to cancel the update operation. Valid values: Quick: cancels the update of a stack as soon as possible. Safe: cancels the update of a stack as safely as possible. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=CancelUpdateStack &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CancelUpdateStackResponse>
         <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
         <StackId type="string">4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
</CancelUpdateStackResponse>
```

`JSON` format `{`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |

#### GetStack

You can call this operation to query information about a stack. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetStack | The operation that you want to perform. Set the value to GetStack. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | String | 2019-08- 01T04:07:39 | The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
| Description | String | my stack description | The description of the stack. |
| DisableRollback | Boolean | false | Indicates whether rollback is disabled on stack creation failure. Default value: false. Valid values: true: The rollback on stack creation failure is disabled. false: The rollback on stack creation failure is enabled. |
| NotificationURL s | List | ["http://127.XX.XX. 1:8080/x", "http://127.0.XX.XX :8080/y"] | The callback URLs for receiving stack events. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Outputs | List | [{"Description": "Instance ID","OutputKey": "InstanceId","Output Value": "i-a****"}] | The output parameters of the stack. |
| Parameters | Array of Parameter |   | The list of input parameters of the stack. |
| ParameterKey | String | InstanceType | The key of the parameter. |
| ParameterValu e | String | ecs.cm4.6xlarge | The value of the parameter. |
| ParentStackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf692**** | The ID of the parent stack. |
| RegionId | String | cn-beijing | The region ID of the stack. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | CREATE COMPLETE _ | The state of the stack. Valid values: CREATE IN PROGRESS _ _ CREATE FAILED _ CREATE COMPLETE _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CREATE ROLLBACK IN PROGRESS _ _ _ CREATE ROLLBACK FAILED _ _ CREATE ROLLBACK COMPLETE _ _ ROLLBACK IN PROGRESS _ _ ROLLBACK FAILED _ ROLLBACK COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ REVIEW IN PROGRESS _ _ IMPORT CREATE IN PROGRESS _ _ _ IMPORT CREATE FAILED _ _ IMPORT CREATE COMPLETE _ _ IMPORT CREATE ROLLBACK IN PROGRESS _ _ _ _ IMPORT CREATE ROLLBACK FAILED _ _ _ IMPORT CREATE ROLLBACK COMPLETE _ _ _ IMPORT UPDATE IN PROGRESS _ _ _ IMPORT UPDATE FAILED _ _ IMPORT UPDATE COMPLETE _ _ IMPORT UPDATE ROLLBACK IN PROGRESS _ _ _ _ IMPORT UPDATE ROLLBACK FAILED _ _ _ IMPORT UPDATE ROLLBACK COMPLETE _ _ _ |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StackName | String | MyStack | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must _ start with a digit or letter. |
| UpdateTime | String | 2019-08- 01T04:07:39 | The time when the stack was last updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
| StatusReason | String | Stack successfully created | The reason why the stack is in its current state. |
| TemplateDescri ption | String | Some description | The description of the stack. |
| TimeoutInMinut es | Integer | 10 | The timeout period that is specified for the stack creation request. Unit: minutes. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |
| DeletionProtect ion | String | Enabled | Indicates whether deletion protection is enabled on the stack. Valid values: Enabled: Deletion protection is enabled on the stack. Disabled: Deletion protection is disabled on the stack. You can release the stack by using the ROS console or by calling the DeleteStack operation. Not e The deletion protection property of a nested stack is the same as that of its root stack. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DriftDetectionTi me | String | 2020-02- 27T07:47:47 | The time when the last successful drift detection operation was initiated. |
| RamRoleName | String | test-role | The name of the RAM role. ROS assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permission to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS uses the role previously associated with the stack. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |
| RootStackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf692**** | The ID of the root stack. This parameter is returned if the specified stack is a nested stack. |
| StackDriftStatu s | String | IN SYNC _ | The drift state of the stack in the last successful drift detection. Valid values: DRIFTED: The stack has drifted. NOT CHECKED: No drift detection has _ been successful on the stack group. IN SYNC: The stack is being synchronized. _ |
| StackType | String | ROS | The type of the stack. Valid values: ROS: The stack was created based on an ROS template. Terraform: The stack was created based on a Terraform template. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetStack &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetStackResponse>
          <CreationTime>2019-08-01T04:07:39</CreationTime>
          <Description>No description</Description>
          <DisableRollback>false</DisableRollback>
          <NotificationURLs>http://127.0.XX.XX:8080/x</NotificationURLs>
          <NotificationURLs>http://127.0.XX.XX:8080/y</NotificationURLs>
          <Outputs>
                <Description>Instance ID</Description>
                <OutputKey>InstanceId</OutputKey>
                <OutputValue>i-a****</OutputValue>
          </Outputs>
          <Parameters>
                <ParameterKey>InstanceType</ParameterKey>
                <ParameterValue>ecs.cm4.6xlarge</ParameterValue>
          </Parameters>
          <RegionId>cn-hangzhou</RegionId>
          <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
          <StackName>MyStack</StackName>
          <Status>CREATE_COMPLETE</Status>
          <StatusReason>Stack successfully created</StatusReason>
          <TemplateDescription>Some description</TemplateDescription>
          <TimeoutInMinutes>10</TimeoutInMinutes>
          <UpdatedTime>2019-08-01T04:07:39</UpdatedTime>
          <ParentStackId>4a6c9851-3b0f-4f5f-b4ca-a14bf692****</ParentStackId>
          <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
          <StackDriftStatus>IN_SYNC</StackDriftStatus>
          <RamRoleName>test-role</RamRoleName>
          <DeletionProtection>Enabled</DeletionProtection>
          <RootStackId>4a6c9851-3b0f-4f5f-b4ca-a14bf692****</RootStackId>
          <StackType>ROS</StackType>
          <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</GetStackResponse>
```

`JSON` format `{`

```json
    "CreationTime": "2019-08-01T04:07:39",
    "Description": "No description",
    "DisableRollback": false,
    "NotificationURLs": [
        "http://127.0.XX.XX:8080/x",
        "http://127.0.XX.XX:8080/y"
```

`],`

```json
    "Outputs": [
```

`{`

```json
            "Description": "Instance ID",
            "OutputKey": "InstanceId",
            "OutputValue": "i-a****"
```

`}` `],`

```json
    "Parameters": [
```

`{`

```json
            "ParameterKey": "InstanceType",
            "ParameterValue": "ecs.cm4.6xlarge"
```

`}` `],`

```json
    "RegionId": "cn-hangzhou",
    "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****",
    "StackName": "MyStack",
    "Status": "CREATE_COMPLETE",
    "StatusReason": "Stack successfully created",
    "TemplateDescription": "Some description",
    "TimeoutInMinutes": 10,
    "UpdatedTime": "2019-08-01T04:07:39",
    "ParentStackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf692****",
    "DriftDetectionTime": "2020-02-27T07:47:47",
    "StackDriftStatus": "IN_SYNC",
    "RamRoleName": "test-role",
    "DeletionProtection": "Enabled",
    "RootStackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf692****",
    "StackType": "ROS",
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

#### DeleteStack

You can call this operation to delete a stack and all of its resources. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteStack | The operation that you want to perform. Set the value to DeleteStack. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| RetainAllResource s | Boolean | No | false | Specifies whether to retain the resources in the stack. |
| RetainResources. N | RepeatLi st | No | WebServer | The list of resources to retain. |
| RamRoleName | String | No | test-role | The name of the RAM role. ROS assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permission to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS does not use the role previously associated with the stack. If you want to use a role, you must specify it in this parameter. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=DeleteStack &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteStackResponse>
      <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</DeleteStackResponse>
```

`JSON` format `{`

```json
  "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidOperation.Deletio nProtection | Fail to delete stack {ID}, as deletion protection is enabled. | The error message returned because deletion protection prevented the stack from being deleted. ID indicates the stack ID. |
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |

#### ListStacks

You can call this operation to query the list of stacks. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListStacks | The operation that you want to perform. Set the value to ListStacks. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Status.N | RepeatLi st | No | CREATE COMPLET _ E | The state of stack N. Valid values: CREATE IN PROGRESS _ _ CREATE FAILED _ CREATE COMPLETE _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CREATE ROLLBACK IN PROGRESS _ _ _ CREATE ROLLBACK FAILED _ _ CREATE ROLLBACK COMPLETE _ _ ROLLBACK IN PROGRESS _ _ ROLLBACK FAILED _ ROLLBACK COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ REVIEW IN PROGRESS _ _ IMPORT CREATE IN PROGRESS _ _ _ IMPORT CREATE FAILED _ _ IMPORT CREATE COMPLETE _ _ IMPORT CREATE ROLLBACK IN PROGR _ _ _ _ ESS IMPORT CREATE ROLLBACK FAILED _ _ _ IMPORT CREATE ROLLBACK COMPLET _ _ _ E IMPORT UPDATE IN PROGRESS _ _ _ IMPORT UPDATE FAILED _ _ IMPORT UPDATE COMPLETE _ _ IMPORT UPDATE ROLLBACK IN PROG _ _ _ _ RESS IMPORT UPDATE ROLLBACK FAILED _ _ _ IMPORT UPDATE ROLLBACK COMPLET _ _ _ E Valid values of N: 1 to 5. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Long | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| ParentStackId | String | No | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the parent stack. |
| StackName.N | RepeatLi st | No | MyStack | The name of stack N. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a digit or letter. _ Fuzzy search with the asterisk (*) is supported. Valid values of N: 1 to 5. |
| PageNumber | Long | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| ShowNestedStac k | Boolean | No | true | Specifies whether to display nested stacks. Default value: false. Valid values: true false Not e This parameter is set to true if the ParentStackId parameter is specified. |
| Tag.N.Key | String | No | usage | The key of tag N of the stack. Valid values of N: 1 to 20. |
| Tag.N.Value | String | No | test | The value of tag N of the stack. Valid values of N: 1 to 20. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StackId | String | No | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. If detailed information about the stack is not required, you can use this parameter to replace the GetStack operation. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Stacks | Array of Stack |   | The list of stacks. |
| CreateTime | String | 2019-08- 01T04:07:39 | The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
| DisableRollback | Boolean | false | Indicates whether rollback is disabled on stack creation failure. Default value: false. Valid values: true: disables rollback on stack creation failure. false: enables rollback on stack creation failure. |
| DriftDetectionTi me | String | 2020-02- 27T07:47:47 | The time when the last successful drift detection operation was initiated. |
| ParentStackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf692**** | The ID of the parent stack. |
| RegionId | String | cn-hangzhou | The region ID of the stack. |
| StackDriftStatu s | String | IN SYNC _ | The drift state of the stack in the last successful drift detection. Valid values: DRIFTED: The stack has drifted. NOT CHECKED: No drift detection has _ been completed on the stack. IN SYNC: The stack is being synchronized. _ |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| Developer Guide·AP | I Reference |   | Resource Orchestration Servic |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| StackName | String | MyStack | The name of the stack. |
| StackType | String | ROS | The type of the stack. Set the value to ROS, indicating that the stack was created based on an ROS template. |
| Status | String | CREATE COMPLETE _ | The state of the stack. Valid values: CREATE IN PROGRESS _ _ CREATE FAILED _ CREATE COMPLETE _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CREATE ROLLBACK IN PROGRESS _ _ _ CREATE ROLLBACK FAILED _ _ CREATE ROLLBACK COMPLETE _ _ ROLLBACK IN PROGRESS _ _ ROLLBACK FAILED _ ROLLBACK COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ REVIEW IN PROGRESS _ _ IMPORT CREATE IN PROGRESS _ _ _ IMPORT CREATE FAILED _ _ IMPORT CREATE COMPLETE _ _ IMPORT CREATE ROLLBACK IN PROGRESS _ _ _ _ IMPORT CREATE ROLLBACK FAILED _ _ _ IMPORT CREATE ROLLBACK COMPLETE _ _ _ IMPORT UPDATE IN PROGRESS _ _ _ IMPORT UPDATE FAILED _ _ IMPORT UPDATE COMPLETE _ _ IMPORT UPDATE ROLLBACK IN PROGRESS _ _ _ _ IMPORT UPDATE ROLLBACK FAILED _ _ _ IMPORT UPDATE ROLLBACK COMPLETE _ _ _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StatusReason | String | Stack successfully created | The reason why the stack is in its current state. |
| TimeoutInMinut es | Integer | 10 | The timeout period that is specified for the stack creation request. Unit: minutes. |
| UpdateTime | String | 2019-08- 01T04:07:39 | The time when the stack was last updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
| PageSize | Integer | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| TotalCount | Integer | 1 | The total number of stacks. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ListStacks &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListStacksResponse>
    <Stacks>
        <Stack>
            <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
            <ParentStackId>4a6c9851-3b0f-4f5f-b4ca-a14bf692****</ParentStackId>
            <StackName>StackName</StackName>
            <RegionId>cn-hangzhou</RegionId>
            <DisableRollback>false</DisableRollback>
            <CreateTime>2019-08-01T04:07:39</CreationTime>
            <Status>CREATE_COMPLETE</Status>
            <StatusReason>Stack successfully created</StatusReason>
            <TimeoutInMinutes>10</TimeoutInMinutes>
            <UpdatedTime>2019-08-01T04:07:39</UpdatedTime>
            <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
            <StackDriftStatus>IN_SYNC</StackDriftStatus>
            <StackType>ROS</StackType>
        </Stack>
    </Stacks>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TotalCount>1</TotalCount>
    <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</ListStacksResponse>
```

`JSON` format `{`

```json
    "Stacks": [
```

`{`

```json
            "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****",
            "ParentStackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf692****",
            "StackName": "MyStack",
            "RegionId": "cn-hangzhou",
            "DisableRollback": false,
            "CreateTime": "2019-08-01T04:07:39",
            "Status": "CREATE_COMPLETE",
            "StatusReason": "Stack successfully created",
            "TimeoutInMinutes": 10,
            "UpdatedTime": "2019-08-01T04:07:39",
            "DriftDetectionTime": "2020-02-27T07:47:47",
      "StackDriftStatus": "IN_SYNC",
            "StackType": "ROS"
```

`}` `],`

```json
    "PageNumber": 1,
    "PageSize": 10,
    "TotalCount": 1,
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

#### PreviewStack

You can call this operation to preview the stack to be created by using a specified template. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PreviewStack | The operation that you want to perform. Set the value to PreviewStack. |
| Parameters.N.Par ameterKey | String | Yes | InstanceType | The key of parameter N. If the key and value of the parameter are not specified, the key and value in the template are used. Maximum value of N: 200. Not e Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.ParameterKe y and Parameters.N.ParameterVa lue. |
| Parameters.N.Par ameterValue | String | Yes | ecs.cm4.6xlarge | The value of parameter N. Maximum value of N: 200. Not e Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.ParameterKe y and Parameters.N.ParameterVa lue. |
| RegionId | String | Yes | cn-beijing | The region ID of the stack. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StackName | String | Yes | MyStack | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a digit or letter. _ |
| DisableRollback | Boolean | No | false | Specifies whether to disable rollback on stack creation failure. Default value: false. Valid values: true: disables rollback on stack creation failure. false: enables rollback on stack creation failure. |
| TimeoutInMinutes | Long | No | 10 | The timeout period that is specified for the stack creation request. Unit: minutes. Default value: 60. |
| TemplateBody | String | No | {"ROSTemplateFo rmatVersion": "2015-09-01" } | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StackPolicyURL | String | No | oss://ros-stack- policy/demo | The URL of the file that contains the stack policy. The URL must point to a policy located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/stack- policy/demo and oss://ros/stack- policy/demo?RegionId=cn-hangzhou. The policy can be up to 16,384 bytes in length and the URL can be up to 1,350 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |
| StackPolicyBody | String | No | {"Statement": [{"Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*"}]} | The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length. Not e You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateURL | String | No | oss://ros- template/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template must be 1 to 524,288 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |
| Stack | Struct |   | Details about the stack. |
| Description | String | One ECS instance. | The description of the stack. |
| DisableRollback | Boolean | false | Indicates whether rollback is disabled. |
| Parameters | Array of Parameter |   | The parameters of the stack. |
| ParameterKey | String | SystemDiskCategory | The key of the parameter. |
| ParameterValu e | String | cloud ssd _ | The value of the parameter. |
| RegionId | String | cn-beijing | The region ID of the stack. |
| Resources | Array of Resource |   | The list of resources in the stack. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | ECS instance. | The description of the resource. |
| LogicalResourc eId | String | WebServer | The logical resource ID. |
| Properties | Map | { "DiskMappings": [ { "Category": "cloud ssd", "Size": _ "20" } ], "SystemDisk Catego _ ry": "cloud ssd", _ "InstanceChargeTyp e": "PostPaid", "AutoRenew": "False", "WillReplace": true, "ImageId": "centos 7", _ "InstanceType": "ecs.g6.large", "AllocatePublicIP": true, "AutoRenewPeriod": 1, "IoOptimized": "optimized", "ZoneId": "cn- beijing-g", "VSwitchId": "", "SecurityGroupId": "", "Period": 1, "InternetChargeType ": "PayByTraffic", "SystemDiskCategor y": "cloud efficiency", _ "InternetMaxBandwi dthOut": 1, "VpcId": "", "InternetMaxBandwi dthIn": 200, "PeriodUnit": "Month" } | The properties of the resource. |
| RequiredBy | List | ["Resource1", "Resource2"] | The list of one or more resources that are dependent on the stack. |
| ResourceType | String | ALIYUN::ECS::Instan ce | The type of the resource. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Stack | Map | {} | Details about the nested stacks. The data structure of this parameter is the same as that of the entire responses. |
| StackName | String | MyStack | The name of the stack. |
| StackPolicyBod y | Map | { "Statement": [ { "Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*" }, { "Action": "Update:*", "Resource": "LogicalResourceId/ apple1", "Effect": "Deny", "Principal": "*" } ] } | The stack policy. |
| TemplateDescri ption | String | One ECS instance. | The description of the template. |
| TimeoutInMinut es | Integer | 10 | The timeout period. Unit: minutes. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=PreviewStack &RegionId=cn-beijing &Parameters.1.ParameterValue=ecs.cm4.6xlarge &Parameters.1.ParameterKey=InstanceType &StackName=MyStack &TimeoutInMinutes=10 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PreviewStackResponse>
          <Stack>
                <Description>No description</Description>
                <DisableRollback>true</DisableRollback>
                <Parameters>
                      <ParameterKey>UpdateVersion</ParameterKey>
                      <ParameterValue>1</ParameterValue>
```

`/`

```xml
                </Parameters>
                <RegionId>cn-beijing</RegionId>
                <Resources>
                      <Description></Description>
                      <LogicalResourceId>WaitConditionHandle</LogicalResourceId>
                      <Properties>
                            <Count>-1</Count>
                            <Mode>Full</Mode>
                            <UpdateVersion>1</UpdateVersion>
                      </Properties>
                      <ResourceType>ALIYUN::ROS::WaitConditionHandle</ResourceType>
                </Resources>
                <Resources>
                      <Description></Description>
                      <LogicalResourceId>nested</LogicalResourceId>
                      <Properties>
                            <Parameters></Parameters>
                            <TemplateURL>oss://nested-stack/test/demo</TemplateURL>
                            <TimeoutMins>16</TimeoutMins>
                      </Properties>
                      <ResourceType>ALIYUN::ROS::Stack</ResourceType>
                      <Stack>
                            <Description>No description</Description>
                            <DisableRollback>true</DisableRollback>
                            <Parameters>
                                  <ParameterKey>ALIYUN::AccountId</ParameterKey>
                                  <ParameterValue>1666666****</ParameterValue>
                            </Parameters>
                            <Parameters>
                                  <ParameterKey>ALIYUN::NoValue</ParameterKey>
                                  <ParameterValue>None</ParameterValue>
                            </Parameters>
                            <Parameters>
                                  <ParameterKey>ALIYUN::Region</ParameterKey>
                                  <ParameterValue>cn-beijing</ParameterValue>
                            </Parameters>
                            <Parameters>
                                  <ParameterKey>ALIYUN::StackId</ParameterKey>
                                  <ParameterValue>None</ParameterValue>
                            </Parameters>
                            <Parameters>
                                  <ParameterKey>ALIYUN::StackName</ParameterKey>
                                  <ParameterValue>test-preview-stack-complex-nested</Parame
terValue>
                            </Parameters>
                            <RegionId>cn-beijing</RegionId>
                            <Resources>
                                  <Description></Description>
                                  <LogicalResourceId>WaitConditionHandle</LogicalResourceId
```

`>`

```xml
                                  <Properties>
                                        <Count>-1</Count>
                                        <Mode>Full</Mode>
                                        <UpdateVersion>1</UpdateVersion>
</Properties>
```

```xml
                                  </Properties>
                                  <ResourceType>ALIYUN::ROS::WaitConditionHandle</ResourceT
ype>
                            </Resources>
                            <StackName>test-preview-stack-complex-nested</StackName>
                            <StackPolicyBody>
                                  <Statement>
                                        <Action>Update:*</Action>
                                        <Effect>Allow</Effect>
                                        <Principal>*</Principal>
                                        <Resource>*</Resource>
                                  </Statement>
                                  <Statement>
                                        <Action>Update:*</Action>
                                        <Effect>Deny</Effect>
                                        <Principal>*</Principal>
                                        <Resource>LogicalResourceId/apple1</Resource>
                                  </Statement>
                            </StackPolicyBody>
                            <TemplateDescription>No description</TemplateDescription>
                            <TimeoutInMinutes>12</TimeoutInMinutes>
                      </Stack>
                </Resources>
                <StackName>test-preview-stack-complex</StackName>
                <StackPolicyBody>
                      <Statement>
                            <Action>Update:*</Action>
                            <Effect>Allow</Effect>
                            <Principal>*</Principal>
                            <Resource>*</Resource>
                      </Statement>
                      <Statement>
                            <Action>Update:*</Action>
                            <Effect>Deny</Effect>
                            <Principal>*</Principal>
                            <Resource>LogicalResourceId/apple1</Resource>
                      </Statement>
                </StackPolicyBody>
                <TemplateDescription>No description</TemplateDescription>
                <TimeoutInMinutes>10</TimeoutInMinutes>
          </Stack>
          <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</PreviewStackResponse>
```

`JSON` format `{`

```json
    "Stack": {
        "Description": "No description",
        "DisableRollback": true,
        "Parameters": [
```

`{`

```json
                "ParameterKey": "UpdateVersion",
                "ParameterValue": "1"
```

`}` `],`

```json
        "RegionId": "cn-beijing",
        "Resources": [
```

`{`

```json
                "Description": "",
                "LogicalResourceId": "WaitConditionHandle",
                "Properties": {
                    "Count": -1,
                    "Mode": "Full",
                    "UpdateVersion": 1
```

`},`

```json
                "RequiredBy": [],
                "ResourceType": "ALIYUN::ROS::WaitConditionHandle"
```

`},` `{`

```json
                "Description": "",
                "LogicalResourceId": "nested",
                "Properties": {
                    "Parameters": null,
                    "TemplateURL": "oss://nested-stack/test/demo",
                    "TimeoutMins": 16
```

`},`

```json
                "RequiredBy": [],
                "ResourceType": "ALIYUN::ROS::Stack",
                "Stack": {
                    "Description": "No description",
                    "DisableRollback": true,
                    "Parameters": [
```

`{`

```json
                            "ParameterKey": "ALIYUN::AccountId",
                            "ParameterValue": "1666666****"
```

`},` `{`

```json
                            "ParameterKey": "ALIYUN::NoValue",
                            "ParameterValue": "None"
```

`},` `{`

```json
                            "ParameterKey": "ALIYUN::Region",
                            "ParameterValue": "cn-beijing"
```

`},` `{`

```json
                            "ParameterKey": "ALIYUN::StackId",
                            "ParameterValue": "None"
```

`},` `{`

```json
                            "ParameterKey": "ALIYUN::StackName",
                            "ParameterValue": "test-preview-stack-complex-nested"
```

`}` `],`

```json
                    "RegionId": "cn-beijing",
                    "Resources": [
```

`{`

```json
                            "Description": "",
```

```json
                            "LogicalResourceId": "WaitConditionHandle",
                            "Properties": {
                                "Count": -1,
                                "Mode": "Full",
                                "UpdateVersion": 1
```

`},`

```json
                            "RequiredBy": [],
                            "ResourceType": "ALIYUN::ROS::WaitConditionHandle"
```

`}` `],`

```json
                    "StackName": "test-preview-stack-complex-nested",
                    "StackPolicyBody": {
                        "Statement": [
```

`{`

```json
                                "Action": "Update:*",
                                "Effect": "Allow",
                                "Principal": "*",
                                "Resource": "*"
```

`},` `{`

```json
                                "Action": "Update:*",
                                "Effect": "Deny",
                                "Principal": "*",
                                "Resource": "LogicalResourceId/apple1"
```

`}` `]` `},`

```json
                    "TemplateDescription": "No description",
                    "TimeoutInMinutes": 12
```

`}` `}` `],`

```json
        "StackName": "test-preview-stack-complex",
        "StackPolicyBody": {
            "Statement": [
```

`{`

```json
                    "Action": "Update:*",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Resource": "*"
```

`},` `{`

```json
                    "Action": "Update:*",
                    "Effect": "Deny",
                    "Principal": "*",
                    "Resource": "LogicalResourceId/apple1"
```

`}` `]` `},`

```json
        "TemplateDescription": "No description",
        "TimeoutInMinutes": 10
```

`},`

```json
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | CircularDependency | Circular Dependency Found: {reason}. | The error message returned because the template contains a circular dependency. reason indicates the specific reason. |
| 400 | InvalidSchema | {reason}. | The error message returned because the specified template format is invalid. reason indicates the specific reason. |
| 400 | InvalidTemplateAttribut e | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is incorrect. resource indicates the resource name, and name indicates the attribute name. |
| 400 | InvalidTemplatePropert yType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is incorrect. resource indicates the resource name, and section indicates the section name. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidTemplateReferen ce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| 400 | InvalidTemplateSection | The template section is invalid: {section}. | The error message returned because the template contains an invalid property. section indicates the section name. |
| 400 | InvalidTemplateVersion | The template version is invalid: {reason}. | The error message returned because the template version is incorrect. reason indicates the specific reason. |
| 400 | StackValidationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |
| 400 | UnknownUserParameter | The Parameter ({name}) was not defined in template. | The error message returned because the specified parameter is not defined in the template. name indicates the parameter key. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | UserParameterMissing | The Parameter {name} was not provided. | The error message returned because no value is passed into the specified parameter defined in the template. name indicates the parameter key. |
| 409 | StackExists | The Stack ({name}) already exists. | The error message returned because a stack with the same name already exists. name indicates the stack name. |

#### ListStackEvents

You can call this operation to query stacks and their resource events. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListStackEvents | The operation that you want to perform. Set the value to ListStackEvents. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Status.N | RepeatLi st | No | CREATE IN PROGR _ _ ESS | The state of resource N. Valid values: CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ UPDATE SKIPPED _ DELETE IN PROGRESS _ _ DELETE FAILED _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ IMPORT IN PROGRESS _ _ IMPORT FAILED _ IMPORT COMPLETE _ |
| ResourceType.N | RepeatLi st | No | ALIYUN::ECS::Inst ance | The type of resource N. Maximum value of N: 200. |
| LogicalResourceId .N | RepeatLi st | No | WebServer | The logical ID of the resource as defined in the template. |
| PageNumber | Long | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Long | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Events | Array of Event |   | The list of events. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | String | 2019-08- 01T04:07:39 | The time when the task was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
| EventId | String | 0086612d-77cf- 4056-b0b5- ff8e94ad**** | The ID of the event. |
| LogicalResourc eId | String | WebServer | The logical ID of the resource as defined in the template. |
| PhysicalResourc eId | String | i- m5e3tfdbinchnexh** ** | The physical ID of the resource. |
| ResourceType | String | ALIYUN::ECS::Instan ce | The type of the resource. |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| StackName | String | StackName | The name of the stack. |
| Status | String | CREATE COMPLETE _ | The state of the resource. |
| StatusReason | String | state changed | The reason why the resource is in its current state. |
| PageNumber | Integer | 1 | The page number of the returned page. Pages start from page 1. Default value: 1. |
| PageSize | Integer | 10 | The number of entries returned per page. Maximum value: 50. Default value: 10. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| TotalCount | Integer | 20 | The total number of returned events. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ListStackEvents &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListStackEventsResponse>
       <Events class="array">
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:56</CreationTime>
                     <EventId type="string">0086612d-77cf-4056-b0b5-ff8e94ad****</EventId>
                     <LogicalResourceId type="string">test-describe-events</LogicalResource
Id>
                     <PhysicalResourceId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****
</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">Stack successfully updated</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:55</CreationTime>
                     <EventId type="string">2b900d01-959b-49a8-8cfe-f7de87aa****</EventId>
                     <LogicalResourceId type="string">dummy</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:55</CreationTime>
                     <EventId type="string">30f721d4-8124-4fd4-8afd-7b21471f****</EventId>
                     <LogicalResourceId type="string">dummy3</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">CREATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:54</CreationTime>
                     <EventId type="string">b5ecc0ac-f855-4503-945c-82d398a2****</EventId>
                     <LogicalResourceId type="string">WaitConditionHandle</LogicalResourceI
```

`d>` `d>`

```
                     <ResourceType type="string">ALIYUN::ROS::WaitConditionHandle</Resource
Type>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">a01e5730-7244-414e-b9ff-f97e3885****</EventId>
                     <LogicalResourceId type="string">dummy3</LogicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">CREATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">262b2f54-7ae7-4cf6-9c8a-eb4d0801****</EventId>
                     <LogicalResourceId type="string">dummy</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">163c3965-1617-4787-ba08-1eed0e3a****</EventId>
                     <LogicalResourceId type="string">nested</LogicalResourceId>
                     <PhysicalResourceId type="string">4ed7ab13-c912-4239-b064-8cea7caa****
</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">71f7c25c-2ac7-4336-9934-85482111****</EventId>
                     <LogicalResourceId type="string">nested</LogicalResourceId>
                     <PhysicalResourceId type="string">4ed7ab13-c912-4239-b064-8cea7caa****
</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
<CreationTimetype="string">2019-08-01T05:57:53</CreationTime>
```

```
                     <CreationTime type=string>20190801T05:57:53</CreationTime>
                     <EventId type="string">a5a0eb9e-7abe-44a1-a376-70955211****</EventId>
                     <LogicalResourceId type="string">WaitConditionHandle</LogicalResourceI
```

`d>`

```
                     <ResourceType type="string">ALIYUN::ROS::WaitConditionHandle</Resource
Type>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">250f5003-f59d-46f9-8471-65d0c630****</EventId>
                     <LogicalResourceId type="string">test-describe-events</LogicalResource
Id>
                     <PhysicalResourceId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****
</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackId>
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">Stack UPDATE started</StatusReason>
              </Event>
       </Events>
       <PageNumber type="number">1</PageNumber>
       <PageSize type="number">10</PageSize>
       <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
       <TotalCount type="number">20</TotalCount>
</ListStackEventsResponse>
```

`JSON` format `{`

```json
   "Events": [
```

`{`

```json
           "CreationTime": "2019-08-01T05:57:56",
           "EventId": "0086612d-77cf-4056-b0b5-ff8e94ad****",
           "LogicalResourceId": "test-describe-events",
           "PhysicalResourceId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "Stack successfully updated"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:55",
           "EventId": "2b900d01-959b-49a8-8cfe-f7de87aa****",
           "LogicalResourceId": "dummy",
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
```

```json
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:55",
           "EventId": "30f721d4-8124-4fd4-8afd-7b21471f****",
           "LogicalResourceId": "dummy3",
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "CREATE_COMPLETE",
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:54",
           "EventId": "b5ecc0ac-f855-4503-945c-82d398a2****",
           "LogicalResourceId": "WaitConditionHandle",
           "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "a01e5730-7244-414e-b9ff-f97e3885****",
           "LogicalResourceId": "dummy3",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "CREATE_IN_PROGRESS",
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "262b2f54-7ae7-4cf6-9c8a-eb4d0801****",
           "LogicalResourceId": "dummy",
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_IN_PROGRESS",
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "163c3965-1617-4787-ba08-1eed0e3a****",
           "LogicalResourceId": "nested",
           "PhysicalResourceId": "4ed7ab13-c912-4239-b064-8cea7caa****",
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_COMPLETE",
"Stt
```

`R` `"`

```
"tt
```

`h` `d"`

```json
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "71f7c25c-2ac7-4336-9934-85482111****",
           "LogicalResourceId": "nested",
           "PhysicalResourceId": "4ed7ab13-c912-4239-b064-8cea7caa****",
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_IN_PROGRESS",
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "a5a0eb9e-7abe-44a1-a376-70955211****",
           "LogicalResourceId": "WaitConditionHandle",
           "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_IN_PROGRESS",
           "StatusReason": "state changed"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "250f5003-f59d-46f9-8471-65d0c630****",
           "LogicalResourceId": "test-describe-events",
           "PhysicalResourceId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_IN_PROGRESS",
           "StatusReason": "Stack UPDATE started"
```

`}` `],`

```json
   "PageNumber": 1,
   "PageSize": 10,
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "TotalCount": 20
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

### Resource operations

#### GetResourceTypeTemplate

You can call this operation to query the template of a resource by resource type. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetResourceType Template | The operation that you want to perform. Set the value to GetResourceTypeTemplate. |
| ResourceType | String | Yes | ALIYUN::ECS::VP C | The type of the resource. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 87F54B2B-AEF0- 4C33-A72A- 3F8856A575E9 | The ID of the request. |
| TemplateBody | Map | {"ROSTemplateForm atVersion": "2015- 09-01"} | The structure that contains the template body. The template body must be 1 to 51,200 bytes in length. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetResourceTypeTemplate &ResourceType=ALIYUN::ECS::VPC &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetResourceTypeTemplateResponse>
       <RequestId type="string">87F54B2B-AEF0-4C33-A72A-3F8856A575E9</RequestId>
       <TemplateBody class="object">
              <Parameters class="object">
                     <CidrBlock class="object">
                            <Type type="string">String</Type>
                     </CidrBlock>
                     <Description class="object">
                            <Type type="string">String</Type>
                     </Description>
                     <ResourceGroupId class="object">
                            <Type type="string">String</Type>
                     </ResourceGroupId>
                     <VpcName class="object">
                            <Type type="string">String</Type>
                     </VpcName>
              </Parameters>
              <ROSTemplateFormatVersion type="string">2015-09-01</ROSTemplateFormatVersion>
              <Resources class="object">
                     <Vpc class="object">
                            <Properties class="object">
                                   <CidrBlock class="object">
                                          <Ref type="string">CidrBlock</Ref>
                                   </CidrBlock>
                                   <Description class="object">
                                          <Ref type="string">Description</Ref>
                                   </Description>
                                   <ResourceGroupId class="object">
                                          <Ref type="string">ResourceGroupId</Ref>
                                   </ResourceGroupId>
                                   <VpcName class="object">
                                          <Ref type="string">VpcName</Ref>
                                   </VpcName>
                            </Properties>
                            <Type type="string">ALIYUN::ECS::VPC</Type>
                     </Vpc>
              </Resources>
       </TemplateBody>
</GetResourceTypeTemplateResponse>
```

`JSON` format `{`

```json
  "RequestId": "87F54B2B-AEF0-4C33-A72A-3F8856A575E9",
  "TemplateBody": {
    "Parameters": {
      "CidrBlock": {
        "Type": "String"
```

`},`

```json
      "Description": {
        "Type": "String"
```

`},`

```json
      "ResourceGroupId": {
        "Type": "String"
```

`},`

```json
      "VpcName": {
        "Type": "String"
```

`}` `},`

```json
    "ROSTemplateFormatVersion": "2015-09-01",
    "Resources": {
      "Vpc": {
        "Properties": {
          "CidrBlock": {
            "Ref": "CidrBlock"
```

`},`

```json
          "Description": {
            "Ref": "Description"
```

`},`

```json
          "ResourceGroupId": {
            "Ref": "ResourceGroupId"
```

`},`

```json
          "VpcName": {
            "Ref": "VpcName"
```

`}` `},`

```json
        "Type": "ALIYUN::ECS::VPC"
```

`}` `}` `}` `}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | ResourceTypeNotFound | The Resource Type ({name}) could not be found. | The error message returned because the specified resource type does not exist. name indicates the name of the resource type. |

#### ListStackResources

You can call this operation to query the resource list of a specific stack. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListStackResourc es | The operation that you want to perform. Set the value to ListStackResources. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| Resources | Array of Resource |   | The list of resources. |
| CreateTime | String | 2019-08- 01T06:01:23 | The time when the resource was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| DriftDetectionTi me | String | 2020-02- 27T07:47:47 | The time when the last successful drift detection operation was initiated. |
| LogicalResourc eId | String | dummy | The logical resource ID defined in the template. |
| PhysicalResourc eId | String | d04af923-e6b7- 4272-aeaa- 47ec9777**** | The physical ID of the resource. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ResourceDriftSt atus | String | IN SYNC _ | The drift state of the resource in the last successful drift detection. Valid values: DELETED: The actual configuration of the resource differs from its expected template configuration because the resource has been deleted. MODIFIED: The actual configuration of the resource differs from its expected template configuration. NOT CHECKED: ROS has not checked _ whether the actual configuration of the resource differs from its expected template configuration. IN SYNC: The actual configuration of the _ resource matches its expected template configuration. |
| ResourceType | String | ALIYUN::ROS::Stack | The type of the resource. |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| StackName | String | test-describe- resource | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must _ start with a digit or letter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | UPDATE COMPLETE _ | The state of the resource. Valid values: CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ IMPORT IN PROGRESS _ _ IMPORT FAILED _ IMPORT COMPLETE _ |
| StatusReason | String | state changed | The reason why the resource is in its current state. |
| UpdateTime | String | 2019-08- 01T06:01:29 | The time when the resource was last updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ListStackResources &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListStackResourcesResponse>
       <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
       <Resources class="array">
              <Resource class="object">
                     <CreationTime type="string">2019-08-01T06:01:23</CreationTime>
                     <LogicalResourceId type="string">dummy</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
<ResourceTypetype="string">ALIYUN::DEBUG::Dummy</ResourceType>
```

```xml
                     <ResourceType type=string>ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackId>
                     <StackName type="string">test-describe-resource</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
                     <UpdatedTime type="string">2019-08-01T06:01:29</UpdatedTime>
                     <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
                     <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
              </Resource>
              <Resource class="object">
                     <CreationTime type="string">2019-08-01T06:01:28</CreationTime>
                     <LogicalResourceId type="string">dummy3</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackId>
                     <StackName type="string">test-describe-resource</StackName>
                     <Status type="string">CREATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
                     <UpdatedTime type="string">2019-08-01T06:01:29</UpdatedTime>
                     <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
                     <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
              </Resource>
              <Resource class="object">
                     <CreationTime type="string">2019-08-01T06:01:23</CreationTime>
                     <LogicalResourceId type="string">WaitConditionHandle</LogicalResourceI
```

`d>`

```xml
                     <PhysicalResourceId type="string"></PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::WaitConditionHandle</Resource
Type>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackId>
                     <StackName type="string">test-describe-resource</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
                     <UpdatedTime type="string">2019-08-01T06:01:29</UpdatedTime>
                     <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
                     <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
              </Resource>
              <Resource class="object">
                     <CreationTime type="string">2019-08-01T06:01:23</CreationTime>
                     <LogicalResourceId type="string">nested</LogicalResourceId>
                     <PhysicalResourceId type="string">d04af923-e6b7-4272-aeaa-47ec9777****
</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackId>
                     <StackName type="string">test-describe-resource</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
                     <UpdatedTime type="string">2019-08-01T06:01:28</UpdatedTime>
                     <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
                     <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
              </Resource>
       </Resources>
</ListStackResourcesResponse>
```

`JSON` format `{`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "Resources": [
```

`{`

```json
           "CreationTime": "2019-08-01T06:01:23",
           "LogicalResourceId": "dummy",
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2****",
           "StackName": "test-describe-resource",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed",
           "UpdatedTime": "2019-08-01T06:01:29",
           "DriftDetectionTime": "2020-02-27T07:47:47",
        "ResourceDriftStatus": "IN_SYNC"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T06:01:28",
           "LogicalResourceId": "dummy3",
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2****",
           "StackName": "test-describe-resource",
           "Status": "CREATE_COMPLETE",
           "StatusReason": "state changed",
           "UpdatedTime": "2019-08-01T06:01:29",
           "DriftDetectionTime": "2020-02-27T07:47:47",
        "ResourceDriftStatus": "IN_SYNC"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T06:01:23",
           "LogicalResourceId": "WaitConditionHandle",
           "PhysicalResourceId": "",
           "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
           "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2****",
           "StackName": "test-describe-resource",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed",
           "UpdatedTime": "2019-08-01T06:01:29",
           "DriftDetectionTime": "2020-02-27T07:47:47",
        "ResourceDriftStatus": "IN_SYNC"
```

`},` `{`

```json
           "CreationTime": "2019-08-01T06:01:23",
           "LogicalResourceId": "nested",
           "PhysicalResourceId": "d04af923-e6b7-4272-aeaa-47ec9777****",
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2e0d5",
           "StackName": "test-describe-resource",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed",
           "UpdatedTime": "2019-08-01T06:01:28",
```

```json
           "DriftDetectionTime": "2020-02-27T07:47:47",
        "ResourceDriftStatus": "IN_SYNC"
```

`}` `]` `}`

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| StackNotFound | The Stack ({name}) could not be found. | 404 | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

#### GetStackResource

You can call this operation to query information about a resource in a specific stack. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetStackResourc e | The operation that you want to perform. Set the value to GetStackResource. |
| LogicalResourceId | String | Yes | WebServer | The logical ID of the resource as defined in the template. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ShowResourceAtt ributes | Boolean | No | true | Specifies whether to query resource attributes. Valid values: true false |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | CREATE COMPLETE _ | The state of the resource. Valid values: CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ IMPORT IN PROGRESS _ _ IMPORT FAILED _ IMPORT COMPLETE _ |
| Description | String | no description | The description of the resource. |
| LogicalResourc eId | String | WebServer | The logical ID of the resource as defined in the template. |
| StackId | String | efdf5c10-96a5- 4fd7-ab89- 68e7baa2**** | The ID of the stack. |
| StackName | String | test-describe- resource | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must _ start with a digit or letter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StatusReason | String | state changed | The reason why the resource is in its current state. |
| PhysicalResourc eId | String | d04af923-e6b7- 4272-aeaa- 47ec9777**** | The physical ID of the resource. |
| ResourceType | String | ALIYUN::ROS::WaitC onditionHandle | The type of the resource. |
| CreateTime | String | 2019-08- 01T06:01:23 | The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
| Metadata | Map | {"key": "value"} | The metadata. |
| UpdateTime | String | 2019-08- 01T06:01:29 | The time when the stack was last updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ResourceAttrib utes | List | [ { "ResourceAttributeV alue":"curl -Uri \"http://100.100.XX .XX/waitcondition? stackname=test- describe- resource&stackid=ef df5c10-96a5-4fd7- ab89- 68e7baa2****&resou rce=WaitConditionH andle&expire=15646 8****&signature=991 d910a901a89db658 0d74233119960c004 ****\" -Method Post -Headers @{\"Content- Type\"=\"applicatio n/json\"; \"Accept\"=\"applic ation/json\"; \"x- acs-region- id\"=\"cn- beijing\"}", "ResourceAttributeK ey":"PowerShellCurl Cli" } ] | The list of resource attributes. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| DriftDetectionTi me | String | 2020-02- 27T07:47:47 | The time when the last successful drift detection operation was initiated. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ResourceDriftSt atus | String | IN SYNC _ | The drift state of the resource in the last successful drift detection. Valid values: DELETED: The actual configuration of the resource differs from its expected template configuration because the resource had been deleted. MODIFIED: The actual configuration of the resource differs from its expected template configuration. NOT CHECKED: ROS has not checked _ whether the actual configuration of the resource differs from its expected template configuration. IN SYNC: The actual configuration of the _ resource matches its expected template configuration. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetStackResource &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &LogicalResourceId=WebServer &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetStackResourceResponse>
          <CreateTime>2019-08-01T06:01:23</CreateTime>
          <Description></Description>
          <LogicalResourceId>WaitConditionHandle</LogicalResourceId>
          <Metadata></Metadata>
          <PhysicalResourceId></PhysicalResourceId>
          <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
          <ResourceAttributes>
                <ResourceAttributeKey>CurlCli</ResourceAttributeKey>
                <ResourceAttributeValue>curl -i -X POST -H 'Content-Type: application/json'
-H 'Accept: application/json' -H 'x-acs-region-id: cn-beijing' http://100.100.XX.XX/waitcon dition?stackname=test-describe-resource\&amp;stackid=efdf5c10-96a5-4fd7-ab89-68e7baa2****\& amp;resource=WaitConditionHandle\&amp;expire=156468****\&amp;signature=991d910a901a89db6580 d74233119960c004****</ResourceAttributeValue>
          </ResourceAttributes>
          <ResourceAttributes>
                <ResourceAttributeKey>WindowsCurlCli</ResourceAttributeKey>
                <ResourceAttributeValue>curl -i -X POST -H "Content-Type: application/json"
-H "Accept: application/json" -H "x-acs-region-id: cn-beijing" "http://100.100.XX.XX/waitco ndition?stackname=test-describe-resource&amp;stackid=efdf5c10-96a5-4fd7-ab89-68e7baa2****&a mp;resource=WaitConditionHandle&amp;expire=156468****&amp;signature=991d910a901a89db6580d74 233119960c004****"</ResourceAttributeValue>
          </ResourceAttributes>
          <ResourceAttributes>
                <ResourceAttributeKey>PowerShellCurlCli</ResourceAttributeKey>
                <ResourceAttributeValue>curl -Uri "http://100.100.XX.XX/waitcondition?stack
name=test-describe-resource&amp;stackid=efdf5c10-96a5-4fd7-ab89-68e7baa2****&amp;resource=W aitConditionHandle&amp;expire=156468****&amp;signature=991d910a901a89db6580d74233119960c004
****" -Method Post -Headers @{"Content-Type"="application/json"; "Accept"="application/json
"; "x-acs-region-id"="cn-beijing"}</ResourceAttributeValue>
          </ResourceAttributes>
          <ResourceType>ALIYUN::ROS::WaitConditionHandle</ResourceType>
          <StackId>efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackId>
          <StackName>test-describe-resource</StackName>
          <Status>UPDATE_COMPLETE</Status>
          <StatusReason>state changed</StatusReason>
          <UpdateTime>2019-08-01T06:01:29</UpdateTime>
          <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
          <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
</GetStackResourceResponse>
```

`JSON` format `{`

```json
    "CreateTime": "2019-08-01T06:01:23",
    "Description": "",
    "LogicalResourceId": "WaitConditionHandle",
    "Metadata": {},
    "PhysicalResourceId": "",
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
    "ResourceAttributes": [
```

`{`

```json
            "ResourceAttributeKey": "CurlCli",
            "ResourceAttributeValue": "curl -i -X POST -H 'Content-Type: application/json'
-H 'Accept: application/json' -H 'x-acs-region-id: cn-beijing' http://100.100.XX.XX/waitcon dition?stackname=test-describe-resource\\&stackid=efdf5c10-96a5-4fd7-ab89-68e7baa2****\\&re source=WaitConditionHandle\\&expire=156468****\\&signature=991d910a901a89db6580d74233119960 c004****"
```

`},` `{`

```json
            "ResourceAttributeKey": "WindowsCurlCli",
            "ResourceAttributeValue": "curl -i -X POST -H \"Content-Type: application/json\
" -H \"Accept: application/json\" -H \"x-acs-region-id: cn-beijing\" \"http://100.100.XX.XX /waitcondition?stackname=test-describe-resource&stackid=efdf5c10-96a5-4fd7-ab89-68e7baa2*** *&resource=WaitConditionHandle&expire=156468****&signature=991d910a901a89db6580d74233119960 c004****\""
```

`},` `{`

```json
            "ResourceAttributeKey": "PowerShellCurlCli",
            "ResourceAttributeValue": "curl -Uri \"http://100.100.XX.XX/waitcondition?stack
name=test-describe-resource&stackid=efdf5c10-96a5-4fd7-ab89-68e7baa2****&resource=WaitCondi tionHandle&expire=156468****&signature=991d910a901a89db6580d74233119960c004****\" -Method P ost -Headers @{\"Content-Type\"=\"application/json\"; \"Accept\"=\"application/json\"; \"xacs-region-id\"=\"cn-beijing\"}"
```

`}` `],`

```json
    "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
    "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2****",
    "StackName": "test-describe-resource",
    "Status": "UPDATE_COMPLETE",
    "StatusReason": "state changed",
    "UpdateTime": "2019-08-01T06:01:29",
    "DriftDetectionTime": "2020-02-27T07:47:47",
    "ResourceDriftStatus": "IN_SYNC"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | The error message returned because the specified resource does not exist in the stack. name indicates the resource name, and stack indicates the name or ID of the stack. |
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

#### GetResourceType

You can call this operation to query details about resource types. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetResourceType | The operation that you want to perform. Set the value to GetResourceType. |
| ResourceType | String | Yes | ALIYUN::ROS::Wa itConditionHandle | The type of the resource. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Attributes | Map | {"CurlCli": {},"PowerShellCurlCli ": {},"WindowsCurlCli": {}} | The attributes of the resource. |
| Properties | Map | {"Count": {},"Mode": {"Constraints": []}} | The properties of the resource. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| ResourceType | String | ALIYUN::ROS::WaitC onditionHandle | The type of the resource. |
| SupportDriftDe tection | Boolean | false | Indicates whether the resource supports drift detection. Valid values: true: The resource supports drift detection. false: The resource does not support drift detection. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetResourceType &ResourceType=ALIYUN::SLB::LoadBalancer &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetResourceTypeResponse>
       <Attributes class="object">
              <CurlCli class="object">
                     <Description type="string">Convenience attribute, provides curl CLI co
mmand prefix, which can be used for signalling handle completion or failure. You can signa l success by adding --data-binary '{"status": "SUCCESS"}' , or signal failure by adding --d ata-binary '{"status": "FAILURE"}'</Description>
              </CurlCli>
              <PowerShellCurlCli class="object">
                     <Description type="string">Convenience attribute, provides curl CLI co
mmand prefix for PowerShell, which can be used for signalling handle completion or failure. As this cmdlet was introduced in PowerShell 3.0, ensure the version of PowerShell satisfies the constraint. (Show the version via $PSVersionTable.PSVersion.) You can signal success by adding -Body '{"status": "SUCCESS"}' , or signal failure by adding -Body '{"status": "FAILU RE"}' </Description>
              </PowerShellCurlCli>
              <WindowsCurlCli class="object">
                     <Description type="string">Convenience attribute, provides curl CLI co
mmand prefix for Windows, which can be used for signalling handle completion or failure. As Windows does not support curl command, you need to install curl.exe and add it to PATH firs t. You can signal success by adding --data-binary "{\"status\": \"SUCCESS\"}" , or signal f ailure by adding --data-binary "{\"status\": \"FAILURE\"}" </Description>
              </WindowsCurlCli>
       </Attributes>
<Propertiesclass="object">
```

```
       <Properties class
object>
              <Count class="object">
                     <Default type="number">-1</Default>
                     <Description type="string">There are 3 preconditions that make Count t
aking effect: 1.Mode is set to Full. 2.Count &gt;= 0. 3.The id of signal is not specified. If so, it will be a self-increasing integer started fr om 1. For example, the id of the first signal is 1, the id of the second signal is 2, and s o on. If Count takes effect, signals with id &gt; Count will be deleted before update. The default value is -1, which means no effect. It is recommended to quote the same value with WaitCondition.Count. </Description>
                     <Immutable type="boolean">false</Immutable>
                     <Required type="boolean">false</Required>
                     <Type type="string">integer</Type>
                     <UpdateAllowed type="boolean">true</UpdateAllowed>
              </Count>
              <Mode class="object">
                     <Constraints class="array">
                            <e class="object">
                                   <AllowedValues class="array">
                                          <e type="string">Increment</e>
                                          <e type="string">Full</e>
                                   </AllowedValues>
                            </e>
                     </Constraints>
                     <Default type="string">Full</Default>
                     <Description type="string">If set to Increment, all old signals will b
e deleted before update. In this mode, WaitCondition.Count should reference an incremental value instead of a full value, such as ScalingGroupEnable.ScalingRuleArisExecuteResultNumbe rOfAddedInstances. If set to Full, no old signal will be deleted unless Count is set. In this mode, WaitCondit ion.Count should reference a full value, such as the same value with InstanceGroup.MaxAmoun t. It is recommended to use this mode with Count. Default to Full. </Description>
                     <Immutable type="boolean">false</Immutable>
                     <Required type="boolean">false</Required>
                     <Type type="string">string</Type>
                     <UpdateAllowed type="boolean">true</UpdateAllowed>
              </Mode>
       </Properties>
       <RequestId type="string">BA4C8BF3-482E-4B03-A1E3-C60DB7A95DE0</RequestId>
       <ResourceType type="string">ALIYUN::ROS::WaitConditionHandle</ResourceType>
       <SupportDriftDetection type="boolean">false</SupportDriftDetection>
</GetResourceTypeResponse>
```

`JSON` format `{`

```json
    "Attributes": {
        "CurlCli": {
            "Description": "Convenience attribute, provides curl CLI command prefix, which
can be used for signalling handle completion or failure. You can signal success by adding
```

```
--data-binary '{\"status\": \"SUCCESS\"}' , or signal failure by adding --data-binary '{\"s tatus\": \"FAILURE\"}'"
```

`},`

```json
        "PowerShellCurlCli": {
            "Description": "Convenience attribute, provides curl CLI command prefix for Pow
erShell, which can be used for signalling handle completion or failure. As this cmdlet was introduced in PowerShell 3.0, ensure the version of PowerShell satisfies the constraint. (S how the version via $PSVersionTable.PSVersion.) You can signal success by adding -Body '{\" status\": \"SUCCESS\"}' , or signal failure by adding -Body '{\"status\": \"FAILURE\"}' "
```

`},`

```json
        "WindowsCurlCli": {
            "Description": "Convenience attribute, provides curl CLI command prefix for Win
dows, which can be used for signalling handle completion or failure. As Windows does not su pport curl command, you need to install curl.exe and add it to PATH first. You can signal s uccess by adding --data-binary \"{\\\"status\\\": \\\"SUCCESS\\\"}\" , or signal failure by adding --data-binary \"{\\\"status\\\": \\\"FAILURE\\\"}\" "
```

`}` `},`

```json
    "Properties": {
        "Count": {
            "Default": -1,
            "Description": "There are 3 preconditions that make Count taking effect:\n1.Mod
e is set to Full.\n2.Count >= 0.\n3.The id of signal is not specified. If so, it will be a self-increasing integer started from 1. For example, the id of the first signal is 1, the i d of the second signal is 2, and so on.\n\nIf Count takes effect, signals with id > Count w ill be deleted before update.\nThe default value is -1, which means no effect.\nIt is recom mended to quote the same value with WaitCondition.Count.",
            "Immutable": false,
            "Required": false,
            "Type": "integer",
            "UpdateAllowed": true
```

`},`

```json
        "Mode": {
            "Constraints": [
```

`{`

```json
                    "AllowedValues": [
                        "Increment",
                        "Full"
```

`]` `}` `],`

```json
            "Default": "Full",
            "Description": "If set to Increment, all old signals will be deleted before upd
ate. In this mode, WaitCondition.Count should reference an incremental value instead of a f ull value, such as ScalingGroupEnable.ScalingRuleArisExecuteResultNumberOfAddedInstances.\n \nIf set to Full, no old signal will be deleted unless Count is set. In this mode, WaitCond ition.Count should reference a full value, such as the same value with InstanceGroup.MaxAmo unt. It is recommended to use this mode with Count.\n\nDefault to Full.",
            "Immutable": false,
            "Required": false,
            "Type": "string",
            "UpdateAllowed": true
```

`}` `},`

```
"ReqestId" "BA4C8BF3482E4B03A1E3C60DB7A95DE0"
```

```json
    "RequestId": "BA4C8BF3-482E-4B03-A1E3-C60DB7A95DE0",
    "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
    "SupportDriftDetection": false
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | ResourceTypeNotFound | The Resource Type ({name}) could not be found. | The error message returned because the specified resource type does not exist. name indicates the name of the resource type. |

#### ListResourceTypes

You can call this operation to query the list of supported resource types. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListResourceType s | The operation that you want to perform. Set the value to ListResourceTypes. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| ResourceTypes | List | ["ALIYUN::ECS::Insta nce","ALIYUN::RDS:: Instance"] | The array of resource types. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ListResourceTypes &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListResorceTpesResponse>
```

|   | <ListResourceTypesResponse> <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId> <ResourceTypes class="array"> <ResourceType type="string">ALIYUN::ACTIONTRAIL::Trail</ResourceType> <ResourceType type="string">ALIYUN::ACTIONTRAIL::TrailLogging</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::Api</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::App</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::Authorization</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::CustomDomain</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::Deployment</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::Group</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::Signature</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::SignatureBinding</ResourceTyp e> <ResourceType type="string">ALIYUN::ApiGateway::StageConfig</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::TrafficControl</ResourceType> <ResourceType type="string">ALIYUN::ApiGateway::TrafficControlBinding</Resour ceType> <ResourceType type="string">ALIYUN::ApiGateway::VpcAccessConfig</ResourceType > <ResourceType type="string">ALIYUN::BSS::WaitOrder</ResourceType> <ResourceType type="string">ALIYUN::CDN::Domain</ResourceType> <ResourceType type="string">ALIYUN::CDN::DomainConfig</ResourceType> <ResourceType type="string">ALIYUN::CEN::CenBandwidthLimit</ResourceType> <ResourceType type="string">ALIYUN::CEN::CenBandwidthPackage</ResourceType> <ResourceType type="string">ALIYUN::CEN::CenBandwidthPackageAssociation</Reso urceType> <ResourceType type="string">ALIYUN::CEN::CenInstance</ResourceType> <ResourceType type="string">ALIYUN::CEN::CenInstanceAttachment</ResourceType> <ResourceType type="string">ALIYUN::CEN::RouteEntry</ResourceType> <ResourceType type="string">ALIYUN::CS::App</ResourceType> <ResourceType type="string">ALIYUN::CS::Cluster</ResourceType> <ResourceType type="string">ALIYUN::DEBUG::Apple</ResourceType> <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType> <ResourceType type="string">ALIYUN::DEBUG::Failure</ResourceType> <ResourceType type="string">ALIYUN::DEBUG::Secret</ResourceType> <ResourceType type="string">ALIYUN::DEBUG::Update</ResourceType> <ResourceType type="string">ALIYUN::DNS::Domain</ResourceType> <ResourceType type="string">ALIYUN::DNS::DomainGroup</ResourceType> <ResourceType type="string">ALIYUN::DNS::DomainRecord</ResourceType> <ResourceType type="string">ALIYUN::ECS::AutoSnapshotPolicy</ResourceType> <ResourceType type="string">ALIYUN::ECS::BandwidthPackage</ResourceType> <ResourceType type="string">ALIYUN::ECS::Command</ResourceType> <ResourceType type="string">ALIYUN::ECS::CopyImage</ResourceType> <ResourceType type="string">ALIYUN::ECS::CustomImage</ResourceType> <ResourceType type="string">ALIYUN::ECS::DedicatedHost</ResourceType> <ResourceType type="string">ALIYUN::ECS::DeploymentSet</ResourceType> <ResourceType type="string">ALIYUN::ECS::Disk</ResourceType> <ResourceType type="string">ALIYUN::ECS::DiskAttachment</ResourceType> <ResourceType type="string">ALIYUN::ECS::ForwardEntry</ResourceType> <ResourceType type="string">ALIYUN::ECS::Instance</ResourceType> <ResourceType type="string">ALIYUN::ECS::InstanceClone</ResourceType> <ResourceType type="string">ALIYUN::ECS::InstanceGroup</ResourceType> <ResourceType type="string">ALIYUN::ECS::InstanceGroupClone</ResourceType> <ResourceType type="string">ALIYUN::ECS::Invocation</ResourceType> |   |
|---|---|---|

```
              <ResourceType type
string>ALIYUN::ECS::Invocation</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::JoinSecurityGroup</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::LaunchTemplate</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::NatGateway</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::NetworkInterface</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::NetworkInterfaceAttachment</Resource
Type>
              <ResourceType type="string">ALIYUN::ECS::NetworkInterfacePermission</Resource
Type>
              <ResourceType type="string">ALIYUN::ECS::PrepayInstance</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::PrepayInstanceGroupClone</ResourceTy
pe>
              <ResourceType type="string">ALIYUN::ECS::Route</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::SNatEntry</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::SSHKeyPair</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::SSHKeyPairAttachment</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::SecurityGroup</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::SecurityGroupClone</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::SecurityGroupEgress</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::SecurityGroupIngress</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::Snapshot</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::VPC</ResourceType>
              <ResourceType type="string">ALIYUN::ECS::VSwitch</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::AlarmTask</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::AlarmTaskEnable</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::LifecycleHook</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::ScalingConfiguration</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::ScalingGroup</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::ScalingGroupEnable</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::ScalingRule</ResourceType>
              <ResourceType type="string">ALIYUN::ESS::ScheduledTask</ResourceType>
              <ResourceType type="string">ALIYUN::FC::Function</ResourceType>
              <ResourceType type="string">ALIYUN::FC::FunctionInvoker</ResourceType>
              <ResourceType type="string">ALIYUN::FC::Service</ResourceType>
              <ResourceType type="string">ALIYUN::FC::Trigger</ResourceType>
              <ResourceType type="string">ALIYUN::KMS::Alias</ResourceType>
              <ResourceType type="string">ALIYUN::KMS::Key</ResourceType>
              <ResourceType type="string">ALIYUN::MEMCACHE::Instance</ResourceType>
              <ResourceType type="string">ALIYUN::MNS::Queue</ResourceType>
              <ResourceType type="string">ALIYUN::MNS::Subscription</ResourceType>
              <ResourceType type="string">ALIYUN::MNS::Topic</ResourceType>
              <ResourceType type="string">ALIYUN::MONGODB::Instance</ResourceType>
              <ResourceType type="string">ALIYUN::MONGODB::PrepayInstance</ResourceType>
              <ResourceType type="string">ALIYUN::MarketPlace::Image</ResourceType>
              <ResourceType type="string">ALIYUN::MarketPlace::Order</ResourceType>
              <ResourceType type="string">ALIYUN::NAS::AccessGroup</ResourceType>
              <ResourceType type="string">ALIYUN::NAS::AccessRule</ResourceType>
              <ResourceType type="string">ALIYUN::NAS::FileSystem</ResourceType>
              <ResourceType type="string">ALIYUN::NAS::MountTarget</ResourceType>
              <ResourceType type="string">ALIYUN::OSS::Bucket</ResourceType>
              <ResourceType type="string">ALIYUN::OTS::Instance</ResourceType>
              <ResourceType type="string">ALIYUN::OTS::VpcBinder</ResourceType>
              <ResourceType type="string">ALIYUN::PVTZ::Zone</ResourceType>
              <ResourceType type="string">ALIYUN::PVTZ::ZoneRecord</ResourceType>
              <ResourceType type="string">ALIYUN::PVTZ::ZoneVpcBinder</ResourceType>
```

`yp` `yp` `g` `p` `yp`

```
              <ResourceType type="string">ALIYUN::RAM::AccessKey</ResourceType>
              <ResourceType type="string">ALIYUN::RAM::AttachPolicyToRole</ResourceType>
              <ResourceType type="string">ALIYUN::RAM::Group</ResourceType>
              <ResourceType type="string">ALIYUN::RAM::ManagedPolicy</ResourceType>
              <ResourceType type="string">ALIYUN::RAM::Role</ResourceType>
              <ResourceType type="string">ALIYUN::RAM::User</ResourceType>
              <ResourceType type="string">ALIYUN::RAM::UserToGroupAddition</ResourceType>
              <ResourceType type="string">ALIYUN::RDS::Account</ResourceType>
              <ResourceType type="string">ALIYUN::RDS::AccountPrivilege</ResourceType>
              <ResourceType type="string">ALIYUN::RDS::DBInstance</ResourceType>
              <ResourceType type="string">ALIYUN::RDS::DBInstanceParameterGroup</ResourceTy
pe>
              <ResourceType type="string">ALIYUN::RDS::DBInstanceSecurityIps</ResourceType>
              <ResourceType type="string">ALIYUN::RDS::PrepayDBInstance</ResourceType>
              <ResourceType type="string">ALIYUN::REDIS::Instance</ResourceType>
              <ResourceType type="string">ALIYUN::REDIS::PrepayInstance</ResourceType>
              <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
              <ResourceType type="string">ALIYUN::ROS::WaitCondition</ResourceType>
              <ResourceType type="string">ALIYUN::ROS::WaitConditionHandle</ResourceType>
              <ResourceType type="string">ALIYUN::SAG::ACL</ResourceType>
              <ResourceType type="string">ALIYUN::SAG::ACLAssociation</ResourceType>
              <ResourceType type="string">ALIYUN::SAG::ACLRule</ResourceType>
              <ResourceType type="string">ALIYUN::SAG::CloudConnectNetwork</ResourceType>
              <ResourceType type="string">ALIYUN::SAG::SmartAccessGatewayBinding</ResourceT
ype>
              <ResourceType type="string">ALIYUN::SLB::AccessControl</ResourceType>
              <ResourceType type="string">ALIYUN::SLB::BackendServerAttachment</ResourceTyp
```

`e>`

```
              <ResourceType type="string">ALIYUN::SLB::BackendServerToVServerGroupAddition<
/ResourceType>
              <ResourceType type="string">ALIYUN::SLB::Certificate</ResourceType>
              <ResourceType type="string">ALIYUN::SLB::DomainExtension</ResourceType>
              <ResourceType type="string">ALIYUN::SLB::Listener</ResourceType>
              <ResourceType type="string">ALIYUN::SLB::LoadBalancer</ResourceType>
              <ResourceType type="string">ALIYUN::SLB::LoadBalancerClone</ResourceType>
              <ResourceType type="string">ALIYUN::SLB::MasterSlaveServerGroup</ResourceType
```

`>`

```
              <ResourceType type="string">ALIYUN::SLB::Rule</ResourceType>
              <ResourceType type="string">ALIYUN::SLB::VServerGroup</ResourceType>
              <ResourceType type="string">ALIYUN::SLS::ApplyConfigToMachineGroup</ResourceT
ype>
              <ResourceType type="string">ALIYUN::SLS::MachineGroup</ResourceType>
              <ResourceType type="string">ALIYUN::UIS::Uis</ResourceType>
              <ResourceType type="string">ALIYUN::UIS::UisConnection</ResourceType>
              <ResourceType type="string">ALIYUN::UIS::UisNode</ResourceType>
              <ResourceType type="string">ALIYUN::VPC::EIP</ResourceType>
              <ResourceType type="string">ALIYUN::VPC::EIPAssociation</ResourceType>
              <ResourceType type="string">ALIYUN::VPC::PeeringRouterInterfaceBinding</Resou
rceType>
              <ResourceType type="string">ALIYUN::VPC::PeeringRouterInterfaceConnection</Re
sourceType>
              <ResourceType type="string">ALIYUN::VPC::RouterInterface</ResourceType>
              <ResourceType type="string">ALIYUN::VPC::SnatEntry</ResourceType>
       </ResourceTypes>
```

```
</ListResourceTypesResponse>
```

`JSON` format `{`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "ResourceTypes": [
       "ALIYUN::ACTIONTRAIL::Trail",
       "ALIYUN::ACTIONTRAIL::TrailLogging",
       "ALIYUN::ApiGateway::Api",
       "ALIYUN::ApiGateway::App",
       "ALIYUN::ApiGateway::Authorization",
       "ALIYUN::ApiGateway::CustomDomain",
       "ALIYUN::ApiGateway::Deployment",
       "ALIYUN::ApiGateway::Group",
       "ALIYUN::ApiGateway::Signature",
       "ALIYUN::ApiGateway::SignatureBinding",
       "ALIYUN::ApiGateway::StageConfig",
       "ALIYUN::ApiGateway::TrafficControl",
       "ALIYUN::ApiGateway::TrafficControlBinding",
       "ALIYUN::ApiGateway::VpcAccessConfig",
       "ALIYUN::BSS::WaitOrder",
       "ALIYUN::CDN::Domain",
       "ALIYUN::CDN::DomainConfig",
       "ALIYUN::CEN::CenBandwidthLimit",
       "ALIYUN::CEN::CenBandwidthPackage",
       "ALIYUN::CEN::CenBandwidthPackageAssociation",
       "ALIYUN::CEN::CenInstance",
       "ALIYUN::CEN::CenInstanceAttachment",
       "ALIYUN::CEN::RouteEntry",
       "ALIYUN::CS::App",
       "ALIYUN::CS::Cluster",
       "ALIYUN::DEBUG::Apple",
       "ALIYUN::DEBUG::Dummy",
       "ALIYUN::DEBUG::Failure",
       "ALIYUN::DEBUG::Secret",
       "ALIYUN::DEBUG::Update",
       "ALIYUN::DNS::Domain",
       "ALIYUN::DNS::DomainGroup",
       "ALIYUN::DNS::DomainRecord",
       "ALIYUN::ECS::AutoSnapshotPolicy",
       "ALIYUN::ECS::BandwidthPackage",
       "ALIYUN::ECS::Command",
       "ALIYUN::ECS::CopyImage",
       "ALIYUN::ECS::CustomImage",
       "ALIYUN::ECS::DedicatedHost",
       "ALIYUN::ECS::DeploymentSet",
       "ALIYUN::ECS::Disk",
       "ALIYUN::ECS::DiskAttachment",
       "ALIYUN::ECS::ForwardEntry",
       "ALIYUN::ECS::Instance",
       "ALIYUN::ECS::InstanceClone",
       "ALIYUN::ECS::InstanceGroup",
"ALIYUN::ECS::InstanceGroupClone",
```

```
       ALIYUN::ECS::InstanceGroupClone,
       "ALIYUN::ECS::Invocation",
       "ALIYUN::ECS::JoinSecurityGroup",
       "ALIYUN::ECS::LaunchTemplate",
       "ALIYUN::ECS::NatGateway",
       "ALIYUN::ECS::NetworkInterface",
       "ALIYUN::ECS::NetworkInterfaceAttachment",
       "ALIYUN::ECS::NetworkInterfacePermission",
       "ALIYUN::ECS::PrepayInstance",
       "ALIYUN::ECS::PrepayInstanceGroupClone",
       "ALIYUN::ECS::Route",
       "ALIYUN::ECS::SNatEntry",
       "ALIYUN::ECS::SSHKeyPair",
       "ALIYUN::ECS::SSHKeyPairAttachment",
       "ALIYUN::ECS::SecurityGroup",
       "ALIYUN::ECS::SecurityGroupClone",
       "ALIYUN::ECS::SecurityGroupEgress",
       "ALIYUN::ECS::SecurityGroupIngress",
       "ALIYUN::ECS::Snapshot",
       "ALIYUN::ECS::VPC",
       "ALIYUN::ECS::VSwitch",
       "ALIYUN::ESS::AlarmTask",
       "ALIYUN::ESS::AlarmTaskEnable",
       "ALIYUN::ESS::LifecycleHook",
       "ALIYUN::ESS::ScalingConfiguration",
       "ALIYUN::ESS::ScalingGroup",
       "ALIYUN::ESS::ScalingGroupEnable",
       "ALIYUN::ESS::ScalingRule",
       "ALIYUN::ESS::ScheduledTask",
       "ALIYUN::FC::Function",
       "ALIYUN::FC::FunctionInvoker",
       "ALIYUN::FC::Service",
       "ALIYUN::FC::Trigger",
       "ALIYUN::KMS::Alias",
       "ALIYUN::KMS::Key",
       "ALIYUN::MEMCACHE::Instance",
       "ALIYUN::MNS::Queue",
       "ALIYUN::MNS::Subscription",
       "ALIYUN::MNS::Topic",
       "ALIYUN::MONGODB::Instance",
       "ALIYUN::MONGODB::PrepayInstance",
       "ALIYUN::MarketPlace::Image",
       "ALIYUN::MarketPlace::Order",
       "ALIYUN::NAS::AccessGroup",
       "ALIYUN::NAS::AccessRule",
       "ALIYUN::NAS::FileSystem",
       "ALIYUN::NAS::MountTarget",
       "ALIYUN::OSS::Bucket",
       "ALIYUN::OTS::Instance",
       "ALIYUN::OTS::VpcBinder",
       "ALIYUN::PVTZ::Zone",
       "ALIYUN::PVTZ::ZoneRecord",
       "ALIYUN::PVTZ::ZoneVpcBinder",
       "ALIYUN::RAM::AccessKey",
       "ALIYUN::RAM::AttachPolicyToRole",
```

`y` `,`

```
       "ALIYUN::RAM::Group",
       "ALIYUN::RAM::ManagedPolicy",
       "ALIYUN::RAM::Role",
       "ALIYUN::RAM::User",
       "ALIYUN::RAM::UserToGroupAddition",
       "ALIYUN::RDS::Account",
       "ALIYUN::RDS::AccountPrivilege",
       "ALIYUN::RDS::DBInstance",
       "ALIYUN::RDS::DBInstanceParameterGroup",
       "ALIYUN::RDS::DBInstanceSecurityIps",
       "ALIYUN::RDS::PrepayDBInstance",
       "ALIYUN::REDIS::Instance",
       "ALIYUN::REDIS::PrepayInstance",
       "ALIYUN::ROS::Stack",
       "ALIYUN::ROS::WaitCondition",
       "ALIYUN::ROS::WaitConditionHandle",
       "ALIYUN::SAG::ACL",
       "ALIYUN::SAG::ACLAssociation",
       "ALIYUN::SAG::ACLRule",
       "ALIYUN::SAG::CloudConnectNetwork",
       "ALIYUN::SAG::SmartAccessGatewayBinding",
       "ALIYUN::SLB::AccessControl",
       "ALIYUN::SLB::BackendServerAttachment",
       "ALIYUN::SLB::BackendServerToVServerGroupAddition",
       "ALIYUN::SLB::Certificate",
       "ALIYUN::SLB::DomainExtension",
       "ALIYUN::SLB::Listener",
       "ALIYUN::SLB::LoadBalancer",
       "ALIYUN::SLB::LoadBalancerClone",
       "ALIYUN::SLB::MasterSlaveServerGroup",
       "ALIYUN::SLB::Rule",
       "ALIYUN::SLB::VServerGroup",
       "ALIYUN::SLS::ApplyConfigToMachineGroup",
       "ALIYUN::SLS::MachineGroup",
       "ALIYUN::UIS::Uis",
       "ALIYUN::UIS::UisConnection",
       "ALIYUN::UIS::UisNode",
       "ALIYUN::VPC::EIP",
       "ALIYUN::VPC::EIPAssociation",
       "ALIYUN::VPC::PeeringRouterInterfaceBinding",
       "ALIYUN::VPC::PeeringRouterInterfaceConnection",
       "ALIYUN::VPC::RouterInterface",
       "ALIYUN::VPC::SnatEntry"
```

`]` `}`

### Template operations

#### ValidateTemplate

You can call this operation to validate the template that is used to create stacks. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ValidateTemplat e | The operation that you want to perform. Set the value to ValidateTemplate. |
| TemplateURL | String | No | oss://ros/templ ate/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length, and the URL can be up to 1,024 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| RegionId | String | No | cn-hangzhou | The region ID of the stack template. |
| TemplateBody | String | No | {"ROSTemplateFo rmatVersion":"20 15-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | No description | The description of the stack template. |
| Parameters | List | [{"Description": "", "Label": "param integer", _ "NoEcho": "false", "ParameterKey": "param integer", _ "Type": "Number"},{ "Description": "", "Label": "param float", _ "NoEcho": "false", "ParameterKey": "param float", _ "Type": "Number"}] | The input parameters of the stack template. The input parameters define the parameters that you must specify to create stacks based on the template. These parameters specify information about a stack, such as the username, password, and environment- related ECS instance type. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ValidateTemplate &TemplateURL=oss://ros/template/demo &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ValidateTemplateResponse>
       <Description type="string">No description</Description>
       <Parameters class="array">
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_integer</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_integer</ParameterKey>
                     <Type type="string">Number</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_float</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_float</ParameterKey>
                     <Type type="string">Number</Type>
              </Parameter>
              <Parameter class="object">
<Descriptiontype="string"></Description>
```

```
                     <Description type=string></Description>
                     <Label type="string">param_bool</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_bool</ParameterKey>
                     <Type type="string">Boolean</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_json_list</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_json_list</ParameterKey>
                     <Type type="string">Json</Type>
              </Parameter>
              <Parameter class="object">
                     <Default class="object">
                            <c class="array"></c>
                     </Default>
                     <Description type="string"></Description>
                     <Label type="string">param_has_default</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_has_default</ParameterKey>
                     <Type type="string">Json</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">UpdateVersion</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">UpdateVersion</ParameterKey>
                     <Type type="string">Number</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_str</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_str</ParameterKey>
                     <Type type="string">String</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_list</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_list</ParameterKey>
                     <Type type="string">CommaDelimitedList</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_json_dict</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_json_dict</ParameterKey>
                     <Type type="string">Json</Type>
              </Parameter>
       </Parameters>
       <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</ValidateTemplateResponse>
```

`JSON` format `{`

```json
   "Description": "No description",
   "Parameters": [
```

`{`

```json
           "Description": "",
           "Label": "param_integer",
           "NoEcho": "false",
           "ParameterKey": "param_integer",
           "Type": "Number"
```

`},` `{`

```json
           "Description": "",
           "Label": "param_float",
           "NoEcho": "false",
           "ParameterKey": "param_float",
           "Type": "Number"
```

`},` `{`

```json
           "Description": "",
           "Label": "param_bool",
           "NoEcho": "false",
           "ParameterKey": "param_bool",
           "Type": "Boolean"
```

`},` `{`

```json
           "Description": "",
           "Label": "param_json_list",
           "NoEcho": "false",
           "ParameterKey": "param_json_list",
           "Type": "Json"
```

`},` `{`

```json
           "Default": {
               "c": []
```

`},`

```json
           "Description": "",
           "Label": "param_has_default",
           "NoEcho": "false",
           "ParameterKey": "param_has_default",
           "Type": "Json"
```

`},` `{`

```json
           "Description": "",
           "Label": "UpdateVersion",
           "NoEcho": "false",
           "ParameterKey": "UpdateVersion",
           "Type": "Number"
```

`},` `{`

```json
           "Description": "",
           "Label": "param_str",
           "NoEcho": "false",
```

```json
           "ParameterKey": "param_str",
           "Type": "String"
```

`},` `{`

```json
           "Description": "",
           "Label": "param_list",
           "NoEcho": "false",
           "ParameterKey": "param_list",
           "Type": "CommaDelimitedList"
```

`},` `{`

```json
           "Description": "",
           "Label": "param_json_dict",
           "NoEcho": "false",
           "ParameterKey": "param_json_dict",
           "Type": "Json"
```

`}` `],`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| InvalidTemplate | {reason}. | 400 | The error message returned because the specified template is invalid. reason indicates the specific reason. |

#### GetTemplate

You can call this operation to query details about a template. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetTemplate | The operation that you want to perform. Set the value to GetTemplate. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | No | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| Developer Guide·API | Reference |   |   | Resource Orchestration Servic |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ChangeSetId | String | No | 1f6521a4-05af- 4975-afe9- bc4b45ad**** | The ID of the change set. |
| TemplateId | String | No | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| TemplateBody | String | {\"ROSTemplateFor matVersion\": \"2015-09-01\"} | The structure that contains the template body. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetTemplate &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```json
<GetTemplateResponse>
        <TemplateBody>{"ROSTemplateFormatVersion": "2015-09-01", "Resources": {"dummy2": {"
Type": "ALIYUN::DEBUG::Dummy", "Properties": {"Map": {"Ref": "param_has_default"}, "List": {"Ref": "param_list"}}}, "dummy": {"Type": "ALIYUN::DEBUG::Dummy", "Properties": {"Map": {" Ref": "param_json_dict"}, "String": {"Ref": "param_str"}, "List": {"Ref": "param_json_list" }, "Number": {"Ref": "param_float"}, "Bool": {"Ref": "param_bool"}, "Integer": {"Ref": "par am_integer"}}}, "nested": {"Type": "ALIYUN::ROS::Stack", "Properties": {"TemplateURL": "oss ://nested-stack/simple/nested_demo", "TimeoutMins": 16}}, "WaitConditionHandle": {"Type": " ALIYUN::ROS::WaitConditionHandle", "Properties": {"UpdateVersion": {"Ref": "UpdateVersion"} }}}, "Parameters": {"param_integer": {"Type": "Number"}, "param_float": {"Type": "Number"}, "param_bool": {"Type": "Boolean"}, "param_json_list": {"Type": "Json"}, "param_has_default" : {"Default": "{\"c\": []}", "Type": "Json"}, "UpdateVersion": {"Type": "Number"}, "param_s tr": {"Type": "String"}, "param_list": {"Type": "CommaDelimitedList"}, "param_json_dict": { "Type": "Json"}}, "Outputs": {"param_integer": {"Value": {"Ref": "param_integer"}}, "param_ float": {"Value": {"Ref": "param_float"}}, "param_bool": {"Value": {"Ref": "param_bool"}}, "param_json_list": {"Value": {"Ref": "param_json_list"}}, "param_has_default": {"Value": {" Ref": "param_has_default"}}, "param_str": {"Value": {"Ref": "param_str"}}, "CurlCli": {"Val ue": {"Fn::GetAtt": ["WaitConditionHandle", "CurlCli"]}}, "param_list": {"Value": {"Ref": " param_list"}}, "param_json_dict": {"Value": {"Ref": "param_json_dict"}}}}</TemplateBody>
        <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</GetTemplateResponse>
```

`JSON` format `{`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "TemplateBody": "{\"ROSTemplateFormatVersion\": \"2015-09-01\", \"Resources\": {\"dummy2
\": {\"Type\": \"ALIYUN::DEBUG::Dummy\", \"Properties\": {\"Map\": {\"Ref\": \"param_has_de fault\"}, \"List\": {\"Ref\": \"param_list\"}}}, \"dummy\": {\"Type\": \"ALIYUN::DEBUG::Dum my\", \"Properties\": {\"Map\": {\"Ref\": \"param_json_dict\"}, \"String\": {\"Ref\": \"par am_str\"}, \"List\": {\"Ref\": \"param_json_list\"}, \"Number\": {\"Ref\": \"param_float\"} , \"Bool\": {\"Ref\": \"param_bool\"}, \"Integer\": {\"Ref\": \"param_integer\"}}}, \"neste d\": {\"Type\": \"ALIYUN::ROS::Stack\", \"Properties\": {\"TemplateURL\": \"oss://nested-st ack/simple/nested_demo\", \"TimeoutMins\": 16}}, \"WaitConditionHandle\": {\"Type\": \"ALIY UN::ROS::WaitConditionHandle\", \"Properties\": {\"UpdateVersion\": {\"Ref\": \"UpdateVersi on\"}}}}, \"Parameters\": {\"param_integer\": {\"Type\": \"Number\"}, \"param_float\": {\"T ype\": \"Number\"}, \"param_bool\": {\"Type\": \"Boolean\"}, \"param_json_list\": {\"Type\" : \"Json\"}, \"param_has_default\": {\"Default\": \"{\\\"c\\\": []}\", \"Type\": \"Json\"}, \"UpdateVersion\": {\"Type\": \"Number\"}, \"param_str\": {\"Type\": \"String\"}, \"param_l ist\": {\"Type\": \"CommaDelimitedList\"}, \"param_json_dict\": {\"Type\": \"Json\"}}, \"Ou tputs\": {\"param_integer\": {\"Value\": {\"Ref\": \"param_integer\"}}, \"param_float\": {\ "Value\": {\"Ref\": \"param_float\"}}, \"param_bool\": {\"Value\": {\"Ref\": \"param_bool\" }}, \"param_json_list\": {\"Value\": {\"Ref\": \"param_json_list\"}}, \"param_has_default\" : {\"Value\": {\"Ref\": \"param_has_default\"}}, \"param_str\": {\"Value\": {\"Ref\": \"par am_str\"}}, \"CurlCli\": {\"Value\": {\"Fn::GetAtt\": [\"WaitConditionHandle\", \"CurlCli\" ]}}, \"param_list\": {\"Value\": {\"Ref\": \"param_list\"}}, \"param_json_dict\": {\"Value\ ": {\"Ref\": \"param_json_dict\"}}}}"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |
| 404 | TemplateNotFound | The Tempalte ({ ID }) could not be found. | The error message returned because the specified template does not exist. ID indicates the template ID. |

#### DeleteTemplate

You can call this operation to delete a stack and all of its resources. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteTemplate | The operation that you want to perform. Set the value to DeleteTemplate. |
| TemplateId | String | Yes | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the stack. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8C5D90E1-66B6- 496C-9371- 3807F8DA80A8 | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=DeleteTemplate &TemplateId=5ecd1e10-b0e9-4389-a565-e4c15efc**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteTemplateResponse>
          <RequestId>8C5D90E1-66B6-496C-9371-3807F8DA80A8</RequestId>
</DeleteTemplateResponse>
```

`JSON` format `{`

```json
    "RequestId": "8C5D90E1-66B6-496C-9371-3807F8DA80A8"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | TemplateNotFound | The Tempalte ({ ID }) could not be found. | The error message returned because the specified stack does not exist. |

#### ListTemplates

You can call this operation to query the list of one or more templates. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListTemplates | The operation that you want to perform. Set the value to ListTemplates. |
| TemplateName | String | No | MyTemplate | The name of the template. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a digit or letter. _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNumber | Long | No | 10 | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Long | No | 1 | The number of entries to return on each page. Valid values: 1 to 50. Default value: 10. |
| Tag.N.Key | String | No | TestKey | The key of tag N. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot contain http:// or https://. It cannot start with acs: or aliyun. |
| Tag.N.Value | String | No | TestValue | The value of tag N. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain http:// or https://. It cannot start with acs: or aliyun. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C3A8413B-1F16- 4DED-AC3E- 61A00718DE8A | The ID of the request. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| PageNumber | Integer | 1 | The page number of the returned page. Pages start from page 1. |
| TotalCount | Integer | 3 | The total number of templates. |
| Templates | Array of Template |   | Details about the templates. |

| esource Orchestra | tion Service |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | String | 2019-10- 15T08:17:14.000000 | The time when the template was created. |
| Description | String | test-description | The description of the template. |
| TemplateId | String | 4d4f5aa2-3260- 4e47-863b- 763fbb12**** | The ID of the template. |
| TemplateName | String | test-list-templates | The name of the template. |
| UpdateTime | String | 2019-10- 15T08:17:14.000000 | The time when the template was created. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ListTemplates &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListTemplatesResponse>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <RequestId>C3A8413B-1F16-4DED-AC3E-61A00718DE8A</RequestId>
    <Templates>
       <CreateTime>2019-10-15T08:17:15.000000</CreateTime>
       <Description>test-description-update</Description>
       <TemplateId>c8b8bd07-c488-4302-ac15-b88ef073****</TemplateId>
       <TemplateName>test-template-name-update</TemplateName>
       <UpdateTime>2019-10-15T08:17:15.000000</UpdateTime>
    </Templates>
    <Templates>
       <CreateTime>2019-10-15T08:17:15.000000</CreateTime>
       <Description>test-description</Description>
       <TemplateId>4d4f5aa2-3260-4e47-863b-763fbb12****</TemplateId>
       <TemplateName>test-list-templates-2</TemplateName>
       <UpdateTime>2019-10-15T08:17:15.000000</UpdateTime>
    </Templates>
    <Templates>
       <CreateTime>2019-10-15T08:17:14.000000</CreateTime>
       <Description>test-description</Description>
       <TemplateId>1e808bb6-c2d1-4196-98a3-3b2cb2a4****</TemplateId>
       <TemplateName>test-list-templates-1</TemplateName>
       <UpdateTime>2019-10-15T08:17:14.000000</UpdateTime>
    </Templates>
    <TotalCount>3</TotalCount>
</ListTemplatesResponse>
```

`JSON` format `{`

```json
    "PageNumber": 1,
    "PageSize": 10,
    "RequestId": "C3A8413B-1F16-4DED-AC3E-61A00718DE8A",
    "Templates": [
```

`{`

```json
            "CreateTime": "2019-10-15T08:17:15.000000",
            "Description": "test-description-update",
            "TemplateId": "c8b8bd07-c488-4302-ac15-b88ef073****",
            "TemplateName": "test-template-name-update",
            "UpdateTime": "2019-10-15T08:17:15.000000"
```

`},` `{`

```json
            "CreateTime": "2019-10-15T08:17:15.000000",
            "Description": "test-description",
            "TemplateId": "4d4f5aa2-3260-4e47-863b-763fbb12****",
            "TemplateName": "test-list-templates-2",
            "UpdateTime": "2019-10-15T08:17:15.000000"
```

`},` `{`

```json
            "CreateTime": "2019-10-15T08:17:14.000000",
            "Description": "test-description",
            "TemplateId": "1e808bb6-c2d1-4196-98a3-3b2cb2a4****",
            "TemplateName": "test-list-templates-1",
            "UpdateTime": "2019-10-15T08:17:14.000000"
```

`}` `],`

```json
    "TotalCount": 3
```

`}`

#### CreateTemplate

You can call this operation to create a template. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateTemplate | The operation that you want to perform. Set the value to CreateTemplate. |
| TemplateName | String | Yes | MyTemplate | The name of the template. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a digit or letter. _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateURL | String | No | oss://ros/templ ate/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length, and the URL can be up to 1,024 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You can specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| Description | String | No | It is a demo. | The description of the template. The description can be up to 256 characters in length. |
| TemplateBody | String | No | {"ROSTemplateFo rmatVersion":"20 15-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8C5D90E1-66B6- 496C-9371- 3807F8DA80A8 | The ID of the request. |
| TemplateId | String | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=CreateTemplate &TemplateName=MyTemplate &TemplateURL=oss://ros/template/demo &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateTemplateResponse>
          <RequestId>8C5D90E1-66B6-496C-9371-3807F8DA80A8</RequestId>
          <TemplateId>5ecd1e10-b0e9-4389-a565-e4c15efc****</TemplateId>
</CreateTemplateResponse>
```

`JSON` format `{`

```json
    "RequestId": "8C5D90E1-66B6-496C-9371-3807F8DA80A8",
    "TemplateId": "5ecd1e10-b0e9-4389-a565-e4c15efc****"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidSchema | {reason}. | The error message returned because the specified template format is invalid. reason indicates the specific reason. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidTemplateAttribut e | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is incorrect. resource indicates the resource name, and name indicates the attribute name. |
| 400 | InvalidTemplatePropert yType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is incorrect. resource indicates the resource name, and section indicates the section name. |
| 400 | InvalidTemplateReferen ce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| 400 | InvalidTemplateSection | The template section is invalid: {section}. | The error message returned because the template contains an invalid property. section indicates the section name. |
| 400 | InvalidTemplateVersion | The template version is invalid: {reason}. | The error message returned because the template version is incorrect. reason indicates the specific reason. |

#### UpdateTemplate

You can call this operation to update a template. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateTemplate | The operation that you want to perform. Set the value to UpdateTemplate. |
| TemplateId | String | Yes | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |
| TemplateURL | String | No | oss://ros/templ ate/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length, and the URL can be up to 1,024 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| TemplateName | String | No | MyTemplate | The name of the template. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a digit or letter. _ |
| Description | String | No | It is a demo. | The description of the template. The description can be up to 256 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateBody | String | No | {"ROSTemplateFo rmatVersion":"20 15-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8C5D90E1-66B6- 496C-9371- 3807F8DA80A8 | The ID of the request. |
| TemplateId | String | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=UpdateTemplate &TemplateId=5ecd1e10-b0e9-4389-a565-e4c15efc**** &TemplateURL=oss://ros/template/demo &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UpdateTemplateResponse>
          <RequestId>8C5D90E1-66B6-496C-9371-3807F8DA80A8</RequestId>
          <TemplateId>5ecd1e10-b0e9-4389-a565-e4c15efc****</TemplateId>
</UpdateTemplateResponse>
```

`JSON` format `{`

```json
    "RequestId": "8C5D90E1-66B6-496C-9371-3807F8DA80A8",
    "TemplateId": "5ecd1e10-b0e9-4389-a565-e4c15efc****"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | TemplateNotFound | The Tempalte ({ ID }) could not be found. | The error message returned because the specified template does not exist. |
| 400 | InvalidSchema | {reason}. | The error message returned because the specified template format is invalid. reason indicates the specific reason. |
| 400 | InvalidTemplateAttribut e | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is invalid. resource indicates the resource name, and name indicates the attribute name. |
| 400 | InvalidTemplatePropert yType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is invalid. resource indicates the resource name, and section indicates the section name. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidTemplateReferen ce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| 400 | InvalidTemplateSection | The template section is invalid: {section}. | The error message returned because the template contains an invalid property. section indicates the section name. |
| 400 | InvalidTemplateVersion | The template version is invalid: {reason}. | The error message returned because the template version is invalid. reason indicates the specific reason. |

#### GetTemplateSummary

You can call this operation to query information about a new or existing template. To specify the query object, you must specify one of the StackId, ChangeSetId, TemplateId, TemplateBody, and TemplateURL parameters. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetTemplateSum mary | The operation that you want to perform. Set the value to GetTemplateSummary. |
| StackId | String | No | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| esource Orchestratio | n Service |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateBody | String | No | {"ROSTemplateFo rmatVersion":"20 15-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| RegionId | String | No | cn-hangzhou | The region ID of the stack. |
| TemplateId | String | No | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| TemplateURL | String | No | oss://ros/templ ate/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length, and the URL can be up to 1,024 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Not e You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| ChangeSetId | String | No | 1f6521a4-05af- 4975-afe9- bc4b45ad**** | The ID of the change set. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | No description | The description of the stack template. |
| Metadata | Map | {"key": "value"} | The metadata that is specified in the template. |
| Parameters | List | [{"Description":"", "Label":"Name", "NoEcho":"false", "ParameterKey":"Na me", "Type":"String"}] | Details about the parameter declarations that describe the attributes of parameters. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| ResourceIdentif ierSummaries | Array of ResourceIdentif ierSummary |   | Details about the resource identifier summaries. A summary describes the resource into which you want to import other resources and the attributes that can be used to identify the resource. For example, VpcId is the identifier of the ALIYUN::ECS::VPC resource. |
| LogicalResourc eIds | List | ["Vpc"] | The logical IDs of all resources that are of the type that is specified by the ResourceType parameter. |
| ResourceIdentif iers | List | ["VpcId"] | The attributes of the resource. The attributes are used to identify the resource into which you want to import other resources. For example, VpcId is the identifier of the ALIYUN::ECS::VPC resource. |
| ResourceType | String | ALIYUN::ECS::VPC | The type of the resource. Not e You can import resources into the ALIYUN::ECS::VPC resource type. |
| ResourceTypes | List | ["ALIYUN::ECS::VPC" ] | All the resource types that are used in the template. |
| Version | String | 2015-09-01 | The version of the template. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetTemplateSummary &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &RegionId=cn-hangzhou &TemplateURL=oss://ros/template/demo &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetTemplateSummary>
          <Description>No description</Description>
          <Metadata></Metadata>
          <Parameters>
                <Description>Description of the vpc, [2, 256] characters. Do not fill or em
pty, the default is empty. </Description>
                <Label>Description</Label>
                <NoEcho>false</NoEcho>
                <ParameterKey>Description</ParameterKey>
                <Type>String</Type>
          </Parameters>
          <Parameters>
                <Description>Tags to attach to vpc. Max support 20 tags to add during creat
e vpc. Each tag with two properties Key and Value, and Key is required. </Description>
                <Label>Tags</Label>
                <MaxLength>20</MaxLength>
                <NoEcho>false</NoEcho>
                <ParameterKey>Tags</ParameterKey>
                <Type>Json</Type>
          </Parameters>
          <Parameters>
                <Description>IPv6 network cidr of the VPC. </Description>
                <Label>Ipv6CidrBlock</Label>
                <MinLength>1</MinLength>
                <NoEcho>false</NoEcho>
                <ParameterKey>Ipv6CidrBlock</ParameterKey>
                <Type>String</Type>
          </Parameters>
          <Parameters>
                <AllowedValues>True</AllowedValues>
                <AllowedValues>true</AllowedValues>
                <AllowedValues>False</AllowedValues>
                <AllowedValues>false</AllowedValues>
                <Default>false</Default>
                <Description>Whether to enable an IPv6 network cidr, the value is:False (de
fault): not turned on.True: On. </Description>
                <Label>EnableIpv6</Label>
                <NoEcho>false</NoEcho>
                <ParameterKey>EnableIpv6</ParameterKey>
                <Type>Boolean</Type>
          </Parameters>
          <Parameters>
                <Description>Resource group id. </Description>
                <Label>ResourceGroupId</Label>
                <NoEcho>false</NoEcho>
                <ParameterKey>ResourceGroupId</ParameterKey>
                <Type>String</Type>
          </Parameters>
          <Parameters>
                <Description>Display name of the vpc instance, [2, 128] English or Chinese
characters, must start with a letter or Chinese in size, can contain numbers, '' or '.', '
```

```
caactes, uststatwt
```

`a`

```
ette
```

`o`

```
ese
```

`s`

```
e,ca cota ubes,
```

`_` `o` `.``,`

```xml
-'</Description>
                <Label>VpcName</Label>
                <NoEcho>false</NoEcho>
                <ParameterKey>VpcName</ParameterKey>
                <Type>String</Type>
          </Parameters>
          <Parameters>
                <Description>
                The IP address range of the VPC in the CIDR block form. You can use the fol
lowing IP address ranges and their subnets:
                10.0.0.0/8
                172.16.0.0/12 (Default)
                192.168.0.0/16</Description>
                <Label>CidrBlock</Label>
                <NoEcho>false</NoEcho>
                <ParameterKey>CidrBlock</ParameterKey>
                <Type>String</Type>
          </Parameters>
          <RequestId>FD70598C-3F4B-4E66-9A76-67F2E2D36938</RequestId>
          <ResourceIdentifierSummaries>
                <LogicalResourceIds>Vpc</LogicalResourceIds>
                <ResourceIdentifiers>VpcId</ResourceIdentifiers>
                <ResourceType>ALIYUN::ECS::VPC</ResourceType>
          </ResourceIdentifierSummaries>
          <ResourceTypes>ALIYUN::ECS::VPC</ResourceTypes>
          <Version>2015-09-01</Version>
</GetTemplateSummary>
```

`JSON` format `{`

```json
    "Description": "No description",
    "Metadata": {},
    "Parameters": [
```

`{`

```json
            "Description": "Description of the vpc, [2, 256] characters. Do not fill or emp
ty, the default is empty.",
            "Label": "Description",
            "NoEcho": "false",
            "ParameterKey": "Description",
            "Type": "String"
```

`},` `{`

```json
            "Description": "Tags to attach to vpc. Max support 20 tags to add during create
vpc. Each tag with two properties Key and Value, and Key is required.",
            "Label": "Tags",
            "MaxLength": 20,
            "NoEcho": "false",
            "ParameterKey": "Tags",
            "Type": "Json"
```

`},` `{`

```json
            "Description": "IPv6 network cidr of the VPC.",
"Lbl"
```

`"I`

```
6CidBl
```

`k"`

```json
            "Label": "Ipv6CidrBlock",
            "MinLength": 1,
            "NoEcho": "false",
            "ParameterKey": "Ipv6CidrBlock",
            "Type": "String"
```

`},` `{`

```json
            "AllowedValues": [
                "True",
                "true",
                "False",
                "false"
```

`],`

```json
            "Default": false,
            "Description": "Whether to enable an IPv6 network cidr, the value is:False (def
ault): not turned on.True: On.",
            "Label": "EnableIpv6",
            "NoEcho": "false",
            "ParameterKey": "EnableIpv6",
            "Type": "Boolean"
```

`},` `{`

```json
            "Description": "Resource group id.",
            "Label": "ResourceGroupId",
            "NoEcho": "false",
            "ParameterKey": "ResourceGroupId",
            "Type": "String"
```

`},` `{`

```json
            "Description": "Display name of the vpc instance, [2, 128] English or Chinese c
haracters, must start with a letter or Chinese in size, can contain numbers, '_' or '.', '- '",
            "Label": "VpcName",
            "NoEcho": "false",
            "ParameterKey": "VpcName",
            "Type": "String"
```

`},` `{`

```json
            "Description": "The IP address range of the VPC in the CIDR block form. You can
use the following IP address ranges and their subnets:\n10.0.0.0/8\n172.16.0.0/12 (Default) \n192.168.0.0/16",
            "Label": "CidrBlock",
            "NoEcho": "false",
            "ParameterKey": "CidrBlock",
            "Type": "String"
```

`}` `],`

```json
    "RequestId": "FD70598C-3F4B-4E66-9A76-67F2E2D36938",
    "ResourceIdentifierSummaries": [
```

`{`

```json
            "LogicalResourceIds": [
                "Vpc"
```

`],`

```json
            "ResourceIdentifiers": [
"VpcId"
```

```
                VpcId
```

`],`

```json
            "ResourceType": "ALIYUN::ECS::VPC"
```

`}` `],`

```json
    "ResourceTypes": [
        "ALIYUN::ECS::VPC"
```

`],`

```json
    "Version": "2015-09-01"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | StackValidationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |
| 404 | TemplateNotFound | The Tempalte ({ ID }) could not be found. | The error message returned because the specified template does not exist. ID indicates the template ID. |

### Other operations

#### DescribeRegions

You can call this operation to query available regions. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |

| Developer Guide·API | Reference |   |   | Resource Orchestration Servic |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AcceptLanguage | String | No | zh-CN | The natural language that is used to filter responses. Default value: zh-CN. Valid values: zh-CN en-US ja |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of Region |   | Details about the regions. |
| LocalName | String | China (Hangzhou) | The name of the region in the local language. |
| RegionEndpoint | String | ros.aliyuncs.com | The endpoint of the region. |
| RegionId | String | cn-hangzhou | The ID of the region. |
| RequestId | String | 59F0F0A0-A637- 4292-9B91- 251EF5010913 | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=DescribeRegions &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRegionsResponse>
    <Regions>
        <Region>
            <RegionId>cn-qingdao</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Qingdao)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-beijing</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
<LocalName>China(Beijing)</LocalName>
```

```xml
            <LocalName>China (Beijing)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-zhangjiakou</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Zhangjiakou)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-huhehaote</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Hohhot)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-hangzhou</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Hangzhou)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-shanghai</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Shanghai)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-shenzhen</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Shenzhen)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-chengdu</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Chengdu)</LocalName>
        </Region>
        <Region>
            <RegionId>ap-northeast-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>Japan (Tokyo)</LocalName>
        </Region>
        <Region>
            <RegionId>ap-southeast-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>Singapore (Singapore)</LocalName>
        </Region>
        <Region>
            <RegionId>ap-southeast-2</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>Australia (Sydney)</LocalName>
        </Region>
        <Region>
            <RegionId>ap-southeast-3</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>Malaysia (Kuala Lumpur)</LocalName>
        </Region>
        <Region>
            <RegionId>ap-southeast-5</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
```

`g` `p` `y` `/` `g` `p`

```xml
            <LocalName>Indonesia (Jakarta)</LocalName>
        </Region>
        <Region>
            <RegionId>ap-south-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>India (Mumbai)</LocalName>
        </Region>
        <Region>
            <RegionId>us-east-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>US (Virginia)</LocalName>
        </Region>
        <Region>
            <RegionId>us-west-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>US (Silicon Valley)</LocalName>
        </Region>
        <Region>
            <RegionId>eu-west-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>UK (London)</LocalName>
        </Region>
        <Region>
            <RegionId>me-east-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>UAE (Dubai)</LocalName>
        </Region>
        <Region>
            <RegionId>eu-central-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>Germany (Frankfurt)</LocalName>
        </Region>
    </Regions>
    <RequestId>59F0F0A0-A637-4292-9B91-251EF5010913</RequestId>
</DescribeRegionsResponse>
```

`JSON` format `{`

```json
    "Regions": [
```

`{`

```json
            "LocalName": "China (Qingdao)"
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-qingdao"
```

`},` `{`

```json
            "localName": "China (Beijing)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-beijing"
```

`},` `{`

```json
            "localName": "China (Zhangjiakou)",
            "RegionEndpoint": "ros.aliyuncs.com",
```

`"R` `i`

```
Id"
```

`"` `h`

```
jik
```

`"`

```json
            "RegionId": "cn-zhangjiakou"
```

`},` `{`

```json
            "localName": "China (Hohhot)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-huhehaote"
```

`},` `{`

```json
            "localName": "China (Hangzhou)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-hangzhou"
```

`},` `{`

```json
            "localName": "China (Shanghai)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-shanghai"
```

`},` `{`

```json
            "localName": "China (Shenzhen)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-shenzhen"
```

`},` `{`

```json
            "LocalName": "China (Chengdu)"
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-chengdu"
```

`},` `{`

```json
            "localName": "Japan (Tokyo)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-northeast-1"
```

`},` `{`

```json
            "localName": "Singapore (Singapore)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-southeast-1"
```

`},` `{`

```json
            "localName": "Australia (Sydney)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-southeast-2"
```

`},` `{`

```json
            "localName": "Malaysia (Kuala Lumpur)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-southeast-3"
```

`},` `{`

```json
            "localName": "Indonesia (Jakarta)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-southeast-5"
```

`},` `{`

```json
            "localName": "India (Mumbai)",
"RegionEndpoint":"rosaliyuncscom"
```

```json
            RegionEndpoint: ros.aliyuncs.com,
            "RegionId": "ap-south-1"
```

`},` `{`

```json
            "localName": "US (Virginia)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "us-east-1"
```

`},` `{`

```json
            "localName": "US (Silicon Valley)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "us-west-1"
```

`},` `{`

```json
            "localName": "UK (London)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "eu-west-1"
```

`},` `{`

```json
            "localName": "UAE (Dubai)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "me-east-1"
```

`},` `{`

```json
            "LocalName": "Germany (Frankfurt)"
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "eu-central-1"
```

`}` `],`

```json
    "RequestId": "59F0F0A0-A637-4292-9B91-251EF5010913"
```

`}`

#### SignalResource

You can call this operation to send signals. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SignalResource | The operation that you want to perform. Set the value to SignalResource. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LogicalResourceId | String | Yes | WebServer | The logical ID of the resource as defined in the template. |
| Status | String | Yes | SUCCESS | The state of the signal. Failure signals can cause stack creation or update to fail. If all signals are warnings, the stack cannot be created or updated. Valid values: SUCCESS FAILURE WARNING |
| UniqueId | String | Yes | 27c7347b-352a- 4377-accf- 63d361c1**** | The unique ID of the signal. The ID must be 1 to 64 characters in length. If multiple signals are sent to a single resource, each signal must have a unique ID. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-) and underscores ( ). _ |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=SignalResource &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &LogicalResourceId=WebServer &Status=SUCCESS &UniqueId=27c7347b-352a-4377-accf-63d361c1**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SignalResourceResponse>
      <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</SignalResourceResponse>
```

`JSON` format `{`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | ResourceNotAvailable | The Resource ({name}) is not available. | The error message returned because the specified resource is unavailable. name indicates the resource name. |
| 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | The error message returned because the specified resource does not exist in the specified stack. name indicates the resource name, and stack indicates the stack name or ID. |
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. The name parameter indicates the name or ID of the stack. |

#### ListStackOperationRisks

You can call this operation to detect the resources that may face high risks caused by a stack deletion operation, and query the reason for each risk. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListStackOperatio nRisks | The operation that you want to perform. Set the value to ListStackOperationRisks. |
| OperationType | String | Yes | DeleteStack | The operation type to be detected. The DeleteStack value specifies to detect resources that may face high risks caused by a stack deletion operation. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RamRoleName | String | No | test-role | The name of the RAM role. If you specify a RAM role, ROS creates stacks based on the permissions granted to the RAM role and uses the credentials of the RAM role to call API operations. If you do not specify a RAM role, ROS creates stacks based on the permissions of the current account. The RAM role name can be up to 64 characters in length. |
| RetainAllResource s | Boolean | No | false | Specifies whether to retain all resources in the stack. Default value: false. Valid values: true: The resources in the stack are retained. false: The resources in the stack are not retained. Not e This parameter is valid only when the OperationType parameter is set to DeleteStack. |
| RetainResources. N | RepeatLi st | No | WebServer | The list of resources to retain. Not e This parameter is valid only when the OperationType parameter is set to DeleteStack. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 72108E7A-E874- 4A5E-B22C- A61E94AD12CD | The ID of the request. |
| RiskResources | Array of Resource |   | The resources that face high risks caused by the stack deletion operation. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | NoPermission | The error code that is returned when the risk detection fails. This parameter is not returned when the risk detection succeeds. |
| LogicalResourc eId | String | MySG | The logical ID of the resource. It is the resource name defined in the template. |
| Message | String | You are not authorized to complete this action. | The error message that is returned when the risk detection fails. This parameter is not returned when the risk detection succeeds. |
| PhysicalResourc eId | String | sg- bp1dpioafqphedg9* *** | The physical ID of the resource. |
| Reason | String | There are some ECS instances (i- bp18el96s4wq635e* ***) depending on the security group. | The reason for the risk. |
| RequestId | String | DF4296CF-F45F- 4845-A72B- BE617601DB25 | The request ID that is returned when the risk detection fails. This parameter is not returned when the risk detection succeeds. |
| ResourceType | String | ALIYUN::ECS::Securi tyGroup | The type of the resource. |
| RiskType | String | Referenced | The type of the risk. Valid values: Referenced: The current resource is referenced by other resources. MaybeReferenced: The current resource may be referenced by other resources. AdditionalRiskCheckRequired: An additional risk detection is required for nested stacks. |

Examples Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ListStackOperationRisks &OperationType=DeleteStack &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListStackOperationRisks>
    <RequestId>72108E7A-E874-4A5E-B22C-A61E94AD12CD</RequestId>
    <RiskResources>
       <LogicalResourceId>MySG</LogicalResourceId>
       <PhysicalResourceId>sg-bp1dpioafqphedg9****</PhysicalResourceId>
       <ResourceType>ALIYUN::ECS::SecurityGroup</ResourceType>
       <Reason>There are some ECS instances (i-bp18el96s4wq635e****) depending on the secur
ity group. </Reason>
       <RiskType>Referenced</RiskType>
    </RiskResources>
</ListStackOperationRisks>
```

`JSON` format `{`

```json
  "RequestId": "772108E7A-E874-4A5E-B22C-A61E94AD12CD",
  "RiskResources": [
```

`{`

```json
      "LogicalResourceId": "MySG",
      "PhysicalResourceId": "sg-bp1dpioafqphedg9****",
      "ResourceType": "ALIYUN::ECS::SecurityGroup",
      "Reason": "There are some ECS instances (i-bp18el96s4wq635e****) depending on the sec
urity group.",
      "RiskType": "Referenced"
```

`}` `]` `}`

## Appendixes

### Call the ASAPI gateway

You can use the Apsara Stack API (ASAPI) gateway to call API operations of most Apsara Stack services. This topic describes how to call API operations by using the ASAPI gateway and provides links to references. Flowchart Procedure
1. Obtain ASAPI SDK.
Before you use ASAPI to call an API operation, you must obtain ASAPI SDK. For more information, see Obtain ASAPI SDK.
2. Obtain the endpoint of ASAPI. For more information, see Obtain the endpoint of ASAPI .
3. Obtain an AccessKey pair.
Obtain the AccessKey pair that is required when you call an API operation. Not e We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services.
4. Obtain the region ID.
Obtain the region ID that is required when you call an API operation.
5. Obtain the organization ID and resource set ID.
You must call an API operation to obtain an organization ID. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management C onsole Developer Guide. You must call an API operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Con sole Developer Guide. Not e When you call an API operation, you can specify the organization ID and resource set ID by using the <x-acs-organizationid> and <x-acs-resourcegroupid> parameters. This allows you to query specified resources. If you do not set the <x-acs-organizationid> parameter, the organization to which the current user belongs is used by default. If you do not set the <x-acs-resourcegroupid> parameter, it is empty by default. If you specify a resource set ID, you must also specify an organization ID.
6. Refer to API references.
Obtain the developer guide of the cloud service that you want to use. You can learn the features of API operations and how to call the API operations. For more information, see Use developer guides.
7. Use ASAPI SDK to call API operations.
After you complete the preceding preparations, you can use ASAPI SDK to call API operations. For more information about how to use SDKs for different languages, see the relevant topics. The following example shows how to call the DescribeInstances operation of Elastic Compute Service (ECS) by using SDK for Java:

```java
public static void main(String[] args) {
    ASClient client = new ASClient();
    // Specify the caller. The caller is recorded in logs.
    client.setSdkSource("autoTest");
    // Configure request parameters.
    Map<String, Object> parameters = new HashMap<String, Object>();;
    parameters.put("Product", "Ecs");// Specify the POP code, which is the same as the
POP code in the corresponding API directory.
    parameters.put("Action", "DescribeInstances"); // Specify the name of the API opera
tion. Use the same case as the case in the corresponding API directory.
    parameters.put("Version", "2014-05-26"); // Specify the API version.
    // Specify the region ID that you obtained.
    parameters.put("RegionId", "xxx");
    // Specify the AccessKey ID and AccessKey secret that you obtained.
    parameters.put("AccessKeyId", "xxx");
    parameters.put("AccessKeySecret", "xxx");
    // Add the parameters based on the API documentation. Take note that the parameters
are case-sensitive.
    parameters.put("PageNumber",1);
    parameters.put("PageSize",10);
    Map<String,String> headers=new HashMap<>();
    // Specify the organization ID in the Apsara Uni-manager Management Console.
    headers.put("x-acs-organizationid","3");
    // Specify the resource set ID in the Apsara Uni-manager Management Console.
    //headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>");
    // Specify the endpoint of ASAPI.
    String endpoint="https://public.asapi.xxx.xxx/asapi/v3";
    // Initiate a request.
    String result = client.doPost(endpoint,headers, parameters);
    // Display the results.
    System.out.println(JSONObject.toJSONString(JSONObject.parseObject(result), Serializ
erFeature.PrettyFormat));
```

`}`

### Use the ASAPI gateway to make

API calls

#### Obtain an endpoint of ASAPI

This topic describes three methods that you can use to obtain an endpoint of Apsara Stack API (ASAPI) and how to verify the endpoint. Methods Method 1: Use Registration Vars of Services to obtain an endpoint
1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click Product s. iii. Choose Plat f orms > Apsara Inf rast ruct ure Management Framework.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for `Registration Vars of Services` and click the report name.
4. On the Regist rat ion Vars of Services page, click the
icon next to Service and search for `asapi` .
5. Find the asapi service, right-click in the Service Regist rat ion column, and then select Show More
from the shortcut menu. In the Det ails dialog box, obtain the value of asapi.public.endpoint .
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
2. Replace <internet-domain> with the root domain of your Apsara Stack service. To obtain the
root domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internetdomain parameter instead of the intranet-domain parameter. If the region value is `cn-****-****-d01` and the int ernet -domain value is `inter.****.****.com` , the following endpoint is used:

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

Not e ${global:region} and ${global:intranet-domain} are variables. You must replace them with the actual values that you obtained. Procedure To obtain the actual values of the variables ${global:region}, ${global:internet-domain}, and ${global:intranet-domain}, perform the following operations:
1. In the address bar, enter the region-id.aso.intranet-domain-id.com URL and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password used to log on to the Apsara Uni-manager Operations Console from the deployment personnel or an administrator. When you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password is 10 to 20 characters in length.
3. Click Log On to log on to the Apsara Uni-manager Operat ions Console.
4. In the top navigation bar, choose Product s > Plat f orms > Apsara Inf rast ruct ure Management
Framework to go to Apsara Infrastructure Management.
5. In the left-side navigation pane, choose Operat ions > Clust er Operat ions.
6. On the Clust ers page, enter ascm-A in the Cluster search box to find the cluster. Click the cluster
name.
7. On the Clust er Dashboard page, click Operat ions Menu > Conf igurat ion Files.
8. In the File List window on the left side of the Clust er Conf igurat ion page, click kv.conf , click the
file content in the right window, and then press Ctrl + F. Search for region, internet-domain, and intranet-domain. Replace ${global:region} with the obtained region value, ${global:internet-domain} with the obtained internet-domain value, and ${global:intranet-domain} with the obtained intranet-domain value. Not e ${global:} is not included in the endpoint of ASAPI that you can use.

#### Obtain Apsara Stack SDKs

Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. Public environment If you are using the public environment, you can go to the Apsara Stack documentation page and download the Apsara Stack SDKs in the Ot her Resources section at the lower part of the page. Private environment If you are using the private environment, you must switch to the public environment and then go to the Apsara Stack documentation page. At the lower part of the page, download the Apsara Stack SDKs in the Ot her Resources section. Apsara Stack SDK for Java

| greopId | artifactId | Version |
|---|---|---|
| com.alibaba | alicrypto-java-aliyun | 1.0.4 |
| com.alibaba | fastjson | 1.2.68 |

| D | eveloper Guide·Appendixes |   | Resource Orchestration Servic | e |
|---|---|---|---|---|

| greopId | artifactId | Version |
|---|---|---|
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

| Paramet er | T ype | Requi red | Example | Descript ion |
|---|---|---|---|---|
| Act ion | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::1234567 89012****:role/ad minrole | The Apsara Stack Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Apsara Stack tenant account. |

| Paramet er | T ype | Requi red | Example | Descript ion |
|---|---|---|---|---|
| RoleSessionNam e | String | Yes | alice | The name of the role session. Set this parameter based on your business requirements. In most cases, you can set this parameter to the identity of the user who calls the operation. For example, specify a username. In ActionTrail logs, you can distinguish the users who assume the same RAM role to perform operations based on the value of the RoleSessionName parameter. This way, you can perform user-specific auditing. The name must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource ": ["*"]}],"Version":"1 "} | The policy that specifies the permissions of the STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. The policy must be 1 to 1,024 characters in length. |

Responses

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| Request Id | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | The ID of the request. |
| Credent ials | None | None | The access credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuKg5 U1**** | The AccessKey ID. |

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| AccessKeySecret | String | wyLTSmsyPGP1ohvv w8xYgB29dlGI8KMiH2 pK**** | The AccessKey secret. |
| Securit yT oken | String | ******** | The security token. |
| Expirat ion | String | 2015-04- 09T11:52:19Z | The time when the STS token expires. |
| AssumedRoleUser | None | None | The temporary identity that you use to assume the RAM role. |
| Arn | String | acs:ram::123456789 012****:role/adminr ole/alice | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495**** :alice | The ID of the temporary identity that you use to assume the RAM role. |

Examples Add Project Object Model (POM) dependencies The Alibaba Cloud core library is required. Perform the following steps to add the Alibaba Cloud core library to POM:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

Call an API operation to obtain the STS AccessKey 3-tuple. In the following sample code, the `Sts::AssumeRole::2015-04-01` operation is used to obtain the 3tuple.

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; importcomaliyuncsexceptionsClientException;
```

```java
import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKe
yID>", "<yourAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        // Replace "sts.aliyuns.com" with the actual endpoint of STS. In most cases, the en
dpoint is in the following format: sts-vpc.${global:region}.${global:internet-domain}.
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        // Replace "<yourRoleSessionName>" with the alias that you specify for the current
role session.
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
        // Replace "<yourRoleArn>" with the actual ARN that you obtained for the RAM role i
n the preceding step.
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
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: " + st
sToken);
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

`}` `}` `}` `}` Call examples In the following sample code, the `DescribeZones` operation in Elastic Compute Service (ECS) is used.

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
        // Replace "<yourRegionID>" with the actual region ID.
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the AccessKey I
D and secret in the 3-tuple that you obtained in the preceding step.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAcces
sKey>", "<yourStsAccessKeySecret>");
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
        // Replace "<yourStsToken>" with the STS token in the 3-tuple that you obtained in
the preceding step.
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
```

```java
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

`}` `}` `}` Error codes

| Ht t pCode | Error code | Error message | Descript ion |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleAr n | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleSe ssionName | The parameter RoleSessionName is wrongly formed. | The error message returned because the value of the RoleSessionName parameter is in an invalid format. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| 400 | InvalidParameter.Durati onSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the Durat ionSeconds parameter is invalid. The minimum value is 900, and the maximum value is equal to the value of the MaxSessionDurat ion parameter. |

| Ht t pCode | Error code | Error message | Descript ion |
|---|---|---|---|
| 400 | InvalidParameter.PolicyG rammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the policy is invalid. |
| 400 | InvalidParameter.PolicyS ize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error occurred. |
